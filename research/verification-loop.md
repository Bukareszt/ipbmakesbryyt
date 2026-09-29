# Verification loop

## Round 1: realism

Reviewer scope: visible text of §2, §3, §5, §6, §7, §8, §9, §10 (state on 2026-09-28). Checked against public sources from 2024 to 2026. Fixes are written in the plan's style (plain first person, no semicolons, no dashes, no numeric thresholds).

### What exists and is usable (verified)

- NWM: code and retrained weights public (github.com/facebookresearch/nwm, huggingface.co/facebook/nwm). Non-commercial licence. Note that NWM predicts in the latent space of an image autoencoder, not in raw pixels.
- Ctrl-World: code and DROID checkpoint public (github.com/Robert-gyj/Ctrl-World, huggingface.co/yjguo/Ctrl-World). Training used one or two nodes of 8 A100/H100, so fine-tuning is within an academic allocation.
- V-JEPA 2 and V-JEPA 2-AC: weights public (facebookresearch/vjepa2, `vjepa2_ac_vit_giant`). The AC predictor exists only on the ViT-g encoder, which is heavy to fine-tune and slow to plan with.
- DINO-WM: code public, but its released environments are simulated. Training it on RECON, SCAND or BridgeData V2 is new engineering work.
- [18] Reconstruction or Semantics: code and models public (github.com/chandar-lab/semantic-wm), an action-conditioned latent diffusion world model on BridgeData V2 with swappable encoders (SD3 VAE, Cosmos, VA-VAE against V-JEPA 2.1, Web-DINO, SigLIP 2). This is a ready testbed for H1.
- Isaac Lab 3.0: kit-less mode with Newton physics and the Newton Warp renderer exists, gives only RGB and depth, and needs no RT cores. Status is early access (v3.0.0-EA, September 2026), after two betas.
- Cosmos-Transfer2.5: needs Hopper or newer with 80 GB (so H100 yes, A100 no), about five minutes per 121-frame clip on one H100.
- SIMPLER: runs on SAPIEN/ManiSkill with Vulkan. Headless Vulkan on H100 nodes has open, unresolved reports (haosulab/SAPIEN issue 250, IsaacLab issue 4271), so it depends on the cluster drivers.
- Open-loop action error against closed-loop success: weakly correlated in recent work (Critical Interval MSE, arXiv 2606.29898, and earlier robomimic findings).
- Relevant work missing from §6: SimDist (Levy et al., arXiv 2603.15759), which pretrains a world model in simulation and adapts it to the real world with little data on contact-rich manipulation and quadruped locomotion. Also Wang et al. (arXiv 2510.02538), sim-pretrained world models fine-tuned on limited real data.

### Findings

**F1. §9 and §5: "real performance" is not real performance. Severity: high.**
Quoted: "I will call this real performance throughout." and in §5 "and this can be judged by success on real data alone."
Problem: without a robot, a policy cannot succeed on real data. Action matching on recordings is open-loop and correlates weakly with closed-loop success. SIMPLER success is success in a simulator. Calling both "real performance" and "success on real data" overstates what is measured and will draw reviewer objections.
Fix (§9): "I will call this performance on real data. It is measured on recordings or in SIMPLER and is not success on a real robot, and I will state this with every result."
Fix (§5): "and I will judge this by observable results on recorded real data and, where access allows, on a real robot."

**F2. §7 RQ1 and §9: a baseline is missing that the metric favours. Severity: high. Most likely RQ1 failure point.**
Quoted: "Every policy is then evaluated by its real performance on the same task".
Problem: a policy trained directly on the real data used to build the world model will score well on held-out action matching by construction. The benefit of imagined data (coverage, recovery from own mistakes) shows mainly in closed loop, which only SIMPLER gives. Without this baseline, RQ1 results cannot show that training inside the world model helps at all, and the pixel against feature comparison may be lost in noise.
Fix: "As a baseline I will train the same policy directly on the real data used to build the world model, and I will report whether imagined data helps beyond it, mainly in SIMPLER, where the policy acts in closed loop."

**F3. §7 H1 and §9: the comparison changes many things at once, and the rival cannot be checked for feature models. Severity: high.**
Quoted: "For navigation I will use NWM [3] as the world model that predicts video, train DINO-WM [16] on the same navigation data as the world model that predicts features" and "I will measure action following for the video models in one observable way".
Problem: NWM against DINO-WM, and Ctrl-World or Cosmos against V-JEPA 2-AC, differ in architecture, size, pretraining data and in how the imagined trajectories are made (rollouts against planning towards goal images). This breaks "one choice at a time". NWM and Cosmos also predict autoencoder latents, not pixels. Action following is measured only for video models, so the rival explanation of H1 cannot be separated from the prediction target.
Fix (§9): "To change only the prediction target, I will train the same predictor on the same data to predict either the latents of an image autoencoder trained to reconstruct pixels or the features of an encoder pretrained on real video, following the setup of [18], whose code is public. The large video and feature models will serve as a second check. For feature models I will measure action following on frames from a decoder trained after the world model, as in DINO-WM, so that the same test applies to every model."
Fix (§7 H1): replace "predicts pixels" with "predicts the latents of an image autoencoder trained to reconstruct pixels".

**F4. §7 RQ2 and §9: simulated scenes do not match the real recordings. Severity: high. Most likely RQ2 failure point.**
Quoted: "I will generate navigation and manipulation data in Isaac Lab ... I will measure how well each world model predicts held-out real recordings from the datasets above".
Problem: a world model trained on Isaac Lab scenes has not seen the rooms, objects and outdoor terrain of DROID, RECON or SCAND. Its PSNR, LPIPS and FVD on those recordings will be dominated by content mismatch, not by the appearance or physics choices RQ2 compares, so all variants may look equally bad. The only public scenes built to match real recordings are the BridgeData V2 scenes in SIMPLER (ManiSkill). There is no comparable simulated twin for RECON or SCAND.
Fix: "For RQ2 I will generate simulation data in scenes that match the real recordings, mainly the BridgeData V2 scenes rebuilt in SIMPLER, and use Isaac Lab to add randomized variations of them. For navigation I will study RQ2 only if I find simulated scenes close to the real recordings, and otherwise treat it as manipulation only."

**F5. Whole plan: scope is too wide for one student in three research years. Severity: high.**
Quoted (§5): "across two tasks of equal weight, robot navigation and robotic manipulation" and §9 lists NWM, DINO-WM, V-JEPA 2-AC, Ctrl-World, Cosmos-Predict, Isaac Lab, Cosmos Transfer, SIMPLER, ManiSkill, Habitat, four datasets.
Problem: four RQs in two domains with about five world models, two simulators, photorealistic transfer and continued pretraining is several PhDs of engineering. Navigation also has no closed-loop proxy, so "equal weight" cannot be delivered with equal evidence.
Fix (§5): "I will study manipulation as the main task and check the main results in robot navigation."
Fix (§9): "I will answer RQ1 to RQ3 mainly on manipulation with BridgeData V2, where SIMPLER gives a closed-loop check, and use navigation for RQ1 and as the second task in RQ4. For each task I will use one world model that predicts video and one that predicts features."

**F6. §6 and §9: SIMPLER and rank correlation are stated as stronger evidence than they are. Severity: medium.**
Quoted (§6): "The rank correlation between success in the simulator and real success is the accepted indicator of how useful a simulator is, and I will use it with the stand-in for real performance described in section 9." (§9): "by its success in SIMPLER, which ranks policies in nearly the same order as real runs."
Problem: SIMPLER reported agreement for the specific generalist policies it tested, with fewer policies on the WidowX setup. It has not been validated for policies trained on imagined data. A rank correlation between success inside a world model and an offline action-matching score is not an established indicator.
Fix (§6): "The rank correlation between success in the simulator and real success is a common indicator of how useful a simulator is, and I will use it with SIMPLER success as the stand-in."
Fix (§9): "by its success in SIMPLER, which ranked the policies tested in its study in nearly the same order as real runs, although it was not tested on policies trained in world models."

**F7. §9: SIMPLER and Isaac Lab may not render on the cluster. Severity: medium.**
Quoted: "so it should run on H100 GPUs. I will check this in the first weeks of cluster access."
Problem: the Isaac Lab check is already planned, which is good. SIMPLER is the only closed-loop proxy and relies on Vulkan, which has open failure reports on headless H100 nodes. Isaac Lab 3.0 is still an early access release.
Fix: "Isaac Lab 3.0 is still an early access release, and SIMPLER also needs graphics drivers that some clusters lack, so I will check both in the first weeks and run SIMPLER on a workstation GPU if the cluster cannot render it."

**F8. §9: Cosmos Transfer cost is not stated. Severity: medium.**
Quoted: "I will drive Cosmos Transfer [13] with these depth images to add photorealistic appearance to the renderings."
Problem: Cosmos-Transfer2.5 needs H100 class GPUs with large memory and takes several GPU minutes per short clip. Transferring a full simulation dataset for every RQ2 variant is expensive, and A100 nodes cannot run it.
Fix: "Cosmos Transfer needs H100 GPUs and several GPU minutes per short clip, so I will transfer a fixed subset of the simulated data once, reuse it across all variants and state its size."

**F9. §7 RQ3 and §9: the design is large and one setting change is a different robot. Severity: medium. Most likely RQ3 failure point.**
Quoted: "continue their pretraining on simulation data, on real robot data and on both, with and without the objective from RQ2" and "the change from the Franka to the WidowX setup".
Problem: continued pretraining of the V-JEPA 2 ViT-g encoder is costly, and six pretraining variants times several real data amounts times seeds times two tasks is large. At small amounts of real data the differences between variants are likely to be smaller than the spread between seeds. Franka to WidowX changes the action space and camera, which is an embodiment change rather than a new setting, and it can only be checked offline or in SIMPLER.
Fix: "I will continue pretraining only the smaller released encoders and compare the variants on the task where SIMPLER gives a closed-loop check. I will treat the change from the Franka to the WidowX setup as an optional extra test."

**F10. §7 RQ4 and H4: "unchanged settings" is undefined and there is no rival. Severity: medium. Most likely RQ4 failure point.**
Quoted: "H4. The choices that work best in navigation, with unchanged settings, also give a gain in manipulation and in unseen scenes."
Problem: the two tasks use different world models, policies and performance measures (path closeness against SIMPLER success and action matching), so settings cannot be unchanged and gains cannot be compared in size. H4 has no rival explanation, unlike H1 to H3.
Fix: "I will call a choice general if it improves performance on real data over the same baseline in both tasks, each measured in its own way, and I will not compare the size of the gains across tasks. The rival explanation is that a gain in one task comes from the data of that task, such as the scene diversity of its recordings, rather than from the representation choice."

**F11. §6: two directly relevant works are missing and the gap statements for RQ2 and RQ3 are too broad. Severity: medium.**
Quoted: "I have not found in my search a controlled study of which representation learning choices ... make a world model trained on simulation data predict real recordings well" and "How the representation of a world model, and of the policy trained in it, should be pretrained so that the fewest real samples are needed later is, as far as my search shows, still open."
Problem: SimDist (arXiv 2603.15759) pretrains world models in simulation and adapts them to the real world with limited data, on manipulation and locomotion with real robots. Wang et al. (arXiv 2510.02538) pretrain world models in simulation and fine-tune on limited real data. A reviewer who knows them will read the gap statements as unaware.
Fix: add "SimDist [x] and Wang et al. [y] pretrained world models in simulation and adapted them to real robots with little real data. I have not found a study that compares the representation learning choices listed above in the same setting." (The student should read both papers to confirm what they do not compare before adding the second sentence.)

**F12. §6: [18] is described as more than it did, and it overlaps RQ1. Severity: medium.**
Quoted: "A comparison of six encoders as the latent space of a world model on real manipulation data found that the encoders with the best pixel scores were not the ones that gave the best policies [18]."
Problem: [18] rolled out a fixed OpenVLA policy inside each world model and judged success with vision-language models. It did not train policies inside the models or test them on real data. Its setup (BridgeData V2, reconstruction against semantic encoders) is close to RQ1, so §6 should say what RQ1 adds.
Fix: "A comparison of six encoders as the latent space of a world model on BridgeData V2 found that semantic encoders gave better results than encoders trained to reconstruct pixels when a fixed policy was evaluated inside the model [18]. It did not train policies inside the models or test them on real data, which is what RQ1 adds."

**F13. §9: the navigation measure rewards imitation, not reaching the goal. Severity: medium.**
Quoted: "For navigation, where no such simulator exists, real performance is the closeness of the planned path to the recorded one."
Problem: a policy that finds a different valid path is penalized, and RECON and SCAND have no success labels. This is a weaker proxy than in manipulation.
Fix: "For navigation, where no such simulator exists, I will report how close the planned path is to the recorded one and whether its end point reaches the goal, and I will state that this measure rewards imitation of the recorded path."

**F14. §5: [7] is used to support a claim it does not test. Severity: low.**
Quoted: "A policy that succeeds in the world model can therefore fail on a real robot. Even a policy built on a video world model and trained only on synthetic demonstrations succeeded in about a third of the trials on a real robot arm in the first such study I have found [7]."
Problem: [7] trained a world action model on physics simulator demonstrations and did not measure success inside a world model. It supports the simulation to reality gap in general, not the gap between imagined and real success. The paper itself presents the result as a positive first transfer.
Fix: "A world action model built on a video model and trained only on demonstrations from a physics simulator succeeded in about a third of the trials on a real robot arm in the first such study I have found [7]." Keep it separate from the "therefore" sentence.

**F15. §7 H1: the mechanism is not testable without latent analysis. Severity: low.**
Quoted: "because such features leave out details that differ between imagined and real frames."
Problem: the owner excluded latent-space measurement, so this cause cannot be checked. It should be stated as an expectation, not as the tested claim.
Fix: "I expect this because such features are trained to leave out detail that cannot be predicted, but I will test only the observable prediction."

**F16. §7 H2: a second rival is missing. Severity: low.**
Quoted: "The rival explanation is that the gap comes mainly from the simulated physics".
Problem: the pairing objective makes simulated frames match Cosmos Transfer frames, not real ones. If the transferred frames still differ from real frames, neither use of them helps, whatever the physics.
Fix: add "A second rival is that the photorealistic frames still differ from real ones, so that neither use of them helps."

**F17. §9: unseen DROID recordings may not exist. Severity: low.**
Quoted: "such as BridgeData V2 and recordings added to DROID after their release".
Problem: I could not confirm that DROID has recordings added after Ctrl-World and V-JEPA 2-AC were trained. Without them, the Franka test set is not clearly unseen.
Fix: "such as BridgeData V2 and other public Franka recordings that these models did not see".

**F18. §8: the first contribution is worded more strongly than the evidence will be. Severity: low.**
Quoted: "evidence on which choices ... decide whether a policy trained inside a world model built from real data works on real inputs."
Problem: without a robot, the evidence will be about performance on recorded data and in SIMPLER. "Decide" also claims causes beyond what controlled comparisons on proxies show.
Fix: "evidence on which choices ... affect how well a policy trained inside a world model built from real data performs on recorded real data and in SIMPLER."

**F19. §3: RQ2 has too little time for its pipeline. Severity: low.**
Quoted: semester 4 "First experiments on world models trained on simulation data (RQ2)".
Problem: the simulation, Cosmos Transfer and matched scene pipeline takes months to build. It starts in the same semester as the first paper.
Fix (semester 3): add "and building the pipeline for simulation data and its photorealistic transfer".

### Remaining latent-space operations

None of the excluded operations remain. The pairing objective in RQ2 and H2 is an invariance training objective judged by observable results, which the owner allowed. The only borderline items are the H1 mechanism wording (F15) and measuring action following for feature models, which F3 routes through a decoder so that it stays in image space.

### Most likely failure point per RQ

- RQ1: the offline real-data measure cannot separate the world model variants, or cannot show a gain over a policy trained directly on the same real data (F1, F2).
- RQ2: simulated scenes do not match the real recordings, so prediction scores reflect content mismatch rather than the compared choices (F4).
- RQ3: differences between pretraining variants are smaller than the spread between seeds at small amounts of real data, and the design is too large to run with enough seeds (F9).
- RQ4: the tasks use different models and measures, so "unchanged settings" and "the same gain" cannot be defined (F10).

### Sources

- [NWM code](https://github.com/facebookresearch/nwm), [NWM weights](https://huggingface.co/facebook/nwm)
- [Ctrl-World code](https://github.com/Robert-gyj/Ctrl-World), [Ctrl-World weights](https://huggingface.co/yjguo/Ctrl-World)
- [V-JEPA 2 code and weights](https://github.com/facebookresearch/vjepa2)
- [Reconstruction or Semantics, arXiv 2605.06388](https://arxiv.org/abs/2605.06388), [semantic-wm code](https://github.com/chandar-lab/semantic-wm)
- [Isaac Lab releases](https://github.com/isaac-sim/IsaacLab/releases), [Isaac Lab 3.0 EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA), [H100 camera issue 4271](https://github.com/isaac-sim/IsaacLab/issues/4271)
- [Cosmos-Transfer2.5 inference](https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/main/docs/inference.md), [Cosmos-Transfer2.5-2B](https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B)
- [SAPIEN headless H100 issue 250](https://github.com/haosulab/SAPIEN/issues/250)
- [Critical Interval MSE, arXiv 2606.29898](https://arxiv.org/abs/2606.29898)
- [SimDist, arXiv 2603.15759](https://arxiv.org/abs/2603.15759), [Wang et al., arXiv 2510.02538](https://arxiv.org/abs/2510.02538)
- [Efficient sim-to-real WAM, arXiv 2606.31101](https://arxiv.org/abs/2606.31101), [DreamZero, arXiv 2602.15922](https://arxiv.org/abs/2602.15922), [SkyJEPA, arXiv 2606.23444](https://arxiv.org/abs/2606.23444)

## Round 2: realism

Reviewer scope: visible text of §2, §3, §5, §6, §7, §8, §9, §10 after the round 1 fixes (state on 2026-09-28). I checked each round 1 finding against the current text and looked for new problems that the fixes introduced. Fixes are in the plan's style.

### Status of round 1 findings

F1, F2, F5, F6, F8, F10, F11, F12, F13, F14, F15, F16, F17, F18 and F19 are resolved in the text. F3, F4, F7 and F9 are resolved in wording, but the fixes created the new problems R1 to R5 below.

### What I verified

- [18] code (chandar-lab/semantic-wm): one DiT predictor with causal attention and action conditioning, the same for every encoder. Encoders include SD3 VAE, Cosmos, VA-VAE, DINOv2 RAE, SigLIP 2, Web-DINO and V-JEPA 2.1. Semantic features of 768 to 1280 dimensions are first compressed by a trained adapter to a 96 dimensional latent, and pixels are recovered by a lightweight CNN decoder. Training scripts for adapters and the world model are released. So swapping the prediction target on one predictor is supported, as §9 says.
- RAE-NWM (arXiv 2603.09241, code github.com/20robo/raenwm): a navigation world model in the space of dense DINOv2 features, compared with NWM on SACSoN, RECON and SCAND, trained on two A800 GPUs in about two days. It plans with CEM and trains no policy. It is not cited in §6.
- NWM itself was trained with far more compute (CDiT XL), so retraining its predictor twice from scratch is not cheap.
- ManiSkill 3 contains only four Bridge digital twins (carrot on plate, spoon on towel, stack cubes, eggplant in basket) in two scenes. They are evaluation twins that overlay a real photograph of the background (green screen) and ship without demonstrations.
- Isaac Lab 3.0 is at v3.0.0 EA (early access), released in September 2026 after two betas. §9 says "in beta".
- Ctrl-World generated imagined trajectories by rolling out a policy in the world model, and DreamGen by prompting the video model and labelling actions with an inverse dynamics model. Neither generated them by planning towards goal images.

### Findings

**R1. §9 RQ2 and §7 H2: SIMPLER is both the source of the simulation training data and the closed loop test of "performance on real data". Severity: high. New, introduced by the F4 fix.**
Quoted (§9): "For RQ2 I will generate simulation data in the BridgeData V2 scenes rebuilt in SIMPLER" and "In SIMPLER the policy acts in closed loop in the rebuilt BridgeData V2 scenes."
Problem: a policy trained in a world model built from SIMPLER data and then tested in SIMPLER is tested in the simulator it came from. The physics, geometry and objects are identical, and the background is the same real photograph. This measures simulation to simulation transfer. It also makes the first rival of H2 untestable in closed loop, because physics randomization cannot matter when the test runs on the same physics. The only real evidence left for RQ2 is prediction of real recordings and open loop action matching.
Fix (§9): "In RQ2 I will not count success in SIMPLER as performance on real data, because the policies were trained on data from the same simulator. I will judge RQ2 by how well each world model predicts real BridgeData V2 recordings of the matching scenes and by how closely its policies match their recorded actions, and I will report SIMPLER success only as a check."

**R2. §9 RQ2: the SIMPLER Bridge scenes are thin as a data source. Severity: medium. New, introduced by the F4 fix.**
Quoted: "add randomized variations of their appearance and physics in ManiSkill, on which SIMPLER is built."
Problem: ManiSkill has four Bridge tasks in two scenes. They are evaluation twins with no demonstrations and a real background photograph pasted in, so appearance randomization of the background and depth for Cosmos Transfer are limited, and I would first have to write scripted or motion planning solutions to produce actions. The held out recordings for RQ2 must also come only from the matching scenes, which the text does not say.
Fix: "SIMPLER provides these scenes without demonstrations, so I will write scripted solutions for its four BridgeData V2 tasks to generate the data, and I will evaluate RQ2 only on real recordings from the matching scenes."

**R3. §9 RQ1: the policy input and the decoder confound the prediction target. Severity: high. New, introduced by the F3 fix.**
Quoted: "The choices are the prediction target, the encoder the policy starts from, pretrained on real video or learned from the world model" and "For feature models I will compare frames from a decoder trained after the world model".
Problem: in the [18] code the feature model predicts a compressed 96 dimensional adapter latent and gets pixels only from a lightweight CNN decoder. If the policy reads images, the feature model feeds it blurry decoded frames and the autoencoder model feeds it sharp ones, so a result against H1 could come from the decoder. If the policy reads the world model's own latent, the prediction target and the policy encoder change together and are no longer one choice at a time. The same decoder issue affects the action following test and the PSNR, LPIPS and FVD scores in RQ2.
Fix: "In the main comparison the policy reads the latent of the world model it was trained in, and it encodes real frames with the same encoder at test time. I will vary the encoder of the policy separately with policies that read decoded frames, and I will report the image quality of every decoder so that a weak decoder is not read as an effect of the prediction target."

**R4. §9 RQ1: generating imagined trajectories by planning is costly, differs between targets and is attributed to the wrong works. Severity: medium. New, introduced by the F3 fix.**
Quoted: "as in Ctrl-World and DreamGen ... I will generate the trajectories in the same way for both prediction targets, by planning towards goal images from real start frames."
Problem: planning with a diffusion world model needs many sampled rollouts per trajectory, which is slow at the scale of a training set. The goal distance is computed in each model's own latent space, and planning in autoencoder latents is known to be weaker, so H1 could be confirmed by the planner rather than by the data the policy learns from. Ctrl-World and DreamGen did not plan.
Fix: "I will generate the trajectories in the same way for both prediction targets, by rolling out the baseline policy trained on real data with added action noise inside each world model and keeping the rollouts that a success classifier, the same for both models, judges successful, as in Ctrl-World."

**R5. §9 and §7 RQ1 in navigation: no policy is named, the predictor is expensive and a close prior work is missing. Severity: medium. New, introduced by the F3 and F5 fixes.**
Quoted (§9): "For navigation I will do the same with the predictor of NWM." and "I will report how close the planned path is to the recorded one".
Problem: RQ1 is about policies trained inside a world model, but for navigation §9 names no policy and measures a planned path. Retraining the NWM predictor on two targets costs far more than an academic allocation allows for a second task. RAE-NWM already compared DINOv2 features with NWM's autoencoder latents on RECON and SCAND for planning, with public code that trains in about two GPU days.
Fix (§9): "For navigation I will use the smaller predictor of RAE-NWM [x], whose code is public, and train it on both targets. I will train a goal conditioned navigation policy on the imagined trajectories and measure its path against the recorded one."
Fix (§6): "RAE-NWM [x] predicted DINOv2 features instead of autoencoder codes in a navigation world model and planned better with them, but it did not train policies inside the model."

**R6. §9 RQ3 and RQ4: SIMPLER cannot give a closed loop check in unseen scenes unless its scenes are held out. Severity: medium. Unresolved part of F9.**
Quoted: "For RQ3 I will adapt a world model and a policy to held out BridgeData V2 scenes" and "For RQ4 I will apply the best choices with unchanged settings to held out scenes".
Problem: SIMPLER covers only two BridgeData V2 scenes. If their recordings train the world models in RQ1, they are not unseen in RQ3 and RQ4, and if they are held out, RQ1 loses its closed loop test in seen scenes. Statistical tests over two scenes also rest mainly on seeds.
Fix: "I will hold out the BridgeData V2 recordings of the two scenes that SIMPLER rebuilds from the world model training data in all RQs, so that SIMPLER tests unseen scenes throughout, and I will measure other held out scenes by action matching only."

**R7. §9 RQ3: each pretraining variant needs a new world model. Severity: medium. Remaining over-ambition.**
Quoted: "continue its pretraining on real robot data, or on real and simulation data with and without the objective from RQ2" and "I will repeat this for several amounts of real data and several seeds".
Problem: continuing to pretrain the encoder changes its feature space, so the adapter, the world model predictor and the policy must be retrained for every variant before adaptation even starts. Three variants and a control, times several amounts of real data and seeds, is again large.
Fix: "I will compare the pretraining variants at a few amounts of real data, and if compute is short I will drop the variant pretrained on real robot data alone."

**R8. §7 H1: the discriminating result for the rival is not stated. Severity: low.**
Quoted: "The rival explanation is that performance depends mainly on how faithfully the model follows actions, not on the prediction target."
Fix: add "If the gain disappears when I compare models with similar action following, I will take this as support for the rival."

**R9. Small inconsistencies. Severity: low.**
- §9 says Isaac Lab 3.0 "is in beta as of September 2026". Fix: "which is an early access release as of September 2026".
- §9 still says "For the video models I will also record how well success inside the world model predicts success in SIMPLER" and "For every world model that produces video". Both targets now produce frames through a decoder. Fix: "For both prediction targets" and "For every world model".
- §3 semester 3 says "the prediction target and the encoder of a world model", while §7 RQ1 varies "the encoder the policy is built on". Fix §3: "the prediction target of a world model and the encoder of the policy".
- §7 H1 says the model predicts "the features of an encoder pretrained on real video", while [18] predicts a compressed adapter latent of those features. Fix: "the compressed features of an encoder pretrained on real video".

### Remaining latent space operations

None added. The adapter in [18] is part of the training pipeline and is not analysed, so it stays within the owner's limits.

### Summary

I found two new high severity problems (R1, R3) and five of medium severity (R2, R4, R5, R6, R7). All come from the round 1 fixes that tied RQ2 to SIMPLER and RQ1 to the [18] setup. None needs a new direction, only the sentences above.

### Sources

- [semantic-wm code](https://github.com/chandar-lab/semantic-wm), [Reconstruction or Semantics, arXiv 2605.06388](https://arxiv.org/abs/2605.06388)
- [RAE-NWM, arXiv 2603.09241](https://arxiv.org/abs/2603.09241), [RAE-NWM code](https://github.com/20robo/raenwm)
- [ManiSkill digital twins](https://maniskill.readthedocs.io/en/latest/tasks/digital_twins/), [ManiSkill3 paper](https://arxiv.org/abs/2410.00425), [SimplerEnv](https://github.com/simpler-env/SimplerEnv)
- [Isaac Lab releases](https://github.com/isaac-sim/IsaacLab/releases)

## Round 3: realism

Reviewer scope: visible text of §2, §3, §5, §6, §7, §8, §9, §10 after the round 2 fixes (state on 2026-09-28). I checked R1 to R9 against the current text and looked for new medium or high problems. Fixes are in the plan's style.

### Status of round 2 findings

- R1 resolved. §9 now says "I will not use success in SIMPLER as evidence here, because the training data come from the same simulator."
- R2 resolved in wording ("scripted solutions of the tasks", "real BridgeData V2 recordings of the matching scenes"). Its data assumption is not yet checked, see N1.
- R3 resolved. The policy reads the representation of its world model, the policy encoder is compared separately and decoder quality is reported.
- R4 resolved. Trajectories come from noisy rollouts of the real data policy filtered by one success classifier, as in Ctrl-World.
- R5 resolved. RAE-NWM is cited in §6 and used in §9 with a goal conditioned policy.
- R6 partly resolved. "In every RQ, recordings of the scenes I use as unseen are left out of world model training" does not say which scenes these are or whether the SIMPLER scenes are among them. See N1, which covers it.
- R7 resolved ("If compute is short, I will drop the variant pretrained on real robot data alone").
- R8 resolved.
- R9 resolved (early access wording, "For both prediction targets", "For every world model", §3 semester 3 wording, "compressed features" in H1).

### What I verified

- The SIMPLER paper (arXiv 2405.05941, Appendix B) describes the WidowX tasks as a tabletop square layout for spoon, carrot and blocks and a sink with a yellow basket for the eggplant, with 24 real trials per task. It does not say that these physical scenes appear in BridgeData V2 or how many BridgeData V2 trajectories were recorded in them. BridgeData V2 has 24 environments, mostly seven toy kitchens plus tabletops and standalone toy sinks. I could not confirm that BridgeData V2 holds a usable number of recordings of the exact SIMPLER scenes.

### Findings

**N1. §9 RQ2 and RQ1: the real recordings "of the matching scenes" may not exist in useful numbers. Severity: medium. New, follows from the R2 and R6 fixes.**
Quoted (§9): "I will judge each world model by how well it predicts real BridgeData V2 recordings of the matching scenes" and "In every RQ, recordings of the scenes I use as unseen are left out of world model training."
Problem: RQ2 now rests entirely on real recordings of the two scenes SIMPLER rebuilds, because SIMPLER success is excluded there. If BridgeData V2 has few or no recordings of those exact scenes, RQ2 falls back to the content mismatch of F4. The same unknown decides whether the SIMPLER scenes count as seen or unseen in RQ1, RQ3 and RQ4.
Fix (§9, after "so that the simulated and real scenes match"): "In the first weeks I will check how many BridgeData V2 recordings come from these scenes. I will leave them out of world model training in every RQ and use them as the unseen scenes. If they are too few, I will use the most similar BridgeData V2 scenes, such as its toy sinks and tabletops, and say so."
Then replace "In every RQ, recordings of the scenes I use as unseen are left out of world model training." with nothing, since the new sentence covers it.

**N2. §3, §7 and §9: navigation is both a part of RQ1 and the held out test of RQ4. Severity: medium. New inconsistency.**
Quoted (§7): "navigation is a second task for RQ1 and RQ4" and RQ4 "does the answer to RQ1 hold in navigation, with unchanged settings, that is with the settings chosen on the main task and no new tuning". (§3 semester 4): "Further experiments on RQ1 in manipulation and navigation."
Problem: if the RQ1 comparison is already run and tuned in navigation in semester 4, the RQ4 test in navigation is no longer done with settings chosen on manipulation alone, so H4 loses its point. It is also more work than needed.
Fix: make navigation a part of RQ4 only.
- §7: "My main setting is manipulation on BridgeData V2, and navigation is a second task for RQ4."
- §3 semester 4: "Further experiments on RQ1 in manipulation."
- §9: "For navigation, which I use in RQ4, I will build both models from the predictor of RAE-NWM [19], whose code is public, and train a goal-conditioned policy in them."
- §8 can stay ("with a check in navigation").

No other medium or high problems remain. Each hypothesis now has a test that can tell it apart from its rival, and the measures match what §7 and §8 claim. Compute and code are within reach (the [18] and RAE-NWM code is public, Cosmos Transfer is limited to a fixed subset, and the larger models are optional).

Low, optional: §7 RQ2 says "give policies that work well on real data", while §9 excludes SIMPLER for RQ2. Adding "measured by action matching" after "real data" in RQ2 would remove the doubt.

### Sentences that could simply be cut

These add detail an accepted plan would not carry. Removing them changes no commitment.
- §3 semester 3: "and checking in the first weeks that SIMPLER renders on the cluster, with a workstation as the fallback" (already in §9).
- §6: "Agreement between the ranking of policies in the simulator and in reality is a common indicator of how useful a simulator is, and I will use it with SIMPLER success standing in for real success."
- §7 Fallback: ", which says less about how representations should be learned".
- §9: "If compute allows, I will repeat the main comparison with larger released models, Ctrl-World [20] and V-JEPA 2-AC." (Ctrl-World is a Franka model on DROID and has no closed loop test in this plan.)
- §9: "This mode gives colour and depth images and does not need the ray-tracing cores that A100 and H100 GPUs lack." The Isaac Lab sentence before it can also be shortened to "If ManiSkill limits the variations I need, I will use NVIDIA Isaac Lab [12]."
- §9: "It needs H100 GPUs and several GPU minutes per short clip, so" (keep "I will transfer a fixed subset of the simulated data once and reuse it for all variants").
- §9: "and I will state for every model which data it had seen" (covered by the held out scenes sentence).
- §9: "For both prediction targets I will also record how well success inside the world model predicts success in SIMPLER, as a rank correlation over policies and scenes." and in the reporting paragraph "and, where both are success rates, the gap between success in the world model and in SIMPLER".
- §9 RQ2: "and I will keep only pairs in which the transferred frame keeps the geometry of the simulated one, judged with the depth image used to drive the transfer".
- §9: "I will first choose the adaptation method with the original encoder and then compare the pretraining variants with that method only." can stay, but the preceding "To keep the cost low" is filler.

### Sources

- [SIMPLER, arXiv 2405.05941](https://arxiv.org/abs/2405.05941), Appendix B
- [BridgeData V2](https://rail-berkeley.github.io/bridgedata/), [BridgeData V2 paper](https://arxiv.org/html/2308.12952v3)
- [SimplerEnv](https://github.com/simpler-env/SimplerEnv)

## Round 4: realism

Reviewer scope: visible text of §2, §3, §5, §6, §7, §8, §9, §10 at commit a5c2998, after the round 3 fixes (state on 2026-09-28). I checked N1, N2 and the cuts against the current text, then read the whole plan once more for medium or high problems. Fixes are in the plan's style.

### Status of round 3 findings

- N1 resolved in wording. §9 now checks in the first weeks how many BridgeData V2 recordings come from the SIMPLER scenes, leaves them out of world model training in every RQ and names a fallback. The data question itself is still open, see P2.
- N2 resolved differently from my proposal, and the new version is consistent across sections. §7 says navigation runs RQ1 only with the settings chosen on manipulation and that these runs test H4, §3 semester 4 has RQ1 in manipulation only, semester 6 has "for RQ1, to navigation (RQ4)", and §9 repeats "with only the settings chosen on manipulation and no new tuning". What "settings" means across two predictors is not defined, see P1.
- The low item on RQ2 is resolved (§7 RQ2 now says "measured in open loop").
- Ctrl-World wording is correct. Its paper selected successful imagined rollouts by human judgement before fine-tuning.
- The cuts left no dangling references. All thirty references are still cited in the visible text, and "the baselines named above" still points to the policy trained on real data.

### What I verified

- BridgeData V2 does contain toy sink and tabletop environments. The raw release lists `toysink1_room8052`, `toysink2_bww`, `toysink3_bww`, `tabletop_dark_wood`, `tabletop_light_wood` and `tabletop_white` under the Berkeley part of BridgeData v1, and `datacol2_tabletop_dark_wood` under BridgeData v2. The SIMPLER paper says only that its WidowX tasks come from "environments from the BridgeData V2 dataset" and describes a tabletop with a square layout and a sink with a yellow basket. It does not name the environment folder or say how many recordings were made there. So the count is still unknown, and the check planned in §9 is needed.
- In the SIMPLER paper, released policies trained on all of BridgeData V2 (RT-1-X, Octo-Base, Octo-Small) reached low average success in the WidowX visual matching tasks, with about 24 trials per task and several task averages near zero.
- RAE-NWM predicts dense DINOv2 features with its own predictor and training recipe, and planned better than NWM on SCAND but not on RECON.

### Findings

**P1. §7, §9 and H4: "settings chosen on manipulation and no new tuning" cannot be applied literally to navigation. Severity: medium. New, follows from the N2 resolution.**
Quoted (§7): "In navigation I run RQ1 only with the settings chosen on manipulation, without new tuning, and these runs are the test of H4." (§9): "For navigation I will do the same with the predictor of RAE-NWM [19] ... with only the settings chosen on manipulation and no new tuning."
Problem: the manipulation models use the predictor of [18], a video encoder such as V-JEPA 2 compressed by an adapter, and a manipulation policy. The navigation models use the RAE-NWM predictor, which was built around dense DINOv2 features, and a goal conditioned policy. Learning rates, adapter size, training length and the amount of imagined data measured in trajectories do not carry over between these models, so some settings must be chosen anew in navigation. If they are chosen by looking at navigation results, the test of H4 is lost. If they are copied, a failure in navigation cannot be told apart from a poor fit of the copied values. What can carry over is the choice itself: which prediction target, which encoder of the policy and whether imagined data are added.
Fix (§9, replace "with only the settings chosen on manipulation and no new tuning"): "I will carry over from manipulation only the choices that won there, and I will train every navigation model with the released settings of RAE-NWM, without looking at navigation results. I will read a gain in navigation as support for H4, and a lack of gain as a limit of the choice that I will report without claiming its cause."

**P2. §9: the pool of SIMPLER scene recordings has to serve several roles, and their split is not stated. Severity: medium. Unresolved part of N1.**
Quoted (§9): "In every RQ I will leave them out of world model training and use them as the unseen scenes" and "co-training with a small set of real trajectories" (RQ2) and "adapt a world model and a policy to held-out BridgeData V2 scenes with a small set of real trajectories" (RQ3).
Problem: the same recordings are the RQ2 test set, the unseen test set in RQ1 and RQ4, the adaptation data of RQ3 at several amounts, and possibly the small real set for RQ2 co-training. RQ3 cannot adapt to these scenes without training on some of their recordings, which contradicts "in every RQ I will leave them out". If the RQ2 co-training set also comes from them, RQ2 is tested on scenes it trained on. With an unknown and possibly small number of recordings, the largest amount in RQ3, called "all available real data" in H3, may be small.
Fix (§9, after "and use them as the unseen scenes"): "In RQ3 I will split these recordings into a part for adaptation and a part for evaluation, and the small real set for co-training in RQ2 will come from other BridgeData V2 scenes."

**P3. §7 RQ4 and §9: the unseen scene part of RQ4 has no test of its own. Severity: medium. New, follows from the N1 fix.**
Quoted (§9): "In every RQ I will leave them out of world model training and use them as the unseen scenes" and "For RQ4 I will apply the best choices with unchanged settings to held-out scenes".
Problem: since the SIMPLER scenes are unseen in every RQ, the closed loop results of RQ1 to RQ3 are already results in unseen scenes. RQ4 then repeats them, and H4 for unseen scenes has no observation that could tell it apart from RQ1.
Fix (§9, replace "For RQ4 I will apply the best choices with unchanged settings to held-out scenes and, for RQ1, to navigation."): "For RQ4 I will compare the gain of each best choice on held-out trajectories of the training scenes with its gain in the unseen scenes, and I will test it in navigation for RQ1."

**P4. §9 RQ1: success in SIMPLER may be too rare to separate the variants. Severity: medium. New.**
Quoted: "I will report whether imagined data helps beyond it, mainly in SIMPLER, where the policy acts in closed loop."
Problem: policies trained on all of BridgeData V2 by large teams reached low success in SIMPLER's WidowX tasks. My policies are smaller, trained from a world model, and tested in scenes left out of training. If most runs score near zero on about 24 trials per task, differences between prediction targets and the gain over the real data baseline will be within noise, and RQ1 loses its only closed loop measure.
Fix (§9, after the baseline sentence): "Before the main comparison I will check that the baseline policy succeeds in SIMPLER often enough to show differences, and if it does not, I will judge RQ1 mainly by action matching and say so."

**P5. §9 RQ1: the success classifier sees frames of different quality for the two prediction targets. Severity: medium. New, not covered by the R3 fix.**
Quoted: "keep the rollouts that the same success classifier judges successful" and "For feature models I will compare frames from a decoder trained separately from the world model".
Problem: the classifier must judge decoded frames, and the feature model is decoded by a light decoder while the autoencoder model is decoded by its own. If the classifier is less accurate on one kind of frame, it keeps more failed rollouts for that target, and the policy trained on them is worse for a reason that has nothing to do with the representation. This confounds H1 in the same way R3 did.
Fix (§9, after the classifier sentence): "I will check the classifier by hand on a sample of rollouts from every world model and report how often it is right for each."

**P6. §7 H1: the rival test needs models that follow actions equally well, but RQ1 has only two per predictor. Severity: medium. Unresolved part of R8.**
Quoted: "If the gain disappears between models that follow actions equally well, this supports the rival."
Problem: with one model per prediction target, the two will almost surely differ in action following, so there is no pair that follows actions equally well and the rival cannot be tested.
Fix (§9, after the action following sentence): "To compare models that follow actions equally well, I will also train policies in earlier checkpoints of each world model and compare targets at similar action following."

### Low items

- §6: "Neither work trained policies inside the models or tested them on real data". RAE-NWM evaluated planning on real RECON and SCAND trajectories offline, which is the same kind of test as my navigation measure. Shorten to "Neither work trained policies inside the models, and this step is what RQ1 adds."
- §7: "these runs are the test of H4" should be "these runs are part of the test of H4", since H4 also covers unseen scenes.
- §9: "one world model that predicts video and one that predicts features" while H1 says "codes of an autoencoder". Use "one that predicts the codes of an image autoencoder" for consistency.
- §9: in navigation, the policy that is rolled out with action noise and the success classifier (for example reaching the goal image) are not named. One clause would do.
- RAE-NWM gained on SCAND but not on RECON, so in navigation I should report the two datasets separately.
- §7 Fallback studies "amount and diversity" of data, which RQ1 already varies for imagined data. It still reads as a fallback because it adds mixing ratios with simulated data, so it can stay.

### Summary

I found no high severity problem. Six medium ones remain (P1 to P6). None needs a new direction or more work than a sentence in §9, and P1 and P3 make H4 testable as written. §3, §5, §7, §8 and §10 are consistent with each other and with §9 on the role of navigation. The overall scope is feasible for one student with the [18] and RAE-NWM code, a fixed Cosmos Transfer subset and the larger models optional.

### Sources

- [SIMPLER, arXiv 2405.05941](https://arxiv.org/abs/2405.05941), Table V and Appendix B
- [BridgeData raw release, BridgeData v1 Berkeley environments](https://rail.eecs.berkeley.edu/datasets/bridge_release/raw/bridge_data_v1/berkeley/), [BridgeData v2 environments](https://rail.eecs.berkeley.edu/datasets/bridge_release/raw/bridge_data_v2/), [BridgeData V2 paper](https://arxiv.org/html/2308.12952v3)
- [Ctrl-World, arXiv 2510.10125](https://arxiv.org/abs/2510.10125)
- [RAE-NWM, arXiv 2603.09241](https://arxiv.org/abs/2603.09241)
- [SimplerEnv](https://github.com/simpler-env/SimplerEnv)

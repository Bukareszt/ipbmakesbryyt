# Review 7: adversarial scientific review of the three-thread plan (world models as simulators)

Reviewed on 2026-09-28. Material: visible text of content/02, 03, 05, 06, 07, 08, 09, 10, 11, 12 (working tree, edited 20:19). Background: research/wm_simulators.md, research/nvidia_stack.md, research/wam_lecun.md. Lens: scientific-critical-thinking (design validity, confounders, claim vs evidence), hypothesis-generation (discriminating predictions, genuine rivals, operationalization), scholar-evaluation (evidence-traceable, developmental, no ranking). No file in content/ or output/ was edited.

One framing note before the list. The memory note of 2026-09-28 records that the owner rejected latent-space methods (latent gap measurement, probing, feature alignment, stage-targeted adaptation) as too ambitious, and that the plan should rest on observable measurements and practical training choices. The visible text still builds RQ1, H1, RQ3, H3, the schedule (semester 3) and half of §9 on exactly those latent-space methods. Most Critical items below are therefore also the places where the text lags the owner's own decision.

---

## CRITICAL

### C1. The dependent variable of H1 and H3, "real success", cannot be measured with the described resources
- **File:** 07-questions-hypotheses.md, 09-methods.md
- **Quoted:** "The latent gap predicts the drop in real success of policies trained in a world model" (H1); "I will train policies in world models ... and measure their success on held-out real data" (§9); "Adaptation targeted at that stage reaches the real performance of full fine-tuning with less real data" (H3).
- **Problem:** Success is a closed-loop quantity. A recorded trajectory from DROID, BridgeData V2, RECON or SCAND cannot tell whether a new policy would have succeeded; it can only tell how far the policy's actions or planned path depart from what the human did. "Published real-robot results" exist for a handful of fixed policies (SIMPLER's, Ctrl-World's checkpoints), not for policies the student trains in world models that "differ in rollout length or post-training data". H1 needs many (world model, policy, real success) triples to compute a rank correlation "across scenes and models". Without a robot these triples do not exist. As written, H1 and H3 are untestable by the student.
- **Fix:** Name the observable stand-ins explicitly and use them consistently: "Because I will not have a robot, I will measure a policy by how closely its actions and planned paths match the recorded human actions on held-out real trajectories and, for manipulation tasks covered by SIMPLER, by its success in the SIMPLER simulator, which has been shown to rank policies like real runs. I will call this real performance and state the limitation with every result." Then replace "real success" by "real performance" in H1, H3 and §8.

### C2. H2's split of the remaining gap into "appearance" and "dynamics" cannot be measured with unpaired data
- **File:** 07-questions-hypotheses.md (H2, RQ2), 09-methods.md (RQ2 paragraph), 08-contribution.md
- **Quoted:** "the remaining gap lies mainly in the dynamics rather than in the appearance"; "I will split the remaining gap into its observation and dynamics parts (H2)"; "how much of the remaining gap comes from appearance and how much from dynamics" (§8).
- **Problem:** The observation term is defined as "the distance between embeddings of matched imagined and real states". For a world model trained on Isaac Lab data there are no matched states: no Isaac Lab scene reproduces a DROID or RECON scene, and the owner dropped digital twins. The dynamics term, "the error of its latent prediction on real transitions", is confounded by appearance shift, because the encoder input has changed as well. With a frozen encoder pretrained on real video (DINOv2, V-JEPA 2) the observation term is a property of the frozen encoder, not of the world model under study. The decomposition is therefore not identifiable from the data described.
- **Fix:** Replace the measured decomposition by an interventional one, which is what §9 already does elsewhere: "I will not try to split one measurement into appearance and dynamics. Instead I will change one thing at a time, adding photorealistic appearance transfer to the simulated frames, adding a small set of real transitions to training, and changing the prediction target, and I will read how much each change improves prediction of held-out real observations and transitions." Rewrite H2 accordingly: "A world model that predicts in the representation space of an encoder pretrained on real video will transfer to real data better than one that predicts pixels, and adding real transitions to training will help more than appearance transfer alone. If appearance transfer alone closes most of the gap, the choice of representation matters less."

### C3. RQ3 and H3 are defined by an output of RQ1 that may not exist, and the Fallback does not cover it
- **File:** 07-questions-hypotheses.md
- **Quoted:** "adapting only the stage at which imagined and real representations diverge, found in RQ1" (RQ3); "Adaptation targeted at that stage" (H3); "If the latent gap does not predict transfer better than pixel-level indicators, I will guide RQ2 and RQ3 with the rank correlation" (Fallback).
- **Problem:** Circular dependency. If RQ1 does not find a single stage (H1's own rival says "the gap is spread over all stages"), the main method of RQ3 has no definition. The Fallback replaces the measure but not the method. The schedule puts first RQ3 experiments in semester 5, one semester after RQ1 closes, so there is no slack. This is also the method the owner rejected on 28 Sep.
- **Fix:** Make RQ3 stand on practical, observable choices and let RQ1 inform rather than define it: "RQ3. How can the amount of real data needed to adapt the world model and the policy to a new real setting be reduced? I will compare, at equal amounts of real data, full fine-tuning, parameter-efficient fine-tuning of a small part of the network, co-training on simulated and real data, and test-time adaptation of the predictor from its own prediction error, and I will report performance as a function of the amount of real data." H3: "Adapting a small part of the network with the rest frozen reaches the performance of full fine-tuning with less real data, because the pretrained parts already generalize. The rival explanation is that the gap is spread over the whole network, so that partial adaptation does not beat full fine-tuning with the same regularization."

### C4. Placeholders in the visible bibliography and a model cited without a reference
- **File:** 12-other.md, 09-methods.md
- **Quoted:** "[18] ZANATTA_PLACEHOLDER"; "[24] IWS_PLACEHOLDER"; §9: "or the small LeWorldModel as latent world models" (no reference number).
- **Problem:** A committee will read this as an unfinished document. [18] carries the most important empirical hint of §6 (representation robustness predicted real transfer). [24] carries a strong quantitative claim.
- **Fix:** From the notes: "[18] Zanatta, ..., Malczyk, ..., & Alexis, K. (2026). [title as on arXiv]. arXiv:2606.05015." "[24] Wang, ..., Syed, ..., Wu, ..., Zhang, ... (2026). Interactive World Simulator [title as on arXiv]. RSS. arXiv:2603.08546." Add "[27] Maes, L., Le Lidec, Q., Scieur, D., LeCun, Y., & Balestriero, R. (2026). LeWorldModel: Stable end-to-end joint-embedding predictive architecture from pixels. arXiv:2603.19312." and cite it in §9. Fill the author lists from the arXiv pages before submission.

### C5. H1 compares the new measure against a baseline the plan itself says is already known to be weak
- **File:** 07-questions-hypotheses.md (H1), 05-justification.md, 06-state-of-the-art.md
- **Quoted:** H1: "better than the pixel-level video quality of the world model". §5: "the visual quality of a world model does not reliably predict whether policies succeed in it [6]". §6: "how well a model follows actions matters more" (World-in-World).
- **Problem:** Beating a predictor already shown to be poor is a low bar and not a discriminating test. The field's current best candidate predictor is action-following or closed-loop consistency (World-in-World, WorldSimProbe, GigaWorld-1 in the notes). H1's rival, "errors the representations do not register, such as small contact details, so that pixel-level indicators predict it equally well", is not a genuine rival either: frame-averaged pixel metrics register contact details no better than latent features do.
- **Fix:** "H1. The gap between imagined and real observations, measured in the representation space of the world model, predicts the drop in real performance of policies trained in it at least as well as measures of how faithfully the model follows actions, and better than its visual quality. The rival explanation is that action following alone explains the drop, so that the representation adds nothing." Add action-following measures to the predictor set in §9.

---

## MAJOR

### M1. "Paired imagined vs real observations" from the same start and actions is a weak pairing for stochastic world models and for on-expert actions
- **File:** 09-methods.md
- **Quoted:** "Rolling a world model forward from the same start state with the same actions gives imagined observations paired with real ones, which I need for measuring the gap and for probing."
- **Problem:** (a) NWM, Ctrl-World and Cosmos are diffusion or flow models. One rollout is one sample from a distribution. The distance between one sample and the one recorded real frame mixes model error with legitimate randomness (people, lighting, unobserved object state). (b) Errors compound with horizon, so frames are matched only near the start. (c) Recorded actions are expert actions. The notes report that world models follow expert actions but ignore off-expert ones, and a policy trained inside a world model explores off-expert actions. A gap measured on recorded actions therefore underestimates the gap that matters for policy training.
- **Fix:** "For each real transition I will draw several rollouts from the world model and compare the real next observation with their spread, at one step and at a few steps with the real frames fed back in. The recorded actions are expert actions, so this measures the gap only where the data went. For actions the data did not take I will use the physics simulator as the reference, where any action can be executed."

### M2. Two tasks of equal weight, four research questions, one student, three research years
- **File:** 05-justification.md, 07-questions-hypotheses.md, 03-schedule.md
- **Quoted:** "I will work on two tasks of equal weight, robot navigation and robotic manipulation."; "Do the answers to RQ1 to RQ3 hold ... across navigation and manipulation?"
- **Problem:** Each task has its own world models (NWM against DINO-WM, V-JEPA 2-AC, Ctrl-World, Cosmos), its own datasets, its own simulator scenes in Isaac Lab, its own policies and its own evaluation stand-in. Doubling every experiment across RQ1 to RQ3 is the largest feasibility risk in the plan. Semester 3 alone asks for the environment on both tasks plus first RQ1 results.
- **Fix:** "I will develop and test the methods on one task first, robotic manipulation, where public data, world models and a simulator that ranks policies like real runs are all available, and I will use robot navigation in RQ4 to check whether the answers hold on a second task." Adjust semester 3 to manipulation only and move navigation set-up to semester 5.

### M3. Confounder in H2: the encoder's real-video pretraining, not the latent prediction target, may explain the transfer advantage
- **File:** 07-questions-hypotheses.md (H2), 09-methods.md
- **Quoted:** "A world model that predicts in the representation space of an encoder pretrained on real video transfers from simulation to real data better than one that predicts pixels".
- **Problem:** The latent model uses DINOv2 or V-JEPA 2 features, which have seen large amounts of real video. The pixel model has not. Any advantage may come from the real-data exposure of the encoder, not from predicting in representation space. The comparison also uses "the latent terms from RQ1 for all models", which scores a pixel model in the latent model's own training space and favours the hypothesis.
- **Fix:** Add the discriminating control: "To separate the effect of the prediction target from the effect of the encoder's real pretraining data, I will also train a small latent world model end to end on simulated pixels only, with no real pretraining, and a pixel model initialized from a video model pretrained on real video." And score all models on a common task-level yardstick (SIMPLER success, trajectory error against recorded paths), not only in latent space.

### M4. RQ1 as phrased is not a question with a discriminating answer
- **File:** 07-questions-hypotheses.md
- **Quoted:** "what in the learned representations decides whether it succeeds or fails?"
- **Problem:** "What decides" has no failure condition. Any correlation found can be reported as the answer. The operational content is two measures and a probing study; the question should name them.
- **Fix:** "RQ1. When a policy is trained inside a world model learned from real data and then run on real inputs, does the gap between imagined and real observations, measured in the representation space of the world model, predict how much the policy loses in reality, and does it predict this better than the model's visual quality or its action following?"

### M5. H4 is phrased so that every outcome confirms something
- **File:** 07-questions-hypotheses.md
- **Quoted:** "Methods that act on the representations transfer between the two tasks with unchanged settings, while methods that act on pixels, such as appearance transfer, need retuning for each task. If neither transfers, the gap is specific to the task."
- **Problem:** "Transfer between tasks with unchanged settings" is undefined for a method (which settings, which measure). The closing sentence turns a null result into a finding about the gap rather than about the methods, so H4 cannot fail. Appearance transfer is not a "method that acts on pixels" in the same sense as a fine-tuning method; the two classes are not comparable.
- **Fix:** "H4. The training and adaptation choices that work best on manipulation, with their settings unchanged, also give a gain on navigation and in unseen scenes. If the best choices differ between the two tasks, I will report the difference and treat the answers as task specific."

### M6. Leftover of the removed idea and a wrong "either... or"
- **File:** 06-state-of-the-art.md
- **Quoted:** "These works adapt either the world model or the policy with one fixed recipe. Which part of the representation should be adapted so that the fewest real samples are needed is, as far as my search shows, still open."
- **Problem:** Two sentences earlier the same paragraph says VLAW "fine-tunes the world model on real rollouts and then improves the policy with synthetic data from it", which adapts both. The claim is self-contradicted. The second sentence also understates surgical fine-tuning [26], which asks exactly "which layers to adapt" under shift. This paragraph is the last trace of the "correct both with few real samples" framing. No other leftover of the removed "choosing real rollouts" idea was found in §3, §5, §7, §8, §9 or §10.
- **Fix:** "These works fix the adaptation recipe in advance. Which recipe needs the fewest real samples when the world model and the policy meet a new real setting, and whether the answer from image classification [26] carries over to world models, is, as far as my search shows, still open."

### M7. Absence claims stated as facts in §5 and §9
- **File:** 05-justification.md, 09-methods.md
- **Quoted:** "Little is known about how to build a world model from physics simulation data"; "it is not known how to adapt it with as few real samples as possible"; §9: "No established theory covers the generalization of world models or of policies trained in them".
- **Problem:** Universal absence claims. The notes list a 2026 generalization theory for JEPA world models (Cui et al., arXiv:2606.27014) and a depth-regularized JEPA study of latent shift under domain change (Khan, arXiv:2607.16314), so the theory claim is false as stated.
- **Fix:** "I have not found in my search a study of how to build a world model from physics simulation data so that it predicts the real world well." "I have not found a settled answer to how to adapt it with as few real samples as possible." §9: "I have not found an established theory that covers the generalization of world models or of policies trained in them, so the work will be mostly empirical."

### M8. Overclaims about prior work
- **File:** 05-justification.md, 06-state-of-the-art.md
- **Quoted and problem:**
  - §5: "In the first study that moved a policy of this kind from purely synthetic training to a real robot arm" and §6: "The first work to report it [7]". "First" is the paper's own claim, and [7] is a workshop preprint. Also a category slip: [7] trained a World Action Model on physics-simulator demonstrations, not a policy inside a world model learned from real data, which is what the §5 paragraph is about. **Fix:** "In the first such study I have found, a policy trained only on synthetic demonstrations succeeded in about a third of the trials on a real robot arm [7]." and in §6 "The first work I have found to report it [7]".
  - §6: "It is the main published bridge from simulation data to real-looking data." The notes list EMMA, World Translation and GigaWorld-0, and older image-translation methods exist. **Fix:** "It is the most widely used published bridge I have found from simulation data to real-looking data."
  - §6: "The term was set by DreamZero [15]". The notes say the term appears earlier in JOWA and DyWA and was popularized by DreamZero. **Fix:** "The term was popularized by DreamZero [15]".
  - §6: "SkyJEPA [10] is the clearest case of a model trained on simulated data only that worked in reality, on a task with simple contact." Quadrotor flight has no contact. **Fix:** "on a task without contact."
  - §6: "the robustness of the learned representation across environments predicted real transfer better than the simulated score did [18]". The notes support "predicted real transfer" and "the best model in simulation failed on the real platform", not a direct comparison of predictive power. **Fix:** "and the robustness of the learned representation across environments was a better guide to real transfer than the simulated score [18]" is acceptable only if the paper states it; otherwise drop "better than the simulated score did".

### M9. Isaac Lab 3.0 kit-less mode limits what §9 promises
- **File:** 09-methods.md, 06-state-of-the-art.md
- **Quoted:** §9: "NVIDIA Isaac Lab 3.0 [12] in its kit-less mode with the Newton physics engine, which runs on H100 GPUs. I will use Cosmos Transfer [13] to add photorealistic appearance to simulator renderings." §6: "Cosmos Transfer [13] turns simulator renderings such as depth or segmentation maps into photorealistic video".
- **Problem:** Per the notes, the kit-less Warp renderer outputs RGB and depth only. Segmentation needs Isaac RTX, which does not run on H100. Isaac Lab 3.0 is an early-access release from 16 Sep 2026, untested on the cluster. The cited paper [12] describes Isaac Lab on Isaac Sim with PhysX and only mentions Newton as planned. No fallback simulator is named.
- **Fix:** "As the physics simulator I will use NVIDIA Isaac Lab 3.0 [12] in its mode that runs without Isaac Sim, which gives colour and depth images on H100 GPUs. I will drive Cosmos Transfer with depth. If this mode proves unstable on the cluster, I will use ManiSkill, on which SIMPLER is built, and Habitat for navigation."

### M10. Cost of training policies inside video world models
- **File:** 09-methods.md
- **Quoted:** "I will train policies in world models that differ in these terms, for example by rollout length or by post-training data".
- **Problem:** Ctrl-World takes about 5 s per interaction step on an H100 (notes); Cosmos-Predict2 about 80 s per generation. Reinforcement learning inside such models over several world-model variants, two tasks and several seeds is out of reach. Ctrl-World's own recipe is supervised fine-tuning on imagined successful trajectories, which is affordable.
- **Fix:** "Policies will be trained in a world model by generating imagined trajectories once and fine-tuning the policy on them, as in Ctrl-World and DreamGen, rather than by reinforcement learning inside the model, which would be too slow for the model sizes I will use."

### M11. Probing "the stage of the policy" has no object for navigation
- **File:** 07-questions-hypotheses.md, 09-methods.md
- **Quoted:** "I will locate with probes the stage of the policy at which real inputs lose task information"; §9: "For navigation I will start from NWM [3]."
- **Problem:** NWM is a planner that searches actions by rolling the world model forward. There is no separate policy network with stages to probe. For manipulation the probed policy would be a large pretrained model (π0.5 for Ctrl-World) whose stages the student did not train. This is also the item the owner rejected.
- **Fix:** Drop probing from §7 and §9 (also fixes the page limit). If kept, restrict it: "For manipulation, where the policy is a separate network, I will additionally check at which stage of the policy real inputs lose task information."

### M12. The sentence "All results will be measured on held-out scenes" contradicts the use of published results and SIMPLER
- **File:** 07-questions-hypotheses.md
- **Quoted:** "All results will be measured on held-out scenes not used for training or model selection."
- **Problem:** Published real-robot results and SIMPLER scenes are fixed by others and overlap with the training data of Ctrl-World (DROID) and V-JEPA 2-AC (DROID). A blanket promise cannot be kept.
- **Fix:** "Where I control the data, results will be measured on held-out scenes not used for training or model selection. Where I rely on published results or on SIMPLER, I will state which data the models had seen."

---

## MINOR

### m1. §5 says three questions, §6 and §7 have four
- **File:** 05-justification.md. **Quoted:** "I will study three connected questions." **Fix:** "I will study three connected questions and check whether the answers hold in unseen scenes and across two tasks."

### m2. Jargon a computer-science committee may not follow
- §9: "PSNR, LPIPS and FVD" (add "three standard scores of image and video similarity"); "permutation tests" (fine, but "rank correlation ... with permutation tests" can be "rank correlation and a test of its significance"); "kit-less mode with the Newton physics engine" (see M9); "DINOv2" (§6 first use: "DINOv2, a vision network pretrained without labels"); "post-trained" (§6: use "further trained"); "pseudo-actions" (§6: "actions inferred from the video"); "teleoperation" (add "remote control by a human"); "test-time adaptation" (§7, §9: "adaptation while the model is running"); "egocentric video" (§6: "video from the robot's own camera"); "SLURM" fine; "Franka arm", "WidowX" fine.

### m3. Anglicisms and punctuation
- No semicolon, em dash or en dash in the visible text. "sim", "sim-to-real" and "sim-and-real" appear only inside cited titles in §12, which is correct. "pixel-level", "post-training", "held-out" are acceptable. "Cosmos-Predict [4]": [4] is the Cosmos 1 platform paper; Predict2.5 is arXiv:2511.00062 (notes). Either cite it or write "the Cosmos video world models [4]".

### m4. Boilerplate and triads
- §8: "This is timely because world models are becoming a common way ..." reads as a grant template. Fix: "World models are now used to create training data and to evaluate robot policies, NVIDIA and others combine them with physics simulators, and World Action Models put the world model and the policy into one network, so answers to these questions are needed now."
- §5: "a warehouse, a hospital or a home"; §10: "faster, more cheaply and more safely"; §10 PL: "szybciej, taniej i bezpieczniej". Harmless, but two of the three triads could go.
- §6: "These works show that latent world models can transfer to reality and hint that the representation decides it." "decides it" overstates [18]; use "and hint that the representation matters for it".

### m5. §7 formatting and page limit
- Body is 3998 characters without the heading (4097 with it), so it fits one page at 11 pt if the list is set tightly. The rendered PDF of 20:14 (before the last edit) overflowed by two lines onto page 7 ("data. This is weaker, because it needs real rollouts of many policies and does not say where the gap arises."). The numbered list wastes vertical space: items 1 to 8 number the RQs and hypotheses twice ("1. RQ1.", "2. H1."), and RQ4 and H4 share item 7 while the others do not.
- **Least harmful cuts, in order:** (1) remove the numbering and use plain paragraphs starting "RQ1.", "H1."; (2) drop "and I will locate with probes the stage of the policy at which real inputs lose task information" from RQ1 (also per M11); (3) shorten the Fallback to "If the latent gap does not predict transfer better than the other indicators, I will guide RQ2 and RQ3 with the rank correlation between performance in the world model and on real data."; (4) drop the sentence "I will work on both navigation and manipulation." from the first paragraph, since §5 says it.

### m6. §10 abstract
- "adapt the dream and the robot to a new place from only a few real trials" and PL "z niewielu prawdziwych prób": "trials" implies real rollouts the student will not have. Fix: "from only a little real experience" / "z niewielkiej ilości prawdziwych danych".

### m7. Bibliography details
- [7] is listed as arXiv only; the notes say CVPR 2026 Embodied AI Workshop. Either is acceptable, but be consistent with how [14] and [22] name venues.
- [9] V-JEPA 2 and [4] Cosmos are arXiv only; fine.
- [18] and [24] see C4.

### m8. Schedule wording
- Semester 3: "measuring the gap between world-model simulations and real data in representation space (RQ1)" should follow whatever RQ1 becomes after C1, C5 and M4. Suggested: "Initial experiments on how well policies trained in a world model perform on real data and on what predicts that (RQ1)".
- Semester 4 and §11 agree (submission by September 2027, ICLR 2028 or RA-L). Semester counting is consistent with a start of studies in October 2025 and research from October 2026 to September 2029.

---

## Claims about prior work, checked against research/*.md

| § | Claim | Status |
|---|---|---|
| 5 | UniSim trained policies only inside the model and used them on real robots [2] | consistent |
| 5 | NWM imagines a walk through an unfamiliar place from a single image [3] | consistent |
| 5 | Cosmos released as a base for building simulators [4] | consistent |
| 5 | Model may ignore an action, let a gripper pass through an object, drift over a long rollout [5],[6] | partly: contact from VLAW [5], action following from World-in-World [6]; long-horizon drift is from WoVR and HaWMPO in the notes, not [5] or [6]. Either add a citation or drop "drift away ... over a long rollout" |
| 5 | First study moving such a policy from synthetic training to a real arm, about a third of trials [7] | value consistent (35%); "first" is the paper's own claim; category slip (see M8) |
| 5 | Visual quality does not reliably predict policy success [6] | consistent |
| 5 | LeCun: predict in representation space, ignore unpredictable details [8] | consistent |
| 5 | V-JEPA 2 planned movements of a real robot arm [9] | consistent |
| 5 | SkyJEPA trained on simulated data only and flew a real quadrotor [10] | consistent (preprint under review) |
| 5 | "Little is known ..." and "it is not known ..." | unsupported as universal claims (M7) |
| 6 | Ha and Schmidhuber: agent learned in its dream, then played the real game [1] | consistent |
| 6 | DreamerV3: one configuration, more than 150 tasks [11] | consistent |
| 6 | UniSim: mixed internet, robot and navigation data; zero-shot real transfer [2] | consistent |
| 6 | NWM predicts egocentric video and plans by simulating trajectories [3] | consistent |
| 6 | Cosmos: open world foundation models meant to be post-trained [4] | consistent |
| 6 | NVIDIA combines these with Isaac Sim and Isaac Lab [12] | consistent |
| 6 | Cosmos Transfer: depth or segmentation to photorealistic video, same geometry and motion [13] | consistent; "the main published bridge" is an overclaim (M8) |
| 6 | DreamGen: fine-tunes video model, generates videos, pseudo-actions, trains policy; 22 new behaviours; three real robots improved [14] | consistent |
| 6 | Term WAM "set by" DreamZero; more than twice the generalization of VLAs [15] | value consistent; "set by" should be "popularized by" (M8) |
| 6 | Sim-to-real transfer of WAMs barely studied; first work [7], 35% on a real Franka | value consistent; "first" is the paper's own claim (M8) |
| 6 | JEPA description [8]; DINO-WM predicts frozen DINOv2 features [16] | consistent |
| 6 | V-JEPA 2 pretrained on more than a million hours; V-JEPA 2-AC less than 62 hours of DROID, real Franka arms in unseen labs, no rewards [9] | consistent |
| 6 | SkyJEPA [10]; AdaJEPA uses its own prediction error at test time [17] | consistent |
| 6 | Zanatta et al.: best in simulation failed on the real platform; representation robustness predicted transfer [18] | consistent except "better than the simulated score did" (M8); reference is a placeholder (C4) |
| 6 | "I have not found in my search a work that measures the gap ... in the latent space ... and relates it to the success of a policy" | correctly phrased; note that Khan 2026 (arXiv:2607.16314) reports latent shift under domain change without the policy link, so the claim survives only because of the last clause |
| 6 | Ctrl-World: trained on DROID, ranks policies without real rollouts, fine-tuning on imagined successes [19] | consistent |
| 6 | World-in-World: visual quality does not guarantee success, action following matters more [6] | consistent |
| 6 | VLAW: models lack physical accuracy, trained without failures, miss contact details [5] | consistent |
| 6 | SIMPLER: visually matched scenes rank policies nearly like real runs [20] | not in the notes; consistent with the SIMPLER paper as generally known |
| 6 | Domain randomization varies textures [21] | consistent |
| 6 | Co-training improved real manipulation [22]; co-training aligns domains but keeps them distinguishable [23] | not in the notes; unverified here |
| 6 | SkyJEPA "clearest case", "task with simple contact" | judgment; "simple contact" is wrong, the task is contact-free (M8) |
| 6 | "I have not found in my search a controlled study of which representation and training choices ..." | correctly phrased; consistent with the notes' gap statement |
| 6 | IWS: policies trained on world-model data comparable to same amount of real data [24] | consistent; reference is a placeholder (C4) |
| 6 | Probing shows action fine-tuning degrades VLA visual representations [25]; surgical fine-tuning: best layers depend on shift type [26] | not in the notes; consistent with the papers as generally known |
| 6 | "These works adapt either the world model or the policy" | contradicted by the same paragraph (M6) |
| 9 | "No established theory covers the generalization of world models" | unsupported; notes list Cui et al. 2026 (M7) |
| 9 | Isaac Sim does not support A100 or H100 | consistent |
| 9 | Isaac Lab 3.0 kit-less mode with Newton runs on H100 | consistent, with the RGB and depth only limit (M9) |
| 9 | DROID: Ctrl-World and V-JEPA 2-AC trained on it; BridgeData V2 WidowX in SIMPLER; RECON and SCAND used by NWM | consistent with the notes and the source papers |

---

## Internal consistency check

- §3 vs §7: every RQ has a semester (RQ1: 3 and 4, RQ2: 4 and 5, RQ3: 5 and 6, RQ4: 6). Every RQ has a method paragraph in §9 and a result in §8. Consistent, except that semester 3 wording depends on how RQ1 is rewritten (m8).
- §3 semester 4 vs §11: both name a submission by September 2027 to ICLR or RA-L. Consistent.
- §5 "three questions" vs §6 and §7 "RQ1 to RQ4": inconsistent (m1).
- §7 H2 and §8 "appearance vs dynamics": both rest on the unmeasurable split (C2). If C2 is applied, §8's second result must change to "which training choices help and by how much".
- §7 RQ3 depends on RQ1's stage; Fallback does not cover it (C3).
- §10 abstract matches §7 in substance. It omits RQ4, which is acceptable.
- Removed idea ("choosing few real rollouts that correct both"): no trace in §3, §5, §7, §8, §9, §10. The nearest residue is the "either the world model or the policy" sentence in §6 (M6).
- §12 opening statement on AI use is consistent with §9.

---

## Verdict

Taken as written, the plan is not yet realistic for one student in three research years, for three reasons that are fixable without changing the topic. First, its main outcome variable, real success of policies trained in a world model, cannot be measured with recorded datasets and published results, so H1 and H3 have no test until a stand-in (trajectory error on held-out real data, SIMPLER success) is named and used throughout. Second, H2 promises to split a measured gap into appearance and dynamics, which is not identifiable without paired simulated and real states that the student will not have; an interventional design (one training change at a time) answers the same question and is already half written in §9. Third, the latent gap, probing and stage-targeted adaptation carry RQ1 and RQ3, make RQ3 depend on an RQ1 result that may not exist, and are the very methods the owner has already set aside as too ambitious; replacing them with practical, observable choices (prediction target, appearance transfer, co-training, parameter-efficient adaptation, data amount curves) removes the circularity and most of the page-limit pressure at once. Running two tasks at equal weight across four RQs is the remaining risk and should become one primary task with the second used as the generality check. With these changes, the three threads (world models as simulators, simulation-trained world models that predict real data, adaptation with less real data) rest on open models that run on H100 nodes, on public datasets, and on comparisons a single student can complete, and the schedule and the September 2027 first submission become credible.

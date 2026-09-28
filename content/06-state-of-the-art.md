# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

The idea of learning a model of the environment and training a controller inside its predictions goes back at least to Ha and Schmidhuber [1], whose agent learned to play a game inside its own "dream" and then played the real game. DreamerV3 [11] turned training in imagination into a general method that works with one fixed configuration across more than 150 tasks. Such models are small and learned for one environment. Since 2023, large generative models trained on internet and robot video have been used as interactive simulators of the real world. UniSim [2] learned a simulator from mixed internet, robot and navigation data, and policies trained purely in it transferred to the real world without further training. Navigation World Models (NWM) [3] predict the first-person video of a moving robot and plan by simulating candidate trajectories. NVIDIA's Cosmos platform [4] provides open world foundation models that are meant to be post-trained into world models for particular robots and vehicles.

NVIDIA also builds physics simulators, Isaac Sim and Isaac Lab [12], and uses Cosmos Transfer [13] to make their renderings look real. Cosmos Transfer generates video from spatial control inputs such as depth or segmentation maps, so a simulator rendering can be turned into a real-looking video that keeps its layout and motion, and the simulated actions remain valid. It is the most widely used bridge I have found from simulation data to real-looking data. DreamGen [14] fine-tunes a video world model on the target robot, generates videos of new behaviours, labels them with actions inferred from the video and trains a policy on them. With these data, a humanoid robot learned 22 new behaviours in seen and unseen environments from teleoperation data of a single pick-and-place task, recorded while a human steered the robot.

A newer line merges the world model and the policy. A World Action Model (WAM) is a single network that predicts both future states of the world and the robot's actions. DreamZero [15], a well known model of this kind, reported that it generalized to new tasks and environments more than twice as well as vision-language-action models (VLAs). VLAs map images and instructions directly to actions. The simulation-to-reality transfer of WAMs has barely been studied. The first such work I have found [7] fine-tuned a Cosmos video model into such a policy, trained it only on synthetic demonstrations and reached 35% average success on a real Franka arm without any real robot demonstrations.

LeCun's position paper [8] argues that a world model should not predict pixels. In his Joint Embedding Predictive Architecture (JEPA), the model encodes the current and the future observation and predicts the future representation, so it can drop unpredictable detail such as texture or sensor noise. DINO-WM [16] predicts the frozen features of DINOv2, a vision network pretrained without labels, and plans without reconstructing pixels. V-JEPA 2 [9] was pretrained on more than a million hours of video. Its action-conditioned version, V-JEPA 2-AC, was further trained on less than 62 hours of robot video from the DROID dataset and planned pick-and-place on real Franka arms in labs it had not seen, without rewards. SkyJEPA [10] trained a JEPA world model on automatically generated data and reported zero-shot simulation-to-reality control of a quadrotor in outdoor flights. In a study of DreamerV3 world models for quadrotor navigation, the model that scored best in simulation failed on the real platform, while the robustness of the learned representation across environments predicted real transfer, and the size of the latent space and the length of the training sequences mattered most for the quality of the world model [17]. A comparison of six encoders as the base of a world model trained on BridgeData V2, a real manipulation dataset, found that encoders trained to reconstruct pixels scored well on pixel metrics, while encoders pretrained on semantic content were better for planning and for evaluating a fixed policy inside the model [18]. In navigation, RAE-NWM [19] predicted DINOv2 features instead of the autoencoder codes of NWM and planned better with them on SCAND but not on RECON. Neither work trained policies inside the models or tested them on real data, and these two steps are what RQ1 adds. I have not found in my search a controlled comparison that measures how the prediction target and the pretrained encoder affect the performance on real data of policies trained inside a world model.

World models are also used to evaluate policies instead of running them on a robot. Ctrl-World [20], trained on DROID, ranked policies without real rollouts and improved a policy by fine-tuning it on imagined successful trajectories. World-in-World [6] tested world models in closed loop on navigation and manipulation and found that visual quality does not guarantee task success, while how well a model follows actions matters more. VLAW [5] found that current world models lack the physical accuracy needed to improve policies, because they are trained on demonstrations without failures and miss small contact details. For physics simulators, the SIMPLER study [21] showed that scenes visually matched to real images can rank policies in nearly the same order as real runs.

Almost all large world models are trained on real video. Training them on physics simulation data is attractive, because such data are cheap, come with exact actions and states and can be generated without limit, but it moves the simulation-to-reality gap from the policy into the world model. The classic tools for this gap were built for policies. Domain randomization [22] varies simulator parameters such as textures so that reality looks like one more variation. Co-training on simulated data together with a small real set improved real-world manipulation [23], and a mechanistic analysis of such co-training showed that it aligns the two domains but keeps them distinguishable [24], so making the two domains identical is not required. For world models, SimDist [25] pretrained a world model in simulation and adapted only the part that predicts the next state with real data, on contact-rich manipulation and quadruped locomotion. Wang et al. [26] pretrained a world model in simulation by imitation and fine-tuned its encoder and policy on a small set of real demonstrations for manipulation, with object poses rather than images as input. SkyJEPA [10] is the clearest case I have found of a model trained without real flight data that worked in reality, on a flight task without contact with objects and with state inputs rather than images. I have not found in my search a controlled study of which representation learning choices, such as the prediction target, appearance randomization or transfer, an objective that pairs simulated and photorealistic views, or co-training, make a world model trained on simulation data predict real recordings well.

When a small amount of real data is available, it is used in different ways. VLAW [5] fine-tunes the world model on real rollouts and then improves the policy with synthetic data from it. DreamGen [14] fine-tunes the video world model on the target robot before generating new training videos. The Interactive World Simulator [27] reported that policies trained on data from its world model performed comparably to policies trained on the same amount of real data. Parameter-efficient fine-tuning, such as LoRA [28], updates only a small set of added weights and is a common way to adapt large pretrained models cheaply. On the policy side, keeping the visual representation of a VLA close to its pretrained state during fine-tuning improved generalization to new conditions [29], and the best layers to fine-tune were found to depend on the type of distribution shift [30]. These works fix the pretrained representation and vary how it is adapted, and SimDist [25] trained its encoder on simulation data and kept it frozen during real adaptation. I have not found in my search a comparison of how the representation of a world model, and of the policy trained in it, should be pretrained so that the fewest real samples are needed later.

My research questions in §7 address these open points. RQ1 asks which representation learning choices affect how well a policy trained in a world model built from real data performs on real data, RQ2 which choices make a world model trained on simulation data predict the real world, RQ3 how to pretrain the world model and the policy so that a new real setting needs less real data, and RQ4 whether the answers hold in unseen scenes and in navigation.

The works cited in this document are listed in section 12.

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 32: rewritten around world models -->
<!-- Wave 31: grounding + clarity (ultracode) -->
<!-- Wave 29: humanized (no semicolons) -->
<!-- Wave 28: restyled after the accepted 2025 IPB (2026-09-28, research/accepted_plan_tts_2025.txt). §6 narrative in first person where natural; same claims and citation order [1]-[23] as Wave 27 (joint error wording, [8] condition, [12], [14] images and controllers, [15] fine-tuned, [19]/[20] separate); reference list MOVED to §12; ends with the accepted plan's pointer to section 12. -->
<!-- Wave 27: mechanisms + citation audit fixes (2026-09-27, reports/Mechanizmy uczenia reprezentacji IPB.md). §6: joint error (invariance does not target it and can increase it; correcting the simulation can reduce it directly); [8] with its condition (label distributions, here actions, differ); invariance locations chosen in advance incl. fixed layers; [12] without real-world demonstrations; [14] matched images and controllers; [15] fine-tuned; [19] VLA models, [20] surgical fine-tuning as a separate finding; 'To our knowledge' for the localization gap; selected data correct either model or simulation; ASID designs the exploration policy in simulation; randomization follows reconstruction error and task relevance; multi-view photographs. Added [18] Wang, Hao, Hu, Li, Ma, Ramani, Moon, Kwon, 'ReVeal: A Reconstruction-Aware Real-to-Sim Framework for VLA Policy Evaluation', arXiv:2609.23910 (verified today on arxiv.org: title, authors, abstract; DINOv2 r=0.795 vs LPIPS 0.600, PSNR 0.512 in the HTML full text), closest work to RQ1 at workspace level. Dropped to stay within 2 pages (least relevant, no longer cited): old [18] Qian 2026 robotic ultrasound (arXiv:2608.29516). Numbering unchanged otherwise ([1]-[23] in order of first citation); §9 cites [10], [14]. [13] TwinRL-VLA, ACM MM 2026 (arXiv:2602.09023); [17] ECCV 2026 in sentence case; [9] sentence case with 'arXiv preprint'. [7] 'observations and actions' kept (matches the abstract). Trims: 'Digital twins are more recent', Vid2Sim 'monocular urban videos', DANN sentence kept short, 'guided by the twin's reconstruction uncertainty' removed from the real-data gap. -->
<!-- Wave 24: humanized (2026-09-27): §6 prose rewritten with the humanizer skill (no "Yet", no staged contrasts, the three-levers list folded into the bound sentence, "A recent development" opener removed); claims, citations and references unchanged. -->
<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §6: twin paragraph balanced between tasks. Added, verified today on the arXiv API (titles/authors/abstracts) with venues from research/litreview-rq1.md and research/crowdedness.md: [12] Qureshi et al., SplatSim, arXiv:2409.10161, ICRA 2025 (doi:10.1109/ICRA55743.2025.11128339); [14] Li et al., SIMPLER, arXiv:2405.05941, CoRL 2024 (paper checked: visual matching = green screening + texture matching; setups = Google Robot (RT series) and WidowX BridgeV2; paired sim-and-real evaluations); [16] Xie, Liu, Peng, Wu, Zhou, Vid2Sim, arXiv:2501.06693, CVPR 2025 (doi:10.1109/CVPR52734.2025.00155). TwinRL moved to the twin paragraph (first citation) and re-cited in the real-data paragraph. Dropped to stay within 2 pages (least relevant): Wang 2026 Phys2Real (old [13]) and Burns 2024 (old [16]). Renumbered [1]-[24] in order of first citation; §9 citations updated ([4], [5], [6], [9] unchanged; TwinRL [22] -> [13]; SIMPLER [14] new). Last paragraph: "to a new scene or to another task". -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §6 (fixes 7, 8, 9): bound stated with its joint-error term, used as motivation only; invariance cannot reduce the joint error, motivating correcting the simulation (third lever). Added, verified today on the arXiv API (exact titles/authors): [9] Lei, Liu, Maddukuri, Jiang, Zhu, 'A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies', arXiv:2604.13645 (domains stay distinguishable in effective co-training); [14] Jin, Zhu, Ouyang, Xu, Yue, Wu, Liu, 'Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models', arXiv:2603.22876 (global factors, real-world manipulation study); [15] Qian, Luo, Zhu, Zhang, Meng, Yuan, Liu, 'Task-Relevant Feature-Dynamics Fidelity Enables Zero-Shot Sim-to-Real Transfer for Robotic Ultrasound Scanning', arXiv:2608.29516. Dropped to stay within 2 pages (least relevant): Truong 2022, James 2019 RCAN, Ramos 2019 BayesSim, DINOv2, Majumdar 2023, ProcTHOR. Renumbered [1]-[23] in order of first citation; §9 citations updated ([4] Chebotar, [5] Tiboni, [6] Ganin, [9] Lei, [22] TwinRL). Summary paragraph reduced to one sentence (each gap is stated in its own paragraph). 'Nobody studied' claims softened to the precise gaps (errors varying across a scene, task-based localization, correcting both from the same data, prediction beyond simple indicators). 'policy' and 'probing' glossed at first use. -->
<!-- Review-6 (2026-09-27): [11] Zhao et al. ICML 2019 (PMLR 97:7523-7532, title plural, verified on proceedings.mlr.press/v97); [18] Burns et al. CoRL 2024 (PMLR 270:4525-4545, verified on proceedings.mlr.press/v270); new [20] Lee, Chen, Tajwar et al., Surgical fine-tuning improves adaptation to distribution shifts, ICLR 2023 (verified on OpenReview, ICLR 2023 poster; arXiv:2210.11466); old [20]-[25] renumbered [21]-[26]. RQ labels removed from summary; RQ3 wording aligned ("correcting both the model and the simulation"); small-real-data paragraph notes ASID-style selection and that robotic evidence is manipulation-only (research/litreview-rq3.md); wording fixes (overly wide, fixed location, outperforms). -->
<!-- Wave 20 (ultracode), 2026-09-27: visible text rewritten from scratch in the narrative style of the
Binkowski IPB §6, organized to lead to the final RQ1-RQ4 (content/07). 25 refs, all from
research/litreview-rq1..rq4 and the earlier §6 lists; no model/checkpoint names in the prose. Re-checked
today on the arXiv API: first authors and titles of Cheng 2509.18631 (NeurIPS 2025 per comment),
EmbodiedSplat 2509.17430 (ICCV 2025), Phys2Real 2510.11689 (comment "Accepted to ... ICRA 2026"),
Kachaev 2510.25616, Su 1904.07848 (WACV 2020 per comment), TwinRL 2602.09023, Tiboni 2311.01885 (ICLR
2024), Xie 2307.03659, ProcTHOR 2206.06994. Zhao 2019 and Burns 2023: no venue confirmed by an API
today, so cited as arXiv. Cut for the 2-page limit: Peng (dynamics DR), Active DR, Chen et al. 2022 (DR
theory), SIMPLER, Alain & Bengio probes (arXiv:1610.01644, verified today). Dropped from the previous
(v8) list: Habitat, ManiSkill3, DD-PPO, Zhao survey, Höfer, NeRF, ScanNet++, Vid2Sim, GNM, ViNT,
OpenVLA, NWM.
-->
<!-- Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top)
and the deep-research report (reports/Uczenie nawigacji w cyfrowych bliźniakach.md). General
real-to-sim-to-real (navigation main testbed, manipulation generalization test); the gap now says
explicitly, per the report's recommendation 1, that no navigation pipeline has a real-trial correction
stage or budget curves and that manipulation accounting is single points. 35 refs (limit <= 35).
Reused from the Wave 16 list (verified in earlier waves, see the comments below): all except Truong
(Rethinking Sim2Real) and NaVILA, dropped for space.
Reinstated from earlier waves (verified then; formatted entries copied from the Wave 6/11/13 lists):
- [2] ManiSkill3: Wave 6 comment, arXiv 2410.00425, Crossref doi:10.15607/RSS.2025.XXI.021.
- [5] SIMPLER: Wave 6 comment, arXiv 2405.05941, PMLR vol. 270 (CoRL 2024); "paired sim-and-real
  evaluations", "strong correlation" from the abstract -> "simulation can track real performance".
- [17] X-Sim: Wave 11 comment, arXiv:2505.07096 (Dan, Kedia, Chao, ...); re-read on the arXiv API
  2026-09-26 (title "X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real"). "a minute of human
  video" = the report's table ("1 min wideo człowieka").
- [20] ASID: Wave 13 comment, arXiv:2404.12308 (Memmel et al.); abstract "leverage a small amount of
  real-world data to autonomously refine a simulation model", "identifying articulation, mass, and other
  physical parameters" -> "exploration designed for identification".
- [33] SureSim: Wave 11 list [33] (Badithela et al., arXiv:2510.04354); "saves about a fifth to a quarter
  of the real-robot effort" = the report ("SureSim oszczędza 20–25% wysiłku sprzętowego").
New, from the report's sources (verified today on the arXiv API, export.arxiv.org, 2026-09-26):
- [15] ReaDy-Go arXiv:2602.11575 (S. Yoo, Y. Jang, D. Kim, Y. Han, S. Jung, H. J. Kim). The report noted
  a T-RO vs RA-L conflict; the arXiv comment now reads "Accepted by IEEE Robotics and Automation Letters
  (RA-L)" and the arXiv DOI is 10.1109/LRA.2026.3707355, so it is cited as IEEE RA-L, 2026 (v7
  correction settled). "adds moving obstacles" = title ("with Moving Obstacles").
- [22] MuSHRoom arXiv:2311.02778 (X. Ren, W. Wang, D. Cai, T. Tuominen, J. Kannala, E. Rahtu), title
  "MuSHRoom: Multi-Sensor Hybrid Room Dataset for Joint 3D Reconstruction and Novel View Synthesis".
  Venue not confirmed here, so cited as arXiv. "phone and depth-camera captures with a reference mesh
  under an open licence" = the report (iPhone + Kinect + reference mesh, CC-BY-4.0, Zenodo 13986996).
Other figures in the visible text, all from the report: SRCC 0.18 -> 0.844 after removing the
wall-sliding artefact (Kadian et al., arXiv:1912.06321); TwinRL "~20 min" on-robot interaction and
failure-prone configurations (arXiv:2602.09023 abstract, also Wave 15 comment); navigation twins
"15 s (Vid2Sim) to 20-30 min (EmbodiedSplat) of video, zero real training trials"; RialTo "scan + 15 demos
vs BC with 50 demos" (report table; the "0/5/10/15 demos" ablation is NOT cited, per v7). "at most two
task-aware capture papers a year" = niches-data.md N1 (2/2/0/2), unchanged.
Old (Wave 16) -> new numbers: 1->1, 2->3, 3->4, 5->6, 6->7, 7->8, 8->9, 9->10, 10->11, 11->12, 12->13,
13->14, 14->16, 15->19, 16->21, 17->23, 18->24, 19->25, 20->26, 21->27, 22->28, 23->29, 25->30, 26->31,
27->18, 28->32, 29->34, 30->35; 4 (Truong) and 24 (NaVILA) dropped. §9 and §12 renumbered in the same
wave. Reference numbers in the older comments below are pre-Wave-18.
-->
<!-- (history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
general description; navigation (indoor mobile robots) is the domain; pipeline real data -> twin ->
navigation models (extended with world models and foundation models) -> real. Manipulation-only works
dropped from the visible text except RialTo [14] (general real-to-sim-to-real loop) and Maddukuri [9]
(general sim-and-real co-training result, used in §12). 30 refs (was 35); no new references: every entry
was verified in an earlier wave (sources below), none was re-looked-up today.
Reused from the Wave 15 list: Habitat, 3DGS, RialTo, EmbodiedSplat, BayesSim, OpenVLA, NaVILA, Suomela,
Maddukuri, TwinRL, Cosmos, NWM, VLAW, FisherRF, Bayes' Rays, Liu et al. risk-aware, AREA3D, ScanNet++,
Tobin, Peng, DINOv2, PPI (verification in the Wave 15/13/11 comments below and in
research/vla-wm-crowdedness.md §2).
Reinstated from earlier waves (verification in research/references-check.md and the Wave 11 comment below):
- DD-PPO (Wijmans et al., ICLR 2020): references-check.md row 5, "Abstract confirms 2.5 billion steps and
  'essentially solves' PointGoal nav" -> "essentially solves point-goal navigation after billions of steps".
- Kadian et al., Sim2Real Predictivity, RA-L 2020, doi:10.1109/LRA.2020.3013848: row 12, metric name
  "Sim-vs-Real Correlation Coefficient (SRCC)" from the abstract.
- Truong et al., Rethinking Sim2Real, CoRL 2022: row 13, "lower fidelity transfers better for navigation".
- Chebotar et al., Closing the Sim-to-Real Loop, ICRA 2019, doi:10.1109/ICRA.2019.8793789: "adapt the
  simulation parameter distribution using a few real world roll-outs" (Wave 11 comment below).
- Vid2Sim (Xie et al., CVPR 2025, doi:10.1109/CVPR52734.2025.00155): row 30, "Monocular video ->
  interactive sim for urban navigation".
- GaussGym (Escontrela et al., arXiv:2510.15352): review-3 R3-F15, S2 title "learning locomotion from
  pixels" -> "navigation and locomotion".
- GNM (Shah et al., ICRA 2023, doi:10.1109/ICRA48891.2023.10161227) and ViNT (Shah et al., CoRL 2023,
  arXiv:2306.14846, "Accepted for oral presentation at CoRL 2023"): references-check.md rows 6-7 (Wave 1-2
  list). "generalize across robots and environments": arXiv API abstracts re-read 2026-09-26, GNM
  arXiv:2210.03370 ("broad generalization across environments and embodiments", comment "Presented at
  ICRA 2023"), ViNT ("a foundation model ... for mobile robotics", "hundreds of hours of robotic navigation
  from a variety of different robotic platforms").
- EmbodiedSplat wording (phone capture, GS meshes in Habitat, image-goal navigation fine-tuning) from the
  arXiv:2509.17430 abstract (review-3 evidence list).
- NWM "plan by imagining trajectories": research/world-models.md row NWM ("plans navigation by simulating
  trajectories (abstract)") and §167 ("plans by imagining trajectories").
Dropped from the Wave 15 list (VLA/manipulation detail removed by v6): pi0, LoRA, OFT, SimpleVLA-RL,
Liu et al. (RL for VLA), WMPO, GigaWorld-0, Qwen2.5-VL, Du et al., ASID, SplatSim, ManiSkill3, SIMPLER.
Old (Wave 15) -> new numbers: 1->1, 2->10, 3->14, 5->11, 7->15, 8->23, 10->24, 13->8, 14->9, 17->27,
18->26, 19->25, 21->28, 25->17, 26->18, 27->19, 29->20, 30->16, 31->5, 32->6, 33->29, 34->30.
"we found at most two task-aware capture papers a year" = niches-data.md N1 (2/2/0/2), unchanged.
Reference numbers in the older comments below are pre-Wave-16.
-->
<!-- Wave 15-U (issue #32), 2026-09-26: pivot decision v5 (VLA/VLM + world models, sim-first fine-tuning in
the twin). New paragraphs on open VLAs + PEFT and on VLA fine-tuning in simulation / twins / world models
(flagged as crowded, per the v5 novelty guardrail; research/vla-wm-crowdedness.md, S2 counts Q1 1/3/40/126,
Q2 0/2/42/183 for 2023-2026). The gap now names the v5 components (VLM-guided capture, twin + twin-grounded
world model, joint twin/WM/VLA uncertainty for real trials) and the H4 comparators of §7 (real-only
fine-tuning of the same VLA; strongest existing twin pipeline = TwinRL/RialTo-style, coordinator message
msg_65a79c659e58). 35 refs (limit <= 35).
New refs, verified 2026-09-26 on the Semantic Scholar batch API (title, authors, date, venue, abstract) and
the arXiv abstract page (author comment); details and quotes in research/vla-wm-crowdedness.md §2:
- [8] OpenVLA arXiv:2406.09246, S2 venue CoRL (2024); "970k real-world robot demonstrations", "fine-tuned on
  consumer GPUs via modern low-rank adaptation methods".
- [9] pi0 arXiv:2410.24164 (Black, Brown, Driess, ...), S2 venue arXiv: cited as arXiv.
- [10] NaVILA arXiv:2412.04453 (A.-C. Cheng, Y. Ji, ...); S2 venue "Robotics" (ambiguous), cited as arXiv.
- [11] LoRA arXiv:2106.09685 (E. J. Hu et al.), S2 venue ICLR (ICLR 2022).
- [12] OpenVLA-OFT arXiv:2502.19645; arXiv comment "Accepted to Robotics: Science and Systems (RSS) 2025".
- [15] SimpleVLA-RL arXiv:2509.09674 (H. Li et al.), arXiv.
- [16] J. Liu et al. arXiv:2505.19789; arXiv comment "Accepted by NeurIPS 2025"; PPO > SFT for generalization.
- [17] TwinRL arXiv:2602.09023 (Q. Xu, J. Liu, R. Zhou, S. Shi, ...): "reconstructs a high-fidelity digital
  twin from smartphone-captured scenes", "identifies failure-prone yet informative configurations,
  enabling targeted human-in-the-loop rollouts", "only 20 minutes of on-robot interaction". GitHub
  zhourui9813/TwinRL README says ACM MM 2026 (not otherwise confirmed): cited as arXiv.
- [18] Cosmos arXiv:2501.03575 (Agarwal et al.), arXiv.
- [19] NWM arXiv:2412.03572, doi:10.1109/CVPR52734.2025.01472 (CVPR 2025).
- [20] WMPO arXiv:2511.09515 (F. Zhu et al.): on-policy VLA RL "without interacting with the real environment".
- [21] VLAW arXiv:2602.12063 (Y. Guo, T. Lee, L. Shi, J. Chen, ...): "uses real-world roll-out data to improve
  the fidelity of the world model".
- [22] GigaWorld-0 arXiv:2511.19861: "3D Gaussian Splatting reconstruction, physically differentiable system
  identification" + video generation as a data engine for VLA learning.
- [23] Qwen2.5-VL arXiv:2502.13923 (S. Bai et al.).
- [24] Du et al. arXiv:2303.07280, S2 venue CoLLAs (2023): success detection as VQA with a pretrained VLM.
- [29] AREA3D arXiv:2512.05131 (T. Xu et al.): active reconstruction with "vision-language guidance".
"20 minutes" is TwinRL's figure (abstract). "we found no world model aimed at the regions where the twin is
uncertain" rests on the S2 queries Q7 (world model + twin/Gaussian) and the top-cited hits
(research/vla-wm-crowdedness.md §1, §3), not on a full survey: supervisor to confirm.
Dropped to stay <= 35 (their §9/§12 uses were removed or reworded in the same wave): Vid2Sim, GaussGym,
PhysTwin, Lin et al. (data scaling laws), CASHER, X-Sim, Truong (Rethinking Sim2Real), GenNBV, SimOpt,
Cheng (generalizable DA), Phys2Real, MetaMVUC, AMF, Anwar et al., SureSim, GaussTwin.
Old (Wave 14) -> new numbers: 1->1, 2->2, 3->3, 4->4, 5->5, 8->6, 9->7, 12->13, 15->14, 17->25, 19->26,
20->27, 21->28, 22->30, 23->31, 24->32, 27->33, 32->34, 34->35; 6, 7, 10, 11, 13, 14, 16, 18, 25, 26, 28-31,
33, 35 dropped. Reference numbers in the older comments below are pre-Wave-15.
-->
<!-- Wave 14 (issue #30), 2026-09-26: pivot decision v4 (framing only). Research gap reworded: what is
missing is ONE method that allocates the real data actively at every step, (i)-(iii) = its components
C1-C3 (RQ1-RQ3), (iv) = evidence that it needs less real data than real-only learning and uniform pipelines
(RQ4/H4 (a),(b); the "strongest existing pipeline" of §7/§9 is uniform capture + domain randomization +
random real-data selection, RialTo-style). No references added or renumbered. Trimmed to keep 2 pages. -->
<!--
Wave 13 (issue #29), 2026-09-26: generalized for pivot decision v3 (research/pivot-decision.md: general,
task- and domain-agnostic real-to-sim-to-real; manipulation and navigation equal testbeds; the twin covers
appearance, geometry and physical/dynamic parameters). Navigation-centric framing removed ("in navigation"
gap, "real rollouts"); the gap now asks for the same budget measurement in both domains. System
identification added as the physical side of the twin and of "capture less". 35 refs (limit <= 35).
New refs, verified 2026-09-26 on the arXiv abstract pages (OpenAlex and Semantic Scholar returned 429):
- [9] BayesSim, arXiv:1906.01728 (Ramos, Possas, Fox); arXiv journal-ref "Robotics Science and Systems
  (RSS) 2019"; abstract: "full Bayesian treatment for the parameters of the simulator", trajectories from
  a physical robot, likelihood-free inference.
- [10] PhysTwin, arXiv:2503.17973 (H. Jiang, Hsu, K. Zhang, Yu, S. Wang, ...); ICCV 2025 open-access page
  (openaccess.thecvf.com/ICCV2025) lists it. Abstract: "sparse videos of dynamic objects under
  interaction", "reconstructs complete geometry, infers dense physical properties, and replicates realistic
  appearance".
- [21] ASID, arXiv:2404.12308 (Memmel, Wagenmaker, Zhu, Yin, Fox, ...). Abstract: "leverage a small amount
  of real-world data to autonomously refine a simulation model", "identifying articulation, mass, and other
  physical parameters". Venue not confirmed (dblp/OpenReview lists CoRR only), so cited as arXiv.
Dropped to stay <= 35 (not used in §9/§12): Kadian et al. "Sim2Real Predictivity" (navigation-specific),
Lei et al. mechanistic co-training analysis, CUPID, DataMIL.
Old -> new numbers: 1->1, 2->2, 3->5, 4->6, 5->7, 6->3, 7->4, 8->8, 9->11, 10->12, 11->13, 12->14,
13->15, 14 dropped, 15->16, 16->17, 17->18, 18->19, 19->20, 20->22, 21->23, 22->24, 23->25, 24->26,
25 dropped, 26->27, 27->28, 28->29, 29->30, 30->31, 31/32 dropped, 33->32, 34->33, 35->34, 36->35.
§9 and §12 renumbered in the same wave. Reference entries below the Wave 13 line use the OLD numbers.
"We found no study ... across domains" rests on crowdedness.md 4.2 and the S2 counts below, not on a full
survey: supervisor to confirm.
-->
<!--
Wave 11 (issue #26), 2026-09-26: rewritten for pivot decision v2 (research/pivot-decision.md, binding:
data-efficient real-to-sim-to-real; no benchmark building; representations and uncertainty are tools).
Structure: twins exist -> how much real data (budget studies) -> RQ1 capture less (active reconstruction,
uncertainty) -> RQ2 train robustly (DR, SimOpt, DA, co-training) -> RQ3 few real rollouts (active data
collection, attribution, PPI, twin correction) -> gap mapped to RQ1-RQ4. 35 refs (limit <= 35).
Old numbers -> new (refs kept from wave 9-10, verified then): 1->1 Habitat, 3->2 3DGS, 4->3 EmbodiedSplat,
5->4 Vid2Sim, 6->5 GaussGym, 7->6 RialTo, 8->7 SplatSim, 9->8 ManiSkill3, 10->14 Kadian, 11->15 Truong,
12->34 SIMPLER, 14->13 Maddukuri, 15->23 Cheng, 16->24 Lei, 17->19 ScanNet++, 20->25 DINOv2, 32->30 CUPID,
33->32 PPI, 34->33 SureSim. Tobin [20], Peng [21], Chebotar [22] from the Wave 1-6 list
(research/references-check.md: IROS 2017 doi:10.1109/IROS.2017.8202133, ICRA 2018
doi:10.1109/ICRA.2018.8460528, ICRA 2019 doi:10.1109/ICRA.2019.8793789); Chebotar abstract re-read today
on S2 ("adapt the simulation parameter distribution using a few real world roll-outs").
Dropped (representation-thesis only): linear probes, CKA, V-JEPA 2, Don't Blind Your VLA, OOD-performance
estimation, weights-only accuracy prediction, model zoos, Navon, Kofinas, conformal, FAIL-Detect, SAFE,
TRAK, WorldEval.
New refs, verified 2026-09-26 on the Semantic Scholar batch API (title, authors, year, venue, abstract);
arXiv API returned nothing (429):
- [9] Lin et al. arXiv:2410.18647, ICLR 2025 (S2 venue ICLR; crowdedness.md 4.1).
- [10] Suomela et al. arXiv:2601.09444, doi:10.1109/LRA.2026.3677718, RA-L 11, pp. 6114-6121. Abstract:
  "data diversity is far more important than data quantity"; benefit from existing locations "saturates
  with very little data".
- [11] CASHER arXiv:2412.01770 (Torne, Jain, Yuan, ...); abstract "performance scales superlinearly with
  human effort". S2 venue label "Robotics" (unconfirmed), cited as arXiv.
- [12] X-Sim arXiv:2505.07096 (Dan, Kedia, Chao, ...). "10x less data collection time" is from
  crowdedness.md (abstract tail, read in wave 8).
- [13] "38% on average": crowdedness.md 4.1 from the arXiv:2503.24361 abstract ("an average of 38%").
- [16] FisherRF arXiv:2311.17874 (Jiang, Lei, Daniilidis); Crossref doi:10.1007/978-3-031-72624-8_24,
  Computer Vision - ECCV 2024 (LNCS). "Expected Information Gain" from the abstract.
- [17] GenNBV arXiv:2402.16174, doi:10.1109/CVPR52733.2024.01555 (CVPR 2024).
- [18] Bayes' Rays arXiv:2309.03185, doi:10.1109/CVPR52733.2024.01896 (CVPR 2024), "volumetric
  uncertainty field ... any pre-trained NeRF" (abstract).
- [26] Phys2Real arXiv:2510.11689 (M. Wang, S. Tian, A. Swann, ...): uncertainty over physical parameters,
  training not evaluation (niches-eval.md N4).
- [27] MetaMVUC doi:10.1109/LRA.2025.3544083, RA-L 10, pp. 3644-3651 (Gilles, Furmans, Rayyes): "selecting
  the most informative real-world data samples" (abstract).
- [28] AMF arXiv:2410.05026 (Bagatella, Hubotter, Martius, ...); S2 venue "International Conference on
  Machine Learning". Year 2025 inferred (arXiv Oct 2024, after the ICML 2024 deadline): CONFIRM on the
  PMLR page before printing.
- [29] Anwar et al. arXiv:2502.09829 ("active testing", "cost-aware expected information gain", abstract).
- [31] DataMIL arXiv:2505.09603 (Dass, Khaddaj, Engstrom, ...).
- [35] GaussTwin arXiv:2603.05108 (Cai, Jansonnie, de Farias, ...): "visual correction" driven by
  photometric error (abstract); ICRA 2026 per arXiv comment (novelty-options.md), cited as arXiv.
Review-3 (issue #27), 2026-09-26: R3-F8 inserted [19] Liu, Jiang, Lei, Pandey, Daniilidis, Motee,
"Beyond Uncertainty: Risk-Aware Active View Acquisition for Safe Robot Navigation and 3D Scene
Understanding with FisherRF", arXiv:2403.11396 (arXiv abs page read 2026-09-26; OpenAlex W4392972342,
2024; no journal-ref, so cited as arXiv). It is the closest H1 competitor (niches-data.md N1 "closest
papers"). Old [19]-[35] -> [20]-[36]; §9 renumbered in the same way. R3-F16 GaussGym = "learning
locomotion from pixels" (S2 title/abstract), so "navigation and locomotion". R3-F17 S2 hit counts removed
from the visible text except "at most two ... per year". ScanNet++ wording from the arXiv:2308.11417
abstract. 36 refs.
Hit counts in the text (0-2, 0-1, one paper) are Semantic Scholar counts from research/niches-data.md
(N1 task-aware capture 2/2/0/2; N9 twin-sample weighting 0/0/1/0) and research/pivot-decision.md
(reconstruction uncertainty as training signal 0/0/1/1). "We found no study" rests on these counts and on
crowdedness.md 4.2 ("Nobody varies the capture budget ... as an experimental variable"), not on a full
survey: supervisor to confirm.
-->

# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Learning-based navigation and its data demands.** Photorealistic simulators such as Habitat [1, 2] and
CARLA [3] made large-scale training of embodied agents possible. Wijmans et al. [4] reached near-perfect
point-goal navigation only after 2.5 billion simulated frames, a volume out of reach on physical robots. *Navigation foundation models* (GNM [5], ViNT [6], NoMaD [7]) are trained on pooled
real-robot datasets, and Open X-Embodiment [8] shows that robot learning scales with data. Such data is
costly, and every new environment or platform typically needs more of it.

**The sim-to-real gap.** Policies trained in simulation degrade on real hardware because of differences
in appearance, geometry and dynamics [9, 10]. Kadian et al. [11] showed that simulation can poorly
predict real-world performance and introduced the Sim-vs-Real Correlation Coefficient
(SRCC) to measure it. Truong et al. [12] found that lower-fidelity simulation can transfer better, so
*which* aspects of reality to model is itself open.

**Domain randomization and adaptation.** Domain randomization trains policies on widely varied synthetic
appearance [13, 14] or dynamics [15], so that reality is just another variation, as in agile
flight [16] and drone racing [17]. Its drawbacks are hand-tuned ranges and lower target-domain
performance. Adaptive approaches fit simulation parameters to real rollouts [18], and
domain adaptation [19] reduces, but does not remove, the need for real data.

**Neural scene reconstruction and real-to-sim-to-real.** Neural Radiance Fields [20] and 3D Gaussian
Splatting (3DGS) [21] render photorealistic novel views from ordinary images, 3DGS in real time. This allows
*digital-twin* simulators built from real data; NeRF2Real [22] trained bipedal
skills inside a NeRF of the target scene. Since 2024 the idea has reached navigation: 3DGS twins
transferred visual drone [24–26] and RGB-only legged [27] navigation policies directly to reality,
Vid2Sim [28] built urban simulators from monocular video (a 68.3% real-world success-rate gain over prior
simulators), and ReaDy-Go [29] added moving humans. Closest to this dissertation, EmbodiedSplat [30] fine-tunes
pretrained image-goal policies in meshes from 20–30-minute phone captures, improves real-robot success in a
captured scene and reports high SRCC. These systems use a fixed capture per scene: none varies the amount of
real data or compares against policies trained on real robot experience at matched budgets.

**Digital twins for manipulation.** RialTo [23] robustifies manipulation policies by
reinforcement learning in twins built from little real data; its ablation over 0–15 real demonstrations is
the closest analysis of a real-data budget.
SplatSim [36] renders simulation with Gaussian splats and transfers RGB manipulation policies zero-shot
(86.25% real success vs. 97.5% for policies trained on real data). SIMPLER [37] shows that simulated
evaluation of manipulation policies correlates strongly with real evaluation, and the GPU simulator
ManiSkill3 [38] includes real-world digital-twin environments. Each work builds its twin for one task and
embodiment; whether one pipeline serves navigation and manipulation, and at what capture and compute cost,
has not been measured.

**Learning under distribution shift.** In machine-learning terms the sim-to-real gap is a domain
shift. Unsupervised domain adaptation aligns feature distributions adversarially [31] or at pixel and
feature level [32]. Scaling laws [33] describe how performance grows with data, but not how *real* and
*reconstructed* data trade off. 3D scene datasets (HM3D [34], ScanNet++ [35]) allow a controlled study, with
real captures as a proxy for reality.

**Research gap.** There is no systematic study of the **trade-off between real-data budget and deployed
policy performance** in real-to-sim-to-real learning, nor a twin-building protocol with measured
cost and fidelity across tasks. Also missing are methods that (i) combine twins with augmentation and
representation alignment to generalize to uncaptured scenes and new tasks, and (ii) correct the twin from a
few real rollouts. This dissertation addresses
that gap in navigation, with manipulation as the generalization domain.

### References
[1] M. Savva et al., "Habitat," ICCV, 2019.
[2] A. Szot et al., "Habitat 2.0," NeurIPS, 2021.
[3] A. Dosovitskiy et al., "CARLA," CoRL, 2017.
[4] E. Wijmans et al., "DD-PPO," ICLR, 2020.
[5] D. Shah et al., "GNM," ICRA, 2023.
[6] D. Shah et al., "ViNT," CoRL, 2023.
[7] A. Sridhar et al., "NoMaD," ICRA, 2024.
[8] Open X-Embodiment Collaboration, "Open X-Embodiment," ICRA, 2024.
[9] W. Zhao et al., "Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics," IEEE SSCI, 2020.
[10] S. Höfer et al., "Sim2Real in Robotics and Automation," IEEE T-ASE, 2021.
[11] A. Kadian et al., "Sim2Real Predictivity," IEEE RA-L, 2020.
[12] J. Truong et al., "Rethinking Sim2Real," CoRL, 2022.
[13] J. Tobin et al., "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World," IROS, 2017.
[14] J. Tremblay et al., "Training Deep Networks with Synthetic Data," CVPRW, 2018.
[15] X. B. Peng et al., "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization," ICRA, 2018.
[16] A. Loquercio et al., "Learning High-Speed Flight in the Wild," Sci. Robot., 2021.
[17] E. Kaufmann et al., "Champion-level drone racing using deep reinforcement learning," Nature, 2023.
[18] Y. Chebotar et al., "Closing the Sim-to-Real Loop," ICRA, 2019.
[19] K. Bousmalis et al., "Using Simulation and Domain Adaptation to Improve Efficiency of Deep Robotic Grasping," ICRA, 2018.
[20] B. Mildenhall et al., "NeRF," ECCV, 2020.
[21] B. Kerbl et al., "3D Gaussian Splatting for Real-Time Radiance Field Rendering," ACM TOG, 2023.
[22] A. Byravan et al., "NeRF2Real," ICRA, 2023.
[23] M. Torne et al., "Reconciling Reality through Simulation," RSS, 2024.
[24] A. Quach et al., "Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks," arXiv:2406.15149, 2024.
[25] J. Low et al., "SOUS VIDE," IEEE RA-L, 2025.
[26] Q. Chen et al., "GRaD-Nav," IROS, 2025.
[27] S. Zhu et al., "VR-Robo," IEEE RA-L, 2025.
[28] Z. Xie et al., "Vid2Sim," CVPR, 2025.
[29] S. Yoo et al., "ReaDy-Go," IEEE RA-L, 2026.
[30] G. Chhablani et al., "EmbodiedSplat," ICCV, 2025.
[31] Y. Ganin et al., "Domain-Adversarial Training of Neural Networks," JMLR, 2016.
[32] J. Hoffman et al., "CyCADA," ICML, 2018.
[33] J. Kaplan et al., "Scaling Laws for Neural Language Models," arXiv:2001.08361, 2020.
[34] S. K. Ramakrishnan et al., "Habitat-Matterport 3D Dataset," NeurIPS Datasets and Benchmarks, 2021.
[35] C. Yeshwanth et al., "ScanNet++," ICCV, 2023.
[36] M. N. Qureshi et al., "SplatSim," ICRA, 2025.
[37] X. Li et al., "Evaluating Real-World Robot Manipulation Policies in Simulation," CoRL, 2024.
[38] S. Tao et al., "ManiSkill3," RSS, 2025.
<!-- [31]-[35] added by the coordinator on 2026-09-26 for the ML-first reframing. Titles, first authors and years were verified on OpenAlex (arXiv 1505.07818, 1711.03213, 2001.08361, 2109.08238, 2308.11417). -->

<!-- Wave 6 (issue #15), 2026-09-26: broadened to digital twins across tasks (navigation -> manipulation).
New paragraph "Digital twins for manipulation"; RialTo [23] moved there with its 0-15-demo ablation;
research gap now also names the twin-building protocol (cost + fidelity) and cross-task generalization.
Three new refs, verified 2026-09-26:
- [36] SplatSim: arXiv 2409.10161 (Qureshi, Garg, Yandun, Held, Kantor, Silwal); Crossref
  doi:10.1109/ICRA55743.2025.11128339 (2025 IEEE ICRA). "86.25% vs 97.5%" read from the arXiv abstract.
- [37] SIMPLER: arXiv 2405.05941 (Li, Hsu, Gu, ... Xiao); listed in PMLR vol. 270 (CoRL 2024). "Strong
  correlation" from the abstract (paired sim-and-real evaluations).
- [38] ManiSkill3: arXiv 2410.00425 (Tao, Xiang, Shukla, ... Su); Crossref doi:10.15607/RSS.2025.XXI.021
  (Robotics: Science and Systems XXI). "Real-world digital twins" environments from the arXiv abstract.
- [23] first author written as on arXiv 2403.03949 ("Marcel Torne").
- Refs [32], [34], [35] titles cut at the colon / parenthesis for the page limit.
- Trimmed elsewhere (flight/drone-racing sentence, EmbodiedSplat detail, SRCC sentence) to keep 2 pages;
  all refs [1]-[35] still cited. The "has not been measured" sentence is our reading of [23], [36]-[38],
  not a full survey: supervisor to confirm. -->

<!--
Revision for issue #9 (research/review-1.md F11, F14), 2026-09-26:
- Added [30] EmbodiedSplat. Verified: arXiv 2509.17430v2 (comment "paper accepted at ICCV, 2025"); Crossref
  doi:10.1109/ICCV51701.2025.02359 (2025 IEEE/CVF ICCV); authors G. Chhablani, X. Ye, M. Z. Irshad, Z. Kira.
  Claims read from the FULL TEXT (arXiv v2): iPhone 13 Pro Max + Polycam capture, "20-30 minutes of recording"
  per scene; DN-Splatter meshes in Habitat-Sim; ImageNav policies pre-trained on HM3D/HSSD then fine-tuned;
  real-world evaluation on a Stretch robot in one scene ("lounge"), 10 episodes; SRCC 0.87-0.97 for the
  reconstructed meshes (abstract). The capture procedure is fixed (1000 sampled frames); the paper does not
  vary the capture amount and has no policy trained on real robot data.
- Novelty sentence narrowed. Full texts of old [24]-[31] (now [22]-[29]) were keyword-searched (arXiv PDFs:
  "amount of", "number of demonstrations/images/frames", "real-world data", "minutes of"). Only RialTo [23]
  varies real data: Appendix "RL from different amounts of real-world data" (0, 5, 10, 15 real demos; success
  of RL fine-tuning) and a comparison with behaviour cloning from 15 and 50 real demos. Hence the sentence
  now says the navigation systems do not vary it and names RialTo as the closest (manipulation) analysis.
  Keyword search is not a close reading; the supervisor should still confirm.
- Removed old [4] AirSim and old [21] Progressive Nets (least essential, for the page limit); renumbered.
  Old -> new: 5-20 -> 4-19 (minus 1), 22-31 -> 20-29 (minus 2), EmbodiedSplat = 30.
- Shortened reference entries: titles cut at the colon (main title kept; F14), (first author + "et al." for [9], venue abbreviations CVPRW, Sci. Robot.).
-->

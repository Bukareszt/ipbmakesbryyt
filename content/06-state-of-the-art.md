# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Learning-based navigation and its data demands.** Photorealistic simulators such as Habitat [1, 2] and
CARLA [3] made large-scale training of embodied agents possible. Wijmans et al. [4] reached near-perfect
point-goal navigation, but only after 2.5 billion frames of simulated experience, a volume out of reach on
physical robots. *Navigation foundation models* (GNM [5], ViNT [6], NoMaD [7]) are trained on pooled
real-robot datasets, and Open X-Embodiment [8] shows that robot learning scales with data. Collecting such
data is still costly, and every new environment or platform typically needs more real-world data.

**The sim-to-real gap.** Policies trained in simulation degrade on real hardware because of differences
in appearance, geometry and dynamics [9, 10]. Kadian et al. [11] showed that simulation performance can
be a poor predictor of real-world performance unless the simulator is carefully tuned, and introduced the
Sim-vs-Real Correlation Coefficient (SRCC) to measure it. Truong et al. [12] found that lower-fidelity
simulation with abstracted dynamics can transfer better for navigation. So *which* aspects of reality to
model is itself an open question.

**Domain randomization and adaptation.** Domain randomization trains policies on widely varied synthetic
appearance [13, 14] or dynamics [15], so that reality looks like just another variation. It powers
landmark results in agile flight [16] and drone racing [17]. Its drawbacks are hand-tuned randomization
ranges and robustness bought at the cost of performance in the specific target domain. Adaptive
approaches fit simulation parameters to real rollouts [18], and domain adaptation [19] reduces the amount
of real data needed, but does not remove the need for it.

**Neural scene reconstruction and real-to-sim-to-real.** Neural Radiance Fields [20] and 3D Gaussian
Splatting (3DGS) [21] produce photorealistic novel views from ordinary image captures, and 3DGS renders in
real time. This allows *digital-twin* simulators built from real data: NeRF2Real [22] trained bipedal
skills inside a NeRF of the target scene, and RialTo [23] robustified manipulation policies in digital
twins built from small amounts of real data. Since 2024 the idea has reached navigation: 3DGS simulators
gave direct sim-to-real transfer of visual drone navigation [24–26]; VR-Robo [27] transferred RGB-only
legged goal-reaching policies from a 3DGS twin with mesh-based physics; Vid2Sim [28] built urban
simulators from monocular video and reported a 68.3% real-world success-rate gain over prior simulators;
ReaDy-Go [29] added animated humans as moving obstacles. Closest to this dissertation, EmbodiedSplat [30]
fine-tunes pretrained image-goal navigation policies in meshes reconstructed from 20–30-minute phone
captures of indoor scenes, improves real-robot success rate in a captured scene, and reports high SRCC
for the reconstructed meshes. These navigation systems use a fixed capture per scene: none varies the
amount of real data (capture length, real rollouts) or compares against policies trained on real robot
experience at matched budgets. The closest such analysis, in manipulation, is RialTo's ablation over 0–15
real demonstrations [23]. Multi-room scenes, collision geometry and generalization to environments that
were never captured also remain open.

**Research gap.** There is no systematic study of the **trade-off between real-data budget and deployed
navigation performance** in a real-to-sim-to-real pipeline. We also lack methods that (i) combine
reconstructed scenes with targeted randomization to generalize beyond the captured environments, and
(ii) use a small number of real rollouts to iteratively correct the simulation. This dissertation
addresses that gap.

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
[23] M. Torne Villasevil et al., "Reconciling Reality through Simulation," RSS, 2024.
[24] A. Quach et al., "Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks," arXiv:2406.15149, 2024.
[25] J. Low et al., "SOUS VIDE," IEEE RA-L, 2025.
[26] Q. Chen et al., "GRaD-Nav," IROS, 2025.
[27] S. Zhu et al., "VR-Robo," IEEE RA-L, 2025.
[28] Z. Xie et al., "Vid2Sim," CVPR, 2025.
[29] S. Yoo et al., "ReaDy-Go," IEEE RA-L, 2026.
[30] G. Chhablani et al., "EmbodiedSplat," ICCV, 2025.

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

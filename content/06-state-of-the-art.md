# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Learning-based navigation and its data demands.** Photorealistic simulators such as Habitat [1, 2],
CARLA [3] and AirSim [4] made large-scale training of embodied agents possible. Wijmans et al. [5] reached
near-perfect point-goal navigation, but only after 2.5 billion frames of simulated experience, a volume
out of reach on physical robots. More recent *navigation foundation models* (GNM [6], ViNT [7], NoMaD [8])
are trained on pooled real-robot datasets, and cross-embodiment efforts like Open X-Embodiment [9] show
that robot learning scales with data. Collecting such data is still costly, and every new environment or
platform typically needs additional real-world data.

**The sim-to-real gap.** Policies trained in simulation degrade on real hardware because of differences
in appearance, geometry and dynamics [10, 11]. Kadian et al. [12] showed that simulation performance can
be a poor predictor of real-world performance unless the simulator is carefully tuned, and introduced the
Sim-vs-Real Correlation Coefficient (SRCC) to measure how well it predicts. Truong et al. [13] found, surprisingly,
that lower-fidelity simulation with abstracted dynamics can transfer better for navigation. So *which*
aspects of reality to model is itself an open research question.

**Domain randomization and adaptation.** Domain randomization trains policies on widely varied synthetic
appearance [14, 15] or dynamics [16], so that reality looks like just another variation. It powers
landmark results in agile flight [17] and drone racing [18]. Its drawbacks are that randomization ranges
are hand-tuned and that robustness is bought at the cost of performance in the specific target domain.
Adaptive approaches close the loop by fitting simulation parameters to real rollouts [19]. Domain
adaptation methods [20] and progressive networks [21] reduce the amount of real data needed, but they do
not remove the need for it.

**Neural scene reconstruction and real-to-sim-to-real.** Neural Radiance Fields [22] and 3D Gaussian
Splatting (3DGS) [23] produce photorealistic novel views from ordinary image captures, and 3DGS renders in
real time. This allows *digital-twin* simulators built from real data: NeRF2Real [24] trained vision-guided
bipedal skills inside a NeRF of the target scene, and RialTo [25] robustified manipulation policies with
reinforcement learning in digital twins built from small amounts of real-world data. Since 2024 the idea
has reached navigation. Gaussian-splatting simulators gave direct sim-to-real transfer of visual drone
navigation policies [26–28]; VR-Robo [29] transferred RGB-only legged goal-reaching policies trained in a
3DGS twin with mesh-based physics; Vid2Sim [30] built interactive urban simulators from monocular video and
reported a 68.3% real-world success-rate gain over agents trained with prior simulators; and ReaDy-Go [31]
added animated human avatars to train for moving obstacles. These systems are typically trained in one or a
few captured scenes, and, to our knowledge, none measures how deployed performance depends on the amount of
real data collected. Large multi-room scenes, accurate collision geometry and generalization to environments
that were never captured also remain open.

**Research gap.** There is no systematic study of the **trade-off between real-data budget and deployed
navigation performance** in a real-to-sim-to-real pipeline. We also lack methods that (i) combine
reconstructed scenes with targeted randomization to generalize beyond the captured environments, and
(ii) use a small number of real rollouts to iteratively correct the simulation. This dissertation
addresses that gap.

### References
[1] M. Savva et al., "Habitat: A Platform for Embodied AI Research," ICCV, 2019.
[2] A. Szot et al., "Habitat 2.0: Training Home Assistants to Rearrange their Habitat," NeurIPS, 2021.
[3] A. Dosovitskiy et al., "CARLA: An Open Urban Driving Simulator," CoRL, 2017.
[4] S. Shah et al., "AirSim: High-Fidelity Visual and Physical Simulation for Autonomous Vehicles," FSR, 2017.
[5] E. Wijmans et al., "DD-PPO: Learning Near-Perfect PointGoal Navigators from 2.5 Billion Frames," ICLR, 2020.
[6] D. Shah et al., "GNM: A General Navigation Model to Drive Any Robot," ICRA, 2023.
[7] D. Shah et al., "ViNT: A Foundation Model for Visual Navigation," CoRL, 2023.
[8] A. Sridhar et al., "NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration," ICRA, 2024.
[9] Open X-Embodiment Collaboration, "Open X-Embodiment: Robotic Learning Datasets and RT-X Models," ICRA, 2024.
[10] W. Zhao, J. P. Queralta, T. Westerlund, "Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey," IEEE SSCI, 2020.
[11] S. Höfer et al., "Sim2Real in Robotics and Automation: Applications and Challenges," IEEE T-ASE, 2021.
[12] A. Kadian et al., "Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?," IEEE RA-L, 2020.
[13] J. Truong et al., "Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation," CoRL, 2022.
[14] J. Tobin et al., "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World," IROS, 2017.
[15] J. Tremblay et al., "Training Deep Networks with Synthetic Data: Bridging the Reality Gap by Domain Randomization," CVPR Workshops, 2018.
[16] X. B. Peng et al., "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization," ICRA, 2018.
[17] A. Loquercio et al., "Learning High-Speed Flight in the Wild," Science Robotics, 2021.
[18] E. Kaufmann et al., "Champion-level drone racing using deep reinforcement learning," Nature, 2023.
[19] Y. Chebotar et al., "Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience," ICRA, 2019.
[20] K. Bousmalis et al., "Using Simulation and Domain Adaptation to Improve Efficiency of Deep Robotic Grasping," ICRA, 2018.
[21] A. A. Rusu et al., "Sim-to-Real Robot Learning from Pixels with Progressive Nets," CoRL, 2017.
[22] B. Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis," ECCV, 2020.
[23] B. Kerbl et al., "3D Gaussian Splatting for Real-Time Radiance Field Rendering," ACM TOG (SIGGRAPH), 2023.
[24] A. Byravan et al., "NeRF2Real: Sim2real Transfer of Vision-guided Bipedal Motion Skills using Neural Radiance Fields," ICRA, 2023.
[25] M. Torne Villasevil et al., "Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation," RSS, 2024.
[26] A. Quach et al., "Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks," arXiv:2406.15149, 2024.
[27] J. Low et al., "SOUS VIDE: Cooking Visual Drone Navigation Policies in a Gaussian Splatting Vacuum," IEEE RA-L, 2025.
[28] Q. Chen et al., "GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics," IROS, 2025.
[29] S. Zhu et al., "VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion," IEEE RA-L, 2025.
[30] Z. Xie et al., "Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation," CVPR, 2025.
[31] S. Yoo et al., "ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles," IEEE RA-L, 2026.

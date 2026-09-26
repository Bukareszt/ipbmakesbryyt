# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

**Platform and data collection.** Experiments will use a mobile robot platform <!-- TODO: e.g. wheeled UGV
(TurtleBot 4 / Clearpath Jackal) or quadruped; confirm availability at K46 --> with an RGB-D camera, a 2D/3D
LiDAR, an IMU and wheel odometry, running ROS 2. A standard capture protocol will record short handheld or
robot-mounted RGB(-D) video of each target environment (several minutes per scene), plus a small number of
teleoperated or autonomous trajectories for evaluation and refinement. The data budget (capture minutes,
number of real rollouts) is an explicit experimental variable (RQ2).

**Real-to-sim reconstruction (RQ1).** Camera poses will be estimated with Structure-from-Motion
(COLMAP) or SLAM. Photorealistic appearance will be modeled with 3D Gaussian Splatting (with NeRF as a
baseline). Collision and depth geometry will come from depth fusion (TSDF) or mesh extraction. The scene
will be imported into a GPU-accelerated simulator (NVIDIA Isaac Sim / Isaac Lab or Habitat), with rendering
from the reconstruction and physics from the extracted geometry. Fidelity will be validated by
image-quality metrics (PSNR, SSIM, LPIPS) against held-out real views, and by geometric error against
LiDAR scans.

**Policy learning.** Two complementary paradigms will be studied: (i) deep reinforcement learning (PPO,
DD-PPO) for point-goal and image-goal navigation, trained at scale in the reconstructed environments; and
(ii) imitation learning and fine-tuning of pretrained navigation models (e.g. GNM, ViNT, NoMaD) using
trajectories generated in simulation. Observations are RGB(-D) and optionally LiDAR. Actions are velocity
commands.

**Generalization through augmentation (RQ3).** Reconstructed scenes will be augmented by inserting and
rearranging objects, randomizing lighting and appearance, modeling sensor noise and latency, randomizing
dynamics (friction, mass, actuation delays), and adding simulated dynamic obstacles and pedestrians. An
ablation study will compare: generic simulator + domain randomization; reconstruction only;
reconstruction + augmentation.

**Closing the loop (RQ4).** Real-world rollouts will be compared with simulated replays of the same
trajectories. The discrepancy will be used to update the reconstruction (e.g. re-capturing
poorly-reconstructed regions) and to fit dynamics/sensor parameters (system identification, adaptive
randomization in the style of SimOpt). The policy is then fine-tuned in the corrected simulation. The
number of real rollouts per iteration is kept small and reported.

**Evaluation.** Real-world experiments in several indoor environments at PWr (offices, corridors,
laboratories), both captured (target) and uncaptured (unseen), with fixed start/goal sets and repeated
trials. Metrics: success rate, SPL (Success weighted by Path Length), collision rate, time to goal, and
intervention count. Sim-to-real predictivity will be measured with the Sim2Real Correlation Coefficient
(SRCC) (H3). For RQ2 and H4 we will plot success rate against the real-data budget. Results will be
reported with confidence intervals and appropriate statistical tests (e.g. bootstrap, Wilcoxon).

**Baselines.** A policy trained in a generic simulator (with and without domain randomization); a policy
trained only on real data at matched and larger budgets; pretrained navigation models zero-shot and
fine-tuned on real data.

**Reproducibility.** Code, configuration and reconstructed scenes will be versioned and released
publicly where permitted. Experiments will be tracked (e.g. Weights & Biases). Compute will use
departmental GPUs and PLGrid/WCSS resources <!-- TODO confirm -->.

# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The research follows four stages (I–IV), matching the schedule in §3. For each stage we give the method,
the data and equipment, the metric, and the success criterion. Stage II (H1 and the real-data budget,
RQ1–RQ2) is the core of the dissertation; Stages III–IV extend it.

**Test stand and data.** Real-robot experiments are planned in collaboration with the K29 "Denali"
Autonomous Robots Laboratory at PWr, which operates Pioneer 3-DX and DrRobot Jaguar 4x4 mobile robots
under ROS 2 *(to be confirmed with the supervisor)*. The robot will carry an RGB-D camera and use wheel
odometry; if the lab has no suitable sensor, one will be bought from an SzD Minigrant.
<!-- UNVERIFIED: RGB-D/LiDAR availability at Denali; Minigrant call ~Jan 2027 --> A fixed capture
protocol records short RGB-D video of each environment (minutes per scene) and a small number of
teleoperated trajectories. The **real-data budget** (capture minutes, number of real rollouts) is an
explicit experimental variable. **Fallback** if robot access is delayed: offline evaluation on public
real-world navigation datasets (e.g. SCAND, RECON) <!-- verified: SCAND = Karnan et al., IEEE RA-L 2022, doi:10.1109/LRA.2022.3184025, arXiv:2203.15041; RECON = Shah et al., CoRL 2021, arXiv:2104.05859. Denali robots: https://denali.kcir.pwr.edu.pl/robots.php (research/resources.md §1) --> and our own hand-held RGB-D captures, with real-robot
deployment moved to the next semester. Compute: WCSS Lem (NVIDIA H100) and PLGrid allocations, plus
departmental GPUs <!-- UNVERIFIED: K46 GPU servers -->.

**Stage I – real-to-sim reconstruction (RQ1; sem. 2–3).**
- *Method:* camera poses from Structure-from-Motion (COLMAP) or RGB-D SLAM; appearance from 3D Gaussian
  Splatting (NeRF as baseline); collision geometry from TSDF depth fusion or mesh extraction; import into
  a GPU simulator (Isaac Sim / Isaac Lab or Habitat) with rendering from the reconstruction and physics
  from the mesh.
- *Data/equipment:* RGB-D captures of ≥ 2 indoor scenes at PWr (corridors, labs, offices).
- *Metric:* PSNR, SSIM and LPIPS on held-out real views; depth and geometric error against sensor depth.
- *Success criterion:* the scene is navigable in simulation (no mesh holes on robot paths) and its
  held-out rendering quality is in the range reported for 3DGS.

**Stage II – policy learning and real-robot transfer (RQ1–RQ2, H1, H4; sem. 3–4).**
- *Method:* (i) deep reinforcement learning (PPO / DD-PPO) for point-goal and image-goal navigation,
  trained at scale in the reconstructed scenes; (ii) imitation learning and fine-tuning of pretrained
  navigation models (GNM, ViNT, NoMaD) on trajectories generated in simulation. Observations: RGB(-D);
  actions: velocity commands.
- *Baselines:* the same policy trained in a generic simulator (with and without domain randomization);
  a policy trained only on real data at matched and larger budgets; pretrained models zero-shot.
- *Metric:* success rate (primary), SPL, collision rate and interventions, on 20 fixed start–goal pairs
  × 3 trials per policy and environment (the §7 protocol); success rate as a function of the real-data
  budget B.
- *Success criterion:* H1 decision rules in §7: higher success rate than the generic-simulator policy
  (one-sided, α = 0.05) and non-inferiority to a policy trained on ≥ 10× more real data (margin
  δ = 10 pp), in ≥ 2 target environments. The first real-robot pilot (one scene) is completed in
  semester 3, the H1 study in ≥ 2 environments by the end of semester 4 (before the mid-term).

**Stage III – closing the loop and sim-to-real validation (RQ4, H3, H4; sem. 5).**
- *Validation protocol:* for every evaluated policy, paired rollouts in simulation and on the robot use
  the same start–goal pairs. Over ≥ 10 policy variants we compute the **Sim-vs-Real Correlation
  Coefficient (SRCC)** between simulated and real success/SPL for (a) the reconstructed and (b) the
  generic simulator, and relate per-scene fidelity (Stage I metrics) to the size of the transfer gap.
- *Method:* the discrepancy between real and replayed trajectories is used to update the scene (re-capture
  of poorly reconstructed regions) and to fit dynamics and sensor parameters (system identification,
  adaptive randomization in the style of SimOpt); the policy is then fine-tuned in the corrected
  simulation. The number of real rollouts per iteration is small and reported.
- *Metric:* SRCC with bootstrap confidence intervals; real rollouts needed to reach a target success rate,
  compared with real-data-only training.
- *Success criterion:* H3 and H4 decision rules in §7: the 95% CI of the SRCC difference excludes 0 (and
  SRCC does not drop after refinement); the upper 95% CI bound of the budget ratio B_pipeline/B_real to
  reach the target success rate is ≤ 0.1.
- *Fallback if validation fails* (low SRCC or no gain): the result is reported as a negative finding, the
  error is attributed to appearance, geometry or dynamics by ablation, and the corresponding model
  (e.g. dynamics identification only) is corrected; Stage II conclusions do not depend on this stage.

**Stage IV – generalization and consolidation (RQ3, H2, H4; sem. 6–7).**
- *Method:* augmentation of reconstructed scenes: object insertion and rearrangement, lighting and
  appearance randomization, sensor noise and latency, dynamics randomization, simulated pedestrians.
  Ablation: generic simulator + domain randomization vs. reconstruction only vs. reconstruction +
  augmentation.
- *Data/equipment:* captured (target) and **uncaptured** (unseen) real environments at PWr and, during the
  foreign visit, at the host lab.
- *Metric:* success rate and SPL in unseen environments; the full real-data-budget curve over all
  baselines.
- *Success criterion:* H2 decision rule in §7 (reconstruction + augmentation better than each component
  alone in unseen environments).

**Statistics and reproducibility.** All real-robot comparisons follow the common protocol of §7: the same
20 start–goal pairs × 3 trials per method and environment, one-sided tests at α = 0.05 with Holm
correction within each hypothesis, and bootstrap confidence intervals over start–goal pairs. Margins and
targets are fixed in the project repository before the Stage II real-robot runs. Code, configurations
and reconstructed scenes are versioned and released where permitted; experiments are logged (e.g.
Weights & Biases).

**Dissemination.** Each stage is published in listed venues: IEEE RA-L, RSS, IROS or Robotics and
Autonomous Systems (§3, §11).

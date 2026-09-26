# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The research follows four stages (I–IV) matching §3; for each we give the method, data, metric and
success criterion. Stage II (H1 and the real-data budget,
RQ1–RQ2) is the core of the dissertation; Stages III–IV extend it.

**Test stand and data.** Real-robot experiments use a mobile-robot platform available at PWr (planned
cooperation with the K29 "Denali" Autonomous Robots Laboratory, which operates Pioneer 3-DX and DrRobot
Jaguar 4x4 robots under ROS 2; terms agreed in sem. 3, T3.2a). The robot carries an RGB-D camera and uses
wheel odometry; if no suitable sensor is available, one is bought from an SzD Minigrant.
<!-- UNVERIFIED: RGB-D/LiDAR availability at Denali; Minigrant call ~Jan 2027 --> A fixed capture
protocol records short RGB-D video of each environment (minutes per scene) and a small number of
teleoperated trajectories. The **real-data budget** (capture minutes, number of real rollouts) is an
explicit experimental variable. *Estimated robot time* (at ~2 min per episode including reset): about
35 robot-hours in Stage II (6 policies × 120 episodes, plus teleoperated data for the real-data-only
baseline) and about 20 in Stage III (≥ 10 variants × 60 episodes); resets are scripted and the H1 core
comparisons are run first. **Fallback** if robot access is delayed: offline evaluation on public
real-world navigation datasets (e.g. SCAND, RECON) <!-- verified: SCAND = Karnan et al., IEEE RA-L 2022, doi:10.1109/LRA.2022.3184025, arXiv:2203.15041; RECON = Shah et al., CoRL 2021, arXiv:2104.05859. Denali robots: https://denali.kcir.pwr.edu.pl/robots.php (research/resources.md §1) --> with real-robot deployment moved to the next semester. Compute: WCSS Lem (NVIDIA H100)
and PLGrid allocations (to be applied for), plus departmental GPUs <!-- UNVERIFIED: K46 GPU servers -->.

**Stage I – real-to-sim reconstruction (RQ1; sem. 3).**
- *Method:* camera poses from Structure-from-Motion (COLMAP) or RGB-D SLAM; appearance from 3D Gaussian
  Splatting (NeRF as baseline); collision geometry from TSDF depth fusion or mesh extraction; import into
  a GPU simulator (Isaac Sim / Isaac Lab or Habitat, chosen in T3.1) with rendering from the
  reconstruction and physics from the mesh.
- *Data/equipment:* RGB-D captures of ≥ 2 indoor scenes at PWr (corridors, labs, offices).
- *Metric and success criterion:* PSNR, SSIM and LPIPS on held-out real views, and depth error against
  sensor depth. A scene passes if its held-out PSNR is within a margin X dB of the value reported for 3DGS
  [21] on comparable indoor scenes (X fixed in the repository before Stage II) and its collision mesh has
  no holes on the evaluation paths.

**Stage II – policy learning and real-robot transfer (RQ1–RQ2, H1, H4; sem. 3–4).**
- *Method:* (i) deep reinforcement learning (PPO / DD-PPO) for point-goal and image-goal navigation,
  trained at scale in the reconstructed scenes; (ii) imitation learning and fine-tuning of pretrained
  navigation models (GNM, ViNT, NoMaD) on trajectories generated in simulation. Input: RGB(-D); output:
  velocity commands.
- *Baselines:* the same policy trained in a generic simulator (public scene dataset, with and without
  domain randomization); a pretrained model fine-tuned by behaviour cloning on teleoperated real
  trajectories at matched and ≥ 10× larger budgets; pretrained models zero-shot.
- *Metric and success criterion:* success rate (primary), SPL, collisions and interventions under the §7
  protocol, and success rate as a function of the real-data budget B; H1 decision rules in §7. The
  real-robot pilot (one scene) runs in sem. 3 if robot access is agreed, otherwise at the start of sem. 4;
  the H1 study in ≥ 2 environments is completed by the end of sem. 4 (before the mid-term).

**Stage III – closing the loop and sim-to-real validation (RQ4, H3, H4; sem. 5).**
- *Validation protocol:* paired simulated and real rollouts on the same start–goal pairs. Over ≥ 10 policy variants we compute the **Sim-vs-Real Correlation
  Coefficient (SRCC)** between simulated and real success/SPL for (a) the reconstructed and (b) the
  generic simulator, and relate per-scene fidelity (Stage I metrics) to the transfer gap.
- *Method:* the discrepancy between real and replayed trajectories is used to update the scene (re-capture
  of poorly reconstructed regions) and to fit dynamics and sensor parameters (system identification,
  adaptive randomization in the style of SimOpt); the policy is then fine-tuned in the corrected
  simulation. The number of real rollouts per iteration is small and reported.
- *Metric and success criterion:* SRCC with bootstrap confidence intervals; real rollouts needed to reach
  the target success rate compared with real-data-only training; H3 and H4 decision rules in §7.
- *Fallback* (low SRCC or no gain): reported as a negative finding, with the error attributed to
  appearance, geometry or dynamics by ablation; Stage II conclusions do not depend on this stage.

**Stage IV – generalization and consolidation (RQ3, H2, H4; sem. 6–7).**
- *Method:* augmentation of reconstructed scenes: object insertion and rearrangement, lighting and
  appearance randomization, sensor noise and latency, dynamics randomization, simulated pedestrians.
  Ablation: generic simulator + domain randomization vs. reconstruction only vs. reconstruction +
  augmentation.
- *Data/equipment:* captured (target) and **uncaptured** (unseen) real environments at PWr and, during the
  foreign visit, at the host lab.
- *Metric and success criterion:* success rate and SPL in unseen environments (H2 decision rule in §7);
  the full real-data-budget curve over all baselines.

**Statistics, reproducibility and dissemination.** All real-robot comparisons follow the §7 protocol.
Code, configurations and scenes are versioned, logged and released where permitted. Each stage is published in listed venues: IEEE RA-L, RSS, IROS or
Robotics and Autonomous Systems (§3, §11).

<!--
Revision for issue #9 (research/review-1.md), 2026-09-26:
- F5: "(to be confirmed with the supervisor)" removed; wording = option (c) of research/resources.md §1
  (collaboration with K29 is planned, not agreed). F2: "our own hand-held RGB-D captures" removed from the
  fallback because sensor availability is unconfirmed (CONFIRM with the student).
- F9: robot-hours are the reviewer's estimate (research/review-1.md F9) under an ASSUMED ~2 min per episode
  incl. reset; 6 policies = recon, generic, generic+DR, real-only at 2 budgets, zero-shot; 120 episodes =
  2 environments × 60 (§7). Teleoperated data for real-only at ≥ 10× budget ≈ 10 h. CONFIRM real episode
  duration after the pilot.
- F10: real-data-only baseline = behaviour cloning / fine-tuning on teleoperated trajectories (as §7).
- F15: "Statistics and reproducibility" merged with "Dissemination"; Metric + Success criterion merged.
- F17: PLGrid/WCSS "to be applied for" (no allocation held, resources.md §2); the simulator is chosen in
  T3.1 because the sem. 1 tool-selection note is not confirmed (F2). Stage I moved to sem. 3 (was 2–3).
- F18: Stage I criterion made checkable (PSNR margin X fixed before Stage II, as the other margins). [21] =
  Kerbl et al. 3DGS after the §6 renumbering.
-->

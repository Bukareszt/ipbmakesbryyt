# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The research follows four stages (I–IV) matching §3; for each we give the method, data, metric and success
criterion. Stages I–II (H1 and the real-data budget, RQ1–RQ2) are the core of the dissertation; Stages III–IV
extend it. Every hypothesis is decided on public benchmarks and datasets and validated on a real robot (the
three evaluation tiers of §7).

**Data and evaluation tiers.** *Tier A (benchmark, primary):* ≥ 10 public indoor scenes that have both real
video and a reference 3D scan, e.g. ScanNet++ (laser scans, DSLR images and iPhone RGB-D video of real
rooms); the reference scan, loaded into a GPU simulator (Habitat or Isaac Sim / Isaac Lab, chosen in T3.1),
is the target domain, and some scenes are held out as uncaptured. Large public scene sets (e.g. HM3D) train
the generic baseline. *Tier B (real-world datasets):* held-out real frames and trajectories from public
navigation datasets (e.g. SCAND, RECON) for representation metrics and offline checks. *Tier C (real-robot
validation):* ≥ 2 PWr environments with a mobile robot (planned cooperation with the K29 "Denali" Autonomous
Robots Laboratory: Pioneer 3-DX and DrRobot Jaguar 4x4 under ROS 2; agreement in T3.2), with an RGB-D camera
and wheel odometry; a sensor is bought from an SzD Minigrant if needed.
<!-- UNVERIFIED: RGB-D/LiDAR availability at Denali; Minigrant call ~Jan 2027 --> The **real-data budget** B
(minutes of target-domain data: capture video plus real experience) is an explicit experimental variable: on
tier A it is set by subsampling the scene's video and the number of rollouts in the reference scan.
*Estimated robot time:* about 16 robot-hours per validation campaign (4 policies × 120 episodes at ~2 min per
episode including reset), in sem. 4–5 and sem. 7. Compute: WCSS Lem (NVIDIA H100) and PLGrid allocations (to
be applied for), plus departmental GPUs <!-- UNVERIFIED: K46 GPU servers -->.

**Stage I – learning from reconstructions (RQ1; sem. 3).**
- *Method:* camera poses from Structure-from-Motion (COLMAP) or the dataset's poses; appearance from 3D
  Gaussian Splatting (NeRF as baseline); collision geometry from depth fusion or mesh extraction; import into
  the simulator with rendering from the reconstruction and physics from the mesh.
- *Metric and success criterion:* PSNR, SSIM and LPIPS on held-out views and depth error against the
  reference scan. A scene passes if its held-out PSNR is within a margin X dB of the value reported for 3DGS
  [21] on comparable indoor scenes (X fixed in the repository before Stage II) and its collision mesh has no
  holes on the evaluation paths.

**Stage II – learning under a real-data budget (RQ1–RQ2, H1, H4; sem. 3–4).**
- *Method:* (i) deep reinforcement learning (PPO / DD-PPO) for point-goal and image-goal navigation, trained
  at scale in the reconstructions; (ii) imitation learning and fine-tuning of pretrained navigation models
  (GNM, ViNT, NoMaD) on trajectories generated in simulation. Input: RGB(-D); output: velocity commands.
- *Baselines (§7):* the same policy trained on generic public scenes with domain randomization; the
  real-data-only baseline, a pretrained model fine-tuned by behaviour cloning on target-domain trajectories
  of budget B, at matched and ≥ 10× larger budgets; pretrained models zero-shot.
- *Metric and success criterion:* success rate (primary), SPL and collisions as a function of B; budget–SR
  scaling curves fitted per method; H1 and H4 decision rules in §7 on tier A, with the robot pilot (tier C,
  one environment) as the first validation.

**Stage III – predictivity and correction (RQ4, H3, H4; sem. 4–5).**
- *Validation protocol:* paired rollouts in simulation and in the target domain on the same start–goal
  pairs. Over ≥ 10 policy variants we compute the **Sim-vs-Real Correlation Coefficient (SRCC)** between
  simulated and target-domain success/SPL for the reconstructed and the generic simulator, on tier A and on
  the robot (tier C), and relate per-scene fidelity (Stage I) to the transfer gap.
- *Method:* the discrepancy between target-domain and replayed trajectories updates the scene (re-capture of
  poorly reconstructed regions) and fits dynamics and sensor parameters (system identification, adaptive
  randomization in the style of SimOpt); the policy is then fine-tuned in the corrected simulation.
- *Metric and success criterion:* SRCC with bootstrap confidence intervals; target-domain rollouts needed to
  reach the target success rate compared with real-data-only learning; H3 and H4 decision rules in §7.
- *Fallback* (low SRCC or no gain): reported as a negative finding, with the error attributed to appearance,
  geometry or dynamics by ablation; Stage II conclusions do not depend on this stage.

**Stage IV – generalization and representations (RQ3, H2, H4; sem. 6–7).**
- *Method:* augmentation of reconstructed scenes (object insertion and rearrangement, lighting and
  appearance randomization, sensor noise, simulated pedestrians) and **representation alignment**: an
  auxiliary objective that brings encoder features of reconstructed and real observations of the same place
  together (e.g. contrastive or distribution-matching losses). Ablation: generic + randomization vs.
  reconstruction only vs. reconstruction + augmentation vs. + alignment.
- *Data:* held-out uncaptured scenes (tier A), real frames (tier B), and uncaptured real environments at PWr
  and, during the foreign visit, at the host lab (tier C).
- *Metric and success criterion:* success rate and SPL in uncaptured scenes, and the feature-distribution
  distance between reconstructed and real frames (H2 rule in §7); the full budget curve over all baselines
  (H4, sem. 7).

**Statistics and reproducibility.** All comparisons follow the §7 protocol, which is pre-registered in the
project repository before each stage; changes are logged with reasons. Code, configurations and
reconstructed scenes are versioned and released where the dataset licences permit.

<!--
Issue #12 (coordinator decisions, 2026-09-26): AI/ML PhD; public benchmarks/datasets first (tiers A/B of §7,
issue #11), real robot = validation (tier C); no venue names in §9 (dissemination is in §3, §11, §12).
- ScanNet++: Yeshwanth, Liu, Nießner, Dai, ICCV 2023, arXiv:2308.11417 (checked 2026-09-26: 460 scenes,
  laser scans + 33 MP DSLR images + iPhone RGB-D). It is a candidate for tier A ("real video + reference
  scan", as required by §7); licence terms for releasing derived reconstructions: UNVERIFIED.
- HM3D: Ramakrishnan et al., arXiv:2109.08238 (checked 2026-09-26: 1,000 building-scale reconstructions of
  real spaces). Not yet in §6 references; add there if kept (owner of §6).
- SCAND = Karnan et al., IEEE RA-L 2022, doi:10.1109/LRA.2022.3184025; RECON = Shah et al., CoRL 2021,
  arXiv:2104.05859. Denali robots: https://denali.kcir.pwr.edu.pl/robots.php (research/resources.md §1).
- Robot time: estimate under an ASSUMED ~2 min per episode incl. reset; 4 policies (recon, generic,
  real-only, full pipeline) × 120 episodes (2 environments × 20 pairs × 3 trials, §7 tier C) = 960 min
  = 16 h. Was ~55 h in the robot-first plan (review-1 F9). CONFIRM real episode duration after the pilot.
- Stage order kept (III = predictivity/correction, IV = generalization) because §7 refers to Stage IV for H2.
- Earlier revision notes (issue #9, F2, F5, F10, F15, F17, F18) still apply: collaboration phrased as planned;
  simulator chosen in T3.1; PLGrid/WCSS to be applied for; Stage I criterion with margin X.
-->

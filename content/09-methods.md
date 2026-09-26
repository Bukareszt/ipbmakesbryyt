# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The research follows four stages (I–IV) that match §3 and the research questions of §7. For each stage we
give the method, data, metric and success criterion. The student uses existing open-source 3D Gaussian
Splatting (3DGS) pipelines and simulators and does not develop new ones. Stages I–II (RQ1–RQ2) are the core;
Stages III–IV (RQ3–RQ4) build on them.

**Data and evaluation tiers.** *Tier A (proxy reality; decides the hypotheses):* ≥ 10 public indoor scenes
that have real captures and a reference laser scan, e.g. ScanNet++ [17]. The reference scan, rendered in a
GPU simulator (Habitat [1] or an Isaac-based 3DGS renderer such as GaussGym [6], chosen in T3.1), is the
"real" target domain. The twin is a 3DGS reconstruction built from a subsample of the scene's real capture.
The **capture budget** (≥ 4 levels of capture minutes or views) is set by subsampling. Some scenes are held
out. *Tier B (real outcomes):* public real-world navigation datasets for representation metrics and
published paired sim/real evaluations of manipulation policies (SIMPLER [12]). *Tier C (validation only):*
≥ 2 PWr environments with a mobile robot (planned cooperation with the K29 "Denali" Autonomous Robots
Laboratory; agreement in T3.2), RGB-D camera and wheel odometry. *Compute:* WCSS Lem (NVIDIA H100) and PLGrid
allocations (to be applied for) <!-- UNVERIFIED: K46 GPU servers; RGB-D availability at Denali -->.

**Stage I – paired-frame benchmark and gap localization (RQ1, H1; sem. 3–4).**
- *Benchmark:* for every scene and capture budget we render twin frames at the camera poses of held-out real
  frames, which gives **paired real/twin frames of the same pose**, plus per-scene fidelity (PSNR, SSIM,
  LPIPS, depth error) and cost (capture minutes, GPU-hours).
- *Encoders:* ≥ 10 frozen image and video encoders used as policy backbones (e.g. DINOv2 [20], CLIP-type,
  V-JEPA 2 [21]), plus the encoders inside twin-trained policies.
- *Method:* for each layer, **linear CKA** [19] between real and twin activations, and **linear probes** [18]
  trained on twin features and tested on real features (targets: depth, semantic class, relative goal
  direction). Gap = 1 − CKA and the probe-accuracy drop.
- *Success criterion (H1):* concentration of the gap in layers, monotonic decrease with the capture budget,
  differences between encoders, and a robustness ranking that predicts downstream twin→real success rate
  (SR) with Spearman ρ ≥ 0.6. Downstream SR comes from navigation policies trained on each frozen encoder
  in the twins and tested in tier A. Decision rules are those of §7.

**Stage II – policy zoo and transfer forecasting (RQ2, H2; sem. 4–5).**
- *Policy zoo:* ≥ 200 point-goal and image-goal navigation policies trained in the twins by reinforcement
  learning (PPO / DD-PPO) and imitation of a privileged planner. They vary scene, capture budget, encoder,
  architecture, training data and seed. Each policy is evaluated in its twin and in tier A, which gives the
  label: the twin→real SR gap. Small policies and shared frozen encoders keep the zoo within academic compute
  (a pilot in sem. 3 fixes the final size).
- *Predictors:* (i) a graph neural network over per-layer hidden-state statistics on a fixed probe set of
  twin frames (the student's prior method for forecasting from hidden states); (ii) weight-space
  metanetworks [26, 27]. *Baselines:* twin SR alone, image fidelity (PSNR/LPIPS), and simulator-level
  predictivity (SRCC-style rollout estimates [10]). Splits are by held-out scene. Ablations keep fidelity
  fixed and vary the policy, so that the predictor cannot rely only on twin quality.
- *Failure monitors:* hidden-state failure scores (in the style of [29, 30]) with thresholds set by split
  conformal prediction [28] at 90% coverage in the twin; coverage is measured on tier A and tier B.
- *Success criterion (H2):* ≥ 20% lower MAE than the best baseline (lower 95% bound of the reduction > 0),
  and real coverage ≥ 85% (ε = 5 pp).

**Stage III – budget-allocation experiments (RQ3, H3; sem. 6).**
- *Levers:* (a) weighting of twin training data by representation distance to a small real set; (b)
  capture selection, i.e. which scenes or regions to (re)capture, guided by the localized gap from Stage I;
  (c) rollout selection, i.e. which real rollouts to collect, guided by the Stage II forecasts and their
  uncertainty. Real SR is estimated from few rollouts with prediction-powered inference [33, 34].
- *Baselines:* uniform and random allocation of the same budget. Analysis: attribution of real successes
  and failures to twin data [31, 32].
- *Success criterion (H3):* budget–performance curves (real data = capture minutes + real rollouts) fitted
  per method; guided allocation reaches the target SR τ with ≤ 0.7 of the uniform budget (upper 95% bound of
  the ratio < 1).

**Stage IV – cross-task and cross-simulator generalization (RQ4, H4; sem. 6–7).**
- *Manipulation zoo:* pick-and-place policies trained in twins of tabletop scenes in ManiSkill3 [9]; labels
  from SIMPLER [12] environments and their published paired sim/real evaluations (tier B).
- *Method:* the navigation-trained predictor is applied without retraining. *Comparators:* SRCC of a generic
  simulator [10] and a frozen learned world model used as a policy evaluator (in the style of [35]); world
  models are not trained.
- *Success criterion (H4):* Spearman ρ ≥ 0.5 on manipulation, and a higher rank correlation with real
  outcomes than both comparators (95% CI of each paired difference excludes 0).

**Tier C validation.** Two robot campaigns (sem. 5 and 7) check that tier-A conclusions carry over: 8 zoo
policies × 60 episodes (2 environments × 10 start–goal pairs × 3 trials), about 16 robot-hours per campaign
at ~2 min per episode. Tier C is reported as agreement and is never used to tune thresholds.

**Statistics and reproducibility.** Tests are one-sided (α = 0.05), bootstrapped over scenes and
Holm-corrected within each hypothesis, as in §7. The protocol is pre-registered in the project repository
before each stage, and changes are logged with reasons. Code, the paired-frame benchmark and the policy zoo
are released where the dataset licences permit.

<!--
Wave 9 (issue #23), 2026-09-26: rewritten for the pivot (research/pivot-decision.md, binding). Stages now
follow RQ1-RQ4: I paired-frame benchmark + probes/CKA (H1, P1), II policy zoo + metanetwork/GNN predictors +
conformal monitors (H2, P2), III budget allocation (H3, P3), IV manipulation + world-model comparator (H4, P3).
Wording and thresholds copied from content/07 (issue #22, worker T): zoo >= 200, >= 10 encoders, >= 4
capture budgets, 90% conformal level with >= 85% real coverage, 0.7 budget ratio, rho >= 0.6 / >= 0.5.
- Refs are §6 numbers (new list): [1] Habitat, [6] GaussGym, [9] ManiSkill3, [10] Kadian SRCC, [12] SIMPLER,
  [17] ScanNet++, [18] probes, [19] CKA, [20] DINOv2, [21] V-JEPA 2, [26] Navon, [27] Kofinas, [28] conformal,
  [29] FAIL-Detect, [30] SAFE, [31] TRAK, [32] CUPID, [33] PPI, [34] SureSim, [35] WorldEval.
- "The student's prior method": ACL 2025 SRW, doi:10.18653/v1/2025.acl-srw.61 (novelty-options.md §3;
  pre-PhD, background only, §12).
- Probe targets (depth, semantics, goal direction) and imitation of a privileged planner are our design
  choices (novelty-options.md §3 risks); CONFIRM supervisor.
- Robot time: 8 policies x 60 episodes x ~2 min = 960 min = 16 h (same total as the previous plan; the ~2 min
  per episode incl. reset is ASSUMED; CONFIRM after the first campaign). Fewer episodes per policy than the old
  non-inferiority test because tier C now only reports rank agreement.
- ScanNet++ licence terms for releasing derived reconstructions: UNVERIFIED (see §12 risk).
- SIMPLER checkpoints and the exact paired numbers must be re-read from the paper before Stage IV
  (novelty-options.md §3). ManiSkill assets are CC BY-NC 4.0 (fine for research).
- Removed from the old plan: twin-vs-generic non-inferiority test, domain-randomization baseline as a
  hypothesis, representation alignment objective, SimOpt-style correction (crowded or out of scope after the
  pivot); twin-vs-generic can still be reported as a sanity check.
-->

# RQ3 and RQ4 feasibility: selective real data to correct the twin and the model, and predicting transfer

Scope: can one PhD student in 2028, with academic GPUs (Department, WCSS, PLGrid) and at best borrowed robot time, answer RQ3 ("which real data, chosen under a limited budget, most efficiently correct both the simulation and the model?") and RQ4 ("do improvements generalize to unseen scenes and across navigation and manipulation, and do attribution and localization predict transfer better than simple predictors?"). Context: content/07-questions-hypotheses.md and content/09-methods.md (visible text). All arXiv IDs below were checked against the arXiv API on 27 Sep 2026; GitHub repos were checked through the GitHub API on the same day.

## 1. Can RQ3 be run without a robot? (proxy "reality" in navigation, new real data in manipulation, SIMPLER, public paired sim/real data)

### Takeaway
Navigation: yes, as a pool-based proxy. ScanNet++ provides independent iPhone and DSLR captures plus laser scans of the same scenes, and since October 2025 it has an official benchmark that trains on iPhone captures and tests against DSLR images. "Acquiring real data" then means choosing which held-out DSLR frames or poses to reveal. Honest closed-loop real evaluation is impossible in this setup: the gap is measured open-loop on real frames and closed-loop only in a reference simulation built from the laser scan.
Manipulation: without an arm, no new real data can be collected. RQ3 there reduces to selecting from logged real datasets and evaluating open-loop, through SIMPLER/PolaRiS-style real-to-sim proxies, or in sim-to-sim setups with hidden parameters. SIMPLER is an evaluation tool for existing policies on the Google Robot and WidowX setups. It is not a source of new real interaction.

### Cited Findings
- ScanNet++ has 1000+ indoor scenes with sub-millimetre laser scans, registered 33-MP DSLR images and iPhone RGB-D streams. "The coupled DSLR and iPhone captures enable benchmarking of novel view synthesis methods in high-quality and commodity settings." v2 (Dec 2024) has 1000+ scenes. On 13 Oct 2025 an "iPhone NVS Benchmark — train on commodity-level captures and test against high-quality DSLR images" was released. On 30 Apr 2025 undistorted DSLR images and a 3DGS example codebase were released. On 30 Oct 2025 360° RGB-D panoramas were released for 956 scenes. Access requires an application and Terms of Use — [ScanNet++ site](https://kaldir.vc.in.tum.de/scannetpp/)
- SIMPLER (arXiv:2405.05941) targets "evaluating real-world robot manipulation policies in simulation" on "common real robot setups" (Google Robot, WidowX+Bridge), using Visual Matching and Variant Aggregation. It reports MMRV/Pearson against paired real evaluations (e.g. MMRV 0.031 / r 0.976 on one task group, with other groups at r 0.855–0.969) over ~1500 evaluation episodes. System identification was done "on a small sample of trajectories from the real world dataset" — [arXiv:2405.05941](https://arxiv.org/abs/2405.05941); [SimplerEnv repo](https://github.com/simpler-env/SimplerEnv) (1.2k stars, last push Dec 2025; built on SAPIEN/ManiSkill2)
- The SimplerEnv repo "provides real and SIMPLER evaluation performance for all policies on all tasks". These are aggregate success rates per policy and task (RT-1, RT-1-X, Octo), usable as paired sim/real logs at the policy level — [SimplerEnv](https://github.com/simpler-env/SimplerEnv)
- A 2026 study of 3 simulators (VLA-Arena, SIMPLER, REALM) with 5 VLAs (π0, π0-FAST, π0.5, GR00T N1.6/N1.7) and 9 tasks ran a total of 11,800 simulated and 1,115 real rollouts. SIMPLER reached only Spearman ρ = 0.400 for policy ranking, versus REALM ρ = 0.700 / Pearson 0.785 / MMRV 0.030. Simulator fine-tuning raised ranking ρ from 0.700 to 0.875. Alignment was non-monotonic in data amount: 10 demos/task was best, 20 degraded — [arXiv:2606.10366](https://arxiv.org/abs/2606.10366). This contradicts the high SIMPLER correlations reported in its own paper for newer VLAs; release of the real logs was not confirmed.
- PolaRiS (arXiv:2512.16881) turns short video scans into 3DGS evaluation environments for DROID-style policies. It used 6 paired real/sim environments across two institutions with 20 real rollouts per policy. Average Pearson was r≈0.9 (worst environment 0.81) and r≈0.98 against RoboArena. Co-training used ~350 sim demos from 15 held-out environments ("less than 25 mins" of fine-tuning). An environment takes under 1 h including splat training, and runs on an RTX 4090. Code is MIT at [github.com/arhanjain/polaris](https://github.com/arhanjain/polaris) (235 stars, active Jul 2026) — [arXiv:2512.16881](https://arxiv.org/abs/2512.16881)
- ArmnetBench v0.1 (arXiv:2607.24481) releases 3,118 real episodes: 2,518 human-scored rollouts of 7 policies × 12 tasks plus 600 demonstrations, on low-cost SO-101 arms, in LeRobot v3.0 format. This is a public real rollout log with success/suboptimal/failure labels — [arXiv:2607.24481](https://arxiv.org/abs/2607.24481)
- X2Real (arXiv:2609.27449, 23 Sep 2026) calibrates Isaac Lab-Arena visuals and physics to real hardware and reports a 0.84 linear sim/real correlation. Release of its real logs was not checked — [arXiv:2609.27449](https://arxiv.org/abs/2609.27449)
- Real-to-sim evaluation also exists for deformables (3DGS + physics; "simulated rollouts correlate strongly with real-world execution") — [arXiv:2511.04665](https://arxiv.org/abs/2511.04665)

### Inferences
- Navigation protocol that is honest and runnable: twin = 3DGS from the iPhone stream. "Reality" = DSLR frames at known poses, which serve as the acquisition pool and the open-loop test set, plus a laser-scan-based reference simulation for closed-loop success. The selection rule decides which DSLR frames or poses to reveal under a budget of k images. The revealed images are used both to refine the 3DGS (twin correction) and to fine-tune or align the policy (model correction). Unlabelled images count toward the budget, as planned in §7. This is pool-based active acquisition. It is defensible as long as the paper says "proxy reality" and does not claim a robot sim-to-real result. It leaves out actuation, sensor noise and dynamics, as §9 already concedes.
- Manipulation protocol without an arm: the pool is frames or episodes from public real datasets (Bridge/DROID/Open-X, ArmnetBench). Twin correction comes from those frames, and model correction is fine-tuning on the selected frames or episodes. Evaluation can be (a) open-loop action error on held-out real episodes, (b) closed-loop in a SIMPLER/PolaRiS-style visually matched twin, with the caveat that the evaluator is then partly the thing being corrected (circularity risk), and (c) sim-to-sim, where a hidden-parameter simulator plays "reality". Only (c) gives true closed-loop control of acquisition, and it is not sim-to-real.
- SIMPLER is usable for evaluating existing policies and as the visual-matching recipe. It cannot answer "which new real data to collect". The 2026 correlation study (ρ=0.40 for SIMPLER on modern VLAs) means SIMPLER should not be the sole manipulation evaluator. PolaRiS (open code, r≈0.9) is a better base for DROID-embodiment tabletop twins.

### Gaps
- No public dataset was found that provides, for the same manipulation scenes, (i) a twin, (ii) a pool of acquirable real observations and (iii) closed-loop real outcomes for many policy variants. The same is true of navigation beyond Kadian et al.'s single lab space (see §4).
- Whether the per-episode real rollout videos behind SIMPLER, PolaRiS and 2606.10366 are downloadable was not verified. Only aggregate tables are confirmed for SIMPLER.

## 2. Correcting twins from real data: sys-ID, 3DGS refinement, joint twin+policy correction

### Takeaway
Every twin or joint-correction method found needs real closed-loop interaction on a robot. ASID, SimOpt, TwinRL, VLAW and RialTo all use real rollouts or real demos on the target robot. Code exists for ASID, TwinRL, PolaRiS and RialTo (repo tiny). Only the visual part of twin correction (3DGS refinement from new real views) is doable offline. That fits the navigation proxy, but it corrects appearance and geometry, not dynamics.

### Cited Findings
- SimOpt (arXiv:1810.05687) adapts the simulation parameter distribution "using a few real world roll-outs interleaved with policy training". It was shown on real swing-peg-in-hole and drawer opening, so it needs real policy rollouts — [arXiv:1810.05687](https://arxiv.org/abs/1810.05687)
- BayesSim (arXiv:1906.01728) gives a Bayesian posterior over simulator parameters from real observations, i.e. likelihood-free inference that needs real trajectories — [arXiv:1906.01728](https://arxiv.org/abs/1906.01728)
- ASID (arXiv:2404.12308) uses an initial simulator to design exploration policies that, "when deployed in the real world, collect high-quality data". It identifies articulation, mass and other physical parameters from "a small amount of real-world data" — [arXiv:2404.12308](https://arxiv.org/abs/2404.12308); code at [github.com/WEIRDLabUW/asid](https://github.com/WEIRDLabUW/asid) (40 stars, pushed Jan 2026). ASID is the closest prior art to "choose where to collect real data to correct the sim". Its criterion is Fisher-information-style exploration for physical parameters, not visual or representation disagreement.
- RialTo (arXiv:2403.03949) builds twins "on the fly from small amounts of real-world data" using a scanning interface, with "inverse distillation" of real demos into sim. It reports a >67% increase in robustness across 8 real tasks and needs real demos plus a real arm — [arXiv:2403.03949](https://arxiv.org/abs/2403.03949); repo [github.com/real-to-sim-to-real/RialTo](https://github.com/real-to-sim-to-real/RialTo) (2 stars, last push Jun 2024, maturity unclear)
- TwinRL (arXiv:2602.09023) reconstructs a twin from smartphone scans and runs parallel RL in the twin to fill the replay buffer. The twin "identifies failure-prone yet informative configurations, enabling targeted human-in-the-loop rollouts". It reports near-100% success on 4 tasks and >30% faster convergence with "only 20 minutes of on-robot interaction". Note that the twin is used to target real data (failure-driven selection) and is not itself corrected from real data — [arXiv:2602.09023](https://arxiv.org/abs/2602.09023); code MIT at [github.com/zhourui9813/TwinRL](https://github.com/zhourui9813/TwinRL) (Octo/SERL-based, pushed Jul 2026)
- VLAW (arXiv:2602.12063) iteratively uses real-world rollouts to improve an action-conditioned video world model, which then generates synthetic rollouts for the VLA. It reports +39.2% absolute success over the base policy and +11.6% from the generated rollouts, on a real robot — [arXiv:2602.12063](https://arxiv.org/abs/2602.12063). This is the closest joint "twin + policy from the same real data" precedent, but the twin is a learned video model, not a 3DGS + physics twin. Code availability was not verified.
- Real-is-Sim (arXiv:2504.03597) keeps an Embodied-Gaussians twin synchronised with the real robot at 60 Hz, so it needs the robot in the loop — [arXiv:2504.03597](https://arxiv.org/abs/2504.03597)
- 3DGS/NeRF uncertainty and active view selection exist offline. FisherRF (arXiv:2311.17874) selects views by expected information gain, and Bayes' Rays (arXiv:2309.03185) gives post-hoc spatial uncertainty for pretrained NeRFs — [arXiv:2311.17874](https://arxiv.org/abs/2311.17874); [arXiv:2309.03185](https://arxiv.org/abs/2309.03185)
- Navigation twins: EmbodiedSplat (arXiv:2509.17430) built 3DGS/mesh twins from iPhone captures (20–30 min capture, 1–2 h DN-Splatter training). Fine-tuning an HM3D-pretrained policy for 20M steps in the twin raised real success on a Hello Robot Stretch from 50% to 70% (HSSD: 10% → 40–50%). This was 1 real scene with 10 episodes. Policy pretraining used 16 A40s for 600M–1.2B steps. The public repo appears to hold only the project page — [arXiv:2509.17430](https://arxiv.org/html/2509.17430); [repo](https://github.com/gchhablani/embodied-splat)
- Other 3DGS real-to-sim navigation works: VR-Robo (legged, arXiv:2502.01536), Vid2Sim (urban, arXiv:2501.06693), ReaDy-Go (dynamic humans, arXiv:2602.11575) — [arXiv:2502.01536](https://arxiv.org/abs/2502.01536); [arXiv:2501.06693](https://arxiv.org/abs/2501.06693); [arXiv:2602.11575](https://arxiv.org/abs/2602.11575)

### Inferences
- The "correct both from the same data" hypothesis has close precedents (VLAW, RialTo, TwinRL, SimOpt), all with a real robot. The novelty left for the IPB is the selection criterion (twin-disagreement from reconstruction uncertainty, representation distance and action sensitivity) and the offline, budgeted, controlled comparison. Reviewers may object that without a robot the "twin correction" is only visual.
- Minimum viable RQ3 (navigation): per scene, budgets k ∈ {5, 10, 25, 50} DSLR frames. The arms are twin-only (3DGS refinement with the k frames), model-only (alignment or fine-tuning with the same k) and joint. Selection rules are random, failure-driven (TwinRL-style: poses where the policy fails in the twin), FisherRF/uncertainty-only, and the proposed composite. The outcome is gap reduction on held-out DSLR frames (open-loop) plus closed-loop success in the laser-scan reference sim. The data exist and the tooling exists (3DGS, Habitat, FisherRF-style uncertainty).
- Fallback for manipulation: sim-to-sim with hidden parameters (textures, lighting, camera pose, friction and mass in ManiSkill3). The "real" pool is observations from the hidden-parameter sim. This is fully controllable and supports ASID-style comparisons, but it only proves the mechanism, not sim-to-real.

### Gaps
- No offline (robot-free) joint twin+policy correction paper with a real-data budget ablation was found.
- VLAW code and RialTo code maturity were not verified.

## 3. Does selective acquisition beat random? Typical gains

### Takeaway
Gains from active selection over random under domain shift are usually a few percentage points, and they are fragile. Several reproducibility studies find little or no advantage over random under strong training (augmentation, SSL). Robotics-specific evidence is effort savings of ~20–25% (SureSim) and qualitative efficiency (ASID, TwinRL). RQ3 should expect small effects, which need many scenes and seeds to detect (see §4).

### Cited Findings
- CLUE (arXiv:2010.08666) argues that uncertainty-only or diversity-only AL is "less effective for Active DA". On DomainNet at a 2k-label budget, CLUE beats margin sampling by ~1.4 pts and coreset by ~3 pts when fine-tuning (~1.3/2.3 pts with MME). These are low single-digit gains — [arXiv:2010.08666](https://arxiv.org/abs/2010.08666) (figures via search summary of the paper; confirm in Table 1)
- AADA (arXiv:1904.07848) uses a domain discriminator for importance-weighted selection, i.e. uncertainty and diversity with respect to the labelled set — [arXiv:1904.07848](https://arxiv.org/abs/1904.07848)
- "Towards Robust and Reproducible Active Learning" (arXiv:2002.09564): under identical settings, AL methods "produce an inconsistent gain over random sampling", and "under strong regularization, AL methods show marginal or no advantage over the random sampling baseline" — [arXiv:2002.09564](https://arxiv.org/abs/2002.09564)
- "Parting with Illusions about Deep Active Learning" (arXiv:1912.05361): AL methods "improve by a large-margin when integrated with semi-supervised learning, but barely perform better than the random baseline" — [arXiv:1912.05361](https://arxiv.org/abs/1912.05361)
- SureSim (arXiv:2510.04354) frames combining a few paired real/sim evaluations with large simulation as prediction-powered inference. It "saves over 20–25% of hardware evaluation effort" for similar confidence bounds (diffusion policy and π0, physics-based sim) — [arXiv:2510.04354](https://arxiv.org/abs/2510.04354); code [github.com/abadithela/suresim](https://github.com/abadithela/suresim) (small repo, Feb 2026). SureSim is for evaluation (estimating real success), not for choosing training data.
- TwinRL's failure-driven targeting is the named baseline in §7 and has open code (see §2) — [arXiv:2602.09023](https://arxiv.org/abs/2602.09023)

### Inferences
- A realistic hope is that the composite twin-disagreement rule beats random by a few points of gap reduction at small budgets, with the advantage vanishing as the budget grows. The IPB should present "does not beat random" as a possible, publishable negative result and use an AL protocol that follows the reproducibility recommendations (same augmentations, several seeds, strong random baseline).
- The joint-correction hypothesis (twin + model better than either alone) is likely easier to show than the selection hypothesis, because it is a larger intervention.
- SureSim can be reused in RQ4, or for the optional robot validation, to get valid confidence intervals from a few real trials plus many sim trials.

### Gaps
- No study was found that measures active acquisition for 3DGS-twin correction and then measures the downstream policy gap. The effect size is unknown.

## 4. RQ4: predicting transfer from pre-measured shift properties; evidence and statistical power

### Takeaway
There is evidence that simple sim-vs-real predictivity can be measured (SRCC, MMRV, Pearson) and that factor-level difficulty orderings are consistent between sim and real (Xie et al.). No paper was found that predicts, per new scene or task, whether a specific improvement will transfer from pre-measured shift properties. This makes RQ4 novel but high-risk. Showing that attribution/localization predictors beat "raw gap" or "image discrepancy" predictors needs on the order of 70–150 held-out scene/task units for a paired correlation comparison. That is feasible in navigation (ScanNet++ has ~1000 scenes) but hard in manipulation.

### Cited Findings
- Kadian et al. (Sim2Real Predictivity, arXiv:1912.06321) introduced SRCC. They scanned one lab space and ran 9 models in sim and on a LoCoBot. SRCC for success was 0.18 with CVPR19 Habitat settings, and tuning simulation parameters raised it to 0.844. The low value came from agents exploiting collision "sliding" — [arXiv:1912.06321](https://arxiv.org/abs/1912.06321)
- Xie et al. (arXiv:2307.03659) decompose the imitation-learning generalization gap into factors of variation (lighting, camera placement, etc.) using a 19-task, 11-factor benchmark. The resulting "ordering of factors based on generalization difficulty ... is consistent across simulation and our real robot setup" — [arXiv:2307.03659](https://arxiv.org/abs/2307.03659)
- 2606.10366 finds the real-world perturbation hierarchy (behaviour > layout > vision/language) is preserved only by some simulators (REALM), not SIMPLER. So whether shift properties predict real outcomes depends on the simulator — [arXiv:2606.10366](https://arxiv.org/abs/2606.10366)
- EmbodiedSplat reports sim-vs-real correlation of 0.87–0.97 for its twins (1 real scene evaluated) — [arXiv:2509.17430](https://arxiv.org/html/2509.17430)
- A commercial guide claims CLIP-embedding sim/real distance < 0.20 corresponds to < 10% success drop and > 0.30 to > 25% drop. It cites no primary study and should NOT be used as evidence, only as a sign that "image-level discrepancy" is the folk predictor RQ4 must beat — [truelabel.ai guide](https://truelabel.ai/guides/how-to-evaluate-sim-to-real-transfer)
- Recent position/survey papers on the reality gap and benchmarking call for quantifying sim/real performance alignment but do not provide predictive models — [arXiv:2510.20808](https://arxiv.org/abs/2510.20808); [arXiv:2508.11117](https://arxiv.org/abs/2508.11117)

### Inferences (own power calculations, Fisher z, α=0.05 two-sided, power 0.8; Steiger-type test for dependent correlations)
- Detecting that a single predictor correlates with transfer: n≈13 units for r=0.7, ≈29 for r=0.5, ≈85 for r=0.3.
- Showing that predictor A beats predictor B (the actual RQ4 claim), with predictors inter-correlated at 0.5: n≈66 for r_A=0.6 vs r_B=0.3, ≈107 for 0.7 vs 0.5, and ≈135 for 0.6 vs 0.4. So ~70–150 held-out units (scene × method pairs) are needed. A unit is only informative if its transfer outcome is measured precisely: a success rate from 20 episodes has SE≈0.11, from 100 episodes ≈0.05. Noisy outcomes attenuate the correlations and raise n further.
- Navigation can provide this: ScanNet++ has ~1000 scenes. With cheap evaluation (pretrained policy, short fine-tunes, 50–100 episodes/scene in the reference sim), 100+ held-out scenes are achievable. Manipulation cannot, since there are a handful of SIMPLER/PolaRiS twins and scene counts in the tens at best. A cross-task claim (navigation ↔ manipulation) will rest on few manipulation units and should be framed as qualitative or exploratory.
- The fallback for RQ4 is to predict transfer across scenes within navigation (well powered), and across factors within manipulation using Xie-style controlled factors in a sim-to-sim setting, where many "scenes" can be generated.

### Gaps
- No study was found that predicts improvement transfer, rather than sim/real correlation, from representation-level shift measures.
- No published power analysis for sim-to-real predictivity studies was found. The numbers above are my own calculations.

## 5. Cost and time of minimal robot validation (TurtleBot 4 at PWr, lab arms)

### Takeaway
Minimal validation is cheap in hardware and costly in person-time. A TurtleBot 4 costs about USD 1.2–1.9k and an SO-101 arm pair about USD 220–275. Physical validation of one navigation scene takes about 1–2 weeks. A credible manipulation validation needs a stable arm and camera for weeks. Existence of a TurtleBot 4 at PWr and lab arm access was not verified.

### Cited Findings
- TurtleBot 4 Standard MSRP USD 1,850. The Lite launched at USD 1,195. Both have a Raspberry Pi 4, OAK-D camera, 2D LiDAR and ROS 2 — [Clearpath TurtleBot 4](https://clearpathrobotics.com/turtlebot-4/); [Hackster launch news](https://www.hackster.io/news/clearpath-robotics-launches-the-turtlebot-4-offering-an-affordable-autonomous-ros-2-robot-platform-6bc3d6a10cbd). A German reseller lists EUR 1,699 — [MYBOTSHOP](https://www.mybotshop.de/TurtleBot-4_1)
- SO-101 (Hugging Face/LeRobot) DIY from about USD 100–130. The dual-arm (leader+follower) motor kit costs USD 220 (Standard) or 240 (Pro), plus ~USD 35 for printed parts — [CNX Software](https://www.cnx-software.com/2025/05/02/so-arm101-open-source-dual-robotic-arm-kit-works-with-hugging-faces-lerobot/); [Seeed Studio](https://www.seeedstudio.com/SO-ARM101-Low-Cost-AI-Arm-Kit-p-6426.html). ArmnetBench shows SO-101 cells are usable for multi-policy real evaluation (2,518 rollouts) — [arXiv:2607.24481](https://arxiv.org/abs/2607.24481)
- Scale of real evaluation in comparable papers: EmbodiedSplat used 1 scene with 10 episodes; PolaRiS used 20 rollouts per policy per environment across 6 environments; Kadian et al. used 9 models in one lab space; TwinRL used 20 min on-robot RL per task — [arXiv:2509.17430](https://arxiv.org/html/2509.17430); [arXiv:2512.16881](https://arxiv.org/abs/2512.16881); [arXiv:1912.06321](https://arxiv.org/abs/1912.06321); [arXiv:2602.09023](https://arxiv.org/abs/2602.09023)
- Twin creation is fast: 5–10 min video plus under 1 h total for PolaRiS, and 20–30 min capture plus 1–2 h splat training for EmbodiedSplat — same sources

### Inferences
- A minimal credible navigation validation: 1–2 rooms at PWr, a 3DGS twin from a phone scan, and 3–5 policy variants (base / twin-corrected / model-corrected / joint) × 20–30 episodes each. That is about 300–600 real episodes. Each ImageNav/PointNav episode takes a few minutes including reset, so this is about 20–40 robot-hours, roughly 1–2 weeks, plus ~2–4 weeks of ROS 2 / camera-calibration integration. It is feasible with a borrowed TurtleBot 4. Note that its OAK-D camera differs from the iPhone/DSLR capture used for the twin, which introduces a sensor gap.
- Manipulation: buying an SO-101 (< USD 300) makes a small RQ3 real loop possible (select which real frames or demos to collect), but the policy class and embodiment differ from SIMPLER/DROID. This is a real option to raise with the supervisor, since it removes the "arm uncertain" risk at negligible cost. Setup, calibration and teleoperating demos take about 1–2 months of part-time work (estimate, not sourced).

### Gaps
- Availability of a TurtleBot 4 or lab arm at PWr, and the lab's booking rules, were not verifiable online.
- Per-episode timing for TurtleBot 4 visual navigation was not found in a primary source. The hours above are estimates.

## 6. What could make RQ3 or RQ4 unsolvable, and compute/time estimates

### Takeaway
Neither question is technically unsolvable in its proxy form. Both become unfalsifiable as sim-to-real claims if no real closed-loop data enter. The main risks are (1) the proxy "reality" being too close to the twin, so the selection signal is trivial, (2) effect sizes of selection over random too small to detect, (3) too few manipulation units for RQ4's cross-task claim, and (4) circular evaluation when the corrected twin also serves as the evaluator.

### Cited Findings
- AL advantages over random are often marginal or inconsistent — [arXiv:2002.09564](https://arxiv.org/abs/2002.09564); [arXiv:1912.05361](https://arxiv.org/abs/1912.05361)
- Simulator-based conclusions can reverse in reality (SRCC 0.18 before tuning; SIMPLER ρ=0.40 on modern VLAs) — [arXiv:1912.06321](https://arxiv.org/abs/1912.06321); [arXiv:2606.10366](https://arxiv.org/abs/2606.10366)
- Compute references: EmbodiedSplat policy pretraining took 16 A40s for 600M–1.2B steps, with fine-tuning of 20M steps per scene. 3DGS per scene takes about 1–2 h on one GPU. PolaRiS co-training takes under 25 min on an RTX 4090 — [arXiv:2509.17430](https://arxiv.org/html/2509.17430); [arXiv:2512.16881](https://arxiv.org/abs/2512.16881)

### Inferences (estimates, not sourced)
- Failure modes and mitigations:
  - (a) Lack of real closed-loop data: state explicitly that navigation results are "proxy-reality" (DSLR / laser-scan) and manipulation results are open-loop or real-to-sim or sim-to-sim. Keep the optional robot study as the only sim-to-real claim.
  - (b) iPhone vs DSLR gap is mostly photometric (exposure, resolution), so the selection learns camera differences: control with colour/exposure normalisation and report per-error-type results, which links back to RQ1.
  - (c) Circularity: never evaluate on a twin refined with the selected data. Use a separate reference (laser-scan sim, held-out DSLR frames, hidden-parameter sim).
  - (d) Small effects: pre-register budgets and seeds, and report effect sizes with CIs.
  - (e) RQ4 underpowered in manipulation: scope the cross-task claim as exploratory.
- Minimum viable versions:
  - RQ3 in navigation only, on ~30–50 ScanNet++ scenes × 4 budgets × 4 selection rules × 3 correction arms × 3 seeds. Using a pretrained policy (no pretraining from scratch) with short fine-tunes (~5–20M steps, or offline fine-tuning or feature alignment instead of RL) plus 3DGS refinement, this is on the order of 10³–10⁴ GPU-hours. That fits a PLGrid grant, while RL fine-tuning at EmbodiedSplat scale per condition would not.
  - RQ4: ≥100 held-out navigation scenes with cheap per-scene measurements, plus a sim-to-sim manipulation factor study.
- Fallbacks: if the joint correction does not beat single corrections, report which correction dominates and when, as a function of RQ1 attribution. If selection does not beat random, report the conditions (budget, error type) where it does. If the cross-task claim is impossible, restrict RQ4 to cross-scene prediction within each task.
- Rough time budget for a single student: RQ3 about 12–15 months (pipeline, selection rules, experiments, paper) and RQ4 about 8–10 months, reusing the RQ1/RQ2 pipelines. Both depend on the RQ1/RQ2 tooling being ready by 2028.

### Gaps
- No compute figures were found for 3DGS refinement with a handful of new views (incremental 3DGS), nor for Habitat evaluation throughput on 3DGS-rendered scenes. GPU-hour numbers above are order-of-magnitude estimates.
- The VLAW and RialTo GPU requirements were not checked.

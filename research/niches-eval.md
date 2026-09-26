# Nearby niches on the evaluation side (issue #20)

Compiled 2026-09-26 · owner: Wave8-R worker · extends [crowdedness.md](crowdedness.md) (#16),
[world-models.md](world-models.md) (#17), [novelty-options.md](novelty-options.md) (#18) and
[novelty-synthesis.md](novelty-synthesis.md). This file does not edit `content/`.

Scope: questions about **how we know a policy trained in a reconstruction twin will work on the real robot**
(forecasting, fidelity, failure, statistics, benchmark predictivity), excluding what the earlier reports
already settled: the H3 SRCC twin-vs-generic contrast (crowdedness §6), world models as policy evaluators
(world-models §1.3), transfer forecasting from policy internals (novelty-options option 1) and
task-conditioned twin fidelity (novelty-options option 2). Each niche below is chosen to sit *next to* those
lines rather than repeat them.

## TL;DR

| # | Niche (short) | S2 hits 2023 / 24 / 25 / 26* (narrow query) | Dist. (0 = same, 3 = far) | Fit (0–3) | No-robot feasibility (0–3) | ML-venue share† | Verdict |
|---|---|---|---|---|---|---|---|
| **N5** | **Failure monitors trained in the twin, transferred to real (hidden-state probes)** | 0 / 5 / 4 / 10 (failure detection × robot policy overall: 3 / 8 / 15 / 27) | 1 | **3** | 2 | 3 of 4 venue-classified 200-pt hits are ML (ICLR, CVPR, NeurIPS) | **Active** (failure detection in general); **open** for twin→real transfer of the monitor and for navigation |
| **N4** | **Reconstruction uncertainty → calibrated uncertainty of the twin's SR estimate** | 0 / 0 / 3 / 4 (radiance-field UQ overall: 5 / 7 / 11 / 11) | 1 | 2 | **3** | Radiance-field UQ: 6 ML vs 5 robotics among 200-pt hits | **Open** |
| **N1** | **Few real rollouts + many twin rollouts: prediction-powered / control-variate estimates of real SR** | 1 / 0 / 2 / 1 (PPI as a method: 4 / 14 / 33 / 59) | 1 | 2 | 2 | Robotics-side papers are RSS / arXiv; PPI methods are ML (15 of 15 venue-classified 200-pt hits) | **Emerging** (≥ 5 papers in Oct 2025 to Aug 2026, all manipulation, driving or legged robots; none for twins or navigation) |
| N9 | Offline/open-loop metrics and checkpoint selection vs. closed-loop real success | 2 / 4 / 2 / 5 (open- vs closed-loop, looser: 2 / 7 / 6 / 19) | 2 | 3 | 3 | Driving side: CVPR, NeurIPS; robot side: RSS, RA-L, IROS | **Active in driving, open in embodied navigation** |
| N6 | OOD / coverage detection relative to what the twin captured | 0 / 0 / 1 / 5 | 1 | 2 | 2 | n too small (0 of 4) | **Open** |
| N3 | Off-policy evaluation that uses the twin as the model (doubly robust with a twin) | 1 / 0 / 2 / 0 (OPE × robot overall: 2 / 1 / 3 / 1) | 1 | 2 | 2 | OPE methods: NeurIPS, ICLR, TMLR | **Open** (in robotics; OPE itself is a large ML field) |
| N8 | Benchmark predictivity: meta-analysis of whether simulator/benchmark rankings predict real rankings | 4 / 2 / 11 / 23 | 1 | 2 | 3 | 1 ML vs 6 robotics | **Active** (overlaps H3; see crowdedness §6) |
| N7 | Failure discovery (falsification) in neural-reconstruction twins, and whether found failures transfer | 0 / 1 / 2 / 1 (strict closed-loop query) | 2 | 1 | 3 | 2 of 2 venue-classified (ECCV, NeurIPS) | **Active in driving, open for indoor robot navigation** |
| N2 | Sequential / active allocation of real evaluation rollouts | 0 / 0 / 1 / 2 | 2 | 1 | 1 | 0 ML; RSS-dominated | **Emerging, owned by one author group** |

\* 2026 = 1 Jan to 26 Sep 2026. † ML-venue share = among Semantic Scholar bulk-search hits (2023–26) whose venue is
one of the 200-pt venues, the fraction at NeurIPS/ICML/ICLR/CVPR/ICCV/ECCV/AAAI/IJCAI vs.
RSS/CoRL/ICRA/IROS/RA-L. Most hits are arXiv-only, so n is small. Read it as a direction, not a number.

**Ranked shortlist** (details in §3):
1. **N5: twin-trained, hidden-state failure predictors that survive the sim-to-real shift.** This is the
   episode-level, online counterpart of novelty-options option 1 and uses the student's probing and
   forecasting background directly. Hidden-state probes plus conformal calibration are an ML-venue idiom
   (SAFECAST 2026, FIPER NeurIPS 2025). Nobody has asked whether a monitor *calibrated in a reconstruction
   twin* keeps its guarantee on real data.
2. **N4: propagate reconstruction uncertainty into the twin's performance estimate.** The fully no-robot
   option. Radiance-field UQ exists (Bayes' Rays CVPR 2024, FisherRF), and so does policy evaluation in
   twins, but no paper found links the two: "how much should I trust this twin's SR number, given which parts
   of the scene were poorly captured?"
3. **N1 with a twist: prediction-powered inference where the predictor is the twin (and the policy's
   representations).** This is the statistics layer that makes H3 a methods contribution. It is moving fast
   (SureSim, X4Val, PERRY, SCAPE, Betting), so it only works as a *twin-specific and navigation-specific*
   extension, published early.

Runner-up: N9 (open- vs closed-loop predictivity in embodied navigation twins) is the safest benchmark paper
if a quick first publication is needed.

## 1. Method and caveats

- **Semantic Scholar** Graph API `GET /graph/v1/paper/search/bulk?query=<Q>&year=<Y>&sort=citationCount:desc`,
  `total` field used as the count; `venue` of the returned hits (≤ 1000 per call) classified into ML /
  robotics / other. All run **2026-09-26** between 16:00 and 16:40 CEST. The bulk endpoint matches title +
  abstract and **stems terms**, so broad OR-groups inflate counts (N8r below is an example and is not used).
- **arXiv API** (`export.arxiv.org/api/query`, same query with `all:` fields and a `submittedDate` window
  per year): **not available in this session.** Every call from this host returned HTTP 429 from about
  16:05 to at least 16:38 CEST. Other workers on the same IP were querying arXiv at the same time.
  A backoff loop (exponential, 3.1 s floor, up to 12 retries per call) ran the whole session without
  getting a single 200. The exact arXiv query strings are in §4 so the counts can be re-run with
  `MODE=arxiv python3 q2.py`. **arXiv counts are therefore missing, not zero.**
- **OpenAlex** also returned 429 ("insufficient budget", as noted in crowdedness §1). It was not used.
- **Paper verification.** Every paper cited below was resolved by arXiv ID through Semantic Scholar
  `/paper/batch` (41 IDs, all found). About half were also resolved through the arXiv `id_list` API before
  the 429s started. Title, year, venue, DOI and first authors come from those records. Claims about what a
  paper does come from its abstract (S2 `abstract` field), unless stated otherwise. Affiliations are **not**
  given, because author blocks were not read in this session.
- **Scores.** *Distance* is 0 = the current IPB question and 3 = a different field. *Fit* is 0–3 against
  the student's strengths (representation learning, GNNs, probing hidden states, LLM forecasting, ML
  venues). *Feasibility* is 0–3 with no own robot and academic GPUs only (WCSS/PLGrid). 3 means public
  data or proxy reality (public scans rendered at two capture budgets, as in novelty-options §3) is
  enough; 1 means real rollouts are essential.
- **Verdict scale** (same as crowdedness §1). *Crowded*: ≥ 50 papers/yr or the exact claim already shown
  by ≥ 2 groups. *Active*: 10–50/yr with partial demonstrations. *Emerging*: < 10/yr but several direct
  hits in the last 12 months. *Open*: < 10/yr and no demonstration of the exact claim.

## 2. Niches

### N1. Few real + many twin rollouts: bias-corrected estimates of real success

1. **RQ.** Can a small number of paired real/twin rollouts correct the bias of large-scale twin evaluation,
   giving valid confidence intervals on real success rate with fewer real trials than real-only testing,
   for navigation policies trained in reconstruction twins?
2. **Counts (S2, 2026-09-26).** N1 narrow: 1 / 0 / 2 / 1 (2023 / 24 / 25 / 26). Context C1 (PPI as a
   method, any domain): 4 / 14 / 33 / 59. arXiv: unavailable (429), query in §4.
3. **Closest verified papers.**
   - *Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators* (SureSim; Badithela, Snyder, et
     al.), arXiv:2510.04354, 2025. Frames sim + real evaluation as **prediction-powered inference**: paired
     real/sim evaluations rectify simulation bias; non-asymptotic CIs. Manipulation.
   - *X4Val: Learning Neural Surrogates for Variance-Reduced Policy Evaluation* (Luo, Watson, et al.),
     arXiv:2606.05159, 2026. Variance-reduced real-world metric estimation from heterogeneous auxiliary
     data (simulation, historical logs, other platforms).
   - *PERRY: Policy Evaluation with Confidence Intervals using Auxiliary Data* (Mandyam, Meng, et al.),
     arXiv:2507.20068, TMLR 2025. Conformal CIs for OPE when the auxiliary data (e.g. generated by a
     generative model) may be biased.
   - Already in crowdedness §6, not repeated: SCAPE (arXiv:2608.19425) and *Betting for Sim-to-Real
     Performance Evaluation* (arXiv:2604.24018, RSS 2026). Method root: *Prediction-Powered Inference*
     (Angelopoulos et al.), arXiv:2301.09633, doi:10.1126/science.adi6000.
4. **Distance** 1: it is the statistical form of H3/RQ4.
5. **Fit** 2: statistics and ML, with room for a learned predictor (policy embeddings as the PPI model);
   not the core probing strength.
6. **Feasibility** 2: needs paired real/sim outcomes. Public paired sets (SIMPLER, arXiv:2405.05941, pairs
   sim with real manipulation evaluations) or proxy reality are enough for a methods paper. The navigation
   version needs a few real runs.
7. **ML-venue share.** The robotics instances are RSS or arXiv; the methodological parent (PPI) is ML
   (all 15 venue-classified 200-pt hits in C1 are ML venues).
8. **Verdict: emerging, moving fast.** Five directly relevant papers appeared in about 11 months (Oct 2025
   to Aug 2026). None uses a reconstruction twin or navigation, and none conditions the rectifier on
   policy representations.

### N2. Sequential and active allocation of real evaluation rollouts

1. **RQ.** Given a twin's prior over which policies or scenarios are uncertain, how should a fixed budget
   of real rollouts be allocated (which policy, which start state, when to stop) to rank policies with a
   guaranteed error rate?
2. **Counts.** S2: 0 / 0 / 1 / 2. arXiv: unavailable.
3. **Closest verified papers.**
   - *Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping*
     (Snyder, Hancock, Badithela, et al.), arXiv:2503.10966, RSS 2025.
   - *Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison* (Snyder,
     Badithela, et al.), arXiv:2603.13616, 2026 (S2 venue label "Robotics", unconfirmed). Safe
     anytime-valid inference beyond binary success.
   - *Active Real-World Factor-Based Evaluation for Generalist Robot Policies* (Liao, Cui, et al.),
     arXiv:2607.14439, 2026. Probabilistic surrogate over task factors; picks evaluation configurations
     by information gain.
   - Context: *Robot Learning as an Empirical Science: Best Practices for Policy Evaluation*
     (Kress-Gazit et al.), arXiv:2409.09491; AutoEval (Zhou et al.), arXiv:2503.24278.
4. **Distance** 2: about evaluation practice, not about twins.
5. **Fit** 1: sequential testing and experimental design; little use of representation learning.
6. **Feasibility** 1: the contribution only counts with real rollouts.
7. **ML-venue share.** 0 ML; RSS is the home venue.
8. **Verdict: emerging, and one author group (Snyder / Badithela) holds 3 of the 5 closest papers,
   including SureSim in N1.** Not recommended as a thesis line. Cite it as the testing protocol for the
   IPB's real runs.

### N3. Off-policy evaluation with the twin as the model

1. **RQ.** Can a reconstruction twin serve as the *model* in model-based or doubly-robust off-policy
   evaluation, so that a new navigation policy is scored from logged real trajectories of *other* policies
   plus twin rollouts, without deploying it?
2. **Counts.** S2 N3: 1 / 0 / 2 / 0. Context C3 (OPE × robot): 2 / 1 / 3 / 1. arXiv: unavailable.
3. **Closest verified papers.**
   - *Off-Policy Evaluation via Off-Policy Classification* (Irpan, Rao, et al.), arXiv:1906.01624,
     NeurIPS 2019. OPE for sim-to-real grasping; the old anchor of the line.
   - *STITCH-OPE: Trajectory Stitching with Guided Diffusion for Off-Policy Evaluation* (Goli, Gimelfarb,
     et al.), arXiv:2505.20781, NeurIPS 2025, doi:10.52202/085713-0242. A generative model as the OPE
     model.
   - *PERRY* (arXiv:2507.20068, see N1): CIs for OPE with possibly biased synthetic auxiliary data.
   - Context: *Benchmarks for Deep Off-Policy Evaluation* (Fu et al.), arXiv:2103.16596, ICLR 2021;
     *OPERA* (Nie, Chandak, et al.), arXiv:2405.17708, NeurIPS 2024.
4. **Distance** 1.
5. **Fit** 2: ML-venue methodology; the student's forecasting background helps.
6. **Feasibility** 2: logged real navigation data is public (e.g. the real-only navigation corpus in
   crowdedness §4), but evaluating the OPE estimate needs ground-truth real returns of the target policy.
   Proxy reality works for a first paper.
7. **ML-venue share.** High (NeurIPS, ICLR, TMLR); robotics venues rarely publish OPE.
8. **Verdict: open in robotics.** OPE itself is a large ML field. Risk: long-horizon visuomotor OPE is
   known to be hard (Fu et al. 2021), so a negative result is plausible.

### N4. Reconstruction uncertainty → uncertainty of the twin's performance estimate

1. **RQ.** Can per-region epistemic uncertainty of a NeRF/3DGS reconstruction be propagated into a
   calibrated interval on the success rate the twin predicts, so the twin says *when its own evaluation
   cannot be trusted* and which extra capture would tighten it most?
2. **Counts.** S2 N4: 0 / 0 / 3 / 4. Context C4 (radiance-field UQ, any use): 5 / 7 / 11 / 11. None of
   the N4 top hits is about evaluation intervals. They are uncertainty-aware *training* (Phys2Real) or
   unrelated. arXiv: unavailable.
3. **Closest verified papers.**
   - *Bayes' Rays: Uncertainty Quantification for Neural Radiance Fields* (Goli et al.), arXiv:2309.03185,
     CVPR 2024, doi:10.1109/CVPR52733.2024.01896.
   - *FisherRF: Active View Selection and Uncertainty Quantification for Radiance Fields using Fisher
     Information* (Jiang, Lei, Daniilidis), arXiv:2311.17874, 2023.
   - *Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real
     Manipulation* (Wang, Tian, et al.), arXiv:2510.11689, 2025. 3DGS geometry plus uncertainty over
     *physical* parameters, used for training, not evaluation.
4. **Distance** 1: it plugs into the twin pipeline and H3 directly, and gives a principled answer to "how
   many capture minutes are enough" (H4).
5. **Fit** 2: uncertainty and representation learning on 3D scenes. Could use GNNs over Gaussians or scene
   graphs, but that is optional.
6. **Feasibility 3.** Proxy reality: treat a dense public scan as "real" and twins from sub-sampled
   captures as the estimates. No robot needed for the first paper.
7. **ML-venue share.** Radiance-field UQ: 6 ML vs 5 robotics among 200-pt hits (CVPR is the main venue).
8. **Verdict: open.** The two ingredients exist separately; the link (reconstruction UQ → evaluation UQ
   → capture decision) was not found.

### N5. Failure monitors trained in the twin, transferred to real

1. **RQ.** Does a runtime failure predictor that probes a policy's hidden states, trained and conformally
   calibrated on twin rollouts (where failures are cheap), keep its detection rate and coverage guarantee
   on real deployment? Can its shift be predicted or corrected from a handful of real episodes?
2. **Counts.** S2 N5 (failure prediction × sim/twin × policy): 0 / 5 / 4 / 10. Context C5 (failure
   detection × robot policy, any source): 3 / 8 / 15 / 27. Novelty-options T10 (failure/OOD from
   representations): S2 0 / 0 / 0 / 2 / 8 (2019–22 / 23 / 24 / 25 / 26). arXiv: unavailable.
3. **Closest verified papers.**
   - *SAFECAST: Robust Failure Detection for VLA Policies with Contrast-Set Training and Calibration*
     (Rajaprakash, Prajapati, et al.), arXiv:2608.04246, 2026. **Hidden-state risk probes + functional
     conformal prediction**. Its stated weakness: reliability "depends on calibration data matching
     deployment conditions". Evaluated on real DROID and LIBERO sim.
   - *Failure Prediction at Runtime for Generative Robot Policies* (FIPER; Römer, Kobras, et al.),
     arXiv:2510.09459, NeurIPS 2025. OOD in the policy embedding space plus action-chunk entropy,
     conformally calibrated, no failure data.
   - *Failure Prediction from Limited Hardware Demonstrations* (Parashar, Garg, et al.), arXiv:2410.09249,
     2024. Failures found in a model/simulator, then corrected with a budget of N real demonstrations.
     Closest in *structure* (sim failures + few real), but state-based, not learned representations.
   - Context: Sentinel (Agia, Sinha, et al.), arXiv:2410.04640, CoRL 2024; FAIL-Detect (Xu et al.),
     arXiv:2503.08558, RSS 2025; RAPT (Munn, Tidd, et al.), arXiv:2602.01515, 2026, a monitor learned from
     large-scale *simulation* and deployed after sim-to-real (humanoid, proprioceptive).
4. **Distance** 1: the twin provides the failure data; H3's predictivity question moves from the policy
   level to the episode level.
5. **Fit 3.** This is probing hidden states to forecast an outcome, the same shape as the student's
   ACL 2025 SRW work. It also complements novelty-synthesis option 1 (policy-level transfer forecast) with
   an online, per-episode version.
6. **Feasibility** 2: a methods paper can use public real failure data (DROID-based, as SAFECAST does)
   and proxy reality for navigation. Real navigation failures are needed to claim the full result.
7. **ML-venue share.** 3 of 4 venue-classified 200-pt hits are ML (AHA at ICLR, Code-as-Monitor at CVPR,
   FIPER at NeurIPS vs. Sentinel at CoRL).
8. **Verdict: active** for failure detection in general (doubling per year). **Open** for the specific
   question of twin→real transfer of a *learned, representation-based* monitor and its calibration. RAPT
   does sim→real for proprioception; SAFECAST names the calibration-mismatch problem but addresses it with
   perturbations, not twins.

### N6. Out-of-distribution / coverage detection relative to the twin

1. **RQ.** Can a deployed policy detect, from its own features, that the current real observation lies
   outside what the reconstruction twin covered (uncaptured region, moved furniture, lighting change), and
   does this "twin-coverage" score predict failure better than generic OOD detectors?
2. **Counts.** S2: 0 / 0 / 1 / 5. arXiv: unavailable.
3. **Closest verified papers.**
   - *RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid
     Robots* (Munn, Tidd, et al.), arXiv:2602.01515, 2026. Self-supervised 50 Hz monitor learned from
     simulation; OOD after sim-to-real.
   - *FIPER* (arXiv:2510.09459, see N5): random-network-distillation OOD score in the policy embedding
     space.
   - *Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for
     Imitation Learning Policies* (FAIL-Detect; Xu et al.), arXiv:2503.08558, RSS 2025.
4. **Distance** 1.
5. **Fit** 2: representation-space density or OOD estimation.
6. **Feasibility** 2: proxy reality (edit the scan after capture) works. Real validation is desirable.
7. **ML-venue share.** n too small (0 of 4 hits at a 200-pt venue).
8. **Verdict: open, but close to N5.** Best treated as one ablation axis of N5 ("coverage" vs. "policy
   uncertainty" signals) rather than as a separate thesis line.

### N7. Failure discovery (falsification) in neural-reconstruction twins

1. **RQ.** Do failure scenarios found by adversarial search in a 3DGS/NeRF twin (object placement,
   lighting, inserted agents) reproduce on the real robot at a higher rate than those found in a generic
   simulator?
2. **Counts.** S2 N7 (broad): 2 / 9 / 27 / 36, **polluted** by non-robotics "digital twin" papers (supply
   chains, grids; see top hits) and not used. N7r (strict: neural rendering + adversarial/safety-critical +
   closed-loop): 0 / 1 / 2 / 1. arXiv: unavailable.
3. **Closest verified papers.**
   - *NeuroNCAP: Photorealistic Closed-loop Safety Testing for Autonomous Driving* (Ljungbergh et al.),
     arXiv:2404.07762, ECCV 2024.
   - *Generating Transferable Adversarial Simulation Scenarios for Self-Driving via Neural Rendering*
     (Abeysirigoonawardena, Xie, et al.), arXiv:2309.15770, CoRL 2023. Asks the transfer question for
     driving.
   - *RADIUM: Predicting and Repairing End-to-End Robot Failures Using Gradient-Accelerated Sampling*
     (Dawson, Parashar, et al.), arXiv:2404.03412, T-RO 2025, doi:10.1109/TRO.2025.3551198.
4. **Distance** 2: dominated by autonomous driving.
5. **Fit** 1: search and optimization, little representation learning.
6. **Feasibility** 3 for the search, but the transfer claim needs real runs.
7. **ML-venue share.** 2 of 2 venue-classified strict hits are ML (ECCV, NeurIPS). Driving publishes at
   vision venues.
8. **Verdict: active in driving, open for indoor robot navigation.** Weak fit; not recommended.

### N8. Benchmark predictivity (meta-evaluation)

1. **RQ.** Across published paired sim/real results, which properties of a simulator or benchmark (visual
   fidelity, physics, task distribution) predict whether its policy *rankings* hold in the real world?
2. **Counts.** S2 N8: 4 / 2 / 11 / 23. The refined N8r (20 / 29 / 84 / 134) is **inflated by S2 stemming**
   (its top hits are generic policy papers) and is not used. The SRCC-by-name counts in crowdedness §2
   (S1: OpenAlex 0 / 3 / 10 in 2024 / 25 / 26) are the better indicator. arXiv: unavailable.
3. **Closest verified papers** (new relative to crowdedness §6, which already lists SIMPLER, Kadian 2020 and
   the Tsinghua "practical recipe" arXiv:2606.10366):
   - *RobotArena ∞: Scalable Robot Benchmarking via Real-to-Sim Translation* (Jangir, Zhang, et al.),
     arXiv:2510.23571, 2025. Converts robot-dataset videos into simulated environments for VLA
     benchmarking with human feedback.
   - *Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation*
     (VISER; Zhu, Wang, et al.), arXiv:2605.06311, 2026. Isolates lighting and material as drivers of
     the sim-real evaluation gap.
   - *A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation* (Wang, Xu, et al.),
     arXiv:2606.10366, 2026.
4. **Distance** 1: this is H3 lifted to the benchmark level.
5. **Fit** 2: meta-analysis and regression over results. A representation-level fidelity predictor would
   connect it to novelty-options option 2.
6. **Feasibility 3**: uses published results only.
7. **ML-venue share.** 1 ML vs 6 robotics among 200-pt hits.
8. **Verdict: active** (2026 growth, mostly manipulation/VLA). A meta-analysis could be a workshop paper,
   not a thesis line.

### N9. Offline/open-loop metrics and checkpoint selection vs. closed-loop real success

1. **RQ.** For navigation policies trained in twins, which cheap signals (offline action error, validation
   loss, twin closed-loop SR, representation statistics) best select the checkpoint or policy that
   performs best in the real world? How badly do open-loop metrics mis-rank?
2. **Counts.** S2 N9 (model/checkpoint/policy selection × sim-to-real/IL): 2 / 4 / 2 / 5. N10 (open- vs
   closed-loop correlation, looser): 2 / 7 / 6 / 19. arXiv: unavailable.
3. **Closest verified papers.**
   - *Scalable Offline Metrics for Autonomous Driving* (Aich, Kulkarni, et al.), arXiv:2510.08571,
     IROS 2025, doi:10.1109/IROS60139.2025.11247722. Finds "an even worse correlation between offline and
     online settings than reported by prior studies".
   - *Post-Convergence Sim-to-Real Policy Transfer: A Principled Alternative to Cherry-Picking* (Khor, Weng,
     et al.), arXiv:2504.15414, 2025. Principled selection among converged checkpoints for real
     deployment (legged).
   - *Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion* (Wu, Guo, et
     al.), arXiv:2602.00678, 2026 (S2 venue label "Robotics", unconfirmed). "RoboGauge", a sim-to-sim assessment suite that
     quantifies sim-to-real transferability.
   - Context: driving already has the open-loop critique (*Is Ego Status All You Need for Open-Loop
     End-to-End Autonomous Driving?*, arXiv:2312.03031, CVPR 2024; NAVSIM, arXiv:2406.15349, NeurIPS 2024).
     Robot IL has the observation that validation loss selects checkpoints poorly (*What Matters in
     Learning from Offline Human Demonstrations for Robot Manipulation*, arXiv:2108.03298, CoRL 2021).
     Offline RL selection: Paine et al., arXiv:2007.09055.
4. **Distance** 2: model selection rather than twin quality. Note that "twin SR as a selector" is H3 again.
5. **Fit 3**: forecasting real outcomes from cheap signals, including hidden states.
6. **Feasibility 3**: logs plus twin closed loop. Proxy reality for the "real" ranking.
7. **ML-venue share.** Driving: CVPR, NeurIPS. Robot side: RSS, RA-L, IROS.
8. **Verdict: active in driving, open in embodied navigation.** It overlaps novelty-options option 1 (if
   the selector uses hidden states, it *is* option 1 applied to checkpoints).

## 3. Ranked shortlist and first-paper ideas

Ranking criterion: openness × fit × no-robot feasibility × ML-venue fit, with a penalty for lines one
group already holds (N2) or that repeat earlier options (N8, and N9's hidden-state variant).

### Rank 1: N5, twin-trained hidden-state failure monitors under sim-to-real shift

- **Why.** Highest fit (3). The mechanism (probes on hidden states + conformal calibration) is accepted at
  ML venues (FIPER at NeurIPS 2025; SAFECAST 2026). The open part is exactly what a twin enables: cheap,
  diverse failure data in the target scene, followed by a calibration shift from twin to real. It also
  gives the IPB a per-episode counterpart to the policy-level forecasting of novelty-synthesis item 1,
  with the same policy zoo.
- **First paper (NeurIPS 2027 / ICLR 2028).** *"Calibrated in the twin, deployed in the world: do
  hidden-state failure predictors transfer across the sim-to-real gap?"*
  (i) Train navigation and manipulation policies in 3DGS twins of public scenes. (ii) Collect twin
  failures at scale and train hidden-state probes (linear, MLP, GNN over layers as in the ACL 2025 SRW
  method). (iii) Test on real data: public real rollouts for manipulation (DROID-based, as in SAFECAST)
  and proxy reality for navigation. (iv) Measure the drop in coverage and AUROC, and propose a
  few-real-episode recalibration (weighted conformal) that restores the guarantee. Baselines: FIPER,
  SAFECAST, FAIL-Detect.
- **Risk.** Needs some real failure episodes for the full claim. Mitigation: manipulation first, because
  public real data exists there.

### Rank 2: N4, reconstruction uncertainty → evaluation uncertainty → capture decision

- **Why.** The only candidate with full no-robot feasibility (3) and no direct competitor found. It
  connects Stage I of the IPB (capture cost vs. fidelity) to H3 (predictivity) and H4 (budget) with one
  quantity: the variance of the twin's SR estimate caused by reconstruction uncertainty.
- **First paper (CVPR 2028, or NeurIPS 2027).** *"How much should you trust your digital twin? Propagating
  radiance-field uncertainty into policy evaluation."* Sample twin variants from Bayes' Rays / FisherRF-style
  posteriors, evaluate a fixed policy across the variants, and calibrate the resulting SR interval against
  proxy-real SR (dense scan) across capture budgets. Then use the interval to choose the next capture views
  (active capture for evaluation, not for PSNR).
- **Risk.** The uncertainty in rendered appearance may be a small part of the sim-real gap (the MIT
  co-training study in crowdedness §4 finds physics matters more than visuals for pushing). This is a
  finding worth reporting either way. Navigation is more vision-bound than pushing, so the effect should be
  larger there.

### Rank 3: N1, twin-specific prediction-powered evaluation with representation-conditioned rectifiers

- **Why.** It turns H3 from "report SRCC" into "certify real SR from few real runs", which reviewers
  value. The field is emerging fast (SureSim, X4Val, PERRY, SCAPE, Betting within about 11 months), so the
  contribution must be specific: (a) reconstruction twins and navigation; (b) the rectifier conditioned on
  policy representations or on N4's twin uncertainty, instead of on a scalar sim outcome.
- **First paper (AAAI 2028 or NeurIPS 2027).** *"Prediction-powered evaluation of embodied policies with
  reconstruction twins."* Compare PPI with scalar twin outcomes, PPI with representation features, and
  real-only estimation, on public paired sim/real data (SIMPLER pairs) plus proxy-real navigation.
  Report the number of real trials needed to reach a fixed CI width.
- **Risk.** Most exposed to scooping (the SureSim/STEP author group is active). Publish early, or fold it
  into the H3 paper as its statistics section.

**Runner-up.** N9 (open- vs closed-loop mis-ranking in embodied navigation twins) is the quickest safe
benchmark paper (feasibility 3, fit 3), if a first publication is needed before the thesis line settles.

## 4. Query strings (all run 2026-09-26)

Semantic Scholar: `GET https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=<S2 Q>&year=<Y>&fields=title,venue,year,externalIds,citationCount&sort=citationCount:desc`,
Y ∈ {2023, 2024, 2025, 2026}; count = `total`.
arXiv (not obtained, HTTP 429): `GET https://export.arxiv.org/api/query?search_query=(<arXiv Q>) AND submittedDate:[<Y>01010000 TO <Y>12312359]&max_results=0`,
count = `opensearch:totalResults`. The arXiv query is the S2 query with `all:` prefixes, `+` → `AND` and
`|` → `OR`. It is given in full only where it differs.

| Key | S2 query (verbatim) | S2 2023 / 24 / 25 / 26 |
|---|---|---|
| N1 | `("sim-to-real" \| sim2real \| simulation \| simulator) + ("prediction-powered" \| "control variate" \| "control variates" \| "variance reduction" \| "bias correction") + "policy evaluation" + (robot \| robotic \| "real-world")` | 1 / 0 / 2 / 1 |
| N2 | `("policy evaluation" \| "policy comparison" \| "evaluating policies" \| "policy ranking") + ("sequential testing" \| "active evaluation" \| "adaptive evaluation" \| "early stopping" \| "sample-efficient evaluation" \| "number of trials" \| "statistically rigorous") + (robot \| robotic)` | 0 / 0 / 1 / 2 |
| N3 | `"off-policy evaluation" + (simulator \| simulation \| "digital twin" \| "world model" \| "model-based") + (robot \| robotic \| navigation \| manipulation)` | 1 / 0 / 2 / 0 |
| N4 | `("gaussian splatting" \| NeRF \| "neural radiance field" \| "digital twin") + (uncertainty \| epistemic) + ("policy evaluation" \| "sim-to-real" \| "real-to-sim") + (robot \| policy)` | 0 / 0 / 3 / 4 |
| N5 | `("failure prediction" \| "failure detection" \| "runtime monitoring" \| "runtime monitor" \| "failure monitor") + ("sim-to-real" \| simulation \| simulator \| "digital twin") + (policy \| policies) + (robot \| robotic)` | 0 / 5 / 4 / 10 |
| N6 | `("out-of-distribution" \| OOD \| novelty \| "distribution shift") + (detection \| detect) + ("sim-to-real" \| "digital twin" \| "gaussian splatting" \| NeRF) + (policy \| navigation \| robot) + deployment` | 0 / 0 / 1 / 5 |
| N7 (broad, polluted, not used) | `("gaussian splatting" \| NeRF \| "neural radiance field" \| "neural rendering" \| "digital twin") + (falsification \| "adversarial scenario" \| "adversarial scenarios" \| "stress testing" \| "safety-critical scenario" \| "safety-critical scenarios" \| "failure discovery" \| "failure modes") + (policy \| driving \| robot \| navigation)` | 2 / 9 / 27 / 36 |
| N7r | `("gaussian splatting" \| NeRF \| "neural radiance field" \| "neural rendering" \| 3DGS) + (adversarial \| falsification \| "safety-critical" \| "stress test" \| "stress testing" \| "failure discovery") + (policy \| driving \| robot \| navigation) + ("closed-loop" \| "closed loop")` | 0 / 1 / 2 / 1 |
| N8 | `(benchmark \| benchmarks) + ("sim-to-real" \| "real-world performance" \| "real-world results") + ("rank correlation" \| predictivity \| "predictive of" \| "correlates with" \| "ranking consistency") + (robot \| embodied \| navigation \| manipulation \| driving)` | 4 / 2 / 11 / 23 |
| N8r (inflated by stemming, not used) | `(benchmark \| "simulation benchmark") + ("real-world" \| "real world") + ("rank correlation" \| "ranking consistency" \| predictivity \| "sim-to-real correlation" \| "sim-real correlation" \| "sim-and-real correlation") + (policy \| policies)` | 20 / 29 / 84 / 134 |
| N9 | `("model selection" \| "checkpoint selection" \| "policy selection" \| "hyperparameter selection") + ("sim-to-real" \| sim2real \| "offline reinforcement learning" \| "imitation learning") + (robot \| robotic \| "real-world")` | 2 / 4 / 2 / 5 |
| N10 | `("open-loop" \| "offline metrics" \| "offline evaluation" \| "validation loss") + ("closed-loop" \| "closed loop") + (correlation \| correlate \| correlates \| predictive) + (policy \| policies) + (robot \| driving \| navigation \| manipulation)` | 2 / 7 / 6 / 19 |
| C1 | `"prediction-powered inference"` (arXiv: `all:"prediction-powered"`) | 4 / 14 / 33 / 59 |
| C3 | `"off-policy evaluation" + (robot \| robotic \| robotics)` | 2 / 1 / 3 / 1 |
| C4 | `("gaussian splatting" \| NeRF \| "neural radiance field") + ("uncertainty quantification" \| "epistemic uncertainty")` | 5 / 7 / 11 / 11 |
| C5 | `("failure detection" \| "failure prediction" \| "runtime monitoring") + (robot \| robotic) + (policy \| policies)` | 3 / 8 / 15 / 27 |

Venue classification used for "ML-venue share". ML = venue string contains NeurIPS / Neural Information
Processing Systems / ICML / ICLR / CVPR / ICCV / ECCV / AAAI / IJCAI. Robotics = RSS / Robotics: Science
and Systems / CoRL / ICRA / IROS / RA-L. Raw per-niche venue tallies (ml, robotics, with-venue, all hits
returned): N1 0/0/4/4, N2 0/0/3/3, N3 1/0/3/3, N4 0/0/7/7, N5 3/1/18/19, N6 0/0/4/6, N7r 2/0/2/4,
N8 1/6/36/40, N9 0/2/13/13, N10 1/4/21/34, C1 15/0/80/110, C3 2/0/7/7, C4 6/5/34/34, C5 6/10/46/53.
(S2 labels preprints as "arXiv.org", which is counted as "other".)

## 5. Verified references (S2 `/paper/batch` by arXiv ID, 2026-09-26)

| arXiv | DOI (S2) | Venue (S2) | Title (short) |
|---|---|---|---|
| 2510.04354 | 10.48550/arXiv.2510.04354 | arXiv | SureSim: Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators |
| 2606.05159 | 10.48550/arXiv.2606.05159 | arXiv | X4Val: Neural Surrogates for Variance-Reduced Policy Evaluation |
| 2507.20068 | 10.48550/arXiv.2507.20068 | TMLR | PERRY: Policy Evaluation with CIs using Auxiliary Data |
| 2301.09633 | 10.1126/science.adi6000 | Science | Prediction-Powered Inference |
| 2608.19425 | – | arXiv | SCAPE |
| 2604.24018 | 10.48550/arXiv.2604.24018 | RSS 2026 (arXiv comment) | Betting for Sim-to-Real Performance Evaluation |
| 2503.10966 | 10.48550/arXiv.2503.10966 | RSS 2025 | Policy Comparison with Near-Optimal Stopping |
| 2603.13616 | 10.48550/arXiv.2603.13616 | "Robotics" (S2 label; unconfirmed) | Beyond Binary Success |
| 2607.14439 | 10.48550/arXiv.2607.14439 | arXiv | Active Real-World Factor-Based Evaluation |
| 2409.09491 | 10.48550/arXiv.2409.09491 | arXiv | Robot Learning as an Empirical Science |
| 2503.24278 | 10.48550/arXiv.2503.24278 | arXiv | AutoEval |
| 1906.01624 | – | NeurIPS 2019 | Off-Policy Evaluation via Off-Policy Classification |
| 2505.20781 | 10.52202/085713-0242 | NeurIPS 2025 | STITCH-OPE |
| 2103.16596 | – | ICLR 2021 | Benchmarks for Deep Off-Policy Evaluation |
| 2405.17708 | 10.48550/arXiv.2405.17708 | NeurIPS 2024 | OPERA |
| 2309.03185 | 10.1109/CVPR52733.2024.01896 | CVPR 2024 | Bayes' Rays |
| 2311.17874 | 10.48550/arXiv.2311.17874 | arXiv | FisherRF |
| 2510.11689 | 10.48550/arXiv.2510.11689 | arXiv | Phys2Real |
| 2608.04246 | – | arXiv | SAFECAST |
| 2510.09459 | 10.48550/arXiv.2510.09459 | NeurIPS 2025 | FIPER: Failure Prediction at Runtime for Generative Robot Policies |
| 2410.00371 | 10.48550/arXiv.2410.00371 | ICLR (S2) | AHA: VLM for Detecting and Reasoning Over Failures in Robotic Manipulation |
| 2412.04455 | 10.1109/CVPR52734.2025.00649 | CVPR 2025 | Code-as-Monitor: Constraint-aware Visual Programming for Robotic Failure Detection |
| 2410.09249 | 10.48550/arXiv.2410.09249 | arXiv | Failure Prediction from Limited Hardware Demonstrations |
| 2410.04640 | 10.48550/arXiv.2410.04640 | CoRL 2024 | Sentinel: Runtime Monitoring of Consistency and Progress |
| 2503.08558 | 10.48550/arXiv.2503.08558 | RSS 2025 | FAIL-Detect |
| 2602.01515 | – | arXiv | RAPT |
| 2404.07762 | 10.48550/arXiv.2404.07762 | ECCV 2024 | NeuroNCAP |
| 2309.15770 | 10.48550/arXiv.2309.15770 | CoRL 2023 | Transferable Adversarial Simulation Scenarios via Neural Rendering |
| 2404.03412 | 10.1109/TRO.2025.3551198 | T-RO | RADIUM |
| 2510.23571 | 10.48550/arXiv.2510.23571 | arXiv | RobotArena ∞ |
| 2605.06311 | 10.48550/arXiv.2605.06311 | arXiv | VISER: Toward Visually Realistic Simulation |
| 2606.10366 | 10.48550/arXiv.2606.10366 | arXiv | Practical Recipe for Sim-and-Real Correlation (VLA) |
| 2405.05941 | 10.48550/arXiv.2405.05941 | CoRL 2024 | SIMPLER |
| 2510.08571 | 10.1109/IROS60139.2025.11247722 | IROS 2025 | Scalable Offline Metrics for Autonomous Driving |
| 2504.15414 | 10.48550/arXiv.2504.15414 | arXiv | Post-Convergence Sim-to-Real Policy Transfer |
| 2602.00678 | 10.48550/arXiv.2602.00678 | "Robotics" (S2 label; unconfirmed) | RoboGauge / MoE sim-to-real predictability |
| 2312.03031 | 10.1109/CVPR52733.2024.01408 | CVPR 2024 | Is Ego Status All You Need for Open-Loop E2E Driving? |
| 2406.15349 | 10.48550/arXiv.2406.15349 | NeurIPS 2024 | NAVSIM |
| 2108.03298 | – | CoRL 2021 | What Matters in Learning from Offline Human Demonstrations |
| 2007.09055 | – | arXiv | Hyperparameter Selection for Offline RL |

Note: S2 gives 1912.06321 (Kadian et al., cited in crowdedness §6) the title of its v1, *"Are We Making
Real Progress in Simulated Environments? Measuring the Sim2Real Gap in Embodied Visual Navigation"*. The
arXiv API returns the later title *"Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World
Performance?"*. Both refer to the same record.

## 6. Open items

- arXiv per-year counts for N1–N9 (HTTP 429 all session). Re-run the §4 queries when the rate limit
  clears. Script: `q2.py` (worker scratchpad) with `MODE=arxiv`.
- Affiliations of the closest papers were not read (author blocks not fetched), so none are claimed.
- The "no competitor found" claims for N4 and for the twin→real part of N5 rest on S2 search only. Before
  committing, repeat the search on arXiv and Google Scholar with the first-paper titles above.

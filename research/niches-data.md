# Nearby niches on the data side: collection, curation, valuation, mixtures (issue #19)

Compiled 2026-09-26 · owner: Wave8-Q worker · extends [crowdedness.md](crowdedness.md),
[world-models.md](world-models.md), [novelty-options.md](novelty-options.md) and
[novelty-synthesis.md](novelty-synthesis.md). This file does not edit `content/`.

## TL;DR

| # | Niche (data side) | S2 hits 2023/24/25/26* | Dist. | Fit | No-robot | ML-venue share† | Verdict |
|---|---|---|---|---|---|---|---|
| **N3** | **Data attribution / valuation for robot policies** (tight query) | 0 / 0 / 2 / 4 | 1 | **3** | 3 | n/a (all preprints) | **Emerging**. Twin → real attribution: **open** |
| **N9** | **Representation-guided selection or weighting of sim/twin samples for sim-to-real** | 0 / 0 / 1 / 0 | 1 | **3** | 3 | 0 / 1 | **Open** |
| **N1** | **Task-aware (policy-driven) capture for twins: where and what to record** | 2 / 2 / 0 / 2 (broad active reconstruction: 11 / 17 / 33 / 35) | 1 | 2 | 2 | 25 % (broad: 14 %) | **Open** (task-aware); active reconstruction itself is **active** |
| N2 | Choosing which real rollouts or demos to collect (active data collection, sim/twin context) | 1 / 2 / 0 / 3 (no sim filter: 3 / 8 / 6 / 6) | 1 | 2 | 1 | 25–31 % | **Open** in the twin setting, **emerging** in general |
| N4 | Sim / real / twin data-mixture optimisation | 0 / 3 / 10 / 15 | 1 | 2 | 2 | 50 % (4/8) | **Active**. Also overlaps novelty-options option 3 |
| N7 | Data-collection cost models and budget allocation (capture vs. real vs. compute) | 2 / 5 / 15 / 16 (noisy) | 1 | 1 | 3 | 5 % | Counts look **active** but mostly off-topic hits. The exact question is **open** |
| N6 | Quality metrics for synthetic or generated demonstrations | 2 / 5 / 14 / 12 | 2 | 2 | 3 | 15 % | **Active** |
| N8 | Retrieval, curation and filtering of large robot datasets | 7 / 6 / 16 / 23 | 2 | 2 | 3 | 27 % | **Active**, dominated by Stanford, Berkeley and TRI |
| N5 | Dataset or behaviour distillation for embodied policies | 5 / 6 / 6 / 2 | 3 | 2 | 3 | 25 % | **Open but stagnant**. Far from twins |
| N10 | Which or how many scenes to digitise for navigation (scene-count and diversity scaling) | 0 / 1 / 2 / 3 | 1 | 1 | 1 | 67 % (2/3) | **Open**, but low ML novelty |

\* Semantic Scholar `/paper/search/bulk` `total`, 2026 through 26 Sep. The arXiv API returned HTTP 429 on all
requests today, so arXiv counts are replaced by the arXiv-indexed subset of the S2 hits (§2).
† Among S2 hits with a known venue, the share that is a 200-point ITiT venue (NeurIPS/ICML/ICLR/CVPR/ICCV/ECCV/
AAAI/IJCAI/RSS).
Scores: *Dist.* is the distance to the current IPB topic (0 = same, 3 = far). *Fit* is the fit to the student
(0–3: representation learning, GNNs, probing hidden states, LLMs). *No-robot* is feasibility without a robot
(0–3). All scores are judgements, not measurements.

**Top 3 (details in §4):**
1. **N3 × twins: attribute real-world transfer to twin training data.** Which reconstructed scenes, frames
   or trajectories make a twin-trained policy succeed or fail in the real scene? Robot-data attribution
   appeared in 2025 (CUPID, DataMIL) and has three follow-ups in 2026, all on *real* demonstration pools.
   None attributes across the sim→real boundary.
2. **N9: representation-guided twin-data weighting.** Weight or select twin samples by their distance to a
   small real set in a frozen policy or foundation-model feature space. S2 finds one paper in four years
   (MetaMVUC, RA-L 2025, grasping, active learning). This is the data-side twin of novelty-options option 2
   and can share its code.
3. **N1: policy-aware capture.** Choose the next views to record for a twin by the *policy's* uncertainty or
   its predicted transfer gap, not by reconstruction uncertainty. Active view selection for NeRF/3DGS is
   active (33–35 papers/yr, e.g. FisherRF, GenNBV). Only 0–2 papers per year connect it to policies or
   sim-to-real.

All three reuse the probing, representation and GNN skills. They need only a phone for capture plus a
public or proxy real set, and they fit the existing thesis ("allocate a limited real-data budget") without
competing on twin infrastructure.

## 1. Method and caveats

- **Date.** All queries ran on **2026-09-26**. 2026 counts are partial (through 26 Sep).
- **Semantic Scholar (primary).** `GET https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=<Q>&year=<Y>&fields=title,year,venue,externalIds,citationCount`.
  Boolean syntax: `+` = AND, `|` = OR, quotes = phrase. The count is the `total` field. Requests used
  exponential backoff (3·2^i s, up to 8 tries). S2 returned several 429s, but every query completed.
- **arXiv API (failed).** `GET http://export.arxiv.org/api/query?search_query=(<Q>) AND submittedDate:[Y01010000 TO Y12312359]&max_results=0`
  (read `opensearch:totalResults`). Every request returned **HTTP 429**, including the https endpoint, for
  about 40 minutes (≥ 18 back-off cycles; other workers share the IP). **No arXiv API counts were obtained.**
  As a proxy, §2 gives the number of S2 hits per year that carry an arXiv ID ("arXiv subset"). This is a
  lower bound on the arXiv count, not a replacement for it. The arXiv query strings are in §5 so they can be
  re-run.
- **OpenAlex** was not used because its daily budget was already exhausted in wave 7 (see crowdedness.md §1).
- **ML-venue share** comes from the S2 `venue` field over all hits for 2023–26. arXiv-only records are
  excluded from the denominator. Robotics venues (ICRA/IROS/RA-L/CoRL/T-RO) are counted separately in §2.
- **Paper verification.** Every paper cited here comes from an S2 record with the arXiv ID or DOI shown.
  Titles, years and venues are copied from those records, and citation counts are S2 values on 2026-09-26.
  Claims about content are limited to what the title and S2 record state. Abstracts were not re-read for
  this file unless noted.
- **Noise.** Two queries were broad enough to catch off-topic work, and tighter variants were run:
  - N3 (with "Shapley") matched Shapley-value explanations in medicine and energy (146 hits). **N3t** drops
    "Shapley" and requires an imitation or robot-policy term, and its hits are all on-topic.
  - N4 matched VLA "co-training" with vision-language data (RoboMamba, InternVLA-M1).
  - N7 matched "cost-aware" and "multi-fidelity" in unrelated control work.
  In these cases the verdict relies on the tight query and on reading the titles.
- **Verdict scale** (same as crowdedness.md): *crowded* ≥ 50/yr or the exact claim already shown by ≥ 2
  groups; *active* 10–50/yr; *emerging* < 10/yr but growing, with ≥ 2 groups on the exact idea in the last
  12 months; *open* < 10/yr and no demonstration of the exact claim.

## 2. Counts per niche (2026-09-26)

| Key | Niche | S2 2023 | S2 2024 | S2 2025 | S2 2026* | arXiv subset 23/24/25/26 | hits with venue | 200-pt ML | robotics venue |
|---|---|---|---|---|---|---|---|---|---|
| N1 | task-aware capture (NeRF/3DGS + active view + policy/sim2real) | 2 | 2 | 0 | 2 | 2/1/0/1 | 4 | 1 | 2 |
| N1b | active view selection / NBV for NeRF/3DGS (context) | 11 | 17 | 33 | 35 | 10/14/25/25 | 49 | 7 | 13 |
| N2 | active data collection × IL × sim/twin | 1 | 2 | 0 | 3 | 1/1/0/2 | 4 | 1 | 2 |
| N2b | active data collection × IL × robot (no sim filter) | 3 | 8 | 6 | 6 | 2/7/2/3 | 16 | 5 | 3 |
| N3 | data attribution/valuation × robot (noisy, incl. Shapley) | 9 | 27 | 54 | 56 | 2/4/7/7 | 131 | 3 | 4 |
| N3t | data attribution/valuation × robot policy (tight) | 0 | 0 | 2 | 4 | 0/0/2/4 | 0 | 0 | 0 |
| N4 | co-training / data mixture × sim/synthetic × real × robot policy | 0 | 3 | 10 | 15 | 0/2/9/14 | 8 | 4 | 4 |
| N5 | dataset / behaviour distillation × RL/IL/robot | 5 | 6 | 6 | 2 | 2/5/5/1 | 12 | 3 | 1 |
| N6 | data/demonstration quality × synthetic/generated × robot policy | 2 | 5 | 14 | 12 | 1/2/8/7 | 20 | 3 | 6 |
| N7 | collection cost / budget allocation / multi-fidelity × robot policy | 2 | 5 | 15 | 16 | 1/2/13/8 | 21 | 1 | 6 |
| N8 | data retrieval / selection / curation × robot IL | 7 | 6 | 16 | 23 | 4/5/14/20 | 22 | 6 | 7 |
| N9 | sim2real/twin × data selection / importance weighting | 0 | 0 | 1 | 0 | 0/0/0/0 | 1 | 0 | 1 |
| N10 | scene diversity / number of scenes × navigation policy | 0 | 1 | 2 | 3 | 0/1/1/3 | 3 | 2 | 1 |

\* through 2026-09-26.

**Reading.** Only N8 (curation and retrieval) and the context query N1b (active reconstruction) pass 20
papers/yr. Everything that crosses the *data* question with the *sim/twin → real* boundary (N1, N2, N3t
restricted to twins, N9, N10) stays at ≤ 4 papers/yr. As in wave 7, the gap sits where two active lines
meet, not inside either line.

## 3. Niche cards

Each card gives (1) the research question, (2) crowdedness, (3) the three closest verified papers,
(4)–(6) the scores, (7) the ML-venue share and (8) the verdict.

### N3. Data attribution and valuation across the twin→real boundary

1. **RQ.** Can we attribute a twin-trained policy's real-world success or failure to individual
   reconstructed scenes, frames or synthetic trajectories, and does pruning the negatively-attributed twin
   data improve real transfer at a fixed budget?
2. **Crowdedness.** Tight query N3t: 0 / 0 / 2 / 4. Four of the six hits appeared in the last 15 months
   (CUPID, DataMIL, then three influence-function follow-ups in 2026). Every one of them attributes over a
   pool of *real* (or single-domain) demonstrations. None was found that attributes sim/twin data to
   real-world outcomes.
3. **Closest papers.**
   - CUPID: Curating Data your Robot Loves with Influence Functions (2025), arXiv:2506.19121, 34 citations.
   - DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (2025), arXiv:2505.09603, 32
     citations.
   - Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning
     (2026), arXiv:2603.09056. Also: ATHENA, accelerated multi-task heterogeneous influence functions for
     robot data curation (2026), arXiv:2606.16208.
4. **Distance:** 1. It works on the same object (twin training data) and answers "which twin data are
   worth it".
5. **Fit:** 3. Influence estimation over representations and gradients is close to the student's probing
   and hidden-state forecasting work, and attribution at the level of scenes or frames can use a GNN over
   the scene graph.
6. **No-robot feasibility:** 3. Outcomes can be proxy-real: policies trained in a twin of scan A and
   evaluated in an independent real capture or public real benchmark, or on public paired sim/real
   evaluations. A real robot is optional.
7. **ML-venue share:** n/a, since all six tight hits are preprints in S2 today. The methods lineage
   (influence functions, datamodels) is an ICML/NeurIPS topic.
8. **Verdict: emerging** for robot data attribution in general, **open** for twin→real attribution.
   *Risk:* the CUPID/DataMIL groups could add a sim-data variant. The protection is the cross-domain framing
   plus the twin-specific units (scenes, capture segments).

### N9. Representation-guided selection or weighting of twin/sim samples

1. **RQ.** Does weighting or selecting twin-generated training samples by their distance to a small real
   set, in a frozen policy or foundation-model feature space, beat uniform twin training and standard domain
   adaptation at an equal real-data budget?
2. **Crowdedness.** N9: 0 / 0 / 1 / 0, and the arXiv subset is 0 / 0 / 0 / 0. The nearest large lines are
   domain adaptation (crowded, see crowdedness.md H2a) and sim+real co-training (N4, active). Neither
   selects or weights *individual twin samples* by representation distance.
3. **Closest papers.**
   - MetaMVUC: Active Learning for Sample-Efficient Sim-to-Real Domain Adaptation in Robotic Grasping (RA-L
     2025), doi:10.1109/LRA.2025.3544083. It is the only S2 hit.
   - Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training (NeurIPS 2025), arXiv:2509.18631.
   - Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation (2025),
     arXiv:2503.24361, 65 citations.
4. **Distance:** 1. It is a direct reframing of H2 ("alignment") from a feature-level loss to a
   *data-level* selection, which avoids the crowded part of H2.
5. **Fit:** 3. It needs representation distances (CKA, MMD, Fréchet), probing, and weighting learned by a
   small metanetwork.
6. **No-robot feasibility:** 3. It needs twin data plus a small real *observation* set (phone video),
   which needs no robot. The outcome needs proxy-real or public evaluations, as in N3.
7. **ML-venue share:** 0 of 1 (the only hit is RA-L).
8. **Verdict: open.** It shares measurement code with novelty-options option 2 (task-conditioned fidelity):
   option 2 scores a *twin*, and N9 scores its *samples*.

### N1. Policy-aware capture: where and what to record for a twin

1. **RQ.** Given a capture budget of *k* minutes, does choosing the next views or areas to record by the
   downstream policy's uncertainty (or its predicted transfer gap) give better real success per capture
   minute than reconstruction-driven next-best-view (Fisher information, mutual information)?
2. **Crowdedness.** The narrow query N1 gives 2 / 2 / 0 / 2. Active view selection and NBV for NeRF/3DGS
   (N1b) give 11 / 17 / 33 / 35, which is active and growing. The optimisation targets there are
   reconstruction quality or safe navigation, not what a *trained policy* needs.
3. **Closest papers.**
   - FisherRF: Active View Selection and Uncertainty Quantification for Radiance Fields using Fisher
     Information (2023), arXiv:2311.17874, 83 citations.
   - GenNBV: Generalizable Next-Best-View Policy for Active 3D Reconstruction (CVPR 2024),
     arXiv:2402.16174, doi:10.1109/CVPR52733.2024.01555.
   - Beyond Uncertainty: Risk-Aware Active View Acquisition for Safe Robot Navigation and 3D Scene
     Understanding (2024), arXiv:2403.11396.
4. **Distance:** 1. It is exactly the "capture minutes" axis of H4/RQ2, made active.
5. **Fit:** 2. The policy-uncertainty signal is a representation or probing problem, but the
   reconstruction side is 3D vision, the student's weakest area.
6. **No-robot feasibility:** 2. Capture needs only a phone. Simulated capture on public scans (for example
   ScanNet++ or ARKitScenes, see benchmarks.md) allows fully offline ablations. The real-transfer check is
   the part that needs a robot or a proxy.
7. **ML-venue share:** 25 % (1 of 4) for the narrow query, 14 % (7 of 49) for N1b. The CV venues
   (CVPR/ICCV/ECCV) are the natural home.
8. **Verdict: open** for policy-aware capture, **active** for active reconstruction in general.

### N2. Choosing which real rollouts or demonstrations to collect

1. **RQ.** With a twin in hand and a budget of *n* real rollouts, which states or tasks should be rolled out
   in the real world (for twin correction, co-training or evaluation) to maximise real SR per rollout?
2. **Crowdedness.** N2 (with a sim/twin filter) gives 1 / 2 / 0 / 3. N2b (without it) gives 3 / 8 / 6 / 6.
   The 2024–26 work is on compositional data collection and active multi-task fine-tuning, not on the twin
   setting.
3. **Closest papers.**
   - Efficient Data Collection for Robotic Manipulation via Compositional Generalization (RSS 2024),
     arXiv:2403.05110, 56 citations.
   - Active Fine-Tuning of Multi-Task Policies (ICML), arXiv:2410.05026.
   - Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection (2025),
     arXiv:2502.09829.
4. **Distance:** 1. It is the "real rollouts" axis of H4 and the correction step of H3.
5. **Fit:** 2. It is uncertainty and active learning, which is standard ML but not the student's core.
6. **No-robot feasibility:** 1. The object *is* real rollouts, so without a robot it is limited to
   simulated-real proxies, which reviewers discount.
7. **ML-venue share:** 25–31 % (ICML and RSS appear among the hits).
8. **Verdict: open** for twins, **emerging** in general. Strong on topic, weak on feasibility.

### N4. Sim / real / twin data-mixture optimisation

1. **RQ.** Can the optimal twin:real mixing ratio (and per-scene weights) be learned online, DoReMi-style,
   instead of grid-searched, and does it transfer across scenes and tasks?
2. **Crowdedness.** 0 / 3 / 10 / 15 (noisy; about 40 % of the top hits are VLA vision-language co-training).
   The robotics co-training recipe papers of 2025–26 already sweep mixing ratios.
3. **Closest papers.**
   - Sim-and-Real Co-Training (2025), arXiv:2503.24361.
   - Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024), arXiv:2408.14037, 63
     citations.
   - A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models (2026),
     arXiv:2602.01067.
4. **Distance:** 1. **Fit:** 2. **No-robot feasibility:** 2 (compute-heavy).
5. **ML-venue share:** 50 % (4 of 8, NeurIPS-heavy).
6. **Verdict: active.** It largely overlaps novelty-options option 3 (the exchange rate), so it is not a new
   niche. Keep it inside option 3 as the "allocation rule" step.

### N7. Data-collection cost models and budget allocation

1. **RQ.** Given explicit costs (capture minutes, operator hours for real rollouts, GPU hours for twin
   training), which allocation maximises real SR, and can a multi-fidelity model predict it from a few
   pilot points?
2. **Crowdedness.** 2 / 5 / 15 / 16, but most hits are off-topic ("cost-aware" control, tactile sim2real,
   digital-twin monitoring). The on-topic hits are a multi-fidelity BO with a digital twin (controller
   tuning, not policies) and active experiment selection for evaluation.
3. **Closest papers.**
   - Guided Multi-Fidelity Bayesian Optimization for Data-driven Controller Tuning with Digital Twin (RA-L
     2025), arXiv:2509.17952.
   - Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection (2025),
     arXiv:2502.09829.
   - Data Scaling Laws in Imitation Learning for Robotic Manipulation (ICLR 2025), arXiv:2410.18647, 210
     citations. This is the cost-free scaling baseline.
4. **Distance:** 1. **Fit:** 1 (operations research and BO flavour). **No-robot feasibility:** 3.
5. **ML-venue share:** 5 %.
6. **Verdict:** the exact question is **open**, but it is hard to sell as ML novelty at 200-point venues.
   It is best used as the *decision layer* on top of option 3 or N3, not as a paper on its own.

### N6. Quality metrics for synthetic or generated demonstrations

1. **RQ.** Can a data-level score computed without training (for example mutual information between
   states and actions, or representation coverage) predict how much a batch of twin-rendered or
   world-model-generated demonstrations will improve real SR?
2. **Crowdedness.** 2 / 5 / 14 / 12, active. Real-data quality scoring has several 2025 papers.
3. **Closest papers.**
   - Robot Data Curation with Mutual Information Estimators (2025), arXiv:2502.08623, 49 citations.
   - Data Quality in Imitation Learning (NeurIPS 2023), arXiv:2306.02437, 128 citations.
   - SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (2025),
     arXiv:2505.22626.
4. **Distance:** 2. **Fit:** 2. **No-robot feasibility:** 3.
5. **ML-venue share:** 15 %.
6. **Verdict: active.** Its twin-specific variant collapses into novelty-options option 2 (fidelity) plus
   N9.

### N8. Retrieval, curation and filtering of large robot datasets

1. **RQ.** Retrieve from large public robot datasets (OXE-scale) the sub-trajectories that best complement
   a twin for a target scene.
2. **Crowdedness.** 7 / 6 / 16 / 23, active, with strong groups and many citations.
3. **Closest papers.**
   - Behavior Retrieval: Few-Shot Imitation Learning by Querying Unlabeled Datasets (RSS 2023),
     arXiv:2304.08742.
   - FlowRetrieval: Flow-Guided Data Retrieval for Few-Shot Imitation Learning (CoRL 2024),
     arXiv:2408.16944.
   - Re-Mix (CoRL 2024), arXiv:2408.14037.
4. **Distance:** 2 (manipulation-centric, no twins). **Fit:** 2. **No-robot feasibility:** 3.
5. **ML-venue share:** 27 %.
6. **Verdict: active**, trending toward crowded, so avoid it as the main line.

### N5. Dataset and behaviour distillation for embodied policies

1. **RQ.** Can a twin's training data be distilled into a tiny synthetic set that trains a transferable
   navigation policy?
2. **Crowdedness.** 5 / 6 / 6 / 2, flat or declining.
3. **Closest papers.**
   - Behaviour Distillation (ICLR 2024), arXiv:2406.15042.
   - Offline Behavior Distillation (NeurIPS 2024), arXiv:2410.22728.
   - Dataset Distillation for Offline Reinforcement Learning (2024), arXiv:2407.20299.
4. **Distance:** 3 (low-dimensional control benchmarks; the link to real transfer is unclear). **Fit:** 2.
   **No-robot feasibility:** 3.
5. **ML-venue share:** 25 %.
6. **Verdict: open but stagnant.** The ML-venue lineage is good, but it is too far from the IPB object and
   the bilevel optimisation is expensive with pixels.

### N10. Which or how many scenes to digitise

1. **RQ.** For navigation, how does real SR scale with the number and diversity of digitised scenes versus
   capture depth per scene, and which scene should be captured next?
2. **Crowdedness.** 0 / 1 / 2 / 3. Scene-scale datasets exist, but no study of the capture allocation.
3. **Closest papers.**
   - InternScenes: A Large-scale Simulatable Indoor Scene Dataset with Realistic Layouts (NeurIPS 2025),
     arXiv:2509.10813.
   - Learning to Navigate Efficiently and Precisely in Real Environments (CVPR 2024), arXiv:2401.14349.
   - ImagiNav: Scalable Embodied Navigation via Generative Visual Prediction and Inverse Dynamics (2026),
     arXiv:2603.13833.
4. **Distance:** 1. **Fit:** 1 (an empirical study). **No-robot feasibility:** 1 (needs many real scenes
   and real tests).
5. **ML-venue share:** 67 % (2 of 3, small sample).
6. **Verdict: open**, but it is a measurement study with low ML novelty. It fits as an ablation axis
   inside H4, not as a line of its own.

## 4. Ranked shortlist and first-paper ideas

Ranking criterion: (openness × fit × no-robot feasibility), with distance ≤ 1 required.

| Rank | Niche | Why it ranks here | First paper (venue target) |
|---|---|---|---|
| **1** | **N3 × twins: twin→real data attribution** | The robot-attribution method appeared in 2025 and grows by about 3 papers/yr, but only over real demo pools. Cross-domain (twin→real) attribution is untouched. It fits the student's hidden-state and representation toolkit, needs no robot, and turns H4 from "how much" into "which" twin data | **"Which parts of a digital twin matter? Attributing real-world transfer to reconstructed training data."** Train a population of navigation policies on 3DGS twins of public scans (reusing the option-1 policy zoo). Attribute proxy-real or public paired real outcomes to scenes, capture segments and trajectories with datamodels or influence functions (CUPID/DataMIL as baselines). Show that pruning or recapturing negatively attributed segments raises proxy-real SR at a fixed budget. Target: NeurIPS 2027 or ICLR 2028 |
| **2** | **N9: representation-guided twin-data weighting** | 0–1 papers per year. It converts the crowded H2 (feature alignment) into an open data-level question. It shares code and metrics with option 2 (fidelity), so both papers come from one infrastructure | **"Real-anchored reweighting of twin data."** Compute per-sample distances (Fréchet, MMD, CKA; probe-based) between twin renders and about 5 min of real phone video in frozen DINOv2/policy feature space. Learn a weighting (a small metanetwork, optionally a GNN over the scene graph) that maximises proxy-real SR. Baselines: uniform, DA losses from arXiv:2509.18631, and co-training from arXiv:2503.24361. Target: ICLR 2028 or CVPR 2028 |
| **3** | **N1: policy-aware capture** | It makes the capture-minutes axis of H4 *active*, which changes H4 from an observational study into a method. Reconstruction-driven NBV is active (≈ 35/yr), but none of it optimises for a policy. It fits less well because of the 3D-vision side | **"Capture what the policy needs."** Given a partial 3DGS twin and a policy trained on it, pick the next capture views by policy uncertainty or the predicted transfer gap (from the option-1 forecaster) versus FisherRF/GenNBV. Measure policy SR per capture minute on simulated captures of public scans, with a small real phone-capture check. Target: CVPR 2028 or ECCV 2028 |

**Runners-up.** N2 (active real-rollout selection) is the strongest on topic but needs a robot; keep it as
future work or for the robot-access semester. N4 and N7 are best absorbed into option 3 as its allocation
rule. N5, N6 and N8 are either too far from the topic (N5) or too active (N6, N8).

**How these relate to wave 7.** N3 and N9 are *data-side counterparts* of options 1 and 2 in
novelty-options.md:

- Option 1 asks "does the *policy* reveal its transfer gap?" and N3 asks "which *data* caused it?".
- Option 2 scores the *twin*, and N9 scores and weights its *samples*.

A thesis could run option 1 and N3 on the same policy zoo, which gives two ML papers from one
infrastructure. That is a coordinator decision, not something this file decides.

## 5. Exact query strings (all run 2026-09-26)

S2 bulk: `query=<S2 Q>&year=<Y>` for Y ∈ {2023, 2024, 2025, 2026}.
arXiv API (all HTTP 429 today): `search_query=(<arXiv Q>) AND submittedDate:[<Y>01010000 TO <Y>12312359]&max_results=0`.

| Key | Semantic Scholar `<S2 Q>` | arXiv `<arXiv Q>` |
|---|---|---|
| N1 | `("gaussian splatting" \| NeRF \| "neural radiance field") + ("active view" \| "next-best-view" \| "view selection" \| "active reconstruction" \| "uncertainty-guided" \| "active capture") + (policy \| "sim-to-real" \| "real-to-sim")` | `(abs:"gaussian splatting" OR abs:NeRF OR abs:"neural radiance field") AND (abs:"active view" OR abs:"next-best-view" OR abs:"view selection" OR abs:"active reconstruction" OR abs:"uncertainty-guided" OR abs:"active capture") AND (abs:policy OR abs:"sim-to-real" OR abs:"real-to-sim")` |
| N1b | N1 without the last `+ (…)` group | N1 without the last `AND (…)` group |
| N2 | `("active learning" \| "active data collection" \| "adaptive data collection" \| "data collection strategy" \| "active fine-tuning") + ("imitation learning" \| "behavior cloning" \| demonstrations) + robot + ("sim-to-real" \| simulation \| "digital twin" \| "real-to-sim")` | same with `abs:` prefixes and AND/OR |
| N2b | `("active learning" \| "active data collection" \| "adaptive data collection" \| "data collection strategy" \| "active fine-tuning" \| "which demonstrations") + ("imitation learning" \| "behavior cloning" \| "robot learning") + robot` | same with `abs:` |
| N3 | `("data attribution" \| "influence function" \| "influence functions" \| "data valuation" \| datamodels \| Shapley) + (robot \| "imitation learning" \| "behavior cloning" \| embodied)` | same with `abs:` |
| N3t | `("data attribution" \| "influence function" \| "influence functions" \| "data valuation" \| datamodels) + ("imitation learning" \| "behavior cloning" \| "robot learning" \| "robot policy" \| "robot policies" \| visuomotor)` | same with `abs:` |
| N4 | `("co-training" \| "data mixture" \| "mixing ratio" \| "data mixing" \| "mixture weights" \| "domain weights") + (simulation \| simulated \| synthetic \| "digital twin") + real + robot + policy` | same with `abs:` |
| N5 | `("dataset distillation" \| "dataset condensation" \| "behavior distillation" \| "behaviour distillation") + ("reinforcement learning" \| "imitation learning" \| robot \| policy \| embodied)` | same with `abs:` |
| N6 | `("data quality" \| "dataset quality" \| "demonstration quality" \| "quality metric") + (synthetic \| generated \| simulation \| "world model") + robot + (policy \| "imitation learning")` | same with `abs:` |
| N7 | `("data collection cost" \| "cost of data collection" \| "collection cost" \| "cost-aware" \| "budget allocation" \| "multi-fidelity") + robot + (policy \| "sim-to-real" \| "digital twin")` | same with `abs:` |
| N8 | `("data retrieval" \| "data selection" \| "data curation" \| "data filtering" \| "retrieval-augmented" \| "behavior retrieval") + ("imitation learning" \| "robot learning" \| "behavior cloning" \| "robot policy" \| "robot policies")` | same with `abs:` |
| N9 | `("sim-to-real" \| sim2real \| "real-to-sim" \| "digital twin") + ("data selection" \| "sample selection" \| "importance weighting" \| "sample weighting" \| "data pruning") + (policy \| robot)` | same with `abs:` |
| N10 | `("scene diversity" \| "number of scenes" \| "environment diversity" \| "scene selection" \| "number of environments" \| "environment selection") + navigation + (policy \| "sim-to-real" \| embodied)` | same with `abs:` |

## 6. Limits and to-do

- **arXiv counts are missing** (HTTP 429 all session). Re-run the §5 arXiv strings once the throttle lifts
  and fill a second count column. The S2 arXiv subset is a lower bound.
- S2 venue metadata is sparse for 2025–26 preprints, so ML-venue shares rest on small denominators (n = 1–8
  for the open niches). Treat them as indicative only.
- The "closest paper" lists come from S2 bulk hits sorted by citations plus title reading. Abstracts were
  not re-read for this file, and a full-text check of CUPID and DataMIL (whether either includes sim data)
  is the first thing to do before committing to N3.
- Pre-2023 counts were not collected. The issue asked for 2023–2026 only.

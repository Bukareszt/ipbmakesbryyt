# Novelty options: less-crowded framings for an ML-first PhD on digital-twin policy learning

Issue #18 (Wave7-P) · compiled 2026-09-26 · owner: Wave7-P worker · **does not edit `content/`**

All counts below were taken on **2026-09-26** with the exact query strings given in §6. Two independent
sources were used for every count: the **arXiv API** (`all:` field = title, abstract, authors, comments) and
the **Semantic Scholar bulk search** (title + abstract, per-year totals). OpenAlex could not be used: its
free daily quota for this network was exhausted after the first probe (HTTP 429, resets at midnight UTC), so
the one OpenAlex number is marked as such. Counts are *indicators of crowdedness*, not systematic reviews;
the closest works were verified one by one on arXiv, Crossref, PMLR or the official project page (URL given).

---

## 0. TL;DR

**Is the current topic (content/02, 07: data-efficient policy learning in 3DGS digital twins, real2sim2real,
navigation + manipulation) too crowded?** Partly.

- The *systems* half ("build a 3DGS twin of a real scene, train a policy in it, deploy") is crowded and
  growing fast: the query for neural reconstruction × sim-to-real returns 78 arXiv papers, and Semantic
  Scholar counts 13 → 39 → 39 papers for 2024 → 2025 → 2026 (to date). Since the IPB draft was written,
  GaussGym (Oct 2025), PolaRiS (Dec 2025), a 3DGS soft-body policy-evaluation twin (Nov 2025), GaussTwin
  (ICRA 2026) and TwinRL (Feb 2026) have appeared, and the work is published mainly at robotics venues (arXiv
  self-reported acceptances 2024–26: 61 at CoRL/RSS/ICRA/IROS vs. 34 at NeurIPS/ICLR/ICML/CVPR/ICCV/ECCV for
  Gaussian splatting × robot/policy). A student with no robot competes there on the big labs' terms.
- The *question* half (how performance scales with the real-data budget) is still open (62 arXiv papers
  for sim-to-real × data budget; RialTo's 0–15-demo appendix remains the closest analysis), but it is an
  empirical result that any lab with more robots can reproduce at larger scale, so it is a fragile *thesis*.

**Recommendation.** Keep the object (policies learned in neural-reconstruction twins under a limited
real-data budget) but move the *thesis* to the representation level, where the student and K46 are strong
and the literature is nearly empty. Ranked options:

| Rank | Framing (one line) | Crowdedness (evidence in §3–§4) | Fits K46 / student | Needs own robot? | First paper |
|---|---|---|---|---|---|
| **1** | **Transfer forecasting from policy internals:** predict the twin-to-real transfer gap of a policy from its hidden states / weights, learned on a population (model zoo) of policies trained in twins | Near-empty: 4 arXiv hits for "internal representations predict the sim-to-real gap"; S2 by year 0/0/0/1/3 (2019–22/23/24/25/26). Weight-space learning itself is an active ML-venue topic (87 arXiv papers self-reporting NeurIPS/ICLR/ICML/CVPR acceptance 2024–26; ICLR 2025 and NeurIPS 2026 workshops) | Direct: the ACL 2025 SRW paper forecasts from LLM hidden states with a GNN over layers; K46 group lists "models in weight space" | No (proxy reality on public scans; public paired sim/real evaluations as labels) | NeurIPS 2027: a policy zoo + "sim-to-real forecasting" benchmark and metanetwork predictor |
| **2** | **Task-conditioned twin fidelity:** representation-level fidelity metrics of a reconstruction that predict downstream transfer better than PSNR/SSIM/LPIPS ("which fidelity matters") | Near-empty: PSNR/LPIPS × policy transfer = 2 arXiv hits; representation distances (Fréchet/MMD/CKA) × sim-to-real × robot = 1 arXiv hit. Closest concept (TR-FDF) appeared Aug 2026 in one domain (ultrasound) | Representation learning, probing; reuses Stage I fidelity–cost curves already in §9 | No | CVPR 2028 or NeurIPS 2027: "Beyond PSNR: what makes a twin good enough for policy learning" |
| **3** | **Exchange-rate scaling laws:** scaling laws in which the axis is *reconstruction budget* (capture minutes / views) vs. *real* experience, giving an exchange rate between reconstructed and real frames | Moderate: scaling laws × robotics 72 arXiv (Lin et al. ICLR 2025 is the anchor, 210 S2 citations), but sim/real mixture trade-off for policies = 7 arXiv; twins × scaling (S2) 1/2/3 in 2024/25/26 | Fits the current RQ2/H4 with a sharper claim; ML-venue friendly (scaling laws) | No (compute-heavy: WCSS/PLGrid) | NeurIPS 2027 or ICML 2028: exchange-rate law + budget allocation rule |
| 4 | **Probing world models trained in twins** (what a learned simulator encodes about the twin vs. reality) | Crowded upstream: world models × robot 1,086 arXiv; × 3DGS 91; probing world models 456; dominated by NVIDIA/Meta-scale work (Cosmos: 864 S2 citations in 2025) | Probing fits K46, but the object is owned by large labs | No | Only as an extension (P3/P4) |

**What changes in the IPB if option 1 (+2) is adopted:** the title and thesis in §2/§7 shift from "twin
policies are non-inferior to real-data policies at ≥ 10× budget" to "the twin-to-real transfer of a policy
can be predicted from its internal representations and from representation-level twin fidelity, without
real rollouts; this prediction is used to allocate a limited real-data budget". Stages I–II (pipeline,
budget curves) remain as the *data-generating* part; the population of policies they produce becomes the
dataset of the thesis. Manipulation stays the cross-task generalization test. Option 3 is the natural P1/P2
if the supervisor prefers minimal change.

---

## 1. Why the current framing is exposed

### 1.1 Growth and venue of the "3DGS twin → policy → real" line

| Query (short name; exact strings in §6) | arXiv total | Semantic Scholar by year 2019–22 / 23 / 24 / 25 / 26 |
|---|---|---|
| C1 neural reconstruction (3DGS/NeRF) × sim-to-real/real-to-sim | 78 | 3 / 2 / 13 / 39 / 39 |
| C3 "real-to-sim-to-real" | 89 | 11 / 6 / 14 / 40 / 41 |
| C4 Gaussian splatting × (navigation ∨ manipulation) × policy | 63 | 0 / 0 / 6 / 28 / 30 |
| C2 digital twin × (RL ∨ IL) × robot | 53 | 37 / 25 / 45 / 95 / 79 |
| C5 sim-to-real × navigation × policy | 152 | 44 / 21 / 19 / 62 / 82 |
| T5 simulation/world-model based policy evaluation predicting real performance | 38 | 2 / 0 / 4 / 10 / 25 |
| OpenAlex (single probe, full-text search) "gaussian splatting" "sim-to-real", 2023–26 | 444 works: 5 / 39 / 126 / 274 for 2023 / 24 / 25 / 26 | — |

Venue split from arXiv comment fields (self-reported acceptance, 2024–26 submissions; lower bound, §6 V):

| Topic | ML venues (NeurIPS, ICLR, ICML, CVPR, ICCV, ECCV) | Robotics venues (CoRL, RSS, ICRA, IROS) |
|---|---|---|
| sim-to-real (V1 / V1r) | 61 | 165 |
| Gaussian splatting × robot/policy/sim-to-real (V2 / V2r) | 34 | 61 |
| weight-space learning (V4) | 87 | n/a |
| world models × robot (V5) | 124 | n/a |
| predicting real-world/transfer performance of policies (V8) | 5 | n/a |

### 1.2 Closest works that appeared during 2025–26 (all verified on arXiv, date = first version)

| Work | What it already does | Overlap with content/07, 09 |
|---|---|---|
| GaussGym, Escontrela et al., 2025-10-17, arXiv:2510.15352 | 3DGS as drop-in renderer in IsaacGym, >100k steps/s, real-to-sim for locomotion/navigation from pixels | Stage I pipeline + Stage II training in twins |
| PolaRiS, Jain et al., 2025-12-18, arXiv:2512.16881 | scalable real-to-sim *evaluation* of generalist policies | Stage III predictivity (SRCC) |
| Real-to-Sim policy evaluation with 3DGS soft bodies, Zhang et al., 2025-11-06, arXiv:2511.04665 | twins from real videos for evaluating manipulation policies | Stage III / cross-task |
| SureSim, Badithela et al., 2025-10-05, arXiv:2510.04354 | prediction-powered inference combining many sim and few real trials | Stage III (few real rollouts) |
| GaussTwin, Cai et al., 2026-03-05, arXiv:2603.05108 (ICRA 2026 per arXiv comment) | real-time 3DGS twin with photometric *correction* loop | RQ4 correction of the twin |
| TwinRL, 2026-02-09, arXiv:2602.09023; D-REX, 2026-03-01, arXiv:2603.01151 | digital-twin RL for manipulation; differentiable real-to-sim-to-real | Stage IV manipulation |
| CASHER, Torne et al., 2024-12-02, arXiv:2412.01770 | crowdsourced 3D-reconstruction twins; performance scales super-linearly with human effort | RQ2 (budget vs. performance) |
| ReBot, Fang et al., 2025-03-15, arXiv:2503.14526 | real-to-sim-to-real video synthesis to scale VLA data | data-efficiency framing |
| Mechanistic analysis of sim-and-real co-training, Lei et al., 2026-04-15, arXiv:2604.13645 | identifies "structured representation alignment" as the primary effect of co-training | H2 representation alignment |
| GaussGym, EmbodiedSplat (ICCV 2025, arXiv:2509.17430), SplatSim (ICRA 2025), Vid2Sim (CVPR 2025) | already in §6 of the IPB | — |

Reading: the twin-building and twin-evaluation *infrastructure* is being commoditised by groups with robots
(Berkeley, Stanford, Georgia Tech, MIT, NVIDIA). A thesis whose contribution is "we built one and measured
how much real data it saves" will be compared against them at every review.

### 1.3 What is *not* crowded inside the same object

| Query | arXiv total | S2 by year 2019–22 / 23 / 24 / 25 / 26 | Note |
|---|---|---|---|
| C6 sim-to-real × real-data budget / data-efficient | 62 | 12 / 4 / 5 / 5 / 26 | the RQ2 question is still open |
| T6 representation alignment × sim-to-real × policy (current H2) | 7 | 0 / 0 / 1 / 3 / 7 | small but heating up (Lei et al. 2026) |
| T1 internal representations used to *predict* the sim-to-real gap | 4 | 0 / 0 / 0 / 1 / 3 | **option 1** |
| A6 predicting real-world performance without deployment | 13 | 2 / 0 / 1 / 6 / 5 | option 1 |
| T2 policy weights / model zoos × sim-to-real or robot policies (S2, tight) | (arXiv total inflated by "generalization", see §6) | 0 / 0 / 0 / 1 / 5 | option 1 |
| F5 PSNR/LPIPS/SSIM × sim-to-real or policy transfer | 2 | 0 / 0 / 0 / 2 / 6 | **option 2** |
| F3 Fréchet/MMD/CKA/feature distance × sim-to-real × robot | 1 | 0 / 0 / 0 / 1 / 0 | option 2 |
| F1 simulation fidelity / photorealism × sim-to-real × policy | 26 | 3 / 4 / 5 / 20 / 11 | option 2 |
| B3 real vs. synthetic data trade-off / mixing ratio × robot policy | 7 | 3 / 1 / 1 / 0 / 5 | **option 3** |
| B1 scaling laws × synthetic/simulated data × embodied | 32 | 9 / 3 / 6 / 11 / 16 | option 3 |
| T3 twins / real-to-sim × scaling laws × policy (S2, tight) | (inflated, §6) | 0 / 0 / 1 / 2 / 3 | option 3 |

---

## 2. Constraints taken from the repository

- ML-first PhD in ITiT at K46; supervisor's group: "Uczenie reprezentacji w grafach, grafy wiedzy i
  **modele w przestrzeni wag**" (representation learning on graphs, knowledge graphs and **weight-space
  models**), 7 people, keywords GNNs / graph representation learning. Source: https://ai.pwr.edu.pl/research-groups
  (read 2026-09-26). K46 has no robotics group (research/resources.md §1).
- Student's prior work: Piotrowski et al., *When Will the Tokens End? Graph-Based Forecasting for LLMs
  Output Length*, ACL 2025 SRW, pp. 843–848, doi:10.18653/v1/2025.acl-srw.61 (Crossref, 2026-09-26): a
  regressor and a **GNN over per-layer hidden states** forecasting a quantity from a model's internals.
  Option 1 below is the same methodological move applied to policies.
- Venues: only 200-point ITiT conferences (NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, AAAI, IJCAI, RSS);
  P1 = NeurIPS 2027 (~May 2027), research/venues-200.md.
- Compute: WCSS Lem (H100) and PLGrid (research/resources.md §2); no own robot; K29 Denali collaboration
  planned, not agreed.

---

## 3. Option 1 (rank 1): transfer forecasting from policy internals

**Thesis (1 sentence).** The twin-to-real transfer gap of an embodied policy trained in a
neural-reconstruction digital twin can be predicted, without real rollouts, from the policy's internal
representations and weights by a model learned on a population of such policies, and this prediction lets a
fixed real-data budget be spent where it closes the gap most.

**Why it is less crowded (evidence).**
- Tight query T1 (hidden states / internal representations / probing × sim-to-real gap × predict): 4 arXiv
  hits, none on the topic (a quadruped world model, person retrieval, swarm probing, ultrasound). Semantic
  Scholar: 0 / 0 / 0 / 1 / 3 for 2019–22 / 23 / 24 / 25 / 26.
- Existing "predict transfer" work uses *rollouts or dynamics*, not representations:
  - Kadian et al., *Sim2Real Predictivity* (SRCC), IEEE RA-L 2020, doi:10.1109/LRA.2020.3013848
    (Crossref) — needs paired real rollouts.
  - Zhang, Kaplan & Schuurmans, *Predicting Sim-to-Real Transfer with Probabilistic Dynamics Models*,
    arXiv:2009.12864 (2020) — transfer metric from a learned dynamics model on a fixed set of real
    trajectories; manipulation only; no representation analysis.
  - Lian & Ma, *A Transferability Metric Using Scene Similarity and Local Map Observation for DRL
    Navigation*, arXiv:2306.04910 (2023) — image template matching, not learned representations.
  - Badithela et al., *SureSim*, arXiv:2510.04354 (2025) — statistical combination of sim and real trials.
  - Wu et al., *Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion*
    ("RoboGauge"), arXiv:2602.00678, RSS 2026 per arXiv comment — an assessment suite for one locomotion
    policy family, proprioception only.
  - The 2025–26 "world model / twin as evaluator" line (SIMPLER, CoRL 2024, PMLR v270; WorldEval
    arXiv:2505.19017; PolaRiS arXiv:2512.16881; Gemini Robotics in Veo, arXiv:2512.10675) evaluates by
    *running* the policy in a proxy. Option 1 asks whether the answer is readable from the network itself.
- The neighbouring lines that *do* read policy internals do it for other targets: runtime failure detection
  (SAFE, arXiv:2506.09937, 84 S2 citations; *Failure Prediction at Runtime for Generative Robot Policies*,
  arXiv:2510.09459; T10: 17 arXiv, S2 0/0/0/2/8) and VLA interpretability (*Don't Blind Your VLA*,
  arXiv:2510.25616; SAEs in VLAs, arXiv:2603.19183; A4: 64 arXiv, S2 2/0/1/10/56). Offline transfer
  forecasting for a *population* of policies is not among them.
- Weight-space learning is an established ML-venue topic with no robotics/sim-to-real application yet:
  Schürholt et al., *Model Zoos*, NeurIPS 2022 (Crossref doi:10.52202/068431-2763); Navon et al., ICML 2023
  (arXiv:2301.12780); Zhou et al., *Neural Functional Transformers*, NeurIPS 2023 (Crossref
  doi:10.52202/075280-3387); Kofinas et al., *GNNs for Learning Equivariant Representations of Neural
  Networks*, ICLR 2024 (arXiv:2403.12143); Lim et al., *Graph Metanetworks*, arXiv:2312.04501. Workshops:
  ICLR 2025 *Weight Space Learning* (Singapore, 27 Apr 2025; https://weight-space-learning.github.io/) and
  its second edition, NeurIPS 2026 *Neural Network Artifacts as a New Data Modality* (Paris; submissions
  closed 6 Sep 2026; https://artifactsasdata.org). The ICLR workshop's stated topic "model analysis:
  inferring model properties such as test performance or generalization error from weights" is exactly
  the target here. Tight query T2 (weights / model zoo × sim-to-real / robot policy) on S2: 0 / 0 / 0 / 1 / 5;
  the one 2026 robotics hit, *Robotic Policy Adaptation via Weight-Space Meta-Learning* (arXiv:2606.07217),
  generates LoRA weights for task adaptation and does not predict transfer.

**Feasibility with academic compute and no own robot.**
- Data-generating part = the current Stages I–II: the Stage I pipeline turns public captures (ScanNet++,
  HM3D scenes; GaussGym or Habitat as the simulator) into twins at several capture budgets and fidelity
  levels; Stage II trains many small policies (RL and IL) in them. A *population* of a few hundred to a few
  thousand small policies is the natural by-product of the budget curves and fits WCSS/PLGrid budgets.
- Labels ("real" performance) come from the tier-A proxy reality already in §7 (the reference scan rendered
  in the simulator) and from public paired sim/real evaluations of released manipulation policies (SIMPLER,
  CoRL 2024, which reports paired sim-and-real evaluations of public policies; the exact checkpoints and
  numbers must be re-read from the paper). Real-robot validation (tier C, Denali) becomes a *small* label
  set for checking that proxy-real predictions carry over, not the main experiment.
- Predictor: linear probes and the student's layer-wise GNN over per-layer activations on a fixed probe set
  of observations (reconstructed frames vs. proxy-real frames), and metanetworks over weights (Kofinas
  2024 style). Baselines: SRCC from rollouts in the twin, image-fidelity metrics, dynamics-model metric
  (Zhang 2020), random.

**First paper for NeurIPS 2027 (P1).** *"Can we forecast sim-to-real transfer from a policy's hidden
states?"* — release a zoo of N navigation policies trained in 3DGS twins of ≥ 10 public scenes under varied
capture budgets and fidelity degradations, with paired twin and proxy-real success rates; show whether
probes/metanetworks predict the gap and rank policies better than SRCC-style rollout estimators at a
fraction of the cost; report negative results honestly (a "benchmark + study" paper is publishable either
way). Cross-task check on a small manipulation zoo (ManiSkill3 twins, SIMPLER proxy) is P3 material.

**Risks.**
- Predictors may learn trivial correlates (e.g. twin fidelity) rather than policy-specific transfer; needs
  ablations that hold fidelity fixed and vary the policy.
- Proxy reality (reference scan) is not reality; a small real-robot label set is still needed for the
  headline claim (mitigation: Denali tier C, ~16 robot-hours as already estimated in §9).
- Population size vs. compute: thousands of RL runs are expensive; mitigation: small policies, IL from
  privileged planners, shared encoders.
- Related-work speed: the failure-detection and VLA-interpretability lines could pivot to transfer
  prediction; mitigation: the *population/weight-space* angle and the twin data-generating process are the
  differentiators, and the zoo release creates a citable asset early.

---

## 4. Option 2 (rank 2): task-conditioned twin fidelity

**Thesis (1 sentence).** The usefulness of a reconstructed twin for policy learning is predicted not by
image-quality metrics but by representation-level, task-conditioned fidelity measures (distances between
encoder features of reconstructed and real observations along policy-relevant directions), which can be
computed before any policy is trained.

**Why it is less crowded (evidence).**
- F5 (PSNR/LPIPS/SSIM × sim-to-real or policy transfer): 2 arXiv hits, both unrelated (sonar, bridge
  imagery); S2 0 / 0 / 0 / 2 / 6. F3 (Fréchet/MMD/CKA/feature distance × sim-to-real × robot): 1 arXiv hit
  (Spot RL, arXiv:2504.17857, which uses Wasserstein/MMD to *tune simulator parameters*, not to predict
  transfer). F1 (fidelity/photorealism × sim-to-real × policy): 26 arXiv, mostly systems.
- Prior evidence that image fidelity is the wrong target: Truong et al., *Rethinking Sim2Real: Lower
  Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation*, CoRL 2022 (PMLR v205, verified on
  https://proceedings.mlr.press/v205/). No follow-up defines a fidelity metric that predicts transfer.
- Closest 2026 concept: Qian et al., *Task-Relevant Feature-Dynamics Fidelity Enables Zero-Shot Sim-to-Real
  Transfer for Robotic Ultrasound Scanning*, arXiv:2608.29516 (Aug 2026) — a task-relevant fidelity notion
  with a contraction analysis, in one domain. VISER (Zhu et al., arXiv:2605.06311, May 2026) isolates
  lighting/material effects on evaluation reliability. Yu et al. (arXiv:2606.15032, Jun 2026) argue for
  decision-centric evaluation of world models. The metric-learning question for *reconstructed twins* is
  open.

**Feasibility.** Fully public: build a fidelity ladder per scene by subsampling capture minutes/views,
removing textures, changing lighting (Stage I already logs PSNR/SSIM/LPIPS/Chamfer); train policies per rung
(Stage II); measure the transfer gap to proxy reality; fit which metric predicts it. Foundation encoders
(DINOv2-like) and the policy's own encoder give the representation spaces; the "policy-relevant direction"
is estimated with probes. No robot needed; a real-robot check is optional.

**First paper (NeurIPS 2027 alternative, or CVPR 2028 as P2).** *"Beyond PSNR: which fidelity matters for
policies learned in digital twins?"* — a controlled study over ≥ 10 scenes × k fidelity rungs × m policy
types, a proposed metric, and a "twin certification" rule (minimum capture for a target gap). It plugs into
§8 contribution 5 (pipeline with measured fidelity) and turns it from engineering into methodology.

**Risks.** Results may depend on the simulator and task; the effect size may be small for RGB-D policies
(depth dominates); mitigation: include RGB-only and depth-only policies and two simulators (Habitat,
GaussGym/Isaac).

---

## 5. Option 3 (rank 3): exchange-rate scaling laws for reconstructed vs. real data

**Thesis (1 sentence).** Deployed performance of policies trained on mixtures of reconstructed and real
experience follows a scaling law in two budgets, capture minutes (or views) and real minutes, whose fitted
exponents give an *exchange rate* between reconstructed and real data and an optimal allocation of a fixed
real-data budget.

**Why it is less crowded (evidence).** Scaling laws for robot learning exist but only on one axis: Lin et
al., *Data Scaling Laws in Imitation Learning for Robotic Manipulation*, ICLR 2025 oral (project page
https://data-scaling-laws.github.io/, arXiv:2410.18647; 210 S2 citations) scales *real* demonstrations;
Sartor & Thompson, *Neural Scaling Laws in Robotics*, arXiv:2405.14005 (meta-analysis); Ai et al.,
*Embodiment Scaling Laws*, CoRL 2025 (arXiv:2505.05753) scales embodiments; Zheng et al. (arXiv:2412.02689)
driving demos. Sim/real mixtures: Maddukuri et al., *Sim-and-Real Co-Training*, RSS 2025 (Crossref
doi:10.15607/rss.2025.xxi.109) and Wei et al., *Empirical Analysis of Sim-and-Real Cotraining*, IROS 2025
per arXiv comment (arXiv:2503.22634), both with hand-built simulators and fixed ratios; Fan et al., *Scaling
Laws of Synthetic Images*, CVPR 2024 (Crossref doi:10.1109/cvpr52733.2024.00705) for supervised vision.
CASHER (arXiv:2412.01770) reports super-linear scaling in *human effort* for reconstruction twins but no
law and no real-data axis. Counts: B3 (real vs. synthetic trade-off × robot policy) 7 arXiv, S2
3 / 1 / 1 / 0 / 5; T3 (twins × scaling laws × policy) S2 0 / 0 / 1 / 2 / 3.

**Feasibility.** This is the current RQ2/H4 with a sharper deliverable; all on tier A with WCSS/PLGrid. It
is compute-heavy (a grid over two budgets × seeds) but needs no robot.

**First paper.** NeurIPS 2027 or ICML 2028: the two-axis law on navigation (P1) with the allocation rule;
manipulation (P3) tests whether the exponents transfer across tasks.

**Risks.** The closest to what big labs can do faster with real robots (Tsinghua/Lin, NVIDIA, MIT co-training
groups); the *reconstruction-budget* axis is the defensible niche. Laws may be simulator-specific; report
on two simulators.

---

## 6. Queries and counts (all 2026-09-26)

arXiv API: `https://export.arxiv.org/api/query?search_query=<Q>` (`all:` field; totals from
`opensearch:totalResults`). Semantic Scholar: `graph/v1/paper/search/bulk?query=<Q>&year=<Y>` for
Y ∈ {2019-2022, 2023, 2024, 2025, 2026}; the S2 query is the arXiv query with `all:` removed, AND → `+`,
OR → `|`. Venue-fit queries (V) add `co:<venue>` (arXiv comment field) and
`submittedDate:[202401010000 TO 202612312359]`; they count self-reported acceptances and are lower bounds.
Raw JSON with top hits is in the worker's scratchpad (`out2.json`, `out3.json`, `out4.json`); the query
strings below are verbatim.

| Key | arXiv query | arXiv total | S2 2019–22 / 23 / 24 / 25 / 26 |
|---|---|---|---|
| C1 | `(all:"gaussian splatting" OR all:NeRF) AND (all:"sim-to-real" OR all:"real-to-sim" OR all:sim2real OR all:real2sim)` | 78 | 3 / 2 / 13 / 39 / 39 |
| C2 | `all:"digital twin" AND (all:"reinforcement learning" OR all:"imitation learning") AND all:robot` | 53 | 37 / 25 / 45 / 95 / 79 |
| C3 | `all:"real-to-sim-to-real" OR all:real2sim2real` | 89 | 11 / 6 / 14 / 40 / 41 |
| C4 | `all:"gaussian splatting" AND (all:navigation OR all:manipulation) AND all:policy` | 63 | 0 / 0 / 6 / 28 / 30 |
| C5 | `(all:"sim-to-real" OR all:sim2real) AND all:navigation AND all:policy` | 152 | 44 / 21 / 19 / 62 / 82 |
| C6 | `(all:"sim-to-real" OR all:sim2real) AND (all:"data-efficient" OR all:"data efficient" OR all:"data budget")` | 62 | 12 / 4 / 5 / 5 / 26 |
| A1 | `(all:"sim-to-real" OR all:sim2real) AND (all:predict OR all:predicting OR all:predictivity) AND (all:representation OR all:representations OR all:embeddings)` | 61 | 11 / 7 / 6 / 17 / 38 |
| A2 | `(all:"sim-to-real" OR all:sim2real) AND (all:predictivity OR all:"correlation coefficient")` | 350 | 62 / 29 / 43 / 96 / 171 |
| A3 | `(all:"transferability estimation" OR all:"transferability metric") AND (all:"reinforcement learning" OR all:policy OR all:robot)` | 7 | 10 / 3 / 3 / 1 / 2 |
| A3b | `all:"transferability estimation" OR all:"transferability metric"` (supervised-learning line, size reference) | 112 | 123 / 31 / 43 / 55 / 67 |
| A4 | `(all:probing OR all:"linear probe") AND (all:"robot policy" OR all:"visuomotor policy" OR all:"vision-language-action" OR all:"navigation policy")` | 64 | 2 / 0 / 1 / 10 / 56 |
| A5 | `(all:"weight space" OR all:"model zoo" OR all:"neural functionals") AND (all:"reinforcement learning" OR all:policy)` | 68 | 11 / 7 / 7 / 9 / 22 |
| A5b | `all:"weight space learning" OR all:"model zoos" OR all:"hyper-representations"` | 130 | 81 / 37 / 34 / 37 / 25 |
| A6 | `all:predicting AND all:"real-world performance" AND all:robot AND all:simulation` | 13 | 2 / 0 / 1 / 6 / 5 |
| B1 | `(all:"scaling law" OR all:"scaling laws") AND (all:"synthetic data" OR all:simulation OR all:"sim-to-real") AND (all:robot OR all:embodied OR all:policy)` | 32 | 9 / 3 / 6 / 11 / 16 |
| B2 | `(all:"scaling law" OR all:"scaling laws") AND (all:robot OR all:robotic OR all:"imitation learning" OR all:embodied)` | 72 | 45 / 8 / 20 / 38 / 31 |
| B3 | `(all:"synthetic data" OR all:"simulated data") AND all:"real data" AND (all:co-training OR all:mixing OR all:ratio) AND all:robot` | 7 | 3 / 1 / 1 / 0 / 5 |
| B3b | `(all:co-training OR all:cotraining) AND (all:simulation OR all:simulated) AND (all:robot OR all:policy)` | 158 | 54 / 25 / 30 / 78 / 120 |
| F1 | `(all:"simulation fidelity" OR all:photorealism OR all:"visual fidelity") AND (all:"sim-to-real" OR all:sim2real) AND (all:policy OR all:robot)` | 26 | 3 / 4 / 5 / 20 / 11 |
| F2 | `(all:"sim-to-real gap" OR all:"reality gap") AND (all:measuring OR all:quantifying OR all:metric)` | 131 | 39 / 17 / 16 / 54 / 90 |
| F3 | `(all:"sim-to-real" OR all:sim2real) AND (all:Frechet OR all:"maximum mean discrepancy" OR all:"feature distance") AND (all:robot OR all:policy)` | 1 | 0 / 0 / 0 / 1 / 0 |
| F4 | `all:"digital twin" AND all:fidelity AND (all:"reinforcement learning" OR all:policy) AND all:robot` | 19 | 0 / 3 / 6 / 17 / 21 |
| F5 | `(all:PSNR OR all:LPIPS) AND (all:"sim-to-real" OR all:sim2real)` | 2 | 0 / 0 / 0 / 2 / 6 |
| D1 | `(all:"world model" OR all:"world models") AND (all:"gaussian splatting" OR all:"digital twin" OR all:NeRF)` | 91 | 2 / 3 / 13 / 39 / 82 |
| D2 | `(all:"world model" OR all:"world models") AND (all:"sim-to-real" OR all:sim2real)` | 67 | 4 / 3 / 9 / 23 / 48 |
| D3 | `(all:"world model" OR all:"world models") AND (all:robot OR all:robotic OR all:embodied)` | 1,086 | 147 / 79 / 114 / 339 / 686 |
| D4 | `(all:"world model" OR all:"world models") AND (all:probing OR all:"linear probe" OR all:interpretability)` | 456 | 50 / 25 / 55 / 133 / 263 |
| D5 | `all:"scene graph" AND (all:"graph neural network" OR all:GNN) AND (all:"sim-to-real" OR all:navigation) AND all:policy` | 1 | 1 / 0 / 1 / 1 / 0 |
| D6 | `(all:"graph neural network" OR all:GNN) AND (all:"sim-to-real" OR all:sim2real)` | 21 | 8 / 3 / 5 / 8 / 11 |
| T1 | `(all:"sim-to-real gap" OR all:"reality gap" OR all:"sim-to-real transfer") AND (all:"hidden states" OR all:"internal representations" OR all:probing OR all:"linear probe" OR all:"representation similarity") AND (all:predict OR all:predicting OR all:predictor OR all:predictive)` | 4 | 0 / 0 / 0 / 1 / 3 |
| T2 | `(all:"weight space" OR all:"weight-space" OR all:"model zoo" OR all:"population of policies" OR all:"policy weights" OR all:metanetwork OR all:metanetworks) AND (all:"sim-to-real" OR all:sim2real OR all:"robot policy" OR all:"robot policies" OR all:generalization)` | 614 (inflated by `generalization`; not used) | S2 without `generalization`: 0 / 0 / 0 / 1 / 5 |
| T3 | `(all:"gaussian splatting" OR all:"real-to-sim" OR all:"digital twins" OR all:"digital twin") AND (all:"scaling law" OR all:"scaling laws" OR all:"scales with" OR all:"data scaling") AND (all:policy OR all:policies OR all:robot)` | 235 (inflated by non-robotics "digital twin"; not used) | S2 (`scaling law(s)`/`data scaling` only): 0 / 0 / 1 / 2 / 3 |
| T5 | `(all:"policy evaluation" OR all:"evaluating policies" OR all:"evaluate policies") AND (all:simulation OR all:simulator OR all:"world model") AND (all:"real-world" OR all:"real world") AND (all:robot OR all:manipulation OR all:navigation) AND (all:correlation OR all:predict OR all:predictive OR all:reliable)` | 38 | 2 / 0 / 4 / 10 / 25 |
| T6 | `(all:"representation alignment" OR all:"feature alignment" OR all:"aligning representations" OR all:"align representations") AND (all:"sim-to-real" OR all:sim2real) AND (all:policy OR all:policies OR all:robot OR all:navigation)` | 7 | 0 / 0 / 1 / 3 / 7 |
| T8 | `(all:"digital twin" OR all:reconstruction OR all:"gaussian splatting" OR all:simulator) AND (all:fidelity OR all:"rendering quality" OR all:realism) AND (all:"downstream" OR all:"task performance" OR all:"policy performance" OR all:"transfer performance") AND (all:predict OR all:predicts OR all:predictive OR all:correlate OR all:correlates)` | 186 (broad; top hits unrelated) | 6 / 1 / 6 / 12 / 28 |
| T9 | `(all:"gaussian splatting" OR all:"gaussian splats" OR all:"3DGS") AND (all:"world model" OR all:"world models" OR all:"learned simulator" OR all:"neural simulator") AND (all:robot OR all:policy OR all:manipulation OR all:navigation)` | 30 | 0 / 0 / 4 / 9 / 18 |
| T10 | `(all:"failure prediction" OR all:"failure detection" OR all:"out-of-distribution detection" OR all:"OOD detection") AND (all:"robot policy" OR all:"robot policies" OR all:"visuomotor" OR all:"vision-language-action" OR all:"imitation learning") AND (all:features OR all:representations OR all:embeddings OR all:"hidden states")` | 17 | 0 / 0 / 0 / 2 / 8 |

Venue-fit queries (arXiv only; `ML = (co:NeurIPS OR co:ICLR OR co:ICML OR co:CVPR OR co:ICCV OR co:ECCV)`,
`RO = (co:CoRL OR co:RSS OR co:ICRA OR co:IROS)`, `D = submittedDate:[202401010000 TO 202612312359]`):

| Key | Query | Total |
|---|---|---|
| V1 | `ML AND (all:"sim-to-real" OR all:sim2real) AND D` | 61 |
| V1r | `RO AND (all:"sim-to-real" OR all:sim2real) AND D` | 165 |
| V2 | `ML AND all:"gaussian splatting" AND (all:robot OR all:policy OR all:"sim-to-real") AND D` | 34 |
| V2r | `RO AND all:"gaussian splatting" AND (all:robot OR all:policy OR all:"sim-to-real") AND D` | 61 |
| V3 | `ML AND (all:"scaling law" OR all:"scaling laws") AND (all:robot OR all:embodied OR all:"synthetic data" OR all:"imitation learning") AND D` | 11 |
| V4 | `ML AND (all:"weight space" OR all:"model zoo" OR all:"model zoos" OR all:"neural functionals" OR all:metanetworks OR all:"weight-space") AND D` | 87 |
| V5 | `ML AND (all:"world model" OR all:"world models") AND (all:robot OR all:embodied OR all:policy) AND D` | 124 |
| V6 | `ML AND all:"digital twin" AND D` | 41 |
| V7 | `ML AND (all:probing OR all:"linear probe" OR all:interpretability OR all:"sparse autoencoders") AND (all:"vision-language-action" OR all:"robot policy" OR all:"robot policies" OR all:visuomotor) AND D` | 20 |
| V8 | `ML AND (all:"sim-to-real" OR all:sim2real OR all:"real-world performance") AND (all:predict OR all:predicting OR all:predictive OR all:predictivity) AND (all:robot OR all:policy) AND D` | 5 |

---

## 7. Verified references used above (2026-09-26)

Format: first author, title, venue (how verified), link. S2 = Semantic Scholar citation count on 2026-09-26
where retrieved (§8).

| Ref | Venue / verification | Link |
|---|---|---|
| Kadian et al., Sim2Real Predictivity | IEEE RA-L 2020 (Crossref) | https://doi.org/10.1109/LRA.2020.3013848 · https://arxiv.org/abs/1912.06321 |
| Truong et al., Rethinking Sim2Real | CoRL 2022, PMLR v205 (PMLR index) | https://arxiv.org/abs/2207.10821 · https://proceedings.mlr.press/v205/ |
| Li et al., SIMPLER | CoRL 2024, PMLR v270 (PMLR index) | https://arxiv.org/abs/2405.05941 · https://proceedings.mlr.press/v270/ |
| Zhang, Kaplan, Schuurmans, Predicting Sim-to-Real Transfer with Probabilistic Dynamics Models | arXiv 2020 | https://arxiv.org/abs/2009.12864 |
| Lian & Ma, Transferability Metric Using Scene Similarity | arXiv 2023 | https://arxiv.org/abs/2306.04910 |
| Badithela et al., SureSim (Reliable and Scalable Robot Policy Evaluation with Imperfect Simulators) | arXiv Oct 2025 | https://arxiv.org/abs/2510.04354 |
| Wu et al., Toward Reliable Sim-to-Real Predictability (RoboGauge) | RSS 2026 (arXiv comment) | https://arxiv.org/abs/2602.00678 |
| Li et al., WorldEval | arXiv May 2025 | https://arxiv.org/abs/2505.19017 |
| Jain et al., PolaRiS | arXiv Dec 2025 | https://arxiv.org/abs/2512.16881 |
| Gemini Robotics Team, Evaluating Gemini Robotics Policies in a Veo World Simulator | arXiv Dec 2025 | https://arxiv.org/abs/2512.10675 |
| Zhang et al., Real-to-Sim Robot Policy Evaluation with 3DGS Soft-Body Interactions | arXiv Nov 2025 | https://arxiv.org/abs/2511.04665 |
| Tseng et al., Scalable Policy Evaluation with Video World Models | arXiv Nov 2025 | https://arxiv.org/abs/2511.11520 |
| Escontrela et al., GaussGym | arXiv Oct 2025 | https://arxiv.org/abs/2510.15352 |
| Cai et al., GaussTwin | ICRA 2026 (arXiv comment) | https://arxiv.org/abs/2603.05108 |
| TwinRL | arXiv Feb 2026 | https://arxiv.org/abs/2602.09023 |
| D-REX | arXiv Mar 2026 | https://arxiv.org/abs/2603.01151 |
| Torne et al., CASHER (Robot Learning with Super-Linear Scaling) | arXiv Dec 2024 | https://arxiv.org/abs/2412.01770 |
| Fang et al., ReBot | arXiv Mar 2025 | https://arxiv.org/abs/2503.14526 |
| Lei et al., Mechanistic Analysis of Sim-and-Real Co-Training | arXiv Apr 2026 | https://arxiv.org/abs/2604.13645 |
| Gu et al., SAFE: Multitask Failure Detection for VLA Models | arXiv Jun 2025 | https://arxiv.org/abs/2506.09937 |
| Failure Prediction at Runtime for Generative Robot Policies | arXiv Oct 2025 | https://arxiv.org/abs/2510.09459 |
| Kachaev et al., Don't Blind Your VLA | arXiv Oct 2025 | https://arxiv.org/abs/2510.25616 |
| Swann et al., SAEs Reveal Interpretable Features in VLA Models | arXiv Mar 2026 | https://arxiv.org/abs/2603.19183 |
| Grant et al., Not All Features Are Created Equal (VLA mechanistic study) | ICLR 2026 workshop (arXiv comment) | https://arxiv.org/abs/2603.19233 |
| Bianchi et al., Robotic Policy Adaptation via Weight-Space Meta-Learning | arXiv Jun 2026 | https://arxiv.org/abs/2606.07217 |
| Schürholt et al., Model Zoos | NeurIPS 2022 (Crossref) | https://doi.org/10.52202/068431-2763 · https://arxiv.org/abs/2209.14764 |
| Schürholt et al., Hyper-Representations as Generative Models | NeurIPS 2022 (arXiv comment) | https://arxiv.org/abs/2209.14733 |
| Navon et al., Equivariant Architectures for Learning in Deep Weight Spaces | ICML 2023 (arXiv comment) | https://arxiv.org/abs/2301.12780 |
| Zhou et al., Neural Functional Transformers | NeurIPS 2023 (Crossref) | https://doi.org/10.52202/075280-3387 · https://arxiv.org/abs/2305.13546 |
| Kofinas et al., GNNs for Learning Equivariant Representations of Neural Networks | ICLR 2024 (arXiv comment) | https://arxiv.org/abs/2403.12143 |
| Lim et al., Graph Metanetworks | arXiv Dec 2023 | https://arxiv.org/abs/2312.04501 |
| Falk et al., Impact of Model Zoo Size and Composition on Weight Space Learning | ICLR 2025 WSL workshop (arXiv comment) | https://arxiv.org/abs/2504.10141 |
| ICLR 2025 Workshop on Weight Space Learning | official page | https://weight-space-learning.github.io/ |
| NeurIPS 2026 Workshop: Neural Network Artifacts as a New Data Modality | official page (Paris; deadline 6 Sep 2026) | https://artifactsasdata.org |
| Qian et al., Task-Relevant Feature-Dynamics Fidelity (ultrasound) | arXiv Aug 2026 | https://arxiv.org/abs/2608.29516 |
| Zhu et al., VISER (Toward Visually Realistic Simulation) | arXiv May 2026 | https://arxiv.org/abs/2605.06311 |
| Yu et al., How Should World Models Be Evaluated for Embodied Decision-Making? | arXiv Jun 2026 | https://arxiv.org/abs/2606.15032 |
| Miller et al., High-Performance RL on Spot (Wasserstein/MMD for sim parameters) | arXiv Apr 2025 | https://arxiv.org/abs/2504.17857 |
| Lin et al., Data Scaling Laws in Imitation Learning for Robotic Manipulation | ICLR 2025 oral (project page) | https://data-scaling-laws.github.io/ · https://arxiv.org/abs/2410.18647 |
| Sartor & Thompson, Neural Scaling Laws in Robotics | arXiv May 2024 | https://arxiv.org/abs/2405.14005 |
| Ai et al., Towards Embodiment Scaling Laws in Robot Locomotion | CoRL 2025 (arXiv comment) | https://arxiv.org/abs/2505.05753 |
| Zheng et al., Data Scaling Laws for IL-Based End-to-End Autonomous Driving | arXiv Dec 2024 | https://arxiv.org/abs/2412.02689 |
| Maddukuri et al., Sim-and-Real Co-Training | RSS 2025 (Crossref) | https://doi.org/10.15607/rss.2025.xxi.109 · https://arxiv.org/abs/2503.24361 |
| Wei et al., Empirical Analysis of Sim-and-Real Cotraining of Diffusion Policies | IROS 2025 (arXiv comment) | https://arxiv.org/abs/2503.22634 |
| Fan et al., Scaling Laws of Synthetic Images for Model Training … for Now | CVPR 2024 (Crossref) | https://doi.org/10.1109/cvpr52733.2024.00705 · https://arxiv.org/abs/2312.04567 |
| Lu et al., GWM: Gaussian World Models for Robotic Manipulation | ICCV 2025 (arXiv comment) | https://arxiv.org/abs/2508.17600 |
| Zhang, What Do World Models Learn in RL? Probing Latent Representations | arXiv Mar 2026 | https://arxiv.org/abs/2603.21546 |
| Majumdar et al., Predictive Red Teaming | CoRL 2025 poster (OpenReview search) | https://arxiv.org/abs/2502.06575 |
| Abou-Chakra et al., Real-is-Sim | arXiv Apr 2025 | https://arxiv.org/abs/2504.03597 |
| Aljalbout et al., The Reality Gap in Robotics (review) | Annual Review of Control, Robotics, and Autonomous Systems (arXiv comment) | https://arxiv.org/abs/2510.20808 |
| Chhablani et al., EmbodiedSplat | ICCV 2025 (already verified in content/06) | https://arxiv.org/abs/2509.17430 |
| Piotrowski et al., When Will the Tokens End? | ACL 2025 SRW (Crossref) | https://doi.org/10.18653/v1/2025.acl-srw.61 |
| K46 research groups (Grupa Uczenia Reprezentacji: "modele w przestrzeni wag") | official page | https://ai.pwr.edu.pl/research-groups |

## 8. Semantic Scholar citation counts (2026-09-26)

Citation counts as returned inside the Semantic Scholar bulk-search results of §6 (sorted by
`citationCount:desc`, 2026-09-26). The per-paper lookup endpoint was rate-limited (HTTP 429) for the whole
session, so only papers that surfaced in a bulk query have a count here; absence means "not retrieved", not
"zero".

| Paper | S2 citations | Retrieved in query |
|---|---|---|
| Li et al., SIMPLER (arXiv:2405.05941) | 548 | T5 |
| Lin et al., Data Scaling Laws in IL (arXiv:2410.18647) | 210 | B2 |
| NVIDIA, Cosmos World Foundation Model Platform (arXiv:2501.03575) | 864 | D1 |
| Gu et al., SAFE (arXiv:2506.09937) | 84 | T10 |
| Li et al., WorldEval (arXiv:2505.19017) | 62 | T5 |
| Gemini Robotics in Veo (arXiv:2512.10675) | 53 | A4 / T5 |
| Lu et al., GWM (arXiv:2508.17600) | 51 | D1 / T9 |
| Failure Prediction at Runtime for Generative Robot Policies (arXiv:2510.09459) | 40 | T10 |
| Jain et al., PolaRiS (arXiv:2512.16881) | 35 | T5 |
| Kachaev et al., Don't Blind Your VLA (arXiv:2510.25616) | 34 | A4 |
| Escontrela et al., GaussGym (arXiv:2510.15352) | 33 | F1 |
| Fang et al., ReBot (arXiv:2503.14526) | 33 | T3 |
| Wei et al., Sim-and-Real Cotraining of Diffusion Policies (arXiv:2503.22634) | 25 | F1 |
| Tseng et al., Scalable Policy Evaluation with Video World Models (arXiv:2511.11520) | 26 | F2 |
| Ai et al., Embodiment Scaling Laws (arXiv:2505.05753) | 21 | B1 |
| Torne et al., CASHER (arXiv:2412.01770) | 18 | B1 / T3 |
| Miller et al., RL on Spot with distributional measures (arXiv:2504.17857) | 17 | F3 |
| Swann et al., SAEs in VLA models (arXiv:2603.19183) | 14 | A4 |
| Lei et al., Mechanistic Analysis of Sim-and-Real Co-Training (arXiv:2604.13645) | 6 | T6 |
| Wu et al., RoboGauge (arXiv:2602.00678) | 5 | A1 |
| Bianchi et al., Weight-Space Meta-Learning for robot policies (arXiv:2606.07217) | 1 | T2 |
| Zhang, Real-to-Sim policy evaluation with 3DGS soft bodies (arXiv:2511.04665) | 36 | F4 |
| Cai et al., GaussTwin (arXiv:2603.05108) | — (not surfaced) | — |
| Kadian et al., Sim2Real Predictivity (arXiv:1912.06321) | — (not surfaced) | — |

## 9. Method notes and limits

- **APIs.** arXiv API (https://export.arxiv.org/api/query), Semantic Scholar Graph API bulk search and
  paper lookup, Crossref REST API, PMLR volume pages, official workshop/group pages. OpenAlex: one probe
  succeeded (§1.1), then HTTP 429 "free daily budget used up" for this network; OpenReview API returned a
  403 challenge; DBLP reset connections. Counts therefore come from arXiv and Semantic Scholar only.
- **Semantics.** arXiv `all:` matches title, abstract, author and comment fields with phrase quotes;
  Semantic Scholar bulk search matches title and abstract. A hit is *not* a close work; the top hits of every
  query were read and the genuinely close ones are listed in §1.2 and §3–§5. Three arXiv totals (T2, T3, T8)
  are inflated by generic terms and are flagged; their S2 counterparts use tighter terms.
- **Not done.** No full-text reading of the listed works beyond abstracts and arXiv comments; no check of
  SIMPLER's exact list of public checkpoints with paired real numbers (needed for option 1's label set); no
  contact with authors. Venue claims from arXiv comments are the authors' own statements.

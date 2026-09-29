# World models for embodied AI vs. reconstruction digital twins (issue #17)

Scope: GitHub issue #17 (Wave 7-O). Question: is the IPB topic (content/02, 07: data-efficient policy learning
in neural-reconstruction digital twins, 3DGS real→sim→real, navigation + manipulation) being overtaken by
learned *world models*, and is it too crowded for one PhD student? Checked on **2026-09-26** against the arXiv
API, OpenAlex, Crossref, Semantic Scholar and official pages. Every paper below was verified by ID or DOI;
every count states its query string and date. **UNVERIFIED** marks what could not be confirmed from a primary
source. This file does not edit content/; §6 below lists the edits it recommends.

---

## TL;DR

1. **World models are not replacing 3DGS digital twins; the two are converging.** The biggest labs (DeepMind
   Genie 2/3, NVIDIA Cosmos 1→3, Meta V-JEPA 2 / NWM, Wayve GAIA) build *video* world models trained on
   internet-scale data. But the systems that must *evaluate a real-robot policy* or *train with physics*
   still use reconstruction: SIMPLER, EmbodiedSplat, RoboGSim, Real-is-Sim, GWM (a *Gaussian* world model),
   and World Labs' Marble exports its worlds as Gaussian splats. The one direct head-to-head we found
   (WorldEval, arXiv 2505.19017, no venue) claims a learned evaluator beats a real-to-sim baseline, but it
   is unrefereed and single-lab; World-in-World (ICLR 2026 oral) finds visual quality does **not** predict
   task success and that *action-observation data* scaling matters most, which is exactly the IPB's
   real-data-budget question.
2. **What is crowded:** training foundation world models (11B-parameter Genie, 1M-hour V-JEPA 2 pretraining,
   79–296-author Cosmos reports) and generic "world model for navigation" papers (arXiv titles with
   *world model* + *navigation*: 2 → 5 → 17 → 26 per year 2023–2026, §3; two ECCV 2026 and one ICML 2026
   acceptance among them). **What is feasible and open:**
   (a) the *real-data budget* as the controlled variable (no paper we found varies capture minutes or real
   rollouts systematically; World-in-World scales post-training data, not real captures); (b) *predictivity*
   of twin vs. learned world model vs. generic simulator on the same policies (SRCC-style, only twins and
   learned evaluators have been measured separately, never against each other on navigation); (c) grounding
   a world model in a twin (few papers; GWM is the closest and is manipulation-only); (d) representation
   alignment between reconstructed, generated and real observations. All four run on frozen pretrained
   models (DINOv2, V-JEPA 2, Cosmos/NWM checkpoints) plus 3DGS, i.e. on academic GPUs.
3. **Recommendation:** keep the twin-centred topic and the real-data-budget thesis. Add world models to §6 as
   the second family of "learned simulators", and to §9/§7 as (i) an extra *comparator* in H3 (twin vs. learned
   world-model evaluator vs. generic sim, all scored by SRCC against the target domain) and (ii) a source of
   *pretrained predictive features* for the representation-alignment objective of H2. This turns the
   student's strengths (representation learning, model internals) into the differentiator and inoculates the
   IPB against the committee question "why not just use Genie/Cosmos?". Do not pivot to training world models.
4. **Venues:** this literature is published exactly where the IPB aims: ICLR (UniSim outstanding paper 2024,
   TD-MPC2, LAPA, World-in-World 2026 oral), ICML (Genie best paper 2024, DINO-WM, AdaWorld, VPP 2025), NeurIPS
   (iVideoGPT 2024), CVPR (NWM, Vid2Sim 2025), ICCV (GWM, IRASim, Aether, EmbodiedSplat 2025), ECCV
   (ManiGaussian 2024; NavWM, LWM-nav 2026), RSS (UWM 2025, Interactive World Simulator 2026); all are 200-pt
   ITiT venues on the 5.01.2024 list (research/venues-200.md). The frontier industrial systems (Genie 2/3,
   Cosmos, V-JEPA 2, GAIA) are blog posts or technical reports, not refereed papers.

---

## 0. Method and sources

- **Paper verification:** arXiv API `export.arxiv.org/api/query?id_list=…` (title, authors, dates, author
  comment) for 46 IDs; Crossref `api.crossref.org/works?query.bibliographic=` for DOIs; Semantic Scholar
  `graph/v1/paper/batch` (venue field and citation counts, 2026-09-26); OpenAlex for DOIs and counts.
  Venue claims below come from a DOI, a proceedings page (PMLR, icml.cc, iclr.cc, blog.iclr.cc) or the arXiv
  author comment; the source is named in each row.
- **Limits:** OpenAlex returned HTTP 429 after ~20 requests and OpenReview's API returned 403, so some venue
  checks rest on the arXiv comment + Semantic Scholar only (marked "arXiv comment / S2"). Citation counts are
  Semantic Scholar's and are indicative only. Content claims are from **abstracts and official pages**, not
  full texts, unless stated.
- **Counts:** arXiv API `search_query` with `submittedDate` windows (§3, query strings verbatim) and OpenAlex
  `title_and_abstract.search` with `publication_year` (§3). OpenAlex indexes arXiv, so its counts are larger
  and include duplicates of published versions; use the two sources for the *trend*, not the absolute number.

---

## 1. The 2023–2026 world-model landscape relevant to embodied AI

"World model" here = a learned, action-conditioned model of observations/dynamics used to imagine, plan,
train or evaluate policies. Three families matter for the IPB.

### 1.1 Latent world models for control (Dreamer line, JEPA line)

| System | Org | ID / DOI | Venue (source) | What it shows | Relevance |
|---|---|---|---|---|---|
| DayDreamer | UC Berkeley | arXiv 2206.14176 | CoRL 2022, PMLR 205:2226 (proceedings.mlr.press/v205/wu23c.html) | Dreamer on 4 real robots; quadruped walks in 1 h real time; wheeled robot navigates from camera images (abstract) | Proof that a *latent* world model learns from little real data, no simulator; a baseline the committee may raise |
| DreamerV3 | DeepMind / UofT | arXiv 2301.04104; doi:10.1038/s41586-025-08744-2 | **Nature 2025** (Crossref) | One configuration across 150+ tasks; Minecraft diamonds from scratch (abstract) | Reference algorithm for "train in imagination" |
| TD-MPC2 | UCSD | arXiv 2310.16828 | ICLR 2024 (arXiv comment / S2) | Scalable latent world model for continuous control | Model-based RL baseline |
| DINO-WM | NYU | arXiv 2411.04983 | **ICML 2025**, PMLR 267 (proceedings.mlr.press/v267) | World model on frozen **DINOv2 patch features**, trained offline, zero-shot planning (abstract) | Cheapest useful world model; feature-space prediction = representation-learning angle |
| V-JEPA 2 / V-JEPA 2-AC | Meta FAIR | arXiv 2506.09985 | arXiv report (no venue found) | 1M h video pretraining; action-conditioned post-training on **< 62 h** of DROID videos; zero-shot pick-and-place on Franka arms in two labs (abstract; ai.meta.com blog) | Shows small robot-data budgets suffice *given* internet pretraining; frozen encoder usable by a PhD student |
| Dreamer 4 | DeepMind | arXiv 2509.24527 (Sep 2025) | arXiv (no venue found; S2 122 cites) | Diamonds in Minecraft from **offline data only**; real-time interactive inference on a **single GPU**; action conditioning learned "from only a small amount of data" (abstract; danijar.com/project/dreamer4) | Data-efficiency claim to compare against; inference on one GPU, training cost not stated in the abstract |
| LAPA | KAIST/… | arXiv 2410.11758 | ICLR 2025 (arXiv comment / S2) | Latent action pretraining from action-free video | Latent actions = representation learning inside world models |
| AdaWorld | HKUST/… | arXiv 2503.18938 | ICML 2025, PMLR 267 | Adaptable world models with latent actions | same |
| VPP | Tsinghua/… | arXiv 2412.14803 | ICML 2025 spotlight, PMLR 267 | Policy on *predictive* features of a video diffusion model | Predictive features as policy representation (H2 angle) |

### 1.2 Generative video world models / "learned simulators" (big-lab line)

| System | Org | ID | Venue (source) | Scale, data | Relevance |
|---|---|---|---|---|---|
| UniSim | Google/Berkeley | arXiv 2310.06114 | **ICLR 2024 outstanding paper** (blog.iclr.cc 2024-05-06; iclr.cc awards) | Universal simulator from orchestrated internet + robot + navigation data; trains policies deployed zero-shot (abstract) | The founding "learned simulator" claim |
| Genie | DeepMind | arXiv 2402.15391 | **ICML 2024 best paper** (icml.cc/virtual/2024/awards_detail) | 11B params, unlabelled internet video, latent actions | Foundation world model |
| Genie 2 | DeepMind | blog, 2024-12-04 | no paper | 3D playable worlds from one image, consistent "up to a minute" (blog) | for "training and evaluating embodied agents" (blog wording) |
| **Genie 3** | DeepMind | blog, 2025-08-05 | no paper | Text-prompted worlds at **24 fps, 720p, consistent for a few minutes**; tested with the SIMA agent (blog) | Not released as weights; no action-space for real robots; no physics guarantees |
| Cosmos | NVIDIA | arXiv 2501.03575 (Jan 2025) | arXiv report; a workshop version doi:10.1145/3746262.3761969 (ACM MM '25 workshop, Crossref) | Open-weight *world foundation models* to fine-tune per robot; 79 authors | Usable as a pretrained backbone |
| Cosmos-Transfer1 | NVIDIA | arXiv 2503.14492 | arXiv | Sim→real *appearance* transfer conditioned on depth/segmentation; real-time on a GB200 NVL72 rack (abstract) | Direct competitor/complement to a 3DGS twin's appearance |
| **Cosmos 3** | NVIDIA | arXiv 2606.02800 (Jun 2026) | arXiv; 296 authors | "Omnimodal" world models unifying VLM, video generator, simulator and world-action model; open code/weights (abstract) | Shows where the compute frontier is; not a PhD-scale target |
| NWM | Meta/NYU | arXiv 2412.03572; doi:10.1109/CVPR52734.2025.01472 | **CVPR 2025** (Crossref) | 1B-param conditional diffusion transformer on egocentric human+robot video; plans navigation by simulating trajectories (abstract) | The reference *navigation* world model; released checkpoints |
| GAIA-1 / GAIA-2 | Wayve | arXiv 2309.17080 / 2503.20523 | tech reports | Driving world models | Industry, driving only |
| iVideoGPT | Tsinghua | arXiv 2405.15223; doi:10.52202/079017-2173 | NeurIPS 2024 (Crossref) | Scalable interactive video world model | |
| DreamGen | NVIDIA | arXiv 2505.12705 | arXiv (S2: 165 cites) | Synthetic "neural trajectories" from video world models + IDM; 22 new humanoid behaviours from one teleop task (abstract) | Video-generated data as the rival to twin-generated data |
| Marble | World Labs | worldlabs.ai/blog/marble-world-model, 2025-11-12 | product | Generates 3D worlds and **exports Gaussian splats and collider meshes** (blog) | Generative world model whose *output format is a 3DGS twin* |
| Surveys | — | arXiv 2510.16732 (world models for embodied AI); 2411.14499 (ACM CSUR ext.); 2503.04641 | | Taxonomies; open problems named: unified datasets, physical-consistency metrics, real-time cost, long-horizon drift (2510.16732 abstract) | Cite one in §6 |

### 1.3 World models as *policy evaluators* (the line closest to H3 / SRCC)

| System | ID | Venue (source) | Claim (abstract) |
|---|---|---|---|
| IRASim | arXiv 2406.14540; doi:10.1109/ICCV51701.2025.00917 | ICCV 2025 (Crossref) | Policy evaluation in the world model "strongly correlates" with the ground-truth simulator |
| WorldEval | arXiv 2505.19017 | arXiv only (S2: 62 cites) | Ranks real-world manipulation policies and checkpoints; "significantly outperforms … real-to-sim approach" |
| WorldGym | arXiv 2506.00613 | arXiv (S2: 52 cites; site world-model-eval.github.io) | VLA policies evaluated from a single real start frame; success in the world model "highly correlates" with real success; preserves rankings; "generating highly realistic object interaction remains challenging" |
| Ctrl-World | arXiv 2510.10125 (Stanford) | arXiv (S2: 148 cites) | Multi-view world model trained on DROID (95k trajectories, 564 scenes); ranks policies without real rollouts; +44.7% success from imagined SFT data |
| World-in-World | arXiv 2510.18135 | **ICLR 2026 oral** (arXiv comment / S2) | Closed-loop benchmark of world models on *task success*; "visual quality alone does not guarantee task success, controllability matters more"; "first data scaling law for world models in embodied settings"; post-training on action-observation data beats upgrading the video generator |
| Interactive World Simulator for Robot Policy Training and Evaluation | arXiv 2603.08546; doi:10.15607/RSS.2026.XXII.018 | **RSS 2026** (Crossref) | Consistency-model world model "from a moderate-sized robot interaction dataset"; stable > 10-min rollouts at 15 FPS **on a single RTX 4090** (abstract) |
| GigaWorld-1 | arXiv 2607.02642 (Jul 2026) | arXiv | WMBench: 7 video world models × 4 action encodings × 324k rollouts; "key properties that make a world model reliable for policy assessment remain poorly understood" |
| WorldSimProbe; *Do Robotic World Models Really Follow Actions?*; *How Should World Models Be Evaluated…* | arXiv 2608.09298; 2608.24885; 2606.15032 (2026) | arXiv | 2026 wave of *faithfulness* critiques: action-following and simulator contracts, not visual quality; "claim/evidence mismatch" in world-model papers (position 2606.15032) |

### 1.4 Reconstruction twins and their hybrids with world models

| System | ID | Venue (source) | What it is |
|---|---|---|---|
| SIMPLER | arXiv 2405.05941 | CoRL 2024 (S2; already §6 [37]) | Real-to-sim evaluation of manipulation policies; strong sim/real correlation |
| EmbodiedSplat | arXiv 2509.17430; doi:10.1109/ICCV51701.2025.02359 | ICCV 2025 (already §6 [30]) | 3DGS twin from phone capture; SRCC 0.87–0.97 |
| RoboGSim | arXiv 2411.11839 | arXiv (S2: 78 cites) | Real2Sim2Real 3DGS simulator with physics engine; online policy evaluation; zero-shot real transfer (abstract) |
| Real-is-Sim | arXiv 2504.03597 | arXiv (S2: 17) | Dynamic 3DGS twin synchronised with the real world at 60 Hz; policy always acts in the twin (abstract) |
| **GWM** (Gaussian World Model) | arXiv 2508.17600; doi:10.1109/ICCV51701.2025.00865 | **ICCV 2025** (Crossref) | World model that predicts *future Gaussian primitives* under robot actions; latent DiT + 3D VAE; serves as neural simulator for model-based RL; "initial data scaling potential of 3D world model" (abstract) |
| ManiGaussian | arXiv 2403.08321; doi:10.1007/978-3-031-72761-0_20 | ECCV 2024 (Crossref) | Dynamic Gaussian splatting as the policy's world representation |
| Aether | arXiv 2503.18945; doi:10.1109/ICCV51701.2025.00799 | ICCV 2025 (Crossref) | Unified 4D reconstruction + action-conditioned prediction + planning; trained on synthetic data only (abstract) |
| PhysTwin | arXiv 2503.17973; doi:10.1109/ICCV51701.2025.00678 | ICCV 2025 (Crossref) | Physics-informed twin of deformables from video |
| RoboTransfer | arXiv 2505.23171 | arXiv | Geometry-consistent video diffusion to re-render manipulation data (sim→real appearance) |
| Vid2Sim | arXiv 2501.06693; doi:10.1109/CVPR52734.2025.00155 | CVPR 2025 (already §6 [28]) | Monocular video → interactive 3DGS urban simulator |
| **GS-Playground** | arXiv 2604.25459 | RSS 2026 (arXiv comment; 42 authors) | Batch 3DGS rendering + parallel physics engine for vision-informed robot learning (abstract) |
| **D-REX** | arXiv 2603.01151 | ICLR 2026 poster (arXiv comment) | Differentiable real-to-sim-to-real engine on Gaussian splats; identifies object mass from video and control signals |
| RoboSnap | arXiv 2607.06699 | arXiv (2026) | One RGB image → simulation-ready scene: collision-aware foreground + 3DGS background; replay and evaluation on DROID scenes |
| GaussFly | arXiv 2604.05062 | arXiv (2026) | Real-to-sim-to-real drone navigation: 3DGS scenes + contrastive RL, representation learning decoupled from policy (abstract) |
| Mirage2Matter | arXiv 2602.00096 | arXiv (2026) | "Physically grounded Gaussian world model from video": 3DGS reconstruction + generative models for physics |
| GaussianDream++ | arXiv 2608.25659 | arXiv (2026) | Gaussian reconstruction/prediction tokens inside a VLA backbone |
| FARM | arXiv 2609.11445 | arXiv (Sep 2026) | 34k-parameter readout over the *frozen internal predictive states* of a robotic world model predicts failure (AUROC 85.7); closest in spirit to the student's ACL 2025 SRW method |

---

## 2. Q1: are world models replacing reconstruction simulators for training and evaluating policies?

**Verdict: no, not in 2023–2026; they are being merged.** Evidence:

- **For "replacing":** UniSim (ICLR 2024) and Genie 3 (2025) explicitly position generated video as the
  simulator for embodied agents; DreamGen trains humanoid policies from generated trajectories; WorldEval
  claims to beat a real-to-sim evaluator (abstract, unrefereed); Ctrl-World and WorldGym rank real policies
  without real rollouts. Cosmos 3 (June 2026) folds "world simulators" into one omnimodal model. NVIDIA's
  own Cosmos page still pairs Cosmos with an Omniverse *simulation* before and after training (nvidia.com/
  en-us/ai/cosmos, 2026-09-26).
- **Against:** every system that needs *physics* (collisions, contact, resets) or a *stable target domain*
  still reconstructs it: SIMPLER, EmbodiedSplat (SRCC 0.87–0.97), RoboGSim, Real-is-Sim (60 Hz sync), GWM,
  ManiSkill3's real-world twins. WorldGym's own abstract concedes "generating highly realistic object
  interaction remains challenging". World-in-World (ICLR 2026 oral) shows visual realism does not predict
  task success and that controllability and *action-observation data* drive closed-loop performance, i.e.
  the missing ingredient is exactly grounded, action-labelled data, which a twin produces for free. The
  survey 2510.16732 lists long-horizon drift, physical-consistency metrics and real-time cost as open.
  Genie 3 is not released and has no robot action interface (blog); Marble, the most "3D" of the generative
  world models, outputs Gaussian splats plus collider meshes, i.e. it *produces* a twin.
- **2026 confirms the merge rather than the replacement:** RSS 2026 accepted both a learned world-model
  simulator (Interactive World Simulator) and a 3DGS simulator (GS-Playground); ICLR 2026 accepted D-REX
  (Gaussian-splat twins with differentiable physics); a wave of 2026 papers questions the faithfulness of
  video world models as simulators (WorldSimProbe, GigaWorld-1, *Do Robotic World Models Really Follow
  Actions?*, position 2606.15032), and the "3D world model" line (Mirage2Matter, HY-World 2.0, GaussianDream++,
  ABot-3DWorld) *outputs* Gaussian splats. The arXiv counts (§3) show 3DGS sim-to-real flat at ~55/yr while
  world-model policy evaluation quadrupled; the cheap, grounded twin is becoming the *substrate* of the
  expensive world model, not its victim.
- **Navigation specifically:** NWM (CVPR 2025) plans by imagining trajectories and is trained on egocentric
  video, but it evaluates on datasets (RECON, SCAND-type data), not on real robots in the paper's abstract;
  the 2026 navigation world-model papers (§3) are mostly latent/feature world models trained on existing
  datasets. None we found builds a twin *of the target scene*; NWM's "unfamiliar environments from a single
  image" is the opposite design point (generic prior, no scene capture).

So the honest framing for the IPB: **two learned simulators now exist, the reconstructed twin (scene-specific,
physically grounded, cheap to build from minutes of video) and the generative world model (generic,
data-hungry, physically unconstrained).** The open question is not "which wins" but how much *real target
data* each needs to predict and improve real performance, and whether a twin can ground a world model. That
is the IPB's RQ2/RQ4 restated, and no paper in §1 answers it.

---

## 3. Q2: what is crowded (big labs) vs. feasible for one PhD student on academic GPUs

### 3.1 Volume of the field

**arXiv API** (`export.arxiv.org/api/query?search_query=<Q> AND submittedDate:[<from> TO <to>]`, `totalResults`,
queried 2026-09-26; 2026 = 1 Jan–26 Sep 2026):

| # | Query Q (arXiv fielded syntax) | 2023 | 2024 | 2025 | 2026 (to 26 Sep) |
|---|---|---|---|---|---|
| Q7 | `ti:"world model"` | 80 | 170 | 450 | 1098 |
| Q1 | `ti:"world model" AND (abs:robot OR abs:embodied)` | 28 | 45 | 168 | 351 |
| Q2 | `ti:"world model" AND ti:navigation` | 2 | 5 | 17 | 26 |
| Q3 | `abs:"Gaussian splatting" AND (abs:"sim-to-real" OR abs:"real-to-sim" OR abs:sim2real OR abs:real2sim OR abs:"digital twin")` | 1 | 12 | 54 | 55 |
| Q4 | `abs:"Gaussian splatting" AND abs:policy AND abs:robot` | 0 | 6 | 29 | 20 |
| Q5 | `abs:"world model" AND abs:"Gaussian splatting"` | 0 | 5 | 12 | 20 |
| Q6 | `abs:"world model" AND abs:"policy evaluation"` | 0 | 2 | 10 | 40 |
| Q8 | `abs:"world model" AND abs:"digital twin"` | 1 | 4 | 14 | 24 |

Reading of the arXiv table: world-model papers about robots (Q1) grew 28 → 351 per year and already exceed
3DGS sim-to-real papers (Q3, 1 → 55) by ~6×; **3DGS sim-to-real has plateaued in 2026 (55 vs. 54)** while
world-model policy evaluation (Q6) quadrupled (10 → 40). The intersections the IPB can claim (Q5, Q8: world
model ∧ Gaussian splatting / digital twin) are still at 20–24 papers per year.

**OpenAlex** (`api.openalex.org/works?filter=title_and_abstract.search:<Q>,publication_year:<Y>`, `meta.count`,
queried 2026-09-26):

| Query Q | 2023 | 2024 | 2025 | 2026 (to date) |
|---|---|---|---|---|
| OA1 `"world model" robot` | 82 | 122 | 315 | 886 |
| OA2 `"world model" navigation` | 33 | 34 | 92 | 262 |
| OA3 `"gaussian splatting" ("sim-to-real" OR "real-to-sim" OR sim2real OR real2sim OR "digital twin")` | 1 | 24 | 141 | 203 |
| OA4 `"world model" "gaussian splatting"` | 0 | 7 | 22 | 43 |
| OA5 `"world model" "policy evaluation"` | 0 | 2 | 9 | 59 |

Reading: world models for robots are growing ~3× per year and are already an order of magnitude larger than
3DGS sim-to-real (OA1 vs OA3). The *intersection* of world models with Gaussian splatting (OA4) and with
policy evaluation (OA5) is small but growing fastest; these are the hybrid niches of §4.

### 3.2 Crowded (do not compete here)

| Direction | Who | Why it is out of reach |
|---|---|---|
| Training foundation video world models | DeepMind (Genie 11B; Genie 2/3 unreleased), NVIDIA (Cosmos, 79→296 authors; Cosmos-Transfer1 real-time only on a GB200 NVL72 rack), Meta (V-JEPA 2: 1M h video), Wayve, World Labs | Internet-scale data and thousands of GPUs; results are blog posts / tech reports |
| Generic "world model for navigation/manipulation" | dozens of groups (OA2: 262 works in 2026 to date; arXiv Q2 below) | Incremental; the compute-rich groups (Meta NWM 1B params, Stanford Ctrl-World on 95k DROID trajectories) set the bar |
| Generalist policy evaluators (WorldGym, WorldEval, Ctrl-World, Cosmos-Surg) | Stanford, Google, NVIDIA, Beijing groups | Need large action-labelled datasets and VLA policies to rank |
| Real-robot humanoid/manipulation data engines (DreamGen, GR00T) | NVIDIA | hardware fleets |

### 3.3 Feasible on academic GPUs (WCSS Lem H100s, PLGrid; research/resources.md §2) and still open

| Direction | Why feasible | Why open (no paper found doing it, 2026-09-26) |
|---|---|---|
| **Real-data budget curves** for twins (RQ2/H4) | 3DGS twins train in GPU-hours from phone video (EmbodiedSplat: 20–30 min capture); policies via DD-PPO/BC on Habitat | Only RialTo varies real data (0–15 demos, manipulation); World-in-World scales *post-training* data of a generic world model, not target-scene captures; nobody reports budget→real-success curves |
| **Predictivity comparison: twin vs. learned world model vs. generic sim** (RQ4/H3) | Frozen NWM / Cosmos-Predict / V-JEPA 2-AC checkpoints as the "learned world model" arm; SRCC over ≥ 10 policy variants already planned; Interactive World Simulator (RSS 2026) trains on one RTX 4090 | Twins report SRCC (EmbodiedSplat, SIMPLER); world models report correlation with real success (WorldGym, WorldEval, IRASim, GigaWorld-1's WMBench, manipulation only) — **never measured side by side on the same policies**, and never for navigation (L7 in §8: 2 hits, neither does it) |
| **Twin-grounded world models** (hybrid) | GWM (ICCV 2025) shows the recipe: latent DiT + 3D VAE over Gaussians; a smaller variant conditioned on a target-scene twin is a single-GPU model | GWM is manipulation-only and not scene-specific; OA4 = 43 works in 2026, mostly 3DGS *as representation* not twin-grounded generation |
| **Representation alignment reconstructed↔generated↔real** (RQ3/H2) | DINO-WM/V-JEPA 2 features are frozen; contrastive/distribution-matching heads are cheap; FARM (2026) trains a 34k-parameter readout on frozen world-model states; *Think Like a World Model, Act Like a VLA* (2026) aligns a policy to cached frozen features | The IPB's alignment objective has no counterpart in the world-model papers; they align nothing to a *target scene*; 2605.06388 asks which latent space suits a world model but not which one closes the reconstructed↔real gap |
| **Twin correction from few rollouts** (RQ4) | Real-is-Sim syncs a twin at 60 Hz with a fixed rig; the IPB's few-rollout, offline version is lighter | Real-is-Sim needs continuous state estimation; no paper corrects a twin from *sparse* real rollouts and measures the SRCC gain |

Compute sanity check (abstracts): DINO-WM trains on offline trajectories with a frozen encoder; DayDreamer
learned on real robots with the 2022 Dreamer; Dreamer 4 infers in real time on one GPU; EmbodiedSplat is
Habitat + DN-Splatter meshes. None of the feasible directions requires training a video generator from
scratch. Fine-tuning Cosmos-Predict or NWM on a few thousand twin-rendered rollouts is a multi-GPU-days job
on Lem (UNVERIFIED: no measured cost found; state as an estimate in §9 if used).

---

## 4. Q3: where world models and reconstruction twins meet (the hybrid space to claim)

1. **Twin as the grounding of a world model.** A twin is a scene-specific, action-labelled data generator; a
   world model is a generic prior. World-in-World's finding (post-training on action-observation data >
   better generator) argues that *twin-rendered rollouts are the right post-training data* for a world
   model of the target scene. GWM and Marble show Gaussians are already the meeting representation. Open
   experiment for the IPB: post-train NWM/Cosmos on twin rollouts of the target scene and measure (a) SRCC
   vs. the target domain, (b) success of policies trained inside it, as a function of *capture minutes*
   (budget B). This is a natural P2 or P4 extension and stays within Stage III/IV compute.
2. **World model as evaluator vs. twin as evaluator.** H3 currently compares twin vs. generic simulator by
   SRCC. Adding a third arm, a frozen pretrained world model (NWM for navigation; WorldGym-style rollouts
   from the real start frame), makes H3 the first three-way predictivity study and directly answers "why not
   Genie/Cosmos?" with data. Cost: inference only.
3. **Representation learning inside world models.** DINO-WM, V-JEPA 2, LAPA, VPP all show that *predictive*
   features (future-patch or latent-action prediction) are better policy inputs than static ones. H2's
   alignment objective can align the encoder features of reconstructed, world-model-generated and real frames
   of the same place; the student's ACL 2025 SRW experience (forecasting from hidden states, GNN over
   layer states) transfers to probing which layers of a world model carry scene geometry vs. appearance. FARM (arXiv
   2609.11445, Sep 2026) shows the community has just started reading frozen world-model states with tiny
   readouts; doing it to *measure the sim-to-real gap* (reconstructed vs. real frames) is unclaimed.
   This is the least crowded and most "AI/ML" of the four.
4. **Appearance transfer instead of reconstruction** (Cosmos-Transfer1, RoboTransfer). A cheaper alternative
   arm for the *appearance* half of the sim-to-real gap: keep the twin's geometry/physics, re-render with a
   video diffusion model. Worth one ablation row in Stage IV (twin appearance vs. diffusion re-rendering),
   not a thesis.

---

## 5. Q4: 200-point venues where this literature is published

Venue Lp numbers and ITiT assignment: research/venues-200.md (list of 5.01.2024).

| Venue (200 pts, ITiT) | World-model / twin papers published there (verified source) |
|---|---|
| ICLR | UniSim 2024 (outstanding paper, blog.iclr.cc); TD-MPC2 2024 (arXiv comment); LAPA 2025 (arXiv comment); World-in-World 2026 oral, D-REX 2026 poster, Neural Gaussian Force Fields 2026 (arXiv comments) |
| ICML | Genie 2024 (best paper, icml.cc); DINO-WM, AdaWorld, VPP 2025 (PMLR v267); SC²-WM, UniJEPA 2026 (arXiv comments) |
| NeurIPS | iVideoGPT 2024 (Crossref doi:10.52202/079017-2173) |
| CVPR | NWM 2025 (doi:10.1109/CVPR52734.2025.01472); Vid2Sim 2025 (doi:…00155); GeoWorld 2026 (arXiv comment) |
| ICCV | GWM, IRASim, Aether, PhysTwin, EmbodiedSplat 2025 (Crossref DOIs above) |
| ECCV | ManiGaussian 2024 (LNCS doi:10.1007/978-3-031-72761-0_20); 2026: NavWM (arXiv 2606.24101, comment "accepted to ECCV 2026"), LWM for navigation (arXiv 2608.26190, journal_ref "ECCV 2026 (Spotlight)") — both UNVERIFIED beyond the arXiv comment |
| RSS | UWM 2025 (doi:10.15607/RSS.2025.XXI.015); PIN-WM 2025 (arXiv comment); Interactive World Simulator 2026 (doi:10.15607/RSS.2026.XXII.018); GS-Playground 2026 (arXiv comment) |
| Nature (journal, separate list) | DreamerV3 2025 (doi:10.1038/s41586-025-08744-2) |
| Not refereed | Genie 2/3 (blogs), Cosmos 1/Transfer1/3 (reports), V-JEPA 2, GAIA-1/2, DreamGen, WorldGym, WorldEval, Ctrl-World, Dreamer 4 (arXiv as of 2026-09-26) |

Implication: the IPB's venue plan (NeurIPS/ICML/ICLR + CVPR/ICCV/ECCV, RSS option) matches where this work
lands; CoRL (not 200-pt) hosts DayDreamer/SIMPLER-type robotics papers, so keep the ML/CV framing.

---

## 6. Recommended changes to the IPB (for the owners of content/; none applied here)

- **§6 (2 pages, tight):** add one paragraph "Learned world models as simulators" between "Neural scene
  reconstruction" and "Digital twins for manipulation": cite UniSim [ICLR 2024], Genie [ICML 2024], NWM
  [CVPR 2025], V-JEPA 2 [arXiv 2025], World-in-World [ICLR 2026] and one evaluator (WorldGym or IRASim
  [ICCV 2025]); state that they are generic priors trained on internet video, need action-observation data
  to be useful in the loop (World-in-World), and have not been compared with reconstructed twins on
  predictivity. Add GWM [ICCV 2025] as the hybrid. To stay within 2 pages, drop [14] Tremblay or [19]
  Bousmalis and shorten the domain-randomization paragraph. Research-gap sentence gains: "nor a comparison
  of reconstructed twins with learned world models as predictors of real performance".
- **§7 H3:** "the SRCC of the twin is higher than that of a generic simulator **and not lower than that of a
  pretrained navigation world model used as an evaluator**" (third arm, inference only). Keep the decision
  rule; add the arm to the pre-registration.
- **§9 Stage III:** name the world-model arm (NWM checkpoint; WorldGym-style rollouts from the real start
  frame) and the comparison metric (SRCC, paired on the same ≥ 10 policies). **Stage IV:** the alignment
  objective may use frozen predictive encoders (DINOv2/V-JEPA 2) and add the ablation row "twin appearance
  vs. diffusion re-rendering (Cosmos-Transfer1-style)". Optional Stage IV/P4: post-train a world model on
  twin rollouts and measure SRCC vs. capture minutes (twin-grounded world model).
- **§5/§8:** one sentence each: the thesis positions reconstructed twins against learned world models on the
  axis that matters for deployment, *real target-domain data*, and studies representations shared by both.
  §8 item 4 (evaluation methodology) becomes "for twins **and learned world models**".
- **§12 risks:** add "Generative world models make scene-specific twins unnecessary (sem. 4–7)": mitigation =
  H3's three-way comparison answers it empirically either way; the budget curves (H4) are the deliverable
  regardless of which simulator wins.
- **Do not** change §2 or the thesis. A pivot to "world models" would move the student into the crowded
  column of §3.2 with no hardware or data advantage.

---

## 7. Open items / UNVERIFIED

- RSS 2026 "Interactive World Simulator" (arXiv 2603.08546): title, DOI (Crossref) and abstract confirmed;
  full text not read.
- All 2026 venue claims in §8 (RSS 2026 GS-Playground, ICLR 2026 D-REX, ECCV 2026 NavWM / LWM, ICML 2026
  SC²-WM / UniJEPA, CVPR 2026 GeoWorld) rest on arXiv author comments only; proceedings not yet indexed.
- Venues of Dreamer 4, V-JEPA 2, WorldGym, WorldEval, Ctrl-World, DreamGen, Real-is-Sim, RoboGSim: none
  found as of 2026-09-26 (Semantic Scholar "venue" = arXiv or empty). OpenReview could not be queried (403).
- ECCV 2026 acceptance of NavWM and LWM-nav rests on arXiv author comments only.
- Training cost of fine-tuning NWM/Cosmos on twin rollouts: no published number; estimate before promising it.
- Whether Genie 3 will expose an API usable for robot policy evaluation: blog only, nothing verifiable.
- Citation counts (Semantic Scholar, 2026-09-26) are indicative; OpenAlex undercounts arXiv-only works.

## 8. 2026 landscape samples (arXiv, sorted by submission date, queried 2026-09-26)

Sample of the most recent entries (title, arXiv ID, venue if stated in the author comment; all verified on
the arXiv API 2026-09-26; venue claims from author comments are UNVERIFIED beyond that):

**L1 `ti:"world model" AND (ti:manipulation OR ti:robot OR ti:robotic)`, 2026: 113 results.** Sept 2026 alone:
PointCast (2609.28393), Generalizable Robotic Insertion with World Models (2609.28258, NVIDIA/UCSD, "IROS
2026"), *Think Like a World Model, Act Like a VLA* (2609.24682: distils a frozen world model's features into a
VLA by one alignment term), *Robot World Models Are Not Invariant to How the Actions Are Written*
(2609.23252), **FARM** (2609.11445: a 34k-parameter readout over the frozen predictive states of a robotic
world model detects failures, AUROC 85.7), DUET-DINO (2609.10506, Burgard), HaWMPO (2609.09941), *Identifying
Habit, Physics, and Nuisance in Robot World Models* (2609.09210), *Do Better Imagined Rollouts Mean Better
Robot Control?* (2609.02811), Motus2 (2608.30237), **GaussianDream++** (2608.25659: 3D Gaussian world
modelling inside a VLA), *Do Robotic World Models Really Follow Actions?* (2608.24885), WorldSimProbe
(2608.09298: "Observable Simulator Contract" for action-conditioned world models), XEWorld (2608.05799),
LAWM-3D (2608.05706), Robot-Factored World Models via Robot Rendering (2607.22535).

**L2 `abs:"Gaussian splatting" AND (sim-to-real|real-to-sim|sim2real|real2sim) AND abs:polic*`, 2026: 12
results** (the twin line is small but alive at top venues): **GS-Playground** (2604.25459, 42 authors,
"Robotics: Science and Systems 2026": batch 3DGS rendering + parallel physics for vision-informed robot
learning), **D-REX** (2603.01151, "ICLR 2026 Poster": differentiable real-to-sim-to-real engine on Gaussian
splats, identifies object mass from video), RoboSnap (2607.06699: one RGB image → simulation-ready scene with
a 3DGS visual layer and collision-aware foreground; evaluated on DROID scenes), VLK (2606.30645, Karen Liu:
humanoid loco-manipulation from synthetic interactions in reconstructed scenes), ExoGS (2601.18629), GaussFly
(2604.05062: contrastive RL for drone visuomotor policies in 3DGS fields, real-to-sim-to-real), QuadVerse
(2606.07118), HumanoidVLN (2608.12860), ReaDy-Go (2602.11575, RA-L; already §6 [29]).

**L3 `abs:"world model" AND abs:"Gaussian splatting"`: 37 results total (all years)**, i.e. the hybrid is
nascent: **Mirage2Matter** (2602.00096: 3DGS reconstruction from multi-view video + generative models for a
physically grounded Gaussian world model), HY-World 2.0 (2604.14268, Tencent: generates *navigable 3DGS
scenes*), ABot-3DWorld 0 (2607.11673), 4DGS-WAM (2608.25956), Visionary (2512.08478: WebGPU 3DGS platform as
"world model carrier"), GigaWorld-0 (2511.19861: world models as data engine), ChronoDreamer (2512.18619),
GWM (ICCV 2025), ManiGaussian++ (2506.19842), PIN-WM (2504.16693, RSS 2025), Dream to Manipulate
(2412.14957).

**L4 `abs:"world model" AND abs:"policy evaluation"`: 53 results total**, 40 of them in 2026: **GigaWorld-1**
(2607.02642: WMBench, 7 video world models, 324k simulated rollouts, "key properties that make a world model
reliable for policy assessment remain poorly understood"), *Interactive World Simulator* (2603.08546, RSS
2026: consistency-model world model from a "moderate-sized" dataset, 10-minute stable rollouts at 15 FPS on
**one RTX 4090**), dWorldEval (2604.22152), StressDream (2606.00267, Bajcsy), SC3-Eval (2606.18610),
WorldArena 1.0/2.0 (2602.08971, 2605.17912), World Action Verifier (2604.01985, Yilun Du), *How Should World
Models Be Evaluated for Embodied Decision-Making?* (2606.15032, position: "claim/evidence mismatch"),
**Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models** (2605.06388: six
encoders compared for action-conditioned latent-diffusion world models), Robotic Video World Models survey
(2601.07823, Majumdar), DreamDojo (2602.06949, NVIDIA, 30 authors), Qwen-RobotWorld (2606.17030, 39 authors),
Hydra-0 (2608.18077, NVIDIA Isaac), Pelican-Sim 1.0 (2609.12036), BWM (2607.29302).

**L5 `abs:"Dreamer 4" OR abs:"V-JEPA 2" OR abs:"Genie 3"`: 44 results**, dominated by JEPA follow-ups:
V-JEPA 2.1 (2603.14482, Meta), UniJEPA (2608.07409, "ICML 2026"), JEPA-VLA (2602.11832), *What Drives Success
in Physical Planning with JEPA World Models?* (2512.24497, LeCun), GeoWorld (2602.23058, "CVPR 2026"),
ARC-Bench (2609.05461: "closed-loop replanning masks broken action ranking in frozen JEPA world models"),
Cosmos-Surg-dVRK (2510.16240). Note: an `abs:"Genie 3"` search returns no robotics paper (only physics
hits), i.e. Genie 3 has not become a usable research platform as of 2026-09-26.

**L6 `abs:"world model" AND abs:"digital twin" AND abs:robot`: 14 results total**, mostly position papers
(Digital Twin AI 2601.01321; Holonic Digital Twins 2608.06227; The Robot Data Factory 2609.16705, Haddadin).
Nobody has yet claimed "twin-grounded world model" as a research line.

**L7 `abs:"world model" AND abs:"real-world" AND abs:navigation AND abs:Gaussian`: 2 results** (FlyMirage
2605.19600; Policy-Guided World Model Planning for VLN 2603.25981): **the navigation + twin + world-model
corner is empty.**

**Navigation world models 2026** (from the `ti:"world model" AND ti:navigation` search, 51 total, 26 in 2026):
NavWM (2606.24101, "ECCV 2026"), Latent World Models for navigation (2608.26190, "ECCV 2026 Spotlight":
trains navigation policies by RL entirely inside a latent world model from real-world datasets), SC²-WM
(2608.07548, "ICML 2026", VLN-CE), Skytopia (2609.26007), AirDreamer (2606.03252), WorldFly (2606.06147),
GLAM (2609.14561), AR Forcing (2605.31314), Drift-Resistant NWM (2605.24761, Alahi), Uncertainty-Aware WM for
aerial image-goal navigation (2608.05597), Latent WMs with monotone planning costs (2608.09073). All train on
existing datasets; none reconstructs the deployment scene or measures a real-data budget.

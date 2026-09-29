# Nearby niches: representations and models (issue #21, Wave8-S)

Compiled 2026-09-26 · owner: Wave8-S worker · owns only this file · does not edit `content/`.
Extends [crowdedness.md](crowdedness.md), [world-models.md](world-models.md),
[novelty-options.md](novelty-options.md) and [novelty-synthesis.md](novelty-synthesis.md). This report does
not re-examine their main option ("transfer forecasting from policy internals / weight space", novelty-options
§3) or "probing world models" as a thesis (novelty-options rank 4, world-models §4.3). It looks at the
representation and model niches *around* them and scores each one.

## TL;DR

Scores: **Dist** = distance to the current IPB topic (0 = same, 3 = far). **Fit** = fit to the student
(representation learning, GNNs, probing hidden states, LLMs; 0–3). **NoRobot** = feasibility without an own
robot (0–3). **S2 23/24/25/26** = Semantic Scholar bulk-search counts for the niche's main query (2026 through
26 Sep). **ML share** = share of arXiv papers (2023–26) whose comments name an ML/vision venue
(NeurIPS/ICLR/ICML/CVPR/ICCV/ECCV/AAAI/IJCAI) among those naming an ML/vision or robotics venue
(CoRL/RSS/ICRA/IROS/RA-L).

| # | Niche (short) | S2 23/24/25/26 | Dist | Fit | NoRobot | ML share | Verdict |
|---|---|---|---|---|---|---|---|
| N1 | Model merging / weight interpolation of twin-trained policies | 1 / 1 / 4 / 10 | 1 | 3 | 3 | 1 of 3 (robot merging); merging overall 146 of 148 | **Emerging** |
| N2 | Parameter-efficient adapters (LoRA) for twin-to-real under a real-data budget | 2 / 2 / 2 / 19 | 1 | 2 | 1 | 18 of 68 (26 %) | **Emerging**, low ML novelty |
| N3 | Mechanistic interpretability of policies/VLAs: where the sim-vs-real gap sits | 11 / 9 / 28 / 93 (VLA interp.) | 1 | 3 | 3 | 7 of 11 (64 %) | **Active** (VLA interp.); sim-vs-real angle **open** |
| N4 | Robustness of frozen foundation encoders to the reconstruction gap (3DGS artifacts) | 1 / 2 / 3 / 1 (tight); 6 / 11 / 23 / 15 (broad) | 1 | 3 | 3 | 5 of 6 (83 %) | **Open** |
| N5 | GNNs over scene graphs of twins as policy/transfer representation | 2 / 9 / 9 / 8; twin-specific 0 / 0 / 5 / 13 | 2 | 3 | 3 | see §N5 | **Emerging**, robotics-venue heavy |
| N6 | LLM/VLM agents that build twins (articulation, physical parameters from video) | 5 / 12 / 23 / 39 (artic.); 1 / 18 / 29 / 47 (physics) | 1 | 2 | 2 | see §N6 | **Active**, growing fast |
| N7 | Probing video world models for physical/3D state | 1 / 3 / 13 / 46 | 2 | 3 | 3 | see §N7 | **Active** (2026 surge) |
| N8 | Hypernetworks / weight generation for scene-conditioned policies | 18 / 11 / 49 / 38 | 2 | 2 | 2 | see §N8 | **Active** |
| N9 | Reconstruction uncertainty as a training signal for policies in twins | 0 / 0 / 1 / 1 | 1 | 2 | 3 | see §N9 | **Open** (thin, also low demand) |
| N10 | Representational similarity of twin-trained vs. real-trained policies | 0 / 0 / 1 / 0 (tight); 4 / 8 / 9 / 20 (broad) | 1 | 3 | 2 | see §N10 | **Open** |
| N11 | Test-time adaptation of twin-trained policies at deployment | 12 / 10 / 32 / 35 | 1 | 2 | 1 | see §N11 | **Active** |

**Top 3 (details in §12):**
1. **N4: reconstruction-gap robustness of frozen encoders.** Open (≤ 3 S2 papers/yr on the tight query),
   83 % ML-venue share, doable on public scans only. First paper: a benchmark of paired real and
   twin-rendered frames at matched poses and graded capture budgets, scoring encoder invariance against
   downstream frozen-encoder policy transfer (CVPR/NeurIPS D&B).
2. **N3 + N10: where the sim-to-real gap lives inside a policy.** VLA interpretability is active (93 S2 papers
   in 2026), but no paper found localizes the twin-vs-real gap layer by layer or patches it. This fits the
   student's hidden-state probing work exactly (ICLR/NeurIPS).
3. **N1: merging per-scene expert policies trained in twins.** Robot-policy merging only started in 2025–26
   (MergeVLA at CVPR 2026 merges *skills*). Merging across *scenes/twins* and sim↔real weight interpolation
   is unclaimed, and it reuses the policy zoo of novelty-options option 1 (ICLR/ICML).

**Least attractive:** N2 and N11 (active or engineering-flavoured, need a real deployment stream), N6 (big-lab
growth, robotics venues), N8 (active, compute-heavy), N7 (already surging and covered in world-models.md).

## 0. Method and caveats

- **Sources and date.** arXiv API (`export.arxiv.org/api/query`, `abs:` field, one request per year with
  `submittedDate:[YYYY01010000 TO YYYY12312359]`, count = `opensearch:totalResults`) and Semantic Scholar
  Graph API (`/graph/v1/paper/search/bulk?query=<Q>&year=<Y>`, count = `total`). All queries ran on
  **2026-09-26**. 2026 is partial (through 26 Sep). The Semantic Scholar query is the arXiv query with `abs:`
  removed, `AND` → `+` and `OR` → `|`. OpenAlex was not used (quota exhausted earlier in this wave, see
  crowdedness.md §1).
- **Rate limits.** Several workers queried the same APIs from this IP in parallel. Semantic Scholar returned
  HTTP 429 and arXiv returned HTTP 500 (for `max_results=0`) and then 429. The script retried with
  back-off and did not fail. Cells that stayed empty after the retries are marked **n/a**. Semantic Scholar
  counts are complete for every niche.
- **Reading the counts.** arXiv's `abs:` search matches phrases loosely and some acronyms collide.
  N2's arXiv counts are inflated: `LoRA` also matches LoRa radio and `adapter` matches hardware adapters,
  so use the Semantic Scholar row. Read trends, not absolute numbers.
- **ML share** comes from arXiv comment fields (`co:`), 2023–2026. Authors do not always report
  acceptances, so these are lower bounds, and small denominators are noisy.
- **Papers.** Every paper below was checked on 2026-09-26 against the arXiv API (`id_list=`) for its title
  and first-version date. Venue labels come from the arXiv comment field and are marked "(arXiv comment)"
  when that is their only source. No citation counts are given here because Semantic Scholar was throttled.
- **Verdict scale** (same as crowdedness.md §1, plus one level): *crowded* means ≥ 50 papers/yr on the
  question, or the exact claim is already shown by ≥ 2 groups. *Active* means 10–50/yr with partial
  demonstrations. *Emerging* means < 10–20/yr with the first ML-venue papers in 2025–26. *Open* means < 5/yr
  and no demonstration of the exact claim found.

---

## N1. Model merging and weight interpolation of twin-trained policies

**RQ.** Can policies trained separately in several reconstruction twins (one expert per scene or capture
budget) be merged in weight space (task arithmetic, TIES, soups, sim↔real interpolation) into one policy
that transfers better to unseen real scenes than joint training at the same compute?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N1a (merging in general) `abs:"model merging" OR abs:"task arithmetic" OR abs:"model soup" OR abs:"model soups" OR abs:"task vectors" OR abs:"weight interpolation"` | 44 / 187 / 327 / 298 | 113 / 323 / 518 / 421 |
| N1b (× robot) `(N1a) AND (abs:robot OR abs:robotic OR abs:"robot policy" OR abs:"visuomotor" OR abs:"vision-language-action" OR abs:"sim-to-real")` | 0 / 1 / 1 / 7 | 1 / 1 / 4 / 10 |

A relevance-sorted arXiv search for `(abs:"sim-to-real" OR abs:sim2real) AND (abs:"weight interpolation" OR
abs:"model merging" OR abs:"weight averaging" OR abs:"weight space" OR abs:"task vector")` returned one
unrelated hit (an underwater optical-flow dataset). No sim-to-real merging paper was found.

**Closest verified papers.**
1. Lawson & Qureshi, *Merging Decision Transformers: Weight Averaging for Forming Multi-Task Policies*,
   arXiv:2303.07551 (2023).
2. *MergeVLA: Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent*, arXiv:2511.18810
   (CVPR 2026, arXiv comment). It merges skills, not scenes or domains.
3. *Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging*, arXiv:2512.08333
   (2025). It uses merging to keep generality after fine-tuning.

**Scores.** Dist 1 (same object: twin-trained policies; new lever: weight space). Fit 3 (weight-space
learning is listed by K46 and matches the student's representation work). NoRobot 3 (proxy-real tier; public
scans). ML share: robot merging 1 of 3 (tiny sample); merging overall 146 ML vs. 2 robotics. **Verdict:
emerging.** Merging is crowded in LLMs but only beginning for robot policies, and nobody merges across twins
or along the sim↔real axis.

## N2. Parameter-efficient adapters for twin-to-real under a real-data budget

**RQ.** Given a policy pretrained in a twin and B minutes of real data, does restricting adaptation to a
low-rank or adapter subspace give a better real-SR-per-minute curve than full fine-tuning or co-training,
and which layers should carry the adapter?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N2a `(abs:LoRA OR abs:adapter OR abs:adapters OR abs:"parameter-efficient") AND (abs:"sim-to-real" OR abs:sim2real OR abs:"real-to-sim")` | 46 / 64 / 153 / 149 (inflated, see §0) | 2 / 2 / 2 / 19 |

**Closest verified papers.**
1. *SLowRL: Safe Low-Rank Adaptation Reinforcement Learning for Locomotion*, arXiv:2603.17092 (2026).
2. *Real2Sim or Sim2Real: Robotics Visual Insertion using Deep RL and Real2Sim Policy Adaptation*,
   arXiv:2206.02679 (2022).
3. Truong et al., *Bi-directional Domain Adaptation for Sim2Real Transfer of Embodied Navigation Agents*,
   arXiv:2011.12421 (2020). It uses small adaptation modules for navigation, before LoRA.

**Scores.** Dist 1. Fit 2 (PEFT is standard ML, but there is little representation insight unless combined
with N3). NoRobot 1 (the claim is about *real* minutes; proxy-real weakens it). ML share 18 of 68 (26 %,
inflated denominator). **Verdict: emerging, low ML novelty.** Best used as a baseline or ablation inside H4
(budget curves), not as a thesis line.

## N3. Mechanistic interpretability of policies/VLAs: where the sim-vs-real gap sits

**RQ.** In which layers and features of a twin-trained policy (or an open VLA) do paired twin-rendered and
real observations of the same state diverge, and does patching or steering those features recover real
performance?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N3a (interpretability × policies) `(abs:"mechanistic interpretability" OR abs:"sparse autoencoder" OR abs:"sparse autoencoders" OR abs:probing OR abs:"linear probe" OR abs:"linear probes") AND (abs:"vision-language-action" OR abs:"robot policy" OR abs:"robot policies" OR abs:visuomotor OR abs:"navigation policy" OR abs:"embodied agent")` | 2 / 1 / 17 / 65 | 11 / 9 / 28 / 93 |
| N3b (interpretability × sim-to-real) `(abs:"mechanistic interpretability" OR abs:"sparse autoencoder" OR abs:"sparse autoencoders" OR abs:probing OR abs:"linear probe" OR abs:interpretability) AND (abs:"sim-to-real" OR abs:sim2real OR abs:"reality gap" OR abs:"domain gap") AND (abs:robot OR abs:policy OR abs:policies)` | 8 / 4 / 26 / 26 | 8 / 7 / 35 / 55 |

N3b is loose ("interpretability" appears in many unrelated sim-to-real abstracts). A relevance-sorted arXiv
search for interpretability/probing/SAE × sim-to-real × policy returned no paper that localizes the
sim-vs-real gap inside a policy. The top hits were co-training analyses and causal discovery over
simulator parameters (arXiv:2306.15864).

**Closest verified papers.**
1. *Mechanistic interpretability for steering vision-language-action models*, arXiv:2509.00328 (CoRL 2025,
   arXiv comment).
2. *Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models*, arXiv:2603.19183 (2026).
3. *Emergent World Representations in OpenVLA*, arXiv:2509.24559 (2025). Also relevant: *Don't Blind Your
   VLA: Aligning Visual Representations for OOD Generalization*, arXiv:2510.25616 (2025), and *Not All
   Features Are Created Equal: A Mechanistic Study of VLA Models*, arXiv:2603.19233 (ICLR 2026 workshop,
   arXiv comment).

**Scores.** Dist 1. Fit 3 (this is the student's ACL 2025 method class: probing hidden states, a GNN over
layers). NoRobot 3 (open VLA checkpoints; paired twin/real frames from public scans or public sim/real
evaluation sets). ML share 7 of 11 (64 %). **Verdict: active** for VLA interpretability in general (65 arXiv
papers in 2026 vs. 1 in 2024). The **sim-vs-real localization and patching angle is open**. Risk: fast-moving
topic; the VLA-steering groups could add a sim-vs-real section.

## N4. Robustness of frozen foundation encoders to the reconstruction gap

**RQ.** How invariant are frozen visual encoders (DINOv2, SigLIP/CLIP, VC-1, V-JEPA-style) to the specific
artifacts of neural reconstruction (floaters, blur, view extrapolation, exposure baking, capture budget), and
does encoder invariance on paired real-vs-rendered frames predict the transfer of frozen-encoder policies
trained in the twin?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N4a (broad) `(abs:"pre-trained visual representations" OR abs:"pretrained visual representations" OR abs:"visual foundation model" OR abs:DINOv2 OR abs:CLIP OR abs:SigLIP) AND (abs:"sim-to-real" OR abs:sim2real OR abs:"gaussian splatting" OR abs:NeRF) AND (abs:robot OR abs:policy OR abs:navigation OR abs:manipulation)` | 4 / 7 / 17 / 13 | 6 / 11 / 23 / 15 |
| N4b (tight) `(abs:"gaussian splatting" OR abs:NeRF OR abs:"neural rendering" OR abs:"novel view synthesis") AND (abs:artifacts OR abs:robustness OR abs:robust) AND (abs:"pre-trained visual representations" OR abs:"pretrained visual representations" OR abs:DINOv2 OR abs:CLIP OR abs:"foundation model features" OR abs:"frozen features") AND (abs:robot OR abs:policy OR abs:navigation OR abs:manipulation)` | 1 / 1 / 2 / 0 | 1 / 2 / 3 / 1 |

**Closest verified papers.**
1. Silwal et al., *What do we learn from a large-scale study of pre-trained visual representations in sim and
   real environments?*, arXiv:2310.02219 (2023). It studies sim vs. real for PVRs on real robots, but with
   classical simulators, not reconstruction twins, and without artifact-level analysis.
2. Burns et al., *What Makes Pre-Trained Visual Representations Successful for Robust Manipulation?*,
   arXiv:2312.12444 (2023). It covers robustness to lighting/texture shifts, not to reconstruction artifacts.
3. Majumdar et al., *Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?*
   (VC-1/CortexBench), arXiv:2303.18240 (2023). Also relevant: *Geometry Meets Vision: Revisiting Pretrained
   Semantics in Distilled Fields*, arXiv:2510.03104 (2025), which uses features in radiance fields but no
   policy.

**Relation to novelty-options option 2 ("task-conditioned twin fidelity").** Option 2 asks which *twin*
fidelity metric predicts transfer. N4 flips the object and asks which *encoder* is invariant to the
reconstruction gap. The two share the same paired-frame dataset and can be one project with two papers.

**Scores.** Dist 1. Fit 3 (representation learning; CKA/probing). NoRobot 3 (ScanNet++-style datasets with
held-out real frames at known poses allow paired real-vs-rendered frames without a robot; the choice of
dataset must be checked against its licence). ML share 5 of 6 (83 %). **Verdict: open.** The PVR sim-vs-real
line stopped at classical simulators in 2023, and the 3DGS line does not study encoders.

## N5. GNNs over scene graphs of twins

**RQ.** Does a 3D scene graph extracted from the twin (objects, rooms, relations), encoded by a GNN, give a
policy representation that is more invariant to the reconstruction gap than pixels, and does it transfer
across scenes and from navigation to manipulation?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N5a `(abs:"scene graph" OR abs:"scene graphs") AND (abs:"graph neural network" OR abs:"graph neural networks" OR abs:GNN OR abs:"graph transformer") AND (abs:navigation OR abs:manipulation OR abs:policy OR abs:robot)` | 3 / 5 / n/a / n/a | 2 / 9 / 9 / 8 |
| N5b `(abs:"scene graph" OR abs:"scene graphs") AND (abs:"sim-to-real" OR abs:sim2real OR abs:"digital twin" OR abs:"gaussian splatting" OR abs:"real-to-sim") AND (abs:policy OR abs:robot OR abs:navigation)` | n/a | 0 / 0 / 5 / 13 |

**Closest verified papers.**
1. Ravichandran et al., *Hierarchical Representations and Explicit Memory: Learning Effective Navigation
   Policies on 3D Scene Graphs using Graph Neural Networks*, arXiv:2108.01176 (ICRA, per arXiv comment; year not stated there).
2. *Task-Driven Graph Attention for Hierarchical Relational Object Navigation*, arXiv:2306.13760 (2023).
3. *Compose by Focus: Scene Graph-based Atomic Skills*, arXiv:2509.16053 (ICRA 2026, arXiv comment). On the
   twin side: *PhySPRING: Structure-Preserving Reduction of Physics-Informed Twins via GNN*,
   arXiv:2605.07687 (2026).

**Scores.** Dist 2 (it changes the policy input, not the twin question). Fit 3 (GNNs). NoRobot 3. ML share:
arXiv venue counts n/a (see §0). The closest papers above are all at robotics venues. **Verdict:
emerging, robotics-venue heavy.** The GNN-on-scene-graph policy is an old idea (2021). What is new is using it
as a *gap-invariant* representation for twins, but that alone is a weak ML-venue claim. It works better as an
ablation arm of N4 (pixels vs. frozen features vs. graphs).

## N6. LLM/VLM agents that build twins (articulation, physical parameters from video)

**RQ.** Can a VLM/LLM agent infer the articulation and physical parameters of a scene captured on video well
enough that policies trained in the resulting interactive twin transfer as well as policies trained in a
manually specified twin?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N6a (articulation) `(abs:articulation OR abs:articulated OR abs:URDF) AND (abs:"vision-language model" OR abs:"vision-language models" OR abs:VLM OR abs:VLMs OR abs:"large language model" OR abs:LLM) AND (abs:video OR abs:reconstruction OR abs:"digital twin" OR abs:simulation OR abs:simulator)` | n/a | 5 / 12 / 23 / 39 |
| N6b (physics) `(abs:"physical parameters" OR abs:"physical properties" OR abs:"material properties" OR abs:"system identification") AND (abs:"vision-language model" OR abs:"vision-language models" OR abs:VLM OR abs:VLMs OR abs:"large language model" OR abs:LLM) AND (abs:video OR abs:"gaussian splatting" OR abs:simulation OR abs:"digital twin")` | n/a | 1 / 18 / 29 / 47 |

**Closest verified papers.**
1. *Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model*,
   arXiv:2410.13882 (ICLR 2025, arXiv comment). Related: Real2Code, arXiv:2406.08474 (2024); URDFormer,
   arXiv:2405.11656 (RSS 2024, arXiv comment).
2. *Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real
   Manipulation*, arXiv:2510.11689 (ICRA 2026, arXiv comment).
3. *RigPI: Dynamic Parameter Identification of Rigid Body via VLM-Seeded Differentiable Simulation*,
   arXiv:2606.25212 (IROS 2026, arXiv comment). Also: LLMPhy, arXiv:2411.08027 (AISTATS 2026, arXiv comment);
   PhysTwin, arXiv:2503.17973 (2025).

**Scores.** Dist 1 (it is the twin-building step). Fit 2 (LLM agents yes, but the evaluation is physics and
robotics). NoRobot 2 (public video; physical ground truth is scarce without a robot). ML share: arXiv venue
counts n/a (see §0). The closest papers are split: ICLR 2025 and AISTATS 2026 vs. RSS 2024, ICRA 2026 and
IROS 2026. **Verdict: active, growing about 2× per year.** Several strong groups work here, and it moves the
thesis back toward twin-building infrastructure, which crowdedness.md advises against.

## N7. Probing video world models for physical/3D state

**RQ.** Do latent states of pretrained video world models linearly encode the 3D geometry and physical
parameters of a scene, and does this encoding degrade on reconstruction-twin rollouts relative to real video?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N7a `(abs:"world model" OR abs:"world models" OR abs:"video generation model" OR abs:"video prediction") AND (abs:probing OR abs:"linear probe" OR abs:"linear probes") AND (abs:physics OR abs:physical OR abs:geometry OR abs:depth OR abs:"3D")` | n/a | 1 / 3 / 13 / 46 |

**Closest verified papers.**
1. Garrido et al., *Intuitive physics understanding emerges from self-supervised pretraining on natural
   videos*, arXiv:2502.11831 (2025).
2. *How Do Video Foundation Models Encode Intuitive Physics? Probing Across Pretraining Paradigms*,
   arXiv:2606.09646 (2026).
3. *Interpreting Physics in Video World Models*, arXiv:2602.07050 (2026). Related: Kang et al., *How Far is
   Video Generation from World Model: A Physical Law Perspective*, arXiv:2411.02385 (ICML 2025, arXiv
   comment); Physics-IQ, arXiv:2501.09038 (2025).

**Scores.** Dist 2. Fit 3. NoRobot 3. ML share: arXiv venue counts n/a (see §0); the closest papers target
ML venues. **Verdict: active (from 3 to 46 S2 papers/yr over 2024–26).** Only the twin-vs-real sub-question
is new, and world-models.md §4.3 already records it. It is not a separate niche for this student.

## N8. Hypernetworks and weight generation for scene-conditioned policies

**RQ.** Can a hypernetwork or weight-diffusion model, conditioned on an embedding of a scene's twin,
generate a policy for that scene without per-scene RL, with the real transfer of the generated policies
matching per-scene training?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N8a `(abs:hypernetwork OR abs:hypernetworks OR abs:"parameter generation" OR abs:"weight generation" OR abs:"generating policy parameters" OR abs:"neural network diffusion") AND (abs:robot OR abs:"reinforcement learning" OR abs:"sim-to-real" OR abs:"imitation learning")` | n/a | 18 / 11 / 49 / 38 |

**Closest verified papers.**
1. Rezaei-Shoshtari et al., *Hypernetworks for Zero-shot Transfer in Reinforcement Learning*,
   arXiv:2211.15457 (AAAI 2023, arXiv comment).
2. Liang et al., *Make-An-Agent: A Generalizable Policy Network Generator with Behavior-Prompted Diffusion*,
   arXiv:2407.10973 (NeurIPS 2024, arXiv comment).
3. *Robotic Policy Adaptation via Weight-Space Meta-Learning*, arXiv:2606.07217 (2026).

**Scores.** Dist 2. Fit 2 (weight space yes; generative training of weights needs large zoos). NoRobot 2
(proxy-real; compute-heavy). ML share: arXiv venue counts n/a (see §0); the closest papers are at AAAI and
NeurIPS. **Verdict: active.** It could be a later extension of an N1/option-1 zoo, not a first paper.

## N9. Reconstruction uncertainty as a training signal for policies in twins

**RQ.** Does propagating per-Gaussian or per-ray reconstruction uncertainty into policy training
(uncertainty-weighted rewards, observation dropout, pessimism) improve real transfer from a short capture?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N9a `(abs:"gaussian splatting" OR abs:NeRF OR abs:"neural radiance field" OR abs:"neural reconstruction") AND (abs:uncertainty OR abs:"uncertainty-aware") AND (abs:policy OR abs:"reinforcement learning" OR abs:"imitation learning") AND (abs:robot OR abs:navigation OR abs:manipulation)` | n/a | 0 / 0 / 1 / 1 |

**Closest verified papers.**
1. *CATNIPS: Collision Avoidance Through Neural Implicit Probabilistic Scenes*, arXiv:2302.12931 (IEEE T-RO,
   arXiv comment). It covers planning, not policy learning.
2. *Enhancing Exploratory Capability of Visual Navigation Using Uncertainty of Implicit Scene
   Representation*, arXiv:2411.03487 (2024).
3. Phys2Real, arXiv:2510.11689 (uncertainty over physical parameters, not over rendering). On the
   uncertainty-estimation side: Bayes' Rays, arXiv:2309.03185; FisherRF, arXiv:2311.17874.

**Scores.** Dist 1. Fit 2 (it is probabilistic modelling more than representation learning). NoRobot 3.
ML share: arXiv venue counts n/a (see §0). **Verdict: open but thin.** The low count may reflect low demand:
3DGS uncertainty estimates are still weak. It is a good ablation for H1/H4 (does uncertainty-aware training
cut the capture budget?) but a risky thesis line.

## N10. Representational similarity of twin-trained vs. real-trained policies

**RQ.** Do policies trained in a reconstruction twin and on real data of the same scene converge to similar
internal representations (CKA, SVCCA, model stitching), and does that similarity, measured before
deployment, track the real performance gap?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N10a (broad) `(abs:CKA OR abs:"representational similarity" OR abs:"representation similarity" OR abs:"platonic representation" OR abs:"representational alignment") AND (abs:robot OR abs:"robot policy" OR abs:"reinforcement learning" OR abs:"sim-to-real" OR abs:embodied)` | n/a | 4 / 8 / 9 / 20 |
| N10b (tight) `(abs:CKA OR abs:"representational similarity" OR abs:"representation similarity" OR abs:"platonic representation" OR abs:"representational alignment") AND (abs:"sim-to-real" OR abs:sim2real OR abs:"simulation and real" OR abs:"simulated and real")` | n/a | 0 / 0 / 1 / 0 |

**Closest verified papers.**
1. Huh et al., *The Platonic Representation Hypothesis*, arXiv:2405.07987 (2024). It concerns
   representational convergence in general and does not cover embodied policies.
2. *Skill Transfer and Discovery for Sim-to-Real Learning: A Representation-Based Viewpoint*,
   arXiv:2404.05051 (2024).
3. *Divergent representations of ethological visual inputs emerge from supervised, unsupervised, and
   reinforcement learning*, arXiv:2112.02027 (2021).

**Scores.** Dist 1. Fit 3 (CKA/probing/stitching is core representation-learning methodology). NoRobot 2
(real-trained policies need real data: public offline navigation datasets, or real frames of the scanned
scene with privileged-planner labels). ML share: arXiv venue counts n/a (see §0). **Verdict: open.** It
merges naturally with N3 (layer localization) and with novelty-options option 1 (the predictor's input).

## N11. Test-time adaptation of twin-trained policies at deployment

**RQ.** Can unsupervised test-time adaptation (normalization statistics, self-supervised auxiliary losses,
test-time training) close the twin-to-real gap during the first minutes of deployment, replacing part of the
real-data budget?

**Crowdedness.**

| Query | arXiv 23/24/25/26 | S2 23/24/25/26 |
|---|---|---|
| N11a `(abs:"test-time adaptation" OR abs:"test-time training") AND (abs:robot OR abs:"robot policy" OR abs:navigation OR abs:manipulation OR abs:"sim-to-real")` | n/a | 12 / 10 / 32 / 35 |

**Closest verified papers.**
1. *Fast-Slow Test-Time Adaptation for Online Vision-and-Language Navigation*, arXiv:2311.13209 (ICML 2024,
   arXiv comment).
2. *TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour*, arXiv:2602.02331 (2026).
3. *RoboTTT: Context Scaling for Robot Policies*, arXiv:2607.15275 (2026, NVIDIA GEAR per the project URL).

**Scores.** Dist 1. Fit 2. NoRobot 1 (TTA needs a deployment stream; proxy-real streams are weak evidence).
ML share: arXiv venue counts n/a (see §0). **Verdict: active.** NVIDIA-scale groups are entering this area
(RoboTTT).

---

## 12. Ranked shortlist and first-paper ideas

Ranking criterion: openness × fit × no-robot feasibility × ML-venue share, with distance ≤ 1 preferred so the
niche plugs into the current Stages I–II without changing the object of the IPB.

### Rank 1: N4, reconstruction-gap robustness of frozen encoders

- **Why.** Open (tight query ≤ 3 S2 papers/yr), the highest ML share found (83 %), and it needs only public
  scans and GPUs. It measures the component that every twin-trained visuomotor policy depends on.
- **First paper (CVPR 2027 or NeurIPS 2027 Datasets & Benchmarks).** *"Is your encoder twin-proof?"*
  (1) Build paired real/rendered frames: reconstruct scenes from public captures at 3–4 capture budgets and
  render at held-out real poses. (2) Score 8–10 frozen encoders (DINOv2, SigLIP, CLIP, VC-1, R3M-type,
  V-JEPA-type) by per-layer representation distance (CKA, linear-probe transfer, kNN retrieval of the real
  frame), broken down by artifact type. (3) Train frozen-encoder ImageNav/BC heads in the twin, evaluate on
  the proxy-real tier, and test whether the invariance score ranks encoders by transfer. A negative result
  ("invariance does not predict transfer") is also publishable as a benchmark finding.
- **Link to the IPB.** It replaces H2's generic "representation alignment" (crowded) with a measurable
  question, and the dataset feeds option 2 (twin fidelity) and option 1 (forecasting).

### Rank 2: N3 + N10, where the sim-to-real gap lives inside a policy

- **Why.** Interpretability of robot policies and VLAs is active and growing fast (N3a S2: 28 → 93), which
  shows the venues care. But the specific question (layer-wise localization of the twin-vs-real gap and
  representational convergence of twin- vs. real-trained policies) returned 0–1 papers (N10b). It is the
  closest match to the student's ACL 2025 method (probing hidden states, a GNN over layers).
- **First paper (ICLR 2028 or NeurIPS 2027).** *"Localizing the reality gap in visuomotor policies."* For
  navigation policies trained in twins (plus one open VLA on public paired sim/real frames): per-layer CKA
  and probe divergence on paired twin/real observations; activation patching of real-frame activations into
  twin rollouts (and the reverse) to find the layers whose patching restores proxy-real success; SAE features
  that fire only on reconstruction artifacts; a comparison with twin- vs. real-trained policies of the same
  architecture (N10). Deliverable: a layer-selection rule for where to put adapters or alignment losses
  (this makes N2 a cheap follow-up).
- **Risk.** The VLA-steering groups (arXiv:2509.00328, arXiv:2603.19183) could add a sim-vs-real section.
  Mitigation: the twin-specific paired-frame data and the navigation setting.

### Rank 3: N1, merging per-scene expert policies trained in twins

- **Why.** Robot-policy merging barely exists (S2 1 / 1 / 4 / 10). The two 2025–26 papers merge *skills*
  (MergeVLA) or protect generality after fine-tuning (arXiv:2512.08333). Merging across *scenes/twins* and
  interpolating along the *sim↔real* axis is unclaimed. Merging is a high-visibility ML topic, and the
  experiment reuses the policy zoo that option 1 already plans to build.
- **First paper (ICML 2028 or ICLR 2028).** *"Twin soups: merging scene-expert policies trained in
  reconstruction twins."* Train K per-scene experts from a shared initialization in K twins; compare
  uniform/TIES/task-arithmetic merges against joint multi-scene training at equal compute on unseen scenes
  (proxy-real tier, then a small Denali tier-C check). Add a sim↔real weight-interpolation curve for one
  scene with a small real fine-tune, and test whether linear mode connectivity between twin-trained and
  real-fine-tuned weights predicts transfer (a link to option 1).
- **Risk.** Merging RL policies can fail without a shared pretraining init. Mitigation: start from a shared
  pretrained encoder (the N4 winner) and merge only the heads/adapters.

### How the three fit together

N4 (which encoder), N3+N10 (where the gap lives inside the policy) and N1 (combining scene experts in weight
space) all use one asset: **a paired twin/real frame set plus a zoo of twin-trained policies**. This is the
asset novelty-synthesis.md already proposes for option 1. Adopting them does not change the IPB's object or
Stages I–II. It changes the ML claims of H2 and the paper plan (§11 of content), which remains a supervisor
decision.

## 13. Reproducibility

- Scripts and raw JSON are in the worker's scratchpad: `q.py`, `q2.py`, `niches.json`, `res_ax.json`,
  `res_s2.json`. The query strings in the tables above are verbatim (arXiv form; the Semantic Scholar form is
  derived as in §0).
- Venue queries: `ML = (co:NeurIPS OR co:ICLR OR co:ICML OR co:CVPR OR co:ICCV OR co:ECCV OR co:AAAI OR
  co:IJCAI)`, `RO = (co:CoRL OR co:RSS OR co:ICRA OR co:IROS OR co:"Robotics and Automation Letters" OR
  co:RA-L)`, each `AND (<niche query>) AND submittedDate:[202301010000 TO 202612312359]`.
- Relevance-sorted arXiv searches used to find the closest papers (2026-09-26):
  `abs:"vision-language-action" AND (abs:"mechanistic interpretability" OR abs:steering OR abs:"sparse
  autoencoder")`; `(abs:merging OR abs:"model merging" OR abs:"task arithmetic") AND (abs:"robot policy" OR
  abs:"robot policies" OR abs:"visuomotor" OR abs:"vision-language-action")`; `(abs:"world model" OR
  abs:"video generation") AND (abs:probing OR abs:"linear probe") AND (abs:physical OR abs:physics OR
  abs:depth)`; `(abs:"vision-language model" OR abs:VLM OR abs:LLM) AND (abs:"physical parameters" OR
  abs:"physical properties" OR abs:"material properties") AND (abs:"gaussian splatting" OR abs:"digital
  twin" OR abs:simulation) AND (abs:robot OR abs:video)`; `(abs:"scene graph" OR abs:"scene graphs") AND
  (abs:GNN OR abs:"graph neural network") AND (abs:navigation OR abs:manipulation)`; `(abs:"test-time
  adaptation" OR abs:"test-time training") AND (abs:"sim-to-real" OR abs:"robot policy" OR
  abs:navigation)`; `(abs:"gaussian splatting" OR abs:NeRF OR abs:"radiance field") AND abs:uncertainty AND
  (abs:policy OR abs:"reinforcement learning" OR abs:"imitation learning")`; `(abs:CKA OR
  abs:"representational similarity" OR abs:"representation similarity") AND (abs:"sim-to-real" OR abs:robot
  OR abs:"reinforcement learning")`; plus the sim-to-real × merging and sim-to-real × LoRA searches quoted in
  N1/N2.
- **Open items.** arXiv per-year and venue counts marked n/a (N5–N11) could not be retrieved because of
  arXiv HTTP 429/500 on 2026-09-26. Re-run `q2.py ax` when the API is free. Semantic Scholar counts are
  complete. Author lists are given only where the first author was checked. Otherwise the title and arXiv ID
  are the identifier.

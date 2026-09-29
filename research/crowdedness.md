# Crowdedness analysis per hypothesis H1–H4 (issue #16)

Compiled 2026-09-26 · owner: Wave7-N worker · scope: `content/07-questions-hypotheses.md` (RQ1–RQ4, H1–H4)
and `content/02-topic.md`. This file does not edit `content/`.

## TL;DR

| Hypothesis | What it claims | Verdict | One-line reason |
|---|---|---|---|
| **H1 / RQ1** twin from minutes of video → policy → real | (a) beats generic sim; (b) non-inferior to real-data-only at ≥ 10× budget | **(a) crowded, (b) open niche** | (a) is demonstrated by ≥ 5 groups since 2024 (EmbodiedSplat, Vid2Sim, VR-Robo, ReaDy-Go, GaussGym). (b) has no navigation paper with a matched-budget real-data baseline; the manipulation analogue (X-Sim: "matches BC with 10× less data collection time") exists. |
| **H4 / RQ2** budget–SR scaling curves, B_pipeline ≤ 0.1 · B_real | Twin pipeline reaches target SR at ≤ 10% of the real-data budget | **Open niche (navigation), active (manipulation)** | Nobody varies capture minutes; real-only data-scaling studies exist (Tsinghua ICLR 2025, Tampere RA-L 2026) and twin-based "scaling laws" exist for manipulation (CASHER, R2R2R, X-Sim). The curve with both axes for navigation is not published. |
| **H2 / RQ3** augmentation + representation alignment → uncaptured scenes and new task | Higher SR than twin alone and generic; lower feature distance | **Crowded (alignment), active (twin augmentation), open (cross-task pipeline study)** | Sim-to-real domain adaptation is a 10-year-old area (OpenAlex 31/53/71 papers in 2024/25/26); NeurIPS 2025 (Georgia Tech + NVIDIA) already does observation–action distribution alignment for sim-and-real co-training. Twin editing for generalization is demonstrated (RoboSplat, FalconGym 2.0, ReaDy-Go). Multi-task twin simulators (GS-Playground, DISCOVERSE, GaussGym, VLK) exist, but no controlled cross-task study of one pipeline. |
| **H3 / RQ4** SRCC of twin > generic sim, kept after refinement from real rollouts | Twin predicts real performance; correction does not hurt | **Active (hot in 2026 for manipulation/VLA), open niche for navigation twins** | SRCC-style papers: 0 → 3 → 10 per year (2024/25/26, OpenAlex). EmbodiedSplat reports SRCC 0.87–0.97 for its meshes but not vs. a generic simulator with CIs; twin calibration from real trajectories exists (QuadVerse 2026, LoopSR, SPI-Active) without SRCC before/after. |

**Bottom line for the student's concern.** The *infrastructure* layer (3DGS twins for robot learning) is crowded
and owned by large labs: OpenAlex counts 23 → 96 → 124 papers per year (2024/25/26) for "Gaussian splatting +
robot + simulator/twin", and at least 12 named open-source twin simulators exist (SplatGym, GaussGym, NavGSim,
GS-Playground, DISCOVERSE, FalconGym, RoboGSim, Vid2Sim, Re3Sim, SplatSim, EmbodiedSplat, ReaDy-Go).
The question "does a policy trained in a 3DGS twin transfer to the real scene?" (H1a) is answered. What is
**not** taken, and is defensible for a 4-year PhD with modest hardware: the **real-data budget** question
(H1b + H4, both axes: capture minutes and real rollouts, navigation, matched baselines) and the
**predictivity-after-correction** question (H3). These are open because they are careful measurement
studies, not because they need new ML. The ML-novelty risk sits in **H2 as phrased**: "representation
alignment to close the sim-real gap" is the most crowded part of the plan and a NeurIPS 2025 paper already
does it for sim-and-real policy co-training. Decision options are in §7.

## 1. Method and caveats

- **Sources.** OpenAlex (`api.openalex.org/works`, filter `title_and_abstract.search`, `group_by=publication_year`),
  arXiv API (`export.arxiv.org/api/query`, `abs:` fields, years binned by `<published>` date of each result),
  Semantic Scholar Graph API (`/paper/search/bulk`, boolean query over title + abstract, `year=` filter;
  `/paper/search/match` and `/paper/batch` for abstracts). All queries run on **2026-09-26**; 2026 is a
  partial year (through 26 Sep). Exact query strings are in §8.
- **Why three sources.** They disagree by a factor of 1.5–2 (OpenAlex counts the arXiv record and the venue
  record separately; Semantic Scholar de-duplicates; arXiv covers preprints only). Read trends, not absolute
  numbers. Where the arXiv count is far off (H3a: arXiv matches phrases loosely), OpenAlex/S2 are used.
- **Affiliations** were read from the author block of each paper's arXiv HTML page (`arxiv.org/html/<id>`) on
  2026-09-26, not inferred from author names. Venues and DOIs come from Semantic Scholar/OpenAlex records.
  Claims about what a paper demonstrates come from its abstract unless "full text" is stated (EmbodiedSplat
  and RialTo full texts were checked earlier for `content/06`, see the HTML comment there).
- **Limits.** OpenAlex's free daily budget for this IP was exhausted mid-session (HTTP 429, "Insufficient
  budget"), so OpenAlex institution breakdowns cover six queries only and OpenAlex candidate lists were taken
  before the cut-off. Semantic Scholar author-level affiliations are sparse and were not used. Citation counts
  are Semantic Scholar values on 2026-09-26.
- **Verdict scale.** *Crowded*: ≥ 50 papers/yr on the question or the exact claim already shown by ≥ 2 groups.
  *Active*: 10–50 papers/yr and partial demonstrations. *Open niche*: < 10 papers/yr and no demonstration of
  the exact claim.

## 2. Publication counts per year (2020–2026)

Query keys: H1a = neural reconstruction (NeRF/3DGS) + sim-to-real/real-to-sim + robot/policy; H1b =
"real-to-sim-to-real" as a named paradigm; H1c = NeRF/3DGS + navigation + policy learning; H4a = sim-to-real
or twin + real-data amount/budget/efficiency + robot; H4b = data scaling laws for robot policies; H2a =
sim-to-real + representation/feature alignment or domain adaptation + policy; H2b = NeRF/3DGS + augmentation
or editing + policy generalization; H2c = reconstruction twin + navigation + manipulation + sim-to-real;
H3a = sim-to-real predictivity / sim-real correlation of policy evaluation; H3b = correcting a simulator or
twin from real rollouts; S1 = SRCC-style "sim-vs-real correlation" by name; S3 = 3DGS + robot + simulator or
twin; S5 = reconstruction twin + real-data budget.

| Query | Source | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026* | Σ 2020–26 |
|---|---|---|---|---|---|---|---|---|---|
| H1a | OpenAlex | 0 | 0 | 1 | 2 | 13 | 46 | 39 | 101 |
| H1a | arXiv | 0 | 0 | 1 | 1 | 8 | 25 | 19 | 54 |
| H1a | Semantic Scholar | 0 | 0 | 2 | 2 | 10 | 33 | 26 | 73 |
| H1b | OpenAlex | 0 | 6 | 9 | 10 | 22 | 49 | 57 | 153 |
| H1b | arXiv | 0 | 4 | 4 | 2 | 13 | 30 | 28 | 81 |
| H1b | Semantic Scholar | 0 | 6 | 4 | 6 | 14 | 40 | 41 | 111 |
| H1c | OpenAlex | 0 | 0 | 1 | 1 | 12 | 19 | 23 | 56 |
| H1c | arXiv | 0 | 0 | 1 | 0 | 4 | 14 | 13 | 32 |
| H1c | Semantic Scholar | 0 | 0 | 1 | 1 | 8 | 15 | 15 | 40 |
| H4a | OpenAlex | 5 | 8 | 5 | 12 | 20 | 46 | 52 | 148 |
| H4a | arXiv | 4 | 3 | 5 | 4 | 10 | 19 | 23 | 68 |
| H4a | Semantic Scholar | 6 | 4 | 5 | 8 | 16 | 31 | 33 | 103 |
| H4b | OpenAlex | 0 | 0 | 1 | 1 | 11 | 15 | 51 | 79 |
| H4b | arXiv | 0 | 0 | 1 | 0 | 8 | 15 | 28 | 52 |
| H4b | Semantic Scholar | 1 | 0 | 1 | 1 | 10 | 17 | 35 | 65 |
| H2a | OpenAlex | 6 | 14 | 21 | 22 | 31 | 53 | 71 | 218 |
| H2a | arXiv | 6 | 5 | 8 | 8 | 19 | 25 | 26 | 97 |
| H2a | Semantic Scholar | 8 | 8 | 16 | 17 | 18 | 45 | 45 | 157 |
| H2b | OpenAlex | 0 | 0 | 3 | 1 | 2 | 7 | 6 | 19 |
| H2b | arXiv | 0 | 1 | 5 | 5 | 12 | 15 | 17 | 55 |
| H2b | Semantic Scholar | 0 | 0 | 2 | 0 | 2 | 6 | 8 | 18 |
| H2c | OpenAlex | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 6 |
| H2c | arXiv | 0 | 0 | 0 | 0 | 0 | 1 | 4 | 5 |
| H2c | Semantic Scholar | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 6 |
| H3a | OpenAlex | 3 | 11 | 8 | 9 | 23 | 39 | 85 | 178 |
| H3a | arXiv† | 28 | 27 | 36 | 47 | 87 | 170 | 224 | 619 |
| H3a | Semantic Scholar | 2 | 7 | 7 | 8 | 14 | 27 | 60 | 125 |
| H3b | OpenAlex | 0 | 0 | 0 | 2 | 1 | 2 | 2 | 7 |
| H3b | arXiv | 0 | 0 | 0 | 1 | 0 | 2 | 4 | 7 |
| H3b | Semantic Scholar | 0 | 0 | 0 | 1 | 1 | 1 | 2 | 5 |
| S1 (SRCC by name) | OpenAlex | 1 | 0 | 0 | 0 | 0 | 3 | 10 | 14 |
| S1 (SRCC by name) | Semantic Scholar | 0 | 0 | 0 | 0 | 0 | 1 | 6 | 7 |
| S3 (3DGS + robot + sim/twin) | OpenAlex | 0 | 0 | 0 | 1 | 23 | 96 | 124 | 244 |
| S3 (3DGS + robot + sim/twin) | Semantic Scholar | 0 | 0 | 0 | 1 | 22 | 71 | 90 | 184 |
| S5 (twin + real-data budget) | OpenAlex | 1 | 1 | 1 | 2 | 4 | 6 | 17 | 32 |
| S5 (twin + real-data budget) | Semantic Scholar | 1 | 0 | 0 | 1 | 2 | 5 | 5 | 14 |

\* 2026 through 26 Sep. † arXiv's `abs:` search matches multi-word phrases loosely, so H3a-arXiv is
inflated; use the other two rows.

**Reading.** Everything touching 3DGS twins for robots roughly doubled each year since 2024 (S3, H1a, H1c).
The specific sub-questions of this IPB stay small: twin + real-data budget (S5) is 4–17 papers/yr, twin
correction from real rollouts (H3b) is ≤ 4/yr, and one twin pipeline for navigation *and* manipulation
(H2c) is ≤ 5/yr. Sim-to-real domain adaptation (H2a) is the only line that is both large and old.

## 3. H1 / RQ1: twin from a short capture → policy → real

### 3.1 Closest papers (2024–2026)

| # | Paper | Year, venue | Group | Relation to H1 |
|---|---|---|---|---|
| 1 | EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device (Chhablani, Ye, Irshad, Kira) | ICCV 2025, doi:10.1109/ICCV51701.2025.02359, arXiv:2509.17430 | Georgia Tech + Toyota Research Institute | iPhone capture, GS → mesh in Habitat-Sim, fine-tunes ImageNav policies; +20 / +40 pp real SR over HM3D / HSSD zero-shot baselines; SRCC 0.87–0.97. Fixed capture (full text: ~1000 frames, 20–30 min), no real-data-only baseline. |
| 2 | VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion (Zhu, Mou, Li, Ye, Huang, Zhao) | RA-L 2025, doi:10.1109/LRA.2025.3575648, arXiv:2502.01536 | Tsinghua IIIS | 3DGS twin from multi-view images; RL for RGB-only goal tracking on a legged robot; "rapid adaptation … in complex new environments". |
| 3 | Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation (Xie, Liu, Peng, Wu, Zhou) | CVPR 2025, doi:10.1109/CVPR52734.2025.00155, arXiv:2501.06693 | UCLA (+ UIUC) | Monocular video → interactive urban twin; RL navigation; +31.2 % (twin) and +68.3 % (real) SR vs. prior simulation methods. 46 citations. |
| 4 | ReaDy-Go: Real-to-Sim Dynamic 3DGS Simulation for Environment-Specific Visual Navigation with Moving Obstacles (Yoo et al.) | RA-L 2026, doi:10.1109/LRA.2026.3707355, arXiv:2602.11575 | Seoul National University + KAIST | Static GS scene + animated human GS avatars; "environment-specific" navigation policies; zero-shot in one unseen environment. |
| 5 | GaussGym: An open-source real-to-sim framework for learning locomotion from pixels (Escontrela, Kerr, Allshire, Frey, Duan, Sferrazza, Abbeel) | arXiv:2510.15352, 2025 | UC Berkeley + ETH Zurich + Amazon FAR | 3DGS as a drop-in renderer in IsaacGym, > 100k steps/s; "thousands of environments from iPhone scans" and scene datasets (ARKit, GrandTour); sim-to-real navigation. 33 citations in < 1 yr. |
| 6 | SOUS VIDE (Low, Adang, Yu, Nagami, Schwager); GRaD-Nav (Chen et al.); SINGER (Adang, Low, Shorinwa, Schwager) | RA-L 2025 (arXiv:2412.16346); IROS 2025 (arXiv:2503.03984); arXiv:2509.18610 | Stanford (Schwager lab) | Three drone-navigation papers in 12 months on GS simulators (FiGS): zero-shot transfer, 105 hardware experiments, language-conditioned generalist policy. |
| 7 | FalconGym (Miao, Shen, Mitra); FalconGym 2.0 with Performance-Guided Refinement (Miao, Yuceel, Fainekos, Hoxha, Okamoto, Mitra) | IROS 2025 (arXiv:2503.02198); arXiv:2510.02248 | UIUC + Toyota Research Institute NA | NeRF/GS quadrotor tracks; editable GS; 98.6 % real gate success zero-shot. |
| 8 | Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks (Quach, Chahine, Amini, Hasani, Rus) | CoRL 2024, arXiv:2406.15149 | MIT CSAIL | GS simulator + imitation learning for quadrotor navigation, zero-shot. |
| 9 | NavGSim (Liu, Duan, Zhang, … He Wang) | arXiv:2603.15186, 2026 | Peking University + Galbot + BAAI | Hierarchical 3DGS for floor-scale navigation; VLA trained on NavGSim trajectories, evaluated sim and real. |
| 10 | GASE (Zhang et al.); NavArena (Wang et al.); Zero-Shot UAV Navigation in Forests via Relightable 3DGS (Lv et al.) | arXiv:2606.17520; arXiv:2609.04602; arXiv:2602.07101 (2026) | SJTU AutoLab + Renmin U.; (affiliation not in arXiv header); SJTU | Automated scene capture with panoramic arrays; automated navigation benchmarks from 3DGS (> 2,000 scenes, 22.2 M expert trajectories); relightable GS for outdoor RL. |
| 11 | SplatGym: Robotic Learning in your Backyard (Zhou, Sinavski, Polydoros) | IRC 2024, doi:10.1109/IRC63610.2024.00031, arXiv:2410.19564 | Cambridge + Lincoln + Wayve | Open-source GS simulator from a single video; RL navigation policies. |

Manipulation counterparts (same claim, other embodiment): SplatSim (CMU, ICRA 2025, arXiv:2409.10161; 86.25 %
real SR vs. 97.5 % for real-trained), RoboGSim (HIT Shenzhen + MEGVII, arXiv:2411.11839, "comparable to real
robot data"), Re3Sim (SJTU + Shanghai AI Lab, arXiv:2502.08645, > 58 % zero-shot), RL-GSBridge (SJTU,
arXiv:2409.20291), DISCOVERSE (Tsinghua AIR, IROS 2025, arXiv:2507.21981).

### 3.2 Is the exact claim already demonstrated?

- **H1(a) "twin-trained beats the generic baseline in SR".** Yes, in navigation, by several groups:
  EmbodiedSplat (vs. HM3D/HSSD-pretrained zero-shot), Vid2Sim (vs. prior simulation methods), ReaDy-Go
  (vs. baselines in target environments), VR-Robo. This is no longer a contribution on its own.
- **H1(b) "non-inferior to a real-data-only policy with ≥ 10× larger budget".** Not found for navigation.
  No navigation paper above trains a baseline on real robot experience of the target scene at a matched or
  larger budget (EmbodiedSplat full text confirms this; the others report zero-shot or generic baselines).
  In manipulation the analogous claims exist: X-Sim (Cornell, arXiv:2505.07096) "matches behavior cloning
  with 10× less data collection time"; Real2Render2Real (UC Berkeley + TRI, arXiv:2505.09601) "a single human
  demonstration can match … 150 human teleoperation demonstrations"; RialTo (MIT, RSS 2024) ablates 0–15 real
  demos. So the *number* 10× is already in print for manipulation; the navigation version, with a
  pre-registered non-inferiority margin, is open.

**Verdict H1: (a) crowded, (b) open niche.** Risk: the (b) gap is a natural next paper for the EmbodiedSplat,
GaussGym or ReaDy-Go groups; it could close within a year. The IPB's protection is the *design* (matched
budgets, non-inferiority margin, ≥ 10 scenes, three tiers), not the idea.

## 4. H4 / RQ2: budget–SR scaling curves

### 4.1 Closest papers (2024–2026)

| # | Paper | Year, venue | Group | Relation to H4 |
|---|---|---|---|---|
| 1 | Data Scaling Laws in Imitation Learning for Robotic Manipulation (Lin, Hu, Sheng, Wen, You, Gao) | ICLR 2025, arXiv:2410.18647 | Tsinghua + Shanghai Qi Zhi Institute + Shanghai AI Lab | Real-only scaling: 40k demos, 15k real rollouts; performance vs. number of environments, objects, demos. 210 citations. The template for "scaling curves" the committee will compare against. |
| 2 | Data Scaling for Navigation in Unknown Environments (Suomela, Takahata, Kuruppu Arachchige, Edelman, Kämäräinen) | RA-L 2026, doi:10.1109/LRA.2026.3677718, arXiv:2601.09444 | Tampere University | Real-only, 4,565 h across 161 locations; large data "approaching the performance of policies trained with environment-specific demonstrations"; diversity ≫ quantity; benefit from more data of an existing location "saturates with very little data". Directly relevant: it gives the real-only curve H4 needs, for sidewalk robots. |
| 3 | Robot Learning with Super-Linear Scaling / CASHER (Torne, Jain, Yuan, Macha, Ankile, Simeonov, Agrawal, Gupta) | arXiv:2412.01770, 2024 | MIT + Stanford + U. Washington | Crowd-sourced 3D-reconstruction twins, RL in sim bootstrapped by demos; "zero-shot and few-shot scaling laws on three real-world tasks"; fine-tuning to a target scenario "using a video scan without any additional human effort". Closest in spirit to H4 (manipulation). |
| 4 | Sim-and-Real Co-Training: A Simple Recipe (Maddukuri, Jiang, Chen, Nasiriany, … Goldberg, Mandlekar, Fan, Zhu) | RSS 2025, arXiv:2503.24361 | UT Austin + NVIDIA + UC Berkeley | Systematic study of sim/real mixture; sim data +38 % real SR on average. 65 citations. |
| 5 | Empirical Analysis of Sim-and-Real Cotraining of Diffusion Policies for Planar Pushing from Pixels (Wei, Agarwal, Chen, Bosworth, Pfaff, Tedrake) | IROS 2025, arXiv:2503.22634 | MIT | 50+ real policies, 250 sim policies: gains scale with sim data up to a plateau; more real data raises the ceiling; physical gap matters more than visual fidelity. This is a budget–performance study, for manipulation. |
| 6 | Real2Render2Real (Yu, Fu, Huang, El-Refai, Ambrus, Cheng, Irshad, Goldberg) | arXiv:2505.09601, 2025 | UC Berkeley + TRI | 1 human video ≈ 150 teleop demos (manipulation). 63 citations. |
| 7 | X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real (Dan, Kedia, Chao, Duan, Pace, Ma, Choudhury) | arXiv:2505.07096, 2025 | Cornell | Matches BC with 10× less data-collection time; online domain adaptation at deployment. |
| 8 | RialTo: Reconciling Reality through Simulation (Torne, Simeonov, Li, Chan, Chen, Gupta, Agrawal) | RSS 2024, arXiv:2403.03949 | MIT | Twin from "small amounts of real-world data"; appendix ablation over 0/5/10/15 real demos (full text). 208 citations. |
| 9 | A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation (Wang, Xu, Hu, Lin, Gao) | arXiv:2606.10366, 2026 | Tsinghua + Shanghai Qi Zhi Institute | Studies "how the amount of post-training data affects sim-and-real alignment". |
| 10 | ReBot (Fang, Yang, Zhu, … Ding) | IROS 2025, arXiv:2503.14526 | UNC Chapel Hill + RAI Institute | Real-to-sim-to-real video synthesis to scale VLA data. |

### 4.2 Is the exact claim already demonstrated?

No paper fits budget–SR curves for a reconstruction pipeline **and** a real-data-only baseline on the same
axis (minutes of target-domain data) for **navigation**. The pieces exist separately: real-only navigation
scaling (Tampere), real-only manipulation scaling (Tsinghua), twin-based scaling and "10×" or "150×"
data-efficiency claims (CASHER, X-Sim, R2R2R, manipulation), and sim/real mixture curves (MIT, UT
Austin/NVIDIA). Nobody varies the **capture** budget (minutes of video) as an experimental variable.

**Verdict H4: open niche for navigation, active for manipulation.** The Tampere result ("saturates with very
little data" from an existing location) is a warning: the real-only baseline may be strong at small budgets
for in-scene navigation, which makes H4's 10× ratio harder, not easier. The pilot should establish the
real-only curve first.

## 5. H2 / RQ3: augmentation + representation alignment, uncaptured scenes and cross-task

### 5.1 Closest papers (2024–2026)

| # | Paper | Year, venue | Group | Relation to H2 |
|---|---|---|---|---|
| 1 | Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training (Cheng, Ma, Chen, Mandlekar, Garrett, Xu) | NeurIPS 2025, arXiv:2509.18631 | Georgia Tech + NVIDIA | Learns a domain-invariant, task-relevant feature space by aligning joint observation–action distributions (optimal-transport loss); up to +30 % real SR; "generalize to scenarios seen only in simulation". This is H2's "representation alignment" claim, done, in manipulation. |
| 2 | Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation (Huang, Li, Wu, Zhou, …) | RA-L 2026, doi:10.1109/LRA.2026.3666383, arXiv:2512.17349 | Zhejiang University + Differential Robotics | 3DGS twin + adversarial domain adaptation "explicitly minimizing feature discrepancy"; zero-shot drone navigation under varying illumination. H2's twin + alignment recipe, for drones. |
| 3 | X-Sim (Cornell, see §4) | 2025 | Cornell | Online domain adaptation aligning real and simulated observations at deployment. |
| 4 | Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting (Tang, Pang, Sun, Ma, Chen, Huang, Lan) | arXiv:2512.04731, 2025 | (affiliation not in arXiv header) | Domain-invariant object-centric features from GS for sim-to-real manipulation. |
| 5 | RoboSplat: Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation (Yang, Yu, Zeng, Lv, Ren, …) | RSS 2025, arXiv:2504.13175 | Shanghai AI Lab + SJTU + CUHK | Edits 3D Gaussians for six generalization types (objects, appearance, embodiment, poses, lighting, viewpoints); one-shot 87.8 % vs. 57.2 % for hundreds of real demos + 2D augmentation. 79 citations. |
| 6 | FalconGym 2.0 + Performance-Guided Refinement (UIUC + TRI, see §3) | 2025 | UIUC + TRI | Editable GS tracks; generalizes to three unseen tracks with 100 % success. |
| 7 | ReaDy-Go (SNU + KAIST, see §3) | RA-L 2026 | SNU + KAIST | Human insertion into GS scenes; zero-shot in an unseen environment. |
| 8 | NeRF-Aug (Zhu, Levy, Gwilliam, Shrivastava) | arXiv:2411.02482, 2024 | U. Maryland | NeRF-based augmentation for unseen objects; +55.6 % over next best. |
| 9 | One Demo is Worth a Thousand Trajectories (Pan, Liang, Bauer, Cousineau, Burchfiel, …) | arXiv:2606.19586, 2026 | Stanford + Columbia + Toyota Research Institute | GS scene editing with unseen obstacles + trajectory optimization for augmentation. |
| 10 | **Cross-task pipelines:** GS-Playground (Jia et al., arXiv:2604.25459, 2026; Tsinghua-led, 40+ authors) "locomotion, navigation, and manipulation"; DISCOVERSE (Tsinghua AIR, IROS 2025); GaussGym (Berkeley); VLK (Wang, Li, Chen, Truong, … Abbeel, Kanazawa, Sferrazza, Shi; arXiv:2606.30645, 2026; Amazon FAR + UC Berkeley + Stanford + CMU) navigation + object transport on a Unitree G1 from 3DGS scenes; MolmoSpaces (Kim et al., arXiv:2602.11337, 2026; Allen Institute for AI + U. Washington + UCLA) navigation + manipulation, 230k synthetic scenes; RoboSnap (Shanghai AI Lab + SJTU + ZJU + Tsinghua, arXiv:2607.06699, 2026) one image → sim scene, DROID-Sim with 564 scenes; From Seeing to Simulating / Digital Cousins (Peking U. + Lightwheel, arXiv:2604.15805, 2026) panoramas → sim for manipulation and multi-room navigation. | 2025–2026 | see left | One reconstruction pipeline serving several tasks is now the *default product* of large-lab simulator papers. |

### 5.2 Is the exact claim already demonstrated?

- **Augmentation of twins → unseen scenes/objects → higher SR:** yes (RoboSplat, FalconGym 2.0, ReaDy-Go,
  NeRF-Aug), across drones, manipulation and one navigation case.
- **Representation alignment reduces the sim-real feature gap and raises real SR:** yes, for manipulation
  (Georgia Tech + NVIDIA, NeurIPS 2025) and drone navigation (Zhejiang, RA-L 2026). Adversarial and
  OT-based alignment for sim-to-real go back to Bousmalis et al. 2018 and DANN 2016 (already cited in §6).
- **Twin + augmentation + alignment, ablated against each other, for indoor navigation to uncaptured
  scenes, with a feature-distance metric on real frames (tier B):** not found as one study.
- **Same pipeline, unchanged, navigation → manipulation, with measured capture/compute cost:** not found as a
  controlled study; multi-task simulators exist (GS-Playground, DISCOVERSE, GaussGym, VLK) but report
  demos, not cost/fidelity comparisons across tasks.

**Verdict H2: crowded on the alignment mechanism, active on twin augmentation, open on the controlled
cross-task/pipeline-cost study.** As phrased in `content/07`, H2 reads as an application of known DA losses;
a reviewer from the representation-learning community will ask what is new beyond the NeurIPS 2025 paper.
This is the hypothesis with the highest novelty risk for an AI/ML PhD.

## 6. H3 / RQ4: predictivity (SRCC) and correction from real rollouts

### 6.1 Closest papers (2024–2026)

| # | Paper | Year, venue | Group | Relation to H3 |
|---|---|---|---|---|
| 1 | Evaluating Real-World Robot Manipulation Policies in Simulation / SIMPLER (Li, Hsu, Gu, Pertsch, …) | CoRL 2024, arXiv:2405.05941 | UC San Diego + Stanford + UC Berkeley + Google DeepMind | Paired sim-and-real evaluations; "strong correlation" without full-fidelity twins. 548 citations: this made "sim-real correlation" a mainstream metric for manipulation. |
| 2 | EmbodiedSplat (Georgia Tech + TRI, §3) | ICCV 2025 | Georgia Tech + TRI | SRCC 0.87–0.97 for GS-reconstructed meshes (navigation); compares reconstruction techniques, one real scene, 10 episodes (full text). Not vs. a generic simulator with CIs. |
| 3 | Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions (Zhang, Sha, Jiang, Loper, …, Li) | arXiv:2511.04665, 2025 | Columbia + SceniX + Google DeepMind | Soft-body twins from video, GS rendering; "simulated rollouts correlate strongly with real-world execution". 36 citations in < 1 yr. |
| 4 | A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation (Tsinghua, §4) | 2026 | Tsinghua + Shanghai Qi Zhi | Systematic study of ranking consistency and correlation across simulators, policies, perturbations; when simulator fine-tuning helps. |
| 5 | MolmoSpaces (AI2 + UW + UCLA, §5); RoboSnap (Shanghai AI Lab, §5); Digital Cousins (PKU, §5) | 2026 | see §5 | Each reports sim-to-real correlation (MolmoSpaces: R = 0.96, ρ = 0.98; the others "meaningful"/"strong"). SRCC-style reporting is becoming standard for simulator papers. |
| 6 | SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation (Zhu, Oh, Huang, Huang, Ma, Tang) | arXiv:2608.19425, 2026 | UCLA (+ SNU, USC, NC State) | Predicts scenario-conditioned real performance from limited paired sim-real samples plus large sim rollouts; corrects sim-to-real bias; conformal intervals. Quadruped + driving. The statistical version of RQ4. |
| 7 | Betting for Sim-to-Real Performance Evaluation (Mahboob, Chen, Weng) | arXiv:2604.24018, 2026 | Iowa State | Estimators for real performance from simulators under scarce real trials. |
| 8 | QuadVerse: Aligning Visual-Physical Reality for Quadruped Simulation (Chen, Wang, Zhang, Zhang, Liu, Jia, Wang, Zhou, Xie) | arXiv:2606.07118, 2026 | Nanjing U. + BUPT + DEXMAL + Tsinghua | 3DGS scenes as a "calibration substrate": friction priors refined by trajectory-based posterior search, residual dynamics from replayed real trajectories, then zero-shot visual navigation. This is H3's "correct the twin from real rollouts" mechanism (without SRCC before/after). |
| 9 | LoopSR (Wu, Xie, Cao, Lai, Zhang) | IROS 2025, arXiv:2409.17992 | SJTU | Real trajectories → latent → simulator parameters; continual adaptation of legged policies. |
| 10 | SPI-Active: Sampling-Based System Identification with Active Exploration (Sobanbabu, He, He, Yang, Shi) | arXiv:2505.14266, 2025 | CMU LeCAR + Google DeepMind | Sys-ID from real trajectories; +42–63 % over baselines (locomotion). |
| 11 | Real-is-Sim (Abou-Chakra, Sun, Rana, May, Schmeckpeper, Suenderhauf, Minniti, Herlant) | arXiv:2504.03597, 2025 | RAI Institute + QUT | Dynamic twin synchronized with the real world at 60 Hz; policies act in the twin. |
| Origin | Sim2Real Predictivity (Kadian, Truong, Gokaslan, Clegg, …) ; Rethinking Sim2Real (Truong et al.) | RA-L 2020, doi:10.1109/LRA.2020.3013848 (arXiv:1912.06321); CoRL 2022, arXiv:2207.10821 | Georgia Tech + Meta AI (Truong 2022 header; the Kadian 2020 arXiv header holds template placeholders, Semantic Scholar lists Georgia Tech) | SRCC defined on PointNav with a scanned lab; lower fidelity can transfer better. |

### 6.2 Is the exact claim already demonstrated?

- **"SRCC of the twin is higher than that of a generic simulator (CI excludes 0) over ≥ 10 policy
  variants":** not found. EmbodiedSplat reports SRCC for its meshes only; Kadian 2020 reports SRCC for
  Habitat with a scanned replica (9 models) but no twin-vs-generic contrast; the 2026 simulator papers report
  a single correlation each.
- **"Refinement from real rollouts does not reduce SRCC":** not found. QuadVerse, LoopSR and SPI-Active
  refine from real trajectories and report task performance, not predictivity before/after.

**Verdict H3: active (sim-real correlation is a 2026 growth topic, mostly manipulation/VLA), open niche for
the navigation-twin contrast and for predictivity after correction.** Note that SCAPE already frames
"predict real performance from few paired samples + many sim rollouts" as a statistics problem; H3 should
cite it and position SRCC + refinement as the twin-specific case.

## 7. Who owns the space, and what this means for the IPB

**Groups with ≥ 2 papers in the tables above (2024–2026):** Stanford (Schwager: SOUS VIDE, GRaD-Nav,
SINGER, Splat-Nav), UC Berkeley (Abbeel, Goldberg, Kerr: GaussGym, R2R2R, co-training), MIT (Agrawal,
Tedrake, Rus: RialTo, CASHER, co-training analysis, Liquid-GS drones), Georgia Tech (Kira, Xu: EmbodiedSplat,
OT co-training), NVIDIA (two co-training papers), Toyota Research Institute (EmbodiedSplat, R2R2R,
FalconGym 2.0, One-Demo), Tsinghua (IIIS, AIR: VR-Robo, DISCOVERSE, GS-Playground, sim-real recipe, data
scaling laws), Shanghai AI Lab + SJTU (Re3Sim, RoboSplat, RoboSnap, RL-GSBridge, LoopSR, ExoGS, relightable
UAV), Peking University (NavGSim, Digital Cousins), Columbia (Yunzhu Li: PhysTwin, soft-body evaluation),
Amazon FAR (GaussGym, VLK), UCLA (Vid2Sim, SCAPE), UIUC (FalconGym ×2), CMU (SplatSim, SPI-Active).
OpenAlex's institution breakdown for H1a in 2024–2026 (98 works, many arXiv records without parsed
institutions) puts CMU (6), Tsinghua (5), NUS, RAI Institute, Zhejiang and Stanford (3 each) on top.

**Answer to the student's question ("too crowded / too hard to be novel?").**

1. *Building the twin is not the thesis.* Twin simulators are a commodity produced by the labs above at a rate
   of ~100+ papers/yr; a PWr group cannot out-engineer GaussGym or GS-Playground. `content/09` already
   plans to reuse them; the IPB should say so more plainly and drop any implication that the pipeline itself is
   a contribution (§6's "twin-building protocol with measured cost and fidelity" is fine as a *protocol*, not
   as software).
2. *The budget question (H1b + H4) is genuinely open for navigation and cheap to defend.* It needs many
   scenes and careful statistics, not GPUs at scale. It is also the part most exposed to being scooped by the
   EmbodiedSplat / ReaDy-Go / GaussGym groups, so the pilot (Stage II) should be published early as a
   workshop/short paper to time-stamp the protocol (§11 already plans the first paper in sem. 3).
3. *H3 is a measurement study.* Keep it, but make it lean on SCAPE-style statistics (paired sim-real
   samples, bias correction) so that it reads as a methods contribution and not only as an SRCC table.
4. *H2 is where novelty is weakest and where the student's strengths are not used.* Options for the
   supervisor to decide (not applied here):
   - (i) Replace "generic representation alignment" by a claim the Representation Learning group can own:
     e.g. **predicting the transfer gap or real SR of a policy from its representations** (a link to the
     student's ACL 2025 SRW work on forecasting from hidden states; SCAPE and the Tsinghua "practical recipe"
     show demand for such predictors), which also strengthens H3.
   - (ii) Reframe H2 as a **learning-theoretic question about mixing reconstructed and real data** (mixture
     ratios, saturation, when real data raises the ceiling), extending the MIT and UT Austin/NVIDIA co-training
     analyses from manipulation to navigation and to the capture-budget axis; this merges naturally with H4.
   - (iii) Keep the cross-task (navigation → manipulation) part only as a *cost/fidelity* study of the unchanged
     pipeline, which no simulator paper reports, and drop the claim that alignment is new.
5. *The number "10×" is already in print for manipulation (X-Sim).* The navigation result stays publishable,
   but the abstract and §5 should not present the ratio as unprecedented.

## 8. Query strings (all run 2026-09-26)

OpenAlex: `GET https://api.openalex.org/works?filter=title_and_abstract.search:<Q>&group_by=publication_year`.
arXiv: `GET https://export.arxiv.org/api/query?search_query=<Q>&max_results=1000&sortBy=submittedDate`, years
binned by `<published>`. Semantic Scholar: `GET https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=<Q>&year=<Y>`.

| Key | OpenAlex `<Q>` | arXiv `<Q>` | Semantic Scholar `<Q>` |
|---|---|---|---|
| H1a | `("gaussian splatting" OR "neural radiance field" OR NeRF) AND ("sim-to-real" OR "real-to-sim" OR sim2real OR real2sim) AND (robot OR policy)` | `(abs:"gaussian splatting" OR abs:"neural radiance field" OR abs:NeRF) AND (abs:"sim-to-real" OR abs:"real-to-sim" OR abs:sim2real OR abs:real2sim) AND (abs:robot OR abs:policy)` | `("gaussian splatting" \| "neural radiance field" \| NeRF) + ("sim-to-real" \| "real-to-sim" \| sim2real \| real2sim) + (robot \| policy)` |
| H1b | `"real-to-sim-to-real" OR "real2sim2real"` | `abs:"real-to-sim-to-real" OR abs:real2sim2real` | `"real-to-sim-to-real" \| real2sim2real` |
| H1c | `("gaussian splatting" OR "neural radiance field" OR NeRF) AND navigation AND (policy OR "reinforcement learning" OR "imitation learning")` | same with `abs:` prefixes | same with `+`/`\|` |
| H4a | `("sim-to-real" OR "real-to-sim" OR sim2real OR "digital twin") AND ("real-world data" OR "real data") AND (budget OR "data-efficient" OR "data efficiency" OR "amount of" OR scaling) AND robot` | same with `abs:` | same with `+`/`\|` |
| H4b | `("scaling law" OR "scaling laws" OR "data scaling") AND (robot OR "robotic") AND (policy OR "imitation learning" OR "reinforcement learning")` | same with `abs:` | same with `+`/`\|` |
| H2a | `("sim-to-real" OR sim2real) AND ("representation alignment" OR "feature alignment" OR "domain adaptation" OR "contrastive") AND (navigation OR manipulation OR policy)` | same with `abs:` | same with `+`/`\|` |
| H2b | `("gaussian splatting" OR "neural radiance field" OR NeRF) AND (augmentation OR "object insertion" OR "scene editing" OR randomization) AND (robot OR policy) AND (generalization OR generalize OR "unseen")` | same with `abs:` | same with `+`/`\|` |
| H2c | `("gaussian splatting" OR "neural radiance field" OR NeRF OR "digital twin") AND navigation AND manipulation AND ("sim-to-real" OR "real-to-sim" OR sim2real OR real2sim)` | same with `abs:` | same with `+`/`\|` |
| H3a | `("sim-to-real" OR sim2real OR "real-to-sim" OR "sim-and-real") AND (predictivity OR "correlation coefficient" OR "correlates with real" OR "simulated evaluation" OR "correlation between simulated") AND robot AND (policy OR policies)` | `(abs:"sim-to-real" OR abs:sim2real OR abs:"real-to-sim") AND (abs:predictivity OR abs:"correlation coefficient" OR abs:"correlates with real" OR abs:"simulated evaluation" OR abs:"sim-and-real") AND abs:robot AND (abs:policy OR abs:policies)` | same as OpenAlex with `+`/`\|` |
| H3b | `("sim-to-real" OR "real-to-sim" OR "digital twin" OR simulator) AND ("real-world rollouts" OR "real rollouts" OR "real-world trajectories" OR "real trajectories") AND (calibrat OR "system identification" OR refine OR correct OR "close the gap") AND robot` | same with `abs:` (`calibration` instead of `calibrat`, no "close the gap") | same as arXiv with `+`/`\|` |
| S1 | `"sim-vs-real correlation" OR "sim2real correlation" OR "sim-to-real correlation" OR "sim-real correlation" OR ("SRCC" AND ("sim-to-real" OR sim2real OR "sim-vs-real" OR "real-world performance"))` | – | `"sim-vs-real correlation" \| "sim2real correlation" \| "sim-to-real correlation" \| "sim-real correlation" \| (SRCC + ("sim-to-real" \| sim2real \| "sim-vs-real"))` |
| S3 | `("gaussian splatting" OR "3DGS") AND (robot OR robotic OR "embodied") AND ("digital twin" OR simulator OR simulation OR "real-to-sim" OR real2sim)` | – | same with `+`/`\|` |
| S5 | `("gaussian splatting" OR "neural radiance field" OR NeRF OR "digital twin") AND (robot OR policy) AND ("real-world data" OR "real data" OR demonstrations) AND (budget OR "amount of" OR "number of demonstrations" OR "data efficiency" OR "data-efficient")` | – | same with `+`/`\|` |

Candidate papers were taken from the top-40 relevance-sorted OpenAlex results (2024–2026) of each query
(before the OpenAlex budget cut-off) and the citation-sorted Semantic Scholar bulk results for S1, H2b, H2c,
H3b and S5, then de-duplicated by hand; each paper's abstract was read via Semantic Scholar and its author
block via `arxiv.org/html/<id>`.

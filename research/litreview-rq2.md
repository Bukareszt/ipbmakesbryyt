# Literature review: RQ2 (sim-real invariant representations)

RQ2 (§7): *"How to learn representations that are invariant to the difference between simulation and reality?"*

## TL;DR
- **Too broad as written.** It covers five method families. Its core hypothesis, invariance on paired sim/real observations, is **already done** [6, 7, 8, 9]. The closest is OT co-training at NeurIPS 2025 [9].
- **Theory warns against it.** Invariant features are not sufficient under conditional shift [4]. IRM asks for an invariant *predictor*, not invariant features [3].
- **Open parts:** (a) how invariant representations are to *reconstruction-twin* artifacts, since PVR studies [11, 12] used only classical simulators or synthetic shifts; (b) **where inside the model** the twin-real gap arises. No verified paper localizes it. The closest are [12, 16, 17].
- **Recommendation:** make RQ2 a localize-then-intervene question (formulation A).

## Key works (verified by curl on 2026-09-26 with arXiv API, OpenAlex, Crossref and Semantic Scholar)

| # | Authors, year, title, venue | ID | Relevance to RQ2 |
|---|---|---|---|
| 1 | Ganin et al., 2016, *Domain-Adversarial Training of Neural Networks*, JMLR 17 | arXiv:1505.07818 | Standard adversarial feature invariance. A required baseline. |
| 2 | Hoffman et al., 2018, *CyCADA*, ICML (S2) | arXiv:1711.03213 | Pixel- and feature-level alignment: invariance at the input vs. at the features. |
| 3 | Arjovsky, Bottou, Gulrajani, Lopez-Paz, 2019, *Invariant Risk Minimization* | arXiv:1907.02893 | Invariant predictor across environments. Twin variants could serve as environments. |
| 4 | Zhao, Tachet des Combes, Zhang, Gordon, 2019, *On Learning Invariant Representation for Domain Adaptation* | arXiv:1901.09453 | Counterexample: invariant features plus low source error do not guarantee transfer. Limits H2. |
| 5 | Bousmalis et al., 2018, *Using Simulation and Domain Adaptation to Improve Efficiency of Deep Robotic Grasping* (GraspGAN), ICRA | doi:10.1109/ICRA.2018.8460875 | Pixel- and feature-level DA cuts the real grasping data needed. |
| 6 | James et al., 2019, *Sim-to-Real via Sim-to-Sim* (RCAN), CVPR | doi:10.1109/CVPR.2019.01291 | Maps randomized and real images to one canonical image: an invariant *input* space. |
| 7 | Truong, Chernova, Batra, 2021, *Bi-directional Domain Adaptation for Sim2Real Transfer of Embodied Navigation Agents*, RA-L | doi:10.1109/LRA.2021.3062303 | Navigation. The visual gap (handled real-to-sim) and the dynamics gap (sim-to-real) are separable. |
| 8 | Yoneda, Yang, Walter, Stadie, 2022, *Invariance Through Latent Alignment*, RSS | doi:10.15607/RSS.2022.XVIII.064 | Unpaired latent alignment at deployment. |
| 9 | Cheng, Ma, Chen, Mandlekar et al., 2025, *Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training*, NeurIPS | arXiv:2509.18631 | OT alignment of joint observation–action distributions beats marginal alignment (up to +30% real success). **Closest to H2.** |
| 10 | Nair et al., 2022, *R3M*, CoRL; Majumdar et al., 2023, *Where are we in the search for an Artificial Visual Cortex…* (VC-1) | arXiv:2203.12601; arXiv:2303.18240 | PVRs help, but none dominates across tasks. |
| 11 | Silwal et al., 2024, *What do we learn from a large-scale study of pre-trained visual representations in sim and real environments?*, ICRA | doi:10.1109/ICRA57147.2024.10610218 | PVR rankings in simulation predict real-world rankings. Classical simulators only. |
| 12 | Burns et al., 2023, *What Makes Pre-Trained Visual Representations Successful for Robust Manipulation?* | arXiv:2312.12444 | PVRs break under lighting and texture shifts. ViT emergent segmentation predicts OOD and real (ALOHA) success, a representation-level predictor. |
| 13 | Oquab et al., 2023, *DINOv2*, TMLR | arXiv:2304.07193 | Candidate frozen encoder. Robust on vision benchmarks, untested on twin/real shift. |
| 14 | Wu, Escontrela, Hafner, Goldberg, Abbeel, 2022, *DayDreamer*, CoRL (S2) | arXiv:2206.14176 | Latent world model learned on real robots. |
| 15 | Lai et al., 2025, *World Model-based Perception for Visual Legged Locomotion*, ICRA | doi:10.1109/ICRA55743.2025.11128762 | World model trained in sim is used zero-shot on a real robot. Its latent serves as the perception representation. |
| 16 | Kachaev et al., 2025, *Don't Blind Your VLA* | arXiv:2510.25616 | Probing: action fine-tuning degrades visual representations, and realigning them restores OOD generalization. Not about sim-vs-real. |
| 17 | Häon, Stocking, Chuang, Tomlin, 2025, *Mechanistic interpretability for steering VLA models*, CoRL | arXiv:2509.00328 | Tools for finding and steering directions in activations. Not applied to the sim-real gap. |

## Generality
**Too broad and partly ill-posed.**
1. It does not say which difference (appearance, geometry or dynamics, which [7] separates) or which part of the model.
2. Full invariance is the wrong target. [4] shows it can fail, and [9] shows that alignment must be conditioned on actions. A policy must *not* be invariant to real dynamics.
3. The paired-invariance hypothesis overlaps with [6, 8, 9], and the world-model part overlaps with [14, 15] and large-lab work (`research/world-models.md`).
4. "Where the gap arises" is the only clearly new clause.

**Proposed formulations:**
- **A (recommended):** *"Where inside a model trained in a digital twin does the twin-to-reality gap arise, and does enforcing task-relevant invariance at that location, using few paired twin/real observations, reduce the real-world generalization gap more than invariance at the input or the output?"* Baselines: [1, 2, 9].
- **B:** *"Which measurable properties of a representation (invariance on paired twin/real frames, emergent segmentation) predict how well policies trained on it in a digital twin transfer to reality?"* This extends [11, 12] to reconstruction twins.

## Is it open? Closest work
- **Invariance learning for sim-to-real:** not open. The closest is [9], then [6, 7, 8].
- **Encoder robustness to reconstruction-twin artifacts:** open. The closest are [11, 12]. `research/niches-models.md` N4 finds 0–2 papers per year on the tight query.
- **Localizing the sim-real gap inside a policy:** open. The closest are [16, 17, 12]. None found in repo scans (`niches-models.md` N3) or OpenAlex.

*Verification caveats:* the venues of [2] and [14] come from Semantic Scholar only. No venue is claimed for [4], [12], [16] or VC-1, because no API returned one. [9], [12] and [16] were checked on their arxiv.org abstract pages because the arXiv API was rate-limited.

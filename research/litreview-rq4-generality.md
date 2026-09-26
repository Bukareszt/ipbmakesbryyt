# Literature review: RQ4 (generalization across scenes and tasks) and overall generality

2026-09-26. Papers verified via arXiv API + Semantic Scholar; theses via OpenAlex/DataCite/repository pages.

## TL;DR
- RQ4 is well supported by the literature. The standard protocol is **held-out contexts** (Kirk et al.): train on one set of scenes or factors of variation, test on disjoint ones, and report the gap. Three things are established. Scene diversity drives generalization (ProcTHOR). Generalization difficulty differs by factor, and the ordering is the same in sim and real (Xie et al.; COLOSSEUM). **No single representation or method is best across navigation and manipulation** (Majumdar et al.).
- Transfer of sim-to-real *methods* across tasks is studied much less than transfer of *policies* across embodiments (OXE, CrossFormer).
- Generality: the topic is acceptable for an ICT PhD, but RQ1 and parts of RQ3 are phrased around "digital twin". I recommend **"generalization under the simulation-to-reality distribution shift"** as the unifying frame, with the digital twin as the source domain. The 4 RQs map cleanly onto data / representation / adaptation / evaluation.
- Comparable accepted theses (verified) use exactly this level of generality: Tobin (Berkeley 2019), Collins (QUT 2022), Y. Wang (CMU 2026), T. He (CMU 2026), W. Sun (CMU 2019).

## Part A: RQ4 key papers

| # | Paper | Venue | ID | What it gives RQ4 |
|---|---|---|---|---|
| 1 | Kirk, Zhang, Grefenstette, Rocktäschel (2023). A Survey of Zero-shot Generalisation in Deep RL | JAIR 76 | arXiv:2111.09794 | Formal train/test *context* split; taxonomy of generalization types. |
| 2 | Deitke et al. (2022). ProcTHOR: Large-Scale Embodied AI Using Procedural Generation | NeurIPS | arXiv:2206.06994 | Scaling the number of training houses gives SOTA zero-shot results on 6 benchmarks spanning navigation, rearrangement and arm manipulation. |
| 3 | Open X-Embodiment Collaboration (2024). Open X-Embodiment: Robotic Learning Datasets and RT-X Models | ICRA | arXiv:2310.08864, DOI 10.1109/ICRA57147.2024.10611477 | Cross-embodiment positive transfer from pooled data. |
| 4 | Doshi, Walke, Mees, Dasari, Levine (2024). Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation (CrossFormer) | CoRL | arXiv:2408.11812 | One set of weights controls nav + manip robots. |
| 5 | Majumdar et al. (2023). Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence? | NeurIPS | arXiv:2303.18240 | CortexBench, 17 tasks (nav, manip, locomotion): "none [of the PVRs] are universally dominant"; scaling data helps on average, not universally. **Direct evidence that nav → manip transfer of a result cannot be assumed.** |
| 6 | Burns et al. (2023). What Makes Pre-Trained Visual Representations Successful for Robust Manipulation? | CoRL | arXiv:2312.12444 | Manipulation-specific PVRs fail under lighting/texture/distractor shifts. Emergent segmentation predicts OOD success, including on a real robot. |
| 7 | Xie, Lee, Xiao, Finn (2024). Decomposing the Generalization Gap in Imitation Learning for Visual Robotic Manipulation | ICRA | arXiv:2307.03659, DOI 10.1109/ICRA57147.2024.10611331 | 11 factors of variation. The ordering of factor difficulty is consistent across sim and real. |
| 8 | Pumacay et al. (2024). THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation | RSS | arXiv:2402.08191 | 14 perturbation axes; SOTA success drops 30–50%. |
| 9 | Li et al. (2024). Evaluating Real-World Robot Manipulation Policies in Simulation (SIMPLER) | CoRL | arXiv:2405.05941 | Real-to-sim evaluation twins whose rankings track real ones. |
| 10 | Gervet, Chintala, Batra, Malik, Chaplot (2023). Navigating to Objects in the Real World | Science Robotics | arXiv:2212.00922, DOI 10.1126/scirobotics.adf6991 | End-to-end nav drops from 77% (sim) to 23% (real); modular reaches 90%. |
| 11 | Chen, Hu, Jin, Li, Wang (2022). Understanding Domain Randomization for Sim-to-real Transfer | ICLR | arXiv:2110.03239 | Bounds on the sim-to-real gap of DR (simulator = family of MDPs). |
| 12 | Garcia, Strudel, Chen, Arlaud, Laptev, Schmid (2023). Robust Visual Sim-to-Real Transfer for Robotic Manipulation | IROS | arXiv:2307.15320, DOI 10.1109/IROS55552.2023.10342471 | Systematic DR benchmark over many manip tasks. DR parameters tuned on an offline proxy task transfer to online policies, so a *method* setting carries across tasks. |

GNM/ViNT are already in §6 [20, 21].

**What is known about cross-task transfer of sim-to-real methods.**
1. Most evidence concerns transfer of *policies/models* (OXE, CrossFormer, GNM). Evidence on whether a *sim-to-real technique* (DR schedule, adaptation rule, data-selection rule) keeps its benefit when the task changes is thin: Garcia (within manipulation), ProcTHOR (same recipe, several tasks) and Chen (theory).
2. Representation results do not carry over automatically between nav and manip (Majumdar; Burns); per-factor difficulty orderings do carry over between sim and real (Xie).

So RQ4 has a clear, publishable gap: *does a method-level generalization gain keep its sign across tasks?*

**Suggested RQ4 protocol.** Kirk-style held-out scenes, per-factor gaps (Xie/COLOSSEUM axes), method and hyperparameters fixed across nav and manip.

## Part B: Generality

**Tied too much to twins or robotics?** Partly. RQ1 ("properties of a digital twin") and RQ3 ("correct... the twin itself") are twin-specific. RQ2 and RQ4 are already general. The twin should be the *instance*; the scientific object is the **shift between a simulator built from real data and reality**, which §6 already names (Ben-David). Make that the thread in §2/§7.

**Unifying framing.** Yes: "generalization under the simulation-to-reality distribution shift". The shift decomposes into three parts: source-domain construction (RQ1), invariant representation (RQ2) and target adaptation with few labels (RQ3). RQ4 is the out-of-distribution test. Each RQ attacks one term of the domain-adaptation bound, which makes this an ML thesis, not an engineering one.

**Coverage.** Data/simulation = RQ1, representation = RQ2, adaptation = RQ3, evaluation = RQ4. The coverage is coherent. Weakness: RQ4 is a "does it work" check; asking *which properties of the shift predict whether a gain transfers* makes it scientific.

**How comparable theses frame it (verified PhD theses):**
- J. Tobin, *Real-World Robotic Perception and Control Using Synthetic Data*, UC Berkeley, 2019, EECS-2019-104. https://escholarship.org/uc/item/2p62j4cm
- J. T. Collins, *Simulation to reality and back: A robot's guide to crossing the reality gap*, QUT (PhD by publication), 2022. https://doi.org/10.5204/thesis.eprints.230537
- Y. Wang, *Scaling Sim-to-Real Learning for Robot Manipulation*, Carnegie Mellon University, 2026. https://doi.org/10.1184/r1/32984711
- T. He, *Scalable Sim-to-Real Learning for General-Purpose Humanoid Skills*, Carnegie Mellon University, 2026. https://doi.org/10.1184/r1/32620404
- W. Sun, *Towards Generalization and Efficiency in Reinforcement Learning*, Carnegie Mellon University, 2019. https://doi.org/10.1184/r1/8397962.v1

These titles name the phenomenon (sim-to-real, reality gap, generalization), not a simulator technology. So "digital twin" belongs in the RQs as the instance, not in the title.

## Proposed refined topic

**EN:** Improving the generalization of deep learning models under the simulation-to-reality distribution shift in real-to-sim-to-real learning for physical AI.
**PL:** Poprawa generalizacji modeli głębokiego uczenia przy przesunięciu rozkładu między symulacją a rzeczywistością w uczeniu typu rzeczywistość–symulacja–rzeczywistość dla fizycznej sztucznej inteligencji.

(Alternative: keep the current title; it is already general enough.)

## Proposed refined RQs (same simple style)

1. **Which properties of a simulation built from real data determine how well models trained in it generalize to reality?** (data/source side; the digital twin is the instance)
2. **How can representations be learned that are invariant to the shift between simulation and reality, and where in the model does this shift cause the generalization gap?** (representation side)
3. **How can a model trained in simulation, together with the simulation itself, be adapted to reality using as little real data as possible?** (adaptation side)
4. **Do the improvements generalize to unseen environments and to other physical tasks, and which properties of the shift explain when they do?** (evaluation side; navigation → manipulation)

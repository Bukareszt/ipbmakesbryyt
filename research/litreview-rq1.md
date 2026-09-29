# Literature review: RQ1 (which twin properties determine generalization)

Verified 2026-09-26 via arXiv API, Semantic Scholar and OpenAlex (curl).

## TL;DR
- Fidelity vs. randomization is an old question. Randomization works, fidelity alone does not (Truong),
  and sim metrics can mislead (Kadian). No one has attributed transfer to properties of a *reconstructed* twin.
- Adaptive DR over **global physics parameters** is well studied (BayesSim, SimOpt, ADR, DORAEMON).
  **Region-level, uncertainty- and task-driven variation of appearance and geometry in 3DGS/NeRF twins is
  open.** The closest work is Phys2Real (uncertainty-aware physics only).
- RQ1 is sound but worded around one artefact. Reframed as "which components of the simulator–reality
  discrepancy govern generalization, and how should simulator uncertainty shape the training
  distribution", it is general ML with a theory anchor (Ben-David; Chen et al. 2022).

## Key papers
| # | Paper | Venue, ID | What it shows for RQ1 |
|---|---|---|---|
| 1 | Tobin et al. 2017, *Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World* | IROS 2017, arXiv:1703.06907 | Random textures are enough. Variability can replace appearance fidelity. |
| 2 | Peng et al. 2018, *Sim-to-Real Transfer of Robotic Control with Dynamics Randomization* | ICRA 2018, arXiv:1710.06537 | The same for physics. |
| 3 | Prakash et al. 2019, *Structured Domain Randomization* | ICRA 2019, arXiv:1810.10093 | Context-structured DR beats uniform DR. |
| 4 | Chebotar et al. 2019, *Closing the Sim-to-Real Loop* (SimOpt) | ICRA 2019, arXiv:1810.05687 | Fits the DR distribution to a few real rollouts. |
| 5 | Ramos, Possas, Fox 2019, *BayesSim* | RSS 2019, arXiv:1906.01728 | The DR distribution is the posterior over simulator parameters, so variation follows uncertainty. |
| 6 | Mehta et al. 2019, *Active Domain Randomization* | CoRL 2019, arXiv:1904.04762 | Samples the environments most informative for the policy. Not all regions of variation are equal. |
| 7 | OpenAI, Akkaya et al. 2019, *Solving Rubik's Cube with a Robot Hand* | arXiv:1910.07113 | Automatic DR: randomization ranges grow with task performance. |
| 8 | Kadian et al. 2020, *Sim2Real Predictivity* | IEEE RA-L 2020, arXiv:1912.06321 | Specific simulator artefacts (sliding) break sim–real correlation. |
| 9 | Chen et al. 2022, *Understanding Domain Randomization for Sim-to-real Transfer* | ICLR 2022, arXiv:2110.03239 | Theory: sim-to-real gap bounds for DR policies. |
| 10 | Truong et al. 2022, *Rethinking Sim2Real: Lower Fidelity Simulation Leads to Higher Sim2Real Transfer in Navigation* | CoRL 2022, arXiv:2207.10821 | Fidelity ablation: added physics fidelity does not help navigation. |
| 11 | García et al. 2023, *Robust Visual Sim-to-Real Transfer for Robotic Manipulation* | IROS 2023, doi:10.1109/IROS55552.2023.10342471 | Systematic benchmark of visual DR factors. |
| 12 | Tiboni, Klink, Peters et al. 2024, *Domain Randomization via Entropy Maximization* | ICLR 2024, arXiv:2311.01885 | Too much variation makes policies conservative, so the variation must be shaped. |
| 13 | Torne et al. 2024, *Reconciling Reality through Simulation* (RialTo) | RSS 2024, arXiv:2403.03949 | A scan-built twin improves real robustness. The twin is fixed. |
| 14 | Li et al. 2024, *Evaluating Real-World Robot Manipulation Policies in Simulation* (SIMPLER) | CoRL 2024, arXiv:2405.05941 | Visual and dynamics matching make sim track real. |
| 15 | Qureshi et al. 2025, *SplatSim* | ICRA 2025, doi:10.1109/ICRA55743.2025.11128339 | 3DGS rendering enables zero-shot RGB policy transfer. Appearance fidelity matters. |
| 16 | Chhablani et al. 2025, *EmbodiedSplat* | ICCV 2025, arXiv:2509.17430 | Phone-captured 3DGS twins for navigation. |
| 17 | Wang, Tian, Swann et al. 2025, *Phys2Real* | arXiv:2510.11689 | **Closest.** A 3DGS twin plus uncertainty-aware fusion of VLM priors over physics parameters. |

Also verified: DROPO (RAS 2023, arXiv:2201.08434); NeRF2Real (ICRA 2023, arXiv:2210.04932); Vid2Sim (CVPR 2025,
arXiv:2501.06693); LucidSim (CoRL 2024, arXiv:2411.00083); RoboSplat (arXiv:2504.13175).

## Generality
- **Not too broad.** It has one object (the training distribution of a real-data simulator) and one
  outcome (the generalization gap).
- **Slightly too narrow in wording.** "Digital twin" ties it to one artefact, and the hypothesis mixes a
  claim (errors are not equally harmful) with a method ("develop a method"). As written it risks reading
  as a 3DGS ablation study, which is engineering.
- **The ML core.** It is distribution shift from a *learned* source that carries its own uncertainty. That
  links it to DA bounds, DR theory (Chen) and Bayesian DR (BayesSim). The question applies to world models
  and generative simulators as well.

Proposed formulations:
1. *"Which components of the discrepancy between a simulator reconstructed from real data and reality
   govern the generalization of models trained in it, and how should the simulator's uncertainty and task
   relevance shape the training distribution?"*
2. (More theoretical) *"How should a learned simulator allocate fidelity and variability, as a function of
   its uncertainty and of the task, to minimise the real-world error of the trained model?"*. The hypothesis
   is that task-weighted, uncertainty-matched variation beats uniform randomization.

## Is it open?
**Partly open.** These parts are settled:
- fidelity is not sufficient (Truong, Kadian);
- structured and adaptive DR beats uniform DR (SDR, ADR, DORAEMON);
- DR can follow a parameter posterior (BayesSim, SimOpt).

These parts are open:
- (a) attributing the gap to *types* of twin error (appearance vs. geometry vs. lighting vs. physics),
  across tasks;
- (b) turning **per-region reconstruction uncertainty** plus **task relevance** into localized variation;
- (c) a theory-backed criterion linking the two.

Closest work:
- Phys2Real: physics only, adapted online.
- BayesSim and SimOpt: global dynamics parameters, non-reconstructed simulators.
- Active DR: task-driven, but ignores uncertainty.
- SIMPLER and García et al.: factor analyses, not of reconstruction error.

Novelty risk: 3DGS augmentation (RoboSplat, RoboGSim arXiv:2411.11839) is moving fast. Recheck before Stage II.

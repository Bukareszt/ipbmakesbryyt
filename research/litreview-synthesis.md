# Literature review v8: synthesis (2026-09-26)

Sources: litreview-rq1.md, litreview-rq2.md, litreview-rq3.md and litreview-rq4-generality.md. About 62
papers in total, each verified via arXiv, Semantic Scholar, OpenAlex or Crossref.

| RQ | Generality | What is already done | What is open |
|---|---|---|---|
| RQ1 twin properties | OK, but tied to the word "twin". Generalize it to "simulation built from real data". | Fidelity alone is not enough; structured or adaptive DR beats uniform DR (SimOpt, BayesSim, Active DR, ADR, DORAEMON). | Attributing the gap to types of twin error (appearance, geometry, lighting, physics); randomization local to regions, driven by reconstruction uncertainty and task relevance. Closest: Phys2Real (physics only). |
| RQ2 invariant representations | Too broad, and full invariance is ill-posed (Zhao 2019). | Invariance on paired sim/real observations (RCAN, ILA, BDA, Cheng NeurIPS 2025, +30%). | Where in the model the gap arises (probing); robustness of frozen encoders to twin reconstruction artifacts. |
| RQ3 adaptation with little real data | Too broad: the whole few-shot sim-to-real field already answers it. | Few-shot adaptation (RMA, co-training, TRANSIC); calibration (SimOpt, BayesSim, ASID). | Choosing real data by the *predicted* twin–reality discrepancy and correcting both twin and model. Must beat TwinRL (failure-driven selection). |
| RQ4 generalization across scenes and tasks | Already general. | Held-out scenes; scene diversity matters (ProcTHOR); no single representation wins across tasks (CortexBench). | Whether a sim-to-real method keeps its benefit when the task changes; which properties of the shift explain transfer. |

**Overall.** The topic is OK for an ICT PhD. Frame everything as "generalization under the simulation-to-reality
distribution shift", with the digital twin as one instance. The 4 RQs map to data, representation, adaptation
and evaluation. Comparable PhD theses (Tobin, Berkeley 2019; Collins, QUT 2022; CMU 2019 and 2026) name
sim-to-real or generalization in the title, never a technology.

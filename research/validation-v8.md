# Validation of the final IPB (v8), 2026-09-27: 4 independent critics

| Lens | Verdict |
|---|---|
| Scientific soundness | Makes sense. RQ1, RQ2 and RQ3 are sound with fixes. RQ4 is flawed as stated: it has no competing predictor, and two tasks is too few for a prediction. |
| Feasibility | Feasible only if descoped. As written, 4 RQs × 2 tasks × a robot × 5 papers is too much for 3 years. |
| Novelty | RQ3 and RQ4 are open. RQ1 and RQ2 are partially answered (Jin 2026 arXiv:2603.22876, Zhang 2025 arXiv:2511.04665, Qian 2026 arXiv:2608.29516, Lei 2026 arXiv:2604.13645). They stay novel only if narrowed. |
| Coherence | One coherent story, tighter than the references. It needs clearer wording, not a new structure. |

## Proposed fixes (no numeric thresholds)

1. **Scope.**
   - Navigation is the main task. Manipulation appears only in RQ4, in semester 6, as a confirmation test. It is sim-to-sim and must be labelled as such.
   - Plan 3 papers at 200-point conferences plus a journal paper; RQ4 is folded into the RQ3 paper or the journal paper.
   - One robot validation block (semesters 6–7, K29).
   - Semester 3: navigation pipeline only (Habitat + gsplat + COLMAP, no Isaac Sim).
2. **Proxy honesty.** Call the ScanNet++ reference a "reconstruction-fidelity gap". The robot is the primary evidence for actuation and sensor gaps. Proxy–robot agreement is a result, not a check.
3. **RQ1.**
   - Narrow it to reconstruction errors that vary across a scene.
   - Make the predictor explicit: the change in representation of a fixed reference model.
   - Replace components with the reference instead of injecting synthetic degradations.
   - State per-region randomization as its own claim.
   - Fallback if it fails: harm follows error magnitude.
4. **RQ2.** Localize by *task* decodability (where task information decodable in simulation stops being decodable from real inputs), not by sim/real separability. Lei 2026 shows probes can always separate the two domains. Cite Lei 2026.
5. **RQ3.** Make "correct both simulation and model from the same data" the central claim. Keep failure-driven selection (TwinRL) as the baseline. Count unlabelled real images in the budget.
6. **RQ4.** The prediction must beat simple predictors (gap size, image discrepancy). Test it across many held-out scenes; manipulation serves as confirmation.
7. **Theory.** The Ben-David bound is motivation only. Name the joint-error (λ) term: invariance cannot fix it, and that motivates correcting the simulation.
8. **§6.** Add Jin 2026, Qian 2026 and Lei 2026 (verified via the arXiv API by the critic). Soften the claims that "nobody looked".
9. **Wording.**
   - Define the terms once (digital twin, sim-to-real gap).
   - Gloss jargon for non-robotics readers (policy, closed-loop, probing).
   - Split the long RQ3 and RQ4 hypotheses.
   - Add one concrete example to §10 (e.g. a glass door or a reflection).

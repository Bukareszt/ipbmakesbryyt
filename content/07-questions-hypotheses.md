# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**Thesis.** A photorealistic, interactive simulation reconstructed from a few minutes of real-world capture
of the target environment lets learned mobile-robot navigation policies reach real-world performance not
worse than policies trained on real robot experience, while needing at least ten times less real-world data.

**Core and extensions.** The dissertation stands on **RQ1–RQ2 with H1 and H4** (the real-data-budget
study). RQ3/H2 (generalization) and RQ4/H3 (closed-loop correction, predictivity) are extensions.

**RQ1.** Can a simulation reconstructed from a short capture (minutes of RGB(-D) video) of a target
environment close the *visual* and *geometric* sim-to-real gap for learned navigation policies?
**RQ2.** How does deployed performance scale with the real-data budget, and what budget suffices compared
with training on real robot experience?
**RQ3.** How should reconstructed scenes be augmented (objects, lighting, sensor noise, dynamic obstacles)
so that policies generalize to environments that were *not* captured?
**RQ4.** Can a few real rollouts iteratively correct the simulation (appearance, dynamics), closing the
real-to-sim-to-real loop?

**Common protocol.** Real-robot evaluation uses fixed sets of 20 start–goal pairs × 3 trials per
environment (60 episodes per policy and environment). Primary metric: success rate (SR); secondary: SPL
and collision rate. *Real-data budget* B = minutes of real-world data collection (scene capture plus robot
rollouts). Tests are one-sided with α = 0.05, use bootstrap confidence intervals over start–goal pairs,
and are Holm-corrected within each hypothesis. Margins and targets below are fixed in the project
repository before the Stage II real-robot runs.

**H1 (RQ1, core).** A policy trained only in the reconstruction of the target environment
(a) reaches a higher real-world SR than the same policy trained in a generic simulator with domain
randomization (one-sided test), and (b) is **non-inferior** to a policy
trained on real robot data with a ≥ 10× larger budget, with margin δ = 10 pp (supported if the lower 95%
CI bound of SR_recon − SR_real is above −10 pp). Tested in ≥ 2 target environments.

**H2 (RQ3).** In uncaptured environments, reconstruction + targeted augmentation reaches a higher SR than
both reconstruction alone and generic domain randomization alone (supported if both one-sided
comparisons are significant after Holm correction).

**H3 (RQ4).** Evaluation in reconstructed environments predicts real-world performance better than a
generic simulator: over ≥ 10 policy variants, the Sim-vs-Real Correlation Coefficient (SRCC) is higher
(95% CI of the difference excludes 0), and it does not decrease after real-rollout refinement.

**H4 (RQ2, core).** The full pipeline, including refinement from a few real rollouts, reaches a target SR
τ with at least ten times less real data than real-data-only training: B_pipeline(τ) ≤ 0.1 · B_real(τ),
supported if the upper 95% CI bound of the budget ratio is ≤ 0.1. τ is the SR of the best real-data-only
baseline minus δ. Otherwise, the measured budget curve still answers RQ2.

<!-- Operationalization follows research/benchmarks.md edit 7 (measurable hypotheses, R5 p. 16–17; form
criterion 3) and edit 8 (core contribution marked, R5 p. 12–14). Numbering RQ1–RQ4 / H1–H4 is unchanged
because §3, §8, §9 and §12 refer to it. The protocol values (20×3 episodes, δ = 10 pp, ≥ 10 policy
variants, α = 0.05) are design choices, not results; TODO confirm with the supervisor and check power once
the Semester 2 baseline success rate is known. SRCC is from Kadian et al. [12] in §6. -->

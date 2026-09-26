# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**Thesis.** A photorealistic, interactive simulation reconstructed from a few minutes of real-world capture
of the target environment lets learned mobile-robot navigation policies reach real-world performance not
worse than policies trained on real robot experience, while needing at least ten times less real-world data.

**Core and extensions.** The dissertation stands on **RQ1–RQ2 with H1 and H4** (the real-data-budget
study). RQ3/H2 (generalization) and RQ4/H3 (closed-loop correction, predictivity) are extensions.

**RQ1.** Can a simulation reconstructed from minutes of RGB(-D) video of the target environment
(*real-to-sim*), with policies deployed back on the robot (*sim-to-real*), close the visual and geometric
gap for learned navigation?
**RQ2.** How does deployed performance scale with the real-data budget, and what budget suffices compared
with training on real robot experience?
**RQ3.** How should reconstructed scenes be augmented so that policies generalize to environments that
were *not* captured?
**RQ4.** Can a few real rollouts iteratively correct the simulation (appearance, dynamics)?

**Common protocol.** 20 fixed start–goal pairs × 3 trials per policy and environment (60 episodes).
Metrics: success rate (SR; primary), SPL, collisions. *Real-data budget* B = minutes of real data
collection (capture plus robot rollouts). The real-data-only baseline is a pretrained navigation model
fine-tuned by behaviour cloning on teleoperated trajectories of budget B; the generic-simulator baseline
uses a public scene dataset of the simulator chosen in T3.1. Tests are one-sided (α = 0.05) with bootstrap
confidence bounds over start–goal pairs and Holm correction within each hypothesis. All values are
pre-registered in the project repository; changes are logged with reasons.

**H1 (RQ1, core).** A policy trained only in the reconstruction of the target environment (a) reaches a
higher real-world SR than the same policy trained in a generic simulator with domain randomization, and
(b) is **non-inferior** to a policy trained on real robot data with a ≥ 10× larger budget: the lower 95%
confidence bound of SR_recon − SR_real, pooled over ≥ 2 environments (120 episodes per policy), is above
−15 pp. This gives ≈ 90% power at SR ≈ 0.8, rechecked after the pilot.

**H2 (RQ3).** In uncaptured environments, reconstruction + targeted augmentation reaches a higher SR than
both reconstruction alone and generic domain randomization alone.

**H3 (RQ4).** Over ≥ 10 policy variants, the Sim-vs-Real Correlation Coefficient (SRCC) of the
reconstructed simulation is higher than that of a generic simulator (95% CI of the difference excludes 0)
and does not drop after real-rollout refinement (lower 95% CI bound of the change ≥ −0.1).

**H4 (RQ2, core).** The full pipeline, including refinement from a few real rollouts, reaches a target SR
τ (best real-data-only SR minus 10 pp) with B_pipeline(τ) ≤ 0.1 · B_real(τ): the upper 95% CI bound of the
ratio is ≤ 0.1. If real-data-only training misses τ within the largest feasible budget B_max,
the ratio is reported as a bound. Otherwise the budget curve still answers RQ2.

<!-- Operationalization follows research/benchmarks.md edit 7 (measurable hypotheses, R5 p. 16–17; form
criterion 3) and edit 8 (core contribution marked, R5 p. 12–14). Numbering RQ1–RQ4 / H1–H4 is unchanged
because §3, §8, §9 and §12 refer to it. The protocol values (20×3 episodes, δ = 10 pp, ≥ 10 policy
variants, α = 0.05) are design choices, not results. SRCC is from Kadian et al. [11] in §6.
Issue #9 (research/review-1.md F8, F10, F21, F23), 2026-09-26:
- F8 power (normal approximation, both arms SR = 0.8, one-sided α = 0.05, ignores clustering on start–goal
  pairs): 60 episodes/arm at δ = 10 pp → power 0.39; 120 pooled at δ = 10 pp → 0.61; 120 pooled at
  δ = 15 pp → 0.90; δ = 10 pp would need ≈ 200 episodes/arm (not feasible on a borrowed robot, see F9).
  Chosen: pooled decision + δ = 15 pp. The τ for H4 keeps 10 pp so H4 is not weakened.
  CONFIRM (supervisor): δ = 15 pp is acceptable; recompute with the pilot SR and the observed clustering.
- F10: behaviour cloning / fine-tuning of a pretrained model (GNM/ViNT/NoMaD, §9) on teleoperated
  trajectories; on-robot RL is not realistic at these budgets. The generic scene dataset is not named
  because the simulator is chosen in T3.1.
- F23: "real-to-sim" / "sim-to-real" glossed in RQ1 so the §2 title term is defined here. -->

# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**Thesis.** How well embodied policies trained in neural-reconstruction digital twins transfer to the real
world can be **measured, localized and predicted from their internal representations**, and this lets a
limited real-data budget be spent where it matters. Navigation is the primary testbed; manipulation is the
cross-task test. RQ1–RQ2 (H1–H2) are the core of the dissertation; RQ3–RQ4 (H3–H4) build on them.

**Setting.** A *twin* is a 3D Gaussian Splatting reconstruction of a real scene built from a short capture;
the *capture budget* is the number of capture minutes (views). Evaluation tiers: **(A)** proxy reality on
public scene datasets with real captures and reference scans (≥ 10 scenes, some held out), which decides the
hypotheses; **(B)** public real-world datasets and published real evaluations with real outcomes;
**(C)** real-robot trials, validation only. A *policy zoo* (≥ 200 navigation policies varying scene, capture
budget, architecture and training data) supplies the population for RQ2–RQ4. Tests are one-sided,
α = 0.05, bootstrapped over scenes, Holm-corrected within each hypothesis and pre-registered in the
repository. All thresholds are design choices to be confirmed with the supervisor.

**RQ1 (measure and localize).** Where inside frozen encoders and twin-trained policies does the
twin-vs-real gap arise, and how does it depend on the capture budget?
**H1.** On paired real and twin-rendered frames of the same pose, the representation gap (1 − linear CKA,
and the drop of linear-probe accuracy) (a) is *concentrated*: the third of layers with the largest gap holds
≥ 50% of the summed gap in ≥ 80% of scenes; (b) decreases monotonically with the capture budget (trend test
over ≥ 4 budgets); (c) differs between ≥ 10 frozen encoders (Friedman test); and (d) the encoders'
robustness ranking predicts their downstream twin→real success rate (SR) with Spearman ρ ≥ 0.6.

**RQ2 (predict).** Can a twin-trained policy's real-world transfer and failures be forecast from its
internals (hidden states, weights) without real rollouts?
**H2.** (a) A predictor trained on the zoo (GNN over layers or weight-space metanetwork) predicts the
twin→real SR gap on held-out scenes with ≥ 20% lower mean absolute error than the best of three baselines
(twin SR alone, image fidelity PSNR/LPIPS, simulator-level predictivity); the lower 95% bound of the relative
reduction must be > 0. (b) Hidden-state failure monitors calibrated conformally in the twin at 90% coverage
keep coverage ≥ 85% on real data (ε = 5 pp).

**RQ3 (use).** Can these measures and forecasts allocate a limited real-data budget: which twin data to
weight, what to capture and which real rollouts to collect?
**H3.** Forecast-guided weighting, capture and rollout selection reaches the target real SR τ with ≥ 30%
less real data (capture minutes + real rollouts) than uniform or random allocation: B_guided(τ) ≤
0.7 · B_uniform(τ) on fitted budget–performance curves, with the upper 95% bound of the ratio < 1. τ is fixed
in the pre-registration as the SR that uniform allocation reaches at the largest budget.

**RQ4 (generalize).** Do the gap measures and predictors transfer across tasks and simulator families?
**H4.** (a) A predictor trained on the navigation zoo, applied to a manipulation zoo without retraining,
ranks policies by real outcome with Spearman ρ ≥ 0.5. (b) Its rank correlation with real outcomes exceeds
that of a generic simulator (Sim-vs-Real Correlation Coefficient, SRCC) and of a learned world-model
evaluator (95% CI of each paired difference excludes 0).

**Decision rule.** A hypothesis is supported when all its parts pass on tier A; tiers B and C report
agreement and are not used to tune thresholds.

<!-- Wave 9 (issue #22), 2026-09-26: rewritten after the pivot (research/pivot-decision.md is binding:
thesis, RQ1-RQ4 / H1-H4 numbering, thresholds rho >= 0.6, MAE -20%, epsilon = 5 pp, -30% real data,
rho >= 0.5, tiers A/B/C, "all thresholds are design choices"). Operationalizations added here (CONFIRM
supervisor; §9 must use the same wording):
- "Concentrated" (H1a): top third of layers >= 50% of the summed gap in >= 80% of scenes. "Monotonic" (H1b):
  one-sided trend test (e.g. Page / Jonckheere) over >= 4 capture budgets. "Differ" (H1c): Friedman test over
  scenes with >= 10 frozen encoders (e.g. DINOv2, SigLIP, CLIP, VC-1-type, R3M-type, V-JEPA-type;
  niches-models N4 suggests 8-10). Critical Spearman rho at one-sided alpha = 0.05 is about 0.64 for n = 8,
  0.60 for n = 9 and 0.56 for n = 10, so rho >= 0.6 is only meaningful with >= 10 encoders.
- Zoo size >= 200 is a design choice (novelty-options §3: "a few hundred to a few thousand small policies").
- H2 baselines follow pivot-decision.md; "simulator-level predictivity" = SRCC-style rollout estimate in the
  twin. Conformal level 90% is a design choice; epsilon = 5 pp is from pivot-decision.md. Real data for
  H2b = tier B (real datasets) and tier A proxy reality (niches-eval N5).
- H3 absorbs the former H1(b)/H4 budget curves (pivot-decision.md). "Real rollouts" on tier A = rollouts in
  the reference scan. The former -10 pp/-15 pp non-inferiority margins and the "twin beats generic" claim
  (crowded, novelty-synthesis.md) are dropped as hypotheses; twin-vs-generic can remain a sanity check in §9.
- H4 manipulation zoo: ManiSkill3 twins, SIMPLER paired sim/real evaluations as labels (novelty-options §3;
  exact checkpoints to be re-read from SIMPLER). World models only as a comparator (pivot scope).
- Core RQ1-RQ2 (P1 NeurIPS 2027, P2 ICLR/CVPR 2028) vs. RQ3-RQ4 (P3) follows the paper plan in
  pivot-decision.md; the core/extension label is our proposal for mid-term risk (CONFIRM supervisor). -->

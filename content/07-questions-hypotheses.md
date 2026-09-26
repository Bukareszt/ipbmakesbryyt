# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**Goal and thesis.** The goal is **a method** for learning in the real-to-sim-to-real loop that reaches a
given real-world performance with **significantly less real data** than existing approaches. It is one
pipeline of three components, one per loop step: (C1) task-aware, uncertainty-guided capture to build
the twin; (C2) uncertainty-aware learning of the policy or model in the imperfect twin; (C3) active
selection of a few real-world data to correct twin and model. The twin's uncertainty and the model's
representations guide all three. The thesis is H4; H1–H3 measure what each component saves at its own step
(ablations of the method). Testbeds (equal status): robotic manipulation and visual navigation.

**Tier A protocol (proxy reality).** In each testbed a **reference from a separate, higher-fidelity source
plays "reality"**, and the *twin* (neural reconstruction + system identification) is built from a
subset of a separate, cheaper capture, sharing no data. Navigation: ≥ 20 public indoor scenes (10
held out), laser-scan and DSLR reference, twin from the phone capture. Manipulation: a physics simulator
with held-out physical parameters and its own rendering (the weaker proxy; tier B, published paired
sim/real evaluations, checks it). Real data (capture = views and interaction samples for
the twin; trials and demonstrations = episodes in the reference) is summed in one operator-time cost.
P = task success rate in the reference. Tier A decides H1–H4; tiers B and C (real robot) report
agreement. Tests: one-sided, α = 0.05, scene/seed bootstrap, Holm correction, pre-registered.

**RQ1 (C1: capture less).** How little capture does a twin need? Can the task guide it?
**H1.** C1 (next data where task-relevant parts of the twin are most uncertain) reaches the P of uniform
capture with ≥ 40% less capture. *Decision:* on fitted capture–P curves, C_task(τ₁) ≤ 0.6 · C_uniform(τ₁),
and the upper 95% bound of C_task / C_recon (task-blind uncertainty selection) is < 1; τ₁ = P of uniform
capture at its largest budget.

**RQ2 (C2: learn in an imperfect twin).** How can learning be robust to the twin's errors?
**H2.** C2 (augmentation and sample weights from the twin's uncertainty and from the representation
distance to a few held-out real samples) improves transfer over uniform domain randomization at an equal
capture budget. *Decision:* mean paired P gain ≥ 10 pp on held-out scenes, lower 95% bound > 0, at each of
≥ 2 capture budgets.

**RQ3 (C3: few real data).** Which few real data close the gap, and how should they be used?
**H3.** C3 (real trials selected by predicted gap or uncertainty, used to correct twin and model) reaches
the target P with ≥ 50% fewer trials than random selection. *Decision:* N_active(τ₃) ≤ 0.5 · N_random(τ₃)
on fitted trial–P curves, upper 95% bound of the ratio < 1; τ₃ = P of random selection at its largest budget.

**RQ4 (the whole method).** How much real data does the method need versus real-only learning and
existing pipelines?
**H4 (thesis).** In each testbed, with C1–C3 and their hyperparameters unchanged, the method reaches the
target P with (a) ≤ 10% of the real data of real-only learning (imitation of demonstrations in the
reference, same encoder and initialization) and (b) ≥ 2× less real data than the strongest existing
pipeline (uniform capture, domain randomization, random real-data selection; RialTo-style). *Decision:*
(a) B_M(τ₄) ≤ 0.1 · B_real(τ₄), upper 95% bound of the ratio < 0.2; (b) B_M(τ₅) ≤ 0.5 · B_pipe(τ₅), upper
95% bound < 1; τ₄, τ₅ = P of each comparator at its largest budget; H1–H3 effects keep their sign and tier
B agrees in direction. Also reported: a world-model simulator.

A hypothesis holds when all its parts pass; a failed one is reported as a budget curve.

<!-- Wave 14 (issue #30), 2026-09-26: reframed after pivot decision v4 (research/pivot-decision.md, top;
overrides v3 on framing; v3 scope unchanged). The goal (cel pracy) is now ONE METHOD with components
C1-C3, one per loop step; the thesis = main hypothesis H4; H1-H3 = component ablations (what each
component saves at its own step). RQ/H numbering, all thresholds (40%, +10 pp, 50%, <= 10%, bounds < 1 /
> 0 / < 0.2), tier A/B/C protocol and review-3 fixes unchanged. New in v4: H4(b) >= 2x less real data than
the strongest existing real-to-sim-to-real pipeline = uniform capture + domain randomization + random
real-data selection, "RialTo-style" (v4 wording; RialTo = §6 [3]). The previous H4(b) ("holds in both
testbeds with the methods unchanged, H1-H3 effects keep their sign, tier B agrees") is kept as the "in
each testbed ... unchanged ... sign ... tier B" clause of the new H4. The former "uniform loop" comparator
of H4(a) became the H4(b) baseline. Operationalization of (b) as B_M(tau5) <= 0.5 * B_pipe(tau5) with the
upper 95% bound of the ratio < 1 mirrors H1/H3 (our proposal). (b) is new in v4: CONFIRM with the
supervisor (pivot-decision.md). "Tier A decides H1-H4" replaces "H1-H3": H4 was always decided on tier A
curves plus tier-B direction (§9 Stage IV). -->
<!-- (history) Wave 13 (issue #28), 2026-09-26: generalized after pivot decision v3 (research/pivot-decision.md,
top; overrides v2 on scope). Loop structure, RQ1-RQ4 / H1-H4 numbering and thresholds unchanged (40% less
capture, +10 pp, 50% fewer real trials, <= 10% of real-only data, bounds < 1 / > 0 / < 0.2). Changes:
- Domain-agnostic wording: "policy or model", "real-world data / interactions / trials" instead of "real
  rollouts", P = task success rate (SR) instead of navigation SR; manipulation and navigation equal status.
- Twin = appearance + geometry (neural reconstruction) and physical/dynamic parameters (system
  identification); capture counts views AND interaction samples used for identification (v3 "capture less
  covers both kinds of real data"). H1 comparator "reconstruction-only view selection" generalized to
  "task-blind uncertainty selection" (FisherRF-type for views, §9 gives the parameter-side analogue).
- Tier A keeps the review-3 non-circular pattern in each domain. Navigation: ScanNet++ laser scan + DSLR
  reference, twin from the iPhone stream (arXiv:2308.11417 abstract). Manipulation: coordinator decision
  2026-09-26 (orca ask, task_4385733a766f): a physics simulator (ManiSkill3, §6 [8]) with held-out
  ground-truth physical parameters and its own rendering as "reality", stated as the weaker proxy and
  backed by tier B (SIMPLER, §6 [35], published paired sim/real evaluations of real policies). Tier A
  decides H1-H3 in both testbeds; H4 needs tier A in both testbeds plus direction agreement with tier B.
- H4(b) was "manipulation ratio upper bound < 1"; now "H4(a) holds in both testbeds, methods and
  hyperparameters unchanged" (coordinator decision above; v3: "budget law holds across both domains").
- "Held-out scenes" in H2 = held-out scenes or task instances in each testbed (§9 defines them).
The dropped wave-9 phrase "to be confirmed with the supervisor" stays out of the visible text
(review-1 F5, review-2 R2-F1). -->
<!-- (history) Wave 11 (issue #25), 2026-09-26: rewritten after pivot decision v2 (research/pivot-decision.md is
binding: thesis sentence, RQ1-RQ4 / H1-H4 numbering and thresholds 40% less capture, +10 pp, 50% fewer
rollouts, <= 10% of real-only data; tiers A/B/C; world models only as a comparator; no benchmark). Removed
wave 9-10 content: representation-level thesis, layer-wise CKA/probing gap (old H1), policy zoo and
transfer forecasting / conformal monitors (old H2), SIMPLER-based H4 ranking. Operationalizations added
here (CONFIRM supervisor; §9, rewritten by another worker, must use the same wording):
- All targets tau are defined from the baseline's own curve at its largest budget, so the ratios are
  well-defined whatever absolute SR levels come out (same pattern as the wave 9-10 H3).
- H1: second comparator "reconstruction-only view selection" (FisherRF-type Fisher information,
  arXiv:2311.17874; GenNBV CVPR 2024) because active view selection itself is active (niches-data N1b
  11/17/33/35); beating uniform alone would not show that the *task* signal matters. Pivot v2 only fixes
  the uniform comparison (>= 40%); the recon-only margin (upper bound < 1) is our proposal.
- H2: "at each of >= 2 capture budgets" and "paired over held-out scenes" are design choices. A standard
  feature-alignment domain-adaptation baseline is reported in §9 but not in the decision (crowded,
  crowdedness.md H2a).
- H3: "real rollouts" on tier A = episodes in the reference. Correction = re-weighting / re-capture of the
  twin regions where rollouts fail plus policy fine-tuning (details in §9).
- H4(a): pivot fixes "at most 10%"; the extra "upper 95% bound < 0.2" guards against a lucky point estimate
  (our proposal). Real-only learning in proxy reality = RL/imitation directly in the reference. World model
  as simulator = comparator only, no training (pivot scope; research/world-models.md).
- H4(b): pivot says "carries over to manipulation with the pipeline unchanged"; operationalized as ratio
  upper bound < 1 plus same sign of H1-H3 effects. Manipulation proxy reality needs reconstructed tabletop
  scenes (e.g. ManiSkill3-based); tier B uses published paired sim/real results (SIMPLER) for agreement.
- Proxy-reality caveat: reference and twin share the reconstruction family, so the gap is smaller than in
  reality; tier B/C check the direction of the effects (research/niches-eval.md N5, novelty-options §3).
- The dropped wave-9 phrase "to be confirmed with the supervisor" stays out of the visible text
  (review-1 F5, review-2 R2-F1).
Review-3 (issue #27), 2026-09-26 (research/review-3.md): R3-F1 reference = ScanNet++ laser scan + DSLR
images, twin = 3DGS from the iPhone stream (arXiv:2308.11417 abstract: laser scan, "registered 33-megapixel
images from a DSLR camera, and RGB-D streams from an iPhone"), so the proxy gap is not a same-method
sparse-view artefact; R3-F10 >= 20 scenes, 10 held out; R3-F2 real-only baseline = imitation from
demonstrations in the reference (the data-efficient real-only recipe, not RL from scratch); R3-F4 H2 real
images held out from twin fitting and counted in the capture budget; R3-F7 H4(b) "allocation methods
unchanged" (the policy learner is task-specific). Thresholds and numbering unchanged. -->

# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**Thesis.** The real data needed in a real-to-sim-to-real loop can be reduced substantially by
**allocating it actively**: capture only what the policy needs to build the twin, train so that the policy
is robust to what the twin got wrong, and collect only the few real rollouts that close the remaining gap.
Reconstruction uncertainty and the policy's own representations guide all three steps. Testbeds:
navigation (primary), manipulation (cross-task).

**Tier A protocol (proxy reality).** On ≥ 20 public indoor scenes (e.g. ScanNet++; 10 held out from all
tuning), a **reference built from the laser scan and DSLR images plays "reality"**; a 3D Gaussian
Splatting *twin* built from a subset of the separate phone capture is the training simulator, so twin and
reference share neither images nor reconstruction method. Real data is counted exactly: capture = views
given to the twin, real rollouts and demonstrations = episodes in the reference, summed in one
operator-time cost at a fixed rate. SR = success rate in the reference. Tier A decides; tiers B (public
real-world data) and C (real robot) only report agreement. Tests are one-sided, α = 0.05, bootstrapped over
scenes and seeds, Holm-corrected within each hypothesis and pre-registered.

**RQ1 (real → sim: capture less).** How little capture does a twin good enough for policy learning need,
and can the task guide the capture?
**H1.** Task-aware, uncertainty-guided capture (next views chosen where task-relevant regions have high
reconstruction uncertainty) reaches the SR of uniform capture with ≥ 40% fewer views. *Decision:* on fitted
capture–SR curves, C_task(τ₁) ≤ 0.6 · C_uniform(τ₁), and the upper 95% bound of C_task / C_recon
(reconstruction-only view selection) is < 1; τ₁ = SR of uniform capture at its largest budget.

**RQ2 (in sim: train robustly on an imperfect twin).** How should a policy be trained to be robust to the
twin's reconstruction errors?
**H2.** Uncertainty-aware training (augmentation and sample weights from per-region reconstruction uncertainty
and from the representation distance to a few held-out capture images) improves real transfer over
uniform domain randomization at an equal capture budget. *Decision:* mean paired SR gain ≥ 10 pp on
held-out scenes, lower 95% bound > 0, at each of ≥ 2 capture budgets.

**RQ3 (sim → real: collect few real rollouts).** Which few real rollouts close the remaining gap, and how
should they correct the twin and the policy?
**H3.** Real rollouts selected actively (by predicted gap or uncertainty) and used for twin and policy
correction reach the target SR with ≥ 50% fewer rollouts than random selection. *Decision:*
N_active(τ₃) ≤ 0.5 · N_random(τ₃) on fitted rollout–SR curves, upper 95% bound of the ratio < 1; τ₃ = SR
of random selection at its largest budget.

**RQ4 (whole loop: budget and generalization).** What real-data budget does the full loop need
compared with real-only learning, and does it hold beyond navigation?
**H4.** (a) The full loop (H1–H3 combined) reaches the target SR with ≤ 10% of the real data needed by
real-only learning (imitation of demonstrations collected in the reference, same encoder and
initialization). *Decision:* B_loop(τ₄) ≤ 0.1 · B_real(τ₄), upper 95% bound of the ratio < 0.2; τ₄ = SR of real-only
learning at its largest budget. The curve is also reported for a uniform loop and for a world model
as the simulator. (b) With the three allocation methods and their hyperparameters unchanged, on
manipulation B_loop / B_real has an upper 95% bound < 1 and the H1–H3 effects keep their sign.

**Decision rule.** A hypothesis holds when all its parts pass on tier A; a failed one is reported as a
measured budget curve and does not block the next step, which has its own baseline.

<!-- Wave 11 (issue #25), 2026-09-26: rewritten after pivot decision v2 (research/pivot-decision.md is
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

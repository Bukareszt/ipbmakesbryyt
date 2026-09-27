# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

The research carried out in the proposed doctoral dissertation is aimed at studying the following research
questions, each on two physical AI tasks: robot navigation and robotic manipulation.

1. **Which reconstruction errors of a digital twin, varying across a scene, determine how well navigation
   and manipulation models trained in it generalize?**
   Domain adaptation theory, used here as motivation, bounds the real-world error of a model by its error in
   simulation, the discrepancy between the simulated and real distributions, and a joint error term. A
   digital twin of a room or a tabletop reproduces appearance, geometry and lighting only approximately,
   and its errors differ between regions of a scene.
   *Hypothesis:* The harm caused by a reconstruction error is predicted better by the change it induces in
   the representation of a fixed reference model on held-out paired views than by its magnitude in the
   image or geometry. Separately, randomizing each region in proportion to its reconstruction uncertainty and
   task relevance yields better generalization than uniform randomization.
   The research will replace components of the twin with a more accurate reference and measure the effect.
   If harm follows error magnitude, this attribution will itself be reported, and the third question will
   rely on reconstruction uncertainty and action sensitivity only.

2. **Where inside a model trained in simulation does the sim-to-real gap arise, and can aligning
   representations at that stage reduce it?**
   Models trained in simulation can rely on features absent in reality, such as reconstruction artifacts.
   Simulated and real inputs remain distinguishable even in models that transfer well, so the gap should be
   localized by what the model loses about the task, not by whether the domains can be told apart.
   *Hypothesis:* In both tasks, there is a first stage of the model at which task information that can be
   decoded from simulated inputs can no longer be decoded from real ones. Aligning simulated and real
   representations at that stage, from a few paired views, yields better generalization than aligning them
   at the input, at the final features or everywhere.
   The research will use probing of hidden states to find this stage before intervening.

3. **Which real data, chosen under a limited budget, most efficiently correct both the simulation and the
   model?**
   Real data are expensive, and existing methods use them to correct either the model or the simulation.
   However, the joint error term cannot be reduced by invariance, only by making the simulation closer to
   reality.
   *Hypothesis:* Correcting both the digital twin and the model from the same selected real data reduces the
   gap more than correcting either one alone. The data should be selected where the twin is predicted to
   disagree with reality in task-relevant ways. This disagreement can be estimated from the reconstruction
   uncertainty, the representation distance between simulated and real views, and the sensitivity of the
   predicted action. Such selection is expected to beat random and failure-driven selection.
   The research will compare selection rules at equal budgets in both tasks, counting unlabelled real images
   as real data.

4. **Do the improvements generalize to unseen environments and from one task to the other, and which
   properties of the shift explain when they do?**
   A valuable method should not be tied to a single scene or task. Therefore, the developed methods shall be
   applied with unchanged settings to many held-out scenes of both tasks, and an improvement found in one
   task shall be tested in the other.
   *Hypothesis:* The attribution of the gap from the first question and its localization from the second
   can be measured in a new scene or task before a method is applied. These measurements predict whether
   the improvement transfers, also between the tasks. They predict it better than simple indicators, such
   as the raw size of the gap or the image-level discrepancy.
   The research will test this prediction across many held-out scenes of navigation and manipulation.

<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §7: intro states both tasks for every RQ; RQ1 title names navigation and manipulation models, twin "of a room or a tabletop"; RQ2 hypothesis "in both tasks"; RQ3 comparison "in both tasks"; RQ4 = generalization to unseen environments AND from one task to the other (an improvement found in one task tested in the other), still against raw gap size and image-level discrepancy, across many held-out scenes of both tasks. Sim-to-sim confirmation wording removed. Structure, narrowing and hypotheses otherwise unchanged. -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §7 (fixes 3-7, 9): RQ1 narrowed to reconstruction errors varying across a scene; predictor = change in the representation of a fixed reference model on held-out paired views; components replaced with the reference; per-region randomization a separate claim; fallback (harm follows magnitude -> reported; RQ3 uses uncertainty and action sensitivity only). RQ2 = first stage where task information decodable in simulation is no longer decodable from real inputs (not domain separability, cf. Lei 2026, §6 [9]); compared with input, final features, everywhere. RQ3 central claim = correcting both from the same data; random and failure-driven selection as baselines; unlabelled real images count in the budget; hypothesis split. RQ4 must beat raw gap size and image-level discrepancy, many held-out scenes, manipulation = sim-to-sim confirmation; hypothesis split. Bound = motivation; joint-error term motivates RQ3. -->
<!-- Review-6 (2026-09-27): RQ1 "Domain adaptation theory"; RQ2 novelty scoped to models trained in simulations built from real data (surgical fine-tuning, §6 [20]), "a few", "yields better generalization", baseline "final features", probing provenance kept only in §8; RQ3 title = correct both simulation and model; circularity removed (cheap unlabelled real observations vs. expensive interaction data); RQ4 manipulation = controlled second task. -->
<!-- Wave 20 (ultracode): final core. Judge synthesis of 3 independent drafts (A theory: RQs = terms of the
Ben-David et al. 2010 bound; B robot-loop: real->sim, learning in sim, sim->real, generalization; C
supervisor-fit: representation-centric, K46). Base = C (representation-centric, probing fits the student's
background); grafted from A: the domain-adaptation-bound opening of RQ1 and "which components of the
discrepancy", the "early features to action output" localization in RQ2, "dominant component" in RQ4;
from B: "as a function of the budget" in RQ3 and "with unchanged settings" in RQ4. Order = data/simulation,
representation, adaptation, evaluation. No numbers, budgets, pre-registration, VoI or model names.
Openness per research/litreview-rq1..rq4: RQ1 closest Phys2Real (physics only) vs BayesSim/SimOpt/DORAEMON
(global physics params); RQ2 invariance itself not open (DANN, RCAN, Cheng et al. 2025), open = localizing
the sim-real gap by probing (Kachaev et al. 2025 not about sim vs real), Zhao et al. 2019 motivates
task-relevant invariance; RQ3 precedents AADA (Su et al. 2020), ASID (Memmel et al. 2024), TwinRL (Xu et
al. 2026, failure-driven, manipulation only) - novelty = predicted discrepancy + joint correction + budget
comparison, navigation; RQ4 Majumdar et al. 2023, Kirk et al. 2023, Xie et al. 2024, Chen et al. 2022. -->
<!-- Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top)
and the deep-research report (reports/Uczenie nawigacji w cyfrowych bliźniakach.md). Goal = v7 goal
(reduce real data; three mechanisms = H1-H3; H4 = thesis); navigation decides H1-H4, manipulation =
generalization test with no separate thresholds (v7 "Scope"). Applied recommendations: one unit (operator
minutes), shared budget grid, target as a fraction of the baseline's plateau, pre-registered baselines, H2
difficulty regime (baseline <= ~75% success), H3 decided vs random at >= 50% and vs the failure-driven
(TwinRL-style) rule only as "fewer" (= upper bound of the ratio < 1 in §9), the SRCC precondition for H3,
H4 baseline assembled and pre-registered with the same budget. The world model is an ablation of step 2
(v6/v7), so it is no longer inside the H2 sentence as a required part. Thresholds kept: 40%, +10 pp, 50%,
2x (H4 new in v4, CONFIRM with the supervisor). The details (bounds, alpha, counts, episodes per arm,
SRCC threshold) are in §9. -->
<!-- (history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
general description, navigation only, pipeline real -> twin -> navigation models -> real; "formulate them
simply (one or two sentences each). Keep one clear quantitative threshold per hypothesis; move the details
(tests, alpha, counts) to §9, briefly." RQ1-RQ4 / H1-H4 numbering and the mapping to stages 1-3 + whole
pipeline kept. Thresholds kept: H1 >= 40% less capture, H2 >= 10 pp (the H2(a) threshold), H3 >= 50% fewer
trials, H4 >= 2x less than the strongest existing real-to-sim-to-real approach (the H4(b) threshold; new in
v4, CONFIRM with the supervisor). Removed from the visible text per v6: H2(b) as a separate part (twin +
world model vs twin only is now an ablation in §9, no threshold), H4(b) TwinRL/VLA detail (now "existing
real-to-sim-to-real approaches" in general terms), model names, manipulation testbed, tier B (SIMPLER was
manipulation-only). H4(a) "<= 10% of real-only data" dropped as a threshold (v6 allows one per hypothesis
and the goal compares with existing approaches); real-only learning stays as a reported reference curve
(§9). Fallback if the supervisor prefers the real-only thesis: H4 "at most 10% of the real data of
learning from real data only" (the v2-v5 H4(a) threshold). Operationalizations (targets tau from each
comparator's own curve at its largest budget, upper/lower 95% bounds, one-sided alpha = 0.05, Holm,
scene bootstrap, >= 20 scenes / 10 held out, >= 2 budgets for H2, second-reference sign check) moved to
§9 unchanged in substance. -->
<!-- (history) Wave 15 (issue #31), 2026-09-26: rewritten after pivot decision v5 (research/pivot-decision.md, top;
overrides v4 on method content; goal, thesis, v3 scope unchanged). RQ/H numbering, all thresholds (40%,
+10 pp, 50%, <= 10%, >= 2x, bounds < 1 / > 0 / < 0.2), tier A/B/C protocol and review-3 fixes unchanged.
Changes:
- Method = pretrained open VLA (v5 examples OpenVLA arXiv:2406.09246, "7B-parameter", "can be fine-tuned
  on consumer GPUs via modern low-rank adaptation methods"; Octo arXiv:2405.12213; pi0 arXiv:2410.24164;
  HF openvla/openvla-7b MIT licence, lerobot/pi0_base) fine-tuned sim-first in the twin with RL + imitation
  and LoRA. Navigation checkpoint to be fixed in the Stage IV pre-registration: NaVILA arXiv:2412.04453 is
  a navigation VLA with checkpoints on HuggingFace (a8cheng/navila-llama3-8b-8f, checked 2026-09-26);
  suitability for point/image-goal navigation UNVERIFIED.
- C1 now names the VLM (task-relevant objects/regions from instruction and scene), C2 names LoRA-style
  fine-tuning and the twin-grounded world model, C3 names twin + WM + VLA uncertainty (v5 wording).
- H2(b) NEW (v5: "twin + world model" beats "twin only" at an equal real-data budget). No pp threshold
  given in v5; "lower 95% bound of the paired gain > 0 at each of >= 2 budgets" is our proposal, CONFIRM
  with the supervisor. "At an equal real-data budget" = same capture budget, since the WM is trained on
  twin data only (no extra real data).
- H4(a) real-only = fine-tuning the same VLA on real demonstrations only (same checkpoint, same LoRA
  setup). This is the data-efficient real-only recipe (keeps R3-F2: not RL from scratch).
- H4(b) baseline (v5: "verify which"). Verified candidates (arXiv abstracts, 2026-09-26):
  TwinRL arXiv:2602.09023 (Feb 2026): "reconstructs a high-fidelity digital twin from smartphone-captured
  scenes", "efficient parallel RL in the digital twin", "identifies failure-prone yet informative
  configurations, enabling targeted human-in-the-loop rollouts"; RialTo (§6); RL fine-tuning of VLAs in
  simulation: VLA-RL arXiv:2505.18719, SimpleVLA-RL arXiv:2509.09674, RL4VLA arXiv:2505.19789. Hence the
  baseline = uniform capture + DR + RL fine-tuning in the twin + random or failure-driven real trials
  (TwinRL/RialTo-style); the exact recipe is fixed in the Stage IV pre-registration. SIMPLER
  (arXiv:2405.05941) is an evaluation twin (tier B), not a fine-tuning pipeline.
- NOVELTY GUARDRAIL (v5): RL fine-tuning of VLAs in sim and world-model VLA training are crowded (also
  VLA-RFT arXiv:2510.00406, World-Env arXiv:2509.24948, WMPO arXiv:2511.09515: world models as simulators
  for VLA RL). Nothing in §7 claims either as new. TwinRL's failure-driven targeting of real rollouts is
  the closest work to C3: C3 differs by selecting under a counted real-data budget and by correcting twin
  and WM as well as the VLA. Flagged for §6 (issue #32).
- "Also reported: a world-model simulator" removed from H4: the WM is now part of the method (H2(b)).
- To stay within 1 page: "next data where ... most uncertain" in H1 moved into the C1 summary; "used to
  correct twin and model" in H3 is in the C3 summary. -->
<!-- (history) Wave 14 (issue #30), 2026-09-26: reframed after pivot decision v4 (research/pivot-decision.md, top;
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

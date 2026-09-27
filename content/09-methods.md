# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The research will follow the methods commonly adopted in machine learning and robot learning projects. Since
no established theory guarantees generalization from simulation to reality, the dominant part of the work
will be empirical. Domain adaptation theory, which relates the error of a model in reality to its error in
simulation and to the discrepancy between the two, will serve as motivation, and the properties of the
proposed methods will be analysed theoretically whenever possible.

The methods will be examined on two physical AI tasks, robot navigation and robotic manipulation, which share
the reconstruction tools. Digital twins will be built from real images with neural scene reconstruction, e.g.,
3D Gaussian Splatting, and coupled with simulators for navigation (e.g., Habitat) and manipulation (e.g.,
ManiSkill3), in which models mapping camera images to actions will be trained or fine-tuned, where possible
starting from pretrained models.

Since the research does not rely on an own robot, the evaluation will use public data. For navigation, public
datasets of real indoor scenes with independent captures of the same scenes (e.g., ScanNet++) will be used:
the twin will be built from one capture, and the other will provide real frames and a dataset-based reference
simulation. This reference measures the gap caused by reconstruction fidelity, not differences in actuation
and sensors. For manipulation, twins of real tabletop scenes will be built from images of public robot
datasets, following the visual matching of SIMPLER [14], and compared with published real-robot results of
the same policies; new models will additionally be evaluated in simulations whose parameters are hidden from
the learner.

For the first research question, variants of the twin in which one type of reconstruction error is corrected
will be examined to attribute the gap to types of error, and randomization guided by reconstruction
uncertainty and task relevance will be studied. For the second question, simple probes on the hidden states
of models will be used to examine at which stage task information decodable in simulation is lost on real
inputs, and alignment at that stage will be compared with alternatives. For the third question, ways of
selecting a small amount of real data used to correct both the twin and the model will be examined. For the
fourth question, the methods will be applied to held-out scenes of both tasks, and it will be examined whether
the measured attribution and localization predict the improvement better than simple predictors.

The evaluation will rely on standard metrics, such as success rate, and on the sim-to-real gap, measured on
held-out scenes in both tasks and complemented where possible by open-loop measures on real frames. Methods
will be compared with relevant baselines under comparable training effort and real data. Statistical methods
will be used to provide reliable outcomes, including repeated runs over seeds and scenes and statistical tests
for comparisons, and ablation studies will determine the contribution of individual components. Data for
training, model selection and final evaluation will be kept separate. If access allows, selected results will
be validated on a real robot in cooperation with a robotics laboratory of the university.

Experiments will be implemented mainly in Python with PyTorch, with source code managed in Git, and run on GPU
clusters of the Department, WCSS and PLGrid. Code and data will be released whenever licences allow,
following open science standards. The findings will be published at leading conferences from the ministerial
list, such as NeurIPS, ICML, ICLR, CVPR and RSS, and presented at smaller venues such as MLinPL.

<!-- Wave 23: trimmed to reference length (2026-09-27, student decision: avoid over-promising; register of the accepted Binkowski and ipb4 §9, ~370-450 words). Visible §9 cut from ~1275 to ~600 words: general empirical ML methodology with theory where possible; twins from real data with neural reconstruction in navigation and manipulation simulators (Habitat, ManiSkill3 as e.g. only); evaluation without an own robot (navigation: independent captures of public datasets, dataset-based reference = reconstruction-fidelity gap; manipulation: SIMPLER-style twins of real tabletop scenes vs published real-robot results [14]); one sentence per RQ; metrics, statistics, ablations; real-robot validation only "if access allows" (semester and robot type dropped); tools, compute, open code; dissemination. Removed: per-RQ baselines and citations [4], [5], [6], [9], [13], real-data units, SPL, BridgeData V2 / Open X-Embodiment / MuSHRoom names, phone captures, uncertainty-estimation detail, rank correlation, the "numbers in brackets" note. -->
<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §9: task-agnostic methods on two equal tasks sharing reconstruction tools; navigation pipeline (Habitat, ScanNet++/MuSHRoom proxy = reconstruction-fidelity gap) kept; new manipulation pipeline: twins from real frames of public robot datasets (BridgeData V2, Open X-Embodiment; described only as far as their arXiv abstracts, verified today: 2308.12952, 2310.08864) and own phone captures, SIMPLER visual matching [14], published paired real results of the same policies (Google Robot and WidowX/BridgeData V2 setups, checked in arXiv:2405.05941) as the real reference; honest limitation: published results cover only released policies, so new models are also evaluated closed-loop in a hidden-parameter simulator (e.g. ManiSkill3, arXiv:2410.00425 verified), which also serves controlled physics studies. RQ1 reference per task; RQ2 task variables per task; RQ3 interaction unit per task; RQ4 across held-out scenes of both tasks and between tasks; gap levels per task; validation on the mobile robot and optionally an arm (sem. 6-7). Trimmed for the 2-page limit: metrics/statistics, tooling and dissemination paragraphs merged; per-Gaussian randomization detail removed. TwinRL citation [22] -> [13]. -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §9 (fixes 1-7): bound = motivation; navigation pipeline only (Habitat); manipulation only in the RQ4 paragraph as a sim-to-sim confirmation in ManiSkill3 with hidden visual/physical parameters; reference simulation measures the reconstruction-fidelity gap, robot = main evidence for actuation/sensor differences, proxy-robot agreement reported as a result; open-loop and closed-loop glossed; RQ1 component replacement, reference-model predictor, fallback, per-region randomization as a separate claim; RQ2 task-decodability probes (task variables), alignment compared with input, final features [6], all layers, full fine-tuning; RQ3 budget counts unlabelled images, same data corrects twin and model, baselines random and failure-driven [22], model-only/twin-only; ASID removed from §9 (manipulation no longer in RQ3); RQ4 vs raw gap size and image-level discrepancy; robot validation one block sem. 6-7. Citations renumbered to the new §6 list ([4], [5], [6], [9], [22]). Trims for the 2-page limit: cooperation-with-PhD-students sentence, representation-similarity sentence, promotion sentence shortened, tooling/compute sentences merged. -->
<!-- Final check (2026-09-27): added the note that bracketed numbers in §9 refer to the §6 reference list; Kachaev et al. AAMAS 2026 venue verified on OpenAlex (doi:10.65109/pper9186). -->
<!-- Review-6 (2026-09-27): two evaluation levels (dataset proxy: open-loop on real frames + reference simulation from the independent higher-fidelity capture; closed-loop on the real mobile robot), gap defined per level; per-region reconstruction uncertainty (view coverage, ensemble disagreement); RQ3 procedure (budget = interaction data, selection scores, dual correction, comparisons at equal real data); manipulation = controlled proxy (hidden visual and physical parameters), no real-arm promise; wording fixes; international dissemination and foreign co-authorship. -->
<!--
Wave 20 (ultracode), 2026-09-27: visible §9 rewritten from scratch in the register of the Binkowski (2022) §9;
aligned with the final RQ1-RQ4 (controlled simulation variants, probing, budget curves, held-out scenes,
second task); no thresholds, no model names, no citations in §9.
-->

<!--
Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top) and
the deep-research report (reports/Uczenie nawigacji w cyfrowych bliźniakach.md, "Rekomendacje" and the
per-hypothesis table). Applied here:
- One unit (operator minutes B = capture + demonstrations + on-robot trials with resets) and the shared
  budget grid {5, 10, 20, 40, 80} min; target P = fraction of the baseline's plateau (e.g. 90% of its P at
  the largest budget); bootstrap CI of the budget ratio by scene.
- Pre-registered baselines per hypothesis: H1 uniform / FisherRF-type task-blind [23] / risk- or
  semantics-weighted with a reconstruction objective [25, 26] (+ ASID-type task-blind identification [20]
  for the physical part); H2 uniform DR [6, 7] / no DR / ablations; H3 random / uniform coverage /
  TwinRL-style failure-driven rule (SR(s0) < tau, [18]); H4 assembled baseline = EmbodiedSplat-style
  capture + fine-tuning [12] + RialTo/TwinRL-style real correction [16, 18], same budget, + zero-shot +
  real-only reference curve.
- H2 difficulty regime (baseline <= ~75%), 150-300 episodes per arm (report: "detekcja +10 pp przy bazie
  ~60% (alpha = 0,05 jednostronnie, moc 80%) wymaga rzędu 150-300 epizodów na ramię"); world model = ablation.
- H3: >= 50% decided vs random; vs the failure-driven rule only upper bound < 1; precondition = SRCC
  twin-vs-proxy above a pre-registered threshold; honest note that selection rules save 20-40% (report;
  SureSim [33] 20-25%).
- H4: >= 30-50 episodes per point (report table).
- Tools: Habitat-Sim/Lab + gsplat + COLMAP 4.x (report: Isaac Sim does not support A100/H100, so it is
  excluded; the visible text says "run on the data-centre GPUs of WCSS and PLGrid" instead of naming
  Isaac). gsplat and COLMAP are software, not cited as references.
- Datasets: ScanNet++ [21] (licence signed by the supervisor; no derived twins published) + MuSHRoom [22]
  (CC-BY-4.0, releasable; ~10 rooms per the report).
- Robot: TurtleBot 4 Lite (~1.7k EUR, SzD Minigrant) or K29 robots; SRCC proxy-vs-robot in 2 PWr rooms.
- Scope: static indoor scenes (dynamic people = future work, §12).
- Manipulation = generalization test: ManiSkill3 [2] with hidden physics as "reality" (Wave 13 protocol,
  coordinator decision task_4385733a766f) + SIMPLER [5] published paired sim/real results; no thresholds.
- Compute: the report's estimate (160-320 3DGS fits <= ~300 GPU-h; policy fine-tuning 10^3-10^4 GPU-h) is
  OUR ESTIMATE, kept out of the visible text; "measured in the pilot" instead.
- Kept from v6/review-4: separate captures (R3-F1), second reference sign check, >= 20 scenes / 10 held
  out (R3-F10), pilot-set difficulty (R3-F6), planner-path relevance (R3-F9), walking-tour time (R3-F5),
  held-out real samples counted (R3-F4), re-capture counted (R3-F12), real-only = imitation (R3-F2), RL on
  a subset of scenes (R4-F9), hidden physical parameters of "reality" (R4-F2), the assembled baseline with
  equal effort (R4-F3), image-goal and point-goal tasks (R4-F5; instruction-following dropped for space).
- "one task-weighted information criterion covers both views and physical parameters" = the report's
  methodological suggestion (FisherRF + ASID/SPI-Active in one task-weighted criterion; "such a
  combination was not found in any source"). Design choice, CONFIRM with the supervisor.
- H1 unit: operator minutes now (v7 one unit); frames also reported (was "views", R4-F6).
Refs follow the Wave 18 §6 list: [1] Habitat, [2] ManiSkill3, [4] Kadian (SRCC), [5] SIMPLER, [6] Tobin,
[7] Peng, [8] Chebotar, [10] Maddukuri, [11] 3DGS, [12] EmbodiedSplat, [16] RialTo, [18] TwinRL,
[19] BayesSim, [20] ASID, [21] ScanNet++, [22] MuSHRoom, [23] FisherRF, [24] Bayes' Rays, [25] Liu et al.
risk-aware, [26] AREA3D, [27] GNM, [28] ViNT, [29] OpenVLA, [30] NWM, [31] Cosmos, [33] SureSim,
[34] DINOv2, [35] PPI. Reference numbers in the older comments below are pre-Wave-18.
-->
<!--
(history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
"methods per stage, method families only, brief evaluation protocol"; "§9 may give at most 'e.g.'
examples of method families"; navigation only. Stages renamed I-IV -> 1-3 + whole pipeline (v6 numbering).
Kept from v5/review-3: the non-circular proxy reality (R3-F1: laser-scan + DSLR reference vs twin from the
separate phone capture; second-reference sign check; proxy error reported), >= 20 scenes / 10 held out
(R3-F10), minimum path length from a pilot (R3-F6), planner-path task relevance (R3-F9), capture from the
recorded pool + walking-tour time (R3-F5), held-out real samples counted (R3-F4), re-capture counted
(R3-F12), real-only = imitation of real demonstrations with the same initialization (R3-F2), robot = 2
validation campaigns, ~8 h each. Removed per v6: model and checkpoint names (OpenVLA-OFT, pi0, NaVILA as
the chosen model, Qwen2.5-VL, Cosmos-Predict2, NWM as chosen checkpoints), LoRA/SFT/PPO recipe details,
the ~23k H100-hour estimate (it was specific to 7B VLAs; research/vla-wm-crowdedness.md §4 keeps it),
manipulation tier A (ManiSkill3) and tier B (SIMPLER), TwinRL as the named H4 baseline (now "existing
real-to-sim-to-real approach, e.g. [14, 27]"). Physical part for navigation (traversable surfaces,
collisions, actuation noise) = design choice, CONFIRM supervisor. "Instruction-following" navigation added
next to image-goal because foundation-model initialization may be language-conditioned (design choice).
Refs follow the Wave 16 §6 list: [1] Habitat, [5] Tobin, [6] Peng, [7] Chebotar, [9] Maddukuri,
[10] 3DGS, [11] EmbodiedSplat, [14] RialTo, [15] BayesSim, [16] ScanNet++, [17] FisherRF, [18] Bayes' Rays,
[19] Liu et al. risk-aware, [20] AREA3D, [21] GNM, [22] ViNT, [23] OpenVLA, [24] NaVILA, [25] NWM,
[26] Cosmos, [27] TwinRL, [29] DINOv2, [30] PPI. Reference numbers in the older comments below are
pre-Wave-16.
-->
<!--
Wave 15-U (issue #32), 2026-09-26: pivot decision v5 (research/pivot-decision.md, top): a pretrained open VLA
fine-tuned sim-first in the twin, a VLM for task-aware capture and success judging, a world model grounded in
the twin. v3 scope, v4 framing, tiers A/B/C, all review-3 fixes and the §7 decision rules (worker T, final
§7 v5; coordinator msg_65a79c659e58) are mirrored: H2(b) twin + world model vs twin only (lower 95% bound of
the paired gain > 0, >= 2 budgets); H4(a) real-only = fine-tuning the SAME VLA on real data only (LoRA SFT
on expert demonstrations in the reference; real-only RL shown); H4(b) = strongest existing twin fine-tuning
pipeline for VLAs, TwinRL/RialTo-style (uniform capture, domain randomization, RL in the twin, random or
failure-driven real trials). The "world-model simulator also reported" comparator of Wave 14 is now part
of the method (C2) and of H2(b).
Models (research/vla-wm-crowdedness.md §2; all checked 2026-09-26):
- OpenVLA-OFT: code github.com/moojink/openvla-oft MIT; OpenVLA weights HF openvla/openvla-7b (MIT tag), but
  the openvla README says the models are "derived from Llama-2" and "subject to the Llama Community License".
- pi0 / pi0.5: github.com/Physical-Intelligence/openpi, Apache-2.0; README: LoRA fine-tuning "> 22.5 GB",
  full "> 70 GB" (A100 80GB / H100).
- OpenVLA LoRA: openvla README: "a single A100 GPU with 80 GB VRAM ... at least ~27 GB of memory";
  batch 16 "requires ~72 GB GPU memory".
- NaVILA: code github.com/AnjieCheng/NaVILA Apache-2.0; HF a8cheng/navila-llama3-8b-8f has NO licence tag
  (§12 licence risk). Mapping of its mid-level language actions to Habitat actions = design choice
  (CONFIRM in the T3.1 pilot). Tasks "instruction and image-goal navigation" replace point-goal (the VLA
  is language-conditioned); image-goal is kept from R3-F6.
- Qwen2.5-VL-7B-Instruct: HF, Apache-2.0.
- Cosmos-Predict2 checkpoints: HF nvidia/Cosmos-Predict2-2B-Video2World, NVIDIA Open Model License (gated
  "auto"). NWM: HF facebook/nwm, CC-BY-4.0, gated (manual).
- PPO as the RL algorithm: [16] "We identify PPO as a more effective RL algorithm for VLAs than
  LLM-derived methods like DPO and GRPO". RL tooling [15] SimpleVLA-RL (MIT); RLinf (Apache-2.0, ships a
  3DGS ManiSkill "GSEnv" for Real2Sim2Real per its README).
- TwinRL code: github.com/zhourui9813/TwinRL, MIT, "offline training code" (Octo/SERL-based, README).
Compute: "one 8-GPU node" = SimpleVLA-RL README example (8x A800 80GB). ~23k H100-hours = OUR ESTIMATE
(research/vla-wm-crowdedness.md §4: 96 LoRA SFT runs x 8 GPU-h, 48 RL runs x 192 GPU-h, 8 WM adaptations
x 384 GPU-h, ~60 Stage III-IV runs x 128 GPU-h, +10%); UNVERIFIED until the T3.1 pilot. WCSS Lem = 76 nodes
x 4 H100 96 GB, 7-day queue (research/resources.md §2).
Design choices (CONFIRM supervisor): the VLM's grounding as an extra task-relevance term in C1 (next to
planner-path visitation, R3-F9); world-model rollouts started from states in the twin's most uncertain
regions and weighted by that uncertainty (C2b); gap score in C3 = twin uncertainty + twin-WM disagreement +
LoRA-ensemble action spread; the H4(b) pipeline reports the better of random and failure-driven trial
selection; AREA3D-type VLM-guided reconstruction selection as an extra H1 comparator (not in the H1
decision rule).
Dropped with the §6 reference cut: GaussGym (3DGS renderer now unnamed), feature-alignment DA comparator
[Cheng], selection rules MetaMVUC/AMF/Anwar, SureSim, GaussTwin (photometric correction now uncited),
SimOpt, real-only scaling [Lin]. Refs renumbered to the Wave 15 §6 list: [1] Habitat, [2] 3DGS, [3]
RialTo, [5] EmbodiedSplat, [6] ManiSkill3, [7] BayesSim, [8] OpenVLA, [9] pi0, [10] NaVILA, [11] LoRA,
[12] OFT, [14] Maddukuri, [15] SimpleVLA-RL, [16] Liu et al. (RL for VLA), [17] TwinRL, [18] Cosmos,
[19] NWM, [20] WMPO, [23] Qwen2.5-VL, [24] Du et al., [25] FisherRF, [26] Bayes' Rays, [27] Liu et al.
risk-aware, [28] ASID, [29] AREA3D, [30] ScanNet++, [31] Tobin, [32] Peng, [33] DINOv2, [34] PPI,
[35] SIMPLER. Reference numbers in the older comments below are pre-Wave-15.
-->
<!--
Wave 14 (issue #30), 2026-09-26: pivot decision v4 (research/pivot-decision.md, top; framing only, v3 scope
and all review-3 fixes unchanged). The intro now says the dissertation develops ONE method with components
C1-C3 (one per loop step), Stages I-III develop and test one component each (ablations, RQ1-RQ3), Stage IV
tests the whole method (RQ4 = thesis H4). Stage headings renamed "C1/C2/C3". Stage IV adds the v4 baseline
"strongest existing real-to-sim-to-real pipeline" = uniform capture + domain randomization + random
real-data selection, RialTo-style (v4 wording; RialTo = §6 [3]); it replaces the former "uniform loop"
comparator and keeps the same twin, learner and correction so only the allocation differs (design choice).
H4 success criterion adds (b) >= 2x less real data than that pipeline, upper 95% bound of the ratio < 1
(mirrors §7; (b) new in v4, CONFIRM supervisor). Trims for the 2-page limit (no content removed): wording
of the tier-A sharing clause, Stage II baselines/metric, Stage III selection, Stage IV curves.
-->
<!--
(history) Wave 13 (issue #29), 2026-09-26: generalized for pivot decision v3 (research/pivot-decision.md) and the
coordinator's agreed §7 protocol (msg_05231fbe3093): per-testbed tier A with a separate, higher-fidelity
reference; navigation = ScanNet++ laser scan + DSLR reference vs. phone-stream twin; manipulation =
ManiSkill3 scene with held-out ground-truth physical parameters vs. 3DGS twin from a subset of its views +
parameters identified from a few interactions; tier B = published SIMPLER paired sim/real evaluations;
one operator-time cost; metric P; H4 needs both testbeds + tier-B direction. Navigation is no longer
"primary"; "rollouts" -> "trials"; the twin has a physical part (system identification, BayesSim-type
posterior [9]); task relevance for physical parameters = sensitivity of the expert's success in the twin
to the parameter's posterior (design choice, CONFIRM supervisor); ASID [21] as the task-blind
identification baseline. Navigation's physical part = actuation-noise parameters of the robot model
(design choice). Manipulation configuration count (>= 20, 10 held out) mirrors navigation (design choice).
SIMPLER ranking check: SIMPLER's paired real evaluations of published policies (RT-1/Octo family on Google
Robot and WidowX set-ups per the SIMPLER paper) are to be re-read before Stage IV. The ManiSkill3
physical-parameter ranges are pre-registered in T3.1. Tier C manipulator: K29 Laboratorium Robotyki
(UR3, FANUC LR Mate, ABB IRB 120; research/resources.md §1), availability UNVERIFIED, hence "where access
is agreed". Refs renumbered to the Wave 13 §6 list: [1] Habitat, [2] 3DGS, [5] EmbodiedSplat, [7]
GaussGym, [8] ManiSkill3, [9] BayesSim, [11] Lin, [12] Suomela, [15] Maddukuri, [17] FisherRF, [19] Bayes'
Rays, [20] Liu et al., [21] ASID, [22] ScanNet++, [23] Tobin, [24] Peng, [25] SimOpt, [26] Cheng, [27]
DINOv2, [29] MetaMVUC, [30] AMF, [31] Anwar, [32] PPI, [33] SureSim, [34] SIMPLER, [35] GaussTwin.
Reference numbers in the older comments below are the OLD (review-3) numbers.
-->
<!--
Wave 11 (issue #26), 2026-09-26: rewritten for pivot decision v2 (research/pivot-decision.md, binding).
Stages follow the loop: I task-aware capture (H1, >= 40% less capture), II uncertainty-aware training
(H2, >= 10 pp over uniform DR), III active real-rollout selection + twin/policy correction (H3, >= 50%
fewer rollouts), IV whole-loop exchange rate (H4, <= 10% of real-only data) + manipulation. Thresholds
copied from pivot-decision.md; decision rules mirrored from the final content/07 (issue #25, worker T):
recon-only comparator in H1, >= 2 budgets in H2, ratio bounds in H3/H4, uniform-loop and world-model
comparators in H4(a), H4(b) sign rule.
Removed from wave 9-10: paired-frame benchmark, CKA/probe gap localization, policy zoo, weight-space
predictors, conformal failure monitors (representation thesis; benchmark building rejected by the student).
Design choices (CONFIRM supervisor):
- Tier A "capture" = selection of frames from the recorded pool (offline NBV); task relevance = visitation
  or attention of a pilot policy; ensemble disagreement as the gap predictor; the capture itself as the
  "small real set" for H2(b).
- Real-only baseline in tier A = policy trained on episodes in the reference twin, counted as real data.
- Manipulation tier A: reference = the ManiSkill3 twin environment, training twin = 3DGS from subsampled
  renders; SIMPLER checkpoints/paired numbers to be re-read before Stage IV.
- Robot time: 3 x 2 x 30 x 2 min = 360 min + 40 x 2 min = 80 min ~ 7.3 h, rounded to ~8 h. ~2 min per
  episode incl. reset is ASSUMED; confirm after the first campaign.
- UNVERIFIED: K46 GPU servers; RGB-D availability at Denali; ScanNet++ licence terms for releasing derived
  reconstructions (§12 risk).
Refs are §6 numbers of the review-3 list (old [19]-[35] shifted by +1 after inserting Liu et al. as [19]):
[1] Habitat, [2] 3DGS, [3] EmbodiedSplat, [5] GaussGym, [8] ManiSkill3, [9] Lin, [10] Suomela,
[13] Maddukuri, [16] FisherRF, [18] Bayes' Rays, [19] Liu et al. risk-aware view acquisition, [20] ScanNet++,
[21] Tobin, [24] Cheng, [26] DINOv2, [28] MetaMVUC, [29] AMF, [30] Anwar, [33] PPI, [34] SureSim,
[35] SIMPLER, [36] GaussTwin.
Review-3 (issue #27), 2026-09-26 (research/review-3.md): R3-F1 tier-A reference = ScanNet++ laser-scan mesh
textured from DSLR images (arXiv:2308.11417 abstract), twin = 3DGS from the iPhone stream; second reference
(3DGS from all DSLR images) as a sign check. EmbodiedSplat runs GS-reconstructed meshes in Habitat-Sim
(arXiv:2509.17430 abstract, "we reconstruct meshes via GS"). R3-F6 image-goal navigation as in EmbodiedSplat;
minimum geodesic distance fixed in the T3.1 pilot. R3-F9 planner-path task relevance (no training in the
capture loop); imitation as the main learner. R3-F5 capture cost: views (H1 decision) plus an estimated
walking-tour time (secondary; walking speed and dwell per view pre-registered). R3-F8 risk-aware view
selection (Liu et al., arXiv:2403.11396) as an H1 comparator where its code runs. R3-F4 held-out capture
slice for H2(b). R3-F12 re-captured views counted. R3-F2 real-only = imitation of planner demonstrations.
R3-F7 manipulation proxy = simulator rendering vs 3DGS twin, physics shared (visual part only).
-->

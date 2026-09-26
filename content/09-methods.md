# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The dissertation develops **one method** with three stages: real data → digital twin → training of
navigation models in the twin → transfer back to reality with a few real data that correct the twin and
the model. Stages 1–3 are developed and tested one at a time (RQ1–RQ3); the whole pipeline is then tested
against existing approaches (RQ4). Existing open-source tools are used throughout: no simulator, dataset
or foundation model is built from scratch.

**Evaluation protocol: proxy reality (decides the hypotheses).** On ≥ 20 public indoor scenes of
ScanNet++ [16] (10 held out from all tuning), "reality" is the laser-scan mesh textured from the DSLR
images and rendered in Habitat [1] with a robot-camera model. The twin is built from a subset of the
separate phone capture of the same scene, so twin and "reality" share neither images nor reconstruction
method; the largest capture budget stays below the full capture. Tasks are indoor goal-reaching
navigation (e.g. image-goal and point-goal; instruction-following where instructions are available), with
a minimum path length set in a pilot so that P stays below its ceiling. "Reality" also has its own
physical parameters (e.g. actuation noise), hidden from the method and learned only from counted real
data; this physical gap is synthetic, and the robot checks it. Real data (captured views, real trials and demonstrations) is summed in one
operator-time cost. The proxy's own error to held-out real images is reported, and every hypothesis is
re-checked for sign with a second reference built from all DSLR images. P = success rate; path efficiency
is also reported.

**Stage 1 – transfer of real data into a digital twin (RQ1, H1; sem. 3–4).**
- *Method:* the twin's appearance and geometry come from neural scene reconstruction (3DGS-type [10]),
  run as a mesh in the simulator (as in [11]) or rendered directly; its physical part (e.g. traversable
  surfaces, collisions, the robot's actuation noise) is estimated from a few measurements as a posterior
  [15]. The next views are chosen where the twin's uncertainty (e.g. Fisher information [17] or an
  uncertainty field [18] adapted to 3DGS) is highest in the regions that matter for navigation: along
  planner paths between likely goals and, optionally, where a pretrained vision-language model grounds
  the task. Candidates come from the recorded capture; capture time is estimated as a walking tour.
- *Comparators:* uniform capture; task-blind and risk-weighted uncertainty selection [17, 19]; vision-
  language-guided reconstruction-quality selection [20].
- *Criterion (H1):* budget–P curves (≥ 4 budgets, the same navigation learner trained in each twin);
  ≥ 40% less capture (in views; operator time also reported) than uniform at equal P, with the 95% bound of the ratio below 1.

**Stage 2 – training navigation models in the twin (RQ2, H2; sem. 4).**
- *Method:* the navigation model is initialized from a pretrained foundation model (e.g. a general
  navigation model or a vision-language-action model [21–24]) and trained in the twin by imitation of
  planner demonstrations and then by reinforcement learning on a subset of scenes, with parameter-efficient adaptation where the
  model is large. Randomization strength follows the twin's uncertainty per region and per physical
  parameter, and twin samples far from a few real samples in a frozen-encoder space [29] are down-weighted;
  these real samples are held out from the capture and count towards its budget. A learned world model
  (e.g. a video world model [25, 26]) adapted on twin data generates additional trajectories where the twin
  is most uncertain.
- *Comparators:* uniform randomization of appearance [5] and dynamics [6], and none; ablations without the
  world model, without uncertainty weighting and without foundation-model initialization.
- *Criterion (H2):* mean paired gain in P over uniform randomization ≥ 10 pp on held-out scenes, lower 95%
  bound > 0, at each of ≥ 2 capture budgets.

**Stage 3 – transfer back to reality with few real data (RQ3, H3; end of sem. 4 – sem. 5).**
- *Method:* candidate real trials are scored by the predicted twin-to-reality gap, combining the twin's
  uncertainty along the planned path, disagreement between twin and world model, and the navigation
  model's own uncertainty (ensemble spread). The top-ranked trials are run in reality; they correct the
  twin (re-capture where real and twin observations disagree, counted in the budget; posterior update of
  physical parameters [7, 15]) and the model (co-training with twin data [9]). Real P from few trials is
  estimated with prediction-powered inference [30].
- *Comparators:* random selection, uniform coverage and failure-prone selection from the twin alone [27].
- *Criterion (H3):* the target P with ≥ 50% fewer trials than random selection (95% bound of the ratio
  below 1).

**Whole pipeline (RQ4, H4; sem. 6).** Budget curves (real data against P) of the whole method, of the
strongest existing real-to-sim-to-real approach, re-implemented for navigation and tuned with the same
effort as the method (uniform capture, uniform randomization, training in the twin and random or
failure-driven real trials, with the same reconstruction pipeline, learner and correction; e.g. [14, 27]),
and of learning from real data only (imitation of real demonstrations, same initialization). The method's
settings are fixed before this stage. *Criterion (H4):* ≥ 2× less real data than the existing approach at
the target P, with the 95% bound of the ratio below 1, and the stage 1–3 effects keep their sign.

**Real-robot validation.** Two campaigns (sem. 5 and 7) with own phone or RGB-D captures of 2 rooms at PWr
and a mobile robot: uniform capture versus the method, ~8 robot-hours per campaign; they check the
direction of the results and never tune thresholds.

**Statistics and compute.** Targets are defined from each comparator's own curve at its largest budget.
Tests are one-sided at α = 0.05 with a scene-level bootstrap and Holm correction, pre-registered before each
stage. Training runs on WCSS and PLGrid GPUs (computing grant applied for in sem. 3); smaller models are
used for development. Code is released where dataset and model licences permit.

<!--
Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
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

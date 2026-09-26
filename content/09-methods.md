# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The dissertation develops **one method** for the loop: real data → twin → sim-first fine-tuning of a
pretrained VLA in the twin and in a world model grounded in it → a few real trials → correction of twin,
world model and VLA → deployment. Stages I–III develop and ablate its components C1–C3 (RQ1–RQ3), and
Stage IV tests the whole method (RQ4, the thesis H4). The twin has two parts: geometry and appearance from
existing open-source 3D Gaussian Splatting (3DGS) [2] pipelines, and physical parameters identified from
real interactions as a posterior (BayesSim-type [7]). No simulator, benchmark, VLA or world model is
trained from scratch.

**Models (open weights, adapted).** *VLA:* OpenVLA-OFT [8, 12] for manipulation, with π0 [9] (openpi) as
a second backbone, and NaVILA [10] for navigation, whose mid-level actions ("move forward 75 cm") map onto
Habitat actions. All VLA fine-tuning is parameter-efficient: LoRA [11] adapters, supervised fine-tuning
(SFT) and then PPO, which generalizes best for VLAs [16], with open RL tooling [15]. *VLM:* Qwen2.5-VL-7B
[23], zero-shot, grounds the instruction to task-relevant objects and regions (C1) and judges success
[24] where the simulator gives no ground truth (checked against it where it does). *World model:*
Cosmos-Predict2 [18] (manipulation) and NWM [19] (navigation) checkpoints, post-trained on twin rollouts.
*Compute:* published needs are ≥ ~27 GB of GPU memory for OpenVLA LoRA, > 22.5 GB for π0 LoRA, and one
8-GPU node for RL of a VLA in simulation [15]. We estimate ~23k H100-hours for sem. 3–7 (~5 H100 on
average): WCSS Lem and a PLGrid grant, applied for in T3.1; small VLAs are used for development.

**Tier A protocol: proxy reality (decides the hypotheses).** In each testbed "reality" is a reference
from a separate, higher-fidelity source, and the twin is built from a subset of a separate, cheaper
capture. *Navigation:* on ≥ 20 ScanNet++ [30] scenes (10 held out from all tuning), the reference is the
laser-scan mesh textured from the DSLR images and rendered in Habitat [1] with a robot-camera model; the
twin is 3DGS from a subset of the phone stream, run as a mesh (as in EmbodiedSplat [5]) or with a 3DGS
renderer; its physical part is actuation noise. Tasks: instruction and image-goal navigation with a
minimum geodesic distance set in a pilot so that P stays below its ceiling. *Manipulation:* ManiSkill3 [6]
tasks (≥ 20 task–object configurations, 10 held out); reality is the simulator with held-out physical
parameters and its own rendering; the twin is 3DGS from a subset of its
views plus parameters identified from a few recorded interactions. Physics is shared, so this is the
weaker proxy. *Both:* capture = views and interaction samples; trials and demonstrations = episodes in the
reference; all summed in one operator-time cost; the largest budget stays below the full capture. In
navigation the proxy's error to held-out real images is reported, and each hypothesis is re-checked for
sign with a second reference (3DGS from all DSLR images). *Tier B:* SIMPLER [35] paired sim/real
evaluations of published policies; the twin must reproduce their direction. P = task success rate.

**Stage I – C1, VLM-guided task-aware capture (RQ1, H1; sem. 3–4).**
- *Method:* the twin's uncertainty, per region (Fisher information [25] or a Bayes' Rays-type [26] field
  adapted to 3DGS) and per physical parameter (posterior spread), is weighted by task relevance: the VLM's
  grounding of the instruction, how often expert trajectories pass through a region, and how much expert
  success changes across a parameter's posterior. The next views or interactions are chosen greedily where
  task-weighted uncertainty is highest, from the recorded pool (capture time estimated as a tour).
- *Baselines:* uniform capture; task-blind uncertainty selection (FisherRF-type [25], ASID-type [28]);
  risk-weighted [27] and VLM-guided reconstruction-quality selection (AREA3D-type [29]); same budget.
- *Metric and criterion (H1):* budget–P curves (≥ 4 budgets per testbed; the VLA LoRA-SFT-tuned in each
  twin); ≥ 40% less capture than uniform at equal P, and the upper 95% bound of C_task / C_recon < 1 (§7).

**Stage II – C2, uncertainty-aware fine-tuning in the twin and a twin-grounded world model (RQ2, H2;
sem. 4).**
- *Method:* the VLA is LoRA-fine-tuned by SFT on expert (planner) demonstrations in the twin and then
  by RL. (a) Randomization strength follows the twin's uncertainty
  (per-region appearance and geometry, physical parameters from their posterior), and twin samples far
  from a few real samples in DINOv2 [33] space are down-weighted; the real samples are a held-out slice of
  the capture and count towards the budget. (b) The world model, post-trained on twin rollouts, generates
  extra rollouts from states in the twin's most uncertain regions for on-policy RL [20], weighted by that
  uncertainty.
- *Baselines:* (a) uniform randomization of appearance [31] and dynamics [32], and none; (b) twin only
  (same C2 without the world model) and world model only; same capture budget.
- *Criterion (H2):* (a) mean paired P gain over uniform randomization ≥ 10 pp on held-out scenes, lower
  95% bound > 0; (b) lower 95% bound of the paired gain of twin + world model over twin only > 0; both at
  each of ≥ 2 capture budgets.

**Stage III – C3, few real trials and correction (RQ3, H3; end of sem. 4 – sem. 5).**
- *Selection:* candidate trials are scored by the predicted gap:
  the twin's uncertainty along the planned trajectory, twin–world-model disagreement on the outcome and the
  VLA's uncertainty (spread of LoRA ensemble actions). The top-k are run in reality (tier A: the reference).
- *Use:* the trials correct the twin (re-capture or re-weighting where real and twin observations disagree,
  counted in the budget; posterior update [7]), extend the world model's post-training data, and fine-tune
  the VLA by co-training with twin data [14]. Real P from few trials uses prediction-powered inference [34].
- *Baselines:* random selection, uniform coverage and failure-prone selection from the twin alone
  (TwinRL-type [17]); same number of trials.
- *Criterion (H3):* the target P with ≥ 50% fewer trials than random (upper 95% bound of the ratio < 1).

**Stage IV – the whole method in both testbeds (RQ4, H4; sem. 6).**
- *Budget curves:* real data (capture + trials, one operator-time cost) against P for the method; for
  **real-only fine-tuning of the same VLA** (LoRA SFT on expert demonstrations in the reference, same
  initialization; real-only RL also shown); and for the **strongest existing twin fine-tuning pipeline for
  VLAs**, TwinRL/RialTo-style [17, 3]: uniform capture, uniform randomization, SFT + RL of the same VLA in
  the twin, random or failure-driven real trials (the better is reported), with the same twin, learner and
  correction and TwinRL's released code where it applies. The exchange rate is the ratio of the budgets
  reaching the target P.
- *Success criterion (H4, the thesis; §7):* with C1–C3 and their hyperparameters unchanged, in each
  testbed ≤ 10% of the real data of real-only fine-tuning (upper 95% bound < 0.2) and ≥ 2× less than the
  pipeline (bound < 1); H1–H3 effects keep their sign; tier B agrees in direction.

**Tier C validation.** Two robot campaigns (sem. 5 and 7) with own phone or RGB-D captures at PWr: a mobile
robot in 2 rooms and, where access is agreed, a tabletop manipulator; uniform capture versus the method,
~8 robot-hours per campaign, agreement only. **Statistics:** tests follow §7; the protocol is
pre-registered before each stage. Code is released where dataset and model licences permit.

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

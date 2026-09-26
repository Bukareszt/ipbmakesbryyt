# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The dissertation develops **one method** for the loop: real data → twin → learning in the twin → a few
real trials → correction of the twin and the policy → deployment. Its three components, one per step, are
developed and tested as ablations in Stages I–III (§3, §7): C1 task-aware capture (RQ1), C2
uncertainty-aware learning in an imperfect twin (RQ2) and C3 active selection of few real data (RQ3);
Stage IV tests the whole method (RQ4, the thesis H4). The components are domain-agnostic: they act on the
twin's uncertainty, on task relevance measured in the twin and on learned representations. The twin has two
parts: geometry and appearance, reconstructed with existing open-source 3D Gaussian Splatting (3DGS) [2]
pipelines, and physical or dynamic parameters, identified from real interactions as a posterior
(BayesSim-type [9]). No simulator or benchmark is developed. Robotic manipulation and visual navigation
are equal testbeds with the same protocol.

**Tier A protocol: proxy reality (decides the hypotheses).** In each testbed, "reality" is a reference
from a separate, higher-fidelity source, and the twin is built from a subset of a separate, cheaper
capture, sharing no data. *Navigation:* ScanNet++ [22] gives each scene a laser scan,
DSLR images and a separate phone RGB-D stream. On ≥ 20 scenes (10 held out from all tuning), the reference
is the laser-scan mesh textured from the DSLR images and rendered in Habitat [1] with a robot-camera model;
the twin is 3DGS from a subset of the phone stream, run as a mesh (as in EmbodiedSplat [5]) or with a 3DGS
renderer (GaussGym [7]); its physical part is the robot's actuation noise. Tasks: image-goal and point-goal navigation with a minimum geodesic distance set in a pilot so
that P stays below its ceiling. *Manipulation:* ManiSkill3 [8] tasks (≥ 20 task–object configurations, 10
held out), where reality is the simulator with held-out ground-truth physical parameters (mass, friction,
articulation) and its own rendering, and the twin is 3DGS from a subset of its views plus parameters
identified from a few recorded interactions. Physics engine and object models are shared, so this is the
weaker proxy (unmodelled dynamics are not tested); tier B checks it. *Both:* real data is counted exactly:
capture = views and interaction samples given to the twin, real trials and demonstrations = episodes in
the reference, summed in one operator-time cost at a pre-registered rate; the largest budget stays below
the full capture. In navigation the proxy's error to held-out real images is reported (PSNR, LPIPS, depth)
and each hypothesis is re-checked for sign with a second reference (3DGS from all DSLR images). *Tier B:* the twin must rank manipulation policies as published paired sim/real evaluations do (SIMPLER [34]).
*Compute:* WCSS Lem (NVIDIA H100), PLGrid (to be applied for). Policies are small heads on frozen visual encoders, trained mainly by
imitation of a privileged expert in the twin (shortest-path planner; motion-planning expert), with
reinforcement learning on a subset. P = task success rate.

**Stage I – C1, task-aware capture (RQ1, H1; sem. 3–4).**
- *Method:* the twin's uncertainty, per region (Fisher information [17] or a Bayes' Rays-type [19] field,
  adapted to 3DGS) and per physical parameter (posterior spread), is weighted by **task relevance**
  measured in the current twin without training: how often expert trajectories pass through a region, and
  how much the expert's success changes across a parameter's posterior. The next views or interactions are
  chosen greedily where task-weighted uncertainty is highest until the budget is spent.
  Candidates come from the recorded pool; capture time is also estimated as a tour of the chosen views.
- *Baselines:* uniform capture, task-blind uncertainty selection (FisherRF-type next-best-view [17];
  ASID-type exploration for parameter accuracy [21]) and risk-weighted view selection [20], at the same
  budget.
- *Metric:* budget–P curves on tier A with ≥ 4 capture budgets per testbed; capture needed to reach the P
  that uniform capture reaches at the largest budget.
- *Success criterion (H1):* ≥ 40% less capture than uniform at equal P, and less than task-blind selection
  (upper 95% bound of the ratio < 1), as in §7.

**Stage II – C2, uncertainty-aware learning in an imperfect twin (RQ2, H2; sem. 4).**
- *Method:* (a) randomization whose strength follows the twin's uncertainty: appearance and geometry
  perturbations per region, and physical parameters sampled from their identified posterior instead of
  hand-set ranges; (b) down-weighting twin samples that lie far from a few real samples in frozen DINOv2
  [27] feature space. The real samples are a held-out slice of the capture,
  not used to fit the twin, and count towards the budget.
- *Baselines:* uniform domain randomization of appearance [23] and dynamics [24] (tuned ranges), no
  randomization, and feature alignment [26] as a comparator; same capture budget.
- *Metric and criterion (H2):* tier-A P, paired by held-out scene; ≥ 10 pp higher P than uniform
  domain randomization (lower 95% bound > 0) at each of ≥ 2 equal capture budgets.

**Stage III – C3, few real trials and correction (RQ3, H3; end of sem. 4 – sem. 5).**
- *Selection:* candidate trials (start–goal pairs, object configurations) are scored by the predicted
  twin-to-real gap: disagreement of a policy ensemble plus the twin's uncertainty along the planned
  trajectory. The top-k are run in reality (tier A: the reference).
- *Use:* the trials (i) correct the twin, by re-capturing or re-weighting regions where real and twin
  observations disagree (photometric correction as in [35]; re-captured views are counted) and by updating the physical-parameter posterior [9, 25]; and (ii) fine-tune the policy by
  co-training with the real trials [15]. Real P is estimated from few trials with prediction-powered
  inference [32, 33].
- *Baselines:* random selection and uniform coverage of the same number of trials; selection rules
  [29–31] where they apply.
- *Success criterion (H3):* the target P is reached with ≥ 50% fewer real trials than random selection
  (upper 95% bound of the ratio < 1).

**Stage IV – the whole method in both testbeds (RQ4, H4; sem. 6).**
- *Budget curves:* real data (capture + trials, one operator-time cost) against P for the method (C1–C3);
  for **real-only learning**, imitation of expert demonstrations in the reference with the same frozen
  encoder and initialization (real-only reinforcement learning also shown); and for the **strongest
  existing pipeline**, RialTo-style [3]: uniform capture, uniform domain randomization and random real
  trials, with the same twin, learner and correction. The "exchange rate" is the ratio of the budgets
  reaching the target P; real-only scaling [11, 12] suggests the curve shapes. Also reported: a released
  pretrained world model as the simulator (not trained).
- *Success criterion (H4, the thesis; §7):* with C1–C3 and their hyperparameters unchanged (the learner is
  each task's standard one), in each testbed ≤ 10% of the real data of real-only learning (upper 95% bound
  < 0.2) and ≥ 2× less than the existing pipeline (bound < 1); H1–H3 effects keep their sign; tier B
  agrees in direction.

**Tier C validation.** Two robot campaigns (sem. 5 and 7) with own phone or RGB-D captures at PWr: a mobile
robot in 2 rooms and, where access is agreed, a tabletop manipulator. Uniform capture versus the method,
plus the few selected trials; about 8 robot-hours per campaign (3 policies × 2 settings × 30 episodes at
~2 min, plus 2 × 20 trials). Tier C reports agreement only and never tunes thresholds.

**Statistics and reproducibility.** Tests follow §7; the protocol is pre-registered before each stage and
changes are logged. Code is released where the dataset licences permit.

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

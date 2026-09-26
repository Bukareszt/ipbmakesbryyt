# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

The research follows the real-to-sim-to-real loop: real capture → twin → policy training in the twin →
a few real rollouts → correction of the twin and the policy → deployment. Four stages (I–IV) match §3 and
the research questions of §7: capture less (RQ1), train robustly on an imperfect twin (RQ2), collect few
real rollouts (RQ3), and measure the budget of the whole loop (RQ4). For each stage we give the method,
data, metric and success criterion. Twins are built with existing open-source 3D Gaussian Splatting (3DGS)
[2] pipelines and simulators; the student develops neither a simulator nor a benchmark. Visual navigation
(point-goal and image-goal) is the primary task; manipulation is the cross-task test in Stage IV.

**Tier A protocol: proxy reality (decides the hypotheses).** Real robots make "real data" slow to collect
and hard to count, so the hypotheses are decided on public real scans. For ≥ 10 indoor scenes with dense
real captures and reference laser scans (e.g. ScanNet++ [19]), a **reference twin** built from the full
capture and the scan plays "reality", rendered in a GPU simulator (Habitat [1] or a 3DGS renderer such as
GaussGym [5], chosen in T3.1). The **training twin** is a 3DGS reconstruction built from a subset of the
same capture. This makes every unit of real data countable: *capture* = views selected from the recorded
pool (converted to capture minutes at the recording rate), *real rollouts* and *real demonstrations* =
episodes in the reference twin. Both are summed in one operator-time cost at a rate fixed in the
pre-registration. Some scenes are held out for all tuning. The proxy's own error is reported: renders of
the reference twin are compared with held-out real images (PSNR, LPIPS, depth error), and tier C checks
that tier-A conclusions hold on a robot. *Tier B:* public real-world datasets and published paired
sim/real results (SIMPLER [34]). *Tier C (validation only):* ≥ 2 PWr rooms captured with a phone or RGB-D
camera and a mobile robot (planned cooperation with the K29 "Denali" Autonomous Robots Laboratory,
agreement in T3.2). *Compute:* WCSS Lem (NVIDIA H100) and PLGrid allocations (to be applied for).
Policies are trained by reinforcement learning (PPO) and by imitation of a shortest-path planner in the
twin; small policies on frozen visual encoders keep the compute academic.

**Stage I – task-aware capture (RQ1, H1; sem. 3–4).**
- *Method:* per-region reconstruction uncertainty of the current twin (Fisher information [16] or a
  Bayes' Rays-type [18] field, adapted to 3DGS) is weighted by **task relevance**, i.e. how often a pilot
  policy trained in the current twin visits or attends to the region on sampled start–goal paths. The next
  views are chosen greedily where task-weighted uncertainty is highest, in rounds, until the budget is
  spent.
- *Baselines:* uniform subsampling of the capture, and reconstruction-only next-best-view (FisherRF-type
  [16]) at the same budget.
- *Metric:* budget–success-rate (SR) curves on tier A, with ≥ 4 capture budgets; capture needed to reach
  the SR that uniform capture reaches at the largest budget. Image fidelity (PSNR, LPIPS) is reported but
  is not the target.
- *Success criterion (H1):* ≥ 40% fewer views than uniform capture at equal SR, and fewer than
  reconstruction-only selection (upper 95% bound of the ratio < 1), as in §7.

**Stage II – uncertainty-aware training on an imperfect twin (RQ2, H2; sem. 4).**
- *Method:* (a) augmentation whose strength follows per-region reconstruction uncertainty (appearance and
  geometry perturbations where the twin is unsure, little where it is sure); (b) sample weighting of twin
  frames by their representation distance (frozen DINOv2 [25] features) to a few real images. The images
  come from the capture itself, so they cost no extra real data.
- *Baselines:* uniform domain randomization [20] with tuned ranges, no randomization, and feature
  alignment [23] as an extra comparator; all at the same capture budget.
- *Metric and criterion (H2):* tier-A SR on held-out scenes, paired by scene; ≥ 10 pp higher SR than
  uniform domain randomization at an equal capture budget (lower 95% bound > 0), at each of ≥ 2 budgets.

**Stage III – few real rollouts and correction (RQ3, H3; end of sem. 4 – sem. 5).**
- *Selection:* candidate real rollouts (start–goal pairs) are scored by the predicted twin-to-real gap:
  disagreement of a small policy ensemble, plus the reconstruction uncertainty along the planned path. The
  top-k are executed in reality (tier A: the reference twin).
- *Use:* the rollouts (i) correct the twin, by re-capturing or re-weighting the regions where real and
  twin observations disagree (photometric correction in the style of [35]), and (ii) fine-tune the policy
  by co-training with the real rollouts [13]. Real SR is estimated from few trials with
  prediction-powered inference [32, 33].
- *Baselines:* random selection and uniform coverage of the same number of rollouts; related selection
  rules [27–29] as comparators where they apply.
- *Success criterion (H3):* the target SR is reached with ≥ 50% fewer real rollouts than random selection
  (upper 95% bound of the ratio < 1).

**Stage IV – budget of the whole loop and cross-task test (RQ4, H4; sem. 6).**
- *Budget curve:* total real data (capture + rollouts, one operator-time cost) against real SR for the full
  loop (Stages I–III) and for **real-only learning**, i.e. a policy trained only on data collected in
  the reference with the same encoder and algorithm, every interaction counted as real data. The
  "exchange rate" is the ratio of the budgets that reach the target SR; real-only scaling results [9, 10]
  give the expected curve shapes. The curve is also reported for a uniform loop (no Stage I–III guidance)
  and for a frozen, pretrained world model used as the simulator (comparator only; not trained).
- *Manipulation:* the same pipeline, unchanged, on public manipulation scenes with twin environments
  (ManiSkill3 [8]) under the tier-A protocol; published paired sim/real results (SIMPLER [34]) check that
  the proxy ranks policies as reality does (tier B).
- *Success criterion (H4):* the loop reaches the target SR with ≤ 10% of the real data needed by
  real-only learning (upper 95% bound of the ratio < 0.2); on manipulation, with pipeline and
  hyperparameters unchanged, the ratio's upper bound is < 1 and the H1–H3 effects keep their sign.

**Tier C validation.** Two robot campaigns (sem. 5 and 7) in 2 PWr rooms: phone or RGB-D capture, twins,
policies with uniform capture versus the loop, and the few selected real rollouts. About 8 robot-hours per
campaign (3 policies × 2 rooms × 30 episodes at ~2 min each, plus 2 × 20 selected rollouts). Tier C is
reported as agreement with tier A and is never used to tune thresholds.

**Statistics and reproducibility.** Tests are one-sided (α = 0.05), bootstrapped over scenes and seeds,
Holm-corrected within each hypothesis, as in §7. The protocol is pre-registered in the project repository
before each stage, and changes are logged with reasons. Code and scripts are released where the dataset
licences permit.

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
Refs are §6 numbers of the wave-11 list: [1] Habitat, [2] 3DGS, [5] GaussGym, [8] ManiSkill3, [9] Lin,
[10] Suomela, [13] Maddukuri, [16] FisherRF, [18] Bayes' Rays, [19] ScanNet++, [20] Tobin, [23] Cheng,
[25] DINOv2, [27] MetaMVUC, [28] AMF, [29] Anwar, [32] PPI, [33] SureSim, [34] SIMPLER, [35] GaussTwin.
-->

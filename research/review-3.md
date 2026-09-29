# Review 3 — mock mid-term committee review of the pivot-v2 IPB

Issue #27 · 2026-09-26 · reviewed state: branch `ipb-draft`, commit 0e348e8 (Wave 11, data-efficient
real-to-sim-to-real), all `content/*.md`. The Phase 2 edits in `content/02–15` are uncommitted. `content/00`,
`content/01` and `tools/` were not touched.

**Role-play.** A sceptical three-person ITiT mid-term committee: an external ML member, a robotics member
and a computer-vision member, plus the SzD office's formal check. The committee reads the IPB as it will in
**Nov 2027**. It checks the text against SPEC §4, the 8 criteria of [benchmarks.md §2.1](benchmarks.md),
the binding [pivot-decision.md](pivot-decision.md) (v2), and [review-1.md](review-1.md) and
[review-2.md](review-2.md), to catch old issues that have come back.

**Evidence rule.** Every finding names a file and section. *(reviewer judgement)* marks an assessment that
isn't a measured fact. Citation claims used in fixes were re-checked on 2026-09-26:
- arXiv abstract pages: 2509.17430 EmbodiedSplat ("we reconstruct meshes via GS", Habitat-Sim, ImageNav),
  2308.11417 ScanNet++ (laser scan, "registered 33-megapixel images from a DSLR camera, and RGB-D streams
  from an iPhone") and 2403.11396 Liu et al. (risk-aware active view acquisition with FisherRF).
- OpenAlex abstracts: RialTo ("small amounts of real-world data") and Maddukuri et al. ("an average of 38%").
- Semantic Scholar: X-Sim ("10x less data collection time") and GaussGym ("learning locomotion from
  pixels").

Semantic Scholar returned HTTP 429 on the other requests. No new facts about people, labs or dates were
added, and nothing new is claimed as agreed.

**Page-limit method.** `tools/build_ipb.py` (Calibri 11 pt, spacing 1). It reports a text-length estimate
and the height measured in a Pages.app PDF. `output/` was rebuilt for the check and then restored with
`git checkout output/`.

---

## 0. Verdict

The v2 pivot is a real improvement for an ITiT/ML committee:
- It has one object (the real data a real-to-sim-to-real loop consumes) and one thesis sentence.
- It has four RQs that follow the loop (capture → train → rollouts → whole budget).
- It has numeric decision rules and no benchmark or zoo to build.
- Review-1 and review-2 structural fixes still hold: the robot is validation only, venues are all 200-point
  ITiT conferences, the visit length matches the funder, the autoreferat is in sem. 5, and no "to be
  confirmed" text is visible.

A committee would still vote **positive**. Three problems, though, would make the external ML member
question criteria 3 and 4 and the robotics member question criterion 2. All three are now fixed in
`content/`:

1. **Tier A proxy reality could be circular** (R3-F1). "Reality" was a high-fidelity reference "built from
   the full capture", and the twin was a 3DGS model built from a subset *of the same capture*. At large
   budgets the twin converges to the reference by construction. The whole twin-to-"reality" gap is then a
   same-method sparse-view artefact, which is exactly what reconstruction uncertainty measures. H1 and H2
   could pass because of the proxy, not the method.
2. **H4's real-only baseline was a strawman** (R3-F2). It was "trained directly in the reference, every
   interaction counted as real data" with "the same encoder and algorithm". With PPO, that needs millions of
   real steps, so "≤ 10% of real-only data" would be trivially true.
3. **The paper-before-results pattern came back** (R3-F3; review-2 R2-F3/F4). P1 (May 2027) was described
   as RQ1 + RQ2, but H2 completes in Jul 2027. P2 was set for ICLR 2028 (~late Sep 2027) or CVPR 2028
   (~Nov 2027), but H3 completed in Feb 2028.

The student-owned P0s from review-1 are **still open** and outside this task: ORCID, start date and
supervisor title in `content/01`, and the sem. 1–2 rows that must describe the work actually done.

---

## 1. Scores per mid-term criterion (projected to Nov 2027)

| # | Criterion | Before fixes | After fixes | Why |
|---|---|---|---|---|
| 1 | Progress on the IPB (1–5) | 4 | **4** | Sem. 3–4 tasks depend only on public data and WCSS, and the robot (T3.2) blocks no hypothesis. The deduction is for sem. 1–2, which are still unconfirmed as actual work (R1-F2). |
| 2 | Submission date realistic? (Y/N) | YES, with reservations | **YES** | 30.09.2029. P1 and P2 now report only results that exist by their deadlines (R3-F3). The feasibility risk of sem. 3 is reduced: task relevance comes from planner paths (no training inside the capture loop), and imitation is the main learner (R3-F9). |
| 3 | Hypotheses properly formulated? (Y/N) | YES, but H4(a) trivially true and H1/H2 open to a circularity objection | **YES** | Thesis, RQ1–RQ4 and H1–H4 keep the pivot thresholds. The real-only comparator is now the data-efficient recipe (R3-F2). Twin and reference come from separate captures and different methods (R3-F1). H4(b) says what "unchanged" means (R3-F7). |
| 4 | Suitability of methods (1–5) | 3 | **4** | The obvious objection ("your reality is a render") is now answered by design: a laser-scan reference, a separate phone capture for the twin, a robot-camera model, a second reference as a sign check, and the proxy's own error reported. The deduction: tier A is still a proxy, the manipulation leg tests only the visual part of the loop (stated as a limitation), and 3DGS-in-simulator throughput is unproven until T3.1. |
| 5 | Relevance of results (1–5) | 4 | **4** (projected) | Every sem. 3–4 task feeds H1 or H2 and P1. |
| 6 | Quality of carrying out tasks (1–5) | 4 | **4** (projected) | Deliverables are dated (Nov 2026, Dec 2026, Feb 2027, Apr 2027, Jul 2027, Sep 2027). |
| 7 | Original contribution (1–5) | 3 | **4** | The closest H1 competitor (risk-weighted FisherRF view acquisition, Liu et al. 2024) was missing from §6. It is now cited, differentiated and used as a baseline (R3-F8). Everything else is novel at the combination level (niches-data N1/N2/N9: 0–3 S2 hits per year). The novelty rests on a combination and on the budget measurement, not on a new primitive *(reviewer judgement)*. |
| 8 | International? (Y/N) | YES, weak | **YES, weak** | Before the mid-term there is a NeurIPS submission, a summer-school poster and a foreign co-author "sought". The visit is after the mid-term. The only thing that would change this to a clear YES is naming a real host or co-author before signing (student/supervisor). |

## 2. SPEC §4 checklist (office view)

| Item | Status |
|---|---|
| All 15 sections filled (§14 n/a) | PASS |
| §1 ORCID valid | **OPEN** (student; `content/01` is not owned here; R1-F1) |
| §3 sem. 1–8 each with a concrete output | PASS. Sem. 1–2 still carry CONFIRM (student) comments (R1-F2). |
| §3 locations, sub-study completion semesters | PASS: H1 Apr 2027, H2 Jul 2027, H3 Jan 2028, H4 Sep 2028 |
| §4 ≤ end of sem. 8 | PASS (30.09.2029) |
| §11 date in §3 and before §4 | PASS (May 2027 = T4.2) |
| §11 venue on the ministerial list | PASS (NeurIPS Lp 87, 200 pts, ITiT). Recheck against the 2027 list (§11 comment). |
| Every H has a method in §9 and a task in §3 | PASS: H1 Stage I/T3.3, T4.1; H2 Stage II/T4.1; H3 Stage III/T4.3, T5.1; H4 Stage IV/T6.1 |
| §8 contributions trace to §7 | PASS (items 1–4 ↔ H1–H4; item 5 = protocol and code) |
| §10 PL = EN | PASS (unchanged since the Wave 11 check; 5/7/3 sentences, same content) |
| Page limits | PASS, tight (see §6) |
| No visible TODO / "to be confirmed" | PASS for the owned sections. §1 "Notes" (not owned) still has visible "unconfirmed" ORCID text: R1-F1. |

## 3. Consistency chain after the fixes

| Item | §7 | §9 stage | §3 task(s) | §8 | §11/§12 papers |
|---|---|---|---|---|---|
| RQ1/H1 | capture less, ≥ 40% fewer views | I, sem. 3–4 | T3.1, T3.3, T4.1 (H1 by Apr 2027) | 1 | P1 NeurIPS 2027 |
| RQ2/H2 | train robustly, ≥ +10 pp | II, sem. 4 | T4.1 (first result Apr 2027, H2 by Jul 2027) | 2 | P1 (first H2 results) |
| RQ3/H3 | few rollouts, ≥ 50% fewer | III, end sem. 4 – sem. 5 | T4.3, T5.1 (H3 by Jan 2028) | 3 | P2 ICML 2028 (CVPR 2028 if H3 is done by Nov 2027) |
| RQ4/H4 | ≤ 10% of real-only; manipulation | IV, sem. 6 | T6.1 (H4 by Sep 2028) | 4 | P3 NeurIPS 2028, fallback ICLR 2029 |
| Tier C | agreement only | 2 campaigns | T5.2, T7.1 | — | — |

**Before the fixes:**
- §11, T4.2, §8 and §12 described P1 as reporting RQ1 + RQ2 in full, while §3 had H2 completed in Jul 2027.
- T5.3 had P2 at ICLR 2028 (~late Sep 2027, with only a first H3 result by then) or CVPR 2028 (~Nov 2027),
  while T5.1 completed H3 in Feb 2028 (R3-F3).
- §7 H4(b) and §9 said "pipeline unchanged", although the navigation learner (imitation/PPO on point-goal
  and image-goal navigation) cannot run unchanged on manipulation (R3-F7).

**Citation numbering.** Liu et al. was inserted as §6 [19], and old [19]–[35] became [20]–[36] (36 refs).
Every bracketed citation in visible text was re-checked by script:
- §6 cites [1]–[36] in order.
- §9 uses [1, 2, 3, 5, 8, 9, 10, 13, 16, 18, 19, 20, 21, 24, 26, 28–30, 33–36].
- §12 uses [3], [10] and [3–7, 11], which are unaffected.
- §5, §7 and §8 have no citations.

The §9 comment maps every number to a work.

**Leftover pre-pivot wording (visible text).** None. "Benchmark" appears only in negations (§5, §8, §9: "not
a … benchmark"). There is no zoo, CKA/probe, transfer forecasting or weight-space learning. Sem. 1 T1.2
("how much real data sim-to-real transfer needs") is pre-pivot but describes sem. 1 and fits v2 well.

## 4. Testability in tier A without a robot

| H | Decided on | Real-data unit in tier A | Verdict |
|---|---|---|---|
| H1 | capture–SR curves on ≥ 20 ScanNet++ scenes | phone-stream views (walking-tour time is secondary) | testable. Validity rests on the proxy, now non-circular (R3-F1). Candidate views are limited to the recorded pool (stated). |
| H2 | paired SR on 10 held-out scenes at ≥ 2 budgets | same, plus a held-out capture slice for the representation signal (R3-F4) | testable. With 10 held-out scenes, a scene-level bootstrap is meaningful (R3-F10). |
| H3 | rollout–SR curves | episodes in the reference; re-captured views count (R3-F12) | testable |
| H4(a) | budget curves: loop vs. real-only imitation in the reference | operator time (views + episodes + demonstrations) | testable, and no longer trivially true (R3-F2) |
| H4(b) | ManiSkill3 simulator rendering as "reality", 3DGS twin from its views | rendered views and episodes | testable, but only for the visual part of the loop (physics shared). Stated as a limitation in §9 (R3-F7). |

**Is the proxy-reality protocol credible now?** It is mostly credible *(reviewer judgement)*:
- The twin (3DGS from the iPhone stream) and "reality" (the laser-scan mesh textured from DSLR images,
  rendered with a robot-camera model) share neither images nor reconstruction method. The twin's errors are
  therefore not a copy of the reference's.
- The largest capture budget stays below the full stream, so the curves cannot converge to the reference
  by construction.
- A second reference (3DGS from all DSLR images) must give the same sign.
- The proxy's own error to held-out real images is reported, and tier C checks the direction on a robot.

What remains is an irreducible limitation that the committee will still raise: no real lighting changes,
motion blur, dynamic objects or actuation noise in tier A. §12 lists it as a risk, and tier C is the answer.

## 5. Novelty versus the closest works

| Work | What it does | What the IPB adds |
|---|---|---|
| RialTo [6] | Twins from "small amounts of real-world data", RL fine-tuning of real demos; appendix ablates 0–15 demos | Capture and rollouts as experimental variables, with one budget and active allocation at every step, in navigation |
| X-Sim [12] | Real-to-sim-to-real from one human RGB-D video; "10x less data collection time" than BC | A budget *curve* against real-only learning rather than a point comparison; active capture and rollout selection |
| EmbodiedSplat [3] | iPhone capture (20–30 min), GS meshes in Habitat-Sim, ImageNav fine-tuning, SRCC 0.87–0.97 | Varies and allocates the capture; used here as the twin-in-simulator route |
| FisherRF [16], GenNBV [17], Bayes' Rays [18] | Active view selection and uncertainty for reconstruction quality | A task-weighted objective judged by policy SR in the twin; FisherRF-type selection is a baseline |
| Liu et al. [19] (new) | FisherRF weighted by safety-critical regions for safe exploration | The closest to H1. The IPB's target is SR of a policy trained in the twin, not reconstruction or exploration safety. It is a baseline in Stage I. |
| GaussTwin [36], SimOpt [23] | Correct a twin or its randomization from real observations | Choosing *which* few real rollouts to collect, under a counted budget |

Verdict: the claim "first treatment of the loop's real data as one budget allocated actively, with budget
curves for navigation" is defensible, and it is hedged with "to our knowledge" in §8. H1's novelty is now
honest because the closest risk-weighted variant is cited and beaten or not.

## 6. Page limits (build_ipb.py, after the fixes)

| § | Limit | est. | PDF | Note |
|---|---|---|---|---|
| 5 | 1 | 0.87 | 0.78 | ok |
| 6 | 2 | 1.98 | 1.70 | ok. Was 2.06 after adding [19]; trimmed (hit counts removed, shorter sentences). |
| 7 | 1 | 0.99 | 0.85 | tight; do not add text |
| 8 | 1 | 0.98 | 0.86 | ok |
| 9 | 2 | 1.99 | 1.78 | tight. Was 2.09 after R3-F1/F2/F7; trimmed (statistics sentence points to §7). |
| 10 | 1 each | 0.50 | 0.44 / 0.43 | ok |
| 12 | 1 | 0.99 | 0.95 | tight |

## 7. Numbered fixes and status

Severity: **P0** = must fix before signing. **P1** = affects a mid-term criterion directly. **P2** = polish.
Status: **done** = applied in `content/`. **open (student)** = needs the student's facts or a file this task
doesn't own. **no change** = deliberately not applied, with the reason given.

### P0

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R3-F1 | **Proxy reality is circular.** The reference was "built from the full capture", and the twin was 3DGS from a subset of the same capture. The gap is a same-method sparse-view artefact, which is exactly what reconstruction uncertainty measures, so H1 and H2 could pass for the wrong reason. At the largest budget, twin ≈ reference. | Reference = the ScanNet++ laser-scan mesh textured from DSLR images, rendered in Habitat with a robot-camera model. Twin = 3DGS from a subset of the *separate iPhone stream*, run as a GS mesh (EmbodiedSplat route) or with a 3DGS renderer. The largest budget stays below the full stream. A second reference (3DGS from all DSLR images) gives a sign check, and the proxy error vs. held-out real images is reported. | 07, 09, 08, 12 | **done** |
| R3-F2 | **H4(a) strawman.** Real-only learning "trained directly in the reference … same encoder and algorithm" means RL from scratch counted as real data, so "≤ 10%" is trivially met. | Real-only = imitation of planner demonstrations collected in the reference, with the same frozen encoder and initialization (the data-efficient real-only recipe; cf. [9, 10]). Real-only PPO is reported only for completeness. Threshold unchanged. | 07, 09 | **done** |
| R3-F3 | **Papers before results** (review-2 R2-F3/F4 returned). P1 was described as RQ1 + RQ2, but H2 completes in Jul 2027. P2 was set for ICLR 2028 (~late Sep 2027) or CVPR 2028 (~Nov 2027), but H3 completed in Feb 2028. | P1 = H1 + first H2 results (§11, T4.2, §8, §12). H3 on tier A by Jan 2028. P2 = ICML 2028 (~late Jan 2028, expected from past cycles, UNVERIFIED; ICML Lp 847, 200 pts, ITiT), with CVPR 2028 only if H3 is complete by Nov 2027. ICLR 2028 dropped for P2. | 03, 08, 11, 12 | **done**. **Coordinator:** this deviates from pivot-decision.md ("P2: ICLR 2028 or CVPR 2028"). |
| R1-F1 | ORCID, start date, supervisor title (review-1, still open). | — | 01 | **open (student)** |
| R1-F2 | Sem. 1–2 must state what was actually done (review-1, still open). | — | 03 | **open (student)** |

### P1

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R3-F4 | H2(b): the "few real images come from the capture itself, so they cost no extra real data". But images used to fit the twin are reproduced almost exactly at their poses, so the distance is biased low. The direction of the weighting was also unclear. | Down-weight twin frames far from the real set (nearest-neighbour distance in DINOv2 space). The real images are a held-out capture slice, not used to fit the twin, and count towards the capture budget. §5: "computed from data the loop already collects". | 05, 07, 09 | **done** |
| R3-F5 | Capture cost: selecting frames offline from a recorded video does not shorten capture time, and views ≠ minutes. | H1 is decided on views (the pivot allows "minutes or views"). Capture time is also estimated as a walking tour through the chosen viewpoints (pre-registered speed and dwell). Candidates are limited to the recorded pool (stated). | 09 | **done** |
| R3-F6 | SR ceiling. Public scans are often room-scale. Point-goal SR can saturate even for poor twins, which would leave the τ-based ratios undefined or trivial. | Image-goal and point-goal navigation with a pre-registered minimum geodesic distance, set in the T3.1 pilot so that SR stays below its ceiling; SPL reported too. | 09, 03 | **done** |
| R3-F7 | Manipulation tier A isn't real-to-sim: ManiSkill3 scenes are synthetic, and physics is shared. "Pipeline unchanged" is impossible for the policy learner. | "Reality" = the simulator's own rendering, and the twin = 3DGS from a subset of its views. Only the visual part of the loop is tested (a stated limitation). "Unchanged" = the three allocation methods and their hyperparameters; the learner is the task's standard one. | 07, 08, 09 | **done** |
| R3-F8 | Missing closest competitor for H1: risk-aware active view acquisition (Liu et al., arXiv:2403.11396) already weights FisherRF by safety-critical regions. | Cited as §6 [19] and differentiated (safe exploration and reconstruction, not policy SR). Added as a Stage I baseline and in T3.3. Refs renumbered. | 06, 09, 03 | **done** |
| R3-F9 | Feasibility of sem. 3: the Stage I inner loop trained a pilot *policy* per round × scene × budget × seed, and PPO in 3DGS scenes is expensive. T3.1 has only ~3 months. | Task relevance = planner-path visitation (geometry only, no training), with pilot-policy attention as a variant. Imitation of a shortest-path planner is the main learner, with PPO on a subset. The twin runs as a GS mesh in Habitat (as EmbodiedSplat does) or in a 3DGS renderer, chosen in T3.1. | 09, 03 | **done** |
| R3-F10 | "≥ 10 scenes, some held out" leaves ~3–5 scenes for the scene-level bootstrap of H2's paired gain. | ≥ 20 scenes, 10 held out from all tuning (§7, §9, T3.1). Compute stays academic with imitation learning *(reviewer judgement)*. | 03, 07, 09 | **done** |
| R3-F11 | Overclaims. §8: "budget law" (a curve fitted on ~20 rooms is not a law); "It tells a practitioner…"; "measured law". §5: "has not been measured" was unhedged. | §8: "budget curves", "roughly", "measured estimate". §5: "to our knowledge". "Budget law" is kept only as P3's working title in §3 T6.3. | 05, 08 | **done** |
| R3-F12 | H3 twin correction "by re-capturing" could spend hidden capture budget. | Re-captured views count towards the budget. | 09 | **done** |
| R3-F13 | Criterion 8 is still weak (no named host or co-author before the mid-term). | — | 12 | **open (student/supervisor)** |

### P2

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R3-F14 | The world-model comparator in H4 is not cited or specified. | §9: "a released pretrained world model" (comparator only). No citation was added, to protect the §6 page limit; name the model in the Stage IV pre-registration. | 09 | **done** (text); citation **no change** |
| R3-F15 | §6 listed GaussGym under navigation, but its title is "learning locomotion from pixels". | "navigation and locomotion". | 06 | **done** |
| R3-F16 | §6 used Semantic Scholar hit counts as evidence in form text ("0–2 hits", "0–1 hits"). | Replaced by the named closest work and "we found at most two … a year". | 06 | **done** |
| R3-F17 | Page limits after the fixes: §6 2.06, §9 2.09, §7 1.03, §8 1.00. | Trimmed without losing content; see §6 of this file. | 06–09 | **done** |
| R3-F18 | Tier C has 30 episodes per condition and can detect only large SR differences. | No change. Tier C is stated as agreement only and is never used to tune thresholds. | — | **no change** |
| R3-F19 | Sem. 4 is heavy: H1 completion, H2, P1, Stage III set-up, grants and a poster. | No text change. R3-F9 cuts the compute, and the Feb 2027 checkpoint (T3.3) is where to cut scope. | — | **no change** (monitor) |
| R3-F20 | ScanNet++ licence terms for releasing derived reconstructions are unverified. | Already covered: "Code and scripts are released where the dataset licences permit" (§9) and the §12 licence risk. | — | **no change** |

## 8. Questions to prepare for the 15-minute talk

1. Your "reality" is a render of a laser scan. What gap does it have to real images, and did H1–H2 keep
   their sign with the second reference? (R3-F1)
2. Why is imitation from real demonstrations the right real-only baseline, and how many demonstrations did
   it need? (R3-F2)
3. Your capture was selected from a pre-recorded video. What would guided capture cost in a real room?
   (R3-F5; tier C)
4. How does your task-weighted uncertainty differ from risk-aware FisherRF [19]? Did you beat it? (R3-F8)
5. Manipulation shares physics between twin and "reality". What does H4(b) actually show? (R3-F7)
6. What was actually done in year 1? (R1-F2)

## 9. Handover

- `output/*.docx|pdf` were regenerated by `tools/build_ipb.py` for the page check and then restored with
  `git checkout output/`. The owner of `output/` must rebuild them after these edits.
- **For the coordinator:** R3-F3 changes the P2 venue options relative to pivot-decision.md. ICLR 2028 is
  dropped for P2, and ICML 2028 (~late Jan 2028) is added, with CVPR 2028 only if H3 is complete by then.
  RQ/H numbering and all pivot thresholds (40%, +10 pp, 50%, ≤ 10%) are unchanged.
- §6 now has 36 references (the old self-imposed ceiling was 35). The README's guideline is 15–30.
  Dropping one low-value reference would need another renumbering.

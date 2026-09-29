# Review 4 (final): mock mid-term committee review of the v6 IPB

Issue #34 · 2026-09-26 · reviewed state: branch `ipb-draft`, commit 41c775c (Wave 16, v6 general rewrite),
all `content/*.md`. The Phase 2 edits in `content/02–15` are uncommitted. `content/00`, `content/01` and
`tools/` were not touched.

**Role-play.** A sceptical three-person ITiT mid-term committee (an external ML member, a robotics member,
a third ITiT member) plus the SzD office's formal check, reading the IPB as it will in **Nov 2027**. The
text was checked against SPEC §4, the 8 criteria of [benchmarks.md §2.1](benchmarks.md), the binding
[pivot-decision.md](pivot-decision.md) (v6 on top) and [review-1](review-1.md), [review-2](review-2.md) and
[review-3](review-3.md), to catch regressions.

**Evidence rule.** Every finding names a file and section. *(reviewer judgement)* marks an assessment, not
a measured fact. No new references, facts about people, labs or dates were added. The one citation
wording change (R4-F1) uses only what [vla-wm-crowdedness.md](vla-wm-crowdedness.md) already records
from the TwinRL abstract.

**Page-limit method.** `tools/build_ipb.py` (Calibri 11 pt, spacing 1): text-length estimate and height in
a Pages.app PDF. `output/` was rebuilt for the check and restored with `git checkout output/`.

---

## 0. Verdict

v6 is the most readable version so far. It has one object (a real-to-sim-to-real method for navigation
models), one thesis sentence, three stages that map 1:1 to RQ1–RQ3/H1–H3, and RQ4/H4 for the whole pipeline.
Each hypothesis has one threshold. There are no model or checkpoint names in §2, §5, §7, §8 or §10, and
manipulation appears only as related work (§6) and future applicability (§12). The review-3 structural
fixes hold: separate captures for twin and "reality", a second reference as a sign check, the real-only
baseline as imitation (not RL from scratch), papers only after their results, and 200-point ITiT venues.

A committee would vote **positive**. The general level of detail is adequate for criteria 3 and 4, with
four gaps that an ML or robotics member would raise. All four are fixed without adding detail:

1. **§6 misdescribed TwinRL [27]** (R4-F1): "fine-tunes such models" referred to world models, but TwinRL
   fine-tunes a pretrained policy in a phone-captured twin.
2. **The physical part of the proxy reality was undefined** (R4-F2). The twin estimates physical
   parameters, H2 randomizes them and H3 corrects them, but it was not said where "reality's" physical
   parameters come from. Without that, stage 1's physics estimation and stage 3's physical correction
   could not fail in the proxy.
3. **The H4 baseline could become a strawman** (R4-F3): "the strongest existing approach ... with the same
   twin" was both contradictory (uniform capture gives a different twin) and open to a weak re-implementation.
4. **P1 (May 2027) promised world-model results** (R4-F4) that stage 2 (Mar–Jul 2027) is unlikely to have
   by then, which is the paper-before-results pattern of review-2/3 in a new form.

The student-owned items from review-1 are **still open** and outside this task: ORCID, start date and
supervisor title in `content/01` (visible `TODO` comments there are HTML comments, not form text), and the
sem. 1–2 rows, which must describe the work actually done.

---

## 1. Scores per mid-term criterion (projected to Nov 2027)

| # | Criterion | Before fixes | After fixes | Why |
|---|---|---|---|---|
| 1 | Progress on the IPB (1–5) | 4 | **4** | Sem. 3–4 depend only on public scans and WCSS/PLGrid, and the robot blocks no hypothesis. Deduction: sem. 1–2 still unconfirmed as actual work (R1-F2). |
| 2 | Submission date realistic? (Y/N) | YES, with reservations | **YES** | 30.09.2029. P1 now reports only what exists by May 2027 (R4-F4). Stage 2 is the heaviest semester (foundation-model init + RL + world model); the world model is scheduled after the first H2 result, and RL runs on a subset of scenes (R4-F9). |
| 3 | Hypotheses properly formulated? (Y/N) | YES | **YES** | Thesis + H1–H4, one threshold each, all decided on the proxy reality. H1's unit (views) and H4's comparator are now unambiguous (R4-F3, R4-F6). |
| 4 | Suitability of methods (1–5) | 3 | **4** | Stage → method → comparators → criterion is visible for every H. The physical gap in the proxy is now defined and stated as synthetic (R4-F2). Deduction: tier-A-style proxy remains a proxy (see §4), and the foundation/world-model parts are unproven in compute until T3.1 *(reviewer judgement)*. |
| 5 | Relevance of results (1–5) | 4 | **4** (projected) | Every sem. 3–4 task feeds H1/H2 and P1. |
| 6 | Quality of carrying out tasks (1–5) | 4 | **4** (projected) | Dated deliverables: Nov 2026, Jan 2027, Feb 2027, Apr 2027, May 2027, Jul 2027, Sep 2027. |
| 7 | Original contribution (1–5) | 3 | **3–4** | Novelty = the real-data budget of the whole loop, stated against navigation twins [11–13], RialTo [14], TwinRL [27], VLAW [28] and view selection [17–20]. It rests on the combination and the measured saving, not on a new primitive, and the area is crowded (§12 risk) *(reviewer judgement)*. |
| 8 | International? (Y/N) | YES, weak | **YES, weak** | NeurIPS/ICML/CVPR submissions, a summer-school poster, NAWA Bekker planned for sem. 6. No named host or co-author before the mid-term (R3-F13, still open). |

## 2. SPEC §4 checklist (office view)

| Item | Status |
|---|---|
| All 15 sections filled (§14 n/a) | PASS |
| §1 ORCID valid | **OPEN** (student; `content/01` not owned; R1-F1) |
| §3 sem. 1–8 each with a concrete output | PASS. Sem. 1–2 still carry a CONFIRM (student) comment (R1-F2). |
| §3 locations, sub-study completion semesters | PASS: H1 Apr 2027, H2 Jul 2027, H3 Jan 2028, H4 Sep 2028; places K46, WCSS, Denali |
| §4 ≤ end of sem. 8 | PASS (30.09.2029) |
| §11 date in §3 and before §4 | PASS (May 2027 = T4.2) |
| §11 venue on the ministerial list | PASS (NeurIPS Lp 87, 200 pts, ITiT); recheck against the 2027 list |
| Every H has a method in §9 and a task in §3 | PASS (see §3 below) |
| §8 contributions trace to §7 | PASS (stages 1–3 ↔ H1–H3, key contribution ↔ H4) |
| §10 PL = EN | PASS (3 paragraphs each, same content, re-read after the Polish edits) |
| Page limits | PASS (see §6) |
| No visible TODO / "to be confirmed" in owned sections | PASS (visible-text scan after stripping HTML comments) |

## 3. Consistency chain after the fixes

| Item | §7 | §9 stage | §3 task(s) | §8 | §11/§12 papers |
|---|---|---|---|---|---|
| RQ1/H1 | ≥ 40% less capture | Stage 1, sem. 3–4 | T3.1, T3.3, T4.1 (H1 by Apr 2027) | stage 1 | P1 NeurIPS 2027 |
| RQ2/H2 | ≥ +10 pp vs uniform DR | Stage 2, sem. 4 | T4.1 (first result Apr 2027, H2 with world model by Jul 2027) | stage 2 | P1 (first H2 results, without the world model) |
| RQ3/H3 | ≥ 50% fewer trials | Stage 3, end sem. 4 – sem. 5 | T4.3, T5.1 (H3 by Jan 2028) | stage 3 | P2 ICML 2028 (CVPR 2028 if H3 done by Nov 2027) |
| RQ4/H4 | ≥ 2× less real data than the strongest existing approach | Whole pipeline, sem. 6 | T6.1 (H4 by Sep 2028) | key contribution | P3 NeurIPS 2028, fallback ICLR 2029 |
| Robot | validates direction only | 2 campaigns | T5.2, T7.1 | — | — |

**Before the fixes:** §11 described P1 as including the world-model extension, while T4.1 gave only a first
H2 result by Apr 2027 (R4-F4). §3 T2.1 still said "evaluation tiers A–C", a term no longer used anywhere
else in the visible text (R4-F7).

**Citation numbering.** §6 cites [1]–[30] in order of first appearance (script check). §9 uses [1, 5, 6, 7,
9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21–24, 25, 26, 27, 29, 30]; §12 uses [8, 11, 27, 28]. All exist.
§5, §7, §8, §10 have no citations. 30 references, within the README's 15–30 guideline.

**Leftover v5/v4 specifics (visible text).** None in §2, §5, §7, §8, §10: no OpenVLA, π0, Octo, Qwen, Cosmos,
NWM, LoRA, TwinRL, checkpoints or C1–C3. §6 names them only as cited works (allowed). §9 names families
only with "e.g." ("a general navigation model or a vision-language-action model [21–24]", "a video world
model [25, 26]"). Manipulation appears only in §6 (RialTo) and §12 (future applicability). "Budget law"
(overclaim flagged in R3-F11) was removed from T6.3.

## 4. Testability and the proxy reality at the general level

| H | Decided on | Real-data unit | Verdict |
|---|---|---|---|
| H1 | budget–P curves, ≥ 4 budgets, ≥ 20 scenes | captured views (operator time reported) | testable; unit now stated (R4-F6) |
| H2 | paired gain on 10 held-out scenes at ≥ 2 budgets | same | testable. It tests the combination (uncertainty-following + world model); the ablations in §9 attribute the gain *(reviewer judgement: acceptable, the hypothesis is about the stage)* |
| H3 | trials-to-target-P curves | real trials, re-captured views counted | testable, now also for physical correction (R4-F2) |
| H4 | budget curves vs a re-implemented existing approach and real-only imitation | operator time | testable; comparator effort equalised (R4-F3) |

**Is the proxy reality described clearly enough?** Yes, at the level v6 asks for. §7 states the principle
in one sentence (public scans, "reality" and twin from separate captures, robot validates direction). §9
gives the construction: laser-scan reference rendered with a robot-camera model, twin from a subset of the
separate phone capture, largest budget below the full capture, a second reference as a sign check, the
proxy's own error reported, and now hidden physical parameters for "reality". The irreducible limitation
(no real lighting changes, motion blur, people, or real actuation) stays as the §12 risk "Proxy reality is
easier than reality", answered by the two robot campaigns.

## 5. Novelty versus existing real-to-sim-to-real navigation work

| Work (§6) | What it does | What the IPB adds |
|---|---|---|
| EmbodiedSplat [11], Vid2Sim [12], GaussGym [13] | Twins from real captures train navigation that transfers | The amount and choice of real data become decisions of the method, at every stage, with measured budget curves |
| RialTo [14] | Twins from small amounts of real data (manipulation) | Budget as the experimental variable; navigation |
| TwinRL [27] | Phone-captured twin targets real rollouts for a fine-tuned policy (manipulation) | Selection of real trials that correct twin and model under one counted budget; comparator in stage 3 and H4 |
| VLAW [28] | Real rollouts improve a world model | Real trials are chosen actively, and the world model is grounded in a twin |
| FisherRF [17], Bayes' Rays [18], risk-aware [19], AREA3D [20] | View selection for reconstruction quality or safe exploration | Objective = P of a navigation model trained in the twin; all are stage 1 comparators |

§6's gap and §8's "To our knowledge, the first ... one budget" are consistent with this table and hedged.
The claim is defensible if H4's comparator is strong, hence R4-F3.

## 6. Page limits (build_ipb.py, after the fixes)

| § | Limit | est. | PDF | Note |
|---|---|---|---|---|
| 5 | 1 | 0.85 | 0.74 | ok |
| 6 | 2 | 1.56 | 1.39 | ok |
| 7 | 1 | 0.75 | 0.63 | ok |
| 8 | 1 | 0.89 | 0.73 | ok |
| 9 | 2 | 1.61 | 1.42 | ok (was 1.53/1.35 before R4-F2/F3/F5/F6/F9) |
| 10 | 1 each | 0.50 / 0.49 | 0.44 / 0.39 | ok |
| 12 | 1 | 0.99 | 0.85 | tight (estimate); unchanged here. Check in Word; do not add text |

## 7. Numbered fixes and status

Severity: **P0** = must fix before signing. **P1** = affects a mid-term criterion directly. **P2** = polish.
Status: **done** = applied in `content/`. **open (student)** = needs the student's facts or a file this task
does not own. **no change** = deliberately not applied, with the reason.

### P0

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R1-F1 | ORCID, start date, supervisor title (review-1, still open). | — | 01 | **open (student)** |
| R1-F2 | Sem. 1–2 must state what was actually done (review-1, still open). | — | 03 | **open (student)** |

No new P0 in the owned sections.

### P1

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R4-F1 | §6 said recent work "fine-tunes such models [world models] in a twin ... [27]". TwinRL fine-tunes a pretrained policy in a phone-captured twin and uses the twin to target real rollouts. A factual misdescription of the closest work. | "fine-tunes a pretrained policy in a twin reconstructed from a phone capture and uses the twin to target real rollouts [27]". | 06 | **done** |
| R4-F2 | The physical part of the proxy reality was undefined. Stage 1 estimates physical parameters, H2 randomizes per physical parameter, H3 corrects them, but "reality" in Habitat shares the twin's physics, so those parts could not fail. | §9 protocol: "reality" has its own physical parameters (e.g. actuation noise), hidden from the method and learned only from counted real data; the physical gap is synthetic and the robot checks it. | 09 | **done** |
| R4-F3 | H4 comparator: "the strongest existing approach ... with the same twin" is contradictory (uniform capture gives another twin) and invites a weak re-implementation (the R3-F2 strawman risk in a new place). | "re-implemented for navigation and tuned with the same effort as the method ... with the same reconstruction pipeline, learner and correction". | 09 | **done** |
| R4-F4 | Paper before results: §11 described P1 (May 2027) as including the world-model extension, but T4.1 gives only a first H2 result by Apr 2027, and stage 2 starts in Mar 2027. | §11: P1 = H1 + first H2 results (uncertainty-following training). T4.1: first H2 result = uncertainty-following training (Apr 2027); H2 completed with the world-model extension (Jul 2027). §7 H2 and §8 unchanged (they describe the full stage). | 11, 03 | **done** |
| R4-F5 | §9 tasks "image-goal and instruction-following": ScanNet++ scenes have no navigation instructions, so this adds an unplanned data dependency to sem. 3. | "e.g. image-goal and point-goal; instruction-following where instructions are available". | 09 | **done** |
| R4-F6 | H1 unit ambiguous: §7 counts real data in one operator-time cost, H1 says "less capture" (review-3 R3-F5 had decided H1 on views). | §9 H1 criterion: "less capture (in views; operator time also reported)". | 09 | **done** |
| R4-F7 | Leftovers in §3: T2.1 "evaluation tiers A–C" (term no longer defined anywhere visible); T3.1 "below the P ceiling" (unclear); T6.3 working title "budget law" (overclaim, R3-F11). | "a proxy-reality evaluation protocol"; "so that P stays below its ceiling"; working title removed. | 03 | **done** |
| R3-F13 | Criterion 8 still weak: no named host or foreign co-author before the mid-term. | — (needs real contacts; §12 already says "not yet contacted"). | 12 | **open (student/supervisor)** |

### P2

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R4-F8 | H2 bundles uncertainty-following training and the world model against uniform DR, so a pass does not say which part helped. | No change to §7: v6 asks for simple hypotheses about stages. §9 already lists ablations without the world model, uncertainty weighting and foundation-model initialization. | — | **no change** |
| R4-F9 | Sem. 4 feasibility: foundation-model init, imitation, RL and world-model adaptation in one stage. | §9: RL "on a subset of scenes" (restores R3-F9's intent); world model after the first H2 result (R4-F4). | 09, 03 | **done** |
| R4-F10 | §8 stage 1: "for both appearance and geometry and the physical properties" (clumsy). | "for appearance, geometry and the physical properties". | 08 | **done** |
| R4-F11 | §2 PL title: "metoda rzeczywistość–symulacja–rzeczywistość" reads as a bare apposition. | "metoda typu rzeczywistość–symulacja–rzeczywistość" (EN unchanged). | 02 | **done** |
| R4-F12 | §10 PL: missing comma around "zamiast nagrywać wszystko po równo"; "pomiar, ile prawdziwych danych oszczędza" has no explicit subject. | Comma added; "pomiar tego, ile prawdziwych danych pozwala ona zaoszczędzić". Content still equals EN. | 10 | **done** |
| R4-F13 | §10 says the software "will be made publicly available", §9 says "where dataset and model licences permit". | No change: the abstract is for the general public and the licence caveat is in §9/§12. | — | **no change** |
| R4-F14 | §12 is at 0.99 (estimate) of its page. | No text added to §12. Check in Word before printing. | — | **no change** (monitor) |

## 8. Questions to prepare for the 15-minute talk

1. Your "reality" is a render of a laser scan with synthetic physics. Did H1–H3 keep their sign on the
   robot? (R4-F2)
2. How did you make sure the re-implemented existing approach was as well tuned as your method? (R4-F3)
3. What does the world model add beyond the uncertainty-following training, according to your ablation?
   (R4-F8)
4. How does your stage 3 differ from TwinRL's twin-targeted rollouts? (R4-F1, §5 above)
5. What was actually done in year 1? (R1-F2)

## 9. Handover

- Edited (uncommitted): `content/02, 03, 06, 08, 09, 10, 11`. Not edited: `content/04, 05, 07, 12–15`
  (reviewed, no change needed), `content/00, 01`, `tools/`.
- RQ/H numbering, all thresholds (40%, +10 pp, 50%, 2×), dates, venues and the reference list are
  unchanged. No new citation was added.
- `output/` was regenerated for the page check and restored with `git checkout output/`; the owner of
  `output/` must rebuild it after these edits.

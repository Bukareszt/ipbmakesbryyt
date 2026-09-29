# Review 2 — mock mid-term committee review of the pivoted IPB

Issue #24 · 2026-09-26 · reviewed state: branch `ipb-draft`, commit 5665799 (Wave 9, representation-level
thesis), all `content/*.md`. Phase 2 edits in `content/02–15` are uncommitted; `content/00`, `content/01`
and `tools/` were not touched.

**Role-play.** A sceptical three-person ITiT mid-term committee: an ML member (external, from another
university), a computer-vision member and a robotics member. It also includes the SzD office's formal check.
The committee reads the IPB as it will in **Nov 2027**, against SPEC §4, the 8 criteria of
[benchmarks.md §2.1](benchmarks.md), the binding [pivot-decision.md](pivot-decision.md) and
[review-1.md](review-1.md).

**Evidence rule.** Every finding names a file and section. *(reviewer calculation)* marks my own
arithmetic. Citation claims were re-checked where the committee is likely to ask (arXiv API, 2026-09-26:
2301.12780 Navon, 2403.12143 Kofinas, 2510.15352 GaussGym, 2604.13645 Lei, 2509.18631 Cheng). No new facts
about people, labs or dates were added; nothing new is claimed as agreed.

**Page-limit method.** `tools/build_ipb.py` (Calibri 11 pt, spacing 1; text estimate + Pages.app PDF).

---

## 0. Verdict

The pivot has worked. The thesis is sharper and more clearly **ITiT/ML** than the robotics-first plan. It
has one object (internal representations), four RQs that follow one another (measure → predict → use →
generalize), numeric decision rules, and **every hypothesis can be decided without an own robot** (tier A).
Review-1's structural problems stay fixed: one venue family, visit length matches the funder, the robot is
validation only, and the page limits hold. A committee would vote **positive** today.

Five issues would have cost points or produced a split vote on criterion 2 or 3. All five are now fixed in
`content/`:
1. **H4 could not be tested as written.** An own ManiSkill3 twin-trained zoo has **no real outcomes**.
   SIMPLER's paired sim/real results exist only for the published checkpoints it evaluated. (R2-F2)
2. **§11 promised more than sem. 3 to Apr 2027 can deliver.** P1 (May 2027) was to report localization
   "inside twin-trained policies", but those policies and the zoo were scheduled "by Sep 2027". (R2-F3)
3. **P3 was due before its own experiments.** NeurIPS 2028 (~May) or ECCV 2028 (~Mar) was planned, yet
   H3–H4 were to be "completed" by Sep 2028, and Stage III was to start only in sem. 6. (R2-F4)
4. **A returned review-1 issue.** §7 visible text said "to be confirmed with the supervisor" (review-1 F5).
   (R2-F1)
5. **Two operationalization holes that an ML member will probe:**
   - H2(b) failure coverage "on tier B". Offline real datasets have no closed-loop failure labels. (R2-F5)
   - "Simulator-level predictivity" is not a per-policy predictor. (R2-F6)

Student-owned P0s from review-1 are **still open** and outside this task: ORCID and start date in
`content/01`, and the sem. 1–2 rows that must describe the work actually done (CONFIRM comments in `03`).

---

## 1. Scores per mid-term criterion (projected to Nov 2027)

| # | Criterion | Before fixes | After fixes | Why |
|---|---|---|---|---|
| 1 | Progress on the IPB (1–5) | 3 | **4** | Sem. 3–4 tasks are checkable and depend only on public data and WCSS. The only external dependency, the robot (T3.2), no longer blocks any hypothesis. The deduction is for sem. 1–2, which are still unconfirmed as actual work. |
| 2 | Submission date realistic? (Y/N) | YES, with reservations | **YES** | 30.09.2029. The P1 and P3 timing clashes (R2-F3, R2-F4) are resolved. Sem. 4 is still heavy: ≥ 200-policy zoo + P1 + grants. The sem. 3 pilot that fixes the zoo size is the safeguard. |
| 3 | Hypotheses properly formulated? (Y/N) | YES, but H4 was not testable | **YES** | Thesis + RQ1–RQ4 + numeric rules, α, Holm, pre-registration. H4 is now tied to data that exist, with n chosen so that ρ ≥ 0.5 can be significant. H3 uses one cost unit. |
| 4 | Suitability of methods (1–5) | 4 | **4** | Organised by stage. The proxy-reality check (R2-F7) answers the obvious "your 'real' is a render" objection. The deduction: tier A is still a proxy, and the 3DGS-in-simulator RL throughput is unproven until the T3.1/T3.3 pilot. |
| 5 | Relevance of results (1–5) | 4 | **4** (projected) | Every sem. 3–4 task feeds H1 or H2. |
| 6 | Quality of carrying out tasks (1–5) | 3 | **4** (projected) | Deliverables carry dates (Nov 2026, Feb 2027, Apr 2027, Sep 2027). |
| 7 | Original contribution (1–5) | 4 | **4** | A representation-level account of twin-to-real transfer and weight-space learning on policies are both thin in the literature (novelty-options §3, niches-map). §8 no longer presupposes positive results (R2-F9). |
| 8 | International? (Y/N) | YES, weak | **YES, weak** | Before the mid-term: a NeurIPS submission, a summer-school poster and a foreign co-author "sought". The visit is after the mid-term. The European host search now targets the community closest to RQ2 (R2-F11). Naming a real host or co-author before signing is the only thing that would change this to a clear YES (student/supervisor). |

## 2. SPEC §4 checklist (office view)

| Item | Status |
|---|---|
| All 15 sections filled (§14 n/a) | PASS |
| §1 ORCID valid | **OPEN** (student; `content/01` not owned; review-1 F1 still open) |
| §3 sem. 1–8 each with a concrete output | PASS. Sem. 1–2 still carry CONFIRM (student) comments (review-1 F2). |
| §3 locations, sub-study completion semesters | PASS. H1 Sep 2027, H2 sem. 5, H3 Apr 2028, H4 Sep 2028. |
| §4 ≤ end of sem. 8 | PASS (30.09.2029) |
| §11 date in §3 and before §4 | PASS (May 2027 = T4.2) |
| §11 venue on the ministerial list | PASS (NeurIPS Lp 87, 200 pts, ITiT). The D&B-track proceedings question stays as a CONFIRM comment. |
| Every H has a method in §9 and a task in §3 | PASS after R2-F2, R2-F5 (was FAIL for H4) |
| §8 contributions trace to §7 | PASS (items 1–4 ↔ H1–H4, item 5 = assets) |
| §10 PL = EN | PASS (re-checked; the R2-F14 change was made in both) |
| Page limits | PASS, tight (see §5) |
| No visible TODO / "to be confirmed" | PASS after R2-F1 |

## 3. Consistency chain after fixes

| Item | §7 | §9 stage | §3 task(s) | §8 | §11/§12 papers |
|---|---|---|---|---|---|
| RQ1/H1 | measure/localize | I, sem. 3–4 | T3.1, T3.3, T4.1 (H1 by Sep 2027) | 1 | P1 NeurIPS 2027 (H1 a–c + first d) |
| RQ2/H2 | predict | II, sem. 4–5 | T4.1 (zoo), T5.1 (H2), T5.2 (tier C) | 2 | P2 CVPR/ICLR 2028 |
| RQ3/H3 | use | III, sem. 5–6 | T5.1 (set-up), T6.1a (H3 by Apr 2028) | 3 | P3 NeurIPS 2028 |
| RQ4/H4 | generalize | IV, sem. 6 | T6.1b (H4 by Sep 2028) | 4 | P3 (first results) / P4 or dissertation |
| Tier C | validation | 2 campaigns | T5.2, T7.1 | — | — |

Before the fixes: §9 Stage IV said sem. 6–7 while §3 said sem. 6; §3 T5.1 said tier B for H2(b) while §7's
decision rule decides on tier A; and §8, §12 and §3 listed ECCV 2028 for P3.

**Citation numbering after the §6 renumbering.** Every bracketed citation in visible text was checked:
§9 uses [1, 6, 9, 10, 12, 17–21, 26–35], §12 uses [4] and [25–27], and §5, §7, §8 have none. All point to the
intended works in the 35-item list. The old numbers ([37], [38]) survive only inside a Wave 6 HTML comment
in `03`, which is not printed.

**Leftover pre-pivot wording.** None in the visible text of §5–§12. No H2 "alignment", no "twin beats
generic", no RA-L/IROS, no "reusable twin pipeline" as a contribution. Sem. 1 T1.2 ("how much real data
sim-to-real transfer needs") is pre-pivot but describes what was done in sem. 1. The pivot keeps sem. 1–2 as
they are, so it stays: it shows the path to the thesis.

**Robotics-first wording.** §5 and §8 place the work in ML/ITiT, and the robot is validation only. The
application list in §5 is still robot-heavy, which is appropriate for "application areas".

## 4. Testability without an own robot

| H | Decided on | Real signal | Verdict |
|---|---|---|---|
| H1 (a–c) | tier A | real images of public scenes (e.g. ScanNet++) paired with twin renders | testable |
| H1 (d), H2, H3 | tier A | closed-loop rollouts in the rendered reference scan (proxy reality) | testable. Validity rests on the proxy, so R2-F7 adds a measured proxy gap. |
| H2 (b) | tier A | failures in proxy-reality rollouts | testable after R2-F5 (tier B has no failure labels) |
| H4 (a–b) | tier B | published paired sim/real results of public manipulation policies (SIMPLER) | testable after R2-F2, and only if ≥ 12 policy–task pairs with released checkpoints exist (re-read in T6.1) |

## 5. Page limits (build_ipb.py, after fixes)

| § | Limit | est. | PDF | Note |
|---|---|---|---|---|
| 5 | 1 | 0.90 | 0.82 | ok |
| 6 | 2 | 1.98 | 1.61 | ok, tight on the estimate |
| 7 | 1 | 0.99 | 0.88 | tight; do not add text |
| 8 | 1 | 0.98 | 0.83 | ok |
| 9 | 2 | 1.75 | 1.57 | ok |
| 10 | 1 each | 0.52 | 0.46/0.44 | ok |
| 12 | 1 | 0.98 | 0.97 | tight: was 1.02 after R2-F11/F15, then trimmed (R2-F16) |

## 6. Numbered fixes and status

Severity: **P0** = must fix before signing. **P1** = affects a mid-term criterion directly. **P2** = polish.
Status: **done** = applied in `content/`. **open (student)** = needs the student's facts or a file this task
doesn't own.

### P0

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R2-F1 | §7 visible "All thresholds are design choices to be confirmed with the supervisor". This is review-1 F5 coming back: the supervisor signs the document. | "…design choices fixed in that pre-registration." | 07 | **done** |
| R2-F2 | H4 not testable as written. A ManiSkill3 twin-trained zoo has no real outcomes, and SIMPLER's paired sim/real results cover only the checkpoints it evaluated. A weight-space predictor also cannot take different architectures "without retraining". Also, ρ ≥ 0.5 is significant (one-sided α = 0.05) only from n ≈ 12 *(reviewer calculation; critical ρ ≈ 0.56 at n = 10, ≈ 0.50 at n = 12)*. | §7 H4(a): published paired sim/real results, ≥ 12 policy–task pairs. §9 Stage IV: manipulation set = public policies in the SIMPLER replicas; the architecture-agnostic hidden-state predictor; limitation stated (these policies are trained on real data). §3 T6.1(b) the same. Threshold unchanged. | 07, 09, 03 | **done** |
| R2-F3 | §11/§3: P1 (May 2027) claims localization inside twin-trained policies, but T4.1 delivers the policies and zoo by Sep 2027. | T4.1: first robustness-vs-transfer result by Apr 2027. T4.2 and §11: P1 = H1(a–c) + first H1(d). H1 completion stays at Sep 2027. | 03, 11 | **done** |
| R2-F4 | P3 (NeurIPS ~May 2028 / ECCV ~Mar 2028) was due before H3–H4 were complete (Sep 2028), and Stage III started only in sem. 6. | Stage III set-up moved to Jan–Feb 2028 (T5.1). H3 by Apr 2028, H4 by Sep 2028. P3 = NeurIPS 2028 with H3 and the first H4 results, fallback ICLR 2029. ECCV 2028 dropped. The same change in §8 and §12. Deviation from pivot-decision.md's "ECCV 2028 or NeurIPS 2028" recorded here: ECCV's expected ~Mar 2028 deadline falls in the first month of Stage III. | 03, 08, 09, 12 | **done** (coordinator to note the venue change) |
| R1-F1 | ORCID, start date, supervisor title (review-1, still open). | — | 01 | **open (student)** |
| R1-F2 | Sem. 1–2 must state what was actually done (review-1, still open; CONFIRM comments). | — | 03 | **open (student)** |

### P1

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R2-F5 | H2(b) coverage "on tier B" (§3 T5.1, §9). Offline real datasets give no closed-loop failure labels for the student's policies, and §7 decides on tier A anyway. | Coverage measured on tier A proxy-reality rollouts; tier C reports agreement. | 03, 09 | **done** |
| R2-F6 | H2 baseline "simulator-level predictivity" is a correlation over a set of models (SRCC), not a per-policy prediction. | Defined as real SR predicted from twin SR by the sim-to-real mapping fitted on the training scenes [10]. | 09 | **done** |
| R2-F7 | Tier A "real" closed-loop outcomes are renders of a laser scan. The ML member will say the measured gap is twin-vs-scan-render. | §9: frame-level measures use real images, and the scan-render-vs-real gap is measured with the same CKA/probe tools, so the proxy's own error is reported. | 09 | **done** |
| R2-F8 | H3 adds capture minutes and real rollouts, which are different units. | One operator-time cost with a pre-registered conversion rate (§7, §9). | 07, 09 | **done** |
| R2-F9 | Overclaims. §5: image-quality scores "are known to track real performance poorly" (the evidence is Truong et al. on simulator fidelity, not reconstruction scores). §8: "first demonstration", "Showing that" presuppose positive results. §6: "no study has measured" rests on S2 counts. §6: [26] Navon et al. said to "predict generalization", but its abstract doesn't claim this. | §5 "need not track real performance (lower-fidelity simulation can even transfer better)". §8 "first systematic test of whether", "Testing whether". §6 "we found no study that measured". §6 [26] "learn directly on weights", with generalization kept for [27] (abstract verified). | 05, 06, 08 | **done** |
| R2-F10 | §9 Stage IV "sem. 6–7" vs §3 sem. 6. After R2-F4, Stage III spans sem. 5–6. | §9 headers aligned with §3. | 09 | **done** |
| R2-F11 | Criterion 8: both named hosts are US 3DGS/navigation groups, which fit the pre-pivot topic. The Erasmus+ route needs a European host. | §12: the European host is sought in the weight-space learning community (authors of §6 [25–27]); no person is named because none is contacted. Naming a real host or co-author before the mid-term is **open (student/supervisor)**. | 12 | **done** (text); host open |
| R2-F12 | The autoreferat (~mid-Oct 2027) was listed in the sem. 4 row, but it falls in sem. 5. | Moved to the sem. 5 row, next to the mid-term. | 03 | **done** |

### P2

| # | Finding | Fix | Files | Status |
|---|---|---|---|---|
| R2-F13 | Stage II predictor input: "without real rollouts" does not forbid unlabelled real frames of the capture, which link RQ1 to RQ2. | §9: the probe set may include unlabelled real frames of the capture. | 09 | **done** |
| R2-F14 | "Millions of trials" (§5, §10) is unsourced in the visible text and not true for imitation-learned manipulation. | §5 dropped; §10 "bardzo wielu prób" / "a very large number of trials" (PL = EN). | 05, 10 | **done** |
| R2-F15 | §12: the Bekker application is T4.3 (year 2) but was listed in year 3. §8 named ICML/ICCV/ECCV as targets although no paper targets them. | Bekker moved to year 2. §8: "NeurIPS, ICLR, CVPR, with ICML, ICCV and ECCV for resubmissions". | 08, 12 | **done** |
| R2-F16 | §12 went to 1.02 pages after R2-F11/F15. | Shortened the header line, the scooping risk and the rejection risk; the "changing venue points" risk is folded into the header (re-check against the new list). | 12 | **done** (0.97 PDF) |
| R2-F17 | Sem. 4 is the heaviest semester: ≥ 200-policy zoo, H1, P1, three applications and a poster. | No text change. The sem. 3 pilot (T3.3) fixes the zoo size, and §12 lists the risk. Watch at the Feb 2027 checkpoint. | — | **no change** (monitor) |
| R2-F18 | 3DGS rendering inside an RL simulator (Habitat vs an Isaac-based renderer) is unproven at zoo scale. | Covered by the T3.1 choice and the "zoo too small" risk; no text change, to protect the §12 page limit. | — | **no change** |

## 7. Questions to prepare for the 15-minute talk

1. Your "reality" in tier A is a rendered laser scan. How big is its own gap to real images? (R2-F7)
2. The manipulation policies in H4 were trained on real data, not in twins. Why is that still a test of
   RQ4? (R2-F2)
3. Why should a predictor trained on navigation policies transfer to VLA-scale manipulation policies
   without retraining? What exactly is its input? (R2-F2, R2-F13)
4. How is this different from Lei et al. [16] (representation alignment in co-training) and SAFE [30]
   (failure features in VLAs)?
5. How many GPU-hours did the ≥ 200-policy zoo take, and what did the pilot fix?
6. What was actually done in year 1? (R1-F2)

## 8. Handover

- `output/*.docx|pdf` were regenerated by `tools/build_ipb.py` for the page check and then restored, so
  the owner of `output/` must rebuild them after these edits.
- For the coordinator: R2-F4 changes the P3 venue options relative to pivot-decision.md (ECCV 2028 dropped;
  ICLR 2029 added as fallback). RQ/H numbering and all pivot thresholds are unchanged.

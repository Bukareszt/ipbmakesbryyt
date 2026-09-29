# Review 1 — mock mid-term committee review of the full IPB

Issue #7 · 2026-09-26 · owner: Wave3-G worker · reviewed state: branch `ipb-draft`, commit 71c4707
(Wave 2), all `content/*.md`.

**Role-play.** This is a sceptical ITiT committee of three: an ML/CV member, a robotics member, and an
external member from another university. It also includes the SzD office's formal check. The committee
reads the IPB now, but scores it **as the mid-term committee will in Nov 2027**, using the 8 criteria in
[benchmarks.md §2.1](benchmarks.md) and the recurring remarks in §2.2. `content/` was **not edited**.

**Evidence rule.** Every finding cites a file and line or a section. Numbers marked *(reviewer estimate)*
are my own calculations from the stated protocol, not sourced facts. No new facts about people, labs or
dates are introduced here. Anything not already in `research/` is marked **verify**.

**Page-limit method.** ~480 words per page at 11 pt, spacing 1 (from the issue). Words were counted with
HTML comments stripped (`perl -0pe 's/<!--.*?-->//gs' | wc -w`). Tables, bullets and headings take more
space than running text, so borderline sections must be checked in `ipb.docx`.

---

## 0. Verdict in one paragraph

The IPB is **well above the ITiT median** we saw in R1–R5. It has a thesis sentence, operational
hypotheses with decision rules, stage-by-stage methods, a risk table, and a venue plan that uses listed
venues. As it stands, a committee would vote **positive**. The main reservations are:
1. **Honesty and checkability of semesters 1–2.** Both rows are still flagged `CONFIRM: actual work`.
2. **An overloaded semester 3.** It holds the pipeline, a test stand that is not yet agreed, the first real
   robot run, and an RA-L paper, all by Feb 2027, on hardware that is not secured.
3. **An underpowered H1 non-inferiority test** at 60 episodes per arm.
4. **Venue lists that disagree** across §3, §8, §9 and §12.
5. **The closest competitor is missing from §6.** EmbodiedSplat is named in §12 but not in §6.
6. **Formal gaps before filing:** ORCID, §14/§15, TODO markers, and visible "to be confirmed with the
   supervisor" text.

Items 1, 2 and 6 are what turn a clean positive into "positive with reservations" or a split vote on
criterion 2 (R5 p. 14, p. 16).

---

## 1. Scores per mid-term criterion (projected to Nov 2027)

Criteria 1, 5, 6 and 7 judge *results*, which don't exist yet. For these the score says how well the IPB
**sets the student up** to score well: are the sem. 1–4 tasks checkable, achievable and relevant?

| # | Criterion (form S8) | Score | Why | Fixes that raise it |
|---|---|---|---|---|
| 1 | Degree of progress on the IPB (1–5) | **3 / 5** | Sem. 1–2 are written as a plan, not as done work (`03-schedule.md` sem. 1–2, `CONFIRM` markers). Sem. 3 has three heavy tasks, two of which depend on unconfirmed external hardware (T3.2 → K29, sensor via Minigrant). At the mid-term the autoreferat % table will likely show T3.2/T3.3 below 100%. | F2, F6, F7 |
| 2 | Is the submission date realistic? (Y/N) | **YES, with reservations** | 30.09.2029 is the recommended value (S11). The risk is the chain of dependencies: the K29 agreement, then a sensor, then the pilot, then the RA-L paper, then H1 in ≥ 2 environments by sem. 4. The real-robot load (~700+ episodes in sem. 4, see F9) isn't budgeted. | F6, F7, F9 |
| 3 | Hypotheses properly formulated? (Y/N) | **YES** | Thesis sentence, core vs. extensions, metric, test and decision rule per H (`07` l. 3–43). The weak points are statistical power (F8) and an undefined real-data-only baseline (F10), which a robotics member *will* ask about. | F8, F10, F21 |
| 4 | Suitability of methods (1–5) | **4 / 5** | Stage-based method → data → metric → success criterion (`09`), SRCC validation, fallback. It loses a point for the unconfirmed test stand, the vague Stage I success criterion, and the undecided simulator (Isaac vs. Habitat) even though T1.2 claims a tool-selection note. | F7, F10, F17, F18 |
| 5 | Relevance of results to the dissertation (1–5) | **4 / 5** (projected) | Every sem. 3–4 task maps to the core RQ1–RQ2/H1+H4. The only off-core item is the pre-PhD ACL paper, which is correctly kept as background only (`12`). | — |
| 6 | Quality of carrying out IPB tasks (1–5) | **3 / 5** (projected) | The tasks have deliverables, but several can't reach 100% without external decisions (K29, Minigrant, Bekker). "H1 completed" by sem. 4 is ambitious. | F6, F7, F9 |
| 7 | Original contribution to the discipline (1–5) | **4 / 5** | A clear core contribution (the real-data-budget study) framed in ITiT terms (`08`). The external member will ask how it differs from **EmbodiedSplat (ICCV 2025)**, which §12 itself calls "a real-to-sim-to-real indoor-navigation method using Gaussian splats" but §6 doesn't cite. The novelty claim ("to our knowledge, none measures…") hasn't been checked against that paper. | F11 |
| 8 | International? (Y/N) | **YES, weak** | Before the mid-term there is only an international-venue submission (RA-L) and a poster at a summer/winter school (T4.2). The visit comes after the mid-term (sem. 6), both hosts are in the USA and not contacted, and the planned funder (Bekker) requires ≥ 3 months, which conflicts with "1–3 months". | F12, F13 |

---

## 2. SPEC §4 acceptance checklist (office view)

| Item | Status | Note |
|---|---|---|
| All 15 sections filled (§14 n/a) | **FAIL** | There is no `content/14-*.md` or `content/15-*.md`. §14 ("—"/n/a) and §15 (date, signatures) must be in the docx. → F4 |
| §1 ORCID valid; external supervisors' affiliation | **FAIL** | ORCID is an unconfirmed candidate (`01` l. 10, 20–30). The supervisor is internal (OK). → F1 |
| §3 has sem. 1–8, each with a concrete output | PASS | Every row has T/D items. |
| §3 names locations and sub-study completion semesters | PASS, partly | H1 by sem. 4, H2 by sem. 6, H4 by sem. 7. **H3's completion semester isn't marked.** → F19 |
| §4 ≤ end of sem. 8 | PASS | 30.09.2029. |
| §11 date appears in §3 and is before §4 | PASS | Feb 2027 = T3.3. |
| §11 venue is on the ministerial list | PASS (2024 list) | RA-L 200 / IROS 140. The 2027 list is still pending (known and noted). |
| Every H in §7 has a method in §9 and a task in §3 | PASS, with one mismatch | §3 sem. 3 header lists H3 in Stage I; §9 puts H3 in Stage III. → F19 |
| §8 contributions trace to §7 | PASS | Items 1–4 map to H4, H1, H2, H3. |
| §10 PL = EN | PASS | Checked paragraph by paragraph: same content (PL 270 / EN 317 words). |
| Page limits | **AT RISK** | §6, §9 and §12 are at or over the limit (see §4 below). → F14, F15, F16 |
| Supervisor reviewed and approved | **OPEN** | Visible text still says "to be confirmed with the supervisor" (`03` T3.2, `09` l. 9). → F5 |
| Signed and submitted by 30.09.2026 | **OPEN** | 4 days left (benchmarks P0 #1). |

---

## 3. Cross-section consistency

### 3.1 RQ/H ↔ §9 stages ↔ §3 tasks ↔ §11 ↔ §12

| Item | §7 | §9 | §3 | §8 | §12 | Status |
|---|---|---|---|---|---|---|
| H1 (core) | RQ1 | Stage II, sem. 3–4 | sem. 4 T4.1 "H1 completed"; pilot T3.2 | item 2 | — | OK |
| H4 (core) | RQ2 | Stage III (+IV), sem. 5–7 | T5.2, T7.1 "H4 completed" | item 1 | — | OK |
| H3 | RQ4 | **Stage III**, sem. 5 | T5.1; but the **sem. 3 header says "Stage I (RQ1, H1, H3)"** | item 4 | risk "sim-to-real validation fails (4–5)" | **Mismatch** (F19) |
| H2 | RQ3 | Stage IV, sem. 6–7 | T6.1 "H2 completed" | item 3 | — | OK |
| §11 article | — | — | T3.3 RA-L, Feb 2027 | RA-L/IROS | Year 2 RA-L Feb 2027 | OK |
| Mid-term date | — | — | sem. 5 "Nov 2027" | — | "Mid-term evaluation" (year 3) | `01` says "~October 2027"; the `11` comment says "(Oct 2027)" (F20) |

### 3.2 Venue lists (the known mismatch, confirmed and widened)

| Where | Venues named |
|---|---|
| §3 (`03` T3.3, T5.3, T6.3, T7.3) | RA-L, IROS 2027, **RSS 2028**, IROS 2028, **RAS** |
| §8 (`08` "Dissemination") | RA-L, IROS |
| §9 (`09` last paragraph) | RA-L, RSS, IROS, RAS |
| §11 | RA-L (IROS 2027 option), fallback IROS |
| §12 table (`12` l. 10–11) | Year 3: **RAS or RA-L; RSS or CVPR/ICCV/ECCV**. Year 4: **IEEE T-RO or RA-L** |

Problems:
- (a) §12 year 3 names CVPR/ICCV/ECCV, and year 4 names T-RO. **Neither appears in §3.**
- (b) §12 year 3 has no IROS 2028, even though §3 T6.3 plans it.
- (c) §12 year 3 has a RAS journal article, but §3 puts RAS in **sem. 7 = year 4**.
- (d) §12 year 4 says T-RO, but §3 sem. 7 says RAS/RA-L.

The autoreferat will copy §3, and the committee will check §12 against it. → F3.

---

## 4. Page limits (visible words, comments stripped)

| Section | Limit | Words | ≈ pages | Verdict |
|---|---|---|---|---|
| §5 | 1 | 419 | 0.87 | OK |
| §6 | 2 | **1057** (body 537 + 31 refs) | **2.2** | **Over.** The references alone are ~520 words. → F14 |
| §7 | 1 | 456 | 0.95 | Tight: many short paragraphs. Check in the docx. |
| §8 | 1 | 378 | 0.79 (+ numbered list) | OK |
| §9 | 2 | 930 | 1.94 + ~25 bullet/heading lines | **Likely over.** → F15 |
| §10 | 1 each | PL 270 / EN 317 | 0.6 / 0.7 | OK |
| §12 | 1 | 466 incl. a 4-column table + 5 risk bullets | table wrap → **likely over** | → F16 |

---

## 5. Claims check (unverified claims, overclaiming)

| Claim | Where | Assessment |
|---|---|---|
| "Near-perfect point-goal navigation … billions of frames" | `05` l. 5–6, `06` l. 3–4 | Verified ([5], references-check #5). OK. |
| Vid2Sim "68.3% real-world success-rate gain" | `06` l. 34 | Verified from the abstract (references-check #30). OK. |
| "to our knowledge, none measures how deployed performance depends on the amount of real data" | `06` l. 36–37, `08` l. 8 | This is the author's reading of **abstracts only** (references-check, "Interpretive statements"). **EmbodiedSplat is not in the set checked.** → F11 |
| "The first systematic, quantitative characterization, to our knowledge" | `08` l. 8 | The hedge is fine, but it depends on F11. |
| Thesis: "not worse … while needing at least ten times less real-world data" | `07` l. 3–5 | This is stated as the thesis. H4 has an honest fallback ("Otherwise, the measured budget curve still answers RQ2"), so it's acceptable. See F8 on power. |
| "Real-robot experiments are planned in collaboration with K29 Denali" | `09` l. 7–10, `12`, `03` T3.2 | **Not agreed** (resources §1, "Implication"). The wording must stay "planned". → F5, F7 |
| "Compute: WCSS Lem (NVIDIA H100) and PLGrid allocations" | `09` l. 16 | The infrastructure exists (resources §2). **No allocation has been obtained**, so say "to be applied for". → F17 |
| "with the option to present it at IEEE/RSJ IROS 2027" | `11` l. 5–6 | The RA-L+IROS 2027 window is **UNVERIFIED** (resources §3). → F22 |
| "NAWA Bekker" for a "1–3 months" visit | `03` T4.2/T6.2, `12` table | Bekker 2026 call: stays of **3–24 months** (resources §5). → F13 |
| Sem. 2: "own hand-held RGB-D captures", "first reconstructed scene" | `03` sem. 2 | Unconfirmed (`CONFIRM` marker). It also conflicts with `09` l. 10: "if the lab has no suitable sensor, one will be bought" — so does the student have an RGB-D sensor or not? → F2 |

---

## 6. Numbered fixes

Severity: **P0** = must fix before signing and filing by 30.09.2026. **P1** = strongly recommended
before signing, because it directly affects a mid-term criterion. **P2** = polish.
"Owner" = who has to supply the fact (S = student, SV = supervisor, E = editor, i.e. any agent editing
`content/`).

### P0

**F1 · P0 · `content/01-basic-data.md` (ORCID row, l. 10; start date l. 9; supervisor title l. 11).**
- Replace `0009-0004-6013-0461 <!-- TODO … -->` with the student's **confirmed** ORCID. If there is no
  record, register one today.
- Remove the TODO once the value is confirmed.
- Confirm the start date against the admission decision.
- Confirm "prof. uczelni" (resources §1 lists it; SV confirms).
- Owner: S.
- *Office:* an unverifiable ORCID is a completeness defect.

**F2 · P0 · `content/03-schedule.md` sem. 1 and sem. 2 rows.** Rewrite both rows as **what was actually
done** (Oct 2025 – Sep 2026), in the past tense, with the real deliverable (file, repo path, number of
scenes). Delete the `CONFIRM` markers.
- If T2.1 (a prototype on own RGB-D captures, a first reconstructed scene) was **not** done, move it to
  T3.1 and write sem. 2 as "literature review completed; tool selection; IPB".
- State whether an RGB-D sensor is available. Make `09` l. 10 ("one will be bought") consistent with that
  answer.
- Owner: S.
- *Why:* the autoreferat copies these rows with % completion (S9), and claimed work that wasn't done is
  the most damaging discrepancy (benchmarks P0 #2, R1 p. 39–40).

**F3 · P0 · `content/12-other.md`, planned-outputs table rows "3 (2027/28)" and "4 (2028/29)".** Make the
rows match §3 exactly:
- Year 3 → "Stage II article, RSS 2028 (200) or IEEE RA-L (200), sem. 5; Stage III article, IROS 2028
  (140) or RA-L (200), sem. 6".
- Year 4 → "Summary journal article, Robotics and Autonomous Systems (140) or IEEE RA-L (200), sem. 7".
- Remove **T-RO** and **CVPR/ICCV/ECCV**. If they are wanted, add them to `03` T5.3/T7.3 and `09`
  "Dissemination" as well, so that all four places match.
- Also align `08` "Dissemination" to the same list (RA-L, IROS, RSS, RAS).
- Update the `12` source comment (l. 45–49) to match.
- Owner: E.

**F4 · P0 · new sections §14 and §15 (outside the currently owned files; the coordinator decides where).**
Add §14 "Opinia promotora pomocniczego / Assistant supervisor's opinion: nie dotyczy / n/a" and a §15
block (date; signatures of the doctoral student and the supervisor), for example as
`content/14-assistant-opinion.md` and `content/15-signatures.md`, or directly in the docx.
- *Office:* SPEC §4 item 1; Pr18 point 3.4 checks signatures (S4).
- Owner: E + S.

**F5 · P0 · `content/03-schedule.md` T3.2 and `content/09-methods.md` l. 9 (visible text).** Remove
"*(to be confirmed with the supervisor)*" / "(*to be confirmed with the supervisor*)". The supervisor signs
this document, so the phrase reads as unreviewed.
- If the K29 cooperation is **agreed** by signing: write "in cooperation with the K29 Denali laboratory".
- If it is **not agreed**: use resources §1 option (c), "on a mobile-robot platform available at PWr
  (planned cooperation with K29 Denali; terms agreed in sem. 3)".
- Keep §12 consistent with whichever wording is chosen.
- Strip **all** HTML comments and TODOs when transferring to `ipb.docx`.
- Owner: SV + E.

### P1

**F6 · P1 · `content/03-schedule.md` sem. 3 and `content/11-publication-date.md` (realism of the §11 date).**
In 5 months, sem. 3 requires the pipeline and fidelity report (T3.1), a test stand that isn't agreed,
possibly a sensor purchase, a real-robot pilot (T3.2), **and** an RA-L submission (T3.3). An RA-L paper
built on one pilot scene is thin, and the sensor's funding (Minigrant, next call ~Jan 2027 UNVERIFIED)
arrives too late for sem. 3. Pick one of:
- **(a) Keep Feb 2027** (IROS deadline 1 Mar 2027 is verified). Scope T3.3 explicitly as "Stage I
  pipeline + fidelity validation on ≥ 2 scenes + (if available) the pilot deployment". Add "the real-robot
  pilot is not a precondition for T3.3".
- **(b) Move §11 to ~September 2027** (end of sem. 4). Submit an RA-L paper with H1 results. Keep
  Feb 2027 IROS as an *optional* early paper.

Record the choice in both files. Option (a) is less disruptive. Option (b) is more realistic and still
before the mid-term, but check that the decision timing works with R5 item 6 ("too few publications").
- Owner: SV decides; E edits.

**F7 · P1 · `content/03-schedule.md` T3.2 + `content/12-other.md` risks (test-stand dependency chain).**
Split T3.2 into two items:
- **T3.2a** "written agreement on robot access (K29 or other), sensor decision". D: agreement/e-mail,
  **by Nov 2026**.
- **T3.2b** "pilot deployment in one scene". D: pilot results.

Add an explicit **decision point**: "if no robot access by end of Jan 2027 → fallback (public real-world
datasets + hand-held capture), and the real-robot pilot moves to sem. 4 start". This way a hardware delay
costs one sub-task, not the whole row. (R3 p. 48: a missing test stand appears in a negative
justification; R5 p. 22–23: postponed experiments are a red flag.)
- Owner: E.

**F8 · P1 · `content/07-questions-hypotheses.md` "Common protocol" + H1(b) (statistical power).**
*(reviewer estimate)* With 60 episodes per arm and SR ≈ 0.8, the SE of the SR difference is about 7.3 pp.
- The one-sided 95% lower bound sits ~12 pp below the observed difference.
- If the two policies are truly **equal**, P(lower bound > −10 pp) ≈ **0.4** per environment, or ≈ 0.6
  when both environments are pooled (120 episodes).
- Clustering on start–goal pairs lowers this further.
- So H1(b) would most likely be "not supported" even when the method works.

Fix by doing one or more of:
- (a) decide H1(b) on the **pooled** environments;
- (b) raise to ≥ 150 episodes per arm for the core comparison (e.g. 30 pairs × 5 trials);
- (c) widen δ to 15 pp.

Then add a one-line power statement: "n chosen for ≥ 80% power at δ under SR ≈ baseline". Also make
"lower 95% CI bound" explicit as **one-sided**. The existing TODO (l. 46–49) already asks for a power check,
so close it with numbers.
- Owner: E + SV.
- *Why:* a robotics or statistics member will ask this directly (criterion 3; R4 p. 15: the student
  couldn't explain their own methodology).

**F9 · P1 · `content/09-methods.md` "Test stand and data" + `content/12-other.md` risks (real-robot
workload).** *(reviewer estimate)*
- H1 needs roughly 6 policies (recon, generic, generic+DR, real-only at ≥ 2 budgets, pretrained zero-shot)
  × 60 episodes × 2 environments ≈ **720 real episodes in sem. 4**.
- On top of that comes the real-only training data at ≥ 10× budget.
- H3 needs ≥ 10 policy variants × 60 ≈ **600** real episodes in sem. 5.

Add one sentence with an estimated number of **robot-hours per stage**, and a risk bullet "real-robot
evaluation time exceeds lab access (4–5) → reduce policy variants, automated resets, night sessions,
prioritise H1 core comparisons". Criterion 2 hinges on whether this is feasible on a borrowed robot.
- Owner: E (numbers from S).

**F10 · P1 · `content/07-questions-hypotheses.md` H1/H4 + `content/09-methods.md` Stage II "Baselines"
(undefined baselines).**
- Specify **how** the "policy trained on real robot data" is trained (e.g. behaviour cloning or
  fine-tuning of GNM/ViNT on teleoperated trajectories; on-robot RL is not realistic at these budgets).
- Specify **which** generic simulator scenes the H1(a) baseline uses (dataset name, to be chosen in T1.2).
- For H4, add a rule for when real-only training **never reaches τ** within the maximum feasible budget
  B_max: "then B_real(τ) is reported as > B_max and H4 is evaluated as a lower bound on the ratio".
- Owner: E + S.

**F11 · P1 · `content/06-state-of-the-art.md` (missing closest competitor, novelty claim).**
- Add **EmbodiedSplat** (Chhablani, Ye, Irshad, Kira, ICCV 2025; arXiv 2509.17430, already sourced in
  `12` l. 58). It is a Gaussian-splat real-to-sim-to-real method for **indoor navigation**, which is exactly
  this topic's setting. §6 currently lists only drone, legged and urban examples.
- Add one sentence saying what it does **not** do, **after reading the full paper** (verify: whether it
  varies the real-data amount).
- Also verify the "none measures … amount of real data" sentence against the **full texts** of
  [24]–[31], not only the abstracts (references-check, "Interpretive statements").
- To stay within the page and reference limit, drop one less essential reference (e.g. [4] AirSim or
  [21] Progressive Nets). Log it in `research/references-check.md`.
- Owner: E (verification by S/SV).
- *Why:* the external member's first question will be "how is this different from EmbodiedSplat?", and
  §12 shows that the authors know it (criterion 7; R5 p. 12–13).

**F12 · P1 · `content/03-schedule.md` sem. 3–4 + `content/12-other.md` (international before the
mid-term).** Criterion 8 is weak before Nov 2027. Add at least one **concrete** pre-mid-term
international item that doesn't depend on a US host:
- (a) an Erasmus+ short-term doctoral mobility (5–30 days, continuous recruitment, resources §5) to a
  European lab working on 3DGS or sim-to-real in sem. 4. The host is to be identified by the student, with
  **no name invented here**. Or:
- (b) a named foreign co-author on the Stage I/II paper (if one exists).

Also add one European candidate host next to the two US hosts, so the Erasmus+ route is actually open
(`12` l. 54–55 says Erasmus+ was excluded *because* both hosts are in the USA).
- Owner: S + SV.

**F13 · P1 · `content/03-schedule.md` T6.2 ("1–3 months") + `content/12-other.md` (Bekker).** The Bekker
2026 call allows stays of **3–24 months** (resources §5). Either:
- change T6.2 to "**3 months**" (Bekker), or
- keep "1–3 months" and name a funder that allows short stays (Erasmus+ short-term 5–30 days, or a
  Minigrant research trip), keeping Bekker only for the 3-month variant.

Mark the next Bekker call as UNVERIFIED in the comment.
- Owner: E.

**F14 · P1 · `content/06-state-of-the-art.md` (page limit, 2 pages).** 1057 visible words ≈ 2.2 pages.
Cut ~100 words:
- abbreviate the reference list: "et al." after the first author (already done), venue abbreviations
  (e.g. "Proc. IEEE ICRA" → "ICRA"), no subtitles after colons where the title is identifiable;
- and/or remove 1–2 references (see F11).

Then check in `ipb.docx` at 11 pt / spacing 1.
- Owner: E.

**F15 · P1 · `content/09-methods.md` (page limit, 2 pages).** 930 words plus ~25 bullet and heading lines
is likely more than 2 pages.
- Merge "Statistics and reproducibility" into one sentence that points to §7 (it restates §7's protocol
  almost word for word).
- Merge the per-stage "Success criterion" bullets that only say "decision rules in §7" into the Metric
  bullet.
- Target ≤ 850 words, then check in the docx.
- Owner: E.

**F16 · P1 · `content/12-other.md` (page limit, 1 page).** 466 words, including a 4-column table whose
cells wrap, plus 5 risk bullets, will very likely exceed 1 page.
- Shorten the table cells (venue + points only; drop "IROS 2027 option; fallback IROS (140)", which is
  already in §11).
- Shorten the host descriptions to one line each.
- Shorten "Ethics and data" to one sentence.
- Target ≤ 400 words, then check in the docx.
- Owner: E.

### P2

**F17 · P2 · `content/09-methods.md` l. 16–17 (compute) and Stage I "Method".**
- Write "WCSS Lem (NVIDIA H100) and PLGrid allocations (**to be applied for**)", since no allocation is
  held.
- If T1.2's tool-selection note was really delivered in sem. 1, state the **chosen** simulator instead of
  "Isaac Sim / Isaac Lab or Habitat". Otherwise T1.2 isn't credible as "done" (see F2).
- Owner: E + S.

**F18 · P2 · `content/09-methods.md` Stage I "Success criterion".** "held-out rendering quality is in the
range reported for 3DGS" can't be checked. Give a rule: for example, "PSNR on held-out views within X dB
of the value reported in [23] for comparable indoor scenes, and no collision-mesh holes on the evaluation
paths", with X fixed in the repository before Stage II, like the other margins.
- Owner: E.

**F19 · P2 · `content/03-schedule.md` sem. 3 header and T5.1.**
- Change "Stage I – real-to-sim pipeline (RQ1, H1, H3)" to "(RQ1, H1)". Fidelity metrics feed H3 later,
  but H3 is tested in Stage III, as `09` says.
- Add "(**H3 completed**)" to T5.1's deliverable, so every hypothesis has a completion semester (SPEC §3
  "completion dates of sub-studies").
- Owner: E.

**F20 · P2 · `content/01-basic-data.md` "Derived dates" and the `content/11-publication-date.md`
comment.** Change "~October 2027" / "(Oct 2027)" to "November 2027 (regular cohorts; autoreferat
~mid-Oct 2027)" to match `03` sem. 5 and SPEC §5 (S7).
- Owner: E.

**F21 · P2 · `content/07-questions-hypotheses.md` H3 and the "Common protocol" last sentence.**
- "SRCC does not decrease after refinement" has no decision rule. Add "(lower 95% CI bound of the
  post − pre difference ≥ −0.1)" or drop the clause.
- "Margins and targets below are fixed … before the Stage II runs" contradicts the fact that margins are
  already stated. Rephrase as "The values below are pre-registered in the project repository; any change
  is recorded with its reason before the Stage II real-robot runs."
- Owner: E.

**F22 · P2 · `content/11-publication-date.md` l. 5–6 (visible text).** Change "with the option to present
it at IEEE/RSJ IROS 2027" to "**planned** presentation at IEEE/RSJ IROS 2027 (if the RA-L–IROS window is
offered)". The window is UNVERIFIED (resources §3).
- Owner: E.

**F23 · P2 · `content/02-topic.md` vs `content/05`/`07`.** The title uses "real-to-sim-to-real" and
"neural scene reconstruction", which is fine. But §5 is the only place where "real-to-sim-to-real" is
defined in plain words, and it isn't defined in §7. Add a 6-word gloss in §7 RQ1 ("a simulation
reconstructed from … (real-to-sim)") so the title's key term is defined where the hypotheses are (R3
p. 48: undefined title terms).
- Owner: E.

---

## 7. Questions the committee would ask at the 15-min talk (prepare answers)

1. How does your work differ from EmbodiedSplat and VR-Robo? (F11)
2. How exactly is the "real-data-only" policy trained, and how many robot-hours did it cost? (F9, F10)
3. With 60 episodes per arm, what is the power of your non-inferiority test? (F8)
4. What happens to the plan if K29 access or the sensor fails in sem. 3? (F7)
5. Why is this ITiT and not *automatyka, elektronika, elektrotechnika i technologie kosmiczne*?
   (Answered well in `05` and `08`; keep it.)
6. What has *actually* been done in year 1? (F2)

---

## 8. What is already strong (keep)

- A thesis sentence, a marked core (RQ1–RQ2, H1+H4), and extensions (`07` l. 3–8). This directly answers
  the R5 p. 12–14 "too many sub-goals" remark.
- Operational hypotheses with α, CI and Holm correction. This is rare in ITiT IPBs (R5 p. 16–17).
- §9 is organised by stage exactly as R5 p. 14–17 asks, with a sim-to-real validation protocol and a
  fallback (R5 p. 17–18, AGH §2.4).
- Venues are checked against the 5.01.2024 list, ICRA and CoRL are deliberately avoided, and the 2027 list
  risk is noted.
- ITiT framing in §5 and §8, and pre-PhD work demoted to background (S9).
- §10 PL and EN match. §13 mirrors the autoreferat % table.

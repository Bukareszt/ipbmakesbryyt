# Review 1 — resolution of fixes F1–F23

Issue #9 · 2026-09-26 · owner: Wave4-H worker · base: branch `ipb-draft` (uncommitted working tree on
top of 71c4707) · source: [review-1.md](review-1.md).

**Scope.** I edited `content/02`–`content/15` only. `content/00`, `content/01`, `tools/` and `output/`
were not touched, and nothing was committed. `output/*.docx` must be rebuilt from `content/` by the
tools owner.

**Coordinator decisions applied** (the doctoral student, 2026-09-26):
- §11 stays IEEE RA-L, Feb 2027, with IROS 2027 as fallback.
- Sem. 3 is descoped so it is feasible (F6).
- EmbodiedSplat goes into §6 only after verification, with a precise novelty claim (F11).
- International activity before the mid-term = summer school + seeking a foreign co-author (F12).
- The visit length matches the funder (F13).
- §6, §9 and §12 are brought within their page limits (F14–F16).
- RQ/H numbering is kept.
- No visible "to be confirmed" text: open points are HTML comments tagged `CONFIRM`.

**Status legend:** **done** = applied in `content/`. **partly done** = what an editor can do is applied,
and the rest needs a fact from the student or supervisor. **deferred to student** = needs the student's
own facts or a file outside this task.

| F# | Sev. | Status | What was done / why deferred | Files |
|---|---|---|---|---|
| F1 | P0 | **deferred to student** | ORCID, start date and supervisor title are the student's own facts, and `content/01` isn't owned by this task. §15 repeats "prof. uczelni" with a CONFIRM comment. | — (01 unchanged), 15 |
| F2 | P0 | **partly done** | Sem. 1–2 now claim only work evidenced by the IPB itself: literature review (§6); RQs, hypotheses, methods and tool survey (§7, §9); the IPB. The pipeline prototype and the tool-selection note moved to T3.1. "Own hand-held RGB-D captures" was removed from the §9 fallback because sensor availability is unknown. CONFIRM comments ask the student to insert what was actually done and whether they have an RGB-D sensor. | 03, 09 |
| F3 | P0 | **done** | §12 table matches §3 exactly: year 2 RA-L; year 3 RSS 2028/RA-L + IROS 2028/RA-L; year 4 RAS/RA-L. T-RO and CVPR/ICCV/ECCV removed. §8 "Dissemination" now lists RA-L, RSS, IROS, RAS (same as §9). §12 source comment updated. | 08, 12 |
| F4 | P0 | **done** (signing = student) | New `content/14-assistant-opinion.md` ("Nie dotyczy / Not applicable (no assistant supervisor appointed)" + CONFIRM). New `content/15-signatures.md` (date 29.09.2026 placeholder; student, supervisor, "—" for second supervisor; layout copied from `ipb.docx` §15). The builder in `tools/` must pick up the two new files; that's up to the tools owner. | 14, 15 |
| F5 | P0 | **done** | "(to be confirmed with the supervisor)" removed from §3 and §9. The wording is option (c) of resources §1: "a mobile-robot platform available at PWr (planned cooperation with K29 Denali; terms agreed in sem. 3, T3.2a)". §12 is consistent. Stripping comments on transfer to the docx = tools owner. | 03, 09, 12 |
| F6 | P1 | **done** (option a) | T3.3 is scoped to "Stage I pipeline, fidelity validation and simulation results; the real-robot pilot is included if available but is not a precondition". §11 visible text and comment record the decision. §9 Stage I moved to sem. 3, and the pilot is "sem. 3 if access agreed, otherwise start of sem. 4". | 03, 09, 11 |
| F7 | P1 | **done** | T3.2 split into T3.2a (written robot-access agreement + sensor decision, **by Nov 2026**) and T3.2b (pilot). Decision point: no access by end of Jan 2027 → the pilot moves to the start of sem. 4, plus offline evaluation on public datasets. The §12 risk bullet was rewritten to match. | 03, 12 |
| F8 | P1 | **done** (δ needs SV sign-off) | H1(b) is decided on the **pooled** ≥ 2 environments (120 episodes per policy), with δ = **15 pp** and a **one-sided** lower 95% bound. It has a visible power statement: ≈ 90% at SR ≈ 0.8, rechecked after the pilot. My calculation (normal approx., one-sided α = 0.05, SR 0.8 in both arms, no clustering): 60/arm δ 10 → 0.39; 120 pooled δ 10 → 0.61; 120 pooled δ 15 → 0.90; δ 10 at 80% needs ≈ 200/arm, which is infeasible given F9. τ for H4 keeps 10 pp so H4 isn't weakened. The old TODO is closed with these numbers, and a CONFIRM (supervisor) comment is on δ. | 07 |
| F9 | P1 | **done** (assumption flagged) | §9 has a robot-time estimate: ~35 robot-hours in Stage II (6 policies × 120 episodes + ~10 h teleoperation for the real-only baseline) and ~20 in Stage III (≥ 10 × 60). It assumes ~2 min per episode including reset. That is an assumption, marked in a comment with CONFIRM after the pilot. New §12 risk "robot time exceeds lab access". | 09, 12 |
| F10 | P1 | **done** | Real-data-only baseline = pretrained navigation model fine-tuned by behaviour cloning on teleoperated trajectories (§7 protocol, §9 baselines). Generic baseline = a public scene dataset of the simulator chosen in T3.1; it isn't named because the simulator isn't chosen yet. H4 has a rule for "real-only never reaches τ within B_max → ratio reported as a bound". | 07, 09 |
| F11 | P1 | **done** (verified) | EmbodiedSplat added as §6 [30]. **Verified** via the arXiv API (2509.17430v2, "accepted at ICCV, 2025") and Crossref (doi:10.1109/ICCV51701.2025.02359). **Full text read**: iPhone/Polycam capture of 20–30 min per scene, DN-Splatter meshes in Habitat-Sim, ImageNav policies pre-trained on HM3D/HSSD and fine-tuned, real test on a Stretch robot in one scene (10 episodes), SRCC 0.87–0.97. It uses a fixed capture and doesn't vary the real-data amount. Old [24]–[31] (now [22]–[29]) were checked by **keyword search of their full texts** (arXiv PDFs). **Finding:** RialTo (now [23]) *does* vary real data (appendix: 0/5/10/15 real demos; BC with 15 vs 50 demos), so the old "none measures…" was too broad. The sentence now says the *navigation* systems don't vary it, and names RialTo as the closest (manipulation) analysis. Old [4] AirSim and [21] Progressive Nets removed; refs renumbered; §7/§8 comments updated. `research/references-check.md` isn't owned by this task, so the log is here and in the §6 comment. Remaining: a close reading (not keyword search) by S/SV. | 06, 07, 08, 12 |
| F12 | P1 | **done** (per coordinator) | T4.2: poster at an international summer/winter school + inviting a foreign co-author for the Stage II article (no name, none is agreed). §12: a European host is sought in sem. 4, which opens the Erasmus+ short-term route. No host or co-author was invented. | 03, 12 |
| F13 | P1 | **done** | T6.2 = **3 months** (NAWA Bekker; the 2026 call allows 3–24 months, resources §5), with Erasmus+ short-term 5–30 days to a European lab as fallback. §12 table says "3-month visit". Next Bekker call marked UNVERIFIED in comments. | 03, 12 |
| F14 | P1 | **done** | §6: 1057 → **886** visible words (limit ≈ 960). Removed 2 refs; titles cut to the main title before the colon; venue abbreviations. | 06 |
| F15 | P1 | **done** | §9: 930 → **852** visible words. "Statistics" merged with "Dissemination" and points to §7; Metric + Success criterion merged per stage. | 09 |
| F16 | P1 | **done** | §12: 466 → **364** visible words. Table cells shortened (venue + points), hosts one line each, ethics and prior work one sentence each. | 12 |
| F17 | P2 | **done** | "PLGrid allocations (to be applied for)". Simulator stays "Isaac Sim / Isaac Lab or Habitat, chosen in T3.1", consistent with F2 (tool selection isn't claimed as done). | 09 |
| F18 | P2 | **done** | Stage I criterion: held-out PSNR within a margin X dB of 3DGS [21] on comparable indoor scenes (X fixed in the repo before Stage II), and no collision-mesh holes on evaluation paths. | 09 |
| F19 | P2 | **done** | Sem. 3 header "(RQ1, H1)". T5.1 deliverable "(**H3 completed**)". | 03 |
| F20 | P2 | **partly done** | `11` comment → "November 2027; autoreferat ~mid-Oct 2027". `01` "Derived dates" (~October 2027) isn't owned by this task and still needs the change. | 11 (01 open) |
| F21 | P2 | **done** | H3: "lower 95% CI bound of the change ≥ −0.1". Protocol: "All values are pre-registered in the project repository; changes are logged with reasons." | 07 |
| F22 | P2 | **done** | §11: "with a planned presentation at IEEE/RSJ IROS 2027 (if the RA-L–IROS window is offered)". | 11 |
| F23 | P2 | **done** | RQ1 now glosses *real-to-sim* and *sim-to-real*, so the title term is defined in §7. | 07 |

## Page check after edits (visible words, comments stripped, ~480 words/page)

| § | Limit | Before | After | Note |
|---|---|---|---|---|
| 5 | 1 | 419 | 429 | unchanged |
| 6 | 2 | 1057 | **886** | OK |
| 7 | 1 | 456 | **482** | at the limit because of F8/F10/F21/F23 additions; check in the docx |
| 8 | 1 | 378 | 399 | OK |
| 9 | 2 | 930 | **852** | OK; bullets add lines, so check in the docx |
| 10 | 1 each | 587 total | 587 | unchanged |
| 12 | 1 | 466 | **364** | OK; the table wraps, so check in the docx |

## Open items for the student / supervisor (all as `CONFIRM` / `UNVERIFIED` HTML comments)
1. F1: ORCID, start date, supervisor title (`content/01`).
2. F2: the real sem. 1–2 work and deliverables; whether an RGB-D sensor is available.
3. F8: δ = 15 pp acceptable? Recompute power with the pilot SR and clustering.
4. F9: real episode duration (robot-hour estimate).
5. F11: close reading of EmbodiedSplat and [22]–[29] to confirm the narrowed novelty sentence.
6. F4: real signing date (placeholder 29.09.2026, must be ≤ 30.09.2026); no assistant supervisor.
7. F20: `content/01` "~October 2027" → "November 2027".
8. The tools owner must add §14/§15 to the docx build and strip all HTML comments.

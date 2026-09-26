# §3 Harmonogram / Schedule

<!--
Structure (research/benchmarks.md §3 edits 2–6, 18): a preparatory phase (sem. 1–2) and four research
stages (I–IV, same as §9). Each semester has ≤ 3 numbered tasks T<sem>.<n>, each with a verifiable
deliverable (D) and the RQ/H from §7 it serves. The mid-term autoreferat copies these rows verbatim with
"% completion" (S9), so every task must be checkable.
Issue #12 (coordinator decisions, 2026-09-26): AI/ML PhD; main evaluation on public benchmarks/datasets
(§7 tiers A/B), real robot = validation (tier C). Papers: only 200-pt conferences of the 5.01.2024 list
assigned to ITiT (research/venues-200.md). Venue-to-semester mapping aligned to past-cycle deadlines and
accepted by the coordinator ("Use your proposal"): P1 NeurIPS 2027 (§11, sem. 4; ICML 2027 early option,
sem. 3); P2 CVPR 2028 or ICLR 2028 (sem. 5); P3 ECCV 2028 or NeurIPS 2028 (sem. 6); P4 optional, ICLR 2029
or CVPR 2029 (sem. 7). Core = P1–P3 (3 linked 200-pt papers). RSS only as an option for the robot paper.
All 2027–2029 deadlines are expected from past cycles: UNVERIFIED.
Places: K46 = Dept. of AI, W4 PWr; Denali = K29 "Laboratorium Robotów Autonomicznych Denali", C-16 room L1.5
(Pioneer 3-DX / DrRobot Jaguar 4x4, ROS 2; https://denali.kcir.pwr.edu.pl/robots.php); WCSS = Lem GPU cluster.
The Denali collaboration is PLANNED, not agreed (research/resources.md §1); T3.2 makes the agreement a task.
Sem. 1–2 (review-1 F2): only work evidenced by this IPB itself is claimed. CONFIRM (student): replace with
what was actually done, with real deliverables, before signing; say whether an RGB-D sensor is available.
Wave 6 (issue #15, 2026-09-26): broadened to a task-agnostic digital-twin methodology. Stage I (T3.1) now
delivers the reusable twin pipeline with capture protocol and fidelity–cost report (§8 contribution 5, §9
Stage I); Stage IV (T6.1b) adds the manipulation study (§9 Stage IV; ManiSkill3 [38], SIMPLER [37] in §6);
P3 = cross-task paper, no extra papers. Sem. 1–2 unchanged. K29 Laboratorium Robotyki manipulators (UR3,
FANUC LR Mate, ABB IRB 120; research/resources.md §1): availability UNVERIFIED, so validation is optional.
RSS 2028 deadline (~Jan/Feb 2028 from past cycles) UNVERIFIED.
Mobility (F12, F13): Bekker 2026 call = stays of 3–24 months; Erasmus+ short-term doctoral mobility =
5–30 days, continuous recruitment (research/resources.md §5).
Wave 9 (issue #23, 2026-09-26): pivot to the representation-level thesis (research/pivot-decision.md,
binding). Sem. 1–2 unchanged except the T2.1 wording. Stages: I paired-frame benchmark + gap localization
(RQ1/H1, sem. 3–4, P1 NeurIPS 2027), II policy zoo + transfer/failure forecasting (RQ2/H2, sem. 4–5, P2
CVPR/ICLR 2028), III budget allocation (RQ3/H3) and IV manipulation + world-model comparator (RQ4/H4), both
sem. 6, P3 NeurIPS/ECCV 2028; sem. 7 consolidation, P4 optional. ICML 2027 early option dropped (pivot lists
CVPR 2028 as the P1 alternative). Robot = 2 validation campaigns (sem. 5, 7), ~16 h each (§9). Old Wave 6
tasks (reusable twin pipeline, alignment, correction) removed: twins are a commodity and are reused.
Review-2 (issue #24), 2026-09-26 (research/review-2.md): R2-F3 P1 (May 2027) reports H1(a-c) + first H1(d);
the full zoo and "H1 completed" stay at Sep 2027. R2-F4 P3: ECCV 2028 (~Mar 2028) dropped because Stage III
cannot finish by then; Stage III set-up moved to the end of sem. 5, H3 by Apr 2028 for NeurIPS 2028 (~May),
H4 by Sep 2028; fallback ICLR 2029 (~late Sep 2028, expected from past cycles, UNVERIFIED). R2-F12
autoreferat moved to sem. 5 (due ~mid-Oct 2027). R2-F2 manipulation labels = published SIMPLER checkpoints.
Wave 11 (issue #26), 2026-09-26: pivot decision v2 (research/pivot-decision.md, binding): data-efficient
real-to-sim-to-real; no benchmark, no policy zoo. Sem. 1-2 unchanged except the T2.1 wording. Stages: I
capture less (RQ1/H1, sem. 3-4), II train robustly (RQ2/H2, sem. 4), P1 NeurIPS 2027 = RQ1+RQ2 (§11);
III few real rollouts (RQ3/H3, set-up Jul-Sep 2027, completed Feb 2028), P2 CVPR/ICLR 2028; IV whole-loop
budget + manipulation (RQ4/H4, sem. 6), P3 NeurIPS 2028 (fallback ICLR 2029); sem. 7 consolidation, P4
optional. P2 at CVPR 2028 (~Nov 2027) reports the H3 results available by then; H3 completion stays at
Feb 2028. Robot campaigns ~8 h each (§9). Venue deadlines as before: expected from past cycles, UNVERIFIED.
Review-3 (issue #27), 2026-09-26 (research/review-3.md): R3-F3 the paper-before-results pattern of review-2
R2-F3/F4 had returned: P1 (May 2027) was described as RQ1+RQ2 although H2 completes in Jul 2027, and P2 was
set for ICLR 2028 (~late Sep 2027, only a first H3 result by then) or CVPR 2028 (~Nov 2027) while H3
completed in Feb 2028. Now T4.2 = H1 + first H2 results; H3 on tier A by Jan 2028; P2 = ICML 2028
(~late Jan 2028, expected from ICML 2026: 28 Jan 2026, UNVERIFIED; ICML Lp 847, 200 pts, ITiT), CVPR 2028
only if H3 is complete by Nov 2027. ICLR 2028 dropped for P2 (it also coincides with the NeurIPS 2027
decision and the autoreferat). Deviation from pivot-decision.md ("P2: ICLR 2028 or CVPR 2028") recorded for
the coordinator. R3-F1/F6/F9/F10 T3.1: >= 20 scenes, separate phone capture, difficulty pilot, imitation.
R3-F8 T3.3: risk-weighted view selection (§6 [19]) as a comparator.
-->

| Semestr | Tasks (T = task, D = deliverable, place) |
|---|---|
| 1 (Oct 2025 – Feb 2026) | **Research target: define the problem and map the state of the art.** **T1.1** Systematic literature review in four areas: (a) sim-to-real transfer and domain randomization, (b) learning under distribution shift and domain adaptation, (c) neural scene reconstruction (NeRF, 3D Gaussian Splatting), (d) learning-based visual navigation. *D:* annotated bibliography and a written research-gap statement (basis of §6). **T1.2** Identification of the open problem: how much real data sim-to-real transfer needs, and whether reconstructed scenes can replace real data. *D:* problem statement and preliminary research questions, discussed with the supervisor. **T1.3** Doctoral School courses of semester 1. *D:* completed courses. Place: K46. <!-- CONFIRM (student): these targets match what was actually done in sem. 1 -->|
| 2 (Mar – Sep 2026) | **Research target: formulate the research plan and select the experimental basis.** **T2.1** Formulation of the data-efficient real-to-sim-to-real thesis, research questions RQ1–RQ4 (capture less, train robustly on an imperfect twin, collect few real rollouts, budget of the whole loop) and hypotheses H1–H4 with measurable decision rules and evaluation tiers A–C. *D:* §7 and §9 of this IPB. **T2.2** Comparative survey of public benchmarks and datasets (e.g. ScanNet++, HM3D), simulators (e.g. Habitat-Sim) and 3D Gaussian Splatting implementations against the needs of RQ1–RQ4 (real video + reference scan, licence, compute cost). *D:* tool-selection note with a shortlist for Stage I. **T2.3** Individual Research Plan agreed with the supervisor. *D:* this IPB, signed and submitted by **30.09.2026**. Place: K46. <!-- CONFIRM (student): these targets match what was actually done in sem. 2; add any prototype that really exists --> |
| 3 (Oct 2026 – Feb 2027) | **Stage I – capture less (RQ1, H1).** **T3.1** Tier A set-up: final choice of ≥ 20 public scenes (10 held out) with laser scans and separate phone captures, simulator and existing 3DGS pipeline from the T2.2 shortlist; references ("reality") and training twins at ≥ 4 capture budgets; pilot fixing task difficulty (below the SR ceiling) and the capture-cost model; imitation-learned navigation policies in the twins; pre-registration of the protocol (§7, §9). *D:* working loop and protocol in the repository, **by Dec 2026**. Place: K46, WCSS. **T3.2** Validation stand: written agreement on robot access (planned cooperation with the K29 Denali laboratory, or another PWr platform) and sensor decision (SzD Minigrant application if a sensor must be bought). *D:* agreement, **by Nov 2026**. **T3.3** Task-aware, uncertainty-guided capture vs. uniform, reconstruction-only and risk-weighted view selection. *D:* first budget–success curves (first H1 result), **by Feb 2027**. |
| 4 (Mar – Sep 2027) | **Stage I completed; Stage II – train robustly on an imperfect twin (RQ1–RQ2, H1–H2).** **T4.1** Uncertainty-aware augmentation and representation-based weighting of twin data vs. uniform domain randomization at an equal capture budget. *D:* **H1 completed** and first H2 result on tier A, **by Apr 2027**; **H2 completed, by Jul 2027**. Place: K46, WCSS. **T4.2** **Prepare and submit article P1 to NeurIPS 2027** (RQ1–RQ2: task-aware capture, H1, and first uncertainty-aware training results, H2). *D:* submission, **May 2027** (§11). **T4.3** Stage III set-up: rollout-selection and correction code on tier A (Jul–Sep 2027). *D:* first H3 result, **by Sep 2027**. **T4.4** Grants and international activity: NCN PRELUDIUM application; poster at an international summer school; foreign co-author sought for P2; NAWA Bekker application for the sem. 6 visit. *D:* applications, poster. <!-- UNVERIFIED: dates of PRELUDIUM 26, the next Bekker call, the autoreferat deadline and NeurIPS 2027 (expected ~May, as NeurIPS 2026: 6 May 2026). No co-author is named because none is agreed. --> |
| 5 (Oct 2027 – Feb 2028) | **Mid-term evaluation** (Nov 2027): autoreferat (≤ 5 pages, ~mid-Oct 2027) and 15-min presentation. **Stage III – collect few real rollouts (RQ3, H3).** **T5.1** Active selection of real rollouts (predicted gap, uncertainty) vs. random selection; correction of the twin and fine-tuning of the policy with the selected rollouts. *D:* **H3 completed** on tier A, **by Jan 2028**. Place: K46, WCSS. **T5.2** First robot validation campaign (tier C, 2 PWr rooms, ~8 robot-hours): own captures, twins, uniform capture vs. the loop. *D:* validation report. Place: Denali. Without robot access, the campaign moves to sem. 7; H1–H3 are decided on tier A either way. **T5.3** **Article P2** (active real-rollout selection and twin correction, RQ3) submitted to **ICML 2028** (~late Jan 2028; CVPR 2028, ~Nov 2027, only if H3 is complete by then). If P1 was rejected, its revision goes to CVPR 2028. *D:* submission(s). |
| 6 (Mar – Sep 2028) | **Stage IV – budget of the whole loop; cross-task test (RQ4, H4).** **T6.1** (a) Real-data budget curves of the full loop vs. real-only learning ("exchange rate") on tier A; (b) the same pipeline, unchanged, on manipulation scenes, with published paired sim/real results as tier-B check. *D:* navigation result **by Apr 2028**; **H4 completed, by Sep 2028**. Place: K46, WCSS. **T6.2** **Foreign research visit** (3 months, NAWA Bekker; if not funded, a 5–30-day Erasmus+ short-term mobility to a European lab; hosts in §12): joint experiments. *D:* visit report. **T6.3** **Article P3** (budget law of the full loop, with first manipulation results) submitted to **NeurIPS 2028** (~May 2028); if not ready, to **ICLR 2029** (~late Sep 2028). *D:* submission. |
| 7 (Oct 2028 – Feb 2029) | **Consolidation (RQ1–RQ4).** **T7.1** Second robot validation campaign (tier C) of the full loop; final analysis of H1–H4 across tiers. *D:* final results. Place: K46, Denali. **T7.2** Release of code and experiment scripts. *D:* public repository. **T7.3** Optional article P4 (consolidated study) to ICLR 2029 (~late Sep 2028) or CVPR 2029 (~Nov 2028); start of dissertation writing. *D:* submission (optional), dissertation outline. |
| 8 (Mar – Sep 2029) | **T8.1** **Editing of the doctoral dissertation**; final version. *D:* dissertation submitted by **30.09.2029** (§4). **T8.2** Responses to reviews and camera-ready versions of pending articles. *D:* revised manuscripts. |

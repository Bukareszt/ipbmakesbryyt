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
Wave 13 (issue #29), 2026-09-26: pivot decision v3 (general, domain-agnostic real-to-sim-to-real;
manipulation and navigation equal testbeds; twin = appearance/geometry + physical parameters). Sem. 1-2
unchanged (v3). Sem. 3-8 rephrased generically: T3.1 sets up tier A in both testbeds (navigation ScanNet++
scenes; manipulation ManiSkill3 configurations with held-out physical parameters, §9) by Jan 2027 (was
Dec 2026 for navigation only; the second testbed costs a month); "rollouts" -> "trials" / "real data";
T3.2 adds a PWr manipulator for tier C only if available (K29 Laboratorium Robotyki, UNVERIFIED); T6.1 =
both testbeds + tier B (SIMPLER, §6 [34]) instead of "navigation, then manipulation". All sub-study dates,
P1 NeurIPS 2027 (May 2027), P2 ICML 2028 / CVPR 2028, P3 NeurIPS 2028 / ICLR 2029 unchanged. "Budget law"
is kept only as P3's working title (review-3 R3-F11). T2.1: only the RQ labels were aligned with §7
(as allowed by pivot v2 "the T2.1 wording may be adapted"); the rest of sem. 1-2 is untouched. §6 reference numbers in older comments are pre-Wave-13.
Wave 14 (issue #30), 2026-09-26: pivot decision v4 (framing only; one method with components C1-C3, thesis
= H4). Sem. 1-2 untouched. Sem. 3-6 stage titles renamed to "method component C1/C2/C3" and "the whole
method (RQ4, H4, the thesis)"; T3.3, T4.1, T5.1 start with the component name; T6.1 adds the v4 baseline
"strongest existing real-to-sim-to-real pipeline" (uniform capture + domain randomization + random
real-data selection, RialTo-style; §9 Stage IV); P1-P3 described by method component (P1 = C1 + first C2,
P2 = C3, P3 = the whole method). "Budget law" stays only as P3's working title (R3-F11). All dates,
deliverables, venues and task numbers unchanged.
Wave 15-U (issue #32), 2026-09-26: pivot decision v5 (VLA/VLM + world models, sim-first fine-tuning in the
twin). Sem. 1-2 untouched. All task numbers, deliverables, dates and venues unchanged. Sem. 3-7 wording:
T3.1 adds the open VLA (LoRA), VLM and world-model checkpoints, the measured GPU cost in the pilot and the
WCSS/PLGrid computing grant (compute estimate ~23k H100-hours for sem. 3-7, §9 and
research/vla-wm-crowdedness.md §4: OUR ESTIMATE, UNVERIFIED until T3.1); T3.3 adds VLM guidance and the
AREA3D-type comparator; T4.1 = C2 with H2(a) vs uniform DR and H2(b) twin + world model vs twin only
(§7 v5, worker T); T4.3/T5.1 gap from twin, world-model and VLA uncertainty, correction of twin, world
model and VLA; T5.1 adds the twin-only failure-driven (TwinRL-type) comparator; T6.1 H4(a) real-only
fine-tuning of the same VLA, H4(b) TwinRL/RialTo-style pipeline (coordinator msg_65a79c659e58); T7.2 LoRA
adapters released where model licences permit (OpenVLA weights: Llama 2 Community License per the openvla
README; NaVILA HF checkpoint without a licence tag).
Wave 16-W (issue #33), 2026-09-26: pivot decision v6 (general description; navigation only; pipeline
real -> twin -> navigation models -> real). Sem. 1-2 untouched. Task numbers, deliverables, dates and
venues unchanged. Sem. 3-7 reworded by stage 1-3 + whole pipeline: manipulation testbed, tier B, PWr
manipulator, VLA/VLM/LoRA/world-model checkpoint wording and the TwinRL-named baseline removed; T3.1 set-up
on public indoor scans only (Jan 2027 kept); T4.1 = stage 2 (world model + foundation-model initialization
as method families, one H2 threshold vs uniform DR); T6.1 compares with the strongest existing
real-to-sim-to-real approach (H4) and real-only learning (reported curve); T7.2 no longer mentions LoRA
adapters.
Wave 18-W (issue #35), 2026-09-26: pivot decision v7 (research/pivot-decision.md, top) and the deep-research
report. Sem. 1-2 untouched (v7). Task numbers renumbered only in sem. 4 (T4.5 = the grants task, was T4.4) and
sem. 5 (T5.3 manipulation set-up new, P2 = T5.4). Stage titles = the three reduction mechanisms + the whole
method. T3.1 adds: ScanNet++ licence application (supervisor signs) and PLGrid grant in Oct 2026, MuSHRoom rooms,
budget grid, hidden physical parameters, difficulty regime, operator-minute cost model, SRCC pilot,
pre-registration. T3.2: SzD Minigrant for a TurtleBot 4 Lite (~1.7k EUR per the report) OR the K29 agreement.
P1 = mechanism 1 (H1) only (v7), so T4.1 = H1 completed + early H1 preprint (report recommendation 7); H2 moves
to T4.3 (first result Jun 2027, completed Jul 2027 as before); T4.4 = mechanism 3 set-up (first H3 Sep 2027).
T5.3 manipulation proxy (ManiSkill3 hidden physics, §9) with mechanisms 1-2 by Dec 2027 so that P2 (ICML 2028,
~late Jan 2028) can carry first manipulation results (v7 P2). T6.1 adds the whole method in manipulation
(Jul 2028) for P3 (v7 P3). T7.2 release wording per the report's recommendation 4 (no ScanNet++-derived
assets). All sub-study dates for H1-H4, venues and deadlines unchanged.
-->

| Semestr | Tasks (T = task, D = deliverable, place) |
|---|---|
| 1 (Oct 2025 – Feb 2026) | **Research target: define the problem and map the state of the art.** **T1.1** Systematic literature review in four areas: (a) sim-to-real transfer and domain randomization, (b) learning under distribution shift and domain adaptation, (c) neural scene reconstruction (NeRF, 3D Gaussian Splatting), (d) learning-based visual navigation. *D:* annotated bibliography and a written research-gap statement (basis of §6). **T1.2** Identification of the open problem: how much real data sim-to-real transfer needs, and whether reconstructed scenes can replace real data. *D:* problem statement and preliminary research questions, discussed with the supervisor. **T1.3** Doctoral School courses of semester 1. *D:* completed courses. Place: K46. <!-- CONFIRM (student): these targets match what was actually done in sem. 1 -->|
| 2 (Mar – Sep 2026) | **Research target: formulate the research plan and select the experimental basis.** **T2.1** Formulation of the data-efficient real-to-sim-to-real thesis, research questions RQ1–RQ4 (capture less, learn robustly in an imperfect twin, few real data, budget of the whole loop) and hypotheses H1–H4 with measurable decision rules and a proxy-reality evaluation protocol. *D:* §7 and §9 of this IPB. **T2.2** Comparative survey of public benchmarks and datasets (e.g. ScanNet++, HM3D), simulators (e.g. Habitat-Sim) and 3D Gaussian Splatting implementations against the needs of RQ1–RQ4 (real video + reference scan, licence, compute cost). *D:* tool-selection note with a shortlist for Stage I. **T2.3** Individual Research Plan agreed with the supervisor. *D:* this IPB, signed and submitted by **30.09.2026**. Place: K46. <!-- CONFIRM (student): these targets match what was actually done in sem. 2; add any prototype that really exists --> |
| 3 (Oct 2026 – Feb 2027) | **Mechanism 1 – less capture (RQ1, H1).** **T3.1** Proxy-reality set-up (§9): application for the ScanNet++ licence (signed by the supervisor) and for a PLGrid computing grant in Oct 2026; ≥ 20 ScanNet++ scenes (10 held out) and the MuSHRoom rooms, with laser-scan or mesh references and separate phone captures; twins on the budget grid with the open simulator, 3DGS and structure-from-motion tools; hidden physical parameters of "reality"; navigation tasks, learner and pretrained models running on the twins; pilot fixing the difficulty regime, the operator-minute cost model, the sim-vs-real correlation between twin and "reality" and the GPU cost; pre-registration of the mechanism 1 baselines. *D:* working pipeline and pre-registered protocol in the repository, **by Jan 2027**. Place: K46, WCSS. **T3.2** Validation stand: SzD Minigrant application for a small mobile robot, or a written agreement on robot access with the K29 Denali laboratory. *D:* application or agreement, **by Nov 2026**. **T3.3** Mechanism 1: capture guided by the task and by the twin's uncertainty vs. uniform, task-blind and task-weighted selection, judged by the success of the model trained in each twin. *D:* first budget–success curves (first H1 result), **by Feb 2027**. |
| 4 (Mar – Sep 2027) | **Mechanism 1 completed; mechanism 2 – better use of simulation (RQ1–RQ2, H1–H2).** **T4.1** Mechanism 1 completed: full budget curves against all pre-registered baselines. *D:* **H1 completed** on the proxy reality and an early preprint of the result, **by Apr 2027**. **T4.2** **Prepare and submit article P1 to NeurIPS 2027** (mechanism 1, H1, in navigation). *D:* submission, **May 2027** (§11). **T4.3** Mechanism 2: training that follows the twin's uncertainty, initialized from pretrained foundation models, vs. uniform and no domain randomization in the pre-registered difficulty regime; the world-model extension as an ablation. *D:* first H2 result **by Jun 2027**; **H2 completed** with the ablations, **by Jul 2027**. Place: K46, WCSS. **T4.4** Mechanism 3 set-up: gap prediction, selection and correction code on the proxy reality, check of the sim-vs-real precondition (Jul–Sep 2027). *D:* first H3 result, **by Sep 2027**. **T4.5** Grants and international activity: NCN PRELUDIUM application; poster at an international summer school; foreign co-author sought for P2; NAWA Bekker application for the sem. 6 visit. *D:* applications, poster. <!-- UNVERIFIED: dates of PRELUDIUM 26, the next Bekker call, the autoreferat deadline and NeurIPS 2027 (expected ~May, as NeurIPS 2026: 6 May 2026). No co-author is named because none is agreed. --> |
| 5 (Oct 2027 – Feb 2028) | **Mid-term evaluation** (Nov 2027): autoreferat (≤ 5 pages, ~mid-Oct 2027) and 15-min presentation. **Mechanism 3 – fewer real trials (RQ3, H3); manipulation set-up.** **T5.1** Mechanism 3: selection of real trials by the predicted twin-to-reality gap vs. random, uniform-coverage and failure-driven selection; correction of the twin (appearance, geometry, physical parameters) and of the model with the selected trials. *D:* **H3 completed** on the proxy reality, **by Jan 2028**. Place: K46, WCSS. **T5.2** First robot validation campaign (2 PWr rooms, ~8 robot-hours): own captures, twins, uniform capture vs. the method, sim-vs-real correlation between proxy and robot. *D:* validation report. Place: K46 or Denali. Without a robot, the campaign moves to sem. 7; H1–H3 are decided on the proxy reality either way. **T5.3** Generalization set-up: manipulation proxy reality with hidden physical parameters (§9) and mechanisms 1–2 run on it unchanged. *D:* first manipulation budget curves, **by Dec 2027**. **T5.4** **Article P2** (mechanisms 2–3, RQ2–RQ3, in navigation, with the first manipulation results) submitted to **ICML 2028** (~late Jan 2028; CVPR 2028, ~Nov 2027, only if H3 is complete by then). If P1 was rejected, its revision goes to CVPR 2028. *D:* submission(s). |
| 6 (Mar – Sep 2028) | **The whole method (RQ4, H4, the thesis) and its generalization.** **T6.1** Budget curves of the whole method vs. the assembled, pre-registered strongest existing real-to-sim-to-real approach and vs. learning from real data only, with the method's settings fixed in advance; the whole method, unchanged, in manipulation. *D:* first H4 result **by Apr 2028**; manipulation curves **by Jul 2028**; **H4 completed, by Sep 2028**. Place: K46, WCSS. **T6.2** **Foreign research visit** (3 months, NAWA Bekker; if not funded, a 5–30-day Erasmus+ short-term mobility to a European lab; hosts in §12): joint experiments. *D:* visit report. **T6.3** **Article P3** (the whole method against existing approaches, with the generalization to manipulation) submitted to **NeurIPS 2028** (~May 2028); if not ready, to **ICLR 2029** (~late Sep 2028). *D:* submission. |
| 7 (Oct 2028 – Feb 2029) | **Consolidation (RQ1–RQ4).** **T7.1** Second robot validation campaign of the whole method; final analysis of H1–H4. *D:* final results. Place: K46, Denali. **T7.2** Release of the method's code, configurations, scene lists, seeds, pre-registrations and the releasable twins (no assets derived from ScanNet++). *D:* public repository. **T7.3** Optional article P4 (consolidated study) to ICLR 2029 (~late Sep 2028) or CVPR 2029 (~Nov 2028); start of dissertation writing. *D:* submission (optional), dissertation outline. |
| 8 (Mar – Sep 2029) | **T8.1** **Editing of the doctoral dissertation**; final version. *D:* dissertation submitted by **30.09.2029** (§4). **T8.2** Responses to reviews and camera-ready versions of pending articles. *D:* revised manuscripts. |

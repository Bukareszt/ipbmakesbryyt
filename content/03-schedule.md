# §3 Harmonogram / Schedule

| Semestr | Brief description of the task |
|---|---|
| 1 | 1. Literature review in the scope of sim-to-real transfer, domain randomization and domain adaptation, neural scene reconstruction from real data (such as 3D Gaussian Splatting) and deep learning for robot navigation and manipulation. 2. Identification of the most important research gaps in the generalization of deep learning models trained in simulations built from real data. 3. Extending theoretical knowledge, including machine learning theory and learning under distribution shift, necessary for further work on the PhD thesis. 4. Participation in the Doctoral School courses. |
| 2 | 1. Continuation of the literature review - participation in the internal reading group, discussing novel methods regarding sim-to-real transfer and physical AI. 2. Initial pilot experiments on reconstructing real scenes with 3D Gaussian Splatting and importing them into navigation and manipulation simulators, with regard to the gaps identified during the literature review. 3. Specifying the Individual Research Plan. 4. Participation in the Doctoral School courses. |
| 3 | 1. Continuation of the literature review - participation in the internal reading group, discussing novel methods regarding sim-to-real transfer and physical AI. 2. Preparation of the research environment for robot navigation and robotic manipulation, with shared reconstruction tools: for navigation, real scene captures, digital twins in a navigation simulator and a dataset-based proxy measuring the reconstruction-fidelity gap; for manipulation, digital twins of real tabletop scenes built from images of public robot datasets and own captures, in a manipulation simulator, paired with published real-robot results of the same policies; and computing resources. 3. Conducting research on which reconstruction errors of a digital twin, varying across a scene, determine the generalization of navigation and manipulation models trained in it. |
| 4 | 1. Continuation of the literature review - participation in the internal reading group, discussing novel methods regarding sim-to-real transfer and physical AI. 2. Finishing the research on the harmful reconstruction errors in both tasks and on randomizing each region of a digital twin according to its reconstruction uncertainty and task relevance. 3. Writing a scientific article for a conference from the ministerial list (regarding the reconstruction errors that determine generalization in navigation and manipulation), planned for submission to e.g. NeurIPS 2027. 4. Starting the research on localizing the sim-to-real gap inside navigation and manipulation models, with first results on the stage at which task information is lost on real inputs. 5. Preparation of the Preludium research grant proposal to the National Science Centre. 6. Participation in an international scientific conference. |
| 5 | 1. Continuation of the literature review - participation in the internal reading group, discussing novel methods regarding sim-to-real transfer and physical AI. 2. Finishing the research on localizing the sim-to-real gap inside the models of both tasks and on aligning representations at that stage. 3. Writing a scientific article for a conference from the ministerial list (regarding the localization of the sim-to-real gap inside deep models), e.g. ICML 2028 or CVPR 2028. 4. Carrying out research on selecting real data under a limited budget to correct both the digital twin and the model in both tasks. 5. Starting the research on predicting whether the improvements transfer to unseen environments and between navigation and manipulation. |
| 6 | 1. Continuation of the literature review - participation in the internal reading group, discussing novel methods regarding sim-to-real transfer and physical AI. 2. Finishing the research on the selection of real data and on predicting the transfer of improvements across environments and tasks, complemented by controlled studies of physical parameters in a simulator with hidden parameters. 3. Writing a scientific article for a conference from the ministerial list (regarding the selection of real data under a limited budget and the prediction of transfer), e.g. NeurIPS 2028. 4. Initial validation of the developed methods on a real robot, if access to a robotics laboratory of Wrocław University of Science and Technology allows. 5. Research internship at a foreign research group working on robot learning, if funding allows. |
| 7 | 1. Continuation of the literature review - participation in the internal reading group, discussing novel methods regarding sim-to-real transfer and physical AI. 2. Finishing the experiments and, if possible, the validation on a real robot. 3. Writing a scientific article for a conference or journal from the ministerial list summarizing the obtained results. 4. Participation in an international scientific conference. 5. Preparing the structure and sketch of the doctoral dissertation. |
| 8 | Editing the doctoral dissertation, preparation of the final version of the document. |

<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §3: sem. 2 pilot imports reconstructions into navigation and manipulation simulators; sem. 3 builds both pipelines with shared reconstruction tools (navigation: captures -> twin -> navigation simulator + ScanNet++-style proxy for the reconstruction-fidelity gap; manipulation: real tabletop images of public robot datasets and own captures -> twin (SIMPLER-style visual matching) -> manipulation simulator, paired with published real-robot results); RQ1 sem. 3-4 on both tasks (NeurIPS 2027); RQ2 sem. 4-5 on both tasks (ICML/CVPR 2028); RQ3 sem. 5-6, RQ4 started sem. 5 and finished sem. 6 across environments and between tasks, with controlled hidden-parameter physics studies as a complement (NeurIPS 2028); robot validation sem. 6-7 on the mobile robot and, if access allows, a robot arm (optional, availability UNVERIFIED); journal summarizes environments, tasks and real robots. Manipulation is no longer a sim-to-sim confirmation test. -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §3 descoped (fix 1): sem. 3 = navigation pipeline only (captures, 3D reconstruction, navigation simulator, dataset-based proxy measuring the reconstruction-fidelity gap) + RQ1 study; RQ2 starts in sem. 4 with first results next to the NeurIPS 2027 article (mid-term evaluation); RQ2 article ICML/CVPR 2028 (sem. 5); RQ3 article NeurIPS 2028 with RQ4 folded in (sem. 6); manipulation only in sem. 6 as a sim-to-sim confirmation test with hidden physics; robot validation merged into one block sem. 6-7 'in cooperation with a robotics laboratory of Wrocław University of Science and Technology' (K29 Laboratorium Robotyki, availability UNVERIFIED, hence 'a'); journal article written in sem. 7, submitted in sem. 8; the ICLR/CVPR 2029 conference article dropped (3 conference papers + 1 journal). Terms: 'sim-to-real gap', 'digital twin' (sem. 1 keeps the descriptive 'simulations built from real data'; the terms are defined in §5). -->
<!-- Review-6 (2026-09-27): sem. 2 item 2 reworded to a pilot on reconstructing scenes and importing them into a navigation simulator; sem. 2 item 4 "machine learning summer school" (unconfirmed) replaced by Doctoral School courses. CONFIRM (student): if a summer school was attended, name it with the year (e.g. "MLSS 2026") and confirm the pilot item. Sem. 4 item 2 "according to the harmful components"; sem. 4 and 7 conferences "international"; sem. 5/7 robot validation restricted to navigation; sem. 6 manipulation = controlled second task, internship host type named (no host); sem. 7 split into one task per item. -->
<!--
Wave 20 (ultracode), 2026-09-27: §3 rewritten from scratch in the Binkowski style for the final core (topic and RQ1-RQ4 of §2/§7): RQ1 sem. 3-4, RQ2 sem. 3-5, RQ3 sem. 5-6, RQ4 sem. 6-7; one conference article per RQ (sem. 4, 5, 6, 7); Preludium sem. 4; internship sem. 6; robot validation sem. 5 and 7. No venues, dates or thresholds in the visible text.
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
| 1 (Oct 2025 – Feb 2026) | **Research target: define the problem and map the state of the art.** **T1.1** Systematic literature review in four areas: (a) sim-to-real transfer and domain randomization, (b) learning under distribution shift and domain adaptation, (c) neural scene reconstruction (NeRF, 3D Gaussian Splatting), (d) learning-based visual navigation. *D:* annotated bibliography and a written research-gap statement (basis of §6). **T1.2** Identification of the open problem: why models trained in digital twins fail to generalize to reality, and at which points of the real-to-sim-to-real loop this can be improved. *D:* problem statement and preliminary research questions, discussed with the supervisor. **T1.3** Doctoral School courses of semester 1. *D:* completed courses. Place: K46. <!-- CONFIRM (student): these targets match what was actually done in sem. 1 -->|
| 2 (Mar – Sep 2026) | **Research target: formulate the research plan and select the experimental basis.** **T2.1** Formulation of the thesis on improving sim-to-real generalization, research questions RQ1–RQ4 (generalization-aware twins, sim-real invariant representations, adaptation with little real data, generalization across scenes and tasks) and hypotheses H1–H4 with measurable criteria and a proxy-reality evaluation protocol. *D:* §7 and §9 of this IPB. **T2.2** Comparative survey of public benchmarks and datasets (e.g. ScanNet++, HM3D), simulators (e.g. Habitat-Sim) and 3D Gaussian Splatting implementations against the needs of RQ1–RQ4 (real video + reference scan, licence, compute cost). *D:* tool-selection note with a shortlist for Stage I. **T2.3** Individual Research Plan agreed with the supervisor. *D:* this IPB, signed and submitted by **30.09.2026**. Place: K46. <!-- CONFIRM (student): these targets match what was actually done in sem. 2; add any prototype that really exists --> |
| 3 (Oct 2026 – Feb 2027) | **RQ1 – generalization-aware twins.** **T3.1** Evaluation set-up (§9): ScanNet++ licence (signed by the supervisor) and PLGrid grant applications in Oct 2026; ≥ 20 ScanNet++ scenes (10 unseen) and MuSHRoom rooms with separate references and phone captures; twins, hidden physical parameters of "reality", navigation tasks and pretrained models running; pilot fixing difficulty and GPU cost; pre-registration of RQ1 baselines. *D:* working protocol in the repository, **by Jan 2027**. Place: K46, WCSS. **T3.2** Validation stand: SzD Minigrant application for a small mobile robot, or an agreement with the K29 Denali laboratory. *D:* application or agreement, **by Nov 2026**. **T3.3** Ablation of twin properties (appearance, geometry, lighting, physics) against the generalization gap. *D:* ablation results, **by Feb 2027**. |
| 4 (Mar – Sep 2027) | **RQ1 completed; RQ2 – sim-real invariant representations.** **T4.1** Twins varied by task relevance and reconstruction uncertainty vs. single twin and uniform randomization, on unseen scenes. *D:* **H1 completed**, **by Apr 2027**. **T4.2** **Prepare and submit article P1 to NeurIPS 2027** (RQ1 and first RQ2 results, navigation). *D:* submission, **May 2027** (§11). **T4.3** Invariance objectives on pretrained encoders, world-model augmentation as an ablation, layer-wise probing of the gap. *D:* first H2 result, **by Sep 2027**. Place: K46, WCSS. **T4.4** Grants and international activity: NCN PRELUDIUM application; poster at an international summer school; foreign co-author sought for P2; NAWA Bekker application. *D:* applications, poster. |
| 5 (Oct 2027 – Feb 2028) | **Mid-term evaluation** (Nov 2027): autoreferat (≤ 5 pages) and 15-min presentation. **RQ2 completed; RQ3 – adaptation with little real data.** **T5.1** H2 completed with ablations. *D:* **H2 completed**, **by Nov 2027**. **T5.2** Adaptation with real samples chosen by twin–reality disagreement vs. random and failure-driven selection and vs. a model trained on the full real dataset. *D:* **H3 completed**, **by Jan 2028**. **T5.3** First robot validation campaign (2 PWr rooms, ~8 robot-hours). *D:* validation report. Place: K46 or Denali. **T5.4** **Article P2** (RQ2–RQ3) to **ICML 2028** (~late Jan 2028); if P1 was rejected, its revision to CVPR 2028. *D:* submission(s). |
| 6 (Mar – Sep 2028) | **RQ4 – generalization across scenes and tasks.** **T6.1** All methods, unchanged, on held-out scenes and in manipulation (ManiSkill3 proxy reality with hidden physics, checked against published paired sim-and-real evaluations). *D:* **H4 completed**, **by Sep 2028**. Place: K46, WCSS. **T6.2** **Foreign research visit** (3 months, NAWA Bekker; else a 5–30-day Erasmus+ mobility; hosts in §12). *D:* visit report. **T6.3** **Article P3** (RQ4, navigation and manipulation) to **NeurIPS 2028** (~May 2028), else **ICLR 2029**. *D:* submission. |
| 7 (Oct 2028 – Feb 2029) | **Consolidation (RQ1–RQ4).** **T7.1** Second robot validation campaign; final analysis of H1–H4. *D:* final results. Place: K46, Denali. **T7.2** Release of code, configurations, scene lists, seeds and releasable twins (nothing derived from ScanNet++). *D:* public repository. **T7.3** Optional article P4 to ICLR 2029 or CVPR 2029; start of dissertation writing. *D:* submission (optional), dissertation outline. |
| 8 (Mar – Sep 2029) | **T8.1** **Editing of the doctoral dissertation**; final version. *D:* dissertation submitted by **30.09.2029** (§4). **T8.2** Responses to reviews and camera-ready versions of pending articles. *D:* revised manuscripts. |

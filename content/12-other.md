# §12 Inne / Other comments (max 1 page)

**Planned outputs by year** (200-point conferences assigned to the discipline, list of 5.01.2024).

| Year | Papers (planned submission, 200 points each) | Code | Grants | Mobility, events |
|---|---|---|---|---|
| 1 (2025/26) | — | — | — | — |
| 2 (2026/27) | P1 (stage 1 and first stage 2 results, RQ1–RQ2): NeurIPS 2027, May 2027 (§11) | Pipeline on public scans | SzD Minigrant; NCN PRELUDIUM; NAWA Bekker | Summer school poster |
| 3 (2027/28) | P2 (stage 3, few real data, RQ3): ICML or CVPR 2028; P3 (the whole pipeline, RQ4): NeurIPS 2028 | Stage 3 code | — | Mid-term; 3-month visit (sem. 6) |
| 4 (2028/29) | Optional P4, consolidated study: ICLR 2029 or CVPR 2029 | Method release | — | Dissertation |

**Foreign research visit (candidate hosts, not yet contacted).** (1) Z. Kira's group, Georgia Tech:
EmbodiedSplat [11]. (2) Multi-robot Systems Lab, Stanford University (M. Schwager): Gaussian-splatting
scene models. A European host (Erasmus+ route) working on active reconstruction or sim-to-real transfer,
and a foreign co-author for P2, are sought with the supervisor in sem. 4.

**Collaboration at PWr.** Robot validation is planned with the K29 *Denali* laboratory (Pioneer 3-DX,
Jaguar 4x4, ROS 2); a written agreement is task T3.2 (Nov 2026).

**Risks and mitigation** (semester affected).
- *One stage gives no gain* (3–5): its budget curve still answers its RQ; H4 is still tested.
- *Twin uncertainty is poorly calibrated* (3–4): two estimators and an ensemble fallback.
- *Proxy reality is easier than reality* (4–7): separate captures for twin and reference, a second
  reference and robot validation check the direction (§9).
- *Learning from real data only is strong at small budgets* (6): in navigation, gains from more data in a
  known location saturate quickly [8]; H4 is reported as a full budget curve.
- *Compute* (3–7): WCSS and PLGrid grants in sem. 3; smaller models for development; fewer seeds.
- *Crowded field, scooping* (3–6): twins, world models and fine-tuning in simulation are active areas,
  with targeted or real rollouts [27, 28]; we claim only the real-data budget; early preprints.
- *Licences, robot access* (3, 5, 7): gated or restricted models have open alternatives; without a
  robot, validation moves by a semester (the proxy reality decides).
- *Rejection at a top venue* (4–7): each paper has a resubmission path inside the 200-point set 2–4 months
  later (NeurIPS → CVPR → ICML → ECCV/ICCV).

**Future applicability.** The method is not specific to navigation; robotic manipulation is a natural
extension after the dissertation.

**Prior work (background only).** A pre-PhD NLP paper (ACL 2025 SRW, forecasting from hidden states); not
part of the dissertation.

**Ethics and data.** Own captures are anonymized (GDPR); public datasets are used under their licences.

<!--
Wave 16-W (issue #33), 2026-09-26: pivot decision v6 (navigation only; manipulation "at most as future
applicability in §12"). Outputs table: P1-P3 by stage (P1 = stage 1 + first stage 2, P2 = stage 3, P3 =
whole pipeline), venues unchanged. PWr manipulator removed from the collaboration line (manipulation is no
longer a testbed). Risks: "component" -> "stage"; proxy-reality risk without tier B (manipulation-only);
real-only risk cites Suomela [8] (new §6 numbering); compute risk without the ~23k H100-hour VLA estimate;
scooping cites TwinRL [27] and VLAW [28] in general terms; licence risk generalized (no OpenVLA/Llama 2
detail). New "Future applicability" paragraph (manipulation). EmbodiedSplat [5] -> [11].
-->
<!--
Wave 15-U (issue #32), 2026-09-26: pivot decision v5 (VLA/VLM + world models). Outputs table unchanged; the
line "P1-P3 present one method ... P4 is optional" was cut for the page limit (the table already says it). Risks: "real-only learning" -> "real-only fine-tuning" of the same pretrained VLA
(H4(a), §7 v5), Suomela [12] -> [13]. New: compute (~23k H100-hours = our estimate, §9 and
research/vla-wm-crowdedness.md §4, UNVERIFIED until the T3.1 pilot); crowded field / scooping (S2 counts Q1
126, Q2 183 papers in 2026 to 26 Sep; TwinRL arXiv:2602.09023 = §6 [17], VLAW arXiv:2602.12063 = §6 [21];
replaces the old twin-based scooping list [3-7, 13]); VLA licences merged with dataset licence and robot
access (OpenVLA README: models "derived from Llama-2" and "subject to the Llama Community License"; HF
a8cheng/navila-llama3-8b-8f without a licence tag; facebook/nwm and Cosmos-Predict2 gated; openpi
Apache-2.0). "Twin uncertainty is poorly calibrated" kept.
-->
<!--
Wave 14 (issue #30), 2026-09-26: pivot decision v4 (framing only). Outputs table: P1-P3 described by method
component (P1 = C1 + first C2, P2 = C3, P3 = the whole method in both testbeds, H4); venues unchanged; code column "C3 code" / "Method release". "P1-P3 are the linked
core" -> "present one method". Risk "task-aware capture gives no gain" generalized to any component
(a failed ablation leaves the other components and H4 testable).
-->
<!--
(history) Wave 13 (issue #29), 2026-09-26: pivot decision v3 (general, domain-agnostic real-to-sim-to-real; equal
testbeds). Outputs table: P1-P3 venues unchanged; P2 "few real data", P3 "both testbeds"; "Rollout
selection" -> "Trial selection". Host 2 no longer described as navigation work (only "Gaussian-splatting
scene models", as verified at https://msl.stanford.edu/). PWr manipulator for tier C only "if available"
(K29 Laboratorium Robotyki, availability UNVERIFIED). Risks: uncertainty calibration covers the physical
posterior; proxy-reality risk names the shared physics engine in manipulation and tier B. Citations
renumbered to the Wave 13 §6 list: EmbodiedSplat [3]->[5], Suomela [10]->[12], twin-based works
[3-7, 11] -> [3-7, 13] (RialTo, SplatSim, EmbodiedSplat, Vid2Sim, GaussGym, CASHER).
-->
<!--
Review-3 (issue #27), 2026-09-26: R3-F3 P2 = ICML or CVPR 2028 (§3 T5.3); P1 = first H2 results; R3-F1
proxy-reality risk names the separate-capture reference and the second-reference sign check (§9).
-->
<!--
Wave 11 (issue #26), 2026-09-26: rewritten for pivot decision v2 (research/pivot-decision.md). Outputs
table follows its paper plan (P1 NeurIPS 2027 RQ1+RQ2; P2 ICLR/CVPR 2028 RQ3; P3 NeurIPS 2028 RQ4, fallback
ICLR 2029; P4 optional). Data column became "Code" (no benchmark, no policy zoo). Risks rebuilt for the
loop: no-gain capture, 3DGS uncertainty calibration, proxy reality easier than reality (§7 caveat,
niches-eval.md N5), real-only baseline strong at small budgets (crowdedness.md 4.2 warning, Suomela et al.
RA-L 2026 = §6 [10]), scooping by twin groups (crowdedness.md 3.1: EmbodiedSplat, GaussGym, CASHER,
ReaDy-Go), licence/robot access. European host no longer tied to weight-space learning (representation
thesis dropped); no person or lab is named because none is contacted. EmbodiedSplat is now §6 [3].
-->
<!--
Wave 6 (issue #15), 2026-09-26: P3 = cross-task (manipulation) paper, ECCV 2028 / NeurIPS 2028 or RSS 2028
(RSS Lp 1277, 200 pts, ITiT); the old "robot paper to RSS" sentence folded into P3's venue list. New risk:
scope creep from manipulation -> simulation-only fallback (coordinator decision). K29 Laboratorium Robotyki
manipulators listed at https://lr.kcir.pwr.edu.pl/ (research/resources.md §1); availability for this project
UNVERIFIED and not agreed, hence "optional ... may use".
-->
<!--
Issue #12 (coordinator decisions, 2026-09-26): outputs table = 200-pt conferences of the 5.01.2024 list
assigned to ITiT only (NeurIPS Lp 87, ICML 847, ICLR 1674, CVPR 417, ICCV 442, ECCV 331, AAAI 1227,
IJCAI 983, RSS 1277; verified by the coordinator in the official xlsx). RA-L, IROS, RAS removed. Venue-to-
semester mapping aligned to past-cycle deadlines and accepted by the coordinator; P4 optional; RSS only as an
option for the robot validation paper. Resubmission path caveat: the NeurIPS decision (~late Sep) nearly
coincides with the ICLR deadline (NeurIPS 2026 notification 24 Sep 2026, ICLR 2027 deadline 25 Sep 2026), so
after a NeurIPS rejection the reliable next slots are CVPR (~Nov) and ICML (~Jan). All 2027–2029 deadlines
are expected from past cycles and UNVERIFIED; sources and dates in research/venues-200.md.
Risk "robot time exceeds lab access" dropped: robot = validation, ~16 h per campaign (§9).
Earlier sources (issues #6, #9) still valid:
- Minigranty SzD: https://szd.pwr.edu.pl/doktoranci/minigranty (up to 20k PLN, years 2–4; next edition
  ~Jan 2027 UNVERIFIED). Preludium 26 timing (~Mar–Jun 2027) inferred from previous calls, UNVERIFIED.
- NAWA Bekker: open to doctoral-school students; next call UNVERIFIED; stays 3–24 months (resources.md §5).
  Erasmus+ short-term 5–30 days, continuous recruitment (resources.md §5).
- Host 1: https://msl.stanford.edu/ (checked 2026-09-26). Host 2: https://arxiv.org/abs/2509.17430
  (EmbodiedSplat, ICCV 2025). Neither host contacted; willingness to host is UNVERIFIED.
- K29 Denali: https://denali.kcir.pwr.edu.pl/robots.php ; K46 has no robotics group:
  https://ai.pwr.edu.pl/research-groups (resources.md §1). Collaboration not yet agreed.
- genwro.AI: https://ai.pwr.edu.pl/research-groups; no verified 3DGS work, so only "consultations are
  possible".
- ACL SRW paper: doi:10.18653/v1/2025.acl-srw.61; pre-PhD, background only.
-->

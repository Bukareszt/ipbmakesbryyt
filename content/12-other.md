# §12 Inne / Other comments (max 1 page)

**Planned outputs by year** (200-point conferences assigned to the discipline, list of 5.01.2024).

| Year | Papers (planned submission, 200 points each) | Code | Grants | Mobility, events |
|---|---|---|---|---|
| 1 (2025/26) | — | — | — | — |
| 2 (2026/27) | P1 (method components C1 and first C2 results, RQ1–RQ2): NeurIPS 2027, May 2027 (§11) | Loop on tier A | SzD Minigrant; NCN PRELUDIUM; NAWA Bekker | Summer school poster |
| 3 (2027/28) | P2 (component C3, few real data, RQ3): ICML or CVPR 2028; P3 (the whole method in both testbeds, RQ4): NeurIPS 2028 | C3 code | — | Mid-term; 3-month visit (sem. 6) |
| 4 (2028/29) | Optional P4, consolidated study: ICLR 2029 or CVPR 2029 | Method release | — | Dissertation |

**Foreign research visit (candidate hosts, not yet contacted).** (1) Z. Kira's group, Georgia Tech:
EmbodiedSplat [5]. (2) Multi-robot Systems Lab, Stanford University (M. Schwager): Gaussian-splatting scene
models. A European host (Erasmus+ route) working on active reconstruction or sim-to-real
transfer, and a foreign co-author for P2, are sought with the supervisor in sem. 4.

**Collaboration at PWr.** Robot validation is planned with the K29 *Denali* laboratory (Pioneer 3-DX,
Jaguar 4x4, ROS 2) and, if available, a PWr manipulator; a written agreement is task T3.2 (Nov 2026).

**Risks and mitigation** (semester affected).
- *One component gives no gain* (3–5): its budget curve still answers its RQ; H4 is still tested.
- *Twin uncertainty is poorly calibrated* (3–4): two estimators and an ensemble fallback.
- *Proxy reality is easier than reality* (4–7): separate sources for twin and reference; tiers B and C
  check the direction (§9).
- *Real-only fine-tuning is strong at small budgets* (6): gains saturate quickly in a known location
  [13]; H4 is reported as a full budget curve.
- *Compute* (3–7): ~23k H100-hours (§9); WCSS and PLGrid grants in sem. 3; LoRA and small VLAs for
  development; if short, fewer seeds and one VLA.
- *Crowded field, scooping* (3–6): VLA fine-tuning in simulation and world models is crowded, and twin
  RL for VLAs exists [17, 21]; we claim only the real-data budget of the loop; early preprints.
- *Licences, robot access* (3, 5, 7): OpenVLA weights carry Llama 2 terms and some checkpoints are
  gated, so openpi's π0 is the fallback; without a robot, tier C moves by a semester (tier A decides).
- *Rejection at a top venue* (4–7): each paper has a resubmission path inside the 200-point set 2–4 months
  later (NeurIPS → CVPR → ICML → ECCV/ICCV).

**Prior work (background only).** A pre-PhD NLP paper (ACL 2025 SRW, forecasting from hidden states); not
part of the dissertation.

**Ethics and data.** Own captures are anonymized (GDPR); public datasets are used under their licences.

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

# §12 Inne / Other comments (max 1 page)

**Planned outputs by year** (200-point conferences assigned to the discipline, list of 5.01.2024).

| Year | Papers (planned submission, 200 points each) | Code | Grants | Mobility, events |
|---|---|---|---|---|
| 1 (2025/26) | — | — | — | — |
| 2 (2026/27) | P1 (RQ1–RQ2, task-aware capture, uncertainty-aware training): NeurIPS 2027, May 2027 (§11) | Loop on tier A | SzD Minigrant; NCN PRELUDIUM; NAWA Bekker | Summer school poster |
| 3 (2027/28) | P2 (RQ3, few real rollouts, twin correction): CVPR or ICLR 2028; P3 (RQ4, budget of the full loop, manipulation): NeurIPS 2028 | Rollout selection | — | Mid-term; 3-month visit (sem. 6) |
| 4 (2028/29) | Optional P4, consolidated study: ICLR 2029 or CVPR 2029 | Full release | — | Dissertation |

P1–P3 are the linked core of the dissertation; P4 is optional.

**Foreign research visit (candidate hosts, not yet contacted).** (1) Z. Kira's group, Georgia Tech:
EmbodiedSplat [3]. (2) Multi-robot Systems Lab, Stanford University (M. Schwager): Gaussian-splatting scene
models and navigation. A European host (Erasmus+ route) working on active reconstruction or sim-to-real
transfer, and a foreign co-author for P2, are sought with the supervisor in sem. 4.

**Collaboration at PWr.** Robot validation is planned with the K29 *Denali* laboratory (Pioneer 3-DX,
Jaguar 4x4, ROS 2); a written agreement is task T3.2 (Nov 2026).

**Risks and mitigation** (semester affected).
- *Task-aware capture gives no gain* (3–4): the measured capture–SR curves still answer RQ1, and Stages
  II–III have their own baselines (§7).
- *3DGS uncertainty is poorly calibrated* (3–4): two estimators and an ensemble fallback, checked against
  the reference twin.
- *Proxy reality is easier than reality* (4–7): the proxy's own error is reported; tier C checks the
  direction of the effects.
- *Real-only learning is strong at small budgets* (6): gains saturate quickly in a known location [10];
  H4 is reported as a full budget curve.
- *Scooping* (3–6): twin-based robot learning moves fast [3–7, 11]; early preprints, monthly monitoring.
- *Dataset licence or robot access* (3, 5): other public scans with reference geometry, own phone captures
  of PWr rooms; without a robot, tier C moves by a semester and hypotheses are still decided on tier A.
- *Rejection at a top venue* (4–7): each paper has a resubmission path inside the 200-point set 2–4 months
  later (NeurIPS → CVPR → ICML → ECCV/ICCV).

**Prior work (background only).** A pre-PhD NLP paper (ACL 2025 SRW, forecasting from hidden states); not
part of the dissertation.

**Ethics and data.** Own captures are anonymized (GDPR); public datasets are used under their licences.

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

# §12 Inne / Other comments (max 1 page)

**Planned outputs by year.** All papers target 200-point conferences assigned to the discipline (list of
5.01.2024; re-checked against the new list).

| Year | Papers (planned submission, 200 points each) | Data and code | Grants | Mobility, events |
|---|---|---|---|---|
| 1 (2025/26) | — | — | — | — |
| 2 (2026/27) | P1 (RQ1, paired-frame benchmark and gap localization): NeurIPS 2027, May 2027 (§11) | Benchmark v1 | SzD Minigrant; NCN PRELUDIUM; NAWA Bekker | Summer school poster |
| 3 (2027/28) | P2 (RQ2, forecasting transfer and failure): CVPR or ICLR 2028; P3 (RQ3–RQ4, budget allocation, manipulation): NeurIPS 2028 | Policy zoo | — | Mid-term; 3-month visit (sem. 6) |
| 4 (2028/29) | Optional P4, consolidated study: ICLR 2029 or CVPR 2029 | Full release | — | Dissertation |

P1–P3 are the thematically linked core of the dissertation; P4 is optional.

**Foreign research visit (candidate hosts, not yet contacted).** (1) Z. Kira's group, Georgia Tech:
EmbodiedSplat [4]. (2) Multi-robot Systems Lab, Stanford University (M. Schwager): Gaussian-splatting scene
models and navigation. A European host (Erasmus+ route) from the weight-space learning community (authors
of [25–27]) and a foreign co-author for P2 are sought with the supervisor in sem. 4.

**Collaboration at PWr.** Real-robot validation is planned with the *Denali* Autonomous Robots Laboratory
(K29, W12N; Pioneer 3-DX, Jaguar 4x4, ROS 2); a written agreement is task T3.2 (Nov 2026).

**Risks and mitigation** (semester affected).
- *Policy zoo too small* (4–5): small policies, shared frozen encoders, imitation of a privileged planner;
  the sem. 3 pilot fixes the size; WCSS and PLGrid grants.
- *Twin–real pairs unavailable* (3): licence or quality limits on the chosen dataset. Other public datasets
  with real captures and reference scans, and own captures at PWr.
- *Scooping* (3–6): failure detection and policy interpretability move fast. Early preprints, benchmark
  release, monthly literature monitoring; the zoo and weight-space angle differentiate the work.
- *Predictor learns only twin fidelity* (5): ablations with fixed fidelity; a negative result still answers RQ2.
- *Proxy reality differs from reality* (5–7): tier C campaigns check agreement; they can move by a semester.
- *Rejection at a top venue* (4–7): every paper has a resubmission path inside the 200-point set, 2–4
  months later (e.g. NeurIPS → CVPR → ICML → ECCV/ICCV), so the degree requirement does not depend on one
  decision.

**Prior work (background only).** A pre-PhD NLP paper (ACL 2025 SRW) forecasts from hidden states with a
graph neural network over layers; Stage II adapts the method, but the paper is not part of the dissertation.

**Ethics and data.** Own captures anonymize personal data (GDPR); public datasets are used under their licences.

<!--
Review-2 (issue #24), 2026-09-26: R2-F15 Bekker application is T4.3 (sem. 4 = year 2), so it moved to the
year-2 grants cell. R2-F4 P3 = NeurIPS 2028 only (§3 T6.3). R2-F11 the European host search now names the
community closest to RQ2 (weight-space learning, §6 [25]-[27]); no person or lab is named because none is
contacted.
-->
<!--
Wave 9 (issue #23), 2026-09-26: rewritten for the pivot (research/pivot-decision.md). Outputs table follows
the pivot's paper plan (P1 NeurIPS 2027 RQ1; P2 ICLR/CVPR 2028 RQ2; P3 NeurIPS/ECCV 2028 RQ3+RQ4; P4
optional) and adds a data/code column (benchmark, zoo). New risks: zoo too small, twin-real pairs
unavailable, scooping (novelty-options.md §3 risks), predictor learns only fidelity, proxy reality. Removed:
risks about reconstruction quality, SRCC failure and manipulation scope creep, the K29 manipulator and
genwro.AI sentences (for the page limit; not needed after the pivot). EmbodiedSplat is now §6 ref [4].
Scooping evidence: failure-detection and VLA-interpretability counts in novelty-options.md / niches-models.md.
Prior-work sentence: doi:10.18653/v1/2025.acl-srw.61 (novelty-options.md §3: "forecasts from LLM hidden
states with a GNN over layers").
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

# §12 Inne / Other comments (max 1 page)

I used Claude (via Claude Code) for literature search, drafting and editing, and I reviewed all content and references myself.

### Bibliography
[1] Maddukuri, A., et al. (2025). Sim-and-real co-training: A simple recipe for vision-based robotic manipulation. RSS.
[2] Kadian, A., et al. (2020). Sim2Real predictivity: Does evaluation in simulation predict real-world performance? RA-L.
[3] Ben-David, S., et al. (2010). A theory of learning from different domains. Machine Learning.
[4] Zhao, H., et al. (2019). On learning invariant representations for domain adaptation. ICML.
[5] Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. IROS.
[6] Chebotar, Y., et al. (2019). Closing the sim-to-real loop: Adapting simulation randomization with real world experience. ICRA.
[7] Tiboni, G., et al. (2024). Domain randomization via entropy maximization. ICLR.
[8] Ganin, Y., et al. (2016). Domain-adversarial training of neural networks. JMLR.
[9] Cheng, S., et al. (2025). Generalizable domain adaptation for sim-and-real policy co-training. NeurIPS.
[10] Lei, Y., et al. (2026). A mechanistic analysis of sim-and-real co-training in generative robot policies. arXiv:2604.13645.
[11] Kerbl, B., et al. (2023). 3D Gaussian splatting for real-time radiance field rendering. ACM TOG.
[12] Torne, M., et al. (2024). Reconciling reality through simulation: A real-to-sim-to-real approach for robust manipulation. RSS.
[13] Qureshi, M. N., et al. (2025). SplatSim: Zero-shot Sim2Real transfer of RGB manipulation policies using Gaussian splatting. ICRA.
[14] Xu, Q., et al. (2026). TwinRL: Digital twin-driven reinforcement learning for real-world robotic manipulation. arXiv:2602.09023.
[15] Li, X., et al. (2024). Evaluating real-world robot manipulation policies in simulation. CoRL.
[16] Jain, A., et al. (2025). PolaRiS: Scalable real-to-sim evaluations for generalist robot policies. arXiv:2512.16881.
[17] Chhablani, G., et al. (2025). EmbodiedSplat: Personalized real-to-sim-to-real navigation with Gaussian splats from a mobile device. ICCV.
[18] Xie, Z., et al. (2025). Vid2Sim: Realistic and interactive simulation from video for urban navigation. CVPR.
[19] Jin, R., et al. (2026). Grounding sim-to-real generalization in robotic manipulation: An empirical study with vision-language-action models. ECCV.
[20] Wang, X., et al. (2026). ReVeal: A reconstruction-aware real-to-sim framework for VLA policy evaluation. arXiv:2609.23910.
[21] Kachaev, N., et al. (2026). Don't blind your VLA: Aligning visual representations for OOD generalization. AAMAS.
[22] Lee, Y., et al. (2023). Surgical fine-tuning improves adaptation to distribution shifts. ICLR.
[23] Memmel, M., et al. (2024). ASID: Active exploration for system identification in robotic manipulation. ICLR.
[24] Agia, C., et al. (2025). CUPID: Curating data your robot loves with influence functions. CoRL.
[25] Xie, A., et al. (2024). Decomposing the generalization gap in imitation learning for visual robotic manipulation. ICRA.
[26] Liao, A., et al. (2026). Active real-world factor-based evaluation for generalist robot policies. arXiv:2607.14439.


<!-- Wave 31: grounding + clarity (ultracode) -->
<!-- Wave 29: humanized (no semicolons) -->
<!-- Wave 28: restyled after the accepted 2025 IPB (2026-09-28, research/accepted_plan_tts_2025.txt). §12 now holds the AI-use disclosure (Claude via Claude Code) and the Bibliography moved from §6, numbering [1]-[23] unchanged. -->
<!--
Wave 18-W (issue #35), 2026-09-26: pivot decision v7 (research/pivot-decision.md, top) and the
deep-research report (reports/Uczenie nawigacji w cyfrowych bliźniakach.md, "Walidność proxy i wyścig z
dużymi laboratoriami" and "Rekomendacje"). Outputs table: P1 = mechanism 1 (H1) + H1 preprint, P2 =
mechanisms 2-3 + first manipulation results, P3 = whole method + manipulation (v7 papers); "Grants,
licences" column adds the ScanNet++ licence and the PLGrid grant (sem. 3). Robot: TurtleBot 4 Lite
(~1699 EUR gross per the report, Elektor listing; within the SzD Minigrant of up to 20k PLN) is named only
as "a small mobile robot bought from an SzD Minigrant" here (§9 names the model); K29 Denali kept as the
alternative. New risks from the report: proxy validity (Kadian SRCC 0.18 -> 0.844 after one artefact, [4]),
physical gap (GaussGym "uniform physical parameters"), success ceiling and noise (twins 70-100% zero-shot;
10-20 real trials confirm direction only), scooping with the named one-step groups ([12] EmbodiedSplat,
[18] TwinRL, [32] VLAW; report also names FisherRF/RaEM, Splat-Nav/VISTA, Pavone group), ScanNet++
licence (ToU: non-commercial, "strictly prohibited" redistribution, revocable, supervisor's handwritten
signature), static scenes only (ReaDy-Go added moving people). Openness per recommendation 4: code,
configurations, scene IDs, seeds, pre-registrations; MuSHRoom (CC-BY-4.0) and own rooms as releasable.
"Future applicability" paragraph removed (manipulation is now inside the plan). "Twin uncertainty is poorly
calibrated" merged into "one mechanism gives no gain" for space. Refs renumbered to the Wave 18 §6 list:
EmbodiedSplat [11]->[12], Suomela [8]->[9], TwinRL [27]->[18], VLAW [28]->[32], Kadian = [4].
-->
<!--
(history) Wave 16-W (issue #33), 2026-09-26: pivot decision v6 (navigation only; manipulation "at most as future
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

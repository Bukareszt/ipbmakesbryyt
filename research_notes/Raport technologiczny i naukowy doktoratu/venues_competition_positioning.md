# Venues, competition and positioning for the PhD (PWr, ITiT, 2025-2029): representation learning for sim/real generalization of world models and robot policies

Context read from the IPB (content/07, content/09, visible text only): RQ1/H1 = prediction target of a world model built from real data (pretrained video-encoder features, e.g. V-JEPA 2, vs pixel-autoencoder codes, at equal action following), policy trained on filtered imagined trajectories, BridgeData V2 + SIMPLER, following Nilaksh et al. RQ2/H2 = world model trained on physics-simulation data; a sim/photoreal feature-consistency objective vs only adding Cosmos-Transfer photoreal frames. RQ3/H3 = encoder further pretrained on real+sim with the H2 objective needs less real data to adapt. RQ4/H4 = unseen scenes and navigation (RAE-NWM, RECON/SCAND), real checks on the Wojtek robot dog and the department humanoid. §9 of the IPB currently says: "journals worth 200 points on the ministerial list, such as NeurIPS, ICML, ICLR, CVPR, RSS and IEEE RA-L". Status date of these notes: 29 Sep 2026.

## Q1. Ministerial list: which venues are worth 200 points, and what changes in 2026/2027; expected 2027-2028 deadlines

### Takeaway
Under the list in force now (communique of 5 Jan 2024), NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, RSS, RA-L, T-RO, IJRR, TPAMI and IJCV are all 200 points, but IROS is 140, ICRA only 70, and CoRL is not on the list at all. A new regulation (30 Apr 2026, in force 27 May 2026) scores conferences directly from ICORE ranks (A* = 200, A = 140, B = 70, C = 40). The new list is due by the end of 2026 and will be signed in early 2027, so it will score most of the PhD's papers. Under ICORE2026, ICRA is A* (200 expected), IROS is A (140), CoRL is "Unranked", and RSS was left out of the 2026 ranking. **The IPB sentence counting RSS among 200-point venues holds for the current list only. It is probably wrong for 2027 onwards, and it wrongly calls conferences "journals".**

### Cited Findings

**Current list (in force for 2026 publications)**
- The newest list published on gov.pl is the "Komunikat Ministra Nauki z dnia 5 stycznia 2024 r. w sprawie wykazu czasopism naukowych i recenzowanych materiałów z konferencji międzynarodowych". No 2025 or 2026 list appears on the official page. — [gov.pl, opublikowane wykazy](https://www.gov.pl/web/nauka/ujednolicony-wykaz-czasopism-naukowych); [komunikat 5.01.2024](https://www.gov.pl/web/nauka/komunikat-ministra-nauki-z-dnia-05-stycznia-2024-r-w-sprawie-wykazu-czasopism-naukowych-i-recenzowanych-materialow-z-konferencji-miedzynarodowych)
- Values below were read directly from the official XLSX attached to that communique (sheet "Konferencje_nauk", 1,735 conferences: 63 at 200 pts, 178 at 140, 440 at 70, 1,052 at 20). Every listed conference below has the disciplines "informatyka techniczna i telekomunikacja; informatyka". — [official XLSX, gov.pl attachment](https://www.gov.pl/attachment/c2510527-171a-451e-b3c4-74ea5a5c6c94)
  - 200 pts: NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, **RSS** (listed as "Robotics: Systems and Science [RSS]"), AAAI, IJCAI, AAMAS, KDD.
  - 140 pts: **IROS**, AISTATS, UAI, WACV, ECAI, ECML PKDD, FSR, ISRR, ISR.
  - 70 pts: **ICRA**, ACCV, ICPR, IJCNN, ICONIP, RoboCup, EWLR.
  - 20 pts: WAFR, ICINCO, MMAR, ACML, ICARCV.
  - **CoRL: not on the list** (no entry matching "Robot Learning"/"CoRL"). Humanoids and HRI: not found either.
- Journals in the same XLSX (sheet "Czasopisma _nauk"). Journals marked "ITiT" are assigned to informatyka techniczna i telekomunikacja. — [official XLSX](https://www.gov.pl/attachment/c2510527-171a-451e-b3c4-74ea5a5c6c94)
  - 200 pts: IEEE RA-L (ITiT), IEEE T-RO (ITiT), IJRR (ITiT), IEEE TPAMI (ITiT), IJCV (ITiT), IEEE TNNLS (ITiT), IEEE TIP (ITiT), Neural Networks (ITiT), Artificial Intelligence (ITiT).
  - 140 pts: JMLR (ITiT), Machine Learning (ITiT), Robotics and Autonomous Systems (ITiT), Pattern Recognition (ITiT), JAIR (ITiT), IEEE T-ASE (ITiT), IEEE Robotics & Automation Magazine, Journal of Field Robotics, IEEE/ASME T-Mech.
  - 100 pts: Autonomous Robots (ITiT), CVIU.
  - 20 pts: Science Robotics (no ITiT assignment), Nature Machine Intelligence (ITiT). These look anomalous, most likely because the journals were new when the list was built, but they are what the file says.
  - TMLR: not found in the list.

**New regulation and new list**
- Regulation: "Rozporządzenie Ministra Nauki i Szkolnictwa Wyższego z dnia 30 kwietnia 2026 r. w sprawie sporządzania wykazu wydawnictw monografii naukowych oraz wykazu czasopism naukowych i recenzowanych materiałów z konferencji międzynarodowych" (Dz.U. 2026 poz. 630). Published 12 May 2026, in force 27 May 2026 (§ 22: 14 days after publication). — [ISAP record](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000630); [text via INFORLEX](https://www.inforlex.pl/dok/tresc,DZU.2026.132.0000630,ROZPORZADZENIE-MINISTRA-NAUKI-I-SZKOLNICTWA-WYZSZEGO-z-dnia-30-kwietnia-2026-r-w-sprawie-sporzadzania-wykazu-wydawnictw-monografii-naukowych-oraz.html)
- § 16 ust. 1 pkt 1 (conferences, by ICORE category): "200 punktów, jeżeli konferencja naukowa posiada kategorię A*"; 140 for A; 70 for B; 40 for C; 20 for "Australasian albo Regional". § 16 ust. 2 lets the KEN move a conference by up to two point thresholds if its category does not reflect its real scientific standing. — [INFORLEX text](https://www.inforlex.pl/dok/tresc,DZU.2026.132.0000630,ROZPORZADZENIE-MINISTRA-NAUKI-I-SZKOLNICTWA-WYZSZEGO-z-dnia-30-kwietnia-2026-r-w-sprawie-sporzadzania-wykazu-wydawnictw-monografii-naukowych-oraz.html); confirmed by [Forum Akademickie, 13 May 2026](https://forumakademickie.pl/opublikowano-rozporzadzenie-dotyczace-sporzadzania-wykazow-czasopism-i-wydawnictw/)
  - **Conflict:** one search snippet claimed conferences would get only 20-100 points (A* = 100). This does not match the published text quoted above. It probably came from a draft version and should not be used.
- § 10 ust. 2 (journals, by percentile or the median of percentiles, CiteScore/JIF-type indicators): 200 pts for ≥93rd percentile; 140 for 75-93; 100 for 50-75; 70 for 25-50; 40 below 25. — [INFORLEX text](https://www.inforlex.pl/dok/tresc,DZU.2026.132.0000630,ROZPORZADZENIE-MINISTRA-NAUKI-I-SZKOLNICTWA-WYZSZEGO-z-dnia-30-kwietnia-2026-r-w-sprawie-sporzadzania-wykazu-wydawnictw-monografii-naukowych-oraz.html)
- The list will cover journals indexed in Scopus/WoS as of 1 July 2026 and conference proceedings in ICORE (in DBLP). Journals get at least 40 points (previously 20). — [prawo.pl](https://www.prawo.pl/student/wykaz-wydawnictw-i-czasopism-naukowych-rozporzadzenie-2026,1544689.html)
- Timeline: MNiSW announcement of 2 June 2026: the new list will be "opracowany i opublikowany do końca 2026 r.", signed "na początku 2027 r.", and "o roku obowiązywania wykazu decyduje data jego podpisania". So the 2024 list keeps scoring 2026 publications, and the new list applies from 2027. — [gov.pl, nowy termin publikacji wykazu](https://www.gov.pl/web/nauka/nowy-termin-publikacji-wykazu-czasopism-naukowych); [Forum Akademickie](https://forumakademickie.pl/kolejna-zmiana-terminu-wykaz-czasopism-do-konca-tego-roku/)
  - **Conflict/superseded:** the 13 May 2026 Forum Akademickie article said the lists would apply retroactively from 1 Jan 2026 (evaluation 2026-2030). The 2 June ministry announcement replaced that. — [Forum Akademickie 13.05.2026](https://forumakademickie.pl/opublikowano-rozporzadzenie-dotyczace-sporzadzania-wykazow-czasopism-i-wydawnictw/)

**ICORE2026 ranks (these will drive conference points from 2027), read from the ICORE portal**
- A*: NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, **ICRA**, HRI, AAAI, IJCAI. — [ICORE portal search](https://portal.core.edu.au/conf-ranks/?search=robot&by=all&source=all&sort=atitle&page=1)
- A: **IROS**, AISTATS, WACV, BMVC. C: ISRR. — [ICORE portal](https://portal.core.edu.au/conf-ranks/?search=robot&by=all&source=all&sort=atitle&page=1)
- **CoRL: ICORE2026 "Unranked"** (portal note: "Requested to be added as unranked, decision Unranked"). — [ICORE CoRL entry](https://portal.core.edu.au/conf-ranks/2308/)
- **RSS: latest source CORE2023, rank "TBR"**, portal note: "No submission in 2025, so excluded from 2026 rankings". Earlier ranks were A* (CORE2008-2018), removed 2020. — [ICORE RSS entry](https://portal.core.edu.au/conf-ranks/1709/)
- Humanoids: only an old ERA2010 "C" entry. — [ICORE portal](https://portal.core.edu.au/conf-ranks/?search=Humanoid&by=all&source=all&sort=atitle&page=1)

**Deadlines (confirmed where official; otherwise EXPECTED from the pattern of past cycles)**
- ICLR 2027: abstract 18 Sep 2026, full paper 25 Sep 2026 (AoE), conference 26-30 Apr 2027. The deadline has passed. — [ICLR 2027 CfP](https://iclr.cc/Conferences/2027/CallForPapers)
- ICRA 2027 (Seoul, 24-28 May 2027): paper deadline 15 Sep 2026 23:59 PST, extended by 24 h to 16 Sep. Passed. — [ICRA 2027 CfP](https://2027.ieee-icra.org/announcements/call-for-technical-papers/); [ICRA on X](https://x.com/ieee_ras_icra/status/2089365401201201516)
- CVPR 2027 (Seattle, June 2027): registration 10 Nov 2026, paper 16 Nov 2026 AoE, supplementary 23 Nov 2026. — [CVPR 2027 CfP](https://cvpr.thecvf.com/Conferences/2027/CallForPapers); [CVPR 2027 dates](https://cvpr.thecvf.com/Conferences/2027/Dates)
- Past-cycle dates from the community-maintained Hugging Face ai-deadlines data (secondary source) — [huggingface/ai-deadlines](https://github.com/huggingface/ai-deadlines):
  - ICML: 30 Jan 2025; 28 Jan 2026 (Seoul, 6-11 Jul 2026).
  - RSS: 24 Jan 2025; 30 Jan 2026 (Sydney, 13-17 Jul 2026).
  - IROS: 2 Mar 2025; 7 Mar 2026 (Pittsburgh, 27 Sep-1 Oct 2026).
  - ICCV: 8 Mar 2025 (Honolulu).
  - ECCV: 5 Mar 2026 (Malmö, 8-12 Sep 2026).
  - NeurIPS: 15 May 2025; 6 May 2026 (Sydney, 6-12 Dec 2026).
  - CoRL: 29 May 2026 (Austin, 9-12 Nov 2026).
- EXPECTED (my extrapolation, not announced):
  - ICML 2027: late Jan 2027. RSS 2027: late Jan/early Feb 2027. IROS 2027: early Mar 2027. ICCV 2027: early Mar 2027. NeurIPS 2027: early/mid May 2027. CoRL 2027: late May 2027.
  - ICLR 2028: late Sep 2027. ICRA 2028: ~15 Sep 2027. CVPR 2028: mid Nov 2027.
  - ICML 2028: late Jan 2028. RSS 2028: late Jan 2028. ECCV 2028: early Mar 2028. IROS 2028: early Mar 2028. NeurIPS 2028: May 2028. CoRL 2028: late May 2028.

### Inferences
- Points per venue under the current list vs the expected new list:
  - NeurIPS/ICML/ICLR/CVPR/ICCV/ECCV: 200 → 200 (A*).
  - ICRA: 70 → probably 200 (A*).
  - IROS: 140 → 140 (A).
  - RSS: 200 → probably absent or unscored, because it is not in ICORE2026. The KEN can only move listed conferences, so this is a real risk.
  - CoRL: 0 → probably 0 (Unranked).
- For journals, RA-L, T-RO, IJRR, TPAMI and IJCV are very likely to stay ≥93rd percentile and keep 200 under § 10. This is not verified until the new list is published.
- For the IPB (§9): replace "journals worth 200 points ... such as NeurIPS, ICML, ICLR, CVPR, RSS and IEEE RA-L" with "conferences and journals". Keep RSS only with a caveat, or swap it for ICRA/RA-L. The ICRA+RA-L route (an RA-L paper presented at ICRA or IROS) is the robotics route most likely to be worth 200 under both lists.
- For papers in 2027-2029, the realistic timing for an IPB defended in 2026/27 is:
  - ICML (Jan) and NeurIPS (May) 2027 for the RQ1 paper.
  - CVPR (Nov 2027) or ICRA 2028 (Sep 2027) for RQ2.
  - A journal (RA-L/T-RO) for the RQ3/RQ4 synthesis.

### Gaps
- I could not open the ISAP PDF itself (redirect loop). The regulation text was read via INFORLEX (a legal-database mirror) and cross-checked with Forum Akademickie.
- Not verified: whether the new list will include conference series outside ICORE (e.g. RSS, or CoRL via PMLR) in any other way, and whether the KEN will use § 16 ust. 2 for robotics venues. No draft of the new list was found.
- The evaluation rules for crediting an article in a journal not assigned to ITiT (e.g. Science Robotics) were not checked in this session.
- RA-L's rolling submission and its ICRA/IROS presentation options were not checked this session.

## Q2. Groups working closest to RQ1-RQ4 (2025-2026)

### Takeaway
The field is crowded and moving fast. The closest direct overlap is Nilaksh, Jha, Zholus and Chandar (Mila). On BridgeV2 they already compared six reconstruction vs semantic latent spaces for action-conditioned latent diffusion world models, and found V-JEPA 2.1 strongest on policy. On sim→real world models, the closest are Purdue with the RAI Institute (a sim-trained world-action model), the UT Austin CLeAR lab (SimDist, RSS 2026), and UT Austin RPL/Yuke Zhu (the mechanism of sim-real co-training via representation alignment). NVIDIA (Cosmos, DreamGen, DreamZero), Meta FAIR/NYU (V-JEPA 2, DINO-WM, SkyJEPA) and Stanford (Ctrl-World, VLAW) provide the base models and are adjacent competitors.

### Cited Findings

**RQ1: prediction target / latent space**
- Nilaksh, S. Jha, A. Zholus, S. Chandar, "Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models" (arXiv 2605.06388, 7 May 2026). They compare six encoders under a fixed protocol on BridgeV2. Visual fidelity alone is insufficient; VAE/Cosmos win on pixels, but "semantic encoders such as V-JEPA 2.1 (strongest overall on policy), Web-DINO, and SigLIP 2 generally excel" at planning/policy and representation quality. — [arXiv 2605.06388](https://arxiv.org/abs/2605.06388)
- JEPA-WAM (Lin et al., arXiv 2608.09381, Aug 2026): a latent world-action model in a pretrained V-JEPA space, with a shared predictor for latent transitions and actions. — [arXiv 2608.09381](https://arxiv.org/abs/2608.09381)
- VLA-JEPA (Sun et al., arXiv 2602.10098, Feb 2026): JEPA-style "leakage-free" latent prediction pretraining for VLAs. It argues that pixel-anchored latent-action objectives are vulnerable to appearance bias. — [arXiv 2602.10098](https://arxiv.org/abs/2602.10098)
- World2Act (Vuong et al., arXiv 2603.10422): latent-space post-training of a VLA from world-model dynamics without pixel supervision. The motivation is that pixel supervision makes policies sensitive to world-model visual artefacts. — [arXiv 2603.10422](https://arxiv.org/abs/2603.10422)
- Contrastive World Models (B. Li, arXiv 2609.22175, Aug 2026): replaces Dreamer's reconstruction with a Deep-InfoMax bound, with gains under distractors and natural-video backgrounds. — [arXiv 2609.22175](https://arxiv.org/abs/2609.22175)
- WAM (Han & Yilmaz, arXiv 2603.28955): adds an inverse-dynamics objective to DreamerV2 so that latents capture action-relevant structure. — [arXiv 2603.28955](https://arxiv.org/abs/2603.28955)

**World models as simulators for policy training and evaluation**
- WoVR (Jiang et al., arXiv 2602.13977): world models as simulators for RL post-training of VLAs; addresses hallucination and error accumulation that policies exploit. — [arXiv 2602.13977](https://arxiv.org/abs/2602.13977)
- Prioritized Rollouts (Sheng et al., arXiv 2609.22879): world-model RL for VLAs. — [arXiv 2609.22879](https://arxiv.org/abs/2609.22879)
- Interactive World Simulator (Y. Wang et al., arXiv 2603.08546): consistency-model world models from moderate-sized robot data, for policy training and evaluation. — [arXiv 2603.08546](https://arxiv.org/abs/2603.08546)
- RoboWorld (Jeon et al., arXiv 2607.01060): policy evaluation with a fast autoregressive video world model. — [arXiv 2607.01060](https://arxiv.org/abs/2607.01060)
- WorldSimProbe (Co et al., arXiv 2608.09298): diagnoses the simulator faithfulness of action-conditioned world models. — [arXiv 2608.09298](https://arxiv.org/abs/2608.09298)
- Decision-centric evaluation position paper (Yu et al., arXiv 2606.15032). — [arXiv 2606.15032](https://arxiv.org/abs/2606.15032)

**RQ2: sim-trained world models transferring to real**
- Z. Wang, K. Sivakumar, J. Shang, Y. Hu, Z. Xie, R. Gong et al., "Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors" (arXiv 2606.31101, 30 Jun 2026; CVPR'26 Embodied AI Workshop). Affiliations on the HTML page: Purdue University and the Robotics and AI Institute.
  - Setup: builds on Cosmos Policy, uses extensive domain randomization and ~800 synthetic demos per task (AnyTask pipeline), and no real demos.
  - Result: 35% average zero-shot success on a Franka. The authors call it "the first successful sim-to-real transfer of a world-action model for robotic manipulation", and describe it as "part of early result" of a larger effort. — [arXiv 2606.31101](https://arxiv.org/abs/2606.31101); [HTML](https://arxiv.org/html/2606.31101)
- Y. Lei, M. Liu, A. Maddukuri, Z. Jiang, Y. Zhu, "A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies" (arXiv 2604.13645, Apr 2026). They identify "structured representation alignment", described as "a balance between cross-domain representation alignment and domain discernibility", as the primary effect, with "importance reweighting" as secondary. — [arXiv 2604.13645](https://arxiv.org/abs/2604.13645)

**RQ3: data-efficient adaptation**
- J. Levy, T. Westenbroek, K. Huang, F. Palafox, P. Yin, S. Omidshafiei et al., "Simulation Distillation" (SimDist; arXiv 2603.15759; RSS 2026; code by the CLeAR Robotics Lab). The whole world-model stack is pretrained in simulation. Then everything except dynamics is frozen, and dynamics is fine-tuned on a small amount of real data. — [arXiv 2603.15759](https://arxiv.org/abs/2603.15759); [RSS 2026 paper page](https://roboticsconference.org/program/papers/17/); [GitHub CLeARoboticsLab/simdist](https://github.com/CLeARoboticsLab/simdist)
- F. Palafox, D. Fridovich-Keil, "Amortized Low-Rank Adaptation for Model-Based RL" (arXiv 2609.12278, Sep 2026): few-episode adaptation of a world model to a test environment. — [arXiv 2609.12278](https://arxiv.org/abs/2609.12278)
- Y. Wang et al., "A Recipe for Efficient Sim-to-Real Transfer in Manipulation with Online Imitation-Pretrained World Models" (arXiv 2510.02538, Oct 2025): online imitation pretraining in simulation followed by offline real fine-tuning. — [arXiv 2510.02538](https://arxiv.org/abs/2510.02538)

**RQ4: variability, navigation, other embodiments**
- L. Zanatta, G. Malczyk, K. Alexis, "Generalization of World Models under Environmental Variability for Vision-based Quadrotor Navigation" (arXiv 2606.05015). A systematic cross-environment study of DreamerV3 world models under different levels of randomization, including SSL pretraining. — [arXiv 2606.05015](https://arxiv.org/abs/2606.05015)
- P. Rao, W. Zhang, R. Balestriero, Y. LeCun, G. Loianno, "SkyJEPA" (arXiv 2606.23444, under review): JEPA world models for zero-shot sim-to-real quadrotor control. — [arXiv 2606.23444](https://arxiv.org/abs/2606.23444)
- M. Zhang et al., "RAE-NWM" (arXiv 2603.09241): a navigation world model in dense DINOv2 space, motivated by DINOv2 features having stronger linear predictability than VAE latents. — [arXiv 2603.09241](https://arxiv.org/abs/2603.09241)

**Community signal**
- The Embodied AI Workshop 2026's overarching theme is "World Models for Embodied AI". — [embodied-ai.org](https://embodied-ai.org/)
- Surveys on world models for robot learning appeared in 2026 (arXiv 2605.00080, 2609.16074). — [arXiv 2605.00080](https://arxiv.org/abs/2605.00080); [arXiv 2609.16074](https://arxiv.org/pdf/2609.16074)

### Inferences
- Labs to watch, and cite as the "competition":
  - Mila / Chandar lab (RQ1).
  - Meta FAIR and NYU (LeCun, Pinto, Loianno), who build the V-JEPA 2 / DINO-WM backbones.
  - NVIDIA GEAR/Cosmos (the base models: Cosmos, Cosmos-Transfer, DreamGen, DreamZero).
  - Stanford (Finn group: Ctrl-World, VLAW; in the IPB references).
  - UT Austin RPL/Yuke Zhu with NVIDIA (co-training, RQ2).
  - UT Austin CLeAR/Fridovich-Keil (RQ3).
  - Purdue + RAI Institute (sim→real world-action models, RQ2).
  - NTNU Autonomous Robots Lab/Alexis (RQ4-style generalization).
- Some institutional affiliations above are from general knowledge; only the arXiv author lists and the Purdue/RAI HTML affiliations were checked in this session.
- Most of these groups have far more compute than a single PhD student. Their scale-driven results can easily overtake a "which is better" comparison. Controlled, confound-aware comparisons and a real-robot check are where a single PhD student can compete.

### Gaps
- No verified lab-page listing of each group's 2026 roadmap. Affiliations of RoboWorld, the Interactive World Simulator and JEPA-WAM authors were not verified.
- The arXiv API was rate-limited, so the systematic sweep of all 2026 arXiv papers was incomplete. A manual sweep of "world model" + "sim-to-real" before submission is advisable.

## Q3. Per RQ: likely scooping work, plausible novelty, scientific risks and fallbacks

### Takeaway
H1 is already partly answered in direction by Nilaksh et al. (semantic > reconstruction latents on BridgeV2 for policy). The novelty must lie in three places: controlling for action following, measuring policies trained on imagined data against a real-data baseline, and checking on real robots. H2 has a direct warning from Lei et al.: alignment helps only when balanced with domain discernibility, so a pure "same features for sim and photoreal" objective could underperform. RQ3 overlaps with SimDist but differs in what is adapted: SimDist freezes the encoder, while RQ3 changes how the encoder is pretrained. RQ4 has the fewest direct competitors, but navigation transfer is the least certain.

### Cited Findings

**RQ1/H1**
- The direction of H1 is pre-empted by Nilaksh et al.: V-JEPA 2.1 was strongest on policy, and pixel fidelity was a poor selector, on the same dataset (BridgeV2) that the IPB uses. — [arXiv 2605.06388](https://arxiv.org/abs/2605.06388)
- Related evidence, pointing the same way, that latent/semantic targets help policies: JEPA-WAM, VLA-JEPA and World2Act. — [2608.09381](https://arxiv.org/abs/2608.09381); [2602.10098](https://arxiv.org/abs/2602.10098); [2603.10422](https://arxiv.org/abs/2603.10422)
- WorldSimProbe argues that evaluations emphasize visual quality or task outcomes without testing action-conditioned fidelity. This supports the IPB's plan to compare targets at equal action following. — [arXiv 2608.09298](https://arxiv.org/abs/2608.09298)
- Risk: imagined rollouts suffer from hallucination and error accumulation, and policies exploit model errors. This can hide any effect of the prediction target. — [WoVR, arXiv 2602.13977](https://arxiv.org/abs/2602.13977)

**RQ2/H2**
- Closest scoop: a sim-trained world-action model on Cosmos Policy with heavy domain randomization, reaching 35% zero-shot on a real Franka. The authors describe it as an early part of a larger effort, so more is likely to come. — [arXiv 2606.31101](https://arxiv.org/abs/2606.31101)
- Risk evidence for H2: Lei et al. find that the primary effect is a balance between alignment and "domain discernibility", not maximal alignment. — [arXiv 2604.13645](https://arxiv.org/abs/2604.13645)
- Evidence that supports the "unless the gap comes mainly from physics" clause of H2: SimDist finds that encoder and value representations transfer from simulation, while the dynamics model needs real adaptation. — [arXiv 2603.15759](https://arxiv.org/abs/2603.15759)

**RQ3/H3**
- Closest work: SimDist (freeze encoder, fine-tune dynamics on small real data), amortized LoRA adaptation, and the online-imitation-pretrained world-model recipe. — [2603.15759](https://arxiv.org/abs/2603.15759); [2609.12278](https://arxiv.org/abs/2609.12278); [2510.02538](https://arxiv.org/abs/2510.02538)
- None of these three, as described in their abstracts, compares encoder-pretraining objectives (real vs real+sim with a sim-photoreal consistency loss) by real-data-efficiency curves for both a world model and a policy.

**RQ4/H4**
- Zanatta et al. show that world-model robustness to environmental variability is "poorly understood". They study it with cross-environment validation in quadrotor navigation, which is a methodological template for H4. — [arXiv 2606.05015](https://arxiv.org/abs/2606.05015)
- RAE-NWM shows that dense DINOv2 features beat VAE latents for navigation world models. This means H1's direction in navigation has partial prior support, which lowers the novelty of that half of H4 but also lowers its risk. — [arXiv 2603.09241](https://arxiv.org/abs/2603.09241)

### Inferences
- **What is plausibly novel.** None of the abstracts read covers any of these points, but the full papers were not all read, so each should be checked before claiming novelty:
  - RQ1: a matched-controllability comparison of prediction targets, measured by policies fine-tuned on success-filtered imagined data against a same-data real baseline and the SIMPLER/offline action-matching proxy, and checked on physical robots.
  - RQ2: a controlled one-factor comparison of the sources of the sim→real gap for world models (appearance DR vs photoreal transfer vs physics DR vs a paired consistency objective vs co-training), with SIMPLER success explicitly excluded as evidence.
  - RQ3: the effect of the encoder-pretraining objective on how much real data adaptation needs.
  - RQ4: whether choices transfer across tasks (manipulation → navigation) and to unseen scenes.
- **Main risks and fallbacks:**
  - (a) Scooping of H1 by Mila or the large labs. Fallback: frame H1 as a replication-plus-control study and move the weight onto RQ2/RQ3.
  - (b) H2 fails because full alignment removes useful domain information (per Lei et al.). Fallback: an alignment objective with a domain-discernibility term, or a data-mix study (already the IPB's general fallback).
  - (c) Effects are within seed noise at academic compute. Fallback: fewer variants and more seeds, with effect-size reporting.
  - (d) The proxy metrics (SIMPLER, action matching) do not predict real success. Fallback: report proxy-vs-real correlation as a finding in its own right; WorldSimProbe/RoboWorld show evaluation fidelity is itself a live topic.
  - (e) The venue-point risk from Q1 (RSS, CoRL).

### Gaps
- Not verified whether Nilaksh et al. control for action following, or train policies on imagined data (their abstract mentions "planning and downstream policy performance"). The full paper needs a close read to state the H1 delta precisely.
- No 2026 paper was found that tests a sim/photoreal paired feature-consistency objective for world models specifically. That is absence of evidence from a limited search, not proof of novelty.

## Q4. European and Polish opportunities (NCN, NAWA, EU, ELLIS, IDEAS, summer schools 2027)

### Takeaway
The main funding route is NCN PRELUDIUM (the 25th call closed 16 Jun 2026; PRELUDIUM 26 is expected in spring 2027). NAWA Bekker is open to doctoral candidates, with a deadline of 10 Dec 2026. The nearest ELLIS unit is Warsaw, led by Tomasz Trzciński; there is none in Wrocław. No robot-learning-specific ELLIS school ran in 2026, and 2027 schools are not yet announced.

### Cited Findings
- **NCN PRELUDIUM 25:** announced 16 Mar 2026, applications in OSF until 16 Jun 2026 14:00. Open to researchers without a doctorate (doctoral candidates). Maximum budgets are 70k / 140k / 210k PLN for 12 / 24 / 36-month projects. Results by December 2026. — [NCN PRELUDIUM 25](https://ncn.gov.pl/ogloszenia/konkursy/preludium25); [UW BOB](https://bob.uw.edu.pl/ncn-ogloszono-konkursy-na-opus-31-i-preludium-25/); [PG](https://pg.edu.pl/czp/2026-03/konkurs-preludium-25)
- **NAWA Bekker 2026:** doctoral candidates are eligible for a stay abroad of 3-24 months; deadline 10 Dec 2026, 15:00. — [NAWA news](https://nawa.gov.pl/nawa/aktualnosci/przypominamy-trwa-nabor-wnioskow-do-programu-bekker-nawa); [mojestypendium summary](https://www.mojestypendium.pl/stypendium_zagr/program-bekker-nawa-dla-doktorantow-i-naukowcow-2026/)
- **NAWA PROM:** short-term mobility for doctoral candidates (conferences, data collection), run through institutions. — [NAWA PROM](https://nawa.gov.pl/en/institutions/prom-programme)
- **NAWA Zawacka:** has a 2026/27 outgoing offer. — [NAWA Zawacka](https://nawa.gov.pl/en/international-cooperation-and-exchange/zawacka-nawa/outgoing)
- **ELLIS units:** 44 units in total; the only unit in Poland is ELLIS Unit Warsaw, directed by Tomasz Trzciński; none in Wrocław. — [ELLIS sites](https://ellis.eu/research/sites)
- **ELLIS PhD Program:** 2026 call deadline 31 Oct 2026 23:59 AoE; referees by 25 Nov 2026. — [ELLIS PhD call 2026](https://ellis.eu/news/ellis-phd-program-call-for-applications-2026)
- **ELLIS schools 2026:** none on robot learning or world models. Relevant ones: Munich "ML & Computer Vision" (14-18 Sep 2026, TUM) and Tübingen MLSS (31 Aug-11 Sep 2026). — [ELLIS schools 2026](https://ellis.eu/news/travel-and-study-in-europe-2026-schedule-of-ellis-phd-winter-and-summer-schools)
- **Other summer schools:**
  - IEEE RAS Embodied Intelligence Summer School, UCL East, London, 6-10 Jul 2026. Covers navigation, whole-body control and VLAs, with simulation and real hardware; open to early-stage PhD students. — [UCL](https://www.ucl.ac.uk/engineering/computer-science/study/ieee-ras-embodied-intelligence-summer-school)
  - EEML 2026: Cetinje, Montenegro, 27 Jul-1 Aug 2026; application deadline 31 Mar 2026; travel/fee support available. — [EEML](https://www.eeml.eu/); [IVI announcement](https://ivi.ac.rs/en/news/apply-now-for-eeml-2026/)
- **IDEAS:** IDEAS NCBR now operates as "IDEAS Instytut Badawczy" (ideas.edu.pl). It ran IDEASHACK 2026 with the EU ELIAS project (Demo Day in Warsaw, 19 Jun 2026). Trzciński led the IDEAS NCBR group "Zero-waste machine learning in computer vision" in 2022-2025. — [IDEASHACK 2026](https://www.ideas.edu.pl/wydarzenia/ideashack-2026/)

### Inferences
- **PRELUDIUM 26 (EXPECTED):** announcement ~mid-March 2027, deadline ~mid-June 2027, results by ~Dec 2027, by analogy with PRELUDIUM 25. A 24- or 36-month PRELUDIUM starting in early 2028 would fit years 3-4 of the PhD.
- **Summer schools 2027 (EXPECTED, not announced):** EEML (Jul/Aug 2027, applications ~March), ELLIS schools (schedule usually published early in the year), IEEE RAS Embodied Intelligence school (July), MLSS.
- **Mobility:** NAWA Bekker or PROM could fund a research stay at one of the Q2 labs, e.g. the UT Austin groups or Mila, or at the ELLIS Warsaw unit.

### Gaps
- PRELUDIUM BIS status in 2026-2027 was not checked (the one search mention concerned an older PRELUDIUM BIS 3 edition).
- EU projects not researched: Horizon Europe Cluster 4 robotics calls, MSCA Doctoral Networks, euROBIN, ELIAS/ELSA. I found no source on whether PWr is in any robot-learning EU consortium.
- IDEAS Instytut Badawczy's current robotics or embodied-AI groups were not verified.
- No 2027 summer-school announcement was found as of 29 Sep 2026.

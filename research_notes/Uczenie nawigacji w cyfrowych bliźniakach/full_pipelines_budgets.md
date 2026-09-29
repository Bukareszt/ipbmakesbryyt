# Complete real-to-sim-to-real pipelines and their real-data budgets (navigation first, manipulation as reference)

Compiled 2026-09-26. Every number below was re-read from the primary source (arXiv HTML/abstract, project page or GitHub README) in this session unless marked "(repo note, not re-verified)". Earlier leads in research/crowdedness.md and research/vla-wm-crowdedness.md were checked; two corrections are flagged (RialTo 0/5/10/15 ablation; ReaDy-Go venue).

## Which works count or vary the real-data budget, and what numbers do they report?

### Takeaway
No navigation real-to-sim-to-real paper varies the real-data budget. All of them (EmbodiedSplat, Vid2Sim, VR-Robo, ReaDy-Go, GaussGym, NeRF2Real) use one fixed capture, and all except VR-Robo compare only against zero-shot or other-simulator baselines, with no real-only baseline at a matched budget. Explicit real-data accounting against real-only training appears only in manipulation. There, the claims are single-point ratios, not curves: RialTo (15 demos + 15 min scan vs. BC with 50 demos), X-Sim (1 min of human video vs. 10 min of robot demos, "10x"), R2R2R (1 human video vs. 150 teleop demos) and TwinRL (about 20 min of on-robot RL).

### Comparison table (numbers quoted from the sources)

| Work (venue, ID) | Task / robot / simulator | Real data used | Real success (method) | Baselines incl. real-only | Real trials per eval | Code |
|---|---|---|---|---|---|---|
| **EmbodiedSplat** (Chhablani, Ye, Irshad, Kira; ICCV 2025; arXiv:2509.17430) | ImageNav, indoor; Hello Robot Stretch; Habitat-Sim on GS/Polycam meshes | iPhone 13 Pro Max + Polycam, "1000 aligned RGB-depth frames", "20-30 minutes of recording"; 0 real demos; 0 real training trials; fine-tune "20M additional steps" in the twin | HM3D-pretrained + fine-tuned: 70% | HM3D zero-shot 50%, HSSD zero-shot 10%, HSSD fine-tuned 50%; **no real-data-only baseline** | "10 distinct start-and-goal locations", 1 real scene (lounge); SRCC "0.87–0.97" | Yes: github.com/gchhablani/embodied-splat-v1, HF dataset |
| **Vid2Sim** (Xie, Liu, Peng, Wu, Zhou; CVPR 2025; arXiv:2501.06693) | Urban PointNav/SocialNav; 4-wheeled delivery robot, RGB; Unity + GS | 30 scenes from web videos, each "15-second video at 30 fps, containing 450 frames"; 0 real demos; SAC "1.5M steps" | 85% / 65% / 55% (go straight / static / dynamic obstacle) | Mesh baseline 0% / 0% / 0%; no real-only baseline | "20 trials for each task" | Yes: github.com/Vid2Sim/Vid2Sim |
| **VR-Robo** (Zhu, Mou, Li, Ye, Huang, Zhao; RA-L 2025; arXiv:2502.01536) | RGB goal (cone) reaching with locomotion; Unitree Go2; Isaac Sim + 3DGS | iPad/iPhone photos, 6 rooms (views and capture time not stated); 0 real demos | 100 / 93.33 / 100% (easy / medium / hard) | **IL on "60 different real-world trajectories via teleoperation": 0 / 0 / 0%**; SARO 66.67 / 26.67 / 0; textured mesh 20 / 6.67 / 0; w/o DR 53.33 / 6.67 / 0 | 3 cone sets × 5 = 15 per level | Project page VR-Robo.github.io; code release not stated in the paper |
| **ReaDy-Go** (Yoo, Kim, Han, Jung, Jang, H. J. Kim; arXiv:2602.11575) | PointGoal with moving humans; differential-drive robot, ZED2; custom dynamic 3DGS sim | "monocular video recorded for about six minutes", "1,000–1,500 images" per environment, 3 environments; 0 real demos | Static / dynamic: Outside 100/90, Lobby 90/70, Library 100/80 % | Vid2Sim 90/60, 70/40, 90/60; ViNT 50/30, 60/20, 80/40; no real-only baseline | "10 episodes" | Project page only |
| **GaussGym** (Escontrela, Kerr, Allshire, Frey, Duan, Sferrazza, Abbeel; arXiv:2510.15352) | Visual locomotion/navigation/stairs; Unitree A1, Booster T1; IsaacGym + 3DGS | iPhone scans + ARKitScenes, GrandTour, Veo; "2,500 scenes"; capture per scene not stated | Stair-climbing transfers "without additional fine-tuning"; no SR numbers | Depth-only, ablations; no real-only baseline | Not stated | "All code and data will be open-sourced" |
| **NeRF2Real** (Byravan et al., DeepMind; arXiv:2210.04932, Oct 2022, outside the 2023–2026 window) | Navigation + ball pushing; 20-DoF humanoid | "a short video of a static scene collected using a generic phone" (duration not in abstract) | Qualitative transfer | — | — | — |
| **RialTo** (Torne, Simeonov, Li, Chan, Chen, Gupta, Agrawal; RSS 2024; arXiv:2403.03949) | Manipulation (book on shelf, etc.); Franka; Isaac Sim | Scan: "under 15 minutes of active interaction time" (user study: 25 min 12 s total, 14 min 40 s active); ~15 real demos (~30 min) | Avg. 91% (pose randomization), 77% (distractors), 75% (disturbances); book on shelf 90±9% | BC 15 demos: 10±9% (book, randomization only); BC 50 demos (1 h 45 min): 40±15%; "less than one third the number of demonstrations" | "at least 10 rollouts" | Yes (project site) |
| **CASHER** (Torne, Jain, Yuan, Macha, Ankile, Simeonov, Agrawal, Gupta; arXiv:2412.01770; no venue found) | Sink/shelf/cabinet; Franka FR3; Isaac Sim | 56 (sink) / 36 (cabinet) crowd-sourced scenes; scan "3 min 15 sec" per scene, objects "4 min 50 sec"; 10 demos per environment (in sim) | 62% zero-shot (56 envs); 16% → 60% from 9 → 56 envs; few-shot fine-tuning +54% | IL 10±5%; OpenVLA / Octo zero-shot 0% | 108 rollouts per policy | Project page |
| **X-Sim** (Dan, Kedia, Chao, Duan, Pace, Ma, Choudhury; CoRL 2025 oral; arXiv:2505.07096) | 5 manipulation tasks; Franka; ManiSkill + 2DGS | Env scan "<2 minutes", objects "<1 minute per object"; RGB-D human videos; no robot demos | "90% success with just 1 minute of human video data" (Mustard Place) | BC: "70% success with 10 minutes of robot demonstrations" (20 s per video vs. 60 s per robot demo) | "10 trials" | Yes (project page) |
| **Real2Render2Real** (Yu, Fu, Huang, El-Refai, Ambrus, Cheng, Irshad, Goldberg; CoRL 2025; arXiv:2505.09601) | 5 tasks; ABB YuMi (+ Franka); no dynamics sim (rendering) | 1 phone object scan + "a single video of a human demonstration" per task | 66.6–86.6% with 1,000 R2R2R demos | 150 teleop demos (60–104 min/task): mug π0-FAST 73.3%, Diffusion 40.0%; R2R2R generation 13.97–38.22 min/task | "15 trials per task" | Yes: github.com/uynitsuj/real2render2real |
| **TwinRL** (Q. Xu, J. Liu, R. Zhou, S. Shi, … S. Zhang; arXiv:2602.09023; ACM MM 2026 per README only) | 4 manipulation tasks; Franka FR3; 3DGS twin + MuJoCo/Blender | Phone video "approximately one minute"; "30 demonstrations" (+ synthetic); "only about 20 minutes of on-robot interaction across four tasks" | "near-100%" ID and OOD; avg. 95% (SD 6.71) | HiL-SERL, ConRFT (real-world RL): TwinRL "over 30% faster convergence" | 5 rounds × 10 rollouts | Partial: github.com/zhourui9813/TwinRL (MIT; offline training + twin assets; real-world RL code "coming soon"; Octo/HIL-SERL-based) |
| **Real-is-Sim** (Abou-Chakra et al., RAI Institute + QUT; arXiv:2504.03597) | PushT; Franka; Embodied Gaussians twin at 60 Hz | 30 real demos; objects from "4 viewpoints" | 30 real + 30 sim demos: 80%; virtual gripper camera 82% | Real 30 demos only: "around 57%" | 60 (20 poses × 3) | Project page; code release not stated |

### Cited Findings
- EmbodiedSplat's capture, SR and baselines are as in the table. Its paper reports no real-data-only baseline, and its real test is 1 scene with 10 episodes — [arXiv:2509.17430](https://arxiv.org/html/2509.17430); code at [GitHub](https://github.com/gchhablani/embodied-splat-v1); ICCV 2025 in [CVF open access](https://openaccess.thecvf.com/content/ICCV2025/papers/Chhablani_EmbodiedSplat_Personalized_Real-to-Sim-to-Real_Navigation_with_Gaussian_Splats_from_a_Mobile_ICCV_2025_paper.pdf)
- Vid2Sim uses 15 s web videos (450 frames) per scene over 30 scenes, with 85/65/55% real SR vs. 0% for the mesh baseline over 20 trials each — [arXiv:2501.06693](https://arxiv.org/html/2501.06693); CVPR 2025 [poster](https://cvpr.thecvf.com/virtual/2025/poster/32747); code [GitHub](https://github.com/Vid2Sim/Vid2Sim)
- VR-Robo is the only navigation work with a real-demonstration baseline: IL on 60 teleoperated trajectories gets 0% at every difficulty, against 93–100% for VR-Robo — [arXiv:2502.01536](https://arxiv.org/html/2502.01536)
- ReaDy-Go uses about 6 min of monocular video (1,000–1,500 images) per environment and beats Vid2Sim and ViNT in all 3 environments over 10 episodes — [arXiv:2602.11575](https://arxiv.org/html/2602.11575). Venue conflict: the arXiv HTML says IEEE T-RO (accepted 9 June 2026), while research/crowdedness.md lists RA-L 2026 (doi:10.1109/LRA.2026.3707355). Resolve this before citing.
- GaussGym gives no real SR numbers and no per-scene capture budget — [arXiv:2510.15352](https://arxiv.org/html/2510.15352)
- RialTo: 15 min of active scanning plus 15 demos (30 min) reaches 90±9%, against 40±15% for BC with 50 demos (1 h 45 min) — [arXiv:2403.03949v3](https://arxiv.org/html/2403.03949v3). **Correction:** research/crowdedness.md says RialTo "ablates 0–15 real demos" (0/5/10/15, appendix). Two fetches of the v3 full text found no such systematic ablation. Treat that claim as unverified; the PDF was too large to fetch.
- X-Sim's "10x" is one point on one task: 1 min of human video → 90%, against 10 min of robot demos → 70% for BC — [arXiv:2505.07096](https://arxiv.org/html/2505.07096); CoRL 2025 oral per [ML Anthology](https://mlanthology.org/corl/2025/dan2025corl-xsim/)
- R2R2R: 1 human demo matches 150 teleop demos (mug task: 73.3% for π0-FAST on 150 teleop demos) — [arXiv:2505.09601](https://arxiv.org/html/2505.09601); CoRL 2025 per [GitHub](https://github.com/uynitsuj/real2render2real)
- CASHER shows zero-shot SR rising from 16% to 60% as the number of reconstructed environments grows from 9 to 56. Scanning takes about 3 min per scene — [arXiv:2412.01770](https://arxiv.org/html/2412.01770). No peer-reviewed venue was found ([project page](https://casher-robot-learning.github.io/CASHER/)).
- TwinRL: 1 min phone video, 30 real demos, about 20 min on-robot RL, 95% average SR, and over 30% faster convergence than HiL-SERL/ConRFT — [arXiv:2602.09023](https://arxiv.org/html/2602.09023). The ACM MM 2026 acceptance and the partial code release come from the [README](https://github.com/zhourui9813/TwinRL).
- Real-is-Sim: 30 real demos alone give about 57%; adding 30 twin demos gives 80% — [arXiv:2504.03597](https://arxiv.org/html/2504.03597)
- NeRF2Real (2022) uses "a short video … using a generic phone" for humanoid navigation — [arXiv:2210.04932](https://arxiv.org/abs/2210.04932)

### Inferences
- In navigation, the "real data" of every existing pipeline is **only the capture** (6–30 min of video, or a 15 s web clip), with zero real training trials. A "≥2× less real data" claim against these baselines therefore reduces to a capture-minutes claim. That is measurable, but it is really an H1-type claim unless the method also uses real trials (stage 3) and the baseline is given the same opportunity.
- Across all rows, real evaluations use 10–20 trials (15 for VR-Robo, 108 for CASHER). A 10-trial SR has a 95% Wilson half-width of about ±25–30 pp near 50%, so a single-point "2×" claim is statistically weak. It needs budget-vs-SR curves with many seeds or trials, or the proxy-reality tier.

### Gaps
- VR-Robo capture views and time, GaussGym per-scene capture time, and NeRF2Real video duration are not reported in the texts read.
- The RialTo appendix could not be read in full (the PDF exceeds the fetch limit), so the 0/5/10/15 ablation remains unconfirmed.
- Venues for CASHER, Real-is-Sim and GaussGym (as of 2026-09) were not found.

## Are there data-scaling or "exchange rate" results comparing sim/twin data with real data?

### Takeaway
Yes, but only for manipulation, and none as a proper exchange-rate curve (real-data-equivalent vs. twin budget). The evidence is sim/real co-training gains (+30–38% SR), plateau effects (sim data saturates, and real data raises the ceiling), real-only power laws in the number of environments, and single-point ratios (10×, 150×, 1/3 of the demos). For navigation, the only data-scaling study found is real-only.

### Cited Findings
- Lin et al., "Data Scaling Laws in Imitation Learning for Robotic Manipulation" (arXiv:2410.18647; ICLR 2025 per repo note): "over 40,000 demonstrations and … more than 15,000 real-world robot rollouts". Generalization "follows a roughly power-law relationship with the number of environments and objects". "With four data collectors working for one afternoon … approximately 90% success rates in novel environments with unseen objects" — [arXiv:2410.18647](https://arxiv.org/abs/2410.18647)
- Maddukuri et al., "Sim-and-Real Co-Training: A Simple Recipe" (arXiv:2503.24361; RSS 2025 per repo note): 50 real demos per task (Panda) and 20 (humanoid), 40–400 real demos in the generalization study, and 10k synthetic trajectories per task. Co-training gives "37.9% over the real-only policies"; the best co-training ratio is 99% sim. Co-trained policies outperform real-only ones even at 400 real demos — [arXiv:2503.24361](https://arxiv.org/html/2503.24361)
- Wei, Agarwal, Chen, Bosworth, Pfaff, Tedrake (IROS 2025, arXiv:2503.22634): "performance gains scale with additional simulated data up to a plateau"; "adding more real-world data increases this performance ceiling". Based on 50+ real policies and 1000+ real trials — [arXiv:2503.22634](https://arxiv.org/abs/2503.22634)
- Cheng, Ma, Chen, Mandlekar, Garrett, Xu (NeurIPS 2025, arXiv:2509.18631): OT-based observation–action alignment gives "up to a 30% improvement in the real-world success rate" with "a few real-world demonstrations" — [arXiv:2509.18631](https://arxiv.org/abs/2509.18631)
- RLinf-Co (Shi et al., arXiv:2602.12628): RL-based sim–real co-training for VLAs gives "+24% real-world success on OpenVLA and +20% on π₀.₅" — [arXiv:2602.12628](https://arxiv.org/abs/2602.12628)
- Single-point exchange ratios: X-Sim 1 min video ≈ better than 10 min robot demos; R2R2R 1 demo ≈ 150 teleop demos; RialTo 15 demos + scan beats 50 demos — see the table sources above.
- Navigation real-only scaling: Suomela et al. (RA-L 2026, arXiv:2601.09444) report that more data from an existing location "saturates with very little data" (repo note in research/crowdedness.md, not re-fetched).

### Inferences
- The "exchange rate" framing (how many real units a twin budget replaces) has not been published as a curve for any domain. Navigation has neither the twin-side nor the matched real-side curve. Both H4(a) (vs. real-only) and H4(b) (vs. the best r2s2r) are unclaimed as *curves*, while the single-point ratios reported in manipulation (10×, 150×) set the committee's expectations.
- Because of the plateau results (Wei et al.), a navigation budget curve will likely saturate. The 2× claim should be stated at a specified target SR below the plateau.

### Gaps
- No sim/twin-vs-real exchange-rate study for navigation was found. The search was limited (about 4 navigation-specific queries), so a 2026 preprint may exist.

## Which approach is the strongest fair baseline for navigation, and is its code available?

### Takeaway
**EmbodiedSplat is the strongest fair baseline for indoor navigation.** It is the only pipeline that matches the IPB setting: indoor rooms, phone capture, Habitat, a pretrained navigation policy fine-tuned in the twin, and published SRCC. Its code and data are public. ReaDy-Go reports the highest real SR and beats Vid2Sim head-to-head, but it is outdoor/lobby PointGoal with humans, and no code release was found. Vid2Sim has code but targets urban outdoor scenes. For H4 with real trials, the baseline should be "EmbodiedSplat + RialTo/TwinRL-style real correction" (random or failure-driven real trials), re-implemented in the same stack.

### Cited Findings
- EmbodiedSplat: fixed 20–30 min iPhone capture, fine-tuning in Habitat, 70% real SR, public code and HF dataset — [arXiv](https://arxiv.org/html/2509.17430); [GitHub](https://github.com/gchhablani/embodied-splat-v1)
- ReaDy-Go > Vid2Sim > ViNT in 6/6 real settings — [arXiv:2602.11575](https://arxiv.org/html/2602.11575)
- Vid2Sim code is public — [GitHub](https://github.com/Vid2Sim/Vid2Sim)
- TwinRL (manipulation) is the closest pipeline that uses real trials. Its real-world RL code is not yet released — [README](https://github.com/zhourui9813/TwinRL)

### Inferences
- No navigation pipeline has a real-trial correction stage. A "strongest existing real-to-sim-to-real" baseline with stage 3 therefore does not exist for navigation and must be composed: EmbodiedSplat capture and fine-tuning + a RialTo/TwinRL-style real-data step. The committee may call this a strawman, so pre-register the baseline recipe and give it the same real budget.
- An alternative honest framing for H4(b) is "≥2× less real data than EmbodiedSplat-style uniform capture + twin fine-tuning, both evaluated as budget curves". This is measurable because EmbodiedSplat's code allows re-running it at 5/10/20/30 min of capture.

### Gaps
- It was not verified whether the EmbodiedSplat repo includes the Polycam→mesh conversion and fine-tuning scripts end-to-end (the README was not fetched).
- The VR-Robo and ReaDy-Go code status is not confirmed.

## What would a fair comparison at equal operator effort look like?

### Takeaway
Count all real-world operator effort in one unit (operator minutes, recorded separately as capture, demonstrations, on-robot trials and resets). Give every method, including real-only, the same budget grid. Report SR-vs-budget curves with confidence intervals on the same held-out real episodes. This follows RialTo and R2R2R, which already report time (scan 15 min, 15 demos 30 min, 50 demos 1 h 45; 150 teleop demos 60–104 min).

### Cited Findings
- RialTo reports active scan time (14 min 40 s), demo time (30 min for 15) and baseline demo time (1 h 45 min for 50) — [arXiv:2403.03949v3](https://arxiv.org/html/2403.03949v3)
- R2R2R reports teleop time (60–104 min per 150 demos) against generation time — [arXiv:2505.09601](https://arxiv.org/html/2505.09601)
- X-Sim normalizes by collection time (20 s per video vs. 60 s per robot demo) — [arXiv:2505.07096](https://arxiv.org/html/2505.07096)
- TwinRL reports on-robot minutes (about 20 min) — [arXiv:2602.09023](https://arxiv.org/html/2602.09023)

### Inferences (proposed protocol)
- Budget unit: operator minutes, B = capture + demos/teleop + on-robot trials (including resets), with each component logged. Also report the raw counts (frames/views, demos, trials).
- Methods on the same budget grid (e.g. B ∈ {5, 10, 20, 40, 80} min): (i) real-only (IL on teleop trajectories, as in VR-Robo's 60-trajectory IL; or real fine-tuning of the same pretrained policy); (ii) zero-shot pretrained; (iii) EmbodiedSplat-style uniform capture + twin fine-tuning, spending all of B on capture; (iv) (iii) + random real trials (RialTo/TwinRL-style), with the split tuned for the baseline; (v) the proposed method.
- The same pretrained initialization, twin-training compute cap and evaluation episodes (fixed start–goal sets) apply to all methods. Use ≥30–50 real episodes per point, or rely on the proxy-reality tier to decide the hypothesis, with real-robot runs as validation only.
- Report budget-to-target B*(SR_target) for each method, with bootstrap CIs on the ratio B*_baseline / B*_method. H4 holds if the lower CI bound is ≥ 2.

### Gaps
- No published navigation study uses operator minutes across all stages, so there is no established convention to cite. The protocol above is a synthesis.

## Crowdedness: how many groups, and at which venues?

### Takeaway
Full real-to-sim-to-real navigation pipelines come from at least 6 groups (Georgia Tech/TRI, UCLA, Tsinghua IIIS, SNU/KAIST, UC Berkeley/ETH, DeepMind earlier), plus at least 4 drone groups (repo note). Most appear at robotics venues (RA-L, T-RO, CoRL, RSS, IROS). The ML/CV-venue items are EmbodiedSplat (ICCV 2025), Vid2Sim (CVPR 2025), Cheng et al. co-training (NeurIPS 2025) and Lin et al. scaling laws (ICLR 2025). Budget-counting claims are concentrated in manipulation (MIT Agrawal/Gupta, Cornell, Berkeley/TRI, Tsinghua/PKU).

### Cited Findings
- CV venues: EmbodiedSplat at ICCV 2025 ([CVF](https://openaccess.thecvf.com/content/ICCV2025/papers/Chhablani_EmbodiedSplat_Personalized_Real-to-Sim-to-Real_Navigation_with_Gaussian_Splats_from_a_Mobile_ICCV_2025_paper.pdf)); Vid2Sim at CVPR 2025 ([CVPR](https://cvpr.thecvf.com/virtual/2025/poster/32747))
- ML venues: Cheng et al. at NeurIPS 2025 ([arXiv](https://arxiv.org/abs/2509.18631)); Lin et al. at ICLR 2025 (repo note)
- Robotics venues: VR-Robo in RA-L ([arXiv](https://arxiv.org/html/2502.01536)); ReaDy-Go in T-RO per arXiv ([arXiv](https://arxiv.org/html/2602.11575)); X-Sim at CoRL 2025 oral ([ML Anthology](https://mlanthology.org/corl/2025/dan2025corl-xsim/)); R2R2R at CoRL 2025 ([GitHub](https://github.com/uynitsuj/real2render2real)); RialTo at RSS 2024 ([project](https://real-to-sim-to-real.github.io/RialTo/)); Wei et al. at IROS 2025 ([arXiv](https://arxiv.org/abs/2503.22634)); TwinRL at ACM MM 2026 per [README](https://github.com/zhourui9813/TwinRL)
- More GS-simulator navigation groups (Stanford Schwager: SOUS VIDE/GRaD-Nav/SINGER; UIUC FalconGym; MIT Liquid-GS; PKU NavGSim; QuadVerse 2026) are listed in research/crowdedness.md (not re-verified here).

### Inferences
- **Novelty of H4:** the navigation pipeline itself is crowded. However, "reaching a target real SR with ≥2× less real data than the strongest r2s2r approach, measured as budget curves" has not been claimed by anyone for navigation. The closest items (X-Sim 10×, R2R2R 150×, RialTo) are manipulation single points, compared against real-only rather than against another r2s2r pipeline. **Novel: yes, as a measured claim.**
- **Realism:** the navigation baselines spend 6–30 min of capture and no real trials. If EmbodiedSplat's SR saturates at about 10 min of capture, halving capture may be easy but trivial. The claim is only meaningful at a target SR the baseline reaches, on a budget curve that includes real trials. Plausible but uncertain. The risk is that the baseline's curve is flat, which makes the "2×" ill-defined. Mitigate by defining the target as a fraction of the baseline's plateau.
- **Measurability:** feasible if the baseline is re-run at multiple budgets (EmbodiedSplat code exists) and the decision is made in the proxy-reality tier. With 10-episode real evaluations, as in the literature, it is not measurable.
- **Scooping risk:** the EmbodiedSplat (Kira lab/TRI), ReaDy-Go and TwinRL groups are each one step from a budget-curve paper. The TRI connection spans EmbodiedSplat and R2R2R, and the Gupta/Agrawal lineage spans RialTo and CASHER.

### Gaps
- Group counts come from the papers read here plus repo notes; no systematic bibliometric count was redone in this session.

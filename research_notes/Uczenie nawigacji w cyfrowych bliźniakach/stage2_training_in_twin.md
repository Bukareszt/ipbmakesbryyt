# Stage 2: training navigation models in digital twins (with world models and foundation VLM/VLA models), 2023–2026

Scope: indoor (plus closely related urban and legged) mobile-robot navigation. As of 26 Sep 2026. Each paper was checked against its arXiv abstract or HTML page during this session unless marked "(repo lead, not re-fetched)". Numbers are the authors' own. Most real-world evaluations use only 10–15 trials per condition, so a single trial is worth 6.7–10 pp.

## Q1. Training navigation in 3DGS/NeRF twins: algorithms, observations, real success, sim-to-real gap

### Takeaway
Since 2024, at least six groups have trained navigation policies in Gaussian-splat twins. They use PPO/DD-PPO, SAC, or imitation from planner experts, almost always with RGB-only inputs. They report large real-world gains over generic-simulator or mesh baselines, typically +20 to +90 pp. Every one of these comparisons is twin vs. a poorer simulator. None compares twin-training recipes at a matched real-data budget, and real evaluations are small (10–15 trials per cell).

### Cited Findings
- **Vid2Sim** (Z. Xie, Z. Liu, Z. Peng, W. Wu, B. Zhou; CVPR 2025; arXiv:2501.06693). Monocular video → photorealistic, physically interactive 3DGS simulation for urban navigation. The abstract claims +31.2% success in the digital twin and +68.3% in the real world vs. agents trained with prior simulation methods. — [arXiv abs](https://arxiv.org/abs/2501.06693)
  - Setup: SAC, 30 Vid2Sim environments, 30 parallel envs, 1.5M steps, "around 15 hours on a single NVIDIA A5000". Observations are RGB stacked with the past 5 timesteps, plus goal distance and heading. — [arXiv HTML](https://arxiv.org/html/2501.06693)
  - Augmentation: scene editing, weather (rain/fog/snow), lighting/seasonal changes, random obstacles. Adding obstacles raised sim PointNav SR from 68.8% to 80.8% (static) and 81.6% (dynamic). — [arXiv HTML](https://arxiv.org/html/2501.06693)
  - Zero-shot real results with 30 training envs: 85% Go Straight, 65% Static Obstacle, 55% Dynamic Obstacle. — [arXiv HTML](https://arxiv.org/html/2501.06693)
- **VR-Robo** (S. Zhu, L. Mou, D. Li, B. Ye, R. Huang, H. Zhao; RA-L 2025; arXiv:2502.01536). 3DGS twin plus mesh physics in Isaac Sim for legged visual navigation (reaching a colored cone). — [arXiv abs](https://arxiv.org/abs/2502.01536), [GitHub](https://github.com/zst1406217/VR-Robo)
  - Setup: hierarchical PPO. The high-level policy runs at 5 Hz on frozen-ViT RGB features plus proprioception. Single RTX 4090D; low-level 4,096 agents × 80k iterations (~3 days). — [arXiv HTML](https://arxiv.org/html/2502.01536)
  - Real SR (Easy/Medium/Hard):
    - VR-Robo: 100 / 93.33 / 100%
    - SARO: 66.67 / 26.67 / 0%
    - Textured mesh: 20 / 6.67 / 0%
    - **Without domain randomization: 53.33 / 6.67 / 0%**
  - The DR used is camera-pose noise, color/brightness/blur/noise augmentation, and 0–1 step image delay. — [arXiv HTML](https://arxiv.org/html/2502.01536)
- **EmbodiedSplat** (G. Chhablani, X. Ye, M. Z. Irshad, Z. Kira; ICCV 2025; arXiv:2509.17430). An iPhone capture becomes a 3DGS/mesh twin in Habitat-Sim, used to fine-tune ImageNav policies. The abstract reports "absolute success rate improvements of 20% and 40%" in the real world over HM3D- and HSSD-pretrained baselines, and a sim-vs-real correlation of 0.87–0.97. — [arXiv abs](https://arxiv.org/abs/2509.17430)
  - Setup: DD-PPO on RGB (640×480), 16× A40. Pretraining took 600M steps (HM3D) or 1,200M steps (HSSD); fine-tuning in the twin took only 20M steps. Capture was 20–30 min with Polycam, plus 1–2 h of DN-Splatter meshing. — [arXiv HTML](https://arxiv.org/html/2509.17430v1)
  - Real Lounge results: zero-shot 50% (HM3D) / 10% (HSSD). Fine-tuned: 70% / 40–50%. Each condition used only 10 start–goal pairs. — [arXiv HTML](https://arxiv.org/html/2509.17430v1)
- **ReaDy-Go** (S. Yoo, Y. Jang, D. Kim, Y. Han, S. Jung, H. J. Kim; RA-L; arXiv:2602.11575). A static 3DGS twin plus dynamic human-GS obstacles; policy trained by **imitation learning** (MSE to expert actions) on RGB (3 stacked frames). — [arXiv abs](https://arxiv.org/abs/2602.11575)
  - Data: each of 3 environments was reconstructed from ~6 min of monocular video (1,000–1,500 images), with 400 training episodes per environment. — [arXiv HTML](https://arxiv.org/html/2602.11575)
  - Real SR, ReaDy-Go / Vid2Sim / ViNT:
    - Outside static: 100 / 90 / 50
    - Outside dynamic: 90 / 60 / 30
    - Lobby static: 90 / 70 / 60
    - Lobby dynamic: 70 / 40 / 20
    - Library static: 100 / 90 / 80
    - Library dynamic: 80 / 60 / 40
  - Compute not reported. — [arXiv HTML](https://arxiv.org/html/2602.11575)
- **GaussGym** (A. Escontrela, J. Kerr, A. Allshire, J. Frey, R. Duan, C. Sferrazza, P. Abbeel; arXiv:2510.15352, Oct 2025). 3DGS inside vectorized IsaacGym, "exceeding 100,000 steps per second on consumer GPUs". Scenes come from iPhone scans, GrandTour, ARKit and Veo-generated video. Tasks are locomotion from pixels and visual-semantic navigation. — [arXiv abs](https://arxiv.org/abs/2510.15352)
- **NavGSim** (J. Liu, Y. Duan, J. Zhang, M. Li, S. Wang, Z. Zhang, H. Wang; arXiv:2603.15186, Mar 2026). A large-scale GS simulator (hundreds of m²) with collision detection and multi-GPU APIs. It is used to generate trajectories that train a navigation **VLA**, which the abstract says "significantly enhances the VLA model's scene understanding". The abstract gives no numbers. — [arXiv abs](https://arxiv.org/abs/2603.15186)
- **SplatGym** / "Robotic Learning in your Backyard" (arXiv:2410.19564). An open-source neural simulator that builds a photorealistic environment from a single video and trains free-space visual navigation policies with RL. It supports ego-camera rendering, collision detection and object in-painting (nerfstudio-based). — [arXiv abs](https://arxiv.org/abs/2410.19564), [GitHub](https://github.com/splatlearn/splatgym)
- Other twin-navigation leads (repo lead, not re-fetched): GaussFly arXiv:2604.05062 (drone), GASE arXiv:2606.17520, GS-Playground arXiv:2604.25459 (RSS 2026) — see research/crowdedness.md.

### Inferences
- Algorithms split three ways:
  - Model-free RL: PPO/DD-PPO for Habitat-style ImageNav/PointNav (EmbodiedSplat, VR-Robo); SAC for urban PointNav (Vid2Sim).
  - Imitation from privileged planners inside the twin (ReaDy-Go).
  - VLA supervised fine-tuning on twin-generated trajectories (NavGSim).
- Observations are almost always RGB, sometimes plus goal vector or proprioception. Depth is often avoided because GS depth is noisy.
- The gap between sim and real success is small in the best cases (VR-Robo: 100% sim / 93–100% real). EmbodiedSplat's 0.87–0.97 correlation is the only formal sim-to-real predictivity number found.
- The baselines are "generic sim" or "mesh twin". Nobody reports curves over capture budget or over DR design at a fixed budget, so H2's comparison (uncertainty-guided vs. uniform DR, both inside a twin) is not directly covered by existing work.
- EmbodiedSplat's pretrain vs. fine-tune numbers (600–1,200M vs. 20M steps) show that twin fine-tuning is cheap once a pretrained policy exists.

### Gaps
- No paper found that reports real SR as a function of capture minutes for navigation.
- NavGSim's real-world numbers were not in the abstract; the full paper was not fetched.
- SplatGym has no quantitative real-world results in what was checked.
- The CVPR 2025 venue of Vid2Sim and the RA-L DOIs for VR-Robo and ReaDy-Go come from arXiv comments, GitHub and IEEE listings, not from a Crossref check in this session. The Vid2Sim DOI 10.1109/CVPR52734.2025.00155 is from the repo notes.

## Q2. Uniform domain randomization vs. uncertainty-aware or targeted randomization in twins: evidence and size of gains

### Takeaway
Adding DR to a twin clearly matters: VR-Robo's ablation without DR loses 47–100 pp in the real world. But no navigation paper found compares **uncertainty- or failure-targeted** randomization against **uniform** DR inside a reconstructed twin. The closest targeted work is in manipulation (TwinRL, Phys2Real) and generic ADR. So H2 is novel in navigation, but its effect-size prior is weakly grounded.

### Cited Findings
- VR-Robo real ablation: full method 100 / 93.33 / 100% vs. "w/o Domain Randomization" 53.33 / 6.67 / 0% (Easy/Medium/Hard). DR here is standard, uniform image and camera randomization. — [arXiv HTML](https://arxiv.org/html/2502.01536)
- Vid2Sim uses broad, uniform-style augmentation (weather, lighting, obstacles). Its only ablation covers obstacles (sim SR 68.8 → 81.6%), not uniform vs. targeted DR. — [arXiv HTML](https://arxiv.org/html/2501.06693)
- ReaDy-Go isolates only the effect of photorealistic dynamic-human obstacles vs. Vid2Sim-style obstacles, with the same policy and planner: +10 to +30 pp real SR in dynamic scenes. It has no DR ablation. — [arXiv HTML](https://arxiv.org/html/2602.11575)
- NavRL++ (Z. Xu, H. Jin, K. Shimada; arXiv:2605.15559, May 2026) proposes "perturbation-aware fine-tuning … explicitly accounting for empirically identified domain discrepancies", a targeted form of randomization, for RL navigation. It achieves zero-shot transfer on aerial and legged robots. The abstract gives no pp gain over uniform DR. — [arXiv abs](https://arxiv.org/abs/2605.15559)
- Phys2Real (arXiv:2510.11689) handles uncertainty over physical parameters by fusing VLM priors with online adaptation. It is a manipulation paper, not navigation. — [arXiv PDF](https://arxiv.org/pdf/2510.11689)
- TwinRL (arXiv:2602.09023, manipulation; repo lead, abstract checked in earlier waves) "identifies failure-prone yet informative configurations, enabling targeted human-in-the-loop rollouts". This is the closest precedent for failure- or uncertainty-targeted training in a twin. — [arXiv abs](https://arxiv.org/abs/2602.09023)
- A 3DGS-specific DR method, "Meshless Domain Randomization via Explicit Parameter Perturbation of 3DGS" (arXiv:2607.22890), targets insect classification. It reports only feature-space silhouette changes (0.14–0.15 → 0.18–0.22), not task success. — [arXiv HTML](https://arxiv.org/html/2607.22890)
- A search snippet claimed that curriculum learning improves navigation SR by "~10% during fine-tuning" and ">15%" in dynamic scenes. The primary source could not be identified, so this is **not used**. — (unverified aggregator result)

### Inferences
- "DR vs. no DR" effects are huge (tens of pp). "Targeted vs. uniform DR" effects in other areas are usually much smaller. In navigation they have not been measured in twins, which is the open niche for H2.
- Uncertainty signals that could drive targeting already exist in the reconstruction literature: FisherRF arXiv:2311.17874 and Bayes' Rays arXiv:2309.03185 (repo leads). Nobody has yet used them to set training-time randomization for navigation policies.

### Gaps
- No quantitative navigation result for adaptive, uncertainty-guided, or active DR vs. uniform DR in a 3DGS twin was found.
- Classic Active DR (Mehta et al., 2019) and ADR (OpenAI, 2019) predate the 2023–2026 window. They were not re-verified here.

## Q3. World models for navigation as data engines or learned simulators; compute

### Takeaway
Navigation world models are mostly used for **planning or ranking** at inference (NWM, NavWM, PiJEPA), not as training simulators for navigation policies. Using a world model as an RL environment is established for manipulation VLAs (World-Env, VLA-RFT, WMPO, World-Gymnast, Interactive World Simulator). World-in-World (ICLR 2026) finds that controllability and action-conditioned post-training matter more than visual quality. No paper was found that fuses a 3DGS navigation twin with a learned world model for policy training. That combination is plausible and new, but unproven.

### Cited Findings
- **NWM, Navigation World Models** (A. Bar, G. Zhou, D. Tran, T. Darrell, Y. LeCun; CVPR 2025; arXiv:2412.03572). A Conditional Diffusion Transformer scaled to 1B parameters, trained on egocentric videos of humans and robots. It plans either by simulating trajectories or by **ranking trajectories sampled from external policies** (e.g., NoMaD). It can imagine trajectories in unfamiliar environments from a single image. — [arXiv abs](https://arxiv.org/abs/2412.03572)
- **NavWM** (Y. Mei, L. Guo, M.-M. Yu, G. Zhao, X. He, J. Liu; ECCV 2026 accepted; arXiv:2606.24101). A unified navigation world model with latent world tokens, anchor-based multimodal trajectory forecasting and controllable generation, used as a closed-loop foresight planner. The abstract claims SOTA generation and zero-shot navigation success but gives no numbers. — [arXiv abs](https://arxiv.org/abs/2606.24101)
- **World-in-World** (J. Zhang et al.; ICLR 2026 oral; arXiv:2510.18135). A closed-loop benchmark of world models for embodied tasks with three findings:
  - "visual quality alone does not guarantee task success, controllability matters more";
  - post-training with action–observation data beats upgrading the base video model;
  - more inference-time compute improves closed-loop performance.
  - It also reports the first data-scaling laws for world models in embodied use. — [arXiv abs](https://arxiv.org/abs/2510.18135)
- **PiJEPA** (A. Chahe, L. Zhou; arXiv:2603.25981, Mar 2026). A policy distribution warm-starts MPPI over a JEPA latent world model for language-conditioned visual navigation. It "significantly outperforms" both the policy alone and uninformed world-model planning in the real world (no numbers in the abstract). — [arXiv abs](https://arxiv.org/abs/2603.25981)
- World models as RL environments for (manipulation) VLAs: World-Env arXiv:2509.24948, VLA-RFT arXiv:2510.00406, WMPO arXiv:2511.09515 (repo leads), World-Gymnast arXiv:2602.02454, and Interactive World Simulator arXiv:2603.08546 (RSS 2026). — [World-Gymnast](https://arxiv.org/pdf/2602.02454), [Interactive World Simulator](https://arxiv.org/html/2603.08546v1)
- A survey notes that world models "can be exploited" by policies during PPO training because of model inaccuracies. As of early 2026, downstream real-robot gains are "less established than marketing implies". — [World Model for Robot Learning survey, arXiv:2605.00080](https://arxiv.org/html/2605.00080v1)
- Cosmos (NVIDIA, arXiv:2501.03575), Genie (ICML 2024, arXiv:2402.15391), DreamerV3 (Nature 2025, doi:10.1038/s41586-025-08744-2) and GWM (ICCV 2025, arXiv:2508.17600) are repo leads, not re-fetched this session. Cosmos-Transfer1 (arXiv:2503.14492) does sim→real appearance transfer and is a candidate "twin-render → realistic" augmenter. — see research/world-models.md
- Compute:
  - Twin simulators are cheap: Vid2Sim needed 15 h on one A5000 and VR-Robo ~3 days on one 4090D. GaussGym runs at >100k steps/s on consumer GPUs. — [Vid2Sim HTML](https://arxiv.org/html/2501.06693), [VR-Robo HTML](https://arxiv.org/html/2502.01536), [GaussGym](https://arxiv.org/abs/2510.15352)
  - Diffusion world models of NWM class are 1B parameters (training compute not in the abstract). — [NWM](https://arxiv.org/abs/2412.03572)

### Inferences
- The practical way to use a world model inside a twin under a PhD-scale budget is one of three roles:
  - a fine-tuned NWM-class model used to rank or filter actions, or to extend the twin to viewpoints and dynamics it does not cover;
  - a latent world model (Dreamer/JEPA-style) trained on twin rollouts;
  - a Cosmos-Transfer-style appearance augmenter.
- Full video-diffusion RL rollouts are orders of magnitude slower than 3DGS rendering: >100k steps/s for GaussGym vs. diffusion sampling. This is an inference from architecture, not a measured comparison.
- World-in-World's finding that controllability matters more than visual quality supports grounding the world model in the twin, where actions and poses are exact.

### Gaps
- No verified navigation paper was found in which a world model generates **training** data or serves as an RL environment for a navigation policy with a real-robot evaluation.
- The DreamerNav article (PMC12510832) could not be fetched because of a captcha. Its claims are unverified.
- NWM training compute is not verified.

## Q4. Foundation navigation models (GNM, ViNT, NoMaD, NaVILA, Uni-NaVid, VLM-based): fine-tuning in sim or twins and data amounts

### Takeaway
Navigation foundation models are pretrained on large real and simulated corpora: Uni-NaVid on 3.6M samples, NaVILA on sim plus real plus human video. Adaptation to a specific deployment site via a twin is rare. The twin papers fine-tune smaller RL policies (EmbodiedSplat: 20M steps) or train a VLA on twin trajectories (NavGSim). ViNT is used as a zero-shot baseline, and in ReaDy-Go's test environments it scored 20–80% real SR vs. 70–100% for twin-trained policies.

### Cited Findings
- **NaVILA** (A.-C. Cheng, Y. Ji, Z. Yang, Z. Gongye, X. Zou, J. Kautz, E. Bıyık, H. Yin, S. Liu, X. Wang; arXiv:2412.04453, rev. Feb 2025; RSS 2025 per repo notes). A two-level system: a VLA emits mid-level language actions (e.g., "moving forward 75cm") and an RL visual-locomotion policy executes them. It has an IsaacLab benchmark and real legged-robot experiments. — [arXiv abs](https://arxiv.org/abs/2412.04453)
- **Uni-NaVid** (J. Zhang, K. Wang, S. Wang, M. Li, H. Liu, S. Wei, Z. Wang, Z. Zhang, H. Wang; arXiv:2412.06224; RSS 2025 per repo, not verified here). A video-based VLA trained on "3.6 million navigation data samples" across four tasks: VLN, ObjectNav, EQA and person following. — [arXiv abs](https://arxiv.org/abs/2412.06224)
- NavGSim (same group as Uni-NaVid) trains a navigation VLA on GS-twin trajectories. This is the closest "foundation model fine-tuned in a twin" precedent for navigation. — [arXiv abs](https://arxiv.org/abs/2603.15186)
- ViNT as a baseline in twin environments: 50/30, 60/20 and 80/40% real SR (static/dynamic; Outside, Lobby, Library) vs. ReaDy-Go 100/90, 90/70 and 100/80%. — [ReaDy-Go HTML](https://arxiv.org/html/2602.11575)
- GNM (ICRA 2023, doi:10.1109/ICRA48891.2023.10161227), ViNT (CoRL 2023, arXiv:2306.14846) and NoMaD are repo leads, not re-fetched. NWM's abstract explicitly ranks trajectories from external policies. — [NWM](https://arxiv.org/abs/2412.03572)
- RL fine-tuning of VLAs in simulation (manipulation) is crowded: VLA-RL arXiv:2505.18719, SimpleVLA-RL arXiv:2509.09674, RL4VLA arXiv:2505.19789 (NeurIPS 2025). OpenVLA arXiv:2406.09246 notes LoRA fine-tuning on consumer GPUs. These are repo leads. — see content/07-questions-hypotheses.md comments

### Inferences
- A realistic plan for the PhD:
  - start from a pretrained navigation policy (ViNT/NoMaD-class, a few hundred M params, or a NaVILA/Uni-NaVid-class ~7–8B VLA with LoRA);
  - fine-tune in the twin with imitation from a planner expert (ReaDy-Go-style, ~400 episodes per scene) and/or RL (EmbodiedSplat-style, ~20M steps).
- The data amounts for twin fine-tuning are small compared with pretraining. The budget constraint is real capture, not sim compute.

### Gaps
- No verified paper was found that fine-tunes NoMaD, ViNT, NaVILA or Uni-NaVid **inside a 3DGS twin of the deployment site** with a real before/after number.
- NaVILA's and Uni-NaVid's venues and dataset composition were not fully verified this session.

## Q5. Typical effect sizes and plausibility of H2 (+10 pp, uncertainty-guided twin + world model vs. uniform DR at the same real-data budget)

### Takeaway
Reported twin-vs-baseline effects are large, +20 to +90 pp, but they compare against weak baselines with 10–15 real trials. A +10 pp gain of one twin-training recipe over another (uniform DR) inside the **same** twin is plausible but at the edge of detectability. H2 appears novel for navigation: no matched-budget, uncertainty-targeted vs. uniform-DR comparison was found. Its realism depends on (a) where uniform DR sits relative to the ceiling and (b) having enough evaluation episodes.

### Cited Findings
- Twin vs. generic sim or pretrained baseline:
  - EmbodiedSplat: +20 pp (HM3D) and +40 pp (HSSD). — [arXiv abs](https://arxiv.org/abs/2509.17430)
  - Vid2Sim: +68.3% real. — [arXiv abs](https://arxiv.org/abs/2501.06693)
  - VR-Robo vs. SARO: +33 to +100 pp. — [arXiv HTML](https://arxiv.org/html/2502.01536)
- Within-twin design changes:
  - ReaDy-Go vs. Vid2Sim with the same policy and planner: +10 to +30 pp. — [arXiv HTML](https://arxiv.org/html/2602.11575)
  - VR-Robo DR vs. no DR: +47 to +100 pp. — [arXiv HTML](https://arxiv.org/html/2502.01536)
- Ceiling effects: several twin-trained policies already reach 90–100% real SR on their tasks (VR-Robo, ReaDy-Go static), which leaves no room for +10 pp on easy tasks. — [VR-Robo HTML](https://arxiv.org/html/2502.01536), [ReaDy-Go HTML](https://arxiv.org/html/2602.11575)
- Sample size: EmbodiedSplat uses 10 start–goal pairs per condition. — [arXiv HTML](https://arxiv.org/html/2509.17430v1)

### Inferences
- **Novelty.** Crowded: twin training for navigation (≥6 groups), world models for navigation planning (NWM, NavWM, PiJEPA), and world-model RL for manipulation VLAs. Open: (i) uncertainty-guided allocation of training or randomization in a navigation twin; (ii) a twin + learned-world-model hybrid for navigation-policy training; (iii) evaluation at a matched real-data budget. The closest precedents are TwinRL (manipulation, failure-targeted) and NavRL++ (perturbation-aware fine-tuning, no uncertainty from the twin).
- **Realism of +10 pp.**
  - Plausible when the uniform-DR baseline sits at roughly 40–75% SR: hard scenes, dynamic obstacles, image-goal tasks, or held-out regions poorly covered by capture. Within-twin design changes in the literature produce 10–30 pp there.
  - Implausible when the baseline sits above ~85%.
  - The world-model contribution is least evidenced. World-in-World warns that visual quality does not translate into task success, and no navigation paper shows real gains from world-model-generated training data.
- **Statistics.** Detecting +10 pp at ~60% baseline with α=0.05 one-sided and 80% power needs on the order of ~150–300 episodes per arm (rough two-proportion estimate; fewer if paired by scene). So the tier-A proxy reality with many scenes is essential. Real-robot tests with 10–20 trials can only confirm direction.
- **Suggested framing.** Keep +10 pp as the threshold, but pre-register the difficulty regime: the uniform-DR baseline should be ≤75% SR. Treat "+world model" as an ablation, as §7 already does.

### Gaps
- No published effect size for uncertainty-guided vs. uniform DR in navigation. The +10 pp prior is inferred from adjacent within-twin comparisons, not measured.
- No navigation paper reports real success as a function of real-data budget for twin training. A matched-budget comparison therefore cannot be benchmarked against published numbers.

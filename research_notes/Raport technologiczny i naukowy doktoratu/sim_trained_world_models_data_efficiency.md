# Sim-trained world models and policies that transfer to the real world, and methods that cut the real data needed for adaptation (2017 to Sept 2026)

Scope note: checked 2026-09-29 against arXiv abstract and HTML pages (fetched through a summarizing tool, so exact wording can differ slightly from the originals). Numbers are as the sources report them. Anything I could not confirm from a primary source is marked **[unverified]** or listed under Gaps. Venue labels come from the arXiv pages unless noted otherwise.

## 1. Methods for transferring sim-trained world models and policies to real data: randomization, image translation, co-training, sim-real pairing, photoreal transfer

### Takeaway
Three families show real-world gains. The first is broad randomization, both visual (Tobin 2017) and physical (Peng 2018, SkyJEPA 2026). The second is image-level sim-to-real translation that preserves task-relevant content (RCAN, RL-CycleGAN, RetinaGAN, and now Cosmos-Transfer). The third is sim-and-real co-training with a small real set (Maddukuri RSS 2025, Wei IROS 2025), which gives the most consistent low-data gains. Two 2025-2026 mechanistic analyses find that co-training works through *structured* alignment. Representations align, yet the domains stay separable, and forcing full sim-real invariance can hurt. For sim-trained **world models** (as opposed to policies), the 2026 evidence (SimDist, SkyJEPA, Zanatta et al., Wang et al. 2606.31101) is positive but comes mostly from small real evaluations (4-10 trials per condition) without factor-by-factor ablations.

### Cited Findings

**Domain randomization (appearance and physics)**
- Tobin et al. (IROS 2017): randomizing rendering (non-realistic random textures and other rendering parameters) makes "the real world just another variation". An object detector trained only on synthetic RGB localized objects in the real world to about 1.5 cm and was used for grasping in clutter. — [arXiv 1703.06907](https://arxiv.org/abs/1703.06907)
- Peng, Andrychowicz, Zaremba, Abbeel (ICRA 2018): dynamics randomization. Policies trained only in simulation kept "a similar level of performance" on a real object-pushing arm. — [arXiv 1710.06537](https://arxiv.org/abs/1710.06537)
- Physics randomization in a sim-trained world model: SkyJEPA uses 20,000 ten-second reference trajectories over 500 randomized domains. Ranges: mass ±50%, inertia ±30%, motor time constant [0.01, 0.1] s, drag [0.1, 0.5], thrust/torque coefficients ±50%. — [SkyJEPA HTML](https://arxiv.org/html/2606.23444)

**Image translation that preserves task content (RCAN, RL-CycleGAN, RetinaGAN)**
- RCAN (James et al., CVPR 2019) translates randomized sim images *and* real images into a canonical sim rendering. It reached 70% zero-shot grasp success on unseen objects, which the authors say is almost double domain randomization alone. With 5,000 real grasps it reached 91%, comparable to a QT-Opt system trained on 580,000 real grasps (">99%" less real data). — [arXiv 1812.07252](https://arxiv.org/abs/1812.07252)
- RL-CycleGAN (Rao et al., CVPR 2020) adds an RL-consistency (Q-value) loss to CycleGAN. Real grasp success by method: plain sim 21% (95% in sim), visual randomization 37%, GAN 29%, CycleGAN 61%, GraspGAN 63%, RL-CycleGAN 70%. With 5,000 real grasps it went from 15% to 75%; with 28,000, from 16% to 86%; with 580,000, from 87% to 94% (SOTA was 96%). 5,000 off-policy grasps plus 10,000 on-policy fine-tuning matched RCAN's 94% (which needed 28,000 on-policy episodes). — [arXiv 2006.09001 PDF, Tables 1-4](https://arxiv.org/pdf/2006.09001)
- RetinaGAN (Ho et al., ICRA 2021) uses object-detection consistency for sim-to-real GAN transfer. It was evaluated on grasping, pushing and door opening, and claims "transfer with no additional real data requirements" for pushing. The abstract gives no numbers, so specific success rates are **[unverified]**. — [arXiv 2011.03148](https://arxiv.org/abs/2011.03148)

**Photorealistic transfer with Cosmos-Transfer**
- Cosmos-Transfer2.5 (NVIDIA, arXiv 2511.00062) is a ControlNet-style model for Sim2Real and Real2Real translation, 2B parameters, "3.5× smaller" than Cosmos-Transfer1-7B. In its robot experiment (bimanual Kinova Gen3, pick-and-place, 100 real teleop demos) the success counts were 1/30 with no augmentation, 5/30 with standard colour/brightness augmentation and 24/30 with Cosmos-Transfer2.5 augmentation. This experiment is **Real2Real**, not sim-to-real. — [arXiv 2511.00062v2](https://arxiv.org/html/2511.00062v2)
- EMMA (arXiv 2509.22407) uses Cosmos-Transfer1 as a baseline. Policies trained with Cosmos-Transfer1 data gained about 22% success over no augmentation. Per task: Fold Cloth 40% (real-to-real), Clean Desk 70% and Throw Bottle 40% (sim-to-real). EMMA's DreamTransfer scored 65%, 80% and 50%. — [arXiv 2509.22407](https://arxiv.org/html/2509.22407v1)
- NVIDIA's SO-101 sim-to-real course treats DR, co-training and Cosmos augmentation as separate "strategies". It shows example control weights (depth 0.2, edge 1.0, seg 0.3, vis 0.1) but reports no quantitative comparison. — [NVIDIA SO-101 tutorial](https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/latest/14-strategy3-cosmos.html)

**Sim-and-real co-training**
- Maddukuri et al. (RSS 2025, per the project page and search listings; the arXiv v2 does not state the venue) report that simulation data improves real success by an average of 38%. Setup: 50 real demos per task (Panda) or 20 (humanoid). Sim data was 10,000 task-aware "digital cousin" demos per task (Panda) or 1,000 (humanoid); prior task-agnostic sim sets were 60k demos over 20 tasks and 10k demos. Other findings:
  - Real+DC gives +35.8% and Real+Prior +31.5%.
  - The best co-training ratio was α = 99% sim. At 99.5% or 99.9%, success fell from 95% to 60%.
  - Camera misalignment reduced co-training success from 67% to 56% (Panda) and from 95% to 70% (humanoid).
  - Sources: [arXiv 2503.24361](https://arxiv.org/html/2503.24361), [co-training.github.io](https://co-training.github.io/)
- Wei et al. (IROS 2025, planar pushing from pixels, Drake/Tedrake lab). Setup: 10/50/150 real demos with 500-4000 sim demos. With 10 real demos: 14/20 cotrained vs 2/20 real-only; with 50: 19/20 vs 10/20. Other findings:
  - Removing the physics gap raised success by 15.5% over a "Level 1" physics shift. For contact-rich tasks, physics gap matters more than visual realism.
  - Linear probes separate sim from real at 100% accuracy in the embedding of good policies. Removing the visual gap while physics differs *hurt* performance, because the policy can no longer tell the domains apart.
  - Scaling law: test loss ∝ |D_S|^-0.332 · |D_T|^-0.397 (R² = 0.945).
  - Gains plateau as sim data grows; more real data raises the ceiling. The optimal α increases with real-data size.
  - Source: [arXiv 2503.22634](https://arxiv.org/html/2503.22634)
- Lei, Liu, Maddukuri, Jiang, Zhu (arXiv 2604.13645, Apr 2026) name two mechanisms:
  - "Structured representation alignment" (balancing cross-domain alignment and domain discernibility) is the primary one; an "importance reweighting" effect is secondary.
  - Their method, CFG-ADDA (domain one-hot label with classifier-free guidance, plus an adversarial discriminator on the remaining dimensions), reached 21/30. Baselines: real-only 8.6/30, co-training 15.3/30, +OT 14.3/30, +ADDA 14.3/30. Setting: robosuite tasks, 50 target demos, about 3000 MimicGen source trajectories.
  - They warn that "blind representation alignment can be harmful".
  - Sources: [arXiv 2604.13645](https://arxiv.org/html/2604.13645v1), [project page](https://science-of-co-training.github.io/)
- Cheng et al. (Georgia Tech and NVIDIA, arXiv 2509.18631): co-training with an (unbalanced) optimal-transport loss that aligns *joint* observation-action distributions. Setup: 10-25 real demos per task and 1000 MimicGen sim demos. Results: real in-distribution averages of 0.73 (image) and 0.77 (point cloud), and "up to 30%" real success improvement, including on scenarios seen only in sim. Baselines were MMD, plain co-training, source-only and target-only. — [arXiv 2509.18631](https://arxiv.org/html/2509.18631v1)
- Shi et al. (arXiv 2602.12628, 2026): SFT on mixed sim and real data, then RL in simulation with an auxiliary supervised loss on real data. Gains: +24% real success (OpenVLA) and +20% (π0.5). — [arXiv 2602.12628](https://arxiv.org/abs/2602.12628)

**Objectives that pair sim frames with real or realistic versions**
- X-Sim (arXiv 2505.07096): replays 10 real rollouts in simulation from the same initial state (FoundationPose on the first frame) to build paired real and sim images. An InfoNCE loss pulls paired embeddings together. Gains: +8% average task progress, +13% on the hardest task (Mug Insert). — [arXiv 2505.07096v5](https://arxiv.org/html/2505.07096v5)
- Invariance Co-training (Yang, Finn, Sadigh, arXiv 2512.05230): a BC loss plus contrastive alignment, extrinsics-regression and bounding-box auxiliary losses. Data: 200 demos per task, static-scene videos and synthetic data (LIBERO, Unreal, Simpler). Gains: +40% over plain BC under viewpoint, lighting and distractor shifts; +18% over generative-augmentation baselines. — [arXiv 2512.05230](https://arxiv.org/html/2512.05230)
- The closest existing analogue to "sim frame ↔ Cosmos-Transfer version of the same frame" is RCAN-style canonicalization combined with X-Sim-style paired contrastive loss. I found no published work that trains a world model with an explicit invariance or contrastive loss on (simulator frame, Cosmos-Transfer rendering of that frame) pairs.

**Sim-trained world models transferred to real (2025-2026)**
- SimDist (Levy, Westenbroek, …, Gupta, Fridovich-Keil; RSS 2026; arXiv 2603.15759). Components: encoder E, history encoder C, latent dynamics f, and transformer reward, value and base-policy heads.
  - Pretraining data is diverse sim data: experts, intermediate checkpoints and action-perturbed rollouts. Simulators: Isaac Sim (quadruped) and MuJoCo-based (manipulation).
  - Sim-data ablation (Peg success): 100% data 0.90, 50% 0.72, 10% 0.06, expert-only 0.10, no transformer reward/value 0.82.
  - Real-world results are in Section 2. — [arXiv 2603.15759 HTML](https://arxiv.org/html/2603.15759)
- SkyJEPA (Rao, Zhang, Balestriero, LeCun, Loianno; arXiv 2606.23444, under review). About 99K parameters: a TCN state/action encoder, a GRU predictor, and a SIGReg-style regularizer (λ = 0.02). A "physics-inspired prober" on frozen latents is used with MPPI, and the model is trained **only on physics-randomized sim**.
  - Open-loop results (pos RMSE m / attitude °): predictive baseline 8.80/53.4, + physics reg 7.12/49.1, reconstruction + prober 6.82/45.2, reconstruction + PI prober 1.53/5.28, SkyJEPA + PI prober 1.43/4.71.
  - Real closed-loop circle: 0.24 m / 7.87° vs MPPI baselines 0.36-0.39 m / 10.99-11.95°. Propeller swap: 0.39 m vs 0.51-0.53 m.
  - Compounding error at k = 60: 1.4× vs 2.4×. State RMSE drops from 5.4 to 1.4 as "trajectory distribution quality" rises from 0.01 to 0.94.
  - Runs near a 10 ms budget on an Orin NX.
  - Source: [arXiv 2606.23444 HTML](https://arxiv.org/html/2606.23444)
- Zanatta, Malczyk, Alexis (arXiv 2606.05015). Setup: DreamerV3 world models trained on depth images in AerialGym at four randomization levels (L1 fixed layout to L4 fully uniform), with no real training data.
  - The most influential hyperparameters were discrete latent size and training-sequence length (L_batch = 64 was best).
  - Every model that generalized well in the self-supervised cross-environment reconstruction check (MSE/SSIM) deployed successfully in the real world (4/4 trials; gaps as narrow as 0.67 m). WM3, which had the best RL sim score (92.5% on L3), failed on the real platform (0/4). Sim RL win rate was therefore a poor predictor of deployability. WM1 scored 99.5% in-distribution and 54.5% out of distribution.
  - Open-loop imagination completed a 12 m traverse after 2.5 s of sensory context.
  - Source: [arXiv 2606.05015 HTML](https://arxiv.org/html/2606.05015)
- Wang Z. et al., "Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors" (CVPR'26 Embodied AI Workshop; arXiv 2606.31101).
  - Cosmos Policy (post-trained Cosmos-Predict2) trained on about 800 AnyTask motion-planned sim demos per task (about 3,200 in total). Randomization covered textures, camera poses, lighting and object placement.
  - Zero-shot on a Franka FR3 with **zero real demos**: 35% average (banana 5/10, brick 5/10, drawer 2/10, strawberry 2/10). The abstract calls it the "first successful sim-to-real transfer of a world-action model".
  - The authors explicitly leave a "controlled ablation of each factor" (video prior vs DR vs joint video-action objective) to future work.
  - Source: [arXiv 2606.31101 HTML](https://arxiv.org/html/2606.31101)
- Wang Y. et al. (Hao Su lab, arXiv 2510.02538, revised 2026-09-18). CDRED world model (an imitation variant of TD-MPC2 with a reward model), pretrained with online imitation in ManiSkill3, then fine-tuned offline on real demos.
  - The abstract claims at least +31.7% (sim-to-sim) and at least +23.3% (sim-to-real) success.
  - Real results vs best baseline: Cabinet Open 9/10 vs 4/10, Push Cube 10/10 vs 9/10, Pick Cube 8/10 vs 6/10, Stack Cube 5/10 vs 4/10.
  - The fetched summary also reported an "overall improvement: 113.3%". This probably uses a different (relative) metric and conflicts in form with the abstract's "at least 23.3%", so **treat 113.3% as [unverified]**.
  - Source: [arXiv 2510.02538](https://arxiv.org/html/2510.02538)

### Inferences
- The strongest *real-world* evidence (Wei, Maddukuri, Lei) says the aim should be *alignment plus domain discernibility*, not full invariance. This bears directly on RQ2's "objective pairing simulated frames with their photorealistic versions": a pure invariance loss could hurt when physics differs. A soft or partial alignment (CFG-ADDA-like, or aligning only a subset of latent dimensions) is the better-supported design.
- For contact-rich dynamics, physics fidelity or physics randomization matters more than visual realism (Wei). For vision-heavy prediction, camera alignment matters a lot (Maddukuri). Both points favour factorial RQ2 experiments that separate appearance randomization, photoreal transfer and physics randomization.
- Zanatta suggests that self-supervised prediction quality on held-out environments, *not* task reward, is the right proxy for real deployability of a sim-trained world model. This supports RQ2's choice of "prediction on real recordings" as the main metric.
- The Cosmos-Transfer gains measured so far come mostly from Real2Real augmentation or policy training. Using it as a *sim-to-real bridge for world-model training* has not been validated quantitatively.

### Gaps
- I found no controlled study that compares appearance DR, Cosmos-Transfer photoreal transfer, physics DR, paired-frame alignment and co-training *within one world model* on real-recording prediction metrics. Wang Z. et al. (2606.31101) explicitly defer that ablation.
- RetinaGAN numbers and Cosmos-Transfer1's own robotics numbers were not verified from full text.
- Temporal consistency of Cosmos-Transfer outputs, and whether translated frames keep action-relevant geometry precise enough for dynamics learning, lacks quantitative robotics evidence.
- SimDist, SkyJEPA and Zanatta use 4-10 real trials per condition, which gives wide confidence intervals.

## 2. Reducing the real data needed to adapt world models and policies (PEFT, which modules to fine-tune, demo counts, test-time adaptation)

### Takeaway
Across 2019-2026, the consistent pattern is to keep the sim-pretrained encoder and task heads **frozen** and adapt a small part of the model: the dynamics, an inverse-dynamics model, LoRA adapters, or a hypernetwork-generated LoRA. This works with minutes of real data or tens of demos. The typical real budgets reported are 10-50 demos (co-training), 15-50 trajectories (world-model offline fine-tuning), 15-36 minutes of real interaction (SimDist), about 2 minutes (FADA), "seconds" (CLAW), and 30 minutes of play data (DreamZero, embodiment transfer).

### Cited Findings
- SimDist: during real adaptation **only the latent dynamics f is updated**, with a supervised prediction loss; encoder, history encoder, reward, value and policy stay frozen.
  - Unfreezing the encoder led to "complete performance loss"; unfreezing the value head caused "catastrophic forgetting".
  - Real data used: about 15-30 minutes (manipulation; 20 teleop demos in some variants), 32.1 minutes (quadruped Foam) and 35.7 minutes (Slippery Slope).
  - Slippery Slope: 1.82 m and 5/5 successes vs IQL 0.39 m 0/5 and RLPD 0.34 m 0/5. Foam: 3.00 m 5/5 vs IQL 2.25 m 2/5. Peg Wide success 0.90.
  - About 2× the success of the baselines (Diffusion Policy, π0.5, RLPD, IQL, SGFT-SAC), and 1.5-2× throughput gains over zero-shot.
  - Source: [arXiv 2603.15759 HTML](https://arxiv.org/html/2603.15759)
- CLAW (Palafox and Fridovich-Keil, arXiv 2609.12278, Sept 2026): a hypernetwork generates LoRA adapters for a world model from "seconds" of test-time data. It outperforms gradient-based adaptation and in-context learning in locomotion and manipulation. The abstract gives no numbers. — [arXiv 2609.12278](https://arxiv.org/abs/2609.12278)
- FADA (Xie, …, Simchowitz, Shi; arXiv 2606.28476): planner plus inverse dynamics model (IDM). The planner is frozen and only the IDM is fine-tuned, on about 2 minutes of target rollouts. It beats in-context and end-to-end adaptation on real humanoids. — [arXiv 2606.28476](https://arxiv.org/abs/2606.28476)
- OpenVLA (Kim et al., 2024), PEFT study on Franka tasks with 10-150 demos:
  - full fine-tuning: 69.7% (7,188M params, 163.3 GB)
  - last layer: 30.3%
  - frozen vision encoder: 47.0%
  - "sandwich": 62.1%
  - LoRA r = 32/64: about 68.2% with 1.4% of parameters (97.6-195.2M, about 60 GB)
  - Freezing the vision encoder hurt, which suggests the *visual* representation must adapt for new scenes.
  - Source: [arXiv 2406.09246](https://arxiv.org/html/2406.09246)
- WestWorld (arXiv 2603.14392): fine-tuning only the last two Sys-MoE layers (21.91% of parameters) beats a fully fine-tuned TrajWorld baseline on three robots. Pretraining gives lower MSE across 10 fine-tuning episodes (based on the search snippet; full text not checked, so **[partially verified]**). — [arXiv 2603.14392](https://arxiv.org/pdf/2603.14392)
- DreamZero (Ye et al., arXiv 2602.15922): a 14B world-action model built on a video-diffusion backbone. Results: more than 2× generalization over VLAs; +42% relative on unseen tasks from 10-20 minutes of cross-embodiment video; embodiment adaptation from 30 minutes of play data; 7 Hz real-time control. — [arXiv 2602.15922](https://arxiv.org/abs/2602.15922)
- Ctrl-World (Guo, Shi, Chen, Finn; ICLR 2026): an SVD-based action-conditioned world model trained on DROID (95k trajectories, 564 scenes). Imagined successful rollouts used for SFT raised policy success by 44.7%. — [arXiv 2510.10125](https://arxiv.org/abs/2510.10125), [GitHub](https://github.com/Robert-gyj/Ctrl-World)
- Demo counts with sim priors:
  - Wang Y. et al.: 15-50 real trajectories per task for offline fine-tuning, and 50% on Cabinet Open with only 20. — [arXiv 2510.02538](https://arxiv.org/html/2510.02538)
  - Cheng et al.: 10-25 real demos per task. — [arXiv 2509.18631](https://arxiv.org/html/2509.18631v1)
  - Wei et al.: 10 real demos plus sim gives 14/20 vs 2/20 real-only. — [arXiv 2503.22634](https://arxiv.org/html/2503.22634)
  - Maddukuri: 20-50 real demos. — [arXiv 2503.24361](https://arxiv.org/html/2503.24361)
- Historical data-reduction numbers: RCAN reached 91% with 5k real grasps, against 580k needed without sim (">99%" reduction). RL-CycleGAN matched 580k-grasp performance with 28k (about 20× fewer). — [arXiv 1812.07252](https://arxiv.org/abs/1812.07252), [arXiv 2006.09001](https://arxiv.org/pdf/2006.09001)

### Inferences
- For RQ3, two partly conflicting findings bound the design space. SimDist says freeze the sim-pretrained encoder and adapt only the dynamics; there the encoder was trained on sim observations and reused on real, and unfreezing it destroyed performance. OpenVLA says freezing vision hurts. This tension probably depends on how well the pretrained encoder already covers the real visual domain. So "which layers or adapters to adapt, as a function of the visual gap" is an open and testable RQ3 variable.
- The data budgets reported for adaptation to *new real scenes* (minutes, or 10-50 demos) set a realistic target range for RQ3 learning curves. A study could report error vs number of real clips in roughly 0/10/25/50/100 steps.

### Gaps
- I found no systematic study of *continued pretraining choices* for world-model encoders (e.g. continued SSL on unlabeled real video vs LoRA on the dynamics vs full fine-tuning), measured by real-data-efficiency curves.
- Test-time and few-shot adaptation work on world models (CLAW, FADA, SimDist) mostly targets *dynamics* shift. Adapting to *visual scene* shift with minimal real data is far less studied.
- Numbers for CLAW and WestWorld were not verified beyond abstracts or snippets.

## 3. What controlled comparisons exist, and what gaps remain

### Takeaway
Controlled, factorial evidence exists mainly for **policies** trained by co-training: Wei et al. vary physics gap, visual gap, α and data sizes, and Maddukuri et al. vary sim type, α and camera alignment. There are also two older head-to-head image-translation comparisons (RL-CycleGAN Table 1; RCAN vs DR). For sim-trained **world models** judged by prediction on real recordings, the only systematic study I found is Zanatta et al. (randomization level and architecture sweeps, on depth rather than RGB). No study compares appearance DR, photoreal transfer (Cosmos-Transfer), physics DR, paired alignment objectives and small-real co-training head to head.

### Cited Findings
- Controlled factor studies:
  - Wei et al. (physics vs visual gap, mixing ratio, data scaling law) — [arXiv 2503.22634](https://arxiv.org/html/2503.22634)
  - Maddukuri et al. (task-aware vs prior sim, α, camera alignment) — [arXiv 2503.24361](https://arxiv.org/html/2503.24361)
  - Lei et al. (co-training vs OT vs ADDA vs CFG vs CFG-ADDA) — [arXiv 2604.13645](https://arxiv.org/html/2604.13645v1)
  - Cheng et al. (OT vs MMD vs co-training) — [arXiv 2509.18631](https://arxiv.org/html/2509.18631v1)
- Visual-transfer head-to-heads: RL-CycleGAN vs randomization vs GAN vs CycleGAN vs GraspGAN (21%, 37%, 29%, 61%, 63%, 70%). — [arXiv 2006.09001](https://arxiv.org/pdf/2006.09001)
- Cosmos-Transfer comparisons: Cosmos-Transfer2.5 vs standard augmentation (24/30 vs 5/30, Real2Real) — [arXiv 2511.00062](https://arxiv.org/html/2511.00062v2); Cosmos-Transfer1 vs DreamTransfer — [arXiv 2509.22407](https://arxiv.org/html/2509.22407v1)
- World-model-specific studies:
  - Zanatta et al., randomization-level sweep with real deployment — [arXiv 2606.05015](https://arxiv.org/html/2606.05015)
  - SkyJEPA, objective ablation (predictive vs reconstruction vs JEPA plus prober) — [arXiv 2606.23444](https://arxiv.org/html/2606.23444)
  - SimDist, sim data diversity and which modules to fine-tune — [arXiv 2603.15759](https://arxiv.org/html/2603.15759)
- Explicitly acknowledged missing ablation: Wang Z. et al. do not separate the video prior, DR and the joint action-video objective. — [arXiv 2606.31101](https://arxiv.org/html/2606.31101)

### Inferences
- An RQ2 study that varies appearance DR, Cosmos-Transfer, physics DR, paired-frame objective and small-real co-training in one world-model pipeline, scored on real-recording prediction, would fill a gap that these papers show clearly. The co-training literature already gives strong priors: expect a plateau with sim volume, a best α near high-sim ratios, and possible harm from forced invariance.
- An RQ3 study of encoder pretraining vs real-data-efficiency curves (which module to adapt, with LoRA vs full vs dynamics-only) would also be new. SimDist and OpenVLA give conflicting priors that such a study could reconcile.

### Gaps
- Nothing located after Sept 2026. Some 2026 preprints (SkyJEPA, 2606.31101, CLAW, FADA) are under review, and their numbers may change.
- Evaluation protocols differ widely (success over 10-30 trials, RMSE, MSE/SSIM), so numbers are not comparable across papers.
- I found no public benchmark of *real recordings* for scoring the prediction quality of sim-trained world models across these randomization and transfer choices.

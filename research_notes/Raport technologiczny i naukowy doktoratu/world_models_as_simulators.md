# Learned world models as simulators for robot policy learning and evaluation (2023 to September 2026), including World Action Models (WAMs)

Notes compiled 2026-09-29. Sources are primary (arXiv abstracts/HTML, project pages, GitHub READMEs, company tech reports) unless stated. Items marked **[UNVERIFIED]** were not confirmed against a primary source in this session. Numbers are quoted as reported by the authors; none were independently reproduced.

## Q1. Key systems: method, results, training, released artifacts, licences, stated limitations

### Takeaway
The field moved in three steps: (1) 2023-2024 "universal" action-conditioned video simulators (UniSim, Navigation World Models, Cosmos) showing that a video generator can stand in for an environment; (2) 2025 robot-specific, policy-in-the-loop world models used to generate training data (DreamGen) and to evaluate or improve generalist VLA policies (Ctrl-World, Veo World Simulator, 1XWM, WorldGym/WorldEval); (3) 2026 "World Action Models" that fine-tune a pretrained video diffusion backbone to output actions directly (Cosmos Policy, DreamZero, Cosmos 3), plus closed loops that co-train policy and world model on real rollouts (VLAW). Open release is dominated by NVIDIA (Apache-2.0 code, NVIDIA Open Model License or OpenMDW weights) and Stanford/academic groups (MIT-licensed Ctrl-World); Google DeepMind, 1X and Wayve systems are closed.

### Cited Findings

**UniSim (Yang et al., ICLR 2024; Google DeepMind / UC Berkeley / MIT)**
- Authors: Sherry Yang, Yilun Du, Kamyar Ghasemipour, Jonathan Tompson, Leslie Kaelbling, Dale Schuurmans, Pieter Abbeel; "Learning Interactive Real-World Simulators", arXiv 2310.06114 — [arXiv](https://arxiv.org/abs/2310.06114)
- Method: a single generative (video diffusion) simulator trained by orchestrating heterogeneous data, "abundant objects in image data, densely sampled actions in robotics data, and diverse movements in navigation data"; it simulates visual outcomes of both high-level instructions ("open the drawer") and low-level controls ("move by x,y") — [arXiv](https://arxiv.org/abs/2310.06114); [ICLR 2024 oral page](https://iclr.cc/virtual/2024/oral/19722)
- Result: both high-level vision-language planners and low-level RL policies trained purely in UniSim "can be deployed in the real world in zero shot"; the RL policy was transferred zero-shot to the real Language Table task — [arXiv](https://arxiv.org/abs/2310.06114); [ICLR proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/c4d66eae503694424123b93ac0fbaf17-Paper-Conference.pdf)
- Venue: ICLR 2024, oral — [ICLR](https://iclr.cc/virtual/2024/oral/19722). (Commonly cited as an ICLR 2024 Outstanding Paper award winner — **[UNVERIFIED in this session]**.)
- Release: no public weights/code found **[UNVERIFIED; I found no release]**. Quantitative real-robot success numbers were not captured in this session (see Gaps).

**NVIDIA Cosmos World Foundation Model platform (arXiv 2501.03575, Jan 2025)**
- Framing: "Physical AI needs to be trained digitally first. It needs a digital twin of itself, the policy model, and a digital twin of the world, the world model." Platform = video curation pipeline, pretrained WFMs, post-training examples, tokenizers — [arXiv](https://arxiv.org/abs/2501.03575)
- Data: ~20 million hours of raw video curated into ~100 million clips (2-60 s) — [arXiv HTML v3](https://arxiv.org/html/2501.03575v3)
- Models (Cosmos-Predict1): diffusion 7B and 14B (Text2World, Video2World); autoregressive 4B, 5B-Video2World, 12B, 13B-Video2World; tokenizers Cosmos-Tokenize1-CV (continuous, 8x8x8 at 720p) and -DV (discrete, 8x16x16) — [arXiv HTML v3](https://arxiv.org/html/2501.03575v3)
- Licence: weights under the NVIDIA Open Model License; paper CC BY 4.0 — [arXiv HTML v3](https://arxiv.org/html/2501.03575v3); [arXiv](https://arxiv.org/abs/2501.03575)
- Stated limitations: "object permanence, contact dynamics, and accurate physics simulation" remain difficult — [arXiv HTML v3](https://arxiv.org/html/2501.03575v3)

**Cosmos-Predict2.5 (Oct 2025 to Feb 2026)**
- 2B (pretrained, post-trained, distilled) and 14B (pretrained, post-trained) models; robotics variants include an action-conditioned model, Multiview-AgiBot (three cameras), and policy models post-trained on LIBERO and RoboCasa — [GitHub cosmos-predict2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5)
- Releases: 6 Oct 2025 launch; 19 Dec 2025 Diffusers support and distilled checkpoints; 23 Feb 2026 robot policy models — [GitHub](https://github.com/nvidia-cosmos/cosmos-predict2.5)
- Licence: code Apache 2.0, weights NVIDIA Open Model License. The repo states it is no longer under active development, superseded by Cosmos 3 — [GitHub](https://github.com/nvidia-cosmos/cosmos-predict2.5)

**Cosmos Transfer and Cosmos Reason**
- Cosmos-Transfer1 (multi-control-conditioned sim-to-real style transfer, e.g. segmentation/depth/edge to photoreal video; arXiv 2503.14492) and Cosmos-Reason1 (physical-reasoning VLM; arXiv 2503.15558) — **[UNVERIFIED in this session; from background knowledge, not fetched]**. Their role for the PhD topic: Transfer is NVIDIA's tool for making physics-simulator renders photoreal (appearance-gap reduction); Reason is used as a critic/judge of physical plausibility.

**Cosmos Policy (Kim et al., arXiv 2601.16163, Jan 2026; NVIDIA + Stanford)**
- Authors include Moo Jin Kim, ..., Chelsea Finn, Jinwei Gu — [project page](https://research.nvidia.com/labs/cosmos-lab/cosmos-policy/)
- Method: single-stage post-training of Cosmos-Predict2 on target-robot demonstrations, "no architectural modifications"; robot actions are encoded as latent frames inside the video latent diffusion process; the same model also predicts future states and values — [arXiv](https://arxiv.org/abs/2601.16163)
- Results: LIBERO 98.5% average success (vs pi0.5 96.9%, OpenVLA-OFT 97.1%, Diffusion Policy 72.4%); RoboCasa 67.1% with 50 demos (pi0 needs 300 demos for 62.5%); "highest average score" on real bimanual ALOHA tasks — [arXiv](https://arxiv.org/abs/2601.16163); [project page](https://research.nvidia.com/labs/cosmos-lab/cosmos-policy/)
- With rollout data, the model can refine its world model and value function and use model-based planning for higher success (quantity not captured) — [arXiv](https://arxiv.org/abs/2601.16163)
- Release: code, models and training data stated as available via the project page — [arXiv](https://arxiv.org/abs/2601.16163). Exact licence not confirmed (likely Apache-2.0 code / NVIDIA Open Model License weights, as for Predict2.5) — **[UNVERIFIED]**.

**Cosmos 3 (NVIDIA, arXiv 2606.02800, June 2026)**
- "Omnimodal" world models jointly processing and generating language, image, video, audio and action with a unified mixture-of-transformers; consolidates VLM, video generator, world simulator and world-action model into one architecture — [arXiv](https://arxiv.org/abs/2606.02800)
- Reported: top open-source T2I and I2V rankings on Artificial Analysis and "best policy model" on RoboArena — [arXiv](https://arxiv.org/abs/2606.02800)
- Release: code, checkpoints, synthetic datasets and benchmarks under the Linux Foundation OpenMDW-1.1 License (a licence change from the NVIDIA Open Model License) — [arXiv](https://arxiv.org/abs/2606.02800)

**Navigation World Models (Bar, Zhou, Tran, Darrell, LeCun; CVPR 2025; Meta FAIR / NYU / Berkeley)**
- Method: Conditional Diffusion Transformer (CDiT), 1B parameters, predicts future egocentric frames from past frames and navigation actions; trained on egocentric videos from humans and robots — [arXiv 2412.03572](https://arxiv.org/abs/2412.03572)
- Uses: planning by simulating trajectories and checking the goal, ranking trajectories from an external policy, imagining trajectories in unfamiliar environments from a single image — [arXiv](https://arxiv.org/abs/2412.03572); [project page](https://www.amirbar.net/nwm/)
- Release: project page linked; code repo and weight licence not confirmed this session **[UNVERIFIED]** (the CC BY 4.0 shown on arXiv is the paper licence).

**DreamGen (Jang et al., arXiv 2505.12705, CoRL 2025; NVIDIA GEAR + UW + UT Austin)**
- 4-stage pipeline: (1) LoRA fine-tune a video world model (mainly WAN 2.1) on target-robot data; (2) prompt it to generate synthetic videos; (3) label pseudo-actions with an inverse dynamics model (IDM) or latent actions (LAPA); (4) train visuomotor policies on these "neural trajectories" — [arXiv HTML](https://arxiv.org/html/2505.12705)
- Results: a GR1 humanoid performed 22 new behaviours from pick-and-place-only teleop data: 43.2% success on new behaviours in seen environments, 28.5% in unseen environments (baseline 0%) — [arXiv HTML](https://arxiv.org/html/2505.12705); [arXiv](https://arxiv.org/abs/2505.12705)
- Augmentation: GR1 37% to 46.4%; Franka 23% to 37%; SO-100 21% to 45.5%; in RoboCasa, log-linear gains up to 333x synthetic data — [arXiv HTML](https://arxiv.org/html/2505.12705)
- DreamGen Bench scores of video models (WAN, Hunyuan, CogVideoX, Cosmos) correlate positively with downstream policy performance — [arXiv HTML](https://arxiv.org/html/2505.12705)
- Limitations: compute (54 hours on 1500 GPUs for the RoboCasa set), reliance on manually provided initial frames, weak automatic physics evaluators — [arXiv HTML](https://arxiv.org/html/2505.12705)
- Code: [NVIDIA/GR00T-Dreams](https://github.com/NVIDIA/GR00T-Dreams). CoRL 2025 acceptance per task brief — **[UNVERIFIED in this session]**.

**Ctrl-World (Guo, Shi, Chen, Finn; arXiv 2510.10125; ICLR 2026; Stanford + Tsinghua)**
- Controllable multi-view world model for evaluating and improving generalist policies; pose-conditioned memory retrieval for consistency and frame-level action conditioning for precision; trained on DROID (95k trajectories, 564 scenes); consistent rollouts for over 20 s — [arXiv](https://arxiv.org/abs/2510.10125)
- Results: ranks policy performance without real rollouts; fine-tuning on successful imagined trajectories gives +44.7% policy success — [arXiv](https://arxiv.org/abs/2510.10125)
- Built on Stable Video Diffusion + CLIP encoders; ~10 s per inference step on A100 (~5 s on H100); code MIT, checkpoint on Hugging Face; README lists ICLR 2026 — [GitHub](https://github.com/Robert-gyj/Ctrl-World)

**World-in-World (Zhang et al., arXiv 2510.18135; ICLR 2026 Oral; JHU and co.)**
- First platform to benchmark generative world models in closed-loop agent-environment interaction, scored on task success rather than visual metrics — [arXiv](https://arxiv.org/abs/2510.18135)
- Findings: "(1) visual quality alone does not guarantee task success, controllability matters more; (2) scaling post-training with action-observation data is more effective than upgrading the pretrained video generators; (3) allocating more inference-time compute allows WMs to substantially improve closed-loop performance"; also reports data scaling laws for embodied WMs — [arXiv](https://arxiv.org/abs/2510.18135)
- Code: [GitHub](https://github.com/World-In-World/world-in-world) (licence not checked)

**VLAW (Guo, Lee, Shi, Chen, Liang, Finn; arXiv 2602.12063; ICML 2026 poster; Stanford)**
- Iterative co-improvement: Ctrl-World world model + pi0.5 policy + Qwen3-VL-4B reward model fine-tuned on rollouts. Per iteration: 50 real rollouts per task; fine-tune WM on those plus DROID; generate 500 synthetic trajectories; keep those with reward prob > 0.8; update the policy with flow matching; two iterations — [arXiv HTML](https://arxiv.org/html/2602.12063)
- Platform: Franka Panda, DROID setup, 3 cameras; 5 contact-rich tasks (block stacking, book opening, whiteboard erasing, scooping, circle drawing) — [arXiv HTML](https://arxiv.org/html/2602.12063)
- Results: mean success 46.0% to 86.8% (+39.2 points absolute); +11.6 points attributable to synthetic rollouts over training on real rollouts alone — [arXiv HTML](https://arxiv.org/html/2602.12063)
- Key point for the PhD: fine-tuning the WM on online rollouts, including failures, is "crucial"; all video-quality metrics (PSNR, SSIM, LPIPS, FID, FVD) improve — [arXiv HTML](https://arxiv.org/html/2602.12063)
- Limitation: only five task categories — [arXiv HTML](https://arxiv.org/html/2602.12063). ICML 2026 poster confirmed — [ICML](https://icml.cc/virtual/2026/poster/66169). No code link found.

**DreamZero (Ye, Ge, ..., Fan, Jang; arXiv 2602.15922, Feb 2026; NVIDIA)**
- "World Action Models are Zero-shot Policies": a 14B autoregressive video diffusion WAM that predicts future frames and actions jointly — [arXiv](https://arxiv.org/abs/2602.15922); [project](https://dreamzero0.github.io/)
- Results: "over 2x improvement in generalization to new tasks and environments" vs SOTA VLAs on real robots; seen tasks 62.2% vs 27.4% for best VLA baseline; DROID unseen verbs 49% vs 25-32%; real-time 7 Hz (150 ms per action chunk, 38x speed-up from optimisations); cross-embodiment gain >42% relative on unseen tasks; adapts to a new embodiment (YAM) with 30 min of play data (55 trajectories) — [arXiv](https://arxiv.org/abs/2602.15922); [project](https://dreamzero0.github.io/)
- Base: Wan2.1-I2V-14B-480P. Release: Apache 2.0; checkpoints DreamZero-DROID (14B) and DreamZero-AgiBot (~45 GB); needs at least 2 GPUs (tested on GB200/H100) — [GitHub](https://github.com/dreamzero0/dreamzero). Note that the Wan2.1 base carries its own licence.
- The project page does not discuss limitations — [project](https://dreamzero0.github.io/)

**Other 2025-2026 policy-evaluation world models**
- Google DeepMind "Evaluating Gemini Robotics Policies in a Veo World Simulator" (arXiv 2512.10675, Dec 2025): Veo fine-tuned for robot-pose action conditioning and tiled 4-camera generation on ALOHA 2. Validated against 1600+ real trials over 8 checkpoints and 5 tasks. OOD single-policy Pearson 0.86, MMRV 0.06. Also used for red-teaming physical and semantic safety via scene editing (new objects, backgrounds, distractors) — [arXiv](https://arxiv.org/abs/2512.10675); [HTML](https://arxiv.org/html/2512.10675v1)
- 1X World Model (1XWM, tech report 2025; productised Jan 2026): video WM plus a state-value head for humanoids EVE and NEO; web-video pretraining, then post-training on teleop and autonomous episodes with success labels; 4 s clips at 256² and 512². "Alignment" (success/failure prediction accuracy) rises with data; Shelf task 63.06% alone vs 71.17% with added Arcade data (~216M vs +1.46B video tokens) — [1X PDF](https://www.1x.tech/1x-world-model.pdf); [1X](https://www.1x.tech/discover/1x-world-model). World Model Lab launched June 2026 — [1X](https://www.1x.tech/discover/1x-world-model-lab); [Forbes](https://www.forbes.com/sites/johnkoetsier/2026/06/04/1x-launches-humanoid-robot-world-model-lab-you-cant-fine-tune-your-way-to-agi/)
- WorldGym (ICLR 2026): an autoregressive action-conditioned video model used as an environment with VLM rewards and Monte Carlo rollouts; preserves policy rankings across versions, sizes and checkpoints — [ML Anthology](https://mlanthology.org/iclr/2026/quevedo2026iclr-worldgym/); [code](https://github.com/world-model-eval/world-model-eval). WorldEval (arXiv 2505.19017) ranks policies and checkpoints in imagination and serves as a safety detector — [arXiv](https://arxiv.org/pdf/2505.19017)
- dWorldEval (arXiv 2604.22152) reports that WorldGym, WorldEval and Ctrl-World show weaker correlation and MMRV up to 0.039 "due to insufficient action controllability", against 0.013 for itself (self-reported comparison) — [arXiv](https://arxiv.org/pdf/2604.22152)

**Genie / GAIA-style interactive world models**
- Genie 3 (Google DeepMind, Aug 2025): real-time interactive, autoregressive general world model; text prompt to navigable world at 24 fps, 720p, consistent for "a few minutes"; tested with the SIMA agent. Not released publicly (research preview) — [DeepMind blog](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/); [TechCrunch](https://techcrunch.com/2025/08/05/deepmind-thinks-genie-3-world-model-presents-stepping-stone-towards-agi/). The claim that SIMA 2 self-improved inside Genie worlds (Nov 2025) comes from secondary coverage — [TechTimes](https://www.techtimes.com/articles/317932/20260606/deepmind-world-models-train-robots-imagined-worlds-sima-practices-inside-genie-3-model.htm) **[secondary source]**
- Wayve GAIA-3 (Dec 2025): 15B-parameter driving world model aimed at evaluation (long perturbations, safety-critical and semantic augmentations, embodiment transfer). Wayve reports that simulated tests "closely mirror" real results and that synthetic-test rejection rates fell fivefold. Closed — [Wayve](https://wayve.ai/thinking/gaia-3/); [Wayve press](https://wayve.ai/press/wayve-launches-gaia3/)

### Inferences
- The most useful released stack for an academic PhD in 2026 is NVIDIA's (Cosmos-Predict2.5 or Cosmos 3 under OpenMDW-1.1, DreamZero under Apache 2.0) plus Stanford's Ctrl-World (MIT). DeepMind (Veo, Genie 3), 1X and Wayve systems cannot be reproduced.
- Across Ctrl-World, VLAW, World-in-World and 1XWM, the same finding recurs: in-domain action-observation data, especially on-policy rollouts with failures, matters more than a bigger or prettier video backbone.

### Gaps
- UniSim's quantitative real-robot numbers and the Cosmos Policy real-ALOHA success rates were not extracted.
- The Cosmos Transfer and Reason papers were not fetched in this session; their details above come from background knowledge.
- Licences not confirmed for NWM code and weights, World-in-World, Cosmos Policy and DreamGen weights.
- I did not verify that DreamGen was accepted at CoRL 2025.

## Q2. Evidence that policies trained or improved in world models transfer to real robots; documented failure modes

### Takeaway
Real-robot evidence now exists, but it is mostly in-domain and small in scale. Imagined data or rollouts give moderate gains: +11.6 points from synthetic data in VLAW, +44.7% in Ctrl-World, and DreamGen's 37-46% on GR1. World-model evaluation reproduces policy rankings well (Pearson 0.86 in the Veo study), but absolute success rates come out biased. Training purely inside a WM with zero-shot transfer has been shown only on simple tasks (UniSim on Language Table). The recurring failure modes are weak action following, contact physics, hallucinated or vanishing objects, long-horizon drift, and reliance on human or VLM judges.

### Cited Findings
- Zero-shot transfer of an RL policy trained only in UniSim to real Language Table — [ICLR 2024 paper](https://proceedings.iclr.cc/paper_files/paper/2024/file/c4d66eae503694424123b93ac0fbaf17-Paper-Conference.pdf)
- Synthetic-data policy learning on real robots: DreamGen gives 22 new GR1 behaviours (43.2% seen environments, 28.5% unseen) and augmentation gains on three embodiments — [arXiv HTML](https://arxiv.org/html/2505.12705)
- Policy improvement from imagined rollouts: Ctrl-World +44.7% — [arXiv](https://arxiv.org/abs/2510.10125); VLAW 46.0% to 86.8% on a real Franka, with 11.6 points of that from synthetic rollouts — [arXiv HTML](https://arxiv.org/html/2602.12063)
- Evaluation fidelity: Veo reaches Pearson 0.86 and MMRV 0.06 in OOD evaluation, over 1600+ real trials — [arXiv HTML](https://arxiv.org/html/2512.10675v1); 1XWM success-prediction accuracy scales with data (63.06% to 71.17% with cross-task data) — [1X PDF](https://www.1x.tech/1x-world-model.pdf)
- **Action following / controllability:** in 1XWM "the model, unaware of that object, still moves the gripper along the commanded trajectory and closes on empty space" — [1X PDF](https://www.1x.tech/1x-world-model.pdf). Weak controllability explains the weaker evaluator correlation of WorldGym, WorldEval and Ctrl-World according to dWorldEval — [arXiv](https://arxiv.org/pdf/2604.22152). World-in-World: "controllability matters more" than visual quality — [arXiv](https://arxiv.org/abs/2510.18135)
- **Physics / contact:** Veo: "simulating contact-rich interactions, particularly with small objects, remains a challenge" — [arXiv HTML](https://arxiv.org/html/2512.10675v1). 1XWM with little data hallucinates the air-fryer tray and body as one unit — [1X PDF](https://www.1x.tech/1x-world-model.pdf). Cosmos: object permanence, contact dynamics and accurate physics remain difficult — [arXiv HTML](https://arxiv.org/html/2501.03575v3)
- **Hallucination:** in Veo, a novel object "appears spontaneously while the gripper is interacting" — [arXiv HTML](https://arxiv.org/html/2512.10675v1)
- **Long-horizon drift:** Veo: "long-horizon (e.g., 1+ minutes) multi-view consistent generation remains a key technical milestone" — [arXiv HTML](https://arxiv.org/html/2512.10675v1). Ctrl-World needs pose-conditioned memory retrieval to stay consistent past 20 s — [arXiv](https://arxiv.org/abs/2510.10125). 1X notes that model-based rollouts "degrade quickly as the imagined horizon grows" — [1X PDF](https://www.1x.tech/1x-world-model.pdf)
- **Calibration and scoring:** Veo's predicted absolute success rates are lower than real ones, and scoring used humans — [arXiv HTML](https://arxiv.org/html/2512.10675v1). DreamGen reports that automatic physics evaluators are limited — [arXiv HTML](https://arxiv.org/html/2505.12705)
- **Compute:** DreamGen used 54 h on 1500 GPUs — [arXiv HTML](https://arxiv.org/html/2505.12705); Ctrl-World takes ~10 s per step on A100 — [GitHub](https://github.com/Robert-gyj/Ctrl-World)
- **Security (new in 2026):** world models open a stealthy data-poisoning path; the authors demonstrate an end-to-end backdoor on a downstream DRL policy and a proof of concept on VLAs — [arXiv 2606.09499](https://arxiv.org/abs/2606.09499)
- WAM tutorial: "accurate visual prediction does not necessarily lead to better control"; errors in imagined subgoals propagate to the inverse dynamics — [arXiv 2607.00836](https://arxiv.org/html/2607.00836v1)

### Inferences
- The documented failure modes line up with the sim2real gap in physics simulators. Action following corresponds to the dynamics gap, hallucination to the appearance gap, and drift to compounding error. This supports framing representation learning (action-grounded, physically structured latents) as the lever for both sim2real and "WM2real".
- Evidence is concentrated on DROID/Franka, ALOHA and humanoids in lab settings, and each paper uses its own tasks. No shared real-world benchmark exists apart from RoboArena and DROID-style setups.

### Gaps
- I found no independent replication of these real-robot gains.
- No study found reports long-horizon (over 1 minute) policy training inside a WM with real transfer.

## Q3. Leading groups and newest (2026) directions

### Takeaway
NVIDIA (Cosmos, GEAR/DreamGen/DreamZero) leads in open models. Stanford (Finn, Liang: Ctrl-World, VLAW, co-author of Cosmos Policy) leads in academic policy-in-the-loop work. Google DeepMind (Veo evaluator, Genie 3, UniSim) and 1X/Wayve lead in closed industrial evaluators, and Meta FAIR in navigation and latent world models. The 2026 trend is World Action Models: one pretrained video backbone that imagines and acts, extended to omnimodal models (Cosmos 3), 3D/geometry-aware latents, and "latent futures" that avoid pixel generation.

### Cited Findings
- NVIDIA: Cosmos 1 to 2.5 to 3 (294 authors on Cosmos 3), DreamGen, DreamZero, Cosmos Policy (with Stanford) — [Cosmos 3](https://arxiv.org/abs/2606.02800); [DreamZero](https://arxiv.org/abs/2602.15922); [NVIDIA blog on WAMs](https://developer.nvidia.com/blog/pretrained-to-imagine-fine-tuned-to-act-the-rise-of-world-action-models/)
- Stanford (Finn, Liang) with Tsinghua (Jianyu Chen): Ctrl-World and VLAW — [Ctrl-World](https://arxiv.org/abs/2510.10125); [VLAW](https://arxiv.org/html/2602.12063)
- Google DeepMind: Veo World Simulator for Gemini Robotics and Genie 3 — [arXiv 2512.10675](https://arxiv.org/abs/2512.10675); [Genie 3](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)
- Meta FAIR / NYU: NWM (LeCun, Darrell) — [arXiv](https://arxiv.org/abs/2412.03572). V-JEPA 2 is listed as a latent-state world model in the 2026 WAM tutorial — [arXiv 2607.00836](https://arxiv.org/html/2607.00836v1)
- 1X: 1XWM, and a World Model Lab (June 2026) headed by Sam Sinha, formerly of Luma AI — [1X](https://www.1x.tech/discover/1x-world-model-lab); Wayve: GAIA-3 — [Wayve](https://wayve.ai/thinking/gaia-3/)
- JHU and collaborators: the World-in-World benchmark — [arXiv](https://arxiv.org/abs/2510.18135)
- WAM taxonomy (July 2026): imagine-then-execute (video plus IDM); video-feature-conditioned action; joint video-action modelling; auxiliary video loss. Named WAMs: DreamZero, Cosmos Policy, GR-2, UniVLA — [arXiv 2607.00836](https://arxiv.org/html/2607.00836v1)
- 2026 WAM wave (titles only; content not read): ImageWAM (2606.19531, "do WAMs need video generation or just image editing?"), DreamWAM (2608.04996, beyond RGB future prediction), Foresight Without Seeing: latent futures for WAMs (2608.11605), Spatially Aware WAM via geometric latent diffusion (2609.02531), StageWAM (2608.10780), Vid2WAM (2608.08558), GlanceWAM (2608.23927), ZimaBlue (2609.00188), VLA-JEPA (2602.10098), GWM-VLA (2608.07619) — [search results listing arXiv IDs](https://arxiv.org/html/2609.02531); [ImageWAM](https://arxiv.org/pdf/2606.19531); [DreamWAM](https://arxiv.org/pdf/2608.04996); [Latent futures](https://arxiv.org/pdf/2608.11605); [ZimaBlue](https://arxiv.org/pdf/2609.00188) **[titles verified via search only; claims not read]**
- Survey: "World Model for Robot Learning: A Comprehensive Survey" (arXiv 2605.00080) — [arXiv](https://arxiv.org/pdf/2605.00080) (not read)

### Inferences
- The 2026 papers point toward the PhD's topic: moving from pixel-space prediction to geometry-aware or JEPA-style latent futures (DreamWAM, latent-futures, spatial WAM, VLA-JEPA) is a representation-learning bet on robustness and transfer.
- WM co-training on real rollouts (VLAW) is effectively a real2sim2real loop with a learned simulator. It is a natural baseline or companion for a real2sim2real PhD project.

### Gaps
- The 2026 WAM papers listed by title were not read, so their results are not reported here.
- Cosmos 3 model sizes and RoboArena numbers were not extracted.
- I found no reliable source on Chinese industrial WAMs (e.g. AgiBot Genie Envisioner) in this session.

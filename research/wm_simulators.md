# Learned world models as simulators for training and evaluating robot policies (2023–2026)

Checked on **2026-09-28** for a possible re-framing of the IPB: from "3DGS digital twins" to "world models
used as simulators", under the topic *Representation learning methods for simulation-to-reality
generalization of deep learning models in physical AI*. It reuses research/world-models.md and
research/vla-wm-crowdedness.md (both from 2026-09-26) and re-verifies their entries.

**How it was verified.**
- The arXiv API (`export.arxiv.org/api/query?id_list=…`) gave title, authors, date, author comment and
  journal-ref for 30 IDs. It then returned HTTP 429, so the other 14 IDs were checked on their arXiv abstract
  pages (`citation_*` meta tags plus the comments and journal-ref cells).
- Genie 2/3, GAIA-2 and the 1X World Model come from their official blog pages (HTTP 200, dates read off
  the page). Weights and licences come from the GitHub and Hugging Face APIs and the READMEs.
- Venues come from the arXiv comment or journal-ref unless stated otherwise. Where an earlier note had a DOI
  or proceedings page, that source is named in brackets.
- **All content claims come from abstracts, READMEs and official pages, not from full texts.**
  **UNVERIFIED** marks anything not confirmed from a primary source.

---

## TL;DR

1. **The field has moved from "can a world model plan?" to "can it replace the simulator?".** Between 2023
   and 2026, learned action-conditioned video models started to be used as simulators for training and
   evaluating robot policies:
   - UniSim (ICLR 2024) trained policies purely in a learned simulator;
   - WorldGym, WorldEval, Ctrl-World and the Veo-based Gemini Robotics evaluator rank real policies;
   - DreamGen, Ctrl-World, VLAW, WMPO and WoVR generate training data or run RL inside the model;
   - Interactive World Simulator (RSS 2026) reports that policies trained on world-model data "perform
     comparably to those trained on the same amount of real-world data".
2. **The standard metric is rank correlation between world-model success and real success.** Papers report
   Pearson/Spearman correlation or ranking agreement with paired real rollouts; Veo/Gemini used 1600+ real
   evaluations. Almost no paper measures *why* the correlation fails, *which* simulation errors change the
   policy, or *what happens inside the policy* when it moves from imagined to real observations.
3. **The failure modes are named and measured, but only at the output.** They are:
   - hallucination and long-horizon error accumulation (WoVR, HaWMPO);
   - weak action following, especially for off-expert actions (WorldEval, WorldEcho/WorldSync, WorldSimProbe);
   - poor contact and object-interaction physics (WorldGym, VLAW);
   - missing failure cases in the training data (VLAW);
   - visual quality that does not predict task success (World-In-World, GigaWorld-1).

   The 2026 critiques (WorldSimProbe, arXiv:2606.15032, GigaWorld-1) all say that pixel realism is the wrong
   yardstick; what matters is action faithfulness and closed-loop consistency.
4. **The strongest single hint for a representation-learning thesis:** Zanatta, Malczyk & Alexis
   (arXiv:2606.05015, 2026) find that the world model which "dominated simulation policy evaluation failed on
   the real platform". The robustness of the world model's *representation* in cross-environment
   self-supervised validation predicted sim-to-real success. The question of which property of the learned
   representation predicts transfer is open, and it matches the student's profile.
5. **Open weights you can run on academic A100/H100 GPUs:**
   - NWM (1B, CC-BY-NC per the README);
   - DINO-WM (MIT);
   - Cosmos-Predict2/2.5 (2B model needs 32.5 GB VRAM; 14B needs 56.4 GB; NVIDIA Open Model License);
   - Ctrl-World (MIT; about 5 s per interaction step on an H100);
   - GigaWorld-1 (Apache-2.0; 1.3B and 5B models, 8×A100 for training);
   - Interactive World Simulator (one RTX 4090 at inference, per the abstract);
   - V-JEPA 2 (MIT code), DreamerV3 and TD-MPC2 (MIT).

   Genie 2/3 and GAIA-2 have no public weights. Veo is closed.
6. **Crowding.** Training foundation world models, and doing "RL of VLAs inside a world model", are crowded
   (S2 query "VLA + world model": 0 → 2 → 42 → 183 papers a year, 2023–2026, from research/vla-wm-crowdedness.md).
   Four questions are still thin:
   - *diagnosing* which world-model errors transfer into policy errors;
   - locating the gap *inside* the policy (representation-level analysis);
   - choosing the *few real data* that correct both the world model and the policy;
   - measuring transfer across scenes and tasks under a counted real-data budget.

   These are the four research questions of §4.

---

## 1. Verified key works (18)

Legend: **WM** = world model. The "Open?" column gives public weights / code and licence where checked.

| # | Work (authors, year) | ID / venue | What it shows (one line) | Open? |
|---|---|---|---|---|
| 1 | **World Models**: Ha & Schmidhuber, 2018 | arXiv:1803.10122 (interactive article; the NeurIPS 2018 version is "Recurrent World Models Facilitate Policy Evolution", **UNVERIFIED** here) | A VAE+RNN world model; a controller trained entirely "inside the dream" transfers back to the real environment (games) | code only |
| 2 | **DayDreamer**: Wu, Escontrela, Hafner, Goldberg, Abbeel, 2022 | arXiv:2206.14176; CoRL 2022 (PMLR 205) | Dreamer learns on 4 physical robots without a simulator; a quadruped walks after about 1 h | yes |
| 3 | **DreamerV3**: Hafner, Pasukonis, Ba, Lillicrap, 2023 | arXiv:2301.04104; Nature 2025 (doi:10.1038/s41586-025-08744-2, earlier note) | One fixed configuration across 150+ tasks; imagination training as a general recipe | MIT |
| 4 | **TD-MPC2**: Hansen, Su, Wang, 2023 | arXiv:2310.16828; ICLR 2024 | Scalable latent (decoder-free) world model with planning; 104 continuous-control tasks | MIT |
| 5 | **UniSim**: Yang, Du, Ghasemipour, Tompson, Kaelbling, Schuurmans, Abbeel, 2023 | arXiv:2310.06114; ICLR 2024 outstanding paper (blog.iclr.cc, earlier note) | A "universal simulator" learned from mixed internet, robot and navigation data; both high-level VLM policies and low-level RL policies trained purely in it and "deployed in the real world in zero shot" | no |
| 6 | **Genie**: Bruce et al. (25 authors), 2024; **Genie 2** (blog, 4 Dec 2024); **Genie 3** (blog, 5 Aug 2025) | arXiv:2402.15391; ICML 2024 best paper (earlier note); Genie 2/3 are DeepMind blog posts only | Interactive environments learned from unlabelled video with latent actions. Genie 2 keeps worlds consistent "up to a minute" for training agents; Genie 3 runs at 24 fps / 720p for minutes (earlier note) | no |
| 7 | **GAIA-1**: Hu et al., 2023; **GAIA-2**: Russell et al., 2025 (Wayve) | arXiv:2309.17080; arXiv:2503.20523; technical reports | Controllable (multi-view in GAIA-2) generative driving world models for synthetic data and scenario testing | no |
| 8 | **Navigation World Models (NWM)**: Bar, Zhou, Tran, Darrell, LeCun, 2024 | arXiv:2412.03572; CVPR 2025 | 1B-parameter conditional diffusion transformer on egocentric human and robot video; plans navigation by simulating trajectories and "imagines" trajectories in unfamiliar scenes from one image | HF `facebook/nwm` (gated). The HF tag says CC-BY-4.0, but the README says CC-BY-NC-4.0 for code and weights |
| 9 | **DINO-WM**: Zhou, Pan, LeCun, Pinto, 2024 | arXiv:2411.04983; ICML 2025 (PMLR 267, earlier note) | A world model that predicts frozen DINOv2 patch features (no pixel reconstruction); zero-shot planning in 6 environments | MIT (`gaoyuezhou/dino_wm`) |
| 10 | **Cosmos WFM platform**: NVIDIA, Agarwal et al. (79 authors), 2025 | arXiv:2501.03575; technical report | Open "world foundation models" (diffusion and autoregressive) plus tokenizers and a curation pipeline, meant to be post-trained into customised robot and driving world models | Code Apache-2.0; weights under the NVIDIA Open Model License. Predict2-2B Video2World needs 32.5 GB VRAM, 14B needs 56.4 GB (repo `performance.md`) |
| 11 | **DreamGen / GR00T-Dreams**: Jang, Ye, Lin, Xiang et al. (28), 2025 | arXiv:2505.12705; arXiv | Video WM + inverse-dynamics model → "neural trajectories"; a humanoid learns 22 new behaviours from teleop data of one task; DreamGen Bench scores correlate with downstream policy success | Apache-2.0 (`NVIDIA/GR00T-Dreams`) |
| 12 | **WorldGym**: Quevedo, Sharma, Sun, Suryavanshi, Liang, Yang, 2025 | arXiv:2506.00613; arXiv | Autoregressive action-conditioned WM plus VLM reward; VLA success in the WM "highly correlates" with real success and preserves rankings; "generating highly realistic object interaction remains challenging" | project site |
| 13 | **WorldEval**: Li, Zhu, Wen, Shen, Xu, 2025 | arXiv:2505.19017; arXiv | Directly feeding actions "often fails to generate action-following videos"; the Policy2Vec latent action fixes this. Ranks policies and checkpoints; claims to beat a real-to-sim baseline | project site |
| 14 | **Ctrl-World**: Guo, Shi, Chen, Finn, 2025 | arXiv:2510.10125; ICLR 2026 per the GitHub repo description (**not confirmed** from iclr.cc/OpenReview) | Multi-view WM trained on DROID (95k trajectories, 564 scenes); consistent for 20+ s; ranks π0.5 policies without real rollouts; imagined successful trajectories used for SFT give +44.7% success | MIT; README: about 10 s per step on an A100, about 5 s on an H100; experiments used 1–2 nodes of 8 A100/H100 |
| 15 | **World-in-World**: Zhang, Jiang, Dai, Lu et al. (17), 2025 | arXiv:2510.18135; ICLR 2026 oral | Closed-loop benchmark covering navigation (AR, image-goal navigation, A-EQA) and manipulation (LIBERO added 2026). Findings: (1) visual quality does not guarantee task success, controllability matters more; (2) scaling post-training on action-observation data beats a bigger video generator; (3) inference compute helps | MIT |
| 16 | **Evaluating Gemini Robotics Policies in a Veo World Simulator**: Gemini Robotics Team, 2025 | arXiv:2512.10675; tech report | A Veo-based, action-conditioned, multi-view evaluator with generative scene edits (new objects, backgrounds, distractors). Predicts the relative performance of 8 checkpoints on nominal and OOD conditions, validated by 1600+ real trials; also red-teams safety | no |
| 17 | **VLAW**: Guo, Lee, Shi, Chen, Liang, Finn, 2026 | arXiv:2602.12063; arXiv | Existing WMs "lack the physical fidelity necessary for policy improvement": they are trained on demonstrations without failures and miss small contact details. VLAW iterates real rollouts → WM fine-tuning → synthetic data → VLA; +39.2% absolute success, of which +11.6% comes from the synthetic rollouts | project site |
| 18 | **GWM (Gaussian World Model)**: Lu, Jia, Li, Chen, Wang, Tang, Huang, 2025 | arXiv:2508.17600; ICCV 2025 | Predicts future *3D Gaussian primitives* under robot actions (latent DiT + 3D VAE); used as a neural simulator for model-based RL and as a self-supervised representation | project page (repo not found under `GuanxingLu/GWM`) |

**Other verified works used below (supporting):**

| Work | ID / venue | Fact used |
|---|---|---|
| Interactive World Simulator (Wang, Syed, Wu, Zhang et al.) | arXiv:2603.08546; RSS 2026 (DOI 10.15607/RSS.2026.XXII.018, earlier note) | Consistency-model WM from "a moderate-sized robot interaction dataset"; stable for more than 10 min at 15 FPS on one RTX 4090; policies trained on WM data ≈ policies trained on the same amount of real data; strong sim-real correlation |
| IRASim (Zhu, Wu, Guo, Liu et al.) | arXiv:2406.14540; ICCV 2025 (journal-ref) | Fine-grained action-conditioned manipulation WM; policy evaluation in it "strongly correlates" with the ground-truth simulator |
| Scalable Policy Evaluation with Video World Models (Tseng, Gu, Zhang, Mao et al., NVIDIA) | arXiv:2511.11520; arXiv | Adds action conditioning to pretrained video models; studies dataset diversity, pretrained weights and "common failure cases"; reports policy ranking and value correlation |
| GigaWorld-1 / WMBench (GigaWorld Team) | arXiv:2607.02642; arXiv | 7 video WMs × 4 action encodings × 324k rollouts paired with real executions. Evaluator quality is "dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism"; Apache-2.0; 1.3B and 5B models, 8×A100 or 8×H20 for training |
| WorldSimProbe (Co, Hu, Jiao, Cheng et al.) | arXiv:2608.09298; arXiv | "Observable Simulator Contract": actions must cause the matching agent motion, and environment responses must follow from that motion. 6 open WMs, 18k instances; systematic failures in action realisation, interaction grounding and dynamics |
| Do Robotic World Models Really Follow Actions? (WorldEcho / WorldSync; Chen, Liu, Wu, Guo et al.) | arXiv:2608.24885; arXiv | WMs follow expert actions but "struggle with diverse off-expert trajectories" (they ignore the action or produce invalid video). This matters for RL, where the policy explores off-expert |
| How Should World Models Be Evaluated for Embodied Decision-Making? (Yu, Zhang, Sheng, Ren et al.) | arXiv:2606.15032; arXiv (position/survey) | An L0–L7 evidence ladder from visual plausibility to optimisation utility; names "claim/evidence mismatch"; proposes a minimum real-robot reporting set: action fidelity, closed-loop validity, ranking agreement, exploitability, calibration |
| WMPO (Zhu, Yan, Hong, Shou et al.) | arXiv:2511.09515; arXiv | On-policy GRPO for a VLA inside a *pixel* WM, chosen so imagined frames align with the VLA's web-pretrained visual features |
| WoVR (Jiang, Zhou, Jiang, Huang et al.) | arXiv:2602.13977; arXiv (project URL `wovr-corl`) | Imagined rollouts "inevitably suffer from hallucination and long-horizon error accumulation", which "mislead policy optimization". Fixes: keyframe-initialised rollouts and WM-policy co-evolution |
| HaWMPO (Chen, Liu, Li, Wang) | arXiv:2609.09941; arXiv | Learned per-chunk hallucination score down-weights unreliable imagined action chunks in GRPO; real G1 robot 67.5% → 80.0% |
| StressDream (Seo, Veer, Tian, Ding et al.) | arXiv:2606.00267; arXiv | Evaluation on "nominal imaginations" misses rare high-impact outcomes; steers diffusion noise toward plausible failures |
| Zanatta, Malczyk, Alexis | arXiv:2606.05015; arXiv | DreamerV3 WMs for quadrotor navigation. Cross-environment self-supervised robustness predicts real transfer; "the model that dominated simulation policy evaluation failed on the real platform"; discrete latent size and sequence length matter most |
| LWM for navigation (Wang, Gao, Shen) | arXiv:2608.26190; ECCV 2026 spotlight | Latent "compatibility" WM, no pixel reconstruction; RL "entirely within the world model" from unlabelled video; real-robot navigation gains |
| NavWM (Mei, Guo, Yu, Zhao et al.) | arXiv:2606.24101; ECCV 2026 | Unified navigation WM (latent tokens, multimodal trajectory proposals, generative foresight for closed-loop planning) |
| Dreamer 4 (Hafner, Yan, Lillicrap) | arXiv:2509.24527; arXiv | RL inside a WM from offline data only (Minecraft diamonds); action conditioning from "a small amount" of labelled data |
| V-JEPA 2 (Assran, Bardes, Fan, Garrido et al.) | arXiv:2506.09985; arXiv | Latent WM post-trained on less than 62 h of robot video; zero-shot Franka pick-and-place (earlier note); code MIT |
| Cosmos Policy (Kim, Gao, Lin, Lin et al.) | arXiv:2601.16163; arXiv | Cosmos-Predict2 fine-tuned into a visuomotor policy and planner |
| GigaWorld-0 (GigaWorld Team) | arXiv:2511.19861; arXiv | WM data engine: video generation plus 3DGS reconstruction and system identification for VLA training |
| Genie Envisioner (Liao, Zhou, Huang, Yang et al.) | arXiv:2508.05635; arXiv | Unified WM platform for manipulation: video-diffusion world model, action decoder and neural simulator |
| 1X World Model (1X, blog 30 Aug 2024) + challenge report (Mereu et al.) | 1x.tech/discover/1x-world-model; arXiv:2510.07092 | 1X motivates the WM as a *policy evaluator* for multi-task home robots; open humanoid dataset and challenge (`1x-technologies/1xgpt`, Apache-2.0). The winning entry fine-tuned Wan-2.2 5B with LoRA (23.0 dB PSNR) |
| PolaRiS (Jain, Zhang, Arora, Chen et al.) | arXiv:2512.16881; arXiv | Scalable *real-to-sim* (reconstruction) evaluation of generalist policies. It is the reconstruction-based comparator to WM evaluators, already cited in content/06 |
| Surveys | arXiv:2609.16697 (Plausible → Controllable → Actionable, Sep 2026); arXiv:2605.00080 (World Model for Robot Learning) | Use one in §6 for the taxonomy |

## 2. How world models are used as simulators (the three roles)

1. **Training in imagination (policy optimisation).**
   - Latent: Dreamer line, TD-MPC2, DINO-WM planning, LWM-nav.
   - Pixel: UniSim, WMPO, WoVR, HaWMPO, Ctrl-World SFT, VLAW.
   - 3D: GWM.

   The latent line is cheap and data-efficient but task-specific. The pixel line reuses web-pretrained video
   models and matches the VLA's visual features (WMPO's argument) but hallucinates.
2. **Data generation (offline synthetic demonstrations).** DreamGen (video WM plus an IDM for pseudo-actions),
   Interactive World Simulator, GigaWorld-0 and Cosmos-Transfer (appearance transfer from sim to real). The
   policy never interacts with the WM in a closed loop, which avoids compounding error but inherits label
   noise from the IDM or latent actions.
3. **Policy evaluation (a proxy for real rollouts).** IRASim, WorldGym, WorldEval, dWorldEval (2604.22152),
   Ctrl-World, the NVIDIA video-WM evaluator, Veo/Gemini, GigaWorld-1 and the 1X World Model. For
   navigation, NWM ranks trajectories from an external policy, and World-in-World scores closed-loop
   navigation.

## 3. Known failure modes and what papers actually measure

| Failure mode | Where it is reported | What is measured |
|---|---|---|
| **Hallucination / long-horizon error accumulation** (compounding error) | WoVR; HaWMPO; Interactive World Sim ("existing approaches … struggle to capture physically consistent interactions over long horizons") | Rollout stability over horizon; downstream success on LIBERO and real robots; a learned per-chunk hallucination score (HaWMPO) |
| **Weak action following / controllability** | WorldEval (raw actions → non-following videos); WorldEcho (off-expert actions ignored); WorldSimProbe; World-in-World ("controllability matters more") | SE(3) trajectory alignment and visual integrity under off-expert actions; action-to-motion correspondence; closed-loop task success |
| **Physics / contact inconsistency** | WorldGym ("realistic object interaction remains challenging"); VLAW ("small yet critical physical details in contact-rich manipulation"); WorldSimProbe (interaction grounding, false interactions, dynamics) | Contact and interaction probes; primitive-level dynamics; mostly qualitative in the evaluator papers |
| **Missing failures / coverage bias** (trained on demonstrations, so the WM is optimistic) | VLAW; StressDream (nominal imagination misses high-impact outcomes) | Gain from adding real failure rollouts; rate of steered failure discovery |
| **Visual quality ≠ utility** | World-in-World; GigaWorld-1; position 2606.15032 | Correlation of FVD/PSNR-type scores with closed-loop success, which is weak |
| **WM-to-real gap of the evaluator** | WorldGym, WorldEval, Ctrl-World, IRASim, Veo/Gemini, Interactive World Sim, NVIDIA video-WM evaluator, GigaWorld-1 | Pearson/Spearman correlation or MMRV-style ranking agreement between WM success and paired real success; policy ranking across checkpoints |
| **WM-to-real gap of the trained policy** | UniSim (zero-shot real deployment), DreamGen, Interactive World Sim (WM data ≈ real data), VLAW, WMPO/WoVR/HaWMPO, Zanatta et al. | Real success after training on WM data, compared with real-data training at equal volume (Interactive World Sim) |
| **Reward error** | WorldGym, World-Env and others use a VLM judge on generated video | Rarely measured separately; the reward and the dynamics errors are confounded |

**What is *not* measured (the gap this thesis can fill).**
- (a) Attribution: which *type* of WM error (action misfollowing, contact physics, appearance, horizon drift)
  causes which *policy* error.
- (b) Representation-level analysis of the policy on imagined vs. real observations. We found no paper that
  probes the policy's internal features across the WM-to-real shift; FARM (2609.11445) probes the *WM's*
  internals for failure prediction, not the policy's.
- (c) Calibration of WM-based evaluation per scene and per task, and how it degrades out of distribution;
  only Veo/Gemini tests OOD axes, with a closed model.
- (d) A counted real-data budget that is shared between correcting the WM and correcting the policy. VLAW
  co-improves both but with unselected rollouts and no budget curve.

## 4. Open problems mapped to the research questions

**OP1: Which simulation errors hurt (RQ "which errors of the simulation harm").**
- The 2026 diagnostics (WorldSimProbe, WorldEcho, GigaWorld-1) score the *WM*.
- The evaluator papers score *end correlation*.
- None does a controlled intervention: inject or remove one error type (action lag, contact error, texture
  drift, horizon length) in a WM or a WM-like perturbation of a reference simulator, and measure the change
  in real (or held-out simulator) policy success and ranking.

Feasible design: use a physics simulator (ManiSkill/LIBERO; Habitat for navigation) as the "reality", train
an open WM on its data (DINO-WM, Ctrl-World, Cosmos-Predict2-2B, GigaWorld-1 Nano), then perturb it
factor by factor. This gives an error-sensitivity profile per factor, which none of the verified works reports.

**OP2: Where inside the policy the gap arises (RQ "where inside the policy").**
- WMPO argues that pixel WMs suit VLAs because they match the VLA's pretrained visual features.
- Zanatta et al. show that representation robustness, not simulated return, predicts real transfer.
- No verified work locates the WM-to-real shift layer by layer in the *policy*: vision encoder vs. fusion vs.
  action head, measured with probes, CKA or similar, on paired imagined and real observations.
- A representation-level diagnostic that *predicts* real success from imagined rollouts is open, in the
  spirit of FARM but applied to the policy. It could also serve as an alignment loss.

**OP3: Which few real data correct both the WM and the policy (RQ "which few real data").**
- VLAW corrects the WM with real rollouts, but they are not selected.
- TwinRL (research/vla-wm-crowdedness.md) selects failure-prone configurations for the policy only.
- StressDream finds failures inside the WM but does not spend real data.
- HaWMPO estimates unreliability but does not query reality.
- Open question: an acquisition rule that picks real rollouts by joint WM uncertainty and policy
  sensitivity, reported as budget curves (real minutes or trials against real success), compared with random
  real data and with real-only fine-tuning.

**OP4: Transfer across scenes and tasks (RQ "transfer").**
- Ctrl-World (new scenes and camera placements), Veo/Gemini (OOD edits), NWM (unfamiliar environments from
  one image) and DreamGen (new behaviours and environments) all claim generalisation, but on their own
  protocols.
- World-in-World and GigaWorld-1 give shared benchmarks but measure WM quality, not the transfer of *policies
  trained* in the WM to new real scenes.
- Open: does WM-trained policy transfer to a new scene or task degrade more slowly than a policy trained in
  a reconstruction twin or in a generic simulator, and does a small amount of scene-specific WM post-training
  (World-in-World's scaling-law finding) close the gap? This covers navigation *and* manipulation with one
  protocol, which World-in-World supports.

**OP5 (cross-cutting): Evaluation-validity standards.** Position 2606.15032 and GigaWorld-1 show that the
field has no agreed minimum evidence for "this WM is a valid simulator". A thesis contribution can be a
small reporting protocol: action fidelity, ranking agreement with CIs, calibration per OOD axis and
exploitability by RL. Every experiment above would be reported with it.

## 5. Feasibility on academic GPUs (A100/H100)

| Model | Size / need (source) | Licence | Fit for a PhD |
|---|---|---|---|
| DINO-WM | small; trains on frozen DINOv2 features (README) | MIT | Yes: fastest to iterate; latent-space planning |
| NWM | 1B CDiT; full training used 8 nodes × 8 GPUs; single-GPU debug and inference; CEM planning on 8 GPUs (README) | CC-BY-NC-4.0 (README) / CC-BY-4.0 (HF tag); gated | Fine-tune or use as is; do not retrain |
| Cosmos-Predict2 / 2.5 (2B, 14B) | 2B Video2World 32.5 GB, 14B 56.4 GB VRAM; about 80 s per 2B generation on an H100 PCIe (performance.md) | Code Apache-2.0; weights NVIDIA Open Model License | Post-training the 2B model on 1–8 H100s is realistic; slow for RL rollouts |
| Ctrl-World | about 5 s per interaction step on an H100; experiments on 1–2 × 8 A100/H100 (README) | MIT | Yes, for DROID-like manipulation; π0.5 integration |
| GigaWorld-1 (Nano 1.3B, Pro 5B) | Training 8 × A100/H20; "few thousand steps on 8 GPUs … within one day" for new domains (README) | Apache-2.0 | Yes, and built for policy evaluation |
| Interactive World Simulator | Inference on one RTX 4090 at 15 FPS (abstract) | code availability not checked | Yes, if released |
| V-JEPA 2 (-AC) | ViT-g encoder; AC post-training on less than 62 h of video (earlier note) | MIT (code) | Frozen features for representation analysis |
| DreamerV3 / TD-MPC2 | a single GPU | MIT | Latent baselines, also for navigation (Zanatta et al.) |
| World-in-World | benchmark harness (AR, image-goal navigation, A-EQA, LIBERO manipulation) | MIT | Shared closed-loop protocol for navigation and manipulation |
| Genie 2/3, GAIA-2, Veo, UniSim | not released | — | Cite only |

Budget sketch (our estimate, not measured): perturbation studies and LoRA post-training of a 2B-scale WM plus
policy RL/SFT in the WM fit the ~20–25k H100-hour envelope already estimated in
research/vla-wm-crowdedness.md §4, since most of the cost there was policy RL and WM adaptation.

## 6. Notes for re-framing the plan (not applied; this file edits nothing else)

- The 3DGS twin can stay as **one kind of learned simulator** (reconstruction) next to the WM (generative),
  and GWM and GigaWorld-0 sit between the two. Or it can become the *reference / ground-truth proxy* against which
  WM errors are measured (OP1).
- The strongest novelty is the combination of OP1 and OP2: *error attribution from the simulator into the
  policy's representation*. It is representation learning proper, it runs on open models, and no verified
  work does it.
- Scooping risk: medium-high on OP3 (VLAW, TwinRL, HaWMPO are each one step away); lower on OP1/OP2.
- Items to check before citing:
  - Ctrl-World at ICLR 2026 (only the GitHub description);
  - the NWM licence mismatch between HF and the README;
  - the NeurIPS 2018 version of Ha & Schmidhuber;
  - WoVR's venue (the project URL suggests CoRL; **UNVERIFIED**).

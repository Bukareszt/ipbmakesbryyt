# NVIDIA simulation and world-model stack for robot learning (verified 2026-09-28)

## TL;DR

- **Isaac Sim still does not run on A100/H100.** The current requirements page (Isaac Sim 6.0/6.1) says: "GPUs without RT Cores (A100, H100) are not supported." The minimum is an RTX 4080 with 16 GB. The earlier claim in `reports/Wykonalność pytań badawczych IPB.md` is **confirmed** for Isaac Sim.
- **This is new since the report: Isaac Lab 3.0 no longer needs Isaac Sim.** Isaac Lab 3.0 (beta in March 2026, v3.0.0-EA on 16 Sep 2026) adds a "kit-less" mode built on the Newton physics engine (Warp / MuJoCo-Warp) and a Warp-based camera renderer. NVIDIA says this decoupling lets Isaac Lab run on "L40s/H100/H200/B200". The claim "the NVIDIA path is out on the cluster" is therefore **outdated for Isaac Lab (kit-less)** but **still true for Isaac Sim / RTX rendering / PhysX-in-Kit**. Limits of kit-less mode: the Newton Warp renderer outputs only RGB and depth (segmentation and normals need Isaac RTX), and nobody has tested it on Lem yet.
- **Cosmos runs natively on H100.** Transfer2.5 needs Hopper or newer with at least 80 GB. Lem's H100 96 GB meet that. Cosmos 3 (1 Jun 2026, arXiv:2606.02800) comes in Nano (16B total) and Super (64B). Weights up to 2.5 use the **NVIDIA Open Model License**; Cosmos 3 uses **OpenMDW-1.1** (Linux Foundation). Both allow commercial use.
- **Evidence that world-model data transfers to real robots is real but thin, and mostly NVIDIA's own.** Peer-reviewed: DreamGen (CoRL 2025), where real-robot success went from 37→46.4% (GR1), 23→37% (Franka) and 21→45.5% (SO-100). Non-peer-reviewed: the Cosmos Cookbook X-Mobility navigation recipe (54→91% success on a real Carter robot, a tutorial with no trial counts), and Wang et al. 2026 (arXiv:2606.31101), where a Cosmos Policy trained only on synthetic data reached 35% zero-shot on a Franka. I found no independent, peer-reviewed controlled study of "Isaac render → Cosmos Transfer → policy → real robot" for navigation. That is a gap the thesis could fill.
- **Suggested split:** world-model generation, Cosmos Transfer augmentation, policy training and kit-less Isaac Lab RL on Lem H100s. Isaac Sim, RTX sensors, NuRec 3DGS scenes and scene authoring on an RTX workstation (at least an RTX 4080, ideally an RTX PRO 6000 with 96 GB, which also runs Cosmos 3 Nano).

## 1. Isaac Sim and Isaac Lab

**Isaac Sim** is NVIDIA's robot simulator, built on Omniverse Kit. It uses PhysX for physics, RTX ray-traced rendering for cameras, lidar and other sensors, and OpenUSD as the scene format.
- The source code is Apache 2.0 on GitHub (https://github.com/isaac-sim/IsaacSim). Running it also needs Omniverse Kit and assets, which have their own licence terms. It is free for internal R&D; redistributing it or offering it as a service needs a separate licence (License FAQ: https://docs.isaacsim.omniverse.nvidia.com/latest/common/license-faq.html).
- Requirements (https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html, Isaac Sim 6.0/6.1):
  - "GPUs without RT Cores (A100, H100) are not supported."
  - Minimum GPU: RTX 4080 with 16 GB. Linux driver 595.58.03.
  - Ubuntu 22.04/24.04 or Windows 11.
- Isaac Sim 6.0.0 reached general availability in June 2026. It includes NuRec support through Kit 110 (https://radiancefields.com/nvidia-s-isaac-sim-6.0-ships-with-nurec-gaussian-splatting; secondary source).

**Isaac Lab** is a robot-learning framework (RL and imitation learning) that succeeds Orbit and Isaac Gym. It is BSD-3 licensed; the `isaaclab_mimic` extension is Apache 2.0 (https://github.com/isaac-sim/IsaacLab).
- **Papers:**
  - Orbit: Mittal et al., IEEE RA-L 8(6), 2023, arXiv:2301.04195, DOI 10.1109/LRA.2023.3270034.
  - Isaac Lab: Mittal, Roth, Tigue et al. (about 110 authors), arXiv:2511.04831 (6 Nov 2025), "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning". This is an arXiv technical report with no venue listed. It describes Isaac Lab as built on Isaac Sim with PhysX, RTX rendering and USD, and mentions the planned integration of Newton.
- **Isaac Lab 3.0.** Releases via the GitHub API: v3.0.0-beta on 17 Mar 2026, beta2 on 17 Jun 2026, v3.0.0-EA on 16 Sep 2026. It targets Isaac Sim 6.1, Python 3.12 and PyTorch 2.11 (https://github.com/isaac-sim/IsaacLab/releases). New in 3.0:
  - **Pluggable physics.** PhysX or Newton. Newton is built on Warp, uses MuJoCo-Warp as its main solver, and adds XPBD, Featherstone, VBD and MPM.
  - **Pluggable renderers:**
    - Isaac RTX, which needs the full Isaac Sim stack;
    - OVRTX and Newton RTX, which are kit-less RTX paths;
    - Newton Warp camera rendering, which is kit-less and outputs RGB and depth only (https://docs.robotsfan.com/isaaclab_official/develop/source/overview/core-concepts/renderers.html, a mirror of the official docs).
  - "Kit-less Newton workflows do not require Isaac Sim". Full PhysX/RTX/ROS workflows still do.
  - **GPU statement.** In Discussion #4339 (6 Jan 2026, https://github.com/isaac-sim/IsaacLab/discussions/4339), NVIDIA wrote: "by decoupling from RTX rendering requirements, you will be able to run Isaac Lab on a mix of the latest NVIDIA compute GPUs (ex: L40s/H100/H200/B200)".
  - **My inference (not verified):** the RTX-based renderers (Isaac RTX, OVRTX, Newton RTX) probably still need RT cores. On H100, plan for Newton physics with the Warp renderer, or state-only RL.
- **Camera throughput.** NVIDIA's guidance for the RTX tiled renderer is about 512 cameras on an RTX 4090-class GPU (Isaac Lab tiled-rendering docs).

## 2. Cosmos world foundation models

| Release | Paper | Contents |
|---|---|---|
| Cosmos 1 (Jan 2025) | NVIDIA; Agarwal, N., et al., arXiv:2501.03575 (v3, Jul 2025), "Cosmos World Foundation Model Platform for Physical AI" | Video curation pipeline, tokenizers, diffusion and autoregressive WFMs (Predict1), post-training examples (robotics, driving, camera control). Open weights. |
| Cosmos-Transfer1 (Mar 2025) | NVIDIA, arXiv:2503.14492, "Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control" | A ControlNet-style model on top of Predict1, conditioned on segmentation, depth, edge and blur with spatially adaptive weights. Explicitly aimed at robotics Sim2Real and data enrichment for autonomous driving. |
| Cosmos-Reason1 (Mar 2025) | NVIDIA, arXiv:2503.15558 | Physical-reasoning VLMs, 7B and 56B, trained with SFT then RL. Later came Cosmos-Reason2 (a 2B version is used in GR00T N1.6). |
| Predict2.5 / Transfer2.5 (Oct 2025) | NVIDIA, arXiv:2511.00062, "World Simulation with Video Foundation Models for Physical AI" | Predict2.5 is flow-based, unifies Text/Image/Video2World, comes in 2B and 14B, and was trained on 200M clips. Transfer2.5 is 3.5× smaller than Transfer1 and targets "Sim2Real and Real2Real". Released under the NVIDIA Open Model License. Robot checkpoints include multiview robot control (depth, edge, blur, seg) and action-conditioned Predict2.5, plus LIBERO/RoboCasa policy checkpoints. |
| Cosmos Policy (Jan 2026) | Kim, M. J., et al., arXiv:2601.16163 | Post-trains Predict2 into a policy that outputs actions, future frames and values as latent frames. Reaches 98.5% on LIBERO and 67.1% on RoboCasa. |
| Cosmos 3 (1 Jun 2026) | NVIDIA, arXiv:2606.02800, "Cosmos 3: Omnimodal World Models for Physical AI" | A mixture-of-transformers with a reasoner tower and a diffusion generator tower, handling text, image, video, audio and action. Nano (16B) is aimed at workstations such as the RTX PRO 6000; Super (64B) at Hopper/Blackwell datacentres. It supports forward/inverse dynamics and policy post-training. The Transfer2.5 repo says it is "no longer under active development" and points users to Cosmos 3. Licence: OpenMDW-1.1 (Hugging Face nvidia/Cosmos3-Nano). |

**Licence.**
- NVIDIA Open Model License (https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/, last modified 24 Oct 2025): commercial use is allowed and you own your derivative models.
- It has three conditions to note:
  - rights terminate if you bypass or disable safety guardrails without a substantially similar replacement;
  - rights terminate if you bring IP litigation claiming the model infringes;
  - Cosmos redistributions must say "Built on NVIDIA Cosmos".
- Code is Apache 2.0.
- Cosmos 3 moved to OpenMDW-1.1.

**GPU requirements.**
- The Predict2.5 and Transfer2.5 repos: "Ampere architecture (RTX 30 Series, A100) or newer", Linux, driver ≥570.124.06 / CUDA 12.8.
- The NIM support matrix (https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html):
  - Transfer2.5-2B needs Hopper or newer with ≥80 GB. It is validated on 1–8× H100 80GB and on RTX PRO 6000 Blackwell.
  - Predict2.5-2B needs compute capability ≥8.9.
  - The Cosmos3 Nano generator needs ≥79 GiB per device, on Hopper or newer.
  - The Cosmos3 Super generator needs ≥121 GiB (FP8), so on H100 it runs only with tensor parallelism across 2–4 GPUs.
- **Consequence for us:** Cosmos does not need RT cores, so it fits H100 96 GB nodes well. A 24 GB RTX 4090 is too small for Transfer2.5 or Cosmos 3.

**How Cosmos is used with simulation (NVIDIA workflows):**
- **Cosmos Transfer as a sim→photoreal "shader".**
  1. Render depth, segmentation and edges from Isaac Sim/Lab.
  2. Transfer generates photoreal video that keeps the same geometry and trajectories, so the labels and actions from simulation stay valid.
  3. Vary the text prompt to change lighting, materials and weather.
  - Recipes:
    - GR00T-Mimic + Transfer1 (https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/transfer1/gr00t-mimic/inference.html);
    - X-Mobility navigation (https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/transfer1/inference-x-mobility/inference.html);
    - CARLA with Transfer2.5.
- **GR00T Blueprint.** Isaac GR00T-Mimic expands a few demonstrations in Isaac Lab, then GR00T-Gen or Cosmos Transfer diversifies them. NVIDIA reports 780K trajectories generated in 11 h, and that combining synthetic with real data improved GR00T N1 by 40% over real data alone (NVIDIA blog, not peer-reviewed).
- **DreamGen / GR00T-Dreams.** A world model is fine-tuned on the target robot, generates videos of new tasks, and an IDM or latent-action model recovers pseudo-actions ("neural trajectories"). This is covered in the next section.

## 3. GR00T N1 / N1.5 / N1.6 / N1.7 and DreamGen

- **GR00T N1.** NVIDIA; Bjorck, J., et al., arXiv:2503.14734 (Mar 2025), "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots".
  - Dual-system VLA: an Eagle VLM ("System 2") plus a diffusion-transformer action head ("System 1").
  - Trained on real robot data, human video, simulation data and neural (world-model-generated) trajectories.
  - The 2B checkpoint is open. This is the only arXiv paper in the GR00T N series.
- **GR00T N1.5** (11 Jun 2025, https://research.nvidia.com/labs/gear/gr00t-n1_5/). There is **no arXiv paper**.
  - 3B parameters, with a frozen Eagle 2.5 VLM and a FLARE loss.
  - DreamGen data led to 38.3% success on 12 new DreamGen tasks, against 13.1% for N1.
- **GR00T N1.6 and N1.7.**
  - N1.6 uses Cosmos-Reason-2B. Its sim-to-real workflow is on NVIDIA's blog (8 Jan 2026); it combines Isaac Lab whole-body RL with COMPASS synthetic navigation data and reports "zero-shot sim-to-real transfer" but gives no numbers.
  - N1.7 is the current version on https://github.com/NVIDIA/Isaac-GR00T.
- **DreamGen.** Jang, J., Ye, S., et al., arXiv:2505.12705, CoRL 2025 (PMLR v305, https://proceedings.mlr.press/v305/jang25a.html). The pipeline has four steps:
  1. fine-tune an image-to-video model with LoRA (main model WAN2.1; Cosmos, Hunyuan and CogVideoX compared);
  2. generate rollouts;
  3. label actions with an IDM or latent-action model;
  4. train a policy (GR00T N1).
  - **Real robots:** GR1 37→46.4%, Franka 23→37%, SO-100 21→45.5%.
  - **New behaviours:** 22 new behaviours from pick-and-place teleoperation data only. Success was 43.2% in seen environments and 28.5% in unseen ones; the N1 baseline scored 0%.
  - **Simulation:** RoboCasa policy performance improved log-linearly with synthetic data, up to 333× the original demonstrations.
  - "GR00T-Dreams" is NVIDIA's blueprint name for this pipeline.

## 4. NuRec (Omniverse neural reconstruction)

- **What it is.** Omniverse NuRec is a set of 3D Gaussian splatting libraries. They reconstruct camera or lidar captures into OpenUSD (USDZ) scenes that load into Isaac Sim as ordinary USD assets (https://developer.nvidia.com/omniverse/nurec). It is also integrated with CARLA and AlpaSim.
- **Reconstruction backend.** The backend is 3DGRUT / 3DGUT: Wu, Q., et al., "3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting", CVPR 2025, arXiv:2412.12507, code at https://github.com/nv-tlabs/3dgrut. The smartphone tutorial runs COLMAP → 3DGUT → USDZ → Isaac Sim (https://developer.nvidia.com/blog/reconstruct-a-scene-in-nvidia-isaac-sim-using-only-a-smartphone/).
- **Physics.** You add collisions yourself, for example a ground plane or proxy meshes. Nova Carter navigation examples exist (https://docs.isaacsim.omniverse.nvidia.com/5.1.0/assets/usd_assets_nurec.html).
- **Hardware.** Rendering goes through Isaac Sim's RTX path, so NuRec in Isaac Sim needs an RTX GPU and cannot run on H100 nodes. Training the 3DGUT reconstruction itself is plain CUDA and runs on H100.

## 5. Published sim-to-real results with world-model or Cosmos data (status)

| Work | Status | Result |
|---|---|---|
| DreamGen, arXiv:2505.12705 | CoRL 2025 (peer-reviewed) | Real-robot gains on 3 embodiments (see §3). This is real-to-real augmentation with a world model; it is not sim-to-real. |
| X-Mobility + Cosmos Transfer1 (Cookbook, 27 Oct 2025) | Tutorial | Real Carter robot, navigation: 54%→91% success, trip time 58.1→25.5 s. Training data was 50% original + 50% Cosmos-augmented (520K frames), trained on 8×H100. No trial counts are given. |
| GR00T-Mimic / Blueprint | NVIDIA blog | +40% for GR00T N1 with synthetic plus real data. |
| Wang, Z., et al., arXiv:2606.31101 (30 Jun 2026) | arXiv preprint | Cosmos Policy trained on about 800 synthetic demonstrations per task and no real data reached 35% average zero-shot on a Franka (lift, drawer, pick-and-place). |
| EMMA, arXiv:2509.22407 | arXiv preprint | Generative visual transfer for real manipulation, reporting a relative gain of more than 92% over training on real data alone. I could not confirm a Cosmos-Transfer comparison in the abstract. |

**Gap:** there is no independent, controlled, peer-reviewed study (with trial counts and ablations of the control modality) of Cosmos-Transfer-augmented *simulation* data for sim-to-real, especially for navigation.

## 6. Key citations

(On arXiv, the author list of the four NVIDIA papers starts with the collective author "NVIDIA", followed by the named authors in alphabetical order. The names are checked against the arXiv abstract pages.)

1. Mittal, M., et al. (2025). Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning. arXiv:2511.04831.
2. Mittal, M., et al. (2023). Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments. IEEE RA-L 8(6). arXiv:2301.04195, DOI:10.1109/LRA.2023.3270034.
3. NVIDIA; Agarwal, N., et al. (2025). Cosmos World Foundation Model Platform for Physical AI. arXiv:2501.03575.
4. NVIDIA; Alhaija, H. A., et al. (2025). Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control. arXiv:2503.14492.
5. NVIDIA; Ali, A., et al. (2025). World Simulation with Video Foundation Models for Physical AI [Cosmos-Predict2.5/Transfer2.5]. arXiv:2511.00062.
6. NVIDIA; Bjorck, J., et al. (2025). GR00T N1: An Open Foundation Model for Generalist Humanoid Robots. arXiv:2503.14734.
7. Jang, J., Ye, S., et al. (2025). DreamGen: Unlocking Generalization in Robot Learning through Video World Models. CoRL 2025 (PMLR 305). arXiv:2505.12705.
8. NVIDIA (2026). Cosmos 3: Omnimodal World Models for Physical AI. arXiv:2606.02800.
9. Wu, Q., et al. (2025). 3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting. CVPR 2025. arXiv:2412.12507.

## 7. How a PhD student with Lem H100s plus an RTX workstation could use this stack

Split the work by hardware. The **RTX workstation** (at least an RTX 4080 16 GB for Isaac Sim; an RTX PRO 6000 96 GB would also run Cosmos 3 Nano and Transfer2.5 locally) is used for:
- authoring scenes in Isaac Sim 6.x;
- importing NuRec/3DGUT reconstructions of the real lab or corridor;
- rendering small sets of RTX sensor data (RGB, depth, segmentation, lidar) that serve as the control inputs for Cosmos Transfer.

The **Lem H100 96 GB nodes**, which have no RT cores but meet Cosmos's "Hopper, ≥80 GB" requirement, are used for:
- training the 3DGUT reconstructions;
- mass generation with Cosmos Transfer2.5 or Cosmos 3 (sim render → many photoreal appearance variants that keep geometry and actions);
- DreamGen-style neural trajectories (post-training Predict2.5 or Cosmos 3 on the robot's own data, plus IDM labelling);
- training the policy (e.g. GR00T N1.x or Cosmos Policy fine-tuning, or the thesis's own navigation and manipulation policies);
- large-scale RL in Isaac Lab 3.0 kit-less mode (Newton physics plus the Warp RGB-D renderer).

Check in the first week of cluster access:
- that an Isaac Lab 3.0 kit-less container runs under Slurm/Apptainer on Lem;
- the NVIDIA driver version on Lem, since Isaac Sim 6 needs 595.x and Cosmos needs ≥570.

Keep ManiSkill3/Habitat as the fallback. The licences (BSD-3/Apache for the code, Open Model License or OpenMDW for the weights) allow academic publication of derived models, provided the Cosmos guardrails are not removed and the "Built on NVIDIA Cosmos" attribution is kept.

# Technology stack and compute for a PhD on world models and sim-to-real generalization (state as of late September 2026)

Scope: datasets, simulators, released models (licences, compute), Polish academic compute (WCSS, PLGrid/Cyfronet), real robots (quadrupeds, humanoids) and what can be verified about PWr's "Wojtek" and a K46 humanoid. Research date: 2026-09-29. Anything marked **[UNVERIFIED]** could not be confirmed from a primary source.

## 1. Datasets: BridgeData V2, SIMPLER, RECON, SCAND, SACSoN, DROID, Open X-Embodiment

### Takeaway
All the core datasets are openly downloadable under permissive licences: CC BY 4.0 for BridgeData V2 and OXE, MIT for RECON and SACSoN. BridgeData V2 (WidowX 250, 24 environments, mostly toy kitchens, plus toy sinks and tabletops) pairs with SIMPLER, which rebuilds 4 Bridge WidowX tasks in simulation. SIMPLER depends on SAPIEN/Vulkan rendering, and Vulkan on headless H100 nodes has an open, unresolved bug report.

### Cited Findings
**BridgeData V2**
- 60,096 trajectories: 50,365 teleoperated demonstrations plus 9,731 rollouts of a scripted pick-and-place policy. 24 environments in 4 categories, 13 skills — [BridgeData V2 project page](https://rail-berkeley.github.io/bridgedata/)
- Robot: WidowX 250 6-DOF arm, several camera views, 5 Hz control, trajectories average 38 timesteps. Images stored as 640x480 JPEGs — [BridgeData V2](https://rail-berkeley.github.io/bridgedata/)
- Environments: 7 toy kitchens are the main source, plus various tabletops, standalone toy sinks, a toy washing machine and other spaces. Skills include pick-and-place, pushing, sweeping, opening drawers and doors, stacking blocks, folding cloth and sweeping granular material — [BridgeData V2](https://rail-berkeley.github.io/bridgedata/)
- Licence: "All data is provided under the Creative Commons Attribution 4.0 International License" — [BridgeData V2](https://rail-berkeley.github.io/bridgedata/)
- Also on TensorFlow Datasets (`bridge`) — [TFDS bridge](https://www.tensorflow.org/datasets/catalog/bridge); code and models at [rail-berkeley/bridge_data_v2](https://github.com/rail-berkeley/bridge_data_v2)

**SIMPLER (SimplerEnv)**
- The Bridge/WidowX part has 4 tasks: put the spoon on the towel, put the carrot on the plate, stack the cube, put the eggplant in the basket — [SimplerEnv GitHub](https://github.com/simpler-env/SimplerEnv)
- Two evaluation modes. "Visual Matching" overlays real images onto the simulation background. "Variant Aggregation" averages results over environment variants — [SimplerEnv](https://github.com/simpler-env/SimplerEnv)
- MIT licence. Requires an NVIDIA GPU ("SAPIEN requires a GPU"), CUDA >=11.8 and <13, and the Vulkan runtime. A ManiSkill3 version (branch `maniskill3`) with GPU parallelism is "10-15x faster" than the ManiSkill2 version — [SimplerEnv](https://github.com/simpler-env/SimplerEnv)
- **Known H100 issue**: SAPIEN issue #250 (24 June 2025), "Headless rendering on an H100". Vulkan does not see the H100 and falls back to llvmpipe (CPU). Errors include `vkCreateDevice: Failed to validate extensions`, `ErrorExtensionNotPresent` and `VK_KHR_external_semaphore_fd not supported`. The cause is the ICD pointing at `libGLX_nvidia.so.0`. Switching it to libEGL and trying drivers 550 and 570 did not help. **No fix posted in the thread** — [SAPIEN issue #250](https://github.com/haosulab/SAPIEN/issues/250)

**RECON**
- About 50 GB main package plus about 30 MB of helper code, downloaded from Berkeley RAIL servers. Robot: Clearpath Jackal. Licence: **MIT** — [RECON dataset page](https://sites.google.com/view/recon-robot/dataset)

**SCAND**
- 8.7 hours, 25 miles, 138 trajectories collected over 15 days. Robots: Clearpath Jackal (wheeled) and Boston Dynamics Spot (legged). Sensors: 5 Spot body cameras, Azure Kinect RGB, Velodyne Puck lidar. Hosted on the Texas Data Repository (doi:10.18738/T8/0PRYRH) — [SCAND page, UT Austin](https://www.cs.utexas.edu/~xiao/SCAND/SCAND.html)

**SACSoN**
- MIT licence (per the TFDS/LeRobot card). A higher-resolution private version is available from the authors on request — [TFDS berkeley_gnm_sac_son](https://www.tensorflow.org/datasets/catalog/berkeley_gnm_sac_son); [LeRobot card](https://huggingface.co/datasets/lerobot/berkeley_gnm_sac_son/blob/main/README.md)
- NWM and RAE-NWM train on RECON, SCAND, SACSoN/HuRoN and TartanDrive, preprocessed with the NoMaD pipeline (`process_bags.py`, `process_recon.py`) — [facebookresearch/nwm](https://github.com/facebookresearch/nwm); [20robo/raenwm](https://github.com/20robo/raenwm)

**DROID**
- 76k demonstration trajectories (350 h), 564 scenes, 86 tasks, 1,417 camera viewpoints, collected over 12 months. Hardware: Franka Panda, 2x Zed 2 plus a Zed Mini on the wrist, Oculus Quest 2 for teleoperation. Distributed through TFDS (`gs://gresearch/robotics`). Updated calibrations and language annotations were published on HF in 2024-2025 — [DROID project page](https://droid-dataset.github.io/)
- The Ctrl-World README describes DROID as "~95k trajectories, 564 scenes, ~370GB". That differs from the 76k on the project page, probably because it counts the full release including failed episodes **[discrepancy not resolved]** — [Ctrl-World GitHub](https://github.com/Robert-gyj/Ctrl-World)
- DROID licence: not confirmed on the page I fetched (generally cited as CC BY 4.0) **[UNVERIFIED]**

**Open X-Embodiment (OXE)**
- 1M+ real trajectories, 22 embodiments, 60 datasets from 34 labs, 527 skills (160,266 tasks), 21 institutions — [OXE project page](https://robotics-transformer-x.github.io/)
- Licence: software under Apache 2.0, other materials under CC BY 4.0. Users are asked to also cite the individual component datasets, which may carry their own terms — [open_x_embodiment GitHub](https://github.com/google-deepmind/open_x_embodiment); [summary, emergentmind](https://www.emergentmind.com/topics/open-x-embodiment-dataset)

### Inferences
- For the Bridge to SIMPLER to real WidowX line, the natural choice is BridgeData V2 (CC BY 4.0) with SimplerEnv (MIT). The whole stack can be used and published without licence conflicts.
- Navigation data (RECON, SACSoN: MIT; SCAND: public repository) is permissively licensed, but the NWM weights trained on it are CC BY-NC (see section 3).
- SCAND includes data from a legged robot (Spot), which matters for moving to a robot dog.

### Gaps
- SCAND licence and RECON hour count not confirmed on the pages I fetched.
- DROID licence not confirmed at source.
- No official SIMPLER/ManiSkill fix for Vulkan on headless H100. Whether it works on a specific cluster depends on the driver and on whether the node has the NVIDIA Vulkan ICD installed.

## 2. Simulators: Isaac Lab 3.0 EA, Isaac Sim, ManiSkill3, MuJoCo/MJX/MuJoCo Warp

### Takeaway
Isaac Sim officially **does not support A100 or H100** (no RT cores) and on aarch64 runs only on DGX Spark. That rules it out on Athena (A100), Lem (H100) and Helios (GH200, ARM). Isaac Lab 3.0 EA brings "kit-less" mode with Newton physics and a Warp renderer that do not need Isaac Sim. That makes it the most realistic way to run Isaac Lab tasks on HPC GPU nodes. The alternatives are ManiSkill3 (SAPIEN/Vulkan) and MuJoCo Warp, which has a batch renderer.

### Cited Findings
**Isaac Lab 3.0 Early Access**
- Built for Isaac Sim 6.1, Python 3.12, PyTorch 2.11, NVIDIA Warp 1.16 and Newton 1.5.2. "One task API across multiple physics, rendering, and visualization backends; kit-less execution; Warp-native data paths" — [Isaac Lab v3.0.0-EA release](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)
- The `isaaclab_newton` extension runs environments without Isaac Sim. The full Isaac Sim is only needed for "XR teleoperation, Isaac Sim PhysX, Isaac Sim RTX, Isaac Sim ROS bridge, livestreaming, or Kit tooling" — [release v3.0.0-EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)
- Newton supports MuJoCo-Warp, VBD, MPM and coupled solvers, including deformables, cables and particles — [release v3.0.0-EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)
- Rendering backends: Isaac Sim RTX, Newton Warp renderer, Newton GL visualization, experimental Newton RTX, and OVRTX as optional extras — [release v3.0.0-EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)
- Validated examples in the EA: Franka Lift, G1 rough locomotion, ANYmal-D rough locomotion. GA "targeted toward the end of October 2026". The `release/3.0.0` branch will take only fixes until then — [release v3.0.0-EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)
- EA release date: the tool summary read "September 16, 2024", which contradicts the stack versions and the October 2026 GA. Most likely **16 September 2026** **[date read ambiguously; check on the page]**
- The EA release notes give no GPU or driver requirements.
- Isaac Lab (2.x/main) environments include Go1, Go2 and A1 (`Isaac-Velocity-Flat-Unitree-Go2-v0`), ANYmal B/C/D, Spot (`Isaac-Velocity-Flat-Spot-v0`), H1 and G1 (`Isaac-Velocity-Rough-G1-v0`), Digit, and navigation `Isaac-Navigation-Flat-Anymal-C-v0` — [Isaac Lab environments](https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html)

**Isaac Sim: GPU requirements**
- Requires GPUs with RT cores. Minimum is an RTX 4080 with 16 GB. "**GPUs without RT Cores (A100, H100) are not supported.**" Driver ≥ 595.58.03 (Linux). Ubuntu 22.04/24.04. aarch64 only on **DGX Spark** (DGX OS 7). The container is Linux-only and needs internet access for assets — [Isaac Sim requirements](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html)

**ManiSkill3**
- GPU-parallel simulation and rendering on SAPIEN. The authors report 10-1000x faster than other platforms, 2-3x less GPU memory and 30,000+ FPS in benchmarks. Tasks in 12 domains, including mobile manipulation and humanoids — [ManiSkill3 arXiv 2410.00425](https://arxiv.org/html/2410.00425)
- Rendering goes through SAPIEN/Vulkan, so the H100 issue from section 1 applies here too — [SAPIEN #250](https://github.com/haosulab/SAPIEN/issues/250)

**MuJoCo / MJX / MuJoCo Warp**
- MJX (JAX backend) had no parallel rendering, according to the ManiSkill3 authors — [ManiSkill3 arXiv](https://arxiv.org/html/2410.00425)
- MuJoCo Warp (MJWarp) is MuJoCo written in Warp for NVIDIA GPUs, with a "high-throughput GPU batch renderer" for cameras across many parallel worlds — [MJWarp docs](https://mujoco.readthedocs.io/en/latest/mjwarp/); [google-deepmind/mujoco_warp](https://github.com/google-deepmind/mujoco_warp)
- MuJoCo-Warp is one of the Newton solvers in Isaac Lab 3.0 — [Isaac Lab v3.0.0-EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)

### Inferences
- On Polish HPC (A100, H100, GH200) the plan should assume **kit-less Isaac Lab 3.0 (Newton plus Warp renderer)**, MuJoCo Warp or ManiSkill3, not full Isaac Sim with RTX. Photorealistic RTX rendering (Isaac Sim) would need a separate RTX workstation, such as an RTX 4090/5090 or an L40S.
- Warp and CUDA rendering (Newton Warp renderer, MJWarp) does not need Vulkan or X, which gets around the problem in SAPIEN issue #250. This has not been tested on these clusters **[inference]**.
- Helios GH200 is aarch64. Every simulator must have ARM builds. Warp and MuJoCo generally do; for SAPIEN/ManiSkill on aarch64 I found no confirmation **[UNVERIFIED]**.

### Gaps
- No official GPU/driver requirements for kit-less Isaac Lab 3.0 and no statement on A100/H100/GH200 support.
- No Newton/Warp benchmark on GH200.

## 3. Released models: compute and licences

### Takeaway
World models range from light ones (DINO-WM, semantic-wm, RAE-NWM ~350M, all MIT) through NWM (1B, CC BY-NC 4.0) and Ctrl-World (SVD, MIT, ~5 s per step on H100) to Cosmos Predict 2.5 (NVIDIA Open Model License; 2B at 720p needs ~32.5 GB and ~229 s per clip on H100; 14B needs 2x80 GB or an H200; multiview needs 8x80 GB). Among open VLAs, openpi (π0/π0.5, Apache 2.0) and GR00T N1.7 (Apache 2.0 code, Open Model License weights) have the best documented hardware requirements.

### Cited Findings
**Cosmos Predict 2.5 / Transfer**
- Predict2.5-2B: NVIDIA Open Model License (commercial use allowed, derivatives allowed). The 720p variant needs **32.54 GB VRAM**. BF16 on Ampere, Hopper and Blackwell. Time per clip: **H100 SXM ~229 s**, B200 ~124 s, L40S ~2,567 s. Output is 5 s at 1280x704, 16 FPS. There are robot action-conditioned variants (256p, 4 FPS) and multiview/policy variants — [HF nvidia/Cosmos-Predict2.5-2B](https://huggingface.co/nvidia/Cosmos-Predict2.5-2B)
- "Multiview inference requires a minimum of 8 GPUs with at least 80GB memory each". "Action conditioned inference does not yet support multi-GPU" — [Cosmos Predict2.5 reference](https://docs.nvidia.com/cosmos/latest/predict2.5/reference.html)
- 14B: about 2x H100 80 GB (tensor parallelism) or one H200 141 GB. **This comes from an aggregator blog, not NVIDIA** — [Spheron blog](https://www.spheron.network/blog/deploy-nvidia-cosmos-gpu-cloud-synthetic-data/) **[secondary source]**
- Cosmos Transfer: I did not get specific requirements from a primary source **[gap]**

**V-JEPA 2 / 2-AC / 2.1**
- V-JEPA 2 weights under Apache 2.0. V-JEPA 2-AC (action-conditioned, post-trained on a small amount of robot data) is available (vitg checkpoint, `dl.fbaipublicfiles.com/vjepa2/vjepa2-ac-vitg.pt`). Also in HF Transformers — [facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2); [HF collection](https://huggingface.co/collections/facebook/v-jepa-2); [HF Transformers docs](https://huggingface.co/docs/transformers/en/model_doc/vjepa2)
- V-JEPA 2.1 (arXiv 2603.14482, dense features) exists — [HF paper page](https://huggingface.co/papers/2603.14482). Also `facebook/jepa-wms` on HF — [HF](https://huggingface.co/facebook/jepa-wms)

**NWM (Navigation World Models, CVPR 2025)**
- CDiT up to 1B parameters. Trained on RECON, SCAND, SACSoN/HuRoN and TartanDrive. Training setup: "8 machines of 8 gpus" (Slurm/submitit). Code and weights under **CC BY-NC 4.0**. Weights at HF `facebook/nwm` — [facebookresearch/nwm](https://github.com/facebookresearch/nwm); [HF facebook/nwm](https://huggingface.co/facebook/nwm)

**RAE-NWM (ECCV 2026)**
- Frozen DINOv2 encoder, frozen RAE decoder, CDiT-DH backbone of about 350M parameters (against NWM's 1B) — [arXiv 2603.09241](https://arxiv.org/html/2603.09241v1)
- **MIT** licence. Weights at HF `zmkun20/raenwm`. Data prepared as in NoMaD. Multi-GPU training and inference (example `--nproc_per_node=8`) — [20robo/raenwm](https://github.com/20robo/raenwm)

**DINO-WM**
- **MIT**. Environments: PointMaze, PushT, Wall, Rope and Granular (deformables through PyFleX in Docker). Datasets on OSF. Checkpoints for PointMaze, PushT and Wall — [gaoyuezhou/dino_wm](https://github.com/gaoyuezhou/dino_wm)

**Ctrl-World (ICLR 2026)**
- Based on Stable Video Diffusion plus CLIP ViT-B/32. Trained only on DROID. **MIT**. Inference: "~10s on A100 or ~5s on H100" per interaction step (1 s action chunk). Training on 1-2 nodes of 8x A100/H100. Checkpoints about 8 GB (Ctrl-World) plus about 8 GB (SVD). Integrates π0.5 (openpi) in the loop — [Robert-gyj/Ctrl-World](https://github.com/Robert-gyj/Ctrl-World); [arXiv 2510.10125](https://arxiv.org/abs/2510.10125)

**semantic-wm (Nilaksh et al., "Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models", arXiv 2605.06388)**
- Code at chandar-lab/semantic-wm, **MIT**. Trained on Bridge v2 (downloaded through TFDS). Encoders: SD3 VAE, DINOv2-RAE, SigLIP2/WebSSL ScaleRAE, Qwen2.5-VL, V-JEPA 2.1, Cosmos CI16x16, VA-VAE. Metrics: PSNR/SSIM/LPIPS/FID/FVD, PCK, controllability, success probing. Single-GPU and multi-GPU (`torchrun`, 4+ GPUs in the examples). Checkpoints at HF `Nilaksh404/semantic-wm` — [chandar-lab/semantic-wm](https://github.com/chandar-lab/semantic-wm); [project page](https://hskalin.github.io/semantic-wm/); [arXiv](https://arxiv.org/html/2605.06388v1)
- Main result: "pixel fidelity alone is not enough". Semantic encoders better preserve action information and planning utility — [chandar-lab/semantic-wm](https://github.com/chandar-lab/semantic-wm)
- The README does not mention SIMPLER integration — [chandar-lab/semantic-wm](https://github.com/chandar-lab/semantic-wm)

**Open VLAs**
- **OpenVLA** (7B): code MIT, weights under the **Llama 2 Community License** (inherited from Llama-2). LoRA: 1x A100 80 GB recommended, at least ~27 GB with a smaller batch. Full fine-tuning needs 8x A100. Trained on 970k OXE trajectories — [openvla/openvla](https://github.com/openvla/openvla)
- **Octo**: MIT, JAX. Octo-Small 27M and Octo-Base 93M. Trained on 800k OXE trajectories. HF `rail-berkeley/octo-base-1.5` — [octo-models/octo](https://github.com/octo-models/octo)
- **openpi (π0, π0-FAST, π0.5)**: **Apache 2.0**, PyTorch and JAX. Inference >8 GB, LoRA >22.5 GB (RTX 4090), full fine-tuning >70 GB (A100/H100). Checkpoints for DROID, ALOHA, LIBERO and UR5. Remote inference over WebSocket — [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi)
- **GR00T N1.7** (current GA, successor to N1.6): code Apache 2.0, weights **NVIDIA Open Model License**. Inference on 1 GPU with 16 GB+. Fine-tuning on ≥40 GB GPUs (H100/L40 recommended). Embodiments include **Unitree G1**, Franka (LIBERO), **WidowX (SimplerEnv Bridge)**, Google Robot (SimplerEnv Fractal) and DROID. Backbone is Cosmos-Reason2-2B/Qwen3-VL — [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T); [HF GR00T-N1.6-3B](https://huggingface.co/nvidia/GR00T-N1.6-3B); [HF blog N1.7](https://huggingface.co/blog/nvidia/gr00t-n1-7)

### Inferences
- Cosmos Predict2.5-2B fits on one H100 96 GB (Lem) or GH200 96 GB (Helios), but at ~4 min per 5 s clip, generating thousands of clips means thousands of GPU-hours. It is worth budgeting that explicitly in the grant application.
- Athena's A100 cards are **40 GB**, below the ~32.5 GB+ overhead of Cosmos 720p in practice and below OpenVLA LoRA with a normal batch. Athena suits smaller models (DINO-WM, RAE-NWM, semantic-wm, Octo, π0 LoRA ~22.5 GB) **[inference from the numbers above]**.
- The NWM licence (NC) does not block academic research, but it restricts derivative weights. RAE-NWM (MIT) is the more permissive navigation baseline.

### Gaps
- No per-clip times for Cosmos Transfer 2.5, and no official NVIDIA source for the 14B requirements.
- No memory requirements for NWM, RAE-NWM or semantic-wm inference.
- π0.5 weights: openpi says Apache 2.0 across the repo. I did not check a separate licence for the checkpoints.

## 4. Polish academic compute: WCSS, PLGrid/Cyfronet

### Takeaway
Three GPU clusters are available: **Lem (WCSS, 304x H100 96 GB)**, **Helios (Cyfronet, 440x GH200 96 GB, ARM aarch64)** and **Athena (Cyfronet, 384x A100 40 GB)**. Access is free through computing grants (PLGrid Portal: pilot and proper grants). Everything runs on SLURM with 48 h limits on Cyfronet GPU partitions. The official cluster pages I fetched say nothing about Apptainer or Vulkan/EGL rendering. That has to be checked with the helpdesk.

### Cited Findings
**WCSS (Wrocław)**
- **Lem** (2024): GPU partition of 76 nodes with **304x NVIDIA H100, 96 GB** each, NVLink. About 21 PFLOPS. 80th on TOP500 in June 2024. There are also service nodes with 40x A30. **Bem 2** (2021, 2.2 PFLOPS, CPU). SLURM — [WCSS HPC](https://www.wcss.pl/en/hpc/)
- Lem later placed 99th on TOP500 and 291st on Green500 — [WCSS news](https://www.wcss.wroc.pl/en/news/315/superkomputer-lem-wsrod-najszybszych-superkomputerow-na-swiecie/)
- "The WCSS computers can be used free of charge, on the basis of the so-called computing grants. Grant applications are accepted continuously." User guide at man.e-science.pl — [WCSS HPC](https://www.wcss.pl/en/hpc/)

**Cyfronet: Helios**
- Partitions: CPU (98,304 Zen4 cores), GPU (**440x GH200**), INT (24x H100 for interactive work). 37 PFLOPS — [Helios docs, Cyfronet](https://docs.hpc.cyfronet.pl/supercomputers/helios/); [PLGrid Helios](https://guide.plgrid.pl/en/resources/supercomputers/helios)
- GPU partition `plgrid-gpu-gh200`, 48 h limit, needs a grant with GPGPU resources (account suffix `-gpu-gh200`). Nodes have 4x GH200 96 GB and **4x Grace, 288 cores, aarch64**. "Modules for ARM and x86 CPUs are not interchangeable" — [Helios docs](https://docs.hpc.cyfronet.pl/supercomputers/helios/)
- HPE press release on the launch (April 2024) — [HPE](https://www.hpe.com/us/en/newsroom/press-release/2024/04/academic-computer-centre-cyfronet-agh-launches-polands-fastest-supercomputer-built-by-hewlett-packard-enterprise.html)

**Cyfronet: Athena**
- 48 nodes with **8x A100-SXM4-40GB** (384 GPUs), 128 GB RAM per GPU. Partition `plgrid-gpu-a100`, 48 h limit. Access after a grant and an access request, usually "within approximately 30 minutes". Running non-GPU jobs "will result in account suspension" — [Athena docs](https://docs.hpc.cyfronet.pl/supercomputers/athena/)

**PLGrid grants**
- Pilot grant: give the real topic (not "infrastructure testing"), the scientific goal and a publication declaration — [PLGrid pilot grant](https://guide.plgrid.pl/grants/plgrid/pilot/)
- Proper grant: Portal → "New Grant" → "Grant właściwy PLGrid". Resources are split per centre, with a scientific goal and a description of how they will be used. It gives more and more varied resources than a pilot. After the grant you still request access to the specific cluster (Services tab) — [PLGrid proper grant](https://guide.plgrid.pl/grants/plgrid/proper/); [proper grant, PL](https://guide.plgrid.pl/pl/portal-for-science/grants/plgrid/proper)
- There are also "subordinate" grants (granty podopiecznych), where a supervisor's grant covers their students — [PLGrid subordinate grants](https://guide.plgrid.pl/grants/plgrid/proper/subordinate/)

**Containers and rendering**
- The Helios and Athena pages I fetched **do not mention** Apptainer/Singularity, Vulkan, EGL or VirtualGL — [Helios docs](https://docs.hpc.cyfronet.pl/supercomputers/helios/); [Athena docs](https://docs.hpc.cyfronet.pl/supercomputers/athena/). The WCSS HPC page does not mention them either — [WCSS HPC](https://www.wcss.pl/en/hpc/)
- Generally Apptainer uses `--nv` to mount NVIDIA drivers. The image must contain the CUDA libraries — [Apptainer GPU docs](https://apptainer.org/docs/user/latest/gpu.html). Vulkan in a container also needs the host's NVIDIA ICD and libraries. Without them you get the fallback to llvmpipe described in SAPIEN #250 — [SAPIEN #250](https://github.com/haosulab/SAPIEN/issues/250)

### Inferences
- For SIMPLER/ManiSkill (Vulkan), the most likely working option is Lem (H100, x86). Before submitting the proposal, test `vulkaninfo` and a short SAPIEN render on an interactive node, then write the result into the risk plan.
- Helios (ARM) is good for training PyTorch models (NWM, Cosmos, VLAs) if aarch64 builds exist. It is risky for x86-only simulators.
- Isaac Sim with RTX will not run on any of these clusters (A100/H100 are unsupported, and the only supported aarch64 is DGX Spark). Only the kit-less Isaac Lab 3.0 path remains.

### Gaps
- No primary source for Apptainer/Singularity availability or for graphics rendering (Vulkan/EGL) on Lem, Athena or Helios. Needs a question to the WCSS or Cyfronet helpdesk, or a look at man.e-science.pl or the full docs.hpc.cyfronet.pl.
- No public numbers on typical GPU-hour allocations in PLGrid grants for 2026.
- I did not confirm whether Lem is available through the PLGrid Portal or only through the WCSS KDM procedure.

## 5. Real robots: quadrupeds and humanoids, SDKs, sim-to-real; PWr "Wojtek" and a K46 humanoid

### Takeaway
Unitree (Go2, G1, H1) has the most complete open pipeline: Isaac Lab (`unitree_rl_lab`), MuJoCo (`unitree_mujoco`, `unitree_rl_mjlab`) and deployment through `unitree_sdk2`. Spot has an official RL Researcher Kit built on Isaac Lab. ANYmal is the reference platform for Isaac Lab. **What I could verify about "Wojtek":** a quadruped robot presented by **Wydział Mechaniczno-Energetyczny PWr** (the Faculty of Mechanical and Power Engineering) at Smart City Day on 27 August 2026. I found **no source linking it to the Department of Artificial Intelligence (K46)**, and **no source confirming a humanoid at K46**.

### Cited Findings
**Unitree**
- `unitree_rl_lab` (Apache 2.0): Isaac Lab 2.3.0 / Isaac Sim ≥5.1. Supports **Go2, H1, G1-29dof**. Pipeline: train in Isaac Lab, sim2sim in `unitree_mujoco`, sim2real through `unitree_sdk2` (C++, built from source) — [unitreerobotics/unitree_rl_lab](https://github.com/unitreerobotics/unitree_rl_lab)
- `unitree_rl_gym`: Isaac Gym plus MuJoCo, Go2, H1 and G1, Train → Play → Sim2Sim → Sim2Real — [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym)
- `unitree_rl_mjlab`: MuJoCo backend (mjlab, Isaac Lab-style API), supports Go2, A2, As2, G1, R1, H1_2 and H2 — [unitree_rl_mjlab](https://github.com/unitreerobotics/unitree_rl_mjlab)
- The claim of "80-95% sim2real transfer success" comes from a secondary source (robotlar.org) and is **not reliable** — [Robotlar](https://www.robotlar.org/en/rl-gym) **[secondary source, do not cite as fact]**
- GR00T N1.7 has an embodiment for the Unitree G1 — [Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T)
- Isaac Lab ships Go2, G1 and H1 environments. The 3.0 EA validates G1 rough locomotion — [Isaac Lab envs](https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html); [v3.0.0-EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)
- In Poland the Unitree G1 is sold through distributors (e.g. unitreepolska.pl). Politechnika Rzeszowska (not PWr) set up a humanoid robotics lab with a Unitree G1 U6 on 1 December 2025 — [KIA PRz news](https://kia.prz.edu.pl/category/aktualnosci/); [PRz lab](https://pawelkus.v.prz.edu.pl/uczelnia/nauka/laboratorium-zastosowan-sztucznej-inteligencji-i-robotow-humanoidalnych-77.html)

**Boston Dynamics Spot**
- Spot RL Researcher Kit: joint-level control API, Jetson AGX Orin mount, and a simulation environment in Isaac Lab for sim-to-real — [BD: Get Started with RL for Spot](https://support.bostondynamics.com/s/article/Get-Started-with-Reinforcement-Learning-for-Spot-49966); [RL Researcher Kit User Guide](https://support.bostondynamics.com/s/article/Spot-RL-Researcher-Kit-User-Guide-49965)
- Spot policy in Isaac Lab (PPO, RSL-rl): 85-95k FPS on an RTX 4090, about 4 h of training — [NVIDIA Technical Blog](https://developer.nvidia.com/blog/closing-the-sim-to-real-gap-training-spot-quadruped-locomotion-with-nvidia-isaac-lab/)
- RAI Institute: open-source end-to-end pipeline for Spot in Isaac Lab, zero-shot transfer, up to 5.2 m/s — [RAI Institute (ICRA 2025)](https://rai-inst.com/resources/papers/high-performance-reinforcement-learning-on-spot/)

**ANYmal**
- ANYmal B/C/D in Isaac Lab, plus a navigation task `Isaac-Navigation-Flat-Anymal-C-v0`. ANYmal-D rough is validated in 3.0 EA — [Isaac Lab envs](https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html); [v3.0.0-EA](https://github.com/isaac-sim/IsaacLab/releases/tag/v3.0.0-EA)

**PWr: "Wojtek"**
- Quote: "Czworonożny robot „Wojtek" – nazwany na cześć słynnego niedźwiedzia z Armii Andersa. Wyposażony w kamerę i zaawansowany system poruszania się robot wzbudził ogromne zainteresowanie. W kolejnym etapie prac projektowych otrzyma ramię robotyczne do przenoszenia przedmiotów." ("The quadruped robot 'Wojtek', named after the famous bear of Anders' Army. Equipped with a camera and an advanced locomotion system, the robot attracted a great deal of interest. In the next stage of the project it will get a robotic arm for carrying objects.") Presented by **Wydział Mechaniczno-Energetyczny** at Smart City Day 2026 (27 August 2026) — [WME PWr news](https://wme.pwr.edu.pl/aktualnosci/wydzial-mechaniczno-energetyczny-pwr-na-smart-city-day-2026-990.html)
- The article **does not say** who built it, whether it is a commercial platform (e.g. Unitree) or built in-house, or give any link to K46 or the Faculty of Information and Communication Technology — [WME PWr](https://wme.pwr.edu.pl/aktualnosci/wydzial-mechaniczno-energetyczny-pwr-na-smart-city-day-2026-990.html)
- A search summary said Wojtek was "built completely from scratch in Poland", but I could not trace this to a primary source **[UNVERIFIED]**
- Other PWr legged robots, not to be confused with Wojtek: **Cerber** (a quadruped on loan from S4Tech, developed by the KoNaR student club) — [PWr news](https://pwr.edu.pl/uczelnia/aktualnosci/na-pwr-powstaje-modulowy-robo-pies-do-zadan-specjalnych-14133.html); **Krab** (eight-legged, Wydział Mechaniczny, 2018-2020) — [Evertiq](https://evertiq.pl/news/26124)

**PWr: K46 (Katedra Sztucznej Inteligencji, Department of Artificial Intelligence) and a humanoid**
- K46 is part of the Faculty of Information and Communication Technology (WIT) PWr — [WIT departments](https://wit.pwr.edu.pl/wydzial/struktura-organizacyjna/katedry)
- **I found no public source** (PWr news, WIT pages, search) confirming a humanoid robot at K46 — searches: "Katedra Sztucznej Inteligencji PWr robot humanoidalny" and "PWr WIT robot humanoidalny Unitree G1 2026" returned no such information.

### Inferences
- **Important for the report:** the latest repo commit describes "the Wojtek robot dog (PWr) and the K46 humanoid". Public sources support only this: Wojtek is a PWr quadruped shown by WME. Both the K46 link and the humanoid are unconfirmed in public sources. The report should describe them from the author's own knowledge (e.g. "robot available through a collaboration with WME / at the department"), not cite a source.
- Because Wojtek's model is unknown, it is not clear whether ready sim models (URDF/MJCF, Isaac Lab assets) exist. If it is an in-house design, the plan must include building the URDF/USD and identifying actuator parameters. If it is a Unitree Go2 or similar, the Unitree pipeline covers it.
- A typical 2025-2026 legged sim-to-real pipeline: RL (PPO/RSL-rl) in Isaac Lab or MuJoCo(-Warp) with domain randomization, then sim2sim validation in MuJoCo, then deployment through the manufacturer's SDK (unitree_sdk2, Spot joint API on Jetson). Navigation and manipulation (VLA, world models) usually run as a higher layer on top of that locomotion controller (sources above).

### Gaps
- Wojtek's model, manufacturer and kinematics, and its links to K46: unknown.
- K46 humanoid: no public confirmation.
- 2026 prices and availability of Go2, B2, G1, H1 and ANYmal in Poland: not researched.
- ANYmal SDK (ANYbotics) details: not researched from a primary source.

# Infrastructure and compute feasibility of the IPB plan (real-to-sim-to-real, navigation + manipulation, one PhD student, PWr, Oct 2026 – Sep 2029)

Checked 2026-09-27. Scope: §9 (methods) and §3 (schedule) as visible before the first `<!--`. The prior notes (`research_notes/Uczenie nawigacji w cyfrowych bliźniakach/feasibility_tools_risks.md`, `research/resources.md`) were re-verified where possible. Items re-fetched this session carry a URL. Items taken over from the prior notes without re-fetching are marked "(prior note, not re-fetched)". GitHub metadata comes from `gh api repos/<owner>/<repo>` on 2026-09-27.

**Timing context (inference from §3).** Semesters 1–2 are courses and research starts in semester 3. If semester 3 begins Oct 2026, the student is in the 2nd year of doctoral school in 2026/27. That matters for Minigrant eligibility (see Q5).

## Q1. Datasets: access, licences, scene counts, capture overlap

### Takeaway
**ScanNet++: GO, with a paperwork lead time.**
- It has 1000+ scenes (v2), each with a laser scan, DSLR images and an iPhone RGB-D stream.
- The existence of an official "iPhone NVS" benchmark (train on iPhone, test against DSLR) confirms that the two captures overlap in the same scenes.
- The exact number of scenes with both captures, and the split sizes, were not published on the pages read.

**MuSHRoom: GO, as a small, freely licensed second navigation source.** It has 10 rooms, iPhone + Kinect, a Faro reference mesh, and a CC-BY licence.

**Manipulation: GO for SIMPLER-style visual matching, with a clear constraint.**
- The paired sim/real results cover RT-1, RT-1-X, RT-2-X, Octo-Base and Octo-Small on Google Robot and WidowX/Bridge tasks.
- They do not cover OpenVLA or pi0 in real paired form from the SIMPLER authors. OpenVLA appears in community forks for sim only.
- BridgeData V2 is CC-BY-4.0 but mostly single fixed-view, which limits multi-view 3DGS reconstruction of tabletop scenes.

### Cited Findings

**ScanNet++**
- "1000+ 3D indoor scenes" with "sub-millimeter resolution laser scans", "registered 33-megapixel DSLR images" and "iPhone RGB-D streams". — [ScanNet++ site](https://scannetpp.mlsg.cit.tum.de/scannetpp/)
  - The old URL kaldir.vc.in.tum.de/scannetpp now 301-redirects here.
- Release history, from the same [ScanNet++ site](https://scannetpp.mlsg.cit.tum.de/scannetpp/):
  - v2 released 20 Dec 2024.
  - Undistorted DSLR images and baseline codebases released 30 Apr 2025.
  - "iPhone NVS Benchmark" launched 13 Oct 2025.
  - 360° RGB-D panoramas for 956 scenes released 30 Oct 2025.
  - Nerfstudio dataparser available since Oct 2023.
- Access: "create an account, login and create an application"; after approval you get "a personalized token to download the data". — [ScanNet++ site](https://scannetpp.mlsg.cit.tum.de/scannetpp/)
- The official toolkit has separate pipelines for iPhone ("Decode the iPhone video into images (and depth maps)") and DSLR (undistortion, COLMAP poses), plus an `nvs_test_iphone` split. So both sensors exist for the same scenes. — [scannetpp toolkit README](https://raw.githubusercontent.com/scannetpp/scannetpp/main/README.md)
- ScanNet++ v1 had 460 scenes, 280k DSLR images and 3.7M iPhone frames. — [arXiv:2308.11417](https://arxiv.org/abs/2308.11417) (prior note, not re-fetched)
- Terms of Use (prior note, not re-fetched):
  - Non-commercial research only.
  - Sharing only with people who have signed the terms.
  - The PI/supervisor must sign by hand; a PhD student cannot apply alone.
  - TUM may terminate access.
  - Source: [ScanNet++ ToU PDF (old host)](https://kaldir.vc.in.tum.de/scannetpp/static/scannetpp-terms-of-use.pdf)

**MuSHRoom**
- 10 rooms, captured with Azure Kinect and iPhone 12 Pro Max LiDAR, with Faro X130 reference meshes.
- 40 RGB-D sequences in total: one long and one short sequence per room per device.
- Released on Zenodo under Creative Commons Attribution.
- Sources: [MuSHRoom project page](https://xuqianren.github.io/publications/MuSHRoom/); [Zenodo iPhone part 1](https://zenodo.org/records/10154395); [arXiv:2311.02778](https://arxiv.org/pdf/2311.02778)
- The GitHub repo TUTvision/MuSHRoom has no licence file detected by GitHub; last push 2024-10-24. — GitHub API

**BridgeData V2**
- 60,096 trajectories (50,365 teleoperated + 9,731 scripted) in 24 environments. — [BridgeData V2 site](https://rail-berkeley.github.io/bridgedata/)
- CC-BY-4.0. — [BridgeData V2 site](https://rail-berkeley.github.io/bridgedata/)
- Camera views: one fixed over-the-shoulder RGB-D camera (640×480), two randomized RGB cameras (poses changed every 50 trajectories) and a wrist camera. However, "the majority of the data only includes the primary fixed camera view, and very little data currently includes all 4 views." — [BridgeData V2 site](https://rail-berkeley.github.io/bridgedata/)

**Open X-Embodiment**
- 1M+ trajectories, 22 embodiments, 60 datasets, 34 labs.
- There is no single licence: per-dataset licences are listed in a spreadsheet.
- Source: [OXE project page](https://robotics-transformer-x.github.io/)

**SIMPLER**
- Two evaluation methods: "visual matching" (real images overlaid on sim backgrounds) and "variant aggregation".
- Robots: Google Robot and WidowX/Bridge.
- The code is based on SAPIEN and "CPU based ManiSkill2". A separate GPU-parallel ManiSkill3 version is "10-15x faster".
- Needs an NVIDIA GPU; "non-RTX GPUs may experience slowness with ray tracing".
- Repo MIT; last push 2025-12-20.
- Sources: [SimplerEnv README](https://raw.githubusercontent.com/simpler-env/SimplerEnv/main/README.md); GitHub API
- Paired policies: RT-1, RT-1-X, RT-2-X, Octo-Base, Octo-Small, with "~1500 evaluation episodes (from each of real and sim)"; correlation is reported as MMRV and Pearson r. — [SIMPLER project page](https://simpler-env.github.io/); paper [arXiv:2405.05941](https://arxiv.org/abs/2405.05941)
- The community fork SimplerEnv-OpenVLA adds OpenVLA inference to SIMPLER (sim side). — [DelinQu/SimplerEnv-OpenVLA](https://github.com/DelinQu/SimplerEnv-OpenVLA)
- Later VLA papers report pi0 SIMPLER sim scores (e.g. "+25.3%" over pi0 under visual matching), but these are sim-only numbers, not paired real results. — search summary of [SpatialVLA arXiv:2501.15830](https://arxiv.org/pdf/2501.15830) and related papers; not read in full.

### Inferences
- **Navigation protocol in §9 (twin from one capture, the other capture as "real" frames and reference).** ScanNet++ (iPhone → twin; laser + DSLR → reference) supports it directly. The ScanNet++ iPhone NVS benchmark is almost the same split and gives a ready-made public comparison point.
- **ScanNet++ lead time.** Apply in the first weeks of Oct 2026. The supervisor's handwritten signature is on the critical path. Plan to release code and metrics, not derived twins; derived twins can be released for MuSHRoom (CC-BY).
- **Manipulation twins.** Build them from SIMPLER's own assets and overlay images rather than reconstructing BridgeData scenes from scratch. Single-view Bridge frames rarely support a full 3DGS reconstruction; at best they allow a partial or background-only one, so a from-scratch 3DGS of Bridge tabletops is high-risk.
- **"Published real-robot results of the same policies" (§9).** In practice this means RT-1 family and Octo from the SIMPLER paper. Claims about OpenVLA or pi0 real-vs-sim correlation would rely on third-party papers and need checking case by case.

### Gaps
- The number of ScanNet++ v2 scenes that have both iPhone and DSLR captures, and the train/val/test sizes, were not found on the pages read. Check the downloaded metadata after access is granted.
- The current ScanNet++ ToU text on the new host was not re-fetched.
- SIMPLER's MMRV/Pearson values and whether the real rollouts (videos or per-episode outcomes) are released were not confirmed.
- MuSHRoom's exact licence variant (CC-BY 4.0 vs other) comes from the search summary and the project page; the Zenodo record's licence field was not opened directly.

## Q2. Simulators and renderers on A100/H100 SLURM clusters

### Takeaway
**Habitat-Sim (MIT, v0.3.3, Feb 2026): GO.**
- Native 3DGS rendering now exists as **Habitat-GS** (ECCV 2026, zju3dv), a Habitat-Sim fork that renders `.gs.ply` stages and keeps NavMesh/Habitat-Lab.
- Its licence is not declared ("NOASSERTION"), so treat it as research code.

**ManiSkill3 (Apache-2.0, v3.0.1): GO with setup risk.**
- Rasterized rendering works on A100/H100 via Vulkan once the host driver's Vulkan ICD files are bound into the container. There is a documented Singularity recipe.
- Ray tracing on H100 is reported as "not very fast" or unavailable in practice.

**Isaac Sim: NO-GO on Lem/Athena/Helios** (no RT cores on A100/H100). It would need a local RTX GPU.

**gsplat and COLMAP 4.x: GO. Nerfstudio: usable but stale.**

### Cited Findings

**Habitat**
- Habitat-Sim: MIT, v0.3.3 (2026-02-12), last push 2026-07-21. — GitHub API
- Habitat-GS: [arXiv:2604.12626](https://arxiv.org/abs/2604.12626); [zju3dv/habitat-gs README](https://raw.githubusercontent.com/zju3dv/habitat-gs/main/README.md)
  - "integrates 3D Gaussian Splatting scene rendering and drivable gaussian avatars while maintaining full compatibility with the Habitat ecosystem".
  - 3DGS handles visuals and the NavMesh governs navigation.
  - Code released Apr 2026; accepted to ECCV 2026.
  - Install: Python 3.12, CUDA PyTorch, `HABITAT_WITH_CUDA=ON HABITAT_WITH_BULLET=OFF pip install .`.
  - Needs Habitat-Lab numpy pinned to `>=2.0.0,<2.4`.
  - Scene assets must be named `*.gs.ply` / `*.3dgs.ply`.
  - README guidance for StreamVLN fine-tuning: "≥80 GB VRAM per GPU (A100 80GB recommended)"; LoRA fits on "a single 24GB RTX 4090".
- Habitat-GS repo: licence NOASSERTION, 308 stars, last push 2026-09-17. — GitHub API
- NavGSim is another GS navigation simulator. — [arXiv:2603.15186](https://arxiv.org/pdf/2603.15186) (title only)

**ManiSkill / SAPIEN**
- ManiSkill: Apache-2.0, v3.0.1 (2026-04-21), last push 2026-08-04. SAPIEN 3.0.3 (2026-03-10). — GitHub API
- GPU sim and rendering are supported on Linux/NVIDIA. Rendering needs Vulkan (`libvulkan1` plus NVIDIA ICD config files). The docs mention an extra Vulkan config file for A100. A Docker image `maniskill/base` exists. — [ManiSkill install docs](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html)
- Shaders: `minimal, default, rt, rt-med, rt-fast`. The docs do not state RT-core requirements. — [ManiSkill sensors docs](https://maniskill.readthedocs.io/en/latest/user_guide/concepts/sensors.html)
- ManiSkill issue #1131, "Setting up Maniskill on A100 Server": [mani-skill/ManiSkill#1131](https://github.com/mani-skill/ManiSkill/issues/1131)
  - The problem was solved with a Singularity recipe that binds host NVIDIA Vulkan libraries and the `nvidia_icd.json` / `10_nvidia.json` files.
  - The recipe author reports it "worked" on 5 clusters: [AlexandreBrown/Maniskill3-Singularity-Example](https://github.com/AlexandreBrown/Maniskill3-Singularity-Example).
  - A maintainer recommends the 4090 as "the best and fastest GPU to run simulation on".
- SAPIEN issue #250 (H100 headless), still open: [haosulab/SAPIEN#250](https://github.com/haosulab/SAPIEN/issues/250)
  - The maintainer ran "both rasterization and ray tracing" on H100, "just not very fast".
  - Vulkan works only on "vanilla H100", not on virtualised or split GPUs.
  - Old drivers crash on ray tracing.
  - Another user fixed it by installing `libnvidia-gl-570-server` — "No raytracing of course".

**Isaac Sim / Isaac Lab**
- Isaac Sim: "GPUs without RT Cores (A100, H100) are not supported". — [Isaac Sim requirements](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html) (prior note, not re-fetched)
- Isaac Lab issue "[Bug Report] H100 Incompatible With Tiled Camera" (title only). — [isaac-sim/IsaacLab#4271](https://github.com/isaac-sim/IsaacLab/issues/4271)
- NVIDIA ovrtx fails on A100/A800 without `VK_KHR_ray_query`. — [NVIDIA-Omniverse/ovrtx#1](https://github.com/NVIDIA-Omniverse/ovrtx/issues/1)

**Reconstruction tools**
- gsplat: Apache-2.0, latest release v1.5.3 (2025-07-04), last push 2026-09-19. — GitHub API
- nerfstudio: Apache-2.0, last release v1.1.5 (2024-11-11), last push 2025-07-29. — GitHub API
- COLMAP 4.2.0 (2026-09-01); GLOMAP is now merged as COLMAP's "global" mapper. — GitHub API; [GLOMAP README](https://raw.githubusercontent.com/colmap/glomap/main/README.md) (prior note)

**Clusters**
- Helios GPUs are GH200 (Grace ARM CPU + Hopper). — [Helios docs](https://docs.hpc.cyfronet.pl/supercomputers/helios/)
- WCSS publishes an Apptainer documentation page; its content could not be extracted (JS page). — [man.e-science.pl apptainer](https://man.e-science.pl/pl/kdm/apptainer)

### Inferences
- **Recommended stack:** ScanNet++ poses (or COLMAP 4 global mapper) → gsplat → (a) Habitat-GS for 3DGS-rendered navigation and (b) a mesh extracted from the 3DGS for collisions.
- Build one Apptainer image per simulator. Budget ~2–4 weeks of engineering in semester 3 for the Vulkan/EGL binding on Lem, and test Habitat EGL and SAPIEN Vulkan in the first week of cluster access.
- **Helios (aarch64)** is a poor target for simulators, because Habitat and SAPIEN wheels are x86-oriented (not verified). Use Helios, if at all, only for pure PyTorch training of models such as OpenVLA LoRA.
- **Avoid ray-traced shaders.** SIMPLER's visual matching uses rasterization plus a real-image overlay, so RT is not needed.
- **Isaac Sim / NuRec** should not appear in the plan unless a local RTX workstation is budgeted.

### Gaps
- No first-hand report was found of Habitat-GS running on an H100 cluster, nor of Habitat-GS rendering throughput (FPS) for RL.
- Habitat-GS licence is undeclared. Check before building on it or releasing derived code.
- Whether WCSS Lem nodes expose Vulkan/EGL graphics libraries (`libnvidia-gl`) was not verified. Ask WCSS support.
- Whether Lem allows Apptainer with `--nv` was not read (the page did not render).

## Q3. Models: licences and GPU memory

### Takeaway
**Octo (MIT): GO.** It fits on one consumer GPU for inference and fine-tuning, and it is the only VLA-type policy with published SIMPLER real/sim pairs.

**OpenVLA: GO.** Code is MIT; weights are under the Llama 2 Community License (fine for research). LoRA needs ~72 GB (one A100/H100 80–96 GB); full fine-tuning needs 8×A100.

**pi0 / pi0.5 (openpi): GO for research, with caveats.** Code is Apache-2.0; weights are PaliGemma-based, so Gemma terms apply (secondary source). Inference needs > 8 GB, LoRA > 22.5 GB, full fine-tuning > 70 GB. The JAX path is complete; the PyTorch path lacks LoRA.

**GNM/ViNT/NoMaD: GO.** MIT, small models, but the repo is unmaintained since Sep 2024.

### Cited Findings
- **OpenVLA** — [OpenVLA GitHub](https://github.com/openvla/openvla); last push 2025-03-23 (GitHub API)
  - Code MIT.
  - `openvla-7b` weights are "subject to the Llama Community License".
  - LoRA on one A100 80 GB at batch 16 takes ~72 GB.
  - Full fine-tuning needs "a full node of 8 A100 GPUs".
  - Trained on OXE "970K trajectories".
- **Octo** — [Octo README](https://raw.githubusercontent.com/octo-models/octo/main/README.md); last push 2024-07-31, v1.5 (GitHub API)
  - MIT.
  - Octo-Base has 93M parameters (13 it/s on a 4090); Octo-Small has 27M (17 it/s).
  - JAX.
  - Inference on a single 4090.
  - Pretraining on TPUv4-128 took 8–14 h.
  - Fine-tuning works on "accessible compute budgets".
- **openpi** — [openpi README](https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/README.md); [openpi LICENSE](https://github.com/Physical-Intelligence/openpi/blob/main/LICENSE); GitHub API (last push 2026-08-24)
  - Apache-2.0.
  - Models: pi0, pi0-FAST, pi0.5 base models; fine-tuned DROID, ALOHA and LIBERO checkpoints.
  - Memory: inference > 8 GB, LoRA > 22.5 GB, full fine-tuning > 70 GB (A100/H100).
  - The PyTorch port "lacks π₀-FAST, mixed precision, FSDP, LoRA, and EMA support".
- **openpi weight terms:** weights built on the PaliGemma backbone fall under the Gemma Terms of Use. — secondary: [HF card maniguard-review/pi0-jar](https://huggingface.co/maniguard-review/pi0-jar) (third-party card, not PI's own statement)
- **GNM/ViNT/NoMaD** (robodhruv/visualnav-transformer): MIT, last push 2024-09-15, single "code_release" tag (2023-10-06). — GitHub API
  - Training data: RECON, SCAND, GoStanford2, SACSoN; some need author contact. — [visualnav-transformer README](https://raw.githubusercontent.com/robodhruv/visualnav-transformer/main/README.md) (prior note)

### Inferences
- **Manipulation.** Octo-Small/Base (MIT, cheap) can be the workhorse for the many-run experiments (twin variants × seeds). OpenVLA can be used for a smaller confirmatory set: LoRA on one H100 96 GB per run, fitting Lem's 96 GB cards. pi0 LoRA also fits on one H100.
- **Probing (RQ2).** Only forward passes with hooked activations are needed, so every model fits on one GPU.
- **Navigation.** NoMaD/ViNT are small (tens of millions of parameters) and cheap. The Habitat-GS/EmbodiedSplat-style ImageNav/PointNav agents (e.g. DD-PPO ResNet policies) are also small.

### Gaps
- No primary source was found for NoMaD/ViNT GPU memory or fine-tuning GPU-hours.
- No primary source was found for Octo fine-tuning GPU-hours (the README gives only qualitative claims).
- The pi0 weights licence was not confirmed from a Physical Intelligence page.
- OpenVLA bf16 inference memory was not stated in the README read. The commonly cited ~15 GB was not verified this session.

## Q4. Compute: WCSS Lem, PLGrid Athena/Helios, and the end-to-end GPU-hour budget

### Takeaway
**Compute access is not a blocker.**
- Lem has 304 H100 (96 GB) GPUs on 76 nodes. SLURM partitions: lem-gpu-short (3-day limit, 74 nodes) and lem-gpu-normal (52 nodes).
- PLGrid grants are open to doctoral students. A "proper" grant (Grant właściwy) for a student under supervision is filed by the supervisor as team leader.
- A pilot grant is active within an hour. Only one pilot grant is allowed per 12 months; it is renegotiated rather than re-created.

**Our estimate of the whole plan: roughly 8,000–20,000 H100-GPU-hours over three years (about 3–7k per year).** That is a normal PLGrid/WCSS grant scale, provided the heavy runs use small policies and 7B VLAs are limited to a small subset.

### Cited Findings
- **WCSS Lem (Lem entry in the PLGrid guide):** [PLGrid guide: Lem](https://guide.plgrid.pl/pl/infrastructure/resources/supercomputers/lem); [WCSS HPC](https://www.wcss.pl/en/hpc/)
  - 76 GPU nodes with 304 H100 GPUs, 96 GB each, NVLink.
  - 1 TB RAM per GPU node; InfiniBand 4× NDR 200 Gb/s.
  - Plus 40 A30 service nodes.
- **WCSS SLURM partitions:** [WCSS SLURM partitions](https://man.e-science.pl/i/402)
  - `lem-gpu-short`: 74 nodes, 4× "NVIDIA H100-94GB" per node, max time 3-00:00:00.
  - `lem-gpu-normal`: 52 nodes.
  - Jobs need a service with CPU and GPU hours ("wymagana usługa posiadająca CPU i GPU godziny").
  - Note the minor discrepancy: 94 GB here vs 96 GB on the WCSS page.
- **PLGrid proper grant for a supervised researcher (Grant Podopiecznego):** [PLGrid: Granty podopiecznych](https://guide.plgrid.pl/pl/portal-for-science/grants/plgrid/proper/subordinate)
  - "O Grant Właściwy na zasoby dla Podopiecznego zawsze wnioskuje … Opiekun" (the supervisor always applies).
  - The student must be added to the supervisor's team and needs the team-leader role to edit or renegotiate.
- **PLGrid pilot grant:** [PLGrid: Grant pilotażowy](https://guide.plgrid.pl/grants/plgrid/pilot/) (page last updated 1 Sep 2026)
  - "Możliwe jest ubieganie się o tylko jeden grant pilotażowy w ciągu 12 miesięcy" (only one pilot grant per 12 months).
  - When resources run out, renegotiate rather than open a new pilot.
  - Active "w ciągu godziny" (within an hour).
  - A search snippet (from an older docs page) says a pilot grant gives "1000 computing hours and 10 GB", with 72-h max jobs and one-year validity. That was not visible on the current page. — [older PLGrid wiki page](https://docs.plgrid.pl/pages/viewpage.action?pageId=130286476)
- **Athena and Helios:** access goes through a PLGrid computing grant; Helios grants must list related projects and an HPC-centre cooperant. — [Helios docs](https://docs.hpc.cyfronet.pl/supercomputers/helios/)
  - Athena has 384× A100 (per resources.md, prior note, not re-fetched).
- **Reference compute points (prior note):**
  - DD-PPO reaches 90% of peak PointNav at 100M steps in < 1 day on 8 GPUs (≈ 192 GPU-h). — [arXiv:1911.00357](https://arxiv.org/abs/1911.00357)
  - 3DGS takes 35–45 min per scene (A6000). — [arXiv:2308.04079](https://arxiv.org/pdf/2308.04079)
  - SceneSplat-7K: ~27 L4-GPU-min per scene. — [HF scene_splat_7k](https://huggingface.co/datasets/GaussianWorld/scene_splat_7k)
  - OpenVLA LoRA fits on one A100 80 GB. — [OpenVLA GitHub](https://github.com/openvla/openvla)

### Inferences — end-to-end budget (our estimate; assumptions stated, not sourced)

| Block | Units | GPU-h per unit (H100) | Total GPU-h |
|---|---|---|---|
| 3DGS twins, navigation: 30 scenes × ~8 variants (iPhone twin; DSLR/laser reference; 3–4 "one error corrected" variants; 2–3 capture budgets) | 240 fits | 0.3–0.7 | 70–170 |
| Mesh extraction, NavMesh, dataset-based reference renders | 240 | 0.1–0.3 | 25–70 |
| Navigation policy fine-tuning (RL/IL from a pretrained agent) in twins: 30 scenes × 6 variants × 3 seeds, or pooled over scenes | 300–540 runs | 5–20 (assumes 10–50M steps at ~1–3k FPS; Habitat-GS FPS unverified) | 1,500–10,800 |
| Navigation evaluation on reference and real frames (open-loop) | — | — | 200–500 |
| Manipulation twins (SIMPLER assets + visual matching; plus a few 3DGS tabletop backgrounds) | 10–20 scenes × 4 variants | 0.3–0.7 | 20–60 |
| Octo fine-tuning in twin variants: ~15 scenes/tasks × 4 variants × 3 seeds | 180 runs | 2–6 | 360–1,080 |
| OpenVLA (or pi0) LoRA confirmatory runs | 20–40 runs | 10–25 | 200–1,000 |
| SIMPLER-style evaluation of all checkpoints (hundreds of episodes each; 7B inference) | ~300 evals | 1–3 | 300–900 |
| RQ2 probing (activation extraction + linear probes + alignment variants) | — | — | 300–800 |
| RQ3 real-data selection loops (repeat twin + model correction under budgets) | — | — | 1,000–3,000 |
| RQ4 held-out scenes and hidden-parameter sim studies | — | — | 500–1,500 |
| Debugging and failed runs (×1.3–1.5 on the above) | — | — | +1,500–5,000 |
| **Total (3 years)** | | | **≈ 6,000–25,000; central ≈ 10–15k** |

- The dominant uncertainty is the navigation RL fine-tuning cost, which depends on Habitat-GS rendering throughput (FPS). Mitigations:
  - (a) Pool scenes into one policy per variant rather than one per scene.
  - (b) Use IL / behaviour cloning from NavMesh shortest-path experts, which costs about 10× less than RL.
  - (c) Render at low resolution (e.g. 128×128).
- For scale: 15k GPU-h is about 5 H100-months of continuous use, or less than 0.2% of one year of Lem's 304 GPUs (304 × 8,760 ≈ 2.66M GPU-h/yr).
- **Wall-clock time.** With 4–8 concurrent GPUs, each paper's experiment block (3–5k GPU-h) finishes in roughly 3–6 weeks of queue time. That fits the semester-level schedule in §3.
- **Storage.** ScanNet++ is multi-TB with DSLR + iPhone video (not verified here). A pilot grant's 10 GB is far too small. Request project storage (≥ 5–10 TB on Lustre) in the proper grant.

### Gaps
- The typical GPU-hour size of a proper PLGrid grant for a doctoral student, and the current pilot-grant resource amounts, are not stated on the pages that could be read (the guide renders client-side).
- The WCSS "Przetwórz na superkomputerze" service limits were not re-fetched (they are in research/resources.md with URLs).
- Queue wait times are not published.
- The ScanNet++ total download size was not confirmed.
- The K46 department GPU servers are undocumented publicly (prior note).

## Q5. Robot access: TurtleBot 4, SzD Minigrant, K29 Denali lab

### Takeaway
Real-robot validation is optional in §9/§3 ("if access allows").
- A TurtleBot 4 Lite costs **€1,804.80 incl. VAT** (€1,504 excl.) at Generation Robots, or €1,699 at MYBOTSHOP.DE (model not specified). That is roughly 7–8k PLN, well inside a Minigrant.
- **SzD Minigrant:** up to **20,000 PLN**, for 2nd–4th year doctoral students, one per doctoral period. Equipment and conferences are eligible.
- The 2026 call closed 20 Jan 2026, with projects running 1 Mar – 15 Dec 2026. The next call is expected around Jan 2027 (inference), which fits a year-2 student.
- The **K29 Denali lab (L1.5)** has Pioneer P3-DX (ROS 2), a DrRobot Jaguar 4x4 and a Robai Cyton arm. No sensor list (RGB-D, lidar) is published, and no modern tabletop arm comparable to WidowX is listed.

### Cited Findings
- **TurtleBot 4 prices:**
  - TurtleBot 4 Lite: "€1,804.80 VAT incl. / €1,504.00 VAT excl." (item A-000000-05408). — [Generation Robots](https://www.generationrobots.com/en/404087-robot-mobile-turtlebot4-tb4-lite.html)
  - TurtleBot 4 at €1,699.00 (variant not clear in the search snippet). — [MYBOTSHOP.DE](https://www.mybotshop.de/TurtleBot-4_1)
  - Earlier: TB4 Lite "Pre-order € 1.699,00 (incl. VAT)". — [Elektor](https://www.elektor.com/products/clearpath-robotics-turtlebot-4-lite) (prior note)
  - 2022 launch price $1,195 Lite / $1,850 Standard; the Lite has a 2D LiDAR and an OAK-D-Lite. — [Clearpath blog](https://clearpathrobotics.com/blog/2022/05/clearpath-robotics-launches-turtlebot-4/) (prior note)
- **SzD PWr Minigranty:** [SzD Minigranty](https://szd.pwr.edu.pl/doktoranci/minigranty)
  - Max 20,000 PLN.
  - Eligible: 2nd, 3rd or 4th year doctoral students (not implementation doctorates) who have not been a project leader in the last 12 months.
  - Deadline 20 Jan 2026, 13:00: paper copy with signatures to SzD room 313 A-1, plus a PDF to minigranty@pwr.edu.pl.
  - Results by 13 Feb 2026; projects run 1 Mar – 15 Dec 2026 (4th-year students until 15 Aug).
  - Eligible costs include "zakup aparatury, urządzeń, materiałów" (equipment, devices, materials), services, short research trips, conferences and training.
  - Minimum score 50/100; one grant per student during the studies.
- **Denali lab (K29, C-16 L1.5):** [Denali robots](https://denali.kcir.pwr.edu.pl/robots.php)
  - Pioneer P3-DX ("small lightweight two-wheel two-motor differential drive robot … for indoor laboratory"), used in Mobile Robotics labs and controlled via ROS 2 in the lab network, with a Python library.
  - Robai Cyton manipulator.
  - DrRobot Jaguar 4x4 (indoor/outdoor).

### Inferences
- **Navigation validation is realistic.** Options:
  - (a) Borrow a Denali P3-DX and mount an RGB-D camera (a few hundred euros; this could come from the Minigrant).
  - (b) Buy a TurtleBot 4 Lite from the 2027 Minigrant (the call is expected ~Jan 2027 and the student will be in year 2).
  - Either fits semester 6 (spring 2028) validation.
- **Manipulation validation is realistic only as a small demo.** The Cyton is a hobby-class arm, and no WidowX-class arm is listed at PWr, so matching SIMPLER/Bridge real conditions is not possible locally. A WidowX 250 kit would exceed a TurtleBot purchase (price not checked). Keep manipulation evaluation on published paired results, as §9 already says.

### Gaps
- The 2027 Minigrant call dates are not published yet; the ~Jan 2027 timing is an inference from the 2026 call.
- Denali robot sensors and whether external doctoral students may use the lab were not published. Ask K29.
- Polish distributor pricing and TB4 lead times were not checked.
- Other PWr labs (e.g. manipulation labs in W4N/W12N) were not surveyed.

## Q6. Hard blockers and mitigations; go/no-go summary

### Takeaway
There is no hard blocker that makes the plan infeasible. The real risks are:
- (1) ScanNet++ access and licence: supervisor signature needed; no release of derived twins.
- (2) Headless Vulkan/EGL rendering on Lem for SAPIEN/Habitat-GS inside Apptainer.
- (3) Unknown Habitat-GS throughput, which drives most of the compute budget.
- (4) Manipulation real references limited to RT-1/Octo-class policies and few Bridge scenes with multi-view images.
- (5) Research-code dependencies with an unclear licence (Habitat-GS) or no maintenance (nerfstudio, visualnav-transformer, Octo).

### Cited Findings
Individual facts are cited in Q1–Q5. Key blocker evidence:
- Isaac Sim does not support A100/H100. — [Isaac Sim requirements](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html) (prior note)
- A100 ManiSkill failures were resolved by a Singularity recipe. — [ManiSkill#1131](https://github.com/mani-skill/ManiSkill/issues/1131)
- H100 SAPIEN Vulkan needs `libnvidia-gl` and non-virtualised GPUs. — [SAPIEN#250](https://github.com/haosulab/SAPIEN/issues/250)
- Bridge is mostly single-view. — [BridgeData V2](https://rail-berkeley.github.io/bridgedata/)
- ScanNet++ access requires an application and token. — [ScanNet++](https://scannetpp.mlsg.cit.tum.de/scannetpp/)
- Habitat-GS licence NOASSERTION. — GitHub API

### Inferences — go/no-go table

| Component | Verdict | Condition / mitigation |
|---|---|---|
| ScanNet++ v2 (iPhone + DSLR + laser) | GO | Apply in Oct 2026 with the supervisor's handwritten signature. Release code and metrics only. Fallback: MuSHRoom (CC-BY). |
| MuSHRoom | GO | Only 10 rooms. Use for a held-out or public-release subset. |
| BridgeData V2 / OXE | GO (as data), weak for 3DGS | Mostly single-view. Use SIMPLER assets and overlays; check per-dataset licences in the OXE sheet. |
| SIMPLER paired real results | GO (limited) | Covers RT-1, RT-1-X, RT-2-X and Octo only. State that OpenVLA/pi0 have sim-only results. |
| Habitat-Sim / Habitat-Lab | GO | MIT, maintained. |
| Habitat-GS (3DGS in Habitat) | GO-conditional | Licence unclear and new code. Fallback: mesh-from-3DGS in plain Habitat, or your own gsplat render loop. |
| ManiSkill3 / SAPIEN on Lem | GO-conditional | Apptainer with host Vulkan ICD binding (documented recipe); rasterization only. |
| Isaac Sim / Isaac Lab | NO-GO on clusters | Only with a local RTX GPU (≥ 16 GB). Not needed for the plan. |
| gsplat, COLMAP 4 | GO | Active and permissive. |
| nerfstudio | GO (stale) | Use it only for dataparsers; train with gsplat directly. |
| Octo | GO | MIT, small. Main manipulation workhorse. |
| OpenVLA | GO | Llama 2 licence; LoRA on one 80–96 GB GPU. |
| pi0 / pi0.5 (openpi) | GO (research) | Gemma terms apply (secondary source); JAX for LoRA. |
| GNM/ViNT/NoMaD | GO | MIT, unmaintained. Pin versions. |
| WCSS Lem / PLGrid | GO | Pilot grant immediately; the supervisor files a proper grant of ~5k GPU-h/yr plus ≥ 5–10 TB storage. |
| Helios (GH200, ARM) | Avoid for simulators | Use only for pure PyTorch training, if at all. |
| Real robot (navigation) | GO-conditional | Denali P3-DX loan or TB4 Lite via Minigrant 2027 (≤ 20k PLN). |
| Real robot (manipulation) | NO-GO locally | No WidowX-class arm found at PWr. Rely on published paired results. |

**Blockers → mitigations (ordered by impact)**
1. **ScanNet++ access delay or refusal** → apply in week 1. Build the pipeline on MuSHRoom meanwhile. The ARKitScenes (iPad LiDAR + laser) fallback comes from the prior note.
2. **Vulkan/EGL not available on Lem compute nodes** → test in the first week with a pilot grant. Ask WCSS for `libnvidia-gl` / EGL vendor files. Fallback: Athena (x86 A100) or a department RTX box. The ManiSkill team itself recommends 4090-class GPUs.
3. **Habitat-GS throughput too low for RL** → switch to IL from NavMesh experts, pooled training, lower resolution, and mesh rendering for most runs with 3DGS rendering only for evaluation.
4. **Manipulation "reality" reference too narrow** → frame manipulation results as correlation with the SIMPLER paired set (RT-1/Octo). Use ManiSkill3 hidden-parameter sims (§9) for controlled studies. Do not promise OpenVLA/pi0 real numbers.
5. **Licences blocking release** → release code, configs and per-scene metrics. Release derived twins only for CC-BY data (MuSHRoom, Bridge-derived).
6. **Compute overrun** → cap 7B-VLA runs at ~1–2k GPU-h in total. Use Octo/NoMaD for sweeps. Renegotiate the PLGrid grant mid-year.

### Gaps
- No evidence was found either way on whether other PWr departments have manipulation arms available to doctoral students.
- No published end-to-end compute figure was found for a comparable "3DGS twin → policy fine-tune → real correlation" study (EmbodiedSplat and Habitat-GS compute not read). The budget above is therefore an informed estimate, not a sourced number.

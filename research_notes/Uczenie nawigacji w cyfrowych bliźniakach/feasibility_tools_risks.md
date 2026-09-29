# Feasibility (data, tools, compute, robots) and key risks of a real-to-sim-to-real navigation PhD without an own robot

Checked 2026-09-26. Everything below was fetched in this session: licence texts, GitHub API, arXiv API and official pages. Items that could not be confirmed are listed under Gaps. Repo context: this re-verifies research/resources.md §2 and content/09-methods.md, which assume ScanNet++ proxy reality, Habitat, 3DGS twins, WCSS/PLGrid GPUs and ~8 robot-hours per campaign.

## Q1. Real indoor-scene datasets pairing a high-fidelity reference with a cheaper separate capture, with licences and whether derived reconstructions may be released

### Takeaway
ScanNet++ is the only dataset found that pairs a laser scan and DSLR images with a separate iPhone RGB-D capture at scale (1000+ scenes in v2). This makes the §9 proxy-reality protocol technically feasible. However, its Terms of Use forbid sharing the data with anyone who has not signed them, need a handwritten signature from the PI or supervisor, and are non-commercial. Publicly releasing reconstructions derived from ScanNet++ (twins, meshes, splats) is therefore **not clearly allowed**. Release code and numbers, not the scenes. MuSHRoom (CC-BY-4.0 on Zenodo; iPhone + Kinect + reference mesh) and ARKitScenes (iPad LiDAR + stationary laser-scanner depth) are secondary paired options. HM3D, MP3D, Gibson and Replica have no separate cheap capture.

### Cited Findings
- **ScanNet++ content:** "1000+ 3D indoor scenes containing sub-millimeter resolution laser scans, registered 33-megapixel DSLR images, and commodity RGB-D streams from iPhone". v2 was released 20 Dec 2024. — [ScanNet++ site](https://kaldir.vc.in.tum.de/scannetpp/)
- **ScanNet++ v1 paper:** 460 scenes, 280k DSLR images and 3.7M iPhone RGB-D frames. — [arXiv:2308.11417](https://arxiv.org/abs/2308.11417)
- **ScanNet++ additions since v1:**
  - 13 Oct 2025: an "iPhone NVS Benchmark — train on commodity-level captures and test against high-quality DSLR images".
  - 30 Oct 2025: 360° RGB-D panoramas for 956 scenes.
  - 30 Apr 2025: undistorted DSLR images and a 3DGS example codebase.
  - A nerfstudio dataparser has existed since Oct 2023.
  - Source: [ScanNet++ site](https://kaldir.vc.in.tum.de/scannetpp/)
- **ScanNet++ Terms of Use:** [ScanNet++ Terms of Use PDF](https://kaldir.vc.in.tum.de/scannetpp/static/scannetpp-terms-of-use.pdf)
  - (1) Use is limited to "non-commercial research and educational purposes".
  - (3) The researcher indemnifies TUM, including for "any copies of copyrighted 3D models that he or she may create from the Database".
  - (4) The researcher may share the data only with associates who "also agreed to and signed these terms"; "Sharing the data otherwise is strictly prohibited".
  - (5) There is a GDPR deletion duty.
  - (6) TUM can terminate access at any time.
  - The PI/supervisor must sign by hand ("Digital signatures cannot be accepted"). Only established researchers (postdoc or above) may apply independently, so a PhD student must apply with the supervisor.
- **Replica** (Facebook research terms): the researcher "may use, modify, improve and/or publish the Dataset only in connection with a research or educational purpose that is non-commercial". Associates must agree to the terms first. Publishing derived work for non-commercial research is therefore explicitly allowed. — [Replica LICENSE](https://raw.githubusercontent.com/facebookresearch/Replica-Dataset/main/LICENSE)
- **HM3D:** "1,000 high-resolution 3D scans … free … for academic, non-commercial research". — [HM3D page](https://aihabitat.org/datasets/hm3d/)
- **Matterport EULA for academic use** (governs HM3D and MP3D):
  - Data is "for non-commercial academic use only".
  - "Matterport Dataset Derived Information" explicitly includes "any models trained on the Matterport Dataset".
  - Anyone publishing or distributing the dataset or derived information must include the Agreement or a link to it.
  - Distributing a "substantial portion" requires a signed or "click-wrap" agreement that records each recipient.
  - Papers must attribute Matterport.
  - Sources: [Matterport EULA (web)](https://matterport.com/matterport-end-user-license-agreement-academic-use-model-data); MP3D version dated Aug 29 2017: [MP_TOS.pdf](https://kaldir.vc.in.tum.de/matterport/MP_TOS.pdf)
- **Gibson:** download goes through a Google form that "will first take you to the license agreement". The MP3D-for-Gibson route needs the signed Matterport ToU. — [GibsonEnv data README](https://raw.githubusercontent.com/StanfordVL/GibsonEnv/master/gibson/data/README.md)
- **ARKitScenes:**
  - 5,047 captures of 1,661 scenes with the iPad Pro LiDAR.
  - Also "high resolution depth maps captured using a stationary laser scanner". The HR/LR subset covers 2,257 captures of 841 scenes.
  - Source: [ARKitScenes README](https://raw.githubusercontent.com/apple/ARKitScenes/main/README.md)
  - The repo LICENSE is Apple's licence for "the Apple Software", granting a "personal, non-commercial" licence to use, reproduce, modify and redistribute for non-commercial purposes. — [ARKitScenes LICENSE](https://raw.githubusercontent.com/apple/ARKitScenes/main/LICENSE)
- **MuSHRoom:** [MuSHRoom README](https://raw.githubusercontent.com/TUTvision/MuSHRoom/main/README.md)
  - Each room has an iPhone capture and a Kinect capture (long and short sequences), plus `gt_mesh.ply` / `gt_pd.ply` "reference mesh used for geometry comparison" with ICP alignments. A test "with a different sequence" is built in.
  - It is supported in the dn-splatter / nerfstudio dataparsers.
  - The Zenodo record of the iPhone COLMAP-pose version is licensed **cc-by-4.0**. — [Zenodo 13986996](https://zenodo.org/records/13986996)
- **Precedent for this pairing with navigation:** EmbodiedSplat uses iPhone captures, reconstructs meshes "via GS" and trains in Habitat-Sim. It compares against zero-shot policies pre-trained on HM3D and HSSD. — [arXiv:2509.17430](https://arxiv.org/abs/2509.17430)

### Inferences
- ScanNet++ is the right primary dataset. Because of ToU item 4, the IPB should say "code and evaluation protocol released; derived scene assets shared only with ScanNet++-licensed users (or not at all)". The supervisor (Kajdanowicz) must hand-sign the application, so do this early in semester 3.
- ScanNet++ already has a phone-train / DSLR-test benchmark (Oct 2025). This supports the "separate capture vs reference" protocol, and it can be cited as precedent. It also means the NVS-quality part of Stage 1 is no longer novel on its own; the novelty must be in navigation relevance.
- MuSHRoom (CC-BY-4.0) is the best candidate for a *second* testbed whose derived twins could legally be released. It has only about 10 rooms, which is not enough for the ≥ 20-scene protocol.
- Replica and HM3D suit pre-training and ablations but offer no separate cheap capture. They could only serve as "reality" with a *simulated* cheap capture, which makes the protocol circular.

### Gaps
- The exact ScanNet++ v2 scene count was not retrieved (the site says "1000+"; commonly cited as 1006). It is not known whether ScanNet++ lets authors release trained 3DGS models or meshes; the ToU is silent on "derived data". Ask TUM (scannetpp contact).
- The ARKitScenes *data* licence was not found. The repo LICENSE text covers "Apple Software" and does not explicitly name the data. Whether the ARKitScenes laser scans are full scene meshes (vs depth maps) and are usable as a navigation "reality" was not verified.
- The MuSHRoom scene count and the reference scanner model (e.g. Faro) were not confirmed from primary text in this session. The licence of the original (non-Zenodo) MuSHRoom release was not checked.
- The Gibson licence text itself sits behind a Google form and was not read.

## Q2. Real-world navigation datasets with real outcomes, and published paired sim/real navigation evaluations

### Takeaway
The GNM/ViNT/NoMaD training mixture is public (RECON, TartanDrive, SCAND, GoStanford2, SACSoN/HuRoN) and at least RECON and TartanDrive tooling are MIT. However, these are *teleoperated or autonomous logs*, not paired sim/real success evaluations. Paired sim-vs-real navigation evaluations do exist:
- **Sim2Real Predictivity:** Habitat + LoCoBot; SRCC_Succ goes from 0.18 to 0.844 after tuning.
- **EmbodiedSplat:** sim-vs-real correlation of 0.87–0.97 on GS meshes.
- **Vid2Sim / VR-Robo / ReaDy-Go:** real-robot results for twin-trained policies.

None of them releases paired data at the scale needed to replace a robot. They are precedents and baselines, not substitutes.

### Cited Findings
- **ViNT/NoMaD training datasets:** the visualnav-transformer README lists RECON, TartanDrive, SCAND, GoStanford2 (Modified), SACSoN/HuRoN, and says "please contact the respective authors for access to the unreleased data". Repo licence MIT, last push Sep 2024. — [visualnav-transformer README](https://raw.githubusercontent.com/robodhruv/visualnav-transformer/main/README.md); GitHub API (`gh api repos/robodhruv/visualnav-transformer`)
- **ViNT scale:** trained on "hundreds of hours of robotic navigation from a variety of different robotic platforms". — [arXiv:2306.14846](https://arxiv.org/abs/2306.14846)
- **NoMaD:** a unified diffusion policy for goal-reaching and exploration, evaluated on a real mobile robot. — [arXiv:2310.07896](https://arxiv.org/abs/2310.07896)
- **RECON:** 50 GB; "released under the MIT License". — [RECON dataset page](https://sites.google.com/view/recon-robot/dataset); paper [arXiv:2104.05859](https://arxiv.org/abs/2104.05859)
- **SCAND:** [SCAND site](https://www.cs.utexas.edu/~xiao/SCAND/SCAND.html)
  - 25 miles and 8.7 h, 138 trajectories, 15 days, Jackal + Spot, indoor and outdoor at UT Austin, mild to heavy crowds.
  - Includes a BC-vs-move_base real human-subject trial.
- **TartanDrive** tooling repo (castacks/tartan_drive) is MIT. — GitHub API (`gh api repos/castacks/tartan_drive`)
- **Sim2Real Predictivity (Kadian et al.):** [arXiv:1912.06321](https://arxiv.org/abs/1912.06321)
  - A 3D-scanned lab replica was used, with "parallel tests of 9 different models in reality and simulation".
  - SRCC for Habitat as in CVPR19 was "low (0.18 for the success metric)", due to agents "abusing collision dynamics to 'slide' along walls".
  - Tuning simulation parameters improved SRCC_Succ "from 0.18 to 0.844".
- **EmbodiedSplat:** iPhone capture → GS mesh → Habitat. Fine-tuned agents gain +20% and +40% absolute success over HM3D- and HSSD-pretrained zero-shot baselines on real ImageNav, with "sim-vs-real correlation (0.87-0.97)". — [arXiv:2509.17430](https://arxiv.org/abs/2509.17430)
- **Vid2Sim:** a monocular video becomes an interactable 3DGS sim for RL urban navigation, with +31.2% (twin) and +68.3% (real) success vs prior sim methods. — [arXiv:2501.06693](https://arxiv.org/abs/2501.06693)
- **VR-Robo:** a 3DGS digital twin with mesh physics gives RGB-only sim-to-real transfer for a goal-tracking task (legged). — [arXiv:2502.01536](https://arxiv.org/abs/2502.01536)

### Inferences
- For §9, Kadian et al. and EmbodiedSplat are the natural citations that "sim-vs-real correlation" is a measurable quantity. Kadian's wall-sliding finding directly motivates the "physical part" of the twin (collision and actuation model).
- The real-log datasets (RECON, SCAND, etc.) can serve as pre-training or co-training data and as the "real data only" comparator's data source, but none gives outcomes *in the ScanNet++ scenes*. The real-only baseline in the proxy protocol must still come from reference-scene demonstrations.

### Gaps
- The SCAND licence could not be read: the Texas Data Repository returned 403. The GoStanford2 and SACSoN/HuRoN licences were not checked.
- No published dataset was found that pairs *the same policy's* real-robot outcomes with a public twin of the *same* space at scale. Kadian et al. used 1 lab and EmbodiedSplat a few scenes; it was not verified whether their paired data are released.

## Q3. Simulators and tools: maturity and GPU needs

### Takeaway
Habitat-Sim/Lab (MIT; v0.3.3 / v0.3.4 in 2026), gsplat (Apache-2.0, active) and COLMAP 4.x (with GLOMAP now merged as the "global" mapper) are mature and run on the data-centre GPUs of PLGrid/WCSS. **Isaac Sim officially does not support GPUs without RT cores (A100, H100).** That rules it out on Lem (H100), Athena (A100) and very likely Helios (GH200/Hopper). NuRec's 3DGS-in-Isaac path therefore needs RTX workstation GPUs. GaussGym is a research release (paper Oct 2025); SplatGym is a small, stale repo. Nerfstudio has not had a release since Nov 2024.

### Cited Findings
- **Habitat-Sim:** MIT, latest release v0.3.3 (2026-02-12), ~3.8k stars, last push 2026-07-21.
- **Habitat-Lab:** MIT, v0.3.4 (2026-05-07).
- Source for both: GitHub API (`api.github.com/repos/facebookresearch/habitat-sim`, `…/habitat-lab`).
- **Isaac Sim:** v6.1.0 (2026-09-10). **Isaac Lab:** BSD-3-Clause, v3.0.0-EA (2026-09-16). — GitHub API (`isaac-sim/IsaacSim`, `isaac-sim/IsaacLab`)
- **Isaac Sim requirements:** [Isaac Sim requirements](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html)
  - Minimum GeForce RTX 4080 with 16 GB; ideal RTX PRO 6000 Blackwell with 48 GB.
  - "GPUs without RT Cores (A100, H100) are not supported".
  - "Isaac Lab usage will require additional RAM and VRAM".
  - The container is Linux-only.
- **Omniverse NuRec:** "3D Gaussian splatting libraries that ingest real sensor data to reconstruct and render interactive simulation in OpenUSD", integrated with Isaac Sim. — [NVIDIA NuRec](https://developer.nvidia.com/omniverse/nurec); Isaac Sim doc page "Neural Volume Rendering": [Isaac Sim 6.0 NuRec docs](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/assets/usd_assets_nurec.html)
- **GaussGym:** [arXiv:2510.15352](https://arxiv.org/abs/2510.15352)
  - Integrates 3DGS "as a drop-in renderer within vectorized physics simulators such as IsaacGym", at ">100,000 steps per second on consumer GPUs".
  - Ingests "iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit)".
  - Code at escontrela.me/gauss_gym.
- **SplatGym** (SplatLearn/SplatGym): Apache-2.0, 16 stars, last push 2025-01-08. — GitHub search API
- **gsplat:** Apache-2.0, v1.5.3, last push 2026-09-19, ~5.7k stars. — GitHub API. gsplat claims "up to 4x less GPU memory with up to 15% less time" vs the official 3DGS. — [gsplat repo](https://github.com/nerfstudio-project/gsplat)
- **nerfstudio:** Apache-2.0, latest release v1.1.5 (2024-11-11), last push 2025-07-29. — GitHub API
- **COLMAP:** 4.2.0 (2026-09-01). GLOMAP README: "[DEPRECATED] … fully migrated to COLMAP, where GLOMAP functionality is exposed as the 'global' mapper". GLOMAP is "typically 1-2 orders of magnitude faster" than COLMAP incremental SfM. — [GLOMAP README](https://raw.githubusercontent.com/colmap/glomap/main/README.md); GitHub API
- **Other GS-to-sim systems for navigation:**
  - GASE (panoramic camera arrays; GS scenes imported into physics simulators): real deployments for manipulation and navigation are within <10% of real-data-trained policies; "Code will be released". — [arXiv:2606.17520](https://arxiv.org/abs/2606.17520)
  - Image2Sim: a feed-forward feature-Gaussian model plus a one-step pixel-flow renderer from posed RGB-D, ~20K interactive environments. — [arXiv:2607.05765](https://arxiv.org/abs/2607.05765)

### Inferences
- The safest stack on PLGrid/WCSS is: COLMAP 4.x (global mapper) or the ScanNet++ poses → gsplat 3DGS → mesh extraction (as in EmbodiedSplat) → Habitat-Sim headless on H100/A100. It stays on MIT/Apache/BSD code.
- Isaac Sim/Lab with NuRec would need a local RTX workstation (≥ 16 GB, realistically 48 GB). This belongs in the §12 risk / equipment budget (e.g. a Minigrant or PRELUDIUM equipment line), or should be avoided.
- The IPB wording "run as a mesh in the simulator or rendered directly" is feasible. Direct 3DGS rendering inside Habitat is not a built-in feature, so "rendered directly" means a custom gsplat render loop (as GaussGym does with IsaacGym). That is extra engineering.

### Gaps
- The GaussGym GitHub repo, its licence and whether it still depends on the deprecated IsaacGym Preview were not verified (GitHub search found only kerrj/nerfstudio-gaussgym, Apache-2.0).
- Whether Habitat-Sim EGL rendering works on Helios GH200 (ARM CPU, aarch64) was not verified. Assume Lem or Athena (x86).
- The NuRec licence terms for academic use were not read.

## Q4. Compute: GPU-hours and PLGrid/WCSS availability

### Takeaway
Reference points:
- **DD-PPO PointNav:** 2.5B frames took ">6 months of GPU-time" (64 GPUs, <3 days). But "90% of peak performance" came at 100M steps in "under 1 day with 8 GPUs", i.e. roughly 192 GPU-h.
- **3DGS:** 35–45 min per scene on an A6000 in the original paper. SceneSplat-7K needed about 150 L4-GPU-days for ~7.9k indoor scenes, i.e. about 27 GPU-min per scene.

A few dozen ScanNet++ twins at several capture budgets are therefore cheap (tens to low hundreds of GPU-h). RL from scratch is the expensive part; fine-tuning a pretrained policy is cheaper. PLGrid grants are open to doctoral students. Lem has 304 H100s (per resources.md).

### Cited Findings
- **DD-PPO:** 2.5B steps; "over 6 months of GPU-time training in under 3 days of wall-clock time with 64 GPUs"; "90% of peak performance is obtained … at 100 million steps … under 1 day with 8 GPUs"; 107× speedup on 128 GPUs. — [arXiv:1911.00357](https://arxiv.org/abs/1911.00357)
- **Original 3DGS:** "35-45 minutes" average training (A6000-class). — [arXiv:2308.04079](https://arxiv.org/pdf/2308.04079) (via search snippet; consistent with the paper)
- **SceneSplat-7K:** 7,916 indoor scenes (incl. ScanNet++, ARKitScenes, Matterport3D), 11.27B Gaussians, "150 GPU-days on one NVIDIA L4 GPU", mean PSNR 29.64 dB. — [HF GaussianWorld/scene_splat_7k](https://huggingface.co/datasets/GaussianWorld/scene_splat_7k)
- **FastGS** claims 3DGS training "in 100 Seconds". — [arXiv:2511.04283](https://arxiv.org/pdf/2511.04283) (title only; not read in detail)
- **PLGrid:**
  - PLGrid grants are open to doctoral students.
  - Athena and Helios access requires a PLGrid computing grant via the portal.
  - Helios grants must list related projects and a cooperant from the HPC centre.
  - Athena is GPU-only; Helios GPUs are GH200 (Grace ARM + Hopper).
  - Sources: [PLGrid grants](https://guide.plgrid.pl/pl/grants/plgrid), [Helios docs](https://docs.hpc.cyfronet.pl/supercomputers/helios/), [Athena docs](https://docs.hpc.cyfronet.pl/supercomputers/athena/)
- **Repo claims about WCSS Lem** (76 nodes × 4 H100 96 GB; 3/7-day queues; e-science.pl "Przetwórz na superkomputerze" open to doctoral students with a supervisor) are recorded with URLs in research/resources.md §2. They were not re-fetched here and are consistent with the PLGrid Lem entry it cites.

### Inferences
- **Budget sketch (our estimate, not sourced):**
  - 20–40 scenes × ≥ 4 capture budgets × 2 references ≈ 160–320 3DGS fits at ~0.5–1 GPU-h each, i.e. ≤ ~300 GPU-h.
  - RL/IL fine-tuning of a small navigation policy per twin at DD-PPO's "90%" scale (~200 GPU-h) × tens of configurations lands at the 10³–10⁴ GPU-h level.
  - This fits a standard PLGrid/WCSS grant. The earlier ~23k H100-h 7B-VLA estimate (vla-wm-crowdedness.md) is the high end, and §9 v6 rightly dropped it.
- Use GNM/ViNT/NoMaD-size models (tens of millions of parameters) for most runs, and reserve VLAs for a small final comparison.

### Gaps
- No primary figure was found for the GPU-hours needed to fine-tune ViNT/NoMaD. The README gives no compute numbers.
- The typical size of a PLGrid grant awarded to a doctoral student (GPU-h) is not public in the pages read.

## Q5. Low-cost real validation options

### Takeaway
A TurtleBot 4 Lite costs about €1,699 incl. VAT (EU retailer, pre-order); the 2022 launch price was $1,195 Lite / $1,850 Standard. That is within an SzD Minigrant (≤ 20k PLN) or the PRELUDIUM equipment line. Alternatives: K29 "Denali" Pioneer 3-DX (ROS 2, remote access, per resources.md) or phone-based evaluation. The ~8 robot-hours per campaign in §9 is small enough for borrowed equipment.

### Cited Findings
- **TurtleBot 4 launch prices:** "$1,195 for the Lite and $1,850 for the Standard" (2022). The Lite has an IMU, optical floor tracking, 2D LiDAR and an OAK-D-Lite; the Standard has an OAK-D-Pro plus a display and expansion. — [Clearpath launch blog (2022)](https://clearpathrobotics.com/blog/2022/05/clearpath-robotics-launches-turtlebot-4/) (via search snippet); [Hackster.io](https://www.hackster.io/news/clearpath-robotics-launches-the-turtlebot-4-offering-an-affordable-autonomous-ros-2-robot-platform-6bc3d6a10cbd)
- **Current EU retail:** TurtleBot 4 Lite "Pre-order € 1.699,00 (incl. VAT)". — [Elektor](https://www.elektor.com/products/clearpath-robotics-turtlebot-4-lite)
- **Precedents with cheap phone capture and a small robot:**
  - EmbodiedSplat (iPhone capture; real ImageNav). — [arXiv:2509.17430](https://arxiv.org/abs/2509.17430)
  - Kadian et al. (LoCoBot, a low-cost platform, with the HaPy bridge running "identical code on simulated agents and robots"). — [arXiv:1912.06321](https://arxiv.org/abs/1912.06321)
- **PWr options:** K29 Denali robots and SzD Minigranty up to 20,000 PLN. See research/resources.md §1 and §5 (sources there: https://denali.kcir.pwr.edu.pl/robots.php, https://szd.pwr.edu.pl/doktoranci/minigranty).

### Inferences
- The TurtleBot 4 Lite's OAK-D-Lite gives RGB-D at a camera height similar to LoCoBot-class robots used in Habitat studies. It is a good match for the "robot-camera model" in the proxy.
- "Phone-based evaluation" (a person carrying a phone and executing the policy's actions) can check the perception side but not collisions or actuation noise. Use it only as a pilot, not as the H-test.

### Gaps
- The current Clearpath list price in 2026 was not confirmed (the Clearpath 2025 comparison blog did not expose a price). Polish distributor pricing and lead time were not checked.
- Whether the Denali robots carry RGB-D cameras (UNVERIFIED in resources.md) remains open.

## Q6. Key open problems and risks, with mitigations

### Takeaway
The main scientific risk is proxy validity: a laser-scan + DSLR mesh rendered in Habitat is itself a simulator, so gains measured against it may not transfer. Kadian et al. show that simulator artefacts (wall sliding) can destroy sim/real rank correlation. The main strategic risk is crowding: at least six 2025–2026 papers do GS-based real-to-sim navigation (EmbodiedSplat, Vid2Sim, VR-Robo, ReaDy-Go, GASE, Image2Sim), and GaussGym/NuRec come from large labs. A budget/allocation angle (how little real data is needed) is still less covered. Licensing limits the release of reproducible artefacts.

### Cited Findings
- **Proxy validity / physics gap:**
  - Habitat's original collision dynamics let agents "'slide' along walls, leading to shortcuts"; SRCC_Succ was 0.18 and rose to 0.844 only after tuning sim parameters. — [arXiv:1912.06321](https://arxiv.org/abs/1912.06321)
  - EmbodiedSplat reports that sim-vs-real correlation depends on the mesh reconstruction technique (0.87–0.97 for its GS meshes). — [arXiv:2509.17430](https://arxiv.org/abs/2509.17430)
- **Dynamic obstacles and humans:** ReaDy-Go notes that "prior GS-based works have considered only static scenes or non-photorealistic human obstacles". It adds animatable human GS avatars and reports gains in sim and real with moving obstacles. SCAND gives real crowd-navigation demonstrations. — [arXiv:2602.11575](https://arxiv.org/abs/2602.11575); [SCAND](https://www.cs.utexas.edu/~xiao/SCAND/SCAND.html)
- **Crowding and scooping:**
  - Vid2Sim (Jan 2025): [arXiv:2501.06693](https://arxiv.org/abs/2501.06693)
  - VR-Robo (Feb 2025): [arXiv:2502.01536](https://arxiv.org/abs/2502.01536)
  - EmbodiedSplat (Sep 2025): [arXiv:2509.17430](https://arxiv.org/abs/2509.17430)
  - GaussGym (Oct 2025): [arXiv:2510.15352](https://arxiv.org/abs/2510.15352)
  - ReaDy-Go (Feb 2026): [arXiv:2602.11575](https://arxiv.org/abs/2602.11575)
  - GASE (Jun 2026): [arXiv:2606.17520](https://arxiv.org/abs/2606.17520)
  - Image2Sim (Jul 2026): [arXiv:2607.05765](https://arxiv.org/abs/2607.05765)
  - NVIDIA NuRec in Isaac Sim: [NuRec](https://developer.nvidia.com/omniverse/nurec)
  - NavDP (sim-only training, zero-shot real, 1M+ m across 3,000 scenes): [arXiv:2505.08712](https://arxiv.org/abs/2505.08712)
- **Benchmark overlap:** the ScanNet++ iPhone NVS benchmark (Oct 2025) already evaluates phone-trained reconstructions against DSLR ground truth. — [ScanNet++ site](https://kaldir.vc.in.tum.de/scannetpp/)
- **Reproducibility and licensing:**
  - ScanNet++ forbids sharing with non-signatories and allows TUM to revoke access. — [ToU](https://kaldir.vc.in.tum.de/scannetpp/static/scannetpp-terms-of-use.pdf)
  - Matterport requires a click-wrap for substantial redistribution. — [Matterport EULA](https://matterport.com/matterport-end-user-license-agreement-academic-use-model-data)
  - nerfstudio releases have stalled since Nov 2024; GLOMAP is deprecated into COLMAP. — GitHub API; [GLOMAP README](https://raw.githubusercontent.com/colmap/glomap/main/README.md)
- **Tool/hardware lock-in:** Isaac Sim is unsupported on A100/H100. — [Isaac Sim requirements](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html)

### Inferences (risks → mitigations)
1. **Proxy ≠ reality.** Mitigations:
   - Report the proxy's photometric and geometric error to held-out DSLR images (already in §9).
   - Tune the reference's collision/actuation model first, following Kadian et al.
   - Pre-register SRCC between proxy and robot on the 2 PWr rooms as a validity check.
   - Keep conclusions phrased as "ranking-preserving", not absolute.
2. **Physics gap** (collisions, actuation, wheel slip are absent from meshes). Mitigations:
   - Use Habitat's non-sliding collision setting.
   - Keep actuation noise as a hidden parameter (as in §9).
   - Use the robot campaigns to estimate real noise.
3. **Dynamic obstacles and humans.** Scope the thesis explicitly to static indoor scenes, name dynamic humans as future work, and cite ReaDy-Go. Optionally, SCAND could be used for a small co-training check.
4. **Scooping.** Big labs own the *simulator/renderer* space (NVIDIA NuRec, GaussGym, Image2Sim). The IPB should differentiate on *allocation of real data* (task-aware capture, uncertainty-weighted randomization, active real-trial selection, and the budget curves H1–H4). Mitigations:
   - Run a quarterly arXiv watch on "real-to-sim navigation budget / active capture".
   - Publish H1 early (e.g. an RA-L submission) to stake the claim.
5. **Reproducibility.** Mitigations:
   - Release code, configs, scene IDs, seeds and pre-registrations, not ScanNet++-derived assets.
   - Add a MuSHRoom (CC-BY-4.0) or own-PWr-room demo whose twins can be released.
   - Pin COLMAP 4.x, gsplat and Habitat versions in containers.
6. **Compute/tool fit.** Stay on Habitat + gsplat (runs on H100/A100). Budget an RTX workstation only if Isaac/NuRec is needed.
7. **Access risk.** The ScanNet++ approval needs a handwritten supervisor signature and can be revoked. Apply in the first month and keep a fallback (MuSHRoom + ARKitScenes).

### Gaps
- No published study was found that directly measures whether a *laser-scan mesh* ranks navigation policies like the *real robot in the same space* (i.e. validates "laser-scan mesh as reality"). Kadian et al. used a scanned replica and robot but not the ScanNet++ capture pipeline. This is an open problem the thesis could partly address.
- The PolaRiS paper ("Scalable Real-to-Sim Evaluations for Generalist Robot Policies", [arXiv:2512.16881](https://arxiv.org/pdf/2512.16881)) was seen only by title. Its relevance (real-to-sim *evaluation* of policies) should be checked by the writer's team before citing.
- It was not verified whether EmbodiedSplat, Vid2Sim or ReaDy-Go study *how much* capture or real data is needed (budget curves). A targeted check of their experiments sections is recommended before claiming this niche is open.

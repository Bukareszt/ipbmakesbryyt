# Stage 1: real-world data → navigation-ready digital twin, with as little capture as possible (state of the art 2023–2026, as of 26 Sep 2026)

Verification method: every arXiv ID below was resolved through the arXiv API (title, authors, date, comment/journal-ref/DOI) on 2026-09-26; venues were cross-checked with the Semantic Scholar batch API or the project page. Where a venue could not be confirmed, it is marked "arXiv only". Numbers come from the papers' HTML full text (fetched) unless stated as abstract-only.

## Q1. Which methods build navigation-ready twins from phone / RGB-D / robot capture, and how much capture do they use?

### Takeaway
Navigation twins are now a standard recipe: 3DGS for appearance plus an extracted mesh (DN-Splatter, TSDF, NKSR, Polycam) for collision in Habitat-Sim / Isaac. Capture amounts vary widely and are almost never varied experimentally: 15 s / 450 frames per street scene (Vid2Sim), 20–30 min / 1000 frames per room (EmbodiedSplat), and "photos from iPad/iPhone" with no count (VR-Robo). No navigation-twin paper reports policy success as a function of capture amount.

### Cited Findings
**Reconstruction backbones (geometry for collision)**
- DN-Splatter (Turkulainen, Ren, Melekhov, Seiskari, et al.), arXiv:2403.17822, WACV 2025. It adds depth and normal priors to 3DGS and uses an adaptive depth loss on indoor scenes, enabling "direct mesh extraction from the Gaussian representation, yielding more physically accurate reconstructions of indoor scenes" — [arXiv](https://arxiv.org/abs/2403.17822)
- SuGaR (Guédon, Lepetit), arXiv:2311.12775, CVPR 2024, doi:10.1109/CVPR52733.2024.00512. Surface-aligned Gaussians give mesh extraction — [arXiv](https://arxiv.org/abs/2311.12775); [Semantic Scholar record](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2311.12775)
- 2D Gaussian Splatting (Huang, Yu, Chen, Geiger, Gao), arXiv:2403.17888, SIGGRAPH 2024, doi:10.1145/3641519.3657428. It gives geometrically accurate radiance fields — [arXiv](https://arxiv.org/abs/2403.17888)
- Splat-Nav (Chen, Shorinwa, Bruno, Swann, et al.), arXiv:2403.02751, IEEE T-RO 2025, doi:10.1109/TRO.2025.3552348. Safe real-time planning directly in a Gaussian Splatting map, with no mesh — [arXiv](https://arxiv.org/abs/2403.02751)

**Navigation twins and how much capture they use**
- EmbodiedSplat (Chhablani, Ye, Irshad, Kira), arXiv:2509.17430, ICCV 2025 (doi:10.1109/ICCV51701.2025.02359 per the repo's earlier Crossref check in research/review-1-resolution.md). It is the closest indoor match: iPhone 13 Pro Max + Polycam; "each capture requires 20–30 minutes of recording"; "1000 aligned RGB-depth frames" selected by Nerfstudio; DN-Splatter trained for 30k iterations (1–2 h); meshes loaded into Habitat-Sim; 4 own scenes + 3 MuSHRoom scenes — [arXiv HTML](https://arxiv.org/html/2509.17430v2)
- EmbodiedSplat results: fine-tuning gives +20 pp (vs HM3D zero-shot) and +40 pp (vs HSSD zero-shot) absolute real-world ImageNav success; sim-vs-real correlation 0.87–0.97; the real test was 10 episodes in one scene (lounge) on a Stretch robot (HM3D zero-shot 50% → fine-tuned 70%) — [arXiv HTML](https://arxiv.org/html/2509.17430v2)
- EmbodiedSplat reports a positive link between reconstruction quality and success: "higher validation PSNR values correspond to improved success rates"; zero-shot SR "is inversely correlated with the scale of the scene, while directly correlated with val. PSNR"; gimbal-stabilised MuSHRoom captures reached 95% zero-shot SR in small scenes. DN and Polycam meshes both give ~60% zero-shot SR in sim, but for policies trained from scratch on one scene, real-world SR was 50% (Polycam) vs 10% (DN) — [arXiv HTML](https://arxiv.org/html/2509.17430v2)
- Vid2Sim (Xie, Liu, Peng, Wu, Zhou), arXiv:2501.06693, CVPR 2025, doi:10.1109/CVPR52734.2025.00155. Urban navigation from "15 seconds of forward-facing video recorded at 30 fps, providing 450 frames per scene" (393 train / 57 test); 30 scenes from 9 web videos; GS for rendering plus a TSDF mesh (voxel 0.1) for collision; 81.6% PointNav / 74.4% SocialNav in sim; real zero-shot 85% / 65% / 55% (straight / static / dynamic obstacle). A single-environment agent scored 0%. Gains grow with the number of scenes (1→5→15→25→30) — [arXiv HTML](https://arxiv.org/html/2501.06693v2)
- VR-Robo (Zhu, Mou, Li, Ye, et al.), arXiv:2502.01536, IEEE RA-L 2025, doi:10.1109/LRA.2025.3575648. Photos from iPad/iPhone → COLMAP → geometry-consistent GS; TSDF mesh for Isaac Sim physics; 6 indoor rooms; real success 93–100% on cone-reaching with a quadruped. The paper states no image count and has no ablation on capture amount — [arXiv HTML](https://arxiv.org/html/2502.01536v3)
- GaussGym (Escontrela, Kerr, Allshire, Frey, et al.), arXiv:2510.15352, arXiv only (2025). Inputs: ARKitScenes, GrandTour, smartphone captures, even Veo-generated video. VGGT gives poses and points, splats are initialised from them, and the collision mesh comes from NKSR. It notes "assets … are initialized with uniform physical parameters (e.g., friction)". Real-world result: zero-shot stair climbing, but "a decline in the precise foot placement" — [arXiv HTML](https://arxiv.org/html/2510.15352v1)
- ReaDy-Go (Yoo, Jang, Kim, Han, Jung, Kim), arXiv:2602.11575, IEEE RA-L 2026, doi:10.1109/LRA.2026.3707355. A static GS scene plus animatable human GS avatars for dynamic-obstacle visual navigation — [arXiv](https://arxiv.org/abs/2602.11575)
- GASE (Zhang, Yan, Liang, Xu, et al.), arXiv:2606.17520, arXiv only. It targets "inefficient data acquisition" using panoramic camera arrays; object/background separation and inpainting. The abstract claims a real-robot gap of "less than 10%" vs policies trained on real data, for manipulation and navigation — [arXiv](https://arxiv.org/abs/2606.17520)
- Image2Sim (Wang, Lee, Xu, Lee), arXiv:2607.05765, arXiv only. Feed-forward feature Gaussians from posed RGB-D, plus a one-step pixel-flow renderer; ~20K scenes and >10M navigation samples (abstract) — [arXiv](https://arxiv.org/abs/2607.05765)
- Feed-forward, sparse input: InstantSplat (Fan, Cong, Wen, Wang, et al.), arXiv:2403.20309, gives "sparse-view Gaussian splatting in seconds"; S2 lists no venue — [arXiv](https://arxiv.org/abs/2403.20309)
- Evaluation substrate: ScanNet++ (Yeshwanth, Liu, Nießner, Dai), arXiv:2308.11417, ICCV 2023. Each scene has laser scan + DSLR + iPhone RGB-D; 460 scenes; >3.7M iPhone RGB-D frames. This allows commodity-capture twins to be compared against a high-fidelity reference — [arXiv](https://arxiv.org/abs/2308.11417)
- Older anchor: NeRF2Real (Byravan, Humplik, Hasenclever, Brussee, et al.), arXiv:2210.04932 (2022). NeRF from phone video for bipedal vision-guided skills — [arXiv](https://arxiv.org/abs/2210.04932)

### Inferences
- Capture budgets span roughly 450 frames (15 s) to 1000 frames (20–30 min) per scene. Each paper uses one fixed budget. The "uniform capture" baseline in H1 has a natural instantiation: uniform temporal subsampling of an EmbodiedSplat-style iPhone/Polycam stream, or of ScanNet++ iPhone streams.
- EmbodiedSplat's PSNR–SR correlation and its capture-stability effect suggest that capture quality matters for navigation. They also show that image PSNR is only a proxy: in the overfitting experiment, Polycam vs DN meshes flip the real-world result. This argues for a task-level objective.

### Gaps
- No navigation-twin paper found gives policy success vs number of frames or capture minutes. VR-Robo and GaussGym do not even report frame counts.
- I did not open the PDFs of GASE or Image2Sim to extract their capture amounts. Only abstracts were read.

## Q2. Active / next-best-view capture and uncertainty for radiance fields: does any of it optimise for a downstream policy or task?

### Takeaway
Uncertainty-driven view selection for NeRF/3DGS is mature. Its evidence is Fisher information (FisherRF), perturbation fields (Bayes' Rays), learned variance (ActiveNeRF) and VLM priors (AREA3D). A 2024–2026 wave adds *task-relevance weighting* (risk regions along a path, language queries, VLM semantics). None of the verified works uses the success of a navigation policy trained in the resulting twin as the selection objective or evaluation metric. All of them evaluate reconstruction quality (PSNR, W2 in risk regions, ROI PSNR) or online exploration/search success.

### Cited Findings
**Task-blind uncertainty and next-best-view**
- ActiveNeRF (Pan, Lai, Song, Huang), arXiv:2209.08546, ECCV 2022. It learns rendering uncertainty to rank candidate views — [arXiv](https://arxiv.org/abs/2209.08546)
- Bayes' Rays (Goli, Reading, Sellán, Jacobson, Tagliasacchi), arXiv:2309.03185, CVPR 2024, doi:10.1109/CVPR52733.2024.01896. Post-hoc uncertainty for a trained NeRF via a perturbation field — [arXiv](https://arxiv.org/abs/2309.03185)
- FisherRF (Jiang, Lei, Daniilidis), arXiv:2311.17874, ECCV 2024 (Oral) per the project page. It maximises expected information gain from the Fisher information of radiance-field parameters — [arXiv](https://arxiv.org/abs/2311.17874); [project page](https://jiangwenpl.github.io/FisherRF/)
- FisherRF protocol and numbers: 4 uniform initial views, grown to 20 views. On Blender with sequential selection, PSNR is 29.525 vs 28.732 (random) and 26.610 (ActiveNeRF), i.e. +0.79 dB over random. With batch selection, 29.094 vs 27.135 random (+1.96 dB). On Mip-NeRF360 (batch), 20.568 vs 19.542 random and 18.303 ActiveNeRF. View scoring runs at ~70 fps with 3DGS — [arXiv HTML](https://arxiv.org/html/2311.17874v2)
- GenNBV (Chen, Li, Wang, Xue, et al.), arXiv:2402.16174, CVPR 2024. An RL-learned, generalisable NBV policy for active 3D reconstruction — [arXiv](https://arxiv.org/abs/2402.16174)
- NARUTO (Feng, Zhan, Chen, Yan, et al.), arXiv:2402.18771, CVPR 2024, doi:10.1109/CVPR52733.2024.02038. Neural active reconstruction driven by uncertainty — [arXiv](https://arxiv.org/abs/2402.18771)
- Active Neural Mapping (Yan, Yang, Zha), arXiv:2308.16246, ICCV 2023 — [arXiv](https://arxiv.org/abs/2308.16246)
- ActiveGS (Jin, Zhong, Pan, Behley, et al.), arXiv:2412.17769, IEEE RA-L 2025, doi:10.1109/LRA.2025.3555149 — [arXiv](https://arxiv.org/abs/2412.17769)
- Li, Jiang, Daniilidis, "Next Best View Selections for Semantic and Dynamic 3D Gaussian Splatting", arXiv:2512.22771, arXiv only. It extends Fisher-information selection to semantic Gaussians and deformation networks. It is evaluated on rendering quality and segmentation — [arXiv](https://arxiv.org/abs/2512.22771)

**Task-relevance- or VLM-weighted capture (closest to H1)**
- Liu, Jiang, Lei, Pandey, Daniilidis, Figueroa (RaEM), "Beyond Uncertainty: Risk-Aware Active View Acquisition for Safe Robot Navigation and 3D Scene Understanding with FisherRF", arXiv:2403.11396, arXiv only per Semantic Scholar. It weights FisherRF by risk regions around a planned path. Setup: Habitat + Matterport3D, 10 waypoints, 11 views total from 250 candidates. It lowers the W2 distance in safety-critical regions by 24.26% (FisherRF) and 17.63% (ray entropy). It **does not measure navigation success** of a policy — [arXiv HTML](https://arxiv.org/html/2403.11396v2)
- AREA3D (Xu, Gan, Gu, Li, Zhan, Pfister), arXiv:2512.05131, CVPR 2026 (journal-ref in the arXiv record). It uses feed-forward 3D perception plus VLM guidance, with the VLM labelling uncertainty regions as occlusion/geometric/lighting/boundary/texture. Replica scenes: 15 initial views and a 40-view budget; room0 PSNR is 29.23 vs FisherRF 29.11 vs random 28.17. It measures no downstream robot task — [arXiv HTML](https://arxiv.org/html/2512.05131v2)
- VISTA (Nagami, Chen, Yu, Shorinwa, et al.), arXiv:2507.01125, IEEE RA-L 2026, doi:10.1109/LRA.2026.3653276. Open-vocabulary, task-relevant exploration with online semantic 3DGS. Its viewpoint-semantic coverage metric beats FisherRF and Bayes' Rays in speed and reconstruction quality, and it gets "6x higher success rates in challenging maps" (search task, quadrotor) — [arXiv](https://arxiv.org/abs/2507.01125)
- GaussLite (Thomas, Peterson, How), arXiv:2606.30809, arXiv only (June 2026). Task-conditioned 3DGS mapping: an LLM parses the task, and the seeding density and gradients follow task relevance. It gains +2.72 dB ROI PSNR on Replica at a matched Gaussian budget. This shifts *representation capacity*, not *capture* — [arXiv](https://arxiv.org/abs/2606.30809)
- ATLAS Navigator (Ong, Tao, Murali, Spasojevic, et al.), arXiv:2502.20386, doi:10.1109/TFR.2026.3732100. Task-driven, language-embedded GS for online semantic navigation, over >2 km and 47,000 m²; ~59% competitive ratio vs the shortest path — [arXiv](https://arxiv.org/abs/2502.20386)
- Zeng et al., multi-robot 3DGS reconstruction with semantic guidance, arXiv:2412.02249, arXiv only. It focuses view sampling on regions with high instance uncertainty — [arXiv](https://arxiv.org/abs/2412.02249)
- Performance-guided refinement in a GS twin: FalconGym 2.0 (Miao, Yuceel, Fainekos, Hoxha, et al.), arXiv:2510.02248, arXiv only. It focuses *policy training* on hard tracks created by editing the GS scene; 98.6% real gate success (69/70). The loop is policy performance → training distribution, not → capture — [arXiv](https://arxiv.org/abs/2510.02248)

### Inferences
- The closest prior work splits along two axes. One axis is navigation-relevant weighting of capture (RaEM: path risk; VISTA/ATLAS: language query; AREA3D: VLM semantics). The other is policy-aware twin use (FalconGym 2.0, EmbodiedSplat). Nobody closes the loop "capture choice → twin → trained navigation policy → real success per unit of capture". This matches the repo's earlier niche count (research/niches-data.md: N1 "task-aware capture × policy" 0–2 papers/yr vs N1b active NBV 11→35/yr).
- H1 is **novel in its objective and metric, not in its ingredients**. Its comparators should be (i) uniform capture, (ii) FisherRF-type task-blind uncertainty, and (iii) RaEM/AREA3D-type task-weighted reconstruction objectives. Otherwise reviewers will say the task signal was not isolated.
- Crowding risk: Daniilidis's group (FisherRF → RaEM → semantic/dynamic NBV) and Stanford MSL (Splat-Nav → VISTA) are one step from evaluating policy success. The niche could close within 12–18 months.

### Gaps
- I found no paper that reports navigation-policy success vs number of actively selected views. Searches for "task-aware active view selection … policy" returned only reconstruction or online-exploration works.
- I did not verify the venues of RaEM or GaussLite beyond Semantic Scholar/arXiv (both appear arXiv-only).

## Q3. Sparse-view / few-shot reconstruction: how does quality degrade with fewer views? Are there curves?

### Takeaway
Quality degrades steeply below about 10 views per object-scale scene and with diminishing returns above that. Few-shot tables at 3/6/9 views are standard (LLFF/DTU). Indoor rooms need on the order of tens of images with depth priors versus hundreds without. No curve links view count to navigation success.

### Cited Findings
- DNGaussian (Li, Zhang, Bai, Zheng, et al.), arXiv:2403.06912, CVPR 2024, doi:10.1109/CVPR52733.2024.01963. LLFF PSNR at 3 / 6 / 9 views is 19.12 / 22.18 / 23.17 (SSIM 0.591 / 0.755 / 0.788). Vanilla 3DGS at 3 views scores 16.46 (LLFF) and 14.74 (DTU) vs DNGaussian 19.12 / 18.91. FreeNeRF at 3 views scores 19.63 (LLFF) and 19.92 (DTU). The authors note gains shrink by 9 views — [arXiv HTML](https://arxiv.org/html/2403.06912v3)
- So going from 3 → 6 views adds +3.06 dB and 6 → 9 adds +0.99 dB, a saturating curve (computed from the numbers above).
- FreeNeRF (Yang, Pavone, Wang), arXiv:2303.07418, CVPR 2023, doi:10.1109/CVPR52729.2023.00798. Frequency regularisation; the standard 3/6/9-view few-shot protocol on Blender, DTU and LLFF — [arXiv](https://arxiv.org/abs/2303.07418)
- FSGS (Zhu, Fan, Jiang, Wang), arXiv:2312.00451, ECCV 2024 per S2 — [arXiv](https://arxiv.org/abs/2312.00451); SparseGS (Xiong et al.), arXiv:2312.00206, 3DV 2025 — [arXiv](https://arxiv.org/abs/2312.00206)
- Room scale: Dense Depth Priors for NeRF (Roessle, Barron, Mildenhall, Srinivasan, Nießner), arXiv:2112.03288, CVPR 2022. Room NeRFs "typically [need] up to a few hundred images"; with depth priors, "as few as 18 images for an entire scene" (ScanNet) — [arXiv](https://arxiv.org/abs/2112.03288)
- Indoor sparse-view 3DGS is an active 2025–2026 topic (e.g. SPC-GS arXiv:2503.12535; FreeSplat++ arXiv:2503.22986; PanoPlane arXiv:2605.14135). A search found typical ScanNet protocols such as "12 evenly sampled sparse views". I did not verify these individually — [search result: SPC-GS](https://arxiv.org/html/2503.12535)
- FisherRF shows the budget interaction: at 20 views, active selection is +0.8 to +2.0 dB over random on Blender and +1.0 dB on Mip-NeRF360 — [arXiv HTML](https://arxiv.org/html/2311.17874v2)

### Inferences
- The saturating PSNR-vs-views curve is exactly what makes a ≥40% saving possible at the high-budget end. If a dense capture (e.g. 1000 frames) sits on the plateau, removing 40% of *uniformly* spaced frames may cost little. The H1 experiment must therefore fix the reference budget in the non-saturated region, or state that the saving is measured at a target success τ taken from the uniform curve (as the repo's §9 plans).
- Feed-forward reconstructors (VGGT in GaussGym, InstantSplat, AREA3D's backbone) move the knee of the curve to fewer views. This helps the "less capture" goal but narrows the gap between strategies.

### Gaps
- I did not verify any published curve of *navigation success or collision rate* vs number of views or capture minutes.
- I did not fetch ScanNet++-specific few-view NVS curves (DSLR vs iPhone subsets).

## Q4. Estimating navigation-relevant physical properties (friction, traversability, dynamics) from few real interactions

### Takeaway
Active and Bayesian system identification from very few real episodes is established. Examples: BayesSim (2019), ASID (single real episode, Fisher-information exploration), SPI-Active (legged robots, Fisher-information commands), and PhysTwin (sparse videos, deformables). For indoor wheeled navigation, twin physics is usually left at uniform defaults (GaussGym says so explicitly). Vision-based terrain friction/stiffness estimation exists for legged robots but has not been integrated into GS twins.

### Cited Findings
- BayesSim (Ramos, Possas, Fox), arXiv:1906.01728, RSS 2019. Likelihood-free posterior over simulator parameters for adaptive domain randomisation (pre-2023 anchor) — [arXiv](https://arxiv.org/abs/1906.01728)
- ASID (Memmel, Wagenmaker, Zhu, Yin, Fox, Gupta), arXiv:2404.12308. Semantic Scholar lists ICLR 2024; the arXiv page gives only the project site. The exploration policy minimises tr(I(θ,π)⁻¹) (Fisher information). Quote: "typically a single episode of data suffices". It identifies friction, mass/inertia, stiffness, articulation and geometry. Real results: rod balancing 6/9 vs domain randomisation 0/9; shuffleboard 7/10 vs 3/10 — [arXiv HTML](https://arxiv.org/html/2404.12308v2); [S2](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2404.12308)
- SPI-Active (Sobanbabu, He, He, Yang, et al.), arXiv:2505.14266, CoRL 2025 (PMLR 305:578–598). Sampling-based parameter identification plus active exploration that maximises the Fisher information of real trajectories. It outperforms baselines by 42–63% on legged locomotion tasks — [arXiv](https://arxiv.org/abs/2505.14266); [PMLR](https://proceedings.mlr.press/v305/sobanbabu25a.html)
- PhysTwin (Jiang, Hsu, Zhang, Yu, et al.), arXiv:2503.17973, ICCV 2025, doi:10.1109/ICCV51701.2025.00678. Spring-mass physics + Gaussian splats + an inverse-physics optimiser, from "sparse videos of dynamic objects under interaction". It targets deformable objects (manipulation), so transfer to navigation is limited to the methodology — [arXiv](https://arxiv.org/abs/2503.17973)
- Chen, Frey, Zhou, Miki, et al., "Identifying Terrain Physical Parameters from Vision", arXiv:2408.16567, IEEE RA-L 2024, doi:10.1109/LRA.2024.3455788. A physical decoder trained in sim predicts friction and stiffness and self-labels real images, validated on ANYmal — [arXiv](https://arxiv.org/abs/2408.16567)
- Splatblox (Chopra, Liang, Seneviratne, Lee, et al.), arXiv:2511.18525, arXiv only. GS + LiDAR build a traversability-aware ESDF (vegetation vs rigid obstacles), outdoors; >50% higher success — [arXiv](https://arxiv.org/abs/2511.18525)
- Material-informed GS (Huynh, Silva, Caesar, Son), arXiv:2511.20348, IEEE IV 2026. Semantic material masks are projected onto a GS-derived mesh to assign physics-based material properties (sensor simulation) — [arXiv](https://arxiv.org/abs/2511.20348)
- GaussGym: "Assets … initialized with uniform physical parameters (e.g., friction), which prevents accurate simulation of surfaces like ice, mud, or sand" — [arXiv HTML](https://arxiv.org/html/2510.15352v1)
- Real-is-Sim (Abou-Chakra, Sun, Rana, May, et al.), arXiv:2504.03597. A dynamic twin (Embodied Gaussians) synchronised with the real world at 60 Hz; manipulation (PushT) — [arXiv](https://arxiv.org/abs/2504.03597)

### Inferences
- For indoor wheeled or legged navigation, the physical parameters that matter (floor friction, robot actuation/latency, maybe door or obstacle mass) are few. ASID/SPI-Active suggest that one to a few Fisher-optimal real episodes suffice. So H1's "capture" should mainly count *visual* capture, with physics as a small add-on (a single "task-relevance + uncertainty" criterion over both views and interaction trajectories, mirroring FisherRF ↔ ASID/SPI-Active, both Fisher-information based).
- Combining view-selection Fisher information (FisherRF) and parameter-identification Fisher information (ASID/SPI-Active) under one task-weighted objective is not reported in any source found. It is a plausible methodological contribution.

### Gaps
- I found no paper that identifies indoor floor friction or wheel-slip parameters for a GS/mesh navigation twin from few interactions and measures the effect on navigation success.
- The ASID venue conflicts: Semantic Scholar says ICLR 2024, while the arXiv comment names no venue. Check the ICLR/OpenReview record before citing.

## Q5. Exact capture amounts in the closest works, and whether ≥40% less capture is plausible

### Takeaway
Reported per-scene budgets: Vid2Sim 15 s / 450 frames; EmbodiedSplat 20–30 min / 1000 RGB-D frames; RaEM 11 views; AREA3D a 40-view budget in Replica rooms; FisherRF 20 views; Dense Depth Priors 18 images per room. Active selection typically buys about +1 dB PSNR over random at a fixed budget. No work converts this into a navigation-success-equivalent capture saving. A ≥40% saving vs *uniform* capture is plausible, given saturating quality curves and the fact that navigation needs mostly floor-level and obstacle geometry. But no source directly shows it, which is what makes H1 novel. Saving ≥40% vs a *strong task-blind active* baseline is much less certain.

### Cited Findings
- Budgets: Vid2Sim 450 frames/scene — [arXiv HTML](https://arxiv.org/html/2501.06693v2); EmbodiedSplat 20–30 min, 1000 frames — [arXiv HTML](https://arxiv.org/html/2509.17430v2); RaEM 11 views — [arXiv HTML](https://arxiv.org/html/2403.11396v2); AREA3D 15 → 40 views — [arXiv HTML](https://arxiv.org/html/2512.05131v2); FisherRF 4 → 20 views — [arXiv HTML](https://arxiv.org/html/2311.17874v2); Dense Depth Priors 18 images — [arXiv](https://arxiv.org/abs/2112.03288)
- Size of the active-selection effect at a fixed budget: FisherRF +0.79 dB (sequential) / +1.96 dB (batch) over random on Blender at 20 views — [arXiv HTML](https://arxiv.org/html/2311.17874v2); AREA3D +1.06 dB over random on Replica room0 at 40 views (29.23 vs 28.17) — [arXiv HTML](https://arxiv.org/html/2512.05131v2); RaEM −24% W2 error in risk regions — [arXiv HTML](https://arxiv.org/html/2403.11396v2)
- Slope of the few-view curve: DNGaussian LLFF +3.06 dB from 3→6 views and +0.99 dB from 6→9 — [arXiv HTML](https://arxiv.org/html/2403.06912v3)
- Nearest measured "budget" analysis in real-to-sim-to-real is on the *demo* axis, not capture: RialTo (Torne et al., arXiv:2403.03949, RSS 2024) ablates 0/5/10/15 real demos (repo's earlier full-text check, research/crowdedness.md) — [arXiv](https://arxiv.org/abs/2403.03949)
- Physics side: ASID needs "typically a single episode" — [arXiv HTML](https://arxiv.org/html/2404.12308v2)

### Inferences
- **Plausibility (our reasoning, not from a source).** On the DNGaussian curve, the 6→9-view step (+50% views) buys ~1 dB. FisherRF and AREA3D buy ~0.8–2 dB over random at a fixed budget. So task-blind active selection is roughly worth "the next 30–50% of views" in the mid-budget regime. Restricting the objective to navigation-relevant regions (floor, obstacles, the goal's surroundings) should save more than whole-scene PSNR objectives do. This makes ≥40% vs *uniform* a realistic target, especially measured at a sub-plateau target τ. Against a FisherRF-type baseline the margin will be smaller. The repo's choice (≥40% vs uniform; only "ratio upper bound < 1" vs task-blind uncertainty) is well calibrated.
- **Risks.**
  - (i) Navigation policies pre-trained on HM3D may be insensitive to twin quality in some regions (EmbodiedSplat: PSNR and mesh choice matter, but not monotonically). The effect could then be small, or dominated by variance with ~10 real episodes per condition.
  - (ii) Feed-forward reconstructors lower the knee of the curve, so the absolute capture numbers shrink and the relative saving is harder to show.
  - (iii) The "capture" unit must be defined: frames, seconds, or path length. Budget curves from continuous video vs discrete views are not directly comparable (Vid2Sim/EmbodiedSplat use video; FisherRF/AREA3D use discrete views).
- **Novelty.** The objective "navigation success of a policy trained in the twin per unit of capture" is not claimed by any verified paper up to Sep 2026. Closest: RaEM (navigation risk, reconstruction metric), VISTA / GaussLite / AREA3D (task/VLM relevance, reconstruction or search metric), EmbodiedSplat (policy success, fixed capture), FalconGym 2.0 (performance-guided, but for training, not capture). H1 is novel as a combination with a new evaluation objective, not as a new primitive.

### Gaps
- No source reports capture-equivalent savings (views needed to match a quality or success level) for active vs uniform/random selection. Only fixed-budget differences are reported, so the ≥40% estimate above is an inference.
- The search was limited to about 20 queries/fetches. A targeted Semantic Scholar sweep of 2026 CVPR/ICRA/IROS/CoRL papers citing FisherRF + "navigation policy" is recommended before submission to confirm that no policy-in-the-loop capture paper has appeared.

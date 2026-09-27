# RQ1 feasibility: which spatially varying digital-twin (3DGS) reconstruction errors drive generalization of navigation/manipulation models

Scope: Can one PhD student, Oct 2026 to mid-2028, with A100/H100 on WCSS/PLGrid and no robot, answer RQ1 (component-swap attribution of twin errors; representation-change vs. error-magnitude predictor; uncertainty- and relevance-weighted per-region randomization)? Evidence current to 27 Sep 2026. All arXiv IDs were checked against the arXiv API; repos were checked with the GitHub API (stars / last push / licence as of 27 Sep 2026).

## Q1. Per-region uncertainty for 3DGS/NeRF: does it exist, is code available, does it work on real indoor/tabletop scans?

### Takeaway
Yes, with limits. Post-hoc per-Gaussian uncertainty for 3DGS exists and has code: FisherRF (3DGS-based, Fisher information) and PUP-3DGS, which reuses FisherRF's Fisher code for per-Gaussian sensitivity. Bayes' Rays covers NeRF (nerfstudio). They are demonstrated mainly on NeRF-synthetic, LLFF and Mip-NeRF360, not on ScanNet++-style room scans or robot tabletops. Porting to gsplat and checking on ScanNet++ is engineering work of a few weeks, not an open research problem. What nobody has shown is that these uncertainties line up with *task-relevant* errors.

### Cited Findings
- FisherRF (arXiv:2311.17874, Nov 2023) quantifies "observed information on the parameters of Radiance Fields" with Fisher information and supports view selection, active mapping and uncertainty quantification. — [arXiv 2311.17874](https://arxiv.org/abs/2311.17874)
- The FisherRF repo is "heavily built on 3D Gaussian Splatting" (original `diff-gaussian-rasterization` + `simple-knn`). It has `render_uncertainty.py` and `ause.py`, demos on NeRF-synthetic, Mip-NeRF360 and LF, no stated real indoor/tabletop demo, 217 stars, last push May 2025, licence NOASSERTION (custom LICENSE.md, likely inherited from the Inria 3DGS non-commercial licence; not verified). — [github.com/JiangWenPL/FisherRF](https://github.com/JiangWenPL/FisherRF)
- Bayes' Rays (arXiv:2309.03185, Sep 2023) is a post-hoc uncertainty method for any pre-trained NeRF, using spatial perturbations plus a Laplace approximation to produce a volumetric uncertainty field. Repo: MIT licence, 157 stars, last push Feb 2024, so inactive. — [arXiv 2309.03185](https://arxiv.org/abs/2309.03185), [github.com/BayesRays/BayesRays](https://github.com/BayesRays/BayesRays)
- PUP-3DGS (CVPR 2025, arXiv:2406.10219) computes a per-Gaussian Fisher/Hessian sensitivity over spatial parameters, using code from FisherRF. Repo: 154 stars, last push Nov 2025. — [arXiv 2406.10219](https://arxiv.org/pdf/2406.10219), [github.com/j-alex-hanson/gaussian-splatting-pup](https://github.com/j-alex-hanson/gaussian-splatting-pup)
- Stochastic Gaussian Splatting (arXiv:2403.18476) is a variational-inference uncertainty method for 3DGS that is trained jointly, not post hoc. Evaluated on LLFF. — [arXiv 2403.18476](https://arxiv.org/abs/2403.18476)
- UncertainGS (Neurocomputing, 2025): uncertainty-aware indoor 3DGS reconstruction that adapts in "regions with complex lighting conditions and texture inconsistencies". Code status not verified. — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0925231225028085)
- gsplat, the likely base renderer, is active: Apache-2.0, ~5.7k stars, last push 19 Sep 2026. — [github.com/nerfstudio-project/gsplat](https://github.com/nerfstudio-project/gsplat)

### Inferences
- MVP: compute a diagonal Fisher per Gaussian (FisherRF/PUP style), backprojected to a voxel or region map, on ScanNet++ iPhone-trained 3DGS. The diagonal Fisher is just the squared gradients of the rendering loss over the training views, so it is cheap: minutes per scene on one A100 (my estimate, not reported by the sources). Porting from the Inria rasterizer to gsplat is about 1–3 weeks.
- A built-in sanity check is available because ScanNet++ has a laser-scan and DSLR reference (see Q2): per-region uncertainty can be validated against per-region true error (depth error vs. the laser mesh, photometric error vs. DSLR views). This is itself a small, publishable result, since nobody has validated these uncertainties on room scans.
- Failure mode: epistemic (Fisher) uncertainty is high where views are sparse. It is blind to systematic errors that are well observed but wrong, such as baked-in view-dependent lighting, floaters that fit the training views, or reflective or transparent surfaces. Uncertainty may therefore correlate only weakly with true error. That weakens H1b but does not block RQ1.

### Gaps
- No 2023–2026 paper found that evaluates FisherRF or Bayes' Rays uncertainty against ground-truth error on ScanNet++ or on robot tabletop scenes.
- No maintained gsplat-native uncertainty module was found. Forks may exist; I did not find one with meaningful adoption.

## Q2. Can twin components (appearance, geometry, lighting) be swapped or corrected per region? Has anyone done controlled fidelity degradation and measured policy transfer?

### Takeaway
The data needed for component swaps exists. ScanNet++ has registered laser scans, DSLR images and iPhone RGB-D of the same 1000+ scenes, with an official "train on iPhone, test against DSLR" NVS benchmark. Appearance and geometry swaps are therefore concrete (see Inferences for how). Lighting swaps are not: both captures share the room's lighting, and 3DGS relighting is still research-grade. Controlled fidelity ablations with policy-level outcomes exist only in coarse, whole-scene form: colour alignment on/off, physics on/off, mesh source A vs. B, correlation of success rate with PSNR across scenes. No work found swaps components *per region* or asks which error types matter for policy transfer. RQ1 is therefore novel, and nothing blocks it.

### Cited Findings
- ScanNet++ v2 has "1000+ scenes" (released Dec 2024) with sub-millimetre laser scans, 33 MP DSLR images and iPhone RGB-D streams of the same scenes. An iPhone NVS benchmark (Oct 2025) lets users "train on commodity-level captures and test against high-quality DSLR images". Access is under the ScanNet++ Terms of Use after registration. — [ScanNet++ site](https://scannetpp.mlsg.cit.tum.de/scannetpp/); toolkit repo 410 stars, active (Jul 2026), no SPDX licence: [github.com/scannetpp/scannetpp](https://github.com/scannetpp/scannetpp)
- EmbodiedSplat (ICCV 2025, arXiv:2509.17430) did a coarse fidelity comparison. Meshes from DN-Splatter (GS then Poisson mesh) were compared with Polycam meshes (which use the original images), and Polycam did better zero-shot "due to superior visual fidelity" (e.g., lounge 76% vs 50% SR). Across scenes, HM3D zero-shot SR "is inversely correlated with the scale of the scene" and positively correlated with GS validation PSNR. Sim-vs-real correlation (SRCC) was 0.87–0.97 on 10 real Stretch episodes. — [arXiv 2509.17430 (HTML)](https://arxiv.org/html/2509.17430v1)
- Zhang et al. 2025 (arXiv:2511.04665; Y. Li's group) degraded components of a GS soft-body twin. Removing colour alignment cut sim-real Pearson r from 0.944/0.901/0.915 to 0.805/0.714/0.529 (toy packing / rope / T-block). Removing physics optimisation cut it to 0.694/0.832/0.905. An IsaacLab baseline reached r = 0.237 on rope. Setup: 4 policies (ACT, DP, π0, SmolVLA), 3 tasks, 16–27 configurations per task, 5–30 FPS on one GPU. Only a project page is listed for code. — [arXiv 2511.04665v2](https://arxiv.org/html/2511.04665v2), [real2sim-eval.github.io](https://real2sim-eval.github.io/)
- Jin et al. 2026 (arXiv:2603.22876, v2 Jun 2026; authors Ruixing Jin … Guiliang Liu) is an empirical study of the determinants of VLA sim-to-real across multi-level domain randomization, photorealistic rendering, physics realism and RL updates, with ">10k real-world trials". It varies factors per dimension, not per scene region. Platform and protocol release was promised; no repo found. — [arXiv 2603.22876](https://arxiv.org/abs/2603.22876)
- ReVeal (arXiv:2609.23910, 20 Sep 2026, Purdue/Samsung) correlates workspace reconstruction fidelity with real-sim agreement for GR00T, SmolVLA and π0.5 on 8 scenes and 8 humanoid tasks in Genesis. It explicitly does *not* do controlled degradation or isolate appearance, geometry and lighting (see Q4 for numbers). — [arXiv 2609.23910](https://arxiv.org/html/2609.23910)
- Vid2Sim (CVPR 2025, arXiv:2501.06693) builds GS+mesh urban navigation sims from monocular video and trains RL navigation. Repo: 286 stars, last push Sep 2025, no SPDX licence. — [arXiv 2501.06693](https://arxiv.org/abs/2501.06693), [github.com/Vid2Sim/Vid2Sim](https://github.com/Vid2Sim/Vid2Sim)
- SplatSim (arXiv:2409.10161) replaces meshes with splats for rendering in manipulation sim and reports 86.25% zero-shot sim2real vs 97.5% for real-data policies. Repo: 159 stars, last push Sep 2025, no licence file. — [arXiv 2409.10161](https://arxiv.org/abs/2409.10161), [github.com/qureshinomaan/SplatSim](https://github.com/qureshinomaan/SplatSim)

### Inferences
- A concrete swap design on ScanNet++ (navigation):
  - Twin T0: 3DGS from the iPhone stream.
  - Reference R: 3DGS from DSLR images, plus the laser-scan mesh.
  - Appearance swap: render RGB from R's Gaussians inside a 3D region mask and from T0 elsewhere. Both captures are registered to the laser-scan frame, so masking Gaussians by position is simple. Blending seams at mask boundaries are a confound; mitigate with soft masks or whole-object regions.
  - Geometry swap: use the laser mesh for depth and collision (and optionally RGB-D depth) while keeping T0 appearance.
  - A cleaner alternative is to degrade the reference instead of correcting the twin. Inject controlled per-region perturbations into R (Gaussian position noise, colour or exposure shift, floaters, blur via fewer views), so error type, magnitude and location are all under experimental control. I recommend this as the main design because it decorrelates magnitude from representation change by construction, which H1a needs. Real iPhone-vs-DSLR swaps can then serve as the ecological validation.
- Lighting: ScanNet++ iPhone and DSLR are captured in the same session, so the natural lighting error between them is small. Lighting should be handled as a synthetic perturbation (global or regional exposure / white-balance / shading shifts), or dropped from the claims. Full 3DGS relighting is too risky for this timeline.
- Manipulation: no public dataset offers an iPhone-vs-reference pair *plus* robot-policy outcomes. The SIMPLER-style path (visual matching to Bridge/Fractal images, evaluating released policies) supports swaps of the background or overlay only, not a laser-grade reference. Treat manipulation as the secondary, lower-fidelity arm of RQ1.

### Gaps
- No work found that corrects or swaps reconstruction components *per region* and measures the downstream policy effect. This is the novelty of RQ1, and there is no precedent for effect sizes.
- Not verified: whether ScanNet++ iPhone and DSLR poses are pre-registered to a common frame for every scene. I believe they are aligned to the laser scan, but this should be checked in the toolkit docs.
- ScanNet++ Terms of Use restrict redistribution. Releasing derived twins may not be allowed (not checked in detail).

## Q3. Do 3DGS scenes run inside Habitat / ManiSkill3 (or similar) fast enough to train or fine-tune policies? Which repos, speed, GPU?

### Takeaway
Not natively. Habitat-Sim has no 3DGS renderer. EmbodiedSplat (the ICCV 2025 Habitat work) loads *Poisson meshes extracted from the splats*, not splats, so the "twin" seen by the policy is a baked mesh. ManiSkill3 likewise has no built-in splat renderer found. Working GS+physics stacks exist: GaussGym on IsaacGym for locomotion/navigation (>100k steps/s claimed), NavArena and NavGSim for navigation, SplatSim on PyBullet for manipulation, and Zhang et al. 2025 for soft-body manipulation at 5–30 FPS. Fine-tuning a navigation policy in GS twins is feasible on academic GPUs. RL training of manipulation from pixels in a GS twin is feasible only for simple tasks. For VLAs, evaluating released policies (no training) is the realistic scope.

### Cited Findings
- EmbodiedSplat: "DN-Splatter gives us Poisson reconstructed meshes … In order to load these meshes in Habitat-Sim, we need to convert these to .glb". Setup: pre-training on 16 A40 per policy; fine-tuning for 20M steps (vs 600M–1.2B pre-training), wall-clock time not reported; DN-Splatter mesh generation about 1–2 h per scene; 4 captured scenes plus 3 MuSHRoom scenes. Repo: 30 stars, last push Oct 2025, no licence. — [arXiv 2509.17430](https://arxiv.org/html/2509.17430v1), [github.com/gchhablani/embodied-splat-v1](https://github.com/gchhablani/embodied-splat-v1)
- DN-Splatter (the GS-to-mesh tool used there): Apache-2.0, 842 stars, last push Jul 2025. — [github.com/maturk/dn-splatter](https://github.com/maturk/dn-splatter)
- Habitat-Sim is active (MIT, 3.8k stars, push Jul 2026). ManiSkill3 is active (Apache-2.0, 3.4k stars, push Aug 2026) and claims "up to 30,000+ FPS" for GPU-parallel sim plus rendering (rasterized meshes, not splats). — [habitat-sim](https://github.com/facebookresearch/habitat-sim), [ManiSkill](https://github.com/mani-skill/ManiSkill), [arXiv 2410.00425](https://arxiv.org/abs/2410.00425)
- GaussGym (arXiv:2510.15352): 3DGS as a drop-in renderer in IsaacGym, ">100,000 steps per second on consumer GPUs" (resolution not given on the page). Scenes are built from VGGT poses, NKSR collision meshes and gsplat appearance, from iPhone, ARKit and GrandTour sources. Demonstrated on locomotion and navigation, not manipulation. Code is promised as open; I could not find the canonical repo via GitHub search (only `kerrj/nerfstudio-gaussgym`). — [arXiv 2510.15352](https://arxiv.org/abs/2510.15352), [gauss-gym.com](https://gauss-gym.com/)
- NavArena (arXiv:2609.04602, Sep 2026) turns fixed 3DGS reconstructions into goal-navigation benchmarks: frozen-3DGS RGB-D rendering, a Gaussian-density occupancy costmap, >2,000 scenes, 22.2M expert trajectories. — [arXiv 2609.04602](https://arxiv.org/abs/2609.04602)
- NavGSim (arXiv:2603.15186): hierarchical-3DGS simulator for large multi-room navigation with a GS "slice" technique for collisions and multi-GPU APIs; used to train a VLA. — [arXiv 2603.15186](https://arxiv.org/abs/2603.15186)
- SAGE-3D / InteriorGS (arXiv:2510.21307): 1K object-annotated indoor 3DGS scenes with collision bodies and a 3DGS VLN benchmark. It reports that "3DGS scene data is more difficult to converge". — [arXiv 2510.21307](https://arxiv.org/abs/2510.21307)
- SplatGym (github.com/SplatLearn/SplatGym): Apache-2.0, but only 16 stars and last push Jan 2025, so effectively unmaintained. — [GitHub](https://github.com/SplatLearn/SplatGym)
- RoboGSim (arXiv:2411.11839): only a project-page repo found (`robogsim/robogsim.github.io`, 2 stars). Simulator code is not publicly usable as far as I could verify. — [arXiv 2411.11839](https://arxiv.org/abs/2411.11839)
- Other manipulation GS real2sim stacks: RL-GSBridge (arXiv:2409.20291), Re³Sim (arXiv:2502.08645), RoboSimGS (arXiv:2510.10637, 3DGS appearance plus mesh physics), PolaRiS (arXiv:2512.16881, real-to-sim *evaluation* of generalist policies from short video scans). — arXiv [2409.20291](https://arxiv.org/abs/2409.20291), [2502.08645](https://arxiv.org/abs/2502.08645), [2510.10637](https://arxiv.org/abs/2510.10637), [2512.16881](https://arxiv.org/abs/2512.16881)
- SimplerEnv (visual matching; MIT, 1.2k stars, last push Dec 2025, slowing). — [arXiv 2405.05941](https://arxiv.org/abs/2405.05941), [github.com/simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv)

### Inferences
- Navigation MVP: skip Habitat's renderer. Use gsplat to render RGB (or RGB-D) inside a thin Habitat-like loop: laser-mesh or GS-derived navmesh for collision, pretrained ImageNav/ObjectNav or PointNav agent (Habitat baselines, or a pretrained diffusion navigation policy such as NavDP). Fine-tune about 5–20M steps per condition.
  - gsplat renders a room at 256×256 very fast on an A100. My estimate, not measured by the sources: several thousand FPS batched. Tens of millions of frames per condition is therefore hours to about a day of A100 time.
  - With ~6 conditions × 5 seeds × 10–20 scenes, that is roughly 300–600 A100-days. Borderline on PLGrid grants; must be scoped down (see Q6).
- Cheaper alternative that still answers RQ1: *evaluate* (not train) a fixed pretrained navigation policy across the swapped twins, plus a small number of fine-tuning runs. Most of the attribution signal (which error hurts) can come from evaluation-only rollouts, which cost roughly 100× less than training.
- Using EmbodiedSplat's mesh route would confound "3DGS error" with "mesh-baking error", which is itself one of the error types. That is fine if declared, but it is not a 3DGS twin.
- Manipulation: do not plan RL in a GS ManiSkill3 twin as a core deliverable (no maintained integration found). Evaluate released VLAs or BC policies in SIMPLER, PolaRiS or SplatSim-style scenes with swapped backgrounds, as prior work did.

### Gaps
- No measured gsplat throughput numbers were found for Habitat-style navigation training at the resolutions used by policies.
- Canonical GaussGym code URL, licence and activity not verified.
- NavArena and NavGSim code availability and licences not checked.

## Q4. Evidence that representation-space distance predicts downstream performance drop better than PSNR/LPIPS

### Takeaway
Correlational support exists and is very recent. ReVeal (Sep 2026) finds DINOv2 feature similarity the strongest single predictor of real-sim agreement (r = 0.795, vs LPIPS r = 0.600), and TR-FDF (Aug 2026, ultrasound) argues theoretically and empirically that *task-relevant feature dynamics*, not single-frame realism, govern zero-shot transfer. Both support H1a in direction. Neither is a controlled per-region test, and ReVeal's sample is 8 scenes, so the r differences are not statistically decisive. H1a remains open, which makes it a good contribution but not a guaranteed positive result.

### Cited Findings
- ReVeal (arXiv:2609.23910, 20 Sep 2026): correlations with real-sim agreement are DINOv2 r = 0.795, SigLIP 0.726, LPIPS 0.600, planar-geometry completeness 0.759, roughness 0.731 (PSNR and SSIM also compared). Setup: 8 scenes, 42 planar regions, 8 tasks, 3 VLAs. No controlled degradation, no component isolation, no code statement. — [arXiv 2609.23910](https://arxiv.org/html/2609.23910)
- TR-FDF (arXiv:2608.29516, 30 Aug 2026), on robotic ultrasound: "zero-shot transfer depends not only on single-frame realism but also on whether simulated observations reproduce task-relevant feature changes induced by probe motion". A contraction analysis shows that motion-sensitive mismatch reduces the closed-loop contraction margin, whereas motion-independent errors mainly enlarge the residual bound. — [arXiv 2608.29516](https://arxiv.org/abs/2608.29516)
- EmbodiedSplat reports only a PSNR–SR correlation, with no feature-space predictor. — [arXiv 2509.17430](https://arxiv.org/html/2509.17430v1)
- Zhang et al. 2025 show that colour alignment (an appearance correction that barely changes geometry) moves sim-real r from 0.53 to 0.92 on T-block, so small image-level corrections can have large policy-level effects. — [arXiv 2511.04665](https://arxiv.org/html/2511.04665v2)

### Inferences
- H1a is testable cheaply once the swap/perturbation pipeline exists. Compute, for each perturbation, (a) PSNR/LPIPS/depth error and (b) the change in a frozen encoder's features (DINOv2, or the policy's own encoder) on held-out paired views. Then regress the policy SR drop on each, with scene-clustered cross-validation.
- Main statistical risk: magnitude and representation change are highly collinear under natural errors. The controlled-perturbation design in Q2 (errors of equal PSNR but different feature impact, e.g., texture-preserving colour shift vs. edge-destroying blur) is what makes the comparison identifiable.
- Circularity risk: if the "reference model" is the policy's own encoder, predicting its drop from its own features is partly tautological. Report both a policy-independent model (DINOv2) and the policy encoder.

### Gaps
- No controlled study (any domain) found that shows feature distance beats PSNR/LPIPS for predicting policy degradation *under matched error magnitude*.
- I did not find the Mar 2026 Jin et al. paper reporting feature-distance predictors; it studies factors, not predictors.

## Q5. Evidence that targeted or structured randomization beats uniform randomization

### Takeaway
Strong evidence exists for *adaptive* randomization of dynamics parameters (DORAEMON, ICLR 2024; Active DR, 2019; ADR; continual DR). I found no evidence for *spatially structured* visual randomization of a reconstructed scene weighted by reconstruction uncertainty and task relevance. H1b is therefore novel. It also has a real chance of a null result, because uniform visual randomization is already a strong baseline.

### Cited Findings
- DORAEMON (arXiv:2311.01885, ICLR 2024) maximises the entropy of the dynamics distribution subject to a success constraint, as an alternative to hand-set uniform DR. It targets dynamics parameters, not visual or per-region randomization. — [arXiv 2311.01885](https://arxiv.org/abs/2311.01885), [ICLR 2024 PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/56adf9cb91aedfa41ce24398782a012f-Paper-Conference.pdf)
- Continual Domain Randomization (arXiv:2403.12193) randomizes parameters sequentially rather than jointly. — [arXiv 2403.12193](https://arxiv.org/pdf/2403.12193)
- Active Domain Randomization (Mehta et al., arXiv:1904.04762, 2019, before the 2023 window) learns which randomization parameters are most informative. — [arXiv 1904.04762](https://arxiv.org/abs/1904.04762)
- Jin et al. 2026 study "multi-level domain randomization" as one of four sim-to-real determinants for VLAs (>10k real trials). This is the closest recent evidence that DR *structure* matters for visual manipulation; exact per-level numbers were not extracted. — [arXiv 2603.22876](https://arxiv.org/abs/2603.22876)
- An aggregator (emergentmind) claims adaptive DR "consistently improves" generalization. This is not primary evidence and is not used. — [emergentmind ADR](https://www.emergentmind.com/topics/automatic-domain-randomization-adr)

### Inferences
- MVP for H1b: three arms at equal randomization "budget" (e.g., total expected per-pixel perturbation energy):
  1. uniform per-region appearance and geometry noise;
  2. noise ∝ Fisher uncertainty;
  3. noise ∝ uncertainty × task relevance, where task relevance is a gradient-based saliency of the policy's action w.r.t. the region, or goal and obstacle masks.
  Evaluate on the DSLR/laser reference twin and on real held-out frames (open loop).
- Equal-budget matching is essential; otherwise "targeted" wins or loses simply by randomizing less.
- Fallback if targeted does not beat uniform: report the null result together with the attribution result from H1a, which already covers RQ1's first half. §7 already anticipates this ("If harm follows error magnitude, this attribution will itself be reported").

### Gaps
- No 2023–2026 paper found on uncertainty-weighted *visual* randomization in reconstructed (NeRF/3DGS) twins.
- No per-level numbers from Jin et al. 2026 were extracted (full text not read).

## Q6. What could make RQ1 unsolvable? Failure modes, minimum viable version, fallback, compute/time

### Takeaway
RQ1 is solvable in about 1–1.5 years if scoped as: navigation on ScanNet++ as the main arm, controlled per-region perturbation of a high-fidelity reference plus natural iPhone-vs-DSLR swaps, evaluation-heavy with limited fine-tuning, and manipulation as an evaluation-only secondary arm. The main risks are statistical power (small, noisy effects), not missing tools. No single missing tool blocks it. Several pieces are research-grade glue, not products: gsplat-in-Habitat rendering, per-region swapping, uncertainty validated on room scans.

### Cited Findings
- Real-to-sim correlations are high only with dozens of configurations and multiple policies (16–27 configurations per task, 4 policies in Zhang et al.; 10 real episodes in EmbodiedSplat). Effect estimates are noisy at these sample sizes. — [arXiv 2511.04665](https://arxiv.org/html/2511.04665v2), [arXiv 2509.17430](https://arxiv.org/html/2509.17430v1)
- In EmbodiedSplat, zero-shot SR varies strongly with scene *scale*, not only with fidelity. That is a nuisance variable to control. — [arXiv 2509.17430](https://arxiv.org/html/2509.17430v1)
- In EmbodiedSplat, further HM3D pre-training beyond about 400M steps did not improve zero-shot real performance. Policy capacity and overfitting interact with twin fidelity. — [arXiv 2509.17430](https://arxiv.org/html/2509.17430v1)
- SAGE-3D reports that 3DGS scene data is "more difficult to converge" for VLN training. — [arXiv 2510.21307](https://arxiv.org/abs/2510.21307)
- Navigation policy pre-training cost is out of reach for re-doing (EmbodiedSplat: 16 A40 per policy, 600M–1.2B steps), so pretrained checkpoints must be reused. — [arXiv 2509.17430](https://arxiv.org/html/2509.17430v1)

### Inferences (failure modes, MVP, fallback, compute)
- **Failure modes**
  1. *Insensitivity*: policies pretrained on HM3D or other mesh scans may barely react to local errors, because navigation relies on coarse layout. Effects are then too small relative to seed and episode variance. Mitigation: include image-goal navigation (appearance-sensitive), use open-loop action-divergence on real frames as a finer-grained outcome, and use perturbations strong enough to guarantee a measurable effect on at least one end.
  2. *Collinearity*: see Q4. Without controlled perturbations, H1a cannot be separated from magnitude.
  3. *No real closed loop*: with no robot, the "real" outcome for navigation is either (a) the DSLR/laser reference twin, which measures fidelity gaps, not true reality, or (b) open-loop action agreement on real ScanNet++ frames. Both must be declared as proxies. For manipulation, the SIMPLER real-robot results are fixed and cover few policies and scenes.
  4. *Seams and artefacts* in per-region compositing create new errors. Degrading R instead of correcting T0 avoids most of this.
  5. *Licensing*: the Inria 3DGS licence is non-commercial (FisherRF and PUP inherit it); ScanNet++ has terms of use; several robotics repos have no licence. This is fine for academic research but restricts code and data release.
  6. *Tooling decay*: SplatGym (last push Jan 2025), Bayes' Rays (Feb 2024) and the SplatSim/Vid2Sim repos (no push since Sep 2025) are effectively unmaintained. Build on gsplat, Habitat-Sim and ManiSkill3, which are active.
- **MVP (≈9–12 months of work)**
  - 10–20 ScanNet++ scenes; 3DGS from iPhone and from DSLR (gsplat); laser mesh for collision and navmesh.
  - 1–2 pretrained navigation policies (PointNav or ImageNav) evaluated closed loop in rendered twins.
  - 4–6 error types × 3 magnitudes × per-region masks (goal region, obstacle regions, background).
  - Outcomes: SR/SPL drop against the reference twin, plus open-loop action divergence on real frames.
  - Predictors: PSNR, LPIPS, depth error vs. DINOv2 and policy-encoder feature change on held-out paired views.
  - Plus one targeted-vs-uniform randomization fine-tuning study on a subset (e.g., 5 scenes × 3 arms × 3 seeds).
- **Compute estimate (my estimate, not from sources)**
  - 3DGS training: about 20–40 min per scene per capture on one A100, so under 1 GPU-day for 40 reconstructions.
  - Evaluation rollouts: 1–2k episodes per condition × ~200 conditions is feasible in a few A100-days if rendering is batched.
  - Fine-tuning: 5–20M steps per run × ~45 runs is about 50–200 A100-days. This fits a typical PLGrid grant if runs are kept short.
- **Fallback** (if closed-loop effects are too small or the rendering loop proves unreliable)
  - Switch the outcome to open-loop action and feature divergence of the policy on paired real vs. twin views. This needs no simulator loop and still attributes harm per error type.
  - Use EmbodiedSplat's mesh-in-Habitat route with declared mesh baking, for which code exists.
  - Drop H1b to a smaller ablation, and report the attribution (H1a) and uncertainty-vs-true-error validation as the core RQ1 result.
- **Manipulation arm**: evaluation-only with released policies (SIMPLER visual matching, background and region swaps). Soft-body or GS twins as in Zhang et al. would require their code, which is not released as far as verified. RL training of manipulation in a GS ManiSkill3 twin is out of scope for this timeline.

### Gaps
- No published effect sizes exist for *local* (per-region) reconstruction errors on navigation success, so power analysis must be done with pilot data in the first months of research.
- Actual PLGrid/WCSS allocation sizes for this project were not researched here.

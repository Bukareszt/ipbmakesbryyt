# RQ1 mechanisms: reconstruction errors of a digital twin, representation-space harm prediction, uncertainty-guided per-region randomization

Scope: technical mechanisms behind RQ1 of the IPB (content/07-questions-hypotheses.md, 09-methods.md, 06-state-of-the-art.md, visible text only), with a wording audit. Status as of 27 Sep 2026. Sources marked "(not fetched this session)" are well-known papers cited from background knowledge; their IDs should be double-checked before use in the plan.

## Q1. How does 3D Gaussian Splatting represent a scene, and which reconstruction errors arise (by region)?

### Takeaway
A 3DGS scene is an explicit set of anisotropic 3D Gaussians. Each one has a mean, a covariance factored as rotation and scale, an opacity and spherical-harmonics (SH) colour. The Gaussians are projected to 2D and alpha-blended front to back by a tile-based differentiable rasterizer, and optimized with an L1 + D-SSIM photometric loss plus heuristic densification and pruning. Geometry and appearance live in the same primitives and are fit only to photometric consistency. Errors therefore concentrate where views are sparse, surfaces are textureless or reflective, or lighting is view-dependent. They appear as floaters, elongated or "splotchy" Gaussians, blur, holes and baked-in lighting.

### Cited Findings
- Each Gaussian has a world-space mean μ, a covariance Σ = R S Sᵀ Rᵀ (R from a quaternion, S from a 3-vector scale), an opacity α passed through a sigmoid, and SH coefficients for view-dependent colour (up to 4 bands, i.e. degree 3) — [Kerbl et al. 2023, arXiv:2308.04079](https://arxiv.org/html/2308.04079)
- Projection: Σ′ = J W Σ Wᵀ Jᵀ (W = viewing transform, J = Jacobian of the local affine approximation of the projection), keeping the 2×2 image-plane block — [arXiv:2308.04079](https://arxiv.org/html/2308.04079)
- Pixel colour is C = Σᵢ cᵢ αᵢ Πⱼ<ᵢ (1 − αⱼ) over depth-sorted Gaussians overlapping the pixel. The screen is split into 16×16 tiles, and Gaussians are radix-sorted by tile ID and depth. The number of blended primitives receiving gradients is not capped, so the whole pipeline is differentiable — [arXiv:2308.04079](https://arxiv.org/html/2308.04079)
- Adaptive density control: small Gaussians with large view-space positional gradients (τ_pos = 0.0002) are cloned, large ones are split into two with scale divided by 1.6, and Gaussians with low opacity or excessive size are pruned. The loss is (1−λ)L1 + λ·L_D-SSIM with λ = 0.2 — [arXiv:2308.04079](https://arxiv.org/html/2308.04079)
- The authors list their own limitations: "elongated artifacts or 'splotchy' Gaussians" in poorly observed regions, "popping" artifacts when large Gaussians are created, and difficulty with view-dependent effects — [arXiv:2308.04079](https://arxiv.org/html/2308.04079)
- In robot-evaluation twins, depth-supervised planar GS (PGSR-D) improved results on "reflective and weakly textured surfaces". Completeness (hole ratio) and roughness of task-relevant planar regions such as tabletops were strongly associated with sim-real agreement of VLA policies (Pearson r = 0.759 and 0.731) — [ReVeal, arXiv:2609.23910](https://arxiv.org/html/2609.23910)
- Generative priors improve rendering but add little to geometry, producing "averaged, blurry results for unseen areas" — [G4Splat, arXiv:2510.12099](https://arxiv.org/pdf/2510.12099) (seen only through a search snippet)

### Inferences
- A practical error taxonomy for RQ1, each type tied to a mechanism:
  - **Floaters**: semi-transparent Gaussians placed in free space to explain view-specific colour. They come from sparse or inconsistent views and are worst near the capture trajectory's edges.
  - **Blur / oversized Gaussians**: under-densified regions such as distant, weakly observed or textureless ones.
  - **Holes / missing geometry**: unobserved surfaces such as under tables, backs of objects and occluded floor.
  - **Wrong geometry with plausible appearance**: textureless or reflective surfaces, where photometric loss does not constrain depth.
  - **Baked lighting and shadows**: SH colour stores the radiance seen at capture time, so illumination is not separated from albedo. Moving objects or lights leaves wrong shading.
  - **View-dependent artefacts**: low-degree SH cannot fit specular highlights, so novel views away from the capture path break.
  - **Exposure / white-balance mismatch** between capture camera and robot camera. This is a global colour shift (see the colour-alignment ablation in Q3).
- These errors are spatially non-uniform because each depends on local view coverage, texture and material. This supports the plan's "errors differ between regions" premise.
- The primitives carry geometry (μ, Σ, α) and appearance (SH) jointly, so "one error type" is not a separable parameter block. Opacity in particular affects both.

### Gaps
- I found no paper that gives a standard, quantitative per-region taxonomy of 3DGS error types for robot scenes. The taxonomy above is a synthesis.

## Q2. How are per-Gaussian / per-pixel uncertainties computed (FisherRF, Bayes' Rays, ensembles), and what are their limitations?

### Takeaway
All three methods estimate epistemic uncertainty, i.e. how weakly the data constrain the parameters. FisherRF and Bayes' Rays use a diagonal Laplace / Fisher approximation built from Jacobians. Ensembles use disagreement between independently trained models. None of them measures systematic bias shared across fits. FisherRF's Hessian does not even depend on the observed pixel values. "Reconstruction uncertainty" is therefore a proxy for coverage and constraint, not for error such as baked lighting, a colour shift or a consistently wrong depth on a textureless surface.

### Cited Findings
- **FisherRF** (Jiang, Lei, Daniilidis): it treats rendering as a Gaussian likelihood, −log p(y|x,w) = ‖y − f(x,w)‖², and uses the Fisher information (the Hessian of the negative log-likelihood) as a measure of parameter information. With millions of parameters it applies a Laplace approximation with a diagonal Hessian, H ≈ diag(∇_w fᵀ ∇_w f) + λI. The paper states the Hessian is "independent of ground truth data or the actual image measurement". Per-pixel uncertainty for 3DGS is rendered by alpha-compositing per-Gaussian terms (trace of each Gaussian's Hessian block) along the ray. It is used for next-best-view selection via expected information gain — [arXiv:2311.17874](https://arxiv.org/html/2311.17874)
- **Bayes' Rays** (Goli et al.): post hoc, for a trained NeRF. It adds a spatial deformation field D_θ (displacement vectors on an M³ grid, trilinearly interpolated) and evaluates the NeRF at x + D_θ(x). A Laplace approximation with a diagonal Fisher approximation, Σ ≈ diag((2/R)Σ_r J_θᵀJ_θ + 2λI)⁻¹, gives a per-vertex ellipsoid within which geometry can move at little loss. The result is a volumetric spatial uncertainty field. The authors say it captures "only the epistemic uncertainty ... often present through missing or occluded data". It does not capture aleatoric uncertainty from noise or view inconsistencies, and it "cannot be trivially translated to other frameworks" beyond NeRF — [arXiv:2309.03185](https://arxiv.org/html/2309.03185)
- **Ensembles** (Sünderhauf et al.): per-pixel predictive uncertainty is the variance of rendered RGB across ensemble members plus a density-aware term from ray termination probabilities. The second term flags unobserved regions where all members may agree on background colour — [arXiv:2209.08718](https://arxiv.org/abs/2209.08718)
- **Evidence that disagreement misses systematic error** (radiative GS for sparse-view CT, a different domain): inside the object, 0.72–0.96 of squared error is "shared" (the mean error across ensemble members or retrainings). Posterior spread correlates with the varying component (0.427) "but barely with the dominant shared component (0.101)". A K=5 deep ensemble "has no detectable Spearman advantage (p=0.229)" over single-pass methods — [Zhao, Xu, Liu, arXiv:2607.13682](https://arxiv.org/html/2607.13682)
- Other 3DGS-native uncertainty methods exist, e.g. stochastic GS with multi-sample variance ([arXiv:2403.18476](https://arxiv.org/pdf/2403.18476)) and predictive photometric uncertainty ([arXiv:2603.22786](https://arxiv.org/pdf/2603.22786)). I did not read these in detail.

### Inferences
- What each method measures:
  - FisherRF: parameter information from view geometry. It is high where few rays constrain Gaussians. It is blind to residuals, so a well-observed but wrong region, such as baked lighting from a moved lamp, reads as certain.
  - Bayes' Rays: positional (geometric) tolerance only. It says nothing about colour or lighting, and as published it is NeRF-only.
  - Ensembles: variability across random seeds or data. They miss errors that every member reproduces, such as model-class bias (SH cannot represent specularity) or capture bias (exposure).
- For RQ1 this means per-region randomization "proportional to reconstruction uncertainty" targets under-observed regions but not systematic appearance errors. The plan should either (a) combine uncertainty with an observed error signal, such as held-out-view residuals or representation distance, or (b) state that uncertainty covers only the epistemic part.
- The CT result is outside the plan's domain. Cite it as supporting evidence, not as a direct finding for RGB 3DGS.

### Gaps
- I found no study quantifying the ratio of shared (bias) to variance error for RGB 3DGS of indoor or tabletop scenes. This is a measurable sub-question inside RQ1.

## Q3. How can error components be replaced or controlled in practice?

### Takeaway
Controlled replacement is feasible only where a more accurate reference exists. ScanNet++ provides laser-scan meshes (Faro, sub-millimetre, Poisson-meshed) and two independent image captures (DSLR and iPhone), which allows geometry to be replaced by the scan while appearance is taken from images. Appearance can be corrected globally by colour alignment. Published ablations already swap one component and hold the rest fixed, reporting sim-real agreement (Pearson r, MMRV).

### Cited Findings
- ScanNet++: 1000+ indoor scenes with sub-millimetre Faro Focus Premium laser scans (~40M points per scan), meshed by Poisson reconstruction, plus registered 33 MP DSLR images and iPhone RGB-D streams — [ScanNet++, arXiv:2308.11417](https://arxiv.org/pdf/2308.11417); [project page](https://scannetpp.mlsg.cit.tum.de/scannetpp/)
- Component-swap ablation (Zhang et al., GS + soft-body twin): removing colour alignment ("use the original GS colors in the iPhone camera space") dropped sim-real Pearson r from 0.915 to 0.529 on T-block pushing. Replacing optimized physics with a single global stiffness dropped r from 0.944 to 0.694 on toy packing. Each component mattered for different tasks — [arXiv:2511.04665](https://arxiv.org/html/2511.04665)
- ReVeal compares three reconstruction pipelines (2DGS, PGSR, PGSR-D with Depth Anything V2 supervision) with foreground objects reconstructed separately (TRELLIS, SAM 3D). Sim-real agreement across 3 VLA policies (GR00T, SmolVLA, π0.5) and 8 tasks was r = 0.773 / 0.850 / 0.960 respectively — [arXiv:2609.23910](https://arxiv.org/html/2609.23910)

### Inferences
- Practical interventions for RQ1:
  1. **Geometry from the scan**: render or collide with the laser mesh, or constrain Gaussians to the mesh surface. Colour is then still fit from images, so appearance changes too, and the "geometry-only" swap is approximate.
  2. **Appearance fixed while geometry varies**: freeze μ, Σ, α and refit only SH, or apply a per-image affine colour transform (exposure / white balance).
  3. **Lighting**: no clean swap exists without relightable reconstruction. Treat baked lighting as a residual category, or use scenes captured under two lighting conditions.
  4. **Per-region swaps**: compose a twin where region r (e.g. the tabletop, or the floor near the goal) comes from the reference and the rest from the reconstruction. This gives a counterfactual per-region harm Δ_r.
- Swaps interact, because shared primitives change both geometry and appearance. The plan should say it holds the other components fixed "where possible" and estimates interactions, e.g. with a factorial design over two or three components.
- For manipulation (SIMPLER-style twins from robot-dataset images) there are no laser scans. The attribution by replacement is therefore mainly feasible in navigation (ScanNet++). Manipulation can use ReVeal-style pipeline comparisons or synthetic injected errors instead.

### Gaps
- I found no published per-region, per-error-type replacement study for navigation twins. This is the novelty gap, but also an unvalidated protocol.

## Q4. How are representation distances between paired views computed, and does feature distance beat PSNR/LPIPS as a predictor?

### Takeaway
The standard per-pair measure is cosine similarity (or L2) between frozen-encoder embeddings of a rendered view and the real view at the same pose. CKA is a set-level similarity between two representation matrices over the same n inputs, so it cannot score single pairs or single regions. ReVeal already shows that DINOv2 cosine similarity on held-out-pose renders correlates better with VLA sim-real agreement (r = 0.795) than LPIPS (0.600), PSNR (0.512) or SSIM (0.229). That result is workspace-level, n = 24, and uses a generic encoder. It is not per-region, per-error-type or policy-encoder-based, which leaves room for RQ1 but also removes the claim to novelty in the general form.

### Cited Findings
- ReVeal NVMF: renders the reconstruction at held-out camera poses and compares against ground-truth RGB with PSNR, SSIM, LPIPS and cosine similarity φ(I_GT)ᵀφ(I_M)/(‖φ(I_GT)‖‖φ(I_M)‖) for φ ∈ {DINOv2, SigLIP} (encoders used by VLAs such as OpenVLA / SmolVLA) — [arXiv:2609.23910](https://arxiv.org/html/2609.23910)
- Correlation with workspace-level real-sim agreement: DINOv2 r = 0.795, SigLIP 0.726, APGF completeness 0.759, roughness 0.731, LPIPS 0.600, PSNR 0.512, SSIM 0.229. Each workspace–pipeline pair is one "reconstruction instance" (8 workspaces × 3 pipelines = 24). NVMF is computed globally per image. APGF is computed per annotated region. The authors name object-level fidelity and physics as future work — [arXiv:2609.23910](https://arxiv.org/html/2609.23910)
- CKA (Kornblith et al., ICML 2019) compares two representations of the same set of inputs through similarity matrices (HSIC-normalized). It is invariant to orthogonal transforms and isotropic scaling, not to arbitrary invertible linear maps. It reliably matches layers across networks trained from different initializations — [arXiv:1905.00414](https://arxiv.org/abs/1905.00414)
- A related perceptual-metric study reports that foundation-model features improve low-level perceptual similarity metrics — [arXiv:2409.07650](https://arxiv.org/html/2409.07650v2) (search snippet only)

### Inferences
- Three variants are possible for the "fixed reference model":
  - A frozen generic encoder such as DINOv2 ([arXiv:2304.07193], not fetched this session). It is independent of the trained policy, so the predictor is not circular.
  - The frozen encoder of a pretrained policy. It is closer to what the policy uses.
  - The encoder of the policy being evaluated. This is circular if that policy is trained in the twin, so it should be avoided as the predictor.
- For per-region attribution, use patch tokens restricted to the region's pixel mask, or the counterfactual distance d(φ(render_with_error), φ(render_with_region_corrected)). The global CLS / pooled embedding is not region-resolved.
- To say "predicts harm better", the plan needs a defined harm target (e.g. change in real success or in sim-real gap when the error is corrected), a defined comparison (rank correlation across error instances, or held-out R²), and the baselines PSNR / SSIM / LPIPS / depth error / Chamfer, all at the same granularity.
- ScanNet++ pairs (DSLR-built twin vs iPhone frames) mix in a sensor gap (camera, exposure, resolution). The representation distance will contain a non-reconstruction component, which should be estimated, e.g. from real DSLR vs real iPhone at the same pose.

### Gaps
- I found no study correlating representation distance with policy harm per region or per error type. I also found none using a policy encoder instead of a generic one. ReVeal's n = 24 is small, and no confidence intervals were reported in what I read.

## Q5. How does domain randomization work, and how do adaptive variants shape the distribution?

### Takeaway
Domain randomization (DR) trains on a distribution over simulator parameters, visual (textures, lighting, camera) or dynamics (mass, friction), so that reality falls inside the training distribution. Adaptive DR learns that distribution:
- SimOpt fits it to real rollouts.
- DORAEMON uses no real data. It maximizes the entropy of independent Beta distributions over dynamics parameters subject to a success-rate constraint and a KL trust region.

Both operate on a few global parameters. None of them assigns per-region randomization from reconstruction uncertainty.

### Cited Findings
- DORAEMON (Tiboni, Klink, Peters, Tommasi, D'Eramo, Chalvatzaki, ICLR 2024):
  - Parametric family: uncorrelated univariate Beta distributions per dynamics parameter, initialized at Be(100, 100).
  - Objective: max H(ν_φ) s.t. G(θ, φ) ≥ α, with α = 0.5.
  - Success is estimated by importance-weighting the K training episodes: (1/K) Σ [ν_φ_{i+1}(ξ_k)/ν_φ_i(ξ_k)]·1{success}.
  - Trust region: KL(ν_φ_{i+1} ‖ ν_φ_i) ≤ ε.
  - When the constraint fails, a backup problem maximizes success within the trust region.
  - It randomizes dynamics only and needs no real-world data. — [arXiv:2311.01885](https://arxiv.org/html/2311.01885)
- The DORAEMON abstract states that high variability "notoriously leads to overly conservative policies when randomizing excessively" — [arXiv:2311.01885](https://arxiv.org/abs/2311.01885)
- Original visual DR randomized textures, lighting, camera pose and distractors so that the real world appears as one more variation (Tobin et al. 2017) — [arXiv:1703.06907](https://arxiv.org/abs/1703.06907) (not fetched this session)
- SimOpt adapts the parameter distribution by minimizing the discrepancy between simulated and a few real trajectories (Chebotar et al., ICRA 2019) — [arXiv:1810.05687](https://arxiv.org/abs/1810.05687) (not fetched this session)

### Inferences
- An uncertainty-weighted per-region DR for a GS twin would randomize, per region r:
  - SH colour / brightness jitter
  - Gaussian position or scale noise
  - opacity perturbation (to simulate or suppress floaters)
  - texture replacement

  Each would have a scale s_r = f(u_r, relevance_r). It is appearance and geometry randomization, not dynamics, which distinguishes it from DORAEMON.
- "Proportional to uncertainty" is only one choice of f. A DORAEMON-like alternative is to maximize the entropy of the per-region distribution subject to a success constraint, with the uncertainty as a prior or upper bound. Stating a fixed proportionality is naive, because optimal scale is not linear in uncertainty.
- Task relevance needs an operational definition, e.g. action-gradient saliency, the change in the predicted action when the region is perturbed, or task masks such as the tabletop or the navigation goal. In the plan it overlaps with RQ3's "action sensitivity".

### Gaps
- I did not verify whether any 2025–2026 paper already does per-Gaussian or per-region randomization weighted by uncertainty in a GS twin. A targeted search before submission is recommended.

## Q6. Wording check: imprecise sentences in §7 and §9 on RQ1, with proposed corrections

### Takeaway
The core idea is sound, but several phrases are underspecified or overclaim:
- "the change it induces in the representation" has no counterfactual.
- "reconstruction uncertainty" is used as if it measured error.
- "replace components" suggests separable components.
- "harm" is undefined.
- ReVeal's prior evidence needs to be acknowledged.

### Cited Findings
- Prior evidence that DINOv2 cosine similarity beats PSNR/LPIPS as a predictor of sim-real agreement at workspace level — [arXiv:2609.23910](https://arxiv.org/html/2609.23910)
- Uncertainty methods capture epistemic uncertainty only. FisherRF's Hessian ignores the measurements, and Bayes' Rays covers geometry only — [arXiv:2311.17874](https://arxiv.org/html/2311.17874); [arXiv:2309.03185](https://arxiv.org/html/2309.03185)
- Geometry and appearance share primitives in 3DGS — [arXiv:2308.04079](https://arxiv.org/html/2308.04079)

### Inferences (problems → proposed phrasing)
1. §7 hypothesis: "The harm caused by a reconstruction error is predicted better by the change it induces in the representation of a fixed reference model on held-out paired views than by its magnitude in the image or geometry."
   - Problems: the counterfactual is missing (change relative to what?). "Harm" and "predicted better" are undefined. The claim does not say it is per region or per error type, and in its global form it is already reported by ReVeal.
   - Proposed: "*Hypothesis:* For each region and type of reconstruction error, the drop in real-world performance it causes is predicted better by the distance between the features of a fixed pretrained encoder on renders with and without the error, at held-out camera poses, than by the corresponding photometric or geometric error (e.g., PSNR, LPIPS, depth error)."
2. §7: "Separately, randomizing each region in proportion to its reconstruction uncertainty and task relevance yields better generalization than uniform randomization."
   - Problems: uncertainty is not error, since it misses systematic bias. "In proportion" fixes an arbitrary functional form. What is randomized is not said. The comparison needs an equal total randomization budget.
   - Proposed: "Separately, randomizing the appearance and geometry of each region with a strength that increases with its estimated reconstruction error (epistemic uncertainty complemented by the discrepancy on held-out views) and its task relevance yields better generalization than uniform randomization of the same total strength."
3. §7: "the research will replace components of the twin with a more accurate reference"
   - Problem: in 3DGS, components are not separable, and a reference exists only for some scenes.
   - Proposed: "To test this, the research will correct one type of error at a time in selected regions, e.g., replacing geometry with a laser scan or aligning colours to real images, while keeping the others fixed where the reconstruction allows, and measure the effect."
4. §7: "the third question will rely on reconstruction uncertainty and action sensitivity only"
   - This is fine, but it should acknowledge the uncertainty limitation. Suggested: "...on reconstruction uncertainty and action sensitivity only, keeping in mind that uncertainty does not reveal errors reproduced consistently by the reconstruction."
5. §9: "examine variants of the twin in which one type of reconstruction error is corrected"
   - Proposed: "...variants of the twin in which one type of reconstruction error is corrected in selected regions using a more accurate reference, e.g. the laser scans of ScanNet++, where such a reference exists".
   - Reason: manipulation twins lack scans.
6. §9: "study randomization guided by reconstruction uncertainty and task relevance"
   - Proposed: "...randomization of appearance and geometry whose per-region strength is guided by estimated reconstruction error and task relevance, compared with uniform randomization of equal total strength".
7. §6: "shape its distribution by ... maximizing its entropy while preserving task success [5]"
   - This is accurate, but it can add "over dynamics parameters, without real data", which sharpens the contrast with per-region appearance randomization. "Tune a few global parameters of a synthetic simulator" is accurate for [4] and [5].
8. §6 should cite ReVeal (Wang et al. 2026, arXiv:2609.23910) as the closest work: it shows at the workspace level that DINOv2 feature similarity predicts sim-real agreement of VLA policies better than PSNR/LPIPS. RQ1's novelty is then its per-region, per-error-type, counterfactual attribution across two tasks.
9. "fixed reference model": say "a fixed pretrained visual encoder (e.g., DINOv2)", which makes clear it is not the policy being trained.
10. "held-out paired views": for navigation the pairs come from a different device (iPhone vs DSLR), so name the sensor confound and the control for it, e.g. "the distance between real frames of the two captures serves as a floor".

### Gaps
- Whether ScanNet++ DSLR and iPhone poses are registered precisely enough for pixel- or patch-level paired comparison was not verified in this session.

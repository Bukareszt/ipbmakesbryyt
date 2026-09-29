# How the representation-learning methods behind RQ2 work, and where the IPB wording is imprecise

Scope: technical mechanics of the methods RQ2 relies on (probing, causal interventions, representation similarity, alignment objectives, surgical fine-tuning, domain-adaptation theory), what the cited VLA/policy papers actually did, and a wording audit of §2, §5–§9 (visible text). Status as of 27 Sep 2026.

Source-verification note: papers marked "(fetched)" were read in this session (arXiv abstract and/or HTML). Papers marked "(from knowledge, not re-fetched)" are standard, well-known references cited with their arXiv IDs; the report writer should treat the specific numbers for those as needing a quick check.

---

## 1. Linear probing: procedure, control tasks/selectivity (Hewitt & Liang 2019), pitfalls

### Takeaway
A probe is a small supervised model (usually linear/logistic regression) trained on frozen hidden states of layer l to predict a label; its held-out accuracy measures how much label information is *linearly decodable* at l. It measures neither how much information exists (a stronger probe can decode more) nor whether the model uses it. For RQ2 the plan must also say whether "no longer decodable from real" means "a probe trained on simulated states fails on real states" (probe-transfer) or "a probe trained on real states fails" (information lost). These are different quantities.

### Cited Findings
- Hewitt & Liang define **control tasks**: tasks that "associate word types with random outputs", so a probe can only solve them by memorising the input type. A **selective** probe has "high linguistic task accuracy and low control task accuracy". Selectivity = task accuracy − control accuracy — [Hewitt & Liang 2019, arXiv:1909.03368](https://arxiv.org/abs/1909.03368) (fetched)
- Popular probes on ELMo "are not selective". Dropout "is ineffective for improving selectivity of MLPs, but ... other forms of regularization are effective". Layer-1 probes gave slightly higher POS accuracy than layer-2 probes, but layer-2 probes were "substantially more selective". So raw accuracy can rank layers wrongly — [arXiv:1909.03368](https://arxiv.org/abs/1909.03368) (fetched)
- Amnesic probing removes a property from the representation (iterative nullspace projection) and measures how much the model's behaviour changes. "Conventional probing performance is not correlated to task importance", and the authors "call for increased scrutiny of claims that draw behavioral or causal conclusions from probing results" — [Elazar et al. 2021, arXiv:2006.00995](https://arxiv.org/abs/2006.00995) (fetched)
- Survey of probing pitfalls: choice of probe capacity, missing baselines/controls, and the correlational nature of probing (decodable ≠ used) — [Belinkov 2022, Computational Linguistics, arXiv:2102.12452](https://arxiv.org/abs/2102.12452) (from knowledge, not re-fetched)
- Alternatives that address probe capacity: MDL/description-length probing reports how compactly the label can be transmitted given the representation, not just accuracy ([Voita & Titov 2020, arXiv:2003.12298](https://arxiv.org/abs/2003.12298)); "usable information" (V-information) formalises decodability under a restricted function class and explains why linear decodability can *increase* with depth even though Shannon information cannot ([Xu et al. 2020, arXiv:2002.10689](https://arxiv.org/abs/2002.10689)) (both from knowledge, not re-fetched)

### Inferences
- **Standard procedure applied to RQ2.** (1) Freeze the policy. (2) Pick probe targets available for both sim and real frames that are task-relevant but not the output itself. For navigation with ScanNet++-style data: depth/free-space in the image, distance/bearing to the goal, object presence. For manipulation: object/gripper pose, contact/grasp state, the target object's identity. (3) At each stage l, extract h_l for paired sim/real views of the same scenes. (4) Fit a linear probe (L2-regularised logistic/ridge regression), cross-validating the regulariser on a held-out *scene* split. (5) Report, per layer: (a) Acc_sim→sim; (b) Acc_sim→real, the probe trained on sim and tested on paired real; (c) Acc_real→real, the probe trained on a small real split. (6) Controls: a control task in the Hewitt–Liang style (random labels tied to scene/view identity), a random-init network baseline, and a pixel-input baseline. Report bootstrap confidence intervals over scenes.
- **Two meanings of "no longer decodable".** A drop in (b) with (c) intact means the information is still there but *encoded differently* for real inputs, i.e. a representational shift, which alignment can fix. A drop in (c) means the information is *absent* in real hidden states. Alignment of the model alone may not fix that, and correcting the twin (RQ3) is needed. This split is useful to the thesis and should be stated in §7/§9.
- **"First stage" is not well defined for linear decodability.** By the data-processing inequality, Shannon information about the label in h_l can only decrease with depth. Linear decodability can rise and fall (V-information). "First stage at which ... can no longer be decoded" therefore needs a threshold, e.g. the first layer where the gap Acc_sim→sim − Acc_sim→real exceeds a set margin beyond the control-task gap, with confidence intervals.
- **Transformer caveat.** In VLAs/ViTs with residual streams, information is rarely deleted at one block. Divergence between sim and real is spread over the stream. Expect a gradual profile rather than a sharp "stage", and phrase the hypothesis so that a gradual profile is still a result.
- Label scarcity on real frames is the practical limit for (c). Probe targets derived from dataset geometry (poses, depth) avoid manual labelling.

### Gaps
- No work was found that runs layer-wise sim→real probe-transfer in robot policies trained in Gaussian-splat twins. This matches the IPB's novelty claim, but the search was not exhaustive.

---

## 2. Causal methods: activation patching and interchange interventions

### Takeaway
Causal methods replace part of a hidden state with its value from another input and measure the change in the output. That tests whether the model *uses* the information a probe finds. For sim/real pairs there is a trap: patching the *entire* state at layer l trivially reproduces the donor's output. Only patching a *subset* (a probe direction/subspace, specific tokens or regions, specific heads) is informative.

### Cited Findings
- "Activation patching, also known as causal tracing or interchange intervention, is a standard technique". Choices of corruption method and metric "could lead to disparate interpretability results". The paper gives best-practice recommendations — [Zhang & Nanda 2024 (ICLR), arXiv:2309.16042](https://arxiv.org/abs/2309.16042) (fetched)
- Interchange interventions align neural representations with variables of an interpretable causal model and "verify that the neural representations have the causal properties of their aligned variables" (causal abstraction). A BERT model realised parts of a natural-logic causal model; a baseline did not — [Geiger et al. 2021 (NeurIPS), arXiv:2106.02997](https://arxiv.org/abs/2106.02997) (fetched)
- Distributed Alignment Search (DAS) learns a rotated *subspace* in which to perform interchange interventions, instead of patching whole neurons/layers — [Geiger et al. 2023/24, arXiv:2303.02536](https://arxiv.org/abs/2303.02536) (from knowledge, not re-fetched)
- In VLAs (π0, OpenVLA), Häon et al. project feedforward activations onto the token-embedding basis, find "semantic directions – such as speed and direction – that are causally linked to action selection", and steer behaviour by adding activations "without fine-tuning, reward signals, or environment interaction". They show this zero-shot in LIBERO and on a real UR5 (CoRL 2025) — [Häon et al., arXiv:2509.00328](https://arxiv.org/abs/2509.00328) (fetched)

### Inferences
- **Concrete sim/real design.** Run the policy on a real view x_r. At layer l, replace only the component c (e.g. the projection onto the probe's subspace, or the tokens of one image region) with its value from the paired sim view x_s. Measure the fraction of the action gap recovered: R(l,c) = (d(a_real, a_sim) − d(a_patched, a_sim)) / d(a_real, a_sim). Do this open-loop on frames (action error) and, where possible, closed-loop in the reference simulation. Also run the reverse (real → sim) to test sufficiency.
- High probe transfer loss at l together with high R(l, probe-subspace) is evidence that the lost information is *used*. High probe loss with R ≈ 0 means it is decodable but unused. Such a layer is a poor target for alignment.
- Region-level patching (swapping the tokens of one scene region) links RQ2 to RQ1: it attributes the representational gap to reconstruction errors in specific regions.
- Closed-loop policies add compounding. A one-step patch measures a local effect only, and the plan should say so.

### Gaps
- No published sim-to-real study using activation patching on navigation/manipulation policies was found. Häon et al. is steering, not a sim/real analysis.

---

## 3. Representation similarity: CKA and SVCCA for sim vs real activations

### Takeaway
With paired views, stack the layer-l activations for n sim views (X, n×d) and the n paired real views (Y, n×d) and compute linear CKA per layer. The curve CKA(l) shows where sim and real representations diverge. CKA is task-agnostic, though: it also counts nuisance directions, so it complements probes rather than replacing them.

### Cited Findings
- Kornblith et al. show that neither CCA "nor any other statistic that is invariant to invertible linear transformation can measure meaningful similarities between representations" when dimensionality exceeds the number of samples. They introduce Centered Kernel Alignment, which compares representational similarity matrices, and "unlike CCA, CKA can reliably identify correspondences between representations in networks trained from different initializations" — [Kornblith et al. 2019 (ICML), arXiv:1905.00414](https://arxiv.org/abs/1905.00414) (fetched)
- Formula (from the same paper, not re-quoted): for column-centred X, Y, linear CKA(X,Y) = ‖YᵀX‖²_F / (‖XᵀX‖_F · ‖YᵀY‖_F). It is invariant to orthogonal transforms and isotropic scaling, but not to arbitrary invertible linear maps. — [arXiv:1905.00414](https://arxiv.org/abs/1905.00414)
- SVCCA: an SVD of each activation matrix keeps the top directions (e.g. those explaining 99% of variance). CCA then finds maximally correlated linear combinations, and the mean canonical correlation is the similarity — [Raghu et al. 2017 (NeurIPS), arXiv:1706.05806](https://arxiv.org/abs/1706.05806) (from knowledge, not re-fetched)
- CKA can be dominated by a few high-variance directions or outlier examples, and small changes can manipulate it strongly — [Davari et al. 2022, "Reliability of CKA as a similarity measure", arXiv:2210.16156](https://arxiv.org/abs/2210.16156) (from knowledge, not re-fetched)
- Lei et al. measured sim/real feature alignment with UMAP, Wasserstein distance (global) and Gromov–Wasserstein distance (local geometry) at the vision stem and encoder trunk. Smaller distances correlated with success (r ≈ 0.6–0.8, p < 0.04) — [Lei et al. 2026, arXiv:2604.13645](https://arxiv.org/html/2604.13645) (fetched)

### Inferences
- CKA needs paired rows, and the plan has them (paired views). Without pairs, use distribution-level distances (MMD, Wasserstein) instead.
- CKA/SVCCA answer "how similar is the geometry?". Probes answer "is task information preserved/transferable?". The RQ2 localisation criterion is defined by task information, so probes must be primary and CKA secondary. Reporting where they disagree is itself informative: low CKA with intact probes means nuisance divergence.

### Gaps
- None critical.

---

## 4. Alignment objectives, what "aligning at a layer" means, and their cost

### Takeaway
"Aligning at layer l" means adding a loss term L_align(h_l(sim), h_l(real)) to the task loss. Its gradients flow only into the parameters θ_{≤l} that produce h_l, plus any auxiliary networks (a discriminator). Layers above l are trained only by the task loss, or frozen. The objectives differ in what they match: marginal distributions (DANN, MMD, CORAL), joint feature–state distributions (Cheng et al. OT), or individual pairs (a paired feature loss, which is what "a few paired views" allows).

### Cited Findings
- **DANN** (Ganin et al., JMLR 2016, [arXiv:1505.07818](https://arxiv.org/abs/1505.07818); from knowledge, not re-fetched). The architecture has a feature extractor G_f(·;θ_f), a label predictor G_y(·;θ_y) and a domain classifier G_d(·;θ_d) attached to the features. The objective is a saddle point: θ_f, θ_y minimise the label loss minus λ·domain loss, and θ_d minimises the domain loss. It is implemented with a **gradient reversal layer**, which is the identity in the forward pass and multiplies the gradient by −λ in the backward pass. The paper schedules λ_p = 2/(1+exp(−10p)) − 1 over training progress p. The discriminator's error relates to the H-divergence (proxy A-distance, see §6 below).
- **MMD** (Gretton et al., JMLR 2012; used in deep DA by DAN, [Long et al. 2015, arXiv:1502.02791](https://arxiv.org/abs/1502.02791); from knowledge). The loss is the squared distance between kernel mean embeddings of the sim and real feature distributions. DAN applies multi-kernel MMD to *several* task-specific layers at once, and Joint Adaptation Networks align the joint distribution of activations across several layers ([Long et al. 2017, arXiv:1605.06636](https://arxiv.org/abs/1605.06636)). Cost: the quadratic estimator is O(n²d) per batch (a linear-time estimator exists), and the kernel bandwidth must be chosen.
- **CORAL / Deep CORAL** ([Sun & Saenko 2016, arXiv:1607.01719](https://arxiv.org/abs/1607.01719); from knowledge). The loss is ‖C_S − C_T‖²_F / (4d²) between the d×d feature covariance matrices of source and target at the chosen layer. It matches second-order statistics only. Cost is O(nd²) with a d×d matrix, so a 4096-d VLA token space means 16.8M entries; projecting or pooling first is usual.
- **Joint OT alignment (Cheng et al. 2025, NeurIPS)** (fetched). The method "aligns the joint distributions of observations and their corresponding actions or task-relevant states across domains". The ground cost is C = α₁·d_Z(f_φ(o_src), f_φ(o_tgt)) + α₂·d_X(x_src, x_tgt), where x are **proprioceptive states**, not actions, because "discrepancies in controller characteristics ... make d_A(a_src, a_tgt) an unreliable indicator". The loss is entropic **unbalanced OT**: min_Π ⟨Π,C⟩ + ε·Ω(Π) + τ·KL(Π1‖p) + τ·KL(Πᵀ1‖q), solved with Sinkhorn–Knopp on mini-batches. The unbalanced form handles |D_src| ≫ |D_tgt| by allowing partial mass transport. Mini-batches pair trajectories by normalised DTW distance. The total loss is L_BC(f_φ, π_θ) + λ·L_UOT(f_φ); the OT loss updates only the encoder f_φ. The paper reports up to 30% higher real-world success — [Cheng et al., arXiv:2509.18631](https://arxiv.org/html/2509.18631)
- **Paired / teacher feature alignment at a middle layer (Kachaev et al.)** (fetched). OpenVLA-7B mid-level backbone features (layer 16 was best) are passed through a *frozen* MLP projector onto the unit sphere and aligned to a frozen teacher encoder's patch embeddings (C-RADIOv3 best; DINOv2, SigLIP and Theia also tried) with L_align = −(1/k) Σ_j cos(u_j, z_j) and L_total = L_VLA + 0.2·L_align. Aligning the backbone to the teacher ("Backbone2Enc") beat aligning encoder to encoder. The projector is frozen so that it cannot absorb the alignment. They report up to 10% relative OOD gain over naive SFT on SIMPLER-based tests — [Kachaev et al., arXiv:2510.25616](https://arxiv.org/html/2510.25616)
- **Adversarial alignment inside co-training (Lei et al.)** (fetched). CFG-ADDA attaches one-hot environment labels, so domain identity stays available, and applies adversarial discriminator regularisation "on remaining representation dimensions". At inference it uses classifier-free guidance, s = (1+λ)s(a,o,c,t) − λ s(a,o,∅,t) with λ = −0.5. The paper reports about 74% real success, roughly 20 points over baseline co-training — [Lei et al., arXiv:2604.13645](https://arxiv.org/html/2604.13645)
- Input-level alignment exists as a separate family: image-to-image translation to a canonical/simulated appearance (e.g. RCAN, [James et al. 2019, arXiv:1812.07252](https://arxiv.org/abs/1812.07252); from knowledge).

### Inferences
- **Where the loss attaches and what it updates.** For "align at stage l" the practical recipe is as follows. Keep the sim branch as target, h_l(x_s) with stop-gradient or from a frozen copy. Add L_align(h_l(x_r), sg[h_l(x_s)]) to the task loss on sim (and any real) data. Update θ_{≤l}; optionally freeze θ_{>l} so the downstream readout that works in sim is kept. This is essentially "adapt real inputs into the simulated feature space up to l". "Input" alignment = l = 0 (image translation or pixel loss). "Final features" = the last encoder layer. "Everywhere" = a sum of losses over all layers (DAN/JAN style).
- **With pairs, per-sample losses are available and cheaper.** An L2/cosine loss on paired views costs O(nd), needs no discriminator and matches individual scenes, not just distributions. Distribution losses (DANN/MMD/CORAL/OT) are needed when pairs are unavailable (unlabelled real images in RQ3). The IPB should name which loss it uses, because "aligning ... from a few paired views" allows several very different objectives.
- **Collapse risk.** A pure alignment loss is minimised by constant features. It must be combined with the task loss, or the downstream layers must be kept fixed. With few pairs it can also overfit, so compare against surgical fine-tuning at the same l on the same real data (see §5).
- **Relative cost (qualitative).** Paired L2/cosine is cheapest (O(nd)). CORAL costs O(nd²). Quadratic MMD costs O(n²d). OT costs O(n²·iterations) per batch plus DTW preprocessing (Cheng). DANN adds a network and min–max training, which is the least stable. None changes inference cost. Multi-layer ("everywhere") scales with the number of layers and needs one weight per layer, a tuning confound: the plan should use equal total tuning budgets.
- **Fair comparison.** Two baselines matter for the RQ2 hypothesis to be a real test: (i) the same loss at every layer, chosen by oracle, which checks whether the probe-chosen layer is near the best; (ii) layer selection by a cheap heuristic such as Auto-RGN or "first block for appearance shift" (Lee et al.). Otherwise the probe localisation may add nothing over known heuristics.

### Gaps
- No paper was found that compares the *same* alignment loss at probe-selected versus fixed layers for sim-to-real policies. This supports the novelty claim, but it was not verified exhaustively.
- Exact per-step wall-clock costs are not reported in Cheng et al. (per the fetched text).

---

## 5. Surgical fine-tuning (Lee et al. 2023): which layers for which shift

### Takeaway
Fine-tuning only a subset of layers on a small target set matches or beats full fine-tuning. The best subset depends on the shift type: early layers for input-level shifts, middle blocks for feature-level shifts, last layer for output-level shifts. Sim-to-real appearance gaps look "input-level", which predicts early layers. That gives RQ2 a strong prior and baseline.

### Cited Findings
- "Selectively fine-tuning a subset of layers (surgical fine-tuning) matches or outperforms commonly used fine-tuning approaches". For image corruptions, "fine-tuning only the first few layers works best". There is a proof that in an idealised two-layer network, first-layer tuning can beat tuning all layers — [Lee et al. 2023 (ICLR), arXiv:2210.11466](https://arxiv.org/abs/2210.11466) (fetched)
- Shift categories: input-level (CIFAR-C, ImageNet-C) → earlier layers; feature-level (Living-17, Entity-30, i.e. subpopulation shift) → middle blocks; output-level (CIFAR-Flip, Waterbirds, CelebA, i.e. label/spurious-correlation changes) → later layers. Models: ResNet-26 (CIFAR), ResNet-50, and CLIP ViT-B/16 on WILDS. Settings go down to "as few as 1 image per class". Auto-RGN (ratio of gradient norm to parameter norm) picks layers automatically and "consistently improves over full fine-tuning"; Auto-SNR is less reliable — [arXiv:2210.11466 HTML](https://arxiv.org/html/2210.11466) (fetched)

### Inferences
- The RQ2 hypothesis is partly anticipated: "adapt where the shift enters" is Lee et al.'s finding for classification. What RQ2 adds: (a) localisation by *measured task-information loss* rather than shift-type labels or gradient norms, (b) a representation-*alignment* loss rather than supervised fine-tuning, and (c) policies in closed loop in both navigation and manipulation. §6 should say this explicitly, and Auto-RGN should be a baseline.
- Sim-to-real in twins mixes shift types. Appearance and lighting errors are input-level. Geometry and physics errors change what the action should be, which is closer to output-level. So different layers may be optimal for different error types, which links to RQ1.

### Gaps
- Surgical fine-tuning has not been verified on robot policies in this session. No source found.

---

## 6. Theory: the Ben-David bound and Zhao et al. on why invariance can hurt

### Takeaway
Ben-David: target error ≤ source error + ½·(H∆H-divergence between the input/feature marginals) + λ, where λ is the combined error of the *best single* hypothesis on both domains. Aligning features shrinks the middle term, but λ is computed *on the aligned features*, so alignment can make λ larger. Zhao et al. prove this happens whenever the "label" distributions differ between domains: perfectly invariant features then force a lower bound on the joint error.

### Cited Findings
- Bound (Ben-David et al. 2010, Machine Learning; from knowledge, not re-fetched; also restated in DANN [arXiv:1505.07818](https://arxiv.org/abs/1505.07818)): for binary classification with 0-1 loss and any h ∈ H,
  ε_T(h) ≤ ε_S(h) + ½ d_{H∆H}(D_S, D_T) + λ, with λ = min_{h'∈H} [ε_S(h') + ε_T(h')], plus finite-sample terms. d_{H∆H} is estimated by training a domain classifier. The proxy A-distance is d̂_A = 2(1 − 2·err_domain), so a perfect domain classifier gives d̂_A = 2, the maximum.
- Zhao et al. build "a simple counterexample showing that, contrary to common belief", invariant representations plus small source error "are not sufficient to guarantee successful domain adaptation". The counterexample "exhibits conditional shift". They give an upper bound that accounts for conditional shift, and "an information-theoretic lower bound on the joint error of any domain adaptation method that attempts to learn invariant representations". This is "a fundamental tradeoff between learning invariant representations and achieving small joint error on both domains when the marginal label distributions differ" — [Zhao et al. 2019 (ICML), arXiv:1901.09453](https://arxiv.org/abs/1901.09453) (fetched)
- The lower bound, from the paper and not re-quoted verbatim: if d_JS(D_S^Y, D_T^Y) ≥ d_JS(D_S^Z, D_T^Z), then ε_S(h∘g) + ε_T(h∘g) ≥ ½ (d_JS(D_S^Y, D_T^Y) − d_JS(D_S^Z, D_T^Z))². Making features Z more invariant (smaller d_JS on Z) *raises* this floor — [arXiv:1901.09453](https://arxiv.org/abs/1901.09453)
- Lei et al.: a 2-layer MLP separates sim and real encoder features with ~100% accuracy, yet co-training transfers well. "Structured representation alignment", which balances "cross-domain representation alignment and domain discernibility", explains about 50% of performance variance — [arXiv:2604.13645](https://arxiv.org/html/2604.13645) (fetched)

### Inferences
- **Simple explanation for the IPB.** Imagine features squeezed so that sim and real images land in the same place. If sim demonstrations and real demonstrations need *different* actions for similar-looking inputs (controller differences, different object poses, different task mixes: the "label shift" of robotics), then after squeezing no single policy head can be right for both. Invariance has pushed the joint error up. Cheng et al. therefore align *joint* feature–state distributions, and Lei et al. keep the domains distinguishable.
- **The bound is vacuous in the sim-real co-training regime.** With ~100% domain separability (Lei), d̂_A ≈ 2, so the bound gives no useful guarantee. Separability alone therefore does not tell you where transfer fails. That motivates RQ2's task-information criterion, and the IPB can state it in one sentence.
- **Scope.** The bound is for classification with a fixed hypothesis class and i.i.d. data. Policies are regression/generative models evaluated in closed loop, with compounding error. "Used as motivation" (as the IPB says) is the correct framing.
- **"Invariance cannot reduce the joint error" is imprecise.** λ depends on the representation. A representation change can lower or raise it, and Zhao's result is that *enforcing invariance* can raise it (under label shift). Moving the simulation closer to reality shrinks both the divergence and the shift that causes the trade-off. Also, λ is not something that "only" shrinks with better simulation: a richer hypothesis class, or conditioning on domain (Lei's one-hot labels), can reduce it too.

### Gaps
- Ben-David et al. 2010 was not re-fetched in this session; the formula is standard.

---

## 7. What the cited VLA/policy probing papers actually did

### Takeaway
None of the three papers localises a sim-to-real gap with probes. Lei et al. analyse representation geometry and domain separability in co-trained diffusion policies. Kachaev et al. probe *general visual knowledge* (ImageNet-100 linear probes, VL-Think) in OpenVLA and add a mid-layer teacher-alignment loss. Häon et al. do causal steering, not probing. The IPB's descriptions are mostly fair but should be tightened.

### Cited Findings
- **Lei et al. 2026** (Lei, Liu, Maddukuri, Jiang, Zhu). They combine theory and experiments on co-training generative (diffusion/flow) policies and identify "structured representation alignment" (primary) and an "importance reweighting effect" (secondary). Setup: a transformer diffusion policy with a ResNet-18 vision backbone on robosuite tasks (NutAssembly, MugHang, MugCleanup), sim-and-sim and sim-and-real, plus a toy manifold model (≈3000 source vs ≈30 target samples). Measurements: UMAP, Wasserstein and Gromov–Wasserstein distances at the vision stem and encoder trunk, and an MLP domain classifier (~100% accuracy). Method: CFG-ADDA. Good mixing ratios lie in (0.016, 0.3) — [arXiv:2604.13645](https://arxiv.org/html/2604.13645) (fetched)
- **Kachaev et al.** (Kachaev, Kolosov, Zelezetsky, Kovalev, Panov; arXiv 29 Oct 2025). They find that "naive action fine-tuning leads to degradation of visual representations" in OpenVLA-7B compared with its VLM base (PrismaticVLM). ImageNet-100 linear-probe accuracy on visual features is 79.88% before fine-tuning, 77.48% after SFT, 82.13% with their alignment, and 87.31% for the C-RADIOv3 teacher. There is "domain-specific forgetting" on the VL-Think suite, diffuse attention in layers 14–24, and t-SNE cluster collapse. The fix is the mid-layer cosine alignment described in §4 — [arXiv:2510.25616](https://arxiv.org/html/2510.25616) (fetched)
- **Häon et al.** (Häon, Stocking, Chuang, Tomlin; CoRL 2025). π0 and OpenVLA: FFN activations are projected onto the token-embedding basis, sparse semantic directions (speed, direction) are found, and activation steering is shown zero-shot in LIBERO and on a UR5 — [arXiv:2509.00328](https://arxiv.org/abs/2509.00328) (fetched)

### Inferences
- §6 attributes Kachaev et al. to "robot policies". It should say "vision-language-action models (OpenVLA)". It probes general visual/semantic knowledge, not sim-vs-real task information.
- §6 lists Kachaev as "AAMAS 2026". I could not verify the venue: arXiv shows cs.LG/AI/RO, Oct 2025.
- Häon et al. is currently not cited in the IPB. It is the natural citation for "causal intervention on VLA hidden states is feasible" if the IPB adds a causal check.
- Lei et al. support two IPB claims directly: sim and real remain separable even when transfer works, and separability alone is not diagnostic. The paper does *not* localise information loss across layers.

### Gaps
- Kachaev et al.'s AAMAS acceptance is unverified.

---

## 8. Does "representation learning methods" fit RQ1–RQ3? Suggested wording for topic, §5, §8

### Takeaway
Only RQ2's alignment is representation learning in the strict (ICLR) sense. RQ1 is simulation design/attribution that *uses* representations as a measurement. RQ3 is active data selection plus twin correction and fine-tuning that *uses* representation distance as a selection signal. The honest umbrella is "representation-based" or "representation analysis and alignment". Alternatively, keep "representation learning" but make the representation the explicit common thread in each RQ.

### Cited Findings
- The IPB's own text supports this reading. RQ1's hypothesis uses "the change it induces in the representation of a fixed reference model" as a predictor (a measurement, not learning). RQ3 selects data using "the representation distance between simulated and real views". Only RQ2 trains representations ("aligning simulated and real representations") — IPB content/07-questions-hypotheses.md (local file).
- Kornblith et al., Hewitt & Liang and Elazar et al. are representation *analysis* methods; DANN, MMD, CORAL and OT are representation *learning* objectives — see sections 1–4 above.

### Inferences
- **Topic options** (keeping the K46 style):
  - (A, most honest) "Representation-based methods for simulation-to-reality generalization of deep learning models in physical AI" / "Metody oparte na reprezentacjach dla generalizacji modeli uczenia głębokiego między symulacją a rzeczywistością w fizycznej sztucznej inteligencji".
  - (B) "Analysis and alignment of learned representations for simulation-to-reality generalization of deep learning models in physical AI".
  - (C, keep current) Keep "Representation learning methods ..." but ensure §5/§8 say that each RQ either learns or is guided by the model's learned representations.
- **§5 goal sentence (proposed):** "Therefore, the dissertation aims to improve the generalization of deep learning models in real-to-simulation-to-real transfer with methods that analyse and align the models' learned representations, applied at the points of the loop where the simulation-to-reality gap arises: the regions of the digital twin whose errors change the representation, the stage of the model where task information is lost on real inputs, and the real data that most reduce the representational discrepancy."
- **§8 second paragraph (proposed insertion):** "Second, it aims to develop a way of locating the stage of a deep model at which task information available for simulated inputs is lost for real ones, using probes with control tasks and causal interventions, and of reducing the gap by aligning simulated and real representations at that stage."
- Also add "representation learning" to the §8 list of subfields only if the topic keeps the term. It already does, so that is consistent.

### Gaps
- Whether the K46 committee expects the strict meaning of "representation learning" is unknown; this is an editorial judgment.

---

## 9. Wording audit of §6, §7 and §9 (RQ2 and theory), with exact corrected phrasings

### Takeaway
Several sentences are imprecise in five ways. (1) They say the *gap* "arises" inside the model, when the gap is an output-level quantity. (2) The decodability criterion is ambiguous. (3) The statement about the joint-error term overclaims. (4) "Invariance is usually enforced at the input or final features" is contradicted by multi-layer and mid-layer methods. (5) Cheng et al. aligns observations with *proprioceptive states*, not actions.

### Cited Findings (each item: current text → problem → proposed text)
1. **§7 RQ2 question.** "Where inside a model trained in simulation does the simulation-to-reality gap arise, and can aligning representations at that stage reduce it?" The gap is a performance drop at the output; what arises inside is a representational discrepancy. **Proposed:** "At which stage of a model trained in simulation do the representations of real inputs first lose task information that is available for simulated inputs, and does aligning simulated and real representations at that stage reduce the simulation-to-reality gap?" (basis: probing measures decodability per layer — [arXiv:1909.03368](https://arxiv.org/abs/1909.03368))
2. **§7 RQ2 hypothesis, first sentence.** "there is a first stage of the model at which task information that can be decoded from simulated inputs can no longer be decoded from real ones." This is ambiguous (probe transfer vs re-trained probe), decodability is not monotone in depth, and no threshold is given. **Proposed:** "In both tasks, there is an identifiable earliest stage of the model at which a linear probe trained on simulated hidden states loses accuracy on the paired real hidden states well beyond a control-task baseline, and this lost information influences the predicted actions." (control tasks — [arXiv:1909.03368](https://arxiv.org/abs/1909.03368); decodable ≠ used — [arXiv:2006.00995](https://arxiv.org/abs/2006.00995))
3. **§7 RQ2 hypothesis, second sentence.** "Aligning simulated and real representations at that stage, from a few paired views, yields better generalization than aligning them at the input, at the final features or everywhere." The loss, the updated parameters and the fairness conditions are unspecified. **Proposed:** "Fine-tuning the layers up to that stage with a loss that matches real to paired simulated representations, using a few paired views, reduces the gap more than the same loss applied at the input, at the final features, at all stages, or at layers selected by gradient-based criteria, under equal real data and training budget." (Auto-RGN baseline — [arXiv:2210.11466](https://arxiv.org/html/2210.11466))
4. **§7 RQ2 last line.** "Probing of hidden states will locate this stage before any intervention." **Proposed:** "Probes with control tasks will locate this stage before any intervention, and activation patching of the probed subspace from simulated into real runs will test whether the model uses the lost information." (patching — [arXiv:2309.16042](https://arxiv.org/abs/2309.16042); subspace interventions — [arXiv:2303.02536](https://arxiv.org/abs/2303.02536))
5. **§7 RQ2 motivation.** "Models trained in simulation can rely on features absent in reality, such as reconstruction artifacts." This is plausible but unsourced. **Proposed:** "Models trained in simulation may rely on features absent in reality, such as reconstruction artifacts." "Even in models that transfer well, simulated and real inputs remain distinguishable" is supported; add [9]. ([arXiv:2604.13645](https://arxiv.org/html/2604.13645))
6. **§7 RQ3 theory sentence.** "Invariance does not reduce the joint error term, which shrinks only as the simulation gets closer to reality." This overclaims: λ depends on the representation, and Zhao shows invariance can *increase* it under label shift. "Only" is false because domain conditioning or a richer hypothesis class can also lower it. **Proposed:** "Enforcing invariance can increase the joint error term when simulated and real data differ in their action distributions [8], whereas bringing the simulation closer to reality reduces the discrepancy without this trade-off." ([arXiv:1901.09453](https://arxiv.org/abs/1901.09453))
7. **§6 para 1.** "... since invariance cannot reduce the joint error, correcting the simulation towards reality." Same issue. **Proposed:** "... and, since enforcing invariance can increase the joint error [8], correcting the simulation towards reality." Also note that the bound holds for classification and is used only as motivation.
8. **§6 para 3.** "Domain-adversarial training aligns features across domains [6]." **Proposed:** "Domain-adversarial training makes the marginal feature distributions of the two domains indistinguishable to a domain classifier [6]."
9. **§6 para 3 on [7].** "aligning the joint distributions of observations and actions" is inaccurate: Cheng et al. use encoder features plus *proprioceptive states*, because actions were unreliable across controllers. **Proposed:** "aligning the joint distributions of encoded observations and robot states in simulated and real data with unbalanced optimal transport improved co-trained policies in reality [7]." ([arXiv:2509.18631](https://arxiv.org/html/2509.18631))
10. **§6 para 3.** "Invariance is also usually enforced at a fixed location, the input or the final features." This is contradicted by multi-layer MMD/JAN and by mid-layer alignment (Kachaev, layer 16). **Proposed:** "Invariance is also usually enforced at locations chosen in advance, such as the input, the final features or a fixed set of layers, rather than where the gap is measured to arise."
11. **§6 para 5.** "Probing ... showed that action fine-tuning degrades the visual representations of robot policies [19], and the best layers to adapt depend on the type of shift [20]." [19] concerns VLAs (OpenVLA), and [20] is surgical fine-tuning, not probing. **Proposed:** "Probing, i.e., reading out information from hidden states with simple classifiers, showed that action fine-tuning degrades the visual representations of vision-language-action models [19]. Separately, selective fine-tuning showed that the best layers to adapt depend on the type of shift [20]." ([arXiv:2510.25616](https://arxiv.org/html/2510.25616); [arXiv:2210.11466](https://arxiv.org/abs/2210.11466))
12. **§6 para 5, last sentence.** Add "To our knowledge," before "the stage ... has not been located".
13. **§9 para 1.** "Domain adaptation theory relates the error of a model in reality to its error in simulation and to the discrepancy between the two." This omits the λ term that §6/§7 rely on. **Proposed:** "... to its error in simulation, the discrepancy between the two distributions and the error of the best model on both."
14. **§9 para 4, RQ2 sentence.** "simple probes on the hidden states of models will show at which stage task information decodable in simulation is lost on real inputs, and alignment at that stage will be compared with alternatives." **Proposed:** "For the second question, linear probes with control tasks, trained on simulated hidden states and tested on paired real ones, will show at which stage task information is lost on real inputs; causal interventions on hidden states will test whether this information is used; and a paired alignment loss attached at that stage will be compared with the same loss at the input, at the final features, at all stages and at layers chosen by existing criteria."

### Inferences
- Items 2, 3, 6, 9 and 10 are substantive (technical correctness). The rest are precision edits.
- Page limits: items 3 and 14 lengthen §7/§9. If space is tight, keep the probe-transfer and control-task wording (item 2) and the causal check (item 4) as the priority.

### Gaps
- The Polish reading copy was not checked. The same fixes should be mirrored there.

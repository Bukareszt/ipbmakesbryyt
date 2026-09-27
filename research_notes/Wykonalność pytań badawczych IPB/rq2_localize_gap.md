# RQ2 feasibility: locating where the sim-to-real gap arises inside a model, and aligning representations at that stage

Scope: can one PhD student solve RQ2 in about 1 to 1.5 years (2027 to 2028) on academic GPUs (A100/H100) without owning a robot? RQ2 and its hypothesis are as stated in §7 of the IPB: there is a first stage at which task information that is decodable from sim inputs stops being decodable from real inputs, and aligning at that stage with few paired views beats aligning at the input, at the final features, or everywhere. The method (§9) uses simple probes on hidden states, followed by alignment at the located stage. All arXiv IDs below were checked against the arXiv API on 2026-09-27 (title, first author and date match). Repository and model facts come from the GitHub or HuggingFace pages cited.

Overall verdict (inference, see details per question): **solvable in a scoped form.** Every building block exists and has open code: open-weight models with accessible hidden states, a layer-resolved probing methodology for VLAs, alignment losses for sim-real co-training, and paired or pairable sim/real data. No published work does exactly this, which gives the novelty. That is also the main risk: nobody has yet shown that the gap *localizes* to one layer. The minimum viable version (MVP) is small models (Diffusion Policy/ResNet-18 or Octo for manipulation, ViNT/NoMaD for navigation) fine-tuned in the twin, with probing on frozen checkpoints plus a layer-sweep alignment ablation. This fits comfortably in about 12 months and roughly 1–3k A100-hours. OpenVLA/pi0 should be treated as a stretch or "probe-only" extension.

---

## Q1. Probing and interpretability of robot policies and VLAs: who probes hidden states, what they found, and whether methods and code are usable

### Takeaway
Since late 2025 a small but fast-growing literature has done layer-resolved linear probing, activation injection and steering on OpenVLA, pi0/pi0.5, SmolVLA, GR00T and X-VLA, and the methods are routine and cheap. **None of it localizes a sim-to-real gap layer by layer.** The closest work (Lei et al. 2026) measures sim/real alignment at only two stages, finds that domain identity stays ~100% decodable even when co-training works, and argues that the gap must be characterized by *task-relevant* alignment rather than domain indistinguishability. That directly supports the IPB's choice to probe task information instead of domain identity.

### Cited Findings
- **Lei et al. 2026, arXiv:2604.13645**, "A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies". It identifies two effects: "structured representation alignment", a balance between cross-domain representation alignment and domain discernibility that "plays a primary role in downstream performance", and a secondary "importance reweighting effect". It is validated on a toy model plus sim-and-sim and sim-and-real manipulation — [arXiv abstract](https://arxiv.org/abs/2604.13645)
  - Setup: a transformer-based diffusion policy with a ResNet-18 vision backbone; robosuite tasks NutAssembly, MugHang and MugCleanup; 50 target-domain demos per task; about 3000 MimicGen sim trajectories; one real robot with calibrated camera — [arXiv HTML](https://arxiv.org/html/2604.13645v1)
  - Stage-wise analysis covers only **two stages**: features after the vision stem ("local geometry alignment", via Gromov-Wasserstein) and the final encoder-trunk output ("representation alignment in global space", via Wasserstein). The distance/success correlations (Spearman/Pearson) are about 0.6–0.8 — [arXiv HTML](https://arxiv.org/html/2604.13645v1)
  - A 2-layer MLP domain classifier reaches about 100% accuracy, so representations stay domain-discernible even when co-training succeeds — [arXiv HTML](https://arxiv.org/html/2604.13645v1)
  - The proposed method, CFG-ADDA (classifier-free guidance on a domain label plus an adversarial discriminator on the remaining dims), gives sim-and-sim 21/30 vs 15.3/30 for baseline co-training, and sim-and-real about 74% success, roughly 20 points above standard co-training. Project page: https://science-of-co-training.github.io/. The fetched page did not show a GitHub link, and compute is not reported beyond "TACC" — [arXiv HTML](https://arxiv.org/html/2604.13645v1)
- **Kachaev et al. 2025, arXiv:2510.25616**, "Don't Blind Your VLA". Naive action fine-tuning degrades visual representations of OpenVLA-7B relative to its base PrismaticVLM. They show this with linear probes (ImageNet-100 on patch embeddings), attention maps (middle layers 14–24 become "diffuse, noisy") and t-SNE. Their fix aligns **one middle layer (layer 16, chosen empirically)** to a frozen C-RADIOv3 teacher with a patch-wise cosine loss (λ=0.2) through a frozen 4096→768 projector. OOD gains are up to about 10% relative (e.g. semantic 0.49→0.61, vision 0.74→0.83). Code: https://blind-vla-paper.github.io. Compute is not stated beyond "negligible overhead" — [arXiv abstract](https://arxiv.org/abs/2510.25616), [arXiv HTML](https://arxiv.org/html/2510.25616v1)
- **Häon et al. 2025, arXiv:2509.00328**, "Mechanistic interpretability for steering VLAs". They project FFN activations of pi0 and OpenVLA onto the token-embedding basis, find sparse semantic directions (speed, direction) that are causally linked to actions, and steer zero-shot in LIBERO and on a UR5. Action-related tokens appear in every layer but concentrate in late layers ("there is not a hard transition" from task to control). Early-layer interventions had small effect (μ=0.007 vs 0.086 late). Hardware: one H100 for sim. **No code repository is given in the paper** — [arXiv abstract](https://arxiv.org/abs/2509.00328), [arXiv HTML](https://arxiv.org/html/2509.00328v1)
- **Grant et al. 2026, arXiv:2603.19233**, "Not All Features Are Created Equal". Activation injection, SAEs and linear probes on six VLAs from 80M to 7B parameters, over 394,000+ rollout episodes and four benchmarks. The visual pathway dominates action generation, and cross-task injection gives "spatially bound motor programs tied to scene coordinates". In pi0.5, SmolVLA and GR00T, the expert pathways encode motor programs and the VLM pathways encode goal semantics in separable subspaces. They release the Action Atlas explorer (https://action-atlas.com) — [arXiv](https://arxiv.org/abs/2603.19233)
- **Liao et al. 2026, arXiv:2607.03372**. Layer-resolved linear probing plus causal interchange interventions on three frozen VLAs from two architecture families. Past-frame content stays linearly decodable throughout the network, but the action readout progressively loses dependence on history with depth. This is a directly reusable template for a "decodability-per-layer" curve — [arXiv](https://arxiv.org/abs/2607.03372)
- **Bhardwaj et al. 2026, arXiv:2608.13474**. Task progress is linearly readable from the pi0.5 residual stream, is already present in the pretrained PaliGemma backbone, and a probe works as an OOD detector — [arXiv](https://arxiv.org/abs/2608.13474)
- **Mahato et al. 2026, arXiv:2606.29699**. A layer-16 logistic probe on OpenVLA MLP activations under visual shift (occlusion) gets AUROC 0.972 retrospectively but 0.689 on a different shift (camera jitter), and fires 3.32 false warnings per clean episode. The authors state that "strong retrospective discrimination does not imply operationally quiet warning behavior" — [arXiv](https://arxiv.org/abs/2606.29699)
- **Yang et al. 2026, arXiv:2605.24642**. Linear probing quantifies a "geometric gap" between the GR00T-N1.5 VLA and the VGGT geometric foundation model, i.e. geometric quantities can be probed from VLA features — [arXiv](https://arxiv.org/abs/2605.24642)
- **Molinari et al. 2025, arXiv:2509.24559**. Linear and nonlinear probes across OpenVLA layers predict state-transition vectors above embedding baselines, evidence for an internal world model — [arXiv](https://arxiv.org/abs/2509.24559)
- Navigation: a targeted search found **no work that probes the hidden states of GNM/ViNT/NoMaD**. Navigation interpretability found in the search is limited to RL agents in synthetic mazes (e.g. arXiv:2504.11419) — [arXiv](https://arxiv.org/abs/2504.11419)
- Probe methodology caveats (canonical, pre-2022 but still the standard): probe accuracy can reflect the probe's own capacity, so control tasks and selectivity are needed (Hewitt & Liang 2019, arXiv:1909.03368), and probing shows correlation, not use (Belinkov, arXiv:2102.12452, Computational Linguistics 2022) — [Hewitt & Liang](https://arxiv.org/abs/1909.03368), [Belinkov](https://arxiv.org/abs/2102.12452)

### Inferences
- The probing toolkit (cache activations, fit per-layer linear or ridge probes, add control tasks and causal interventions) is mature and cheap. It is not a feasibility risk.
- Lei et al. is both the closest prior work and a competitor. They already say that the "alignment/discernibility balance" matters and give a method, but they look at only two stages, use only a diffusion policy with ResNet-18, and do not probe task variables. RQ2 has to position itself as "full layer-resolved, task-variable probing + controlled layer-sweep of the alignment site, in two tasks". This is a clear increment, but the paper must cite and beat CFG-ADDA or at least compare against it.
- Kachaev et al. is existing evidence that aligning **one middle layer** of a VLA beats doing nothing, but their alignment target is a VLM teacher, not a real-domain view. Their code is a practical starting point for the "align at layer k" machinery on OpenVLA.
- Häon et al. (no hard task-to-control transition) and Mahato et al. (probes do not transfer across shift types) are early warnings that the "first stage" may be a gradual slope rather than a sharp step.
- Navigation probing is essentially virgin territory. That is good for novelty, but means no reference results exist.

### Gaps
- No paper found (2022–Sep 2026) that plots per-layer decodability of a task variable on sim vs paired real inputs for any robot policy. The core empirical claim of H2 is untested in the literature.
- Compute budgets for Lei et al. and Kachaev et al. are not reported in the pages fetched.
- Whether the Lei et al. code is public was not confirmed (only the project page URL).

---

## Q2. Can "task information" be operationalized for probing, and where do paired sim/real views come from?

### Takeaway
Yes. The four proposed variables (goal direction, object pose, collision/free-space distance, gripper state) are all computable from ground truth or metadata in both domains. Paired data exists for navigation, where ScanNet++ gives DSLR + iPhone + laser-scan captures of the same 460 scenes. For manipulation it has to be *built*: SIMPLER provides the real-background inpainting images and policy-matched environments but not frame-aligned sim/real pairs, and BridgeData real frames need a twin render with estimated camera and object poses. Building paired manipulation data is the costliest part of RQ2.

### Cited Findings
- ScanNet++ (Yeshwanth et al. 2023, arXiv:2308.11417): 460 indoor scenes, each with sub-millimetre laser scan, 280,000 registered 33-MP DSLR images and over 3.7M iPhone RGB-D frames. Commodity and high-end captures of the same scene are coupled — [arXiv](https://arxiv.org/abs/2308.11417)
- EmbodiedSplat (Chhablani et al. 2025, arXiv:2509.17430, ICCV 2025): iPhone captures → 3DGS → mesh in Habitat-Sim. Fine-tuning in the reconstructed scenes gives +20/+40 points of absolute success on real ImageNav over HM3D/HSSD zero-shot, with sim-vs-real correlation 0.87–0.97. This shows a real-to-sim navigation pipeline of exactly the needed kind exists — [arXiv](https://arxiv.org/abs/2509.17430), [ICCV paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Chhablani_EmbodiedSplat_Personalized_Real-to-Sim-to-Real_Navigation_with_Gaussian_Splats_from_a_Mobile_ICCV_2025_paper.pdf)
- SIMPLER (Li et al. 2024, arXiv:2405.05941) makes "paired sim-and-real evaluations" of manipulation policies with visual matching. The repo ships real-world inpainting images (`data/real_inpainting/`) for visual matching and sim eval videos on HuggingFace, and supports RT-1 and Octo. The README does not mention OpenVLA — [arXiv](https://arxiv.org/abs/2405.05941), [GitHub](https://github.com/simpler-env/SimplerEnv)
- PolaRiS (Jain et al. 2025, arXiv:2512.16881) turns short video scans of real scenes into interactive sim with neural reconstruction, co-trains on sim to close the remaining gap, and reports "extensive paired evaluations between simulation and the real world" for generalist policies — [arXiv](https://arxiv.org/abs/2512.16881)
- Real-is-Sim (arXiv:2504.03597): a dynamic Gaussian digital twin synchronized with the real world at 60 Hz, i.e. frame-synchronous sim/real pairs can be produced when a robot is available — [arXiv](https://arxiv.org/abs/2504.03597)
- Probed geometric quantities are known to be linearly decodable from VLA features to a measurable degree (the "geometric gap" in GR00T-N1.5 vs VGGT, arXiv:2605.24642), as are task progress (arXiv:2608.13474) and state transitions (arXiv:2509.24559) — [2605.24642](https://arxiv.org/abs/2605.24642), [2608.13474](https://arxiv.org/abs/2608.13474), [2509.24559](https://arxiv.org/abs/2509.24559)

### Inferences
- **Navigation labels:** with ScanNet++ poses and the laser mesh, one can compute, for every real frame and for the twin render from the same pose: relative goal direction/distance, geodesic distance to goal, free-space distance to nearest obstacle along several headings, and traversability. The same labels hold for both views by construction, which makes it the cleanest paired probing setup available. The twin comes from one capture (e.g. iPhone), the real frames from the other (DSLR). This matches §9.
- **Manipulation labels:** in simulation, object pose, gripper state/aperture and end-effector-to-object distance are free. For real BridgeData/OXE frames, gripper state and EE pose come from proprioception in the dataset. Object pose must be estimated (e.g. from a twin fit, with noise), so probes on real frames will have label noise. This has to be quantified, e.g. by a noise ceiling from twin-fit residuals.
- "Few paired views" is realistic: aligned pairs come from re-rendering the twin at the logged real camera pose. For BridgeData the camera is not calibrated per episode, so pose estimation is needed. This is the SIMPLER visual-matching problem, and a scoped subset (a few Bridge/"toy kitchen" scenes that SIMPLER already models) is the practical choice.
- Continuous targets such as direction and distance should use ridge regression and report R² with a control-task baseline, so that a drop on real inputs is not a probe-capacity artifact.

### Gaps
- No public dataset found with *frame-aligned* sim/real pairs plus task labels for manipulation with the policies in question. It has to be built (estimate: 1–2 months).
- The exact release status of PolaRiS scenes and code was not checked.
- Whether ScanNet++ DSLR vs iPhone differences (sensor, exposure, FOV) confound "sim vs real" with "camera vs camera" needs a control (e.g. real-vs-real probing between the two real captures).

---

## Q3. Evidence that layer-specific (partial or targeted) alignment beats whole-model or input/output alignment

### Takeaway
There is good general evidence that the *best layer to adapt depends on the shift type*, and that adapting a subset can match or beat adapting everything under small target data (surgical fine-tuning). There is one VLA-specific instance of single middle-layer alignment helping OOD (Kachaev et al.). **No robotics paper directly compares sim-real alignment at input vs a probed intermediate layer vs final features vs everywhere.** Existing sim-real co-training alignment (Cheng et al. OT, Lei et al. CFG-ADDA) aligns only the encoder output. H2 is therefore novel but also unproven.

### Cited Findings
- Surgical fine-tuning (Lee et al. 2022, arXiv:2210.11466, ICLR 2023): selectively fine-tuning a subset of layers "matches or outperforms" standard approaches across seven datasets and three shift types. "For image corruptions, fine-tuning only the first few layers works best", and "fine-tuning more parameters on a small target dataset can cause information learned during pre-training to be forgotten". There is also a theoretical result for two-layer nets — [arXiv](https://arxiv.org/abs/2210.11466). (From memory of the paper body, not re-verified here: input-level shifts favour the first block, feature-level shifts the middle blocks, output-level shifts the last layer, and they propose automatic selection criteria. Check against the paper's tables before citing.)
- Selective layer fine-tuning in federated CLIP (arXiv:2408.15600): for CIFAR-10 mostly top layers are updated, while DomainNet (large domain shift) "necessitates extensive tuning of the middle layers" — [arXiv](https://arxiv.org/html/2408.15600)
- Cheng et al. 2025, arXiv:2509.18631 ("Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training"): an unbalanced-OT loss on the joint (encoder feature, proprioception/action) distribution, applied **at the encoder output** of Diffusion Policy (ResNet-18) or DP3 (PointNet). It uses 10–25 real demos, 200–1000 MimicGen sim trajectories per task, and six tasks. It reports up to 30% real-success improvement and generalization to scenarios seen only in sim. Baselines include MMD and standard co-training, but **there is no ablation on alignment layer**. Code and data: https://ot-sim2real.github.io/ — [arXiv](https://arxiv.org/abs/2509.18631), [HTML](https://arxiv.org/html/2509.18631v3)
- Lei et al. 2026 (arXiv:2604.13645): alignment at the encoder output with an adversarial discriminator plus domain-label CFG. The two stages studied (stem vs trunk) show different alignment types (local geometric vs global) — [arXiv HTML](https://arxiv.org/html/2604.13645v1)
- Kachaev et al. 2025 (arXiv:2510.25616): aligning one middle layer (16) of OpenVLA to a vision teacher improves OOD success by up to about 10% relative. The layer was chosen empirically — [HTML](https://arxiv.org/html/2510.25616v1)
- Found-adapt (Da et al., ICLR 2026, "Latent Adaptation of Foundation Policies for Sim-to-Real Transfer"): an adapter refines a latent representation from a small amount of target-domain data. This is again a single-site (latent) alignment without a layer comparison — [ML Anthology](https://mlanthology.org/iclr/2026/da2026iclr-latent/), [OpenReview](https://openreview.net/forum?id=yn9dzttHvT)

### Inferences
- The IPB's comparison set (input / final / everywhere / probed-stage) is exactly the missing ablation in Cheng et al. and Lei et al. The cheapest credible experiment is to take their released co-training setup (Diffusion Policy with ResNet-18, whose stages are clean: stem, res1–res4, pool, trunk), sweep the OT/MMD/adversarial loss over each stage, and check whether the probe-identified stage wins. That is roughly 6 sites × 3 seeds × a few tasks of small-model training, which is very affordable.
- Surgical fine-tuning predicts that for predominantly **appearance** gaps (3DGS artifacts, lighting) the best site is **early**, and for **geometry/semantic** gaps it is **middle**. This gives a falsifiable secondary prediction that also ties RQ2 to RQ1's error types.
- A plausible negative outcome is that "align at the final features" (as in Cheng/Lei) is already close to the best. The IPB wording should allow reporting "the probed stage is as good as the best swept site at lower cost", which is still a useful result.

### Gaps
- No source found comparing alignment sites for sim-to-real in robot policies or navigation.
- The per-shift-type table of surgical fine-tuning was not re-fetched (see note above).

---

## Q4. Open-weight models with accessible hidden states, and GPU memory

### Takeaway
All candidate models are open and their hidden states are accessible: OpenVLA through HF `transformers` (PyTorch), Octo (JAX), openpi pi0/pi0.5 (JAX, plus a partial PyTorch port), and GNM/ViNT/NoMaD (PyTorch, MIT). Inference and probing fit on one GPU. LoRA fine-tuning of OpenVLA needs about one 80 GB A100/H100, and pi0 LoRA needs >22.5 GB. The small models (Octo, ViNT/NoMaD, Diffusion Policy) can be fine-tuned many times over, which a layer-sweep with seeds requires.

### Cited Findings
- OpenVLA: 7B parameters, Llama-2 backbone plus DINOv2+SigLIP fused vision encoder, trained on 970k real demos — [arXiv:2406.09246](https://arxiv.org/abs/2406.09246). LoRA fine-tuning on BridgeData V2 is recommended on a single 80 GB A100, using about 72 GB at batch 16 (smaller GPUs work with smaller batches plus gradient accumulation). Full fine-tuning is recommended on 8×A100. Checkpoints: openvla-7b, openvla-v01-7b, and LIBERO-fine-tuned variants — [GitHub](https://github.com/openvla/openvla)
- openpi (pi0, pi0-FAST, pi0.5, plus DROID/ALOHA/LIBERO fine-tunes): inference >8 GB, LoRA >22.5 GB, full fine-tuning >70 GB (A100/H100 80 GB). The PyTorch port covers pi0/pi0.5 but LoRA, FSDP, mixed precision and EMA remain JAX-only — [GitHub](https://github.com/Physical-Intelligence/openpi)
- Octo-Base-1.5: 93M parameters (ViT-B scale), MIT licence, 256×256 primary + 128×128 wrist images, window 2, diffusion head predicting 7-D actions 4 steps ahead, trained on 26 OXE datasets (Fractal, Kuka and Bridge each 17% of batches). JAX — [HuggingFace](https://huggingface.co/rail-berkeley/octo-base-1.5), [arXiv:2405.12213](https://arxiv.org/abs/2405.12213)
- GNM/ViNT/NoMaD: checkpoints released, MIT licence, PyTorch, trained on RECON, TartanDrive, SCAND, GoStanford2, SACSoN/HuRoN and additional unreleased data. Deployment targets LoCoBot/Jetson Orin Nano, i.e. the models are small. The README does not state parameter counts — [GitHub](https://github.com/robodhruv/visualnav-transformer), [ViNT arXiv:2306.14846](https://arxiv.org/abs/2306.14846)
- SIMPLER runs on an NVIDIA GPU (ray-tracing environments are slow on non-RTX cards such as the A100), and there is a ManiSkill3 GPU-parallel branch that is "10-15x faster" — [GitHub](https://github.com/simpler-env/SimplerEnv)
- Probing precedent on these exact models: OpenVLA layer 16 (arXiv:2606.29699, 2510.25616), pi0 and OpenVLA FFN layers (2509.00328), pi0.5 residual stream (2608.13474), six VLAs up to 7B (2603.19233) — see Q1 links.

### Inferences
- Caching activations is cheap. For example, 20k frames × 33 OpenVLA layers × 4096 dims, mean-pooled, in fp16 is about 5 GB. Per-token caching is about 256× larger, so cache pooled or selected tokens. A forward pass of OpenVLA in bf16 fits on a 24–40 GB card. (The ~15 GB bf16 inference figure is recalled from the OpenVLA paper and not re-verified here.)
- Note for the A100 specifically: SIMPLER's ray-traced setups are slow on non-RTX GPUs. Plan rendering on RTX-class nodes, or use the non-ray-traced/ManiSkill3 path.
- **Important mismatch:** GNM/ViNT/NoMaD and OpenVLA/Octo/pi0 are pretrained on *real* data, not "trained in simulation". For RQ2 as worded, the model must first be fine-tuned (or trained) in the twin. Only then does "sim-decodable but not real-decodable" have the intended meaning. The alternative is to state that for pretrained real-data models the analysis is of the reverse (real→sim) gap, which SIMPLER-style evaluation already measures.
- A layer sweep × seeds × two tasks is only affordable for small models. OpenVLA at 7B allows one LoRA run in about 1–2 GPU-days, so a 6-site × 3-seed sweep is about 20–40 GPU-days per task. That is possible on PLGrid but would dominate the budget. Recommended: small models for the full sweep, OpenVLA or pi0 only for probe-only analysis plus one or two alignment runs at the located layer.

### Gaps
- Exact parameter counts of ViNT/NoMaD not verified here (commonly cited as tens of millions).
- OpenVLA LoRA wall-clock per run was not found in a primary source.
- Maturity of the Octo PyTorch port was not checked.

---

## Q5. What could make RQ2 unsolvable? Failure modes, minimum viable version, fallback, compute and time

### Takeaway
The main scientific risk is that there is **no sharp first stage**: task decodability on real inputs may decline gradually, or be fine everywhere and fail only at the action readout. Some evidence points this way: the "no hard transition" finding of Häon et al., and Lei et al.'s point that success correlates with alignment, not with loss of discernibility. The main practical risk is paired manipulation data. Neither risk makes RQ2 unsolvable, provided the hypothesis is phrased so that the layer-resolved localization curve is itself the result, and the alignment-site sweep is reported whatever it shows.

### Cited Findings
- Gradual rather than discrete: in pi0 and OpenVLA "there is not a hard transition" from task to control across layers, and action-related directions exist in every layer — [arXiv HTML 2509.00328](https://arxiv.org/html/2509.00328v1)
- Domain identity stays about 100% decodable even in well-transferring co-trained policies, so a domain probe cannot localize the gap. This supports probing task variables instead, as the IPB does — [arXiv HTML 2604.13645](https://arxiv.org/html/2604.13645v1)
- Probe reliability: a probe fitted on one visual shift drops from AUROC 0.972 to 0.689 on another shift, with many false alarms on clean data — [arXiv:2606.29699](https://arxiv.org/abs/2606.29699). Probe accuracy can reflect probe capacity (control tasks needed) — [arXiv:1909.03368](https://arxiv.org/abs/1909.03368). Probing shows correlation, not causal use — [arXiv:2102.12452](https://arxiv.org/abs/2102.12452)
- History and other information stays decodable throughout the network while the action readout stops using it (decodable ≠ used) — [arXiv:2607.03372](https://arxiv.org/abs/2607.03372)
- VLA behaviour is dominated by the visual pathway and tied to scene coordinates — [arXiv:2603.19233](https://arxiv.org/abs/2603.19233). This suggests that for VLAs the gap is likely to show up early (vision encoder / first LLM layers), which is testable.
- Action fine-tuning itself degrades visual representations in middle layers of OpenVLA — [arXiv:2510.25616](https://arxiv.org/abs/2510.25616). This is a confound: twin fine-tuning may create a "stage" that reflects forgetting rather than the sim-real gap.

### Inferences

**Failure modes and mitigations**
1. *No single first stage*: the real-input decodability drops gradually. Mitigation: define the stage operationally (the first layer where the sim-real decodability difference exceeds a threshold or reaches X% of its final value, with bootstrap CIs over scenes), and report the whole curve. Hypothesis-side fallback: "the curve's knee predicts the best alignment site" (a weaker claim).
2. *Task info is fully decodable on real inputs at all layers* and only the readout fails (decodable ≠ used). Mitigation: add causal tests, e.g. patch real-input activations with the paired sim activations at layer k (interchange intervention, as in 2607.03372) and measure action error recovery. This "causal localization" is more robust than probes and costs only forward passes.
3. *Probe artifacts*: label noise on real manipulation frames, probe capacity, and camera differences (DSLR vs iPhone). Mitigations: linear/ridge probes only, control tasks, a real-vs-real baseline between the two real captures, and a noise ceiling.
4. *Too few pairs*: alignment with 10s–100s of pairs may overfit. Cheng et al. work with 10–25 real demos and Lee et al. note that small target data favours fewer tuned parameters, which supports single-stage alignment.
5. *Model too large for sweeps*: restrict sweeps to small models (see MVP).
6. *"Trained in simulation" mismatch*: pretrained navigation and VLA models are real-data models, so the student must fine-tune them in the twin first (see Q4).
7. *Scoop risk*: Lei et al. (Apr 2026) and follow-ups are in exactly this space. By 2027–28 someone may publish a layer-wise sim-real analysis. Mitigations: the navigation side (unexplored) plus coupling to RQ1 error types gives differentiation.

**Minimum viable version (about 8–10 months, 1 student)**
- Manipulation: Diffusion Policy with ResNet-18 co-trained on sim + few real, reusing the Cheng et al. OT code/tasks (https://ot-sim2real.github.io/). Paired views: SIMPLER Bridge/Google-robot scenes with the real frames and re-rendered twin frames. Also Octo-Base (93M) fine-tuned in SIMPLER as a second model.
- Navigation: ViNT or NoMaD fine-tuned in 3DGS/mesh twins of about 10–20 ScanNet++ scenes (built from iPhone), probed on DSLR frames at the same poses. Labels: goal direction/distance and free-space distance.
- Analysis: per-layer ridge probes (sim-train → sim-test vs sim-train → real-test, and real-train → real-test as a ceiling), plus interchange interventions at each stage.
- Intervention: MMD/OT/CORAL alignment on paired views at {input via image translation or augmentation, each backbone stage, final features, all stages}, 3 seeds. Metrics: open-loop action error on held-out real frames, SIMPLER success, and success in held-out twin or reference simulation.

**Compute estimate (inference; order-of-magnitude, not from a source)**
- Twin building: about 20 ScanNet++ scenes × about 0.5–1 GPU-h of 3DGS each ≈ 20 GPU-h. A few SIMPLER/Bridge scenes are negligible.
- Small-model training/fine-tuning: Diffusion Policy/ViNT-scale runs of about 5–20 GPU-h each × (6 sites × 3 seeds × 2–3 tasks per domain) ≈ 1–2k GPU-h in total.
- Probing: activation caching plus probes < 100 GPU-h.
- Optional OpenVLA/pi0 stretch: probe-only is about 50 GPU-h. Alignment at 1–2 layers × 3 seeds with LoRA (1×80 GB) is about 0.5–1k GPU-h.
- Total ≈ 1.5–3.5k A100-hours. This fits a standard PLGrid grant.

**Fallback if H2 fails**
- Report the localization curves plus the sweep as an empirical characterization ("where the gap lives, and whether the site matters"). It remains publishable as an analysis paper (the Lei et al. style).
- Replace "first stage" with "stage of maximal causal effect" from interchange interventions.
- Feed the per-layer sim-real representation distance into RQ3 (data selection) and RQ4 (predicting transfer). The IPB already plans this, so a negative H2 still yields a usable measurement.

**Time estimate:** 12–15 months for MVP plus a paper (analysis + sweep in both tasks), consistent with the 1–1.5-year window, **provided** RQ1's twins/pipeline (ScanNet++ twins, SIMPLER setup) are shared and ready at the start. If twins must be built from scratch for RQ2, add about 2–3 months.

### Gaps
- No quantitative evidence exists yet on whether sim-to-real task-information loss is sharp or gradual in any robot policy. This is the key unknown and can only be settled empirically.
- The compute estimates above are the researcher's projections, not taken from papers (the relevant papers do not report compute).
- No evidence was found on the minimum number of paired views needed for stage-wise alignment in robotics.

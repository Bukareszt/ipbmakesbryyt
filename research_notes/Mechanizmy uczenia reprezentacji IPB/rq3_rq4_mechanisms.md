# RQ3 and RQ4 mechanisms: selecting real data, correcting twin and model, predicting transfer

Scope: how the mechanisms behind RQ3 and RQ4 of the IPB work technically (content/07-questions-hypotheses.md, 09-methods.md, 06-state-of-the-art.md, visible text only), with a wording check. Every formula and number below was read from the original PDFs (downloaded from arXiv on 27 Sep 2026 and converted with pdftotext) unless marked as an inference. Complements `research_notes/Wykonalność pytań badawczych IPB/rq3_rq4_real_data_transfer.md`, which covers feasibility and is not repeated here.

## 1. Acquisition functions in active learning and active domain adaptation: how they are computed, typical gains, when random wins

### Takeaway
Acquisition functions fall into three groups. Uncertainty scores need only the model's prediction on a candidate: entropy, margin and BALD. Diversity scores need only embeddings: core-set. Hybrid scores use both: BADGE, CLUE and AADA. Under domain shift, hybrids beat random by about 1-2 accuracy points on DomainNet. Pure entropy and core-set often do worse than uniform random sampling, and on hard shifts they do so consistently. For RQ3 this means the proposed composite score must be benchmarked against a strong random baseline, and the effect size should be expected to be small.

### Cited Findings
- **Entropy (uncertainty sampling).** H(Y|x) = −Σ_c p_θ(c|x) log p_θ(c|x); pick the top-B instances. **Margin** picks the smallest difference between the top-2 class scores — [CLUE, arXiv:2010.08666](https://arxiv.org/abs/2010.08666) (Sec. 3.2 and baseline list).
- **BALD** expresses information gain as a difference of predictive entropies: I(y; θ | x, D) = H[y|x,D] − E_{θ~p(θ|D)} H[y|x,θ]. This selects points where the model is uncertain on average but individual posterior samples are confident, i.e. where the posterior samples disagree — [Houlsby et al. 2011, arXiv:1112.5745](https://arxiv.org/abs/1112.5745). Gal et al. made it practical for deep image models by approximating the posterior with MC dropout — [arXiv:1703.02910](https://arxiv.org/abs/1703.02910). (The formula is the standard statement of the paper's "information gain in terms of predictive entropies". The abstract confirms the approach; I checked the formula against the abstract only, not the full text.)
- **Core-set** treats active learning as core-set selection: "choosing set of points such that a model learned over the selected subset is competitive for the remaining data points". In practice this is greedy k-center in embedding space, i.e. picking the point farthest from the already selected or labelled points. The authors also report that "many of the active learning heuristics in the literature are not effective when applied to CNNs in batch setting" — [Sener & Savarese, arXiv:1708.00489](https://arxiv.org/abs/1708.00489).
- **BADGE** "samples groups of points that are disparate and high-magnitude when represented in a hallucinated gradient space". This is the gradient of the loss with respect to the last layer, computed with the predicted label, and followed by k-means++ seeding — [arXiv:1906.03671](https://arxiv.org/abs/1906.03671).
- **CLUE (Prabhu et al. 2021)**, exact mechanism — [arXiv:2010.08666](https://arxiv.org/abs/2010.08666), Sec. 3.2 and Alg. 1:
  (i) Compute the entropy H(Y|x) of every unlabelled target instance. Under shift, entropy is read as capturing "both uncertainty and domainness", via an implicit domain classifier p(d(x)=1) = H(Y|x)/log C.
  (ii) Take the penultimate-layer embeddings φ(x).
  (iii) Solve an uncertainty-weighted set-partitioning objective, argmin_{S,μ} Σ_k (1/Z_k) Σ_{x∈X_k} H(Y|x)·||φ(x) − μ_k||², with Z_k = Σ_{x∈X_k} H(Y|x). The paper describes this as "weighted population variance". It is NP-hard and is approximated with weighted K-means with K = B (the per-round budget).
  (iv) Acquire the instance nearest to each centroid.
  A softmax temperature T trades uncertainty against diversity. Higher T gives flatter uncertainties, so diversity matters more.
- **CLUE numbers (DomainNet, ResNet-34, 3 runs, 4 shifts; Table 1, 4-shift average at 1k/2k/5k labels).**
  - Fine-tuning from source: uniform random 39.5/42.9/47.5; entropy 38.1/41.3/46.4; margin 39.6/42.9/47.7; core-set 38.4/41.3/45.6; BADGE 39.8/43.6/48.3; CLUE 40.7/44.3/48.6.
  - With MME: uniform 42.1/45.7/49.8; entropy 40.4/43.5/48.2; CLUE 43.1/46.8/51.3.
  - With DANN: AADA 40.3/43.3/47.6; CLUE 41.9/45.4/49.6.
  - So CLUE's gain over uniform random is about 1.0-1.4 points. Entropy and core-set fall *below* random.
  The authors state that uncertainty-based (margin, entropy) and diversity-based (core-set) approaches "generalize poorly to challenging shifts ... frequently underperforming even random sampling". Gains on DIGITS and Office are larger: at B = 30 on SVHN→MNIST, CLUE beats margin, core-set and BADGE by 1.9%, 12.3% and a third figure truncated in the extracted text — [arXiv:2010.08666](https://arxiv.org/abs/2010.08666).
- **AADA (Su et al. 2020)**, exact mechanism — [arXiv:1904.07848](https://arxiv.org/abs/1904.07848), Eqs. 4-5:
  - Train a DANN. With adversarial training the optimal discriminator is G*_d(x̂) = p_S(x)/(p_S(x)+p_T(x)), so the importance weight is w(x) = p_T/p_S = (1−G*_d)/G*_d.
  - The selection score is s(x) = [(1 − G*_d(G_f(x)))/G*_d(G_f(x))] · H(G_y(G_f(x))), i.e. "targetness" times entropy. The entropy is used as a lower bound on the cross-entropy risk.
  - Result: on a digits shift, AADA reached 95% accuracy with 160 labels, while random needed about twice as many. At 1000 labels AADA "performs similarly as random selection (97.5%)".
- **When random wins.**
  - "Under strong regularization, AL methods show marginal or no advantage over the random sampling baseline", and gains are "inconsistent" under identical settings — [arXiv:2002.09564](https://arxiv.org/abs/2002.09564).
  - AL methods "barely perform better than the random baseline" unless combined with semi-supervised learning — [arXiv:1912.05361](https://arxiv.org/abs/1912.05361).
  - At low budgets, "typical examples are best queried", while "unrepresentative examples are best queried when the budget is large". Uncertainty-type selection therefore suits high budgets, and at very low budgets representativeness (TypiClust) beats it — [Hacohen et al., arXiv:2202.02794](https://arxiv.org/abs/2202.02794).

### Inferences
- RQ3's proposed score is structurally a hybrid of the AADA kind. It combines an uncertainty term (3DGS reconstruction uncertainty), a "targetness" or domain-distance term (the sim-real representation distance, analogous to (1−G_d)/G_d) and a task-relevance term (action sensitivity). To avoid redundant picks, it needs a diversity step (CLUE-style weighted K-means over the candidate embeddings, or k-center). Without one, a top-B ranking of an uncertainty score will pick clustered, redundant views. This is the failure mode of entropy in CLUE's Fig. 3.
- Given Hacohen et al., the per-image composite score may lose to a representativeness-based or random choice at the smallest budgets (a few images per scene). RQ3 should report results as a curve over budgets, not at a single budget.
- Baselines for RQ3 should include uniform random, a pure reconstruction-uncertainty rule (FisherRF, see §2), a pure diversity rule (k-center on embeddings), failure-driven selection (TwinRL) and one hybrid active domain adaptation method (CLUE). Without them, "beats random and failure-driven" does not show that the particular composite is needed.

### Gaps
- No active domain adaptation paper was found whose target is a policy (action regression) rather than classification. Entropy is undefined for deterministic continuous-action policies. Alternatives are ensemble variance of actions (BALD-like), or the diffusion-policy sample variance. These are not validated as acquisition functions for sim-to-real.

## 2. Correcting a simulator or twin from real data: system identification, SimOpt, ASID, 3DGS refinement

### Takeaway
All physics-correction methods use real data the same way. They replay the real actions in simulation and minimize a trajectory discrepancy over simulator parameters, as a point estimate or a distribution. They differ in which real data are collected:
- SimOpt uses rollouts of the current task policy.
- ASID uses one trajectory of an exploration policy designed in simulation to maximize Fisher information.
Visual correction of a 3DGS twin uses real images at known poses to continue photometric optimization. FisherRF's Fisher/Laplace criterion can rank candidate poses *before* the image is captured, because the score does not depend on the observed pixels.

### Cited Findings
- **SimOpt (Chebotar et al. 2019)** — [arXiv:1810.05687](https://arxiv.org/abs/1810.05687):
  - The simulation parameter distribution is Gaussian, p_φ(ξ) = N(μ, Σ) with full covariance. It is updated by min_{φ_{i+1}} E_{ξ~p_φ} E_{π_θ} D(τ^ob_ξ, τ^ob_real) s.t. D_KL(p_{φ_{i+1}} || p_{φ_i}) ≤ ε.
  - The discrepancy is D = w_ℓ1 Σ_t |W(o_{t,ξ} − o_{t,real})| + w_ℓ2 Σ_t ||W(o_{t,ξ} − o_{t,real})||²₂, where W holds per-dimension importance weights. A Gaussian filter handles trajectory misalignment.
  - Optimization is gradient-free and REPS-based, so the simulator is a black box.
  - Real data: rollouts of the *current task policy*. Swing-peg-in-hole used 3 real rollouts per iteration and succeeded after 2 SimOpt iterations. Drawer opening used 3 real rollouts per iteration, each iteration preceded by about 22 minutes of RL and followed by 20 update steps of the simulation parameters.
  - The policy is corrected only indirectly, by retraining it on the updated p_φ.
- **ASID (Memmel et al. 2024, ICLR)** — [arXiv:2404.12308](https://arxiv.org/abs/2404.12308):
  - (1) Exploration design in simulation. By the Cramér-Rao bound, E||θ̂ − θ*||² ≥ T⁻¹ tr(I(θ*)⁻¹). Assuming dynamics s_{h+1} = f_θ(s_h, a_h) + w_h with w_h ~ N(0, σ_w² I), the Fisher information is I(θ, π) = σ_w⁻² E_{p_θ(·|π)} [Σ_h ∇_θ f_θ(s_h, a_h) ∇_θ f_θ(s_h, a_h)^T]. The exploration policy solves the A-optimal design π_exp = argmin_π E_{θ~q0} tr(I(θ, π)⁻¹). Here θ* is unknown, so the objective averages over a domain-randomization prior q0. ∇_θ f is obtained by finite differences when the simulator is not differentiable, and π_exp is trained with PPO.
  - (2) System identification. A *single* real trajectory τ_real of π_exp is collected. The method then finds q_φ minimizing E_{θ~q_φ} E_{τ_sim~p_θ(·|A(τ_real))} ||τ_real − τ_sim||²₂, replaying the real action sequence, with REPS in simulation and CEM in real.
  - (3) The task policy is trained in the identified simulator and deployed zero-shot.
  - Results: real rod balancing succeeded 2/3, 1/3 and 3/3 (mass on left/middle/right) versus 0/3 for domain randomization. In simulation, rod tilt was 0.00-0.72° versus 4-27° for the baselines.
  - Intuition in the authors' words: go to states "for which the next state predicted by the dynamics is very sensitive to θ".
- **3DGS/NeRF refinement from new views, and choosing views** — [FisherRF, arXiv:2311.17874](https://arxiv.org/abs/2311.17874):
  - The next view is chosen by argmax over candidate poses x_acq of tr(H''[y_acq | x_acq, w*] · H''[w* | D_train]⁻¹).
  - Hessians are approximated by a Laplace/diagonal approximation, H'' ≈ diag(∇_w f(x,w*)^T ∇_w f(x,w*)) + λI, over 3DGS parameters.
  - Evaluation runs at "70 fps" with 3DGS. A per-pixel rendered uncertainty map is also defined.
  - The formula needs only the candidate *pose*, not its image, because the Fisher information of a Gaussian-likelihood model does not depend on the observed y.
  - Refinement itself means continuing standard 3DGS photometric optimization on the enlarged image set. This is standard 3DGS practice; I found no specific source for "incremental" refinement budgets.
- Post-hoc spatial uncertainty for a trained NeRF (Laplace approximation over a perturbation field) is also available — [Bayes' Rays, arXiv:2309.03185](https://arxiv.org/abs/2309.03185).
- A likelihood-free alternative for physics parameters is BayesSim, which computes a posterior over simulator parameters from real trajectories — [arXiv:1906.01728](https://arxiv.org/abs/1906.01728) (abstract level).

### Inferences
- The IPB's three signals map onto these mechanisms.
  - "Reconstruction uncertainty" is FisherRF or Bayes' Rays. It can be computed for candidate poses before any real image exists.
  - "Action sensitivity" is the policy-level analogue of ASID's ∇_θ f_θ. It asks: at which states does the output (next state for ASID, action for the IPB) change most when the uncertain twin parameters change?
  - A principled combined score is first order: the expected action change under reconstruction uncertainty, E_{δw~N(0,Σ_w)} ||a(render(w*+δw)) − a(render(w*))||. With a diagonal Σ_w this approximates tr(J Σ_w J^T), with J = ∂a/∂w (the chain rule through the differentiable 3DGS renderer). This parallels ASID's Fisher criterion, with 3DGS parameters in place of physics parameters and the policy in place of the dynamics.
  - The "representation distance between simulated and real views" needs the real image. It is therefore not a predictor of disagreement but a measurement, available only for candidates whose unlabelled real image is already in the pool.
- In the navigation proxy (ScanNet++), "correcting the twin" means 3DGS refinement with the selected DSLR frames. Physics correction (SimOpt/ASID) applies only to manipulation, and only in a sim-to-sim setting or with a robot.

### Gaps
- No paper was found that selects real views to refine a 3DGS twin *for a downstream policy*, i.e. with task-weighted rather than photometric information gain.

## 3. Correcting the model; how RialTo, TwinRL and sim-and-real co-training use real data, and what they select

### Takeaway
Model correction in the cited works is one of three things:
- A mixture loss over simulated and real data, with the co-training ratio α as a critical hyperparameter (Maddukuri et al.).
- A real-data imitation term added to sim-based distillation (RialTo).
- Real-world RL with a replay buffer pre-filled from the twin (TwinRL).
None of them *selects* real data by an acquisition function. TwinRL selects *initial configurations* for real rollouts by thresholding success in the twin, and does not update the twin from the real data. RialTo uses real data for both the twin (a scan) and the model (demos), but these are *different* data and are not selected.

### Cited Findings
- **Sim-and-real co-training (Maddukuri et al. 2025, RSS)** — [arXiv:2503.24361](https://arxiv.org/abs/2503.24361):
  - Loss: L_total(θ) = α·L(θ; D_sim) + (1−α)·L(θ; D_real), with L = −(1/|D|) Σ log π_θ(a_i|o_i). Equivalently, each batch element is drawn from simulation with probability α.
  - Tuning α: α = 0.9-0.99 was optimal and 0.99 was the default. At 99.5% and 99.9%, success dropped "from 95% to 60%".
  - Headline result: the abstract reports "an average of 38%" improvement. In-domain real success went from 45.3% (real only) to 83.2% (real + digital cousin + prior sim data), about 100 real demos per task, with 10,000 MimicGen demos per task in simulation.
  - Recommendations: task definitions shared across sim and real; aligned cameras "can improve performance"; sim data "orders of magnitude more" than real.
- **RialTo (Torne et al. 2024, RSS)** — [arXiv:2403.03949](https://arxiv.org/abs/2403.03949):
  - (a) The twin is built from a scan (Polycam, ARCode or NeRFStudio) with articulation added in a GUI.
  - (b) "Inverse distillation". A policy π_real(a|o) is trained by imitation on N real demos (point clouds, delta end-effector actions). It is executed in simulation to collect successful trajectories with privileged state, D_sim.
  - (c) RL fine-tuning of a state-based policy in simulation, with a BC term on D_sim.
  - (d) Teacher-student DAgger distillation to a point-cloud policy, co-trained with the real demos: max_θ α Σ_{sim} log π_θ(π_teacher(s_i)|o_i) + β Σ_{(o_i,a_i)∈D_real} log π_θ(a_i|o_i).
  - Fig. 5 compares with imitation from 15 demonstrations. The abstract reports a >67% robustness increase.
  - The real demos are not selected by any criterion, and the twin is not refined from the demos.
- **TwinRL (Xu et al. 2026, arXiv:2602.09023, v4 revised 19 May 2026)** — [arXiv:2602.09023](https://arxiv.org/abs/2602.09023):
  - Stage I: SFT with "exploration space expansion" (twin-synthesized demos outside the real-demo region). The twin is aligned to real observations with differentiable 3DGS rendering.
  - Stage II: parallel RL in the twin fills D_twin. The real replay buffer is initialized as D_real ← D_twin.
  - Stage III: real online RL with human-in-the-loop (HiL). The selection rule is explicit: "evaluate the current policy in the digital twin and construct a targeted set of initial configurations, S_target = { s0 | SR(s0) < τ }", where SR is the twin success rate and τ a proficiency threshold. "Episode resets [are] prioritized from S_target."
  - Results: near-100% success on 4 Franka tasks within about 20 minutes of real interaction.
  - I found no step that updates the twin from real rollouts.
- **Fine-tuning versus co-training.** Maddukuri et al. compare co-training with real-only training. Their recipe mixes the data rather than pretraining on sim and then fine-tuning — [arXiv:2503.24361](https://arxiv.org/abs/2503.24361). Lei et al. 2026 attribute co-training gains mainly to "structured representation alignment", i.e. a balance between cross-domain alignment and "domain discernibility", with an "importance reweighting effect" second — [arXiv:2604.13645](https://arxiv.org/abs/2604.13645).

### Inferences
- The "failure-driven (TwinRL-style)" baseline in RQ3 should be operationalized exactly as S_target = {candidates with twin success < τ}, sampled uniformly within S_target. In navigation, candidates are start poses or episodes. In manipulation, they are initial object configurations. In TwinRL this rule selects *where to act*, not *which images to label*. Adapted to an image budget, it becomes "acquire real views along episodes that fail in the twin".
- The "joint correction" arm is only well-defined if the same selected real data feed both corrections: 3DGS refinement of the twin, and a real-data loss term (co-training with ratio α, or paired-view alignment) for the model. The three arms (twin-only, model-only, both) must use the same selected set and the same compute. Otherwise "both > either" is confounded by extra effective data use.
- Co-training results show α is a first-order hyperparameter. RQ3 must tune α per arm on a validation split, or fix it across arms. Otherwise an untuned "model-only" arm could lose for reasons unrelated to selection.

### Gaps
- TwinRL's value of τ and the size of S_target were not extracted (they are in the text, but not in the parts I read).
- RialTo's co-training weights α and β were not extracted.

## 4. Action sensitivity: how it is computed

### Takeaway
Two standard families exist.
- Gradient-based: the norm of the Jacobian of the action with respect to the input (or a Jacobian-vector product along a chosen direction). This follows Simonyan et al.'s saliency, "the gradient of the class score with respect to the input image".
- Perturbation-based: the change in the policy output when part of the input is perturbed (blurred or replaced), as in Greydanus et al. for RL agents.
For RQ3 the sensitivity must be taken with respect to *twin-specific* perturbations (reconstruction uncertainty), not generic pixel noise. Otherwise it measures model fragility, not twin-reality disagreement.

### Cited Findings
- Gradient saliency computes "the gradient of the class score with respect to the input image" — [Simonyan et al., arXiv:1312.6034](https://arxiv.org/abs/1312.6034).
- Perturbation-based saliency for deep RL agents measures how the policy output changes when image regions are perturbed. It is used to show "what strong agents attend to" and "whether agents are making decisions for the right or wrong reasons" — [Greydanus et al., arXiv:1711.00138](https://arxiv.org/abs/1711.00138) (abstract. The exact blur-and-mask formula is from memory of the paper and was not re-read.)
- ASID's criterion is a parameter-sensitivity analogue: states where "the next state predicted by the dynamics is very sensitive to θ", with ∇_θ f computed by finite differences — [arXiv:2404.12308](https://arxiv.org/abs/2404.12308).

### Inferences
- Concrete definitions for a candidate pose or state c, with policy π, 3DGS parameters w and renderer R:
  - (a) Finite-difference or Monte Carlo: S(c) = E_{δw~q(δw)} ||π(R(w*+δw, c)) − π(R(w*, c))||, where q is the reconstruction posterior (Bayes' Rays or FisherRF diagonal).
  - (b) First order: S(c) ≈ sqrt(tr(J_c Σ_w J_c^T)) with J_c = ∂π/∂w, via autodiff through the 3DGS rasterizer.
  - (c) Task-level: the change in twin success or value when w is perturbed. This is costly but closest to "task-relevant".
- For discrete navigation actions, use the change in the action distribution (KL or total variation) instead of a norm. For diffusion or flow policies, use the distance between action-chunk means over several samples.

### Gaps
- No robotics paper was found that uses action sensitivity to 3DGS reconstruction uncertainty as an acquisition score. This part of the IPB appears novel, and it is unvalidated.

## 5. RQ4: measuring predictivity (SRCC), decomposing the gap (Xie et al.), and testing that a predictor beats simple baselines

### Takeaway
SRCC is the *Pearson* correlation between the simulated and real performance of n methods. Kadian et al. had n = 9. Xie et al. decompose the gap by shifting one factor at a time (gap = P_train − P_factor) and test pairs for compounding. Their difficulty ordering is consistent between simulation and a real robot, except for background. To claim that an attribution/localization predictor beats "raw gap" or "image discrepancy", one must correlate each predictor with the same outcome across held-out units and compare the two *dependent, overlapping* correlations with Williams'/Steiger's test or Zou's confidence interval. My simulations give roughly 60-80 units for r = 0.6 vs 0.3, and 100-140+ for smaller differences.

### Cited Findings
- **SRCC** — [Kadian et al., arXiv:1912.06321](https://arxiv.org/abs/1912.06321), Sec. IV-E. "Let (s_i, r_i) denote accuracy (episode success rate, SPL, etc.) of navigation method i in simulation and reality ... SRCC is the sample Pearson correlation."
  - 9 models, PointNav, a 6.5 m × 10 m room, 40.5 hours of real testing.
  - With CVPR19 Habitat settings, SRCC_Succ = 0.18 and SRCC_SPL = 0.603. After tuning simulator parameters (sliding off, actuation noise), SRCC_Succ = 0.844 and SRCC_SPL = 0.875. Rank reversals fell to 5 (13.8%).
- **Xie et al. 2024 (ICRA)** — [arXiv:2307.03659](https://arxiv.org/abs/2307.03659):
  - The environment is decomposed into factors (background, lighting, distractors, table texture, object texture, table position, camera position). Factor World has 19 tasks, 11 factors and >100 values per factor.
  - Gap per factor = P_T − P_F, averaged over 100 test environments that shift only factor F.
  - Pairs are compared with the metric (P_{A+B} − min(P_A, P_B))/min(P_A, P_B). For 16 of 21 pairs it lies in [−6%, 6%], i.e. "most pairs of factors do not have a compounding effect".
  - Ordering: backgrounds, distractors and lighting are easier; table texture and camera position are harder. It is consistent between simulation and a real RT-1 robot, but backgrounds were harder in Factor World and easiest on the real robot.
  - Real pair example: new table texture 52.8%; with a new background 55.6%; with new distractors 50.0%.
  - The gap closes from about 0.4 to <0.1 as training environments increase from 5 to 100.
- **Comparing correlations.** cocor implements tests for dependent correlations with overlapping or nonoverlapping variables, including Steiger's (1980) tests and Zou's (2007) confidence interval, in R and on the web — [Diedenhofen & Musch 2015, PLoS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0121945); [comparingcorrelations.org](http://comparingcorrelations.org/).
- **Own Monte Carlo power check.** Williams' t for r(outcome, A) vs r(outcome, B), with r(A,B) = 0.5, bivariate normal, α = 0.05, 4000 simulations, script run in the scratchpad. Power by effect size:

  | r_A vs r_B | n = 60 | n = 80 | n = 100 | n = 140 | n = 200 |
  |---|---|---|---|---|---|
  | 0.6 vs 0.3 | 0.79 | 0.89 | — | — | — |
  | 0.7 vs 0.5 | — | 0.69 | 0.78 | 0.91 | — |
  | 0.6 vs 0.4 | — | — | 0.68 | 0.82 | 0.93 |
  | 0.5 vs 0.3 | — | — | 0.60 | 0.76 | 0.90 |

  These results agree with the earlier Fisher-z estimates (~66 / ~107 / ~135) in the feasibility notes.

### Inferences
- **Recommended RQ4 protocol.**
  - Unit: a held-out scene × method pair.
  - Outcome: Δgap, the reduction of the sim-to-real (or sim-to-proxy-real) gap achieved by the method in that scene, or the real-success improvement.
  - Candidate predictors, all measured *before* applying the method and using only data the method may also use:
    - (i) attribution features from RQ1, e.g. the share of the gap removed by swapping in reference geometry or appearance;
    - (ii) localization features from RQ2, e.g. the layer of first probe drop and its size;
    - (iii) baselines: the base model's raw gap, image-level discrepancy (e.g. KID/FID or LPIPS between rendered and real views) and reconstruction error (PSNR).
  - Metric: Spearman ρ (robust to non-normal Δgap) or out-of-sample R²/AUROC for "transfers vs not". The primary test compares dependent overlapping correlations (Williams/Steiger, with a Zou CI), or a paired bootstrap over scenes of the difference in ρ.
  - Multiple predictors: use cross-validated regression (leave-scenes-out), and compare nested models with a paired test on held-out errors.
  - Pre-register the predictor definitions to avoid garden-of-forking-paths inflation.
- SRCC measures whether *simulation ranks methods* like reality does. RQ4's claim is different: whether *pre-measured shift properties predict a method's benefit*. An SRCC-style check (does twin evaluation rank the RQ1-3 methods as the real or proxy evaluation does) is a useful sanity check, but it is not the RQ4 test.
- Xie et al.'s one-factor-at-a-time design is the template for RQ1's "component swap" attribution. Their no-compounding finding (16/21 pairs) justifies additive attribution only approximately. RQ1/RQ4 should test for interactions (pairwise swaps) rather than assume additivity.
- Cross-task prediction (navigation → manipulation) will have few manipulation units (a handful of twins). By the table above it cannot reach adequate power, so it should be framed as exploratory.

### Gaps
- No prior work was found that predicts per-scene *method benefit* from representation-level shift measures, so there is no effect-size prior. The r values above are assumptions.
- Steiger 1980 and Zou 2007 were not read directly; the citation is via cocor.

## 6. Wording check of §7 and §9 (and related §6 sentences) for RQ3 and RQ4, with proposed corrections

### Takeaway
The main technical imprecisions are:
- The "joint error term" sentence overstates what shrinks it.
- "Predicted to disagree" is circular for the representation-distance signal, which needs the real view.
- "Sensitivity of the predicted action" lacks a perturbation.
- The budget unit, the candidate set and the equal-budget arms are unspecified.
- RQ4 conflates "explain" and "predict".
- "Measured before a method is applied" hides that the measurements need real or reference data.
- The RQ4 outcome and statistical test are undefined.
- §6 says prior methods correct "either" the model or the simulation, although RialTo uses real data for both (with different, unselected data).

### Cited Findings (basis for the corrections)
- The joint term λ is the error of the best joint hypothesis *in the hypothesis class on the given representation*, and invariance can increase it — [Zhao et al. 2019, arXiv:1901.09453](https://arxiv.org/abs/1901.09453) (cited in IPB as [8]; from knowledge of the paper, not re-read here). The term thus depends on the representation, not only on how close the simulation is to reality.
- Representation distance requires the real image, whereas FisherRF-type uncertainty needs only the pose — [arXiv:2311.17874](https://arxiv.org/abs/2311.17874).
- TwinRL's selection rule is SR_twin(s0) < τ over initial configurations — [arXiv:2602.09023](https://arxiv.org/abs/2602.09023).
- RialTo builds the twin from a real scan and co-trains the policy on real demos — [arXiv:2403.03949](https://arxiv.org/abs/2403.03949).
- ASID designs exploration in simulation for one real trajectory maximizing Fisher information — [arXiv:2404.12308](https://arxiv.org/abs/2404.12308).
- SRCC is a Pearson correlation — [arXiv:1912.06321](https://arxiv.org/abs/1912.06321).
- Active learning gains shrink or reverse depending on budget — [arXiv:2202.02794](https://arxiv.org/abs/2202.02794); [arXiv:2010.08666](https://arxiv.org/abs/2010.08666).

### Inferences (problem → proposed exact phrasing)

**§7, RQ3**
1. Title: "most efficiently correct both the simulation and the model". "Efficiently" is undefined, and "simulation" is inconsistent with "digital twin".
   → "**Which real data, chosen under a fixed budget, most reduce the simulation-to-reality gap when used to correct both the digital twin and the model?**"
2. "Real data are expensive, and existing methods use them to correct either the model or the simulation." This is inaccurate for RialTo.
   → "Real data are expensive, and existing methods select them to correct either the model or the simulation; where both are corrected, different and unselected real data serve each purpose."
3. "Invariance does not reduce the joint error term, which shrinks only as the simulation gets closer to reality." This is too strong.
   → "Invariance alone does not reduce the joint error term and can increase it; for a given representation, this term is reduced when the simulation reproduces the task-relevant properties of reality more closely."
4. "…correcting either one alone." Add the equal-budget and same-data condition.
   → "*Hypothesis:* At an equal budget, using the same selected real data to correct both the digital twin and the model reduces the gap more than using them to correct either one alone."
5. "The data should be selected where the twin is predicted to disagree with reality in task-relevant ways, as estimated from the reconstruction uncertainty, the representation distance between simulated and real views and the sensitivity of the predicted action." This is circular (distance needs the real view) and leaves "sensitivity" undefined.
   → "Candidate real observations should be selected where the twin is likely to disagree with reality in ways that affect the task. Each candidate is scored by the twin's reconstruction uncertainty at that viewpoint, by how much the model's action changes when the twin is perturbed within this uncertainty and, when an unlabelled real image of the candidate is available, by the distance between the model's representations of the rendered and the real view."
6. "Such selection is expected to beat random and failure-driven selection."
   → "Such selection is expected to beat random selection and selection of configurations where the model fails in the twin, as in TwinRL, especially at small budgets."
7. "Selection rules will be compared at equal budgets in both tasks, with unlabelled real images counted as real data." Add the unit.
   → "Selection rules will be compared at equal budgets in both tasks, counted in real images for navigation and in real episodes or frames for manipulation, with unlabelled real images included in the budget."

**§7, RQ4**
8. Title: "Do the improvements generalize … and which properties of the shift explain when they do?" The hypothesis is about prediction, not explanation, and "improvements" is vague.
   → "**Do the methods developed for the first three questions, applied with unchanged settings, improve generalization in unseen scenes and in the other task, and can properties of the shift measured beforehand predict when they do?**"
9. "…can be measured in a new scene or task before a method is applied." This hides the data it requires.
   → "…can be measured in a new scene or task from a reference reconstruction and a small set of paired simulated and real views, without applying or evaluating the method."
10. "These measurements predict whether the improvement transfers … better than simple indicators such as the raw size of the gap or the image-level discrepancy." The outcome and the comparison are undefined.
   → "Across held-out scenes, these measurements are more strongly rank-correlated with the reduction of the gap achieved by a method than simple indicators are, such as the gap of the base model or the image-level discrepancy between rendered and real views."
11. "This prediction will be tested across many held-out scenes of navigation and manipulation." "Many" is vague, and cross-task prediction is underpowered.
   → "This will be tested on about a hundred held-out navigation scenes by comparing dependent correlations, and, as an exploratory analysis, on the available manipulation scenes and between the tasks."

**§9**
12. "The third question concerns ways of selecting a small amount of real data used to correct both the twin and the model." Add the comparisons and mechanisms.
   → "For the third question, rules for selecting a small amount of real data will be compared at equal budgets with random and failure-driven selection. The selected data will refine the reconstruction of the twin and enter the training of the model, and correcting both will be compared with correcting only one."
13. "…to check whether the measured attribution and localization predict the improvement better than simple predictors."
   → "…to check whether the attribution and localization measured before applying a method predict its gain in each scene better than simple predictors, using rank correlations compared with tests for dependent correlations."
14. "…and on the simulation-to-reality gap, measured on held-out scenes…" Define the gap.
   → "…and on the simulation-to-reality gap, i.e., the difference between the performance of the same model in the twin and in reality or its reference, measured per held-out scene…"

**§6 (for consistency with RQ3)**
15. "active system identification collects the real trajectories most informative about physics [22]"
   → "active system identification designs, in simulation, an exploration policy whose real trajectory is most informative about physical parameters [22]".
16. "These methods correct either the model or the simulation."
   → "These methods use the selected real data to correct either the model or the simulation."
17. "To our knowledge, correcting both from the same selected data, guided by the twin's reconstruction uncertainty, has not been studied." This is acceptable as is. Optionally add "…and by the sensitivity of the model's actions to it".

### Gaps
- The Polish copy of the IPB was not checked. The same corrections would need translating.
- Whether the full RQ1-RQ2 texts use "simulation" and "digital twin" interchangeably elsewhere was not audited.

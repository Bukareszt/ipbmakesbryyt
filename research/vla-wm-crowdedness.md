# VLA/VLM + world models: crowdedness check and the H4(b) baseline (issue #32, Wave 15-U)

Checked on **2026-09-26** for pivot decision v5 (research/pivot-decision.md, top). Semantic Scholar (S2)
bulk search gave the counts and the top papers. The S2 batch API gave title, authors, date, venue and
abstract for every paper named below. arXiv abstract pages gave the author comments (venue notes). GitHub
and HuggingFace APIs gave code/weight licences. The arXiv query API returned HTTP 500 all day, so there are
no arXiv counts this time. Everything is from **abstracts, READMEs and model cards**, not full texts.

---

## TL;DR

1. **The guardrail is confirmed.** RL/IL fine-tuning of VLAs in simulation (S2 Q1: 1 → 3 → 40 → 126 papers
   per year, 2023 → 2026) and world models for VLA training and evaluation (Q2: 0 → 2 → 42 → 183) are
   **crowded and growing 3–4× a year**. Neither can be claimed as new. Well-funded groups set the pace
   (Physical Intelligence, NVIDIA Cosmos, Stanford/Finn, Tsinghua/RLinf, GigaAI).
2. **Real-to-sim twins for VLA fine-tuning** are a smaller niche (Q3: 0 → 2 → 15 → 33), and one paper sits
   right on top of the method: **TwinRL** (arXiv:2602.09023, Feb 2026). It builds a digital twin from a
   smartphone capture, runs parallel RL of a VLA in the twin, and then uses the twin to find
   "failure-prone yet informative configurations" for targeted real rollouts. It reports "only 20 minutes
   of on-robot interaction" for near-100% success on four tasks.
3. **The loop's real-data budget is still open.** Only 0 / 0 / 1 / 2 S2 papers a year match
   VLA ∧ twin ∧ data-efficiency (Q5), and none of them varies the real-data budget as an experimental
   variable.
   - **VLM-guided capture** for a twin is almost empty (Q4b: 0 / 0 / 1 / 2). The closest work, AREA3D
     (arXiv:2512.05131), uses VLM guidance for reconstruction quality, not for the downstream policy.
   - **Twin-grounded world models** exist as *representations* (GWM, ICCV 2025; PEGS) and as a *data
     engine* (GigaWorld-0: 3DGS + system identification + video generation). No paper uses a world model
     to cover the **twin's uncertain regions** under a counted real-data budget.
   - **Correcting the world model with real rollouts** exists (VLAW, arXiv:2602.12063), but its rollouts
     are not actively selected.
4. **The H4(b) baseline is a TwinRL-style pipeline** (worker T's §7 wording, coordinator message
   msg_65a79c659e58): uniform capture of the twin, domain randomization, RL fine-tuning of the same VLA in
   the twin, and random or failure-driven real trials. TwinRL has released code: `zhourui9813/TwinRL`, MIT,
   with "offline training code" and twin assets. Its README says Octo- and SERL-based, and "accepted to
   ACM MM 2026" (README only). The baseline therefore runs its published recipe on the same twin, VLA,
   learner and budget accounting as the method. Where the TwinRL code does not cover our VLA or simulator,
   it uses open tools:
   - RLinf (Apache-2.0; ships a ManiSkill 3DGS "GSEnv" for Real2Sim2Real);
   - SimpleVLA-RL (MIT).

   RialTo [§6 RialTo] is the non-VLA ancestor of this pipeline.
5. **Feasibility is fine at LoRA scale.**
   - LoRA fine-tuning of the 7B OpenVLA needs ≥ ~27 GB of GPU memory (~72 GB at batch 16, one A100 80 GB;
     openvla README).
   - π0/π0.5 LoRA needs > 22.5 GB (openpi README).
   - RL fine-tuning in simulation is a one- or two-node job: the SimpleVLA-RL example uses 8× A800 80 GB.
     A WCSS Lem node has 4× H100 96 GB, and queues allow up to 7 days (research/resources.md §2).
   - Existing world-model checkpoints are adapted, not trained from scratch.

---

## 1. Queries and counts (Semantic Scholar bulk search, 2026-09-26)

Endpoint: `api.semanticscholar.org/graph/v1/paper/search/bulk?query=<Q>&year=<Y>`, value = `total`.
2026 = 1 Jan – 26 Sep 2026. S2 matches title and abstract. Treat the counts as a trend, not a census.

| # | Area | Query Q (S2 bulk syntax, verbatim) | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| Q1 | RL/IL fine-tuning of VLAs in simulation | `("vision-language-action" \| VLA) + ("reinforcement learning" \| "fine-tuning") + simulation` | 1 | 3 | 40 | 126 |
| Q2 | World models for VLA training/evaluation | `("vision-language-action" \| VLA) + "world model"` | 0 | 2 | 42 | 183 |
| Q3 | Real-to-sim twins for VLA fine-tuning | `("vision-language-action" \| VLA) + ("digital twin" \| "real-to-sim" \| real2sim \| "Gaussian splatting")` | 0 | 2 | 15 | 33 |
| Q4 | VLM-guided data capture/collection (broad) | `("vision-language model" \| VLM) + ("next-best-view" \| "view selection" \| "active reconstruction" \| "data collection") + robot` | 2 | 9 | 22 | 40 |
| Q4b | VLM/task-guided active view selection for reconstruction | `("vision-language" \| VLM \| "language-guided" \| "task-driven" \| "task-aware") + ("next-best-view" \| "active view selection" \| "active reconstruction" \| "view planning") + (radiance \| "Gaussian splatting" \| NeRF \| reconstruction)` | 0 | 0 | 1 | 2 |
| Q5 | Real-data budget of a VLA twin loop | `("vision-language-action" \| VLA) + ("real-to-sim" \| "digital twin") + ("real data" \| "data efficiency" \| "data-efficient")` | 0 | 0 | 1 | 2 |
| Q6 | VLM as reward/success judge for VLAs | `("vision-language model" \| VLM) + (reward \| "success detection" \| "success detector") + ("vision-language-action" \| VLA)` | 0 | 2 | 5 | 12 |
| Q7 | World models grounded in twins/Gaussians | `"world model" + ("digital twin" \| "Gaussian splatting") + (robot \| policy)` | 2 | 6 | 20 | 34 |
| Q8 | Active real-data selection for VLA sim-to-real | `("vision-language-action" \| VLA) + ("sim-to-real" \| "real-to-sim") + ("active learning" \| "uncertainty" \| "failure")` | 0 | 0 | 1 | 10 |

How to read the table:
- Q1 and Q2 are the crowded core, as the v5 guardrail expected.
- Q4 is mostly VLM affordance or planning work (RoboPoint, CoPa, AutoRT), not capture for a twin. The
  capture-specific Q4b is nearly empty.
- Q5 hits: ReBot (IROS 2025), and two 2026 VLA papers that only mention real-to-sim. None has a budget
  curve.
- Q8 hits are about failure prediction (Tri-Info, SAFECAST) or evaluation correlation (REALM; "A Practical
  Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation", arXiv:2606.10366). The exception
  is TwinRL. None selects real data under a budget to correct a twin.

## 2. Verified works by area (S2 batch + arXiv abstract page, 2026-09-26)

Venue source: S2 `venue` field, the arXiv comment, or a DOI. "arXiv" means no refereed venue was
confirmed.

### 2.1 Open VLAs and parameter-efficient fine-tuning (the policy of C2)

| Work | ID | Venue | Fact used (abstract/README) | Weights / licence |
|---|---|---|---|---|
| OpenVLA (Kim, Pertsch, Karamcheti, ...) | 2406.09246 | CoRL 2024 (S2) | 7B VLA trained on 970k real demonstrations. Llama 2 backbone with fused DINOv2 + SigLIP. "fine-tuned on consumer GPUs via modern low-rank adaptation methods" | HF `openvla/openvla-7b`, MIT tag. README: models "derived from Llama-2" and "subject to the Llama Community License". LoRA ≥ ~27 GB; batch 16 ≈ 72 GB on one A100 80 GB |
| OpenVLA-OFT (Kim, Finn, Liang) | 2502.19645 | RSS 2025 (arXiv comment) | OFT recipe; LIBERO 76.5% → 97.1%; 26× faster action generation | GitHub `moojink/openvla-oft`, MIT |
| π0 (Black, Brown, Driess, ...) | 2410.24164 | arXiv | flow-matching VLA on a pretrained VLM | `openpi` (Apache-2.0): π0, π0-FAST and π0.5 base checkpoints. LoRA > 22.5 GB, full fine-tuning > 70 GB |
| π0.5 | 2504.16054 | arXiv | co-training for open-world generalization | same repository |
| Octo | 2405.12213 | RSS 2024 (S2) | 800k OXE trajectories, fine-tunes to new domains | HF `rail-berkeley/octo-base-1.5`, MIT |
| SmolVLA | 2506.01844 | arXiv | "designed to be trained on a single GPU" | HF `lerobot/smolvla_base`, Apache-2.0 |
| GR00T N1 | 2503.14734 | arXiv | open humanoid VLA | not needed |
| NaVILA (Cheng, Ji, Yang, ...) | 2412.04453 | arXiv (S2 venue "Robotics", not confirmed) | navigation VLA; outputs mid-level language actions ("moving forward 75cm") executed by a locomotion policy | code `AnjieCheng/NaVILA`, Apache-2.0. HF `a8cheng/navila-llama3-8b-8f` has **no licence tag** (risk) |
| Uni-NaVid / NaVid | 2412.06224 / 2402.15852 | arXiv / RSS 2024 (S2) | video-based navigation VLA/VLM | alternatives to NaVILA |
| LoRA (Hu et al.) | 2106.09685 | ICLR 2022 (S2) | low-rank adapters, frozen base weights | — |

### 2.2 RL/IL fine-tuning of VLAs in simulation (crowded; Q1)

| Work | ID | Venue | What it shows |
|---|---|---|---|
| What Can RL Bring to VLA Generalization? (J. Liu et al.) | 2505.19789 | NeurIPS 2025 (arXiv comment) | PPO fine-tuning improves semantic and execution generalization over SFT; "simple recipe for efficient PPO training on VLAs" |
| SimpleVLA-RL (H. Li et al.) | 2509.09674 | arXiv | RL on OpenVLA-OFT; state of the art on LIBERO and RoboTwin; "surpasses SFT in real-world tasks". Example set-up: 8× A800 80 GB (README) |
| VLA-RL (G. Lu et al.) | 2505.18719 | arXiv | online RL for autoregressive VLAs; a fine-tuned VLM as a dense process-reward model |
| RIPT-VLA (Tan et al.) | 2505.17016 | arXiv | interactive post-training with sparse binary rewards; OpenVLA-OFT to 97.5% |
| RLinf-VLA (Zang et al.) | 2510.06710 | RSS 2026 (RLinf README; not otherwise confirmed) | unified RL framework for VLAs over simulators; supports OpenVLA/OFT, π0; GSEnv (3DGS ManiSkill) for Real2Sim2Real |
| πRL (K. Chen et al.) | 2510.25889 | arXiv | online RL for flow-based VLAs (π0, π0.5) |

### 2.3 World models for VLA training and evaluation (crowded; Q2)

| Work | ID | Venue | What it shows |
|---|---|---|---|
| WMPO (F. Zhu et al.) | 2511.09515 | arXiv | on-policy VLA RL (GRPO) inside a pixel-space world model "without interacting with the real environment" |
| VLA-RFT (H. Li et al.) | 2510.00406 | arXiv | a world model trained from real interaction data as a controllable simulator with verified rewards |
| World-Env | 2509.24948 | arXiv | a world model as a virtual environment for VLA post-training; VLM reward |
| WoVR | 2602.13977 | arXiv | makes world-model RL reliable against hallucination and long-horizon error |
| **VLAW** (Guo, Lee, Shi, Chen, ...) | 2602.12063 | arXiv | **iteratively uses real-world rollouts to improve the world model's fidelity**, then generates synthetic data for the VLA; +39.2% absolute SR. Closest to C3's world-model correction. Its rollouts are not actively selected, and there is no twin |
| Ctrl-World (Guo, Shi, Chen, Finn) | 2510.10125 | arXiv | controllable multi-view world model; policy evaluation and improvement in imagination |
| WorldGym | 2506.00613 | arXiv | world model as a policy-evaluation environment for VLAs, with a VLM providing rewards |
| World-VLA-Loop; World-Gymnast; RAW-Dream | 2602.06508; 2602.02454; 2605.12334 | arXiv | 2026 variants (co-training, RL in a world model, task-agnostic world and reward models) |
| Cosmos (Agarwal et al.) | 2501.03575 | arXiv | open world foundation models "fine-tuned into customized world models". Cosmos-Predict2 checkpoints: NVIDIA Open Model License (HF card) |
| Cosmos Policy (Kim et al.) | 2601.16163 | arXiv | Cosmos-Predict2 post-trained into a policy |
| NWM (Bar et al.) | 2412.03572 | CVPR 2025 (DOI) | navigation world model, 1B-parameter CDiT; HF `facebook/nwm`, CC-BY-4.0, gated |
| **GigaWorld-0** | 2511.19861 | arXiv | world-model data engine for VLAs: video generation **plus 3DGS reconstruction and differentiable system identification**; "without any real-world interaction during training". Closest to C2's twin + world model. The real-data budget is not a variable |
| GWM (G. Lu et al.) | 2508.17600 | ICCV 2025 (DOI) | Gaussian world model: predicts future Gaussian primitives under actions |
| PEGS (Abou-Chakra et al.) | 2406.10788 | arXiv | Gaussian–particle world model, corrected online from observations |

### 2.4 Real-to-sim twins for VLA fine-tuning (Q3) and the H4(b) baseline

| Work | ID | Venue | What it shows |
|---|---|---|---|
| **TwinRL** (Q. Xu, J. Liu, R. Zhou, S. Shi, ...) | 2602.09023 | arXiv; ACM MM 2026 per the GitHub README (not otherwise confirmed); code `zhourui9813/TwinRL`, MIT (offline training code; Octo/SERL-based) | smartphone-captured twin; "SFT warm-up, twin RL warm-up, and real-world RL"; the twin "identifies failure-prone yet informative configurations, enabling targeted human-in-the-loop rollouts"; "only 20 minutes of on-robot interaction", four tasks |
| ReBot | 2503.14526 | IROS 2025 (DOI) | replays real robot trajectories in simulation to adapt VLAs to target domains |
| Real2Render2Real | 2505.09601 | arXiv | phone scan + one human video → rendered robot demonstrations; no dynamics simulation |
| LEGS | 2606.01458 | arXiv | VLA fine-tuning in a mesh-over-3DGS hybrid simulator for humanoid loco-manipulation |
| RobotArena ∞; REALM | 2510.23571; 2512.19562 | arXiv; RA-L 2026 (DOI) | real-to-sim evaluation of VLAs |
| SIMPLER (X. Li et al.) | 2405.05941 | CoRL 2024 (S2) | "paired sim-and-real evaluations of manipulation policies", strong correlation; open-source environments (SimplerEnv, MIT) |

**Recommended H4(b) baseline: "TwinRL-style".** The steps below re-implement TwinRL's published recipe on
the same twin and VLA:
1. uniform capture at the same budget;
2. the same 3DGS twin + system identification;
3. uniform domain randomization;
4. LoRA SFT warm-up and then RL fine-tuning of the same VLA in the twin;
5. real trials chosen at random **or** by the twin's failure-prone configurations (TwinRL's rule), with
   the better of the two reported;
6. the same correction and fine-tuning with those trials.

RialTo is the non-VLA ancestor. Why this is the strongest fair baseline:
- it is the only published VLA pipeline that uses a phone-captured twin *and* spends real data
  selectively;
- it is recent (Feb 2026);
- it uses the same ingredients as the method except the three allocation rules (C1–C3) and the world
  model.

Risk: TwinRL's public code covers offline training only, and its README ties it to Octo, so parts must be
re-implemented for our VLA and testbeds, and a re-implementation can be called weak. Mitigations:
pre-register the recipe, use the released code wherever it applies, and report the baseline's tuned
hyperparameters.

### 2.5 VLM-guided capture and VLM judges (C1; C2 reward)

| Work | ID | Venue | Relevance |
|---|---|---|---|
| **AREA3D** | 2512.05131 | arXiv | active reconstruction with feed-forward 3D perception + "vision-language guidance" for "informative and diverse viewpoints". Closest to C1; its objective is reconstruction quality, not policy success |
| FisherRF; Bayes' Rays; risk-aware FisherRF; ASID | (§6, verified in earlier waves) | ECCV 2024; CVPR 2024; arXiv; arXiv | task-blind or risk-weighted uncertainty baselines, unchanged |
| VLMs as Success Detectors (Du et al.) | 2303.07280 | CoLLAs 2023 (S2) | SuccessVQA: success detection as VQA with a pretrained VLM |
| GVL (Ma et al.) | 2411.04549 | ICLR 2025 (S2) | VLMs as in-context value (progress) estimators |
| VLAC | 2509.15937 | arXiv | VLA-critic process reward for real-world RL |
| Qwen2.5-VL | 2502.13923 | arXiv | open VLM; HF `Qwen/Qwen2.5-VL-7B-Instruct`, Apache-2.0 |

## 3. What is new, and what is not (for §6 and §8)

**Not new (cite, use as components or baselines, never claim):**
- LoRA/PEFT fine-tuning of open VLAs;
- RL fine-tuning of VLAs in simulation (SimpleVLA-RL, RL4VLA, RLinf, VLA-RL);
- RL of VLAs inside world models (WMPO, VLA-RFT, World-Env, WoVR);
- VLM success or reward judges (SuccessVQA, GVL, VLAC, WorldGym's VLM reward);
- phone-captured twins for VLA RL (TwinRL);
- world models built with 3DGS and system identification as data engines (GigaWorld-0);
- correcting a world model with real rollouts (VLAW).

**Still open, and the v5 novelty** (no paper found in Q1–Q8 or among the top-cited hits):
1. **Real-data budget as the controlled variable of a VLA twin loop.** Budget curves of capture + real
   trials against real success, versus real-only fine-tuning of the same VLA and versus a TwinRL-style
   pipeline.
2. **Task-aware capture from the instruction.** A VLM names the task-relevant objects and regions, and
   capture goes where those regions are most uncertain in the twin. AREA3D uses VLM guidance for
   reconstruction quality only.
3. **A world model used where the twin is uncertain.** It is conditioned on or adapted to twin rollouts
   and weighted by the twin's uncertainty. GigaWorld-0 and GWM combine Gaussians and generation but do not
   target the twin's error.
4. **Active selection of a few real trials across twin, world model and VLA uncertainty.** The selected
   trials correct all three. TwinRL uses failure-prone configurations for the policy only; VLAW corrects
   the world model with unselected rollouts.

**Scooping risk: high.** TwinRL (Feb 2026) and VLAW (Feb 2026) are each one step away from parts of the
method. Well-funded groups publish monthly. Mitigations:
- monthly S2 alerts on Q3, Q5 and Q8;
- a P1 preprint at submission;
- keep the claim on the *budget measurement and allocation*, not on any single component.

## 4. Compute estimate (for §9; our estimate, not measured)

Facts:
- OpenVLA LoRA ≥ ~27 GB (≈ 72 GB at batch 16, one A100 80 GB).
- π0 LoRA > 22.5 GB.
- SimpleVLA-RL example: one node of 8× A800 80 GB.
- WCSS Lem: 76 nodes × 4 H100 96 GB; queues of 3 days (short) and 7 days (normal).
- PLGrid Athena A100 and Helios GH200 are available through a PLGrid grant.

Estimate (assumptions stated; to be replaced by the T3.1 pilot measurement):

| Item | Runs (both testbeds) | Per run (assumed) | H100-hours |
|---|---|---|---|
| Stage I: LoRA SFT of the VLA per capture budget (4 budgets × 4 selection rules × 3 seeds × 2 testbeds) | 96 | 1 GPU × ~8 h | ~0.8k |
| Stage II: RL/IL fine-tuning in twin (± world model): 4 arms × 2 budgets × 3 seeds × 2 testbeds | 48 | 8 GPUs × ~24 h | ~9.2k |
| World-model adaptation to twin rollouts (Cosmos-Predict2 2B / NWM), ~4 adaptations per testbed | 8 | 8 GPUs × ~48 h | ~3.1k |
| Stage III–IV: trial selection, correction, budget curves (method, TwinRL-style, real-only) | ~60 | 8 GPUs × ~16 h | ~7.7k |
| Rendering, VLM judging, evaluation (10% overhead) | — | — | ~2k |
| **Total, sem. 3–7** | | | **~23k H100-hours** |

That is about 5 H100s busy on average over 24 months. It fits a WCSS computing grant plus PLGrid, but it
is large enough that the grant must be applied for in sem. 3 (T3.1). Ways to cut cost:
- SmolVLA for development and ablations;
- LoRA SFT before RL;
- the world model only in the arms that need it.

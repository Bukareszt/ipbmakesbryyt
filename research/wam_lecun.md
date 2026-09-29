# World Action Models (WAMs) and LeCun's JEPA line: notes for the thesis

Thesis: "Representation learning methods for simulation-to-reality generalization of deep learning models in physical AI".
Compiled 2026-09-28. Every arXiv ID below was checked against the arXiv API or the arXiv abstract page
(authors, date, title). Venues were checked against proceedings or conference pages. Where no venue was found,
the paper is cited as arXiv only.

## TL;DR

- **The term "WAM" = World Action Model is real and now standard.** It was popularized by NVIDIA's DreamZero,
  *World Action Models are Zero-shot Policies* (Feb 2026). By mid-2026 there are at least four surveys or tutorials
  and dozens of "X-WAM" papers. A WAM is one model that predicts **future world states and actions jointly**
  (or makes a forecast of the future available to the action head). A **VLA** maps observation plus language
  straight to actions and has no explicit model of how the world evolves. A **pure video world model**
  predicts future frames given actions but does not output actions (it is a simulator or evaluator, not a policy).
- The earlier "unified" papers of 2025 are the direct ancestors: UWM (RSS 2025), UVA (RSS 2025),
  WorldVLA, DreamVLA (NeurIPS 2025) and Genie Envisioner. Ctrl-World (ICLR 2026) is an action-conditioned
  *world model* used to evaluate and improve VLAs. It is not itself a WAM.
- **Sim-to-real of WAMs is almost untouched.** The first claimed zero-shot sim-to-real WAM (Wang et al., 2026,
  a CVPR 2026 workshop paper) reaches 35% success on a Franka.
- **LeCun's line** runs from the 2022 position paper (JEPA: predict in representation space, not pixels) to
  I-JEPA (CVPR 2023), V-JEPA (TMLR 2024), DINO-WM (ICML 2025), V-JEPA 2 / V-JEPA 2-AC (arXiv 2025,
  zero-shot robot planning), and in 2026 LeWorldModel, AdaJEPA and SkyJEPA (zero-shot sim-to-real quadrotor
  control). LeCun left Meta (announced 19 Nov 2025) and founded **AMI Labs** (Paris). It launched on 10 Mar 2026
  with a US$1.03B round to build world models.
- **Why JEPA fits this thesis:** a JEPA world model learns an embedding space in which unpredictable,
  task-irrelevant detail (textures, lighting, rendering artifacts) is meant to be discarded, and dynamics are
  predicted in that space. That is exactly where a sim-to-real gap can be **measured** (embedding distributions,
  latent prediction error or "surprise" on real data) and **reduced** (a regularized or adapted encoder). It
  makes a representation-learning thesis a thesis about world models without needing to generate pixels.

---

## 1. World Action Models (WAMs)

### 1.1 Is "WAM" used this way? Yes.

- **Definition 1 (Wang et al., 2026, survey):** WAMs are "embodied foundation models that unify predictive state
  modeling with action generation, targeting a joint distribution over future states and actions rather than
  actions alone." The survey splits them into **Cascaded** WAMs (first predict the future, then decode an action)
  and **Joint** WAMs (one model generates both).
- **Definition 2 (Shen et al., 2026, survey):** WAMs are "embodied predictive-action models that make a forecast
  of the future available to action." They say a WAM is *not* "simply a video generator with an action head", and
  that the field is "moving toward methods that generate less of the future while preserving what control requires."
  That trend (rendered futures, then latent futures) is where JEPA meets WAMs (see §3).
- **Origin of the term.** The phrase "world-action model" appears earlier in JOWA (ICLR 2025, offline RL on
  Atari) and DyWA (2025). It became the name of a robot-learning paradigm with DreamZero (NVIDIA, Feb 2026):
  "Unlike VLAs, WAMs learn physical dynamics by predicting future world states and actions, using video as a
  dense representation of how the world evolves."
- **Advice for the IPB:** define WAM explicitly on first use and cite one survey. Use the Wang et al. (2026)
  definition (a joint distribution over future states and actions), because some authors use the term loosely.

### 1.2 WAM vs VLA vs pure video world model

| | Input | Output | What it learns | Examples |
|---|---|---|---|---|
| **VLA** | image(s) + language (+ proprioception) | actions | a reactive observation-to-action mapping, usually on a VLM backbone. No explicit model of future states | π0, OpenVLA (not reviewed here) |
| **Pure (action-conditioned) video world model** | image(s) + actions (+ text) | future frames or latents | dynamics p(o_{t+1:T} \| o_t, a_t). Used as a simulator, for policy evaluation, or for planning with a separate optimizer | Ctrl-World, GE-Sim, Navigation World Models, V-JEPA 2-AC (latent) |
| **WAM** | image(s) + language | future states (pixels, latents or other features) **and** actions | the joint p(future, action \| obs, instr). The future prediction is a training signal and/or conditions the action | DreamZero, UWM, UVA, WorldVLA, GE-Act, DreamVLA (a borderline "VLA with foresight") |

In short: a VLA acts without imagining, a world model imagines without acting, and a WAM does both in one network.

### 1.3 Verified WAM and "unified" papers (chronological)

1. Cheng, J., et al. (2024). Scaling Offline Model-Based RL via Jointly-Optimized World-Action Model Pretraining. ICLR 2025 / arXiv:2410.00564.
   *JOWA: an early use of the term, in offline RL on Atari (not robotics).*
2. Li, S., Gao, Y., Sadigh, D., Song, S. (2025). Unified Video Action Model. RSS 2025 / arXiv:2503.00200.
   *UVA: a joint video-action latent with decoupled decoding. Video decoding can be skipped at inference. One model
   serves as policy, video model, forward dynamics or inverse dynamics.*
3. Lyu, J., et al. (2025). DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation. arXiv:2503.16806.
   *Trained in simulation. Uses the term "world action model" before DreamZero.*
4. Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. RSS 2025 / arXiv:2504.02792.
   *UWM: one transformer with independent diffusion timesteps for video and action. By setting those timesteps
   it acts as a policy, forward dynamics, inverse dynamics or video generator. It can also learn from action-free video.*
5. Cen, J., et al. (2025). WorldVLA: Towards Autoregressive Action World Model. arXiv:2506.21539.
   *Alibaba DAMO. One autoregressive model that generates both images and actions (a VLA and a world model in one
   framework). No venue found.*
6. Zhang, W., et al. (2025). DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge. NeurIPS 2025 / arXiv:2507.04447.
   *Predicts compact "world knowledge" (dynamic regions, depth, semantic features) rather than full frames, then
   acts through inverse dynamics. An early "latent-future" WAM.*
7. Liao, Y., et al. (2025). Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation. arXiv:2508.05635.
   *AgiBot. GE-Base (a video diffusion world model), GE-Act (latent to actions), GE-Sim (an action-conditioned neural
   simulator) and the EWMBench benchmark.*
8. Guo, Y., Shi, L. X., Chen, J., Finn, C. (2025). Ctrl-World: A Controllable Generative World Model for Robot Manipulation. ICLR 2026 / arXiv:2510.10125.
   *An action-conditioned multi-view world model trained on DROID. It runs a policy in the loop "in imagination" to
   evaluate and improve VLAs. It is a world model used with a VLA, not a WAM.*
9. Kim, M. J., et al. (2026). Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning. arXiv:2601.16163.
   *NVIDIA. Cosmos-Predict2 fine-tuned to emit actions as latent frames inside the video diffusion process.*
10. Ye, S., et al. (2026). World Action Models are Zero-shot Policies. arXiv:2602.15922.
    *DreamZero (NVIDIA). A 14B autoregressive video-diffusion WAM running at 7 Hz closed loop. Reports more than 2x
    better generalization to new tasks and environments than state-of-the-art VLAs. This is the paper that set the term.*
11. Wang, S., et al. (2026). World Action Models: The Next Frontier in Embodied AI. arXiv:2605.12090.
    *Survey with the formal definition and the Cascaded vs Joint taxonomy.*
12. Shen, Q., et al. (2026). World Action Models: A Survey. arXiv:2606.20781.
    *Survey. Organizes WAMs by what they generate: rendered futures, latent futures, or no video generation at all.*
13. Wang, Z., et al. (2026). Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors. CVPR 2026 Embodied AI Workshop / arXiv:2606.31101.
    *Claims the first sim-to-real WAM. Cosmos Policy trained on about 800 domain-randomized synthetic demos per task;
    35% average zero-shot success on a Franka. **The closest WAM paper to this thesis.** It shows the area is open
    and the numbers are low.*
14. Xia, T., et al. (2026). ReWorld: Representation Learning for World Action Models. arXiv:2606.27504.
    *Driving. Explicitly optimizes the intermediate world-to-action representation. Evidence that "representation
    learning for WAMs" is an emerging subtopic.*
15. Lu, Z., et al. (2026). World-Action Models for Robot Learning and Control: A Survey. arXiv:2609.16074. *(Third survey, Sep 2026.)*

Latent / JEPA-flavoured WAMs, which bridge to §2: Sun, J., et al. (2026). VLA-JEPA: Enhancing Vision-Language-Action
Model with Latent World Model. arXiv:2602.10098. Also LaWAM (arXiv:2606.15768) and "Foresight Without Seeing"
(arXiv:2608.11605). All three predict the future in latent space instead of pixels.

**Crowdedness note:** a title search on arXiv for "world action model(s)" returns more than 50 papers from 2026 alone
(tactile, driving, navigation, humanoid, distillation, safety, efficiency variants). Proposing a *new WAM
architecture* would be a crowded contribution for a single PhD. Using WAMs as the **object of study** (their
representations under sim-to-real shift) is not crowded.

---

## 2. LeCun: world models and representation learning

### 2.1 Verified citations

1. LeCun, Y. (2022). A Path Towards Autonomous Machine Intelligence (version 0.9.2, 2022-06-27). OpenReview, https://openreview.net/pdf?id=BZ5a1r-kVsf.
   *Position paper: a modular agent (perception, world model, cost, actor, short-term memory, configurator). The
   world model is a hierarchical **JEPA**: encode x and y, then predict s_y from s_x (plus a latent z) in
   representation space. It is trained with non-contrastive, energy-based objectives that avoid collapse. Main
   argument: generative pixel prediction wastes capacity on unpredictable detail, while prediction in an abstract
   space can drop it.*
2. Assran, M., et al. (2023). Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture. CVPR 2023, pp. 15619–15629 / arXiv:2301.08243.
   *I-JEPA: predict the representations of masked target blocks from a context block. No hand-crafted augmentations
   and no pixel reconstruction. Note: the arXiv comment field says "ICCV". The paper is in fact in the CVPR 2023
   proceedings (CVF open access), so cite CVPR 2023.*
3. Bardes, A., et al. (2024). Revisiting Feature Prediction for Learning Visual Representations from Video. TMLR 2024 / arXiv:2404.08471.
   *V-JEPA: video feature prediction as the only objective, trained on 2M videos. Frozen-backbone evaluation.*
4. Zhou, G., Pan, H., LeCun, Y., Pinto, L. (2024). DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning. ICML 2025 (PMLR 267:79115–79135) / arXiv:2411.04983.
   *An action-conditioned predictor over **frozen DINOv2 patch features**, trained on offline trajectories. Plans by
   MPC toward a goal image's features. No pixel reconstruction and no reward.*
5. Bar, A., Zhou, G., Tran, D., Darrell, T., LeCun, Y. (2024). Navigation World Models. CVPR 2025 / arXiv:2412.03572.
   *A conditional diffusion transformer world model for navigation, planning by simulating trajectories. Included for
   contrast: it is generative (it predicts frames in a VAE latent), unlike a JEPA.*
6. Sobal, V., et al. (2025). Learning from Reward-Free Offline Data: A Case for Planning with Latent Dynamics Models. arXiv:2502.14819.
   *PLDM, last author LeCun. A JEPA latent dynamics model plus planning generalizes better to new layouts than
   offline goal-conditioned RL.*
7. Assran, M., et al. (2025). V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning. arXiv:2506.09985.
   *Action-free pre-training on more than 1M hours of video. Then **V-JEPA 2-AC**: an action-conditioned latent
   predictor post-trained on under 62 h of unlabeled DROID robot video. It was deployed **zero-shot on Franka arms in
   two labs** for pick-and-place with image goals, planning in latent space, with no data from those environments and
   no reward. No peer-reviewed venue found as of Sep 2026, so cite arXiv.*
8. Balestriero, R., LeCun, Y. (2025). LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics. arXiv:2511.08544.
   *Theory-driven JEPA with the SIGReg regularizer (isotropic Gaussian embeddings). No EMA or stop-gradient tricks.*
9. Chen, D., et al. (2025). VL-JEPA: Joint Embedding Predictive Architecture for Vision-language. arXiv:2512.10942. *(LeCun is a co-author.)*
10. Maes, L., Le Lidec, Q., Scieur, D., LeCun, Y., Balestriero, R. (2026). LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels. arXiv:2603.19312.
    *LeWM: an end-to-end JEPA world model from pixels with two losses (next-embedding prediction plus SIGReg). About
    15M parameters, trains on **one GPU in hours**, and plans up to 48x faster than foundation-model world models.
    Its latents can be probed for physical quantities. **The most practical base model for a single-GPU PhD.***
11. Mur-Labadia, L., et al. (2026). V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning. arXiv:2603.14482. *(Meta, after LeCun's departure. Dense features.)*
12. Wang, Y., Bounou, O., LeCun, Y., Ren, M. (2026). AdaJEPA: An Adaptive Latent World Model. arXiv:2606.32026.
    *Test-time adaptation inside the MPC loop: the observed next-state error is the self-supervised signal; one
    gradient step per control cycle; handles test-time distribution shift. **A direct baseline for adaptation to
    real data.***
13. Rao, P., Zhang, W., Balestriero, R., LeCun, Y., Loianno, G. (2026). SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors. arXiv:2606.23444 (under review).
    *A JEPA latent dynamics model plus a physics-inspired probe from frozen latents to state, with sampling-based MPC
    on embedded hardware. Trained on automatically generated (simulated) data, with **zero-shot sim-to-real** in
    outdoor closed loop. **The closest LeCun-group paper to this thesis.** It shows JEPA world models transfer
    sim-to-real. It does not measure the gap in latent space.*

Related 2026 JEPA work useful as neighbours or baselines (verified on arXiv, LeCun not an author):
Cui, J., et al. (2026). A Generalization Theory for JEPA-Based World Models. arXiv:2606.27014 (a bound linking JEPA
pre-training error to planning regret, which could be extended to domain shift). Khan, U. M. (2026).
Depth-Regularized JEPA World Models Learn More Transferable Representations from Real Outdoor Robot Data.
arXiv:2607.16314 (reports latent "surprise" separation and rollout fidelity under domain shift). Zeng, X., et al.
(2026). PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models. arXiv:2608.05720. Ivashkov, P.,
Balestriero, R., Schölkopf, B. (2026). Sensorimotor World Models: Perception for Action via Inverse Dynamics.
arXiv:2606.20104. Nilaksh, et al. (2026). Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic
World Models. arXiv:2605.06388. Yao, X., Chang, L., Chen, H. (2026). World Translation: Minimizing Sim-to-Real Gap
with Backward Dynamics Extraction and Unpaired Domain Translation. arXiv:2607.18154.

### 2.2 LeCun in 2025–2026 (non-paper, from reliable press)

- **19 Nov 2025:** LeCun told Meta staff he would leave at the end of 2025 to found a world-model start-up; Meta
  would partner with it. Sources: Bloomberg (2025-11-19), CNBC (2025-11-19).
- **10 Mar 2026:** **AMI Labs** (Advanced Machine Intelligence Labs, Paris; CEO Alex LeBrun) launched with a
  **US$1.03B** round. Co-leads: Cathay Innovation, Greycroft, Hiro Capital, HV Capital and Bezos Expeditions.
  Post-money valuation about US$4.5B. Stated focus: world models for robotics, healthcare, wearables and industrial
  automation. Sources: TechCrunch (2026-03-09), HPCwire/AIwire (2026-03-11), Wikipedia "Advanced Machine Intelligence Labs".
- His long-standing public position (in the 2022 paper and many talks): LLMs and pixel-generative models are not
  the path to machine intelligence that understands the physical world; the alternative is **JEPA world models
  plus planning (MPC)**. For the IPB, cite the 2022 paper and V-JEPA 2 rather than talks or tweets.

### 2.3 The JEPA idea in one paragraph

A generative world model predicts the next *observation* (pixels, or VAE latents trained to reconstruct pixels).
Its loss therefore charges it for every texture, reflection and noise pattern, most of which cannot be predicted
and do not matter for control. A JEPA encodes both the current and the future observation and predicts the
**future embedding** from the current embedding (plus the action, for a world model). Because the target is also
learned, the encoder is free to **discard what is unpredictable**. A collapse-preventing term (VICReg, EMA
teacher, or SIGReg in LeJEPA and LeWM) keeps the embedding informative. Planning then optimizes actions so that
the predicted embedding approaches a goal embedding (DINO-WM, V-JEPA 2-AC, LeWM, SkyJEPA).

---

## 3. Why the JEPA view fits a thesis on representation learning for sim-to-real generalization

1. **The sim-to-real gap is largely nuisance variation.** Rendering, texture, lighting and sensor noise are
   exactly what a JEPA encoder is pushed to ignore. If the representation is right, simulated and real
   observations of the same state should map close together. Whether they actually do is an open, measurable
   question, and it is a question about representations, which is the thesis's discipline.
2. **Dynamics gaps show up as latent prediction error.** An action-conditioned JEPA predictor trained in
   simulation, rolled forward on real transitions, gives a per-transition "surprise" signal in latent space. This
   separates the **observation gap** (encoder: do embeddings shift?) from the **dynamics gap** (predictor: does
   ẑ_{t+1} miss the real z_{t+1}?), with no pixel generation needed. Depth-regularized JEPA (Khan, 2026) already uses
   surprise separation under domain shift, and AdaJEPA uses next-state error as an adaptation signal.
3. **It is feasible on one GPU and has a clear lineage.** DINO-WM and V-JEPA 2 give frozen, pretrained encoders;
   LeWM trains end-to-end in hours. The thesis can therefore work with world models without training a 14B
   video-diffusion WAM.
4. **It sits on the side of the WAM field that is growing.** Shen et al. (2026) observe WAMs moving toward "latent
   futures". JEPA-style latents are the principled version of that trend. The first sim-to-real WAM result (35%)
   shows plenty of room to improve.
5. **Novelty gap.** SkyJEPA shows JEPA world models *can* transfer sim-to-real, and AdaJEPA adapts under shift.
   Among the verified papers, none **measures or minimizes the sim-to-real gap in the world model's latent space**
   and relates that gap to downstream policy transfer. (This is from a targeted search, not a systematic review.
   Re-check before submission.)

## 4. Suggested thesis hook (2–3 sentences)

The thesis can use a JEPA-style, action-conditioned world model (frozen V-JEPA 2 or DINOv2 features, or a small
LeWM trained on twin data) as a common latent space in which the simulation-to-reality gap is **measured**. It
would be split into an observation term (the distance between sim and real embedding distributions of matched
states) and a dynamics term (the latent prediction error, or "surprise", of a sim-trained predictor on real
transitions), and tested for whether these latent gaps predict real-world policy success better than pixel-level
or rollout-based metrics. The same quantities then become training objectives: regularizing or adapting the
encoder and predictor (with LeJEPA/SIGReg, AdaJEPA-style test-time updates as baselines) to shrink the latent gap.
The hypothesis is that shrinking it improves sim-to-real transfer of both latent-planning agents and WAM-style
policies.

---

## Sources (non-arXiv)

- CVPR 2023 I-JEPA: https://openaccess.thecvf.com/content/CVPR2023/html/Assran_Self-Supervised_Learning_From_Images_With_a_Joint-Embedding_Predictive_Architecture_CVPR_2023_paper.html
- V-JEPA TMLR: https://dblp.org/rec/journals/tmlr/BardesGPCRLAB24.html
- DINO-WM ICML 2025: https://proceedings.mlr.press/v267/zhou25t.html
- LeCun 2022 position paper: https://openreview.net/pdf?id=BZ5a1r-kVsf
- UWM RSS 2025: https://roboticsconference.org/program/papers/15/
- UVA RSS 2025: https://github.com/ShuangLI59/unified_video_action (README states RSS 2025)
- DreamVLA NeurIPS 2025: https://neurips.cc/virtual/2025/poster/118226
- Ctrl-World ICLR 2026: https://iclr.cc/virtual/2026/10018003
- LeCun leaving Meta: https://www.cnbc.com/2025/11/19/meta-chief-ai-scientist-yann-lecun-is-leaving-the-company-.html ; https://www.bloomberg.com/news/articles/2025-11-19/meta-ai-s-lecun-to-announce-exit-startup-as-soon-as-this-week
- AMI Labs funding: https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/ ; https://www.hpcwire.com/aiwire/2026/03/11/yann-lecuns-ami-secures-1b-seed-to-develop-ai-world-models/ ; https://en.wikipedia.org/wiki/Advanced_Machine_Intelligence_Labs
- WAM survey homepage: https://world-action-models.github.io/

# Stage 3: Twin-to-Real Transfer with Little Real Data (Correcting Both the Twin and the Model)

Scope: 2019–2026 for background, focused on 2023–2026, as of 26 Sep 2026. Metadata was checked against the arXiv API (export.arxiv.org) on 2026-09-26. Numbers come from arXiv abstracts or full-text HTML. Where a number came only from a secondary summary, that is stated.

Status of earlier repo leads (research/vla-wm-crowdedness.md, research/niches-eval.md), re-checked here:
- TwinRL (2602.09023): the ID, title, authors and "20 minutes" claim are confirmed. arXiv is now at v4, dated 19 May 2026. The ACM MM 2026 venue is still unconfirmed.
- VLAW (2602.12063): confirmed. Authors: Guo, Lee, Shi, Chen, Liang, Finn.
- SureSim (2510.04354), X4Val (2606.05159), PERRY (2507.20068), SCAPE (2608.19425) and Betting (2604.24018, RSS 2026 per the arXiv comment): all confirmed.
- SIMPLER (2405.05941): confirmed.
- Kadian (1912.06321, RA-L 2020): confirmed. The arXiv v2 title is "Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?"
- Correction to the brief: SPI-Active is arXiv:2505.14266, a legged-robot system-identification paper by Sobanbabu, He, He, Yang and Shi. It does not do navigation or policy fine-tuning.

## Q1. Methods that use real rollouts to correct simulators or twins and to fine-tune policies, and how much real data they use

### Takeaway
Correcting a simulator or twin from real rollouts is well established. SimOpt uses a handful of rollouts per iteration, ASID a single episode, AdaptSim and LoopSR tens of minutes to about 2 hours. The 2026 VLA wave (TwinRL, VLAW) does both twin/world-model correction and policy fine-tuning with 20 minutes to a few hundred real rollouts. Almost all of this work is manipulation or locomotion. The navigation analogues (BDA, EmbodiedSplat) correct dynamics or fine-tune in a reconstructed twin, but none selects which real trials to run.

### Cited Findings
**Correcting the simulator or twin (real-to-sim calibration and system identification)**
- **SimOpt.** Chebotar, Handa, Makoviychuk, Macklin, Issac, Ratliff, Fox, "Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience", arXiv:1810.05687 (ICRA 2019; the venue is the standard citation and was not re-checked on IEEE here).
  - Method: it adapts the distribution of simulation parameters "using a few real world roll-outs interleaved with policy training".
  - Real data, swing-peg-in-hole: "at each iteration, we perform 100 iterations of RL in approximately 7 minutes and 3 roll-outs on the real robot". The task succeeded "after two SimOpt iterations" (about 6 real rollouts).
  - Real data, drawer opening: it worked after one SimOpt iteration.
  - Source: [arXiv PDF](https://arxiv.org/pdf/1810.05687)
- **ASID** (Memmel, Wagenmaker, Zhu, Yin, Fox, Gupta), arXiv:2404.12308. It designs exploration in the (inaccurate) simulator and then plays it in the real world "for a single episode" to identify parameters.
  - Sphere striking: 28.0±9.7% success versus 10.62±4.3% with random exploration.
  - Rod balancing: 0.00° tilt versus 12.44±19.6° with random exploration.
  - Venue is commonly given as ICLR 2024; not verified here.
  - Source: [arXiv HTML](https://arxiv.org/html/2404.12308v2)
- **SPI-Active** (Sobanbabu, G. He, T. He, Yang, Shi), arXiv:2505.14266, 2025, legged robots. It uses sampling-based parameter identification plus an "active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories". It beats baselines "by 42-63% in various locomotion tasks". — [arXiv](https://arxiv.org/abs/2505.14266)
- **AdaptSim** (Ren, Dai, Burchfiel, Majumdar), arXiv:2302.04903, CoRL 2023. It meta-learns a task-driven adaptation policy that updates simulation parameters from real task performance. It reports "1-3x asymptotic performance and ∼2x real data efficiency" versus system-identification baselines and training directly in the target environment. — [arXiv](https://arxiv.org/abs/2302.04903)
- **LoopSR** (Wu, Xie, Cao, Lai, Zhang), arXiv:2409.17992, IROS 2025, legged robots.
  - Method: it maps real trajectories to a latent space and "reconstruct[s] a digital twin" for continual training in simulation.
  - Real data: "30 loops ... each loop ... a batch of 55 trajectories, each with length of 200 timesteps (equal to 4 seconds)". That is about 1,650 trajectories, or about 110 min (my arithmetic).
  - Result on stairs: 100% real success versus 70% for the original policy and 60% for RMA.
  - Source: [arXiv HTML](https://arxiv.org/html/2409.17992v3)
- **RSR loop** (Shi et al.), arXiv:2503.10118, 2025. It uses differentiable MuJoCo MJX with "an informative cost function that encourages the collection of diverse and representative real-world data" to refine simulation parameters. The approach is closest in spirit to "choose informative real data to fix the sim", but the paper reports no savings versus random. — [arXiv](https://arxiv.org/abs/2503.10118)
- **Real-is-Sim** (Abou-Chakra et al.), arXiv:2504.03597, 2025. A dynamic digital twin (Embodied Gaussians) is "continuously corrected with real world measurements" at 60 Hz, and virtual evaluations are "consistent with real-world results" on PushT. — [arXiv](https://arxiv.org/abs/2504.03597)
- **Background, older.** "Virtual vs. Real" (Marco, Berkenkamp, Hennig, Schoellig, Krause, Schaal, Trimpe), arXiv:1703.01250, ICRA 2017. Multi-fidelity Entropy Search chooses between sim and real experiments; on a cart-pole it finds good policies "with fewer experiments than standard Bayesian optimization on the physical system only". — [arXiv](https://arxiv.org/abs/1703.01250)

**Fine-tuning the policy with real data after twin or sim training**
- **RialTo** (Torne, Simeonov, Li, Chan, Chen, Gupta, Agrawal), arXiv:2403.03949, RSS 2024 ([proceedings](https://www.roboticsproceedings.org/rss20/p015.pdf)).
  - Real data: about 15 real demonstrations per task. A scene takes "25 minutes and 12 seconds of which only 14 minutes and 40 seconds were active work".
  - Book on shelf: 90% success versus 40% for BC with 50 demos. The paper says this is "approximately 2.5 times higher success rate than pure BC, despite using less than one third the number of demonstrations".
  - RialTo does not use real rollouts to correct the twin.
  - Source: [arXiv HTML](https://arxiv.org/html/2403.03949v3)
- **TwinRL** (Q. Xu, J. Liu, R. Zhou, S. Shi, ... S. Zhang), arXiv:2602.09023, v4 of 19 May 2026.
  - Pipeline: a smartphone-captured twin, then "SFT warm-up, twin RL warm-up, and real-world RL".
  - Real data: "only about 20 minutes of on-robot interaction across four tasks". Insert-Hexagon-Block reaches 100% at "around 44k steps (∼14 min)".
  - Selection rule: "𝒮target={s₀|SR(s₀)<τ} ... During real-world online interaction, episode resets are prioritized from 𝒮target". In other words, real trials are selected by the twin's predicted failure, not by the predicted gap.
  - Speed: "over 30% faster convergence than prior real-world RL methods" (HiL-SERL, ConRFT).
  - The guided-versus-unguided ablation (Fig. 6) reports no numbers for the unguided run.
  - The twin is not corrected from real rollouts.
  - Source: [arXiv HTML](https://arxiv.org/html/2602.09023v4)
- **VLAW** (Guo, Lee, Shi, Chen, Liang, Finn), arXiv:2602.12063, 2026.
  - It uses real rollouts to improve an action-conditioned video world model, then trains the VLA on synthetic rollouts.
  - Real data: "In each iteration, we roll out 50 trajectories per task category", over 2 iterations.
  - Results: base 46.0%, filtered BC after 2 iterations 75.2%, VLAW 86.8%.
  - The paper describes no active selection of rollouts.
  - Source: [arXiv HTML](https://arxiv.org/html/2602.12063v2)
- **Sim-and-real co-training** (Maddukuri et al.), arXiv:2503.24361, 2025. It uses 50 real demos per task (Panda) or 20 (humanoid) plus 1k–10k sim demos per task. Simulation data raises real performance "by an average of 38%". — [arXiv](https://arxiv.org/abs/2503.24361); [HTML](https://arxiv.org/html/2503.24361v2)
  - Follow-up: "A Mechanistic Analysis of Sim-and-Real Co-Training" (Lei, Liu, Maddukuri, Jiang, Zhu), arXiv:2604.13645, 2026. It finds that representation alignment plus domain discernibility matters most and importance reweighting matters second. — [arXiv](https://arxiv.org/abs/2604.13645)
- **SGFT** (Yin, Westenbroek, Bagaria, Huang, Cheng, Kolobov, Gupta), arXiv:2502.02705, 2025. A value function learned in sim guides real exploration, "requiring up to an order of magnitude fewer real-world samples" than baseline fine-tuning on 5 dexterous tasks. — [arXiv](https://arxiv.org/abs/2502.02705)
- **Wagenmaker et al.**, "Overcoming the Sim-to-Real Gap: Leveraging Simulation to Learn to Explore for Real-World RL", arXiv:2410.20254, NeurIPS 2024. Transferring exploratory policies gives an exponential improvement in sample complexity in theory (low-rank MDPs), with real-robot validation. — [arXiv](https://arxiv.org/abs/2410.20254)
- **Hard-to-simulate objectives** (Nai et al.), arXiv:2502.10956, ICRA 2025. Real data models the objective, which is then put into simulation. Result: 24–28% battery-power saving on a quadruped. — [arXiv](https://arxiv.org/abs/2502.10956)

### Inferences
- The pattern "real rollouts correct the sim, then the policy is retrained in the sim" is old (SimOpt 2019) and typically needs very little real data: single episodes up to about 2 h.
- The 2026 contributions (TwinRL, VLAW) apply the pattern to VLAs with phone-captured twins or world models, but each corrects only one side:
  - TwinRL corrects the policy only;
  - VLAW corrects the world model and then the policy, without a twin and without selection.
- No verified paper corrects a reconstruction twin *and* the policy from the same selected real trials in navigation.

### Gaps
- TwinRL's unguided-HiL numbers (Fig. 6) are not given in the text, so the effect of its failure-driven selection by itself cannot be quantified.
- SimOpt's venue and ASID's venue were not re-checked against IEEE/OpenReview.

## Q2. Active or targeted selection of real trials: what savings over random?

### Takeaway
Active or targeted selection of real trials against random has been studied almost only for *evaluation*, not for correcting or training a twin. The reported savings are moderate: 20–40% fewer trials (up to 50–65 of 100 on a likelihood metric), 20–25% of hardware effort, up to 38% variance reduction, and up to 2x more failures found. On the training side, about 2x real-data efficiency (AdaptSim) and "30% faster" (TwinRL) are reported, but against other methods, not against random selection with the same learner.

### Cited Findings
- **Anwar, Gupta, Merchant, Ghosh, Neiswanger, Thomason**, "Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection", arXiv:2502.09829, CoRL 2025 (PMLR v305).
  - Method: cost-aware expected information gain with language priors over tasks.
  - Data: HAMSTER and OpenVLA real data, MetaWorld sim; no navigation.
  - Result: EIG "clearly dominate[s]" when estimating the mean, at lower cost than random.
  - The full text I fetched gave no single savings percentage. A search-engine snippet claimed a "50% reduction" in mean estimates at fixed budget, but I could not confirm it in the paper, so treat it as unverified.
  - Sources: [arXiv](https://arxiv.org/abs/2502.09829); [PMLR](https://proceedings.mlr.press/v305/anwar25a.html)
- **Liao, Cui, Desingh, Deshwal**, "Active Real-World Factor-Based Evaluation for Generalist Robot Policies", arXiv:2607.14439, 2026.
  - Data: 2,331 real evaluations across 3 tasks.
  - Savings: active testing "typically saves the evaluator at least 20-40% of trials compared to typical random testing". Out of 100 trials that is 20–40 fewer for RMSE and "50-65 fewer trials" for log-likelihood.
  - No simulation prior is used: the surrogate is trained "exclusively on the real-world evaluation data".
  - Sources: [arXiv](https://arxiv.org/abs/2607.14439); [HTML](https://arxiv.org/html/2607.14439v1)
- **Parashar, Luo, Sharma, Veer, Schmerling, Sobolewski, Yu, Fan, Pavone**, "Coverage Aware Active Evaluation for Failure Discovery with Paired Systems", arXiv:2608.13719, Aug 2026. This is the closest in mechanism to H3.
  - Method: it "learns a local predictor of target risk by correcting proxy failure signals using control-variate-inspired residual modeling". This is effectively a learned proxy-to-target gap, used to choose which target (real) scenarios to test.
  - Domains: driving, manipulation, quadruped.
  - Result: "discovers up to 2× as many failures as random sampling and active-learning baselines".
  - The goal is failure discovery, not reaching a target success rate.
  - Source: [arXiv](https://arxiv.org/abs/2608.13719)
- **SCAPE** (Zhu, Oh, Huang, Huang, Ma, Tang), arXiv:2608.19425, 2026. It predicts *scenario-conditioned* real performance from limited paired sim/real samples by first correcting sim-to-real bias in simulation labels, with conformal calibration.
  - Scenario-level prediction error falls by 4.9%/34.7% (driving) and 14.5%/27.7% (quadruped) against the two baselines.
  - It "improves testing sample efficiency" on a real Go2.
  - Source: [arXiv](https://arxiv.org/abs/2608.19425)
- **TwinRL** prioritizes real resets from twin-identified failure-prone initial states, as in Q1. It reports "over 30% faster convergence than prior real-world RL methods", which bundles all of its components and is not a selection-versus-random comparison. — [arXiv HTML](https://arxiv.org/html/2602.09023v4)
- **ASID** (Fisher-information-driven exploration versus random exploration for system identification) gives 28.0% versus 10.6% success on sphere striking from one real episode. **SPI-Active** is 42–63% better than baselines. — [ASID](https://arxiv.org/html/2404.12308v2); [SPI-Active](https://arxiv.org/abs/2505.14266)
- **AdaptSim**: about 2x real data efficiency against system identification and training directly in the target. — [arXiv](https://arxiv.org/abs/2302.04903)
- **Older perception analogue.** "Bayesian Active Learning for Sim-to-Real Robotic Perception", arXiv:2109.11547, actively picks real images to fine-tune a sim-trained perception model; savings not extracted. — [arXiv](https://arxiv.org/pdf/2109.11547)

### Inferences
- Nothing verified selects real trials by the *predicted twin-to-reality gap* in order to correct both a twin and a policy. The nearest items are:
  - Parashar et al. 2026: a residual gap model selects real tests, for evaluation;
  - SCAPE: scenario-level gap-corrected prediction, for evaluation;
  - TwinRL: twin failure, not gap, selects resets for training.
- The mechanism of H3 is therefore novel as a training and correction rule, and navigation is untouched. The evaluation-side component, however, is crowded (at least 6 papers from Oct 2025 to Aug 2026).
- The relevant strong baseline is not only random selection but TwinRL's failure-driven rule (SR(s₀)<τ in the twin) and an uncertainty/EIG rule. A reviewer will ask for both.

### Gaps
- I found no paper that reports "trials to reach a target success rate" for gap-driven versus random real-trial selection in any domain. The exact metric of H3 has no published precedent to calibrate against.
- Anwar et al.'s exact savings figure is unverified.

## Q3. Predicting sim-to-real performance: SRCC, SIMPLER, prediction-powered and control-variate estimators, failure prediction

### Takeaway
Sim-to-real predictivity is a mature metric in navigation: SRCC started with Kadian 2020, and a phone-captured 3DGS twin reaches SRCC 0.87–0.97 in EmbodiedSplat. Statistical combination of sim and real (PPI, control variates, betting, scenario-conditioned prediction) is an active 2025–2026 area. Its savings are 20–38% and collapse when the sim–real correlation is low.

### Cited Findings
- **Kadian, Truong, Gokaslan, Clegg, Wijmans, Lee, Savva, Chernova, Batra**, arXiv:1912.06321, RA-L 2020.
  - Setup: PointGoal navigation, a LoCoBot, a 3D-scanned lab replica and 9 models.
  - SRCC for success was 0.18 for the CVPR19 Habitat challenge setup, caused by agents exploiting collision "sliding".
  - Tuning simulation parameters raised SRCC_Succ "from 0.18 to 0.844".
  - Source: [arXiv](https://arxiv.org/abs/1912.06321)
- **SIMPLER** (X. Li et al.), arXiv:2405.05941, CoRL 2024 (venue per earlier repo notes). Paired sim-and-real evaluations of manipulation policies show "strong correlation" without full digital twins. — [arXiv](https://arxiv.org/abs/2405.05941)
- **PolaRiS** (Jain et al.), arXiv:2512.16881, 2025. Neural reconstruction from short video scans plus a "simple simulation data co-training recipe" gives a "much stronger correlation" to real generalist-policy performance than existing sim benchmarks. — [arXiv](https://arxiv.org/abs/2512.16881)
- **Zhang, Sha, et al.**, arXiv:2511.04665, 2025. Gaussian-splatting soft-body twins built from video; sim success correlates with real at r>0.9 (per the search snippet of the HTML); used for checkpoint selection. — [arXiv](https://arxiv.org/abs/2511.04665)
- **SureSim** (Badithela, Snyder, Zha, Mikhail, O'Kelly, Dixit, Majumdar), arXiv:2510.04354, 2025.
  - Method: prediction-powered inference with non-asymptotic CIs.
  - Data: n=60 paired real/sim trials plus N=700–2100 extra sim trials.
  - Savings: "over 20−25%" of hardware evaluation effort at ρ≈0.59–0.72.
  - At ρ≈−0.05 "none of our methods beat Classical".
  - Source: [arXiv HTML](https://arxiv.org/html/2510.04354)
- **X4Val** (Luo et al.), arXiv:2606.05159, 2026. A learned cross-domain surrogate inside a control-variates estimator, which works without paired samples. Up to 38.4% variance reduction on driving and real manipulation. — [arXiv](https://arxiv.org/abs/2606.05159)
- **Betting for Sim-to-Real Performance Evaluation** (Mahboob, Chen, Weng), arXiv:2604.24018, RSS 2026. A betting-based estimator "provably outperforming the Monte Carlo estimator" under stated conditions. — [arXiv](https://arxiv.org/abs/2604.24018)
- **PERRY** (Mandyam et al.), arXiv:2507.20068. Conformal and doubly-robust/PPI CIs for off-policy evaluation with biased auxiliary data. — [arXiv](https://arxiv.org/abs/2507.20068)
- **SCAPE** (see Q2): scenario-conditioned prediction of the gap, which is the per-configuration quantity H3 needs. — [arXiv](https://arxiv.org/abs/2608.19425)
- **Predicting transfer from a model** (Zhang, Plappert, Zaremba), arXiv:2009.12864, 2020. A probabilistic dynamics model evaluated on a fixed set of real trajectories predicts sim-to-real transfer and is "highly correlated" with real performance. — [arXiv](https://arxiv.org/abs/2009.12864)

### Inferences
- H3's "predicted twin-to-reality gap" can be built on this literature:
  - SCAPE-style bias-corrected scenario predictors;
  - Parashar et al.'s residual control-variate model;
  - Zhang 2020's dynamics-model transfer metric.
- The statistical ceiling is informative. When savings from optimal *estimation* sit at about 20–40%, a *selection* rule for training has to exploit heterogeneity in the gap across configurations to beat 50%.
- SureSim's failure at low ρ implies that H3's gap predictor will not help if twin and real outcomes are weakly correlated. The SRCC of the twin should be measured and reported as a precondition.

### Gaps
- Failure *prediction* specifically transferred from twin to real (monitors trained in the twin) was not re-searched here; repo niche N5 covers it and is marked "open" for navigation.

## Q4. Evidence specific to navigation versus manipulation

### Takeaway
Navigation has strong zero-shot twin-to-real results and good predictivity:
- Vid2Sim: +68.3% real success;
- EmbodiedSplat: +20/+40 pp real success, SRCC 0.87–0.97;
- the "Synthetic vs. Real" navigation study: sim-trained beats real-trained by 31 pp.

Almost no navigation work uses a small, selected real set to correct the twin and the policy. The exception is the older BDA, which corrects dynamics from about 5k real transitions. Every paper on active or gap-driven selection of real trials is manipulation, driving or legged.

### Cited Findings
- **BDA** (Truong, Chernova, Batra), arXiv:2011.12421, RA-L 2021. Real-to-sim for vision plus sim-to-real for dynamics in PointGoal navigation: "BDA with only 5k real-world (state, action, next-state) samples matches the performance of a policy fine-tuned with ~600k samples ... speed-up of ~120x". — [arXiv](https://arxiv.org/abs/2011.12421)
- **"Rethinking Sim2Real"** (Truong, Rudolph, Yokoyama, Chernova, Batra, Rai), arXiv:2207.10821, CoRL 2022 (PMLR v205). Across 2 simulators and 3 robots, adding fidelity did not help; "building simple models of the robot motion using real-world data can improve learning and generalization". — [arXiv](https://arxiv.org/abs/2207.10821); [PMLR](https://proceedings.mlr.press/v205/truong23a.html)
- **EmbodiedSplat** (Chhablani, Ye, Irshad, Kira), arXiv:2509.17430, ICCV 2025. iPhone-captured 3DGS meshes in Habitat-Sim for fine-tuning ImageNav policies. Absolute real-world SR improves by 20% over HM3D-pretrained and 40% over HSSD-pretrained zero-shot baselines, with "sim-vs-real correlation (0.87-0.97)". — [arXiv](https://arxiv.org/abs/2509.17430)
- **Vid2Sim** (Xie, Liu, Peng, Wu, Zhou), arXiv:2501.06693, CVPR 2025. A monocular video becomes an interactive 3DGS-plus-mesh sim for urban navigation RL, with +31.2% (twin) and +68.3% (real) success rate over prior simulation methods, deployed zero-shot. — [arXiv](https://arxiv.org/abs/2501.06693); [CVF](https://openaccess.thecvf.com/content/CVPR2025/papers/Xie_Vid2Sim_Realistic_and_Interactive_Simulation_from_Video_for_Urban_Navigation_CVPR_2025_paper.pdf)
- **"Synthetic vs. Real Training Data for Visual Navigation"** (Suomela et al.), arXiv:2509.11791, ICRA 2026. The sim-trained policy "outperforms its real-world-trained version by 31 and the prior state-of-the-art methods by 50 points in navigation success rate". — [arXiv](https://arxiv.org/abs/2509.11791)
- **Kadian 2020** (Q3): navigation-specific evidence that correcting simulation parameters from real paired tests changes predictivity sharply (0.18 to 0.844). — [arXiv](https://arxiv.org/abs/1912.06321)
- **2026 3DGS navigation infrastructure**, with no real-data correction loop in either:
  - NavGSim (Liu et al.), arXiv:2603.15186: trains a navigation VLA, evaluated in sim and real;
  - NavArena (Wang et al.), arXiv:2609.04602: 3DGS navigation benchmarks, 2,000+ scenes.
  - Sources: [NavGSim](https://arxiv.org/abs/2603.15186); [NavArena](https://arxiv.org/abs/2609.04602)
- **RL fine-tuning of diffusion navigation policies** (Sheng et al.), arXiv:2603.12868, 2026. GRPO in Isaac Sim raises SR from 52.0% to 58.7%. Fine-tuning is in sim, not with selected real trials. — [arXiv](https://arxiv.org/abs/2603.12868)

### Inferences
- In navigation, visual appearance is largely handled by reconstruction twins and pretrained encoders (EmbodiedSplat, Suomela). The residual gap is more likely to sit in dynamics and collision geometry (Kadian's sliding exploit, Truong 2022) and in scene changes. That gap is spatially localized: doorways, clutter, glass, thin obstacles. Localized gaps are exactly where gap-targeted selection can beat random by a lot.
- The flip side: navigation zero-shot success from good twins is already high (EmbodiedSplat, Vid2Sim), so the headroom for "trials to target P" may be small. H3 needs a target P set above zero-shot twin performance.
- The navigation niche for H3 is open: no verified navigation paper actively selects real trials.

### Gaps
- There are no published real-trial counts for navigation fine-tuning after twin training comparable to TwinRL's minutes. EmbodiedSplat's real evaluation episode counts were not extracted.

## Q5. Is "≥50% fewer real trials than random selection" plausible? What effect sizes are reported?

### Takeaway
Plausible but at the upper edge. Direct selection-versus-random savings in the literature are mostly 20–40%. Larger effects (about 2x, i.e. 50%) appear for failure discovery, task-driven sim adaptation, and some likelihood metrics. Order-of-magnitude savings appear only when comparing whole *methods* (SGFT, BDA), not selection rules. H3 at ≥50% against *random* is defensible only if the gap is concentrated in a minority of configurations and the predictor ranks them well. Against the failure-driven (TwinRL) rule, 50% is unlikely.

### Cited Findings (effect sizes, grouped by what is compared)

**Selection or evaluation versus random**
| Source | Reported effect |
|---|---|
| [Liao et al. 2026](https://arxiv.org/html/2607.14439v1) | 20–40% fewer trials (RMSE); 50–65 fewer of 100 (log-likelihood) |
| [SureSim](https://arxiv.org/html/2510.04354) | 20–25% hardware effort saved; none at low ρ |
| [X4Val](https://arxiv.org/abs/2606.05159) | up to 38.4% variance reduction |
| [Parashar et al. 2026](https://arxiv.org/abs/2608.13719) | up to 2x failures found |

**Training-side, method versus method (not a selection-only comparison)**
| Source | Reported effect |
|---|---|
| [AdaptSim](https://arxiv.org/abs/2302.04903) | ~2x real-data efficiency |
| [TwinRL](https://arxiv.org/html/2602.09023v4) | >30% faster convergence |
| [SGFT](https://arxiv.org/abs/2502.02705) | up to 10x fewer samples |
| [BDA](https://arxiv.org/abs/2011.12421) | ~120x fewer samples |
| [RialTo](https://arxiv.org/html/2403.03949v3) | 2.5x success with less than 1/3 of the demos |

**Active versus random exploration for system identification**
| Source | Reported effect |
|---|---|
| [ASID](https://arxiv.org/html/2404.12308v2) | 28% vs 10.6% success |

### Inferences
- **Novelty.** Medium-high as stated. No verified paper selects real trials by *predicted twin-to-real gap* to reach a *target real success* while *correcting both the twin and the policy*, and none does it in navigation. Scooping risk is high:
  - TwinRL is one step away: swap SR(s₀)<τ for a gap score and add twin correction;
  - Parashar et al. (Aug 2026) and SCAPE already build gap/residual predictors that pick real tests;
  - the Pavone group (X4Val, Parashar) is active in exactly this space.
- **Realism of the 50% threshold.** Random selection is a weak baseline, so 50% is reachable if the gap is heterogeneous. Recommendations:
  1. Pre-register the primary comparison against random, and also report against failure-driven (TwinRL rule) and uncertainty/EIG selection, because reviewers will demand it.
  2. State the expected effect honestly: 20–40% is the literature norm, and 50% is ambitious.
  3. Define "trials to target P" with a CI. Binary navigation success needs many trials per estimate, so each "trials-to-target" measurement is itself noisy, and several seeds or runs per arm are needed.
  4. Make the 50% conditional on a measured precondition: twin–real correlation or SRCC above some level, and gap heterogeneity (a share of the gap mass concentrated in the top-k configurations). SureSim shows gains vanish at low correlation.
  5. Consider stating H3 as the upper 95% bound of the trials ratio < 1, with 0.5 as the point target. This matches the repo's existing "ratio bound < 1" pattern in content/07-questions-hypotheses.md.
- The per-configuration gap predictor can reuse SCAPE-style bias correction or Parashar-style residual control-variate modelling. Kadian/EmbodiedSplat-style SRCC serves as the global sanity check.

### Gaps
- No published measurement of trials-to-target for gap-driven versus random selection exists in any domain, so the 50% threshold cannot be calibrated from prior work.
- TwinRL's unguided ablation numbers are unavailable.
- Navigation real-trial costs (minutes per episode, resets) comparable to TwinRL's "20 minutes" were not found.

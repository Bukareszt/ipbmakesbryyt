# §9 Planowane metody badawcze / Planned research methods (max 2 pages)

Most of my work will consist of training and fine-tuning policies inside learned world models, measuring how they perform on real data and designing methods that analyse and align the representations they learn. No established theory covers the generalization of policies trained in world models, so the work will be mostly empirical. Domain adaptation theory [20] will be my motivation, and where possible I will check whether an alignment lowers the discrepancy between imagined and real features without raising the joint error.

I will use PyTorch for training, Git with GitHub repositories for version control and Hugging Face for downloading and publishing models and data. For navigation I will start from NWM [3]. For manipulation I will use DINO-WM [15], V-JEPA 2-AC [9] or the small LeWorldModel as latent world models, and Ctrl-World [17] or Cosmos-Predict [4] as video world models. I will use open weights where they exist and respect their licences, some of which allow only non-commercial use. As a physics simulator for comparison I will use NVIDIA Isaac Lab 3.0 in its kit-less mode with the Newton physics engine, which runs on H100 GPUs. I will use Cosmos Transfer to add photorealistic appearance to simulator renderings. Isaac Sim does not support A100 or H100 GPUs, so I will use it only on an RTX workstation if one is available.

Since I will not have my own robot at the start, I will evaluate mainly on public data. For manipulation I will use DROID, on which Ctrl-World and V-JEPA 2-AC were trained, and BridgeData V2, whose WidowX setup is one of the robot setups modelled in SIMPLER [19]. For navigation I will use RECON and SCAND, two of the real robot datasets on which NWM was trained. Held-out trajectories and scenes of these datasets give real observations paired with imagined ones that start from the same state and follow the same actions, which I need for probing and alignment. I will also check whether the ranking of policies in a world model agrees with published real-robot results, from SIMPLER and from the real evaluations reported for the world models. Evaluation inside a world model or on recorded data is only a proxy for reality. It leaves out parts of the gap, such as the robot's own actuation and camera, and I will state this with every result. If access allows, I will use a real robot in a university laboratory to check selected results.

For RQ1 I will inject one type of error at a time into a world model, or remove it by replacing imagined frames with real or physics-simulated ones. The error types are ignored or delayed actions, wrong contact outcomes, appearance changes and drift over long rollouts. I will train or fine-tune a policy in each version and measure the change in its success. I will compare the change in the latent representation of a fixed pretrained encoder, such as DINOv2 or V-JEPA 2, with pixel-level video metrics such as PSNR, LPIPS and FVD by their rank correlation with harm. I will also test targeted augmentation against uniform augmentation of equal strength (H1). For RQ2 I will train linear probes, that is, linear models that read task information such as the direction to the goal or the position of an object, on the hidden states of each stage of the policy for imagined inputs, and test them on the paired real inputs. Control tasks with random labels will show that the probes do not simply memorize. To test whether the policy uses the lost information, I will replace the component of the real hidden state along the probe directions with the one from the paired imagined input and check whether the action improves. I will compare this with replacing the same number of random directions. I will then add an alignment loss, such as maximum mean discrepancy or a contrastive loss between paired features, at the identified stage. I will compare it with the same loss at the input, at the final features, at all stages and at layers chosen as in surgical fine-tuning [25] (H2). For RQ3 I will compare rules for selecting real rollouts with random selection, failure-driven selection as in TwinRL [26] and unselected data as in VLAW [5], at equal budgets. I will also compare correcting both the world model and the policy with correcting only one of them. For RQ4 I will apply the methods with unchanged settings to held-out scenes and to the other task. I will measure the latent gap as an observation term, the distance between the embeddings of matched imagined and real states, and a dynamics term, the error of the world model's latent prediction on real transitions. I will test whether these terms predict the gains better than the rank correlation of world-model success with real success or video quality, using Spearman rank correlation across scenes with permutation tests.

For every policy I will measure the success rate in the world model and in the evaluation setting of each task, the gap between imagined and real performance and the rank correlation of world-model results with real results. I will compare my methods with domain randomization [22], co-training on imagined and real data [23] and the baselines named above, with the same number of training steps and the same amount of real data for every method. To get reliable results I will repeat runs over random seeds and scenes, use statistical tests for comparisons and run ablation studies. Data for training, model selection and final evaluation will be kept separate.

I will run experiments on the H100 nodes of the Wrocław Centre for Networking and Supercomputing (WCSS), with jobs managed by SLURM, and on PLGrid resources. I intend to use AI coding assistants like Claude Code to speed up writing and testing code. They will also help with routine work such as monitoring long experiments and proofreading.

I plan to publish my results at conferences and in journals worth 200 points on the ministerial list. In machine learning these are NeurIPS, ICML and ICLR, in computer vision CVPR, ICCV and ECCV, and in robot learning RSS and the journal IEEE RA-L. Where possible, I will also post the papers as arXiv preprints.

<!-- Wave 32: rewritten around world models -->
<!-- Wave 31: grounding + clarity (ultracode) -->
<!-- Wave 29: humanized (no semicolons) -->
<!-- Wave 28: restyled after the accepted 2025 IPB (2026-09-28, research/accepted_plan_tts_2025.txt). §9 practical first-person methods as in the accepted plan: tools (PyTorch, gsplat, COLMAP, Habitat, ManiSkill3, Git/GitHub, Hugging Face), open release, public data (ScanNet++, MuSHRoom, public robot datasets, SIMPLER [14]), honest proxy statement, optional robot, per-RQ protocol, metrics and statistics, WCSS SLURM + PLGrid, AI coding assistants, venues and arXiv. MLinPL and department clusters dropped. -->
<!-- Wave 27: mechanisms + citation audit fixes (2026-09-27, reports/Mechanizmy uczenia reprezentacji IPB.md). §9: bound with the joint error term; 3D Gaussian Splatting [10] cited; RQ1 per-region correction with a more accurate reference (ScanNet++ laser scans) or controlled injection, randomization of appearance and geometry following the estimated reconstruction error and task relevance at equal total strength; RQ2 linear probes with control tasks, causal interventions, paired alignment loss vs input/final features/all stages/existing layer-selection criteria; RQ3 equal budgets, random and failure-driven baselines, same data refine twin and model; RQ4 gain per scene, rank correlations with tests for dependent correlations; gap defined; robot = check of the direction of results and of the proxy, if access allows. -->
<!-- Wave 24: humanized (2026-09-27, humanizer skill, voice of the accepted Binkowski and ipb4 §9). Visible §9 only: "will serve as motivation" -> "is used as motivation" (bound sentence split); long passive chain on training in the simulators split and made active; "Since the research does not rely on an own robot" -> "does not rely on a robot of its own, so"; not-X-but-Y "reconstruction fidelity, not differences in actuation and sensors" -> "isolates ... and leaves out ..."; RQ paragraph passive chains given the research as actor. No claim, term or citation changed. -->
<!-- Wave 23: trimmed to reference length (2026-09-27, student decision: avoid over-promising; register of the accepted Binkowski and ipb4 §9, ~370-450 words). Visible §9 cut from ~1275 to ~600 words: general empirical ML methodology with theory where possible; twins from real data with neural reconstruction in navigation and manipulation simulators (Habitat, ManiSkill3 as e.g. only); evaluation without an own robot (navigation: independent captures of public datasets, dataset-based reference = reconstruction-fidelity gap; manipulation: SIMPLER-style twins of real tabletop scenes vs published real-robot results [14]); one sentence per RQ; metrics, statistics, ablations; real-robot validation only "if access allows" (semester and robot type dropped); tools, compute, open code; dissemination. Removed: per-RQ baselines and citations [4], [5], [6], [9], [13], real-data units, SPL, BridgeData V2 / Open X-Embodiment / MuSHRoom names, phone captures, uncertainty-estimation detail, rank correlation, the "numbers in brackets" note. -->
<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §9: task-agnostic methods on two equal tasks sharing reconstruction tools; navigation pipeline (Habitat, ScanNet++/MuSHRoom proxy = reconstruction-fidelity gap) kept; new manipulation pipeline: twins from real frames of public robot datasets (BridgeData V2, Open X-Embodiment; described only as far as their arXiv abstracts, verified today: 2308.12952, 2310.08864) and own phone captures, SIMPLER visual matching [14], published paired real results of the same policies (Google Robot and WidowX/BridgeData V2 setups, checked in arXiv:2405.05941) as the real reference; honest limitation: published results cover only released policies, so new models are also evaluated closed-loop in a hidden-parameter simulator (e.g. ManiSkill3, arXiv:2410.00425 verified), which also serves controlled physics studies. RQ1 reference per task; RQ2 task variables per task; RQ3 interaction unit per task; RQ4 across held-out scenes of both tasks and between tasks; gap levels per task; validation on the mobile robot and optionally an arm (sem. 6-7). Trimmed for the 2-page limit: metrics/statistics, tooling and dissemination paragraphs merged; per-Gaussian randomization detail removed. TwinRL citation [22] -> [13]. -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §9 (fixes 1-7): bound = motivation; navigation pipeline only (Habitat); manipulation only in the RQ4 paragraph as a sim-to-sim confirmation in ManiSkill3 with hidden visual/physical parameters; reference simulation measures the reconstruction-fidelity gap, robot = main evidence for actuation/sensor differences, proxy-robot agreement reported as a result; open-loop and closed-loop glossed; RQ1 component replacement, reference-model predictor, fallback, per-region randomization as a separate claim; RQ2 task-decodability probes (task variables), alignment compared with input, final features [6], all layers, full fine-tuning; RQ3 budget counts unlabelled images, same data corrects twin and model, baselines random and failure-driven [22], model-only/twin-only; ASID removed from §9 (manipulation no longer in RQ3); RQ4 vs raw gap size and image-level discrepancy; robot validation one block sem. 6-7. Citations renumbered to the new §6 list ([4], [5], [6], [9], [22]). Trims for the 2-page limit: cooperation-with-PhD-students sentence, representation-similarity sentence, promotion sentence shortened, tooling/compute sentences merged. -->
<!-- Final check (2026-09-27): added the note that bracketed numbers in §9 refer to the §6 reference list; Kachaev et al. AAMAS 2026 venue verified on OpenAlex (doi:10.65109/pper9186). -->
<!-- Review-6 (2026-09-27): two evaluation levels (dataset proxy: open-loop on real frames + reference simulation from the independent higher-fidelity capture; closed-loop on the real mobile robot), gap defined per level; per-region reconstruction uncertainty (view coverage, ensemble disagreement); RQ3 procedure (budget = interaction data, selection scores, dual correction, comparisons at equal real data); manipulation = controlled proxy (hidden visual and physical parameters), no real-arm promise; wording fixes; international dissemination and foreign co-authorship. -->
<!--
Wave 20 (ultracode), 2026-09-27: visible §9 rewritten from scratch in the register of the Binkowski (2022) §9;
aligned with the final RQ1-RQ4 (controlled simulation variants, probing, budget curves, held-out scenes,
second task); no thresholds, no model names, no citations in §9.
-->

<!--
Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top) and
the deep-research report (reports/Uczenie nawigacji w cyfrowych bliźniakach.md, "Rekomendacje" and the
per-hypothesis table). Applied here:
- One unit (operator minutes B = capture + demonstrations + on-robot trials with resets) and the shared
  budget grid {5, 10, 20, 40, 80} min; target P = fraction of the baseline's plateau (e.g. 90% of its P at
  the largest budget); bootstrap CI of the budget ratio by scene.
- Pre-registered baselines per hypothesis: H1 uniform / FisherRF-type task-blind [23] / risk- or
  semantics-weighted with a reconstruction objective [25, 26] (+ ASID-type task-blind identification [20]
  for the physical part); H2 uniform DR [6, 7] / no DR / ablations; H3 random / uniform coverage /
  TwinRL-style failure-driven rule (SR(s0) < tau, [18]); H4 assembled baseline = EmbodiedSplat-style
  capture + fine-tuning [12] + RialTo/TwinRL-style real correction [16, 18], same budget, + zero-shot +
  real-only reference curve.
- H2 difficulty regime (baseline <= ~75%), 150-300 episodes per arm (report: "detekcja +10 pp przy bazie
  ~60% (alpha = 0,05 jednostronnie, moc 80%) wymaga rzędu 150-300 epizodów na ramię"); world model = ablation.
- H3: >= 50% decided vs random; vs the failure-driven rule only upper bound < 1; precondition = SRCC
  twin-vs-proxy above a pre-registered threshold; honest note that selection rules save 20-40% (report;
  SureSim [33] 20-25%).
- H4: >= 30-50 episodes per point (report table).
- Tools: Habitat-Sim/Lab + gsplat + COLMAP 4.x (report: Isaac Sim does not support A100/H100, so it is
  excluded; the visible text says "run on the data-centre GPUs of WCSS and PLGrid" instead of naming
  Isaac). gsplat and COLMAP are software, not cited as references.
- Datasets: ScanNet++ [21] (licence signed by the supervisor; no derived twins published) + MuSHRoom [22]
  (CC-BY-4.0, releasable; ~10 rooms per the report).
- Robot: TurtleBot 4 Lite (~1.7k EUR, SzD Minigrant) or K29 robots; SRCC proxy-vs-robot in 2 PWr rooms.
- Scope: static indoor scenes (dynamic people = future work, §12).
- Manipulation = generalization test: ManiSkill3 [2] with hidden physics as "reality" (Wave 13 protocol,
  coordinator decision task_4385733a766f) + SIMPLER [5] published paired sim/real results; no thresholds.
- Compute: the report's estimate (160-320 3DGS fits <= ~300 GPU-h; policy fine-tuning 10^3-10^4 GPU-h) is
  OUR ESTIMATE, kept out of the visible text; "measured in the pilot" instead.
- Kept from v6/review-4: separate captures (R3-F1), second reference sign check, >= 20 scenes / 10 held
  out (R3-F10), pilot-set difficulty (R3-F6), planner-path relevance (R3-F9), walking-tour time (R3-F5),
  held-out real samples counted (R3-F4), re-capture counted (R3-F12), real-only = imitation (R3-F2), RL on
  a subset of scenes (R4-F9), hidden physical parameters of "reality" (R4-F2), the assembled baseline with
  equal effort (R4-F3), image-goal and point-goal tasks (R4-F5; instruction-following dropped for space).
- "one task-weighted information criterion covers both views and physical parameters" = the report's
  methodological suggestion (FisherRF + ASID/SPI-Active in one task-weighted criterion; "such a
  combination was not found in any source"). Design choice, CONFIRM with the supervisor.
- H1 unit: operator minutes now (v7 one unit); frames also reported (was "views", R4-F6).
Refs follow the Wave 18 §6 list: [1] Habitat, [2] ManiSkill3, [4] Kadian (SRCC), [5] SIMPLER, [6] Tobin,
[7] Peng, [8] Chebotar, [10] Maddukuri, [11] 3DGS, [12] EmbodiedSplat, [16] RialTo, [18] TwinRL,
[19] BayesSim, [20] ASID, [21] ScanNet++, [22] MuSHRoom, [23] FisherRF, [24] Bayes' Rays, [25] Liu et al.
risk-aware, [26] AREA3D, [27] GNM, [28] ViNT, [29] OpenVLA, [30] NWM, [31] Cosmos, [33] SureSim,
[34] DINOv2, [35] PPI. Reference numbers in the older comments below are pre-Wave-18.
-->
<!--
(history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
"methods per stage, method families only, brief evaluation protocol"; "§9 may give at most 'e.g.'
examples of method families"; navigation only. Stages renamed I-IV -> 1-3 + whole pipeline (v6 numbering).
Kept from v5/review-3: the non-circular proxy reality (R3-F1: laser-scan + DSLR reference vs twin from the
separate phone capture; second-reference sign check; proxy error reported), >= 20 scenes / 10 held out
(R3-F10), minimum path length from a pilot (R3-F6), planner-path task relevance (R3-F9), capture from the
recorded pool + walking-tour time (R3-F5), held-out real samples counted (R3-F4), re-capture counted
(R3-F12), real-only = imitation of real demonstrations with the same initialization (R3-F2), robot = 2
validation campaigns, ~8 h each. Removed per v6: model and checkpoint names (OpenVLA-OFT, pi0, NaVILA as
the chosen model, Qwen2.5-VL, Cosmos-Predict2, NWM as chosen checkpoints), LoRA/SFT/PPO recipe details,
the ~23k H100-hour estimate (it was specific to 7B VLAs; research/vla-wm-crowdedness.md §4 keeps it),
manipulation tier A (ManiSkill3) and tier B (SIMPLER), TwinRL as the named H4 baseline (now "existing
real-to-sim-to-real approach, e.g. [14, 27]"). Physical part for navigation (traversable surfaces,
collisions, actuation noise) = design choice, CONFIRM supervisor. "Instruction-following" navigation added
next to image-goal because foundation-model initialization may be language-conditioned (design choice).
Refs follow the Wave 16 §6 list: [1] Habitat, [5] Tobin, [6] Peng, [7] Chebotar, [9] Maddukuri,
[10] 3DGS, [11] EmbodiedSplat, [14] RialTo, [15] BayesSim, [16] ScanNet++, [17] FisherRF, [18] Bayes' Rays,
[19] Liu et al. risk-aware, [20] AREA3D, [21] GNM, [22] ViNT, [23] OpenVLA, [24] NaVILA, [25] NWM,
[26] Cosmos, [27] TwinRL, [29] DINOv2, [30] PPI. Reference numbers in the older comments below are
pre-Wave-16.
-->
<!--
Wave 15-U (issue #32), 2026-09-26: pivot decision v5 (research/pivot-decision.md, top): a pretrained open VLA
fine-tuned sim-first in the twin, a VLM for task-aware capture and success judging, a world model grounded in
the twin. v3 scope, v4 framing, tiers A/B/C, all review-3 fixes and the §7 decision rules (worker T, final
§7 v5; coordinator msg_65a79c659e58) are mirrored: H2(b) twin + world model vs twin only (lower 95% bound of
the paired gain > 0, >= 2 budgets); H4(a) real-only = fine-tuning the SAME VLA on real data only (LoRA SFT
on expert demonstrations in the reference; real-only RL shown); H4(b) = strongest existing twin fine-tuning
pipeline for VLAs, TwinRL/RialTo-style (uniform capture, domain randomization, RL in the twin, random or
failure-driven real trials). The "world-model simulator also reported" comparator of Wave 14 is now part
of the method (C2) and of H2(b).
Models (research/vla-wm-crowdedness.md §2; all checked 2026-09-26):
- OpenVLA-OFT: code github.com/moojink/openvla-oft MIT; OpenVLA weights HF openvla/openvla-7b (MIT tag), but
  the openvla README says the models are "derived from Llama-2" and "subject to the Llama Community License".
- pi0 / pi0.5: github.com/Physical-Intelligence/openpi, Apache-2.0; README: LoRA fine-tuning "> 22.5 GB",
  full "> 70 GB" (A100 80GB / H100).
- OpenVLA LoRA: openvla README: "a single A100 GPU with 80 GB VRAM ... at least ~27 GB of memory";
  batch 16 "requires ~72 GB GPU memory".
- NaVILA: code github.com/AnjieCheng/NaVILA Apache-2.0; HF a8cheng/navila-llama3-8b-8f has NO licence tag
  (§12 licence risk). Mapping of its mid-level language actions to Habitat actions = design choice
  (CONFIRM in the T3.1 pilot). Tasks "instruction and image-goal navigation" replace point-goal (the VLA
  is language-conditioned); image-goal is kept from R3-F6.
- Qwen2.5-VL-7B-Instruct: HF, Apache-2.0.
- Cosmos-Predict2 checkpoints: HF nvidia/Cosmos-Predict2-2B-Video2World, NVIDIA Open Model License (gated
  "auto"). NWM: HF facebook/nwm, CC-BY-4.0, gated (manual).
- PPO as the RL algorithm: [16] "We identify PPO as a more effective RL algorithm for VLAs than
  LLM-derived methods like DPO and GRPO". RL tooling [15] SimpleVLA-RL (MIT); RLinf (Apache-2.0, ships a
  3DGS ManiSkill "GSEnv" for Real2Sim2Real per its README).
- TwinRL code: github.com/zhourui9813/TwinRL, MIT, "offline training code" (Octo/SERL-based, README).
Compute: "one 8-GPU node" = SimpleVLA-RL README example (8x A800 80GB). ~23k H100-hours = OUR ESTIMATE
(research/vla-wm-crowdedness.md §4: 96 LoRA SFT runs x 8 GPU-h, 48 RL runs x 192 GPU-h, 8 WM adaptations
x 384 GPU-h, ~60 Stage III-IV runs x 128 GPU-h, +10%); UNVERIFIED until the T3.1 pilot. WCSS Lem = 76 nodes
x 4 H100 96 GB, 7-day queue (research/resources.md §2).
Design choices (CONFIRM supervisor): the VLM's grounding as an extra task-relevance term in C1 (next to
planner-path visitation, R3-F9); world-model rollouts started from states in the twin's most uncertain
regions and weighted by that uncertainty (C2b); gap score in C3 = twin uncertainty + twin-WM disagreement +
LoRA-ensemble action spread; the H4(b) pipeline reports the better of random and failure-driven trial
selection; AREA3D-type VLM-guided reconstruction selection as an extra H1 comparator (not in the H1
decision rule).
Dropped with the §6 reference cut: GaussGym (3DGS renderer now unnamed), feature-alignment DA comparator
[Cheng], selection rules MetaMVUC/AMF/Anwar, SureSim, GaussTwin (photometric correction now uncited),
SimOpt, real-only scaling [Lin]. Refs renumbered to the Wave 15 §6 list: [1] Habitat, [2] 3DGS, [3]
RialTo, [5] EmbodiedSplat, [6] ManiSkill3, [7] BayesSim, [8] OpenVLA, [9] pi0, [10] NaVILA, [11] LoRA,
[12] OFT, [14] Maddukuri, [15] SimpleVLA-RL, [16] Liu et al. (RL for VLA), [17] TwinRL, [18] Cosmos,
[19] NWM, [20] WMPO, [23] Qwen2.5-VL, [24] Du et al., [25] FisherRF, [26] Bayes' Rays, [27] Liu et al.
risk-aware, [28] ASID, [29] AREA3D, [30] ScanNet++, [31] Tobin, [32] Peng, [33] DINOv2, [34] PPI,
[35] SIMPLER. Reference numbers in the older comments below are pre-Wave-15.
-->
<!--
Wave 14 (issue #30), 2026-09-26: pivot decision v4 (research/pivot-decision.md, top; framing only, v3 scope
and all review-3 fixes unchanged). The intro now says the dissertation develops ONE method with components
C1-C3 (one per loop step), Stages I-III develop and test one component each (ablations, RQ1-RQ3), Stage IV
tests the whole method (RQ4 = thesis H4). Stage headings renamed "C1/C2/C3". Stage IV adds the v4 baseline
"strongest existing real-to-sim-to-real pipeline" = uniform capture + domain randomization + random
real-data selection, RialTo-style (v4 wording; RialTo = §6 [3]); it replaces the former "uniform loop"
comparator and keeps the same twin, learner and correction so only the allocation differs (design choice).
H4 success criterion adds (b) >= 2x less real data than that pipeline, upper 95% bound of the ratio < 1
(mirrors §7; (b) new in v4, CONFIRM supervisor). Trims for the 2-page limit (no content removed): wording
of the tier-A sharing clause, Stage II baselines/metric, Stage III selection, Stage IV curves.
-->
<!--
(history) Wave 13 (issue #29), 2026-09-26: generalized for pivot decision v3 (research/pivot-decision.md) and the
coordinator's agreed §7 protocol (msg_05231fbe3093): per-testbed tier A with a separate, higher-fidelity
reference; navigation = ScanNet++ laser scan + DSLR reference vs. phone-stream twin; manipulation =
ManiSkill3 scene with held-out ground-truth physical parameters vs. 3DGS twin from a subset of its views +
parameters identified from a few interactions; tier B = published SIMPLER paired sim/real evaluations;
one operator-time cost; metric P; H4 needs both testbeds + tier-B direction. Navigation is no longer
"primary"; "rollouts" -> "trials"; the twin has a physical part (system identification, BayesSim-type
posterior [9]); task relevance for physical parameters = sensitivity of the expert's success in the twin
to the parameter's posterior (design choice, CONFIRM supervisor); ASID [21] as the task-blind
identification baseline. Navigation's physical part = actuation-noise parameters of the robot model
(design choice). Manipulation configuration count (>= 20, 10 held out) mirrors navigation (design choice).
SIMPLER ranking check: SIMPLER's paired real evaluations of published policies (RT-1/Octo family on Google
Robot and WidowX set-ups per the SIMPLER paper) are to be re-read before Stage IV. The ManiSkill3
physical-parameter ranges are pre-registered in T3.1. Tier C manipulator: K29 Laboratorium Robotyki
(UR3, FANUC LR Mate, ABB IRB 120; research/resources.md §1), availability UNVERIFIED, hence "where access
is agreed". Refs renumbered to the Wave 13 §6 list: [1] Habitat, [2] 3DGS, [5] EmbodiedSplat, [7]
GaussGym, [8] ManiSkill3, [9] BayesSim, [11] Lin, [12] Suomela, [15] Maddukuri, [17] FisherRF, [19] Bayes'
Rays, [20] Liu et al., [21] ASID, [22] ScanNet++, [23] Tobin, [24] Peng, [25] SimOpt, [26] Cheng, [27]
DINOv2, [29] MetaMVUC, [30] AMF, [31] Anwar, [32] PPI, [33] SureSim, [34] SIMPLER, [35] GaussTwin.
Reference numbers in the older comments below are the OLD (review-3) numbers.
-->
<!--
Wave 11 (issue #26), 2026-09-26: rewritten for pivot decision v2 (research/pivot-decision.md, binding).
Stages follow the loop: I task-aware capture (H1, >= 40% less capture), II uncertainty-aware training
(H2, >= 10 pp over uniform DR), III active real-rollout selection + twin/policy correction (H3, >= 50%
fewer rollouts), IV whole-loop exchange rate (H4, <= 10% of real-only data) + manipulation. Thresholds
copied from pivot-decision.md; decision rules mirrored from the final content/07 (issue #25, worker T):
recon-only comparator in H1, >= 2 budgets in H2, ratio bounds in H3/H4, uniform-loop and world-model
comparators in H4(a), H4(b) sign rule.
Removed from wave 9-10: paired-frame benchmark, CKA/probe gap localization, policy zoo, weight-space
predictors, conformal failure monitors (representation thesis; benchmark building rejected by the student).
Design choices (CONFIRM supervisor):
- Tier A "capture" = selection of frames from the recorded pool (offline NBV); task relevance = visitation
  or attention of a pilot policy; ensemble disagreement as the gap predictor; the capture itself as the
  "small real set" for H2(b).
- Real-only baseline in tier A = policy trained on episodes in the reference twin, counted as real data.
- Manipulation tier A: reference = the ManiSkill3 twin environment, training twin = 3DGS from subsampled
  renders; SIMPLER checkpoints/paired numbers to be re-read before Stage IV.
- Robot time: 3 x 2 x 30 x 2 min = 360 min + 40 x 2 min = 80 min ~ 7.3 h, rounded to ~8 h. ~2 min per
  episode incl. reset is ASSUMED; confirm after the first campaign.
- UNVERIFIED: K46 GPU servers; RGB-D availability at Denali; ScanNet++ licence terms for releasing derived
  reconstructions (§12 risk).
Refs are §6 numbers of the review-3 list (old [19]-[35] shifted by +1 after inserting Liu et al. as [19]):
[1] Habitat, [2] 3DGS, [3] EmbodiedSplat, [5] GaussGym, [8] ManiSkill3, [9] Lin, [10] Suomela,
[13] Maddukuri, [16] FisherRF, [18] Bayes' Rays, [19] Liu et al. risk-aware view acquisition, [20] ScanNet++,
[21] Tobin, [24] Cheng, [26] DINOv2, [28] MetaMVUC, [29] AMF, [30] Anwar, [33] PPI, [34] SureSim,
[35] SIMPLER, [36] GaussTwin.
Review-3 (issue #27), 2026-09-26 (research/review-3.md): R3-F1 tier-A reference = ScanNet++ laser-scan mesh
textured from DSLR images (arXiv:2308.11417 abstract), twin = 3DGS from the iPhone stream; second reference
(3DGS from all DSLR images) as a sign check. EmbodiedSplat runs GS-reconstructed meshes in Habitat-Sim
(arXiv:2509.17430 abstract, "we reconstruct meshes via GS"). R3-F6 image-goal navigation as in EmbodiedSplat;
minimum geodesic distance fixed in the T3.1 pilot. R3-F9 planner-path task relevance (no training in the
capture loop); imitation as the main learner. R3-F5 capture cost: views (H1 decision) plus an estimated
walking-tour time (secondary; walking speed and dwell per view pre-registered). R3-F8 risk-aware view
selection (Liu et al., arXiv:2403.11396) as an H1 comparator where its code runs. R3-F4 held-out capture
slice for H2(b). R3-F12 re-captured views counted. R3-F2 real-only = imitation of planner demonstrations.
R3-F7 manipulation proxy = simulator rendering vs 3DGS twin, physics shared (visual part only).
-->

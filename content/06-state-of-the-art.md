# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Real-to-sim-to-real with digital twins.** A real-to-sim-to-real loop builds a simulation of the target
scene or object (a *digital twin*) from real data, learns a policy in it and transfers it back. Generic
simulators such as Habitat [1] train at scale, but not in the target scene. 3D Gaussian Splatting (3DGS)
[2] turns a short camera capture into a photorealistic twin, and policies trained in such twins transfer
in manipulation (RialTo [3], SplatSim [4]) and navigation (EmbodiedSplat [5]); GPU simulators ship twin
environments (ManiSkill3 [6]). Physical parameters are inferred from real trajectories as a posterior
(BayesSim [7]). Building a twin is no longer the bottleneck; **real data** is: the capture that builds the
twin and the real trials that correct it. Current systems fix this cost by hand;
RialTo's ablation over 0–15 real demonstrations is the closest published analysis of a real-data budget.

**Pretrained vision-language-action (VLA) policies.** Open VLA models map camera images and an instruction
to actions: OpenVLA [8], π0 [9] and, for navigation, NaVILA [10].
They need fine-tuning for a new setup. Low-rank adaptation (LoRA) [11] makes this feasible on a single GPU
[8], and the OFT recipe [12] raises success and speed. Fine-tuning still consumes real demonstrations: in
navigation, more data from a known location saturates quickly [13], and sim-and-real co-training raises
real success by 38% on average [14].

**Fine-tuning VLAs in simulation, twins and world models (crowded).** Reinforcement learning (RL)
fine-tuning of VLAs in simulation improves on supervised fine-tuning, especially under distribution shift
[15, 16]. TwinRL [17] fine-tunes a VLA with RL in a twin reconstructed from a smartphone capture and uses
the twin to find failure-prone configurations for targeted real rollouts, reporting 20 minutes of on-robot
interaction. Learned **world models** serve as the simulator instead: open world foundation models are
post-trained per setup (Cosmos [18]; NWM [19] for navigation), VLAs are optimized on-policy inside them
without real interaction [20], and VLAW [21] improves a world model with real rollouts and then the VLA
with its synthetic data. GigaWorld-0 [22] combines 3DGS reconstruction, system identification and video
generation into a data engine for VLAs. Open vision-language models (VLMs) such as Qwen2.5-VL [23] can
judge task success [24]. Here they are components and baselines, each reported at a fixed, hand-chosen
real-data budget.

**Capturing less: active reconstruction and identification.** Active view selection chooses the images
that improve a reconstruction most: FisherRF [25] maximizes expected information gain on radiance-field
parameters, and Bayes' Rays [26] estimates an uncertainty field for a trained radiance field. Risk-aware
view acquisition [27] weights FisherRF by safety-critical regions, ASID [28] designs exploration that
identifies physical parameters from little real data, and AREA3D [29] adds VLM guidance to active
reconstruction. Their objective is reconstruction quality, safe exploration or parameter accuracy, not the
success of a policy fine-tuned in the twin; we found at most two task-aware capture papers a year in
2023–2026. ScanNet++ [30] pairs laser scans and DSLR images with a separate phone stream, so budgets can
be varied offline.

**Learning in an imperfect twin, and collecting few real data.** Domain randomization varies appearance
[31] or dynamics [32] uniformly within hand-set ranges; frozen encoders (DINOv2 [33]) make twin and real
samples comparable. A twin's own reconstruction uncertainty is rarely used as a training signal, and we
found no world model aimed at the regions where the twin is uncertain. On the real side,
prediction-powered inference [34] combines many cheap predictions with a few labels, and SIMPLER [35]
shows on paired simulated and real evaluations that simulation can track the real performance of
manipulation policies. TwinRL picks failure-prone configurations for the policy, and VLAW corrects the
world model with rollouts that are not selected; neither selects the few real trials by the joint
uncertainty of twin, world model and policy under a counted budget.

**Research gap.** Real-to-sim-to-real fine-tuning of VLAs works, but its real-data cost is set by hand,
spent uniformly and measured in one domain per study. Missing is one method that allocates it actively at
every step: (i) VLM-guided, task-aware capture of appearance and physical parameters, judged by task
success (RQ1); (ii) fine-tuning in the twin and in a world model grounded in the twin, driven by the twin's
uncertainty (RQ2); (iii) active selection of the few real data that correct twin, world model and VLA
(RQ3); and (iv) evidence that it needs less real data than real-only fine-tuning of the same VLA and the
strongest existing twin pipeline, measured the same way in manipulation and navigation (RQ4).

### References
[1] M. Savva et al., "Habitat," ICCV, 2019.
[2] B. Kerbl et al., "3D Gaussian Splatting," ACM TOG, 2023.
[3] M. Torne et al., "Reconciling Reality through Simulation," RSS, 2024.
[4] M. N. Qureshi et al., "SplatSim," ICRA, 2025.
[5] G. Chhablani et al., "EmbodiedSplat," ICCV, 2025.
[6] S. Tao et al., "ManiSkill3," RSS, 2025.
[7] F. Ramos et al., "BayesSim," RSS, 2019.
[8] M. J. Kim et al., "OpenVLA," CoRL, 2024.
[9] K. Black et al., "π0," arXiv:2410.24164, 2024.
[10] A.-C. Cheng et al., "NaVILA," arXiv:2412.04453, 2024.
[11] E. J. Hu et al., "LoRA," ICLR, 2022.
[12] M. J. Kim, C. Finn, P. Liang, "Fine-Tuning Vision-Language-Action Models…," RSS, 2025.
[13] L. Suomela et al., "Data Scaling for Navigation…," IEEE RA-L, 2026.
[14] A. Maddukuri et al., "Sim-and-Real Co-Training," RSS, 2025.
[15] H. Li et al., "SimpleVLA-RL," arXiv:2509.09674, 2025.
[16] J. Liu et al., "What Can RL Bring to VLA Generalization?," NeurIPS, 2025.
[17] Q. Xu et al., "TwinRL," arXiv:2602.09023, 2026.
[18] N. Agarwal et al., "Cosmos World Foundation Model Platform…," arXiv:2501.03575, 2025.
[19] A. Bar et al., "Navigation World Models," CVPR, 2025.
[20] F. Zhu et al., "WMPO," arXiv:2511.09515, 2025.
[21] Y. Guo et al., "VLAW," arXiv:2602.12063, 2026.
[22] GigaWorld Team, "GigaWorld-0," arXiv:2511.19861, 2025.
[23] S. Bai et al., "Qwen2.5-VL Technical Report," arXiv:2502.13923, 2025.
[24] Y. Du et al., "Vision-Language Models as Success Detectors," CoLLAs, 2023.
[25] W. Jiang et al., "FisherRF," ECCV, 2024.
[26] L. Goli et al., "Bayes' Rays," CVPR, 2024.
[27] G. Liu et al., "Risk-Aware Active View Acquisition…," arXiv:2403.11396, 2024.
[28] M. Memmel et al., "ASID," arXiv:2404.12308, 2024.
[29] T. Xu et al., "AREA3D," arXiv:2512.05131, 2025.
[30] C. Yeshwanth et al., "ScanNet++," ICCV, 2023.
[31] J. Tobin et al., "Domain Randomization…," IROS, 2017.
[32] X. B. Peng et al., "Sim-to-Real Transfer… with Dynamics Randomization," ICRA, 2018.
[33] M. Oquab et al., "DINOv2," TMLR, 2024.
[34] A. N. Angelopoulos et al., "Prediction-Powered Inference," Science, 2023.
[35] X. Li et al., "Evaluating Real-World Robot Manipulation Policies…," CoRL, 2024.

<!-- Wave 15-U (issue #32), 2026-09-26: pivot decision v5 (VLA/VLM + world models, sim-first fine-tuning in
the twin). New paragraphs on open VLAs + PEFT and on VLA fine-tuning in simulation / twins / world models
(flagged as crowded, per the v5 novelty guardrail; research/vla-wm-crowdedness.md, S2 counts Q1 1/3/40/126,
Q2 0/2/42/183 for 2023-2026). The gap now names the v5 components (VLM-guided capture, twin + twin-grounded
world model, joint twin/WM/VLA uncertainty for real trials) and the H4 comparators of §7 (real-only
fine-tuning of the same VLA; strongest existing twin pipeline = TwinRL/RialTo-style, coordinator message
msg_65a79c659e58). 35 refs (limit <= 35).
New refs, verified 2026-09-26 on the Semantic Scholar batch API (title, authors, date, venue, abstract) and
the arXiv abstract page (author comment); details and quotes in research/vla-wm-crowdedness.md §2:
- [8] OpenVLA arXiv:2406.09246, S2 venue CoRL (2024); "970k real-world robot demonstrations", "fine-tuned on
  consumer GPUs via modern low-rank adaptation methods".
- [9] pi0 arXiv:2410.24164 (Black, Brown, Driess, ...), S2 venue arXiv: cited as arXiv.
- [10] NaVILA arXiv:2412.04453 (A.-C. Cheng, Y. Ji, ...); S2 venue "Robotics" (ambiguous), cited as arXiv.
- [11] LoRA arXiv:2106.09685 (E. J. Hu et al.), S2 venue ICLR (ICLR 2022).
- [12] OpenVLA-OFT arXiv:2502.19645; arXiv comment "Accepted to Robotics: Science and Systems (RSS) 2025".
- [15] SimpleVLA-RL arXiv:2509.09674 (H. Li et al.), arXiv.
- [16] J. Liu et al. arXiv:2505.19789; arXiv comment "Accepted by NeurIPS 2025"; PPO > SFT for generalization.
- [17] TwinRL arXiv:2602.09023 (Q. Xu, J. Liu, R. Zhou, S. Shi, ...): "reconstructs a high-fidelity digital
  twin from smartphone-captured scenes", "identifies failure-prone yet informative configurations,
  enabling targeted human-in-the-loop rollouts", "only 20 minutes of on-robot interaction". GitHub
  zhourui9813/TwinRL README says ACM MM 2026 (not otherwise confirmed): cited as arXiv.
- [18] Cosmos arXiv:2501.03575 (Agarwal et al.), arXiv.
- [19] NWM arXiv:2412.03572, doi:10.1109/CVPR52734.2025.01472 (CVPR 2025).
- [20] WMPO arXiv:2511.09515 (F. Zhu et al.): on-policy VLA RL "without interacting with the real environment".
- [21] VLAW arXiv:2602.12063 (Y. Guo, T. Lee, L. Shi, J. Chen, ...): "uses real-world roll-out data to improve
  the fidelity of the world model".
- [22] GigaWorld-0 arXiv:2511.19861: "3D Gaussian Splatting reconstruction, physically differentiable system
  identification" + video generation as a data engine for VLA learning.
- [23] Qwen2.5-VL arXiv:2502.13923 (S. Bai et al.).
- [24] Du et al. arXiv:2303.07280, S2 venue CoLLAs (2023): success detection as VQA with a pretrained VLM.
- [29] AREA3D arXiv:2512.05131 (T. Xu et al.): active reconstruction with "vision-language guidance".
"20 minutes" is TwinRL's figure (abstract). "we found no world model aimed at the regions where the twin is
uncertain" rests on the S2 queries Q7 (world model + twin/Gaussian) and the top-cited hits
(research/vla-wm-crowdedness.md §1, §3), not on a full survey: supervisor to confirm.
Dropped to stay <= 35 (their §9/§12 uses were removed or reworded in the same wave): Vid2Sim, GaussGym,
PhysTwin, Lin et al. (data scaling laws), CASHER, X-Sim, Truong (Rethinking Sim2Real), GenNBV, SimOpt,
Cheng (generalizable DA), Phys2Real, MetaMVUC, AMF, Anwar et al., SureSim, GaussTwin.
Old (Wave 14) -> new numbers: 1->1, 2->2, 3->3, 4->4, 5->5, 8->6, 9->7, 12->13, 15->14, 17->25, 19->26,
20->27, 21->28, 22->30, 23->31, 24->32, 27->33, 32->34, 34->35; 6, 7, 10, 11, 13, 14, 16, 18, 25, 26, 28-31,
33, 35 dropped. Reference numbers in the older comments below are pre-Wave-15.
-->
<!-- Wave 14 (issue #30), 2026-09-26: pivot decision v4 (framing only). Research gap reworded: what is
missing is ONE method that allocates the real data actively at every step, (i)-(iii) = its components
C1-C3 (RQ1-RQ3), (iv) = evidence that it needs less real data than real-only learning and uniform pipelines
(RQ4/H4 (a),(b); the "strongest existing pipeline" of §7/§9 is uniform capture + domain randomization +
random real-data selection, RialTo-style). No references added or renumbered. Trimmed to keep 2 pages. -->
<!--
Wave 13 (issue #29), 2026-09-26: generalized for pivot decision v3 (research/pivot-decision.md: general,
task- and domain-agnostic real-to-sim-to-real; manipulation and navigation equal testbeds; the twin covers
appearance, geometry and physical/dynamic parameters). Navigation-centric framing removed ("in navigation"
gap, "real rollouts"); the gap now asks for the same budget measurement in both domains. System
identification added as the physical side of the twin and of "capture less". 35 refs (limit <= 35).
New refs, verified 2026-09-26 on the arXiv abstract pages (OpenAlex and Semantic Scholar returned 429):
- [9] BayesSim, arXiv:1906.01728 (Ramos, Possas, Fox); arXiv journal-ref "Robotics Science and Systems
  (RSS) 2019"; abstract: "full Bayesian treatment for the parameters of the simulator", trajectories from
  a physical robot, likelihood-free inference.
- [10] PhysTwin, arXiv:2503.17973 (H. Jiang, Hsu, K. Zhang, Yu, S. Wang, ...); ICCV 2025 open-access page
  (openaccess.thecvf.com/ICCV2025) lists it. Abstract: "sparse videos of dynamic objects under
  interaction", "reconstructs complete geometry, infers dense physical properties, and replicates realistic
  appearance".
- [21] ASID, arXiv:2404.12308 (Memmel, Wagenmaker, Zhu, Yin, Fox, ...). Abstract: "leverage a small amount
  of real-world data to autonomously refine a simulation model", "identifying articulation, mass, and other
  physical parameters". Venue not confirmed (dblp/OpenReview lists CoRR only), so cited as arXiv.
Dropped to stay <= 35 (not used in §9/§12): Kadian et al. "Sim2Real Predictivity" (navigation-specific),
Lei et al. mechanistic co-training analysis, CUPID, DataMIL.
Old -> new numbers: 1->1, 2->2, 3->5, 4->6, 5->7, 6->3, 7->4, 8->8, 9->11, 10->12, 11->13, 12->14,
13->15, 14 dropped, 15->16, 16->17, 17->18, 18->19, 19->20, 20->22, 21->23, 22->24, 23->25, 24->26,
25 dropped, 26->27, 27->28, 28->29, 29->30, 30->31, 31/32 dropped, 33->32, 34->33, 35->34, 36->35.
§9 and §12 renumbered in the same wave. Reference entries below the Wave 13 line use the OLD numbers.
"We found no study ... across domains" rests on crowdedness.md 4.2 and the S2 counts below, not on a full
survey: supervisor to confirm.
-->
<!--
Wave 11 (issue #26), 2026-09-26: rewritten for pivot decision v2 (research/pivot-decision.md, binding:
data-efficient real-to-sim-to-real; no benchmark building; representations and uncertainty are tools).
Structure: twins exist -> how much real data (budget studies) -> RQ1 capture less (active reconstruction,
uncertainty) -> RQ2 train robustly (DR, SimOpt, DA, co-training) -> RQ3 few real rollouts (active data
collection, attribution, PPI, twin correction) -> gap mapped to RQ1-RQ4. 35 refs (limit <= 35).
Old numbers -> new (refs kept from wave 9-10, verified then): 1->1 Habitat, 3->2 3DGS, 4->3 EmbodiedSplat,
5->4 Vid2Sim, 6->5 GaussGym, 7->6 RialTo, 8->7 SplatSim, 9->8 ManiSkill3, 10->14 Kadian, 11->15 Truong,
12->34 SIMPLER, 14->13 Maddukuri, 15->23 Cheng, 16->24 Lei, 17->19 ScanNet++, 20->25 DINOv2, 32->30 CUPID,
33->32 PPI, 34->33 SureSim. Tobin [20], Peng [21], Chebotar [22] from the Wave 1-6 list
(research/references-check.md: IROS 2017 doi:10.1109/IROS.2017.8202133, ICRA 2018
doi:10.1109/ICRA.2018.8460528, ICRA 2019 doi:10.1109/ICRA.2019.8793789); Chebotar abstract re-read today
on S2 ("adapt the simulation parameter distribution using a few real world roll-outs").
Dropped (representation-thesis only): linear probes, CKA, V-JEPA 2, Don't Blind Your VLA, OOD-performance
estimation, weights-only accuracy prediction, model zoos, Navon, Kofinas, conformal, FAIL-Detect, SAFE,
TRAK, WorldEval.
New refs, verified 2026-09-26 on the Semantic Scholar batch API (title, authors, year, venue, abstract);
arXiv API returned nothing (429):
- [9] Lin et al. arXiv:2410.18647, ICLR 2025 (S2 venue ICLR; crowdedness.md 4.1).
- [10] Suomela et al. arXiv:2601.09444, doi:10.1109/LRA.2026.3677718, RA-L 11, pp. 6114-6121. Abstract:
  "data diversity is far more important than data quantity"; benefit from existing locations "saturates
  with very little data".
- [11] CASHER arXiv:2412.01770 (Torne, Jain, Yuan, ...); abstract "performance scales superlinearly with
  human effort". S2 venue label "Robotics" (unconfirmed), cited as arXiv.
- [12] X-Sim arXiv:2505.07096 (Dan, Kedia, Chao, ...). "10x less data collection time" is from
  crowdedness.md (abstract tail, read in wave 8).
- [13] "38% on average": crowdedness.md 4.1 from the arXiv:2503.24361 abstract ("an average of 38%").
- [16] FisherRF arXiv:2311.17874 (Jiang, Lei, Daniilidis); Crossref doi:10.1007/978-3-031-72624-8_24,
  Computer Vision - ECCV 2024 (LNCS). "Expected Information Gain" from the abstract.
- [17] GenNBV arXiv:2402.16174, doi:10.1109/CVPR52733.2024.01555 (CVPR 2024).
- [18] Bayes' Rays arXiv:2309.03185, doi:10.1109/CVPR52733.2024.01896 (CVPR 2024), "volumetric
  uncertainty field ... any pre-trained NeRF" (abstract).
- [26] Phys2Real arXiv:2510.11689 (M. Wang, S. Tian, A. Swann, ...): uncertainty over physical parameters,
  training not evaluation (niches-eval.md N4).
- [27] MetaMVUC doi:10.1109/LRA.2025.3544083, RA-L 10, pp. 3644-3651 (Gilles, Furmans, Rayyes): "selecting
  the most informative real-world data samples" (abstract).
- [28] AMF arXiv:2410.05026 (Bagatella, Hubotter, Martius, ...); S2 venue "International Conference on
  Machine Learning". Year 2025 inferred (arXiv Oct 2024, after the ICML 2024 deadline): CONFIRM on the
  PMLR page before printing.
- [29] Anwar et al. arXiv:2502.09829 ("active testing", "cost-aware expected information gain", abstract).
- [31] DataMIL arXiv:2505.09603 (Dass, Khaddaj, Engstrom, ...).
- [35] GaussTwin arXiv:2603.05108 (Cai, Jansonnie, de Farias, ...): "visual correction" driven by
  photometric error (abstract); ICRA 2026 per arXiv comment (novelty-options.md), cited as arXiv.
Review-3 (issue #27), 2026-09-26: R3-F8 inserted [19] Liu, Jiang, Lei, Pandey, Daniilidis, Motee,
"Beyond Uncertainty: Risk-Aware Active View Acquisition for Safe Robot Navigation and 3D Scene
Understanding with FisherRF", arXiv:2403.11396 (arXiv abs page read 2026-09-26; OpenAlex W4392972342,
2024; no journal-ref, so cited as arXiv). It is the closest H1 competitor (niches-data.md N1 "closest
papers"). Old [19]-[35] -> [20]-[36]; §9 renumbered in the same way. R3-F16 GaussGym = "learning
locomotion from pixels" (S2 title/abstract), so "navigation and locomotion". R3-F17 S2 hit counts removed
from the visible text except "at most two ... per year". ScanNet++ wording from the arXiv:2308.11417
abstract. 36 refs.
Hit counts in the text (0-2, 0-1, one paper) are Semantic Scholar counts from research/niches-data.md
(N1 task-aware capture 2/2/0/2; N9 twin-sample weighting 0/0/1/0) and research/pivot-decision.md
(reconstruction uncertainty as training signal 0/0/1/1). "We found no study" rests on these counts and on
crowdedness.md 4.2 ("Nobody varies the capture budget ... as an experimental variable"), not on a full
survey: supervisor to confirm.
-->

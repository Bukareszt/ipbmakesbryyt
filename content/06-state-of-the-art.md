# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Real-to-sim-to-real with neural digital twins.** Simulators such as Habitat [1] made large-scale training
of embodied agents possible, but a generic simulator is not the robot's scene. 3D Gaussian Splatting (3DGS) [2] now turns a short camera capture into a real-time,
photorealistic *digital twin* of that scene. Policies trained in such twins transfer to real robots in
navigation (EmbodiedSplat [3], Vid2Sim [4], GaussGym [5]) and manipulation (RialTo [6], SplatSim [7]), and
GPU simulators ship twin environments (ManiSkill3 [8]). Building a twin is no longer the bottleneck; **real
data** is: the capture that builds the twin and the real rollouts that correct the policy. Current systems
fix this cost by hand. EmbodiedSplat uses a 20–30-minute phone capture
per scene, and RialTo builds its twins from "small amounts of real-world data"; its ablation over 0–15 real
demonstrations is the closest published analysis of a real-data budget.

**How much real data does transfer need?** Real-only scaling studies relate performance to the number of real
demonstrations in manipulation [9]; in navigation, diversity matters more than quantity and more data from
a known location saturates quickly [10]. On the twin side, CASHER [11] reports
performance that scales super-linearly with human effort, X-Sim [12] matches behaviour cloning with ten
times less data-collection time, and sim-and-real co-training raises real success by 38% on average [13].
Simulation can poorly predict real navigation results (Sim-vs-Real Correlation Coefficient,
SRCC [14]), and lower-fidelity simulation can transfer better [15], so more capture is not automatically
better. All of these report results at fixed or hand-chosen budgets. **We found no
study that varies the capture budget of a twin as an experimental variable in navigation, or that fits
real-data budget curves for the whole loop against real-only learning.**

**Capturing less: active reconstruction and its uncertainty.** Active view selection chooses the images
that improve a reconstruction most: FisherRF [16] maximizes the expected information gain on
radiance-field parameters, GenNBV [17] learns a next-best-view policy that generalizes across scenes, and
Bayes' Rays [18] estimates a volumetric uncertainty field for a trained neural radiance field. Their
objective is reconstruction quality or coverage, not what a downstream policy needs; task-aware capture
for twins has only 0–2 Semantic Scholar hits per year (2023–2026). ScanNet++ [19] pairs real captures of rooms
with reference laser scans, so capture budgets can be varied offline.

**Training robustly on an imperfect twin.** Domain randomization varies appearance [20] or dynamics [21]
uniformly within hand-set ranges, and SimOpt [22] adapts the randomization distribution from a few real
rollouts. Domain adaptation aligns sim and real features in co-training [23], and a mechanistic analysis
finds that representation alignment is the main effect of co-training [24]. Frozen encoders such as DINOv2
[25] allow twin and real frames to be compared, and Phys2Real [26] trains with uncertainty over physical
parameters. Still, a twin's own **reconstruction
uncertainty** is rarely used as a training signal (0–1 hits per year), and weighting twin samples by their
representation distance to a small real set appeared in one paper in 2023–2026.

**Collecting few real rollouts.** Active learning selects the most informative real samples for sim-to-real
adaptation in grasping [27], AMF [28] chooses which tasks to demonstrate under a demonstration budget, and
active experiment selection reduces the cost of real evaluation [29]. CUPID [30] and DataMIL [31] select
training data by its influence on closed-loop success. Prediction-powered inference [32] combines many
cheap predictions with a few labels, SureSim [33] applies it to simulated and real trials, and SIMPLER
[34] shows that simulated evaluation of manipulation policies can track real evaluation. GaussTwin [35]
corrects a 3DGS twin from photometric error. These methods select demonstrations, tasks or trials; none selects
the real rollouts that should correct a reconstructed twin and its policy.

**Research gap.** Real-to-sim-to-real works, but its real-data cost is set by hand and spent uniformly.
Missing are (i) task-aware, uncertainty-guided capture
judged by downstream policy success rather than image quality (RQ1), (ii) training that uses the twin's
reconstruction uncertainty and its representation distance to a small real set (RQ2), (iii) active
selection of the few real rollouts that correct the twin and the policy (RQ3), and (iv) a total real-data
budget curve of the full loop against real-only learning, in navigation and manipulation (RQ4). This
dissertation addresses that gap.

### References
[1] M. Savva et al., "Habitat," ICCV, 2019.
[2] B. Kerbl et al., "3D Gaussian Splatting," ACM TOG, 2023.
[3] G. Chhablani et al., "EmbodiedSplat," ICCV, 2025.
[4] Z. Xie et al., "Vid2Sim," CVPR, 2025.
[5] A. Escontrela et al., "GaussGym," arXiv:2510.15352, 2025.
[6] M. Torne et al., "Reconciling Reality through Simulation," RSS, 2024.
[7] M. N. Qureshi et al., "SplatSim," ICRA, 2025.
[8] S. Tao et al., "ManiSkill3," RSS, 2025.
[9] F. Lin et al., "Data Scaling Laws in Imitation Learning…," ICLR, 2025.
[10] L. Suomela et al., "Data Scaling for Navigation…," IEEE RA-L, 2026.
[11] M. Torne et al., "Robot Learning with Super-Linear Scaling," arXiv:2412.01770, 2024.
[12] P. Dan et al., "X-Sim," arXiv:2505.07096, 2025.
[13] A. Maddukuri et al., "Sim-and-Real Co-Training," RSS, 2025.
[14] A. Kadian et al., "Sim2Real Predictivity," IEEE RA-L, 2020.
[15] J. Truong et al., "Rethinking Sim2Real," CoRL, 2022.
[16] W. Jiang et al., "FisherRF," ECCV, 2024.
[17] X. Chen et al., "GenNBV," CVPR, 2024.
[18] L. Goli et al., "Bayes' Rays," CVPR, 2024.
[19] C. Yeshwanth et al., "ScanNet++," ICCV, 2023.
[20] J. Tobin et al., "Domain Randomization…," IROS, 2017.
[21] X. B. Peng et al., "Sim-to-Real Transfer… with Dynamics Randomization," ICRA, 2018.
[22] Y. Chebotar et al., "Closing the Sim-to-Real Loop," ICRA, 2019.
[23] S. Cheng et al., "Generalizable Domain Adaptation for Sim-and-Real…," NeurIPS, 2025.
[24] Y. Lei et al., "A Mechanistic Analysis of Sim-and-Real Co-Training…," arXiv:2604.13645, 2026.
[25] M. Oquab et al., "DINOv2," TMLR, 2024.
[26] M. Wang et al., "Phys2Real," arXiv:2510.11689, 2025.
[27] M. Gilles et al., "MetaMVUC," IEEE RA-L, 2025.
[28] M. Bagatella et al., "Active Fine-Tuning of Multi-Task Policies," ICML, 2025.
[29] A. Anwar et al., "Efficient Evaluation of Multi-Task Robot Policies…," arXiv:2502.09829, 2025.
[30] C. Agia et al., "CUPID," arXiv:2506.19121, 2025.
[31] S. Dass et al., "DataMIL," arXiv:2505.09603, 2025.
[32] A. N. Angelopoulos et al., "Prediction-Powered Inference," Science, 2023.
[33] A. Badithela et al., "Reliable and Scalable Robot Policy Evaluation…," arXiv:2510.04354, 2025.
[34] X. Li et al., "Evaluating Real-World Robot Manipulation Policies…," CoRL, 2024.
[35] Y. Cai et al., "GaussTwin," arXiv:2603.05108, 2026.

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
Hit counts in the text (0-2, 0-1, one paper) are Semantic Scholar counts from research/niches-data.md
(N1 task-aware capture 2/2/0/2; N9 twin-sample weighting 0/0/1/0) and research/pivot-decision.md
(reconstruction uncertainty as training signal 0/0/1/1). "We found no study" rests on these counts and on
crowdedness.md 4.2 ("Nobody varies the capture budget ... as an experimental variable"), not on a full
survey: supervisor to confirm.
-->

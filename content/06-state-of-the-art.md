# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Real-to-sim-to-real with digital twins.** A real-to-sim-to-real loop builds a simulation of the target
scene or object (a *digital twin*) from real data, learns a policy or model in it and transfers it back.
Generic simulators such as Habitat [1] train at scale, but not in the target scene. 3D Gaussian Splatting
(3DGS) [2] turns a short camera capture into a real-time, photorealistic twin of geometry and appearance,
and policies trained in such twins transfer in manipulation (RialTo [3], SplatSim [4]) and in navigation
and locomotion (EmbodiedSplat [5], Vid2Sim [6], GaussGym [7]); GPU simulators ship twin environments
(ManiSkill3 [8]). The physical side is identified from real data: BayesSim [9] infers a posterior over
simulator parameters from real trajectories, and PhysTwin [10] recovers the geometry, physical properties
and appearance of deformable objects from sparse videos. Building a twin is no longer the bottleneck;
**real data** is: the capture that builds the twin and the real-world data or interactions that correct
it and the policy. Current systems fix this cost by hand: EmbodiedSplat uses a 20–30-minute phone capture
per scene, and RialTo's ablation over 0–15 real demonstrations is the closest published analysis of a
real-data budget.

**How much real data does transfer need?** Real-only scaling studies relate performance to the number of
real demonstrations in manipulation [11]; in navigation, diversity matters more than quantity and more
data from a known location saturates quickly [12]. On the twin side, CASHER [13] reports performance that
scales super-linearly with human effort, X-Sim [14] matches behaviour cloning with ten times less
data-collection time, and sim-and-real co-training raises real success by 38% on average [15].
Lower-fidelity simulation can transfer better [16], so more capture is not automatically better. All of
these report results at fixed or hand-chosen budgets in one domain. **We found no study that varies the
real-data budget of a twin as an experimental variable, or that fits real-data budget curves of the whole
loop against real-only learning across domains.**

**Capturing less: active reconstruction and active identification.** Active view selection chooses the
images that improve a reconstruction most: FisherRF [17] maximizes the expected information gain on
radiance-field parameters, GenNBV [18] learns a next-best-view policy that generalizes across scenes, and
Bayes' Rays [19] estimates a volumetric uncertainty field for a trained neural radiance field. Risk-aware
view acquisition [20] weights FisherRF by safety-critical regions during exploration. For physical
parameters, ASID [21] uses an initial simulator to design exploration that collects a small amount of
informative real data for identifying articulation, mass and other parameters. Their objective is
reconstruction quality, safe exploration or parameter accuracy, not the success of a policy trained in the
twin; we found at most two task-aware capture papers a year in 2023–2026. Public data allow budgets to be
varied offline: ScanNet++ [22] pairs laser scans with DSLR images and a separate phone stream.

**Learning robustly in an imperfect twin.** Domain randomization varies appearance [23] or dynamics [24]
uniformly within hand-set ranges, and SimOpt [25] adapts the randomization distribution from a few real
rollouts. Domain adaptation aligns sim and real features in co-training [26]. Frozen encoders (DINOv2
[27]) make twin and real samples comparable, and Phys2Real [28] trains with uncertainty over physical
parameters. Still, a twin's own **reconstruction uncertainty** is rarely used as a training signal, and
weighting twin samples by representation distance to a small real set appeared in one paper in 2023–2026.

**Collecting few real data.** Active learning selects the most informative real samples for sim-to-real
adaptation in grasping [29], AMF [30] chooses which tasks to demonstrate under a budget, and active
experiment selection reduces the cost of real evaluation [31]. Prediction-powered inference [32] combines
many cheap predictions with a few labels, SureSim [33] applies it to simulated and real trials, and
SIMPLER [34] shows, on paired simulated and real evaluations, that simulation can track real performance
of manipulation policies. GaussTwin [35] corrects a 3DGS twin from photometric error. They select
demonstrations, tasks or trials, not the real data that should correct a twin and its policy.

**Research gap.** Real-to-sim-to-real works, but its real-data cost is set by hand and spent uniformly,
and measured in one domain per study. Missing is one method that allocates it actively at every step:
(i) task-aware, uncertainty-guided capture of both
appearance and physical parameters, judged by task success, not reconstruction or parameter
accuracy (RQ1), (ii) learning driven by the twin's uncertainty and by representation distance to a small
real set (RQ2), (iii) active selection of the few real data that correct twin and policy (RQ3),
and (iv) evidence that it needs less real data than real-only learning and uniform
pipelines, measured the same way in manipulation and navigation (RQ4).

### References
[1] M. Savva et al., "Habitat," ICCV, 2019.
[2] B. Kerbl et al., "3D Gaussian Splatting," ACM TOG, 2023.
[3] M. Torne et al., "Reconciling Reality through Simulation," RSS, 2024.
[4] M. N. Qureshi et al., "SplatSim," ICRA, 2025.
[5] G. Chhablani et al., "EmbodiedSplat," ICCV, 2025.
[6] Z. Xie et al., "Vid2Sim," CVPR, 2025.
[7] A. Escontrela et al., "GaussGym," arXiv:2510.15352, 2025.
[8] S. Tao et al., "ManiSkill3," RSS, 2025.
[9] F. Ramos et al., "BayesSim," RSS, 2019.
[10] H. Jiang et al., "PhysTwin," ICCV, 2025.
[11] F. Lin et al., "Data Scaling Laws in Imitation Learning…," ICLR, 2025.
[12] L. Suomela et al., "Data Scaling for Navigation…," IEEE RA-L, 2026.
[13] M. Torne et al., "Robot Learning with Super-Linear Scaling," arXiv:2412.01770, 2024.
[14] P. Dan et al., "X-Sim," arXiv:2505.07096, 2025.
[15] A. Maddukuri et al., "Sim-and-Real Co-Training," RSS, 2025.
[16] J. Truong et al., "Rethinking Sim2Real," CoRL, 2022.
[17] W. Jiang et al., "FisherRF," ECCV, 2024.
[18] X. Chen et al., "GenNBV," CVPR, 2024.
[19] L. Goli et al., "Bayes' Rays," CVPR, 2024.
[20] G. Liu et al., "Risk-Aware Active View Acquisition…," arXiv:2403.11396, 2024.
[21] M. Memmel et al., "ASID," arXiv:2404.12308, 2024.
[22] C. Yeshwanth et al., "ScanNet++," ICCV, 2023.
[23] J. Tobin et al., "Domain Randomization…," IROS, 2017.
[24] X. B. Peng et al., "Sim-to-Real Transfer… with Dynamics Randomization," ICRA, 2018.
[25] Y. Chebotar et al., "Closing the Sim-to-Real Loop," ICRA, 2019.
[26] S. Cheng et al., "Generalizable Domain Adaptation for Sim-and-Real…," NeurIPS, 2025.
[27] M. Oquab et al., "DINOv2," TMLR, 2024.
[28] M. Wang et al., "Phys2Real," arXiv:2510.11689, 2025.
[29] M. Gilles et al., "MetaMVUC," IEEE RA-L, 2025.
[30] M. Bagatella et al., "Active Fine-Tuning of Multi-Task Policies," ICML, 2025.
[31] A. Anwar et al., "Efficient Evaluation of Multi-Task Robot Policies…," arXiv:2502.09829, 2025.
[32] A. N. Angelopoulos et al., "Prediction-Powered Inference," Science, 2023.
[33] A. Badithela et al., "Reliable and Scalable Robot Policy Evaluation…," arXiv:2510.04354, 2025.
[34] X. Li et al., "Evaluating Real-World Robot Manipulation Policies…," CoRL, 2024.
[35] Y. Cai et al., "GaussTwin," arXiv:2603.05108, 2026.

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

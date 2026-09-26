# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Simulation and sim-to-real transfer.** Robot models for navigation and manipulation are commonly trained
in simulators such as Habitat [1] and ManiSkill3 [2], where large-scale reinforcement learning essentially
solves point-goal navigation after billions of steps [3]. Transfer to the real world is the open part:
simulation success need not predict real success (the Sim-vs-Real Correlation Coefficient rose from 0.18 to 0.84 once one collision artefact was removed [4]; paired evaluations in manipulation [5]). Domain randomization varies appearance [6] or dynamics [7] uniformly within hand-set
ranges, and a few real rollouts can adapt the simulation parameter distribution [8]. In navigation,
more data from a known location saturates quickly [9]; sim-and-real co-training raises real success [10].

**From real data to digital twins.** Neural scene reconstruction, above all 3D Gaussian Splatting (3DGS)
[11], turns a short real capture into a photorealistic model of a scene. Twins built this way train models
that transfer. In navigation, EmbodiedSplat [12] reconstructs rooms from a phone capture and fine-tunes
image-goal navigation in Habitat, Vid2Sim [13] builds simulators for urban navigation from monocular
video, GaussGym [14] trains from pixels, and ReaDy-Go [15] adds moving obstacles.
In manipulation, RialTo [16] builds a twin from a scan and a few demonstrations, X-Sim [17] from a minute
of human video, and TwinRL [18] fine-tunes a pretrained policy in a phone-captured twin and targets its
few real rollouts at configurations where the twin predicts failure. The physical part of a twin can be identified from a small amount of real data, as a
posterior over simulator parameters [19] or by exploration designed for identification [20]. Datasets such
as ScanNet++ [21] pair laser scans and DSLR images with a separate phone capture of the same scene, and
MuSHRoom [22] pairs phone and depth-camera captures with a reference mesh under an open licence. In all
these works the amount of real data is fixed by hand: the navigation twins use between 15 seconds and 30
minutes of video per scene and no real training trials, and the manipulation works report single points
(e.g. a scan and 15 demonstrations instead of 50 demonstrations [16]) rather than curves.

**Capturing the right real data.** Active view selection chooses the images that improve a reconstruction
most: FisherRF [23] maximizes expected information gain, and Bayes' Rays [24] estimates an uncertainty
field for a trained radiance field. Risk-aware view acquisition [25] weights FisherRF by safety-critical
regions for navigation, and AREA3D [26] adds vision-language guidance. None measures the success of a model trained in the resulting twin (at most two task-aware capture papers a year, 2023–2026).

**Foundation models, world models and real trials.** Pretrained navigation foundation models generalize
across robots and environments (GNM [27], ViNT [28]), and vision-language-action models map images and
instructions to actions [29]; they still need data from the target place to work there. Learned world
models predict future observations: navigation world models plan by imagining trajectories [30], and open
world foundation models are post-trained per setup [31]; VLAW [32] improves a world model with real
rollouts, at a fixed, hand-chosen number of them. Choosing real trials has been studied for *evaluating*
policies (a fifth to a quarter less robot effort [33]), not for *correcting* a twin and its model.
Frozen visual encoders [34] make twin and real observations comparable, and prediction-powered inference
[35] estimates real performance from many cheap predictions and a few real labels.

**Theory.** Domain-adaptation theory bounds target error by source error plus a discrepancy between domains
[38], and Bayesian experimental design chooses measurements by expected information gain [36, 37]; neither
has been applied to the allocation of real data across a real-to-sim-to-real loop.

**Research gap.** Real-to-sim-to-real learning works, but the real data it consumes is set by hand and
spent uniformly at every step. No navigation pipeline has a stage that corrects the twin with real trials,
and none reports how success depends on the real data spent; in manipulation the real data is accounted
at single points, against learning from real data only, never against another real-to-sim-to-real
pipeline. Missing are a principled criterion for spending real data across the whole loop, its theory, and
a method built on it that reduces real data at every step (RQ1–RQ3) and in total (RQ4).

### References
[1] M. Savva et al., "Habitat," ICCV, 2019.
[2] S. Tao et al., "ManiSkill3," RSS, 2025.
[3] E. Wijmans et al., "DD-PPO," ICLR, 2020.
[4] A. Kadian et al., "Sim2Real Predictivity," IEEE RA-L, 2020.
[5] X. Li et al., "Evaluating Real-World Robot Manipulation Policies…," CoRL, 2024.
[6] J. Tobin et al., "Domain Randomization…," IROS, 2017.
[7] X. B. Peng et al., "Sim-to-Real Transfer… with Dynamics Randomization," ICRA, 2018.
[8] Y. Chebotar et al., "Closing the Sim-to-Real Loop," ICRA, 2019.
[9] L. Suomela et al., "Data Scaling for Navigation…," IEEE RA-L, 2026.
[10] A. Maddukuri et al., "Sim-and-Real Co-Training," RSS, 2025.
[11] B. Kerbl et al., "3D Gaussian Splatting," ACM TOG, 2023.
[12] G. Chhablani et al., "EmbodiedSplat," ICCV, 2025.
[13] Z. Xie et al., "Vid2Sim," CVPR, 2025.
[14] A. Escontrela et al., "GaussGym," arXiv:2510.15352, 2025.
[15] S. Yoo et al., "ReaDy-Go," IEEE RA-L, 2026.
[16] M. Torne et al., "Reconciling Reality through Simulation," RSS, 2024.
[17] P. Dan et al., "X-Sim," arXiv:2505.07096, 2025.
[18] Q. Xu et al., "TwinRL," arXiv:2602.09023, 2026.
[19] F. Ramos et al., "BayesSim," RSS, 2019.
[20] M. Memmel et al., "ASID," arXiv:2404.12308, 2024.
[21] C. Yeshwanth et al., "ScanNet++," ICCV, 2023.
[22] X. Ren et al., "MuSHRoom," arXiv:2311.02778, 2023.
[23] W. Jiang et al., "FisherRF," ECCV, 2024.
[24] L. Goli et al., "Bayes' Rays," CVPR, 2024.
[25] G. Liu et al., "Risk-Aware Active View Acquisition…," arXiv:2403.11396, 2024.
[26] T. Xu et al., "AREA3D," arXiv:2512.05131, 2025.
[27] D. Shah et al., "GNM," ICRA, 2023.
[28] D. Shah et al., "ViNT," CoRL, 2023.
[29] M. J. Kim et al., "OpenVLA," CoRL, 2024.
[30] A. Bar et al., "Navigation World Models," CVPR, 2025.
[31] N. Agarwal et al., "Cosmos World Foundation Model Platform…," arXiv:2501.03575, 2025.
[32] Y. Guo et al., "VLAW," arXiv:2602.12063, 2026.
[33] A. Badithela et al., "Reliable and Scalable Robot Policy Evaluation…," arXiv:2510.04354, 2025.
[34] M. Oquab et al., "DINOv2," TMLR, 2024.
[35] A. N. Angelopoulos et al., "Prediction-Powered Inference," Science, 2023.
[36] K. Chaloner, I. Verdinelli, "Bayesian Experimental Design: A Review," Statistical Science, 1995.
[37] T. Rainforth et al., "Modern Bayesian Experimental Design," Statistical Science, 2024.
[38] S. Ben-David et al., "A theory of learning from different domains," Machine Learning, 2010.

<!-- Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top)
and the deep-research report (reports/Uczenie nawigacji w cyfrowych bliźniakach.md). General
real-to-sim-to-real (navigation main testbed, manipulation generalization test); the gap now says
explicitly, per the report's recommendation 1, that no navigation pipeline has a real-trial correction
stage or budget curves and that manipulation accounting is single points. 35 refs (limit <= 35).
Reused from the Wave 16 list (verified in earlier waves, see the comments below): all except Truong
(Rethinking Sim2Real) and NaVILA, dropped for space.
Reinstated from earlier waves (verified then; formatted entries copied from the Wave 6/11/13 lists):
- [2] ManiSkill3: Wave 6 comment, arXiv 2410.00425, Crossref doi:10.15607/RSS.2025.XXI.021.
- [5] SIMPLER: Wave 6 comment, arXiv 2405.05941, PMLR vol. 270 (CoRL 2024); "paired sim-and-real
  evaluations", "strong correlation" from the abstract -> "simulation can track real performance".
- [17] X-Sim: Wave 11 comment, arXiv:2505.07096 (Dan, Kedia, Chao, ...); re-read on the arXiv API
  2026-09-26 (title "X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real"). "a minute of human
  video" = the report's table ("1 min wideo człowieka").
- [20] ASID: Wave 13 comment, arXiv:2404.12308 (Memmel et al.); abstract "leverage a small amount of
  real-world data to autonomously refine a simulation model", "identifying articulation, mass, and other
  physical parameters" -> "exploration designed for identification".
- [33] SureSim: Wave 11 list [33] (Badithela et al., arXiv:2510.04354); "saves about a fifth to a quarter
  of the real-robot effort" = the report ("SureSim oszczędza 20–25% wysiłku sprzętowego").
New, from the report's sources (verified today on the arXiv API, export.arxiv.org, 2026-09-26):
- [15] ReaDy-Go arXiv:2602.11575 (S. Yoo, Y. Jang, D. Kim, Y. Han, S. Jung, H. J. Kim). The report noted
  a T-RO vs RA-L conflict; the arXiv comment now reads "Accepted by IEEE Robotics and Automation Letters
  (RA-L)" and the arXiv DOI is 10.1109/LRA.2026.3707355, so it is cited as IEEE RA-L, 2026 (v7
  correction settled). "adds moving obstacles" = title ("with Moving Obstacles").
- [22] MuSHRoom arXiv:2311.02778 (X. Ren, W. Wang, D. Cai, T. Tuominen, J. Kannala, E. Rahtu), title
  "MuSHRoom: Multi-Sensor Hybrid Room Dataset for Joint 3D Reconstruction and Novel View Synthesis".
  Venue not confirmed here, so cited as arXiv. "phone and depth-camera captures with a reference mesh
  under an open licence" = the report (iPhone + Kinect + reference mesh, CC-BY-4.0, Zenodo 13986996).
Other figures in the visible text, all from the report: SRCC 0.18 -> 0.844 after removing the
wall-sliding artefact (Kadian et al., arXiv:1912.06321); TwinRL "~20 min" on-robot interaction and
failure-prone configurations (arXiv:2602.09023 abstract, also Wave 15 comment); navigation twins
"15 s (Vid2Sim) to 20-30 min (EmbodiedSplat) of video, zero real training trials"; RialTo "scan + 15 demos
vs BC with 50 demos" (report table; the "0/5/10/15 demos" ablation is NOT cited, per v7). "at most two
task-aware capture papers a year" = niches-data.md N1 (2/2/0/2), unchanged.
Old (Wave 16) -> new numbers: 1->1, 2->3, 3->4, 5->6, 6->7, 7->8, 8->9, 9->10, 10->11, 11->12, 12->13,
13->14, 14->16, 15->19, 16->21, 17->23, 18->24, 19->25, 20->26, 21->27, 22->28, 23->29, 25->30, 26->31,
27->18, 28->32, 29->34, 30->35; 4 (Truong) and 24 (NaVILA) dropped. §9 and §12 renumbered in the same
wave. Reference numbers in the older comments below are pre-Wave-18.
-->
<!-- (history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
general description; navigation (indoor mobile robots) is the domain; pipeline real data -> twin ->
navigation models (extended with world models and foundation models) -> real. Manipulation-only works
dropped from the visible text except RialTo [14] (general real-to-sim-to-real loop) and Maddukuri [9]
(general sim-and-real co-training result, used in §12). 30 refs (was 35); no new references: every entry
was verified in an earlier wave (sources below), none was re-looked-up today.
Reused from the Wave 15 list: Habitat, 3DGS, RialTo, EmbodiedSplat, BayesSim, OpenVLA, NaVILA, Suomela,
Maddukuri, TwinRL, Cosmos, NWM, VLAW, FisherRF, Bayes' Rays, Liu et al. risk-aware, AREA3D, ScanNet++,
Tobin, Peng, DINOv2, PPI (verification in the Wave 15/13/11 comments below and in
research/vla-wm-crowdedness.md §2).
Reinstated from earlier waves (verification in research/references-check.md and the Wave 11 comment below):
- DD-PPO (Wijmans et al., ICLR 2020): references-check.md row 5, "Abstract confirms 2.5 billion steps and
  'essentially solves' PointGoal nav" -> "essentially solves point-goal navigation after billions of steps".
- Kadian et al., Sim2Real Predictivity, RA-L 2020, doi:10.1109/LRA.2020.3013848: row 12, metric name
  "Sim-vs-Real Correlation Coefficient (SRCC)" from the abstract.
- Truong et al., Rethinking Sim2Real, CoRL 2022: row 13, "lower fidelity transfers better for navigation".
- Chebotar et al., Closing the Sim-to-Real Loop, ICRA 2019, doi:10.1109/ICRA.2019.8793789: "adapt the
  simulation parameter distribution using a few real world roll-outs" (Wave 11 comment below).
- Vid2Sim (Xie et al., CVPR 2025, doi:10.1109/CVPR52734.2025.00155): row 30, "Monocular video ->
  interactive sim for urban navigation".
- GaussGym (Escontrela et al., arXiv:2510.15352): review-3 R3-F15, S2 title "learning locomotion from
  pixels" -> "navigation and locomotion".
- GNM (Shah et al., ICRA 2023, doi:10.1109/ICRA48891.2023.10161227) and ViNT (Shah et al., CoRL 2023,
  arXiv:2306.14846, "Accepted for oral presentation at CoRL 2023"): references-check.md rows 6-7 (Wave 1-2
  list). "generalize across robots and environments": arXiv API abstracts re-read 2026-09-26, GNM
  arXiv:2210.03370 ("broad generalization across environments and embodiments", comment "Presented at
  ICRA 2023"), ViNT ("a foundation model ... for mobile robotics", "hundreds of hours of robotic navigation
  from a variety of different robotic platforms").
- EmbodiedSplat wording (phone capture, GS meshes in Habitat, image-goal navigation fine-tuning) from the
  arXiv:2509.17430 abstract (review-3 evidence list).
- NWM "plan by imagining trajectories": research/world-models.md row NWM ("plans navigation by simulating
  trajectories (abstract)") and §167 ("plans by imagining trajectories").
Dropped from the Wave 15 list (VLA/manipulation detail removed by v6): pi0, LoRA, OFT, SimpleVLA-RL,
Liu et al. (RL for VLA), WMPO, GigaWorld-0, Qwen2.5-VL, Du et al., ASID, SplatSim, ManiSkill3, SIMPLER.
Old (Wave 15) -> new numbers: 1->1, 2->10, 3->14, 5->11, 7->15, 8->23, 10->24, 13->8, 14->9, 17->27,
18->26, 19->25, 21->28, 25->17, 26->18, 27->19, 29->20, 30->16, 31->5, 32->6, 33->29, 34->30.
"we found at most two task-aware capture papers a year" = niches-data.md N1 (2/2/0/2), unchanged.
Reference numbers in the older comments below are pre-Wave-16.
-->
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

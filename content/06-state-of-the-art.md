# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

Deep reinforcement and imitation learning made it possible to train robots for complex tasks such as
visual navigation and manipulation. Since such methods require very large amounts of experience,
simulation became the standard training environment. Platforms such as Habitat [1] and ManiSkill3 [2]
allow training at the scale of billions of steps, and in simulation point-goal navigation has been
practically solved [3]. However, the performance of models in simulation does not always predict their
performance in the real world [4], and the transfer of models from simulation to reality, known as the
sim-to-real problem, remains one of the central challenges of robot learning [5, 6].

The most common approach to the sim-to-real problem is domain randomization, which varies the appearance
[7] or the dynamics [8] of the simulation so that reality appears as one more variation. Other works adapt
the parameters of the simulator to a few real-world rollouts [9]. Interestingly, the fidelity of the
simulator alone does not guarantee better transfer, as lower-fidelity simulation can transfer better in
navigation [10]. From the machine learning perspective, the sim-to-real problem is an instance of learning
under distribution shift. Domain adaptation theory bounds the error on the target domain by the error on
the source domain and a discrepancy between the two domains [11], and domain-adversarial training learns
representations that are invariant across domains [12]. Nevertheless, such principled approaches are
rarely applied to models trained in simulation for physical tasks, where randomization heuristics dominate.

A major recent development is the construction of simulations directly from real data. Neural Radiance
Fields [13] and 3D Gaussian Splatting [14] reconstruct photorealistic 3D scenes from ordinary images, and
datasets such as ScanNet++ [15] provide real indoor scenes captured both with high-end and consumer
devices. Such digital twins have been used to train navigation models from a phone capture of a room [16]
or from monocular videos of urban scenes [17], and robotic manipulation policies from a scan of the target
scene [18], showing that real-to-sim-to-real learning improves real-world performance in comparison with
generic simulators. The physical parameters of a digital twin can be estimated from a small amount of
real data [19]. However, these works treat the digital twin mostly as a fixed, as-accurate-as-possible copy
of reality. It is not known which properties of a twin (appearance, geometry, lighting or physics) actually
determine the generalization of the trained models, and the twins are randomized uniformly rather than
according to where they are uncertain or where it matters for the task. Moreover, the evaluation is
usually limited to a handful of scenes and a single task.

In parallel, pretrained foundation models changed how robot policies are built. General navigation models
trained on data from many robots [20, 21] and vision-language-action models [22] transfer to new robots
and environments, and self-supervised visual encoders [23] provide representations that are robust to
many appearance changes. Learned world models predict future observations and can be used for planning
in navigation [24]. These models are a promising basis for generalization, but it has not been studied
how their representations behave under the specific shift between a digital twin and reality, and how
they should be trained in a twin so that this shift does not harm their performance. Finally, adapting
a model trained in simulation to reality usually relies on real data collected at random or by hand, and
on co-training with simulated data [25], without selecting the real data that is most informative about
the remaining gap.

In summary, the literature shows that real-to-sim-to-real learning is effective, but the generalization
of the trained models to reality, to unseen scenes and to other tasks is still limited and poorly
understood. The proposed dissertation addresses this gap by studying the generalization of deep learning
models at each stage of the real-to-sim-to-real loop.

### References
[1] Savva, M., Kadian, A., Maksymets, O., et al. (2019). Habitat: A platform for embodied AI research. ICCV.
[2] Tao, S., et al. (2025). ManiSkill3: GPU parallelized robotics simulation and rendering for generalizable embodied AI. RSS.
[3] Wijmans, E., et al. (2020). DD-PPO: Learning near-perfect PointGoal navigators from 2.5 billion frames. ICLR.
[4] Kadian, A., et al. (2020). Sim2Real predictivity: Does evaluation in simulation predict real-world performance? IEEE Robotics and Automation Letters, 5(4).
[5] Zhao, W., Queralta, J. P., & Westerlund, T. (2020). Sim-to-real transfer in deep reinforcement learning for robotics: a survey. IEEE SSCI.
[6] Höfer, S., et al. (2021). Sim2Real in robotics and automation: Applications and challenges. IEEE Transactions on Automation Science and Engineering, 18(2).
[7] Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. IROS.
[8] Peng, X. B., Andrychowicz, M., Zaremba, W., & Abbeel, P. (2018). Sim-to-real transfer of robotic control with dynamics randomization. ICRA.
[9] Chebotar, Y., et al. (2019). Closing the sim-to-real loop: Adapting simulation randomization with real world experience. ICRA.
[10] Truong, J., et al. (2022). Rethinking sim2real: Lower fidelity simulation leads to higher sim2real transfer in navigation. CoRL.
[11] Ben-David, S., et al. (2010). A theory of learning from different domains. Machine Learning, 79.
[12] Ganin, Y., et al. (2016). Domain-adversarial training of neural networks. Journal of Machine Learning Research, 17.
[13] Mildenhall, B., et al. (2020). NeRF: Representing scenes as neural radiance fields for view synthesis. ECCV.
[14] Kerbl, B., Kopanas, G., Leimkühler, T., & Drettakis, G. (2023). 3D Gaussian splatting for real-time radiance field rendering. ACM Transactions on Graphics, 42(4).
[15] Yeshwanth, C., Liu, Y.-C., Nießner, M., & Dai, A. (2023). ScanNet++: A high-fidelity dataset of 3D indoor scenes. ICCV.
[16] Chhablani, G., et al. (2025). EmbodiedSplat. ICCV. arXiv:2509.17430.
[17] Xie, Z., et al. (2025). Vid2Sim: Realistic and interactive simulation from video for urban navigation. CVPR.
[18] Torne, M., et al. (2024). Reconciling reality through simulation: A real-to-sim-to-real approach for robust manipulation. RSS.
[19] Ramos, F., Possas, R., & Fox, D. (2019). BayesSim: Adaptive domain randomization via probabilistic inference for robotics simulators. RSS.
[20] Shah, D., et al. (2023). GNM: A general navigation model to drive any robot. ICRA.
[21] Shah, D., et al. (2023). ViNT: A foundation model for visual navigation. CoRL.
[22] Kim, M. J., et al. (2024). OpenVLA: An open-source vision-language-action model. CoRL.
[23] Oquab, M., et al. (2024). DINOv2: Learning robust visual features without supervision. TMLR.
[24] Bar, A., et al. (2025). Navigation world models. CVPR.
[25] Maddukuri, A., et al. (2025). Sim-and-real co-training: A simple recipe for vision-based robotic manipulation. RSS.

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

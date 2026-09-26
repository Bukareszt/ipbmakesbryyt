# §6 Zarys aktualnego stanu badań / State of the art (max 2 pages)

**Digital twins have become a commodity.** Photorealistic simulators such as Habitat [1] and domain randomization [2]
made large-scale training of embodied agents possible. 3D Gaussian Splatting (3DGS) [3] now turns a short phone or camera capture into a real-time, photorealistic
*digital twin*. Twin-trained policies transfer to real robots in navigation (EmbodiedSplat [4], Vid2Sim [5],
GaussGym [6]) and manipulation (RialTo [7], SplatSim [8]), and GPU simulators ship twin environments
(ManiSkill3 [9]). Building twins is therefore no longer the bottleneck. The open question is **when a
twin-trained policy will work in reality, and why**.

**Predicting real performance from simulation.** Kadian et al. [10] introduced the Sim-vs-Real Correlation
Coefficient (SRCC) and showed that simulation can poorly predict real navigation results. Truong et al. [11]
found that lower-fidelity simulation can transfer better, so image fidelity is not the same as transfer.
SIMPLER [12] reports strong sim-real correlation for manipulation evaluation, and pretrained visual
representations rank similarly in simulation and reality [13]. All of these measure transfer at the level of
*simulators* and success rates, after deployment.

**The representation gap.** Sim-and-real co-training works with few real demonstrations [14], domain
adaptation aligns sim and real features [15], and a mechanistic analysis finds that "structured
representation alignment" is the primary effect of co-training [16]. ScanNet++ [17] pairs real captures of rooms
with reference scans. Linear
probes [18] and centered kernel alignment (CKA) [19] measure what each layer encodes and how similar two
representations are. Frozen image and video encoders (DINOv2 [20], V-JEPA 2 [21]) are common policy
backbones, and probing of vision-language-action models shows that action fine-tuning degrades their visual
representations [22]. However, **we found no study that measured, on paired real and twin-rendered frames of the same
pose, where inside encoders and policies the twin-vs-real gap arises, or how it shrinks with the capture
budget.**

**Predicting performance from model internals.** Accuracy under distribution shift can be estimated from
unlabeled target data [23]. A network's accuracy can be predicted from its weights alone [24], and
populations of trained models ("model zoos" [25]) are now inputs to weight-space learning: equivariant
metanetworks [26] learn directly on weights, and graph neural networks over the computational graph [27]
predict generalization.
They have been tested on image classifiers and implicit neural representations, **not on embodied
policies or twin-to-real transfer**.

**Failure prediction and calibrated monitoring.** Conformal prediction [28] gives distribution-free
guarantees. FAIL-Detect [29] detects failures of imitation policies without failure data and calibrates
thresholds with conformal prediction, and SAFE [30] finds that the features of vision-language-action models
encode task success and failure across tasks. These monitors are calibrated and tested in the *same* domain.
Whether a monitor calibrated in the twin keeps its coverage on real data has not been studied.

**Spending a small real-data budget.** Data attribution estimates how training examples affect predictions
[31], and CUPID [32] ranks robot demonstrations by their influence on closed-loop success.
Prediction-powered inference [33] combines many cheap predictions with a few labels, and SureSim [34] uses it
to correct simulated evaluation with a few paired real trials. Learned world models are also proposed as
policy evaluators [35]. These tools treat the policy as a black box; none
uses its internal representations to decide which twin data to weight, what to capture or which
real rollouts to collect.

**Research gap.** Twins are widely available, but there is **no representation-level account
of how twin-trained policies transfer to reality**. Missing are (i) a paired real/twin benchmark that localizes the
gap inside encoders and policies across capture budgets, (ii) predictors of real transfer and
failure from policy internals (weights, hidden states) that beat simulator-level and image-fidelity
baselines, (iii) methods that use such forecasts to spend a limited real-data budget, and (iv) evidence
that these measures carry over from navigation to manipulation. This dissertation addresses that gap.

### References
[1] M. Savva et al., "Habitat," ICCV, 2019.
[2] J. Tobin et al., "Domain Randomization for Transferring Deep Neural Networks…," IROS, 2017.
[3] B. Kerbl et al., "3D Gaussian Splatting," ACM TOG, 2023.
[4] G. Chhablani et al., "EmbodiedSplat," ICCV, 2025.
[5] Z. Xie et al., "Vid2Sim," CVPR, 2025.
[6] A. Escontrela et al., "GaussGym," arXiv:2510.15352, 2025.
[7] M. Torne et al., "Reconciling Reality through Simulation," RSS, 2024.
[8] M. N. Qureshi et al., "SplatSim," ICRA, 2025.
[9] S. Tao et al., "ManiSkill3," RSS, 2025.
[10] A. Kadian et al., "Sim2Real Predictivity," IEEE RA-L, 2020.
[11] J. Truong et al., "Rethinking Sim2Real," CoRL, 2022.
[12] X. Li et al., "Evaluating Real-World Robot Manipulation Policies…," CoRL, 2024.
[13] S. Silwal et al., "What Do We Learn from a Large-Scale Study of Pre-Trained Visual…," ICRA, 2024.
[14] A. Maddukuri et al., "Sim-and-Real Co-Training," RSS, 2025.
[15] S. Cheng et al., "Generalizable Domain Adaptation for Sim-and-Real…," NeurIPS, 2025.
[16] Y. Lei et al., "A Mechanistic Analysis of Sim-and-Real Co-Training…," arXiv:2604.13645, 2026.
[17] C. Yeshwanth et al., "ScanNet++," ICCV, 2023.
[18] G. Alain, Y. Bengio, "Understanding Intermediate Layers Using Linear…," arXiv:1610.01644, 2016.
[19] S. Kornblith et al., "Similarity of Neural Network Representations…," ICML, 2019.
[20] M. Oquab et al., "DINOv2," TMLR, 2024.
[21] M. Assran et al., "V-JEPA 2," arXiv:2506.09985, 2025.
[22] N. Kachaev et al., "Don't Blind Your VLA," arXiv:2510.25616, 2025.
[23] S. Garg et al., "Leveraging Unlabeled Data to Predict OOD Performance," ICLR, 2022.
[24] T. Unterthiner et al., "Predicting Neural Network Accuracy…," arXiv:2002.11448, 2020.
[25] K. Schürholt et al., "Model Zoos," NeurIPS Datasets and Benchmarks, 2022.
[26] A. Navon et al., "Equivariant Architectures for Deep Weight Spaces," ICML, 2023.
[27] M. Kofinas et al., "Graph Neural Networks for Learning Equivariant…," ICLR, 2024.
[28] A. N. Angelopoulos, S. Bates, "A Gentle Introduction to Conformal…," arXiv:2107.07511, 2021.
[29] C. Xu et al., "Can We Detect Failures Without Failure Data?," RSS, 2025.
[30] Q. Gu et al., "SAFE," NeurIPS, 2025.
[31] S. M. Park et al., "TRAK," ICML, 2023.
[32] C. Agia et al., "CUPID," arXiv:2506.19121, 2025.
[33] A. N. Angelopoulos et al., "Prediction-Powered Inference," Science, 2023.
[34] A. Badithela et al., "Reliable and Scalable Robot Policy Evaluation…," arXiv:2510.04354, 2025.
[35] Y. Li et al., "WorldEval," arXiv:2505.19017, 2025.

<!--
Review-2 (issue #24), 2026-09-26: R2-F9 (a) [26] Navon et al. abstract (arXiv 2301.12780, re-read via the
arXiv API today) does not report generalization prediction, so the claim is now attached to [27] only
(Kofinas et al. abstract: "predicting generalization performance"). (b) "no study has measured" -> "we
found no study that measured" (the gap rests on S2 counts, not a full survey). Numbering unchanged; all
bracketed citations in §9 and §12 were checked against this list.
-->
<!--
Wave 9 (issue #23), 2026-09-26: rewritten for the pivot (research/pivot-decision.md): twins as a commodity
-> simulator-level predictivity -> representation gap and probing -> weight-space learning -> failure
prediction -> data attribution / prediction-powered evaluation / world models -> gap mapped to RQ1-RQ4.
35 refs. Robotics-only refs pruned: Habitat 2.0, CARLA, DD-PPO, GNM, ViNT, NoMaD, Open X-Embodiment,
Zhao/Höfer surveys, Tremblay, Peng, Loquercio, Kaufmann, Chebotar, Bousmalis, NeRF, NeRF2Real, drone and
legged 3DGS navigation papers (Quach, SOUS VIDE, GRaD-Nav, VR-Robo), ReaDy-Go, DANN, CyCADA, Kaplan, HM3D.
Old -> new numbers for refs kept: 1->1, 13->2, 21->3, 30->4, 28->5, 23->7, 36->8, 38->9, 11->10, 12->11,
37->12, 35->17. Other sections citing old numbers must be updated (05 cited [4], 07 [11], 08 [23][24][30]).
Long titles are cut with an ellipsis for the page limit (full titles below or via the arXiv IDs).
Verification, 2026-09-26, Semantic Scholar batch API (title, year, venue, first authors, DOI):
- [6] GaussGym arXiv 2510.15352 (Escontrela, Kerr, Allshire, Frey ...), arXiv only.
- [13] Silwal et al. arXiv 2310.02219, doi:10.1109/ICRA57147.2024.10610218 (ICRA 2024). Claim "PVR trends in
  simulation are generally indicative of real trends" from the abstract.
- [14] Maddukuri et al. arXiv 2503.24361, RSS 2025 (S2 venue "Robotics"; crowdedness.md). [15] Cheng et al.
  arXiv 2509.18631, NeurIPS 2025 (OT-inspired alignment of joint obs-action distributions, abstract).
- [16] Lei et al. arXiv 2604.13645: "structured representation alignment ... primary role" (abstract).
- [18] arXiv 1610.01644 (S2 lists ICLR; it was an ICLR 2017 workshop paper, so cited as arXiv).
- [19] arXiv 1905.00414, ICML 2019. [20] arXiv 2304.07193, TMLR. [21] arXiv 2506.09985, no venue found.
- [22] arXiv 2510.25616 (S2 venue AAMAS 2026 with doi:10.65109/PPER9186; cited as arXiv to be safe).
  "Naive action fine-tuning degrades visual representations", "we probe VLA's hidden representations" (abstract).
- [23] arXiv 2201.04234, ICLR 2022. [24] arXiv 2002.11448 (weights-only predictors, R2 > 0.98, 120k CNNs).
- [25] arXiv 2209.14764, NeurIPS 2022 (Datasets and Benchmarks track). [26] arXiv 2301.12780, ICML 2023.
  [27] arXiv 2403.12143, ICLR 2024 ("predicting generalization performance" in the abstract).
- [28] arXiv 2107.07511 (also in Foundations and Trends in ML; cited as arXiv).
- [29] FAIL-Detect arXiv 2503.08558, RSS 2025 (niches-eval.md; S2 venue "Robotics"); conformal thresholds and
  no failure data, from the abstract. [30] SAFE arXiv 2506.09937, NeurIPS 2025 (S2); feature-space claim from
  the abstract.
- [31] TRAK arXiv 2303.14186, ICML 2023. [32] CUPID arXiv 2506.19121 (influence on closed-loop return).
- [33] PPI arXiv 2301.09633, doi:10.1126/science.adi6000. [34] SureSim arXiv 2510.04354 (PPI with paired
  real/sim evaluations). [35] WorldEval arXiv 2505.19017 (world model as a proxy real-world evaluator).
- Kept refs were verified in earlier waves (see git history of this file); re-checked on S2 the same day.
"No study has measured ..." and "not on embodied policies" rest on the Semantic Scholar counts in
research/niches-map.md, niches-models.md and novelty-options.md (0-3 hits per year), not on a full survey:
supervisor to confirm.
-->

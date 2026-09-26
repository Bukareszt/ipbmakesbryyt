# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Modern machine learning is limited less by models than by **data in the target domain**. Embodied agents
(mobile robots, manipulators) learn strong behaviour only from very large amounts of experience. In the
real world such data is
slow, expensive and sometimes risky to collect, so a policy is usually trained in simulation and then
deployed on real sensor data, where it often fails (the **sim-to-real gap**).

**Digital twins built by neural scene reconstruction** (3D Gaussian Splatting, Neural Radiance Fields)
turn a few minutes of real video into a photorealistic, interactive model of the target scene, in which a
policy can be trained at scale. Building such twins has quickly become routine: dozens of papers a year
and more than ten open-source twin simulators. The open question has moved from *how to build a twin* to
*when a policy trained in it can be trusted in reality*. Today this is answered in two unsatisfying ways:
by running the policy in the real world (slow and costly, which is what the twin was meant to avoid) or by
image-quality scores of the reconstruction, which need not track real performance (lower-fidelity
simulation can even transfer better). Neither says
**where** the gap arises, and neither tells how to spend the few real observations one can afford.

**Why representations.** Whatever a policy does, it does through its internal representations: the
features its encoder and layers compute from an image. This is where reconstructed and real inputs either
meet or diverge. Machine learning now has mature tools to read representations: layer-wise probing,
representational similarity (e.g. centred kernel alignment), and learning on network weights
(metanetworks over model populations). They have been used to predict the accuracy and generalization of
image classifiers and other networks from their weights, but not the real-world transfer of policies trained in twins. The dissertation
asks whether this transfer can be **measured, localized and predicted from representations** without real
rollouts, and whether such forecasts let a small real-data budget be spent where it matters: which twin
data to weight, what to capture, and which real trials to run.

**Why this topic, and why in this discipline.** The object is a learning and evaluation methodology, not a
robot or a simulator, which places it in *information and communication technology* (representation
learning, learning under distribution shift, model analysis). The student uses existing twin pipelines and
simulators and does not develop new ones. **Visual navigation** is the primary testbed, because public
scene datasets with real captures allow controlled, reproducible measurement without an own robot;
**robotic manipulation** tests that the findings carry over to another task. Trials on a real robot
(planned cooperation with a PWr robotics laboratory) validate, but do not decide, the conclusions. The
topic fits the Department of Artificial Intelligence (K46), whose research groups include representation
learning on graphs and models in weight space. The computation runs on the GPU infrastructure available to
PWr researchers (WCSS, PLGrid). A benchmark of paired real and reconstructed data and a measured answer to
"which representations survive reconstruction" are useful whatever the hypotheses' outcome.

**Potential application areas:** faster and cheaper deployment of learned robots in new buildings and
workcells (service, assistive, warehouse and inspection robotics, flexible manipulation); pre-deployment
screening of candidate policies and safety monitors that flag likely failures; choosing which visual
foundation models to use in twin-based training; and, beyond robotics, any system trained on reconstructed
or synthetic data and deployed on real sensor data (industrial digital twins, perception for autonomous
systems).

<!--
Wave 9 (issue #22), 2026-09-26: rewritten after the pivot to the representation-level thesis
(research/pivot-decision.md). Sources for the claims (no bracketed citations here, to stay independent of
§6 numbering, which another worker rewrites in parallel):
- "millions of trials or more": e.g. DD-PPO (Wijmans et al., ICLR 2020) used 2.5 billion frames; the
  reference was pruned from §6 in wave 9, so the visible text no longer quotes the number.
- "dozens of papers a year, more than ten open-source twin simulators" = research/crowdedness.md and
  novelty-synthesis.md (3DGS twins for robot learning 23 -> 96 -> 124 papers/yr 2024/25/26; >= 12
  open-source twin simulators). Kept deliberately vague ("dozens").
- "running the policy in the real world" = SRCC needs paired real rollouts (Kadian et al., RA-L 2020);
  "image-quality scores track real performance poorly" = Truong et al., CoRL 2022 (lower fidelity can
  transfer better) and novelty-options §4 (no fidelity metric predicting transfer found).
- "used to predict accuracy/generalization of image classifiers and other networks" = weight-space learning /
  model zoos (Schürholt et al. NeurIPS 2022; Navon et al. ICML 2023; Zhou et al. NeurIPS 2023; Kofinas et
  al. ICLR 2024; ICLR 2025 Weight Space Learning workshop topic "inferring test performance or
  generalization error from weights"), novelty-options §3. Not applied to twin-trained policies: S2
  0/0/0/1/3 (2019-22/23/24/25/26), novelty-options §3 and niches-map rank 1.
- Review-2 (issue #24), 2026-09-26, R2-F9/F14: "known to track real performance poorly" overstated the
  evidence (Truong et al. compare simulator fidelity settings; no study of reconstruction image-quality
  scores vs transfer was found), so softened; "millions of trials or more" dropped (unsourced in visible text).
- K46 groups: https://ai.pwr.edu.pl/research-groups (read 2026-09-26), group "Uczenie reprezentacji w
  grafach, grafy wiedzy i modele w przestrzeni wag".
- Real robot = tier C, planned K29 Denali cooperation (not agreed; research/resources.md §1), so the lab is
  not named in the visible text.
- The pre-PhD ACL 2025 SRW paper stays only in §12 (review-1 decision), although its method (GNN over
  per-layer hidden states) is the direct precursor of RQ2.
-->

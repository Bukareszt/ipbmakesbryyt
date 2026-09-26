# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Modern machine learning is limited less by models than by **data in the target domain**. Embodied agents
(mobile robots, manipulators) learn strong behaviour only from very large amounts of experience. In the
real world such data is slow, expensive and sometimes risky to collect, so a policy is usually trained in
simulation and then deployed on real sensor data, where it often fails (the **sim-to-real gap**).

**Digital twins built by neural scene reconstruction** (3D Gaussian Splatting, Neural Radiance Fields)
turn a short real capture into a photorealistic model of the target scene, in which a policy can be trained
at scale. This gives a **real-to-sim-to-real loop**: capture the real scene, build a twin, train the policy
in the twin, run a few real trials, correct the twin and the policy, deploy. Building twins has quickly
become routine, with dozens of papers a year and more than ten open-source twin simulators. What remains
open is the **real data** the loop consumes. Each step spends it: the capture, the real data used to make
training robust to what the twin got wrong, and the real trials used to check and correct the policy.
Today these amounts are chosen by habit: the scene is recorded uniformly, the policy is trained with
generic randomization, and real trials are picked at random or by hand. How much real data a twin
actually saves, especially for navigation, has, to our knowledge, not been measured.

**What the dissertation proposes.** The real data needed by the loop can be reduced by **allocating it
actively**: capture only what the policy needs to build the twin, train so that the policy is robust to
the twin's errors, and collect only the few real rollouts that close the remaining gap. Two signals, both
computed from data the loop already collects, guide these choices: the **uncertainty of the reconstruction** (where
the twin is unreliable) and the **policy's own internal representations** (where twin and real inputs look
different to the policy). The result is measured as a budget–performance curve: how much real data the loop
needs to reach a given real success rate, compared with uniform allocation and with learning from real
data only.

**Why this topic, and why in this discipline.** The object is a data-efficient learning methodology
(active learning, learning under distribution shift, uncertainty estimation), not a robot, a simulator or a
benchmark, which places it in *information and communication technology*. The student uses existing twin
pipelines, simulators and public datasets and does not develop new ones. **Visual navigation** is the
primary testbed, because public scene datasets with dense real captures make it possible to count real
data exactly without an own robot; **robotic manipulation** tests that the methods carry over to another
task. Trials on a real robot (planned cooperation with a PWr robotics laboratory) validate, but do not
decide, the conclusions. The topic fits the Department of Artificial Intelligence (K46), whose research
groups include representation learning. The computation runs on the GPU infrastructure available to PWr
researchers (WCSS, PLGrid).

**Potential application areas:** faster and cheaper deployment of learned robots in new buildings and
workcells (service, assistive, warehouse and inspection robotics, flexible manipulation), with less time
spent recording scenes and supervising real trials; guidance on how to record a site for a twin; and,
beyond robotics, any system trained on reconstructed or synthetic data and deployed on real sensor data
(industrial digital twins, perception for autonomous systems), where real data must be collected on a
budget.

<!--
Review-3 (issue #27), 2026-09-26: R3-F4 the real images for the representation signal are a held-out slice
of the capture (counted in its budget, §9 Stage II), so "without extra real data" became "from data the loop
already collects". R3-F11 "to our knowledge" added to the not-measured claim.
-->
<!--
Wave 11 (issue #25), 2026-09-26: rewritten after pivot decision v2 (research/pivot-decision.md, binding):
object = the real-to-sim-to-real loop and using less real data; representations and uncertainty are tools,
not the object; no benchmark building. Removed wave 9-10 wording: "measured, localized and predicted from
representations", "benchmark of paired real and reconstructed data", "which representations survive
reconstruction", weight-space learning / metanetworks as the core, pre-deployment screening of policies.
Sources for the claims (no bracketed citations here, to stay independent of §6 numbering, which another
worker rewrites in parallel):
- "dozens of papers a year, more than ten open-source twin simulators" = research/crowdedness.md and
  novelty-synthesis.md (3DGS twins for robot learning 23 -> 96 -> 124 papers/yr 2024/25/26; >= 12
  open-source twin simulators). Kept deliberately vague ("dozens").
- "chosen by habit" / openness of each step = research/niches-data.md: task-aware capture N1 2/2/0/2
  (S2 2023/24/25/26; active view selection for NeRF/3DGS itself is active, 11/17/33/35, but optimises
  reconstruction quality, e.g. FisherRF arXiv:2311.17874, GenNBV CVPR 2024); active choice of real rollouts
  in the twin setting N2 1/2/0/3 (open); representation-guided weighting of twin data N9 0/0/1/0;
  reconstruction uncertainty in the loop niches-eval N4 0/0/3/4 (pivot-decision.md: "0/0/1/1" as a
  training signal). "Generic randomization" = domain randomization (Tobin et al., IROS 2017, §6).
- "how much real data a twin saves, especially for navigation, has not been measured" = pivot-decision.md
  and crowdedness.md ("real-data-budget curves for navigation: none published"; manipulation analogues
  exist: X-Sim, R2R2R, novelty-synthesis.md); references-check.md marks the general statement as the
  author's reading of the abstracts, to be confirmed by the supervisor after reading the full papers.
  Worded as "has not been measured" for navigation only, and softened by "especially".
- "Learning from real data only" = the H4 comparator (§7).
- K46 groups: https://ai.pwr.edu.pl/research-groups (read 2026-09-26), group "Uczenie reprezentacji w
  grafach, grafy wiedzy i modele w przestrzeni wag". Only "representation learning" is used now, because
  weight-space models are no longer the core method.
- Real robot = tier C, planned K29 Denali cooperation (not agreed; research/resources.md §1), so the lab is
  not named in the visible text.
-->

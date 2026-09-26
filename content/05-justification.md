# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Modern machine learning is limited less by models than by **data in the target domain**. Systems that act
in or measure the physical world, such as robot manipulators, mobile robots and other autonomous or
perception systems, need large amounts of experience, and in the real world that data is slow, expensive
and sometimes risky to collect. A policy or model is therefore often trained in simulation and then used
on real data, where it often performs worse (the **sim-to-real gap**).

**Digital twins** built from real data narrow this gap. Neural scene reconstruction (3D Gaussian
Splatting, Neural Radiance Fields) turns a short real capture into a photorealistic model of the geometry
and appearance of a scene, and system identification estimates its physical and dynamic parameters (masses,
friction, actuation) from a few real interactions. This gives a **real-to-sim-to-real loop**: collect real
data, build a twin, learn in the twin, check and correct with a little more real data, deploy. Building
twins has become routine, with dozens of papers a year and more than ten open-source twin
simulators. What remains open is the **real data** the loop consumes. Each step spends it: the capture that
builds the twin, the real data used to make learning robust to what the twin got wrong, and the real-world
trials or interactions used to check and correct the result. Today these amounts are chosen by habit: data
is collected uniformly, learning uses generic randomization, and real trials are picked at random or by
hand. How much real data a twin actually saves has, to our knowledge, not been measured systematically
across tasks.

**Goal of the dissertation.** The goal is to develop **a method** for learning in the real-to-sim-to-real
loop that reaches a given real-world performance with **significantly less real data** than existing
approaches. The method is one pipeline with three components, one per loop step: (C1) task-aware capture
of the data that builds the twin, (C2) learning that is robust to the twin's errors, and (C3) active
selection of the few real-world data or interactions that correct the twin and the model. Two signals,
both computed from data the loop already collects, guide all three: the **uncertainty of the twin** (where
it is unreliable) and the **learned model's own
representations** (where twin and real inputs look different to it). The thesis is that the method needs
at most a tenth of the real data of learning from real data only, and at least two times less than the
strongest existing real-to-sim-to-real pipeline, measured as budget–performance curves in both testbeds.

**Why this topic, and why in this discipline.** The object is a general, task- and domain-agnostic
data-efficient learning methodology (active learning, learning under distribution shift, uncertainty
estimation), not a particular robot, task, simulator or benchmark, which places it in *information and
communication technology*. The student uses existing twin pipelines, simulators and public datasets and
does not develop new ones. The methods are tested with the same settings on two testbeds of equal status,
**robotic manipulation** and **visual navigation**, where public data make it possible to count real data
exactly without an own robot. Trials on a real robot (planned cooperation with a PWr robotics laboratory)
validate, but do not decide, the conclusions. The topic fits the Department of Artificial Intelligence
(K46), whose research groups include representation learning. The computation runs on the GPU
infrastructure available to PWr researchers (WCSS, PLGrid).

**Potential application areas:** faster and cheaper deployment of learned systems in new places, such as
robot workcells, warehouses, buildings and inspection sites, with less time spent collecting data and
supervising real trials; guidance on how much real data to collect for a twin; and, beyond robotics, any
model trained on reconstructed or simulated data and used on real sensor data (industrial digital twins,
perception for autonomous systems), where real data must be collected on a budget.

<!--
Wave 14 (issue #30), 2026-09-26: pivot decision v4 (research/pivot-decision.md, top; framing only, v3
scope unchanged). "What the dissertation proposes" became "Goal of the dissertation" (cel pracy): one
method with components C1-C3 (v4 wording), guided by the same two signals; the thesis sentence = §7 H4:
(a) <= 10% of real-only data, (b) >= 2x less than the strongest existing real-to-sim-to-real pipeline
(uniform capture + domain randomization + random real-data selection, RialTo-style; §7, §9 Stage IV).
(b) is new in v4 and marked there for supervisor confirmation.
-->
<!--
(history) Wave 13 (issue #28), 2026-09-26: generalized after pivot decision v3 (research/pivot-decision.md, top):
domain-agnostic methodology; "policy" -> "policy or model"; "real rollouts/trials" -> "real-world data /
interactions / trials"; the twin covers geometry and appearance (neural reconstruction) AND physical and
dynamic parameters identified from real data (system identification; cf. §6 [22, 23, 27]: dynamics
randomization, SimOpt, Phys2Real); manipulation and navigation are equal testbeds (no "primary"). The
not-measured claim is now "not measured systematically across tasks" (manipulation point comparisons exist:
X-Sim "10x less data collection time", RialTo; review-3 §5), hedged with "to our knowledge". Examples of
physical parameters (masses, friction, actuation) are generic textbook examples, not claims about a work.
-->
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

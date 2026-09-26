# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Modern machine learning is limited less by models than by **data in the target domain**. Robot
manipulators, mobile robots and other systems acting in the physical world need much experience, which is
slow, expensive and sometimes risky to collect in reality. Pretrained open
**vision-language-action (VLA) models**, trained on large robot datasets, have made the starting point much
stronger, but they still need data from the target task and place to work there. Training in simulation
avoids that cost but opens a **sim-to-real gap**.

**Digital twins** built from real data narrow this gap. Neural scene reconstruction (3D Gaussian
Splatting, Neural Radiance Fields) turns a short real capture into a photorealistic model of the geometry
and appearance of a scene, and system identification estimates its physical parameters (masses, friction,
actuation) from a few real interactions. Learned **world models** can generate further variations. This
gives a **real-to-sim-to-real loop**: collect real data, build a twin, fine-tune in the twin, check and
correct with a little more real data, deploy. Building twins, fine-tuning VLAs in simulation and training
them in world models are all active research areas. What remains open is the **real data** the whole loop
consumes. Each step spends it: the capture that builds the twin, the real data used to make learning
robust to what the twin got wrong, and the real-world trials used to check and correct the result. Today
these amounts are chosen by habit: data is collected uniformly, learning uses generic randomization, and
real trials are picked at random or by hand. How much real data a twin actually saves has, to our
knowledge, not been measured systematically across tasks.

**Goal of the dissertation.** The goal is to develop **a method** for learning in the real-to-sim-to-real
loop that reaches a given real-world performance with **significantly less real data** than existing
approaches. A pretrained open VLA is fine-tuned sim-first in the twin. The method has three components,
one per loop step: (C1) capture guided by a vision-language model (VLM) to the task-relevant parts of the
scene where the twin is most uncertain, (C2) parameter-efficient fine-tuning that is robust to the twin's
errors, in the twin and in a world model grounded in it that covers what the twin got wrong, and (C3)
active selection of the few real-world data that correct the twin, the world model and the VLA. The
**uncertainty** of the twin, the world model and the VLA guides all three. The thesis is that the method
needs at most a tenth of the real data of fine-tuning the same VLA on real data only, and at least two
times less than the strongest existing twin fine-tuning pipeline, in both testbeds.

**Why this topic, and why in this discipline.** The object is a general, task- and domain-agnostic
data-efficient learning methodology (active learning, learning under distribution shift, uncertainty
estimation, adaptation of foundation models), not a particular robot, task, simulator or benchmark, which
places it in *information and communication technology*. The student builds on existing open models,
twin pipelines, simulators and public datasets. The method is tested with the
same settings on two testbeds of equal status, **robotic manipulation** and **visual navigation**, where
public data make it possible to count real data exactly without an own robot. Trials on a real robot
(planned cooperation with a PWr robotics laboratory) validate, but do not decide, the conclusions. The
topic fits the Department of Artificial Intelligence (K46), whose research groups include representation
learning. Parameter-efficient fine-tuning of open VLAs runs on the GPU infrastructure available to PWr
researchers (WCSS, PLGrid).

**Potential application areas:** faster and cheaper deployment of robot foundation models in new places,
such as robot workcells, warehouses, buildings and inspection sites, with less time spent collecting data
and supervising real trials; guidance on how much real data to collect for a twin; and, beyond robotics,
any model adapted on reconstructed or simulated data and used on real sensor data.

<!--
Wave 15 (issue #31), 2026-09-26: pivot decision v5 (research/pivot-decision.md, top; method content; goal,
thesis and v3 scope unchanged). Changes:
- Para 1: open VLAs as the starting point. "trained on large robot datasets" = OpenVLA arXiv:2406.09246
  ("970k real-world robot demonstrations"), Octo arXiv:2405.12213 ("800k trajectories from the Open
  X-Embodiment dataset"). "still need data from the target task" = both abstracts describe fine-tuning to
  new settings/domains with in-domain data.
- Para 2: world models added; "fine-tuning VLAs in simulation and training them in world models are all
  active" = v5 novelty guardrail (crowded), verified examples: VLA-RL arXiv:2505.18719, SimpleVLA-RL
  arXiv:2509.09674, RL4VLA arXiv:2505.19789, TwinRL arXiv:2602.09023 (RL of a VLA in a smartphone-captured
  twin), VLA-RFT arXiv:2510.00406, World-Env arXiv:2509.24948, WMPO arXiv:2511.09515. "Dozens of papers a
  year, more than ten open-source twin simulators" dropped for space; it stays in research/crowdedness.md.
- Goal: C1-C3 per v5; the guiding signal is now the uncertainty of twin, WM and VLA (v5 C3). The
  "model's own representations" signal survives inside C2 (representation distance, §7 H2(a)), not
  repeated here for space. Thesis = §7 H4 (a) real-only fine-tuning of the same VLA, (b) strongest
  existing twin fine-tuning pipeline for VLAs (TwinRL/RialTo-style, §7 comment). (b) new in v4: CONFIRM
  with the supervisor.
- Compute: "Parameter-efficient fine-tuning of open VLAs runs on ... WCSS, PLGrid" rests on OpenVLA's
  abstract ("can be fine-tuned on consumer GPUs via modern low-rank adaptation methods"). PLGrid/WCSS GPU
  types and grant size UNVERIFIED (research/resources.md).
- "adaptation of foundation models" added to the ML areas (the object is still the loop's real data).
- Application list shortened for space ("industrial digital twins, perception for autonomous systems"
  removed).
-->
<!--
(history) Wave 14 (issue #30), 2026-09-26: pivot decision v4 (research/pivot-decision.md, top; framing only, v3
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

# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Mobile robots that move around buildings, such as service, delivery, inspection and assistive robots,
rely increasingly on learned **navigation models**. Such models need a lot of experience from the place
where they will work, and collecting it in reality is slow, expensive and sometimes unsafe. Training in
simulation avoids this cost but opens a **sim-to-real gap**: a model that works in a generic simulator
often fails in a real building.

**Digital twins** built from real data narrow this gap. Neural scene reconstruction turns a short video or
depth capture of a real building into a photorealistic model of its geometry and appearance, and a few
measurements give the physical properties that matter for navigation. Learned **world models** can
generate further situations, and pretrained **foundation models** provide a strong starting point. This
gives a **real-to-sim-to-real pipeline**: acquire real data, build a twin, train the navigation model in
it at scale, and transfer it back to reality, where a little more real data checks and corrects the twin
and the model. Each of these parts is an active research area. What remains open is the **real data** the
whole pipeline consumes: the capture that builds the twin, the real samples that make training robust to
what the twin got wrong, and the real trials that correct the result. Today these amounts are chosen by
habit: data is captured uniformly, training uses generic randomization, and real trials are picked at
random or by hand. How much real data a twin actually saves in navigation has, to our knowledge, not been
measured systematically.

**Goal of the dissertation.** The goal is to develop **a method** for real-to-sim-to-real learning of
navigation models that reaches a given real-world navigation performance with **significantly less real
data** than existing approaches. The method covers the three stages of the pipeline: (1) deciding which
real data is worth acquiring to build the twin, (2) training navigation models in the imperfect twin,
extended with world models and foundation models, so that its errors do not transfer, and (3) choosing the
few real data that best correct the twin and the model. The thesis is that the whole method needs at least
two times less real data than the strongest existing real-to-sim-to-real approach.

**Why this topic, and why in this discipline.** The object is a data-efficient learning method (active
learning, learning under distribution shift, uncertainty estimation, adaptation of pretrained models), not
a particular robot, simulator or benchmark, which places it in *information and communication technology*.
The student builds on existing open reconstruction pipelines, simulators, pretrained models and public
datasets. Public scans of real buildings make it possible to count real data exactly without an own robot;
trials on a real robot (planned cooperation with a PWr robotics laboratory) validate, but do not decide,
the conclusions. The topic fits the Department of Artificial Intelligence (K46), whose research groups
include representation learning, and the training runs on the GPU infrastructure available to PWr
researchers (WCSS, PLGrid).

**Potential application areas:** faster and cheaper deployment of mobile robots in new buildings, such as
warehouses, hospitals, offices and inspection sites, with less time spent collecting data and supervising
real trials; guidance on how much real data to collect for a twin; and, beyond robotics, any model trained
on reconstructed or simulated data and used on real sensor data.

<!--
Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
general description; navigation (indoor mobile robots) is the domain; pipeline real data -> twin ->
navigation models (with world models and foundation models as families, no names) -> real. No model or
checkpoint names, no VLA/TwinRL detail, no manipulation (v6 "Level of detail", "Domain"). Goal = v6 goal;
the three stages = v6 "Object" 1-3; thesis = §7 H4 (>= 2x less than the strongest existing
real-to-sim-to-real approach; new in v4, CONFIRM with the supervisor). "How much real data a twin saves in
navigation has not been measured systematically" = the Wave 11 claim (crowdedness.md: "real-data-budget
curves for navigation: none published"), hedged with "to our knowledge" (R3-F11). The generic application
examples (service, delivery, inspection, assistive robots; warehouses, hospitals, offices) are examples,
not claims about a work. "Each of these parts is an active research area" = §6 (twins [11-13], world models
[25, 26], navigation foundation models [21, 22]). The "compute" sentence no longer names VLAs or LoRA.
-->
<!--
(history) Wave 15 (issue #31), 2026-09-26: pivot decision v5 (research/pivot-decision.md, top; method content; goal,
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

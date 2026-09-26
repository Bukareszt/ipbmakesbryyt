# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Deep learning has led to impressive results in computer vision and natural language processing, and it is
now increasingly applied to physical AI: robots and other embodied systems that perceive and act in the
real world, such as mobile robots navigating buildings or robotic arms manipulating objects. Unlike models
trained on images or text, such models need very large amounts of interaction data, which is slow,
expensive and sometimes unsafe to collect in the real world. Therefore, they are commonly trained in
simulation. Recently, digital twins built from real data became a promising alternative to hand-made
simulators: neural scene reconstruction methods, such as Neural Radiance Fields and 3D Gaussian Splatting,
turn a short video of a real place into a photorealistic 3D model in which a robot can be trained at
scale. This gives the real-to-sim-to-real loop: real data is transferred into a simulation, a model is
trained there, and the model is transferred back to the real world.

However, the usefulness of this loop depends entirely on how well the trained models generalize. A model
that performs very well in simulation often fails in reality, because a digital twin never reproduces the
real world exactly: appearance, lighting, geometry and physical properties differ. Moreover, models often
fail again in places or tasks that were not seen during training. This sim-to-real generalization gap
remains one of the main obstacles for physical AI. The methods proposed so far, such as domain
randomization, rely largely on hand-tuned heuristics, are typically evaluated on a single task and a few
scenes, and do not explain which properties of the simulation and of the learned representations
actually determine generalization to reality. Therefore, the dissertation aims at developing methods that
improve the generalization of deep learning models trained in real-to-sim-to-real loops, with a particular
focus on the digital twin itself, the representations learned in it, and the adaptation of models to
reality with little real data.

The research is relevant to machine learning in general, as it concerns learning under distribution shift
and the generalization of representations, and it could help to understand why models trained on
synthetic data succeed or fail on real data. The results have potential applications in service and
logistic robotics, where robots could be trained in a digital copy of a new warehouse, hospital or office
and work there reliably, as well as in autonomous systems and any other domain where models are trained on
simulated or reconstructed data and used on real sensor data.

<!--
Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top):
the goal is a method that REDUCES real data (three reduction mechanisms, one per loop step); budget
curves and operator minutes are only the evaluation; navigation = main testbed, manipulation =
generalization test; general level of detail, no model or checkpoint names. Sources of the claims:
- "twins built from a phone video already train navigation and manipulation models that work in reality"
  = §6 [12-18] (EmbodiedSplat, Vid2Sim, GaussGym, ReaDy-Go, RialTo, X-Sim, TwinRL), all in the
  deep-research report (reports/Uczenie nawigacji w cyfrowych bliźniakach.md, table "Pełne potoki").
- "no navigation pipeline has a stage that corrects the twin with real trials, and none reports how
  success depends on the real data spent; in manipulation such accounting exists only at single points"
  = the report's lead ("Żadna praca nawigacyjna nie zmienia budżetu ... Żadna nie ma etapu korekty ...
  Żadna nie publikuje krzywej"; manipulation: RialTo, X-Sim, R2R2R, TwinRL single points) and its
  recommendation 1 (name this in §5-§7). Hedged with "to our knowledge" (R3-F11).
- Thesis = §7 H4 (>= 2x less than the strongest existing real-to-sim-to-real approach; new in v4, CONFIRM
  with the supervisor).
- "minutes of operator work" = the report's one-unit recommendation (B = capture + demonstrations +
  on-robot trials with resets).
- "small mobile robot" = TurtleBot 4 Lite (SzD Minigrant) or K29 robots (§9, §12); the lab is not named
  here because the cooperation is not agreed.
The generic application examples are examples, not claims about a work.
-->
<!--
(history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
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

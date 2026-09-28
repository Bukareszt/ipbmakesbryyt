# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Robots that learn by trial and error need a very large number of attempts, more than is practical or safe to collect on a real robot [1]. For this reason such models are usually trained in simulation [2]. A newer kind of simulation is the digital twin. A short video of a real room or table is turned into a photorealistic 3D copy with methods such as 3D Gaussian Splatting. The robot model is trained in this copy and then used in the real place.

The weak point of this approach is that the copy is never exact. A glass door may be missing from the copy, a mirror may look like an open room behind it, and textures and lighting are always slightly different. A model that works well in the copy can therefore fail in reality [3], and it does even worse in real places for which no copy was made [2]. This drop in performance is called the simulation-to-reality gap, and it is one of the main reasons why learned robot models are still hard to deploy.

The usual remedies do not use knowledge of where the copy is wrong. Domain randomization adds random changes to colours, textures or physics [4]. Newer variants learn how wide these changes should be [5],[6], but they tune physical parameters and do not ask which visual errors of the copy actually matter. Other methods force the model to see simulated and real images the same way, but in doing so they can also remove information the robot needs. When a few real examples are collected, they are mostly used to correct either the copy [5],[7] or the model [8],[9], and I found no method that chooses them to improve both at once. Earlier studies measured how factors such as lighting, texture or physics realism affect transfer [10],[11], but it is still not known which local reconstruction errors of a digital twin harm a model and at which stage inside it the harm appears.

I want to answer this question by looking inside the models. A neural network does not use the image directly. It turns it into internal features, called representations, and makes its decision from them. My working assumption is that an error in the copy that leaves these features unchanged does little harm, while an error that changes the features the decision depends on is likely to cause failures [12],[13]. This gives a measurable way to study the gap. First, I will check which reconstruction errors change the representations in a harmful way. Then I will find the stage inside the model at which real images lose information needed for the task, and correct the representations there. I will also study how to choose the few real examples that best improve both the copy and the model, and whether the improvements hold in new places and in a second task. I will work on two tasks of equal weight, robot navigation and robotic manipulation, and always test on scenes not used for training.

The answer would help decide which parts of a digital twin need to be accurate and where extra real data is worth collecting. In practice, a robot could be trained in a digital copy of a new warehouse, hospital or home and work there reliably after little real-world adaptation. The same questions arise in autonomous driving, where simulators and reconstructions of recorded drives are widely used to train and test models.

<!-- Wave 31: grounding + clarity (ultracode) -->
<!-- Wave 30: §5 rewritten as a clear argument (problem, example, open question, representation-level approach, relevance) at the student's request ("not gibberish") -->
<!-- Wave 29: humanized (no semicolons) -->
<!-- Wave 28: restyled after the accepted 2025 IPB (2026-09-28, research/accepted_plan_tts_2025.txt). §5 narrative motivation, first person, about 440 words; content unchanged (twins, gap as distribution shift, limits of DR/invariance/one-sided correction, aim with representation methods, two equal tasks, held-out scenes, applications). Proxy and robot details moved to §9 only. -->
<!-- Wave 27: mechanisms + citation audit fixes (2026-09-27, reports/Mechanizmy uczenia reprezentacji IPB.md). §5: aim names the representation methods (analyse and align learned representations); RQ2 = stage where task information is lost on real inputs; RQ3 = fixed budget; RQ4 = properties measured beforehand; robot = optional check of the direction of results and of the proxy's validity, if access allows (consistent with §9). -->
<!-- Wave 24: humanized -->
<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §5: navigation and manipulation are two equal testbeds for task-agnostic methods; RQ4 wording "from one physical task to another"; proxy honesty kept for navigation (independent capture = reconstruction-fidelity gap, robot = actuation and sensors); manipulation = twins of real tabletop scenes from public robot dataset images, compared with published real-robot results of the same policies. No model/checkpoint names. -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §5: terms defined once here ('digital twins, i.e., simulations built from real data'; 'the sim-to-real gap' = the drop in performance) and used consistently in §5-§9 (fix 9); navigation = main task, manipulation = controlled simulated confirmation test (fix 1); one proxy-honesty sentence: the independent capture measures the reconstruction-fidelity gap, the robot is the main evidence for actuation and sensor differences (fix 2); 'chosen at random, by hand or by simple heuristics such as observed failures' shortened. -->
<!-- Review-6 (2026-09-27): grammar (data plural, "such models", present perfect, "aims to improve", "small amount of real data", "logistics"); Physical AI = AI in robots...; DR limitation aligned with §6 ("even when fitted to real data, varies a few global parameters"); run-on sentence split. -->
<!--
Wave 20 (ultracode), 2026-09-27: visible text rewritten from scratch in the narrative register of the
accepted Binkowski IPB §5 (need for data -> simulation/digital twins -> sim-to-real gap -> limitations ->
aim -> applications). Aim paragraph mirrors RQ1-RQ4 of content/07 without numbers, model names or
benchmark goals. Earlier wave notes below are kept as history.
-->
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

# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The proposed PhD dissertation aims to introduce several contributions to the development of the
scientific discipline. The central scientific problem addressed is explaining and reducing the sim-to-real
gap caused by the distribution shift between a digital twin and reality; poor generalization of models
trained in simulation remains one of the main obstacles to applying machine learning in physical AI. The
central claim of the dissertation is that this gap is concentrated in a small set of task-relevant
discrepancies, which can be identified among the reconstruction errors of the digital twin, localized at
the stage of the model where task information is lost, and reduced by correcting both the digital twin and
the model from the same small set of real data. Addressing them there is expected to yield better
generalization than uniform randomization, alignment at a fixed location of the model, or real data chosen
at random or at the model's failures. Research questions 1-3 test the three parts of this claim, and
question 4 tests whether it holds across environments and tasks; the methods derived from it are intended
to be general, i.e., not tied to a particular robot, scene or task, and will be examined on two equal
physical AI tasks, robot navigation and robotic manipulation.

Furthermore, the research is expected to deliver new methods and findings that do not exist at present:
an attribution of the sim-to-real gap to reconstruction errors that vary across a scene, with a principle
for randomizing each region of a digital twin according to its reconstruction uncertainty and task
relevance; a method for localizing the gap as the first stage of a deep model at which task information is
lost on real inputs, and for aligning representations only there; a rule for selecting real data that
corrects the digital twin and the model at the same time; and an empirical account of whether properties
of the shift, measured before a method is applied, predict better than simple indicators when these
improvements carry over across environments and from one task to another. Such knowledge could complement the currently
dominant randomization heuristics with more principled and interpretable approaches, and could introduce
new perspectives for the design of simulations and of training procedures.

Since transfer from simulation to reality is an instance of learning under distribution shift, the
findings are also expected to be relevant to machine learning in general. The analysis of which errors in
the training distribution are harmful concerns domain adaptation; the localization of the sim-to-real gap
inside a model extends probing methods developed for language and vision models and contributes to
representation learning; and the selection of informative data under a budget concerns active learning
and the adaptation of pretrained foundation models to new domains from a few examples.

Finally, the developed methods could reduce the amount of real data, and thus the cost, needed to deploy
learning-based robots in new environments. The source code and the experimental setups are planned to be
released, which could facilitate further research in the field and attract other researchers. Apart from
purely scientific results, the methods could be used in real-world applications such as service,
logistics and inspection robotics, as well as in other domains where models are trained in simulation,
e.g., autonomous driving.

<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §8: methods examined on two equal tasks (navigation and manipulation) instead of "mainly navigation, manipulation as a controlled confirmation test"; RQ4 contribution "across environments and from one task to another". -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §8: terms (digital twin, sim-to-real gap); central claim and contribution list aligned with the narrowed RQ1-RQ4 (errors varying across a scene, task-information localization, correcting both from the same data, prediction beyond simple indicators); manipulation = controlled confirmation test (fix 1). -->
<!-- Review-6 (2026-09-27): central scientific problem and single central claim added to paragraph 1, RQs presented as parts of it; "dominant", "a few", "logistics", "PhD". -->
<!-- Wave 20 (ultracode), 2026-09-27: visible text rewritten from scratch in the Binkowski §8 register; contributions mapped to the final RQ1-RQ4 (components of the discrepancy, localization of the gap and task-relevant invariance, budgeted real-data selection correcting model and simulation, generality across environments and tasks); relevance to distribution shift, representation learning, active learning and foundation-model adaptation; code release; applications. No numbers, no model names. -->
<!-- Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top):
key contribution = a method that REDUCES real data (three reduction mechanisms, one per loop step); the
budget curves, the one unit (operator minutes), the budget grid, the proxy protocol and the code are how
the method is evaluated and released, not contributions. Navigation decides H1-H4; manipulation =
generalization test without separate thresholds (v7 "Scope"). "First evidence ... of how much real data
such a loop needs" = the report's conclusion that no such curves exist in navigation and only single points
in manipulation (reports/Uczenie nawigacji w cyfrowych bliźniakach.md), hedged with "to our knowledge"
(R3-F11). Comparators per mechanism = the report's pre-registered baselines (H1: uniform, FisherRF-type,
risk/semantic-weighted; H2: uniform DR, no DR; H3: random, failure-driven). Papers per v7: P1 = mechanism 1
(H1) in navigation, NeurIPS 2027; P2 = mechanisms 2-3 (H2, H3) in navigation + first manipulation results,
ICML 2028 (CVPR 2028 per §3 T5.4 only if H3 is complete by Nov 2027); P3 = the whole method (H4) with
generalization to manipulation, NeurIPS 2028, fallback ICLR 2029. H4 threshold new in v4, CONFIRM with the
supervisor. -->
<!-- (history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
general description, navigation only, stages 1-3 + whole pipeline. Key contribution = the method (v4
framing kept); its claim = §7 H4 (>= 2x less than the strongest existing real-to-sim-to-real approach,
CONFIRM with the supervisor). Novelty guardrail kept in general terms ("Building twins, training in
simulation and using world models or foundation models are not new"; v5 crowdedness,
research/vla-wm-crowdedness.md). Removed per v6: VLA/VLM/LoRA wording, TwinRL/RialTo-style baseline
detail, manipulation testbed. Real-only learning kept only as a reported curve (§7, §9). Papers P1-P3,
venues and the review-3 R3-F3 mapping unchanged, content adapted to navigation. "To our knowledge" kept
(R3-F11). -->
<!-- (history) Wave 15 (issue #31), 2026-09-26: pivot decision v5 (research/pivot-decision.md, top; method content;
goal, thesis, v3 scope and v4 framing unchanged: the key contribution is the method, C1-C3 are its parts,
curves/protocol/code are how it is evaluated and released). Changes:
- Key contribution now names the setting of v5: a pretrained open VLA fine-tuned sim-first in the twin and
  a twin-grounded world model. H4 (a) = real-only fine-tuning of the same VLA, (b) = strongest existing twin
  fine-tuning pipeline for VLAs (TwinRL arXiv:2602.09023 / RialTo-style; §7 comment).
- NOVELTY GUARDRAIL (v5): explicit sentence that fine-tuning VLAs in simulation and in world models is not
  new (VLA-RL arXiv:2505.18719, SimpleVLA-RL arXiv:2509.09674, RL4VLA arXiv:2505.19789, TwinRL; VLA-RFT
  arXiv:2510.00406, World-Env arXiv:2509.24948, WMPO arXiv:2511.09515). The claimed novelty is the
  real-data budget of the whole loop (v5). "To our knowledge" kept (R3-F11).
- C1: VLM picks task-relevant regions (v5). C2: LoRA-type parameter-efficient RL + imitation fine-tuning,
  twin-grounded WM, second comparator "twin alone" = §7 H2(b). C3: gap predicted from twin, WM and VLA
  uncertainty; corrects twin, WM and VLA (v5). Closest to C3: TwinRL's "failure-prone yet informative
  configurations" for "targeted human-in-the-loop rollouts"; C3 differs by selecting under a counted
  budget and correcting twin and WM, not only the policy.
- Trims for the 1-page limit: practitioner sentence dropped from the evaluation paragraph; the proxy
  description keeps "a separate, higher-fidelity reference" (the separate-capture twin detail of R3-F1 is
  in §7 and §9).
- Dissemination unchanged (paper-to-venue mapping per §11/§12, review-3 R3-F3). -->
<!-- (history) Wave 14 (issue #30), 2026-09-26: reframed after pivot decision v4 (research/pivot-decision.md, top;
framing only, v3 scope unchanged). v4: "The key original contribution in §8 is the method"; "Budget curves,
the proxy-reality protocol and the code are how the method is evaluated and released. They are not
contributions in their own right"; C1-C3 "are parts of the method. They are not separate contributions."
So: key contribution = one method (C1-C3) + its claim (§7 H4 (a) <= 10% of real-only, (b) >= 2x less than
the strongest existing pipeline, uniform capture + DR + random real-data selection, RialTo-style; (b) new
in v4, CONFIRM supervisor); old items 1-3 became components C1-C3 (still RQ1-RQ3 / H1-H3, now ablations);
old item 4 (budget curves) and item 5 (protocol and code) merged into the supporting paragraph. The
"Contributions to ML methodology / in engineering terms (ITiT)" headings were dropped; the ITiT placement
stays in the first paragraph. Dissemination: paper-to-venue mapping unchanged; P1-P3 described by
component. "To our knowledge" kept (review-3 R3-F11). -->
<!-- (history) Wave 13 (issue #28), 2026-09-26: generalized after pivot decision v3 (research/pivot-decision.md,
top): object = the real-to-sim-to-real loop in general (task- and domain-agnostic); twin includes physical
parameters (system identification); "real rollouts" -> "real-world trials or interactions"; "policy" ->
"policy or model"; key contribution no longer "budget curves for navigation, where none have been
published" but curves measured with the same methods in two equal-status domains (manipulation point
comparisons exist: X-Sim, RialTo; review-3 §5). Items 1-4 still map one-to-one to RQ1-RQ4 / H1-H4; item
4 "hold unchanged in both domains" = §7 H4(b). Papers P1-P3 and venues unchanged (v3); P3 wording "budget
curves in both domains" replaces "budget law and manipulation" (R3-F11: a fitted curve is not a law). -->
<!-- (history) Wave 11 (issue #25), 2026-09-26: rewritten after pivot decision v2 (research/pivot-decision.md,
binding). Items 1-4 map one-to-one to RQ1-RQ4 / H1-H4 (one method per loop step + budget law). Removed
wave 9-10 content: representation-level thesis, gap localization, transfer forecasting from weights,
policy zoo as a contribution, the public paired-frame benchmark (the student rejected benchmark building).
Item 5 is a protocol + code, not a benchmark or dataset.
"To our knowledge" / "no real-data-budget curves published for navigation" = pivot-decision.md and
crowdedness.md; manipulation analogues exist (X-Sim, R2R2R, novelty-synthesis.md), hence "for navigation".
references-check.md marks this as the author's reading of the abstracts (supervisor to confirm).
"Hardly done" (item 2) = pivot-decision.md S2 counts: representation-guided weighting 0/0/1/0,
reconstruction uncertainty as a training signal 0/0/1/1 (2023/24/25/26); closest: MetaMVUC (RA-L 2025),
Phys2Real (arXiv:2510.11689) in niches-data N9 / niches-eval N4.
Item 1 vs. active reconstruction: FisherRF (arXiv:2311.17874), GenNBV (CVPR 2024) optimise reconstruction
quality (niches-data N1). Item 3: active data collection in the twin setting is open (niches-data N2,
1/2/0/3); closest: Active Fine-Tuning of Multi-Task Policies (arXiv:2410.05026).
Venue list = coordinator decision, verified from the official 5.01.2024 xlsx (Lp: NeurIPS 87, ICML 847,
ICLR 1674, CVPR 417, ICCV 442, ECCV 331). Paper-to-venue mapping = pivot-decision.md "Papers"
(P3 fallback ICLR 2029 as in §3 T6.3, review-2 R2-F4).
Review-3 (issue #27), 2026-09-26: R3-F3 P2 = ICML 2028 or CVPR 2028 (ICLR 2028 dropped, §3 T5.3); P1 = H1 +
first H2. R3-F11 "budget law" in the key contribution -> "budget curves" (a curve fitted on ~20 rooms is not
a law); item 5 names the separate-capture reference (R3-F1) and says "estimate". -->

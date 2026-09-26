# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The dissertation is in **information and communication technology** (*informatyka techniczna i
telekomunikacja*), area machine learning. Its object is the task- and domain-agnostic **real-to-sim-to-real
learning loop**: building a digital twin (appearance, geometry and, where
relevant, physical parameters) from limited real data, fine-tuning a policy (here a pretrained VLA) in it and transferring the result
back to reality; it develops a method that makes this loop work with **less real data**. Building twins,
world models, simulators or benchmarks, training foundation models from scratch, control design and mechanical engineering are not the object of the research;
the student uses existing tools, open models and public data.

**Key original contribution: the method.** To our knowledge, the first method for real-to-sim-to-real
learning that treats the real data of the whole loop as **one budget allocated actively at every step**
when a pretrained open vision-language-action (VLA) model is fine-tuned sim-first in a digital twin and in
a world model grounded in it. It targets a given real-world performance with at most a tenth of the real
data of real-only fine-tuning of the same VLA and at least two times less than the strongest existing twin
fine-tuning pipeline (RQ4, H4), with the same settings in robotic manipulation and visual navigation. Fine-tuning VLAs in simulation and in world models is not new; spending
the loop's real data where it matters is. The three components are parts of
this one method, each tested as an ablation at its own step:

1. **C1, capture less (RQ1, H1).** A vision-language model picks the task-relevant objects and regions
   from the instruction and scene, and capture (views for appearance and geometry, interactions for
   physical parameters) goes where the twin is most uncertain in them; compared with uniform and
   task-blind selection.
2. **C2, learn robustly in an imperfect twin (RQ2, H2).** Parameter-efficient reinforcement and
   imitation fine-tuning with augmentation and sample weights from the twin's uncertainty and the
   representation distance to a few real samples, and a twin-grounded world model covering the twin's
   uncertain regions; compared with uniform domain randomization and with the twin alone.
3. **C3, transfer with few real data (RQ3, H3).** Active selection of real-world trials by the twin-to-real
   gap predicted from the uncertainty of twin, world model and VLA, used to correct all three; compared
   with random selection.

**How the method is evaluated and released** (supporting the method, not contributions in their own
right). Budget–performance curves of the method against real-only fine-tuning and the existing pipeline,
which give the "exchange rate" between twin and real data; a proxy-reality protocol on public data that counts real data
exactly without a robot (a separate, higher-fidelity reference as "reality"), applied in each domain; and open-source code of the
method, built on existing open models, twin pipelines and simulators.

**Significance for the discipline.** Real target-domain data is the main cost of deploying learned
systems; methods that decide where it is worth spending, and a measured estimate of how much of it a twin
can replace, are relevant to active learning, learning under distribution shift, uncertainty
estimation and adaptation of foundation models in general, beyond robotics.

**Dissemination.** Results are planned for peer-reviewed conferences worth 200 points and assigned to ITiT
on the ministerial list of 5.01.2024: NeurIPS, ICML and ICLR (machine learning) and CVPR (computer vision),
with ICCV and ECCV for resubmissions. P1 (C1 and first C2 results, RQ1–RQ2) targets
NeurIPS 2027; P2 (C3, RQ3) ICML 2028 or CVPR 2028; P3 (the whole method against real-only fine-tuning and the
existing pipeline in both domains, RQ4) NeurIPS 2028, with ICLR 2029 as the fallback.

<!-- Wave 15 (issue #31), 2026-09-26: pivot decision v5 (research/pivot-decision.md, top; method content;
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

# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The dissertation is carried out in **information and communication technology** (*informatyka techniczna i
telekomunikacja*), in the area of machine learning. Its object is the **real-to-sim-to-real learning
loop** in general, task- and domain-agnostic: building a digital twin (appearance, geometry and, where
relevant, physical parameters) from limited real data, learning a policy or model in it and transferring
the result back to reality, and how to make this loop work with **less real data**. Building twins,
simulators or benchmarks, control design and mechanical engineering are not the object of the research;
the student uses existing tools and public data.

**Key original contribution.** To our knowledge, the first treatment of the real data in the whole
real-to-sim-to-real loop as **one budget to be allocated actively**, with a method for each step of the
loop and real-data budget curves measured with the same methods in two domains, robotic manipulation and
visual navigation.

Contributions to machine learning methodology:

1. **Capture less (RQ1, H1).** A task-aware capture method that chooses which real data to collect for a
   twin (views for its appearance and geometry, interactions for its physical parameters) from the twin's
   uncertainty in the parts that matter for the task, instead of for reconstruction quality alone, and a
   test of how much capture it saves against uniform and task-blind selection.
2. **Learn robustly in an imperfect twin (RQ2, H2).** An uncertainty-aware training method that turns the
   twin's per-region and per-parameter uncertainty and the representation distance to a small set of real
   samples into augmentation and sample weights, compared with uniform domain randomization at an equal
   capture budget.
3. **Transfer with few real data (RQ3, H3).** An active selection method for real-world trials or
   interactions, driven by the predicted twin-to-real gap and its uncertainty, and a procedure
   that uses them to correct both the twin and the learned model, compared with random selection.
4. **Budget curves for the loop (RQ4, H4).** Budget–performance curves of the full loop that give the
   "exchange rate" between twin and real data (how much real data the loop needs, relative to learning from
   real data only, to reach a given real task performance), and a test of whether the methods hold
   unchanged in both domains.

Contributions in engineering terms (ITiT):

5. **Evaluation protocol and software (supports all RQs).** A proxy-reality protocol on public data that
   counts real data exactly without a robot (a reference from a separate, higher-fidelity source as
   "reality", a low-budget twin from a separate capture as the simulator), applied in each domain, and
   open-source code for the three methods and the budget curves, built on existing twin pipelines and
   simulators. It tells practitioners roughly how much real data to collect for a new task or site.

**Significance for the discipline.** Real target-domain data is the main cost of deploying learned
systems. Methods that decide where it is worth spending, and a measured estimate of how much of it a twin
can replace, are relevant to active learning, learning under distribution shift and uncertainty
estimation in general, beyond robotics.

**Dissemination.** Results are planned for peer-reviewed conferences worth 200 points and assigned to ITiT
on the ministerial list of 5.01.2024: NeurIPS, ICML and ICLR (machine learning) and CVPR (computer vision),
with ICCV and ECCV for resubmissions. P1 (RQ1–RQ2, task-aware capture and first
uncertainty-aware training results) targets NeurIPS 2027; P2 (RQ3, active selection of real data and twin
correction) ICML 2028 or CVPR 2028; P3 (RQ4, budget curves in both domains) NeurIPS 2028, with ICLR 2029 as
the fallback.

<!-- Wave 13 (issue #28), 2026-09-26: generalized after pivot decision v3 (research/pivot-decision.md,
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

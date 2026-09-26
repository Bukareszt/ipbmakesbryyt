# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The dissertation is carried out in **information and communication technology** (*informatyka techniczna i
telekomunikacja*), in the area of machine learning. Its object is the **real-to-sim-to-real learning loop**
of embodied policies with digital twins built by neural reconstruction of real scenes, and how to make this
loop work with **less real data**. Visual navigation is the primary testbed and robotic manipulation the
cross-task test. Building twins, simulators or benchmarks, control design and mechanical engineering are not
the object of the research; the student uses existing tools and public data.

**Key original contribution.** To our knowledge, the first treatment of the real data in the whole
real-to-sim-to-real loop as **one budget to be allocated actively**, with a method for each step of the loop
and a measured budget law for navigation, where no real-data-budget curves have been published.

Contributions to machine learning methodology:

1. **Capture less (RQ1, H1).** A task-aware capture method that chooses which real views to record for a
   twin from the reconstruction's uncertainty in the regions that matter for the policy, instead of for
   image quality alone, and a test of how much capture it saves against uniform and reconstruction-only
   view selection.
2. **Train robustly on an imperfect twin (RQ2, H2).** An uncertainty-aware training method that turns
   per-region reconstruction uncertainty and the representation distance to a small set of real images
   into augmentation and sample weights, compared with uniform domain randomization at an equal capture
   budget.
3. **Collect few real rollouts (RQ3, H3).** An active selection method for real rollouts, driven by the
   predicted twin-to-real gap and its uncertainty, together with a procedure that uses the selected
   rollouts to correct both the twin and the policy, compared with random selection.
4. **A budget law for the loop (RQ4, H4).** Budget–performance curves of the full loop that give the
   "exchange rate" between twin and real data (how much real data the loop needs, relative to learning from
   real data only, to reach a given real success rate), compared with a uniform loop and a learned world
   model used as the simulator, and a test of whether the loop carries over unchanged from navigation to
   manipulation.

Contributions in engineering terms (ITiT):

5. **Evaluation protocol and software (supports all RQs).** A proxy-reality protocol on public scene
   datasets that counts real data exactly without a robot (a high-fidelity reference as "reality", a
   low-budget twin as the simulator), and open-source code for the three methods and the budget curves,
   built on existing twin pipelines and simulators. It tells a practitioner how much to record and how
   many real trials to plan for a new site.

**Significance for the discipline.** Real target-domain data is the main cost of deploying learned
systems, and models are increasingly trained on reconstructed or synthetic data and deployed on real sensor
data. Methods that decide where real data is worth spending, and a measured law of how much of it a twin
can replace, are relevant to active learning, learning under distribution shift and uncertainty estimation
in general, beyond robotics.

**Dissemination.** Results are planned for peer-reviewed conferences worth 200 points and assigned to ITiT
on the ministerial list of 5.01.2024: NeurIPS and ICLR (machine learning) and CVPR (computer vision), with
ICML, ICCV and ECCV for resubmissions, as in §3, §11 and §12. P1 (RQ1–RQ2, task-aware capture and
uncertainty-aware training) targets NeurIPS 2027; P2 (RQ3, active real-rollout selection and twin
correction) ICLR or CVPR 2028; P3 (RQ4, budget law and manipulation) NeurIPS 2028, with ICLR 2029 as the
fallback.

<!-- Wave 11 (issue #25), 2026-09-26: rewritten after pivot decision v2 (research/pivot-decision.md,
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
(P3 fallback ICLR 2029 as in §3 T6.3, review-2 R2-F4). -->

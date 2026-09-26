# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The dissertation is carried out in **information and communication technology** (*informatyka techniczna i
telekomunikacja*), in the area of machine learning. Its object is the **internal representations** of
encoders and embodied policies trained in digital twins built by neural reconstruction of real scenes, used
to measure, localize and predict how well the policies transfer to reality. Visual navigation is the
primary testbed and robotic manipulation the cross-task test. Building twins or simulators, control design
and mechanical engineering are not the object of the research.

**Key original contribution (core, RQ1–RQ2, H1–H2).** To our knowledge, the first demonstration that the
twin-to-real transfer of embodied policies can be **read from their representations**: where in the network
the gap arises, how it shrinks with the capture budget, and how large it will be for a given policy,
forecast from its hidden states or weights without real rollouts.

Contributions to machine learning methodology:

1. **Measuring and localizing the reconstruction gap (core; RQ1, H1).** A layer-wise analysis of paired real
   and twin-rendered observations (representational similarity, probing) that locates the gap inside frozen
   visual encoders and policies, relates it to the capture budget, and ranks encoders by robustness to
   reconstruction artifacts, tested against downstream transfer.
2. **Forecasting transfer and failure from internals (core; RQ2, H2).** Predictors learned over a population
   of twin-trained policies (graph networks over layers, weight-space metanetworks) that estimate a policy's
   real performance before deployment, and hidden-state failure monitors whose statistical coverage is
   checked across the twin-to-real shift. This brings weight-space learning and model analysis to embodied
   policies and distribution shift.
3. **Representation-guided use of a real-data budget (RQ3, H3).** Methods that use the measures and
   forecasts to weight twin training data, choose what to capture and select which real rollouts to
   collect, quantified by budget–performance curves against uniform and random allocation.
4. **Generalization of the measures (RQ4, H4).** Evidence of whether representation-based predictors carry
   over from navigation to manipulation and across simulator families, compared with simulation-based
   predictivity (SRCC) and a learned world-model evaluator.

Contributions in engineering terms (ITiT):

5. **Benchmark, data and software (supports all RQs).** A public benchmark of paired real and
   twin-rendered frames at graded capture budgets, a released zoo of twin-trained policies with twin and
   real outcomes, and evaluation code with pre-registered protocols, built on existing open-source twin
   pipelines and simulators. It gives other groups a reproducible way to test sim-to-real claims and to
   screen policies and encoders before a costly real deployment.

**Significance for the discipline.** Real target-domain data is the main cost of deploying learned
systems, and trained models are increasingly deployed on data unlike their training data. Showing that
transfer can be diagnosed and forecast from a model's internals, and that such forecasts save real data,
is relevant to machine learning under distribution shift and to model evaluation in general, beyond
robotics.

**Dissemination.** Results are planned for peer-reviewed conferences worth 200 points and assigned to ITiT
on the ministerial list of 5.01.2024: NeurIPS, ICML and ICLR (machine learning) and CVPR, ICCV and ECCV
(computer vision), as in §3, §11 and §12. P1 (RQ1, benchmark and localization) targets NeurIPS 2027; P2
(RQ2) ICLR or CVPR 2028; P3 (RQ3–RQ4, including manipulation) ECCV or NeurIPS 2028.

<!-- Wave 9 (issue #22), 2026-09-26: rewritten after the pivot (research/pivot-decision.md): items 1-4 map
one-to-one to RQ1-RQ4 / H1-H4; item 5 replaces the former "twin pipeline" contribution because the student
no longer builds twin pipelines (pivot scope: "no development of twin simulators"). The paired-frame
benchmark and policy zoo are the citable assets (novelty-options §3, niches-models N4).
"To our knowledge" is backed by research/novelty-options.md §3 (tight query "internal representations
predict the sim-to-real gap": 4 arXiv hits, none on topic; S2 0/0/0/1/3 for 2019-22/23/24/25/26) and
niches-map.md ranks 1-3; the weight-space-learning papers cited there (Schürholt et al. NeurIPS 2022; Navon
et al. ICML 2023; Zhou et al. NeurIPS 2023; Kofinas et al. ICLR 2024) do not address robot policies. §6
(rewritten by another worker) should carry the gap statement that supports it.
Venue list = coordinator decision, verified from the official 5.01.2024 xlsx (Lp: NeurIPS 87, ICML 847,
ICLR 1674, CVPR 417, ICCV 442, ECCV 331); RSS (Lp 1277) is dropped from the visible list because no paper
in pivot-decision.md targets it. Paper-to-venue mapping = pivot-decision.md "Papers". -->

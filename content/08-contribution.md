# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The dissertation is carried out in **information and communication technology** (*informatyka techniczna i
telekomunikacja*). Its contributions are learning algorithms, data-efficient training methodology,
software, data and evaluation methodology for machine learning in autonomous systems. The robot is the
test platform; control design and mechanical engineering are not the object of the research.

**Key original contribution (core, RQ1–RQ2, H1 + H4).** The first systematic, quantitative
characterization, to our knowledge, of how the deployed performance of learned mobile-robot navigation
policies depends on the **real-data budget** in a real-to-sim-to-real pipeline. It answers "how much real
data is enough" with measured budget–success-rate curves and a non-inferiority comparison against
policies trained on real robot experience. This is the result the dissertation stands on.

Contributions, in ITiT terms:

1. **Data-efficient training methodology (core; RQ2, H4).** A procedure for training navigation policies
   under an explicit real-data budget. It covers scene capture and a small number of real rollouts, and
   the budget–performance curves that quantify the trade-off.
2. **Software pipeline (core; RQ1, H1).** A reproducible, open real-to-sim-to-real pipeline that turns short
   RGB(-D) captures into interactive, photorealistic training environments (3D Gaussian Splatting for
   appearance, extracted geometry for collisions) inside a GPU simulator.
3. **Learning algorithm for generalization (extension; RQ3, H2).** A scheme for augmenting reconstructed
   scenes so that policies transfer to environments that were never captured. It connects the
   digital-twin and domain-randomization lines of research.
4. **Closed-loop simulation correction and evaluation methodology (extension; RQ4, H3).** A method to update
   simulation parameters from a few real rollouts, and a protocol for measuring how well simulation
   predicts real performance (SRCC, pre-specified margins and decision rules), so that sim-to-real
   claims can be tested rather than asserted.
5. **Data and benchmark (supports all RQs).** Released code, reconstructed environments and a real-world
   evaluation set with fixed start–goal pairs, supporting reproducible sim-to-real benchmarking.

**Significance for the discipline.** Collecting robot experience is the main cost of learning-based
robotics. Replacing most of it with cheap scene captures and simulation lowers the cost and time of
deploying learned systems in new environments. The evaluation methodology (item 4) is reusable for other
simulators and embodied-AI tasks.

**Dissemination.** Results are planned for venues assigned to ITiT on the ministerial list, e.g. IEEE
RA-L (200 pts) and IEEE/RSJ IROS (140 pts) (list of 5.01.2024), in line with §3 and §11.

<!-- Follows research/benchmarks.md edits 8 (mark core, "The key original contribution is …") and 16
(ITiT framing, prefer venues listed for ITiT; M1). "To our knowledge" is backed by the gap statement in §6
(none of [24]–[31] measures performance vs. amount of real data). Point values: 5.01.2024 list; a new
list is expected in early 2027, recheck then. -->

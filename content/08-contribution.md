# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The dissertation is carried out in **information and communication technology** (*informatyka techniczna i
telekomunikacja*), in the area of machine learning. Its object is a general, task-agnostic methodology for
learning embodied policies in **digital twins** built by neural reconstruction of real scenes (real → twin →
policy → real). Visual navigation is the primary testbed and robotic manipulation the generalization
domain; control design and mechanical engineering are not the object of the research.

**Key original contribution (core, RQ1–RQ2, H1 + H4).** The first systematic, quantitative
characterization, to our knowledge, of how performance of policies learned in **neural-reconstruction
twins** scales with the **real-data budget** of the target domain. It answers "how much real data is
enough" with measured budget–success-rate scaling curves and a non-inferiority comparison against learning
from real data alone, on public navigation benchmarks and validated on a real robot.

Contributions to machine learning methodology:

1. **Data-efficient learning under a real-data budget (core; RQ2, H4).** A training procedure that treats
   the amount of real target-domain data (captures and a few real rollouts) as an explicit budget, and
   scaling curves that quantify the trade-off between real data and deployed performance.
2. **Learning from reconstructed data (core; RQ1, H1).** Evidence of when training in photorealistic twins
   (3D Gaussian Splatting for appearance, extracted geometry for collisions) closes the distribution gap to
   real observations, compared with generic simulation and domain randomization.
3. **Cross-scene and cross-task generalization (extension; RQ3, H2).** Augmentation of reconstructed scenes
   combined with representation alignment between reconstructed and real observations, so that policies
   generalize to scenes that were never captured, and evidence that the same pipeline transfers from
   navigation to manipulation. It connects the digital-twin and domain-randomization lines of research.
4. **Closed-loop correction and evaluation methodology (extension; RQ4, H3).** A method to update the twin
   from a few real rollouts, and a protocol for measuring how well simulation predicts real performance
   (SRCC, pre-specified margins and decision rules), so that sim-to-real claims are tested, not asserted.

Contributions in engineering terms (ITiT):

5. **Digital-twin pipeline, software and data (supports all RQs).** A reusable, task-agnostic pipeline and
   protocol that turns a short RGB(-D) capture into a simulation-ready twin, with measured cost (capture
   minutes, compute hours) and fidelity metrics; released code, reconstructed scenes and evaluation sets
   with fixed episodes for reproducible sim-to-real benchmarking in navigation and manipulation.

**Significance for the discipline.** Target-domain data is the main cost of deploying learned systems.
Showing how far cheap captures and reconstruction can replace it, across tasks and embodiments, and which
representations make this work, is relevant to machine learning under distribution shift in general. The
evaluation methodology (item 4) is reusable for other simulators and embodied-AI tasks.

**Dissemination.** Results are planned for peer-reviewed conferences worth 200 points and assigned to ITiT
on the ministerial list of 5.01.2024: NeurIPS, ICML and ICLR (machine learning), CVPR, ICCV and ECCV
(computer vision), and RSS (robot learning), as in §3, §11 and §12; the cross-task (manipulation) study is
paper P3.

<!-- Wave 6 (issue #14), 2026-09-26: broadened to the general digital-twin methodology; item 3 now
cross-scene AND cross-task (navigation -> manipulation); item 5 makes the twin pipeline with measured cost
and fidelity a contribution in its own right (coordinator decision). P3 (sem. 6; ECCV 2028 / NeurIPS 2028,
or RSS) = cross-task paper; no extra papers. -->
<!-- Wave 5 (issue #11), 2026-09-26: reframed ML-first on the student's decision (AI/ML PhD; methodology
first, then ITiT-framed software/data). Venue list = coordinator decision (2), verified by the coordinator
from the official 5.01.2024 xlsx (Lp: NeurIPS 87, ICML 847, ICLR 1674, CVPR 417, ICCV 442, ECCV 331,
RSS 1277; AAAI 1227 and IJCAI 983 are also eligible but not named here). IROS/ICRA/CoRL/RA-L/RAS are no
longer targets. Details and deadlines: research/venues-200.md (issue #12). A new list is expected in early
2027; this is noted once in §12 (issue #12).
"To our knowledge" is backed by the §6 gap statement (issue #9 / review-1 F11: none of the navigation
systems [24]–[30], incl. EmbodiedSplat [30], varies the amount of real data; RialTo [23] does so only for
manipulation, 0–15 demos; full texts keyword-searched 2026-09-26). -->

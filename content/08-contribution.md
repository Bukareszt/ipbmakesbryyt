# §8 Wkład w rozwój dyscypliny / Contribution to the discipline (max 1 page)

The dissertation is carried out in **information and communication technology** (*informatyka techniczna i
telekomunikacja*), in the area of machine learning. Its contributions are learning methodology,
representation learning, evaluation methodology, software and data. Visual navigation of mobile robots is
the application and testbed; control design and mechanical engineering are not the object of the research.

**Key original contribution (core, RQ1–RQ2, H1 + H4).** The first systematic, quantitative
characterization, to our knowledge, of how performance of policies learned from **neural scene
reconstructions** scales with the **real-data budget** of the target domain. It answers "how much real
data is enough" with measured budget–success-rate scaling curves and a non-inferiority comparison against
learning from real data alone, on public benchmarks and validated on a real robot. This is the result the
dissertation stands on.

Contributions to machine learning methodology:

1. **Data-efficient learning under a real-data budget (core; RQ2, H4).** A training procedure that treats
   the amount of real target-domain data (captures and a few real rollouts) as an explicit budget, and
   scaling curves that quantify the trade-off between real data and deployed performance.
2. **Learning from reconstructed data (core; RQ1, H1).** Evidence of when training on photorealistic
   reconstructions (3D Gaussian Splatting for appearance, extracted geometry for collisions) closes the
   distribution gap to real observations, compared with generic simulation and domain randomization.
3. **Representation learning across the sim-real gap (extension; RQ3, H2).** Augmentation of reconstructed
   scenes combined with representation-alignment objectives between reconstructed and real observations,
   so that policies generalize to environments that were never captured. It connects the digital-twin and
   domain-randomization lines of research.
4. **Closed-loop correction and evaluation methodology (extension; RQ4, H3).** A method to update the
   simulation from a few real rollouts, and a protocol for measuring how well simulation predicts real
   performance (SRCC, pre-specified margins and decision rules), so that sim-to-real claims are tested
   rather than asserted.

Contributions in engineering terms (ITiT):

5. **Software and data (support all RQs).** An open, reproducible pipeline that turns short RGB(-D) video
   into interactive training environments inside a GPU simulator, and released code, reconstructed scenes
   and an evaluation set with fixed episodes for reproducible sim-to-real benchmarking.

**Significance for the discipline.** Target-domain data is the main cost of deploying learned systems.
Showing how far cheap captures and reconstruction can replace it, and which representations make this
work, is relevant to machine learning under distribution shift in general, not only to robotics. The
evaluation methodology (item 4) is reusable for other simulators and embodied-AI tasks.

**Dissemination.** Results are planned for peer-reviewed conferences worth 200 points and assigned to ITiT
on the ministerial list of 5.01.2024: NeurIPS, ICML and ICLR (machine learning), CVPR, ICCV and ECCV
(computer vision), and RSS (robot learning), as in §3, §11 and §12.

<!-- Wave 5 (issue #11), 2026-09-26: reframed ML-first on the student's decision (AI/ML PhD; methodology
first, then ITiT-framed software/data). Venue list = coordinator decision (2), verified by the coordinator
from the official 5.01.2024 xlsx (Lp: NeurIPS 87, ICML 847, ICLR 1674, CVPR 417, ICCV 442, ECCV 331,
RSS 1277; AAAI 1227 and IJCAI 983 are also eligible but not named here). IROS/ICRA/CoRL/RA-L/RAS are no
longer targets. Details and deadlines: research/venues-200.md (issue #12). A new list is expected in early
2027; this is noted once in §12 (issue #12).
"To our knowledge" is backed by the §6 gap statement (issue #9 / review-1 F11: none of the navigation
systems [24]–[30], incl. EmbodiedSplat [30], varies the amount of real data; RialTo [23] does so only for
manipulation, 0–15 demos; full texts keyword-searched 2026-09-26). -->

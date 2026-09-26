# §12 Inne / Other comments (max 1 page)

**Planned outputs by year** (points: ministerial list of 5.01.2024; the list signed in 2027 will apply
and will be re-checked).

| Year | Papers (venue, points) | Grants | Mobility, events |
|---|---|---|---|
| 1 (2025/26) | — | — | — |
| 2 (2026/27) | Stage I article, IEEE RA-L (200), Feb 2027, IROS 2027 option; fallback IROS (140) | SzD PWr Minigrant (next call); NCN Preludium (sem. 4) | International summer/winter school with a poster |
| 3 (2027/28) | Journal article, Robotics and Autonomous Systems (140) or RA-L (200); conference paper, RSS or CVPR/ICCV/ECCV (200) | NAWA Bekker (for the visit) | Mid-term evaluation; 1–3-month foreign research visit (sem. 6) |
| 4 (2028/29) | Summary journal article (IEEE T-RO or RA-L, 200) | — | Release of code, scenes and evaluation data; dissertation |

**Foreign research visit (candidate hosts, not yet contacted).** (1) *Multi-robot Systems Lab*, Stanford
University (M. Schwager), which works on Gaussian-splatting scene models, sim-to-real and navigation.
(2) *Zsolt Kira's group*, Georgia Tech, co-authors of EmbodiedSplat (ICCV 2025), a real-to-sim-to-real
indoor-navigation method using Gaussian splats. The host is chosen in sem. 4 with the supervisor.

**Collaboration at PWr.** K46 has no mobile-robot laboratory, so the real-robot experiments are planned in
cooperation with the *Denali* Autonomous Robots Laboratory of the Department of Cybernetics and Robotics
(K29, W12N): Pioneer 3-DX robots on ROS 2 and a Jaguar 4x4 platform. The terms are to be agreed in sem. 3.
Consultations on 3D scene reconstruction with K46's genwro.AI group (generative models, 3D; head
M. Zięba) are possible.

**Risks and mitigation** (semester affected).
- *Delayed hardware or lab access* (3–4): early work on public real-world navigation datasets and
  simulation; a Minigrant or Preludium budget for our own sensors or a small platform.
- *Dependence on an external lab or partner* (3–6): a written agreement with K29 by sem. 3; the pipeline
  is kept platform-agnostic (ROS 2) so it can move to another robot; the foreign visit has two candidate
  hosts.
- *Sim-to-real validation fails* (4–5): a pre-specified protocol (paired sim/real rollouts, SRCC);
  if the gap is not closed, the budget–performance study is reported as a negative result, which is
  still publishable and keeps the core contribution (RQ2).
- *Poor reconstruction in low-texture or large scenes* (3–4): depth/LiDAR priors, scene segmentation,
  fallback to mesh rendering.
- *Changing venue points* (3): re-check the 2027 list; keep a 140/200-point alternative.

**Prior work (background only).** Before the programme, the candidate co-authored an NLP paper on learning
from internal representations of large language models (ACL 2025 Student Research Workshop). It gives
methodological experience (representation learning, graph neural networks) but is not part of the
dissertation.

**Ethics and data.** Real-world captures in public spaces will avoid personal data or be anonymized
(blurred faces) in line with GDPR and PWr rules.

<!--
Revision for issue #6 (research/benchmarks.md edits 12, 13, 14, 15, 20; research/resources.md).
Sources:
- Points: Komunikat MNiSW 5.01.2024 (benchmarks.md M1, resources.md §3): RA-L 200, T-RO 200, RSS 200,
  CVPR/ICCV/ECCV 200, RAS 140, IROS 140. ICRA (70) and CoRL (not listed) deliberately not used as targets.
  New list expected early 2027 (benchmarks.md M3).
- Minigranty SzD: https://szd.pwr.edu.pl/doktoranci/minigranty (up to 20k PLN, years 2–4; next edition
  ~Jan 2027 UNVERIFIED).
- Preludium 26 timing (~Mar–Jun 2027) is inferred from previous calls, UNVERIFIED (resources.md §4).
- NAWA Bekker: open to doctoral-school students; next call UNVERIFIED (resources.md §5). Erasmus+ is not
  listed for the visit because both candidate hosts are in the USA.
- Host 1: https://msl.stanford.edu/ (checked 2026-09-26: Multi-robot Systems Lab, Stanford Aero/Astro,
  directed by Mac Schwager; projects Splat-Nav, GRaD-Nav++, SAFER-Splat, Phys2Real).
- Host 2: https://arxiv.org/abs/2509.17430 (EmbodiedSplat, ICCV 2025; G. Chhablani, X. Ye,
  M. Z. Irshad, Z. Kira; affiliations Georgia Tech / Toyota Research Institute, checked 2026-09-26).
  Neither host has been contacted; willingness to host is UNVERIFIED.
- K29 Denali: https://denali.kcir.pwr.edu.pl/robots.php ; K46 has no robotics group:
  https://ai.pwr.edu.pl/research-groups (resources.md §1). Collaboration not yet agreed; confirm with the
  supervisor before signing.
- genwro.AI: https://ai.pwr.edu.pl/research-groups ("modele generatywne, modele dyfuzyjne, widzenie
  komputerowe"; subtitle mentions "3D"). No verified 3DGS work, so it is phrased only as "3D scene
  reconstruction consultations are possible". The 2023-cohort 3DGS doctoral topic (benchmarks.md R5
  p. 20–21) is NOT named because its group/supervisor attribution is UNVERIFIED.
- ACL SRW paper: doi:10.18653/v1/2025.acl-srw.61; pre-PhD, so it is background only (edit 15, S9).
Word count ≈ 480 incl. table; check at 11 pt / spacing 1 after transfer to ipb.docx.
-->

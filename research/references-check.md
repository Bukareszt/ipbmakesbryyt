# §6 reference verification log

Scope: every reference in `content/06-state-of-the-art.md` (GitHub issue #2).
Checked on 2026-09-26 by title search against **OpenAlex** (`api.openalex.org/works?search=`), the
**arXiv API** (`export.arxiv.org/api/query`) and **Crossref** (`api.crossref.org/works`), plus the
publisher/proceedings page where the venue was not in the metadata. DBLP returned a bot-check page and
Semantic Scholar returned HTTP 429 during this session, so neither was used.

Verdicts: **OK** = authors, title, venue and year match. **FIXED** = an error was corrected (details given).
**OK (preprint)** = only an arXiv record could be confirmed, and the reference is cited as arXiv.

## Existing references [1]–[25]

| # | Reference (short) | Verdict | Source URL(s) | Notes |
|---|---|---|---|---|
| 1 | Savva et al., Habitat, ICCV 2019 | OK | https://doi.org/10.1109/ICCV.2019.00943 · https://arxiv.org/abs/1904.01201 | |
| 2 | Szot et al., Habitat 2.0, NeurIPS 2021 | OK | https://proceedings.neurips.cc/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html · https://arxiv.org/abs/2106.14405 | |
| 3 | Dosovitskiy et al., CARLA, CoRL 2017 | OK | https://proceedings.mlr.press/v78/ · https://arxiv.org/abs/1711.03938 | PMLR vol. 78 |
| 4 | Shah et al., AirSim, FSR 2017 | OK | https://doi.org/10.1007/978-3-319-67361-5_40 · https://arxiv.org/abs/1705.05065 | Published in Springer Proceedings in Advanced Robotics (FSR 2017), print year 2018 |
| 5 | Wijmans et al., DD-PPO, ICLR 2020 | OK | https://iclr.cc/virtual_2020/poster_H1gX8C4YPr.html · https://arxiv.org/abs/1911.00357 | Abstract confirms 2.5 billion steps and "essentially solves" PointGoal nav |
| 6 | Shah et al., GNM, ICRA 2023 | OK | https://doi.org/10.1109/ICRA48891.2023.10161227 · https://arxiv.org/abs/2210.03370 | |
| 7 | Shah et al., ViNT, CoRL 2023 | OK | https://arxiv.org/abs/2306.14846 | arXiv comment: "Accepted for oral presentation at CoRL 2023" (PMLR v229) |
| 8 | Sridhar et al., NoMaD, ICRA 2024 | OK | https://doi.org/10.1109/ICRA57147.2024.10610665 · https://arxiv.org/abs/2310.07896 | |
| 9 | Open X-Embodiment Collaboration, ICRA 2024 | OK | https://doi.org/10.1109/ICRA57147.2024.10611477 · https://arxiv.org/abs/2310.08864 | |
| 10 | Zhao, Peña Queralta, Westerlund, SSCI 2020 | OK | https://doi.org/10.1109/SSCI47803.2020.9308468 · https://arxiv.org/abs/2009.13303 | |
| 11 | Höfer et al., IEEE T-ASE 2021 | OK | https://doi.org/10.1109/TASE.2021.3064065 | |
| 12 | Kadian et al., Sim2Real Predictivity, RA-L 2020 | FIXED (text) | https://doi.org/10.1109/LRA.2020.3013848 · https://arxiv.org/abs/1912.06321 | Reference correct. The body called the metric "Sim2Real Correlation Coefficient"; the abstract says **Sim-vs-Real Correlation Coefficient (SRCC)**. Body corrected. |
| 13 | Truong et al., Rethinking Sim2Real, CoRL 2022 | OK | https://proceedings.mlr.press/v205/ · https://arxiv.org/abs/2207.10821 | Claim ("lower fidelity transfers better for navigation") matches the abstract |
| 14 | Tobin et al., Domain Randomization, IROS 2017 | OK | https://doi.org/10.1109/IROS.2017.8202133 · https://arxiv.org/abs/1703.06907 | |
| 15 | Tremblay et al., CVPR Workshops 2018 | OK | https://doi.org/10.1109/CVPRW.2018.00143 · https://arxiv.org/abs/1804.06516 | |
| 16 | Peng et al., Dynamics Randomization, ICRA 2018 | OK | https://doi.org/10.1109/ICRA.2018.8460528 · https://arxiv.org/abs/1710.06537 | |
| 17 | Loquercio et al., High-Speed Flight in the Wild, Sci. Robot. 2021 | OK | https://doi.org/10.1126/scirobotics.abg5810 · https://arxiv.org/abs/2110.05113 | |
| 18 | Kaufmann et al., Champion-level drone racing, Nature 2023 | OK | https://doi.org/10.1038/s41586-023-06419-4 | |
| 19 | Chebotar et al., Closing the Sim-to-Real Loop, ICRA 2019 | OK | https://doi.org/10.1109/ICRA.2019.8793789 · https://arxiv.org/abs/1810.05687 | |
| 20 | Bousmalis et al., Sim + Domain Adaptation for Grasping, ICRA 2018 | OK | https://doi.org/10.1109/ICRA.2018.8460875 · https://arxiv.org/abs/1709.07857 | |
| 21 | Rusu et al., Progressive Nets, CoRL 2017 | OK | https://proceedings.mlr.press/v78/ · https://arxiv.org/abs/1610.04286 | arXiv 2016, published at CoRL 2017 (PMLR v78) |
| 22 | Mildenhall et al., NeRF, ECCV 2020 | OK | https://doi.org/10.1007/978-3-030-58452-8_24 · https://arxiv.org/abs/2003.08934 | |
| 23 | Kerbl et al., 3D Gaussian Splatting, ACM TOG 2023 | OK | https://doi.org/10.1145/3592433 · https://arxiv.org/abs/2308.04079 | ACM TOG 42(4), SIGGRAPH 2023 |
| 24 | Byravan et al., NeRF2Real, ICRA 2023 | OK | https://doi.org/10.1109/ICRA48891.2023.10161544 · https://arxiv.org/abs/2210.04932 | |
| 25 | Torne Villasevil et al., RialTo, RSS 2024 | FIXED (minor) | https://doi.org/10.15607/RSS.2024.XX.015 · https://arxiv.org/abs/2403.03949 | First author appears as "Marcel Torne Villasevil" in the RSS record and as "Marcel Torne" on arXiv, so the full surname is now used. The body claim "only a few real demonstrations" was reworded to match the abstract ("constructed ... from small amounts of real-world data"). |

## Added references [26]–[31] (2024–2026, real-to-sim(-to-real) for navigation)

| # | Reference | Verdict | Source URL(s) | Claim used in §6 (from abstract) |
|---|---|---|---|---|
| 26 | A. Quach et al., "Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks," arXiv 2024 | OK (preprint) | https://arxiv.org/abs/2406.15149 | Builds a 3DGS + quadrotor-dynamics simulator and transfers navigation learned in a single sim scene directly to the real world. The peer-reviewed venue was not found in OpenAlex or Crossref (UNVERIFIED), so it is cited as arXiv. |
| 27 | J. Low et al., "SOUS VIDE: …," IEEE RA-L 2025 | OK | https://doi.org/10.1109/LRA.2025.3553785 · https://arxiv.org/abs/2412.16346 | GS-based simulator (FiGS) and zero-shot sim-to-real visual drone navigation |
| 28 | Q. Chen et al., "GRaD-Nav: …," IROS 2025 | OK | https://doi.org/10.1109/IROS60139.2025.11247514 · https://arxiv.org/abs/2503.03984 | 3DGS + differentiable dynamics, zero-shot sim-to-real drone navigation |
| 29 | S. Zhu et al., "VR-Robo: …," IEEE RA-L 2025 | OK | https://doi.org/10.1109/LRA.2025.3575648 · https://arxiv.org/abs/2502.01536 | 3DGS digital twin with mesh-based physics, RGB-only sim-to-real transfer for legged visual goal-tracking |
| 30 | Z. Xie et al., "Vid2Sim: …," CVPR 2025 | OK | https://doi.org/10.1109/CVPR52734.2025.00155 · https://arxiv.org/abs/2501.06693 | Monocular video → interactive sim for urban navigation. Abstract: success rate +31.2% (digital twins) and +68.3% (real world) vs. prior simulation methods |
| 31 | S. Yoo et al., "ReaDy-Go: …," IEEE RA-L 2026 | OK | https://doi.org/10.1109/LRA.2026.3707355 · https://arxiv.org/abs/2602.11575 | Dynamic GS simulator with animatable human avatars for navigation with moving obstacles. Crossref issue date 2026-08. |

Candidates checked but not added (to stay within the page limit): Adamkiewicz et al., "Vision-Only Robot
Navigation in a Neural Radiance World," RA-L 2022 (https://doi.org/10.1109/LRA.2022.3150497), which is
from before 2023; Chen et al., "Splat-Nav," T-RO 2025 (https://doi.org/10.1109/TRO.2025.3552348), which
covers planning in GS maps rather than policy training; Cai et al., "NavDP," arXiv 2025
(https://arxiv.org/abs/2505.08712); and Gervet et al., "Navigating to objects in the real world," Sci.
Robot. 2023 (https://doi.org/10.1126/scirobotics.adf6991).

## Interpretive statements in §6 (not directly citable)
- "to our knowledge, none measures how deployed performance depends on the amount of real data collected".
  This is the author's reading of [24]–[31] from their abstracts, not a verified fact. The supervisor
  should confirm it after reading the full papers.

## Size check
Body (excluding heading and reference list): 523 words. References: 31 (limit ≤ 32).

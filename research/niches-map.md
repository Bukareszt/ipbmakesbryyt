# Nearby, less-crowded niches: combined map (wave 8, 2026-09-26)

Sources: [niches-data.md](niches-data.md) (#19), [niches-eval.md](niches-eval.md) (#20),
[niches-models.md](niches-models.md) (#21), [novelty-options.md](novelty-options.md) (#18). The counts are
Semantic Scholar bulk-search hits for 2023/24/25/26 (2026 through 26 Sep). The arXiv API rate-limited us
(HTTP 429), so the arXiv counts are partial. Scores are judgement calls: Dist = distance to the current
topic (0 = same, 3 = far); Fit = fit to the student (0–3).

## Ranked shortlist (open or emerging, distance ≤ 1, fit ≥ 2)

| Rank | Niche | Side | S2 23/24/25/26 | Verdict | Dist | Fit | Robot needed? |
|---|---|---|---|---|---|---|---|
| 1 | **Forecast twin→real transfer from policy internals** (weights / hidden states over a policy zoo) | eval + models | 0/0/1/3 (2024/25/26: 0/1/3) | Open | 1 | 3 | No |
| 2 | **Localize the sim-vs-real gap inside the policy** (layer-wise probing, representational similarity, patching) | models | 0/0/1/0 (tight) | Open (VLA interpretability in general is active: 93 in 2026) | 1 | 3 | No |
| 3 | **Frozen-encoder robustness to reconstruction artifacts** (paired real vs. 3DGS-rendered frames, graded capture budget) | models | 1/2/3/1 | Open, 83 % ML venues | 1 | 3 | No |
| 4 | **Twin-trained hidden-state failure monitors that stay calibrated on real data** | eval | 0/5/4/10 | Active in general, open for twin→real | 1 | 3 | Partly (real datasets suffice) |
| 5 | **Representation-guided weighting of twin data** by distance to a small real set | data | 0/0/1/0 | Open | 1 | 3 | No |
| 6 | **Twin→real data attribution** (which captured scenes or frames cause real success or failure) | data | 0/0/2/4 (robot attribution) | Emerging; the cross-boundary version is open | 1 | 3 | No |
| 7 | **Reconstruction uncertainty → calibrated uncertainty of the twin's success estimate** | eval | 0/0/3/4 | Open | 1 | 2 | No |
| 8 | Prediction-powered estimates of real success (many twin rollouts + few real) | eval | 1/0/2/1 | Emerging fast (SureSim, X4Val, PERRY…) | 1 | 2 | Partly |
| 9 | Merging per-scene twin-trained policies | models | 1/1/4/10 | Emerging | 1 | 3 | No |

**Avoid (crowded or far):**
- LLM/VLM agents that build twins (39–47 per year).
- Probing video world models (46 in 2026).
- Test-time adaptation (35).
- Curation of large robot datasets (Stanford/Berkeley/TRI).
- Hypernetworks.
- Twin-vs-generic-simulator transfer (H1a).
- Representation alignment for domain adaptation (H2 as currently phrased).

## Pattern: one coherent thesis from the top niches

Niches 1–6 are the same object seen from different angles: **the representations of twin-trained
policies as the bridge between twin and reality.** Together they give one thesis, three papers, and no
dependence on owning a robot:

> *The real-world transfer of embodied policies trained in neural-reconstruction digital twins can be
> measured, localized and predicted from their internal representations, and this makes it possible to
> spend a limited real-data budget where it matters.*

| Paper | Niches | Venue fit |
|---|---|---|
| P1 (NeurIPS 2027) | 3 + 2: benchmark of paired real and twin frames; where in encoders and policies the gap lives | NeurIPS D&B / CVPR |
| P2 (ICLR/CVPR 2028) | 1 + 4: forecasting transfer and failure from hidden states and weights over a policy zoo | ICLR / NeurIPS |
| P3 (NeurIPS/ECCV 2028) | 5 + 6 (+ 7): using the forecasts to weight or attribute twin data and to choose what to capture or collect; manipulation as the cross-task test | ICML / NeurIPS |

The current plan's open parts stay in as the experimental backbone:
- the real-data-budget curves (H1b/H4),
- predictivity (H3), with a world model as a third comparator.

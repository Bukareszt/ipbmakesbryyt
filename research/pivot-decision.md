# Pivot decision (student, 2026-09-26): representation-level thesis

Based on research/niches-map.md. This file is the single source of truth for waves 9–10.

**Thesis.** How well embodied policies trained in neural-reconstruction digital twins transfer to the real
world can be **measured, localized and predicted from their internal representations**, and this lets a
limited real-data budget be spent where it matters.

**Object.** A policy is trained in a twin: a 3DGS reconstruction built from a short real capture. It is
then deployed in reality. Navigation is the primary testbed; manipulation is the cross-task test. The
student builds on existing twin pipelines and simulators and does not develop new ones.

## Research questions and hypotheses (numbering fixed)

**RQ1 (measure and localize).** Where inside frozen encoders and twin-trained policies does the twin-vs-real
gap arise, and how does it depend on the capture budget?
- **H1.** On paired real and twin-rendered frames (same pose), the representation gap is concentrated in
  identifiable layers and decreases monotonically with the capture budget. The gap is measured by linear
  CKA and by the linear-probe accuracy drop. Frozen encoders differ significantly in their robustness to
  reconstruction artifacts, and this robustness ranking predicts downstream twin→real transfer (Spearman
  ρ ≥ 0.6).

**RQ2 (predict).** Can a twin-trained policy's real-world transfer and failures be forecast from its
internals (hidden states, weights) without real rollouts?
- **H2.** Consider a predictor trained on a policy zoo: a GNN over layers or a weight-space metanetwork.
  On held-out scenes it predicts the twin→real success-rate gap with at least 20% lower MAE than the
  baselines: twin SR alone, image fidelity (PSNR/LPIPS), and simulator-level predictivity. In addition,
  hidden-state failure monitors calibrated in the twin keep their conformal coverage on real data within
  ε = 5 pp.

**RQ3 (use).** Can these measures and predictions allocate a limited real-data budget? That is: which twin
data to weight, what to capture, and which real rollouts to collect.
- **H3.** Forecast-guided twin-data weighting, capture and rollout selection reaches a target real SR with
  at least 30% less real data (capture minutes + real rollouts) than uniform or random allocation. The
  evidence is budget–performance curves, which absorb the former H1(b)/H4.

**RQ4 (generalize).** Do the gap measures and predictors transfer across tasks and simulator families?
- **H4.** A predictor trained on the navigation zoo keeps its ranking ability on manipulation (Spearman
  ρ ≥ 0.5). Representation-based prediction also predicts real outcomes better than two alternatives:
  simulator-level SRCC of a generic simulator, and a learned world-model evaluator.

All thresholds are design choices for the supervisor to confirm.

## Evaluation tiers (unchanged idea)
- **A:** proxy reality on public real scans with twins (e.g. ScanNet++). This tier decides the hypotheses.
- **B:** real-world datasets or published real evaluations with paired real outcomes.
- **C:** real-robot validation (planned K29 Denali collaboration). Validation only.

## Papers (200-pt ITiT conferences only)
- **P1:** NeurIPS 2027 (May 2027, §11). RQ1: a benchmark of paired real and twin frames, plus localization
  of the gap. Datasets & Benchmarks or main track; alternative CVPR 2028.
- **P2:** ICLR 2028 or CVPR 2028 (sem. 5). RQ2: forecasting transfer and failure from internals.
- **P3:** NeurIPS 2028 (sem. 6), fallback ICLR 2029 (ECCV 2028 dropped in review-2: results not ready by March 2028). RQ3 + RQ4: budget allocation and cross-task transfer
  (manipulation).
- **P4 (optional):** ICLR 2029 or CVPR 2029 (sem. 7). Consolidated study.

## Scope
- Semesters 1–2 in §3 stay as they are. T2.1 wording may be adapted to the new RQs.
- World models appear only as a comparator (H4) and a source of frozen features.
- No development of twin simulators.

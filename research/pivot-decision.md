# Pivot decision v2 (student, 2026-09-26): data-efficient real-to-sim-to-real

Supersedes v1 (the representation-level thesis). **No benchmark building.** The object of research is the
real-to-sim-to-real loop itself, and how to make it work with **less real data**. Representations and
uncertainty are *tools* inside the methods, not the object.

**Thesis.** The real data needed in a real-to-sim-to-real loop can be reduced substantially by *allocating it
actively*: capture only what the policy needs to build the twin, train so that the policy is robust to what
the twin got wrong, and collect only the few real rollouts that close the remaining gap. All three steps are
guided by reconstruction uncertainty and by the policy's own representations.

**Loop.** Real capture → twin (3DGS reconstruction, using existing tools) → policy training in the twin →
a few real rollouts → twin/policy correction → deployment. Navigation is the primary testbed; manipulation
is the cross-task test.

**Why this is open** (research/niches-data.md, niches-eval.md, niches-models.md; Semantic Scholar hits per
year 2023/24/25/26):
- Task-aware capture for twins: 2/2/0/2.
- Active selection of real rollouts in the twin setting: open.
- Representation-guided weighting of twin data: 0/0/1/0.
- Reconstruction uncertainty as a training signal: 0/0/1/1.
- Real-data-budget curves for navigation: none published (crowdedness.md).

**What to avoid, because it is crowded:** "twin beats generic simulator", generic domain adaptation, building
twin simulators, and building benchmarks.

## Research questions and hypotheses (numbering fixed; thresholds for the supervisor to confirm)

**RQ1 (real → sim: capture less).** How little capture data is needed to build a twin that is good enough
for policy learning, and can the capture be guided by the task?
- **H1.** Task-aware, uncertainty-guided capture (views chosen where the policy's task-relevant regions have
  high reconstruction uncertainty) reaches the same downstream success rate as uniform capture with at least
  40% less capture (minutes or views).

**RQ2 (in sim: train robustly on an imperfect twin).** How should a policy be trained so that it is robust to
the twin's reconstruction errors?
- **H2.** Uncertainty-aware training (augmentation and sample weighting driven by per-region reconstruction
  uncertainty and by the representation distance to a small real set) improves real transfer over uniform
  domain randomization, at an equal capture budget, by at least 10 pp success rate.

**RQ3 (sim → real: collect few real rollouts).** Which few real rollouts should be collected to close the
remaining gap, and how should they be used to correct the twin and the policy?
- **H3.** Real rollouts selected actively (by predicted gap or uncertainty) reach the target success rate
  with at least 50% fewer real rollouts than random selection.

**RQ4 (whole loop: budget and generalization).** What is the total real-data budget of the full loop,
compared with real-data-only learning, and does it hold beyond navigation?
- **H4.** The full loop reaches the target success rate with at most 10% of the real data needed by
  real-only learning (an "exchange rate" budget curve), and the method carries over to manipulation with
  the pipeline unchanged.

## Evaluation (no own benchmark)
- **Tier A: proxy reality.** Use existing public real scans (e.g. ScanNet++). A full-capture, high-fidelity
  twin plays "reality", and a low-budget twin is the training simulator. This makes it possible to count
  "real data" precisely without a robot. This tier decides the hypotheses.
- **Tier B: real-world datasets.** Existing datasets and published paired sim/real results.
- **Tier C: real-robot validation.** Planned K29 Denali collaboration, plus own phone or RGB-D captures of
  PWr rooms. Validation only.

## Papers (200-point ITiT conferences only)
- **P1: NeurIPS 2027** (May 2027, §11). RQ1 + RQ2: task-aware capture and uncertainty-aware training.
- **P2: ICLR 2028 or CVPR 2028** (semester 5). RQ3: active real-rollout selection and twin correction.
- **P3: NeurIPS 2028** (semester 6; fallback ICLR 2029). RQ4: full-loop budget law and manipulation.
- **P4 (optional):** consolidation.

## Scope
- Semesters 1–2 in §3 stay as they are; the T2.1 wording may be adapted.
- World models appear only as a comparator where relevant (e.g. H4 baseline), with no training.
- No benchmark or simulator development. The student builds on existing tools.

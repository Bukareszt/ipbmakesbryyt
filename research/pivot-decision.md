# Decision v5 (student, 2026-09-26): the method uses VLA/VLM and world models, sim-first, fine-tuned in the twin

**v5 overrides v4 on the method content. The goal, thesis and scope stay as in v4/v3:** one method that needs
**less real data**; general real-to-sim-to-real; manipulation and navigation as equal testbeds.

**Core idea.** Run everything in simulation. A **pretrained VLA policy** (open weights, e.g. OpenVLA, Octo,
π0-family) is **fine-tuned in the digital twin**. A **world model** grounded in the twin, and a **VLM**, make
the most of the twin, so that very little real data is needed.

**Components (numbering kept):**
- **C1 (real → twin: capture less).** A VLM identifies the task-relevant objects and regions from the
  instruction and scene. Capture is guided to them by the twin's uncertainty. The twin is built by neural
  reconstruction plus system identification.
- **C2 (learn in the twin: sim-first fine-tuning).** The VLA is fine-tuned in the twin with RL and imitation
  learning, using parameter-efficient methods such as LoRA. A **world model grounded in the twin** (trained
  or adapted on twin data) generates additional variations and covers the regions where the twin is
  uncertain. The VLM can serve as a success or reward judge in simulation. Training is uncertainty-aware.
- **C3 (twin → real: few real data).** The twin, the world model and the VLA's own uncertainty predict where
  sim and real disagree. Only those few real data or trials are collected, and they are used to correct the
  twin and world model and to fine-tune the VLA.

**Hypotheses.** H1–H4 keep their numbering and meaning. H4 (the thesis) compares the method with (a)
real-only fine-tuning of the same VLA and (b) the strongest existing sim or twin fine-tuning pipeline for
VLAs (verify which: e.g. RL fine-tuning of VLAs in simulation, SIMPLER-style twins). H2 also covers: "twin +
world model" beats "twin only" at an equal real-data budget.

**Novelty guardrail.** RL fine-tuning of VLAs in simulation and world-model-based VLA training are
**crowded** (2025–2026). Do not claim either as new. Novelty = **the real-data budget of the whole loop**:
task-aware capture for VLA fine-tuning, a twin-grounded world model to cover twin uncertainty, active
selection of real data, and the measured ≥ 2× saving versus existing pipelines.

**Feasibility.** Parameter-efficient fine-tuning of open ~7B VLAs on WCSS/PLGrid GPUs (verify the published
compute requirements). Existing world-model checkpoints are adapted, not trained from scratch. Tier B
SIMPLER provides real/sim paired evaluations of open VLAs, which fits this setup exactly.

---
(v4 below: goal, thesis and framing stay valid)

# Decision v4 (student, 2026-09-26): the goal is ONE METHOD that needs LESS real data

**v4 overrides v3/v2 on framing. Scope from v3 is unchanged:** general, domain-agnostic
real-to-sim-to-real; manipulation and navigation as equal testbeds; twins include physical parameters.

**Goal of the dissertation (cel pracy).** To develop **a method** for learning in the real-to-sim-to-real
loop that reaches a given real-world performance with **significantly less real data** than existing
approaches.

**Method.** The method is one pipeline with three components, one per loop step:
- (C1) task-aware, uncertainty-guided capture for building the twin;
- (C2) uncertainty-aware learning in the imperfect twin;
- (C3) active selection of a few real-world data or trials to correct the twin and the model.

The components are parts of the method. They are not separate contributions.

**Thesis (main hypothesis).** The proposed method reaches the target real-world success rate with
(a) at most 10% of the real data needed by learning from real data only, and (b) at least 2× less real
data than the strongest existing real-to-sim-to-real pipeline. That baseline is uniform capture + domain
randomization + random real-data selection, RialTo-style. The claim must hold in both testbeds.
<!-- (b) is new in v4: CONFIRM with the supervisor -->

**RQ/H mapping (numbering kept):**
- RQ1–RQ3 / H1–H3: how much each component C1–C3 saves at its own step (ablations of the method).
- RQ4 / H4: the whole method, i.e. the thesis above, in both domains.

**Framing rules:**
- Budget curves, the proxy-reality protocol and the code are **how the method is evaluated and
  released**. They are not contributions in their own right.
- The key original contribution in §8 is **the method**.
- Title, goal (§5, §7), contributions (§8) and abstracts (§10) must say plainly that the dissertation
  develops a method that needs less real data.

---
(v3 below: its scope stays valid)

# Pivot decision v3 (student, 2026-09-26): GENERAL data-efficient real-to-sim-to-real

**v3 overrides v2 on scope.** The research is about **real-to-sim-to-real in general**, not about navigation,
driving, autonomy or robot "rollouts" in particular. The object is a **task- and domain-agnostic methodology**:
building a simulation (digital twin) from limited real data, learning a policy or model in it, and transferring
it back to reality with limited real data.

- **Wording:**
  - "real rollouts" → "real-world data / interactions / trials";
  - "navigation policy" → "policy or model learned in the twin".
- **Testbeds (at least 2, equal status; none is "primary"):** robotic manipulation and visual navigation. Pick
  others only if verified public data exist. The methodology must not rely on task-specific components.
- **What the twin contains:** geometry and appearance (neural reconstruction) **and**, where relevant,
  physical and dynamic parameters identified from real data (system identification). "Capture less" covers
  both kinds of real data.
- **Hypotheses:** RQ1–RQ4 / H1–H4 keep their loop structure, numbering and thresholds, but are stated
  domain-agnostically:
  - H1: less real data to build the twin;
  - H2: robust learning in an imperfect twin;
  - H3: few, actively selected real-world data or interactions to correct the twin and the policy;
  - H4: the whole-loop budget law holds across **both** domains.
- **Evaluation tiers:** keep the review-3 protocol (a non-circular reference from a separate high-fidelity
  source) as a *pattern*. Apply it in each domain using verified public datasets.
- **Unchanged:** papers P1–P3 and their venues. No benchmark building. No simulator development. Semesters
  1–2 unchanged.

---
(v2 text below, still valid except where v3 overrides it)

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
- **P2: ICML 2028** (semester 5, ~Jan 2028; moved in review-3 so results exist before submission). RQ3: active real-rollout selection and twin correction.
- **P3: NeurIPS 2028** (semester 6; fallback ICLR 2029). RQ4: full-loop budget law and manipulation.
- **P4 (optional):** consolidation.

## Scope
- Semesters 1–2 in §3 stay as they are; the T2.1 wording may be adapted.
- World models appear only as a comparator where relevant (e.g. H4 baseline), with no training.
- No benchmark or simulator development. The student builds on existing tools.

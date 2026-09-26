# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**Thesis.** Embodied policies learned in a digital twin reconstructed from a small budget of real
observations, with aligned representations, perform in the target
domain not worse than policies learned from ≥ 10× more real data, and the method transfers across scenes
and tasks. Visual navigation is the primary testbed; robotic manipulation tests generalization.

**Core and extensions.** The dissertation stands on **RQ1–RQ2 with H1 and H4** (real-data budget,
navigation). RQ3/H2 (cross-scene and cross-task generalization) and RQ4/H3 (correction,
predictivity) are extensions.

**RQ1.** Does training an embodied policy in a twin built from minutes of real video of the target scene
(*real-to-sim*), then deploying it on real observations (*sim-to-real*), close the appearance and geometry gap?
**RQ2.** How does target-domain performance scale with the real-data budget, and what budget suffices
compared with learning from real data alone?
**RQ3.** Which augmentation and representation-alignment objectives let policies generalize to scenes that
were *not* captured and to another task and embodiment (navigation → manipulation)?
**RQ4.** Can a few real rollouts correct the twin so that it predicts real performance?

**Evaluation.** *Navigation:* (A, primary) ≥ 10 public indoor scenes with real video and a reference 3D
scan that serves as the target domain ("proxy reality"), some held out as uncaptured; (B) real-world
datasets for representation metrics; (C) real-robot validation in ≥ 2 PWr environments, 20 start–goal pairs
× 3 trials per policy. Metrics: success rate (SR; primary), SPL, collisions. *Manipulation:* tabletop
pick-and-place in twins of public scenes and objects in a public simulator; metric: task SR. *Budget* B =
minutes of target-domain data (capture plus real experience). Baselines: a pretrained policy fine-tuned by
behaviour cloning on target-domain data of budget B (*real-data-only*), and the same policy trained with
domain randomization on generic scenes (*generic*). Tests: one-sided (α = 0.05), bootstrapped over scenes
or start–goal pairs, Holm-corrected per hypothesis, pre-registered in the repository.

**H1 (RQ1, core).** A navigation policy trained only in the twin (a) beats the generic baseline in SR and
(b) is **non-inferior** to the real-data-only baseline with a ≥ 10× larger budget: the lower 95% bound of
SR_twin − SR_real is above −10 pp on tier A and above −15 pp on tier C (120 pooled episodes per policy;
≈ 90% power at SR ≈ 0.8).

**H2 (RQ3).** In uncaptured navigation scenes, and in manipulation with an unchanged pipeline,
twin + augmentation + representation alignment reaches a higher SR than the twin alone and than the generic
baseline, and alignment lowers the feature distance between reconstructed and real frames (tier B).

**H3 (RQ4).** Over ≥ 10 navigation policy variants, the Sim-vs-Real Correlation Coefficient (SRCC) of the
twin is higher than that of a generic simulator (95% CI of the difference excludes 0) and does not drop
after refinement from real rollouts (lower 95% bound of the change ≥ −0.1).

**H4 (RQ2, core).** The full pipeline reaches a target navigation SR τ (best real-data-only SR minus 10 pp)
with B_pipeline(τ) ≤ 0.1 · B_real(τ): the upper 95% bound of the ratio, from fitted budget–SR scaling
curves, is ≤ 0.1. If real-data-only training misses τ within the largest
feasible budget, the ratio is reported as a bound.

<!-- Wave 6 (issue #14), 2026-09-26: broadened on the coordinator's decision. RQ1/RQ2 phrased for
"embodied policies"; H1, H3, H4 stay decided on navigation (tiers A/B/C unchanged). RQ3/H2 broadened to
cross-scene AND cross-task (navigation -> manipulation) generalization. Manipulation = public simulators and
benchmarks first (concrete simulator/benchmark chosen in §9); real validation at PWr optional (K29
Laboratorium Robotyki manipulators UR3/FANUC/ABB, availability UNVERIFIED), so no manipulation tier C is
promised. "SR_recon" renamed "SR_twin". Evaluation paragraph compacted to keep the 1-page limit
(tier A/C baselines and Holm correction unchanged in substance). -->
<!-- Wave 5 (issue #11), 2026-09-26: reframed ML-first on the student's decision (AI/ML PhD, navigation =
testbed; main evaluation on public simulators/benchmarks and real-world datasets; the real robot = validation
subset, which reduces hardware risk). RQ1–RQ4 / H1–H4 numbering kept because §3, §8, §9 and §12 refer to it.
- Tier A "proxy reality" = the reference scan of a public scene, rendered in the simulator, is the target
  domain; the reconstruction is built from that scene's real video capture. The concrete dataset and
  simulator are chosen in §9 / T3.1 (CONFIRM with §9: it needs scenes with both real video and a reference
  scan). "Real experience" on tier A = rollouts in the reference scan. Tier B datasets: e.g. SCAND, RECON (§9).
- H1(b) tier A margin −10 pp is a design choice (many scenes and episodes; power must be rechecked after the
  pilot with scene-level clustering: CONFIRM supervisor). Tier C keeps the issue #9 rule: normal
  approximation, SR = 0.8 both arms, one-sided α = 0.05, 120 pooled episodes at δ = 15 pp → power 0.90
  (research/review-1.md F8). τ in H4 keeps 10 pp.
- H2 "feature-distribution distance": e.g. Fréchet distance between encoder features; exact metric fixed in
  the repository before Stage IV. Representation alignment added on the student's decision (representation
  learning to close the sim-real distribution gap).
- F10: real-data-only baseline = behaviour cloning / fine-tuning of a pretrained model (GNM/ViNT/NoMaD, §9).
- F23: "real-to-sim" / "sim-to-real" glossed in RQ1. SRCC is from Kadian et al. [11] in §6. -->

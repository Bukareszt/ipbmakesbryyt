# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**Thesis.** Learning in a photorealistic simulation reconstructed from a small budget of real observations,
with representations aligned between reconstructed and real data, yields navigation policies that perform in
the target domain not worse than policies learned from ≥ 10× more real data.

**Core and extensions.** The dissertation stands on **RQ1–RQ2 with H1 and H4** (the real-data-budget
study). RQ3/H2 (generalization, representations) and RQ4/H3 (correction, predictivity) are extensions.

**RQ1.** Does learning in a reconstruction built from minutes of real video of the target environment
(*real-to-sim*), with deployment on real observations (*sim-to-real*), close the appearance and geometry gap?
**RQ2.** How does target-domain performance scale with the real-data budget, and what budget suffices
compared with learning from real data alone?
**RQ3.** Which data augmentation and representation-learning objectives (aligning reconstructed and real
observations) let policies generalize to environments that were *not* captured?
**RQ4.** Can a few real rollouts correct the simulation so that it predicts real performance?

**Evaluation tiers.** (A) *Benchmark, primary:* ≥ 10 public indoor scenes with real video and a reference 3D
scan, which serves in the simulator as the target domain ("proxy reality"); some scenes are held out as
uncaptured. (B) *Real-world datasets:* held-out real frames for representation metrics. (C) *Real-robot
validation:* ≥ 2 PWr environments, 20 start–goal pairs × 3 trials per policy. Metrics: success rate (SR;
primary), SPL, collisions. *Budget* B = minutes of target-domain data (capture plus real experience).
Baselines: a pretrained navigation model fine-tuned by behaviour cloning on target-domain trajectories of
budget B (*real-data-only*), and the same policy trained on the simulator's public scenes with domain
randomization (*generic*). Tests are one-sided (α = 0.05), bootstrapped over scenes (A) or start–goal pairs
(C), Holm-corrected within each hypothesis. Tier A decides, tier C validates. Values are pre-registered in
the repository.

**H1 (RQ1, core).** A policy trained only in the reconstruction (a) beats the generic baseline in SR and
(b) is **non-inferior** to the real-data-only baseline with a ≥ 10× larger budget: the lower 95% bound of
SR_recon − SR_real is above −10 pp on tier A, and above −15 pp on tier C (120 pooled episodes per policy;
≈ 90% power at SR ≈ 0.8).

**H2 (RQ3).** In uncaptured scenes, reconstruction + augmentation + representation alignment reaches a
higher SR than reconstruction alone and than the generic baseline, and alignment lowers the feature
distance between reconstructed and real frames (tier B) against the unaligned encoder.

**H3 (RQ4).** Over ≥ 10 policy variants, the Sim-vs-Real Correlation Coefficient (SRCC) of the
reconstruction is higher than that of a generic simulator (95% CI of the difference excludes 0) and does not
drop after refinement from real rollouts (lower 95% bound of the change ≥ −0.1).

**H4 (RQ2, core).** The full pipeline reaches a target SR τ (best real-data-only SR minus 10 pp) with
B_pipeline(τ) ≤ 0.1 · B_real(τ): the upper 95% bound of the ratio, from fitted budget–SR scaling curves,
is ≤ 0.1. If real-data-only training misses τ within the largest feasible budget, the ratio is reported as
a bound; either way the curves answer RQ2.

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

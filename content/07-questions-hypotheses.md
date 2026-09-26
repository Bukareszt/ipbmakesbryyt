# §7 Pytania i hipotezy badawcze / Research questions and hypotheses (max 1 page)

**RQ1.** Can a photorealistic simulation reconstructed from a short real-world capture (minutes of
video/RGB-D) of a target environment close the *visual* and *geometric* sim-to-real gap for learned
navigation policies?

**RQ2.** How does deployed navigation performance scale with the amount of real-world data? What is the
minimal real-data budget for reliable transfer, compared with training on real robot experience?

**RQ3.** How can reconstructed scenes be augmented (object insertion and rearrangement, lighting and sensor
randomization, dynamic obstacles) so that policies generalize to environments that were *not* captured?

**RQ4.** Can a small number of real-world rollouts be used to iteratively correct the simulation (appearance
and dynamics parameters), closing the real-to-sim-to-real loop?

**H1.** A navigation policy trained only in a 3DGS-based reconstruction of the target environment reaches a
real-world success rate significantly higher than a policy trained in a conventional (non-reconstructed)
simulator, and comparable to a policy trained on a much larger real-robot dataset.

**H2.** Combining reconstructed scenes with targeted randomization generalizes better to unseen real
environments than either reconstruction alone or domain randomization alone.

**H3.** Evaluation in reconstructed environments predicts real-world performance better than evaluation in
a generic simulator. This will be measured by the Sim2Real Correlation Coefficient.

**H4.** Iterative real-to-sim-to-real refinement using a few real rollouts reduces the real-data budget
needed to reach a target success rate by at least an order of magnitude, compared with real-data-only
training.

<!-- Numeric thresholds (e.g. "≥ X pp success rate") to be set after the Semester 2 baseline. -->

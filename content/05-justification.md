# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Modern machine learning is limited less by models than by **data in the target domain**. Deep
reinforcement learning, imitation learning and large pretrained models learn strong behaviour, but only
from very large amounts of experience: near-perfect point-goal navigation in simulation took billions of
frames. In many applications such data can only come from the real world, where it is slow, expensive and
sometimes risky to collect. The central question is therefore how to learn well from **a small, fixed
budget of real data**.

Simulation and synthetic data are the usual answer, but models trained on them often fail on real inputs.
This **sim-to-real gap** is a distribution shift between training and deployment data: in appearance
(textures, lighting, sensor noise), geometry and dynamics. Domain randomization widens the training
distribution by hand and still gives no guarantee for a particular target domain; training directly on
real data does not scale.

**Neural scene reconstruction** (Neural Radiance Fields, 3D Gaussian Splatting) opens a third path. A few
minutes of real video are turned into a photorealistic, interactive model of the target environment, in
which a model can be trained at scale (*real-to-sim-to-real*). This moves the cost from collecting
experience to collecting cheap captures. It raises open machine-learning questions that have not been
studied systematically: how performance **scales with the real-data budget**, which **representations**
make the reconstructed and real data distributions close enough, how to generalize beyond the captured
scenes, and how a few real observations can correct the simulation.

**Why this topic, and why in this discipline.** The research object is a learning methodology, which
places it in *information and communication technology*: data-efficient learning, learning from
reconstructed and synthetic data, representation learning under distribution shift, and methods for
testing whether results obtained in simulation can be trusted. **Visual navigation** of mobile robots is
the application and testbed, chosen because public simulators, benchmarks and real-world datasets allow
controlled, reproducible measurement of the gap. The main evaluation uses these public resources; trials on
a real robot validate the conclusions. The topic fits the representation learning, computer vision and
generative modelling work of the Department of Artificial Intelligence (K46). The computation-heavy parts
(3D reconstruction, large-scale training) can run on the GPU infrastructure available to PWr researchers
(WCSS, PLGrid). Its main result, a measured answer to "how much real data is enough", is useful whatever the
outcome.

**Potential application areas:** service, assistive and warehouse robotics, inspection and last-mile
delivery, and rapid deployment of learned systems in new buildings with minimal on-site data collection.
More broadly, the methods apply wherever models are trained on reconstructed or synthetic data and deployed
on real sensor data: other embodied agents (manipulators, drones), digital twins, and perception models for
autonomous systems.

<!--
Wave 5 (issue #11): rewritten ML-first. The problem is framed as learning under a limited target-domain data
budget and distribution shift; navigation is the testbed; main evaluation on public simulators/benchmarks
and real-world datasets, the real robot (planned K29 "Denali" cooperation, §9) as validation. The
"billions of frames" claim = Wijmans et al. [4] in §6 (2.5 billion frames). K46 groups: research/resources.md
§1 (Representation Learning group led by the supervisor; genwro.AI works on generative models / 3D).
Compute: research/resources.md §2 (WCSS Lem, PLGrid "Doktorant" affiliation; allocations to be applied for).
Earlier revision (issue #6): the pre-PhD ACL 2025 SRW sentence stays removed (kept only in §12).
Visible word count ≈ 440 (limit ~480 at 11 pt, spacing 1).
-->

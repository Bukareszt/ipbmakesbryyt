# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Autonomous mobile robots such as service robots, warehouse and inspection platforms, and delivery vehicles
depend on perception-driven navigation policies. Modern learning-based approaches (deep reinforcement
learning, imitation learning, large pretrained navigation models) outperform hand-engineered pipelines in
unstructured scenes, but they are extremely data-hungry. Near-perfect point-goal navigation in simulation
took billions of frames of experience. Collecting data at that scale on real robots is slow, expensive,
and risky for the hardware and for people.

Simulation is the natural alternative, but policies trained in simulation often fail when deployed on a
real robot. This is the **sim-to-real gap**: differences in appearance (textures, lighting, sensor noise),
geometry, and dynamics (friction, actuation delays). The standard remedy, domain randomization, requires
careful manual design and still gives no guarantee for a particular target environment. The opposite
option, training directly on real data, does not scale.

Recent progress in **neural scene reconstruction** (Neural Radiance Fields, 3D Gaussian Splatting) makes a
third path possible: **real-to-sim-to-real**. A few minutes of real-world capture are turned into a
photorealistic, interactive simulation of the target environment. The policy is trained there at scale and
then deployed back on the real robot. This shifts the cost from collecting *robot experience* to
collecting *cheap scene captures*. It is a promising way out of the data bottleneck, but it has not yet
been studied systematically for mobile-robot navigation. Open questions include how much real data is
really needed, how to generalize beyond the captured scenes, and how to correct the simulation with
feedback from real rollouts.

**Why this topic, and why in this discipline.** The core problems are problems of *information and
communication technology*: learning algorithms, data-efficient training methodology, software for
building simulators from sensor data, and methods for evaluating whether simulation results can be
trusted. The robot is the test platform, not the object of the research. The topic fits the machine
learning, computer vision and representation learning work of the Department of Artificial Intelligence
(K46), and the computation-heavy parts (3D reconstruction, large-scale policy training) can run on the
GPU infrastructure available to PWr researchers (WCSS, PLGrid). Its main result, a measured answer to
"how much real data is enough", is useful to both researchers and practitioners, whatever the outcome.

**Potential application areas:** indoor service and assistive robotics, logistics and warehouse
automation, inspection of industrial facilities, last-mile delivery, and rapid deployment of robots in new
buildings with minimal on-site data collection. The methods also carry over to other embodied systems,
such as manipulators and drones, and to digital twins of real environments more generally.

<!--
Revision (issue #6, research/benchmarks.md edit 15): the sentence "continues my earlier work ... (ACL 2025
SRW)" was removed so that the topic stands on its own. The ACL paper is pre-PhD and in NLP; the mid-term
autoreferat forbids listing recruitment-stage achievements (S9) and off-topic papers are criticised (R1,
AGH). It is kept only as methodological background in §12.
Word count ≈ 470 (limit ~480 at 11 pt, spacing 1).
Sources for the compute claim: research/resources.md §2 (WCSS Lem, PLGrid "Doktorant" affiliation).
-->

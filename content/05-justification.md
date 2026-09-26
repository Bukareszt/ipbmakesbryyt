# §5 Uzasadnienie wyboru tematu / Justification (max 1 page)

Modern machine learning is limited less by models than by **data in the target domain**. Deep
reinforcement learning, imitation learning and large pretrained models learn strong behaviour, but only
from very large amounts of experience: near-perfect point-goal navigation in simulation took billions of
frames. For embodied agents (mobile robots, manipulators) such data can only come from the real world,
where it is slow, expensive and sometimes risky to collect. The central question is therefore how to learn
well from **a small, fixed budget of real data**.

Simulation is the usual answer, but policies trained there often fail on real inputs. This **sim-to-real
gap** is a distribution shift between training and deployment data in appearance, geometry and dynamics.
Domain randomization widens the training distribution by hand and still gives no guarantee for a
particular target domain; training directly on real data does not scale.

**Digital twins built by neural scene reconstruction** (Neural Radiance Fields, 3D Gaussian Splatting) open
a third path. A few minutes of real video are turned into a photorealistic, interactive model of the target
scene, in which a policy can be trained at scale (*real-to-sim-to-real*). This moves the cost from
collecting experience to collecting cheap captures. It raises open machine-learning questions that have not
been studied systematically: how performance **scales with the real-data budget**, which
**representations** bring reconstructed and real data close enough, how to generalize beyond the captured
scenes **and to other tasks and embodiments**, how a few real observations can correct the simulation, and
what a twin costs to build and how faithful it is.

**Why this topic, and why in this discipline.** The research object is a general, task-agnostic learning
methodology, which places it in *information and communication technology*: data-efficient learning,
learning from reconstructed data, representation learning under distribution shift, and methods for
testing whether results from simulation can be trusted. **Visual navigation** is the primary testbed,
because public simulators, benchmarks and real-world datasets allow controlled, reproducible measurement of
the gap; trials on a real robot validate the conclusions. **Robotic manipulation** (e.g. tabletop
pick-and-place in reconstructed scenes) is the generalization domain: it tests, mainly on public
simulators and benchmarks, that the method is not specific to one task or robot. The topic fits the
representation learning, computer vision and generative modelling work of the Department of Artificial
Intelligence (K46). The computation-heavy parts can run on the GPU infrastructure available to PWr
researchers (WCSS, PLGrid). The main result, a measured answer to "how much real data is enough", is useful
whatever the outcome.

**Potential application areas:** service, assistive and warehouse robotics, inspection and delivery,
flexible industrial manipulation, and rapid deployment of learned systems in new buildings and workcells
with minimal on-site data collection. More broadly, the methods apply wherever models are trained on
reconstructed or synthetic data and deployed on real sensor data: other embodied agents, industrial
digital twins, and perception for autonomous systems.

<!--
Wave 6 (issue #14), 2026-09-26: broadened to a general digital-twin policy-learning methodology on the
coordinator's decision; navigation = primary testbed (all feasibility tiers A/B/C unchanged), manipulation =
generalization domain on public simulators/benchmarks first (real validation at PWr optional; K29
Laboratorium Robotyki lists UR3, FANUC LR Mate, ABB IRB 120 per research/resources.md, availability
UNVERIFIED, so no PWr manipulator is named in the visible text). The twin pipeline cost/fidelity is a
contribution (§8 item 5).
Wave 5 (issue #11): ML-first framing. "Billions of frames" = Wijmans et al. [4] in §6 (2.5 billion frames).
K46 groups and compute: research/resources.md §1–§2. The pre-PhD ACL 2025 SRW sentence stays only in §12.
-->

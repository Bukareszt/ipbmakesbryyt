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
been studied systematically for mobile navigation. Open questions include how much real data is really
needed, how to generalize beyond the captured scenes, and how to correct the simulation with feedback
from real rollouts.

The topic continues my earlier work on learning from the internal representations of large models (ACL
2025 SRW) and fits the Department of Artificial Intelligence's work on machine learning.

**Potential application areas:** indoor service and assistive robotics, logistics and warehouse
automation, inspection of industrial facilities, last-mile delivery, and rapid deployment of robots in new
buildings with minimal on-site data collection. The methods also carry over to manipulation and UAVs.

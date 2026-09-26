# §3 Harmonogram / Schedule

<!-- Semesters 1–2 (Oct 2025 – Sep 2026) are already over. TODO: replace them with what was actually done. -->

| Semestr | Task (brief description) |
|---|---|
| 1 (Oct 2025 – Feb 2026) | **Literature review** of sim-to-real transfer, domain randomization/adaptation, neural scene reconstruction (NeRF, 3D Gaussian Splatting) and learning-based navigation. Selection of the robotic platform, sensors and simulator (e.g. NVIDIA Isaac Sim / Habitat). Place: K46 PWr. |
| 2 (Mar – Sep 2026) | **Research infrastructure:** setup of the mobile robot (sensors, ROS 2 stack, logging) and a data-collection protocol. Pilot capture of 2–3 indoor environments at PWr, and a baseline simulation-only navigation policy with its sim-to-real gap measured. Preparation of the IPB. Place: K46 PWr laboratory. |
| 3 (Oct 2026 – Feb 2027) | **Stage I – real-to-sim pipeline:** reconstruct real scenes from short captures (SfM + 3D Gaussian Splatting, with collision geometry), import them into the simulator and validate visual/geometric fidelity. **Prepare and submit a scientific article** (e.g. IROS 2027 / IEEE RA-L), deadline **March 2027**. Participation in a summer/winter school on robot learning. |
| 4 (Mar – Sep 2027) | **Stage II – policy learning in reconstructed scenes:** train navigation policies (RL and imitation learning, fine-tuning of pretrained navigation models) in the reconstructed environments with domain randomization. Real-robot evaluation vs. the baseline, and a study of how performance scales with the real-data budget (addresses H1–H2). Conference presentation of the results. Preparation of an **NCN Preludium grant application**. Preparation for the mid-term evaluation. |
| 5 (Oct 2027 – Feb 2028) | **Mid-term evaluation.** **Stage III – closing the loop:** use real-world rollouts to iteratively correct the simulation (appearance and dynamics parameters) and measure how well simulation results predict real performance (H3–H4). Submission of an article to a journal from the ministerial list (e.g. IEEE RA-L / Robotics and Autonomous Systems). |
| 6 (Mar – Sep 2028) | **Foreign research visit** (1–3 months) at a robot-learning lab to test in new environments and on a second robot. Generalization experiments in unseen environments, including outdoor and dynamic obstacles. Conference paper (e.g. ICRA / CoRL). |
| 7 (Oct 2028 – Feb 2029) | **Stage IV – consolidation:** a full comparison study (real-data budget vs. success rate), release of the code and dataset, and a journal article summarizing the method. Start of dissertation writing. |
| 8 (Mar – Sep 2029) | **Editing of the doctoral dissertation.** Preparation of the final version and submission. |

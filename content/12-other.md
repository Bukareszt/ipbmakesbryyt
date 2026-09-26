# §12 Inne / Other comments (max 1 page)

**Prior work.** Before the doctoral programme, the candidate co-authored "When Will the Tokens End?
Graph-Based Forecasting for LLMs Output Length" (ACL 2025 Student Research Workshop,
doi:10.18653/v1/2025.acl-srw.61). This work on learning from internal representations of large models
provides methodological experience (representation learning, graph neural networks) that is relevant to
learning navigation policies from pretrained visual representations.

**Risks and mitigation.**
- *Hardware availability or failure:* use a widely supported ROS 2 platform, and share equipment with K46
  projects. If needed, run early stages on public real-world navigation datasets.
- *Reconstruction quality in low-texture or large scenes:* combine RGB with depth/LiDAR priors, split
  scenes into segments, and fall back to mesh-based rendering.
- *Negative transfer results:* these are still publishable as a systematic study of the data-budget
  trade-off (RQ2), which keeps the dissertation's contribution intact.

**Planned grants and mobility.** An NCN Preludium application (semester 4) and a 1–3 month foreign research
visit (semester 6). Possible funding: NAWA, Erasmus+, or the PWr doctoral mobility programme.

**Ethics and data.** Real-world captures in public spaces will avoid personal data or be anonymized (blurred
faces) in line with GDPR and PWr rules.

# Novelty synthesis (wave 7, 2026-09-26)

Sources: [crowdedness.md](crowdedness.md) (#16), [world-models.md](world-models.md) (#17),
[novelty-options.md](novelty-options.md) (#18). Counts come from OpenAlex, arXiv and Semantic Scholar; the
exact queries are in each report.

## Verdict per hypothesis (current content/07)

| Hypothesis | Verdict | Keep? |
|---|---|---|
| H1(a): twin beats generic simulator | **Crowded.** At least 5 groups since 2024 (EmbodiedSplat, Vid2Sim, VR-Robo, ReaDy-Go, GaussGym) | Only as a baseline or sanity check, not as a contribution |
| H1(b) + H4: real-data-budget curves (capture minutes vs. real rollouts), navigation | **Open niche.** The manipulation analogue exists (X-Sim, R2R2R) | Yes, as the empirical core |
| H2: representation alignment for the sim-real gap | **Crowded.** 10-year-old domain adaptation field; NeurIPS 2025 (GaTech+NVIDIA) already aligns sim and real | **Reframe.** This is the main novelty risk |
| H3: predictivity (SRCC) of twin vs. generic simulator, after correction | **Active, but open for navigation twins** | Yes. Add a learned world model as a third comparator |

- **The infrastructure layer is a commodity.** Building 3DGS twins for robot learning ran at 23 → 96 → 124
  papers/yr (2024/25/26), with at least 12 open-source twin simulators from Stanford, Berkeley, MIT, NVIDIA,
  TRI and others. We must *use* twins, not compete on building them.
- **World models are converging with twins, not replacing them.** Training foundation world models (Genie,
  Cosmos, V-JEPA 2) is out of reach for a single PhD. Using frozen world-model features, and comparing a
  world model as an *evaluator* against a twin, is open and needs only academic GPUs.

## Recommended direction (coordinator = student; needs supervisor approval)

Keep the object: policies learned in reconstruction twins under a limited real-data budget. Move the **ML
thesis to the representation level**, where K46 and the student's ACL 2025 method (forecasting from hidden
states with a GNN over layers) are strong and the literature is nearly empty:

1. **Core novelty (novelty-options option 1): transfer forecasting from policy internals.** Predict a
   policy's twin-to-real transfer gap from its hidden states or weights, learned over a population of
   policies trained in twins. Only 4 arXiv hits, and Semantic Scholar shows 0/0/0/1/3 papers for 2019–22 /
   2023 / 2024 / 2025 / 2026.
2. **Supporting work (option 2): task-conditioned twin fidelity.** A representation-level metric that
   predicts transfer better than PSNR or LPIPS. Only 1–2 hits.
3. **Empirical core (option 3):** H1(b)/H4 as an "exchange-rate" scaling law, i.e. how many reconstructed
   frames are worth one real frame.
4. **World models:** used as a comparator in H3 (twin vs. world-model evaluator vs. generic simulator) and as
   a source of frozen features. They are not trained.

Proposed thesis: *"The real-world transfer of embodied policies trained in neural-reconstruction twins can
be predicted from their internal representations and from representation-level twin fidelity, without real
rollouts, and this prediction allows a limited real-data budget to be allocated efficiently."*
Manipulation stays as the cross-task test. The first paper (NeurIPS 2027) is a policy zoo plus a
sim-to-real forecasting benchmark with a metanetwork predictor.

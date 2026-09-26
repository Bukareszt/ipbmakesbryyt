# Prior work (input for §2, §5, §6, §11, §12)

## Publications
- G. Piotrowski, M. Bystroński, M. Hołysz, J. Binkowski, G. Chodak, T. J. Kajdanowicz.
  **When Will the Tokens End? Graph-Based Forecasting for LLMs Output Length.**
  Proceedings of the 63rd Annual Meeting of the ACL (Vol. 4: Student Research Workshop), Vienna, July 2025,
  pp. 843–848. doi:[10.18653/v1/2025.acl-srw.61](https://doi.org/10.18653/v1/2025.acl-srw.61)
  - Question: do LLM hidden states encode how much output is left during generation?
  - Methods: (1) aggregation-based regression over transformer layer states; (2) **Layerwise Graph Regressor**,
    a GNN over frozen per-layer embeddings.
  - Result: SOTA on Alpaca with LLaMA-3-8B-Instruct. NMAE is reduced by >50% for short outputs.
  - Published before the PhD start (Oct 2025), so it counts as prior work. It shows research continuity
    and supports §5, §6 and §12.
  - Open question for the supervisor: can it satisfy art. 186 ust. 1 pkt 3? That depends on whether ACL
    SRW proceedings count as the listed ACL conference on the ministerial list. Even if it does, plan a
    new paper for §11, because the IPB should show publication progress during the PhD.

# Lit review: RQ3 (adapting a twin-trained model with little real data)

Verified 2026-09-26 via the arXiv API or abs page, OpenAlex, Crossref or DataCite (curl). (*) means the venue comes from the arXiv comment or project page only.

## TL;DR
- Three lines of work exist: model adaptation from few real samples, simulator calibration from real rollouts, and active selection of data. **None selects real data by twin-reality discrepancy, corrects both twin and model with it, and reports budget curves against random selection. Nothing like this exists in navigation.**
- Closest work: **TwinRL** (failure-driven real rollouts), **ASID** (active real data for system identification) and **MetaMVUC** (active learning for sim-to-real grasping).
- The RQ as worded is **too broad**; the hypothesis is the new part. Reformulate as below.
- Risk: disagreement is measurable only *after* collection, so select by *predicted* discrepancy, and beat failure-driven selection too.

## Papers
**A. Few-shot adaptation and fine-tuning**
1. Rusu, Večerík, Rothörl, Heess, Pascanu et al. (2017). *Sim-to-Real Robot Learning from Pixels with Progressive Nets.* CoRL, PMLR 78. arXiv:1610.04286. Reusing sim features makes real fine-tuning sample-efficient. Baseline for adapting the model only.
2. Kumar, Fu, Pathak, Malik (2021). *RMA: Rapid Motor Adaptation for Legged Robots.* RSS (*). arXiv:2107.04034. Online adaptation, no real training data; dynamics only.
3. Maddukuri, Jiang, Chen, Nasiriany, Xie et al. (2025). *Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation.* RSS. arXiv:2503.24361. A small real set plus sim data gives large gains. The real data are chosen by hand.
4. Jiang, Wang, Zhang, Wu, Fei-Fei (2024). *TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction.* CoRL (*). arXiv:2405.10315. Residual policy from human corrections; a human does the targeting.

**B. Simulator calibration**
5. Chebotar, Handa, Makoviychuk, Macklin, Issac et al. (2019). *Closing the Sim-to-Real Loop (SimOpt).* ICRA. doi:10.1109/ICRA.2019.8793789, arXiv:1810.05687. Adapts the distribution of sim parameters from a few real rollouts. The rollouts are not selected.
6. Ramos, Possas, Fox (2019). *BayesSim: Adaptive Domain Randomization via Probabilistic Inference for Robotics Simulators.* RSS. arXiv:1906.01728. Gives a posterior over sim parameters, a ready source of *predicted* discrepancy.
7. Du, Watkins, Darrell, Abbeel, Pathak (2021). *Auto-Tuned Sim-to-Real Transfer.* ICRA (*). arXiv:2104.07662. Tunes the sim from unlabeled real observations.
8. Memmel, Wagenmaker, Zhu, Yin, Fox (2024). *ASID: Active Exploration for System Identification in Robotic Manipulation.* ICLR, oral (*). arXiv:2404.12308. Collects the most informative real trajectory (Fisher information) to identify the sim. **Closest on the twin side**, but physics only and no policy correction from that data.
9. Torne, Simeonov, Li, Chan, Chen et al. (2024). *Reconciling Reality through Simulation (RialTo).* RSS. arXiv:2403.03949. Fixed-twin baseline.

**C. Active or targeted selection of real data**
10. Su, Tsai, Sohn, Liu, Maji (2020). *Active Adversarial Domain Adaptation.* WACV (*). arXiv:1904.07848. Also Prabhu et al. (2021), *CLUE*, ICCV (*), arXiv:2010.08666. Choosing target labels by domain discrepancy and uncertainty beats random. This is the H3 principle, shown for vision only.
11. Gilles, Furmans, Rayyes (2025). *MetaMVUC: Active Learning for Sample-Efficient Sim-to-Real Domain Adaptation in Robotic Grasping.* IEEE RA-L 10:3644–3651. doi:10.1109/LRA.2025.3544083. **Closest active-learning precedent** in robotics: covers perception only and leaves the twin uncorrected.
12. Bagatella, Hübotter, Martius, Krause (2025). *Active Fine-Tuning of Multi-Task Policies.* ICML (PMLR, per DataCite). arXiv:2410.05026. Selects demonstrations by information gain under a fixed budget. Provides the formalism, but selects over tasks rather than over the sim-real gap.
13. Xu, Liu, Zhou, Shi, Han et al. (2026). *TwinRL: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation.* arXiv:2602.09023. The twin finds failure-prone configurations and real rollouts are targeted there. **Closest overall**, but it selects by failure rather than by twin-reality disagreement, reports no budget curves, and covers manipulation only.
14. Wagenmaker, Huang, Ke, Boots (2024). *Overcoming the Sim-to-Real Gap: Leveraging Simulation to Learn to Explore for Real-World RL.* NeurIPS (*). arXiv:2410.20254. The sim shows where real exploration pays off, even when direct transfer fails.

**D. Test-time adaptation**
15. Hansen, Jangir, Sun, Alenyà, Abbeel et al. (2021). *Self-Supervised Policy Adaptation during Deployment.* ICLR (venue not confirmed in an index). arXiv:2007.04309. Label-free test-time adaptation of the encoder.
16. Zhu, Ye, Wang, Chen et al. (2026). *TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour.* arXiv:2602.02331. Reconstructs each new terrain and fine-tunes quickly, i.e. per-deployment real-to-sim correction.

## Generality
**Too broad.** "How to adapt ... with a small amount of real data?" is answered by the whole field (1–16) and fixes no contribution. The hypothesis is specific and falsifiable, but "disagreement" is undefined and cannot be observed in advance.

Better formulations:
- **RQ3a:** *Which real-world data, chosen under a fixed budget, most efficiently close the twin-to-reality gap of both the model and the twin?* H3 then says that selection by *predicted* twin-reality discrepancy reaches the target success rate with ≥ 50% less real data than random selection, and with no more than failure-driven selection.
- **RQ3b** (optional, isolates the twin correction): *At an equal real-data budget, does using the selected samples to correct the twin as well as the model beat correcting the model alone?*

## Open?
**The combination is open; each part has precedent.** Active target selection exists in vision domain adaptation (10–11), active system identification for physics (8), failure-targeted real rollouts with twins (13), and budgeted information-gain demonstrations (12). Nobody combines three things:
- selection by predicted discrepancy across appearance, geometry and physics;
- joint twin and model correction;
- real-data budget curves against random and failure-driven selection.

No navigation study was found. For novelty, show that discrepancy and failure are different signals (rank correlation below 1) and beat the TwinRL-style rule.

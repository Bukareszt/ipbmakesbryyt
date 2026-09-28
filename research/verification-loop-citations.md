# Verification loop: citations

## Round 1: citations

Date: 2026-09-28. Inputs: visible text (before the first "<!--") of content/05 to 09, bibliography in content/12-other.md, output/IPB_Grzegorz_Piotrowski_PL.md.
Sources: arXiv API (export.arxiv.org, all 26 arXiv ids fetched with abstracts), Crossref (DreamerV3 Nature), OpenReview API (VLAW, DreamGen, Don't Blind), PMLR / ACM DL / RSS / ICLR pages via web search, arXiv HTML full text for [6], [5], [7], [10], [12].

### A. Bibliography metadata

| # | Status | Evidence / problem |
|---|---|---|
| 1 | OK | arXiv:1803.10122, Ha + Schmidhuber, 2018 |
| 2 | OK | arXiv:2310.06114, Sherry Yang first, ICLR 2024 |
| 3 | OK | arXiv:2412.03572, Bar first, arXiv comment "CVPR 2025" |
| 4 | OK (note) | arXiv:2501.03575, arXiv author field "NVIDIA", first named person Niket Agarwal |
| 5 | OK | arXiv:2602.12063, Guo Y. first, OpenReview venueid ICML.cc/2026/Conference |
| 6 | OK | arXiv:2510.18135, Zhang J. first, arXiv comment "ICLR 2026 Oral" |
| 7 | OK | arXiv:2606.31101, Zixing Wang first, 2026. Only a CVPR'26 Embodied AI workshop paper, so arXiv is the right citation |
| 8 | OK | LeCun 2022, OpenReview |
| 9 | OK | arXiv:2506.09985, Assran first, 2025, arXiv only |
| 10 | OK | arXiv:2606.23444, Rao first, 2026, "Under Review" |
| 11 | OK | Crossref 10.1038/s41586-025-08744-2, "Mastering diverse control tasks through world models", Nature 640:647-653, 2025 (arXiv title differs, Nature title is the one cited, correct) |
| 12 | OK (note) | arXiv:2511.04831, author field "NVIDIA", first person Mayank Mittal, 2025 |
| 13 | MINOR | arXiv:2503.14492, first person is Hassan Abu Alhaija. Surname is "Abu Alhaija", so "Abu Alhaija, H., et al." not "Alhaija, H. A., et al." |
| 14 | OK | arXiv:2505.12705, Jang first, OpenReview "CoRL 2025 Poster" |
| 15 | OK | arXiv:2602.15922, Seonghyeon Ye first, 2026 |
| 16 | OK | arXiv:2411.04983, Zhou G. first, PMLR v267 (ICML 2025) |
| 17 | OK | arXiv:2606.05015, Zanatta, Malczyk, Alexis |
| 18 | ERROR | arXiv:2605.06388 authors are Nilaksh, Saurav Jha, Artem Zholus, Sarath Chandar. Bibliography says "Jha, A.". Fix to "Jha, S." |
| 19 | OK | arXiv:2510.10125, Guo Y. first, ICLR 2026 (iclr.cc virtual poster, OpenReview v7hqqBLosx) |
| 20 | OK | arXiv:2405.05941, Li X. first, CoRL 2024 (PMLR v270) |
| 21 | OK | arXiv:1703.06907, Tobin first, IROS 2017 |
| 22 | OK | arXiv:2503.24361, Maddukuri first, RSS 2025 (UT RPL page) |
| 23 | OK | arXiv:2604.13645, Yu Lei first, 2026 |
| 24 | OK | arXiv:2603.08546, Yixuan Wang first, RSS 2026 (roboticsconference.org program paper 18) |
| 25 | OK | arXiv:2106.09685, Hu first, ICLR 2022 |
| 26 | OK | arXiv:2510.25616, Kachaev first, AAMAS 2026 (ACM DL doi 10.65109/PPER9186, also SCALE@ICML2026 workshop) |
| 27 | OK | arXiv:2210.11466, Lee Y. first, arXiv comment "ICLR 2023" |

All venue claims confirmed. No arXiv ids or DOIs are printed for conference entries, which is a style choice, not an error.

### B. Claim support (sentence by sentence)

S = supported, P = partly supported, N = not supported.

§5
- "A newer option is a learned world model [1]." S. Ha and Schmidhuber define and train such a model.
- "UniSim [2] trained robot policies only inside such a model and then used them on real robots." S. Abstract: policies "deployed in the real world in zero shot after training purely in simulation".
- "Navigation World Models [3] imagine how a walk through an unfamiliar place would look from a single image of it" S. Abstract: "imagine trajectories in unfamiliar environments from a single input image".
- "NVIDIA's Cosmos models [4] are released as a base for building such simulators." S. "general-purpose world model that can be fine-tuned into customized world models".
- "The model may ignore an action or let a gripper pass through an object [5],[6]" P. [6] full text: models "ignore action controls" and produce "rollouts that violate physics". [5]: world models "struggle to accurately model small yet critical physical details in contact-rich manipulation". Neither paper describes a gripper passing through an object. Fix: "The model may ignore an action or predict motion that breaks physics [5],[6]".
- "Even a policy built on a video world model and trained only on synthetic demonstrations succeeded in about a third of the trials on a real robot arm in the first such study I have found [7]." S. 35% average on a Franka, ~800 synthetic demos per task, paper claims "first successful sim-to-real transfer of a world-action model".
- "the visual quality of a world model does not reliably predict whether policies succeed in it [6]" S. "visual quality alone does not guarantee task success", Fig. 5a plots success against generation quality.
- "LeCun argued ... predict in such a representation space rather than in pixels ... [8]" S.
- "V-JEPA 2 [9] showed that a world model of this kind can plan the movements of a real robot arm" S.
- "SkyJEPA [10] trained one without real flight data and flew a real quadrotor with it." S on the facts (full text: data generated in simulation with 500 randomized dynamics domains, real outdoor flights only for evaluation). Caveat: SkyJEPA takes low-dimensional state (position, velocity, attitude) as input, not images. The next sentence of §5 is about "features that leave out what differs between simulated and real images", so SkyJEPA supports the sim-only JEPA idea but not the image gap. Fix: "SkyJEPA [10] trained one on simulated states without real flight data and flew a real quadrotor with it."

§6
- "Ha and Schmidhuber [1] ... learned to play a game inside its own dream and then played the real game." S.
- "DreamerV3 [11] ... one fixed configuration across more than 150 tasks." S ("over 150 diverse tasks, with a single configuration").
- "UniSim [2] learned a simulator from mixed internet, robot and navigation data, and policies trained purely in it transferred to the real world without further training." S.
- "NWM [3] predict the first-person video of a moving robot and plan by simulating candidate trajectories." S (trained on egocentric video of humans and robots, plans by simulating trajectories).
- "Cosmos platform [4] provides open world foundation models ... post-trained into world models for particular robots and vehicles." S.
- "NVIDIA also combines these models with its physics simulators, Isaac Sim and Isaac Lab [12]." P. [12] is the Isaac Lab paper and does not mention Cosmos (checked full text). It supports only that Isaac Lab exists. Fix: "NVIDIA also builds physics simulators, Isaac Sim and Isaac Lab [12], and uses Cosmos Transfer [13] to make their renderings look real." (the [13] abstract names "robotics Sim2Real").
- "Cosmos Transfer [13] generates video from spatial control inputs such as depth or segmentation maps, so a simulator rendering can be turned into a real-looking video ... and the simulated actions remain valid." S for control inputs and Sim2Real use. "actions remain valid" is the author's inference, acceptable since layout and motion are kept. "most widely used bridge I have found" is an unsourced opinion, hedged, acceptable.
- "DreamGen [14] fine-tunes a video world model on the target robot, generates videos ..., labels them with actions inferred from the video" S. "22 new behaviours in seen and unseen environments from teleoperation data of a single pick-and-place task" S (abstract adds "in one environment").
- "The term was popularized by DreamZero [15], which reported ... more than twice as well as VLAs." Number S ("over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments"). "popularized" not supported by the source and the term was used earlier (Liang et al. 2025 per later WAM papers). Fix: "DreamZero [15], a well known model of this kind, reported that it generalized ..."
- "The first such work I have found [7] fine-tuned a Cosmos video model into such a policy, trained it only on synthetic demonstrations and reached 35% average success on a real Franka arm without any real training data." Mostly S (built on Cosmos Policy, which is Cosmos-Predict2 post-trained into a policy, 35%, Franka Research 3, "no real demonstrations"). "without any real training data" is too strong, because the Cosmos base model was pretrained on real video. Fix: "without any real robot demonstrations".
- "LeCun's position paper [8] ... JEPA ... predicts the future representation, so it can drop unpredictable detail" S.
- "DINO-WM [16] predicts the frozen features of DINOv2 ... and plans without reconstructing pixels." S.
- "V-JEPA 2 [9] was pretrained on more than a million hours of video. ... less than 62 hours of robot video from DROID ... planned pick-and-place on real Franka arms in labs it had not seen, without rewards." S (abstract: "over 1 million hours of internet video", "less than 62 hours", "Franka arms in two different labs", no data from those environments, no reward).
- "SkyJEPA [10] trained a JEPA world model on automatically generated data and reported zero-shot simulation-to-reality control of a quadrotor in outdoor flights." S. Same state-input caveat.
- "[17] ... the model that scored best in simulation failed on the real platform, while the robustness of the learned representation across environments predicted real transfer, and the size of the latent space and the length of the training sequences mattered most" S. Small precision: the paper says the discrete latent size and sequence length govern "world model quality". Optional fix: "mattered most for the quality of the world model".
- "[18] ... six encoders ... on real manipulation data found that the encoders with the best pixel scores were not the ones that gave the best policies" S (BridgeV2, VAE and Cosmos best pixel scores, V-JEPA 2.1 best on policy).
- "Ctrl-World [19], trained on DROID, ranked policies without real rollouts and improved a policy by fine-tuning it on imagined successful trajectories." S (44.7% improvement).
- "World-in-World [6] tested world models in closed loop on navigation and manipulation and found that visual quality does not guarantee task success, while how well a model follows actions matters more." S (four tasks include ImageNav and robotic manipulation, "controllability matters more").
- "VLAW [5] found that current world models lack the physical accuracy needed to improve policies, because they are trained on demonstrations without failures and miss small contact details." S (near quote).
- "the SIMPLER study [20] showed that scenes visually matched to real images can rank policies in nearly the same order as real runs." S (strong sim to real correlation, low rank violation).
- "The rank correlation between success in the simulator and real success is the accepted indicator of how useful a simulator is" P. SIMPLER reports Pearson correlation and MMRV (mean maximum rank violation), not a rank correlation, and "the accepted" is stronger than any source. Fix: "Agreement between the ranking of policies in the simulator and in reality is a common indicator of how useful a simulator is".
- "Domain randomization [21] varies simulator parameters such as textures so that reality looks like one more variation." S (near quote).
- "Co-training on simulated data together with a small real set improved real-world manipulation [22]" S (average +38%).
- "[23] showed that it aligns the two domains but keeps them distinguishable" S ("balance between cross-domain representation alignment and domain discernibility"). The conclusion "so making the two domains identical is not required" is the author's inference, fair.
- "SkyJEPA [10] is the clearest case I have found of a model trained without real flight data that worked in reality, on a flight task without contact with objects." S, but the sentence sits in a paragraph about visual sim-to-real of world models. Fix: add "and with state inputs rather than images".
- "VLAW [5] fine-tunes the world model on real rollouts and then improves the policy with synthetic data from it." S.
- "DreamGen [14] fine-tunes the video world model on the target robot before generating new training videos." S.
- "The Interactive World Simulator [24] reported that policies trained on data from its world model performed comparably to policies trained on the same amount of real data." S (near quote).
- "LoRA [25] updates only a small set of added weights and is the usual way to adapt large pretrained models with little data." S for the mechanism. "the usual way" is general knowledge, acceptable. "with little data" is not a LoRA claim (LoRA targets parameter and memory cost). Optional fix: "is a common way to adapt large pretrained models cheaply".
- "keeping the visual representation of a VLA close to its pretrained state during fine-tuning improved generalization to new conditions [26]" S (alignment to a frozen teacher's features, better OOD generalization).
- "the best layers to fine-tune were found to depend on the type of distribution shift [27]" S (near quote).

§7, §8: no numbered citations.

§9
- NWM [3] as video world model, DINO-WM [16] as feature world model, V-JEPA 2-AC [9], Ctrl-World [19], Cosmos-Predict from the Cosmos platform [4]: S as tool references.
- "as in Ctrl-World and DreamGen" (generate imagined trajectories, then fine-tune the policy): S.
- "NVIDIA Isaac Lab 3.0 [12] in its mode that runs without Isaac Sim, with the Newton physics engine, which gives colour and depth images" P. [12] (Nov 2025) describes Newton only as an upcoming integration and does not mention Isaac Lab 3.0 or a mode without Isaac Sim. The GitHub release v3.0.0-beta confirms a kit-less mode with Newton and a Warp renderer, with general availability targeted for end of October 2026. The facts exist but [12] does not support them and 3.0 is still beta. Fix: "Isaac Lab [12], version 3.0 (in beta as of September 2026), in its mode that runs without Isaac Sim ..." (optionally cite the release page github.com/isaac-sim/IsaacLab/releases).
- "I will drive Cosmos Transfer [13] with these depth images" S (depth is a supported control input).
- "BridgeData V2, whose WidowX setup is one of the robot setups modelled in SIMPLER [20]" S.
- "ManiSkill, on which SIMPLER is built" S (not cited, true).
- "RECON and SCAND, two of the real robot datasets on which NWM was trained" S (NWM trains on SCAND, TartanDrive, RECON, HuRoN).
- "DROID, on which Ctrl-World and V-JEPA 2-AC were trained" S.
- "LoRA [25]", "domain randomization [21]", "co-training on simulated and real data [22]" as baselines: S.

### C. Numbering and Polish copy

- Order of first appearance across §5 to §9 is exactly 1, 2, ..., 27 (52 citation markers in total). Every entry is cited, and no marker points to a missing entry.
- PL bibliography entries [1] to [27] are identical in order and text to the English list.
- Citation sequences per paragraph in PL §5 to §9 match the English ones in all 14 citing paragraphs (52 markers each).
- The PL copy repeats the same wording problems (gripper [5],[6], "spopularyzowała" [15], "bez żadnych rzeczywistych danych treningowych" [7], Isaac Sim and Isaac Lab [12], SkyJEPA state inputs, [18] "Jha, A.", [13] "Alhaija, H."), so each fix must be applied in both languages.

### D. Problems and minimal fixes

1. [18] author error. "Jha, A." should be "Jha, S." (Saurav Jha). EN and PL.
2. [13] surname. Use "Abu Alhaija, H., et al." EN and PL.
3. §5 "let a gripper pass through an object [5],[6]" not in either source. Use "predict motion that breaks physics [5],[6]".
4. §6 "NVIDIA also combines these models with its physics simulators, Isaac Sim and Isaac Lab [12]" not supported by [12]. Use "NVIDIA also builds physics simulators, Isaac Sim and Isaac Lab [12], and uses Cosmos Transfer [13] to make their renderings look real." Then start the next sentence "Cosmos Transfer generates video ..." without repeating [13] if wished.
5. §6 "The term was popularized by DreamZero [15]" not supported. Use "DreamZero [15], a well known model of this kind, reported that it generalized ...".
6. §6 [7] "without any real training data" too strong (Cosmos base pretrained on real video). Use "without any real robot demonstrations".
7. §5 and §6 SkyJEPA [10] uses state inputs, not images. Add "on simulated states" in §5 and "and with state inputs rather than images" in the §6 paragraph on simulation data.
8. §6 "The rank correlation ... is the accepted indicator" overstated, SIMPLER uses Pearson correlation and rank violation. Use "Agreement between the ranking of policies in the simulator and in reality is a common indicator of how useful a simulator is".
9. §9 "Isaac Lab 3.0 [12] in its mode that runs without Isaac Sim, with the Newton physics engine" not in [12], and 3.0 is still beta. Add "in beta as of September 2026" and optionally cite the Isaac Lab release page.
10. Optional. §6 [17] "mattered most" could say "mattered most for the quality of the world model". §6 LoRA "with little data" could say "cheaply".

## Round 2: citations

Date: 2026-09-28. Inputs: visible text of content/05 to 09, "### Bibliography" in content/12-other.md (29 entries), output/IPB_Grzegorz_Piotrowski_PL.md.
Sources: arXiv API and arXiv HTML full text for 2603.15759, 2510.02538, 2605.06388, 2411.04983, 2503.14492, 2606.31101, roboticsconference.org program (SimDist paper 17), github.com/chandar-lab/semantic-wm (code of [18]).

### A. New entries

- [24] OK. arXiv:2603.15759, Jacob Levy first of 9 authors, title matches, arXiv comment "Robotics: Science and Systems 2026", listed in the RSS 2026 program. Sentence "pretrained a world model in simulation and adapted only the part that predicts the next state with real data, on contact-rich manipulation and quadruped locomotion" S (abstract: "updates only the latent dynamics model using real-world prediction losses", "contact-rich manipulation and quadruped locomotion tasks").
- [25] OK. arXiv:2510.02538, Yilin Wang first of 7 authors, title matches, first posted October 2025, v2 September 2026, no venue found, so arXiv is right. Sentence "pretrained a world model in simulation by imitation and fine-tuned it on a small set of real demonstrations for manipulation" S in substance (online imitation pretraining in ManiSkill, then offline fine-tuning with 15 or 30 real expert trajectories). Precision note: only the encoder and the policy are fine-tuned, and the method uses states (proprioception and estimated object poses), not images.

### B. Changed or renumbered sentences

All round 1 fixes are in place in EN and PL ([5],[6] physics, [12]/[13] NVIDIA sentence, supported by the Cosmos-Transfer1 full text which uses Isaac Lab renderings, DreamZero wording, [7] "without any real robot demonstrations", SkyJEPA state inputs, SIMPLER ranking sentence, Isaac Lab 3.0 beta, [17] and LoRA wording, [13] and [18] authors). [7] in §5 ("trained only on demonstrations from a physics simulator") S. [26] to [29] sentences unchanged and still S. [18] code is public (github.com/chandar-lab/semantic-wm), so §9 is S.

### C. Numbering and Polish copy

- First appearance across §5 to §9 is exactly 1 to 29 (55 markers). Every entry is cited.
- EN and PL bibliographies [1] to [29] are identical.
- Citation sequences match in all 15 citing paragraphs of EN and PL.

### D. New problems and minimal fixes

1. §6 [18] "encoders trained to reconstruct pixels gave the best pixel scores" is too strong. The abstract says only "strong pixel-level scores", and §4.3 of the paper says semantic encoders "dominate most perceptual, structural, and video-level metrics" at the small model size, with VAE best on several metrics only at the largest size. EN fix: "found that encoders trained to reconstruct pixels scored well on pixel metrics, while encoders pretrained on semantic content were better for planning and for evaluating a fixed policy inside the model [18]". PL fix: "enkodery uczone rekonstrukcji pikseli dawały dobre wyniki pikselowe".
2. §6 "SimDist [24] pretrained its encoder only in simulation" is not accurate. In the manipulation tasks the SimDist encoder passes each camera image through "a ResNet-18 encoder pretrained on imagenet" (appendix), so it did not start from simulation alone. What the paper shows is that the encoder is trained on simulation data and frozen during real adaptation. EN fix: "and SimDist [24] trained its encoder on simulation data and kept it frozen during real adaptation." PL fix: "a SimDist [24] trenował swój enkoder na danych z symulacji i nie zmieniał go podczas adaptacji do rzeczywistości."
3. §9 "a decoder trained after the world model, as in DINO-WM [16]". DINO-WM trains the decoder separately from the predictor, with no decoder gradient into the world model (§3.1.3), not necessarily after it. EN fix: "frames from a decoder trained separately from the world model, as in DINO-WM [16]". PL fix: "z dekodera trenowanego osobno od modelu świata".
4. Optional. §6 [25]: "fine-tuned its encoder and policy on a small set of real demonstrations for manipulation, with object poses rather than images as input". PL: "dotrenowali jego enkoder i politykę na małym zbiorze rzeczywistych demonstracji manipulacji, z pozycjami obiektów, a nie obrazami, na wejściu".

No other new or unresolved problems found.

## Round 3: citations

Date: 2026-09-28. Inputs: visible text of content/05 to 09, "### Bibliography" in content/12-other.md (30 entries), output/IPB_Grzegorz_Piotrowski_PL.md.
Sources: arXiv API and arXiv HTML full text for 2603.09241 (RAE-NWM), 2510.10125 (Ctrl-World), 2605.06388 ([18]), GitHub API for 20robo/raenwm and isaac-sim/IsaacLab releases.

### A. New entry [19] RAE-NWM

- Metadata OK. arXiv:2603.09241, Mingkun Zhang first of 6 authors (Tsinghua), posted 2026-03-10, title matches. The repository README says "provisionally accepted to ECCV 2026", so arXiv is still a correct citation (optional: "ECCV" once final).
- Code public: github.com/20robo/raenwm, MIT licence, with train.py, planning_eval.py, and weights on Hugging Face (zmkun20/raenwm). §9 "whose code is public" S.
- Datasets: one model trained on the union of SACSoN/HuRoN, RECON and SCAND, tested on held-out trajectories of each (§5.1), plus a separate Habitat model. "on RECON and SCAND" S.
- DINOv2 instead of NWM codes: S. It works in dense DINOv2 space with a frozen RAE decoder, NWM is the SD-VAE baseline, and the ablation "substitute[s] the DINOv2 encoder with the same frozen SD-VAE used in NWM" (§5.5).
- "planned better with them on RECON and SCAND": N for RECON. Table 2 (CEM planning, ATE/RPE): SCAND RAE-NWM 1.14/0.28 vs NWM 1.28/0.33 (better), RECON RAE-NWM 1.36/0.37 vs NWM 1.13/0.35 (worse). The text says "In this short-horizon setting, NWM obtains lower ATE and RPE on RECON". Long 16 s rollouts are better on RECON (Fig. 10), but planning is not.
- "Neither work trained policies inside the models or tested them on real data": S. [18] only runs fixed VLAs in the loop, RAE-NWM only plans with CEM.

### B. Ctrl-World [20] in §9

- "As in Ctrl-World, I will run a policy trained on real data with added action noise in each world model and keep the rollouts that the same success classifier judges successful." P/N. Ctrl-World §4.2 creates diversity by "(i) rephras[ing] the instructions" or "(ii) reset[ting] the policy to random initial states" (Algorithm 1 only names a generic "action perturbation function"), and success is judged by humans: "we label each trajectory as a success or failure based on human preference judgments", "we use human annotators". No success classifier. Only "keep successful imagined rollouts and fine-tune on them" matches.

### C. Isaac Lab 3.0 [12] in §9

- S. GitHub release v3.0.0-EA "Isaac Lab 3.0 Early Access", published 2026-09-16, "General Availability is targeted toward the end of October 2026", with kit-less Newton workflows and "Newton Warp camera rendering". "an early access release as of September 2026" is correct.

### D. Other changed sentences, numbering, Polish copy

- [18] sentence (round 2 fix), SimDist [25] frozen encoder, Wang et al. [26] with object poses, DINO-WM decoder "trained separately": all in place in EN and PL and S. [20] to [30] sentences unchanged in substance after renumbering and still S.
- First appearance across §5 to §9 is exactly 1 to 30 (57 markers). Every entry is cited.
- EN and PL bibliographies [1] to [30] are identical (byte-for-byte diff).
- Citation sequences match in all 15 citing paragraphs of EN and PL.

### E. New problems and minimal fixes

1. §6 RAE-NWM planned worse than NWM on RECON.
   EN: "In navigation, RAE-NWM [19] predicted DINOv2 features instead of the autoencoder codes of NWM and planned better with them on SCAND but not on RECON."
   PL: "W nawigacji model RAE-NWM [19] przewidywał cechy DINOv2 zamiast kodów autoenkodera używanego w NWM i planował z nimi lepiej na zbiorze SCAND, ale nie na RECON."
2. §9 Ctrl-World used varied instructions and start states and human judges, not action noise and a success classifier.
   EN: "Ctrl-World varied the instructions and start states of a policy in its world model and kept the rollouts that human annotators judged successful. I will instead run a policy trained on real data with added action noise in each world model and keep the rollouts that the same success classifier judges successful."
   PL: "Ctrl-World zmieniał polecenia i stany początkowe polityki w swoim modelu świata i zachowywał przebiegi, które ludzie uznali za udane. Ja uruchomię w każdym modelu świata politykę wytrenowaną na danych rzeczywistych z dodanym szumem akcji i zachowam przebiegi, które ten sam klasyfikator sukcesu uzna za udane."
3. Optional. [19] could read "ECCV" (provisionally accepted per the repository), in EN and PL.

No other new or unresolved problems found.

## Round 4: citations

Date: 2026-09-28. Inputs: committed version a5c2998, visible text (before the first "<!--") of content/05 to 09, "### Bibliography" in content/12-other.md (30 entries), output/IPB_Grzegorz_Piotrowski_PL.md.
Sources: arXiv API (all 28 arXiv ids re-fetched: titles, author lists, dates, comments), arXiv HTML full text of 2603.09241 (RAE-NWM, §5.1, §5.3, Table 2, §5.5) and 2510.10125 (Ctrl-World, §4.2, Algorithm 1, §5, appendix), GitHub API for isaac-sim/IsaacLab releases.

### A. Sentences changed in round 3

- §6 RAE-NWM [19] "predicted DINOv2 features instead of the autoencoder codes of NWM and planned better with them on SCAND but not on RECON." S. Table 2 (CEM planning, ATE/RPE, 2 s): SCAND 1.14/0.28 vs NWM 1.28/0.33, RECON 1.36/0.37 vs 1.13/0.35, and the text says "NWM obtains lower ATE and RPE on RECON". RAE-NWM is also better on SACSoN (2.91/0.70 vs 4.12/0.96). The sentence leaves SACSoN out but says nothing false. PL says the same.
- §6 "Neither work trained policies inside the models or tested them on real data" S. [18] runs fixed VLAs inside the model, RAE-NWM plans with CEM and tests closed loop only in Habitat.
- §9 Ctrl-World [20] "kept imagined rollouts that people judged successful and fine-tuned the policy on them." S. §4.2 "we label each trajectory as a success or failure based on human preference judgments", §5 "retain 25 to 50 successful trajectories based on human preference judgments", then fine-tune on them. PL says the same.
- §9 "version 3.0 of NVIDIA Isaac Lab [12], an early access release as of September 2026." S. Release v3.0.0-EA "Isaac Lab 3.0 Early Access", published 2026-09-16, is still the latest release. [12] supports only that Isaac Lab exists, which is all the sentence now cites it for. PL says the same.

### B. Sentences whose context changed after the cuts

- §6 SIMPLER [21] now stands alone after the "common indicator" sentence was cut. Still S and still reads correctly.
- §9 V-JEPA 2 [9] now appears only as "an encoder pretrained on real video, such as V-JEPA 2 [9]", and Ctrl-World [20] only in the rollout sentence. Both S. No citation lost its only occurrence through the cuts.
- §9 kit-less mode, Newton and ray-tracing sentences are gone, so the round 1 problem with [12] is fully resolved.
- All other cited sentences in §5 to §9 are unchanged from round 3 and still S.

### C. Numbering, bibliography and Polish copy

- First appearance across §5 to §9 is exactly 1 to 30 (57 markers). Every bibliography entry is cited, no marker points to a missing entry.
- Metadata of all 30 entries matches the sources (arXiv first authors, titles, years, venue comments, [11] Nature per round 1, [8] OpenReview per round 1). No changes since round 3.
- EN and PL bibliographies are identical line by line (30 of 30).
- Citation sequences match in all 15 citing paragraphs (57 markers each).
- PL cited sentences say the same as EN, including all round 3 changes.

### D. New or unresolved problems

No required fixes remain. One optional wording point:

1. Optional. §9 "I will instead run a policy trained on real data with added action noise ..." can read as if Ctrl-World did not perturb actions, but its Algorithm 1 samples actions from a "perturbed policy" (the concrete perturbations in the text are rephrased instructions and random start states). What differs is the judge. Minimal fix that keeps both sentences:
   EN: "I will instead keep the rollouts that one success classifier, the same for every world model, judges successful, and I will create varied rollouts by adding action noise to a policy trained on real data."
   PL: "Ja zamiast tego zachowam przebiegi, które jeden klasyfikator sukcesu, ten sam dla każdego modelu świata, uzna za udane, a różne przebiegi uzyskam, dodając szum akcji do polityki wytrenowanej na danych rzeczywistych."
2. Optional. §6 RAE-NWM could name SACSoN too: EN "planned better with them on SACSoN and SCAND but not on RECON", PL "planował z nimi lepiej na zbiorach SACSoN i SCAND, ale nie na RECON".

No other new or unresolved problems found.

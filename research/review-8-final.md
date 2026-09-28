# Review 8: final adversarial review of the IPB (world models as simulators, observable results only)

Reviewed on 2026-09-28. Material: visible text of content/02, 03, 05, 06, 07, 08, 09, 10, 11, 12 (working tree). Background: research/wm_simulators.md, research/nvidia_stack.md, research/wam_lecun.md, research/review-7-threads.md, output/IPB_Grzegorz_Piotrowski.pdf (20:33 build). Lens: scientific-critical-thinking, hypothesis-generation, scholar-evaluation. Read-only, nothing in content/ or output/ was edited. Placeholders [17] and [23] ignored as instructed. Owner constraints (first person, no thresholds, no semicolons or dashes, no pre-registration, both tasks at equal weight, representation learning as choices in how features are learned, judged only by observable results) were treated as binding.

Summary of the state: the plan has moved off latent-space methods almost completely, the absence claims are hedged, real performance is defined, and every RQ has a rival. What remains is (1) one measurement in §9 that is still a latent-space operation in disguise and does not measure what it claims, (2) an unstated pipeline gap for feature-predicting world models that would force a second latent-space measure, (3) a data mismatch that makes the real-performance stand-in only partly available, and (4) RQ3's pretraining arms, which are not feasible as written and are internally incoherent in H3.

---

## CRITICAL

### C1. The action-following measure in §9 is unsound and, for feature-predicting models, a latent-space distance
- **File:** 09-methods.md (RQ1 paragraph), 07-questions-hypotheses.md (H1 rival).
- **Quoted verbatim:** "To separate the effect of the prediction target from the effect of how faithfully a world model follows actions, I will compare world models that follow actions equally well, measured by how their one-step predictions change when the recorded action is replaced by another (H1)."
- **Problem:** (a) Sensitivity to an action swap measures whether the prediction depends on the action, not whether it follows it. A model that changes its prediction strongly and wrongly scores as "following actions" well. (b) For DINO-WM and V-JEPA 2-AC the "one-step prediction" is a feature vector, so "how it changes" is a distance in representation space, which is the kind of measure the owner ruled out, and it is not comparable with the pixel change of a video model (different spaces, different scales). (c) "Compare world models that follow actions equally well" cannot be engineered. Action following is a property of the models the student gets, not a knob. (d) The H1 rival ("once action following is matched") therefore has no sound test.
- **Fix (replaces the quoted sentence):** "To tell the effect of the prediction target apart from the effect of how faithfully a world model follows actions, I will measure action following for every world model in the same observable way: on held-out real transitions I will check whether the prediction made with the recorded action is closer to the recorded next frame than the prediction made with a different recorded action, and report the fraction of transitions where the recorded action wins. I will then report the effect of the prediction target together with each model's action following, so that a difference between the two targets can be told apart from a difference in action following (H1)."
  This uses recorded data as the reference, gives one number that means the same thing for pixel and feature models, and needs no matched pairs of models.

### C2. Training policies in, and measuring success inside, a feature-predicting world model is undefined and would force a second latent-space measure
- **File:** 09-methods.md (paragraphs 2, 4 and 6), 07-questions-hypotheses.md (RQ1).
- **Quoted:** "Policies will be trained in a world model by generating imagined trajectories once and fine-tuning the policy on them, as in Ctrl-World and DreamGen"; "I will record how well its success inside the world model predicts its real performance, as a rank correlation over policies and scenes"; "For every policy I will report the success rate in the world model".
- **Problem:** Ctrl-World and DreamGen produce video, so a policy can be fine-tuned on imagined frames and success can be judged from the video. DINO-WM and V-JEPA 2-AC produce feature sequences. For them, (a) the imagined trajectory has no frames, so the policy must act on the world model's own features, which ties the "encoder the policy is built on" factor to the prediction-target factor and breaks the one-change-at-a-time design for that pair, (b) actions come from planning toward a goal, not from a policy acting in the loop, which is a different way of producing training data, and (c) "success inside the world model" can only be the distance between the predicted features and the goal features, which is a latent-space measure. As written, half of RQ1's arms have no defined success rate and the rank correlation promised "for every world model" cannot be computed for them.
- **Fix (add after the "Policies will be trained..." sentence):** "For world models that predict features, the policy will act on the same features and the imagined trajectories will come from planning in the world model toward goal images, as in DINO-WM. Because such models produce no video, I will judge success inside the model only for models that predict video, and I will judge feature models by their prediction quality on real recordings and by the real performance of the policies trained in them." And in the last paragraph replace "For every world model I will report its prediction quality on real recordings and the rank correlation of the success of policies inside it with their real performance" with "For every world model I will report its prediction quality on real recordings and, where the model produces video, the rank correlation of the success of policies inside it with their real performance."

### C3. The real-performance stand-in is only partly available with the named models and data
- **File:** 09-methods.md (paragraph 3).
- **Quoted:** "For manipulation I will use DROID, on which Ctrl-World and V-JEPA 2-AC were trained, and BridgeData V2, whose WidowX setup is one of the robot setups modelled in SIMPLER [19]. Held-out trajectories of these datasets give real observations, actions and next observations. A world model is tested on them by how well it predicts the recorded next frames."
- **Problem:** (a) Ctrl-World used the whole of DROID and V-JEPA 2-AC was trained on DROID, so "held-out" DROID trajectories are training data for both, and prediction quality measured on them is a training-set score. (b) SIMPLER covers the WidowX (BridgeData) and Google Robot setups. No world model named in §9 is trained on BridgeData V2, so a policy trained inside Ctrl-World or V-JEPA 2-AC is a Franka policy that SIMPLER cannot run. The SIMPLER half of "real performance" therefore exists only if the student post-trains a world model on BridgeData V2, which the text does not say. For navigation there is no SIMPLER analogue, so navigation real performance is action closeness alone, which the text should say plainly.
- **Fix:** "Because Ctrl-World and V-JEPA 2-AC were trained on DROID, I will measure prediction quality on recordings these models have not seen, such as BridgeData V2 and recordings added to DROID after their release, and I will state for every model which data it had seen. So that SIMPLER success is available, I will also further train at least one world model of each kind on BridgeData V2, whose WidowX setup SIMPLER models. For navigation, where no such simulator exists, real performance is the closeness of the planned path to the recorded one."

### C4. RQ3's pretraining arms are not feasible as written and H3 is incoherent
- **File:** 07-questions-hypotheses.md (RQ3, H3), 09-methods.md (RQ3 paragraph), and the promise in §7 paragraph 2.
- **Quoted:** "I will compare encoders pretrained on real video, on simulation data and on both, with and without the objective from RQ2" (RQ3 and §9); "Models whose encoder was pretrained on real video with the objective from RQ2 reach the performance of full fine-tuning with less real data than models pretrained on simulation data only or without the objective" (H3); "I will fine-tune existing pretrained world models and policies rather than train large models from scratch" (§7, paragraph 2).
- **Problem:** (a) An encoder "pretrained on real video" at the scale of DINOv2 or V-JEPA 2 cannot be produced by one student, so the real-video arm will be an existing checkpoint while the simulation arm is something the student trains. The arms then differ in data scale and model size, not only in data domain, and the comparison is confounded. (b) The objective from RQ2 pairs a simulated frame with its photorealistic version, so it needs simulation data. "Pretrained on real video with the objective from RQ2" describes an arm that cannot exist. (c) Both contradict the stated policy of not training large models from scratch.
- **Fix (RQ3 and §9):** "I will start from existing encoders pretrained on real video and continue their pretraining on simulation data, on real robot data and on both, with and without the objective from RQ2, and compare full fine-tuning against parameter-efficient fine-tuning and co-training with generated data, at equal amounts of real data."
  **H3:** "Models whose encoder was further pretrained on both real and simulation data with the objective from RQ2 reach the performance of full fine-tuning with less real data than models further pretrained on either kind of data alone or without the objective. The rival explanation is that the amount of real data is set by the dynamics of the new setting rather than by the encoder, so that all variants need the same amount."

---

## MAJOR

### M1. The navigation branch has no policy and no feature-predicting world model, so RQ1 cannot be run on navigation as designed
- **File:** 09-methods.md (paragraph 2).
- **Quoted:** "For navigation I will start from NWM [3]. For manipulation I will use DINO-WM [16] or V-JEPA 2-AC [9] as world models that predict features, and Ctrl-World [18] or Cosmos-Predict from the Cosmos platform [4] as world models that predict video."
- **Problem:** NWM is a video model used as a planner. RQ1 needs, for navigation too, a policy network to train on imagined trajectories and a feature-predicting world model to compare with the video one. Neither is named, so the prediction-target factor and the "encoder the policy is built on" factor exist only for manipulation, which contradicts the equal-weight decision and RQ4.
- **Fix:** "For navigation I will use NWM [3] as the world model that predicts video and train DINO-WM [16] on the same navigation data as the world model that predicts features, and I will train a goal-conditioned navigation policy on the imagined trajectories of each, starting from a policy pretrained on the same public navigation datasets."

### M2. The RQ2 pairing objective needs a trainable encoder, while RQ1 uses frozen encoders, and H2's fairness needs one stated check
- **File:** 07-questions-hypotheses.md (RQ2, H2), 09-methods.md (RQ1 and RQ2 paragraphs).
- **Quoted:** RQ1: "pixels against the frozen features of DINOv2 or V-JEPA 2"; RQ2: "a self-supervised objective that gives each simulated frame and its photorealistic version the same features"; H2: "than when the photorealistic frames are only added to the training set".
- **Assessment:** The objective is a representation learning objective in the owner's sense (an invariance objective on how features are learned, judged by prediction quality and real performance), and the comparison against merely adding the frames is the right control: both arms see the same frames, only the pairing information differs. Two things make it unfair or unrunnable as written. (a) A frozen encoder cannot be trained with the objective, so RQ2 must say the encoder is fine-tuned, and the frozen encoder becomes the control. (b) Cosmos Transfer can move or reshape objects. If a pair no longer shows the same geometry, the objective teaches the features to ignore real change, and the comparison is biased against the objective for a reason that has nothing to do with the hypothesis.
- **Fix (§9 RQ2):** "For this objective the encoder is fine-tuned rather than frozen, and the frozen encoder is the control. I will keep only pairs in which the transferred frame keeps the geometry of the simulated one, judged with the depth image used to drive the transfer."

### M3. Nearest prior work is missing and one absence claim in §5 is broader than §6 allows
- **File:** 05-justification.md (paragraph 2), 06-state-of-the-art.md (paragraphs 4, 6 and 7).
- **Quoted:** §5: "I have not found in my search a study of how to build a world model from physics simulation data, which is cheap and unlimited, so that it predicts the real world well." §6: "How the representation should be pretrained in the first place, so that the fewest real samples are needed later, is, as far as my search shows, still open."
- **Problem:** (a) The §5 sentence is contradicted by the plan's own §6, which cites SkyJEPA as a world model built from simulation data that worked in reality. §6 carries the narrower and defensible version ("a controlled study of which representation learning choices ..."). (b) research/wam_lecun.md lists World Translation (Yao et al., arXiv:2607.18154, sim-to-real for world models by unpaired domain translation) and "Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models" (Nilaksh et al., arXiv:2605.06388, a comparison of prediction targets for robotic world models). Both are the nearest neighbours of RQ2 and RQ1 and neither is cited. (c) The §6 claim about pretraining for few real samples ignores the line of visual representations pretrained for robot learning and compared by how many demonstrations they need (R3M, VC-1 and successors). The hedge "as far as my search shows" does not cover a body of work a robotics committee member will know. Narrow the claim to world models.
- **Fix (§5):** "I have not found in my search a controlled comparison of ways to build a world model from physics simulation data, which is cheap and unlimited, so that it predicts the real world well." **Fix (§6, paragraph 6, add before the absence claim):** "World Translation [n] reduces the gap of a simulation-trained world model with unpaired image translation and recovered dynamics, and a recent comparison of feature spaces for robotic world models [n] asks which latent space is useful without measuring real transfer." **Fix (§6, paragraph 7):** "How the representation of a world model, and of the policy trained in it, should be pretrained so that the fewest real samples are needed later is, as far as my search shows, still open. For policies alone, visual encoders pretrained for robot learning have been compared by how many demonstrations they need [n]."

### M4. Two sentences overstate what will be measured
- **File:** 06-state-of-the-art.md (paragraph 5), 09-methods.md (last but two paragraph).
- **Quoted:** "The rank correlation between success in the simulator and real success is the accepted indicator of how useful a simulator is, and I will use it in the same way." "For every policy I will report the success rate in the world model, its real performance and the gap between the two."
- **Problem:** "In the same way" implies real success from real runs, which the student will not have. "The gap between the two" subtracts a success rate from an action-closeness score, which has no meaning except where real performance is SIMPLER success.
- **Fix:** "The rank correlation between success in the simulator and real success is the accepted indicator of how useful a simulator is, and I will use it with the stand-in for real performance described in section 9." and "For every policy I will report the success rate in the world model and its real performance, and where both are success rates, the gap between the two."

### M5. RQ3 is a full factorial that one student cannot run, and "a new real setting" has no named source
- **File:** 09-methods.md (RQ3 paragraph).
- **Quoted:** "The pretraining variants are ... The adaptation variants are full fine-tuning, parameter-efficient fine-tuning with LoRA [24], fine-tuning of selected layers as in surgical fine-tuning [26] and co-training with generated data at different mixing ratios. I will repeat this for several amounts of real data"; "a new real scene or robot setup".
- **Problem:** Pretraining variants times adaptation variants times mixing ratios times amounts of real data times two tasks times seeds is hundreds of fine-tuning runs plus evaluations, in semesters 5 and 6, next to RQ2 and RQ4. The text also does not say where the new setting comes from without a robot.
- **Fix:** "The new settings will be held-out scenes of DROID and BridgeData V2 and held-out environments of RECON and SCAND, and the change from the Franka to the WidowX setup. I will first choose the adaptation method with the encoder pretrained on real video, and then compare the pretraining variants with that method, so that the two comparisons are not fully crossed."

### M6. §8 still promises an attribution of the gap
- **File:** 08-contribution.md (paragraph 1).
- **Quoted:** "together with evidence on how much of the remaining gap comes from the simulated physics".
- **Problem:** This is the residue of the appearance-versus-dynamics split removed after review 7. Nothing in §9 measures how much of the gap "comes from" physics. §9 measures whether randomizing physics or adding real data helps.
- **Fix:** "together with evidence on whether randomizing the simulated physics or adding a small real set helps more than changing appearance."

### M7. The Fallback uses the wrong term and a condition that does not apply
- **File:** 07-questions-hypotheses.md (item 8).
- **Quoted:** "If the prediction target and the pretraining choices make no difference to real success at equal video quality, I will study the data side instead".
- **Problem:** "Real success" is the term §9 replaced by "real performance". "At equal video quality" is a leftover: the plan matches on action following, not video quality, and feature models have no video quality.
- **Fix:** "If the prediction target and the pretraining choices make no difference to real performance at similar action following, I will study the data side instead: the mixing ratios of generated, simulated and real data and their amount and diversity. This is weaker, because it says less about how representations should be learned."

### M8. Schedule names a venue that has no deadline before the §11 date
- **File:** 03-schedule.md (semester 4), 11-publication-date.md.
- **Quoted:** §3: "Preparing and submitting the first publication to a 200-point venue in machine learning or robot learning, such as ICLR, RSS or IEEE RA-L." §11: "September 2027 (... such as the ICLR 2028 conference or the journal IEEE Robotics and Automation Letters)".
- **Problem:** RSS deadlines fall in winter, so RSS 2028 cannot be reached by September 2027 and RSS 2027 is before the first results. §11 correctly omits RSS.
- **Fix (§3, semester 4):** "Preparing and submitting the first publication to a 200-point venue in machine learning or robot learning, such as ICLR or IEEE RA-L."

---

## MINOR

### m1. §7 page limit and numbering
- Body without heading is 4280 characters, at the edge of the safe limit. In the 20:33 PDF §7 runs about 105 text lines against about 100 per full page, so it spills. The list numbers each RQ and H separately ("1. RQ1.", "2. H1.") and puts RQ4 and H4 in one item, which wastes vertical space and looks uneven.
- **Least harmful cuts, in order:** (1) drop the list numbers and start paragraphs with "RQ1.", "H1."; (2) drop "I will work on both navigation and manipulation." from paragraph 1 (§5 and RQ4 say it); (3) drop the line "My research questions (RQ) and hypotheses (H) are as follows."; (4) use the shorter Fallback from M7; (5) in paragraph 2 replace "As the reference for reality I will use recorded real robot data and published real-robot results, which are only a proxy, and a real robot if access allows." with "As the reference for reality I will use recorded real robot data and published real-robot results, and a real robot if access allows." Together these save about 300 characters and two to three lines.

### m2. §5 category slip on [7]
- **Quoted:** "A policy that succeeds in the world model can therefore fail on a real robot. In the first such study I have found, a policy trained only on synthetic demonstrations succeeded in about a third of the trials on a real robot arm [7]."
- **Problem:** [7] trained a World Action Model on physics-simulator demonstrations, not a policy inside a world model built from real data, so "such study" points at the wrong thing.
- **Fix:** "Even a policy built on a video world model and trained only on synthetic demonstrations succeeded in about a third of the trials on a real robot arm in the first such study I have found [7]."

### m3. Jargon without a gloss
- §6: "teleoperation data" (add "recorded while a human steered the robot"); "DINOv2" at first use in §6 paragraph 4 (add "a vision network pretrained without labels"). §9: "self-supervised objective" is fine, "SLURM", "H100", "Franka", "WidowX" are fine.

### m4. Repetition and triads
- "judged by observable results" appears in §7 paragraph 1 and §9 paragraph 1. Keep it once, in §7. Triads: §5 "a warehouse, a hospital or a home", §10 "slow, costly and sometimes unsafe" and "faster, more cheaply and more safely" (both languages). Harmless, but one of the §10 pair could go. No semicolons, em dashes or en dashes in the visible text. "sim", "sim2real" and "sim-to-real" appear only inside cited titles in §12, which is correct.

### m5. Small inconsistencies
- §6 closing paragraph says RQ3 seeks "the least real data", §7 says "less real data". Use "less". §9 RQ2 says "train world models on it" while §7 promises to fine-tune existing models. Write "train small world models or further train large ones on it". §9 "how well it predicts the recorded next frames" for diffusion or flow models compares one sample with one real frame, which mixes error with legitimate randomness. Add "averaged over several samples" after PSNR and LPIPS.

### m6. Prior-work claims re-checked against research/*.md
- Consistent with the notes: UniSim, NWM, Cosmos, Cosmos Transfer ("most widely used bridge I have found"), DreamGen (22 behaviours, three real robots), WAM "popularized by DreamZero", [7] at 35% on a Franka, JEPA, DINO-WM, V-JEPA 2 (million hours, less than 62 hours of DROID, unseen labs, no rewards), SkyJEPA "without contact with objects", Zanatta wording, Ctrl-World, World-in-World, VLAW, Isaac Lab 3.0 mode without Isaac Sim with colour and depth on H100, Isaac Sim not on A100 or H100, Cosmos Transfer driven by depth. Not in the notes but consistent with the papers as known: SIMPLER, [21], [22], [25], [26]. Remaining overclaims: the §5 sentence in M3 and the "in the same way" sentence in M4. All other absence claims are phrased as "I have not found in my search" or "as far as my search shows".

---

## Status of review 7 items

| Item | Status |
|---|---|
| C1 real success unmeasurable | Resolved by the §9 definition, with a residue in the Fallback (M7) and "gap between the two" (M4). Availability of the stand-in is a new problem (C3). |
| C2 appearance versus dynamics split | Resolved by the one-change-at-a-time design. Residue in §8 (M6). |
| C3 RQ3 defined by an RQ1 stage | Resolved. RQ3 now depends softly on the RQ2 objective, which is acceptable because its other arms stand without it. New feasibility and coherence problem in the pretraining arms (C4). |
| C4 placeholders, LeWorldModel uncited | Placeholders excluded from this review by instruction. LeWorldModel is no longer used, so no longer applicable. |
| C5 H1 against a weak baseline | Resolved, the rival is now action following. Its measurement is unsound (C1). |
| M1 paired imagined and real observations | No longer applicable, the latent gap is gone. The single-sample issue survives in a small form (m5). |
| M2 two tasks at equal weight | Still open as a feasibility risk, kept by owner decision. Not raised again except through M1 and M5. |
| M3 encoder pretraining confound in the pixel versus feature comparison | Reduced, since the video models are also pretrained on real video, but the two families differ in size and training recipe. Optional within-family control: "Within one small world model I will also swap the prediction target between reconstruction features and the features of a pretrained encoder, keeping the architecture fixed." |
| M4 RQ1 not discriminating | Resolved. |
| M5 H4 confirms everything | Resolved. |
| M6 "either the world model or the policy" | Resolved. |
| M7 absence claims as facts | Resolved in §5 and §9, one §5 sentence still too broad (M3). |
| M8 overclaims | Resolved, except the category slip on [7] (m2). |
| M9 Isaac Lab mode and fallback | Resolved. |
| M10 cost of training policies in video models | Resolved. |
| M11 probing the navigation policy | No longer applicable, probing removed. The navigation policy is still unnamed (M1). |
| M12 blanket held-out promise | Resolved for published results and SIMPLER, still open for DROID prediction quality (C3). |
| m1 three versus four questions | Resolved. |
| m2 jargon | Mostly resolved, two glosses missing (m3). |
| m3 anglicisms and punctuation | Resolved. |
| m4 boilerplate | Resolved in §8, triads remain (m4 above). |
| m5 §7 formatting and page limit | Still open (m1 above). |
| m6 §10 "real trials" | Resolved. |
| m7 bibliography details | Excluded by instruction. |
| m8 schedule wording | Resolved, one venue mismatch remains (M8). |

---

## Internal consistency

- §3 against §7: RQ1 in semesters 3 and 4, RQ2 in 4 and 5, RQ3 in 5 and 6, RQ4 in 6. Consistent. Semester 4 and §11 agree on September 2027 except for RSS (M8).
- §5 against §6 and §7: three questions plus the generality check, RQ1 to RQ4 in the same order and wording. Consistent.
- §6 closing paragraph against §7: consistent apart from "least" versus "less" (m5).
- §7 against §9: every factor named in RQ1 to RQ3 has a method paragraph. The paragraph on real performance is referenced from RQ1 as "as defined in section 9". The Fallback still says "real success" (M7). §7 paragraph 2 promises no training from scratch while RQ3 asks for encoders pretrained on simulation data (C4).
- §8 against §7 and §9: three results match the three RQs. "How much of the remaining gap comes from the simulated physics" has no method (M6).
- §10 against §7: the three threads and both tasks appear in both languages. Consistent.
- §12 statement on AI use against §9: consistent.

---

## Verdict

With the four Critical items fixed, the plan is realistic for one student in three research years, though with little slack. The three threads rest on open models that run on H100 nodes, on public datasets, and on comparisons that need no robot. The hard constraint is not the science but the arithmetic of the design: two tasks at equal weight, four factors in RQ1, six in RQ2 and a pretraining-by-adaptation cross in RQ3, each over seeds and scenes, all between semesters 3 and 7. The plan survives this only if RQ3 is run sequentially rather than fully crossed (M5), if feature-predicting models are judged by prediction quality and real performance rather than by an invented in-model success (C2), and if at least one world model is post-trained on BridgeData V2 early so that SIMPLER success exists when RQ1 results are due in semester 4 (C3). The first publication by September 2027 is credible for RQ1 on manipulation with navigation following in the same paper or the next one. The main scientific risk is that action following, once measured soundly (C1), explains most of the variation and the prediction target adds little, which the Fallback covers honestly.

# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Roboty coraz częściej uczy się we „śnie”, czyli w kopii świata przewidywanej przez sieć neuronową zwaną modelem świata, ponieważ nauka w prawdziwym świecie jest powolna, kosztowna i czasem niebezpieczna. Sieć uczy się z nagrań wideo, co zwykle dzieje się po ruchu robota, ale jej sen nigdy nie jest idealny. Robot, który dobrze radzi sobie we śnie, w prawdziwym świecie często zawodzi, zwłaszcza w nowych miejscach. Chcę sprawdzić, jak takie sieci powinny uczyć się swojego wewnętrznego obrazu świata, aby umiejętności ze snu przenosiły się do rzeczywistości. Chcę też zbadać, jak budować takie sny z tanich symulacji fizyki, aby dobrze przewidywały prawdziwy świat, oraz jak przygotować sen i robota, aby do nowego miejsca wystarczyło niewiele prawdziwego doświadczenia. Zbadam głównie chwytanie i przestawianie przedmiotów, a wyniki sprawdzę także w nawigacji robotów. Efektem mają być metody, dzięki którym roboty będą szybciej, taniej i bezpieczniej uczyć się nowej pracy.

## Abstract for general public

Robots are increasingly trained in a "dream", a copy of the world predicted by a neural network called a world model, because real-world learning is slow, costly and sometimes unsafe. The network learns from videos what usually happens after a robot moves, but its dream is never perfect. A robot that does well in the dream often fails in reality, especially in new places. I want to find out how such networks should learn their internal picture of the world so that skills from the dream carry over to reality. I also want to study how to build such dreams from cheap physics simulations so that they predict the real world well, and how to prepare the dream and the robot so that a new place takes only a little real experience. I will study mainly the grasping and moving of objects and check the results in robot navigation. The result should be methods that let robots learn new work faster, more cheaply and more safely.

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 33 (2026-09-28): re-centred on three threads: world models as simulators and real-to-simulation-to-real generalization (RQ1), world models trained on physics simulation data that transfer to reality (RQ2), reducing the real data needed for adaptation (RQ3), generality across scenes and tasks (RQ4). The old RQ3 on choosing real rollouts to correct both the world model and the policy was removed at the owner's request. References renumbered by first appearance across §5-§9. Older notes below are history. -->

<!-- Wave 32: rewritten around world models -->
<!-- Wave 29: humanized (no semicolons) -->
<!-- Wave 28: restyled after the accepted 2025 IPB (2026-09-28, research/accepted_plan_tts_2025.txt). §10 shortened to about 130 words per language in the accepted plan's simple style; PL and EN identical; glass-door example kept; reflection example dropped. -->
<!-- Wave 24: humanized (2026-09-27). §10: humanizer pass on both languages in parallel: 'beyond computer screens' opener cut; 'remains one of the main obstacles' simplified; the goal sentence and the methods sentence each split in two (17 / 17 sentences, same content); closing sentence rephrased as the expected outcome. No claims added or removed. -->
<!-- Wave 22: navigation + manipulation equal (2026-09-27, binding student decision). §10: navigation and manipulation as two equal tasks (manipulation glossed as grasping and moving objects on a table); simulation results compared with published real-robot results and verified on a real mobile robot; cross-task transfer sentence added. PL and EN kept parallel sentence by sentence. -->
<!-- Wave 21: validation fixes (2026-09-27, research/validation-v8.md, approved by the student). §10 (fix 9): example of a harmful difference added (glass door / reflection in a mirror); the long 'copy is never perfect' sentence split into four; 'przy różnych zadaniach'/'on different tasks' -> 'przy więcej niż jednym zadaniu'/'on more than one task'; navigation main (with robot), manipulation 'simulated' (fix 1); 'digital twin' used consistently. PL and EN kept parallel sentence by sentence. -->
<!-- Review-6 (2026-09-27): "generalizacja" explained in both languages; RQ1 outcome added ("więcej ćwiczyć tam, gdzie wirtualna kopia jest najmniej dokładna"); ending softened to "przy różnych zadaniach" / "on different tasks"; "modele te uczy się zwykle" / "such models are usually trained"; "uczonych"; EN "carry objects" to match PL. -->
<!--
Wave 20 (ultracode), 2026-09-27: rewritten from scratch in the style of Binkowski §10 (one paragraph per
language: goal, planned research, why this topic, expected effects). Aligned with the final core: topic =
generalization of DL models in real-to-sim-to-real transfer for physical AI; research = which differences
harm (RQ1), where in the model (RQ2), invariance + choice of few real examples correcting model and
simulation (RQ2/RQ3), held-out environments on navigation and manipulation (RQ4). No numbers, no model
names. PL and EN checked sentence by sentence: 9 / 9 sentences, same content.
-->
<!--
Wave 18-W (issue #35), 2026-09-26: pivot decision v7 (research/pivot-decision.md, top). Both languages
rewritten in parallel: the goal is a method that REDUCES real data (three reduction mechanisms, one per
step: less capture, better use of simulation incl. the world model filling gaps, fewer real trials);
navigation of mobile robots is the main testbed and robots that handle objects (manipulation) the
generalization test ("unchanged"); "minutes of a person's work, in the same way for every approach" =
operator minutes on a shared budget grid, stated as the measurement, not the goal; "today nobody knows how
little would be enough" = the report's finding that no pipeline varies or reports the real-data budget.
No model or checkpoint names. PL and EN checked sentence by sentence: 3 paragraphs each, 5 / 7 / 3
sentences, same content.
-->
<!--
(history) Wave 16-W (issue #33), 2026-09-26: pivot decision v6 (research/pivot-decision.md, top). Both languages
rewritten in parallel: navigation of mobile robots in buildings is the only domain (manipulation /
grasping removed); the pipeline is described as three steps real -> twin -> navigation model -> real (v6
"Object" 1-3); step 2 names world models and pretrained foundation models as families ("a program that
learns to predict what happens next", "large models pretrained on much other data"), no model names, no
VLA; the expected result compares with existing approaches (§7 H4). PL and EN checked sentence by
sentence: 3 paragraphs each, 5 / 5 / 3 sentences, same content.
-->
<!--
(history) Wave 15 (issue #31), 2026-09-26: pivot decision v5 (research/pivot-decision.md, top). Both languages
changed in parallel. Para 1 now starts from pretrained VLA models ("understand images and ... instructions
and choose movements") that still need further training for a new place and task (OpenVLA arXiv:2406.09246,
Octo arXiv:2405.12213 abstracts: fine-tuning to new settings), and the twin is where this further training
happens (sim-first fine-tuning). Para 2: C1 = a VLM ("a model that understands images and language")
points out what matters, capture goes where the copy is uncertain; C2 = robust fine-tuning plus a world
model ("a program that learns to predict what happens next") generating extra situations where the copy is
uncertain; C3 = few real trials correct the copy, the world model and the model. "Guidance will come from
the copy itself ... the way the learning system describes what it sees" was dropped (the v5 signal is the
uncertainty of twin, WM and VLA, already implied by "knows too little" / "uncertain parts"). "Device"
dropped from the twin definition (the testbeds are places/scenes). Para 3: "learning systems" -> "robots"
(the method now fine-tunes robot VLAs). PL and EN checked sentence by sentence: 3 paragraphs each, 5 / 7 /
3 sentences, same content.
-->
<!--
(history) Wave 14 (issue #30), 2026-09-26: pivot decision v4 (research/pivot-decision.md, top; framing only). Both
languages changed in parallel: the goal is now to DEVELOP A METHOD that needs much less real data than
existing approaches (v4 "cel pracy"); a new sentence says it has three parts, one per loop step (C1-C3);
the expected result is "one method" plus how much real data it saves versus real-only learning and existing
approaches (H4 (a) and (b)). PL and EN checked sentence by sentence: 3 paragraphs each, 5 / 8 / 3
sentences, same content.
-->
<!--
(history) Wave 13 (issue #28), 2026-09-26: generalized in both languages in parallel after pivot decision v3
(research/pivot-decision.md, top): "robot" -> "system" where the claim is general; the twin includes "how
things move" (physical parameters, system identification); "whatever the task" = task-agnostic; the two
testbeds (grasping = manipulation, moving around buildings = navigation) have equal status, no "main
task". "Publicly available data" replaces "recordings and 3D scans of real buildings" (manipulation tier A
uses a simulator reference and tier B public paired evaluations). Mapping to RQ1-RQ4 unchanged. PL and EN
checked sentence by sentence: 3 paragraphs each, same number of sentences (5 / 7 / 3), same content.
-->
<!--
(history) Wave 11 (issue #25), 2026-09-26: rewritten in both languages in parallel after pivot decision v2
(research/pivot-decision.md). Removed wave 9-10 content: "looking inside the head of the robot" as the goal,
predicting transfer before deployment, released data and trained models (no benchmark / policy zoo).
Mapping: "record mainly the places that matter ... still uncertain" = RQ1/H1 (task-aware capture); "train
the robot so that it does not rely on the uncertain parts" = RQ2/H2 (uncertainty-aware training); "choose
only the few trials ... correct both the copy and the robot" = RQ3/H3; "measurement of how much real data is
needed" = RQ4/H4 budget law; "the copy knows where it is uncertain, the way the model describes what it
sees" = reconstruction uncertainty and policy representations as tools; navigation main task, grasping =
cross-task (H4b); "public recordings and 3D scans of real buildings" = tier A (and B); "confirmed on a real
robot" = tier C (validation only; lab not named because the cooperation is not agreed). "Short recording"
instead of "phone video" because tier A uses public captures. "Very large number of trials" kept from
review-2 R2-F14. PL and EN checked sentence by sentence: 3 paragraphs each, same number of sentences
(5 / 7 / 3), same content.
-->

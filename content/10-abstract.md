# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Sztuczna inteligencja coraz częściej wychodzi poza ekrany komputerów i trafia do systemów fizycznych, takich jak roboty poruszające się po budynkach lub przenoszące przedmioty. Modele uczenia głębokiego sterujące takimi robotami potrzebują ogromnej liczby przykładów, których zebranie w prawdziwym świecie jest powolne, kosztowne, a czasem niebezpieczne. Dlatego modele te uczy się zwykle w symulacji, a coraz częściej w cyfrowych bliźniakach, czyli wirtualnych kopiach rzeczywistych miejsc odtworzonych na podstawie ich nagrań. Taka kopia nigdy nie jest jednak idealna. Na przykład szklane drzwi lub odbicie w lustrze mogą zostać odtworzone błędnie i zmylić robota. W efekcie model, który dobrze działa w symulacji, w rzeczywistości często zawodzi, zwłaszcza w miejscach, których wcześniej nie widział. Pozostaje to jedną z głównych przeszkód na drodze do szerszego zastosowania fizycznej sztucznej inteligencji. Celem rozprawy jest poprawa zdolności generalizacji modeli uczenia głębokiego trenowanych w cyfrowych bliźniakach, czyli umiejętności poprawnego działania w warunkach innych niż te, w których je trenowano, a zwłaszcza w rzeczywistości. Badania w pierwszej kolejności pozwolą ustalić, które różnice między symulacją a rzeczywistością faktycznie szkodzą modelowi i na którym etapie przetwarzania w modelu przekształcają się one w błędy. Na tej podstawie zostaną opracowane metody, które nauczą model pomijać nieistotne różnice i więcej ćwiczyć tam, gdzie cyfrowy bliźniak jest najmniej dokładny, a także metody wyboru nielicznych rzeczywistych przykładów, które najlepiej poprawiają zarówno model, jak i cyfrowego bliźniaka. Metody zostaną sprawdzone przede wszystkim w zadaniu nawigacji robotów, w środowiskach, które nie były wykorzystywane podczas uczenia, i zweryfikowane na prawdziwym robocie mobilnym. Zostaną też przetestowane w symulowanym zadaniu manipulacji robotycznej. Oczekuje się, że rozprawa przyniesie lepsze zrozumienie przyczyn, dla których modele uczone w symulacji zawodzą w rzeczywistości, a także metody, dzięki którym roboty będą mogły szybciej, taniej i bezpieczniej uczyć się pracy w nowych miejscach i przy więcej niż jednym zadaniu.

## Abstract for general public

Artificial intelligence is increasingly moving beyond computer screens into physical systems, such as robots that move around buildings or carry objects. Deep learning models that control such robots need a huge number of examples, which are slow, costly and sometimes unsafe to collect in the real world. Therefore, such models are usually trained in simulation, and increasingly in digital twins, that is, virtual copies of real places rebuilt from recordings of those places. Such a copy is never perfect, however. For example, a glass door or a reflection in a mirror may be rebuilt incorrectly and mislead the robot. As a result, a model that works well in simulation often fails in reality, especially in places it has not seen before. This remains one of the main obstacles to the wider use of physical artificial intelligence. The goal of the dissertation is to improve the generalization of deep learning models trained in digital twins, i.e., their ability to work correctly in conditions different from those they were trained in, and in particular in reality. The research will first establish which differences between simulation and reality actually harm the model, and at which stage of processing inside the model they turn into errors. On this basis, methods will be developed that teach the model to ignore irrelevant differences and to practise more where the digital twin is least accurate, together with methods that choose the few real examples that best correct both the model and the digital twin. The methods will be examined mainly on robot navigation, in environments that were not used during training, and verified on a real mobile robot. They will also be tested on a simulated robotic manipulation task. The dissertation is expected to bring a better understanding of why models trained in simulation fail in reality, as well as methods that allow robots to learn to work in new places and on more than one task faster, more cheaply and more safely.

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

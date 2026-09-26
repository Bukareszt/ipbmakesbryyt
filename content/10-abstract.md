# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Roboty, które poruszają się po budynkach, na przykład w magazynach, szpitalach czy biurach, coraz
częściej korzystają z modeli nawigacji, które uczą się na podstawie doświadczenia. Aby taki model dobrze
działał w konkretnym budynku, potrzebuje wielu danych z tego miejsca, a zbieranie ich w rzeczywistości
jest powolne i kosztowne. Dlatego coraz częściej robot uczy się w cyfrowym bliźniaku: wiernej kopii
prawdziwego budynku, którą można odtworzyć z krótkiego nagrania i kilku pomiarów. Powstaje w ten sposób
droga w trzech krokach: zbieramy dane w rzeczywistości i budujemy z nich kopię, uczymy w niej model
nawigacji, a następnie przenosimy go z powrotem do rzeczywistości i tam sprawdzamy oraz poprawiamy. Każdy
z tych kroków wymaga jednak prawdziwych danych.

Celem rozprawy jest opracowanie metody, która przejdzie tę drogę z dużo mniejszą ilością prawdziwych
danych niż dotychczasowe podejścia. W pierwszym kroku zamiast nagrywać wszystko po równo, będziemy nagrywać
przede wszystkim te miejsca, które są ważne dla poruszania się robota, a o których kopia wie jeszcze za
mało. W drugim kroku, ponieważ kopia nigdy nie jest idealna, będziemy uczyć model tak, aby nie polegał na
jej niepewnych fragmentach; pomogą w tym model świata, czyli program, który uczy się przewidywać, co
wydarzy się dalej, oraz duże modele wstępnie wytrenowane na wielu innych danych. W trzecim kroku wybierzemy
tylko te nieliczne próby w rzeczywistości, które najwięcej mówią o tym, gdzie kopia i model jeszcze się
mylą, i wykorzystamy je do ich poprawienia. Badania będą prowadzone przede wszystkim na publicznie
dostępnych skanach prawdziwych budynków, a wyniki zostaną potwierdzone na prawdziwym robocie.

Spodziewanym efektem jest metoda, która pozwoli nauczyć robota poruszania się w nowym budynku przy dużo
mniejszej ilości prawdziwych danych, oraz pomiar, ile prawdziwych danych oszczędza w porównaniu z
dotychczasowymi podejściami. Może to przyspieszyć i potanić wdrażanie robotów mobilnych w magazynach,
szpitalach i biurach. Opracowane oprogramowanie zostanie udostępnione publicznie.

## Abstract for general public

Robots that move around buildings, for example in warehouses, hospitals or offices, increasingly rely on
navigation models that learn from experience. For such a model to work well in a particular building, it
needs a lot of data from that place, and collecting it in reality is slow and costly. That is why robots
increasingly learn in a digital twin: a faithful copy of a real building that can be rebuilt from a short
recording and a few measurements. This creates a path in three steps: we collect data in reality and
build the copy from it, train the navigation model in the copy, and then transfer it back to reality,
where we check and correct it. Each of these steps, however, needs real data.

The goal of this dissertation is to develop a method that follows this path with much less real data than
existing approaches. In the first step, instead of recording everything evenly, we will record mainly the
places that matter for the robot's movement and about which the copy still knows too little. In the second
step, because the copy is never perfect, we will train the model so that it does not rely on the
uncertain parts of the copy; a world model, a program that learns to predict what happens next, and large
models pretrained on much other data will help with this. In the third step, we will choose only the few
trials in reality that tell the most about where the copy and the model are still wrong, and use them to
correct both. The research will be carried out mainly on publicly available scans of real buildings, and
the results will be confirmed on a real robot.

The expected result is a method that makes it possible to teach a robot to move around a new building with
much less real data, and a measurement of how much real data it saves compared with existing approaches.
This may make deploying mobile robots in warehouses, hospitals and offices faster and cheaper. The
software developed will be made publicly available.

<!--
Wave 16-W (issue #33), 2026-09-26: pivot decision v6 (research/pivot-decision.md, top). Both languages
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

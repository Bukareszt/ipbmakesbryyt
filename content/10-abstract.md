# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Systemy sztucznej inteligencji, które działają w prawdziwym świecie, na przykład roboty chwytające
przedmioty lub poruszające się po budynkach, uczą się na bardzo wielu przykładach i próbach. W
rzeczywistości zbieranie takich danych jest powolne i kosztowne, dlatego systemy te często ćwiczą w
symulacji komputerowej. Coraz częściej jest nią cyfrowy bliźniak: wierna kopia prawdziwego miejsca lub
urządzenia, którą można odtworzyć z nagrań i pomiarów, łącznie z wyglądem, kształtem i tym, jak rzeczy się
poruszają. Powstaje w ten sposób pętla: zbieramy dane w rzeczywistości, budujemy kopię, uczymy w niej
system, sprawdzamy go w rzeczywistości, poprawiamy i dopiero wtedy wdrażamy. Każdy z tych kroków wymaga
jednak prawdziwych danych, a ich zbieranie jest kosztowne.

Celem rozprawy jest sprawdzenie, jak przejść przez tę pętlę z jak najmniejszą ilością prawdziwych danych,
niezależnie od zadania. Zamiast zbierać wszystko po równo, będziemy zbierać przede wszystkim te dane, które
są ważne dla zadania i o których kopia wie jeszcze za mało. Ponieważ kopia nigdy nie jest idealna, nauczymy
system tak, aby nie polegał na jej niepewnych fragmentach i radził sobie z jej błędami. Na koniec wybierzemy
tylko te nieliczne próby w rzeczywistości, które najwięcej mówią o tym, gdzie system jeszcze zawodzi, i
wykorzystamy je do poprawienia zarówno kopii, jak i systemu. Wskazówek dostarczy sama kopia, która wie,
gdzie jest niepewna, oraz sposób, w jaki uczony system opisuje to, co widzi. Te same metody sprawdzimy na
dwóch różnych zadaniach: chwytaniu przedmiotów ramieniem robota i poruszaniu się robota po budynkach.
Badania będą prowadzone przede wszystkim na publicznie dostępnych danych, a wybrane wyniki zostaną
potwierdzone na prawdziwym robocie.

Spodziewanym efektem są metody, które pozwolą zbierać mniej danych, uczyć skuteczniej i wykonywać mniej
kosztownych prób w rzeczywistości, oraz pomiar, ile prawdziwych danych potrzeba, gdy system uczy się w
cyfrowej kopii. Może to przyspieszyć i potanić wdrażanie uczących się systemów w fabrykach, magazynach,
szpitalach i biurach. Opracowane oprogramowanie zostanie udostępnione publicznie.

## Abstract for general public

Artificial intelligence systems that act in the real world, for example robots that grasp objects or
move around buildings, learn from a very large number of examples and trials. In reality, collecting such
data is slow and costly, so these systems often practise in a computer simulation. Increasingly, this is a
digital twin: a faithful copy of a real place or device that can be rebuilt from recordings and
measurements, including how things look, their shape and how they move. This creates a loop: we collect
data in reality, build the copy, train the system in it, check it in reality, correct it and only then
deploy it. Each of these steps, however, needs real data, and collecting it is costly.

The goal of this dissertation is to find out how to go through this loop with as little real data as
possible, whatever the task. Instead of collecting everything evenly, we will collect mainly the data that
matters for the task and about which the copy still knows too little. Because the copy is never perfect,
we will train the system so that it does not rely on the uncertain parts of the copy and copes with its
errors. Finally, we will choose only the few trials in reality that tell the most about where the system
still fails, and use them to correct both the copy and the system. Guidance will come from the copy
itself, which knows where it is uncertain, and from the way the learning system describes what it sees.
We will test the same methods on two different tasks: grasping objects with a robot arm and a robot moving
around buildings. The research will be carried out mainly on publicly available data, and selected results
will be confirmed on a real robot.

The expected result is methods that make it possible to collect less data, train more effectively and
carry out fewer costly trials in reality, and a measurement of how much real data is needed when a system
learns in a digital copy. This may make deploying learning systems in factories, warehouses, hospitals
and offices faster and cheaper. The software developed will be made publicly available.

<!--
Wave 13 (issue #28), 2026-09-26: generalized in both languages in parallel after pivot decision v3
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

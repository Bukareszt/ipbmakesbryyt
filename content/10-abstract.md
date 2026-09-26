# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Roboty uczą się dziś samodzielnego działania, na przykład poruszania się po budynku lub chwytania
przedmiotów, metodą prób i błędów. Potrzebują do tego bardzo wielu prób, więc zwykle ćwiczą w symulacji
komputerowej. Coraz częściej jest nią cyfrowy bliźniak: wierna, fotorealistyczna kopia prawdziwego miejsca,
którą metody sztucznej inteligencji potrafią odtworzyć z krótkiego nagrania. Powstaje w ten sposób pętla:
nagrywamy prawdziwe miejsce, budujemy jego kopię, uczymy w niej robota, sprawdzamy go w rzeczywistości,
poprawiamy i dopiero wtedy wdrażamy. Każdy z tych kroków wymaga jednak prawdziwych danych, czyli nagrań i
prób w prawdziwym świecie, a ich zbieranie jest powolne i kosztowne.

Celem rozprawy jest sprawdzenie, jak przejść przez tę pętlę z jak najmniejszą ilością prawdziwych danych.
Zamiast nagrywać wszystko po równo, będziemy nagrywać przede wszystkim te miejsca, które są ważne dla
zadania robota i których kopia jest jeszcze niepewna. Ponieważ kopia nigdy nie jest idealna, nauczymy
robota tak, aby nie polegał na jej niepewnych fragmentach i radził sobie z jej błędami. Na koniec wybierzemy
tylko te nieliczne próby w rzeczywistości, które najwięcej mówią o tym, gdzie robot jeszcze zawodzi, i
wykorzystamy je do poprawienia zarówno kopii, jak i robota. Wskazówek dostarczy sama kopia, która wie,
gdzie jest niepewna, oraz sposób, w jaki model sterujący robotem opisuje to, co widzi. Głównym zadaniem
testowym będzie nawigacja robota mobilnego, a sprawdzianem uniwersalności chwytanie przedmiotów ramieniem
robota. Badania będą prowadzone przede wszystkim na publicznie dostępnych nagraniach i trójwymiarowych
skanach prawdziwych budynków, a wybrane wyniki zostaną potwierdzone na prawdziwym robocie.

Spodziewanym efektem są metody, które pozwolą nagrywać mniej, uczyć skuteczniej i wykonywać mniej
kosztownych prób w rzeczywistości, oraz pomiar, ile prawdziwych danych potrzeba, gdy robot uczy się w
cyfrowej kopii. Może to przyspieszyć i potanić wdrażanie robotów w magazynach, szpitalach, biurach i
fabrykach. Opracowane oprogramowanie zostanie udostępnione publicznie.

## Abstract for general public

Robots today learn to act on their own, for example to move around a building or to grasp objects, by
trial and error. They need a very large number of trials, so they usually practise in a computer
simulation. Increasingly, this is a digital twin: a faithful, photorealistic copy of a real place that
artificial intelligence methods can reconstruct from a short recording. This creates a loop: we record the
real place, build its copy, train the robot in it, check it in reality, correct it and only then deploy it.
Each of these steps, however, needs real data, that is, recordings and trials in the real world, and
collecting them is slow and costly.

The goal of this dissertation is to find out how to go through this loop with as little real data as
possible. Instead of recording everything evenly, we will record mainly the places that matter for the
robot's task and whose copy is still uncertain. Because the copy is never perfect, we will train the robot
so that it does not rely on the uncertain parts of the copy and copes with its errors. Finally, we will
choose only the few trials in reality that tell the most about where the robot still fails, and use them
to correct both the copy and the robot. Guidance will come from the copy itself, which knows where it is
uncertain, and from the way the model that controls the robot describes what it sees. Mobile-robot
navigation will be the main test task, and grasping objects with a robot arm will test how universal the
approach is. The research will be carried out mainly on publicly available recordings and
three-dimensional scans of real buildings, and selected results will be confirmed on a real robot.

The expected result is methods that make it possible to record less, train more effectively and carry out
fewer costly trials in reality, and a measurement of how much real data is needed when a robot learns in a
digital copy. This may make deploying robots in warehouses, hospitals, offices and factories faster and
cheaper. The software developed will be made publicly available.

<!--
Wave 11 (issue #25), 2026-09-26: rewritten in both languages in parallel after pivot decision v2
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

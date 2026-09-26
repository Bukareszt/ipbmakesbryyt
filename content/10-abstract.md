# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Roboty uczą się dziś samodzielnego działania, na przykład poruszania się po budynku lub chwytania
przedmiotów, metodą prób i błędów. Potrzebują do tego bardzo wielu prób, więc zwykle ćwiczą w symulacji
komputerowej. Coraz częściej jest nią cyfrowy bliźniak: wierna, fotorealistyczna kopia prawdziwego miejsca,
którą metody sztucznej inteligencji potrafią odtworzyć z krótkiego filmu nagranego telefonem. Kopia nigdy
nie jest jednak idealna. Bywa rozmyta, ma drobne zniekształcenia i inaczej oddaje światło. Robot, który
świetnie radzi sobie w kopii, może więc zawieść w prawdziwym świecie. Dziś można to sprawdzić tylko,
wypuszczając go do prawdziwego budynku, a to jest powolne i kosztowne.

Celem rozprawy jest sprawdzenie, czy da się to przewidzieć wcześniej, zaglądając „do głowy” robota. Model
sztucznej inteligencji, który steruje robotem, przetwarza każdy obraz na wewnętrzny opis tego, co widzi.
Zbadamy, czy obraz z kopii i obraz z rzeczywistości tego samego miejsca są przez model opisywane podobnie,
w której części modelu pojawiają się różnice i jak maleją, gdy nagranie jest dłuższe. Następnie nauczymy
osobny model przewidywać na podstawie tych wewnętrznych opisów, jak dobrze robot poradzi sobie w
rzeczywistości i kiedy może popełnić błąd, zanim zostanie tam wysłany. Na koniec sprawdzimy, czy takie
prognozy pomagają mądrze wydać niewielki zasób prawdziwych danych: co warto nagrać i które próby w
rzeczywistości przeprowadzić. Głównym zadaniem testowym będzie nawigacja robota mobilnego, a sprawdzianem
uniwersalności chwytanie przedmiotów ramieniem robota. Badania będą prowadzone przede wszystkim na
publicznie dostępnych nagraniach i trójwymiarowych skanach prawdziwych budynków, a wybrane wyniki zostaną
potwierdzone na prawdziwym robocie.

Spodziewanym efektem są metody, które pozwolą ocenić robota wyuczonego w cyfrowej kopii, zanim trafi do
prawdziwego świata, oraz zmniejszyć liczbę kosztownych prób w rzeczywistości. Może to przyspieszyć i
potanić wdrażanie robotów w magazynach, szpitalach, biurach i fabrykach. Opracowane oprogramowanie, dane i
wyuczone modele zostaną udostępnione publicznie.

## Abstract for general public

Robots today learn to act on their own, for example to move around a building or to grasp objects, by
trial and error. They need a very large number of trials, so they usually practise in a computer simulation.
Increasingly, this is a digital twin: a faithful, photorealistic copy of a real place that artificial
intelligence methods can reconstruct from a short video recorded with a phone. The copy, however, is never
perfect. It can be blurry, have small distortions and render light differently. A robot that does very
well in the copy may therefore fail in the real world. Today this can only be checked by sending it into a
real building, which is slow and costly.

The goal of this dissertation is to find out whether this can be predicted earlier by looking "inside the
head" of the robot. The artificial intelligence model that controls the robot turns every image into an
internal description of what it sees. We will study whether an image from the copy and an image from
reality of the same place are described similarly by the model, in which part of the model differences
appear, and how they shrink when the recording is longer. Next, we will teach a separate model to predict
from these internal descriptions how well the robot will cope in reality and when it may make a mistake,
before it is sent there. Finally, we will check whether such forecasts help to spend a small amount of
real data wisely: what is worth recording and which trials in reality to carry out. Mobile-robot
navigation will be the main test task, and grasping objects with a robot arm will test how universal the
approach is. The research will be carried out mainly on publicly available recordings and
three-dimensional scans of real buildings, and selected results will be confirmed on a real robot.

The expected result is methods that make it possible to assess a robot trained in a digital copy before it
reaches the real world, and to reduce the number of costly trials in reality. This may make deploying
robots in warehouses, hospitals, offices and factories faster and cheaper. The software, data and trained
models developed will be made publicly available.

<!--
Review-2 (issue #24), 2026-09-26, R2-F14: "milionów prób" / "millions of trials" -> "bardzo wielu prób" /
"a very large number of trials" in both versions (same change, PL = EN kept).
-->
<!--
Wave 9 (issue #22), 2026-09-26: rewritten in both languages in parallel after the pivot
(research/pivot-decision.md). Mapping: "in which part of the model differences appear, how they shrink when
the recording is longer" = RQ1/H1 (localization, capture budget); "teach a separate model to predict ...
and when it may make a mistake" = RQ2/H2 (transfer forecasting, failure monitors); "spend a small amount of
real data wisely: what to record, which trials" = RQ3/H3; navigation main task, grasping = cross-task RQ4/H4;
"public recordings and 3D scans of real buildings" = tier A (and B), "confirmed on a real robot" = tier C
(validation only; lab not named because the cooperation is not agreed). "Phone" capture: twins in §6
(e.g. EmbodiedSplat) use phone captures. PL and EN checked sentence by sentence: same number of paragraphs
and sentences, same content. Each ≈ 330 words, under 1 page.
-->

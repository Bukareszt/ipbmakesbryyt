# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Współczesna sztuczna inteligencja uczy się na przykładach i zwykle potrzebuje ich ogromnej liczby. W wielu
zastosowaniach dobre przykłady pochodzą jednak tylko z prawdziwego świata, a ich zbieranie jest powolne,
drogie, a czasem ryzykowne. Dobrym przykładem są roboty, na przykład w magazynach, szpitalach, biurach czy
fabrykach. Aby robot nauczył się samodzielnie poruszać lub chwytać przedmioty, potrzebuje milionów prób i
błędów. Dlatego uczy się
go zwykle w symulacji komputerowej, czyli w wirtualnym świecie przypominającym grę. Świat wirtualny różni
się jednak od prawdziwego: inaczej wyglądają ściany, światło i przedmioty. Model sztucznej inteligencji
wyuczony w symulacji często zawodzi, gdy zobaczy prawdziwe obrazy.

Celem rozprawy jest opracowanie metod uczenia maszynowego, które pozwolą sztucznej inteligencji dobrze
działać w prawdziwym świecie przy bardzo małej ilości prawdziwych danych. Pomysł polega na nagraniu
krótkiego filmu z danego miejsca, na przykład korytarza, biura lub stołu roboczego. Na jego podstawie metody
sztucznej inteligencji odtwarzające trójwymiarowe sceny tworzą wierną, fotorealistyczną cyfrową kopię tego
miejsca, tzw. cyfrowego bliźniaka. Opracujemy uniwersalny sposób budowania takich kopii i zmierzymy, ile
kosztuje ich wykonanie i jak wiernie odwzorowują rzeczywistość.
W tej kopii model może bezpiecznie i szybko ćwiczyć miliony razy. Zbadamy też, jak nauczyć model takiego
„widzenia” świata, by obrazy z kopii i z rzeczywistości były dla niego podobne, oraz jak kilka prawdziwych
prób może poprawić symulację. Głównym zadaniem testowym będzie nawigacja robota mobilnego. Metody
zostaną sprawdzone przede wszystkim na publicznie dostępnych wirtualnych budynkach i zbiorach prawdziwych
nagrań, a następnie potwierdzone na prawdziwym robocie w budynkach Politechniki Wrocławskiej. Aby pokazać,
że podejście działa także w innych zadaniach, zastosujemy je również do chwytania i przenoszenia
przedmiotów przez ramię robota, przede wszystkim w publicznie dostępnych symulatorach.

Badania pokażą, ile prawdziwych danych naprawdę potrzeba, aby wyuczony model działał niezawodnie, oraz jak
sprawić, by radził sobie również w miejscach, których wcześniej nie widział, i w innych zadaniach. Spodziewanym efektem jest
znaczne obniżenie kosztu i czasu wdrażania systemów sztucznej inteligencji w nowych miejscach, co może
przyspieszyć wykorzystanie robotów w logistyce, opiece i przemyśle. Opracowane oprogramowanie i dane
zostaną udostępnione publicznie.

## Abstract for general public

Modern artificial intelligence learns from examples, and it usually needs an enormous number of them. In
many applications, however, good examples come only from the real world, where collecting them is slow,
expensive and sometimes risky. Robots, for example in warehouses, hospitals, offices or factories, are a good
example. For a robot to learn to move or grasp objects on its own, it needs millions of trials and errors. That is why it is
usually trained in a computer simulation, a virtual world similar to a video game. The virtual world,
however, differs from the real one: walls, light and objects look different. An artificial intelligence
model trained in simulation often fails when it sees real images.

The goal of this dissertation is to develop machine learning methods that let artificial intelligence work
well in the real world using very little real data. The idea is to record a short video of a place, such as
a corridor, an office or a workbench. From this video, artificial intelligence methods that reconstruct
three-dimensional scenes create a faithful, photorealistic digital copy of the place, a so-called digital
twin. We will develop a universal way of building such copies and measure how much they cost to make and
how faithfully they reproduce reality. In this copy the
model can practice safely and quickly millions of times. We will also study how to teach the model to
"see" the world so that images from the copy and from reality look similar to it, and how a few real trials
can correct the simulation. Mobile-robot navigation will be the main test task. The methods will be
tested mainly on publicly available virtual buildings and collections of real recordings, and then
confirmed on a real robot in the buildings of Wrocław University of Science and Technology. To show that
the approach also works in other tasks, we will also apply it to grasping and moving objects with a robot
arm, mainly in publicly available simulators.

The research will show how much real data is truly needed for a trained model to work reliably, and how
to make it cope with places it has never seen before and with other tasks. The expected result is a significant reduction in
the cost and time of deploying artificial intelligence systems in new places, which may speed up the use
of robots in logistics, care and industry. The software and data developed will be made publicly
available.

<!--
Wave 6 (issue #14), 2026-09-26: broadened in both languages in parallel: robots in general (move or grasp;
factories), digital twin named and the universal twin-building procedure with measured cost and fidelity
(§8 item 5), navigation = main test task, manipulation (grasping and moving objects with a robot arm, mainly
in public simulators) = generalization, "and with other tasks" in the results = cross-task RQ3/H2. PL and EN
re-checked sentence by sentence.
Wave 5 (issue #11), 2026-09-26: reframed ML-first (learning from little real data; reconstruction; aligned
representations = "teach the model to see so that images from the copy and from reality look similar";
correction from a few real trials = RQ4; navigation = test task; evaluation mainly on public virtual
buildings (benchmark scenes) and real-recording datasets, real robot at PWr as confirmation = §7 tiers A/B/C).
The PL and EN versions were checked paragraph by paragraph and say the same thing. Each ≈ 300 words,
under 1 page.
-->

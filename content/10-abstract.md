# §10 Streszczenie popularnonaukowe / Abstract for general public (max 1 page each)

## Streszczenie popularnonaukowe

Roboty mobilne, na przykład w magazynach, szpitalach czy biurach, coraz częściej uczą się poruszać
samodzielnie dzięki metodom sztucznej inteligencji. Takie uczenie wymaga jednak ogromnej liczby
przykładów, często milionów prób i błędów. Zebranie ich na prawdziwym robocie trwa bardzo długo, jest
kosztowne i może prowadzić do uszkodzeń sprzętu. Dlatego roboty uczy się zwykle w symulacji komputerowej,
czyli w wirtualnym świecie przypominającym grę. Problem polega na tym, że świat wirtualny różni się od
prawdziwego: inaczej wyglądają ściany, światło i przedmioty, a robot zachowuje się inaczej na śliskiej
podłodze. Robot wyszkolony w symulacji często gubi się po przeniesieniu do rzeczywistości.

Celem rozprawy jest opracowanie metody, która pozwoli nauczyć robota mobilnego nawigacji w konkretnym
miejscu przy użyciu bardzo małej ilości prawdziwych danych. Pomysł polega na nagraniu krótkiego filmu z
danego miejsca, na przykład korytarza lub biura. Na jego podstawie metody sztucznej inteligencji
odtwarzające trójwymiarowe sceny tworzą wierną, fotorealistyczną cyfrową kopię tego miejsca. W tej kopii
robot może bezpiecznie i szybko ćwiczyć miliony razy, a następnie wrócić do prawdziwego świata.
Informacje z kilku prawdziwych przejazdów posłużą dodatkowo do poprawiania symulacji tak, by coraz lepiej
odpowiadała rzeczywistości. Metoda zostanie sprawdzona na prawdziwym robocie w budynkach Politechniki
Wrocławskiej i porównana z robotami uczonymi w zwykłej symulacji.

Badania pokażą, ile prawdziwych danych naprawdę potrzeba, aby robot działał niezawodnie, oraz jak sprawić,
by radził sobie również w miejscach, których wcześniej nie widział. Spodziewanym efektem jest znaczne
obniżenie kosztu i czasu wdrażania autonomicznych robotów w nowych budynkach, co może przyspieszyć ich
wykorzystanie w logistyce, opiece i przemyśle. Opracowane oprogramowanie i dane zostaną udostępnione
publicznie.

## Abstract for general public

Mobile robots, for example in warehouses, hospitals or offices, increasingly learn to move on their own
using artificial intelligence. This learning needs an enormous number of examples, often millions of
trials and errors. Collecting them on a real robot takes a very long time, is expensive and can damage the
hardware. That is why robots are usually trained in a computer simulation, a virtual world similar to a
video game. The problem is that the virtual world differs from the real one: walls, light and objects look
different, and the robot behaves differently on a slippery floor. A robot trained in simulation often gets
lost when moved to reality.

The goal of this dissertation is to develop a method that teaches a mobile robot to navigate a specific
place using very little real data. The idea is to record a short video of a place, such as a corridor or
an office. From this video, artificial intelligence methods that reconstruct three-dimensional scenes
create a faithful, photorealistic digital copy of the place. In this copy the robot can practice safely and
quickly millions of times, and then return to the real world. Information from a few real runs will also
be used to correct the simulation so that it matches reality more and more closely. The method will be
tested on a real robot in the buildings of Wrocław University of Science and Technology and compared with
robots trained in an ordinary simulation.

The research will show how much real data is truly needed for a robot to work reliably, and how to make it
cope with places it has never seen before. The expected result is a significant reduction in the cost and
time of deploying autonomous robots in new buildings, which may speed up their use in logistics, care and
industry. The software and data developed will be made publicly available.

<!--
Revision for issue #6: aligned with the §2 topic (mobile robots, neural scene reconstruction =
"AI methods that reconstruct 3D scenes", real-to-sim-to-real loop, real-data budget), the §9 evaluation
(real robot at PWr, comparison with a generic simulator) and §8 item 5 (open code and data). The PL and EN
versions were checked paragraph by paragraph and say the same thing. Each is ≈ 290 words, under 1 page.
-->

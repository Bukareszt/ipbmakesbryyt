# Indywidualny Plan Badawczy (IPB)

*Polska wersja robocza do czytania (tłumaczenie treści IPB).*

## 1. Podstawowe dane

| Pole | Wartość |
|---|---|
| Imię i nazwisko | Grzegorz Piotrowski |
| Dyscyplina kształcenia | informatyka techniczna i telekomunikacja |
| Wydział | W4 Wydział Informatyki i Telekomunikacji |
| Katedra | K46 Katedra Sztucznej Inteligencji |
| Data rozpoczęcia kształcenia | 01.10.2025 |
| Nr ORCID | 0009-0004-6013-0461 |
| Promotor | dr hab. inż. Tomasz Jan Kajdanowicz, prof. uczelni, Politechnika Wrocławska (K46, W4), ORCID 0000-0002-8417-1012 |
| Promotor pomocniczy | brak |

## 2. Temat rozprawy doktorskiej

Metody uczenia reprezentacji dla generalizacji modeli świata i polityk z symulacji do rzeczywistości w fizycznej sztucznej inteligencji / Representation learning methods for the simulation-to-reality generalization of world models and policies in physical AI

## 3. Harmonogram przygotowania rozprawy doktorskiej

| Semestr | Zwięzły opis zadania |
|---|---|
| 1 | Udział w zajęciach Szkoły Doktorskiej. Zapoznanie się z literaturą i rozważenie możliwych kierunków badań |
| 2 | Udział w zajęciach Szkoły Doktorskiej i przegląd literatury. Wybór tematu rozprawy doktorskiej wspólnie z promotorem i przygotowanie Indywidualnego Planu Badawczego |
| 3 | Uruchomienie modeli świata, zbioru BridgeData V2 i symulatora SIMPLER na superkomputerach WCSS. Pierwsze eksperymenty z RQ1 w Katedrze K46. Budowa potoku danych z symulacji i ich fotorealistycznego transferu (RQ2) |
| 4 | Zakończenie badania RQ1 w manipulacji i opracowanie jego wyników (H1). Przygotowanie pierwszego artykułu i zgłoszenie go na konferencję lub do czasopisma za 200 punktów, takich jak ICLR lub IEEE RA-L. Pierwsze eksperymenty z RQ2 |
| 5 | Zakończenie badania RQ2 i opracowanie jego wyników (H2). Pierwsze eksperymenty z RQ3. Przygotowanie drugiej publikacji |
| 6 | Zakończenie badania RQ3 (H3). Eksperymenty z RQ4 w niewidzianych scenach i w nawigacji. Testy na rzeczywistym robocie w laboratorium uczelnianym, jeśli pozwoli na to dostęp |
| 7 | Zakończenie badania RQ4 i opracowanie wszystkich wyników (H4). Zgłoszenie artykułu na konferencję lub do czasopisma. Pierwsza wersja rozprawy doktorskiej |
| 8 | Ukończenie, poprawienie i złożenie rozprawy doktorskiej |

## 4. Termin złożenia rozprawy doktorskiej

Wrzesień 2029

## 5. Uzasadnienie wyboru tematu rozprawy doktorskiej

Roboty uczące się metodą prób i błędów potrzebują znacznie więcej prób, niż rzeczywisty robot może wykonać bezpiecznie i tanio, dlatego zwykle trenuje się je w symulacji. Ręcznie budowane symulatory fizyki są szybkie, ale realistyczna kopia każdego nowego miejsca wymaga dużo pracy, a ich obrazy nadal różnią się od obrazów z prawdziwych kamer. Nowszą możliwością jest wyuczony model świata [1]. Jest to sieć neuronowa, która przewiduje, co robot zobaczy po wykonaniu danej akcji. Najnowsze modele świata uczy się na dużych ilościach rzeczywistych nagrań wideo i mogą one pełnić rolę symulatorów. W pracy UniSim [2] polityki sterowania robotem wytrenowano wyłącznie wewnątrz takiego modelu, a następnie zastosowano je na rzeczywistych robotach, a NVIDIA udostępnia swoje modele Cosmos [3] jako podstawę do budowy takich symulatorów.

Powstaje w ten sposób pętla od rzeczywistości do symulacji i z powrotem. Rzeczywiste nagrania służą do wytrenowania modelu świata, wewnątrz niego trenuje się politykę, a politykę stosuje się następnie w rzeczywistym świecie. Słabym punktem jest to, że wyobrażony przebieg nigdy nie jest dokładny. Model może zignorować akcję albo przewidzieć ruch sprzeczny z fizyką [4],[5], więc polityka, która odnosi sukces w modelu świata, może zawieść na rzeczywistym robocie. Lepiej wyglądające wideo tego nie naprawia, ponieważ jakość wizualna modelu świata nie pozwala wiarygodnie przewidzieć, czy polityki odnoszą w nim sukces [5]. Dane z symulacji fizyki są tanie i nieograniczone, jednak w pierwszym takim badaniu, jakie znalazłem, model świata i działania wytrenowany wyłącznie na symulowanych demonstracjach odniósł sukces w około jednej trzeciej prób na rzeczywistym ramieniu robota [6]. Nie znalazłem kontrolowanego porównania sposobów budowy modelu świata z takich danych, tak aby dobrze przewidywał rzeczywisty świat, ani rozstrzygającej odpowiedzi na pytanie, jak dostosować model świata lub politykę do nowego rzeczywistego miejsca przy niewielkiej liczbie rzeczywistych próbek.

Do tych problemów chcę podejść od strony reprezentacji, których uczą się modele. Sieć neuronowa najpierw przekształca obraz w wewnętrzne cechy, a dopiero na ich podstawie podejmuje decyzję. Sposób uczenia tych cech jest wyborem: co model świata ma przewidywać, od jakich danych i jakiego enkodera zaczyna oraz jakie cele uczenia skłaniają cechy do pomijania tego, czym różni się obraz symulowany od rzeczywistego. LeCun argumentował, że model świata powinien przewidywać w takiej przestrzeni cech, a nie w pikselach, aby mógł pomijać szczegóły, których nie da się przewidzieć i które nie mają znaczenia dla sterowania [7]. Celem moich badań jest ustalenie, które z tych wyborów pozwalają polityce wytrenowanej w modelu świata działać na danych rzeczywistych, jak zbudować model świata z danych z symulacji, aby przewidywał rzeczywisty świat, oraz jak przygotować oba modele, aby w nowym rzeczywistym miejscu wystarczyło niewiele danych rzeczywistych. Głównym zadaniem będzie manipulacja, a główne wyniki sprawdzę w niewidzianych scenach i w nawigacji robotów.

Wyniki mogłyby pozwolić robotowi nauczyć się nowej pracy w magazynie, szpitalu lub domu głównie na podstawie symulowanych i przewidywanych doświadczeń, a następnie pracować tam po krótkiej adaptacji w rzeczywistym świecie. Te same pytania pojawiają się w autonomicznej jeździe, gdzie generatywne modele świata już teraz tworzą scenariusze do treningu i testów, oraz w modelach świata i działania (WAM), które w jednej sieci przewidują przyszłość i wybierają akcje.

## 6. Zarys aktualnego stanu badań w tematyce rozprawy doktorskiej

Idea trenowania sterownika wewnątrz wyuczonego modelu środowiska sięga co najmniej pracy Ha i Schmidhubera [1], w której agent nauczył się grać w grę wewnątrz własnego „snu”, a następnie grał w prawdziwą grę. Od 2023 roku duże modele generatywne trenowane na nagraniach wideo z internetu i z robotów są używane jako interaktywne symulatory rzeczywistego świata. Yang i in. [2] pokazali w pracy UniSim, że polityki wytrenowane wyłącznie w takim modelu działały w rzeczywistym świecie bez dalszego treningu. Bar i in. [8] zbudowali Navigation World Models (NWM), które przewidują wideo z perspektywy pierwszej osoby poruszającego się robota i planują, symulując kandydackie trajektorie. Platforma Cosmos firmy NVIDIA [3] udostępnia otwarte bazowe modele świata, które mają być dotrenowywane dla konkretnych robotów i pojazdów. NVIDIA buduje też symulatory fizyki, Isaac Sim i Isaac Lab [9], i używa Cosmos Transfer [10], aby ich rendery wyglądały realistycznie. Cosmos Transfer generuje wideo na podstawie map głębi lub segmentacji, dzięki czemu render zachowuje swój układ i ruch, a symulowane akcje pozostają poprawne. DreamGen [11] dotrenowuje model świata generujący wideo na docelowym robocie, generuje nagrania nowych zachowań, oznacza je akcjami odtworzonymi z wideo i trenuje na nich politykę. W ten sposób robot humanoidalny nauczył się 22 nowych zachowań na podstawie danych z teleoperacji jednego zadania chwytania i odkładania.

Nowszy nurt łączy model świata i politykę w model świata i działania (WAM, World Action Model), czyli jedną sieć, która przewiduje zarówno przyszłe stany świata, jak i akcje robota. Autorzy DreamZero [12], znanego modelu tego rodzaju, podali, że uogólniał się on na nowe zadania i środowiska ponad dwukrotnie lepiej niż modele wizja-język-akcja. Przenoszenie modeli WAM z symulacji do rzeczywistości prawie nie zostało zbadane. W pierwszej takiej pracy, jaką znalazłem [6], model wideo Cosmos dotrenowano do roli polityki, wytrenowano go wyłącznie na syntetycznych demonstracjach i uzyskano średnio 35% sukcesów na rzeczywistym ramieniu Franka bez żadnych demonstracji z rzeczywistego robota.

Drugi nurt pyta, co model świata powinien przewidywać. LeCun [7] argumentuje, że powinien on przewidywać reprezentację przyszłej obserwacji, a nie jej piksele, aby mógł pomijać nieprzewidywalne szczegóły, takie jak tekstura czy szum czujników. DINO-WM [13] przewiduje zamrożone cechy modelu DINOv2, sieci wizyjnej wstępnie wytrenowanej bez etykiet, i planuje bez rekonstrukcji pikseli. Assran i in. [14] wstępnie wytrenowali model V-JEPA 2 na ponad milionie godzin wideo, a jego wersja warunkowana akcjami, dotrenowana na mniej niż 62 godzinach nagrań robotów, planowała chwytanie i odkładanie przedmiotów na rzeczywistych ramionach Franka w nieznanych jej laboratoriach. W pracy SkyJEPA [15] wytrenowano taki model świata na automatycznie wygenerowanych danych i opisano sterowanie kwadrokopterem w lotach na zewnątrz z przeniesieniem z symulacji do rzeczywistości bez dodatkowego treningu, ze stanami, a nie obrazami, na wejściu. W badaniu modeli świata do wizyjnej nawigacji kwadrokoptera model, który uzyskał najlepszy wynik w symulacji, zawiódł na rzeczywistej platformie, podczas gdy odporność wyuczonej reprezentacji na zmianę środowiska przewidywała przeniesienie do rzeczywistości [16]. Nilaksh i in. [17] porównali sześć enkoderów jako podstawę modelu świata trenowanego na BridgeData V2, rzeczywistym zbiorze danych z manipulacji, i stwierdzili, że enkodery wstępnie wytrenowane na treści semantycznej lepiej sprawdzały się w planowaniu i w ocenie stałej polityki niż enkodery uczone rekonstrukcji pikseli. W nawigacji model RAE-NWM [18] przewidywał cechy DINOv2 zamiast kodów autoenkodera używanego w NWM i planował z nimi lepiej na zbiorach SACSoN i SCAND, ale nie na RECON. W żadnej z tych prac nie trenowano polityk wewnątrz modeli i nie znalazłem kontrolowanego porównania tego, jak cel predykcji i wstępnie wytrenowany enkoder wpływają na skuteczność na danych rzeczywistych polityk trenowanych wewnątrz modelu świata.

Modele świata służą też do oceny i ulepszania polityk. Ctrl-World [19], wytrenowany na zbiorze DROID, uszeregował polityki bez rzeczywistych przebiegów i poprawił politykę przez dotrenowanie jej na wyobrażonych udanych trajektoriach. W pracy World-in-World [5] przetestowano modele świata w zamkniętej pętli i stwierdzono, że jakość wizualna nie gwarantuje sukcesu w zadaniu, a większe znaczenie ma to, jak wiernie model podąża za akcjami. Autorzy VLAW [4] stwierdzili, że obecnym modelom świata brakuje dokładności fizycznej potrzebnej do ulepszania polityk. W przypadku symulatorów fizyki Li i in. [20] pokazali w pracy SIMPLER, że sceny wizualnie dopasowane do rzeczywistych obrazów pozwalają uszeregować polityki niemal w tej samej kolejności co rzeczywiste uruchomienia.

Niemal wszystkie duże modele świata trenuje się na rzeczywistych nagraniach wideo. Trenowanie ich na danych z symulacji fizyki jest atrakcyjne, ponieważ takie dane są tanie, zawierają dokładne akcje i można je generować bez ograniczeń, ale przenosi to lukę między symulacją a rzeczywistością do modelu świata. Klasyczne narzędzia do tej luki powstały z myślą o politykach. Randomizacja domeny [21] zmienia parametry symulatora, takie jak tekstury, tak aby rzeczywistość wyglądała jak kolejny wariant, a wspólny trening na danych symulowanych i małym zbiorze rzeczywistym poprawił manipulację w rzeczywistym świecie [22]. W przypadku modeli świata SimDist [23] wstępnie wytrenował model świata w symulacji i danymi rzeczywistymi dostosował tylko jego część przewidującą następny stan. Wang i in. [24] dotrenowali enkoder i politykę modelu świata wstępnie wytrenowanego w symulacji na małym zbiorze rzeczywistych demonstracji, z pozycjami obiektów, a nie obrazami, na wejściu. Nie znalazłem kontrolowanego badania tego, które wybory w uczeniu reprezentacji, takie jak randomizacja lub transfer wyglądu, cel uczenia parujący widoki symulowane i fotorealistyczne czy wspólny trening, sprawiają, że model świata wytrenowany na danych z symulacji dobrze przewiduje rzeczywiste nagrania.

Gdy dostępna jest niewielka ilość rzeczywistych danych, wykorzystuje się je na różne sposoby. VLAW [4] dotrenowuje model świata na rzeczywistych przebiegach, a następnie ulepsza politykę danymi syntetycznymi z tego modelu, DreamGen [11] dotrenowuje swój model świata generujący wideo na docelowym robocie, a LoRA [25] tanio dostosowuje duże wstępnie wytrenowane modele, aktualizując tylko niewielki zbiór dodanych wag. SimDist [23] trenował swój enkoder na danych z symulacji i nie zmieniał go podczas adaptacji do rzeczywistości. Nie znalazłem porównania tego, jak wstępnie trenować reprezentację modelu świata i trenowanej w nim polityki, aby później potrzebna była jak najmniejsza liczba rzeczywistych próbek. Żadna z tych prac nie pyta, jak oba modele powinny uczyć się reprezentacji, aby polityka wytrenowana w modelu świata działała na danych rzeczywistych po niewielkiej adaptacji, i tę lukę podejmują moje pytania badawcze w sekcji 7.

Cytowane prace wymieniam w sekcji 12.

## 7. Pytania i hipotezy badawcze

Celem mojej rozprawy jest opracowanie metod uczenia reprezentacji, dzięki którym wyuczone modele świata mogą pełnić rolę symulatorów w uczeniu robotów generalizującym do rzeczywistego świata. Przez uczenie reprezentacji rozumiem to, jak model świata i polityka uczą się swoich wewnętrznych cech: co przewiduje model świata, od jakich danych i jakiego enkodera zaczynają oraz jakie cele uczenia sprawiają, że cechy pomijają to, czym różnią się obrazy symulowane od rzeczywistych. Te wybory będę oceniał wyłącznie po obserwowalnych wynikach.

Moja praca musi spełniać kilka ograniczeń. Będę dotrenowywał istniejące, wstępnie wytrenowane modele świata i polityki na akademickich klastrach GPU, zamiast trenować duże modele od podstaw. Nie mam własnego robota, dlatego będę pracował na publicznych zbiorach danych, a na rzeczywistym robocie przeprowadzę testy tylko wtedy, gdy pozwoli na to dostęp. Przez skuteczność na danych rzeczywistych rozumiem to, jak blisko akcje polityki odpowiadają akcjom z odłożonych rzeczywistych nagrań, oraz to, jak często polityka odnosi sukces w SIMPLER, symulatorze scen odtworzonych z rzeczywistych nagrań. Jest to przybliżenie sukcesu na rzeczywistym robocie. Głównym zadaniem jest manipulacja, a nawigacja służy do sprawdzenia wyników.

Moje pytania badawcze i hipotezy są następujące:

1. RQ1. Które wybory w uczeniu reprezentacji wpływają na to, jak dobrze polityka wytrenowana w modelu świata zbudowanym z danych rzeczywistych działa na danych rzeczywistych, w porównaniu z polityką wytrenowaną bezpośrednio na tych danych?
2. H1. Przy tym samym predyktorze i tych samych danych model świata przewidujący skompresowane cechy enkodera wstępnie wytrenowanego na rzeczywistym wideo daje lepsze polityki niż model przewidujący kody autoenkodera pikseli, a zysk utrzymuje się, gdy oba modele równie wiernie podążają za akcjami.
3. RQ2. Które wybory w uczeniu reprezentacji sprawiają, że model świata wytrenowany na danych z symulacji fizyki dobrze przewiduje rzeczywiste nagrania i daje polityki, których akcje odpowiadają nagranym rzeczywistym akcjom?
4. H2. Uczenie enkodera tak, aby dawał te same cechy dla symulowanej klatki i jej fotorealistycznej wersji, pomaga bardziej niż samo dodanie fotorealistycznych klatek do danych treningowych, chyba że luka wynika głównie z symulowanej fizyki.
5. RQ3. Jak wstępnie trenować enkoder modelu świata i polityki, aby ich adaptacja do nowych rzeczywistych scen wymagała mniej danych rzeczywistych?
6. H3. Enkoder dalej wstępnie trenowany na danych rzeczywistych i symulowanych z celem uczenia z H2 osiąga skuteczność dotrenowania na wszystkich dostępnych danych rzeczywistych przy mniejszej ilości danych rzeczywistych niż pozostałe warianty wstępnego treningu.
7. RQ4. Czy te odpowiedzi utrzymują się w scenach niewidzianych podczas treningu i czy odpowiedź na RQ1 utrzymuje się w nawigacji robotów?
8. H4. Wybory najlepsze w manipulacji poprawiają skuteczność na danych rzeczywistych względem tej samej metody bazowej także w niewidzianych scenach i w nawigacji.
9. Plan awaryjny. Jeśli wybory dotyczące reprezentacji nie będą miały wyraźnego wpływu, zbadam zamiast tego, jak proporcje, ilość i różnorodność danych generowanych, symulowanych i rzeczywistych wpływają na skuteczność na danych rzeczywistych.

## 8. Wkład spodziewanych wyników dla rozwoju dyscypliny naukowej

Głównym spodziewanym wkładem mojej rozprawy jest zestaw metod uczenia reprezentacji, dzięki którym wyuczone modele świata mogą pełnić rolę symulatorów w uczeniu robotów generalizującym do rzeczywistego świata. Rozprawa powinna dostarczyć dowodów na to, które wybory, takie jak cel predykcji i wstępnie wytrenowany enkoder, wpływają na to, jak dobrze polityki wytrenowane w modelu świata działają na danych rzeczywistych, i czy te wybory pomagają także w niewidzianych scenach i w nawigacji (RQ1, RQ4). Powinna też dostarczyć metod treningu, dzięki którym modele świata budowane z danych z symulacji fizyki lepiej przewidują rzeczywiste nagrania (RQ2), oraz metod wstępnego treningu, które pozwalają dostosować model świata i politykę do nowego rzeczywistego otoczenia przy mniejszej ilości danych rzeczywistych niż pełne dotrenowanie (RQ3).

Modele świata stają się powszechnym sposobem tworzenia danych treningowych i oceny polityk sterowania robotami, a modele świata i działania łączą dziś model świata i politykę w jednej sieci. Moje wyniki powinny pokazać, które własności modelu świata muszą być poprawne dla danego zadania, co jest przydatne zarówno dla tych, którzy budują modele świata, jak i dla tych, którzy trenują w nich polityki. Wyniki dotyczące wstępnego treningu i celów uczenia, które pomijają różnicę między obrazami symulowanymi a rzeczywistymi, mogą być przydatne także szerzej w adaptacji domenowej. Planuję udostępnić kod, protokół ewaluacji oraz, tam gdzie pozwalają na to licencje, wytrenowane modele, aby inni mogli porównywać metody w ten sam sposób.

## 9. Planowane metody badawcze

Moja praca będzie głównie empiryczna. Nie znalazłem ugruntowanej teorii tego, jak modele świata i polityki w nich trenowane generalizują do rzeczywistości, dlatego przeprowadzę kontrolowane porównania, w których zmienia się jeden wybór naraz. Nie będę trenował dużych modeli od podstaw. Będę dotrenowywał istniejące, wstępnie wytrenowane modele świata, enkodery i polityki, których kod i wagi są publiczne. Głównym ustawieniem będzie manipulacja na BridgeData V2, publicznym zbiorze danych nagranym z ramieniem robota WidowX, razem z SIMPLER [20], który odtwarza niektóre sceny BridgeData V2 w symulatorze fizyki. Dla H1 wytrenuję ten sam predyktor na tych samych danych i zmienię tylko to, co przewiduje: kody autoenkodera obrazów uczonego rekonstrukcji pikseli albo cechy enkodera wstępnie wytrenowanego na rzeczywistym wideo, takiego jak V-JEPA 2 [14]. Pójdę za ustawieniem z pracy Nilaksha i in. [17], której kod jest publiczny. Politykę w każdym modelu świata wytrenuję, generując raz wyobrażone trajektorie, zachowując te, które jeden klasyfikator sukcesu uzna za udane, i dotrenowując na nich politykę. W nawigacji użyję RAE-NWM [18] na zbiorach RECON i SCAND, przeniosę tam tylko wybory, które okazały się najlepsze w manipulacji, i zachowam udostępnione ustawienia RAE-NWM.

W RQ2 wygeneruję dane z symulacji za pomocą zaprogramowanych rozwiązań zadań w scenach SIMPLER i dodam losowe odmiany ich wyglądu i fizyki. Jeśli ten symulator nie pozwoli na potrzebne odmiany, użyję zamiast niego NVIDIA Isaac Lab [9]. Renderom nadam realistyczny wygląd za pomocą Cosmos Transfer [10], sterowanego mapami głębi. Modele świata trenowane na tych danych będą się różnić jednym wyborem: randomizacją wyglądu, fotorealistycznym transferem, randomizacją fizyki, celem uczenia nadającym każdej symulowanej klatce i jej fotorealistycznej wersji te same cechy albo wspólnym treningiem z małym zbiorem rzeczywistym. W RQ3 będę kontynuował wstępny trening mniejszych udostępnionych enkoderów na danych rzeczywistych albo na danych rzeczywistych i symulowanych, a następnie dostosuję model świata i politykę do nowych scen przy kilku małych ilościach danych rzeczywistych, przez pełne dotrenowanie albo metodą LoRA [25].

Nie mam własnego robota, dlatego pomiary przeprowadzę na danych publicznych. Model świata ocenię po tym, jak dobrze przewiduje odłożone rzeczywiste nagrania, standardowymi miarami podobieństwa obrazów i wideo, takimi jak PSNR, LPIPS i FVD. Politykę ocenię po tym, jak blisko jej akcje odpowiadają akcjom z odłożonych rzeczywistych nagrań, oraz po tym, jak często odnosi sukces w SIMPLER, gdzie działa w zamkniętej pętli. W RQ2 nie uznam sukcesu w SIMPLER za dowód, ponieważ dane treningowe pochodzą z tego samego symulatora. Zmierzę też, jak wiernie każdy model świata podąża za akcjami, i porównam cele predykcji przy podobnym podążaniu za akcjami, w razie potrzeby na wcześniejszych punktach kontrolnych, aby nie pomylić wpływu celu predykcji z tym efektem. W nawigacji zmierzę, jak blisko ścieżka polityki jest nagranej ścieżki i czy polityka osiąga cel. W RQ3 przedstawię skuteczność w funkcji ilości danych rzeczywistych, co pokaże, ile danych rzeczywistych potrzebuje każdy wariant. W RQ4 porównam zysk każdego najlepszego wyboru w scenach treningowych z jego zyskiem w niewidzianych scenach i w nawigacji. Wszystkie te miary są przybliżeniem sukcesu na rzeczywistym robocie i zaznaczę to przy każdym wyniku. Jeśli pozwoli na to dostęp, wybrane wyniki sprawdzę na rzeczywistym robocie w laboratorium uczelnianym.

Aby uniknąć stronniczości, wyłączę nagrania BridgeData V2 ze scen odtworzonych w SIMPLER z treningu modeli świata i użyję ich tylko do adaptacji i testów. Jako metodę bazową wytrenuję tę samą politykę bezpośrednio na danych rzeczywistych użytych do zbudowania modelu świata, aby sprawdzić, czy wyobrażone dane w ogóle pomagają. Moje metody porównam z randomizacją domeny [21] i wspólnym treningiem na danych symulowanych i rzeczywistych [22], przy tym samym budżecie treningu i tej samej ilości danych rzeczywistych. Powtórzę treningi dla kilku ziaren losowych, rozdzielę dane do treningu, wyboru modelu i testów oraz ręcznie sprawdzę klasyfikator sukcesu na próbce przebiegów z każdego modelu świata.

Do treningu użyję biblioteki PyTorch, do pobierania i publikowania modeli i danych serwisu Hugging Face, a do kontroli wersji systemu Git z serwisem GitHub. Eksperymenty uruchomię na węzłach z GPU H100 Wrocławskiego Centrum Sieciowo-Superkomputerowego (WCSS) oraz na zasobach PLGrid, gdzie zadaniami zarządza SLURM. Będę przestrzegał licencji otwartych wag, z których niektóre dopuszczają wyłącznie użytek niekomercyjny. Zamierzam korzystać z agentów programistycznych opartych na sztucznej inteligencji, takich jak Claude Code, aby szybciej pisać i testować kod oraz nadzorować długie eksperymenty.

Udostępnię swój kod oraz, tam gdzie pozwalają na to licencje, wytrenowane punkty kontrolne. Wyniki planuję publikować na konferencjach i w czasopismach za 200 punktów z listy ministerialnej, takich jak NeurIPS, ICML, ICLR, CVPR, RSS i IEEE RA-L, a artykuły udostępniać także jako preprinty w serwisie arXiv.

## 10. Streszczenie popularnonaukowe

### Streszczenie popularnonaukowe

Roboty mogą uczyć się nowych umiejętności w komputerowej kopii świata. Jest to bezpieczniejsze i tańsze niż nauka na prawdziwym robocie. Jedną z takich kopii jest model świata. To sieć neuronowa, która obejrzała wiele nagrań wideo i przewiduje, co robot zobaczy po wykonaniu ruchu. Te przewidywania nigdy nie są jednak dokładne. Robot, który nauczył się czegoś w modelu świata, w prawdziwym świecie często sobie nie radzi. Chcę sprawdzić, jak modele świata i roboty powinny uczyć się widzieć świat, aby ich umiejętności działały także w rzeczywistości. Zbadam też, jak budować modele świata z tanich symulacji komputerowych i jak przygotować robota, aby w nowym miejscu wystarczyło mu niewiele prawdziwej praktyki. Zajmę się głównie robotami, które chwytają i przestawiają przedmioty, a wyniki sprawdzę też na robotach, które jeżdżą. Chcę opracować metody, dzięki którym roboty będą uczyć się nowej pracy szybciej, taniej i bezpieczniej.

### Abstract for general public

Robots can learn new skills in a computer copy of the world. This is safer and cheaper than learning on a real robot. One such copy is a world model. It is a neural network that has watched many videos and predicts what a robot will see after it moves. But these predictions are never exact. A robot that learned something in a world model often struggles in the real world. I want to find out how world models and robots should learn to see the world so that their skills also work in reality. I will also study how to build world models from cheap computer simulations and how to prepare a robot so that it needs only a little real practice in a new place. I will mainly work with robots that grasp and move objects, and I will also check the results on robots that drive around. I want to develop methods that let robots learn new work faster, more cheaply and more safely.

## 11. Termin oddania do druku artykułu naukowego lub monografii

Wrzesień 2027 (planowane zgłoszenie na konferencję lub do czasopisma za 200 punktów z listy ministerialnej, takie jak konferencja ICLR 2028 lub czasopismo IEEE Robotics and Automation Letters).

## 12. Inne

Korzystałem z Claude (przez Claude Code) przy wyszukiwaniu literatury, pisaniu wstępnych wersji tekstu i redakcji, a całą treść i wszystkie pozycje bibliografii przejrzałem samodzielnie.

### Bibliografia

[1] Ha, D., & Schmidhuber, J. (2018). World models. arXiv:1803.10122.

[2] Yang, S., et al. (2024). Learning interactive real-world simulators. ICLR.

[3] Agarwal, N., et al. (2025). Cosmos world foundation model platform for physical AI. arXiv:2501.03575.

[4] Guo, Y., et al. (2026). VLAW: Iterative co-improvement of vision-language-action policy and world model. ICML.

[5] Zhang, J., et al. (2026). World-in-World: World models in a closed-loop world. ICLR.

[6] Wang, Z., et al. (2026). Efficient sim-to-real transfer of world-action models from synthetic priors. arXiv:2606.31101.

[7] LeCun, Y. (2022). A path towards autonomous machine intelligence. OpenReview.

[8] Bar, A., et al. (2025). Navigation world models. CVPR.

[9] Mittal, M., et al. (2025). Isaac Lab: A GPU-accelerated simulation framework for multi-modal robot learning. arXiv:2511.04831.

[10] Abu Alhaija, H., et al. (2025). Cosmos-Transfer1: Conditional world generation with adaptive multimodal control. arXiv:2503.14492.

[11] Jang, J., et al. (2025). DreamGen: Unlocking generalization in robot learning through video world models. CoRL.

[12] Ye, S., et al. (2026). World action models are zero-shot policies. arXiv:2602.15922.

[13] Zhou, G., et al. (2025). DINO-WM: World models on pre-trained visual features enable zero-shot planning. ICML.

[14] Assran, M., et al. (2025). V-JEPA 2: Self-supervised video models enable understanding, prediction and planning. arXiv:2506.09985.

[15] Rao, P., et al. (2026). SkyJEPA: Learning long-horizon world models for zero-shot sim-to-real control of quadrotors. arXiv:2606.23444.

[16] Zanatta, L., Malczyk, G., & Alexis, K. (2026). Generalization of world models under environmental variability for vision-based quadrotor navigation. arXiv:2606.05015.

[17] Nilaksh, Jha, S., Zholus, A., & Chandar, S. (2026). Reconstruction or semantics? What makes a latent space useful for robotic world models. arXiv:2605.06388.

[18] Zhang, M., et al. (2026). RAE-NWM: Navigation world model in dense visual representation space. arXiv:2603.09241.

[19] Guo, Y., et al. (2026). Ctrl-World: A controllable generative world model for robot manipulation. ICLR.

[20] Li, X., et al. (2024). Evaluating real-world robot manipulation policies in simulation. CoRL.

[21] Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. IROS.

[22] Maddukuri, A., et al. (2025). Sim-and-real co-training: A simple recipe for vision-based robotic manipulation. RSS.

[23] Levy, J., et al. (2026). Simulation distillation: Pretraining world models in simulation for rapid real-world adaptation. RSS.

[24] Wang, Y., et al. (2025). A recipe for efficient sim-to-real transfer in manipulation with online imitation-pretrained world models. arXiv:2510.02538.

[25] Hu, E. J., et al. (2022). LoRA: Low-rank adaptation of large language models. ICLR.

## 13. Określenie planowanej formy współpracy z promotorem

Z promotorem planujemy spotykać się co tydzień. Na każdym spotkaniu będę przedstawiał postępy i wyniki, a razem będziemy ustalać kolejne kroki i omawiać wspólne publikacje. Będę też uczestniczył w cotygodniowych spotkaniach grupy doktorantów promotora. Między spotkaniami będziemy się kontaktować mailowo i przez komunikatory. Kod, wytrenowane modele i źródła LaTeX publikacji będziemy przechowywać we wspólnych repozytoriach Git.

## 14. Opinia promotora pomocniczego

Nie dotyczy (promotor pomocniczy nie został wyznaczony).

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
| Promotor pomocniczy | — |

## 2. Temat rozprawy doktorskiej

Metody uczenia reprezentacji dla generalizacji polityk uczonych w modelach świata do rzeczywistości w fizycznej sztucznej inteligencji / Representation learning methods for the simulation-to-reality generalization of policies trained in world models for physical AI

## 3. Harmonogram przygotowania rozprawy doktorskiej

| Semestr | Zwięzły opis zadania |
|---|---|
| 1 | Udział w zajęciach Szkoły Doktorskiej. Zapoznanie się z literaturą i rozważenie możliwych kierunków badań |
| 2 | Udział w zajęciach Szkoły Doktorskiej i przegląd literatury. Wybór tematu rozprawy doktorskiej wspólnie z promotorem i przygotowanie Indywidualnego Planu Badawczego |
| 3 | Przygotowanie środowiska badawczego z modelami świata, symulatorem fizyki i publicznymi zbiorami danych z robotów. Wstępne eksperymenty dotyczące szkodliwych błędów symulacji tworzonej przez model świata (RQ1) |
| 4 | Dalsze eksperymenty z RQ1. Przygotowanie pierwszej publikacji i zgłoszenie jej na konferencję lub do czasopisma za 200 punktów z zakresu uczenia maszynowego lub uczenia robotów, takich jak ICLR, RSS lub IEEE RA-L. Pierwsze eksperymenty z RQ2 |
| 5 | Eksperymenty dotyczące lokalizacji luki wewnątrz polityk (czyli sieci neuronowych wybierających akcje robota na podstawie jego obserwacji) i wyrównywania reprezentacji (RQ2). Przygotowanie publikacji naukowej |
| 6 | Eksperymenty dotyczące wyboru rzeczywistych przebiegów (RQ3) oraz przenoszenia wyników na niewidziane sceny i między zadaniami (RQ4). Przygotowanie publikacji oraz, jeśli pozwoli na to dostęp, testy na rzeczywistym robocie |
| 7 | Końcowe eksperymenty i zgłoszenie artykułu na konferencję lub do czasopisma. Pierwsza wersja rozprawy doktorskiej |
| 8 | Ukończenie i poprawienie rozprawy doktorskiej, a następnie jej złożenie |

## 4. Termin złożenia rozprawy doktorskiej

Wrzesień 2029

## 5. Uzasadnienie wyboru tematu rozprawy doktorskiej

Roboty uczące się metodą prób i błędów potrzebują znacznie więcej prób, niż rzeczywisty robot może wykonać bezpiecznie i tanio, dlatego zwykle trenuje się je w symulacji. Ręcznie budowane symulatory fizyki są szybkie, ale stworzenie realistycznej kopii każdego nowego miejsca wymaga dużo pracy, a generowane przez nie obrazy nadal różnią się od obrazów z prawdziwych kamer. Nowszą możliwością jest wyuczony model świata [1]. Jest to sieć neuronowa, która przewiduje, co robot zobaczy po wykonaniu danej akcji. Najnowsze modele świata uczy się na dużych ilościach rzeczywistych nagrań wideo i mogą one pełnić rolę symulatorów. W pracy UniSim [2] polityki sterowania robotem wytrenowano wyłącznie wewnątrz takiego modelu, a następnie zastosowano je na rzeczywistych robotach. Navigation World Models [3] na podstawie jednego zdjęcia nieznanego miejsca wyobrażają sobie, jak wyglądałoby przejście przez nie, a modele Cosmos firmy NVIDIA [4] są udostępniane jako podstawa do budowy takich symulatorów.

Słabym punktem tego podejścia jest to, że wyobrażony przebieg nigdy nie jest dokładny. Model może zignorować akcję i pokazać robota stojącego w miejscu. Może pozwolić, by chwytak przeszedł przez przedmiot, albo pokazać podniesienie przedmiotu bez właściwego kontaktu. Drobne błędy sumują się też w długich przebiegach, aż scena oddala się od wszystkiego, co jest fizycznie możliwe [5],[6]. Polityka, która odnosi sukces w modelu świata, może więc zawieść na rzeczywistym robocie. W pierwszym badaniu, w którym politykę tego rodzaju przeniesiono z treningu wyłącznie na danych syntetycznych na rzeczywiste ramię robota, odniosła ona sukces w około jednej trzeciej prób [7]. Wciąż nie wiadomo, które z tych błędów rzeczywiście szkodzą polityce i dlaczego. Lepiej wyglądające wideo nie daje odpowiedzi na to pytanie, ponieważ jakość wizualna modelu świata nie pozwala wiarygodnie przewidzieć, czy polityki odnoszą w nim sukces [6].

Chcę odpowiedzieć na to pytanie, zaglądając do wnętrza modeli. Sieć neuronowa nie działa bezpośrednio na obrazie. Najpierw przekształca go w wewnętrzne cechy, nazywane reprezentacjami, i na ich podstawie podejmuje decyzję. LeCun argumentował, że model świata również powinien przewidywać w takiej przestrzeni reprezentacji, a nie w pikselach, aby mógł pomijać szczegóły, których nie da się przewidzieć i które nie mają znaczenia dla sterowania [8]. Model V-JEPA 2 [9] pokazał, że model świata tego rodzaju potrafi planować ruchy rzeczywistego ramienia robota. Moje robocze założenie wynika z tej samej idei. Błąd modelu świata, który nie zmienia reprezentacji, powinien wyrządzać niewielką szkodę, a błąd zmieniający cechy, od których zależy decyzja, powinien prowadzić do porażek [10]. Daje to mierzalny sposób badania luki między symulacją a rzeczywistością. Najpierw sprawdzę, które błędy symulacji tworzonej przez model świata zmieniają reprezentacje w szkodliwy sposób. Następnie znajdę etap wewnątrz polityki, na którym rzeczywiste dane wejściowe tracą informacje potrzebne do wykonania zadania, i tam skoryguję reprezentacje. Zbadam też, jak wybrać nieliczne rzeczywiste przebiegi, które najlepiej poprawiają zarówno model świata, jak i politykę, oraz czy korzyści utrzymują się w nowych scenach i w drugim zadaniu. Będę pracował nad dwoma równie ważnymi zadaniami, nawigacją robotów i manipulacją robotyczną.

Odpowiedź pokazałaby, które własności modelu świata muszą być dokładne dla danego zadania i gdzie warto zbierać dodatkowe rzeczywiste dane. W praktyce robot mógłby nauczyć się nowej pracy w magazynie, szpitalu lub domu głównie na podstawie przewidywanych doświadczeń, a następnie niezawodnie tam pracować po niewielkiej adaptacji w rzeczywistym świecie. Te same pytania pojawiają się w autonomicznej jeździe, gdzie generatywne modele świata już teraz tworzą scenariusze do treningu i testów, oraz w modelach, które w jednej sieci przewidują przyszłość i wybierają akcje.

## 6. Zarys aktualnego stanu badań w tematyce rozprawy doktorskiej

Idea uczenia modelu środowiska i trenowania sterownika wewnątrz jego przewidywań sięga co najmniej pracy Ha i Schmidhubera [1], w której agent nauczył się grać w grę wewnątrz własnego „snu”, a następnie grał w prawdziwą grę. DreamerV3 [11] przekształcił trening w wyobraźni w ogólną metodę, która działa z jedną stałą konfiguracją w ponad 150 zadaniach. Takie modele są małe i uczone dla jednego środowiska. Od 2023 roku duże modele generatywne trenowane na nagraniach wideo z internetu i z robotów są używane jako interaktywne symulatory rzeczywistego świata. UniSim [2] nauczył się symulatora z połączonych danych internetowych, robotycznych i nawigacyjnych, a polityki wytrenowane wyłącznie w nim działały w rzeczywistym świecie bez dalszego treningu. Navigation World Models (NWM) [3] przewidują wideo z perspektywy poruszającego się robota i planują, symulując kandydackie trajektorie. Platforma Cosmos firmy NVIDIA [4] udostępnia otwarte bazowe modele świata, które mają być dotrenowywane do postaci modeli świata dla konkretnych robotów i pojazdów.

NVIDIA łączy też te modele ze swoimi symulatorami fizyki, Isaac Sim i Isaac Lab [12]. Cosmos Transfer, należący do rodziny Cosmos, zamienia rendery z symulatora, takie jak mapy głębi czy segmentacji, w fotorealistyczne wideo o tej samej geometrii i ruchu, dzięki czemu symulowane akcje pozostają poprawne. DreamGen [13] dotrenowuje model świata generujący wideo na docelowym robocie, generuje nagrania nowych zachowań, oznacza je pseudoakcjami i trenuje na nich politykę. Dzięki tym danym polityka GR00T N1 firmy NVIDIA nauczyła się 22 nowych zachowań na podstawie danych z teleoperacji jednego zadania, a jej skuteczność wzrosła na trzech rzeczywistych robotach.

Nowszy nurt łączy model świata z polityką. Model świata i działania (WAM, World Action Model) to jedna sieć, która przewiduje zarówno przyszłe stany świata, jak i akcje robota. Termin wprowadzono w pracy DreamZero [14], której autorzy podali, że taki model uogólniał się na nowe zadania i środowiska ponad dwukrotnie lepiej niż modele wizja-język-akcja (VLA). Modele VLA odwzorowują obrazy i polecenia bezpośrednio na akcje. Przenoszenie modeli świata i działania (WAM) z symulacji do rzeczywistości prawie nie zostało zbadane. W pierwszej pracy, która je opisała [7], model wideo Cosmos dotrenowano do roli takiej polityki, wytrenowano go wyłącznie na syntetycznych demonstracjach i uzyskano średnio 35% sukcesów na rzeczywistym ramieniu Franka bez żadnych rzeczywistych danych treningowych.

W artykule programowym LeCuna [8] autor argumentuje, że model świata nie powinien przewidywać pikseli. W jego architekturze JEPA (Joint Embedding Predictive Architecture) model koduje bieżącą i przyszłą obserwację i przewiduje przyszłą reprezentację, dzięki czemu może pomijać nieprzewidywalne szczegóły, takie jak tekstura czy szum czujników. DINO-WM [15] przewiduje zamrożone cechy wstępnie wytrenowanego modelu DINOv2 i planuje bez rekonstrukcji pikseli. Model V-JEPA 2 [9] wstępnie wytrenowano na ponad milionie godzin wideo. Jego wersję warunkowaną akcjami, V-JEPA 2-AC, dotrenowano na mniej niż 62 godzinach nagrań robotów ze zbioru DROID. Model ten planował chwytanie i odkładanie przedmiotów na rzeczywistych ramionach Franka w nieznanych mu laboratoriach, bez nagród. W pracy SkyJEPA [16] wytrenowano model świata JEPA na danych symulowanych i sterowano nim rzeczywistym kwadrokopterem bez treningu w rzeczywistym świecie. Prace te pokazują, że modele świata działające w przestrzeni reprezentacji mogą przenosić się do rzeczywistości. Nie mierzą one jednak luki między symulowanymi a rzeczywistymi danymi wejściowymi w tej przestrzeni ani nie wiążą jej z sukcesem polityki.

Modele świata służą też do oceny polityk zamiast uruchamiania ich na robocie. Ctrl-World [17], wytrenowany na zbiorze DROID, uszeregował polityki bez rzeczywistych przebiegów i poprawił politykę przez dotrenowanie jej na wyobrażonych udanych trajektoriach. Symulator świata oparty na modelu Veo [18] przewidział względną skuteczność polityk Gemini Robotics, co sprawdzono w ponad 1600 rzeczywistych próbach. W pracy World-in-World [6] przetestowano modele świata w zamkniętej pętli w zadaniach nawigacji i manipulacji. Okazało się, że jakość wizualna nie gwarantuje sukcesu w zadaniu, a większe znaczenie ma to, jak wiernie model podąża za akcjami. Autorzy VLAW [5] stwierdzili, że obecnym modelom świata brakuje dokładności fizycznej potrzebnej do ulepszania polityk, ponieważ trenuje się je na demonstracjach bez porażek i pomijają one drobne szczegóły kontaktu. W przypadku symulatorów fizyki badanie SIMPLER [19] pokazało, że sceny wizualnie dopasowane do rzeczywistych obrazów pozwalają uszeregować polityki niemal w tej samej kolejności co rzeczywiste uruchomienia. Badania te mierzą błędy modelu świata na jego wyjściu lub przez końcową korelację z rzeczywistym sukcesem. Nie pokazują, który typ błędu zmienia politykę ani w jaki sposób.

Luka między modelem świata a rzeczywistością jest przypadkiem przesunięcia rozkładu. Teoria adaptacji domenowej ogranicza błąd w domenie docelowej przez błąd w domenie źródłowej, rozbieżność między oboma rozkładami i łączny błąd najlepszego pojedynczego modelu w obu domenach [20]. Traktuję to ograniczenie wyłącznie jako motywację. Uczynienie cech niezmienniczymi względem domeny nie jest ukierunkowane na łączny błąd, a nawet może go zwiększyć [21]. Randomizacja domeny zmienia parametry symulatora, takie jak tekstury, tak aby rzeczywistość wyglądała jak kolejny wariant [22]. Zmienia ona globalne ustawienia ręcznie zbudowanego symulatora, podczas gdy błędy modelu świata zależą od akcji, kontaktu i długości przebiegu. Wspólny trening na danych symulowanych i małym zbiorze rzeczywistym poprawił manipulację w rzeczywistym świecie [23]. Mechanistyczna analiza takiego wspólnego treningu wykazała, że wyrównuje on obie domeny, ale pozostawia je rozróżnialnymi [24], więc pełne wyrównanie wszędzie nie jest celem.

Nie wiadomo też, gdzie wewnątrz polityki powstaje luka. Sondowanie, czyli odczytywanie informacji ze stanów ukrytych za pomocą prostych klasyfikatorów, pokazało, że dotrenowanie do przewidywania akcji pogarsza reprezentacje wizualne modeli VLA [10]. Badania nad chirurgicznym dotrenowaniem (surgical fine-tuning) pokazały, że najlepsze warstwy do adaptacji zależą od typu przesunięcia [25]. Nie znalazłem pracy, która w politykach trenowanych w modelach świata lokalizowałaby etap, na którym informacja o zadaniu dostępna dla wyobrażonych danych wejściowych zostaje utracona dla rzeczywistych.

Gdy zbiera się niewielką ilość rzeczywistych danych, wykorzystuje się je na różne sposoby. VLAW [5] dotrenowuje model świata na rzeczywistych przebiegach, a następnie ulepsza politykę danymi syntetycznymi z tego modelu, nie wybierając, które przebiegi zebrać. TwinRL [26] używa cyfrowego bliźniaka do wyszukiwania konfiguracji podatnych na porażki, w których zbiera rzeczywiste przebiegi poprawiające politykę. Otwarte pozostaje pytanie, jak przy stałym budżecie wybierać rzeczywiste przebiegi, aby były jak najbardziej przydatne zarówno dla modelu świata, jak i dla polityki.

Wreszcie lukę w generalizacji wizualnych polityk manipulacji można rozłożyć na czynniki, takie jak oświetlenie czy położenie kamery, a uporządkowanie tych czynników według trudności było w dużej mierze takie samo w symulacji i na rzeczywistym robocie [27]. Nie wiadomo, czy luka zmierzona w przestrzeni reprezentacji przed zastosowaniem metody pozwala przewidzieć, czy jej korzyść przeniesie się na nową scenę lub zadanie, ani czy robi to lepiej niż proste wskaźniki, takie jak jakość wideo modelu świata. Moje pytania badawcze w sekcji 7 dotyczą tych otwartych kwestii. RQ1 pyta, które błędy szkodzą polityce, RQ2, gdzie wewnątrz polityki pojawia się szkoda, RQ3, które rzeczywiste przebiegi zebrać, a RQ4, czy korzyści i miary w przestrzeni reprezentacji się przenoszą.

Cytowane prace wymieniam w sekcji 12.

## 7. Pytania i hipotezy badawcze

Celem mojej rozprawy jest opracowanie metod uczenia reprezentacji, które poprawiają generalizację do rzeczywistości polityk sterowania robotami trenowanych w symulacjach tworzonych przez wyuczone modele świata. Polityki powinny działać niezawodnie na rzeczywistych danych wejściowych i w scenach niewidzianych podczas treningu, a metody powinny działać z niezmienionymi ustawieniami zarówno w nawigacji, jak i w manipulacji.

Na początku nie będę miał własnego robota i będę pracował na akademickich klastrach GPU, dlatego wykorzystam istniejące, wstępnie wytrenowane modele świata i polityki i będę je dotrenowywał zamiast trenować duże modele od zera. Jako odniesienie do rzeczywistości wykorzystam nagrane dane z rzeczywistych robotów i opublikowane wyniki uzyskane na rzeczywistych robotach, a jeśli pozwoli na to dostęp, także rzeczywistego robota. To odniesienie jest przybliżeniem i będę podawał, którą część luki mierzy. Zbadam nawigację robotów i manipulację robotyczną, a wszystkie wyniki będę mierzył na odłożonych scenach, których nie użyto do treningu ani wyboru modelu.

Moje pytania badawcze (RQ) i hipotezy (H) są następujące.

1. RQ1. Które błędy symulacji tworzonej przez model świata, takie jak słabe podążanie za akcjami, błędna fizyka kontaktu, błędy wyglądu i dryf w długim horyzoncie, zmienne w zależności od sytuacji, szkodzą generalizacji trenowanych w niej polityk?
2. H1. Szkodliwość błędu to spadek skuteczności na odłożonych danych rzeczywistych polityki wytrenowanej w modelu świata z tym błędem w porównaniu z tą samą polityką wytrenowaną bez niego. Tę szkodliwość lepiej przewiduje to, jak bardzo błąd zmienia reprezentację stałego, wstępnie wytrenowanego enkodera lub modelu świata typu JEPA, niż jakość wideo mierzona na poziomie pikseli. Ponadto ukierunkowana augmentacja szkodliwych typów błędów lepiej generalizuje niż jednolita augmentacja o tej samej sile.
3. RQ2. Na którym etapie polityki trenowanej w modelu świata rzeczywiste dane wejściowe po raz pierwszy tracą informację o zadaniu, która jest dostępna dla wyobrażonych danych wejściowych? Będę go szukał za pomocą sond liniowych z zadaniami kontrolnymi, a za pomocą interwencji przyczynowych sprawdzę, czy polityka korzysta z tej informacji.
4. H2. Wyrównywanie reprezentacji wyobrażonych i rzeczywistych na tym etapie zmniejsza lukę bardziej niż to samo wyrównywanie na wejściu, na końcowych cechach lub na wszystkich etapach, przy tych samych danych rzeczywistych i tym samym nakładzie treningu.
5. RQ3. Które nieliczne rzeczywiste przebiegi, wybrane przy stałym budżecie z użyciem sygnałów z RQ1 i RQ2, najlepiej poprawiają zarówno model świata, jak i politykę? Porównam mój sposób wyboru z wyborem losowym, z wyborem kierowanym porażkami oraz z tą samą ilością niewybieranych danych rzeczywistych wykorzystanych tak jak w VLAW [5].
6. RQ4. Czy korzyści przenoszą się przy niezmienionych ustawieniach na niewidziane sceny oraz między nawigacją a manipulacją? Czy luka zmierzona w przestrzeni reprezentacji, rozłożona zgodnie z podejściem JEPA na lukę obserwacji w enkoderze i lukę dynamiki w predyktorze, pozwala przewidzieć to przeniesienie lepiej niż proste wskaźniki, takie jak korelacja rang między sukcesem w modelu świata a sukcesem rzeczywistym lub jakość wideo?
7. Plan awaryjny. Jeśli jakość na poziomie pikseli będzie lepiej przewidywać szkodliwość niż zmiana reprezentacji, do kierowania augmentacją i wyborem danych użyję zamiast zmiany reprezentacji niepewności modelu świata i wrażliwości akcji polityki. Ten plan awaryjny jest słabszy, ponieważ model świata może się mylić z dużą pewnością, na przykład co do kontaktu po akcjach dalekich od jego danych treningowych.

## 8. Wkład spodziewanych wyników dla rozwoju dyscypliny naukowej

Głównym spodziewanym wkładem mojej rozprawy jest zestaw metod uczenia reprezentacji, które pomagają politykom sterowania robotami trenowanym w symulacjach tworzonych przez modele świata generalizować się do rzeczywistości i na niewidziane sceny. Razem z metodami chcę wyjaśnić, w jaki sposób błędy modelu świata docierają do polityki. Chcę ustalić, które typy błędów mają znaczenie, na którym etapie polityki zamieniają się w utraconą informację o zadaniu i ile dobrze wybranych danych rzeczywistych potrzeba, aby je skorygować.

Jest to aktualne, ponieważ modele świata stają się powszechnym sposobem tworzenia danych treningowych i oceny polityk, a modele świata i działania (WAM) łączą dziś model świata i politykę w jednej sieci. Moje wyniki powinny pokazać, które własności modelu świata muszą być dokładne dla danego zadania. Jest to przydatne zarówno dla tych, którzy budują modele świata, jak i dla tych, którzy trenują w nich polityki. Ponieważ pytania dotyczą uczenia przy przesunięciu rozkładu, wyniki dotyczące tego, gdzie wyrównywać reprezentacje i jakie dane wybierać, mogą być przydatne także w adaptacji domenowej i uczeniu aktywnym. Planuję udostępnić kod, protokół ewaluacji oraz, tam gdzie pozwalają na to licencje, wytrenowane modele, aby inni mogli porównywać metody w ten sam sposób.

## 9. Planowane metody badawcze

Większość mojej pracy będzie polegać na trenowaniu i dotrenowywaniu polityk wewnątrz wyuczonych modeli świata, mierzeniu ich działania na danych rzeczywistych oraz projektowaniu metod, które analizują i wyrównują uczone przez nie reprezentacje. Nie istnieje ugruntowana teoria generalizacji polityk trenowanych w modelach świata, dlatego praca będzie głównie empiryczna. Teoria adaptacji domenowej [20] będzie dla mnie motywacją, a tam, gdzie to możliwe, sprawdzę, czy wyrównanie zmniejsza rozbieżność między cechami wyobrażonymi a rzeczywistymi bez zwiększania łącznego błędu.

Do treningu użyję biblioteki PyTorch, do kontroli wersji systemu Git z repozytoriami w serwisie GitHub, a do pobierania i publikowania modeli i danych serwisu Hugging Face. W nawigacji zacznę od NWM [3]. W manipulacji jako modeli świata działających w przestrzeni reprezentacji użyję DINO-WM [15], V-JEPA 2-AC [9] lub małego modelu LeWorldModel, a jako modeli świata generujących wideo Ctrl-World [17] lub Cosmos-Predict [4]. Tam, gdzie to możliwe, skorzystam z otwartych wag i będę przestrzegał ich licencji, z których niektóre dopuszczają wyłącznie użytek niekomercyjny. Jako symulatora fizyki do porównań użyję NVIDIA Isaac Lab 3.0 w trybie bez środowiska Kit (kit-less) z silnikiem fizyki Newton, który działa na GPU H100. Cosmos Transfer wykorzystam do nadania renderom z symulatora fotorealistycznego wyglądu. Isaac Sim nie obsługuje GPU A100 ani H100, więc użyję go tylko na stacji roboczej z kartą RTX, jeśli będzie dostępna.

Ponieważ na początku nie będę miał własnego robota, ewaluację przeprowadzę głównie na danych publicznych. W manipulacji użyję zbioru DROID, na którym trenowano Ctrl-World i V-JEPA 2-AC, oraz zbioru BridgeData V2, którego konfiguracja z robotem WidowX jest jedną z konfiguracji odwzorowanych w SIMPLER [19]. W nawigacji użyję zbiorów RECON i SCAND, dwóch zbiorów danych z rzeczywistych robotów, na których trenowano NWM. Odłożone trajektorie i sceny z tych zbiorów dają rzeczywiste obserwacje sparowane z wyobrażonymi, które zaczynają się od tego samego stanu i przebiegają według tych samych akcji. Takich par potrzebuję do sondowania i wyrównywania. Sprawdzę też, czy kolejność polityk w modelu świata zgadza się z opublikowanymi wynikami uzyskanymi na rzeczywistych robotach, pochodzącymi z SIMPLER i z rzeczywistych ewaluacji opisanych dla modeli świata. Ewaluacja wewnątrz modelu świata lub na nagranych danych jest jedynie przybliżeniem rzeczywistości. Pomija ona część luki, na przykład napędy i kamerę samego robota, i będę to zaznaczał przy każdym wyniku. Jeśli pozwoli na to dostęp, wybrane wyniki sprawdzę na rzeczywistym robocie w laboratorium uczelnianym.

W RQ1 będę wprowadzał do modelu świata po jednym typie błędu naraz albo usuwał go, zastępując wyobrażone klatki rzeczywistymi lub wygenerowanymi przez symulator fizyki. Typy błędów to ignorowane lub opóźnione akcje, błędne skutki kontaktu, zmiany wyglądu i dryf w długich przebiegach. W każdej wersji wytrenuję lub dotrenuję politykę i zmierzę zmianę jej skuteczności. Zmianę reprezentacji stałego, wstępnie wytrenowanego enkodera, takiego jak DINOv2 lub V-JEPA 2, porównam z pikselowymi miarami jakości wideo, takimi jak PSNR, LPIPS i FVD, na podstawie ich korelacji rang ze szkodliwością. Porównam też ukierunkowaną augmentację z jednolitą augmentacją o tej samej sile (H1). W RQ2 wytrenuję sondy liniowe, czyli modele liniowe odczytujące informacje o zadaniu, takie jak kierunek do celu lub położenie przedmiotu, ze stanów ukrytych każdego etapu polityki dla wyobrażonych danych wejściowych, i przetestuję je na sparowanych rzeczywistych danych wejściowych. Zadania kontrolne z losowymi etykietami pokażą, że sondy nie zapamiętują po prostu danych. Aby sprawdzić, czy polityka korzysta z utraconej informacji, przeprowadzę interwencje przyczynowe. Zastąpię składową rzeczywistego stanu ukrytego wzdłuż kierunków sond składową pochodzącą ze sparowanego wyobrażonego wejścia i sprawdzę, czy akcja się poprawi. Porównam to z zastąpieniem tej samej liczby losowych kierunków. Następnie na wskazanym etapie dodam funkcję straty wyrównującej, taką jak maksymalna rozbieżność średnich (MMD) lub strata kontrastowa między sparowanymi cechami. Porównam ją z tą samą stratą zastosowaną na wejściu, na końcowych cechach, na wszystkich etapach oraz w warstwach wybranych tak jak w chirurgicznym dotrenowaniu [25] (H2). W RQ3 porównam reguły wyboru rzeczywistych przebiegów z wyborem losowym, wyborem kierowanym porażkami jak w TwinRL [26] i niewybieranymi danymi jak w VLAW [5], przy równych budżetach. Porównam też korygowanie zarówno modelu świata, jak i polityki z korygowaniem tylko jednego z nich. W RQ4 zastosuję metody z niezmienionymi ustawieniami na odłożonych scenach i w drugim zadaniu. Lukę w przestrzeni reprezentacji zmierzę jako składnik obserwacji, czyli odległość między reprezentacjami dopasowanych stanów wyobrażonych i rzeczywistych, oraz składnik dynamiki, czyli błąd przewidywania modelu świata w przestrzeni reprezentacji na rzeczywistych przejściach. Sprawdzę, czy te składniki przewidują korzyści lepiej niż korelacja rang między sukcesem w modelu świata a sukcesem rzeczywistym lub jakość wideo. Użyję do tego korelacji rang Spearmana obliczanej między scenami oraz testów permutacyjnych.

Dla każdej polityki zmierzę odsetek sukcesów w modelu świata i w środowisku ewaluacyjnym danego zadania, lukę między skutecznością wyobrażoną a rzeczywistą oraz korelację rang między wynikami w modelu świata a wynikami rzeczywistymi. Moje metody porównam z randomizacją domeny [22], wspólnym treningiem na danych wyobrażonych i rzeczywistych [23] oraz metodami bazowymi wymienionymi wyżej, przy tej samej liczbie kroków treningu i tej samej ilości danych rzeczywistych dla każdej metody. Aby wyniki były wiarygodne, powtórzę treningi dla różnych ziaren losowych i scen, porównania poprę testami statystycznymi i przeprowadzę badania ablacyjne. Dane do treningu, wyboru modelu i końcowej ewaluacji będą rozdzielone.

Eksperymenty uruchomię na węzłach z GPU H100 Wrocławskiego Centrum Sieciowo-Superkomputerowego (WCSS), gdzie zadaniami zarządza SLURM, oraz na zasobach PLGrid. Zamierzam korzystać z asystentów programowania opartych na sztucznej inteligencji, takich jak Claude Code, aby szybciej pisać i testować kod. Pomogą mi też w rutynowych zadaniach, takich jak monitorowanie długich eksperymentów i korekta tekstu.

Wyniki planuję publikować na konferencjach i w czasopismach za 200 punktów z listy ministerialnej. W uczeniu maszynowym są to NeurIPS, ICML i ICLR, w widzeniu komputerowym CVPR, ICCV i ECCV, a w uczeniu robotów RSS i czasopismo IEEE RA-L. Tam, gdzie to możliwe, udostępnię artykuły także jako preprinty w serwisie arXiv.

## 10. Streszczenie popularnonaukowe

### Streszczenie popularnonaukowe

Roboty coraz częściej uczy się we „śnie”, czyli w kopii świata przewidywanej przez sieć neuronową zwaną modelem świata, ponieważ nauka w prawdziwym świecie jest powolna, kosztowna i czasem niebezpieczna. Sieć uczy się z nagrań wideo, co zwykle dzieje się po ruchu robota, ale jej sen nigdy nie jest idealny. Może zignorować ruch, pozwolić, by chwytak przeszedł przez przedmiot, albo oddalić się od rzeczywistości. Dlatego robot, który dobrze radzi sobie we śnie, w prawdziwym świecie często zawodzi, zwłaszcza w nowych miejscach. Chcę ustalić, które błędy snu szkodzą robotowi i gdzie wewnątrz jego sieci neuronowej zamieniają się w błędne działania. Chcę też sprawdzić, które nieliczne prawdziwe próby najlepiej poprawiają zarówno sen, jak i robota. Zbadam nawigację robotów oraz chwytanie i przestawianie przedmiotów. Efektem mają być metody, dzięki którym roboty będą szybciej, taniej i bezpieczniej uczyć się nowej pracy.

### Abstract for general public

Robots are increasingly trained in a "dream", a copy of the world predicted by a neural network called a world model, because real-world learning is slow, costly and sometimes unsafe. The network learns from videos what usually happens after a robot moves, but its dream is never perfect. It may ignore a movement, let the gripper pass through an object or drift away from reality. A robot that does well in the dream often fails in reality, especially in new places. I want to find out which mistakes of the dream harm the robot and where inside its neural network they turn into wrong actions. I also want to check which few real trials best correct both the dream and the robot. I will study robot navigation and the grasping and moving of objects. The result should be methods that let robots learn new work faster, more cheaply and more safely.

## 11. Termin oddania do druku artykułu naukowego lub monografii

Wrzesień 2027 (planowane zgłoszenie na konferencję lub do czasopisma za 200 punktów z listy ministerialnej, takie jak konferencja ICLR 2028 lub czasopismo IEEE Robotics and Automation Letters).

## 12. Inne

Korzystałem z Claude (przez Claude Code) przy wyszukiwaniu literatury, pisaniu wstępnych wersji tekstu i redakcji, a całą treść i wszystkie pozycje bibliografii przejrzałem samodzielnie.

### Bibliografia

[1] Ha, D., & Schmidhuber, J. (2018). World models. arXiv:1803.10122.

[2] Yang, S., et al. (2024). Learning interactive real-world simulators. ICLR.

[3] Bar, A., et al. (2025). Navigation world models. CVPR.

[4] Agarwal, N., et al. (2025). Cosmos world foundation model platform for physical AI. arXiv:2501.03575.

[5] Guo, Y., et al. (2026). VLAW: Iterative co-improvement of vision-language-action policy and world model. arXiv:2602.12063.

[6] Zhang, J., et al. (2026). World-in-World: World models in a closed-loop world. ICLR.

[7] Wang, Z., et al. (2026). Efficient sim-to-real transfer of world-action models from synthetic priors. arXiv:2606.31101.

[8] LeCun, Y. (2022). A path towards autonomous machine intelligence. OpenReview.

[9] Assran, M., et al. (2025). V-JEPA 2: Self-supervised video models enable understanding, prediction and planning. arXiv:2506.09985.

[10] Kachaev, N., et al. (2026). Don't blind your VLA: Aligning visual representations for OOD generalization. AAMAS.

[11] Hafner, D., et al. (2025). Mastering diverse control tasks through world models. Nature.

[12] Mittal, M., et al. (2025). Isaac Lab: A GPU-accelerated simulation framework for multi-modal robot learning. arXiv:2511.04831.

[13] Jang, J., et al. (2025). DreamGen: Unlocking generalization in robot learning through video world models. CoRL.

[14] Ye, S., et al. (2026). World action models are zero-shot policies. arXiv:2602.15922.

[15] Zhou, G., et al. (2025). DINO-WM: World models on pre-trained visual features enable zero-shot planning. ICML.

[16] Rao, P., et al. (2026). SkyJEPA: Learning long-horizon world models for zero-shot sim-to-real control of quadrotors. arXiv:2606.23444.

[17] Guo, Y., et al. (2026). Ctrl-World: A controllable generative world model for robot manipulation. ICLR.

[18] Gemini Robotics Team (2025). Evaluating Gemini Robotics policies in a Veo world simulator. arXiv:2512.10675.

[19] Li, X., et al. (2024). Evaluating real-world robot manipulation policies in simulation. CoRL.

[20] Ben-David, S., et al. (2010). A theory of learning from different domains. Machine Learning.

[21] Zhao, H., et al. (2019). On learning invariant representations for domain adaptation. ICML.

[22] Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. IROS.

[23] Maddukuri, A., et al. (2025). Sim-and-real co-training: A simple recipe for vision-based robotic manipulation. RSS.

[24] Lei, Y., et al. (2026). A mechanistic analysis of sim-and-real co-training in generative robot policies. arXiv:2604.13645.

[25] Lee, Y., et al. (2023). Surgical fine-tuning improves adaptation to distribution shifts. ICLR.

[26] Xu, Q., et al. (2026). TwinRL: Digital twin-driven reinforcement learning for real-world robotic manipulation. arXiv:2602.09023.

[27] Xie, A., et al. (2024). Decomposing the generalization gap in imitation learning for visual robotic manipulation. ICRA.

## 13. Określenie planowanej formy współpracy z promotorem

Z promotorem planujemy cotygodniowe spotkania. Będę na nich przedstawiał postępy i najnowsze wyniki, a razem będziemy ustalać kolejne kroki i omawiać wspólne publikacje. Będę też uczestniczył w cotygodniowych spotkaniach grupy doktorantów promotora, na których omawiane są bieżące wyniki, problemy i nowe prace w dziedzinie. Na bieżąco będziemy się kontaktować mailowo i przez komunikatory. Kod, wytrenowane modele i źródła LaTeX publikacji będą przechowywane we wspólnych repozytoriach Git.

## 14. Opinia promotora pomocniczego

Nie dotyczy (promotor pomocniczy nie został wyznaczony).

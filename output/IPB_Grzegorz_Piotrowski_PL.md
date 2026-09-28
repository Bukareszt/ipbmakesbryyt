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

Metody uczenia reprezentacji dla generalizacji modeli uczenia głębokiego między symulacją a rzeczywistością w fizycznej sztucznej inteligencji / Representation learning methods for simulation-to-reality generalization of deep learning models in physical AI

## 3. Harmonogram przygotowania rozprawy doktorskiej

| Semestr | Zwięzły opis zadania |
|---|---|
| 1 | Udział w zajęciach Szkoły Doktorskiej, zapoznanie się z literaturą i rozważenie możliwych kierunków badań |
| 2 | Udział w zajęciach Szkoły Doktorskiej, przegląd literatury, wybór tematu rozprawy doktorskiej wspólnie z promotorem i przygotowanie Indywidualnego Planu Badawczego |
| 3 | Przygotowanie środowiska badawczego z cyfrowymi bliźniakami, symulatorami i publicznymi zbiorami danych oraz wstępne eksperymenty z RQ1 dotyczące szkodliwych błędów rekonstrukcji |
| 4 | Dalsze eksperymenty z RQ1, przygotowanie pierwszej publikacji i zgłoszenie jej na konferencję lub do czasopisma za 200 punktów z zakresu uczenia maszynowego lub uczenia robotów, na przykład na ICLR, RSS lub do IEEE RA-L, a także pierwsze eksperymenty z RQ2 |
| 5 | Eksperymenty z RQ2 dotyczące lokalizacji luki wewnątrz modeli i wyrównywania reprezentacji oraz przygotowanie publikacji naukowej |
| 6 | Eksperymenty z RQ3 dotyczące doboru danych rzeczywistych i z RQ4 dotyczące transferu do niewidzianych scen i między zadaniami, przygotowanie publikacji oraz testy na rzeczywistym robocie, jeśli pozwoli na to dostęp |
| 7 | Końcowe eksperymenty, zgłoszenie artykułu na konferencję lub do czasopisma i pierwsza wersja rozprawy doktorskiej |
| 8 | Ukończenie, poprawienie i złożenie rozprawy doktorskiej |

## 4. Termin złożenia rozprawy doktorskiej

Wrzesień 2029

## 5. Uzasadnienie wyboru tematu rozprawy doktorskiej

Roboty, które uczą się metodą prób i błędów, potrzebują bardzo dużej liczby prób, większej, niż da się praktycznie i bezpiecznie zebrać na prawdziwym robocie [1]. Dlatego takie modele trenuje się zwykle w symulacji [2]. Nowszym rodzajem symulacji jest cyfrowy bliźniak. Krótkie nagranie prawdziwego pokoju lub stołu zamienia się w fotorealistyczną kopię 3D metodami takimi jak 3D Gaussian Splatting. Model robota uczy się w tej kopii, a potem działa w prawdziwym miejscu.

Słabym punktem tego podejścia jest to, że kopia nigdy nie jest dokładna. W kopii może brakować szklanych drzwi, lustro może wyglądać jak otwarte pomieszczenie za nim, a tekstury i oświetlenie zawsze trochę się różnią. Model, który dobrze działa w kopii, może więc zawieść w rzeczywistości [3], a jeszcze gorzej radzi sobie w rzeczywistych miejscach, dla których nie zbudowano kopii [2]. Ten spadek skuteczności nazywa się luką między symulacją a rzeczywistością i jest jednym z głównych powodów, dla których wyuczone modele robotów wciąż trudno wdrożyć.

Typowe sposoby radzenia sobie z tym problemem nie korzystają z wiedzy o tym, gdzie kopia jest błędna. Randomizacja domeny wprowadza losowe zmiany kolorów, tekstur albo fizyki [4]. Nowsze warianty uczą się, jak szerokie powinny być te zmiany [5],[6], ale dostrajają parametry fizyczne i nie pytają, które błędy wizualne kopii naprawdę mają znaczenie. Inne metody zmuszają model, by tak samo widział obrazy z symulacji i z rzeczywistości, ale przy okazji mogą usunąć informacje potrzebne robotowi. Gdy zbiera się kilka prawdziwych przykładów, zwykle poprawia się nimi albo kopię [5],[7], albo model [8],[9]. Wcześniejsze badania mierzyły, jak czynniki takie jak oświetlenie, tekstura czy realizm fizyki wpływają na transfer [10],[11], ale wciąż nie wiadomo, które lokalne błędy rekonstrukcji cyfrowego bliźniaka szkodzą modelowi i na którym etapie wewnątrz modelu pojawia się ta szkoda.

Chcę odpowiedzieć na to pytanie, zaglądając do wnętrza modeli. Sieć neuronowa nie korzysta z obrazu bezpośrednio. Zamienia go na wewnętrzne cechy, nazywane reprezentacjami, i na ich podstawie podejmuje decyzję. Zakładam roboczo, że błąd w kopii, który nie zmienia tych cech, niewiele szkodzi, a błąd, który zmienia cechy, od których zależy decyzja, prawdopodobnie powoduje niepowodzenia [12],[13]. Daje to mierzalny sposób badania luki. Najpierw sprawdzę, które błędy rekonstrukcji zmieniają reprezentacje w szkodliwy sposób. Potem znajdę etap wewnątrz modelu, na którym prawdziwe obrazy tracą informację potrzebną do zadania, i poprawię reprezentacje właśnie tam. Zbadam też, jak wybrać kilka prawdziwych przykładów, które najlepiej poprawiają jednocześnie kopię i model, oraz czy poprawa utrzymuje się w nowych miejscach i w drugim zadaniu. Będę pracował nad dwoma równorzędnymi zadaniami, nawigacją robotów i manipulacją robotyczną, i zawsze będę testował na scenach nieużywanych do treningu.

Odpowiedź pomogłaby zdecydować, które części cyfrowego bliźniaka muszą być dokładne i gdzie warto zbierać dodatkowe prawdziwe dane. W praktyce robota można by wytrenować w cyfrowej kopii nowego magazynu, szpitala lub domu, a po niewielkiej adaptacji w rzeczywistym świecie niezawodnie tam wykorzystywać. Te same pytania pojawiają się przy autonomicznej jeździe, gdzie do trenowania i testowania modeli powszechnie używa się symulatorów i rekonstrukcji nagranych przejazdów.

## 6. Zarys aktualnego stanu badań w tematyce rozprawy doktorskiej

Modele uczenia głębokiego do nawigacji robotów i manipulacji robotycznej potrzebują więcej doświadczenia, niż mogą łatwo dostarczyć rzeczywiste roboty, dlatego często trenuje się je w całości lub częściowo w symulacji [9]. Badanie dotyczące nawigacji wykazało, że bez starannego dostrojenia symulatora skuteczność w symulacji może słabo przewidywać skuteczność w rzeczywistości [14]. Luka między symulacją a rzeczywistością jest szczególnym przypadkiem przesunięcia rozkładu. Teoria adaptacji domenowej ogranicza błąd modelu w domenie docelowej przez jego błąd w domenie źródłowej, rozbieżność między rozkładami obu domen oraz łączny błąd najlepszego pojedynczego modelu w obu domenach [12]. Ograniczenie to traktuję tylko jako motywację. Sugeruje ono, by rozkład treningowy obejmował rzeczywistość i by model był niewrażliwy na pozostałą rozbieżność. Cechy niezmiennicze nie są jednak ukierunkowane na błąd łączny, a mogą go nawet zwiększyć [15]. Korygowanie symulacji w stronę rzeczywistości zmienia same dane treningowe i dlatego może zmniejszyć ten błąd, ponieważ usuwa widoki, dla których poprawna akcja w cyfrowym bliźniaku jest inna niż w rzeczywistości.

Szeroko stosuje się randomizację domeny. Zmienia ona parametry symulatora, na przykład tekstury, tak aby rzeczywistość była dla modelu jeszcze jednym wariantem [4]. Zbyt szeroka randomizacja prowadzi do zachowawczego działania, dlatego późniejsze prace kształtują jej rozkład, dopasowując go do kilku rzeczywistych przebiegów [5] lub maksymalizując jego entropię przy zachowaniu skuteczności w zadaniu [6]. Metody te losują lub dostosowują globalne parametry ręcznie zbudowanego symulatora, takie jak tekstury, oświetlenie, tarcie czy masy [4],[5],[6]. Nie korzystają z wiedzy o tym, gdzie scena została odtworzona błędnie. Cyfrowe bliźniaki zbudowane z danych rzeczywistych mają błędy, które silnie różnią się między obszarami, na przykład tam, gdzie scenę obejmuje niewiele widoków kamery, a parametry globalne nie potrafią opisać takich błędów.

Inne podejście polega na tym, by model był niezmienniczy względem domeny, tak aby symulowane i rzeczywiste dane wejściowe dawały podobne cechy. Trening domenowo-adwersarialny sprawia, że klasyfikator domeny nie potrafi odróżnić cech obu domen [16]. W robotyce wyrównanie łącznych rozkładów obserwacji i akcji w danych symulowanych i rzeczywistych poprawiło działanie w rzeczywistości polityk trenowanych wspólnie na obu rodzajach danych, czyli modeli odwzorowujących obserwacje na akcje [8]. Niezmienniczość przy niskim błędzie w domenie źródłowej nie gwarantuje jednak transferu. Gdy rozkłady etykiet, czyli tutaj akcji, różnią się między domenami, może ona zwiększać składnik błędu łącznego [15], a pełna niezmienniczość może odrzucać informacje o zadaniu. Niedawna analiza wykazała, że skuteczny wspólny trening na danych symulowanych i rzeczywistych wyrównuje obie domeny, a zarazem zachowuje ich rozróżnialność [17]. To, czy domeny da się odróżnić, nie jest więc miarą szkodliwości, a użyteczna miara musi odnosić się do informacji potrzebnej w zadaniu. W pracach nad przenoszeniem modeli z symulacji do rzeczywistości niezmienniczość wymusza się zwykle w miejscu wybranym z góry, takim jak obrazy wejściowe, cechy końcowe [16] lub wspólna przestrzeń ukryta [8], bez wcześniejszego pomiaru, gdzie powstaje luka.

Nowszym kierunkiem są cyfrowe bliźniaki budowane na podstawie danych rzeczywistych. 3D Gaussian Splatting [18] rekonstruuje fotorealistyczne sceny z wielowidokowych zdjęć i renderuje je w czasie rzeczywistym. W manipulacji cyfrowe bliźniaki posłużyły do zwiększenia odporności polityk wyuczonych z kilku rzeczywistych demonstracji za pomocą uczenia ze wzmocnieniem w szybkim skanie docelowej sceny [1], do przenoszenia polityk opartych na obrazach do rzeczywistości bez rzeczywistych demonstracji [19] oraz do ukierunkowania uczenia ze wzmocnieniem w rzeczywistym świecie na podstawie nagrania telefonem [20]. Badanie SIMPLER [21] oceniło te same polityki w symulacji i na dwóch rzeczywistych konfiguracjach robotów. W scenach wizualnie dopasowanych do rzeczywistych obrazów i przy dopasowanych sterownikach skuteczność w symulacji silnie korelowała z rzeczywistą i porządkowała polityki niemal w tej samej kolejności. PolaRiS [3] zamienia krótkie nagrania wideo rzeczywistych scen w interaktywne środowiska symulacyjne do oceny polityk, ale nadal wymaga wspólnego trenowania polityk na danych symulowanych, aby zniwelować różnice pozostałe po rekonstrukcji. Nawet starannie zbudowane cyfrowe bliźniaki zachowują więc błędy ważne dla polityk. W nawigacji polityki dostrajano w cyfrowych bliźniakach zbudowanych z nagrania pomieszczenia telefonem [2] i trenowano w bliźniakach zbudowanych z monokularnych nagrań miejskich [22]. Czynniki symulacji, takie jak randomizacja, fotorealizm i realizm fizyki, zmieniano dotąd głównie jako jedno ustawienie dla całej sceny, tak jak w niedawnym badaniu rzeczywistej manipulacji [10]. Dla całych przestrzeni roboczych podobieństwo cech wstępnie wytrenowanego modelu między widokami renderowanymi a rzeczywistymi było silniej związane ze zgodnością skuteczności polityk w symulacji i w rzeczywistości niż miary jakości obrazu, takie jak LPIPS czy PSNR [23]. Otwarte pozostaje pytanie, które lokalne błędy rekonstrukcji szkodzą generalizacji w nawigacji i manipulacji oraz jak silnie należy randomizować każdy obszar, biorąc pod uwagę jego błąd rekonstrukcji i znaczenie dla zadania.

Niejasne jest również, gdzie wewnątrz modelu powstaje luka. Sondowanie, czyli odczytywanie informacji ze stanów ukrytych za pomocą prostych klasyfikatorów, wykazało, że dostrajanie do generowania akcji pogarsza reprezentacje wizualne modeli wizja-język-akcja [13]. W innej pracy dostrajano tylko wybrane warstwy i stwierdzono, że to, które warstwy najlepiej adaptować, zależy od rodzaju przesunięcia [24]. Badanie wspólnego treningu porównało cechy symulowane i rzeczywiste w kolejnych warstwach, ale mierzyło, jak dobrze obie domeny są wyrównane, a nie to, czy informacja o zadaniu się zachowuje [17]. Nie znalazłem pracy, która w modelach trenowanych w cyfrowych bliźniakach lokalizuje etap, na którym informacja o zadaniu dostępna w symulacji przestaje być możliwa do odtworzenia z rzeczywistych danych wejściowych.

Pozostałą lukę zmniejsza się zwykle niewielką ilością danych rzeczywistych. W manipulacji wspólny trening na danych symulowanych i małym zbiorze danych rzeczywistych poprawił skuteczność w rzeczywistości średnio o 38% w porównaniu z polityką trenowaną tylko na tym zbiorze rzeczywistym [9]. Aktywna identyfikacja systemu trenuje w symulacji politykę eksploracji, która maksymalizuje informację Fishera zawartą w jej rzeczywistej trajektorii o parametrach fizycznych [7]. Funkcje wpływu pozwalają uszeregować rzeczywiste demonstracje według ich wpływu na skuteczność polityki w pętli zamkniętej i wybrać nowo zebrane trajektorie, które najbardziej jej pomagają [25]. Najbliższa moim badaniom praca używa cyfrowego bliźniaka do znajdowania konfiguracji podatnych na niepowodzenia i w nich wykonuje rzeczywiste przebiegi [20]. W tych pracach dane rzeczywiste poprawiają albo model [9],[25],[20], albo symulację [7], a wszystkie poza [9] wybierają, które dane rzeczywiste zebrać. Według mojej wiedzy nikt dotąd nie użył tych samych wybranych danych rzeczywistych do poprawienia zarówno rekonstrukcji wizualnego cyfrowego bliźniaka, jak i trenowanego w nim modelu.

Wreszcie lukę w generalizacji wizualnych polityk manipulacji uczonych przez naśladowanie można rozłożyć na czynniki zmienności, takie jak oświetlenie czy położenie kamery, a uporządkowanie tych czynników według trudności było w dużej mierze takie samo w symulacji i na rzeczywistym robocie [11]. Aktywna ewaluacja dopasowuje model probabilistyczny do czynników zadania, takich jak położenie obiektu i punkt widzenia kamery, aby wybierać informatywne próby rzeczywiste [26]. Przewiduje ona jednak skuteczność na podstawie rzeczywistych wyników tej samej polityki w tym samym zadaniu, a nie na podstawie pomiarów wykonanych przed zastosowaniem metody. Niewiele badań sprawdza, czy właściwości przesunięcia zmierzone przed zastosowaniem metody, takie jak zmiana wewnętrznych cech między widokami z cyfrowego bliźniaka i rzeczywistymi, przewidują, czy korzyść z tej metody przeniesie się na nową scenę lub inne zadanie. Niejasne jest też, czy takie pomiary radzą sobie lepiej niż proste wskaźniki, takie jak wielkość luki. Tymi otwartymi kwestiami zajmują się moje pytania badawcze w sekcji 7.

Cytowane prace wymieniam w sekcji 12.

## 7. Pytania i hipotezy badawcze

Celem mojej rozprawy jest opracowanie metod uczenia reprezentacji, które poprawią generalizację modeli uczenia głębokiego trenowanych w cyfrowych bliźniakach zbudowanych z danych rzeczywistych. Modele mają niezawodnie działać w rzeczywistości i w miejscach niewidzianych podczas treningu, a metody mają działać przy niezmienionych ustawieniach zarówno w nawigacji, jak i w manipulacji.

Na początku nie będę miał własnego robota, a modele będę trenował na akademickich klastrach GPU, dlatego zamiast trenować od zera duże polityki będę dostrajał istniejące modele wstępnie wytrenowane. Skorzystam z publicznych zbiorów danych, które zawierają niezależne nagrania tych samych rzeczywistych scen. Zbadam dwa zadania, nawigację robotów i manipulację robotyczną, a wszystkie wyniki zmierzę na odłożonych scenach, nieużywanych do treningu ani do wyboru modelu.

Stawiam następujące pytania badawcze, oznaczone RQ, i hipotezy, oznaczone H:

1. RQ1. Które błędy rekonstrukcji cyfrowego bliźniaka, zmieniające się w obrębie sceny, szkodzą generalizacji trenowanych w nim modeli nawigacji i manipulacji?
2. H1. Szkodliwość błędu w danym obszarze to spadek skuteczności na odłożonych scenach modelu trenowanego w cyfrowym bliźniaku, który zawiera ten błąd, w porównaniu z tym samym modelem trenowanym w cyfrowym bliźniaku, w którym ten błąd poprawiono. Szkodliwość tę lepiej przewiduje to, jak bardzo błąd zmienia cechy ustalonego, wstępnie wytrenowanego kodera wizualnego na widokach renderowanych z tym błędem i bez niego, niż wielkość błędu w obrazie lub geometrii, mierzona przez PSNR, LPIPS czy błąd głębi. Ponadto randomizacja każdego obszaru zgodnie z jego szacowanym błędem rekonstrukcji i znaczeniem dla zadania daje lepszą generalizację niż jednorodna randomizacja o tej samej średniej sile w całej scenie.
3. RQ2. Na którym etapie modelu trenowanego lub dostrajanego w cyfrowym bliźniaku rzeczywiste dane wejściowe po raz pierwszy tracą informację o zadaniu, dostępną dla danych symulowanych? Oczekuję, że najwcześniejszy taki etap lub wąski zakres etapów da się wskazać sondami liniowymi weryfikowanymi zadaniami kontrolnymi. Interwencjami przyczynowymi sprawdzę, czy model korzysta z tej informacji.
4. H2. Wyrównywanie reprezentacji symulowanych i rzeczywistych na tym etapie zmniejsza lukę między symulacją a rzeczywistością bardziej niż takie samo wyrównywanie na wejściu, na cechach końcowych, na wszystkich etapach lub w warstwach wybranych według istniejących kryteriów, przy tych samych danych rzeczywistych i tym samym nakładzie treningu.
5. RQ3. Które rzeczywiste obserwacje, wybrane w ramach ustalonego budżetu za pomocą sygnałów opartych na reprezentacjach z RQ1 i RQ2, najbardziej zmniejszają lukę, gdy użyje się ich zarówno do poprawienia rekonstrukcji cyfrowego bliźniaka, jak i do dostrojenia modelu? Oczekuję, że poprawienie obu na tych samych wybranych danych zmniejszy lukę bardziej niż poprawienie tylko jednego z nich. Mój sposób doboru danych porównam z doborem losowym i doborem opartym na niepowodzeniach.
6. RQ4. Czy uzyskane korzyści przenoszą się przy niezmienionych ustawieniach na niewidziane sceny i z jednego zadania na drugie? Czy sygnały oparte na reprezentacjach z RQ1 i RQ2, zmierzone przed zastosowaniem metody, przewidują ten transfer lepiej niż luka przed adaptacją lub rozbieżność na poziomie obrazu między widokami z cyfrowego bliźniaka a rzeczywistymi, na przykład LPIPS?
7. Plan awaryjny. Jeśli wielkość błędu okaże się lepszym predyktorem szkodliwości niż zmiana cech, randomizacją i doborem danych pokieruję zamiast tego za pomocą niepewności rekonstrukcji i wrażliwości akcji. To rozwiązanie jest słabsze, ponieważ niepewność pokazuje głównie, gdzie widoki wejściowe słabo określają scenę, i może pozostać niska dla błędu, co do którego wszystkie widoki są zgodne.

## 8. Wkład spodziewanych wyników dla rozwoju dyscypliny naukowej

Głównym oczekiwanym wkładem rozprawy jest zestaw metod uczenia reprezentacji, dzięki którym modele uczenia głębokiego trenowane w cyfrowych bliźniakach lepiej generalizują na rzeczywistość i na niewidziane miejsca. Chcę też sprawdzić, czy większość luki między symulacją a rzeczywistością wynika z niewielkiej liczby błędów rekonstrukcji ważnych dla zadania, czy ich wpływ da się przypisać konkretnemu etapowi modelu i czy do zmniejszenia tej luki wystarczy niewielka ilość dobrze dobranych danych rzeczywistych.

Eksperymenty powinny pokazać, które błędy rekonstrukcji szkodzą generalizacji, na którym etapie modelu informacja o zadaniu ginie dla rzeczywistych danych wejściowych i kiedy opłaca się poprawiać cyfrowego bliźniaka i model na tych samych danych rzeczywistych. Powinny też pokazać, czy korzyści przenoszą się na nowe sceny oraz między nawigacją a manipulacją. Ponieważ pytania te dotyczą uczenia przy przesunięciu rozkładu, wyniki dotyczące tego, gdzie wyrównywać reprezentacje i jakie dane wybierać, mogą się przydać także w adaptacji domenowej i uczeniu aktywnym. Planuję udostępnić kod i protokół ewaluacji, a jeśli pozwolą licencje, także wytrenowane modele, aby inni mogli w ten sam sposób porównywać metody na odłożonych scenach. Mam nadzieję, że wyniki pokażą praktykom, jak dokładny musi być cyfrowy bliźniak dla danego zadania i które dane rzeczywiste warto zebrać, tak aby uczące się roboty można było mniejszym nakładem pracy wdrażać w nowych miejscach.

## 9. Planowane metody badawcze

W pracy będę budował cyfrowe bliźniaki rzeczywistych scen, trenował i dostrajał w nich modele uczenia głębokiego oraz projektował metody, które analizują i wyrównują reprezentacje wyuczone przez te modele. Nie ma ugruntowanej teorii opisującej generalizację głębokich modeli trenowanych w cyfrowych bliźniakach zrekonstruowanych z danych rzeczywistych, więc praca będzie głównie empiryczna. Teoria adaptacji domenowej posłuży mi jako motywacja, a tam, gdzie to możliwe, odniosę moje metody do składników ograniczenia z [12], na przykład sprawdzając, czy wyrównanie na danym etapie zmniejsza składnik rozbieżności, nie zwiększając składnika błędu łącznego.

Do trenowania modeli użyję PyTorcha, do 3D Gaussian Splatting [18] biblioteki gsplat, a do wyznaczania pozycji kamer programu COLMAP. Nawigację będę symulował w Habitat, a manipulację w ManiSkill3. Wersje kodu będę kontrolował w Gicie i repozytoriach GitHub, a modele i zbiory danych będę pobierał i publikował przez Hugging Face. Tam, gdzie to możliwe, zacznę od modeli wstępnie wytrenowanych. Udostępnię kod i skrypty ewaluacyjne, a jeśli pozwolą licencje, także wytrenowane modele i dane pochodne.

Na początku nie będę miał własnego robota, dlatego ewaluację oprę głównie na danych publicznych. W nawigacji wykorzystam publiczne zbiory rzeczywistych scen wewnątrz budynków, które zawierają niezależne nagrania tych samych scen, takie jak ScanNet++ i MuSHRoom. Cyfrowego bliźniaka zbuduję z jednego nagrania. Drugie nagranie dostarczy rzeczywistych klatek, sparowanych z renderingami z cyfrowego bliźniaka z tych samych pozycji kamery, do sondowania i wyrównywania. Razem ze skanami laserowymi da też dokładniejsze środowisko odniesienia, w którym uruchomię modele w pętli zamkniętej jako miarę zastępczą (proxy) rzeczywistości. Ta miara zastępcza mierzy głównie część luki wynikającą z błędów rekonstrukcji i pomija różnice w tym, jak prawdziwy robot porusza się i odbiera otoczenie, na przykład w jego napędach i własnej kamerze. W manipulacji zbuduję cyfrowe bliźniaki rzeczywistych scen stołowych z obrazów publicznych zbiorów danych robotycznych, stosując dopasowanie wizualne jak w SIMPLER [21]. Następnie sprawdzę, czy skuteczność tych samych polityk w tych bliźniakach zgadza się z ich opublikowaną skutecznością na rzeczywistych robotach, zarówno co do wartości, jak i kolejności polityk. Jeśli pozwoli na to dostęp, użyję rzeczywistego robota w laboratorium uczelni, aby sprawdzić, czy wybrane poprawy pojawiają się też w rzeczywistości i czy środowisko odniesienia porządkuje modele w tej samej kolejności co rzeczywiste przebiegi.

W RQ1 będę zmieniał jeden rodzaj błędu rekonstrukcji naraz w wybranych obszarach. Błąd ten będę albo korygował za pomocą dokładniejszego odniesienia, takiego jak skany laserowe ze ScanNet++, albo wprowadzał w kontrolowany sposób, a następnie zmierzę wynikającą z tego zmianę odsetka sukcesów wytrenowanego modelu. Zmianę cech ustalonego, wstępnie wytrenowanego kodera porównam z PSNR, LPIPS i błędem głębi na podstawie ich korelacji rang ze szkodliwością w różnych obszarach i scenach. Sprawdzę też randomizację zależną od obszaru na tle jednorodnej randomizacji o tej samej średniej sile w całej scenie (H1). Błąd obszaru oszacuję na podstawie zmiany jego cech, a znaczenie dla zadania na podstawie tego, jak bardzo zmieniają się akcje modelu po zaburzeniu tego obszaru. W RQ2 wytrenuję sondy liniowe, czyli modele liniowe odczytujące informację o zadaniu, na przykład kierunek do celu, na stanach ukrytych każdego etapu dla danych symulowanych, i przetestuję je na sparowanych danych rzeczywistych. Zadania kontrolne z losowymi etykietami pokażą, że sondy nie uczą się po prostu na pamięć. Aby sprawdzić, czy model korzysta z utraconej informacji, zastąpię składową rzeczywistego stanu ukrytego wzdłuż kierunków sond składową ze sparowanych danych symulowanych i sprawdzę, czy akcja się poprawi. Wynik porównam z zastąpieniem tej samej liczby losowych kierunków. Następnie dodam na zidentyfikowanym etapie funkcję straty wyrównującej, na przykład maksymalną rozbieżność średnich (MMD) lub stratę kontrastową między sparowanymi cechami symulowanymi i rzeczywistymi. Porównam ją z tą samą stratą na wejściu, na cechach końcowych, na wszystkich etapach i w warstwach wybranych jak w chirurgicznym dostrajaniu [24] (H2). W RQ3 porównam przy równych budżetach reguły doboru danych rzeczywistych z doborem losowym i doborem opartym na niepowodzeniach. Porównam też poprawianie cyfrowego bliźniaka razem z modelem z poprawianiem tylko jednego z nich. W RQ4 zastosuję metody przy niezmienionych ustawieniach na odłożonych scenach i w drugim zadaniu. Następnie sprawdzę, czy sygnały z RQ1 i RQ2, zmierzone przed adaptacją, przewidują uzyskane korzyści, korzystając z korelacji rang Spearmana między scenami i testów permutacyjnych.

Na odłożonych scenach będę mierzył odsetek sukcesów każdego modelu w cyfrowym bliźniaku i w środowisku ewaluacyjnym danego zadania. W nawigacji jest nim środowisko odniesienia, a w manipulacji opublikowane wyniki rzeczywistych robotów oraz, jeśli pozwoli na to dostęp, rzeczywisty robot. Luka między symulacją a rzeczywistością to różnica między odsetkami sukcesów w cyfrowym bliźniaku i w tym środowisku. Podobnie jak w [14] i [21] zmierzę też, jak dobrze wyniki w cyfrowym bliźniaku przewidują kolejność modeli w środowisku ewaluacyjnym. Moje metody porównam z randomizacją domeny, treningiem domenowo-adwersarialnym, wspólnym treningiem na danych symulowanych i rzeczywistych oraz metodami bazowymi wymienionymi wyżej, przy tej samej liczbie kroków treningu i tej samej ilości danych rzeczywistych dla każdej metody. Aby wyniki były wiarygodne, powtórzę przebiegi dla różnych ziaren losowych i scen, porównania poprę testami statystycznymi i przeprowadzę badania ablacyjne. Dane do treningu, wyboru modelu i końcowej ewaluacji będą rozdzielone.

Eksperymenty uruchomię na superkomputerach WCSS, czyli Wrocławskiego Centrum Sieciowo-Superkomputerowego, gdzie zadaniami zarządza SLURM, oraz na zasobach PLGrid. Zamierzam korzystać z asystentów programowania opartych na sztucznej inteligencji, takich jak Claude Code, aby szybciej pisać i testować kod. Pomogą mi też w rutynowych zadaniach, takich jak monitorowanie długich eksperymentów i korekta tekstu. Przygotowałem ten plan z pomocą Claude, narzędzia sztucznej inteligencji, którego używałem przez Claude Code do wyszukiwania i weryfikacji literatury, pisania wstępnych wersji tekstu, korekty, redakcji i formatowania. Całą treść przejrzałem samodzielnie i każdą pozycję bibliograficzną sprawdziłem w rejestrach wydawców i serwisów z preprintami.

Wyniki planuję publikować na konferencjach i w czasopismach za 200 punktów z listy ministerialnej. W uczeniu maszynowym są to NeurIPS, ICML i ICLR, w widzeniu komputerowym CVPR, ICCV i ECCV, a w uczeniu robotów RSS i czasopismo IEEE RA-L. Tam, gdzie to możliwe, udostępnię artykuły także jako preprinty w serwisie arXiv.

## 10. Streszczenie popularnonaukowe

### Streszczenie popularnonaukowe

Roboty coraz częściej uczy się w cyfrowych bliźniakach, czyli wirtualnych kopiach rzeczywistych miejsc odtworzonych na podstawie ich nagrań, ponieważ nauka w prawdziwym świecie jest powolna, kosztowna i czasem niebezpieczna. Taka kopia nigdy nie jest idealna. Na przykład szklane drzwi mogą zostać odtworzone błędnie i zmylić robota. W efekcie model, który dobrze działa w symulacji, w rzeczywistości często zawodzi, zwłaszcza w miejscach, których wcześniej nie widział. Chcę ustalić, które różnice między kopią a rzeczywistością szkodzą modelowi i w którym miejscu wewnątrz modelu zamieniają się w błędy. Chcę też sprawdzić, które nieliczne rzeczywiste przykłady najlepiej poprawiają zarówno model, jak i kopię. Zbadam to w nawigacji robotów oraz w chwytaniu i przestawianiu przedmiotów. Efektem mają być metody, dzięki którym roboty będą mogły szybciej, taniej i bezpieczniej uczyć się pracy w nowych miejscach.

### Abstract for general public

Robots are increasingly trained in digital twins, that is, virtual copies of real places rebuilt from their recordings, because learning in the real world is slow, costly and sometimes unsafe. Such a copy is never perfect. For example, a glass door may be rebuilt incorrectly and mislead the robot. As a result, a model that works well in simulation often fails in reality, especially in places it has not seen before. I want to find out which differences between the copy and reality harm the model and where inside the model they turn into errors. I also want to check which few real examples best correct both the model and the copy. I will study this in robot navigation and in grasping and moving objects. The result should be methods that let robots learn to work in new places faster, more cheaply and more safely.

## 11. Termin oddania do druku artykułu naukowego lub monografii

Wrzesień 2027 (planowane zgłoszenie na konferencję lub do czasopisma za 200 punktów z listy ministerialnej, takie jak konferencja ICLR 2028 lub czasopismo IEEE Robotics and Automation Letters).

## 12. Inne

Korzystałem z Claude (przez Claude Code) przy wyszukiwaniu literatury, pisaniu wstępnych wersji tekstu i redakcji, a całą treść i wszystkie pozycje bibliografii sprawdziłem samodzielnie.

### Bibliografia

[1] Torne, M., et al. (2024). Reconciling reality through simulation: A real-to-sim-to-real approach for robust manipulation. RSS.

[2] Chhablani, G., et al. (2025). EmbodiedSplat: Personalized real-to-sim-to-real navigation with Gaussian splats from a mobile device. ICCV.

[3] Jain, A., et al. (2025). PolaRiS: Scalable real-to-sim evaluations for generalist robot policies. arXiv:2512.16881.

[4] Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. IROS.

[5] Chebotar, Y., et al. (2019). Closing the sim-to-real loop: Adapting simulation randomization with real world experience. ICRA.

[6] Tiboni, G., et al. (2024). Domain randomization via entropy maximization. ICLR.

[7] Memmel, M., et al. (2024). ASID: Active exploration for system identification in robotic manipulation. ICLR.

[8] Cheng, S., et al. (2025). Generalizable domain adaptation for sim-and-real policy co-training. NeurIPS.

[9] Maddukuri, A., et al. (2025). Sim-and-real co-training: A simple recipe for vision-based robotic manipulation. RSS.

[10] Jin, R., et al. (2026). Grounding sim-to-real generalization in robotic manipulation: An empirical study with vision-language-action models. ECCV.

[11] Xie, A., et al. (2024). Decomposing the generalization gap in imitation learning for visual robotic manipulation. ICRA.

[12] Ben-David, S., et al. (2010). A theory of learning from different domains. Machine Learning.

[13] Kachaev, N., et al. (2026). Don't blind your VLA: Aligning visual representations for OOD generalization. AAMAS.

[14] Kadian, A., et al. (2020). Sim2Real predictivity: Does evaluation in simulation predict real-world performance? RA-L.

[15] Zhao, H., et al. (2019). On learning invariant representations for domain adaptation. ICML.

[16] Ganin, Y., et al. (2016). Domain-adversarial training of neural networks. JMLR.

[17] Lei, Y., et al. (2026). A mechanistic analysis of sim-and-real co-training in generative robot policies. arXiv:2604.13645.

[18] Kerbl, B., et al. (2023). 3D Gaussian splatting for real-time radiance field rendering. ACM TOG.

[19] Qureshi, M. N., et al. (2025). SplatSim: Zero-shot Sim2Real transfer of RGB manipulation policies using Gaussian splatting. ICRA.

[20] Xu, Q., et al. (2026). TwinRL: Digital twin-driven reinforcement learning for real-world robotic manipulation. arXiv:2602.09023.

[21] Li, X., et al. (2024). Evaluating real-world robot manipulation policies in simulation. CoRL.

[22] Xie, Z., et al. (2025). Vid2Sim: Realistic and interactive simulation from video for urban navigation. CVPR.

[23] Wang, X., et al. (2026). ReVeal: A reconstruction-aware real-to-sim framework for VLA policy evaluation. arXiv:2609.23910.

[24] Lee, Y., et al. (2023). Surgical fine-tuning improves adaptation to distribution shifts. ICLR.

[25] Agia, C., et al. (2025). CUPID: Curating data your robot loves with influence functions. CoRL.

[26] Liao, A., et al. (2026). Active real-world factor-based evaluation for generalist robot policies. arXiv:2607.14439.

## 13. Określenie planowanej formy współpracy z promotorem

Z promotorem planujemy cotygodniowe spotkania. Będę na nich przedstawiał postępy i najnowsze wyniki, a razem będziemy ustalać kolejne kroki i omawiać wspólne publikacje. Będę też uczestniczył w cotygodniowych spotkaniach grupy doktorantów promotora, na których omawiane są bieżące wyniki, problemy i nowe prace w dziedzinie. Na bieżąco będziemy się kontaktować mailowo i przez komunikatory. Kod, wytrenowane modele i źródła LaTeX publikacji będą przechowywane we wspólnych repozytoriach Git.

## 14. Opinia promotora pomocniczego

Nie dotyczy (promotor pomocniczy nie został wyznaczony).

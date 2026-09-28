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
| 4 | Dalsze eksperymenty z RQ1, przygotowanie pierwszej publikacji i zgłoszenie jej na konferencję lub do czasopisma z zakresu robotyki, na przykład na ICRA lub do RA-L, a także pierwsze eksperymenty z RQ2 |
| 5 | Eksperymenty z RQ2 dotyczące lokalizacji luki wewnątrz modeli i wyrównywania reprezentacji oraz przygotowanie publikacji naukowej |
| 6 | Eksperymenty z RQ3 dotyczące doboru danych rzeczywistych i z RQ4 dotyczące transferu do niewidzianych scen i między zadaniami, przygotowanie publikacji oraz testy na rzeczywistym robocie, jeśli pozwoli na to dostęp |
| 7 | Końcowe eksperymenty, zgłoszenie artykułu na konferencję lub do czasopisma i pierwsza wersja rozprawy doktorskiej |
| 8 | Ukończenie, poprawienie i złożenie rozprawy doktorskiej |

## 4. Termin złożenia rozprawy doktorskiej

Wrzesień 2029

## 5. Uzasadnienie wyboru tematu rozprawy doktorskiej

Uczenie głębokie przyniosło ogromny postęp w widzeniu komputerowym i przetwarzaniu języka, w dużej mierze dzięki olbrzymim ilościom danych z internetu. Fizyczna sztuczna inteligencja, czyli sztuczna inteligencja w robotach i innych systemach, które postrzegają rzeczywisty świat i działają w nim, nie może opierać się na takich danych. Zbieranie danych z rzeczywistymi robotami jest powolne i kosztowne, a czasem niebezpieczne, dlatego modele robotów trenuje się zwykle w symulacji. W ostatnim czasie obiecującą alternatywą dla ręcznie tworzonych symulatorów stały się cyfrowe bliźniaki, czyli symulacje zbudowane na podstawie danych rzeczywistych. Metody neuronowej rekonstrukcji scen, takie jak 3D Gaussian Splatting, zamieniają krótkie nagranie rzeczywistego miejsca w fotorealistyczną kopię. Można w niej wytrenować model, a potem przenieść go z powrotem do rzeczywistości.

Cyfrowy bliźniak nigdy nie odtwarza świata dokładnie. Wygląd, geometria, oświetlenie i fizyka są w nim jedynie przybliżone, a błędy rekonstrukcji różnią się między obszarami sceny. Dlatego model, który dobrze działa w swoim cyfrowym bliźniaku, często zawodzi w rzeczywistości, a jeszcze częściej w miejscach, których nigdy nie widział. Ten spadek skuteczności nazywa się luką między symulacją a rzeczywistością. Jest to przypadek uczenia przy przesunięciu rozkładu i jedna z głównych przeszkód w rozwoju fizycznej sztucznej inteligencji.

Obecne metody radzą sobie z tą luką tylko częściowo. Randomizacja domeny zmienia kilka globalnych parametrów symulatora bez względu na to, gdzie cyfrowy bliźniak rzeczywiście jest błędny. Reprezentacje niezmiennicze mogą odrzucać informacje potrzebne do wykonania zadania. Nieliczne dane rzeczywiste zbierane do adaptacji poprawiają zwykle tylko model albo tylko symulację. Większość metod ocenia się też na jednym zadaniu i kilku scenach, więc nie wiadomo, które właściwości cyfrowego bliźniaka i wyuczonych reprezentacji decydują o działaniu modelu w rzeczywistości.

Celem moich badań jest zmniejszenie tej luki metodami, które analizują reprezentacje wyuczone przez modele i wyrównują je na etapie, na którym luka powstaje. Chcę ustalić, które błędy rekonstrukcji cyfrowego bliźniaka rzeczywiście szkodzą modelowi i na którym etapie wewnątrz modelu informacja o zadaniu ginie dla rzeczywistych danych wejściowych. Chcę też znaleźć niewielki zbiór danych rzeczywistych, który najlepiej poprawia zarówno cyfrowego bliźniaka, jak i model. Sprawdzę również, czy uzyskane poprawy przenoszą się na niewidziane sceny i z jednego zadania na drugie. Z równą wagą zbadam dwa zadania, nawigację robotów i manipulację robotyczną, a wszystkie wyniki zmierzę na scenach nieużywanych do treningu.

Wyniki mogą znaleźć zastosowanie w robotyce usługowej, logistycznej i asystującej. Robota można by tam wytrenować w cyfrowej kopii nowego magazynu, szpitala lub domu i po niewielkiej adaptacji w rzeczywistym świecie niezawodnie wykorzystywać na miejscu. Dotyczy to także autonomicznej jazdy i robotów inspekcyjnych, których modele również trenuje się na danych symulowanych lub zrekonstruowanych.

## 6. Zarys aktualnego stanu badań w tematyce rozprawy doktorskiej

Modele uczenia głębokiego do nawigacji robotów i manipulacji robotycznej potrzebują więcej doświadczenia, niż mogą dostarczyć rzeczywiste roboty, dlatego zwykle trenuje się je w symulacji. Badanie dotyczące nawigacji wykazało, że bez starannego dostrojenia symulatora skuteczność w symulacji może słabo przewidywać skuteczność w rzeczywistości [1]. Luka między symulacją a rzeczywistością jest szczególnym przypadkiem przesunięcia rozkładu. Teoria adaptacji domenowej ogranicza błąd modelu w domenie docelowej przez jego błąd w domenie źródłowej, rozbieżność między rozkładami obu domen oraz łączny błąd najlepszego pojedynczego modelu w obu domenach [2]. Ograniczenie to traktuję tylko jako motywację. Sugeruje ono, by rozkład treningowy obejmował rzeczywistość i by model był niewrażliwy na pozostałą rozbieżność. Niezmienniczość nie jest jednak ukierunkowana na błąd łączny, a może go nawet zwiększyć. Dlatego symulację warto też korygować w stronę rzeczywistości, co może bezpośrednio zmniejszyć ten błąd.

Szeroko stosuje się randomizację domeny. Zmienia ona parametry symulatora, na przykład tekstury, tak aby rzeczywistość była dla modelu jeszcze jednym wariantem [3]. Zbyt szeroka randomizacja prowadzi do zachowawczego działania, dlatego późniejsze prace kształtują jej rozkład, dopasowując go do kilku rzeczywistych przebiegów [4] lub maksymalizując jego entropię przy zachowaniu skuteczności w zadaniu [5]. Metody te dostrajają kilka globalnych parametrów syntetycznego symulatora i nie uwzględniają błędów zmieniających się w obrębie sceny, typowych dla cyfrowych bliźniaków zrekonstruowanych z danych rzeczywistych.

Inne podejście polega na tym, by model był niezmienniczy względem domeny. Trening domenowo-adwersarialny sprawia, że klasyfikator domeny nie potrafi odróżnić cech obu domen [6]. Polityka to model, który odwzorowuje obserwacje na akcje. W robotyce wyrównanie łącznych rozkładów obserwacji i akcji w danych symulowanych i rzeczywistych poprawiło działanie w rzeczywistości polityk trenowanych wspólnie na obu rodzajach danych [7]. Niezmienniczość przy niskim błędzie w domenie źródłowej nie gwarantuje jednak transferu. Gdy rozkłady etykiet, czyli tutaj akcji, różnią się między domenami, może ona zwiększać składnik błędu łącznego [8], a pełna niezmienniczość może odrzucać informacje o zadaniu. Niedawna analiza wykazała, że skuteczny wspólny trening na danych symulowanych i rzeczywistych wyrównuje obie domeny, a zarazem zachowuje ich rozróżnialność [9]. Sama separowalność domen nie pokazuje więc, gdzie luka szkodzi zadaniu. Niezmienniczość wymusza się też zwykle w miejscach wybranych z góry, takich jak wejście, cechy końcowe lub ustalone warstwy, bez pomiaru, gdzie luka faktycznie powstaje.

Nowszym kierunkiem są cyfrowe bliźniaki budowane na podstawie danych rzeczywistych. 3D Gaussian Splatting [10] rekonstruuje fotorealistyczne sceny z wielowidokowych zdjęć i renderuje je w czasie rzeczywistym. W manipulacji cyfrowe bliźniaki posłużyły do trenowania polityk na skanie docelowej sceny [11], do przenoszenia polityk opartych na obrazach do rzeczywistości bez rzeczywistych demonstracji [12] oraz do ukierunkowania uczenia ze wzmocnieniem w rzeczywistym świecie na podstawie nagrania telefonem [13]. Badanie SIMPLER [14] na podstawie sparowanych ocen w symulacji i w rzeczywistości wykazało, że sceny i sterowniki dopasowane do rzeczywistych obrazów dwóch konfiguracji robotów odzwierciedlają rzeczywistą skuteczność tych samych polityk. W nawigacji polityki dostrajano w cyfrowych bliźniakach zbudowanych z nagrania pomieszczenia telefonem [15] i trenowano w bliźniakach zbudowanych z monokularnych nagrań miejskich [16]. Wpływ czynników symulacji, takich jak randomizacja, fotorealizm i realizm fizyki, badano w rzeczywistej manipulacji głównie globalnie [17]. Dla całych przestrzeni roboczych podobieństwo cech wstępnie wytrenowanego modelu między widokami renderowanymi a rzeczywistymi przewidywało zgodność skuteczności w symulacji i w rzeczywistości lepiej niż LPIPS czy PSNR [18]. Otwarte pozostaje pytanie, które lokalne błędy rekonstrukcji szkodzą generalizacji w nawigacji i manipulacji. Nie wiadomo też, jak zmienność w treningu powinna uwzględniać błąd rekonstrukcji i znaczenie każdego obszaru dla zadania.

Niejasne jest również, gdzie wewnątrz modelu powstaje luka. Sondowanie, czyli odczytywanie informacji ze stanów ukrytych za pomocą prostych klasyfikatorów, wykazało, że dostrajanie do generowania akcji pogarsza reprezentacje wizualne modeli wizja-język-akcja [19]. W innej pracy dostrajanie tylko wybranych warstw pokazało, że to, które warstwy najlepiej adaptować, zależy od rodzaju przesunięcia [20]. Według mojej wiedzy w modelach trenowanych w cyfrowych bliźniakach nie zlokalizowano etapu, na którym informacja o zadaniu dostępna w symulacji przestaje być możliwa do odtworzenia z rzeczywistych danych wejściowych.

Pozostałą lukę zmniejsza się zwykle niewielką ilością danych rzeczywistych. Wspólny trening z małym zbiorem danych rzeczywistych daje duże korzyści [21]. Aktywna identyfikacja systemu projektuje w symulacji politykę eksploracji, której rzeczywista trajektoria niesie najwięcej informacji o parametrach fizycznych [22]. Najbliższa moim badaniom praca używa cyfrowego bliźniaka do znajdowania konfiguracji podatnych na niepowodzenia i w nich wykonuje rzeczywiste przebiegi [13]. Prace te wykorzystują wybrane dane rzeczywiste do poprawienia albo modelu, albo symulacji. Według mojej wiedzy nie badano dotąd korygowania obu na podstawie tych samych wybranych danych.

Wreszcie lukę można rozłożyć na czynniki zmienności, których uporządkowanie według trudności jest w dużej mierze zgodne między symulacją a rzeczywistością [23]. Rzadko sprawdza się natomiast, czy da się z góry przewidzieć, że korzyść z metody przeniesie się na nową scenę lub inne zadanie, i czy pomiary wykonane przed jej zastosowaniem robią to lepiej niż proste wskaźniki, takie jak wielkość luki. Tymi pytaniami zajmuje się moja rozprawa.

Cytowane prace wymieniam w sekcji 12.

## 7. Pytania i hipotezy badawcze

Celem mojej rozprawy jest opracowanie metod uczenia reprezentacji dla modeli uczenia głębokiego trenowanych w cyfrowych bliźniakach zbudowanych z danych rzeczywistych. Metody te mają poprawić generalizację modeli tak, aby niezawodnie działały w rzeczywistości i w miejscach niewidzianych podczas treningu. Nie powinny być związane z konkretnym robotem, sceną ani zadaniem.

Na początku nie będę miał własnego robota, a modele będę trenował na akademickich klastrach GPU, więc metody muszą działać w tej skali. Skorzystam z publicznych zbiorów danych, które zawierają niezależne nagrania tych samych rzeczywistych scen. Zbadam dwa zadania, nawigację robotów i manipulację robotyczną. Wszystkie wyniki muszą pochodzić z odłożonych scen, nieużywanych do treningu ani do wyboru modelu.

Stawiam następujące pytania badawcze, oznaczone RQ, i hipotezy, oznaczone H:

1. RQ1. Które błędy rekonstrukcji cyfrowego bliźniaka, zmieniające się w obrębie sceny, szkodzą generalizacji trenowanych w nim modeli nawigacji i manipulacji?
2. H1. Szkodliwość błędu w danym obszarze lepiej przewiduje zmiana cech ustalonego, wstępnie wytrenowanego kodera wizualnego między widokami renderowanymi z tym błędem i bez niego niż wielkość błędu w obrazie lub geometrii, mierzona przez PSNR, LPIPS czy błąd głębi. Po drugie, randomizacja każdego obszaru zgodnie z jego szacowanym błędem rekonstrukcji i znaczeniem dla zadania daje lepszą generalizację niż jednorodna randomizacja o tej samej łącznej sile.
3. RQ2. Na którym etapie modelu trenowanego lub dostrajanego w cyfrowym bliźniaku rzeczywiste dane wejściowe po raz pierwszy tracą informację o zadaniu, dostępną dla danych symulowanych? Oczekuję, że najwcześniejszy taki etap lub wąski zakres etapów da się wskazać sondami liniowymi weryfikowanymi zadaniami kontrolnymi. Interwencjami przyczynowymi sprawdzę, czy model korzysta z tej informacji.
4. H2. Wyrównywanie reprezentacji symulowanych i rzeczywistych na tym etapie zmniejsza lukę między symulacją a rzeczywistością bardziej niż takie samo wyrównywanie na wejściu, na cechach końcowych, na wszystkich etapach lub w warstwach wybranych według istniejących kryteriów. Obie wersje dostają tę samą ilość danych rzeczywistych i ten sam nakład treningu.
5. RQ3. Które dane rzeczywiste najlepiej poprawiają zarówno cyfrowego bliźniaka, jak i model, jeśli wybiera się je w ramach ustalonego budżetu na podstawie sygnałów opartych na reprezentacjach, wypracowanych w RQ1 i RQ2? Oczekuję, że poprawienie obu na tych samych wybranych danych zmniejszy lukę bardziej niż poprawienie tylko jednego z nich. Mój sposób doboru danych porównam z doborem losowym i doborem opartym na niepowodzeniach.
6. RQ4. Czy uzyskane korzyści przenoszą się przy niezmienionych ustawieniach na niewidziane sceny i z jednego zadania na drugie? Czy właściwości przesunięcia zmierzone wcześniej przewidują to lepiej niż proste wskaźniki, takie jak wielkość luki lub rozbieżność na poziomie obrazu?
7. Plan awaryjny. Jeśli okaże się, że szkodliwość błędu zależy od jego wielkości, a nie od zmiany cech, randomizacją i doborem danych mogą zamiast tego kierować niepewność rekonstrukcji i wrażliwość akcji. Niepewność pomija jednak błędy, które rekonstrukcja odtwarza w spójny sposób, dlatego sięgnę po to rozwiązanie tylko wtedy, gdy sygnały oparte na reprezentacjach okażą się mało informatywne.

## 8. Wkład spodziewanych wyników dla rozwoju dyscypliny naukowej

Głównym oczekiwanym wkładem rozprawy jest zestaw metod uczenia reprezentacji, dzięki którym modele uczenia głębokiego trenowane w cyfrowych bliźniakach lepiej generalizują na rzeczywistość i na niewidziane miejsca. Chcę też sprawdzić, czy luka między symulacją a rzeczywistością wynika głównie z ograniczonego zbioru różnic ważnych dla zadania. Takie różnice dałoby się znaleźć wśród błędów rekonstrukcji cyfrowego bliźniaka, zlokalizować wewnątrz modelu i zmniejszyć niewielką ilością dobrze dobranych danych rzeczywistych.

Eksperymenty powinny pokazać, które błędy rekonstrukcji szkodzą generalizacji i na którym etapie modelu informacja o zadaniu ginie dla rzeczywistych danych wejściowych. Powinny też wskazać, kiedy opłaca się poprawiać cyfrowego bliźniaka i model na tych samych danych rzeczywistych oraz czy takie korzyści przenoszą się na nowe sceny i między nawigacją a manipulacją. Pytania te dotyczą uczenia przy przesunięciu rozkładu, więc wyniki mogą mieć znaczenie także dla adaptacji domenowej, uczenia reprezentacji i uczenia aktywnego w ogólności. Planuję udostępnić kod i protokół ewaluacji, a jeśli pozwolą licencje, także wytrenowane modele, aby inni mogli w ten sam sposób porównywać metody na odłożonych scenach. Liczę też, że rozprawa zbliży badania nad przesunięciem rozkładu w uczeniu maszynowym do praktyki robotyki i ułatwi wdrażanie uczących się robotów w nowych magazynach, szpitalach i domach.

## 9. Planowane metody badawcze

W pracy będę budował cyfrowe bliźniaki rzeczywistych scen, trenował i dostrajał w nich modele uczenia głębokiego oraz projektował metody, które analizują i wyrównują reprezentacje wyuczone przez te modele. Nie ma ugruntowanej teorii gwarantującej generalizację z symulacji do rzeczywistości, więc większość pracy będzie empiryczna. Teoria adaptacji domenowej posłuży mi jako motywacja, a właściwości moich metod będę w miarę możliwości analizował teoretycznie.

Do trenowania modeli użyję PyTorcha, do 3D Gaussian Splatting [10] biblioteki gsplat, a do wyznaczania pozycji kamer programu COLMAP. Nawigację będę symulował w Habitat, a manipulację w ManiSkill3. Wersje kodu będę kontrolował w Gicie i repozytoriach GitHub, a modele i zbiory danych będę pobierał i publikował przez Hugging Face. Tam, gdzie to możliwe, zacznę od modeli wstępnie wytrenowanych. Udostępnię kod i skrypty ewaluacyjne, a jeśli pozwolą licencje, także wytrenowane modele i dane pochodne.

Na początku nie będę miał własnego robota, dlatego ewaluację oprę głównie na danych publicznych. W nawigacji wykorzystam publiczne zbiory rzeczywistych scen wewnątrz budynków, które zawierają niezależne nagrania tych samych scen, takie jak ScanNet++ i MuSHRoom. Cyfrowego bliźniaka zbuduję z jednego nagrania, a drugie dostarczy rzeczywistych klatek i odniesienia opartego na zbiorze danych. Odniesienie to jest miarą zastępczą (proxy) rzeczywistości. Mierzy lukę wynikającą z wierności rekonstrukcji, ale pomija różnice w napędach i czujnikach. W manipulacji zbuduję cyfrowe bliźniaki rzeczywistych scen stołowych z obrazów publicznych zbiorów danych robotycznych, stosując dopasowanie wizualne jak w SIMPLER [14], i porównam je z opublikowanymi wynikami tych samych polityk na rzeczywistych robotach. Jeśli uzyskam dostęp do laboratorium robotycznego uczelni, sprawdzę na rzeczywistym robocie kierunek wybranych wyników i trafność miary zastępczej.

W RQ1 będę korygował jeden rodzaj błędu rekonstrukcji naraz w wybranych obszarach, korzystając z dokładniejszego odniesienia, takiego jak skany laserowe ze ScanNet++, albo wprowadzał taki błąd w kontrolowany sposób. Potem zmierzę jego wpływ na wytrenowany model. Jako predyktory szkodliwości porównam zmianę cech ustalonego, wstępnie wytrenowanego kodera z PSNR, LPIPS i błędem głębi. Sprawdzę też randomizację zależną od obszaru na tle jednorodnej randomizacji o tej samej łącznej sile, co pozwoli zweryfikować H1. W RQ2 wytrenuję sondy liniowe z zadaniami kontrolnymi na symulowanych stanach ukrytych i przetestuję je na sparowanych stanach rzeczywistych. Interwencje przyczynowe na stanach ukrytych, takie jak podmiana sondowanej podprzestrzeni z symulowanych danych wejściowych do rzeczywistych, pokażą, czy model korzysta z utraconej informacji. Następnie dodam funkcję straty wyrównującej na zidentyfikowanym etapie i porównam ją z wyrównywaniem na wejściu, na cechach końcowych, na wszystkich etapach i w warstwach wybranych według istniejących kryteriów, co weryfikuje H2. W RQ3 porównam przy równych budżetach reguły doboru danych rzeczywistych z doborem losowym i doborem opartym na niepowodzeniach. Porównam też poprawianie cyfrowego bliźniaka razem z modelem z poprawianiem tylko jednego z nich. W RQ4 zastosuję metody przy niezmienionych ustawieniach na odłożonych scenach i za pomocą korelacji rang z odpowiednimi testami istotności sprawdzę, czy wcześniejsze pomiary przewidują uzyskane korzyści.

Na odłożonych scenach będę mierzył odsetek sukcesów oraz lukę między symulacją a rzeczywistością, czyli różnicę między skutecznością tego samego modelu w cyfrowym bliźniaku a jego skutecznością w rzeczywistości lub w jej odniesieniu. Metody porównam z odpowiednimi metodami bazowymi przy porównywalnym nakładzie treningu i ilości danych rzeczywistych. Aby wyniki były wiarygodne, powtórzę przebiegi dla różnych ziaren losowych i scen, porównania poprę testami statystycznymi i przeprowadzę badania ablacyjne. Dane do treningu, wyboru modelu i końcowej ewaluacji będą rozdzielone.

Eksperymenty uruchomię na superkomputerach WCSS, czyli Wrocławskiego Centrum Sieciowo-Superkomputerowego, gdzie zadaniami zarządza SLURM, oraz na zasobach PLGrid. Zamierzam korzystać z asystentów programowania opartych na sztucznej inteligencji, takich jak Claude Code. Pomogą mi szybciej pisać i testować kod oraz wykonywać rutynowe zadania, jak monitorowanie długich eksperymentów i korekta tekstu.

Wyniki planuję publikować na konferencjach i w czasopismach z listy ministerialnej. W robotyce są to między innymi ICRA, IROS, RSS i IEEE RA-L, a w uczeniu maszynowym i widzeniu komputerowym NeurIPS, ICML, ICLR i CVPR. Tam, gdzie to możliwe, udostępnię artykuły także jako preprinty w serwisie arXiv.

## 10. Streszczenie popularnonaukowe

### Streszczenie popularnonaukowe

Roboty coraz częściej uczy się w cyfrowych bliźniakach, czyli wirtualnych kopiach rzeczywistych miejsc odtworzonych na podstawie ich nagrań, ponieważ nauka w prawdziwym świecie jest powolna, kosztowna i czasem niebezpieczna. Taka kopia nigdy nie jest idealna. Na przykład szklane drzwi mogą zostać odtworzone błędnie i zmylić robota. W efekcie model, który dobrze działa w symulacji, w rzeczywistości często zawodzi, zwłaszcza w miejscach, których wcześniej nie widział. Chcę ustalić, które różnice między kopią a rzeczywistością szkodzą modelowi i w którym miejscu wewnątrz modelu zamieniają się w błędy. Chcę też sprawdzić, które nieliczne rzeczywiste przykłady najlepiej poprawiają zarówno model, jak i kopię. Zbadam to w nawigacji robotów oraz w chwytaniu i przestawianiu przedmiotów. Efektem mają być metody, dzięki którym roboty będą mogły szybciej, taniej i bezpieczniej uczyć się pracy w nowych miejscach.

### Abstract for general public

Robots are increasingly trained in digital twins, that is, virtual copies of real places rebuilt from their recordings, because learning in the real world is slow, costly and sometimes unsafe. Such a copy is never perfect. For example, a glass door may be rebuilt incorrectly and mislead the robot. As a result, a model that works well in simulation often fails in reality, especially in places it has not seen before. I want to find out which differences between the copy and reality harm the model and where inside the model they turn into errors. I also want to check which few real examples best correct both the model and the copy. I will study this in robot navigation and in grasping and moving objects. The result should be methods that let robots learn to work in new places faster, more cheaply and more safely.

## 11. Termin oddania do druku artykułu naukowego lub monografii

Wrzesień 2027 (planowane zgłoszenie na konferencję lub do czasopisma z listy ministerialnej poświęcone robotyce, np. ICRA 2028 lub IEEE Robotics and Automation Letters).

## 12. Inne

Przygotowałem ten plan z pomocą narzędzi sztucznej inteligencji, a konkretnie modelu Claude używanego w Claude Code. Korzystałem z nich przy wyszukiwaniu i weryfikacji literatury, pisaniu wstępnych wersji tekstu, korekcie, redakcji i formatowaniu. Całą treść przejrzałem, a pozycje bibliograficzne zweryfikowano w rejestrach wydawców i serwisów z preprintami.

### Bibliografia

[1] Kadian, A., et al. (2020). Sim2Real predictivity: Does evaluation in simulation predict real-world performance? RA-L.

[2] Ben-David, S., et al. (2010). A theory of learning from different domains. Machine Learning.

[3] Tobin, J., et al. (2017). Domain randomization for transferring deep neural networks from simulation to the real world. IROS.

[4] Chebotar, Y., et al. (2019). Closing the sim-to-real loop: Adapting simulation randomization with real world experience. ICRA.

[5] Tiboni, G., et al. (2024). Domain randomization via entropy maximization. ICLR.

[6] Ganin, Y., et al. (2016). Domain-adversarial training of neural networks. JMLR.

[7] Cheng, S., et al. (2025). Generalizable domain adaptation for sim-and-real policy co-training. NeurIPS.

[8] Zhao, H., et al. (2019). On learning invariant representations for domain adaptation. ICML.

[9] Lei, Y., et al. (2026). A mechanistic analysis of sim-and-real co-training in generative robot policies. arXiv preprint arXiv:2604.13645.

[10] Kerbl, B., et al. (2023). 3D Gaussian splatting for real-time radiance field rendering. ACM TOG.

[11] Torne, M., et al. (2024). Reconciling reality through simulation: A real-to-sim-to-real approach for robust manipulation. RSS.

[12] Qureshi, M. N., et al. (2025). SplatSim: Zero-shot Sim2Real transfer of RGB manipulation policies using Gaussian splatting. ICRA.

[13] Xu, Q., et al. (2026). TwinRL-VLA: Digital twin-driven reinforcement learning for real-world robotic manipulation. ACM MM (arXiv:2602.09023).

[14] Li, X., et al. (2024). Evaluating real-world robot manipulation policies in simulation. CoRL.

[15] Chhablani, G., et al. (2025). EmbodiedSplat: Personalized real-to-sim-to-real navigation with Gaussian splats from a mobile device. ICCV.

[16] Xie, Z., et al. (2025). Vid2Sim: Realistic and interactive simulation from video for urban navigation. CVPR.

[17] Jin, R., et al. (2026). Grounding sim-to-real generalization in robotic manipulation: An empirical study with vision-language-action models. ECCV.

[18] Wang, X., et al. (2026). ReVeal: A reconstruction-aware real-to-sim framework for VLA policy evaluation. arXiv preprint arXiv:2609.23910.

[19] Kachaev, N., et al. (2026). Don't blind your VLA: Aligning visual representations for OOD generalization. AAMAS.

[20] Lee, Y., et al. (2023). Surgical fine-tuning improves adaptation to distribution shifts. ICLR.

[21] Maddukuri, A., et al. (2025). Sim-and-real co-training: A simple recipe for vision-based robotic manipulation. RSS.

[22] Memmel, M., et al. (2024). ASID: Active exploration for system identification in robotic manipulation. ICLR.

[23] Xie, A., et al. (2024). Decomposing the generalization gap in imitation learning for visual robotic manipulation. ICRA.

## 13. Określenie planowanej formy współpracy z promotorem

Z promotorem planujemy cotygodniowe spotkania. Będę na nich przedstawiał postępy i najnowsze wyniki eksperymentów, a razem będziemy ustalać kolejne kroki i pracować nad wspólnymi publikacjami. Będę też uczestniczył w cotygodniowych spotkaniach grupy doktorantów promotora, na których omawiane są bieżące wyniki, problemy i nowe prace w dziedzinie. Na bieżąco będziemy się kontaktować mailowo i przez komunikatory. Kod, wytrenowane modele i źródła LaTeX publikacji będą przechowywane we wspólnych repozytoriach Git.

## 14. Opinia promotora pomocniczego

Nie dotyczy (promotor pomocniczy nie został wyznaczony).

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
| 1 | Udział w zajęciach Szkoły Doktorskiej; zapoznanie się z literaturą i rozważenie możliwych kierunków badań |
| 2 | Udział w zajęciach Szkoły Doktorskiej; przegląd literatury; wybór tematu rozprawy doktorskiej wspólnie z promotorem; przygotowanie Indywidualnego Planu Badawczego |
| 3 | Przygotowanie środowiska badawczego (cyfrowe bliźniaki, symulatory, publiczne zbiory danych); wstępne eksperymenty dotyczące szkodliwych błędów rekonstrukcji (RQ1) |
| 4 | Dalsze eksperymenty dotyczące RQ1; przygotowanie i zgłoszenie pierwszej publikacji na konferencję lub do czasopisma z zakresu robotyki (np. ICRA lub RA-L); pierwsze eksperymenty dotyczące RQ2 |
| 5 | Eksperymenty dotyczące lokalizacji luki wewnątrz modeli i wyrównywania reprezentacji (RQ2); przygotowanie publikacji naukowej |
| 6 | Eksperymenty dotyczące doboru danych rzeczywistych (RQ3) oraz transferu do niewidzianych scen i między zadaniami (RQ4); przygotowanie publikacji; testy na rzeczywistym robocie, jeśli pozwoli na to dostęp |
| 7 | Końcowe eksperymenty i zgłoszenie artykułu na konferencję lub do czasopisma; pierwsza wersja rozprawy doktorskiej |
| 8 | Ukończenie, poprawienie i złożenie rozprawy doktorskiej |

## 4. Termin złożenia rozprawy doktorskiej

Wrzesień 2029

## 5. Uzasadnienie wyboru tematu rozprawy doktorskiej

Uczenie głębokie przyniosło ogromny postęp w widzeniu komputerowym i przetwarzaniu języka, w dużej mierze dzięki olbrzymim ilościom danych zebranych z internetu. Fizyczna sztuczna inteligencja, czyli sztuczna inteligencja w robotach i innych systemach, które postrzegają rzeczywisty świat i działają w nim, nie może opierać się na takich danych. Zbieranie danych z interakcji z rzeczywistymi robotami jest powolne, kosztowne i czasem niebezpieczne, dlatego modele robotów trenuje się zwykle w symulacji. W ostatnim czasie obiecującą alternatywą dla ręcznie tworzonych symulatorów stały się cyfrowe bliźniaki, czyli symulacje zbudowane na podstawie danych rzeczywistych. Metody neuronowej rekonstrukcji scen, takie jak 3D Gaussian Splatting, zamieniają krótkie nagranie rzeczywistego miejsca w fotorealistyczną kopię, w której można wytrenować model, a następnie przenieść go z powrotem do rzeczywistości.

Model, który dobrze działa w swoim cyfrowym bliźniaku, często jednak zawodzi w rzeczywistości, a jeszcze częściej w miejscach, których nigdy nie widział. Żaden cyfrowy bliźniak nie odtwarza świata dokładnie. Wygląd, geometria, oświetlenie i fizyka są jedynie przybliżone, a błędy rekonstrukcji różnią się między obszarami sceny. Wynikający z tego spadek skuteczności nazywa się luką między symulacją a rzeczywistością. Jest to przypadek uczenia przy przesunięciu rozkładu i jedna z głównych przeszkód na drodze rozwoju fizycznej sztucznej inteligencji.

Stosowane obecnie metody rozwiązują ten problem tylko częściowo. Randomizacja domeny zmienia kilka globalnych parametrów symulatora, niezależnie od tego, gdzie cyfrowy bliźniak rzeczywiście jest błędny. Reprezentacje niezmiennicze mogą odrzucać informacje potrzebne do wykonania zadania. Nieliczne dane rzeczywiste zebrane w celu adaptacji służą zwykle do poprawienia albo modelu, albo symulacji, ale nie obu jednocześnie. Większość metod jest też oceniana na jednym zadaniu i kilku scenach, więc nie wiadomo, które właściwości cyfrowego bliźniaka i wyuczonych reprezentacji decydują o tym, czy model będzie działał w rzeczywistości.

Celem moich badań jest zmniejszenie tej luki za pomocą metod, które analizują reprezentacje wyuczone przez modele i wyrównują je na tym etapie, na którym luka powstaje. Chcę ustalić, które błędy rekonstrukcji cyfrowego bliźniaka rzeczywiście szkodzą modelowi, na którym etapie wewnątrz modelu informacja o zadaniu zostaje utracona dla rzeczywistych danych wejściowych oraz jaki niewielki zbiór danych rzeczywistych najlepiej poprawia zarówno cyfrowego bliźniaka, jak i model. Sprawdzę również, czy uzyskane poprawy przenoszą się na niewidziane sceny oraz z jednego zadania na drugie. Zbadam dwa zadania o równej wadze, nawigację robotów i manipulację robotyczną, a wszystkie wyniki będę mierzył na scenach, które nie były używane do treningu.

Wyniki mogą znaleźć zastosowanie w robotyce usługowej, logistycznej i asystującej, gdzie robota można by wytrenować w cyfrowej kopii nowego magazynu, szpitala lub domu, a następnie, po niewielkiej adaptacji w rzeczywistym świecie, niezawodnie tam wykorzystywać. Dotyczą one także autonomicznej jazdy i robotów inspekcyjnych, których modele również są trenowane na danych symulowanych lub zrekonstruowanych.

## 6. Zarys aktualnego stanu badań w tematyce rozprawy doktorskiej

Modele uczenia głębokiego do nawigacji robotów i manipulacji robotycznej potrzebują więcej doświadczenia, niż mogą dostarczyć rzeczywiste roboty, dlatego zwykle trenuje się je w symulacji. Badanie dotyczące nawigacji wykazało, że skuteczność w symulacji może słabo przewidywać skuteczność w rzeczywistości, jeśli symulator nie zostanie starannie dostrojony [1]. Luka między symulacją a rzeczywistością jest szczególnym przypadkiem przesunięcia rozkładu. Teoria adaptacji domenowej ogranicza błąd modelu w domenie docelowej przez jego błąd w domenie źródłowej, rozbieżność między oboma rozkładami oraz łączny błąd najlepszego pojedynczego modelu w obu domenach [2]. Traktuję to ograniczenie wyłącznie jako motywację. Sugeruje ono, by rozkład treningowy obejmował rzeczywistość, by model był niewrażliwy na pozostałą rozbieżność oraz, ponieważ niezmienniczość nie jest ukierunkowana na błąd łączny, a nawet może go zwiększyć, by korygować symulację w stronę rzeczywistości, co może bezpośrednio zmniejszyć ten błąd.

Szeroko stosowanym podejściem jest randomizacja domeny, która zmienia parametry symulatora, takie jak tekstury, tak aby rzeczywistość jawiła się modelowi jako jeszcze jeden wariant [3]. Zbyt szeroka randomizacja prowadzi do zachowawczego działania, dlatego późniejsze prace kształtują jej rozkład, dopasowując go do kilku rzeczywistych przebiegów [4] lub maksymalizując jego entropię przy zachowaniu skuteczności w zadaniu [5]. Metody te dostrajają kilka globalnych parametrów syntetycznego symulatora. Nie uwzględniają błędów zmieniających się w obrębie sceny, typowych dla cyfrowych bliźniaków zrekonstruowanych z danych rzeczywistych.

Innym podejściem jest uczynienie modelu niezmienniczym względem domeny. Trening domenowo-adwersarialny sprawia, że cechy obu domen stają się nierozróżnialne dla klasyfikatora domeny [6]. W robotyce wyrównanie łącznych rozkładów obserwacji i akcji w danych symulowanych i rzeczywistych poprawiło w rzeczywistości działanie polityk trenowanych wspólnie na obu rodzajach danych, czyli modeli odwzorowujących obserwacje na akcje [7]. Niezmienniczość przy niskim błędzie w domenie źródłowej nie gwarantuje jednak transferu. Może ona zwiększać składnik błędu łącznego, gdy rozkłady etykiet, tutaj akcji, różnią się między domenami [8], a pełna niezmienniczość może odrzucać informacje o zadaniu. Niedawna analiza wykazała, że skuteczny trening wspólny na danych symulowanych i rzeczywistych wyrównuje obie domeny, zachowując zarazem ich rozróżnialność [9], zatem sama separowalność domen nie pokazuje, gdzie luka szkodzi zadaniu. Niezmienniczość jest też zwykle wymuszana w miejscach wybranych z góry, takich jak wejście, cechy końcowe lub ustalone warstwy, a nie tam, gdzie według pomiarów luka powstaje.

Nowszym kierunkiem są cyfrowe bliźniaki budowane na podstawie danych rzeczywistych. 3D Gaussian Splatting [10] rekonstruuje fotorealistyczne sceny z wielowidokowych zdjęć i renderuje je w czasie rzeczywistym. W manipulacji cyfrowe bliźniaki wykorzystano do trenowania polityk na podstawie skanu docelowej sceny [11], do przenoszenia polityk opartych na obrazach do rzeczywistości bez rzeczywistych demonstracji [12] oraz do ukierunkowania uczenia ze wzmocnieniem w rzeczywistym świecie na podstawie nagrania telefonem [13]. Badanie SIMPLER [14] wykazało, na podstawie sparowanych ocen w symulacji i w rzeczywistości, że sceny i sterowniki dopasowane do rzeczywistych obrazów dwóch konfiguracji robotów odzwierciedlają rzeczywistą skuteczność tych samych polityk. W nawigacji polityki dostrajano w cyfrowych bliźniakach zbudowanych z nagrania pomieszczenia telefonem [15] oraz trenowano w cyfrowych bliźniakach zbudowanych z monokularnych nagrań miejskich [16]. Wpływ czynników symulacji badano głównie globalnie, na przykład randomizacji, fotorealizmu i realizmu fizyki w rzeczywistej manipulacji [17]. Dla całych przestrzeni roboczych podobieństwo cech wstępnie wytrenowanego modelu między widokami renderowanymi a rzeczywistymi przewidywało zgodność skuteczności w symulacji i w rzeczywistości lepiej niż LPIPS czy PSNR [18]. Otwarte pozostaje pytanie, które lokalne błędy rekonstrukcji szkodzą generalizacji w nawigacji i manipulacji oraz jak zmienność w treningu powinna uwzględniać błąd rekonstrukcji i znaczenie każdego obszaru dla zadania.

Niejasne jest również, gdzie wewnątrz modelu powstaje luka. Sondowanie, czyli odczytywanie informacji ze stanów ukrytych za pomocą prostych klasyfikatorów, wykazało, że dostrajanie do generowania akcji pogarsza reprezentacje wizualne modeli wizja-język-akcja [19]. Niezależnie od tego dostrajanie tylko wybranych warstw pokazało, że najlepsze do adaptacji warstwy zależą od rodzaju przesunięcia [20]. Według mojej wiedzy w modelach trenowanych w cyfrowych bliźniakach nie zlokalizowano etapu, na którym informacja o zadaniu dostępna w symulacji przestaje być możliwa do odtworzenia z rzeczywistych danych wejściowych.

Pozostałą lukę zmniejsza się zwykle za pomocą niewielkiej ilości danych rzeczywistych. Trening wspólny z małym zbiorem danych rzeczywistych daje duże korzyści [21], a aktywna identyfikacja systemu projektuje w symulacji politykę eksploracji, której rzeczywista trajektoria niesie najwięcej informacji o parametrach fizycznych [22]. Najbliższa moim badaniom praca wykorzystuje cyfrowego bliźniaka do znajdowania konfiguracji podatnych na niepowodzenia, w których wykonuje się rzeczywiste przebiegi [13]. Prace te wykorzystują wybrane dane rzeczywiste do poprawienia albo modelu, albo symulacji. Według mojej wiedzy korygowanie obu na podstawie tych samych wybranych danych nie było dotąd badane.

Wreszcie lukę można rozłożyć na czynniki zmienności, których uporządkowanie według trudności jest w dużej mierze zgodne między symulacją a rzeczywistością [23]. Rzadko sprawdza się, czy pomiary wykonane przed zastosowaniem metody przewidują, lepiej niż proste wskaźniki, takie jak wielkość luki, czy jej korzyść przeniesie się na nową scenę lub na inne zadanie. Moja rozprawa podejmuje te pytania.

(Cytowania użyte w tym dokumencie znajdują się w sekcji 12)

## 7. Pytania i hipotezy badawcze

Celem mojej rozprawy jest opracowanie metod uczenia reprezentacji, które poprawią generalizację modeli uczenia głębokiego trenowanych w cyfrowych bliźniakach zbudowanych na podstawie danych rzeczywistych, tak aby modele niezawodnie działały w rzeczywistości i w miejscach niewidzianych podczas treningu. Metody nie powinny być związane z konkretnym robotem, sceną ani zadaniem.

Na początku nie będę dysponował własnym robotem, a modele będę trenował na akademickich klastrach GPU, więc metody muszą działać w tej skali. Będę korzystał z publicznych zbiorów danych zawierających niezależne nagrania tych samych rzeczywistych scen. Zbadam dwa zadania, nawigację robotów i manipulację robotyczną, a wszystkie wyniki muszą być mierzone na odłożonych scenach, które nie były używane do treningu ani do wyboru modelu.

Pytania (RQ) i hipotezy (H) moich badań są następujące:

1. RQ1. Które błędy rekonstrukcji cyfrowego bliźniaka, zmieniające się w obrębie sceny, szkodzą generalizacji trenowanych w nim modeli nawigacji i manipulacji?
2. H1. Szkodliwość błędu w danym obszarze lepiej przewiduje to, jak bardzo zmienia on cechy ustalonego, wstępnie wytrenowanego kodera wizualnego na widokach renderowanych z tym błędem i bez niego, niż jego wielkość w obrazie lub geometrii, np. PSNR, LPIPS czy błąd głębi. Po drugie, randomizacja każdego obszaru zgodnie z jego szacowanym błędem rekonstrukcji i znaczeniem dla zadania zapewnia lepszą generalizację niż jednorodna randomizacja o tej samej łącznej sile.
3. RQ2. Na którym etapie modelu trenowanego lub dostrajanego w cyfrowym bliźniaku rzeczywiste dane wejściowe po raz pierwszy tracą informację o zadaniu, która jest dostępna dla danych symulowanych? Oczekuję, że da się wskazać najwcześniejszy taki etap lub wąski zakres etapów, znaleziony za pomocą sond liniowych weryfikowanych zadaniami kontrolnymi, a za pomocą interwencji przyczynowych sprawdzę, czy model korzysta z tej informacji.
4. H2. Wyrównywanie reprezentacji symulowanych i rzeczywistych na tym etapie zmniejsza lukę między symulacją a rzeczywistością bardziej niż takie samo wyrównywanie na wejściu, na cechach końcowych, na wszystkich etapach lub w warstwach wybranych według istniejących kryteriów, przy tej samej ilości danych rzeczywistych i tym samym nakładzie treningu.
5. RQ3. Które dane rzeczywiste, wybrane w ramach ustalonego budżetu na podstawie sygnałów opartych na reprezentacjach, wypracowanych w RQ1 i RQ2, najlepiej poprawiają zarówno cyfrowego bliźniaka, jak i model? Oczekuję, że wykorzystanie tych samych wybranych danych do poprawienia obu zmniejsza lukę bardziej niż poprawienie tylko jednego z nich, a mój sposób doboru danych porównam z doborem losowym i doborem opartym na niepowodzeniach.
6. RQ4. Czy uzyskane korzyści przenoszą się, przy niezmienionych ustawieniach, na niewidziane sceny oraz z jednego zadania na drugie, i czy właściwości przesunięcia zmierzone wcześniej pozwalają przewidzieć to lepiej niż proste wskaźniki, takie jak wielkość luki lub rozbieżność na poziomie obrazu?
7. Plan awaryjny. Jeśli szkodliwość błędu zależy od jego wielkości, a nie od zmiany cech, randomizację i dobór danych mogą zamiast tego ukierunkowywać niepewność rekonstrukcji i wrażliwość akcji, choć niepewność pomija błędy, które rekonstrukcja odtwarza w spójny sposób. Skorzystam z tego rozwiązania tylko wtedy, gdy sygnały oparte na reprezentacjach okażą się mało informatywne.

## 8. Wkład spodziewanych wyników dla rozwoju dyscypliny naukowej

Głównym oczekiwanym wkładem mojej rozprawy jest zestaw metod uczenia reprezentacji, dzięki którym modele uczenia głębokiego trenowane w cyfrowych bliźniakach lepiej generalizują na rzeczywistość i na niewidziane miejsca. Spodziewam się również dowiedzieć, czy luka między symulacją a rzeczywistością wynika głównie z ograniczonego zbioru różnic istotnych dla zadania, które można znaleźć wśród błędów rekonstrukcji cyfrowego bliźniaka, zlokalizować wewnątrz modelu i zmniejszyć za pomocą niewielkiej ilości dobrze dobranych danych rzeczywistych.

Eksperymenty powinny wskazać, które błędy rekonstrukcji szkodzą generalizacji, na którym etapie modelu informacja o zadaniu jest tracona dla rzeczywistych danych wejściowych, kiedy opłaca się poprawiać zarówno cyfrowego bliźniaka, jak i model na podstawie tych samych danych rzeczywistych oraz czy takie korzyści przenoszą się na nowe sceny i między nawigacją a manipulacją. Ponieważ pytania te dotyczą uczenia przy przesunięciu rozkładu, wyniki mogą mieć znaczenie także dla adaptacji domenowej, uczenia reprezentacji i uczenia aktywnego w ogólności. Planuję udostępnić kod, protokół ewaluacji oraz, jeśli pozwolą na to licencje, wytrenowane modele, tak aby inni mogli w ten sam sposób porównywać metody na odłożonych scenach. Mam nadzieję, że rozprawa połączy badania z zakresu uczenia maszynowego dotyczące przesunięcia rozkładu z praktyką robotyki i ułatwi wdrażanie uczących się robotów w nowych magazynach, szpitalach i domach.

## 9. Planowane metody badawcze

Trzonem pracy będzie budowanie cyfrowych bliźniaków rzeczywistych scen, trenowanie i dostrajanie w nich modeli uczenia głębokiego oraz projektowanie metod, które analizują i wyrównują reprezentacje wyuczone przez te modele. Ponieważ nie istnieje ugruntowana teoria gwarantująca generalizację z symulacji do rzeczywistości, większość pracy będzie miała charakter empiryczny. Teorię adaptacji domenowej wykorzystam jako motywację, a właściwości moich metod będę w miarę możliwości analizował teoretycznie.

Głównymi narzędziami będą PyTorch do trenowania modeli, gsplat do 3D Gaussian Splatting [10] i COLMAP do wyznaczania pozycji kamer, symulator Habitat do nawigacji i ManiSkill3 do manipulacji, Git z repozytoriami GitHub do kontroli wersji oraz Hugging Face do pobierania i publikowania modeli i zbiorów danych. Tam, gdzie to możliwe, będę zaczynał od modeli wstępnie wytrenowanych. Kod i skrypty ewaluacyjne zostaną udostępnione, a jeśli pozwolą na to licencje, także wytrenowane modele i dane pochodne.

Na początku nie będę dysponował własnym robotem, dlatego ewaluację będę prowadził głównie na danych publicznych. W przypadku nawigacji wykorzystam publiczne zbiory danych rzeczywistych scen wewnątrz budynków z niezależnymi nagraniami tych samych scen, takie jak ScanNet++ i MuSHRoom. Cyfrowego bliźniaka zbuduję z jednego nagrania, a drugie dostarczy rzeczywistych klatek i odniesienia opartego na zbiorze danych. To odniesienie jest miarą zastępczą (proxy) rzeczywistości. Mierzy ono lukę wynikającą z wierności rekonstrukcji i pomija różnice w napędach i czujnikach. W przypadku manipulacji zbuduję cyfrowe bliźniaki rzeczywistych scen stołowych na podstawie obrazów z publicznych zbiorów danych robotycznych, zgodnie z dopasowaniem wizualnym stosowanym w SIMPLER [14], i porównam je z opublikowanymi wynikami tych samych polityk na rzeczywistych robotach. Jeśli pozwoli na to dostęp do laboratorium robotycznego uczelni, wykorzystam rzeczywistego robota, aby sprawdzić kierunek wybranych wyników i trafność miary zastępczej.

W przypadku RQ1 będę korygował jeden rodzaj błędu rekonstrukcji naraz w wybranych obszarach, korzystając z dokładniejszego odniesienia, takiego jak skany laserowe ze ScanNet++, lub wprowadzał go w kontrolowany sposób, i mierzył wpływ na wytrenowany model. Porównam zmianę cech ustalonego, wstępnie wytrenowanego kodera z PSNR, LPIPS i błędem głębi jako predyktorami szkodliwości oraz sprawdzę randomizację zależną od obszaru w porównaniu z jednorodną randomizacją o tej samej łącznej sile (H1). W przypadku RQ2 wytrenuję sondy liniowe z zadaniami kontrolnymi na symulowanych stanach ukrytych i przetestuję je na sparowanych stanach rzeczywistych. Interwencje przyczynowe na stanach ukrytych, takie jak podmiana sondowanej podprzestrzeni z symulowanych danych wejściowych do rzeczywistych, pozwolą sprawdzić, czy model korzysta z utraconej informacji. Następnie dołączę funkcję straty wyrównującej na zidentyfikowanym etapie i porównam ją z wyrównywaniem na wejściu, na cechach końcowych, na wszystkich etapach i w warstwach wybranych według istniejących kryteriów (H2). W przypadku RQ3 porównam reguły doboru danych rzeczywistych z doborem losowym i doborem opartym na niepowodzeniach przy równych budżetach, a także porównam poprawianie zarówno cyfrowego bliźniaka, jak i modelu z poprawianiem tylko jednego z nich. W przypadku RQ4 zastosuję metody przy niezmienionych ustawieniach na odłożonych scenach i sprawdzę, czy pomiary wykonane wcześniej przewidują uzyskane korzyści, wykorzystując korelację rang z odpowiednimi testami istotności.

Będę mierzył odsetek sukcesów oraz lukę między symulacją a rzeczywistością, czyli różnicę między skutecznością tego samego modelu w cyfrowym bliźniaku a w rzeczywistości lub w jej odniesieniu, na odłożonych scenach. Metody porównam z odpowiednimi metodami bazowymi przy porównywalnym nakładzie treningu i ilości danych rzeczywistych. Aby uzyskać wiarygodne wyniki, będę powtarzał przebiegi dla różnych ziaren losowych i scen, stosował testy statystyczne do porównań oraz przeprowadzał badania ablacyjne. Dane do treningu, wyboru modelu i końcowej ewaluacji będą rozdzielone.

Eksperymenty będę prowadził na superkomputerach Wrocławskiego Centrum Sieciowo-Superkomputerowego (WCSS), z zadaniami zarządzanymi przez SLURM, oraz na zasobach PLGrid. Zamierzam korzystać z asystentów programowania opartych na sztucznej inteligencji, takich jak Claude Code, aby przyspieszyć pisanie i testowanie kodu oraz pomagać sobie w rutynowych zadaniach, takich jak monitorowanie długich eksperymentów i korekta tekstu.

Planuję publikować wyniki na konferencjach i w czasopismach z listy ministerialnej, takich jak ICRA, IROS, RSS i IEEE RA-L w robotyce oraz NeurIPS, ICML, ICLR i CVPR w uczeniu maszynowym i widzeniu komputerowym. Tam, gdzie to możliwe, artykuły będą również udostępniane jako preprinty w serwisie arXiv.

## 10. Streszczenie popularnonaukowe

Roboty coraz częściej uczy się w cyfrowych bliźniakach, czyli wirtualnych kopiach rzeczywistych miejsc odtworzonych na podstawie ich nagrań, ponieważ nauka w prawdziwym świecie jest powolna, kosztowna i czasem niebezpieczna. Taka kopia nigdy nie jest idealna. Na przykład szklane drzwi mogą zostać odtworzone błędnie i zmylić robota. W efekcie model, który dobrze działa w symulacji, w rzeczywistości często zawodzi, zwłaszcza w miejscach, których wcześniej nie widział. Chcę ustalić, które różnice między kopią a rzeczywistością naprawdę szkodzą modelowi, w którym miejscu wewnątrz modelu zamieniają się w błędy oraz które nieliczne rzeczywiste przykłady najlepiej poprawiają zarówno model, jak i kopię. Sprawdzę to w nawigacji robotów oraz w chwytaniu i przestawianiu przedmiotów. Oczekiwanym wynikiem są metody, dzięki którym roboty będą mogły szybciej, taniej i bezpieczniej uczyć się pracy w nowych miejscach.

## 11. Termin oddania do druku artykułu naukowego lub monografii

Wrzesień 2027 (planowane zgłoszenie na konferencję lub do czasopisma z listy ministerialnej poświęcone robotyce, np. ICRA 2028 lub IEEE Robotics and Automation Letters).

## 12. Inne

Przygotowałem ten plan z pomocą narzędzi sztucznej inteligencji (Claude, używanego za pośrednictwem Claude Code). Używałem ich do wyszukiwania i weryfikacji literatury, przygotowywania wstępnych wersji tekstu, korekty, redakcji i formatowania. Przejrzałem całą treść, a pozycje bibliograficzne zostały zweryfikowane w rejestrach wydawców i serwisów z preprintami.

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

Wraz z promotorem planujemy cotygodniowe spotkania, na których będę przedstawiał postępy i najnowsze wyniki eksperymentów, będziemy uzgadniać kolejne kroki i pracować nad wspólnymi publikacjami. Ponadto będę uczestniczył w cotygodniowych spotkaniach grupy doktorantów promotora, na których omawiane są bieżące wyniki, problemy i nowe prace w dziedzinie. Bieżący kontakt będzie odbywał się drogą mailową i za pomocą komunikatorów, a kod, wytrenowane modele i źródła LaTeX publikacji będą przechowywane we wspólnych repozytoriach Git.

## 14. Opinia promotora pomocniczego

Nie dotyczy (promotor pomocniczy nie został wyznaczony).

# RAPORT – temat: zwiad po strzelaniu

> Autor: Jakub. Kopia referencyjna (snapshot z 2026-09-26) — patrz [README.md](README.md).
> Oryginał: https://docs.google.com/document/d/17JDY8zzVpUDmG0eyuPWLyqNK-GnWKb9h/edit

## 1. Proponowany temat

Metoda oceny gotowości przodka do wejścia załogi po robotach strzałowych na podstawie pomiarów realizowanych przez autonomicznego robota kroczącego

## 2. Skrótowy opis

### Problem

- kontrola przed wejściem do świeżo odstrzelonego miejsca to jedna z najważniejszych i zarazem najbardziej niebezpiecznych czynności w zapobieganiu obwałom [1]
- pracownicy ginęli i odnosili obrażenia podczas prac po strzelaniu; narażeni są na gazy postrzałowe, ruchy skał i zjawiska sejsmiczne wywołane strzałem [2]
- obwały skał odpowiadają za ok. jedną czwartą śmiertelnych wypadków w górnictwie [3]
- kontrola bezpieczeństwa przodka przed rozpoczęciem pracy należy do zadań górnika eksploatacji podziemnej [4]; wymagania określa rozporządzenie o prowadzeniu ruchu podziemnych zakładów górniczych [5]

### Stan obecny

- większość kopalń ustala czas wejścia po strzelaniu na podstawie doświadczenia i obserwacji [6]; przeszacowanie oznacza straty produkcji, niedoszacowanie — urazy i ofiary śmiertelne [6]
- ankiety w kopalniach wskazują dominację strategii stałego czasu, a niewiele kopalń monitoruje gazy postrzałowe [7]
- obecna praktyka: pomiar przenośnymi detektorami po upływie stałego czasu [8]
- modele czasu wejścia zakładają natychmiastowe uwolnienie gazów, a 60–70% może pozostać uwięzione w górotworze lub urobku [9]
- wykrywanie luźnych skał wciąż wykonuje głównie doświadczony personel [10]

### Propozycja

- robot kroczący wchodzi do przodka jako pierwszy, przed ludźmi
- mierzy atmosferę (także przy urobku) i ocenia stan stropu i ociosów metodami bezkontaktowymi
- dostarcza podstawy do decyzji: przodek gotowy / niegotowy

### Dlaczego robot

- robot uzasadnia się tam, gdzie nie ma maszyny, na której można zamontować czujnik
- po strzale przodek jest pusty — w KGHM przy strzelaniach grupowych odpala się jednocześnie dziesiątki przodków [11]
- kontrast: istnieją stacjonarne systemy monitoringu gazów do decyzji o wejściu [8, 12] — mierzą jednak w punktach stałych, nie przy urobku (hipoteza — do potwierdzenia)

### Dlaczego robot kroczący

- robot kroczący jest już stosowany po strzelaniu w przemyśle (LKAB), m.in. dlatego, że drony mają ograniczony czas pracy, wzbijają pył i tracą łączność [13]
- dron może zakłócać pomiar przez strumień wirników przy pomiarze lokalnych chmur gazu [14, 26]; w jednorodnej chmurze wpływ ten jest pomijalny [15]
- hipoteza: przy urobku, gdzie uwalniają się gazy uwięzione, rozkład gazu jest lokalny — robot kroczący stojący przy urobku nie wytwarza strumienia powietrza

### Teza główna

Autonomiczny robot kroczący wykonujący pomiary atmosfery i ocenę stanu stropu i ociosów może dostarczyć podstawy do decyzji o wejściu załogi do przodka po robotach strzałowych z wiarygodnością co najmniej porównywalną z obecną praktyką, bez narażania człowieka.

## 3. Luki badawcze

| # | luka | podparcie | źródło |
|---|---|---|---|
| G1 | Czas wejścia po strzelaniu ustala się głównie na podstawie doświadczenia; metody teoretyczne nie uwzględniają zmienności warunków | cytat | [6, 7, 8] |
| G2 | Modele czasu wejścia zakładają natychmiastowe uwolnienie gazów, choć 60–70% może pozostać w urobku; wcześniejsze badania pomijały ten efekt | cytat | [9, 16] |
| G3 | Strzelanie zwiększa uwalnianie H₂S z górotworu w polskiej kopalni miedzi, a zachowanie gazu po strzale różniło się istotnie między okresami badań | cytat — KGHM | [17] |
| G4 | Pomiar gazów z drona: strumień wirników rozcieńcza i odsuwa lokalne chmury gazu [14, 26]; w jednorodnej chmurze efekt jest pomijalny [15]; po ruchu drona potrzebny jest czas stabilizacji [18] | kontrast | [14, 15, 18, 26] |
| G5 | Kontrola przed wejściem po strzale jest jedną z najniebezpieczniejszych czynności; wykrywanie luźnych skał wykonuje człowiek | cytat | [1, 10] |
| G6 | Termowizja do wykrywania luźnych skał ma wąskie pole widzenia [1] i słabnie przy równowadze termicznej [19]; przepływ powietrza wentylacyjnego wzmacnia kontrasty [3]; brak weryfikacji w kopalniach miedzi | cytat + brak publ. | [1, 3, 19] |
| G7 | Robot kroczący jest używany po strzelaniu w przemyśle [13, 20], lecz nie znaleziono publikacji naukowej oceniającej jakość jego pomiarów; pomiary gazów z robotów mobilnych mają własną, rozbudowaną literaturę [28] | brak publ. | [13, 20, 28] |
| G8 | Luleå mierzy gazy po strzale dronem [21], CSIR ocenia strop [1] — nie znaleziono kontroli łączącej oba elementy | kontrast | [1, 21] |
| G9 | Brak metody decyzji o wejściu załogi na podstawie pomiarów robota | brak publ. | — |

## 4. Pytania badawcze

| # | pytanie | luki |
|---|---|---|
| PB1 | Czy lokalne pomiary atmosfery w przodku, w tym przy urobku, dają pełniejszy obraz warunków po strzelaniu niż stały czas wyczekiwania i pomiary stacjonarne? | G1, G2, G3 |
| PB2 | Czy bezkontaktowe metody wykrywania luźnych skał zachowują skuteczność w warunkach przodków kopalń miedzi? | G5, G6 |
| PB3 | Jak lokomocja krocząca wpływa na jakość pomiarów atmosfery i danych o stanie wyrobiska? | G4, G7 |
| PB4 | Jak na podstawie pomiarów robota podjąć wiarygodną decyzję o dopuszczeniu załogi do przodka? | G8, G9 |

## 5. Zakres misji

| obszar | co | podstawa |
|---|---|---|
| atmosfera | CO, NO₂, O₂ | gazy postrzałowe [6, 8] |
| | H₂S, CH₄ | H₂S jako nowe zagrożenie w kopalniach KGHM [22, 23]; strzał zwiększa uwalnianie [17] |
| | stężenia przy urobku | gazy uwięzione w urobku [9, 16] |
| | przepływ powietrza | do potwierdzenia |
| strop i ociosy | luźne skały — termowizja + lidar | [1, 3, 10, 19] |
| | zmiany geometrii | detekcja zmian po strzale robiona przez Luleå [21] — pomocniczo |
| warunki ogólne | zapylenie, temperatura, przejezdność | pomocniczo |
| poza zakresem | niewypały, opukiwanie, rozdrobnienie urobku | kontakt lub inny cel |

## 6. Kontekst KGHM

- strzelania grupowe: jednoczesne odpalenie dziesiątek przodków w celu prowokowania wstrząsów [11, 24]
- H₂S po raz pierwszy stwierdzony w 2010 r., uznany za nowy rodzaj zagrożenia gazowego w kopalniach KGHM [22]; występuje w ZG Polkowice-Sieroszowice i ZG Rudna; stężenie powyżej 1000 mg/m³ powoduje utratę przytomności i zgon [23]
- w KGHM obrywkę wykonuje się m.in. samojezdnym wozem do obrywki [25] — do potwierdzenia, czy kontrola przed obrywką jest wizualna
- do potwierdzenia: pora strzelań (koniec zmiany?), typowy czas wyczekiwania, sposób pierwszej kontroli

## 7. Istniejące rozwiązania i luki, które zostawiają

| rozwiązanie | co robi | jakie luki zostawia |
|---|---|---|
| dron Luleå [21] | pierwsza w pełni autonomiczna misja z pomiarem gazów po rzeczywistym strzale, ok. 40 min po odpaleniu; detekcja zmian geometrii | tylko atmosfera, bez oceny stropu (G8); ograniczony czas lotu [13]; zakłócenia pomiaru przy lokalnych chmurach gazu [14, 26]; czas stabilizacji po ruchu [18] (G4) |
| Spot w LKAB [13, 20] | pomiary gazów i lidar w świeżo odstrzelonych rejonach; planowana inspekcja po nocnym strzelaniu | sterowany zdalnie; brak publikacji oceniających jakość pomiarów (G7); brak metody decyzji o wejściu (G9) |
| robot CSIR [1, 27] | ocena stropu: skaner 3D z termowizją, wykrywanie chłodniejszych, spękanych obszarów; opukiwanie do weryfikacji | tylko strop, bez atmosfery (G8); kopalnie złota RPA — wyrobiska ok. 1 m wysokości, inne warunki niż w KGHM (G6); opukiwanie wymaga kontaktu |
| stacjonarne systemy monitoringu gazów [8, 12] | ciągły pomiar gazów w stałych punktach, np. w prądzie powietrza zużytego | hipoteza: przodek postępuje z każdym cyklem, a czujniki stoją w miejscu; brak pomiaru przy urobku (G2) |
| żadne z powyższych | — | brak metody decyzji o wejściu łączącej ocenę atmosfery i stanu stropu (G9) |

## Źródła

1. Dickens J.S. i in. (CSIR), *The design of an automated 3D-thermal mine scanning tool*, 2012 — https://www.researchgate.net/publication/261111958
2. Ontario Ministry of Labour, *Post-blast examinations in mines* — https://ontario.ca/page/post-blast-examinations-mines
3. Missouri S&T, *AI-Driven Frameworks for Mitigating Rockfall Hazards… Through Thermal Imaging*, poster, 2026 — https://scholarsmine.mst.edu/src/2026/graduate_poster_session/24/
4. ORE, *Górnik eksploatacji podziemnej — opis zawodu* — https://zasobyip2.ore.edu.pl/pl/publications/download/50692
5. Rozporządzenie Ministra Energii w sprawie szczegółowych wymagań dotyczących prowadzenia ruchu w podziemnych zakładach górniczych, Dz.U. 2017 poz. 1118 — https://eli.gov.pl/api/acts/DU/2017/1118/text.html
6. Tiile R.N., rozprawa doktorska o czasie wejścia po strzelaniu, Missouri S&T — https://scholarsmine.mst.edu/doctoral_dissertations/2794
7. *Development of an Assessment Tool to Minimize Safe after Blast Re-Entry Time to Improve the Mining Cycle*, Missouri S&T — https://scholarsmine.mst.edu/min_nuceng_facwork/1
8. Bahrami D., Yuan L., Rowland J.H., Thomas R.A., *Evaluation of Post-Blast Re-Entry Times Based On Gas Monitoring of Return Air*, Mining, Metallurgy & Exploration 36 (2019) 513–521. DOI: 10.1007/s42461-019-0058-6
9. Adhikari A., Jayaraman Sridharan S., Tukkaraja P., Sasmito A., *The Effect of Porous Muckpile on Dilution of Blasting Induced Fumes*, ISEE, 2020 — https://onemine.org/documents/the-effect-of-porous-muckpile-on-dilution-of-blasting-induced-fumes
10. Radl A., Mitra R., Clausen E., *Loose rock detection methods for automating the scaling process*, Mining Technology 131(4), 2022. DOI: 10.1080/25726668.2022.2078091
11. Mertuszka P., Fuławka K., Stolecki L., Szumny M., *Seismic effect of group winning blasting — case study from a Polish copper mine*. arXiv: 1903.04816
12. Conspec, *Gas detection solutions for post-blast re-entry* (materiał komercyjny) — https://conspec-controls.com/?p=18591
13. Boston Dynamics, *LKAB and Luleå University of Technology* (studium przypadku) — https://bostondynamics.com/case-studies/lkab-and-lulea-university-of-technology/
14. Taupe P. i in. (AIT), *Dealing with UAV downwash effects during airborne detection of localised gas plumes*, ERCIM News 133 — https://ercim-news.ercim.eu/en133/r-i/dealing-with-uav-downwash-effects-during-airborne-detection-of-localised-gas-plumes
15. Brinkman J.L., Johnson C.E., *Effects of Downwash from a 6-Rotor Unmanned Aerial Vehicle (UAV) on Gas Monitor Concentrations*, Mining, Metallurgy & Exploration, 2021. DOI: 10.1007/s42461-021-00436-5
16. Adhikari A. i in., *The Effect Of Trapped Fumes On Clearance Time In Underground Development Blasting*, SME, 2022 — https://onemine.org/documents/the-effect-of-trapped-fumes-on-clearance-time-in-underground-development-blasting
17. Banasiewicz A., Kotyla M., Gola S., *Assessment of the Impact of Blasting Operations on the Intensity of Gas Emission from Rock Masses: A Case Study of Hydrogen Sulfide Occurrence in a Polish Copper Ore Mine*, Applied Sciences 15(23), 12781, 2025. DOI: 10.3390/app152312781
18. Brinkman J.L., Davis B., Johnson C.E., *Post-movement stabilization time for the downwash region of a 6-rotor UAV for remote gas monitoring*, Heliyon 6(9), e04994, 2020. DOI: 10.1016/j.heliyon.2020.e04994
19. *Application of Infrared Thermography and the Acoustic Emission Technology for Loose Rock Detection*, Mining, Metallurgy & Exploration, 2026. DOI: 10.1007/s42461-026-01469-4 — autorzy do uzupełnienia
20. LKAB, *Spot is breaking new ground at LKAB* — https://lkab.com/en/news/spot-is-breaking-new-ground-at-lkab/
21. Nordström S. i in., *Safety Inspections and Gas Monitoring in Hazardous Mining Areas Shortly After Blasting Using Autonomous UAVs*, Journal of Field Robotics, 2025. DOI: 10.1002/rob.22500
22. Kijewski P., Kubiak J., Gola S., artykuł o siarkowodorze w O/ZG Polkowice-Sieroszowice — https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-article-AGHM-0050-0019
23. Biuletyn PIG — gaz ziemny i siarkowodór w kopalniach Rudna i Polkowice-Sieroszowice — https://geojournals.pgi.gov.pl/bp/article/download/28669/pdf/44956
24. Gogolewska A.B., Kowalczyk M., *Group winning blasting as a measure to mitigate seismic hazard in a deep copper ore mine, SW Poland*, Mining Science 27, 2020 — https://www.dbc.wroc.pl/dlibra/publication/152258/edition/110127/content
25. Egzamin zawodowy GIW.10 — przykładowy zakres robót (obrywka wozem SWB) — https://zawodowe.edu.pl/arkusz-praktyczny/giw10-2023-styczen-01/klucz-odpowiedzi.pdf
26. Burgués J., Marco S., *Environmental chemical sensing using small drones: A review*, Science of the Total Environment 748, 141172, 2020. DOI: 10.1016/j.scitotenv.2020.141172
27. Green J.J., *CSIR Centre for Mining Innovation and the mine safety platform robot*, IEEE SSRR 2012, College Station — http://hdl.handle.net/10204/6685 (DOI do uzupełnienia z IEEE Xplore)
28. Lilienthal A.J., Loutfi A., Duckett T., *Airborne Chemical Sensing with Mobile Robots*, Sensors 6, 1616–1678, 2006. DOI: 10.3390/s6111616

**Stan DOI:** Bez DOI z natury: rozprawy, konferencje ISEE/SME, strony urzędowe i przemysłowe. Do uzupełnienia: [19] autorzy, [24] Mining Science, [23] Biuletyn PIG, [27] IEEE SSRR.

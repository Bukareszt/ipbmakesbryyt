# Resources & feasibility — verified facts (checked 2026-09-26)

Scope: GitHub issue #3. Every fact has a source URL. **UNVERIFIED** = we could not confirm it from a primary
source, so don't state it as fact in the IPB.

---

## 1. Robotics labs and equipment

### K46 (Katedra Sztucznej Inteligencji) and T. Kajdanowicz's group
- **K46 has no robotics research group.** None of its 14 research groups works on robotics. Their topics are
  ML, NLP, computer vision, complex networks, biomedical AI and security. Source: https://ai.pwr.edu.pl/research-groups
- **Kajdanowicz leads two groups:**
  - *Centrum Zastosowań Sztucznej Inteligencji* works on agentic AI.
  - *Grupa Uczenia Reprezentacji* works on GNNs, knowledge graphs and weight-space models.

  Source: https://ai.pwr.edu.pl/research-groups
- **Robotics hardware in K46 or his groups: none found.** No hardware or lab page was published. This is
  **UNVERIFIED** (absence of evidence only), so ask the supervisor.
- **Possibly relevant K46 group:** genwro.AI (head M. Zięba) works on generative models, 3D and computer
  vision, which is relevant to Gaussian-splatting reconstruction. Source: https://ai.pwr.edu.pl/research-groups
- **Kajdanowicz:** dr hab. inż., prof. uczelni, head of K46. His research interests are LLMs, ML,
  representation learning and deep learning, not robotics.
  - https://ai.pwr.edu.pl/people/tomasz-kajdanowicz
  - https://wit.pwr.edu.pl/wydzial/struktura-organizacyjna/pracownicy/tomasz-kajdanowicz
  - https://pwr.edu.pl/uczelnia/aktualnosci/dolnoslaski-klucz-sukcesu-2025-dla-naszego-naukowca-14008.html

### Closest existing robotics labs at PWr: Katedra Cybernetyki i Robotyki (K29, faculty W12N)
Source for the lab list: https://k29.pwr.edu.pl/dydaktyka/laboratoria

- **Laboratorium Robotów Autonomicznych "Denali"** (C-16, room L1.5):
  - Pioneer 3-DX mobile robots on ROS 2 (ros2aria), a DrRobot Jaguar 4x4 indoor/outdoor platform, and a
    Robai Cyton arm.
  - Remote access via VPN/x2go.
  - Contact: l15@kcir.pwr.edu.pl.
  - Source: https://denali.kcir.pwr.edu.pl/robots.php
- **Laboratorium Robotyki** (C-3, room 010):
  - Mostly manipulators: UR3, FANUC LR Mate, ABB IRB 120.
  - e-Puck mini robots; ROS and Gazebo.
  - Source: https://lr.kcir.pwr.edu.pl/
- **Laboratorium Inteligencji Robotów** (C-3, room 07): does research on mobile robots, AI and vision. No
  equipment list is published (UNVERIFIED). Source: https://k29.pwr.edu.pl/dydaktyka/laboratoria
- **LiDAR / RGB-D sensors:** none of these pages lists them, so availability is **UNVERIFIED**.
- **KoNaR student club (K29):**
  - The "Ariadna" autonomous mobile platform and the "Cerber" quadruped.
  - https://wefim.pwr.edu.pl/studenci/aktywnosc-studencka/kola-naukowe/kolo-naukowe-robotykow-konar
  - https://pwr.edu.pl/uczelnia/aktualnosci/na-pwr-powstaje-modulowy-robo-pies-do-zadan-specjalnych-14133.html

### Planned at W4: PL-6G national 6G laboratory (announced 27.08.2026, about 63 mln zł FENG)
- Its "Laboratorium Usług 6G" is to test autonomous systems and robotics with ground and aerial drones that
  carry lidar/radar and high-resolution cameras, plus Digital-Twin and AI compute.
- The W4 PIs are dr inż. P. Schauer and dr inż. Ł. Falas.
- This is **future** equipment: the hosting site and the timeline are not stated.
- Source: https://pwr.edu.pl/uczelnia/aktualnosci/satelity--drony-i-cyfrowe-blizniaki-powstanie-krajowe-laboratorium-sieci-i-uslug-6g-14277.html

> **Implication for the IPB:** §3 and §9 currently assume a mobile robot "at the K46 laboratory". Nothing we
> found supports that. Before signing, either:
> - (a) confirm with the supervisor that the group has or will buy a platform (e.g. from Preludium or
>   Minigrant funds), or
> - (b) name a K29 "Denali" collaboration, or
> - (c) phrase it neutrally ("mobile robot platform available at PWr").

---

## 2. Compute (GPU)

### WCSS (Wrocław, at PWr)
- **Lem cluster (2024):**
  - 76 GPU nodes, each with 4× NVIDIA H100 96 GB, so **304 H100** in total.
  - Also 40 nodes with A30 and 188 CPU nodes. About 21 PFLOPS.
  - https://www.wcss.pl/en/hpc/
  - https://man.e-science.pl/pl/kdm/lem-parametry
- **Bem 2** is CPU only. Source: https://www.wcss.pl/en/hpc/
- **GPU queues** (https://man.e-science.pl/i/402):
  - lem-gpu-short: 3-day limit.
  - lem-gpu-normal: 7-day limit.
  - lem-gpu-interactive: 6 h, 1 GPU.
  - plgrid-lem-gpu-h100: open to PLGrid users only.
- **Access for PhD students:**
  1. Create an account at e-science.pl.
  2. Apply for the "Przetwórz na superkomputerze" service with GPU hours. Doctoral students may apply and must
     name their supervisor.
  3. Access is free for non-commercial research and lasts 1 year.
  4. You must file an annual report and acknowledge WCSS in publications.

  Sources:
  - https://man.e-science.pl/pl/kdm/uzytkownik
  - https://man.e-science.pl/pl/kdm/slurm/gpu

### PLGrid
- **"Doktorant" affiliation:**
  - For students of Polish doctoral schools.
  - Valid for 6 months and renewable. The supervisor ("Opiekun") approves it.
  - Lets you set up your own team and apply for your own computing grant.
  - Source: https://guide.plgrid.pl/pl/portal-for-science/affiliations/select
- **Athena (Cyfronet):** 384× NVIDIA A100. Source: https://guide.plgrid.pl/pl/infrastructure/resources/supercomputers/athena
- **Helios (Cyfronet):** 440× NVIDIA GH200 96 GB. A grant application must list related projects and a
  KDM-centre cooperant. Source: https://guide.plgrid.pl/pl/infrastructure/resources/supercomputers/helios
- **Lem (WCSS)** is also offered through PLGrid. Source: https://guide.plgrid.pl/pl/infrastructure/resources/supercomputers/lem

### K46-internal
- **K46 GPU servers:** not publicly documented, so **UNVERIFIED**. Ask the supervisor.
- **CLARIN LLM-infrastructure project at K46 (2025–2027):** whether PhD students can use its resources is
  **UNVERIFIED**. Source: https://ai.pwr.edu.pl/projects/clarin-llm-infrastructure

---

## 3. Ministerial list points (wykaz czasopism i materiałów konferencyjnych)

**List in force:** the komunikat of **5 January 2024**. The journal sheet and the conference sheet
("Konferencje_nauk") are in the same file.
- https://www.gov.pl/web/nauka/komunikat-ministra-nauki-z-dnia-05-stycznia-2024-r-w-sprawie-wykazu-czasopism-naukowych-i-recenzowanych-materialow-z-konferencji-miedzynarodowych
- xlsx: https://www.gov.pl/attachment/c2510527-171a-451e-b3c4-74ea5a5c6c94
- List of lists: https://www.gov.pl/web/nauka/ujednolicony-wykaz-czasopism-naukowych

**A new list is coming.** On 02.06.2026 the Ministry announced that a new list will be published by the end
of 2026 and signed in early 2027 (for the 2026–2030 evaluation). Source:
https://www.gov.pl/web/nauka/nowy-termin-publikacji-wykazu-czasopism-naukowych

⚠️ The degree requirement (art. 186 ust. 1 pkt 3) counts the list **in the year of final publication**. A
paper published in 2027 will therefore probably be scored on the **new** list, so the points below may change.
Re-check them once the new list is out.

"ITiT" below means the discipline informatyka techniczna i telekomunikacja.

| Venue | Type | Points (list of 5.01.2024) | Assigned to ITiT | Notes |
|---|---|---|---|---|
| IEEE Robotics and Automation Letters (RA-L), ISSN 2377-3766 | journal | **200** | yes | |
| IEEE Transactions on Robotics (T-RO), 1552-3098 | journal | **200** | yes | |
| Robotics: Science and Systems (RSS) | conference | **200** | yes | listed as "Robotics: Systems and Science [RSS]", Lp. 1277 |
| Robotics and Autonomous Systems (Elsevier), 0921-8890 | journal | **140** | yes | |
| IEEE/RSJ IROS | conference | **140** | yes | Lp. 575 |
| Sensors (MDPI), 1424-8220 | journal | **100** | yes | not assigned to informatyka |
| IEEE ICRA | conference | **70** | yes | Lp. 1521 |
| CoRL (Conference on Robot Learning) | conference | **not on the list** | n/a | a CoRL paper alone does **not** satisfy the degree requirement |

Source for every row: the xlsx above. Values were read directly from the file.

### Upcoming deadlines relevant to semester 3 (Oct 2026 – Feb 2027)
- **IROS 2027**
  - Where and when: Florence, Italy, 26 Sep – 1 Oct 2027.
  - **Paper deadline 1 March 2027.**
  - Source: https://www.ieee-ras.org/event/call-for-papers-paper-submission-deadline-iros-2027-ieee-rsj-international-conference-on-intelligent-robots-and-systems-iros-27403-0/
- **ICRA 2027**
  - Where and when: Seoul, 24–28 May 2027.
  - Paper deadline 15–16 Sep 2026, **already closed**.
  - An RA-L paper can be transferred for presentation at ICRA 2027 until 31 Dec 2026.
  - Source: https://2027.ieee-icra.org/contribute/call-for-icra-2027-papers-now-accepting-submissions/
- **RA-L**
  - Rolling submission. Accepted papers can be transferred to a RAS conference within 270 days of acceptance.
  - Source: https://www.ieee-ras.org/publications/ra-l/
  - An RA-L paper can be presented at IROS; the exact RA-L+IROS 2027 window is **UNVERIFIED** (not yet
    published).
- **CoRL 2027:** location, dates and deadline are not announced, so **UNVERIFIED**. CoRL 2026 is in Austin, TX.
  Source: https://www.corl.org/

---

## 4. NCN PRELUDIUM

- **PRELUDIUM 25 (latest call, closed):**
  - Announced 16.03.2026, deadline 16.06.2026, results by Dec 2026.
  - **PI:** anyone without a PhD on the deadline day, once in a lifetime. The call does not exclude doctoral
    school students.
  - **Supervisor (opiekun naukowy):** mandatory, and cannot be paid from the project.
  - **Budget:** up to 70k / 140k / 210k PLN for 12 / 24 / 36 months.
  - **Team:** up to 3 people.
  - **Salaries:** PI + contractor capped at 2,000 PLN/month combined. NCN and doctoral stipends cannot be
    budgeted.
  - **Equipment:** up to 30% of the budget.
  - Source: https://ncn.gov.pl/ogloszenia/konkursy/preludium25
- **PRELUDIUM 26 / 2027 call:** **UNVERIFIED**, because the 2027 NCN schedule is not published yet. The 2026
  schedule was published on 12.12.2025. PRELUDIUM 24 ran 21.03–17.06.2025 and PRELUDIUM 25 ran 16.03–16.06.2026,
  so by pattern (inference, not an announcement) PRELUDIUM 26 would run about **mid-March to mid-June 2027**.
  That fits the semester 4 plan in §3.
  - https://www.ncn.gov.pl/finansowanie-nauki/konkursy/harmonogram
  - https://www.ncn.gov.pl/aktualnosci/2025-12-12-harmonogram-konkursow-ncn-2026
  - https://www.ncn.gov.pl/ogloszenia/konkursy/preludium24
- **ETIUDA:** discontinued; the last call was ETIUDA 8 in 2019. Source: https://www.ncn.gov.pl/konkursy-krajowe
- **PRELUDIUM BIS:** only doctoral schools can apply. The last call was edition 5 in 2023, and it is not in the
  2026 schedule. Source: https://www.ncn.gov.pl/ogloszenia/konkursy/preludiumbis5

---

## 5. Mobility funding

### NAWA
- **Bekker NAWA (call 2026)** is open to **doctoral school students**.
  - Deadline was 29.05.2026.
  - Stays must start 1.03–1.10.2027 and last 3–24 months.
  - Doctoral stipend 3,750 PLN/month plus a monthly allowance by country group (4,000–12,000 PLN) and a travel
    lump sum.
  - Page (confirms doctoral students can apply): https://nawa.gov.pl/naukowcy/program-imienia-bekkera/ogloszenie
  - Amounts and dates: https://nawa.gov.pl/images/Bekker/Bekker-2026/00-Ogloszenie-Bekker-2026.pdf
  - **Next call** (expected about spring 2027, for stays from 2028): **UNVERIFIED**. NAWA's 2026 action plan
    lists Bekker as a permanent programme: https://nawa.gov.pl/images/2026/Plan-dzialania/Plan_dzialania_NAWA_na_rok_2026.pdf
  - → Fits the §3 semester 6 foreign visit (Mar–Sep 2028) if you apply in the 2027 call.
- **Iwanowska Programme:** closed and replaced by Bekker for doctoral students. Source: https://nawa.gov.pl/en/scientists/the-iwanowska-programme
- **Walczak NAWA:** medical and health sciences only, so not applicable. Source: NAWA 2026 action plan (above).
- **STER NAWA:** only doctoral schools can apply. PWr's STER project "InterDocSchool" ended 31.12.2023. Whether
  PWr has a new STER project is **UNVERIFIED**. Source: https://szd.pwr.edu.pl/o-szkole/realizowane-projekty/nawa-ster

### Erasmus+ (PWr)
- **Short-term doctoral mobility:**
  - 5–30 days; for doctoral students the virtual component is optional.
  - 79 EUR/day for days 5–14, 56 EUR/day for days 15–30, plus travel.
  - Continuous recruitment through the faculty coordinator.
  - Source: https://crm.pwr.edu.pl/studenci/program-erasmus-plus/erasmus/wyjazdy-krotkoterminowe-erasmus
- **Traineeships:** open to doctoral students. Source: https://crm.pwr.edu.pl/studenci/program-erasmus-plus/erasmus/erasmus-plus-praktyki-i-staze
- **W4 coordinator:** erasmus_w4n@pwr.edu.pl. Source: https://wit.pwr.edu.pl/studenci/program-erasmus

### PWr internal
- **SzD Minigranty:**
  - Up to 20,000 PLN for doctoral students in years 2–4. Covers equipment, services, research trips,
    conferences and training.
  - The last call closed 20.01.2026.
  - The next edition (expected about Jan 2027) is **UNVERIFIED**.
  - Could fund sensors or a small platform, or IROS travel.
  - Source: https://szd.pwr.edu.pl/doktoranci/minigranty
- **Unite! research visits (SzD):** only for first-year students with a co-supervisor at a partner university,
  so this student is most likely no longer eligible. That is our reading of the rules. Source: https://szd.pwr.edu.pl/doktoranci/unite
- **PWr is not an IDUB research university.** Source: https://naukawpolsce.pl/aktualnosci/news,79243,resort-nauki-oglosil-liste-10-uczelni-badawczych.html

---

## 6. Open questions for the supervisor
1. Does K46 or the group have a mobile robot, RGB-D camera or LiDAR, or a budget to buy them? Otherwise, should
   we collaborate with K29 "Denali" (Pioneer 3-DX, Jaguar 4x4)?
2. Is there a group GPU server or CLARIN allocation, or should we apply for WCSS Lem and PLGrid "Doktorant"
   grants?
3. Is RA-L with the IROS 2027 option acceptable as the §11 target, with a Feb 2027 submission?

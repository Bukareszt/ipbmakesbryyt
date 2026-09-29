# Benchmark: IPB plans, doctoral topics and mid-term outcomes (PWr + other Polish doctoral schools)

Issue #1 · compiled 2026-09-26 · owner: Wave1-A worker

**Scope.** This file collects public evidence on how IPBs (research plans) are judged at the PWr Doctoral
School (SzD PWr), especially in the discipline *informatyka techniczna i telekomunikacja* (ITiT). It adds
comparable material from other Polish doctoral schools and ends with a numbered list of concrete edits
for `content/`.

**Method.** Official SzD PWr pages and PDFs were downloaded and their text extracted. All the published
mid-term results (2019–2024 cohorts) were read, with the ITiT sections read in full for the 2023 cohort
and keyword-scanned for the others. The ministerial list of 5 Jan 2024 was searched for robotics and ML
venues. A sub-agent covered the other schools. Page numbers refer to the PDF's own "Strona X z N" markers.

**Privacy.** The mid-term PDFs name students; SzD publishes them because § 14 ust. 11 of the Regulations
makes results and justifications public. Here, cases are cited **anonymously** (cohort, discipline,
page) because we only need the patterns.

**Main finding.** No full IPB by a PWr ITiT or K46 doctoral student is publicly available. Neither is a
full robotics IPB from any other Polish school. What *is* public, and more useful, is:
(a) the **mid-term evaluation form**, i.e. the exact criteria the IPB will be scored against;
(b) **five years of published committee justifications** for ITiT at PWr; and
(c) templates and guidance from PW, PG, PUT, PolSl, AGH, UJ and UAM.

---

## 1. Sources

### 1.1 SzD PWr: rules and forms

| # | Source | URL | What we took from it |
|---|---|---|---|
| S1 | IPB page | https://szd.pwr.edu.pl/doktoranci/indywidualny-plan-badawczy | Submit within 12 months. From sem. 3 the individual study plan (IPK) follows the IPB. Not submitting the dissertation by the IPB date means removal from the list (it can be extended by ≤ 2 years). |
| S2 | IPB FAQ | https://szd.pwr.edu.pl/faq/indywidualny-plan-badawczy | IPB = "important milestone". One change allowed, after the mid-term, "in justified cases". |
| S3 | **Regulations 2025** (in force from 1.10.2025), §§ 13–15 | https://szd.pwr.edu.pl/o-szkole/akty-prawne/regulamin-szkoly-doktorskiej → `regulamin_szkoly_doktorskiej_politechniki_wroclawskiej_2025.pdf` ([direct](https://szd.pwr.edu.pl/d/JGBUKOTtQKxVvAUdqREFBPF0WUXJ-XFxOSylDC0QHFm9PFQk5Eht1FRMSWHoFPFgHFkhCcH5bXldcOA/regulamin_szkoly_doktorskiej_politechniki_wroclawskiej_2025.pdf)) | § 13 ust. 2 pkt 1–11: the required content (matches the form). § 13 ust. 3: update only after the mid-term; the Dean decides after the discipline director's opinion. § 14 ust. 7: the evaluation is based on the IPB, the autoreferat, a 15-min presentation and a discussion. § 14 ust. 10: a split committee votes by simple majority; numeric criteria are averaged. § 14 ust. 11: results and justifications are public. § 14 ust. 14: appeal within 7 days. |
| S4 | **Procedure SzD/Pr18/2026 "Indywidualny plan badawczy"** (in force from 26.01.2026) | https://szd.pwr.edu.pl/o-szkole/akty-prawne/informacje-dziekana-szkoly-doktorskiej → `procedura_szd_18_indywidualny_plan_badawczy.pdf` | Point 3.4: the office checks **completeness incl. signatures of student and supervisor(s)**. Point 3.5: students who have **not filed by 30 September** get a reminder, and if they still don't file, **removal proceedings start**. |
| S5 | Winter 2026/27 duty schedule | https://szd.pwr.edu.pl/doktoranci/harmonogram-obowiazkow-doktoranta-w-semestrze-zimowym-2026-2027 | Cohort started 1.10.2025: **IPB due 30.09.2026**; semester report due 15.10.2026. Cohort started 1.10.2024: mid-term autoreferat due **13.10.2026** (so ours will be about mid-Oct 2027). |
| S6 | Mid-term page | https://szd.pwr.edu.pl/doktoranci/ocena-srodokresowa | 3-person committee (1 external), max 7 students per committee, supervisor excluded. |
| S7 | Mid-term FAQ | https://szd.pwr.edu.pl/faq/ocena-srodokresowa | Regular cohorts are evaluated in **November**. A negative result means **removal**; a positive one raises the stipend. |
| S8 | **Mid-term evaluation form** (PL `formularz_oceny_srodokresowej.docx`, EN `mid-term_evaluation_form.docx`) | https://szd.pwr.edu.pl/doktoranci/ocena-srodokresowa/dokumenty-do-pobrania | **8 scored criteria**, reproduced in §2.1 below. Any "NO" or score < 5 must be justified in writing. |
| S9 | **Autoreferat template** (`autoreferat_oceny_srodokresowej_mid-term_report.docx`) | same page as S8 | Scientific report of **max 5 pages** (11 pt): significance, goal + hypotheses, concept and plan, methodology, results, literature. **A table of every IPB task, "the same as in IRP", with % completion.** Discrepancies must be explained, but "are not a reason for an automatic negative evaluation". Papers are listed with DOI and **MEiN points**. **Achievements already shown at recruitment must not be listed.** |
| S10 | Committee minutes template (`protokol_komisji_oceny_srodokresowej.docx`) | same page as S8 | Confirms the inputs: IPB + autoreferat + 15-min talk + discussion. |
| S11 | Official IPB form `ipb.docx` | https://szd.pwr.edu.pl/doktoranci/indywidualny-plan-badawczy | The form's own §3 examples: sem. 1 "Literature review…", sem. 3 "Preparation of a scientific article for a journal / conference from the ministerial list", sem. 8 "Editing of the doctoral dissertation…". §4 recommended date for a 1.10.2025 start: **30.09.2029**. |
| S12 | PWr regulations on awarding degrees (Oct 2025 consolidated text), via the ITiT discipline council | https://rd-itt.pwr.edu.pl/dokumenty-i-procedury → `regulamin_nadawania_stopni_naukowych_tj_pazdziernik_2025.pdf` | Degree requirement: ≥ 1 article in a listed journal or listed international conference proceedings. The dissertation may be "zbiór opublikowanych i powiązanych tematycznie artykułów" (a set of published, thematically linked papers) with a short introduction. |
| S13 | ITiT discipline council: conditions for distinguishing dissertations (`warunki_wyrozniania_28_05_2025_aktualizacja_strona.pdf`) | https://rd-itt.pwr.edu.pl/dokumenty-i-procedury | Scanned PDF with no text layer; **contents UNVERIFIED**. Worth reading by hand if a distinction is a goal. |

### 1.2 SzD PWr: published mid-term results (with justifications)

Index page: https://szd.pwr.edu.pl/doktoranci/ocena-srodokresowa/wyniki-oceny-srodokresowej

| # | Cohort (start) | File | ITiT students | ITiT negatives | Negatives, all disciplines |
|---|---|---|---|---|---|
| R1 | 1.10.2019 | `szkola_doktorska_pwr_-_wyniki_oceny_srodokresowej.pdf` | 9 | 0 | 1 |
| R2 | 1.10.2020 | `wyniki_oceny_srodokresowej_1102020.pdf` | 22 | 0 | 0 |
| R3 | 1.10.2021 | `wyniki_oceny_srodokresowej_1102021.pdf` | 21 | 0 | 1 |
| R4 | 1.10.2022 | `wyniki_oceny_srodokresowej_1102022_.pdf` | 16 | 0 | 2 |
| R5 | **1.10.2023** (latest full cohort) | `wyniki_oceny_srodokresowej_1102023_aktualizacja.pdf` | 17 | 0 | 0 |

(The small February cohorts, 2020/2021/2022/2024, were also downloaded. They contain no ITiT negatives.)

Counts come from counting "Wynik oceny" in the ITiT section of each PDF. Across 2019–2023 there are
**85 ITiT evaluations and 0 negatives**, but many are "positive with reservations" (see §2.2). Negatives
happen in other disciplines, and their reasons are instructive (§2.3).

### 1.3 Ministerial list of venues (for §11 and §3)

| # | Source | URL |
|---|---|---|
| M1 | Komunikat Ministra Nauki z 5.01.2024 (list of journals and international conference proceedings); PDF/XLSX attachments | https://www.gov.pl/web/nauka/komunikat-ministra-nauki-z-dnia-05-stycznia-2024-r-w-sprawie-wykazu-czasopism-naukowych-i-recenzowanych-materialow-z-konferencji-miedzynarodowych |
| M2 | MNiSW list history: 5.01.2024 is the latest list | https://www.gov.pl/web/nauka/ujednolicony-wykaz-czasopism-naukowych |
| M3 | Forum Akademickie, 2.06.2026: the new list will be "opracowany i opublikowany do końca 2026 roku", with signature "na początku 2027 roku", applying from 2027 | https://forumakademickie.pl/kolejna-zmiana-terminu-wykaz-czasopism-do-konca-tego-roku/ |

Points extracted from the M1 PDF (list of 5.01.2024). All the venues below are assigned to the
discipline "informatyka techniczna i telekomunikacja":

| Venue | Points | Lp. in list | Note |
|---|---|---|---|
| IEEE Robotics and Automation Letters (RA-L) | **200** | 7928 | journal |
| IEEE Transactions on Robotics | 200 | 8010 | journal |
| International Journal of Robotics Research | 200 | 9325 | journal |
| Robotics and Autonomous Systems | 140 | 17973 | journal |
| Science Robotics | 20 (as extracted) | 18237 | **Looks like a text-extraction artefact; check the XLSX** |
| Robotics: Science and Systems (listed as "Robotics: Systems and Science [RSS]") | **200** | conf. 1277 | conference |
| IEEE/RSJ IROS | **140** | conf. 575 | conference |
| IEEE ICRA | **70** | conf. 1521 | conference. Surprisingly low, but that is what the list says |
| CVPR / ICCV / ECCV | 200 / 200 / 200 | conf. 417 / 442 / 331 | conference |
| NeurIPS / ICML / ICLR | 200 / 200 / 200 | conf. 87 / 847 / 1674 | conference |
| ACL | 200 | conf. 153 | Whether the **ACL SRW** (Student Research Workshop) volume counts as "ACL" is **UNVERIFIED** |
| **CoRL (Conference on Robot Learning)** | **not found** | — | Not present in the text of the 5.01.2024 list (searched "Robot Learning"/"CoRL"). **Treat CoRL as not listed** unless the 2027 list adds it |

**Caveat.** § 13 ust. 2 pkt 8 of the Regulations counts a venue if it was on the list **in the year the
article is published in final form**. A paper submitted in 2027 will almost certainly be judged against
the **new list signed in early 2027** (M3), and those point values are unknown (UNVERIFIED). Recheck in
Q1 2027.

### 1.4 Other Polish doctoral schools (compiled by the sub-agent; URLs as it reported them)

| # | School | URL | Key facts |
|---|---|---|---|
| O1 | Politechnika Warszawska: IPB procedure | https://sd.pw.edu.pl/Doktoranci/Nauka/Indywidualny-Plan-Badawczy-IPB/Procedura-przygotowania-Indywidualnego-Planu-Badawczego-wraz-z-aktualnymi-formularzami | Schedule over 8 semesters with "kamienie milowe" (milestones). The qualifying article should be filed "co najmniej rok przed terminem złożenia rozprawy" (at least a year before the dissertation deadline), ideally by the end of sem. 6. The new form's fields are UNVERIFIED (the download returned HTML). |
| O2 | PW: mid-term | https://sd.pw.edu.pl/Doktoranci/Nauka/Ocena-Srodokresowa | Autoreferat due 30 days before the end of sem. 4. Public part (talk + questions), then a closed verdict. |
| O3 | Politechnika Gdańska: IPB | https://pg.edu.pl/szkola-doktorska/ksztalcenie/indywidualny-plan-badawczy | Written in English. **Measurable milestones**, funding sources, and a "plan i harmonogram publikowania wyników badań" (publication plan and schedule). |
| O4 | PG: mid-term | https://pg.edu.pl/szkola-doktorska/ksztalcenie/ocena-srodokresowa | Report of 50,000–70,000 characters with 3 reviews. The dissertation's table of contents is required. |
| O5 | Politechnika Poznańska: IPB template 2024 | https://phdschool.put.poznan.pl/sites/default/files/SzD/do_pobrania/IPB%202024/Indywidualny_plan_badawczy_2024.docx | Explicit "Research hypothesis or a problem…" field. The **monthly** schedule gives each task "Criteria and expected outcomes of task completion" and a "Contribution (%)" to the dissertation. Separate tables for dissemination, internships, grants and conferences, plus a Gantt chart. |
| O6 | PUT: mid-term form 2026 | https://phdschool.put.poznan.pl/sites/default/files/SzD/ksztalcenie/OS2026/2_2026_Formularz%20Oceny%20%C5%9Ar%C3%B3dokresowej.pdf | YES/NO items: "Termin … jest realny" (the date is realistic), "Hipoteza lub problem badawczy została już sformułowana" (the hypothesis or problem is already formulated), results "możliwe do uzyskania w okresie kolejnych 2 lat" (achievable in the next 2 years). HIGH/MEDIUM/LOW for "Nowatorstwo wyników" (novelty of the results). |
| O7 | Politechnika Śląska: "IPBhowto" | https://www.polsl.pl/rjo15-sd/wp-content/uploads/sites/607/2026/05/IPBhowto-2.pdf | Name the research gap. The schedule need not be per semester, "The most important thing is to indicate what will be done for the mid-term evaluation". Planned outputs go in a per-year table (papers, talks, internships, patents, grants). |
| O8 | AGH: mid-term FAQ | https://sd.agh.edu.pl/ocena-srodokresowa/faq | Autoreferat ≤ 10 pages, starting with a task-status table. For changes to the plan: "Należy przedstawić różnice i wyjaśnić powód zmian" (show the differences and explain why). |
| O9 | AGH: 2024 briefing slides | https://sd.agh.edu.pl/home/sd/Ocena_Srodokresowa/Ocena-srodokresowa-prezentacja_2024.pdf | 4 criteria: progress and conformity with the IPB, how the research is conducted, degree of completion, timeliness and quality. |
| O10 | AGH: published results with justifications | https://sd.agh.edu.pl/ocena-srodokresowa/wyniki-oceny-srodokresowej (e.g. [2025](https://sd.agh.edu.pl/home/sd/Ocena_Srodokresowa/Wyniki_oceny_srodokresowej_2025_semestr_letni_2.pdf): 156 positive / 2 negative; [2023](https://sd.agh.edu.pl/home/sd/Ocena_Srodokresowa/SD_AGH_Ocena_srodokresowa_2023.pdf): 162 / 3) | Includes a deep-RL robotic-workstation case with virtual environments, and an event-camera perception for autonomous vehicles case (see §2.4). |
| O11 | UJ, Doctoral School of Exact and Natural Sciences: mid-term regulations 2024 | https://science.phd.uj.edu.pl/documents/142594442/156424211/PL_KD2024_06_Ocena_srodokresowa_REGULAMIN.pdf/4b443fb8-e436-4728-8e83-6e2cdbedbf12 | Evaluates "stopień realizacji zakładanych w planie celów, badań oraz terminowość" (how far planned goals and research were completed, and on time). The supervisor gives a separate written opinion. About a 20-minute talk. |
| O12 | UAM: discipline-level criteria | https://amu.edu.pl/__data/assets/pdf_file/0031/179095/KOsD_SNs.pdf | Physics: the IPB's **risk-analysis section is formally taken into account**. Negative only for "istotny brak postępów" (significant lack of progress). |

Not reached within the time box: Politechnika Łódzka, IPPT PAN, IPI PAN, IDEAS NCBR. **No public full
robotics / embodied-AI IPB was found at any school.**

### 1.5 PWr W4 / K46 context

- No list of K46 doctoral topics or IPBs was found publicly. The ITiT discipline council site
  (https://rd-itt.pwr.edu.pl/) has documents and meeting pages but no topic registry. The graduates page
  (https://szd.pwr.edu.pl/o-szkole/absolwenci2/rok-2023-2024) lists names only, with no titles. **K46 /
  Kajdanowicz-group IPBs: none public (UNVERIFIED whether any exist in open form).**
- The 2023 ITiT cohort (R5) includes W4-style ML topics: LLMs for Polish, LLMs with spatial context, and
  **3D scene reconstruction from 2D images with implicit neural representations and 3D Gaussian
  Splatting** (R5 p. 20–21: collaborations with UJ, UAM, IDEAS NCBR; NCN Opus/Sonata projects on 3D
  representations). That last one is the closest PWr ITiT precedent to our topic. Committees in this
  discipline are therefore used to 3DGS topics, and a **possible local collaborator group exists**.
  Supervisor/department attribution is UNVERIFIED.
- No PWr ITiT mid-term case on robot navigation or sim-to-real was found (keyword scan of R1–R5 for
  robot/nawigac/Gaussian/reinforcement). Robotics topics at PWr show up in *automatyka…* and *inżynieria
  mechaniczna*, e.g. R1 p. 29–30 (mobile robots with omnidirectional tracks) and R5 p. 46 (UAV
  autonomy). **Implication:** our IPB must argue its **ITiT** contribution (learning algorithms, software,
  data, evaluation methodology), not control or mechanical engineering.

---

## 2. Extracted patterns

### 2.1 What the IPB will be scored on (PWr mid-term form, S8)

The committee fills this in about 2 years after submission, with our IPB as the reference:

1. Degree of progress on the IPB during the period (1–5)
2. **Is the dissertation submission date in the IPB realistic?** (yes/no)
3. **Were the hypotheses or research problems properly formulated?** (yes/no)
4. How suitable are the chosen methods for the planned research and expected results? (1–5)
5. How relevant are the results so far to completing the dissertation? (1–5)
6. Quality of carrying out the IPB tasks (1–5)
7. How far are the results so far an **original contribution to the discipline**? (1–5)
8. **Are the IPB's planned tasks international** (international publications, joint initiatives with
   foreign institutions, foreign co-authors, **foreign internships**, international projects)? (yes/no)

Plus a justification of at least ½ page. Criteria 2, 3, 4 and 8 are judged **directly from the IPB
text**, so they must be visibly satisfied in `content/`.

### 2.2 Recurring remarks in PWr ITiT justifications (R1–R5; R5 read in full)

Keyword counts over the ITiT sections of 2019/20/21/22/23: "doprecyz-" (make more precise) 0/0/2/1/**10**;
"metodyk-" (methodology) 0/0/3/1/**8**; "termin" (deadline) 5/10/16/15/18; "opóźni-" (delay)
1/7/1/5/6; "międzynarod-" (international) 1/25/15/6/6; "publikac-" (publication) 10/33/24/11/20. The
recent trend is clear: **committees increasingly ask for more precise problems and methodology.**

1. **Main goal / original contribution not sharp enough.**
   - R5 p. 12: "…more clearly identifies the main achievements that will constitute his key original
     contribution".
   - R5 p. 12–13: the committee "nie uzyskała wystarczająco dobrego zrozumienia na czym ma polegać
     główne oryginalne osiągnięcie badawcze" (did not get a clear enough picture of what the main
     original achievement is) and suggested "zawężenie" (narrowing the scope).
2. **Too many sub-goals.** R5 p. 13–14: "Nie jest dla Komisji jasne, które z obszernej listy siedmiu
   celów cząstkowych zawartych w IPB zostały zrealizowane" (it is not clear which of the IPB's long list
   of seven sub-goals were achieved). The recommendation was to sharpen the main goal and possibly narrow
   the scope; the committee also said the IPB deadline was at risk.
3. **Methodology per stage** (a near-boilerplate recommendation, repeated for 4 students in R5
   p. 14–17): "przedstawić plan badań, w szczególności przedstawić etapy procedury badawczej … oraz
   przedstawić metody badawcze, które są wykorzystywane w poszczególnych etapach badawczych" (present the
   research plan, in particular the stages of the research procedure and the methods used in each stage).
4. **Measurable hypothesis.** R5 p. 16–17 (a "very weak positive"): "rekomenduje pilne zdefiniowanie
   mierzalnego problemu badawczego/hipotezy badawczej wraz z planem prac" (urgently define a measurable
   research problem or hypothesis, with a work plan).
5. **Publication quality targets.** R5 p. 17: "skupienie się na publikowaniu wyników w lepszych
   czasopismach (140p) i na lepszych konferencjach (A* i A)" (focus on better journals, 140 points, and
   better conferences, CORE A* and A).
6. **Too few publications** is flagged even in positive cases (R5 p. 17–18, p. 20–21). Unpublished but
   solid results are tolerated if the committee sees they are "podstawą do dobrych publikacji" (a basis
   for good papers) (R5 p. 13).
7. **Delays tolerated when explained.** R5 p. 19–20: small delays for personal reasons, and one planned
   paper "świadomie odłożona" (deliberately postponed), were not a big risk. R5 p. 21–22: a delay caused
   by a paper's model that could not be reproduced was accepted.
8. **Postponing experiments is a red flag.** R5 p. 22–23: "przełożenie badań eksperymentalnych na
   kolejne semestry" (moving experimental work to later semesters) "może … przyczynić się do opóźnienia"
   (may cause a delay). This matters for a real-robot topic.
9. **Split votes and "positive, but the date is at risk".** R5 p. 14 (2:1 vote) and p. 16: "nie rokuje
   złożenia rozprawy w planowanym terminie, jednak rokuje … po przedłużeniu" (unlikely to submit on the
   planned date, but likely after an extension).
10. **What gets praised.** Strong publications, international cooperation (a foreign internship, a
    foreign assistant supervisor, joint work with foreign labs), Preludium grants (R5 p. 19–20), project
    participation (NCN, Horizon), "jasno określony problem badawczy" (a clearly defined research problem)
    with precisely stated questions and hypotheses (R5 p. 16–17), and "precyzyjnie i jasno sformułowane plany
    i metody dalszych prac" (precisely and clearly stated plans and methods for further work).
11. **Simulation fidelity questioned** even outside robotics. R5 p. 17–18 (ITiT, blockchain simulation):
    "Powstaje problem jak precyzyjnie dostroić parametry symulacji, aby dokładniej odzwierciedlały
    rzeczywiste systemy" (the question is how to tune simulation parameters precisely enough to match
    real systems). Our §7/§9 should pre-empt exactly this question.

### 2.3 Why PWr negatives happened (other disciplines, R1/R3/R4)

- R1 p. 39–40: the planned literature-review tasks were done only "w niewielkim stopniu" (to a small
  extent). There were no conclusions from the review, the methodology "wymaga uszczegółowienia" (needs
  more detail), the thesis needed sharpening, method-testing tasks were not done, and publications were
  off-topic.
- R3 p. 48: the methodology was not clearly characterised, there was **no scheme of the test stand
  ("stanowiska badawczego")**, no results, the added value over existing methods was not argued, and
  terms in the title were unclear. The committee concluded the dissertation would likely miss the IPB
  date.
- R4 p. 15 (automatics discipline): the student **could not explain the details of their own model,
  parameters and methodology** during the discussion.
- R4 (civil engineering): the topic and supervisor changed but **the IPB was not updated**, so progress
  could not be matched to the plan.

### 2.4 Cross-school patterns (O1–O12)

- Committees **check the schedule task by task**. The PWr autoreferat (S9) copies the IPB tasks
  verbatim and asks for "% completion", as do the AGH (O8) and PUT (O5) templates. So **each §3 item
  becomes a row the committee will tick or not.**
- Tasks should have **completion criteria** (PUT O5, PG O3 "measurable milestones"). PolSl (O7) says
  the key is to show *what will be done by the mid-term*.
- **Publication plan:** name the venue type per semester (PG O3, PolSl O7). PW (O1) wants the qualifying
  article ≥ 1 year before submission.
- **Risk analysis** is valued (UAM O12; AGH O10 recommended "analizę ryzyk" (risk analysis) for
  externally built hardware in an autonomous-vehicle perception case).
- **Sim-vs-real validation is a known failure mode.** In an AGH 2023 case, "niezgodności wyników
  symulacji z wykonanymi pomiarami" (simulation results disagreeing with measurements) delayed a planned
  paper "ze względu na problem z walidacją" (because of the validation problem).
- **Off-topic papers** don't help (AGH 2025) and can hurt (PWr R1). Pre-PhD achievements don't count
  (PWr S9, AGH).
- Many parallel threads are criticised ("wielotorowe i nie zawsze spójne", many-tracked and not always
  coherent, AGH). Committees want "jednolity wynik naukowy" (a single unified scientific result).

### 2.5 Topic phrasing patterns

- PWr committees ask for titles that **name the application domain** (R5 p. 14: add that the research is
  in medical imaging) and that **define their key terms** (R3 p. 48: "kontrola", "energia liniowa").
- ITiT titles in R5 use the pattern **method + object + domain**, e.g. "3D scene models from 2D data
  using AI methods", or "LLMs for text processing grounded in spatial data".

### 2.6 Schedule granularity observed

- PWr form (S11): one row per semester (8 rows), free text.
- PUT (O5): monthly tasks with a % contribution each, plus a quarterly Gantt chart.
- PolSl (O7): semester or freer, plus a yearly output table.
- **Practical consensus:** keep 8 semester rows (the PWr form requires it), but inside each row use
  **2–4 numbered tasks with a deliverable each**, and put a compact **planned-outputs table** in §12.

---

## 3. Recommended edits to `content/` (numbered, concrete)

> Priority: **P0** = before submission (deadline 30.09.2026), **P1** = strongly recommended,
> **P2** = nice to have. Each item names the file and the evidence behind it.

1. **P0 · process (README/SPEC, all).** The hard deadline for the 1.10.2025 cohort is **30.09.2026** (S5).
   Procedure Pr18 (S4, point 3.5) starts removal proceedings if the IPB is still not filed after a
   reminder. The office checks **signatures of student and supervisor** (S4, point 3.4). As of today
   (26.09.2026) that leaves **4 days**. Get the signatures now, and file on paper plus upload to
   raporty.szd.pwr.edu.pl.
2. **P0 · `03-schedule.md`, sem. 1–2.** Replace the planned wording with **what was actually done** in
   Oct 2025 – Sep 2026 (there is already a TODO). The IPB is submitted at month 12, and the autoreferat
   will list these exact rows with "% completion" (S9). Claiming undone work (e.g. "robot set up, 2–3
   scenes captured, baseline gap measured") would show up as a discrepancy at the mid-term. If the
   hardware isn't ready, say so and move it to sem. 3.
3. **P0 · `11-publication-date.md` + `03-schedule.md` sem. 3.** Change the target to **IEEE RA-L (200 pts)**,
   optionally with IROS 2027 presentation, or **IROS 2027 (140 pts)** as a fallback. Both are listed for
   ITiT (M1). Keep "March 2027" only if the paper is realistic by then (the IROS 2027 deadline is
   UNVERIFIED). Add a note that the list signed in early 2027 applies (M3), and recheck points in Q1 2027.
4. **P1 · `03-schedule.md` sem. 6 and `09`/`12`.** Remove or requalify **"ICRA / CoRL" as scoring
   targets**. ICRA is only **70 pts** and **CoRL was not found** on the 5.01.2024 list (M1). Prefer
   **RSS (200)**, **CVPR/ICCV/ECCV (200)** for the reconstruction part, **RA-L (200)**, or **RAS (140)**
   for the journal paper in sem. 5/7. This matches the ITiT committee advice to target 140-pt journals and
   A*/A conferences (§2.2 item 5).
5. **P1 · `03-schedule.md`.** Inside each semester, **number the tasks** (T3.1, T3.2…) and give each a
   **verifiable deliverable** and the **H/RQ it serves**. Mark the place (K46 lab; partner lab). The rows
   are copied verbatim into the autoreferat % table (S9), and PG/PUT require measurable milestones
   (O3, O5). Keep it to **≤ 3 tasks per semester** so that each can reach 100%.
6. **P1 · `03-schedule.md` sem. 3–4.** Put **at least one real-robot experiment before the mid-term**,
   e.g. a first real deployment of a policy trained on a reconstruction, even in one scene. Committees
   penalise postponing experiments (R5 p. 22–23) and missing test stands (R3 p. 48). Everything for H1 in
   one environment should be finished by the end of sem. 4.
7. **P1 · `07-questions-hypotheses.md`.** Add **one overarching thesis sentence** ("teza"). Make every
   hypothesis **operational**: metric, comparison and decision rule. For example, for H1: "success rate on
   N fixed start–goal pairs × K trials, reconstruction-trained vs. generic-sim-trained, one-sided test
   α = 0.05". Define "comparable" in H1 as a **non-inferiority margin** (e.g. ≤ X pp). Replace the HTML
   TODO "thresholds after the Semester 2 baseline" with either the numbers or the rule for fixing them.
   This targets form criterion 3 (§2.1) and the "mierzalna hipoteza" remark (R5 p. 16–17).
8. **P1 · `07` + `08`.** **Mark the core contribution.** Four RQs, four hypotheses and five
   contributions is the "long list of sub-goals" that drew criticism (R5 p. 12–14). State explicitly
   that **RQ1–RQ2/H1+H4 (the real-data-budget study) is the core** that the dissertation stands on, and
   that RQ3 and RQ4 are extensions. Add a line to §8: "The key original contribution is …".
9. **P1 · `09-methods.md`.** **Restructure by stage** (Stage I–IV, matching §3). For each stage give
   method → data/equipment → metric → success criterion. This is the exact template ITiT committees asked
   for four times in R5 ("etapy procedury badawczej … metody w poszczególnych etapach", stages of the
   research procedure and the methods in each).
10. **P1 · `09-methods.md`.** Resolve the **robot platform TODO**: name the platform, its sensors, and
    where it is (K46 or shared), or state the fallback (e.g. a public real-world dataset plus a borrowed
    robot). A missing test stand appears in a negative justification (R3 p. 48).
11. **P1 · `09` + `07` H3.** Add an explicit **sim-to-real validation protocol**: paired sim/real
    rollouts, SRCC, and reconstruction-fidelity metrics. Add a **fallback if validation fails**. This is
    the sim-vs-measurement failure mode seen at AGH (§2.4), and the committee's "how do you tune the
    simulator to reality" question (R5 p. 17–18).
12. **P1 · `03-schedule.md` + `12-other.md` (international, criterion 8).** Keep the sem. 6 foreign visit,
    but make it **concrete**: a candidate host lab, 1–3 months, planned funding (NAWA/Erasmus+/PWr, all to
    be confirmed). Add a lighter international item **before the mid-term**, e.g. an international summer
    school with a poster in sem. 3/4 or a foreign co-author on the RA-L/IROS paper. Form criterion 8 asks
    this directly, and it is the most-praised item in ITiT justifications (R2–R5).
13. **P1 · `12-other.md`.** Add a compact **planned-outputs table** by year: papers (venue, points on the
    2024 list), conference talks, grants (NCN Preludium sem. 4; **SzD PWr Minigranty**,
    https://szd.pwr.edu.pl/doktoranci/minigranty, as an early internal option), and mobility. This follows
    PolSl/PUT (O5, O7) and makes the autoreferat easy to write.
14. **P1 · `12-other.md` risks.** Extend the risk list with (a) **delays in hardware or lab access**,
    (b) **sim-to-real validation failure** (see edit 11), and (c) **dependence on external robots or
    partners**, each with a mitigation and the semester it could affect. Risk sections are formally used
    at UAM (O12) and recommended by AGH committees (O10).
15. **P1 · `05-justification.md` / `12-other.md` prior work.** The ACL 2025 SRW paper is **pre-PhD** and
    in **NLP**. The autoreferat forbids listing recruitment-stage achievements (S9), and off-topic papers
    are criticised (R1, AGH). Keep it only as methodological background (as §12 does now). In §5, soften
    or drop "continues my earlier work" so the topic stands on its own. Whether ACL SRW counts as "ACL"
    (200 pts) for art. 186 is UNVERIFIED, so ask the supervisor.
16. **P1 · `08-contribution.md` (discipline fit).** Frame the contributions **in ITiT terms**: learning
    algorithms, data-efficient training methodology, software pipeline, datasets and benchmarks,
    evaluation methodology. PWr robotics topics usually sit in *automatyka…* or *inżynieria mechaniczna*
    (§1.5), and one committee noted papers published in venues outside the discipline (R5 p. 46). Prefer
    venues whose list entry includes ITiT (RA-L, RAS, IROS and RSS all do; M1).
17. **P2 · `02-topic.md`.** Make the object explicit ("**mobile robots**") and name the core technique,
    for example: EN "Data-efficient sim-to-real transfer of mobile-robot navigation policies using
    real-to-sim-to-real neural scene reconstruction"; PL "Efektywne pod względem danych przenoszenie
    polityk nawigacji robotów mobilnych z symulacji do rzeczywistości z wykorzystaniem neuronowej
    rekonstrukcji scen (real-to-sim-to-real)". Committees ask titles to name the domain and define their
    terms (R5 p. 14, R3 p. 48). This is optional, since the topic "nie musi stanowić ostatecznego
    tytułu" (does not have to be the final title) (S11).
18. **P2 · `03-schedule.md` sem. 4.** Add "**prepare the mid-term autoreferat (≤ 5 pages) and 15-min
    presentation; deadline ~mid-Oct 2027**". By analogy with S5 (the previous cohort's deadline is
    13.10.2026), the exact date is UNVERIFIED. Sem. 5 then shows "mid-term evaluation (Nov 2027, S7)".
19. **P2 · `13-cooperation.md`.** Add "the monthly summary tracks each IPB task's % completion", which
    mirrors the autoreferat table (S9). Also add "supervisor co-signs the annual report and the mid-term
    autoreferat" (the autoreferat has a supervisor-signature field, S9).
20. **P2 · `06-state-of-the-art.md` / `12-other.md`.** Consider naming possible **PWr-internal
    collaboration** with the W4 group that works on 3DGS/implicit neural scene representations (R5
    p. 20–21), and the existing NCN Opus/Sonata 3D-representation projects mentioned there. Committees
    reward collaboration, and it reduces the risk around reconstruction quality. **Verify group and
    supervisor names before writing them in.**
21. **P2 · `04-submission-date.md`.** Keep **30.09.2029**, the form's recommended value (S11). Form
    criterion 2 ("is the date realistic") is where split votes happen (R5 p. 14, p. 16). The best
    safeguard is edits 2, 5 and 6 (an honest, checkable sem. 1–4), not an earlier date.
22. **P2 · SPEC.md §5 (for the coordinator; not owned here).** Update: the evaluation takes place in
    **November** for regular cohorts (S7); a negative result means **removal** (S7); and the committee
    scores the **8 criteria** in §2.1 (S8). Link this file from SPEC.

---

## 4. Open items / UNVERIFIED

- Whether ACL SRW 2025 proceedings count as the listed "ACL" (200 pts) for art. 186 ust. 1 pkt 3.
- Point values on the **new list (signed early 2027)** for RA-L, IROS, ICRA, RSS and CoRL.
- The **Science Robotics = 20 pts** reading from the 5.01.2024 PDF (probably an extraction artefact;
  check the XLSX).
- The IROS 2027 submission deadline (assumed ~March 2027 in the draft).
- Contents of the ITiT "warunki wyróżniania" (conditions for distinguishing dissertations) PDF (S13 is
  scanned).
- Supervisor and department attribution of the 2023-cohort 3DGS topic (R5 p. 20–21).
- The exact mid-term autoreferat deadline for the 1.10.2025 cohort (expected ~mid-Oct 2027).

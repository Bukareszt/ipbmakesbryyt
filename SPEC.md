# SPEC — Individual Research Plan (IPB), PWr Doctoral School

Source of truth: the official form [`ipb.docx`](ipb.docx), the page
https://szd.pwr.edu.pl/doktoranci/indywidualny-plan-badawczy, the FAQ, and **§ 13 of the Doctoral School
Regulations**. This spec lists what each section must contain and how we'll check it before submission.

Conventions:
- **MUST** = required by the form or the regulations. **SHOULD** = our best practice.
- Free-text sections: **11 pt, line spacing 1**. The page limits below are hard limits.
- `{…}` = input we still need from the doctoral student or supervisor.

---

## 1. Inputs to collect

| Input | Notes |
|---|---|
| `{full_name}` | |
| `{discipline}` | Pick from the form's dropdown (discipline of education) |
| `{faculty}` | Dropdown (e.g. W4N, W8…) |
| `{department}` | Katedra |
| `{start_date}` | Date the doctoral training started. It drives every deadline |
| `{orcid}` | Format `0000-0000-0000-0000` |
| `{supervisors}` | Name, degree, and affiliation (**required if outside PWr**). One or two |
| `{assistant_supervisor}` | Optional. If appointed, their opinion is required |
| `{topic}` | Working topic, agreed with the supervisor |
| `{target_venues}` | Journals/conferences on the ministerial list for the discipline |
| Research idea notes, key references, methods, planned mobility/grants | Raw material for sections 5–9, 12 |

Derived:
- `ipb_deadline = start_date + 12 months` (e.g. 1.10.2025 → 30.09.2026)
- `dissertation_deadline = start_date + 4 years − 1 day` (e.g. → 30.09.2029)
- `midterm = beginning of semester 5` (the September/October after year 2)

---

## 2. Section requirements

### §1 Basic data (Podstawowe dane)
- MUST: name, discipline, faculty, department, start date, ORCID, supervisor(s), and assistant supervisor
  (or "—").
- MUST: the affiliation of any supervisor from outside PWr.

### §2 Dissertation topic (Temat rozprawy)
- MUST: a proposed topic. It doesn't have to be the final title.
- SHOULD: one sentence, specific about the object and method, consistent with the discipline.

### §3 Schedule (Harmonogram) — table, semesters 1–8
- MUST: one entry for each of **semesters 1–8** with a short task description.
- MUST: research **stages and locations**, and the **completion dates of sub-studies** (by semester) and
  of the analysis of their results.
- SHOULD include the relevant items from the official list:
  - research execution (setup/test stand, materials, measurements/experiments, analysis of results)
  - preparing and submitting a scientific article
  - patent application
  - industry implementation proposal
  - conferences / workshops / summer-winter schools with presentation of results
  - grant application
  - domestic/foreign mobility (consultations, study visits)
- SHOULD: every entry has at least one **verifiable output**.
- SHOULD: semester 1 = literature review / state of the art. Semester 8 = writing and final version of the
  dissertation (as in the template examples).
- MUST (consistency): contains the article submission from §11. Its end is ≤ §4.

### §4 Dissertation submission date
- MUST: ≤ the end of semester 8.
- SHOULD: use the recommended value, `dissertation_deadline` (the last day of the 4-year period).

### §5 Justification of the topic — max 1 page
- MUST: why this topic, and the **potential application areas** of the results.

### §6 State of the art — max 2 pages
- MUST: a literature review with references to the most important works.
- SHOULD: end with an explicit **research gap** statement. Use a consistent citation style.

### §7 Research questions & hypotheses — max 1 page
- MUST: the main research questions and hypotheses.
- SHOULD: number them (RQ1…, H1…) so §9 and §3 can refer to them. Each hypothesis should be testable.

### §8 Contribution to the discipline — max 1 page
- MUST: the expected contribution to the **discipline in which the dissertation is carried out**.
- SHOULD: map each contribution to an RQ/H.

### §9 Research methods — max 2 pages
- MUST: a short description of the methods.
- SHOULD: for each RQ/H, give the method, data/materials, tools/equipment, and validation/evaluation
  metrics.

### §10 Popular-science abstract — max 1 page each
- MUST: **both Polish and English**, and the **two versions must say the same thing**.
- MUST: written for the general public. Cover the goal, the planned research, why this topic, and the
  main expected results.

### §11 Article/monograph submission date
- MUST: the date by which at least one qualifying work is submitted for review/print:
  - an article in a journal **or** peer-reviewed international conference proceedings that is on the
    **ministerial list** in the year of final publication (art. 267 ust. 2 pkt 2 lit. b), **or**
  - a monograph from a publisher on the ministerial list (art. 267 ust. 2 pkt 2 lit. a).
  - This meets art. 186 ust. 1 pkt 3 of the Act (a degree requirement).
- Format: month and year (e.g. "October 2026").
- SHOULD: in semesters 3–6, leaving time for review before §4.

### §12 Other — max 1 page
- Optional: extra comments, risks and mitigations, collaborations, a summary.

### §13 Cooperation with the supervisor
- MUST: the planned form of cooperation: meeting frequency, format, scope, and communication channel.

### §14 Assistant supervisor's opinion
- MUST if an assistant supervisor is appointed: a written opinion and signature. Otherwise mark "n/a".

### §15 Signatures
- MUST: date, doctoral student signature, supervisor signature, and the second supervisor's signature if
  there is one.

---

## 3. Submission

| Step | Channel |
|---|---|
| Paper original, signed | Doctoral School Dean's office (Dziekanat SzD) |
| Electronic version | https://raporty.szd.pwr.edu.pl/ (signed scan + unsigned PDF recommended) |
| Deadline | `ipb_deadline` (12 months from `start_date`) |
| Late submission | Grounds for removal from the doctoral student list |

Changes after submission: only **after the mid-term evaluation**, in justified cases, with the
supervisor's agreement. The **Dean** approves after consulting the discipline director (§ 13 ust. 3).

---

## 4. Acceptance checklist (run before printing)

- [ ] All 15 sections are filled (or explicitly "n/a" for §14 when there's no assistant supervisor)
- [ ] §1 ORCID is valid, and external supervisors have their affiliation
- [ ] §3 has an entry for each of semesters 1–8, each with a concrete output
- [ ] §3 names research locations and sub-study completion semesters
- [ ] §4 ≤ end of semester 8 (recommended: `dissertation_deadline`)
- [ ] §11 date appears as a task in §3 and falls before §4
- [ ] Target venue(s) for §11 are on the current ministerial list for the discipline
- [ ] Every hypothesis in §7 has a method in §9 and a task in §3
- [ ] §8 contributions trace back to §7
- [ ] §10 PL and EN versions have the same content
- [ ] Page limits are met at 11 pt / spacing 1 (§5, 7, 8, 10, 12: 1 page; §6, 9: 2 pages)
- [ ] Supervisor(s) reviewed and approved the content
- [ ] Assistant supervisor's opinion is attached (if applicable)
- [ ] Signed, and submitted on paper and in raporty.szd.pwr.edu.pl before `ipb_deadline`
- [ ] Final PDF archived as the baseline for the mid-term autoreferat

---

## 5. Link to the mid-term evaluation (for planning)

At the start of semester 5, the student submits the IPB, a written **autoreferat** on IPB progress, and a
**15-minute presentation**. The committee has 3 members from the discipline, one of them external, and
no supervisors. The result is positive or negative, and after a negative result the student can request
a re-evaluation within 7 days. Write §3 so that the semester 1–4 outputs can be shown clearly at this
review.

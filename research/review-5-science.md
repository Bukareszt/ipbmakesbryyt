# Review-5: is this a scientific dissertation, not an implementation ("wdrożeniowy") one? (2026-09-26)

## Criteria
- **Ustawa PSWiN art. 187 ust. 1.** A doctoral dissertation must present the candidate's general theoretical
  knowledge in the discipline and an **original solution to a scientific problem**.
- **Art. 206 (doktorat wdrożeniowy).** An implementation doctorate is carried out with an employer, and its
  dissertation solves a practical problem for that employer. This IPB is not that type, but the text must
  not *read* like it.
- **ITiT committee remarks** (research/benchmarks.md §2.2): state the main goal and original contribution
  sharply; give a clear methodology.

## Implementation signals found in v7 (before the fix)
1. **The goal was "a method that reduces data".** That is a tool or system goal, with no scientific problem
   stated.
2. **Hypotheses compared systems.** All of them had the form "A beats B by X".
3. **No general principle.** The three mechanisms were independent tricks.
4. **No theoretical component.** There was nothing about *why* or *when* twin data can replace real data.
5. **The contribution was framed as "the first method + the first measurement".** It read like engineering
   plus benchmarking.
6. **The title named the method and its applications, not the research question.**

## Fixes applied (coordinator)
- **§2 title.** Now names the scientific object: *the value of real data* in real-to-sim-to-real learning. The
  method comes second.
- **§7.**
  - New **Scientific problem**: learning under distribution shift in which target-domain data can be bought
    at a cost; allocating it across the loop is sequential experimental design [36, 37].
  - New **Principle and theoretical claim**: value each real datum by its expected reduction of the
    twin-to-reality gap per unit cost; a task-weighted, domain-adaptation-style bound [38] says when twin
    data can replace real data.
  - The three mechanisms are now **instances of one criterion**.
  - RQ4 is now "When and why can twin data replace real data?"
  - H4 adds a **falsifiable theoretical prediction**: savings grow with the twin-to-reality correlation and
    with how concentrated the gap is.
- **§8.** The key contribution is (i) formulation + criterion + bound, (ii) the method instantiating it,
  (iii) empirical knowledge of when and why savings arise. "What is new is not the twin but the principled
  spending of real data."
- **§5.** A "Scientific problem and goal" paragraph.
- **§6.** New "Theory" paragraph plus 3 references, verified via Crossref on 2026-09-26:
  - [36] Chaloner & Verdinelli 1995, doi:10.1214/ss/1177009939
  - [37] Rainforth et al. 2024, doi:10.1214/23-STS915
  - [38] Ben-David et al. 2010, doi:10.1007/s10994-009-5152-4

  The gap statement now asks for a principled criterion, its theory, and a method built on it.
- **§9.** New "Theoretical part" paragraph: posterior over twin and gap, bound, acquisition criterion, and
  predictions tested against the curves.
- **§10.** One sentence per language on the scientific question (identical content).
- **Page limits.** All pass (build report); §6 and §9 are at 1.97 and 2.00 estimated pages, so check them in
  Word.

## Remaining risk
- **The theory must be delivered.** At minimum: the formal model, a bound under stated assumptions, and a
  test of its predictions. This is what makes the dissertation scientific. The supervisor should confirm
  the ambition level.
- **Venues.** NeurIPS and ICML value exactly this: a principled criterion with analysis plus experiments.

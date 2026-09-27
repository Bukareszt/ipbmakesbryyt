# Citation audit of §6 (with §7 and §9 cross-check), done 2026-09-27

Scope: the visible text of content/06-state-of-the-art.md (23 references), plus content/07-questions-hypotheses.md and content/09-methods.md.
Metadata was checked against the arXiv API and abstract pages, Crossref, OpenAlex, PMLR proceedings pages and the OpenReview API. DBLP was not usable because it returned a bot-check page, and the arXiv API throttled some queries, so those were re-fetched from the arxiv.org/abs pages.

## Metadata: are authors, year, title and venue correct for each of [1]-[23]?

### Takeaway
21 of 23 entries are correct as written. Two 2026 preprints now have venues and should be updated: [13] TwinRL was accepted at ACM MM 2026 under the title "TwinRL-VLA", and [17] Jin et al. is published in ECCV 2026 (LNCS). [9] and [18] are still arXiv-only. The only other issues are cosmetic: [9], [17] and [18] use title case while the rest use sentence case.

### Cited Findings (one row per reference)

| # | Verified metadata | Source | Status / fix |
|---|---|---|---|
| 1 | Kadian, A., Truong, J., Gokaslan, A., ... (9 authors). "Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?" IEEE RA-L 5(4):6670-6677, Oct 2020. DOI 10.1109/LRA.2020.3013848; arXiv 1912.06321 | [Crossref](https://api.crossref.org/works/10.1109/lra.2020.3013848), [arXiv](https://arxiv.org/abs/1912.06321) | OK |
| 2 | Ben-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., Vaughan, J. W. "A theory of learning from different domains." Machine Learning 79(1-2):151-175. Online 23 Oct 2009, issue 2010 | [Crossref](https://api.crossref.org/works/10.1007/s10994-009-5152-4) | OK. The issue year 2010 is the standard citation year. |
| 3 | Tobin, J., Fong, R., Ray, A., ... (6 authors). IROS 2017. DOI 10.1109/IROS.2017.8202133; arXiv 1703.06907 | [arXiv](https://arxiv.org/abs/1703.06907), [OpenAlex](https://api.openalex.org/works?search=Domain%20randomization%20for%20transferring%20deep%20neural%20networks) | OK |
| 4 | Chebotar, Y., Handa, A., Makoviychuk, V., ... (7 authors). ICRA 2019. DOI 10.1109/ICRA.2019.8793789; arXiv 1810.05687 | [arXiv](https://arxiv.org/abs/1810.05687) | OK |
| 5 | Tiboni, G., Klink, P., Peters, J., ... (6 authors). "Domain Randomization via Entropy Maximization." ICLR 2024 (the arXiv comment says "Published as a conference paper at ICLR 2024"); arXiv 2311.01885 | [arXiv](https://arxiv.org/abs/2311.01885) | OK |
| 6 | Ganin, Y., Ustinova, E., Ajakan, H., ... (8 authors). JMLR 17(59):1-35, 2016; arXiv 1505.07818 | [arXiv](https://arxiv.org/abs/1505.07818) | OK |
| 7 | Cheng, S., Ma, L., Chen, Z., Mandlekar, A., Garrett, C., Xu, D. NeurIPS 38 (2025), pp. 13271-13299. DOI 10.52202/085713-0399; arXiv 2509.18631 | [Crossref](https://api.crossref.org/works/10.52202/085713-0399) | OK |
| 8 | Zhao, H., Tachet des Combes, R., Zhang, K., Gordon, G. "On Learning Invariant Representations for Domain Adaptation." ICML 2019, PMLR 97:7523-7532 | [PMLR v97](https://proceedings.mlr.press/v97/) | OK. The PMLR title uses the plural "Representations", as the reference does; arXiv v2 uses the singular. |
| 9 | Lei, Y., Liu, M., Maddukuri, A., ... (5 authors). arXiv:2604.13645, v1 of 15 Apr 2026 | [arXiv](https://arxiv.org/abs/2604.13645), [project page](https://science-of-co-training.github.io/) | Exists. No venue announced on arXiv, the project page or Crossref. Only fix: sentence case. |
| 10 | Kerbl, B., Kopanas, G., Leimkühler, T., Drettakis, G. ACM TOG 42(4), July 2023. DOI 10.1145/3592433 | [Crossref](https://api.crossref.org/works/10.1145/3592433) | OK |
| 11 | Torne (Villasevil), M., Simeonov, A., Li, Z., ... (7 authors). RSS XX, 2024. DOI 10.15607/RSS.2024.XX.015 | [Crossref](https://api.crossref.org/works/10.15607/rss.2024.xx.015) | OK |
| 12 | Qureshi, M. N., Garg, S., Yandun, F., ... (6 authors). ICRA 2025. DOI 10.1109/ICRA55743.2025.11128339; arXiv 2409.10161 | [arXiv](https://arxiv.org/abs/2409.10161), [OpenAlex](https://api.openalex.org/works?search=SplatSim) | OK |
| 13 | Xu, Q., Liu, J., Zhou, R., ... (14 authors). arXiv:2602.09023 (v4). The repository README says "2026-07: TwinRL-VLA is accepted to ACM MM 2026", and uses the title "TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation" | [arXiv](https://arxiv.org/abs/2602.09023), [GitHub](https://github.com/zhourui9813/TwinRL) | UPDATE: the venue is now ACM MM 2026. No ACM DL/Crossref record exists yet, so keep the arXiv id as well. |
| 14 | Li, X., Hsu, K., Gu, J., ... (16 authors). "Evaluating Real-World Robot Manipulation Policies in Simulation." CoRL 2024, PMLR 270:3705-3728 | [PMLR v270](https://proceedings.mlr.press/v270/) | OK |
| 15 | Chhablani, G., Ye, X., Irshad, M. Z., Kira, Z. (4 authors). ICCV 2025. DOI 10.1109/ICCV51701.2025.02359; arXiv 2509.17430 ("paper accepted at ICCV, 2025") | [arXiv](https://arxiv.org/abs/2509.17430) | OK |
| 16 | Xie, Z., Liu, Z., Peng, Z., ... (5 authors). CVPR 2025. DOI 10.1109/CVPR52734.2025.00155; arXiv 2501.06693 | [arXiv](https://arxiv.org/abs/2501.06693) | OK |
| 17 | Jin, R., Zhu, Z., Ouyang, R., Xu, ..., Yue, ..., Wu, ..., Liu, ... (7 authors). Computer Vision - ECCV 2026, LNCS, pp. 20-37. DOI 10.1007/978-3-032-37602-2_2. arXiv v1 was titled "...in Dexterous Manipulation..."; v2 (29 Jun 2026) and the ECCV version use "...in Robotic Manipulation..." | [Crossref](https://api.crossref.org/works/10.1007/978-3-032-37602-2_2), [Springer](https://link.springer.com/chapter/10.1007/978-3-032-37602-2_2), [arXiv](https://arxiv.org/abs/2603.22876) | UPDATE: the venue is ECCV 2026. The title is correct for v2 and ECCV. |
| 18 | Qian, Y., Luo, J., Zhu, W., ... (7 authors). arXiv:2608.29516, v1 of 30 Aug 2026 | [arXiv](https://arxiv.org/abs/2608.29516) | Exists. No venue found. Only fix: sentence case. |
| 19 | Kachaev, N., Kolosov, M., Zelezetsky, D., Kovalev, ..., Panov, ... (5 authors). Proc. 25th Int. Conf. on Autonomous Agents and Multiagent Systems (AAMAS 2026). DOI 10.65109/PPER9186; arXiv 2510.25616 | [Crossref](https://api.crossref.org/works/10.65109/pper9186) | OK |
| 20 | Lee, Y., Chen, A. S., Tajwar, F., ... (7 authors). ICLR 2023 (the arXiv comment says "ICLR 2023"); arXiv 2210.11466 | [arXiv](https://arxiv.org/abs/2210.11466) | OK |
| 21 | Maddukuri, A., Jiang, Z., Chen, L. Y., ... (15 authors). RSS XXI, 2025. DOI 10.15607/RSS.2025.XXI.109 | [OpenAlex](https://api.openalex.org/works?search=Sim-and-real%20co-training%20simple%20recipe) | OK |
| 22 | Memmel, M., Wagenmaker, A., Zhu, C., ... (6 authors). ICLR 2024 (oral) per OpenReview; arXiv 2404.12308 | [OpenReview API](https://api2.openreview.net/notes/search?term=ASID%20Active%20Exploration%20System%20Identification&limit=5) | OK |
| 23 | Xie, A., Lee, L., Xiao, T., Finn, C. (4 authors). ICRA 2024. DOI 10.1109/ICRA57147.2024.10611331; arXiv 2307.03659 | [OpenAlex](https://api.openalex.org/works?search=Decomposing%20the%20generalization%20gap%20imitation%20learning) | OK |

- Every entry's first author and "et al." are correct. Every entry has at least 4 authors, so "et al." is never hiding a 2- or 3-author paper where it would look odd. — sources as in the table.
- The conference and journal names RA-L, IROS, ICRA, ICLR, JMLR, NeurIPS, ICML, ACM TOG, RSS, CoRL, ICCV, CVPR and AAMAS all match the verified records. — sources as in the table.

### Inferences
- The title given for [13] in the camera-ready ACM MM version is probably "TwinRL-VLA: ...", because the repository uses it. arXiv still says "TwinRL: ...". Either form is defensible. Citing the ACM MM venue together with the arXiv id is the safest choice.

### Gaps
- There is no ACM Digital Library record yet for [13] at ACM MM 2026, so its final title and pages are unconfirmed.
- DBLP could not be queried because of its bot check. Venues were confirmed through Crossref, PMLR, OpenReview and the arXiv comments instead.

## In-text claims: is each sentence citing [n] or naming a work accurate?

### Takeaway
Most claims are accurate. Four are slightly overstated: [12] "without real data", [14] credits visual matching alone, [15] "trained", and [8] leaves out its condition. One uncited theoretical claim repeated in §6 and §7 is overstated: that invariance "cannot reduce" the joint error, and that the joint error shrinks "only" as the simulation improves. No claim is inaccurate.

### Cited Findings

| # | Claim in the plan | Evidence (abstract/text) | Verdict | Suggested wording |
|---|---|---|---|---|
| 1 | "performance in simulation can poorly predict real-world performance unless the simulator is carefully tuned [1]" | Sim-vs-real correlation (SRCC) for Habitat in the CVPR19 setting was 0.18, because agents exploited collision "sliding". Tuning the simulation parameters raised it to 0.844. This was PointGoal navigation, with 9 models. — [arXiv 1912.06321](https://arxiv.org/abs/1912.06321) | Accurate. The claim generalizes one navigation study, which is acceptable. | Optional: "In navigation, performance in simulation predicted real-world performance poorly until simulator parameters were tuned [1]." |
| 2 | The bound: target error ≤ source error + discrepancy + joint error of the best single model | This is the Ben-David et al. bound: source error + ½ H∆H-divergence + λ (the error of the ideal joint hypothesis). — [Crossref](https://api.crossref.org/works/10.1007/s10994-009-5152-4) | Accurate | none |
| 2/8 (uncited) | §6: "since invariance cannot reduce the joint error"; §7 RQ3: "Invariance does not reduce the joint error term, which shrinks only as the simulation gets closer to reality." | Zhao et al. prove a lower bound on the joint error of invariant representations, and show a trade-off *when the marginal label distributions differ*. λ is defined in the representation space, so it depends on the representation, not only on the simulator. — [arXiv 1901.09453](https://arxiv.org/abs/1901.09453) | Overstated | See the corrections list |
| 3 | "varies simulator parameters such as textures so that reality appears as one more variation" | "With enough variability in the simulator, the real world may appear to the model as just another variation"; randomized rendering and textures. — [arXiv 1703.06907](https://arxiv.org/abs/1703.06907) | Accurate | none |
| 4 | "fitting it to a few real rollouts" | "adapt the simulation parameter distribution using a few real world roll-outs interleaved with policy training" — [arXiv 1810.05687](https://arxiv.org/abs/1810.05687) | Accurate | none |
| 5 | "maximizing its entropy while preserving task success"; also the uncited "Overly wide randomization leads to conservative behaviour" | DORAEMON "maximizes the entropy of the training distribution" and increases diversity "as long as the probability of success of the current policy is sufficiently high". The same abstract says excessive randomization "leads to overly conservative policies". — [arXiv 2311.01885](https://arxiv.org/abs/2311.01885) | Accurate | none |
| 4-5 | "These methods tune a few global parameters of a synthetic simulator" | [4] and [5] adapt distributions over simulation and dynamics parameters. — same sources | Accurate | none |
| 6 | "Domain-adversarial training aligns features across domains" | DANN learns features that cannot discriminate between domains. — [arXiv 1505.07818](https://arxiv.org/abs/1505.07818) | Accurate | none |
| 7 | "aligning the joint distributions of observations and actions in simulated and real data improved co-trained policies ... in reality" | "aligning the joint distributions of observations and their corresponding actions across domains"; OT loss; "up to a 30% improvement in the real-world success rate". — [arXiv 2509.18631](https://arxiv.org/abs/2509.18631) | Accurate | none |
| 8 | "invariance with low source error does not guarantee transfer, as it can increase the joint error term" | A counterexample shows that invariance plus low source error is not sufficient. The lower bound on joint error holds "when the marginal label distributions differ". — [arXiv 1901.09453](https://arxiv.org/abs/1901.09453) | Accurate, with a condition omitted (slightly overstated) | "...as it can increase the joint error term when label distributions differ between domains [8]" |
| 9 | "Effective simulation-and-real co-training aligns the two domains while keeping them distinguishable" | "structured representation alignment ... reflects a balance between cross-domain representation alignment and domain discernibility, and plays a primary role". — [arXiv 2604.13645](https://arxiv.org/abs/2604.13645) | Accurate | none |
| 10 | "3D Gaussian Splatting reconstructs photorealistic scenes from ordinary images" | The method takes multi-view photos calibrated with SfM and does real-time radiance-field rendering. — [Crossref](https://api.crossref.org/works/10.1145/3592433) | Accurate. "ordinary" is loose. | Optional: "from ordinary multi-view photographs" |
| 11 | "train policies from a scan of the target scene" | RialTo robustifies imitation policies with RL in digital twins "constructed on the fly from small amounts of real-world data" through a scanning interface. — [arXiv 2403.03949](https://arxiv.org/abs/2403.03949) | Accurate | none |
| 12 | "transfer image-based policies to reality without real data" | Zero-shot transfer of RGB policies trained in SplatSim: 86.25% success, against 97.5% for policies trained on real data. The splats themselves are built from real images of the scene. — [arXiv 2409.10161](https://arxiv.org/abs/2409.10161) | Overstated: real images are used to build the twin | "without real-world demonstrations" |
| 13 | "guide real-world reinforcement learning from a phone capture"; §6 later: "uses a twin to find failure-prone configurations for real rollouts" | Twin reconstructed "from smartphone-captured scenes"; RL in the twin acts as "an exploration guide for real-world RL" and "identifies failure-prone yet informative configurations, enabling targeted human-in-the-loop rollouts". — [arXiv 2602.09023](https://arxiv.org/abs/2602.09023) | Accurate (both) | none |
| 14 | §6: "scenes visually matched to real images of two robot setups track the real-world performance of the same policies"; §9: "following the visual matching of SIMPLER [14]" | SIMPLER addresses both *control* and visual gaps (system identification plus "Visual Matching" = green-screening and texture matching) on Google Robot and WidowX, and reports "strong correlation" in paired sim-and-real evaluations. — [arXiv 2405.05941](https://arxiv.org/abs/2405.05941); SIMPLER paper text (Fig. 4 SysID, Fig. 5 Visual Matching) | §6 is slightly overstated because it credits visual matching alone and omits controller alignment. §9 is accurate. | §6: "...scenes matched to real images and robot controllers of two robot setups track..." |
| 15 | "policies have been trained in twins built from a phone capture of a room" | "fine-tuning policies within the reconstructed scenes"; iPhone capture; +20%/+40% success on real ImageNav; SRCC 0.87-0.97. — [arXiv 2509.17430](https://arxiv.org/abs/2509.17430) | Slightly overstated: the policies were fine-tuned, not trained from scratch | "policies have been fine-tuned in twins built from a phone capture of a room [15]" |
| 16 | "from a monocular video of urban scenes" | "Given a monocular video as input, Vid2Sim can generate ... 3D simulation environments" for urban navigation RL. — [arXiv 2501.06693](https://arxiv.org/abs/2501.06693) | Accurate | none |
| 17 | "randomization, photorealism and physics realism in real-world manipulation" | Studies "multi-level domain randomization, photorealistic rendering, physics-realistic modeling, and reinforcement learning updates" in more than 10k real trials with VLA models. — [arXiv 2603.22876](https://arxiv.org/abs/2603.22876) | Accurate (it also covers RL updates) | none |
| 18 | "task-relevant fidelity in robotic ultrasound" | "task-relevant feature-dynamics fidelity (TR-FDF)"; 390/400 zero-shot successes; TR-FDF "complements single-frame realism in predicting zero-shot transfer". — [arXiv 2608.29516](https://arxiv.org/abs/2608.29516) | Accurate. The paper is more precisely about feature *dynamics* fidelity. | Optional: "task-relevant feature-dynamics fidelity in robotic ultrasound [18]" |
| 19 | "Probing ... showed that action fine-tuning degrades the visual representations of robot policies" | "naive action fine-tuning leads to degradation of visual representations ... we probe VLA's hidden representations and analyze attention maps". — [arXiv 2510.25616](https://arxiv.org/abs/2510.25616) | Accurate. The paper is about VLA models specifically. | Optional: "...of vision-language-action policies [19]" |
| 20 | "the best layers to adapt depend on the type of shift" | "the type of distribution shift influences which subset is more effective to tune" (surgical fine-tuning). — [arXiv 2210.11466](https://arxiv.org/abs/2210.11466) | Accurate | none |
| 21 | "Co-training with a small real set yields large gains" | "simulation data can enhance real-world task performance by an average of 38%". — [arXiv 2503.24361](https://arxiv.org/abs/2503.24361) | Accurate | none |
| 22 | "active system identification collects the real trajectories most informative about physics" | Uses the simulator to design exploration policies that collect "high-quality data" to identify articulation, mass and other parameters (Fisher-information exploration). — [arXiv 2404.12308](https://arxiv.org/abs/2404.12308) | Accurate | none |
| 23 | "factors of variation whose difficulty ordering is largely consistent between simulation and reality" | "an ordering of factors based on generalization difficulty, that is consistent across simulation and our real robot setup". — [arXiv 2307.03659](https://arxiv.org/abs/2307.03659) | Accurate | none |

- §7 contains no [n] citations. Its RQ2 sentence "Even in models that transfer well, simulated and real inputs remain distinguishable" restates [9] and is accurate. §7 RQ1's statement of the bound restates [2] and is accurate. §7 RQ3's joint-error sentence is overstated; see the corrections list. — [arXiv 2604.13645](https://arxiv.org/abs/2604.13645), [arXiv 1901.09453](https://arxiv.org/abs/1901.09453)
- §9 names works without references: 3D Gaussian Splatting (= [10], uncited in §9), Habitat, ManiSkill3 and ScanNet++. Its only [n] citation is [14], which is accurate. — plan text

### Inferences
- Adding "[10]" after "3D Gaussian Splatting" in §9 is optional but consistent. Habitat, ManiSkill3 and ScanNet++ would need new reference entries if cited. Because the IPB keeps references in §6 only, leaving them as named tools is acceptable.

### Gaps
- Claims were checked against abstracts and, for [9] and [14], against the paper text. Full-text checks for the other papers were not done because their abstracts contain the specific statements.

## Formatting: numbering order and completeness

### Takeaway
The numbering is correct. First citations in §6 run [1]→[23] in order ([13] is re-cited later, which is fine). All 23 references are cited, and every citation is listed. §9 cites only [14], which exists.

### Cited Findings
- Order of first citation in §6: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, (13), 23. — plan text (content/06-state-of-the-art.md)

### Inferences
- If "[10]" is added in §9, the order is unaffected, because first citations determine numbering.

### Gaps
- none

## Style: which reference format?

### Takeaway
Keep the current format, "Surname, I., et al. (Year). Title in sentence case. Venue.", and make it fully consistent. All 23 works have 4 or more authors, and §6 has a 2-page limit, so "et al." after the first author is justified. The accepted ipb4 IPB uses exactly this "Surname, First, et al." pattern.

### Cited Findings
- binkowski.txt uses numbered APA references with full author lists up to about 7 and "..." truncation, e.g. "Jumper, J., Evans, R., Pritzel, A., ... & Hassabis, D. (2021)". — scratchpad/binkowski.txt lines 299-345
- ipb4.txt uses numbered references with the first author and "et al.", e.g. "[4] Wielopolski, Patryk, et al. \"...\" ... (2025)", and cites arXiv items as "arXiv preprint arXiv:2602.18792 (2026)". — scratchpad/ipb4.txt lines 209-240

### Inferences
- The current style is internally consistent except for three points:
  1. Title case in [9], [17] and [18], while all others use sentence case.
  2. arXiv items are written as a bare "arXiv:XXXX" id. That is fine, but "arXiv preprint arXiv:XXXX" matches ipb4.
  3. There are two stale venues, [13] and [17].
- Full author lists (APA 7) would add about 10 lines (SIMPLER alone has 16 authors) and are not needed.

### Gaps
- none

## Required corrections (exact old → new)

References (content/06-state-of-the-art.md):

1. `[9] Lei, Y., et al. (2026). A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies. arXiv:2604.13645.`
   → `[9] Lei, Y., et al. (2026). A mechanistic analysis of sim-and-real co-training in generative robot policies. arXiv preprint arXiv:2604.13645.`
2. `[13] Xu, Q., et al. (2026). TwinRL: Digital twin-driven reinforcement learning for real-world robotic manipulation. arXiv:2602.09023.`
   → `[13] Xu, Q., et al. (2026). TwinRL-VLA: Digital twin-driven reinforcement learning for real-world robotic manipulation. ACM MM (arXiv:2602.09023).`
3. `[17] Jin, R., et al. (2026). Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models. arXiv:2603.22876.`
   → `[17] Jin, R., et al. (2026). Grounding sim-to-real generalization in robotic manipulation: An empirical study with vision-language-action models. ECCV.`
4. `[18] Qian, Y., et al. (2026). Task-Relevant Feature-Dynamics Fidelity Enables Zero-Shot Sim-to-Real Transfer for Robotic Ultrasound Scanning. arXiv:2608.29516.`
   → `[18] Qian, Y., et al. (2026). Task-relevant feature-dynamics fidelity enables zero-shot sim-to-real transfer for robotic ultrasound scanning. arXiv preprint arXiv:2608.29516.`

In-text, §6:

5. `and, since invariance cannot reduce the joint error, correcting the simulation towards reality.`
   → `and, since invariance does not target the joint error and can even increase it, correcting the simulation towards reality.`
6. `as it can increase the joint error term [8]`
   → `as it can increase the joint error term when label distributions differ between domains [8]`
7. `to transfer image-based policies to reality without real data [12]`
   → `to transfer image-based policies to reality without real-world demonstrations [12]`
8. `Paired simulated and real evaluations showed that scenes visually matched to real images of two robot setups track the real-world performance of the same policies [14].`
   → `Paired simulated and real evaluations showed that scenes matched to real images and robot controllers of two robot setups track the real-world performance of the same policies [14].`
9. `In navigation, policies have been trained in twins built from a phone capture of a room [15]`
   → `In navigation, policies have been fine-tuned in twins built from a phone capture of a room [15]`

In-text, §7 (RQ3):

10. `Invariance does not reduce the joint error term, which shrinks only as the simulation gets closer to reality.`
    → `Invariance does not target the joint error term and can even increase it, whereas bringing the simulation closer to reality reduces it directly.`

Optional (accurate as written, sharper if changed):

11. §6 `reconstructs photorealistic scenes from ordinary images [10]` → `reconstructs photorealistic scenes from ordinary multi-view photographs [10]`
12. §6 `or task-relevant fidelity in robotic ultrasound [18]` → `or task-relevant feature-dynamics fidelity in robotic ultrasound [18]`
13. §6 `degrades the visual representations of robot policies [19]` → `degrades the visual representations of vision-language-action policies [19]`
14. §9 `e.g., 3D Gaussian Splatting,` → `e.g., 3D Gaussian Splatting [10],`

The same edits should be mirrored in the Polish reading copy if it contains §6 and §7.

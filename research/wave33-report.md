# Wave 33 report (2026-09-28): IPB re-centred on world models, three threads, observable measures only

## New research questions and hypotheses (§7)
- RQ1 (thread a, real-to-simulation-to-real): which representation learning choices (world-model prediction target: pixels vs features of an encoder pretrained on real video, policy encoder, amount and diversity of imagined data) decide whether a policy trained inside a world model built from real data works on real inputs. H1: feature-predicting world models give policies that transfer better; rival: action following explains the results.
- RQ2 (thread c, simulation-trained world models): which choices (prediction target, appearance randomization, Cosmos Transfer photorealistic transfer, physics randomization, an objective pairing each simulated frame with its photorealistic version, co-training with a small real set) make a world model trained on Isaac Lab data predict real recordings and give policies that work on real data. H2: the pairing objective beats merely adding the frames; rival: the gap is mainly physics.
- RQ3 (thread b, reducing real data): how to pretrain representations so a new real setting needs less real data (continue pretraining of existing real-video encoders on simulation / real / both, with and without the RQ2 objective; full vs LoRA vs co-training at equal real data). H3: both-data pretraining with the objective reaches full fine-tuning performance with less real data; rival: real-data need is set by the new dynamics.
- RQ4: do the answers hold in unseen scenes and across navigation and manipulation. H4: best choices in navigation also help manipulation, otherwise reported as task specific.
- Fallback: study the data side (mixing ratios, amount and diversity of generated data).
- Removed: the old RQ3 on choosing real rollouts that correct both the world model and the policy, and (owner redirect during the wave) every latent-space method (latent gap, observation/dynamics split, probing, alignment, stage-targeted or test-time adaptation).

## Changes per section
- §2: topic retuned to "Representation learning methods for the simulation-to-reality generalization of world models and policies in physical AI" (PL: "Metody uczenia reprezentacji dla generalizacji modeli świata i polityk z symulacji do rzeczywistości w fizycznej sztucznej inteligencji"), confirmed by the coordinator.
- §3: semesters 1-2 unchanged; 3-6 re-labelled to RQ1-RQ4; RSS removed from the semester-4 venue example (no RSS deadline before September 2027).
- §5: rewritten around the loop reality -> world model -> policy -> reality, the three threads, and representation learning as the choice of how features are learned; absence claims phrased as "I have not found in my search".
- §6: new paragraphs on world models trained on simulation data and on adapting with little real data; new refs Cosmos-Transfer1, Zanatta et al. 2026, Nilaksh et al. 2026, Interactive World Simulator (RSS 2026), LoRA; dropped TwinRL, Veo evaluator, Ben-David, Zhao, Xie, AdaJEPA; overclaims softened (DreamGen, SkyJEPA, Cosmos Transfer, "first", "term was set").
- §7: goal + constraints + 8 labelled items (RQ1, H1, RQ2, H2, RQ3, H3, RQ4/H4, Fallback).
- §8: three expected results matching the three threads.
- §9: methods per RQ; "real performance" defined (action closeness on held-out real trajectories + SIMPLER success; path closeness for navigation); DROID contamination handled; Isaac Lab 3.0 mode without Isaac Sim (RGB+depth), Cosmos Transfer driven by depth, ManiSkill/Habitat fallback; policies trained on generated trajectories (no RL inside video models); RQ3 not fully crossed.
- §10: abstract PL/EN rewritten (identical content).
- §12: AI disclosure kept; 27 references numbered by first appearance across §5-§9, identical in EN and PL.
- PL copy (output/IPB_Grzegorz_Piotrowski_PL.md + .docx via python-docx) fully synced.

## Verification
- Build: python3 tools/build_ipb.py. PDF (Pages.app) measures: §5 0.84, §6 1.69, §7 0.96, §8 0.34, §9 1.84, §12 0.87, §10 0.19/0.17 pages. The text-length estimator flags §7, §9, §12 as RISK (it overestimates by about 10-15 percent); the PDF is within every limit. Check in Word before printing.
- Punctuation: no ';', '—', '–' in EN visible text or PL copy. "sim-to-real" only inside cited titles.
- 6-gram overlap with the three reference plans: 0.
- Citations: first-appearance order 1..27 in EN §5-§9 and identical in PL; bibliography identical EN/PL.
- References verified by a literature agent (arXiv API, OpenReview, Crossref, PMLR): research/lit_threads_2026-09-28.md. Isaac Lab kit-less mode on H100: kit-less confirmed in NVIDIA docs, H100 support NOT found in docs, so §9 says "should run on H100" and promises a check.
- Adversarial reviews: research/review-7-threads.md (pre-redirect draft) and research/review-8-final.md (final draft); all Critical and Major items applied except those noted below.

## Open doubts
- Two tasks at equal weight with four RQs is tight for one student (both reviews). Kept per the owner's binding decision.
- For feature-predicting world models the policy encoder and the prediction target are tied (policy acts on the world model's features), so RQ1 is not fully one-factor-at-a-time for that pair.
- Nearest neighbours not cited to keep §12 within one page: World Translation (arXiv:2607.18154), R3M/VC-1 style encoder comparisons for policies.
- Wang et al. 2026 [7] is a CVPR 2026 workshop paper, cited as arXiv. VLAW now listed as ICML 2026.
- Nothing committed (per instructions). Untracked new files: research/lit_threads_2026-09-28.md, research/review-7-threads.md, research/review-8-final.md, research/wave33-report.md.

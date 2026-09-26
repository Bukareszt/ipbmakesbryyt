# §2 Temat rozprawy doktorskiej / Topic of doctoral dissertation

Improving generalization of deep learning models in real-to-sim-to-real transfer for physical AI.

<!-- Wave 18-W (issue #35), 2026-09-26: rewritten after pivot decision v7 (research/pivot-decision.md, top):
the dissertation is about HOW TO REDUCE the amount of real data (not about measuring it); the title is
general and mentions navigation and manipulation as examples; navigation is the main testbed, manipulation
the generalization test. The title names the goal (reducing real data), the setting (the real-to-sim-to-real
loop with digital twins), the product (a method) and the two example tasks. No model or checkpoint names.
Alternatives for the supervisor:
- EN "A real-to-sim-to-real method that reduces the real data needed to teach robots, applied to navigation
  and manipulation" / PL "Metoda typu rzeczywistość–symulacja–rzeczywistość ograniczająca ilość danych
  rzeczywistych potrzebnych do uczenia robotów, z zastosowaniem w nawigacji i manipulacji"
- EN "Teaching robots with less real data: a real-to-sim-to-real method with digital twins for navigation
  and manipulation" / PL "Uczenie robotów przy mniejszej ilości danych rzeczywistych: metoda typu
  rzeczywistość–symulacja–rzeczywistość z cyfrowymi bliźniakami dla nawigacji i manipulacji"
The Wave 16 (v6) title is kept below as history. -->

<!-- (history) Wave 16-W (issue #33), 2026-09-26: rewritten after pivot decision v6 (research/pivot-decision.md, top):
"The title is short and general"; no model or checkpoint names; navigation is the domain; the object is a
method for real-to-sim-to-real learning of navigation models that needs less real data. The title names
the learned object (robot navigation models), the tool (digital twins), the goal (less real data) and the
product (a real-to-sim-to-real method). v6 title: PL "Uczenie modeli nawigacji robotów w cyfrowych
bliźniakach przy mniejszej ilości danych rzeczywistych: metoda typu rzeczywistość–symulacja–rzeczywistość";
EN "Learning robot navigation models in digital twins with less real data: a real-to-sim-to-real method".
Alternatives for the supervisor:
- EN "A real-data-efficient real-to-sim-to-real method for learning robot navigation" / PL "Oszczędna pod
  względem danych rzeczywistych metoda uczenia nawigacji robotów w pętli rzeczywistość–symulacja–
  rzeczywistość"
- EN "From real data to digital twins and back: learning robot navigation with less real data" / PL "Od
  danych rzeczywistych do cyfrowego bliźniaka i z powrotem: uczenie nawigacji robotów przy mniejszej
  ilości danych rzeczywistych" -->

<!-- (history) Wave 15 (issue #31), 2026-09-26: rewritten after pivot decision v5 (research/pivot-decision.md, top;
method content; goal, thesis and v3 scope unchanged). The task allowed naming VLA and world models "only if
it stays readable". The title keeps the v4 structure (one method, needs less real data, the loop, C1-C3)
and adds the object being fine-tuned (vision-language-action models) and, in C2, world models. "Pretrained"
and "open" and the VLM (C1) are left to §5/§7 to keep the title readable. PL "wizja–język–działanie"
follows the EN term; the student/supervisor may prefer the English acronym "VLA" in the PL title.
Previous (v4) title: "A method for learning in the real-to-sim-to-real loop that needs less real data:
task-aware capture for building digital twins, uncertainty-aware learning in them and active selection of
few real-world data" (kept as the fallback if the supervisor wants a model-agnostic title).
Shorter alternative for the supervisor:
- EN "Real-data-efficient fine-tuning of vision-language-action models in digital twins and world models" /
  PL "Oszczędne pod względem danych rzeczywistych dostrajanie modeli wizja–język–działanie w cyfrowych
  bliźniakach i modelach świata" -->

<!-- (history) Wave 14 (issue #30), 2026-09-26: rewritten after pivot decision v4 (research/pivot-decision.md, top;
overrides v3 on framing, v3 scope unchanged). v4: "Title ... must say plainly that the dissertation develops
a method that needs less real data." The title now names the product (one method), its property (needs
less real data), the setting (the real-to-sim-to-real loop) and its three components C1-C3 (task-aware
capture, uncertainty-aware learning in the imperfect twin, active selection of few real-world data), one
per loop step. The previous title ("Active allocation of limited real data in the real-to-sim-to-real
loop: building digital twins, learning in them and transferring the results back to reality") named the
allocation idea but not the method as the deliverable. Testbeds (manipulation and navigation, equal
status) stay in §5/§7. The topic does not have to be the final title (SPEC §2).
Shorter alternative for the supervisor:
- EN "A real-data-efficient method for real-to-sim-to-real learning with digital twins" / PL "Metoda
  uczenia w pętli rzeczywistość–symulacja–rzeczywistość z cyfrowymi bliźniakami oszczędzająca dane
  rzeczywiste" -->

<!-- (history) Wave 13 (issue #28), 2026-09-26: rewritten after pivot decision v3 (research/pivot-decision.md, top
section, overrides v2 on scope): a GENERAL, task- and domain-agnostic real-to-sim-to-real methodology, not
centred on navigation, autonomy or robot rollouts. The title names the object (the real-to-sim-to-real
loop), the thesis (active allocation of limited real data) and the three steps of the loop (RQ1 build the
twin with less capture, RQ2 learn robustly in it, RQ3 transfer back with few real-world data; RQ4 the whole
budget). "Embodied policies", "neural scene reconstruction" and navigation were dropped from the title: the
twin now covers appearance, geometry and physical/dynamic parameters, and the learned object is a "policy
or model". Testbeds (manipulation and navigation, equal status) are named in §5/§7 only.
Alternatives for the supervisor:
- EN "Data-efficient real-to-sim-to-real learning: capturing less, learning robustly in imperfect digital
  twins and transferring with few real-world data" / PL "Efektywne pod względem danych uczenie w pętli
  rzeczywistość–symulacja–rzeczywistość: mniej danych do budowy bliźniaka, odporne uczenie w
  niedoskonałym cyfrowym bliźniaku i transfer przy niewielu danych rzeczywistych"
- EN "How much real data does a digital twin save? Active data allocation in real-to-sim-to-real
  learning" / PL "Ile danych rzeczywistych oszczędza cyfrowy bliźniak? Aktywna alokacja danych w uczeniu
  w pętli rzeczywistość–symulacja–rzeczywistość" -->

<!-- (history) Wave 11 (issue #25), 2026-09-26: rewritten after pivot decision v2 (research/pivot-decision.md, binding;
supersedes the wave-9 representation-level title "Internal representations as a measure and predictor of
the real-world transfer ..."). The title names the object (the real-to-sim-to-real loop of embodied
policies), the goal (a limited real-data budget = capture less, train robustly, collect few real rollouts:
RQ1-RQ4) and the tool (digital twins from neural scene reconstruction = 3D Gaussian Splatting, existing
pipelines). Representations and uncertainty are tools inside the methods (pivot v2), so they are left to
§5/§7. Navigation (primary) and manipulation (cross-task) are also left to §5/§7 to keep the title short.
The topic does not have to be the final title (SPEC §2).
Alternatives for the supervisor:
- EN "Data-efficient real-to-sim-to-real transfer of embodied policies: capturing less, training robustly
  on imperfect digital twins and collecting few real rollouts" / PL "Efektywny pod względem danych transfer
  rzeczywistość–symulacja–rzeczywistość polityk agentów ucieleśnionych: mniej nagrań, odporny trening na
  niedoskonałych cyfrowych bliźniakach i nieliczne próby rzeczywiste"
- EN "Active allocation of real data in real-to-sim-to-real learning of embodied policies with neural
  digital twins" / PL "Aktywna alokacja danych rzeczywistych w uczeniu polityk agentów ucieleśnionych w
  pętli rzeczywistość–symulacja–rzeczywistość z neuronowymi cyfrowymi bliźniakami" -->

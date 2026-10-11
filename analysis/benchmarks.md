# Benchmarks and protocols

[Analysis notes](README.md) · [References](../references/README.md)

Representative resources from the manuscript evaluation table. The solver column describes a documented use configuration; it does not assert that the resource requires that solver. Resource-introduction citations and configuration-use citations are kept separate.

## Task solutions and formal models

| Benchmark / protocol | Task | Solver / reference | Evaluation target |
| --- | --- | --- | --- |
| PrOntoQA [saparov2023language](../references/README.md#saparov2023language) | Deductive reasoning | Pyke [pan2023logiclm](../references/README.md#pan2023logiclm) | Answer |
| ProofWriter [tafjord2021proofwriter](../references/README.md#tafjord2021proofwriter) | Deductive reasoning | Pyke [pan2023logiclm](../references/README.md#pan2023logiclm); Prover9 [olausson2023linc](../references/README.md#olausson2023linc) | Task labels; answer accuracy |
| FOLIO [han2024folio](../references/README.md#han2024folio) | First-order reasoning | Prover9 [pan2023logiclm](../references/README.md#pan2023logiclm), [olausson2023linc](../references/README.md#olausson2023linc) | Answer |
| AR-LSAT [zhong2022analytical](../references/README.md#zhong2022analytical) | Analytical reasoning | Z3 [pan2023logiclm](../references/README.md#pan2023logiclm) | Answer |
| LogicalDeduction [srivastava2023beyond](../references/README.md#srivastava2023beyond) | Ordering constraints | python-constraint [pan2023logiclm](../references/README.md#pan2023logiclm) | Answer |
| GSM-SYS (GSM8K subset) [ye2023satlm](../references/README.md#ye2023satlm) | Arithmetic modeling | Z3 / arithmetic constraints  | Answer |
| ALGEBRA [heyueya2023solving](../references/README.md#heyueya2023solving) | Arithmetic modeling | Z3 [ye2023satlm](../references/README.md#ye2023satlm) | Answer |
| BoardgameQA [kazemi2023boardgameqa](../references/README.md#kazemi2023boardgameqa) | Rule reasoning | Z3 [ye2023satlm](../references/README.md#ye2023satlm) | Answer |
| CLUTRR [sinha2019clutrr](../references/README.md#sinha2019clutrr) | Relational reasoning | Z3 [ye2023satlm](../references/README.md#ye2023satlm) | Answer |
| NL4OPT [ramamonjison2023nl4opt](../references/README.md#ramamonjison2023nl4opt) | Linear optimization | Constraint programming [shi2025constraintllm](../references/README.md#shi2025constraintllm) | Verified solutions; solving accuracy |
| ComplexOR [xiao2024chain](../references/README.md#xiao2024chain) | Mixed-integer modeling | AutoOR evaluation [motwani2026autoor](../references/README.md#motwani2026autoor) | Reference solutions |
| IndustryOR [tang2024orlm](../references/README.md#tang2024orlm) | Mixed-integer modeling | AutoOR evaluation [motwani2026autoor](../references/README.md#motwani2026autoor) | Reference solutions |
| IndusCP [shi2025constraintllm](../references/README.md#shi2025constraintllm) | Combinatorial modeling | Constraint programming  | Solving accuracy |
| CP-Bench [michailidis2025cpbench](../references/README.md#michailidis2025cpbench) | Constraints / optimization | CP-Agent revision; CPMpy [szeider2026cpagent](../references/README.md#szeider2026cpagent) | Withheld models and optima; feasibility/optimality |
| ASP-Bench [szeider2026asp](../references/README.md#szeider2026asp) | Logic programming / optimization | ASP / Clingo  | Reference validators; feasibility/optimality |
| BlocksWorld-100 / Logistics-100 [huang2025limit](../references/README.md#huang2025limit) | Planning formalization | PDDL; VAL validation  | Withheld reference PDDL; plan correctness |
| CoPE: BlocksWorld; CoinCollector [huang2026cope](../references/README.md#huang2026cope) | Constrained planning | PDDL  | Reference PDDL; constraint-valid plans |
| PlanBench [valmeekam2023planbench](../references/README.md#valmeekam2023planbench) | Plan verification | Verification variant; NuSMV / LTL [corpus20261009d728294efd40](../references/README.md#corpus20261009d728294efd40) | Plan validity; unknown |
| ALFWorld [shridhar2020alfworld](../references/README.md#shridhar2020alfworld) | Embodied planning | NeSyC; ASP [choi2025nesyc](../references/README.md#choi2025nesyc) | Task success under dynamics |
| VirtualHome [puig2018virtualhome](../references/README.md#puig2018virtualhome) | Embodied safety | SENTINEL; LTL [zhan2025sentinel](../references/README.md#zhan2025sentinel) | Reference constraints; agreement and plan safety |
| RuleArena [zhou2025rulearena](../references/README.md#zhou2025rulearena) | Policy reasoning | ASP / Clingo [nair2026policy](../references/README.md#nair2026policy) | Decision accuracy; robustness |

## Construction of checked formal artifacts

| Benchmark / protocol | Task | Solver / reference | Evaluation target |
| --- | --- | --- | --- |
| miniF2F [zheng2022minif2f](../references/README.md#zheng2022minif2f) | Theorem proving | Lean kernel [xin2024deepseekprover](../references/README.md#xin2024deepseekprover), [yang2023leandojo](../references/README.md#yang2023leandojo) | Supplied theorems; proof Pass@$k$ |
| ProofNet [azerbayev2023proofnet](../references/README.md#azerbayev2023proofnet) | Theorem proving | Lean 4 port; Lean kernel [xin2024deepseekprover](../references/README.md#xin2024deepseekprover) | Proof success; Pass@$k$ |
| FIMO [liu2023fimo](../references/README.md#liu2023fimo) | Theorem proving | Lean kernel  | Proof success; Pass@$k$ |
| PutnamBench [tsoukalas2024putnambench](../references/README.md#tsoukalas2024putnambench) | Theorem proving | DSP+ Lean subset [corpus202610095c24eb6d4be3](../references/README.md#corpus202610095c24eb6d4be3) | Proof success |
| LeanDojo [yang2023leandojo](../references/README.md#yang2023leandojo) | Library theorem proving | Lean / mathlib  | Split-specific proof success |
| PISA [jiang2021lisa](../references/README.md#jiang2021lisa) | Library theorem proving | Isabelle; Baldur split [first2023baldur](../references/README.md#first2023baldur) | Proof success |
| DafnyBench [loughridge2024dafnybench](../references/README.md#loughridge2024dafnybench) | Verification hints | Dafny verifier  | Contract-preserving verification |
| Verus-Bench [yang2025autoverus](../references/README.md#yang2025autoverus) | Verification completion | Verus / SMT  | Proof success |
| Code2Inv [si2020code2inv](../references/README.md#si2020code2inv) | Invariant generation | Z3 [bharti2025loop](../references/README.md#bharti2025loop) | Verified invariants |
| SV-COMP 2023 [beyer2023svcomp](../references/README.md#beyer2023svcomp) | Program-property verification | LEMUR subset; ESBMC / UAutomizer [wu2024lemur](../references/README.md#wu2024lemur) | Verified properties |
| SpecGenBench [corpus202610099d0d88ee902b](../references/README.md#corpus202610099d0d88ee902b) | Contract generation | OpenJML  | Verifiable specifications |
| Alloy4Fun [macedo2021alloy4fun](../references/README.md#macedo2021alloy4fun) | Relational-specification repair | Alloy Analyzer repair [coverage20261009s251](../references/README.md#coverage20261009s251) | Repair validation |
| OSVBench [li2026osvbench](../references/README.md#li2026osvbench) | OS specification generation | Z3 / state model  | Specification Pass@1 |
| Vericoding benchmark [bursuc2025benchmark](../references/README.md#bursuc2025benchmark) | Verified implementation synthesis | Dafny; Verus; Lean  | Verified implementation |

## Correspondence and verifier diagnostics

| Benchmark / protocol | Task | Solver / reference | Evaluation target |
| --- | --- | --- | --- |
| ProofNet# [poiroux2406reliable](../references/README.md#poiroux2406reliable) | Statement formalization | Lean statements  | Reference statements; equivalence assessment |
| RLM25 [poiroux2406reliable](../references/README.md#poiroux2406reliable) | Statement formalization | Lean statements  | Reference statements; equivalence assessment |
| Beyond Compilation (v1) [zhang2026beyond2](../references/README.md#zhang2026beyond2) | Statement formalization | Lean compilation  | Semantic judges; strict consensus |
| ITPEval [wu2026itpeval](../references/README.md#wu2026itpeval) | Cross-prover translation | Lean; Rocq; Isabelle; HOL Light  | Native acceptance; BEq |
| ProofNetVerif [poiroux2406reliable](../references/README.md#poiroux2406reliable) | Metric calibration | BEqL / BEq+ assessment  | Human semantic labels; precision/recall |
| FaithformBench [cornish2026faithformbench](../references/README.md#cornish2026faithformbench) | Validity preservation | Formal validity checks  | Error induction; correction |
| ProcessBench [zheng2024processbench](../references/README.md#zheng2024processbench) | Step-error diagnosis | Coq / formal critic [zhou2025step](../references/README.md#zhou2025step) | Detection F1 |
| SAT-Menu [hazra2024can](../references/README.md#hazra2024can) | Constraint difficulty diagnosis | MiniSat  | Accuracy; phase transition |
| CloverBench [sun2024clover](../references/README.md#sun2024clover) | Acceptance-gate diagnosis | Dafny; tests; docstring judgments  | Correct/adversarial examples; acceptance |

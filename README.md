<div align="center">

# Solvers in the Loop

**A Survey of Verifiable Neuro-Symbolic Reasoning with Large Language Models**

Yishuai Geng · Guohui Xiao · Guilin Qi · Huajun Chen · Haofen Wang

Paper link forthcoming · [Manuscript information](manuscript/README.md)

**[Paper lists](#paper-lists) · [Solver evolution](#solver-evolution) · [Full catalogue](papers/README.md) · [Resources](#resources) · [Citation](#citation)**

</div>

This repository accompanies *Solvers in the Loop*, a survey of how symbolic solvers support reasoning with large language models. We organize the literature around five uses of solver feedback: **symbolic solving, verification, diagnosis and repair, search control, and learning supervision**.

The review covers **1,429 studies** from January 2020 through September 2026. Start with the classified examples below, or browse the [complete literature catalogue](papers/README.md).

<p align="center">
  <img src="assets/figures/overview.png" alt="Overview of language models, symbolic solvers, and five uses of solver feedback." width="100%">
</p>

## Solver evolution

Formal foundations, solver tools, and LLM–solver configurations across ten solver families.

[![Solver development tree](assets/figures/solver-evolution.png)](assets/figures/solver-evolution.png)

[Open at full resolution](assets/figures/solver-evolution.png) · [Role taxonomy](docs/taxonomy.md) · [Full method index](docs/method-index.md)

## Paper lists

Examples from the survey's taxonomy, grouped by how solver feedback is used. A study can appear under more than one role.

[Symbolic Solving](#symbolic-solving) · [Verification](#verification) · [Diagnosis and Repair](#diagnosis-and-repair) · [Search Control](#search-control) · [Learning Supervision](#learning-supervision)

### Symbolic Solving

Use the returned consequence, model, plan, or proof to construct an answer.

**Symbolic Inference**

- **BeliefBank** · [BeliefBank: Adding Memory to a Pre-Trained Language Model for a Systematic Notion of Belief](<https://doi.org/10.18653/v1/2021.emnlp-main.697>) (2021).
- **Maieutic Prompting** · [Maieutic Prompting: Logically Consistent Reasoning with Recursive Explanations](<https://doi.org/10.18653/v1/2022.emnlp-main.82>) (2022).

**Constraint Solving**

- **LiP-LLM** · [LiP-LLM: Integrating Linear Programming and Dependency Graph With Large Language Models for Multi-Robot Task Planning.](<https://doi.org/10.1109/lra.2024.3518105>) (2025).
- **Lucy** · [Lucy: Think and Reason to Solve Text-to-SQL](<https://arxiv.org/abs/2407.05153>) (2024).

**Symbolic Planning**

- **LLM+P** · [LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](<https://arxiv.org/abs/2304.11477>) (2023).
- **NL2Plan** · [NL2Plan: Robust LLM-Driven Planning from Minimal Text Descriptions](<https://arxiv.org/abs/2405.04215>) (2024).

[Browse all 606 studies →](papers/roles/symbolic-solving.md)

### Verification

Use the verdict to accept, reject, or qualify a candidate relative to an encoded obligation.

**Proof Checking**

- **Baldur** · [Baldur: Whole-Proof Generation and Repair with Large Language Models](<https://doi.org/10.1145/3611643.3616243>) (2023).
- **LogicGuide** · [Certified Deductive Reasoning with Language Models](<https://www.scopus.com/pages/publications/85214721943?origin=resultslist>) (2024).

**Formalization Validation**

- **LLM-ARC** · [LLM-ARC: Enhancing LLMs with an Automated Reasoning Critic](<https://arxiv.org/abs/2406.17663>) (2024).
- **RAINCOAT** · [Normative Requirements Operationalization with Large Language Models](<https://doi.org/10.1109/re59067.2024.00022>) (2024).

**Program Verification**

- **LEMUR** · [LEMUR: INTEGRATING LARGE LANGUAGE MODELS IN AUTOMATED PROGRAM VERIFICATION](<https://www.scopus.com/pages/publications/85198296534?origin=resultslist>) (2024).
- **Clover** · [Clover: Closed-Loop Verifiable Code Generation](<https://doi.org/10.1007/978-3-031-65112-0_7>) (2024).

**Behavioral Verification**

- **AutoIoT** · [AutoIoT: Automated IoT Platform Using Large Language Models](<https://doi.org/10.1109/jiot.2024.3523907>) (2025).
- **SymPlanner** · [SymPlanner: Deliberate Planning in Language Models with Symbolic Representation.](<https://arxiv.org/abs/2505.01479>) (2025).

[Browse all 1,043 studies →](papers/roles/verification.md)

### Diagnosis and Repair

Use counterexamples, errors, or other diagnostic feedback to revise a candidate.

**Representation Repair**

- **BeliefBank** · [BeliefBank: Adding Memory to a Pre-Trained Language Model for a Systematic Notion of Belief](<https://doi.org/10.18653/v1/2021.emnlp-main.697>) (2021).
- **ConCoRD** · [Enhancing Self-Consistency and Performance of Pre-Trained Language Models through Natural Language Inference](<https://doi.org/10.18653/v1/2022.emnlp-main.115>) (2022).

**Proof Repair**

- **Baldur** · [Baldur: Whole-Proof Generation and Repair with Large Language Models](<https://doi.org/10.1145/3611643.3616243>) (2023).
- **Lyra** · [Lyra: Orchestrating Dual Correction in Automated Theorem Proving](<https://www.scopus.com/pages/publications/85204811545?origin=resultslist>) (2024).

**Program Repair**

- **SmartHalo** · [Augmenting Smart Contract Decompiler Output Through Fine-Grained Dependency Analysis and LLM-Facilitated Semantic Recovery](<https://doi.org/10.1109/tse.2025.3623325>) (2025).
- **LusGen** · [LusGen: Leveraging LLMs for Safety-Critical Lustre Design and Requirements Traceability](<https://doi.org/10.1007/978-3-032-22774-4_4>) (2026).

**Plan Repair**

- **PanelShield** · [PanelShield: Verifiable Closed-Loop Safe Planning for Robotic Industrial Panel Operation](<https://arxiv.org/abs/2608.28305>) (2026).
- **GCC** · [Neuro-symbolic Hierarchical Learning for Long-Horizon Robotic Tasks](<https://doi.org/10.1145/3808338>) (2026).

[Browse all 574 studies →](papers/roles/diagnosis-repair.md)

### Search Control

Use solver signals to guide expansion, pruning, or selection during search.

**Constrained Generation**

- **LogicGuide** · [Certified Deductive Reasoning with Language Models](<https://www.scopus.com/pages/publications/85214721943?origin=resultslist>) (2024).
- **Agent-C** · [Enforcing Temporal Constraints for LLM Agents](<https://arxiv.org/abs/2512.23738>) (2025).

**Candidate Pruning**

- **Safety Chip** · [Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents](<https://doi.org/10.1109/icra57147.2024.10611447>) (2024).
- **D&P** · [Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning](<https://arxiv.org/abs/2603.17233>) (2026).

**State-Space Exploration**

- **GPT-f** · [Generative Language Modeling for Automated Theorem Proving](<https://arxiv.org/abs/2009.03393>) (2020).
- **Thor** · [Thor: Wielding Hammers to Integrate Language Models and Automated Theorem Provers](<https://www.scopus.com/pages/publications/85163186428?origin=resultslist>) (2022).

[Browse all 275 studies →](papers/roles/search-control.md)

### Learning Supervision

Use solver outcomes to construct or select training data, rewards, or learning targets.

**Supervised Training**

- **PACT** · [PROOF ARTIFACT CO-TRAINING FOR THEOREM PROVING WITH LANGUAGE MODELS](<https://www.scopus.com/pages/publications/85131513069?origin=resultslist>) (2022).
- **Baldur** · [Baldur: Whole-Proof Generation and Repair with Large Language Models](<https://doi.org/10.1145/3611643.3616243>) (2023).

**Reinforcement Learning**

- **DeepSeek-Prover-V1.5** · [DEEPSEEK-PROVER-V1.5: HARNESSING PROOF ASSISTANT FEEDBACK FOR REINFORCEMENT LEARNING AND MONTE-CARLO TREE SEARCH](<https://www.scopus.com/pages/publications/105010181109?origin=resultslist>) (2025).
- **WARP** · [Worst-Case Symbolic Constraints Analysis and Generalisation with Large Language Models](<https://arxiv.org/abs/2506.08171>) (2025).

**On-Policy Distillation**

- **RWOPD** · [Reward-Weighted On-Policy Distillation with an Open Property-Equivalence Verifier for NL-to-SVA Generation](<https://arxiv.org/abs/2605.13501>) (2026).
- **SOLID** · [Beyond Verified Answers: Solver-Informed Self-Distillation for Bootstrapping Operations Research Language Models](<https://arxiv.org/abs/2609.09957>) (2026).

[Browse all 262 studies →](papers/roles/learning-supervision.md)


[Browse all papers by role or year](papers/README.md) · [September-window additions](papers/updates/2026-09.md)

## Resources

- **[Complete paper catalogue](papers/README.md)** — all 1,429 studies, organized by role and citation year; download [CSV](data/papers.csv) or [JSON](data/papers.json).
- **[Taxonomy and method index](docs/taxonomy.md)** — finer mechanism groups and the scope of verification claims.
- **[Benchmarks and analysis](analysis/README.md)** — evaluation resources and descriptive summaries, with their coverage stated.
- **[Manuscript bibliography](references/README.md)** — 488 cited references; download [BibTeX](references/references.bib).

[Scope and interpretation](docs/methodology.md) · [Data field definitions](data/schema.md)

## Contributing

Suggestions and corrections are welcome through [Issues](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/issues/new/choose). Include a paper link and explain the relevant solver interaction or correction. See the [contribution guide](CONTRIBUTING.md).

## Citation

A paper citation will be added when the manuscript is public. For now, you can cite this companion repository.

```bibtex
@misc{geng2026solvers_companion,
  author = {Yishuai Geng},
  title = {Solvers in the Loop: Survey Companion Repository},
  year = {2026},
  howpublished = {GitHub repository},
  url = {https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey}
}
```

For a specific state of the catalogue, include an access date or commit in your citation. GitHub's **Cite this repository** button uses [CITATION.cff](CITATION.cff).

Copyright is retained; see [LICENSE](LICENSE) and [figure credits](assets/README.md).

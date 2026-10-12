<div align="center">

# Solvers in the Loop

**A Survey of Verifiable Neuro-Symbolic Reasoning with Large Language Models**

Yishuai Geng · Guohui Xiao · Guilin Qi · Huajun Chen · Haofen Wang

[![Validation](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/actions/workflows/validate.yml/badge.svg)](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/actions/workflows/validate.yml)
![Studies](https://img.shields.io/badge/studies-1429-286b75)
![Coverage](https://img.shields.io/badge/literature-through_September_2026-64748b)

**[Paper status](manuscript/README.md) · [Latest release](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/releases/latest)**

Manuscript in preparation · Public paper links will be added when available.

**[Literature](papers/README.md) · [Solver evolution](#solver-evolution) · [Taxonomy](docs/taxonomy.md) · [Benchmarks & analysis](analysis/README.md) · [Bibliography](references/README.md)**

</div>

Language models propose representations, candidates, and actions; symbolic solvers return answers, verdicts, counterexamples, or structured feedback. This survey connects **solver families**, **the roles of their returned signals**, and **the evidence needed to interpret a formal check as a claim about a task**.

<p align="center">
  <img src="assets/figures/overview.png" alt="Solver-in-the-loop reasoning and five uses of solver feedback." width="100%">
</p>

**1,429 included studies · 1,715 reports · 5 solver roles · 486 cited references**

Literature coverage: **January 2020–September 2026**. [Scope and definitions](docs/methodology.md) · [Papers added in this update](papers/updates/2026-09.md)

## Solver evolution

Selected **formal foundations**, **solver tools**, and **LLM–solver configurations**, arranged by family and the publication year of the cited report.

<a href="assets/figures/solver-evolution.png">
  <img src="assets/figures/solver-evolution.png" alt="Development of ten solver families and their connections to language-model reasoning." width="100%">
</a>

[Open at full resolution](assets/figures/solver-evolution.png) · [Explore the full role taxonomy](docs/taxonomy.md) · [Representative methods](docs/method-index.md)

## Five uses of solver feedback

| Role | How the signal is used | Studies |
| --- | --- | --- |
| [R1 · Symbolic Solving](papers/roles/symbolic-solving.md) | Use the returned consequence, model, plan, or proof to construct an answer. | 606 |
| [R2 · Verification](papers/roles/verification.md) | Use the verdict to accept, reject, or qualify a candidate relative to an encoded obligation. | 1,043 |
| [R3 · Diagnosis and Repair](papers/roles/diagnosis-repair.md) | Use counterexamples, errors, or other diagnostic feedback to revise a candidate. | 574 |
| [R4 · Search Control](papers/roles/search-control.md) | Use solver signals to guide expansion, pruning, or selection during search. | 275 |
| [R5 · Learning Supervision](papers/roles/learning-supervision.md) | Use solver outcomes to construct or select training data, rewards, or learning targets. | 262 |

Role assignments overlap; the counts cannot be summed. [Unassigned role labels](papers/roles/unassigned.md) remain explicit.

## Companion resources

| Resource | Contents |
| --- | --- |
| [Literature catalogue](papers/README.md) | Papers by solver role and citation year, with public source links |
| [Taxonomy](docs/taxonomy.md) | Mechanism groups, representative methods, and verification boundaries |
| [Benchmarks and protocols](analysis/benchmarks.md) | Evaluation resources, solver configurations, and source references |
| [Analysis](analysis/README.md) | Corpus distributions and task/metric summaries with their coverage units |
| [Bibliography](references/README.md) | The manuscript's cited references and downloadable [BibTeX](references/references.bib) |
| [Data](data/README.md) | [CSV](data/papers.csv), [JSON](data/papers.json), and [field definitions](data/schema.md) |

## Contribute

Suggest a paper or report a correction through [Issues](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/issues/new/choose). Include a public source and explain the solver interaction or proposed correction. [Contribution guide](CONTRIBUTING.md) · [Maintenance policy](docs/maintenance.md) · [Release changes](CHANGELOG.md)

## Cite

Until a public paper citation is available, cite the companion repository and specify the release you used. GitHub's **Cite this repository** button uses [CITATION.cff](CITATION.cff).

```bibtex
@misc{geng2026solvers_companion,
  author = {Yishuai Geng},
  title = {Solvers in the Loop: Survey Companion Repository},
  year = {2026},
  howpublished = {GitHub repository, version v0.2.0},
  url = {https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey}
}
```

Copyright is retained; no open license is granted at this stage. See [LICENSE](LICENSE) and [figure credits](assets/README.md).

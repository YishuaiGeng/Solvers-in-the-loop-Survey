<div align="center">

# Solvers in the Loop

**A Survey of Verifiable Neuro-Symbolic Reasoning with Large Language Models**

Yishuai Geng · Guohui Xiao · Guilin Qi · Huajun Chen · Haofen Wang

[![Validation](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/actions/workflows/validate.yml/badge.svg)](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/actions/workflows/validate.yml)
![Studies](https://img.shields.io/badge/studies-1301-286b75)
![Eligibility](https://img.shields.io/badge/eligibility-through_Aug_2026-64748b)

**[Paper status](manuscript/README.md) · [Latest release](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/releases/latest)**

Manuscript in preparation · Public paper links will be added when available.

**[Literature](papers/README.md) · [Solver evolution](#solver-evolution) · [Taxonomy](docs/taxonomy.md) · [Benchmarks & analysis](analysis/README.md) · [Bibliography](references/README.md)**

</div>

Language models propose representations, candidates, and actions; symbolic solvers return answers, verdicts, counterexamples, or other structured feedback. This survey connects **solver families**, **the roles of their returned signals**, and **the scope of the resulting verification evidence**.

<p align="center">
  <img src="assets/figures/overview.png" alt="Language models interact with symbolic solvers; returned signals support five distinct roles." width="100%">
</p>

**1,301 included studies · 1,587 reports · 5 solver roles · 418 manuscript references**

## Solver evolution

A chronological view of selected **formal foundations**, **solver tools**, and **LLM–solver configurations** across ten solver families. Nodes are placed by the publication year of their cited report.

<a href="assets/figures/solver-evolution.png">
  <img src="assets/figures/solver-evolution.png" alt="Solver development tree with ten families, formal foundations and tools below, and recent LLM configurations above." width="100%">
</a>

[Open the development tree at full resolution](assets/figures/solver-evolution.png) · [Browse representative methods](docs/method-index.md)

## Explore the five solver roles

| Role | How the signal is used | Studies |
| --- | --- | --- |
| [R1 · Symbolic Solving](papers/roles/symbolic-solving.md) | Use the returned consequence, model, plan, or proof to construct an answer. | 559 |
| [R2 · Verification](papers/roles/verification.md) | Use the verdict to accept, reject, or qualify a candidate relative to an encoded obligation. | 931 |
| [R3 · Diagnosis and Repair](papers/roles/diagnosis-repair.md) | Use counterexamples, errors, or other diagnostic feedback to revise a candidate. | 512 |
| [R4 · Search Control](papers/roles/search-control.md) | Use solver signals to guide expansion, pruning, or selection during search. | 228 |
| [R5 · Learning Supervision](papers/roles/learning-supervision.md) | Use solver outcomes to construct or select training data, rewards, or learning targets. | 234 |

Roles overlap. The counts describe the confirmed corpus's stored role annotations, not disjoint method families or quality scores. [Unassigned labels](papers/roles/unassigned.md) remain explicit. For finer groupings, browse the [representative method index](docs/method-index.md).

## Resources

| Explore | What you will find |
| --- | --- |
| [Literature catalogue](papers/README.md) | Studies by solver role and citation year, with source links and stable IDs |
| [Taxonomy and verification boundaries](docs/taxonomy.md) | Role definitions, representative methods, and the scope of a successful check |
| [Benchmarks and protocols](analysis/benchmarks.md) | Task settings, solver-use configurations, and their source references |
| [Descriptive analysis](analysis/README.md) | Task and metric summaries, units, and coding provenance |
| [Bibliography](references/README.md) | Readable reference list and [BibTeX](references/references.bib) |
| [Data downloads](data/README.md) | [CSV](data/papers.csv), [JSON](data/papers.json), and the [data dictionary](data/schema.md) |

<details>
<summary><strong>Review scope and snapshot dates</strong></summary>

| Resource | Snapshot |
| --- | --- |
| Included corpus | **1,301 studies / 1,587 reports** |
| Eligibility classes | 1,129 core-method studies; 172 evaluation/diagnostic studies |
| Research eligibility | Earliest evaluable public report: **1 Jan 2020 – 31 Aug 2026** |
| Report versions used in the review | Available through **9 Oct 2026** |
| Manuscript bibliography | **418 cited entries**, including background and resources |
| First public companion release | **12 Oct 2026 · v0.1.0** |

The eligibility cutoff, actual search dates, and report-version cutoff describe different things. The first public release reuses existing records; it does not extend the literature search. See [methodology and limitations](docs/methodology.md).

</details>

## Updates and contributions

**2026-10-12:** Added the Solver development tree and refreshed the homepage navigation and paper-link entry. The initial corpus and bibliography are available in [v0.1.0](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/releases/tag/v0.1.0). [Change log](CHANGELOG.md).

Suggestions for new papers, version updates, and metadata or classification corrections are welcome through [Issues](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/issues/new/choose) or pull requests. Please include a public source and explain the relevant solver interaction. Suggestions are reviewed before entering a released corpus. See [contribution guidance](CONTRIBUTING.md) and the [maintenance policy](docs/maintenance.md).

## Citation and rights

Until a public paper citation is available, cite the companion repository and specify the release you used. GitHub's **Cite this repository** button reads [CITATION.cff](CITATION.cff).

<details>
<summary><strong>Companion repository BibTeX</strong></summary>

```bibtex
@misc{geng2026solvers_companion,
  author = {Yishuai Geng},
  title = {Solvers in the Loop: Survey Companion Repository},
  year = {2026},
  howpublished = {GitHub repository, version v0.1.0},
  url = {https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey}
}
```

</details>

Copyright is retained; no open-source or open-content license is granted at this stage. Bibliographic records identify works owned by their respective rights holders. See [LICENSE](LICENSE) and [figure credits](assets/README.md).

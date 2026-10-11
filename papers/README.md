# Literature catalogue

**1,301 included studies**, represented by 1,587 reports in the confirmed review corpus. Each row below identifies a study and links to its selected citation report where a source is recorded. Full author lists, identifiers and metadata are in [CSV](../data/papers.csv) / [JSON](../data/papers.json).

## Browse by solver role

| Role | Signal use | Studies |
| --- | --- | --- |
| [R1 · Symbolic Solving](roles/symbolic-solving.md) | Use the returned consequence, model, plan, or proof to construct an answer. | 559 |
| [R2 · Verification](roles/verification.md) | Use the verdict to accept, reject, or qualify a candidate relative to an encoded obligation. | 931 |
| [R3 · Diagnosis and Repair](roles/diagnosis-repair.md) | Use counterexamples, errors, or other diagnostic feedback to revise a candidate. | 512 |
| [R4 · Search Control](roles/search-control.md) | Use solver signals to guide expansion, pruning, or selection during search. | 228 |
| [R5 · Learning Supervision](roles/learning-supervision.md) | Use solver outcomes to construct or select training data, rewards, or learning targets. | 234 |

[59 studies without an assigned role](roles/unassigned.md). Roles overlap and cannot be summed.

## Browse by citation year

| Year | Studies |
| --- | --- |
| [2027](years/2027.md) | 2 |
| [2026](years/2026.md) | 584 |
| [2025](years/2025.md) | 460 |
| [2024](years/2024.md) | 185 |
| [2023](years/2023.md) | 56 |
| [2022](years/2022.md) | 10 |
| [2021](years/2021.md) | 2 |
| [2020](years/2020.md) | 2 |

## Reading the catalogue

- `core_method` and `evaluation_diagnostic` are eligibility classes, not quality scores.
- Role labels describe uses of solver signals; they are independent of engine families and task labels.
- Author-confirmed inclusion does not imply independent human verification of every metadata or coding field.
- 0 studies have no recoverable public source URL in the exported local metadata; these appear as plain text.
- The selected report can be later than the eligibility cutoff; see [methodology](../docs/methodology.md).

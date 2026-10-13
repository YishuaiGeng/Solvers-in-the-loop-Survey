# Benchmarks and analysis

[Benchmark guide](benchmarks.md) · [Literature catalogue](../papers/catalogue.md) · [Scope](../docs/methodology.md)

The benchmark guide groups representative resources by task solutions and formal models, checked-artifact construction, and correspondence/verification diagnostics. It distinguishes the resource's original publication from the paper documenting a solver-use configuration.

## Downloads and coverage

| File | Population | Unit |
| --- | --- | --- |
| [Corpus distributions](corpus-summary.csv) | Current 1,429-study catalogue | Distinct studies by year, class, role, and report type |
| [Extension distributions](catalogue-extension.csv) | 128 studies added in the September-window update | The same descriptive dimensions for the added cohort |
| [Task relevance](task-relevance-counts.csv) | Original 1,301-study analysis cohort | Distinct studies per task and relevance category |
| [Task × metric](task-by-scoped-metric.csv) | Original 1,301-study analysis cohort | Distinct studies per task and scoped metric dimension |

The two detailed task/metric tables have not been extended to the added 128 studies. Their coverage is explicit in [coverage.json](coverage.json); do not use 1,429 as their denominator. The current-corpus and extension distributions are generated directly from the released catalogue.

## Reading the results

Task labels, solver roles, relevance categories, and metric dimensions can overlap. Do not sum their cells to recover a population size. The extension includes boundary recoveries as well as September papers.

`core_evaluation` identifies an experimental relation to a task; it does not count every mention of a benchmark. The metric matrix uses qualifying core-evaluation, boundary-diagnostic, and solver-supervision-data relations. Transfer after training, supporting components, and unrelated background measurements remain outside that matrix.

The relevance annotations were produced as AI recommendations against stored evidence. Inclusion is author-confirmed; these are separate statuses. Counts describe recorded coverage, not performance, proof strength, or a finding that an unrecorded property was absent. These heterogeneous settings do not support a pooled effect or leaderboard.

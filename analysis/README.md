# Benchmarks and descriptive analysis

[Benchmark / protocol guide](benchmarks.md) · [Source data](benchmarks.json) · [Methodology](../docs/methodology.md)

The benchmark guide presents the manuscript's representative evaluation resources, grouped by task solutions and formal models, proof construction, and verification/interface diagnostics. It distinguishes resource-introduction references from papers demonstrating a solver-use configuration. It is not a leaderboard.

## Aggregate tables

| File | Row | Cell / unit |
| --- | --- | --- |
| [task-relevance-counts.csv](task-relevance-counts.csv) | One of eight task categories | Distinct study count per task and relevance category |
| [task-by-scoped-metric.csv](task-by-scoped-metric.csv) | One of eight task categories | Distinct study count per task and scoped metric dimension |

These are preserved numerical aggregates from the existing topic-relevance analysis. Re-encoding removes the UTF-8 BOM and normalizes newlines; numerical values are unchanged. **Task labels, relevance categories and metric dimensions can overlap.** Do not sum cells to estimate the number of studies or calculate an overall prevalence from them.

The task table distinguishes actual core evaluation, boundary diagnostics, solver-supervision data, transfer after solver supervision, supporting components, independent comparisons, ancillary experiments, background, and unclear relations. Its `core_evaluation` column counts studies with an identified core experimental relation to that task; it is not all studies mentioning a benchmark in that domain.

The metric matrix groups existing scoped measurements into twelve dimensions, including task correctness, formal validity, semantic fidelity, coverage and cost. It uses core-evaluation, boundary-diagnostic and solver-supervision-data relations with qualifying metric evidence. Supervision measurements do not become runtime guarantees; transfer, supporting-component and unrelated background measurements are outside this matrix. A study may contribute to several cells. Counts indicate recorded measurement coverage, not performance or strength of evidence.

## Interpretation limits

Underlying task/resource/metric relations were coded as AI recommendations against stored source evidence. They were not newly adjudicated by a human for this export, and they do not alter the confirmed 1,301-study eligibility population. The tables preserve that provenance. A zero or absent entry is not proof that a paper lacked the property; it describes the coded relation and evidence available in the analysis snapshot.

These tables summarize heterogeneous settings and should not be treated as pooled effects, rankings, or new experiments. For source fingerprints and dates, see [snapshot metadata](../data/snapshot.json).

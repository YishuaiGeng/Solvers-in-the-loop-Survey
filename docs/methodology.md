# Scope and interpretation

This companion accompanies *Symbolic Solvers for Verifiable Large Language Model Reasoning: A Survey*. It provides the literature catalogue, taxonomy, cited bibliography, illustrations, and descriptive analyses supporting the review.

## Review scope

A qualifying symbolic component operates on a declarative specification, answers a formal query or check, and supplies a result used by the language-model system or its evaluation. General code execution and ordinary unit testing alone do not establish a qualifying solver interaction.

The catalogue contains **1,459 studies / 1,745 reports**: **1,254 core-method studies** and **205 evaluation/diagnostic studies**. A catalogue row identifies one study and its selected report; versions of the same study are not independent studies.

| Date | Meaning |
| --- | --- |
| 1 January 2020–31 October 2026 | Eligibility window for the earliest assessable public report |
| 4 November 2026 | Latest author-confirmed corpus integration |
| 5 November 2026 | Current manuscript and companion refresh |

Source coverage varies by platform; the review window does not imply identical execution dates or a complete five-source rerun in every month. The catalogue preserves all previously released study identities and adds only author-confirmed inclusions. A selected citation report can postdate the eligibility window. Catalogue metadata follows the author-confirmed selected-report register; the bibliography follows the editions cited in the manuscript, which can differ in year or venue.

The [manuscript bibliography](../references/README.md) follows the current citation set. Changing a citation or a method placement affects the selected presentation; the confirmed eligibility catalogue retains the underlying study records.

The [search and selection figure](review-flow.md) reports the completed selection cohort and uses the same counts as the manuscript. Its 60,206 source records precede deduplication; the final corpus contains 1,745 reports of 1,459 studies.

## Classification and analysis

The five solver roles describe how a returned signal is consumed. Roles overlap and differ from solver families and task categories. Author-confirmed inclusion is separate from AI-assisted role annotations and analytical groupings; it does not imply independent human verification of every exported field.

Corpus and extension distributions cover the current catalogue. The two detailed task/metric tables retain their **1,301-study baseline**; the 158 subsequent additions are not included in those aggregates. Their relevance annotations remain AI recommendations. See [analysis coverage](../analysis/README.md) for units and interpretation.

A successful formal check concerns the encoded obligation and stated assumptions. It does not by itself establish semantic fidelity, complete coverage, or the correctness of later unchecked outputs. The summaries are descriptive, not pooled performance estimates or quality rankings.

## Data use

Study identities are retained across releases. Missing values remain explicit. Public source links and bibliographic metadata identify the recorded report versions; their continued online availability is not guaranteed by offline validation. Source fingerprints and release dates are in [snapshot metadata](../data/snapshot.json).

The released JSON reproduces the CSV and readable catalogues with the included renderer. Full texts, internal adjudication records, writing notes, and the draft manuscript are not part of this companion. Corrections and new-paper suggestions can be submitted through [Issues](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/issues/new/choose).

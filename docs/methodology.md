# Scope, dates, and limitations

The first companion release reuses the confirmed corpus and current manuscript assets. It performs no new literature search, downloads no full texts, and changes no eligibility decisions.

## Three distinct dates

| Date | Meaning |
| --- | --- |
| 2020-01-01 to 2026-08-31 | Eligibility window, based on the earliest evaluable public report of a study |
| 2026-09-09 and 2026-09-10 | Main historical search dates and the final historical arXiv search, respectively |
| 2026-10-09 | Report-version availability cutoff used in the review synthesis |

A study first eligible before September can be represented by a later report version. Citation year and publication status therefore cannot be used to reconstruct eligibility dates. The public release date is a fourth date: it records publication of these companion materials, not a search update.

## Population and classification

The confirmed corpus comprises **1,301 studies / 1,587 reports**: 1,129 `core_method` studies and 172 `evaluation_diagnostic` studies. Public catalogue rows represent studies, with one selected citation report per row. The manuscript reference library has a different purpose: its cited entries also include foundations, datasets, tools and related surveys.

R1–R5 describe how a solver signal is consumed. Engine families, task categories, and roles are different axes. Roles can overlap within one study; unresolved and inapplicable role annotations remain explicit. A diagnostic paper associated with a role does not automatically instantiate a deployed method in that role.

The initial catalogue's inclusion and eligibility classes come from the author-confirmed final study snapshot. Bibliography and report versions come from its citation-version snapshot, with source-link fallback by exact report ID from existing catalogues. Key associations and representative method placements are retained from the manuscript's registers. These layers were not subjected to a new independent human audit for this export.

The cited-reference set is frozen from a committed manuscript snapshot, identified in `data/snapshot.json`, so ongoing writing edits cannot change it mid-export. Citation metadata are preserved as recorded, including two 2027 bibliographic years in the local citation-version snapshot. These are not treated as evidence of first public availability in 2027; the year fields have not been reverified for this release.

## Analysis provenance

The task and metric tables are existing descriptive aggregates derived from the review's relevance coding. Their underlying relevance annotations were produced as **AI recommendations**, without changing author-confirmed inclusion. They are published with that status, not relabeled as independent human coding. Their units and exclusions are explained in [analysis notes](../analysis/README.md).

No pooled performance estimate, new experimental result, search-completeness claim, or quality ranking is created by these tables. Positive formal checks concern their encoded obligations; they do not alone demonstrate semantic fidelity to an intended task.

## Access and reproducibility

The public files contain selected metadata, classification derivatives, illustrations, and aggregate analysis. Copyrighted full texts, raw database exports, internal review records and the draft manuscript are outside this release. Source fingerprints identify the snapshots used. The public renderer reproduces CSV and Markdown views from released JSON, and validation checks data contracts, links, generated views and file fingerprints. It cannot reproduce the entire private screening and extraction process.

Broken source links, missing metadata and version ambiguities can be reported through an issue. External destinations were not revalidated for this release, so link format checks do not guarantee ongoing availability.

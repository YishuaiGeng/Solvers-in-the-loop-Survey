# Public data dictionary

`papers.json` is the editable public catalogue. `papers.csv` is generated from it with identical rows, ordered by stable study ID. UTF-8 is used throughout; semicolons join arrays in CSV. A row represents a **study**, and its `report_id` identifies the selected citation report. It does not enumerate every report of that study.

| Field | Type / allowed values | Meaning |
| --- | --- | --- |
| `study_id` | Unique `STUDY-*` string | Stable identity retained from the confirmed corpus |
| `report_id` | `RPT-*` or `SEP26-ARXIV-*` string | Selected report identity |
| `title`, `authors` | Nonempty string | Citation-version metadata; full authors retained |
| `year` | Integer | Selected report's citation year; not its eligibility date |
| `venue` | String or `not_reported` | Venue recorded in the source metadata |
| `doi`, `arxiv_id` | Identifier or `not_reported` | Identifiers of the citation version |
| `url` | Public HTTP(S) URL or `not_reported` | Recorded source, DOI resolver, or arXiv abstract page |
| `url_basis` | See below | How the source link was obtained |
| `literature_class` | `core_method`, `evaluation_diagnostic` | Author-confirmed eligibility classification |
| `solver_roles` | Array of `R1`–`R5` | Stored, overlapping annotations of signal use |
| `role_status` | `classified`, `unclear`, `not_applicable` | Distinguishes assigned roles from unresolved/inapplicable labels |
| `report_type` | `publication`, `preprint` | Recorded report type; not a fresh online verification |
| `bibtex_keys` | Array of strings | Existing key-register associations; aliases can map to multiple studies |
| `record_version` | Positive integer | Public record revision; increment on substantive correction |

`url_basis` is one of `citation_version`, `citation_doi`, `citation_arxiv`, `canonical_report_catalogue`, `canonical_report_library`, or `not_reported`. Fallback links are joined by exact report ID, not by a title-similarity guess. A fallback source can identify a related report version; consult the identifiers before selecting a version to cite. Missing metadata and URLs are preserved, never manufactured.

`snapshot.json` records the eligibility window, evidence-version date, counts, and SHA-256 fingerprints of local source snapshots under semantic names. Those hashes identify the inputs; they do not make private source ledgers publicly reconstructible. `release-manifest.json` fingerprints every released file except itself.

`taxonomy-methods.json` is a separate placement table: `role`, `grouping_axis`, `direction`, `method`, `bibtex_key`, `study_id`, `report_id`, and `label_type`. It preserves the manuscript's analytical grouping. Multiple rows may concern one study, role names are spelled out, and historical section numbers are omitted. It is not a second eligibility ledger.

Bibliographic and classification metadata are derivatives of existing records. Formal inclusion was confirmed by the author; this does not imply human verification of every exported annotation. [Methodology](../docs/methodology.md) documents the distinction.

The initial 1,301 study IDs remain unchanged. Added studies use `STUDY-SEP26-<arXiv ID>`, a stable companion ID derived from the approved report's unversioned arXiv identity; report IDs preserve `SEP26-ARXIV-<arXiv ID>v<version>` from the source records. This naming does not merge studies.

`analysis/coverage.json` identifies the added cohort and the baseline population of the detailed task/metric tables. Catalogue years use the author-confirmed selected-report metadata; bibliography years use the cited editions and may differ.

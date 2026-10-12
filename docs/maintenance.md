# Literature and release maintenance

The public repository tracks released companion material. Its initial release preserves a confirmed review baseline; incoming suggestions are discussed in Issues until evidence review supports a release change.

## Supported update types

| Update | Required evidence | Effect |
| --- | --- | --- |
| Metadata correction | Public source and exact field / version | Correct the record; retain its identity |
| New report version | Source link and explicit relation to an existing study | Link versions; select the citation version deliberately |
| Classification correction | Solver interaction and page / section supporting the proposed label | Review the source coding and affected discussion |
| New study suggestion | Actual source, eligibility date and relevant solver mechanism | Treat as a candidate until eligibility review is complete |
| Corpus-window extension | Explicit maintainer-started update with a protocol and dates | Review and synthesize new evidence before changing the released population |

## Review and publication

1. Record the suggestion and its source in an issue; do not fabricate missing metadata or claim full-text review from an abstract.
2. Reconcile study/report identity with the existing corpus. Keep raw evidence and review events in the research records; only approved derivatives belong in the public release.
3. Verify the affected fields against an identified report version and source locator. Separate author claims, experimental evidence and the review's analysis. AI recommendations remain recommendations until the required author decision occurs.
4. For a corpus update, reassess the affected synthesis, task counts, taxonomy, citations and manuscript statements together. A monthly paper list alone is not a revised review.
5. Prepare an update branch and a concrete public diff. Preserve stable IDs; record corrections, withdrawals and merges in the change ledger with before/after values. Retain superseded release history.
6. Run rendering, validation and tests. Review the changed sources and aggregate units; automated checks cannot decide eligibility or verify substantive claims.
7. Merge after maintainer review, update `CHANGELOG.md`, and create a dated or semantic release tag. Do not rewrite published tags. Record separate eligibility, search, evidence-version and release dates.

No automated literature searches or unattended inclusion decisions are enabled by this repository. No source API, full-text collection or website deployment is part of its validation workflow.

## Updating paper links

Maintain public paper destinations in [`manuscript/links.json`](../manuscript/links.json). Use `not_reported` until a verified URL exists. Set `status` to `in_preparation`, `preprint`, or `published` as appropriate, and fill `arxiv_url`, `pdf_url`, and/or `doi_url` with the actual public destinations. Never guess an arXiv ID or DOI.

Run `python3 -B scripts/render.py --refresh-manifest` and `python3 -B scripts/validate.py` after editing. The homepage's paper links and status, its citation guidance, and the manuscript page update together. For a paper release, also add the verified paper citation to `CITATION.cff` and update the change log.

## Repository design references

The organization was informed by [RUCAIBox/LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) (illustrated overview, topic navigation and update log) and [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) (taxonomy-aligned paper lists and citation entry). Their prose, data, code and figures were not copied. This repository uses its own corpus and solver-role framework.

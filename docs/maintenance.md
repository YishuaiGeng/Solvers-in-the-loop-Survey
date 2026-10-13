# Maintaining the paper lists

Routine updates are reviewed and committed to `main`. Git history records each change; a new Release or version number is not required for every paper, correction, or documentation edit.

## Papers and corrections

Suggestions arrive through [Issues](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/issues/new/choose). Include a public source, the relevant study ID when known, and a page or section supporting a classification correction. A suggestion remains a candidate until reviewed.

Preserve stable study/report identities and missing-value statuses. Inclusion, identity merges and substantive reclassification require maintainer review against the underlying evidence. Metadata corrections do not automatically extend the eligibility window. Keep original evidence and review events in the research records; publish approved metadata and summaries here.

## Updating the repository

1. Edit the relevant JSON or documentation. The homepage template is `scripts/README.template`; full lists are generated from `data/papers.json`.
2. Keep the homepage concise: introduce the survey, show its overview and development figures, and link to the paper indexes. Do not add selected paper lists to the homepage. The method index preserves the existing taxonomy placements and links them to the cited paper records.
3. For a changed study record, increment `record_version` and append its before/after values to `data/changes.csv`. Presentation-only changes leave those records unchanged.
4. Run the renderer, validation, and tests, inspect the diff, then commit the reviewed update.

```sh
python3 -B scripts/render.py --refresh-manifest
python3 -B scripts/validate.py
python3 -B -m unittest discover -s tests
```

The CSV and readable lists reproduce the released metadata. Automated checks verify structure and consistency; they do not decide eligibility, establish scientific correctness, or enable literature searches.

## Paper links and fixed snapshots

Store verified paper destinations in [`manuscript/links.json`](../manuscript/links.json), using `not_reported` until an actual URL exists. Regeneration updates the homepage and manuscript page together. Add the formal paper citation when it becomes public.

A tagged snapshot is useful alongside an arXiv posting, formal publication, or a specifically cited dataset. It is optional for ordinary maintenance. Keep existing tags and releases unchanged. `data/snapshot.json` and the version in `CITATION.cff` identify the retained data snapshot; routine presentation edits are identified by their commits. When a new data snapshot is needed, update its counts, dates, citation metadata and change notes consistently.

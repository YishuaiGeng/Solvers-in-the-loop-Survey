# Contributing

Thank you for helping maintain this survey companion. Use an [issue form](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/issues/new/choose) to suggest a paper, report a new version, correct metadata, or discuss a classification.

Include a public paper URL/DOI/arXiv identifier, the relevant stable study ID if known, and a short explanation with a section or page locator. For classification suggestions, identify the formal object, the solver query or check, and how the returned signal is consumed. Distinguish what the paper claims from what its evidence establishes. Please link to lawfully accessible material rather than attaching copyrighted full texts.

New suggestions remain candidates until reviewed. They do not automatically change the confirmed corpus or its eligibility cutoff. Inclusion, identity merges and substantive reclassification require the maintainer's review against the underlying evidence. This repository's automated checks verify structure and release consistency, not research truth.

## Proposing a change

1. Open an issue describing the source and proposed correction, or reference an existing issue in a pull request.
2. Edit the relevant JSON source or documentation. Preserve stable study/report IDs. Do not hand-edit generated CSV or catalogue Markdown.
3. Increment the affected `record_version` and append an entry to `data/changes.csv` for record changes. Explain before/after values and evidence. Do not silently remove or merge studies.
4. Update counts and descriptions when their underlying data change. Routine updates are committed to `main`; no new Release is required. Reserve tagged snapshots for a paper posting, publication, or specifically cited dataset. A metadata-only correction need not advance eligibility dates.
5. Regenerate and check locally with Python 3.10 or newer:

```sh
python3 -B scripts/render.py --refresh-manifest
python3 -B scripts/validate.py
python3 -B -m unittest discover -s tests
```

The maintainer will review the public diff, source evidence and CI results before merging. Keep proposed evidence and discussion in the issue; publish only approved metadata, classifications and summaries. See the [maintenance policy](docs/maintenance.md).

#!/usr/bin/env python3
"""Render public catalogues from the released JSON; Python 3.10+, stdlib only."""
import argparse
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ROLES = {
    'R1': ('symbolic-solving', 'Symbolic Solving', 'Use the returned consequence, model, plan, or proof to construct an answer.'),
    'R2': ('verification', 'Verification', 'Use the verdict to accept, reject, or qualify a candidate relative to an encoded obligation.'),
    'R3': ('diagnosis-repair', 'Diagnosis and Repair', 'Use counterexamples, errors, or other diagnostic feedback to revise a candidate.'),
    'R4': ('search-control', 'Search Control', 'Use solver signals to guide expansion, pruning, or selection during search.'),
    'R5': ('learning-supervision', 'Learning Supervision', 'Use solver outcomes to construct or select training data, rewards, or learning targets.'),
}
FIELDS = ['study_id','report_id','title','authors','year','venue','doi','arxiv_id','url','url_basis',
          'literature_class','solver_roles','role_status','report_type','bibtex_keys','record_version']


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def md(s):
    return str(s).replace('\n',' ').replace('|','\\|').replace('[','\\[').replace(']','\\]').replace('<','&lt;').replace('>','&gt;').replace('*','\\*').replace('_','\\_')


def source_link(title, url):
    return md(title) if url == 'not_reported' else '[' + md(title) + '](<' + url.replace('>','%3E').replace('<','%3C') + '>)'


def short_authors(s):
    names = s.split(';') if ';' in s else s.split(' and ')
    return '; '.join(names[:3]) + (' et al.' if len(names) > 3 else '')


def paper_list(papers):
    sections = []
    for label, category in [('Core methods', 'core_method'),
                            ('Evaluation and diagnostic studies', 'evaluation_diagnostic')]:
        subset = [p for p in papers if p['literature_class'] == category]
        if not subset:
            continue
        lines = ['## ' + label, '']
        for p in sorted(subset, key=lambda p:(-p['year'],p['title'].casefold(),p['study_id'])):
            lines.append(f"- {source_link(p['title'],p['url'])} ({p['year']}) — {md(short_authors(p['authors']).rstrip('.'))}.")
        sections.append('\n'.join(lines))
    return '\n\n'.join(sections) + '\n'


def classified_paper_list(methods, refs):
    by_key = {r['key']: r for r in refs}
    groups = defaultdict(lambda: defaultdict(list))
    for method in methods:
        groups[method['role']][method['direction']].append(method)
    unique = len({m['bibtex_key'] for m in methods})
    lines = ['# Paper list', '',
        '[Repository home](../README.md) · [Full catalogue](catalogue.md) · [All manuscript references](../references/README.md) · [Method index](../docs/method-index.md)', '',
        f"Papers organized by the survey's five solver roles and subcategories: **{len(methods)} method placements**, corresponding to **{unique} distinct cited papers**. "
        'A paper can appear in several groups. Titles and years follow the manuscript-cited edition.', '',
        'Use **Ctrl+F / ⌘F** to find a title, author or method. Follow a title or source badge to its recorded paper link. '
        'The [full catalogue](catalogue.md) provides all included studies by role and year.', '',
        ' · '.join(f'[{name}](#{name.lower().replace(" ", "-")})' for _,name,_ in ROLES.values()), '']
    for _, name, definition in ROLES.values():
        lines += ['## '+name, '', definition, '']
        for direction, entries in groups[name].items():
            lines += ['### '+direction, '']
            for method in entries:
                ref = by_key[method['bibtex_key']]
                names = ref['authors'].split(';') if ';' in ref['authors'] else ref['authors'].split(' and ')
                author = names[0].strip() + (' et al.' if len(names)>1 else '')
                url = ref['url']
                host = urlsplit(url).hostname if url!='not_reported' else ''
                label, color = ('arXiv', 'b31b1b') if host in ('arxiv.org','www.arxiv.org') else ('DOI','286b75') if host in ('doi.org','dx.doi.org') else ('Paper','286b75')
                if url == 'not_reported':
                    label, color = 'Reference', '64748b'
                    url = '../references/README.md#'+ref['key']
                year = str(ref['year']) if ref['year']!='not_reported' else 'year not reported'
                badge_url = 'https://img.shields.io/badge/'+label+'-'+quote(year.replace('-','--'),safe='')+'-'+color+'?style=flat-square'
                badge = f'[![{label} · {md(year)}]({badge_url})](<{url}>)'
                lines.append(f"- **{source_link(ref['title'],ref['url'])}**, {md(author)} {badge} <sub>{md(method['method'])}</sub>")
            lines.append('')
    return '\n'.join(lines)


def render():
    papers, snap = load('data/papers.json'), load('data/snapshot.json')
    refs, methods = load('references/references.json'), load('data/taxonomy-methods.json')
    outputs = {'papers/README.md': classified_paper_list(methods,refs)}
    buf = io.StringIO(newline='')
    writer = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator='\n')
    writer.writeheader()
    writer.writerows({k:';'.join(p[k]) if isinstance(p[k],list) else p[k] for k in FIELDS} for p in papers)
    outputs['data/papers.csv'] = buf.getvalue()

    role_rows = []
    for role, (slug,name,definition) in ROLES.items():
        subset = [p for p in papers if role in p['solver_roles']]
        role_rows.append(f'| [{role} · {name}](papers/roles/{slug}.md) | {definition} | {len(subset):,} |')
        outputs[f'papers/roles/{slug}.md'] = (f'# {role} · {name}\n\n'
            f'[All papers](../catalogue.md) · [Taxonomy](../../docs/taxonomy.md) · [CSV metadata](../../data/papers.csv)\n\n'
            f'{definition}\n\n![{name}](../../assets/figures/{slug}.png)\n\n'
            f'{len(subset):,} studies in the confirmed corpus snapshot. Role assignments overlap; '
            'a diagnostic study carrying a role label is not thereby a deployed method.\n\n' + paper_list(subset))
    years = sorted({p['year'] for p in papers}, reverse=True)
    year_rows = []
    for year in years:
        subset = [p for p in papers if p['year']==year]
        year_rows.append(f'| [{year}](years/{year}.md) | {len(subset):,} |')
        outputs[f'papers/years/{year}.md'] = (f'# Citation year {year}\n\n[All papers](../catalogue.md)\n\n'
            'Citation year describes the selected report, not the earliest eligible report. '
            '[Full metadata](../../data/papers.csv).\n\n' + paper_list(subset))
    other = [p for p in papers if not p['solver_roles']]
    outputs['papers/roles/unassigned.md'] = ('# Studies without an assigned R1–R5 label\n\n'
        '[All papers](../catalogue.md)\n\n'
        '`unclear` and `not_applicable` are preserved in the [metadata](../../data/papers.csv); they are not negative findings.\n\n' + paper_list(other))
    outputs['papers/catalogue.md'] = ('# Literature catalogue\n\n'
        '[Classified paper list](README.md) · [Repository home](../README.md)\n\n'
        f"**{len(papers):,} included studies**, represented by {snap['reports']:,} reports in the confirmed review corpus. "
        'Browse the paper lists by solver role or citation year. Each entry links to its selected report where a source is recorded. '
        'Full author lists, identifiers and metadata are in [CSV](../data/papers.csv) / [JSON](../data/papers.json).\n\n'
        'For a method named in the survey, use the [methods → papers index](../docs/method-index.md). '
        'For a manuscript citation, use the [reference index](../references/README.md). '
        'Search an index page with **Ctrl+F / ⌘F**, or download the CSV to filter the full catalogue by title, author, year or role.\n\n'
        '## Browse by solver role\n\n| Role | Signal use | Studies |\n| --- | --- | --- |\n' +
        '\n'.join(row.replace('](papers/roles/','](roles/') for row in role_rows) + '\n\n'
        f'[{len(other)} studies without an assigned role](roles/unassigned.md). Roles overlap and cannot be summed.\n\n'
        '## Browse by citation year\n\n| Year | Studies |\n| --- | --- |\n' + '\n'.join(year_rows) + '\n\n'
        '## Reading the catalogue\n\n'
        '- `core_method` and `evaluation_diagnostic` are eligibility classes, not quality scores.\n'
        '- Role labels describe uses of solver signals; they are independent of engine families and task labels.\n'
        '- Author-confirmed inclusion does not imply independent human verification of every metadata or coding field.\n'
        f"- {snap['missing_source_links']} studies have no recoverable public source URL in the exported local metadata; these appear as plain text.\n"
        '- The selected report can be later than the eligibility cutoff; see [methodology](../docs/methodology.md).\n')

    coverage = load('analysis/coverage.json')
    added_ids = set(coverage['extension_study_ids'])
    added = [p for p in papers if p['study_id'] in added_ids]
    outputs['papers/updates/2026-09.md'] = ('# Papers added in the September-window update\n\n'
        '[All papers](../catalogue.md) · [Scope](../../docs/methodology.md)\n\n'
        f'{len(added)} author-confirmed additions. This cohort includes boundary recoveries; '
        'it is not restricted to studies first made public in September. Role annotations overlap.\n\n' + paper_list(added))
    outputs['papers/catalogue.md'] += f'\n[Browse the {len(added)} studies added in this update](updates/2026-09.md).\n'
    for filename, cohort in [('corpus-summary.csv', papers), ('catalogue-extension.csv', added)]:
        buf = io.StringIO(newline='')
        writer = csv.writer(buf, lineterminator='\n')
        writer.writerow(['dimension', 'category', 'studies'])
        writer.writerow(['population', 'all_studies', len(cohort)])
        for field in ['year', 'literature_class', 'role_status', 'report_type']:
            for category, count in sorted(Counter(str(p[field]) for p in cohort).items()):
                writer.writerow([field, category, count])
        for role, count in sorted(Counter(r for p in cohort for r in p['solver_roles']).items()):
            writer.writerow(['solver_role', role, count])
        outputs['analysis/' + filename] = buf.getvalue()

    links = load('manuscript/links.json')
    link_labels = [('arxiv_url','arXiv'),('pdf_url','Paper PDF'),('doi_url','Publication / DOI')]
    paper_links = [f'[{label}](<{links[key]}>)' for key,label in link_labels if links[key]!='not_reported']
    paper_status = {
        'in_preparation':'Manuscript in preparation · Public paper links will be added when available.',
        'preprint':'Preprint available · See the paper links above for the current public version.',
        'published':'Published paper · See the paper links above for the publication and available versions.',
    }[links['status']]
    paper_nav = ' · '.join(paper_links) if paper_links else 'Paper link forthcoming · [Manuscript information](manuscript/README.md)'
    citation_status = ('A paper citation will be added when the manuscript is public. For now, you can cite this companion repository.'
        if not paper_links else 'Please cite the survey using its public paper record. The companion repository can be cited separately when using its catalogue or data.')
    manuscript = ['# Manuscript','',
        '**Symbolic Solvers for Large Language Model Reasoning: A Survey**','',
        'Yishuai Geng, Guohui Xiao, Guilin Qi, Tianxing Wu, Huajun Chen, and Haofen Wang.','',paper_status,'']
    if paper_links:
        manuscript += [' · '.join(paper_links),'']
    else:
        manuscript += ['The manuscript PDF and a verified arXiv or publication link will be added after finalization or public posting.','']
    manuscript += [citation_status,'',
        'Repository citation: [CITATION.cff](../CITATION.cff). Manuscript references: [bibliography](../references/README.md).','']
    outputs['manuscript/README.md'] = '\n'.join(manuscript)

    template = (ROOT/'scripts/README.template').read_text(encoding='utf-8')
    for key,val in {'ROLE_ROWS':'\n'.join(role_rows),'STUDIES':f'{len(papers):,}','STUDIES_RAW':str(len(papers)),'VERSION':snap['version'],
                    'REPORTS':f"{snap['reports']:,}",'REFERENCES':str(len(refs)),
                    'CORE':f"{snap['literature_classes']['core_method']:,}",
                    'DIAGNOSTIC':str(snap['literature_classes']['evaluation_diagnostic']),
                    'PAPER_LINKS':paper_nav,'PAPER_STATUS':paper_status,'CITATION_STATUS':citation_status}.items():
        template = template.replace('@'+key+'@',val)
    outputs['README.md'] = template
    ref_lookup = {r['key']:r for r in refs}
    ref_lines = ['# Manuscript references','', '[BibTeX](references.bib) · [JSON](references.json) · [Methods → papers](../docs/method-index.md) · [Included studies](../papers/catalogue.md)', '',
        'Use **Ctrl+F / ⌘F** to find a paper title, author or citation key. Follow a linked title to its recorded source.', '',
        f'{len(refs)} entries cited by the current manuscript snapshot. This includes background, resources and related surveys, '
        f"so it differs from the {len(papers):,}-study eligibility corpus. An absent study link does not establish exclusion.", '',
        'Bibliographic fields are exported from the manuscript library; study associations use retained key mappings and exact arXiv identifiers. '
        'Aliases can map to several study IDs and are preserved without merging. Online availability and publication status have not been rechecked for this release.', '']
    for r in refs:
        ref_lines += [f'<a id="{r["key"]}"></a>', f'**{r["key"]}** · {source_link(r["title"],r["url"])}', '',
            f'{md(r["authors"])}. {md(r["year"])}. {md(r["venue"])}.', '',
            ('Study IDs: ' + ', '.join('`'+s+'`' for s in r['study_ids']) if r['study_ids'] else 'Study association: `not_reported`.'), '']
    outputs['references/README.md'] = '\n'.join(ref_lines)

    def ref_link(key):
        return f'[{md(key)}](../references/README.md#{key})' if key in ref_lookup else md(key)
    mlines = ['# Methods and papers','', '[Role definitions](taxonomy.md) · [Manuscript references](../references/README.md) · [Full catalogue](../papers/catalogue.md)', '',
        'Use **Ctrl+F / ⌘F** to find a method name or paper title. A paper title links to its recorded source; '
        'a method name links to the full reference entry.', '',
        'Names and categories follow the manuscript taxonomy. A study may appear in several categories. '
        'Titles and years describe the manuscript-cited edition; the catalogue can select a different report. '
        'Study/report identities and grouping axes remain in [taxonomy metadata](../data/taxonomy-methods.json).', '',
        '| Method | Role / category | Paper | Year |', '| --- | --- | --- | --- |']
    for m in methods:
        ref = ref_lookup[m['bibtex_key']]
        method_link = f"[{md(m['method'])}](../references/README.md#{m['bibtex_key']})"
        mlines.append('| ' + ' | '.join([method_link, md(m['role'] + ' · ' + m['direction']),
                      source_link(ref['title'],ref['url']), md(ref['year'])]) + ' |')
    outputs['docs/method-index.md'] = '\n'.join(mlines) + '\n'
    blines = ['# Benchmarks and protocols','', '[Analysis notes](README.md) · [References](../references/README.md)', '',
        'Representative resources from the manuscript evaluation table. The solver column describes a documented use configuration; '
        'it does not assert that the resource requires that solver. Resource-introduction citations and configuration-use citations are kept separate.', '']
    groups = defaultdict(list)
    for b in load('analysis/benchmarks.json'):
        groups[b['part']].append(b)
    for part, items in groups.items():
        blines += ['## '+part, '', '| Benchmark / protocol | Task | Solver / reference | Evaluation target |', '| --- | --- | --- | --- |']
        for b in items:
            title = md(b['name']) + ' ' + ', '.join(ref_link(k) for k in b['citations'])
            protocols = '; '.join(md(p['text']) + ' ' + ', '.join(ref_link(k) for k in p['citations']) for p in b['protocols'])
            blines.append(f"| {title} | {md(b['category'])} | {protocols} | {md(b['modality'])} |")
        blines.append('')
    outputs['analysis/benchmarks.md'] = '\n'.join(blines)
    return outputs


def manifest():
    files = {}
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or any(part in ('.git','__pycache__') for part in p.relative_to(ROOT).parts):
            continue
        if p.name == 'release-manifest.json':
            continue
        files[p.relative_to(ROOT).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return {'version':load('data/snapshot.json')['version'], 'files':files}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--refresh-manifest',action='store_true')
    args = parser.parse_args()
    if args.check and args.refresh_manifest:
        parser.error('--check is read-only')
    stale = []
    for name,content in render().items():
        path = ROOT/name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8')
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    if args.refresh_manifest:
        (ROOT/'release-manifest.json').write_text(json.dumps(manifest(),indent=2)+'\n',encoding='utf-8')
    print('Generated catalogue check passed.' if args.check else 'Rendered catalogues.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Render public catalogues from the released JSON; Python 3.10+, stdlib only."""
import argparse
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from pathlib import Path

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


def table(papers):
    lines = ['| Year | Study | Authors | Roles / status | Class |', '| --- | --- | --- | --- | --- |']
    for p in sorted(papers, key=lambda p:(-p['year'],p['title'].casefold(),p['study_id'])):
        roles = ', '.join(p['solver_roles']) or p['role_status']
        lines.append(f"| {p['year']} | {source_link(p['title'],p['url'])}<br><sub>{p['study_id']}</sub> | {md(short_authors(p['authors']))} | {roles} | {p['literature_class']} |")
    return '\n'.join(lines) + '\n'


def render():
    papers, snap = load('data/papers.json'), load('data/snapshot.json')
    refs, methods = load('references/references.json'), load('data/taxonomy-methods.json')
    outputs = {}
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
            f'[All papers](../README.md) · [Taxonomy](../../docs/taxonomy.md)\n\n'
            f'{definition}\n\n![{name}](../../assets/figures/{slug}.png)\n\n'
            f'{len(subset):,} studies in the confirmed corpus snapshot. Role assignments overlap; '
            'a diagnostic study carrying a role label is not thereby a deployed method.\n\n' + table(subset))
    years = sorted({p['year'] for p in papers}, reverse=True)
    year_rows = []
    for year in years:
        subset = [p for p in papers if p['year']==year]
        year_rows.append(f'| [{year}](years/{year}.md) | {len(subset):,} |')
        outputs[f'papers/years/{year}.md'] = (f'# Citation year {year}\n\n[All papers](../README.md)\n\n'
            'Citation year describes the selected report, not the earliest eligible report.\n\n' + table(subset))
    other = [p for p in papers if not p['solver_roles']]
    outputs['papers/roles/unassigned.md'] = ('# Studies without an assigned R1–R5 label\n\n'
        '[All papers](../README.md)\n\n'
        '`unclear` and `not_applicable` are preserved from the source snapshot; they are not negative findings.\n\n' + table(other))
    outputs['papers/README.md'] = ('# Literature catalogue\n\n'
        f"**{len(papers):,} included studies**, represented by {snap['reports']:,} reports in the confirmed review corpus. "
        'Each row below identifies a study and links to its selected citation report where a source is recorded. '
        'Full author lists, identifiers and metadata are in [CSV](../data/papers.csv) / [JSON](../data/papers.json).\n\n'
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

    links = load('manuscript/links.json')
    link_labels = [('arxiv_url','arXiv'),('pdf_url','Paper PDF'),('doi_url','Publication / DOI')]
    paper_links = [f'[{label}](<{links[key]}>)' for key,label in link_labels if links[key]!='not_reported']
    paper_status = {
        'in_preparation':'Manuscript in preparation · Public paper links will be added when available.',
        'preprint':'Preprint available · See the paper links above for the current public version.',
        'published':'Published paper · See the paper links above for the publication and available versions.',
    }[links['status']]
    paper_nav = ' · '.join(paper_links + ['[Paper status](manuscript/README.md)',
        '[Latest release](https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey/releases/latest)'])
    citation_status = ('Until a public paper citation is available, cite the companion repository and specify the release you used.'
        if not paper_links else 'For the paper, use the citation provided by its public record. For companion data and resources, also cite this repository and specify the release used.')
    manuscript = ['# Manuscript','',
        '**Solvers in the Loop: A Survey of Verifiable Neuro-Symbolic Reasoning with Large Language Models**','',
        'Yishuai Geng, Guohui Xiao, Guilin Qi, Huajun Chen, and Haofen Wang.','',paper_status,'']
    if paper_links:
        manuscript += [' · '.join(paper_links),'']
    else:
        manuscript += ['The manuscript PDF and a verified arXiv or publication link will be added after finalization or public posting.','']
    manuscript += [citation_status,'',
        'Repository citation: [CITATION.cff](../CITATION.cff). Manuscript references: [bibliography](../references/README.md).','']
    outputs['manuscript/README.md'] = '\n'.join(manuscript)

    template = (ROOT/'scripts/README.template').read_text(encoding='utf-8')
    for key,val in {'ROLE_ROWS':'\n'.join(role_rows),'STUDIES':f'{len(papers):,}',
                    'REPORTS':f"{snap['reports']:,}",'REFERENCES':str(len(refs)),
                    'CORE':f"{snap['literature_classes']['core_method']:,}",
                    'DIAGNOSTIC':str(snap['literature_classes']['evaluation_diagnostic']),
                    'PAPER_LINKS':paper_nav,'PAPER_STATUS':paper_status,'CITATION_STATUS':citation_status}.items():
        template = template.replace('@'+key+'@',val)
    outputs['README.md'] = template
    ref_lookup = {r['key']:r for r in refs}
    ref_lines = ['# Manuscript references','', '[BibTeX](references.bib) · [JSON](references.json) · [Included studies](../papers/README.md)', '',
        f'{len(refs)} entries cited by the current manuscript snapshot. This includes background, resources and related surveys, '
        'so it differs from the 1,301-study eligibility corpus. An absent study link does not establish exclusion.', '',
        'Bibliographic fields are exported from the manuscript library; study associations come from the existing key register. '
        'Aliases can map to several study IDs and are preserved without merging. Online availability and publication status have not been rechecked for this release.', '']
    for r in refs:
        ref_lines += [f'<a id="{r["key"]}"></a>', f'**{r["key"]}** · {source_link(r["title"],r["url"])}', '',
            f'{md(r["authors"])}. {md(r["year"])}. {md(r["venue"])}.', '',
            ('Study IDs: ' + ', '.join('`'+s+'`' for s in r['study_ids']) if r['study_ids'] else 'Study association: `not_reported`.'), '']
    outputs['references/README.md'] = '\n'.join(ref_lines)

    def ref_link(key):
        return f'[{md(key)}](../references/README.md#{key})' if key in ref_lookup else md(key)
    mlines = ['# Taxonomy method index','', '[Role definitions](taxonomy.md) · [Literature catalogue](../papers/README.md)', '',
        'Representative method placements from the manuscript taxonomy source. A study may have multiple placements; '
        'these rows are analytical groupings, not a performance ranking. Names and associations are retained from the source map.', '',
        '| Role | Grouping axis | Direction | Method | Reference | Study |', '| --- | --- | --- | --- | --- | --- |']
    for m in methods:
        mlines.append('| ' + ' | '.join([md(m[k]) for k in ('role','grouping_axis','direction','method')] +
                      [ref_link(m['bibtex_key']), '`'+m['study_id']+'`']) + ' |')
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

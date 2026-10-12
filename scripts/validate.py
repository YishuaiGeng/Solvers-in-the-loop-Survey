#!/usr/bin/env python3
"""Validate the public release offline, without third-party Python packages."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

from render import FIELDS, ROLES, ROOT, load, manifest, render


class ValidationError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise ValidationError(message)


def valid_url(url):
    if url == 'not_reported':
        return True
    try:
        u = urlsplit(url)
        return bool(u.scheme in ('http','https') and u.hostname and not u.username and not u.password
                    and not re.search(r'(?i)(token|api_key|password|secret)=', u.query)
                    and not re.search(r'[\s<>]',url))
    except ValueError:
        return False


def validate_papers(papers, snap):
    require(len(papers) == snap['studies'], 'Study count differs from snapshot')
    require(len({p['study_id'] for p in papers}) == len(papers), 'Duplicate study identity')
    for p in papers:
        sid = p['study_id']
        require(set(p) == set(FIELDS), f'{sid}: unexpected or missing public fields')
        require(re.fullmatch(r'STUDY-[a-f0-9]{24}',sid), f'{sid}: malformed study ID')
        require(re.fullmatch(r'RPT-[a-f0-9]{24}',p['report_id']), f'{sid}: malformed report ID')
        require(all(isinstance(p[k],str) and p[k].strip() for k in ('title','authors','venue')), f'{sid}: empty metadata')
        require(isinstance(p['year'],int) and 1900 <= p['year'] <= 2100, f'{sid}: invalid year')
        require(isinstance(p['solver_roles'],list) and set(p['solver_roles']) <= set(ROLES), f'{sid}: unknown role')
        require(len(set(p['solver_roles'])) == len(p['solver_roles']), f'{sid}: repeated role')
        require(p['role_status'] in ('classified','unclear','not_applicable'), f'{sid}: unknown role status')
        require(bool(p['solver_roles']) == (p['role_status']=='classified'), f'{sid}: inconsistent role status')
        require(p['literature_class'] in ('core_method','evaluation_diagnostic'), f'{sid}: unknown class')
        require(p['report_type'] in ('preprint','publication'), f'{sid}: unknown report type')
        require(p['record_version'] >= 1 and isinstance(p['record_version'],int), f'{sid}: invalid revision')
        require(p['url_basis'] in ('citation_version','citation_doi','citation_arxiv','canonical_report_catalogue','canonical_report_library','not_reported'), f'{sid}: unknown URL basis')
        require((p['url']=='not_reported') == (p['url_basis']=='not_reported'), f'{sid}: inconsistent missing URL')
        require(valid_url(p['url']), f'{sid}: unsafe URL')
        require(p['doi']=='not_reported' or re.fullmatch(r'10\.\d{4,9}/\S+',p['doi']), f'{sid}: malformed DOI')
        require(p['arxiv_id']=='not_reported' or re.fullmatch(r'(\d{4}\.\d{4,5}|[a-z.-]+/\d{7})(v\d+)?',p['arxiv_id']), f'{sid}: malformed arXiv ID')
        require(isinstance(p['bibtex_keys'],list) and all(re.fullmatch(r'[A-Za-z0-9:_-]+',k) for k in p['bibtex_keys']), f'{sid}: malformed citation key')
    for field,actual in [
        ('roles',Counter(r for p in papers for r in p['solver_roles'])),
        ('role_status',Counter(p['role_status'] for p in papers)),
        ('literature_classes',Counter(p['literature_class'] for p in papers)),
        ('citation_years',Counter(str(p['year']) for p in papers))]:
        require(dict(actual) == snap[field], f'{field}: stale snapshot counts')
    require(sum(p['url']=='not_reported' for p in papers)==snap['missing_source_links'], 'Stale missing-source count')


def validate_csv(papers, path):
    with path.open(encoding='utf-8',newline='') as f:
        reader = csv.DictReader(f)
        require(reader.fieldnames==FIELDS, 'CSV header differs from schema')
        actual = list(reader)
    expected = [{k:';'.join(p[k]) if isinstance(p[k],list) else str(p[k]) for k in FIELDS} for p in papers]
    require(actual==expected, 'CSV and JSON differ')


def validate_files():
    allowed_dirs = {'data','docs','papers','references','analysis','assets','manuscript','scripts','tests','.github'}
    allowed_root = {'README.md','LICENSE','CITATION.cff','CONTRIBUTING.md','AGENTS.md','CHANGELOG.md','.gitignore','release-manifest.json'}
    allowed_ext = {'.md','.csv','.json','.bib','.png','.py','.yml','.yaml','.cff','.template'}
    # Split literals so the validator does not mistake its own patterns for leaks.
    forbidden = ['/'+'Users/', '/'+'home/', 'file'+ '://', 'Solvers-in-the-loop-Survey'+'-Workspace',
                 'canonical_'+'pdf_path', 'name_evidence_'+'excerpt', 'BEGIN '+'PRIVATE KEY']
    paths = []
    for p in ROOT.rglob('*'):
        rel = p.relative_to(ROOT)
        if '.git' in rel.parts or '__pycache__' in rel.parts:
            continue
        require(not p.is_symlink(), f'Symlink is outside release policy: {rel}')
        if not p.is_file():
            continue
        require((len(rel.parts)==1 and p.name in allowed_root) or (len(rel.parts)>1 and rel.parts[0] in allowed_dirs and p.suffix in allowed_ext), f'Unapproved file: {rel}')
        require(p.stat().st_size < 5_000_000, f'Unexpected large file: {rel}')
        paths.append(p)
        if p.suffix == '.png':
            require(p.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'), f'Invalid PNG: {rel}')
            continue
        text = p.read_text(encoding='utf-8')
        require(not any(s in text for s in forbidden), f'Private content marker: {rel}')
        require(not re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{30,}',text), f'Credential-like content: {rel}')
        if p.suffix != '.md':
            continue
        for dest in re.findall(r'\]\(<?([^\s)>]+)>?\)',text) + re.findall(r'src="([^"]+)"',text):
            if re.match(r'https?://',dest):
                continue
            filepart,_,fragment = dest.partition('#')
            target = (p.parent/unquote(filepart)).resolve() if filepart else p
            require(target==ROOT or ROOT in target.parents, f'Link escapes release: {rel}: {dest}')
            require(target.exists(), f'Broken relative link: {rel}: {dest}')
            if fragment and target.name=='README.md' and target.parent.name=='references':
                require(f'id="{fragment}"' in target.read_text(encoding='utf-8'), f'Missing reference anchor: {dest}')
    return paths


def main():
    papers,snap = load('data/papers.json'),load('data/snapshot.json')
    links = load('manuscript/links.json')
    require(set(links)=={'status','arxiv_url','pdf_url','doi_url'}, 'Unexpected manuscript link fields')
    require(links['status'] in ('in_preparation','preprint','published'), 'Unknown manuscript status')
    require(all(valid_url(links[k]) for k in ('arxiv_url','pdf_url','doi_url')), 'Unsafe manuscript URL')
    require(links['status']=='in_preparation' or any(links[k]!='not_reported' for k in ('arxiv_url','pdf_url','doi_url')), 'Public manuscript status requires a source link')
    validate_papers(papers,snap)
    validate_csv(papers,ROOT/'data/papers.csv')
    ids = {p['study_id'] for p in papers}
    refs = load('references/references.json')
    require(len(refs)==snap['manuscript_references'], 'Reference count differs')
    require(len({r['key'] for r in refs})==len(refs),'Duplicate reference key')
    for r in refs:
        require(set(r)=={'key','title','authors','year','venue','url','study_ids'}, 'Unknown reference fields')
        require(set(r['study_ids'])<=ids and valid_url(r['url']), 'Invalid reference association / URL')
    bib = (ROOT/'references/references.bib').read_text(encoding='utf-8')
    require(set(re.findall(r'@\w+\s*\{\s*([^,]+),',bib))=={r['key'] for r in refs}, 'BibTeX/JSON key mismatch')
    for m in load('data/taxonomy-methods.json'):
        require(set(m)=={'role','grouping_axis','direction','method','bibtex_key','study_id','report_id','label_type'}, 'Unknown taxonomy fields')
        require(m['study_id'] in ids, 'Taxonomy references absent study')
    for b in load('analysis/benchmarks.json'):
        require(set(b)=={'part','name','category','source','modality','citations','protocols'}, 'Unknown benchmark fields')
        require(set(b['citations']) <= {r['key'] for r in refs}, 'Absent resource citation')
        for p in b['protocols']:
            require(set(p)=={'text','citations'} and set(p['citations'])<={r['key'] for r in refs}, 'Absent solver-use citation')
    for name in ('task-relevance-counts.csv','task-by-scoped-metric.csv'):
        with (ROOT/'analysis'/name).open(encoding='utf-8',newline='') as f:
            rows = list(csv.DictReader(f))
        require(len(rows)==8 and len({r['topic'] for r in rows})==8, 'Unexpected task aggregate shape')
        require(all(v.isdigit() and 0 <= int(v) <= len(papers) for r in rows for k,v in r.items() if k not in ('topic','label')), 'Invalid aggregate count')
    for name,content in render().items():
        require((ROOT/name).read_text(encoding='utf-8')==content, f'Stale generated view: {name}')
    files=validate_files()
    require(load('release-manifest.json')==manifest(), 'Release file manifest differs; regenerate after reviewed edits')
    cff=(ROOT/'CITATION.cff').read_text()
    require('version: '+snap['version'] in cff and 'date-released: '+snap['release_date'] in cff, 'Citation version/date differs')
    require('https://github.com/YishuaiGeng/Solvers-in-the-loop-Survey' in cff,'Citation repository missing')
    print(f"Validated {len(papers):,} studies, {len(refs)} references, {len(files)} public files; generated views and fingerprints agree.")


if __name__=='__main__':
    try:
        main()
    except (ValidationError, KeyError, ValueError, OSError) as exc:
        raise SystemExit(str(exc))

#!/usr/bin/env python3
from pathlib import Path
import re, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
SKIP_PARTS={'.git','__pycache__'}
required=['README.md','ADOPT.md','CUSTOMIZE.md','FIRST-WEEK.md','FIELD-TESTING.md','.github/ISSUE_TEMPLATE/concept-field-test.yml','SOUL.md','GOVERNANCE.md','LINEAGE.md','SYNC.md','LICENSE','index.md']
for name in required:
    if not (ROOT/name).is_file(): errors.append(f'missing required file: {name}')
required_fragments={
 'ADOPT.md':['Replace source identities before activation','Repository attribution may remain'],
 'CUSTOMIZE.md':['Identity handoff checklist','Search for the repository owner'],
 'FIELD-TESTING.md':['Situational-understanding starter test','Critical-capability mapping candidate test','Do not force one decisive centre','Do not label a person as a vulnerability','Operational-friction candidate test','Friction is a cross-layer amplifier, not a seventh stage','Do not manufacture disruption in a live consequential system','Never label a person, relationship, dissent, or protected exercise of agency as “friction”','A clean null result includes finding that the check only renamed an already-known concern','Privacy and authority boundary'],
 'doctrine/design/right-sized-change.md':['Operational-friction check (candidate)','Friction is a **cross-layer amplifier**, not a seventh stage','manufactured disruption in a live consequential system','Never label a person, relationship, dissent, or protected exercise of agency as “friction”','Count the check as a null result when it only renames an already-known preflight, critical-path, or resilience concern','Local discretion remains bounded by authority, rights, competence, and recovery conditions'],
 '.github/ISSUE_TEMPLATE/concept-field-test.yml':['Concept field test','Strongest alternative explanation or confound','runtime state and dumps','do not reconstruct one'],
}
for name,fragments in required_fragments.items():
    path=ROOT/name
    if not path.is_file(): continue
    text=path.read_text()
    for fragment in fragments:
        if fragment not in text: errors.append(f'{name} missing required guidance: {fragment}')
issue_form=ROOT/'.github/ISSUE_TEMPLATE/concept-field-test.yml'
if issue_form.is_file():
    form=issue_form.read_text()
    for key in ['name','description','title','body']:
        if not re.search(rf'(?m)^{key}:',form): errors.append(f'issue form missing top-level key: {key}')
    field_ids=re.findall(r'(?m)^    id:\s*([a-z0-9_-]+)\s*$',form)
    if not field_ids: errors.append('issue form has no field ids')
    if len(field_ids)!=len(set(field_ids)): errors.append('issue form has duplicate field ids')
    for field_type in ['markdown','input','dropdown','textarea','checkboxes']:
        if not re.search(rf'(?m)^  - type:\s*{field_type}\s*$',form): errors.append(f'issue form missing field type: {field_type}')
banned={
 'private identity':'Austin|Lourdes|Temperance|Upstate Organized|Bell household',
 'private path':r'/Users/|/root/|robertbell|\.hermes/cache|Documents/Agent-Ops-Wiki',
 'runtime residue':r'Honcho|Telegram|YNAB|HealthKit|UniFi',
 'secret material':r'AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----',
}
def skipped(p): return any(part in SKIP_PARTS for part in p.parts)
text_files=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or skipped(p) or p.name in {'LICENSE','check_template.py'}: continue
    try: text=p.read_text()
    except UnicodeDecodeError: errors.append(f'binary/unreadable file: {p.relative_to(ROOT)}');continue
    text_files.append(p)
    for label,pat in banned.items():
        if re.search(pat,text,re.I): errors.append(f'{label} in {p.relative_to(ROOT)}')
    if text and not text.endswith('\n'): errors.append(f'missing final newline: {p.relative_to(ROOT)}')
ids=[]
for p in sorted((ROOT/'doctrine').rglob('*.md')):
    text=p.read_text()
    if not text.startswith('---\n') or '\n---\n' not in text[4:]: errors.append(f'bad frontmatter: {p.relative_to(ROOT)}');continue
    fm=text.split('\n---\n',1)[0]
    for key in ['id','type','status','authority','confidence','consult_when','do_not_use_when','router_summary','decision_effect','review_when']:
        if not re.search(rf'(?m)^{re.escape(key)}:',fm): errors.append(f'{p.relative_to(ROOT)} missing {key}')
    m=re.search(r'(?m)^id:\s*(.+)$',fm)
    if m: ids.append((m.group(1).strip(),p))
for ident in {x for x,_ in ids}:
    ps=[str(p.relative_to(ROOT)) for x,p in ids if x==ident]
    if len(ps)>1: errors.append(f'duplicate doctrine id {ident}: {ps}')
if len(ids)!=8: errors.append(f'expected 8 doctrine pages, found {len(ids)}')
link_re=re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
for p in text_files:
    if p.suffix.lower()!='.md': continue
    for target in link_re.findall(p.read_text()):
        target=target.split('#',1)[0]
        if not target or re.match(r'^[a-z]+://',target,re.I) or target.startswith('mailto:'): continue
        if not (p.parent/target).resolve().exists(): errors.append(f'broken link in {p.relative_to(ROOT)}: {target}')
gen=ROOT/'scripts/generate_index.py'
if gen.exists() and (ROOT/'index.md').exists():
    before=(ROOT/'index.md').read_bytes()
    cp=subprocess.run([sys.executable,str(gen)],cwd=ROOT,capture_output=True,text=True)
    if cp.returncode: errors.append('index generator failed: '+cp.stderr.strip())
    elif (ROOT/'index.md').read_bytes()!=before: errors.append('index.md was stale (regenerated during check)')
for p in ROOT.rglob('*'):
    if skipped(p): continue
    if p.name.startswith('._') or p.name=='.DS_Store': errors.append(f'metadata sidecar: {p.relative_to(ROOT)}')
    if p.is_symlink(): errors.append(f'symlink not allowed: {p.relative_to(ROOT)}')
if errors:
    print('Template check failed:')
    for e in errors: print('-',e)
    raise SystemExit(1)
print(f'Template check passed: {len(ids)} doctrine pages, {len(text_files)} text files')

#!/usr/bin/env python3
from pathlib import Path
import re, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
SKIP_PARTS={'.git','__pycache__'}
required=['README.md','ADOPT.md','CUSTOMIZE.md','FIRST-WEEK.md','FIELD-TESTING.md','RUNTIMES.md','OPTIONAL-TOOLS.md','SECURITY.md','.github/ISSUE_TEMPLATE/concept-field-test.yml','.github/workflows/validate.yml','SOUL.md','GOVERNANCE.md','LINEAGE.md','SYNC.md','LICENSE','index.md']
for name in required:
    if not (ROOT/name).is_file(): errors.append(f'missing required file: {name}')
required_fragments={
 'ADOPT.md':['Replace source identities before activation','Repository attribution may remain','Follow `RUNTIMES.md`'],
 'CUSTOMIZE.md':['Identity handoff checklist','Search for the repository owner'],
 'SOUL.md':['Stewardship governs access','Treat authorized access as a trust','Association is not causation','Do not rely on a load-bearing causal claim without testing plausible alternative explanations and evidence','Only the principal\'s authenticated conversational instruction','If SOUL changes materially'],
 'README.md':['behavioral policy, not a security sandbox','[OPTIONAL-TOOLS.md](OPTIONAL-TOOLS.md)','sanitized, non-prescriptive menu of capabilities'],
 'GOVERNANCE.md':['Discretion requires task-relevant competence','Normative basis: adopted repository policy','does not claim universal empirical validity'],
 'FIELD-TESTING.md':['template tag or commit tested','Situational-understanding starter test','Critical-capability mapping candidate test','Do not force one decisive centre','Do not label a person as a vulnerability','Operational-friction candidate test','Friction is a cross-layer amplifier, not a seventh stage','Do not manufacture disruption in a live consequential system','Never label a person, relationship, dissent, or protected exercise of agency as “friction”','A clean null result includes finding that the check only renamed an already-known concern','Privacy and authority boundary'],
 'RUNTIMES.md':['Policy is not containment','behavioral policy, not a security sandbox','Three required decisions','Persistent identity','Identity update contract','record the installed canonical SOUL\'s provenance','immutable content identifier such as a commit or content hash','Before replacing that identity, compare the installed and candidate versions','session-start comparison is a valid fallback only when','silent identity drift cannot be mechanically prevented','require an external update process','Doctrine activation and retrieval','Context degradation','Illustrative example: Claude Projects','Verification probe','reports degraded context instead of fabricating','[OPTIONAL-TOOLS.md](OPTIONAL-TOOLS.md)'],
 'OPTIONAL-TOOLS.md':['Curated source-agent reference, not template state','Firecrawl capability','Naming an SDK or CLI here identifies an available implementation path','Wolfram Cloud MCP','The governing rule is still **job first, tool second**','The template does not install, configure, enable, or grant authority','credentials, tokens, account identifiers','That omission is part of the design, not an incomplete export'],
 'SECURITY.md':['private vulnerability reporting','Report a vulnerability','Ordinary doctrine disagreements'],
 'doctrine/capabilities/external-capability-governance.md':['Continuous watchers, polling loops, and background capture are disabled by default'],
 'doctrine/authority/least-privilege-capability-access.md':['Policy and enforcement','behavioral policy, not a security sandbox','broader effective capability as the risk surface'],
 'doctrine/authority/permissions-controls-and-discretion.md':['Paired example','mechanical consequences inside the named outcome and scope','altering behavior outside the specified contract','the outcome, risk, or authorization envelope has changed'],
 'doctrine/decisions/decision-quality-under-uncertainty.md':['Keep three registers separate when values could contaminate prediction'],
 'doctrine/decisions/strategic-response-and-incentives.md':['Treat reputation as a narrow prior for a specific claim and context'],
 'doctrine/design/decision-records-and-operational-documentation.md':['Design for the next reader and task'],
 'doctrine/design/right-sized-change.md':['Operational-friction check (candidate)','Friction is a **cross-layer amplifier**, not a seventh stage','manufactured disruption in a live consequential system','Never label a person, relationship, dissent, or protected exercise of agency as “friction”','Count the check as a null result when it only renames an already-known preflight, critical-path, or resilience concern','Local discretion remains bounded by authority, rights, competence, and recovery conditions','maximum time, cost, retries'],
 'doctrine/knowledge/information-placement-and-source-authority.md':['prefer one residual question, one missing measurement, or one bounded follow-up'],
 '.github/ISSUE_TEMPLATE/concept-field-test.yml':['Concept field test','template_version','Strongest alternative explanation or confound','runtime state and dumps','do not reconstruct one'],
 '.github/workflows/validate.yml':['permissions:','contents: read','git diff --exit-code -- index.md','python3 scripts/check_template.py'],
}
required_sections={
 'FIELD-TESTING.md':{
  'Claim-to-evidence audit candidate test':[
   'audit completeness by scanning the final output',
   'Audit correctness by testing whether each evidence item supports the claim\'s actual wording, scope, and strength',
   'performed`, `not applicable — rationale`, or `blocked — reason',
   'A second pass by the same model is useful discrepancy detection but not independent proof',
   'zero phantom references means 0 of 337 references in that evaluated sample, not a general guarantee',
  ],
 },
 'doctrine/design/decision-records-and-operational-documentation.md':{
  'Consequential claim-to-evidence audit (candidate)':[
   'A claim is **load-bearing** when its falsity would materially change',
   'Audit **completeness** and **correctness** separately',
   'inspect the output for claims missing from the record rather than checking only records already created',
   'Reference:** verify source existence, identity, locator, and attributed support',
   'Specification:** test the actual objective and constraints rather than a convenient proxy or evaluator loophole',
   'Method–artifact:** compare described methods, configuration, and procedures with what actually executed',
   'A second pass by the same model can detect discrepancies but is not independent proof',
   'Do not impose this as a universal ledger',
  ],
 },
}
forbidden_section_fragments={
 'FIELD-TESTING.md':{
  'Claim-to-evidence audit candidate test':[
   'A second pass by the same model is independent proof',
   'zero phantom references is a general guarantee',
  ],
 },
 'doctrine/design/decision-records-and-operational-documentation.md':{
  'Consequential claim-to-evidence audit (candidate)':[
   'A second pass by the same model can provide independent proof',
   'A second pass by the same model is independent proof',
   'Impose this as a universal ledger',
   'Do not inspect the output for claims missing from the record',
  ],
 },
}

def active_markdown(text):
    """Remove comments and fenced examples that do not express active guidance."""
    text=re.sub(r'<!--.*?(?:-->|$)','',text,flags=re.S)
    active=[]
    fence_character=None
    fence_length=0
    for line in text.splitlines(keepends=True):
        if fence_character is None:
            opener=re.match(r'^ {0,3}(`{3,}|~{3,})',line)
            if opener:
                marker=opener.group(1)
                fence_character=marker[0]
                fence_length=len(marker)
                continue
            active.append(line)
            continue
        if re.match(rf'^ {{0,3}}{re.escape(fence_character)}{{{fence_length},}}\s*$',line):
            fence_character=None
            fence_length=0
    return ''.join(active)

def atx_heading(line):
    """Return a CommonMark ATX heading's level and normalized title."""
    match=re.match(r'^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*$',line)
    if not match:
        return None
    title=re.sub(r'[ \t]+#+[ \t]*$','',match.group(2)).strip()
    return len(match.group(1)),title

def markdown_sections(text,heading):
    """Return active level-two section bodies, excluding later top-level sections."""
    lines=active_markdown(text).splitlines()
    sections=[]
    start=None
    for index,line in enumerate(lines):
        parsed=atx_heading(line)
        if parsed and parsed==(2,heading):
            if start is not None:
                sections.append('\n'.join(lines[start:index]))
            start=index+1
            continue
        if start is not None and parsed and parsed[0]<=2:
            sections.append('\n'.join(lines[start:index]))
            start=None
    if start is not None:
        sections.append('\n'.join(lines[start:]))
    return sections

def has_same_model_independence_claim(section):
    """Detect direct positive claims that same-model review is independent proof."""
    sentences=re.split(r'(?<=[.!?])(?:\s+|$)|\n+',section)
    for sentence in sentences:
        lower=sentence.lower()
        if not re.search(r'\b(?:same[- ]model|second pass by the same model)\b',lower):
            continue
        if 'independent proof' not in lower:
            continue
        if re.search(r'\b(?:not|isn.t|cannot|can.t|does not|doesn.t)\b[^.!?]{0,45}\bindependent proof\b',lower):
            continue
        if re.search(r'\b(?:is|provides?|constitutes?|offers?|counts as|establishes?)\b[^.!?]{0,60}\bindependent proof\b',lower):
            return True
    return False

for name,fragments in required_fragments.items():
    path=ROOT/name
    if not path.is_file(): continue
    text=active_markdown(path.read_text())
    for fragment in fragments:
        if fragment not in text: errors.append(f'{name} missing required guidance: {fragment}')
# Location-sensitive static preservation canaries. They establish that active
# guidance remains in its owning section, not runtime compliance or semantic proof.
for name,sections in required_sections.items():
    path=ROOT/name
    if not path.is_file(): continue
    text=path.read_text()
    for heading,fragments in sections.items():
        matches=markdown_sections(text,heading)
        if len(matches)!=1:
            errors.append(f'{name} must contain exactly one active {heading!r} section; found {len(matches)}')
            continue
        section=matches[0]
        for fragment in fragments:
            if fragment not in section: errors.append(f'{name} section {heading!r} missing required guidance: {fragment}')
        for fragment in forbidden_section_fragments.get(name,{}).get(heading,[]):
            if fragment in section: errors.append(f'{name} section {heading!r} contains contradictory guidance: {fragment}')
        if has_same_model_independence_claim(section):
            errors.append(f'{name} section {heading!r} claims same-model review is independent proof')
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

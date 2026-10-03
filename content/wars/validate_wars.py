import json, sys, os, re
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(H, '..', '..', 'data')  # the site's border data
files = json.load(open(os.path.join(D, 'timeline.json')))['borderFiles']
yr = lambda f: -int(f[2:]) if f.startswith('bc') else int(f)
names = {f: {x['properties']['name'] for x in json.load(open(os.path.join(D, 'borders_%s.json' % f)))['features']} for f in files}
def file_for(y):
    ok = [f for f in files if yr(f) <= y]
    return ok[-1] if ok else files[0]
def pt(p): return isinstance(p, list) and len(p) == 2 and all(isinstance(v, (int, float)) for v in p) and -180 <= p[0] <= 180 and -90 <= p[1] <= 90
errs = []
data = json.load(open(sys.argv[1]))
ids = set()
for w in data:
    W = w.get('id', '?')
    for k in ('id', 'name', 'start', 'end', 'kind', 'summary', 'sides', 'theater', 'steps'):
        if k not in w: errs.append(f'{W}: missing {k}')
    if W in ids: errs.append(f'{W}: duplicate id')
    ids.add(W)
    if w.get('kind') not in ('war', 'conflict'): errs.append(f'{W}: kind must be war|conflict')
    ns = len(w.get('sides', []))
    if not 2 <= ns <= 3: errs.append(f'{W}: needs 2-3 sides')
    for s in w.get('sides', []):
        if not re.match(r'^#[0-9a-fA-F]{6}$', s.get('color', '')): errs.append(f'{W}: bad side colour')
    for t in w.get('theater', []):
        if not pt([t.get('lon'), t.get('lat')]) or not 0 < t.get('r', 0) <= 60: errs.append(f'{W}: bad theater')
    st = w.get('steps', [])
    if not 3 <= len(st) <= 10: errs.append(f'{W}: needs 3-10 steps')
    prev = -1e9
    for i, s in enumerate(st):
        S = f'{W} step {i}'
        for k in ('year', 'label', 'title', 'text', 'territories', 'fronts', 'moves', 'events'):
            if k not in s: errs.append(f'{S}: missing {k}')
        y = s.get('year', 0)
        if y < prev: errs.append(f'{S}: years out of order')
        prev = y
        if not (w['start'] - 1 <= y <= w['end'] + 1): errs.append(f'{S}: year {y} outside war')
        f = file_for(y)
        for t in s.get('territories', []):
            if not 0 <= t.get('side', -1) < ns: errs.append(f'{S}: bad territory side')
            for n in t.get('polities', []):
                if n not in names[f]: errs.append(f'{S}: polity "{n}" not in names_{f}.tsv')
        for fr in s.get('fronts', []):
            if not (2 <= len(fr.get('path', [])) and all(pt(p) for p in fr['path'])): errs.append(f'{S}: bad front path')
        mv = s.get('moves', [])
        if len(mv) > 5: errs.append(f'{S}: more than 5 moves')
        for m in mv:
            if not 0 <= m.get('side', -1) < ns: errs.append(f'{S}: bad move side')
            if not m.get('commander'): errs.append(f'{S}: move without commander')
            if not (2 <= len(m.get('path', [])) <= 6 and all(pt(p) for p in m['path'])): errs.append(f'{S}: bad move path')
        ev = s.get('events', [])
        if len(ev) > 3: errs.append(f'{S}: more than 3 events')
        for e in ev:
            if e.get('kind') not in ('battle', 'siege', 'treaty', 'war', 'event'): errs.append(f'{S}: bad event kind')
            if not pt([e.get('lon'), e.get('lat')]): errs.append(f'{S}: bad event coords')
            if e.get('winner') is not None and not 0 <= e['winner'] < ns: errs.append(f'{S}: bad winner')
        for k in ('text', 'title'):
            if re.search('[–—]', s.get(k, '')): errs.append(f'{S}: dash in {k}')
print('\n'.join(errs) if errs else f'OK: {len(data)} wars, {sum(len(w["steps"]) for w in data)} steps')

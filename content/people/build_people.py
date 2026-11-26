"""Builds data/people.json from the era files in this folder and checks them against the border data.

Run from the repository root:  python3 content/people/build_people.py
Checks: required fields, life and stint years, tags, places, and that each "rule" stint names a state that is on the
map in every border snapshot its years use (else it needs `at`, a place to show the person instead).
It also writes data/commanders.json (the generals in commanders.py that get a figure at the head of their army) and
titles.txt, every Wikipedia title the page will ask for a portrait. If wiki_checked.json is present (title -> {ok, title},
from checking those titles against Wikipedia), commanders whose title failed get no portrait and corrected titles are used.
"""
import json, os, sys, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data')
sys.path.insert(0, HERE)
import _lib

for f in sorted(glob.glob(os.path.join(HERE, 'p[0-9][0-9]_*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    spec.loader.exec_module(importlib.util.module_from_spec(spec))
people = _lib.PEOPLE

tl = json.load(open(os.path.join(DATA, 'timeline.json')))
FILES = tl['borderFiles']
fy = lambda f: -int(f[2:]) if f.startswith('bc') else int(f)
def file_for(y):
    best = FILES[0]
    for f in FILES:
        if fy(f) <= y: best = f
    return best
names, group = {}, {}
for f in FILES:
    fc = json.load(open(os.path.join(DATA, f'borders_{f}.json')))
    s, g = set(), {}
    for ft in fc['features']:
        p = ft['properties']; s.add(p['name'])
        g[p['name']] = (p.get('sub') or p.get('part') or p['name']).strip()
        for k in ('sub', 'part'):
            if p.get(k): s.add(p[k])
    names[f], group[f] = s, g

errs, warns = [], []
ids = set()
for p in people:
    who = p['id']
    if who in ids: errs.append(f'{who}: duplicate id')
    ids.add(who)
    for k in ('name', 'role', 'why', 'wiki'):
        if not p.get(k): errs.append(f'{who}: missing {k}')
    if len(p['why']) > 230: warns.append(f'{who}: why is {len(p["why"])} chars')
    b, d = p['life']
    if b is not None and d is not None and b >= d: errs.append(f'{who}: life {b}..{d}')
    if p['rank'] not in (1, 2, 3): errs.append(f'{who}: rank {p["rank"]}')
    bad = [t for t in p['tags'] if t not in _lib.TAGS]
    if bad or not p['tags']: errs.append(f'{who}: tags {p["tags"]}')
    if not p['stints']: errs.append(f'{who}: no stints')
    for s in p['stints']:
        if s['from'] > s['to']: errs.append(f'{who}: stint {s["label"]} {s["from"]}..{s["to"]}')
        if s['from'] == 0 or s['to'] == 0: errs.append(f'{who}: year 0 in {s["label"]}')
        if b is not None and s['from'] < b: errs.append(f'{who}: stint {s["label"]} starts {s["from"]} before birth {b}')
        if d is not None and s['to'] > d: errs.append(f'{who}: stint {s["label"]} ends {s["to"]} after death {d}')
        pts = s.get('path') or ([s['at']] if s.get('at') else [])
        for q in pts:
            if not (-180 <= q[0] <= 180 and -90 <= q[1] <= 90): errs.append(f'{who}: bad point {q}')
            if len(q) > 2 and not (s['from'] <= q[2] <= s['to'] + 1): errs.append(f'{who}: waypoint year {q[2]} outside {s["label"]}')
        if 'rule' in s:
            used = sorted({file_for(y) for y in range(s['from'], s['to'] + 1) if y}, key=fy)
            miss = [f for f in used if not any(n in names[f] for n in s['rule'])]
            if miss and not s.get('at'):
                errs.append(f'{who}: "{s["label"]}" {s["rule"]} not on map in {miss}')
            # the simplified map labels whole groups (a state with its subjects); a ruler only sits by a group's
            # label when the group is their own state, which the stint says by listing the group's name too
            for f in used:
                n = next((n for n in s['rule'] if n in group[f]), None)
                if n and group[f][n] != n and group[f][n] not in s['rule'] and not s.get('at'):
                    warns.append(f'{who}: "{s["label"]}" {n} is under {group[f][n]} on the simple map in {f}; no at')
        elif not s.get('path'):
            errs.append(f'{who}: stint {s["label"]} has neither rule nor path')

def rnd(q): return [round(q[0], 2), round(q[1], 2)] + ([q[2]] if len(q) > 2 else [])
checked = {}
cp = os.path.join(HERE, 'wiki_checked.json')
if os.path.exists(cp): checked = json.load(open(cp))
out = []
for p in people:
    q = {k: p[k] for k in ('id', 'name', 'role', 'life', 'rank', 'tags', 'why', 'wiki')}
    if p.get('short'): q['short'] = p['short']
    c = checked.get(p['wiki'])
    if c and c.get('title') and c['title'] != p['wiki']: q['wiki'] = c['title']
    if c is not None and not c.get('ok', True): q.pop('wiki')  # no reliable page: show initials only
    st = []
    for s in p['stints']:
        t = {'from': s['from'], 'to': s['to'], 'label': s['label']}
        if 'rule' in s: t['rule'] = s['rule']
        if s.get('at'): t['at'] = rnd(s['at'])
        if s.get('path'): t['path'] = [rnd(x) for x in s['path']]
        st.append(t)
    q['stints'] = st
    out.append(q)
json.dump({'people': out}, open(os.path.join(DATA, 'people.json'), 'w'), ensure_ascii=False, separators=(',', ':'))

# the generals worth knowing (content/people/commanders.py): commander string -> {wiki, person}
import commanders
byname = {q['name']: q for q in out}
used = set()
for w in json.load(open(os.path.join(DATA, 'wars.json'))):
    for st in w['steps']:
        for m in st.get('moves', []):
            if m.get('commander'): used.add(m['commander'])
cm = {}
for c, t in commanders.NOTABLE.items():
    if c not in used: warns.append(f'commander "{c}" is not in any war'); continue
    q = byname.get(t)
    if q: cm[c] = {'person': q['id']} | ({'wiki': q['wiki']} if q.get('wiki') else {})
    else:
        k = checked.get(t)
        if k is not None and not k.get('ok', True): cm[c] = {}; continue
        cm[c] = {'wiki': (k or {}).get('title') or t}
json.dump(cm, open(os.path.join(DATA, 'commanders.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(cm), 'notable commanders,', sum(1 for v in cm.values() if 'person' in v), 'linked to people')
with open(os.path.join(HERE, 'titles.txt'), 'w') as fh:
    fh.write('\n'.join(sorted({p['wiki'] for p in people} | {t for t in commanders.NOTABLE.values() if t not in byname})))
print(f'{len(people)} people, {sum(len(p["stints"]) for p in people)} stints; '
      f'{sum(1 for p in people if p["rank"] == 1)} rank 1, {sum(1 for p in people if p["rank"] == 2)} rank 2')
print(f'{len(errs)} errors, {len(warns)} warnings')
for e in errs: print('E', e)
for w in warns: print('W', w)
print(os.path.getsize(os.path.join(DATA, 'people.json')) // 1024, 'KB')

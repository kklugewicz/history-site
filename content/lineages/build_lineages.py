"""Builds data/lineages.json, each country's own timeline, from the region files in this folder (l*.py, see _lib.py).

Run from the repository root:  python3 content/lineages/build_lineages.py [--report]   (needs shapely)

Checks, as errors: periods in order and inside the slider's years (10,000 BC to the end of the 2020s; the page ends the
timeline at the current year), every state name present in the border files, and no state at home in two countries for
the same years. Warnings: a state listed for a period it is never on the map near; a border snapshot in which none of a
country's states is drawn; the state that held a country's core in a snapshot when it isn't one of that country's
states (a sign of a missing name); a state drawn wholly outside its country's years (a click on it there shows its own
years); and a state drawn in a snapshot that no period of its country near then lists (the country's timeline would
not keep it picked). --report also lists the states the simplified map shows that belong to no country, biggest
first; a click on one shows its own years.

Output: {lineages: [{id, name, region, core, periods: [{name, short, from, to, note, states}]}],
         names: {state: id or [[id, from, to], ...] when it is at home in different countries in different years},
         seen: {state: [from, to]}: the years each state with no country is on the map (to null: still there),
         shared: [the peoples and loose labels a click resolves by the land it falls on today (see _lib.shared)]}
"""
import json, math, os, re, sys, glob, importlib.util, collections
from shapely.geometry import shape, Point
from shapely.prepared import prep

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data')
sys.path.insert(0, HERE)
import _lib  # noqa: E402

REPORT = '--report' in sys.argv
LO, HI = -10000, 2029

for f in sorted(glob.glob(os.path.join(HERE, 'l[0-9][0-9]_*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    spec.loader.exec_module(importlib.util.module_from_spec(spec))

# ---------- the border snapshots, with the page's own rule for which states the simplified map shows ----------
tl = json.load(open(os.path.join(DATA, 'timeline.json')))
FILES = tl['borderFiles']
fy = lambda f: -int(f[2:]) if f.startswith('bc') else int(f)
YEARS = [fy(f) for f in FILES]
# the years a snapshot stands for: from its own year to the next one's
def file_span(i): return (YEARS[i], YEARS[i + 1] - 1 if i + 1 < len(YEARS) else HI)
FAMOUS = re.compile(r"egypt|sumer|akkad|babylon|assyria|hittite|mycen|minoa|athen|sparta|greek|macedon|rom[ae]|carthag|phoenic|israel|juda|persia|maya|aztec|mexica|inca|olmec|harappa|indus|shang|zhou|qin|venice|venezia|genoa|papal|byzantine|kush|axum|aksum|mali|songhai|ghana|zimbabwe|khmer|champa|silla|goguryeo|baekje|japan|yamato|korea|joseon|goryeo|portugal|england|scotland|hungary|poland|bohemia|serbia|bulgaria|armenia|georgia|teotihuacan|zapotec|toltec|chim[uú]|moche|nazca|tiwanaku|wari|cahokia|ethiopia", re.I)
NOT_STATE = re.compile(r"hunter|gatherer|forag|fich|fisher|farmers|pastoral|herder|cultures?\b|khoi|bant[ou]|aborigin|siberians", re.I)
R = 6371.0


def ring_km2(r):
    a = 0
    for i in range(len(r)):
        x1, y1 = r[i - 1]; x2, y2 = r[i]
        a += math.radians(x2 - x1) * (2 + math.sin(math.radians(y1)) + math.sin(math.radians(y2)))
    return abs(a * R * R / 2)


def km2(g):
    polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    return sum(ring_km2(p[0]) - sum(ring_km2(h) for h in p[1:]) for p in polys)


snap = []        # per file: list of {name, group, major, km2, geom}
present = collections.defaultdict(list)   # name -> file indexes
for i, f in enumerate(FILES):
    fc = json.load(open(os.path.join(DATA, f'borders_{f}.json')))
    modern = YEARS[i] >= 1900
    rows, gA, gH = [], collections.Counter(), {}
    for ft in fc['features']:
        p = ft['properties']
        r = dict(name=p['name'], group=(p.get('sub') or p.get('part') or p['name']).strip(), km2=km2(ft['geometry']),
                 region=p['regions'][0], geom=ft['geometry'])
        gA[r['group']] += r['km2']
        if r['group'] not in gH or r['km2'] > gH[r['group']][1]: gH[r['group']] = (r['region'], r['km2'])
        rows.append(r)
    by = collections.defaultdict(list)
    for g in gA:
        if not NOT_STATE.search(g): by[gH[g][0]].append(g)
    top = {g for gs in by.values() for g in sorted(gs, key=lambda g: -gA[g])[:2 if modern else 3]}
    for r in rows:
        g = r['group']
        r['major'] = bool(FAMOUS.search(g) or FAMOUS.search(r['name']) or
                          (not NOT_STATE.search(g) and (gA[g] >= (10e3 if modern else 1.5e6) or g in top)))
        if i not in present[r['name']]: present[r['name']].append(i)
    snap.append(rows)


def holder(i, lonlat):
    """the state drawn over a point in snapshot i, biggest first if several overlap (the simplified map's choice too)"""
    pt = Point(*lonlat)
    hits = []
    for r in snap[i]:
        if 'shape' not in r: r['shape'] = prep(shape(r['geom']))
        if r['shape'].contains(pt): hits.append(r)
    hits.sort(key=lambda r: (not r['major'], -r['km2']))
    return hits[0] if hits else None


# ---------- the countries ----------
errs, warns = [], []
byid = {}
for l in _lib.LINEAGES:
    if l['id'] in byid: errs.append(f"{l['id']}: listed twice")
    byid[l['id']] = l
for l in _lib.LINEAGES:
    if l['base']:
        bid, until = l['base']
        if bid not in byid: errs.append(f"{l['id']}: base {bid} is not a country"); continue
        b = byid[bid]
        if b['base']: errs.append(f"{l['id']}: base {bid} has a base of its own")
        own = l['periods']
        l['periods'] = [dict(p, states=[s if s.startswith('~') else '~' + s for s in p['states']], borrowed=True)
                        for p in b['periods'] if p['start'] < until] + own
        if l['periods'] and own and l['periods'][len(l['periods']) - len(own) - 1]['start'] >= own[0]['start']:
            errs.append(f"{l['id']}: base periods run past {own[0]['name']}")


def span_end(ps, i):
    """where period i ends on the timeline: the year before the next one starts (there is no year 0)"""
    if i + 1 < len(ps):
        n = ps[i + 1]['start']
        return -1 if n == 1 else n - 1
    return HI if ps[i]['end'] is None else min(ps[i]['end'], HI)


homes = collections.defaultdict(list)   # name -> [(id, from, to)]
for l in _lib.LINEAGES:
    lid, ps = l['id'], l['periods']
    if not ps: errs.append(f'{lid}: no periods'); continue
    if l['region'] not in tl['regions']: errs.append(f"{lid}: region {l['region']!r} is not one of the timeline's")
    for i, p in enumerate(ps):
        a, b = p['start'], p['end']
        if a == 0 or b == 0: errs.append(f"{lid}: {p['name']}: year 0")
        if a < LO or a > HI: errs.append(f"{lid}: {p['name']}: starts {a}, outside the slider")
        if b is not None and b < a: errs.append(f"{lid}: {p['name']}: ends {b} before it starts {a}")
        if i and a <= ps[i - 1]['start']: errs.append(f"{lid}: {p['name']} starts {a}, not after {ps[i - 1]['name']}")
        if i + 1 < len(ps) and b is None: errs.append(f"{lid}: {p['name']} has no end but is not the last period")
        if b is not None and i + 1 < len(ps) and ps[i + 1]['start'] - b > 40:
            warns.append(f"{lid}: {b + 1}..{ps[i + 1]['start'] - 1} between {p['name']} and {ps[i + 1]['name']} falls to {p['name']}")
        p['span'] = (a, span_end(ps, i))
        for s in p['states']:
            n = s.lstrip('~')
            if n not in present: errs.append(f"{lid}: {p['name']}: no state is called {n!r} in the border files")
            elif not p.get('borrowed'):
                # on the map at some time near the period (a snapshot stands for the years up to the next one)
                lo, hi = p['span']
                near = [j for j in present[n] if file_span(j)[1] >= lo - 150 and file_span(j)[0] <= hi + 150]
                if not near:
                    warns.append(f"{lid}: {p['name']} ({lo}..{hi}): {n!r} is on the map only in {', '.join(FILES[j] for j in present[n])}")
            if not s.startswith('~'): homes[n].append((lid, p['span'][0], p['span'][1]))

# a name at home in one country for all its listings, or in several for different years
names = {}
for n, hs in homes.items():
    hs.sort(key=lambda h: h[1])
    merged = []
    for h in hs:
        if merged and merged[-1][0] == h[0]: merged[-1][2] = max(merged[-1][2], h[2])
        else: merged.append(list(h))
    for x, y in zip(merged, merged[1:]):
        if y[1] <= x[2]: errs.append(f'{n!r} is at home in {x[0]} ({x[1]}..{x[2]}) and {y[0]} ({y[1]}..{y[2]}); mark one with ~')
    if len(merged) == 1: names[n] = merged[0][0]
    else:
        merged[0][1] = None; merged[-1][2] = None
        names[n] = [[i, a, b] for i, a, b in merged]


def gap(lo, hi, a, b): return a - hi if a is not None and hi < a else lo - b if b is not None and lo > b else 0


def home_in(n, j):
    """the country a click on state n in snapshot j opens: for a name at home in several, the one whose years come
    nearest the snapshot's, as the page's lineageOf picks it (its tie-break, the year shown, is the snapshot's first here)"""
    h = names[n]
    if isinstance(h, str): return h
    a, b = file_span(j)
    return min(h, key=lambda e: gap(a, b, e[1], e[2]) * 1e5 + gap(a, a, e[1], e[2]))[0]


# which state held each country's core, snapshot by snapshot, and the snapshots that draw none of its states
for l in _lib.LINEAGES:
    ps, lid = l['periods'], l['id']
    if not ps or not l['core']: continue
    lo, hi = ps[0]['span'][0], ps[-1]['span'][1]
    empty, held = [], collections.defaultdict(list)
    for i in range(len(FILES)):
        a, b = file_span(i)
        if b < lo or a > hi or YEARS[i] < lo - 1: continue
        # the states the page counts as the country's in this snapshot (its rankIn): those of the periods the snapshot
        # touches, the own states of the periods either side, and a borrowed state of theirs only while it holds the core
        idx = [k for k, p in enumerate(ps) if p['span'][1] >= max(a, lo) and p['span'][0] <= min(b, hi)]
        side = [s for k in range(max(0, idx[0] - 1), min(len(ps), idx[-1] + 2)) for s in ps[k]['states']]
        h = holder(i, l['core'])
        near = {s.lstrip('~') for k in idx for s in ps[k]['states']} | {s for s in side if s[0] != '~'}
        if h and '~' + h['name'] in side: near.add(h['name'])
        if not any(r['name'] in near for r in snap[i]): empty.append(FILES[i])
        if h and h['name'] not in near and not NOT_STATE.search(h['name']):
            held[h['name'] + (f" (in {h['group']})" if h['group'] != h['name'] else '')].append(FILES[i])
    if empty: warns.append(f"{lid}: none of its states is drawn in {', '.join(empty)}")
    # a state at home here drawn in a snapshot wholly outside the country's years opens its own years instead
    outside = sorted({f"{n} in {FILES[j]}" for n in names for j in present[n]
                      if (file_span(j)[1] < lo or file_span(j)[0] > hi) and home_in(n, j) == lid})
    if outside: warns.append(f"{lid}: drawn outside its years: {', '.join(outside)}")
    for n, fs in held.items(): warns.append(f"{lid}: its core is held by {n!r} in {', '.join(fs)}")

# a state clicked in a snapshot opens the timeline of the country it is at home in (for a name at home in several, the
# one whose years come nearest the snapshot's, as the page picks it); it stays picked there only while a period of that
# country near the year lists it, so one drawn in years its country's periods don't cover would hand the pick over
def seg_in(ps, y):
    y = 1 if y == 0 else y
    return next((k for k, p in enumerate(ps) if y <= p['span'][1]), len(ps) - 1)


for n in names:
    for j in present[n]:
        a, b = file_span(j)
        lid = home_in(n, j)
        ps = byid[lid]['periods']
        lo, hi = ps[0]['span'][0], ps[-1]['span'][1]
        if b < lo or a > hi: continue   # outside the country's years: reported above
        y = max(a, lo); i = seg_in(ps, y)
        near = {seg_in(ps, a), *(k for k in (i - 1, i, i + 1) if 0 <= k < len(ps))}
        if not any(n in {s.lstrip('~') for s in ps[k]['states']} for k in near):
            warns.append(f"{lid}: {n!r} is drawn in {FILES[j]} but listed in no period near then")

# the shared peoples and labels: each on the map, and in at least two countries' stories (else sharing changes nothing)
listed = collections.defaultdict(set)
for l in _lib.LINEAGES:
    for p in l['periods']:
        for s in p['states']: listed[s.lstrip('~')].add(l['id'])
for n in sorted(set(_lib.SHARED)):
    if n not in present: errs.append(f'shared {n!r}: no state is called that in the border files')
    elif len(listed[n]) < 2: errs.append(f"shared {n!r}: listed by {', '.join(sorted(listed[n])) or 'no country'} only")
if len(_lib.SHARED) != len(set(_lib.SHARED)): errs.append('shared: a name listed twice')

for w in warns: print('warning:', w)
for e in errs: print('ERROR:', e)

# the years each state with no country is on the map, so a click on it can show them
# (a state in one snapshot only needs none: the page takes that snapshot's years)
seen = {}
for n, idx in present.items():
    if n in names or len(idx) < 2: continue
    seen[n] = [YEARS[idx[0]], None if idx[-1] == len(FILES) - 1 else YEARS[idx[-1] + 1] - 1]

if REPORT:
    print('\nStates the simplified map shows that belong to no country (snapshots x size):')
    score = collections.Counter(); where = {}
    for i, rows in enumerate(snap):
        for r in rows:
            if r['major'] and r['name'] not in names and not NOT_STATE.search(r['name']):
                score[r['name']] += r['km2'] ** .5; where.setdefault(r['name'], []).append(FILES[i])
    for n, s in score.most_common(150):
        print(f"  {n!r:48} {round(s):6}  {where[n][0]}..{where[n][-1]} x{len(where[n])}")

if errs: sys.exit(1)

out = []
for l in _lib.LINEAGES:
    ps = []
    for p in l['periods']:
        short = p['short'] or re.sub(r' (dynasty|period)$', '', p['name'])
        e = dict(name=p['name'], **({'short': short} if short != p['name'] else {}), **{'from': p['start'], 'to': p['end']})
        if p['note']: e['note'] = p['note']
        e['states'] = p['states']
        ps.append(e)
    out.append(dict(id=l['id'], name=l['name'], region=l['region'], core=l['core'], periods=ps))
with open(os.path.join(DATA, 'lineages.json'), 'w') as fh:
    json.dump(dict(lineages=out, names=names, seen=seen, shared=sorted(set(_lib.SHARED))), fh,
              ensure_ascii=False, separators=(',', ':'))
print(f"{len(out)} countries, {sum(len(l['periods']) for l in out)} periods, {len(names)} states with a country, "
      f"{len(seen)} without, {len(set(_lib.SHARED))} shared; {len(warns)} warnings; "
      f"{os.path.getsize(os.path.join(DATA, 'lineages.json')) // 1024} KB")

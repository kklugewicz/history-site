"""Adds map extras to data/wars.json so the page can show wars on the ordinary map.

For every war step:
- "contact": where the sides' territories touch (lines of [lon, lat]), computed from the border file the
  step is drawn on. Only for steps without hand-drawn "fronts"; the page draws swords along fronts or contacts.
- moves get "sea": true when the army went by sea (most of its route is over water, or a fleet on a
  partly-sea route); the page draws ships for them.
- events get "sea": true when they happened at sea (a naval battle).

Run from the repository root after scripts/merge_wars.py:  python3 scripts/war_extras.py
It is idempotent: it recomputes the extras each time.
"""
import json, re, os
from shapely.geometry import shape, Point, LineString, MultiLineString
from shapely.ops import unary_union, linemerge

DATA = 'data'
tl = json.load(open(os.path.join(DATA, 'timeline.json')))
FILES = tl['borderFiles']
fy = lambda f: -int(f[2:]) if f.startswith('bc') else int(f)


def file_for(year):
    best = FILES[0]
    for f in FILES:
        if fy(f) <= year:
            best = f
    return best


_geo = {}
def polities(f):
    if f not in _geo:
        fc = json.load(open(os.path.join(DATA, f'borders_{f}.json')))
        d = {}
        for ft in fc['features']:
            g = shape(ft['geometry']).buffer(0)
            n = ft['properties']['name']
            d[n] = d[n].union(g) if n in d else g
        _geo[f] = d
    return _geo[f]


_land = json.load(open(os.path.join(DATA, 'land.json')))
land = shape(_land['geometry'] if _land.get('type') == 'Feature' else _land).buffer(0)

NAVAL = re.compile(r'fleet|navy|naval|armada|squadron|\bships?\b|galleys|flotilla|convoy|u-boat|submarine|carrier|task force|longship|corsair|privateer', re.I)


def densify(path, step=0.25):
    pts = []
    for (x0, y0), (x1, y1) in zip(path, path[1:]):
        n = max(1, int(max(abs(x1 - x0), abs(y1 - y0)) / step))
        for i in range(n):
            pts.append((x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n))
    pts.append(tuple(path[-1][:2]))
    return pts


def sea_frac(path):
    pts = densify([p[:2] for p in path])
    return sum(1 for p in pts if not land.contains(Point(p))) / len(pts)


def rnd(c):
    return [round(c[0], 2), round(c[1], 2)]


def contact_lines(step):
    terr = step.get('territories') or []
    sides = {}
    f = file_for(step['year'])
    geo = polities(f)
    for t in terr:
        for n in t['polities']:
            if n in geo:
                sides.setdefault(t['side'], []).append(geo[n])
    keys = sorted(sides)
    out = []
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            A = unary_union(sides[a]).buffer(0)
            B = unary_union(sides[b]).buffer(0)
            line = A.boundary.intersection(B.buffer(0.12))
            if line.is_empty:
                continue
            parts = []
            geoms = getattr(line, 'geoms', [line])
            ls = [g for g in geoms if g.geom_type == 'LineString']
            for g in geoms:
                if g.geom_type == 'MultiLineString':
                    ls.extend(g.geoms)
            if not ls:
                continue
            merged = linemerge(MultiLineString(ls)) if len(ls) > 1 else ls[0]
            for g in getattr(merged, 'geoms', [merged]):
                g = g.simplify(0.05)
                if g.length >= 0.6:
                    parts.append(g)
            parts.sort(key=lambda g: -g.length)
            for g in parts[:6]:
                out.append({'sides': [a, b], 'path': [rnd(c) for c in g.coords]})
    return out


wars = json.load(open(os.path.join(DATA, 'wars.json')))
nc = nm = ne = 0
for w in wars:
    for st in w['steps']:
        st.pop('contact', None)
        if not st.get('fronts'):
            c = contact_lines(st)
            if c:
                st['contact'] = c
                nc += 1
        for m in st.get('moves', []):
            m.pop('sea', None)
            if len(m.get('path', [])) < 2:
                continue
            sf = sea_frac(m['path'])
            txt = (m.get('label') or '') + ' ' + (m.get('commander') or '')
            if sf >= 0.6 or (NAVAL.search(txt) and sf >= 0.2):
                m['sea'] = True
                nm += 1
        for e in st.get('events', []):
            e.pop('sea', None)
            p = Point(e['lon'], e['lat'])
            if not land.contains(p) and land.distance(p) > 0.03:
                e['sea'] = True
                ne += 1
json.dump(wars, open(os.path.join(DATA, 'wars.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(f'contacts on {nc} steps, {nm} sea moves, {ne} sea events')

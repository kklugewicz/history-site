"""Builds data/migrations.json: the peoples on the move that the map draws through time.

Run from the repository root:  python3 content/migrations/build_migrations.py
It loads every content/migrations/mNN_*.py (see _lib.py for the format), checks lengths that fit the panel, years,
places and links (war= must be a war in data/wars.json, story= a story in data/events/ or data/stories/), checks that
sea moves stay off land except near their waypoints (needs shapely), and writes the file.
"""
import glob, importlib.util, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import _lib  # noqa: E402

KINDS = {'folk', 'nomads', 'seafarers', 'settlers', 'forced', 'exiles', 'refugees', 'emigrants'}
BY = {'foot', 'wagon', 'horse', 'river', 'canoe', 'galley', 'longship', 'sail', 'steam', 'train', 'plane'}
SEA = {'canoe', 'galley', 'longship', 'sail', 'steam'}
LIM = dict(name=44, people=26, summary=560, numbers=90, label=24, title=52, text=430, site=170, sitename=40, movelabel=30)
DASH = re.compile('[–—]')

errors, warnings = [], []
err = errors.append
warn = warnings.append


def main():
    for f in sorted(glob.glob(os.path.join(HERE, 'm[0-9][0-9]_*.py'))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        spec.loader.exec_module(importlib.util.module_from_spec(spec))
    mig = _lib.MIG
    wars = {w['id'] for w in json.load(open(os.path.join(ROOT, 'data', 'wars.json')))}
    evs = {e['id'] for e in json.load(open(os.path.join(ROOT, 'data', 'events', 'index.json')))['events']}
    try:
        from shapely.geometry import shape, Point
        from shapely.prepared import prep
        land = prep(shape(json.load(open(os.path.join(ROOT, 'data', 'land.json')))['geometry']))
    except ImportError:
        land = None
        warn('shapely is not installed: sea moves were not checked against the coastline')
    ids = set()
    for m in mig:
        i = m['id']
        if i in ids: err(f'{i}: duplicate id')
        ids.add(i)
        if m['kind'] not in KINDS: err(f'{i}: kind {m["kind"]!r}')
        if not re.fullmatch(r'#[0-9a-f]{6}', m['color']): err(f'{i}: colour {m["color"]!r}')
        if not (-10000 <= m['start'] < m['end'] <= 2025): err(f'{i}: years {m["start"]}..{m["end"]}')
        if m['rank'] not in (1, 2): err(f'{i}: rank')
        if m['war'] and m['war'] not in wars: err(f'{i}: no war {m["war"]!r}')
        if m['story'] and not (m['story'].startswith('ev:') and m['story'][3:] in evs): err(f'{i}: no story {m["story"]!r}')
        for k in ('name', 'people', 'summary', 'numbers'):
            v = m[k] or ''
            if len(v) > LIM[k]: err(f'{i}: {k} is {len(v)} long (max {LIM[k]})')
            if DASH.search(v): err(f'{i}: {k} has a long dash')
        if not 2 <= len(m['steps']) <= 8: err(f'{i}: {len(m["steps"])} steps')
        last = -1e9
        for n, s in enumerate(m['steps']):
            w = f'{i} step {n + 1}'
            if s['year'] < last: err(f'{w}: year goes back')
            last = s['year']
            if not m['start'] <= s['year'] <= m['end']: err(f'{w}: year {s["year"]} outside the migration')
            for k in ('label', 'title', 'text'):
                if not s[k]: err(f'{w}: no {k}')
                if len(s[k]) > LIM[k]: err(f'{w}: {k} is {len(s[k])} long (max {LIM[k]})')
                if DASH.search(s[k]): err(f'{w}: {k} has a long dash')
            if not s['moves'] and not s['sites']: err(f'{w}: nothing on the map')
            for mo in s['moves']:
                p = mo['path']
                if mo['by'] not in BY: err(f'{w}: by {mo["by"]!r}')
                if len(p) < 2: err(f'{w}: a move needs two points')
                if mo['label'] and len(mo['label']) > LIM['movelabel']: err(f'{w}: move label too long')
                for a in p:
                    if len(a) != 3: err(f'{w}: point {a} needs lon, lat, year'); continue
                    if not (-180 <= a[0] <= 180 and -85 <= a[1] <= 85): err(f'{w}: point {a} off the globe')
                    if not m['start'] <= a[2] <= m['end']: err(f'{w}: point {a} outside the years {m["start"]}..{m["end"]}')
                if any(p[j][2] < p[j - 1][2] for j in range(1, len(p))): err(f'{w}: move years go back')
                if mo['until'] is not None and not (p[-1][2] <= mo['until'] <= m['end']): err(f'{w}: until {mo["until"]}')
                if land and mo['by'] in SEA: sea_check(w, mo, land, Point)
            for x in s['sites']:
                if len(x['text']) > LIM['site'] or len(x['name']) > LIM['sitename']: err(f'{w}: site {x["name"]} text too long')
                if DASH.search(x['text']): err(f'{w}: site {x["name"]} has a long dash')
                if not m['start'] <= x['year'] <= m['end']: err(f'{w}: site {x["name"]} year {x["year"]} outside')
    for e in errors: print('ERROR', e)
    for e in warnings: print('warning', e)
    if errors: sys.exit(1)
    r2 = lambda v: round(v, 2)
    out = []
    for m in sorted(mig, key=lambda m: (m['start'], m['id'])):
        o = {k: m[k] for k in ('id', 'name', 'people', 'kind', 'color', 'start', 'end', 'rank', 'summary') }
        for k in ('war', 'story', 'numbers'):
            if m[k]: o[k] = m[k]
        o['steps'] = []
        for s in m['steps']:
            so = {k: s[k] for k in ('year', 'label', 'title', 'text')}
            if s['moves']: so['moves'] = [dict({'by': mo['by'], 'path': [[r2(a[0]), r2(a[1]), a[2]] for a in mo['path']]},
                                               **({'label': mo['label']} if mo['label'] else {}), **({'until': mo['until']} if mo['until'] is not None else {})) for mo in s['moves']]
            if s['sites']: so['sites'] = [dict(x, lon=r2(x['lon']), lat=r2(x['lat'])) for x in s['sites']]
            o['steps'].append(so)
        out.append(o)
    path = os.path.join(ROOT, 'data', 'migrations.json')
    with open(path, 'w') as f: json.dump({'migrations': out}, f, ensure_ascii=False, separators=(',', ':'))
    moves = sum(len(s.get('moves', [])) for m in out for s in m['steps'])
    print(f'{len(out)} migrations, {sum(len(m["steps"]) for m in out)} steps, {moves} moves, {os.path.getsize(path) // 1024} KB')


def sea_check(w, mo, land, Point):
    """A ship may touch land only within 0.7 degrees of a waypoint (a port or a cape it rounds)."""
    p = mo['path']
    for j in range(1, len(p)):
        a, b = p[j - 1], p[j]
        if abs(a[0] - b[0]) > 180: continue   # across the date line: open Pacific
        d = math.hypot(a[0] - b[0], a[1] - b[1]); n = max(2, int(d / .15))
        run = []
        for t in range(1, n):
            x, y = a[0] + (b[0] - a[0]) * t / n, a[1] + (b[1] - a[1]) * t / n
            if math.hypot(x - a[0], y - a[1]) < .7 or math.hypot(x - b[0], y - b[1]) < .7: continue
            if land.contains(Point(x, y)): run.append((round(x, 2), round(y, 2)))
        if run: err(f'{w}: sea leg {j} {a[:2]} -> {b[:2]} crosses land at {run[0]}..{run[-1]} ({len(run)})')


if __name__ == '__main__':
    main()

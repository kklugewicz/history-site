"""Builds data/cities.json from content/cities/cities.py (the cities, their names, ranks and landmarks over time) and
content/cities/icons.py (the landmark silhouettes, one SVG path each in a 100 x 100 box).

    python3 scripts/build_cities.py

Output: {icons: {id: path}, cities: [{id, at: [lon, lat], y: [first, last], n: [[from, name]], r: [[from, rank]], lm: [[from, icon, label]], now}]}
Each list is sorted by year and each entry holds until the next one; the page shows a city between its first and last year.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'content', 'cities'))
from icons import ICONS  # noqa: E402
from cities import CITIES  # noqa: E402


def steps(v, first, what, cid):
    out = [[first, v]] if not isinstance(v, list) else [list(e) for e in v]
    ys = [e[0] for e in out]
    assert ys == sorted(ys) and len(set(ys)) == len(ys), f'{cid}: {what} out of order: {ys}'
    assert ys[0] <= first, f'{cid}: {what} starts at {ys[0]}, after the city ({first})'
    return out


def main():
    used, out, ids = set(), [], set()
    for c in CITIES:
        cid = c['id']
        assert cid not in ids, f'{cid}: listed twice'
        ids.add(cid)
        first, last = c['years']
        assert last is None or last > first, f'{cid}: ends before it starts'
        assert -180 <= c['lon'] <= 180 and -90 <= c['lat'] <= 90, f'{cid}: bad position'
        n = steps(c['names'], first, 'names', cid)
        r = steps(c['ranks'], first, 'ranks', cid)
        for e in r: assert e[1] in (0, 1, 2, 3), f'{cid}: rank {e[1]}'
        lm = []
        for e in steps(c['lms'], first, 'landmarks', cid):
            y, icon, label = (e + [None])[:3]
            assert icon in ICONS, f'{cid}: no icon {icon!r}'
            assert last is None or y <= last, f'{cid}: landmark {icon} after the city ends'
            used.add(icon)
            lm.append([y, icon, label] if label else [y, icon])
        d = {'id': cid, 'at': [round(c['lon'], 3), round(c['lat'], 3)], 'y': [first, last], 'n': n, 'r': r, 'lm': lm}
        if c['now']: d['now'] = c['now']
        out.append(d)
    unused = sorted(set(ICONS) - used)
    if unused: print('icons not used by any city:', ', '.join(unused))
    data = {'icons': {k: ICONS[k] for k in sorted(used)}, 'cities': out}
    path = os.path.join(ROOT, 'data', 'cities.json')
    with open(path, 'w') as fh: json.dump(data, fh, ensure_ascii=False, separators=(',', ':'))
    print(f'{len(out)} cities, {len(used)} landmarks, {os.path.getsize(path) // 1024} KB -> data/cities.json')


if __name__ == '__main__':
    main()

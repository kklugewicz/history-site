"""Check a zones_<area>.json file. Usage: python3 validate_zones.py zones_x.json"""
import json, sys, os, re
from shapely.geometry import shape, Point
H = os.path.dirname(os.path.abspath(__file__))
den = {d['id']: d for d in json.load(open(os.path.join(H, 'denominations.json')))}
land = shape(json.load(open(os.path.join(H, 'land.json')))['geometry']).buffer(0.6)
zones = json.load(open(sys.argv[1])); errs = []; ids = set()
for z in zones:
    Z = z.get('id', '?')
    for k in ('id', 'name', 'lon', 'lat', 'history'):
        if k not in z: errs.append(f'{Z}: missing {k}')
    if Z in ids: errs.append(f'{Z}: duplicate id')
    ids.add(Z)
    if not re.fullmatch(r'[a-z0-9-]+', str(Z)): errs.append(f'{Z}: id must be kebab-case')
    if not (-180 <= z.get('lon', 999) <= 180 and -60 <= z.get('lat', 999) <= 85): errs.append(f'{Z}: lon/lat out of range')
    elif not land.contains(Point(z['lon'], z['lat'])): errs.append(f'{Z}: anchor {z["lon"]},{z["lat"]} is not on land (lon first!)')
    h = z.get('history', [])
    if not h or h[0].get('from', 0) > -3000: errs.append(f'{Z}: history must start at or before -3000')
    prev = None
    for e in h:
        f = e.get('faith')
        if f not in den: errs.append(f'{Z}: unknown faith {f}'); continue
        if not isinstance(e.get('from'), int): errs.append(f'{Z}: from must be an integer year'); continue
        if prev is not None and e['from'] <= prev['from']: errs.append(f'{Z}: years not increasing at {e["from"]}')
        if prev is not None and prev['faith'] == f: errs.append(f'{Z}: {f} repeated back to back at {e["from"]}')
        st = den[f]['start']
        if st is not None and e['from'] < st - 50: errs.append(f'{Z}: {f} at {e["from"]} predates its start {st}')
        if f == 'christian' and e['from'] >= 1054: errs.append(f'{Z}: use catholic/orthodox after 1054, not christian')
        n = e.get('note', '')
        if not n or len(n) > 260: errs.append(f'{Z}: note missing or over 260 chars at {e["from"]}')
        if re.search('[–—]', n + z.get('name', '')): errs.append(f'{Z}: en/em dash in text')
        prev = e
if errs: print('\n'.join(errs)); sys.exit(1)
print(f'OK: {len(zones)} zones, {sum(len(z["history"]) for z in zones)} entries')

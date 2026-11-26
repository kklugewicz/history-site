"""Builds data/stories/ from the story files in this folder (sNN_*.py) and checks them.

Run from the repository root:  python3 content/stories/build_stories.py
Writes data/stories/<person id>.json (one story, loaded when it is opened), data/stories/index.json (who has a story,
with the line under their name) and content/stories/media.txt (every Wikipedia title and recording page the stories
ask for, to check against Wikipedia from a machine that can reach it).
Checks: each story belongs to one of the 200 people in chosen.py and each of them has one; 5 to 12 pages in a known
kind, legacy last and only there, with 2 to 4 points; lengths that fit the card; places that resolve; sane years.
"""
import json, os, sys, glob, importlib.util, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data')
sys.path.insert(0, HERE)
import _lib
from chosen import CHOSEN

for f in sorted(glob.glob(os.path.join(HERE, 's[0-9][0-9]_*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    spec.loader.exec_module(importlib.util.module_from_spec(spec))

people = {p['id']: p for p in json.load(open(os.path.join(DATA, 'people.json')))['people']}
# place names written on the card, where the key spelled out would be wrong
PRETTY = {
    'thebes_gr': 'Thebes', 'trier2': 'Trier', 'santiago_c': 'Santiago de Compostela', 'the_hague': 'The Hague',
    'st_petersburg': 'St Petersburg', 'port_au_prince': 'Port-au-Prince', 'dar_es_salaam': 'Dar es Salaam',
    'lanse_aux_meadows': "L'Anse aux Meadows", 'new_york': 'New York', 'washington': 'Washington, D.C.',
    'mount_sinai': 'Mount Sinai', 'saint_denis': 'Saint-Denis', 'ain_jalut': 'Ain Jalut', 'tel_aviv': 'Tel Aviv',
    'lake_trasimene': 'Lake Trasimene', 'new_carthage': 'Cartagena', 'kitty_hawk': 'Kitty Hawk', 'menlo_park': 'Menlo Park',
    'los_alamos': 'Los Alamos', 'cape_canaveral': 'Cape Canaveral', 'lutetia': 'Paris', 'constantinople': 'Constantinople',
    'springfield_il': 'Springfield', 'rochester_ny': 'Rochester', 'auburn_ny': 'Auburn', 'milan_ohio': 'Milan, Ohio',
    'gads_hill': "Gad's Hill", 'schonhausen': 'Schönhausen', 'koniggratz': 'Königgrätz', 'saint_remy': 'Saint-Rémy',
    'auvers': 'Auvers-sur-Oise', 'le_havre': 'Le Havre', 'yasnaya_polyana': 'Yasnaya Polyana', 'pribor': 'Příbor',
    'combahee': 'Combahee River', 'osborne': 'Osborne House', 'niagara': 'Niagara Falls', 'heinzendorf': 'Heinzendorf',
    'highland_park_mi': 'Highland Park', 'south_pole': 'South Pole', 'framheim': 'Bay of Whales', 'blenheim': 'Blenheim Palace',
    'kim_lien': 'Kim Liên', 'pac_bo': 'Pác Bó', 'colombey': 'Colombey', 'neauphle': 'Neauphle-le-Château', 'guang_an': "Guang'an",
    'pt_109': 'Solomon Islands', 'birmingham_al': 'Birmingham, Alabama', 'memphis_tn': 'Memphis', 'bergen_belsen': 'Bergen-Belsen',
    'cambridge_ma': 'Cambridge, Massachusetts', 'portland_or': 'Portland, Oregon', 'treetops': 'Treetops, Kenya',
    'mezzegra': 'Lake Como', 'vatican': 'Vatican City', 'edwards': 'Edwards Air Force Base', 'cern': 'CERN, Geneva',
}
SMALL = {'of', 'de', 'da', 'del', 'la', 'le', 'the', 'and', 'on', 'upon', 'aux', 'du', 'des', 'van', 'von', 'al'}


def pretty(key):
    if key in PRETTY:
        return PRETTY[key]
    w = re.sub(r'\d+$', '', key).split('_')
    return ' '.join(x if (i and x in SMALL) else x.capitalize() for i, x in enumerate(w))


LIMITS = {'t': 56, 'x': 430, 'fx': 260, 'pt': 80, 'hook': 120, 'cap': 90, 'wh': 34}
errs, warns, media = [], [], []
chosen = set(CHOSEN)
if len(CHOSEN) != len(chosen):
    errs.append('chosen.py lists someone twice')
for pid in CHOSEN:
    if pid not in people:
        errs.append(f'chosen: {pid} is not in data/people.json')

out = {}
for pid, st in _lib.STORIES.items():
    who = pid
    if pid not in chosen:
        errs.append(f'{who}: not one of the 200 in chosen.py')
    p = people.get(pid)
    if not p:
        errs.append(f'{who}: no such person'); continue
    b, d = p['life']
    hook, pages = st['hook'], st['pages']
    if not hook or len(hook) > LIMITS['hook']:
        errs.append(f'{who}: hook is {len(hook or "")} chars (max {LIMITS["hook"]})')
    if not 5 <= len(pages) <= 12:
        errs.append(f'{who}: {len(pages)} pages (5 to 12)')
    kinds = [pg['k'] for pg in pages]
    if kinds.count('legacy') != 1 or kinds[-1] != 'legacy':
        errs.append(f'{who}: the legacy page must come last, once')
    res = []
    for i, pg in enumerate(pages):
        at = f'{who} page {i + 1} ({pg["k"]} "{pg.get("t", "")[:30]}")'
        if pg['k'] not in _lib.KINDS:
            errs.append(f'{at}: kind {pg["k"]}')
        for k in ('t', 'x'):
            if not pg.get(k):
                errs.append(f'{at}: missing {k}')
        lim_x = 260 if pg['k'] == 'made' else 330 if pg['k'] == 'legacy' else LIMITS['x']
        if len(pg.get('t', '')) > LIMITS['t']:
            errs.append(f'{at}: title is {len(pg["t"])} chars (max {LIMITS["t"]})')
        if len(pg.get('x', '')) > lim_x:
            errs.append(f'{at}: text is {len(pg["x"])} chars (max {lim_x})')
        if pg['k'] == 'made' and (not pg.get('fx') or len(pg['fx']) > LIMITS['fx']):
            errs.append(f'{at}: effect is {len(pg.get("fx") or "")} chars (1 to {LIMITS["fx"]})')
        if pg['k'] == 'legacy':
            pts = pg.get('pts') or []
            if not 2 <= len(pts) <= 4:
                errs.append(f'{at}: {len(pts)} points (2 to 4)')
            for t in pts:
                if len(t) > LIMITS['pt']:
                    errs.append(f'{at}: point is {len(t)} chars (max {LIMITS["pt"]}): {t[:40]}')
        for k in ('t', 'x', 'fx', 'cap'):
            v = pg.get(k) or ''
            if '—' in v or ' - ' in v or '--' in v:
                warns.append(f'{at}: dash in {k}')
            if re.search(r'\s{2,}|\s[,.;:]', v):
                warns.append(f'{at}: stray space in {k}')
        if pg.get('cap') and len(pg['cap']) > LIMITS['cap']:
            errs.append(f'{at}: caption is {len(pg["cap"])} chars (max {LIMITS["cap"]})')
        y = pg.get('y')
        if y is not None:
            if not isinstance(y, int) or y == 0:
                errs.append(f'{at}: year {y!r}')
            elif b is not None and y < b - 1:
                errs.append(f'{at}: year {y} before birth {b}')
        q = {'k': pg['k'], 't': pg['t'], 'x': pg['x']}
        for k in ('fx', 'img', 'cap', 'y', 'au', 'listen', 'pts', 'kick'):
            if pg.get(k) is not None:
                q[k] = pg[k]
        place = pg.get('at')
        if place is not None:
            if isinstance(place, str):
                if place not in _lib.C:
                    errs.append(f'{at}: unknown place {place}')
                    continue
                lon, lat = _lib.C[place][:2]
                q['wh'] = pg.get('where') or pretty(place)
            else:
                lon, lat = place[:2]
                if not pg.get('where'):
                    errs.append(f'{at}: a place given as (lon, lat) needs where=')
                q['wh'] = pg.get('where', '')
            if not (-180 <= lon <= 180 and -90 <= lat <= 90):
                errs.append(f'{at}: place {lon},{lat}')
            if len(q['wh']) > LIMITS['wh']:
                errs.append(f'{at}: place name "{q["wh"]}" is long')
            q['at'] = [round(lon, 2), round(lat, 2)]
        elif pg.get('where'):
            errs.append(f'{at}: where= without at=')
        if pg['k'] == 'song' and not (pg.get('au') or pg.get('listen')):
            warns.append(f'{at}: a song page without a recording or a link (it will search for one)')
        if pg.get('img'):
            media.append(pg['img'])
        if pg.get('au'):
            media.append('audio: ' + pg['au']['page'] + (' | ' + pg['au']['hint'] if pg['au'].get('hint') else ''))
        res.append(q)
    out[pid] = {'id': pid, 'hook': hook, 'pages': res}

missing = [pid for pid in CHOSEN if pid not in _lib.STORIES]
if missing:
    warns.append(f'{len(missing)} of the 200 have no story yet: {" ".join(missing[:12])}{" ..." if len(missing) > 12 else ""}')
for e in errs:
    print('ERROR', e)
for w in warns:
    print('warn ', w)
if errs:
    sys.exit(f'{len(errs)} errors')

dest = os.path.join(DATA, 'stories')
os.makedirs(dest, exist_ok=True)
for f in glob.glob(os.path.join(dest, '*.json')):
    os.remove(f)
size = 0
for pid, st in out.items():
    s = json.dumps(st, ensure_ascii=False, separators=(',', ':'))
    size += len(s.encode())
    open(os.path.join(dest, pid + '.json'), 'w').write(s)
order = [pid for pid in CHOSEN if pid in out]
idx = {'ids': {pid: out[pid]['hook'] for pid in order}}
open(os.path.join(dest, 'index.json'), 'w').write(json.dumps(idx, ensure_ascii=False, separators=(',', ':')))
open(os.path.join(HERE, 'media.txt'), 'w').write('\n'.join(sorted(set(media))) + '\n')
pages = sum(len(s['pages']) for s in out.values())
print(f'{len(out)} stories, {pages} pages, {len(set(media))} pictures and recordings; {size // 1024} KB')

"""Builds data/events/ from the event story files in this folder (eNN_*.py) and checks them.

Run from the repository root:  python3 content/events/build_events.py
Writes data/events/<event id>.json (one story's pages, loaded when it is opened), data/events/index.json (every
event: name, kind, years, hook, cover, war, place and the states it belongs to) and content/events/media.txt (every
Wikipedia title and recording page the stories ask for, to check from a machine that can reach Wikipedia).
Checks: 5 to 12 pages of a known kind, legacy last and only there, with 2 to 4 points; lengths that fit the card;
places that resolve; sane years; people who exist; states spelled as in the border files of the event's years;
wars that exist in data/wars.json.
"""
import json, os, sys, glob, importlib.util, re, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data')
sys.path.insert(0, HERE)
import _lib

for f in sorted(glob.glob(os.path.join(HERE, 'e[0-9][0-9]_*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    spec.loader.exec_module(importlib.util.module_from_spec(spec))

people = {p['id']: p for p in json.load(open(os.path.join(DATA, 'people.json')))['people']}
try:
    with_story = set(json.load(open(os.path.join(DATA, 'stories', 'index.json')))['ids'])
except OSError:
    with_story = set()
wars = {w['id']: w for w in json.load(open(os.path.join(DATA, 'wars.json')))}
files = json.load(open(os.path.join(DATA, 'timeline.json')))['borderFiles']
fyear = lambda f: -int(f[2:]) if f.startswith('bc') else int(f)
names = {f: {x['properties']['name'] for x in json.load(open(os.path.join(DATA, f'borders_{f}.json')))['features']} for f in files}
every_name = set().union(*names.values())


def file_for(y):
    ok = [f for f in files if fyear(f) <= y]
    return ok[-1] if ok else files[0]


def files_over(a, b, slack=1):
    """the border files in use from year a to year b, and `slack` files either side"""
    i, j = files.index(file_for(a)), files.index(file_for(b))
    return files[max(0, i - slack): j + 1 + slack]


# place names written on the card, where the key spelled out would be wrong (the people's stories have more)
PRETTY = {
    'guanahani': 'Guanahani, Bahamas', 'la_navidad': 'La Navidad, Hispaniola', 'santa_fe_gr': 'Santa Fe, Granada',
    'canary_gomera': 'La Gomera, Canary Islands',
}
_stories_build = os.path.join(os.path.dirname(HERE), 'stories', 'build_stories.py')
for m in re.finditer(r"'([a-z0-9_]+)': (\"[^\"]*\"|'[^']*')", open(_stories_build).read().split('PRETTY = {', 1)[1].split('\n}', 1)[0]):
    PRETTY.setdefault(m.group(1), m.group(2)[1:-1])
SMALL = {'of', 'de', 'da', 'del', 'la', 'le', 'the', 'and', 'on', 'upon', 'aux', 'du', 'des', 'van', 'von', 'al'}


def pretty(key):
    if key in PRETTY:
        return PRETTY[key]
    w = re.sub(r'\d+$', '', key).split('_')
    return ' '.join(x if (i and x in SMALL) else x.capitalize() for i, x in enumerate(w))


LIMITS = {'name': 48, 't': 56, 'x': 430, 'fx': 260, 'pt': 80, 'hook': 120, 'cap': 90, 'wh': 34, 'num': 22, 'of': 44}
errs, warns, media = [], [], []


def place(at, where, ctx):
    """[lon, lat] and the name to write for a place key or a (lon, lat) pair"""
    if isinstance(at, str):
        if at not in _lib.C:
            errs.append(f'{ctx}: unknown place {at}')
            return None, None
        lon, lat = _lib.C[at][:2]
        wh = where or pretty(at)
    else:
        lon, lat = at[:2]
        if not where:
            errs.append(f'{ctx}: a place given as (lon, lat) needs where=')
        wh = where or ''
    if not (-180 <= lon <= 180 and -90 <= lat <= 90):
        errs.append(f'{ctx}: place {lon},{lat}')
    if len(wh) > LIMITS['wh']:
        errs.append(f'{ctx}: place name "{wh}" is long')
    return [round(lon, 2), round(lat, 2)], wh


def text_checks(v, ctx, key):
    if '—' in v or '–' in v or ' - ' in v or '--' in v:
        warns.append(f'{ctx}: dash in {key}')
    if re.search(r'\s{2,}|\s[,.;:]', v):
        warns.append(f'{ctx}: stray space in {key}')


index, out = [], {}
for eid, ev in _lib.EVENTS.items():
    who = eid
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', eid):
        errs.append(f'{who}: id must be lowercase words joined by hyphens')
    a, b = ev['years']
    if not (isinstance(a, int) and isinstance(b, int)) or a == 0 or b == 0 or a > b:
        errs.append(f'{who}: years {ev["years"]!r}')
        continue
    if ev['kind'] not in _lib.KINDS:
        errs.append(f'{who}: kind {ev["kind"]!r} (one of {", ".join(_lib.KINDS)})')
    if not ev['name'] or len(ev['name']) > LIMITS['name']:
        errs.append(f'{who}: name is {len(ev["name"] or "")} chars (max {LIMITS["name"]})')
    hook, pages = ev['hook'], ev['pages']
    if not hook or len(hook) > LIMITS['hook']:
        errs.append(f'{who}: hook is {len(hook or "")} chars (max {LIMITS["hook"]})')
    text_checks(hook or '', who, 'hook')
    if not ev['wiki']:
        errs.append(f'{who}: needs wiki= (the article for "Read more")')
    if ev['img'] and ev['img'].startswith('File:'):
        errs.append(f'{who}: the cover img= must be an article, so the trays can show its picture')
    if ev['label'] and len(ev['label']) > 28:
        errs.append(f'{who}: label is long')
    if not 5 <= len(pages) <= 12:
        errs.append(f'{who}: {len(pages)} pages (5 to 12)')
    kinds = [pg['k'] for pg in pages]
    if kinds.count('legacy') != 1 or kinds[-1] != 'legacy':
        errs.append(f'{who}: the legacy page must come last, once')
    # the states it belongs to
    st = []
    pool = set().union(*(names[f] for f in files_over(a, b)))
    for n in ev['states']:
        if n in st:
            warns.append(f'{who}: state {n} listed twice')
            continue
        if n not in pool:
            near = difflib.get_close_matches(n, sorted(pool), n=3, cutoff=.6)
            where_else = sorted({fyear(f) for f in files if n in names[f]})
            hint = f'; did you mean {", ".join(near)}?' if near else ''
            if where_else:
                hint += f' (it is in the border files of {", ".join(str(y) for y in where_else[:6])})'
            errs.append(f'{who}: state "{n}" is not in the border files of {a} to {b}{hint}')
        st.append(n)
    war = ev['war']
    if war:
        w = wars.get(war)
        if not w:
            errs.append(f'{who}: no war {war} in data/wars.json')
        else:
            for s in w['steps']:
                for t in s.get('territories', []):
                    for n in t['polities']:
                        if n not in st:
                            st.append(n)
            if not (w['start'] - 2 <= a and b <= w['end'] + 2):
                warns.append(f'{who}: years {a} to {b} go beyond its war, {w["start"]} to {w["end"]}')
    if not st:
        errs.append(f'{who}: belongs to no state (give states= or war=)')
    res = []
    for i, pg in enumerate(pages):
        at = f'{who} page {i + 1} ({pg["k"]} "{pg.get("t", "")[:30]}")'
        if pg['k'] not in _lib.PAGE_KINDS:
            errs.append(f'{at}: kind {pg["k"]}')
        for k in ('t', 'x'):
            if not pg.get(k):
                errs.append(f'{at}: missing {k}')
        lim_x = 260 if pg['k'] == 'made' else 330 if pg['k'] in ('legacy', 'cost') else LIMITS['x']
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
        if pg['k'] == 'cost':
            if not pg.get('num') or len(pg['num']) > LIMITS['num']:
                errs.append(f'{at}: num is {len(pg.get("num") or "")} chars (1 to {LIMITS["num"]})')
            if pg.get('of') and len(pg['of']) > LIMITS['of']:
                errs.append(f'{at}: of= is {len(pg["of"])} chars (max {LIMITS["of"]})')
        if pg['k'] == 'figure':
            pid = pg.get('who')
            if pid is not None and pid not in people:
                errs.append(f'{at}: no person {pid} in data/people.json')
            if pid is None and not pg.get('img'):
                errs.append(f'{at}: a figure who is not on the map needs img=')
        for k in ('t', 'x', 'fx', 'cap', 'num', 'of'):
            text_checks(pg.get(k) or '', at, k)
        if pg.get('cap') and len(pg['cap']) > LIMITS['cap']:
            errs.append(f'{at}: caption is {len(pg["cap"])} chars (max {LIMITS["cap"]})')
        y = pg.get('y')
        if y is not None:
            if not isinstance(y, int) or y == 0:
                errs.append(f'{at}: year {y!r}')
            elif not (a - 400 <= y <= b + 800):
                warns.append(f'{at}: year {y} far from the event ({a} to {b})')
        q = {'k': pg['k'], 't': pg['t'], 'x': pg['x']}
        for k in ('fx', 'img', 'cap', 'y', 'au', 'listen', 'pts', 'kick', 'who', 'num', 'of'):
            if pg.get(k) is not None:
                q[k] = pg[k]
        if pg.get('at') is not None:
            xy, wh = place(pg['at'], pg.get('where'), at)
            if xy:
                q['at'], q['wh'] = xy, wh
        elif pg.get('where'):
            errs.append(f'{at}: where= without at=')
        if pg['k'] == 'song' and not (pg.get('au') or pg.get('listen')):
            warns.append(f'{at}: a song page without a recording or a link (it will search for one)')
        if pg.get('img'):
            media.append(pg['img'])
        if pg.get('au'):
            media.append('audio: ' + pg['au']['page'] + (' | ' + pg['au']['hint'] if pg['au'].get('hint') else ''))
        res.append(q)
    lb, ic = _lib.KINDS.get(ev['kind'], ('Event', 'star'))
    row = {'id': eid, 'name': ev['name'], 'kind': ev['kind'], 'lb': ev['label'] or lb, 'ic': ic, 'from': a, 'to': b, 'hook': hook, 'wiki': ev['wiki']}
    if ev['img']: row['img'] = ev['img']
    if war: row['war'] = war
    if ev['at'] is not None:
        xy, wh = place(ev['at'], ev['where'], who)
        if xy:
            row['at'], row['wh'] = xy, wh
    elif not war:
        warns.append(f'{who}: no at= (the story cannot show where it happened)')
    row['st'] = st
    index.append(row)
    media.append(ev['img'] or ev['wiki'])
    out[eid] = {'id': eid, 'pages': res}

told = {r['war'] for r in index if r.get('war')}
dup = [r['war'] for r in index if r.get('war')]
for wid in set(dup):
    if dup.count(wid) > 1:
        errs.append(f'war {wid} has more than one story')
for e in errs:
    print('ERROR', e)
for w in warns:
    print('warn ', w)
if errs:
    sys.exit(f'{len(errs)} errors')

index.sort(key=lambda r: (r['from'], r['to'], r['name']))
dest = os.path.join(DATA, 'events')
os.makedirs(dest, exist_ok=True)
for f in glob.glob(os.path.join(dest, '*.json')):
    os.remove(f)
size = 0
for eid, st in out.items():
    s = json.dumps(st, ensure_ascii=False, separators=(',', ':'))
    size += len(s.encode())
    open(os.path.join(dest, eid + '.json'), 'w').write(s)
ix = json.dumps({'events': index}, ensure_ascii=False, separators=(',', ':'))
open(os.path.join(dest, 'index.json'), 'w').write(ix)
open(os.path.join(HERE, 'media.txt'), 'w').write('\n'.join(sorted(set(media))) + '\n')
pages = sum(len(s['pages']) for s in out.values())
print(f'{len(out)} event stories ({len(told)} of {len(wars)} wars), {pages} pages, {len(set(media))} pictures and recordings; '
      f'{size // 1024} KB of pages, index {len(ix) // 1024} KB')

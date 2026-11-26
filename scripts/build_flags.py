"""Build the flags: every state's flag for each year it is on the map, the flag pictures, and map tints taken from them.

    python3 scripts/build_flags.py <source dir> data

Reads content/flags/flags.py (which flag each state flies, year by year, and the historical flags drawn in SVG) and
the border files in data/. Writes:
  data/flags.json         flags (title, kind, note, place in the sprite), each state's flag timeline, and the map tint of
                          every state in every border file, chosen from its flag's colours so that neighbours differ
  data/flags/sprite.webp  all flags at 48 x 36, for the small flags over state names
  data/flags/<id>.webp    each flag at 240 x 180, for the side panel

Modern flags come from flag-icons (MIT licence), fetched from npm into <source dir>/flag-icons when missing.
Rendering uses the Chromium that Playwright drives (node and playwright on the path); tints need numpy, shapely and Pillow."""
import base64, colorsys, json, math, os, re, subprocess, sys, tarfile, tempfile, urllib.request
import numpy as np
from PIL import Image
from shapely.geometry import shape
from shapely.strtree import STRtree
from shapely.ops import transform

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'content', 'flags'))
import flags as FL  # noqa: E402

SRC, OUT = sys.argv[1], sys.argv[2]
FI_VERSION = '7.6.0'
CELL = (48, 36)      # sprite cell
BIG = (240, 180)     # panel picture
COLS = 24


# ---------- sources ----------
def flag_icons():
    d = os.path.join(SRC, 'flag-icons')
    if not os.path.exists(os.path.join(d, 'package', 'flags', '4x3')):
        os.makedirs(d, exist_ok=True)
        tgz = os.path.join(d, 'flag-icons.tgz')
        print('fetching flag-icons', FI_VERSION)
        urllib.request.urlretrieve('https://registry.npmjs.org/flag-icons/-/flag-icons-%s.tgz' % FI_VERSION, tgz)
        with tarfile.open(tgz) as t:
            t.extractall(d, filter='data')
    return os.path.join(d, 'package', 'flags', '4x3')


fy = lambda f: -int(f[2:]) if f.startswith('bc') else int(f)
FILES = sorted([p[8:-5] for p in os.listdir(OUT) if p.startswith('borders_') and p.endswith('.json')], key=fy)
SPAN = {f: (fy(f), (fy(FILES[i + 1]) - 1) if i + 1 < len(FILES) else 2029) for i, f in enumerate(FILES)}
R = 6371.0
EQ = lambda g: transform(lambda x, y, z=None: (np.radians(x) * R, R * np.sin(np.radians(y))), g)

# the page's own rule for which states the simplified map colours (index.html, classify)
FAMOUS = re.compile(r'egypt|sumer|akkad|babylon|assyria|hittite|mycen|minoa|athen|sparta|greek|macedon|rom[ae]|carthag|phoenic|israel|juda|persia|maya|aztec|mexica|inca|olmec|harappa|indus|shang|zhou|qin|venice|venezia|genoa|papal|byzantine|kush|axum|aksum|mali|songhai|ghana|zimbabwe|khmer|champa|silla|goguryeo|baekje|japan|yamato|korea|joseon|goryeo|portugal|england|scotland|hungary|poland|bohemia|serbia|bulgaria|armenia|georgia|teotihuacan|zapotec|toltec|chim[uú]|moche|nazca|tiwanaku|wari|cahokia|ethiopia', re.I)
NOT_STATE = re.compile(r'hunter|gatherer|forag|fich|fisher|farmers|pastoral|herder|cultures?\b|khoi|bant[ou]|aborigin|siberians', re.I)


def load_file(fn):
    fc = json.load(open(os.path.join(OUT, 'borders_%s.json' % fn)))
    feats = []
    for ft in fc['features']:
        p = ft['properties']; g = shape(ft['geometry'])
        if not g.is_valid: g = g.buffer(0)
        feats.append(dict(name=p['name'], sub=p.get('sub'), part=p.get('part'), region=p['regions'][0], geom=g,
                          area=EQ(g).area, group=(p.get('sub') or p.get('part') or p['name']).strip()))
    modern = fy(fn) >= 1900; min_km2 = 10e3 if modern else 1.5e6
    g_area, g_home = {}, {}
    for ft in feats:
        g_area[ft['group']] = g_area.get(ft['group'], 0) + ft['area']
        if ft['group'] not in g_home or ft['area'] > g_home[ft['group']][1]: g_home[ft['group']] = (ft['region'], ft['area'])
    by_region = {}
    for g in g_area:
        if not NOT_STATE.search(g): by_region.setdefault(g_home[g][0], []).append(g)
    top = {g for gs in by_region.values() for g in sorted(gs, key=lambda g: -g_area[g])[:2 if modern else 3]}
    for ft in feats:
        ft['major'] = bool(FAMOUS.search(ft['group']) or FAMOUS.search(ft['name']) or
                           (not NOT_STATE.search(ft['group']) and (g_area[ft['group']] >= min_km2 or ft['group'] in top)))
    return feats


# ---------- timelines ----------
SUFFIX_RE = re.compile(r'^(.*?)\s*\(([^()]+)\)\s*$')
_memo = {}


def iso_of(name):
    if name in FL.ISO:
        v = FL.ISO[name]
        return v
    try:
        import pycountry
        c = pycountry.countries.lookup(name)
        code = c.alpha_2.lower()
        if code in FL.SINCE: return (code, FL.SINCE[code])
    except (LookupError, ImportError):
        pass
    return None


def timeline(name, depth=0):
    """[(from, to, flag id)] for a name, with references to other states' timelines expanded"""
    if name in _memo: return _memo[name]
    if depth > 8: raise ValueError('reference loop at ' + name)
    raw = FL.TL.get(name)
    if isinstance(raw, str): raw = [(None, None, raw)]
    if raw is None:
        iso = iso_of(name)
        if iso: raw = [(iso[1], None, 'iso:' + iso[0])]
    if raw is None:
        m = SUFFIX_RE.match(name)
        if m and m.group(2) in FL.SUFFIX: raw = [(None, None, '=' + FL.SUFFIX[m.group(2)])]
        elif name.startswith('Rome ('): raw = [(None, None, '=Rome')]
    out = []
    for y0, y1, ref in raw or []:
        if ref and ref.startswith('='):
            for a, b, r in timeline(ref[1:], depth + 1):
                lo = max(a if a is not None else -1e9, y0 if y0 is not None else -1e9)
                hi = min(b if b is not None else 1e9, y1 if y1 is not None else 1e9)
                if lo <= hi: out.append((None if lo == -1e9 else int(lo), None if hi == 1e9 else int(hi), r))
        elif ref:
            out.append((y0, y1, ref))
    _memo[name] = out
    return out


def flag_at(tl, y):
    for a, b, r in tl:
        if (a is None or y >= a) and (b is None or y <= b): return r
    return None


# ---------- pictures ----------
def svg_of(fid, fi_dir):
    if fid.startswith('iso:'):
        return open(os.path.join(fi_dir, fid[4:] + '.svg'), encoding='utf-8').read()
    return FL.DEFS[fid]['svg']


def render(ids, fi_dir, size, cols, out_png):
    w, h = size; rows = math.ceil(len(ids) / cols)
    cells = ''.join('<img src="data:image/svg+xml;base64,%s" style="left:%dpx;top:%dpx">' % (
        base64.b64encode(svg_of(fid, fi_dir).encode()).decode(), (i % cols) * w, (i // cols) * h) for i, fid in enumerate(ids))
    page = ('<!doctype html><html><head><style>html,body{margin:0;background:transparent}img{position:absolute;width:%dpx;height:%dpx}'
            '</style></head><body>%s</body></html>') % (w, h, cells)
    with tempfile.TemporaryDirectory() as td:
        hp = os.path.join(td, 'flags.html'); open(hp, 'w').write(page)
        js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
              "const p=await b.newPage({viewport:{width:%d,height:%d},deviceScaleFactor:1});"
              "await p.goto('file://%s');await p.waitForTimeout(400);"
              "await p.screenshot({path:'%s',omitBackground:true,clip:{x:0,y:0,width:%d,height:%d}});await b.close();})();") % (
            cols * w, rows * h, hp, out_png, cols * w, rows * h)
        subprocess.run(['node', '-e', js], check=True)


# ---------- tints ----------
HUES = [8, 24, 40, 62, 95, 140, 168, 192, 212, 236, 262, 292, 322, 345]


def hash_hue(name):
    h = 0
    for ch in name: h = (h * 31 + ord(ch)) & 0xffffffff
    return HUES[h % len(HUES)]


def palette_from(img):
    """the flag's colours, most area first, as hues in degrees (white, black and greys left out)"""
    a = np.asarray(img.convert('RGBA')).reshape(-1, 4).astype(float) / 255
    a = a[a[:, 3] > .5]
    hsv = np.array([colorsys.rgb_to_hsv(*px[:3]) for px in a])
    chroma = (hsv[:, 1] > .28) & (hsv[:, 2] > .25)
    if chroma.sum() < len(a) * .04: return []
    hh = hsv[chroma, 0] * 360
    bins = np.bincount((hh // 10).astype(int) % 36, minlength=36).astype(float)
    out, used = [], np.zeros(36, bool)
    while True:
        i = int(np.argmax(np.where(used, -1, bins)))
        if bins[i] <= 0 or used[i] or bins[i] < len(a) * .05: break
        idx = [(i + d) % 36 for d in (-1, 0, 1)]
        sel = np.isin((hh // 10).astype(int) % 36, idx)
        ang = np.radians(hh[sel]); mean = math.degrees(math.atan2(np.sin(ang).mean(), np.cos(ang).mean())) % 360
        out.append(round(mean))
        for j in [(i + d) % 36 for d in (-2, -1, 0, 1, 2)]: used[j] = True
    return out


def hue_dist(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def colour_file(fn, feats, mode, flag_hues, prev, timelines):
    """one border file's tints. Each state would like its flag's main colour, then its other flag colours, then a
    near shade of them, and last any colour; neighbours must stay 30 degrees of hue apart. A greedy pass (biggest
    first) is followed by trades that lower the total cost, where big states count more and a state whose flag has
    not changed pays a little to leave last file's tint, so colours hold steady from one map to the next."""
    keyf = (lambda ft: ft['group']) if mode == 'g' else (lambda ft: ft['name'])
    nodes = {}
    for ft in feats:
        if mode == 'g' and not ft['major']: continue
        k = keyf(ft)
        n = nodes.setdefault(k, dict(geoms=[], area=0))
        n['geoms'].append(ft['geom']); n['area'] += ft['area']
    keys = list(nodes)
    geoms, owner = [], []
    for k in keys:
        for g in nodes[k]['geoms']: geoms.append(g); owner.append(k)
    tree = STRtree(geoms)
    adj = {k: set() for k in keys}
    for i, g in enumerate(geoms):
        for j in tree.query(g.buffer(.3)):
            j = int(j)
            if owner[j] != owner[i] and g.distance(geoms[j]) < .3:
                adj[owner[i]].add(owner[j]); adj[owner[j]].add(owner[i])
    y0, y1 = SPAN[fn]
    flags_now, rank, weight = {}, {}, {}
    for k in keys:
        tl = timelines.get(k) or []
        # the flag shown for most of this file's years
        counts = {}
        for y in range(y0, y1 + 1, max(1, (y1 - y0) // 20 or 1)):
            fid = flag_at(tl, y); counts[fid] = counts.get(fid, 0) + 1
        fid = max(counts, key=counts.get) if counts else None
        flags_now[k] = fid
        tint = FL.TINT.get(k)
        own = ([tint] if tint is not None else []) + (flag_hues.get(fid, []) if fid else [])
        r = {}
        for i, h in enumerate(own): r.setdefault(h % 360, float(i))
        for h in own[:2]:
            for d in (36, -36, 52, -52): r.setdefault((h + d) % 360, 2.5)
        base = hash_hue(k)
        for h in HUES[HUES.index(base):] + HUES[:HUES.index(base)]: r.setdefault(h, 4.0)
        rank[k] = r
        weight[k] = math.sqrt(nodes[k]['area'] / 1e4) + .5

    def cost(k, h):
        c = rank[k].get(h, 4.0)
        p = prev.get(k)
        if p and p[1] == flags_now[k] and h != p[0]: c += 1.5
        return c * weight[k]

    out = {}
    def ok(k, h, skip=()):
        return all(hue_dist(h, out[n]) >= 30 for n in adj[k] if n in out and n not in skip)
    def best(k, skip=(), avoid=None):
        cs = [h for h in rank[k] if ok(k, h, skip) and (avoid is None or hue_dist(h, avoid) >= 30)]
        return min(cs, key=lambda h: cost(k, h)) if cs else None
    order = sorted(keys, key=lambda k: -nodes[k]['area'])
    for k in order:
        p = prev.get(k)
        h = best(k, (), None)
        if p is not None and ok(k, p[0]) and cost(k, p[0]) <= (cost(k, h) if h is not None else 1e9): h = p[0]
        if h is None:  # nothing fits: the colour farthest from the neighbours'
            h = max(rank[k], key=lambda c: min([hue_dist(c, out[n]) for n in adj[k] if n in out] or [360]))
        out[k] = h
    # trades: a state takes a colour it likes better when the neighbours in its way can move to another colour
    for _ in range(6):
        moved = False
        for k in order:
            cur = cost(k, out[k])
            for h in sorted(rank[k], key=lambda h: cost(k, h)):
                if cost(k, h) >= cur: break
                block = [n for n in adj[k] if hue_dist(h, out[n]) < 30]
                if len(block) > 3: continue
                trial, delta, fail = {}, cost(k, h) - cur, False
                for n in block:
                    # each blocked neighbour moves to its best colour clear of the new one and of its other neighbours
                    old = out[n]; out[n] = None
                    nh = None
                    cs = [c for c in rank[n] if hue_dist(c, h) >= 30 and
                          all(hue_dist(c, out[m]) >= 30 for m in adj[n] if m != k and out.get(m) is not None) and
                          all(hue_dist(c, t) >= 30 for m, t in trial.items() if m in adj[n])]
                    if cs: nh = min(cs, key=lambda c: cost(n, c))
                    out[n] = old
                    if nh is None: fail = True; break
                    trial[n] = nh; delta += cost(n, nh) - cost(n, old)
                if fail or delta >= -1e-9: continue
                out[k] = h
                for n, nh in trial.items(): out[n] = nh
                moved = True
                break
        if not moved: break
    for k, h in out.items(): prev[k] = (h, flags_now[k])
    return out


def main():
    fi_dir = flag_icons()
    data = {fn: load_file(fn) for fn in FILES}
    print('border files', len(FILES))
    names = set()
    for feats in data.values():
        for ft in feats: names |= {ft['name'], ft['group']} | ({ft['sub']} if ft['sub'] else set())
    timelines = {n: timeline(n) for n in sorted(names)}
    timelines = {n: t for n, t in timelines.items() if t}
    used = sorted({r for t in timelines.values() for _, _, r in t})
    missing = [r for r in used if not r.startswith('iso:') and r not in FL.DEFS]
    missing += [r for r in used if r.startswith('iso:') and not os.path.exists(os.path.join(fi_dir, r[4:] + '.svg'))]
    if missing: raise SystemExit('unknown flags: %s' % missing)
    unused_rules = [n for n in FL.TL if n not in names and not isinstance(FL.TL[n], str)]
    print('states with flags %d of %d names; %d flags; rules for names not on the map: %s' % (
        len(timelines), len(names), len(used), ', '.join(sorted(unused_rules)) or 'none'))

    os.makedirs(os.path.join(OUT, 'flags'), exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        sp = os.path.join(td, 'sprite.png')
        render(used, fi_dir, CELL, COLS, sp)
        sprite = Image.open(sp).convert('RGBA')
        sprite.save(os.path.join(OUT, 'flags', 'sprite.webp'), quality=88, method=6)
        hues = {}
        for i, fid in enumerate(used):
            x, y = (i % COLS) * CELL[0], (i // COLS) * CELL[1]
            hues[fid] = palette_from(sprite.crop((x + 2, y + 2, x + CELL[0] - 2, y + CELL[1] - 2)))
            tint = FL.DEFS.get(fid, {}).get('tint')
            if tint is not None: hues[fid] = [tint] + [h for h in hues[fid] if hue_dist(h, tint) > 20]
        big = os.path.join(td, 'big.png'); bc = 8
        render(used, fi_dir, BIG, bc, big)
        im = Image.open(big).convert('RGBA')
        for i, fid in enumerate(used):
            x, y = (i % bc) * BIG[0], (i // bc) * BIG[1]
            im.crop((x, y, x + BIG[0], y + BIG[1])).save(os.path.join(OUT, 'flags', fid.replace(':', '-') + '.webp'), quality=86, method=6)

    # tints, file by file in time order so a state keeps its colour while its flag stays the same
    tints = {'g': {}, 'n': {}}
    for mode in 'gn':
        prev = {}
        for i, fn in enumerate(FILES):
            for k, h in colour_file(fn, data[fn], mode, hues, prev, timelines).items():
                seq = tints[mode].setdefault(k, [])
                if not seq or seq[-1][1] != h: seq.append([i, h])
    for mode in 'gn':
        # a state whose tint never leaves the page's own fallback (hash_hue) needs no entry
        tints[mode] = {k: (v[0][1] if len(v) == 1 else v) for k, v in tints[mode].items() if not (len(v) == 1 and v[0][1] == hash_hue(k))}

    try:
        import pycountry
    except ImportError:
        pycountry = None
    meta = {}
    for i, fid in enumerate(used):
        if fid.startswith('iso:'):
            t, note = FL.ISO_TITLES.get(fid[4:], (None, ''))
            if not t:
                c = pycountry and pycountry.countries.get(alpha_2=fid[4:].upper())
                t = 'Flag of ' + (getattr(c, 'common_name', None) or c.name if c else fid[4:].upper())
            meta[fid] = [i, t, 'flag', note]
        else:
            d = FL.DEFS[fid]; meta[fid] = [i, d['title'], d['kind'], d['note']]
    # the years each state with flags is on the map, so the page only offers to jump to a year it can show
    seen = {}
    for fn in FILES:
        a, b = SPAN[fn]
        for ft in data[fn]:
            n = ft['name']
            if n in timelines: s = seen.get(n); seen[n] = [min(s[0], a), max(s[1], b)] if s else [a, b]
    out = dict(sprite=dict(src='flags/sprite.webp', w=CELL[0], h=CELL[1], cols=COLS, n=len(used)),
               files=FILES, flags=meta, names={n: [[a, b, r] for a, b, r in t] for n, t in sorted(timelines.items())},
               seen=dict(sorted(seen.items())), tints=tints)
    with open(os.path.join(OUT, 'flags.json'), 'w', encoding='utf-8') as fo:
        json.dump(out, fo, ensure_ascii=False, separators=(',', ':'))
    print('flags.json %d KB, sprite %d KB' % (os.path.getsize(os.path.join(OUT, 'flags.json')) // 1024,
                                             os.path.getsize(os.path.join(OUT, 'flags', 'sprite.webp')) // 1024))


if __name__ == '__main__':
    main()

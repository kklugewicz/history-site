"""Works out which states each person with a story belongs to, year by year, for the "Stories from <state>" row that
opens when a state is clicked. Writes data/story_states.json.

Run from the repository root, after content/people/build_people.py:  python3 content/stories/build_states.py
A person belongs to a state in a year when, in the border snapshot the map shows for that year:
  - they rule it: a "rule" stint, under the first of its names that is on the map (as the page ties a ruler to a label).
    In a year whose borders lack all of its names, the page draws them at their seat, inside some other state (Sejong's
    Korea in the 1400 snapshot); they still belong to the state they rule, under its first name, not to that one;
  - or they are in it: where the map puts them in the middle of the year, and every waypoint of a journey that falls
    in that year (the places they actually stopped). A point just offshore takes the state beside it, as cities do.
A journey across a state none of its waypoints is in is only in passing: it counts for the year it happens, so a face
seen crossing a state is in its row then, but not as one of the state's people in other years.
Where a snapshot is plainly wrong for the years it is shown (FIXES, below), a point takes the state that really held it.
A place someone lived in also gets the state it is in on today's map (the last snapshot), so the page can give it to
the country whose land it is when the state then was at home elsewhere (Leonardo's Florence inside the Holy Roman
Empire is Italy's; Marie Curie's Warsaw inside the Russian Empire is Poland's).
Output: {"ties": {person id: [[state name, from, to, kind], ...]}}, a run per state and kind, oldest first, where kind
is "r" (ruled it), "h" (lived or stopped there) or "p" (there in passing). A lived-in run whose place has another name
today adds that name and the place: [state, from, to, "h", state there today, lon, lat]. Years skip 0, as the
timeline does (1 BC is followed by AD 1).
"""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data')
sys.path.insert(0, HERE)
from chosen import CHOSEN

people = {p['id']: p for p in json.load(open(os.path.join(DATA, 'people.json')))['people']}
tl = json.load(open(os.path.join(DATA, 'timeline.json')))
FILES = tl['borderFiles']
Y0, Y1 = tl['snapshots'][0]['span'][0], tl['snapshots'][-1]['span'][1]
fy = lambda f: -int(f[2:]) if f.startswith('bc') else int(f)


def file_for(y):  # the latest snapshot at or before the year, as the page picks it
    best = FILES[0]
    for f in FILES:
        if fy(f) <= y: best = f
    return best


# Places a snapshot gives to the wrong state for the years it is shown: (box, the state the map says or None where it
# draws none, the right one or None for no state). The right one need not be drawn in that snapshot: it only names the
# place for the rows.
GENEVA, ROYAL_PRUSSIA, HAITI = (5.9, 46.12, 6.35, 46.35), (18.5, 53.6, 20.8, 54.45), (-74.5, 17.9, -71.7, 20.1)
CAUCASUS = [((40.0, 39.8, 47.0, 43.6), 'Persia', 'Russian Empire'), ((47.0, 39.3, 50.5, 42.0), 'Persia', 'Russian Empire')]
FIXES = {
    # Sinai and the Gulf of Suez, Egypt's in the time of Moses, not the Levant's "state societies"
    'bc1500': [((32.2, 27.5, 35.0, 31.3), 'state societies and Aramaean kingdoms', 'Egypt')],
    # the Punjab, where Alexander's army turned back at the Beas, is not Tibet
    'bc400': [((73.5, 30.5, 76.5, 32.8), 'Proto-Tibetan cultures', 'Hindu kingdoms')],
    # Mecca and Medina were never Himyar's (Muhammad's youth)
    '500': [((37.0, 19.0, 42.0, 26.5), 'Himyarite Kingdom', 'Hejaz')],
    # Khwarazm (Avicenna at Gurganj) was no Pecheneg land
    '1000': [((57.5, 40.5, 62.5, 43.8), 'Peshemegs', None)],
    # Royal Prussia and Warmia were the Polish crown's from 1466 (Copernicus at Frombork)
    '1500': [(ROYAL_PRUSSIA, 'Teutonic Knights', 'Poland-Lithuania')],
    '1530': [(ROYAL_PRUSSIA, 'Prussia', 'Poland-Lithuania'), (GENEVA, 'Savoy', 'Geneva')],   # Calvin's Geneva
    # St Petersburg and Ingria were Russia's from 1703 (Euler and the Academy, Catherine the Great's court); Ferney,
    # Voltaire's home beside Geneva, was French
    '1715': [((27.8, 59.0, 31.6, 60.8), 'Sweden', 'Tsardom of Muscovy'), ((5.9, 46.22, 6.2, 46.35), 'Sardinia-Piedmont', 'France')],
    # Belgium (Marx in Brussels, Waterloo) was never the Austrian Empire's, and Strasbourg was French (Pasteur)
    '1815': [((2.5, 49.4, 6.5, 51.55), 'Austrian Empire', 'Belgium'), ((7.6, 48.4, 7.85, 48.7), 'Baden', 'France')],
    # Gallipoli was Ottoman (Mustafa Kemal's battle)
    '1914': [((25.8, 39.9, 27.0, 40.7), 'Bulgaria', 'Ottoman Empire')],
    # the zone the 1920 treaties offered Italy in Anatolia, drawn as Italy's until 1929, was won back by Turkey in 1922
    '1920': [((28.5, 36.5, 33.5, 40.0), 'Italy', 'Ottoman Sultanate')],
    # Syracuse, Archimedes' city, a Greek city-state the map leaves out
    'bc300': [((14.8, 36.6, 15.6, 37.4), None, 'Greek city-states')],
    # Roman Britain (Boudica's revolt), which the map for AD 1 has not drawn
    'bc1': [((-6.0, 50.0, 2.0, 55.0), None, 'Roman Empire')],
    # Iceland, settled from 874, with its own Althing from 930 (Leif Erikson's birthplace)
    '900': [((-25.0, 63.0, -13.0, 67.0), None, 'Icelandic Commonwealth')],
    # Saint-Domingue, Toussaint Louverture's Haiti, drawn as no state until 1815
    '1783': [(HAITI, None, 'Haiti')], '1800': [(HAITI, None, 'Haiti')],
    # Georgia and the rest of the Caucasus north of the Aras were Russia's from the 1800s, not Persia's (Stalin's Gori)
    '1878': CAUCASUS, '1880': CAUCASUS, '1900': CAUCASUS,
}


class Borders:
    """One snapshot: each state's polygons with their boxes, for point lookups."""
    def __init__(self, f):
        self.fixes = FIXES.get(f, [])
        self.feats = []
        for ft in json.load(open(os.path.join(DATA, f'borders_{f}.json')))['features']:
            polys = []
            for poly in ft['geometry']['coordinates']:
                xs = [q[0] for q in poly[0]]; ys = [q[1] for q in poly[0]]
                polys.append((min(xs), min(ys), max(xs), max(ys), poly))
            self.feats.append((ft['properties']['name'], polys))
        self.names = {n for n, _ in self.feats}

    @staticmethod
    def _in_ring(x, y, r):
        c = False
        j = len(r) - 1
        for i in range(len(r)):
            xi, yi = r[i][0], r[i][1]; xj, yj = r[j][0], r[j][1]
            if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi: c = not c
            j = i
        return c

    def _at(self, x, y):
        for name, polys in self.feats:
            for x0, y0, x1, y1, poly in polys:
                if x0 <= x <= x1 and y0 <= y <= y1:
                    inside = False
                    for r in poly:
                        if self._in_ring(x, y, r): inside = not inside
                    if inside: return name
        return None

    def state_at(self, lon, lat):
        # the same small steps the page takes for a port that the simplified borders leave just offshore
        for a, b in ((0, 0), (.2, 0), (-.2, 0), (0, .2), (0, -.2), (.4, .4), (-.4, -.4), (.4, -.4), (-.4, .4)):
            n = self._at(lon + a, lat + b)
            if n:
                for (x0, y0, x1, y1), was, right in self.fixes:
                    if n == was and x0 <= lon <= x1 and y0 <= lat <= y1: return right
                return n
        for (x0, y0, x1, y1), was, right in self.fixes:
            if was is None and x0 <= lon <= x1 and y0 <= lat <= y1: return right
        return None


_borders = {}
def borders(y):
    f = file_for(y)
    if f not in _borders: _borders[f] = Borders(f)
    return _borders[f]


def prep(s):
    """The page's prepStint: route points (longitudes unwrapped) and the fraction of the stint at each waypoint."""
    src = s.get('path') or [s['at']]
    pts = [[q[0], q[1]] for q in src]
    for i in range(1, len(pts)):
        while pts[i][0] - pts[i - 1][0] > 180: pts[i][0] -= 360
        while pts[i][0] - pts[i - 1][0] < -180: pts[i][0] += 360
    cum = [0.0]
    for i in range(1, len(pts)):
        la = (pts[i][1] + pts[i - 1][1]) / 2 * math.pi / 180
        cum.append(cum[-1] + math.hypot((pts[i][0] - pts[i - 1][0]) * math.cos(la), pts[i][1] - pts[i - 1][1]))
    span = s['to'] - s['from'] + 1
    t = [(q[2] - s['from']) / span if len(q) > 2 else None for q in src]
    if t[0] is None: t[0] = 0
    if t[-1] is None: t[-1] = 1 if len(pts) > 1 else 0
    for i in range(1, len(t)):
        if t[i] is None:
            j = i
            while t[j] is None: j += 1
            a, b, c0, c1 = t[i - 1], t[j], cum[i - 1], cum[j]
            for m in range(i, j):
                t[m] = a + (b - a) * ((cum[m] - c0) / (c1 - c0) if c1 > c0 else (m - i + 1) / (j - i + 1))
    return pts, t


def where(pts, t, s, yf):
    """The page's whereAt: the point on the route at fractional year yf."""
    if len(pts) == 1: return pts[0]
    f = min(1, max(0, (yf - s['from']) / (s['to'] - s['from'] + 1)))
    i = 0
    while i < len(t) - 2 and t[i + 1] <= f: i += 1
    u = min(1, max(0, (f - t[i]) / (t[i + 1] - t[i]))) if t[i + 1] > t[i] else 1
    x = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u
    return [((x + 540) % 360) - 180, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u]


def years(a, b):
    return [y for y in range(max(a, Y0), min(b, Y1) + 1) if y != 0]


def nxt(y): return 1 if y == -1 else y + 1


TODAY = Borders(FILES[-1])   # today's map, for the state a place is in now
STRONG = {'p': 0, 'h': 1, 'r': 2}   # ruling a state beats living there, which beats passing through
out, stats = {}, {'r': 0, 'h': 0, 'p': 0, 'now': 0}
for pid in CHOSEN:
    p = people[pid]
    seen, at = {}, {}   # (state, year, state there today or None) -> kind, and a point for each lived-in key
    def tie(name, y, k, pt=None, now=None):
        if not name: return
        key = (name, y, now if k == 'h' and now != name else None)
        if STRONG[k] > STRONG.get(seen.get(key), -1): seen[key] = k
        if key[2] and key not in at: at[key] = pt
    for s in p['stints']:
        if s.get('rule'):
            for y in years(s['from'], s['to']):
                b = borders(y)
                tie(next((n for n in s['rule'] if n in b.names), s['rule'][0]), y, 'r')
            continue
        pts, t = prep(s)
        span, stops, today = s['to'] - s['from'] + 1, set(), set()
        if len(pts) > 1:   # the stops on a journey, each in the year the route reaches it
            for (lon, lat), ti in zip(pts, t):
                y = min(s['to'], max(s['from'], math.floor(s['from'] + ti * span)))
                y = 1 if y == 0 else y
                if Y0 <= y <= Y1:
                    q = (((lon + 540) % 360) - 180, lat)
                    n, m = borders(y).state_at(*q), TODAY.state_at(*q)
                    if n: tie(n, y, 'h', q, m); stops.add(n); today.add(m)
        for y in years(s['from'], s['to']):
            q = where(pts, t, s, y + .5)
            n, m = borders(y).state_at(*q), TODAY.state_at(*q)
            # between the stops of a journey a place's name today only counts if the journey stopped in that land
            tie(n, y, 'h' if len(pts) == 1 or n in stops else 'p', q, m if len(pts) == 1 or m in today else None)
    lived = {(n, y) for (n, y, _), k in seen.items() if k != 'p'}
    for key in [key for key, k in seen.items() if k == 'p' and (key[0], key[1]) in lived]: del seen[key]
    runs = []
    for (name, y, now), k in sorted(seen.items(), key=lambda e: (e[0][0], e[0][2] or '', e[1], e[0][1])):
        last = runs[-1] if runs else None
        if last and last[0] == name and last[3] == k and last[4] == now and nxt(last[2]) == y: last[2] = y
        else: runs.append([name, y, y, k, now, at.get((name, y, now))])
    runs.sort(key=lambda r: (r[1], r[2], r[0]))
    out[pid] = [r[:4] + ([r[4], round(r[5][0], 1), round(r[5][1], 1)] if r[4] else []) for r in runs]
    for r in runs: stats[r[3]] += 1; stats['now'] += bool(r[4])

json.dump({'ties': out}, open(os.path.join(DATA, 'story_states.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
states = {r[0] for runs in out.values() for r in runs}
none = [pid for pid, runs in out.items() if not runs]
print(f'{len(out)} people, {stats["r"]} runs ruling a state, {stats["h"]} living or stopping in one ({stats["now"]} in a land named otherwise today) '
      f'and {stats["p"]} there in passing, across {len(states)} states; {os.path.getsize(os.path.join(DATA, "story_states.json")) // 1024} KB')
if none: print('on no state:', ' '.join(none))

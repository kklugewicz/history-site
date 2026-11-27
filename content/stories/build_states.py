"""Works out which states each person with a story belongs to, year by year, for the "Stories from <state>" row that
opens when a state is clicked. Writes data/story_states.json.

Run from the repository root, after content/people/build_people.py:  python3 content/stories/build_states.py
A person belongs to a state in a year when, in the border snapshot the map shows for that year:
  - they rule it: a "rule" stint, under the first of its names that is on the map (as the page ties a ruler to a label);
  - or they are in it: where the map puts them in the middle of the year, and every waypoint of a journey that falls
    in that year (the places they actually stopped). A point just offshore takes the state beside it, as cities do.
Some of that is only in passing: a journey across a state none of its waypoints is in, or a ruler drawn at their seat
inside another state because that year's borders don't have their own (Sejong's Korea in the 1400 snapshot). It counts
for the year it happens, so a face seen inside a state is in its row, but not as one of the state's people in other years.
Output: {"ties": {person id: [[state name, from, to, kind], ...]}}, a run per state and kind, oldest first, where kind
is "r" (ruled it), "h" (lived or stopped there) or "p" (there in passing). Years skip 0, as the timeline does (1 BC is
followed by AD 1).
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


class Borders:
    """One snapshot: each state's polygons with their boxes, for point lookups."""
    def __init__(self, f):
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
            if n: return n
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


STRONG = {'p': 0, 'h': 1, 'r': 2}   # ruling a state beats living there, which beats passing through
out, stats = {}, {'r': 0, 'h': 0, 'p': 0}
for pid in CHOSEN:
    p = people[pid]
    seen = {}   # (state, year) -> kind
    def tie(name, y, k):
        if name and STRONG[k] > STRONG.get(seen.get((name, y)), -1): seen[(name, y)] = k
    for s in p['stints']:
        if s.get('rule'):
            for y in years(s['from'], s['to']):
                b = borders(y)
                n = next((n for n in s['rule'] if n in b.names), None)
                if n: tie(n, y, 'r')
                elif s.get('at'): tie(b.state_at(*s['at'][:2]), y, 'p')   # drawn at their seat: their state is not on the map
            continue
        pts, t = prep(s)
        span, stops = s['to'] - s['from'] + 1, set()
        if len(pts) > 1:   # the stops on a journey, each in the year the route reaches it
            for (lon, lat), ti in zip(pts, t):
                y = min(s['to'], max(s['from'], math.floor(s['from'] + ti * span)))
                y = 1 if y == 0 else y
                if Y0 <= y <= Y1:
                    n = borders(y).state_at(((lon + 540) % 360) - 180, lat)
                    if n: tie(n, y, 'h'); stops.add(n)
        for y in years(s['from'], s['to']):
            n = borders(y).state_at(*where(pts, t, s, y + .5))
            tie(n, y, 'h' if len(pts) == 1 or n in stops else 'p')
    runs = []
    for (name, y), k in sorted(seen.items(), key=lambda e: (e[0][0], e[1], e[0][1])):
        last = runs[-1] if runs else None
        if last and last[0] == name and last[3] == k and nxt(last[2]) == y: last[2] = y
        else: runs.append([name, y, y, k])
    runs.sort(key=lambda r: (r[1], r[2], r[0]))
    out[pid] = runs
    for r in runs: stats[r[3]] += 1

json.dump({'ties': out}, open(os.path.join(DATA, 'story_states.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
states = {r[0] for runs in out.values() for r in runs}
none = [pid for pid, runs in out.items() if not runs]
print(f'{len(out)} people, {stats["r"]} runs ruling a state, {stats["h"]} living or stopping in one and {stats["p"]} there in passing, across {len(states)} states; '
      f'{os.path.getsize(os.path.join(DATA, "story_states.json")) // 1024} KB')
if none: print('on no state:', ' '.join(none))

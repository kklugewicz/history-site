"""Builds data/leaders.json, the Leaders list, from leaders.py in this folder, and checks it.

Run from the repository root, after build_stories.py:  python3 content/stories/build_leaders.py
Checks: each person is listed once, with known roles and regions; their year is a whole number inside their life; the
lines are short enough for the list. A person who is not on the map or has no story yet is only a warning: the page
leaves them out until their story is there, then shows them with no rebuild. --report lists the people with a story who
are in neither Leaders nor Discovery, to see that nobody who belongs in one was missed.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data')
sys.path.insert(0, HERE)
from leaders import ROLES, REGIONS, LEADERS

people = {p['id']: p for p in json.load(open(os.path.join(DATA, 'people.json')))['people']}
stories = json.load(open(os.path.join(DATA, 'stories', 'index.json')))['ids']
LIMITS = {'as': 38, 'k': 56}
errs, warns, seen = [], [], set()

for e in LEADERS:
    pid, y = e['id'], e['y']
    if pid in seen:
        errs.append(f'{pid}: listed twice')
    seen.add(pid)
    for key, known, what in (('f', ROLES, 'roles'), ('r', REGIONS, 'regions')):
        v = e[key]
        if not v or any(x not in known for x in v) or len(set(v)) != len(v):
            errs.append(f'{pid}: {what} {" ".join(v)}; known ones are {" ".join(known)}')
    if not isinstance(y, int) or y == 0 or not -3000 <= y <= 2030:
        errs.append(f'{pid}: year {y!r}')
    for k, n in LIMITS.items():
        s = e[k]
        if not s or len(s) > n:
            errs.append(f'{pid}: "{k}" is {len(s)} characters, at most {n}: {s}')
        elif s != s.strip() or s.endswith('.'):
            errs.append(f'{pid}: "{k}" has a stray space or full stop: {s!r}')
    p = people.get(pid)
    if not p:
        warns.append(f'{pid}: not in data/people.json yet; left out of the list until they are there with a story')
        continue
    if pid not in stories:
        warns.append(f'{pid}: has no story yet; left out of the list until it has one')
    b, d = (p.get('life') or [None, None])[:2]
    if isinstance(y, int) and ((b is not None and y <= b) or (d is not None and y > d)):
        errs.append(f'{pid}: year {y} is outside their life ({b} to {d})')

for e in errs:
    print('ERROR', e)
for w in warns:
    print('warn ', w)
if errs:
    sys.exit(f'{len(errs)} errors')

if '--report' in sys.argv:
    from discovery import DISCOVERY
    listed = seen | {e['id'] for e in DISCOVERY}
    rest = [i for i in stories if i not in listed and not i.startswith('ev:')]
    print(f'{len(rest)} people with a story in neither Leaders nor Discovery:')
    for i in rest:
        print(f'  {i}: {people.get(i, {}).get("role", "")}')

out = sorted(LEADERS, key=lambda e: e['y'])
open(os.path.join(DATA, 'leaders.json'), 'w').write(
    json.dumps({'fields': ROLES, 'regions': REGIONS, 'people': out}, ensure_ascii=False, separators=(',', ':')))
shown = sum(e['id'] in stories and e['id'] in people for e in out)
print(f'{len(out)} people in Leaders ({shown} with a story now): '
      + ', '.join(f'{sum(f in e["f"] for e in out)} {ROLES[f].lower()}' for f in ROLES) + '; '
      + ', '.join(f'{sum(r in e["r"] for e in out)} in {REGIONS[r]}' for r in REGIONS))

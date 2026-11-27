"""Builds data/discovery.json, the Discovery list, from discovery.py in this folder, and checks it.

Run from the repository root, after build_stories.py:  python3 content/stories/build_discovery.py
Checks: each person is listed once, in known fields; their year is a whole number inside their life (or the year after,
for a book that came out as they died); the lines are short enough for the list. A person who is not on the map or has
no story yet is only a warning: the page leaves them out until their story is there, then shows them with no rebuild.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, 'data')
sys.path.insert(0, HERE)
from discovery import FIELDS, DISCOVERY

people = {p['id']: p for p in json.load(open(os.path.join(DATA, 'people.json')))['people']}
stories = json.load(open(os.path.join(DATA, 'stories', 'index.json')))['ids']
LIMITS = {'as': 34, 'k': 56}
errs, warns, seen = [], [], set()

for e in DISCOVERY:
    pid, y = e['id'], e['y']
    if pid in seen:
        errs.append(f'{pid}: listed twice')
    seen.add(pid)
    if not e['f'] or any(f not in FIELDS for f in e['f']) or len(set(e['f'])) != len(e['f']):
        errs.append(f'{pid}: fields {" ".join(e["f"])}; known ones are {" ".join(FIELDS)}')
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
    if isinstance(y, int) and ((b is not None and y <= b) or (d is not None and y > d + 1)):
        errs.append(f'{pid}: year {y} is outside their life ({b} to {d})')

for e in errs:
    print('ERROR', e)
for w in warns:
    print('warn ', w)
if errs:
    sys.exit(f'{len(errs)} errors')

out = sorted(DISCOVERY, key=lambda e: e['y'])
counts = {f: sum(f in e['f'] for e in out) for f in FIELDS}
open(os.path.join(DATA, 'discovery.json'), 'w').write(
    json.dumps({'fields': FIELDS, 'people': out}, ensure_ascii=False, separators=(',', ':')))
shown = sum(e['id'] in stories and e['id'] in people for e in out)
print(f'{len(out)} people in Discovery ({shown} with a story now): ' + ', '.join(f'{counts[f]} {FIELDS[f].lower()}' for f in FIELDS))

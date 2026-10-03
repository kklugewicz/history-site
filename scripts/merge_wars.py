import json, glob, subprocess, sys
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W = os.path.join(ROOT, 'content', 'wars'); out = []; ids = set()
for f in sorted(glob.glob(W + '/wars_g[0-9][0-9].json')):
    r = subprocess.run(['python3', W + '/validate_wars.py', f], capture_output=True, text=True)
    last = (r.stdout.strip().splitlines() or ['?'])[-1]
    print(f, last)
    for w in json.load(open(f)):
        if w['id'] in ids: print('  dup id', w['id']); continue
        ids.add(w['id']); out.append(w)
out.sort(key=lambda w: (w['start'], w['end']))
json.dump(out, open(os.path.join(ROOT, 'data', 'wars.json'), 'w'), separators=(',', ':'), ensure_ascii=False)
print(len(out), 'wars', sum(len(w['steps']) for w in out), 'steps')

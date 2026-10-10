"""Merge zones_*.json + denominations.json into the site's religions.json (keeping its spread stories).
Usage: python3 merge_religions.py <site religions.json in> <out>"""
import json, glob, sys, os, math, subprocess
H = os.path.dirname(os.path.abspath(__file__))
old = json.load(open(sys.argv[1]))
den = json.load(open(os.path.join(H, 'denominations.json')))
STORY_BY_FAMILY = {'Christianity': 'christianity', 'Islam': 'islam', 'Judaism': 'judaism', 'Buddhism': 'buddhism', 'Hinduism': 'hinduism'}
STORY_BY_ID = {'zoroastrianism': 'zoroastrianism', 'sikhism': 'sikhism'}
stories = {s['id'] for s in old['stories']}
for d in den:
    st = STORY_BY_ID.get(d['id']) or STORY_BY_FAMILY.get(d['family'])
    d['story'] = st if st in stories else None
zones, src = [], {}
for f in sorted(glob.glob(os.path.join(H, 'zones_*.json'))):
    r = subprocess.run(['python3', os.path.join(H, 'validate_zones.py'), f], capture_output=True, text=True)
    print(os.path.basename(f), (r.stdout.strip().splitlines() or ['?'])[-1])
    for z in json.load(open(f)):
        if z['id'] in src: print('  dup id', z['id'], 'in', src[z['id']]); continue
        src[z['id']] = os.path.basename(f); zones.append(z)
for i, a in enumerate(zones):
    for b in zones[i + 1:]:
        if src[a['id']] != src[b['id']] and math.hypot(a['lon'] - b['lon'], a['lat'] - b['lat']) < 1.5:
            print('  close anchors across files:', a['id'], b['id'])
hist = {}
for f in sorted(glob.glob(os.path.join(H, 'hist_*.json'))): hist.update(json.load(open(f)))
for d in den:
    d['history'] = hist.get(d['id'], [])
    if not d['history']: print('  no history for', d['id'])
# rough population weight for unusually thin or dense zones, so a vast empty desert or tundra
# does not outvote the crowded heartland when a big state takes its majority faith
SPARSE = {
    'russia-yakutia': .03, 'russia-chukotka': .02, 'russia-magadan': .03, 'russia-kamchatka': .05,
    'russia-amur': .2, 'russia-sakhalin': .2, 'russia-krasnoyarsk': .2, 'russia-irkutsk': .3,
    'russia-south-siberia': .5, 'russia-west-siberia': .4, 'russia-komi': .2, 'russia-north': .2, 'russia-karelia': .3,
    'ogaden': .1, 'afar': .15, 'somaliland': .5,
    'borkou-tibesti': .05, 'air': .1, 'kidal': .05, 'timbuktu': .3, 'mauritania-adrar': .1, 'fezzan': .05,
    'algeria-sahara': .05, 'western-sahara': .1, 'najd': .3, 'namibia-central': .2,
    'alaska': .1, 'yukon': .05, 'northwest-territories': .03, 'nunavut': .01, 'greenland': .02,
    'brazil-amazon': .1, 'upper-amazon': .2, 'french-guiana': .2,
    'australia-centre': .02, 'australia-west': .2,
    'sapmi': .2, 'manchuria': .5, 'makuria': .3, 'nobadia': .3, 'alodia': .5, 'beja': .3, 'kordofan': .5, 'arsi-bale': .6, 'gambela': .3, 'puntland': .3, 'kenya-northeast': .2,
    # crowded highland and island cores
    'shewa': 3, 'gondar': 2, 'tigray': 2, 'lasta': 2,
    'japan-kansai': 3, 'japan-kanto': 3, 'tohoku': 3, 'nagasaki': 3,
}
# the page only needs when each place changed faith; the per-place notes stay in the zone source files
for k in set(SPARSE) - {z['id'] for z in zones}: print('  weight for unknown zone', k)
zones = [{**z, 'history': [{'from': h['from'], 'faith': h['faith']} for h in z['history']],
          **({'w': SPARSE[z['id']]} if z['id'] in SPARSE else {})} for z in zones]
out = {'denominations': den, 'zones': zones, 'stories': old['stories']}
json.dump(out, open(sys.argv[2], 'w'), separators=(',', ':'), ensure_ascii=False)
print(len(zones), 'zones', sum(len(z['history']) for z in zones), 'entries')

"""Helpers for the stories of the map's most important people (see the README at the repository root).

Each sNN file calls story(...) once per person. A story is read like a phone story: one page at a time, tapped through.

  story(person_id, hook, *pages)     hook: one line under the name on the cover. The cover, with the person's
                                     portrait, name and years, is added in front; the legacy page must come last.
Pages, in reading order (keep them in the order things happened):
  life(title, text)                  a chapter of their life
  win(title, text)                   a major achievement: marked with a medal, and listed on the cover
  made(title, what, effect)          an invention or discovery: what it is, then what it changed
  work(title, text)                  a painting, building, book or other work, shown whole
  song(title, text, page=, hint=)    a piece they wrote: the page plays a free recording found on the Wikipedia article
                                     `page` (one whose file name contains `hint` first). listen= links out instead,
                                     for music still under copyright.
  tale(title, text)                  an anecdote, important or fun (say so when it is only a legend)
  legacy(text, *points)              why they matter; points are 2 to 4 short lines to remember them by
Every page can also take img= (a Wikipedia article whose lead picture is shown, or 'File:Name.jpg' on Commons),
cap= (a caption for the picture), y= (the year it happened), at= (where: a place key from content/people/_lib.py,
or (lon, lat)) and where= (the place's name, when it is not the key spelled out).
"""
import os, importlib.util

# the people's table of places (content/people/_lib.py, loaded under another name: this file is _lib too)
_spec = importlib.util.spec_from_file_location('people_lib', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'people', '_lib.py'))
_people = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_people)
C = _people.C

STORIES = {}
KINDS = ('life', 'win', 'made', 'work', 'song', 'tale', 'legacy')


def story(pid, hook, *pages):
    if pid in STORIES:
        raise SystemExit(f'story {pid} written twice')
    STORIES[pid] = {'hook': hook, 'pages': list(pages)}


def _page(kind, title, text, **kw):
    p = {'k': kind, 't': title, 'x': text}
    for k, v in kw.items():
        if v is not None:
            p[k] = v
    return p


def life(title, text, **kw): return _page('life', title, text, **kw)
def win(title, text, **kw): return _page('win', title, text, **kw)
def made(title, what, effect, **kw): return _page('made', title, what, fx=effect, **kw)
def work(title, text, **kw): return _page('work', title, text, **kw)
def tale(title, text, **kw): return _page('tale', title, text, **kw)


def song(title, text, page=None, hint=None, listen=None, **kw):
    p = _page('song', title, text, **kw)
    if page: p['au'] = {'page': page, **({'hint': hint} if hint else {})}
    if listen: p['listen'] = listen
    return p


def legacy(text, *points, **kw):
    return _page('legacy', 'Legacy', text, pts=list(points), **kw)


# places the stories need that the people's table does not have
C.update({
    'vinci': (10.93, 43.79), 'amboise': (0.98, 47.41), 'heiligenstadt': (16.35, 48.25), 'eisenach': (10.32, 50.98),
    'deir_el_bahari': (32.61, 25.74), 'valley_of_kings': (32.6, 25.74), 'behistun': (47.44, 34.39), 'mount_nebo': (35.73, 31.77),
    'nippur': (45.23, 32.13), 'wadi_al_jarf': (32.64, 29.03), 'pi_ramesses': (31.83, 30.8), 'mari': (40.89, 34.55),
})

C.update({  # the 1800s
    'guernsey': (-2.54, 49.46), 'shrewsbury': (-2.75, 52.71), 'hodgenville': (-85.74, 37.57), 'new_salem': (-89.84, 40.0),
    'springfield_il': (-89.65, 39.8), 'gads_hill': (0.47, 51.41), 'bayreuth': (11.58, 49.95), 'lucerne': (8.31, 47.05),
    'schonhausen': (12.03, 52.58), 'koniggratz': (15.83, 50.29), 'friedrichsruh': (10.34, 53.53), 'baltimore': (-76.61, 39.29),
    'new_bedford': (-70.93, 41.64), 'rochester_ny': (-77.61, 43.16), 'windsor': (-0.6, 51.48), 'balmoral': (-3.23, 57.04),
    'osborne': (-1.27, 50.75), 'scutari': (29.02, 41.0), 'balaclava': (33.6, 44.5), 'dole': (5.49, 47.09), 'arbois': (5.77, 46.9),
    'lille': (3.06, 50.63), 'strasbourg': (7.75, 48.58), 'brno': (16.61, 49.2), 'heinzendorf': (17.78, 49.66),
    'auburn_ny': (-76.56, 42.93), 'combahee': (-80.65, 32.63), 'yasnaya_polyana': (37.53, 54.07), 'astapovo': (39.45, 53.24),
    'giverny': (1.53, 49.08), 'le_havre': (0.11, 49.49), 'argenteuil': (2.25, 48.95), 'milan_ohio': (-82.6, 41.3),
    'port_huron': (-82.42, 42.98), 'west_orange': (-74.24, 40.79), 'brantford': (-80.26, 43.14), 'baddeck': (-60.75, 46.1),
    'zundert': (4.66, 51.47), 'nuenen': (5.55, 51.47), 'borinage': (3.85, 50.43), 'arles': (4.63, 43.68),
    'saint_remy': (4.83, 43.79), 'auvers': (2.17, 49.07), 'smiljan': (15.31, 44.57), 'graz': (15.44, 47.07),
    'niagara': (-79.07, 43.08), 'colorado_springs': (-104.82, 38.83), 'wardenclyffe': (-72.91, 40.95), 'pribor': (18.15, 49.64),
    'santiniketan': (87.68, 23.68), 'heidelberg': (8.69, 49.4), 'trieste': (13.77, 45.65),
})

C.update({  # the 1900s
    'dearborn': (-83.18, 42.32), 'highland_park_mi': (-83.1, 42.41), 'durban': (31.03, -29.86), 'pietermaritzburg': (30.39, -29.6),
    'shushenskoye': (91.95, 53.32), 'south_pole': (0.0, -89.9), 'framheim': (-164.0, -78.5), 'tromso': (18.96, 69.65),
    'borge': (10.98, 59.27), 'blenheim': (-1.36, 51.84), 'sandhurst': (-0.77, 51.35), 'kureika': (87.2, 66.45), 'ulm': (9.99, 48.4),
    'bern': (7.45, 46.95), 'thessaloniki': (22.94, 40.64), 'malaga': (-4.42, 36.72), 'guernica': (-2.68, 43.32),
    'warm_springs': (-84.68, 32.89), 'predappio': (11.98, 44.1), 'xikou': (121.25, 29.68), 'whampoa': (113.42, 23.09),
    'braunau': (13.04, 48.26), 'linz': (14.29, 48.31), 'kim_lien': (105.58, 18.67), 'pac_bo': (106.05, 22.98),
    'colombey': (4.88, 48.22), 'jinggangshan': (114.17, 26.57), 'khomein': (50.08, 33.64), 'neauphle': (1.9, 48.82),
    'guang_an': (106.63, 30.47), 'shenzhen': (114.06, 22.54), 'berkeley': (-122.27, 37.87), 'skopje': (21.43, 42.0),
    'bletchley_park': (-0.74, 52.0), 'wilmslow': (-2.23, 53.33), 'tuskegee': (-85.69, 32.42), 'brookline': (-71.12, 42.33),
    'pt_109': (157.0, -8.1), 'mvezo': (28.48, -31.93), 'qunu': (28.6, -31.8), 'rivonia': (28.06, -26.05), 'wadowice': (19.49, 49.88),
    'vatican': (12.45, 41.9), 'gdansk': (18.65, 54.35), 'auschwitz': (19.2, 50.03), 'biran': (-75.78, 20.72),
    'santiago_de_cuba': (-75.82, 20.02), 'treetops': (36.9, -0.4), 'birmingham_al': (-86.8, 33.52), 'memphis_tn': (-90.05, 35.15),
    'bergen_belsen': (9.91, 52.76), 'wapakoneta': (-84.19, 40.57), 'edwards': (-117.88, 34.9), 'privolnoye': (42.27, 46.6),
    'stavropol': (41.97, 45.04), 'chernobyl': (30.1, 51.39), 'foros': (33.79, 44.39), 'klushino': (34.75, 55.65),
    'saratov': (46.03, 51.53), 'baikonur': (63.31, 45.92), 'star_city': (38.12, 55.88), 'taktser': (101.88, 36.47),
    'tawang': (91.86, 27.59), 'grozny': (45.69, 43.32), 'crimea': (34.1, 44.95), 'cern': (6.05, 46.23),
    'cambridge_ma': (-71.09, 42.36), 'los_altos': (-122.11, 37.38), 'cupertino': (-122.03, 37.32), 'portland_or': (-122.68, 45.52),
    'abbey_road': (-0.18, 51.53), 'rishikesh': (78.27, 30.09), 'kyiv': (30.52, 50.45), 'mezzegra': (9.21, 46.0),
})

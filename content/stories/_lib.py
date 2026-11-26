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

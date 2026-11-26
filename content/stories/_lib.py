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

"""Helpers for the stories of wars and great events (see the README at the repository root).

Each eNN file calls event(...) once per story. An event's story reads like a person's: a cover with its picture, name,
years and one line, then one page at a time, tapped through or turning by itself, with the legacy page last.

  event(id, name, kind, years, hook, *pages, states=, war=, wiki=, img=, at=, label=)
    kind     what it was: a key of KINDS below. It picks the icon, and the cover's label unless label= is given.
    years    (from, to): integer years, BC negative.
    hook     one line under the name on the cover.
    states   the states it belongs to, each spelled as in the border files of its years (data/borders_<year>.json,
             the file in use for a year being the latest one at or before it). The country view lists the story
             under each of them. A war story gets the states of its war on the map as well.
    war      the id of the war in data/wars.json that this story tells: the story then offers to follow the war on
             the map, and the war's own view offers the story.
    wiki     the Wikipedia article for "Read more". Its lead picture is the cover unless img= names another
             (an article, so the small picture in the story trays can load too).
    at       where it happened (a place key, or (lon, lat) with where=), for "See it on the map".
Pages, in reading order (keep them in the order things happened):
  scene(title, text)            what happened: a chapter of the story. kick= changes its label ('How it began').
  battle(title, text)           a battle or a siege. Listed on the cover.
  turn(title, text)             a turning point. Listed on the cover.
  figure(person, title, text)   someone who was there. person is an id in data/people.json: their portrait is the
                                picture unless img= is given, and the page offers their own story when they have
                                one. None for someone who is not on the map (give img= then).
  cost(title, text, num=, of=)  the human cost: num is the big figure ('17 million'), of= says what it counts.
  made(title, what, effect)     an invention or discovery it brought: what it was, then what it changed.
  work(title, text)             a painting, book, poem or building it left, shown whole.
  song(title, text, page=, hint=, listen=)   music of it, as in the people's stories: page= is a Wikipedia article
                                whose free recording is played (one whose file name has the words of hint= first);
                                listen= links out instead, for music still under copyright.
  tale(title, text)             an anecdote, important or fun (say so when it is only a legend).
  legacy(text, *points)         why it matters: last, once; points are 2 to 4 short lines to remember it by.
Every page can also take img= (a Wikipedia article whose lead picture is shown, or 'File:Name.jpg' on Commons),
cap= (a caption for the picture), y= (the year it happened), at= (a place key, or (lon, lat) with where=) and
where= (the place's name, when it is not the key spelled out).
Write in our own words: short quotes only, and no song lyrics.
"""
import os, importlib.util

# the places of the people's stories (content/stories/_lib.py, which adds its own to content/people/_lib.py)
_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('stories_lib', os.path.join(os.path.dirname(_here), 'stories', '_lib.py'))
_stories = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_stories)
C = _stories.C

# kind: (cover label, icon). The icons are drawn in index.html (EVI).
KINDS = {
    'war': ('War', 'swords'), 'wars': ('Wars', 'swords'), 'world-war': ('World war', 'swords'), 'civil-war': ('Civil war', 'swords'),
    'conquest': ('Conquest', 'swords'), 'invasion': ('Invasion', 'swords'), 'battle': ('Battle', 'swords'), 'siege': ('Siege', 'tower'),
    'revolution': ('Revolution', 'flame'), 'uprising': ('Uprising', 'flame'), 'independence': ('Independence', 'flag'),
    'voyage': ('Voyage', 'ship'), 'expedition': ('Expedition', 'compass'), 'migration': ('Migration', 'compass'),
    'disaster': ('Disaster', 'wave'), 'epidemic': ('Epidemic', 'virus'), 'famine': ('Famine', 'wheat'),
    'genocide': ('Genocide', 'candle'), 'slavery': ('Slavery', 'chain'), 'crisis': ('Crisis', 'bolt'),
    'turning': ('Turning point', 'star'), 'treaty': ('Treaty', 'scroll'), 'law': ('Law', 'scroll'),
    'feat': ('Great feat', 'star'), 'building': ('Great work', 'column'), 'founding': ('Founding', 'column'),
    'games': ('Games', 'star'), 'space': ('Space', 'rocket'), 'change': ('Great change', 'gear'), 'fall': ('Fall', 'column'),
}
PAGE_KINDS = ('scene', 'battle', 'turn', 'figure', 'cost', 'made', 'work', 'song', 'tale', 'legacy')

EVENTS = {}


def event(eid, name, kind, years, hook, *pages, states=(), war=None, wiki=None, img=None, at=None, where=None, label=None):
    if eid in EVENTS:
        raise SystemExit(f'event {eid} written twice')
    EVENTS[eid] = {'id': eid, 'name': name, 'kind': kind, 'years': years, 'hook': hook, 'pages': list(pages),
                   'states': list(states), 'war': war, 'wiki': wiki, 'img': img, 'at': at, 'where': where, 'label': label}


def _page(kind, title, text, **kw):
    p = {'k': kind, 't': title, 'x': text}
    for k, v in kw.items():
        if v is not None:
            p[k] = v
    return p


def scene(title, text, **kw): return _page('scene', title, text, **kw)
def battle(title, text, **kw): return _page('battle', title, text, **kw)
def turn(title, text, **kw): return _page('turn', title, text, **kw)
def tale(title, text, **kw): return _page('tale', title, text, **kw)
def work(title, text, **kw): return _page('work', title, text, **kw)
def made(title, what, effect, **kw): return _page('made', title, what, fx=effect, **kw)
def figure(person, title, text, **kw): return _page('figure', title, text, who=person, **kw)


def cost(title, text, num=None, of=None, **kw):
    return _page('cost', title, text, num=num, of=of, **kw)


def song(title, text, page=None, hint=None, listen=None, **kw):
    p = _page('song', title, text, **kw)
    if page: p['au'] = {'page': page, **({'hint': hint} if hint else {})}
    if listen: p['listen'] = listen
    return p


def legacy(text, *points, **kw):
    return _page('legacy', 'Legacy', text, pts=list(points), **kw)


# places the event stories need that the people's and the stories' tables do not have
C.update({
    'guanahani': (-74.48, 24.05), 'la_navidad': (-72.1, 19.75), 'santa_fe_gr': (-3.72, 37.19), 'canary_gomera': (-17.2, 28.1),
})

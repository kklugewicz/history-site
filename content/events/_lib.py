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
    'invention': ('Invention', 'scroll'), 'legend': ('Legend', 'star'), 'trade': ('Trade', 'compass'),
    'unification': ('Unification', 'flag'),
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
    'pompeii': (14.49, 40.75), 'herculaneum': (14.35, 40.81), 'misenum': (14.08, 40.78), 'vesuvius': (14.43, 40.82),
    'yarmouk': (35.95, 32.8), 'qadisiyyah': (44.43, 31.79), 'camulodunum': (0.9, 51.89), 'mona': (-4.35, 53.25),
    'milvian_bridge': (12.47, 41.94), 'catalaunian_plains': (4.37, 48.95), 'ferghana': (71.78, 40.39),
    'pelusium': (32.57, 31.04), 'mons_graupius': (-2.6, 57.3),
    'stamford_bridge': (-0.91, 53.99), 'pevensey': (0.33, 50.82), 'caffa': (35.38, 45.03), 'messina': (15.55, 38.19),
    'castillon': (-0.04, 44.85), 'tlatelolco': (-99.14, 19.45), 'runnymede': (-0.56, 51.44), 'dan_no_ura': (130.96, 33.96),
    'ichi_no_tani': (135.1, 34.65), 'onon': (108.9, 48.8), 'las_navas': (-3.58, 38.29), 'valencia': (-0.38, 39.47),
    'rapa_nui': (-109.35, -27.12), 'mawei': (108.2, 34.3), 'sarnath': (83.02, 25.38),
    'bosworth': (-1.41, 52.59), 'leicester': (-1.14, 52.63), 'towton': (-1.27, 53.84), 'diu': (70.99, 20.71),
    'sanlucar': (-6.35, 36.78), 'tilbury': (0.37, 51.46), 'isker': (68.4, 58.1), 'panipat': (76.97, 29.39),
    'nagashino': (137.56, 34.92), 'tanegashima': (130.98, 30.6), 'mohacs': (18.68, 45.99), 'chaldiran': (44.0, 39.05),
    'kosovo_polje': (21.08, 42.7), 'ankara': (32.86, 39.93), 'bursa': (29.06, 40.19), 'gallipoli': (26.67, 40.41),
    'myeongnyang': (126.31, 34.57), 'noryang': (127.87, 34.94),
    'magdeburg': (11.63, 52.13), 'white_mountain': (14.32, 50.08), 'munster': (7.63, 51.96), 'naseby': (-0.99, 52.4),
    'shanhai_pass': (119.75, 40.0), 'bender': (29.48, 46.83), 'cromford': (-1.56, 53.11), 'coalbrookdale': (-2.49, 52.64),
    'varennes': (5.03, 49.23), 'jumonville_glen': (-79.65, 39.88), 'karlowitz': (19.94, 45.2), 'burhanpur': (76.23, 21.31),
    'worcester': (-2.22, 52.19), 'yangzhou': (119.41, 32.39), 'nystad': (21.41, 60.8),
    'berezina': (28.35, 54.32), 'balaklava': (33.6, 44.5), 'marsala': (12.44, 37.8), 'teano': (14.07, 41.25),
    'navarino': (21.67, 36.92), 'missolonghi': (21.42, 38.37), 'skibbereen': (-9.27, 51.55), 'humen': (113.67, 22.82),
    'fort_sumter': (-79.87, 32.75), 'chios': (26.14, 38.37), 'barrackpore': (88.38, 22.76), 'guayaquil': (-79.89, -2.19),
    'ipiranga': (-46.61, -23.59), 'solferino': (10.57, 45.37), 'combahee': (-80.65, 32.6), 'chapultepec': (-99.18, 19.42),
    'orasac': (20.58, 44.33), 'tripolitsa': (22.37, 37.51), 'nafplio': (22.8, 37.57), 'moraviantown': (-81.89, 42.58),
    'new_echota': (-84.91, 34.54), 'tahlequah': (-94.97, 35.91), 'alamo': (-98.49, 29.43), 'coloma': (-120.89, 38.8),
    'sinop': (35.15, 42.03), 'gwalior': (78.18, 26.22), 'jintian': (110.1, 23.5), 'cerro_gordo': (-96.7, 19.45),
    'cerro_cora': (-56.03, -22.63), 'dybbol': (9.74, 54.91), 'bad_ems': (7.71, 50.33), 'ismailia': (32.27, 30.6),
    'krakatoa': (105.42, -6.1), 'mafeking': (25.64, -25.85), 'vereeniging': (27.93, -26.67), 'tsushima': (129.8, 34.4),
    'portsmouth_nh': (-70.76, 43.07), 'culebra_cut': (-79.65, 9.05), 'belfast': (-5.93, 54.6),
    'southampton': (-1.4, 50.9), 'titanic_wreck': (-49.95, 41.73), 'columbus_nm': (-107.64, 31.83),
    'ladysmith': (29.78, -28.56),
    'deir_ez_zor': (40.14, 35.33), 'brest_litovsk': (23.69, 52.1), 'camp_funston': (-96.78, 39.07),
    'dunkirk': (2.38, 51.03),
    'panmunjom': (126.68, 37.96), 'golan': (35.75, 33.0), 'xinyang': (114.07, 32.12), 'greensboro': (-79.79, 36.07),
    'panjshir': (69.75, 35.35), 'termez': (67.28, 37.22), 'khorramshahr': (48.18, 30.44), 'halabja': (45.99, 35.18),
    'stanley': (-57.85, -51.69), 'san_carlos': (-59.05, -51.5), 'goose_green': (-58.97, -51.82),
    'pripyat': (30.06, 51.41), 'forsmark': (18.17, 60.4), 'sopron': (16.6, 47.68), 'tallinn': (24.75, 59.44),
    'viskuli': (23.83, 52.57), 'sharpeville': (27.87, -26.69),
    'vukovar': (19.0, 45.35), 'srebrenica': (19.3, 44.1), 'ground_zero': (-74.01, 40.71), 'pentagon': (-77.06, 38.87),
    'shanksville': (-78.9, 40.05), 'abbottabad': (73.21, 34.17), 'tora_bora': (70.22, 34.1), 'doha': (51.53, 25.29),
    'banda_aceh': (95.32, 5.55), 'simeulue': (96.0, 2.6), 'phuket': (98.3, 8.1), 'sidi_bouzid': (9.48, 35.04),
    'daraa': (36.1, 32.62), 'raqqa': (39.01, 35.95), 'ghouta': (36.43, 33.52), 'idlib': (36.63, 35.93),
    'mariupol': (37.55, 47.1), 'bucha': (30.21, 50.54), 'kharkiv': (36.23, 49.99), 'hrabove': (38.65, 48.14),
    'rafah': (34.25, 31.29), 'fordow': (50.99, 34.88), 'coventry': (-1.51, 52.41), 'bergamo': (9.67, 45.7),
    'goma': (29.22, -1.68), 'arusha': (36.68, -3.37),
    'muye': (113.93, 35.3), 'modiin': (35.0, 31.9), 'roncevaux': (-1.32, 43.01), 'verden': (9.23, 52.92),
    'trajans_gate': (23.98, 42.27), 'kleidion': (23.05, 41.38), 'ohrid': (20.8, 41.12), 'konstanz': (9.17, 47.66),
    'domazlice': (12.93, 49.44), 'lipany': (14.98, 50.03), 'cateau_cambresis': (3.54, 50.1), 'wassy': (4.95, 48.5),
    'blois': (1.33, 47.59), 'blindheim': (10.63, 48.63), 'malplaquet': (3.87, 50.34), 'tinta': (-71.4, -14.15),
    'valmy': (4.77, 49.08), 'rivoli': (10.81, 45.57), 'marengo': (8.67, 44.89), 'dandanaqan': (62.3, 37.3),
    'batak': (24.18, 41.94), 'svishtov': (25.35, 43.62), 'pleven': (24.62, 43.42), 'shipka': (25.33, 42.75),
    'san_stefano': (28.82, 40.96), 'rorkes_drift': (30.54, -28.35), 'iquique': (-70.14, -20.21),
    'arica': (-70.31, -18.48), 'antofagasta': (-70.4, -23.65), 'weihaiwei': (122.12, 37.5),
    'shimonoseki': (130.94, 33.96), 'samsun': (36.33, 41.29), 'haiphong': (106.68, 20.86), 'cao_bang': (106.25, 22.67),
    'nyeri': (36.95, -0.42), 'setif': (5.41, 36.19), 'enugu': (7.5, 6.44), 'umuahia': (7.49, 5.53),
    'managua': (-86.25, 12.13), 'san_salvador': (-89.19, 13.69), 'el_mozote': (-88.11, 13.9),
    'guatemala_city': (-90.51, 14.64), 'hodeidah': (42.95, 14.8), 'axum': (38.72, 14.13), 'mekelle': (39.47, 13.5),
    'el_geneina': (22.45, 13.45), 'el_fasher': (25.35, 13.63), 'lausanne': (6.63, 46.52), 'sakarya': (32.15, 39.58),
    'dumlupinar': (30.0, 38.86), 'evian': (6.59, 46.4), 'sabra_shatila': (35.5, 33.86), 'suez_canal': (32.34, 30.45),
    'kumanovo': (21.71, 42.13), 'vlore': (19.49, 40.47),
})

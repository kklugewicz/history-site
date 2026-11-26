"""Build the physical geography layers of the map.

    python3 scripts/build_geo.py <source dir> data

Writes:
  data/water.json  rivers, lakes and canals, each with the years it existed (reservoirs from the year they filled,
                   the Aral Sea and Lake Chad shrinking, the Yellow River's southern course of 1128-1855, the Suez canal...)
  data/geo.json    names of oceans, seas, straits, mountain ranges, deserts and peaks, with a place to put each name,
                   historical names of seas, and the great ocean currents

Sources: Natural Earth 1:10m vectors (public domain), fetched into <source dir>/ne when missing; canals, old river courses,
historical sea names, straits and currents are written out below. Needs shapely and numpy.
Coordinates are stored as integers in hundredths of a degree, each point as the step from the one before."""
import json, math, os, sys, urllib.request
import numpy as np
from shapely.geometry import shape, LineString, Polygon, MultiPolygon, mapping
from shapely.geometry.polygon import orient
from shapely.ops import linemerge, unary_union
from shapely.ops import polylabel

SRC, OUT = sys.argv[1], sys.argv[2]
NE = 'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/'
Q = 100  # hundredths of a degree


def ne(name):
    p = os.path.join(SRC, 'ne', name + '.geojson')
    if not os.path.exists(p):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        print('fetching', name); urllib.request.urlretrieve(NE + name + '.geojson', p)
    return json.load(open(p))['features']


def enc(coords):
    """[[lon, lat], ...] -> [x0, y0, dx1, dy1, ...] in hundredths of a degree, repeated points dropped"""
    out, px, py = [], 0, 0
    for lon, lat in coords:
        x, y = round(lon * Q), round(lat * Q)
        if out and x == px and y == py: continue
        out += [x - px, y - py]; px, py = x, y
    return out


# ---------- the page's projection (d3.geoNaturalEarth1), for angles and lengths on screen ----------
def proj(lon, lat):
    lam, phi = math.radians(lon), math.radians(lat)
    p2 = phi * phi; p4 = p2 * p2
    return (lam * (0.8707 - 0.131979 * p2 + p4 * (-0.013791 + p4 * (0.003971 * p2 - 0.001529 * p4))),
            -phi * (1.007226 + p2 * (0.015085 + p4 * (-0.044475 + 0.028874 * p2 - 0.005916 * p4))))  # y down, like the screen


DEG = proj(1, 0)[0]  # projected width of a degree of longitude at the equator


# ---------- rivers ----------
# Natural lakes that a dam later raised: Natural Earth files them as reservoirs, but they were always there.
NATURAL = {"Lake Zaysan", "Lake Habbaniyah", "Lake Kovdozero", "Lake Imandra", "Koitere", "Rikkavesi", "Lake Il'Men'", "Oulujärvi",
           "Umbozero Lake", "Akkajaure", "Southern Indian Lake", "Cedar Lake", "Lake Abitibi", "Lac Saint-Jean", "Lake Chelan",
           "Ozero Kubenskoye", "Lower Arrow Lake", "Lake Pukaki", "Lake Manapouri", "Lake Te Anau", "Lake Hawea", "Lac Bermen",
           "Lake Tana", "Lake Victoria", "Lake Kyoga", "Lake Ontario", "Lake Taupo", "Vänern", "Vättern", "Mälaren", "Inari",
           "Lake Inari", "Saimaa", "Päijänne", "Lake Segozero", "Vygozero", "Lake Vygozero", "Topozero", "Pyaozero", "Lake Seliger",
           "Ozero Beloye", "Lake Beloye", "Lake Kubenskoye", "Lake Sevan", "Lake Baikal", "Lake Titicaca", "Lago Titicaca",
           "Upper Lough Erne", "Lough Neagh", "Lake Kainji"}
RES_YEAR = {'Buhayrat ath Tharthar': 1956, 'Réservoir de La Grande 2': 1979, 'Serebryanskoe Reservoir': 1970,
            'Repressa de Jupia': 1974, 'Vilyuy Reservoir': 1967, 'Lake Kainji': 1968}
# lakes that came or went: name -> (first year, last year)
LAKE_YEARS = {'Salton Sea': (1905, None), 'South Aral Sea': (1985, None), 'North Aral Sea': (1985, None),
              'Lake Chad': (1975, None), 'Kakhovka Reservoir': (1956, 2022)}
HISTORIC = {'Aral Sea': (None, 1984), 'Lake Chad': (None, 1974), 'Lake Texcoco': (None, 1850), 'Lop Nur': (None, 1971)}
# water the Dutch later drained: the Zuiderzee polders of the Noordoostpolder (1942) and Flevoland (1957-68)
POLDERS = [((None, 1941), [[5.55, 52.62], [5.61, 52.85], [5.79, 52.86], [5.94, 52.76], [5.94, 52.66], [5.85, 52.56], [5.68, 52.56]]),
           ((None, 1956), [[5.13, 52.34], [5.24, 52.47], [5.43, 52.57], [5.6, 52.6], [5.86, 52.56], [5.84, 52.47], [5.63, 52.35],
                           [5.43, 52.27], [5.22, 52.28]])]

# old courses: the Yellow River ran south of Shandong into the Yellow Sea from 1128, when the Song breached its dikes,
# until the great flood of 1855 turned it back north
YELLOW_SOUTH = [[114.82, 35.02], [114.95, 34.85], [115.65, 34.45], [116.35, 34.42], [116.9, 34.3], [117.18, 34.27], [117.75, 34.1],
                [118.3, 33.95], [118.8, 33.75], [119.15, 33.55], [119.6, 33.85], [120.0, 34.1], [120.3, 34.25]]
CANALS = [
    ('Canal of the Pharaohs', -500, 767, [[31.5, 30.58], [31.85, 30.55], [32.05, 30.55], [32.28, 30.57], [32.35, 30.4], [32.45, 30.25], [32.55, 29.97]]),
    ('Grand Canal', 605, None, [[120.17, 30.27], [120.35, 30.75], [120.62, 31.3], [119.97, 31.78], [119.45, 32.2], [119.42, 32.4], [119.45, 32.95], [119.02, 33.6]]),
    ('Grand Canal', 605, 1127, [[119.02, 33.6], [118.5, 33.3], [117.6, 33.6], [116.8, 33.95], [115.6, 34.45], [114.35, 34.79], [113.6, 34.75], [112.45, 34.62]]),
    ('Grand Canal', 608, 1127, [[113.4, 35.05], [113.9, 35.3], [114.4, 35.6], [114.9, 35.95], [115.3, 36.55], [115.7, 36.85], [116.3, 37.45], [116.85, 38.3], [117.2, 39.1], [116.4, 39.9]]),
    ('Grand Canal', 1293, None, [[119.02, 33.6], [118.28, 33.96], [117.18, 34.26], [116.85, 34.75], [116.58, 35.41], [116.25, 35.95], [115.98, 36.45],
                                [115.7, 36.85], [116.3, 37.45], [116.85, 38.3], [117.2, 39.1], [116.9, 39.65], [116.66, 39.9], [116.4, 39.92]]),
    ('Canal du Midi', 1681, None, [[1.44, 43.6], [1.73, 43.42], [1.95, 43.32], [2.35, 43.21], [2.8, 43.24], [3.22, 43.34], [3.5, 43.32], [3.6, 43.4]]),
    ('Caledonian Canal', 1822, None, [[-4.23, 57.48], [-4.45, 57.35], [-4.68, 57.14], [-4.9, 56.98], [-5.1, 56.82]]),
    ('Erie Canal', 1825, None, [[-73.75, 42.65], [-73.94, 42.81], [-74.5, 42.95], [-75.23, 43.1], [-75.9, 43.08], [-76.15, 43.05], [-76.9, 43.08],
                                [-77.61, 43.16], [-78.2, 43.2], [-78.69, 43.17], [-78.88, 42.89]]),
    ('Suez Canal', 1869, None, [[32.3, 31.26], [32.31, 31.0], [32.32, 30.85], [32.3, 30.68], [32.28, 30.58], [32.33, 30.42], [32.42, 30.28], [32.5, 30.1], [32.55, 29.94]]),
    ('Corinth Canal', 1893, None, [[22.94, 37.955], [23.0, 37.915]]),
    ('Kiel Canal', 1895, None, [[9.14, 53.9], [9.4, 54.1], [9.67, 54.3], [9.9, 54.33], [10.14, 54.37]]),
    ('Panama Canal', 1914, None, [[-79.915, 9.355], [-79.92, 9.27], [-79.85, 9.18], [-79.75, 9.13], [-79.69, 9.12], [-79.65, 9.05], [-79.61, 9.02],
                                  [-79.59, 9.0], [-79.57, 8.95]]),
    ('Volga–Don Canal', 1952, None, [[44.55, 48.5], [44.2, 48.6], [43.85, 48.65], [43.53, 48.69]]),
    ('Karakum Canal', 1959, None, [[65.0, 37.65], [64.3, 37.55], [63.3, 37.5], [62.4, 37.6], [61.85, 37.6], [61.2, 37.5], [60.45, 37.38],
                                   [59.6, 37.4], [58.95, 37.7], [58.38, 37.95], [57.4, 38.3]]),
    ('Rhine–Main–Danube Canal', 1992, None, [[10.89, 49.89], [11.0, 49.65], [11.08, 49.45], [11.35, 49.2], [11.6, 49.05], [11.88, 48.92]]),
]
NE_CANALS = {'White Sea Canal': 1933, 'Moscow Canal': 1937}
RIVER_NAMES = {'Chang Jiang': 'Yangtze', 'Huang': 'Yellow River', 'Amazonas': 'Amazon', 'Donau': 'Danube', 'Rhein': 'Rhine', 'Rhin': 'Rhine',
               'Al Furat': 'Euphrates', 'Firat': 'Euphrates', 'Dicle': 'Tigris', 'Dnepre': 'Dnieper', 'Dnipro': 'Dnieper', 'Heilong Jiang': 'Amur',
               'Ertis': 'Irtysh', 'Ertix': 'Irtysh', 'Lancang': 'Mekong', 'Nu': 'Salween', 'Ayeyarwady': 'Irrawaddy', 'El Bahr el Abyad': 'White Nile',
               'El Bahr el Azraq': 'Blue Nile', 'Abay': 'Blue Nile', 'Bahr el Jebel': 'White Nile', 'Bénoué': 'Benue', 'Sénégal': 'Senegal',
               'Wisla': 'Vistula', 'Elbe': 'Elbe', 'Labe': 'Elbe', 'Odra': 'Oder', 'Loire': 'Loire', 'Ebro': 'Ebro', 'Tajo': 'Tagus', 'Tejo': 'Tagus',
               'Po': 'Po', 'Tevere': 'Tiber', 'Severnaya Dvina': 'Northern Dvina', 'Zapadnaya Dvina': 'Daugava', 'Daugava': 'Daugava',
               'Syrdariya': 'Syr Darya', 'Amudar’ya': 'Amu Darya', 'Amu Darya': 'Amu Darya', 'Xi': 'Xi River', 'Jinsha': 'Yangtze',
               'Yarlung': 'Brahmaputra', 'Dihang': 'Brahmaputra', 'Padma': 'Ganges', 'Ganga': 'Ganges', 'Yamuna': 'Yamuna',
               'Rio Grande': 'Rio Grande', 'Grande': 'Rio Grande', 'Saint Lawrence': 'St. Lawrence', 'São Francisco': 'São Francisco'}


def river_layers():
    feats = ne('ne_10m_rivers_lake_centerlines_scale_rank')
    groups, named = {}, {}
    for ft in feats:
        p, g = ft['properties'], ft['geometry']
        if not g: continue
        cla = p['featurecla']
        z = float(p['min_zoom'] or 7)
        if z > 6.8: continue
        w = round(float(p['strokeweig'] or .2), 2)
        name = p['name'] or ''
        years = [(None, None)]
        if cla == 'Canal':
            if name not in NE_CANALS: continue
            years = [(NE_CANALS[name], None)]
        lines = [g['coordinates']] if g['type'] == 'LineString' else g['coordinates']
        for ln in lines:
            s = LineString(ln).simplify(.006 if z < 3 else .01 if z < 5 else .018)
            if s.length < .05 and z >= 5: continue
            pts = list(s.coords)
            if name == 'Huang' and min(x for x, _ in pts) >= 114.8:
                yrs = [(None, 1127), (1855, None)]
            else:
                yrs = years
            for y0, y1 in yrs:
                key = ('c' if cla == 'Canal' else 'r', z, w, y0, y1)
                groups.setdefault(key, []).append(enc(pts))
            if cla != 'Canal' and z <= 6:
                nm = RIVER_NAMES.get(name, p.get('name_en') or name)
                if nm: named.setdefault(nm, []).append((z, w, pts))
    groups.setdefault(('r', 3, 1.25, 1128, 1854), []).append(enc(YELLOW_SOUTH))
    named.setdefault('Yellow River (1128–1855)', []).append((3, 1.25, YELLOW_SOUTH))
    out = [{'k': k, 'z': z, 'w': w, **({'y0': y0} if y0 is not None else {}), **({'y1': y1} if y1 is not None else {}), 'g': g}
           for (k, z, w, y0, y1), g in sorted(groups.items(), key=lambda kv: (kv[0][1], -kv[0][2]))]
    return out, named


def canal_layers():
    out = []
    for name, y0, y1, pts in CANALS:
        out.append({'k': 'c', 'n': name, 'z': 3, 'w': .6, 'y0': y0, **({'y1': y1} if y1 else {}), 'g': [enc(pts)]})
    return out


# the rivers whose names show first, and where to write the best known ones
RIVER_TIER = {1: ['Nile', 'Amazon', 'Mississippi', 'Yangtze', 'Yellow River', 'Volga', 'Danube', 'Ganges', 'Indus', 'Congo', 'Niger',
                  'Euphrates', 'Tigris', 'Ob', 'Yenisey', 'Lena', 'Mekong', 'Paraná', 'Amur', 'Zambezi', 'Mackenzie', 'Rhine', 'Dnieper'],
              2: ['Don', 'Vistula', 'Oder', 'Elbe', 'Seine', 'Loire', 'Rhône', 'Po', 'Ebro', 'Tagus', 'Thames', 'Tiber', 'Missouri', 'Ohio',
                  'Rio Grande', 'St. Lawrence', 'Colorado', 'Columbia', 'Orinoco', 'Brahmaputra', 'Irrawaddy', 'Salween', 'Syr Darya',
                  'Amu Darya', 'Blue Nile', 'White Nile', 'Murray', 'Darling', 'Orange', 'Senegal', 'Yukon', 'Irtysh', 'Ural', 'Kama',
                  'Northern Dvina', 'São Francisco', 'Madeira', 'Negro', 'Xi River', 'Huai', 'Godavari', 'Krishna', 'Narmada', 'Jordan',
                  'Dniester', 'Daugava', 'Neva', 'Garonne', 'Douro', 'Guadalquivir', 'Weser', 'Main', 'Sava', 'Tisza', 'Drava', 'Kura',
                  'Araks', 'Han', 'Red River', 'Chao Phraya', 'Hudson', 'Delaware', 'Potomac', 'Tennessee', 'Arkansas', 'Red', 'Platte',
                  'Snake', 'Sacramento', 'Fraser', 'Nelson', 'Limpopo', 'Okavango', 'Kasai', 'Ubangi', 'Benue', 'Uruguay', 'Paraguay',
                  'Tocantins', 'Purus', 'Ucayali', 'Marañón', 'Magdalena', 'Pechora', 'Kolyma', 'Angara', 'Aldan', 'Vilyuy', 'Tobol',
                  'Ishim', 'Indigirka', 'Selenga', 'Liao', 'Songhua', 'Yalu', 'Sutlej', 'Chenab', 'Jhelum', 'Ravi', 'Yamuna', 'Karun',
                  'Helmand', 'Atrak', 'Kızılırmak', 'Sakarya', 'Meander', 'Struma', 'Maritsa', 'Vardar', 'Morava', 'Prut', 'Bug',
                  'Western Bug', 'Neman', 'Pripyat', 'Desna', 'Oka', 'Kama', 'Belaya', 'Vyatka', 'Shilka', 'Argun', 'Murrumbidgee',
                  'Lachlan', 'Fly', 'Sepik', 'Mahakam', 'Kapuas']}
TIER_OF = {n: t for t, ns in RIVER_TIER.items() for n in ns}
ANCHOR = {'Nile': (31.15, 27.6), 'Yangtze': (115.4, 29.9), 'Yellow River': (110.45, 37.2), 'Mississippi': (-91.1, 32.6),
          'Mekong': (105.85, 15.6), 'Danube': (19.0, 46.4), 'Volga': (46.4, 49.6), 'Euphrates': (41.0, 34.5), 'Tigris': (44.1, 34.1),
          'Indus': (69.4, 27.6), 'Ganges': (84.6, 25.5), 'Rhine': (7.6, 50.3), 'Amazon': (-60.5, -3.1), 'Niger': (-2.5, 14.9),
          'Dnieper': (31.2, 49.3), 'Congo': (19.0, 1.0)}


def river_labels(named):
    """a spot along each river to write its name, with the angle of the river there: the straightest stretch near the middle
    of its longest run, or near a chosen spot for the best known rivers"""
    out = []
    for name, parts in named.items():
        label = name.split(' (')[0]
        tier = TIER_OF.get(label, 3)
        zmin = min(z for z, _, _ in parts)
        merged = linemerge([LineString(p) for _, _, p in parts if len(p) > 1])
        runs = [merged] if merged.geom_type == 'LineString' else list(merged.geoms)
        plen = lambda r: sum(math.dist(proj(*a), proj(*b)) for a, b in zip(r.coords, r.coords[1:]))
        if label in ANCHOR and '1128' not in name:
            ax, ay = ANCHOR[label]
            run = min(runs, key=lambda r: r.distance(LineString([(ax, ay), (ax + 1e-6, ay)])))
        else:
            run = max(runs, key=plen)
        P = [proj(*c) for c in run.coords]
        seg = [math.dist(a, b) for a, b in zip(P, P[1:])]
        total = sum(seg)
        if total < (1.6 if tier < 3 else 4) * DEG: continue
        cum = np.concatenate([[0], np.cumsum(seg)])
        half = min(total * .3, 4 * DEG)
        best = None
        for i in range(len(P)):
            if cum[i] < half * .5 or cum[i] > total - half * .5: continue
            a = int(np.searchsorted(cum, cum[i] - half)); b = min(int(np.searchsorted(cum, cum[i] + half)), len(P) - 1)
            chord = math.dist(P[a], P[b]); path = cum[b] - cum[a]
            if label in ANCHOR and '1128' not in name:
                score = -math.dist(run.coords[i], ANCHOR[label])
            else:
                score = chord / max(path, 1e-9) - abs(cum[i] / total - .5) * .6
            if not best or score > best[0]:
                ang = math.degrees(math.atan2(P[b][1] - P[a][1], P[b][0] - P[a][0]))
                if ang > 90: ang -= 180
                if ang < -90: ang += 180
                best = (score, i, ang)
        if not best: continue
        lon, lat = run.coords[best[1]]
        # the zoom (map scale) at which the name appears
        k = 1.4 if tier == 1 else 2.6 if tier == 2 else max(4.5, 2 ** (zmin - 1.4))
        y = {'y0': 1128, 'y1': 1854} if '1128' in name else {}
        if y: tier = 2
        out.append({'n': label, 'lon': round(lon, 2), 'lat': round(lat, 2), 'a': round(best[2], 1), 'k': round(k, 1), 't': tier, **y})
    out.sort(key=lambda d: (d['k'], d['t']))
    return out


# ---------- lakes ----------
def poly_parts(geom, tol):
    geom = geom.simplify(tol, preserve_topology=True)
    polys = [geom] if geom.geom_type == 'Polygon' else list(getattr(geom, 'geoms', []))
    out = []
    for pg in polys:
        if pg.is_empty or pg.area < 1e-4: continue
        pg = orient(pg, sign=-1.0)  # d3 wants the outer ring clockwise
        rings = [enc(list(pg.exterior.coords))] + [enc(list(r.coords)) for r in pg.interiors if Polygon(r).area > 1e-4]
        if len(rings[0]) >= 6: out.append(rings)
    return out


def lake_layers():
    groups = {}
    for ft in ne('ne_10m_lakes'):
        p, g = ft['properties'], ft['geometry']
        if not g: continue
        z = float(p['min_zoom'] or 7)
        if z > 6.5: continue
        name = p['name'] or ''
        y0, y1 = None, None
        if p['featurecla'] == 'Reservoir' and name not in NATURAL:
            yr = p.get('year') or -99
            y0 = RES_YEAR.get(name, yr if yr and yr > 0 else 1960)
        if name in LAKE_YEARS: y0, y1 = LAKE_YEARS[name]
        parts = poly_parts(shape(g), .004 if z < 3 else .008 if z < 5 else .012)
        if parts: groups.setdefault((z, y0, y1), []).extend(parts)
    for ft in ne('ne_10m_lakes_historic'):
        p = ft['properties']
        if p['name'] not in HISTORIC: continue
        y0, y1 = HISTORIC[p['name']]
        groups.setdefault((3, y0, y1), []).extend(poly_parts(shape(ft['geometry']), .004))
    for (y0, y1), ring in POLDERS:
        groups.setdefault((4, y0, y1), []).extend(poly_parts(Polygon(ring), .001))
    return [{'k': 'l', 'z': z, **({'y0': y0} if y0 is not None else {}), **({'y1': y1} if y1 is not None else {}), 'g': g}
            for (z, y0, y1), g in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1] or -9999))]


# ---------- names on the sea and the land ----------
def proj_inv(x, y):
    """inverse of proj (y down), by Newton's method"""
    yy = -y; phi = yy
    for _ in range(30):
        p2 = phi * phi; p4 = p2 * p2
        f = phi * (1.007226 + p2 * (0.015085 + p4 * (-0.044475 + 0.028874 * p2 - 0.005916 * p4))) - yy
        df = 1.007226 + p2 * (0.015085 * 3 + p4 * (-0.044475 * 7 + 0.028874 * 9 * p2 - 0.005916 * 11 * p4))
        phi -= f / df
    p2 = phi * phi
    lam = x / (0.8707 + p2 * (-0.131979 + p2 * (-0.013791 + p2 * p2 * p2 * (0.003971 - 0.001529 * p2))))
    return math.degrees(lam), math.degrees(phi)


def place(geom, elong=1.8):
    """label point (pole of inaccessibility on screen) and angle along the long axis when the shape is long and thin"""
    polys = [geom] if geom.geom_type == 'Polygon' else list(geom.geoms)
    pg = max(polys, key=lambda g: g.area)
    sp = Polygon([proj(*c) for c in pg.exterior.coords], [[proj(*c) for c in r.coords] for r in pg.interiors]).buffer(0)
    if sp.geom_type != 'Polygon': sp = max(sp.geoms, key=lambda g: g.area)
    pt = polylabel(sp, tolerance=DEG * .05)
    lon, lat = proj_inv(pt.x, pt.y)
    rect = list(sp.minimum_rotated_rectangle.exterior.coords)
    e1 = (rect[1][0] - rect[0][0], rect[1][1] - rect[0][1]); e2 = (rect[2][0] - rect[1][0], rect[2][1] - rect[1][1])
    l1, l2 = math.hypot(*e1), math.hypot(*e2)
    long_e, ratio = (e1, l1 / max(l2, 1e-9)) if l1 >= l2 else (e2, l2 / max(l1, 1e-9))
    ang = 0.0
    if ratio > elong:
        ang = math.degrees(math.atan2(long_e[1], long_e[0]))
        if ang > 90: ang -= 180
        if ang < -90: ang += 180
        if abs(ang) < 8: ang = 0.0
    width = max(l1, l2) / DEG  # length of the shape in degrees-at-the-equator
    return round(lon, 2), round(lat, 2), round(ang, 1), round(width, 1)


OCEANS = [('Pacific Ocean', -150, 8), ('Pacific Ocean', 168, -32), ('Atlantic Ocean', -40, 31), ('Atlantic Ocean', -18, -21),
          ('Indian Ocean', 78, -24), ('Arctic Ocean', -8, 83), ('Southern Ocean', 60, -60)]
# the sea names each age used: modern name -> [(first year, last year, name)]
OLD_SEA = {'Mediterranean Sea': [(-146, 476, 'Mare Nostrum')], 'Black Sea': [(-700, 500, 'Pontus Euxinus')],
           'Red Sea': [(-300, 600, 'Sinus Arabicus')], 'Persian Gulf': [(-300, 600, 'Sinus Persicus')],
           'Arabian Sea': [(-300, 600, 'Erythraean Sea')], 'Adriatic Sea': [(-300, 476, 'Mare Hadriaticum'), (1000, 1797, 'Gulf of Venice')],
           'Aegean Sea': [(1453, 1830, 'The Archipelago')], 'North Sea': [(-100, 500, 'Mare Germanicum'), (1600, 1830, 'German Ocean')],
           'Baltic Sea': [(-100, 500, 'Mare Suebicum')], 'Sea of Azov': [(-600, 500, 'Lake Maeotis')],
           'Sea of Marmara': [(-600, 1453, 'Propontis')], 'Caspian Sea': [(-550, 640, 'Hyrcanian Sea')]}
# seas named on the world view; other seas wait for zoom by size
WORLD_SEAS = {'Mediterranean Sea', 'Caribbean Sea', 'Arabian Sea', 'Bay of Bengal', 'South China Sea', 'Gulf of Mexico', 'Black Sea',
              'Red Sea', 'Caspian Sea', 'Persian Gulf', 'Hudson Bay', 'Sea of Japan', 'Philippine Sea', 'Coral Sea', 'Tasman Sea'}
KEEP_CHANNELS = {'English Channel', 'Mozambique Channel', 'Drake Passage', 'Davis Strait', 'Hudson Strait', 'Luzon Strait', 'Makassar Strait',
                 'Yucatan Channel', 'Bass Strait', 'Torres Strait', 'Denmark Strait', 'Tatar Strait', 'La Pérouse Strait', 'Cook Strait'}
SEA_NAMES = {'SOUTHERN OCEAN': None, 'INDIAN OCEAN': None, 'Golfo de California': 'Gulf of California', 'Bahía de Campeche': 'Bay of Campeche',
             'Estrecho de Magellanes': None, 'The North Western Passages': 'Northwest Passage'}


def sea_labels():
    out = []
    for name, lon, lat in OCEANS:
        d = {'n': name, 'c': 'ocean', 'lon': lon, 'lat': lat, 'a': 0, 'k': .5}
        out.append(d)
    for ft in ne('ne_10m_geography_marine_polys'):
        p = ft['properties']; cla = p['featurecla']; name = p['name'] or ''
        name = SEA_NAMES.get(name, name)
        if not name or cla in ('ocean', 'generic', 'river', 'reef', 'inlet', 'fjord', 'lagoon'): continue
        if cla in ('strait', 'channel') and name not in KEEP_CHANNELS: continue
        sr = int(p['scalerank'] or 9)
        if sr > 6: continue
        lon, lat, ang, width = place(shape(ft['geometry']))
        if name in PLACE: lon, lat, ang = PLACE[name]
        k = .9 if name in WORLD_SEAS else {0: 1, 1: 1.5, 2: 2.2, 3: 3.2, 4: 4.5, 5: 7, 6: 10}[sr]
        d = {'n': name, 'c': 'sea' if sr <= 2 else 'sea2', 'lon': lon, 'lat': lat, 'a': ang, 'k': k, 'w': width}
        if name in OLD_SEA: d['old'] = OLD_SEA[name]
        out.append(d)
    return out


# straits and capes the history of the map turns on: name, lon, lat, zoom to show, older names, one line of history
STRAITS = [
    ('Strait of Gibraltar', -5.6, 35.95, 1.8, [(-1100, 710, 'Pillars of Hercules')], 'The gate between the Mediterranean and the Atlantic. Tariq crossed it in 711 to conquer Spain; the rock still bears his name.'),
    ('Bosporus', 29.05, 41.12, 2.2, [], 'Constantinople\'s strait, the only sea road between the Black Sea and the Mediterranean.'),
    ('Dardanelles', 26.4, 40.2, 2.6, [(-1200, 1453, 'Hellespont')], 'Xerxes bridged it with boats in 480 BC to invade Greece; the Gallipoli campaign was fought on its shore in 1915.'),
    ('Strait of Hormuz', 56.4, 26.45, 1.8, [], 'The mouth of the Persian Gulf. Portugal held Hormuz from 1515 to 1622; today a fifth of the world\'s oil sails through.'),
    ('Bab-el-Mandeb', 43.35, 12.6, 1.8, [], 'The "Gate of Grief" at the mouth of the Red Sea, on the sea road from the Mediterranean to India.'),
    ('Strait of Malacca', 99.8, 3.6, 1.6, [], 'The sea road between India and China. Srivijaya, Malacca and then Singapore grew rich guarding it.'),
    ('Strait of Dover', 1.45, 51.0, 2.6, [], 'The narrowest crossing of the English Channel, 33 km: the road of invaders from Caesar to William of Normandy.'),
    ('Øresund', 12.7, 55.9, 3.2, [], '"The Sound". Denmark made every ship pay a toll here from 1429 to 1857, the backbone of its crown\'s income.'),
    ('Strait of Messina', 15.62, 38.22, 3.5, [], 'Scylla and Charybdis of the Odyssey; the crossing from Italy to Sicily.'),
    ('Kerch Strait', 36.6, 45.3, 3.5, [(-600, 500, 'Cimmerian Bosporus')], 'The mouth of the Sea of Azov, guarded in antiquity by the Bosporan Kingdom.'),
    ('Bering Strait', -169.0, 65.8, 1.6, [], 'People first reached the Americas across this gap, then dry land, over 15,000 years ago.'),
    ('Strait of Magellan', -70.9, -53.6, 2.2, [], 'Magellan found this way into the Pacific in 1520, on the first voyage around the world.'),
    ('Cape of Good Hope', 18.47, -34.36, 1.8, [], 'Dias rounded it in 1488 and da Gama sailed past it to India in 1497, opening the sea route to Asia.'),
    ('Cape Horn', -67.27, -55.98, 1.8, [], 'The southern tip of the Americas, where the clipper route rounded through some of the worst seas on earth.'),
    ('Korea Strait', 129.3, 34.4, 2.4, [], 'Kublai Khan\'s fleets crossed it in 1274 and 1281 and were wrecked by the "divine winds"; Japan sank Russia\'s fleet here at Tsushima in 1905.'),
    ('Sunda Strait', 105.8, -6.0, 2.8, [], 'Between Java and Sumatra, the Dutch East India Company\'s gate to Batavia. Krakatoa exploded in it in 1883.'),
    ('Florida Straits', -80.5, 24.0, 2.4, [], 'Spain\'s treasure fleets rode the Gulf Stream home through here from Havana.'),
    ('Taiwan Strait', 119.6, 24.4, 2.6, [], 'Koxinga crossed it in 1661 to drive the Dutch from Taiwan.'),
]


def strait_labels():
    return [{'n': n, 'c': 'strait', 'lon': lon, 'lat': lat, 'k': k, **({'old': old} if old else {}), 'note': note}
            for n, lon, lat, k, old, note in STRAITS]


LAND_KEEP = {'Range/mtn', 'Desert', 'Plateau', 'Plain', 'Basin', 'Tundra', 'Depression', 'Wetlands', 'Valley', 'Delta'}
LAND_SKIP = {'Transantarctic Mountains', 'Polar Plateau', 'Western Plateau', 'Canadian Shield', 'Punjab', 'Caatingas', 'Selvas',
             'Bol’shezemel’skaya Tundra', 'American Highland', 'Siwalik Hills', 'Queen Maude Mountains', 'Península Ibérica',
             'Cordillera Occidental', 'Cordillera Real', 'Cordillera Oriental', 'Cord. Central', 'Cord. Occidental', 'Chaco Boreal',
             'Chaco Austral', 'Coastal Plain', 'Central Lowland', 'North Slope', 'Barren Grounds', 'Crystal Mountains', 'Western Desert',
             'Great Artesian Basin', 'Planalto Central', 'Katanga Plateau', 'Aldan Upland', 'Yukon Plateau', 'Cumberland Plateau',
             'Allegheny Plateau', 'Columbia Plateau', 'Khorat Plateau', 'Central Highlands', 'Guiana Shield', 'Betpaqdala Desert',
             'Mitumba Mountains', 'Tarbagatay Range', 'Altun Mountains', 'Dabie Mountains', 'Wuyi Mountains', 'Quilian Mountains',
             'Lesser Khingan Range', 'Chugach Mountains', 'Mackenzie Mountains', 'Haut Atlas', 'Atlas Saharien', 'Asir Mountains',
             'Coast Ranges', 'Sierra Madre del Sur', 'Eastern Sayan Mountains', 'Yablonovyy Range', 'Aïr Mountains', 'Putorana Plateau'}
LAND_NAMES = {'Caucasus Mountains': 'Caucasus', 'Appalachian Mountains': 'Appalachians', 'Karakoram Range': 'Karakoram',
              'Chaîne Annamitique': 'Annamite Range', 'Plateau of Tibet': 'Tibetan Plateau', 'Rub’ al Khali': 'Rub\' al Khali',
              'Appennini': 'Apennines', 'Garagum Desert': 'Karakum Desert', 'Qizilqum Desert': 'Kyzylkum Desert',
              'Desierto de Atacama': 'Atacama Desert', 'Kjølen Mountains': 'Scandinavian Mountains', 'Elburz Mountains': 'Alborz Mountains',
              'Planalto do Mato Grosso': 'Mato Grosso Plateau', 'Alti-planicie Mexicana': 'Mexican Plateau', 'Murray-darling Basin': 'Murray–Darling Basin',
              'Sikhote-alin’ Range': 'Sikhote-Alin', 'Tibesti Mountains': 'Tibesti', 'Ahaggar Mountains': 'Ahaggar', 'Nan Ling Mountains': 'Nanling'}
# where to write a name, and at what angle, when the shape misleads: name -> (lon, lat, angle)
PLACE = {'Mediterranean Sea': (18.0, 34.6, 0), 'Black Sea': (34.0, 43.3, 0), 'South China Sea': (114.0, 14.5, -58), 'Sea of Okhotsk': (149.5, 54.5, 0),
         'Andaman Sea': (96.0, 10.5, -80), 'Drake Passage': (-64.0, -58.5, 0), 'Scotia Sea': (-45.0, -57.5, 0), 'Sahara': (8.0, 23.5, 0),
         'Northern European Plain': (16.0, 52.6, 0), 'Rocky Mountains': (-110.5, 43.5, -56), 'Kalahari Desert': (22.5, -23.5, 0),
         'Great Dividing Range': (148.5, -27.0, -70), 'Arabian Sea': (63.0, 14.5, 0), 'Caribbean Sea': (-75.0, 14.5, 0)}
EXTRA_LAND = [('Nile Delta', 'land', 31.0, 30.85, 0, 3.2), ('Mesopotamia', 'land', 44.6, 33.6, -38, 2.6), ('Anatolia', 'land', 33.0, 39.0, 0, 2.4)]
LAND_EXTRA_K = {'Pontic Steppe': 1.8, 'Kazakh Steppe': 1.8, 'Sahara': .9, 'Gobi Desert': 1.3, 'Himalayas': 1.3, 'Andes': 1.2, 'Alps': 1.8,
                'Rocky Mountains': 1.3, 'Ural Mountains': 1.6, 'Great Plains': 1.6, 'Amazon Basin': 1.3, 'Tibetan Plateau': 1.6,
                'Arabian Desert': 1.8, 'Kalahari Desert': 1.8, 'Atlas Mountains': 2.2, 'Zagros Mountains': 2.2, 'Taurus Mountains': 3,
                'Pyrenees': 3, 'Carpathian Mountains': 2.6, 'Hindu Kush': 2.4, 'Sahel': 1.8, 'Caucasus': 1.8, 'Tian Shan': 2,
                'Appalachians': 2.2, 'Great Dividing Range': 2.4, 'Congo Basin': 1.6, 'Deccan Plateau': 2.4, 'Pampas': 2.4,
                'Mongolian Plateau': 2.4, 'Taklamakan Desert': 2.2, 'Syrian Desert': 2.6, 'Thar Desert': 2.6, 'Karakum Desert': 2.6,
                'Kyzylkum Desert': 2.8, 'Apennines': 3.4, 'Balkan Mountains': 3.4, 'Dinaric Alps': 3.4, 'Nubian Desert': 2.6,
                'Libyan Desert': 2.6, 'Great Basin': 3, 'Sierra Madre Occidental': 3, 'Sierra Madre Oriental': 3.2, 'Altay Mountains': 2.8,
                'Kunlun Mountains': 2.4, 'Zagros': 2.2, 'Brazilian Highlands': 2.4, 'Patagonia': 2.4, 'Atacama Desert': 2.8,
                'Great Victoria Desert': 2.6, 'Great Sandy Desert': 2.6, 'Ethiopian Highlands': 2.4, 'Rub\' al Khali': 2.4,
                'Scandinavian Mountains': 2.6, 'Pamirs': 2.6, 'Elburz Mountains': 3, 'Anatolian Plateau': 3, 'Iranian Plateau': 2.6}


def tcase(n):
    small = {'of', 'the', 'de', 'del', 'al', 'do'}
    n = ' '.join(w.lower() if (i and w.lower() in small) else w[:1].upper() + w[1:].lower() if w.isupper() else w
                 for i, w in enumerate(n.split()))
    return n.replace(' Mts.', ' Mountains').replace(' Ra.', ' Range').replace(' Plat.', ' Plateau')


def land_labels():
    out, seen = [], set()
    for ft in ne('ne_10m_geography_regions_polys'):
        p = ft['properties']; cla = p['FEATURECLA']; sr = int(p['SCALERANK'] or 9)
        if cla not in LAND_KEEP: continue
        name = tcase(p['NAME'] or '')
        name = LAND_NAMES.get(name, name)
        if not name or name in LAND_SKIP or (sr > 3 and name not in LAND_EXTRA_K): continue
        if name in seen: continue
        seen.add(name)
        lon, lat, ang, width = place(shape(ft['geometry']), elong=1.6 if cla == 'Range/mtn' else 2.6)
        if name in PLACE: lon, lat, ang = PLACE[name]
        if lat < -60: continue
        k = LAND_EXTRA_K.get(name, {1: 1.7, 2: 2.6, 3: 3.6}.get(sr, 4.5))
        out.append({'n': name, 'c': 'mtn' if cla == 'Range/mtn' else 'land', 'lon': lon, 'lat': lat, 'a': ang, 'k': k, 'w': width})
    out += [{'n': n, 'c': c, 'lon': lon, 'lat': lat, 'a': a, 'k': k} for n, c, lon, lat, a, k in EXTRA_LAND]
    return out


# peaks: name, lon, lat, metres, zoom to show, volcano, one line of history
PEAKS = [
    ('Everest', 86.925, 27.988, 8849, 2.2, 0, 'The highest mountain on earth, first climbed by Tenzing Norgay and Edmund Hillary in 1953.'),
    ('K2', 76.513, 35.881, 8611, 4, 0, ''),
    ('Kilimanjaro', 37.355, -3.066, 5895, 2.4, 1, 'Africa\'s highest mountain, a dormant volcano capped with ice near the equator.'),
    ('Mont Blanc', 6.865, 45.833, 4806, 4, 0, 'The roof of the Alps, first climbed in 1786.'),
    ('Mount Olympus', 22.35, 40.085, 2918, 3.6, 0, 'Home of the Greek gods.'),
    ('Mount Ararat', 44.30, 39.70, 5137, 3, 1, 'Where Noah\'s Ark came to rest, in the Bible; the symbol of Armenia.'),
    ('Mount Fuji', 138.727, 35.361, 3776, 3, 1, 'Japan\'s sacred volcano; it last erupted in 1707.'),
    ('Vesuvius', 14.426, 40.821, 1281, 4, 1, 'Its eruption in AD 79 buried Pompeii and Herculaneum.'),
    ('Etna', 14.995, 37.751, 3357, 4, 1, 'Europe\'s most active volcano; the Greeks put the forge of Hephaestus under it.'),
    ('Mount Sinai', 33.975, 28.539, 2285, 4, 0, 'Where Moses received the Ten Commandments, by tradition.'),
    ('Elbrus', 42.439, 43.355, 5642, 3.4, 1, 'The highest peak of the Caucasus, where Prometheus was chained in Greek myth.'),
    ('Aconcagua', -70.011, -32.653, 6961, 2.6, 0, 'The highest mountain outside Asia.'),
    ('Denali', -151.007, 63.069, 6190, 2.8, 0, 'North America\'s highest peak.'),
    ('Mount Kailash', 81.311, 31.067, 6638, 4, 0, 'Sacred to Hindus, Buddhists, Jains and Bön; never climbed.'),
    ('Mount Tai', 117.10, 36.25, 1545, 4.5, 0, 'The most sacred of China\'s mountains, where emperors made sacrifices to Heaven.'),
    ('Popocatépetl', -98.622, 19.023, 5426, 4, 1, 'The smoking volcano above the Valley of Mexico.'),
    ('Chimborazo', -78.817, -1.469, 6263, 4, 1, 'Its summit is the point farthest from the earth\'s centre.'),
    ('Thera', 25.396, 36.404, 367, 5, 1, 'Its eruption around 1600 BC buried the Minoan town of Akrotiri.'),
    ('Krakatoa', 105.423, -6.102, 813, 5, 1, 'Its eruption in 1883 was heard 4,800 km away and cooled the world.'),
    ('Tambora', 118.0, -8.25, 2850, 5, 1, 'The eruption of 1815 brought the "year without a summer" of 1816.'),
    ('Mount Athos', 24.326, 40.157, 2033, 5, 0, 'The holy mountain of Orthodox monks, home of monasteries for over a thousand years.'),
]


def peak_labels():
    return [{'n': n, 'c': 'peak', 'lon': lon, 'lat': lat, 'm': m, 'k': k, **({'v': 1} if v else {}), **({'note': note} if note else {})}
            for n, lon, lat, m, k, v, note in PEAKS]


# ---------- ocean currents ----------
# name, warm (1) or cold (0), points along the flow
CURRENTS = [
    ('Gulf Stream', 1, [(-80.4, 25.4), (-79.9, 28.5), (-78.6, 32.0), (-75.2, 35.3), (-70, 38.2), (-62, 40.2), (-52, 41.6), (-44, 43.2)]),
    ('North Atlantic Drift', 1, [(-44, 43.2), (-35, 47), (-25, 51), (-16, 55), (-9, 58.5), (0, 61.5), (8, 64.5), (14, 68), (20, 71)]),
    ('Canary Current', 0, [(-16, 42), (-13.5, 37), (-11.5, 33), (-14, 28.5), (-18, 23.5), (-21, 18)]),
    ('North Equatorial Current', 1, [(-23, 15), (-35, 13.5), (-48, 12.5), (-58, 13.5), (-68, 14.5), (-77, 16), (-84, 19.5), (-86, 23.5), (-83.5, 25), (-80.6, 25)]),
    ('South Equatorial Current', 1, [(8, -2), (-5, -3), (-18, -4), (-30, -5), (-34.5, -6)]),
    ('Brazil Current', 1, [(-34.5, -8), (-37, -14), (-39.5, -20), (-43.5, -25.5), (-48.5, -31), (-52.5, -37)]),
    ('Benguela Current', 0, [(17, -35), (14, -30), (12, -24), (10, -18), (8, -11), (5.5, -4)]),
    ('Agulhas Current', 1, [(40.5, -15.5), (37, -22), (33, -29), (28.5, -33.8), (22.5, -36.8), (18.5, -38)]),
    ('Antarctic Circumpolar Current', 0, [(-180, -58), (-150, -60), (-120, -58), (-90, -57), (-70, -58.5), (-60, -57.5), (-40, -53), (-10, -50),
                                          (20, -48), (50, -48), (80, -50), (110, -52), (140, -54), (170, -57), (180, -58)]),
    ('Kuroshio', 1, [(122, 21.5), (123.5, 25.5), (127.5, 29), (132, 31.8), (138, 34.3), (145, 35.8), (155, 37.2)]),
    ('North Pacific Current', 1, [(155, 38.5), (170, 40.5), (-170, 42.5), (-150, 44.5), (-135, 45.5)]),
    ('California Current', 0, [(-128, 48), (-126, 42), (-123.2, 36), (-118.5, 30), (-115.5, 24.5)]),
    ('Oyashio', 0, [(165, 58), (160, 52), (153, 46), (146.5, 42), (143.5, 38.8)]),
    ('North Equatorial Current', 1, [(-110, 15), (-130, 14), (-150, 13), (-170, 13), (170, 14), (150, 15), (132, 15.5), (124, 18)]),
    ('Humboldt Current', 0, [(-75.5, -45), (-74.5, -38), (-73.2, -30), (-72.2, -22), (-77, -14), (-81.5, -6), (-86, -2)]),
    ('South Equatorial Current', 1, [(-86, -2), (-100, -4), (-120, -5), (-140, -6), (-160, -8), (-180, -10), (165, -12), (156, -14)]),
    ('East Australian Current', 1, [(155.5, -15), (154.5, -22), (154.2, -28), (153.4, -33), (151.5, -38)]),
    ('Labrador Current', 0, [(-61, 66.5), (-58.5, 60.5), (-55, 55.5), (-51.5, 50.5), (-50, 46)]),
    ('East Greenland Current', 0, [(-12, 76), (-20, 71), (-28, 67), (-36, 63.5), (-43, 60.2)]),
    ('South Equatorial Current', 1, [(112, -12), (97, -12), (82, -12), (67, -12.5), (54, -14), (46, -15)]),
    ('West Australian Current', 0, [(114.5, -36), (112, -30), (110, -25), (108, -19)]),
    ('Somali Current', 1, [(40.5, -8), (43.5, 0), (48.5, 5.5), (52.5, 10.5), (57.5, 14.5)]),
]
CURRENT_LABEL_K = {'Gulf Stream': 1.4, 'North Atlantic Drift': 2, 'Kuroshio': 1.6, 'Humboldt Current': 1.8, 'Benguela Current': 2,
                   'Canary Current': 2, 'California Current': 2, 'Agulhas Current': 2.2, 'Brazil Current': 2.4, 'Labrador Current': 2.4,
                   'Antarctic Circumpolar Current': 2, 'Oyashio': 2.6, 'East Australian Current': 2.6, 'Somali Current': 2.6}


def spline(pts, step=1.0):
    """Catmull-Rom through the points (longitudes unwrapped across the date line), about a point per degree"""
    P = [list(pts[0])]
    for lon, lat in pts[1:]:
        while lon - P[-1][0] > 180: lon -= 360
        while lon - P[-1][0] < -180: lon += 360
        P.append([lon, lat])
    P = [P[0]] + P + [P[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        n = max(2, int(math.dist(p1, p2) / step))
        for j in range(n):
            t = j / n; t2, t3 = t * t, t * t * t
            out.append([.5 * ((2 * p1[c]) + (-p0[c] + p2[c]) * t + (2 * p0[c] - 5 * p1[c] + 4 * p2[c] - p3[c]) * t2 +
                              (-p0[c] + 3 * p1[c] - 3 * p2[c] + p3[c]) * t3) for c in (0, 1)])
    out.append(P[-2])
    return [[((x + 180) % 360) - 180 if abs(x) > 180 else x, y] for x, y in out]


def currents():
    out = []
    for name, warm, pts in CURRENTS:
        line = spline(pts)
        d = {'n': name, 'warm': warm, 'g': enc(line)}
        k = CURRENT_LABEL_K.get(name)
        if k:
            mid = line[len(line) // 2]; a, b = proj(*line[max(0, len(line) // 2 - 3)]), proj(*line[min(len(line) - 1, len(line) // 2 + 3)])
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
            if ang > 90: ang -= 180
            if ang < -90: ang += 180
            d['label'] = {'lon': round(mid[0], 2), 'lat': round(mid[1], 2), 'a': round(ang, 1), 'k': k}
        out.append(d)
    return out


if __name__ == '__main__':
    rivers, named = river_layers()
    water = {'rivers': rivers + canal_layers(), 'lakes': lake_layers(), 'labels': river_labels(named)}
    p = os.path.join(OUT, 'water.json')
    json.dump(water, open(p, 'w'), separators=(',', ':'), ensure_ascii=False)
    print('water.json', os.path.getsize(p) // 1024, 'KB:', len(water['rivers']), 'river groups,', len(water['lakes']), 'lake groups,',
          len(water['labels']), 'river names')
    geo = {'labels': sea_labels() + strait_labels() + land_labels() + peak_labels(), 'currents': currents()}
    p = os.path.join(OUT, 'geo.json')
    json.dump(geo, open(p, 'w'), separators=(',', ':'), ensure_ascii=False)
    print('geo.json', os.path.getsize(p) // 1024, 'KB:', len(geo['labels']), 'names,', len(geo['currents']), 'currents')

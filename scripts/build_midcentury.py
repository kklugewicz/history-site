"""Border years between 1815 and 1878, which historical-basemaps does not have.

    python3 scripts/build_midcentury.py data

Without them every year from 1815 to 1877 showed the 1815 map: Spain's viceroyalties in 1857, no Mexico, no Gran Colombia,
the American West still Spanish. This builds twelve snapshots from the two border files either side (data/borders_1815.json
and data/borders_1878.json) and cuts the changes of those years into them:

  1822  Mexican Empire (with Central America), Gran Colombia, Empire of Brazil, royalist Upper Peru; Haiti holds Hispaniola;
        the United Kingdom of the Netherlands; the Oregon Country held jointly by Britain and the United States
  1823  the Mexican republic and the Federal Republic of Central America
  1825  Bolivia free after Ayacucho
  1831  Gran Colombia split (New Granada, Venezuela, Ecuador); Uruguay; Belgium; Greece; autonomous Serbia
  1836  Republic of Texas; Peru-Bolivian Confederation
  1840  Central America split into five republics; Peru and Bolivia apart again
  1846  Texas and Oregon to the United States; Dominican Republic; French Algeria
  1848  the Mexican Cession
  1854  the Gadsden Purchase
  1861  Italy (without Venetia and Rome); the United Principalities (Romania); Argentina
  1867  base 1878: Alaska to the United States, North German Confederation, Italy without Rome, United States of Colombia
  1871  base 1878: German Empire and Italy with Rome, before the Treaty of Berlin (Bulgaria, Bosnia still Ottoman)

It also corrects three later source years: 1878 and 1880 name the Empire of Brazil a kingdom and 1900 the republic, and
1900 draws South America as before the War of the Pacific. (1878 still gives Greece Thessaly three years early.)

Files up to 1861 keep the 1815 map outside the Americas and the European changes above; 1867 and 1871 start from 1878.
The Americas come from 1878's shapes throughout, so every year's borders meet without gaps.
Run after scripts/build_data.py, which lists these years in timeline.json (MID_FILES there). Running it again gives the
same files: the later years are put right only once."""
import ast, json, os, sys
from shapely.geometry import shape, Point, Polygon, box
from shapely.ops import unary_union
from shapely.geometry.polygon import orient

OUT = sys.argv[1] if len(sys.argv) > 1 else 'data'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# the region anchors and the tidy-up of scripts/build_data.py, read from it so the two never differ
_src = open(os.path.join(ROOT, 'scripts', 'build_data.py')).read()
REGIONS = next(ast.literal_eval(n.value) for n in ast.parse(_src).body
               if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'REGIONS')
anchors = [(r, Point(p)) for r, ps in REGIONS.items() for p in ps]
order = list(REGIONS)


def fmt(p): return round(p, 2)


def clean(geom, tol=0.02):
    geom = geom.simplify(tol, preserve_topology=True).buffer(0)
    polys = [geom] if geom.geom_type == 'Polygon' else list(getattr(geom, 'geoms', []))
    polys = [orient(p, sign=-1.0) for p in polys if p.geom_type == 'Polygon' and p.area > 0.004]
    if not polys: return None
    coords = []
    for p in polys:
        rings = [[[fmt(x), fmt(y)] for x, y, *_ in p.exterior.coords]]
        rings += [[[fmt(x), fmt(y)] for x, y, *_ in r.coords] for r in p.interiors]
        coords.append(rings)
    return {'type': 'MultiPolygon', 'coordinates': coords}


def regions_of(g):
    parts = list(g.geoms) if hasattr(g, 'geoms') else [g]
    big = max(parts, key=lambda p: p.area)
    rp = big.representative_point()
    inside = big.buffer(0.05)
    home = next((r for r, p in anchors if inside.contains(p) and p.distance(rp) < 8), None) \
        or min(anchors, key=lambda a: a[1].distance(big))[0]
    regs = {r for r, p in anchors if g.buffer(0.05).contains(p)}
    return [home] + sorted(regs - {home}, key=order.index)


def load(f):
    d = json.load(open(os.path.join(OUT, 'borders_%s.json' % f)))
    return [(ft['properties'], shape(ft['geometry']).buffer(0), ft['geometry']) for ft in d['features']]


class Map:
    """a border file being edited: an ordered list of [props, geometry, the source geometry while the state is untouched]
    (an untouched state is written exactly as it was read)"""

    def __init__(self, feats):
        self.f = [[dict(p), g, raw] for p, g, raw in feats]

    def get(self, name):
        return next((x[1] for x in self.f if x[0]['name'] == name), None)

    def has(self, name):
        return self.get(name) is not None

    def drop(self, *names):
        self.f = [x for x in self.f if x[0]['name'] not in names]

    def put(self, name, geom, sub=None, keep_others=False):
        """add (or replace) a state: its land is taken from every other state unless keep_others"""
        geom = geom.buffer(0)
        if not keep_others:
            for x in self.f:
                if x[0]['name'] != name and x[1].intersects(geom) and x[1].intersection(geom).area > 1e-6:
                    x[1] = x[1].difference(geom).buffer(0); x[2] = None
        props = {'name': name}
        if sub: props['sub'] = sub
        for x in self.f:
            if x[0]['name'] == name:
                x[0] = props; x[1] = geom; x[2] = None; return
        self.f.append([props, geom, None])

    def give(self, name, piece):
        """hand a piece of land to a state, taking it from whoever held it"""
        for x in self.f:
            if x[0]['name'] != name and x[1].intersects(piece) and x[1].intersection(piece).area > 1e-6:
                x[1] = x[1].difference(piece).buffer(0); x[2] = None
        for x in self.f:
            if x[0]['name'] == name:
                x[1] = x[1].union(piece).buffer(0); x[2] = None

    def rename(self, old, new):
        for x in self.f:
            if x[0]['name'] == old: x[0]['name'] = new

    def write(self, f, tol=0.02):
        feats = []
        for p, g, raw in self.f:
            if raw:   # untouched: as it was
                feats.append({'type': 'Feature', 'properties': p, 'geometry': raw}); continue
            if g.is_empty: continue
            # a state the cuts left as crumbs is dropped rather than drawn as a few specks
            geo = clean(g, tol)
            if not geo: continue
            props = {'name': p['name'], 'regions': regions_of(g)}
            for k in ('sub', 'part'):
                if p.get(k): props[k] = p[k]
            feats.append({'type': 'Feature', 'properties': props, 'geometry': geo})
        path = os.path.join(OUT, 'borders_%s.json' % f)
        json.dump({'type': 'FeatureCollection', 'features': feats}, open(path, 'w'), separators=(',', ':'), ensure_ascii=False)
        print(f, len(feats), os.path.getsize(path) // 1024, 'KB')


B1815, B1878 = load('1815'), load('1878')
M15, M78 = Map(B1815), Map(B1878)
# 1878's Brazil is renamed below (fixes to 1878, 1880 and 1900), so a second run finds it under its new name
M78.rename('Kingdom of Brazil', 'Empire of Brazil')
g78 = M78.get
U = lambda *gs: unary_union([g for g in gs if g is not None]).buffer(0)

# ---------- the Americas, cut from 1878's shapes ----------
ALASKA = g78('United States of America').intersection(box(-180, 51, -129.9, 72))
LOWER48 = g78('United States of America').difference(ALASKA)
NEW_SPAIN = M15.get('Viceroyalty of New Spain')
# what of the 1878 United States had been New Spain's (Texas, the Southwest, California), from the 1815 line
SPANISH_NORTH = LOWER48.intersection(NEW_SPAIN).buffer(0)
# drop slivers where the two files' lines differ a little: keep only the large pieces
SPANISH_NORTH = U(*[p for p in getattr(SPANISH_NORTH, 'geoms', [SPANISH_NORTH]) if p.area > 1])
US_1821 = LOWER48.difference(SPANISH_NORTH)
CENTRAL = ['Guatemala', 'El Salvador', 'Honduras', 'Nicaragua', 'Costa Rica']
CENTRAL_ALL = U(*[g78(n) for n in CENTRAL])
MEXICO_1878 = g78('Mexico')
MEXICO_1825 = U(MEXICO_1878, SPANISH_NORTH)

# The Rio Grande from its mouth to its source, then the Republic of Texas's claim due north to the 42nd parallel
RIO_GRANDE = [(-97.15, 25.95), (-97.5, 25.88), (-98.2, 26.06), (-98.8, 26.36), (-99.1, 26.55), (-99.5, 27.5), (-100.3, 28.3),
              (-100.5, 28.7), (-101.0, 29.4), (-101.4, 29.77), (-102.0, 29.8), (-102.7, 29.75), (-103.0, 29.0), (-103.3, 29.0),
              (-104.0, 29.4), (-104.4, 29.57), (-104.7, 30.1), (-105.0, 30.7), (-106.0, 31.4), (-106.5, 31.78), (-106.75, 32.3),
              (-106.9, 33.0), (-106.85, 34.0), (-106.7, 34.8), (-106.65, 35.1), (-106.4, 35.6), (-106.1, 36.0), (-105.75, 36.5),
              (-105.8, 37.0), (-106.2, 37.5), (-107.0, 37.75), (-107.3, 37.8)]
TEXAS_CLAIM = Polygon(RIO_GRANDE + [(-107.3, 42.5), (-90, 42.5), (-90, 25.0), (-97.0, 25.4)])
TEXAS = MEXICO_1825.intersection(TEXAS_CLAIM).buffer(0)
# The Gadsden Purchase (1853): south of the Gila and of the 1848 line along 32 deg 22' N, north of today's border
GADSDEN_AREA = Polygon([(-114.62, 32.73), (-114.0, 32.85), (-113.3, 32.95), (-112.8, 32.95), (-112.4, 33.15), (-111.9, 33.15),
                        (-111.39, 33.03), (-110.77, 32.98), (-110.45, 33.1), (-109.9, 32.9), (-109.6, 32.85), (-109.6, 32.37),
                        (-106.75, 32.37), (-106.55, 31.78), (-106.0, 30.5), (-116.0, 30.5), (-116.0, 32.6)])
GADSDEN = SPANISH_NORTH.intersection(GADSDEN_AREA).buffer(0)
CESSION_LAND = SPANISH_NORTH.difference(TEXAS)   # what Mexico lost in 1848 and 1853

# The Oregon Country (1818-1846), held jointly by Britain and the United States: west of the Continental Divide,
# from 42 deg N to 54 deg 40' N
DIVIDE = [(-109.3, 42.0), (-109.0, 42.4), (-109.8, 43.3), (-110.3, 44.2), (-111.2, 44.6), (-112.3, 44.5), (-113.4, 45.0),
          (-113.9, 45.7), (-112.5, 46.0), (-112.4, 46.6), (-112.4, 47.1), (-113.4, 48.3), (-113.9, 48.8), (-114.06, 49.0),
          (-115.5, 50.3), (-116.3, 51.45), (-117.5, 52.0), (-118.45, 52.9), (-119.5, 53.7), (-120.3, 54.2), (-120.8, 54.67)]
OREGON_AREA = Polygon(DIVIDE + [(-145, 54.67), (-145, 41.99), (-109.3, 41.99)])
CANADA = g78('Canada')
OREGON = U(US_1821, CANADA).intersection(OREGON_AREA).buffer(0)
OREGON_SOUTH = OREGON.intersection(box(-145, 40, -100, 49.0))

HISPANIOLA = box(-74.6, 17.5, -68.2, 20.1)

SOUTH_1878 = ['Colombia', 'Venezuela', 'Ecuador', 'Peru', 'Bolivia', 'Chile', 'Argentina', 'Paraguay', 'Uruguay',
              'Empire of Brazil', 'British Guiana', 'Dutch Guiana', 'French Guiana', 'Mapuche', 'Pampas cultures',
              'Patagonian shellfish and marine mammal hunters']
OLD_AMERICAS = ['Viceroyalty of New Spain', 'United States', 'Viceroyalty of New Granada', 'Viceroyalty of Peru',
                'Viceroyalty of Brazil', 'United Provinces of the Río de la Plata', 'Paraguay', 'Guiana', 'Shuar',
                'Pampas cultures', 'Patagonian shellfish and marine mammal hunters', 'Mapuche']


def americas(m, y):
    """the Americas of year y (1822 to 1871) on the map m"""
    m.drop(*OLD_AMERICAS)
    for n in ('United States of America', 'Mexico', *CENTRAL, *SOUTH_1878):
        m.drop(n)
    us = 'United States' if y < 1867 else 'United States of America'
    # North America
    if y < 1846:
        m.put(us, US_1821.difference(OREGON))
        m.put('Oregon Country', OREGON)
    elif y < 1848:
        m.put(us, U(US_1821.difference(OREGON), OREGON_SOUTH, TEXAS))
    elif y < 1854:
        m.put(us, U(US_1821, OREGON_SOUTH, CESSION_LAND.difference(GADSDEN), TEXAS))
    else:
        m.put(us, U(LOWER48, ALASKA) if y >= 1867 else LOWER48)
    if y >= 1846: m.put('Canada', CANADA.difference(OREGON_SOUTH))
    mexico = MEXICO_1878 if y >= 1854 else U(MEXICO_1878, GADSDEN) if y >= 1848 else MEXICO_1825.difference(TEXAS) if y >= 1836 else MEXICO_1825
    if y < 1823:
        m.put('Mexican Empire', U(mexico, CENTRAL_ALL))
    else:
        m.put('Mexico', mexico)
        if 1836 <= y < 1846: m.put('Republic of Texas', TEXAS)
        if y < 1840:
            m.put('Federal Republic of Central America', CENTRAL_ALL)
        else:
            for n in CENTRAL: m.put(n, g78(n))
    # Hispaniola: Haiti held the whole island from 1822 to 1844
    if y < 1846:
        m.put('Haiti', U(m.get('Haiti'), m.get('Spain').intersection(HISPANIOLA)))
    else:
        m.put('Haiti', g78('Haiti')); m.put('Dominican Republic', g78('Dominican Republic'))
    # South America
    for n in ('British Guiana', 'Dutch Guiana', 'French Guiana', 'Paraguay', 'Chile', 'Mapuche', 'Pampas cultures',
              'Patagonian shellfish and marine mammal hunters'):
        m.put(n, g78(n))
    if y < 1831:
        m.put('Gran Colombia', U(g78('Colombia'), g78('Venezuela'), g78('Ecuador')))
    else:
        m.put('Republic of New Granada' if y < 1858 else 'United States of Colombia', g78('Colombia'))
        m.put('Venezuela', g78('Venezuela')); m.put('Ecuador', g78('Ecuador'))
    if y < 1825:
        m.put('Peru', g78('Peru'))
        m.put('Viceroyalty of Peru', g78('Bolivia'), sub='Spain')   # royalist Upper Peru until Ayacucho (1824)
    elif 1836 <= y < 1840:
        m.put('Peru–Bolivian Confederation', U(g78('Peru'), g78('Bolivia')))
    else:
        m.put('Peru', g78('Peru')); m.put('Bolivia', g78('Bolivia'))
    m.put('United Provinces of the Río de la Plata' if y < 1831 else 'Argentine Confederation' if y < 1861 else 'Argentina',
          g78('Argentina'))
    if y < 1831:
        m.put('Empire of Brazil', U(g78('Empire of Brazil'), g78('Uruguay')))   # Uruguay was Brazil's Cisplatina
    else:
        m.put('Empire of Brazil', g78('Empire of Brazil')); m.put('Uruguay', g78('Uruguay'))


# ---------- Europe and North Africa ----------
NL, BE = g78('Netherlands'), g78('Belgium')
ARTA_VOLOS = Polygon([(19.5, 30), (19.5, 39.15), (20.98, 39.16), (22.94, 39.36), (27, 39.4), (27, 30)])
IONIAN = box(19.0, 37.5, 21.0, 39.9)
# 1832: the mainland south of the Arta-Volos line, Euboea and the Cyclades; the Ionian Islands were British until 1864
GREECE_1832 = U(g78('Greece'),
                M15.get('Ottoman Empire').intersection(box(22.8, 36.3, 25.9, 39.15)),
             M15.get('Ottoman Empire').intersection(box(21.0, 36.3, 23.2, 38.35))) \
    .intersection(ARTA_VOLOS).intersection(box(19, 36.0, 26, 40)).difference(IONIAN)
IONIAN_ISLANDS = U(*[p for p in getattr(g78('Greece'), 'geoms', [g78('Greece')]) if IONIAN.contains(p)])
LAZIO = Polygon([(11.4, 42.4), (11.9, 42.78), (12.6, 42.62), (13.2, 42.15), (13.9, 41.6), (13.75, 41.25), (12.8, 41.2), (11.7, 42.0)])
ITALY_1878 = g78('Italy')
# the Principality of Serbia, autonomous from 1830 (its 1833 lands, before Nis and Pirot were added in 1878)
SERBIA_1833 = g78('Serbia').intersection(Polygon([(18, 46), (18, 43.5), (20.3, 43.2), (21.0, 43.15), (21.5, 43.4), (21.85, 43.45),
                                                   (22.4, 43.9), (23.5, 44.2), (23.5, 46)]))
# the United Principalities (1859) without northern Dobruja, Romanian only from 1878
DOBRUJA = Polygon([(27.9, 45.0), (28.2, 45.5), (29.8, 45.4), (30.0, 43.5), (27.5, 43.5)])
ROMANIA_1859 = g78('Romania').difference(DOBRUJA)


def europe_1815(m, y):
    """the European changes of year y (1822 to 1861) on a map built from 1815"""
    if y < 1831:
        m.put('United Kingdom of the Netherlands', U(NL, BE).difference(m.get('Luxembourg')))
    else:
        m.put('Netherlands', NL.difference(m.get('Luxembourg'))); m.put('Belgium', BE.difference(m.get('Luxembourg')))
        m.put('Greece', GREECE_1832)
        m.put('Serbia', SERBIA_1833, sub='Ottoman Empire')
    if y >= 1861: m.put('Romania', ROMANIA_1859, sub='Ottoman Empire')
    if y >= 1846:   # French Algeria once Abd al-Qadir's state was broken (he surrendered in 1847)
        m.rename('Algiers', 'Algeria (FR)')
        for x in m.f:
            if x[0]['name'] == 'Algeria (FR)': x[0]['sub'] = 'France'
    if y >= 1861:
        venetia = m.get('Venetia')
        italy = ITALY_1878.difference(venetia).difference(LAZIO)
        # Savoy and Nice went to France in 1860
        m.put('France', U(m.get('France'), m.get('Kingdom of Sardinia').difference(ITALY_1878.buffer(0.05))))
        m.put('Italy', italy)
        m.put('Papal States', m.get('Papal States').intersection(LAZIO))
        for n in ('Kingdom of Sardinia', 'Kingdom of the Two Sicilies', 'Lombardy', 'Parma', 'Modena', 'Tuscany', 'Lucca', 'Massa',
                  'Pontremoli', 'Fivizzano'):
            m.drop(n)


# ---------- South Asia and southern Africa ----------
RAJ = g78('British Raj')
BURMA_ALL = RAJ.intersection(Polygon([(92.3, 5), (92.3, 20.7), (92.6, 21.5), (93.0, 22.5), (93.3, 23.5), (94.2, 24.0), (94.6, 25.5),
                                      (95.5, 27.0), (97.5, 28.3), (102, 28.3), (102, 5)])).buffer(0)
ARAKAN = BURMA_ALL.intersection(Polygon([(92.0, 15.8), (92.0, 21.5), (93.0, 22.6), (94.2, 21.0), (94.6, 19.0), (94.8, 17.0), (94.3, 15.8)]))
TENASSERIM = BURMA_ALL.intersection(box(97.3, 5, 100.5, 16.6))
PEGU = BURMA_ALL.intersection(box(94.0, 15.0, 97.6, 19.4)).difference(ARAKAN)          # Lower Burma, British from 1852
UPPER_BURMA = BURMA_ALL.difference(U(ARAKAN, TENASSERIM, PEGU))                      # British only from 1885
SUBCONTINENT = RAJ.difference(BURMA_ALL)
SIKH = SUBCONTINENT.intersection(Polygon([(70.0, 33.5), (71.1, 34.6), (72.5, 35.2), (74.5, 36.2), (76.5, 35.8), (78.0, 35.3), (79.3, 34.2),
                                          (78.7, 32.5), (77.6, 32.2), (76.5, 31.1), (75.85, 30.95), (74.6, 30.95), (73.5, 30.0), (72.3, 29.6),
                                          (71.0, 29.3), (70.3, 28.9), (69.6, 30.0), (69.3, 31.5), (69.9, 32.6)]))
SINDH = SUBCONTINENT.intersection(Polygon([(66.6, 25.3), (67.0, 24.0), (68.5, 23.6), (70.6, 24.3), (71.1, 25.0), (70.6, 27.9), (69.6, 28.6),
                                           (68.0, 28.5), (67.5, 27.8), (66.7, 26.5)]))
KALAT = SUBCONTINENT.intersection(Polygon([(60, 24), (66.6, 25.3), (66.7, 26.5), (67.5, 27.8), (68.0, 28.5), (69.6, 28.6), (70.3, 28.9),
                                           (69.6, 30.0), (69.3, 31.5), (69.9, 32.6), (70.0, 33.5), (60, 33.5)])).difference(U(SIKH, SINDH))


def south_asia(m, y):
    """India and Burma in year y: the 1815 map still has the Maratha Confederacy, broken in 1818, and 1878 all of Burma"""
    m.drop('Maratha Confederacy', 'British East India Company', 'Mysore (Indian princely state)', 'Travancore', 'Assam', 'Arakan',
           'Burma', 'British Raj')
    oudh = m.get('Oudh')
    company = SUBCONTINENT.difference(KALAT)
    if y < 1849: company = company.difference(SIKH)
    if y < 1843: company = company.difference(SINDH)
    burma = UPPER_BURMA
    if y < 1854: burma = U(burma, PEGU)
    if y < 1826: burma = U(burma, ARAKAN, TENASSERIM, M15.get('Assam').intersection(SUBCONTINENT))   # Assam, Burmese 1817-1826
    else: company = U(company, ARAKAN, TENASSERIM)
    if y >= 1854: company = U(company, PEGU)
    if y < 1826: company = company.difference(M15.get('Assam'))
    if y < 1858:
        m.put('British East India Company', company, sub='United Kingdom of Great Britain and Ireland')
        if oudh is not None and y < 1856: m.put('Oudh', oudh)
        else: m.drop('Oudh')
    else:
        m.drop('Oudh')
        m.put('British Raj', company, sub='United Kingdom of Great Britain and Ireland')
    m.put('Burma', burma)
    if y < 1849: m.put('Sikh Empire', SIKH)
    if y < 1843: m.put('Sindh', SINDH)
    m.put('Khanate of Kalat', KALAT)


def southern_africa(m, y):
    """the Great Trek's republics and British Natal"""
    if y >= 1843: m.put('Natal', g78('Natal'), sub='United Kingdom of Great Britain and Ireland')
    if y >= 1852: m.put('Transvaal', g78('Transvaal'))
    if y >= 1854: m.put('Orange Free State', g78('Orange Free State'))


SOUTH_GERMANY = ['Bavaria', 'Württemberg', 'Baden']


def europe_1878(m, y):
    """1867 and 1871 from the 1878 map: undo the Treaty of Berlin and, for 1867, German and Italian unity"""
    ott = m.get('Ottoman Empire')
    m.put('Ottoman Empire', U(ott, m.get('Bulgaria'), m.get('Bosnia-Herzegovina')))
    m.drop('Bulgaria', 'Bosnia-Herzegovina')
    # 1878's Greece already has Thessaly and Arta (1881): before that, the 1832 line and the Ionian Islands (1864)
    greece = U(GREECE_1832, IONIAN_ISLANDS)
    m.put('Ottoman Empire', U(m.get('Ottoman Empire'), m.get('Greece').difference(greece)))
    m.put('Greece', greece)
    m.put('Ottoman Empire', U(m.get('Ottoman Empire'), m.get('Romania').intersection(DOBRUJA)))
    m.put('Romania', ROMANIA_1859)
    m.put('Ottoman Empire', U(m.get('Ottoman Empire'), m.get('Serbia').difference(SERBIA_1833)))
    m.put('Serbia', SERBIA_1833)
    if y < 1870:
        germany = m.get('Germany')
        alsace = germany.intersection(M15.get('France')).buffer(0)
        alsace = U(*[p for p in getattr(alsace, 'geoms', [alsace]) if p.area > 0.3])
        m.put('France', U(m.get('France'), alsace))
        south = {n: M15.get(n).intersection(germany) for n in SOUTH_GERMANY}
        m.put('North German Confederation', germany.difference(U(alsace, *south.values())))
        m.drop('Germany')
        for n, g in south.items(): m.put(n, g)
        m.put('Papal States', ITALY_1878.intersection(LAZIO))
        m.put('Italy', ITALY_1878.difference(LAZIO))


# ---------- fixes to the source years after 1871 ----------
# The War of the Pacific (1879-1884): Chile took Bolivia's coast and Peru's Tarapaca, and held Tacna and Arica;
# Bolivia's Puna de Atacama went to Argentina in 1899. West of this line is Chile's.
CHILE_NORTH = Polygon([(-72, -17.0), (-69.5, -17.5), (-68.8, -19.0), (-68.5, -20.0), (-68.2, -21.3), (-67.9, -22.2), (-67.2, -22.8),
                       (-67.5, -23.8), (-68.3, -24.5), (-68.4, -25.4), (-68.5, -27.5), (-72, -27.5)])


def fix_later():
    """1878 and 1880 call the Empire of Brazil a kingdom; 1900 calls the Brazilian republic one too, and still has
    Bolivia's coast and Peru's south as before the War of the Pacific"""
    for f in ('1878', '1880', '1900'):
        m = Map(load(f))
        if not m.has('Kingdom of Brazil'): continue   # put right on an earlier run
        m.rename('Kingdom of Brazil', 'Brazil' if f == '1900' else 'Empire of Brazil')
        if f == '1900':
            won = U(m.get('Bolivia').intersection(CHILE_NORTH), m.get('Peru').intersection(CHILE_NORTH))
            puna = m.get('Bolivia').difference(CHILE_NORTH).intersection(box(-70, -28, -64, -22.8))
            m.give('Chile', won)
            m.give('Argentina', puna)
        m.write(f, tol=0)


MID = [1822, 1823, 1825, 1831, 1836, 1840, 1846, 1848, 1854, 1861, 1867, 1871]
for y in MID:
    if y < 1867:
        m = Map(B1815); europe_1815(m, y); southern_africa(m, y)
    else:
        m = Map(B1878); europe_1878(m, y)
    south_asia(m, y)
    americas(m, y)
    m.write(str(y))
fix_later()

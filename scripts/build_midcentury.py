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
  1861  Italy (without Venetia and Rome); the United Principalities (Romania); Argentina; the Confederate States
  1865  as 1861, after the Civil War
  1867  base 1878: Alaska to the United States, North German Confederation, Italy without Rome, United States of Colombia
  1871  base 1878: German Empire and Italy with Rome, before the Treaty of Berlin (Bulgaria, Bosnia still Ottoman)

Outside the Americas and Europe the years from the 1815 base also get: Russia's Caucasus north of the Aras (Erivan from
1828) and Bessarabia, which the source leaves to Persia and the Ottomans; the Amur and Ussuri as Qing land until 1858;
Russia's advance over the Kazakh steppe; Egypt's Sudan from 1822 and its Syria and Crete in the 1830s; the Australian
colonies as they were founded; Wallachia and Moldavia; Kraków to Austria (1846); Montenegro; Liberia; and Hong Kong as
Chinese until 1842. 1867 and 1871 get back Khiva and Kokand, which the 1878 file has inside Russia.

It also corrects later source years: 1878 and 1880 name the Empire of Brazil a kingdom and 1900 the republic; 1900 draws
South America as before the War of the Pacific; 1878 to 1914 give the Caucasus to Persia, Shirak and (from 1878) Kars to
the Ottomans and Bessarabia to Romania; 1878 gives Greece Thessaly three years early and Britain Upper Burma seven; and
1914 draws the Caucasus republics of 1918.

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
# The source's Romania (1878 on) also takes in Bessarabia east of the Prut, Russian from 1812 to 1918; only its south
# (Cahul, Bolgrad, Izmail) was Moldavia's and then Romania's, from 1856 to 1878
BESSARABIA = Polygon([(26.6, 48.5), (26.8, 48.27), (27.25, 47.85), (27.8, 47.21), (28.05, 46.9), (28.2, 46.48), (28.15, 45.9), (28.2, 45.4),
                      (29.0, 45.15), (29.75, 45.15), (31.0, 46.0), (31.0, 48.6)])
SOUTH_BESSARABIA = U(M15.get('Russian Empire'), M15.get('Ottoman Empire')).intersection(BESSARABIA).intersection(box(28, 45.0, 30.0, 46.05))
ROMANIA_1859 = g78('Romania').difference(DOBRUJA).difference(BESSARABIA)


def europe_1815(m, y):
    """the European changes of year y (1822 to 1861) on a map built from 1815"""
    if y < 1831:
        m.put('United Kingdom of the Netherlands', U(NL, BE).difference(m.get('Luxembourg')))
    else:
        m.put('Netherlands', NL.difference(m.get('Luxembourg'))); m.put('Belgium', BE.difference(m.get('Luxembourg')))
        m.put('Greece', GREECE_1832)
        m.put('Serbia', SERBIA_1833, sub='Ottoman Empire')
    if y >= 1861: m.put('Romania', U(ROMANIA_1859, SOUTH_BESSARABIA), sub='Ottoman Empire')
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
RAJ = U(g78('British Raj'), g78('Burma'))   # Burma: 1878 is given back Upper Burma below
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
    m.give('Russian Empire', m.get('Romania').intersection(BESSARABIA))
    m.put('Romania', U(ROMANIA_1859, SOUTH_BESSARABIA))
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


# ---------- the rest of the world ----------
# The Caucasus: the source files from 1815 to 1900 leave Georgia, Shirvan and Baku to Persia, though Russia had Georgia
# from 1801 and the khanates north of the Aras from the Treaty of Gulistan (1813); Erivan and Nakhichevan followed at
# Turkmenchay (1828). Russia's part is what Persia is drawn with north of the Aras and of the Astara line.
TRANSCAUCASIA = Polygon([(42.0, 40.0), (43.0, 39.9), (44.3, 39.72), (44.8, 39.65), (45.1, 39.4), (45.5, 39.0), (46.0, 38.9), (46.55, 38.87),
                         (47.0, 39.2), (47.6, 39.4), (48.0, 39.65), (48.35, 39.4), (48.1, 39.0), (48.3, 38.6), (48.87, 38.43), (51, 38.43),
                         (51, 47), (40, 47), (40, 41.0)])
ERIVAN = Polygon([(43.9, 40.05), (44.1, 40.9), (44.9, 41.05), (45.6, 40.65), (46.1, 39.9), (46.6, 39.2), (45.9, 38.85), (45.0, 39.3),
                  (44.3, 39.4)])
KARS = Polygon([(41.5, 41.52), (41.6, 41.2), (41.85, 40.9), (41.8, 40.6), (42.3, 40.3), (42.8, 40.15), (43.65, 40.1), (43.65, 40.5),
               (43.6, 40.9), (43.45, 41.4), (42.5, 41.6)])   # Kars and Ardahan: east to the Akhurian
# Shirak (Gyumri), Russian from 1805, which the source gives to the Ottomans until 1914
SHIRAK = Polygon([(43.65, 40.1), (44.4, 39.9), (44.6, 41.2), (43.45, 41.4), (43.6, 40.9), (43.65, 40.5)])
BATUMI = box(41.3, 41.25, 42.6, 41.9)   # Ottoman Adjara until 1878


def shirak(m):
    piece = m.get('Ottoman Empire').intersection(SHIRAK)
    if piece.area > 0.01: m.give('Russian Empire', piece)


def caucasus(m, y):
    shirak(m)
    persia = m.get('Persia')
    if persia is None: return
    piece = persia.intersection(TRANSCAUCASIA)
    if y < 1828: piece = piece.difference(ERIVAN)
    if piece.area > 0.01: m.give('Russian Empire', piece)
    if y < 1878:   # Adjara, Kars and Ardahan were Ottoman until 1878
        held = m.get('Russian Empire').intersection(U(BATUMI, KARS))
        if held.area > 0.01: m.give('Ottoman Empire', held)


# The Amur and the Ussuri: the source draws Outer Manchuria as Russian already in 1815; it was Qing until the
# treaties of Aigun (1858) and Peking (1860). Everything Russian south of the Stanovoy range and east of the Argun.
OUTER_MANCHURIA = Polygon([(121.0, 53.4), (124.0, 54.3), (127.0, 55.3), (131.0, 55.3), (135.0, 54.9), (137.5, 55.0), (141.0, 53.5),
                           (141.45, 52.2), (140.6, 48.0), (139.0, 45.0), (136.0, 43.0), (131.0, 42.3), (130.0, 42.0), (121.0, 49.0)])

# The Kazakh steppe (the source's "central Asian khanates" in 1815) passed to Russia from the north: the Middle and
# Little Hordes lost their khans in 1822 and 1824, Kenesary's revolt was put down in 1847, and Verny was founded in the
# Senior Horde's land in 1854, the year after Russia took Ak-Mechet on the Syr Darya. Qing Dzungaria to the east stays.
STEPPE_WEST = box(40, 30, 80.5, 60)


def steppe(m, y):
    """the source's Turan reaches far into the steppe north of the khanates too: the same lines cut both"""
    if y < 1831: return
    line = 48.5 if y < 1846 else 45.5 if y < 1854 else 0
    north = box(40, line, 100, 60)
    if y >= 1854: north = U(box(40, 44.3, 67.5, 60), box(67.5, 45.0, 100, 60))   # Kokand kept the middle Syr Darya until 1864
    for n in ('central Asian khanates', 'Turan'):
        piece = m.get(n).intersection(STEPPE_WEST).intersection(north if n == 'Turan' or y < 1854 else STEPPE_WEST)
        if piece.area > 0.01: m.give('Russian Empire', piece)
    if y >= 1854 and m.has('central Asian khanates'):   # what is left is Qing Tarbagatai
        m.give('Manchu Empire', m.get('central Asian khanates')); m.drop('central Asian khanates')


# Khiva and Kokand in 1867 and 1871, which the 1878 file has inside Russia (Khiva a protectorate from 1873, Kokand
# annexed in 1876); Bukhara still had Samarkand until 1868
TURAN = M15.get('Turan')
KHIVA = TURAN.intersection(box(55.5, 39.0, 62.0, 45.0)).difference(g78('Bokhara Khanate'))
KOKAND = TURAN.intersection(Polygon([(70.0, 40.3), (70.5, 41.2), (71.6, 41.7), (73.4, 41.9), (75.2, 41.1), (73.8, 39.4), (71.0, 39.3),
                                     (70.0, 39.8)]))
SAMARKAND = box(66.0, 39.25, 68.2, 40.15)


def central_asia_1878(m, y):
    m.put('Khiva Khanate', KHIVA)
    m.put('Khanate of Kokand', KOKAND)
    if y < 1868:
        m.give('Bokhara Khanate', m.get('Russian Empire').intersection(SAMARKAND))


# Egypt: Muhammad Ali conquered the Nile Sudan (Sennar, Kordofan) in 1820-1822, and held Syria, Adana and Crete from
# 1831 to 1840; Darfur (1874) and Equatoria came later
SUDAN = g78('Egypt').difference(box(-20, -20, 27, 16)).difference(box(-20, -20, 60, 9.0)).difference(box(20, 21.9, 40, 33))
LEVANT = Polygon([(32.0, 31.4), (34.25, 31.25), (34.95, 29.5), (37.0, 30.5), (38.8, 33.0), (40.3, 35.6), (38.6, 36.85), (36.9, 37.45),
                  (35.3, 37.6), (34.2, 37.0), (34.75, 36.0), (34.0, 33.0)])   # Cyprus stayed Ottoman
CRETE = box(23.4, 34.7, 26.5, 35.75)


def egypt(m, y):
    m.put('Egypt', U(m.get('Egypt'), SUDAN))
    if 1831 <= y < 1840:
        m.give('Egypt', U(m.get('Ottoman Empire').intersection(LEVANT), m.get('Ottoman Empire').intersection(CRETE)))


# Australia: the 1815 file has only New South Wales and the Aboriginal nations. Western Australia (1829), South
# Australia (1836), Victoria (1851) and Queensland (1859) take 1878's lines; the Northern Territory was New South
# Wales's until South Australia took it in 1863.
AUS = {n: g78(n) for n in ('Western Australia (UK)', 'South Australia (UK)', 'Victoria (UK)', 'Queensland (UK)',
                           'New South Wales (UK)', 'Northern Territory (UK)')}
AUS_FROM = {'Western Australia (UK)': 1831, 'South Australia (UK)': 1836, 'Victoria (UK)': 1854, 'Queensland (UK)': 1861}


def australia(m, y):
    if y < 1831: return
    nsw = U(m.get('New South Wales'), AUS['New South Wales (UK)'], AUS['Northern Territory (UK)'])
    for n, since in AUS_FROM.items():
        if y >= since: m.put(n, AUS[n], sub='United Kingdom of Great Britain and Ireland')
        else: nsw = U(nsw, AUS[n])
    for n in AUS_FROM:
        if m.has(n): nsw = nsw.difference(m.get(n))
    m.put('New South Wales', nsw, sub='United Kingdom of Great Britain and Ireland')


# The Danube principalities, Ottoman vassals the source draws as plain Ottoman land: autonomous under Russian protection
# after the Treaty of Adrianople (1829), until their union in 1859. The Milcov line between them.
WALLACHIA_SIDE = Polygon([(20, 40), (31, 40), (31, 45.25), (28.05, 45.45), (27.25, 45.68), (26.6, 45.85), (26.1, 45.95), (25.7, 45.7),
                          (20, 45.7)])


def europe_rest(m, y):
    # Bessarabia, Russian from 1812 (the 1815 file leaves it Ottoman); its south was Moldavia's from 1856
    bess = m.get('Ottoman Empire').intersection(BESSARABIA)
    if y >= 1856: bess = bess.difference(SOUTH_BESSARABIA)
    if bess.area > 0.01: m.give('Russian Empire', bess)
    if 1831 <= y < 1861:
        m.put('Principality of Wallachia', ROMANIA_1859.intersection(WALLACHIA_SIDE), sub='Ottoman Empire')
        m.put('Moldavia', U(ROMANIA_1859.difference(WALLACHIA_SIDE), SOUTH_BESSARABIA if y >= 1856 else None), sub='Ottoman Empire')
    if y >= 1848 and m.has('Republic of Kraków'):   # annexed by Austria in November 1846
        m.give('Austrian Empire', m.get('Republic of Kraków')); m.drop('Republic of Kraków')
    if y >= 1854:   # Danilo made the prince-bishopric a secular principality in 1852
        m.put('Montenegro', g78('Montenegro'))


def africa_asia_rest(m, y):
    if y >= 1848: m.put('Liberia', g78('Liberia'))   # independent in 1847
    if y < 1842 and m.has('Hong Kong'):              # British from the Treaty of Nanking (1842)
        m.give('Manchu Empire', m.get('Hong Kong')); m.drop('Hong Kong')
    if y < 1858:
        m.give('Manchu Empire', m.get('Russian Empire').intersection(OUTER_MANCHURIA))


# The Confederate States of America (1861-1865): the eleven seceding states, without West Virginia, Kentucky and Missouri
CSA_AREA = Polygon([(-106.62, 32.0), (-103.06, 32.0), (-103.04, 36.5), (-100.0, 36.5), (-100.0, 34.56), (-99.5, 34.4), (-99.0, 34.2),
                    (-98.5, 34.1), (-97.5, 33.85), (-96.5, 33.8), (-95.5, 33.88), (-94.9, 33.8), (-94.48, 33.64), (-94.45, 35.38),
                    (-94.62, 36.5), (-90.15, 36.5), (-90.08, 36.3), (-90.37, 36.0), (-89.71, 36.0), (-89.53, 36.5), (-88.05, 36.5),
                    (-88.07, 36.68), (-87.85, 36.63), (-86.0, 36.63), (-83.68, 36.6), (-83.1, 36.75), (-82.4, 37.25), (-81.97, 37.54),
                    (-81.2, 37.26), (-80.85, 37.33), (-80.3, 37.5), (-80.0, 37.8), (-79.65, 38.4), (-79.3, 38.45), (-79.0, 38.8),
                    (-78.4, 39.2), (-77.8, 39.32), (-77.5, 39.2), (-77.25, 39.0), (-77.05, 38.85), (-77.2, 38.4), (-76.9, 38.2),
                    (-76.25, 37.9), (-76.1, 37.0), (-75.5, 36.5), (-74.0, 35.0), (-79.0, 24.0), (-81.0, 23.5), (-98.0, 24.0),
                    (-104.0, 26.0), (-108.0, 29.0)])


def confederacy(m, y):
    if 1861 <= y < 1865:
        csa = m.get('United States').intersection(CSA_AREA)
        m.put('Confederate States of America', csa)


# ---------- fixes to the source years after 1871 ----------
# The War of the Pacific (1879-1884): Chile took Bolivia's coast and Peru's Tarapaca, and held Tacna and Arica;
# Bolivia's Puna de Atacama went to Argentina in 1899. West of this line is Chile's.
CHILE_NORTH = Polygon([(-72, -17.0), (-69.5, -17.5), (-68.8, -19.0), (-68.5, -20.0), (-68.2, -21.3), (-67.9, -22.2), (-67.2, -22.8),
                       (-67.5, -23.8), (-68.3, -24.5), (-68.4, -25.4), (-68.5, -27.5), (-72, -27.5)])


def fix_later():
    """1878 and 1880 call the Empire of Brazil a kingdom; 1900 calls the Brazilian republic one too, and still has
    Bolivia's coast and Peru's south as before the War of the Pacific. 1878 to 1900 give the Caucasus to Persia, and 1878
    has Greece with Thessaly (1881) and Britain with Upper Burma (1885). 1914 draws the Caucasus republics of 1918.
    Each fix is made only where it is still needed, so a second run changes nothing."""
    for f in ('1878', '1880', '1900', '1914'):
        m = Map(load(f)); before = [x[2] is None for x in m.f]
        if m.has('Kingdom of Brazil'):
            m.rename('Kingdom of Brazil', 'Brazil' if f == '1900' else 'Empire of Brazil')
            if f == '1900':
                won = U(m.get('Bolivia').intersection(CHILE_NORTH), m.get('Peru').intersection(CHILE_NORTH))
                puna = m.get('Bolivia').difference(CHILE_NORTH).intersection(box(-70, -28, -64, -22.8))
                m.give('Chile', won)
                m.give('Argentina', puna)
            for x in m.f: x[2] = None if x[0]['name'] in ('Empire of Brazil', 'Brazil') else x[2]
        if f != '1914' and m.has('Persia') and m.get('Persia').intersection(TRANSCAUCASIA).area > 0.05:
            caucasus(m, int(f))
        bess = m.get('Romania').intersection(BESSARABIA) if m.has('Romania') else Polygon()
        if bess.area > 0.05:
            m.give('Russian Empire', bess)
        shirak(m)
        kars = m.get('Ottoman Empire').intersection(KARS)
        if kars.area > 0.05:   # Kars, Ardahan and Batumi, Russian from the Treaty of Berlin (1878)
            m.give('Russian Empire', kars)
        if f == '1878':
            thessaly = m.get('Greece').difference(ARTA_VOLOS).difference(IONIAN_ISLANDS.buffer(0.05))
            if thessaly.area > 0.05:
                m.give('Ottoman Empire', thessaly)
            if not m.has('Burma'):
                m.put('Burma', UPPER_BURMA)
        if f == '1914' and m.has('Georgia'):
            m.give('Russian Empire', U(m.get('Georgia'), m.get('Armenia'), m.get('Azerbaijan')))
            m.drop('Georgia', 'Armenia', 'Azerbaijan')
        if any(x[2] is None for x in m.f) or len(m.f) != len(before):
            m.write(f, tol=0)


MID = [1822, 1823, 1825, 1831, 1836, 1840, 1846, 1848, 1854, 1861, 1865, 1867, 1871]
for y in MID:
    if y < 1867:
        m = Map(B1815); europe_1815(m, y); europe_rest(m, y); southern_africa(m, y)
        steppe(m, y); egypt(m, y); australia(m, y); africa_asia_rest(m, y)
    else:
        m = Map(B1878); europe_1878(m, y); central_asia_1878(m, y)
    caucasus(m, y)
    south_asia(m, y)
    americas(m, y)
    confederacy(m, y)
    m.write(str(y))
fix_later()

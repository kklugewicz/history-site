"""The cities on the map, each with the names it went by, how much it mattered in each age, and the landmark that stood for it.

C(id, lon, lat, (first, last), names, ranks, landmarks, now=None)
  years   the city shows from `first` to `last` (None: still standing)
  names   a name, or [(from year, name), ...]
  ranks   a rank, or [(from year, rank), ...]: 1 shows on the whole world, 2 once you zoom to a region, 3 closer in, 0 not at all
  lms     [(from year, icon, label), ...]: the icon (content/cities/icons.py) and what it shows; label None for a plain town
  now     the modern name, when the last name in `names` isn't it
Each value lasts until the next one starts. Years before Christ are negative.
"""

CITIES = []


def C(id, lon, lat, years, names, ranks, lms, now=None):
    CITIES.append(dict(id=id, lon=lon, lat=lat, years=years, names=names, ranks=ranks, lms=lms, now=now))


# ---------- the Mediterranean and Europe ----------
C('troy', 26.24, 39.96, (-3000, -1180), 'Troy', 3, [(-3000, 'walls', 'The walls of Troy')], now='Hisarlik')
C('knossos', 25.163, 35.298, (-1950, -1375), 'Knossos', 2, [(-1950, 'minoan', 'The palace of Knossos')])
C('mycenae', 22.756, 37.731, (-1600, -1100), 'Mycenae', 2, [(-1600, 'walls', None), (-1250, 'liongate', 'The Lion Gate, about 1250 BC')])
C('hattusa', 34.62, 40.02, (-1650, -1180), 'Hattusa', 2, [(-1650, 'liongate', 'The Lion Gate of Hattusa')], now='Boğazkale')
C('tyre', 35.20, 33.27, (-2750, None), 'Tyre', [(-2750, 3), (-1000, 2), (-332, 3)], [(-2750, 'ship', 'The twin harbours of Tyre')])
C('athens', 23.726, 37.972, (-1000, None), 'Athens', [(-1000, 3), (-550, 2), (-480, 1), (-322, 2), (200, 3), (1834, 2)],
  [(-1000, 'walls', None), (-525, 'temple', 'The Old Temple of Athena on the Acropolis'), (-438, 'parthenon', 'The Parthenon, finished in 438 BC')])
C('syracuse', 15.29, 37.07, (-734, None), 'Syracuse', [(-734, 3), (-480, 2), (-212, 3)], [(-734, 'temple', 'The Temple of Apollo')])
C('carthage', 10.323, 36.853, (-814, 698), 'Carthage', [(-814, 3), (-650, 2), (-300, 1), (-146, 0), (-29, 2), (533, 3)],
  [(-814, 'ship', 'The great harbours of Carthage'), (-29, 'temple', 'Roman Carthage, refounded by Augustus')])
C('rome', 12.484, 41.893, (-753, None), 'Rome', [(-753, 3), (-338, 2), (-146, 1), (410, 2)],
  [(-753, 'walls', None), (-509, 'temple', 'The Temple of Jupiter on the Capitoline, 509 BC'), (80, 'colosseum', 'The Colosseum, opened in 80')])
C('alexandria', 29.92, 31.20, (-331, None), 'Alexandria', [(-331, 2), (-300, 1), (400, 2), (900, 3), (1850, 2)],
  [(-331, 'walls', None), (-280, 'pharos', 'The Lighthouse of Alexandria, about 280 BC'), (1323, 'walls', None),
   (1477, 'castle', 'The Citadel of Qaitbay, built in 1477 from the fallen lighthouse')])
C('byzantium', 28.98, 41.01, (-667, None), [(-667, 'Byzantium'), (330, 'Constantinople'), (1930, 'Istanbul')], [(-667, 3), (330, 1), (1923, 2)],
  [(-667, 'walls', None), (537, 'hagia', 'Hagia Sophia, finished in 537'), (1453, 'hagia_m', 'Hagia Sophia, a mosque from 1453')])
C('ravenna', 12.20, 44.42, (402, 1000), 'Ravenna', [(402, 2), (751, 3)], [(402, 'walls', None), (547, 'palatine', 'The Basilica of San Vitale, 547')])
C('naples', 14.25, 40.85, (-600, None), [(-600, 'Neapolis'), (600, 'Naples')], [(-600, 3), (1282, 2), (1861, 3)],
  [(-600, 'walls', None), (1279, 'castle', 'Castel Nuovo, 1279')])
C('venice', 12.336, 45.437, (697, None), 'Venice', [(697, 3), (1000, 2), (1204, 1), (1453, 2), (1797, 3)],
  [(697, 'town', None), (1173, 'campanile', "St Mark's Basilica and the Campanile")])
C('florence', 11.256, 43.773, (-59, None), [(-59, 'Florentia'), (500, 'Florence')], [(-59, 3), (1250, 2), (1569, 3)],
  [(-59, 'walls', None), (900, 'town', None), (1436, 'duomo', 'The Duomo, its dome finished in 1436')])
C('toledo', -4.02, 39.86, (560, None), 'Toledo', [(560, 2), (711, 3), (1085, 2), (1561, 3)], [(560, 'walls', None), (1085, 'castle', 'The Alcázar of Toledo')])
C('cordoba', -4.78, 37.88, (-169, None), [(-169, 'Corduba'), (711, 'Qurtuba'), (1236, 'Córdoba')], [(-169, 3), (756, 2), (929, 1), (1031, 2), (1236, 3)],
  [(-169, 'walls', None), (785, 'mezquita', 'The Great Mosque, begun in 785')])
C('seville', -5.99, 37.39, (-206, None), [(-206, 'Hispalis'), (712, 'Ishbiliya'), (1248, 'Seville')], [(-206, 3), (1503, 2), (1717, 3)],
  [(-206, 'walls', None), (1198, 'sqminaret', 'The Giralda, built as a minaret in 1198')])
C('granada', -3.59, 37.18, (1013, None), 'Granada', [(1013, 3), (1238, 2), (1492, 3)], [(1013, 'walls', None), (1238, 'alhambra', 'The Alhambra, from 1238')])
C('lisbon', -9.14, 38.71, (-138, None), [(-138, 'Olisipo'), (714, 'al-Ushbuna'), (1147, 'Lisbon')], [(-138, 3), (1255, 2), (1500, 1), (1580, 2)],
  [(-138, 'walls', None), (1147, 'castle', 'São Jorge Castle'), (1520, 'belem', 'The Belém Tower, 1520')])
C('madrid', -3.70, 40.42, (1561, None), 'Madrid', 2, [(1561, 'castle', 'The Royal Alcázar'), (1764, 'palace', 'The Royal Palace, 1764')])
C('paris', 2.35, 48.853, (-250, None), [(-250, 'Lutetia'), (360, 'Paris')], [(-250, 3), (508, 2), (1600, 1)],
  [(-250, 'walls', None), (500, 'town', None), (1250, 'notredame', 'Notre-Dame de Paris, finished about 1260'), (1889, 'eiffel', 'The Eiffel Tower, 1889')])
C('aachen', 6.08, 50.775, (790, 1531), 'Aachen', [(790, 2), (814, 3)], [(790, 'palatine', "Charlemagne's Palatine Chapel, consecrated in 805")])
C('london', -0.10, 51.51, (47, None), [(47, 'Londinium'), (600, 'London')], [(47, 3), (1066, 2), (1700, 1)],
  [(47, 'walls', None), (600, 'town', None), (1100, 'towerlondon', 'The Tower of London, about 1100'),
   (1859, 'bigben', 'Big Ben and the Houses of Parliament, 1859')])
C('edinburgh', -3.19, 55.95, (600, None), 'Edinburgh', [(600, 3), (1437, 2), (1707, 3)], [(600, 'castle', 'Edinburgh Castle')])
C('amsterdam', 4.90, 52.37, (1275, None), 'Amsterdam', [(1275, 3), (1585, 2), (1600, 1), (1700, 2)],
  [(1275, 'town', None), (1615, 'canalhouses', 'The canal houses of the Golden Age')])
C('copenhagen', 12.57, 55.68, (1167, None), 'Copenhagen', [(1167, 3), (1443, 2)], [(1167, 'castle', "Bishop Absalon's castle"), (1745, 'palace', 'Christiansborg Palace')])
C('stockholm', 18.07, 59.33, (1252, None), 'Stockholm', [(1252, 3), (1523, 2)], [(1252, 'spire', 'Riddarholmen Church')])
C('vienna', 16.37, 48.21, (-15, None), [(-15, 'Vindobona'), (881, 'Vienna')], [(-15, 3), (1438, 2)],
  [(-15, 'walls', None), (881, 'town', None), (1433, 'ststephen', "St. Stephen's Cathedral, its south tower finished in 1433")])
C('prague', 14.40, 50.09, (880, None), 'Prague', [(880, 3), (1346, 2), (1420, 3)], [(880, 'castlecathedral', 'Prague Castle and St. Vitus Cathedral')])
C('krakow', 19.94, 50.06, (1000, None), 'Kraków', [(1000, 3), (1038, 2), (1596, 3)], [(1000, 'castlecathedral', 'Wawel Castle and Cathedral')])
C('warsaw', 21.01, 52.23, (1300, None), 'Warsaw', [(1300, 3), (1596, 2)], [(1300, 'castle', 'The Royal Castle')])
C('budapest', 19.04, 47.50, (1000, None), [(1000, 'Buda'), (1873, 'Budapest')], [(1000, 3), (1361, 2), (1541, 3), (1873, 2)], [(1000, 'castle', 'Buda Castle')])
C('berlin', 13.40, 52.52, (1237, None), 'Berlin', [(1237, 3), (1701, 2), (1871, 1), (1945, 2)],
  [(1237, 'town', None), (1451, 'palace', 'The Berlin Palace'), (1791, 'brandenburg', 'The Brandenburg Gate, 1791')])
C('kyiv', 30.52, 50.45, (482, None), 'Kyiv', [(482, 3), (882, 2), (1240, 3), (1991, 2)],
  [(482, 'walls', None), (1037, 'kyivdomes', 'Saint Sophia Cathedral, founded in 1037')])
C('moscow', 37.62, 55.75, (1147, None), 'Moscow', [(1147, 3), (1480, 2), (1918, 1)],
  [(1147, 'town', None), (1495, 'kremlin', 'The Kremlin, its walls rebuilt 1485–1495'), (1561, 'stbasil', "St. Basil's Cathedral, 1561"),
   (1935, 'kremlin', 'The Kremlin, its towers topped with red stars from 1935'), (1991, 'stbasil', "St. Basil's Cathedral, 1561")])
C('stpetersburg', 30.32, 59.94, (1703, None), [(1703, 'Saint Petersburg'), (1914, 'Petrograd'), (1924, 'Leningrad'), (1991, 'Saint Petersburg')],
  [(1703, 2), (1712, 1), (1918, 2)], [(1703, 'spire', 'The Peter and Paul Fortress and Cathedral')])

# ---------- Africa ----------
C('memphis', 31.255, 29.845, (-3100, 641), 'Memphis', [(-3100, 1), (-2100, 2), (-331, 3)],
  [(-3100, 'walls', 'Ineb-hedj, the White Walls'), (-2560, 'pyramids', 'The pyramids of Giza, about 2560 BC')])
C('thebes', 32.64, 25.70, (-2100, -27), 'Thebes', [(-2100, 2), (-1550, 1), (-1070, 2), (-663, 3)], [(-2100, 'pylon', 'The temples of Karnak')], now='Luxor')
C('meroe', 33.75, 16.94, (-590, 350), 'Meroë', 2, [(-590, 'nubian', 'The pyramids of Meroë')])
C('axum', 38.72, 14.13, (-100, None), 'Aksum', [(-100, 3), (100, 2), (940, 3)], [(-100, 'walls', None), (300, 'stele', 'The steles of Aksum, about 300')])
C('cairo', 31.25, 30.04, (641, None), [(641, 'Fustat'), (969, 'Cairo')], [(641, 2), (1250, 1), (1517, 2)],
  [(641, 'mosque', 'The Mosque of Amr ibn al-As, 641'), (972, 'mosque', 'Al-Azhar Mosque, 972'),
   (1848, 'alimosque', 'The Mosque of Muhammad Ali on the Citadel, 1848')])
C('kairouan', 10.10, 35.68, (670, None), 'Kairouan', [(670, 2), (909, 3)], [(670, 'sqminaret', 'The Great Mosque of Kairouan')])
C('marrakesh', -7.99, 31.63, (1070, None), 'Marrakesh', [(1070, 2), (1269, 3), (1554, 2), (1669, 3)],
  [(1070, 'walls', None), (1158, 'sqminaret', 'The Koutoubia Mosque, 1158')])
C('timbuktu', -3.0, 16.77, (1327, None), 'Timbuktu', [(1327, 2), (1591, 3)], [(1327, 'mudmosque', 'The Djinguereber Mosque, 1327')])
C('gao', 0.03, 16.27, (800, None), 'Gao', [(800, 3), (1430, 2), (1591, 3)], [(800, 'walls', None), (1495, 'mudmosque', 'The Tomb of Askia, 1495')])
C('benin', 5.62, 6.34, (1180, None), 'Benin City', [(1180, 3), (1440, 2), (1897, 3)], [(1180, 'walls', 'The walls and moats of Benin City')])
C('zimbabwe', 30.93, -20.27, (1100, 1450), 'Great Zimbabwe', 2, [(1100, 'zimbabwe', 'The Great Enclosure and its conical tower')])
C('kilwa', 39.51, -8.96, (1000, 1600), 'Kilwa', 2, [(1000, 'domesrow', 'The Great Mosque of Kilwa')])
C('capetown', 18.42, -33.92, (1652, None), 'Cape Town', [(1652, 3), (1910, 2)], [(1652, 'tablemtn', 'Table Mountain')])
C('johannesburg', 28.05, -26.20, (1886, None), 'Johannesburg', [(1886, 3), (1930, 2)], [(1886, 'headframe', 'The gold-mine headframes of the Witwatersrand')])

# ---------- the Middle East and Central Asia ----------
C('uruk', 45.64, 31.32, (-4000, 100), 'Uruk', [(-4000, 1), (-2900, 2), (-2000, 3)], [(-4000, 'ziggurat', 'The temples of Uruk on their high terraces')])
C('ur', 46.10, 30.96, (-3800, -500), 'Ur', [(-3800, 3), (-2600, 2), (-2112, 1), (-2004, 2), (-1700, 3)],
  [(-3800, 'walls', None), (-2100, 'ziggurat', 'The Great Ziggurat of Ur, about 2100 BC')])
C('babylon', 44.42, 32.54, (-2300, 100), 'Babylon', [(-2300, 3), (-1894, 2), (-1792, 1), (-1595, 2), (-626, 1), (-331, 2), (-275, 3)],
  [(-2300, 'walls', None), (-1800, 'ziggurat', 'Etemenanki, the ziggurat of Marduk'), (-575, 'ishtar', 'The Ishtar Gate, about 575 BC')])
C('nineveh', 43.15, 36.36, (-1000, -612), 'Nineveh', [(-1000, 3), (-705, 1)],
  [(-1000, 'walls', None), (-705, 'lamassu', "Sennacherib's palace and its winged bulls")], now='Mosul')
C('jerusalem', 35.235, 31.778, (-1000, None), 'Jerusalem', 2,
  [(-1000, 'walls', None), (-957, 'temple_jer', "Solomon's Temple"), (-587, 'walls', None), (-516, 'temple_jer', 'The Second Temple, rebuilt by Herod'),
   (70, 'walls', None), (691, 'domerock', 'The Dome of the Rock, 691')])
C('damascus', 36.31, 33.51, (-1000, None), 'Damascus', [(-1000, 3), (661, 1), (750, 2)], [(-1000, 'walls', None), (715, 'mosque', 'The Umayyad Mosque, 715')])
C('petra', 35.444, 30.329, (-312, 663), 'Petra', [(-312, 3), (-100, 2), (106, 3)], [(-312, 'walls', None), (-50, 'treasury', 'Al-Khazneh, the Treasury, carved in the 1st century')])
C('persepolis', 52.89, 29.935, (-518, -330), 'Persepolis', 1, [(-518, 'persepolis', 'The Apadana of Persepolis')])
C('ctesiphon', 44.58, 33.09, (-120, 637), 'Ctesiphon', [(-120, 2), (226, 1)], [(-120, 'walls', None), (540, 'ctesiphon', 'Taq Kasra, the great arch, about 540')])
C('mecca', 39.826, 21.4225, (400, None), 'Mecca', [(400, 3), (630, 2)], [(400, 'kaaba', 'The Kaaba')])
C('baghdad', 44.38, 33.31, (762, None), 'Baghdad', [(762, 1), (1258, 3), (1921, 2)],
  [(762, 'roundcity', 'The Round City of al-Mansur, 762–766'), (1258, 'mosque', None)])
C('isfahan', 51.67, 32.66, (900, None), 'Isfahan', [(900, 3), (1051, 2), (1200, 3), (1598, 1), (1722, 3)],
  [(900, 'mosque', 'The Jameh Mosque of Isfahan'), (1629, 'iwan', 'The Shah Mosque on Naqsh-e Jahan Square, 1629')])
C('tehran', 51.39, 35.69, (1786, None), 'Tehran', 2, [(1786, 'mosque', None), (1971, 'azadi', 'The Azadi Tower, 1971')])
C('bukhara', 64.42, 39.77, (-500, None), 'Bukhara', [(-500, 3), (892, 2), (999, 3), (1500, 2), (1920, 3)],
  [(-500, 'walls', None), (1127, 'qutub', 'The Kalyan Minaret, 1127')])
C('samarkand', 66.975, 39.655, (-700, None), [(-700, 'Maracanda'), (712, 'Samarkand')], [(-700, 3), (1370, 1), (1449, 2), (1507, 3)],
  [(-700, 'walls', None), (712, 'mosque', None), (1420, 'registan', 'The Registan, from 1420')])
C('dubai', 55.27, 25.20, (2010, None), 'Dubai', 2, [(2010, 'burj', 'The Burj Khalifa, 2010')])

# ---------- South Asia ----------
C('mohenjodaro', 68.14, 27.33, (-2500, -1900), 'Mohenjo-daro', 1, [(-2500, 'mohenjo', 'The citadel mound and its Great Bath')])
C('pataliputra', 85.14, 25.61, (-490, None), [(-490, 'Pataliputra'), (1541, 'Patna')], [(-490, 3), (-321, 1), (-185, 2), (550, 3)],
  [(-490, 'walls', None), (-250, 'ashoka', "Ashoka's lion pillars, about 250 BC"), (550, 'walls', None)])
C('anuradhapura', 80.40, 8.35, (-377, 1017), 'Anuradhapura', 2, [(-377, 'walls', None), (-140, 'stupa', 'The Ruwanwelisaya stupa, about 140 BC')])
C('delhi', 77.21, 28.61, (736, None), 'Delhi', [(736, 3), (1206, 1), (1526, 2), (1648, 1), (1857, 2), (1947, 1)],
  [(736, 'walls', None), (1220, 'qutub', 'The Qutb Minar, finished about 1220'), (1648, 'redfort', 'The Red Fort, 1648'), (1931, 'indiagate', 'India Gate, 1931')])
C('agra', 78.04, 27.175, (1504, None), 'Agra', [(1504, 3), (1526, 1), (1648, 2), (1803, 3)],
  [(1504, 'walls', None), (1573, 'redfort', 'Agra Fort, rebuilt 1565–1573'), (1653, 'taj', 'The Taj Mahal, 1653')])
C('vijayanagara', 76.46, 15.335, (1336, 1565), 'Vijayanagara', [(1336, 2), (1440, 1)], [(1336, 'gopuram', 'The gopuram of the Virupaksha Temple')], now='Hampi')
C('goa', 73.91, 15.50, (1510, None), 'Goa', [(1510, 2), (1760, 3)], [(1510, 'cathedral', 'The Basilica of Bom Jesus, 1605')])
C('bombay', 72.835, 18.94, (1661, None), [(1661, 'Bombay'), (1995, 'Mumbai')], [(1661, 3), (1850, 2)],
  [(1661, 'town', None), (1924, 'gatewayindia', 'The Gateway of India, 1924')])
C('calcutta', 88.36, 22.57, (1690, None), [(1690, 'Calcutta'), (2001, 'Kolkata')], [(1690, 3), (1772, 2)],
  [(1690, 'town', None), (1921, 'victoria', 'The Victoria Memorial, 1921')])
C('lhasa', 91.17, 29.65, (637, None), 'Lhasa', [(637, 2), (842, 3), (1642, 2)], [(637, 'potala', 'The Potala Palace, rebuilt 1645–1694')])

# ---------- East Asia ----------
C('yin', 114.31, 36.12, (-1300, -1046), 'Yin', 1, [(-1300, 'ding', 'Bronze ritual vessels of the Shang kings')], now='Anyang')
C('changan', 108.94, 34.26, (-1046, None), [(-1046, 'Haojing'), (-350, 'Xianyang'), (-202, "Chang'an"), (1369, "Xi'an")],
  [(-1046, 1), (-771, 3), (-350, 2), (-221, 1), (25, 2), (582, 1), (904, 3)],
  [(-1046, 'walls', None), (652, 'pagoda_cn', 'The Giant Wild Goose Pagoda, 652')])
C('luoyang', 112.45, 34.62, (-770, None), 'Luoyang', [(-770, 2), (25, 1), (190, 2), (493, 1), (534, 2), (907, 3)],
  [(-770, 'walls', None), (493, 'pagoda_cn', 'The Buddhist pagodas of Luoyang')])
C('kaifeng', 114.31, 34.80, (907, None), 'Kaifeng', [(907, 2), (960, 1), (1127, 3)], [(907, 'walls', None), (1049, 'pagoda_cn', 'The Iron Pagoda, 1049')])
C('hangzhou', 120.16, 30.27, (589, None), [(589, 'Hangzhou'), (1129, "Lin'an"), (1276, 'Hangzhou')], [(589, 3), (1129, 1), (1276, 2), (1400, 3)],
  [(589, 'walls', None), (970, 'pagoda_cn', 'The Six Harmonies Pagoda, 970')])
C('nanjing', 118.78, 32.06, (229, None), [(229, 'Jianye'), (317, 'Jiankang'), (589, 'Jinling'), (1368, 'Nanjing')],
  [(229, 2), (317, 1), (589, 3), (1368, 1), (1421, 2), (1927, 1), (1949, 2)],
  [(229, 'walls', None), (1368, 'krgate', 'The Ming city walls and the Zhonghua Gate'), (1431, 'pagoda_cn', 'The Porcelain Tower, 1431'),
   (1856, 'krgate', 'The Ming city walls and the Zhonghua Gate')])
C('beijing', 116.39, 39.91, (938, None), [(938, 'Yanjing'), (1153, 'Zhongdu'), (1272, 'Dadu'), (1368, 'Beiping'), (1403, 'Beijing'), (1928, 'Beiping'), (1949, 'Beijing')],
  [(938, 3), (1153, 2), (1272, 1), (1368, 2), (1421, 1), (1928, 2), (1949, 1)],
  [(938, 'walls', None), (1272, 'krgate', 'The walls and gates of Dadu'), (1420, 'heaven', 'The Temple of Heaven, 1420')])
C('canton', 113.26, 23.13, (-214, None), [(-214, 'Panyu'), (226, 'Guangzhou')], [(-214, 3), (1757, 2), (1842, 3)],
  [(-214, 'walls', None), (537, 'pagoda_cn', 'The Flower Pagoda, 537')])
C('hongkong', 114.17, 22.28, (1841, None), 'Hong Kong', [(1841, 3), (1900, 2)], [(1841, 'ship', 'Victoria Harbour'), (1990, 'skyline', 'The towers of Central')])
C('shanghai', 121.47, 31.23, (1843, None), 'Shanghai', 2, [(1843, 'customs', 'The Bund and its Custom House'), (1994, 'pearl', 'The Oriental Pearl Tower, 1994')])
C('karakorum', 102.83, 47.20, (1220, 1388), 'Karakorum', [(1220, 2), (1235, 1), (1260, 2), (1271, 3)], [(1220, 'ger', 'The tents and palace of the Great Khan')])
C('gyeongju', 129.22, 35.835, (-57, None), [(-57, 'Seorabeol'), (940, 'Gyeongju')], [(-57, 3), (668, 2), (935, 3)],
  [(-57, 'walls', None), (647, 'cheomseong', 'Cheomseongdae, the star-gazing tower, 647')])
C('seoul', 126.98, 37.57, (1394, None), [(1394, 'Hanseong'), (1910, 'Keijō'), (1945, 'Seoul')], 2, [(1394, 'krgate', 'Sungnyemun, the Great South Gate, 1398')])
C('nara', 135.84, 34.685, (710, None), 'Nara', [(710, 2), (784, 3)], [(710, 'jphall', 'Tōdai-ji and its Great Buddha Hall, 752')])
C('kyoto', 135.76, 35.01, (794, None), [(794, 'Heian-kyō'), (1100, 'Kyoto')], [(794, 2), (1868, 3)], [(794, 'pagoda_jp', 'The pagoda of Tō-ji, first raised in 826')])
C('tokyo', 139.76, 35.68, (1457, None), [(1457, 'Edo'), (1868, 'Tokyo')], [(1457, 3), (1603, 2), (1700, 1)],
  [(1457, 'jpcastle', 'Edo Castle'), (1958, 'tokyotower', 'Tokyo Tower, 1958')])

# ---------- South-East Asia and Oceania ----------
C('angkor', 103.867, 13.4125, (802, 1431), 'Angkor', [(802, 2), (1113, 1), (1220, 2)],
  [(802, 'angkor', 'The temple-mountains of Angkor'), (1150, 'angkor', 'Angkor Wat, about 1150')])
C('pagan', 94.86, 21.17, (849, 1369), 'Pagan', [(849, 3), (1044, 2), (1287, 3)], [(849, 'stupa', 'The temples and stupas of Pagan')], now='Bagan')
C('ayutthaya', 100.56, 14.355, (1351, 1767), 'Ayutthaya', 2, [(1351, 'prang', 'The prangs of Ayutthaya')])
C('bangkok', 100.50, 13.75, (1782, None), 'Bangkok', 2,
  [(1782, 'stupa', 'The Grand Palace and Wat Phra Kaew, 1784'), (1851, 'prang', 'Wat Arun, its great prang finished in 1851')])
C('rangoon', 96.15, 16.80, (1755, None), [(1755, 'Rangoon'), (1989, 'Yangon')], [(1755, 3), (1852, 2)], [(1755, 'stupa', 'The Shwedagon Pagoda')])
C('hanoi', 105.85, 21.03, (1010, None), [(1010, 'Thăng Long'), (1831, 'Hanoi')], 2, [(1010, 'onepillar', 'The One Pillar Pagoda, 1049')])
C('malacca', 102.25, 2.19, (1400, None), 'Malacca', [(1400, 2), (1824, 3)], [(1400, 'ship', 'The port of Malacca'), (1512, 'castle', 'A Famosa, the Portuguese fort of 1512')])
C('batavia', 106.81, -6.13, (1619, None), [(1619, 'Batavia'), (1949, 'Jakarta')], 2,
  [(1619, 'canalhouses', 'The Dutch canal houses of old Batavia'), (1975, 'monas', 'The National Monument, 1975')])
C('manila', 120.97, 14.59, (1571, None), 'Manila', 2, [(1571, 'cathedral', 'Manila Cathedral, in the walls of Intramuros')])
C('singapore', 103.85, 1.29, (1819, None), 'Singapore', [(1819, 3), (1870, 2)], [(1819, 'ship', 'The port of Singapore'), (2010, 'marina', 'Marina Bay Sands, 2010')])
C('sydney', 151.21, -33.86, (1788, None), 'Sydney', [(1788, 3), (1850, 2)],
  [(1788, 'ship', 'Sydney Cove'), (1932, 'archbridge', 'The Sydney Harbour Bridge, 1932'), (1973, 'opera', 'The Sydney Opera House, 1973')])

# ---------- the Americas ----------
C('teotihuacan', -98.84, 19.69, (-100, 550), 'Teotihuacan', [(-100, 2), (200, 1)], [(-100, 'pyramidsun', 'The Pyramid of the Sun, about 200')])
C('tikal', -89.62, 17.22, (-400, 900), 'Tikal', [(-400, 3), (200, 2)], [(-400, 'mayatemple', 'The temple-pyramids of Tikal')])
C('chichen', -88.57, 20.68, (600, 1200), 'Chichén Itzá', [(600, 3), (900, 2)], [(600, 'elcastillo', 'El Castillo, the Temple of Kukulcán')])
C('tenochtitlan', -99.13, 19.43, (1325, None), [(1325, 'Tenochtitlan'), (1521, 'Mexico City')], [(1325, 2), (1428, 1), (1521, 2)],
  [(1325, 'templomayor', 'The Templo Mayor'), (1521, 'cathedral', 'The Metropolitan Cathedral, built 1573–1813')])
C('cahokia', -90.06, 38.66, (1050, 1350), 'Cahokia', 2, [(1050, 'monksmound', 'Monks Mound')])
C('tiwanaku', -68.67, -16.55, (500, 1000), 'Tiwanaku', 2, [(500, 'sungate', 'The Gate of the Sun')])
C('cusco', -71.97, -13.53, (1100, None), 'Cusco', [(1100, 3), (1438, 1), (1533, 3)],
  [(1100, 'inca', 'Inca stonework of Sacsayhuamán'), (1654, 'cathedral', 'Cusco Cathedral, 1654')])
C('lima', -77.03, -12.05, (1535, None), 'Lima', 2, [(1535, 'cathedral', 'Lima Cathedral')])
C('potosi', -65.75, -19.59, (1545, None), 'Potosí', [(1545, 2), (1570, 1), (1700, 2), (1800, 3)], [(1545, 'cerro', 'Cerro Rico, the silver mountain')])
C('havana', -82.36, 23.14, (1519, None), 'Havana', [(1519, 3), (1561, 2)], [(1519, 'town', None), (1589, 'morro', 'Morro Castle, begun in 1589')])
C('rio', -43.21, -22.91, (1565, None), 'Rio de Janeiro', [(1565, 3), (1763, 2)],
  [(1565, 'sugarloaf', 'Sugarloaf Mountain'), (1931, 'christ', 'Christ the Redeemer, 1931')])
C('brasilia', -47.86, -15.80, (1960, None), 'Brasília', 2, [(1960, 'congress', 'The National Congress, 1960')])
C('buenosaires', -58.38, -34.60, (1580, None), 'Buenos Aires', [(1580, 3), (1776, 2)], [(1580, 'town', None), (1936, 'obelisco', 'The Obelisco, 1936')])
C('quebec', -71.21, 46.81, (1608, None), 'Québec', [(1608, 2), (1867, 3)], [(1608, 'castle', 'The fortress of Québec')])
C('newyork', -74.01, 40.71, (1625, None), [(1625, 'New Amsterdam'), (1664, 'New York')], [(1625, 3), (1790, 2), (1880, 1)],
  [(1625, 'windmill', 'The windmills of New Amsterdam'), (1664, 'town', None), (1886, 'liberty', 'The Statue of Liberty, 1886')])
C('philadelphia', -75.165, 39.95, (1682, None), 'Philadelphia', [(1682, 3), (1750, 2), (1800, 3)],
  [(1682, 'town', None), (1753, 'independence', 'Independence Hall, 1753')])
C('washington', -77.009, 38.89, (1800, None), 'Washington', [(1800, 2), (1917, 1)], [(1800, 'capitol', 'The Capitol')])
C('chicago', -87.63, 41.88, (1833, None), 'Chicago', [(1833, 3), (1880, 2)],
  [(1833, 'town', None), (1885, 'skyline', 'The first skyscrapers, from 1885'), (1974, 'willis', 'The Sears Tower, 1974')])
C('sanfrancisco', -122.42, 37.77, (1847, None), 'San Francisco', [(1847, 3), (1849, 2)],
  [(1847, 'town', None), (1937, 'goldengate', 'The Golden Gate Bridge, 1937')])

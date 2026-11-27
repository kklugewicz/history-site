"""Helpers for writing the people of the map (see the Layout section of the README at the repository root).

Each era file calls P(...) once per person. A person has stints:
  R(from, to, label, *polity_names, at=place)  leads a state: the portrait sits beside that state's name on the map.
                                               `at` is where to show them when none of the names is on the map that year.
  G(from, to, label, *places)                  is somewhere: one place, or a route walked over the stint's years.
A place is a key of C, a (lon, lat) pair, or either of those with a year: ('rome', -49) or (12.5, 41.9, -49).
When a person's stints overlap, a place or route (G) wins over a reign (R) for every year it covers, so a campaign
inside a reign shows the ruler on the move; otherwise the shorter stint wins.
P(..., short=...) or the SHORT table below sets the name written under a face when the page's own rule gets it wrong.
"""

C = {
    # Europe
    'rome': (12.48, 41.89), 'ostia': (12.29, 41.76), 'ravenna': (12.2, 44.42), 'milan': (9.19, 45.46), 'venice': (12.34, 45.44),
    'florence': (11.26, 43.77), 'pisa': (10.4, 43.72), 'genoa': (8.93, 44.41), 'naples': (14.27, 40.85), 'turin': (7.69, 45.07),
    'palermo': (13.36, 38.12), 'syracuse': (15.29, 37.08), 'brundisium': (17.94, 40.64), 'capua': (14.21, 41.08), 'cannae': (16.13, 41.31),
    'pavia': (9.16, 45.19), 'bologna': (11.34, 44.49), 'padua': (11.88, 45.41), 'assisi': (12.61, 43.07), 'urbino': (12.64, 43.73),
    'mantua': (10.79, 45.16), 'verona': (10.99, 45.44), 'trento': (11.12, 46.07), 'caprera': (9.45, 41.21), 'elba': (10.3, 42.78),
    'corsica': (8.74, 41.92), 'sardinia': (9.11, 39.22), 'sicily': (14.0, 37.5), 'lake_trasimene': (12.1, 43.13), 'zama': (9.33, 36.2),
    'rubicon': (12.38, 44.15), 'actium': (20.75, 38.95), 'pharsalus': (22.38, 39.3), 'philippi': (24.29, 41.01), 'thermopylae': (22.54, 38.8),
    'marathon': (23.97, 38.15), 'salamis': (23.47, 37.95), 'plataea': (23.27, 38.21), 'athens': (23.73, 37.98), 'sparta': (22.43, 37.07),
    'corinth': (22.93, 37.94), 'thebes_gr': (23.32, 38.32), 'delphi': (22.5, 38.48), 'olympia': (21.63, 37.64), 'pella': (22.52, 40.76),
    'aegae': (22.32, 40.48), 'chaeronea': (22.85, 38.49), 'stagira': (23.79, 40.53), 'samos': (26.97, 37.75), 'abdera': (24.98, 40.95),
    'mytilene': (26.55, 39.11), 'crete': (25.0, 35.2), 'knossos': (25.16, 35.3), 'mycenae': (22.76, 37.73), 'ithaca': (20.7, 38.37),
    'constantinople': (28.98, 41.01), 'nicaea': (29.72, 40.43), 'chalcedon': (29.03, 40.99), 'adrianople': (26.56, 41.68), 'thessalonica': (22.94, 40.64),
    'sofia': (23.32, 42.7), 'belgrade': (20.46, 44.79), 'bucharest': (26.1, 44.43), 'targoviste': (25.46, 44.93), 'varna': (27.91, 43.21),
    'kosovo': (21.08, 42.66), 'sarajevo': (18.41, 43.86), 'zagreb': (15.98, 45.81), 'ljubljana': (14.51, 46.06), 'tirana': (19.82, 41.33),
    'mohacs': (18.68, 45.99), 'budapest': (19.04, 47.5), 'esztergom': (18.74, 47.79), 'vienna': (16.37, 48.21), 'prague': (14.42, 50.09),
    'krakow': (19.94, 50.06), 'warsaw': (21.01, 52.23), 'gniezno': (17.6, 52.54), 'vilnius': (25.28, 54.69), 'riga': (24.11, 56.95),
    'tannenberg': (20.1, 53.48), 'konigsberg': (20.51, 54.71), 'danzig': (18.65, 54.35), 'berlin': (13.4, 52.52), 'potsdam': (13.06, 52.39),
    'wittenberg': (12.65, 51.87), 'eisleben': (11.55, 51.53), 'wartburg': (10.31, 50.97), 'worms': (8.36, 49.63), 'mainz': (8.27, 50.0),
    'aachen': (6.08, 50.78), 'cologne': (6.96, 50.94), 'trier': (6.64, 49.75), 'frankfurt': (8.68, 50.11), 'nuremberg': (11.08, 49.45),
    'munich': (11.58, 48.14), 'augsburg': (10.9, 48.37), 'regensburg': (12.1, 49.01), 'speyer': (8.43, 49.32), 'canossa': (10.4, 44.58),
    'leipzig': (12.37, 51.34), 'dresden': (13.74, 51.05), 'jena': (11.59, 50.93), 'weimar': (11.33, 50.98), 'hamburg': (9.99, 53.55),
    'gottingen': (9.93, 51.53), 'brunswick': (10.52, 52.26),
    'lubeck': (10.69, 53.87), 'bremen': (8.8, 53.08), 'hanover': (9.73, 52.37), 'bonn': (7.1, 50.73), 'trier2': (6.64, 49.75),
    'teutoburg': (8.13, 52.41), 'lutzen': (12.14, 51.26), 'breitenfeld': (12.4, 51.4), 'blenheim': (10.64, 48.64), 'austerlitz': (16.76, 49.13),
    'wagram': (16.56, 48.3), 'waterloo': (4.41, 50.68), 'sedan': (4.94, 49.7), 'verdun': (5.39, 49.16), 'somme': (2.7, 50.0),
    'ypres': (2.88, 50.85), 'compiegne': (2.83, 49.42), 'paris': (2.35, 48.86), 'versailles': (2.13, 48.8), 'saint_denis': (2.36, 48.94),
    'reims': (4.03, 49.26), 'orleans': (1.91, 47.9), 'rouen': (1.1, 49.44), 'domremy': (5.67, 48.44), 'tours': (0.69, 47.39),
    'poitiers': (0.34, 46.58), 'clermont': (3.08, 45.78), 'cluny': (4.66, 46.43), 'clairvaux': (4.78, 48.15), 'lyon': (4.84, 45.76),
    'avignon': (4.81, 43.95), 'marseille': (5.37, 43.3), 'toulouse': (1.44, 43.6), 'bordeaux': (-0.58, 44.84), 'nantes': (-1.55, 47.22),
    'alesia': (4.5, 47.54), 'gergovia': (3.12, 45.71), 'bibracte': (4.03, 46.92), 'lutetia': (2.35, 48.86), 'agincourt': (2.14, 50.46),
    'crecy': (1.88, 50.25), 'calais': (1.86, 50.95), 'normandy': (-0.6, 49.3), 'brest': (-4.49, 48.39), 'toulon': (5.93, 43.12),
    'ajaccio': (8.74, 41.92), 'nice': (7.26, 43.7), 'geneva': (6.14, 46.2), 'zurich': (8.54, 47.37), 'basel': (7.59, 47.56),
    'brussels': (4.35, 50.85), 'antwerp': (4.4, 51.22), 'ghent': (3.72, 51.05), 'bruges': (3.22, 51.21), 'amsterdam': (4.9, 52.37),
    'the_hague': (4.3, 52.08), 'leiden': (4.49, 52.16), 'rotterdam': (4.48, 51.92), 'delft': (4.36, 52.01), 'luxembourg': (6.13, 49.61),
    'london': (-0.13, 51.51), 'westminster': (-0.13, 51.5), 'canterbury': (1.08, 51.28), 'winchester': (-1.31, 51.06), 'hastings': (0.49, 50.91),
    'oxford': (-1.26, 51.75), 'cambridge': (0.12, 52.21), 'york': (-1.08, 53.96), 'lindisfarne': (-1.8, 55.67), 'jarrow': (-1.48, 54.98),
    'manchester': (-2.24, 53.48), 'birmingham': (-1.9, 52.48), 'bristol': (-2.59, 51.45), 'plymouth': (-4.14, 50.38), 'portsmouth': (-1.09, 50.8),
    'dover': (1.31, 51.13), 'stratford': (-1.71, 52.19), 'downe': (0.05, 51.33), 'woolsthorpe': (-0.63, 52.81), 'edinburgh': (-3.19, 55.95),
    'stirling': (-3.94, 56.12), 'glasgow': (-4.25, 55.86), 'dublin': (-6.26, 53.35), 'armagh': (-6.65, 54.35), 'iona': (-6.41, 56.33),
    'madrid': (-3.7, 40.42), 'toledo': (-4.02, 39.86), 'cordoba': (-4.78, 37.88), 'seville': (-5.98, 37.39), 'granada': (-3.6, 37.18),
    'valladolid': (-4.72, 41.65), 'burgos': (-3.7, 42.34), 'leon': (-5.57, 42.6), 'oviedo': (-5.85, 43.36), 'santiago_c': (-8.54, 42.88),
    'barcelona': (2.17, 41.39), 'zaragoza': (-0.89, 41.65), 'valencia': (-0.38, 39.47), 'cadiz': (-6.29, 36.53), 'gibraltar': (-5.35, 36.14),
    'palos': (-6.89, 37.23), 'covadonga': (-5.05, 43.31), 'lisbon': (-9.14, 38.72), 'sagres': (-8.94, 37.01), 'porto': (-8.61, 41.15),
    'coimbra': (-8.43, 40.21), 'trafalgar': (-6.03, 36.18), 'escorial': (-4.15, 40.59), 'numantia': (-2.44, 41.81), 'new_carthage': (-0.99, 37.6),
    'moscow': (37.62, 55.75), 'st_petersburg': (30.31, 59.94), 'novgorod': (31.27, 58.52), 'kiev': (30.52, 50.45), 'vladimir': (40.41, 56.13),
    'kazan': (49.1, 55.8), 'astrakhan': (48.03, 46.35), 'sarai': (47.0, 47.0), 'poltava': (34.55, 49.59), 'borodino': (35.82, 55.52),
    'stalingrad': (44.52, 48.71), 'kursk': (36.19, 51.73), 'yalta': (34.16, 44.5), 'sevastopol': (33.52, 44.62), 'odessa': (30.72, 46.48),
    'minsk': (27.56, 53.9), 'smolensk': (32.05, 54.78), 'tver': (35.9, 56.86), 'yekaterinburg': (60.6, 56.84), 'tobolsk': (68.25, 58.2),
    'simbirsk': (48.4, 54.32), 'gori': (44.11, 41.98), 'tbilisi': (44.79, 41.72), 'yerevan': (44.51, 40.18), 'baku': (49.87, 40.41),
    'stockholm': (18.07, 59.33), 'uppsala': (17.64, 59.86), 'copenhagen': (12.57, 55.68), 'roskilde': (12.08, 55.64), 'oslo': (10.75, 59.91),
    'trondheim': (10.4, 63.43), 'bergen': (5.32, 60.39), 'reykjavik': (-21.94, 64.15), 'helsinki': (24.94, 60.17), 'narva': (28.19, 59.38),
    'kalmar': (16.36, 56.66), 'birka': (17.54, 59.33), 'hedeby': (9.57, 54.49), 'stiklestad': (11.56, 63.8),
    # Anatolia, Levant, Mesopotamia, Iran, Arabia
    'troy': (26.24, 39.96), 'miletus': (27.28, 37.53), 'ephesus': (27.34, 37.94), 'sardis': (28.04, 38.49), 'gordium': (31.99, 39.65),
    'granicus': (27.2, 40.2), 'issus': (36.21, 36.84), 'tarsus': (34.9, 36.92), 'hattusa': (34.62, 40.02), 'nicomedia': (29.92, 40.77),
    'bursa': (29.06, 40.18), 'edirne': (26.56, 41.68), 'ankara': (32.86, 39.93), 'konya': (32.49, 37.87), 'manzikert': (42.54, 39.14),
    'smyrna': (27.14, 38.42), 'gallipoli': (26.67, 40.41), 'trebizond': (39.72, 41.0), 'kayseri': (35.49, 38.72), 'antioch': (36.16, 36.2),
    'aleppo': (37.16, 36.2), 'damascus': (36.29, 33.51), 'palmyra': (38.27, 34.55), 'kadesh': (36.51, 34.56), 'tyre': (35.2, 33.27),
    'sidon': (35.37, 33.56), 'byblos': (35.65, 34.12), 'beirut': (35.5, 33.89), 'jerusalem': (35.23, 31.78), 'bethlehem': (35.2, 31.7),
    'nazareth': (35.3, 32.7), 'capernaum': (35.57, 32.88), 'jericho': (35.44, 31.86), 'hebron': (35.1, 31.53), 'masada': (35.35, 31.32),
    'caesarea': (34.89, 32.5), 'acre': (35.08, 32.93), 'hattin': (35.45, 32.8), 'ain_jalut': (35.36, 32.55), 'tel_aviv': (34.78, 32.08),
    'gaza': (34.47, 31.5), 'amman': (35.93, 31.95), 'petra': (35.44, 30.33), 'mount_sinai': (33.97, 28.54), 'ur': (46.1, 30.96),
    'uruk': (45.64, 31.32), 'lagash': (46.4, 31.41), 'kish': (44.6, 32.55), 'akkad': (44.1, 33.1), 'babylon': (44.42, 32.54),
    'nineveh': (43.15, 36.36), 'assur': (43.26, 35.46), 'nimrud': (43.33, 36.1), 'gaugamela': (43.43, 36.57), 'mosul': (43.13, 36.34),
    'baghdad': (44.37, 33.31), 'samarra': (43.87, 34.2), 'ctesiphon': (44.58, 33.09), 'kufa': (44.4, 32.03), 'karbala': (44.02, 32.62),
    'najaf': (44.33, 32.0), 'basra': (47.78, 30.51), 'tikrit': (43.68, 34.6), 'susa': (48.25, 32.19), 'persepolis': (52.89, 29.93),
    'pasargadae': (53.17, 30.2), 'ecbatana': (48.52, 34.8), 'isfahan': (51.67, 32.65), 'shiraz': (52.53, 29.59), 'tabriz': (46.29, 38.08),
    'tehran': (51.39, 35.69), 'qom': (50.88, 34.64), 'mashhad': (59.61, 36.3), 'nishapur': (58.8, 36.21), 'rayy': (51.43, 35.59),
    'alamut': (50.59, 36.44), 'yazd': (54.37, 31.9), 'hormuz': (56.46, 27.1), 'mecca': (39.83, 21.42), 'medina': (39.61, 24.47),
    'badr': (38.77, 23.73), 'taif': (40.42, 21.27), 'riyadh': (46.72, 24.69), 'diriyah': (46.57, 24.74), 'sanaa': (44.21, 15.35),
    'aden': (45.03, 12.79), 'muscat': (58.4, 23.6), 'dubai': (55.27, 25.2), 'kuwait': (47.98, 29.38), 'bahrain': (50.58, 26.22),
    'jeddah': (39.17, 21.49), 'mocha': (43.25, 13.32), 'kabul': (69.17, 34.53), 'kandahar': (65.71, 31.61), 'herat': (62.2, 34.35),
    'ghazni': (68.42, 33.55), 'balkh': (66.9, 36.76), 'bamiyan': (67.83, 34.82), 'merv': (61.83, 37.66), 'samarkand': (66.96, 39.65),
    'bukhara': (64.42, 39.77), 'khiva': (60.36, 41.38), 'urgench': (59.15, 42.31), 'otrar': (68.3, 42.85), 'tashkent': (69.24, 41.3),
    'kashgar': (75.99, 39.47), 'khotan': (79.92, 37.11), 'turfan': (89.19, 42.95), 'dunhuang': (94.66, 40.14), 'talas': (72.24, 42.52),
    'karakorum': (102.83, 47.2), 'onon': (110.5, 48.5), 'ulaanbaatar': (106.9, 47.92), 'almaty': (76.89, 43.24), 'sarai_batu': (47.0, 47.0),
    # South Asia
    'harappa': (72.86, 30.63), 'mohenjo_daro': (68.14, 27.33), 'taxila': (72.83, 33.75), 'peshawar': (71.58, 34.01), 'lahore': (74.35, 31.55),
    'amritsar': (74.87, 31.63), 'kartarpur': (75.16, 32.08), 'anandpur': (76.5, 31.24), 'delhi': (77.21, 28.61), 'panipat': (76.97, 29.39),
    'agra': (78.01, 27.18), 'fatehpur_sikri': (77.66, 27.09), 'mathura': (77.67, 27.49), 'kurukshetra': (76.88, 29.97), 'pataliputra': (85.14, 25.59),
    'varanasi': (83.01, 25.32), 'sarnath': (83.03, 25.38), 'bodh_gaya': (84.99, 24.7), 'rajgir': (85.42, 25.03), 'lumbini': (83.28, 27.47),
    'kapilavastu': (83.05, 27.54), 'kushinagar': (83.89, 26.74), 'vaishali': (85.13, 25.99), 'nalanda': (85.44, 25.14), 'ujjain': (75.78, 23.18),
    'sanchi': (77.74, 23.48), 'ayodhya': (82.2, 26.8), 'prayagraj': (81.85, 25.44), 'kalinga': (85.82, 20.3), 'puri': (85.83, 19.81),
    'dhaka': (90.41, 23.81), 'murshidabad': (88.27, 24.18), 'plassey': (88.25, 23.8), 'calcutta': (88.36, 22.57), 'kolkata': (88.36, 22.57),
    'bombay': (72.88, 19.08), 'mumbai': (72.88, 19.08), 'pune': (73.86, 18.52), 'raigad': (73.44, 18.23), 'surat': (72.83, 21.17),
    'ahmedabad': (72.57, 23.02), 'porbandar': (69.6, 21.64), 'dandi': (72.82, 20.89), 'goa': (73.83, 15.49), 'hampi': (76.46, 15.33),
    'bijapur': (75.71, 16.83), 'golconda': (78.4, 17.38), 'hyderabad': (78.49, 17.39), 'mysore': (76.64, 12.3), 'seringapatam': (76.69, 12.42),
    'madras': (80.27, 13.08), 'thanjavur': (79.14, 10.79), 'madurai': (78.12, 9.93), 'kanchipuram': (79.7, 12.83), 'calicut': (75.78, 11.25),
    'cochin': (76.27, 9.93), 'kaladi': (76.44, 10.17), 'sringeri': (75.25, 13.42), 'anuradhapura': (80.4, 8.31), 'kandy': (80.64, 7.29),
    'colombo': (79.86, 6.93), 'kathmandu': (85.32, 27.72), 'lhasa': (91.11, 29.65), 'shigatse': (88.88, 29.27), 'dharamshala': (76.32, 32.22),
    'jhansi': (78.57, 25.45), 'lucknow': (80.95, 26.85), 'meerut': (77.71, 28.98), 'kanpur': (80.33, 26.45), 'karachi': (67.0, 24.86),
    'islamabad': (73.05, 33.68), 'rawalpindi': (73.05, 33.6), 'srinagar': (74.8, 34.08),
    # East Asia
    'anyang': (114.35, 36.1), 'haojing': (108.76, 34.23), 'luoyang': (112.45, 34.62), 'xianyang': (108.71, 34.33), 'changan': (108.94, 34.34),
    'xian': (108.94, 34.34), 'qufu': (116.99, 35.6), 'linzi': (118.31, 36.83), 'handan': (114.49, 36.61), 'ying': (112.19, 30.4),
    'kaifeng': (114.31, 34.8), 'hangzhou': (120.16, 30.27), 'nanjing': (118.78, 32.06), 'beijing': (116.4, 39.9), 'dadu': (116.4, 39.9),
    'shangdu': (116.18, 42.36), 'shanghai': (121.47, 31.23), 'guangzhou': (113.26, 23.13), 'canton': (113.26, 23.13), 'macau': (113.54, 22.2),
    'hong_kong': (114.17, 22.32), 'chengdu': (104.07, 30.67), 'chongqing': (106.55, 29.56), 'wuhan': (114.31, 30.59), 'changsha': (112.94, 28.23),
    'shaoshan': (112.53, 27.92), 'yanan': (109.49, 36.59), 'ruijin': (116.03, 25.89), 'zunyi': (106.93, 27.73), 'red_cliffs': (113.92, 29.86),
    'xuzhou': (117.18, 34.26), 'yangzhou': (119.41, 32.39), 'suzhou': (120.62, 31.3), 'fuzhou': (119.3, 26.08), 'quanzhou': (118.59, 24.91),
    'xiamen': (118.09, 24.48), 'taipei': (121.56, 25.03), 'tainan': (120.2, 22.99), 'shenyang': (123.43, 41.8), 'mukden': (123.43, 41.8),
    'harbin': (126.53, 45.8), 'dalian': (121.61, 38.91), 'port_arthur': (121.25, 38.81), 'tianjin': (117.2, 39.08), 'jinan': (117.0, 36.67),
    'taiyuan': (112.55, 37.87), 'datong': (113.3, 40.08), 'kunming': (102.83, 24.88), 'dali': (100.23, 25.6), 'guilin': (110.29, 25.27),
    'mount_tai': (117.1, 36.25), 'shaolin': (112.94, 34.51), 'longmen': (112.47, 34.55), 'nanchang': (115.86, 28.68), 'yan_an': (109.49, 36.59),
    'kyoto': (135.77, 35.01), 'nara': (135.8, 34.69), 'asuka': (135.82, 34.47), 'kamakura': (139.55, 35.32), 'edo': (139.69, 35.69),
    'tokyo': (139.69, 35.69), 'osaka': (135.5, 34.69), 'nagoya': (136.91, 35.18), 'sekigahara': (136.47, 35.37), 'kagoshima': (130.56, 31.6),
    'nagasaki': (129.87, 32.75), 'hiroshima': (132.46, 34.39), 'hakata': (130.4, 33.59), 'yokohama': (139.64, 35.44), 'uraga': (139.72, 35.24),
    'mount_koya': (135.58, 34.21), 'mount_hiei': (135.84, 35.07), 'ise': (136.72, 34.46), 'gyeongju': (129.21, 35.86), 'seoul': (126.98, 37.57),
    'hanseong': (126.98, 37.57), 'kaesong': (126.55, 37.97), 'pyongyang': (125.75, 39.03), 'busan': (129.08, 35.18), 'incheon': (126.71, 37.46),
    'hansan': (128.46, 34.77), 'myeongnyang': (126.31, 34.57),
    # Southeast Asia, Oceania
    'hanoi': (105.85, 21.03), 'thang_long': (105.85, 21.03), 'hue': (107.58, 16.46), 'saigon': (106.7, 10.78), 'dien_bien_phu': (103.02, 21.39),
    'angkor': (103.87, 13.41), 'phnom_penh': (104.92, 11.56), 'ayutthaya': (100.57, 14.35), 'sukhothai': (99.7, 17.01), 'bangkok': (100.5, 13.76),
    'pagan': (94.86, 21.17), 'mandalay': (96.08, 21.97), 'rangoon': (96.15, 16.87), 'yangon': (96.15, 16.87), 'pegu': (96.48, 17.34),
    'vientiane': (102.63, 17.97), 'luang_prabang': (102.13, 19.89), 'malacca': (102.25, 2.19), 'singapore': (103.82, 1.35), 'kuala_lumpur': (101.69, 3.14),
    'palembang': (104.76, -2.99), 'borobudur': (110.2, -7.61), 'yogyakarta': (110.36, -7.8), 'jakarta': (106.85, -6.21), 'batavia': (106.85, -6.21),
    'majapahit': (112.38, -7.56), 'bali': (115.19, -8.41), 'makassar': (119.42, -5.14), 'ternate': (127.38, 0.79), 'manila': (120.98, 14.6),
    'cebu': (123.89, 10.32), 'mactan': (123.98, 10.29), 'guam': (144.79, 13.44), 'sydney': (151.21, -33.87), 'botany_bay': (151.2, -34.0),
    'canberra': (149.13, -35.28), 'melbourne': (144.96, -37.81), 'wellington': (174.78, -41.29), 'auckland': (174.76, -36.85), 'waitangi': (174.08, -35.27),
    'tahiti': (-149.43, -17.65), 'hawaii': (-155.5, 19.6), 'honolulu': (-157.86, 21.31), 'kealakekua': (-155.92, 19.48), 'pearl_harbor': (-157.95, 21.35),
    'easter_island': (-109.35, -27.11), 'tonga': (-175.2, -21.14), 'fiji': (178.07, -17.71), 'samoa': (-171.76, -13.83), 'new_guinea': (145.0, -6.0),
    'midway': (-177.37, 28.21), 'iwo_jima': (141.32, 24.78), 'okinawa': (127.68, 26.21), 'guadalcanal': (160.0, -9.6), 'leyte': (124.97, 10.86),
    'tinian': (145.63, 15.0), 'saipan': (145.75, 15.18), 'corregidor': (120.57, 14.38),
    # Africa
    'cairo': (31.24, 30.04), 'giza': (31.13, 29.98), 'memphis': (31.25, 29.85), 'saqqara': (31.22, 29.87), 'heliopolis': (31.31, 30.13),
    'alexandria': (29.92, 31.2), 'thebes': (32.64, 25.7), 'luxor': (32.64, 25.7), 'karnak': (32.66, 25.72), 'amarna': (30.9, 27.65),
    'abydos': (31.92, 26.19), 'aswan': (32.9, 24.09), 'abu_simbel': (31.63, 22.34), 'avaris': (31.82, 30.79), 'tanis': (31.88, 30.98),
    'sais': (30.77, 30.96), 'siwa': (25.52, 29.2), 'el_alamein': (28.95, 30.83), 'suez': (32.55, 29.97), 'port_said': (32.3, 31.26),
    'napata': (31.83, 18.54), 'meroe': (33.75, 16.94), 'kerma': (30.4, 19.6), 'khartoum': (32.53, 15.5), 'omdurman': (32.48, 15.64),
    'axum': (38.72, 14.13), 'adulis': (39.66, 15.26), 'lalibela': (39.05, 12.03), 'gondar': (37.47, 12.61), 'adwa': (38.9, 14.16),
    'addis_ababa': (38.74, 9.03), 'magdala': (39.39, 11.36), 'harar': (42.12, 9.31), 'mogadishu': (45.32, 2.05), 'kilwa': (39.51, -8.96),
    'mombasa': (39.67, -4.04), 'malindi': (40.12, -3.22), 'zanzibar': (39.19, -6.16), 'dar_es_salaam': (39.28, -6.79), 'nairobi': (36.82, -1.29),
    'kampala': (32.58, 0.35), 'kigali': (30.06, -1.94), 'great_zimbabwe': (30.93, -20.27), 'harare': (31.05, -17.83), 'sofala': (34.75, -20.15),
    'mozambique_island': (40.74, -15.03), 'cape_town': (18.42, -33.92), 'cape_good_hope': (18.47, -34.36), 'ulundi': (31.42, -28.32), 'isandlwana': (30.65, -28.36),
    'pretoria': (28.19, -25.75), 'johannesburg': (28.05, -26.2), 'robben_island': (18.37, -33.81), 'qunu': (28.62, -31.78), 'soweto': (27.86, -26.27),
    'kinshasa': (15.27, -4.44), 'mbanza_kongo': (14.24, -6.27), 'luanda': (13.23, -8.84), 'lagos': (3.38, 6.52), 'abuja': (7.4, 9.06),
    'benin_city': (5.63, 6.34), 'ife': (4.56, 7.47), 'oyo': (3.93, 7.85), 'kano': (8.52, 12.0), 'sokoto': (5.24, 13.06), 'katsina': (7.6, 12.99),
    'kukawa': (13.56, 12.92), 'njimi': (14.6, 14.3), 'kumasi': (-1.62, 6.69), 'accra': (-0.19, 5.6), 'elmina': (-1.35, 5.08),
    'abomey': (1.99, 7.18), 'ouidah': (2.09, 6.36), 'dakar': (-17.44, 14.69), 'goree': (-17.4, 14.67), 'saint_louis_sn': (-16.49, 16.03),
    'timbuktu': (-3.0, 16.77), 'djenne': (-4.56, 13.91), 'gao': (-0.04, 16.27), 'niani': (-8.39, 11.38), 'kangaba': (-8.39, 11.94),
    'kumbi_saleh': (-7.97, 15.66), 'segou': (-6.26, 13.43), 'bamako': (-8.0, 12.64), 'conakry': (-13.68, 9.64), 'freetown': (-13.23, 8.48),
    'monrovia': (-10.8, 6.3), 'tunis': (10.18, 36.81), 'carthage': (10.32, 36.85), 'utica': (10.06, 37.06), 'kairouan': (10.1, 35.68),
    'hippo': (7.77, 36.88), 'thagaste': (7.95, 36.29), 'algiers': (3.06, 36.75), 'oran': (-0.64, 35.7), 'tlemcen': (-1.31, 34.88),
    'fez': (-5.0, 34.03), 'marrakesh': (-7.99, 31.63), 'rabat': (-6.84, 34.02), 'tangier': (-5.83, 35.77), 'ceuta': (-5.32, 35.89),
    'meknes': (-5.55, 33.9), 'sijilmasa': (-4.27, 31.28), 'tripoli': (13.19, 32.89), 'leptis_magna': (14.29, 32.64), 'cyrene': (21.86, 32.82),
    'tobruk': (23.96, 32.08), 'benghazi': (20.07, 32.12), 'sirte': (16.59, 31.21), 'tamanrasset': (5.52, 22.79), 'agadez': (7.99, 16.97),
    'madagascar': (47.5, -18.9), 'antananarivo': (47.52, -18.88), 'st_helena': (-5.72, -15.97), 'luxor2': (32.64, 25.7),
    # Americas
    'tenochtitlan': (-99.13, 19.43), 'mexico_city': (-99.13, 19.43), 'teotihuacan': (-98.84, 19.69), 'tula': (-99.34, 20.06), 'cholula': (-98.3, 19.06),
    'tlaxcala': (-98.24, 19.32), 'veracruz': (-96.13, 19.17), 'tikal': (-89.62, 17.22), 'palenque': (-91.98, 17.48), 'copan': (-89.14, 14.84),
    'calakmul': (-89.74, 18.1), 'chichen_itza': (-88.57, 20.68), 'mayapan': (-89.46, 20.63), 'monte_alban': (-96.77, 17.04), 'la_venta': (-94.04, 18.1),
    'oaxaca': (-96.73, 17.07), 'puebla': (-98.2, 19.04), 'queretaro': (-100.39, 20.59), 'dolores': (-100.93, 21.16), 'guadalajara': (-103.35, 20.67),
    'chihuahua': (-106.09, 28.63), 'morelos': (-99.07, 18.68), 'yucatan': (-89.62, 20.97), 'cuzco': (-71.97, -13.53), 'machu_picchu': (-72.55, -13.16),
    'cajamarca': (-78.52, -7.16), 'lima': (-77.04, -12.05), 'callao': (-77.15, -12.06), 'quito': (-78.47, -0.18), 'tumbes': (-80.45, -3.57),
    'chan_chan': (-79.08, -8.11), 'tiwanaku': (-68.67, -16.55), 'lake_titicaca': (-69.3, -15.9), 'potosi': (-65.75, -19.58), 'la_paz': (-68.15, -16.5),
    'sucre': (-65.26, -19.04), 'ayacucho': (-74.22, -13.16), 'junin': (-75.99, -11.16), 'bogota': (-74.07, 4.71), 'boyaca': (-73.4, 5.45),
    'cartagena': (-75.48, 10.39), 'caracas': (-66.9, 10.48), 'carabobo': (-68.04, 10.05), 'angostura': (-63.55, 8.12), 'guayaquil': (-79.89, -2.19),
    'santa_marta': (-74.2, 11.24), 'panama': (-79.52, 8.98), 'darien': (-77.8, 8.4), 'buenos_aires': (-58.38, -34.6), 'santiago': (-70.67, -33.45),
    'valparaiso': (-71.61, -33.05), 'mendoza': (-68.83, -32.89), 'chacabuco': (-70.7, -32.97), 'maipu': (-70.76, -33.51), 'montevideo': (-56.16, -34.9),
    'asuncion': (-57.58, -25.26), 'rio': (-43.17, -22.91), 'sao_paulo': (-46.63, -23.55), 'salvador': (-38.5, -12.97), 'recife': (-34.88, -8.05),
    'brasilia': (-47.88, -15.79), 'ouro_preto': (-43.5, -20.38), 'porto_seguro': (-39.06, -16.45), 'manaus': (-60.02, -3.12), 'belem': (-48.5, -1.46),
    'tierra_del_fuego': (-68.3, -54.8), 'strait_magellan': (-70.9, -53.3), 'galapagos': (-90.5, -0.7), 'havana': (-82.38, 23.13), 'santiago_cuba': (-75.82, 20.02),
    'sierra_maestra': (-76.7, 20.0), 'bay_of_pigs': (-81.1, 22.1), 'santo_domingo': (-69.93, 18.49), 'hispaniola': (-71.0, 19.0), 'cap_haitien': (-72.2, 19.76),
    'port_au_prince': (-72.34, 18.54), 'san_salvador_bh': (-74.48, 24.05), 'kingston': (-76.79, 18.0), 'puerto_rico': (-66.1, 18.47), 'trinidad': (-61.3, 10.5),
    'grenada': (-61.68, 12.12), 'martinique': (-61.02, 14.64), 'barbados': (-59.6, 13.1), 'washington': (-77.04, 38.9), 'philadelphia': (-75.17, 39.95),
    'boston': (-71.06, 42.36), 'new_york': (-74.0, 40.71), 'jamestown': (-76.78, 37.21), 'plymouth_ma': (-70.67, 41.96), 'yorktown': (-76.51, 37.24),
    'valley_forge': (-75.44, 40.1), 'saratoga': (-73.64, 43.0), 'mount_vernon': (-77.09, 38.71), 'monticello': (-78.45, 38.01), 'springfield_il': (-89.65, 39.8),
    'gettysburg': (-77.23, 39.83), 'richmond': (-77.44, 37.54), 'appomattox': (-78.8, 37.38), 'atlanta': (-84.39, 33.75), 'savannah': (-81.1, 32.08),
    'charleston': (-79.93, 32.78), 'vicksburg': (-90.88, 32.35), 'antietam': (-77.74, 39.47), 'new_orleans': (-90.07, 29.95), 'st_louis': (-90.2, 38.63),
    'chicago': (-87.63, 41.88), 'detroit': (-83.05, 42.33), 'pittsburgh': (-80.0, 40.44), 'fort_duquesne': (-80.0, 40.44), 'memphis_tn': (-90.05, 35.15),
    'montgomery': (-86.3, 32.38), 'selma': (-87.02, 32.41), 'birmingham_al': (-86.8, 33.52), 'dallas': (-96.8, 32.78), 'houston': (-95.37, 29.76),
    'san_antonio': (-98.49, 29.42), 'santa_fe': (-105.94, 35.69), 'los_alamos': (-106.3, 35.88), 'denver': (-104.99, 39.74), 'salt_lake': (-111.89, 40.76),
    'little_bighorn': (-107.43, 45.57), 'wounded_knee': (-102.36, 43.14), 'black_hills': (-103.75, 44.0), 'san_francisco': (-122.42, 37.77), 'los_angeles': (-118.24, 34.05),
    'sacramento': (-121.49, 38.58), 'seattle': (-122.33, 47.61), 'portland_or': (-122.68, 45.52), 'fort_clatsop': (-123.88, 46.13), 'cahokia': (-90.06, 38.66),
    'chaco_canyon': (-107.96, 36.06), 'mesa_verde': (-108.46, 37.18), 'quebec': (-71.21, 46.81), 'montreal': (-73.57, 45.5), 'ottawa': (-75.7, 45.42),
    'toronto': (-79.38, 43.65), 'halifax': (-63.57, 44.65), 'louisbourg': (-59.99, 45.92), 'hudson_bay': (-85.0, 60.0), 'newfoundland': (-55.7, 48.6),
    'lanse_aux_meadows': (-55.53, 51.6), 'greenland': (-45.0, 61.0), 'brattahlid': (-45.51, 61.16), 'vancouver': (-123.12, 49.28), 'juneau': (-134.42, 58.3),
    'cape_canaveral': (-80.6, 28.39), 'houston_space': (-95.09, 29.56), 'atlanta2': (-84.39, 33.75), 'lexington': (-71.23, 42.45), 'trenton': (-74.76, 40.22),
    'hyde_park': (-73.93, 41.78), 'independence_mo': (-94.42, 39.09), 'abilene': (-97.21, 38.92), 'west_point': (-73.96, 41.39), 'plains_ga': (-84.39, 32.03),
    'oyster_bay': (-73.53, 40.87), 'dayton': (-84.19, 39.76), 'kitty_hawk': (-75.67, 36.02), 'menlo_park': (-74.33, 40.56), 'princeton': (-74.66, 40.35),
}

PEOPLE = []
TAGS = {'war', 'explore', 'faith', 'mind', 'art', 'rule', 'power', 'reform'}


def _pt(p):
    """a place: key, (key, year), (lon, lat) or (lon, lat, year) -> [lon, lat] or [lon, lat, year]"""
    if isinstance(p, str):
        return list(C[p])
    if isinstance(p, (tuple, list)) and p and isinstance(p[0], str):
        return list(C[p[0]]) + [p[1]]
    return list(p)


def R(a, b, label, *names, at=None):
    s = {'from': a, 'to': b, 'label': label, 'rule': list(names)}
    if at is not None:
        s['at'] = _pt(at)
    return s


def G(a, b, label, *places):
    return {'from': a, 'to': b, 'label': label, 'path': [_pt(p) for p in places]}


# the name the map writes under a face, for the long names that the page's own rule gets wrong (it keeps the part
# before ', ', ' of ' or ' the ', then a regnal number, then the surname with its particles)
SHORT = {
    'Antonio López de Santa Anna': 'Santa Anna', 'Edward the Black Prince': 'Black Prince', 'Archduke Franz Ferdinand': 'Franz Ferdinand',
    'Agha Mohammad Khan Qajar': 'Agha Mohammad Khan', 'Arthur Wellesley, 1st Duke of Wellington': 'Wellington',
    'John Churchill, 1st Duke of Marlborough': 'Marlborough', 'Camillo Benso, Count of Cavour': 'Cavour',
    'Joséphine de Beauharnais': 'Joséphine',
    'Naser al-Din Shah Qajar': 'Naser al-Din Shah', 'Mozaffar ad-Din Shah Qajar': 'Mozaffar ad-Din Shah',
    'Mohammad Ali Shah Qajar': 'Mohammad Ali Shah', 'Charles Cornwallis, 1st Marquess Cornwallis': 'Cornwallis',
    'Nasir-ud-Din Mahmud Shah Tughluq': 'Mahmud Tughluq', 'Zine El Abidine Ben Ali': 'Ben Ali',
    'José Eduardo dos Santos': 'dos Santos', 'Andrés Manuel López Obrador': 'López Obrador',
    'Anastasio Somoza García': 'Somoza García', 'Anastasio Somoza Debayle': 'Somoza Debayle',
    'Humberto Castelo Branco': 'Castelo Branco', 'Cristina Fernández de Kirchner': 'Cristina Kirchner',
    'William Lyon Mackenzie King': 'Mackenzie King', 'António José de Almeida': 'Almeida', 'Carlos Salinas de Gortari': 'Carlos Salinas',
    'Fernando Collor de Mello': 'Fernando Collor', 'Carlos Ibáñez del Campo': 'Carlos Ibáñez', 'José Gaspar Rodríguez de Francia': 'Francia',
}


def P(name, role, life, rank, tags, why, *stints, wiki=None, id=None, short=None):
    import re, unicodedata
    slug = id or re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower()).strip('-')
    short = short or SHORT.get(name)
    PEOPLE.append({'id': slug, 'name': name, 'role': role, 'life': list(life), 'rank': rank,
                   'tags': tags.split(), 'why': why, 'wiki': wiki or name, 'stints': list(stints)} | ({'short': short} if short else {}))

# places added for the 1650-2026 files
C.update({
    'salzburg': (13.04, 47.8), 'utrecht': (5.12, 52.09), 'jaffa': (34.75, 32.05), 'liverpool': (-2.98, 53.41),
})

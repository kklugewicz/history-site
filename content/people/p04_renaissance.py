from _lib import P, R, G

ENG = ('England', 'English territory', 'England and Ireland')
FRA = ('France', 'Kingdom of France')
OTT = ('Ottoman Empire',)
HRE = ('Holy Roman Empire',)
SPAIN = ('Spain', 'Castille', 'Castile')

# ---------- Late medieval Europe and the Mediterranean ----------
P('Osman I', 'Founder of the Ottoman Empire', (1258, 1326), 2, 'rule war',
  'Turkish chief in north-west Anatolia whose small state grew into the Ottoman Empire.',
  G(1299, 1326, 'Founder of the Ottoman state', (30.15, 40.15), 'bursa'))
P('Philip IV of France', 'King of France', (1268, 1314), 3, 'rule',
  "'The Fair': broke the Knights Templar and dragged the papacy to Avignon.",
  R(1285, 1314, 'King of France', *FRA, at='paris'))
P('Mansa Musa', 'Emperor of Mali', (1280, 1337), 1, 'rule faith',
  "Perhaps the richest man who ever lived: his pilgrimage to Mecca spent so much gold that Cairo's prices crashed.",
  G(1324, 1325, 'Pilgrimage to Mecca', ('niani', 1324), ('timbuktu', 1324.15), ((-0.04, 16.27, 1324.2)), ((7.99, 16.97, 1324.35)), ('cairo', 1324.55),
    ('medina', 1324.85), ('mecca', 1324.95), ('cairo', 1325.3), ('gao', 1325.65), ('timbuktu', 1325.8)),
  R(1312, 1337, 'Mansa of Mali', 'Mali', at='niani'))
P('Giotto', 'Italian painter', (1267, 1337), 3, 'art',
  'Broke with flat medieval painting and gave figures weight and feeling, the first step to the Renaissance.',
  G(1300, 1337, 'Painter in Padua and Florence', 'padua', 'assisi', 'florence'))
P('Petrarch', 'Italian poet and scholar', (1304, 1374), 3, 'art mind',
  'Hunted down lost Latin classics and wrote the love sonnets that founded Renaissance humanism.',
  G(1326, 1352, 'Avignon and Vaucluse', 'avignon'), G(1353, 1374, 'Milan, Venice and Padua', 'milan', 'venice', 'padua'))
P('Edward III of England', 'King of England', (1312, 1377), 2, 'rule war',
  'Claimed the French crown and began the Hundred Years War with victory at Crécy.',
  G(1346, 1347, 'Crécy and Calais', (-1.3, 49.57), 'crecy', 'calais'), R(1327, 1377, 'King of England', *ENG, at='london'))
P('Edward the Black Prince', 'English prince and commander', (1330, 1376), 3, 'war',
  'Captured the king of France at Poitiers in 1356.',
  G(1355, 1356, 'Raids and Poitiers', 'bordeaux', 'toulouse', 'bordeaux', (0.38, 46.6)))
P('Ibn Battuta', 'Moroccan traveller', (1304, 1369), 1, 'explore',
  'Travelled about 120,000 km over thirty years, from Mali to China, and dictated it all in his Rihla.',
  G(1325, 1354, 'Travels of thirty years', ('tangier', 1325.45), ('tunis', 1325.7), ('alexandria', 1326.3), 'cairo', ('damascus', 1326.6),
    ('mecca', 1326.85), ('baghdad', 1327.3), ('tabriz', 1327.4), ('mecca', 1327.8), ('mecca', 1330.6), ('aden', 1330.8), ('mogadishu', 1331),
    ('kilwa', 1331.2), ('muscat', 1331.6), ('hormuz', 1331.7), ('mecca', 1332.1), ('konya', 1332.5), ('sarai', 1333.3), ('constantinople', 1333.6),
    ('bukhara', 1333.9), ('samarkand', 1334), ('kabul', 1334.3), ('delhi', 1334.6), ('delhi', 1341.6), ('calicut', 1342.1), ((73.5, 4.2, 1343)),
    ('colombo', 1344.3), ((90.4, 23.8, 1345.2)), ((95.3, 5.5, 1345.5)), ('quanzhou', 1345.8), ('beijing', 1346.1), ('quanzhou', 1346.5),
    ('calicut', 1347.2), ('baghdad', 1348), ('damascus', 1348.4), ('mecca', 1348.9), ('cairo', 1349.3), ('fez', 1349.85), ('granada', 1350.4),
    ('fez', 1351), ('timbuktu', 1353.1), ('fez', 1354)),
  G(1355, 1368, 'Dictates the Rihla in Fez', 'fez'))
P('Murad I', 'Ottoman sultan', (1326, 1389), 3, 'rule war',
  'Took Adrianople and the Balkans for the Ottomans and was killed at the Battle of Kosovo.',
  G(1389, 1389, 'Battle of Kosovo', 'edirne', 'sofia', 'kosovo'), R(1362, 1389, 'Ottoman sultan', *OTT, at='edirne'))
P('Timur', 'Founder of the Timurid Empire', (1336, 1405), 1, 'war rule',
  'Tamerlane: conquered from Delhi to Ankara and built Samarkand with the craftsmen of the cities he sacked.',
  G(1386, 1388, 'Persia and the Caucasus', 'samarkand', 'herat', 'isfahan', 'tabriz', 'tbilisi', 'samarkand'),
  G(1395, 1395, 'Destruction of the Golden Horde', 'samarkand', (46.6, 43.6), 'sarai', 'samarkand'),
  G(1398, 1399, 'Sack of Delhi', 'samarkand', 'kabul', 'delhi', 'samarkand'),
  G(1400, 1402, 'Syria and Ankara', 'tbilisi', 'aleppo', 'damascus', 'baghdad', ('ankara', 1402.55), 'smyrna'),
  G(1404, 1405, 'March on China', 'samarkand', 'otrar'),
  R(1370, 1405, 'Emir of Samarkand', 'Timurid Empire', 'Chagatai Khanate', at='samarkand'))
P('Bayezid I', 'Ottoman sultan', (1360, 1403), 2, 'rule war',
  "'The Thunderbolt': crushed the crusaders at Nicopolis, then was beaten and captured by Timur at Ankara.",
  G(1396, 1396, 'Battle of Nicopolis', 'edirne', (24.9, 43.7)), G(1402, 1403, 'Captive of Timur', 'ankara', (31.42, 38.36)),
  R(1389, 1401, 'Ottoman sultan', *OTT, at='edirne'))
P('Hongwu Emperor', 'Founder of the Ming dynasty', (1328, 1398), 2, 'rule',
  'A poor orphan and Red Turban rebel who drove out the Mongols and founded the Ming dynasty.',
  G(1352, 1367, 'Red Turban rebel', (117.4, 32.9), 'nanjing'), R(1368, 1398, 'Emperor of Ming China', 'Ming Empire', at='nanjing'))
P('Yongle Emperor', 'Emperor of Ming China', (1360, 1424), 2, 'rule',
  'Moved the capital to Beijing, built the Forbidden City and sent out Zheng He\'s treasure fleets.',
  R(1402, 1424, 'Emperor of Ming China', 'Ming Empire', at='beijing'))
P('Zheng He', 'Ming admiral', (1371, 1433), 1, 'explore',
  'Led seven treasure fleets of hundreds of ships across the Indian Ocean to Arabia and East Africa.',
  G(1405, 1433, 'Treasure fleet voyages', ('nanjing', 1405.5), ((109.2, 13.0, 1405.9)), ((106.85, -6.21, 1406.2)), ('palembang', 1406.4), ('malacca', 1406.6),
    ((79.86, 6.93, 1406.9)), ('calicut', 1407.1), ('nanjing', 1407.8), ('calicut', 1409.5), ('nanjing', 1411.6), ('malacca', 1413.5), ('hormuz', 1414.3),
    ('aden', 1417.5), ('mogadishu', 1417.8), ('malindi', 1418.1), ('calicut', 1418.6), ('nanjing', 1419.6), ('nanjing', 1431.9), ('malacca', 1432.3),
    ('calicut', 1432.8), ('hormuz', 1433.1), ('calicut', 1433.4)))
P('Jan Hus', 'Czech church reformer', (1372, 1415), 2, 'faith reform',
  'Preached against church corruption a century before Luther and was burned at the Council of Constance.',
  G(1402, 1413, 'Preacher in Prague', 'prague'), G(1414, 1415, 'Council of Constance', 'prague', (9.17, 47.66)))
P('Jan Žižka', 'Hussite general', (1360, 1424), 3, 'war',
  'One-eyed, then blind, general whose war wagons beat every crusade sent against the Hussites.',
  G(1419, 1424, 'Hussite Wars', 'prague', (14.66, 49.41), (15.26, 49.95)))
P('Władysław II Jagiełło', 'King of Poland', (1352, 1434), 3, 'rule war',
  'Grand Duke of Lithuania who married Poland\'s queen and broke the Teutonic Knights at Grunwald.',
  G(1410, 1410, 'Battle of Grunwald', 'krakow', 'warsaw', 'tannenberg'), R(1386, 1434, 'King of Poland', 'Poland-Lithuania', 'Poland', at='krakow'))
P('Henry the Navigator', 'Portuguese prince', (1394, 1460), 2, 'explore',
  "Sent ship after ship down the African coast, starting Europe's age of exploration.",
  G(1415, 1415, 'Conquest of Ceuta', 'lisbon', 'ceuta'), G(1419, 1460, 'Patron of exploration at Sagres', 'sagres'))
P('Henry V of England', 'King of England', (1386, 1422), 2, 'rule war',
  'Won the battle of Agincourt against a far larger French army and was made heir to France.',
  G(1415, 1415, 'Agincourt', 'london', (0.1, 49.49), 'agincourt', 'calais'), G(1417, 1422, 'Conquest of Normandy', 'rouen', 'paris'),
  R(1413, 1416, 'King of England', *ENG, at='london'))
P('Joan of Arc', 'French heroine and saint', (1412, 1431), 1, 'war faith',
  "Peasant girl who heard voices, broke the siege of Orléans and had the king crowned at Reims; burned by the English at 19.",
  G(1412, 1428, 'Youth at Domrémy', 'domremy'),
  G(1429, 1429, 'Orléans and Reims', 'domremy', (0.24, 47.17), 'orleans', 'reims', 'paris'),
  G(1430, 1431, 'Captured, tried and burned', 'compiegne', 'rouen'))
P('Charles VII of France', 'King of France', (1403, 1461), 3, 'rule',
  "Crowned at Reims thanks to Joan of Arc; drove the English out of France.",
  R(1422, 1461, 'King of France', *FRA, at='orleans'))
P('Johannes Gutenberg', 'Inventor of the printing press', (1400, 1468), 1, 'mind',
  'His movable-type printing press made books cheap and spread the Renaissance and the Reformation.',
  G(1434, 1444, 'Strasbourg', (7.75, 48.58)), G(1448, 1468, 'Printing press at Mainz', 'mainz'))
P('Sejong the Great', 'King of Joseon Korea', (1397, 1450), 2, 'rule mind',
  'Created Hangul, the Korean alphabet, and sponsored inventions from rain gauges to water clocks.',
  R(1418, 1450, 'King of Joseon', 'Korea', at='seoul'))
P('Lê Lợi', 'Emperor of Đại Việt', (1385, 1433), 3, 'rule war',
  'Led ten years of war that drove the Ming out of Vietnam.',
  G(1418, 1427, 'War of liberation', (105.5, 20.0), 'thang_long'), G(1428, 1433, 'Emperor of Đại Việt', 'thang_long'))
P('Cosimo de\' Medici', 'Banker and ruler of Florence', (1389, 1464), 3, 'rule art',
  "Europe's richest banker, who ruled Florence from behind the scenes and paid for its Renaissance.",
  G(1434, 1464, 'First citizen of Florence', 'florence'))
P('Filippo Brunelleschi', 'Florentine architect', (1377, 1446), 3, 'art mind',
  'Built the great dome of Florence cathedral and worked out the rules of perspective.',
  G(1418, 1446, 'Builds the dome of Florence', 'florence'))
P('John Hunyadi', 'Hungarian general', (1406, 1456), 3, 'war',
  "Hungary's champion against the Ottomans, who held Belgrade against Mehmed II in 1456.",
  G(1444, 1444, 'Battle of Varna', 'budapest', 'varna'), G(1456, 1456, 'Siege of Belgrade', 'budapest', 'belgrade'))
P('Skanderbeg', 'Albanian national hero', (1405, 1468), 3, 'war',
  'Deserted the Ottoman army and held Albania against it for 25 years from his castle at Krujë.',
  G(1443, 1468, 'Revolt against the Ottomans', (19.79, 41.5)))
P('Constantine XI Palaiologos', 'Last Byzantine emperor', (1404, 1453), 3, 'rule',
  'Died fighting on the walls when Constantinople fell in 1453.',
  R(1449, 1453, 'Emperor of the Romans', 'Byzantine Empire', at='constantinople'))
P('Mehmed II', 'Ottoman sultan', (1432, 1481), 1, 'rule war',
  "Took Constantinople in 1453 with giant cannon, ending the Roman Empire, and made it the Ottoman capital.",
  G(1453, 1453, 'Conquest of Constantinople', 'edirne', 'constantinople'),
  R(1451, 1481, 'Ottoman sultan', *OTT, at='constantinople'), wiki='Mehmed II')
P('Vlad the Impaler', 'Prince of Wallachia', (1431, 1476), 2, 'war rule',
  'Fought the Ottomans with such cruelty that he became the model for Dracula.',
  G(1456, 1462, 'Prince of Wallachia', 'targoviste'))
P('Nezahualcoyotl', 'Poet-king of Texcoco', (1402, 1472), 3, 'rule art',
  'Philosopher, poet and engineer king who co-founded the Aztec Triple Alliance.',
  G(1431, 1472, 'King of Texcoco', (-98.88, 19.51)), wiki='Nezahualcoyotl (tlatoani)')
P('Pachacuti', 'Founder of the Inca Empire', (1418, 1471), 2, 'rule war',
  'Saved Cusco from the Chanka and turned a small kingdom into the Inca Empire; Machu Picchu was likely his estate.',
  G(1438, 1471, 'Sapa Inca at Cusco', 'cuzco', 'machu_picchu'))
P('Ivan III', 'Grand Prince of Moscow', (1440, 1505), 2, 'rule',
  "Threw off the Tatar yoke, took Novgorod and styled Moscow the heir of Byzantium.",
  R(1462, 1505, 'Grand Prince of Moscow', 'Grand Duchy of Moscow', at='moscow'), wiki='Ivan III of Russia')
P('Sunni Ali', 'King of Songhai', (1420, 1492), 3, 'rule war',
  'Took Timbuktu and Djenné and built the Songhai Empire.',
  R(1464, 1492, 'King of Songhai', 'Songhai', at='gao'))
P('Lorenzo de\' Medici', 'Ruler of Florence', (1449, 1492), 2, 'rule art',
  "'The Magnificent': patron of Botticelli and the young Michelangelo at the height of the Florentine Renaissance.",
  G(1469, 1492, 'Lord of Florence', 'florence'))
P('Sandro Botticelli', 'Florentine painter', (1445, 1510), 3, 'art',
  'Painted The Birth of Venus and Primavera for the Medici circle.',
  G(1470, 1510, 'Painter in Florence', 'florence'))
P('Isabella I of Castile', 'Queen of Castile', (1451, 1504), 1, 'rule',
  'With Ferdinand of Aragon united Spain, conquered Granada and sent Columbus across the Atlantic.',
  G(1492, 1492, 'Fall of Granada', (-3.67, 37.17), 'granada'), R(1474, 1504, 'Queen of Castile', *SPAIN, at='valladolid'))
P('Ferdinand II of Aragon', 'King of Aragon and Castile', (1452, 1516), 2, 'rule',
  "Isabella's husband and partner: together the Catholic Monarchs made Spain a great power.",
  R(1479, 1516, 'King of Aragon, ruler of Spain', 'Aragón', *SPAIN, at='zaragoza'))
P('Tomás de Torquemada', 'Grand Inquisitor of Spain', (1420, 1498), 3, 'faith',
  'Led the Spanish Inquisition and pushed for the expulsion of the Jews in 1492.',
  G(1483, 1498, 'Grand Inquisitor', 'valladolid', (-4.7, 40.66)))
P('Bartolomeu Dias', 'Portuguese explorer', (1450, 1500), 3, 'explore',
  'First European to sail round the southern tip of Africa, in 1488.',
  G(1487, 1488, 'Rounds the Cape of Good Hope', 'lisbon', (12.0, -15.0), 'cape_good_hope', (26.5, -33.8), 'cape_good_hope', 'lisbon'))
P('Christopher Columbus', 'Explorer for Spain', (1451, 1506), 1, 'explore',
  'Sailed west in 1492 looking for Asia and reached the Americas, linking the two halves of the world for good.',
  G(1492, 1493, 'First voyage', ('palos', 1492.6), ((-15.4, 28.1, 1492.7)), ('san_salvador_bh', 1492.78), ((-75.8, 21.2, 1492.85)), ('hispaniola', 1492.95),
    ((-31.0, 37.5, 1493.15)), ('palos', 1493.2), ('barcelona', 1493.3)),
  G(1493, 1496, 'Second voyage', ('cadiz', 1493.73), ((-61.5, 16.2, 1493.85)), ('puerto_rico', 1493.88), ('hispaniola', 1493.92), ((-77.3, 18.1, 1494.4)),
    ('hispaniola', 1494.7), ('cadiz', 1496.45)),
  G(1498, 1500, 'Third voyage, sent home in chains', ('seville', 1498.4), ((-23.5, 14.9, 1498.55)), ('trinidad', 1498.6), ((-62.0, 10.5, 1498.62)),
    ('santo_domingo', 1498.65), ('cadiz', 1500.9)),
  G(1502, 1504, 'Fourth voyage', ('cadiz', 1502.3), ('santo_domingo', 1502.5), ((-86.0, 16.0, 1502.6)), ((-79.9, 9.3, 1502.9)), ((-77.3, 18.5, 1503.5)),
    ((-77.3, 18.5, 1504.5)), ('seville', 1504.85)),
  G(1505, 1506, 'Last years', 'valladolid'))
P('Vasco da Gama', 'Portuguese explorer', (1469, 1524), 1, 'explore',
  'First to sail from Europe round Africa to India, opening the sea route to the spice trade.',
  G(1497, 1499, 'Voyage to India', ('lisbon', 1497.52), ((-23.5, 14.9, 1497.6)), ((18.0, -32.7, 1497.85)), ('cape_good_hope', 1497.88), ((32.0, -29.0, 1497.98)),
    ('mozambique_island', 1498.2), ('mombasa', 1498.27), ('malindi', 1498.3), ('calicut', 1498.39), ('malindi', 1499.02), ('cape_good_hope', 1499.2), ('lisbon', 1499.6)),
  G(1502, 1503, 'Second voyage', 'lisbon', 'calicut', 'cochin', 'lisbon'), G(1524, 1524, 'Viceroy of India', 'goa', 'cochin'))
P('Pedro Álvares Cabral', 'Portuguese explorer', (1467, 1520), 3, 'explore',
  'Landed in Brazil in 1500 on his way to India, claiming it for Portugal.',
  G(1500, 1501, 'Brazil and India', ('lisbon', 1500.2), ('porto_seguro', 1500.31), ('cape_good_hope', 1500.4), ('calicut', 1500.7), ('cochin', 1500.95), ('lisbon', 1501.5)))
P('Amerigo Vespucci', 'Italian explorer', (1454, 1512), 3, 'explore',
  'Realised that the lands Columbus found were a New World; America is named after him.',
  G(1501, 1502, 'Voyage along South America', 'lisbon', (-35.0, -5.0), 'rio', (-58.0, -36.0), 'lisbon'))
P('Afonso de Albuquerque', 'Portuguese conqueror', (1453, 1515), 2, 'war explore',
  "Took Goa, Malacca and Hormuz to build Portugal's empire of sea forts in the Indian Ocean.",
  G(1506, 1515, 'Conquests in the Indian Ocean', (53.85, 12.5), 'hormuz', ('goa', 1510.9), ('malacca', 1511.6), ('goa', 1512.5), 'aden', ('hormuz', 1515.3), ('goa', 1515.9)))
P('Leonardo da Vinci', 'Italian painter, engineer and inventor', (1452, 1519), 1, 'art mind',
  'Painted the Mona Lisa and the Last Supper and filled notebooks with flying machines, anatomy and engineering.',
  G(1466, 1481, 'Florence', 'florence'), G(1482, 1499, 'Milan', 'milan'), G(1500, 1505, 'Venice and Florence', 'venice', 'florence'),
  G(1506, 1512, 'Milan', 'milan'), G(1513, 1515, 'Rome', 'rome'), G(1516, 1519, 'Amboise', (0.98, 47.41)))
P('Niccolò Machiavelli', 'Florentine diplomat and writer', (1469, 1527), 2, 'mind',
  'Wrote The Prince, a cold guide to winning and keeping power.',
  G(1498, 1527, 'Florence', 'florence'))
P('Desiderius Erasmus', 'Dutch humanist scholar', (1466, 1536), 2, 'mind faith',
  "The prince of humanists: edited the Greek New Testament and mocked church abuses in In Praise of Folly.",
  G(1499, 1514, 'England and Italy', 'cambridge', 'venice', 'rome', 'london'), G(1514, 1529, 'Louvain and Basel', (4.7, 50.88), 'basel'),
  G(1529, 1536, 'Freiburg and Basel', (7.85, 47.99), 'basel'), wiki='Erasmus')
P('Michelangelo', 'Italian sculptor and painter', (1475, 1564), 1, 'art',
  "Carved David, painted the Sistine Chapel ceiling and designed the dome of St Peter's.",
  G(1488, 1504, 'Florence, carves David', 'florence'), G(1505, 1515, 'Rome, the Sistine Chapel', 'rome'),
  G(1516, 1533, 'Florence', 'florence'), G(1534, 1564, "Rome, St Peter's", 'rome'))
P('Raphael', 'Italian painter', (1483, 1520), 3, 'art',
  "Painted the School of Athens in the Pope's apartments.",
  G(1508, 1520, 'Painter in Rome', 'rome'))
P('Nicolaus Copernicus', 'Polish astronomer', (1473, 1543), 1, 'mind',
  'Put the Sun, not the Earth, at the centre of the universe.',
  G(1497, 1503, 'Studies in Italy', 'bologna', 'padua'), G(1510, 1543, 'Canon at Frombork', (19.69, 54.36)))
P('Askia Muhammad I', 'Emperor of Songhai', (1443, 1538), 2, 'rule faith',
  'Brought Songhai to its height and made Timbuktu a great centre of Islamic learning.',
  G(1496, 1497, 'Pilgrimage to Mecca', 'gao', 'cairo', 'mecca', 'gao'), R(1493, 1528, 'Askia of Songhai', 'Songhai', at='gao'), wiki='Askia Muhammad I')
P('Guru Nanak', 'Founder of Sikhism', (1469, 1539), 2, 'faith',
  "Taught that 'there is no Hindu, there is no Muslim', only one God, and travelled widely to preach it.",
  G(1469, 1499, 'Youth at Talwandi', (73.69, 31.45)),
  G(1500, 1524, 'Journeys of teaching', ((75.2, 31.2, 1500)), ('delhi', 1502), ('varanasi', 1504), ((86.0, 23.0, 1506)), ('puri', 1508), ('colombo', 1512),
    ((79.49, 30.74, 1516)), ('mecca', 1518), ('baghdad', 1519.5), ('kabul', 1521)),
  G(1525, 1539, 'Kartarpur', 'kartarpur'))
P('Martin Luther', 'Leader of the Protestant Reformation', (1483, 1546), 1, 'faith reform',
  "Nailed up 95 theses against the sale of indulgences in 1517, defied the emperor at Worms and translated the Bible into German.",
  G(1505, 1511, 'Monk at Erfurt', (11.03, 50.98)), G(1512, 1546, 'Professor at Wittenberg', 'wittenberg'),
  G(1521, 1522, 'Worms and the Wartburg', 'worms', 'wartburg', 'wittenberg'))
P('Huldrych Zwingli', 'Swiss reformer', (1484, 1531), 3, 'faith reform',
  "Led the Reformation in Zürich and died in battle against the Catholic cantons.",
  G(1519, 1531, 'Reformer of Zürich', 'zurich'))
P('Selim I', 'Ottoman sultan', (1470, 1520), 2, 'rule war',
  'Beat Safavid Persia at Chaldiran and conquered Syria and Egypt from the Mamluks.',
  G(1514, 1514, 'Battle of Chaldiran', 'constantinople', 'ankara', (44.0, 39.1)),
  G(1516, 1517, 'Conquest of Syria and Egypt', (37.2, 36.5), 'damascus', 'gaza', 'cairo'),
  R(1512, 1520, 'Ottoman sultan', *OTT, at='constantinople'))
P('Ismail I', 'Founder of Safavid Iran', (1487, 1524), 2, 'rule faith',
  'Teenage warrior-mystic who conquered Iran and made it Shia.',
  G(1514, 1514, 'Battle of Chaldiran', 'tabriz', (44.0, 39.1)), R(1501, 1524, 'Shah of Iran', 'Safavid Empire', at='tabriz'))
P('Moctezuma II', 'Emperor of the Aztecs', (1466, 1520), 2, 'rule',
  'Ruled the Aztec Empire at its height and was taken hostage by Cortés in his own palace.',
  R(1502, 1520, 'Huey tlatoani of the Aztecs', 'Aztec Empire', at='tenochtitlan'))
P('Hernán Cortés', 'Spanish conquistador', (1485, 1547), 1, 'war explore',
  'With a few hundred Spaniards and many native allies, he brought down the Aztec Empire.',
  G(1519, 1521, 'Conquest of the Aztec Empire', ('havana', 1519.1), ((-86.9, 20.5, 1519.2)), ((-92.9, 18.4, 1519.25)), ('veracruz', 1519.3),
    ('tlaxcala', 1519.7), ('cholula', 1519.8), ('tenochtitlan', 1519.85), ('tenochtitlan', 1520.5), ('tlaxcala', 1520.6), ('tenochtitlan', 1521.4), ('tenochtitlan', 1521.6)),
  G(1522, 1528, 'Governor of New Spain', 'mexico_city'))
P('La Malinche', "Cortés's interpreter", (1500, 1529), 3, 'explore',
  'Nahua woman given to the Spaniards who became their interpreter and adviser in the conquest.',
  G(1519, 1521, 'Interpreter for Cortés', 'veracruz', 'tlaxcala', 'tenochtitlan'))
P('Cuauhtémoc', 'Last Aztec emperor', (1497, 1525), 3, 'rule war',
  'Led the last defence of Tenochtitlan and was hanged by Cortés.',
  G(1520, 1521, 'Defence of Tenochtitlan', 'tenochtitlan'))
P('Ferdinand Magellan', 'Portuguese explorer for Spain', (1480, 1521), 1, 'explore',
  'Led the first voyage round the world; killed in the Philippines, but his ship made it home.',
  G(1519, 1521, 'Voyage round the world', ('seville', 1519.6), ((-16.25, 28.47, 1519.75)), ('rio', 1519.95), ((-58.0, -35.0, 1520.05)), ((-67.7, -49.3, 1520.25)),
    ('strait_magellan', 1520.82), ((-80.0, -35.0, 1520.95)), ((-110.0, -15.0, 1521.05)), ('guam', 1521.18), ('cebu', 1521.3), ('mactan', 1521.32)))
P('Juan Sebastián Elcano', 'Basque navigator', (1476, 1526), 3, 'explore',
  "Took over Magellan's last ship and brought it home: the first voyage round the world.",
  G(1521, 1522, 'Completes the circumnavigation', ('cebu', 1521.4), ((127.4, 0.68, 1521.85)), ((125.0, -8.5, 1522.05)), ((20.0, -36.0, 1522.4)),
    ((-23.5, 14.9, 1522.55)), ('seville', 1522.7)))
P('Charles V, Holy Roman Emperor', 'King of Spain and Holy Roman Emperor', (1500, 1558), 1, 'rule',
  'Ruled Spain, the Netherlands, Austria, much of Italy and the Americas; faced Luther, the Ottomans and France.',
  G(1521, 1521, 'Diet of Worms', 'valladolid', 'aachen', 'worms'), G(1556, 1558, 'Retirement at Yuste', (-5.74, 40.11)),
  R(1516, 1556, 'King of Spain, Holy Roman Emperor', *SPAIN, *HRE, at='valladolid'))
P('Suleiman the Magnificent', 'Ottoman sultan', (1494, 1566), 1, 'rule war',
  'Took Belgrade, crushed Hungary at Mohács, besieged Vienna, and gave the empire its laws.',
  G(1526, 1526, 'Battle of Mohács', 'constantinople', 'belgrade', 'mohacs', 'budapest'),
  G(1529, 1529, 'Siege of Vienna', 'constantinople', 'belgrade', 'vienna'), G(1566, 1566, 'Death at Szigetvár', 'belgrade', (17.8, 46.05)),
  R(1520, 1566, 'Ottoman sultan', *OTT, at='constantinople'))
P('Hürrem Sultan', 'Wife of Suleiman the Magnificent', (1502, 1558), 3, 'rule',
  "Roxelana: a Ruthenian slave who became Suleiman's wife and the most powerful woman in the empire.",
  G(1534, 1558, 'Empress at Constantinople', 'constantinople'))
P('Hayreddin Barbarossa', 'Ottoman admiral', (1478, 1546), 2, 'war',
  'Corsair of Algiers who became grand admiral of the Ottoman fleet and ruled the Mediterranean.',
  G(1516, 1532, 'Corsair king of Algiers', 'algiers'), G(1533, 1546, 'Grand admiral', 'constantinople', 'tunis', (20.75, 38.95), 'nice', 'constantinople'))
P('Babur', 'Founder of the Mughal Empire', (1483, 1530), 2, 'rule war',
  'Descendant of Timur and Genghis Khan who won north India at Panipat in 1526.',
  G(1504, 1525, 'King of Kabul', 'kabul'), G(1526, 1526, 'Battle of Panipat', 'kabul', 'lahore', 'panipat', 'agra'),
  R(1527, 1530, 'Mughal emperor', 'Mughal Empire', at='agra'))
P('Afonso I of Kongo', 'King of Kongo', (1456, 1543), 3, 'rule faith',
  'Made Kongo Christian and wrote to the king of Portugal to protest against the slave trade.',
  R(1509, 1543, 'King of Kongo', 'Congo', at='mbanza_kongo'))
P('Krishnadevaraya', 'Emperor of Vijayanagara', (1471, 1529), 3, 'rule',
  'Ruled the south Indian Vijayanagara empire at its richest.',
  R(1509, 1529, 'Emperor of Vijayanagara', 'Vijayanagara', at='hampi'))
P('Francisco Pizarro', 'Spanish conquistador', (1478, 1541), 1, 'war explore',
  "Captured the Inca emperor Atahualpa at Cajamarca and conquered the Inca Empire.",
  G(1524, 1528, 'Voyages down the Pacific coast', 'panama', 'tumbes', 'panama'),
  G(1531, 1533, 'Conquest of the Inca Empire', ('panama', 1531.05), ('tumbes', 1532.3), ('cajamarca', 1532.87), ('cajamarca', 1533.6), ('cuzco', 1533.88)),
  G(1535, 1541, 'Founder of Lima', 'lima'))
P('Atahualpa', 'Last Sapa Inca', (1502, 1533), 2, 'rule',
  'Won the Inca civil war against his brother, then was captured and killed by Pizarro.',
  G(1529, 1531, 'War with Huáscar', 'quito', 'cuzco'), G(1532, 1533, 'Captive at Cajamarca', 'cajamarca'))
P('Huayna Capac', 'Sapa Inca', (1464, 1527), 3, 'rule',
  'Took the Inca Empire to its greatest size; died of smallpox before the Spanish even arrived.',
  R(1493, 1527, 'Sapa Inca', 'Inca Empire', at='cuzco'))
P('Ignatius of Loyola', 'Founder of the Jesuits', (1491, 1556), 2, 'faith',
  'Soldier turned priest who founded the Society of Jesus, the shock troops of the Counter-Reformation.',
  G(1528, 1535, 'Student in Paris', 'paris'), G(1537, 1556, 'Founds the Jesuits in Rome', 'venice', 'rome'))
P('John Calvin', 'Protestant reformer', (1509, 1564), 2, 'faith reform',
  'Made Geneva the citadel of Reformed Protestantism, whose ideas spread to Scotland, the Netherlands and New England.',
  G(1536, 1538, 'Geneva', 'paris', 'geneva'), G(1538, 1541, 'Strasbourg', (7.75, 48.58)), G(1541, 1564, 'Leader of Geneva', 'geneva'))
P('Henry VIII', 'King of England', (1491, 1547), 1, 'rule',
  'Broke with Rome to divorce Catherine of Aragon, married six times and closed the monasteries.',
  R(1509, 1547, 'King of England', *ENG, at='london'))
P('Francis Xavier', 'Jesuit missionary', (1506, 1552), 2, 'faith explore',
  'Carried Christianity to India, the Spice Islands and Japan and died trying to enter China.',
  G(1541, 1552, 'Mission to Asia', ('lisbon', 1541.3), ('mozambique_island', 1541.7), ('goa', 1542.4), ((77.5, 8.3, 1543)), ('malacca', 1545.8),
    ('ternate', 1546.6), ('malacca', 1547.6), ('goa', 1548.1), ('kagoshima', 1549.6), ('kyoto', 1551), ('goa', 1552.1), ((112.8, 21.7, 1552.9))))
P('Sher Shah Suri', 'Emperor of north India', (1486, 1545), 3, 'rule reform',
  'Drove out the Mughals for fifteen years and built the Grand Trunk Road and the rupee.',
  G(1540, 1545, 'Emperor of Hindustan', 'delhi', (84.03, 24.95)))
P('Ahmad ibn Ibrahim al-Ghazi', 'Imam of Adal', (1506, 1543), 3, 'war',
  "Called Gran, 'the left-handed': nearly conquered Christian Ethiopia before dying in battle.",
  G(1529, 1543, 'Conquest of Ethiopia', 'harar', (38.5, 9.3), 'axum', (37.5, 12.0)))
P('Pedro de Valdivia', 'Spanish conquistador', (1497, 1553), 3, 'war explore',
  'Founded Santiago de Chile and was killed by the Mapuche under Lautaro.',
  G(1540, 1553, 'Conquest of Chile', 'cuzco', (-69.0, -23.0), 'santiago', (-73.05, -36.82)))
P('Bartolomé de las Casas', 'Spanish friar', (1484, 1566), 3, 'faith reform',
  "Former settler who spent fifty years denouncing the cruelty of the conquest of the Americas.",
  G(1502, 1547, 'Defender of the Indians', 'santo_domingo', 'havana', (-92.6, 16.7), 'valladolid'))
P('Jacques Cartier', 'French explorer', (1491, 1557), 3, 'explore',
  "Sailed up the St Lawrence and claimed Canada for France.",
  G(1534, 1542, 'Voyages up the St Lawrence', (-2.02, 48.65), 'newfoundland', 'quebec', 'montreal', (-2.02, 48.65)))
P('Ivan the Terrible', 'First tsar of Russia', (1530, 1584), 2, 'rule war',
  'Crowned the first tsar, conquered Kazan and Astrakhan, and turned on his own people in the Oprichnina terror.',
  G(1552, 1552, 'Conquest of Kazan', 'moscow', 'kazan'), R(1547, 1584, 'Tsar of Russia', 'Tsardom of Muscovy', at='moscow'))
P('Akbar', 'Mughal emperor', (1542, 1605), 1, 'rule',
  'Built the Mughal Empire across north India and invited Hindus, Muslims, Jains and Christians to debate at his court.',
  G(1571, 1585, 'Court at Fatehpur Sikri', 'fatehpur_sikri'), R(1556, 1605, 'Mughal emperor', 'Mughal Empire', at='agra'))
P('Mimar Sinan', 'Ottoman architect', (1490, 1588), 3, 'art',
  "Built more than 300 buildings, including the great mosques of Istanbul and Edirne.",
  G(1539, 1588, 'Chief architect of the empire', 'constantinople', 'edirne', 'constantinople'))
P('Philip II of Spain', 'King of Spain', (1527, 1598), 1, 'rule',
  "Ruled the first empire on which the sun never set; sent the Armada against England.",
  R(1556, 1598, 'King of Spain and Portugal', *SPAIN, at='madrid'))
P('Elizabeth I', 'Queen of England', (1533, 1603), 1, 'rule',
  "Kept England Protestant, beat the Spanish Armada and gave her name to an age of Shakespeare and sea dogs.",
  R(1558, 1603, 'Queen of England', *ENG, at='london'))
P('Mary, Queen of Scots', 'Queen of Scotland', (1542, 1587), 3, 'rule',
  "Catholic queen forced to abdicate, held captive in England for 19 years and executed by Elizabeth.",
  R(1561, 1567, 'Queen of Scots', 'Scotland', at='edinburgh'), G(1568, 1587, 'Captive in England', (-1.6, 53.3), (-0.45, 52.53)))
P('William the Silent', 'Leader of the Dutch Revolt', (1533, 1584), 2, 'war rule',
  'Led the Dutch revolt against Spain and was shot by an assassin at Delft.',
  G(1568, 1584, 'Leader of the Dutch Revolt', (8.3, 50.73), 'brussels', 'delft'))
P('Don John of Austria', 'Spanish commander', (1547, 1578), 3, 'war',
  "Led the Holy League's fleet to victory over the Ottomans at Lepanto in 1571.",
  G(1571, 1571, 'Battle of Lepanto', (15.55, 38.19), (21.0, 38.3)))
P('Miguel de Cervantes', 'Spanish novelist', (1547, 1616), 2, 'art',
  'Wounded at Lepanto, five years a captive in Algiers, he wrote Don Quixote, the first modern novel.',
  G(1571, 1571, 'Battle of Lepanto', (21.0, 38.3)), G(1575, 1580, 'Captive in Algiers', 'algiers'), G(1581, 1616, 'Writer in Spain', 'seville', 'valladolid', 'madrid'))
P('Catherine de\' Medici', 'Queen and regent of France', (1519, 1589), 3, 'rule',
  "Ruled through three sons during the Wars of Religion and the St Bartholomew's Day massacre.",
  G(1547, 1589, 'Queen of France, then queen mother', 'paris'))
P('Henry IV of France', 'King of France', (1553, 1610), 2, 'rule',
  "Protestant king who turned Catholic ('Paris is well worth a Mass') and gave Huguenots freedom by the Edict of Nantes.",
  R(1589, 1610, 'King of France', *FRA, at='paris'))
P('Francis Drake', 'English sea captain', (1540, 1596), 2, 'explore war',
  'Raided Spanish treasure, sailed round the world and helped beat the Armada.',
  G(1577, 1580, 'Voyage round the world', ('plymouth', 1577.95), ((-23.5, 14.9, 1578.05)), ((-67.7, -49.3, 1578.5)), ('strait_magellan', 1578.7),
    ('valparaiso', 1578.92), ('callao', 1579.1), ((-123.0, 38.0, 1579.5)), ('ternate', 1579.9), ('cape_good_hope', 1580.45), ('plymouth', 1580.74)),
  G(1588, 1588, 'Defeat of the Armada', 'plymouth', (-2.0, 50.4), (2.13, 50.99)))
P('Yi Sun-sin', 'Korean admiral', (1545, 1598), 2, 'war',
  'Never lost a sea battle; his turtle ships cut the supply line of the Japanese invasion of Korea.',
  G(1592, 1598, 'War against the Japanese invasion', 'hansan', 'myeongnyang', (127.9, 34.95)))
P('Oda Nobunaga', 'Japanese warlord', (1534, 1582), 2, 'war rule',
  'First of the three unifiers of Japan, master of the musket, killed by his own general.',
  G(1560, 1582, 'Unifier of Japan', (136.91, 35.18), (136.76, 35.42), 'kyoto', (136.09, 35.15)))
P('Toyotomi Hideyoshi', 'Ruler of Japan', (1537, 1598), 2, 'rule war',
  "Peasant's son who finished unifying Japan and twice invaded Korea.",
  R(1585, 1598, 'Ruler of Japan', 'Japan (Warring States)', at='osaka'))
P('Tokugawa Ieyasu', 'First Tokugawa shogun', (1543, 1616), 2, 'rule war',
  "Won at Sekigahara in 1600 and founded the shogunate that ruled a peaceful, closed Japan for 250 years.",
  G(1600, 1600, 'Battle of Sekigahara', 'edo', 'sekigahara'),
  R(1603, 1616, 'Shogun', 'Tokugawa shogunate', 'Japan (Warring States)', at='edo'))
P('Shah Abbas I', 'Shah of Iran', (1571, 1629), 2, 'rule',
  'Took back land from the Ottomans and made Isfahan one of the most beautiful cities in the world.',
  R(1588, 1629, 'Shah of Iran', 'Safavid Empire', at='isfahan'), wiki='Abbas the Great')
P('Matteo Ricci', 'Jesuit missionary in China', (1552, 1610), 2, 'faith mind',
  'Learned Chinese, dressed as a Confucian scholar and brought European maths and maps to the Ming court.',
  G(1582, 1610, 'Jesuit in China', 'macau', (112.47, 23.05), 'nanchang', 'nanjing', 'beijing'))
P('Yermak Timofeyevich', 'Cossack leader', (1532, 1585), 3, 'war explore',
  'Led the Cossacks who conquered the Khanate of Sibir and opened Siberia to Russia.',
  G(1581, 1585, 'Conquest of Siberia', (56.2, 58.0), (65.53, 57.15), 'tobolsk', (69.0, 57.4)))
P('Sonam Gyatso', '3rd Dalai Lama', (1543, 1588), 3, 'faith',
  'Given the title Dalai Lama by the Mongol Altan Khan, converting the Mongols to Tibetan Buddhism.',
  G(1578, 1588, 'Mission to the Mongols', 'lhasa', (100.2, 36.9), (111.65, 40.82)), wiki='Sonam Gyatso, 3rd Dalai Lama')
P('Tycho Brahe', 'Danish astronomer', (1546, 1601), 3, 'mind',
  'Measured the stars and planets more precisely than anyone before the telescope.',
  G(1576, 1597, 'Observatory on Hven', (12.69, 55.91)), G(1599, 1601, 'Prague', 'prague'))
P('William Shakespeare', 'English playwright and poet', (1564, 1616), 1, 'art',
  "The greatest writer in English: Hamlet, Macbeth, King Lear and 34 more plays for the Globe theatre.",
  G(1564, 1586, 'Stratford', 'stratford'), G(1587, 1612, 'Playwright in London', 'london'), G(1613, 1616, 'Stratford', 'stratford'))
P('Galileo Galilei', 'Italian astronomer and physicist', (1564, 1642), 1, 'mind',
  'Turned a telescope on the sky, found the moons of Jupiter and was tried by the Inquisition for saying the Earth moves.',
  G(1589, 1591, 'Pisa', 'pisa'), G(1592, 1609, 'Padua', 'padua'), G(1610, 1632, 'Florence', 'florence'),
  G(1633, 1633, 'Trial in Rome', 'florence', 'rome'), G(1634, 1642, 'House arrest at Arcetri', (11.25, 43.75)))
P('Johannes Kepler', 'German astronomer', (1571, 1630), 2, 'mind',
  'Found that the planets move in ellipses, laying the ground for Newton.',
  G(1600, 1611, 'Imperial mathematician at Prague', 'prague'), G(1612, 1626, 'Linz', (14.29, 48.31)))
P('Naresuan', 'King of Ayutthaya', (1555, 1605), 3, 'rule war',
  'Freed Siam from Burmese rule and killed the Burmese crown prince in an elephant duel.',
  R(1590, 1605, 'King of Ayutthaya', 'Ayutthaya', at='ayutthaya'))
P('Samuel de Champlain', 'French explorer', (1567, 1635), 3, 'explore',
  "Founded Quebec in 1608 and the colony of New France.",
  G(1608, 1635, 'Founder of Quebec', 'quebec', 'montreal', 'quebec'))
P('Henry Hudson', 'English explorer', (1565, 1611), 3, 'explore',
  'Explored the river and the bay that bear his name, and was cast adrift by his mutinous crew.',
  G(1609, 1609, 'Hudson River voyage', 'amsterdam', 'new_york', (-73.9, 42.6)), G(1610, 1611, 'Hudson Bay', 'london', (-60.0, 61.0), 'hudson_bay'))
P('Pocahontas', 'Powhatan woman', (1596, 1617), 3, 'explore',
  'Daughter of the Powhatan chief who married the colonist John Rolfe and died on a visit to England.',
  G(1607, 1615, 'Virginia', (-76.9, 37.4), 'jamestown'), G(1616, 1617, 'Visit to England', 'london'))
P('Nurhaci', 'Founder of the Manchu state', (1559, 1626), 2, 'rule war',
  'United the Jurchen tribes into the Manchu nation and challenged the Ming.',
  G(1616, 1626, 'Khan of the Later Jin', (124.9, 41.7), 'shenyang'))
P('Hong Taiji', 'Qing emperor', (1592, 1643), 3, 'rule war',
  'Named his people the Manchus and his state the Qing, and forced Korea to submit in 1637.',
  G(1636, 1637, 'Invasion of Korea', 'shenyang', 'seoul', 'shenyang'), G(1626, 1643, 'Khan, then emperor of the Qing', 'shenyang'))
P('Jahangir', 'Mughal emperor', (1569, 1627), 3, 'rule art',
  "Akbar's son, a lover of painting and gardens who left much of the ruling to his wife Nur Jahan.",
  R(1605, 1627, 'Mughal emperor', 'Mughal Empire', at='lahore'))
P('Shah Jahan', 'Mughal emperor', (1592, 1666), 2, 'rule art',
  "Built the Taj Mahal for his wife Mumtaz Mahal, then was locked up by his son in Agra Fort.",
  R(1628, 1658, 'Mughal emperor', 'Mughal Empire', at='agra'), G(1659, 1666, 'Prisoner in Agra Fort', 'agra'))
P('Cardinal Richelieu', 'Chief minister of France', (1585, 1642), 2, 'rule',
  "Louis XIII's red-robed minister who broke the Huguenots and the nobles and fought the Habsburgs.",
  R(1624, 1642, 'Chief minister of France', *FRA, at='paris'))
P('Gustavus Adolphus', 'King of Sweden', (1594, 1632), 2, 'rule war',
  "'The Lion of the North': saved the Protestant cause in the Thirty Years War and died at Lützen.",
  G(1630, 1632, 'Thirty Years War in Germany', ((13.82, 54.1, 1630.5)), ('berlin', 1631.3), ('breitenfeld', 1631.7), ('munich', 1632.4), ('nuremberg', 1632.6), ('lutzen', 1632.85)),
  R(1611, 1632, 'King of Sweden', 'Sweden', at='stockholm'))
P('Albrecht von Wallenstein', 'Imperial generalissimo', (1583, 1634), 3, 'war',
  "Raised huge armies for the emperor in the Thirty Years War and was murdered on his orders.",
  G(1625, 1634, 'Imperial commander', 'prague', 'lutzen', (12.38, 50.08)))
P('Charles I of England', 'King of England, Scotland and Ireland', (1600, 1649), 2, 'rule',
  'Fought Parliament in the English Civil War, lost, and was beheaded in 1649.',
  R(1625, 1649, 'King of England, Scotland and Ireland', *ENG, at='london'))
P('Abel Tasman', 'Dutch explorer', (1603, 1659), 3, 'explore',
  'First European to reach Tasmania, New Zealand and Fiji.',
  G(1642, 1643, 'Voyage to Tasmania and New Zealand', 'batavia', (57.5, -20.2), (147.0, -42.8), (172.0, -40.8), 'tonga', 'fiji', 'batavia'))
P('Chongzhen Emperor', 'Last Ming emperor', (1611, 1644), 3, 'rule',
  "Hanged himself on Coal Hill as rebels took Beijing in 1644.",
  R(1627, 1644, 'Emperor of Ming China', 'Ming Chinese Empire', at='beijing'))
P('Li Zicheng', 'Rebel leader', (1606, 1645), 3, 'war',
  "Peasant rebel who took Beijing in 1644 and ended the Ming, only to be driven out by the Manchus weeks later.",
  G(1630, 1645, 'Rebellion and the fall of Beijing', ((109.0, 37.0, 1630)), ('xian', 1643.8), ('beijing', 1644.3), ('xian', 1644.8), ((114.3, 29.7, 1645.3))))
P('Nzinga of Ndongo and Matamba', 'Queen of Ndongo and Matamba', (1583, 1663), 2, 'rule war',
  'Outwitted Portuguese governors and fought them for thirty years to keep her kingdoms free.',
  G(1622, 1622, 'Envoy to Luanda', (15.5, -9.0), 'luanda'), G(1624, 1663, 'Queen of Ndongo and Matamba', (15.5, -9.0), (16.5, -9.5)))

"""Heads of state of central, northern and eastern Europe between the famous ones in the era files: the Holy Roman
Empire and Austria, Prussia and Germany, Hungary, Poland and Lithuania, Scandinavia, Russia, Byzantium, the Balkans, Ireland."""
from _lib import P, R, G


def K(name, role, life, a, b, why, *names, at, rank=3, tags='rule', wiki=None):
    """one reign: the ruler sits by the first of `names` on the map from year a to b, or at `at` when none is"""
    P(name, role, life, rank, tags, why, R(a, b, role, *names, at=at), wiki=wiki)


HRE = ('Holy Roman Empire', 'East Francia')
AUS = ('Austrian Empire', 'Holy Roman Empire', 'Austria Hungary', 'Austro-Hungarian Empire', 'Austria')
DE = ('Germany', 'German Empire')
HU = ('Hungary', 'Kingdom of Hungary', 'Imperial Hungary')
PL = ('Poland', 'Poland-Lithuania', 'Polish–Lithuanian Commonwealth')
SWE = ('Sweden', 'Sweden–Norway', 'Kalmar Union')
DEN = ('Denmark', 'Denmark-Norway', 'Kalmar Union')
MOS = ('Grand Duchy of Moscow', 'Tsardom of Muscovy', 'Principality of Vladimir-Suzdal')
RUS = ('Russian Empire', 'Tsardom of Muscovy')
BYZ = ('Byzantine Empire', 'Eastern Roman Empire')
EMP, KH, KPL, KSW, KDK = 'Holy Roman Emperor', 'King of Hungary', 'King of Poland', 'King of Sweden', 'King of Denmark'
CH = 'Chancellor of Germany'

# ---------- the Holy Roman Empire and Austria ----------
P('Otto III, Holy Roman Emperor', EMP, (980, 1002), 3, 'rule',
  'Became king at three and dreamed of ruling a reborn Roman Empire from Rome itself.',
  R(983, 1002, EMP, *HRE, at='aachen'), G(998, 1001, 'Ruling from Rome', 'rome'))
K('Henry II, Holy Roman Emperor', EMP, (973, 1024), 1002, 1024,
  'Last of the Saxon emperors, a pious king later made a saint, who founded the bishopric of Bamberg.', *HRE, at='aachen', tags='rule faith')
K('Conrad II, Holy Roman Emperor', EMP, (990, 1039), 1024, 1039,
  'First Salian emperor, who added the Kingdom of Burgundy to the empire.', *HRE, at='speyer')
K('Henry III, Holy Roman Emperor', EMP, (1017, 1056), 1039, 1056,
  'At the height of imperial power he deposed three rival popes at Sutri in 1046.', *HRE, at='speyer')
K('Henry V, Holy Roman Emperor', EMP, (1086, 1125), 1105, 1125,
  'Forced his own father off the throne and settled the long fight with the pope over bishops at Worms in 1122.', *HRE, at='speyer')
K('Lothair III, Holy Roman Emperor', EMP, (1075, 1137), 1125, 1137,
  'Duke of Saxony chosen king over the Hohenstaufens, who pushed German rule east of the Elbe.', *HRE, at='aachen')
K('Conrad III of Germany', 'King of Germany', (1093, 1152), 1138, 1152,
  'First Hohenstaufen king, who led the Germans on the failed Second Crusade.', *HRE, at='aachen')
K('Henry VI, Holy Roman Emperor', EMP, (1165, 1197), 1191, 1197,
  "Barbarossa's son, who held Richard the Lionheart for ransom and won the Kingdom of Sicily.", *HRE, at='aachen')
K('Otto IV, Holy Roman Emperor', EMP, (1175, 1218), 1209, 1215,
  'Welf emperor beaten by Philip II of France at Bouvines in 1214.', *HRE, at='aachen')
K('Rudolf I of Germany', 'King of Germany', (1218, 1291), 1273, 1291,
  'First Habsburg king, who ended twenty years without an emperor and won Austria for his family in 1278.', *HRE, at='vienna')
K('Louis IV, Holy Roman Emperor', EMP, (1282, 1347), 1314, 1347,
  'Ludwig the Bavarian, excommunicated by the pope, who had himself crowned in Rome in the name of the Roman people.', *HRE, at='munich')
K('Charles IV, Holy Roman Emperor', EMP, (1316, 1378), 1346, 1378,
  "King of Bohemia who made Prague the empire's capital, founded its university and fixed how emperors are chosen in the Golden Bull.",
  *HRE, at='prague', rank=2)
P('Sigismund, Holy Roman Emperor', EMP, (1368, 1437), 3, 'rule',
  'King of Hungary and emperor, who called the Council of Constance that ended the papal schism and burned Jan Hus.',
  R(1387, 1410, KH, *HU, at='budapest'), R(1411, 1437, 'King of Germany, then emperor', *HRE, at='prague'))
K('Frederick III, Holy Roman Emperor', EMP, (1415, 1493), 1440, 1493,
  'Reigned 53 years and married his son Maximilian to the heiress of Burgundy, the start of Habsburg greatness.', *HRE, at='vienna')
K('Maximilian I, Holy Roman Emperor', EMP, (1459, 1519), 1493, 1519,
  "'The last knight', who built the Habsburg empire by marriages: Burgundy for himself and Spain for his son.", *HRE, at='vienna', rank=2)
K('Ferdinand I, Holy Roman Emperor', EMP, (1503, 1564), 1556, 1564,
  'Brother of Charles V, who won Bohemia and Hungary in 1526 and took over the empire in 1556.', *HRE, at='vienna')
K('Maximilian II, Holy Roman Emperor', EMP, (1527, 1576), 1564, 1576,
  'Tolerant emperor who let the Protestants of Austria worship in peace.', *HRE, at='vienna')
K('Rudolf II, Holy Roman Emperor', EMP, (1552, 1612), 1576, 1612,
  'Eccentric emperor who filled Prague with alchemists, artists and astronomers, among them Tycho Brahe and Kepler.', *HRE, at='prague',
  tags='rule mind')
K('Matthias, Holy Roman Emperor', EMP, (1557, 1619), 1612, 1619,
  "Pushed his brother Rudolf aside; his reign ended with the Defenestration of Prague that began the Thirty Years' War.", *HRE, at='vienna')
K('Ferdinand II, Holy Roman Emperor', EMP, (1578, 1637), 1619, 1637,
  "Fervent Catholic whose crushing of the Bohemian Protestants set off the Thirty Years' War.", *HRE, at='vienna', tags='rule faith')
K('Ferdinand III, Holy Roman Emperor', EMP, (1608, 1657), 1637, 1657,
  "Ended the Thirty Years' War with the Peace of Westphalia in 1648.", *HRE, at='vienna')
K('Leopold I, Holy Roman Emperor', EMP, (1640, 1705), 1658, 1705,
  'Emperor during the Turkish siege of Vienna in 1683, after which his armies won back Hungary.', *AUS, at='vienna')
K('Joseph I, Holy Roman Emperor', EMP, (1678, 1711), 1705, 1711,
  'Fought Louis XIV in the War of the Spanish Succession.', *AUS, at='vienna')
K('Charles VI, Holy Roman Emperor', EMP, (1685, 1740), 1711, 1740,
  'Spent his reign getting Europe to agree that his daughter Maria Theresa could inherit.', *AUS, at='vienna')
K('Leopold II, Holy Roman Emperor', EMP, (1747, 1792), 1790, 1792,
  "Brother of Marie Antoinette, who warned revolutionary France with the Declaration of Pillnitz.", *AUS, at='vienna')
K('Francis II, Holy Roman Emperor', 'Last Holy Roman Emperor, first emperor of Austria', (1768, 1835), 1792, 1835,
  'Lost to Napoleon at Austerlitz, ended the Holy Roman Empire in 1806 and married his daughter to Napoleon.', *AUS, at='vienna', rank=2)
K('Ferdinand I of Austria', 'Emperor of Austria', (1793, 1875), 1835, 1848,
  'Gentle, epileptic emperor who left the ruling to Metternich and gave up the throne in the revolution of 1848.', *AUS, at='vienna')
K('Charles I of Austria', 'Emperor of Austria', (1887, 1922), 1916, 1918,
  'Last Habsburg emperor, who tried to make a secret peace in 1917 and lost his throne when the empire broke apart.', *AUS, at='vienna')
K('Engelbert Dollfuss', 'Chancellor of Austria', (1892, 1934), 1932, 1934,
  'Ruled Austria as a dictator and was murdered by Austrian Nazis in 1934.', 'Austria', at='vienna')

# ---------- Prussia and Germany ----------
K('The Great Elector', 'Elector of Brandenburg and Duke of Prussia', (1620, 1688), 1640, 1688,
  "Frederick William, who rebuilt Brandenburg-Prussia after the Thirty Years' War and took in Huguenots fleeing France.", 'Prussia', at='berlin',
  wiki='Frederick William, Elector of Brandenburg')
K('Frederick I of Prussia', 'King in Prussia', (1657, 1713), 1688, 1713,
  'Crowned himself the first King in Prussia in 1701.', 'Prussia', at='berlin')
K('Frederick William I of Prussia', 'King in Prussia', (1688, 1740), 1713, 1740,
  "The 'Soldier King', who built Prussia's army and collected a regiment of giant grenadiers.", 'Prussia', at='potsdam')
K('Frederick William II of Prussia', 'King of Prussia', (1744, 1797), 1786, 1797,
  'Took a large share of Poland when it was carved up in 1793 and 1795.', 'Prussia', at='berlin')
K('Frederick William III of Prussia', 'King of Prussia', (1770, 1840), 1797, 1840,
  'Crushed by Napoleon at Jena in 1806, he joined the coalition that beat him in 1813.', 'Prussia', at='berlin')
K('Frederick William IV of Prussia', 'King of Prussia', (1795, 1861), 1840, 1861,
  'Turned down the crown of a united Germany offered by the Frankfurt Parliament in 1849.', 'Prussia', at='berlin')
K('Friedrich Ebert', 'President of Germany', (1871, 1925), 1919, 1925,
  'Social Democrat and saddler by trade who became the first president of the Weimar Republic.', *DE, at='berlin')
P('Paul von Hindenburg', 'President of Germany', (1847, 1934), 2, 'war rule',
  "Field marshal who won at Tannenberg in 1914, ran Germany's war with Ludendorff, and as president made Hitler chancellor in 1933.",
  G(1914, 1918, 'At the head of the German army', ('tannenberg', 1914.65), ((18.95, 49.98, 1916.7)), ((18.95, 49.98, 1918.1)), ((5.86, 50.49, 1918.2)),
    ((5.86, 50.49, 1918.86))),
  R(1925, 1934, 'President of Germany', *DE, at='berlin'))
K('Gustav Stresemann', 'Foreign minister of Germany', (1878, 1929), 1923, 1929,
  'Ended the great inflation of 1923 and brought Germany back into Europe; Nobel Peace Prize in 1926.', *DE, at='berlin')
K('Walter Ulbricht', 'Leader of East Germany', (1893, 1973), 1950, 1971,
  'Communist leader of East Germany who built the Berlin Wall in 1961.', 'East Germany', 'Germany (Soviet)', at='berlin')
K('Erich Honecker', 'Leader of East Germany', (1912, 1994), 1971, 1989,
  "East Germany's last hardline leader, pushed out weeks before the Berlin Wall fell.", 'East Germany', at='berlin')
P('Willy Brandt', 'Chancellor of West Germany', (1913, 1992), 3, 'rule reform',
  'Mayor of West Berlin when the Wall went up, then chancellor who knelt at the Warsaw Ghetto memorial and made peace with the East.',
  G(1957, 1966, 'Mayor of West Berlin', 'berlin'), R(1969, 1974, 'Chancellor of West Germany', 'West Germany', 'Germany', at='bonn'))
K('Helmut Schmidt', 'Chancellor of West Germany', (1918, 2015), 1974, 1982,
  'Steered West Germany through the oil shocks and the terror of the Red Army Faction.', 'West Germany', 'Germany', at='bonn')
K('Gerhard Schröder', CH, (1944, None), 1998, 2005,
  'Reformed German welfare and kept Germany out of the Iraq war.', 'Germany', at='berlin')
K('Olaf Scholz', CH, (1958, None), 2021, 2025,
  "Chancellor who weaned Germany off Russian gas and rearmed it after Russia invaded Ukraine.", 'Germany', at='berlin')
K('Friedrich Merz', CH, (1955, None), 2025, 2026,
  'Christian Democrat chancellor since 2025.', 'Germany', at='berlin')

# ---------- Hungary ----------
K('Andrew II of Hungary', KH, (1177, 1235), 1205, 1235,
  "Issued the Golden Bull of 1222, Hungary's Magna Carta.", *HU, at='esztergom')
P('Béla IV of Hungary', KH, (1206, 1270), 3, 'rule',
  'Fled the Mongol invasion of 1241 to the Adriatic coast, then rebuilt Hungary with stone castles.',
  R(1235, 1270, KH, *HU, at='esztergom'),
  G(1241, 1242, 'Fleeing the Mongols', ((20.9, 47.98, 1241.28)), ('zagreb', 1241.6), ((16.25, 43.52, 1242.0)), ((16.25, 43.52, 1242.3)), ('esztergom', 1242.6)))
K('Charles I of Hungary', KH, (1288, 1342), 1308, 1342,
  "Angevin king who restored order after a civil war and opened Hungary's rich gold mines.", *HU, at='budapest')
K('Louis I of Hungary', 'King of Hungary and Poland', (1326, 1382), 1342, 1382,
  'Louis the Great, who ruled Hungary and, from 1370, Poland too.', *HU, at='budapest')
K('Matthias Corvinus', KH, (1443, 1490), 1458, 1490,
  'Renaissance king with a famous library and a standing Black Army, who took Vienna in 1485.', *HU, at='budapest', rank=2)
K('Louis II of Hungary', KH, (1506, 1526), 1516, 1526,
  'Drowned fleeing the Turks after Mohács in 1526, the battle that ended the medieval kingdom of Hungary.', *HU, at='budapest')
K('Miklós Horthy', 'Regent of Hungary', (1868, 1957), 1920, 1944,
  'Admiral who ruled landlocked Hungary as regent for a king who never came back, and sided with Hitler.', 'Hungary', at='budapest')
P('Imre Nagy', 'Prime minister of Hungary', (1896, 1958), 3, 'rule reform',
  'Communist reformer who led the 1956 revolution against Soviet rule and was hanged for it.',
  R(1953, 1955, 'Prime minister of Hungary', 'Hungary', at='budapest'), R(1956, 1956, 'Leader of the 1956 revolution', 'Hungary', at='budapest'))
K('János Kádár', 'Leader of Hungary', (1912, 1989), 1956, 1988,
  "Put in power by Soviet tanks in 1956, he later allowed a softer 'goulash communism'.", 'Hungary', at='budapest')
P('Viktor Orbán', 'Prime minister of Hungary', (1963, None), 3, 'rule',
  "Ruled Hungary as an 'illiberal democracy' for sixteen years until he lost the 2026 election.",
  R(1998, 2002, 'Prime minister of Hungary', 'Hungary', at='budapest'), R(2010, 2026, 'Prime minister of Hungary', 'Hungary', at='budapest'))
K('Péter Magyar', 'Prime minister of Hungary', (1981, None), 2026, 2026,
  'Former insider of Orbán\'s party who beat him in a landslide in April 2026.', 'Hungary', at='budapest')

# ---------- Poland and Lithuania ----------
K('Bolesław III Wrymouth', 'Duke of Poland', (1086, 1138), 1107, 1138,
  'Split Poland among his sons in his will, starting two centuries of division.', *PL, at='krakow')
K('Casimir III the Great', KPL, (1310, 1370), 1333, 1370,
  "Found Poland made of wood and left it of stone, as the saying goes; welcomed Jews and founded Kraków's university.", *PL, at='krakow', rank=2)
K('Jadwiga of Poland', KPL, (1374, 1399), 1384, 1399,
  'Girl crowned king of Poland, who married Jogaila of Lithuania and joined the two lands; later made a saint.', *PL, at='krakow',
  tags='rule faith')
K('Władysław III of Poland', 'King of Poland and Hungary', (1424, 1444), 1434, 1444,
  'King of Poland and Hungary at twenty, killed leading a crusade against the Turks at Varna.', *PL, at='krakow', tags='rule war')
K('Casimir IV Jagiellon', KPL, (1427, 1492), 1447, 1492,
  'Beat the Teutonic Knights in the Thirteen Years\' War and won back Danzig and the Baltic coast.', *PL, at='krakow')
K('Sigismund I the Old', KPL, (1467, 1548), 1506, 1548,
  'Brought the Italian Renaissance to Kraków.', *PL, at='krakow', tags='rule art')
K('Sigismund II Augustus', KPL, (1520, 1572), 1548, 1572,
  'Joined Poland and Lithuania into one Commonwealth at Lublin in 1569.', *PL, at='krakow')
K('Stephen Báthory', KPL, (1533, 1586), 1576, 1586,
  'Prince of Transylvania elected king of Poland, who beat Ivan the Terrible.', *PL, at='krakow', tags='rule war')
K('Sigismund III Vasa', KPL, (1566, 1632), 1587, 1632,
  'Moved the capital to Warsaw and briefly saw his son chosen tsar in Moscow.', *PL, at='warsaw')
K('Władysław IV Vasa', KPL, (1595, 1648), 1632, 1648,
  "Chosen tsar of Russia as a boy, later a tolerant king who kept Poland out of the Thirty Years' War.", *PL, at='warsaw')
K('John II Casimir Vasa', KPL, (1609, 1672), 1648, 1668,
  "Reigned through the Cossack revolt and the Swedish 'Deluge', then gave up the crown.", *PL, at='warsaw')
K('Augustus II the Strong', KPL, (1670, 1733), 1697, 1733,
  'Elector of Saxony and king of Poland, famed for his strength, his mistresses and his Meissen porcelain.', *PL, at='warsaw')
K('Stanisław August Poniatowski', KPL, (1732, 1798), 1764, 1795,
  "Catherine the Great's former lover and Poland's last king, who saw it carved up by its neighbours.", *PL, at='warsaw')
K('Władysław Gomułka', 'Leader of Poland', (1905, 1982), 1956, 1970,
  'Communist leader who won Poland a little freedom from Moscow in 1956.', 'Poland', at='warsaw')
K('Wojciech Jaruzelski', 'Leader of Poland', (1923, 2014), 1981, 1989,
  'General who declared martial law against Solidarity in 1981 and later handed power over peacefully.', 'Poland', at='warsaw')
K('Lech Kaczyński', 'President of Poland', (1949, 2010), 2005, 2010,
  "President killed with much of Poland's leadership in a plane crash at Smolensk in 2010.", 'Poland', at='warsaw')
P('Donald Tusk', 'Prime minister of Poland', (1957, None), 3, 'rule',
  'Twice prime minister of Poland and in between president of the European Council.',
  R(2007, 2014, 'Prime minister of Poland', 'Poland', at='warsaw'), R(2023, 2026, 'Prime minister of Poland', 'Poland', at='warsaw'))
K('Andrzej Duda', 'President of Poland', (1972, None), 2015, 2025,
  'Conservative president of Poland for ten years.', 'Poland', at='warsaw')
K('Karol Nawrocki', 'President of Poland', (1983, None), 2025, 2026,
  'Historian and nationalist elected president of Poland in 2025.', 'Poland', at='warsaw')
K('Gediminas', 'Grand Duke of Lithuania', (1275, 1341), 1316, 1341,
  'Pagan grand duke who made Vilnius his capital and Lithuania a great power.', 'Lithuania', at='vilnius')
K('Vytautas', 'Grand Duke of Lithuania', (1350, 1430), 1392, 1430,
  'Helped crush the Teutonic Knights at Grunwald in 1410 and ruled Lithuania from the Baltic almost to the Black Sea.', 'Lithuania',
  'Poland-Lithuania', at='vilnius', tags='rule war')

# ---------- Scandinavia ----------
K('Olof Skötkonung', KSW, (980, 1022), 995, 1022,
  'First king of Sweden known to have been baptised.', *SWE, at='uppsala', tags='rule faith')
K('Birger Jarl', 'Jarl of Sweden', (1210, 1266), 1248, 1266,
  'Statesman who ran Sweden for his sons and is said to have founded Stockholm.', *SWE, at='stockholm')
K('Margaret I of Denmark', 'Queen of Denmark, Norway and Sweden', (1353, 1412), 1375, 1412,
  'United Denmark, Norway and Sweden under one crown in the Kalmar Union of 1397.', *DEN, at='roskilde', rank=2)
K('Gustav Vasa', KSW, (1496, 1560), 1523, 1560,
  'Led the revolt that broke Sweden away from Denmark and made it Lutheran.', *SWE, at='stockholm', rank=2, wiki='Gustav I of Sweden')
K('Eric XIV of Sweden', KSW, (1533, 1577), 1560, 1568,
  'Went mad, murdered nobles, and was deposed and probably poisoned.', *SWE, at='stockholm')
K('John III of Sweden', KSW, (1537, 1592), 1568, 1592,
  'Took the throne from his mad brother Eric and leaned toward the old Catholic faith.', *SWE, at='stockholm')
K('Charles IX of Sweden', KSW, (1550, 1611), 1599, 1611,
  'Took the crown from his Catholic nephew Sigismund; father of Gustavus Adolphus.', *SWE, at='stockholm')
P('Christina, Queen of Sweden', 'Queen of Sweden', (1626, 1689), 2, 'rule mind',
  'Learned queen who brought Descartes to Stockholm, then gave up her throne, became a Catholic and moved to Rome.',
  R(1632, 1654, 'Queen of Sweden', *SWE, at='stockholm'), G(1655, 1689, 'In Rome', 'rome'))
K('Axel Oxenstierna', 'Lord High Chancellor of Sweden', (1583, 1654), 1612, 1654,
  'Ran Sweden for Gustavus Adolphus and then for the young Queen Christina.', *SWE, at='stockholm')
K('Charles X Gustav', KSW, (1622, 1660), 1654, 1660,
  'Marched his army across the frozen sea to beat Denmark in 1658.', *SWE, at='stockholm', tags='rule war')
K('Charles XI of Sweden', KSW, (1655, 1697), 1660, 1697,
  'Made the Swedish crown absolute and paid off its debts by taking back noble lands.', *SWE, at='stockholm')
K('Gustav III', KSW, (1746, 1792), 1771, 1792,
  'Theatre-loving king who seized absolute power and was shot at a masked ball in 1792.', *SWE, at='stockholm')
K('Gustav IV Adolf', KSW, (1778, 1837), 1792, 1809,
  'Lost Finland to Russia in 1809 and was deposed.', *SWE, at='stockholm')
K('Oscar II', 'King of Sweden and Norway', (1829, 1907), 1872, 1907,
  'Lost Norway when it voted for independence in 1905.', *SWE, at='stockholm')
K('Gustaf V', KSW, (1858, 1950), 1907, 1950,
  'Kept Sweden neutral through both world wars.', *SWE, at='stockholm')
P('Olof Palme', 'Prime minister of Sweden', (1927, 1986), 3, 'rule reform',
  'Outspoken prime minister of Sweden, shot dead on a Stockholm street in 1986.',
  R(1969, 1976, 'Prime minister of Sweden', 'Sweden', at='stockholm'), R(1982, 1986, 'Prime minister of Sweden', 'Sweden', at='stockholm'))
K('Carl XVI Gustaf', KSW, (1946, None), 1973, 2026,
  'King of Sweden since 1973, the longest reign in its history.', 'Sweden', at='stockholm')
K('Valdemar I of Denmark', KDK, (1131, 1182), 1157, 1182,
  'Valdemar the Great, who reunited Denmark after civil war and crusaded against the pagan Wends.', *DEN, at='roskilde')
K('Valdemar II of Denmark', KDK, (1170, 1241), 1202, 1241,
  'Conquered Estonia, where legend says the Danish flag fell from the sky in 1219.', *DEN, at='roskilde')
P('Christian II of Denmark', KDK, (1481, 1559), 3, 'rule',
  'Ordered the Stockholm Bloodbath of 1520, which cost him Sweden, and spent his last 27 years a prisoner.',
  R(1513, 1523, KDK, *DEN, at='copenhagen'), G(1532, 1559, 'A prisoner in Danish castles', (9.79, 55.26)))
K('Christian IV of Denmark', KDK, (1577, 1648), 1588, 1648,
  "Builder king of Copenhagen who fared badly in the Thirty Years' War.", *DEN, at='copenhagen', rank=2)
K('Christian IX of Denmark', KDK, (1818, 1906), 1863, 1906,
  "The 'father-in-law of Europe', whose children married into the thrones of Britain, Russia and Greece.", *DEN, at='copenhagen')
K('Christian X of Denmark', KDK, (1870, 1947), 1912, 1947,
  'Rode out on horseback through occupied Copenhagen every day of the Second World War.', *DEN, at='copenhagen')
K('Margrethe II', 'Queen of Denmark', (1940, None), 1972, 2024,
  'Reigned for 52 years and stepped down in favour of her son in 2024.', 'Denmark', at='copenhagen')
K('Frederik X', KDK, (1968, None), 2024, 2026,
  'King of Denmark since his mother stepped down in 2024.', 'Denmark', at='copenhagen')
P('Haakon VII', 'King of Norway', (1872, 1957), 3, 'rule',
  'Danish prince chosen king of newly independent Norway in 1905, who led its resistance to Hitler from London.',
  R(1905, 1957, 'King of Norway', 'Norway', at='oslo'),
  G(1940, 1945, 'In exile in London', ('oslo', 1940.3), ((18.96, 69.65, 1940.4)), ('london', 1940.48), ('london', 1945.4), ('oslo', 1945.43)))

# ---------- Russia ----------
P('Alexander Nevsky', 'Prince of Novgorod and Grand Prince of Vladimir', (1221, 1263), 2, 'rule war faith',
  'Beat the Swedes on the Neva and the Teutonic Knights on the ice of Lake Peipus, then kept peace with the Mongols.',
  R(1236, 1251, 'Prince of Novgorod', 'Principality of Novgorod', 'Novgorod', at='novgorod'),
  G(1242, 1242, 'The battle on the ice', ('novgorod', 1242.1), ((27.7, 58.4, 1242.26)), ('novgorod', 1242.4)),
  R(1252, 1263, 'Grand Prince of Vladimir', *MOS, at='vladimir'))
K('Ivan I of Moscow', 'Grand Prince of Moscow', (1288, 1340), 1325, 1340,
  "'Moneybag', who collected the Mongols' tribute for them and made Moscow the seat of the Russian Church.", *MOS, at='moscow')
P('Dmitry Donskoy', 'Grand Prince of Moscow', (1350, 1389), 2, 'rule war',
  'Beat the Golden Horde at Kulikovo in 1380, the first great Russian victory over the Mongols.',
  R(1359, 1389, 'Grand Prince of Moscow', *MOS, at='moscow'),
  G(1380, 1380, 'To Kulikovo Field', ('moscow', 1380.6), ((38.66, 53.67, 1380.69)), ('moscow', 1380.8)))
K('Vasily I of Moscow', 'Grand Prince of Moscow', (1371, 1425), 1389, 1425,
  "Dmitry Donskoy's son, who added Nizhny Novgorod to Moscow's lands.", *MOS, at='moscow')
K('Vasily II of Moscow', 'Grand Prince of Moscow', (1415, 1462), 1425, 1462,
  "'The Blind', blinded by a rival in a civil war, who refused his Church's union with Rome.", *MOS, at='moscow')
K('Vasily III of Russia', 'Grand Prince of Moscow', (1479, 1533), 1505, 1533,
  'Took Pskov and Smolensk, gathering the last free Russian lands under Moscow.', *MOS, at='moscow')
K('Boris Godunov', 'Tsar of Russia', (1552, 1605), 1585, 1605,
  'Regent for the feeble Tsar Feodor, then tsar himself; his death opened the Time of Troubles.', *MOS, at='moscow')
K('Michael of Russia', 'Tsar of Russia', (1596, 1645), 1613, 1645,
  'Chosen tsar at sixteen after the Time of Troubles, the first of the Romanovs.', *MOS, at='moscow')
K('Alexis of Russia', 'Tsar of Russia', (1629, 1676), 1645, 1676,
  "Took eastern Ukraine and saw the Russian Church split over Patriarch Nikon's reforms.", *MOS, at='moscow')
K('Catherine I of Russia', 'Empress of Russia', (1684, 1727), 1725, 1727,
  'A Livonian peasant girl who married Peter the Great and ruled after him.', *RUS, at='st_petersburg')
K('Anna of Russia', 'Empress of Russia', (1693, 1740), 1730, 1740,
  'Ruled through German favourites and built a palace of ice for a jester\'s wedding.', *RUS, at='st_petersburg')
K('Elizabeth of Russia', 'Empress of Russia', (1709, 1762), 1741, 1762,
  "Peter the Great's daughter, who took the throne in a coup, founded Moscow University and fought Frederick the Great.", *RUS,
  at='st_petersburg')
K('Paul I of Russia', 'Emperor of Russia', (1754, 1801), 1796, 1801,
  "Catherine the Great's son, strangled by his own officers in 1801.", *RUS, at='st_petersburg')
K('Alexander III of Russia', 'Emperor of Russia', (1845, 1894), 1881, 1894,
  "Crushed reform after his father's assassination and began the Trans-Siberian Railway.", *RUS, at='st_petersburg')
K('Alexander Kerensky', 'Head of the Russian Provisional Government', (1881, 1970), 1917, 1917,
  "Led Russia's Provisional Government until Lenin's Bolsheviks overthrew it in October 1917.", 'Russian Empire', at='st_petersburg')
K('Yuri Andropov', 'Leader of the Soviet Union', (1914, 1984), 1982, 1984,
  'Former KGB chief who led the Soviet Union for fifteen months.', 'USSR', at='moscow')
P('Bohdan Khmelnytsky', 'Hetman of the Cossacks', (1595, 1657), 3, 'war rule',
  'Cossack hetman whose rising against Poland in 1648 founded a Cossack state in Ukraine and led to its union with Russia.',
  G(1648, 1657, 'The Cossack rising', ((33.5, 48.35, 1648.35)), ((31.26, 49.42, 1648.4)), ((24.03, 49.84, 1648.8)), ('kiev', 1649.0),
    ((32.66, 49.08, 1649.2)), ((25.15, 50.36, 1651.5)), ((32.66, 49.08, 1651.8)), ((31.45, 50.07, 1654.05)), ((32.66, 49.08, 1654.3)),
    ((32.66, 49.08, 1657.6))))

# ---------- Byzantium and the Balkans ----------
K('Constantine IX Monomachos', 'Byzantine emperor', (1000, 1055), 1042, 1055,
  'Emperor when the Church split between Rome and Constantinople in 1054.', *BYZ, at='constantinople')
P('Romanos IV Diogenes', 'Byzantine emperor', (1030, 1072), 3, 'rule war',
  'Soldier-emperor beaten and captured by the Seljuks at Manzikert in 1071; blinded by his rivals when he came home.',
  R(1068, 1070, 'Byzantine emperor', *BYZ, at='constantinople'),
  G(1071, 1072, 'Manzikert and after', ('constantinople', 1071.2), ('manzikert', 1071.65), ('manzikert', 1071.72), ((29.98, 39.42, 1072.3)),
    ((29.1, 40.87, 1072.5))))
K('John II Komnenos', 'Byzantine emperor', (1087, 1143), 1118, 1143,
  "'John the Good', the most admired of the Komnenian emperors.", *BYZ, at='constantinople')
K('Manuel I Komnenos', 'Byzantine emperor', (1118, 1180), 1143, 1180,
  'Last great Byzantine emperor, crushed by the Seljuks at Myriokephalon in 1176.', *BYZ, at='constantinople')
K('Theodore I Laskaris', 'Emperor at Nicaea', (1174, 1221), 1205, 1221,
  'Kept Byzantium alive in exile at Nicaea after the crusaders took Constantinople.', *BYZ, at='nicaea')
K('Michael VIII Palaiologos', 'Byzantine emperor', (1224, 1282), 1259, 1282,
  'Took Constantinople back from the Latins in 1261.', *BYZ, at='constantinople')
K('Andronikos II Palaiologos', 'Byzantine emperor', (1259, 1332), 1282, 1328,
  'Disbanded the navy and hired the Catalan Company, which turned on him.', *BYZ, at='constantinople')
K('John VI Kantakouzenos', 'Byzantine emperor', (1292, 1383), 1347, 1354,
  'Brought the Ottomans into Europe as allies in a civil war, then retired as a monk.', *BYZ, at='constantinople')
P('Manuel II Palaiologos', 'Byzantine emperor', (1350, 1425), 3, 'rule',
  "Toured Europe begging for help against the Turks, and was saved instead by Timur's defeat of Bayezid.",
  R(1391, 1425, 'Byzantine emperor', *BYZ, at='constantinople'),
  G(1399, 1403, 'Begging the West for help', ('constantinople', 1399.92), ('venice', 1400.3), ('paris', 1400.44), ('london', 1400.96), ('london', 1401.1),
    ('paris', 1401.2), ('paris', 1402.7), ('venice', 1402.95), ('constantinople', 1403.45)))
P('John VIII Palaiologos', 'Byzantine emperor', (1392, 1448), 3, 'rule faith',
  'Went to Italy in 1438 and agreed to reunite his Church with Rome, for help that never came.',
  R(1425, 1448, 'Byzantine emperor', *BYZ, at='constantinople'),
  G(1437, 1440, 'To the council in Italy', ('constantinople', 1437.9), ('venice', 1438.1), ((11.62, 44.84, 1438.2)), ('florence', 1439.1),
    ('florence', 1439.6), ('venice', 1439.8), ('constantinople', 1440.1)))
K('Stefan Dušan', 'Emperor of the Serbs and Greeks', (1308, 1355), 1331, 1355,
  'Made Serbia the strongest state in the Balkans and crowned himself emperor in 1346.', 'Serbia', at=(21.43, 42.0))
K('Carol I of Romania', 'King of Romania', (1839, 1914), 1866, 1914,
  "German prince who became Romania's ruler and won its independence from the Ottomans in 1878.", 'Romania', at='bucharest')
P('Eleftherios Venizelos', 'Prime minister of Greece', (1864, 1936), 3, 'rule',
  'Cretan statesman who nearly doubled the size of Greece in the Balkan Wars.',
  R(1910, 1915, 'Prime minister of Greece', 'Greece', at='athens'), R(1917, 1920, 'Prime minister of Greece', 'Greece', at='athens'),
  R(1928, 1932, 'Prime minister of Greece', 'Greece', at='athens'))
K('Tomáš Garrigue Masaryk', 'President of Czechoslovakia', (1850, 1937), 1918, 1935,
  'Philosopher who founded Czechoslovakia and was its president for seventeen years.', 'Czechoslovakia', at='prague')
P('Carl Gustaf Emil Mannerheim', 'President of Finland', (1867, 1951), 3, 'war rule',
  "Led Finland's defence against the Soviet Union in the Winter War and later became its president.",
  G(1939, 1944, 'Commander-in-chief of Finland', (27.27, 61.69)), R(1944, 1946, 'President of Finland', 'Finland', at='helsinki'))
K('Enver Hoxha', 'Leader of Albania', (1908, 1985), 1944, 1985,
  'Stalinist dictator who sealed Albania off from the world and built some 170,000 concrete bunkers.', 'Albania', at='tirana')

# ---------- Ireland ----------
P('Brian Boru', 'High King of Ireland', (941, 1014), 3, 'rule war',
  'High King of Ireland, killed in his tent as his army beat the Vikings of Dublin at Clontarf in 1014.',
  G(1002, 1013, 'High King of Ireland, at Kincora', (-8.44, 52.81)),
  G(1014, 1014, 'Battle of Clontarf', ((-8.44, 52.81, 1014.0)), ((-6.21, 53.36, 1014.31))))
P('Michael Collins', 'Irish revolutionary leader', (1890, 1922), 3, 'war',
  "Ran the IRA's guerrilla war against Britain, signed the treaty that made the Irish Free State, and was shot in the civil war that followed.",
  G(1916, 1922, 'The fight for Irish independence', ('dublin', 1916.3), ('dublin', 1921.8), ('london', 1921.85), ('london', 1921.93), ('dublin', 1922.0),
    ((-8.86, 51.79, 1922.64))))
P('Éamon de Valera', 'Taoiseach and president of Ireland', (1882, 1975), 3, 'rule',
  'Survived the 1916 Easter Rising and led independent Ireland for most of the next forty years.',
  R(1932, 1948, 'Leader of Ireland', 'Ireland', at='dublin'), R(1951, 1954, 'Taoiseach', 'Ireland', at='dublin'),
  R(1957, 1973, 'Taoiseach, then president', 'Ireland', at='dublin'))


# ---------- filling the years between the reigns above ----------
# the empire, Bohemia and Austria
K('Philip of Swabia', 'King of Germany', (1177, 1208), 1198, 1208,
  "Barbarossa's youngest son, who fought Otto IV for the crown for ten years and was murdered at Bamberg.", *HRE, at='aachen')
K('Richard of Cornwall', 'King of the Romans', (1209, 1272), 1257, 1272,
  'English prince, brother of Henry III, who bought the German crown in the years without an emperor.', *HRE, at='aachen')
K('Adolf of Nassau', 'King of Germany', (1250, 1298), 1292, 1298,
  'Minor count chosen king by the electors, then deposed and killed in battle by Albert of Habsburg.', *HRE, at='aachen',
  wiki='Adolf of Germany')
K('Albert I of Germany', 'King of Germany', (1255, 1308), 1298, 1308,
  'Habsburg king murdered by his own nephew; the legend of William Tell is set in his reign.', *HRE, at='vienna')
P('Henry VII, Holy Roman Emperor', EMP, (1273, 1313), 3, 'rule',
  'Count of Luxembourg who marched into Italy to restore the empire, as Dante hoped, and died of fever near Siena.',
  R(1308, 1309, 'King of Germany', *HRE, at='aachen'),
  G(1310, 1313, 'The march into Italy', ((6.93, 45.25, 1310.8)), ('turin', 1310.85), ((9.19, 45.46, 1310.97)), ('genoa', 1311.8), ('pisa', 1312.2),
    ('rome', 1312.4), ('rome', 1312.6), ('pisa', 1313.2), ((11.48, 43.13, 1313.65))))
P('Ottokar II of Bohemia', 'King of Bohemia', (1233, 1278), 3, 'rule war',
  "'The Iron and Golden King', who ruled from the Baltic to the Adriatic and fell fighting Rudolf of Habsburg on the Marchfeld.",
  G(1253, 1277, 'King of Bohemia', 'prague'), G(1278, 1278, 'Battle on the Marchfeld', ('prague', 1278.5), ((16.85, 48.35, 1278.65))))
K('Wenceslaus IV of Bohemia', 'King of Bohemia and of the Romans', (1361, 1419), 1378, 1400,
  'Idle, hard-drinking king of the Romans, deposed in 1400; the Hussite revolt broke out in his last days.', *HRE, at='prague')
K('Rupert of Germany', 'King of Germany', (1352, 1410), 1400, 1410,
  'Elector Palatine chosen king in place of Wenceslaus, who never won real power.', *HRE, at=(8.69, 49.41))
K('Albert II of Germany', 'King of Germany, Hungary and Bohemia', (1397, 1439), 1438, 1439,
  "Sigismund's son-in-law, first of the Habsburgs who then held the imperial crown almost without a break until 1806.", *HRE,
  at='vienna')
P('George of Poděbrady', 'King of Bohemia', (1420, 1471), 3, 'rule',
  'Hussite king of Bohemia who proposed a union of Christian rulers to keep the peace, an early dream of a league of nations.',
  G(1458, 1471, 'King of Bohemia', 'prague'))
P('Karl Renner', 'Chancellor and president of Austria', (1870, 1950), 3, 'rule',
  'Led Austria twice out of the ruins of a lost war: as its first chancellor in 1918 and again in 1945.',
  R(1919, 1920, 'Chancellor of Austria', *AUS, at='vienna'), R(1945, 1950, 'President of Austria', *AUS, at='vienna'))
K('Kurt Schuschnigg', 'Chancellor of Austria', (1897, 1977), 1934, 1938,
  'Last chancellor of independent Austria, who called a vote against union with Germany and was jailed by Hitler.', 'Austria',
  at='vienna')
K('Bruno Kreisky', 'Chancellor of Austria', (1911, 1990), 1970, 1983,
  'Socialist chancellor for thirteen years, who made neutral Austria a meeting place between East and West.', 'Austria', at='vienna')
P('Kurt Waldheim', 'President of Austria', (1918, 2007), 3, 'rule',
  'Secretary-General of the United Nations, then president of Austria, shunned abroad when his hidden war record came out.',
  G(1972, 1981, 'Secretary-General of the United Nations', 'new_york'), R(1986, 1992, 'President of Austria', 'Austria', at='vienna'))
K('Alexander Van der Bellen', 'President of Austria', (1944, None), 2017, 2026,
  'Green economics professor elected president of Austria in 2016.', 'Austria', at='vienna')

# Prussia
K('Albert, Duke of Prussia', 'Duke of Prussia', (1490, 1568), 1525, 1568,
  'Last grand master of the Teutonic Knights, who turned their land into Prussia, the first Lutheran state.', 'Prussia', 'Teutonic Knights',
  at='konigsberg', tags='rule faith')
K('George William, Elector of Brandenburg', 'Elector of Brandenburg and Duke of Prussia', (1595, 1640), 1619, 1640,
  "Weak elector who watched Swedish and imperial armies ravage Brandenburg in the Thirty Years' War.", 'Prussia', at='berlin')

# Russia
K('Vsevolod the Big Nest', 'Grand Prince of Vladimir', (1154, 1212), 1176, 1212,
  'Strongest of the Russian princes of his day, named for his many children.', 'Principality of Vladimir-Suzdal', 'Kievan Rus',
  at='vladimir')
K('Yuri II of Vladimir', 'Grand Prince of Vladimir', (1189, 1238), 1218, 1238,
  'Founded Nizhny Novgorod and was killed when the Mongols destroyed his army on the Sit River in 1238.', *MOS, at='vladimir')
K('Daniel of Moscow', 'Prince of Moscow', (1261, 1303), 1283, 1303,
  'Youngest son of Alexander Nevsky, given little Moscow, who founded the line that would rule Russia.', *MOS, at='moscow')
K('Yury of Moscow', 'Prince of Moscow', (1281, 1325), 1303, 1325,
  'First prince of Moscow to win the title of grand prince, killed at the Horde by a rival from Tver.', *MOS, at='moscow')
K('Simeon of Moscow', 'Grand Prince of Moscow', (1316, 1353), 1340, 1353,
  "'The Proud', who kept peace with the Horde and died of the Black Death with his sons.", *MOS, at='moscow')
K('Ivan II of Moscow', 'Grand Prince of Moscow', (1326, 1359), 1353, 1359,
  "'The Fair', father of Dmitry Donskoy.", *MOS, at='moscow')
K('Elena Glinskaya', 'Regent of Russia', (1510, 1538), 1533, 1538,
  'Mother and regent of the young Ivan the Terrible, who reformed the coinage and probably died of poison.', *MOS, at='moscow')
P('False Dmitry I', 'Tsar of Russia', (1581, 1606), 3, 'rule war',
  'Pretender who claimed to be the dead son of Ivan the Terrible, marched on Moscow with Polish help and was killed a year after his crowning.',
  G(1604, 1605, 'The march on Moscow', ((30.52, 50.45, 1604.75)), ((33.26, 52.0, 1604.85)), ((33.87, 51.34, 1605.1)), ((33.87, 51.34, 1605.35)),
    ('moscow', 1605.47)),
  R(1606, 1606, 'Tsar of Russia', *MOS, at='moscow'))
P('Vasili IV of Russia', 'Tsar of Russia', (1552, 1612), 3, 'rule',
  'Boyar who led the plot against False Dmitry and took the crown, then was deposed and died a prisoner in Poland.',
  R(1606, 1610, 'Tsar of Russia', *MOS, at='moscow'), G(1611, 1612, 'A prisoner in Poland', ('warsaw', 1611.8), ((19.46, 52.43, 1612.0))))
P('Dmitry Pozharsky', 'Prince and Russian national hero', (1578, 1642), 3, 'war',
  'Led the army of townsfolk raised by the butcher Kuzma Minin that drove the Poles out of Moscow in 1612.',
  G(1611, 1612, "The people's army", ((44.0, 56.33, 1611.9)), ((44.0, 56.33, 1612.1)), ((39.89, 57.63, 1612.3)), ((39.89, 57.63, 1612.55)),
    ('moscow', 1612.65), ('moscow', 1612.9)))
K('Feodor III of Russia', 'Tsar of Russia', (1661, 1682), 1676, 1682,
  'Sickly tsar who burned the old books of noble rank so that offices would go by merit; half-brother of Peter the Great.', *MOS,
  at='moscow')
K('Sophia Alekseyevna', 'Regent of Russia', (1657, 1704), 1682, 1689,
  'Ruled Russia as regent for her young brothers until Peter the Great shut her in a convent.', *MOS, at='moscow')
K('Peter II of Russia', 'Emperor of Russia', (1715, 1730), 1727, 1730,
  'Grandson of Peter the Great, who moved the court back to Moscow and died of smallpox at fourteen.', *RUS, at='moscow')

# Poland
K('Mieszko II Lambert', KPL, (990, 1034), 1025, 1031,
  "Son of Bolesław the Brave, who lost his father's conquests and was driven out by his brothers.", *PL, at='gniezno')
K('Casimir I the Restorer', 'Duke of Poland', (1016, 1058), 1039, 1058,
  'Rebuilt Poland after a pagan revolt and a Czech invasion, and made Kraków the capital.', *PL, at='krakow')
K('Bolesław II the Generous', KPL, (1042, 1081), 1058, 1079,
  'Crowned king in 1076, then driven into exile after he had Bishop Stanislaus of Kraków killed.', *PL, at='krakow')
K('Władysław I Herman', 'Duke of Poland', (1044, 1102), 1079, 1102,
  'Weak duke who left the ruling to his count palatine and fought with his own sons.', *PL, at='krakow')
P('Henry II the Pious', 'High Duke of Poland', (1196, 1241), 3, 'rule war',
  'Duke of Silesia and of Poland, killed and beheaded by the Mongols at Legnica in 1241.',
  R(1238, 1240, 'High Duke of Poland', *PL, at=(17.04, 51.11)),
  G(1241, 1241, 'Battle of Legnica', ((17.04, 51.11, 1241.2)), ((16.16, 51.21, 1241.27))))
K('Władysław I the Elbow-high', KPL, (1260, 1333), 1306, 1333,
  'Tiny duke who spent his life putting the Polish lands back together and was crowned king in 1320.', *PL, at='krakow',
  wiki='Władysław I Łokietek')
K('John I Albert', KPL, (1459, 1501), 1492, 1501,
  'Lost an army in the forests of Moldavia in 1497.', *PL, at='krakow')
K('Alexander Jagiellon', KPL, (1461, 1506), 1501, 1506,
  "Agreed in 1505 that no new law could be made without the nobles' parliament, the Sejm.", *PL, at='krakow')
K('Michał Korybut Wiśniowiecki', KPL, (1640, 1673), 1669, 1673,
  'Chosen king for the fame of his father, a great Cossack-fighting lord; he lost Podolia to the Turks.', *PL, at='warsaw')
K('Augustus III of Poland', KPL, (1696, 1763), 1733, 1763,
  'Elector of Saxony put on the Polish throne by Russian troops, who preferred hunting and opera in Dresden to ruling.', *PL,
  at='warsaw')
K('Ignacy Mościcki', 'President of Poland', (1867, 1946), 1926, 1939,
  'Chemist who became president of Poland under Piłsudski and fled when Germany invaded.', *PL, at='warsaw')
P('Władysław Sikorski', 'Prime minister of Poland in exile', (1881, 1943), 3, 'war rule',
  'Led the Polish government and army in exile from France and then London, and died in a plane crash at Gibraltar.',
  G(1939, 1943, 'The Polish government in exile', ('paris', 1939.8), ((-0.55, 47.47, 1940.0)), ((-0.55, 47.47, 1940.4)), ('london', 1940.5),
    ('london', 1943.4), ((-5.35, 36.14, 1943.51))))
K('Bolesław Bierut', 'Leader of Poland', (1892, 1956), 1945, 1956,
  "Stalin's man, who led communist Poland until he died in Moscow in 1956.", 'Poland', at='warsaw')
K('Edward Gierek', 'Leader of Poland', (1913, 2001), 1970, 1980,
  'Borrowed heavily from the West to raise living standards, and fell when the Solidarity strikes began.', 'Poland', at='warsaw')
K('Aleksander Kwaśniewski', 'President of Poland', (1954, None), 1995, 2005,
  'Former communist who beat Lech Wałęsa and took Poland into NATO and the European Union.', 'Poland', at='warsaw')

# Sweden
K('Eric IX of Sweden', KSW, (1120, 1160), 1156, 1160,
  "Saint Eric, Sweden's patron saint, said to have led a crusade to Finland; killed at Uppsala.", *SWE, at='uppsala', tags='rule faith')
K('Magnus Ladulås', KSW, (1240, 1290), 1275, 1290,
  "'Barn-lock', who spared the peasants from having to feed and house travelling nobles.", *SWE, at='stockholm')
K('Magnus IV of Sweden', 'King of Sweden and Norway', (1316, 1374), 1319, 1364,
  'King of Sweden and Norway as a small child, who gave Sweden its first national law code and reigned through the Black Death.', *SWE,
  at='stockholm')
P('Sten Sture the Elder', 'Regent of Sweden', (1440, 1503), 3, 'rule war',
  'Regent who beat the Danes at Brunkeberg in 1471 and kept Sweden out of the hands of the Kalmar Union kings.',
  R(1470, 1497, 'Regent of Sweden', *SWE, at='stockholm'), R(1501, 1503, 'Regent of Sweden', *SWE, at='stockholm'))
K('Ulrika Eleonora, Queen of Sweden', 'Queen of Sweden', (1688, 1741), 1719, 1720,
  'Sister of Charles XII, who gave up absolute power to win the crown, then handed it to her husband.', *SWE, at='stockholm')
K('Frederick I of Sweden', KSW, (1676, 1751), 1720, 1751,
  "Reigned through the 'Age of Liberty', when parliament held the real power.", *SWE, at='stockholm')
K('Adolf Frederick, King of Sweden', KSW, (1710, 1771), 1751, 1771,
  'Powerless king who made snuffboxes and died after a huge feast of lobster, caviar and cream buns.', *SWE, at='stockholm')
K('Charles XIII', 'King of Sweden and Norway', (1748, 1818), 1809, 1818,
  'Old king put on the throne after the coup of 1809, who adopted the French marshal Bernadotte as his heir.', *SWE, at='stockholm')
K('Oscar I of Sweden', 'King of Sweden and Norway', (1799, 1859), 1844, 1859,
  "Bernadotte's son, a liberal king who gave daughters the same right to inherit as sons.", *SWE, at='stockholm')
K('Charles XV of Sweden', 'King of Sweden and Norway', (1826, 1872), 1859, 1872,
  'Painter and poet king, in whose reign parliament became two elected chambers.', *SWE, at='stockholm')
K('Gustaf VI Adolf', KSW, (1882, 1973), 1950, 1973,
  'Archaeologist king and expert on Chinese art, who took part in digs in Greece and Italy.', *SWE, at='stockholm', tags='rule mind')
K('Tage Erlander', 'Prime minister of Sweden', (1901, 1985), 1946, 1969,
  "Prime minister for 23 years, the builder of Sweden's welfare state.", 'Sweden', at='stockholm', tags='rule reform')

# Denmark and Norway
P('Harthacnut', 'King of Denmark and England', (1018, 1042), 3, 'rule',
  "Cnut the Great's son and the last Danish king of England, who died at a wedding feast.",
  R(1035, 1039, KDK, *DEN, at='roskilde'), R(1040, 1042, 'King of England and Denmark', 'England', *DEN, at='winchester'))
P('Magnus the Good', 'King of Norway and Denmark', (1024, 1047), 3, 'rule',
  'Son of Saint Olaf, called home from Russia to be king of Norway, and later of Denmark too.',
  R(1035, 1041, 'King of Norway', 'Norway', 'Denmark-Norway', at='trondheim'), R(1042, 1047, 'King of Norway and Denmark', *DEN, at='roskilde'))
K('Sweyn II of Denmark', KDK, (1019, 1076), 1047, 1076,
  "Cnut the Great's nephew, who organised the Danish Church and fathered some twenty children.", *DEN, at='roskilde')
K('Canute IV of Denmark', KDK, (1042, 1086), 1080, 1086,
  "Planned a great invasion of England in 1085 and was killed in a church at Odense; later Denmark's patron saint.", *DEN,
  at=(10.39, 55.4), tags='rule faith')
P('Eric I of Denmark', KDK, (1060, 1103), 3, 'rule faith',
  "'Evergood', the first Scandinavian king to set out for Jerusalem; he died on Cyprus on the way.",
  R(1095, 1102, KDK, *DEN, at='roskilde'),
  G(1103, 1103, 'Pilgrimage to the Holy Land', ('roskilde', 1103.0), ('constantinople', 1103.4), ((32.42, 34.77, 1103.53))))
K('Niels of Denmark', KDK, (1065, 1134), 1104, 1134,
  'Reigned thirty years, until his son murdered a rival and the king was beaten at Fotevik and killed.', *DEN, at='roskilde')
K('Canute VI of Denmark', KDK, (1163, 1202), 1182, 1202,
  'Refused to bow to the emperor and pushed Danish power along the Baltic coast.', *DEN, at='roskilde')
K('Eric IV of Denmark', KDK, (1216, 1250), 1241, 1250,
  "'Ploughpenny', named for a hated tax on ploughs, murdered on his brother's orders.", *DEN, at='roskilde')
K('Eric VI of Denmark', KDK, (1274, 1319), 1286, 1319,
  'Spent heavily on wars in northern Germany and left Denmark deep in debt.', *DEN, at='roskilde')
K('Valdemar IV of Denmark', KDK, (1320, 1375), 1340, 1375,
  "'Atterdag', who bought back a pawned and broken Denmark piece by piece and sacked the rich Baltic town of Visby.", *DEN,
  at='roskilde')
K('Eric of Pomerania', 'King of the Kalmar Union', (1382, 1459), 1412, 1439,
  'Great-nephew of Margaret I and king of all three Nordic kingdoms, who began charging ships a toll to pass the Sound.', *DEN,
  at='copenhagen')
K('Christian I of Denmark', KDK, (1426, 1481), 1448, 1481,
  "First king of the House of Oldenburg; he pawned Orkney and Shetland to Scotland to pay his daughter's dowry.", *DEN,
  at='copenhagen')
K('John, King of Denmark', KDK, (1455, 1513), 1481, 1513,
  'Won back Sweden for a few years and built up the Danish navy.', *DEN, at='copenhagen')
K('Frederick IV of Denmark', KDK, (1671, 1730), 1699, 1730,
  'Fought Charles XII of Sweden in the Great Northern War and sent the first Danish missionaries to India and Greenland.', *DEN,
  at='copenhagen')
K('Christian VI of Denmark', KDK, (1699, 1746), 1730, 1746,
  'Pious king who made confirmation compulsory and built the palace of Christiansborg.', *DEN, at='copenhagen', tags='rule faith')
K('Frederick V of Denmark', KDK, (1723, 1766), 1746, 1766,
  'Pleasure-loving king whose reign was a golden age for Danish art and trade.', *DEN, at='copenhagen')
K('Christian VII of Denmark', KDK, (1749, 1808), 1766, 1808,
  'Mentally ill king whose doctor Struensee ruled in his name and had an affair with the queen.', *DEN, at='copenhagen')
K('Johann Friedrich Struensee', 'Royal physician and ruler of Denmark', (1737, 1772), 1770, 1772,
  'German doctor who ran Denmark for the mad Christian VII, passed a flood of reforms, and was beheaded.', *DEN, at='copenhagen',
  tags='rule reform')
K('Frederick VI of Denmark', KDK, (1768, 1839), 1808, 1839,
  'Sided with Napoleon after the British bombarded Copenhagen, and lost Norway to Sweden in 1814.', *DEN, at='copenhagen')
K('Christian VIII of Denmark', KDK, (1786, 1848), 1839, 1848,
  'Briefly king of an independent Norway in 1814 before he became king of Denmark.', *DEN, at='copenhagen')
K('Frederick VII of Denmark', KDK, (1808, 1863), 1848, 1863,
  'Gave up absolute power and signed the democratic constitution of 1849.', *DEN, at='copenhagen')
K('Frederick IX of Denmark', KDK, (1899, 1972), 1947, 1972,
  'Changed the law so that his daughter Margrethe could inherit the throne.', *DEN, at='copenhagen')

# Hungary
K('Coloman, King of Hungary', KH, (1070, 1116), 1095, 1116,
  "'The Learned', who won Croatia for Hungary and declared that witches do not exist.", *HU, at='esztergom')
K('Géza II of Hungary', KH, (1130, 1162), 1141, 1162,
  'Invited German settlers, the Transylvanian Saxons, into his kingdom.', *HU, at='esztergom')
K('Béla III of Hungary', KH, (1148, 1196), 1172, 1196,
  'Raised in Constantinople as heir to the Byzantine throne, he became one of the richest kings in Europe.', *HU, at='esztergom')
K('Ladislaus IV of Hungary', KH, (1262, 1290), 1272, 1290,
  "'The Cuman', who lived among his mother's nomad people and was murdered by them.", *HU, at='esztergom')
K('Andrew III of Hungary', KH, (1265, 1301), 1290, 1301,
  'Last of the Árpád kings, who had ruled Hungary for four centuries.', *HU, at='budapest')
K('Mary, Queen of Hungary', 'Queen of Hungary', (1371, 1395), 1382, 1395,
  'Crowned king of Hungary at eleven, kidnapped by rebels, and freed by her husband Sigismund.', *HU, at='budapest')
K('Ladislaus the Posthumous', 'King of Hungary and Bohemia', (1440, 1457), 1444, 1457,
  'Born after his father died and crowned as a baby; John Hunyadi ruled for him.', *HU, at='budapest')
K('Vladislaus II of Hungary', 'King of Hungary and Bohemia', (1456, 1516), 1490, 1516,
  "'King Okay', who agreed to whatever the nobles asked and let the strong kingdom of Matthias Corvinus fall apart.", *HU, at='budapest')
K('John Zápolya', KH, (1487, 1540), 1526, 1540,
  'Chosen king after Mohács, he held eastern Hungary against the Habsburgs as a vassal of Suleiman.', *HU, at='budapest')
K('Mátyás Rákosi', 'Leader of Hungary', (1892, 1971), 1947, 1956,
  "Stalinist dictator who called himself 'Stalin's best Hungarian pupil', removed just before the 1956 revolution.", 'Hungary',
  at='budapest')
K('Árpád Göncz', 'President of Hungary', (1922, 2015), 1990, 2000,
  'Writer and translator, jailed after 1956, who became the first president of free Hungary.', 'Hungary', at='budapest')
P('Gyula Horn', 'Prime minister of Hungary', (1932, 2013), 3, 'rule reform',
  'As foreign minister he cut the Iron Curtain fence with Austria in 1989 and let East Germans flee west; later prime minister.',
  G(1989, 1989, 'Opening the Iron Curtain', (16.6, 47.68)), R(1994, 1998, 'Prime minister of Hungary', 'Hungary', at='budapest'))
K('Ferenc Gyurcsány', 'Prime minister of Hungary', (1961, None), 2004, 2009,
  'Socialist prime minister brought down after a leaked speech admitting his government had lied.', 'Hungary', at='budapest')

# Byzantium
K('Zoe Porphyrogenita', 'Byzantine empress', (978, 1050), 1028, 1050,
  'Born in the purple, she made three husbands emperor in turn and briefly ruled in her own right with her sister.', *BYZ,
  at='constantinople')
K('Isaac I Komnenos', 'Byzantine emperor', (1007, 1061), 1057, 1059,
  'General who seized the throne, then fell ill and retired to a monastery.', *BYZ, at='constantinople')
K('Constantine X Doukas', 'Byzantine emperor', (1006, 1067), 1059, 1067,
  'Cut the army to save money while the Seljuks pressed into Anatolia.', *BYZ, at='constantinople')
K('Michael VII Doukas', 'Byzantine emperor', (1050, 1090), 1071, 1078,
  "Scholarly emperor nicknamed 'minus a quarter' after bread prices rose; most of Anatolia was lost in his reign.", *BYZ,
  at='constantinople')
K('Nikephoros III Botaneiates', 'Byzantine emperor', (1001, 1081), 1078, 1081,
  'Elderly general overthrown by Alexios Komnenos.', *BYZ, at='constantinople')
K('Andronikos I Komnenos', 'Byzantine emperor', (1118, 1185), 1183, 1185,
  'Charming adventurer who seized the throne, ruled by terror and was torn apart by the mob of Constantinople.', *BYZ,
  at='constantinople')
P('Isaac II Angelos', 'Byzantine emperor', (1156, 1204), 3, 'rule',
  'Blinded and deposed by his brother, then put back on the throne by the crusaders in 1203.',
  R(1185, 1195, 'Byzantine emperor', *BYZ, at='constantinople'), R(1203, 1204, 'Byzantine emperor', *BYZ, at='constantinople'))
K('Alexios III Angelos', 'Byzantine emperor', (1153, 1211), 1195, 1203,
  'Blinded his brother to take the throne, then fled when the Fourth Crusade arrived.', *BYZ, at='constantinople')
P('Alexios IV Angelos', 'Byzantine emperor', (1182, 1204), 3, 'rule',
  'Promised the Fourth Crusade a fortune to put him on the throne, could not pay, and was strangled.',
  G(1203, 1203, 'With the crusaders', ((15.23, 44.12, 1203.05)), ((19.92, 39.62, 1203.38)), ('constantinople', 1203.48)),
  R(1204, 1204, 'Byzantine emperor', *BYZ, at='constantinople'))
K('John III Doukas Vatatzes', 'Emperor at Nicaea', (1192, 1254), 1221, 1254,
  'Wise emperor in exile at Nicaea who won back much of Greece; the Orthodox Church honours him as a saint.', *BYZ, at='nicaea')
K('Theodore II Laskaris', 'Emperor at Nicaea', (1221, 1258), 1254, 1258,
  'Scholar emperor who wrote books of philosophy and died young of epilepsy.', *BYZ, at='nicaea', tags='rule mind')
K('Andronikos III Palaiologos', 'Byzantine emperor', (1297, 1341), 1328, 1341,
  'Overthrew his grandfather and fought the rising Ottomans, losing Nicaea to them in 1331.', *BYZ, at='constantinople')
K('John V Palaiologos', 'Byzantine emperor', (1332, 1391), 1341, 1391,
  'Reigned fifty years through civil wars, went to Rome to become a Catholic, and ended as a vassal of the Ottoman sultan.', *BYZ,
  at='constantinople')

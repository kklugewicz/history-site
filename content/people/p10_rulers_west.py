"""Heads of state of western Europe between the famous ones in the era files, so a country's name on the map has its
ruler beside it in nearly every year: France, Britain, Spain and Portugal, the Low Countries, Italy, the popes, Venice."""
from _lib import P, R, G


def K(name, role, life, a, b, why, *names, at, rank=3, tags='rule', wiki=None):
    """one reign: the ruler sits by the first of `names` on the map from year a to b, or at `at` when none is"""
    P(name, role, life, rank, tags, why, R(a, b, role, *names, at=at), wiki=wiki)


FR = ('Kingdom of France', 'France', 'West Francia')
EN = ('England', 'English territory', 'Angevin Empire', 'England and Ireland')
GB1 = ('United Kingdom', 'England and Ireland')
GB2 = ('United Kingdom of Great Britain and Ireland', 'United Kingdom')
CAS = ('Castilla', 'Castile', 'Castille', 'Spain')
DUT = ('Dutch Republic', 'Netherlands', 'Habsburg Netherlands')
IT = ('Italy', 'Kingdom of Italy')
PAP = ('Papal States',)
KF, KE, KS, KP = 'King of France', 'King of England', 'King of Spain', 'King of Portugal'
PM = 'Prime minister of the United Kingdom'

# ---------- France ----------
K('Robert II of France', KF, (972, 1031), 996, 1031,
  "'Robert the Pious', the second Capetian king, excommunicated for marrying his cousin Bertha.", *FR, at='paris')
K('Henry I of France', KF, (1008, 1060), 1031, 1060,
  'Spent his reign fighting his own great lords; married Anne of Kiev, a daughter of Yaroslav the Wise.', *FR, at='paris')
K('Philip I of France', KF, (1052, 1108), 1060, 1108,
  "Reigned 48 years; excommunicated for running off with a count's wife, he sat out the First Crusade.", *FR, at='paris')
K('Louis VI of France', KF, (1081, 1137), 1108, 1137,
  "'Louis the Fat', who with Abbot Suger tamed the robber barons around Paris and made the crown strong again.", *FR, at='paris')
P('Louis VII of France', KF, (1120, 1180), 3, 'rule war',
  'Led the failed Second Crusade with his queen, Eleanor of Aquitaine, who then left him for Henry II of England.',
  R(1137, 1180, KF, *FR, at='paris'),
  G(1147, 1149, 'The Second Crusade', ('paris', 1147.45), ('constantinople', 1147.78), ((30.7, 36.89, 1148.05)), ('antioch', 1148.22),
    ('jerusalem', 1148.4), ((36.29, 33.51, 1148.56)), ('jerusalem', 1148.7), ('acre', 1149.27), ((16.0, 38.9, 1149.55)), ('rome', 1149.78), ('paris', 1149.88)))
K('Louis VIII of France', KF, (1187, 1226), 1223, 1226,
  'As a prince he invaded England in 1216 and was proclaimed king in London; died coming home from the crusade against the Cathars.', *FR, at='paris')
K('Philip III of France', KF, (1245, 1285), 1270, 1285,
  "'The Bold', who became king when his father died on crusade at Tunis, and died after his own failed crusade against Aragon.", *FR, at='paris')
K('Philip V of France', KF, (1291, 1322), 1316, 1322,
  'Took the crown over his little niece, which set the rule that no woman could inherit the French throne.', *FR, at='paris')
K('Charles IV of France', KF, (1294, 1328), 1322, 1328,
  'Last of the direct line of Capetian kings; his death without a son gave Edward III of England his claim to France.', *FR, at='paris')
K('Philip VI of France', KF, (1293, 1350), 1328, 1350,
  'First Valois king; Edward III beat him at Crécy in 1346, and the Black Death came two years later.', *FR, at='paris')
P('John II of France', KF, (1319, 1364), 3, 'rule war',
  "'John the Good', captured by the Black Prince at Poitiers in 1356 and held in London for a king's ransom.",
  R(1350, 1364, KF, *FR, at='paris'),
  G(1357, 1360, 'A prisoner of the English', ('bordeaux', 1357.0), ('bordeaux', 1357.3), ('london', 1357.4), ('london', 1360.5), ('calais', 1360.8)),
  G(1364, 1364, 'Back to London, where he died', ('paris', 1364.0), ('london', 1364.05)))
K('Charles V of France', KF, (1338, 1380), 1364, 1380,
  "'The Wise', who with his constable Bertrand du Guesclin won back most of the land France had lost to England.", *FR, at='paris')
K('Charles VI of France', KF, (1368, 1422), 1380, 1422,
  "'The Mad', whose fits of madness let France fall into civil war; after Agincourt he made Henry V of England his heir.", *FR, at='paris')
K('Louis XI', KF, (1423, 1483), 1461, 1483,
  "'The Universal Spider', who outwitted Charles the Bold and brought Burgundy, Anjou and Provence under the crown.", 'France', at='paris')
P('Charles VIII of France', KF, (1470, 1498), 3, 'rule war',
  'Marched into Italy in 1494 to claim Naples, starting sixty years of Italian Wars.',
  R(1483, 1498, KF, 'France', at='paris'),
  G(1494, 1495, 'Into Italy for Naples', ('lyon', 1494.55), ('turin', 1494.7), ('pisa', 1494.85), ('florence', 1494.88), ('rome', 1494.99),
    ('naples', 1495.14), ('naples', 1495.38), ('rome', 1495.42), ((10.1, 44.69, 1495.51)), ('turin', 1495.75), ('lyon', 1495.85)))
K('Louis XII', KF, (1462, 1515), 1498, 1515,
  "'Father of the People', who conquered Milan in 1499 and had lost it again by 1513.", 'France', at='paris')
P('Francis I of France', KF, (1494, 1547), 2, 'rule art war',
  'Renaissance king who won at Marignano, was captured at Pavia, and brought Leonardo da Vinci to France.',
  R(1515, 1547, KF, 'France', at='paris'),
  G(1525, 1526, 'Prisoner of Charles V', ('pavia', 1525.15), ('genoa', 1525.45), ('barcelona', 1525.47), ('madrid', 1525.62), ('madrid', 1526.12),
    ((-1.78, 43.36, 1526.21)), ('paris', 1526.5)))
K('Henry II of France', KF, (1519, 1559), 1547, 1559,
  'Took Calais back from the English in 1558; died when a lance splintered into his eye at a tournament.', 'France', at='paris')
K('Francis II of France', KF, (1544, 1560), 1559, 1560,
  'Teenage husband of Mary, Queen of Scots, who died after seventeen months on the throne.', 'France', at='paris')
K('Charles IX of France', KF, (1550, 1574), 1560, 1574,
  "Reigned under his mother, Catherine de' Medici, and ordered the St Bartholomew's Day massacre of Protestants in 1572.", 'France', at='paris')
P('Henry III of France', KF, (1551, 1589), 3, 'rule',
  'Last Valois king, elected king of Poland first; he had the Duke of Guise murdered and was stabbed to death by a friar.',
  R(1574, 1589, KF, 'France', at='paris'),
  G(1573, 1574, 'King of Poland for five months', ('paris', 1573.75), ('krakow', 1574.13), ('krakow', 1574.46), ('vienna', 1574.48), ('venice', 1574.54),
    ('lyon', 1574.68), ('avignon', 1574.9)))
K('Louis XIII', KF, (1601, 1643), 1610, 1643,
  'Became king at eight when his father was murdered; with Cardinal Richelieu he made the crown supreme.', 'France', at='paris', rank=2)
K('Cardinal Mazarin', 'Chief minister of France', (1602, 1661), 1643, 1661,
  'Italian-born cardinal who governed for the boy Louis XIV, beat the Fronde revolts and won the Peace of the Pyrenees.', 'France', at='paris')
K('Louis XV', KF, (1710, 1774), 1715, 1774,
  "'The Beloved', great-grandson of Louis XIV, under whom France lost Canada and India to Britain.", 'France', at='versailles', rank=2)
K('Louis XVIII', KF, (1755, 1824), 1814, 1824,
  'Brother of Louis XVI, put back on the throne when Napoleon fell; he fled to Ghent during the Hundred Days.', 'France', at='paris')
K('Charles X of France', KF, (1757, 1836), 1824, 1830,
  'Last Bourbon king of France, overthrown in the July Revolution of 1830.', 'France', at='paris')
K('Adolphe Thiers', 'President of France', (1797, 1877), 1871, 1873,
  'Crushed the Paris Commune in 1871 and paid off the Germans early, founding the Third Republic.', 'France', at='versailles')
K('Patrice de MacMahon', 'President of France', (1808, 1893), 1873, 1879,
  'Marshal captured at Sedan who, as president, kept the seat warm for a king who never came.', 'France', at='paris')
P('Jules Ferry', 'Prime minister of France', (1832, 1893), 3, 'rule reform',
  'Made French schools free, secular and compulsory, and won Tunisia and Indochina for the empire.',
  R(1880, 1881, 'Prime minister of France', 'France', at='paris'), R(1883, 1885, 'Prime minister of France', 'France', at='paris'))
P('Raymond Poincaré', 'President of France', (1860, 1934), 3, 'rule',
  'President through the First World War; as prime minister he sent troops into the Ruhr in 1923 when Germany fell behind on reparations.',
  R(1913, 1920, 'President of France', 'France', at='paris'), R(1922, 1924, 'Prime minister of France', 'France', at='paris'),
  R(1926, 1929, 'Prime minister of France', 'France', at='paris'))
K('Léon Blum', 'Prime minister of France', (1872, 1950), 1936, 1937,
  "First Socialist and first Jewish prime minister of France, who won workers paid holidays and the forty-hour week.", 'France', at='paris', tags='rule reform')
K('Édouard Daladier', 'Prime minister of France', (1884, 1970), 1938, 1940,
  'Signed the Munich Agreement with Chamberlain in 1938 and took France to war in 1939.', 'France', at='paris')
K('Georges Pompidou', 'President of France', (1911, 1974), 1969, 1974,
  "De Gaulle's prime minister and successor, who opened the way for Britain to join the European Community.", 'France', at='paris')
K("Valéry Giscard d'Estaing", 'President of France', (1926, 2020), 1974, 1981,
  'Modernising president who lowered the voting age to 18 and legalised abortion.', 'France', at='paris', tags='rule reform')
K('François Mitterrand', 'President of France', (1916, 1996), 1981, 1995,
  "France's longest-serving president, a Socialist who abolished the death penalty and built the euro with Helmut Kohl.", 'France', at='paris', rank=2)
K('Jacques Chirac', 'President of France', (1932, 2019), 1995, 2007,
  "Kept France out of the Iraq war in 2003 and was the first president to admit France's part in the Holocaust.", 'France', at='paris')
K('Nicolas Sarkozy', 'President of France', (1955, None), 2007, 2012,
  "Steered France through the 2008 crash and led the bombing of Gaddafi's Libya in 2011.", 'France', at='paris')
K('François Hollande', 'President of France', (1954, None), 2012, 2017,
  'Led France through the terror attacks of 2015 and hosted the Paris climate agreement.', 'France', at='paris')

# ---------- England, Scotland and Britain ----------
P('Æthelred the Unready', KE, (966, 1016), 3, 'rule',
  'Paid the Vikings Danegeld, ordered the massacre of the Danes in England in 1002, and fled when Sweyn Forkbeard conquered the country.',
  R(978, 1013, KE, *EN, at='winchester'), R(1014, 1016, KE, *EN, at='london'))
P('Sweyn Forkbeard', 'King of Denmark and England', (963, 1014), 3, 'rule war',
  'Viking king of Denmark who conquered England in 1013 and died five weeks after being proclaimed its king; father of Cnut.',
  R(986, 1012, 'King of Denmark', 'Denmark-Norway', 'Denmark', at='roskilde'),
  G(1013, 1014, 'Conquers England', ('roskilde', 1013.45), ((1.34, 51.27, 1013.6)), ((-0.77, 53.4, 1013.65)), ('london', 1013.95), ((-0.77, 53.4, 1014.09))))
K('Edward the Confessor', KE, (1003, 1066), 1042, 1066,
  'Built Westminster Abbey; his death without a son brought three claimants to the throne and the Norman Conquest.', *EN, at='westminster', tags='rule faith')
K('William II of England', KE, (1056, 1100), 1087, 1100,
  "William Rufus, the Conqueror's son, shot dead by an arrow while hunting in the New Forest.", *EN, at='winchester')
K('Henry I of England', KE, (1068, 1135), 1100, 1135,
  "The Conqueror's youngest son; when his only son drowned in the White Ship, England was left to fight over the crown.", *EN, at='winchester')
K('Stephen, King of England', KE, (1092, 1154), 1135, 1154,
  'Seized the crown from his cousin Matilda, starting the civil war called the Anarchy.', *EN, at='london')
P('Empress Matilda', 'Claimant to the English throne', (1102, 1167), 3, 'rule war',
  "Henry I's heir, who fought her cousin Stephen for England and escaped besieged Oxford across the snow; her son became Henry II.",
  G(1139, 1148, 'War for the English crown', ((-0.55, 50.86, 1139.75)), ('bristol', 1139.85), ('bristol', 1141.1), ('winchester', 1141.2), ('london', 1141.45),
    ('oxford', 1141.55), ('oxford', 1142.95), ((-1.99, 51.35, 1143.1)), ((-1.99, 51.35, 1148.1)), ('rouen', 1148.3)))
K('Henry III of England', KE, (1207, 1272), 1216, 1272,
  "King at nine who reigned 56 years, rebuilt Westminster Abbey and was captured by Simon de Montfort's rebel barons.", *EN, at='westminster')
K('Edward II of England', KE, (1284, 1327), 1307, 1327,
  'Beaten by Robert the Bruce at Bannockburn in 1314, deposed by his own queen, Isabella, and probably murdered.', *EN, at='westminster')
K('Richard II of England', KE, (1367, 1400), 1377, 1399,
  "Faced down the Peasants' Revolt at fourteen; overthrown by his cousin Henry Bolingbroke and probably starved in prison.", *EN, at='westminster')
K('Henry IV of England', KE, (1367, 1413), 1399, 1413,
  'Henry Bolingbroke, who took the throne from Richard II and spent his reign putting down rebels like Hotspur and Owain Glyndŵr.', *EN, at='westminster')
P('Henry VI of England', KE, (1421, 1471), 3, 'rule',
  "King at nine months old; he lost France at the end of the Hundred Years' War, went mad, and lost his throne in the Wars of the Roses.",
  R(1422, 1461, KE, *EN, at='westminster'), R(1470, 1471, 'King of England, restored for a year', *EN, at='westminster'))
P('Edward IV of England', KE, (1442, 1483), 3, 'rule war',
  'Yorkist warrior king who won the crown in the Wars of the Roses; father of the Princes in the Tower.',
  R(1461, 1470, KE, *EN, at='westminster'), R(1471, 1483, KE, *EN, at='westminster'))
P('Richard III of England', KE, (1452, 1485), 3, 'rule war',
  'Took the crown from his nephews, the Princes in the Tower, and died at Bosworth, the last English king killed in battle.',
  R(1483, 1484, KE, *EN, at='westminster'),
  G(1485, 1485, 'To Bosworth Field', ('westminster', 1485.3), ((-1.15, 52.95, 1485.45)), ((-1.15, 52.95, 1485.6)), ((-1.41, 52.59, 1485.64))))
K('Henry VII of England', KE, (1457, 1509), 1485, 1509,
  'Won the crown at Bosworth, ended the Wars of the Roses by marrying Elizabeth of York, and founded the Tudor dynasty.', *EN, at='westminster', rank=2)
K('Edward VI of England', KE, (1537, 1553), 1547, 1553,
  "Henry VIII's only son, a boy king under whom England became firmly Protestant.", *EN, at='westminster', tags='rule faith')
K('Mary I of England', 'Queen of England', (1516, 1558), 1553, 1558,
  "'Bloody Mary', who brought back Catholicism, burned nearly three hundred Protestants and lost Calais.", *EN, at='westminster', tags='rule faith')
P('James VI and I', 'King of Scotland and England', (1566, 1625), 2, 'rule',
  'King of Scots who inherited England from Elizabeth I in 1603, survived the Gunpowder Plot and gave his name to the King James Bible.',
  R(1567, 1602, 'King of Scots', 'Scotland', at='edinburgh'), R(1603, 1625, 'King of England and Scotland', *EN, 'Scotland', at='westminster'))
P('James II of England', KE, (1633, 1701), 3, 'rule faith',
  'Catholic king driven out by the Glorious Revolution of 1688, who lost his last stand in Ireland at the Boyne.',
  R(1685, 1688, KE, *EN, at='westminster'),
  G(1689, 1690, 'The war for Ireland', ((2.09, 48.9, 1689.0)), ('brest', 1689.15), ((-8.52, 51.71, 1689.2)), ('dublin', 1689.25), ((-6.35, 53.72, 1690.5)),
    ('dublin', 1690.52), ((2.09, 48.9, 1690.65))),
  G(1691, 1701, 'Exile at Saint-Germain', (2.09, 48.9)))
K('Anne, Queen of Great Britain', 'Queen of Great Britain', (1665, 1714), 1702, 1714,
  'Last Stuart monarch, under whom England and Scotland united as Great Britain in 1707 and Marlborough beat Louis XIV.',
  'England and Ireland', 'United Kingdom', 'Scotland', at='westminster')
K('George I of Great Britain', 'King of Great Britain', (1660, 1727), 1714, 1727,
  'German Elector of Hanover who became king in 1714 because he was the nearest Protestant heir.', *GB1, at='westminster')
K('Robert Walpole', 'Prime minister of Great Britain', (1676, 1745), 1721, 1742,
  "Britain's first prime minister in all but name, who kept the country out of war for most of twenty years.", *GB1, at='westminster')
K('George II of Great Britain', 'King of Great Britain', (1683, 1760), 1727, 1760,
  'Last British king to lead his army into battle, at Dettingen in 1743.', *GB1, at='westminster')
P('William Pitt the Elder', 'Prime minister of Great Britain', (1708, 1778), 3, 'rule war',
  "Ran Britain's side of the Seven Years' War, which won it Canada and India.",
  R(1756, 1761, 'Leader of the war government', *GB1, at='westminster'), R(1766, 1768, 'Prime minister of Great Britain', *GB1, at='westminster'))
P('William Pitt the Younger', 'Prime minister of Great Britain', (1759, 1806), 2, 'rule',
  'Prime minister at 24, who led Britain against revolutionary France and Napoleon.',
  R(1783, 1801, 'Prime minister of Great Britain', *GB1, at='westminster'), R(1804, 1806, PM, *GB2, at='westminster'))
P('George IV', 'King of the United Kingdom', (1762, 1830), 3, 'rule',
  'Spendthrift Prince Regent who ruled for his mad father from 1811 and built the Royal Pavilion at Brighton.',
  R(1811, 1819, 'Prince Regent', *GB2, at='westminster'), R(1820, 1830, 'King of the United Kingdom', *GB2, at='westminster'))
K('William IV', 'King of the United Kingdom', (1765, 1837), 1830, 1837,
  "The 'Sailor King', who let the Great Reform Act pass in 1832 and saw slavery abolished across the empire.", *GB2, at='westminster')
K('Robert Peel', PM, (1788, 1850), 1841, 1846,
  "Founded London's police, the 'bobbies', and split his own party by repealing the Corn Laws.", *GB2, at='westminster', tags='rule reform')
P('Lord Palmerston', PM, (1784, 1865), 3, 'rule',
  'Gunboat diplomat who ran British foreign policy on and off for thirty years and saw the Crimean War through as prime minister.',
  R(1855, 1858, PM, *GB2, at='westminster'), R(1859, 1865, PM, *GB2, at='westminster'), wiki='Henry John Temple, 3rd Viscount Palmerston')
K('Edward VII', 'King of the United Kingdom', (1841, 1910), 1901, 1910,
  "Victoria's pleasure-loving son, whose short reign gave its name to the Edwardian age and the friendship with France.", *GB2, at='westminster')
K('H. H. Asquith', PM, (1852, 1928), 1908, 1916,
  'Liberal prime minister who brought in old-age pensions and took Britain into the First World War.', *GB2, at='westminster')
K('George V', 'King of the United Kingdom', (1865, 1936), 1910, 1936,
  'King through the First World War, who renamed the royal family Windsor in 1917 to shed its German name.', *GB2, at='westminster')
K('Edward VIII', 'King of the United Kingdom', (1894, 1972), 1936, 1936,
  'Gave up the throne after eleven months to marry the American divorcée Wallis Simpson.', *GB2, at='westminster')
K('George VI', 'King of the United Kingdom', (1895, 1952), 1936, 1952,
  'Shy, stammering king who stayed in London through the Blitz.', *GB2, at='westminster')
K('Harold Macmillan', PM, (1894, 1986), 1957, 1963,
  "Prime minister of the 'wind of change', who began giving up Britain's African empire.", 'United Kingdom', at='westminster')
P('Harold Wilson', PM, (1916, 1995), 3, 'rule',
  'Labour prime minister who kept Britain out of the Vietnam War.',
  R(1964, 1970, PM, 'United Kingdom', at='westminster'), R(1974, 1976, PM, 'United Kingdom', at='westminster'))
K('David Cameron', PM, (1966, None), 2010, 2016,
  'Called the 2016 referendum in which Britain voted to leave the European Union.', 'United Kingdom', at='westminster')
K('Boris Johnson', PM, (1964, None), 2019, 2022,
  'Took Britain out of the European Union in 2020 and led it through the Covid pandemic.', 'United Kingdom', at='westminster')
K('Charles III', 'King of the United Kingdom', (1948, None), 2022, 2026,
  'Became king in 2022 at 73, after a record seventy years as heir.', 'United Kingdom', at='westminster', rank=2)
K('Keir Starmer', PM, (1962, None), 2024, 2026,
  'Won a Labour landslide in 2024, then resigned two years later as his party turned against him.', 'United Kingdom', at='westminster')
K('Andy Burnham', PM, (1970, None), 2026, 2026,
  'Mayor of Greater Manchester who succeeded Keir Starmer as Labour leader and prime minister in July 2026.', 'United Kingdom', at='westminster')
K('Macbeth, King of Scotland', 'King of Scots', (1005, 1057), 1040, 1057,
  'The real Macbeth, who killed King Duncan in battle and ruled Scotland for seventeen years before Shakespeare made him a villain.',
  'Scotland', at=(-3.43, 56.42))
K('James IV of Scotland', 'King of Scots', (1473, 1513), 1488, 1513,
  'Renaissance king of Scots, killed with much of his nobility fighting the English at Flodden.', 'Scotland', at='edinburgh')

# ---------- Castile, Aragon and Spain ----------
K('Ferdinand I of León', 'King of Castile and León', (1015, 1065), 1037, 1065,
  'Ferdinand the Great, count of Castile, who won León in 1037, called himself king and made the Muslim kingdoms of Spain pay him tribute.',
  *CAS, at='burgos')
K('Alfonso VI of León and Castile', 'King of León and Castile', (1040, 1109), 1072, 1109,
  'Took Toledo from the Moors in 1085 and twice exiled El Cid; was then beaten by the Almoravids at Sagrajas.', *CAS, at='toledo', tags='rule war')
K('Urraca of León and Castile', 'Queen of León and Castile', (1079, 1126), 1109, 1126,
  'Ruled León and Castile in her own right and fought her husband, Alfonso of Aragon, to keep them.', *CAS, at='leon')
K('Alfonso VII of León and Castile', 'King of León and Castile', (1105, 1157), 1126, 1157,
  "Had himself crowned 'Emperor of All Spain' in 1135.", *CAS, at='leon')
K('Ferdinand III of Castile', 'King of Castile and León', (1199, 1252), 1217, 1252,
  'Saint Ferdinand, who took Córdoba and Seville from the Moors and joined Castile and León for good.', *CAS, at='burgos', tags='rule war')
K('Alfonso X of Castile', 'King of Castile and León', (1221, 1284), 1252, 1284,
  "'The Wise', whose court of Christian, Muslim and Jewish scholars translated Arabic science and drew up new tables of the planets.",
  *CAS, at='toledo', tags='rule mind')
K('Alfonso XI of Castile', 'King of Castile and León', (1311, 1350), 1312, 1350,
  'Beat the last great invasion from Morocco at the Río Salado in 1340; died of the Black Death besieging Gibraltar.', *CAS, at='burgos')
K('Peter of Castile', 'King of Castile and León', (1334, 1369), 1350, 1369,
  "'Peter the Cruel', stabbed to death in a tent by his half-brother Henry, who took his crown.", *CAS, at='seville')
K('John II of Castile', 'King of Castile and León', (1405, 1454), 1406, 1454,
  'Poet-king who left the ruling to his favourite, Álvaro de Luna; father of Isabella the Catholic.', *CAS, at='valladolid')
K('Henry IV of Castile', 'King of Castile and León', (1425, 1474), 1454, 1474,
  "'Henry the Impotent', whose half-sister Isabella took the throne over his daughter Joanna.", *CAS, at='valladolid')
K('James I of Aragon', 'King of Aragon', (1208, 1276), 1213, 1276,
  "'The Conqueror', who took Majorca and Valencia from the Moors and wrote the first memoir by a Christian king.", 'Aragón', at='zaragoza', tags='rule war')
K('Philip III of Spain', KS, (1578, 1621), 1598, 1621,
  "Expelled the Moriscos, some 300,000 descendants of Spain's Muslims, in 1609.", 'Spain', at='madrid')
K('Philip IV of Spain', KS, (1605, 1665), 1621, 1665,
  'Patron of Velázquez, who reigned while Spain lost Portugal and the Dutch Republic for good.', 'Spain', at='madrid', tags='rule art')
K('Charles II of Spain', KS, (1661, 1700), 1665, 1700,
  'Last Habsburg king of Spain, sickly from generations of inbreeding; his death set off the War of the Spanish Succession.', 'Spain', at='madrid')
K('Philip V of Spain', KS, (1683, 1746), 1700, 1746,
  "Louis XIV's grandson and the first Bourbon king of Spain, whose crown cost Europe the War of the Spanish Succession.", 'Spain', at='madrid')
K('Ferdinand VI of Spain', KS, (1713, 1759), 1746, 1759,
  'Kept Spain at peace and rebuilt its navy.', 'Spain', at='madrid')
K('Charles IV of Spain', KS, (1748, 1819), 1788, 1808,
  'Left the ruling to his favourite Godoy and was made to hand his crown to Napoleon at Bayonne in 1808.', 'Spain', at='madrid')
P('Joseph Bonaparte', KS, (1768, 1844), 3, 'rule',
  "Napoleon's elder brother, made king of Naples and then of Spain, and driven out of Spain by Wellington in 1813.",
  R(1806, 1807, 'King of Naples', 'Kingdom of the Two Sicilies', at='naples'), R(1808, 1813, KS, 'Spain', at='madrid'))
K('Ferdinand VII of Spain', KS, (1784, 1833), 1814, 1833,
  'Restored after Napoleon, he tore up the liberal constitution while Spain lost most of its American empire.', 'Spain', at='madrid')
K('Isabella II of Spain', 'Queen of Spain', (1830, 1904), 1833, 1868,
  'Queen at three; her reign of civil wars and coups ended in exile in 1868.', 'Spain', at='madrid')
K('Alfonso XII', KS, (1857, 1885), 1874, 1885,
  'Brought back the monarchy in 1874 after the short-lived First Republic.', 'Spain', at='madrid')
K('Alfonso XIII', KS, (1886, 1941), 1886, 1931,
  'King from birth, who lost Cuba and the Philippines in 1898 and left Spain when it voted for a republic in 1931.', 'Spain', at='madrid')
K('Manuel Azaña', 'President of the Spanish Republic', (1880, 1940), 1936, 1939,
  'President of the Spanish Republic through the civil war against Franco.', 'Spain', at='madrid')
K('Juan Carlos I', KS, (1938, None), 1975, 2014,
  "Franco's chosen heir, who instead led Spain to democracy and faced down an army coup in 1981.", 'Spain', at='madrid', rank=2)
K('Felipe González', 'Prime minister of Spain', (1942, None), 1982, 1996,
  'Socialist who modernised Spain and took it into the European Community in 1986.', 'Spain', at='madrid')
K('Felipe VI', KS, (1968, None), 2014, 2026,
  'Became king when his father abdicated in 2014.', 'Spain', at='madrid')

# ---------- Portugal ----------
K('Denis of Portugal', KP, (1261, 1325), 1279, 1325,
  "'The Farmer King', who planted the great pine forest of Leiria and founded Portugal's first university.", 'Portugal', at='lisbon')
K('John I of Portugal', KP, (1357, 1433), 1385, 1433,
  'Kept Portugal free of Castile at Aljubarrota in 1385, sealed the alliance with England and fathered Henry the Navigator.', 'Portugal', at='lisbon')
K('Afonso V of Portugal', KP, (1432, 1481), 1438, 1481,
  "'The African', who took towns in Morocco and fought Isabella for the crown of Castile.", 'Portugal', at='lisbon')
K('John II of Portugal', KP, (1455, 1495), 1481, 1495,
  "'The Perfect Prince', who sent Bartolomeu Dias round the Cape of Good Hope and turned Columbus away.", 'Portugal', at='lisbon', tags='rule explore')
K('Manuel I of Portugal', KP, (1469, 1521), 1495, 1521,
  "'The Fortunate', who sent Vasco da Gama to India and Cabral to Brazil.", 'Portugal', at='lisbon', rank=2, tags='rule explore')
K('John III of Portugal', KP, (1502, 1557), 1521, 1557,
  'Ruled the spice empire at its height and brought the Inquisition to Portugal.', 'Portugal', at='lisbon')
P('Sebastian of Portugal', KP, (1554, 1578), 3, 'rule war',
  'Boy king who vanished in battle in Morocco in 1578; for centuries Portugal waited for him to come back.',
  R(1557, 1577, KP, 'Portugal', at='lisbon'),
  G(1578, 1578, 'Crusade to Morocco', ('lisbon', 1578.48), ((-6.03, 35.47, 1578.55)), ((-5.9, 35.0, 1578.59))))
K('John IV of Portugal', KP, (1604, 1656), 1640, 1656,
  'Led the revolt that freed Portugal from Spain in 1640 and founded the Braganza dynasty.', 'Portugal', at='lisbon')
P('Maria I of Portugal', 'Queen of Portugal', (1734, 1816), 3, 'rule',
  'First queen to reign over Portugal; she went mad and fled with the court to Brazil when Napoleon invaded in 1807.',
  R(1777, 1806, 'Queen of Portugal', 'Portugal', at='lisbon'),
  G(1807, 1816, 'With the court in Rio de Janeiro', ('lisbon', 1807.9), ('salvador', 1808.06), ('rio', 1808.18), ('rio', 1816.21)))
P('John VI of Portugal', KP, (1767, 1826), 3, 'rule',
  'Ran Portugal for his mad mother, fled Napoleon to Rio de Janeiro in 1807 and ruled the empire from Brazil until 1821.',
  R(1799, 1806, 'Prince regent of Portugal', 'Portugal', at='lisbon'),
  G(1807, 1821, 'Ruling the empire from Rio', ('lisbon', 1807.9), ('salvador', 1808.06), ('rio', 1808.18), ('rio', 1821.32), ('lisbon', 1821.5)),
  R(1822, 1826, KP, 'Portugal', at='lisbon'))
K('António de Oliveira Salazar', 'Prime minister of Portugal', (1889, 1970), 1932, 1968,
  'Economics professor who ruled Portugal as a dictator for 36 years and clung on to its African colonies.', 'Portugal', at='lisbon')
P('Mário Soares', 'President of Portugal', (1924, 2017), 3, 'rule',
  'Socialist who led Portugal to democracy after the Carnation Revolution of 1974.',
  R(1976, 1978, 'Prime minister of Portugal', 'Portugal', at='lisbon'), R(1983, 1996, 'Prime minister, then president', 'Portugal', at='lisbon'))

# ---------- the Low Countries ----------
K('Johan van Oldenbarnevelt', "Land's Advocate of Holland", (1547, 1619), 1586, 1618,
  'Steered the young Dutch Republic and founded its East India Company; beheaded after a feud with Prince Maurice.', *DUT, at='the_hague')
K('Maurice, Prince of Orange', 'Stadtholder of the Dutch Republic', (1567, 1625), 1585, 1625,
  "William the Silent's son, who drilled the Dutch army into Europe's best and held the north free of Spain.", *DUT, at='the_hague', tags='rule war')
K('Frederick Henry, Prince of Orange', 'Stadtholder of the Dutch Republic', (1584, 1647), 1625, 1647,
  'Took the great fortresses of the south and brought Spain to the point of recognising Dutch independence.', *DUT, at='the_hague')
K('Johan de Witt', 'Grand Pensionary of Holland', (1625, 1672), 1653, 1672,
  "Ran the Dutch Republic in its golden age; lynched by a mob in The Hague in the 'disaster year' of 1672.", *DUT, at='the_hague')
K('William I of the Netherlands', 'King of the Netherlands', (1772, 1843), 1815, 1840,
  'First king of the Netherlands, who lost Belgium to its revolution in 1830.', 'Netherlands', at='the_hague')
P('Wilhelmina of the Netherlands', 'Queen of the Netherlands', (1880, 1962), 2, 'rule',
  'Queen for 58 years, who led the Dutch resistance to the Nazis over the radio from London.',
  R(1890, 1948, 'Queen of the Netherlands', 'Netherlands', at='the_hague'),
  G(1940, 1945, 'In exile in London', ('the_hague', 1940.36), ('london', 1940.37), ('london', 1945.2), ('the_hague', 1945.3)))
K('Juliana of the Netherlands', 'Queen of the Netherlands', (1909, 2004), 1948, 1980,
  "Spent the war in Ottawa, then reigned 32 years as the down-to-earth 'bicycle queen'.", 'Netherlands', at='the_hague')
K('Beatrix of the Netherlands', 'Queen of the Netherlands', (1938, None), 1980, 2013,
  'Reigned 33 years and handed the throne to her son in 2013.', 'Netherlands', at='the_hague')
K('Willem-Alexander of the Netherlands', 'King of the Netherlands', (1967, None), 2013, 2026,
  'The first Dutch king in more than a century, since 2013.', 'Netherlands', at='the_hague')
K('Leopold I of Belgium', 'King of the Belgians', (1790, 1865), 1831, 1865,
  'German prince chosen as the first king of newly independent Belgium.', 'Belgium', at='brussels')
K('Albert I of Belgium', 'King of the Belgians', (1875, 1934), 1909, 1934,
  "The 'Soldier King', who held the last corner of free Belgium against the German invasion of 1914.", 'Belgium', at='brussels', tags='rule war')

# ---------- Italy ----------
K('Umberto I of Italy', 'King of Italy', (1844, 1900), 1878, 1900,
  'Second king of united Italy, shot dead by an anarchist in 1900.', *IT, at='rome')
K('Victor Emmanuel III', 'King of Italy', (1869, 1947), 1900, 1946,
  'Made Mussolini prime minister in 1922 and had him arrested in 1943.', *IT, at='rome')
K('Alcide De Gasperi', 'Prime minister of Italy', (1881, 1954), 1945, 1953,
  'Christian Democrat who rebuilt Italy after the war and helped found the first European community.', 'Italy', at='rome')
P('Aldo Moro', 'Prime minister of Italy', (1916, 1978), 3, 'rule',
  'Five-time prime minister of Italy, kidnapped and killed by the Red Brigades in 1978.',
  R(1963, 1968, 'Prime minister of Italy', 'Italy', at='rome'), R(1974, 1976, 'Prime minister of Italy', 'Italy', at='rome'))
P('Silvio Berlusconi', 'Prime minister of Italy', (1936, 2023), 3, 'rule',
  'Media tycoon who led four Italian governments between 1994 and 2011.',
  R(1994, 1995, 'Prime minister of Italy', 'Italy', at='rome'), R(2001, 2006, 'Prime minister of Italy', 'Italy', at='rome'),
  R(2008, 2011, 'Prime minister of Italy', 'Italy', at='rome'))
K('Giorgia Meloni', 'Prime minister of Italy', (1977, None), 2022, 2026,
  "Italy's first woman prime minister, since 2022.", 'Italy', at='rome')

# ---------- the popes ----------
POPE = 'Pope'
K('Pope Boniface VIII', POPE, (1230, 1303), 1294, 1303,
  'Claimed power over every king on earth and was seized at Anagni by agents of the French king in 1303.', *PAP, at='rome', tags='faith rule')
P('Pope Clement V', POPE, (1264, 1314), 3, 'faith rule',
  'French pope who moved the papacy to Avignon and helped the French king destroy the Knights Templar.',
  G(1305, 1314, 'The popes move to Avignon', ('lyon', 1305.87), ('bordeaux', 1306.5), ('poitiers', 1307.4), ('avignon', 1309.2)))
P('Pope Gregory XI', POPE, (1329, 1378), 3, 'faith rule',
  'Brought the papacy back from Avignon to Rome in 1377, urged on by Catherine of Siena.',
  G(1370, 1378, 'From Avignon back to Rome', ('avignon', 1370.0), ('avignon', 1376.7), ('marseille', 1376.75), ('rome', 1377.04)))
K('Pope Martin V', POPE, (1369, 1431), 1417, 1431,
  'Elected at the Council of Constance in 1417, ending the Great Schism of three rival popes.', *PAP, at='rome', tags='faith rule')
K('Pope Nicholas V', POPE, (1397, 1455), 1447, 1455,
  'Scholar pope who founded the Vatican Library.', *PAP, at='rome', tags='faith rule')
K('Pope Pius II', POPE, (1405, 1464), 1458, 1464,
  'Humanist writer who died at Ancona trying to launch a crusade to win back Constantinople.', *PAP, at='rome', tags='faith rule')
K('Pope Sixtus IV', POPE, (1414, 1484), 1471, 1484,
  'Built the Sistine Chapel and backed the Pazzi plot to murder the Medici.', *PAP, at='rome', tags='faith rule')
K('Pope Alexander VI', POPE, (1431, 1503), 1492, 1503,
  'Rodrigo Borgia, who divided the New World between Spain and Portugal and carved out a state for his son Cesare.', *PAP, at='rome', tags='faith rule', rank=2)
K('Pope Julius II', POPE, (1443, 1513), 1503, 1513,
  "The 'warrior pope', who led his own armies, began the new St Peter's and had Michelangelo paint the Sistine ceiling.", *PAP, at='rome',
  tags='faith rule art', rank=2)
K('Pope Leo X', POPE, (1475, 1521), 1513, 1521,
  "Medici pope who sold indulgences to pay for St Peter's and excommunicated Martin Luther.", *PAP, at='rome', tags='faith rule', rank=2)
K('Pope Clement VII', POPE, (1478, 1534), 1523, 1534,
  'Medici pope who saw Rome sacked by imperial troops in 1527 and refused Henry VIII his divorce.', *PAP, at='rome', tags='faith rule')
K('Pope Paul III', POPE, (1468, 1549), 1534, 1549,
  'Called the Council of Trent to answer the Protestants and approved the Jesuits.', *PAP, at='rome', tags='faith rule')
K('Pope Gregory XIII', POPE, (1502, 1585), 1572, 1585,
  'Gave the world the Gregorian calendar in 1582.', *PAP, at='rome', tags='faith rule mind')
K('Pope Sixtus V', POPE, (1521, 1590), 1585, 1590,
  "Rebuilt Rome's streets and raised the obelisk in St Peter's Square.", *PAP, at='rome', tags='faith rule')
K('Pope Urban VIII', POPE, (1568, 1644), 1623, 1644,
  'Barberini pope who had Galileo tried by the Inquisition in 1633.', *PAP, at='rome', tags='faith rule')
K('Pope Innocent XI', POPE, (1611, 1689), 1676, 1689,
  'Built the Holy League that saved Vienna from the Turks in 1683.', *PAP, at='rome', tags='faith rule')
K('Pope Benedict XIV', POPE, (1675, 1758), 1740, 1758,
  'Scholarly pope admired even by Voltaire.', *PAP, at='rome', tags='faith rule')
K('Pope Clement XIV', POPE, (1705, 1774), 1769, 1774,
  'Abolished the Jesuit order in 1773 under pressure from the Catholic kings.', *PAP, at='rome', tags='faith rule')
P('Pope Pius VI', POPE, (1717, 1799), 3, 'faith rule',
  'Carried off by the armies of revolutionary France in 1798; he died their prisoner at Valence.',
  R(1775, 1797, POPE, *PAP, at='rome'),
  G(1798, 1799, 'Prisoner of the French', ('rome', 1798.15), ('florence', 1798.4), ('florence', 1799.2), ('turin', 1799.3), ((4.89, 44.93, 1799.53))))
P('Pope Pius VII', POPE, (1742, 1823), 3, 'faith rule',
  'Crowned Napoleon emperor in 1804, was then kidnapped by him and held prisoner for five years.',
  R(1800, 1808, POPE, *PAP, at='rome'),
  G(1809, 1814, "Napoleon's prisoner", ('rome', 1809.51), ((8.48, 44.31, 1809.62)), ((8.48, 44.31, 1812.42)), ((2.7, 48.4, 1812.47)), ((2.7, 48.4, 1814.1)),
    ('rome', 1814.39)),
  R(1815, 1823, POPE, *PAP, at='rome'))
K('Pope Gregory XVI', POPE, (1765, 1846), 1831, 1846,
  'Arch-conservative pope who banned railways from the Papal States.', *PAP, at='rome', tags='faith rule')
P('Pope Leo XIII', POPE, (1810, 1903), 3, 'faith reform',
  "Wrote Rerum novarum in 1891, the Church's first great letter on the rights of workers.", G(1878, 1903, 'Pope in the Vatican', 'rome'))
P('Pope Pius XII', POPE, (1876, 1958), 3, 'faith',
  'Pope through the Second World War, criticised for keeping publicly silent about the Holocaust.', G(1939, 1958, 'Pope in the Vatican', 'rome'))
P('Pope John XXIII', POPE, (1881, 1963), 3, 'faith reform',
  "'Good Pope John', who opened the Second Vatican Council in 1962 to bring the Church up to date.", G(1958, 1963, 'Pope in the Vatican', 'rome'))
P('Pope Benedict XVI', POPE, (1927, 2022), 3, 'faith',
  'German theologian who in 2013 became the first pope to resign in six hundred years.', G(2005, 2013, 'Pope in the Vatican', 'rome'))
P('Pope Francis', POPE, (1936, 2025), 2, 'faith reform',
  'Argentine Jesuit, the first pope from the Americas, who championed the poor and the planet.', G(2013, 2025, 'Pope in the Vatican', 'rome'))
P('Pope Leo XIV', POPE, (1955, None), 3, 'faith',
  'Robert Prevost of Chicago, elected in 2025 as the first pope from the United States.', G(2025, 2026, 'Pope in the Vatican', 'rome'))

# ---------- Venice ----------
K('Pietro II Orseolo', 'Doge of Venice', (961, 1009), 991, 1009,
  'Doge who made Venice master of the Dalmatian coast in the year 1000.', 'Venice', at='venice')
P('Enrico Dandolo', 'Doge of Venice', (1107, 1205), 3, 'rule war',
  'Blind doge in his nineties who steered the Fourth Crusade into sacking Constantinople in 1204.',
  R(1192, 1201, 'Doge of Venice', 'Venice', at='venice'),
  G(1202, 1205, 'The Fourth Crusade', ('venice', 1202.8), ((15.23, 44.12, 1202.87)), ((15.23, 44.12, 1203.3)), ('constantinople', 1203.48),
    ('constantinople', 1205.42)))
K('Francesco Foscari', 'Doge of Venice', (1373, 1457), 1423, 1457,
  'Longest-serving doge, who won Venice its empire on the Italian mainland.', 'Venice', at='venice')
K('Leonardo Loredan', 'Doge of Venice', (1436, 1521), 1501, 1521,
  'Doge who held Venice together when half of Europe allied against it in 1508; painted by Giovanni Bellini.', 'Venice', at='venice')
K('Ludovico Manin', 'Doge of Venice', (1725, 1802), 1789, 1797,
  'Last doge of Venice, who gave up the thousand-year-old republic to Napoleon in 1797.', 'Venice', at='venice')


# ---------- filling the years between the reigns above ----------
# France
K('Louis X of France', KF, (1289, 1316), 1314, 1316,
  "'The Quarreller', whose short reign let serfs on the royal lands buy their freedom.", *FR, at='paris')
K('Paul Barras', 'Director of the French Republic', (1755, 1829), 1795, 1799,
  'The most powerful of the five Directors who ran France after the Terror, and the patron of young Napoleon.', 'France', at='paris')
P('Léon Gambetta', 'Prime minister of France', (1838, 1882), 3, 'rule',
  'Escaped besieged Paris by balloon in 1870 to raise new armies against Prussia, and later led the young Third Republic.',
  G(1870, 1871, 'By balloon out of besieged Paris', ('paris', 1870.76), ((2.55, 49.4, 1870.77)), ((0.69, 47.39, 1870.78)), ((0.69, 47.39, 1870.94)),
    ('bordeaux', 1870.95), ('bordeaux', 1871.1)),
  R(1881, 1882, 'Prime minister of France', 'France', at='paris'))
K('Jules Grévy', 'President of France', (1807, 1891), 1879, 1887,
  'First president of the Third Republic to serve a full term, brought down when his son-in-law was caught selling medals.', 'France', at='paris')
K('Sadi Carnot', 'President of France', (1837, 1894), 1887, 1894,
  'President of France stabbed to death by an Italian anarchist in Lyon in 1894.', 'France', at='paris', wiki='Sadi Carnot (statesman)')
K('Félix Faure', 'President of France', (1841, 1899), 1895, 1899,
  'President during the Dreyfus affair, who died suddenly in the Élysée Palace in 1899.', 'France', at='paris')
K('Émile Loubet', 'President of France', (1838, 1929), 1899, 1906,
  'Pardoned Alfred Dreyfus in 1899 and saw church and state separated by law in 1905.', 'France', at='paris')
K('Armand Fallières', 'President of France', (1841, 1931), 1906, 1913,
  'Easygoing president in the years when France drew close to Britain and Russia.', 'France', at='paris')
P('Aristide Briand', 'Prime minister of France', (1862, 1932), 3, 'rule reform',
  'Prime minister eleven times, who made peace with Germany at Locarno and won the Nobel Peace Prize in 1926.',
  R(1921, 1922, 'Prime minister of France', 'France', at='paris'), R(1925, 1932, 'Foreign minister of France', 'France', at='paris'))
K('Gaston Doumergue', 'President of France', (1863, 1937), 1924, 1931,
  'First Protestant president of France.', 'France', at='paris')
K('Paul Doumer', 'President of France', (1857, 1932), 1931, 1932,
  'Former governor of Indochina, shot dead by a Russian émigré a year into his presidency.', 'France', at='paris')
K('Albert Lebrun', 'President of France', (1871, 1950), 1932, 1940,
  'Last president of the Third Republic, which ended when France fell to Germany in 1940.', 'France', at='paris')
K('Vincent Auriol', 'President of France', (1884, 1966), 1947, 1954,
  'First president of the Fourth Republic after the Second World War.', 'France', at='paris')
K('René Coty', 'President of France', (1882, 1962), 1954, 1959,
  'Last president of the Fourth Republic, who called de Gaulle back to power in 1958.', 'France', at='paris')
K('Pierre Mendès France', 'Prime minister of France', (1907, 1982), 1954, 1955,
  'Ended the French war in Indochina in 1954.', 'France', at='paris')

# England
K('Richard Cromwell', 'Lord Protector', (1626, 1712), 1658, 1659,
  "Oliver Cromwell's son, 'Tumbledown Dick', who lost power within a year and opened the way for the king's return.", *GB1, at='westminster')
K('Mary II', 'Queen of England, Scotland and Ireland', (1662, 1694), 1689, 1694,
  'Daughter of James II, who took his throne with her husband William of Orange in the Glorious Revolution.', *GB1, at='westminster')

# Navarre, Castile and Spain
K('Sancho III of Pamplona', 'King of Pamplona', (992, 1035), 1004, 1035,
  "'The Great', king of Navarre, who ruled most of Christian Spain by his death and left Castile and Aragon to his sons.", 'Navarre', *CAS,
  at=(-1.64, 42.82))
K('Sancho II of Castile', 'King of Castile', (1036, 1072), 1065, 1072,
  "King served by El Cid, who took his brothers' kingdoms and was murdered at the siege of Zamora.", *CAS, at='burgos')
K('Sancho IV of Castile', 'King of Castile', (1258, 1295), 1284, 1295,
  "'The Brave', who seized the crown from his father Alfonso X and held Tarifa against the Moroccans.", *CAS, at='toledo')
K('María de Molina', 'Queen and regent of Castile', (1265, 1321), 1295, 1301,
  'Widow of Sancho IV who held Castile together as regent for her son and then for her grandson.', *CAS, at='valladolid')
K('Ferdinand IV of Castile', 'King of Castile', (1285, 1312), 1302, 1312,
  "'The Summoned', who took Gibraltar from the Moors in 1309.", *CAS, at='burgos')
K('Henry II of Castile', 'King of Castile', (1334, 1379), 1369, 1379,
  'Bastard brother of Peter the Cruel, whom he stabbed to death at Montiel in 1369 to take his throne.', *CAS, at='burgos', tags='rule war')
K('John I of Castile', 'King of Castile', (1358, 1390), 1379, 1390,
  'Tried to take the crown of Portugal and was crushed at Aljubarrota in 1385.', *CAS, at='burgos')
K('Henry III of Castile', 'King of Castile', (1379, 1406), 1390, 1406,
  'Sent an embassy to Timur in Samarkand and backed the conquest of the Canary Islands.', *CAS, at='burgos')
K('Juan Prim', 'Prime minister of Spain', (1814, 1870), 1869, 1870,
  'General who overthrew Isabella II, searched Europe for a new king and was shot dead in Madrid in 1870.', 'Spain', at='madrid')
K('Amadeo I of Spain', 'King of Spain', (1845, 1890), 1871, 1873,
  'Italian prince chosen king of Spain, who gave up after two years, calling the Spanish ungovernable.', 'Spain', at='madrid')
K('Niceto Alcalá-Zamora', 'President of Spain', (1877, 1949), 1931, 1936,
  'First president of the Second Spanish Republic.', 'Spain', at='madrid')

# Portugal
PT = ('Portugal',)
K('Sancho I of Portugal', KP, (1154, 1211), 1185, 1211,
  "'The Populator', who settled the lands his father had won from the Moors.", *PT, at='coimbra')
K('Afonso II of Portugal', KP, (1185, 1223), 1211, 1223,
  "'The Fat', who gave Portugal its first written laws and quarrelled with the pope.", *PT, at='coimbra')
K('Sancho II of Portugal', KP, (1209, 1248), 1223, 1247,
  'Won much of the Alentejo and the Algarve from the Moors, but was deposed by the pope and his own brother.', *PT, at='coimbra')
K('Afonso III of Portugal', KP, (1210, 1279), 1248, 1279,
  'Took the Algarve in 1249, completing the Portuguese reconquest, and made Lisbon the capital.', *PT, at='lisbon')
K('Afonso IV of Portugal', KP, (1291, 1357), 1325, 1357,
  "Fought beside Castile at the Río Salado in 1340, and had his son's beloved Inês de Castro murdered.", *PT, at='lisbon')
K('Peter I of Portugal', KP, (1320, 1367), 1357, 1367,
  'Took revenge on the murderers of Inês de Castro; legend says he had her dead body crowned queen.', *PT, at='lisbon')
K('Ferdinand I of Portugal', KP, (1345, 1383), 1367, 1383,
  'Lost three wars with Castile; his death without a son led to the crisis that put John I on the throne.', *PT, at='lisbon')
K('Edward of Portugal', KP, (1391, 1438), 1433, 1438,
  "'The Philosopher King', who wrote a book on good counsel and saw his brother taken prisoner at Tangier.", *PT, at='lisbon',
  wiki='Edward, King of Portugal')
K('Henry, King of Portugal', 'Cardinal and king of Portugal', (1512, 1580), 1578, 1580,
  'Elderly cardinal who became king after Sebastian vanished in Morocco; his death let Philip II of Spain take Portugal.', *PT, at='lisbon',
  tags='rule faith')
K('Afonso VI of Portugal', KP, (1643, 1683), 1656, 1667,
  'Paralysed in childhood, he won the war of independence from Spain and was then pushed aside by his brother.', *PT, at='lisbon')
K('Peter II of Portugal', KP, (1648, 1706), 1668, 1706,
  'Made peace with Spain in 1668 and grew rich on the gold found in Brazil.', *PT, at='lisbon')
K('John V of Portugal', KP, (1689, 1750), 1706, 1750,
  "'The Magnanimous', who spent Brazil's gold on the vast palace of Mafra.", *PT, at='lisbon')
K('Joseph I of Portugal', KP, (1714, 1777), 1750, 1777,
  'King when the great earthquake of 1755 destroyed Lisbon; he left the rebuilding, and the country, to Pombal.', *PT, at='lisbon')
K('Miguel I of Portugal', KP, (1802, 1866), 1828, 1834,
  'Seized the throne from his niece Maria II and lost it in a civil war to his brother Pedro.', *PT, at='lisbon')
K('Maria II of Portugal', 'Queen of Portugal', (1819, 1853), 1834, 1853,
  'Born in Rio, made queen at seven, and put back on the throne by her father Pedro after the civil war.', *PT, at='lisbon')
K('Pedro V of Portugal', KP, (1837, 1861), 1853, 1861,
  'Well-loved young king who built railways and died of typhoid at 24.', *PT, at='lisbon')
K('Luís I of Portugal', KP, (1838, 1889), 1861, 1889,
  'Scholar king who translated Shakespeare and ended slavery in the Portuguese empire.', *PT, at='lisbon')
K('Carlos I of Portugal', KP, (1863, 1908), 1889, 1908,
  'Painter and ocean scientist, shot dead with his heir in a Lisbon square in 1908.', *PT, at='lisbon')
K('Manuel II of Portugal', KP, (1889, 1932), 1908, 1910,
  'Last king of Portugal, overthrown by the republican revolution of 1910 and exiled to England.', *PT, at='lisbon')
K('Sidónio Pais', 'President of Portugal', (1872, 1918), 1917, 1918,
  "Army officer who seized power and ruled as the 'President-King' until he was shot at a Lisbon station.", *PT, at='lisbon')
K('Óscar Carmona', 'President of Portugal', (1869, 1951), 1926, 1951,
  'General who led the coup of 1926 and stayed president while Salazar ran the country.', *PT, at='lisbon')
K('Marcelo Caetano', 'Prime minister of Portugal', (1906, 1980), 1968, 1974,
  "Salazar's successor, overthrown by the army in the Carnation Revolution of 1974.", *PT, at='lisbon')
K('António Ramalho Eanes', 'President of Portugal', (1935, None), 1976, 1986,
  'General who stopped a far-left coup in 1975 and became the first elected president of democratic Portugal.', *PT, at='lisbon')
K('Jorge Sampaio', 'President of Portugal', (1939, 2021), 1996, 2006,
  'Socialist president who pushed the world to rescue East Timor in 1999.', *PT, at='lisbon')
P('Aníbal Cavaco Silva', 'Prime minister and president of Portugal', (1939, None), 3, 'rule',
  "Led Portugal's government for its first ten years in the European Community, then served two terms as president.",
  R(1985, 1995, 'Prime minister of Portugal', *PT, at='lisbon'), R(2006, 2016, 'President of Portugal', *PT, at='lisbon'))
P('António Guterres', 'Secretary-General of the United Nations', (1949, None), 3, 'rule',
  'Prime minister of Portugal, then the UN refugee chief, then Secretary-General of the United Nations from 2017.',
  R(1995, 2002, 'Prime minister of Portugal', *PT, at='lisbon'), G(2005, 2015, 'UN High Commissioner for Refugees', 'geneva'),
  G(2017, 2026, 'Secretary-General of the United Nations', 'new_york'))
K('Marcelo Rebelo de Sousa', 'President of Portugal', (1948, None), 2016, 2026,
  'Television commentator turned president, famous for his selfies and his swims in the sea.', *PT, at='lisbon')
P('António Costa', 'President of the European Council', (1961, None), 3, 'rule',
  'Socialist prime minister of Portugal for eight years, then president of the European Council from 2024.',
  R(2015, 2023, 'Prime minister of Portugal', *PT, at='lisbon'), G(2024, 2026, 'President of the European Council', 'brussels'))
K('António José Seguro', 'President of Portugal', (1962, None), 2026, 2026,
  'Socialist who beat the far-right candidate in a landslide in February 2026.', *PT, at='lisbon')

# the Low Countries
K('William II, Prince of Orange', 'Stadtholder of the Dutch Republic', (1626, 1650), 1647, 1650,
  'Stadtholder who tried to seize Amsterdam by force in 1650 and died of smallpox weeks later.', *DUT, at='the_hague')
K('Anthonie Heinsius', 'Grand Pensionary of Holland', (1641, 1720), 1689, 1720,
  'Ran the Dutch Republic for William III and held the alliance against Louis XIV together.', *DUT, at='the_hague')
K('William IV, Prince of Orange', 'Stadtholder of the Dutch Republic', (1711, 1751), 1747, 1751,
  'Made stadtholder of all seven provinces when France invaded in 1747.', *DUT, at='the_hague')
K('William V, Prince of Orange', 'Stadtholder of the Dutch Republic', (1748, 1806), 1766, 1795,
  'Last stadtholder, who fled to England when the French marched in in 1795.', *DUT, at='the_hague')
K('Louis Bonaparte', 'King of Holland', (1778, 1846), 1806, 1810,
  "Napoleon's brother, made king of Holland, who sided with his subjects so often that Napoleon took the country from him.",
  'Batavian Republic', *DUT, at='the_hague')
K('William II of the Netherlands', 'King of the Netherlands', (1792, 1849), 1840, 1849,
  'Fought at Waterloo as a young general and gave the Netherlands a liberal constitution in 1848.', *DUT, at='the_hague')
K('William III of the Netherlands', 'King of the Netherlands', (1817, 1890), 1849, 1890,
  'Reigned 41 years, the last king of the Netherlands for more than a century.', *DUT, at='the_hague')
K('Rob Jetten', 'Prime minister of the Netherlands', (1987, None), 2026, 2026,
  'Liberal who became the youngest Dutch prime minister in February 2026.', 'Netherlands', at='the_hague')

# Italy
K('Luigi Einaudi', 'President of Italy', (1874, 1961), 1948, 1955,
  'Economist who became the first elected president of the Italian Republic.', *IT, at='rome')
P('Amintore Fanfani', 'Prime minister of Italy', (1908, 1999), 3, 'rule',
  "Christian Democrat who led Italy's government five times between 1954 and 1987.",
  R(1954, 1954, 'Prime minister of Italy', *IT, at='rome'), R(1958, 1959, 'Prime minister of Italy', *IT, at='rome'),
  R(1960, 1963, 'Prime minister of Italy', *IT, at='rome'))
P('Giulio Andreotti', 'Prime minister of Italy', (1919, 2013), 3, 'rule',
  'Seven times prime minister and a power in Italian politics for half a century.',
  R(1972, 1973, 'Prime minister of Italy', *IT, at='rome'), R(1976, 1979, 'Prime minister of Italy', *IT, at='rome'),
  R(1989, 1992, 'Prime minister of Italy', *IT, at='rome'))
K('Sandro Pertini', 'President of Italy', (1896, 1990), 1978, 1985,
  'Anti-fascist partisan who became the best-loved president of Italy.', *IT, at='rome')
P('Bettino Craxi', 'Prime minister of Italy', (1934, 2000), 3, 'rule',
  'Socialist prime minister who fled to Tunisia when the great bribery scandal of the 1990s broke.',
  R(1983, 1987, 'Prime minister of Italy', *IT, at='rome'), G(1994, 2000, 'In exile at Hammamet', (10.6, 36.4)))
K('Francesco Cossiga', 'President of Italy', (1928, 2010), 1985, 1992,
  'Interior minister during the kidnapping of Aldo Moro, later a president famous for his outbursts.', *IT, at='rome')
P('Carlo Azeglio Ciampi', 'President of Italy', (1920, 2016), 3, 'rule',
  'Central banker who led the government through the crisis of 1993, took Italy into the euro and became president.',
  R(1993, 1994, 'Prime minister of Italy', *IT, at='rome'), R(1999, 2006, 'President of Italy', *IT, at='rome'))
P('Romano Prodi', 'Prime minister of Italy', (1939, None), 3, 'rule',
  'Twice beat Berlusconi to lead Italy, and was president of the European Commission when the euro arrived.',
  R(1996, 1998, 'Prime minister of Italy', *IT, at='rome'), G(1999, 2004, 'President of the European Commission', 'brussels'),
  R(2006, 2008, 'Prime minister of Italy', *IT, at='rome'))
K('Giorgio Napolitano', 'President of Italy', (1925, 2023), 2006, 2015,
  'Former communist who became the first Italian president to be elected twice.', *IT, at='rome')
K('Matteo Renzi', 'Prime minister of Italy', (1975, None), 2014, 2016,
  'Became prime minister at 39 and resigned when he lost a referendum on his reforms.', *IT, at='rome')
K('Sergio Mattarella', 'President of Italy', (1941, None), 2015, 2026,
  'Sicilian law professor and judge whose brother was murdered by the Mafia; president of Italy since 2015.', *IT, at='rome')
P('Mario Draghi', 'Prime minister of Italy', (1947, None), 3, 'rule',
  "Saved the euro by promising to do 'whatever it takes' as head of the European Central Bank, then led Italy's government.",
  G(2011, 2019, 'President of the European Central Bank', 'frankfurt'), R(2021, 2022, 'Prime minister of Italy', *IT, at='rome'))


# more popes
def PP(name, life, a, b, why):
    K(name, POPE, life, a, b, why, *PAP, at='rome', tags='faith rule')


PP('Pope Callixtus II', (1065, 1124), 1119, 1124, 'Ended the long fight with the emperors over who appoints bishops, at Worms in 1122.')
PP('Pope Adrian IV', (1100, 1159), 1154, 1159, 'The only English pope, who crowned Frederick Barbarossa and then quarrelled with him.')
PP('Pope Alexander III', (1100, 1181), 1159, 1181, 'Outlasted four rival popes and made Barbarossa kneel to him at Venice in 1177.')
PP('Pope Gregory IX', (1145, 1241), 1227, 1241, 'Set up the papal Inquisition and excommunicated Emperor Frederick II twice.')
P('Pope Innocent IV', POPE, (1195, 1254), 3, 'faith rule',
  'Fled to Lyon, declared Emperor Frederick II deposed at a council there, and sent friars to the Mongol khan.',
  R(1243, 1243, POPE, *PAP, at='rome'),
  G(1244, 1251, 'Exile in Lyon', ('rome', 1244.45), ('genoa', 1244.55), ('lyon', 1244.92), ('lyon', 1251.3)),
  R(1252, 1254, POPE, *PAP, at='rome'))
PP('Pope Gregory X', (1210, 1276), 1271, 1276, 'Elected pope while at Acre in 1271; he sent the Polos back to Kublai Khan with his letters.')
PP('Pope Celestine V', (1210, 1296), 1294, 1294, 'An old hermit made pope, who resigned after five months; Dante seems to have put him in hell for it.')
P('Pope John XXII', POPE, (1244, 1334), 3, 'faith rule',
  'Avignon pope who filled the papal treasury, fought the Franciscans over poverty and was still pope at ninety.',
  G(1316, 1334, 'Pope at Avignon', 'avignon'))
PP('Pope Urban VI', (1318, 1389), 1378, 1389, 'His violent temper drove the cardinals to elect a rival pope, starting the Great Schism of the West.')
P('Pope Eugene IV', POPE, (1383, 1447), 3, 'faith rule',
  'Driven out of Rome by a revolt, he held the council at Florence that briefly reunited the Greek and Latin churches.',
  R(1431, 1433, POPE, *PAP, at='rome'), G(1434, 1443, 'Exile in Florence', 'florence'), R(1444, 1447, POPE, *PAP, at='rome'))
PP('Pope Callixtus III', (1378, 1458), 1455, 1458, 'First Borgia pope, who ordered the retrial that cleared Joan of Arc.')
PP('Pope Innocent VIII', (1432, 1492), 1484, 1492, 'Issued the bull against witchcraft of 1484 and openly raised his children at court.')
PP('Pope Adrian VI', (1459, 1523), 1522, 1523, 'Dutch tutor of Charles V and the last pope from outside Italy for over four centuries.')
PP('Pope Paul IV', (1476, 1559), 1555, 1559, "Fierce reformer who walled Rome's Jews into a ghetto and drew up the Index of forbidden books.")
PP('Pope Pius IV', (1499, 1565), 1559, 1565, 'Brought the Council of Trent to a close in 1563.')
PP('Pope Pius V', (1504, 1572), 1566, 1572, 'Built the Holy League that beat the Turks at Lepanto, and excommunicated Elizabeth I.')
PP('Pope Clement VIII', (1536, 1605), 1592, 1605, 'Took Henry IV of France back into the Church and had Giordano Bruno burned in 1600.')
PP('Pope Paul V', (1550, 1621), 1605, 1621, "Finished the front of St Peter's and had Galileo warned off Copernicus in 1616.")
PP('Pope Innocent X', (1574, 1655), 1644, 1655, 'Condemned the Peace of Westphalia; his portrait by Velázquez is one of the great paintings of the age.')
PP('Pope Alexander VII', (1599, 1667), 1655, 1667, "Had Bernini build the colonnade of St Peter's Square and welcomed Queen Christina to Rome.")
PP('Pope Clement XI', (1649, 1721), 1700, 1721, "Condemned the Jesuits' acceptance of Chinese rites and the Jansenists in France.")
PP('Pope Clement XII', (1652, 1740), 1730, 1740, 'Blind for most of his reign, he began the Trevi Fountain and first condemned the Freemasons.')
PP('Pope Clement XIII', (1693, 1769), 1758, 1769, 'Defended the Jesuits as they were thrown out of Portugal, France and Spain.')

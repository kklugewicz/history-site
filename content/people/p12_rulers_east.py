"""Heads of state of Asia and the Middle East between the famous ones in the era files, so a country's name on the map has
its ruler beside it in nearly every year: the Seljuks, Mamluks and Ottomans, Persia, India and its neighbours, Afghanistan,
the modern Middle East, China, the steppe and Tibet, Japan, Korea and Southeast Asia."""
from _lib import P, R, G


def K(name, role, life, a, b, why, *names, at, rank=3, tags='rule', wiki=None):
    """one reign: the ruler sits by the first of `names` on the map from year a to b, or at `at` when none is"""
    P(name, role, life, rank, tags, why, R(a, b, role, *names, at=at), wiki=wiki)


OT = ('Ottoman Empire', 'Ottoman Sultanate', 'Turkey', 'Republic of Turkey')
TR = ('Turkey', 'Republic of Turkey')
SEL = ('Seljuk Empire',)
MAM = ('Mamluke Sultanate', 'Egypt')
ILK = ('Ilkhanate',)
TIM = ('Timurid Empire', 'Timurid Emirates')
SAF = ('Safavid Empire',)
QAJ = ('Persia', 'Iran')
DS = ('Sultanate of Delhi',)
MUG = ('Mughal Empire',)
MAR = ('Maratha', 'Maratha Confederacy')
BI = ('Bengal', 'British East India Company', 'British Raj', 'India')
SULTAN, SHAH = 'Ottoman sultan', 'Shah of Persia'
QAZVIN, SATARA = (49.99, 36.27), (74.0, 17.68)

# ---------- the Seljuks, the Zengids and the Mamluks ----------
K('Tughril', 'Sultan of the Seljuks', (990, 1063), 1037, 1063,
  'Turkish chief who conquered Persia, entered Baghdad in 1055 and was named sultan by the caliph.', *SEL, at=(51.43, 35.59),
  tags='rule war')
K('Malik-Shah I', 'Sultan of the Seljuks', (1055, 1092), 1072, 1092,
  'Ruled the Seljuk empire at its height, from Syria to Central Asia, with his vizier Nizam al-Mulk; Omar Khayyam reformed his calendar.',
  *SEL, at='isfahan')
K('Ahmad Sanjar', 'Sultan of the Seljuks', (1086, 1157), 1118, 1157,
  'Last great Seljuk sultan, beaten by the Kara-Khitai on the Qatwan steppe in 1141 and later held captive by nomads.', *SEL,
  at=(61.83, 37.66))
P('Zengi', 'Atabeg of Mosul and Aleppo', (1085, 1146), 3, 'war rule',
  'Turkish warlord whose capture of the crusader city of Edessa in 1144 set off the Second Crusade.',
  G(1127, 1143, 'Atabeg of Mosul and Aleppo', 'mosul'),
  G(1144, 1146, 'The fall of Edessa', ('mosul', 1144.6), ((38.79, 37.15, 1144.98)), ((38.79, 37.15, 1145.1)), ('mosul', 1145.5),
    ((38.48, 35.9, 1146.7))))
P('Nur ad-Din', 'Emir of Syria', (1118, 1174), 3, 'war rule faith',
  "Zengi's son, who united Muslim Syria against the crusaders and sent Saladin's uncle to take Egypt.",
  G(1146, 1153, 'Emir of Aleppo', 'aleppo'), G(1154, 1174, 'Emir of Aleppo and Damascus', 'damascus'), wiki='Nur ad-Din (died 1174)')
P('Qutuz', 'Mamluk sultan of Egypt', (1221, 1260), 3, 'war rule',
  'Mamluk sultan who beat the Mongols at Ain Jalut in 1260, the first great defeat of their armies, and was murdered weeks later.',
  R(1259, 1259, 'Sultan of Egypt', *MAM, at='cairo'),
  G(1260, 1260, 'To Ain Jalut', ('cairo', 1260.5), ((35.36, 32.55, 1260.68)), ('damascus', 1260.72), ((31.97, 30.77, 1260.81))))
K('Qalawun', 'Mamluk sultan of Egypt', (1222, 1290), 1279, 1290,
  'Beat the Mongols at Homs in 1281, took Tripoli from the crusaders and built a great hospital in Cairo.', *MAM, at='cairo')
P('Al-Nasir Muhammad', 'Mamluk sultan of Egypt', (1285, 1341), 3, 'rule',
  'Put on the throne three times; in his long last reign Mamluk Egypt reached its height and Cairo was the greatest city of Islam.',
  R(1293, 1294, 'Sultan of Egypt', *MAM, at='cairo'), R(1299, 1308, 'Sultan of Egypt', *MAM, at='cairo'),
  R(1310, 1341, 'Sultan of Egypt', *MAM, at='cairo'))
K('Barquq', 'Mamluk sultan of Egypt', (1336, 1399), 1382, 1399,
  'First of the Circassian Mamluk sultans, who stood up to Timur.', *MAM, at='cairo')
K('Barsbay', 'Mamluk sultan of Egypt', (1369, 1438), 1422, 1438,
  'Conquered Cyprus in 1426 and brought its king to Cairo as a prisoner.', *MAM, at='cairo')
K('Qaitbay', 'Mamluk sultan of Egypt', (1416, 1496), 1468, 1496,
  'Builder sultan whose fortress still guards the harbour of Alexandria.', *MAM, at='cairo')
P('Qansuh al-Ghawri', 'Mamluk sultan of Egypt', (1441, 1516), 3, 'rule war',
  'Next-to-last Mamluk sultan, who died fighting the Ottomans at Marj Dabiq in 1516.',
  R(1501, 1515, 'Sultan of Egypt', *MAM, at='cairo'),
  G(1516, 1516, 'To Marj Dabiq', ('cairo', 1516.35), ('damascus', 1516.5), ((37.27, 36.53, 1516.64))))
K('Ali Bey al-Kabir', 'Ruler of Egypt', (1728, 1773), 1760, 1772,
  'Mamluk chief who threw off Ottoman rule over Egypt and briefly conquered Syria.', 'Egypt', at='cairo')

# ---------- the Ottomans and Turkey ----------
K('Mehmed I', SULTAN, (1389, 1421), 1413, 1421,
  'Won the civil war among the sons of Bayezid after Timur crushed him, and put the Ottoman state back together.', *OT, at='edirne')
P('Murad II', SULTAN, (1404, 1451), 2, 'rule war',
  'Twice gave up the throne and twice came back to beat the crusaders, at Varna in 1444 and at Kosovo in 1448.',
  R(1421, 1443, SULTAN, *OT, at='edirne'),
  G(1444, 1444, 'The crusade of Varna', ('edirne', 1444.7), ((27.92, 43.21, 1444.86)), ('edirne', 1445.0)),
  R(1446, 1447, SULTAN, *OT, at='edirne'),
  G(1448, 1448, 'Second battle of Kosovo', ('edirne', 1448.6), ((21.1, 42.7, 1448.8)), ('edirne', 1448.95)),
  R(1449, 1451, SULTAN, *OT, at='edirne'))
K('Bayezid II', SULTAN, (1447, 1512), 1481, 1512,
  'Pious sultan who sent his fleet to bring the Jews expelled from Spain in 1492 to safety in his empire.', *OT, at='constantinople')
K('Selim II', SULTAN, (1524, 1574), 1566, 1574,
  "Son of Suleiman and Hürrem, called 'the Sot', who took Cyprus in 1571 and lost his fleet at Lepanto.", *OT, at='constantinople')
K('Sokollu Mehmed Pasha', 'Grand vizier of the Ottoman Empire', (1506, 1579), 1565, 1579,
  'Bosnian-born grand vizier who ran the empire for three sultans and dreamed of a canal at Suez.', *OT, at='constantinople')
K('Murad III', SULTAN, (1546, 1595), 1574, 1595,
  'Sultan who seldom left his harem, while his armies took the Caucasus from Persia.', *OT, at='constantinople')
K('Mehmed III', SULTAN, (1566, 1603), 1595, 1603,
  'Had nineteen of his brothers strangled when he took the throne, then led his army to victory in Hungary.', *OT, at='constantinople')
K('Ahmed I', SULTAN, (1590, 1617), 1603, 1617,
  "Built the Blue Mosque and ended the custom of killing a new sultan's brothers.", *OT, at='constantinople', tags='rule faith')
K('Osman II', SULTAN, (1604, 1622), 1618, 1622,
  'Young sultan who tried to replace the Janissaries and became the first sultan they murdered.', *OT, at='constantinople')
P('Murad IV', SULTAN, (1612, 1640), 3, 'rule war',
  'Stern sultan who banned coffee and tobacco on pain of death and took Baghdad back from Persia in 1638.',
  R(1623, 1637, SULTAN, *OT, at='constantinople'),
  G(1638, 1638, 'To retake Baghdad', ('constantinople', 1638.37), ((40.22, 37.91, 1638.65)), ('mosul', 1638.8), ('baghdad', 1638.88),
    ('baghdad', 1638.99)),
  R(1639, 1640, SULTAN, *OT, at='constantinople'))
K('Kösem Sultan', 'Valide sultan of the Ottoman Empire', (1589, 1651), 1623, 1651,
  'Greek-born wife and mother of sultans, the most powerful woman in Ottoman history, strangled in a palace plot.', *OT,
  at='constantinople')
K('Ibrahim of the Ottoman Empire', SULTAN, (1615, 1648), 1640, 1648,
  "'The Mad', kept locked up for years before he took the throne, then deposed and strangled by his own officials.", *OT,
  at='constantinople')
K('Mehmed IV', SULTAN, (1642, 1693), 1648, 1687,
  "'The Hunter', made sultan at six, whose Köprülü grand viziers revived the empire until the defeat at Vienna in 1683.", *OT,
  at='constantinople')
K('Köprülü Mehmed Pasha', 'Grand vizier of the Ottoman Empire', (1575, 1661), 1656, 1661,
  'Elderly grand vizier who restored order by executing thousands and founded a dynasty of viziers.', *OT, at='constantinople')
K('Suleiman II', SULTAN, (1642, 1691), 1687, 1691,
  'Spent 39 years locked in the palace before he became sultan in the middle of a losing war.', *OT, at='constantinople')
P('Mustafa II', SULTAN, (1664, 1703), 3, 'rule war',
  'Led his own armies against the Habsburgs, was crushed at Zenta in 1697 and signed away Hungary at Karlowitz.',
  R(1695, 1696, SULTAN, *OT, at='edirne'),
  G(1697, 1697, 'The Zenta campaign', ('edirne', 1697.4), ('belgrade', 1697.6), ((20.08, 45.93, 1697.69)), ('edirne', 1697.85)),
  R(1698, 1703, SULTAN, *OT, at='edirne'))
K('Ahmed III', SULTAN, (1673, 1736), 1703, 1730,
  "Sheltered Charles XII of Sweden and reigned in the 'Tulip Era' of garden parties and the first Ottoman printing press.", *OT,
  at='constantinople', tags='rule art')
K('Mahmud I', SULTAN, (1696, 1754), 1730, 1754,
  'Took Belgrade back from Austria in 1739 and built libraries and fountains across Constantinople.', *OT, at='constantinople')
K('Osman III', SULTAN, (1699, 1757), 1754, 1757,
  'Hated music and women so much that he wore iron-nailed shoes so the palace women could hear him coming.', *OT,
  at='constantinople')
K('Mustafa III', SULTAN, (1717, 1774), 1757, 1774,
  'Started a war with Catherine the Great in 1768 and saw his fleet burned at Chesma.', *OT, at='constantinople')
K('Abdul Hamid I', SULTAN, (1725, 1789), 1774, 1789,
  'Lost the Crimea to Russia after the treaty of Küçük Kaynarca.', *OT, at='constantinople')
K('Abdulmejid I', SULTAN, (1823, 1861), 1839, 1861,
  'Began the Tanzimat reforms that made all his subjects equal before the law, and fought beside Britain and France in the Crimean War.',
  *OT, at='constantinople', tags='rule reform')
P('Abdulaziz', SULTAN, (1830, 1876), 3, 'rule',
  'First sultan to tour western Europe, who built ironclads with borrowed money until the empire went bankrupt; deposed in 1876.',
  R(1861, 1866, SULTAN, *OT, at='constantinople'),
  G(1867, 1867, 'Tour of Europe', ('constantinople', 1867.47), ('paris', 1867.49), ('london', 1867.53), ('vienna', 1867.57),
    ('constantinople', 1867.6)),
  R(1868, 1876, SULTAN, *OT, at='constantinople'))
K('Mehmed V', SULTAN, (1844, 1918), 1909, 1918,
  'Figurehead sultan under the Young Turks, who proclaimed a holy war on the Allies in 1914.', *OT, at='constantinople')
P('Enver Pasha', 'Minister of War of the Ottoman Empire', (1881, 1922), 3, 'war rule',
  'Young Turk who led the empire into the First World War, lost an army in the snows of Sarikamish, and died fighting the Red Army in Central Asia.',
  R(1913, 1913, 'Young Turk leader', *OT, at='constantinople'),
  G(1914, 1915, 'Sarikamish', ('constantinople', 1914.0), ('constantinople', 1914.85), ((41.27, 39.9, 1914.93)), ((42.59, 40.33, 1914.99)),
    ('constantinople', 1915.2)),
  R(1916, 1918, 'Minister of War', *OT, at='constantinople'),
  G(1919, 1922, 'Flight and death in Central Asia', ('berlin', 1919.0), ('moscow', 1920.6), ((49.87, 40.41, 1920.7)), ('moscow', 1921.0),
    ('bukhara', 1921.85), ((69.68, 38.32, 1922.59))))
P('Talaat Pasha', 'Grand vizier of the Ottoman Empire', (1874, 1921), 3, 'rule',
  'Interior minister who organised the Armenian genocide of 1915, grand vizier until the defeat of 1918, shot in Berlin by a survivor.',
  R(1913, 1918, 'Interior minister, then grand vizier', *OT, at='constantinople'), G(1919, 1921, 'In hiding in Berlin', 'berlin'))
P('Mehmed VI', SULTAN, (1861, 1926), 3, 'rule',
  'Last Ottoman sultan, who fled Constantinople on a British warship when the sultanate was abolished in 1922.',
  R(1918, 1922, SULTAN, *OT, at='constantinople'),
  G(1923, 1926, 'In exile', ((14.51, 35.9, 1923.0)), ((7.78, 43.82, 1923.5)), ((7.78, 43.82, 1926.4))))
P('İsmet İnönü', 'President of Turkey', (1884, 1973), 3, 'rule war',
  "Atatürk's right-hand general, who signed the peace of Lausanne, kept Turkey out of the Second World War and allowed free elections.",
  R(1938, 1950, 'President of Turkey', *TR, at='ankara'), R(1961, 1965, 'Prime minister of Turkey', *TR, at='ankara'))
K('Adnan Menderes', 'Prime minister of Turkey', (1899, 1961), 1950, 1960,
  'First freely elected prime minister of Turkey, overthrown by the army in 1960 and hanged.', *TR, at='ankara')
P('Süleyman Demirel', 'Prime minister and president of Turkey', (1924, 2015), 3, 'rule',
  'Seven times prime minister, twice overthrown by the army, and finally president of Turkey.',
  R(1965, 1971, 'Prime minister of Turkey', *TR, at='ankara'), R(1975, 1977, 'Prime minister of Turkey', *TR, at='ankara'),
  R(1979, 1980, 'Prime minister of Turkey', *TR, at='ankara'), R(1991, 2000, 'Prime minister, then president', *TR, at='ankara'))
P('Bülent Ecevit', 'Prime minister of Turkey', (1925, 2006), 3, 'rule',
  'Poet and translator who as prime minister sent the army into Cyprus in 1974.',
  R(1974, 1974, 'Prime minister of Turkey', *TR, at='ankara'), R(1978, 1979, 'Prime minister of Turkey', *TR, at='ankara'),
  R(1999, 2002, 'Prime minister of Turkey', *TR, at='ankara'))
K('Kenan Evren', 'President of Turkey', (1917, 2015), 1980, 1989,
  'General who led the military coup of 1980 and became president.', *TR, at='ankara')
K('Turgut Özal', 'Prime minister and president of Turkey', (1927, 1993), 1983, 1993,
  "Opened Turkey's economy to the world as prime minister and then president.", *TR, at='ankara')

# ---------- Persia and Iran ----------
K('Abaqa Khan', 'Ilkhan of Persia', (1234, 1282), 1265, 1282,
  "Hulagu's son, who wrote to the pope proposing an alliance against the Mamluks.", *ILK, at='tabriz')
K('Arghun', 'Ilkhan of Persia', (1258, 1291), 1284, 1291,
  'Buddhist khan who sent the monk Rabban Bar Sauma to the kings of Europe to plan a joint crusade.', *ILK, at='tabriz')
K('Ghazan', 'Ilkhan of Persia', (1271, 1304), 1295, 1304,
  'Became a Muslim, made Islam the faith of Mongol Persia and had Rashid al-Din write a history of the world.', *ILK, at='tabriz',
  tags='rule faith')
K('Öljaitü', 'Ilkhan of Persia', (1280, 1316), 1304, 1316,
  'Built a new capital at Soltaniyeh, whose great domed tomb still stands.', *ILK, at=(48.8, 36.43))
K("Abu Sa'id Bahadur Khan", 'Ilkhan of Persia', (1305, 1335), 1316, 1335,
  'Last of the Ilkhans; when he died without an heir, Mongol Persia broke apart.', *ILK, at=(48.8, 36.43))
P('Rashid al-Din Hamadani', 'Vizier and historian of the Ilkhans', (1247, 1318), 3, 'mind rule',
  'Jewish-born doctor who became vizier of Mongol Persia and wrote the first history of the whole known world.',
  G(1298, 1318, 'Vizier at Tabriz', 'tabriz'))
K('Shah Rukh', 'Timurid ruler', (1377, 1447), 1405, 1447,
  "Timur's son, who ruled from Herat with his wife Gawhar Shad and made it a centre of Persian art.", *TIM, at='herat', tags='rule art')
P('Ulugh Beg', 'Timurid ruler and astronomer', (1394, 1449), 3, 'mind rule',
  "Timur's grandson, who built a great observatory at Samarkand and charted a thousand stars, and was killed on his own son's orders.",
  G(1409, 1446, 'Governor of Samarkand', 'samarkand'), R(1447, 1449, 'Timurid ruler', *TIM, at='samarkand'))
K("Abu Sa'id Mirza", 'Timurid ruler', (1424, 1469), 1451, 1469,
  "Babur's grandfather, who held the Timurid lands together until he was killed fighting the Turkmen.", *TIM, at='herat')
K('Husayn Bayqara', 'Timurid sultan of Herat', (1438, 1506), 1469, 1506,
  'Last great Timurid, whose court at Herat was home to the poet Navoi and the painter Bihzad.', *TIM, at='herat', tags='rule art')
P('Uzun Hasan', 'Ruler of the White Sheep Turkmen', (1423, 1478), 3, 'rule war',
  'Turkmen ruler of western Persia who allied with Venice against the Ottomans and lost to Mehmed II at Otlukbeli in 1473.',
  G(1453, 1478, 'Ruler of the White Sheep Turkmen', 'tabriz'))
P('Muhammad Shaybani', 'Khan of the Uzbeks', (1451, 1510), 3, 'war rule',
  'Uzbek khan who drove Babur out of Samarkand and took Herat, then was killed by Shah Ismail, who made a drinking cup of his skull.',
  G(1500, 1510, 'The Uzbek conquest', ((64.42, 39.77, 1500.0)), ('samarkand', 1500.5), ('samarkand', 1506.9), ('herat', 1507.4), ('herat', 1510.5),
    ((61.83, 37.66, 1510.92))))
K('Tahmasp I', SHAH, (1514, 1576), 1524, 1576,
  'Reigned 52 years, held off the Ottomans and sheltered the exiled Mughal emperor Humayun.', *SAF, at=QAZVIN)
K('Safi of Persia', SHAH, (1611, 1642), 1629, 1642,
  'Cruel grandson of Abbas the Great, who lost Baghdad to the Ottomans for good in 1638.', *SAF, at='isfahan')
K('Abbas II of Persia', SHAH, (1632, 1666), 1642, 1666,
  'Took Kandahar back from the Mughals and was known both for his tolerance and for his drinking.', *SAF, at='isfahan')
K('Suleiman I of Persia', SHAH, (1647, 1694), 1666, 1694,
  'Spent his reign in the harem while the Safavid state slowly decayed.', *SAF, at='isfahan')
K('Sultan Husayn', SHAH, (1668, 1726), 1694, 1722,
  'Pious, weak shah who surrendered Isfahan to Afghan rebels after a terrible siege in 1722.', *SAF, at='isfahan')
K('Mahmud Hotak', 'Shah of Persia', (1697, 1725), 1722, 1725,
  'Afghan chief who marched from Kandahar, took Isfahan and made himself shah, then went mad.', *SAF, at='isfahan', tags='rule war')
K('Tahmasp II', SHAH, (1704, 1740), 1729, 1732,
  'Safavid prince put back on the throne by his general Nader, who then deposed him.', *SAF, at='isfahan')
K('Karim Khan Zand', 'Ruler of Persia', (1705, 1779), 1751, 1779,
  'Kindly ruler who would not call himself shah, only regent of the people, and beautified his capital Shiraz.', 'Persia', *SAF,
  at='shiraz')
K('Fath-Ali Shah Qajar', SHAH, (1772, 1834), 1797, 1834,
  'Famous for his long beard, wasp waist and many wives; he lost the Caucasus to Russia.', *QAJ, at='tehran')
K('Mohammad Shah Qajar', SHAH, (1808, 1848), 1834, 1848,
  'Besieged Herat in vain and left the ruling to his Sufi minister.', *QAJ, at='tehran')
P('Naser al-Din Shah Qajar', SHAH, (1831, 1896), 3, 'rule',
  'Reigned almost fifty years, the first shah to visit Europe and an early photographer; shot at a shrine in 1896.',
  R(1848, 1872, SHAH, *QAJ, at='tehran'),
  G(1873, 1873, 'Tour of Europe', ('tehran', 1873.3), ('st_petersburg', 1873.4), ('berlin', 1873.44), ('london', 1873.47), ('paris', 1873.53),
    ('vienna', 1873.6), ('constantinople', 1873.68), ('tehran', 1873.8)),
  R(1874, 1896, SHAH, *QAJ, at='tehran'))
K('Amir Kabir', 'Chief minister of Persia', (1807, 1852), 1848, 1851,
  "Reforming chief minister who founded Persia's first modern college, then was murdered on the shah's orders.", *QAJ, at='tehran',
  tags='rule reform')
K('Mozaffar ad-Din Shah Qajar', SHAH, (1853, 1907), 1896, 1907,
  'Signed the constitution of 1906 that gave Persia its first parliament, days before he died.', *QAJ, at='tehran')
K('Mohammad Ali Shah Qajar', SHAH, (1872, 1925), 1907, 1909,
  'Shelled the new parliament in 1908 and was deposed by the constitutionalists.', *QAJ, at='tehran')
K('Ahmad Shah Qajar', SHAH, (1898, 1930), 1909, 1925,
  'Last Qajar shah, crowned at eleven, who lost his throne to Reza Khan while touring Europe.', *QAJ, at='tehran')
K('Mojtaba Khamenei', 'Supreme Leader of Iran', (1969, None), 2026, 2026,
  'Son of Ali Khamenei, named Supreme Leader of Iran in March 2026 after his father was killed.', 'Iran', at='tehran',
  tags='rule faith')

# ---------- India and its neighbours ----------
K('Iltutmish', 'Sultan of Delhi', (1180, 1236), 1211, 1236,
  'Slave who rose to be sultan of Delhi, kept Genghis Khan out of India by turning away a fleeing prince, and finished the Qutb Minar.',
  *DS, at='delhi')
K('Ghiyas ud din Balban', 'Sultan of Delhi', (1216, 1287), 1266, 1287,
  'Stern sultan who held off the Mongols and taught that a king is the shadow of God on earth.', *DS, at='delhi')
K('Alauddin Khalji', 'Sultan of Delhi', (1266, 1316), 1296, 1316,
  'Murdered his uncle to take the throne, beat back the Mongols again and again, and sent his armies deep into southern India.', *DS,
  at='delhi', rank=2, tags='rule war')
K('Muhammad bin Tughluq', 'Sultan of Delhi', (1290, 1351), 1325, 1351,
  'Brilliant, erratic sultan who moved his whole capital south to Daulatabad and back, and issued copper coins as if they were silver.',
  *DS, at='delhi')
K('Firuz Shah Tughluq', 'Sultan of Delhi', (1309, 1388), 1351, 1388,
  "Built canals, towns and hospitals, and had two of Ashoka's ancient pillars moved to Delhi.", *DS, at='delhi')
K('Bahlul Lodi', 'Sultan of Delhi', (1420, 1489), 1451, 1489,
  'Afghan chief who founded the Lodi dynasty and won back the lands around Delhi.', *DS, at='delhi')
K('Sikandar Lodi', 'Sultan of Delhi', (1458, 1517), 1489, 1517,
  'Founded the city of Agra and wrote Persian poetry.', *DS, at='agra')
K('Ibrahim Lodi', 'Sultan of Delhi', (1480, 1526), 1517, 1526,
  'Last sultan of Delhi, killed by Babur at the first battle of Panipat in 1526.', *DS, at='agra')
P('Humayun', 'Mughal emperor', (1508, 1556), 2, 'rule',
  "Babur's son, who lost his empire to Sher Shah, spent fifteen years in exile, won it back, and died falling down his library stairs.",
  R(1530, 1539, 'Mughal emperor', *MUG, at='agra'),
  G(1540, 1554, 'Exile', ('agra', 1540.4), ('lahore', 1540.6), ((68.37, 25.4, 1541.5)), ((69.73, 25.36, 1542.8)), ('kandahar', 1543.8),
    ('herat', 1544.2), ('isfahan', 1544.5), ((49.99, 36.27, 1544.7)), ('kandahar', 1545.6), ('kabul', 1545.9), ('kabul', 1554.8)),
  R(1555, 1556, 'Mughal emperor', *MUG, at='delhi'))
K('Bahadur Shah I', 'Mughal emperor', (1643, 1712), 1707, 1712,
  "Aurangzeb's son, who won the war for the throne at sixty-three.", *MUG, at='delhi')
K('Muhammad Shah', 'Mughal emperor', (1702, 1748), 1719, 1748,
  "'The Merry', a patron of music who watched Nader Shah sack Delhi in 1739 and carry off the Peacock Throne.", *MUG, at='delhi')
K('Shah Alam II', 'Mughal emperor', (1728, 1806), 1760, 1806,
  "Gave the British the right to tax Bengal in 1765; blinded by a rebel in 1788, he ended under British 'protection'.", *MUG, at='delhi')
P('Bahadur Shah Zafar', 'Last Mughal emperor', (1775, 1862), 3, 'rule art',
  'Poet and last Mughal emperor, made the figurehead of the rising of 1857 and exiled by the British to Rangoon.',
  R(1837, 1857, 'Mughal emperor', *MUG, at='delhi'),
  G(1858, 1862, 'Exile in Rangoon', ('delhi', 1858.8), ('rangoon', 1858.95), ('rangoon', 1862.85)))
K('Shahu I', 'Chhatrapati of the Marathas', (1682, 1749), 1707, 1749,
  "Shivaji's grandson, raised as a Mughal prisoner, under whom Maratha power spread across India.", *MAR, at=SATARA)
K('Madhavrao I', 'Peshwa of the Marathas', (1745, 1772), 1761, 1772,
  'Rebuilt Maratha power after the disaster of Panipat in 1761 and died of tuberculosis at 27.', *MAR, at='pune')
K('Nana Fadnavis', 'Chief minister of the Marathas', (1742, 1800), 1773, 1800,
  "'The Maratha Machiavelli', who held the Maratha confederacy together against the British.", *MAR, at='pune')
K('Baji Rao II', 'Peshwa of the Marathas', (1775, 1851), 1795, 1818,
  'Last peshwa, who signed his power over to the British in 1802 and lost the rest in 1818.', *MAR, at='pune')
P('Siraj ud-Daulah', 'Nawab of Bengal', (1733, 1757), 3, 'rule war',
  'Last independent nawab of Bengal, who took Calcutta from the British in 1756 and lost Bengal to Robert Clive at Plassey.',
  R(1756, 1756, 'Nawab of Bengal', 'Bengal', at=(88.27, 24.18)),
  G(1757, 1757, 'Plassey', ((88.27, 24.18, 1757.4)), ((88.25, 23.8, 1757.48)), ((88.27, 24.18, 1757.5))))
K('Warren Hastings', 'Governor-General of India', (1732, 1818), 1773, 1785,
  'First governor-general of British India, later impeached in London in a trial that dragged on for seven years.', *BI, at='calcutta')
P('Charles Cornwallis, 1st Marquess Cornwallis', 'General and governor-general of India', (1738, 1805), 3, 'war rule',
  'British general who surrendered to Washington at Yorktown in 1781, then governed India and Ireland.',
  G(1780, 1781, 'The southern campaign', ((-79.93, 32.78, 1780.4)), ((-80.6, 34.25, 1780.62)), ((-80.84, 35.23, 1780.75)),
    ((-79.84, 36.13, 1781.2)), ((-77.93, 34.23, 1781.3)), ((-77.4, 37.23, 1781.4)), ('yorktown', 1781.6), ('yorktown', 1781.8)),
  R(1786, 1793, 'Governor-General of India', *BI, at='calcutta'),
  G(1798, 1801, 'Lord Lieutenant of Ireland', 'dublin'),
  G(1805, 1805, 'Back to India', ('calcutta', 1805.6), ((83.57, 25.58, 1805.76))))
K('Lord Wellesley', 'Governor-General of India', (1760, 1842), 1798, 1805,
  'Brother of the Duke of Wellington, who crushed Tipu Sultan and made Britain master of most of India.', *BI, at='calcutta',
  wiki='Richard Wellesley, 1st Marquess Wellesley')
K('Lord Dalhousie', 'Governor-General of India', (1812, 1860), 1848, 1856,
  'Built railways and telegraphs and took over Indian states whose rulers died without an heir, feeding the anger behind the rising of 1857.',
  *BI, at='calcutta', wiki='James Broun-Ramsay, 1st Marquess of Dalhousie')
K('Lord Canning', 'Viceroy of India', (1812, 1862), 1856, 1862,
  "Governor-general through the rising of 1857, mocked as 'Clemency Canning' for refusing mass revenge; the first viceroy.", *BI,
  at='calcutta', wiki='Charles Canning, 1st Earl Canning')
K('Lord Curzon', 'Viceroy of India', (1859, 1925), 1899, 1905,
  'Grand viceroy who held the Delhi durbar of 1903 and split Bengal in two, setting off a storm of protest.', *BI, at='calcutta',
  wiki='George Curzon, 1st Marquess Curzon of Kedleston')
P('Lord Mountbatten', 'Last Viceroy of India', (1900, 1979), 3, 'war rule',
  'Commanded the Allies in Southeast Asia, then as the last viceroy rushed through the partition of India in 1947; killed by the IRA.',
  G(1943, 1946, 'Supreme Allied Commander, Southeast Asia', (80.64, 7.29)),
  R(1947, 1948, 'Viceroy, then governor-general of India', 'India', at='delhi'), wiki='Louis Mountbatten, 1st Earl Mountbatten of Burma')
K('Lal Bahadur Shastri', 'Prime minister of India', (1904, 1966), 1964, 1966,
  "Led India through the war of 1965 with Pakistan under the slogan 'Hail the soldier, hail the farmer', and died at the peace talks.",
  'India', at='delhi')
K('Morarji Desai', 'Prime minister of India', (1896, 1995), 1977, 1979,
  'First prime minister of India from outside the Congress party, elected after Indira Gandhi\'s emergency rule.', 'India', at='delhi')
K('Rajiv Gandhi', 'Prime minister of India', (1944, 1991), 1984, 1989,
  "Indira Gandhi's son, prime minister at forty after her murder, killed by a suicide bomber in 1991.", 'India', at='delhi')
K('P. V. Narasimha Rao', 'Prime minister of India', (1921, 2004), 1991, 1996,
  "Opened India's economy to the world with his finance minister Manmohan Singh.", 'India', at='delhi', tags='rule reform')
P('Atal Bihari Vajpayee', 'Prime minister of India', (1924, 2018), 3, 'rule',
  'Poet and Hindu nationalist prime minister who ordered the nuclear tests of 1998 and then rode a bus to Pakistan to make peace.',
  R(1996, 1996, 'Prime minister of India', 'India', at='delhi'), R(1998, 2004, 'Prime minister of India', 'India', at='delhi'))
K('Manmohan Singh', 'Prime minister of India', (1932, 2024), 2004, 2014,
  'Economist who freed the Indian economy as finance minister in 1991 and led India for ten years of fast growth.', 'India', at='delhi')
K('Liaquat Ali Khan', 'Prime minister of Pakistan', (1895, 1951), 1947, 1951,
  "Pakistan's first prime minister, shot dead at a rally in 1951.", 'Pakistan', at='karachi')
K('Ayub Khan', 'President of Pakistan', (1907, 1974), 1958, 1969,
  "Pakistan's first military ruler, who built a new capital at Islamabad.", 'Pakistan', at='karachi', wiki='Ayub Khan (general)')
K('Zulfikar Ali Bhutto', 'Prime minister of Pakistan', (1928, 1979), 1971, 1977,
  'Led Pakistan after it lost Bangladesh, began its nuclear programme, and was overthrown and hanged by General Zia.', 'Pakistan',
  at='islamabad')
K('Muhammad Zia-ul-Haq', 'President of Pakistan', (1924, 1988), 1977, 1988,
  'General who ruled Pakistan for eleven years, imposed strict Islamic law and backed the Afghan fighters against the Soviets.',
  'Pakistan', at='islamabad')
P('Nawaz Sharif', 'Prime minister of Pakistan', (1949, None), 3, 'rule',
  'Three times prime minister of Pakistan, overthrown by the army in 1999 and later removed by the courts.',
  R(1990, 1993, 'Prime minister of Pakistan', 'Pakistan', at='islamabad'), R(1997, 1999, 'Prime minister of Pakistan', 'Pakistan', at='islamabad'),
  R(2013, 2017, 'Prime minister of Pakistan', 'Pakistan', at='islamabad'))
K('Pervez Musharraf', 'President of Pakistan', (1943, 2023), 1999, 2008,
  'General who seized power in 1999 and became an American ally after the attacks of 11 September 2001.', 'Pakistan', at='islamabad')
K('Asif Ali Zardari', 'President of Pakistan', (1955, None), 2008, 2013,
  'Widower of Benazir Bhutto, elected president after her assassination.', 'Pakistan', at='islamabad')
K('Imran Khan', 'Prime minister of Pakistan', (1952, None), 2018, 2022,
  "Captain of Pakistan's 1992 cricket World Cup winners who became prime minister, then was ousted and jailed.", 'Pakistan',
  at='islamabad')
K('Shehbaz Sharif', 'Prime minister of Pakistan', (1951, None), 2024, 2026,
  'Younger brother of Nawaz Sharif, prime minister of Pakistan.', 'Pakistan', at='islamabad')
K('Ziaur Rahman', 'President of Bangladesh', (1936, 1981), 1977, 1981,
  'Army officer who read out the declaration of independence in 1971, later president, killed in a coup.', 'Bangladesh', at='dhaka')
P('Sheikh Hasina', 'Prime minister of Bangladesh', (1947, None), 3, 'rule',
  'Daughter of the founder of Bangladesh, who ruled for twenty years until a student uprising drove her to India in 2024.',
  R(1996, 2001, 'Prime minister of Bangladesh', 'Bangladesh', at='dhaka'), R(2009, 2023, 'Prime minister of Bangladesh', 'Bangladesh', at='dhaka'),
  G(2024, 2026, 'Fled to India', ('dhaka', 2024.59), ('delhi', 2024.6), ('delhi', 2026.9)))
K('Muhammad Yunus', 'Chief adviser of Bangladesh', (1940, None), 2024, 2025,
  'Banker to the poor and Nobel Peace Prize winner, who led Bangladesh after the fall of Sheikh Hasina.', 'Bangladesh', at='dhaka')
K('Tarique Rahman', 'Prime minister of Bangladesh', (1965, None), 2026, 2026,
  'Son of Ziaur Rahman and Khaleda Zia, who returned from exile and won the election of February 2026.', 'Bangladesh', at='dhaka')
P('Sirimavo Bandaranaike', 'Prime minister of Sri Lanka', (1916, 2000), 3, 'rule',
  "The world's first woman prime minister, elected in Ceylon in 1960 after her husband was assassinated.",
  R(1960, 1965, 'Prime minister of Ceylon', 'Ceylon', 'Sri Lanka', at='colombo'), R(1970, 1977, 'Prime minister of Sri Lanka', 'Ceylon',
    'Sri Lanka', at='colombo'), R(1994, 2000, 'Prime minister of Sri Lanka', 'Sri Lanka', at='colombo'))
K('Mahinda Rajapaksa', 'President of Sri Lanka', (1945, None), 2005, 2015,
  'President who ended the long civil war with the Tamil Tigers in 2009.', 'Sri Lanka', at='colombo')

# ---------- Afghanistan ----------
AF = ('Afghanistan',)
K('Timur Shah Durrani', 'King of Afghanistan', (1748, 1793), 1772, 1793,
  'Son of Ahmad Shah Durrani, who moved the capital to Kabul.', *AF, at='kabul')
P('Dost Mohammad Khan', 'Emir of Afghanistan', (1793, 1863), 3, 'rule war',
  'Emir driven out by the British invasion of 1839, who came back after their army was destroyed on the retreat from Kabul.',
  R(1826, 1839, 'Emir of Afghanistan', *AF, at='kabul'), G(1840, 1842, 'A prisoner of the British', ((75.86, 30.9))),
  R(1843, 1863, 'Emir of Afghanistan', *AF, at='kabul'))
K('Shah Shuja Durrani', 'King of Afghanistan', (1785, 1842), 1839, 1842,
  'Put back on the throne by a British army in 1839 and murdered when it was destroyed.', *AF, at='kabul')
K('Sher Ali Khan', 'Emir of Afghanistan', (1825, 1879), 1868, 1878,
  'Turned away a British mission in 1878 and fled when the British invaded again.', *AF, at='kabul')
K('Abdur Rahman Khan', 'Emir of Afghanistan', (1840, 1901), 1880, 1901,
  "'The Iron Emir', who forged a single Afghan state by force and agreed its border with British India.", *AF, at='kabul')
K('Habibullah Khan', 'Emir of Afghanistan', (1872, 1919), 1901, 1919,
  'Kept Afghanistan neutral in the First World War and was shot dead on a hunting trip.', *AF, at='kabul')
P('Amanullah Khan', 'King of Afghanistan', (1892, 1960), 3, 'rule reform',
  "Won Afghanistan's full independence from Britain in 1919, tried to modernise it at speed, and was driven out by a revolt.",
  R(1919, 1929, 'King of Afghanistan', *AF, at='kabul'), G(1929, 1960, 'Exile in Italy', ('kabul', 1929.05), ('rome', 1929.5), ('rome', 1960.3)))
P('Mohammed Zahir Shah', 'King of Afghanistan', (1914, 2007), 3, 'rule',
  'Last king of Afghanistan, who gave it forty years of peace and was overthrown by his cousin while abroad in 1973.',
  R(1933, 1973, 'King of Afghanistan', *AF, at='kabul'), G(1973, 2002, 'Exile in Rome', 'rome'))
K('Mohammed Daoud Khan', 'President of Afghanistan', (1909, 1978), 1973, 1978,
  'Overthrew his cousin the king and was killed in the communist coup of 1978.', *AF, at='kabul')
K('Mohammad Najibullah', 'President of Afghanistan', (1947, 1996), 1986, 1992,
  'Communist president who outlasted the Soviet withdrawal by three years and was hanged by the Taliban in 1996.', *AF, at='kabul')
K('Mullah Omar', 'Leader of the Taliban', (1960, 2013), 1996, 2001,
  'One-eyed cleric who founded the Taliban, ruled Afghanistan from Kandahar and sheltered Osama bin Laden.', *AF, at='kandahar',
  tags='rule faith')
K('Ashraf Ghani', 'President of Afghanistan', (1949, None), 2014, 2021,
  'Former World Bank economist who fled Kabul as the Taliban took it in August 2021.', *AF, at='kabul')
K('Hibatullah Akhundzada', 'Leader of the Taliban', (1961, None), 2021, 2026,
  'Reclusive cleric who rules Afghanistan from Kandahar and has banned girls from school beyond the age of twelve.', *AF,
  at='kandahar', tags='rule faith')

# ---------- the modern Middle East ----------
P('Hussein bin Ali, Sharif of Mecca', 'King of the Hejaz', (1854, 1931), 3, 'rule',
  'Guardian of Mecca who launched the Arab Revolt against the Ottomans in 1916, then lost his kingdom to Ibn Saud.',
  R(1916, 1924, 'King of the Hejaz', 'Hejaz', at='mecca'), G(1925, 1931, 'Exile on Cyprus', (33.36, 35.17)))
P('Faisal I of Iraq', 'King of Iraq', (1885, 1933), 3, 'war rule',
  "Led the Arab Revolt beside Lawrence of Arabia from Arabia to Damascus, was crowned king of Syria, thrown out by the French, and made king of Iraq.",
  G(1916, 1918, 'The Arab Revolt', ('mecca', 1916.43), ((39.6, 24.47, 1916.5)), ((38.06, 24.09, 1916.9)), ((36.45, 26.23, 1917.07)),
    ((35.0, 29.53, 1917.6)), ((35.0, 29.53, 1918.4)), ('damascus', 1918.75)),
  R(1920, 1920, 'King of Syria', 'Syria (France)', at='damascus'),
  R(1921, 1933, 'King of Iraq', 'Mesopotamia (GB)', 'Iraq', at='baghdad'))
K('Faisal II of Iraq', 'King of Iraq', (1935, 1958), 1939, 1958,
  'Boy king of Iraq, killed with his family in the revolution of 1958.', 'Mesopotamia (GB)', 'Iraq', at='baghdad')
K('Abd al-Karim Qasim', 'Prime minister of Iraq', (1914, 1963), 1958, 1963,
  'Officer who overthrew the monarchy in 1958 and was shot in a coup by the Baath party.', 'Iraq', at='baghdad')
K('Nouri al-Maliki', 'Prime minister of Iraq', (1950, None), 2006, 2014,
  'Shia prime minister of Iraq through the civil war and the American withdrawal, until the rise of the Islamic State.', 'Iraq',
  at='baghdad')
K('Abdullah I of Jordan', 'King of Jordan', (1882, 1951), 1921, 1951,
  'Son of the Sharif of Mecca, who founded Transjordan, took the West Bank in 1948 and was shot at the Al-Aqsa Mosque.', 'Jordan',
  at='amman')
K('Hussein of Jordan', 'King of Jordan', (1935, 1999), 1952, 1999,
  'Survived dozens of plots to rule Jordan for 46 years, lost the West Bank in 1967 and made peace with Israel in 1994.', 'Jordan',
  at='amman')
K('Abdullah II of Jordan', 'King of Jordan', (1962, None), 1999, 2026,
  'King of Jordan since 1999.', 'Jordan', at='amman')
K('Faisal of Saudi Arabia', 'King of Saudi Arabia', (1906, 1975), 1964, 1975,
  'Modernising king who led the Arab oil embargo of 1973 and was shot by his nephew.', 'Saudi Arabia', at='riyadh')
K('Fahd of Saudi Arabia', 'King of Saudi Arabia', (1921, 2005), 1982, 2005,
  'King who invited American troops in after Iraq invaded Kuwait in 1990.', 'Saudi Arabia', at='riyadh')
K('Abdullah of Saudi Arabia', 'King of Saudi Arabia', (1924, 2015), 2005, 2015,
  'Cautious reformer who let women vote in local elections.', 'Saudi Arabia', at='riyadh')
K('Salman of Saudi Arabia', 'King of Saudi Arabia', (1935, None), 2015, 2026,
  'King of Saudi Arabia, who handed the running of the country to his son Mohammed.', 'Saudi Arabia', at='riyadh')
K('Levi Eshkol', 'Prime minister of Israel', (1895, 1969), 1963, 1969,
  'Prime minister during the Six-Day War of 1967.', 'Israel', at='jerusalem')
K('Menachem Begin', 'Prime minister of Israel', (1913, 1992), 1977, 1983,
  'Former underground fighter who made peace with Egypt at Camp David and shared the Nobel Peace Prize with Sadat.', 'Israel',
  at='jerusalem')
P('Shimon Peres', 'Prime minister and president of Israel', (1923, 2016), 3, 'rule',
  'Founding father of Israel who shared the Nobel Peace Prize for the Oslo accords and was president in his eighties.',
  R(1984, 1986, 'Prime minister of Israel', 'Israel', at='jerusalem'), R(1995, 1996, 'Prime minister of Israel', 'Israel', at='jerusalem'),
  R(2007, 2014, 'President of Israel', 'Israel', at='jerusalem'))
K('Ehud Olmert', 'Prime minister of Israel', (1945, None), 2006, 2009,
  'Prime minister during the 2006 war in Lebanon, later jailed for corruption.', 'Israel', at='jerusalem')

# ---------- China ----------
SONG, YUAN = ('Song Empire',), ('Great Khanate',)
MING = ('Ming Empire', 'Ming Chinese Empire')
QING = ('Manchu Empire', 'Qing Empire')
TW = ('Taiwan',)
SE, YE, ME, QE = 'Emperor of Song China', 'Emperor of Yuan China', 'Emperor of Ming China', 'Emperor of Qing China'
K('Emperor Zhenzong of Song', SE, (968, 1022), 997, 1022,
  'Bought peace from the Khitan Liao with a yearly gift of silver and silk in the treaty of Chanyuan of 1005.', *SONG, at='kaifeng')
K('Emperor Renzong of Song', SE, (1010, 1063), 1022, 1063,
  'Reigned 41 years, the longest of any Song emperor, while Song art and learning flowered and Bi Sheng invented movable type.', *SONG,
  at='kaifeng')
K('Emperor Yingzong of Song', SE, (1032, 1067), 1063, 1067,
  "Renzong's adopted heir, whose short reign was taken up by a quarrel over how to honour his real father.", *SONG, at='kaifeng')
K('Emperor Shenzong of Song', SE, (1048, 1085), 1067, 1085,
  "Backed Wang Anshi's sweeping New Policies to make the Song state rich and strong.", *SONG, at='kaifeng', tags='rule reform')
K('Emperor Zhezong of Song', SE, (1077, 1100), 1085, 1100,
  'Came to the throne at eight; his grandmother undid the reforms, and he brought them back once he ruled himself.', *SONG, at='kaifeng')
P('Emperor Qinzong of Song', SE, (1100, 1161), 3, 'rule',
  'Emperor for barely a year before the Jurchen took Kaifeng in 1127 and carried him and his father north; he died a prisoner.',
  R(1126, 1126, SE, *SONG, at='kaifeng'),
  G(1127, 1161, 'Captive of the Jin', ('kaifeng', 1127.3), ((129.3, 45.75, 1128.5)), ((129.3, 45.75, 1161.5))))
K('Emperor Gaozong of Song', SE, (1107, 1187), 1127, 1162,
  'Escaped the fall of the north, founded the Southern Song at Hangzhou, and had the general Yue Fei put to death to make peace with the Jin.',
  *SONG, at='hangzhou')
K('Emperor Xiaozong of Song', SE, (1127, 1194), 1162, 1189,
  'Ablest of the Southern Song emperors, who cleared the name of Yue Fei and tried to win back the north.', *SONG, at='hangzhou')
K('Emperor Guangzong of Song', SE, (1147, 1200), 1189, 1194,
  'Mentally ill emperor, pushed off the throne by his own court in 1194.', *SONG, at='hangzhou')
K('Emperor Ningzong of Song', SE, (1168, 1224), 1194, 1224,
  'Weak emperor whose minister Han Tuozhou started a failed war against the Jin in 1206.', *SONG, at='hangzhou')
K('Emperor Lizong of Song', SE, (1205, 1264), 1224, 1264,
  "Joined the Mongols to destroy the Jin in 1234, then spent thirty years fighting the Mongols; he made Zhu Xi's teachings the state creed.",
  *SONG, at='hangzhou')
K('Jia Sidao', 'Chancellor of Song China', (1213, 1275), 1264, 1275,
  'Cricket-loving chancellor who ran the Song state in its last years while the Mongols besieged Xiangyang, and was murdered after losing his army.',
  *SONG, at='hangzhou')
P('Wen Tianxiang', 'Song loyalist', (1236, 1283), 3, 'war',
  'Scholar-general who fought on for the Song after Hangzhou fell and chose death rather than serve Kublai Khan; Chinese children still learn his poems.',
  G(1276, 1278, 'Fights on for the Song', ('hangzhou', 1276.1), ((119.3, 26.08, 1276.6)), ((115.35, 22.97, 1278.95))),
  G(1279, 1283, 'Prisoner in Dadu', 'dadu'))
K('Temür Khan', YE, (1265, 1307), 1294, 1307,
  "Kublai's grandson, who called off a third invasion of Japan and made peace with Vietnam.", *YUAN, at='dadu')
K('Külüg Khan', YE, (1281, 1311), 1307, 1311,
  'Soldier emperor who spent so freely that he flooded the empire with new paper money.', *YUAN, at='dadu')
K('Ayurbarwada', YE, (1285, 1320), 1311, 1320,
  'Confucian-schooled emperor who brought back the civil service examinations in 1315.', *YUAN, at='dadu',
  wiki='Ayurbarwada Buyantu Khan')
K('Gegeen Khan', YE, (1302, 1323), 1320, 1323,
  'Reforming young emperor murdered by his own officials in 1323.', *YUAN, at='dadu')
K('Yesün Temür', YE, (1293, 1328), 1323, 1328,
  'Put on the throne by the plotters who killed Gegeen Khan, and then had them executed.', *YUAN, at='dadu',
  wiki='Yesün Temür (Yuan dynasty)')
K('Tugh Temür', YE, (1304, 1332), 1328, 1332,
  'Won a civil war for the throne in 1328 and founded an academy of the arts and Confucian learning.', *YUAN, at='dadu',
  wiki='Jayaatu Khan Tugh Temür')
P('Toghon Temür', 'Last Yuan emperor of China', (1320, 1370), 3, 'rule',
  'Last Mongol emperor of China, who fled Dadu as the Ming army came in 1368 and died on the steppe.',
  R(1333, 1367, YE, *YUAN, at='dadu'),
  G(1368, 1370, 'Flight to the steppe', ('dadu', 1368.65), ('shangdu', 1368.75), ((116.6, 43.3, 1369.5)), ((116.6, 43.3, 1370.4))))
K('Jianwen Emperor', ME, (1377, 1402), 1398, 1402,
  "Hongwu's grandson, overthrown by his uncle, the future Yongle emperor; he vanished when his palace at Nanjing burned.", *MING,
  at='nanjing')
K('Xuande Emperor', ME, (1399, 1435), 1425, 1435,
  'Painter emperor who loved cricket fighting and sent Zheng He on the last of his great voyages.', *MING, at='beijing',
  tags='rule art')
P('Zhengtong Emperor', ME, (1427, 1464), 3, 'rule',
  'Led an army against the Mongols himself and was taken prisoner at Tumu in 1449; freed a year later, he won his throne back in a palace coup.',
  R(1435, 1448, ME, *MING, at='beijing'),
  G(1449, 1450, 'Captive of the Oirat Mongols', ('beijing', 1449.6), ((115.6, 40.4, 1449.67)), ((112.0, 41.5, 1450.0)), ('beijing', 1450.7)),
  R(1457, 1464, ME, *MING, at='beijing'), wiki='Emperor Yingzong of Ming')
K('Jingtai Emperor', ME, (1428, 1457), 1449, 1457,
  'Took the throne when his brother was captured and saved Beijing from the Mongols, then was pushed aside when his brother came back.',
  *MING, at='beijing')
K('Chenghua Emperor', ME, (1447, 1487), 1464, 1487,
  "Shy emperor devoted to Lady Wan, seventeen years his elder; the little 'chicken cups' made for him are some of the costliest porcelain on earth.",
  *MING, at='beijing')
K('Hongzhi Emperor', ME, (1470, 1505), 1487, 1505,
  'Model Confucian ruler and the only Chinese emperor known to have had just one wife.', *MING, at='beijing')
K('Zhengde Emperor', ME, (1491, 1521), 1505, 1521,
  'Pleasure-loving emperor who played at war and roamed in disguise while eunuchs ruled; the first Portuguese envoys reached China in his reign.',
  *MING, at='beijing')
K('Jiajing Emperor', ME, (1507, 1567), 1521, 1567,
  'Survived an attempt by palace women to strangle him in 1542, then shut himself away seeking Daoist elixirs of immortality.', *MING,
  at='beijing')
K('Longqing Emperor', ME, (1537, 1572), 1567, 1572,
  'Lifted the long ban on private sea trade, letting Spanish silver from the Americas flow into China.', *MING, at='beijing')
K('Wanli Emperor', ME, (1563, 1620), 1572, 1620,
  'Reigned 48 years, sent armies to save Korea from Hideyoshi, then refused to meet his ministers for decades.', *MING, at='beijing')
K('Zhang Juzheng', 'Senior Grand Secretary of Ming China', (1525, 1582), 1572, 1582,
  "Ruled in the boy Wanli emperor's name and reformed the land tax so it was paid in silver.", *MING, at='beijing', tags='rule reform')
K('Tianqi Emperor', ME, (1605, 1627), 1620, 1627,
  'Spent his days at carpentry while the eunuch Wei Zhongxian terrorised the court.', *MING, at='beijing')
P('Dorgon', 'Prince regent of the Qing', (1612, 1650), 3, 'war rule',
  'Manchu prince who led the Qing armies through the Great Wall at Shanhai Pass in 1644, took Beijing, and ruled China as regent for his nephew.',
  G(1644, 1644, 'Through the Shanhai Pass to Beijing', ('shenyang', 1644.3), ((119.75, 40.0, 1644.38)), ('beijing', 1644.45), ('beijing', 1644.95)),
  R(1645, 1650, 'Prince regent of the Qing', *QING, at='beijing'))
K('Shunzhi Emperor', QE, (1638, 1661), 1651, 1661,
  'First Qing emperor to rule from Beijing, who took power at thirteen when Dorgon died, befriended the Jesuit Adam Schall and died of smallpox.',
  *QING, at='beijing')
K('Yongzheng Emperor', QE, (1678, 1735), 1722, 1735,
  'Tireless emperor who read every report himself, set up the Grand Council and hid the name of his heir in a sealed box.', *QING,
  at='beijing')
K('Jiaqing Emperor', QE, (1760, 1820), 1796, 1820,
  "Arrested his father's corrupt favourite Heshen, perhaps the richest man in the world, and fought the White Lotus rebels.", *QING,
  at='beijing')
K('Daoguang Emperor', QE, (1782, 1850), 1820, 1850,
  'Ordered the opium trade stamped out and lost the Opium War to Britain, giving up Hong Kong in 1842.', *QING, at='beijing')
P('Xianfeng Emperor', QE, (1831, 1861), 3, 'rule',
  'Reigned through the Taiping Rebellion and fled to Chengde when British and French troops took Beijing and burned the Summer Palace in 1860.',
  R(1850, 1859, QE, *QING, at='beijing'),
  G(1860, 1861, 'Flight to Chengde', ('beijing', 1860.7), ((117.94, 40.97, 1860.75)), ((117.94, 40.97, 1861.6))))
K('Tongzhi Emperor', QE, (1856, 1875), 1861, 1874,
  "Cixi's only son, emperor at five, who died of smallpox at eighteen.", *QING, at='beijing')
K('Guangxu Emperor', QE, (1871, 1908), 1875, 1908,
  "Tried to modernise China in the Hundred Days' Reform of 1898, then was locked up by Cixi; he died of arsenic poisoning a day before her.",
  *QING, at='beijing', tags='rule reform')
P('Li Hongzhang', 'Qing statesman', (1823, 1901), 3, 'rule war',
  "China's leading statesman for thirty years, who fought the Taiping, built a modern navy, signed away Taiwan at Shimonoseki and toured the world in 1896.",
  G(1862, 1864, 'Against the Taiping', ('shanghai', 1862.3), ((120.58, 31.3, 1863.9)), ((119.95, 31.78, 1864.4))),
  G(1870, 1894, 'Viceroy of Zhili', (117.2, 39.13)),
  G(1895, 1895, 'The peace of Shimonoseki', ((117.2, 39.13, 1895.15)), ((130.94, 33.96, 1895.22)), ((130.94, 33.96, 1895.3)),
    ((117.2, 39.13, 1895.38))),
  G(1896, 1896, 'Tour of the world', ('shanghai', 1896.2), ('singapore', 1896.24), ('colombo', 1896.27), ((45.03, 12.8, 1896.31)),
    ((32.55, 29.97, 1896.34)), ((30.73, 46.48, 1896.37)), ('moscow', 1896.4), ('berlin', 1896.47), ('the_hague', 1896.5), ('paris', 1896.55),
    ('london', 1896.6), ('new_york', 1896.66), ((-123.1, 49.28, 1896.7)), ((117.2, 39.13, 1896.8))),
  G(1900, 1901, 'Peace talks after the Boxer Rising', ('canton', 1900.5), ('beijing', 1900.8), ('beijing', 1901.85)))
P('Zeng Guofan', 'Qing general and statesman', (1811, 1872), 3, 'war rule',
  'Confucian scholar who raised his own Hunan army and crushed the Taiping Rebellion, taking their capital Nanjing in 1864.',
  G(1853, 1864, 'The Xiang Army against the Taiping', ((112.94, 28.23, 1853.5)), ('wuhan', 1854.8), ((117.05, 30.52, 1861.7)), ('nanjing', 1864.55)),
  G(1865, 1872, 'Viceroy at Nanjing', 'nanjing'))
P('Zuo Zongtang', 'Qing general', (1812, 1885), 3, 'war',
  "General who won back the northwest and Xinjiang for China in 1867 to 1878; the American dish 'General Tso's chicken' is named after him.",
  G(1867, 1878, 'Reconquest of the northwest and Xinjiang', ('xian', 1867.5), ((103.83, 36.06, 1872.6)), ((98.5, 39.73, 1875.5)),
    ((87.62, 43.83, 1876.6)), ((75.99, 39.47, 1877.95)), ((75.99, 39.47, 1878.9))))
K('Hua Guofeng', 'Chairman of the Chinese Communist Party', (1921, 2008), 1976, 1978,
  "Mao's chosen heir, who arrested the Gang of Four a month after Mao died and was soon pushed aside by Deng Xiaoping.", 'China',
  at='beijing')
K('Jiang Zemin', 'Leader of China', (1926, 2022), 1989, 2002,
  'Shanghai party chief raised to the top after Tiananmen, who took back Hong Kong in 1997 and brought China into the World Trade Organization.',
  'China', at='beijing')
K('Hu Jintao', 'Leader of China', (1942, None), 2002, 2012,
  'Engineer who led China through its fastest growth and the Beijing Olympics of 2008.', 'China', at='beijing')
K('Chiang Ching-kuo', 'President of Taiwan', (1910, 1988), 1975, 1988,
  "Chiang Kai-shek's Soviet-educated son, who ran Taiwan after his father and ended martial law in 1987.", *TW, at='taipei')
K('Lee Teng-hui', 'President of Taiwan', (1923, 2020), 1988, 2000,
  "'Mr Democracy', the first Taiwan-born president, who won Taiwan's first direct presidential election in 1996.", *TW, at='taipei')
K('Chen Shui-bian', 'President of Taiwan', (1950, None), 2000, 2008,
  'First president from outside the Kuomintang, later jailed for corruption.', *TW, at='taipei')
K('Ma Ying-jeou', 'President of Taiwan', (1950, None), 2008, 2016,
  "Drew Taiwan closer to China and met Xi Jinping in Singapore in 2015, the first meeting of the two sides' leaders since 1949.", *TW,
  at='taipei')
K('Tsai Ing-wen', 'President of Taiwan', (1956, None), 2016, 2024,
  "Taiwan's first woman president, under whom it became the first place in Asia to allow same-sex marriage.", *TW, at='taipei')
K('Lai Ching-te', 'President of Taiwan', (1959, None), 2024, 2026,
  'Doctor turned politician, elected president of Taiwan in 2024.', *TW, at='taipei')

# ---------- the steppe, Tibet and Mongolia ----------
GH = ('Khanate of the Golden Horde', 'Golden Horde', 'Blue Horde')
GHK = 'Khan of the Golden Horde'
K('Öz Beg Khan', GHK, (1282, 1341), 1313, 1341,
  'Made Islam the faith of the Golden Horde, which reached its height under him; Ibn Battuta visited his travelling court.', *GH,
  at='sarai', tags='rule faith')
P('Jani Beg', GHK, (1310, 1357), 3, 'rule war',
  'Besieged the Genoese port of Kaffa in 1346, where by one account his men catapulted plague corpses over the walls and the Black Death set sail for Europe.',
  R(1342, 1345, GHK, *GH, at='sarai'),
  G(1346, 1346, 'Siege of Kaffa', ('sarai', 1346.2), ((35.38, 45.03, 1346.5)), ('sarai', 1346.95)),
  R(1347, 1357, GHK, *GH, at='sarai'))
P('Mamai', 'Warlord of the Golden Horde', (1335, 1380), 3, 'war rule',
  'Warlord who ruled the western Golden Horde through puppet khans until Dmitry Donskoy beat him at Kulikovo in 1380.',
  R(1361, 1379, 'Warlord of the Golden Horde', *GH, at='sarai'),
  G(1380, 1380, 'Kulikovo and flight', ((44.5, 47.0, 1380.5)), ((38.66, 53.6, 1380.69)), ((35.38, 45.03, 1380.9))))
P('Tokhtamysh', GHK, (1342, 1406), 3, 'war rule',
  'Reunited the Golden Horde with help from Timur, burned Moscow in 1382, then turned on Timur and lost everything.',
  R(1380, 1381, GHK, *GH, at='sarai'),
  G(1382, 1382, 'Sack of Moscow', ('sarai', 1382.45), ('moscow', 1382.65), ('sarai', 1382.9)),
  R(1383, 1394, GHK, *GH, at='sarai'),
  G(1395, 1406, 'Beaten by Timur, a fugitive', ((44.6, 43.5, 1395.3)), ('vilnius', 1397.0), ((34.55, 49.6, 1399.6)), ((65.53, 57.15, 1406.0))))
P('Altan Khan', 'Khan of the Tümed Mongols', (1507, 1582), 3, 'war rule faith',
  'Mongol khan who raided to the walls of Beijing in 1550, founded the city of Hohhot and gave the leader of Tibetan Buddhism the title Dalai Lama.',
  G(1542, 1582, 'Khan of the Tümed Mongols', (111.67, 40.82)),
  G(1550, 1550, 'Raid to the walls of Beijing', ((111.67, 40.82, 1550.5)), ('beijing', 1550.7), ((111.67, 40.82, 1550.9))))
P('5th Dalai Lama', 'Ruler of Tibet', (1617, 1682), 3, 'faith rule',
  "'The Great Fifth', who united Tibet under the Dalai Lamas with Mongol help in 1642 and built the Potala Palace.",
  R(1642, 1651, 'Ruler of Tibet', 'Tibet', at='lhasa'),
  G(1652, 1653, 'Visit to the Shunzhi Emperor', ('lhasa', 1652.3), ('beijing', 1653.0), ('lhasa', 1653.9)),
  R(1654, 1682, 'Ruler of Tibet', 'Tibet', at='lhasa'), wiki='5th Dalai Lama')
P('13th Dalai Lama', 'Ruler of Tibet', (1876, 1933), 3, 'faith rule',
  'Fled a British invasion in 1904 and a Chinese one in 1910, then came home and declared Tibet independent in 1913.',
  R(1895, 1903, 'Ruler of Tibet', 'Tibet', at='lhasa'),
  G(1904, 1909, 'Exile in Mongolia and China', ('lhasa', 1904.55), ('ulaanbaatar', 1904.9), ((101.57, 36.49, 1906.8)), ('beijing', 1908.75),
    ('lhasa', 1909.95)),
  G(1910, 1912, 'Exile in British India', ('lhasa', 1910.12), ((88.26, 27.04, 1910.2)), ((88.26, 27.04, 1912.5)), ('lhasa', 1913.0)),
  R(1913, 1933, 'Ruler of Tibet', 'Tibet', at='lhasa'), wiki='13th Dalai Lama')
K('Bogd Khan', 'Khan of Mongolia', (1869, 1924), 1911, 1924,
  "Tibetan-born head of Mongolia's Buddhists, made khan when Mongolia broke away from China in 1911.", 'Mongolia', at='ulaanbaatar',
  tags='rule faith')
K('Khorloogiin Choibalsan', 'Leader of Mongolia', (1895, 1952), 1939, 1952,
  "'Mongolia's Stalin', whose purges killed tens of thousands of monks and others.", 'Mongolia', at='ulaanbaatar')
K('Yumjaagiin Tsedenbal', 'Leader of Mongolia', (1916, 1991), 1952, 1984,
  'Ruled communist Mongolia for over thirty years, until he was removed while on a visit to Moscow.', 'Mongolia', at='ulaanbaatar')

# ---------- Japan ----------
JP = ('Japan', 'Imperial Japan (Fujiwara)', 'Shogun Japan (Kamakura)', 'Japan (Warring States)', 'Tokugawa shogunate', 'Imperial Japan',
      'Empire of Japan', 'Japan (USA)')
EJ, SG, PMJ, HR = 'Emperor of Japan', 'Shogun of Japan', 'Prime minister of Japan', "Shogun's regent"
K('Fujiwara no Yorimichi', 'Regent of Japan', (992, 1074), 1028, 1067,
  "Michinaga's son, regent for fifty years, who built the Phoenix Hall of the Byōdō-in, the temple on Japan's 10-yen coin.", *JP,
  at='kyoto')
K('Emperor Go-Sanjō', EJ, (1034, 1073), 1068, 1072,
  'First emperor in over a century whose mother was not a Fujiwara, who began to break their hold on the throne.', *JP, at='kyoto')
K('Emperor Shirakawa', EJ, (1053, 1129), 1073, 1129,
  "Gave up the throne and ruled for forty more years as 'cloistered emperor'; only the river, the dice and the warrior monks would not obey him.",
  *JP, at='kyoto')
K('Emperor Toba', EJ, (1103, 1156), 1130, 1156,
  'Ruled as cloistered emperor; the quarrel over his succession set the samurai clans fighting in 1156.', *JP, at='kyoto')
K('Emperor Go-Shirakawa', EJ, (1127, 1192), 1155, 1192,
  "Wily cloistered emperor who played the Taira and Minamoto clans off against each other; Yoritomo called him Japan's greatest goblin.",
  *JP, at='kyoto')
K('Taira no Kiyomori', 'Ruler of Japan', (1118, 1181), 1160, 1181,
  "First samurai to rule Japan, who put his infant grandson on the throne; his clan's fall is the story of the Tale of the Heike.", *JP,
  at='kyoto', tags='rule war')
K('Hōjō Masako', 'Ruler of the Kamakura shogunate', (1157, 1225), 1199, 1225,
  "Yoritomo's widow, the 'nun shogun', who ran the shogunate after his death and rallied the samurai to crush the emperor's revolt of 1221.",
  *JP, at='kamakura')
K('Hōjō Yasutoki', HR, (1183, 1242), 1225, 1242,
  "Gave Japan its first samurai law code in 1232, which lasted for centuries.", *JP, at='kamakura', tags='rule reform')
K('Hōjō Tokiyori', HR, (1227, 1263), 1246, 1263,
  "Zen-loving regent who, legend says, roamed the country disguised as a monk to see how his people lived.", *JP, at='kamakura')
K('Hōjō Sadatoki', HR, (1271, 1311), 1285, 1311,
  "Tokimune's son, who ruled through the costly aftermath of the Mongol invasions and cancelled the samurai's debts in 1297.", *JP,
  at='kamakura')
P('Emperor Go-Daigo', EJ, (1288, 1339), 3, 'rule war',
  'Plotted to overthrow the shogunate, was exiled to the Oki islands, escaped and brought it down in 1333, then lost to Ashikaga Takauji and set up a rival court in the mountains.',
  R(1318, 1331, EJ, *JP, at='kyoto'),
  G(1332, 1333, 'Exile on the Oki islands', ('kyoto', 1332.25), ((133.3, 36.2, 1332.35)), ((133.3, 36.2, 1333.2)), ('kyoto', 1333.45)),
  R(1334, 1335, EJ, *JP, at='kyoto'),
  G(1336, 1339, 'The Southern Court at Yoshino', (135.86, 34.37)))
K('Ashikaga Takauji', SG, (1305, 1358), 1336, 1358,
  'Samurai who turned on the Hōjō and then on Emperor Go-Daigo, and founded the Ashikaga shogunate in Kyoto.', *JP, at='kyoto',
  tags='rule war')
K('Ashikaga Yoshiakira', SG, (1330, 1367), 1358, 1367,
  "Takauji's son, who spent his reign at war with the Southern Court.", *JP, at='kyoto')
K('Ashikaga Yoshimitsu', SG, (1358, 1408), 1368, 1408,
  "Ended the split between the two courts in 1392, built the Golden Pavilion, and accepted the title 'King of Japan' from the Ming.", *JP,
  at='kyoto', tags='rule art')
K('Ashikaga Yoshimochi', SG, (1386, 1428), 1409, 1423,
  "Broke off his father's tribute trade with Ming China.", *JP, at='kyoto')
K('Ashikaga Yoshinori', SG, (1394, 1441), 1429, 1441,
  "Picked as shogun by drawing lots at a shrine; his harsh rule ended when a lord he threatened had him killed at a banquet.", *JP,
  at='kyoto')
K('Ashikaga Yoshimasa', SG, (1436, 1490), 1449, 1473,
  "Built the Silver Pavilion and loved tea and gardens, while the quarrel over his heir set off the Ōnin War that wrecked Kyoto.", *JP,
  at='kyoto', tags='rule art')
P('Takeda Shingen', 'Daimyo of Kai', (1521, 1573), 3, 'war',
  "'The Tiger of Kai', the most feared warlord of his day, who fought Uesugi Kenshin five times at Kawanakajima and died marching on Kyoto.",
  G(1541, 1571, 'Daimyo of Kai', (138.57, 35.66)),
  G(1572, 1573, 'March on Kyoto', ((138.57, 35.66, 1572.8)), ((137.73, 34.75, 1573.07)), ((137.62, 35.08, 1573.3))))
P('Uesugi Kenshin', 'Daimyo of Echigo', (1530, 1578), 3, 'war',
  "'The Dragon of Echigo', Shingen's great rival, who is said to have sent him salt when an enemy cut off his supply.",
  G(1548, 1578, 'Daimyo of Echigo', (138.24, 37.15)),
  G(1561, 1561, 'Fourth battle of Kawanakajima', ((138.24, 37.15, 1561.6)), ((138.18, 36.61, 1561.7)), ((138.24, 37.15, 1561.85))))
K('Ashikaga Yoshiaki', SG, (1537, 1597), 1568, 1573,
  'Last Ashikaga shogun, put in office by Oda Nobunaga in 1568 and driven out by him in 1573.', *JP, at='kyoto')
K('Tokugawa Hidetada', SG, (1579, 1632), 1605, 1632,
  "Ieyasu's son, who arrived too late for Sekigahara but took Osaka Castle in 1615 and made the Tokugawa peace secure.", *JP, at='edo')
K('Tokugawa Iemitsu', SG, (1604, 1651), 1633, 1651,
  'Closed Japan to the world, banned Christianity, crushed the Shimabara revolt and made the lords spend every other year in Edo.', *JP,
  at='edo')
K('Tokugawa Ietsuna', SG, (1641, 1680), 1651, 1680,
  'Shogun at ten; his reign saw the great fire of 1657 that burned most of Edo.', *JP, at='edo')
K('Tokugawa Tsunayoshi', SG, (1646, 1709), 1680, 1709,
  "'The Dog Shogun', whose laws protecting animals made harming a dog a crime punished by death; the tale of the 47 rōnin happened in his reign.",
  *JP, at='edo')
K('Tokugawa Yoshimune', SG, (1684, 1751), 1716, 1751,
  'Thrifty reformer who put a suggestion box outside his castle and let Western books into Japan again in 1720.', *JP, at='edo',
  tags='rule reform')
K('Tokugawa Ieharu', SG, (1737, 1786), 1760, 1786,
  'Left the government to the bribe-taking minister Tanuma Okitsugu as famine swept Japan.', *JP, at='edo')
K('Tokugawa Ienari', SG, (1773, 1841), 1787, 1837,
  'Longest-serving shogun, who fathered over fifty children.', *JP, at='edo')
K('Tokugawa Ieyoshi', SG, (1793, 1853), 1837, 1853,
  "Died weeks after Commodore Perry's black ships sailed into Edo Bay in 1853.", *JP, at='edo')
K('Abe Masahiro', 'Chief councillor of the shogunate', (1819, 1857), 1853, 1856,
  'Opened Japan to American ships with the treaty of Kanagawa in 1854.', *JP, at='edo')
K('Ii Naosuke', 'Great elder of the shogunate', (1815, 1860), 1858, 1860,
  "Signed the treaty that opened Japan's ports to American trade without the emperor's consent and was cut down at a castle gate in the snow.",
  *JP, at='edo')
K('Tokugawa Iemochi', SG, (1846, 1866), 1858, 1866,
  "Married the emperor's sister to heal the rift between Edo and Kyoto, and died at twenty fighting rebels.", *JP, at='edo')
P('Tokugawa Yoshinobu', 'Last shogun of Japan', (1837, 1913), 3, 'rule',
  'Last shogun, who handed power back to the emperor in 1867, lost the short war that followed, and spent his long retirement on photography and cycling.',
  R(1866, 1867, SG, *JP, at='kyoto'),
  G(1868, 1868, 'Defeat in the Boshin War', ('kyoto', 1868.05), ('osaka', 1868.08), ('edo', 1868.2), ((138.38, 34.98, 1868.6))))
P('Itō Hirobumi', 'Prime minister of Japan', (1841, 1909), 3, 'rule',
  "Japan's first prime minister and author of its 1889 constitution, who was shot dead at Harbin by a Korean patriot after ruling Korea for Japan.",
  R(1885, 1888, PMJ, *JP, at='tokyo'), R(1892, 1896, PMJ, *JP, at='tokyo'), R(1900, 1901, PMJ, *JP, at='tokyo'),
  G(1906, 1909, 'Resident-General of Korea', ('seoul', 1906.2), ('seoul', 1909.4), ('tokyo', 1909.6), ('harbin', 1909.82)))
K('Emperor Taishō', EJ, (1879, 1926), 1912, 1926,
  'Sickly emperor whose son Hirohito ruled for him from 1921.', *JP, at='tokyo')
K('Hara Takashi', PMJ, (1856, 1921), 1918, 1921,
  "Japan's first commoner prime minister, stabbed to death at Tokyo Station.", *JP, at='tokyo')
P('Shigeru Yoshida', PMJ, (1878, 1967), 3, 'rule',
  'Prime minister under the American occupation, who rebuilt Japan as a trading nation sheltering under American protection.',
  R(1946, 1947, PMJ, *JP, at='tokyo'), R(1948, 1954, PMJ, *JP, at='tokyo'))
K('Eisaku Satō', PMJ, (1901, 1975), 1964, 1972,
  'Won back Okinawa from the United States and the Nobel Peace Prize for keeping Japan free of nuclear weapons.', *JP, at='tokyo')
K('Kakuei Tanaka', PMJ, (1918, 1993), 1972, 1974,
  'Self-made builder who restored ties with China in 1972 and fell in the Lockheed bribery scandal.', *JP, at='tokyo')
K('Yasuhiro Nakasone', PMJ, (1918, 2019), 1982, 1987,
  "Reagan's close ally, who sold off Japan's state railways.", *JP, at='tokyo')
K('Akihito', EJ, (1933, None), 1989, 2019,
  'Emperor who travelled Asia to make peace with the memory of the war and became the first Japanese emperor to abdicate in two centuries.',
  *JP, at='tokyo')
K('Naruhito', EJ, (1960, None), 2019, 2026,
  'Emperor of Japan since 2019, who studied river transport on the Thames at Oxford.', *JP, at='tokyo')
K('Junichiro Koizumi', PMJ, (1942, None), 2001, 2006,
  'Maverick reformer with a lion-mane haircut and a love of Elvis, who privatised the post office.', *JP, at='tokyo')
P('Shinzo Abe', PMJ, (1954, 2022), 3, 'rule',
  "Japan's longest-serving prime minister, known for 'Abenomics', shot dead while giving a speech in 2022.",
  R(2006, 2007, PMJ, *JP, at='tokyo'), R(2012, 2020, PMJ, *JP, at='tokyo'))
K('Fumio Kishida', PMJ, (1957, None), 2021, 2024,
  'Prime minister from Hiroshima, who hosted the G7 summit there in 2023.', *JP, at='tokyo')
K('Shigeru Ishiba', PMJ, (1957, None), 2024, 2025,
  'Former defence minister, prime minister for a year.', *JP, at='tokyo')
K('Sanae Takaichi', PMJ, (1961, None), 2025, 2026,
  "Admirer of Margaret Thatcher who became Japan's first woman prime minister in 2025.", *JP, at='tokyo')

# ---------- Korea ----------
KO = ('Korea', 'Goryeo')
SK = ('Korea, Republic of', 'Korea (USA)')
KG, KJ, PSK = 'King of Goryeo', 'King of Joseon Korea', 'President of South Korea'
GANGHWA = (126.49, 37.75)
K('Hyeonjong of Goryeo', KG, (992, 1031), 1009, 1031,
  'Fled his burning capital before a Khitan invasion and came back to beat them; the first carving of the Buddhist scriptures, the Tripitaka Koreana, began under him.',
  *KO, at='kaesong')
P('Gang Gam-chan', 'Goryeo general', (948, 1031), 3, 'war',
  'Old scholar-general who destroyed a Khitan army at Gwiju in 1019, ending their invasions of Korea.',
  G(1018, 1019, 'The Khitan war', ('kaesong', 1018.85), ((124.85, 40.1, 1018.95)), ((125.3, 39.95, 1019.2)), ('kaesong', 1019.4)))
K('Munjong of Goryeo', KG, (1019, 1083), 1046, 1083,
  'Reigned in the golden age of Goryeo, when its celadon pottery and Buddhist learning flourished.', *KO, at='kaesong')
K('Sukjong of Goryeo', KG, (1054, 1105), 1095, 1105,
  "Minted Korea's first coins.", *KO, at='kaesong')
K('Yejong of Goryeo', KG, (1079, 1122), 1105, 1122,
  'Sent an army to wall off the Jurchen in the north, then gave the land back.', *KO, at='kaesong')
K('Injong of Goryeo', KG, (1109, 1146), 1122, 1146,
  "Survived two great revolts and had Kim Busik write Korea's oldest surviving history.", *KO, at='kaesong')
K('Uijong of Goryeo', KG, (1127, 1173), 1146, 1170,
  'Pleasure-loving king overthrown by his own generals in 1170, which began a century of military rule.', *KO, at='kaesong')
K('Choe Chung-heon', 'Military ruler of Goryeo', (1149, 1219), 1196, 1219,
  'General who seized power in 1196 and made kings and unmade them; his family ruled Korea for sixty years.', *KO, at='kaesong',
  tags='rule war')
K('Gojong of Goryeo', KG, (1192, 1259), 1213, 1259,
  'Reigned as the Mongols ravaged Korea; his court held out on Ganghwa Island for decades and carved the 81,000 woodblocks of the Tripitaka Koreana.',
  *KO, at=GANGHWA)
K('Chungnyeol of Goryeo', KG, (1236, 1308), 1274, 1308,
  "Married Kublai Khan's daughter and sent Korean ships and men on the Mongol invasions of Japan.", *KO, at='kaesong')
K('Gongmin of Goryeo', KG, (1330, 1374), 1351, 1374,
  'Threw off Mongol rule in 1356 and was a fine painter; he was murdered in his palace.', *KO, at='kaesong', tags='rule art')
P('Taejo of Joseon', 'Founder of Joseon Korea', (1335, 1408), 3, 'rule war',
  'General who turned his army around on an island in the Yalu instead of attacking Ming China, seized power, and founded the Joseon kingdom at Seoul.',
  G(1388, 1391, 'Turns his army back and seizes power', ((124.4, 40.1, 1388.45)), ('kaesong', 1388.6), ('kaesong', 1391.9)),
  R(1392, 1398, KJ, *KO, at='seoul'))
K('Taejong of Joseon', KJ, (1367, 1422), 1400, 1418,
  "Killed his rivals and brothers on his way to the throne, then built the strong state that his son Sejong ruled.", *KO, at='seoul')
K('Sejo of Joseon', KJ, (1417, 1468), 1455, 1468,
  'Took the throne from his boy nephew and had him killed, then ruled as a strong reformer.', *KO, at='seoul')
K('Seongjong of Joseon', KJ, (1457, 1494), 1469, 1494,
  "Finished Korea's great law code and filled his court with Confucian scholars.", *KO, at='seoul')
K('Yeonsangun of Joseon', KJ, (1476, 1506), 1494, 1506,
  "Korea's worst tyrant, who purged the scholars and turned the national academy into a pleasure ground; he was overthrown in 1506.", *KO,
  at='seoul')
K('Jungjong of Joseon', KJ, (1488, 1544), 1506, 1544,
  'Put on the throne by the coup against his half-brother; his reformer Jo Gwang-jo was purged and poisoned.', *KO, at='seoul')
K('Myeongjong of Joseon', KJ, (1534, 1567), 1545, 1567,
  'Boy king whose mother ruled in his name.', *KO, at='seoul')
P('Seonjo of Joseon', KJ, (1552, 1608), 3, 'rule',
  "King who fled his capital to the Chinese border when Hideyoshi's armies invaded in 1592, and was saved by Ming troops and Admiral Yi's fleet.",
  R(1567, 1591, KJ, *KO, at='seoul'),
  G(1592, 1593, 'Flight from the Japanese', ('seoul', 1592.35), ('pyongyang', 1592.45), ((124.53, 40.2, 1592.6)), ((124.53, 40.2, 1593.3)),
    ('seoul', 1593.8)),
  R(1594, 1608, KJ, *KO, at='seoul'))
K('Gwanghaegun of Joseon', KJ, (1575, 1641), 1608, 1623,
  'Rebuilt Korea after the Japanese war and steered between the Ming and the Manchus, until a coup sent him into exile.', *KO, at='seoul')
P('Injo of Joseon', KJ, (1595, 1649), 3, 'rule',
  'Stood a siege in the mountain fortress of Namhansanseong, then knelt and bowed nine times to the Manchu emperor Hong Taiji in 1637.',
  R(1623, 1635, KJ, *KO, at='seoul'),
  G(1636, 1637, 'Siege of Namhansanseong', ('seoul', 1636.95), ((127.18, 37.48, 1636.97)), ((127.18, 37.48, 1637.07)), ((127.05, 37.52, 1637.08)),
    ('seoul', 1637.12)),
  R(1638, 1649, KJ, *KO, at='seoul'))
P('Hyojong of Joseon', KJ, (1619, 1659), 3, 'rule',
  'Spent eight years as a Manchu hostage in Shenyang, then as king planned a revenge march north that never came; Dutch sailors were shipwrecked in his reign.',
  G(1637, 1645, 'Hostage in Shenyang', 'shenyang'), R(1649, 1659, KJ, *KO, at='seoul'))
K('Sukjong of Joseon', KJ, (1661, 1720), 1674, 1720,
  'Reigned 46 years amid fierce court factions and the drama of his consort Jang Hui-bin.', *KO, at='seoul')
K('Yeongjo of Joseon', KJ, (1694, 1776), 1724, 1776,
  'Longest-reigning king of Korea, who tried to end the court feuds and had his own son locked in a rice chest to die.', *KO, at='seoul')
K('Jeongjo of Joseon', KJ, (1752, 1800), 1776, 1800,
  'Reforming king who founded a royal library and built the fortress of Hwaseong to honour his murdered father.', *KO, at='seoul',
  tags='rule reform')
K('Sunjo of Joseon', KJ, (1790, 1834), 1800, 1834,
  "Came to the throne at ten; Korea's first Catholics were massacred in the persecution of 1801.", *KO, at='seoul')
K('Heungseon Daewongun', 'Regent of Korea', (1820, 1898), 1864, 1873,
  "Regent for his son Gojong, who shut Korea to the West, fought off French and American raids, and rebuilt the great palace in Seoul.",
  *KO, at='seoul')
K('Gojong of Korea', 'King, then emperor of Korea', (1852, 1919), 1864, 1907,
  'Last king of Joseon, who proclaimed the Korean Empire in 1897 and was forced to abdicate by Japan in 1907; his funeral sparked the protests of 1919.',
  *KO, at='seoul')
K('Empress Myeongseong', 'Queen of Korea', (1851, 1895), 1873, 1895,
  "Gojong's strong-willed queen, who led the court's resistance to Japan and was murdered in the palace by Japanese agents in 1895.", *KO,
  at='seoul')
K('Sunjong of Korea', 'Emperor of Korea', (1874, 1926), 1907, 1910,
  'Last emperor of Korea, who signed nothing as Japan annexed his country in 1910.', *KO, at='seoul')
K('Park Chung-hee', PSK, (1917, 1979), 1961, 1979,
  "General who seized power in 1961 and turned South Korea into an industrial power, until his own spy chief shot him.", *SK, at='seoul')
K('Chun Doo-hwan', PSK, (1931, 2021), 1980, 1988,
  'General who took power after Park was killed and crushed the Gwangju uprising of 1980; later sentenced to death and pardoned.', *SK,
  at='seoul')
K('Roh Tae-woo', PSK, (1932, 2021), 1988, 1993,
  "Chun's fellow general, who allowed free elections, won them and hosted the Seoul Olympics.", *SK, at='seoul')
K('Kim Young-sam', PSK, (1927, 2015), 1993, 1998,
  'First civilian president in thirty years, who put his two predecessors on trial.', *SK, at='seoul')
K('Kim Dae-jung', PSK, (1924, 2009), 1998, 2003,
  "Democracy campaigner once kidnapped and nearly drowned by the regime, who as president reached out to the North and won the Nobel Peace Prize.",
  *SK, at='seoul')
K('Roh Moo-hyun', PSK, (1946, 2009), 2003, 2008,
  'Self-taught human-rights lawyer who became president.', *SK, at='seoul')
K('Lee Myung-bak', PSK, (1941, None), 2008, 2013,
  'Former Hyundai boss, later jailed for bribery.', *SK, at='seoul')
K('Park Geun-hye', PSK, (1952, None), 2013, 2017,
  "Park Chung-hee's daughter and South Korea's first woman president, impeached and removed in 2017.", *SK, at='seoul')
K('Moon Jae-in', PSK, (1953, None), 2017, 2022,
  'Held three summits with Kim Jong Un in 2018.', *SK, at='seoul')
K('Yoon Suk Yeol', PSK, (1960, None), 2022, 2025,
  'Former prosecutor who declared martial law in December 2024 and was impeached and removed from office.', *SK, at='seoul')
K('Lee Jae-myung', PSK, (1963, None), 2025, 2026,
  "Former factory child labourer who became president after Yoon's removal in 2025.", *SK, at='seoul')

# ---------- Southeast Asia ----------
VN = ('Đại Việt', 'Annam', 'Vietnam')
SIAM = ('Ayutthaya', 'Rattanakosin Kingdom', 'Siam', 'Thailand')
BUR = ('Burmese kingdoms', 'Ava', 'Burma')
KH = ('Khmer Empire', 'Cambodia')
PH, IDN, MY = ('Philippines',), ('Indonesia',), ('Malaysia',)
EV, KS = 'Emperor of Vietnam', 'King of Siam'
K('Lý Thái Tổ', EV, (974, 1028), 1009, 1028,
  'Founded the Lý dynasty and moved the capital to Thăng Long, today Hanoi, in 1010.', *VN, at='hanoi')
P('Lý Thường Kiệt', 'Vietnamese general', (1019, 1105), 3, 'war',
  "Struck first into Song China in 1075 and stopped the Song counter-attack; the poem 'Mountains and Rivers of the Southern Country' is credited to him.",
  G(1075, 1077, 'War with Song China', ('hanoi', 1075.8), ((108.37, 22.82, 1076.1)), ('hanoi', 1076.4), ((105.95, 21.18, 1077.1)),
    ((105.95, 21.18, 1077.3))))
K('Lý Nhân Tông', EV, (1066, 1128), 1072, 1127,
  'Longest-reigning Vietnamese monarch, under whom the first national university opened in Hanoi.', *VN, at='hanoi')
K('Trần Thái Tông', EV, (1218, 1277), 1226, 1258,
  'First Trần emperor, who drove out the first Mongol invasion of Vietnam in 1258.', *VN, at='hanoi')
P('Trần Hưng Đạo', 'Vietnamese general', (1228, 1300), 2, 'war',
  "Beat the Mongols twice, in 1285 and 1288, finishing their fleet on iron-tipped stakes hidden in the Bạch Đằng River; Vietnam's greatest hero.",
  G(1284, 1285, 'The second Mongol invasion', ('hanoi', 1284.95), ((106.2, 20.4, 1285.3)), ('hanoi', 1285.5)),
  G(1287, 1288, 'The third invasion and Bạch Đằng', ('hanoi', 1287.95), ((106.8, 20.9, 1288.3)), ((106.8, 20.9, 1288.6))))
K('Lê Thánh Tông', EV, (1442, 1497), 1460, 1497,
  'Conquered the kingdom of Champa in 1471 and gave Vietnam the Hồng Đức law code.', *VN, at='hanoi')
K('Minh Mạng', EV, (1791, 1841), 1820, 1841,
  'Strict Confucian emperor who persecuted Christians and renamed his country Đại Nam.', *VN, at='hue')
K('Tự Đức', EV, (1829, 1883), 1847, 1883,
  'Scholar and poet emperor who lost southern Vietnam to France.', *VN, at='hue')
K('Bảo Đại', EV, (1913, 1997), 1926, 1945,
  'Last emperor of Vietnam, who gave up his throne to Ho Chi Minh in 1945 and died in Paris.', *VN, at='hue')
K('Lê Duẩn', 'Leader of Vietnam', (1907, 1986), 1969, 1986,
  "The real master of North Vietnam behind Ho Chi Minh, who ran the war to conquer the South and ruled united Vietnam.", 'Vietnam',
  at='hanoi', tags='rule war')
K('Nguyễn Văn Linh', 'Leader of Vietnam', (1915, 1998), 1986, 1991,
  "Launched Đổi Mới, the reforms that opened Vietnam's economy.", 'Vietnam', at='hanoi', tags='rule reform')
K('Nguyễn Phú Trọng', 'Leader of Vietnam', (1944, 2024), 2011, 2024,
  "Led Vietnam's Communist Party for thirteen years and waged a sweeping war on corruption.", 'Vietnam', at='hanoi')
K('Tô Lâm', 'Leader of Vietnam', (1957, None), 2024, 2026,
  "Former police chief who has led Vietnam's Communist Party since 2024.", 'Vietnam', at='hanoi')
P('Norodom Sihanouk', 'King of Cambodia', (1922, 2012), 3, 'rule',
  'Won Cambodia its independence from France, ruled it for thirty years, was overthrown in 1970, and came back as king in 1993.',
  R(1941, 1969, 'King, then head of state of Cambodia', *KH, at='phnom_penh'),
  G(1970, 1975, 'Exile in Beijing', 'beijing'),
  R(1993, 2004, 'King of Cambodia', *KH, at='phnom_penh'))
K('Lon Nol', 'President of Cambodia', (1913, 1985), 1970, 1975,
  'General who overthrew Sihanouk in 1970 and fled as the Khmer Rouge took Phnom Penh.', *KH, at='phnom_penh')
K('Hun Sen', 'Prime minister of Cambodia', (1952, None), 1985, 2023,
  'Former Khmer Rouge commander who ruled Cambodia for 38 years and handed power to his son.', *KH, at='phnom_penh')
K('Hun Manet', 'Prime minister of Cambodia', (1977, None), 2023, 2026,
  "Hun Sen's son, a West Point graduate.", *KH, at='phnom_penh')
K('Ramathibodi I', 'King of Ayutthaya', (1314, 1369), 1351, 1369,
  'Founded the city and kingdom of Ayutthaya, which ruled Siam for four centuries.', *SIAM, at='ayutthaya')
K('Borommatrailokkanat', 'King of Ayutthaya', (1431, 1488), 1448, 1488,
  'Reorganised Siam with a ranking of every person by land and rank that lasted into the 1900s.', *SIAM, at='ayutthaya')
K('Narai', 'King of Ayutthaya', (1632, 1688), 1656, 1688,
  'Traded with all of Europe, exchanged embassies with Louis XIV and trusted a Greek adventurer as his minister; he was overthrown as he lay dying.',
  *SIAM, at='ayutthaya')
K('Rama I', KS, (1737, 1809), 1782, 1809,
  'General who founded Bangkok and the Chakri dynasty, which still reigns in Thailand.', *SIAM, at='bangkok', wiki='Phutthayotfa Chulalok')
K('Rama II', KS, (1767, 1824), 1809, 1824,
  'Poet king of a golden age of Thai literature.', *SIAM, at='bangkok', tags='rule art', wiki='Phutthaloetla Naphalai')
K('Rama III', KS, (1788, 1851), 1824, 1851,
  'Pious king who grew rich on trade with China and signed the first treaty with Britain.', *SIAM, at='bangkok', wiki='Nangklao')
K('Mongkut', KS, (1804, 1868), 1851, 1868,
  "Spent 27 years as a monk before he became king, opened Siam to the West and appears in 'The King and I'; he caught a fatal fever watching an eclipse he had predicted.",
  *SIAM, at='bangkok', tags='rule mind')
K('Vajiravudh', KS, (1881, 1925), 1910, 1925,
  'Oxford-educated king who brought Siam into the First World War on the Allied side.', *SIAM, at='bangkok')
K('Prajadhipok', KS, (1893, 1941), 1925, 1935,
  'Last absolute king of Siam, who lost his powers in the revolution of 1932 and gave up the throne in England.', *SIAM, at='bangkok')
P('Plaek Phibunsongkhram', 'Prime minister of Thailand', (1897, 1964), 3, 'rule',
  "Military strongman who renamed Siam 'Thailand' in 1939 and sided with Japan in the Second World War.",
  R(1938, 1944, 'Prime minister of Thailand', *SIAM, at='bangkok'), R(1948, 1957, 'Prime minister of Thailand', *SIAM, at='bangkok'))
K('Bhumibol Adulyadej', KS, (1927, 2016), 1946, 2016,
  'King of Thailand for seventy years, born in Massachusetts, a jazz saxophonist and the revered arbiter of its many coups.', *SIAM,
  at='bangkok')
K('Vajiralongkorn', KS, (1952, None), 2016, 2026,
  'King of Thailand since 2016.', *SIAM, at='bangkok')
P('Bayinnaung', 'King of Burma', (1516, 1581), 3, 'rule war',
  'Built the largest empire in the history of Southeast Asia and twice took Ayutthaya.',
  R(1550, 1567, 'King of Burma', *BUR, at='pegu'),
  G(1568, 1569, 'Conquest of Ayutthaya', ('pegu', 1568.9), ('ayutthaya', 1569.6), ('pegu', 1569.9)),
  R(1570, 1581, 'King of Burma', *BUR, at='pegu'))
K('Bodawpaya', 'King of Burma', (1745, 1819), 1782, 1819,
  'Conquered Arakan and began a pagoda at Mingun meant to be the largest in the world.', *BUR, at=(96.05, 21.9))
K('Mindon Min', 'King of Burma', (1808, 1878), 1853, 1878,
  'Founded Mandalay in 1857 and hosted a great council of Buddhist monks.', *BUR, at='mandalay', tags='rule faith')
P('Thibaw Min', 'Last king of Burma', (1859, 1916), 3, 'rule',
  'Last king of Burma, deposed by the British in 1885 and exiled to India.',
  R(1878, 1885, 'King of Burma', *BUR, at='mandalay'), G(1886, 1916, 'Exile at Ratnagiri', (73.3, 16.99)))
P('Aung San', 'Founder of independent Burma', (1915, 1947), 3, 'war rule',
  'Trained in Japan to fight the British, turned on the Japanese in 1945, won Burma its independence, and was murdered months before it came.',
  G(1941, 1947, 'Fights for Burmese independence', ('tokyo', 1941.2), ('rangoon', 1942.2), ('rangoon', 1947.55)))
P('U Nu', 'Prime minister of Burma', (1907, 1995), 3, 'rule',
  'First prime minister of independent Burma, overthrown by the army in 1962.',
  R(1948, 1958, 'Prime minister of Burma', *BUR, at='rangoon'), R(1960, 1962, 'Prime minister of Burma', *BUR, at='rangoon'))
K('Ne Win', 'Leader of Burma', (1910, 2002), 1962, 1988,
  "General who seized power in 1962 and sealed Burma off on the 'Burmese Way to Socialism'.", *BUR, at='rangoon')
K('Than Shwe', 'Leader of Burma', (1933, None), 1992, 2011,
  'Head of the military junta, who built a new capital at Naypyidaw.', *BUR, at=(96.13, 19.75))
P('Aung San Suu Kyi', 'Leader of Myanmar', (1945, None), 3, 'rule reform',
  "Aung San's daughter, who spent fifteen years under house arrest, won the Nobel Peace Prize, led the country, and was locked up again after the coup of 2021.",
  G(1989, 2010, 'Under house arrest', 'rangoon'), R(2016, 2020, 'State Counsellor of Myanmar', *BUR, at=(96.13, 19.75)),
  G(2021, 2026, 'Held by the army', (96.13, 19.75)))
K('Min Aung Hlaing', 'Military ruler of Myanmar', (1956, None), 2021, 2026,
  'Army chief who seized power in the coup of 2021, plunging Myanmar into civil war.', *BUR, at=(96.13, 19.75))
P('Gajah Mada', 'Chief minister of Majapahit', (1290, 1364), 3, 'rule war',
  'Swore to taste no spice until he had united the islands of Indonesia under Majapahit, and came close.',
  G(1331, 1364, 'Chief minister of Majapahit', (112.38, -7.56)))
P('Hayam Wuruk', 'King of Majapahit', (1334, 1389), 3, 'rule',
  'Ruled the Javanese empire of Majapahit at its height.',
  G(1350, 1389, 'King of Majapahit', (112.38, -7.56)))
P('Sultan Agung of Mataram', 'Sultan of Mataram', (1593, 1645), 3, 'rule war',
  'Javanese sultan who conquered most of Java and twice besieged the Dutch in Batavia.',
  G(1613, 1645, 'Sultan of Mataram', (110.4, -7.83)),
  G(1628, 1629, 'Sieges of Batavia', ((110.4, -7.83, 1628.5)), ('batavia', 1628.7), ((110.4, -7.83, 1629.1)), ('batavia', 1629.7),
    ((110.4, -7.83, 1629.95))))
P('Diponegoro', 'Javanese prince', (1785, 1855), 3, 'war faith',
  'Prince who led the Java War against the Dutch from 1825 to 1830, was seized at peace talks and exiled.',
  G(1825, 1830, 'The Java War', ((110.36, -7.8, 1825.55)), ((110.15, -7.6, 1827.0)), ((110.22, -7.48, 1830.2))),
  G(1831, 1855, 'Exile', ((124.84, 1.49, 1831.0)), ((119.41, -5.13, 1834.0)), ((119.41, -5.13, 1855.0))))
K('B. J. Habibie', 'President of Indonesia', (1936, 2019), 1998, 1999,
  'Aircraft engineer who took over from Suharto, freed the press and let East Timor vote on independence.', *IDN, at='jakarta')
K('Abdurrahman Wahid', 'President of Indonesia', (1940, 2009), 1999, 2001,
  "Nearly blind Muslim cleric, Indonesia's first freely elected president.", *IDN, at='jakarta')
K('Megawati Sukarnoputri', 'President of Indonesia', (1947, None), 2001, 2004,
  "Sukarno's daughter and Indonesia's first woman president.", *IDN, at='jakarta')
K('Susilo Bambang Yudhoyono', 'President of Indonesia', (1949, None), 2004, 2014,
  "Retired general, Indonesia's first directly elected president.", *IDN, at='jakarta')
K('Joko Widodo', 'President of Indonesia', (1961, None), 2014, 2024,
  'Furniture seller turned mayor and president, who began building a new capital on Borneo.', *IDN, at='jakarta')
K('Prabowo Subianto', 'President of Indonesia', (1951, None), 2024, 2026,
  "Former general and Suharto's son-in-law, elected president in 2024.", *IDN, at='jakarta')
K('Tunku Abdul Rahman', 'Prime minister of Malaysia', (1903, 1990), 1957, 1970,
  'Prince who led Malaya to independence in 1957 and founded Malaysia in 1963.', *MY, at='kuala_lumpur')
K('Abdul Razak Hussein', 'Prime minister of Malaysia', (1922, 1976), 1970, 1976,
  "Launched the New Economic Policy to lift up the Malay majority.", *MY, at='kuala_lumpur')
P('Mahathir Mohamad', 'Prime minister of Malaysia', (1925, None), 3, 'rule',
  'Ruled Malaysia for 22 years, built the Petronas Towers, and came back at 92 as the oldest leader in the world.',
  R(1981, 2003, 'Prime minister of Malaysia', *MY, at='kuala_lumpur'), R(2018, 2020, 'Prime minister of Malaysia', *MY, at='kuala_lumpur'))
K('Najib Razak', 'Prime minister of Malaysia', (1953, None), 2009, 2018,
  'Lost power over the vast 1MDB fraud and was jailed.', *MY, at='kuala_lumpur')
K('Anwar Ibrahim', 'Prime minister of Malaysia', (1947, None), 2022, 2026,
  "Mahathir's deputy turned rival, twice jailed, who became prime minister in 2022.", *MY, at='kuala_lumpur')
P('José Rizal', 'Filipino writer and patriot', (1861, 1896), 2, 'art reform',
  "Doctor and novelist whose books exposed Spanish rule in the Philippines; his execution in 1896 fired the revolution.",
  G(1882, 1891, 'Studies and writes in Europe', ('manila', 1882.35), ('singapore', 1882.4), ((45.03, 12.8, 1882.48)), ((32.55, 29.97, 1882.52)),
    ((5.37, 43.3, 1882.58)), ((2.17, 41.38, 1882.6)), ('madrid', 1882.7), ('paris', 1885.5), ((8.69, 49.41, 1886.2)), ('berlin', 1886.9),
    ((5.37, 43.3, 1887.42)), ((32.55, 29.97, 1887.47)), ('singapore', 1887.55), ('manila', 1887.6), ('manila', 1888.1), ('hong_kong', 1888.13),
    ('tokyo', 1888.25), ((-122.42, 37.77, 1888.35)), ('new_york', 1888.4), ('london', 1888.45), ('paris', 1889.5), ('brussels', 1890.1),
    ((3.72, 51.05, 1891.5)), ((5.37, 43.3, 1891.8)), ((32.55, 29.97, 1891.83)), ('singapore', 1891.9), ('hong_kong', 1891.95)),
  G(1892, 1896, 'Exile in Mindanao and execution', ('hong_kong', 1892.4), ('manila', 1892.5), ((123.42, 8.65, 1892.6)), ((123.42, 8.65, 1896.6)),
    ('manila', 1896.99)))
P('Emilio Aguinaldo', 'President of the Philippines', (1869, 1964), 3, 'war rule',
  'Led the revolution against Spain, declared Philippine independence in 1898, then fought the Americans until he was captured in 1901.',
  G(1896, 1898, 'Revolution against Spain', ((120.9, 14.44, 1896.66)), ((121.08, 15.1, 1897.9)), ('hong_kong', 1898.0), ((120.9, 14.44, 1898.4))),
  R(1899, 1900, 'President of the Philippines', *PH, at=(120.81, 14.84)),
  G(1901, 1901, 'Captured at Palanan', ((122.43, 17.06, 1901.22)), ('manila', 1901.3)))
P('Manuel L. Quezon', 'President of the Philippines', (1878, 1944), 3, 'rule',
  'First president of the self-governing Philippines, who led its government in exile in America after the Japanese invaded.',
  R(1935, 1941, 'President of the Philippines', *PH, at='manila'), G(1942, 1944, 'Government in exile', ('manila', 1942.1), ('washington', 1942.4)))
P('Ferdinand Marcos', 'President of the Philippines', (1917, 1989), 3, 'rule',
  'Ruled the Philippines under martial law with his wife Imelda until the People Power revolution of 1986 drove them to Hawaii.',
  R(1965, 1985, 'President of the Philippines', *PH, at='manila'), G(1986, 1989, 'Exile in Hawaii', ('manila', 1986.15), ((-157.86, 21.31, 1986.17))))
K('Corazon Aquino', 'President of the Philippines', (1933, 2009), 1986, 1992,
  'Widow of a murdered opposition leader, swept to power by the People Power revolution of 1986.', *PH, at='manila')
K('Fidel V. Ramos', 'President of the Philippines', (1928, 2022), 1992, 1998,
  'General who helped topple Marcos and as president opened up the economy.', *PH, at='manila')
K('Gloria Macapagal Arroyo', 'President of the Philippines', (1947, None), 2001, 2010,
  'Economist president, daughter of an earlier president.', *PH, at='manila')
K('Benigno Aquino III', 'President of the Philippines', (1960, 2021), 2010, 2016,
  "Son of Corazon Aquino, who took China to court over the South China Sea and won.", *PH, at='manila')
P('Rodrigo Duterte', 'President of the Philippines', (1945, None), 3, 'rule',
  'Mayor turned president whose war on drugs killed thousands; arrested in 2025 and sent to the International Criminal Court.',
  R(2016, 2022, 'President of the Philippines', *PH, at='manila'),
  G(2025, 2026, 'Held at The Hague', ('manila', 2025.19), ('the_hague', 2025.2), ('the_hague', 2026.9)))
K('Bongbong Marcos', 'President of the Philippines', (1957, None), 2022, 2026,
  'Son of Ferdinand Marcos, elected president 36 years after his family fled.', *PH, at='manila')

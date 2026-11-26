"""The last holes in the ruler lines of the bigger countries: British India's governors-general and viceroys and the Delhi
sultans between the famous ones, late Ashikaga and Tokugawa shoguns, the Ottoman civil war of 1402, Persia between its great
dynasties, Joseon and Goryeo kings, late Mamluk sultans, doges of Venice, popes, medieval Sweden, Poland and Hungary,
interwar and postwar Austria, Portugal's First Republic and a few prime ministers and presidents elsewhere."""
from _lib import P, R, G


def K(name, role, life, a, b, why, *names, at, rank=3, tags='rule', wiki=None, short=None):
    """one reign: the ruler sits by the first of `names` on the map from year a to b, or at `at` when none is"""
    P(name, role, life, rank, tags, why, R(a, b, role, *names, at=at), wiki=wiki, short=short)


# the same map names as the ruler files before this one
EN = ('England', 'English territory', 'Angevin Empire', 'England and Ireland')
PT, PAP = ('Portugal',), ('Papal States',)
AUS = ('Austrian Empire', 'Holy Roman Empire', 'Austria Hungary', 'Austro-Hungarian Empire', 'Austria')
HU = ('Hungary', 'Kingdom of Hungary', 'Imperial Hungary')
PL = ('Poland', 'Poland-Lithuania', 'Polish–Lithuanian Commonwealth')
SWE = ('Sweden', 'Sweden–Norway', 'Kalmar Union')
OT = ('Ottoman Empire', 'Ottoman Sultanate', 'Turkey', 'Republic of Turkey')
MAM = ('Mamluke Sultanate', 'Egypt')
ILK, SAF, QAJ = ('Ilkhanate',), ('Safavid Empire',), ('Persia', 'Iran')
DS, MUG = ('Sultanate of Delhi',), ('Mughal Empire',)
BI = ('Bengal', 'British East India Company', 'British Raj', 'India')
JP = ('Japan', 'Imperial Japan (Fujiwara)', 'Shogun Japan (Kamakura)', 'Japan (Warring States)', 'Tokugawa shogunate', 'Imperial Japan',
      'Empire of Japan', 'Japan (USA)')
KO = ('Korea', 'Goryeo')
QAZVIN = (49.99, 36.27)
GG, VR, PMI = 'Governor-general of India', 'Viceroy of India', 'Prime minister of India'
DSUL, MEMP = 'Sultan of Delhi', 'Mughal emperor'
SG, SUL, SHAH = 'Shogun of Japan', 'Ottoman sultan', 'Shah of Persia'
KGO, KJO, MS = 'King of Goryeo', 'King of Joseon', 'Mamluk sultan of Egypt'
DOGE, POPE = 'Doge of Venice', 'Pope'
KSW, KPL, KH = 'King of Sweden', 'King of Poland', 'King of Hungary'
CHA, PRA = 'Chancellor of Austria', 'President of Austria'
PRP = 'President of Portugal'

# ---------- India ----------
K('Nasiruddin Mahmud Shah', DSUL, (1229, 1266), 1246, 1266,
  'Pious sultan said to have lived by copying out the Quran, while his deputy Balban ran the state.', *DS, at='delhi')
K('Jalal-ud-din Khalji', DSUL, (1220, 1296), 1290, 1296,
  'Elderly founder of the Khalji dynasty, murdered by his nephew Alauddin, who took the throne.', *DS, at='delhi')
K('Ghiyath al-Din Tughluq', DSUL, (1260, 1325), 1320, 1325,
  'Founder of the Tughluq dynasty and of the fortress city of Tughlaqabad; killed when a pavilion collapsed on him.', *DS, at='delhi')
K('Nasir-ud-Din Mahmud Shah Tughluq', DSUL, (1380, 1413), 1394, 1412,
  'Last Tughluq sultan, who fled when Timur sacked Delhi in 1398.', *DS, at='delhi')
K('Khizr Khan', DSUL, (1360, 1421), 1414, 1421,
  "Timur's governor of Multan, who took Delhi and founded the Sayyid dynasty, ruling in the name of Timur's son.", *DS, at='delhi')
K('Mubarak Shah', DSUL, (1390, 1434), 1421, 1434,
  'Sayyid sultan who held on to a shrunken Delhi Sultanate and was murdered at prayer.', *DS, at='delhi',
  wiki='Mubarak Shah (Sayyid dynasty)')
K('Ahmad Shah Bahadur', MEMP, (1725, 1775), 1748, 1754,
  'Mughal emperor deposed and blinded by his own vizier.', *MUG, at='delhi')
K('Alamgir II', MEMP, (1699, 1759), 1754, 1759,
  'Puppet emperor while Afghans and Marathas fought over Delhi; murdered by his vizier.', *MUG, at='delhi')
K('Lord Hastings', GG, (1754, 1826), 1813, 1823,
  'Fought at Bunker Hill as a young officer, and as governor-general broke the last Maratha power in 1818.', *BI, at='calcutta',
  wiki='Francis Rawdon-Hastings, 1st Marquess of Hastings')
K('Lord Amherst', GG, (1773, 1857), 1823, 1828,
  'Refused to kowtow to the emperor of China in 1816, then as governor-general fought the first war with Burma.', *BI, at='calcutta',
  wiki='William Amherst, 1st Earl Amherst')
K('Lord William Bentinck', GG, (1774, 1839), 1828, 1835,
  'Banned the burning of widows in 1829 and made English the language of higher education in India.', *BI, at='calcutta',
  tags='rule reform')
K('Lord Auckland', GG, (1784, 1849), 1836, 1842,
  'Started the First Afghan War, which ended with the army retreating from Kabul cut to pieces in 1842.', *BI, at='calcutta',
  wiki='George Eden, 1st Earl of Auckland')
P('Lord Elgin', 'Governor-general of Canada, envoy to China, viceroy of India', (1811, 1863), 3, 'rule war',
  "Accepted self-government for Canada, then as Britain's envoy in the Second Opium War had the Summer Palace in Beijing burned, and died viceroy of India.",
  R(1847, 1854, 'Governor-general of Canada', 'Canada', at='montreal'),
  G(1857, 1860, 'Envoy to China and Japan', ('hong_kong', 1857.55), ('canton', 1857.95), ('hong_kong', 1858.1), ((116.5, 22.7, 1858.15)),
    ((119.6, 24.6, 1858.2)), ((123.0, 30.5, 1858.27)), ((123.0, 37.7, 1858.35)), ((119.5, 38.6, 1858.4)), ('tianjin', 1858.45),
    ((121.0, 38.5, 1858.5)), ((123.0, 37.6, 1858.52)), ((124.5, 34.0, 1858.54)), ((128.0, 31.5, 1858.56)), ((130.7, 30.8, 1858.57)),
    ((132.5, 31.5, 1858.58)), ((133.5, 32.6, 1858.59)), ((136.0, 33.2, 1858.6)), ((139.7, 34.9, 1858.62)), ('edo', 1858.65),
    ((139.7, 34.9, 1858.68)), ((136.0, 33.2, 1858.7)), ((133.5, 32.6, 1858.71)), ((132.5, 31.5, 1858.72)), ((130.7, 30.8, 1858.73)),
    ((123.0, 27.5, 1858.8)), ((119.6, 24.6, 1858.85)), ((116.5, 22.7, 1858.88)), ('hong_kong', 1858.9), ('hong_kong', 1860.4),
    ((116.5, 22.7, 1860.43)), ((119.6, 24.6, 1860.46)), ((123.0, 30.5, 1860.5)), ((123.0, 37.7, 1860.55)), ((119.5, 38.6, 1860.58)),
    ('tianjin', 1860.62), ('beijing', 1860.79), ('beijing', 1860.9)),
  R(1862, 1863, VR, *BI, at='calcutta'), wiki='James Bruce, 8th Earl of Elgin')
K('Lord Lawrence', VR, (1811, 1879), 1864, 1869,
  "Held the Punjab for Britain in the rising of 1857, which made him 'the saviour of India' to the British.", *BI, at='calcutta',
  wiki='John Lawrence, 1st Baron Lawrence')
K('Lord Mayo', VR, (1822, 1872), 1869, 1872,
  'Stabbed to death by a convict while visiting the prison colony in the Andaman Islands.', *BI, at='calcutta',
  wiki='Richard Bourke, 6th Earl of Mayo')
K('Lord Northbrook', VR, (1826, 1904), 1872, 1876,
  'Cautious viceroy who resigned rather than push British power into Afghanistan.', *BI, at='calcutta',
  wiki='Thomas Baring, 1st Earl of Northbrook')
K('Lord Lytton', VR, (1831, 1891), 1876, 1880,
  'Poet who proclaimed Queen Victoria Empress of India at a vast durbar in 1877 while famine killed millions, and began the Second Afghan War.',
  *BI, at='calcutta', wiki='Robert Bulwer-Lytton, 1st Earl of Lytton')
K('Lord Ripon', VR, (1827, 1909), 1880, 1884,
  'Liberal viceroy whose bill letting Indian judges try Europeans set off a storm among the British in India.', *BI, at='calcutta',
  wiki='George Robinson, 1st Marquess of Ripon')
K('Lord Dufferin', VR, (1826, 1902), 1884, 1888,
  'Took Upper Burma in 1885, the year the Indian National Congress was founded.', *BI, at='calcutta',
  wiki='Frederick Hamilton-Temple-Blackwood, 1st Marquess of Dufferin and Ava')
K('Lord Lansdowne', VR, (1845, 1927), 1888, 1894,
  "Viceroy when the Durand Line was drawn between British India and Afghanistan in 1893; it is still Pakistan's disputed border.", *BI,
  at='calcutta', wiki='Henry Petty-Fitzmaurice, 5th Marquess of Lansdowne')
K('Victor Bruce, 9th Earl of Elgin', VR, (1849, 1917), 1894, 1899,
  'Viceroy through the plague and famine of the late 1890s; son of the Lord Elgin who burned the Summer Palace.', *BI, at='calcutta',
  short='Lord Elgin')
K('Lord Minto', VR, (1845, 1914), 1905, 1910,
  'His reforms of 1909 brought elected Indians onto the councils, with separate seats for Muslims.', *BI, at='calcutta',
  wiki='Gilbert Elliot-Murray-Kynynmound, 4th Earl of Minto')
K('Lord Hardinge', VR, (1858, 1944), 1910, 1916,
  'Moved the capital from Calcutta to Delhi, where a bomb thrown into his howdah wounded him in 1912.', *BI, at='delhi',
  wiki='Charles Hardinge, 1st Baron Hardinge of Penshurst')
K('Lord Chelmsford', VR, (1868, 1933), 1916, 1921,
  "Viceroy when General Dyer's troops shot down hundreds of unarmed people at Amritsar in 1919.", *BI, at='delhi',
  wiki='Frederic Thesiger, 1st Viscount Chelmsford')
K('Lord Reading', VR, (1860, 1935), 1921, 1926,
  'Rufus Isaacs, Lord Chief Justice and the first Jewish viceroy, who had Gandhi jailed in 1922.', *BI, at='delhi',
  wiki='Rufus Isaacs, 1st Marquess of Reading')
K('Lord Irwin', VR, (1881, 1959), 1926, 1931,
  "Faced Gandhi's Salt March and made a pact with him in 1931; later, as Lord Halifax, Chamberlain's foreign secretary.", *BI, at='delhi',
  wiki='E. F. L. Wood, 1st Earl of Halifax')
K('Lord Willingdon', VR, (1866, 1941), 1931, 1936,
  'Jailed Gandhi and the Congress leaders again when civil disobedience began anew in 1932.', *BI, at='delhi',
  wiki='Freeman Freeman-Thomas, 1st Marquess of Willingdon')
K('Lord Linlithgow', VR, (1887, 1952), 1936, 1943,
  'Declared India at war in 1939 without asking a single Indian, and jailed the Congress leaders in the Quit India movement of 1942.',
  *BI, at='delhi', wiki='Victor Hope, 2nd Marquess of Linlithgow')
P('Lord Wavell', VR, (1883, 1950), 3, 'war rule',
  'British commander in the Middle East who destroyed an Italian army in 1940, then the last viceroy but one, who tried and failed to keep India united.',
  G(1940, 1941, 'Commander in the Middle East', 'cairo'), R(1943, 1947, VR, *BI, at='delhi'), wiki='Archibald Wavell, 1st Earl Wavell')
K('V. P. Singh', PMI, (1931, 2008), 1989, 1990,
  'Reserved government jobs for the lower castes, setting off fierce protests.', *BI, at='delhi')
K('Chandra Shekhar', PMI, (1927, 2007), 1990, 1991,
  'Socialist who led a minority government for seven months.', *BI, at='delhi')
K('H. D. Deve Gowda', PMI, (1933, None), 1996, 1997,
  "Farmer's son from Karnataka who led a coalition for ten months.", *BI, at='delhi')
K('I. K. Gujral', PMI, (1919, 2012), 1997, 1998,
  "Diplomat whose 'Gujral doctrine' sought good terms with all of India's neighbours.", *BI, at='delhi')

# ---------- Persia ----------
K('Hasan Buzurg', 'Jalayirid ruler', (1290, 1356), 1336, 1356,
  'Founded the Jalayirid dynasty, which ruled Iraq from Baghdad as the Mongol Ilkhanate fell apart.', *ILK, at='baghdad')
K('Shaikh Uvais', 'Jalayirid sultan', (1338, 1374), 1356, 1374,
  'Took Tabriz and ruled Iraq and Azerbaijan, a great patron of Persian painting.', *ILK, at='tabriz', tags='rule art',
  wiki='Shaikh Uvais Jalayir')
K('Ismail II', SHAH, (1537, 1577), 1576, 1577,
  'Spent nearly twenty years locked in a castle by his father, then took the throne, killed most of his relatives and died within two years.',
  *SAF, at=QAZVIN)
K('Mohammad Khodabanda', SHAH, (1532, 1595), 1578, 1587,
  'Nearly blind shah under whom the Ottomans took Tabriz; deposed by his son, Abbas the Great.', *SAF, at=QAZVIN)
K('Ashraf Hotak', SHAH, (1700, 1730), 1725, 1729,
  'Afghan who took the throne in Isfahan after the Safavids fell, until Nader drove him out.', *SAF, at='isfahan')
P('Lotf Ali Khan', SHAH, (1769, 1794), 3, 'rule war',
  'Last of the Zand shahs, a dashing young warrior hunted down by Agha Mohammad Khan, who blinded thousands of men of Kerman when it fell to him in 1794.',
  R(1789, 1791, SHAH, *QAJ, at='shiraz'),
  G(1792, 1794, 'Fighting for his throne', ((52.53, 29.59, 1792.0)), ((54.4, 31.9, 1792.6)), ((57.08, 30.28, 1794.0)), ((58.35, 29.1, 1794.8))))

# ---------- Japan ----------
K('Ashikaga Yoshihisa', SG, (1465, 1489), 1473, 1489,
  'Child shogun over whose claim to succeed his father the Ōnin War began; he died in camp at 23.', *JP, at='kyoto')
P('Ashikaga Yoshitane', SG, (1466, 1523), 3, 'rule',
  'Shogun deposed in a coup in 1493, who escaped and came back to rule fifteen years later.',
  R(1490, 1493, SG, *JP, at='kyoto'), R(1508, 1521, SG, *JP, at='kyoto'))
K('Ashikaga Yoshizumi', SG, (1481, 1511), 1494, 1508,
  'Shogun put in place by the Hosokawa clan, who ran Kyoto in his name.', *JP, at='kyoto')
K('Ashikaga Yoshiharu', SG, (1511, 1550), 1521, 1546,
  'Shogun driven out of Kyoto again and again by the warring clans.', *JP, at='kyoto')
K('Ashikaga Yoshiteru', SG, (1536, 1565), 1546, 1565,
  'Swordsman shogun who was killed fighting in his own palace when the Miyoshi clan attacked it in 1565.', *JP, at='kyoto',
  tags='rule war')
K('Tokugawa Ienobu', SG, (1662, 1712), 1709, 1712,
  "Repealed Tsunayoshi's laws protecting dogs and ruled with the help of the scholar Arai Hakuseki.", *JP, at='edo')
K('Tokugawa Ietsugu', SG, (1709, 1716), 1713, 1716,
  'Became shogun at three and died at six.', *JP, at='edo')
K('Tokugawa Ieshige', SG, (1712, 1761), 1745, 1760,
  'Sickly shogun who could barely speak; his officials ruled for him.', *JP, at='edo')
K('Tokugawa Iesada', SG, (1824, 1858), 1853, 1858,
  "Shogun when Commodore Perry's black ships forced Japan to open its ports.", *JP, at='edo')

# ---------- the Ottomans ----------
K('Süleyman Çelebi', SUL, (1377, 1411), 1402, 1411,
  "Bayezid I's eldest son, who held the European half of the empire in the civil war that followed Timur's victory at Ankara.", *OT,
  at='edirne')
K('Musa Çelebi', SUL, (1388, 1413), 1411, 1413,
  'Overthrew his brother Süleyman and was killed by his brother Mehmed, who put the empire back together.', *OT, at='edirne')
K('Ahmed II', SUL, (1643, 1695), 1691, 1695,
  'Spent most of his life shut up in the palace before a short reign at war with Austria, whose armies crushed his at Slankamen in 1691.',
  *OT, at='constantinople')

# ---------- Korea ----------
K('Myeongjong of Goryeo', KGO, (1131, 1202), 1170, 1197,
  'Put on the throne by the generals who seized power in 1170, and deposed by them 27 years later.', *KO, at='kaesong')
K('Wonjong of Goryeo', KGO, (1219, 1274), 1259, 1274,
  "Made peace with the Mongols after thirty years of war, and married his son to Kublai Khan's daughter.", *KO, at='kaesong')
K('Hyeonjong of Joseon', KJO, (1641, 1674), 1659, 1674,
  'Reigned through bitter court quarrels over how long to mourn the royal dead.', *KO, at='seoul')
K('Gyeongjong of Joseon', KJO, (1688, 1724), 1720, 1724,
  'Sickly son of the executed Lady Jang, who reigned for four years.', *KO, at='seoul')
K('Heonjong of Joseon', KJO, (1827, 1849), 1834, 1849,
  'Became king at seven; his reign saw the great persecution of Korean Catholics in 1839.', *KO, at='seoul')
K('Cheoljong of Joseon', KJO, (1831, 1864), 1849, 1863,
  'A farmer on Ganghwa Island, picked to be king because he had royal blood and would be easy to control.', *KO, at='seoul')

# ---------- the Mamluks ----------
K('Al-Ashraf Khalil', MS, (1262, 1293), 1290, 1293,
  'Took Acre in 1291 and swept the last crusaders out of the Holy Land; murdered by his emirs two years later.', *MAM, at='cairo',
  tags='rule war')
K("Al-Ashraf Sha'ban", MS, (1354, 1377), 1363, 1377,
  'Boy sultan in whose reign crusaders from Cyprus sacked Alexandria in 1365; strangled by his own soldiers.', *MAM, at='cairo')
K('Jaqmaq', MS, (1373, 1453), 1438, 1453,
  'Pious old sultan who sent his fleets against the Knights of Rhodes.', *MAM, at='cairo', wiki='Sayf ad-Din Jaqmaq')
K('Inal', MS, (1381, 1461), 1453, 1461,
  'Old soldier who became sultan in the year the Ottomans took Constantinople.', *MAM, at='cairo', wiki='Sayf ad-Din Inal')
K('Khushqadam', MS, (1400, 1467), 1461, 1467,
  'Mamluk of Greek birth who rose to be sultan.', *MAM, at='cairo')
K('Tuman bay II', MS, (1476, 1517), 1516, 1517,
  'Last Mamluk sultan, who fought the Ottoman conqueror Selim to the end and was hanged at the Bab Zuwayla gate of Cairo.', *MAM,
  at='cairo', tags='rule war')

# ---------- Venice ----------
K('Domenico Michiel', DOGE, (1080, 1130), 1117, 1130,
  'Led the Venetian Crusade that smashed an Egyptian fleet and helped take Tyre in 1124.', 'Venice', at='venice', tags='rule war')
K('Vitale II Michiel', DOGE, (1110, 1172), 1156, 1172,
  'Murdered by a mob after his fleet, sent against Byzantium, came home with the plague.', 'Venice', at='venice')
K('Sebastiano Ziani', DOGE, (1102, 1178), 1172, 1178,
  'Richest man in Venice, who hosted the peace between Emperor Frederick Barbarossa and Pope Alexander III in 1177.', 'Venice',
  at='venice')
K('Pietro Ziani', DOGE, (1154, 1229), 1205, 1229,
  'Organised the empire of islands and ports that Venice won in the Fourth Crusade.', 'Venice', at='venice')
K('Ranieri Zeno', DOGE, (1200, 1268), 1253, 1268,
  'Fought Genoa in the War of Saint Sabas, the first of four great wars between the two sea republics.', 'Venice', at='venice')
K('Pietro Gradenigo', DOGE, (1251, 1311), 1289, 1311,
  "Closed the Great Council to new families in 1297, fixing Venice's ruling class for five hundred years.", 'Venice', at='venice')
K('Andrea Dandolo', DOGE, (1306, 1354), 1343, 1354,
  'Scholar doge and friend of Petrarch, who wrote a history of Venice and saw half the city die in the Black Death.', 'Venice',
  at='venice', tags='rule mind')
K('Marino Faliero', DOGE, (1285, 1355), 1354, 1355,
  "Beheaded for plotting to make himself prince; in the Doge's Palace his portrait is a painted black shroud.", 'Venice', at='venice')
K('Andrea Contarini', DOGE, (1300, 1382), 1368, 1382,
  'Old doge who led the fleet himself in the War of Chioggia, when Genoa nearly took Venice in 1380.', 'Venice', at='venice',
  tags='rule war')
K('Michele Steno', DOGE, (1331, 1413), 1400, 1413,
  "Took Padua, Verona and Vicenza, beginning Venice's empire on the mainland.", 'Venice', at='venice')
K('Tommaso Mocenigo', DOGE, (1343, 1423), 1414, 1423,
  'Warned on his deathbed against war with Milan, and against electing Foscari, who would start one.', 'Venice', at='venice')
K('Cristoforo Moro', DOGE, (1390, 1471), 1462, 1471,
  'Doge in the long war with the Ottomans that cost Venice the island of Negroponte in 1470.', 'Venice', at='venice')
K('Agostino Barbarigo', DOGE, (1419, 1501), 1486, 1501,
  "Won Cyprus for Venice in 1489 and built the clock tower on St Mark's Square.", 'Venice', at='venice')
K('Andrea Gritti', DOGE, (1455, 1538), 1523, 1538,
  "Merchant and soldier who won back Padua in 1509 and, as doge, rebuilt St Mark's Square.", 'Venice', at='venice')
P('Sebastiano Venier', DOGE, (1496, 1578), 3, 'rule war',
  'Commanded the Venetian fleet at Lepanto at the age of 75, and was made doge for it.',
  G(1571, 1571, 'Battle of Lepanto', (21.1, 38.25)), R(1577, 1578, DOGE, 'Venice', at='venice'))
K('Leonardo Donà', DOGE, (1536, 1612), 1606, 1612,
  "Defied the pope's ban on Venice in 1606, and was shown Galileo's new telescope in 1609.", 'Venice', at='venice')
P('Francesco Morosini', DOGE, (1619, 1694), 3, 'rule war',
  'Conquered the Peloponnese from the Ottomans; one of his shells blew up the Parthenon in 1687.',
  G(1685, 1687, 'Conquest of the Morea', ((21.96, 36.8, 1685.5)), ((21.98, 36.68, 1686.25)), ((21.8, 36.64, 1686.3)), ((21.6, 36.75, 1686.4)),
    ((21.67, 36.91, 1686.45)), ((21.6, 36.7, 1686.5)), ((22.0, 36.45, 1686.52)), ((22.5, 36.3, 1686.54)), ((22.9, 36.05, 1686.56)),
    ((23.3, 36.1, 1686.58)), ((23.3, 36.6, 1686.6)), ((23.0, 37.3, 1686.63)), ((22.8, 37.57, 1686.65)), ((23.0, 37.3, 1687.6)),
    ((23.3, 37.2, 1687.62)), ((23.6, 37.25, 1687.64)), ((23.7, 37.45, 1687.66)), ((23.62, 37.75, 1687.68)), ('athens', 1687.72)),
  R(1688, 1694, DOGE, 'Venice', at='venice'))


# ---------- popes ----------
def PP(name, life, a, b, why, tags='faith rule'):
    K(name, POPE, life, a, b, why, *PAP, at='rome', tags=tags)


def AV(name, life, a, b, why):
    """a pope of the Avignon years, who lived there rather than in Rome"""
    P(name, POPE, life, 3, 'faith rule', why, G(a, b, 'Pope at Avignon', 'avignon'))


PP('Pope Paschal II', (1050, 1118), 1099, 1118, 'Fought Emperor Henry V over who appoints bishops and was taken prisoner by him in 1111.')
PP('Pope Innocent II', (1080, 1143), 1130, 1143, 'Won a schism against a rival pope with the help of Bernard of Clairvaux.')
PP('Pope Eugene III', (1080, 1153), 1145, 1153, 'Monk and pupil of Bernard of Clairvaux who called the Second Crusade.')
PP('Pope Celestine III', (1106, 1198), 1191, 1198,
   'Elected at 85, he crowned the Emperor Henry VI and spent seven years trying to keep him from swallowing Italy.')
PP('Pope Honorius III', (1150, 1227), 1216, 1227,
   'Approved the new orders of St Dominic and St Francis and crowned Frederick II emperor.')
PP('Pope Alexander IV', (1199, 1261), 1254, 1261, 'Fought the heirs of Frederick II and made Clare of Assisi a saint.')
PP('Pope Urban IV', (1195, 1264), 1261, 1264,
   "Cobbler's son from Troyes who created the feast of Corpus Christi and invited Charles of Anjou to take Sicily.")
PP('Pope Clement IV', (1190, 1268), 1265, 1268,
   'French lawyer-pope who made Charles of Anjou king of Sicily; after his death the cardinals took three years to choose a successor.')
PP('Pope Nicholas III', (1225, 1280), 1277, 1280, 'Pope of the Orsini family, whom Dante put in hell for selling church offices.')
PP('Pope Martin IV', (1210, 1285), 1281, 1285,
   'So devoted to Charles of Anjou that he excommunicated the Sicilians who rose against him; Dante put him in purgatory for gluttony.')
PP('Pope Nicholas IV', (1227, 1292), 1288, 1292,
   'First Franciscan pope, who sent the friar John of Montecorvino as the first Catholic missionary to China.')
AV('Pope Benedict XII', (1285, 1342), 1334, 1342, 'Cistercian monk who began the great papal palace at Avignon.')
AV('Pope Clement VI', (1291, 1352), 1342, 1352,
   'Lavish pope who bought Avignon, and protected the Jews when they were blamed for the Black Death.')
AV('Pope Innocent VI', (1282, 1362), 1352, 1362, 'Sent Cardinal Albornoz with an army to win back the Papal States in Italy.')
P('Pope Urban V', POPE, (1310, 1370), 3, 'faith rule',
  'Took the papacy back to Rome in 1367, but returned to Avignon three years later and died there.',
  G(1362, 1370, 'Pope at Avignon and Rome', ('avignon', 1362.9), ('avignon', 1367.3), ((8.0, 43.4, 1367.38)), ((9.8, 43.2, 1367.42)),
    ((10.0, 42.6, 1367.45)), ((11.0, 42.2, 1367.5)), ('rome', 1367.8), ('rome', 1370.4), ((11.0, 42.2, 1370.55)), ((10.0, 42.6, 1370.6)),
    ((9.8, 43.2, 1370.63)), ((8.0, 43.4, 1370.66)), ('avignon', 1370.75)))
PP('Pope Boniface IX', (1350, 1404), 1389, 1404, 'Roman pope of the Great Schism, who sold indulgences on a grand scale.')
PP('Pope Innocent VII', (1336, 1406), 1404, 1406, 'Roman pope of the Great Schism, driven out of Rome by a riot in 1405.')
PP('Pope Gregory XII', (1326, 1417), 1406, 1415,
   'Resigned in 1415 to end the Great Schism, the last pope to step down until Benedict XVI.')
PP('Pope Paul II', (1417, 1471), 1464, 1471, 'Venetian pope who built the Palazzo Venezia in Rome and staged lavish carnivals.')
PP('Pope Julius III', (1487, 1555), 1550, 1555,
   'Reopened the Council of Trent, and scandalised Rome by making a teenage boy he had found in the streets a cardinal.')
PP('Pope Gregory XV', (1554, 1623), 1621, 1623,
   'Set up the office that ran Catholic missions around the world, and made Ignatius of Loyola and Francis Xavier saints.')
PP('Pope Clement IX', (1600, 1669), 1667, 1669, 'Poet and opera librettist, pope when Venice lost Crete to the Ottomans in 1669.')
PP('Pope Clement X', (1590, 1676), 1670, 1676, 'Became pope at 79 and left the work to his cardinal nephew.')
PP('Pope Innocent XII', (1615, 1700), 1691, 1700, 'Forbade popes to make their relatives rich, ending centuries of papal nepotism.',
   tags='faith rule reform')
PP('Pope Benedict XIII', (1649, 1730), 1724, 1730, 'Friar who lived as a monk while his corrupt secretary ran Rome.')
PP('Pope Leo XII', (1760, 1829), 1823, 1829, 'Stern pope who forced the Jews of Rome back into their ghetto and policed the morals of the city.')

# ---------- Sweden ----------
K('Anund Jacob', KSW, (1008, 1050), 1022, 1050,
  'Son of Olof Skötkonung, who fought Canute the Great at the Battle of Helgeå.', *SWE, at='uppsala')
K('Emund the Old', KSW, (1000, 1060), 1050, 1060, 'Last king of the old royal house of Uppsala.', *SWE, at='uppsala')
K('Stenkil', KSW, (1028, 1066), 1060, 1066,
  'Founder of a new royal house, a Christian who stopped the missionaries from tearing down the pagan temple at Uppsala.', *SWE,
  at='uppsala')
K('Inge the Elder', KSW, (1050, 1105), 1079, 1105,
  'Christian king driven out for a time by pagans when he would not hold the sacrifices at Uppsala.', *SWE, at='uppsala',
  tags='rule faith')
K('Sverker the Elder', KSW, (1100, 1156), 1130, 1156,
  "Brought in the monks who founded Sweden's first monasteries, and was murdered on his way to church at Christmas.", *SWE,
  at='uppsala')
K('Charles VII of Sweden', KSW, (1130, 1167), 1161, 1167,
  'First to be called king of the Swedes and the Goths; killed by Knut Eriksson.', *SWE, at='uppsala')
K('Knut Eriksson', KSW, (1150, 1196), 1167, 1196,
  'Son of Saint Eric, who killed King Charles to take the throne and then ruled in peace for nearly thirty years.', *SWE,
  at='uppsala')
K('Sverker the Younger', KSW, (1164, 1210), 1196, 1208,
  'Lost his throne in battle at Lena in 1208 and died trying to win it back.', *SWE, at='uppsala')
K('Eric X of Sweden', KSW, (1180, 1216), 1208, 1216, 'The first king of Sweden known to have been crowned.', *SWE, at='uppsala')
K('John I of Sweden', KSW, (1201, 1222), 1216, 1222,
  'Became king at fifteen and died at 21, the last of the house of Sverker.', *SWE, at='uppsala')
K('Eric XI of Sweden', KSW, (1216, 1250), 1222, 1250,
  "'The Lisp and Lame', in whose name the great nobles ruled; the last of Saint Eric's line.", *SWE, at='uppsala')
K('Valdemar Birgersson', KSW, (1239, 1302), 1250, 1275,
  'Son of Birger Jarl, made king as a boy; deposed by his brother Magnus.', *SWE, at='stockholm', wiki='Valdemar, King of Sweden')
K('Birger Magnusson', KSW, (1280, 1321), 1290, 1318,
  'Invited his brothers to a feast at Nyköping in 1317, threw them in the dungeon and let them starve; driven out the next year.',
  *SWE, at='stockholm', wiki='Birger, King of Sweden')
K('Albert of Mecklenburg', KSW, (1338, 1412), 1364, 1389,
  'German prince put on the Swedish throne by the nobles, who lost it to Margaret of Denmark in 1389.', *SWE, at='stockholm',
  wiki='Albert, King of Sweden')

# ---------- Poland ----------
K('Władysław II the Exile', 'High Duke of Poland', (1105, 1159), 1138, 1146,
  'Eldest son of Bolesław III, driven out by his brothers when he tried to rule all of Poland.', *PL, at='krakow')
K('Bolesław IV the Curly', 'High Duke of Poland', (1122, 1173), 1146, 1173,
  'Lost a war to Frederick Barbarossa in 1157 and had to kneel before him.', *PL, at='krakow')
K('Casimir II the Just', 'High Duke of Poland', (1138, 1194), 1177, 1194,
  "Took Kraków from his brother Mieszko the Old and was remembered as 'the Just'.", *PL, at='krakow')
K('Leszek the White', 'High Duke of Poland', (1186, 1227), 1194, 1227,
  'Murdered at a meeting of the Polish princes, leaving the country more divided than ever.', *PL, at='krakow')
K('Henry the Bearded', 'High Duke of Poland', (1165, 1238), 1232, 1238,
  'Duke of Silesia and husband of Saint Hedwig, who came close to reuniting Poland.', *PL, at='krakow')
K('Bolesław V the Chaste', 'Duke of Kraków', (1226, 1279), 1243, 1279,
  'Fled the Mongols twice and gave Kraków its town charter in 1257.', *PL, at='krakow')
K('Leszek II the Black', 'Duke of Kraków', (1241, 1288), 1279, 1288,
  'Fled to Hungary when the Mongols invaded Poland for the third time in 1287.', *PL, at='krakow')
K('Przemysł II', KPL, (1257, 1296), 1290, 1296,
  'Crowned in 1295 as the first king of Poland in two centuries, and murdered seven months later.', *PL, at='gniezno')
P('Wenceslaus II of Bohemia', 'King of Bohemia and Poland', (1271, 1305), 3, 'rule',
  'King of Bohemia, made rich by the silver mines of Kutná Hora, who was crowned king of Poland too in 1300.',
  R(1278, 1305, 'King of Bohemia', 'Bohemia', at='prague'), R(1300, 1305, KPL, *PL, at='krakow'))

# ---------- Hungary ----------
K('Stephen II of Hungary', KH, (1101, 1131), 1116, 1131, 'Warred with all his neighbours and lost most of the wars.', *HU,
  at='esztergom')
K('Béla II of Hungary', KH, (1109, 1141), 1131, 1141,
  "'The Blind', blinded as a boy by his uncle King Coloman; his queen had the nobles who had backed it massacred.", *HU, at='esztergom')
K('Stephen III of Hungary', KH, (1147, 1172), 1162, 1172,
  'Fought off the Byzantine emperor Manuel, who tried to make Hungary a client state.', *HU, at='esztergom')
K('Emeric of Hungary', KH, (1174, 1204), 1196, 1204,
  'Lost the city of Zara to the Fourth Crusade, which Venice turned against it in 1202.', *HU, at='esztergom',
  wiki='Emeric, King of Hungary')

# ---------- Austria ----------
K('Michael Hainisch', PRA, (1858, 1940), 1920, 1928, 'First president of the Austrian republic.', *AUS, at='vienna')
P('Ignaz Seipel', CHA, (1876, 1932), 3, 'rule faith',
  'Catholic priest who was twice chancellor and saved the currency with a loan from the League of Nations.',
  R(1922, 1924, CHA, *AUS, at='vienna'), R(1926, 1929, CHA, *AUS, at='vienna'))
K('Wilhelm Miklas', PRA, (1872, 1956), 1928, 1938,
  'President when Hitler took Austria in 1938, who held out longest against appointing a Nazi chancellor.', *AUS, at='vienna')
K('Leopold Figl', CHA, (1902, 1965), 1945, 1953,
  "Survived Dachau to become postwar Austria's first chancellor; as foreign minister he signed the treaty that freed Austria in 1955.",
  *AUS, at='vienna')
K('Julius Raab', CHA, (1891, 1964), 1953, 1961,
  'Negotiated the end of the four-power occupation in Moscow in 1955, in return for Austrian neutrality.', *AUS, at='vienna')
K('Alfons Gorbach', CHA, (1898, 1972), 1961, 1964, 'Another survivor of Dachau, chancellor for three years.', *AUS, at='vienna')
K('Josef Klaus', CHA, (1910, 2001), 1964, 1970, "Led Austria's first one-party government after the war.", *AUS, at='vienna')
K('Fred Sinowatz', CHA, (1929, 2008), 1983, 1986, 'Chancellor when the Waldheim affair broke.', *AUS, at='vienna')
K('Franz Vranitzky', CHA, (1937, None), 1986, 1997,
  'Banker who took Austria into the European Union in 1995 and admitted its share of guilt for the Holocaust.', *AUS, at='vienna')
K('Viktor Klima', CHA, (1947, None), 1997, 2000, 'Former oil company manager, chancellor for three years.', *AUS, at='vienna')
K('Wolfgang Schüssel', CHA, (1945, None), 2000, 2007,
  'Brought the far-right Freedom Party into government in 2000, and the rest of the EU shunned Austria for months.', *AUS,
  at='vienna')
K('Werner Faymann', CHA, (1960, None), 2008, 2016, 'Chancellor in the refugee crisis of 2015.', *AUS, at='vienna')

# ---------- Portugal, England and France ----------
K('Manuel de Arriaga', PRP, (1840, 1917), 1911, 1915,
  'Lawyer elected the first president of the Portuguese republic, who resigned in 1915.', *PT, at='lisbon')
P('Bernardino Machado', PRP, (1851, 1944), 3, 'rule',
  'Twice president and overthrown both times: by Sidónio Pais in 1917 and by the army in 1926.',
  R(1915, 1917, PRP, *PT, at='lisbon'), R(1925, 1926, PRP, *PT, at='lisbon'))
K('António José de Almeida', PRP, (1866, 1929), 1919, 1923,
  'The only president of the First Republic to finish his term.', *PT, at='lisbon')
K('Manuel Teixeira Gomes', PRP, (1860, 1941), 1923, 1925,
  'Writer who gave up the presidency and spent his last years in Algeria.', *PT, at='lisbon', tags='rule art')
K('Harold Harefoot', 'King of England', (1016, 1040), 1035, 1040,
  'Son of Canute, who took England while his half-brother Harthacnut was away in Denmark.', *EN, at='london')

# ---------- Canada, Australia and Argentina ----------
K('Lord Durham', 'Governor-general of British North America', (1792, 1840), 1838, 1838,
  "'Radical Jack', sent to Canada after the rebellions of 1837, whose report urged self-government and the union of the two Canadas.",
  'Canada', at='quebec', wiki='John Lambton, 1st Earl of Durham')
P('Louis-Joseph Papineau', 'Leader of the Patriotes', (1786, 1871), 3, 'reform',
  'Led the French-Canadian Patriotes, whose rising of 1837 was crushed; he fled to the United States and then to France.',
  G(1837, 1838, 'The Patriote rising', ('montreal', 1837.85), ((-73.16, 45.78, 1837.88)), ((-73.45, 44.7, 1837.95)), ((-73.75, 42.65, 1838.5))))
K('John Gorton', 'Prime minister of Australia', (1911, 2002), 1968, 1971,
  'Fighter pilot whose face was rebuilt after a crash in the war; he lost his party\'s vote of confidence with his own casting vote.',
  'Australia', at='canberra')
K('William McMahon', 'Prime minister of Australia', (1908, 1988), 1971, 1972,
  'Lost to Gough Whitlam in 1972, ending 23 years of conservative rule.', 'Australia', at='canberra')
K('José Figueroa Alcorta', 'President of Argentina', (1860, 1931), 1906, 1910,
  'The only Argentine to lead all three branches of government: the Senate, the presidency and the supreme court.', 'Argentina',
  at='buenos_aires')
K('Ramón Castillo', 'President of Argentina', (1873, 1944), 1940, 1943,
  'Kept Argentina neutral in the Second World War until the army threw him out in 1943.', 'Argentina', at='buenos_aires')
K('Eduardo Duhalde', 'President of Argentina', (1941, None), 2002, 2003,
  "Chosen by Congress to steer Argentina out of the crash of 2001; he cut the peso's tie to the dollar.", 'Argentina',
  at='buenos_aires')

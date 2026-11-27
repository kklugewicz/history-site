"""Migrations of the modern age, 1788 to today: the great emigrations, the settlers of the American West, indentured and
Chinese labour, the deportations and population exchanges of the world wars, partition, and the refugees of our time."""
from _lib import M, S, mv, site

M('australia', 'Convicts and settlers to Australia', 'Convicts and settlers', 'forced', '#1b4f72', 1787, 1868,
  'In 1788 the First Fleet landed 750 convicts at Sydney Cove, on land the Eora people had lived on for tens of thousands of '
  'years. Britain transported some 162,000 convicts to Australia until 1868. Free settlers came too, and after gold was '
  'found in 1851 they came in floods: Australia\'s population tripled in ten years.',
  story='ev:first-fleet', rank=1, steps=[
    S(1787, '1787 to 1830', 'The First Fleet',
      'Eleven ships sailed from Portsmouth in May 1787 by Tenerife, Rio and the Cape, eight months and 24,000 km, and anchored '
      'in Botany Bay in January 1788. Governor Phillip moved on to Sydney Cove.',
      moves=[mv('sail', (-1.1, 50.75, 1787), (-3.0, 49.9, 1787), (-6.0, 48.5, 1787), (-11.0, 42.0, 1787), (-16.0, 28.6, 1787), (-24.0, 10.0, 1787),
                (-33.0, -10.0, 1787), (-36.0, -18.0, 1787), (-40.0, -23.5, 1787), (-42.8, -23.2, 1787), (-30.0, -30.0, 1787), (0.0, -36.0, 1787), (17.8, -34.5, 1787), (20.0, -35.5, 1787), (40.0, -40.0, 1787),
                (80.0, -43.0, 1788), (120.0, -42.0, 1788), (146.0, -44.5, 1788), (148.8, -43.5, 1788), (150.5, -38.0, 1788), (151.25, -34.0, 1788), label='First Fleet', until=1840)],
      sites=[site('Sydney Cove', 151.21, -33.86, 1788, 'The convict colony of New South Wales, founded 26 January 1788.'),
             site('Van Diemen\'s Land', 147.33, -42.88, 1803, 'Tasmania, where the worst offenders were sent.')]),
    S(1830, '1830 to 1868', 'Free settlers and gold',
      'Assisted passages brought poor British and Irish families. The gold rushes of Victoria from 1851 drew diggers from '
      'everywhere; Melbourne became one of the richest cities in the world. The last convict ship reached Western Australia in 1868.',
      moves=[mv('sail', (-3.1, 53.45, 1830), (-3.4, 53.55, 1830), (-4.6, 53.55, 1830), (-5.5, 52.6, 1830), (-6.0, 51.8, 1830), (-7.0, 51.0, 1830), (-12.0, 45.0, 1831), (-20.0, 20.0, 1831), (-28.0, 0.0, 1831), (-25.0, -25.0, 1831),
                (10.0, -40.0, 1832), (60.0, -44.0, 1832), (110.0, -42.0, 1832), (140.0, -40.0, 1833), (144.3, -39.2, 1833), (144.7, -38.4, 1833), label='Emigrants', until=1868)],
      sites=[site('Ballarat', 143.85, -37.56, 1851, 'The gold fields of Victoria, and the Eureka rebellion of 1854.')]),
  ])

M('atlantic-emigration', 'The great Atlantic migration', 'European emigrants', 'emigrants', '#21618c', 1820, 1924,
  'Between 1820 and 1924 some 55 million Europeans crossed the Atlantic, the largest voluntary migration in history: '
  'Irish fleeing famine, Germans and Scandinavians seeking land, Italians, Poles and Jews from the Russian Empire seeking '
  'work and freedom. Most went to the United States; millions to Argentina, Brazil and Canada. Steamships cut the crossing '
  'from six weeks to one, until the United States closed its doors in 1924.',
  numbers='About 55 million people, 1820 to 1924', rank=1, steps=[
    S(1820, '1820 to 1845', 'The first wave',
      'Sailing ships carried British, Irish and German emigrants from Liverpool and Le Havre, often in the holds that carried '
      'cotton the other way.',
      moves=[mv('sail', (-3.1, 53.45, 1820), (-3.4, 53.55, 1820), (-4.6, 53.55, 1820), (-5.5, 52.6, 1820), (-6.5, 51.5, 1821), (-20.0, 50.0, 1821), (-50.0, 43.0, 1822), (-70.0, 40.2, 1822), (-74.0, 40.6, 1823), label='Liverpool to New York', until=1924)]),
    S(1845, '1845 to 1880', 'Famine and revolution',
      'The Great Famine drove a million and a half Irish to America in ten years, many on "coffin ships". After the failed '
      'revolutions of 1848 Germans came in hundreds of thousands, and Scandinavians filled the Midwest.',
      moves=[mv('sail', (-8.3, 51.75, 1845), (-8.3, 51.5, 1845), (-12.0, 51.0, 1846), (-35.0, 46.0, 1846), (-60.0, 42.5, 1847), (-70.0, 42.3, 1847), (-71.0, 42.35, 1848), label='Irish to Boston', until=1924),
             mv('steam', (8.6, 53.9, 1848), (4.0, 53.3, 1848), (2.0, 51.5, 1849), (1.0, 50.7, 1849), (-2.0, 50.2, 1849), (-5.5, 49.5, 1849), (-20.0, 48.0, 1849),
                (-50.0, 42.0, 1850), (-70.0, 40.2, 1850), (-74.0, 40.6, 1850), label='Germans to New York', until=1924)],
      sites=[site('Cobh', -8.3, 51.85, 1845, 'Queenstown, last sight of Ireland for millions of emigrants.'),
             site('Castle Garden', -74.02, 40.7, 1855, 'New York\'s immigrant station before Ellis Island.')]),
    S(1880, '1880 to 1914', 'The new immigrants',
      'Now the emigrants came from the south and east: Italians, Poles, Greeks, Hungarians and Jews. Ellis Island opened in '
      '1892; in 1907 alone 1.3 million people entered the United States. Italians and Spaniards made Buenos Aires.',
      moves=[mv('steam', (14.25, 40.8, 1880), (12.0, 40.0, 1880), (9.5, 38.3, 1881), (5.0, 37.8, 1881), (-1.0, 36.5, 1881), (-5.6, 35.95, 1881), (-7.0, 36.0, 1881),
                (-20.0, 36.0, 1882), (-50.0, 39.0, 1882), (-70.0, 40.2, 1883), (-74.0, 40.6, 1883), label='Italians to New York', until=1924),
             mv('steam', (-7.0, 36.0, 1882), (-12.0, 30.0, 1882), (-18.5, 29.5, 1882), (-19.0, 24.0, 1882), (-21.0, 12.0, 1883), (-20.0, 10.0, 1883), (-30.0, -5.0, 1883), (-38.0, -20.0, 1884), (-50.0, -35.5, 1884),
                (-55.5, -35.6, 1885), (-57.5, -35.0, 1885), (-58.37, -34.6, 1885), label='To Buenos Aires', until=1924)],
      sites=[site('Ellis Island', -74.04, 40.7, 1892, 'Through which 12 million immigrants passed, 1892 to 1954.'),
             site('Buenos Aires', -58.38, -34.6, 1914, 'By 1914 half its people were born abroad.')]),
    S(1914, '1914 to 1924', 'The door closes',
      'The First World War halted the flow; afterwards, the United States passed quota laws in 1921 and 1924 that all but shut '
      'out southern and eastern Europeans. The age of mass migration across the Atlantic was over.',
      moves=[mv('steam', (8.6, 53.9, 1919), (4.0, 53.3, 1919), (2.0, 51.5, 1919), (1.0, 50.7, 1919), (-2.0, 50.2, 1919), (-5.5, 49.5, 1920), (-20.0, 48.0, 1920),
                (-50.0, 42.0, 1920), (-70.0, 40.2, 1921), (-74.0, 40.6, 1921), label='Last of the great flow')],
      sites=[site('Washington', -77.04, 38.9, 1924, 'The Immigration Act of 1924 sets national quotas.')]),
  ])

M('indian-indenture', 'Indian indentured labourers', 'Indian labourers', 'forced', '#ca6f1e', 1834, 1920,
  'When the British Empire ended slavery in 1834, planters turned to India. Over 1.3 million Indians signed five-year '
  'contracts of indenture, many tricked or desperate, and sailed to the sugar colonies: Mauritius, Guyana, Trinidad, Natal, '
  'Fiji. Gandhi fought for them in South Africa. Today their descendants are half the people of Mauritius, Guyana and '
  'Trinidad.',
  numbers='About 1.3 million people, 1834 to 1920', rank=2, steps=[
    S(1834, '1834 to 1860', 'To Mauritius and the Caribbean',
      'The first ships left Calcutta for Mauritius in 1834 and for British Guiana in 1838. The voyage to the Caribbean round '
      'the Cape took three months.',
      moves=[mv('sail', (88.2, 21.6, 1834), (88.0, 19.0, 1834), (85.0, 10.0, 1834), (81.0, 4.5, 1834), (70.0, -5.0, 1835), (60.0, -15.0, 1835), (57.6, -20.0, 1835), label='To Mauritius', until=1920),
             mv('sail', (81.0, 4.5, 1838), (60.0, -15.0, 1838), (45.0, -28.0, 1838), (20.0, -36.5, 1839), (5.0, -25.0, 1839), (-20.0, -10.0, 1839), (-40.0, 2.0, 1839),
                (-55.0, 8.0, 1840), (-58.15, 6.85, 1840), label='To Guyana and Trinidad', until=1917)],
      sites=[site('Aapravasi Ghat', 57.5, -20.16, 1834, 'Immigration depot in Port Louis where half a million Indians landed.')]),
    S(1860, '1860 to 1920', 'Natal and Fiji',
      'From 1860 Indians were shipped from Madras to Natal\'s sugar fields, and from 1879 to Fiji. Indenture was abolished in '
      '1917 to 1920 after a long campaign in India.',
      moves=[mv('sail', (80.3, 13.0, 1860), (82.5, 8.0, 1860), (81.0, 4.5, 1860), (60.0, -15.0, 1860), (45.0, -28.0, 1860), (33.0, -30.5, 1860), (31.1, -29.9, 1860), label='To Natal', until=1911),
             mv('sail', (88.2, 21.6, 1879), (88.0, 19.0, 1879), (93.0, 5.0, 1879), (105.0, -10.0, 1879), (110.0, -36.0, 1879), (146.0, -45.0, 1879), (165.0, -37.0, 1879),
                (177.5, -18.2, 1879), label='To Fiji', until=1916)],
      sites=[site('Durban', 31.03, -29.86, 1860, 'Where Gandhi began his struggle for the rights of Indians.')]),
  ])

M('chinese-diaspora', 'The Chinese go overseas', 'Chinese emigrants', 'emigrants', '#c0392b', 1848, 1930,
  'From the 1840s, war, rebellion and famine in southern China and the demand for labour abroad sent millions of men from '
  'Guangdong and Fujian overseas: to the tin mines and plantations of Malaya and the Dutch Indies, to the gold rushes of '
  'California and Australia, to the guano pits of Peru, and to build the Central Pacific Railroad. Most meant to return; '
  'many stayed, founding the Chinatowns of the world.',
  numbers='About 20 million left southern China, 1840 to 1940', rank=2, steps=[
    S(1848, '1848 to 1882', 'Gold Mountain',
      'News of gold in California in 1848 brought tens of thousands from Hong Kong to "Gold Mountain"; they built the western '
      'part of the first transcontinental railroad, until the Chinese Exclusion Act of 1882 shut them out.',
      moves=[mv('steam', (114.2, 22.2, 1849), (121.5, 21.5, 1849), (140.0, 30.0, 1850), (180.0, 38.0, 1850), (-150.0, 38.0, 1851), (-123.0, 37.7, 1851), (-122.4, 37.8, 1852), label='To California', until=1882),
             mv('steam', (114.2, 22.2, 1853), (114.5, 21.0, 1853), (112.0, 12.0, 1853), (108.0, 5.0, 1854), (107.0, 0.0, 1854), (107.0, -2.8, 1854), (106.2, -5.5, 1854),
                (105.6, -6.4, 1855), (104.5, -8.0, 1855), (110.0, -20.0, 1855), (111.0, -25.0, 1855), (113.5, -35.5, 1856), (130.0, -37.5, 1856), (140.0, -39.5, 1856), (144.3, -39.2, 1857), (144.7, -38.4, 1857), label='To the Victorian gold fields', until=1890)],
      sites=[site('San Francisco', -122.41, 37.79, 1852, 'Its Chinatown is the oldest in North America.')]),
    S(1860, '1860 to 1930', 'Nanyang, the southern seas',
      'Far more went south, to Singapore, Penang, Bangkok, Batavia and Manila, as coolies, traders and miners. By 1930 Chinese '
      'were the majority in Singapore and a third of Malaya.',
      moves=[mv('steam', (118.1, 24.3, 1860), (116.0, 22.0, 1861), (113.0, 18.0, 1862), (110.0, 12.0, 1863), (107.0, 6.0, 1864), (104.5, 2.0, 1865), (103.85, 1.25, 1866), label='To Singapore', until=1930)],
      sites=[site('Singapore', 103.85, 1.29, 1900, 'A British port that became a Chinese city.')]),
  ])

M('american-west', 'The trails west', 'American settlers', 'settlers', '#a04000', 1841, 1869,
  'From 1841, wagon trains of American families set out from the Missouri on the 3,000 km Oregon Trail. The Mormons, '
  'driven out of Illinois, trekked to the Great Salt Lake in 1847; the next year gold was found in California, and in 1849 '
  'a hundred thousand "forty-niners" rushed west. Some 400,000 people took the trails before the railroad was finished in '
  '1869, crossing lands that were home to the Lakota, Cheyenne and Shoshone.',
  rank=1, steps=[
    S(1841, '1841 to 1846', 'The Oregon Trail',
      'Wagon trains left Independence in spring to cross the plains, the Rockies at South Pass and the Blue Mountains before '
      'the snows. One in ten died on the way, most of cholera.',
      moves=[mv('wagon', (-94.42, 39.09, 1841), (-96.7, 40.0, 1842), (-98.98, 40.64, 1842), (-102.0, 41.1, 1842), (-104.55, 42.2, 1843), (-108.9, 42.35, 1843),
                (-112.45, 43.0, 1844), (-116.5, 44.0, 1844), (-119.5, 45.6, 1845), (-122.6, 45.36, 1846), label='Oregon Trail', until=1869)],
      sites=[site('Independence Rock', -107.13, 42.49, 1843, 'Emigrants hoped to reach it by 4 July to beat the snows.'),
             site('Oregon City', -122.6, 45.36, 1846, 'End of the Oregon Trail.')]),
    S(1846, '1846 to 1847', 'The Mormon trek',
      'After their prophet Joseph Smith was murdered, Brigham Young led the Latter-day Saints out of Nauvoo across Iowa and '
      'Nebraska to the valley of the Great Salt Lake, where he said, "This is the place."',
      moves=[mv('wagon', (-91.38, 40.55, 1846), (-93.5, 41.0, 1846), (-95.95, 41.32, 1846), (-99.0, 40.7, 1847), (-104.55, 42.2, 1847), (-108.9, 42.35, 1847),
                (-110.5, 41.3, 1847), (-111.89, 40.76, 1847), label='Mormon Trail', until=1869)],
      sites=[site('Salt Lake City', -111.89, 40.76, 1847, 'Founded by the Mormon pioneers on 24 July 1847.')]),
    S(1849, '1849 to 1869', 'Gold, and the railroad',
      'In 1849 the gold rush turned the trails into highways. California went from 15,000 settlers to a state of 250,000 in '
      'four years. In 1869 the railroads met at Promontory, and the wagon trains were over.',
      moves=[mv('wagon', (-112.45, 43.0, 1849), (-114.5, 41.5, 1849), (-117.7, 40.9, 1849), (-119.8, 39.5, 1849), (-121.5, 38.58, 1849), label='California Trail', until=1869),
             mv('train', (-95.95, 41.25, 1866), (-104.8, 41.14, 1867), (-110.0, 41.5, 1868), (-112.55, 41.62, 1869), label='Union Pacific')],
      sites=[site('Sutter\'s Mill', -120.89, 38.8, 1848, 'Where gold was found in January 1848.'),
             site('Promontory', -112.55, 41.62, 1869, 'The golden spike joins the first railroad across America.')]),
  ])

M('circassians', 'The Circassian exile', 'Circassians', 'forced', '#196f3d', 1863, 1865,
  'At the end of a century of war in the Caucasus, the Russian army drove the Circassians and other peoples of the north-west '
  'Caucasus from their mountains in 1863 and 1864. Hundreds of thousands were herded to the Black Sea shore and shipped to the '
  'Ottoman Empire in overcrowded boats; many died of hunger, cold and disease. Circassians remember it as a genocide; their '
  'descendants live in Turkey, Syria and Jordan.',
  numbers='Perhaps 500,000 to 1,000,000 expelled', rank=2, steps=[
    S(1863, '1863 to 1864', 'To the Black Sea shore',
      'Russian columns burned the villages valley by valley. The last Circassian resistance ended at Kbaada, today\'s Krasnaya '
      'Polyana above Sochi, in May 1864.',
      moves=[mv('foot', (40.5, 44.6, 1863), (39.5, 44.3, 1863), (38.5, 44.5, 1864), (39.7, 43.6, 1864), label='Circassians')],
      sites=[site('Kbaada', 40.2, 43.68, 1864, 'Russia\'s victory parade marks the end of the Caucasian War.')]),
    S(1864, '1864 to 1865', 'Across the sea',
      'From Tuapse, Sochi and Anapa, crowded boats carried the exiles to Trabzon, Samsun and Varna, where tens of thousands '
      'died in camps. The Ottomans settled them across Anatolia, the Balkans and Syria.',
      moves=[mv('sail', (39.6, 43.5, 1864), (39.0, 42.5, 1864), (39.7, 41.1, 1864), label='To Trabzon'),
             mv('sail', (38.9, 44.0, 1864), (37.0, 43.0, 1864), (36.4, 41.4, 1864), label='To Samsun'),
             mv('foot', (36.4, 41.3, 1864), (36.0, 39.5, 1865), (36.4, 36.5, 1865), (36.0, 32.5, 1865), label='To Syria and Jordan')],
      sites=[site('Samsun', 36.33, 41.29, 1864, 'A port where tens of thousands of exiles died in camps.')]),
  ])

M('manchuria', 'Crashing into Manchuria', 'Chinese settlers', 'settlers', '#e67e22', 1860, 1930,
  'For two centuries the Qing kept their Manchu homeland closed to Chinese settlers. When the ban crumbled after 1860, '
  'peasants from overcrowded, famine-stricken Shandong and Hebei poured north, the Chuang Guandong, "crashing past the '
  'pass". Some 25 million came by 1930, by junk across the Bohai Sea and on foot past the Great Wall, and later by '
  'railway. It was one of the largest migrations in history.',
  numbers='About 25 million people', rank=2, steps=[
    S(1860, '1860 to 1900', 'Past the pass',
      'Settlers walked through Shanhaiguan, where the Great Wall meets the sea, or crossed from the Shandong peninsula to the '
      'Liaodong peninsula by boat, and cleared the black-earth plains.',
      moves=[mv('foot', (117.0, 36.7, 1860), (118.5, 38.5, 1870), (119.75, 40.0, 1880), (121.5, 41.0, 1890), (123.4, 41.8, 1900), label='Shandong settlers'),
             mv('sail', (121.4, 37.6, 1870), (121.4, 38.3, 1870), (121.6, 38.9, 1870), label='Across the Bohai')],
      sites=[site('Shanhaiguan', 119.75, 40.0, 1880, '"The first pass under heaven", where the Great Wall reaches the sea.')]),
    S(1900, '1900 to 1930', 'By railway to the north',
      'The Russian-built Chinese Eastern Railway and the South Manchuria Railway carried migrants north to Harbin and beyond; '
      'in the late 1920s a million came every year, fleeing famine and warlords.',
      moves=[mv('train', (121.6, 38.9, 1903), (122.5, 40.6, 1910), (123.4, 41.8, 1915), (125.3, 43.9, 1920), (126.63, 45.75, 1925), (128.0, 47.5, 1930), label='Settlers by rail')],
      sites=[site('Harbin', 126.63, 45.75, 1925, 'A railway town that grew into a city of half a million.')]),
  ])

M('jewish-emigration', 'Jews leave the Russian Empire', 'Jewish emigrants', 'emigrants', '#5b2c6f', 1881, 1924,
  'After the pogroms of 1881 and the harsh May Laws, some two and a half million Jews left the Russian Empire, mostly from the '
  'Pale of Settlement, in forty years. Nearly all went to America: New York\'s Lower East Side became the most crowded place '
  'on earth. A few thousand idealists went to Ottoman Palestine to farm, the first waves of Zionist immigration.',
  rank=2, steps=[
    S(1881, '1881 to 1914', 'To America',
      'Emigrants crossed the German border, often illegally, and took ship at Hamburg and Bremen. Some 2 million reached the '
      'United States.',
      moves=[mv('train', (30.5, 50.45, 1881), (27.0, 53.9, 1882), (23.2, 53.1, 1882), (17.0, 52.4, 1883), (13.4, 52.52, 1883), (10.0, 53.55, 1884), label='To Hamburg', until=1914),
             mv('steam', (8.6, 53.9, 1884), (4.0, 53.3, 1884), (2.0, 51.5, 1885), (1.0, 50.7, 1885), (-2.0, 50.2, 1885), (-5.5, 49.5, 1885), (-20.0, 48.0, 1886),
                (-50.0, 42.0, 1886), (-70.0, 40.2, 1887), (-74.0, 40.6, 1887), label='To New York', until=1924)],
      sites=[site('Lower East Side', -73.99, 40.72, 1900, 'New York\'s Jewish quarter of tenements and garment shops.')]),
    S(1882, '1882 to 1914', 'To Palestine',
      'In the First and Second Aliyah some 60,000 Jews, many of them young socialists, settled in Ottoman Palestine, founding '
      'farming colonies, the first kibbutz at Degania in 1910, and Tel Aviv in 1909.',
      moves=[mv('steam', (30.7, 46.45, 1882), (30.5, 44.0, 1883), (29.2, 41.4, 1883), (29.05, 41.1, 1883), (28.0, 40.8, 1883), (26.7, 40.4, 1884), (26.2, 40.05, 1884),
                (25.5, 38.5, 1884), (27.0, 36.0, 1885), (32.0, 33.5, 1885), (34.6, 32.1, 1886), (34.75, 32.05, 1886), label='From Odessa to Jaffa', until=1914)],
      sites=[site('Tel Aviv', 34.78, 32.08, 1909, 'Founded on the dunes outside Jaffa in 1909.')]),
  ])

M('armenian-deportations', 'The Armenian deportations', 'Armenians', 'forced', '#78281f', 1915, 1916,
  'In 1915 the Ottoman government ordered the Armenians of Anatolia deported to the Syrian desert. Men were mostly killed at '
  'once; women, children and the old were marched for months to Aleppo and Deir ez-Zor. Some 1 million or more died, by '
  'massacre, starvation and disease, in what is recognised as the Armenian genocide.',
  story='ev:armenian-genocide', numbers='About 1 million or more killed', rank=2, steps=[
    S(1915, '1915', 'The death marches',
      'Convoys from Erzurum, Sivas, Harput and the other towns of the east were driven south through the mountains to Aleppo.',
      moves=[mv('foot', (41.27, 39.9, 1915), (39.5, 39.3, 1915), (39.2, 38.7, 1915), (38.3, 38.35, 1915), (37.5, 37.4, 1915), (37.16, 36.2, 1915), label='From Erzurum'),
             mv('foot', (37.0, 39.75, 1915), (37.4, 38.5, 1915), (37.4, 37.5, 1915), (37.16, 36.2, 1915), label='From Sivas'),
             mv('foot', (29.0, 40.9, 1915), (30.5, 39.8, 1915), (32.5, 38.0, 1915), (35.3, 37.0, 1915), (36.6, 36.6, 1915), (37.16, 36.2, 1915), label='From the west')],
      sites=[site('Erzurum', 41.27, 39.9, 1915, 'One of the great Armenian centres of the east.')]),
    S(1916, '1916', 'Deir ez-Zor',
      'From Aleppo the survivors were driven east down the Euphrates to camps around Deir ez-Zor, where most of them were '
      'killed or starved in 1916.',
      moves=[mv('foot', (37.16, 36.2, 1916), (38.0, 36.0, 1916), (39.0, 35.95, 1916), (40.14, 35.33, 1916), label='To the desert')],
      sites=[site('Deir ez-Zor', 40.14, 35.33, 1916, 'The end of the deportation routes; a memorial church stood here until 2014.')]),
  ])

M('great-migration', 'The Great Migration', 'African Americans', 'emigrants', '#6e2c00', 1916, 1970,
  'Between 1916 and 1970 some six million African Americans left the rural South, its Jim Crow laws, lynchings and '
  'sharecropping, for the cities of the North and West. They rode the trains to Chicago, Detroit, New York, Philadelphia '
  'and later Los Angeles and Oakland, and changed those cities and America: the Harlem Renaissance, Chicago blues and the '
  'civil rights movement grew from it.',
  story='ev:civil-rights-movement', numbers='About 6 million people', rank=1, steps=[
    S(1916, '1916 to 1940', 'North by train',
      'The First World War stopped immigration from Europe and Northern factories needed workers. The Chicago Defender urged '
      'Southerners to come; the Illinois Central ran straight up from the Mississippi Delta.',
      moves=[mv('train', (-90.6, 33.4, 1916), (-90.18, 32.3, 1916), (-90.05, 35.15, 1917), (-88.9, 37.0, 1917), (-88.2, 40.1, 1918), (-87.63, 41.88, 1918), label='To Chicago', until=1970),
             mv('train', (-86.8, 33.5, 1917), (-86.78, 36.16, 1918), (-84.5, 39.1, 1919), (-83.05, 42.33, 1920), label='To Detroit', until=1970),
             mv('train', (-81.0, 33.9, 1917), (-78.6, 35.8, 1918), (-77.4, 37.5, 1919), (-75.16, 39.95, 1920), (-73.94, 40.81, 1920), label='To New York', until=1970)],
      sites=[site('Harlem', -73.94, 40.81, 1925, 'Capital of Black America and its Renaissance.'),
             site('Bronzeville', -87.62, 41.82, 1925, 'Chicago\'s "Black Metropolis".')]),
    S(1940, '1940 to 1970', 'To the West',
      'The Second World War brought a second, larger wave, now also to the shipyards and factories of California.',
      moves=[mv('train', (-95.37, 29.76, 1940), (-98.5, 29.4, 1941), (-106.5, 31.75, 1942), (-112.07, 33.45, 1943), (-118.24, 34.05, 1944), label='To Los Angeles', until=1970),
             mv('train', (-91.2, 30.45, 1941), (-97.3, 32.75, 1942), (-106.6, 35.1, 1943), (-114.5, 35.0, 1944), (-119.8, 36.75, 1944), (-122.27, 37.8, 1945), label='To Oakland', until=1970)]),
  ])

M('population-exchange', 'The Greek and Turkish population exchange', 'Refugees', 'refugees', '#2471a3', 1922, 1923,
  'After Turkey defeated Greece in 1922, Smyrna burned and the Greeks of Anatolia fled. The Treaty of Lausanne of 1923 then '
  'made it law: Orthodox Christians in Turkey and Muslims in Greece were exchanged, by religion, not by language. About 1.2 '
  'million went to Greece and some 400,000 to Turkey, ending 3,000 years of Greek life in Asia Minor.',
  numbers='About 1.6 million people', rank=2, steps=[
    S(1922, '1922', 'The flight from Smyrna',
      'In September 1922 the Turkish army entered Smyrna, the Greek and Armenian quarters burned, and hundreds of thousands '
      'crowded the quay waiting for ships.',
      moves=[mv('steam', (27.1, 38.45, 1922), (26.6, 38.5, 1922), (26.0, 38.3, 1922), (24.5, 37.9, 1922), (23.6, 37.9, 1922), label='To Piraeus')],
      sites=[site('Smyrna', 27.14, 38.42, 1922, 'The great fire of September 1922; today Izmir.')]),
    S(1923, '1923', 'Exchanged by treaty',
      'Muslims of Macedonia and Crete were sent to Turkey; Orthodox Christians still in Anatolia, even Turkish speakers, to '
      'Greece. Refugees made up a fifth of Greece\'s people.',
      moves=[mv('steam', (22.9, 40.55, 1923), (23.5, 40.0, 1923), (25.0, 40.0, 1923), (26.2, 40.05, 1923), (26.7, 40.4, 1923), (28.0, 40.8, 1923), (28.95, 41.0, 1923), label='Muslims to Turkey'),
             mv('foot', (35.5, 38.7, 1923), (32.0, 39.0, 1923), (29.0, 39.5, 1923), (27.1, 38.45, 1923), label='Anatolian Greeks')],
      sites=[site('Lausanne', 6.63, 46.52, 1923, 'The treaty of January 1923 orders the exchange.')]),
  ])

M('soviet-deportations', 'Stalin\'s deportations', 'Deported peoples', 'forced', '#4a235a', 1941, 1944,
  'During the Second World War Stalin deported whole nations he accused of disloyalty: the Volga Germans in 1941, the '
  'Chechens, Ingush, Karachays and Balkars, and the Crimean Tatars in 1944, loaded into cattle trucks and sent to Kazakhstan, '
  'Central Asia and Siberia. Perhaps a fifth or more died on the way and in the first years. Most could not go home until '
  'after Stalin\'s death, and the Crimean Tatars not until 1989.',
  numbers='About 3 million people', rank=2, steps=[
    S(1941, '1941', 'The Volga Germans',
      'Two weeks after Hitler invaded, the Soviet state abolished the Volga German Republic. Some 400,000 people, whose '
      'ancestors had come at Catherine the Great\'s invitation, were sent east.',
      moves=[mv('train', (46.0, 51.5, 1941), (51.4, 51.2, 1941), (57.2, 50.3, 1941), (63.6, 53.2, 1941), (71.4, 51.2, 1941), (73.1, 49.8, 1941), label='Volga Germans')]),
    S(1944, '1944', 'Chechens and Crimean Tatars',
      'On 23 February 1944 the whole Chechen and Ingush nations, nearly 500,000 people, were deported in a few days; in May '
      'some 190,000 Crimean Tatars were sent to Uzbekistan.',
      moves=[mv('train', (45.7, 43.3, 1944), (47.5, 45.0, 1944), (51.4, 47.1, 1944), (58.0, 48.0, 1944), (65.5, 44.8, 1944), (69.6, 42.3, 1944), (76.9, 43.25, 1944), label='Chechens and Ingush'),
             mv('train', (34.1, 44.95, 1944), (37.6, 47.1, 1944), (44.5, 48.7, 1944), (51.4, 47.1, 1944), (61.3, 45.5, 1944), (66.0, 43.5, 1944), (69.24, 41.3, 1944), label='Crimean Tatars')],
      sites=[site('Grozny', 45.69, 43.32, 1944, 'Operation Lentil: the Chechens are deported in a week.')]),
  ])

M('german-expulsion', 'The flight and expulsion of the Germans', 'German refugees', 'refugees', '#424949', 1944, 1950,
  'As the Red Army advanced in 1944 and 1945, millions of Germans fled west from East Prussia, Silesia and Pomerania in '
  'winter treks and on ships across the Baltic. After the war the Allies agreed at Potsdam to move the rest out of Poland, '
  'Czechoslovakia and Hungary. Some 12 million people lost their homes, the largest expulsion in European history; '
  'Poland itself was moved west, and Poles from the lost east were resettled in the former German lands.',
  numbers='About 12 to 14 million Germans', rank=1, steps=[
    S(1944, '1944 to 1945', 'The treks and the Baltic',
      'In January 1945 columns of wagons crossed the frozen Vistula Lagoon under air attack. The navy evacuated about 800,000 '
      'people by sea; the Wilhelm Gustloff was sunk with over 9,000 aboard.',
      moves=[mv('wagon', (21.5, 54.4, 1944), (20.5, 54.7, 1945), (19.6, 54.42, 1945), (18.65, 54.35, 1945), (16.0, 54.2, 1945), (13.0, 53.8, 1945), label='East Prussians'),
             mv('steam', (18.7, 54.6, 1945), (17.0, 55.0, 1945), (14.0, 54.9, 1945), (11.5, 54.5, 1945), (10.2, 54.4, 1945), label='Across the Baltic'),
             mv('wagon', (17.03, 51.1, 1945), (15.0, 51.15, 1945), (13.7, 51.05, 1945), (11.5, 50.5, 1945), label='Silesians')],
      sites=[site('Wilhelm Gustloff', 17.68, 55.07, 1945, 'Torpedoed on 30 January 1945: the deadliest sinking in history.')]),
    S(1945, '1945 to 1950', 'Expelled',
      'After Potsdam, trains carried the remaining Germans west from Silesia, Pomerania and the Sudetenland. Poles expelled from '
      'Lwow and Wilno were settled in their place; Breslau became Wroclaw.',
      moves=[mv('train', (14.0, 50.6, 1946), (12.5, 50.2, 1946), (11.0, 49.45, 1946), label='Sudeten Germans'),
             mv('train', (17.03, 51.1, 1946), (14.9, 51.15, 1946), (12.4, 51.3, 1946), (10.0, 51.5, 1947), label='Silesians'),
             mv('train', (24.03, 49.84, 1945), (22.0, 50.0, 1945), (19.94, 50.06, 1946), (17.03, 51.1, 1946), label='Poles from Lwow')],
      sites=[site('Wroclaw', 17.03, 51.11, 1946, 'German Breslau, resettled by Poles, many from Lwow.')]),
  ])

M('partition', 'The partition of India', 'Partition refugees', 'refugees', '#b03a2e', 1947, 1948,
  'When British India was divided into India and Pakistan in August 1947, some 15 million people crossed the new borders in '
  'a few months, Hindus and Sikhs east, Muslims west, in one of the largest migrations in history. Trains arrived full of '
  'the dead. Perhaps a million people were killed in the killings that went with it, above all in the Punjab.',
  story='ev:partition-of-india', numbers='About 15 million people', rank=1, steps=[
    S(1947, 'August to December 1947', 'The Punjab',
      'The Radcliffe Line cut the Punjab in two. Columns of refugees, some 400,000 strong, crossed each other on the Grand Trunk '
      'Road between Lahore and Amritsar.',
      moves=[mv('foot', (74.35, 31.55, 1947), (74.87, 31.63, 1947), (75.6, 31.3, 1947), (76.0, 30.0, 1947), (77.2, 28.6, 1947), label='Hindus and Sikhs'),
             mv('train', (77.2, 28.6, 1947), (76.0, 30.0, 1947), (75.6, 31.3, 1947), (74.87, 31.63, 1947), (74.35, 31.55, 1947), (71.5, 30.2, 1947), (67.0, 24.86, 1947), label='Muslims')],
      sites=[site('Wagah', 74.57, 31.6, 1947, 'The border crossing between Lahore and Amritsar.')]),
    S(1947, '1947 to 1948', 'Bengal and Sindh',
      'In the east, Hindus left East Bengal for Calcutta and Muslims went the other way, over several years. Muslims from '
      'northern India took trains and ships to Karachi, Pakistan\'s capital.',
      moves=[mv('train', (90.4, 23.8, 1947), (89.5, 23.2, 1947), (88.36, 22.57, 1948), label='Hindus to Calcutta'),
             mv('train', (88.36, 22.57, 1947), (89.5, 23.2, 1948), (90.4, 23.8, 1948), label='Muslims to Dhaka'),
             mv('steam', (72.6, 18.9, 1947), (71.0, 19.5, 1947), (68.5, 21.0, 1947), (66.8, 24.0, 1948), (67.0, 24.8, 1948), label='Bombay to Karachi')],
      sites=[site('Karachi', 67.0, 24.86, 1948, 'Pakistan\'s first capital, its people doubled by refugees.')]),
  ])

M('palestine-1948', 'Exodus and ingathering, 1948', 'Palestinian refugees', 'refugees', '#117864', 1947, 1951,
  'In the war of 1947 to 1949 over Palestine and the birth of Israel, some 700,000 Palestinian Arabs fled or were driven from '
  'their homes, the Nakba, "catastrophe"; they and their descendants remain refugees in Gaza, the West Bank, Jordan, Lebanon '
  'and Syria. In the same years Israel took in hundreds of thousands of Jewish survivors of the Holocaust and, by 1951, '
  'whole Jewish communities from Iraq, Yemen and other Arab countries.',
  rank=2, steps=[
    S(1947, '1947 to 1949', 'The Palestinian exodus',
      'Arabs left Haifa, Jaffa, Lydda, Ramle and hundreds of villages, to Lebanon, the West Bank, Gaza and across the Jordan.',
      moves=[mv('foot', (35.0, 32.8, 1948), (35.2, 33.1, 1948), (35.4, 33.5, 1948), label='To Lebanon'),
             mv('foot', (34.75, 32.05, 1948), (34.6, 31.7, 1948), (34.45, 31.5, 1948), label='To Gaza'),
             mv('foot', (34.9, 31.95, 1948), (35.2, 31.95, 1948), (35.6, 32.0, 1948), (35.93, 31.95, 1949), label='To the West Bank and Jordan'),
             mv('foot', (35.5, 32.9, 1948), (35.9, 33.2, 1948), (36.3, 33.5, 1949), label='To Syria')],
      sites=[site('Lydda', 34.89, 31.95, 1948, 'Tens of thousands expelled in July 1948.')]),
    S(1948, '1948 to 1951', 'Jews come to Israel',
      'Holocaust survivors came from the DP camps of Europe; Operation Magic Carpet flew 49,000 Yemeni Jews in 1949 and 1950, '
      'and Operation Ezra and Nehemiah airlifted 120,000 Iraqi Jews in 1951.',
      moves=[mv('plane', (45.0, 12.8, 1949), (42.0, 20.0, 1949), (38.0, 27.0, 1950), (34.9, 32.0, 1950), label='From Yemen'),
             mv('plane', (44.4, 33.3, 1950), (40.0, 33.0, 1950), (34.9, 32.0, 1951), label='From Iraq'),
             mv('steam', (5.3, 43.25, 1948), (7.5, 41.5, 1948), (7.6, 39.0, 1948), (9.5, 38.5, 1948), (11.5, 38.0, 1948), (12.5, 36.7, 1948), (20.0, 35.0, 1948), (28.0, 33.5, 1948), (34.9, 32.85, 1948), label='Survivors from Europe')],
      sites=[site('Haifa', 34.99, 32.82, 1948, 'Port where ships of survivors landed.')]),
  ])

M('postwar-europe', 'Coming to postwar Europe', 'Migrants to Europe', 'emigrants', '#1f618d', 1948, 1974,
  'Rebuilding after 1945, western Europe ran short of workers and looked to its empires and its neighbours. The Windrush '
  'brought Caribbean migrants to Britain in 1948, followed by people from India, Pakistan and Bangladesh; West Germany '
  'signed guest-worker deals with Italy, Turkey and Yugoslavia; France drew Algerians and Portuguese. When the oil shock of '
  '1973 ended the boom, many stayed and brought their families, and Europe\'s cities changed for good.',
  rank=2, steps=[
    S(1948, '1948 to 1962', 'The Windrush and the empire',
      'The Empire Windrush docked at Tilbury in June 1948 with 1,027 passengers, most from Jamaica. Over the next years half a '
      'million came from the Caribbean and South Asia.',
      moves=[mv('steam', (-76.8, 17.9, 1948), (-75.5, 17.6, 1948), (-74.8, 18.6, 1948), (-73.9, 20.0, 1948), (-71.5, 22.8, 1948), (-65.0, 24.0, 1948), (-45.0, 37.0, 1948), (-20.0, 46.0, 1948), (-6.0, 49.3, 1948),
                (-2.0, 50.2, 1948), (1.0, 50.9, 1948), (0.36, 51.45, 1948), label='Windrush', until=1962),
             mv('plane', (73.7, 33.1, 1955), (60.0, 38.0, 1956), (35.0, 45.0, 1957), (10.0, 50.0, 1958), (-1.75, 53.8, 1960), label='From Pakistan', until=1974)],
      sites=[site('Tilbury', 0.36, 51.46, 1948, 'Where the Empire Windrush docked on 22 June 1948.')]),
    S(1955, '1955 to 1974', 'Guest workers',
      'Trains from Istanbul, Belgrade and Naples carried millions of "Gastarbeiter" to Munich and on to the factories of '
      'Germany. After Algerian independence in 1962 nearly a million pieds-noirs and many Algerians crossed to France.',
      moves=[mv('train', (28.98, 41.0, 1961), (26.5, 42.5, 1962), (23.3, 42.7, 1962), (20.46, 44.8, 1963), (16.37, 48.2, 1963), (11.58, 48.14, 1964), label='Turks to Germany', until=1974),
             mv('steam', (3.06, 36.8, 1962), (4.0, 39.0, 1962), (5.3, 43.25, 1962), label='Algeria to Marseille', until=1974),
             mv('train', (14.25, 40.85, 1955), (12.5, 41.9, 1956), (11.25, 43.77, 1956), (11.34, 44.5, 1957), (11.1, 46.1, 1957), (11.4, 47.27, 1958), (11.58, 48.14, 1958), label='Italians to Germany', until=1973)],
      sites=[site('Munich Hauptbahnhof', 11.56, 48.14, 1964, 'Arrival hall for guest workers; Germany welcomed its millionth in 1964.')]),
  ])

M('mexico-us', 'From Mexico to the United States', 'Mexican migrants', 'emigrants', '#239b56', 1942, 2020,
  'In 1942 the United States, short of farm hands in wartime, began the Bracero Program: 4.6 million contracts for Mexican '
  'workers by 1964. When it ended, the migrants kept coming, often without papers. By 2010 some 12 million people born in '
  'Mexico lived in the United States, the largest single migration of modern times, and Spanish is the country\'s second '
  'language.',
  rank=1, steps=[
    S(1942, '1942 to 1964', 'The braceros',
      'Workers gathered at recruiting centres in Mexico and were taken north by train to the fields of California, Texas and '
      'Arizona.',
      moves=[mv('train', (-101.2, 19.7, 1942), (-102.3, 21.9, 1943), (-104.0, 24.0, 1944), (-106.1, 28.6, 1945), (-106.5, 31.75, 1946), (-111.0, 32.2, 1947),
                (-115.5, 32.7, 1948), (-119.8, 36.75, 1950), label='Braceros', until=2020)],
      sites=[site('El Paso', -106.49, 31.76, 1946, 'One of the great crossing points on the border.')]),
    S(1965, '1965 to 2020', 'North for work',
      'Millions crossed the border to work in farms, building sites and kitchens, from California to Chicago. Since 2008 more '
      'Mexicans have gone home than arrived, while Central Americans fleeing violence took the same roads.',
      moves=[mv('foot', (-99.13, 19.43, 1965), (-100.3, 25.67, 1970), (-98.5, 29.42, 1975), (-96.8, 32.78, 1980), (-94.6, 39.1, 1985), (-87.63, 41.88, 1990), label='To Texas and Chicago', until=2020),
             mv('foot', (-103.35, 20.67, 1970), (-105.0, 23.5, 1975), (-110.97, 29.07, 1980), (-114.5, 32.5, 1985), (-117.1, 32.7, 1988), (-118.24, 34.05, 1990), label='To Los Angeles', until=2020)],
      sites=[site('Los Angeles', -118.24, 34.05, 2000, 'Home to more Mexicans than any city but Mexico City and Guadalajara.')]),
  ])

M('boat-people', 'The Vietnamese boat people', 'Boat people', 'refugees', '#2e86c1', 1975, 1995,
  'After the fall of Saigon in 1975, and above all in 1978 and 1979, some 800,000 Vietnamese, many of them ethnic Chinese, '
  'fled by sea in small, crowded boats. Pirates, storms and hunger killed perhaps 200,000. Survivors reached camps in '
  'Malaysia, Hong Kong, Indonesia and the Philippines, and most were resettled in the United States, Canada, Australia and '
  'France.',
  numbers='About 800,000 reached safety', rank=2, steps=[
    S(1975, '1975 to 1979', 'Escape by sea',
      'Families paid in gold for a place on a fishing boat. Malaysia\'s island of Pulau Bidong held 40,000 people at once.',
      moves=[mv('canoe', (106.8, 10.3, 1975), (106.0, 8.5, 1976), (104.5, 6.8, 1977), (103.3, 5.7, 1978), label='To Malaysia', until=1995),
             mv('canoe', (107.0, 10.3, 1976), (108.2, 10.0, 1976), (110.0, 12.0, 1977), (112.0, 17.0, 1978), (114.2, 22.2, 1979), label='To Hong Kong', until=1995),
             mv('canoe', (107.0, 10.3, 1977), (112.0, 9.5, 1978), (117.0, 9.5, 1979), (118.5, 9.6, 1979), label='To the Philippines', until=1995)],
      sites=[site('Pulau Bidong', 103.06, 5.62, 1978, 'A refugee camp on an island off Malaysia.')]),
    S(1979, '1979 to 1995', 'New lives',
      'An international conference in 1979 agreed to resettle the refugees. Over a million Vietnamese went to new countries; '
      'the last camps closed in the 1990s.',
      moves=[mv('plane', (114.2, 22.3, 1980), (140.0, 35.0, 1981), (180.0, 40.0, 1982), (-150.0, 40.0, 1983), (-118.0, 33.8, 1984), label='To California', until=1995)],
      sites=[site('Little Saigon', -117.95, 33.75, 1984, 'Westminster, California: the largest Vietnamese community abroad.')]),
  ])

M('syrian-refugees', 'The Syrian refugees', 'Syrian refugees', 'refugees', '#7b7d7d', 2011, 2016,
  'The Syrian civil war that began in 2011 drove half of Syria\'s people from their homes. Over 6 million fled the country, '
  'mostly to Turkey, Lebanon and Jordan. In 2015 about a million people, many of them Syrians, crossed the Aegean in rubber '
  'boats and walked up the Balkans to Germany and Sweden, the largest movement of refugees into Europe since 1945.',
  numbers='Over 6 million refugees, 6 million more displaced inside Syria', rank=1, steps=[
    S(2011, '2011 to 2014', 'To the neighbours',
      'Refugees crossed into Turkey, Lebanon, where they became a quarter of the people, and Jordan, where the Zaatari camp '
      'grew into a city of 80,000.',
      moves=[mv('foot', (37.16, 36.2, 2012), (37.3, 36.7, 2012), (37.38, 37.07, 2013), label='To Turkey'),
             mv('foot', (36.3, 33.5, 2012), (35.9, 33.6, 2012), (35.5, 33.9, 2013), label='To Lebanon'),
             mv('foot', (36.3, 33.5, 2012), (36.1, 32.6, 2013), (36.33, 32.3, 2013), label='To Jordan')],
      sites=[site('Zaatari', 36.33, 32.3, 2013, 'Refugee camp in the Jordanian desert.')]),
    S(2015, '2015 to 2016', 'The Balkan route',
      'From the Turkish coast, smugglers sent people across to Lesbos in rubber boats. They walked and rode through Greece, '
      'North Macedonia, Serbia, Hungary and Austria. Germany took in nearly a million; "Wir schaffen das," said Angela Merkel.',
      moves=[mv('canoe', (26.75, 39.4, 2015), (26.55, 39.25, 2015), (26.4, 39.2, 2015), label='To Lesbos'),
             mv('foot', (26.55, 39.1, 2015), (23.6, 38.0, 2015), (22.6, 40.6, 2015), (22.5, 41.15, 2015), (21.43, 42.0, 2015), (21.9, 43.3, 2015),
                (20.46, 44.8, 2015), (19.9, 46.2, 2015), (19.04, 47.5, 2015), (16.37, 48.2, 2015), (13.0, 47.8, 2015), (11.58, 48.14, 2015),
                (13.4, 52.52, 2016), label='To Germany')],
      sites=[site('Lesbos', 26.3, 39.1, 2015, 'Half a million people landed on the island in 2015.'),
             site('Munich', 11.56, 48.14, 2015, 'Crowds welcome refugee trains in September 2015.')]),
  ])

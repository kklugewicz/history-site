from _lib import P, R, G

FRA = ('France',)
UK = ('United Kingdom of Great Britain and Ireland', 'United Kingdom')
RUS = ('Russian Empire',)
AUS = ('Austrian Empire', 'Austria Hungary', 'Austro-Hungarian Empire')
OTT = ('Ottoman Empire',)
USA = ('United States', 'United States of America')

# ---------- Napoleon and his enemies ----------
P('Napoleon', 'Emperor of the French', (1769, 1821), 1, 'war rule',
  'Corsican artillery officer who rose through the Revolution, crowned himself emperor and conquered most of Europe before Waterloo.',
  G(1793, 1793, 'Siege of Toulon', 'paris', 'toulon'),
  G(1796, 1797, 'Italian campaign', ('nice', 1796.25), ('milan', 1796.37), ((11.24, 45.35, 1796.87)), ((10.79, 45.16, 1797.1)), ((14.6, 47.4, 1797.3)),
    ('milan', 1797.6), ('paris', 1797.93)),
  G(1798, 1799, 'Egyptian campaign', ('toulon', 1798.38), ((14.51, 35.9, 1798.44)), ('alexandria', 1798.5), ((31.13, 29.98, 1798.55)), ('cairo', 1798.57),
    ((34.45, 31.5, 1799.12)), ('jaffa', 1799.18), ('acre', 1799.3), ('cairo', 1799.45), ('alexandria', 1799.62), ((6.74, 43.43, 1799.78)), ('paris', 1799.8)),
  G(1800, 1800, 'Over the Alps to Marengo', ('paris', 1800.35), ((7.17, 45.87, 1800.38)), ('milan', 1800.42), ((8.68, 44.89, 1800.45)), ('paris', 1800.55)),
  G(1805, 1805, 'Ulm and Austerlitz', ('paris', 1805.73), ((10.0, 48.4, 1805.8)), ('vienna', 1805.87), ((16.76, 49.13, 1805.92)), ('vienna', 1805.97)),
  G(1806, 1807, 'Jena, Berlin, Eylau, Friedland, Tilsit', ('paris', 1806.73), ((11.59, 50.93, 1806.79)), ('berlin', 1806.82), ('warsaw', 1806.97),
    ((20.62, 54.4, 1807.1)), ((21.0, 54.43, 1807.45)), ((21.88, 55.08, 1807.52)), ('paris', 1807.6)),
  G(1808, 1809, 'Spain, then Wagram', ('paris', 1808.83), ((-3.68, 42.34, 1808.86)), ('madrid', 1808.92), ('paris', 1809.07), ('vienna', 1809.37),
    ((16.56, 48.3, 1809.52)), ('paris', 1809.8)),
  G(1812, 1812, 'Invasion of Russia', ('paris', 1812.35), ('dresden', 1812.4), ((23.9, 54.9, 1812.48)), ((25.28, 54.68, 1812.49)), ((30.2, 55.19, 1812.56)),
    ((32.05, 54.78, 1812.63)), ((35.82, 55.53, 1812.69)), ('moscow', 1812.7), ('moscow', 1812.8), ((32.05, 54.78, 1812.86)), ((28.4, 54.3, 1812.91)),
    ((26.4, 54.48, 1812.93)), ('paris', 1812.96)),
  G(1813, 1813, 'Germany and Leipzig', ('paris', 1813.3), ('dresden', 1813.6), ('leipzig', 1813.8), ('paris', 1813.86)),
  G(1814, 1814, 'Abdication; exile on Elba', ('paris', 1814.2), ((2.7, 48.4, 1814.3)), ((10.33, 42.81, 1814.35))),
  G(1815, 1815, 'The Hundred Days and Waterloo', ((10.33, 42.81, 1815.15)), ((7.07, 43.57, 1815.17)), ((5.72, 45.19, 1815.19)), ('paris', 1815.22),
    ('waterloo', 1815.46), ('paris', 1815.48), ((-1.15, 46.0, 1815.54)), ((-5.72, -15.95, 1815.8))),
  G(1816, 1821, 'Exile on St Helena', (-5.72, -15.95)),
  R(1799, 1815, 'First Consul, then Emperor of the French', *FRA, at='paris'))
P('Joséphine de Beauharnais', 'Empress of the French', (1763, 1814), 3, 'rule',
  "Napoleon's first wife, crowned empress beside him in 1804 and divorced in 1809 for giving him no heir.",
  G(1796, 1814, 'Empress, then at Malmaison', 'paris', (2.17, 48.87)), wiki='Empress Joséphine')
P('Horatio Nelson', 'British admiral', (1758, 1805), 2, 'war',
  "Lost an eye and an arm in battle, smashed the French fleet at the Nile and died winning at Trafalgar.",
  G(1797, 1797, 'Cape St Vincent', (-9.3, 37.0)), G(1798, 1798, 'Battle of the Nile', ((-5.35, 36.14, 1798.4)), ((15.1, 37.5, 1798.5)), ((30.07, 31.32, 1798.59)), ('naples', 1798.73)),
  G(1801, 1801, 'Battle of Copenhagen', ((1.73, 52.6, 1801.2)), ((12.6, 55.69, 1801.25))),
  G(1805, 1805, 'Trafalgar', ((-1.1, 50.8, 1805.7)), ((-6.2, 36.2, 1805.8))))
P('Arthur Wellesley, 1st Duke of Wellington', 'British general and prime minister', (1769, 1852), 2, 'war rule',
  "The 'Iron Duke': drove the French out of Spain and beat Napoleon at Waterloo.",
  G(1797, 1805, 'Campaigns in India', 'calcutta', 'madras', 'seringapatam', (75.86, 20.3), 'calcutta'),
  G(1808, 1814, 'The Peninsular War', ('lisbon', 1808.6), ((-8.4, 40.2, 1809.4)), ((-4.42, 39.95, 1809.55)), ((-7.17, 38.88, 1812.25)), ((-5.66, 40.97, 1812.55)),
    ('madrid', 1812.62), ((-2.67, 42.85, 1813.47)), ((-1.48, 43.48, 1813.9)), ('toulouse', 1814.28)),
  G(1815, 1815, 'Waterloo', 'brussels', 'waterloo', 'paris'),
  R(1828, 1830, 'Prime minister', *UK, at='london'))
P('Mikhail Kutuzov', 'Russian field marshal', (1745, 1813), 3, 'war',
  'Lost at Austerlitz, then traded space for time in 1812 and drove Napoleon out of Russia.',
  G(1805, 1805, 'Austerlitz', ('st_petersburg', 1805.6), ((16.76, 49.13, 1805.92))),
  G(1812, 1813, 'Defeats Napoleon in Russia', ('st_petersburg', 1812.6), ((35.82, 55.53, 1812.69)), ('moscow', 1812.7), ((37.0, 55.0, 1812.78)),
    ((35.0, 54.6, 1812.84)), ((32.05, 54.78, 1812.88)), ((25.28, 54.68, 1812.97)), ((15.57, 51.26, 1813.3))))
P('Alexander I of Russia', 'Emperor of Russia', (1777, 1825), 2, 'rule',
  'Survived Napoleon\'s invasion of 1812 and rode into Paris as the liberator of Europe.',
  G(1814, 1815, 'Paris and the Congress of Vienna', ('paris', 1814.25), ('london', 1814.45), ('vienna', 1814.75), ('vienna', 1815.45)),
  R(1801, 1825, 'Emperor of Russia', *RUS, at='st_petersburg'))
P('Klemens von Metternich', 'Austrian statesman', (1773, 1859), 3, 'rule',
  "Built the order of Europe at the Congress of Vienna and held down revolution until 1848.",
  G(1809, 1848, 'Foreign minister and chancellor of Austria', 'vienna'), G(1848, 1851, 'Exile', 'london', 'brussels'), G(1851, 1859, 'Vienna', 'vienna'))
P('Gebhard Leberecht von Blücher', 'Prussian field marshal', (1742, 1819), 3, 'war',
  "'Marshal Forwards', who arrived at Waterloo in time to finish Napoleon.",
  G(1813, 1815, 'Leipzig, Paris and Waterloo', ((17.03, 51.11, 1813.4)), ('leipzig', 1813.8), ('paris', 1814.25), ((4.4, 50.5, 1815.44)), ('waterloo', 1815.46), ('paris', 1815.52)))
P('Charles XIV John', 'King of Sweden and Norway', (1763, 1844), 3, 'rule war',
  "Jean-Baptiste Bernadotte: a marshal of Napoleon's who was chosen heir of Sweden and turned against him.",
  G(1813, 1813, 'Battle of Leipzig', 'stockholm', 'berlin', 'leipzig'), R(1818, 1844, 'King of Sweden and Norway', 'Sweden–Norway', 'Sweden', at='stockholm'))
P('Jean-Jacques Dessalines', 'First ruler of independent Haiti', (1758, 1806), 3, 'war rule',
  "Born a slave, he finished Toussaint's revolution, beat Napoleon's army and declared Haiti free in 1804.",
  G(1802, 1803, 'War of independence', 'cap_haitien', (-72.53, 19.11), 'port_au_prince', 'cap_haitien'),
  R(1804, 1806, 'Emperor of Haiti', 'Haiti', at='port_au_prince'))

# ---------- the Americas, 1790-1850 ----------
P('Meriwether Lewis', 'American explorer', (1774, 1809), 2, 'explore',
  'With William Clark, led the first American expedition across the continent to the Pacific.',
  G(1804, 1806, 'Lewis and Clark Expedition', ((-90.2, 38.63, 1804.37)), ((-96.0, 41.3, 1804.6)), ((-101.4, 47.3, 1804.85)), ((-101.4, 47.3, 1805.27)),
    ((-111.3, 47.5, 1805.45)), ((-113.0, 44.9, 1805.62)), ((-114.3, 46.6, 1805.7)), ((-116.0, 46.4, 1805.75)), ((-123.88, 46.13, 1805.92)),
    ((-123.88, 46.13, 1806.22)), ((-116.0, 46.4, 1806.45)), ((-111.3, 47.5, 1806.55)), ((-101.4, 47.3, 1806.62)), ((-90.2, 38.63, 1806.73))))
P('Sacagawea', 'Shoshone guide', (1788, 1812), 3, 'explore',
  'Young Shoshone woman who guided and translated for Lewis and Clark, carrying her baby across the Rockies.',
  G(1805, 1806, 'With Lewis and Clark', ((-101.4, 47.3, 1805.27)), ((-111.3, 47.5, 1805.45)), ((-113.0, 44.9, 1805.62)), ((-114.3, 46.6, 1805.7)),
    ((-123.88, 46.13, 1805.92)), ((-123.88, 46.13, 1806.22)), ((-111.0, 45.7, 1806.55)), ((-101.4, 47.3, 1806.62))))
P('Alexander von Humboldt', 'German naturalist and explorer', (1769, 1859), 2, 'explore mind',
  "Climbed volcanoes and paddled the Orinoco for five years; his books founded modern geography and ecology.",
  G(1799, 1804, 'Expedition to the Americas', ((-16.25, 28.47, 1799.47)), ((-64.18, 10.46, 1799.54)), ('caracas', 1799.9), ((-67.5, 3.0, 1800.3)),
    ((-63.55, 8.13, 1800.5)), ('havana', 1801.0), ('bogota', 1801.5), ('quito', 1802.0), ((-78.82, -1.47, 1802.48)), ('lima', 1802.8), ('mexico_city', 1803.3),
    ('havana', 1804.2), ('philadelphia', 1804.4), ('washington', 1804.43), ((-0.57, 44.84, 1804.6))),
  G(1805, 1827, 'Paris', 'paris'), G(1829, 1829, 'Journey through Siberia', 'berlin', 'st_petersburg', 'moscow', 'kazan', (60.6, 56.84), 'tobolsk', (83.0, 50.0), 'astrakhan', 'moscow', 'berlin'),
  G(1830, 1859, 'Berlin', 'berlin'))
P('Miguel Hidalgo y Costilla', 'Father of Mexican independence', (1753, 1811), 2, 'war faith',
  "Village priest whose cry from the church at Dolores in 1810 began Mexico's war of independence.",
  G(1810, 1811, 'The War of Independence', ((-100.93, 21.16, 1810.71)), ((-101.26, 21.02, 1810.74)), ((-101.19, 19.7, 1810.8)), ((-99.4, 19.33, 1810.83)),
    ((-103.35, 20.67, 1810.9)), ((-103.0, 20.5, 1811.04)), ((-101.0, 25.42, 1811.2)), ((-106.07, 28.63, 1811.55))))
P('José María Morelos', 'Mexican independence leader', (1765, 1815), 3, 'war faith',
  "Priest and general who carried on Hidalgo's war and declared Mexico independent in 1813.",
  G(1810, 1815, 'War of Independence in the south', (-99.88, 16.85), (-98.95, 18.81), (-96.73, 17.06), (-99.5, 17.55), (-101.19, 19.7), (-99.13, 19.43)))
P('Simón Bolívar', 'The Liberator of South America', (1783, 1830), 1, 'war rule',
  'Freed Venezuela, Colombia, Ecuador, Peru and Bolivia from Spain; Bolivia is named after him.',
  G(1813, 1814, 'The Admirable Campaign', ((-75.5, 10.4, 1813.0)), ((-72.5, 7.9, 1813.2)), ((-71.15, 8.6, 1813.4)), ((-69.75, 9.57, 1813.55)), ('caracas', 1813.6),
    ((-67.5, 10.25, 1814.5)), ((-75.5, 10.4, 1814.9))),
  G(1815, 1818, 'Exile and return', ((-76.8, 18.0, 1815.4)), ('port_au_prince', 1816.0), ((-63.8, 11.0, 1816.4)), ((-63.55, 8.13, 1817.6)), ((-63.55, 8.13, 1818.9))),
  G(1819, 1822, 'Boyacá, Carabobo and Pichincha', ((-63.55, 8.13, 1819.1)), ((-69.0, 7.1, 1819.4)), ((-72.6, 5.9, 1819.5)), ((-73.4, 5.45, 1819.6)),
    ('bogota', 1819.62), ((-63.55, 8.13, 1820.0)), ((-68.2, 9.9, 1821.47)), ('caracas', 1821.5), ('bogota', 1821.8), ((-77.3, 1.2, 1822.3)), ('quito', 1822.45),
    ((-79.9, -2.2, 1822.55))),
  G(1823, 1825, 'Liberation of Peru and Bolivia', ((-79.9, -2.2, 1823.4)), ('lima', 1823.7), ((-78.5, -8.1, 1824.2)), ((-76.1, -11.0, 1824.6)), ('lima', 1824.95),
    ((-65.75, -19.58, 1825.75)), ((-65.26, -19.05, 1825.8))),
  G(1826, 1830, 'President of Gran Colombia', 'lima', 'bogota', ((-74.2, 11.24, 1830.9))))
P('José de San Martín', 'Liberator of Argentina, Chile and Peru', (1778, 1850), 2, 'war',
  'Led an army over the Andes to free Chile, then sailed north to free Peru.',
  G(1812, 1816, 'War of independence in Argentina', 'buenos_aires', (-60.7, -32.75), (-65.2, -26.8), (-68.84, -32.89)),
  G(1817, 1818, 'Crossing of the Andes', ((-68.84, -32.89, 1817.05)), ((-70.0, -32.8, 1817.08)), ((-70.7, -33.05, 1817.11)), ('santiago', 1817.15),
    ((-70.75, -33.51, 1818.27)), ('santiago', 1818.3)),
  G(1820, 1822, 'Liberation of Peru', ('valparaiso', 1820.7), ((-76.2, -13.7, 1820.7)), ('lima', 1821.5), ((-79.9, -2.2, 1822.55)), ('lima', 1822.7)),
  G(1824, 1850, 'Exile in Europe', 'brussels', 'paris', (1.61, 50.73)))
P('Antonio José de Sucre', 'South American independence leader', (1795, 1830), 3, 'war',
  "Bolívar's finest general: won at Pichincha and Ayacucho, ending Spanish rule in South America.",
  G(1821, 1825, 'Pichincha and Ayacucho', ((-79.9, -2.2, 1821.4)), ('quito', 1822.4), ('lima', 1823.5), ((-74.22, -13.16, 1824.93)), ('cuzco', 1825.1), ((-65.26, -19.05, 1825.6))))
P('Bernardo O\'Higgins', 'Liberator of Chile', (1778, 1842), 3, 'war rule',
  "Son of an Irish-born viceroy who fought beside San Martín and became Chile's first ruler.",
  G(1817, 1823, 'Supreme Director of Chile', 'santiago'))
P('Pedro I of Brazil', 'First emperor of Brazil', (1798, 1834), 3, 'rule',
  "Portuguese prince who declared Brazil independent in 1822 with the cry 'Independence or death!'",
  G(1822, 1831, 'Emperor of Brazil', (-46.63, -23.55), 'rio'), G(1832, 1834, 'Civil war in Portugal', (-8.61, 41.15), 'lisbon'))
P('Andrew Jackson', 'Seventh President of the United States', (1767, 1845), 2, 'war rule',
  'Won the Battle of New Orleans, became a populist president, and forced the Cherokee west on the Trail of Tears.',
  G(1814, 1815, 'Horseshoe Bend and New Orleans', (-86.8, 36.16), (-85.73, 32.98), (-88.04, 30.69), 'new_orleans'),
  R(1829, 1837, 'President of the United States', *USA, at='washington'))
P('Tecumseh', 'Shawnee leader', (1768, 1813), 2, 'war',
  'Built an alliance of nations to stop American expansion and died fighting beside the British in 1813.',
  G(1808, 1813, "Tecumseh's Confederacy", (-86.9, 40.42), (-86.0, 34.0), (-86.9, 40.42), (-83.05, 42.33), (-81.85, 42.55)))
P('Antonio López de Santa Anna', 'Mexican general and president', (1794, 1876), 3, 'war rule',
  "President of Mexico eleven times; took the Alamo, then lost Texas, and later half of Mexico, to the United States.",
  G(1833, 1855, 'President of Mexico, on and off', 'mexico_city'),
  G(1836, 1836, 'The Alamo and San Jacinto', ('mexico_city', 1836.0), ((-98.49, 29.43, 1836.18)), ((-95.08, 29.75, 1836.3))),
  G(1847, 1847, 'War with the United States', ((-101.0, 25.42, 1847.15)), ('mexico_city', 1847.4), ((-97.0, 19.5, 1847.3)), ('mexico_city', 1847.7)))
P('Sequoyah', 'Cherokee scholar', (1770, 1843), 3, 'mind',
  "Invented a writing system for the Cherokee language, used within a few years by most of the nation.",
  G(1809, 1824, 'Creates the Cherokee syllabary', (-84.4, 35.6)), G(1829, 1843, 'Indian Territory', (-94.8, 35.5)))

# ---------- Europe, 1800-1850 ----------
P('Ludwig van Beethoven', 'German composer', (1770, 1827), 1, 'art',
  'Kept composing as he went deaf; his nine symphonies bridge the classical and romantic ages.',
  G(1770, 1791, 'Bonn', (7.1, 50.73)), G(1792, 1827, 'Vienna', 'vienna'))
P('Johann Wolfgang von Goethe', 'German writer', (1749, 1832), 2, 'art mind',
  "Germany's greatest writer: Faust, The Sorrows of Young Werther, and science too.",
  G(1775, 1785, 'Weimar', 'weimar'), G(1786, 1788, 'Italian journey', 'weimar', 'venice', 'rome', 'naples', (13.36, 38.12), 'rome', 'weimar'),
  G(1789, 1832, 'Weimar', 'weimar'))
P('Mary Wollstonecraft', 'English writer', (1759, 1797), 3, 'mind reform',
  'Wrote A Vindication of the Rights of Woman (1792), a founding work of feminism.',
  G(1792, 1797, 'Paris and London', 'paris', 'london'))
P('Louis Philippe I', 'King of the French', (1773, 1850), 3, 'rule',
  "The 'citizen king' put on the throne by the revolution of 1830 and toppled by the one of 1848.",
  R(1830, 1848, 'King of the French', *FRA, at='paris'))
P('Muhammad Ali of Egypt', 'Ruler of Egypt', (1769, 1849), 2, 'rule reform',
  "Albanian officer who seized Egypt, massacred the Mamluks and built a modern army, factories and schools.",
  R(1805, 1848, 'Wali of Egypt', 'Egypt', at='cairo'))
P('Mahmud II', 'Ottoman sultan', (1785, 1839), 3, 'rule reform',
  'Destroyed the Janissaries in 1826 and began the reform of the Ottoman Empire.',
  R(1808, 1839, 'Ottoman sultan', *OTT, at='constantinople'))
P('Usman dan Fodio', 'Founder of the Sokoto Caliphate', (1754, 1817), 3, 'faith rule',
  'Fulani scholar whose holy war united the Hausa states into the largest state in 19th-century Africa.',
  G(1804, 1817, 'Founder of the Sokoto Caliphate', (5.98, 13.4), (5.23, 13.06)))
P('Shaka', 'King of the Zulu', (1787, 1828), 2, 'war rule',
  'Turned the Zulu into a great military kingdom with new tactics and the short stabbing spear.',
  R(1816, 1828, 'King of the Zulu', 'Zulu', at=(31.45, -28.8)), wiki='Shaka')
P('Ranjit Singh', 'Maharaja of the Sikh Empire', (1780, 1839), 3, 'rule war',
  "The 'Lion of Punjab', who built a strong Sikh state that kept the British out for his lifetime.",
  R(1801, 1839, 'Maharaja of the Sikh Empire', 'Sikhs', at='lahore'))
P('Ram Mohan Roy', 'Indian reformer', (1772, 1833), 3, 'reform faith',
  "Father of the Bengal Renaissance who campaigned against widow-burning and for modern schools.",
  G(1814, 1830, 'Reformer in Calcutta', 'calcutta'), G(1831, 1833, 'England', 'london', (-2.6, 51.45)))
P('Gia Long', 'Emperor of Vietnam', (1762, 1820), 3, 'rule war',
  'Last survivor of the Nguyễn lords, he beat the Tây Sơn and united Vietnam for the first time.',
  R(1802, 1820, 'Emperor of Vietnam', 'Đại Việt', 'Annam', at='hue'))
P('Kamehameha I', 'King of Hawaii', (1758, 1819), 2, 'rule war',
  'United the Hawaiian Islands by conquest and kept them independent of the European powers.',
  G(1795, 1819, 'Unifier of Hawaii', (-155.93, 19.64), (-157.86, 21.31), (-155.93, 19.64)))
P('Lin Zexu', 'Chinese official', (1785, 1850), 3, 'rule reform',
  "Burned the British opium at Canton in 1839, setting off the First Opium War.",
  G(1839, 1840, 'Destroys the opium at Canton', 'beijing', 'canton'), G(1842, 1845, 'Exile in Xinjiang', (81.3, 43.9)))
P('Shamil', 'Imam of Dagestan', (1797, 1871), 3, 'war faith',
  'Led the peoples of the Caucasus against Russia for 25 years from mountain strongholds.',
  G(1834, 1859, 'War in the Caucasus', (46.6, 42.6), (46.23, 42.95), (45.9, 43.0), (46.96, 42.39)))
P('Nicholas I of Russia', 'Emperor of Russia', (1796, 1855), 3, 'rule',
  "Iron-fisted tsar who crushed revolts in Poland and Hungary and started the Crimean War.",
  R(1825, 1855, 'Emperor of Russia', *RUS, at='st_petersburg'))
P('Lajos Kossuth', 'Leader of the Hungarian revolution', (1802, 1894), 3, 'rule reform',
  'Led Hungary\'s revolution of 1848 against the Habsburgs until Russian troops crushed it.',
  G(1848, 1849, 'Hungarian revolution', 'budapest', (21.63, 47.53), (21.3, 46.18)), G(1851, 1894, 'Exile in London and Turin', 'london', 'turin'))
P('Karl Marx', 'German philosopher and revolutionary', (1818, 1883), 1, 'mind reform',
  'Wrote The Communist Manifesto and Das Kapital, the ideas behind the communist revolutions of the 20th century.',
  G(1843, 1845, 'Paris', 'paris'), G(1845, 1847, 'Brussels', 'brussels'), G(1848, 1849, 'The Communist Manifesto and the 1848 revolution', 'brussels', 'paris', (6.96, 50.94)),
  G(1849, 1883, 'London: Das Kapital', 'london'))
P('Friedrich Engels', 'German philosopher', (1820, 1895), 3, 'mind reform',
  "Cotton mill heir who saw the slums of Manchester and wrote the Communist Manifesto with Marx.",
  G(1842, 1844, 'Manchester', 'manchester'), G(1850, 1869, 'Manchester', 'manchester'), G(1870, 1895, 'London', 'london'))
P('George Stephenson', 'English railway engineer', (1781, 1848), 3, 'mind',
  "Built the first public steam railways, the 'father of railways'.",
  G(1825, 1830, 'Stockton and Darlington, then Liverpool and Manchester', (-1.32, 54.57), (-1.55, 54.52), 'liverpool', 'manchester'))
P('Michael Faraday', 'English scientist', (1791, 1867), 3, 'mind',
  'Bookbinder\'s apprentice who discovered electromagnetic induction, the basis of every electric generator.',
  G(1813, 1867, 'Royal Institution in London', 'london'))
P('Charles Darwin', 'English naturalist', (1809, 1882), 1, 'mind explore',
  'Sailed round the world on the Beagle and worked out the theory of evolution by natural selection.',
  G(1831, 1836, 'Voyage of the Beagle', ('plymouth', 1831.99), ((-23.5, 14.9, 1832.05)), ((-38.5, -12.97, 1832.15)), ('rio', 1832.3), ('montevideo', 1832.6),
    ((-68.3, -54.8, 1832.95)), ((-59.0, -51.7, 1833.2)), ((-62.3, -38.7, 1833.6)), ('buenos_aires', 1833.75), ((-68.3, -54.8, 1834.15)), ('valparaiso', 1834.55),
    ((-73.8, -42.5, 1834.9)), ((-73.05, -36.82, 1835.15)), ('lima', 1835.55), ((-90.5, -0.8, 1835.75)), ('tahiti', 1835.87), ((174.0, -35.3, 1835.97)),
    ((151.2, -33.87, 1836.03)), ((147.3, -42.9, 1836.1)), ((117.9, -35.0, 1836.2)), ((96.9, -12.1, 1836.28)), ((57.5, -20.2, 1836.35)), ('cape_town', 1836.45),
    ((-5.72, -15.95, 1836.53)), ((-14.4, -7.9, 1836.56)), ((-38.5, -12.97, 1836.6)), ((-25.7, 37.75, 1836.72)), ((-5.07, 50.15, 1836.75))),
  G(1842, 1882, 'Down House: On the Origin of Species', (0.05, 51.33)))
P('Queen Victoria', 'Queen of the United Kingdom', (1819, 1901), 1, 'rule',
  "Reigned 63 years over the largest empire in history, which gave its name to the Victorian age.",
  R(1837, 1901, 'Queen of the United Kingdom and Empress of India', *UK, at='london'))
P('Pope Pius IX', 'Pope', (1792, 1878), 3, 'faith rule',
  'The longest-reigning pope, who lost the Papal States to united Italy and declared popes infallible.',
  R(1846, 1870, 'Pope and ruler of the Papal States', 'Papal States', at='rome'), G(1871, 1878, 'Prisoner in the Vatican', 'rome'))
P('Napoleon III', 'Emperor of the French', (1808, 1873), 2, 'rule',
  "Napoleon's nephew, elected president in 1848, made himself emperor, rebuilt Paris and was captured at Sedan.",
  R(1848, 1869, 'President, then Emperor of the French', *FRA, at='paris'), G(1870, 1870, 'Captured at Sedan', 'paris', (6.18, 49.12), (4.94, 49.7)),
  G(1871, 1873, 'Exile in England', (0.07, 51.42)))
P('Franz Joseph I', 'Emperor of Austria-Hungary', (1830, 1916), 2, 'rule',
  "Ruled for 68 years, from the revolutions of 1848 to the middle of the First World War.",
  R(1848, 1916, 'Emperor of Austria, King of Hungary', *AUS, at='vienna'), wiki='Franz Joseph I of Austria')

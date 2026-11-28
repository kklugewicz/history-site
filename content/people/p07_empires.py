from _lib import P, R, G

FRA = ('France',)
UK = ('United Kingdom of Great Britain and Ireland', 'United Kingdom')
RUS = ('Russian Empire',)
OTT = ('Ottoman Empire',)
USA = ('United States', 'United States of America')
GER = ('Prussia', 'North German Confederation', 'Germany', 'German Empire')
JAPAN = ('Japan', 'Imperial Japan', 'Empire of Japan')
QING = ('Manchu Empire', 'Qing Empire')

# ---------- the United States, 1840-1910 ----------
P('Frederick Douglass', 'American abolitionist', (1818, 1895), 2, 'reform',
  'Escaped slavery, taught himself to write and became the most powerful voice against it in America.',
  G(1838, 1847, 'Escape and the abolition movement', (-76.61, 39.29), 'new_york', (-70.93, 41.64), 'boston'), G(1845, 1847, 'Speaking tour of Britain', 'london', 'dublin', 'edinburgh'),
  G(1847, 1872, 'The North Star at Rochester', (-77.61, 43.16)), G(1872, 1895, 'Washington', 'washington'))
P('Harriet Tubman', 'American abolitionist', (1822, 1913), 2, 'reform',
  'Escaped slavery and went back again and again to lead about seventy others to freedom on the Underground Railroad.',
  G(1849, 1860, 'The Underground Railroad', (-76.08, 38.55), 'philadelphia', (-76.08, 38.55), 'philadelphia', (-79.24, 43.16)),
  G(1862, 1865, 'Union scout and spy in the Civil War', (-80.7, 32.4)), G(1866, 1913, 'Auburn, New York', (-76.56, 42.93)))
P('John Brown', 'American abolitionist', (1800, 1859), 3, 'reform war',
  'Fought slavery with guns in Kansas and was hanged after his raid on Harpers Ferry.',
  G(1855, 1859, 'Bleeding Kansas and Harpers Ferry', (-95.2, 38.4), (-77.74, 39.32)))
P('Brigham Young', 'Mormon leader', (1801, 1877), 3, 'faith explore',
  'Led the Mormons on a great trek across the plains to found Salt Lake City.',
  G(1846, 1847, 'The trek to Utah', ((-91.38, 40.55, 1846.1)), ((-95.93, 41.26, 1846.8)), ((-95.93, 41.26, 1847.3)), ((-104.6, 42.2, 1847.45)), ((-111.89, 40.76, 1847.56))),
  G(1848, 1877, 'Salt Lake City', (-111.89, 40.76)))
P('Abraham Lincoln', 'Sixteenth President of the United States', (1809, 1865), 1, 'rule reform',
  'Led the Union through the Civil War, freed the slaves with the Emancipation Proclamation and was murdered at its end.',
  G(1837, 1860, 'Lawyer in Springfield', (-89.65, 39.8)), R(1861, 1865, 'President of the United States', *USA, at='washington'))
P('Jefferson Davis', 'President of the Confederacy', (1808, 1889), 3, 'rule',
  'President of the slave states that broke away in 1861.',
  G(1861, 1865, 'President of the Confederate States', (-86.3, 32.38), 'richmond'))
P('Ulysses S. Grant', 'Union general and president', (1822, 1885), 2, 'war rule',
  'Took Vicksburg, wore down Lee in Virginia and accepted his surrender at Appomattox; later president.',
  G(1861, 1863, 'War in the West', ((-89.18, 37.0, 1861.7)), ((-87.86, 36.5, 1862.12)), ((-88.32, 35.15, 1862.27)), ((-90.88, 32.35, 1863.5)), ((-85.31, 35.05, 1863.9))),
  G(1864, 1865, 'Overland Campaign and Appomattox', ((-77.73, 38.3, 1864.35)), ((-77.6, 38.2, 1864.4)), ((-77.4, 37.23, 1864.5)), ((-77.4, 37.23, 1865.25)), ((-78.8, 37.38, 1865.27))),
  R(1869, 1877, 'President of the United States', *USA, at='washington'))
P('Robert E. Lee', 'Confederate general', (1807, 1870), 2, 'war',
  'Brilliant commander of the Confederate army in Virginia, beaten at Gettysburg and forced to surrender at Appomattox.',
  G(1862, 1865, 'Army of Northern Virginia', ((-77.43, 37.54, 1862.42)), ((-77.74, 39.47, 1862.71)), ((-77.46, 38.3, 1862.95)), ((-77.65, 38.3, 1863.33)),
    ((-77.23, 39.82, 1863.5)), ((-77.73, 38.3, 1864.35)), ((-77.4, 37.23, 1864.6)), ((-77.4, 37.23, 1865.25)), ((-78.8, 37.38, 1865.27))))
P('William Tecumseh Sherman', 'Union general', (1820, 1891), 3, 'war',
  "Burned a path from Atlanta to the sea to break the South's will: 'War is hell.'",
  G(1864, 1865, 'Atlanta and the March to the Sea', ((-85.31, 35.05, 1864.35)), ((-84.39, 33.75, 1864.67)), ((-83.6, 33.0, 1864.88)), ((-81.09, 32.08, 1864.97)),
    ((-81.03, 34.0, 1865.13)), ((-78.64, 35.78, 1865.3))))
P('Sitting Bull', 'Hunkpapa Lakota leader', (1831, 1890), 2, 'war faith',
  'Holy man whose vision foretold the destruction of Custer at the Little Bighorn in 1876.',
  G(1876, 1876, 'The Little Bighorn', (-106.6, 45.2), (-107.43, 45.57), (-106.0, 46.5)), G(1877, 1881, 'Exile in Canada', (-106.6, 49.5)),
  G(1885, 1885, "Buffalo Bill's Wild West", 'philadelphia', 'boston', 'montreal'), G(1886, 1890, 'Standing Rock', (-100.67, 45.73)))
P('Crazy Horse', 'Oglala Lakota war leader', (1840, 1877), 3, 'war',
  'Led the charge that wiped out Custer at the Little Bighorn.',
  G(1876, 1877, 'The Great Sioux War', (-106.9, 45.0), (-107.43, 45.57), (-106.0, 44.8), (-103.45, 42.67)))
P('George Armstrong Custer', 'US cavalry officer', (1839, 1876), 3, 'war',
  "Killed with all his men at the Little Bighorn: 'Custer's Last Stand'.",
  G(1876, 1876, 'March to the Little Bighorn', ((-100.83, 46.77, 1876.38)), ((-105.85, 46.4, 1876.45)), ((-106.6, 45.6, 1876.47)), ((-107.43, 45.57, 1876.49))))
P('Geronimo', 'Apache leader', (1829, 1909), 3, 'war',
  "Chiricahua Apache who fought Mexico and the United States until his surrender in 1886.",
  G(1876, 1886, 'Apache resistance', (-109.35, 31.95), (-108.6, 30.0), (-109.35, 31.95), (-109.05, 31.55)), G(1894, 1909, 'Prisoner at Fort Sill', (-98.4, 34.65)))
P('Thomas Edison', 'American inventor', (1847, 1931), 2, 'mind',
  'Gave the world the phonograph, the practical light bulb and the first power stations.',
  G(1876, 1886, 'Menlo Park', (-74.34, 40.57)), G(1887, 1931, 'West Orange', (-74.24, 40.79)))
P('Alexander Graham Bell', 'Inventor of the telephone', (1847, 1922), 2, 'mind',
  'Scottish-born teacher of the deaf who patented the telephone in 1876.',
  G(1847, 1869, 'Youth in Edinburgh, then London', 'edinburgh', 'london'), G(1870, 1870, 'Brantford, Canada', (-80.26, 43.14)),
  G(1871, 1922, 'Boston, Washington and Nova Scotia', 'boston', 'washington', (-60.58, 46.1)))
P('Nikola Tesla', 'Serbian-American inventor', (1856, 1943), 2, 'mind',
  'Invented the alternating-current motor that powers the world, and dreamed of wireless power.',
  G(1856, 1874, 'Youth in Lika, on the Croatian Military Frontier', (15.32, 44.57)), G(1875, 1880, 'Studies at Graz and Prague', (15.44, 47.07), 'prague'),
  G(1881, 1883, 'Budapest and Paris', 'budapest', 'paris'), G(1884, 1943, 'New York', 'new_york', (-104.82, 38.83), 'new_york'))

# ---------- Europe, 1850-1914 ----------
P('Florence Nightingale', 'Founder of modern nursing', (1820, 1910), 2, 'reform mind',
  "The 'Lady with the Lamp' who cut deaths in the army hospitals of the Crimean War and founded modern nursing.",
  G(1854, 1856, 'Scutari in the Crimean War', 'london', (29.02, 41.0), (33.52, 44.6), (29.02, 41.0)), G(1856, 1910, 'London', 'london'))
P('Leo Tolstoy', 'Russian novelist', (1828, 1910), 2, 'art faith',
  'Wrote War and Peace and Anna Karenina, then preached a radical Christianity of peace.',
  G(1854, 1855, 'Siege of Sevastopol', (33.52, 44.6)), G(1856, 1910, 'Yasnaya Polyana', (37.53, 54.08)))
P('Fyodor Dostoevsky', 'Russian novelist', (1821, 1881), 3, 'art',
  'Faced a mock execution and Siberian prison, then wrote Crime and Punishment and The Brothers Karamazov.',
  G(1850, 1854, 'Prison camp at Omsk', (73.37, 54.98)), G(1859, 1881, 'St Petersburg', 'st_petersburg'))
P('Alexander II of Russia', 'Emperor of Russia', (1818, 1881), 2, 'rule reform',
  "The 'Tsar Liberator' who freed 23 million serfs in 1861 and was blown up by revolutionaries.",
  R(1855, 1881, 'Emperor of Russia', *RUS, at='st_petersburg'))
P('Giuseppe Garibaldi', 'Hero of Italian unification', (1807, 1882), 2, 'war',
  'Led his red-shirted Thousand to conquer Sicily and Naples and hand them to a united Italy.',
  G(1836, 1848, 'Wars in South America', 'rio', (-51.2, -30.03), 'montevideo'), G(1849, 1849, 'Defence of the Roman Republic', 'rome', (12.25, 44.42)),
  G(1860, 1860, 'Expedition of the Thousand', ((8.93, 44.41, 1860.35)), ((12.44, 37.8, 1860.37)), ((13.36, 38.12, 1860.4)), ((15.65, 38.11, 1860.63)),
    ('naples', 1860.68), ((14.33, 41.07, 1860.77))),
  G(1861, 1882, 'Caprera', (9.46, 41.2)))
P('Camillo Benso, Count of Cavour', 'Prime minister of Piedmont-Sardinia', (1810, 1861), 3, 'rule',
  'The cunning statesman who used France to drive Austria out of northern Italy and unite the country.',
  R(1852, 1861, 'Prime minister of Sardinia, then Italy', 'Kingdom of Sardinia', 'Italy', at='turin'))
P('Giuseppe Mazzini', 'Italian revolutionary', (1805, 1872), 3, 'reform',
  'Spent his life plotting for a free, united Italy, mostly from exile in London.',
  G(1831, 1848, 'Exile: Marseille, Switzerland, London', 'marseille', 'geneva', 'london'), G(1849, 1849, 'Roman Republic', 'rome'),
  G(1850, 1872, 'London', 'london', 'pisa'))
P('Victor Emmanuel II', 'First king of united Italy', (1820, 1878), 3, 'rule',
  'King of Sardinia who became the first king of Italy in 1861.',
  R(1849, 1878, 'King of Sardinia, then of Italy', 'Kingdom of Sardinia', 'Italy', at='turin'))
P('Otto von Bismarck', 'Chancellor of Germany', (1815, 1898), 1, 'rule war',
  "The 'Iron Chancellor' who united Germany by three short wars and then kept Europe at peace.",
  R(1862, 1890, 'Minister-president of Prussia, chancellor of Germany', *GER, at='berlin'))
P('Wilhelm I', 'German emperor', (1797, 1888), 3, 'rule',
  'King of Prussia proclaimed the first emperor of Germany at Versailles in 1871.',
  R(1861, 1888, 'King of Prussia, German emperor', *GER, at='berlin'), wiki='Wilhelm I, German Emperor')
P('Benjamin Disraeli', 'British prime minister', (1804, 1881), 3, 'rule',
  "Novelist turned Conservative prime minister who bought the Suez Canal shares and made Victoria Empress of India.",
  G(1868, 1880, 'Prime minister', 'london'))
P('William Ewart Gladstone', 'British prime minister', (1809, 1898), 3, 'rule reform',
  'Liberal prime minister four times, who fought for Irish home rule.',
  G(1868, 1894, 'Prime minister', 'london'))
P('Charles Dickens', 'English novelist', (1812, 1870), 2, 'art reform',
  'Wrote Oliver Twist and A Christmas Carol, showing Victorian Britain its poor.',
  G(1833, 1870, 'London', 'london'))
P('Victor Hugo', 'French writer', (1802, 1885), 2, 'art',
  'Wrote Les Misérables and The Hunchback of Notre-Dame, and spent 19 years in exile against Napoleon III.',
  G(1830, 1851, 'Paris', 'paris'), G(1855, 1870, 'Exile on Guernsey', (-2.54, 49.45)), G(1870, 1885, 'Paris', 'paris'))
P('Louis Pasteur', 'French scientist', (1822, 1895), 2, 'mind',
  'Proved that germs cause disease, invented pasteurisation and made vaccines against rabies and anthrax.',
  G(1849, 1856, 'Strasbourg and Lille', (7.75, 48.58), (3.06, 50.63)), G(1857, 1895, 'Paris', 'paris'))
P('Gregor Mendel', 'Austrian monk and scientist', (1822, 1884), 2, 'mind',
  'Bred pea plants in his monastery garden and discovered the laws of heredity.',
  G(1856, 1884, 'Abbey at Brno', (16.61, 49.2)))
P('Dmitri Mendeleev', 'Russian chemist', (1834, 1907), 2, 'mind',
  'Arranged the elements in the periodic table and predicted ones not yet found.',
  G(1869, 1907, 'St Petersburg', 'st_petersburg'))
P('Richard Wagner', 'German composer', (1813, 1883), 2, 'art',
  'Wrote the four operas of The Ring of the Nibelung and built a theatre at Bayreuth to stage them.',
  G(1849, 1858, 'Exile in Zurich', 'zurich'), G(1864, 1872, 'Munich and Lucerne', 'munich', (8.31, 47.05)), G(1872, 1883, 'Bayreuth', (11.58, 49.94)))
P('Vincent van Gogh', 'Dutch painter', (1853, 1890), 2, 'art',
  'Sold almost nothing in his lifetime; his Sunflowers and Starry Night are now among the most loved paintings in the world.',
  G(1880, 1885, 'Belgium and the Netherlands', 'brussels', (5.41, 51.44)), G(1886, 1887, 'Paris', 'paris'), G(1888, 1889, 'Arles', (4.63, 43.68)),
  G(1889, 1890, 'Saint-Rémy and Auvers', (4.83, 43.79), (2.17, 49.07)))
P('Claude Monet', 'French painter', (1840, 1926), 2, 'art',
  "His Impression, Sunrise gave Impressionism its name; he spent his last decades painting his water lilies.",
  G(1871, 1882, 'Argenteuil and Paris', (2.25, 48.95), 'paris'), G(1883, 1926, 'Giverny', (1.53, 49.08)))
P('Ferdinand de Lesseps', 'French diplomat and developer', (1805, 1894), 3, 'mind',
  'Built the Suez Canal, opened in 1869, and failed at Panama.',
  G(1859, 1869, 'Builds the Suez Canal', (32.3, 31.26), (32.27, 30.6), (32.55, 29.97)), G(1881, 1888, 'The failed Panama Canal', (-79.9, 9.35), 'panama'))
P('Leopold II of Belgium', 'King of the Belgians', (1835, 1909), 2, 'rule',
  'Ran the Congo Free State as his private colony, where forced labour for rubber killed millions.',
  R(1865, 1909, 'King of the Belgians and owner of the Congo', 'Belgium', at='brussels'))
P('Abdul Hamid II', 'Ottoman sultan', (1842, 1918), 3, 'rule',
  'Ruled the shrinking empire as an autocrat for 33 years until the Young Turks deposed him.',
  R(1876, 1909, 'Ottoman sultan', *OTT, at='constantinople'))

# ---------- Africa ----------
P('David Livingstone', 'Scottish missionary and explorer', (1813, 1873), 2, 'explore faith',
  "Crossed Africa coast to coast, named Victoria Falls and campaigned against the slave trade: 'Dr Livingstone, I presume?'",
  G(1849, 1856, 'Across Africa', ((23.43, -27.46, 1849.5)), ((25.86, -17.92, 1851.6)), ((13.23, -8.84, 1854.4)), ((25.86, -17.92, 1855.88)), ((33.6, -16.15, 1856.2)),
    ((36.89, -17.88, 1856.4))),
  G(1858, 1864, 'Zambezi expedition', (36.89, -17.88), (33.6, -16.15), (35.25, -15.8), (34.7, -12.0), (36.89, -17.88)),
  G(1866, 1873, 'Search for the source of the Nile', ((40.13, -10.27, 1866.25)), ((35.0, -14.0, 1866.7)), ((29.65, -4.88, 1869.2)), ((26.2, -3.98, 1871.5)),
    ((29.65, -4.88, 1871.85)), ((32.82, -5.02, 1872.2)), ((30.4, -12.3, 1873.33))))
P('Henry Morton Stanley', 'Welsh-American explorer', (1841, 1904), 3, 'explore',
  'Found Livingstone at Ujiji in 1871 and followed the Congo River to the sea; later carved out the Congo for Leopold II.',
  G(1871, 1872, 'The search for Livingstone', ((39.2, -6.16, 1871.1)), ((38.9, -6.43, 1871.2)), ((32.82, -5.02, 1871.5)), ((29.65, -4.88, 1871.85)), ((39.2, -6.16, 1872.4))),
  G(1874, 1877, 'Down the Congo', ((39.2, -6.16, 1874.9)), ((32.9, -2.5, 1875.3)), ((29.65, -4.88, 1876.4)), ((26.2, -3.98, 1876.8)), ((25.2, 0.52, 1877.05)),
    ((15.3, -4.3, 1877.25)), ((13.05, -5.8, 1877.6))))
P('Abdelkader', 'Algerian resistance leader', (1808, 1883), 3, 'war faith',
  'Sufi scholar who fought the French conquest of Algeria for 15 years, then saved thousands of Christians in Damascus.',
  G(1832, 1847, 'War against the French', (0.14, 35.4), (-0.64, 35.7), (1.32, 35.37), (-1.3, 34.9), (-2.0, 34.7)), G(1848, 1852, 'Prisoner in France', (0.98, 47.41)),
  G(1855, 1883, 'Damascus', 'damascus'), wiki='Emir Abdelkader')
P('Tewodros II', 'Emperor of Ethiopia', (1818, 1868), 3, 'rule',
  "Reunited Ethiopia and shot himself rather than surrender to a British army at Magdala.",
  R(1855, 1868, 'Emperor of Ethiopia', 'Ethiopia', at=(39.36, 11.13)))
P('Menelik II', 'Emperor of Ethiopia', (1844, 1913), 2, 'rule war',
  "Beat Italy at Adwa in 1896, keeping Ethiopia free while the rest of Africa was colonised.",
  G(1896, 1896, 'Battle of Adwa', 'addis_ababa', (39.47, 13.5), (38.9, 14.16), 'addis_ababa'),
  R(1889, 1913, 'Emperor of Ethiopia', 'Ethiopia', at='addis_ababa'))
P('Cetshwayo', 'King of the Zulu', (1826, 1884), 3, 'rule war',
  'His army destroyed a British force at Isandlwana in 1879 before the British took his kingdom.',
  R(1872, 1879, 'King of the Zulu', 'Zulu', 'Zululand', at=(31.43, -28.32)), G(1880, 1882, 'Exile and London', 'cape_town', 'london'))
P('Muhammad Ahmad', 'The Mahdi of Sudan', (1844, 1885), 3, 'faith war',
  'Declared himself the Mahdi, drove the Egyptians and British out of Sudan and took Khartoum.',
  G(1881, 1885, 'The Mahdist revolt', (32.55, 13.37), (30.22, 13.18), 'khartoum', 'omdurman'))
P('Charles George Gordon', 'British general', (1833, 1885), 3, 'war',
  "'Chinese Gordon' of the Taiping war, killed when the Mahdi's army stormed Khartoum.",
  G(1863, 1864, 'The Ever-Victorious Army in China', 'shanghai', (120.62, 31.3)), G(1884, 1885, 'Siege of Khartoum', 'cairo', 'khartoum'))
P('Samori Ture', 'West African ruler', (1830, 1900), 3, 'war rule',
  'Built the Wassoulou Empire and fought the French for 16 years.',
  G(1878, 1898, 'Wassoulou Empire against the French', (-8.94, 10.36), (-7.6, 11.4), (-4.0, 9.0), (-2.75, 8.6)))
P('Cecil Rhodes', 'British businessman and colonialist', (1853, 1902), 3, 'rule',
  "Diamond king of Kimberley and prime minister of the Cape who seized the land named Rhodesia after him.",
  G(1871, 1902, 'Kimberley, the Cape and Rhodesia', (24.76, -28.74), 'cape_town', (31.05, -17.83), 'cape_town'))
P('Paul Kruger', 'President of the Transvaal', (1825, 1904), 3, 'rule',
  "Boer leader who defied the British Empire in the Boer War.",
  R(1883, 1900, 'President of the South African Republic', 'Transvaal', at=(28.19, -25.75)), G(1900, 1904, 'Exile in Europe', (5.13, 52.09), (7.88, 46.1)))

# ---------- Asia ----------
P('Hong Xiuquan', 'Leader of the Taiping Rebellion', (1814, 1864), 2, 'faith war',
  "Failed exam candidate who believed he was Jesus' younger brother and led a rebellion that cost twenty million lives.",
  G(1851, 1853, 'The Taiping march', ((109.85, 23.38, 1851.05)), ((110.3, 25.28, 1852.3)), ((112.95, 28.2, 1852.7)), ((114.3, 30.6, 1852.95)), ('nanjing', 1853.25)),
  G(1854, 1864, 'Heavenly King in Nanjing', 'nanjing'))
P('Empress Dowager Cixi', 'Ruler of Qing China', (1835, 1908), 2, 'rule',
  "Concubine who ruled China from behind the throne for nearly fifty years.",
  R(1861, 1908, 'Ruler of China behind the throne', *QING, at='beijing'))
P('Rani of Jhansi', 'Queen of Jhansi', (1828, 1858), 3, 'war rule',
  'Rode into battle against the British in the rebellion of 1857 and died fighting at Gwalior.',
  G(1857, 1858, 'The Indian Rebellion', (78.57, 25.45), (79.73, 26.12), (78.18, 26.22)))
P('Swami Vivekananda', 'Hindu monk', (1863, 1902), 3, 'faith',
  "Brought Hinduism and yoga to the West with his speech at the Parliament of Religions in Chicago in 1893.",
  G(1893, 1897, 'Chicago and the West', ('calcutta', 1893.3), ((-87.63, 41.88, 1893.7)), ('new_york', 1894.5), ('london', 1895.7), ('colombo', 1897.05), ('calcutta', 1897.15)),
  G(1898, 1902, 'Belur Math', 'calcutta'))
P('Matthew C. Perry', 'US naval officer', (1794, 1858), 3, 'explore war',
  "His black ships forced Japan to open its ports in 1854 after two centuries of isolation.",
  G(1852, 1854, 'Expedition to Japan', ((-76.29, 36.85, 1852.88)), ((-16.9, 32.65, 1852.97)), ('cape_town', 1853.1), ((57.5, -20.2, 1853.17)),
    ((79.86, 6.93, 1853.25)), ('singapore', 1853.27), ('hong_kong', 1853.35), ('shanghai', 1853.37), ((127.68, 26.21, 1853.4)), ((139.72, 35.25, 1853.53)),
    ('hong_kong', 1853.7), ((139.64, 35.44, 1854.15)), ((139.72, 35.25, 1854.3))))
P('Emperor Meiji', 'Emperor of Japan', (1852, 1912), 2, 'rule reform',
  "Reigned while Japan turned itself, in one generation, from a feudal shogunate into a modern industrial power.",
  R(1867, 1912, 'Emperor of Japan', *JAPAN, at='tokyo'))
P('Saigō Takamori', 'Samurai leader', (1828, 1877), 3, 'war',
  'Helped overthrow the shogun, then led the last samurai revolt against the new government and died fighting.',
  G(1868, 1868, 'The Boshin War', 'kyoto', 'edo'), G(1877, 1877, 'The Satsuma Rebellion', 'kagoshima', (130.71, 32.8), 'kagoshima'))
P('Chulalongkorn', 'King of Siam', (1853, 1910), 3, 'rule reform',
  'Modernised Siam and played Britain and France off against each other to keep it free.',
  R(1868, 1910, 'King of Siam', 'Rattanakosin Kingdom', 'Siam', at='bangkok'))

# ---------- Latin America and the Pacific ----------
P('Benito Juárez', 'President of Mexico', (1806, 1872), 2, 'rule reform',
  "Zapotec orphan who became president, beat the French-backed emperor Maximilian and is Mexico's great national hero.",
  G(1858, 1861, 'War of Reform from Veracruz', 'mexico_city', (-101.26, 21.02), (-103.35, 20.67), 'veracruz', 'mexico_city'),
  G(1863, 1867, 'Resistance to the French', ('mexico_city', 1863.4), ((-101.0, 25.42, 1864.0)), ((-100.31, 25.67, 1864.3)), ((-106.08, 28.64, 1864.8)),
    ((-106.48, 31.74, 1865.6)), ((-106.08, 28.64, 1866.5)), ((-100.39, 20.59, 1867.4)), ('mexico_city', 1867.55)),
  G(1868, 1872, 'President of Mexico', 'mexico_city'))
P('Maximilian I of Mexico', 'Emperor of Mexico', (1832, 1867), 3, 'rule',
  'Austrian archduke put on a Mexican throne by Napoleon III and shot by Juárez\'s republicans.',
  G(1864, 1867, 'Emperor of Mexico', 'mexico_city', (-100.39, 20.59)))
P('Pedro II of Brazil', 'Emperor of Brazil', (1825, 1891), 3, 'rule',
  'Bookish emperor who ruled Brazil for 49 years and saw slavery abolished before he was deposed.',
  R(1840, 1889, 'Emperor of Brazil', 'Empire of Brazil', at='rio'), G(1889, 1891, 'Exile in Paris', 'paris'))
P('Francisco Solano López', 'President of Paraguay', (1827, 1870), 3, 'rule war',
  'Led Paraguay into a war with Brazil, Argentina and Uruguay that killed most of its men.',
  R(1862, 1870, 'President of Paraguay', 'Paraguay', at='asuncion'))
P('José Martí', 'Cuban poet and patriot', (1853, 1895), 3, 'art war',
  'Poet who organised the Cuban war of independence from exile in New York and died in its first battles.',
  G(1881, 1895, 'Exile in New York', 'new_york'), G(1895, 1895, 'Return to Cuba', ((-72.3, 19.9, 1895.3)), ((-74.6, 20.2, 1895.33)), ((-76.1, 20.2, 1895.38))))
P('Liliʻuokalani', 'Queen of Hawaii', (1838, 1917), 3, 'rule',
  "The last monarch of Hawaii, overthrown by American planters in 1893.",
  R(1891, 1893, 'Queen of Hawaii', 'Kingdom of Hawaii', at=(-157.86, 21.31)))

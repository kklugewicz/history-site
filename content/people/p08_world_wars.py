from _lib import P, R, G

UK = ('United Kingdom of Great Britain and Ireland', 'United Kingdom')
USA = ('United States', 'United States of America')
GER = ('Germany', 'German Empire')
RUS = ('Russian Empire',)
SOV = ('USSR',)
ITA = ('Italy', 'Kingdom of Italy')
JAPAN = ('Empire of Japan', 'Imperial Japan', 'Japan', 'Japan (USA)')

# ---------- the First World War and its revolutions ----------
P('Theodore Roosevelt', 'Twenty-sixth President of the United States', (1858, 1919), 2, 'rule',
  "Rough Rider of the Cuban war who as president built the Panama Canal and America's national parks.",
  G(1898, 1898, 'The Rough Riders in Cuba', (-82.45, 27.95), (-75.83, 20.02)), R(1901, 1909, 'President of the United States', *USA, at='washington'))
P('Woodrow Wilson', 'Twenty-eighth President of the United States', (1856, 1924), 2, 'rule',
  'Took America into the First World War and dreamed up the League of Nations.',
  G(1919, 1919, 'Paris Peace Conference', 'washington', 'paris', 'washington'), R(1913, 1921, 'President of the United States', *USA, at='washington'))
P('Wilhelm II', 'German emperor', (1859, 1941), 2, 'rule',
  "The last Kaiser, whose bluster helped bring on the First World War; he fled to the Netherlands in 1918.",
  R(1888, 1918, 'German emperor', *GER, at='berlin'), G(1919, 1941, 'Exile in the Netherlands', (5.27, 52.04)), wiki='Wilhelm II')
P('Nicholas II', 'Last emperor of Russia', (1868, 1918), 2, 'rule',
  'Lost a war to Japan, a revolution in 1905 and his throne in 1917; shot with his family by the Bolsheviks.',
  R(1894, 1916, 'Emperor of Russia', *RUS, at='st_petersburg'),
  G(1917, 1918, 'Prisoner of the revolution', ((30.4, 59.72, 1917.25)), ((68.25, 58.2, 1917.65)), ((60.6, 56.84, 1918.35))), wiki='Nicholas II of Russia')
P('Grigori Rasputin', 'Mystic at the Russian court', (1869, 1916), 3, 'faith',
  "Siberian holy man who seemed to heal the tsar's son and was murdered by nobles in 1916.",
  G(1905, 1916, 'At the court of the tsar', 'st_petersburg'))
P('Archduke Franz Ferdinand', 'Heir to Austria-Hungary', (1863, 1914), 3, 'rule',
  'His assassination in Sarajevo in June 1914 set off the First World War.',
  G(1914, 1914, 'Assassinated in Sarajevo', ((16.37, 48.21, 1914.45)), ((18.41, 43.86, 1914.49))), wiki='Archduke Franz Ferdinand of Austria')
P('Gavrilo Princip', 'Bosnian Serb assassin', (1894, 1918), 3, 'war',
  "Shot Franz Ferdinand in Sarajevo, the spark of the First World War; died in prison.",
  G(1914, 1918, 'Sarajevo, then prison', ((18.41, 43.86, 1914.49)), ((14.15, 50.51, 1914.95))))
P('David Lloyd George', 'British prime minister', (1863, 1945), 3, 'rule',
  'Led Britain to victory in the First World War and helped write the peace.',
  R(1916, 1922, 'Prime minister', *UK, at='london'))
P('Georges Clemenceau', 'French prime minister', (1841, 1929), 3, 'rule',
  "'The Tiger' who led France through the last year of the war and demanded a harsh peace.",
  R(1917, 1920, 'Prime minister of France', 'France', at='paris'))
P('Philippe Pétain', 'French marshal', (1856, 1951), 3, 'war rule',
  'Hero of Verdun in 1916 who led Vichy France\'s collaboration with Hitler in 1940 and died in prison.',
  G(1916, 1916, 'Verdun', (5.38, 49.16)), R(1940, 1944, 'Head of Vichy France', 'France', at=(3.43, 46.13)), G(1945, 1951, 'Prisoner on the Île d\'Yeu', (-2.35, 46.71)))
P('T. E. Lawrence', 'British officer in the Arab Revolt', (1888, 1935), 2, 'war explore',
  "'Lawrence of Arabia', who rode with the Arab Revolt against the Ottomans from Mecca to Damascus.",
  G(1916, 1918, 'The Arab Revolt', ((39.2, 21.5, 1916.8)), ((38.06, 24.09, 1916.95)), ((36.47, 26.23, 1917.1)), ((35.0, 29.53, 1917.5)), ((35.83, 30.2, 1918.2)),
    ((36.25, 32.33, 1918.7)), ('damascus', 1918.75)))
P('Vladimir Lenin', 'Founder of the Soviet Union', (1870, 1924), 1, 'rule reform',
  'Led the Bolsheviks to power in the October Revolution of 1917 and founded the first communist state.',
  G(1900, 1916, 'Exile in Europe', 'munich', 'london', 'geneva', 'st_petersburg', 'geneva', 'paris', 'krakow', 'zurich'),
  G(1917, 1917, 'The sealed train to Petrograd', ('zurich', 1917.27), ((13.7, 54.5, 1917.28)), ('stockholm', 1917.285), ('st_petersburg', 1917.29)),
  R(1918, 1924, 'Leader of Soviet Russia', *SOV, *RUS, at='moscow'))
P('Leon Trotsky', 'Russian revolutionary', (1879, 1940), 2, 'war rule',
  'Organised the October Revolution and built the Red Army, then lost to Stalin, who had him killed in Mexico.',
  G(1917, 1924, 'Commander of the Red Army', 'st_petersburg', ('kazan', 1918.65), 'moscow', ((39.72, 47.23, 1919.9)), 'moscow'),
  G(1929, 1940, 'Exile', ((29.12, 40.86, 1929.1)), ((29.12, 40.86, 1933.5)), ((2.35, 48.86, 1933.6)), ((2.35, 48.86, 1935.4)), ((10.75, 59.91, 1935.5)),
    ((10.75, 59.91, 1936.95)), ((-99.16, 19.35, 1937.05))))
P('Joseph Stalin', 'Dictator of the Soviet Union', (1878, 1953), 1, 'rule war',
  'Turned the Soviet Union into an industrial and military giant through terror, famine and the Gulag, and beat Hitler.',
  R(1924, 1953, 'Leader of the Soviet Union', *SOV, at='moscow'))
P('Mustafa Kemal Atatürk', 'Founder of modern Turkey', (1881, 1938), 1, 'war rule reform',
  'Hero of Gallipoli who won the Turkish War of Independence and made Turkey a secular republic.',
  G(1915, 1915, 'Gallipoli', (26.3, 40.23)),
  G(1919, 1922, 'War of Independence', ((36.33, 41.29, 1919.38)), ((41.27, 39.9, 1919.55)), ((37.02, 39.75, 1919.7)), ('ankara', 1920.0), ((30.3, 39.6, 1921.65)),
    ('ankara', 1921.8), ((30.0, 38.75, 1922.65)), ('smyrna', 1922.7)),
  R(1923, 1938, 'President of Turkey', 'Republic of Turkey', 'Turkey', at='ankara'))
P('Sun Yat-sen', 'Father of modern China', (1866, 1925), 2, 'rule reform',
  'Plotted revolution from exile for twenty years; first president of the Republic of China in 1912.',
  G(1895, 1911, 'Revolutionary in exile', 'canton', 'hong_kong', (-157.86, 21.31), 'london', 'tokyo', 'singapore', 'tokyo', (-104.99, 39.74)),
  G(1912, 1912, 'First president of the Republic of China', 'nanjing'), G(1913, 1916, 'Exile in Japan', 'tokyo'), G(1917, 1925, 'Government at Canton', 'canton', 'beijing'))
P('Yuan Shikai', 'President of China', (1859, 1916), 3, 'rule',
  'General who forced the last emperor out, then tried to make himself emperor.',
  G(1912, 1916, 'President, then would-be emperor of China', 'beijing'))
P('Puyi', 'Last emperor of China', (1906, 1967), 3, 'rule',
  'Became emperor at two, was deposed at six, served Japan as puppet ruler of Manchukuo and ended as a gardener in Beijing.',
  R(1908, 1912, 'Emperor of China', 'Manchu Empire', at='beijing'), G(1932, 1945, 'Puppet emperor of Manchukuo', (125.32, 43.88)),
  G(1950, 1959, 'Prisoner at Fushun', (123.9, 41.88)), G(1960, 1967, 'Beijing', 'beijing'))
P('Roald Amundsen', 'Norwegian polar explorer', (1872, 1928), 2, 'explore',
  'First through the Northwest Passage and first to the South Pole, in 1911, beating Scott by five weeks.',
  G(1903, 1906, 'The Northwest Passage', ((10.75, 59.91, 1903.45)), ((-53.0, 66.9, 1903.6)), ((-95.88, 68.63, 1903.75)), ((-95.88, 68.63, 1905.4)),
    ((-141.0, 69.65, 1905.7)), ((-141.0, 69.65, 1906.4)), ((-165.41, 64.5, 1906.65))),
  G(1910, 1912, 'First to the South Pole', ((10.75, 59.91, 1910.6)), ((-16.9, 32.65, 1910.7)), ((-164.0, -78.5, 1911.03)), ((-160.0, -89.0, 1911.94)),
    ((-164.0, -78.5, 1912.07)), ((147.33, -42.88, 1912.2))))
P('Robert Falcon Scott', 'British polar explorer', (1868, 1912), 3, 'explore',
  'Reached the South Pole a month after Amundsen and died with his men on the way back.',
  G(1910, 1912, 'The race to the South Pole', ((-3.18, 51.46, 1910.45)), ((172.72, -43.6, 1910.9)), ((166.67, -77.85, 1911.0)), ((-160.0, -89.0, 1912.05)), ((169.0, -79.6, 1912.24))))
P('Ernest Shackleton', 'Anglo-Irish polar explorer', (1874, 1922), 3, 'explore',
  'When the ice crushed his ship Endurance, he sailed a lifeboat 1,300 km to fetch help and saved every man.',
  G(1914, 1916, 'The Endurance expedition', ((-36.5, -54.28, 1914.92)), ((-40.0, -74.0, 1915.1)), ((-53.0, -69.0, 1915.85)), ((-55.1, -61.1, 1916.3)),
    ((-36.5, -54.28, 1916.38)), ((-57.85, -51.69, 1916.5)), ((-55.1, -61.1, 1916.66))))
P('Wright brothers', 'Aviation pioneers', (1867, 1948), 2, 'mind',
  'Bicycle makers Orville and Wilbur Wright made the first powered aeroplane flight at Kitty Hawk in 1903.',
  G(1903, 1903, 'First powered flight at Kitty Hawk', (-84.19, 39.76), (-75.67, 36.02)), G(1904, 1908, 'Dayton and France', (-84.19, 39.76), (0.2, 48.0)))
P('Henry Ford', 'American industrialist', (1863, 1947), 3, 'mind',
  'His moving assembly line made the Model T cheap enough for ordinary families.',
  G(1903, 1947, 'Ford Motor Company in Detroit', (-83.05, 42.33)))
P('Albert Einstein', 'German-born physicist', (1879, 1955), 1, 'mind',
  'Worked out relativity and E = mc², and fled the Nazis for America.',
  G(1902, 1909, 'Patent office in Bern', (7.45, 46.95)), G(1909, 1913, 'Zurich and Prague', 'zurich', 'prague', 'zurich'),
  G(1914, 1932, 'Berlin: general relativity', 'berlin'), G(1933, 1955, 'Princeton', (-74.66, 40.35)))
P('Marie Curie', 'Polish-French physicist and chemist', (1867, 1934), 1, 'mind',
  'Discovered radium and polonium, the first person to win two Nobel prizes.',
  G(1867, 1890, 'Warsaw', 'warsaw'), G(1891, 1934, 'Paris', 'paris'))
P('Sigmund Freud', 'Founder of psychoanalysis', (1856, 1939), 2, 'mind',
  'Explored the unconscious mind and dreams in Vienna; fled the Nazis to London.',
  G(1886, 1938, 'Vienna', 'vienna'), G(1938, 1939, 'Exile in London', 'london'))
P('Emmeline Pankhurst', 'British suffragette', (1858, 1928), 3, 'reform',
  "Led the suffragettes' fight, through prison and hunger strikes, for women's right to vote.",
  G(1903, 1918, 'Suffragette leader', 'manchester', 'london'))
P('Emiliano Zapata', 'Mexican revolutionary', (1879, 1919), 3, 'war reform',
  "Led the peasant armies of the south in the Mexican Revolution under the cry 'Land and liberty'.",
  G(1910, 1919, 'The revolution in the south', (-98.95, 18.81), (-99.23, 18.92), 'mexico_city', (-99.23, 18.92), (-98.87, 18.62)))
P('Pancho Villa', 'Mexican revolutionary', (1878, 1923), 3, 'war',
  'Bandit turned general of the north in the Mexican Revolution who even raided the United States.',
  G(1910, 1920, 'The revolution in the north', ((-106.08, 28.64, 1910.9)), ((-106.42, 31.74, 1911.35)), ((-103.4, 25.54, 1914.25)), ((-102.57, 22.77, 1914.47)),
    ('mexico_city', 1914.92), ((-100.81, 20.52, 1915.3)), ((-107.64, 31.83, 1916.2)), ((-105.66, 26.93, 1920.6))))

# ---------- between the wars and the Second World War ----------
P('Benito Mussolini', 'Fascist dictator of Italy', (1883, 1945), 1, 'rule war',
  'Founded fascism, marched on Rome in 1922 and took Italy into the war on Hitler\'s side; shot by partisans.',
  R(1922, 1942, 'Dictator of Italy', *ITA, at='rome'), G(1943, 1945, 'Puppet state at Salò', (10.52, 45.6), (9.28, 46.12)))
P('Adolf Hitler', 'Nazi dictator of Germany', (1889, 1945), 1, 'rule war',
  'Took Germany into the Second World War and ordered the murder of six million Jews in the Holocaust.',
  G(1914, 1918, 'Soldier on the Western Front', 'munich', (2.95, 50.75)), G(1919, 1932, 'Munich: the rise of the Nazi party', 'munich'),
  R(1933, 1945, 'Dictator of Germany', 'Germany', at='berlin'))
P('Hirohito', 'Emperor of Japan', (1901, 1989), 2, 'rule',
  'Reigned through Japan\'s wars of conquest and its surrender in 1945, then as a constitutional monarch.',
  R(1926, 1989, 'Emperor of Japan', *JAPAN, at='tokyo'))
P('Hideki Tojo', 'Prime minister of Japan', (1884, 1948), 3, 'war rule',
  'General who led Japan into war with the United States in 1941; hanged as a war criminal.',
  G(1941, 1944, 'Prime minister of Japan', 'tokyo'))
P('Neville Chamberlain', 'British prime minister', (1869, 1940), 3, 'rule',
  "Gave Hitler part of Czechoslovakia at Munich in 1938, promising 'peace for our time'.",
  R(1937, 1940, 'Prime minister', *UK, at='london'), G(1938, 1938, 'The Munich agreement', 'london', 'munich', 'london'))
P('Winston Churchill', 'British prime minister', (1874, 1965), 1, 'rule war',
  "Rallied Britain to fight on alone against Hitler in 1940: 'We shall never surrender.'",
  G(1899, 1900, 'Boer War: captured and escaped', ((18.42, -33.92, 1899.83)), ((29.79, -29.0, 1899.87)), ((28.19, -25.75, 1899.9)), ((32.6, -25.97, 1899.97))),
  G(1915, 1916, 'Gallipoli, then the trenches', 'london', (2.9, 50.75)),
  R(1940, 1945, 'Prime minister', *UK, at='london'), R(1951, 1955, 'Prime minister', *UK, at='london'))
P('Franklin D. Roosevelt', 'Thirty-second President of the United States', (1882, 1945), 1, 'rule',
  'Led America through the Great Depression with the New Deal and through the Second World War.',
  R(1933, 1945, 'President of the United States', *USA, at='washington'))
P('Francisco Franco', 'Dictator of Spain', (1892, 1975), 2, 'war rule',
  'Won the Spanish Civil War and ruled Spain as dictator until his death.',
  G(1936, 1939, 'Spanish Civil War', ((-15.42, 28.1, 1936.54)), ((-5.37, 35.57, 1936.55)), ((-5.98, 37.39, 1936.6)), ((-3.7, 42.34, 1936.8)), ('madrid', 1939.24)),
  R(1939, 1975, 'Dictator of Spain', 'Spain', at='madrid'))
P('Haile Selassie', 'Emperor of Ethiopia', (1892, 1975), 2, 'rule',
  "Pleaded with the League of Nations against Mussolini's invasion, returned in 1941 and ruled until 1974.",
  R(1930, 1974, 'Emperor of Ethiopia', 'Ethiopia', 'Abyssinia', at='addis_ababa'), G(1936, 1940, 'Exile in Bath', 'addis_ababa', (43.14, 11.6), 'london', (-2.36, 51.38)))
P('Ibn Saud', 'Founder of Saudi Arabia', (1875, 1953), 2, 'rule war',
  'Retook Riyadh with forty men in 1902 and conquered most of Arabia, where oil was found in 1938.',
  G(1902, 1931, 'Conquest of Arabia', ((47.98, 29.37, 1902.0)), ((46.72, 24.69, 1902.04)), ((43.97, 26.33, 1906)), ((50.0, 26.0, 1913.4)), ((41.69, 27.52, 1921.85)),
    ((39.83, 21.42, 1924.8)), ((39.19, 21.49, 1925.95)), ((46.72, 24.69, 1931))),
  R(1932, 1953, 'King of Saudi Arabia', 'Saudi Arabia', at=(46.72, 24.69)))
P('Reza Shah', 'Shah of Iran', (1878, 1944), 3, 'rule reform',
  'Cossack officer who seized power, made himself shah and forced Iran to modernise.',
  R(1925, 1941, 'Shah of Iran', 'Iran', at='tehran'))
P('Mahatma Gandhi', 'Leader of Indian independence', (1869, 1948), 1, 'reform faith',
  "Led India to independence by non-violent protest, from the Salt March of 1930 to Britain's departure in 1947.",
  G(1893, 1914, 'Lawyer and protest leader in South Africa', (31.03, -29.86), (28.05, -26.2), (30.38, -29.6)),
  G(1915, 1929, 'Leader of the independence movement', (72.58, 23.03), 'delhi', 'calcutta', (72.58, 23.03)),
  G(1930, 1930, 'The Salt March', ((72.58, 23.03, 1930.2)), ((72.99, 22.31, 1930.23)), ((72.83, 21.17, 1930.25)), ((72.81, 20.89, 1930.26))),
  G(1931, 1931, 'Round Table Conference in London', 'bombay', 'london', 'rome', 'bombay'),
  G(1932, 1948, 'Quit India and independence', (73.9, 18.55), (78.66, 20.73), (73.9, 18.55), 'calcutta', (91.0, 23.0), 'delhi'))
P('Muhammad Ali Jinnah', 'Founder of Pakistan', (1876, 1948), 2, 'rule',
  "Lawyer who led the Muslim League's demand for a separate state and became Pakistan's first governor-general.",
  G(1916, 1946, 'Leader of the Muslim League', 'bombay', 'delhi'), R(1947, 1948, 'Governor-general of Pakistan', 'Pakistan', at=(67.0, 24.86)))
P('Jawaharlal Nehru', 'First prime minister of India', (1889, 1964), 2, 'rule',
  "Gandhi's heir who led independent India for 17 years and helped found the non-aligned movement.",
  G(1920, 1946, 'Independence movement and prison', (81.85, 25.43), 'delhi', (75.85, 22.72)), R(1947, 1964, 'Prime minister of India', 'India', at='delhi'))
P('Rabindranath Tagore', 'Bengali poet', (1861, 1941), 3, 'art',
  'The first non-European to win the Nobel prize for literature; wrote the national anthems of India and Bangladesh.',
  G(1901, 1941, 'Santiniketan', (87.68, 23.68)))
P('Chiang Kai-shek', 'Leader of the Republic of China', (1887, 1975), 1, 'war rule',
  'Led the Nationalists against the warlords, Japan and the Communists, then ruled on Taiwan after losing China.',
  G(1926, 1928, 'The Northern Expedition', ((113.26, 23.13, 1926.55)), ((112.95, 28.2, 1926.6)), ((114.3, 30.6, 1926.75)), ('nanjing', 1927.2), ('shanghai', 1927.28),
    ((117.2, 39.13, 1928.4)), ('beijing', 1928.45)),
  R(1928, 1936, 'Leader of the Republic of China', 'Republic of China', 'China', at='nanjing'),
  R(1937, 1949, 'Leader of the Republic of China', 'Republic of China', 'China', at=(106.55, 29.56)),
  R(1950, 1975, 'President on Taiwan', 'Taiwan', at=(121.56, 25.04)))
P('Mao Zedong', 'Founder of the People\'s Republic of China', (1893, 1976), 1, 'rule war',
  'Led the Communists on the Long March and to victory in 1949, then ruled China through famine and the Cultural Revolution.',
  G(1927, 1934, 'Jinggang Mountains and the Jiangxi Soviet', (114.17, 26.57), (115.97, 25.89)),
  G(1934, 1935, 'The Long March', ((115.97, 25.89, 1934.8)), ((110.3, 25.28, 1934.92)), ((106.93, 27.7, 1935.04)), ((102.6, 26.6, 1935.33)), ((102.22, 29.92, 1935.4)),
    ((102.9, 32.6, 1935.6)), ((104.2, 34.0, 1935.75)), ((108.0, 36.9, 1935.8))),
  G(1936, 1947, "Yan'an", (109.49, 36.6)), G(1947, 1949, 'Victory in the civil war', (110.0, 37.6), (114.0, 38.35), 'beijing'),
  R(1949, 1976, "Chairman of the People's Republic of China", 'China', at='beijing'))
P('Ho Chi Minh', 'Founder of communist Vietnam', (1890, 1969), 1, 'rule war',
  "Spent thirty years abroad, led the Viet Minh to independence from France and North Vietnam against the US.",
  G(1911, 1940, 'Thirty years abroad', ((106.7, 10.78, 1911.45)), ('marseille', 1911.7), ('new_york', 1912.6), ('london', 1913.9), ('london', 1917.3), ('paris', 1917.5),
    ('paris', 1923.4), ('moscow', 1923.6), ('moscow', 1924.8), ('canton', 1925), ('canton', 1927.3), ('hong_kong', 1930.1), ('hong_kong', 1932.9), ('moscow', 1934.5),
    ('moscow', 1938.6), ((108.35, 22.8, 1938.9)), ((106.25, 22.93, 1940.99))),
  G(1941, 1945, 'Pác Bó cave and the Viet Minh', (106.25, 22.93)), G(1945, 1954, 'War against France', 'thang_long', (105.6, 21.8), 'thang_long'),
  R(1955, 1969, 'President of North Vietnam', 'Vietnam', at='thang_long'))
P('Sukarno', 'First president of Indonesia', (1901, 1970), 2, 'rule',
  'Declared Indonesia independent from the Dutch in 1945 and led it until 1967.',
  R(1945, 1967, 'President of Indonesia', 'Indonesia', at=(106.85, -6.21)))
P('Józef Piłsudski', 'Founder of reborn Poland', (1867, 1935), 3, 'war rule',
  'Led Poland back to independence in 1918 and beat the Red Army at the gates of Warsaw in 1920.',
  R(1918, 1935, 'Leader of Poland', 'Poland', at='warsaw'))
P('Charles Lindbergh', 'American aviator', (1902, 1974), 3, 'explore',
  'Flew alone, non-stop, from New York to Paris in 1927.',
  G(1927, 1927, 'Solo across the Atlantic', ((-73.6, 40.73, 1927.385)), ((-53.0, 47.5, 1927.39)), ((-10.0, 52.0, 1927.393)), ((2.44, 48.97, 1927.396))))
P('Amelia Earhart', 'American aviator', (1897, 1937), 3, 'explore',
  'First woman to fly solo across the Atlantic; vanished over the Pacific trying to fly round the world.',
  G(1932, 1932, 'Solo across the Atlantic', ((-53.22, 47.7, 1932.38)), ((-7.3, 55.0, 1932.39))),
  G(1937, 1937, 'The last flight', ((-122.22, 37.72, 1937.39)), ((-80.2, 25.8, 1937.42)), ((-48.5, -1.45, 1937.45)), ((-17.44, 14.69, 1937.47)),
    ((72.88, 19.08, 1937.5)), ((100.5, 13.76, 1937.51)), ((130.84, -12.46, 1937.53)), ((147.0, -6.73, 1937.54)), ((-176.62, 0.81, 1937.55))))
P('Anne Frank', 'Jewish diarist', (1929, 1945), 2, 'art',
  'Hid from the Nazis in an Amsterdam attic for two years; her diary survived her death in Bergen-Belsen.',
  G(1934, 1944, 'Amsterdam', 'amsterdam'), G(1944, 1945, 'Deported', ((19.2, 50.03, 1944.75)), ((9.9, 52.76, 1944.85))))
P('Erwin Rommel', 'German field marshal', (1891, 1944), 3, 'war',
  "The 'Desert Fox' of the North African campaign, forced to kill himself after the plot against Hitler.",
  G(1940, 1940, 'Through France', (6.4, 50.0), (4.85, 50.2), (0.1, 49.5)),
  G(1941, 1943, 'North Africa', ((13.19, 32.89, 1941.12)), ((23.97, 32.08, 1941.3)), ((23.97, 32.08, 1942.47)), ((28.95, 30.83, 1942.55)), ((28.95, 30.83, 1942.82)),
    ((13.19, 32.89, 1943.05)), ((10.18, 36.81, 1943.2))),
  G(1944, 1944, 'Normandy', (-0.37, 49.18), (9.9, 48.6)))
P('Dwight D. Eisenhower', 'Allied commander and US president', (1890, 1969), 2, 'war rule',
  'Commanded the D-Day landings and the Allied armies in Europe, then served two terms as president.',
  G(1942, 1945, 'Supreme Allied commander', ('london', 1942.5), ((-5.35, 36.14, 1942.85)), ('algiers', 1943.0), ((14.5, 35.9, 1943.5)), ('london', 1944.05),
    ((-1.3, 50.88, 1944.43)), ((-0.6, 49.3, 1944.45)), ('paris', 1944.65), ((4.03, 49.26, 1945.35))),
  R(1953, 1961, 'President of the United States', *USA, at='washington'))
P('Douglas MacArthur', 'American general', (1880, 1964), 3, 'war',
  "Left the Philippines in 1942 promising 'I shall return', did, then ran occupied Japan and the Korean War.",
  G(1942, 1951, 'The Pacific war and Korea', ((120.98, 14.6, 1942.2)), ((153.03, -27.47, 1942.6)), ((147.15, -9.44, 1943.0)), ((125.0, 11.2, 1944.8)), ((120.98, 14.6, 1945.2)),
    ('tokyo', 1945.66), ('tokyo', 1950.7), ((126.63, 37.47, 1950.71)), ('tokyo', 1951.3)))
P('Georgy Zhukov', 'Soviet marshal', (1896, 1974), 3, 'war',
  'Saved Moscow and Leningrad, planned the victory at Stalingrad and took Berlin.',
  G(1939, 1945, 'From Khalkhin Gol to Berlin', ((118.2, 47.65, 1939.6)), ('moscow', 1941.8), ((44.5, 48.7, 1942.9)), ((36.2, 51.7, 1943.55)), ('warsaw', 1945.05), ('berlin', 1945.32)))
P('Charles de Gaulle', 'Leader of Free France and president', (1890, 1970), 2, 'war rule',
  'Refused to accept defeat in 1940, led the Free French from London and later founded the Fifth Republic.',
  G(1940, 1944, 'Leader of the Free French', ('london', 1940.46), ((-17.44, 14.69, 1940.7)), ('london', 1941.0), ('london', 1943.35), ('algiers', 1943.42),
    ('algiers', 1944.4), ((-0.6, 49.3, 1944.45)), ('paris', 1944.65)),
  R(1945, 1946, 'Head of the provisional government', 'France', at='paris'),
  R(1959, 1969, 'President of France', 'France', at='paris'))
P('Bernard Montgomery', 'British field marshal', (1887, 1976), 3, 'war',
  "'Monty', who beat Rommel at El Alamein in 1942 and led the British armies from Normandy to the Baltic.",
  G(1942, 1945, 'From El Alamein to the Baltic', ((28.95, 30.83, 1942.6)), ((28.95, 30.83, 1942.84)), ('tripoli', 1943.06), ('tunis', 1943.35), ('syracuse', 1943.53),
    ((16.2, 38.5, 1943.7)), ('london', 1944.0), ((-0.37, 49.18, 1944.45)), ((4.4, 51.22, 1944.68)), ((5.9, 51.98, 1944.72)), ((10.4, 53.25, 1945.34))))
P('Hermann Göring', 'Head of the German air force', (1893, 1946), 3, 'war power',
  "Hitler's second-in-command, whose Luftwaffe lost the Battle of Britain; killed himself before he could be hanged.",
  G(1933, 1944, 'Head of the Luftwaffe', 'berlin'), G(1945, 1946, 'Tried at Nuremberg', ('berlin', 1945.0), ((13.0, 47.63, 1945.3)), ('nuremberg', 1945.8)))
P('Isoroku Yamamoto', 'Japanese admiral', (1884, 1943), 3, 'war',
  'Planned the attack on Pearl Harbor, lost the Battle of Midway and was shot down by American fighters.',
  G(1941, 1943, 'Commander of the Combined Fleet', ((132.42, 34.2, 1941.0)), ((132.42, 34.2, 1942.38)), ((160.0, 32.0, 1942.42)), ((132.42, 34.2, 1942.47)),
    ((151.78, 7.42, 1942.6)), ((152.2, -4.2, 1943.25)), ((155.45, -6.67, 1943.3))))
P('Chester W. Nimitz', 'American admiral', (1885, 1966), 3, 'war',
  'Commanded the US Pacific Fleet from Pearl Harbor to the Japanese surrender in Tokyo Bay.',
  G(1941, 1945, 'Commander of the Pacific Fleet', ('pearl_harbor', 1941.98), ('pearl_harbor', 1945.0), ('guam', 1945.1), ((139.78, 35.35, 1945.67))))
P('Porfirio Díaz', 'Dictator of Mexico', (1830, 1915), 3, 'rule',
  'Ruled Mexico for 35 years of railways and foreign money until the Revolution of 1910 drove him out.',
  R(1876, 1910, 'President of Mexico', 'Mexico', at='mexico_city'), G(1911, 1915, 'Exile in Paris', ('veracruz', 1911.4), ('paris', 1911.5)))
P('Francisco Madero', 'President of Mexico', (1873, 1913), 3, 'rule reform',
  'Rich landowner who called the Mexican Revolution in 1910 and was murdered by his own general in 1913.',
  G(1910, 1911, 'The call to revolution', ((-100.98, 25.42, 1910.4)), ((-98.49, 29.42, 1910.8)), ((-106.42, 31.74, 1911.35)), ('mexico_city', 1911.45)),
  R(1911, 1913, 'President of Mexico', 'Mexico', at='mexico_city'))
P('Fulgencio Batista', 'Dictator of Cuba', (1901, 1973), 3, 'rule',
  'Army sergeant who ruled Cuba on and off from 1933 until Castro drove him out on New Year\'s Day 1959.',
  R(1940, 1944, 'President of Cuba', 'Cuba', at='havana'), R(1952, 1958, 'Dictator of Cuba', 'Cuba', at='havana'))

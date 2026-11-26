"""Heads of state of Africa, the Americas and Oceania between the famous ones in the era files, so a country's name on the
map has its ruler beside it in nearly every year: Egypt and the rest of Africa, the presidents of the United States,
Mexico, Brazil, Argentina and the rest of Latin America, Canada, Australia and New Zealand."""
from _lib import P, R, G


def K(name, role, life, a, b, why, *names, at, rank=3, tags='rule', wiki=None):
    """one reign: the ruler sits by the first of `names` on the map from year a to b, or at `at` when none is"""
    P(name, role, life, rank, tags, why, R(a, b, role, *names, at=at), wiki=wiki)


# ---------- Egypt ----------
EG = ('Egypt',)
MAM = ('Mamluke Sultanate', 'Egypt')
MS = 'Mamluk sultan of Egypt'
P('An-Nasir Hasan', MS, (1334, 1361), 3, 'rule art',
  'Boy sultan in the years of the Black Death, who built the vast mosque and school of Sultan Hasan below the Cairo citadel.',
  R(1347, 1351, MS, *MAM, at='cairo'), R(1354, 1361, MS, *MAM, at='cairo'))
K('An-Nasir Faraj', MS, (1386, 1412), 1399, 1412,
  'Lost Syria to Timur, who sacked Damascus in 1401, and was killed by his own emirs.', *MAM, at='cairo')
K("Al-Mu'ayyad Shaykh", MS, (1370, 1421), 1412, 1421,
  'Former slave who built his great mosque by the Bab Zuwayla gate on the site of the prison where he had once been held.', *MAM,
  at='cairo')
P('Ibrahim Pasha of Egypt', 'Egyptian general', (1789, 1848), 3, 'war rule',
  "Muhammad Ali's son and greatest general, who crushed the first Saudi state, fought the Greek rebels, and conquered Syria almost to Constantinople.",
  G(1816, 1818, 'War against the Saudis', ('cairo', 1816.7), ('jeddah', 1816.85), ('medina', 1817.2), ((46.57, 24.73, 1818.3)),
    ((46.57, 24.73, 1818.7))),
  G(1824, 1828, 'War in Greece', ('alexandria', 1824.6), ((21.73, 36.82, 1825.15)), ((21.67, 36.91, 1827.8)), ((21.73, 36.82, 1828.6))),
  G(1831, 1840, 'Conquest of Syria', ('cairo', 1831.8), ((35.07, 32.92, 1832.4)), ('damascus', 1832.5), ('aleppo', 1832.6),
    ('konya', 1832.97), ((37.98, 37.02, 1839.48)), ('damascus', 1840.5), ('cairo', 1840.95)),
  R(1848, 1848, 'Ruler of Egypt', *EG, at='cairo'))
K('Abbas I of Egypt', 'Ruler of Egypt', (1812, 1854), 1849, 1854,
  "Muhammad Ali's grandson, who shut his grandfather's schools and factories and was murdered by two of his servants.", *EG, at='cairo')
K("Sa'id of Egypt", 'Ruler of Egypt', (1822, 1863), 1854, 1863,
  'Gave his French friend Ferdinand de Lesseps the right to dig the Suez Canal.', *EG, at='cairo')
K("Isma'il Pasha", 'Khedive of Egypt', (1830, 1895), 1863, 1879,
  'Opened the Suez Canal in 1869 and declared Egypt part of Europe, then ran up such debts that Britain and France had him deposed.',
  *EG, at='cairo')
K('Tewfik Pasha', 'Khedive of Egypt', (1852, 1892), 1879, 1892,
  'Khedive under whom Britain occupied Egypt in 1882 after crushing the Urabi revolt.', *EG, at='cairo')
P('Ahmed Urabi', 'Egyptian nationalist', (1841, 1911), 3, 'war reform',
  'Peasant-born colonel who rose against foreign control of Egypt and was beaten by the British at Tel el-Kebir in 1882.',
  G(1881, 1882, 'The Urabi revolt', ('cairo', 1881.7), ('alexandria', 1882.5), ((31.87, 30.55, 1882.7)), ('cairo', 1882.75)),
  G(1883, 1901, 'Exile in Ceylon', 'colombo'))
K('Lord Cromer', 'British consul-general in Egypt', (1841, 1917), 1883, 1907,
  'British agent who ran Egypt in all but name for 24 years.', *EG, at='cairo', wiki='Evelyn Baring, 1st Earl of Cromer')
K('Abbas II of Egypt', 'Khedive of Egypt', (1874, 1944), 1892, 1914,
  'Last khedive, who clashed with Lord Cromer and was deposed by the British when the First World War began.', *EG, at='cairo')
K('Hussein Kamel of Egypt', 'Sultan of Egypt', (1853, 1917), 1914, 1917,
  'Made sultan by the British when they declared Egypt a protectorate in 1914.', *EG, at='cairo')
K('Fuad I of Egypt', 'King of Egypt', (1868, 1936), 1917, 1936,
  'Sultan, then the first king of Egypt after Britain granted it independence in name in 1922.', *EG, at='cairo')
P('Saad Zaghloul', 'Prime minister of Egypt', (1859, 1927), 3, 'rule reform',
  'Leader of the revolution of 1919 against British rule, twice exiled, who came back to win a landslide and lead the government.',
  G(1919, 1923, 'The revolution of 1919 and exile', ('cairo', 1919.18), ((14.51, 35.9, 1919.22)), ('paris', 1919.4), ('cairo', 1921.3),
    ('cairo', 1921.97), ((45.03, 12.8, 1922.05)), ((55.45, -4.62, 1922.3)), ((45.03, 12.8, 1922.85)), ((32.55, 29.97, 1922.9)),
    ((14.51, 35.9, 1922.95)), ((-5.35, 36.14, 1923.0)), ((5.0, 37.6, 1923.3)), ((14.51, 35.9, 1923.5)), ('alexandria', 1923.68),
    ('cairo', 1923.7)),
  R(1924, 1924, 'Prime minister of Egypt', *EG, at='cairo'))
P('Farouk of Egypt', 'King of Egypt', (1920, 1965), 3, 'rule',
  "Last king of Egypt, famous for his appetites and his collections, overthrown by Nasser's army officers in 1952.",
  R(1936, 1951, 'King of Egypt', *EG, at='cairo'),
  G(1952, 1965, 'Exile in Italy', ('alexandria', 1952.56), ('rome', 1952.75), ('rome', 1965.2)))
K('Muhammad Naguib', 'President of Egypt', (1901, 1984), 1952, 1954,
  'Popular general put at the head of the revolution of 1952 as Egypt\'s first president, then pushed aside by Nasser.', *EG, at='cairo')
K('Hosni Mubarak', 'President of Egypt', (1928, 2020), 1981, 2011,
  'Air force commander who ruled Egypt for thirty years after Sadat was shot, until the protests of 2011 brought him down.', *EG,
  at='cairo')
K('Mohamed Morsi', 'President of Egypt', (1951, 2019), 2012, 2013,
  "Egypt's first freely elected president, of the Muslim Brotherhood, overthrown by the army after a year; he died in court.", *EG,
  at='cairo')
K('Abdel Fattah el-Sisi', 'President of Egypt', (1954, None), 2014, 2026,
  'General who overthrew Morsi in 2013 and has ruled Egypt since.', *EG, at='cairo')

# ---------- Ethiopia and the Horn ----------
ET = ('Ethiopia', 'Abyssinia', 'Ethiopia (Italy)')
EE = 'Emperor of Ethiopia'
K('Zara Yaqob', EE, (1399, 1468), 1434, 1468,
  'Zealous emperor who founded Debre Berhan and sent monks to the church council of Florence.', *ET, at=(39.53, 9.68), tags='rule faith')
P('Lebna Dengel', EE, (1496, 1540), 3, 'rule',
  'Saw his empire overrun by Ahmad Gragn of Adal, appealed to Portugal for help, and died a fugitive in the mountains.',
  R(1508, 1528, EE, *ET, at=(39.53, 9.68)),
  G(1529, 1540, 'A fugitive in the highlands', ((39.6, 9.2, 1529.2)), ((38.5, 11.9, 1533.0)), ((39.28, 14.37, 1540.6))))
K('Fasilides', EE, (1603, 1667), 1632, 1667,
  'Threw out the Jesuits, restored the Orthodox faith and built the castles of his new capital, Gondar.', *ET, at='gondar')
P('Yohannes IV', EE, (1837, 1889), 3, 'rule war',
  'Beat two Egyptian invasions and fell fighting the Sudanese Mahdists at Gallabat in 1889.',
  R(1872, 1888, EE, *ET, at=(39.47, 13.5)),
  G(1889, 1889, 'Battle of Gallabat', ((39.47, 13.5, 1889.0)), ((36.36, 12.97, 1889.19))))
K('Mengistu Haile Mariam', 'Leader of Ethiopia', (1937, None), 1977, 1991,
  'Army officer who helped overthrow Haile Selassie, ran a Red Terror and ruled through the famine of the 1980s, then fled to Zimbabwe.',
  *ET, at='addis_ababa')
K('Meles Zenawi', 'Prime minister of Ethiopia', (1955, 2012), 1991, 2012,
  'Rebel leader who overthrew Mengistu and ruled Ethiopia for 21 years.', *ET, at='addis_ababa')
K('Hailemariam Desalegn', 'Prime minister of Ethiopia', (1965, None), 2012, 2017,
  'Took over when Meles died and resigned amid mass protests.', *ET, at='addis_ababa')
K('Siad Barre', 'President of Somalia', (1919, 1995), 1969, 1991,
  'General who ruled Somalia for 22 years; his fall left the country without a government.', 'Somalia', at=(45.34, 2.04))

# ---------- North Africa and Sudan ----------
MOR = ('Morocco', 'Watassid Morocco', 'Morocco (France)')
K('Ahmad al-Mansur', 'Sultan of Morocco', (1549, 1603), 1578, 1603,
  'Became sultan on the day of the Battle of the Three Kings in 1578, sent an army across the Sahara to conquer Songhai, and grew rich on its gold.',
  *MOR, at='marrakesh', tags='rule war')
P('Mohammed V of Morocco', 'King of Morocco', (1909, 1961), 3, 'rule',
  'Sultan exiled by the French to Corsica and Madagascar, who came home to lead Morocco to independence in 1956.',
  R(1927, 1952, 'Sultan of Morocco', *MOR, at='rabat'),
  G(1953, 1955, 'Exiled by the French', ('rabat', 1953.64), ((8.74, 41.92, 1953.66)), ((47.03, -19.87, 1954.1)), ((47.03, -19.87, 1955.75)),
    ('paris', 1955.85), ('rabat', 1955.88)),
  R(1956, 1961, 'King of Morocco', *MOR, at='rabat'))
K('Hassan II of Morocco', 'King of Morocco', (1929, 1999), 1961, 1999,
  'Ruled for 38 years, survived two coup attempts, and sent 350,000 Moroccans on the Green March into Western Sahara in 1975.', *MOR,
  at='rabat')
K('Mohammed VI of Morocco', 'King of Morocco', (1963, None), 1999, 2026,
  'King of Morocco since 1999.', *MOR, at='rabat')
K('Habib Bourguiba', 'President of Tunisia', (1903, 2000), 1956, 1987,
  'Led Tunisia to independence and gave its women rights unmatched in the Arab world, until he was removed as senile in 1987.',
  'Tunisia', at='tunis', tags='rule reform')
P('Zine El Abidine Ben Ali', 'President of Tunisia', (1936, 2019), 3, 'rule',
  "Ruled Tunisia for 23 years until a street vendor's suicide set off the Arab Spring and he fled to Saudi Arabia.",
  R(1987, 2010, 'President of Tunisia', 'Tunisia', at='tunis'), G(2011, 2019, 'Exile in Saudi Arabia', ('tunis', 2011.03), ('jeddah', 2011.04)))
K('Kais Saied', 'President of Tunisia', (1958, None), 2019, 2026,
  'Law professor elected in 2019 who shut down parliament in 2021 and rules by decree.', 'Tunisia', at='tunis')
K('Ahmed Ben Bella', 'President of Algeria', (1916, 2012), 1962, 1965,
  'Hero of the war of independence, first president of Algeria, overthrown by his own defence minister.', 'Algeria', at='algiers')
K('Houari Boumédiène', 'President of Algeria', (1932, 1978), 1965, 1978,
  'Colonel who overthrew Ben Bella and nationalised Algeria\'s oil and gas.', 'Algeria', at='algiers')
K('Abdelaziz Bouteflika', 'President of Algeria', (1937, 2021), 1999, 2019,
  'Ended the civil war of the 1990s with an amnesty and ruled until mass protests forced him out in 2019.', 'Algeria', at='algiers')
K('Abdelmadjid Tebboune', 'President of Algeria', (1945, None), 2019, 2026,
  'President of Algeria since 2019.', 'Algeria', at='algiers')
K('Idris of Libya', 'King of Libya', (1889, 1983), 1951, 1969,
  'Only king of Libya, overthrown by Gaddafi while abroad for medical treatment in 1969.', 'Libya', at='tripoli')
K('Omar al-Bashir', 'President of Sudan', (1944, None), 1989, 2019,
  'Ruled Sudan for thirty years and was charged with genocide in Darfur by the International Criminal Court; overthrown in 2019.', 'Sudan',
  at='khartoum')
K('Abdel Fattah al-Burhan', 'Leader of Sudan', (1960, None), 2019, 2026,
  'Army chief who took power after Bashir, seized it outright in 2021, and has fought the RSF militia in a civil war since 2023.', 'Sudan',
  at='khartoum')

# ---------- West Africa ----------
NG = ('Nigeria',)
K('Nnamdi Azikiwe', 'President of Nigeria', (1904, 1996), 1960, 1966,
  "'Zik', father of Nigerian nationalism and its first head of state.", *NG, at='lagos')
K('Abubakar Tafawa Balewa', 'Prime minister of Nigeria', (1912, 1966), 1960, 1965,
  "Nigeria's first prime minister, killed in the army coup of January 1966.", *NG, at='lagos')
K('Yakubu Gowon', 'Leader of Nigeria', (1934, None), 1966, 1975,
  "Young officer who led Nigeria through the Biafran war and declared 'no victor, no vanquished'.", *NG, at='lagos')
P('Odumegwu Ojukwu', 'Leader of Biafra', (1933, 2011), 3, 'war rule',
  'Led the breakaway state of Biafra in the civil war of 1967 to 1970, in which a million or more people starved.',
  G(1967, 1970, 'Leader of Biafra', ((7.49, 6.44, 1967.4)), ((7.49, 5.53, 1968.8)), ((7.03, 5.48, 1969.5)), ((-4.03, 5.35, 1970.03))))
P('Olusegun Obasanjo', 'President of Nigeria', (1937, None), 3, 'rule',
  "The first Nigerian military ruler to hand power to civilians, in 1979; he was later elected president twice.",
  R(1976, 1979, 'Leader of Nigeria', *NG, at='lagos'), R(1999, 2007, 'President of Nigeria', *NG, at='abuja'))
K('Ibrahim Babangida', 'Leader of Nigeria', (1941, None), 1985, 1993,
  'General who moved the capital to Abuja and cancelled the election of 1993.', *NG, at='abuja')
K('Sani Abacha', 'Leader of Nigeria', (1943, 1998), 1993, 1998,
  'Brutal dictator who hanged the writer Ken Saro-Wiwa and stole billions.', *NG, at='abuja')
K('Goodluck Jonathan', 'President of Nigeria', (1957, None), 2010, 2015,
  'Became the first Nigerian president to accept defeat at the polls, in 2015.', *NG, at='abuja')
P('Muhammadu Buhari', 'President of Nigeria', (1942, 2025), 3, 'rule',
  'Military ruler in the 1980s who came back thirty years later as the first opposition candidate to win a Nigerian election.',
  R(1983, 1985, 'Leader of Nigeria', *NG, at='lagos'), R(2015, 2023, 'President of Nigeria', *NG, at='abuja'))
K('Bola Tinubu', 'President of Nigeria', (1952, None), 2023, 2026,
  'Former governor of Lagos, elected president in 2023.', *NG, at='abuja')
K('Jerry Rawlings', 'Leader of Ghana', (1947, 2020), 1981, 2000,
  'Air force officer who seized power twice, then turned Ghana into a working democracy.', 'Ghana', at='accra')
K('Nana Akufo-Addo', 'President of Ghana', (1944, None), 2017, 2024,
  'Human-rights lawyer, president of Ghana for eight years.', 'Ghana', at='accra')
P('John Mahama', 'President of Ghana', (1958, None), 3, 'rule',
  'President of Ghana twice, returning in 2025 after eight years out of office.',
  R(2012, 2016, 'President of Ghana', 'Ghana', at='accra'), R(2025, 2026, 'President of Ghana', 'Ghana', at='accra'))
K('Léopold Sédar Senghor', 'President of Senegal', (1906, 2001), 1960, 1980,
  'Poet of black pride who led Senegal for twenty years and became the first African in the French Academy.', 'Senegal', at='dakar',
  tags='rule art')
K('Félix Houphouët-Boigny', 'President of Ivory Coast', (1905, 1993), 1960, 1993,
  'Ruled Ivory Coast for 33 years and built a copy of St Peter\'s in Rome in his home village of Yamoussoukro.', 'Ivory Coast',
  at=(-4.03, 5.35))
K('Ahmed Sékou Touré', 'President of Guinea', (1922, 1984), 1958, 1984,
  'Told de Gaulle that Guinea preferred poverty in freedom to riches in slavery, then ruled it as a dictator for 26 years.', 'Guinea',
  at=(-13.68, 9.51))
K('Thomas Sankara', 'President of Burkina Faso', (1949, 1987), 1983, 1987,
  "Charismatic revolutionary who renamed Upper Volta 'Burkina Faso', land of upright people, and was killed in a coup at 37.",
  'Burkina Faso', at=(-1.52, 12.37), tags='rule reform')
K('Ibrahim Traoré', 'Leader of Burkina Faso', (1988, None), 2022, 2026,
  'Army captain who seized power at 34 and broke with France.', 'Burkina Faso', at=(-1.52, 12.37))
K('William Tubman', 'President of Liberia', (1895, 1971), 1944, 1971,
  'Ruled Liberia for 27 years and opened it to foreign investment.', 'Liberia', at='monrovia')
P('Charles Taylor', 'President of Liberia', (1948, None), 3, 'war rule',
  'Warlord who fought his way to power in Liberia, fuelled the war in Sierra Leone with blood diamonds, and is serving fifty years for war crimes in a British prison.',
  G(1989, 1996, 'The Liberian civil war', ((-8.6, 7.3, 1989.98)), ((-10.35, 6.5, 1990.6)), ((-9.4, 6.99, 1996.0))),
  R(1997, 2003, 'President of Liberia', 'Liberia', at='monrovia'),
  G(2006, 2026, 'Tried for war crimes, imprisoned in Britain', ('monrovia', 2006.24), ('the_hague', 2006.5), ('the_hague', 2013.7),
    ((-1.55, 54.77, 2013.8)), ((-1.55, 54.77, 2026.9))), wiki='Charles Taylor (Liberian politician)')
K('Ellen Johnson Sirleaf', 'President of Liberia', (1938, None), 2006, 2017,
  "Africa's first elected woman head of state, who rebuilt Liberia after its civil wars and shared the Nobel Peace Prize.", 'Liberia',
  at='monrovia')
P('Yaa Asantewaa', 'Queen mother of Ejisu', (1840, 1921), 3, 'war',
  'Queen mother who led the Ashanti rising of 1900 when the British governor demanded to sit on the sacred Golden Stool.',
  G(1900, 1900, 'War of the Golden Stool', 'kumasi'), G(1901, 1921, 'Exile in the Seychelles', (55.45, -4.62)))
P('Prempeh I', 'King of Ashanti', (1870, 1931), 3, 'rule',
  'King of Ashanti who would not fight the British invasion of 1896 to spare his people, and was exiled for nearly thirty years.',
  G(1888, 1895, 'King of Ashanti', 'kumasi'),
  G(1896, 1924, 'Exile in Sierra Leone and the Seychelles', ('kumasi', 1896.05), ((-13.23, 8.48, 1897.0)), ((-13.23, 8.48, 1900.4)),
    ((-17.0, -20.0, 1900.55)), ((20.0, -36.5, 1900.7)), ((40.0, -28.0, 1900.8)), ((55.45, -4.62, 1900.95)), ((55.45, -4.62, 1924.6))),
  G(1925, 1931, 'Back in Kumasi', 'kumasi'))

# ---------- East, Central and Southern Africa ----------
KE, TZ, ZR, ZA = ('Kenya',), ('Tanzania, United Republic of',), ('Zaire',), ('South Africa', 'Union of South Africa')
K('Daniel arap Moi', 'President of Kenya', (1924, 2020), 1978, 2002,
  'Former teacher who ruled Kenya for 24 years, most of them as a one-party state.', *KE, at='nairobi')
K('Mwai Kibaki', 'President of Kenya', (1931, 2022), 2002, 2013,
  'Economist president; the disputed election of 2007 set off weeks of killings.', *KE, at='nairobi')
K('Uhuru Kenyatta', 'President of Kenya', (1961, None), 2013, 2022,
  'Son of Jomo Kenyatta, president for nine years.', *KE, at='nairobi')
K('William Ruto', 'President of Kenya', (1966, None), 2022, 2026,
  'Former chicken seller who became president in 2022.', *KE, at='nairobi')
P('Milton Obote', 'President of Uganda', (1925, 2005), 3, 'rule',
  "Led Uganda to independence, was overthrown by Idi Amin in 1971, and came back to rule again until 1985.",
  R(1962, 1970, 'Leader of Uganda', 'Uganda', at=(32.58, 0.35)), R(1980, 1985, 'President of Uganda', 'Uganda', at=(32.58, 0.35)))
K('Yoweri Museveni', 'President of Uganda', (1944, None), 1986, 2026,
  'Rebel leader who took Kampala in 1986 and has ruled Uganda ever since; sworn in for a seventh term in 2026.', 'Uganda',
  at=(32.58, 0.35))
K('Ali Hassan Mwinyi', 'President of Tanzania', (1925, 2024), 1985, 1995,
  "Nyerere's successor, who opened up Tanzania's economy.", *TZ, at=(39.28, -6.8))
K('Benjamin Mkapa', 'President of Tanzania', (1938, 2020), 1995, 2005,
  'Former journalist, president for ten years.', *TZ, at=(39.28, -6.8))
K('Jakaya Kikwete', 'President of Tanzania', (1950, None), 2005, 2015,
  'President of Tanzania for ten years.', *TZ, at=(39.28, -6.8))
K('John Magufuli', 'President of Tanzania', (1959, 2021), 2015, 2021,
  "'The Bulldozer', who denied that COVID-19 was in Tanzania and died in office.", *TZ, at=(35.74, -6.17))
K('Samia Suluhu Hassan', 'President of Tanzania', (1960, None), 2021, 2026,
  "Tanzania's first woman president, who took over when Magufuli died.", *TZ, at=(35.74, -6.17))
K('Juvénal Habyarimana', 'President of Rwanda', (1937, 1994), 1973, 1994,
  'Hutu general who ruled Rwanda for twenty years; the shooting down of his plane in 1994 was the signal for the genocide.', 'Rwanda',
  at=(30.06, -1.95))
P('Laurent-Désiré Kabila', 'President of Congo', (1939, 2001), 3, 'war rule',
  'Rebel who marched across Congo in 1996 and 1997 to overthrow Mobutu, and was shot dead by his bodyguard.',
  G(1996, 1997, 'March on Kinshasa', ((29.22, -1.68, 1996.8)), ((25.19, 0.52, 1997.2)), ((27.48, -11.66, 1997.28)), ('kinshasa', 1997.38)),
  R(1998, 2001, 'President of Congo', *ZR, at='kinshasa'))
K('Joseph Kabila', 'President of Congo', (1971, None), 2001, 2018,
  'Took over at 29 when his father was killed and ruled for eighteen years.', *ZR, at='kinshasa')
K('Félix Tshisekedi', 'President of Congo', (1963, None), 2019, 2026,
  'President of the Democratic Republic of the Congo since 2019.', *ZR, at='kinshasa')
K('Kenneth Kaunda', 'President of Zambia', (1924, 2021), 1964, 1991,
  "Led Zambia to independence and ruled it for 27 years, waving his white handkerchief.", 'Zambia', at=(28.28, -15.42))
K('Seretse Khama', 'President of Botswana', (1921, 1980), 1966, 1980,
  'Chief exiled by the British for marrying a white Englishwoman, who came back to lead Botswana to independence and prosperity.',
  'Botswana', at=(25.91, -24.65))
K('Ian Smith', 'Prime minister of Rhodesia', (1919, 2007), 1964, 1979,
  "Declared white-ruled Rhodesia independent of Britain in 1965 and fought a long war to keep majority rule out.", 'Rhodesia', 'Zimbabwe',
  at='harare')
K('Emmerson Mnangagwa', 'President of Zimbabwe', (1942, None), 2017, 2026,
  "'The Crocodile', Mugabe's enforcer, who pushed him out in 2017.", 'Zimbabwe', at='harare')
K('Agostinho Neto', 'President of Angola', (1922, 1979), 1975, 1979,
  'Poet and doctor who led Angola to independence from Portugal in 1975.', 'Angola', at='luanda', tags='rule art')
K('José Eduardo dos Santos', 'President of Angola', (1942, 2022), 1979, 2017,
  'Ruled Angola for 38 years through civil war and an oil boom that made his family rich.', 'Angola', at='luanda')
K('João Lourenço', 'President of Angola', (1954, None), 2017, 2026,
  'President of Angola since 2017.', 'Angola', at='luanda')
P('Jonas Savimbi', 'Angolan rebel leader', (1934, 2002), 3, 'war',
  'Led the UNITA rebels in a civil war of 27 years against the Angolan government, until he was killed in battle in 2002.',
  G(1975, 2002, 'UNITA rebel leader', ((15.74, -12.78, 1975.9)), ((20.0, -15.0, 1980.0)), ((16.93, -12.38, 1992.8)), ((18.9, -11.7, 2002.15))))
K('Samora Machel', 'President of Mozambique', (1933, 1986), 1975, 1986,
  'Guerrilla leader who won Mozambique its independence and died in a mysterious plane crash.', 'Mozambique', at=(32.57, -25.97))
K('Paul Biya', 'President of Cameroon', (1933, None), 1982, 2026,
  "Has ruled Cameroon since 1982, much of the time from a Swiss hotel; at 92 he won another term in 2025.", 'Cameroon', at=(11.5, 3.87))
K('Andrianampoinimerina', 'King of Imerina', (1745, 1810), 1787, 1810,
  'United the Merina highlands of Madagascar, saying the sea would be the border of his rice field.', 'Merina Kingdom', 'Madagascar',
  at=(47.52, -18.91))
K('Radama I', 'King of Madagascar', (1793, 1828), 1810, 1828,
  'Conquered most of Madagascar with British help and let missionaries in to write down the Malagasy language.', 'Merina Kingdom',
  'Madagascar', at=(47.52, -18.91))
K('Ranavalona I', 'Queen of Madagascar', (1778, 1861), 1828, 1861,
  'Threw out the missionaries, persecuted Christians and kept the French and British out of Madagascar for 33 years.', 'Merina Kingdom',
  'Madagascar', at=(47.52, -18.91))
P('Ranavalona III', 'Queen of Madagascar', (1861, 1917), 3, 'rule',
  'Last queen of Madagascar, deposed when France conquered the island and exiled to Algiers.',
  R(1883, 1896, 'Queen of Madagascar', 'Madagascar', at=(47.52, -18.91)), G(1897, 1917, 'Exile in Algiers', ('algiers', 1899.0)))
P('Louis Botha', 'Prime minister of South Africa', (1862, 1919), 3, 'war rule',
  'Boer general who fought the British, then made peace and became the first prime minister of the Union of South Africa.',
  G(1899, 1902, 'Boer commander', ((29.78, -28.56, 1899.85)), ((29.4, -28.5, 1900.1)), ('pretoria', 1900.4), ((30.0, -26.5, 1901.5))),
  R(1910, 1919, 'Prime minister of South Africa', *ZA, at='pretoria'))
P('Jan Smuts', 'Prime minister of South Africa', (1870, 1950), 2, 'war rule',
  'Boer guerrilla turned British field marshal, who fought in two world wars, led South Africa twice, and helped write the charter of the United Nations.',
  G(1901, 1902, 'Commando raid into the Cape', ((27.1, -26.7, 1901.55)), ((26.0, -30.7, 1901.75)), ((19.2, -32.0, 1902.0)),
    ((17.88, -29.67, 1902.3))),
  G(1916, 1916, 'East African campaign', ((37.34, -3.35, 1916.2)), ((37.66, -6.82, 1916.65)), ((39.28, -6.8, 1916.7))),
  G(1917, 1918, 'Imperial War Cabinet in London', 'london'),
  R(1919, 1924, 'Prime minister of South Africa', *ZA, at='pretoria'),
  R(1939, 1948, 'Prime minister of South Africa', *ZA, at='pretoria'))
K('J. B. M. Hertzog', 'Prime minister of South Africa', (1866, 1942), 1924, 1939,
  'Boer general who put Afrikaner nationalism in power.', *ZA, at='pretoria')
K('D. F. Malan', 'Prime minister of South Africa', (1874, 1959), 1948, 1954,
  'Won the election of 1948 and began building apartheid.', *ZA, at='pretoria')
K('Hendrik Verwoerd', 'Prime minister of South Africa', (1901, 1966), 1958, 1966,
  'Chief architect of apartheid, stabbed to death in parliament in 1966.', *ZA, at='pretoria')
K('B. J. Vorster', 'Prime minister of South Africa', (1915, 1983), 1966, 1978,
  'Prime minister during the Soweto uprising of 1976.', *ZA, at='pretoria')
K('P. W. Botha', 'President of South Africa', (1916, 2006), 1978, 1989,
  "'The Great Crocodile', who wagged his finger at the world and kept Mandela in prison.", *ZA, at='pretoria')
K('Thabo Mbeki', 'President of South Africa', (1942, None), 1999, 2008,
  "Mandela's successor, who denied that HIV causes AIDS.", *ZA, at='pretoria')
K('Jacob Zuma', 'President of South Africa', (1942, None), 2009, 2018,
  'Former anti-apartheid fighter whose presidency sank in corruption scandals.', *ZA, at='pretoria')
K('Cyril Ramaphosa', 'President of South Africa', (1952, None), 2018, 2026,
  'Mine workers\' union leader who negotiated the end of apartheid, became a billionaire and then president.', *ZA, at='pretoria')

# ---------- the United States ----------
USA = ('United States', 'United States of America')
PUS = 'President of the United States'
K('James Madison', PUS, (1751, 1836), 1809, 1817,
  'Father of the Constitution and fourth president, who fled the White House when the British burned Washington in 1814.', *USA,
  at='washington')
K('James Monroe', PUS, (1758, 1831), 1817, 1825,
  'Warned Europe off the Americas in the Monroe Doctrine of 1823.', *USA, at='washington')
K('John Quincy Adams', PUS, (1767, 1848), 1825, 1829,
  'Son of John Adams; after one term as president he spent seventeen years in Congress fighting slavery.', *USA, at='washington')
K('Martin Van Buren', PUS, (1782, 1862), 1837, 1841,
  'First president born an American citizen, who grew up speaking Dutch; the panic of 1837 wrecked his term.', *USA, at='washington')
P('William Henry Harrison', PUS, (1773, 1841), 3, 'war rule',
  "Frontier general who beat Tecumseh's confederacy at Tippecanoe; he gave the longest inaugural speech in the cold and died a month later.",
  G(1811, 1811, 'Battle of Tippecanoe', ((-87.53, 38.68, 1811.7)), ((-86.84, 40.5, 1811.85))),
  G(1813, 1813, 'Battle of the Thames', ((-83.05, 42.33, 1813.72)), ((-81.98, 42.55, 1813.76))),
  R(1841, 1841, PUS, *USA, at='washington'))
K('John Tyler', PUS, (1790, 1862), 1841, 1845,
  "First vice-president to take over on a president's death; he annexed Texas and later sided with the Confederacy.", *USA,
  at='washington')
K('James K. Polk', PUS, (1795, 1849), 1845, 1849,
  'Took California and the Southwest in the war with Mexico and Oregon by treaty with Britain, growing the country by a third.', *USA,
  at='washington')
P('Zachary Taylor', PUS, (1784, 1850), 3, 'war rule',
  "'Old Rough and Ready', hero of the Mexican War, who died sixteen months into his presidency.",
  G(1846, 1847, 'War with Mexico', ((-97.4, 27.8, 1846.2)), ((-97.48, 26.02, 1846.35)), ((-100.31, 25.67, 1846.72)), ((-101.0, 25.35, 1847.15)),
    ((-101.0, 25.35, 1847.85))),
  R(1849, 1850, PUS, *USA, at='washington'))
K('Millard Fillmore', PUS, (1800, 1874), 1850, 1853,
  'Signed the Compromise of 1850, with its hated Fugitive Slave Act, and sent Commodore Perry to open Japan.', *USA, at='washington')
K('Franklin Pierce', PUS, (1804, 1869), 1853, 1857,
  "His Kansas–Nebraska Act of 1854 set North and South fighting over slavery in 'Bleeding Kansas'.", *USA, at='washington')
K('James Buchanan', PUS, (1791, 1868), 1857, 1861,
  'The only bachelor president, who did nothing as the Southern states began to secede.', *USA, at='washington')
K('Andrew Johnson', PUS, (1808, 1875), 1865, 1869,
  "Lincoln's successor, who fought Congress over Reconstruction and was the first president impeached, surviving by one vote.", *USA,
  at='washington')
K('Rutherford B. Hayes', PUS, (1822, 1893), 1877, 1881,
  'Won the disputed election of 1876 in a deal that ended Reconstruction in the South.', *USA, at='washington')
K('James A. Garfield', PUS, (1831, 1881), 1881, 1881,
  "Shot four months into his term by a disappointed office-seeker; his doctors' probing fingers did as much harm as the bullet.", *USA,
  at='washington')
K('Chester A. Arthur', PUS, (1829, 1886), 1881, 1885,
  'Party machine politician who surprised everyone by reforming the civil service.', *USA, at='washington')
P('Grover Cleveland', PUS, (1837, 1908), 3, 'rule',
  'The only president besides Donald Trump to serve two terms that were not back to back.',
  R(1885, 1889, PUS, *USA, at='washington'), R(1893, 1897, PUS, *USA, at='washington'))
K('Benjamin Harrison', PUS, (1833, 1901), 1889, 1893,
  'Grandson of William Henry Harrison, under whom six western states joined the Union.', *USA, at='washington')
K('William McKinley', PUS, (1843, 1901), 1897, 1901,
  'Won the Spanish–American War of 1898, took the Philippines, Puerto Rico and Guam, and was shot dead in Buffalo.', *USA,
  at='washington')
K('William Howard Taft', PUS, (1857, 1930), 1909, 1913,
  'The only man to serve as both president and chief justice of the United States.', *USA, at='washington')
K('Warren G. Harding', PUS, (1865, 1923), 1921, 1923,
  "Promised a 'return to normalcy' after the war; the Teapot Dome bribes of his cabinet came out after he died in office.", *USA,
  at='washington')
K('Calvin Coolidge', PUS, (1872, 1933), 1923, 1929,
  "'Silent Cal', president through the booming Roaring Twenties.", *USA, at='washington')
K('Herbert Hoover', PUS, (1874, 1964), 1929, 1933,
  'Mining engineer who fed starving Belgium in the First World War, and was president when the crash of 1929 began the Great Depression.',
  *USA, at='washington')
K('Gerald Ford', PUS, (1913, 2006), 1974, 1977,
  'The only president never elected president or vice-president, who pardoned Nixon.', *USA, at='washington')

# ---------- Mexico and Central America ----------
MX = ('Mexico',)
PMX = 'President of Mexico'
P('Agustín de Iturbide', 'Emperor of Mexico', (1783, 1824), 3, 'war rule',
  'Royalist officer who switched sides, won Mexico its independence in 1821 and crowned himself emperor; overthrown, he came back from exile and was shot.',
  G(1820, 1821, 'Plan of Iguala and the march on Mexico City', ('mexico_city', 1820.9), ((-99.54, 18.35, 1821.15)), ('mexico_city', 1821.74)),
  R(1822, 1823, 'Emperor of Mexico', *MX, at='mexico_city'),
  G(1824, 1824, 'Return and execution', ('london', 1824.3), ((-98.2, 23.77, 1824.53)), ((-98.89, 24.03, 1824.55))))
K('Victoriano Huerta', PMX, (1850, 1916), 1913, 1914,
  'General who had President Madero murdered and seized power, until the revolutionaries and the Americans drove him out.', *MX,
  at='mexico_city')
K('Venustiano Carranza', PMX, (1859, 1920), 1914, 1920,
  'Revolutionary chief who gave Mexico its constitution of 1917 and was killed fleeing a revolt.', *MX, at='mexico_city')
K('Álvaro Obregón', PMX, (1880, 1928), 1920, 1924,
  'Revolutionary general who lost an arm fighting Pancho Villa, became president, and was shot at a banquet after winning a second term.',
  *MX, at='mexico_city', tags='rule war')
K('Plutarco Elías Calles', PMX, (1877, 1945), 1924, 1934,
  'Fought the Catholic Cristero rebels and founded the party that ruled Mexico for 71 years, ruling through puppets until 1934.', *MX,
  at='mexico_city')
K('Lázaro Cárdenas', PMX, (1895, 1970), 1934, 1940,
  'Handed land to millions of peasants, took over the foreign oil companies in 1938, and gave refuge to Trotsky and Spanish Republicans.',
  *MX, at='mexico_city', tags='rule reform')
K('Manuel Ávila Camacho', PMX, (1897, 1955), 1940, 1946,
  'Brought Mexico into the Second World War on the Allied side and sent its fighter pilots to the Philippines.', *MX, at='mexico_city')
K('Miguel Alemán Valdés', PMX, (1900, 1983), 1946, 1952,
  'First civilian president after the revolution, who built the national university city and made Acapulco a resort.', *MX,
  at='mexico_city')
K('Adolfo Ruiz Cortines', PMX, (1890, 1973), 1952, 1958,
  'Gave Mexican women the vote in 1953.', *MX, at='mexico_city')
K('Adolfo López Mateos', PMX, (1909, 1969), 1958, 1964,
  'Took over the electricity industry and gave every schoolchild free textbooks.', *MX, at='mexico_city')
K('Gustavo Díaz Ordaz', PMX, (1911, 1979), 1964, 1970,
  "His troops massacred student protesters at Tlatelolco ten days before Mexico City's Olympics of 1968.", *MX, at='mexico_city')
K('Luis Echeverría', PMX, (1922, 2022), 1970, 1976,
  "Posed as a champion of the Third World while his forces waged a 'dirty war' on the left.", *MX, at='mexico_city')
K('José López Portillo', PMX, (1920, 2004), 1976, 1982,
  "Promised to defend the peso 'like a dog' and saw it collapse in the debt crisis of 1982.", *MX, at='mexico_city')
K('Miguel de la Madrid', PMX, (1934, 2012), 1982, 1988,
  'Steered Mexico through the debt crisis and the Mexico City earthquake of 1985.', *MX, at='mexico_city')
K('Carlos Salinas de Gortari', PMX, (1948, None), 1988, 1994,
  'Signed the NAFTA free-trade pact; the Zapatista rising broke out the day it came into force.', *MX, at='mexico_city')
K('Ernesto Zedillo', PMX, (1951, None), 1994, 2000,
  'Let the ruling party lose an election for the first time in 71 years.', *MX, at='mexico_city', tags='rule reform')
K('Vicente Fox', PMX, (1942, None), 2000, 2006,
  'Former Coca-Cola executive, the first opposition president of modern Mexico.', *MX, at='mexico_city')
K('Felipe Calderón', PMX, (1962, None), 2006, 2012,
  'Sent the army against the drug cartels in a war that killed tens of thousands.', *MX, at='mexico_city')
K('Enrique Peña Nieto', PMX, (1966, None), 2012, 2018,
  "Opened Mexico's oil industry to foreign companies.", *MX, at='mexico_city')
K('Andrés Manuel López Obrador', PMX, (1953, None), 2018, 2024,
  'Left-wing populist who held a press conference every weekday morning.', *MX, at='mexico_city')
K('Claudia Sheinbaum', PMX, (1962, None), 2024, 2026,
  "Climate scientist and Mexico's first woman president.", *MX, at='mexico_city')
K('Rafael Trujillo', 'Dictator of the Dominican Republic', (1891, 1961), 1930, 1961,
  'Named the capital after himself and ordered the massacre of thousands of Haitians in 1937; ambushed and shot in 1961.',
  'Dominican Republic', at=(-69.93, 18.47))
HT = ('Haiti',)
K('Henri Christophe', 'King of Haiti', (1767, 1820), 1807, 1820,
  'Former slave and general of the revolution who crowned himself king of northern Haiti and built the vast Citadelle on a mountaintop.',
  *HT, at=(-72.2, 19.76))
K('Alexandre Pétion', 'President of Haiti', (1770, 1818), 1807, 1818,
  'Ruled southern Haiti and gave Bolívar ships and guns on condition that he free the slaves.', *HT, at=(-72.34, 18.54))
K('Jean-Pierre Boyer', 'President of Haiti', (1776, 1850), 1818, 1843,
  'Reunited Haiti, took the Spanish half of the island, and agreed to pay France a crushing price for recognition.', *HT,
  at=(-72.34, 18.54))
K('François Duvalier', 'President of Haiti', (1907, 1971), 1957, 1971,
  "'Papa Doc', the country doctor who ruled Haiti by terror through his Tonton Macoute militia.", *HT, at=(-72.34, 18.54))
K('Jean-Claude Duvalier', 'President of Haiti', (1951, 2014), 1971, 1986,
  "'Baby Doc', president for life at nineteen, driven out in 1986.", *HT, at=(-72.34, 18.54))
P('Jean-Bertrand Aristide', 'President of Haiti', (1953, None), 3, 'rule',
  'Slum priest twice elected president of Haiti and twice overthrown.',
  R(1991, 1991, 'President of Haiti', *HT, at=(-72.34, 18.54)), R(1994, 1996, 'President of Haiti', *HT, at=(-72.34, 18.54)),
  R(2001, 2004, 'President of Haiti', *HT, at=(-72.34, 18.54)))
K('Gerardo Machado', 'President of Cuba', (1871, 1939), 1925, 1933,
  'Elected reformer who turned dictator and was driven out by a general strike in 1933.', 'Cuba', at='havana')
K('Miguel Díaz-Canel', 'President of Cuba', (1960, None), 2018, 2026,
  'First leader of communist Cuba who is not a Castro.', 'Cuba', at='havana')
K('Omar Torrijos', 'Leader of Panama', (1929, 1981), 1968, 1981,
  'Won back the Panama Canal in treaties signed with Jimmy Carter in 1977, and died in a plane crash.', 'Panama', at='panama')
P('Manuel Noriega', 'Leader of Panama', (1934, 2017), 3, 'rule',
  'Military dictator, CIA informant and drug trafficker, seized by American troops who invaded Panama in 1989.',
  R(1983, 1989, 'Leader of Panama', 'Panama', at='panama'),
  G(1990, 1990, 'Captured and flown to Miami', ('panama', 1990.01), ((-80.19, 25.77, 1990.02)), ((-80.19, 25.77, 1990.9))))
K('Anastasio Somoza García', 'Dictator of Nicaragua', (1896, 1956), 1936, 1956,
  'Had the rebel hero Sandino murdered and founded a family dictatorship that lasted 43 years.', 'Nicaragua', at=(-86.25, 12.13))
K('Anastasio Somoza Debayle', 'Dictator of Nicaragua', (1925, 1980), 1967, 1979,
  'Last of the Somozas, overthrown by the Sandinistas in 1979 and killed in exile in Paraguay.', 'Nicaragua', at=(-86.25, 12.13))
P('Daniel Ortega', 'President of Nicaragua', (1945, None), 3, 'rule',
  'Sandinista guerrilla who led the revolutionary government of the 1980s, then came back to rule Nicaragua with his wife.',
  R(1979, 1990, 'Leader of Nicaragua', 'Nicaragua', at=(-86.25, 12.13)), R(2007, 2026, 'President of Nicaragua', 'Nicaragua', at=(-86.25, 12.13)))
K('Jacobo Árbenz', 'President of Guatemala', (1913, 1971), 1951, 1954,
  'Reforming president whose land reform angered the United Fruit Company; overthrown in a CIA-backed coup in 1954.', 'Guatemala',
  at=(-90.51, 14.64))
K('Nayib Bukele', 'President of El Salvador', (1981, None), 2019, 2026,
  "Self-styled 'coolest dictator in the world', who jailed tens of thousands in a war on gangs and made bitcoin legal money.",
  'El Salvador', at=(-89.19, 13.69))

# ---------- South America ----------
BR = ('Brazil', 'Kingdom of Brazil')
PBR = 'President of Brazil'
K('Deodoro da Fonseca', PBR, (1827, 1892), 1889, 1891,
  'Marshal who overthrew Emperor Pedro II in 1889 and became the first president of Brazil.', *BR, at='rio')
K('Floriano Peixoto', PBR, (1839, 1895), 1891, 1894,
  "The 'Iron Marshal', who crushed a naval revolt to save the young republic.", *BR, at='rio')
K('Prudente de Morais', PBR, (1841, 1902), 1894, 1898,
  "Brazil's first civilian president, who sent the army against the backland rebels of Canudos.", *BR, at='rio')
K('Campos Sales', PBR, (1841, 1913), 1898, 1902,
  'Set up the deal between the coffee states that ran the Old Republic.', *BR, at='rio')
K('Rodrigues Alves', PBR, (1848, 1919), 1902, 1906,
  'Rebuilt Rio de Janeiro and stamped out yellow fever, sparking a revolt against compulsory vaccination.', *BR, at='rio')
K('Afonso Pena', PBR, (1847, 1909), 1906, 1909,
  'Pushed railways and immigration, and died in office.', *BR, at='rio')
K('Hermes da Fonseca', PBR, (1855, 1923), 1910, 1914,
  'Marshal whose term began with the Revolt of the Lash, when sailors mutinied against flogging.', *BR, at='rio')
K('Wenceslau Brás', PBR, (1868, 1966), 1914, 1918,
  'Took Brazil into the First World War in 1917.', *BR, at='rio', wiki='Venceslau Brás')
K('Epitácio Pessoa', PBR, (1865, 1942), 1919, 1922,
  'Was elected president while away at the Versailles peace conference.', *BR, at='rio')
K('Artur Bernardes', PBR, (1875, 1955), 1922, 1926,
  'Ruled almost his whole term under a state of siege, fighting army revolts.', *BR, at='rio')
K('Washington Luís', PBR, (1869, 1957), 1926, 1930,
  'Last president of the Old Republic, overthrown by Getúlio Vargas in 1930.', *BR, at='rio')
P('Getúlio Vargas', PBR, (1882, 1954), 2, 'rule',
  'Ruled Brazil for 18 years as revolutionary, dictator and elected president, and shot himself in the presidential palace in 1954 rather than be overthrown.',
  R(1930, 1945, PBR, *BR, at='rio'), R(1951, 1954, PBR, *BR, at='rio'))
K('Eurico Gaspar Dutra', PBR, (1883, 1974), 1946, 1951,
  'General who banned gambling and the Communist Party.', *BR, at='rio')
K('Juscelino Kubitschek', PBR, (1902, 1976), 1956, 1961,
  "Promised 'fifty years of progress in five' and built the new capital, Brasília.", *BR, at='brasilia')
K('João Goulart', PBR, (1919, 1976), 1961, 1964,
  'Left-leaning president overthrown by the army in 1964.', *BR, at='brasilia')
K('Humberto Castelo Branco', PBR, (1897, 1967), 1964, 1967,
  'First general of the military regime.', *BR, at='brasilia')
K('Artur da Costa e Silva', PBR, (1899, 1969), 1967, 1969,
  'Closed Congress and suspended civil rights with Institutional Act No. 5 in 1968.', *BR, at='brasilia')
K('Emílio Garrastazu Médici', PBR, (1905, 1985), 1969, 1974,
  "Ruled in the years of the 'economic miracle' and the worst torture.", *BR, at='brasilia')
K('Ernesto Geisel', PBR, (1907, 1996), 1974, 1979,
  'Began the slow opening of the military regime.', *BR, at='brasilia')
K('João Figueiredo', PBR, (1918, 1999), 1979, 1985,
  'Last military president, who granted an amnesty and said he preferred the smell of horses to the smell of the people.', *BR,
  at='brasilia')
K('José Sarney', PBR, (1930, None), 1985, 1990,
  'First civilian president after 21 years of military rule.', *BR, at='brasilia')
K('Fernando Collor de Mello', PBR, (1949, None), 1990, 1992,
  "Froze everyone's savings to fight inflation and resigned as he was being impeached for corruption.", *BR, at='brasilia')
K('Itamar Franco', PBR, (1930, 2011), 1992, 1994,
  'Took over from Collor and launched the plan that ended runaway inflation.', *BR, at='brasilia')
K('Fernando Henrique Cardoso', PBR, (1931, None), 1995, 2002,
  "Sociologist who ended Brazil's runaway inflation with a new currency, the real.", *BR, at='brasilia', tags='rule reform')
K('Dilma Rousseff', PBR, (1947, None), 2011, 2016,
  "Former guerrilla tortured under the dictatorship, Brazil's first woman president, impeached in 2016.", *BR, at='brasilia')
K('Michel Temer', PBR, (1940, None), 2016, 2018,
  "Rousseff's vice-president, who took over when she was removed.", *BR, at='brasilia')
K('Jair Bolsonaro', PBR, (1955, None), 2019, 2022,
  'Former army captain who was later sentenced to 27 years in prison for plotting a coup to stay in power.', *BR, at='brasilia')
AR = ('Argentina',)
PAR = 'President of Argentina'
K('Bartolomé Mitre', PAR, (1821, 1906), 1862, 1868,
  'First president of a united Argentina, who led it into the Paraguayan War and founded the newspaper La Nación.', *AR,
  at='buenos_aires')
K('Domingo Faustino Sarmiento', PAR, (1811, 1888), 1868, 1874,
  'Writer and teacher who built schools across Argentina and wrote Facundo, a classic of Latin American literature.', *AR,
  at='buenos_aires', tags='rule mind')
K('Nicolás Avellaneda', PAR, (1837, 1885), 1874, 1880,
  'Made Buenos Aires the federal capital after a short civil war in 1880.', *AR, at='buenos_aires')
P('Julio Argentino Roca', PAR, (1843, 1914), 3, 'war rule',
  'General whose Conquest of the Desert took Patagonia from its Indigenous peoples; twice president.',
  G(1879, 1879, 'Conquest of the Desert', ('buenos_aires', 1879.3), ((-65.6, -39.27, 1879.4)), ((-65.6, -39.27, 1879.5))),
  R(1880, 1886, PAR, *AR, at='buenos_aires'), R(1898, 1904, PAR, *AR, at='buenos_aires'))
K('Miguel Juárez Celman', PAR, (1844, 1909), 1886, 1890,
  'Fell in the Revolution of the Park of 1890 amid a financial crash.', *AR, at='buenos_aires')
K('Carlos Pellegrini', PAR, (1846, 1906), 1890, 1892,
  "Rescued the country's finances after the crash of 1890.", *AR, at='buenos_aires')
K('Roque Sáenz Peña', PAR, (1851, 1914), 1910, 1914,
  'Gave Argentine men the secret and compulsory vote in 1912.', *AR, at='buenos_aires', tags='rule reform')
P('Hipólito Yrigoyen', PAR, (1852, 1933), 3, 'rule',
  "First president elected by secret ballot, overthrown in Argentina's first military coup in 1930.",
  R(1916, 1922, PAR, *AR, at='buenos_aires'), R(1928, 1930, PAR, *AR, at='buenos_aires'))
K('Marcelo T. de Alvear', PAR, (1868, 1942), 1922, 1928,
  "Wealthy aristocrat who presided over Argentina's last years of prosperity before the Depression.", *AR, at='buenos_aires')
K('José Félix Uriburu', PAR, (1868, 1932), 1930, 1932,
  'General who led the coup of 1930.', *AR, at='buenos_aires')
K('Agustín P. Justo', PAR, (1876, 1943), 1932, 1938,
  "President in the 'Infamous Decade' of rigged elections.", *AR, at='buenos_aires')
K('Roberto M. Ortiz', PAR, (1886, 1942), 1938, 1941,
  'Tried to end the electoral fraud but went blind from diabetes.', *AR, at='buenos_aires')
K('Edelmiro Farrell', PAR, (1887, 1980), 1944, 1946,
  'General in whose military government Colonel Juan Perón rose to power.', *AR, at='buenos_aires')
K('Pedro Eugenio Aramburu', PAR, (1903, 1970), 1955, 1958,
  'General who overthrew Perón and was later kidnapped and killed by the Montoneros guerrillas.', *AR, at='buenos_aires')
K('Arturo Frondizi', PAR, (1908, 1995), 1958, 1962,
  'Developer president overthrown by the army in 1962.', *AR, at='buenos_aires')
K('Arturo Illia', PAR, (1900, 1983), 1963, 1966,
  'Honest country doctor overthrown by the army in 1966.', *AR, at='buenos_aires')
K('Juan Carlos Onganía', PAR, (1914, 1995), 1966, 1970,
  "General whose police beat professors and students in the 'Night of the Long Batons'.", *AR, at='buenos_aires')
K('Alejandro Lanusse', PAR, (1918, 1996), 1971, 1973,
  'General who let Perón come back from exile.', *AR, at='buenos_aires')
K('Isabel Perón', PAR, (1931, None), 1974, 1976,
  "Perón's third wife and vice-president, the world's first woman to hold the title of president, overthrown in 1976.", *AR,
  at='buenos_aires')
K('Jorge Rafael Videla', PAR, (1925, 2013), 1976, 1981,
  "Led the junta of the 'Dirty War', in which some 30,000 people were made to disappear.", *AR, at='buenos_aires')
K('Leopoldo Galtieri', PAR, (1926, 2003), 1981, 1982,
  'Invaded the Falkland Islands in 1982 and fell when Britain took them back.', *AR, at='buenos_aires', tags='rule war')
K('Raúl Alfonsín', PAR, (1927, 2009), 1983, 1989,
  'Brought back democracy and put the junta leaders on trial.', *AR, at='buenos_aires', tags='rule reform')
K('Carlos Menem', PAR, (1930, 2021), 1989, 1999,
  'Tied the peso to the dollar and sold off state companies.', *AR, at='buenos_aires')
K('Fernando de la Rúa', PAR, (1937, 2019), 1999, 2001,
  "Fled the presidential palace by helicopter as Argentina's economy collapsed in December 2001.", *AR, at='buenos_aires')
K('Néstor Kirchner', PAR, (1950, 2010), 2003, 2007,
  "Led Argentina's recovery from the crash of 2001.", *AR, at='buenos_aires')
K('Cristina Fernández de Kirchner', PAR, (1953, None), 2007, 2015,
  "Néstor Kirchner's widow and successor, later convicted of corruption and put under house arrest.", *AR, at='buenos_aires')
K('Mauricio Macri', PAR, (1959, None), 2015, 2019,
  'Former president of the Boca Juniors football club.', *AR, at='buenos_aires')
K('Alberto Fernández', PAR, (1959, None), 2019, 2023,
  'President through the pandemic and soaring inflation.', *AR, at='buenos_aires')
K('Javier Milei', PAR, (1970, None), 2023, 2026,
  'Libertarian economist who campaigned with a chainsaw to cut the state down to size.', *AR, at='buenos_aires')
VE = ('Venezuela',)
P('José Antonio Páez', 'President of Venezuela', (1790, 1873), 3, 'war rule',
  "Plainsman cavalry chief of the independence war who became Venezuela's first president.",
  R(1830, 1835, 'President of Venezuela', *VE, at='caracas'), R(1839, 1843, 'President of Venezuela', *VE, at='caracas'),
  R(1861, 1863, 'Dictator of Venezuela', *VE, at='caracas'))
K('Antonio Guzmán Blanco', 'President of Venezuela', (1829, 1899), 1870, 1887,
  'Ruled Venezuela for nearly two decades, often from Paris, and covered Caracas with statues of himself.', *VE, at='caracas')
K('Cipriano Castro', 'President of Venezuela', (1858, 1924), 1899, 1908,
  'His unpaid debts brought British, German and Italian warships to blockade Venezuela in 1902.', *VE, at='caracas')
K('Juan Vicente Gómez', 'Dictator of Venezuela', (1857, 1935), 1908, 1935,
  'Ruled Venezuela for 27 years and grew rich as oil was found.', *VE, at='caracas')
K('Marcos Pérez Jiménez', 'Dictator of Venezuela', (1914, 2001), 1952, 1958,
  'Military dictator who built grand highways and housing blocks with oil money.', *VE, at='caracas')
K('Rómulo Betancourt', 'President of Venezuela', (1908, 1981), 1959, 1964,
  'Father of Venezuelan democracy, who helped found OPEC.', *VE, at='caracas')
P('Carlos Andrés Pérez', 'President of Venezuela', (1922, 2010), 3, 'rule',
  'Nationalised the oil industry in his first term; riots and two coup attempts, one led by Hugo Chávez, shook his second.',
  R(1974, 1979, 'President of Venezuela', *VE, at='caracas'), R(1989, 1993, 'President of Venezuela', *VE, at='caracas'))
P('Nicolás Maduro', 'President of Venezuela', (1962, None), 3, 'rule',
  "Bus driver who became Chávez's heir; his rule saw the economy collapse and millions flee, until American forces seized him in January 2026.",
  R(2013, 2025, 'President of Venezuela', *VE, at='caracas'),
  G(2026, 2026, 'Seized and flown to New York', ('caracas', 2026.0), ('new_york', 2026.01), ('new_york', 2026.9)))
K('Delcy Rodríguez', 'Acting president of Venezuela', (1969, None), 2026, 2026,
  "Maduro's vice-president, who took over after his capture.", *VE, at='caracas')
CO = ('Colombia',)
P('Francisco de Paula Santander', 'President of New Granada', (1792, 1840), 3, 'war rule',
  "Bolívar's general and rival, who ran Gran Colombia while Bolívar fought in Peru and later led the country that became Colombia.",
  R(1819, 1826, 'Vice-president of Gran Colombia', *CO, at='bogota'), R(1832, 1837, 'President of New Granada', *CO, at='bogota'))
K('Rafael Núñez', 'President of Colombia', (1825, 1894), 1880, 1894,
  "Gave Colombia the constitution of 1886 and wrote the words of its national anthem.", *CO, at='bogota')
P('Jorge Eliécer Gaitán', 'Colombian Liberal leader', (1903, 1948), 3, 'reform',
  "Spellbinding champion of the poor whose murder in 1948 set Bogotá ablaze and began the decade of killing called 'La Violencia'.",
  G(1946, 1948, 'Liberal leader', 'bogota'))
K('Gustavo Rojas Pinilla', 'President of Colombia', (1900, 1975), 1953, 1957,
  'General who seized power promising to end La Violencia.', *CO, at='bogota')
K('Álvaro Uribe', 'President of Colombia', (1952, None), 2002, 2010,
  'Hard-line president who drove back the FARC guerrillas.', *CO, at='bogota')
K('Juan Manuel Santos', 'President of Colombia', (1951, None), 2010, 2018,
  'Made peace with the FARC and won the Nobel Peace Prize in 2016.', *CO, at='bogota')
K('Gustavo Petro', 'President of Colombia', (1960, None), 2022, 2026,
  "Former guerrilla and Colombia's first left-wing president.", *CO, at='bogota')
PE = ('Peru',)
P('Ramón Castilla', 'President of Peru', (1797, 1867), 3, 'rule reform',
  "Freed Peru's slaves and ended the tribute paid by its Indigenous people, paying for it with money from guano.",
  R(1845, 1851, 'President of Peru', *PE, at='lima'), R(1855, 1862, 'President of Peru', *PE, at='lima'))
P('Augusto B. Leguía', 'President of Peru', (1863, 1932), 3, 'rule',
  "Twice president, the second time for eleven years as a dictator, until he was overthrown in 1930.",
  R(1908, 1912, 'President of Peru', *PE, at='lima'), R(1919, 1930, 'President of Peru', *PE, at='lima'))
K('Juan Velasco Alvarado', 'President of Peru', (1910, 1977), 1968, 1975,
  'General who seized power and handed the great estates to the peasants.', *PE, at='lima', tags='rule reform')
P('Alberto Fujimori', 'President of Peru', (1938, 2024), 3, 'rule',
  "Crushed the Shining Path guerrillas and runaway inflation, shut down Congress, and fled to Japan when his spy chief was caught bribing; later jailed for death-squad killings.",
  R(1990, 1999, 'President of Peru', *PE, at='lima'),
  G(2000, 2005, 'Flight to Japan', ('lima', 2000.86), ('tokyo', 2000.88), ('tokyo', 2005.8)))
K('Keiko Fujimori', 'President of Peru', (1975, None), 2026, 2026,
  "Alberto Fujimori's daughter, elected president of Peru on her fourth try in 2026.", *PE, at='lima')
CL = ('Chile',)
K('José Manuel Balmaceda', 'President of Chile', (1840, 1891), 1886, 1891,
  'Lost a civil war against Congress in 1891 and shot himself in the Argentine embassy.', *CL, at='santiago')
P('Arturo Alessandri', 'President of Chile', (1868, 1950), 3, 'rule',
  "'The Lion of Tarapacá', who gave Chile a new constitution in 1925.",
  R(1920, 1925, 'President of Chile', *CL, at='santiago'), R(1932, 1938, 'President of Chile', *CL, at='santiago'))
P('Carlos Ibáñez del Campo', 'President of Chile', (1877, 1960), 3, 'rule',
  'Army officer who ruled Chile as a dictator in the 1920s and was elected president again in 1952.',
  R(1927, 1931, 'President of Chile', *CL, at='santiago'), R(1952, 1958, 'President of Chile', *CL, at='santiago'))
K('Eduardo Frei Montalva', 'President of Chile', (1911, 1982), 1964, 1970,
  "Christian Democrat whose 'revolution in liberty' began land reform.", *CL, at='santiago')
K('Patricio Aylwin', 'President of Chile', (1918, 2016), 1990, 1994,
  'First president after Pinochet, who set up a commission on the crimes of the dictatorship.', *CL, at='santiago')
K('Ricardo Lagos', 'President of Chile', (1938, None), 2000, 2006,
  'Socialist who once wagged his finger at Pinochet on live television.', *CL, at='santiago')
P('Michelle Bachelet', 'President of Chile', (1951, None), 3, 'rule',
  "Doctor once tortured under Pinochet, Chile's first woman president.",
  R(2006, 2010, 'President of Chile', *CL, at='santiago'), R(2014, 2018, 'President of Chile', *CL, at='santiago'))
P('Sebastián Piñera', 'President of Chile', (1949, 2024), 3, 'rule',
  'Billionaire president who saw 33 trapped miners rescued in 2010; he died in a helicopter crash.',
  R(2010, 2014, 'President of Chile', *CL, at='santiago'), R(2018, 2022, 'President of Chile', *CL, at='santiago'))
K('Gabriel Boric', 'President of Chile', (1986, None), 2022, 2026,
  'Former student protest leader, president at 36.', *CL, at='santiago')
K('José Antonio Kast', 'President of Chile', (1966, None), 2026, 2026,
  "Hard-right lawyer sworn in in March 2026, Chile's most conservative leader since Pinochet.", *CL, at='santiago')
K('Víctor Paz Estenssoro', 'President of Bolivia', (1907, 2001), 1952, 1964,
  "Led Bolivia's revolution of 1952, which gave land to the peasants and the vote to all.", 'Bolivia', at=(-68.15, -16.5))
K('Evo Morales', 'President of Bolivia', (1959, None), 2006, 2019,
  "Coca farmers' leader, Bolivia's first Indigenous president.", 'Bolivia', at=(-68.15, -16.5))
K('Rodrigo Paz', 'President of Bolivia', (1967, None), 2025, 2026,
  'Son of a former president, elected in 2025 to end nearly twenty years of left-wing rule.', 'Bolivia', at=(-68.15, -16.5),
  wiki='Rodrigo Paz Pereira')
P('Gabriel García Moreno', 'President of Ecuador', (1821, 1875), 3, 'rule faith',
  'Catholic strongman who dedicated Ecuador to the Sacred Heart of Jesus and was hacked to death on the steps of his palace.',
  R(1861, 1865, 'President of Ecuador', 'Ecuador', at='quito'), R(1869, 1875, 'President of Ecuador', 'Ecuador', at='quito'))
P('Eloy Alfaro', 'President of Ecuador', (1842, 1912), 3, 'rule reform',
  'Liberal revolutionary who built the railway from Quito to Guayaquil and was lynched by a mob in 1912.',
  R(1895, 1901, 'President of Ecuador', 'Ecuador', at='quito'), R(1906, 1911, 'President of Ecuador', 'Ecuador', at='quito'))
K('Rafael Correa', 'President of Ecuador', (1963, None), 2007, 2017,
  'Left-wing economist who ruled Ecuador for ten years.', 'Ecuador', at='quito')
K('Daniel Noboa', 'President of Ecuador', (1987, None), 2023, 2026,
  'Banana heir elected at 35, who declared war on the drug gangs.', 'Ecuador', at='quito')
P('José Batlle y Ordóñez', 'President of Uruguay', (1856, 1929), 3, 'rule reform',
  "Built South America's first welfare state in Uruguay, with an eight-hour day and divorce at the wife's request.",
  R(1903, 1907, 'President of Uruguay', 'Uruguay', at='montevideo'), R(1911, 1915, 'President of Uruguay', 'Uruguay', at='montevideo'))
K('José Mujica', 'President of Uruguay', (1935, 2025), 2010, 2015,
  'Former guerrilla who gave most of his pay away and drove an old Volkswagen Beetle.', 'Uruguay', at='montevideo')
K('José Gaspar Rodríguez de Francia', 'Dictator of Paraguay', (1766, 1840), 1814, 1840,
  "'El Supremo', who sealed Paraguay off from the world for 26 years.", 'Paraguay', at=(-57.58, -25.28))
K('Alfredo Stroessner', 'Dictator of Paraguay', (1912, 2006), 1954, 1989,
  'Ruled Paraguay for 35 years and sheltered Nazi fugitives.', 'Paraguay', at=(-57.58, -25.28))

# ---------- Canada, Australia and New Zealand ----------
CA, AU, NZ = ('Canada',), ('Australia',), ('New Zealand',)
PCA, PAU, PNZ = 'Prime minister of Canada', 'Prime minister of Australia', 'Prime minister of New Zealand'
P('John A. Macdonald', PCA, (1815, 1891), 2, 'rule',
  'First prime minister of Canada, who brought the provinces together in 1867 and built the railway to the Pacific.',
  R(1867, 1873, PCA, *CA, at='ottawa'), R(1878, 1891, PCA, *CA, at='ottawa'))
K('Alexander Mackenzie', PCA, (1822, 1892), 1873, 1878,
  'Scottish stonemason turned prime minister.', *CA, at='ottawa', wiki='Alexander Mackenzie (politician)')
K('Wilfrid Laurier', PCA, (1841, 1919), 1896, 1911,
  'First French-Canadian prime minister.', *CA, at='ottawa')
K('Robert Borden', PCA, (1854, 1937), 1911, 1920,
  'Led Canada through the First World War, in which its troops took Vimy Ridge.', *CA, at='ottawa')
P('William Lyon Mackenzie King', PCA, (1874, 1950), 3, 'rule',
  "Canada's longest-serving prime minister, who secretly held séances to talk with his dead mother.",
  R(1921, 1930, PCA, *CA, at='ottawa'), R(1935, 1948, PCA, *CA, at='ottawa'))
K('R. B. Bennett', PCA, (1870, 1947), 1930, 1935,
  'Prime minister in the depths of the Depression.', *CA, at='ottawa')
K('Louis St. Laurent', PCA, (1882, 1973), 1948, 1957,
  'Took Canada into NATO and brought in Newfoundland.', *CA, at='ottawa')
K('John Diefenbaker', PCA, (1895, 1979), 1957, 1963,
  'Gave Canada its first bill of rights in 1960.', *CA, at='ottawa')
K('Lester B. Pearson', PCA, (1897, 1972), 1963, 1968,
  'Won the Nobel Peace Prize for inventing UN peacekeeping in the Suez crisis, and gave Canada its maple leaf flag.', *CA, at='ottawa')
P('Pierre Trudeau', PCA, (1919, 2000), 3, 'rule reform',
  "Brought home Canada's constitution with a charter of rights in 1982.",
  R(1968, 1979, PCA, *CA, at='ottawa'), R(1980, 1984, PCA, *CA, at='ottawa'))
K('Brian Mulroney', PCA, (1939, 2024), 1984, 1993,
  'Signed free trade with the United States.', *CA, at='ottawa')
K('Jean Chrétien', PCA, (1934, None), 1993, 2003,
  'Narrowly kept Quebec in Canada in the referendum of 1995 and kept Canada out of the Iraq War.', *CA, at='ottawa')
K('Paul Martin', PCA, (1938, None), 2003, 2006,
  'Prime minister when Canada made same-sex marriage legal in 2005.', *CA, at='ottawa')
K('Stephen Harper', PCA, (1959, None), 2006, 2015,
  'Conservative prime minister for nine years.', *CA, at='ottawa')
K('Justin Trudeau', PCA, (1971, None), 2015, 2025,
  "Pierre Trudeau's son, prime minister for nine years.", *CA, at='ottawa')
K('Mark Carney', PCA, (1965, None), 2025, 2026,
  'Former head of the Bank of Canada and the Bank of England.', *CA, at='ottawa')
K('Edmund Barton', PAU, (1849, 1920), 1901, 1903,
  'First prime minister of Australia.', *AU, at='melbourne')
P('Alfred Deakin', PAU, (1856, 1919), 3, 'rule',
  'Three times prime minister, who shaped the new federation.',
  R(1903, 1904, PAU, *AU, at='melbourne'), R(1905, 1908, PAU, *AU, at='melbourne'), R(1909, 1910, PAU, *AU, at='melbourne'))
P('Andrew Fisher', PAU, (1862, 1928), 3, 'rule',
  "Scottish coal miner who promised that Australia would fight in the First World War 'to our last man and our last shilling'.",
  R(1910, 1913, PAU, *AU, at='melbourne'), R(1914, 1915, PAU, *AU, at='melbourne'))
K('Billy Hughes', PAU, (1862, 1952), 1915, 1923,
  "'The Little Digger', who led Australia through the First World War and twice failed to bring in conscription.", *AU, at='melbourne')
K('Stanley Bruce', PAU, (1883, 1967), 1923, 1929,
  'Prime minister when the parliament moved to Canberra in 1927.', *AU, at='canberra')
K('James Scullin', PAU, (1876, 1953), 1929, 1932,
  'Took office days before the Wall Street crash.', *AU, at='canberra')
K('Joseph Lyons', PAU, (1879, 1939), 1932, 1939,
  'The only prime minister from Tasmania, who died in office.', *AU, at='canberra')
P('Robert Menzies', PAU, (1894, 1978), 3, 'rule',
  "Australia's longest-serving prime minister.",
  R(1939, 1941, PAU, *AU, at='canberra'), R(1949, 1966, PAU, *AU, at='canberra'))
K('John Curtin', PAU, (1885, 1945), 1941, 1945,
  'Turned to America for help after Singapore fell, and died weeks before the war ended.', *AU, at='canberra')
K('Ben Chifley', PAU, (1885, 1951), 1945, 1949,
  'Former train driver who launched mass immigration and the Snowy Mountains scheme.', *AU, at='canberra')
K('Harold Holt', PAU, (1908, 1967), 1966, 1967,
  'Vanished while swimming in rough surf in 1967 and was never found.', *AU, at='canberra')
K('Gough Whitlam', PAU, (1916, 2014), 1972, 1975,
  'Brought in free universities and public health care, and was dismissed by the governor-general in 1975.', *AU, at='canberra',
  tags='rule reform')
K('Malcolm Fraser', PAU, (1930, 2015), 1975, 1983,
  'Took over when Whitlam was dismissed.', *AU, at='canberra')
K('Bob Hawke', PAU, (1929, 2019), 1983, 1991,
  "Union leader and record-setting beer drinker who opened up Australia's economy.", *AU, at='canberra')
K('Paul Keating', PAU, (1944, None), 1991, 1996,
  'Sharp-tongued treasurer turned prime minister.', *AU, at='canberra')
K('John Howard', PAU, (1939, None), 1996, 2007,
  'Brought in strict gun laws after the Port Arthur massacre of 1996.', *AU, at='canberra')
P('Kevin Rudd', PAU, (1957, None), 3, 'rule',
  "Apologised in 2008 to the Stolen Generations of Aboriginal children taken from their families.",
  R(2007, 2010, PAU, *AU, at='canberra'), R(2013, 2013, PAU, *AU, at='canberra'))
K('Julia Gillard', PAU, (1961, None), 2010, 2013,
  "Australia's first woman prime minister.", *AU, at='canberra')
K('Tony Abbott', PAU, (1957, None), 2013, 2015,
  'Conservative prime minister for two years.', *AU, at='canberra')
K('Malcolm Turnbull', PAU, (1954, None), 2015, 2018,
  'Lawyer and banker who won the Spycatcher case against the British government.', *AU, at='canberra')
K('Scott Morrison', PAU, (1968, None), 2018, 2022,
  'Prime minister through the bushfires of 2019 and the pandemic.', *AU, at='canberra')
K('Anthony Albanese', PAU, (1963, None), 2022, 2026,
  'Raised by a single mother in public housing, prime minister since 2022.', *AU, at='canberra')
K('Richard Seddon', PNZ, (1845, 1906), 1893, 1906,
  "New Zealand's longest-serving prime minister, in whose first year it became the first country where women could vote.", *NZ,
  at='wellington')
K('Michael Joseph Savage', PNZ, (1872, 1940), 1935, 1940,
  "Built New Zealand's welfare state.", *NZ, at='wellington')
K('Peter Fraser', PNZ, (1884, 1950), 1940, 1949,
  'Led New Zealand through the Second World War.', *NZ, at='wellington')
K('David Lange', PNZ, (1942, 2005), 1984, 1989,
  'Made New Zealand nuclear-free.', *NZ, at='wellington')
K('Helen Clark', PNZ, (1950, None), 1999, 2008,
  'Prime minister for nine years, then head of the UN Development Programme.', *NZ, at='wellington')
K('John Key', PNZ, (1961, None), 2008, 2016,
  'Currency trader turned prime minister.', *NZ, at='wellington')
K('Jacinda Ardern', PNZ, (1980, None), 2017, 2023,
  'Led New Zealand through the Christchurch mosque shootings of 2019 and the pandemic.', *NZ, at='wellington')
K('Christopher Luxon', PNZ, (1970, None), 2023, 2026,
  'Former head of Air New Zealand, prime minister since 2023.', *NZ, at='wellington')

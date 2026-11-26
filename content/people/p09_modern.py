from _lib import P, R, G

USA = ('United States',)
UK = ('United Kingdom',)
SOV = ('USSR',)
NK = ("Korea, Democratic People's Republic of", 'Korea (USSR)')
SK = ('Korea, Republic of', 'Korea (USA)')
PRES = 'President of the United States'

# ---------- the Cold War: America and Europe ----------
P('Harry S. Truman', 'Thirty-third President of the United States', (1884, 1972), 2, 'rule war',
  'Ordered the atomic bombs on Japan, rebuilt Europe with the Marshall Plan and fought the Korean War.',
  R(1945, 1952, PRES, *USA, at='washington'))
P('Clement Attlee', 'British prime minister', (1883, 1967), 3, 'rule reform',
  'Beat Churchill in 1945, founded the National Health Service and let India go.',
  R(1945, 1951, 'Prime minister', *UK, at='london'))
P('Konrad Adenauer', 'First chancellor of West Germany', (1876, 1967), 3, 'rule',
  'Rebuilt West Germany from the ruins as a democracy tied to the West.',
  R(1949, 1963, 'Chancellor of West Germany', 'West Germany', 'Germany (UK)', at='bonn'))
P('John F. Kennedy', 'Thirty-fifth President of the United States', (1917, 1963), 1, 'rule',
  'Faced down the Soviet Union over its missiles in Cuba in 1962, started the race to the Moon and was shot in Dallas.',
  R(1961, 1962, PRES, *USA, at='washington'),
  G(1963, 1963, 'Berlin, then Dallas', ('washington', 1963.0), ('washington', 1963.45), ('berlin', 1963.48), ((-6.95, 52.39, 1963.49)), ('washington', 1963.5), ('dallas', 1963.89)))
P('Lyndon B. Johnson', 'Thirty-sixth President of the United States', (1908, 1973), 3, 'rule reform',
  'Signed the Civil Rights Act and sent half a million soldiers to Vietnam.',
  R(1963, 1968, PRES, *USA, at='washington'))
P('Richard Nixon', 'Thirty-seventh President of the United States', (1913, 1994), 2, 'rule',
  "Opened relations with Mao's China, pulled America out of Vietnam and resigned over the Watergate scandal.",
  R(1969, 1971, PRES, *USA, at='washington'),
  G(1972, 1972, 'To Beijing and Moscow', ('washington', 1972.0), ('washington', 1972.13), ('beijing', 1972.15), ('hangzhou', 1972.16), ('shanghai', 1972.165), ('washington', 1972.18),
    ('washington', 1972.37), ('moscow', 1972.39), ('washington', 1972.42)),
  R(1973, 1974, PRES, *USA, at='washington'))
P('Jimmy Carter', 'Thirty-ninth President of the United States', (1924, 2024), 3, 'rule',
  'Brokered peace between Egypt and Israel at Camp David in 1978.',
  R(1977, 1980, PRES, *USA, at='washington'))
P('Ronald Reagan', 'Fortieth President of the United States', (1911, 2004), 2, 'rule',
  'Film actor turned president who out-spent the Soviets on arms, then made peace with Gorbachev.',
  R(1981, 1988, PRES, *USA, at='washington'))
P('George H. W. Bush', 'Forty-first President of the United States', (1924, 2018), 3, 'rule war',
  'Saw out the Cold War and led the coalition that drove Iraq out of Kuwait in 1991.',
  R(1989, 1992, PRES, *USA, at='washington'))
P('Bill Clinton', 'Forty-second President of the United States', (1946, None), 3, 'rule',
  'Led America through the boom of the 1990s and the wars in the former Yugoslavia.',
  R(1993, 2000, PRES, *USA, at='washington'))
P('George W. Bush', 'Forty-third President of the United States', (1946, None), 2, 'rule war',
  'President on 11 September 2001, who led the wars in Afghanistan and Iraq.',
  R(2001, 2008, PRES, *USA, at='washington'))
P('Barack Obama', 'Forty-fourth President of the United States', (1961, None), 2, 'rule',
  'The first black president of the United States.',
  R(2009, 2016, PRES, *USA, at='washington'))
P('Donald Trump', 'Forty-fifth and forty-seventh President of the United States', (1946, None), 2, 'rule',
  'Property developer and television star who won the presidency in 2016 and again in 2024.',
  R(2017, 2020, PRES, *USA, at='washington'), R(2025, 2026, PRES, *USA, at='washington'))
P('Joe Biden', 'Forty-sixth President of the United States', (1942, None), 3, 'rule',
  "Beat Trump in 2020 and backed Ukraine against Russia's invasion.",
  R(2021, 2024, PRES, *USA, at='washington'))
P('Martin Luther King Jr.', 'Leader of the civil rights movement', (1929, 1968), 1, 'reform faith',
  "Baptist minister who led the non-violent fight against segregation ('I have a dream'); shot in Memphis.",
  G(1954, 1959, 'The Montgomery bus boycott', 'montgomery'),
  G(1960, 1968, 'The civil rights movement', ('atlanta', 1960.1), ('birmingham_al', 1963.3), ('washington', 1963.66), ('atlanta', 1964.0), ('oslo', 1964.94), ('selma', 1965.2),
    ('montgomery', 1965.23), ('chicago', 1966.5), ('atlanta', 1967.0), ('memphis_tn', 1968.26)))
P('Malcolm X', 'Black nationalist leader', (1925, 1965), 3, 'reform faith',
  'Nation of Islam preacher who broke with it after his pilgrimage to Mecca; shot in New York.',
  G(1952, 1965, 'Detroit, Harlem and Mecca', ('detroit', 1952.6), ('new_york', 1954.5), ('new_york', 1964.25), ('jeddah', 1964.3), ('mecca', 1964.31), ('cairo', 1964.33),
    ('accra', 1964.36), ('new_york', 1964.4), ('new_york', 1965.14)))
P('Rosa Parks', 'Civil rights activist', (1913, 2005), 2, 'reform',
  'Refused to give up her bus seat in Montgomery in 1955, starting the bus boycott.',
  G(1955, 1956, 'The Montgomery bus boycott', 'montgomery'))
P('Neil Armstrong', 'American astronaut', (1930, 2012), 2, 'explore',
  "First person to walk on the Moon, on 20 July 1969: 'one small step for man'.",
  G(1969, 1969, 'Apollo 11', ('houston_space', 1969.0), ('cape_canaveral', 1969.54), ((-169.15, 13.32, 1969.565)), ('honolulu', 1969.58), ('houston_space', 1969.62)))
P('J. Robert Oppenheimer', 'American physicist', (1904, 1967), 2, 'mind war',
  "Led the Los Alamos laboratory that built the atomic bomb: 'Now I am become Death, the destroyer of worlds.'",
  G(1943, 1945, 'Los Alamos', ('los_alamos', 1943.2), ('los_alamos', 1945.5), ((-106.48, 33.68, 1945.54)), ('los_alamos', 1945.6)))
P('Margaret Thatcher', 'British prime minister', (1925, 2013), 2, 'rule',
  "The 'Iron Lady', Britain's first woman prime minister, who won the Falklands War and remade the economy.",
  R(1979, 1990, 'Prime minister', *UK, at='london'))
P('Elizabeth II', 'Queen of the United Kingdom', (1926, 2022), 2, 'rule',
  "Reigned for seventy years as Britain's empire became a Commonwealth.",
  R(1952, 2022, 'Queen of the United Kingdom', *UK, at='london'))
P('Tony Blair', 'British prime minister', (1953, None), 3, 'rule',
  'Won three elections, made peace in Northern Ireland and joined the invasion of Iraq.',
  R(1997, 2007, 'Prime minister', *UK, at='london'))
P('Helmut Kohl', 'Chancellor of Germany', (1930, 2017), 3, 'rule',
  'Reunited Germany in 1990 and helped create the euro.',
  R(1982, 1998, 'Chancellor of Germany', 'West Germany', 'Germany', at='bonn'))
P('Angela Merkel', 'Chancellor of Germany', (1954, None), 2, 'rule',
  'Physicist from East Germany who led Germany for sixteen years, through the euro and refugee crises.',
  R(2005, 2021, 'Chancellor of Germany', 'Germany', at='berlin'))
P('Emmanuel Macron', 'President of France', (1977, None), 3, 'rule',
  "Founded his own party and in 2017 became France's youngest head of state since Napoleon.",
  R(2017, 2026, 'President of France', 'France', at='paris'))
P('Pope John Paul II', 'Pope', (1920, 2005), 2, 'faith',
  'The first Polish pope, whose visit home in 1979 helped inspire the Solidarity movement.',
  G(1978, 2005, 'Pope in Rome', 'rome'))
P('Josip Broz Tito', 'Leader of Yugoslavia', (1892, 1980), 2, 'war rule',
  'Led the partisans who freed Yugoslavia from the Nazis, then defied Stalin.',
  G(1941, 1945, 'The partisan war', ('belgrade', 1941.5), ((19.85, 43.86, 1941.75)), ((15.87, 44.81, 1942.9)), ((17.27, 44.34, 1943.9)), ((16.38, 44.37, 1944.4)),
    ((16.18, 43.06, 1944.5)), ('belgrade', 1944.8)),
  R(1945, 1980, 'Leader of Yugoslavia', 'Yugoslavia', at='belgrade'))
P('Nicolae Ceaușescu', 'Dictator of Romania', (1918, 1989), 3, 'rule',
  'Communist tyrant who was shot with his wife on Christmas Day 1989.',
  R(1965, 1989, 'Leader of Romania', 'Romania', at='bucharest'))
P('Lech Wałęsa', 'Leader of Solidarity', (1943, None), 3, 'reform rule',
  "Shipyard electrician whose Solidarity union helped bring down communism in Poland.",
  G(1980, 1989, 'Solidarity at the Gdańsk shipyard', 'danzig'), R(1990, 1995, 'President of Poland', 'Poland', at='warsaw'))
P('Václav Havel', 'President of Czechoslovakia, then the Czech Republic', (1936, 2011), 3, 'art rule',
  'Dissident playwright who led the Velvet Revolution of 1989.',
  R(1989, 2003, 'President', 'Czechoslovakia', 'Czech Republic', at='prague'))
P('Slobodan Milošević', 'President of Serbia', (1941, 2006), 3, 'rule war',
  'Stirred up Serb nationalism as Yugoslavia broke apart in war; died on trial for war crimes.',
  R(1989, 2000, 'Leader of Serbia', 'Serbia', 'Yugoslavia', at='belgrade'), G(2001, 2006, 'On trial in The Hague', 'the_hague'))
P('Ratko Mladić', 'Bosnian Serb general', (1942, None), 3, 'war',
  'Commanded the siege of Sarajevo and the Srebrenica massacre; jailed for life for genocide.',
  G(1992, 1995, 'Commander of the Bosnian Serb army', ((18.57, 43.82, 1992.4)), ('sarajevo', 1993.0), ((19.3, 44.1, 1995.53)), ((18.57, 43.82, 1995.9))))

# ---------- the Soviet Union and Russia ----------
P('Nikita Khrushchev', 'Leader of the Soviet Union', (1894, 1971), 2, 'rule',
  "Denounced Stalin's crimes, crushed Hungary's revolt and brought the world to the brink over Cuba.",
  R(1953, 1964, 'Leader of the Soviet Union', *SOV, at='moscow'))
P('Yuri Gagarin', 'Soviet cosmonaut', (1934, 1968), 2, 'explore',
  'The first human in space, once around the Earth on 12 April 1961.',
  G(1961, 1961, 'Vostok 1', ((63.31, 45.92, 1961.27)), ((45.99, 51.27, 1961.28)), ('moscow', 1961.29)))
P('Leonid Brezhnev', 'Leader of the Soviet Union', (1906, 1982), 3, 'rule',
  'Ruled the Soviet Union through eighteen years of stagnation and invaded Afghanistan in 1979.',
  R(1964, 1982, 'Leader of the Soviet Union', *SOV, at='moscow'))
P('Aleksandr Solzhenitsyn', 'Russian writer', (1918, 2008), 3, 'art',
  'Survived the Gulag and exposed it to the world in The Gulag Archipelago.',
  G(1950, 1953, 'Prisoner in the Gulag', (75.32, 51.72)),
  G(1974, 1994, 'Exile in the West', ('moscow', 1974.12), ('zurich', 1974.15), ((-72.38, 43.15, 1976.5)), ((-72.38, 43.15, 1994.38)), ((131.9, 43.12, 1994.4)), ('moscow', 1994.55)))
P('Mikhail Gorbachev', 'Last leader of the Soviet Union', (1931, 2022), 1, 'rule reform',
  'Opened up the Soviet Union, let Eastern Europe go free in 1989 and ended the Cold War.',
  R(1985, 1991, 'Leader of the Soviet Union', *SOV, at='moscow'))
P('Boris Yeltsin', 'First president of Russia', (1931, 2007), 2, 'rule',
  'Stood on a tank to defeat the hardliners\' coup of 1991 and led Russia through the chaotic 1990s.',
  R(1991, 1999, 'President of Russia', 'Russia', 'USSR', at='moscow'))
P('Vladimir Putin', 'President of Russia', (1952, None), 1, 'rule war',
  'KGB officer who has ruled Russia since 2000 and invaded Ukraine in 2014 and 2022.',
  G(1985, 1990, 'KGB officer in Dresden', 'dresden'), G(1991, 1996, 'St Petersburg city hall', 'st_petersburg'),
  R(2000, 2026, 'Leader of Russia', 'Russia', at='moscow'))
P('Alexei Navalny', 'Russian opposition leader', (1976, 2024), 3, 'reform',
  "Putin's boldest critic, poisoned with a nerve agent in 2020, jailed when he came home and killed in an Arctic prison.",
  G(2011, 2024, 'Moscow, Berlin and prison', ('moscow', 2011.9), ('moscow', 2020.6), ((84.97, 56.5, 2020.63)), ((73.37, 54.99, 2020.64)), ('berlin', 2020.65),
    ('berlin', 2021.04), ('moscow', 2021.05), ((39.47, 55.92, 2021.2)), ((65.85, 66.8, 2023.95)), ((65.85, 66.8, 2024.13))))
P('Yevgeny Prigozhin', 'Head of the Wagner Group', (1961, 2023), 3, 'war',
  "Putin's caterer turned warlord, whose mercenaries took Bakhmut and then marched on Moscow; killed in a plane crash two months later.",
  G(2022, 2023, 'Bakhmut and the march on Moscow', ((38.0, 48.6, 2022.6)), ((38.0, 48.6, 2023.4)), ((39.72, 47.23, 2023.478)), ((39.2, 51.66, 2023.48)), ((38.5, 52.62, 2023.482)),
    ((39.72, 47.23, 2023.486)), ((34.0, 57.73, 2023.64))))
P('Volodymyr Zelenskyy', 'President of Ukraine', (1978, None), 2, 'rule war',
  "Comic actor elected in 2019 who stayed in Kyiv to lead Ukraine's resistance to Russia's invasion.",
  R(2019, 2026, 'President of Ukraine', 'Ukraine', at='kiev'))

# ---------- Asia ----------
P('Zhou Enlai', 'Premier of China', (1898, 1976), 2, 'rule',
  "Mao's polished premier for 27 years, who opened China to Nixon in 1972.",
  G(1920, 1924, 'Student in France', ('shanghai', 1920.85), ('paris', 1921.0), ('berlin', 1922.2), ('paris', 1923.0), ('paris', 1924.5), ('canton', 1924.7)),
  R(1949, 1976, 'Premier of China', 'China', at='beijing'))
P('Deng Xiaoping', 'Leader of China', (1904, 1997), 1, 'rule reform',
  "Survived three purges, then from 1978 opened China's economy to the market and launched its rise.",
  G(1920, 1926, 'Work and study in France, then Moscow', ('shanghai', 1920.7), ('marseille', 1920.8), ('paris', 1921.0), ('paris', 1925.9), ('moscow', 1926.05)),
  R(1978, 1992, 'Leader of China', 'China', at='beijing'))
P('Xi Jinping', 'Leader of China', (1953, None), 2, 'rule',
  "Sent to live in a village cave as a teenager in the Cultural Revolution; China's most powerful leader since Mao.",
  G(1969, 1975, 'Sent down to the countryside', ((109.75, 36.7, 1969.1)), ((109.75, 36.7, 1975.8))),
  R(2012, 2026, 'Leader of China', 'China', at='beijing'))
P('14th Dalai Lama', 'Spiritual leader of Tibet', (1935, None), 2, 'faith',
  'Fled Tibet in 1959 as China crushed a revolt and has led the Tibetans in exile ever since.',
  G(1940, 1958, 'Lhasa', 'lhasa'), G(1959, 1959, 'Flight to India', ('lhasa', 1959.2), ((91.86, 27.59, 1959.24)), ((92.8, 26.63, 1959.3))),
  G(1960, 2026, 'In exile at Dharamshala', 'dharamshala'), wiki='14th Dalai Lama')
P('Kim Il Sung', 'Founder of North Korea', (1912, 1994), 2, 'rule war',
  'Guerrilla put in power by Stalin, who invaded the South in 1950 and founded a family dictatorship.',
  R(1948, 1994, 'Leader of North Korea', *NK, at='pyongyang'))
P('Kim Jong Il', 'Leader of North Korea', (1941, 2011), 3, 'rule',
  "Kim Il Sung's son, who ruled through a famine and built the bomb.",
  R(1994, 2011, 'Leader of North Korea', *NK, at='pyongyang'))
P('Kim Jong Un', 'Leader of North Korea', (1984, None), 3, 'rule',
  'The third Kim to rule North Korea, who has tested missiles that can reach America.',
  R(2011, 2026, 'Leader of North Korea', *NK, at='pyongyang'))
P('Syngman Rhee', 'First president of South Korea', (1875, 1965), 3, 'rule',
  'Led South Korea through the Korean War; driven out by student protests in 1960.',
  R(1948, 1959, 'President of South Korea', *SK, at='seoul'), G(1960, 1965, 'Exile in Hawaii', ('seoul', 1960.3), ('honolulu', 1960.4)))
P('Peng Dehuai', 'Chinese marshal', (1898, 1974), 3, 'war',
  "Led China's armies in the Korean War; purged for criticising Mao's Great Leap Forward.",
  G(1950, 1953, 'Commander in Korea', ('shenyang', 1950.75), ((126.4, 40.1, 1950.82)), ('pyongyang', 1950.93), ('seoul', 1951.01), ((127.0, 38.3, 1951.5)), ((127.0, 38.3, 1953.55))))
P('Võ Nguyên Giáp', 'Vietnamese general', (1911, 2013), 2, 'war',
  'History teacher turned general, who beat France at Dien Bien Phu in 1954 and then outlasted the United States.',
  G(1944, 1954, 'The Viet Minh war against France', ((106.25, 22.93, 1944.9)), ('thang_long', 1945.67), ((105.6, 21.8, 1947.0)), ((105.6, 21.8, 1953.8)),
    ('dien_bien_phu', 1954.2), ('dien_bien_phu', 1954.35), ('thang_long', 1954.75)),
  G(1955, 1975, 'Commander against the United States', 'thang_long'))
P('Ngo Dinh Diem', 'President of South Vietnam', (1901, 1963), 3, 'rule',
  'Catholic anti-communist backed by America; killed in a coup in 1963.',
  G(1955, 1963, 'President of South Vietnam', 'saigon'))
P('Pol Pot', 'Leader of the Khmer Rouge', (1925, 1998), 2, 'rule',
  "Emptied Cambodia's cities in 1975 and killed about a quarter of its people.",
  R(1975, 1978, 'Leader of Cambodia', 'Cambodia', at='phnom_penh'),
  G(1979, 1998, 'In the jungle on the Thai border', ((102.95, 13.8, 1979.1)), ((104.08, 14.23, 1994.0)), ((104.08, 14.23, 1998.29))))
P('Suharto', 'President of Indonesia', (1921, 2008), 3, 'rule',
  'General who crushed the communists in the massacres of 1965 and ruled Indonesia for 31 years.',
  R(1967, 1998, 'President of Indonesia', 'Indonesia', at='jakarta'))
P('Lee Kuan Yew', 'Founder of modern Singapore', (1923, 2015), 3, 'rule',
  'Turned a small port into one of the richest countries on Earth.',
  G(1959, 1990, 'Prime minister of Singapore', 'singapore'))
P('Indira Gandhi', 'Prime minister of India', (1917, 1984), 2, 'rule war',
  "Nehru's daughter, who won the 1971 war that made Bangladesh free; shot by her Sikh bodyguards.",
  R(1966, 1977, 'Prime minister of India', 'India', at='delhi'), R(1980, 1984, 'Prime minister of India', 'India', at='delhi'))
P('Narendra Modi', 'Prime minister of India', (1950, None), 3, 'rule',
  'Hindu nationalist who has led India since 2014.',
  R(2014, 2026, 'Prime minister of India', 'India', at='delhi'))
P('Benazir Bhutto', 'Prime minister of Pakistan', (1953, 2007), 3, 'rule',
  'The first woman elected to lead a Muslim-majority country; assassinated in 2007.',
  R(1988, 1990, 'Prime minister of Pakistan', 'Pakistan', at='islamabad'), R(1993, 1996, 'Prime minister of Pakistan', 'Pakistan', at='islamabad'))
P('Sheikh Mujibur Rahman', 'Founder of Bangladesh', (1920, 1975), 3, 'rule',
  'Led East Pakistan to independence as Bangladesh in 1971; murdered in a coup in 1975.',
  R(1972, 1975, 'Leader of Bangladesh', 'Bangladesh', at='dhaka'))
P('Mother Teresa', 'Catholic nun', (1910, 1997), 2, 'faith',
  'Albanian nun who cared for the dying poor of Calcutta.',
  G(1929, 1997, 'Calcutta', 'calcutta'))
P('Malala Yousafzai', "Pakistani campaigner for girls' schooling", (1997, None), 3, 'reform',
  'Shot by the Taliban in 2012 for going to school; the youngest winner of the Nobel peace prize.',
  G(2009, 2012, 'The Swat valley', ((72.36, 34.77, 2009.0)), ((72.36, 34.77, 2012.77)), ('birmingham', 2012.8)))

# ---------- the Middle East ----------
P('David Ben-Gurion', 'Founder of Israel', (1886, 1973), 2, 'rule',
  'Proclaimed the state of Israel in 1948 and led it through its first war.',
  R(1948, 1963, 'Prime minister of Israel', 'Israel', at='tel_aviv'))
P('Golda Meir', 'Prime minister of Israel', (1898, 1978), 3, 'rule',
  'Kyiv-born, Milwaukee-raised prime minister who led Israel through the Yom Kippur War.',
  R(1969, 1974, 'Prime minister of Israel', 'Israel', at='jerusalem'))
P('Yitzhak Rabin', 'Prime minister of Israel', (1922, 1995), 3, 'rule war',
  'Commander in the Six-Day War who signed the Oslo peace accords with Arafat; shot by an Israeli extremist.',
  R(1992, 1995, 'Prime minister of Israel', 'Israel', at='jerusalem'))
P('Ariel Sharon', 'Israeli general and prime minister', (1928, 2014), 3, 'war rule',
  'Crossed the Suez Canal in 1973, led the invasion of Lebanon in 1982 and pulled Israel out of Gaza in 2005.',
  R(2001, 2005, 'Prime minister of Israel', 'Israel', at='jerusalem'))
P('Benjamin Netanyahu', 'Prime minister of Israel', (1949, None), 3, 'rule war',
  "Israel's longest-serving prime minister, in power through the war with Hamas after 7 October 2023.",
  R(1996, 1999, 'Prime minister of Israel', 'Israel', at='jerusalem'), R(2009, 2021, 'Prime minister of Israel', 'Israel', at='jerusalem'),
  R(2023, 2026, 'Prime minister of Israel', 'Israel', at='jerusalem'))
P('Yasser Arafat', 'Palestinian leader', (1929, 2004), 2, 'rule war',
  'Led the Palestine Liberation Organization from exile for decades, then signed the Oslo accords.',
  G(1959, 2004, 'Leader of the Palestinians', ('kuwait', 1959.0), ('kuwait', 1964.5), ('damascus', 1965.0), ('damascus', 1967.6), ('amman', 1968.0), ('amman', 1970.75),
    ('beirut', 1971.0), ('beirut', 1982.6), ('tunis', 1982.7),
    ('tunis', 1994.4), ('gaza', 1994.5), ((35.2, 31.9, 1996.5)), ((35.2, 31.9, 2004.8)), ('paris', 2004.85)))
P('Gamal Abdel Nasser', 'President of Egypt', (1918, 1970), 2, 'rule',
  'Overthrew the king, seized the Suez Canal in 1956 and became the hero of Arab nationalism.',
  R(1954, 1970, 'Leader of Egypt', 'Egypt', at='cairo'))
P('Anwar Sadat', 'President of Egypt', (1918, 1981), 2, 'rule war',
  'Attacked Israel in 1973, then flew to Jerusalem and made peace; assassinated in 1981.',
  R(1970, 1976, 'President of Egypt', 'Egypt', at='cairo'),
  G(1977, 1978, 'Peace with Israel', ('cairo', 1977.0), ('cairo', 1977.86), ('jerusalem', 1977.88), ('cairo', 1977.9), ('cairo', 1978.65), ((-77.46, 39.65, 1978.68)), ('cairo', 1978.75)),
  R(1979, 1981, 'President of Egypt', 'Egypt', at='cairo'))
P('Hafez al-Assad', 'President of Syria', (1930, 2000), 3, 'rule war',
  'Air force officer who seized Syria in 1970 and ruled it with an iron hand for thirty years.',
  R(1971, 2000, 'President of Syria', 'Syria', at='damascus'))
P('Bashar al-Assad', 'President of Syria', (1965, None), 3, 'rule war',
  'Eye doctor who inherited Syria and fought a civil war that killed half a million people; fled to Moscow in 2024.',
  R(2000, 2024, 'President of Syria', 'Syria', at='damascus'), G(2025, 2026, 'Exile in Moscow', 'moscow'))
P('Ahmed al-Sharaa', 'President of Syria', (1982, None), 3, 'war rule',
  'Former jihadist commander whose rebels took Damascus in December 2024.',
  G(2017, 2024, 'Rebel leader in Idlib', ((36.63, 35.93, 2017.0)), ((36.63, 35.93, 2024.9)), ('aleppo', 2024.92), ((36.75, 35.13, 2024.93)), ((36.72, 34.73, 2024.935)), ('damascus', 2024.94)),
  R(2025, 2026, 'President of Syria', 'Syria', at='damascus'))
P('Mohammad Reza Pahlavi', 'Last shah of Iran', (1919, 1980), 3, 'rule',
  'Modernised Iran with American backing and a feared secret police until the revolution of 1979 drove him out.',
  R(1941, 1978, 'Shah of Iran', 'Iran', at='tehran'),
  G(1979, 1980, 'Exile', ('tehran', 1979.04), ('aswan', 1979.05), ('rabat', 1979.1), ((-77.35, 25.06, 1979.25)), ((-99.23, 18.92, 1979.45)), ('new_york', 1979.81),
    ((-79.03, 8.62, 1979.96)), ('cairo', 1980.23)))
P('Ruhollah Khomeini', 'Supreme leader of Iran', (1902, 1989), 1, 'rule faith',
  'Exiled cleric who led the revolution of 1979 that overthrew the shah and made Iran an Islamic republic.',
  G(1964, 1979, 'Exile and return', ('qom', 1964.8), ((29.06, 40.18, 1964.85)), ('najaf', 1965.8), ('najaf', 1978.75), ((2.0, 48.85, 1978.8)), ((2.0, 48.85, 1979.08)), ('tehran', 1979.09)),
  R(1980, 1989, 'Supreme leader of Iran', 'Iran', at='tehran'))
P('Ali Khamenei', 'Supreme leader of Iran', (1939, 2026), 3, 'rule faith',
  "Khomeini's successor, who ruled Iran for 36 years until he was killed in the 2026 war with Israel and the United States.",
  R(1989, 2025, 'Supreme leader of Iran', 'Iran', at='tehran'))
P('Saddam Hussein', 'Dictator of Iraq', (1937, 2006), 2, 'rule war',
  'Invaded Iran in 1980 and Kuwait in 1990; overthrown by the American invasion of 2003 and hanged.',
  R(1979, 2002, 'Leader of Iraq', 'Iraq', at='baghdad'),
  G(2003, 2006, 'Overthrown, caught and tried', ('baghdad', 2003.2), ('tikrit', 2003.3), ('tikrit', 2003.95), ('baghdad', 2004.0)))
P('Osama bin Laden', 'Founder of al-Qaeda', (1957, 2011), 2, 'war faith',
  'Saudi millionaire who fought the Soviets in Afghanistan and planned the attacks of 11 September 2001.',
  G(1980, 2011, 'Afghanistan, Sudan and hiding', ('jeddah', 1980.0), ('peshawar', 1980.5), ('peshawar', 1986.5), ((70.45, 34.43, 1987.3)), ((70.45, 34.43, 1989.8)), ('jeddah', 1990.0),
    ('jeddah', 1991.9), ('khartoum', 1992.0), ('khartoum', 1996.3),
    ((70.45, 34.43, 1996.4)), ('kandahar', 1997.5), ('kandahar', 2001.8), ((70.2, 34.1, 2001.95)), ((73.24, 34.17, 2005.5)), ((73.24, 34.17, 2011.34))))
P('Ahmad Shah Massoud', 'Afghan resistance commander', (1953, 2001), 3, 'war',
  "The 'Lion of Panjshir', who fought the Soviets and then the Taliban; killed by al-Qaeda two days before 11 September.",
  G(1979, 2001, 'The Panjshir valley', ((69.7, 35.3, 1979.5)), ((69.7, 35.3, 1992.3)), ('kabul', 1992.35), ('kabul', 1996.7), ((69.7, 35.3, 1996.75)), ((69.4, 37.4, 2001.69))))
P('Hamid Karzai', 'President of Afghanistan', (1957, None), 3, 'rule',
  'Led Afghanistan after the Taliban fell in 2001.',
  R(2002, 2014, 'Leader of Afghanistan', 'Afghanistan', at='kabul'))
P('Abu Bakr al-Baghdadi', 'Leader of the Islamic State', (1971, 2019), 3, 'war',
  'Declared a caliphate from Mosul in 2014 over a third of Iraq and Syria.',
  G(2010, 2019, 'The Islamic State', ((43.0, 34.2, 2010.4)), ((39.01, 35.95, 2013.5)), ('mosul', 2014.5), ((39.01, 35.95, 2015.0)), ((40.92, 34.45, 2018.0)), ((36.63, 36.17, 2019.82))))
P('Recep Tayyip Erdoğan', 'President of Turkey', (1954, None), 3, 'rule',
  'Former mayor of Istanbul who has led Turkey since 2003.',
  R(2003, 2026, 'Leader of Turkey', 'Turkey', at='ankara'))
P('Mohammed bin Salman', 'Crown prince of Saudi Arabia', (1985, None), 3, 'rule',
  "Saudi Arabia's young ruler since 2017, who is spending its oil money to remake the kingdom.",
  R(2017, 2026, 'Ruler of Saudi Arabia', 'Saudi Arabia', at='riyadh'))

# ---------- Africa ----------
P('Kwame Nkrumah', 'First president of Ghana', (1909, 1972), 2, 'rule',
  "Led Ghana to independence in 1957, the first of Africa's colonies south of the Sahara to break free.",
  R(1957, 1966, 'Leader of Ghana', 'Ghana', 'Gold Coast', at='accra'))
P('Jomo Kenyatta', 'First president of Kenya', (1897, 1978), 3, 'rule',
  'Jailed by the British during the Mau Mau uprising, then led Kenya after independence in 1963.',
  G(1953, 1961, 'Imprisoned in the north', ((35.12, 1.24, 1953.3)), ((35.76, 4.26, 1954.0)), ((35.6, 3.12, 1959.3)), ((36.7, 1.1, 1961.3)), ('nairobi', 1961.6)),
  R(1963, 1978, 'Leader of Kenya', 'Kenya', at='nairobi'))
P('Patrice Lumumba', 'First prime minister of the Congo', (1925, 1961), 3, 'rule',
  'Led the Congo to independence from Belgium in 1960; overthrown within months and murdered.',
  G(1960, 1961, 'Prime minister, then prisoner', ('kinshasa', 1960.5), ('kinshasa', 1960.9), ((27.48, -11.66, 1961.05))))
P('Mobutu Sese Seko', 'Dictator of Zaire', (1930, 1997), 3, 'rule',
  'Seized the Congo in 1965, renamed it Zaire and looted it for 32 years.',
  R(1965, 1997, 'Leader of Zaire', 'Zaire', at='kinshasa'))
P('Julius Nyerere', 'First president of Tanzania', (1922, 1999), 3, 'rule',
  'Schoolteacher who led Tanganyika to independence and joined it with Zanzibar as Tanzania.',
  R(1961, 1985, 'Leader of Tanzania', 'Tanzania, United Republic of', at='dar_es_salaam'))
P('Muammar Gaddafi', 'Dictator of Libya', (1942, 2011), 2, 'rule',
  'Army captain who seized Libya in 1969 and ruled it until he was killed in the uprising of 2011.',
  R(1969, 2010, 'Leader of Libya', 'Libya', at='tripoli'), G(2011, 2011, 'Uprising and death', ('tripoli', 2011.1), ('tripoli', 2011.64), ('sirte', 2011.8)))
P('Idi Amin', 'Dictator of Uganda', (1925, 2003), 3, 'rule',
  'Killed perhaps 300,000 people and expelled the Asians from Uganda.',
  R(1971, 1979, 'Leader of Uganda', 'Uganda', at='kampala'))
P('Nelson Mandela', 'First black president of South Africa', (1918, 2013), 1, 'rule reform',
  'Spent 27 years in prison for fighting apartheid, then led South Africa to democracy.',
  G(1941, 1961, 'Lawyer and ANC leader in Johannesburg', 'johannesburg'),
  G(1962, 1962, 'Africa tour, then arrest', ('johannesburg', 1962.0), ('addis_ababa', 1962.1), ((-1.91, 34.68, 1962.25)), ('london', 1962.45), ('dar_es_salaam', 1962.5), ((30.23, -29.47, 1962.6))),
  G(1963, 1981, 'Prisoner on Robben Island', 'robben_island'),
  G(1982, 1990, 'Prisoner near Cape Town', ((18.45, -34.03, 1982.25)), ((18.92, -33.73, 1988.95)), ((18.92, -33.73, 1990.1))),
  R(1994, 1999, 'President of South Africa', 'South Africa', at='pretoria'))
P('F. W. de Klerk', 'President of South Africa', (1936, 2021), 3, 'rule reform',
  'Freed Mandela in 1990 and took apartheid apart with him.',
  R(1989, 1994, 'President of South Africa', 'South Africa', at='pretoria'))
P('Robert Mugabe', 'Leader of Zimbabwe', (1924, 2019), 3, 'rule',
  "Guerrilla leader of Zimbabwe's independence war who then ruled it for 37 years.",
  R(1980, 2017, 'Leader of Zimbabwe', 'Zimbabwe', at='harare'))
P('Paul Kagame', 'President of Rwanda', (1957, None), 3, 'war rule',
  'Led the rebel army that ended the genocide of 1994 and has ruled Rwanda since.',
  G(1990, 1994, 'The rebel war from Uganda', ('kampala', 1990.75), ((30.0, -1.3, 1990.8)), ((29.9, -1.45, 1992.5)), ('kigali', 1994.53)),
  R(1995, 2026, 'Leader of Rwanda', 'Rwanda', at='kigali'))
P('Abiy Ahmed', 'Prime minister of Ethiopia', (1976, None), 3, 'rule war',
  'Won the Nobel peace prize in 2019 for ending the war with Eritrea, then fought a brutal war in Tigray.',
  R(2018, 2026, 'Prime minister of Ethiopia', 'Ethiopia', at='addis_ababa'))

# ---------- the Americas ----------
P('Fidel Castro', 'Leader of communist Cuba', (1926, 2016), 1, 'rule war',
  'Led the Cuban Revolution from the Sierra Maestra to victory in 1959 and ruled Cuba for half a century.',
  G(1953, 1953, 'Attack on the Moncada barracks', 'havana', ('santiago_cuba', 1953.57)),
  G(1955, 1956, 'Exile in Mexico and the voyage of the Granma', ('mexico_city', 1955.55), ((-97.4, 20.96, 1956.9)), ((-77.73, 19.84, 1956.92)), ('sierra_maestra', 1956.97)),
  G(1957, 1958, 'Guerrilla war in the Sierra Maestra', 'sierra_maestra'),
  G(1959, 1959, 'Victory march to Havana', ('santiago_cuba', 1959.0), ((-77.92, 21.38, 1959.01)), ((-79.96, 22.4, 1959.015)), ('havana', 1959.02)),
  R(1960, 2008, 'Leader of Cuba', 'Cuba', at='havana'))
P('Che Guevara', 'Argentine revolutionary', (1928, 1967), 2, 'war',
  'Doctor who crossed South America by motorbike, fought beside Castro in Cuba and died leading a guerrilla war in Bolivia.',
  G(1952, 1952, 'The motorcycle journey', ('buenos_aires', 1952.0), ((-71.31, -41.13, 1952.1)), ('valparaiso', 1952.2), ((-69.9, -22.4, 1952.28)), ('cuzco', 1952.33),
    ('machu_picchu', 1952.35), ('lima', 1952.4), ((-70.1, -4.1, 1952.48)), ('bogota', 1952.52), ('caracas', 1952.55)),
  G(1953, 1956, 'Guatemala and Mexico', ('la_paz', 1953.55), ((-90.51, 14.63, 1954.0)), ('mexico_city', 1954.7), ((-97.4, 20.96, 1956.9)), ((-77.73, 19.84, 1956.92)),
    ('sierra_maestra', 1956.97)),
  G(1957, 1958, 'The Cuban Revolution', ('sierra_maestra', 1957.0), ('sierra_maestra', 1958.65), ((-79.96, 22.4, 1958.99))),
  G(1959, 1964, 'Minister in Havana', 'havana'),
  G(1965, 1965, 'Guerrilla war in the Congo', ('havana', 1965.2), ((29.2, -4.6, 1965.3)), ((29.2, -4.6, 1965.88)), ('dar_es_salaam', 1965.95)),
  G(1966, 1967, 'Guerrilla war in Bolivia', ('havana', 1966.8), ('la_paz', 1966.85), ((-63.6, -19.4, 1966.9)), ((-63.9, -18.8, 1967.77))))
P('Raúl Castro', 'Leader of Cuba', (1931, None), 3, 'rule war',
  "Fidel's younger brother and commander, who led Cuba after him.",
  R(2008, 2018, 'Leader of Cuba', 'Cuba', at='havana'))
P('Juan Perón', 'President of Argentina', (1895, 1974), 2, 'rule',
  'Colonel who won over the workers with his wife Evita, was overthrown in 1955 and returned from exile in 1973.',
  R(1946, 1955, 'President of Argentina', 'Argentina', at='buenos_aires'),
  G(1956, 1972, 'Exile', ('asuncion', 1956.0), ('panama', 1956.5), ('caracas', 1957.0), ('santo_domingo', 1958.2), ('santo_domingo', 1959.95), ('madrid', 1960.1), ('madrid', 1972.9)),
  R(1973, 1974, 'President of Argentina', 'Argentina', at='buenos_aires'))
P('Eva Perón', 'First lady of Argentina', (1919, 1952), 3, 'rule reform',
  "'Evita', the actress who championed Argentina's poor and won its women the vote.",
  G(1946, 1952, 'First lady of Argentina', ('buenos_aires', 1946.4), ('buenos_aires', 1947.42), ('madrid', 1947.44), ('rome', 1947.49), ('paris', 1947.55), ('geneva', 1947.59),
    ('buenos_aires', 1947.64), ('buenos_aires', 1952.57)))
P('Salvador Allende', 'President of Chile', (1908, 1973), 3, 'rule',
  'The first Marxist elected president in Latin America; died in the coup of 1973.',
  R(1970, 1973, 'President of Chile', 'Chile', at='santiago'))
P('Augusto Pinochet', 'Dictator of Chile', (1915, 2006), 3, 'rule',
  'General who seized power in 1973 and ruled by terror until 1990.',
  R(1973, 1990, 'Leader of Chile', 'Chile', at='santiago'))
P('Hugo Chávez', 'President of Venezuela', (1954, 2013), 3, 'rule',
  "Paratrooper who led a socialist revolution paid for with Venezuela's oil.",
  R(1999, 2013, 'President of Venezuela', 'Venezuela', at='caracas'))
P('Luiz Inácio Lula da Silva', 'President of Brazil', (1945, None), 3, 'rule',
  'Factory worker and union leader who became president in 2003 and again in 2023.',
  R(2003, 2010, 'President of Brazil', 'Brazil', at='brasilia'), R(2023, 2026, 'President of Brazil', 'Brazil', at='brasilia'))

# ---------- art, science and the modern world ----------
P('Pablo Picasso', 'Spanish painter', (1881, 1973), 2, 'art',
  'Co-founder of Cubism and painter of Guernica, the most famous artist of the 20th century.',
  G(1895, 1903, 'Barcelona, Madrid and Paris', ('barcelona', 1895.8), ('madrid', 1897.8), ('barcelona', 1899.0), ('barcelona', 1900.75), ('paris', 1900.8),
    ('paris', 1901.9), ('barcelona', 1902.0)),
  G(1904, 1946, 'Paris', 'paris'), G(1947, 1973, 'The south of France', ((7.05, 43.58, 1948.0)), ((7.0, 43.6, 1961.0)), ((7.0, 43.6, 1973.27))))
P('Alan Turing', 'British mathematician', (1912, 1954), 2, 'mind',
  'Founded computer science and broke German codes at Bletchley Park.',
  G(1939, 1945, 'Codebreaker at Bletchley Park', (-0.74, 52.0)), G(1946, 1954, 'The first computers', ('london', 1946.0), ('london', 1947.9), ('manchester', 1948.5)))
P('The Beatles', 'English rock band', (1960, 1970), 2, 'art',
  'Four lads from Liverpool who became the most famous band in history.',
  G(1960, 1969, 'Liverpool, Hamburg, London and the world', ('liverpool', 1960.5), ('hamburg', 1960.65), ('liverpool', 1961.2), ('london', 1963.5), ('new_york', 1964.1),
    ('london', 1964.2), ((78.27, 30.12, 1968.15)), ('london', 1968.35), ('london', 1969.99)))
P('Tim Berners-Lee', 'English computer scientist', (1955, None), 2, 'mind',
  'Invented the World Wide Web at CERN in 1989.',
  G(1989, 1991, 'Inventing the web at CERN', (6.05, 46.23)))
P('Steve Jobs', 'Co-founder of Apple', (1955, 2011), 2, 'mind',
  'Made the personal computer, and then the smartphone, something everyone wanted.',
  G(1976, 2011, 'Apple, in what became Silicon Valley', (-122.03, 37.32)))

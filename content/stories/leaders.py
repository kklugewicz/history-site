"""Leaders: the rulers, conquerors, generals, statesmen, revolutionaries and reformers among the people with a story,
listed century by century. The Leaders button at the top of the map opens the list (beside Discovery, which lists the
great minds); each name opens that person's story. python3 content/stories/build_leaders.py checks this file and writes
data/leaders.json.

L(person id, roles, regions, year, what they were, what they are known for, c=True when the year is approximate)
  roles    one or more of: rule (rulers: kings, queens, emperors, pharaohs, caliphs, sultans, dictators), conq
           (conquerors, who built or won an empire by war), gen (generals and commanders), state (statesmen:
           presidents, prime ministers, chancellors, founders of nations by politics), rev (revolutionaries, who led a
           revolt, revolution or fight for independence), ref (reformers, who changed their country without ruling it:
           the Reformation, abolition, civil rights). The list's first row of buttons filters by them.
  regions  one or more of: eu (Europe), me (the Middle East: Mesopotamia, Persia, Anatolia, the Levant and Arabia), af
           (Africa, Egypt and Carthage included), as (the rest of Asia), am (the Americas): where they led, not where
           they were born. The second row of buttons filters by them.
  year     the year of the first thing named in "known for", the deed they are best known for (a battle, a crowning, a
           revolution, a speech). It puts them in their century: 6th century BC is 600 to 501 BC, and from AD 1 the
           1600s are the 17th century.
Only people with a story belong here, and not all of them: explorers (Columbus, Zheng He, Cook), founders and leaders of
faiths (Moses, the Buddha, Jesus, Muhammad, the popes, the Dalai Lama), saints, scientists and artists stay out unless
they led a state, an army or a movement. A few are in Discovery too: Marcus Aurelius and Sejong ruled, Sun Tzu was a
general, Benjamin Franklin was a statesman as well as a scientist.
"""

ROLES = {'rule': 'Rulers', 'conq': 'Conquerors', 'gen': 'Generals', 'state': 'Statesmen', 'rev': 'Revolutionaries',
         'ref': 'Reformers'}
REGIONS = {'eu': 'Europe', 'me': 'Middle East', 'af': 'Africa', 'as': 'Asia', 'am': 'Americas'}
LEADERS = []


def L(pid, roles, regions, year, what, known, c=False):
    e = {'id': pid, 'f': roles.split(), 'r': regions.split(), 'y': year, 'as': what, 'k': known}
    if c:
        e['c'] = 1
    LEADERS.append(e)


# ---- the first kingdoms
L('khufu', 'rule', 'af', -2580, 'Pharaoh of Egypt', 'The Great Pyramid of Giza', c=True)
L('sargon-of-akkad', 'rule conq', 'me', -2300, 'King of Akkad', 'The first empire, from the Gulf to the Mediterranean', c=True)
L('hammurabi', 'rule', 'me', -1754, 'King of Babylon', "Hammurabi's Code, laws carved in stone", c=True)
L('hatshepsut', 'rule', 'af', -1479, 'Pharaoh of Egypt', 'A woman pharaoh: trade, temples, twenty years of peace', c=True)
L('tutankhamun', 'rule', 'af', -1332, 'Boy pharaoh of Egypt', 'The boy king whose tomb was found full of gold', c=True)
L('ramesses-ii', 'rule gen', 'af', -1274, 'Pharaoh of Egypt', 'The Battle of Kadesh, and the first known peace treaty')

# ---- the classical world
L('cyrus-the-great', 'rule conq', 'me', -539, 'Founder of the Persian Empire', "Took Babylon and let its captive peoples go home")
L('darius-i', 'rule', 'me', -518, 'King of Persia', 'Royal roads, coins, satraps, and Persepolis', c=True)
L('sun-tzu', 'gen', 'as', -500, 'General and strategist', 'The Art of War', c=True)
L('leonidas-i', 'rule gen', 'eu', -480, 'King of Sparta', 'The 300 at Thermopylae')
L('pericles', 'state', 'eu', -447, 'Leader of Athens', "Athens' golden age: democracy and the Parthenon")
L('alexander-the-great', 'rule conq gen', 'eu me as af', -334, 'King of Macedon', 'Conquered the Persian Empire, from Egypt to India')
L('ashoka', 'rule', 'as', -260, 'Maurya emperor', 'Turned from war to Buddhism after Kalinga', c=True)
L('qin-shi-huang', 'rule conq', 'as', -221, 'First emperor of China', 'United China; the Terracotta Army')
L('hannibal', 'gen', 'af eu', -218, 'Carthaginian general', 'Crossed the Alps with elephants to fight Rome')
L('spartacus', 'rev gen', 'eu', -73, 'Gladiator and rebel', 'The great slave revolt against Rome')
L('pompey', 'gen state', 'eu me', -67, 'Roman general', 'Swept the pirates from the sea, then conquered the East')
L('cleopatra', 'rule', 'af', -51, 'Last queen of Egypt', 'Allied with Caesar and Antony to keep Egypt free')
L('julius-caesar', 'gen conq state', 'eu', -49, 'Roman general and dictator', 'Crossed the Rubicon, after conquering Gaul')
L('mark-antony', 'gen state', 'eu af', -42, 'Roman general', 'Avenged Caesar; ruled the East beside Cleopatra')
L('augustus', 'rule state', 'eu', -27, 'First Roman emperor', 'Ended the civil wars and began the Pax Romana')
L('boudica', 'rule rev', 'eu', 60, 'Queen of the Iceni', "Led Britain's revolt against Rome and burned London", c=True)
L('marcus-aurelius', 'rule', 'eu', 161, 'Roman emperor', 'The last of the Five Good Emperors')
L('constantine-the-great', 'rule', 'eu me', 312, 'Roman emperor', 'The first Christian emperor; founded Constantinople')

# ---- the middle ages
L('attila', 'rule conq', 'eu', 451, 'King of the Huns', 'The Scourge of God, who terrified Rome')
L('justinian-i', 'rule', 'eu me', 529, 'Byzantine emperor', 'His code of Roman law, Hagia Sophia, Rome won back')
L('ali', 'rule', 'me', 656, 'Fourth caliph', 'Cousin of Muhammad, and the first imam of the Shia')
L('wu-zetian', 'rule', 'as', 690, 'Empress of China', 'The only woman to rule China as emperor in her own name')
L('harun-al-rashid', 'rule', 'me', 786, 'Abbasid caliph', "Baghdad's golden age, the court of the Arabian Nights")
L('charlemagne', 'rule conq', 'eu', 800, 'King of the Franks', 'Crowned emperor of the West; united much of Europe')
L('william-the-conqueror', 'rule conq', 'eu', 1066, 'Duke of Normandy, King of England', 'Won England at the Battle of Hastings')
L('saladin', 'rule gen', 'me af', 1187, 'Sultan of Egypt and Syria', 'Took Jerusalem back from the Crusaders')
L('genghis-khan', 'rule conq', 'as', 1206, 'Founder of the Mongol Empire', 'United the Mongols, then conquered half of Asia')
L('kublai-khan', 'rule conq', 'as', 1271, 'Great Khan, emperor of China', "Founded the Yuan dynasty; Marco Polo's host")
L('mansa-musa', 'rule', 'af', 1324, 'Emperor of Mali', "A pilgrimage to Mecca so rich it crashed gold's price")
L('timur', 'rule conq', 'as me', 1370, 'Founder of the Timurid Empire', 'Conquered from Delhi to Ankara; built Samarkand')

# ---- the fifteenth and sixteenth centuries
L('joan-of-arc', 'gen', 'eu', 1429, 'French heroine and saint', 'Broke the siege of Orléans at seventeen')
L('pachacuti', 'rule conq', 'am', 1438, 'Founder of the Inca Empire', 'Built the Inca Empire, and Machu Picchu', c=True)
L('sejong-the-great', 'rule', 'as', 1443, 'King of Korea', 'Gave Korea its own alphabet, Hangul')
L('mehmed-ii', 'rule conq', 'me eu', 1453, 'Ottoman sultan', 'Conquered Constantinople at twenty-one')
L('vlad-the-impaler', 'rule gen', 'eu', 1462, 'Prince of Wallachia', 'Fought the Ottomans; the model for Dracula')
L('isabella-i-of-castile', 'rule', 'eu', 1492, 'Queen of Castile', 'Took Granada, united Spain and sent Columbus west')
L('moctezuma-ii', 'rule', 'am', 1502, 'Emperor of the Aztecs', 'Ruled the Aztecs at their height, until Cortés came')
L('martin-luther', 'ref', 'eu', 1517, 'Leader of the Reformation', 'The 95 Theses, which split the Western Church')
L('charles-v-holy-roman-emperor', 'rule', 'eu am', 1519, 'Holy Roman Emperor, King of Spain', 'An empire on which the sun never set')
L('suleiman-the-magnificent', 'rule conq', 'me eu', 1520, 'Ottoman sultan', 'The Lawgiver: the Ottomans at their height')
L('hernan-cortes', 'conq', 'am', 1521, 'Spanish conquistador', 'Conquered the Aztec Empire')
L('francisco-pizarro', 'conq', 'am', 1532, 'Spanish conquistador', 'Conquered the Inca Empire')
L('henry-viii', 'rule', 'eu', 1534, 'King of England', 'Six wives, and the break with Rome')
L('john-calvin', 'ref', 'eu', 1536, 'Protestant reformer', 'The Institutes, and Geneva as a godly city')
L('akbar', 'rule conq', 'as', 1556, 'Mughal emperor', 'Built Mughal India and welcomed every faith')
L('philip-ii-of-spain', 'rule', 'eu', 1588, 'King of Spain', "The Armada, at the height of Spain's empire")
L('elizabeth-i', 'rule', 'eu', 1588, 'Queen of England', 'Beat the Spanish Armada; the Elizabethan age')

# ---- the seventeenth and eighteenth centuries
L('tokugawa-ieyasu', 'rule gen', 'as', 1600, 'First Tokugawa shogun', 'Won at Sekigahara: 250 years of peace for Japan')
L('shah-jahan', 'rule', 'as', 1632, 'Mughal emperor', 'Built the Taj Mahal for his wife')
L('oliver-cromwell', 'rev gen state', 'eu', 1649, 'Lord Protector of England', 'Beat the king in a civil war and ruled without one')
L('aurangzeb', 'rule conq', 'as', 1658, 'Mughal emperor', 'Took the Mughal Empire to its largest')
L('louis-xiv', 'rule', 'eu', 1682, 'King of France', 'The Sun King, and the court of Versailles')
L('peter-the-great', 'rule', 'eu', 1703, 'Tsar and emperor of Russia', 'Founded St Petersburg and made Russia modern')
L('frederick-the-great', 'rule gen', 'eu', 1740, 'King of Prussia', 'Made Prussia a great power by war')
L('catherine-the-great', 'rule', 'eu', 1762, 'Empress of Russia', 'Took Russia to the Black Sea; its golden age')
L('george-washington', 'gen state rev', 'am', 1775, 'First president of the United States', 'Led the army that won American independence')
L('thomas-jefferson', 'state rev', 'am', 1776, 'Third president of the United States', 'Wrote the Declaration of Independence')
L('benjamin-franklin', 'state', 'am', 1776, 'Founding Father and diplomat', 'Signed the Declaration and won France to its side')
L('toussaint-louverture', 'rev gen', 'am', 1791, 'Leader of the Haitian Revolution', 'Led the slave revolt that freed Haiti')

# ---- the 1800s
L('napoleon', 'rule conq gen', 'eu', 1804, 'Emperor of the French', 'Conquered most of Europe; the Napoleonic Code')
L('simon-bolivar', 'rev gen', 'am', 1819, 'The Liberator', 'Freed six nations of South America from Spain')
L('queen-victoria', 'rule', 'eu', 1837, 'Queen of the United Kingdom', 'The Victorian age, the British Empire at its height')
L('frederick-douglass', 'ref', 'am', 1845, 'Abolitionist', 'Escaped slavery; his Narrative moved a nation')
L('harriet-tubman', 'ref', 'am', 1850, 'Abolitionist', 'Led the enslaved to freedom on the Underground Railroad')
L('abraham-lincoln', 'state', 'am', 1863, '16th president of the United States', 'Won the Civil War and ended slavery')
L('emperor-meiji', 'rule', 'as', 1868, 'Emperor of Japan', 'The Meiji Restoration: Japan made a modern power')
L('otto-von-bismarck', 'state', 'eu', 1871, 'Chancellor of Germany', 'United Germany by "blood and iron"')

# ---- the 1900s
L('vladimir-lenin', 'rev state', 'eu', 1917, 'Founder of the Soviet Union', 'Led the Russian Revolution')
L('benito-mussolini', 'rule', 'eu', 1922, 'Fascist dictator of Italy', 'Marched on Rome and founded fascism')
L('mustafa-kemal-ataturk', 'gen rev state', 'me', 1923, 'Founder of modern Turkey', 'Built the Turkish Republic from the Ottoman ruins')
L('joseph-stalin', 'rule', 'eu', 1924, 'Dictator of the Soviet Union', 'Ruled by terror, and beat Hitler in World War II')
L('chiang-kai-shek', 'state gen', 'as', 1928, 'Leader of the Republic of China', 'United China, then lost it to Mao')
L('mahatma-gandhi', 'rev ref', 'as', 1930, 'Leader of Indian independence', 'The Salt March: freedom without violence')
L('adolf-hitler', 'rule', 'eu', 1933, 'Nazi dictator of Germany', 'Started World War II and the Holocaust')
L('franklin-d-roosevelt', 'state', 'am', 1933, '32nd president of the United States', 'The New Deal, and America in World War II')
L('winston-churchill', 'state', 'eu', 1940, 'British prime minister', 'Led Britain against Hitler when it stood alone')
L('charles-de-gaulle', 'gen state', 'eu', 1940, 'Leader of Free France and president', 'Led Free France, then founded the Fifth Republic')
L('ho-chi-minh', 'rev', 'as', 1945, 'Founder of communist Vietnam', "Led Vietnam's fight for independence")
L('mao-zedong', 'rev rule', 'as', 1949, "Founder of the People's Republic", 'Won the civil war and ruled China for 27 years')
L('elizabeth-ii', 'rule', 'eu', 1952, 'Queen of the United Kingdom', 'Seventy years on the throne, longest in British history')
L('rosa-parks', 'ref', 'am', 1955, 'Civil rights activist', 'Kept her seat on a Montgomery bus')
L('fidel-castro', 'rev rule', 'am', 1959, 'Leader of communist Cuba', 'Led the Cuban Revolution')
L('john-f-kennedy', 'state', 'am', 1962, '35th president of the United States', 'The Cuban Missile Crisis, and the race to the Moon')
L('martin-luther-king-jr', 'ref', 'am', 1963, 'Leader of the civil rights movement', 'The March on Washington: "I have a dream"')
L('deng-xiaoping', 'state', 'as', 1978, 'Leader of China', "Opened China's economy to the world")
L('ruhollah-khomeini', 'rev rule', 'me', 1979, 'Supreme leader of Iran', 'Led the Islamic Revolution')
L('mikhail-gorbachev', 'state ref', 'eu', 1985, 'Last leader of the Soviet Union', 'Glasnost, and a peaceful end to the Cold War')
L('nelson-mandela', 'rev state', 'af', 1994, 'First black president of South Africa', 'Ended apartheid, after twenty-seven years in prison')

# ---- the 2000s
L('vladimir-putin', 'rule', 'eu', 2000, 'President of Russia', 'Two decades in power, and the invasion of Ukraine')

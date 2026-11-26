from _lib import P, R, G

# ---------- Egypt, Mesopotamia, Anatolia, Persia ----------
P('Narmer', 'First king of a united Egypt', (-3150, -3100), 2, 'rule',
  'Joined Upper and Lower Egypt under one crown around 3100 BC, the start of three thousand years of pharaohs.',
  R(-3130, -3100, 'King of Upper and Lower Egypt', 'Egypt', at='memphis'))
P('Imhotep', 'Egyptian architect and sage', (-2700, -2620), 3, 'mind art',
  'Designed the step pyramid of Djoser at Saqqara, the first great stone building; later worshipped as a god of healing.',
  G(-2670, -2640, 'Builds the Step Pyramid', 'saqqara'))
P('Khufu', 'Pharaoh of Egypt', (-2620, -2566), 2, 'rule',
  'Built the Great Pyramid of Giza, the tallest building on Earth for nearly four thousand years.',
  R(-2589, -2566, 'Pharaoh of the Old Kingdom', 'Egypt', at='giza'))
P('Sargon of Akkad', 'Founder of the Akkadian Empire', (-2334, -2279), 1, 'rule war',
  "Conquered the Sumerian cities and ruled from the Persian Gulf to Syria: the world's first known empire.",
  G(-2334, -2279, 'King of Akkad and Sumer', 'akkad'))
P('Hammurabi', 'King of Babylon', (-1810, -1750), 1, 'rule reform',
  'United Mesopotamia and had 282 laws carved in stone, one of the earliest written law codes.',
  G(-1792, -1750, 'King of Babylon', 'babylon'))
P('Hatshepsut', 'Pharaoh of Egypt', (-1507, -1458), 2, 'rule',
  'One of the few women to rule Egypt as pharaoh; sent trading fleets to Punt and built the temple at Deir el-Bahari.',
  R(-1479, -1458, 'Pharaoh', 'Egypt', at='thebes'))
P('Thutmose III', 'Pharaoh of Egypt', (-1481, -1425), 2, 'rule war',
  "Egypt's greatest warrior pharaoh: won at Megiddo and pushed the empire to the Euphrates.",
  G(-1457, -1456, 'Battle of Megiddo', 'thebes', (35.18, 32.58)),
  R(-1458, -1425, 'Pharaoh', 'Egypt', at='thebes'))
P('Suppiluliuma I', 'King of the Hittites', (-1380, -1322), 3, 'rule war',
  'Made the Hittites a great power, conquering Mitanni and taking Syria from Egypt.',
  R(-1350, -1322, 'Great King of Hatti', 'Hittites', at='hattusa'))
P('Akhenaten', 'Pharaoh of Egypt', (-1380, -1336), 2, 'rule faith',
  "Abolished Egypt's old gods for the worship of the sun disc Aten and built a new capital at Amarna.",
  R(-1353, -1336, 'Pharaoh, worshipper of the Aten', 'Egypt', at='amarna'))
P('Nefertiti', 'Queen of Egypt', (-1370, -1330), 3, 'rule',
  "Akhenaten's queen and partner in his sun cult, famous for her painted bust.",
  G(-1353, -1336, 'Queen at Amarna', 'amarna'))
P('Tutankhamun', 'Pharaoh of Egypt', (-1341, -1323), 2, 'rule',
  'Boy king who restored the old gods; his intact tomb, found in 1922, is the richest ever discovered.',
  R(-1332, -1323, 'Pharaoh', 'Egypt', at='thebes'))
P('Ramesses II', 'Pharaoh of Egypt', (-1303, -1213), 1, 'rule war',
  'Fought the Hittites at Kadesh, signed the first known peace treaty and built Abu Simbel over a 66-year reign.',
  G(-1274, -1274, 'Battle of Kadesh', 'memphis', 'gaza', 'kadesh'),
  R(-1279, -1213, 'Pharaoh of the New Kingdom', 'Egypt', at='thebes'))
P('Moses', 'Prophet of Israel', (-1391, -1271), 2, 'faith',
  'In Hebrew tradition, led the Israelites out of slavery in Egypt and received the Ten Commandments on Mount Sinai.',
  G(-1313, -1273, 'The Exodus', 'avaris', 'mount_sinai', 'petra', (35.73, 31.77)), wiki='Moses')
P('David', 'King of Israel', (-1040, -970), 2, 'rule faith',
  'In the Hebrew Bible, the shepherd who slew Goliath and made Jerusalem the capital of a united Israel.',
  G(-1010, -970, 'King of Israel in Jerusalem', 'jerusalem'))
P('Solomon', 'King of Israel', (-990, -931), 2, 'rule faith',
  "David's son, remembered for his wisdom and for building the First Temple in Jerusalem.",
  G(-970, -931, 'King of Israel, builds the Temple', 'jerusalem'))
P('Tiglath-Pileser III', 'King of Assyria', (-780, -727), 3, 'rule war',
  'Reorganised the Assyrian army into a standing force and conquered Syria, Israel and Babylon.',
  R(-745, -727, 'King of Assyria', 'Assyria', at='nimrud'))
P('Sennacherib', 'King of Assyria', (-745, -681), 3, 'rule war',
  'Besieged Jerusalem, destroyed Babylon and made Nineveh a magnificent capital.',
  G(-701, -701, 'Campaign against Judah', 'nineveh', 'aleppo', 'tyre', (34.85, 31.56), 'jerusalem'),
  R(-705, -681, 'King of Assyria', 'Assyria', at='nineveh'))
P('Ashurbanipal', 'King of Assyria', (-685, -631), 2, 'rule mind',
  'Last great king of Assyria; conquered Egypt and Elam and gathered the clay-tablet library of Nineveh.',
  R(-669, -631, 'King of Assyria', 'Assyria', at='nineveh'))
P('Piye', 'King of Kush, pharaoh of Egypt', (-770, -714), 3, 'rule war',
  'Kushite king from Nubia who marched north and conquered Egypt, founding its 25th dynasty.',
  G(-728, -727, 'Conquest of Egypt', 'napata', 'thebes', 'memphis'),
  R(-744, -714, 'King of Kush', 'Kush', at='napata'))
P('Nebuchadnezzar II', 'King of Babylon', (-642, -562), 2, 'rule war',
  'Destroyed Jerusalem and its Temple, exiled the Jews to Babylon and built the Ishtar Gate.',
  G(-587, -586, 'Siege of Jerusalem', 'babylon', 'aleppo', 'jerusalem'),
  R(-605, -562, 'King of Babylon', 'Babylonia', at='babylon'))
P('Croesus', 'King of Lydia', (-595, -546), 3, 'rule',
  "Proverbially rich king who minted the first gold coins and lost his kingdom to Cyrus.",
  G(-560, -546, 'King of Lydia', 'sardis'))
P('Cyrus the Great', 'Founder of the Persian Empire', (-600, -530), 1, 'rule war',
  'Conquered Media, Lydia and Babylon, freed the Jewish exiles and built the largest empire the world had yet seen.',
  G(-547, -546, 'Conquest of Lydia', 'ecbatana', 'gordium', 'sardis'),
  G(-539, -539, 'Takes Babylon', 'susa', 'babylon'),
  G(-530, -530, 'Last campaign against the Massagetae', 'pasargadae', 'merv', (60.5, 42.0)),
  R(-559, -530, 'King of Persia', 'Achaemenid Empire', at='pasargadae'))
P('Cambyses II', 'King of Persia', (-560, -522), 3, 'rule war',
  "Cyrus's son, who conquered Egypt in 525 BC.",
  G(-525, -525, 'Conquest of Egypt', 'babylon', 'gaza', (32.55, 30.95), 'memphis'),
  R(-530, -522, 'King of Persia', 'Achaemenid Empire', at='susa'))
P('Darius I', 'King of Persia', (-550, -486), 1, 'rule',
  'Organised the Persian Empire into satrapies, built Persepolis and the Royal Road, and sent the army that lost at Marathon.',
  R(-522, -486, 'King of Kings', 'Achaemenid Empire', at='persepolis'))
P('Xerxes I', 'King of Persia', (-518, -465), 2, 'rule war',
  'Invaded Greece with a vast army, won at Thermopylae and burned Athens, then lost his fleet at Salamis.',
  G(-480, -479, 'Invasion of Greece', 'sardis', ('troy', -480), (26.4, 40.9), 'thessalonica', ('thermopylae', -479.5), 'athens', ('salamis', -479.3), 'sardis'),
  R(-486, -465, 'King of Kings', 'Achaemenid Empire', at='persepolis'))
P('Darius III', 'Last king of Achaemenid Persia', (-380, -330), 2, 'rule war',
  'Lost his empire to Alexander at Issus and Gaugamela and was murdered by his own satrap.',
  G(-331, -330, 'Flight after Gaugamela', 'gaugamela', 'ecbatana', (54.0, 36.2)),
  R(-336, -332, 'King of Kings', 'Achaemenid Empire', at='susa'))
P('Ptolemy I Soter', "Alexander's general, king of Egypt", (-367, -282), 3, 'rule war',
  "Took Egypt after Alexander's death, founded the Ptolemaic dynasty and the Library of Alexandria.",
  R(-305, -282, 'King of Egypt', 'Ptolemaic Kingdom', at='alexandria'))
P('Seleucus I Nicator', "Alexander's general, king of Asia", (-358, -281), 3, 'rule war',
  "Won the largest share of Alexander's empire, from Syria to the Indus, and founded Antioch.",
  R(-305, -281, 'King of the Seleucid Empire', 'Seleucid Kingdom', at='antioch'))
P('Antiochus III the Great', 'Seleucid king', (-241, -187), 3, 'rule war',
  "Rebuilt the Seleucid empire on a march to India, then lost to Rome at Magnesia.",
  G(-212, -205, 'Eastern expedition', 'antioch', 'ecbatana', 'balkh', (70.0, 34.4), 'kandahar', 'persepolis', 'antioch'),
  R(-222, -187, 'Seleucid king', 'Seleucid Kingdom', at='antioch'), wiki='Antiochus III the Great')
P('Mithridates VI', 'King of Pontus', (-135, -63), 2, 'rule war',
  "Rome's most stubborn enemy in the east: ordered the massacre of Romans in Asia and fought three wars against Rome.",
  G(-120, -63, 'King of Pontus', (35.15, 42.02)), wiki='Mithridates VI of Pontus')
P('Cleopatra', 'Last queen of Ptolemaic Egypt', (-69, -30), 1, 'rule',
  "Allied with Caesar and then Mark Antony to save Egypt's independence; her suicide made Egypt a Roman province.",
  G(-46, -44, 'In Rome with Caesar', 'rome'),
  R(-51, -30, 'Queen of Egypt', 'Ptolemaic Kingdom', at='alexandria'), wiki='Cleopatra')
P('Herod the Great', 'King of Judea', (-73, -4), 3, 'rule',
  "Rome's client king of Judea, who rebuilt the Temple in Jerusalem on a grand scale.",
  G(-37, -4, 'King of Judea', 'jerusalem'))

# ---------- Greece and Macedon ----------
P('Solon', 'Athenian lawgiver', (-630, -560), 3, 'reform',
  'Cancelled debts, freed debt slaves and gave Athens laws that laid the ground for democracy.',
  G(-594, -570, 'Archon and lawgiver of Athens', 'athens'))
P('Pythagoras', 'Greek philosopher and mathematician', (-570, -495), 2, 'mind',
  'Founded a brotherhood at Croton that taught that the world is ordered by number.',
  G(-570, -532, 'Youth on Samos', 'samos'), G(-531, -495, 'School at Croton', (17.13, 39.08)))
P('Leonidas I', 'King of Sparta', (-540, -480), 2, 'war',
  'Held the pass of Thermopylae against the Persian army with 300 Spartans and died there.',
  G(-489, -481, 'King of Sparta', 'sparta'), G(-480, -480, 'Thermopylae', 'sparta', 'corinth', 'thermopylae'))
P('Themistocles', 'Athenian statesman and general', (-524, -459), 2, 'war',
  "Built Athens's fleet and lured the Persian navy into defeat at Salamis.",
  G(-493, -472, 'Leader of Athens, victor of Salamis', 'athens'), G(-471, -459, 'Exile in Persia', 'athens', 'ephesus', (28.33, 37.86)))
P('Pericles', 'Leader of Athens', (-495, -429), 1, 'rule',
  "Led Athens at its height: democracy, the Parthenon and the Delian empire, until the plague killed him.",
  G(-461, -429, 'First citizen of Athens', 'athens'))
P('Herodotus', 'Greek historian', (-484, -425), 3, 'mind',
  "'The father of history': travelled the Persian world and wrote the story of the Greek-Persian wars.",
  G(-460, -430, 'Travels and histories', (27.42, 37.04), 'samos', 'athens', 'tyre', 'memphis', 'babylon', 'athens', (16.4, 39.7)))
P('Socrates', 'Athenian philosopher', (-470, -399), 1, 'mind',
  'Questioned everything in the streets of Athens and was condemned to death for it; the founder of Western philosophy.',
  G(-450, -399, 'Philosopher in Athens', 'athens'))
P('Thucydides', 'Athenian historian', (-460, -400), 3, 'mind',
  'Wrote the history of the Peloponnesian War as cold political analysis.',
  G(-431, -400, 'Writes the Peloponnesian War', 'athens'))
P('Alcibiades', 'Athenian general and turncoat', (-450, -404), 3, 'war',
  'Brilliant and faithless: led the Sicilian expedition, defected to Sparta, then to Persia, then back to Athens.',
  G(-415, -404, 'Sicily, Sparta, Persia and back', 'athens', ('syracuse', -414), ('sparta', -413), ('sardis', -411), ('samos', -410), ('athens', -407), (26.7, 40.4)))
P('Lysander', 'Spartan admiral', (-454, -395), 3, 'war',
  "Destroyed Athens's fleet at Aegospotami and ended the Peloponnesian War.",
  G(-407, -404, 'Admiral of Sparta', 'ephesus', (26.55, 40.33), 'athens'))
P('Plato', 'Greek philosopher', (-428, -348), 1, 'mind',
  "Socrates's student; founded the Academy in Athens and wrote the Republic.",
  G(-387, -348, 'The Academy in Athens', 'athens'))
P('Epaminondas', 'Theban general', (-418, -362), 3, 'war',
  "Broke Spartan power at Leuctra with a new oblique battle line and freed the helots of Messenia.",
  G(-371, -362, 'Leader of Thebes', 'thebes_gr', (23.2, 38.27), 'sparta', (22.37, 37.47)))
P('Philip II of Macedon', 'King of Macedon', (-382, -336), 2, 'rule war',
  "Built the Macedonian phalanx, beat Athens and Thebes at Chaeronea and made Greece follow Macedon.",
  G(-338, -338, 'Battle of Chaeronea', 'pella', 'thermopylae', 'chaeronea'),
  R(-359, -336, 'King of Macedon', 'Macedon and Hellenic League', at='pella'))
P('Demosthenes', 'Athenian orator', (-384, -322), 3, 'reform',
  'Roused Athens against Philip of Macedon in fiery speeches, the Philippics.',
  G(-355, -322, 'Orator of Athens', 'athens'))
P('Aristotle', 'Greek philosopher and scientist', (-384, -322), 1, 'mind',
  "Plato's pupil and Alexander's tutor; wrote on logic, biology, politics and ethics and founded the Lyceum.",
  G(-367, -348, "At Plato's Academy", 'athens'), G(-343, -336, 'Tutor to Alexander', 'pella'),
  G(-335, -323, 'The Lyceum', 'athens'))
P('Diogenes', 'Cynic philosopher', (-412, -323), 3, 'mind',
  'Lived in a jar in the marketplace to show how little a person needs.',
  G(-362, -323, 'Cynic in Athens and Corinth', 'athens', 'corinth'), wiki='Diogenes')
P('Alexander the Great', 'King of Macedon, conqueror of Persia', (-356, -323), 1, 'war rule',
  'Conquered the Persian Empire from Egypt to India in eleven years without losing a battle, spreading Greek culture across Asia.',
  R(-336, -335, 'King of Macedon', 'Macedon and Hellenic League', at='pella'),
  G(-334, -323, 'Conquest of the Persian Empire', ('pella', -334), ('granicus', -333.7), 'sardis', 'miletus', ('gordium', -333.2),
    ('issus', -332.2), ('tyre', -331.7), 'gaza', ('memphis', -331.2), 'siwa', ('alexandria', -330.9), 'tyre', ('gaugamela', -330.2),
    ('babylon', -330), 'susa', ('persepolis', -329.6), 'ecbatana', 'herat', 'kandahar', ('kabul', -328.5), ('balkh', -328.2),
    ('samarkand', -327.8), 'balkh', ('taxila', -326.6), ((73.5, 32.9, -325.6)), ((75.5, 31.8, -325.4)), ((68.4, 25.4, -324.8)),
    ((63.0, 26.0, -324.5)), ('persepolis', -323.9), ('susa', -323.7), ('babylon', -323.3)))
P('Euclid', 'Greek mathematician', (-325, -270), 2, 'mind',
  'Wrote the Elements in Alexandria, the textbook of geometry for two thousand years.',
  G(-300, -270, 'Teaches in Alexandria', 'alexandria'))
P('Archimedes', 'Greek mathematician and inventor', (-287, -212), 2, 'mind',
  "The ancient world's greatest mathematician; his machines held off the Roman siege of Syracuse.",
  G(-260, -212, 'Mathematician of Syracuse', 'syracuse'))
P('Eratosthenes', 'Greek scholar', (-276, -194), 3, 'mind',
  "Librarian of Alexandria who measured the Earth's circumference with shadows.",
  G(-245, -194, 'Librarian of Alexandria', 'alexandria'))
P('Pyrrhus of Epirus', 'King of Epirus', (-319, -272), 3, 'war',
  "Beat Rome twice at a cost so heavy it gave us 'Pyrrhic victory'.",
  G(-280, -275, 'War with Rome', (20.85, 39.62), (17.24, 40.47), (16.33, 40.22), (15.65, 41.13), 'syracuse', (14.77, 41.13)))

# ---------- Rome and Carthage ----------
P('Hamilcar Barca', 'Carthaginian general', (-275, -228), 3, 'war',
  "Fought Rome in Sicily, then won Carthage a new empire in Spain; Hannibal's father.",
  G(-247, -241, 'War in Sicily', (12.57, 38.03)), G(-237, -228, 'Conquest of Spain', 'carthage', 'cadiz', (-3.79, 38.0)))
P('Hannibal', 'Carthaginian general', (-247, -183), 1, 'war',
  'Crossed the Alps with elephants and destroyed Roman armies at Trebia, Trasimene and Cannae before losing at Zama.',
  G(-221, -219, 'Commander in Spain', 'new_carthage', (-0.27, 39.68)),
  G(-218, -203, 'War in Italy', ('new_carthage', -218), (2.0, 42.0), (4.6, 44.3), (6.9, 45.2), ('turin', -217.8), ((9.6, 45.0, -217.6)),
    ('lake_trasimene', -216.6), ('cannae', -215.4), ('capua', -214.5), ((15.8, 40.6, -212)), ((16.6, 39.5, -208)), ((16.6, 39.1, -204))),
  G(-202, -202, 'Battle of Zama', (16.6, 39.1), 'zama'),
  G(-201, -196, 'Leader of Carthage', 'carthage'),
  G(-195, -183, 'Exile in the east', 'tyre', 'antioch', (27.27, 38.71), (29.5, 40.78)), wiki='Hannibal')
P('Scipio Africanus', 'Roman general', (-236, -183), 2, 'war',
  'Took Spain from Carthage and beat Hannibal at Zama, ending the Second Punic War.',
  G(-210, -206, 'Conquest of Spain', 'new_carthage', (-5.7, 37.6)),
  G(-204, -202, 'Invasion of Africa', 'syracuse', 'utica', 'zama'),
  G(-201, -184, 'First man of Rome', 'rome'))
P('Cato the Elder', 'Roman statesman', (-234, -149), 3, 'reform',
  "Stern guardian of old Roman ways who ended every speech with 'Carthage must be destroyed'.",
  G(-184, -149, 'Censor in Rome', 'rome'))
P('Scipio Aemilianus', 'Roman general', (-185, -129), 3, 'war',
  'Destroyed Carthage in 146 BC and Numantia in 133 BC.',
  G(-147, -146, 'Destruction of Carthage', 'utica', 'carthage'), G(-134, -133, 'Siege of Numantia', 'new_carthage', 'numantia'))
P('Tiberius Gracchus', 'Roman tribune and reformer', (-163, -133), 3, 'reform',
  "Tried to give public land to Rome's poor and was clubbed to death by senators.",
  G(-133, -133, 'Tribune of the plebs', 'rome'))
P('Gaius Gracchus', 'Roman tribune and reformer', (-154, -121), 3, 'reform',
  "Took up his brother's land reform and cheap grain for the poor, and died like him in political violence.",
  G(-123, -121, 'Tribune of the plebs', 'rome'))
P('Gaius Marius', 'Roman general and seven times consul', (-157, -86), 2, 'war',
  'Opened the legions to the landless poor, beat Jugurtha and the invading Cimbri and Teutones, and fought Sulla.',
  G(-107, -105, 'War against Jugurtha', 'utica', (8.0, 35.4)),
  G(-102, -101, 'Destroys the Cimbri and Teutones', (5.45, 43.53), (8.42, 45.32)),
  R(-100, -100, 'Consul', 'Roman Republic', at='rome'), G(-87, -86, 'Return and purge of Rome', 'rome'))
P('Sulla', 'Roman general and dictator', (-138, -78), 2, 'war rule',
  'First Roman to march on Rome with his army; won the civil war and ruled as dictator.',
  G(-87, -83, 'War against Mithridates', 'brundisium', 'athens', (22.9, 38.45), (26.1, 39.25), 'brundisium'),
  R(-82, -79, 'Dictator of Rome', 'Roman Republic', at='rome'))
P('Spartacus', 'Gladiator and rebel leader', (-111, -71), 2, 'war',
  'Led a slave army of up to 70,000 that beat several Roman armies and roamed Italy for two years.',
  G(-73, -71, 'Slave revolt', ('capua', -73), ((14.43, 40.82, -72.8)), ((16.2, 40.0, -72.4)), ((12.0, 44.0, -72)), ((10.93, 44.65, -71.7)),
    ((15.6, 40.6, -71.3)), ((16.0, 38.9, -71.1)), ((15.4, 40.55, -70.5))))
P('Pompey', 'Roman general, member of the First Triumvirate', (-106, -48), 1, 'war rule',
  "Rome's greatest general before Caesar: cleared the seas of pirates, conquered the east, then lost the civil war to Caesar.",
  G(-76, -71, 'War in Spain', 'rome', 'valencia', (-1.0, 41.6)),
  G(-67, -62, 'Pirates and the conquest of the east', ('rome', -67), ((28.22, 36.43, -66.5)), ((35.15, 42.02, -65)),
    ('antioch', -64), ('damascus', -63.5), ('jerusalem', -63), ('rome', -62)),
  R(-61, -50, 'First Triumvirate', 'Roman Republic', at='rome'),
  G(-49, -48, 'Civil war against Caesar', 'rome', 'brundisium', ('pharsalus', -48.4), (32.55, 31.05)), wiki='Pompey')
P('Marcus Licinius Crassus', 'Richest man in Rome, member of the First Triumvirate', (-115, -53), 2, 'rule war',
  'Crushed the revolt of Spartacus, bankrolled Caesar, and died leading an army against Parthia at Carrhae.',
  G(-71, -71, 'Crushes Spartacus', (16.0, 39.2), 'rome'),
  R(-60, -55, 'First Triumvirate', 'Roman Republic', at='rome'),
  G(-54, -53, 'Invasion of Parthia', 'brundisium', 'antioch', (38.43, 36.8), (39.03, 36.86)))
P('Cicero', 'Roman orator and statesman', (-106, -43), 2, 'reform mind',
  "Rome's greatest orator: saved the Republic from Catiline's plot, defended it against Antony, and was murdered for it.",
  G(-75, -43, 'Orator and consul in Rome', 'rome'))
P('Cato the Younger', 'Roman senator', (-95, -46), 3, 'reform',
  "The Republic's most stubborn defender, who killed himself at Utica rather than live under Caesar.",
  G(-63, -49, 'Senator in Rome', 'rome'), G(-48, -46, 'Last stand in Africa', 'utica'))
P('Julius Caesar', 'Roman general and dictator', (-100, -44), 1, 'war rule',
  'Conquered Gaul, crossed the Rubicon, beat Pompey in civil war and made himself dictator for life before his murder.',
  R(-60, -59, 'First Triumvirate, consul', 'Roman Republic', at='rome'),
  G(-58, -50, 'Conquest of Gaul', ('geneva', -58), ((4.03, 46.92, -57.6)), ((7.3, 47.9, -57.3)), ((3.6, 49.6, -56.7)), ((-2.7, 47.5, -55.6)),
    ((7.5, 50.4, -54.6)), ((1.6, 50.75, -54.3)), ((0.5, 51.3, -54.1)), ((1.6, 50.75, -53.8)), ((5.0, 49.3, -53)), ('gergovia', -51.6),
    ('alesia', -51.3), ((2.5, 47.0, -50.5)), ((3.0, 50.0, -50))),
  G(-49, -45, 'Civil war against Pompey', ('rubicon', -49), ('rome', -48.9), ((2.0, 42.0, -48.8)), ((0.6, 41.6, -48.6)), ('brundisium', -48.2),
    ('pharsalus', -47.4), ('alexandria', -47.2), ((35.0, 40.9, -46.6)), ('utica', -46.3), ((-4.9, 37.4, -45.3))),
  R(-46, -44, 'Dictator of Rome', 'Roman Republic', at='rome'))
P('Vercingetorix', 'Chief of the Arverni, leader of the Gauls', (-82, -46), 2, 'war',
  "United the Gauls against Caesar, won at Gergovia, and surrendered at Alesia after a famous siege.",
  G(-52, -52, 'Revolt of Gaul', 'gergovia', 'bibracte', 'alesia'))
P('Marcus Junius Brutus', "Caesar's assassin", (-85, -42), 3, 'war',
  "Led the plot to kill Caesar in the name of the Republic, and died after losing at Philippi.",
  G(-44, -42, 'From the Ides of March to Philippi', 'rome', 'athens', (27.0, 38.4), 'philippi'), wiki='Marcus Junius Brutus')
P('Mark Antony', 'Roman general, member of the Second Triumvirate', (-83, -30), 1, 'war rule',
  "Caesar's lieutenant who ruled the east as triumvir with Cleopatra and lost everything to Octavian at Actium.",
  R(-43, -42, 'Second Triumvirate', 'Roman Republic', at='rome'),
  G(-42, -42, 'Battle of Philippi', 'brundisium', 'philippi'),
  G(-41, -32, 'Triumvir in the east, with Cleopatra', ('ephesus', -41), ((34.9, 36.92, -40.8)), ('alexandria', -40.5), ('athens', -38),
    ('antioch', -37), ((45.5, 37.0, -36)), ('alexandria', -35)),
  G(-31, -30, 'Actium and the fall of Alexandria', 'actium', 'alexandria'))
P('Marcus Aemilius Lepidus', 'Member of the Second Triumvirate', (-89, -13), 3, 'rule',
  'The third and weakest triumvir with Antony and Octavian; given Africa, he was pushed aside in 36 BC.',
  R(-43, -41, 'Second Triumvirate', 'Roman Republic', at='rome'), G(-40, -36, 'Triumvir in Africa', 'carthage'),
  G(-35, -13, 'Pontifex maximus in retirement', (12.94, 41.39)), wiki='Marcus Aemilius Lepidus (triumvir)')
P('Augustus', 'First Roman emperor', (-63, 14), 1, 'rule',
  'Caesar\'s heir: won the civil wars, ended the Republic and ruled as Rome\'s first emperor, opening two centuries of Pax Romana.',
  R(-43, -32, 'Second Triumvirate', 'Roman Republic', at='rome'),
  G(-31, -30, 'War against Antony and Cleopatra', 'actium', 'alexandria'),
  R(-29, 14, 'Emperor of Rome', 'Roman Empire', 'Roman Republic', at='rome'))
P('Virgil', 'Roman poet', (-70, -19), 3, 'art',
  "Wrote the Aeneid, Rome's national epic of its founding.",
  G(-42, -19, 'Poet in Rome and Naples', 'rome', 'naples'))

# ---------- India ----------
P('Mahavira', 'Founder of Jainism as it is known today', (-599, -527), 2, 'faith',
  'The 24th Jain tirthankara: taught non-violence to all living things and the path of the soul\'s liberation.',
  G(-569, -527, 'Teaching in the Ganges plain', 'vaishali', 'rajgir', (85.47, 25.09)))
P('Gautama Buddha', 'Founder of Buddhism', (-563, -483), 1, 'faith',
  'A prince who gave up his palace to seek the end of suffering; enlightened under the Bodhi tree, he taught for 45 years.',
  G(-563, -535, 'Prince of the Shakyas', 'lumbini', 'kapilavastu'),
  G(-534, -483, 'Enlightenment and teaching', ('kapilavastu', -534), ('rajgir', -532), ('bodh_gaya', -528), ('sarnath', -527.5),
    ('rajgir', -526), ('vaishali', -510), ('varanasi', -500), ((82.04, 27.51, -490)), ('vaishali', -484), ('kushinagar', -483)), wiki='The Buddha')
P('Chandragupta Maurya', 'Founder of the Maurya Empire', (-350, -295), 2, 'rule war',
  'Overthrew the Nanda kings, drove out Alexander\'s garrisons and united most of India.',
  R(-321, -297, 'Maurya emperor', 'Mauryan Empire', 'Magadha', at='pataliputra'))
P('Chanakya', 'Indian statesman and author of the Arthashastra', (-375, -283), 3, 'mind',
  "Chandragupta's adviser, credited with the Arthashastra, a ruthless handbook of statecraft.",
  G(-321, -297, 'Adviser at Pataliputra', 'pataliputra'))
P('Porus', 'King of the Punjab', (-360, -317), 3, 'war',
  "Fought Alexander at the Hydaspes with war elephants and so impressed him that he kept his kingdom.",
  G(-326, -317, 'King on the Hydaspes', (73.5, 32.9)))
P('Ashoka', 'Maurya emperor', (-304, -232), 1, 'rule faith',
  'Conquered Kalinga, was horrified by the slaughter, embraced Buddhism and carved edicts of peace across India.',
  G(-261, -261, 'Conquest of Kalinga', 'pataliputra', 'kalinga'),
  R(-268, -232, 'Maurya emperor', 'Mauryan Empire', at='pataliputra'))

# ---------- China ----------
P('King Wu of Zhou', 'Founder of the Zhou dynasty', (-1076, -1043), 3, 'rule war',
  'Overthrew the last Shang king at Muye and founded the Zhou, the longest dynasty in Chinese history.',
  G(-1046, -1043, 'Conquers the Shang', 'haojing', (114.0, 35.2), 'anyang'))
P('Duke of Zhou', 'Regent of early Zhou China', (-1100, -1032), 3, 'rule mind',
  'Regent for the boy king Cheng; crushed a great rebellion and was revered by Confucius as the model statesman.',
  G(-1042, -1036, 'Regent of Zhou', 'luoyang'))
P('Laozi', 'Chinese philosopher, founder of Taoism', (-571, -471), 2, 'faith mind',
  'Traditionally the author of the Tao Te Ching, the root text of Taoism; said to have left China riding west on an ox.',
  G(-530, -471, 'Archivist at the Zhou court', 'luoyang', (110.4, 34.6)))
P('Sun Tzu', 'Chinese general and strategist', (-544, -496), 2, 'war mind',
  'Credited with The Art of War, the most famous book of strategy ever written.',
  G(-512, -496, 'General of Wu', 'suzhou', (113.0, 31.0)))
P('Confucius', 'Chinese philosopher', (-551, -479), 1, 'mind faith',
  "Taught duty, learning and good government; his sayings shaped China, Korea and Japan for two thousand years.",
  G(-501, -498, 'Minister in Lu', 'qufu'),
  G(-497, -484, 'Wandering the states', ('qufu', -497), ((114.3, 35.75, -496)), ((115.65, 34.42, -492)), ((114.65, 33.75, -489)),
    ((114.3, 32.98, -488)), ((113.0, 32.1, -487)), ((114.3, 35.75, -486)), ('qufu', -484)),
  G(-483, -479, 'Teaching in Lu', 'qufu'))
P('Mencius', 'Confucian philosopher', (-372, -289), 3, 'mind',
  "Taught that people are born good and that a ruler who oppresses them loses Heaven's mandate.",
  G(-330, -289, 'Advising the warring kings', (117.08, 35.4), 'linzi', (114.3, 34.8)))
P('Shang Yang', 'Qin statesman and reformer', (-390, -338), 3, 'reform',
  "His harsh laws and reforms made Qin the strongest of the warring states.",
  G(-356, -338, 'Chancellor of Qin', 'xianyang'))
P('Bai Qi', 'Qin general', (-332, -257), 3, 'war',
  "Qin's most feared general, said to have killed 400,000 surrendered Zhao soldiers after Changping.",
  G(-293, -257, 'Wars of conquest for Qin', 'xianyang', (112.6, 34.6), 'ying', (112.9, 35.8)))
P('Qin Shi Huang', 'First emperor of China', (-259, -210), 1, 'rule',
  'Conquered the six rival kingdoms, unified China in 221 BC, standardised its script and began the Great Wall.',
  R(-247, -222, 'King of Qin', 'Qin', 'Zhou states', at='xianyang'),
  R(-221, -210, 'First Emperor of China', 'Qin', 'Han Empire', at='xianyang'))
P('Xiang Yu', 'Hegemon-King of Western Chu', (-232, -202), 3, 'war',
  'Destroyed the Qin army and burned its capital, then lost the war for China to Liu Bang.',
  G(-207, -202, 'Fall of Qin and war with Han', (115.2, 36.6), 'xianyang', 'xuzhou', (117.9, 32.95)))
P('Emperor Gaozu of Han', 'Founder of the Han dynasty', (-256, -195), 2, 'rule',
  'Peasant-born rebel Liu Bang, who beat Xiang Yu and founded the Han dynasty.',
  G(-206, -203, 'War against Xiang Yu', (107.03, 33.07), 'xianyang', 'xuzhou'),
  R(-202, -195, 'Emperor of Han', 'Han Empire', 'Qin', at='changan'))
P('Modu Chanyu', 'Ruler of the Xiongnu', (-234, -174), 3, 'rule war',
  'Forged the Xiongnu steppe empire and forced the Han to pay tribute.',
  R(-209, -174, 'Chanyu of the Xiongnu', 'Xiongnu', at=(103.0, 46.0)))
P('Emperor Wu of Han', 'Emperor of China', (-156, -87), 2, 'rule',
  'Pushed back the Xiongnu, opened the Silk Road and made Confucianism the creed of the state.',
  R(-141, -87, 'Emperor of Han', 'Han Empire', at='changan'))
P('Zhang Qian', 'Han envoy and explorer', (-164, -113), 2, 'explore',
  'His journey to Central Asia, with ten years as a Xiongnu captive, opened the Silk Road.',
  G(-138, -126, 'Journey to the Western Regions', ('changan', -138), ((103.8, 36.0, -137.5)), ((94.66, 40.14, -137)), ((96.0, 42.0, -136)),
    ((72.8, 40.8, -128)), ('samarkand', -128.6), ('balkh', -128.2), ((89.2, 40.0, -127)), ('changan', -126)))
P('Sima Qian', 'Chinese historian', (-145, -86), 3, 'mind',
  "Wrote the Records of the Grand Historian, the model for all later Chinese histories.",
  G(-108, -86, 'Grand Historian at Chang\'an', 'changan'))

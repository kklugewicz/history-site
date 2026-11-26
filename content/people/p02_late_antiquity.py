from _lib import P, R, G

ROME = ('Roman Empire',)
TETRARCHY = ('Rome (Constantinus)', 'Rome (Diocletianus)', 'Rome (Galerius)', 'Rome (Maximian)')
EAST = ('Eastern Roman Empire', 'Byzantine Empire')
SASAN = ('Sasanian Empire', 'Persia', 'Parthian Empire')

# ---------- Rome and the early Christians ----------
P('Jesus', 'Founder of Christianity', (-4, 30), 1, 'faith',
  'Jewish preacher from Galilee whose teaching, crucifixion and reported resurrection became the faith of a third of humanity.',
  G(-4, 26, 'Youth in Nazareth', 'nazareth'),
  G(27, 30, 'Ministry and crucifixion', ('nazareth', 27), (35.55, 32.33), 'capernaum', (35.4, 32.95), 'capernaum', 'jericho', ('jerusalem', 30.4)))
P('Arminius', 'Chieftain of the Cherusci', (-18, 21), 2, 'war',
  'Trained as a Roman officer, he led three legions into ambush in the Teutoburg Forest and kept Rome out of Germany.',
  G(9, 9, 'Ambush in the Teutoburg Forest', (8.8, 51.8), 'teutoburg'), G(10, 21, 'Leader of the German tribes', (9.0, 52.1)))
P('Tiberius', 'Roman emperor', (-42, 37), 3, 'rule',
  "Augustus's stepson and heir, a gloomy and able ruler who spent his last years on Capri.",
  G(26, 37, 'Rules from Capri', (14.24, 40.55)), R(14, 37, 'Roman emperor', *ROME, at='rome'))
P('Saint Peter', 'Apostle, first bishop of Rome', (-1, 64), 2, 'faith',
  'Fisherman of Galilee who became the leader of the apostles; Catholics count him the first pope.',
  G(28, 49, 'Leader of the apostles', 'capernaum', 'jerusalem'), G(50, 64, 'Antioch and Rome', 'antioch', 'rome'))
P('Paul the Apostle', 'Christian missionary', (5, 64), 1, 'faith',
  'Persecutor turned apostle whose journeys and letters carried Christianity to the Greek and Roman world.',
  G(34, 45, 'Conversion and early mission', (36.29, 33.51), 'jerusalem', 'tarsus', 'antioch'),
  G(46, 48, 'First journey', 'antioch', (33.9, 35.18), (32.4, 34.77), (30.85, 36.96), (31.19, 38.31), 'konya', (32.33, 37.58), (33.36, 37.35), 'antioch'),
  G(49, 52, 'Second journey', 'antioch', 'tarsus', (33.36, 37.35), (32.33, 37.58), (26.16, 39.75), ('philippi', 50), 'thessalonica', (22.2, 40.52),
    'athens', ('corinth', 50.6), ('corinth', 52), 'ephesus', 'caesarea', 'jerusalem'),
  G(53, 57, 'Third journey', 'antioch', 'ankara', ('ephesus', 54), ('ephesus', 56.5), 'thessalonica', ('corinth', 57), 'miletus', 'tyre', 'jerusalem'),
  G(58, 59, 'Prisoner at Caesarea', 'caesarea'),
  G(60, 60, 'Voyage to Rome and shipwreck', 'caesarea', 'sidon', (29.98, 36.26), (24.8, 34.93), (14.4, 35.9), 'syracuse', (15.65, 38.11), (14.12, 40.82), 'rome'),
  G(61, 64, 'Prisoner in Rome', 'rome'))
P('Claudius', 'Roman emperor', (-10, 54), 3, 'rule',
  'Scholarly emperor, mocked for his stammer, who conquered Britain.',
  G(43, 43, 'Invasion of Britain', 'rome', 'marseille', (1.6, 50.7), (0.9, 51.89)), R(41, 54, 'Roman emperor', *ROME, at='rome'))
P('Nero', 'Roman emperor', (37, 68), 2, 'rule',
  'Murdered his mother, sang while Rome burned in 64, blamed the Christians and died by suicide when the army turned on him.',
  R(54, 68, 'Roman emperor', *ROME, at='rome'))
P('Boudica', 'Queen of the Iceni', (30, 61), 2, 'war',
  'Led the Britons in revolt against Rome and burned Colchester, London and St Albans before her defeat.',
  G(60, 61, 'Revolt against Rome', (1.0, 52.6), (0.9, 51.89), (-0.09, 51.51), (-0.36, 51.75), (-1.5, 52.55)))
P('Vespasian', 'Roman emperor', (9, 79), 3, 'rule war',
  'Crushed the Jewish revolt, won the civil war of 69 and built the Colosseum.',
  G(67, 69, 'Jewish War', 'antioch', 'tyre', 'caesarea', 'alexandria'), R(69, 79, 'Roman emperor', *ROME, at='rome'))
P('Titus', 'Roman emperor', (39, 81), 3, 'war rule',
  'Captured Jerusalem and destroyed the Second Temple in 70; as emperor he faced the eruption of Vesuvius.',
  G(70, 70, 'Siege of Jerusalem', 'caesarea', 'jerusalem'), R(79, 81, 'Roman emperor', *ROME, at='rome'))
P('Trajan', 'Roman emperor', (53, 117), 2, 'rule war',
  'Conquered Dacia and Mesopotamia, bringing the Roman Empire to its greatest size.',
  G(101, 106, 'Conquest of Dacia', 'rome', (22.66, 44.63), (23.31, 45.62)),
  G(114, 117, 'War with Parthia', 'antioch', (44.3, 37.1), 'ctesiphon', (47.8, 30.5), (32.27, 36.25)),
  R(98, 117, 'Roman emperor', *ROME, at='rome'))
P('Hadrian', 'Roman emperor', (76, 138), 2, 'rule',
  'Gave up conquest, built his wall across Britain and spent half his reign touring the provinces.',
  G(121, 125, 'Tour of the provinces', 'rome', 'lyon', (-2.3, 55.0), (-6.0, 37.4), 'ephesus', 'athens'),
  G(128, 132, 'Africa, the east and Egypt', 'carthage', 'athens', 'antioch', 'jerusalem', 'alexandria', 'thebes', 'athens'),
  R(117, 138, 'Roman emperor', *ROME, at='rome'))
P('Bar Kokhba', 'Leader of the last Jewish revolt', (100, 135), 3, 'war',
  "Ruled an independent Judea for three years until Rome crushed the revolt and barred Jews from Jerusalem.",
  G(132, 135, 'Revolt against Rome', 'jerusalem', (35.13, 31.73)), wiki='Simon bar Kokhba')
P('Ptolemy', 'Astronomer and geographer', (100, 170), 3, 'mind',
  'His Almagest, with the Earth at the centre of the universe, guided astronomy for 1,400 years.',
  G(127, 168, 'Astronomer in Alexandria', 'alexandria'))
P('Marcus Aurelius', 'Roman emperor and Stoic philosopher', (121, 180), 1, 'rule mind',
  "The philosopher-emperor: fought the Germans on the Danube for years and wrote the Meditations in camp.",
  G(168, 180, 'Wars on the Danube', 'rome', (13.37, 45.77), (16.86, 48.11), (18.2, 48.3), 'vienna'),
  R(161, 180, 'Roman emperor', *ROME, at='rome'))
P('Galen', 'Greek physician', (129, 216), 3, 'mind',
  "Physician to emperors whose medicine was taught in Europe and the Islamic world until the 1600s.",
  G(162, 216, 'Physician in Rome', 'rome'))
P('Septimius Severus', 'Roman emperor', (145, 211), 3, 'rule war',
  'African-born emperor who sacked Ctesiphon and died campaigning in Scotland at York.',
  G(208, 211, 'Campaign in Britain', 'rome', (1.6, 50.7), 'york'), R(193, 211, 'Roman emperor', *ROME, at='rome'))
P('Ardashir I', 'Founder of the Sasanian Empire', (180, 242), 2, 'rule',
  "Overthrew the Parthians in 224 and founded Persia's Sasanian dynasty.",
  R(224, 242, 'King of Kings of Iran', *SASAN, at='ctesiphon'))
P('Shapur I', 'Sasanian king of kings', (215, 270), 2, 'rule war',
  'Beat three Roman emperors and took Emperor Valerian prisoner at Edessa.',
  G(260, 260, 'Captures Emperor Valerian', 'ctesiphon', (38.79, 37.16)), R(240, 270, 'King of Kings', *SASAN, at='ctesiphon'))
P('Mani', 'Founder of Manichaeism', (216, 274), 3, 'faith',
  'Prophet who taught a cosmic war of light and darkness; his religion spread from Rome to China.',
  G(240, 242, 'Mission to India', 'ctesiphon', 'hormuz', (67.0, 25.0)), G(242, 274, 'Prophet at the Persian court', 'ctesiphon', (48.53, 32.3)))
P('Zenobia', 'Queen of Palmyra', (240, 274), 2, 'rule war',
  "Broke away from Rome and conquered Egypt and Anatolia before Aurelian brought her to Rome in chains.",
  G(267, 272, 'Queen of Palmyra', 'palmyra'), G(273, 274, 'Captive in Rome', 'rome'))
P('Aurelian', 'Roman emperor', (214, 275), 3, 'rule war',
  "Reunited the broken empire, beat Zenobia and built Rome's Aurelian walls.",
  G(272, 273, 'War against Palmyra', 'nicomedia', 'antioch', 'palmyra'), R(270, 275, 'Roman emperor', *ROME, at='rome'))
P('Diocletian', 'Roman emperor', (244, 311), 2, 'rule reform',
  'Split the empire among four emperors, reformed the army and taxes, and launched the last great persecution of Christians.',
  G(305, 311, 'Retirement at Split', (16.44, 43.51)), R(284, 305, 'Roman emperor', 'Rome (Diocletianus)', *ROME, at='nicomedia'))
P('Constantine the Great', 'Roman emperor', (272, 337), 1, 'rule faith',
  'First Christian emperor: won at the Milvian Bridge, legalised Christianity and founded Constantinople.',
  G(312, 312, 'Battle of the Milvian Bridge', 'trier', 'turin', 'verona', (12.47, 41.94)),
  R(306, 337, 'Roman emperor', 'Rome (Constantinus)', *ROME, at='constantinople'))
P('Arius', 'Christian priest', (256, 336), 3, 'faith',
  "Taught that the Son was made by the Father; condemned at Nicaea, but his Arian creed converted the Goths.",
  G(318, 336, 'Priest in Alexandria', 'alexandria'))
P('Athanasius of Alexandria', 'Bishop of Alexandria', (296, 373), 3, 'faith',
  'Champion of the Nicene Creed against Arianism, exiled five times.',
  G(328, 373, 'Bishop of Alexandria', 'alexandria'))
P('Shapur II', 'Sasanian king of kings', (309, 379), 3, 'rule war',
  'Crowned before birth, he ruled seventy years and beat the Roman invasion of Julian.',
  R(309, 379, 'King of Kings', *SASAN, at='ctesiphon'))
P('Ezana of Axum', 'King of Aksum', (320, 360), 3, 'rule faith',
  'Made Aksum, in Ethiopia, one of the first Christian kingdoms in the world.',
  R(330, 356, 'King of Aksum', 'Axum', at='axum'))
P('Julian', 'Roman emperor', (331, 363), 3, 'rule faith',
  'The last pagan emperor, who tried to undo Christianity and died invading Persia.',
  G(363, 363, 'Invasion of Persia', 'antioch', (39.03, 36.86), (40.45, 35.15), 'ctesiphon', (44.1, 34.0)),
  R(361, 362, 'Roman emperor', *TETRARCHY, at='constantinople'), wiki='Julian (emperor)')
P('Theodosius I', 'Roman emperor', (347, 395), 2, 'rule faith',
  'Made Nicene Christianity the religion of the empire and was the last emperor to rule both halves.',
  R(379, 395, 'Roman emperor', 'Rome (Diocletianus)', *TETRARCHY, at='constantinople'))
P('Ambrose', 'Bishop of Milan', (339, 397), 3, 'faith',
  "Made Emperor Theodosius do penance for a massacre, and baptised Augustine.",
  G(374, 397, 'Bishop of Milan', 'milan'))
P('Jerome', 'Christian scholar', (347, 420), 3, 'faith mind',
  'Translated the Bible into Latin, the Vulgate, in a cave at Bethlehem.',
  G(386, 420, 'Translating the Bible in Bethlehem', 'bethlehem'))
P('Augustine of Hippo', 'Christian theologian', (354, 430), 1, 'faith mind',
  "Wrote the Confessions and the City of God and shaped Western Christianity's ideas of sin and grace.",
  G(354, 370, 'Youth at Thagaste', 'thagaste'), G(371, 382, 'Student and teacher in Carthage', 'carthage'),
  G(383, 387, 'Rome and Milan, conversion', 'rome', 'milan'), G(388, 390, 'Return to Africa', 'thagaste'),
  G(391, 430, 'Bishop of Hippo', 'hippo'))
P('Hypatia', 'Philosopher and mathematician', (360, 415), 3, 'mind',
  'Taught philosophy and mathematics in Alexandria until a Christian mob murdered her.',
  G(390, 415, 'Teacher in Alexandria', 'alexandria'))
P('Stilicho', 'Roman general', (359, 408), 3, 'war',
  'Half-Vandal general who defended the West against Alaric until the emperor had him executed.',
  G(395, 408, 'Commander of the West', 'milan', 'ravenna'))
P('Alaric I', 'King of the Visigoths', (370, 410), 2, 'war',
  "Led the Visigoths through the Balkans and Italy and sacked Rome in 410, the first time in 800 years.",
  G(395, 410, 'Wanderings and the sack of Rome', ('adrianople', 395), ('athens', 396), ((21.8, 37.6, 397)), ((20.5, 39.6, 398)), ((7.92, 44.7, 402)),
    ('verona', 403), ((20.5, 39.6, 405)), ('rome', 408.8), ('rome', 410.6), ((16.25, 39.3, 410.95))))
P('Saint Patrick', 'Apostle of Ireland', (385, 461), 2, 'faith',
  "A Briton enslaved in Ireland who escaped, then returned as a bishop and converted the Irish.",
  G(432, 461, 'Mission to Ireland', (-5.6, 54.35), 'armagh', (-7.0, 53.6)))
P('Attila', 'King of the Huns', (406, 453), 1, 'war rule',
  "'The Scourge of God': ruled from the Rhine to the Caspian, ravaged the Balkans, Gaul and Italy.",
  G(451, 451, 'Invasion of Gaul', (19.0, 47.0), (6.18, 49.12), 'orleans', (4.4, 48.9), (19.0, 47.0)),
  G(452, 452, 'Invasion of Italy', (19.0, 47.0), (13.37, 45.77), 'milan', (10.8, 45.2), (19.0, 47.0)),
  R(434, 453, 'King of the Huns', 'Hunnic Empire', at=(20.0, 46.6)))
P('Flavius Aetius', 'Roman general', (391, 454), 3, 'war',
  "'The last of the Romans': held Gaul for the West and stopped Attila at the Catalaunian Plains.",
  G(433, 450, 'Commander of the West', 'ravenna', (4.63, 43.68)),
  G(451, 451, 'Battle of the Catalaunian Plains', (4.63, 43.68), 'orleans', (4.4, 48.9)), G(452, 454, 'Commander of the West', 'ravenna'))
P('Pope Leo I', 'Pope', (400, 461), 3, 'faith',
  'Met Attila on the Mincio and persuaded him to turn back from Rome.',
  G(440, 461, 'Bishop of Rome', 'rome'))
P('Gaiseric', 'King of the Vandals', (389, 477), 3, 'war rule',
  'Led the Vandals into Africa, took Carthage and sacked Rome in 455.',
  G(429, 439, 'Conquest of Africa', (-5.6, 36.0), 'oran', 'hippo', 'carthage'),
  G(455, 455, 'Sack of Rome', 'carthage', 'rome', 'carthage'),
  R(439, 477, 'King of the Vandals', 'Vandals', at='carthage'))
P('Odoacer', 'King of Italy', (433, 493), 3, 'rule',
  'German general who deposed the last western emperor, Romulus Augustulus, in 476.',
  R(476, 493, 'King of Italy', 'Western Roman Empire', at='ravenna'))
P('Theodoric the Great', 'King of the Ostrogoths', (454, 526), 2, 'rule',
  "Took Italy from Odoacer and ruled Goths and Romans together in peace from Ravenna.",
  G(488, 493, 'Conquest of Italy', (20.5, 44.8), 'verona', 'ravenna'),
  R(494, 526, 'King of Italy', 'Ostrogoths', at='ravenna'))
P('Clovis I', 'King of the Franks', (466, 511), 2, 'rule',
  'United the Franks, became a Catholic and founded the Frankish kingdom that became France.',
  G(507, 507, 'Battle of Vouillé', 'paris', 'tours', (0.16, 46.64), 'toulouse'),
  R(481, 511, 'King of the Franks', 'Franks', 'Frankish Kingdom', at='paris'))
P('Benedict of Nursia', 'Father of Western monasticism', (480, 547), 2, 'faith',
  "Wrote the Rule of Saint Benedict, the pattern for monastic life in Europe, at Monte Cassino.",
  G(500, 528, 'Hermit at Subiaco', (13.1, 41.93)), G(529, 547, 'Abbot of Monte Cassino', (13.81, 41.49)))
P('Justinian I', 'Byzantine emperor', (482, 565), 1, 'rule',
  'Reconquered Africa and Italy, rewrote Roman law and built the Hagia Sophia.',
  R(527, 565, 'Emperor of the Romans', *EAST, at='constantinople'))
P('Theodora', 'Byzantine empress', (500, 548), 2, 'rule',
  "Actress turned empress, who stiffened Justinian's nerve during the Nika riots.",
  R(527, 548, 'Empress of the Romans', *EAST, at='constantinople'), wiki='Theodora (wife of Justinian I)')
P('Belisarius', 'Byzantine general', (500, 565), 2, 'war',
  "Justinian's great general: beat Persia at Dara, took back Africa from the Vandals and Italy from the Goths.",
  G(530, 531, 'War with Persia', 'constantinople', (40.94, 37.18)), G(532, 532, 'Nika riots', 'constantinople'),
  G(533, 534, 'Reconquest of Africa', 'constantinople', 'syracuse', (11.0, 35.5), (10.2, 36.7), 'carthage'),
  G(535, 540, 'Reconquest of Italy', 'syracuse', 'naples', 'rome', 'ravenna'),
  G(541, 543, 'Eastern front', (40.94, 37.18), (38.8, 37.15)), G(544, 549, 'Second war in Italy', 'ravenna', 'rome'),
  G(559, 559, 'Saves Constantinople from the Huns', (28.6, 41.05)))
P('Khosrow I', 'Sasanian king of kings', (501, 579), 2, 'rule',
  "Persia's most admired king: reformed taxes, sacked Antioch and welcomed scholars to his court.",
  G(540, 540, 'Sack of Antioch', 'ctesiphon', 'antioch', 'ctesiphon'), R(531, 579, 'King of Kings', *SASAN, at='ctesiphon'))
P('Aryabhata', 'Indian mathematician and astronomer', (476, 550), 2, 'mind',
  'Used zero as a place-holder, calculated pi closely and taught that the Earth spins on its axis.',
  G(499, 550, 'Astronomer at Pataliputra', 'pataliputra'))
P('Gregory the Great', 'Pope', (540, 604), 2, 'faith',
  "Monk turned pope who fed Rome through plague and famine and sent missionaries to the English.",
  G(590, 604, 'Pope', 'rome'), wiki='Pope Gregory I')
P('Khosrow II', 'Sasanian king of kings', (570, 628), 2, 'rule war',
  "Conquered Jerusalem and Egypt from Byzantium, then lost everything to Heraclius and was killed by his son.",
  R(590, 628, 'King of Kings', *SASAN, at='ctesiphon'))
P('Heraclius', 'Byzantine emperor', (575, 641), 2, 'rule war',
  'Saved the empire from Persia with a daring march to Nineveh, then lost Syria and Egypt to the Arabs.',
  G(622, 628, 'War against Persia', ('constantinople', 622), ('trebizond', 623), ((44.5, 40.2, 624)), ((47.3, 36.6, 624.5)), ((45.0, 40.5, 625)),
    ('nineveh', 627.9), ((45.07, 33.88, 628.1)), ((44.5, 40.2, 628.5))),
  G(630, 630, 'Returns the True Cross to Jerusalem', 'constantinople', 'antioch', 'jerusalem'),
  R(610, 641, 'Emperor of the Romans', *EAST, at='constantinople'))

# ---------- Asia ----------
P('Wang Mang', 'Emperor of the Xin dynasty', (-45, 23), 3, 'rule reform',
  "Seized the Han throne, tried sweeping land reforms and was killed when the Red Eyebrows revolt overran China.",
  R(9, 23, 'Emperor of Xin', 'Han', at='changan'))
P('Emperor Guangwu of Han', 'Founder of the Eastern Han', (-5, 57), 3, 'rule',
  'Restored the Han dynasty after Wang Mang and moved the capital to Luoyang.',
  R(25, 57, 'Emperor of Han', 'Han', at='luoyang'))
P('Ban Chao', 'Han general', (32, 102), 2, 'war explore',
  'Spent thirty years in the Tarim Basin bringing the oasis kingdoms under Han rule.',
  G(73, 102, 'Protector of the Western Regions', 'dunhuang', 'khotan', 'kashgar', (82.96, 41.72)))
P('Cai Lun', 'Han court official', (50, 121), 2, 'mind',
  'Credited with inventing paper from bark, rags and fishing nets around AD 105.',
  G(89, 121, 'Invents paper at the court', 'luoyang'))
P('Kanishka', 'Kushan emperor', (100, 150), 2, 'rule faith',
  'Ruled from Central Asia to the Ganges and championed Buddhism along the Silk Road.',
  R(127, 150, 'Kushan emperor', 'Kushan Empire', at='peshawar'))
P('Himiko', 'Queen of Yamatai', (170, 248), 3, 'rule faith',
  'Shaman queen of Japan who sent envoys to China; the first Japanese ruler named in writing.',
  G(189, 248, 'Queen of Yamatai', (135.84, 34.55)))
P('Cao Cao', 'Chancellor of Han, founder of Wei', (155, 220), 2, 'war rule',
  'Reunited northern China in the chaos of the late Han, but was stopped at the Red Cliffs.',
  G(196, 207, 'Unifies the north', (113.82, 34.03), (114.0, 34.75), (114.4, 36.3)),
  G(208, 208, 'Battle of Red Cliffs', (112.2, 30.35), 'red_cliffs'), G(209, 220, 'Ruler of the north', (114.4, 36.3)))
P('Liu Bei', 'Founder of Shu Han', (161, 223), 2, 'war rule',
  'Wandering warlord who allied with Wu at the Red Cliffs and founded the kingdom of Shu.',
  G(208, 220, 'Red Cliffs and the conquest of Shu', 'red_cliffs', 'chengdu'), G(221, 223, 'Emperor of Shu Han', 'chengdu'))
P('Zhuge Liang', 'Chancellor of Shu Han', (181, 234), 2, 'war mind',
  "China's model of the wise strategist: Liu Bei's chancellor, he led five campaigns north against Wei.",
  G(207, 227, 'Chancellor of Shu', 'chengdu'),
  G(228, 234, 'Northern expeditions', 'chengdu', (107.03, 33.07), (105.25, 34.45), (107.03, 33.07), (107.65, 34.3)))
P('Sun Quan', 'Founder of Eastern Wu', (182, 252), 3, 'rule',
  "Held southern China at the Red Cliffs and founded Wu, the third of the Three Kingdoms.",
  G(208, 252, 'Ruler of Wu', 'red_cliffs', 'nanjing'))
P('Emperor Wu of Jin', 'Founder of the Jin dynasty', (236, 290), 3, 'rule',
  'Sima Yan took the throne of Wei, conquered Wu and reunited China in 280.',
  R(266, 290, 'Emperor of Jin', 'Jin', at='luoyang'))
P('Samudragupta', 'Gupta emperor', (318, 375), 3, 'rule war',
  "Conquered much of India and began the Gupta golden age.",
  R(335, 375, 'Gupta emperor', 'Gupta Empire', at='pataliputra'))
P('Chandragupta II', 'Gupta emperor', (355, 415), 2, 'rule',
  "Ruled India's golden age of art, science and Sanskrit poetry.",
  R(375, 415, 'Gupta emperor', 'Gupta Empire', at='ujjain'))
P('Kalidasa', 'Sanskrit poet and playwright', (370, 450), 3, 'art',
  "India's greatest classical poet, author of the play Shakuntala.",
  G(380, 415, 'Poet at the Gupta court', 'ujjain'))
P('Gwanggaeto the Great', 'King of Goguryeo', (374, 413), 3, 'rule war',
  'Made Goguryeo the master of Manchuria and northern Korea.',
  R(391, 413, 'King of Goguryeo', 'Koguryo', at=(126.18, 41.14)))
P('Siyaj Kʼakʼ', 'Teotihuacan warlord', (350, 402), 3, 'war',
  'Arrived at the Maya city of Tikal from Teotihuacan in 378, the same day its king died, and set up a new dynasty.',
  G(378, 378, 'March from Teotihuacan to Tikal', 'teotihuacan', (-92.0, 18.3), 'tikal'), G(379, 402, 'Overlord of the Maya lowlands', 'tikal'))
P('Faxian', 'Chinese Buddhist pilgrim', (337, 422), 3, 'explore faith',
  'Walked from China to India to fetch Buddhist scriptures and sailed home by way of Sri Lanka and Java.',
  G(399, 413, 'Pilgrimage to India', ('changan', 399), ('dunhuang', 400), ('khotan', 401), ('peshawar', 402), ('mathura', 404),
    'kapilavastu', ('pataliputra', 405), ((88.0, 22.0, 409)), ('anuradhapura', 410), ((110.0, -7.0, 412)), ((120.4, 36.1, 412.6)), ('nanjing', 413)))
P('Kumārajīva', 'Buddhist monk and translator', (344, 413), 3, 'faith',
  'Kuchean monk whose Chinese translations of the sutras are still read today.',
  G(401, 413, "Translating sutras at Chang'an", 'changan'))
P('Emperor Xiaowen of Northern Wei', 'Emperor of Northern Wei', (467, 499), 3, 'rule reform',
  'Moved his capital to Luoyang and made his nomad Xianbei court adopt Chinese dress, language and names.',
  R(471, 499, 'Emperor of Northern Wei', 'Toba Wei', at='luoyang'))
P('Emperor Wen of Sui', 'Founder of the Sui dynasty', (541, 604), 2, 'rule',
  'Reunited China in 589 after nearly 300 years of division.',
  R(581, 604, 'Emperor of Sui', 'Sui Empire', at='changan'))
P('Emperor Yang of Sui', 'Emperor of Sui', (569, 618), 3, 'rule',
  "Built the Grand Canal and lost three disastrous wars in Korea that brought down his dynasty.",
  R(604, 618, 'Emperor of Sui', 'Sui Empire', at='luoyang'))
P('Prince Shōtoku', 'Regent of Japan', (574, 622), 2, 'rule faith',
  "Spread Buddhism, wrote Japan's Seventeen-Article Constitution and opened relations with China.",
  R(593, 622, 'Regent of Japan', 'Yamato', at='asuka'))
P('Harsha', 'Emperor of northern India', (590, 647), 2, 'rule',
  'Last great Buddhist emperor of northern India, praised by the pilgrim Xuanzang.',
  R(606, 647, 'Emperor of northern India', 'Kanauj', at=(79.92, 27.06)))
P('Xuanzang', 'Chinese monk and pilgrim', (602, 664), 2, 'explore faith',
  'Walked from China to India and back over sixteen years and brought home hundreds of Buddhist texts.',
  G(629, 645, 'Journey to the West', ('changan', 629), ((102.64, 37.93, 629.5)), ('turfan', 630), ((82.96, 41.72, 630.2)), ((75.0, 42.8, 630.4)),
    ('samarkand', 630.6), ('balkh', 630.8), ('bamiyan', 631), ('peshawar', 631.4), ('srinagar', 631.7), ('mathura', 633.5), ((79.92, 27.06, 634)),
    ('bodh_gaya', 635.3), ('nalanda', 635.6), ('nalanda', 637.5), ((88.0, 23.0, 638.5)), ('kanchipuram', 640), ('nalanda', 642),
    ((79.92, 27.06, 643)), ('taxila', 644), ('kashgar', 644.5), ('khotan', 644.8), ('dunhuang', 645), ('changan', 645.1)),
  G(646, 664, "Translating at Chang'an", 'changan'))
P('Yazdegerd III', 'Last Sasanian king', (624, 651), 3, 'rule',
  "Lost Persia to the Arab armies at Qadisiyya and Nahavand and was murdered in flight at Merv.",
  R(632, 636, 'King of Kings', *SASAN, at='ctesiphon'),
  G(637, 651, 'Flight from the Arabs', 'ctesiphon', (48.37, 34.19), 'isfahan', (55.0, 31.0), 'merv'))
P("Kʼinich Janaab Pakal", 'King of Palenque', (603, 683), 3, 'rule',
  'Ruled the Maya city of Palenque for 68 years; his jade-masked tomb lies in the Temple of the Inscriptions.',
  G(615, 683, 'King of Palenque', 'palenque'))

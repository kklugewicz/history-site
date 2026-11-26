from _lib import P, R, G

EAST = ('Byzantine Empire', 'Eastern Roman Empire')
HRE = ('Holy Roman Empire', 'East Francia')
ENG = ('England', 'English territory', 'Angevin Empire')
FRA = ('Kingdom of France', 'France', 'West Francia')

# ---------- Islam ----------
P('Muhammad', 'Prophet of Islam', (570, 632), 1, 'faith rule',
  'Received the revelations of the Quran in Mecca, founded the first Muslim community at Medina and united Arabia.',
  G(570, 609, 'Youth in Mecca', 'mecca'), G(610, 621, 'Prophet in Mecca', 'mecca'),
  G(622, 622, 'The Hijra to Medina', 'mecca', 'medina'), G(623, 629, 'Leader of Medina', 'medina'),
  G(624, 624, 'Battle of Badr', 'medina', 'badr', 'medina'), G(630, 630, 'Return to Mecca', 'medina', 'mecca', 'taif', 'medina'),
  G(631, 632, 'Ruler of Arabia', 'medina'))
P('Abu Bakr', 'First caliph', (573, 634), 2, 'rule faith',
  "Muhammad's father-in-law and successor, who held Arabia together and launched the conquests of Iraq and Syria.",
  R(632, 634, 'First caliph', 'Hejaz', at='medina'))
P('Khalid ibn al-Walid', 'Arab general', (585, 642), 2, 'war',
  "'The Sword of God': never lost a battle; conquered Iraq and beat the Byzantines at the Yarmouk.",
  G(633, 633, 'Conquest of Iraq', 'medina', (44.36, 31.93)), G(634, 636, 'Conquest of Syria', (44.36, 31.93), (38.3, 34.0), 'damascus', (35.95, 32.8)))
P('Umar', 'Second caliph', (584, 644), 2, 'rule faith',
  'Under him the Arabs took Syria, Egypt, Iraq and Persia; he entered Jerusalem in 637.',
  G(637, 637, 'Visit to Jerusalem', 'medina', 'jerusalem', 'medina'), R(634, 644, 'Second caliph', 'Hejaz', at='medina'))
P('Uthman', 'Third caliph', (576, 656), 3, 'rule faith',
  'Had the Quran written down in one standard text; his murder began the first Muslim civil war.',
  R(644, 656, 'Third caliph', 'Hejaz', at='medina'))
P('Ali', 'Fourth caliph, first Shia imam', (600, 661), 1, 'faith rule',
  "Muhammad's cousin and son-in-law; Shia Muslims hold he was the rightful successor. Murdered at Kufa.",
  G(656, 661, 'Caliph at Kufa', 'kufa'))
P('Muawiya I', 'Founder of the Umayyad Caliphate', (602, 680), 2, 'rule',
  "Governor of Syria who won the civil war against Ali and made the caliphate a dynasty ruled from Damascus.",
  R(661, 680, 'Umayyad caliph', 'Umayyad Caliphate', at='damascus'))
P('Husayn ibn Ali', 'Grandson of Muhammad, third Shia imam', (626, 680), 2, 'faith',
  "Killed with his family at Karbala by an Umayyad army, a martyrdom Shia Muslims mourn every year at Ashura.",
  G(680, 680, 'Journey to Karbala', 'medina', 'mecca', 'karbala'))
P('Abd al-Malik', 'Umayyad caliph', (646, 705), 3, 'rule',
  'Built the Dome of the Rock and made Arabic the language of government.',
  R(685, 705, 'Umayyad caliph', 'Umayyad Caliphate', at='damascus'), wiki='Abd al-Malik ibn Marwan')
P('Tariq ibn Ziyad', 'Berber commander', (670, 720), 2, 'war',
  'Crossed to Spain in 711, giving Gibraltar its name, and destroyed the Visigothic kingdom.',
  G(711, 712, 'Conquest of Spain', 'tangier', 'gibraltar', (-5.85, 36.6), 'cordoba', 'toledo'))
P('Musa ibn Nusayr', 'Umayyad governor of Africa', (640, 716), 3, 'war',
  "Completed the conquest of North Africa and followed Tariq into Spain.",
  G(698, 711, 'Governor of Ifriqiya', 'kairouan'), G(712, 714, 'Conquest of Spain', 'gibraltar', 'seville', 'toledo', 'zaragoza'))
P('Abd al-Rahman I', 'Founder of the Emirate of Córdoba', (731, 788), 2, 'rule',
  'Last survivor of the massacred Umayyad family, he fled to Spain and founded a rival Muslim state there.',
  G(750, 755, 'Flight from the Abbasids', 'damascus', (31.2, 30.0), 'kairouan', (-2.0, 35.0)),
  R(756, 788, 'Emir of Córdoba', 'Emirate of Córdoba', at='cordoba'))
P('Al-Mansur', 'Abbasid caliph', (714, 775), 3, 'rule',
  'Founded Baghdad in 762, the round city that became the largest in the world.',
  R(754, 775, 'Abbasid caliph', 'Abbasid Caliphate', at='baghdad'))
P('Harun al-Rashid', 'Abbasid caliph', (763, 809), 2, 'rule',
  "Ruled Baghdad at the height of its glory, the caliph of the Thousand and One Nights.",
  R(786, 809, 'Abbasid caliph', 'Abbasid Caliphate', at='baghdad'))
P("Al-Ma'mun", 'Abbasid caliph', (786, 833), 3, 'rule mind',
  'Patron of the House of Wisdom, where Greek science was translated into Arabic.',
  R(813, 833, 'Abbasid caliph', 'Abbasid Caliphate', at='baghdad'))
P('Al-Khwarizmi', 'Persian mathematician', (780, 850), 2, 'mind',
  "His books gave us algebra, and his name gave us the word 'algorithm'.",
  G(813, 850, 'Scholar at the House of Wisdom', 'baghdad'), wiki='Muhammad ibn Musa al-Khwarizmi')
P('Abd al-Rahman III', 'Caliph of Córdoba', (891, 961), 2, 'rule',
  "Declared himself caliph in 929; under him Córdoba was the richest city in Europe.",
  R(912, 961, 'Emir, then caliph of Córdoba', 'Emirate of Córdoba', 'Caliphate of Córdoba', at='cordoba'))
P('Ferdowsi', 'Persian poet', (940, 1020), 3, 'art',
  "Spent thirty years writing the Shahnameh, Iran's national epic.",
  G(977, 1010, 'Writes the Shahnameh', (59.47, 36.43)))
P('Mahmud of Ghazni', 'Sultan of Ghazni', (971, 1030), 2, 'rule war',
  'Raided India seventeen times and looted the temple of Somnath to build a glittering court at Ghazni.',
  G(1025, 1026, 'Raid on Somnath', 'ghazni', 'lahore', (70.4, 20.89), 'ghazni'),
  R(998, 1030, 'Sultan of Ghazni', 'Ghaznavid Emirate', at='ghazni'))
P('Al-Biruni', 'Persian scholar', (973, 1050), 3, 'mind',
  "Measured the Earth's radius and wrote the first great study of India and its religions.",
  G(1017, 1048, 'Scholar at the court of Ghazni', 'ghazni', 'lahore'))
P('Avicenna', 'Persian physician and philosopher', (980, 1037), 2, 'mind',
  "His Canon of Medicine was the standard medical textbook in Europe and the Islamic world for 600 years.",
  G(980, 999, 'Youth in Bukhara', 'bukhara'), G(1000, 1022, 'Wandering physician', 'urgench', 'rayy', 'ecbatana'),
  G(1023, 1037, 'Physician at Isfahan', 'isfahan'))
P('Alp Arslan', 'Seljuk sultan', (1029, 1072), 2, 'rule war',
  'Destroyed the Byzantine army at Manzikert in 1071, opening Anatolia to the Turks.',
  G(1071, 1071, 'Battle of Manzikert', 'rayy', 'tabriz', 'manzikert'),
  R(1063, 1072, 'Seljuk sultan', 'Seljuk Empire', at='rayy'))
P('Nizam al-Mulk', 'Seljuk vizier', (1018, 1092), 3, 'rule mind',
  'Ran the Seljuk empire for thirty years and founded the Nizamiyya colleges; murdered by the Assassins.',
  G(1064, 1092, 'Vizier of the Seljuks', 'isfahan'))
P('Omar Khayyam', 'Persian poet and astronomer', (1048, 1131), 3, 'mind art',
  'Reformed the calendar, solved cubic equations and wrote the quatrains of the Rubaiyat.',
  G(1074, 1092, 'Astronomer at Isfahan', 'isfahan'), G(1093, 1131, 'Nishapur', 'nishapur'))
P('Hasan-i Sabbah', 'Founder of the Nizari Ismaili state', (1050, 1124), 3, 'faith war',
  'Took the castle of Alamut and led the sect the crusaders called the Assassins.',
  G(1090, 1124, 'Master of Alamut', 'alamut'))
P('Al-Ghazali', 'Islamic theologian', (1058, 1111), 3, 'faith mind',
  'Left his chair at Baghdad to live as a wandering Sufi, and reconciled mysticism with Islamic law.',
  G(1091, 1095, 'Professor at Baghdad', 'baghdad'), G(1096, 1105, 'Wandering Sufi', 'damascus', 'jerusalem', 'mecca'),
  G(1106, 1111, 'Return to Khorasan', 'nishapur'))
P('Yusuf ibn Tashfin', 'Almoravid emir', (1009, 1106), 3, 'rule war',
  'Founded Marrakesh and crossed into Spain to beat Castile at Sagrajas.',
  G(1086, 1086, 'Battle of Sagrajas', 'marrakesh', 'gibraltar', (-6.9, 38.9)),
  R(1061, 1106, 'Almoravid emir', 'Almoravid dynasty', at='marrakesh'))
P('Averroes', 'Andalusian philosopher', (1126, 1198), 3, 'mind',
  "Wrote the commentaries on Aristotle that revived Greek philosophy in Christian Europe.",
  G(1169, 1194, 'Judge and philosopher', 'seville', 'cordoba'), G(1195, 1198, 'Exile in Marrakesh', 'marrakesh'))
P('Maimonides', 'Jewish philosopher and physician', (1138, 1204), 2, 'faith mind',
  'Fled Córdoba, became physician to Saladin\'s court in Cairo and wrote the great codes of Jewish law and thought.',
  G(1148, 1165, 'Flight from Córdoba', 'cordoba', 'fez'), G(1166, 1204, 'Physician in Cairo', 'cairo'))
P('Saladin', 'Sultan of Egypt and Syria', (1137, 1193), 1, 'war rule',
  'United Egypt and Syria, destroyed the crusader army at Hattin and retook Jerusalem in 1187.',
  G(1169, 1173, 'Vizier of Egypt', 'cairo'), G(1174, 1186, 'Sultan of Egypt and Syria', 'cairo', 'damascus'),
  G(1187, 1187, 'Hattin and Jerusalem', 'damascus', 'hattin', 'acre', 'jerusalem'),
  G(1188, 1192, 'War with the Third Crusade', 'acre', (34.82, 32.2), 'jerusalem'), G(1193, 1193, 'Last days in Damascus', 'damascus'))
P('Rumi', 'Persian poet and Sufi mystic', (1207, 1273), 2, 'art faith',
  "His Masnavi is the most loved poem in Persian; his followers became the whirling dervishes.",
  G(1215, 1228, 'Flight from the Mongols', 'balkh', 'nishapur', 'baghdad', 'mecca', 'damascus', (33.23, 37.18), 'konya'),
  G(1229, 1273, 'Poet of Konya', 'konya'))
P('Baybars', 'Mamluk sultan', (1223, 1277), 2, 'war rule',
  'Beat the Mongols at Ain Jalut and spent his reign tearing down the crusader states.',
  G(1260, 1260, 'Battle of Ain Jalut', 'cairo', 'gaza', 'ain_jalut'),
  R(1260, 1277, 'Mamluk sultan', 'Mamluke Sultanate', at='cairo'))

# ---------- Byzantium and the Slavs ----------
P('Leo III the Isaurian', 'Byzantine emperor', (685, 741), 3, 'rule',
  'Beat the great Arab siege of Constantinople and began the ban on holy images.',
  R(717, 741, 'Emperor of the Romans', *EAST, at='constantinople'))
P('Irene of Athens', 'Byzantine empress', (752, 803), 3, 'rule',
  "Blinded her own son to rule alone, the first woman to reign over the empire in her own name.",
  R(797, 802, 'Empress of the Romans', *EAST, at='constantinople'))
P('Cyril and Methodius', 'Missionaries to the Slavs', (815, 885), 3, 'faith',
  'Byzantine brothers who created the first Slavic alphabet to bring the Bible to the Slavs.',
  G(863, 885, 'Mission to the Slavs', 'constantinople', (17.4, 49.1), 'rome', (17.4, 49.1)), wiki='Saints Cyril and Methodius')
P('Rurik', 'Founder of the Rurik dynasty', (830, 879), 3, 'rule',
  'Varangian chief who, by the chronicle, was invited to rule Novgorod in 862; his line ruled Russia until 1598.',
  G(862, 879, 'Prince of Novgorod', 'novgorod'))
P('Vladimir the Great', 'Grand Prince of Kiev', (958, 1015), 2, 'rule faith',
  "Had himself and his people baptised in 988, making Rus' an Orthodox Christian land.",
  G(988, 988, 'Baptism at Chersonesus', 'kiev', (33.49, 44.61), 'kiev'),
  R(980, 1015, "Grand Prince of Kiev", 'Kyivan Rus', at='kiev'))
P('Basil II', 'Byzantine emperor', (958, 1025), 2, 'rule war',
  "'The Bulgar-Slayer': destroyed the Bulgarian empire and left Byzantium at its medieval height.",
  G(1014, 1014, 'Battle of Kleidion', 'constantinople', 'thessalonica', (23.0, 41.4)),
  R(976, 1025, 'Emperor of the Romans', *EAST, at='constantinople'))
P('Yaroslav the Wise', 'Grand Prince of Kiev', (978, 1054), 3, 'rule',
  "Gave Rus' its first written law and married his daughters to the kings of France, Hungary and Norway.",
  R(1019, 1054, 'Grand Prince of Kiev', 'Kyivan Rus', at='kiev'))
P('Michael I Cerularius', 'Patriarch of Constantinople', (1000, 1059), 3, 'faith',
  'His clash with the pope\'s envoys in 1054 split the Catholic and Orthodox churches.',
  G(1043, 1059, 'Patriarch of Constantinople', 'constantinople'))
P('Alexios I Komnenos', 'Byzantine emperor', (1057, 1118), 3, 'rule',
  'Asked the West for help against the Turks, and got the First Crusade.',
  R(1081, 1118, 'Emperor of the Romans', *EAST, at='constantinople'))
P('Anna Komnene', 'Byzantine princess and historian', (1083, 1153), 3, 'mind',
  "Wrote the Alexiad, her father's history and the first by a woman historian in Europe.",
  G(1118, 1153, 'Writes the Alexiad', 'constantinople'))

# ---------- Western Europe ----------
P('Charles Martel', 'Frankish ruler', (688, 741), 2, 'war rule',
  'Stopped the Arab advance into France at Tours in 732 and founded the Carolingian line.',
  G(732, 732, 'Battle of Tours', 'paris', 'tours', (0.43, 46.75)), R(718, 741, 'Mayor of the palace', 'Frankish Kingdom', at='paris'))
P('Pepin the Short', 'King of the Franks', (714, 768), 3, 'rule',
  'Became king with the pope\'s blessing and gave the pope lands that became the Papal States.',
  R(751, 768, 'King of the Franks', 'Frankish Kingdom', at='paris'))
P('Charlemagne', 'King of the Franks and emperor', (747, 814), 1, 'rule war',
  'Conquered most of western Europe, revived learning and was crowned emperor in Rome on Christmas Day 800.',
  G(773, 774, 'Conquest of the Lombards', 'aachen', 'geneva', 'pavia'),
  G(778, 778, 'Spanish expedition', 'toulouse', 'zaragoza', (-1.33, 43.01)),
  G(800, 800, 'Crowned emperor in Rome', 'aachen', 'rome'),
  R(768, 814, 'King of the Franks, emperor', 'Frankish Kingdom', 'Carolingian Empire', at='aachen'))
P('Pope Leo III', 'Pope', (750, 816), 3, 'faith',
  'Crowned Charlemagne emperor in 800, founding the Western empire anew.',
  R(795, 816, 'Pope', 'Papal States', at='rome'))
P('Alcuin', 'English scholar', (735, 804), 3, 'mind',
  "Ran Charlemagne's palace school and the revival of learning in the Frankish kingdom.",
  G(782, 795, 'Scholar at Aachen', 'aachen'), G(796, 804, 'Abbot of Tours', 'tours'))
P('Alfred the Great', 'King of Wessex', (849, 899), 2, 'rule war',
  'Held off the Vikings from a marsh at Athelney, beat them at Edington and laid the foundations of England.',
  G(878, 878, 'Athelney and Edington', 'winchester', (-2.93, 51.06), (-2.1, 51.27)),
  R(871, 899, 'King of Wessex', 'Wessex', at='winchester'))
P('Rollo', 'First ruler of Normandy', (846, 930), 3, 'war rule',
  "Viking leader granted Normandy by the French king in 911; William the Conqueror's ancestor.",
  G(911, 930, 'Count of Rouen', 'rouen'))
P('Otto I', 'Holy Roman Emperor', (912, 973), 2, 'rule war',
  'Smashed the Magyars at Lechfeld and was crowned emperor in Rome in 962, founding the Holy Roman Empire.',
  G(955, 955, 'Battle of Lechfeld', (11.63, 52.13), (10.9, 48.3)), G(962, 962, 'Crowned emperor in Rome', 'pavia', 'rome'),
  R(936, 973, 'King of Germany', *HRE, at=(11.63, 52.13)), wiki='Otto the Great')
P('Erik the Red', 'Norse explorer', (950, 1003), 3, 'explore',
  'Outlawed from Iceland, he explored Greenland and led the first Norse settlers there.',
  G(982, 985, 'Explores Greenland', 'reykjavik', (-40.0, 64.5), 'brattahlid'), G(986, 1003, 'Settler of Greenland', 'brattahlid'))
P('Leif Erikson', 'Norse explorer', (970, 1020), 2, 'explore',
  'Reached North America around 1000, five centuries before Columbus, and named it Vinland.',
  G(1000, 1001, 'Voyage to Vinland', 'brattahlid', (-66.0, 66.0), (-60.0, 54.0), 'lanse_aux_meadows', 'brattahlid'))
P('Stephen I of Hungary', 'First king of Hungary', (975, 1038), 3, 'rule faith',
  'Crowned in 1000 with a crown from the pope, he made the Magyars a Christian kingdom.',
  R(1000, 1038, 'King of Hungary', 'Hungary', at='esztergom'))
P('Bolesław I the Brave', 'First king of Poland', (967, 1025), 3, 'rule',
  'Built Poland into a power and was crowned its first king in 1025.',
  R(992, 1025, 'Duke, then king of Poland', 'Poland', at='gniezno'))
P('Cnut the Great', 'King of England, Denmark and Norway', (995, 1035), 2, 'rule',
  'Danish king who conquered England and ruled a North Sea empire.',
  R(1016, 1035, 'King of England, Denmark and Norway', 'England', 'Denmark-Norway', 'Denmark', at='winchester'))
P('Harald Hardrada', 'King of Norway', (1015, 1066), 2, 'war rule',
  "Fought for Byzantium in the Varangian Guard, ruled Norway, and died invading England at Stamford Bridge.",
  G(1031, 1042, 'Varangian Guard', 'kiev', 'constantinople', 'syracuse', 'constantinople', 'kiev'),
  R(1046, 1065, 'King of Norway', 'Norway', 'Denmark-Norway', at='trondheim'),
  G(1066, 1066, 'Invasion of England', 'bergen', (-1.2, 60.2), (-0.91, 53.99)))
P('Harold Godwinson', 'Last Anglo-Saxon king of England', (1022, 1066), 3, 'rule war',
  'Beat Harald Hardrada at Stamford Bridge, then marched south and died at Hastings.',
  G(1066, 1066, 'Stamford Bridge and Hastings', 'london', (-0.91, 53.99), 'london', 'hastings'))
P('William the Conqueror', 'King of England', (1028, 1087), 1, 'war rule',
  'Duke of Normandy who won England at Hastings in 1066 and ordered the Domesday Book.',
  G(1035, 1065, 'Duke of Normandy', 'rouen'),
  G(1066, 1066, 'Conquest of England', (-0.1, 49.29), (1.9, 50.1), (0.33, 50.82), 'hastings', 'london'),
  R(1067, 1087, 'King of England', *ENG, at='london'))
P('El Cid', 'Castilian knight', (1043, 1099), 2, 'war',
  'Fought for Christian and Muslim lords alike and took Valencia for himself; hero of Spain\'s epic poem.',
  G(1081, 1093, 'Exile and campaigns', 'burgos', 'zaragoza'), G(1094, 1099, 'Lord of Valencia', 'valencia'))
P('Pope Gregory VII', 'Pope', (1015, 1085), 2, 'faith',
  'Fought the emperor over who appoints bishops and made Henry IV kneel in the snow at Canossa.',
  G(1077, 1077, 'Canossa', 'rome', 'canossa'), R(1073, 1083, 'Pope', 'Papal States', at='rome'),
  G(1084, 1085, 'Driven out of Rome, died at Salerno', ('rome', 1084.4), ((14.76, 40.68, 1084.6))))
P('Henry IV, Holy Roman Emperor', 'Holy Roman Emperor', (1050, 1106), 3, 'rule',
  "Excommunicated by Gregory VII, he crossed the Alps in winter to beg forgiveness at Canossa.",
  G(1077, 1077, 'The walk to Canossa', 'speyer', 'canossa'), R(1056, 1105, 'King of Germany, emperor', *HRE, at='speyer'))
P('Pope Urban II', 'Pope', (1035, 1099), 2, 'faith',
  'Called the First Crusade at Clermont in 1095.',
  G(1095, 1096, 'Preaching the crusade', (9.69, 45.05), 'clermont', 'tours', 'rome'), R(1088, 1099, 'Pope', 'Papal States', at='rome'))
P('Godfrey of Bouillon', 'Leader of the First Crusade', (1060, 1100), 2, 'war faith',
  'Led the crusaders who took Jerusalem in 1099 and became its first Latin ruler.',
  G(1096, 1099, 'First Crusade', ((5.07, 49.79, 1096.6)), ((16.37, 48.21, 1096.8)), ('belgrade', 1096.9), ('constantinople', 1097),
    ('nicaea', 1097.4), ((30.52, 39.79, 1097.5)), ('antioch', 1097.8), ('antioch', 1099), ('jerusalem', 1099.5)),
  G(1099, 1100, 'Ruler of Jerusalem', 'jerusalem'))
P('Hildegard of Bingen', 'Abbess, mystic and composer', (1098, 1179), 3, 'faith art',
  'Wrote visions, medicine and music and corresponded with popes and emperors.',
  G(1136, 1179, 'Abbess on the Rhine', (7.9, 49.97)))
P('Bernard of Clairvaux', 'Cistercian abbot', (1090, 1153), 3, 'faith',
  'The most powerful churchman of his age, who preached the Second Crusade.',
  G(1146, 1147, 'Preaching the Second Crusade', (3.75, 47.47), 'speyer'), G(1115, 1153, 'Abbot of Clairvaux', 'clairvaux'))
P('Afonso I of Portugal', 'First king of Portugal', (1109, 1185), 3, 'rule war',
  'Won independence from León and took Lisbon from the Moors in 1147.',
  G(1147, 1147, 'Conquest of Lisbon', 'coimbra', 'lisbon'), R(1139, 1185, 'King of Portugal', 'Portugal', at='coimbra'))
P('Eleanor of Aquitaine', 'Queen of France, then of England', (1122, 1204), 2, 'rule',
  'Queen of France and then England, mother of Richard the Lionheart and King John, and the richest heiress in Europe.',
  G(1137, 1146, 'Queen of France', 'paris'), G(1147, 1149, 'Second Crusade', 'paris', 'constantinople', 'antioch', 'paris'),
  G(1150, 1152, 'Queen of France', 'paris'), G(1154, 1189, 'Queen of England', 'london', 'poitiers'), G(1190, 1204, 'Fontevraud', (0.05, 47.18)))
P('Frederick Barbarossa', 'Holy Roman Emperor', (1122, 1190), 2, 'rule war',
  'Fought the Italian cities for decades and drowned in a river in Anatolia on the Third Crusade.',
  G(1176, 1176, 'Battle of Legnano', 'pavia', (8.92, 45.6)),
  G(1189, 1190, 'Third Crusade', 'regensburg', 'vienna', 'belgrade', 'adrianople', 'konya', (33.95, 36.38)),
  R(1155, 1190, 'Holy Roman Emperor', *HRE, at='aachen'), wiki='Frederick Barbarossa')
P('Henry II of England', 'King of England', (1133, 1189), 2, 'rule',
  'Ruled an empire from Scotland to the Pyrenees, built English common law, and quarrelled fatally with Becket.',
  R(1154, 1189, 'King of England', *ENG, at='london'))
P('Thomas Becket', 'Archbishop of Canterbury', (1120, 1170), 3, 'faith',
  "Murdered in his cathedral by Henry II's knights in 1170; his shrine became England's great pilgrimage.",
  G(1162, 1170, 'Archbishop of Canterbury', 'canterbury'))
P('Philip II of France', 'King of France', (1165, 1223), 2, 'rule war',
  "Won Normandy from King John, beat his allies at Bouvines and made France the strongest kingdom in Europe.",
  G(1190, 1191, 'Third Crusade', 'marseille', 'acre', 'paris'), G(1214, 1214, 'Battle of Bouvines', 'paris', (3.18, 50.58)),
  R(1180, 1223, 'King of France', *FRA, at='paris'))
P('Richard I of England', 'King of England', (1157, 1199), 2, 'war rule',
  "'The Lionheart': led the Third Crusade, beat Saladin at Arsuf but never took Jerusalem.",
  G(1190, 1192, 'Third Crusade', (3.75, 47.47), 'marseille', (15.55, 38.19), (33.04, 34.68), ('acre', 1191.5), (34.82, 32.2), (34.75, 32.05)),
  G(1193, 1194, 'Captive in Germany', (15.52, 48.4), (7.97, 49.2)),
  G(1194, 1199, 'Wars in France', (1.4, 49.24), (1.0, 45.75)),
  R(1189, 1199, 'King of England', *ENG, at='london'))
P('King John', 'King of England', (1166, 1216), 2, 'rule',
  'Lost Normandy and was forced by his barons to seal Magna Carta in 1215.',
  G(1215, 1215, 'Magna Carta at Runnymede', 'london', (-0.56, 51.44)), R(1199, 1216, 'King of England', *ENG, at='london'),
  wiki='John, King of England')
P('Pope Innocent III', 'Pope', (1161, 1216), 2, 'faith',
  'The most powerful medieval pope: launched the Fourth Crusade and the crusade against the Cathars.',
  R(1198, 1216, 'Pope', 'Papal States', at='rome'))
P('Simon de Montfort, 5th Earl of Leicester', 'Leader of the Albigensian Crusade', (1175, 1218), 3, 'war faith',
  'Led the crusade against the Cathars of southern France and was killed besieging Toulouse.',
  G(1209, 1218, 'Albigensian Crusade', (3.22, 43.34), (2.35, 43.21), (1.55, 43.4), 'toulouse'), wiki='Simon de Montfort, 5th Earl of Leicester')
P('Francis of Assisi', 'Founder of the Franciscans', (1181, 1226), 2, 'faith',
  'Gave up his wealth to live in poverty and preach; he even crossed the lines to preach to the sultan of Egypt.',
  G(1219, 1220, 'Mission to the sultan', 'assisi', 'acre', (31.8, 31.4), 'acre', 'assisi'), G(1208, 1226, 'Founds the Franciscans', 'assisi'))
P('Saint Dominic', 'Founder of the Dominicans', (1170, 1221), 3, 'faith',
  'Founded the order of preaching friars to win back the Cathars.',
  G(1206, 1221, 'Preaching in Languedoc and Italy', 'toulouse', 'rome', 'bologna'))
P('Alfonso VIII of Castile', 'King of Castile', (1155, 1214), 3, 'rule war',
  'Led the Christian kings to victory over the Almohads at Las Navas de Tolosa in 1212.',
  G(1212, 1212, 'Las Navas de Tolosa', 'toledo', (-3.58, 38.28)), R(1158, 1214, 'King of Castile', 'Castile', at='toledo'))
P('Frederick II, Holy Roman Emperor', 'Holy Roman Emperor and king of Sicily', (1194, 1250), 2, 'rule mind',
  "'The wonder of the world': spoke six languages, won back Jerusalem by treaty and was excommunicated four times.",
  G(1228, 1229, 'Sixth Crusade', (17.94, 40.64), 'acre', 'jerusalem', 'acre', (17.94, 40.64)),
  R(1220, 1250, 'Emperor and king of Sicily', 'Holy Roman Empire', 'Sicily', at='palermo'))
P('Louis IX of France', 'King of France', (1214, 1270), 2, 'rule faith',
  'Saint Louis: led two crusades, was captured in Egypt and died of disease before Tunis.',
  G(1248, 1254, 'Seventh Crusade', (4.19, 43.57), (33.04, 34.68), (31.8, 31.4), (31.38, 31.04), ('acre', 1250.6), ('acre', 1254)),
  G(1270, 1270, 'Eighth Crusade', (4.19, 43.57), 'tunis'), R(1226, 1270, 'King of France', *FRA, at='paris'))
P('Thomas Aquinas', 'Theologian and philosopher', (1225, 1274), 2, 'faith mind',
  'Joined Aristotle\'s philosophy to Christian faith in the Summa Theologica.',
  G(1245, 1259, 'Paris and Cologne', 'cologne', 'paris'), G(1260, 1271, 'Teaching in Italy and Paris', 'naples', 'rome', 'paris'),
  G(1272, 1274, 'Naples', 'naples'))
P('Simon de Montfort, 6th Earl of Leicester', 'Leader of the barons against Henry III', (1208, 1265), 3, 'reform war',
  "Defeated the king and called the first English parliament with elected townsmen in 1265.",
  G(1264, 1265, 'Lewes and the first parliament', 'london', (0.0, 50.87), 'london', (-1.94, 52.09)))
P('Edward I of England', 'King of England', (1239, 1307), 2, 'rule war',
  'Conquered Wales, hammered the Scots and shaped Parliament.',
  G(1296, 1298, 'War in Scotland', 'york', (-2.0, 55.77), 'stirling', (-3.78, 55.99)),
  R(1272, 1307, 'King of England', *ENG, at='london'))
P('William Wallace', 'Scottish patriot', (1270, 1305), 2, 'war',
  'Beat the English at Stirling Bridge in 1297; captured and executed in London in 1305.',
  G(1297, 1298, 'Stirling Bridge and Falkirk', 'stirling', (-3.78, 55.99)), G(1305, 1305, 'Execution in London', 'london'))
P('Robert the Bruce', 'King of Scots', (1274, 1329), 2, 'rule war',
  'Won Scottish independence from England at Bannockburn in 1314.',
  G(1314, 1314, 'Battle of Bannockburn', 'stirling', (-3.92, 56.09)), R(1306, 1329, 'King of Scots', 'Scotland', at='stirling'))
P('Marco Polo', 'Venetian merchant and traveller', (1254, 1324), 1, 'explore',
  'Spent 24 years in Asia, 17 of them serving Kublai Khan, and told Europe about China.',
  G(1271, 1275, 'Journey to China', ('venice', 1271), ('acre', 1271.5), (35.79, 36.77), ('tabriz', 1272), ('hormuz', 1272.5), 'herat', ('balkh', 1273),
    (73.0, 37.3), ('kashgar', 1274), 'khotan', ('dunhuang', 1274.7), ('shangdu', 1275.4)),
  G(1276, 1291, 'In the service of Kublai Khan', 'dadu', 'hangzhou', 'dadu', 'chengdu', 'dali', 'dadu'),
  G(1292, 1295, 'Voyage home', ('quanzhou', 1292), (109.2, 13.0), ((95.3, 5.5, 1292.6)), ((79.86, 6.93, 1293.2)), ('hormuz', 1293.5), ('tabriz', 1293.8),
    ('trebizond', 1294.8), 'constantinople', ('venice', 1295.5)),
  G(1296, 1299, 'Prisoner in Genoa, dictates his Travels', 'genoa'), G(1300, 1324, 'Merchant in Venice', 'venice'))
P('Dante Alighieri', 'Italian poet', (1265, 1321), 2, 'art',
  'Wrote the Divine Comedy in exile from Florence, founding the Italian literary language.',
  G(1265, 1301, 'Florence', 'florence'), G(1302, 1321, 'Exile, writes the Divine Comedy', 'verona', 'ravenna'))

# ---------- Mongols and Central Asia ----------
P('Genghis Khan', 'Founder of the Mongol Empire', (1162, 1227), 1, 'war rule',
  'United the Mongol tribes and conquered from China to the Caspian, founding the largest land empire in history.',
  G(1162, 1205, 'Rise on the steppe', 'onon', (106.9, 47.92), 'onon'),
  G(1211, 1215, 'Invasion of the Jin', ('onon', 1211), ((111.0, 43.5, 1211.5)), ('datong', 1212), ('beijing', 1213.5), ('beijing', 1215)),
  G(1219, 1223, 'Conquest of Khwarazm', ((87.0, 48.0, 1219)), ('otrar', 1219.8), ('bukhara', 1220.2), ('samarkand', 1220.4), ((69.4, 36.7, 1221)),
    ('balkh', 1221.3), ((70.8, 32.0, 1221.8)), ('samarkand', 1222.5), ((75.0, 43.0, 1223.5))),
  G(1226, 1227, 'Campaign against Xixia', 'karakorum', (106.23, 38.49), (106.2, 35.7)),
  R(1206, 1227, 'Great Khan of the Mongols', 'Mongol Empire', at='karakorum'))
P('Subutai', 'Mongol general', (1175, 1248), 2, 'war',
  "Genghis's greatest general: led the raid round the Caspian and the invasion of Russia, Poland and Hungary.",
  G(1220, 1223, 'Great raid round the Caspian', 'rayy', 'tabriz', 'tbilisi', (48.29, 42.06), (37.5, 47.6), (49.1, 55.0), (65.0, 48.0)),
  G(1236, 1242, 'Invasion of Europe', ((49.1, 55.0, 1236)), ('vladimir', 1238), ('kiev', 1240.9), ((20.94, 47.97, 1241.3)), ((19.04, 47.5, 1241.5)), ((47.0, 47.0, 1242.6))))
P('Ögedei Khan', 'Great Khan of the Mongols', (1186, 1241), 2, 'rule',
  "Genghis's son: finished off the Jin, built Karakorum and sent the armies into Europe.",
  R(1229, 1241, 'Great Khan', 'Mongol Empire', at='karakorum'))
P('Batu Khan', 'Founder of the Golden Horde', (1205, 1255), 2, 'war rule',
  "Led the Mongol conquest of Rus' and the invasion of Hungary and founded the Golden Horde.",
  G(1236, 1242, "Conquest of Rus' and invasion of Hungary", 'kazan', 'vladimir', 'kiev', (20.94, 47.97), 'esztergom', 'sarai'),
  R(1243, 1255, 'Khan of the Golden Horde', 'Khanate of the Golden Horde', at='sarai'))
P('Möngke Khan', 'Great Khan of the Mongols', (1209, 1259), 3, 'rule',
  'Sent Hulagu west and Kublai south, and died besieging a Song fortress.',
  R(1251, 1259, 'Great Khan', 'Mongol Empire', at='karakorum'))
P('Hulagu Khan', 'Founder of the Ilkhanate', (1217, 1265), 2, 'war rule',
  'Destroyed the Assassins and sacked Baghdad in 1258, ending the Abbasid caliphate.',
  G(1256, 1258, 'Alamut and Baghdad', 'samarkand', 'alamut', 'baghdad'), G(1259, 1260, 'Invasion of Syria', 'tabriz', 'aleppo', 'damascus', 'tabriz'),
  R(1261, 1265, 'Ilkhan of Persia', 'Ilkhanate', 'Mongol Empire', at=(46.24, 37.39)))
P('Kublai Khan', 'Great Khan and emperor of China', (1215, 1294), 1, 'rule',
  'Conquered Song China, founded the Yuan dynasty and built his capital at Beijing.',
  R(1260, 1294, 'Great Khan, emperor of Yuan China', 'Great Khanate', 'Mongol Empire', at='dadu'))

# ---------- China, Japan, Korea ----------
P('Emperor Taizong of Tang', 'Emperor of Tang China', (598, 649), 2, 'rule',
  "Built the Tang into Asia's superpower and is remembered as one of China's wisest emperors.",
  R(626, 649, 'Emperor of Tang', 'Tang Empire', at='changan'))
P('Kim Yu-sin', 'Silla general', (595, 673), 3, 'war',
  "Led Silla's armies in the wars that united the Korean peninsula.",
  G(660, 673, 'Unifies Korea for Silla', 'gyeongju', (126.9, 36.3), 'pyongyang', 'gyeongju'))
P('Wu Zetian', 'Empress of China', (624, 705), 2, 'rule',
  "The only woman to rule China as emperor in her own name.",
  R(690, 705, 'Emperor of Zhou', 'Tang Empire', at='luoyang'))
P('Emperor Xuanzong of Tang', 'Emperor of Tang China', (685, 762), 3, 'rule',
  'Ruled the high Tang golden age until the An Lushan rebellion drove him from his capital.',
  R(712, 756, 'Emperor of Tang', 'Tang Empire', at='changan'))
P('Li Bai', 'Chinese poet', (701, 762), 3, 'art',
  "China's most loved poet of wine, moonlight and wandering.",
  G(742, 744, 'Poet at the Tang court', 'changan'), G(745, 762, 'Wanderings', 'luoyang', 'nanjing', (118.5, 31.55)))
P('Du Fu', 'Chinese poet', (712, 770), 3, 'art',
  'Wrote of the suffering of war and rebellion; often called China\'s greatest poet.',
  G(746, 759, "Chang'an and the rebellion", 'changan'), G(760, 765, 'Thatched cottage at Chengdu', 'chengdu'),
  G(766, 770, 'Last wanderings', (109.47, 31.02), (112.9, 28.2)))
P('Gao Xianzhi', 'Tang general', (705, 756), 3, 'war',
  'Korean-born Tang general who crossed the Pamirs and lost the Battle of Talas to the Arabs in 751.',
  G(747, 751, 'Wars in Central Asia', 'kashgar', (73.5, 36.3), 'kashgar', 'talas'))
P('An Lushan', 'Tang general and rebel', (703, 757), 2, 'war',
  "His rebellion, one of history's deadliest, broke the power of the Tang dynasty.",
  G(755, 757, 'An Lushan rebellion', 'beijing', 'luoyang', 'changan', 'luoyang'))
P('Adi Shankara', 'Hindu philosopher', (788, 820), 2, 'faith mind',
  'Taught Advaita Vedanta, that the self and the absolute are one, and founded monasteries at the four corners of India.',
  G(796, 820, 'Wandering teacher', 'kaladi', 'varanasi', (79.49, 30.74), (68.97, 22.24), 'sringeri', 'puri', 'kanchipuram'))
P('Emperor Kanmu', 'Emperor of Japan', (737, 806), 3, 'rule',
  'Moved the capital to Heian-kyō, modern Kyoto, where it stayed for a thousand years.',
  R(781, 806, 'Emperor of Japan', 'Japan', 'Yamato', at='kyoto'))
P('Kūkai', 'Founder of Shingon Buddhism', (774, 835), 3, 'faith',
  'Brought esoteric Buddhism from China and founded the monastery on Mount Kōya.',
  G(804, 806, 'Studies in China', 'nara', 'changan', 'kyoto'), G(816, 835, 'Mount Kōya', 'mount_koya'))
P('Wang Geon', 'Founder of Goryeo', (877, 943), 3, 'rule',
  'Reunited Korea under the Goryeo dynasty, which gave Korea its name.',
  R(918, 943, 'King of Goryeo', 'Korea', at='kaesong'), wiki='Taejo of Goryeo')
P('Emperor Taizu of Song', 'Founder of the Song dynasty', (927, 976), 2, 'rule',
  'General Zhao Kuangyin, who seized the throne and reunited China under scholar-officials instead of generals.',
  R(960, 976, 'Emperor of Song', 'Song Empire', at='kaifeng'))
P('Murasaki Shikibu', 'Japanese novelist', (973, 1014), 2, 'art',
  "Lady-in-waiting at the Heian court who wrote The Tale of Genji, often called the world's first novel.",
  G(1000, 1014, 'Writes The Tale of Genji at court', 'kyoto'))
P('Fujiwara no Michinaga', 'Regent of Japan', (966, 1028), 3, 'rule',
  'Ruled Japan through four emperors married to his daughters, at the height of Fujiwara power.',
  R(995, 1027, 'Regent of Japan', 'Imperial Japan (Fujiwara)', 'Japan', at='kyoto'))
P('Rajaraja I', 'Chola emperor', (947, 1014), 3, 'rule',
  'Built the Chola navy and the great Brihadeeswarar temple at Thanjavur.',
  R(985, 1014, 'Chola emperor', 'Chola Empire', 'Cholas', at='thanjavur'), wiki='Rajaraja I')
P('Rajendra I', 'Chola emperor', (971, 1044), 3, 'rule war',
  'Sent the Chola fleet across the Bay of Bengal to raid Srivijaya in Sumatra.',
  G(1025, 1025, 'Naval raid on Srivijaya', 'thanjavur', (95.3, 5.5), 'palembang', 'thanjavur'),
  R(1014, 1044, 'Chola emperor', 'Chola Empire', at='thanjavur'), wiki='Rajendra I')
P('Anawrahta', 'King of Pagan', (1015, 1078), 3, 'rule faith',
  'United Burma for the first time and made it Theravada Buddhist.',
  R(1044, 1077, 'King of Pagan', 'Kingdom of Pagan', 'Pagan', at='pagan'))
P('Wang Anshi', 'Song chancellor and reformer', (1021, 1086), 3, 'reform',
  'Pushed through sweeping New Policies on farm loans, taxes and the army.',
  G(1069, 1076, 'Chancellor and reformer', 'kaifeng'))
P('Emperor Huizong of Song', 'Emperor of Song China', (1082, 1135), 3, 'rule art',
  'A brilliant painter and calligrapher who lost north China to the Jurchens and died their prisoner.',
  R(1100, 1126, 'Emperor of Song', 'Song Empire', at='kaifeng'), G(1127, 1135, 'Captive of the Jin', (129.3, 45.75)))
P('Suryavarman II', 'King of the Khmer Empire', (1094, 1150), 2, 'rule',
  'Built Angkor Wat, the largest religious monument in the world.',
  R(1113, 1150, 'King of Angkor', 'Khmer Empire', at='angkor'))
P('Yue Fei', 'Song general', (1103, 1142), 3, 'war',
  'Fought to win back north China from the Jin and was executed on false charges; a national hero.',
  G(1134, 1140, 'Campaigns against the Jin', 'wuhan', (114.0, 33.6), 'kaifeng'), G(1141, 1142, 'Prison and death', 'hangzhou'))
P('Zhu Xi', 'Neo-Confucian philosopher', (1130, 1200), 3, 'mind',
  'His commentaries on the classics were the basis of the Chinese civil-service exams for 700 years.',
  G(1150, 1200, 'Teaching in the Wuyi Mountains', (118.03, 27.75)))
P('Minamoto no Yoritomo', 'First shogun of Japan', (1147, 1199), 2, 'rule war',
  'Won the Genpei War and set up the first shogunate at Kamakura, beginning 700 years of samurai rule.',
  G(1180, 1199, 'Shogun at Kamakura', 'kamakura'))
P('Minamoto no Yoshitsune', 'Samurai general', (1159, 1189), 3, 'war',
  "Yoritomo's brother, who won the Genpei War at Dan-no-ura and was hunted to death by him.",
  G(1184, 1185, 'Victories of the Genpei War', 'kyoto', (135.08, 34.64), (134.07, 34.3), (130.96, 33.96)),
  G(1186, 1189, 'Flight and death', (141.1, 38.99)))
P('Prithviraj Chauhan', 'Rajput king', (1166, 1192), 3, 'rule war',
  'Beat Muhammad of Ghor at Tarain in 1191 but lost to him there the next year.',
  G(1191, 1192, 'Battles of Tarain', (74.64, 26.45), (76.9, 29.8)), R(1177, 1190, 'King of Ajmer and Delhi', 'Rajput kingdoms', at=(74.64, 26.45)))
P('Muhammad of Ghor', 'Sultan of the Ghurids', (1149, 1206), 3, 'war rule',
  "His victory at Tarain in 1192 opened northern India to Muslim rule.",
  G(1173, 1206, 'Conquest of northern India', 'ghazni', 'lahore', (76.9, 29.8), 'delhi', 'lahore'))
P('Qutb ud-Din Aibak', 'First sultan of Delhi', (1150, 1210), 3, 'rule',
  'A former slave who founded the Delhi Sultanate and began the Qutb Minar.',
  R(1206, 1210, 'Sultan of Delhi', 'Sultanate of Delhi', at='delhi'))
P('Razia Sultana', 'Sultana of Delhi', (1205, 1240), 3, 'rule',
  'The only woman to rule the Delhi Sultanate.',
  R(1236, 1240, 'Sultana of Delhi', 'Sultanate of Delhi', at='delhi'))
P('Jayavarman VII', 'King of the Khmer Empire', (1122, 1218), 3, 'rule faith',
  "Drove out the Chams, made the Khmer empire Buddhist and built the Bayon temple with its stone faces.",
  R(1181, 1218, 'King of Angkor', 'Khmer Empire', at='angkor'))
P('Hōjō Tokimune', 'Regent of the Kamakura shogunate', (1251, 1284), 3, 'rule war',
  'Led Japan against the Mongol invasions of 1274 and 1281.',
  R(1268, 1284, 'Shogun\'s regent', 'Shogun Japan (Kamakura)', 'Imperial Japan (Fujiwara)', at='kamakura'))
P('Ram Khamhaeng', 'King of Sukhothai', (1237, 1298), 3, 'rule',
  'Credited with creating the Thai alphabet.',
  R(1279, 1298, 'King of Sukhothai', 'Sukhothai', at='sukhothai'), wiki='Ram Khamhaeng')

# ---------- Africa and the Americas ----------
P('Sundiata Keita', 'Founder of the Mali Empire', (1217, 1255), 2, 'rule war',
  'The lion king of the Mande epic: beat the Sosso at Kirina and founded the Mali Empire.',
  G(1235, 1235, 'Battle of Kirina', (-8.0, 12.8)), R(1235, 1255, 'Mansa of Mali', 'Mali', at='niani'))
P('Gebre Mesqel Lalibela', 'King of Ethiopia', (1162, 1221), 3, 'rule faith',
  'Had eleven churches carved down into the living rock as a new Jerusalem.',
  G(1185, 1221, 'King, builder of rock churches', 'lalibela'))
P('Eight Deer Jaguar Claw', 'Mixtec ruler', (1063, 1115), 3, 'war rule',
  'Warlord whose conquests are painted in the Mixtec picture books.',
  G(1083, 1115, 'Lord of Tilantongo', (-97.3, 17.29), (-97.67, 16.0)))

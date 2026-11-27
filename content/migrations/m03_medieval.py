"""Migrations of the Middle Ages: Magyars, Norse settlers, Turks, Banu Hilal, Romani, German settlers in the east, Jews to
Poland, the Mexica, Thule Inuit, the Navajo and Apache, Chinese flights south, the Tai and the Vietnamese, the Arawaks and
the Fulani."""
from _lib import M, S, mv, site

M('arawaks', 'The Arawaks settle the Caribbean', 'Arawaks', 'seafarers', '#1abc9c', -500, 1450,
  'From the Orinoco delta, farming peoples speaking Arawakan languages paddled great dugout canoes up the chain of the '
  'Lesser Antilles, reaching Puerto Rico about 400 BC. Their descendants, the Taino, spread over Hispaniola, Cuba, Jamaica '
  'and the Bahamas, where Columbus met them in 1492. Later the Kalinago (Island Caribs) followed the same path.',
  rank=2, steps=[
    S(-500, 'c. 500 BC to AD 600', 'Up the island chain',
      'The Saladoid people, named after their white-on-red pottery, came out of the Orinoco and settled island after island '
      'within sight of the next, until they reached Puerto Rico and Hispaniola.',
      moves=[mv('canoe', (-61.0, 9.3, -500), (-61.6, 10.4, -470), (-61.7, 12.1, -440), (-61.2, 13.2, -420), (-61.0, 14.0, -410),
                (-61.0, 14.7, -405), (-61.4, 15.4, -400), (-61.5, 16.3, -395), (-62.7, 17.3, -390), (-64.6, 18.3, -385), (-66.1, 18.4, -380), label='Saladoid'),
             mv('canoe', (-66.1, 17.9, 400), (-67.5, 17.9, 430), (-68.6, 18.1, 460), (-69.9, 18.4, 500), label='To Hispaniola')],
      sites=[site('Orinoco delta', -61.0, 9.0, -500, 'Homeland of the Arawakan farmers who settled the islands.')]),
    S(600, 'c. 600 to 1450', 'The Taino world',
      'From Hispaniola the Taino settled Cuba, Jamaica and the Bahamas, growing cassava, playing a ball game in stone courts. '
      'Kalinago warriors moved up the Lesser Antilles from about 1200, taking the islands from the Arawaks.',
      moves=[mv('canoe', (-73.4, 19.95, 600), (-74.1, 20.15, 610), label='Taino to Cuba'),
             mv('foot', (-74.1, 20.2, 610), (-76.0, 20.4, 650), (-77.9, 21.4, 700), (-80.5, 22.5, 750), (-82.5, 22.6, 800), label='Taino'),
             mv('canoe', (-74.4, 19.0, 650), (-75.6, 18.3, 680), (-76.6, 18.0, 700), label='To Jamaica'),
             mv('canoe', (-72.8, 20.0, 700), (-73.3, 21.0, 750), (-74.5, 23.0, 800), (-75.5, 24.3, 850), label='To the Bahamas'),
             mv('canoe', (-61.0, 9.3, 1200), (-61.6, 10.4, 1230), (-61.7, 12.1, 1260), (-61.2, 13.2, 1280), (-61.0, 14.0, 1300), (-61.0, 14.7, 1320), (-61.4, 15.4, 1340), label='Kalinago')],
      sites=[site('Guanahani', -74.5, 24.05, 1450, 'Taino island in the Bahamas where Columbus landed in 1492.')]),
  ])

M('han-south', 'The Chinese flights to the south', 'Northern Chinese', 'refugees', '#922b21', 307, 1140,
  'Twice the people of the north China plain fled south in their millions. When the Xiongnu sacked Luoyang in 311, nobles, '
  'scholars and farmers crossed the Yangtze to found a new court at Jiankang (Nanjing): the "clothes and caps went south". '
  'In 1127 the Jurchen took Kaifeng and the Song court fled again, to Hangzhou. Each time the south grew richer, until it '
  'became China\'s heart.',
  rank=1, steps=[
    S(307, '307 to 330', 'The clothes and caps go south',
      'After the Disaster of Yongjia in 311, when Luoyang was sacked and the emperor taken, perhaps a million northerners went '
      'south over a generation. The Eastern Jin dynasty ruled from Jiankang.',
      moves=[mv('foot', (112.45, 34.62, 307), (114.0, 33.8, 310), (116.0, 33.0, 313), (117.5, 32.5, 316), (118.78, 32.06, 318), label='Northerners'),
             mv('foot', (114.3, 35.0, 311), (115.5, 33.5, 315), (116.5, 31.5, 320), (117.0, 30.5, 325), label='To the Yangtze')],
      sites=[site('Luoyang', 112.45, 34.62, 311, 'Sacked by the Xiongnu in 311; tens of thousands killed.'),
             site('Jiankang', 118.78, 32.06, 317, 'Nanjing, capital of the Eastern Jin and the southern dynasties.')]),
    S(1127, '1127 to 1140', 'The Song cross the Yangtze',
      'When the Jurchen Jin took Kaifeng in 1127 and carried off two emperors, a prince of the Song fled south. Millions '
      'followed; the Southern Song made Hangzhou, then the largest city on earth, their capital.',
      moves=[mv('foot', (114.3, 34.8, 1127), (115.5, 33.5, 1128), (117.0, 32.2, 1129), (118.8, 32.0, 1130), (120.15, 30.25, 1138), label='Song refugees')],
      sites=[site('Kaifeng', 114.31, 34.8, 1127, 'The Song capital falls to the Jurchen.'),
             site('Hangzhou', 120.15, 30.25, 1138, 'The Southern Song capital, Marco Polo\'s "Quinsai".')]),
  ])

M('magyars', 'The Magyars', 'Magyars', 'nomads', '#c0392b', 750, 955,
  'The Hungarians, the Magyars, speak a language whose closest kin are spoken in western Siberia. Over centuries their '
  'ancestors moved from the Ural forests onto the steppe and west along it. In 895, under Arpad, seven tribes crossed the '
  'Carpathians and took the plain that is Hungary still. For sixty years their horsemen raided Europe, from Spain to '
  'Constantinople, until Otto I beat them at the Lech in 955.',
  numbers='About 400,000 people crossed the Carpathians', rank=1, steps=[
    S(750, 'c. 750 to 890', 'Along the steppe',
      'From "Magna Hungaria" near the Urals the Magyars moved to Levedia by the Don and then to Etelkoz between the Dnieper '
      'and the Danube, living alongside the Khazars as herders and horsemen.',
      moves=[mv('horse', (56.0, 54.0, 750), (50.0, 51.0, 790), (42.0, 48.5, 830), (36.0, 47.5, 860), (31.0, 47.2, 880), label='Magyars')],
      sites=[site('Magna Hungaria', 56.0, 54.5, 750, 'The Magyars\' old home on the edge of the Urals, where a Dominican friar found Hungarian speakers in 1235.')]),
    S(895, '895 to 900', 'The Conquest',
      'Attacked by the Pechenegs, the seven tribes crossed the Verecke pass in 895 and took the Carpathian basin from Bulgars, '
      'Moravians and Slavs. Hungarians call it the honfoglalas, the "taking of the homeland".',
      moves=[mv('horse', (31.0, 47.2, 895), (26.5, 48.0, 895), (23.2, 48.8, 895), (22.0, 48.2, 896), (20.0, 47.6, 898), (19.0, 47.5, 900), label='Arpad\'s Magyars')],
      sites=[site('Verecke Pass', 23.08, 48.81, 895, 'The pass over the Carpathians where the Magyars entered their new land.')]),
    S(899, '899 to 955', 'The raids',
      'Magyar riders struck Italy, Germany, France, even Spain, faster than any army could follow. "From the arrows of the '
      'Hungarians, deliver us, O Lord," prayed the monks. In 955 Otto I destroyed their army on the Lechfeld near Augsburg.',
      moves=[mv('horse', (19.0, 47.5, 899), (16.0, 46.5, 899), (13.4, 45.8, 899), (11.5, 45.4, 899), (10.0, 45.5, 900), label='Raid on Italy'),
             mv('horse', (19.0, 47.5, 926), (16.4, 48.2, 926), (12.0, 48.5, 926), (9.4, 47.4, 926), (7.5, 48.3, 926), (4.0, 49.3, 937), label='Raid on the west'),
             mv('horse', (19.0, 47.5, 955), (16.0, 48.0, 955), (12.5, 48.3, 955), (10.9, 48.37, 955), label='To the Lechfeld')],
      sites=[site('Lechfeld', 10.9, 48.3, 955, 'Otto I crushes the Magyar army; they settle down and become a Christian kingdom.')]),
  ])

M('norse-settlers', 'The Norse settlers', 'Norse', 'seafarers', '#34495e', 750, 1010,
  'The Viking Age was raids, but also one of the great migrations of the Middle Ages. Norwegians settled the islands of '
  'the North Atlantic, Iceland and Greenland, and touched America; Danes settled the Danelaw in England and Normandy in '
  'France; Swedes went east along the rivers of Russia, where the Rus\' founded the first Russian state.',
  rank=1, war='viking-invasions', steps=[
    S(750, '750 to 900', 'The Rus\' go east',
      'Swedish traders and warriors, the Varangians, rowed up the Gulf of Finland to Staraya Ladoga, then down the Volga and '
      'the Dnieper to Baghdad\'s silver and Constantinople. Rurik ruled Novgorod from 862, and Oleg took Kiev in 882.',
      moves=[mv('river', (18.5, 59.3, 750), (21.0, 59.6, 755), (25.0, 59.8, 758), (29.5, 60.0, 760), (32.3, 60.0, 762), (31.3, 58.5, 862),
                (30.8, 55.5, 870), (30.5, 50.45, 882), label='Rus\''),
             mv('river', (30.5, 50.45, 882), (32.5, 47.0, 890), (31.0, 46.4, 893), (30.5, 44.0, 895), (29.0, 41.1, 900), label='To Constantinople')],
      sites=[site('Staraya Ladoga', 32.3, 60.0, 753, 'The first Norse trading town in Russia.'),
             site('Kiev', 30.52, 50.45, 882, 'Capital of Kievan Rus\'.')]),
    S(790, '790 to 870', 'Islands and the Danelaw',
      'After the first raids, Norwegians settled the Shetlands, Orkneys, Hebrides and founded Dublin in 841. The Danish '
      'Great Heathen Army landed in 865, took York and settled half of England, the Danelaw.',
      moves=[mv('longship', (5.3, 60.4, 790), (2.0, 60.4, 795), (-1.2, 60.2, 800), (-3.0, 59.4, 810), (-5.5, 58.8, 820), (-7.2, 57.5, 830),
                (-6.5, 55.8, 835), (-6.0, 54.5, 838), (-6.1, 53.35, 841), label='Norwegians'),
             mv('longship', (8.4, 55.4, 865), (8.0, 55.0, 865), (4.0, 53.8, 865), (1.0, 52.9, 865), (0.3, 53.6, 866), (-0.1, 53.7, 866), label='Danes'),
             mv('foot', (-0.1, 53.7, 866), (-1.08, 53.96, 867), label='Great Army')],
      sites=[site('Dublin', -6.26, 53.35, 841, 'Founded as a Norse longphort, a ship camp, in 841.'),
             site('Jorvik', -1.08, 53.96, 867, 'York, capital of the Viking kingdom of Northumbria.')]),
    S(870, '870 to 930', 'Iceland and Normandy',
      'From about 870 Norwegian families fleeing King Harald Finehair sailed to Iceland; in sixty years it was full, and in '
      '930 they founded the Althing, a parliament. In 911 the Frankish king gave Rouen to the Viking chief Rollo: Normandy.',
      moves=[mv('longship', (5.3, 60.4, 870), (1.0, 61.5, 872), (-6.8, 62.0, 873), (-12.0, 63.5, 874), (-18.0, 63.2, 874), (-20.5, 63.2, 874), (-22.8, 63.7, 874), (-21.95, 64.15, 874), label='To Iceland'),
             mv('longship', (8.0, 55.0, 900), (4.0, 53.5, 905), (1.5, 51.2, 908), (0.2, 49.7, 910), (1.1, 49.44, 911), label='Rollo\'s Danes')],
      sites=[site('Thingvellir', -21.12, 64.26, 930, 'Where the Icelanders met in the Althing from 930.'),
             site('Rouen', 1.1, 49.44, 911, 'Given to Rollo: the start of Normandy.')]),
    S(985, '985 to 1010', 'Greenland and Vinland',
      'Erik the Red, outlawed from Iceland, led 25 ships to Greenland in 985; 14 arrived. About 1000 his son Leif Eriksson '
      'reached the coast of North America, Vinland. The settlement at L\'Anse aux Meadows did not last; the Greenland Norse '
      'held on for four centuries.',
      moves=[mv('longship', (-21.9, 64.1, 985), (-26.0, 64.0, 985), (-35.0, 62.5, 985), (-42.0, 59.5, 986), (-44.0, 59.5, 986), (-46.0, 60.3, 986), (-45.5, 61.1, 986), label='Erik the Red'),
             mv('longship', (-46.0, 60.3, 1000), (-48.5, 60.5, 1000), (-53.0, 62.5, 1000), (-58.0, 59.5, 1001), (-56.0, 54.5, 1001), (-55.2, 52.5, 1001), (-55.53, 51.6, 1001), label='Leif Eriksson')],
      sites=[site('Brattahlid', -45.5, 61.15, 986, 'Erik the Red\'s farm in Greenland.'),
             site('L\'Anse aux Meadows', -55.53, 51.6, 1001, 'The only known Norse site in North America.')]),
  ])

M('thule', 'The Thule (Inuit) migration', 'Thule Inuit', 'folk', '#5dade2', 1000, 1350,
  'The ancestors of the Inuit, the Thule people, came out of Alaska about 1000 and crossed the whole Canadian Arctic to '
  'Greenland in perhaps two centuries, with dog sleds, kayaks, big skin boats and harpoons for whales. They replaced the '
  'older Dorset people and met the Norse in Greenland. Every Inuit people from Alaska to Greenland descends from them.',
  rank=2, steps=[
    S(1000, 'c. 1000 to 1200', 'Across the Arctic',
      'Following the bowhead whales in a warm spell, the Thule moved east along the northern coasts and the channels between '
      'the Arctic islands, faster than any people before them.',
      moves=[mv('foot', (-156.8, 71.3, 1000), (-145.0, 70.2, 1050), (-133.0, 69.5, 1100), (-120.0, 69.0, 1130), (-105.0, 68.8, 1160),
                (-95.0, 70.0, 1180), (-85.0, 73.5, 1200), (-78.0, 76.5, 1220), label='Thule')]),
    S(1200, 'c. 1200 to 1350', 'Into Greenland',
      'They crossed Smith Sound into Greenland and moved down both coasts, meeting the Norse farmers, whom they called '
      'Kavdlunait. By the time the Norse colony died out in the 1400s, the Inuit held all of Greenland.',
      moves=[mv('foot', (-78.0, 76.5, 1200), (-72.0, 77.5, 1230), (-68.0, 76.5, 1260), (-60.0, 75.5, 1280), (-56.0, 72.0, 1300),
                (-53.5, 68.5, 1320), (-52.0, 65.5, 1340), (-49.0, 62.0, 1350), label='Inuit')],
      sites=[site('Smith Sound', -73.0, 78.0, 1230, 'The narrows between Canada and Greenland.')]),
  ])

M('turks-west', 'The Turks move west', 'Turks', 'nomads', '#a93226', 985, 1100,
  'In the eleventh century Turkic horsemen poured west out of Central Asia. The Oghuz Turks led by the Seljuk clan took '
  'Iran and Baghdad, and after Manzikert in 1071 their herds and families filled Anatolia, which in time became Turkey. '
  'To the north, the Kipchaks (Cumans) spread over the whole steppe from the Irtysh to the Danube.',
  rank=1, war='seljuk-conquests', steps=[
    S(985, '985 to 1040', 'The Oghuz cross the Oxus',
      'Seljuk, a chief of the Oghuz on the lower Syr Darya, became a Muslim about 985. His grandsons Tughril and Chaghri led '
      'their tribes into Khorasan and beat the Ghaznavids at Dandanaqan in 1040.',
      moves=[mv('horse', (65.5, 44.5, 985), (64.4, 41.5, 1010), (64.4, 39.8, 1025), (62.0, 37.5, 1035), (62.2, 37.4, 1040), label='Seljuk Turks')],
      sites=[site('Dandanaqan', 62.2, 37.4, 1040, 'The Seljuks win Khorasan from the Ghaznavids.')]),
    S(1030, '1030 to 1080', 'The Kipchaks on the steppe',
      'From the Irtysh, the Kipchaks pushed west across the steppe, driving the Pechenegs and Oghuz before them. Russians '
      'called them Polovtsians, Byzantines Cumans; their lands became the Dasht-i Kipchak, the Kipchak steppe.',
      moves=[mv('horse', (76.0, 51.0, 1030), (66.0, 50.0, 1045), (55.0, 49.0, 1055), (46.0, 48.0, 1065), (38.0, 47.5, 1075), (32.0, 47.0, 1080), label='Kipchaks')]),
    S(1040, '1040 to 1071', 'Iran and Baghdad',
      'Tughril took Iran, entered Baghdad in 1055 as protector of the caliph, and was named sultan. Turkmen herders roamed '
      'ahead of the armies into Armenia and Anatolia.',
      moves=[mv('horse', (62.2, 37.4, 1040), (58.0, 36.2, 1042), (51.4, 35.7, 1050), (47.0, 34.3, 1053), (44.4, 33.3, 1055), label='Seljuks'),
             mv('horse', (51.4, 35.7, 1050), (47.0, 38.0, 1055), (44.5, 39.0, 1064), (42.5, 39.15, 1071), label='Turkmen')],
      sites=[site('Baghdad', 44.4, 33.32, 1055, 'Tughril becomes sultan, guardian of the Abbasid caliph.'),
             site('Manzikert', 42.53, 39.15, 1071, 'Alp Arslan captures the Byzantine emperor; Anatolia opens to the Turks.')]),
    S(1071, '1071 to 1100', 'Into Anatolia',
      'After Manzikert Turkmen tribes moved in with their flocks. The Seljuks of Rum ruled from Nicaea, then from Konya.',
      moves=[mv('horse', (42.5, 39.15, 1071), (39.5, 39.8, 1074), (35.5, 39.0, 1077), (32.5, 38.6, 1080), (30.0, 40.4, 1081), label='Turkmen'),
             mv('horse', (30.0, 40.4, 1097), (32.5, 37.87, 1100), label='To Konya')],
      sites=[site('Konya', 32.49, 37.87, 1100, 'Capital of the Seljuk sultanate of Rum.')]),
  ])

M('banu-hilal', 'The Banu Hilal', 'Banu Hilal', 'nomads', '#ca6f1e', 1050, 1160,
  'In about 1050 the Fatimid caliph of Egypt, to punish his rebellious vassals in Ifriqiya, let loose on them the Bedouin '
  'tribes of the Banu Hilal and Banu Sulaym. Some 200,000 Arabs with their camels moved west across North Africa, sacked '
  'Kairouan in 1057 and spread over the plains of the Maghreb. They did more than the first conquest to make North Africa '
  'Arabic-speaking.',
  rank=2, steps=[
    S(1050, '1050 to 1057', 'Out of Egypt',
      'The tribes crossed Cyrenaica and Tripolitania and beat the Zirid army at Haydaran in 1052. Kairouan was abandoned to '
      'them in 1057.',
      moves=[mv('horse', (32.5, 26.5, 1050), (29.0, 30.0, 1051), (24.0, 31.6, 1051), (20.0, 31.5, 1051), (15.0, 31.5, 1052), (11.5, 33.0, 1052),
                (10.1, 35.68, 1057), label='Banu Hilal')],
      sites=[site('Kairouan', 10.1, 35.68, 1057, 'The old capital of Ifriqiya, sacked by the Bedouin.')]),
    S(1060, '1060 to 1160', 'Across the Maghreb',
      'The tribes spread west over the high plains of Algeria. The Almohads moved many of them on into Morocco. Ibn Khaldun '
      'later compared them to a swarm of locusts; others credit their epic, the Taghriba, which is still sung.',
      moves=[mv('horse', (10.1, 35.68, 1060), (7.0, 35.5, 1080), (4.0, 35.5, 1100), (1.0, 35.0, 1130), (-2.5, 34.5, 1150), (-6.0, 34.0, 1160), label='Arab tribes')]),
  ])

M('ostsiedlung', 'German settlers in the east', 'German settlers', 'settlers', '#5b2c6f', 1140, 1350,
  'From the twelfth century, lords and churchmen in the lands east of the Elbe invited farmers, miners and townsmen from '
  'Flanders, the Rhineland, Saxony and Franconia, offering land and German town law. Hundreds of thousands moved east over '
  'two centuries, into Brandenburg, Pomerania, Silesia, Bohemia, Prussia and as far as Transylvania. The Ostsiedlung changed '
  'the map of languages in Europe until 1945.',
  rank=2, steps=[
    S(1140, '1140 to 1250', 'East of the Elbe',
      'Settlers cleared forest and drained marsh in Holstein, Mecklenburg and Brandenburg; Slavic princes in Pomerania and '
      'Silesia invited them too. New towns like Lubeck (1143) and Berlin grew.',
      moves=[mv('wagon', (5.5, 51.0, 1140), (8.0, 52.0, 1150), (10.68, 53.87, 1160), (13.0, 54.0, 1200), (14.6, 53.4, 1230), label='Flemings and Saxons'),
             mv('wagon', (8.0, 52.0, 1150), (11.6, 52.1, 1160), (13.4, 52.5, 1200), (17.03, 51.1, 1240), label='To Silesia')],
      sites=[site('Lubeck', 10.69, 53.87, 1143, 'Founded 1143; later queen of the Hanseatic League.')]),
    S(1141, '1141 to 1350', 'To Prussia and Transylvania',
      'King Geza II of Hungary invited settlers, mostly from the Moselle, to Transylvania, where the "Saxons" built fortified '
      'churches. In the 1200s the Teutonic Knights brought colonists into conquered Prussia, founding Thorn, Kulm and Konigsberg.',
      moves=[mv('wagon', (6.5, 49.7, 1141), (10.0, 49.8, 1145), (14.0, 48.5, 1150), (19.0, 47.5, 1155), (22.0, 46.5, 1160), (24.15, 45.8, 1165), label='Transylvanian Saxons'),
             mv('wagon', (11.6, 52.1, 1230), (15.0, 52.8, 1240), (18.6, 53.0, 1250), (20.5, 54.7, 1260), (21.5, 54.2, 1300), label='To Prussia')],
      sites=[site('Hermannstadt', 24.15, 45.8, 1191, 'Sibiu, chief town of the Transylvanian Saxons.'),
             site('Konigsberg', 20.51, 54.71, 1255, 'Founded by the Teutonic Knights.')]),
  ])

M('ashkenazi-east', 'Jews move to Poland and Lithuania', 'Ashkenazi Jews', 'exiles', '#6c3483', 1096, 1500,
  'The Jews of the Rhineland, the first Ashkenazim, suffered massacres in the First Crusade in 1096 and later in the Black '
  'Death. England expelled its Jews in 1290 and France in 1306. Polish kings, starting with the charter of Kalisz in 1264, '
  'welcomed them as townspeople and traders. By 1500 Poland and Lithuania held the largest Jewish community in the world, '
  'and Yiddish, born on the Rhine, was its language.',
  rank=2, steps=[
    S(1096, '1096 to 1306', 'Massacres and expulsions in the west',
      'Crusaders on their way east murdered the Jews of Worms, Mainz and Speyer in 1096. Expelled from England and France, '
      'Jews moved to Germany and on east.',
      moves=[mv('foot', (8.3, 49.8, 1096), (11.0, 50.0, 1120), (14.4, 50.1, 1150), label='Rhineland Jews'),
             mv('sail', (0.9, 51.45, 1290), (1.6, 51.1, 1290), (1.9, 50.95, 1290), label='Expelled from England'),
             mv('foot', (2.35, 48.86, 1306), (5.0, 49.0, 1306), (7.8, 49.5, 1306), label='Expelled from France')],
      sites=[site('Mainz', 8.27, 50.0, 1096, 'One of the three great Jewish communities of the Rhine, attacked in 1096.')]),
    S(1264, '1264 to 1500', 'The charter of Kalisz',
      'Boleslaw the Pious\'s charter of 1264, and Casimir the Great after the Black Death, protected Jews in Poland. Jewish '
      'towns grew in Krakow, Lviv, Lublin, Grodno and Vilnius.',
      moves=[mv('foot', (11.0, 50.0, 1264), (14.4, 50.1, 1270), (17.0, 51.1, 1290), (19.94, 50.06, 1330), (22.57, 51.25, 1380), (24.03, 49.84, 1400), label='To Poland'),
             mv('foot', (19.94, 50.06, 1350), (21.0, 52.2, 1380), (23.8, 53.7, 1388), (25.28, 54.69, 1420), label='To Lithuania')],
      sites=[site('Kalisz', 18.09, 51.76, 1264, 'Where Duke Boleslaw granted the Jews their charter.')]),
  ])

M('tai', 'The Tai peoples move south', 'Tai', 'folk', '#d35400', 1000, 1350,
  'The Tai peoples, ancestors of the Thai, Lao and Shan, came from the hills of today\'s Guangxi and Guizhou in southern '
  'China. Between about 1000 and 1300 they moved south-west down the river valleys into the lands of the Mon and the '
  'Khmer, founding kingdoms: Sukhothai and Lanna in Thailand, Lan Xang in Laos, the Shan states of Burma, and the Ahom '
  'kingdom in Assam.',
  rank=2, steps=[
    S(1000, 'c. 1000 to 1200', 'Down the valleys',
      'Rice farmers organised in muang, valley chiefdoms, moved south and west, pushed perhaps by Chinese expansion and '
      'drawn by open land.',
      moves=[mv('foot', (107.5, 23.8, 1000), (105.0, 23.0, 1050), (103.0, 22.0, 1100), (101.5, 21.0, 1150), (100.3, 20.0, 1200), label='Tai')]),
    S(1200, '1200 to 1350', 'New kingdoms',
      'Tai chiefs threw off Khmer rule at Sukhothai about 1238; Mangrai founded Chiang Mai in 1296; Sukaphaa led the Ahom over '
      'the mountains into Assam in 1228; Fa Ngum founded Lan Xang in 1353.',
      moves=[mv('foot', (100.3, 20.0, 1220), (99.9, 18.8, 1230), (99.8, 17.0, 1238), label='To Sukhothai'),
             mv('foot', (100.3, 20.0, 1260), (99.0, 18.8, 1296), label='To Chiang Mai'),
             mv('foot', (99.0, 23.5, 1200), (97.5, 25.0, 1215), (95.5, 26.5, 1225), (94.6, 27.0, 1228), label='Ahom'),
             mv('foot', (100.3, 20.0, 1300), (102.13, 19.89, 1350), label='To Luang Prabang')],
      sites=[site('Sukhothai', 99.82, 17.01, 1238, 'The first great Thai kingdom.')]),
  ])

M('romani', 'The Romani migration', 'Romani', 'folk', '#af601a', 1000, 1505,
  'The Romani people came from north-western India: their language is close to Punjabi and Hindi. They left about the year '
  '1000, perhaps as camp followers driven by the wars of Mahmud of Ghazni, and moved through Persia and Armenia into the '
  'Byzantine Empire. In the fifteenth century they spread across all of Europe, where they were called "Egyptians", the '
  'root of "Gypsies".',
  rank=2, steps=[
    S(1000, 'c. 1000 to 1300', 'Out of India',
      'Words borrowed from Persian, Armenian and Greek in Romani show the road they took, and how long they stayed: long in '
      'the Greek-speaking Byzantine world.',
      moves=[mv('foot', (74.0, 31.5, 1000), (69.0, 33.0, 1030), (61.0, 34.3, 1060), (53.0, 35.5, 1100), (46.3, 38.1, 1150), (44.5, 40.2, 1180),
                (40.0, 40.5, 1220), (33.0, 39.5, 1260), (29.0, 41.0, 1300), label='Romani')]),
    S(1350, '1350 to 1505', 'Into Europe',
      'Romani appear in Greece and the Balkans in the 1300s. In 1417 a band with a letter from Emperor Sigismund reached '
      'Germany; they were in Paris in 1427, Spain by 1425 and Scotland by 1505.',
      moves=[mv('foot', (29.0, 41.0, 1350), (23.7, 38.0, 1360), (21.7, 36.8, 1384), (23.3, 42.7, 1385), (26.1, 44.4, 1385), label='Romani'),
             mv('foot', (26.1, 44.4, 1410), (21.0, 46.0, 1414), (17.1, 48.1, 1416), (14.4, 50.1, 1417), (10.0, 50.0, 1418), (6.0, 50.8, 1420),
                (2.35, 48.86, 1427), label='To the west'),
             mv('foot', (2.35, 48.86, 1427), (1.0, 45.0, 1430), (-1.5, 42.0, 1440), (-3.7, 40.4, 1450), label='To Spain'),
             mv('foot', (2.35, 48.86, 1450), (1.5, 50.5, 1460), (0.0, 51.5, 1480), (-1.5, 53.5, 1495), (-3.2, 55.95, 1505), label='To Britain')],
      sites=[site('Modon', 21.7, 36.8, 1384, 'A Venetian port in Greece, called "Little Egypt", where travellers met Romani.'),
             site('Paris', 2.35, 48.86, 1427, 'A Romani band camps at La Chapelle in August 1427.')]),
  ])

M('mexica', 'The Mexica migration', 'Mexica (Aztecs)', 'folk', '#16a085', 1111, 1325,
  'The Mexica told how they left Aztlan, an island in a lake somewhere in the north-west, in about 1111, led by their god '
  'Huitzilopochtli. They wandered for two centuries, settling and leaving, until they saw an eagle on a cactus on an island '
  'in Lake Texcoco and founded Tenochtitlan there in 1325. The eagle is on Mexico\'s flag today.',
  story='ev:tenochtitlan', rank=2, steps=[
    S(1111, 'c. 1111 to 1250', 'From Aztlan',
      'Where Aztlan lay no one knows; the story is part legend. The codices show the Mexica walking, carrying their god, '
      'through Chicomoztoc, the place of the seven caves, and Coatepec near Tula.',
      moves=[mv('foot', (-104.5, 22.5, 1111), (-103.0, 21.8, 1140), (-101.5, 21.0, 1170), (-99.6, 20.4, 1200), (-99.33, 20.05, 1220), label='Mexica')],
      sites=[site('Coatepec', -99.4, 20.1, 1163, 'Where, in legend, Huitzilopochtli was born and fought his sister.')]),
    S(1250, 'c. 1250 to 1325', 'To the lake',
      'Arriving in the Valley of Mexico, the Mexica were despised newcomers, mercenaries for the city of Culhuacan, driven from '
      'Chapultepec. On a swampy island they found the eagle on the cactus.',
      moves=[mv('foot', (-99.33, 20.05, 1250), (-99.2, 19.7, 1270), (-99.19, 19.42, 1280), (-99.1, 19.33, 1300), (-99.13, 19.43, 1325), label='Mexica')],
      sites=[site('Tenochtitlan', -99.13, 19.43, 1325, 'Founded on an island in Lake Texcoco; today Mexico City.')]),
  ])

M('athabaskans-south', 'The Navajo and Apache go south', 'Navajo and Apache', 'folk', '#935116', 1300, 1525,
  'The Navajo and Apache speak Athabaskan languages, whose relatives are spoken in Alaska and north-western Canada. Some '
  'time between about 1300 and 1500 their ancestors made a journey of 3,000 km down the plains along the Rocky Mountains to '
  'the Southwest, where they became the neighbours of the Pueblo peoples.',
  rank=2, steps=[
    S(1300, 'c. 1300 to 1450', 'Down the Rockies',
      'Small bands of hunters with dog travois moved south along the eastern side of the mountains.',
      moves=[mv('foot', (-123.0, 62.0, 1300), (-118.0, 57.0, 1340), (-114.0, 52.5, 1380), (-110.0, 48.0, 1410), (-106.5, 43.0, 1440), label='Athabaskans')]),
    S(1450, 'c. 1450 to 1525', 'The Southwest',
      'By the early 1500s they were in the Southwest, when the Spanish first met "Apaches de Nabajo". The Navajo learned '
      'farming and weaving from the Pueblos, and later sheep-herding from the Spanish.',
      moves=[mv('foot', (-106.5, 43.0, 1450), (-106.0, 39.5, 1480), (-107.5, 36.5, 1510), label='Navajo'),
             mv('foot', (-106.0, 39.5, 1480), (-104.5, 35.5, 1510), (-105.5, 33.0, 1525), label='Apache')],
      sites=[site('Dinetah', -107.5, 36.6, 1500, 'The first homeland of the Navajo in the Southwest.')]),
  ])

M('fulani', 'The Fulani across the Sahel', 'Fulani', 'nomads', '#a6812c', 1000, 1810,
  'The Fulani, cattle herders of the Senegal valley, spread east across the whole Sahel over eight centuries, grazing their '
  'herds between farming peoples, from Senegal to Cameroon. Many became devout Muslim scholars; in the jihads of the 1700s '
  'and 1800s Fulani leaders founded states, the greatest the Sokoto Caliphate of Usman dan Fodio.',
  rank=2, steps=[
    S(1000, 'c. 1000 to 1500', 'East from Futa Toro',
      'Herding families moved east by stages along the band of grassland between the desert and the forest, to Macina on the '
      'inner Niger delta and on to Hausaland.',
      moves=[mv('foot', (-14.0, 16.2, 1000), (-11.0, 15.0, 1100), (-8.0, 14.5, 1200), (-4.5, 14.2, 1300), (-1.0, 13.5, 1380), (3.0, 13.0, 1430), (7.5, 12.5, 1500), label='Fulani')]),
    S(1500, '1500 to 1810', 'To Adamawa, and the jihad',
      'Fulani herders reached Bornu and Adamawa in Cameroon. In 1804 Usman dan Fodio proclaimed a jihad against the Hausa kings '
      'and founded the Sokoto Caliphate, the largest state in West Africa.',
      moves=[mv('foot', (7.5, 12.5, 1500), (10.5, 12.0, 1600), (12.5, 10.5, 1700), (13.4, 9.3, 1806), label='Fulani')],
      sites=[site('Sokoto', 5.24, 13.06, 1809, 'Capital of Usman dan Fodio\'s caliphate.')]),
  ])

M('nam-tien', 'The Vietnamese march south', 'Vietnamese', 'settlers', '#b03a2e', 1069, 1757,
  'For seven centuries the Vietnamese pushed south from the Red River delta along the narrow coast, the Nam tien, "march '
  'to the south". Soldier-farmers settled the lands of Champa and then of the Khmer, until Vietnam reached the Mekong delta '
  'and took the shape it has today.',
  rank=2, steps=[
    S(1069, '1069 to 1471', 'Taking Champa',
      'Vietnamese kings took Cham provinces in 1069 and 1306 (Hue came as a princess\'s dowry) and in 1471 Le Thanh Tong '
      'sacked Vijaya, the Cham capital.',
      moves=[mv('foot', (105.85, 21.03, 1069), (105.7, 19.8, 1100), (106.0, 18.0, 1200), (107.6, 16.45, 1306), (108.3, 15.0, 1400), (109.1, 13.9, 1471), label='Vietnamese')],
      sites=[site('Vijaya', 109.06, 13.93, 1471, 'Capital of Champa, sacked in 1471.')]),
    S(1611, '1611 to 1757', 'To the Mekong',
      'The Nguyen lords pushed on to the southern coast, then settled Prey Nokor, a Khmer port, which became Saigon in 1698. '
      'By 1757 they held the whole Mekong delta.',
      moves=[mv('foot', (109.1, 13.9, 1611), (109.2, 12.2, 1653), (108.1, 11.0, 1680), (106.7, 10.8, 1698), (105.8, 10.0, 1730), (105.1, 9.2, 1757), label='Vietnamese')],
      sites=[site('Saigon', 106.7, 10.78, 1698, 'The Khmer port of Prey Nokor, made a Vietnamese prefecture in 1698.')]),
  ])

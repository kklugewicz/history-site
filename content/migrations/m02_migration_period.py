"""The Migration Period (c. 150 to 700): the Germanic peoples, the Huns, the Slavs, Avars and Bulgars, and the Hijra."""
from _lib import M, S, mv, site

ROME = 'fall-of-western-rome'

M('goths-south', 'The Goths go south to the Black Sea', 'Goths', 'folk', '#8e5a2b', 150, 270,
  'Roman writers and the Goths\' own legends say they came from Scandza, Scandinavia, to the lower Vistula. Archaeology '
  'follows the Wielbark culture of the Vistula south-east to the Black Sea in the second and third centuries, where the '
  'Goths built a great realm on the steppe and the forest edge, and from there raided deep into the Roman Empire.',
  rank=2, steps=[
    S(150, 'c. 150 to 230', 'From the Vistula to the Black Sea',
      'Families with wagons and cattle moved up the Vistula and over to the Dnieper and the Dniester, settling among the '
      'peoples of the steppe edge. Their Chernyakhov culture of villages spread from Romania to Ukraine.',
      moves=[mv('wagon', (18.8, 53.6, 150), (21.0, 52.2, 170), (24.0, 51.0, 190), (27.0, 50.0, 205), (30.0, 48.5, 220), (32.0, 47.0, 230), label='Goths')],
      sites=[site('Wielbark', 19.13, 53.94, 150, 'The Gothic homeland on the lower Vistula, in archaeology.')]),
    S(238, '238 to 270', 'Raiders of the empire',
      'Goths crossed the Danube and killed Emperor Decius at Abritus in 251, the first emperor to die fighting a foreign foe. '
      'By ship they raided the Aegean and sacked Athens in 267, until Claudius II beat them at Naissus in 268.',
      moves=[mv('wagon', (29.0, 46.5, 238), (28.0, 45.0, 245), (26.8, 43.5, 251), label='Goths'),
             mv('galley', (31.5, 46.4, 267), (30.0, 44.0, 267), (29.2, 41.4, 267), (29.05, 41.1, 267), (28.0, 40.8, 267), (26.7, 40.4, 267), (26.2, 40.05, 267), (25.0, 39.5, 267), (24.0, 38.0, 267), (23.6, 37.9, 267), label='Goths and Heruli')],
      sites=[site('Abritus', 26.83, 43.53, 251, 'Emperor Decius dies in battle against the Goths.'),
             site('Naissus', 21.9, 43.32, 268, 'Claudius II beats the Goths: they called him Gothicus.')]),
  ])

M('huns', 'The Huns', 'Huns', 'nomads', '#6e2c00', 350, 469,
  'About 370 a people of mounted archers from the steppe of Central Asia crossed the Volga, conquered the Alans and smashed '
  'the Gothic kingdoms north of the Black Sea, setting off the great migrations into the Roman Empire. Under Attila, from '
  '434, the Huns ruled from the Rhine to the Caspian. After his death in 453 their empire broke apart within a year.',
  rank=1, war=ROME, steps=[
    S(350, 'c. 350 to 376', 'Out of the steppe',
      'Where the Huns came from is still argued; many think they had among their ancestors the Xiongnu who once fought China. '
      'They fell on the Alans by the Don and then on the Greuthungi Goths, whose old king Ermanaric took his own life.',
      moves=[mv('horse', (62.0, 48.5, 350), (52.0, 48.5, 365), (46.0, 48.0, 370), (40.0, 47.5, 372), (34.0, 47.0, 375), (29.5, 47.0, 376), label='Huns')]),
    S(400, '400 to 434', 'Masters of the Danube',
      'The Huns moved their camp to the Hungarian plain, ruling Goths, Gepids, Alans and others, raiding the Balkans and '
      'taking huge payments of gold from Constantinople.',
      moves=[mv('horse', (29.5, 47.0, 395), (26.0, 46.5, 400), (22.5, 46.8, 410), (19.8, 47.0, 420), label='Huns')],
      sites=[site('Attila\'s camp', 20.2, 47.2, 434, 'A town of timber halls on the Hungarian plain, described by the envoy Priscus.')]),
    S(441, '441 to 452', 'Attila',
      'Attila ravaged the Balkans, then in 451 rode west into Gaul with Germanic allies and was stopped by Aetius\'s Romans '
      'and Visigoths on the Catalaunian Plains. In 452 he invaded Italy, sacked Aquileia, and turned back after meeting Pope Leo.',
      moves=[mv('horse', (19.8, 47.0, 441), (21.9, 43.3, 443), (25.0, 42.5, 447), (23.3, 42.7, 447), (19.8, 47.0, 449), label='Attila'),
             mv('horse', (19.8, 47.0, 451), (15.0, 48.2, 451), (10.5, 48.8, 451), (7.0, 49.5, 451), (4.4, 48.9, 451), label='Attila in Gaul'),
             mv('horse', (19.8, 47.0, 452), (15.5, 46.3, 452), (13.37, 45.77, 452), (11.0, 45.3, 452), (10.4, 45.1, 452), label='Attila in Italy')],
      sites=[site('Catalaunian Plains', 4.4, 48.9, 451, 'Aetius, Theodoric of the Visigoths and their allies halt Attila.'),
             site('Aquileia', 13.37, 45.77, 452, 'Sacked so thoroughly that refugees fled to the lagoons where Venice would grow.')]),
    S(453, '453 to 469', 'The end of the Huns',
      'Attila died on his wedding night in 453. His sons quarrelled, the subject peoples rose and beat them at the Nedao in '
      '454, and the Huns went back east to the steppe, where they vanish from history after 469.',
      moves=[mv('horse', (19.8, 47.0, 454), (24.0, 46.0, 458), (29.0, 46.5, 463), (35.0, 47.0, 469), label='Huns')],
      sites=[site('Nedao', 19.5, 46.0, 454, 'Gepids, Ostrogoths and others break the power of Attila\'s sons.')]),
  ])

M('visigoths', 'The Visigoths', 'Visigoths', 'folk', '#c0762b', 376, 418,
  'Fleeing the Huns, tens of thousands of Goths begged to be let into the Roman Empire in 376. Cheated and starved by Roman '
  'officials, they rose up, destroyed an emperor\'s army at Adrianople, and spent forty years on the move inside the '
  'empire. Under Alaric they sacked Rome in 410, the first time in 800 years the city fell to a foreign enemy, and in 418 '
  'they were given land in Aquitaine, where their kingdom of Toulouse began.',
  numbers='About 100,000 people, a fifth of them warriors', rank=1, war=ROME, steps=[
    S(376, '376 to 382', 'Across the Danube',
      'The Romans ferried the Goths over the Danube but sold them dogs to eat in exchange for their children. The Goths '
      'revolted, and on 9 August 378 at Adrianople they killed Emperor Valens and two thirds of his army. In 382 they were '
      'settled in the Balkans as allies.',
      moves=[mv('wagon', (28.0, 45.6, 376), (27.3, 44.1, 376), (26.6, 43.0, 377), (26.56, 41.68, 378), (25.5, 42.6, 380), (25.0, 43.2, 382), label='Goths')],
      sites=[site('Adrianople', 26.56, 41.68, 378, 'Emperor Valens and his army are destroyed by the Goths.')]),
    S(395, '395 to 408', 'Alaric',
      'Alaric, chosen king, led his people through Greece in 395 to 397 and then into Italy, looking for land and a Roman '
      'command. Stilicho beat him back at Pollentia in 402, but when Stilicho was murdered in 408 nothing stood in Alaric\'s way.',
      moves=[mv('wagon', (25.0, 43.2, 395), (22.9, 40.6, 395), (22.4, 39.0, 396), (22.9, 37.9, 396), (21.5, 38.3, 397), (20.8, 39.7, 398),
                (19.5, 41.8, 400), (16.0, 45.5, 401), (13.4, 45.8, 401), (11.0, 45.4, 402), (7.96, 44.69, 402), label='Alaric\'s Goths')],
      sites=[site('Pollentia', 7.96, 44.69, 402, 'Stilicho stops Alaric\'s first invasion of Italy.')]),
    S(408, '408 to 412', 'The sack of Rome',
      'After three sieges Alaric\'s Goths broke into Rome on 24 August 410 and plundered it for three days. The shock ran '
      'through the Roman world; Augustine wrote The City of God in answer. Alaric died weeks later in Calabria, buried in a '
      'riverbed with his treasure.',
      moves=[mv('wagon', (13.4, 45.8, 408), (12.2, 44.4, 408), (12.5, 43.0, 408), (12.48, 41.9, 410), (14.5, 41.0, 410), (16.25, 39.3, 410),
                (14.5, 41.0, 411), (12.48, 41.9, 411), (10.0, 43.8, 412), (7.5, 44.0, 412), label='Visigoths')],
      sites=[site('Rome', 12.48, 41.9, 410, 'Sacked by Alaric\'s Goths on 24 August 410.'),
             site('Cosenza', 16.25, 39.3, 410, 'Alaric dies; his men divert the river Busento to bury him.')]),
    S(412, '412 to 418', 'A kingdom in Gaul',
      'Under Athaulf, who married the emperor\'s sister Galla Placidia, the Goths moved into southern Gaul and Spain. In 418 '
      'Rome settled them in Aquitaine as allies. Their kingdom of Toulouse later moved to Spain, ruling it from Toledo until 711.',
      moves=[mv('wagon', (7.5, 44.0, 412), (5.4, 43.5, 413), (3.0, 43.18, 413), (2.17, 41.39, 415), (3.0, 43.18, 416), (1.44, 43.6, 418), label='Visigoths')],
      sites=[site('Toulouse', 1.44, 43.6, 418, 'Capital of the Visigothic kingdom until 507.')]),
  ])

M('rhine-crossing', 'Vandals, Alans and Suebi', 'Vandals', 'folk', '#7b241c', 401, 455,
  'On the last day of 406, a host of Vandals, Alans and Suebi crossed the Rhine, perhaps over the frozen river near '
  'Mainz, and ravaged Gaul. Three years later they crossed into Spain. The Vandals went on to Africa in 429 and took '
  'Carthage in 439, the richest city of the West, and from there sacked Rome in 455, so thoroughly that "vandalism" '
  'bears their name.',
  numbers='About 80,000 Vandals and Alans crossed to Africa', rank=1, war=ROME, steps=[
    S(401, '401 to 406', 'The crossing of the Rhine',
      'Driven west by the Huns, the peoples gathered on the middle Rhine. On 31 December 406 they broke through the Frankish '
      'allies guarding the frontier and poured into Gaul. The Burgundians followed and settled around Worms.',
      moves=[mv('wagon', (17.0, 50.5, 401), (13.5, 50.3, 404), (10.0, 50.0, 406), (8.27, 50.0, 406), label='Vandals and Alans'),
             mv('wagon', (16.5, 47.8, 401), (12.5, 48.6, 404), (8.27, 50.0, 406), label='Suebi'),
             mv('wagon', (15.0, 52.5, 406), (11.0, 51.0, 409), (8.36, 49.63, 413), label='Burgundians')],
      sites=[site('Mainz', 8.27, 50.0, 406, 'The Rhine frontier breaks on the last day of 406.'),
             site('Worms', 8.36, 49.63, 413, 'The Burgundian kingdom of the Nibelungenlied, destroyed by Aetius\'s Huns in 436.')]),
    S(407, '407 to 409', 'Through Gaul to Spain',
      'For two years the host plundered Gaul: Reims, Trier, Arras, Tours, down to the Pyrenees. In autumn 409 they crossed into '
      'Spain and shared it out: the Suebi took Galicia, the Alans Lusitania, the Vandals the south.',
      moves=[mv('wagon', (8.27, 50.0, 407), (4.0, 49.3, 407), (2.8, 50.3, 407), (0.7, 47.4, 408), (0.0, 44.5, 409), (-1.5, 43.2, 409), label='Vandals and Alans'),
             mv('wagon', (-1.5, 43.2, 409), (-4.5, 42.5, 410), (-8.43, 41.55, 411), label='Suebi'),
             mv('wagon', (-1.5, 43.2, 409), (-4.0, 41.0, 410), (-5.0, 39.0, 411), (-5.9, 37.4, 412), label='Vandals')],
      sites=[site('Braga', -8.43, 41.55, 411, 'Capital of the Suebi kingdom in Galicia, which lasted until 585.')]),
    S(429, '429 to 439', 'To Africa',
      'In May 429 King Gaiseric ferried his whole people, 80,000 strong, across the Strait of Gibraltar and marched east along '
      'the coast. They besieged Hippo, where St Augustine died in 430, and in 439 took Carthage by surprise.',
      moves=[mv('sail', (-5.6, 36.1, 429), (-5.6, 35.95, 429), (-5.8, 35.75, 429), label='Vandals'),
             mv('wagon', (-5.8, 35.75, 429), (-3.0, 35.0, 429), (0.0, 35.6, 430), (3.0, 36.6, 430), (7.75, 36.88, 430), (9.0, 36.8, 437), (10.32, 36.85, 439), label='Vandals')],
      sites=[site('Hippo Regius', 7.75, 36.88, 430, 'St Augustine dies during the Vandal siege.'),
             site('Carthage', 10.32, 36.85, 439, 'Taken by Gaiseric: capital of the Vandal kingdom until 533.')]),
    S(455, '455', 'The sack of Rome',
      'With Africa\'s grain and a fleet, the Vandals ruled the western Mediterranean. In June 455 Gaiseric sailed to Rome and '
      'plundered it for two weeks, taking the empress and the treasures of the Temple of Jerusalem back to Carthage.',
      moves=[mv('sail', (10.32, 36.95, 455), (11.2, 38.8, 455), (12.0, 40.8, 455), (12.25, 41.7, 455), label='Gaiseric\'s fleet')],
      sites=[site('Rome', 12.48, 41.9, 455, 'Two weeks of plunder by the Vandals.')]),
  ])

M('ostrogoths', 'The Ostrogoths', 'Ostrogoths', 'folk', '#a04000', 454, 493,
  'The Ostrogoths lived under the Huns until they won their freedom at the Nedao in 454. Settled in Pannonia and then the '
  'Balkans, they were a danger on Constantinople\'s doorstep, until Emperor Zeno sent their king Theodoric to take Italy '
  'from Odoacer. After four years of war Theodoric ruled Italy from Ravenna, and his kingdom was the most Roman of them all.',
  rank=1, war=ROME, steps=[
    S(454, '454 to 488', 'Free of the Huns',
      'The Ostrogoths settled in Pannonia, then moved into the Balkans in 473, now allies, now enemies of the eastern emperor. '
      'Their young king Theodoric had grown up a hostage in Constantinople.',
      moves=[mv('wagon', (18.5, 46.5, 454), (19.5, 45.0, 470), (21.9, 43.3, 473), (23.5, 42.0, 476), (25.4, 43.6, 483), label='Ostrogoths')],
      sites=[site('Novae', 25.4, 43.62, 483, 'Theodoric\'s base on the Danube.')]),
    S(488, '488 to 493', 'Theodoric takes Italy',
      'In the autumn of 488 the whole people, perhaps 100,000, set out with their wagons for Italy. They beat Odoacer on the '
      'Isonzo and at Verona in 489, besieged him in Ravenna for three years and, in 493, Theodoric killed him with his own hand '
      'at a banquet.',
      moves=[mv('wagon', (25.4, 43.6, 488), (21.9, 43.3, 488), (19.5, 45.0, 488), (16.5, 46.0, 489), (13.6, 45.9, 489),
                (11.0, 45.44, 489), (11.9, 44.9, 490), (12.2, 44.42, 493), label='Theodoric\'s Goths')],
      sites=[site('Ravenna', 12.2, 44.42, 493, 'Theodoric\'s capital; his mausoleum and churches still stand.'),
             site('Verona', 10.99, 45.44, 489, 'Theodoric beats Odoacer: the "Dietrich of Bern" of German legend.')]),
  ])

M('franks', 'The Franks take Gaul', 'Franks', 'folk', '#1f618d', 358, 511,
  'The Franks were a league of Germanic peoples on the lower Rhine. Rome let the Salian Franks settle in Toxandria in 358 as '
  'allies; as Roman power faded they spread south over northern Gaul. Clovis, king from 481, beat the last Roman ruler at '
  'Soissons, the Alemanni and the Visigoths, became a Catholic Christian, and made Paris the capital of the kingdom that '
  'gave France its name.',
  rank=1, war=ROME, steps=[
    S(358, '358 to 460', 'Over the lower Rhine',
      'The Franks moved slowly, farming families more than a marching army, from the Rhine mouths into today\'s Belgium. '
      'Childeric, Clovis\'s father, ruled from Tournai, where his grave was found full of gold bees.',
      moves=[mv('wagon', (6.0, 51.9, 358), (5.2, 51.4, 380), (4.4, 51.0, 420), (3.39, 50.6, 460), label='Salian Franks')],
      sites=[site('Tournai', 3.39, 50.6, 481, 'Childeric\'s capital and grave.')]),
    S(486, '486 to 511', 'Clovis',
      'Clovis took Soissons from Syagrius in 486, was baptised at Reims, beat the Visigoths at Vouille in 507 and drove them '
      'into Spain. He made Paris his capital; by his death in 511 the Franks held almost all of Gaul.',
      moves=[mv('wagon', (3.39, 50.6, 486), (3.32, 49.38, 486), (2.35, 48.86, 490), (1.0, 47.5, 507), (0.16, 46.64, 507), (1.44, 43.6, 508), label='Clovis\'s Franks')],
      sites=[site('Soissons', 3.32, 49.38, 486, 'Clovis ends the last Roman state in Gaul.'),
             site('Vouille', 0.16, 46.64, 507, 'Clovis kills Alaric II and takes Aquitaine from the Visigoths.')]),
  ])

M('anglo-saxons', 'Angles, Saxons and Jutes', 'Anglo-Saxons', 'seafarers', '#7d6608', 430, 600,
  'When Rome left Britain in 410, the Britons hired Saxon soldiers, says Gildas, and the soldiers sent for their kin. Over '
  'the fifth and sixth centuries Angles from Schleswig, Saxons from the North Sea coast and Jutes from Jutland settled '
  'eastern Britain, and their language became English. Britons fought back, the battle of Mount Badon is remembered as a '
  'victory, and some sailed to Armorica, which became Brittany.',
  rank=1, steps=[
    S(430, 'c. 430 to 500', 'Over the North Sea',
      'Small boats like the Nydam ship, rowed, not sailed, carried warriors and then families. They settled Kent, East '
      'Anglia, the Thames valley and Lindsey; their cemeteries show the same brooches and pots as at home.',
      moves=[mv('longship', (8.4, 54.6, 440), (7.0, 54.6, 445), (4.5, 53.8, 450), (2.5, 53.0, 455), (1.85, 52.6, 460), label='Angles'),
             mv('longship', (8.4, 53.8, 450), (6.0, 53.7, 455), (3.5, 52.6, 460), (2.0, 51.5, 465), (1.5, 51.4, 470), label='Saxons and Jutes')],
      sites=[site('Sutton Hoo', 1.34, 52.09, 600, 'Later royal ship burial of the East Angles, about 625.'),
             site('Ebbsfleet', 1.33, 51.33, 449, 'Where Hengist and Horsa are said to have landed in 449.')]),
    S(500, 'c. 500 to 600', 'Westward through Britain',
      'After a pause, perhaps after Mount Badon, the English pushed west in the later sixth century, to the Severn and up to '
      'Northumbria. Britons kept Wales, Cornwall and the north-west, and many crossed the sea to Brittany.',
      moves=[mv('foot', (1.0, 51.5, 500), (-0.5, 51.4, 530), (-1.5, 51.2, 552), (-2.2, 51.6, 577), label='Saxons'),
             mv('foot', (0.5, 53.3, 520), (-1.0, 54.0, 550), (-1.6, 55.0, 590), label='Angles'),
             mv('sail', (-4.5, 50.3, 460), (-4.3, 49.6, 470), (-3.6, 48.9, 480), label='Britons to Brittany')],
      sites=[site('Dyrham', -2.37, 51.48, 577, 'The West Saxons cut off the Britons of Wales from those of Cornwall.')]),
  ])

M('lombards', 'The Lombards', 'Lombards', 'folk', '#117864', 489, 572,
  'The Lombards, the "long beards", moved from the middle Danube into Pannonia in the sixth century. In 568, after '
  'destroying the Gepids with the Avars, King Alboin led his whole people, with Saxons and others, into an Italy worn out '
  'by Justinian\'s wars and plague. They took the north and much of the south; Lombardy still bears their name.',
  rank=1, steps=[
    S(489, '489 to 567', 'To Pannonia',
      'The Lombards moved into the lands north of the Danube left empty by the Rugii, then in 526 into Pannonia. Allied with '
      'the Avars, they destroyed the Gepids in 567; Alboin made a drinking cup of the Gepid king\'s skull.',
      moves=[mv('wagon', (16.0, 49.0, 489), (17.0, 48.2, 505), (18.0, 47.0, 526), (19.0, 46.0, 560), label='Lombards')]),
    S(568, '568 to 572', 'Into Italy',
      'At Easter 568 they left Pannonia to the Avars and crossed the Julian Alps. Cividale fell first, then Milan in 569; '
      'Pavia held out for three years and became their capital.',
      moves=[mv('wagon', (19.0, 46.0, 568), (15.5, 46.0, 568), (13.43, 46.09, 568), (12.0, 45.6, 569), (9.19, 45.46, 569), (9.16, 45.19, 572), label='Alboin\'s Lombards'),
             mv('wagon', (12.0, 45.6, 570), (12.5, 43.5, 571), (14.0, 42.0, 572), (14.78, 41.13, 572), label='To Spoleto and Benevento')],
      sites=[site('Pavia', 9.16, 45.19, 572, 'Lombard capital until Charlemagne took it in 774.')]),
  ])

M('slavs', 'The Slavic migrations', 'Slavs', 'folk', '#2471a3', 500, 700,
  'In the sixth and seventh centuries Slavic peoples spread from a homeland between the Vistula and the Dnieper over half of '
  'Europe: west to the Elbe, south over the Danube deep into the Balkans and Greece, and north into the forests toward '
  'Novgorod. Simple farming villages of sunken houses mark their spread. They are the ancestors of today\'s Poles, Czechs, '
  'Serbs, Croats, Bulgarians, Russians and Ukrainians.',
  rank=1, steps=[
    S(500, 'c. 500 to 600', 'West to the Elbe',
      'As the Germanic peoples left for the empire, Slavs settled their old lands, reaching Bohemia and the Elbe by about 600.',
      moves=[mv('foot', (26.0, 51.0, 500), (22.0, 51.0, 530), (18.5, 50.8, 560), (14.4, 50.1, 580), (12.0, 51.5, 600), label='West Slavs')],
      sites=[site('Prague-Korchak', 26.0, 51.0, 500, 'The early Slavic culture of simple villages and plain pots.')]),
    S(550, 'c. 550 to 630', 'Over the Danube',
      'Slav raiders crossed the Danube from the 540s, and then settled in the Balkans as the Avars broke the Roman frontier. '
      'They reached the Peloponnese; Croats and Serbs arrived in the 620s.',
      moves=[mv('foot', (26.0, 47.0, 550), (25.0, 44.5, 570), (23.0, 42.5, 585), (22.5, 40.5, 590), (22.2, 37.5, 620), label='South Slavs'),
             mv('foot', (19.0, 49.0, 610), (17.5, 46.5, 620), (16.4, 44.0, 630), label='Croats'),
             mv('foot', (20.0, 50.0, 610), (21.0, 46.5, 620), (20.5, 43.5, 630), label='Serbs')]),
    S(600, 'c. 600 to 700', 'North into the forests',
      'Eastern Slavs moved north up the rivers into the lands of the Finnic and Baltic peoples, reaching Lake Ilmen, where '
      'Novgorod would rise.',
      moves=[mv('foot', (30.5, 50.5, 600), (31.0, 53.0, 630), (31.0, 56.0, 660), (31.3, 58.5, 700), label='East Slavs')]),
  ])

M('avars', 'The Avars', 'Avars', 'nomads', '#6c3483', 555, 568,
  'The Avars were horsemen from the steppe, perhaps the remnant of the Rouran khaganate of Mongolia, destroyed by the Turks '
  'in 552. Fleeing west, they reached the Caucasus in 557, took Roman gold to fight Rome\'s enemies, and in 568 seized the '
  'Hungarian plain. For 230 years their khagans ruled the Slavs and raided the empire, until Charlemagne broke them.',
  rank=2, steps=[
    S(555, '555 to 562', 'Fleeing the Turks',
      'The Avars rode across the steppe to the north Caucasus and sent envoys to Justinian, who paid them to fight other '
      'nomads. The Turks complained the Avars were their runaway slaves.',
      moves=[mv('horse', (60.0, 49.0, 555), (50.0, 47.5, 557), (44.0, 45.0, 558), (36.0, 46.5, 560), (29.0, 46.0, 562), label='Avars')]),
    S(567, '567 to 568', 'Into Pannonia',
      'With the Lombards they destroyed the Gepids in 567; the next year the Lombards left for Italy and the Avars took the '
      'whole Carpathian basin.',
      moves=[mv('horse', (29.0, 46.0, 567), (25.0, 46.5, 567), (21.5, 47.0, 568), (19.5, 47.2, 568), label='Avars')],
      sites=[site('Avar ring', 19.5, 47.0, 568, 'The khagans\' great camp, plundered by Charlemagne\'s Franks in 796.')]),
  ])

M('hijra', 'The Hijra', 'Muhammad\'s followers', 'exiles', '#1d8348', 615, 622,
  'Persecuted in Mecca, some of the first Muslims crossed the Red Sea to the Christian king of Aksum in 615. In 622 '
  'Muhammad and his followers left Mecca for Yathrib, which became Medina, "the city of the Prophet". This migration, the '
  'Hijra, is the start of the Islamic calendar.',
  rank=2, steps=[
    S(615, '615', 'Refuge in Aksum',
      'About eighty Muslims crossed to Ethiopia, where the Negus refused to hand them back to Mecca.',
      moves=[mv('sail', (39.1, 21.5, 615), (39.0, 19.5, 615), (39.2, 16.5, 615), (39.4, 15.6, 615), label='First emigrants'),
             mv('foot', (39.4, 15.6, 615), (38.72, 14.13, 615), label='To Aksum')],
      sites=[site('Aksum', 38.72, 14.13, 615, 'The Christian kingdom that gave the first Muslims refuge.')]),
    S(622, '622', 'From Mecca to Medina',
      'Muhammad and Abu Bakr slipped out of Mecca, hid three days in a cave on Mount Thawr, and reached Yathrib about 400 km '
      'to the north. There the first Muslim community was formed.',
      moves=[mv('foot', (39.83, 21.42, 622), (39.85, 21.38, 622), (39.3, 22.4, 622), (39.1, 23.6, 622), (39.61, 24.47, 622), label='Muhammad')],
      sites=[site('Mecca', 39.83, 21.42, 622, 'Muhammad leaves his home city.'),
             site('Medina', 39.61, 24.47, 622, 'The first Muslim community; Muhammad\'s mosque and tomb.')]),
  ])

M('bulgars', 'The Bulgars', 'Bulgars', 'nomads', '#148f77', 632, 700,
  'The Bulgars were Turkic horsemen of the steppe north of the Black Sea. When the Khazars broke their "Old Great Bulgaria" '
  'after Khan Kubrat died, his sons led their people in different directions. Asparukh crossed the Danube and founded a '
  'Bulgarian state in 681; his people mixed with the Slavs there and took their language. Another branch went north to the '
  'Volga.',
  rank=2, steps=[
    S(632, '632 to 668', 'Old Great Bulgaria',
      'Kubrat freed the Bulgars from the Avars and ruled the steppe east of the Sea of Azov. After his death the Khazars '
      'pressed in from the east.',
      moves=[mv('horse', (45.0, 46.0, 632), (40.0, 46.0, 640), (38.0, 46.5, 650), label='Bulgars')],
      sites=[site('Phanagoria', 36.78, 45.28, 650, 'Kubrat\'s capital on the Taman peninsula.')]),
    S(670, '670 to 700', 'Asparukh and the Danube',
      'Asparukh led his horde west to the Danube delta and, after beating a Byzantine army in 680, crossed into today\'s '
      'Bulgaria. Byzantium recognised his state in 681. Kotrag\'s Bulgars went north and founded Volga Bulgaria.',
      moves=[mv('horse', (38.0, 46.5, 670), (33.0, 46.8, 672), (29.0, 45.5, 678), (28.5, 44.5, 680), (27.13, 43.38, 681), label='Asparukh\'s Bulgars'),
             mv('horse', (40.0, 47.5, 670), (44.0, 50.5, 680), (47.5, 53.0, 690), (49.1, 54.98, 700), label='Volga Bulgars')],
      sites=[site('Pliska', 27.13, 43.38, 681, 'First capital of the Bulgarian state.')]),
  ])

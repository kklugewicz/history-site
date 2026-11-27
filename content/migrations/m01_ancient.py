"""Migrations before the Common Era: the first farmers, the steppe herders, the Bantu, the Austronesians, the Sea Peoples,
the colonists of the Mediterranean, Celts, Cimbri and Yuezhi."""
from _lib import M, S, mv, site

M('first-farmers', 'The first farmers reach Europe', 'First farmers', 'folk', '#7a8a2e', -7000, -3800,
  'Farming began in the Fertile Crescent, and from about 7000 BC farmers from Anatolia carried wheat, barley, sheep, goats and '
  'pottery into Europe, family by family and generation by generation. Ancient DNA shows they were newcomers, not locals '
  'copying a new idea: they mixed with the hunter-gatherers they met but largely replaced them. By 4000 BC fields reached '
  'from Greece to Britain and Scandinavia.',
  numbers='A few kilometres a generation, for three thousand years', rank=1, steps=[
    S(-7000, 'c. 7000 BC', 'Out of Anatolia',
      'Villages like Catalhoyuk in central Anatolia had farmed for two thousand years. Their people spread west to the Aegean '
      'coast and crossed into Greece, where the first farming villages of Europe appear in Thessaly about 6500 BC.',
      moves=[mv('foot', (32.8, 37.7, -7000), (30.5, 38.8, -6800), (27.3, 39.6, -6650), (22.4, 39.6, -6400), label='First farmers')],
      sites=[site('Catalhoyuk', 32.83, 37.67, -7000, 'A town of mud-brick houses entered through the roof, home to thousands of early farmers.'),
             site('Sesklo', 22.83, 39.36, -6400, 'One of the first farming villages in Europe.')]),
    S(-6200, 'c. 6200 to 5000 BC', 'Up the Danube',
      'One stream followed the rivers north. Farmers of the Starcevo culture filled the Balkans; the Linear Pottery people '
      'then raced across the loess soils of central Europe in a few centuries, building longhouses from Hungary to the Paris basin.',
      moves=[mv('foot', (22.4, 39.6, -6200), (21.4, 42.0, -6000), (20.5, 44.8, -5800), (18.9, 46.9, -5600), (16.4, 48.2, -5500),
                (13.0, 50.2, -5350), (9.5, 50.3, -5250), (6.3, 50.6, -5150), (3.0, 49.3, -5000), label='Linear Pottery farmers')],
      sites=[site('Linear Pottery longhouses', 13.0, 50.2, -5350, 'Timber longhouses up to 40 metres long, the first villages of central Europe.')]),
    S(-6000, 'c. 6000 to 5400 BC', 'Along the Mediterranean shore',
      'Another stream went by boat, hopping along the coasts of the Adriatic, Italy, southern France and Spain. Archaeologists '
      'follow them by their pots, decorated with the edge of a cockle shell.',
      moves=[mv('galley', (21.3, 37.6, -6000), (19.8, 39.0, -5950), (18.7, 39.6, -5920), (17.6, 38.9, -5880), (16.3, 37.6, -5850),
                (15.1, 36.5, -5830), (13.0, 36.8, -5800), (11.8, 37.8, -5780), (11.5, 40.0, -5740), (9.9, 43.6, -5700), (7.0, 43.2, -5650),
                (5.5, 42.9, -5620), (4.6, 43.25, -5600), (3.4, 42.3, -5550), (3.4, 41.6, -5520), (1.5, 40.7, -5480), (0.5, 40.4, -5450), label='Cardial ware farmers')]),
    S(-4500, 'c. 4500 to 3800 BC', 'To Britain and the north',
      'After a long pause on the edge of the North European Plain, farming crossed the Channel to Britain and Ireland about '
      '4000 BC, and reached southern Scandinavia. Within a few centuries the first great stone monuments rose along the Atlantic.',
      moves=[mv('foot', (3.0, 49.3, -4500), (1.6, 50.6, -4100), label='First farmers'),
             mv('sail', (1.6, 50.6, -4100), (0.3, 50.6, -4050), (-1.5, 50.6, -4000), label='To Britain'),
             mv('foot', (9.5, 52.4, -4300), (9.6, 55.2, -4000), (13.2, 55.7, -3900), label='To Scandinavia')],
      sites=[site('Carnac', -3.08, 47.58, -4500, 'Thousands of standing stones raised by the first farmers of Brittany.')]),
  ])

M('indo-europeans', 'The steppe herders (Indo-Europeans)', 'Steppe herders', 'nomads', '#a0522d', -3300, -1400,
  'From about 3300 BC herders of the Pontic steppe, the Yamnaya, took to wagons and horses and spread east and west. Their '
  'descendants carried Indo-European languages from Ireland to India: the ancestors of English, Latin, Greek, Russian, '
  'Persian and Sanskrit. Ancient DNA shows a huge movement of people into Europe about 2800 BC, and into South Asia after '
  '2000 BC, mixing with the farmers already there.',
  numbers='Ancestors of nearly half the world\'s languages', rank=1, steps=[
    S(-3300, 'c. 3300 to 3000 BC', 'The Yamnaya',
      'On the grasslands north of the Black Sea, herders with ox-drawn wagons and horses could live on the move. Their '
      'kurgans, burial mounds, run from the Danube to the Urals, and one branch went 2,000 km east to the Altai mountains.',
      moves=[mv('wagon', (40.0, 48.0, -3300), (58.0, 50.5, -3200), (73.0, 51.0, -3100), (86.5, 51.0, -3000), label='Afanasievo')],
      sites=[site('Yamnaya kurgans', 40.0, 48.0, -3300, 'Burial mounds of the steppe herders, with wagons buried beside the dead.')]),
    S(-3000, 'c. 3000 to 2400 BC', 'Into Europe',
      'Steppe people pushed up the Danube and across the plains north of the Carpathians. In central Europe they became the '
      'Corded Ware culture; within a few centuries most of the ancestry of northern Europeans came from the steppe. The Bell '
      'Beaker people carried it on to Britain.',
      moves=[mv('wagon', (40.0, 48.0, -3000), (33.0, 47.0, -2950), (28.5, 45.5, -2900), (22.0, 46.8, -2800), (19.0, 47.3, -2750), label='Yamnaya'),
             mv('wagon', (33.0, 47.0, -2950), (26.5, 49.7, -2900), (20.0, 51.5, -2800), (13.0, 52.0, -2700), (10.0, 55.5, -2600), label='Corded Ware'),
             mv('foot', (13.0, 52.0, -2600), (7.0, 51.0, -2550), (3.0, 50.5, -2500), (-1.8, 51.2, -2450), label='Bell Beakers')],
      sites=[site('Amesbury Archer', -1.78, 51.17, -2350, 'A man born in the Alps and buried near Stonehenge with the richest Beaker grave in Britain.')]),
    S(-2300, 'c. 2300 to 1900 BC', 'Anatolia and the Tarim',
      'Other speakers reached Anatolia, where the Hittites would write the oldest Indo-European texts, and the ancestors of the '
      'Tocharians settled the oases of the Tarim basin, where their mummies, in woollen tartans, still lie in the desert.',
      moves=[mv('foot', (28.0, 44.0, -2300), (29.0, 41.1, -2200), (32.0, 40.2, -2100), (34.6, 40.0, -2000), label='Hittites'),
             mv('wagon', (86.5, 49.0, -2100), (87.0, 45.0, -2000), (88.0, 41.5, -1900), label='Tocharians')],
      sites=[site('Hattusa', 34.61, 40.02, -1650, 'Capital of the Hittites, whose tablets are the oldest written Indo-European.'),
             site('Xiaohe cemetery', 88.4, 40.3, -1900, 'Mummies of the Tarim basin, buried under boat-shaped coffins.')]),
    S(-2100, 'c. 2100 to 1700 BC', 'The chariot people of the Urals',
      'East of the Urals the Sintashta people built fortified towns and the first spoked-wheel chariots. Their successors, the '
      'Andronovo herders, spread across the steppe of Kazakhstan to the edge of the Bactrian oases.',
      moves=[mv('wagon', (45.0, 49.0, -2100), (52.0, 51.5, -2050), (59.6, 52.6, -2000), (66.0, 50.5, -1900), (70.0, 46.5, -1800),
                (66.0, 40.5, -1750), (64.0, 37.8, -1700), label='Indo-Iranians')],
      sites=[site('Sintashta', 61.6, 52.48, -2000, 'Fortified town where the oldest spoked-wheel chariots were buried.')]),
    S(-1700, 'c. 1700 to 1400 BC', 'Into Iran and India',
      'Indo-Iranian speakers moved south through Bactria. One branch became the Iranian peoples; another, the Indo-Aryans, '
      'crossed the Hindu Kush into the Punjab, where the Rigveda was composed in Sanskrit. Indo-Aryan names even appear among '
      'the kings of Mitanni in Syria.',
      moves=[mv('horse', (64.0, 37.8, -1700), (68.0, 36.0, -1650), (71.5, 34.8, -1600), (73.5, 33.0, -1550), (75.5, 31.0, -1500),
                (77.5, 29.8, -1450), label='Indo-Aryans'),
             mv('horse', (64.0, 37.8, -1700), (59.6, 36.3, -1650), (54.0, 35.5, -1600), (48.5, 34.8, -1550), (41.0, 36.8, -1500), label='To Iran and Mitanni')]),
  ])

M('bantu', 'The Bantu expansion', 'Bantu speakers', 'folk', '#b9770e', -2000, 500,
  'From the grasslands of Cameroon, farmers speaking Bantu languages spread over most of Africa south of the equator in '
  'about two thousand years, through the rainforest and around it, learning to work iron on the way. It was one of the '
  'largest movements of people in history: today some 350 million people speak over 500 Bantu languages, from Swahili '
  'and Kikongo to Zulu and Xhosa.',
  numbers='Today 350 million speakers of 500 languages', rank=1, steps=[
    S(-2000, 'c. 2000 to 1000 BC', 'From the Cameroon grasslands',
      'The first Bantu farmers grew yams and oil palms and fished the rivers. They moved south into the equatorial forest, '
      'along the rivers and the coast, settling clearings for a few generations and then moving on.',
      moves=[mv('foot', (10.5, 6.0, -2000), (10.8, 3.5, -1700), (11.8, 1.0, -1500), (13.5, -1.0, -1300), (14.8, -3.5, -1100),
                (14.5, -5.5, -1000), label='Bantu farmers')],
      sites=[site('Cameroon grasslands', 10.5, 6.0, -2000, 'The homeland of the Bantu languages, near today\'s border of Nigeria and Cameroon.')]),
    S(-1500, 'c. 1500 to 500 BC', 'Around the forest to the Great Lakes',
      'An eastern stream skirted the northern edge of the rainforest and reached the Great Lakes, where people learned to '
      'smelt iron and herd cattle. Urewe pottery and iron furnaces mark them around Lake Victoria by 500 BC.',
      moves=[mv('foot', (10.5, 6.0, -1500), (16.0, 4.5, -1300), (22.0, 3.8, -1100), (27.5, 2.5, -900), (30.5, 0.0, -700),
                (33.0, -1.0, -500), label='Eastern Bantu')],
      sites=[site('Urewe', 34.0, 0.0, -500, 'Early ironworking farmers on the shores of Lake Victoria.')]),
    S(-500, 'c. 500 BC to AD 100', 'West to Angola',
      'The western stream crossed the lower Congo and moved down into the savannas of Angola, reaching the edge of the Namib '
      'desert, home of the Khoisan herders and foragers.',
      moves=[mv('foot', (14.5, -5.5, -500), (14.8, -8.5, -350), (15.5, -12.5, -200), (16.0, -15.5, -50), (17.0, -17.8, 100), label='Western Bantu')]),
    S(-200, 'c. 200 BC to AD 500', 'Iron down the east',
      'From the Great Lakes, iron-using farmers spread fast down the eastern side of the continent: through Tanzania, Malawi '
      'and Zambia to Zimbabwe, and along the coast to Mozambique, reaching today\'s KwaZulu-Natal by about AD 400.',
      moves=[mv('foot', (33.0, -1.0, -200), (35.0, -5.5, -100), (34.0, -10.5, 0), (32.8, -14.0, 100), (30.8, -18.0, 200),
                (30.5, -22.5, 300), (30.8, -27.0, 400), (30.5, -29.5, 450), label='Eastern Bantu'),
             mv('foot', (35.0, -5.5, -100), (38.8, -6.8, 0), (39.3, -10.5, 100), (40.0, -15.0, 200), (35.0, -19.5, 300), label='To the coast')],
      sites=[site('Great Zimbabwe', 30.93, -20.27, 450, 'Later, about 1100, Bantu-speaking Shona built the stone city of Great Zimbabwe here.')]),
  ])

M('austronesians', 'The Austronesian voyagers', 'Austronesians', 'seafarers', '#138d75', -3000, 600,
  'From Taiwan about 3000 BC, farmers and sailors in outrigger canoes spread through the islands of Southeast Asia and out '
  'into the Pacific and the Indian Ocean. Their languages, over 1,200 of them, run from Madagascar to Easter Island, more '
  'than halfway around the world: Malay, Tagalog, Javanese, Malagasy, Maori and Hawaiian are all Austronesian.',
  numbers='Over 1,200 languages, from Madagascar to Rapa Nui', rank=1, steps=[
    S(-3000, 'c. 3000 to 2000 BC', 'Out of Taiwan',
      'Rice farmers of Taiwan crossed the Luzon Strait to the Philippines about 2200 BC, then island-hopped south with pigs, '
      'dogs and pottery, sailing outrigger canoes that could carry families and seed.',
      moves=[mv('canoe', (120.4, 23.0, -3000), (120.3, 21.6, -2300), (121.0, 20.0, -2250), (120.6, 18.6, -2200), (119.8, 16.2, -2150),
                (119.9, 12.5, -2100), (121.0, 9.5, -2050), (122.0, 7.0, -2000), label='Austronesians')],
      sites=[site('Batanes Islands', 121.97, 20.45, -2250, 'Stepping stones between Taiwan and Luzon, where the oldest Philippine red-slipped pottery is found.')]),
    S(-2000, 'c. 2000 to 1500 BC', 'Through the islands',
      'They spread through Borneo, Sulawesi, Java and the Moluccas, meeting the older peoples of the region and mixing with '
      'them. At the edge of New Guinea they turned east, out into the open Pacific.',
      moves=[mv('canoe', (122.0, 7.0, -2000), (121.0, 4.0, -1950), (119.0, 1.0, -1900), (118.6, -2.5, -1850), (117.5, -5.5, -1800),
                (112.0, -5.8, -1750), (107.0, -5.5, -1700), label='To Java'),
             mv('canoe', (122.0, 7.0, -2000), (125.5, 3.5, -1900), (127.0, 0.5, -1800), (128.5, -3.0, -1650), label='To the Moluccas')]),
    S(-1500, 'c. 1500 to 800 BC', 'The Lapita people',
      'In the Bismarck Archipelago the voyagers became the Lapita people, known for their stamped pottery. In a few centuries '
      'they crossed thousands of kilometres of open sea to Vanuatu, New Caledonia, Fiji, Tonga and Samoa, islands no human '
      'had ever seen.',
      moves=[mv('canoe', (128.5, -3.0, -1500), (129.0, -1.8, -1480), (131.5, 0.3, -1460), (134.5, -0.6, -1440), (138.0, -1.3, -1420), (141.0, -2.1, -1400), (145.5, -3.6, -1370), (150.0, -3.2, -1350),
                (154.0, -5.5, -1250), (160.0, -9.6, -1150), (166.5, -14.0, -1050), (168.5, -17.5, -1000), (174.0, -18.5, -950),
                (177.5, -17.9, -900), label='Lapita'),
             mv('canoe', (177.5, -17.9, -900), (-178.0, -19.5, -870), (-175.3, -21.0, -850), (-173.5, -16.0, -820), (-171.8, -13.9, -800), label='To Tonga and Samoa')],
      sites=[site('Lapita', 164.6, -21.0, -1000, 'The site on New Caledonia that gave its name to the first Pacific voyagers.')]),
    S(200, 'c. AD 200 to 600', 'Across the Indian Ocean',
      'Westward, sailors from Borneo crossed the whole Indian Ocean. They settled Madagascar, where Malagasy, a language close '
      'to one spoken in southern Borneo, is still spoken, along with bananas and outrigger canoes on the African coast.',
      moves=[mv('canoe', (114.0, -3.5, 200), (110.0, -5.5, 250), (106.0, -6.0, 300), (102.0, -8.0, 350), (90.0, -10.0, 400),
                (75.0, -11.0, 450), (60.0, -13.0, 500), (51.0, -15.0, 550), (50.45, -15.4, 600), label='To Madagascar')],
      sites=[site('Madagascar', 47.5, -18.9, 600, 'Settled by Austronesians from Borneo, later joined by Bantu-speaking Africans.')]),
  ])

M('sea-peoples', 'The Sea Peoples', 'Sea Peoples', 'seafarers', '#2e4053', -1210, -1150,
  'About 1200 BC, as the palace kingdoms of the Bronze Age collapsed, bands of warriors and whole families, the "Sea '
  'Peoples" of Egyptian records, moved by land and sea through Anatolia, Cyprus and the Levant. Ugarit and other cities '
  'burned. Ramesses III fought them off at the mouth of the Nile, and one group, the Peleset, settled the coast of Canaan '
  'as the Philistines.',
  story='ev:bronze-age-collapse', rank=1, steps=[
    S(-1210, 'c. 1210 to 1185 BC', 'Raiders from the Aegean',
      'Who they were is still argued: Mycenaean Greeks, Sardinians, Sicilians, Anatolians, driven perhaps by drought, famine '
      'and the fall of their own kingdoms. Letters from Ugarit beg for help against enemy ships just before the city burned.',
      moves=[mv('galley', (24.5, 37.5, -1210), (27.5, 36.2, -1200), (30.5, 36.0, -1195), (32.5, 35.95, -1192), (34.8, 35.95, -1189), (35.5, 35.3, -1185), label='Sea Peoples'),
             mv('wagon', (27.5, 39.0, -1205), (30.5, 37.5, -1198), (33.5, 37.0, -1192), (36.0, 36.6, -1186), label='By land')],
      sites=[site('Ugarit', 35.78, 35.6, -1185, 'A rich port of Syria, destroyed and never rebuilt.')]),
    S(-1185, 'c. 1185 to 1150 BC', 'To the gates of Egypt',
      'They came down the coast with ox carts carrying women and children. In about 1177 BC Ramesses III met them on land and '
      'in the Nile delta, and carved the victory on his temple at Medinet Habu. The defeated Peleset settled Gaza, Ashkelon '
      'and Ashdod.',
      moves=[mv('galley', (35.5, 35.3, -1185), (34.5, 33.0, -1182), (33.5, 31.8, -1179), (32.0, 31.6, -1177), label='Sea Peoples'),
             mv('wagon', (36.0, 36.6, -1186), (35.8, 34.5, -1182), (35.0, 32.5, -1179), (34.5, 31.6, -1170), label='Philistines')],
      sites=[site('Battle of the Delta', 31.8, 31.4, -1177, 'Ramesses III defeats the Sea Peoples at the Nile mouths.'),
             site('Philistia', 34.55, 31.67, -1150, 'Gaza, Ashkelon and Ashdod: the Philistines\' new home.')]),
  ])

M('phoenician-colonies', 'Phoenician colonists', 'Phoenicians', 'settlers', '#7d3c98', -1100, -650,
  'The merchant cities of Phoenicia, Tyre above all, sent colonists across the whole Mediterranean to the Atlantic, '
  'founding trading posts that grew into cities: Kition on Cyprus, Utica, Carthage, Motya in Sicily, Nora in Sardinia and '
  'Gadir, today\'s Cadiz. They carried the alphabet with them.',
  rank=2, steps=[
    S(-1100, 'c. 1100 to 800 BC', 'West from Tyre',
      'Hemmed in between the mountains and the sea, the Phoenicians looked west for silver, tin and trade. Tradition puts the '
      'founding of Gadir beyond the Pillars of Hercules as early as 1100 BC; the oldest remains there date from about 800 BC.',
      moves=[mv('galley', (35.1, 33.27, -1100), (33.6, 34.7, -1050), (33.3, 34.45, -1040), (32.4, 34.45, -1030), (28.0, 35.0, -1000), (22.0, 34.8, -950), (15.5, 36.4, -900),
                (11.0, 37.3, -870), (5.0, 37.3, -850), (-1.5, 36.2, -830), (-5.4, 36.0, -815), (-6.3, 36.5, -800), label='Phoenicians')],
      sites=[site('Tyre', 35.2, 33.27, -1000, 'Island city of Phoenicia, famous for its purple dye.'),
             site('Gadir', -6.29, 36.53, -800, 'Cadiz, the Phoenicians\' gateway to the Atlantic.')]),
    S(-814, 'c. 814 to 650 BC', 'Carthage, the new city',
      'In legend, Princess Elissa (Dido) fled Tyre and founded Qart-hadasht, the "new city", in 814 BC. Carthage became the '
      'greatest Phoenician city of all, founding its own colonies in Sicily, Sardinia, Ibiza and Spain.',
      moves=[mv('galley', (35.1, 33.27, -814), (32.0, 33.8, -810), (26.0, 34.4, -805), (19.0, 35.0, -800), (13.0, 36.5, -795),
                (10.5, 36.95, -790), label='Elissa\'s followers'),
             mv('galley', (10.5, 36.95, -750), (11.8, 37.6, -740), label='To Motya'),
             mv('galley', (10.5, 36.95, -720), (9.0, 38.3, -700), label='To Sardinia'),
             mv('galley', (10.5, 37.0, -670), (10.3, 37.4, -668), (9.5, 37.5, -665), (6.0, 37.8, -660), (2.5, 38.6, -655), (1.45, 38.85, -654), label='To Ibiza')],
      sites=[site('Carthage', 10.32, 36.85, -814, 'Founded by colonists from Tyre; for six centuries the rival of Greeks and Romans.')]),
  ])

M('greek-colonies', 'Greek colonists', 'Greek colonists', 'settlers', '#2874a6', -775, -550,
  'Between about 775 and 550 BC Greek cities short of farmland sent out bands of colonists, chosen by lot and blessed by '
  'the oracle at Delphi. They founded hundreds of cities from Spain to the Crimea: Syracuse, Naples, Marseille, Byzantium '
  'and Cyrene among them. Southern Italy became Magna Graecia, "Great Greece", and the Mediterranean, in Plato\'s words, '
  'a pond with Greeks around it like frogs.',
  rank=1, steps=[
    S(-775, 'c. 775 to 700 BC', 'To Sicily and Italy',
      'Euboeans settled Pithekoussai on Ischia and then Cumae, near Naples. Corinth founded Syracuse in 733 BC, Sparta founded '
      'Taras (Taranto) in 706. The fertile plains of the west filled with Greek cities.',
      moves=[mv('galley', (23.6, 38.45, -775), (24.4, 38.0, -770), (23.2, 36.3, -765), (21.0, 37.0, -760), (17.0, 38.0, -755),
                (15.65, 38.2, -752), (15.4, 39.5, -750), (14.0, 40.6, -748), label='Euboeans'),
             mv('galley', (22.9, 37.94, -733), (22.4, 38.2, -733), (21.0, 38.5, -733), (19.0, 38.0, -733), (16.5, 37.2, -733), (15.29, 37.07, -733), label='Corinthians'),
             mv('galley', (22.56, 36.7, -706), (22.48, 36.3, -706), (21.8, 36.4, -706), (20.5, 37.5, -706), (19.2, 39.0, -706), (18.6, 39.4, -706), (17.5, 39.9, -706), (17.2, 40.4, -706), label='Spartans')],
      sites=[site('Syracuse', 15.29, 37.07, -733, 'Founded by Corinth; it became the greatest city of the Greek west.'),
             site('Pithekoussai', 13.9, 40.74, -770, 'On Ischia: the oldest Greek settlement in the west.')]),
    S(-680, 'c. 680 to 600 BC', 'To the Black Sea',
      'Miletus alone was said to have founded ninety colonies. Greeks settled the straits, where Megara founded Byzantium about '
      '667 BC, and then the shores of the Black Sea, trading wine and olive oil for the grain of the steppe.',
      moves=[mv('galley', (27.2, 37.4, -680), (26.9, 37.3, -679), (26.2, 37.8, -678), (25.7, 38.4, -677), (25.7, 39.3, -675), (26.0, 40.0, -673), (26.3, 40.2, -672), (27.5, 40.7, -670), (29.0, 41.05, -667),
                (29.5, 41.6, -660), (31.5, 43.0, -655), (31.8, 46.4, -647), label='Milesians'),
             mv('galley', (29.5, 41.6, -650), (32.5, 42.1, -640), (35.1, 42.03, -631), label='To Sinope')],
      sites=[site('Byzantium', 28.98, 41.01, -667, 'Founded by Megara on the Bosporus; later Constantinople and Istanbul.'),
             site('Olbia', 31.9, 46.69, -647, 'Milesian colony at the mouth of the Bug, trading with the Scythians.')]),
    S(-630, 'c. 630 to 550 BC', 'To Africa and Gaul',
      'Settlers from the island of Thera founded Cyrene in Libya about 630 BC, after the oracle told them to. Greeks from '
      'Phocaea in Asia Minor sailed to the far west and founded Massalia, Marseille, about 600 BC.',
      moves=[mv('galley', (25.4, 36.4, -630), (24.0, 35.8, -628), (22.5, 33.4, -626), (21.86, 32.82, -625), label='Theraeans'),
             mv('galley', (26.75, 38.65, -600), (25.0, 37.4, -600), (23.0, 36.2, -600), (20.0, 37.0, -600), (16.0, 37.9, -600),
                (15.62, 38.25, -600), (13.0, 39.5, -600), (11.0, 41.0, -600), (9.8, 43.0, -600), (7.2, 43.1, -600), (5.9, 42.95, -600), (5.37, 43.28, -600), label='Phocaeans')],
      sites=[site('Massalia', 5.37, 43.3, -600, 'Marseille, founded by Greeks from Phocaea.'),
             site('Cyrene', 21.86, 32.82, -630, 'The great Greek city of Libya.')]),
  ])

M('yayoi', 'Rice farmers reach Japan (Yayoi)', 'Yayoi farmers', 'folk', '#c0392b', -900, -100,
  'From about 900 BC, rice farmers from the Korean peninsula crossed to northern Kyushu, bringing wet-rice paddies, bronze '
  'and then iron. The Yayoi culture they began spread up the Japanese islands over the next thousand years, mixing with '
  'the Jomon people, foragers who had lived there for over ten thousand years. Most Japanese today descend from both.',
  rank=2, steps=[
    S(-900, 'c. 900 to 400 BC', 'Across the Tsushima Strait',
      'The first paddy fields of Japan, at Itazuke near Fukuoka, look just like those of southern Korea. Newcomers and '
      'Jomon locals farmed side by side.',
      moves=[mv('sail', (128.9, 35.1, -900), (129.3, 34.4, -850), (129.9, 33.85, -800), (130.35, 33.62, -800), label='Yayoi farmers')],
      sites=[site('Itazuke', 130.45, 33.57, -800, 'Some of the oldest rice paddies in Japan.')]),
    S(-400, 'c. 400 to 100 BC', 'East through Honshu',
      'Rice farming spread along the Inland Sea to the Kinai plain and then north and east, though in cold northern Honshu '
      'and Hokkaido people kept the Jomon way of life much longer.',
      moves=[mv('foot', (130.4, 33.6, -400), (131.5, 34.0, -350), (133.5, 34.5, -300), (135.5, 34.7, -250), (137.0, 35.1, -200),
                (139.0, 35.5, -150), (140.5, 38.0, -100), label='Yayoi farmers')],
      sites=[site('Yoshinogari', 130.38, 33.33, -300, 'A great moated Yayoi town in Kyushu.')]),
  ])

M('celts', 'The Celts on the move', 'Celts (Gauls)', 'folk', '#1e8449', -450, -270,
  'From their heartland north of the Alps, Celtic peoples moved south and east in the fourth and third centuries BC. Gauls '
  'took the Po valley and sacked Rome in 390 BC; later bands crossed the Balkans, plundered Delphi in 279 BC, and three '
  'tribes went on into Asia Minor, where they settled as the Galatians, to whom St Paul later wrote.',
  rank=1, steps=[
    S(-450, 'c. 450 to 390 BC', 'Over the Alps into Italy',
      'Senones, Boii, Insubres and other tribes crossed the Alps and drove the Etruscans out of the Po valley, which the Romans '
      'came to call Cisalpine Gaul. In 390 BC the Senones beat a Roman army on the Allia and sacked Rome.',
      moves=[mv('wagon', (7.0, 47.0, -450), (8.6, 46.3, -420), (9.2, 45.5, -400), (11.3, 44.5, -395), (12.3, 43.0, -392), (12.5, 41.9, -390), label='Gauls')],
      sites=[site('La Tene', 7.02, 47.0, -450, 'On Lake Neuchatel; its name is given to Celtic art and culture of the time.'),
             site('Sack of Rome', 12.48, 41.89, -390, 'Brennus and the Senones take Rome: "Vae victis", woe to the conquered.')]),
    S(-335, 'c. 335 to 278 BC', 'Down the Danube to Delphi',
      'Celtic bands moved down the Danube into the Balkans. In 279 BC Brennus led a great army through Macedonia to Delphi, '
      'where the Greeks beat them back in a storm. Some settled on the Danube, where Belgrade began as their Singidunum.',
      moves=[mv('wagon', (13.0, 48.0, -335), (17.0, 48.0, -320), (19.5, 46.5, -300), (20.5, 44.8, -285), (21.5, 42.0, -280),
                (22.0, 40.5, -279), (22.5, 38.5, -279), label='Brennus\'s Gauls')],
      sites=[site('Delphi', 22.5, 38.48, -279, 'The Gauls\' attack on the sanctuary fails in snow and earthquake.')]),
    S(-278, 'c. 278 to 270 BC', 'The Galatians in Asia',
      'Some 20,000 Celts, with their families, crossed the Hellespont in 278 BC, hired by the king of Bithynia. After years of '
      'raiding they were settled in central Anatolia around Ancyra, today\'s Ankara, which became Galatia.',
      moves=[mv('wagon', (22.0, 40.5, -278), (25.0, 40.9, -278), (26.6, 40.4, -278), (29.0, 40.3, -276), (31.0, 39.8, -274), (32.85, 39.93, -270), label='Galatians')],
      sites=[site('Ancyra', 32.86, 39.93, -270, 'Today\'s Ankara, chief town of the Galatians.')]),
  ])

M('cimbri-teutons', 'The Cimbri and Teutons', 'Cimbri and Teutons', 'folk', '#5d6d7e', -120, -101,
  'About 120 BC the Cimbri and Teutons left Jutland, perhaps after floods, and wandered through Europe for twenty years '
  'with their wagons, families and herds, looking for land. They crushed Roman armies, worst at Arausio in 105 BC, before '
  'Gaius Marius destroyed them at Aquae Sextiae and Vercellae. Rome never forgot the terror from the north.',
  rank=2, steps=[
    S(-120, '120 to 105 BC', 'Out of Jutland',
      'The tribes went south to the Danube, beat a Roman army at Noreia in 113 BC, turned west into Gaul, and in 105 BC '
      'destroyed two Roman armies at Arausio (Orange): tens of thousands of Romans died, one of Rome\'s worst defeats.',
      moves=[mv('wagon', (9.2, 56.5, -120), (10.0, 53.5, -117), (13.5, 50.5, -115), (14.3, 47.2, -113), (11.0, 47.8, -111),
                (7.5, 47.6, -110), (5.0, 46.5, -108), (4.8, 44.2, -105), label='Cimbri and Teutons')],
      sites=[site('Arausio', 4.81, 44.14, -105, 'Two Roman armies destroyed by the Cimbri.')]),
    S(-104, '104 to 101 BC', 'Marius stops them',
      'After a raid into Spain the tribes split to invade Italy. Marius, with a newly reformed army, destroyed the Teutons at '
      'Aquae Sextiae in 102 BC and the Cimbri at Vercellae in 101 BC.',
      moves=[mv('wagon', (4.8, 44.2, -104), (2.0, 43.2, -104), (-1.0, 43.0, -103), (2.0, 43.5, -103), (5.45, 43.53, -102), label='Teutons'),
             mv('wagon', (5.0, 46.5, -103), (9.0, 47.5, -102), (11.3, 47.0, -102), (11.0, 46.0, -101), (8.4, 45.3, -101), label='Cimbri')],
      sites=[site('Aquae Sextiae', 5.45, 43.53, -102, 'Marius destroys the Teutons near Aix-en-Provence.'),
             site('Vercellae', 8.42, 45.32, -101, 'The Cimbri are annihilated in the Po valley.')]),
  ])

M('yuezhi', 'The Yuezhi go west', 'Yuezhi', 'nomads', '#b7950b', -176, 30,
  'The Yuezhi, horse nomads of the Gansu corridor, were driven out by the Xiongnu about 176 BC; their king\'s skull, the '
  'story goes, became a Xiongnu drinking cup. They rode 3,000 km west, through the Ili valley to Bactria, where they '
  'conquered the last Greek kingdom of the east. One of their clans founded the Kushan Empire, which joined the trade of '
  'Rome, Persia, India and China.',
  rank=2, steps=[
    S(-176, '176 to 130 BC', 'Driven from Gansu',
      'Beaten by the Xiongnu, the Yuezhi fled to the Ili valley; pushed on again by the Wusun, they moved to the Oxus and '
      'crossed it into Bactria about 130 BC.',
      moves=[mv('horse', (100.5, 39.0, -176), (95.0, 40.5, -170), (88.0, 43.5, -165), (81.5, 43.8, -160), (76.0, 42.5, -140),
                (71.0, 40.5, -135), (67.5, 37.8, -130), label='Yuezhi')],
      sites=[site('Hexi Corridor', 100.5, 39.0, -176, 'The Yuezhi homeland between the Qilian mountains and the desert.')]),
    S(-128, '128 BC to AD 30', 'Masters of Bactria',
      'The Chinese envoy Zhang Qian found them in 128 BC, settled and rich, and uninterested in revenge on the Xiongnu. In the '
      'first century AD their Kushan clan united the rest and pushed south over the Hindu Kush.',
      moves=[mv('horse', (67.5, 37.8, -128), (67.0, 36.7, -100), (69.0, 35.5, 0), (71.5, 34.0, 30), label='Kushans')],
      sites=[site('Zhang Qian', 66.9, 36.7, -128, 'China\'s envoy reaches the Yuezhi; his journey opens the Silk Road.')]),
  ])

M('babylonian-exile', 'The Babylonian exile', 'Judeans', 'exiles', '#5b2c6f', -597, -515,
  'Nebuchadnezzar of Babylon took Jerusalem in 597 BC and carried its king and thousands of its people into exile; in 587 '
  'BC he destroyed the city and the Temple and deported more. By the rivers of Babylon the exiles kept their faith and '
  'began to gather their scriptures. When Cyrus the Great of Persia took Babylon in 539 BC he let them go home, and the '
  'Second Temple was finished in 515 BC.',
  rank=2, steps=[
    S(-597, '597 to 582 BC', 'By the rivers of Babylon',
      'The deportees walked some 1,300 km around the desert, by the Euphrates, to Babylonia, where they were settled in '
      'villages like Al-Yahudu, "Judah town", whose clay tablets have been found.',
      moves=[mv('foot', (35.23, 31.78, -597), (36.3, 33.5, -596), (37.5, 35.5, -595), (38.5, 36.0, -594), (40.5, 34.8, -593),
                (42.5, 33.6, -592), (44.42, 32.54, -591), label='Exiles')],
      sites=[site('Jerusalem', 35.23, 31.78, -587, 'Nebuchadnezzar destroys the city and Solomon\'s Temple.'),
             site('Babylon', 44.42, 32.54, -597, 'Where the exiles lived for two generations.')]),
    S(-538, '538 to 515 BC', 'The return',
      'Cyrus\'s decree allowed the exiles to return and rebuild. Many went home under Zerubbabel; many stayed, and Babylonia '
      'remained a great centre of Jewish life for fifteen hundred years.',
      moves=[mv('foot', (44.42, 32.54, -538), (42.5, 33.6, -537), (40.5, 34.8, -536), (38.5, 36.0, -535), (36.3, 33.5, -534), (35.23, 31.78, -533), label='Returning exiles')],
      sites=[site('Second Temple', 35.24, 31.78, -515, 'The rebuilt Temple, finished in 515 BC.')]),
  ])

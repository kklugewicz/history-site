from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('kalinga-war', 'The Kalinga War', 'war', (-262, -261),
      'One bloody conquest made the emperor Ashoka turn away from war and preach kindness across India.',
      scene('The last free kingdom',
            'The Mauryan Empire, founded by Chandragupta around 320 BC, ruled nearly all of the Indian subcontinent. '
            'Kalinga, on the east coast in what is now Odisha, grew rich from trade by sea and stayed free. Around 262 BC '
            "Chandragupta's grandson, the emperor Ashoka, marched against it.",
            kick='How it began', y=-262, at='kalinga'),
      battle('The war',
             'Kalinga fought hard, but we know almost nothing of how. Nearly everything we know of the war comes from Ashoka '
             'himself. Tradition places the last battle by the Daya river, below the hill of Dhauli, where the river is said '
             'to have run red.',
             img='Dhauli', y=-261, at='kalinga'),
      cost("Ashoka's own count",
           'In an inscription carved on rock a few years later, Ashoka says that 150,000 people were carried off, 100,000 '
           'were killed and many times that number died. He says the memory filled him with sorrow and regret, words no '
           'other conqueror of the ancient world put in stone.',
           num='100,000', of="killed, by Ashoka's own count", y=-256),
      figure('ashoka', 'Conquest by dhamma',
             'After Kalinga, Ashoka gave himself to dhamma, the Buddhist idea of right living: kindness to all living things, '
             'respect for parents, teachers and the poor, and tolerance of every faith. He said he would conquer from now on '
             'only by dhamma, never again by the sword.',
             y=-260),
      made('Words in stone',
           'Ashoka had his messages carved on rocks and on polished stone pillars across his empire, in local languages, '
           'and in Greek and Aramaic in the far northwest.',
           'They are among the oldest readable writing in India. Their Brahmi script, mother of most Indian scripts, was '
           'deciphered again only in 1837.',
           img='Edicts of Ashoka', y=-256),
      scene('Wells, trees and hospitals',
            'The inscriptions tell of wells dug and banyan trees planted along the roads for shade, of rest houses, of care '
            'for sick people and sick animals, and of fewer animals killed for the royal kitchen. Ashoka sent teachers of '
            'the Buddha to Sri Lanka and to the Greek kings of the west.',
            y=-250),
      work('The Lion Capital',
           'Four lions back to back crowned the pillar Ashoka set up at Sarnath, where the Buddha first taught. They are now '
           'the emblem of India, and the wheel carved beneath them is the wheel on its flag.',
           img='Lion Capital of Ashoka', y=-250, at=(83.02, 25.38), where='Sarnath'),
      legacy('Kalinga made Ashoka that rare conqueror remembered for his regret. His support helped Buddhism spread from '
             'India to Sri Lanka and, in time, across Asia, and his picture of a ruler who governs by kindness is still '
             'honoured in India.',
             "100,000 dead, by Ashoka's own count",
             'Turned Ashoka from war to dhamma',
             'His lions and wheel are symbols of India today'),
      states=['Mauryan Empire'], war='kalinga-war', wiki='Kalinga War', img='Dhauli')

event('silk-road', 'The Silk Road opens', 'trade', (-138, -60),
      "A Han envoy's thirteen-year journey opened the roads that carried silk, horses, faiths and plague across Asia.",
      figure('zhang-qian', 'An envoy to the west',
             'In 138 BC the Han emperor Wu sent an officer, Zhang Qian, west to look for allies against the Xiongnu, horse '
             'nomads who raided China. The Xiongnu caught him and kept him for ten years. He escaped, went on, and came home '
             'after thirteen years with news of lands no Chinese had seen.',
             y=-138, at='changan'),
      scene('Heavenly horses',
            'Zhang Qian told of the tall, fast horses of Ferghana, in Central Asia, said to sweat blood. Emperor Wu wanted '
            'them for his cavalry. When Ferghana would not sell, he sent armies thousands of kilometres across the deserts, '
            'and in 101 BC they came back with the horses.',
            img='Ferghana horse', y=-101, at='ferghana'),
      scene('Roads across a continent',
            'With Han forts guarding the oasis towns of the Tarim Basin, camel caravans carried silk, lacquer and iron west '
            'and brought back horses, glass, jade, grapes and alfalfa. Few traders went the whole way: goods passed from '
            'hand to hand, through Parthian, Kushan and Sogdian merchants.',
            y=-60, at='dunhuang'),
      tale('Silk in Rome',
           'Romans had no idea how silk was made: some thought it was combed from the leaves of trees. Rich Romans wore it '
           'all the same. The writer Seneca grumbled that it hid nothing of a woman\'s body, and Pliny the Elder that '
           'luxuries from the east drained the empire of its gold.',
           img='Silk', y=60, at='rome'),
      made('The secret of silk',
           'China kept secret for centuries how silk was made: it is spun from the cocoons of silkworms, fed on mulberry '
           'leaves.',
           'Around 552, the story goes, two monks smuggled silkworm eggs to Constantinople in hollow canes for the emperor '
           'Justinian, and Europe began to make its own silk.',
           img='Bombyx mori', y=552, at='constantinople'),
      scene('Faiths on the road',
            'Ideas travelled with the goods. Buddhist monks carried their faith from India into China along the trade '
            'routes from the first century AD, followed later by Christians, Manichaeans and Muslims. Paper travelled the '
            'other way, reaching Samarkand by the 700s and Europe after that.',
            img='Mogao Caves', y=70, at='dunhuang'),
      tale('Who named it',
           'No one at the time spoke of a Silk Road. A German geographer, Ferdinand von Richthofen, made up the name, '
           'Seidenstraße, in 1877. It was never one road but a web of routes across land and sea.',
           y=1877),
      legacy('For more than 1,500 years the Silk Road joined China, India, Persia, the Arab world and Europe, carrying '
             'goods, faiths, inventions and also diseases such as the Black Death. It tied the old world together long '
             'before ships sailed around it.',
             "Opened by Zhang Qian's journey of 138 BC",
             'Carried silk, horses, paper and faiths',
             'Named only in 1877'),
      states=['Han Empire', 'Han', 'Xiongnu', 'Yuezhi', 'Bactria', 'Parthia', 'Parthian Empire', 'Kushan Empire'],
      wiki='Silk Road', img='Silk Road', at='dunhuang')

event('fall-of-the-roman-republic', 'The fall of the Roman Republic', 'civil-war', (-49, -27),
      "Rome's generals turned their armies on each other, and a republic of nearly five centuries ended with an emperor.",
      scene('Generals with their own armies',
            'By the first century BC Rome ruled the Mediterranean, but its Republic, run by elected magistrates and the '
            'Senate, was breaking down. Soldiers were loyal to the generals who paid them, and Sulla had already marched on '
            'Rome itself. Caesar, Pompey and Crassus made a private pact to share power.',
            kick='How it began', y=-60, at='rome'),
      figure('julius-caesar', 'The die is cast',
             'In January 49 BC the Senate ordered Caesar, fresh from conquering Gaul, to give up his army. Instead he led a '
             'legion across the Rubicon, the stream at the edge of his province, which made him an enemy of the state. The '
             'die is cast, he is said to have quoted.',
             y=-49, at='rubicon'),
      figure('pompey', 'Pharsalus',
             'Pompey and much of the Senate fled to Greece. At Pharsalus in 48 BC Caesar\'s veterans beat Pompey\'s larger '
             'army. Pompey escaped to Egypt, where the advisers of the boy king Ptolemy XIII had him stabbed as he stepped '
             'ashore, hoping to please Caesar.',
             y=-48, at='pharsalus'),
      figure('cleopatra', 'A queen in a bedding sack',
             'In Alexandria, the young queen Cleopatra, driven out by her brother, had herself carried in to Caesar hidden '
             'in a sack for bedding, Plutarch says. Caesar took her side, won a short war in the streets of Alexandria and '
             'made her ruler of Egypt.',
             y=-48, at='alexandria'),
      scene('Dictator for life',
            'Caesar came home master of Rome. He pardoned many enemies and gave Rome a new calendar of 365 days with a leap '
            'year, which, slightly mended, is the one we use. Early in 44 BC he was made dictator for life. To many senators '
            'that made him a king in all but name.',
            y=-44, at='rome'),
      turn('The Ides of March',
           'On 15 March 44 BC a group of senators led by Brutus and Cassius stabbed Caesar 23 times at a meeting of the '
           'Senate in a hall by Pompey\'s theatre. They cried that Rome was free again. It was not: within months there was '
           'civil war again.',
           img='Assassination of Julius Caesar', y=-44, at='rome'),
      battle('Philippi and Actium',
             "Caesar's heir, his 18-year-old great-nephew Octavian, joined Mark Antony to destroy the assassins at Philippi "
             'in 42 BC. Then the two fell out. Antony allied with Cleopatra, and at Actium in 31 BC Octavian\'s admiral '
             'Agrippa beat their fleet. A year later both took their own lives in Egypt.',
             img='Battle of Actium', y=-31, at='actium'),
      figure('augustus', 'The first emperor',
             'In 27 BC the Senate gave Octavian a new name, Augustus. He never called himself king, and claimed he had '
             'restored the Republic, keeping its Senate and consuls. But he commanded the armies and decided everything, '
             'and those who ruled after him were emperors.',
             y=-27, at='rome'),
      legacy('The Republic\'s fall brought the Roman world two centuries of peace under emperors, but it ended Rome\'s long '
             'experiment with elected government. Its story, of a free state lost to ambition, haunted the founders of later '
             'republics, who borrowed its Senate and its words.',
             'Caesar crossed the Rubicon in 49 BC',
             'Murdered on the Ides of March, 44 BC',
             'Augustus became the first emperor in 27 BC'),
      states=['Roman Republic', 'Roman Empire', 'Ptolemaic Kingdom'], wiki='Crisis of the Roman Republic',
      img='Assassination of Julius Caesar', at='rome')

event('gallic-wars', "Caesar's Gallic Wars", 'wars', (-58, -50),
      'Julius Caesar conquered Gaul in eight years of war, and wrote the story of it himself.',
      scene('Gaul',
            'Gaul, roughly today\'s France and Belgium, was a land of Celtic peoples, with hill towns, gold coins and druid '
            'priests, split into dozens of rival tribes. Rome already held the south coast. In 58 BC its governor, Julius '
            'Caesar, deep in debt and hungry for glory, found reasons to march in.',
            kick='How it began', y=-58),
      battle('Helvetii and Germans',
             'In his first summer Caesar stopped the Helvetii, a whole people on the move with their wagons from what is now '
             'Switzerland, near Bibracte. Then he drove a German king, Ariovistus, back over the Rhine. Within three years '
             'most of Gaul had submitted.',
             y=-58),
      made('A bridge over the Rhine',
           'In 55 BC Caesar\'s engineers bridged the Rhine in about ten days, driving wooden piles into the river bed at a '
           'slant against the current.',
           'He crossed, burned villages for 18 days, came back and pulled the bridge down. It was a show of strength: Rome '
           'could go where it liked.',
           img="Caesar's Rhine bridges", y=-55),
      scene('Across the sea to Britain',
            'He also crossed to Britain, twice, in 55 and 54 BC, the first Roman army to go there. Storms wrecked his ships, '
            'and the Britons fought from chariots, which the Romans had not faced for generations. He took hostages and '
            'promises of tribute, and left.',
            y=-54, at=(1.38, 51.27), where='The coast of Kent'),
      figure('vercingetorix', 'One leader for all Gaul',
             'In 52 BC the Gauls rose together under a young noble of the Arverni, Vercingetorix. He had towns and farms '
             'burned so that the Romans could find no food, and beat Caesar at Gergovia, the worst defeat Caesar himself '
             'suffered in Gaul.',
             y=-52, at='gergovia'),
      battle('Alesia',
             'Vercingetorix shut himself up in the hill town of Alesia with 80,000 men. Caesar surrounded it with 16 km of '
             'walls and towers, then built a second ring of 21 km facing outwards against a huge Gaulish army coming to the '
             'rescue. Attacked from both sides at once, the Romans held.',
             img='Battle of Alesia', y=-52, at='alesia'),
      tale('The surrender',
           'Plutarch tells how Vercingetorix rode out of Alesia in his finest armour, circled Caesar on his horse, then '
           'jumped down and threw his weapons at Caesar\'s feet. He was kept in prison in Rome for six years, paraded in '
           "Caesar's triumph, and then strangled.",
           img='Vercingetorix Throws Down His Arms at the Feet of Julius Caesar', y=-52, at='alesia'),
      cost('The cost to Gaul',
           'Plutarch wrote that Caesar fought three million men, killed a million and enslaved a million more. The numbers '
           'are surely too high, but whole peoples were sold as slaves, and the trade made Caesar rich.',
           num='A million', of="killed, by Plutarch's count", y=-50),
      work('The Gallic War',
           'Caesar sent home reports each year, later published as The Gallic War. Written about himself as "Caesar", in '
           'plain, clear Latin, it opens: all Gaul is divided into three parts. It was propaganda, but it is also our main '
           'source, and for centuries pupils learned Latin from it.',
           img='Commentarii de Bello Gallico', y=-50),
      legacy('The conquest made Caesar rich, famous and strong enough to take Rome itself. Gaul stayed Roman for 500 years: '
             'its people came to speak Latin, which grew into French, and Roman towns grew into cities such as Lyon and '
             'Paris.',
             'Conquered Gaul in eight years',
             'Ended with the siege of Alesia',
             'Made Caesar strong enough to take Rome'),
      war='gallic-wars', wiki='Gallic Wars', img='Battle of Alesia')

event('roman-conquest-of-britain', 'The Roman conquest of Britain', 'conquest', (43, 84),
      'Rome took Britain in forty years of war, and Queen Boudica nearly drove it out again.',
      scene('Across the Channel',
            'A century after Caesar\'s raids, the emperor Claudius, who needed a victory, sent four legions across the '
            'Channel in AD 43. They beat the Britons under Caratacus and his brother on the river Medway in a two-day '
            'battle and crossed the Thames.',
            kick='How it began', y=43),
      tale('An emperor and his elephants',
           'Claudius came over himself, for just 16 days, bringing elephants, to lead his army into Camulodunum, now '
           'Colchester, the chief town of the strongest British tribe. On his arch in Rome an inscription boasted that '
           'eleven British kings had surrendered to him.',
           y=43, at='camulodunum'),
      figure(None, 'Caratacus',
             'Caratacus fought on in the hills of Wales for eight years, until Cartimandua, queen of the Brigantes, handed '
             'him over in chains. Brought to Rome, he spoke so proudly before Claudius, Tacitus says, that the emperor '
             'spared him and his family.',
             img='Caratacus', y=51, at='rome'),
      scene('The druids of Mona',
            'In 60 the governor, Suetonius Paulinus, attacked Mona, now Anglesey, the stronghold of the druids. Tacitus '
            'describes women in black with torches running among the warriors, and druids raising their hands to the sky '
            'with curses, until the legionaries steadied and cut them down.',
            y=60, at='mona'),
      figure('boudica', 'The queen of the Iceni',
             'Meanwhile the Iceni rose. Their king had left half his kingdom to the emperor, but Roman officials seized it '
             'all, flogged his widow Boudica and raped her daughters. She led the Iceni and their neighbours to burn '
             'Camulodunum, London and Verulamium. Tacitus says 70,000 people died.',
             y=60, at='camulodunum'),
      battle('The last battle',
             'Suetonius faced her vast army with about 10,000 men, in a narrow valley with woods behind him. The tight Roman '
             'ranks broke the charge, and the Britons were trapped against their own wagons. Boudica died soon after, of '
             'poison, Tacitus says.',
             y=61),
      battle('Mons Graupius',
             'The legions pushed on into Wales and Scotland. In 83 or 84 the governor Agricola beat the Caledonians at Mons '
             'Graupius, somewhere in the Highlands. Tacitus, his son-in-law, gave their leader a famous line about Rome: '
             'they make a desert and call it peace.',
             y=83, at='mons_graupius'),
      made("Hadrian's Wall",
           'Rome never held the far north. In 122 the emperor Hadrian ordered a wall of stone and turf 117 km long, coast to '
           'coast, with a small fort every Roman mile.',
           "It marked the empire's edge for nearly 300 years, and long stretches still stand. Letters on wooden tablets "
           'from a fort nearby tell of soldiers\' daily lives.',
           y=122, at=(-2.37, 55.0), where="Hadrian's Wall"),
      legacy('Britain was Roman for nearly 400 years, until about 410. The Romans founded London, built roads that modern '
             'ones still follow, and brought towns, baths and Latin. Boudica, who almost drove them out, became a heroine, '
             'and her statue stands by the Houses of Parliament.',
             'Invaded by Claudius in AD 43',
             "Boudica's revolt burned London",
             'Roman for nearly 400 years'),
      war='roman-conquest-of-britain', wiki='Roman conquest of Britain', img='Boadicea and Her Daughters')

event('jewish-roman-wars', 'The Jewish revolts against Rome', 'wars', (66, 136),
      'Judea rose against Rome again and again. Rome destroyed the Temple of Jerusalem and renamed the land.',
      scene('Judea under Rome',
            'Rome had ruled Judea since 63 BC, first through kings such as Herod the Great, who rebuilt the Temple in '
            'Jerusalem in splendour, then through governors. Taxes, insults to the Jewish faith and quarrels between Jews and '
            'Greeks built up, and in 66, when the governor took money from the Temple treasury, Jerusalem rose.',
            kick='How it began', y=66, at='jerusalem'),
      battle('Vespasian marches',
             'Nero sent his general Vespasian with three legions, and he took Galilee town by town. A rebel commander there, '
             'Joseph ben Matityahu, surrendered and foretold that Vespasian would be emperor. When that came true in 69, '
             'Joseph, now Flavius Josephus, became the historian of the war.',
             img='Josephus', y=67),
      figure('titus', 'The siege of Jerusalem',
             "In 70 Vespasian's son Titus besieged Jerusalem, crowded with pilgrims for Passover and split between rebel "
             'groups who fought each other. Famine set in. In the summer the Romans broke through the walls, and the Temple '
             'went up in flames.',
             y=70, at='jerusalem'),
      cost('The Temple falls',
           'Josephus says over a million died in the siege, surely too many, and 97,000 were taken as slaves. The Temple was '
           'never rebuilt. Jews still mourn it on the fast of Tisha B\'Av, and the Western Wall, part of its platform, is '
           'the holiest place where Jews pray.',
           num='97,000', of='taken as slaves, says Josephus', img='Western Wall', y=70, at='jerusalem'),
      work('The Arch of Titus',
           'In Rome, an arch built in honour of Titus shows his soldiers carrying off the treasures of the Temple, among '
           'them its great seven-branched lampstand, the menorah. That menorah is now the emblem of the State of Israel.',
           img='Arch of Titus', y=81, at='rome'),
      tale('Masada',
           'The last rebels held Masada, a fortress on a cliff top by the Dead Sea. In 73 or 74 the Romans built a huge ramp '
           'up to its walls. Josephus says that when they broke in, they found that the 960 defenders had killed themselves '
           'rather than be taken. Archaeologists still argue over his account.',
           img='Masada', y=73, at='masada'),
      figure('bar-kokhba', 'Son of the star',
             'In 132, after the emperor Hadrian planned a Roman city on the ruins of Jerusalem, Simon bar Kosiba led a new '
             'revolt. His followers called him Bar Kokhba, son of the star. For three years he ruled a free Judea and struck '
             'his own coins, until Rome crushed the revolt.',
             y=132),
      turn('A new name',
           'Hadrian built his city, Aelia Capitolina, and banned Jews from it. He renamed the province Syria Palaestina. '
           'The historian Cassius Dio says 580,000 Jewish fighters were killed and 985 villages destroyed.',
           y=136, at='jerusalem'),
      legacy('The wars ended Jewish self-rule in the land for almost 1,900 years. They also changed Judaism: without its '
             'Temple, it came to centre on scripture, the synagogue and the study of the rabbis, a faith that could be '
             'carried anywhere in the world.',
             'The Temple of Jerusalem destroyed in AD 70',
             'Masada fell in 73 or 74',
             'Judaism lived on without its Temple'),
      war='jewish-roman-wars', wiki='Jewish–Roman wars', img='Arch of Titus')

event('vesuvius-79', 'The eruption of Vesuvius', 'disaster', (79, 79),
      'In two days a volcano buried Pompeii and Herculaneum, and kept a Roman town exactly as it was.',
      scene('A town by the bay',
            'Pompeii was a busy town of some 11,000 people on the Bay of Naples, with temples, baths, bakeries, bars and two '
            'theatres, and rich villas along the coast. Few knew that Vesuvius, the green mountain above, was a volcano. A '
            'great earthquake in 62 had been a warning.',
            kick='Before', img='Pompeii', y=62, at='pompeii'),
      turn('The cloud',
           'One day in AD 79, in late October by the newest evidence, Vesuvius blew open. A column of ash and pumice shot '
           'more than 30 km into the sky. Pliny the Younger, watching from across the bay, said it was shaped like an '
           'umbrella pine.',
           y=79, at='vesuvius'),
      scene('A rain of stone',
            'Pumice and ash fell on Pompeii for hours and piled up nearly three metres deep. Roofs gave way under the weight. '
            'Many people fled. Others stayed in their houses, hoping it would pass.',
            y=79, at='pompeii'),
      figure(None, 'Pliny the Elder',
             'Pliny the Elder, admiral of the fleet at Misenum and author of a vast book about nature, sailed across the bay '
             'with warships to rescue people and see it close up. Fortune favours the brave, he said. He landed at Stabiae, '
             'and died on the beach the next morning, perhaps choked by fumes.',
             img='Pliny the Elder', y=79, at='misenum'),
      cost('The surge',
           'In the night and the next morning, avalanches of scorching gas and ash, faster than anyone could run, swept '
           'over Herculaneum and then Pompeii, killing everyone still there. Remains of some 1,150 people have been found at '
           'Pompeii so far, and over 300 by the harbour of Herculaneum.',
           num='1,150', of='people found at Pompeii so far', img='Herculaneum', y=79, at='herculaneum'),
      work('Letters to Tacitus',
           'Years later, Pliny\'s nephew, Pliny the Younger, 17 at the time, wrote two letters about it for the historian '
           'Tacitus: the cloud, his uncle\'s death, and his own escape with his mother through a darkness like a lamp put '
           'out in a closed room. Scientists still call such eruptions Plinian.',
           img='Pliny the Younger', y=106),
      tale('Writing on the walls',
           "Pompeii's walls are covered in writing: election posters, adverts for gladiator shows, lovers' notes, jokes and "
           'insults. One scribbler wondered that the wall had not fallen down under the weight of so much boring writing.',
           y=79, at='pompeii'),
      turn('Found again',
           'Pompeii lay buried and forgotten until digging began in 1748. In 1863 the archaeologist Giuseppe Fiorelli '
           'poured plaster into hollows that bodies had left in the hardened ash, bringing back the last moments of people, '
           'and even of a dog.',
           img='Giuseppe Fiorelli', y=1863, at='pompeii'),
      legacy('The eruption froze a Roman town in a single moment: its streets, food, paintings and people. Pompeii is still '
             'being dug, millions visit it each year, and Vesuvius, which last erupted in 1944, is watched day and night.',
             'Buried Pompeii and Herculaneum in AD 79',
             'Told by Pliny the Younger, who saw it',
             'A whole Roman town, kept as it was'),
      states=['Roman Empire'], wiki='Eruption of Mount Vesuvius in 79 AD', img='Pompeii', at='pompeii')

event('three-kingdoms', 'The Three Kingdoms', 'civil-war', (184, 280),
      "As the Han dynasty fell apart, warlords fought for a century, and their story became China's favourite novel.",
      scene('The Yellow Turbans',
            'By the 180s the Han emperors were puppets of palace eunuchs, and famine and plague stalked the land. In 184 '
            'hundreds of thousands of farmers rose under a faith healer, Zhang Jue, wearing yellow headscarves. The generals '
            'who crushed the Yellow Turbans became warlords with armies of their own.',
            kick='How it began', y=184),
      figure('cao-cao', 'The strongman of the north',
             'The strongest of them, Cao Cao, took the young emperor under his protection in 196 and ruled northern China in '
             'his name. A fine poet and a ruthless general, he was later cast as the great villain of the story.',
             y=196),
      battle('Red Cliffs',
             'In 208 Cao Cao sailed down the Yangtze with a huge fleet to finish off his rivals in the south. Sun Quan and '
             'Liu Bei joined against him. At Red Cliffs their general Zhou Yu sent burning ships into his fleet, and with '
             'sickness in his camp, Cao Cao turned back north. China would stay divided.',
             img='Battle of Red Cliffs', y=208, at='red_cliffs'),
      scene('Three emperors',
            'In 220 Cao Cao\'s son made the last Han emperor give up the throne and founded Wei in the north. Liu Bei, who '
            'claimed Han royal blood, made himself emperor of Shu in the southwest, and Sun Quan in time of Wu in the '
            'southeast. Three rulers each claimed to be the only Son of Heaven.',
            y=221),
      figure('zhuge-liang', 'The Sleeping Dragon',
             "Liu Bei's chief minister, Zhuge Liang, nicknamed the Sleeping Dragon, became China's model of the wise "
             'strategist. After Liu Bei died he led five campaigns north across the mountains against Wei, and died in camp '
             'in 234, still fighting.',
             y=234, at='chengdu'),
      tale('Borrowing arrows',
           'In the novel, Zhuge Liang must find 100,000 arrows in three days. He sends boats lined with straw dummies toward '
           'Cao Cao\'s camp in thick fog, with drums beating. Cao Cao\'s archers shoot into the fog, and the boats come back '
           'bristling with arrows. It never happened, but every Chinese child knows it.',
           kick='A legend'),
      cost('An empty land',
           'Wars, famine and plague emptied the country. A Han census of 157 counted 56 million people; the count of 280 '
           'found only 16 million. Many had fled or slipped out of the records, but the loss of life was still enormous.',
           num='16 million', of='people counted in 280, from 56 million', y=280),
      turn('None of the three',
           'In the end none of the three kingdoms won. Wei conquered Shu in 263. Then a Wei general\'s grandson, Sima Yan, '
           'took the throne for his own family, the Jin, and in 280 conquered Wu. China was one again, though not for long.',
           y=280, at='nanjing'),
      work('Romance of the Three Kingdoms',
           'In the 1300s Luo Guanzhong turned the history into a long novel of loyalty and cunning, which opens with Liu '
           'Bei, Guan Yu and Zhang Fei swearing brotherhood in a peach garden. It is still retold in operas, comics, TV '
           'series and video games.',
           img='Romance of the Three Kingdoms', y=1360),
      legacy('The Three Kingdoms lasted barely sixty years but became the best loved story of Chinese history. Its heroes are '
             'everywhere in East Asia: Guan Yu, Liu Bei\'s sworn brother, is worshipped as a god of loyalty in temples, '
             'shops and police stations.',
             'Began with the Yellow Turbans in 184',
             'Red Cliffs kept China divided',
             'Retold in a famous novel of the 1300s'),
      states=['Han', 'Jin'], wiki='Three Kingdoms', img='Battle of Red Cliffs', at='red_cliffs')

event('christian-rome', 'Rome becomes Christian', 'turning', (303, 380),
      'In less than a century Christianity went from a hunted faith to the religion of the Roman Empire.',
      scene('The Great Persecution',
            'For nearly three centuries Christians were a small, often distrusted faith in the empire, persecuted now and '
            'then. In 303 the emperor Diocletian ordered churches pulled down, scriptures burned and Christians forced to '
            'sacrifice to the gods. Thousands were killed.',
            kick='How it began', y=303),
      figure('constantine-the-great', 'In this sign',
             'In 312 Constantine, one of several rivals for the throne, marched on Rome. Before the battle at the Milvian '
             'Bridge, Christian writers later said, he saw a cross of light in the sky with the words: in this sign, '
             'conquer. His soldiers painted a Christian sign on their shields, and he won.',
             y=312, at='milvian_bridge'),
      turn('Freedom of worship',
           'In 313 Constantine and his fellow emperor Licinius agreed at Milan that everyone, Christians too, could worship '
           'as they chose, and that church property should be given back. Constantine built great churches in Rome and '
           'Jerusalem and gave bishops wealth and power.',
           img='Edict of Milan', y=313),
      scene('The Council of Nicaea',
            'Christians quarrelled over whether Jesus was fully equal to God the Father. In 325 Constantine called some 300 '
            'bishops to Nicaea, the first council of the whole Church. They agreed the Nicene Creed, which most churches '
            'still say today.',
            img='First Council of Nicaea', y=325, at='nicaea'),
      made('A new Rome',
           'In 330 Constantine moved his capital east, to the old Greek town of Byzantium on the Bosporus, rebuilt as '
           'Constantinople.',
           'It was the capital of the eastern Roman Empire for over a thousand years, and is now Istanbul.',
           img='Constantinople', y=330, at='constantinople'),
      tale('Baptised at the last',
           'Constantine put off being baptised until he lay dying in 337, as many did then, so that all his sins would be '
           'washed away at once. In 361 his nephew Julian, who loved the old gods, became emperor and tried to bring them '
           'back. He died fighting in Persia less than two years later.',
           y=337),
      turn('The faith of the empire',
           'In 380 the emperor Theodosius declared the Nicene faith the religion of all Romans, and in the 390s he banned '
           'sacrifices to the old gods and closed their temples. The Olympic Games, held in honour of Zeus, came to an end '
           'at about this time.',
           img='Theodosius I', y=380),
      legacy('Within a century Christianity went from a persecuted faith to the religion of the Roman state. Through Rome it '
             'spread across Europe and far beyond, and the creeds, churches and calendar of that age still shape the lives '
             'of more than two billion Christians.',
             'The Great Persecution of 303',
             'Made legal by Constantine in 313',
             'The religion of the empire by 380'),
      states=['Rome (Constantinus)', 'Rome (Maximian)', 'Rome (Galerius)', 'Rome (Diocletianus)', 'Roman Empire',
              'Eastern Roman Empire', 'Western Roman Empire'],
      wiki='Constantine the Great and Christianity', img='Battle of the Milvian Bridge', at='rome')

event('fall-of-western-rome', 'The fall of the Western Roman Empire', 'fall', (376, 476),
      'Goths, Huns and Vandals broke into a divided empire, and in 476 the last emperor in the west was sent into retirement.',
      scene('Refugees at the Danube',
            'In 376 tens of thousands of Goths, fleeing the Huns, begged to be let across the Danube into the empire. The '
            'Romans let them in, then starved and cheated them: officers traded dogs to eat for their children as slaves, a '
            'Roman historian wrote. The Goths rose in revolt.',
            kick='How it began', y=376),
      battle('Adrianople',
             'In 378 the emperor Valens attacked the Goths near Adrianople without waiting for help from the west. The '
             'Gothic horsemen came back from foraging and caught his army on a hot August afternoon. Two thirds of it was '
             'destroyed, and Valens was never found.',
             y=378, at='adrianople'),
      figure('alaric-i', 'Rome is sacked',
             'In 410 Alaric, king of the Visigoths, tired of waiting for the land and pay he had been promised, took and '
             'plundered Rome itself, the first time in 800 years an enemy had done so. He spared the churches. The whole '
             'Roman world was stunned.',
             y=410, at='rome'),
      figure('attila', 'Attila the Hun',
             'In the 440s Attila ruled an empire from the Rhine to the Black Sea and made Constantinople pay him tonnes of '
             'gold. In 451 Romans and Goths together stopped him in Gaul, at the Catalaunian Plains. He invaded Italy the '
             'next year but turned back, and died in 453.',
             y=451, at='catalaunian_plains'),
      battle('The Vandals',
             'The Vandals crossed from Spain to Africa in 429 and took Carthage and the rich grain lands that fed Rome. In 455 '
             'their king Gaiseric sailed to Rome and plundered it for two weeks. That is why wrecking things is still called '
             'vandalism.',
             img='Sack of Rome (455)', y=455, at='rome'),
      figure('odoacer', '476',
             'By now the western emperors were puppets of Germanic generals. In 476 one of them, Odoacer, removed the boy '
             'emperor Romulus Augustulus, sent him to live on an estate near Naples, and sent the imperial robes to '
             'Constantinople: the west no longer needed an emperor of its own.',
             y=476, at='ravenna'),
      scene('Why did Rome fall?',
            'A German historian once counted 210 reasons that have been given, from lead pipes to Christianity. Most '
            'historians now point to civil wars between generals, an empire split in two whose richer eastern half stayed '
            'safe, money troubles, and peoples on the move whom Rome could no longer beat or take in.',
            kick='Why it happened'),
      legacy('The west broke up into kingdoms of Goths, Franks, Vandals and others that grew into the countries of Europe. '
             'But Rome did not vanish: its eastern half lasted another thousand years, and Latin, Roman law and the Church '
             'lived on in the west.',
             'Rome sacked in 410 and 455',
             'The last western emperor removed in 476',
             'The eastern empire lasted until 1453'),
      war='fall-of-western-rome', wiki='Fall of the Western Roman Empire', img='Sack of Rome (410)')

event('plague-of-justinian', 'The Plague of Justinian', 'epidemic', (541, 549),
      'The first known pandemic of plague swept the Roman world and Persia, and kept coming back for two hundred years.',
      scene("Justinian's empire",
            'The emperor Justinian, ruling from Constantinople, had won back North Africa and much of Italy and built the '
            'great church of Hagia Sophia. In 541, with his armies still at war, a new sickness appeared at Pelusium, a port '
            'on the edge of Egypt.',
            kick='Before', img='Hagia Sophia', y=541, at='pelusium'),
      figure('justinian-i', 'The emperor falls ill',
             'In the spring of 542 the plague reached Constantinople, probably on the grain ships from Egypt. The historian '
             'Procopius, who lived through it, says that at its worst 10,000 people died in the city each day. The emperor '
             'himself caught it, and lived.',
             y=542, at='constantinople'),
      scene('Swellings',
            'People would suddenly run a fever, and then swellings, buboes, rose in the groin and armpits. Many fell into a '
            'coma or raved; most died within days. No one knew it was spread by fleas from rats.',
            y=542),
      cost('Bodies in the towers',
           'There were too few living to bury the dead. Procopius says great pits were dug, and when they were full, bodies '
           'were piled inside the towers of the city walls, until the whole city stank.',
           num='10,000', of='deaths a day in the capital, said Procopius', y=542, at='constantinople'),
      scene('Across the world',
            'The plague spread to Italy, Gaul, Spain, Persia and Arabia, and came back again and again for two hundred '
            'years, until about 750. Farms lost their workers, taxes fell and armies shrank, just when Justinian needed them '
            'most.',
            y=543),
      made('Proof from the grave',
           'In 2013 scientists found the DNA of the plague germ, Yersinia pestis, in skeletons from a graveyard of the 500s '
           'in Bavaria.',
           'It proved that this plague was the same disease as the Black Death of 1347: the first of three great plague '
           'pandemics in history.',
           img='Yersinia pestis', y=2013),
      legacy('The plague weakened both Rome and Persia just before the armies of Islam came out of Arabia, and some '
             'historians see it as the moment the ancient world turned into the Middle Ages. How many died is argued over: '
             'guesses run from a few million to tens of millions.',
             'Reached Constantinople in 542',
             'Came back for two hundred years',
             'The first of three plague pandemics'),
      states=['Eastern Roman Empire', 'Sasanian Empire', 'Ostrogoths', 'Franks', 'Visigoths'],
      wiki='Plague of Justinian', at='constantinople')

event('early-muslim-conquests', 'The early Muslim conquests', 'conquest', (632, 750),
      "Within a century of Muhammad's death, Arab armies built an empire from Spain to the Indus.",
      figure('abu-bakr', 'Out of Arabia',
             'When the Prophet Muhammad died in 632, most of Arabia had accepted Islam. The first caliph, Abu Bakr, put down '
             'the tribes that broke away, then sent armies north against the two great powers of the day, Rome and Persia, '
             'both worn out by a long war with each other and by plague.',
             kick='How it began', y=632, at='medina'),
      figure('khalid-ibn-al-walid', 'Yarmouk',
             'The most famous Arab general, Khalid ibn al-Walid, called the Sword of God, led his men on a daring march '
             'across the Syrian desert. In 636, by the river Yarmouk, the Arabs destroyed a great Roman army, and Syria was '
             'lost to Rome for good.',
             y=636, at='yarmouk'),
      battle('Qadisiyyah',
             'At about the same time, at Qadisiyyah in Iraq, an Arab army beat the Persians after days of fighting, war '
             'elephants and all. The Persian capital Ctesiphon fell with its treasures. By 651 the last Persian king was '
             'dead and his empire gone.',
             y=636, at='qadisiyyah'),
      figure('umar', 'Jerusalem',
             'Under the second caliph, Umar, the Arabs took Jerusalem in 637 or 638. Tradition says Umar came in person, '
             'dressed simply, and promised the Christians safety for their lives, their property and their churches. Egypt '
             'fell soon after.',
             y=638, at='jerusalem'),
      scene('Why so fast?',
            'The Arab armies were small, but united by their new faith and well led, and their enemies were exhausted. Many '
            'conquered peoples did not resist. They paid a tax and kept their own religions, and only slowly, over '
            'centuries, did most of them become Muslim.',
            kick='Why it happened'),
      figure('tariq-ibn-ziyad', 'Into Spain',
             'The Umayyad caliphs, ruling from Damascus, pushed on across North Africa. In 711 Tariq ibn Ziyad crossed to '
             'Spain with Berber and Arab troops, and the rock where he landed was named after him: Jabal Tariq, Gibraltar. '
             'In a few years almost all of Spain was theirs.',
             y=711, at=(-5.35, 36.14), where='Gibraltar'),
      battle('The edges of the world',
             'In 732 a Frankish army under Charles Martel beat an Arab raiding army between Tours and Poitiers. In the east, '
             'Arab armies had reached the Indus and Central Asia. By 750 the caliphate ran from the Atlantic to the borders '
             'of India and China.',
             img='Battle of Tours', y=732, at='tours'),
      turn('Quarrels over the leadership',
           'The conquests were matched by civil wars over who should lead the Muslims, which left the lasting split between '
           'Sunni and Shia. In 750 the Abbasid family overthrew the Umayyads and moved the capital east, soon to their new '
           'city of Baghdad.',
           y=750, at='baghdad'),
      legacy('In barely a century the conquests made Arabic the language of the Middle East and North Africa and began the '
             'spread of Islam, today the faith of nearly two billion people. The caliphate became one great world of trade '
             'and learning, from Spain to Central Asia.',
             'From Arabia to Spain and the Indus in a century',
             'Ended the Persian Empire',
             'Spread Arabic and Islam'),
      war='early-muslim-conquests', wiki='Early Muslim conquests', img='Battle of Yarmouk')

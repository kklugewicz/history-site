from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('assyria-kush-wars', 'The wars of Assyria and Kush', 'wars', (-744, -663),
      'The Assyrian empire and the Kushite pharaohs of Egypt fought for eighty years over the lands between them.',
      figure('tiglath-pileser-iii', 'The war machine',
             'In 745 BC Tiglath-Pileser III seized the throne of Assyria, in northern Iraq, in a revolt. He built a '
             'standing army of iron-armed infantry, chariots, cavalry and siege engines, and turned it west against '
             'the kingdoms of Syria and the Levant. Conquered peoples were deported by the tens of thousands, to break '
             'their will to rebel.',
             kick='How it began', y=-745, at='nimrud'),
      figure('piye', 'The black pharaohs',
             'Far up the Nile, in Nubia, the kings of Kush ruled from Napata, below the holy mountain of Jebel Barkal. '
             'They worshipped Egypt\'s god Amun, and saw themselves as the true heirs of the pharaohs. Around 728 BC '
             'King Piye sailed north, stormed Memphis, and made the princes of a divided Egypt kneel to him.',
             y=-728, at='napata'),
      turn('Israel falls',
           'In 722 BC the Assyrians took Samaria, capital of the kingdom of Israel, after a long siege, and carried '
           'off its people, the ten lost tribes of later legend. When Gaza rebelled with help from Egypt, Sargon II '
           'beat the rebels and an Egyptian army at Raphia, in 720 BC: the first clash between the two powers.',
           y=-720, at='samaria'),
      figure('sennacherib', 'Lachish',
             'In 701 BC King Hezekiah of Judah rebelled, counting on Egypt. Sennacherib swept down the coast, beat a '
             'Kushite and Egyptian army, and stormed the city of Lachish, a siege he had carved in stone on the walls '
             'of his palace at Nineveh. Then he shut Hezekiah up in Jerusalem, he boasted, like a bird in a cage.',
             y=-701, at='lachish'),
      tale('Jerusalem spared',
           'Jerusalem was not taken. Sennacherib\'s own records say that Hezekiah paid a huge tribute of gold and '
           'silver. The Bible says that an angel of the Lord struck down 185,000 Assyrians in a night, and the Greek '
           'historian Herodotus heard that mice had gnawed through the bowstrings of an Assyrian army in Egypt.',
           y=-701, at='jerusalem'),
      figure(None, 'Taharqa',
             'Taharqa, the greatest of the Kushite pharaohs, built temples from Nubia to the Nile delta, and kept '
             'stirring up revolt in the Levant. In 674 BC he threw back an Assyrian invasion. But in 671 BC Esarhaddon '
             'crossed Sinai with water carried by Arab camels and took Memphis, and Taharqa fled south, leaving his '
             'son a captive.',
             img='Taharqa', y=-671, at='memphis'),
      figure('ashurbanipal', 'The sack of Thebes',
             'The Kushites came back again and again. In 663 BC, when Taharqa\'s successor retook Memphis, the '
             'Assyrian king Ashurbanipal sent a great army up the Nile and sacked Thebes, the holy city of Amun, '
             'carrying off its treasure and two great obelisks. The Hebrew prophet Nahum remembered its fall.',
             y=-663, at='thebes'),
      legacy('Kush withdrew to Nubia for good, and its kings ruled on at Napata and later Meroë for almost a thousand '
             'years, building pyramids of their own. Assyria had overreached: within about fifty years Egypt and '
             'Babylon broke free, and in 612 BC Nineveh itself fell.',
             'Eighty years of war over the Levant',
             'Israel fell in 722 BC, Thebes in 663 BC',
             'Assyria itself fell in 612 BC'),
      war='assyria-kush-wars', wiki='Assyrian conquest of Egypt', at='memphis')

event('persian-conquests-cyrus-cambyses', 'The conquests of Cyrus', 'conquest', (-553, -525),
      'In twenty-five years a minor Persian king and his son built the largest empire the world had yet seen.',
      scene('Anshan',
            'Around 559 BC Cyrus became king of Anshan, a small Persian kingdom in the south of Iran, under the rule '
            'of the Medes. Legend said that his grandfather, the Median king Astyages, had dreamed that the boy would '
            'take his throne, and ordered him killed as a baby, but a herdsman raised him instead.',
            kick='How it began', y=-559, at='pasargadae'),
      figure('cyrus-the-great', 'The Medes',
             'Around 553 BC Cyrus rose against Astyages. When Astyages marched into Persia, part of his army mutinied '
             'under a noble, Harpagus, and handed the king over. Cyrus took the Median capital, Ecbatana, and its '
             'treasure, and the Persians became masters of the Medes\' empire, from the Zagros to central Anatolia.',
             y=-550, at='ecbatana'),
      figure('croesus', 'A great empire',
             'Croesus of Lydia, the richest king of his day, decided to strike first, after the oracle at Delphi told '
             'him that if he attacked he would destroy a great empire. He did: his own. Cyrus followed him home to '
             'Sardis, frightened his horses with camels, whose smell they could not stand, and took the citadel.',
             y=-547, at='sardis'),
      tale('The pyre',
           'Herodotus tells that Cyrus set the captured Croesus on a pyre to be burned, and that Croesus called out '
           'the name of Solon, the Athenian wise man who had told him that no one can be called happy until he is '
           'dead. Moved, Cyrus ordered the fire put out, and a sudden storm of rain did it for him.',
           y=-547, at='sardis'),
      turn('Babylon',
           'In 539 BC Cyrus turned on Babylon, the greatest city in the world. Its king, Nabonidus, had angered the '
           'priests of the city\'s god, Marduk. Cyrus beat his army at Opis, and his general entered Babylon without a '
           'fight. A clay cylinder later told how Cyrus had come as a peacemaker, chosen by Marduk himself.',
           y=-539, at='babylon', img='Cyrus Cylinder'),
      scene('The return',
            'Cyrus let the peoples whom the Babylonians had deported go home. Among them were the Jews, exiled since '
            'Nebuchadnezzar destroyed Jerusalem, and many returned to rebuild the Temple. The Bible calls Cyrus the '
            'anointed of the Lord, the only foreign king it honours so.',
            y=-538, at='jerusalem'),
      tale('Tomyris',
           'Cyrus spent his last years on the steppe frontier. Herodotus says that in 530 BC he was killed fighting '
           'the Massagetae, nomads east of the Caspian, and that their queen, Tomyris, whose son had died through his '
           'trickery, had his head plunged into a skin full of blood, so that he could drink his fill.',
           y=-530),
      figure('cambyses-ii', 'Egypt',
             'His son Cambyses II took on the last great power of the Near East. With water supplied by Arab chiefs he '
             'crossed Sinai, and in 525 BC crushed the army of the young pharaoh Psamtik III at Pelusium, then took '
             'Memphis. A later tale says his soldiers carried cats, sacred to the Egyptians, in front of them.',
             y=-525, at='pelusium'),
      legacy('The Persians now ruled from the Aegean to Central Asia and the Nile, the largest empire the world had '
             'yet seen. Cyrus was remembered, even by the Greeks who fought his heirs, as the model of a wise and '
             'tolerant king, and his tomb still stands at Pasargadae, in Iran.',
             'Cyrus beat the Medes, Lydia and Babylon',
             'Cambyses took Egypt in 525 BC',
             'The largest empire yet seen'),
      war='persian-conquests-cyrus-cambyses', wiki='Achaemenid Empire', img='Cyrus Cylinder', at='pasargadae')

event('roman-conquest-of-italy', 'Rome conquers Italy', 'conquest', (-390, -264),
      'In 125 years Rome went from a city sacked by the Gauls to the master of Italy.',
      scene('The Gauls',
            'In about 390 BC a war band of Gauls came south from the Po valley, routed the Roman army at the Allia '
            'River, eleven miles from the city, and sacked Rome. Legend says the sacred geese on the Capitol cackled '
            'and woke the defenders in time to beat off a night attack on the citadel.',
            kick='How it began', y=-390, at='rome'),
      tale('Woe to the conquered',
           'The Gauls agreed to leave for a ransom in gold. When the Romans complained that the weights were false, '
           'the story goes, the Gallic chief, Brennus, threw his sword onto the scales and said, "Woe to the '
           'conquered." Romans later told how their hero Camillus arrived just in time to drive the Gauls off.',
           y=-390, at='rome'),
      turn('Allies',
           'Rome recovered, built a great new wall, and fought its neighbours one by one. When its Latin allies rose '
           'against it, Rome crushed them, and in 338 BC bound each city to itself by a separate treaty. The defeated '
           'became allies who sent soldiers to Rome\'s wars, and some were made Roman citizens.',
           y=-338),
      battle('The Caudine Forks',
             'The Samnites, tough hill peoples of the Apennines, were Rome\'s hardest enemy. In 321 BC their general, '
             'Gavius Pontius, trapped a whole Roman army in a mountain pass, the Caudine Forks, and made every man '
             'crawl under a yoke of spears in shame. Rome later broke the peace, and fought on.',
             y=-321, at='caudine_forks'),
      made('The Appian Way',
           'To move its armies south, Rome began in 312 BC a great road from the city to Capua, named after the '
           'censor who built it, Appius Claudius.',
           'The first of the great Roman roads, which in the end ran some 80,000 kilometres across the empire. Parts '
           'of the Appian Way are still walked today.',
           img='Appian Way', y=-312, at='rome'),
      battle('Sentinum',
             'In 295 BC the Samnites joined Gauls, Etruscans and Umbrians in a great alliance against Rome. At '
             'Sentinum, it is said, the consul Decius Mus offered his life to the gods of the underworld and rode to '
             'his death to win the battle, and the allied army was destroyed. Rome was master of central Italy.',
             y=-295, at='sentinum'),
      figure('pyrrhus-of-epirus', 'A Pyrrhic victory',
             'Tarentum, the richest Greek city in Italy, called in King Pyrrhus of Epirus, with a professional army '
             'and war elephants. He beat the Romans at Heraclea and Asculum, but lost so many men that, the story '
             'goes, he said that one more such victory would ruin him. A costly win is still called a Pyrrhic victory.',
             y=-279, at='tarentum'),
      turn('Master of Italy',
           'Pyrrhus went off to fight Carthage in Sicily, came back, and was checked at Beneventum in 275 BC. He '
           'sailed home, Tarentum surrendered, and by 264 BC Rome ruled all of Italy south of the Po. That year it '
           'answered a call for help from across the strait in Sicily, and went to war with Carthage.',
           y=-275, at='beneventum'),
      legacy('Rome held Italy not by force alone, but with a web of alliances, colonies and roads, and by sharing its '
             'citizenship. Its allies\' soldiers made its armies almost impossible to wear down, as Hannibal would '
             'find. From Italy, Rome went on to conquer the Mediterranean.',
             'A city sacked by the Gauls around 390 BC',
             'Master of Italy by 264 BC',
             'Allies, colonies and roads held it together'),
      war='roman-conquest-of-italy', wiki='Roman expansion in Italy', img='Appian Way', at='rome')

event('roman-conquest-of-hispania', 'Rome conquers Spain', 'conquest', (-218, -19),
      'Rome came to Spain to fight Carthage, and stayed for two hundred years of war to conquer it.',
      scene('Hannibal\'s base',
            'Carthage had built an empire in southern Spain, rich in silver, and from there Hannibal set out in 218 BC '
            'to invade Italy. To cut him off from his base, Rome landed an army in the north-east, at the Greek port of '
            'Emporion. Spain became the second front of the war.',
            kick='How it began', y=-218, at='emporion'),
      figure('scipio-africanus', 'New Carthage',
             'Both Roman commanders, the Scipio brothers, were killed in 211 BC. The son of one of them, the young '
             'Publius Scipio, took over, and in 209 BC stormed New Carthage, the enemy\'s capital in Spain, sending men '
             'across a lagoon as the water fell. At Ilipa in 206 BC he drove the Carthaginians out of Spain.',
             y=-209, at='new_carthage'),
      figure('cato-the-elder', 'The provinces',
             'Rome stayed. In 197 BC it made the coasts into two provinces, and governors came to collect tribute, '
             'often with a heavy hand. The peoples of the interior, the Celtiberians of the hills and the Lusitanians '
             'of the west, rose again and again. Cato, sent to crush them, boasted that he had taken more towns in '
             'Spain than he had spent days there.',
             y=-195),
      figure(None, 'Viriathus',
             'In 150 BC a governor massacred thousands of Lusitanians who had laid down their arms. One who escaped, a '
             'shepherd named Viriathus, led eight years of guerrilla war from the hills, beating army after army. In '
             '139 BC Rome bribed three of his friends to murder him in his sleep; when they asked for their reward, the '
             'story goes, they were told that Rome does not pay traitors.',
             img='Viriathus', y=-139),
      battle('Numantia',
             'The hill town of Numantia defied Rome for ten years. In 134 BC Scipio Aemilianus, who had destroyed '
             'Carthage, ringed it with walls and camps nine kilometres long, and starved it. When it fell, many '
             'Numantines killed themselves rather than surrender, and the town was razed.',
             y=-133, at='numantia'),
      figure('pompey', 'Sertorius',
             'In the 70s BC Spain became a battlefield of Rome\'s own civil wars. Quintus Sertorius, a Roman rebel, won '
             'the Lusitanians and Celtiberians to his side, kept a white fawn that he said brought him messages from '
             'the goddess Diana, and beat the Senate\'s armies, the young Pompey\'s among them, until his own officers '
             'murdered him at dinner in 72 BC.',
             y=-76),
      figure('augustus', 'The last war',
             'Only the mountains of the north still held out. In 26 BC the emperor Augustus came in person to fight '
             'the Cantabrians and Astures, who, the Romans said, would rather die than be enslaved. Revolts flared '
             'until his general Agrippa ended them in 19 BC, two centuries after the Romans first landed.',
             y=-26),
      legacy('Hispania became one of the most Roman parts of the empire. It gave Rome the emperors Trajan and Hadrian, '
             'the writer Seneca, silver and olive oil, and its Latin grew into Spanish, Portuguese and Catalan. Roman '
             'bridges, aqueducts and theatres still stand across Spain and Portugal.',
             'Rome came to fight Carthage in 218 BC',
             'Two centuries of war for the interior',
             'Its Latin grew into Spanish and Portuguese'),
      war='roman-conquest-of-hispania', wiki='Roman conquest of the Iberian Peninsula', at='numantia')

event('han-expansion-korea-vietnam', 'The Han conquests of Nanyue and Korea', 'conquest', (-111, -108),
      'Emperor Wu of Han sent armies south and north-east, and brought northern Vietnam and Korea under Chinese rule.',
      scene('The southern kingdom',
            'When the Qin dynasty fell, one of its generals, Zhao Tuo, made himself king of Nanyue, the Southern Yue, '
            'with its capital at Panyu, today\'s Guangzhou. His kingdom reached into what is now northern Vietnam. For '
            'almost a century its kings honoured the Han emperors when it suited them, and called themselves emperors '
            'at home.',
            kick='How it began', y=-204, at='guangzhou', where='Panyu'),
      figure('emperor-wu-of-han', 'Emperor Wu',
             'Emperor Wu of Han, who reigned for 54 years, pushed China\'s borders outward on every side. In 112 BC a '
             'minister of Nanyue, Lü Jia, killed the young king, his Chinese-born mother, who wanted to submit to the '
             'Han, and the Han envoys. Wu sent his armies south over the mountain passes and down the rivers.',
             y=-112),
      battle('Panyu',
             'In 111 BC one Han general reached Panyu first and set it on fire, and its defenders surrendered to '
             'another. Lü Jia and the new king fled by sea, and were caught. Nanyue was cut into nine commanderies '
             'reaching down to the Red River delta of Vietnam, and the next year the Han took Minyue, on the coast to '
             'the north, as well.',
             y=-111, at='guangzhou', where='Panyu'),
      scene('A thousand years',
            'Northern Vietnam stayed under Chinese rule for about a thousand years, with many risings, the most famous '
            'led in AD 40 by two sisters, Trưng Trắc and Trưng Nhị, who are national heroines in Vietnam today. Vietnam '
            'won lasting independence only in 938.',
            y=40, img='Trưng sisters'),
      battle('Gojoseon',
             'Then Wu turned north-east, to Gojoseon, the oldest Korean kingdom, whose king, Ugeo, blocked the way to '
             'the lands beyond. In 109 BC one Han army crossed the Bohai Sea by ship while another marched overland. '
             'Both were beaten back at first, then closed in on the capital, Wanggeom, near today\'s Pyongyang.',
             y=-109, at='pyongyang'),
      turn('The four commanderies',
           'In the summer of 108 BC, besieged and divided, Gojoseon\'s ministers murdered their king, and the capital '
           'fell. The Han split the land into four commanderies. The greatest, Lelang, around Pyongyang, lasted four '
           'centuries, and carried Chinese writing, tools and ideas into Korea and on to Japan.',
           y=-108, at='pyongyang'),
      legacy('The wars set the edges of the Chinese world for centuries. In Vietnam and Korea, Chinese writing, '
             'Confucian learning and later Buddhism took root, but both peoples kept their own languages, and fought '
             'long and proudly to rule themselves.',
             'Nanyue fell in 111 BC',
             'Gojoseon fell in 108 BC',
             'Northern Vietnam was ruled from China for a thousand years'),
      war='han-expansion-korea-vietnam', wiki='Han conquest of Nanyue', at='guangzhou', where='Panyu')

event('mithridatic-wars', 'The Mithridatic Wars', 'wars', (-88, -63),
      'Mithridates, king of Pontus, fought Rome three times for the East, and became the enemy Rome feared most.',
      figure('mithridates-vi', 'The poison king',
             'Mithridates VI became king of Pontus, on the Black Sea coast of Anatolia, as a boy, after his father was '
             'poisoned. Afraid of being poisoned himself, he took small doses every day to make himself immune. He '
             'grew into a giant of a man who could speak, it was said, all 22 languages of his lands.',
             kick='How it began', y=-110, at='sinope'),
      cost('The Asian Vespers',
           'In 88 BC, while Rome was at war with its own allies in Italy, Mithridates swept through the Roman province '
           'of Asia, welcomed by many cities sick of Roman tax collectors. Then he ordered every Roman and Italian in '
           'the province killed on a single day.',
           num='Perhaps 80,000', of='Romans and Italians killed in a day', y=-88, at='ephesus'),
      figure('sulla', 'Sulla in Greece',
             'Athens joined Mithridates. Rome sent Sulla, who besieged the city, cutting down the groves of Plato\'s '
             'Academy for timber, and stormed it in 86 BC. He then crushed much larger armies at Chaeronea and '
             'Orchomenus, and made a quick peace so that he could hurry home to fight a civil war.',
             y=-86, at='athens'),
      battle('Lucullus',
             'In 74 BC the king of Bithynia died and left his kingdom to Rome, and Mithridates went to war a third '
             'time. The Roman general Lucullus starved his army outside Cyzicus, invaded Pontus, and in 69 BC routed the '
             'huge army of Mithridates\' son-in-law, Tigranes of Armenia, at his new capital, Tigranocerta. Then his '
             'weary troops mutinied.',
             y=-69),
      tale('Cherries',
           'Lucullus grew enormously rich in the East, and his feasts were so lavish that a Lucullan banquet still '
           'means a splendid one. The Roman writer Pliny says that he brought the first cherry trees to Italy, from '
           'Pontus.',
           y=-72, at='sinope'),
      figure('pompey', 'Pompey the Great',
             'In 66 BC Rome gave the command to Pompey, fresh from sweeping the pirates from the sea. He caught '
             'Mithridates by night and destroyed his army, and Tigranes laid his crown at Pompey\'s feet. Mithridates '
             'escaped around the Black Sea to the Crimea, planning, it was said, to march on Italy over the Alps.',
             y=-66),
      turn('The end of Mithridates',
           'In 63 BC his son Pharnaces led a revolt against him. Cornered at Panticapaeum, the old king took poison, '
           'but, the story goes, his body was so used to it that it would not work, and he had a soldier of his guard '
           'kill him with a sword.',
           y=-63, at='panticapaeum'),
      legacy('Pompey reorganised the whole East. Pontus, Bithynia and Syria became Roman provinces, ringed by client '
             'kings, and he took Jerusalem. He came home the greatest man in Rome. Mithridates became a legend, and '
             'gave his name to the art of making oneself immune to poison.',
             'Three wars with Rome, 88 to 63 BC',
             'Sulla, Lucullus and Pompey fought him',
             'Rome won Anatolia and Syria'),
      war='mithridatic-wars', wiki='Mithridatic Wars', at='sinope')

event('huna-invasions-india', 'The Huna invasions of India', 'invasion', (460, 528),
      'Hun horsemen broke into India from the north-west, and the golden age of the Gupta emperors came to an end.',
      scene('A golden age',
            'In the fifth century the Gupta emperors ruled most of northern India, in what is remembered as a golden '
            'age: the poet Kalidasa wrote his plays, mathematicians used the decimal numbers we use today, and the great Buddhist '
            'university at Nalanda was founded. Beyond the mountains to the north-west, a new people of the steppe, '
            'the Alchon Huns, had taken Kabul.',
            kick='How it began', y=450, at='pataliputra'),
      figure(None, 'Skandagupta',
             'Around 460 the Huns pushed through the passes into India. The emperor Skandagupta led the Gupta army '
             'against them and drove them back, and his pillar at Bhitari boasts that the earth shook when he met the '
             'Hunas in battle. For a generation, they stayed beyond the Indus.',
             img='Skandagupta', y=460),
      turn('Toramana',
           'After Skandagupta died, quarrels over the throne weakened the empire. Around 500 the Hun king Toramana '
           'came down from Gandhara with his horsemen, overran the Punjab and reached Malwa, in the heart of India. An '
           'inscription on a great stone boar at Eran is dated in his reign.',
           y=500, at='eran'),
      figure(None, 'Mihirakula',
             'Toramana\'s son Mihirakula ruled from Sakala, today\'s Sialkot, over lands from Kashmir to Gwalior. '
             'Buddhist writers remembered him as a monster who burned monasteries and killed monks, and a chronicle of '
             'Kashmir, written six centuries later, says he loved to hear the screams of elephants pushed over a '
             'cliff.',
             img='Mihirakula', y=520, at='sakala'),
      scene('A pilgrim',
            'Around 520 a Chinese Buddhist pilgrim, Song Yun, came to the Hun court in Gandhara. He found a proud king '
            'who had been at war with Kashmir for three years, with hundreds of war elephants, and who received the '
            'Chinese emperor\'s letter without rising from his seat.',
            y=520),
      battle('Yashodharman',
             'At last Indian kings joined against the Huns. Around 528 Yashodharman, king of Mandasor in Malwa, beat '
             'Mihirakula, and set up victory pillars saying that the Hun king had bowed at his feet. A later Chinese '
             'pilgrim gave the credit to a Gupta king, Narasimhagupta, who, he said, captured Mihirakula and let him '
             'go.',
             y=528, at='mandsaur', where='Mandasor'),
      legacy('Mihirakula withdrew to Kashmir, and Hun power in India was broken. But so was the Gupta Empire, which '
             'split into rival kingdoms within a few decades, and India\'s classical age ended in a patchwork of '
             'regional states. Some historians think Hun settlers were among the ancestors of later warrior clans.',
             'The Huns broke in around 460',
             'Mihirakula ruled from Kashmir to Gwalior',
             'The Gupta Empire broke apart'),
      war='huna-invasions-india', wiki='Alchon Huns', at='eran')

event('justinian-reconquests', 'Justinian\'s wars of reconquest', 'conquest', (533, 554),
      'The emperor Justinian set out to win back the lost West of the Roman Empire, and very nearly did.',
      scene('The lost West',
            'By 500 the Western Roman Empire was gone. Vandals ruled North Africa from Carthage, Ostrogoths ruled '
            'Italy and Visigoths Spain. In Constantinople the emperors of the East still called their realm the Roman '
            'Empire, and in 527 a man came to the throne who meant to make it whole again: Justinian.',
            kick='How it began', y=527, at='constantinople'),
      figure('theodora', 'Nika',
             'In 532 the chariot-racing fans of Constantinople rioted, burned much of the city, and crowned a new '
             'emperor. Justinian was ready to flee, but his wife, Theodora, a former actress, said, it is told, that '
             'royalty makes a fine burial shroud. He stayed, and his general Belisarius massacred thousands of rioters '
             'in the Hippodrome.',
             y=532, at='constantinople'),
      battle('The Vandal War',
             'In 533 Belisarius sailed for Africa with about 15,000 men in 500 ships. He routed the Vandal king, '
             'Gelimer, at Ad Decimum, entered Carthage the next day, and in 534 Gelimer surrendered. Led in triumph '
             'through Constantinople, he kept repeating, it was said, the words of the Bible: "Vanity of vanities, all '
             'is vanity."',
             y=533, at='carthage'),
      figure('belisarius', 'Belisarius in Italy',
             'In 535 Belisarius took Sicily almost without a fight, then crossed to Italy, stormed Naples and entered '
             'Rome in December 536. The Goths besieged him there for a year, and failed. In 540 they offered to make '
             'him emperor of the West; he pretended to agree, Ravenna opened its gates, and the Gothic king was taken '
             'captive to Constantinople.',
             y=536, at='rome'),
      battle('Totila',
             'Just as a terrible plague began to sweep the empire in 541, the Goths chose a brilliant new king, '
             'Totila. He won back most of Italy, freeing slaves and winning over peasants to his side, and in 546 '
             'starved Rome into surrender. Belisarius came back with too few men, and was recalled again in 549.',
             y=546, at='rome'),
      battle('Narses',
             'At last Justinian gave a large, well-paid army to Narses, a eunuch of the palace in his seventies. In '
             '552, at Taginae, his archers cut down the Gothic cavalry, and Totila was killed. The last Gothic king '
             'fell near Vesuvius that autumn, and in 554 Narses destroyed an army of Franks. Italy was Roman again.',
             y=552, at='taginae'),
      work('San Vitale',
           'In Ravenna, won back from the Goths, the church of San Vitale was finished in 547. Its glittering mosaics '
           'show Justinian and Theodora, with haloes, bringing gifts to the altar among their courtiers and guards: '
           'the most famous portraits of the age.',
           img='Basilica of San Vitale', y=547, at='ravenna'),
      turn('Ruin',
           'Twenty years of war, famine and plague had wrecked Italy, and Rome, taken and retaken again and again, was '
           'a shadow of itself. In 568, three years after Justinian\'s death, the Lombards invaded and took much of '
           'the peninsula for good.',
           y=568),
      legacy('Africa, Italy and a strip of southern Spain were Roman again, and the Mediterranean was almost a Roman '
             'lake once more. But the wars had cost too much, and the empire, worn down by plague, could not hold its '
             'gains: the Lombards soon took most of Italy, and the Arabs, later, Africa.',
             'Africa was won back in 533 and 534',
             'Twenty years of war for Italy',
             'The gains were soon lost'),
      war='justinian-reconquests', wiki='Gothic War (535–554)', img='Belisarius', at='ravenna')

event('roman-persian-war-602-628', 'The last war of Rome and Persia', 'war', (602, 628),
      'The last and greatest war between Rome and Persia nearly destroyed both empires, just before the Arabs came.',
      scene('A murdered emperor',
            'In 602 a rough centurion named Phocas led a mutiny, seized the throne in Constantinople and had the '
            'emperor Maurice and his sons put to death. The Persian king, Khosrow II, owed his throne to Maurice, who '
            'had helped him win it back years before, and he declared war to avenge him.',
            kick='How it began', y=602, at='constantinople'),
      figure('khosrow-ii', 'The king of kings',
             'Khosrow\'s armies took the great frontier fortress of Dara in 604, then overran Roman Mesopotamia and '
             'Armenia. In 610 Heraclius, son of the governor of Africa, sailed from Carthage, overthrew Phocas and '
             'became emperor, but he inherited an eastern front in collapse.',
             y=604),
      cost('Jerusalem',
           'In 614 the Persians took Jerusalem after a short siege. Thousands of its people were killed, churches were '
           'burned, and the True Cross, believed to be the cross of Christ, was carried off to the Persian capital, '
           'Ctesiphon. By 619 they had taken Egypt too, the granary that fed Constantinople.',
           num='Thousands', of='killed when Jerusalem fell', y=614, at='jerusalem'),
      figure('heraclius', 'The counterattack',
             'Heraclius made peace with the Avars, melted down church treasure to pay his troops, and in 622 crossed '
             'to Asia Minor to train a new army. In 624 he marched into the heart of Persia and destroyed its holiest '
             'fire temple, at Ganzak. For three years he outfought one Persian army after another.',
             y=624),
      battle('Constantinople besieged',
             'In 626 Khosrow struck at the capital itself. A Persian army camped across the Bosporus while a vast horde '
             'of Avars and Slavs attacked the land walls, and Heraclius stayed in the east. The defenders sank the '
             'Slavs\' canoes as they tried to ferry the Persians across, and the Avars gave up. The city thanked the '
             'Virgin Mary.',
             y=626, at='constantinople'),
      battle('Nineveh',
             'With the Western Turks pouring into the Caucasus as his allies, Heraclius invaded Mesopotamia, and in '
             'December 627 destroyed a Persian army near the ruins of Nineveh, killing its general, it is said, in '
             'single combat. He sacked Khosrow\'s palace at Dastagird and marched on Ctesiphon.',
             y=627, at='nineveh'),
      turn('The True Cross',
           'Khosrow was overthrown and killed by his own son in February 628, and the new king made peace, handing '
           'back all the lands Persia had taken. In 630 Heraclius carried the True Cross back into Jerusalem in '
           'triumph.',
           y=630, at='jerusalem'),
      legacy('After 26 years of war the frontier was back where it had been, and both empires were bled white. '
             'Within a decade the armies of a new faith, Islam, burst out of Arabia. They took Syria, Jerusalem and '
             'Egypt from the Romans, and swept the Persian empire away altogether.',
             'Persia took Jerusalem and Egypt',
             'Heraclius struck back into Persia',
             'Both empires were left open to the Arabs'),
      war='roman-persian-war-602-628', wiki='Byzantine–Sasanian War of 602–628', at='constantinople')

event('struggle-for-sicily', 'The struggle for Sicily', 'wars', (827, 1091),
      'Arabs from Tunisia took Sicily from Byzantium, and Norman adventurers took it from them: an island of three cultures.',
      scene('An invitation',
            'In 827 a rebel Byzantine admiral, Euphemius, invited the Aghlabid emirs of Tunisia into Sicily. An army '
            'of about 10,000 men landed at Mazara under an aged judge and scholar, Asad ibn al-Furat. He died '
            'besieging Syracuse, but the invaders stayed, and in 831 took Palermo.',
            kick='How it began', y=827, at='mazara'),
      battle('Fortress by fortress',
             'The conquest went on fortress by fortress through the mountains for 75 years. Arab raiders also struck '
             'mainland Italy, and in 846 even plundered the church of St Peter outside the walls of Rome. Enna, the '
             'island\'s central stronghold, fell in 859, and Syracuse in 878, after a siege of nine months.',
             y=878, at='syracuse'),
      scene('Arab Sicily',
            'By 965 the last Byzantine towns had fallen. Under its emirs Sicily flourished: the Arabs brought lemons, '
            'oranges, sugar cane and cotton, and new ways to water the land, and Palermo, with hundreds of mosques, '
            'became one of the largest cities in Europe.',
            y=965, at='palermo'),
      figure('harald-hardrada', 'Maniakes',
             'In 1038, while the emirs fought among themselves, the Byzantine general George Maniakes invaded, with '
             'Norman knights in his army and Varangian guards led by Harald Hardrada, the future king of Norway. He '
             'took Messina and Syracuse, but was recalled under suspicion, and his gains were soon lost.',
             y=1040, at='syracuse'),
      figure(None, 'Robert Guiscard',
             'Normans from northern France had come south as mercenaries, and stayed as conquerors. The boldest was '
             'Robert de Hauteville, called Guiscard, the Cunning. He beat a papal army in 1053, was made duke of '
             'Apulia and Calabria by the pope, and in 1071 took Bari, ending five centuries of Byzantine rule in Italy.',
             img='Robert Guiscard', y=1071, at='bari'),
      battle('Roger in Sicily',
             'Robert\'s youngest brother, Roger, crossed to Sicily in 1061 at the invitation of one of the quarrelling '
             'emirs, and took Messina. In 1063, with a small band of knights, he beat a far larger Muslim army at '
             'Cerami, and in 1072 the brothers took Palermo by land and sea.',
             y=1072, at='palermo'),
      turn('The last emirs',
           'It took Roger almost twenty more years to win the rest. Noto, the last Muslim town, surrendered in 1091, '
           'the year he also took Malta. As count of Sicily he let his Muslim subjects keep their faith, and Arab '
           'scholars, Greek monks and Latin knights lived side by side under Norman rule.',
           y=1091),
      work('The Palatine Chapel',
           'In Palermo, Roger\'s son, King Roger II, built a chapel for his palace in the 1140s, with Greek mosaics of '
           'Christ, Latin inscriptions, and a wooden ceiling carved and painted by Muslim artists, with writing in '
           'Arabic. It sums up the kingdom of three cultures.',
           img='Cappella Palatina', y=1140, at='palermo'),
      legacy('The Norman conquests became the Kingdom of Sicily in 1130, one of the richest states in Europe, where '
             'Arab, Greek and Latin learning met. Sicilian is still full of Arabic words, and Arab gardens, Byzantine '
             'mosaics and Norman churches stand side by side in Palermo.',
             'The Arabs took Sicily over 75 years',
             'The Normans took it from 1061 to 1091',
             'A kingdom of three cultures'),
      war='struggle-for-sicily', wiki='Emirate of Sicily', img='Cappella Palatina', at='palermo')

event('albigensian-crusade', 'The Albigensian Crusade', 'war', (1209, 1229),
      'A pope called a crusade against heretics in France, and northern knights conquered the south.',
      scene('The Cathars',
            'In the rich, sunny south of France, in Languedoc, many people followed the Cathars, Good Men and Good '
            'Women who taught that the world was the work of an evil power, and lived lives of poverty and fasting. The '
            'Church called them heretics, and the lords of the south, above all the count of Toulouse, would not root '
            'them out.',
            kick='How it began', y=1200, at='toulouse'),
      figure('pope-innocent-iii', 'A crusade at home',
             'In 1208 a papal legate was murdered, and Pope Innocent III blamed Count Raymond VI of Toulouse. He called '
             'a crusade against the heretics, promising the knights who joined it the same forgiveness of sins as a '
             'crusade to the Holy Land, and the heretics\' lands as well.',
             y=1208),
      cost('Béziers',
           'In July 1209 the crusaders stormed Béziers and massacred its people, Catholics and Cathars alike, many in '
           'the churches where they had taken refuge. A monk later wrote that the pope\'s legate, asked how to tell '
           'them apart, answered, "Kill them all. God will know his own," though he may never have said it.',
           num='Thousands', of='killed when Béziers fell', y=1209, at='beziers', where='Béziers'),
      figure('simon-de-montfort-5th-earl-of-leicester', 'Simon de Montfort',
             'Carcassonne surrendered weeks later, and its lands were given to a hard northern baron, Simon de '
             'Montfort. He took the Cathar strongholds one by one, and at Minerve and Lavaur burned hundreds of Cathars '
             'alive. At Bram he had a hundred prisoners blinded, leaving one man a single eye to lead the rest.',
             y=1210, at='carcassonne'),
      battle('Muret',
             'King Peter II of Aragon, overlord of many southern lords and a hero of the wars against the Moors in '
             'Spain, crossed the Pyrenees to protect his vassals. At Muret in September 1213, Montfort\'s much smaller '
             'force charged and killed him, and the southern army fled.',
             y=1213, at='muret'),
      tale('The stone',
           'In 1217 Toulouse rose again for its count, and Montfort laid siege to it. On 25 June 1218 a stone from a '
           'catapult on the walls, worked, the song of the crusade says, by the women and girls of the city, struck '
           'him on the head and killed him.',
           y=1218, at='toulouse'),
      turn('The king takes over',
           'Simon\'s son could not hold his father\'s conquests, and in 1224 he handed his rights to the king of '
           'France. In 1226 King Louis VIII led a royal army south, and most towns submitted. By the Treaty of Paris in '
           '1229 the count of Toulouse gave up much of his land, and his heiress was married to the new king\'s '
           'brother.',
           y=1229, at='paris'),
      cost('Montségur',
           'To finish the Cathars off, the Church set up the Inquisition. In 1244 their last great stronghold, the '
           'mountain castle of Montségur, fell after a siege of ten months, and more than two hundred Cathars who would '
           'not give up their faith were burned together on a great pyre below it.',
           num='Over 200', of='Cathars burned at Montségur in one day', y=1244, at='montsegur', where='Montségur'),
      legacy('The crusade brought the south into the kingdom of France, and the Inquisition stamped out the Cathars '
             'within a century. The south\'s own language, Occitan, and the culture of its troubadours slowly faded, '
             'and the ruined Cathar castles on their crags still haunt the landscape.',
             'A crusade against heretics in France',
             'Simon de Montfort conquered the south',
             'Languedoc became part of France'),
      war='albigensian-crusade', wiki='Albigensian Crusade', at='carcassonne')

event('edward-i-conquest-of-wales', 'Edward I\'s conquest of Wales', 'conquest', (1277, 1283),
      'The last native Prince of Wales was killed, and Edward I ringed his land with great stone castles.',
      scene('Llywelyn',
            'By the 1260s Llywelyn ap Gruffudd, ruler of Gwynedd in the mountains of north Wales, had made himself '
            'master of most of Wales, and in 1267 the English king recognised him as Prince of Wales. But when Edward I '
            'came to the throne, Llywelyn refused, again and again, to come and swear homage to him.',
            kick='How it began', y=1267, img='Llywelyn ap Gruffudd'),
      figure('edward-i-of-england', 'The first war',
             'In 1277 Edward invaded from three sides, the king himself marching along the north coast from Chester, '
             'cutting roads through the forests as he went. His fleet seized Anglesey and its harvest, the bread of '
             'Gwynedd, and the starving Welsh made peace. Llywelyn was left only the land west of the River Conwy.',
             y=1277),
      turn('Palm Sunday 1282',
           'In 1282 Llywelyn\'s brother Dafydd stormed the English castle of Hawarden, and all Wales rose. Edward came '
           'back, meaning to finish it this time. But an English force crossing a bridge of boats from Anglesey to the '
           'mainland was caught by the Welsh at Moel-y-Don, and many knights drowned.',
           y=1282),
      turn('The last prince',
           'In December Llywelyn went south to raise mid Wales. On 11 December 1282, near Builth, he was killed in a '
           'skirmish, cut down, it seems, by an English soldier who did not know who he was. His head was sent to '
           'London and set on the Tower, crowned with ivy.',
           y=1282, at='cilmeri', where='Cilmeri'),
      scene('The end of Gwynedd',
            'Edward fought on through the winter. His armies took the last Welsh castles, and in June 1283 Dafydd was '
            'caught in the mountains. He was hanged, drawn and quartered at Shrewsbury, one of the first men known to '
            'have suffered that death.',
            y=1283, at='shrewsbury'),
      work('The castles',
           'To hold Wales, Edward built a ring of great stone castles, at Conwy, Caernarfon, Harlech and Beaumaris, '
           'designed by a master mason from Savoy, James of St George, with walled towns beside them for English '
           'settlers. Caernarfon\'s banded walls were meant to recall those of Constantinople.',
           img='Caernarfon Castle', y=1283, at='caernarfon'),
      turn('Prince of Wales',
           'By the Statute of Rhuddlan in 1284 Wales was annexed to the English crown and divided into shires. In '
           '1301 Edward made his son, born at Caernarfon, Prince of Wales. Ever since, the title has gone to the heir '
           'to the English, and later British, throne.',
           y=1301, at='caernarfon'),
      legacy('Independent Welsh rule was over. There would be one more great rising, led by Owain Glyndŵr from 1400, '
             'but Wales stayed under English rule. Its language and poetry lived on, and Llywelyn is remembered as '
             'Llywelyn the Last.',
             'Two English invasions, 1277 and 1282',
             'Llywelyn was killed in December 1282',
             'Edward ringed Wales with castles'),
      war='edward-i-conquest-of-wales', wiki='Conquest of Wales by Edward I', at='caernarfon',
      # the map of 1200 draws Wales and Gaelic Ireland as one state, the Celtic kingdoms, which the country timelines give
      # to Ireland; Wales is Britain's, by the story's places
      drop=('Celtic kingdoms',))

event('siamese-khmer-wars', 'The fall of Angkor', 'war', (1350, 1431),
      'The new Thai kingdom of Ayutthaya fought the old Khmer Empire, and in 1431 sacked its great capital, Angkor.',
      scene('Angkor',
            'For five centuries the Khmer kings had ruled much of mainland Southeast Asia from Angkor, a vast city of '
            'temples and reservoirs in what is now Cambodia. Angkor Wat, built in the 1100s, is the largest religious '
            'monument in the world. But by the 1300s the empire was in decline.',
            kick='How it began', y=1300, at='angkor', img='Angkor Wat'),
      figure('ramathibodi-i', 'Ayutthaya',
             'In 1351 a Thai ruler, U Thong, founded a new capital on an island in the Chao Phraya River and named it '
             'Ayutthaya. Crowned as King Ramathibodi I, he gave his kingdom laws, and set out to win the western lands '
             'that had once been Angkor\'s. Standing on the trade routes to the sea, Ayutthaya grew rich fast.',
             y=1351, at='ayutthaya'),
      battle('The first siege',
             'According to the chronicles of Ayutthaya, the king\'s son, Prince Ramesuan, marched east and besieged '
             'Angkor around 1352, and the city fell after a long siege. The Khmer won their capital back within a few '
             'years, but the raid showed how weak they had become.',
             y=1352, at='angkor'),
      battle('Angkor taken again',
             'Ramesuan, now king, took Angkor again around 1394, the chronicles say, carrying off thousands of '
             'captives and setting a son on the Khmer throne. Once more the Khmer drove the Siamese out, but province '
             'after province was slipping away.',
             y=1394, at='angkor'),
      battle('The sack of Angkor',
             'In 1431 King Borommarachathirat II of Ayutthaya besieged Angkor for months and took it. Its treasures, '
             'its Brahmin priests and dancers and many of its people were carried off to Ayutthaya, where Khmer court '
             'culture shaped the ceremonies of the Siamese kings for centuries.',
             y=1431, at='angkor'),
      turn('Angkor abandoned',
           'The Khmer king, Ponhea Yat, judged Angkor too close to the Siamese, and moved his court south-east, in the '
           'end to Phnom Penh, where the Mekong and the Tonle Sap rivers meet. The temples of Angkor were left to the '
           'monks and the jungle.',
           y=1434, at='phnom_penh'),
      tale('A lost city',
           'Angkor was never quite forgotten: Buddhist monks kept Angkor Wat as a holy place. But when a French '
           'explorer, Henri Mouhot, described the ruins in the 1860s, Europeans thought they had found a lost city in '
           'the jungle, and Angkor became famous around the world.',
           y=1860, at='angkor'),
      legacy('Ayutthaya was the leading power of mainland Southeast Asia for four centuries, until the Burmese '
             'destroyed it in 1767. Cambodia, squeezed between Siam and Vietnam, never regained its old power, but '
             'Angkor Wat stands at the centre of its national flag.',
             'Ayutthaya was founded in 1351',
             'Angkor fell in 1431',
             'The Khmer moved to Phnom Penh'),
      war='siamese-khmer-wars', wiki='Angkor', img='Angkor Wat', at='angkor')

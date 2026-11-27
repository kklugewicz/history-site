from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('zhou-conquest-of-shang', 'The Zhou conquest of the Shang', 'conquest', (-1050, -1039),
      'A western people overthrew China\'s first great dynasty, and said that Heaven had chosen them to rule.',
      scene('The Shang',
            'For centuries the Shang kings ruled the plain of the Yellow River. At their last capital, near today\'s '
            'Anyang, they wrote questions to their ancestors on turtle shells and ox bones, the oldest Chinese writing '
            'we have, and honoured them with offerings of bronze, wine and human sacrifice.',
            kick='How it began', y=-1100, at='anyang'),
      figure('king-wu-of-zhou', 'The rising in the west',
             'In the Wei valley to the west, the Zhou grew strong under King Wen. His son, King Wu, gathered allies '
             'against the last Shang king, Di Xin, at the ford of Mengjin on the Yellow River, and in about 1046 BC '
             'led them east.',
             y=-1048),
      tale('Wine and meat',
           'Later writers said that Di Xin dug a lake of wine and hung meat from the trees, so that his guests could '
           'feast as they chased each other naked, and that he roasted his critics on a burning bronze pillar. The '
           'tales were told by the winners, and may be mostly legend.',
           y=-1050),
      battle('Muye',
             'King Wu\'s army met the Shang host at Muye, south of the Shang capital. The Shang army was far larger, '
             'but many of its soldiers, it is said, turned their spears around and joined the Zhou. Di Xin fled to his '
             'palace, put on his robes of jade, and burned himself to death.',
             y=-1046, at='muye'),
      turn('The Mandate of Heaven',
           'To explain their right to rule, the Zhou taught that Heaven gives its mandate to a just ruler, and takes '
           'it away from a wicked one. The idea lasted three thousand years: every new dynasty in China claimed the '
           'Mandate, and floods, famines and revolts were read as signs that it had been lost.',
           y=-1046),
      scene('The Duke of Zhou',
            'King Wu died a few years later, leaving a boy king. His brother, the Duke of Zhou, ruled for him, crushed '
            'a revolt by Shang loyalists and his own brothers, and then, it is said, handed power back when the king '
            'came of age. Confucius later held him up as the perfect minister.',
            y=-1042),
      legacy('The Zhou dynasty lasted almost 800 years, longer than any other in Chinese history. The idea it gave '
             'China, that a ruler\'s right to rule depends on ruling well, became the backbone of Chinese political '
             'thought, and the Shang were remembered as a warning.',
             'The battle of Muye, about 1046 BC',
             'It gave China the Mandate of Heaven',
             'The Zhou ruled for almost 800 years'),
      war='zhou-conquest-of-shang', wiki='Battle of Muye', at='muye')

event('maccabean-revolt', 'The Maccabean Revolt', 'uprising', (-167, -160),
      'When a Greek king banned the Jewish faith, a priest and his sons rose up and won back the Temple of Jerusalem.',
      scene('A Greek king',
            'Judea was ruled by the Seleucids, Greek kings descended from one of Alexander\'s generals. In 167 BC King '
            'Antiochus IV, who called himself Epiphanes, God made manifest, banned Jewish practices, from circumcision '
            'to keeping the Sabbath, and set up an altar to Zeus in the Temple in Jerusalem.',
            kick='How it began', y=-167, at='jerusalem'),
      scene('Modiin',
            'In the village of Modiin an old priest, Mattathias, was ordered to make a sacrifice to the Greek gods. '
            'He refused, and when another Jew stepped forward to do it, Mattathias killed him and the king\'s officer, '
            'and fled to the hills with his five sons.',
            y=-167, at='modiin'),
      battle('Judah the Hammer',
             'When Mattathias died, his son Judah took command. He was called Maccabee, probably meaning the hammer. '
             'With bands of fighters who knew the hills, he ambushed and beat one Seleucid army after another, at Beth '
             'Horon and at Emmaus.',
             y=-166),
      turn('The Temple',
           'In 164 BC Judah\'s men took back Jerusalem. They cleansed the Temple and dedicated it again, with eight '
           'days of celebration. Jews have marked it ever since as Hanukkah, which means dedication. A later tradition '
           'tells of a single jar of pure oil that burned for all eight days.',
           y=-164, at='jerusalem'),
      battle('The elephant',
             'The war went on. At Beth Zechariah the Seleucids came with war elephants, and Judah\'s brother Eleazar '
             'ran beneath the largest, thinking it carried the king, and stabbed it in the belly; it fell and crushed '
             'him. In 160 BC Judah himself was killed in battle at Elasa.',
             y=-162),
      legacy('Judah\'s brothers fought on and won full independence. Their family, the Hasmoneans, ruled Judea as '
             'priests and kings for about a century, until Rome took over. The revolt is one of the first wars on '
             'record fought for freedom of religion, and every winter Jews light the Hanukkah candles in its memory.',
             'A revolt against a ban on Judaism',
             'The Temple was dedicated again in 164 BC',
             'Remembered every year at Hanukkah'),
      war='maccabean-revolt', wiki='Maccabean Revolt', at='jerusalem')

event('charlemagne-wars', 'Charlemagne\'s wars', 'conquest', (772, 814),
      'The king of the Franks went to war almost every summer for forty years, and built an empire across western Europe.',
      scene('The summer campaigns',
            'Each spring the Franks held a great assembly, and each summer their king, Charles, called Charlemagne, '
            'Charles the Great, led his army out to war. In 46 years as king he fought more than fifty campaigns: '
            'against the Saxons, the Lombards, the Moors of Spain, the Bretons, the Avars and the Danes.',
            kick='How it began', y=772, at='aachen'),
      battle('The Saxon wars',
             'The pagan Saxons, in the forests of northern Germany, were the hardest enemy. In 772 Charlemagne cut down '
             'their sacred tree, the Irminsul. For thirty years they rose again and again, led for a time by a '
             'chieftain named Widukind, and Saxons were made to be baptised, on pain of death.',
             y=772),
      cost('Verden',
           'In 782 the Saxons wiped out a Frankish army. Charlemagne took his revenge at Verden, where, the royal '
           'annals say, 4,500 Saxon prisoners were beheaded in a single day. Widukind finally gave up and was baptised '
           'in 785, with Charlemagne as his godfather.',
           num='4,500', of='Saxons beheaded in a day, the annals say', y=782, at='verden'),
      turn('King of the Lombards',
           'In 773 the pope begged for help against the Lombards, who ruled northern Italy. Charlemagne crossed the '
           'Alps, besieged their capital, Pavia, through the winter, and in 774 made himself king of the Lombards. He '
           'sent their king to end his days in a monastery.',
           y=774, at='pavia'),
      tale('Roland',
           'In 778, coming back from Spain, the rear of Charlemagne\'s army was ambushed by Basques in the mountain '
           'pass of Roncevaux, and every man was killed, among them a lord named Roland. Three centuries later The '
           'Song of Roland turned it into a heroic last stand against a Muslim army.',
           y=778, at='roncevaux'),
      battle('The Avar treasure',
             'The Avars, horsemen from the steppe, held the plain of Hungary inside great ring-shaped fortresses. In '
             '795 and 796 the Franks broke into their main ring and carried off its treasure, two centuries of plunder '
             'and tribute, said to have filled fifteen wagons drawn by oxen. The Avars never recovered.',
             y=796),
      figure('charlemagne', 'Emperor',
             'On Christmas Day 800, in St Peter\'s in Rome, Pope Leo III set a crown on Charlemagne\'s head and hailed '
             'him as emperor, the first in the West for over three hundred years. His wars had united most of western '
             'Christendom, from northern Spain to the Elbe.',
             y=800, at='rome'),
      legacy('Charlemagne\'s empire was split among his grandsons in 843, and its western and eastern parts grew into '
             'France and Germany. His wars carried Christianity into Saxony, and his idea of a Christian empire in the '
             'West lived on in the Holy Roman Empire for a thousand years.',
             'More than fifty campaigns in 46 years',
             'Crowned emperor in Rome in 800',
             'His empire was the seed of France and Germany'),
      war='charlemagne-wars', wiki='Carolingian Empire', img='Charlemagne', at='aachen')

event('basil-ii-bulgarian-wars', 'Basil II and the Bulgarians', 'war', (976, 1018),
      'A Byzantine emperor spent forty years destroying the Bulgarian empire, and earned the name Bulgar-slayer.',
      scene('Two empires',
            'In the tenth century the Bulgarians ruled a great Christian empire across the Balkans, the rival of '
            'Byzantium. When the young emperor Basil II came to the throne in Constantinople, a Bulgarian noble, '
            'Samuel, led a rising that won back most of the Bulgarian lands, and made his capital at Ohrid.',
            kick='How it began', y=976, at='ohrid'),
      battle('Trajan\'s Gate',
             'In 986 Basil marched on Bulgaria himself. On the way home his army was ambushed in a mountain pass called '
             'Trajan\'s Gate and cut to pieces, and Basil barely escaped. It was a humiliation he never forgot.',
             y=986, at='trajans_gate'),
      figure('basil-ii', 'The soldier emperor',
             'Basil grew into a grim, tireless soldier. He never married, ate little, wore plain dark clothes, and '
             'spent his life on campaign with his men. From 1001 he invaded Bulgaria almost every year, taking its '
             'fortresses one by one.',
             y=1001),
      cost('Kleidion',
           'In July 1014 Basil trapped Samuel\'s army in the pass of Kleidion. The story goes that he had the prisoners '
           'blinded, leaving one man in every hundred one eye to lead the rest home. When Samuel saw them, he '
           'collapsed, and died two days later. The numbers may be exaggerated, but the story made Basil famous.',
           num='15,000', of='prisoners blinded, the story goes', y=1014, at='kleidion'),
      turn('The end of Bulgaria',
           'Without Samuel, Bulgaria fell apart. In 1018 its last rulers surrendered, and Basil entered Ohrid in '
           'triumph, master of the Balkans from the Danube to the Adriatic. Then he went to Athens and gave thanks in '
           'the Parthenon, by then a church of the Virgin Mary.',
           y=1018, at='ohrid'),
      legacy('Basil was later called Boulgaroktonos, the Bulgar-slayer. He left Byzantium at the height of its power, '
             'with a full treasury. But Bulgaria rose again in 1185, and Bulgarians remember Samuel as a hero.',
             'Forty years of war against Bulgaria',
             'The blinding after Kleidion, 1014',
             'Byzantium at the height of its power'),
      war='basil-ii-bulgarian-wars', wiki='Byzantine conquest of Bulgaria', at='ohrid')

event('seljuk-conquests', 'The Seljuk conquests', 'conquest', (1037, 1092),
      'Turkish nomads swept from the steppe to Baghdad, broke Byzantium at Manzikert, and opened Anatolia to the Turks.',
      scene('Out of the steppe',
            'The Seljuks were a clan of Oghuz Turks, herders and horse archers from the steppe east of the Caspian Sea, '
            'who had become Muslims. Led by two brothers, Tughril and Chaghri, they moved into Khorasan, and in 1040 at '
            'Dandanaqan they routed the army of the Ghaznavid sultan and its war elephants.',
            kick='How it began', y=1040, at='dandanaqan'),
      turn('Sultan in Baghdad',
           'Tughril took Persia city by city, and in 1055 he entered Baghdad, home of the caliph, the spiritual head of '
           'Sunni Muslims, who had long been under the thumb of the Shia Buyid dynasty. The caliph named him sultan, '
           'and the Turks became the sword of Sunni Islam.',
           y=1055, at='baghdad'),
      figure('alp-arslan', 'Manzikert',
             'In 1071 Tughril\'s nephew, Alp Arslan, met the Byzantine emperor Romanos IV Diogenes at Manzikert, in '
             'eastern Anatolia. Part of the Byzantine army deserted or held back, and the Turks\' horse archers '
             'surrounded the rest. Romanos was captured, the first Byzantine emperor ever taken prisoner by a Muslim '
             'ruler.',
             y=1071, at='manzikert'),
      tale('The emperor in chains',
           'Romanos was brought before Alp Arslan, who asked him what he would have done if their places were '
           'reversed. Perhaps killed you, or paraded you through the streets of Constantinople, said Romanos. My '
           'punishment is far heavier, the sultan replied: I forgive you, and set you free.',
           y=1071, at='manzikert'),
      scene('Into Anatolia',
            'Romanos was overthrown and blinded by his rivals at home, and Byzantium fell into civil war. Turkish bands '
            'poured into Anatolia, and within a few years they had reached the Aegean. A branch of the Seljuks founded '
            'the Sultanate of Rum there, Rum meaning Rome, with its capital at Nicaea and later Konya.',
            y=1081, at='nicaea'),
      turn('A cry for help',
           'Under Malik Shah, sultan from 1072 to 1092, the empire stretched from Central Asia to the Mediterranean, '
           'run by a brilliant Persian minister, Nizam al-Mulk, who founded colleges across it. In 1095 the Byzantine '
           'emperor asked the pope for help against the Turks, and the answer was the First Crusade.',
           y=1092, at='isfahan'),
      legacy('The Seljuks brought the Turks into the heart of the Islamic world, where Turkish soldiers and dynasties '
             'would rule for centuries. They made Anatolia Turkish, set off the Crusades, and left mosques and '
             'caravanserais that still stand.',
             'Took Baghdad in 1055',
             'Beat Byzantium at Manzikert in 1071',
             'Opened Anatolia to the Turks'),
      war='seljuk-conquests', wiki='Seljuk Empire', at='manzikert')

event('timur-conquests', 'Timur\'s conquests', 'conquest', (1370, 1405),
      'From Samarkand a lame warlord led his armies from Delhi to Damascus, leaving towers of skulls behind him.',
      figure('timur', 'Lord of Samarkand',
             'Timur was born near Samarkand into a Turkic-Mongol clan. Wounds in his youth left him lame in his right '
             'leg and arm, and his enemies called him Timur the Lame, Tamerlane. By 1370 he was master of the lands '
             'around Samarkand, ruling in the name of puppet khans descended from Genghis Khan.',
             kick='How it began', y=1370, at='samarkand'),
      battle('Persia and the Golden Horde',
             'Through the 1380s his armies swept over Persia, and cities that resisted were destroyed. When Isfahan '
             'rose against his garrison in 1387, his soldiers were ordered to bring in heads; a chronicler counted '
             '70,000, piled into towers. Then he turned north and broke the Golden Horde, the Mongol khanate of the '
             'Russian steppe.',
             y=1387, at='isfahan'),
      cost('The sack of Delhi',
           'In 1398 Timur invaded India. Before the battle for Delhi he ordered his men to kill their Indian captives, '
           'fearing they would rise during the fight. He took the city, and for days his troops plundered and '
           'slaughtered. He left with elephants, treasure and craftsmen, and Delhi took a century to recover.',
           num='100,000', of='captives killed before Delhi, it is said', y=1398, at='delhi'),
      battle('Damascus and Baghdad',
             'In 1400 and 1401 he turned west, beat the Mamluks of Egypt, and sacked Aleppo and Damascus. Outside '
             'Damascus he talked for weeks with the great historian Ibn Khaldun, who had been let down the city wall on '
             'ropes to meet him. In Baghdad, which dared to resist, each soldier was ordered to bring back two heads.',
             y=1401, at='damascus'),
      battle('Ankara',
             'In 1402 he met the Ottoman sultan Bayezid I, called the Thunderbolt, near Ankara. Bayezid\'s Tatar troops '
             'changed sides and his army broke. Bayezid was taken prisoner and died months later; later tales said he '
             'was carried about in an iron cage. The young Ottoman state almost fell apart.',
             y=1402, at='ankara'),
      turn('The last campaign',
           'In the winter of 1404 Timur, nearly seventy, set out to conquer Ming China. He fell ill on the march and '
           'died at Otrar in February 1405. His empire split among his sons and grandsons, but they ruled Central Asia '
           'for a century, and one of his descendants, Babur, founded the Mughal Empire in India.',
           y=1405, at='otrar'),
      legacy('Timur\'s wars may have killed 17 million people, one in twenty of everyone alive, though such figures '
             'are guesses. He was also a patron of builders and scholars, who made Samarkand one of the most beautiful '
             'cities in the world, with blue-tiled domes that still stand.',
             'From Delhi to Damascus in thirty-five years',
             'He beat the Ottomans at Ankara in 1402',
             'He made Samarkand a jewel of Asia'),
      war='timur-conquests', wiki='Timurid conquests and invasions', at='samarkand')

event('hussite-wars', 'The Hussite Wars', 'war', (1419, 1434),
      'After the church burned their preacher Jan Hus, the Czechs beat five crusades with farm wagons and peasant armies.',
      figure('jan-hus', 'The preacher',
             'Jan Hus, a priest in Prague, preached in Czech, not Latin, and attacked the wealth and corruption of the '
             'church. Summoned to a church council at Constance with a promise of safe conduct, he was arrested, tried '
             'for heresy, and burned at the stake in 1415. In Bohemia he became a martyr.',
             kick='How it began', y=1415, at='konstanz', where='Constance'),
      turn('Out of the window',
           'On 30 July 1419 a crowd of Hussites marched on Prague\'s New Town Hall to free prisoners, and threw the '
           'councillors out of the windows, killing several of them: the first defenestration of Prague. The king died '
           'weeks later, and Bohemia rose in revolt.',
           y=1419, at='prague'),
      figure('jan-zizka', 'The blind general',
             'The Hussites\' general, Jan Žižka, had lost one eye in his youth, and lost the other in battle. He turned '
             'farm wagons into moving forts, chained together and packed with crossbowmen and men with early handguns, '
             'and he never lost a battle. His peasant armies beat the knights of Europe.',
             y=1420, at='prague'),
      battle('Five crusades',
             'The emperor Sigismund and the pope sent five crusades against the Hussites between 1420 and 1431, and '
             'every one failed. At Domažlice in 1431, it is said, the crusaders ran as soon as they heard the Hussites '
             'singing their battle hymn as they came: You who are the warriors of God.',
             y=1431, at='domazlice'),
      tale('The pistol',
           'The Hussites called their handguns píšťala, a Czech word for a pipe or whistle. The word travelled into '
           'German and other languages, and is probably where the word pistol comes from.',
           y=1425),
      turn('Lipany',
           'In the end the Hussites split. Moderates made peace with the church, which allowed them to take '
           'communion with the cup as well as the bread. In 1434 they joined Catholic lords to crush the radicals at '
           'Lipany, and two years later Sigismund was accepted as king.',
           y=1434, at='lipany'),
      legacy('The Hussites broke with Rome a century before Luther, and their church lasted two hundred years. Luther '
             'later said: we are all Hussites without knowing it. A statue of Hus stands in Prague\'s Old Town Square, '
             'and 6 July, the day he died, is a national holiday.',
             'Jan Hus was burned at the stake in 1415',
             'Five crusades were beaten by peasant armies',
             'A century before the Reformation'),
      war='hussite-wars', wiki='Hussite Wars', at='prague')

event('italian-wars', 'The Italian Wars', 'wars', (1494, 1559),
      'For sixty-five years the kings of France and Spain fought over Italy, as the Renaissance flowered around them.',
      figure('charles-viii-of-france', 'A king comes south',
             'In 1494 the young king of France, Charles VIII, crossed the Alps with an army of 25,000 and a train of '
             'new bronze cannon, to claim the kingdom of Naples. The Italian states, used to small wars fought by hired '
             'captains, could not stop him, and he rode into Naples in February 1495.',
             kick='How it began', y=1494, at='naples'),
      scene('A new kind of war',
            'His cannon smashed in hours walls that had held out for months. Italy became the training ground of '
            'Europe: Swiss pikemen, Spanish soldiers with arquebuses, German landsknechts in slashed and puffed '
            'clothes, and new star-shaped forts built to stand up to cannon fire.',
            y=1500),
      work('The Prince',
           'Watching the chaos as a diplomat of Florence, Niccolò Machiavelli wrote The Prince, a handbook on how a '
           'ruler wins and keeps power, by force and cunning if need be. He held up as a model Cesare Borgia, the '
           'pope\'s son, who had carved out a state for himself in these wars.',
           y=1513, at='florence'),
      figure('francis-i-of-france', 'Pavia',
             'The French king Francis I won a great victory at Marignano in 1515. But at Pavia in 1525 the army of the '
             'emperor Charles V, who was also king of Spain, cut down his knights with arquebus fire, and Francis was '
             'taken prisoner. He wrote to his mother that all was lost except his honour and his life.',
             y=1525, at='pavia'),
      cost('The sack of Rome',
           'In May 1527 Charles\'s unpaid army, many of them German Lutherans, mutinied and stormed Rome. For months '
           'they looted, tortured and killed. The pope\'s Swiss Guards held the steps of St Peter\'s long enough for '
           'Clement VII to flee to his castle; new guards still swear their oath on that day, 6 May.',
           num='147', of='of 189 Swiss Guards died saving the pope', y=1527, at='rome'),
      turn('Peace at last',
           'The wars dragged on, with France even allying with the Ottoman Turks. In 1559 France and Spain made peace '
           'at Cateau-Cambrésis, leaving Spain master of Milan, Naples and Sicily. At a tournament held to celebrate, '
           'a splinter from a lance pierced the eye of the French king, Henry II, and he died.',
           y=1559, at='cateau_cambresis', where='Cateau-Cambrésis'),
      legacy('The wars left Spain master of Italy for 150 years, and taught Europe a new way of war. They also spread '
             'the Renaissance: kings who came to fight went home with Italian painters, builders and ideas. Francis I '
             'brought Leonardo da Vinci to France, where he died.',
             'France and Spain fought over Italy for 65 years',
             'Rome was sacked in 1527',
             'Spain won Milan, Naples and Sicily'),
      war='italian-wars', wiki='Italian Wars', at='pavia')

event('french-wars-of-religion', 'The French Wars of Religion', 'civil-war', (1562, 1598),
      'Catholics and Protestants fought eight civil wars for France, until a Protestant king turned Catholic to make peace.',
      scene('Huguenots',
            'By 1560 perhaps one French person in ten had become a Protestant, a Huguenot, following the teaching of '
            'John Calvin, among them many nobles. The king was a boy, and his mother tried to keep the peace between '
            'the two faiths. In 1562 the Duke of Guise\'s men massacred Protestants at worship in a barn at Wassy, and '
            'war broke out.',
            kick='How it began', y=1562, at='wassy'),
      figure('catherine-de-medici', 'A royal wedding',
             'The queen mother, Catherine de\' Medici, tried everything: edicts of toleration, peace treaties, and a '
             'royal wedding. In August 1572 her daughter Margaret married the young Protestant Henry of Navarre in '
             'Paris, and the Huguenot nobility crowded into the city for the celebrations.',
             y=1572, at='paris'),
      cost('St Bartholomew\'s Day',
           'Days after the wedding someone shot and wounded the Huguenot leader, Admiral Coligny. Fearing revenge, the '
           'king and his mother agreed to strike first. Before dawn on 24 August Coligny was murdered, and Paris mobs '
           'hunted down Protestants through the streets. The killing spread to other cities.',
           num='5,000 to 30,000', of='Protestants killed across France', y=1572, at='paris'),
      scene('The three Henrys',
            'The wars went on, with Spain backing the Catholic League and England the Protestants. In 1588 King Henry '
            'III had his rival, Henry, Duke of Guise, stabbed to death in his castle at Blois; the next year a monk '
            'stabbed the king himself. The heir to the throne was the Protestant Henry of Navarre.',
            y=1588, at='blois'),
      figure('henry-iv-of-france', 'Paris is worth a Mass',
             'Catholic Paris would not accept a Protestant king, and Henry IV fought for years to win it. In 1593 he '
             'became a Catholic. Paris is worth a Mass, he is supposed to have said, though he probably never did. The '
             'city opened its gates to him in 1594.',
             y=1593, at='paris'),
      turn('The Edict of Nantes',
           'In 1598 Henry signed the Edict of Nantes, which let Protestants worship freely in many places, hold office, '
           'and keep their own fortified towns. It was one of the first laws in Europe to let two faiths live side by '
           'side in one kingdom. In 1610 Henry was stabbed to death by a Catholic fanatic.',
           y=1598, at='nantes'),
      legacy('The wars killed perhaps two to four million people, through fighting, hunger and disease. Henry\'s '
             'peace lasted until 1685, when his grandson Louis XIV took back the edict, and some 200,000 Huguenots fled '
             'abroad, taking their skills to England, the Netherlands, Prussia and South Africa.',
             'Eight civil wars from 1562 to 1598',
             'The St Bartholomew\'s Day massacre, 1572',
             'The Edict of Nantes, 1598'),
      war='french-wars-of-religion', wiki='French Wars of Religion', at='paris')

event('war-of-the-spanish-succession', 'The War of the Spanish Succession', 'war', (1701, 1714),
      'When Spain\'s last Habsburg king died childless, Europe went to war to stop France from swallowing his empire.',
      scene('The bewitched king',
            'Charles II of Spain, sickly from birth and called the Bewitched, had no children. When he died in 1700 he '
            'left his whole empire, Spain, much of Italy, the Spanish Netherlands and the Americas, to Philip, the '
            'grandson of Louis XIV of France. England, the Dutch and Austria feared France and Spain would become one '
            'superpower.',
            kick='How it began', y=1700, at='madrid'),
      figure('louis-xiv', 'No more Pyrenees',
             'Louis XIV accepted the will, and his grandson became Philip V of Spain. Now, someone at Versailles is said '
             'to have declared, there are no more Pyrenees. In 1701 England, the Dutch Republic and the Austrian '
             'emperor formed a Grand Alliance against France.',
             y=1701, at='versailles'),
      figure('john-churchill-1st-duke-of-marlborough', 'Blenheim',
             'In 1704 the Duke of Marlborough, England\'s greatest general, marched his army 400 kilometres from the '
             'Low Countries to the Danube, joined Prince Eugene of Savoy, and smashed a French and Bavarian army at '
             'Blenheim, France\'s first great defeat in forty years. A grateful queen gave him a palace, named Blenheim.',
             y=1704, at='blindheim', where='Blenheim, Bavaria'),
      tale('The Rock',
           'Also in 1704 an English and Dutch fleet captured Gibraltar, the rock at the mouth of the Mediterranean. '
           'Britain kept it, and it is still British today, though Spain wants it back.',
           y=1704, at='gibraltar'),
      cost('Malplaquet',
           'The war spread from Spain to Italy, Germany, the Low Countries and the Americas. At Malplaquet in 1709, '
           'the bloodiest battle of the century, the allies won but lost twice as many men as the French. France itself '
           'was starving after the great frost of that winter.',
           num='About 35,000', of='killed or wounded in one day', y=1709, at='malplaquet'),
      turn('Utrecht',
           'In 1711 the Habsburg claimant to Spain became emperor, and his allies had no wish to see him rule Spain '
           'too. By the peace of 1713 and 1714 Philip kept Spain and its colonies but gave up any claim to France, '
           'Austria took Spain\'s lands in Italy and the Netherlands, and Britain won Gibraltar, Minorca and the right '
           'to sell enslaved Africans in Spanish America.',
           y=1713, at='utrecht'),
      legacy('The war kept France and Spain apart, and set up a balance of power that shaped Europe for a century. '
             'Philip\'s Bourbon family still holds the Spanish throne. Britain came out as a great naval and trading '
             'power, on its way to ruling the waves.',
             'Europe fought to keep France and Spain apart',
             'Marlborough\'s victory at Blenheim, 1704',
             'Britain won Gibraltar'),
      war='war-of-the-spanish-succession', wiki='War of the Spanish Succession', at='blindheim',
      where='Blenheim, Bavaria')

event('afghan-maratha-war', 'The Third Battle of Panipat', 'battle', (1758, 1761),
      'The Marathas, masters of India, met the Afghan king at Panipat, in one of the bloodiest battles of the century.',
      scene('To the Indus',
            'As the Mughal Empire crumbled, the Marathas of western India became the strongest power in the land. By '
            '1758 their horsemen had reached Lahore and the river Indus, and the Mughal emperor in Delhi was in their '
            'hands.',
            kick='How it began', y=1758, at='lahore'),
      figure('ahmad-shah-durrani', 'The Afghan king',
             'Ahmad Shah Durrani had founded the kingdom of Afghanistan in 1747, and had already raided India several '
             'times, sacking Delhi in 1757. He would not let the Marathas keep the Punjab. In 1759 he came down through '
             'the passes again, and Muslim princes of India, the Rohillas and the nawab of Awadh, joined him.',
             y=1759, at='kandahar'),
      scene('Two months of waiting',
            'The Marathas sent a great army north under Sadashivrao Bhau, with cannon trained in the French style, and '
            'tens of thousands of pilgrims and camp followers came with it. The two armies dug in facing each other '
            'near Panipat, north of Delhi, and for two months they waited, while food in the Maratha camp ran out.',
            y=1760, at='panipat'),
      cost('Panipat',
           'On 14 January 1761 the starving Marathas attacked. Their guns tore holes in the Afghan lines, but in the '
           'afternoon Durrani threw in his reserves, and the Maratha army broke. Bhau was killed. The next day '
           'thousands of prisoners were massacred, and camp followers who could not escape were killed or enslaved.',
           num='Tens of thousands', of='killed in one of history\'s bloodiest days', y=1761, at='panipat'),
      turn('A victory without a prize',
           'Durrani\'s soldiers, unpaid for two years, wanted to go home, and he went back to Afghanistan without '
           'taking the Mughal throne. Within ten years the Marathas were strong again in the north. But the battle had '
           'weakened both of India\'s great powers, and the British, gaining ground in Bengal, were the real winners.',
           y=1761),
      legacy('Panipat became a byword in India for disaster. It ended the Marathas\' hopes of ruling all India, and '
             'cleared the way for the British East India Company. In Afghanistan Ahmad Shah is remembered as Ahmad '
             'Shah Baba, the father of the nation.',
             'The battle of 14 January 1761',
             'One of the bloodiest days of the century',
             'It opened the way for British rule in India'),
      states=('Afghanistan', 'Maratha Confederacy', 'Mughal Empire'), war='afghan-maratha-war',
      wiki='Third Battle of Panipat', at='panipat')

event('tupac-amaru-ii-rebellion', 'The rising of Túpac Amaru II', 'uprising', (1780, 1782),
      'A descendant of the last Inca ruler led the peoples of the Andes in a great rising against Spanish rule.',
      scene('The mita',
            'Two and a half centuries after the conquest, the native peoples of the Andes were still forced to work in '
            'the silver mines of Potosí under the mita, a labour draft that sent many to their deaths, and to buy goods '
            'at high prices from Spanish officials, the corregidores. New taxes in the 1770s made things worse.',
            kick='How it began', y=1779, at='potosi'),
      figure('tupac-amaru-ii', 'Túpac Amaru II',
             'José Gabriel Condorcanqui, a wealthy mule-train owner and local chief, was descended from Túpac Amaru, '
             'the last Inca ruler, executed by the Spanish in 1572, and took the name Túpac Amaru II. On 4 November '
             '1780 his men seized the hated corregidor Antonio de Arriaga, and six days later hanged him.',
             y=1780, at='tinta'),
      scene('Micaela Bastidas',
            'His wife, Micaela Bastidas, ran the rebels\' supplies and recruiting, and urged him to strike at Cusco '
            'before the Spanish could gather their forces. He waited. By the time tens of thousands of rebels laid '
            'siege to the old Inca capital in January 1781, it had been reinforced, and the siege failed.',
            y=1781, at='cuzco'),
      turn('The execution',
           'In April 1781 Túpac Amaru was betrayed and captured. On 18 May, in the main square of Cusco, he was made to '
           'watch the execution of his wife and son. Then his tongue was cut out, and horses were tied to his arms and '
           'legs to tear him apart. When they failed, he was beheaded.',
           y=1781, at='cuzco'),
      battle('The siege of La Paz',
             'The rising went on. In the south an Aymara leader, Túpac Katari, besieged La Paz for months in 1781, and '
             'thousands inside died of hunger. He too was captured and torn apart by horses. Before he died, he is '
             'remembered as saying: I will return, and I will be millions.',
             y=1781, at='la_paz'),
      cost('The reckoning',
           'By the time the last rebels gave up in 1782, perhaps 100,000 people had died, most of them native Andeans. '
           'Spain banned the titles and dress of the Inca nobility, and even the Quechua plays that told of the Incas.',
           num='About 100,000', of='died in the rising and its crushing', y=1782),
      legacy('The rising failed, but it was the greatest revolt in Spain\'s American empire before the wars of '
             'independence forty years later. Túpac Amaru became a symbol of resistance across Latin America, and the '
             'name of the Inca rebel lives on in Peru and beyond.',
             'Began on 4 November 1780',
             'The greatest revolt against Spain\'s empire',
             'A symbol of resistance in the Andes'),
      states=('Viceroyalty of the Río de la Plata',), war='tupac-amaru-ii-rebellion',
      wiki='Rebellion of Túpac Amaru II', at='cuzco')

event('french-revolutionary-wars', 'The French Revolutionary Wars', 'wars', (1792, 1802),
      'The kings of Europe went to war to crush the French Revolution, and a nation in arms threw them back.',
      scene('The Revolution in danger',
            'In April 1792 revolutionary France declared war on Austria, home of the French queen, Marie Antoinette. '
            'Prussia joined Austria, and its commander warned that Paris would be destroyed if the royal family were '
            'harmed. Instead, the threat helped to topple the king.',
            kick='How it began', y=1792, at='paris'),
      song('La Marseillaise',
           'That April an army officer, Rouget de Lisle, wrote a war song for the Army of the Rhine in Strasbourg. '
           'Volunteers from Marseille sang it as they marched into Paris that summer, and it took their name. In 1795 '
           'it became the national anthem of France.',
           page='La Marseillaise', y=1792, at='strasbourg'),
      battle('Valmy',
             'On 20 September 1792, at Valmy, the raw volunteers of the new French army stood firm under Prussian '
             'cannon fire, shouting long live the nation, and the Prussians turned back. The next day France became a '
             'republic. The German poet Goethe, who was there, said that a new age of history had begun.',
             y=1792, at='valmy'),
      turn('The nation in arms',
           'In 1793, with enemies on every border and revolts at home, the Republic ordered the levée en masse: every '
           'unmarried man from 18 to 25 was called up, and everyone else had a task, from making weapons to tearing old '
           'linen into bandages. France raised armies of about 800,000, the largest Europe had ever seen.',
           y=1793),
      figure('napoleon', 'Bonaparte in Italy',
             'In 1796 a 26-year-old general, Napoleon Bonaparte, took command of a hungry, ragged army in Italy. In a '
             'year of lightning marches he beat the Austrians again and again, at Lodi, Arcole and Rivoli, and forced '
             'them to make peace. He sent home gold, and paintings and statues taken from Italy\'s churches and palaces.',
             y=1796, at='rivoli'),
      battle('Egypt',
             'In 1798 Bonaparte sailed to Egypt, to strike at Britain\'s route to India. He beat the Mamluks in sight of '
             'the pyramids, but Admiral Nelson destroyed his fleet at the Battle of the Nile, trapping his army. Scholars '
             'who came with him studied Egypt\'s past, and his soldiers found the Rosetta Stone, the key to reading '
             'hieroglyphs.',
             y=1798, at='giza'),
      turn('Marengo and peace',
           'Bonaparte slipped back to France in 1799 and seized power as First Consul. In 1800 he crossed the Alps and '
           'beat the Austrians at Marengo, while another French army won at Hohenlinden. Austria made peace, and in '
           '1802 even Britain signed the Peace of Amiens. It lasted fourteen months.',
           y=1800, at='marengo'),
      legacy('The wars carried the ideas of the Revolution, equality before the law and the nation as the source of '
             'power, across Europe, along with French armies and looting. They made Napoleon, and led straight into his '
             'wars. The nation in arms became the model for the wars of the next 150 years.',
             'Valmy saved the Revolution in 1792',
             'The nation in arms',
             'They made Napoleon'),
      war='french-revolutionary-wars', wiki='French Revolutionary Wars', at='valmy')

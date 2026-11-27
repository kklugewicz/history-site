from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('columbus-first-voyage', "Columbus's first voyage", 'voyage', (1492, 1493),
      'Three small ships sailed west to find Asia and found a world Europe did not know.',
      scene('A plan to sail west',
            'Christopher Columbus, a sailor from Genoa, was sure that Asia lay only about 4,000 km west of Europe. He had '
            'shrunk the Earth and stretched Asia: the real distance to Japan is nearer 20,000 km. Experts in Portugal and '
            'in Spain turned him down, because they thought his numbers were wrong. They were right.',
            kick='How it began', img='Erdapfel', cap='The oldest globe that survives, made in 1492, has no Americas on it'),
      figure('isabella-i-of-castile', 'A yes at Santa Fe',
             'In January 1492 Granada, the last Muslim kingdom in Spain, surrendered. At the royal camp of Santa Fe, Queen '
             'Isabella and King Ferdinand at last agreed to back him. If he found land, he would be its governor, Admiral '
             'of the Ocean Sea, and keep a tenth of its riches.',
             y=1492, at='santa_fe_gr'),
      scene('Three small ships',
            'The Niña, the Pinta and the larger Santa María left Palos on 3 August 1492 with about 90 men. After repairs in '
            'the Canary Islands they sailed west on 6 September, into an ocean no one they knew had crossed, pushed by the '
            'steady trade winds.',
            img='Santa María (ship)', cap='A replica of the Santa María', y=1492, at='palos'),
      tale('Two logbooks',
           'Columbus kept two counts of how far they had sailed, it is said: a true one for himself and a shorter one for '
           'the crew, so they would not panic at how far they were from home. The joke is that the false count was closer '
           'to the truth. By 10 October the men were close to mutiny, and he promised to turn back if no land was seen '
           'within days.',
           y=1492),
      turn('Land!',
           'At 2 in the morning on 12 October a lookout on the Pinta, Rodrigo de Triana, saw white cliffs in the moonlight '
           'and shouted "Tierra!" Columbus claimed the reward for himself, saying he had seen a light the night before. '
           'They landed on an island of the Bahamas its people called Guanahani. Columbus named it San Salvador.',
           img='Landing of Columbus', cap='The landing, as John Vanderlyn painted it in 1847', y=1492, at='guanahani'),
      scene('The Taíno',
            'The islanders were Taíno, farmers and fishers who welcomed the strangers with gifts. Our words hammock, canoe, '
            'hurricane, barbecue and tobacco come from their language. Columbus wrote that they were gentle, had no iron '
            'weapons and would make good servants, and he took several of them with him as guides.',
            kick='Who they met', img='Taíno', y=1492),
      scene('Looking for the Great Khan',
            'Sure he was off the coast of Asia, Columbus sailed on to Cuba, which he took for part of China, and sent two men '
            'inland with letters for the Great Khan. They found villages, and people smoking rolled leaves. On Hispaniola '
            'the chief Guacanagarí traded gold ornaments, and Columbus was certain great riches lay close by.',
            img='Hispaniola', y=1492, at='hispaniola'),
      tale('Shipwreck on Christmas Eve',
           'On Christmas Eve, with a ship\'s boy at the helm, the Santa María ran onto a reef and broke up. Guacanagarí\'s '
           'people helped save her cargo. Columbus built a fort from her timbers, La Navidad, and left 39 men there. When '
           'he came back the next year, every one of them was dead.',
           y=1492, at='la_navidad'),
      scene('Home through the storms',
            'On the way back, storms nearly sank the Niña. Columbus sealed an account of his voyage in a barrel and threw it '
            'overboard in case they drowned. He reached Lisbon, then Palos on 15 March 1493, and rode in triumph to '
            'Barcelona with parrots, gold and six Taíno to show the king and queen.',
            kick='The return', y=1493, at='barcelona'),
      cost('What came next',
           'He came back that same year with 17 ships and 1,200 men to settle and rule. War, forced labour in the gold '
           'fields and diseases the islanders had never met, above all smallpox, destroyed the Taíno world. Within 50 years '
           'only a few hundred Taíno were left on Hispaniola.',
           num='A few hundred', of='Taíno left on Hispaniola by the 1540s', img='Bartolomé de las Casas',
           cap='Bartolomé de las Casas, the friar who recorded what was done to them', y=1542),
      legacy('Columbus died in 1506 still insisting he had reached Asia. But his voyage joined the two halves of the world '
             'for good. Ships soon carried horses, wheat and smallpox west, and maize, potatoes and tomatoes east, and it '
             'began the conquest of the Americas.',
             'Linked Europe and the Americas for good',
             'Began the exchange of crops, animals and diseases',
             'Opened the way to the conquest of the Americas',
             img='Columbian exchange'),
      states=['Castille', 'Aragón', 'Taino', 'Caribbean hunter-gatherers'],
      wiki='Voyages of Christopher Columbus', img='Landing of Columbus', at='guanahani')

event('wars-of-the-roses', 'The Wars of the Roses', 'civil-war', (1455, 1487),
      "Two branches of England's royal family fought over the crown for thirty years, until a Tudor took it.",
      figure('henry-vi-of-england', 'A king who could not rule',
             'Henry VI became king of England as a baby in 1422. He grew up gentle and pious, but in 1453, as the last '
             'English lands in France were lost, he fell into a stupor and for over a year knew no one, not even his '
             'newborn son. The great lords began to fight over who should rule.',
             kick='How it began', y=1453, at='london'),
      scene('Red rose, white rose',
            'Henry was of the house of Lancaster. His rival, Richard, Duke of York, was descended from an older son of '
            'Edward III. The fighting began at St Albans in 1455. The roses came later: Shakespeare had each side pick a '
            'red or a white rose in a garden, and the Tudors made the two into one badge.',
            y=1455),
      battle('Towton',
             'The bloodiest battle ever fought in England came at Towton, in Yorkshire, on Palm Sunday 1461, in a snowstorm. '
             'Chroniclers said 28,000 died. The Lancastrians broke, and many drowned in a stream as they fled. York\'s son '
             'was crowned Edward IV.',
             y=1461, at='towton'),
      tale('The Kingmaker',
           'The Earl of Warwick, the richest lord in England, helped Edward win his crown, then fell out with him, changed '
           'sides and put Henry VI back on the throne in 1470. People called him the Kingmaker. Edward came back and killed '
           'him at Barnet in 1471, and Henry VI died in the Tower soon after, almost surely murdered.',
           y=1471, at='london'),
      figure('richard-iii-of-england', 'The princes in the Tower',
             'When Edward IV died in 1483, his brother Richard took charge of his sons, aged 12 and 9, and lodged them in '
             'the Tower of London. Then he had them declared illegitimate and took the crown himself as Richard III. The '
             'boys were never seen again.',
             y=1483, at='london'),
      figure('henry-vii-of-england', 'Bosworth',
             'In 1485 Henry Tudor, a Lancastrian exile with Welsh roots, landed in Wales with French help. At Bosworth Field '
             'Richard charged straight at him and was cut down when the powerful Stanley family turned against him. Henry '
             "married Edward IV's daughter, Elizabeth of York, joining the two houses.",
             y=1485, at='bosworth'),
      tale('A king under a car park',
           "Richard III was buried without ceremony in a friary in Leicester, later pulled down. In 2012 archaeologists found "
           'his skeleton under a car park, with a curved spine and wounds to the skull, and DNA from a living relative '
           'proved it was him.',
           img='Exhumation and reburial of Richard III of England', y=2012, at='leicester'),
      work("Shakespeare's history plays",
           'A century later Shakespeare turned the wars into eight plays, ending with Richard III as a hunchbacked villain '
           'who cries: a horse! a horse! my kingdom for a horse! His picture of Richard, written under the Tudors, is still '
           'argued over.',
           img='Richard III (play)', y=1593),
      legacy('The wars ended more than 300 years of Plantagenet kings and began the Tudor age of Henry VIII and Elizabeth I. '
             'The Tudor rose, red and white together, is still a symbol of England.',
             'Lancaster against York, 1455 to 1487',
             'Ended at Bosworth in 1485',
             'Began the Tudor age'),
      war='wars-of-the-roses', wiki='Wars of the Roses', img='Tudor rose')

event('sea-road-to-india', "Portugal's sea road to India", 'voyage', (1488, 1515),
      'Portuguese sailors rounded Africa, reached India by sea and built an empire of forts on the Indian Ocean.',
      scene('Caravels down Africa',
            'From the 1420s Portuguese ships, sent out by Prince Henry, called the Navigator, crept down the coast of Africa '
            'in small, nimble caravels. They were looking for gold, for slaves, and for a way round to the spices of Asia, '
            'which reached Europe only through Muslim and Venetian middlemen.',
            kick='How it began', img='Caravel', y=1420, at='sagres'),
      figure('bartolomeu-dias', 'The Cape of Storms',
             'In 1488 Bartolomeu Dias was blown south by a storm for days. Turning east and finding no land, he sailed north '
             'and landed beyond the tip of Africa. His frightened crew made him turn back. He called it the Cape of Storms, '
             'but the king renamed it the Cape of Good Hope.',
             y=1488, at='cape_good_hope'),
      figure('vasco-da-gama', 'Christians and spices',
             'In 1497 Vasco da Gama swung far out into the Atlantic, rounded the Cape and, with a pilot found at Malindi, '
             'crossed the Indian Ocean on the monsoon winds. In May 1498 he reached Calicut. Asked what they had come for, '
             'his men answered: Christians and spices.',
             y=1498, at='calicut'),
      cost('Scurvy',
           'Of the 170 or so men who sailed with da Gama, only about 55 came home. Most were killed by scurvy, from a lack '
           'of fresh food. Even so, the pepper and spices he brought back paid for the voyage many times over.',
           num='About 55', of='of some 170 men came home', y=1499, at='lisbon'),
      figure('pedro-alvares-cabral', 'Brazil by chance',
             'The next fleet, under Pedro Álvares Cabral, swung so far west in 1500 that it struck an unknown coast: Brazil. '
             'Cabral claimed it for Portugal, sent a ship home with the news and sailed on to India.',
             y=1500),
      battle('Diu',
             'In 1509 a Portuguese fleet with heavy guns destroyed the fleets of the Mamluk sultan of Egypt and of Gujarat '
             'off Diu, in India. For a century no one could match Portuguese guns at sea in the Indian Ocean.',
             y=1509, at='diu'),
      figure('afonso-de-albuquerque', 'Forts on the ocean',
             'Portugal could not conquer India, so it took the sea. Afonso de Albuquerque seized Goa in 1510, Malacca, the '
             'gateway to the spice islands, in 1511, and Hormuz, at the mouth of the Persian Gulf, in 1515. Ships trading '
             'without a Portuguese pass could be sunk.',
             y=1511, at='malacca'),
      legacy('The sea road joined Europe and Asia directly for the first time and began 450 years of European empires in '
             'Asia. Portugal held Goa until 1961 and Macau until 1999, and Portuguese is still spoken in Brazil, Angola and '
             'Mozambique.',
             'Round the Cape of Good Hope in 1488',
             'Da Gama reached India in 1498',
             'Began European empires in Asia'),
      states=['Portugal'], war='portuguese-indian-ocean', wiki='Portuguese discoveries', img='Padrão dos Descobrimentos')

event('first-circumnavigation', 'The first voyage around the world', 'voyage', (1519, 1522),
      'Five ships and some 270 men sailed west for the Spice Islands. Three years later one ship came home.',
      scene('West to the spices',
            'Spain and Portugal had split the newly found world between them in 1494, and the spice-rich Moluccas lay '
            'somewhere on the far side. Ferdinand Magellan, a Portuguese captain serving Spain, promised the young King '
            'Charles to reach them by sailing west, around the Americas. In September 1519 five ships left Spain.',
            kick='How it began', y=1519, at='sanlucar'),
      tale("Pigafetta's diary",
           'Among the crew was a young Italian scholar, Antonio Pigafetta, who paid his own way for the adventure. He wrote '
           'down everything: penguins and sea lions, giants he thought he saw in Patagonia, storms, and the words of the '
           'peoples they met. His diary is the reason we know the story.',
           y=1520),
      figure('ferdinand-magellan', 'The Pacific',
             'In October 1520, after crushing a mutiny, the fleet found a maze of channels at the tip of South America, today '
             'the Strait of Magellan. One ship slipped away and sailed home. When the others came out into a calm ocean, '
             'Magellan named it the Pacific, the peaceful sea.',
             y=1520, at=(-71.0, -53.5), where='Strait of Magellan'),
      scene('The widest ocean',
            'No one knew the Pacific was so wide. For more than three months they crossed it, eating biscuit dust, rats and '
            'leather softened in seawater. Scurvy swelled their gums until they could not eat at all, and 19 men died '
            'before they reached Guam.',
            y=1521),
      battle('Mactan',
             'In the Philippines Magellan won allies and converts, and promised to defeat a chief who refused to submit, '
             'Lapulapu of Mactan. On 27 April 1521 he waded ashore with about 50 men against some 1,500 warriors and was '
             'killed in the shallows. Filipinos honour Lapulapu as the first to resist Europe.',
             img='Lapulapu', y=1521, at='mactan'),
      figure('juan-sebastian-elcano', 'Home the other way',
             'The survivors burned a ship they could no longer crew, reached the Moluccas and loaded cloves. Juan Sebastián '
             'Elcano took the Victoria home westward across the Indian Ocean and round Africa, keeping clear of the '
             'Portuguese, as men died of hunger on the way.',
             y=1522, at='ternate'),
      tale('The lost day',
           'When the Victoria reached the Cape Verde Islands in July 1522, the crew found it was Thursday ashore, though '
           'their logs said Wednesday. Sailing west around the world, they had lost a day: the first sign of what the '
           'international date line deals with today.',
           y=1522),
      cost('Eighteen men',
           'On 6 September 1522 the Victoria limped into Sanlúcar with 18 Europeans aboard. Most of the others had died '
           'of scurvy, hunger, fighting and shipwreck, though a handful came home later.',
           num='18', of='men came home, of about 270', img='Victoria (ship)', y=1522, at='sanlucar'),
      legacy('The voyage proved that all the oceans are joined and showed how big the Earth really is. The cloves in the '
             "Victoria's hold paid for the whole expedition, and a Basque captain, not Magellan, completed the first circle "
             'of the world.',
             'Five ships sailed in 1519, one came back',
             'Crossed the Pacific, far wider than anyone knew',
             'Proved that the oceans are all joined'),
      states=['Spain', 'Castille'], wiki='Magellan expedition', img='Victoria (ship)', at='sanlucar')

event('conquest-of-the-aztecs-and-incas', 'The fall of the Aztecs and the Incas', 'conquest', (1519, 1533),
      'A few hundred Spaniards, their native allies and smallpox brought down the two greatest empires of the Americas.',
      figure('hernan-cortes', 'The ships are sunk',
             'In 1519 Hernán Cortés landed on the coast of Mexico with about 500 men, 16 horses and a few cannon, against '
             'the orders of the governor of Cuba. So that no one could turn back, he had his ships run aground and sunk.',
             kick='How it began', y=1519, at='veracruz'),
      figure('la-malinche', 'The interpreter',
             'A Nahua woman given to the Spaniards as a slave, Malintzin, called La Malinche, spoke both Maya and Nahuatl, '
             "and soon Spanish. She became Cortés's voice and adviser. To some Mexicans her name has stood for betrayal; to "
             'others, for survival.',
             y=1519),
      scene('Allies',
            'Many peoples hated paying tribute to the Mexica. The Tlaxcalans, their old enemies, joined the Spaniards with '
            'thousands of warriors, and others followed. Without them the conquest could never have happened.',
            y=1519, at='tlaxcala'),
      figure('moctezuma-ii', 'Guests in the city',
             'Moctezuma II welcomed the strangers into Tenochtitlan in November 1519. Within days Cortés made him a prisoner '
             'in his own palace. In June 1520 Moctezuma died, stoned by his own people, the Spaniards said, and they fled '
             'the city by night, losing hundreds of men.',
             y=1520, at='tenochtitlan'),
      scene('Smallpox',
            'Then smallpox arrived with a later Spanish expedition. The peoples of Mexico had never met it, and it killed '
            'perhaps half of Tenochtitlan, among them the new emperor, Cuitláhuac. In 1521 Cortés came back with his allies '
            'and took the city after a long siege.',
            y=1520, at='tenochtitlan'),
      figure('cuauhtemoc', 'The last emperor',
             'The last emperor, Cuauhtémoc, led the defence to the end and was captured in August 1521. He was later '
             'tortured for gold and hanged in 1525. Mexico honours him as the hero who would not give in.',
             y=1521, at='tenochtitlan'),
      figure('atahualpa', 'A room of gold',
             'In 1532 Francisco Pizarro, with 168 men, met the Inca emperor Atahualpa at Cajamarca, just after he had won a '
             'civil war against his brother. In a surprise attack the Spaniards killed thousands of his followers and seized '
             'him. Atahualpa offered to fill a room once with gold and twice with silver for his freedom.',
             y=1532, at='cajamarca'),
      turn('Executed',
           'The ransom was paid and melted into bars, and Pizarro had Atahualpa executed anyway in 1533. The Spaniards took '
           'Cusco, the Inca capital. Inca resistance went on in the mountains until 1572, when the last emperor, Túpac '
           'Amaru, was beheaded.',
           y=1533, at='cuzco'),
      cost('The great dying',
           'Within a century most of the native peoples of Mexico and Peru were dead, nine in ten by many estimates. Most '
           'died of new diseases, smallpox, measles and typhus, made worse by war, forced labour and hunger.',
           num='9 in 10', of='native people dead within a century', y=1600),
      legacy('The conquests gave Spain an empire and a flood of silver that changed the world\'s economy, and made Spanish '
             'the language of most of the Americas. They also began a new, mixed people and culture, and Mexico today '
             'honours both its Aztec and its Spanish past.',
             'Tenochtitlan fell in 1521',
             'Atahualpa seized at Cajamarca in 1532',
             'Disease killed most of the native peoples'),
      war='spanish-conquest-aztec-maya-inca', wiki='Spanish conquest of the Aztec Empire', at='tenochtitlan')

event('reformation', 'The Reformation', 'turning', (1517, 1555),
      "A monk's protest against the sale of forgiveness split Western Christianity in two.",
      scene('Forgiveness for sale',
            "To pay for the new St Peter's in Rome, the Church sold indulgences, papers said to shorten the time a soul "
            'spent being punished after death. One preacher, Johann Tetzel, was said to promise that as soon as a coin '
            'rang in the box, a soul sprang out of purgatory.',
            kick='How it began', y=1517),
      figure('martin-luther', 'Ninety-five theses',
             'On 31 October 1517 Martin Luther, a monk and professor at Wittenberg, sent the archbishop 95 arguments against '
             'indulgences and, the story goes, nailed them to a church door. Printed copies spread across Germany within '
             'weeks.',
             y=1517, at='wittenberg'),
      turn('Here I stand',
           'Luther went further: people were saved by faith alone, he said, and the Bible, not the pope, was the final word. '
           'Cast out by the pope, he was called before the emperor Charles V at Worms in 1521 and refused to take back his '
           'words. He is said to have ended: here I stand, I can do no other.',
           img='Diet of Worms', y=1521, at='worms'),
      made('The Bible in German',
           'Hidden in Wartburg castle by a friendly prince, Luther translated the New Testament from Greek into German in '
           'eleven weeks.',
           'Ordinary people could now read the Bible for themselves, and his German became the base of the modern written '
           'language.',
           img='Luther Bible', y=1522, at='wartburg'),
      cost("The Peasants' War",
           "Peasants took Luther's words as a call for freedom and rose across Germany in 1524 and 1525. Luther urged the "
           'princes to crush them, and they did.',
           num='100,000', of='peasants killed in 1524 and 1525', y=1525),
      scene('Many reformations',
            'Others went their own way: Zwingli in Zurich, John Calvin in Geneva, and the Anabaptists, who baptised only '
            'adults. In England, Henry VIII broke with Rome in 1534, less over faith than because the pope would not end his '
            'marriage, and made himself head of the Church of England.',
            y=1534, at='geneva'),
      turn('Whose land, his faith',
           'After years of war, the Peace of Augsburg in 1555 let each German prince choose whether his land would be '
           'Catholic or Lutheran, and his subjects had to follow or move. The Catholic Church answered with reforms of its '
           'own at the Council of Trent.',
           y=1555, at='augsburg'),
      legacy('The Reformation split Western Christianity into Catholic and Protestant churches. It led to a century of '
             'religious wars, but also spread reading and schooling and new ideas about conscience. Today some 800 million '
             'people are Protestants.',
             'Began with 95 theses in 1517',
             'Spread by the printing press',
             'Split Western Christianity in two'),
      states=['Holy Roman Empire', 'England and Ireland', 'England'], wiki='Reformation', img='Ninety-five Theses',
      at='wittenberg')

event('rise-of-the-ottomans', 'The rise of the Ottoman Empire', 'conquest', (1299, 1529),
      'A small Turkish band on the Byzantine frontier grew into an empire on three continents.',
      figure('osman-i', "Osman's dream",
             'Around 1299 Osman, leader of a small Turkish band on the edge of Byzantine lands in Anatolia, began raiding and '
             'taking the towns around him. A later legend says he dreamed of a tree growing from his body whose branches '
             'spread over the whole world.',
             kick='How it began', y=1299, at='bursa'),
      battle('Into Europe',
             "His son Orhan took Bursa in 1326 and made it his capital. In 1354 an earthquake shattered the walls of "
             'Gallipoli, and the Ottomans crossed into Europe. In 1389 they beat the Serbs at Kosovo, though Sultan Murad I '
             'was killed there.',
             y=1389, at='kosovo_polje'),
      figure('bayezid-i', 'In the hands of Timur',
             'Sultan Bayezid I, called the Thunderbolt, conquered fast until 1402, when Timur, the conqueror from Central '
             'Asia, crushed his army at Ankara and took him prisoner. Legend says Timur carried him about in an iron cage. '
             'Bayezid died a captive, and his sons fought each other for ten years.',
             y=1402, at='ankara'),
      turn('Constantinople',
           'The empire recovered, and in 1453 Mehmed II took Constantinople and made it his capital. The sultans now saw '
           'themselves as the heirs of Rome.',
           img='Fall of Constantinople', y=1453, at='constantinople'),
      made('The janissaries',
           "The sultans' best troops were the janissaries, Christian boys taken from Balkan villages, made Muslims and "
           'trained from childhood as soldiers loyal only to the sultan.',
           'They were one of the first standing armies in Europe, armed with guns, and the terror of their enemies for two '
           'centuries.',
           img='Janissaries'),
      figure('selim-i', 'Selim the Grim',
             'Selim I, called the Grim, crushed the Safavids of Persia at Chaldiran in 1514, and in 1516 and 1517 conquered '
             'the Mamluk lands of Syria and Egypt. With Mecca and Medina, he took the title of protector of the holy '
             'cities.',
             y=1517),
      figure('suleiman-the-magnificent', 'At the gates of Vienna',
             'His son Suleiman the Magnificent took Belgrade, destroyed the Hungarian army at Mohács in 1526, where the '
             'young Hungarian king died, and in 1529 besieged Vienna. Snow, rain and stubborn defenders drove him back. '
             'Vienna would stop the Ottomans again in 1683.',
             y=1529, at='vienna'),
      legacy('The Ottoman Empire lasted more than 600 years, until 1922, ruling peoples of many faiths and languages from '
             'Algeria to Iraq and from Hungary to Yemen. Modern Turkey grew out of it, and its food, music and buildings '
             'shaped the whole region.',
             'Founded by Osman around 1299',
             'Took Constantinople in 1453',
             'Reached Vienna in 1529'),
      states=['Ottoman Empire'], war='rise-of-the-ottoman-empire', wiki='Rise of the Ottoman Empire',
      img='Battle of Mohács')

event('founding-of-the-mughal-empire', 'The founding of the Mughal Empire', 'founding', (1526, 1556),
      'A prince from Central Asia with cannon and a small army won North India at Panipat.',
      figure('babur', 'A prince without a kingdom',
             'Babur, descended from Timur on his father\'s side and from Genghis Khan on his mother\'s, was a prince of '
             'Ferghana who won and lost Samarkand three times. Driven south, he made Kabul his base and looked to the rich '
             'lands of India.',
             kick='How it began', y=1504, at='kabul'),
      battle('Panipat, 1526',
             'In April 1526 he met the sultan of Delhi, Ibrahim Lodi, at Panipat, with about 12,000 men against perhaps '
             '100,000 and a thousand war elephants. Babur chained carts together, fired cannon and muskets from behind them '
             'and sent horse archers round the flanks. Ibrahim died on the field.',
             img='First Battle of Panipat', y=1526, at='panipat'),
      work('The Baburnama',
           'Babur wrote his own memoirs, in his Turkic language: his battles, but also gardens, fruit, wine, friends and the '
           'animals of India. He missed the melons of home. It is one of the first autobiographies by a ruler.',
           img='Baburnama', y=1529),
      tale("A father's gift",
           'In 1530 his son Humayun lay dying. Babur, the story goes, walked three times around the bed, praying to give his '
           "own life for his son's. Humayun recovered, and Babur fell ill and died.",
           y=1530, at='agra'),
      figure('humayun', 'Lost and won again',
             'Humayun lost the new empire to the Afghan Sher Shah Suri in 1540 and spent fifteen years in exile, much of it '
             'in Persia. He won Delhi back in 1555, and died a year later after falling down the stairs of his library.',
             y=1555, at='delhi'),
      figure('akbar', 'Panipat again',
             "Humayun's son Akbar was 13. In 1556 his guardian, Bairam Khan, beat Hemu, the Hindu general who had taken "
             'Delhi, in a second battle at Panipat. Akbar would spread the empire across most of North India and rule for '
             '49 years.',
             y=1556, at='panipat'),
      legacy('The Mughals ruled much of India for two centuries. They left the Taj Mahal and the Red Fort, and a blend of '
             'Persian and Indian culture that shaped the Urdu language and the food, music and painting of North India '
             'and Pakistan.',
             'Babur won at Panipat in 1526',
             'Humayun lost the empire and won it back',
             'Began two centuries of Mughal rule'),
      states=['Sultanate of Delhi', 'Mughal Empire'], wiki='Mughal Empire', img='Baburnama', at='panipat')

event('russia-conquers-siberia', 'Russia conquers Kazan and Siberia', 'conquest', (1552, 1598),
      'The first tsar took the Tatar khanates of the Volga, and Cossacks crossed the Urals into Siberia.',
      figure('ivan-the-terrible', 'The first tsar',
             'In 1547 Ivan IV, grand prince of Moscow, was crowned the first tsar of all Russia, a title taken from Caesar. '
             'To the east lay the Tatar khanates, heirs of the Golden Horde that had once ruled the Russians.',
             kick='How it began', y=1547, at='moscow'),
      battle('Kazan',
             'In 1552 Ivan besieged Kazan, on the Volga, with some 150,000 men. His engineers dug tunnels under the walls '
             'and blew them open with gunpowder, and the city was stormed and its men killed. Astrakhan fell in 1556, and '
             'the whole Volga was Russian.',
             img='Siege of Kazan', y=1552, at='kazan'),
      work("St Basil's Cathedral",
           'To give thanks, Ivan built a cathedral on Red Square with nine chapels under bright onion domes. A legend says he '
           'blinded its architects so they could never build anything as beautiful again. It is almost certainly untrue.',
           img="Saint Basil's Cathedral", y=1561, at='moscow'),
      turn('The Terrible',
           'Ivan grew cruel and suspicious. His black-robed guards, the oprichniki, terrorised the land and in 1570 '
           'massacred thousands in Novgorod. In 1581, in a rage, he struck his own son and heir with his staff and killed '
           'him.',
           y=1581, at='novgorod'),
      figure('yermak-timofeyevich', 'Yermak',
             'In 1582 a Cossack chief, Yermak, paid by the Stroganov merchants, crossed the Urals with about 800 men and took '
             'Isker, capital of the khanate of Sibir. He drowned in a river in 1585, weighed down, the story goes, by armour '
             'the tsar had given him.',
             y=1582, at='isker'),
      scene('To the Pacific',
            'Cossacks and fur trappers pushed east along the great rivers, building wooden forts as they went. In 1639 they '
            'reached the Pacific. The furs of Siberia, sable above all, made the tsars rich.',
            y=1639),
      legacy('The conquests turned Muscovy into a vast empire of many peoples and faiths that reached the Pacific within a '
             'century. Russia is still the largest country on Earth, and Siberia makes up three quarters of it.',
             'Kazan fell in 1552',
             'Yermak crossed the Urals in 1582',
             'Russia reached the Pacific by 1639'),
      states=['Tsardom of Muscovy', 'Kazan Khanate', 'Astrakhan Khanate', 'Khanate of Sibir'],
      war='russian-conquest-kazan-astrakhan-siberia', wiki='Russian conquest of Siberia', img="Saint Basil's Cathedral")

event('spanish-armada', 'The Spanish Armada', 'invasion', (1588, 1588),
      'Spain sent a great fleet to invade England. Fire ships and Atlantic storms destroyed it.',
      scene('Why Spain sailed',
            'Philip II of Spain, the most powerful king in Europe, was a devout Catholic. Protestant England under Elizabeth '
            'I helped the Dutch rebels fighting Spain, and English privateers raided Spanish treasure ships. When Elizabeth '
            'executed the Catholic Mary, Queen of Scots, in 1587, Philip decided to invade.',
            kick='How it began', img='Philip II of Spain', y=1587),
      figure('francis-drake', "Singeing the king's beard",
             "In 1587 Drake sailed into Cádiz harbour and burned some 30 of the ships being made ready, which he called "
             "singeing the king of Spain's beard. It held the Armada back a year. The tale that he finished his game of "
             'bowls when it was sighted is a legend.',
             y=1587, at='cadiz'),
      scene('The Armada sails',
            'In May 1588 some 130 ships with nearly 30,000 men left Lisbon under the Duke of Medina Sidonia, who had little '
            "experience at sea. They were to sail up the Channel, meet the Duke of Parma's army in Flanders and carry it "
            'across to England.',
            y=1588, at='lisbon'),
      battle('Fire ships off Calais',
             'English ships harried the Armada up the Channel, but its tight crescent held. Then, at anchor off Calais on '
             'the night of 7 August, it was attacked by eight burning ships sent in on the tide. The Spanish cut their '
             'cables and scattered, and the next day were beaten at Gravelines.',
             img='Battle of Gravelines', y=1588, at='calais'),
      figure('elizabeth-i', 'The heart of a king',
             'At Tilbury, Elizabeth rode among her soldiers waiting for the invasion and told them she had the body of a weak '
             'and feeble woman, but the heart and stomach of a king. By then the danger had already passed.',
             y=1588, at='tilbury'),
      cost('Wrecked',
           'With the wind against them, the Spanish sailed home the long way, round Scotland and Ireland, into terrible '
           'storms. Perhaps a third of the ships were lost, and many men drowned or were killed on the Irish coast.',
           num='Half', of="of the Armada's men never came home", y=1588),
      tale('God blew',
           'English medals for the victory read: God blew, and they were scattered. Philip is said to have answered that he '
           'had sent his ships to fight men, not the winds.',
           y=1589),
      legacy('The defeat saved Protestant England and the Dutch revolt and became a national legend. But the war went on '
             'for 16 more years, Spain rebuilt its fleet, and England\'s own armada of 1589 failed too. Its rise as a sea '
             'power had only begun.',
             'About 130 ships sailed in 1588',
             'Scattered by fire ships off Calais',
             'Wrecked by storms off Ireland'),
      states=['Spain', 'England and Ireland', 'Habsburg Netherlands', 'Portugal'], wiki='Spanish Armada',
      img='Spanish Armada', at='calais')

event('imjin-war', 'The Imjin War', 'invasion', (1592, 1598),
      "Japan's ruler tried to conquer China through Korea. An admiral with ironclad turtle ships helped stop him.",
      figure('toyotomi-hideyoshi', 'A plan to conquer China',
             'Toyotomi Hideyoshi, born a peasant, had finished uniting Japan after a century of civil war. With hundreds of '
             'thousands of battle-hardened samurai and nothing left to conquer at home, he set out to conquer Ming China, '
             'and asked Korea to let his armies through. Korea refused.',
             kick='How it began', y=1591),
      battle('The invasion',
             'In May 1592 some 150,000 Japanese troops landed at Busan. Armed with muskets, they swept north, took Seoul '
             'in under three weeks and soon held Pyongyang. King Seonjo fled toward the Chinese border.',
             y=1592, at='busan'),
      figure('yi-sun-sin', 'The turtle ships',
             'At sea it was another story. Admiral Yi Sun-sin led a fleet that included turtle ships, low warships roofed '
             'with iron spikes, with cannon on every side and a dragon head that belched smoke. He won battle after battle '
             'and cut the sea lanes that fed the Japanese armies.',
             img='Turtle ship', y=1592),
      scene('China joins in',
            'The Ming emperor Wanli sent a great army to help Korea, and in 1593 it took back Pyongyang. Korean volunteer '
            'armies, monks among them, fought behind the Japanese lines. The war sank into years of talks that went '
            'nowhere.',
            y=1593, at='pyongyang'),
      battle('Myeongnyang',
             'When the war began again in 1597, Yi, dismissed and jailed through court jealousy, was called back with only '
             '13 ships. In the narrow strait of Myeongnyang he beat a Japanese fleet of more than 100 by using the fierce '
             'tidal current against it.',
             y=1597, at='myeongnyang'),
      cost('The ear mound',
           "Hideyoshi's soldiers were rewarded for proof of their kills, and sent home the noses and ears of tens of "
           'thousands of Koreans, soldiers and civilians. They lie buried in the Mimizuka, the Ear Mound, in Kyoto.',
           num='A million', of='Koreans dead in the war, perhaps', y=1597, at='kyoto'),
      turn('Noryang',
           'Hideyoshi died in 1598, and the Japanese pulled out. In the last battle, at Noryang, Yi Sun-sin was struck by a '
           'bullet. He told his men to hide his death until the battle was won.',
           y=1598, at='noryang'),
      legacy('The war wrecked Korea, emptied the Ming treasury and ended Japan\'s hopes of a mainland empire for 300 years. '
             'Yi Sun-sin is Korea\'s greatest hero, and his statue stands in the heart of Seoul.',
             'Japan invaded Korea in 1592',
             'Turtle ships ruled the sea',
             'Korea and Ming China drove Japan out'),
      war='imjin-war', wiki='Imjin War', img='Turtle ship')

event('sengoku-japan', "Japan's age of warring states", 'civil-war', (1467, 1615),
      'For 150 years Japanese warlords fought each other, until three men in turn united the country.',
      scene('The Onin War',
            'In 1467 a quarrel over who would be the next shogun split the great lords into two camps and set them '
            'fighting in the streets of Kyoto. After ten years the capital lay in ashes and no one had won. The shoguns lost '
            'control, and Japan broke up into the lands of rival warlords, the daimyo.',
            kick='How it began', y=1467, at='kyoto'),
      scene('The country at war',
            'For a century the daimyo fought for land, castles and survival. Vassals overthrew their lords, which the '
            'Japanese called gekokujo, the low overthrowing the high. Even Buddhist temples raised armies of warrior monks.',
            y=1500),
      made('Guns from a shipwreck',
           'In 1543 Portuguese traders landed on the island of Tanegashima with matchlock guns. Japanese smiths copied them '
           'within a year.',
           'Within decades Japan was making guns by the tens of thousands, and battles were won by massed ranks of '
           'musketeers.',
           y=1543, at='tanegashima'),
      figure('oda-nobunaga', 'Nobunaga',
             'The first great unifier, Oda Nobunaga, beat a far larger army at Okehazama in 1560, took Kyoto in 1568, and '
             'in 1575 used volleys of gunfire to crush the famous horsemen of the Takeda at Nagashino. In 1582 one of his '
             'own generals turned on him at a temple in Kyoto, and he died in the flames.',
             y=1575, at='nagashino'),
      figure('toyotomi-hideyoshi', 'Hideyoshi',
             "Nobunaga's general Hideyoshi, a peasant's son, avenged him and finished uniting Japan by 1590. He took away "
             "the peasants' swords and froze everyone in their class, so that no one could rise as he had.",
             y=1590, at='osaka'),
      battle('Sekigahara',
             'Hideyoshi died in 1598, leaving a five-year-old heir, and the daimyo split again. On 21 October 1600, in fog, '
             'at Sekigahara, Tokugawa Ieyasu beat the lords of the west, helped when several of them changed sides in the '
             'middle of the battle.',
             img='Battle of Sekigahara', y=1600, at='sekigahara'),
      figure('tokugawa-ieyasu', 'The patient one',
             'Ieyasu became shogun in 1603. In 1615 he took Osaka castle and wiped out Hideyoshi\'s family. A Japanese '
             'saying sums up the three: Nobunaga pounded the rice, Hideyoshi kneaded the cake, and Ieyasu sat down and ate '
             'it.',
             y=1615, at='osaka'),
      legacy('The Tokugawa shoguns gave Japan more than 250 years of peace, until 1868, and shut it off from most of the '
             'world. The age of warring states, with its castles, samurai and ninja, is still the favourite setting of '
             'Japanese novels, films and games.',
             'Began with the Onin War in 1467',
             'Three men united Japan in turn',
             'Ended with Sekigahara and Osaka'),
      states=['Japan (Warring States)', 'Japan'], war='onin-war-sengoku', wiki='Sengoku period', img='Himeji Castle')

event('atlantic-slave-trade', 'The Atlantic slave trade', 'slavery', (1526, 1867),
      'For three and a half centuries, European ships carried 12 million Africans in chains to the Americas.',
      scene('A trade in people',
            'Slavery was old in Africa, Europe and the Middle East. But when the sugar, tobacco and silver of the Americas '
            'needed workers, and the native peoples were dying, Europeans began to buy captives in West Africa and ship '
            'them across the Atlantic. From the 1520s ships sailed straight from Africa to the Americas.',
            kick='How it began', y=1526),
      scene('Captured',
            'Most captives were taken in wars and raids between African states, or kidnapped, and sold at the coast to '
            'European traders for cloth, guns, iron and cowrie shells. Kingdoms such as Dahomey and Asante grew rich and '
            'strong on the trade.',
            y=1700),
      cost('The Middle Passage',
           'On the crossing, the Middle Passage, captives were chained below decks, packed so tightly they could barely '
           'move, for six to ten weeks. About one in seven died at sea, of disease, hunger and despair. Some leapt '
           'overboard.',
           num='1.8 million', of='died on the way across', y=1750),
      work('The Brookes',
           'In 1788 campaigners against the trade printed a plan of the slave ship Brookes, showing how 454 people could be '
           'packed into its hold under British law. It became one of the most famous images of the campaign.',
           img='Brookes (ship)', y=1788),
      figure(None, 'Olaudah Equiano',
             'Olaudah Equiano said he was kidnapped as a boy in what is now Nigeria and shipped to the Caribbean. He bought '
             'his own freedom, and his life story, published in London in 1789, made thousands of readers see the trade '
             'through the eyes of its victims.',
             img='Olaudah Equiano', y=1789, at='london'),
      scene('The plantations',
            'Most enslaved Africans went to Brazil and the Caribbean to grow sugar, in such brutal conditions that many were '
            'worked to death within a few years. About 400,000 were taken to North America. Their children were born '
            'slaves too.',
            y=1780),
      turn('Abolition',
           'Enslaved people resisted from the start: they ran away, rose in revolts such as the one that freed Haiti, and '
           'kept their cultures alive. In Britain a mass campaign won a ban on the trade in 1807. The last known slave ship '
           'reached Cuba in 1867, and Brazil freed its last slaves in 1888.',
           y=1807),
      legacy('The trade was one of the largest forced migrations in history. It built fortunes in Europe and the Americas, '
             'held back West Africa, and left a racism whose effects last today. It also made the African diaspora, whose '
             'music, faiths and food shaped the whole Atlantic world.',
             '12.5 million Africans shipped across',
             'About 1.8 million died on the way',
             'Banned in the 1800s'),
      states=['Portugal', 'Spain', 'England and Ireland', 'United Kingdom', 'France', 'Dutch Republic', 'Benin', 'Oyo',
              'Dahomey', 'Asante', 'Ndongo', 'Portuguese Brazil', 'Viceroyalty of Brazil', 'British American colonies'],
      wiki='Atlantic slave trade', img='Brookes (ship)', at=(-1.35, 5.08), where='Elmina Castle')

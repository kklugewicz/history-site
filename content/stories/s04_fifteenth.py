from _lib import story, life, win, made, work, song, tale, legacy

story('filippo-brunelleschi', 'The goldsmith who rediscovered perspective and raised the great dome of Florence.',
    life('A goldsmith of Florence',
         'Filippo Brunelleschi was born in Florence in 1377, the son of a notary, and trained as a goldsmith. In 1401 he '
         'lost a famous contest to design bronze doors for the Baptistery to Lorenzo Ghiberti, and, legend says, gave up '
         'sculpture in disgust. With his friend Donatello he went to Rome to measure the ancient ruins.',
         img='Florence Baptistery', y=1401, at='florence'),
    made('Perspective',
         'Around 1415 he painted the Baptistery on a panel with a peephole in it. Looking through the hole at a mirror, '
         'people could not tell his picture from the real building.',
         'He had worked out linear perspective, where parallel lines meet at a vanishing point. Within a few years '
         'painters were making flat walls look like windows into real space.',
         img='Perspective (graphical)', y=1415, at='florence'),
    tale('The egg',
         'The cathedral of Florence had a gap 45 metres wide where a dome should go, and no one knew how to build one. '
         'Brunelleschi refused to show his plans, but challenged his rivals to stand an egg on its end. None could. He '
         'cracked its bottom on the table and stood it up. "We could have done that," they said. "Yes, and you would say '
         'the same if you saw my plans."',
         y=1418, at='florence'),
    win('The dome',
        'From 1420 to 1436 he built the dome without the forest of wooden supports everyone thought it would need, using '
        'two shells, one inside the other, and bricks laid in a herringbone pattern. He invented ox-driven hoists to lift '
        'the materials. It is still the largest brick dome ever built.',
        img='Florence Cathedral', y=1436, at='florence'),
    tale('A patent, and a shipwreck',
         'In 1421 Florence granted him what is often called the first modern patent, for a giant boat to carry marble up '
         'the river Arno. On its first trip it sank, with all its marble.',
         y=1427, at='florence'),
    legacy('Brunelleschi was the first great architect of the Renaissance. His dome still crowns Florence, his '
           'perspective changed how artists painted, and his clean, classical churches set a style for centuries.',
           'Built the dome of Florence Cathedral',
           'Worked out linear perspective',
           'The father of Renaissance architecture'),
)

story('henry-the-navigator', 'The prince who sent Portugal\'s ships into the unknown Atlantic.',
    life('A prince of Portugal',
         'Henry was the third son of King John I of Portugal and his English queen, Philippa. In 1415, aged 21, he helped '
         'capture Ceuta, a Muslim port in North Africa, where he heard of gold caravans crossing the Sahara from lands far '
         'to the south.',
         img='Conquest of Ceuta', y=1415, at='ceuta'),
    win('Sending out the ships',
        'From the south-west tip of Portugal, near Sagres, he paid for voyage after voyage down the coast of Africa. He '
        'gathered mapmakers, sailors and shipbuilders, though he never sailed on the voyages himself. His sailors settled '
        'Madeira and the Azores, where sugar soon made Portugal rich.',
        img='Sagres', y=1420, at='sagres'),
    made('The caravel',
         'His shipbuilders developed the caravel, a small, light ship with triangular sails that could sail close into the '
         'wind.',
         'Caravels could explore unknown coasts and beat their way home against the wind. They opened the age of discovery; '
         'Columbus crossed the Atlantic in two of them.',
         img='Caravel', y=1440),
    tale('The sea that boiled',
         'Sailors dreaded Cape Bojador on the Sahara coast, where the sea was said to boil and sea monsters waited. For '
         'years Henry\'s captains turned back. In 1434 his squire Gil Eanes finally sailed round it, and found only calm '
         'water.',
         img='Cape Bojador', y=1434, at=(-14.49, 26.13), where='Cape Bojador'),
    life('The slave trade begins',
         'In 1444 his ships brought 235 captured Africans to Lagos, in Portugal, and sold them. It was the start of the '
         'Atlantic slave trade. A chronicler who watched wrote that even he wept to see families torn apart.',
         y=1444, at=(-8.67, 37.1), where='Lagos, Portugal'),
    legacy("Henry never sailed farther than North Africa, but the voyages he paid for began Europe's age of exploration. "
           "They led to Vasco da Gama's route to India and a Portuguese empire around the world, and also to the Atlantic "
           'slave trade.',
           'Launched the Portuguese voyages of discovery',
           'His sailors developed the caravel',
           'Began the exploration of the African coast',
           img='Padrão dos Descobrimentos', cap='The Monument to the Discoveries in Lisbon, with Henry at the front'),
)

story('johannes-gutenberg', 'The goldsmith of Mainz whose printing press changed the world.',
    life('A goldsmith of Mainz',
         'Johannes Gutenberg was born around 1400 in Mainz, in Germany, and trained in metalwork. Forced out by a quarrel '
         'in the city, he moved to Strasbourg, where he made little mirrors for pilgrims, which were said to catch the holy '
         'power of relics.',
         img='Mainz', y=1400, at='mainz'),
    made('The printing press',
         'He brought together metal letters cast in a hand mould, an oily ink, and a press like a wine press, so pages '
         'could be printed fast and the letters used again and again.',
         'A press could print thousands of pages a day, where a scribe copied a few. In 50 years some 20 million books '
         'were printed in Europe.',
         img='Printing press', y=1440, at=(7.75, 48.58), where='Strasbourg'),
    work('The Gutenberg Bible',
         'Around 1455 in Mainz he printed about 180 copies of the Bible in Latin, each of 1,282 pages, so beautiful they '
         'looked handwritten. Forty-nine survive, and a single copy is worth tens of millions of dollars.',
         img='Gutenberg Bible', y=1455, at='mainz'),
    life('Ruined by his partner',
         'He had borrowed heavily from a lawyer, Johann Fust, who sued him just as the Bible was nearly done and took over '
         'his workshop and type. Gutenberg ended his days on a small pension from the archbishop of Mainz, paid in grain, '
         'wine and clothes.',
         y=1455, at='mainz'),
    tale('Wildfire',
         'Printing spread like wildfire. By 1500 there were presses in more than 250 towns, and printed books carried the '
         'Renaissance, the Reformation and the new science across Europe. Martin Luther called printing "God\'s highest act '
         'of grace".',
         img='Global spread of the printing press', y=1500),
    legacy("Gutenberg's press is often called the most important invention of the last thousand years. Cheap books spread "
           'ideas faster than any ruler could stop them, and made the Reformation, modern science and mass reading possible.',
           'Brought printing with movable metal type to Europe',
           'Printed the Gutenberg Bible',
           'Started an information revolution'),
)

story('joan-of-arc', 'The peasant girl who led the French army at 17 and was burned at 19.',
    life('A farm girl of Domrémy',
         "Joan was born around 1412 in Domrémy, a village in north-eastern France, to a farming family. France was losing "
         "the Hundred Years' War: the English and their allies held Paris and the north, and the heir to the throne, "
         'Charles, had not even been crowned.',
         img='Domrémy-la-Pucelle', y=1412, at='domremy'),
    tale('The voices',
         'At 13 she began to hear voices she said were saints, telling her to drive out the English and see Charles crowned '
         'at Reims. At 16 she walked to the nearest fortress and demanded an escort to the prince. The captain laughed, '
         'then gave in.',
         y=1428, at='domremy'),
    tale('Finding the prince',
         'At Chinon in 1429 Charles hid among his courtiers, dressed like them, to test her. Joan walked straight up to him. '
         'Churchmen questioned her for three weeks, then let her ride to war in armour, with her own white banner.',
         img='Château de Chinon', y=1429, at=(0.24, 47.17), where='Chinon'),
    win('The Maid of Orléans',
        'The English had besieged Orléans for months. Joan arrived in April 1429, and in nine days the French stormed the '
        'English forts. She was hit in the shoulder by an arrow, pulled it out, and went back into the fight. The siege '
        'was lifted.',
        img='Siege of Orléans', y=1429, at='orleans'),
    win('A crown at Reims',
        'In July 1429 she led Charles through enemy country to Reims, where he was crowned Charles VII. Joan stood by the '
        'altar holding her banner.',
        img='Reims Cathedral', y=1429, at='reims'),
    life('Burned at the stake',
         'In 1430 she was captured at Compiègne and sold to the English. A church court at Rouen tried her for heresy, and '
         "for wearing men's clothes. On 30 May 1431, aged 19, she was burned at the stake in the market square.",
         img='Trial of Joan of Arc', y=1431, at='rouen'),
    legacy("Twenty-five years later a new trial declared her innocent, and in 1920 she was made a saint. Joan turned the "
           "tide of the Hundred Years' War and became the national heroine of France.",
           'Lifted the siege of Orléans at 17',
           'Saw Charles VII crowned at Reims',
           'A saint, and the heroine of France'),
)

story('pachacuti', 'The Inca ruler who "shook the earth", built an empire and Machu Picchu.',
    life('A younger son',
         'Cusi Yupanqui was a younger son of Viracocha, ruler of the small Inca kingdom around Cusco, high in the Andes. He '
         'was not meant to rule.',
         img='Cusco', y=1418, at='cuzco'),
    win('Saving Cusco',
        'Around 1438 the powerful Chanka people attacked Cusco. The old king and his heir fled; Cusi Yupanqui stayed and '
        'defended the city. Legend says the very stones of the field rose up as warriors to fight for him. He won, took '
        'the throne and a new name: Pachacuti, "he who shakes the earth".',
        y=1438, at='cuzco'),
    win('Building an empire',
        'With his son Topa Inca, Pachacuti conquered much of the Andes, turning a small kingdom into Tawantinsuyu, "the '
        'four parts together", the largest empire in the Americas.',
        img='Inca Empire', y=1463),
    work('A city of stone',
         'He rebuilt Cusco in stone, perhaps in the shape of a puma, with the fortress of Sacsayhuaman as its head, and a '
         'Temple of the Sun whose walls were covered in gold. Inca stones fit so tightly that a knife blade cannot slip '
         'between them.',
         img='Sacsayhuamán', y=1450, at='cuzco'),
    work('Machu Picchu',
         'High on a mountain ridge he built an estate of granite palaces, temples and terraces: Machu Picchu. The Spanish '
         'never found it. The world heard of it in 1911, when local farmers led the American explorer Hiram Bingham there.',
         img='Machu Picchu', y=1450, at='machu_picchu'),
    made('Roads, runners and knots',
         'He organised roads that grew to about 40,000 km, relay runners, storehouses, and records kept on quipus, strings '
         'tied with knots.',
         'Messages could cross the empire at 240 km a day, and the stored food fed armies, and the hungry in bad years.',
         img='Quipu', y=1460),
    legacy('Pachacuti turned a small Andean kingdom into the greatest empire of the Americas, with roads, cities and '
           'Machu Picchu. Peruvians honour him as one of the founders of their nation.',
           'Founded the Inca Empire',
           'Built Machu Picchu',
           'Rebuilt Cusco as a city of stone'),
)

story('vlad-the-impaler', 'The prince of Wallachia whose cruelty gave the world Dracula.',
    life('Son of the dragon',
         'Vlad was born around 1431, son of Vlad Dracul, prince of Wallachia, in what is now Romania. "Dracul" came from '
         'the Order of the Dragon his father had joined, so Vlad was "Dracula", son of the dragon. As a boy he and his '
         'brother were sent as hostages to the Ottoman sultan.',
         img='Order of the Dragon', y=1442, at='edirne'),
    life('Prince of Wallachia',
         'His father and elder brother were murdered by rebel nobles; his brother was buried alive. Vlad won the throne for '
         'good in 1456 and, the stories say, invited the nobles to a feast and had them impaled on stakes.',
         img='Târgoviște', y=1456, at='targoviste'),
    tale('The golden cup',
         'He ruled through terror. A story says he left a golden cup by a fountain for anyone to drink from, and no one '
         'ever dared steal it. Thieves, liars and enemies were impaled. German pamphlets with woodcuts of him dining among '
         'the dead became early best-sellers.',
         y=1459, at='targoviste'),
    win('The night attack',
        "In 1462 Sultan Mehmed II invaded with a huge army. Vlad burned crops and poisoned wells, then led a night raid on "
        'the Ottoman camp, trying to kill the sultan himself. Marching on, the Ottomans found a forest of thousands of '
        'impaled prisoners outside his capital, and turned back.',
        img='Night Attack at Târgoviște', y=1462, at='targoviste'),
    life('Prisoner, and death',
         'Betrayed, he spent years as a prisoner of the king of Hungary. He won back his throne in 1476 but was killed in '
         'battle within months, and his head was sent to Constantinople.',
         y=1476, at='bucharest'),
    tale('Count Dracula',
         'In 1897 the Irish writer Bram Stoker borrowed the name Dracula for the vampire count of his novel. Vlad never '
         'drank blood, but Bran Castle, which has little to do with him, now draws crowds of tourists as "Dracula\'s castle".',
         img='Bran Castle', y=1897),
    legacy('In Romania, Vlad is remembered as a hero who fought the Ottomans and punished corrupt nobles. Elsewhere, his '
           'cruelty and his name made him the model for the most famous vampire in fiction.',
           'Fought the Ottoman Empire',
           'Infamous for impaling his enemies',
           'Gave his name to Dracula'),
)

story('mehmed-ii', 'The 21-year-old sultan who conquered Constantinople.',
    life('A boy sultan',
         'Mehmed was born in Edirne in 1432, son of Sultan Murad II. His father handed him the throne at 12, then took it '
         'back when the army rebelled and a crusade threatened. Mehmed never forgot it. He grew up speaking several '
         'languages and reading the lives of Alexander and Caesar.',
         img='Edirne', y=1444, at='edirne'),
    tale('Giant cannons',
         'A Hungarian engineer, Orban, cast him huge bronze cannons. The biggest fired stone balls of more than 500 kg and '
         'took 60 oxen to pull. For a thousand years the walls of Constantinople had never been broken.',
         img='Dardanelles Gun', y=1453, at='edirne'),
    tale('Ships over the hills',
         'In 1453 he besieged Constantinople. A great chain blocked the Golden Horn, its harbour, so he had about 70 ships '
         'hauled overland on greased logs, over a hill, and launched them behind the chain.',
         img='Fall of Constantinople', y=1453, at='constantinople'),
    win('The fall of Constantinople',
        'On 29 May 1453, after 53 days, his troops stormed the battered walls. The last Byzantine emperor, Constantine '
        'XI, died fighting. Mehmed rode to Hagia Sophia and made it a mosque. From then on he was called Fatih, "the '
        'Conqueror".',
        img='Walls of Constantinople', y=1453, at='constantinople'),
    win('Rebuilding Istanbul',
        'He made the city his capital, filled it with people of every faith, and named a Greek patriarch to lead its '
        'Christians. He built a great mosque and the Topkapi Palace, the home of sultans for 400 years.',
        img='Topkapı Palace', y=1478, at='constantinople'),
    tale('Sitting for Bellini',
         'Mehmed loved art and collected books in Greek, Latin and Arabic. In 1479 he invited the Venetian painter Gentile '
         'Bellini to Istanbul to paint him; the portrait of the sultan in a red cloak and white turban hangs in London.',
         img='Gentile Bellini', y=1480, at='constantinople'),
    legacy('Mehmed ended the thousand-year Byzantine Empire and made Istanbul the capital of an empire that lasted until '
           '1922. To Turks he is Fatih, the Conqueror, one of their greatest heroes.',
           'Conquered Constantinople in 1453',
           'Ended the Byzantine Empire',
           'Made Istanbul the Ottoman capital'),
)

story('sandro-botticelli', 'The painter of The Birth of Venus, favourite of the Medici.',
    life('The little barrel',
         'Alessandro Filipepi was born in Florence around 1445, the youngest son of a tanner. His nickname, Botticelli, '
         '"little barrel", came from his plump elder brother. He trained as a goldsmith, then with the painter Fra Filippo '
         'Lippi.',
         img='Fra Filippo Lippi', cap='Fra Filippo Lippi, his teacher', y=1460, at='florence'),
    life('Painter of the Medici',
         'He became a favourite of the Medici, the banking family who ran Florence. He painted members of the family as '
         'the three kings in The Adoration of the Magi, and put himself in too, at the edge in a yellow cloak, looking out '
         'at us.',
         img='Adoration of the Magi (Botticelli, 1475)', y=1475, at='florence'),
    work('Primavera',
         'Around 1480 he painted Primavera, "Spring": Venus in an orange grove, the Three Graces dancing, Flora scattering '
         'flowers. Botanists have counted about 500 plants in it, of nearly 200 kinds.',
         img='Primavera (Botticelli)', y=1480, at='florence'),
    work('The Sistine Chapel walls',
         'In 1481 the pope called him to Rome with other leading painters to decorate the walls of his new Sistine Chapel, '
         "a quarter of a century before Michelangelo painted its ceiling.",
         img='Sistine Chapel', y=1481, at='rome'),
    work('The Birth of Venus',
         'His most famous picture shows the goddess Venus, newly born from the sea, drifting ashore on a scallop shell, '
         'blown by the winds. It was one of the first large paintings since ancient times of a goddess from the old myths.',
         img='The Birth of Venus', y=1485, at='florence'),
    tale('The bonfire of the vanities',
         'In the 1490s the fiery preacher Savonarola turned Florence against luxury. Crowds threw mirrors, cards, fine '
         'clothes and paintings onto a great bonfire. A story says Botticelli threw in some of his own pictures. His late '
         'work grew darker and more religious.',
         img='Bonfire of the vanities', y=1497, at='florence'),
    life('Forgotten, then found',
         'Tastes changed, and he died poor in 1510, almost forgotten. For three centuries his paintings were ignored, until '
         'Victorian artists in England rediscovered him.',
         y=1510, at='florence'),
    legacy("Botticelli's Venus and Primavera are among the best-loved paintings in the world, and his graceful figures "
           'still sum up the dreamy beauty of the early Renaissance.',
           'Painted The Birth of Venus',
           'Painted Primavera',
           'Favourite painter of the Medici'),
)

story('isabella-i-of-castile', 'The queen who united Spain, conquered Granada and sent Columbus west.',
    life('An unlikely queen',
         'Isabella was born in 1451, daughter of the king of Castile, but with brothers ahead of her she was not expected '
         'to rule. Her half-brother, King Henry IV, tried to marry her to the much older king of Portugal. She refused.',
         img='Crown of Castile', y=1468),
    tale('A secret wedding',
         'In 1469 she secretly married Ferdinand, heir to Aragon, who rode to meet her disguised as a servant. They used a '
         "forged permission from the pope. The marriage joined Spain's two largest kingdoms.",
         img='Ferdinand II of Aragon', cap='Ferdinand of Aragon, her husband', y=1469, at='valladolid'),
    win('Queen of Castile',
        'When Henry died in 1474 she had herself proclaimed queen and won a five-year war against her rivals. She and '
        'Ferdinand ruled together as "the Catholic Monarchs", with a motto meaning that each was worth as much as the '
        'other.',
        img='Catholic Monarchs', y=1474, at=(-4.12, 40.95), where='Segovia'),
    win('The fall of Granada',
        'After ten years of war they took Granada, the last Muslim kingdom in Spain, on 2 January 1492, ending almost '
        '800 years of Muslim rule. The last sultan, it is said, wept as he looked back at the Alhambra.',
        img='Alhambra', y=1492, at='granada'),
    life('Expelling the Jews',
         'The same year she ordered every Jew in her kingdoms to convert or leave; tens of thousands left. The Spanish '
         'Inquisition, which she and Ferdinand had set up in 1478, hunted those suspected of secretly keeping their old '
         'faith.',
         img='Alhambra Decree', y=1492, at='granada'),
    win('Backing Columbus',
        "Also in 1492, after years of saying no, she agreed to pay for Christopher Columbus's voyage west across the "
        "Atlantic. His landing in the Americas began Spain's empire there.",
        img='Santa María (ship)', y=1492, at='palos'),
    legacy('Isabella united Spain with Ferdinand, finished the long reconquest of Spain and launched its empire in the '
           'Americas. She also set up the Inquisition and drove out the Jews. Her grandson Charles V ruled half the world.',
           'United Spain with Ferdinand of Aragon',
           'Completed the conquest of Granada',
           "Paid for Columbus's voyage",
           'Expelled the Jews and backed the Inquisition'),
)

story('christopher-columbus', 'The sailor who crossed the Atlantic in 1492, thinking he had reached Asia.',
    life("A weaver's son from Genoa",
         'Christopher Columbus was born in Genoa in 1451, son of a wool weaver. He went to sea young, survived a shipwreck '
         'off Portugal by clinging to an oar and swimming ashore, and settled in Lisbon, making maps and sailing as far as '
         'West Africa.',
         img='Genoa', y=1451, at='genoa'),
    life('The wrong sums',
         'He believed he could reach Asia by sailing west. Experts agreed the Earth was round, but said he had badly '
         'underestimated its size, which he had. Portugal and others turned him down. In 1492, after six years of asking, '
         "Spain's monarchs said yes.",
         img='Isabella I of Castile', cap='Queen Isabella, who paid for the voyage', y=1492, at='granada'),
    win('The first voyage',
        'On 3 August 1492 he sailed from Palos with three ships, the Santa María, the Pinta and the Niña, and about 90 '
        'men. After five weeks out of sight of land the crew was close to mutiny. Then, on 12 October, a lookout shouted '
        '"Land!": an island in the Bahamas.',
        img='Santa María (ship)', y=1492, at='palos'),
    tale('"Indians"',
         'Sure he had reached Asia, he called the people he met, the Taíno, "Indians". He wrote that they were gentle and '
         'generous, and in the same letter that they would make good servants. On Christmas Day, off Hispaniola, the Santa '
         'María ran aground.',
         img='Taíno', y=1492, at='san_salvador_bh'),
    life('Governor in chains',
         'He made three more voyages and became governor of Hispaniola. He ruled so harshly that in 1500 he was arrested '
         'and shipped home in chains. The Taíno were forced to dig for gold, and within decades most had died from cruelty '
         'and European diseases.',
         img='Hispaniola', y=1500, at='santo_domingo'),
    tale('The eclipse trick',
         'Stranded on Jamaica in 1504, with the islanders refusing to bring more food, he used an almanac to predict an '
         'eclipse of the Moon. He warned them that God would take away the Moon unless they helped. When it darkened, they '
         'came running with food.',
         img='Lunar eclipse', y=1504, at=(-77.2, 18.4), where='Jamaica'),
    legacy('Columbus died in 1506 still believing he had reached Asia. His voyages linked Europe and the Americas for '
           'good, bringing new foods and riches, and also conquest, slavery and the deaths of millions of Native Americans.',
           'Crossed the Atlantic in 1492',
           'Began the lasting link between Europe and the Americas',
           'His arrival brought conquest and catastrophe to Native peoples'),
)

story('moctezuma-ii', 'The last great ruler of the Aztecs, who welcomed Cortés into his city.',
    life('Priest and warrior',
         'Moctezuma was born around 1466, a nephew of earlier Aztec rulers. He served as a priest and a successful '
         'general, and in 1502 was chosen huey tlatoani, "great speaker", the ruler of the Aztec Empire.',
         img='Aztec Empire', y=1502, at='tenochtitlan'),
    win('Lord of Tenochtitlan',
        'He ruled from Tenochtitlan, a city of perhaps 200,000 people on an island in a lake, bigger than any city in '
        'Spain, with causeways, canals, floating gardens and the Great Temple at its heart. He was carried in a litter, '
        'and commoners had to look at the ground as he passed.',
        img='Templo Mayor', y=1510, at='tenochtitlan'),
    tale('Fresh fish and chocolate',
         'Runners brought him fresh fish from the coast, hundreds of kilometres away. The Spanish wrote that he drank '
         'frothy chocolate from golden cups, and at each meal chose from hundreds of dishes.',
         img='History of chocolate', y=1515, at='tenochtitlan'),
    tale('Omens',
         'Later accounts said omens had warned of disaster: a comet, a temple bursting into flames, a woman weeping in the '
         'night for her children. Whether he really believed the Spanish leader was the returning god Quetzalcoatl is '
         'doubted by historians today.',
         img='Quetzalcoatl', y=1517),
    life('Meeting Cortés',
         'In November 1519 he met Hernán Cortés on the causeway into the city, welcomed him as a guest and lodged the '
         'Spaniards in a palace. Days later, Cortés took him prisoner in his own city.',
         img='Hernán Cortés', cap='Hernán Cortés', y=1519, at='tenochtitlan'),
    life('Death',
         'In 1520, after the Spaniards massacred Aztec nobles at a festival, the city rose up. Moctezuma was brought out to '
         'calm the crowd and was struck by stones. Whether he died of those wounds or was killed by the Spaniards is still '
         'argued.',
         y=1520, at='tenochtitlan'),
    legacy('Moctezuma ruled the Aztec Empire at its height, and saw it fall to a few hundred Spaniards and their many '
           'native allies. His name lives on as the symbol of the last days of the Aztecs.',
           'Ruled the Aztec Empire at its height',
           "Lord of Tenochtitlan, one of the world's largest cities",
           'His capture began the fall of the Aztecs'),
)

story('vasco-da-gama', 'The Portuguese captain who found the sea route from Europe to India.',
    life('A nobleman of the sea',
         'Vasco da Gama was born around 1469 in Sines, a fishing port in Portugal, into a minor noble family. Tough and '
         'hot-tempered, he was chosen by King Manuel I to finish what Prince Henry had begun: to reach India by sea.',
         img='Sines', y=1469, at=(-8.87, 37.95), where='Sines'),
    win('Around Africa',
        'He sailed from Lisbon in July 1497 with four ships. Swinging far out into the Atlantic, he spent three months out '
        'of sight of land, longer than any sailor before him, then rounded the Cape of Good Hope and sailed up the coast '
        'of East Africa.',
        img='Cape of Good Hope', y=1497, at='cape_good_hope'),
    win('India',
        'At Malindi he found a pilot who knew the monsoon winds, and in May 1498 reached Calicut in India, the great spice '
        'port. Asked what they had come for, his men answered: "Christians and spices."',
        img='Black pepper', y=1498, at='calicut'),
    tale('Poor presents',
         "His gifts for Calicut's ruler were cloth, hats, coral, sugar and honey, and the court laughed: the poorest "
         'merchant brought better. Still, he sailed home with spices worth many times the cost of the voyage. Half his men '
         'died on the way, mostly of scurvy.',
         y=1499, at='lisbon'),
    life('Return with cannon',
         'On his second voyage in 1502 he came with warships and bombarded Calicut. He captured a ship of Muslim pilgrims '
         'and burned it with hundreds of people on board. Portugal built forts along the coasts of Africa and India.',
         y=1502, at='calicut'),
    life('Viceroy of India',
         'In 1524 he was sent back as viceroy of Portuguese India, but fell ill and died in Cochin on Christmas Eve, a few '
         'months after arriving.',
         img='Kochi', y=1524, at='cochin'),
    legacy("Da Gama's voyage opened the first sea route from Europe to Asia. It tied the world's trade together by sea, "
           'and began centuries of European empire in Asia.',
           'First to sail from Europe to India',
           'Opened the sea route around Africa',
           'Began the Portuguese empire in Asia',
           img='Jerónimos Monastery', cap='Jerónimos Monastery in Lisbon, built with spice money, where he lies', at='lisbon'),
)

story('niccolo-machiavelli', 'The Florentine who wrote The Prince, a ruthless rulebook for rulers.',
    life('A servant of the republic',
         'Niccolò Machiavelli was born in Florence in 1469. When the Medici were driven out and Florence became a '
         'republic, he rose to be one of its top officials, handling its dealings with other states and setting up a '
         'citizen army.',
         img='Palazzo Vecchio', y=1498, at='florence'),
    tale('Watching Cesare Borgia',
         "As an envoy he met kings and popes, and watched Cesare Borgia, the pope's ruthless son, carve out a state in "
         'central Italy. Borgia invited his rebellious captains to make peace, then had them strangled. Machiavelli '
         'admired his nerve.',
         img='Cesare Borgia', y=1502),
    life('Tortured, then retired',
         'When the Medici came back in 1512, Machiavelli was sacked, accused of plotting, and tortured, hung by his wrists '
         'from a rope. He confessed nothing, was released, and retired to his small farm outside Florence.',
         y=1513, at='florence'),
    tale('Dinner with the ancients',
         'In a famous letter he describes his evenings on the farm. He takes off his muddy clothes, puts on robes fit for '
         'a court, and enters his study to talk with the great men of the past in their books, for four hours forgetting '
         'every trouble.',
         y=1513, at=(11.24, 43.69), where="Sant'Andrea in Percussina"),
    work('The Prince',
         'There he wrote The Prince, a handbook for rulers. It said a prince must sometimes be cruel to keep the peace, '
         'that it is safer to be feared than loved, and that a ruler must be a fox to spot traps and a lion to scare off '
         'wolves.',
         img='The Prince', y=1513),
    legacy('Machiavelli was the first to write about politics as it really works, not as it ought to. "Machiavellian" '
           'now means cunning and ruthless, but he is also called the founder of modern political science.',
           'Wrote The Prince',
           'A founder of modern political thought',
           'His name became a word for ruthless cunning'),
)

story('guru-nanak', 'The founder of Sikhism, who taught one God and the equality of all people.',
    life('A boy who asked questions',
         'Nanak was born in 1469 at Talwandi, near Lahore, in what is now Pakistan, to a Hindu family. As a boy he asked '
         'awkward questions. At the ceremony where he was to receive a sacred thread, he refused it and asked for a thread '
         'of kindness and truth that would never break.',
         img='Nankana Sahib', y=1469, at=(73.68, 31.45), where='Nankana Sahib'),
    win('No Hindu, no Muslim',
        'Working as a storekeeper at Sultanpur, he went to bathe in a river and disappeared for three days. When he came '
        'back he said: "There is no Hindu and no Muslim", meaning all are equal before the one God. Sikhs see this as the '
        'beginning of their faith.',
        img='Sultanpur Lodhi', y=1499, at=(75.14, 31.21), where='Sultanpur Lodhi'),
    life('The long journeys',
         'With his Muslim friend Mardana, who played the rabab, he travelled for more than twenty years, singing the hymns '
         'he composed, perhaps as far as Sri Lanka, Tibet, Mecca and Baghdad.',
         y=1510),
    tale('Where God is not',
         'A story says that in Mecca he fell asleep with his feet pointing towards the Kaaba. An angry man dragged his feet '
         'the other way, and found that the Kaaba seemed to turn with them. Nanak said: then point my feet where God is '
         'not.',
         y=1518, at='mecca'),
    win('Kartarpur and the langar',
        'He settled at Kartarpur, a village he founded on the river Ravi, and farmed the land. There he began the langar, '
        'a free kitchen where everyone, of any caste or faith, sits together on the floor and shares a meal.',
        img='Langar (Sikhism)', y=1521, at='kartarpur'),
    legacy('Guru Nanak founded Sikhism, followed today by about 25 million people. His hymns are in the Sikh holy book, '
           'and his teaching of one God, equality and service lives on in langars that feed millions every day.',
           'Founder of Sikhism',
           'Taught one God and the equality of all people',
           'Began the langar, the free community kitchen',
           img='Golden Temple', cap='The Golden Temple at Amritsar', at='amritsar'),
)

from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('spain-in-europe', "Spain's wars for Europe", 'wars', (1494, 1659),
      'For a century and a half the kings of Spain fought France, the Turks and the Protestants to be masters of Europe.',
      figure(None, 'The Great Captain',
             'In 1494 the French king Charles VIII marched the length of Italy to seize Naples. Ferdinand of Aragon sent '
             'his best soldier, Gonzalo Fernández de Córdoba, the Great Captain. In 1503 at Cerignola his arquebusiers, '
             'firing from behind a ditch, cut down the French knights, and Naples became Spanish for two hundred years.',
             img='Gonzalo Fernández de Córdoba', kick='How it began', y=1503, at='cerignola'),
      figure('charles-v-holy-roman-emperor', 'Heir to half of Europe',
             "Ferdinand's grandson Charles inherited Spain and its Italian kingdoms from his mother's family, and the "
             "Netherlands and Austria from his father's. In 1519 the German princes, well bribed, elected him Holy Roman "
             'Emperor. No ruler since Charlemagne had held so much of Europe, and France found itself surrounded.',
             y=1519, at='frankfurt'),
      made('The tercios',
           "From the 1530s Spain's foot soldiers were formed into tercios: permanent regiments of pikemen and men with "
           'guns, who trained and lived together and were paid, when the money came, from Spain.',
           'For a century they were the most feared infantry in Europe, fighting from Tunis to the Netherlands. Spanish '
           'foot soldiers had already captured the king of France himself, at Pavia in 1525.',
           img='Tercio', y=1536, at='milan'),
      work('The emperor at Mühlberg',
           'In Germany the Protestant princes had joined in a league against the Catholic emperor. In April 1547 Charles '
           "and the Duke of Alba forded the Elbe at Mühlberg, routed the league's army and took its leader prisoner. "
           'Titian painted Charles riding to that battle in armour, alone, gaunt and calm, and set the pattern for royal '
           'portraits on horseback for centuries.',
           img='Equestrian Portrait of Charles V', y=1548, at='muhlberg'),
      figure('philip-ii-of-spain', 'The sun never sets',
             'Worn out, Charles gave up his crowns in 1556. His brother Ferdinand, already ruler of Austria, became '
             'emperor, and his son Philip II took Spain, Italy, the Netherlands and the Americas. In 1580 Philip claimed Portugal and its empire too. '
             'One king now ruled from Mexico to Manila, and it was said that the sun never set on his lands.',
             y=1556, at='brussels'),
      figure('william-the-silent', 'The Netherlands rise',
             "Philip's heavy taxes and his burning of Protestants drove the Netherlands to revolt. In 1568 the Duke of "
             'Alba beheaded two great nobles, Egmont and Horn, in the main square of Brussels, and William of Orange led '
             'the rebels. Unpaid Spanish soldiers sacked Antwerp in 1576, and the northern provinces broke away to form '
             'the Dutch Republic.',
             y=1568, at='brussels'),
      battle('Lepanto',
             'On 7 October 1571 the fleet of the Holy League, mostly Spanish and Venetian, met the Ottoman fleet in the '
             'Gulf of Patras, off western Greece. Over 400 galleys fought it out in a few hours, one of the largest sea '
             "battles ever fought. The Christians won, led by Philip's young half-brother, Don John of Austria. Among the "
             'wounded was a Spanish soldier named Miguel de Cervantes.',
             img='Battle of Lepanto', y=1571, at='lepanto'),
      made('Silver and bankruptcy',
           'Silver from the mines of Potosí and Mexico poured into Seville, and Philip spent it before it arrived, on '
           'armies in Italy and the Netherlands and fleets at sea, among them the Armada of 1588.',
           'It was never enough. The crown went bankrupt in 1557, 1560, 1575 and 1596, unpaid soldiers mutinied, and the '
           'taxes fell hardest on Castile, which grew poorer as its king grew mightier.',
           img='Cerro Rico', y=1575, at='potosi'),
      work('The Surrender of Breda',
           'The war with the Dutch began again in 1621. In 1625 the Genoese general Ambrogio Spinola took the fortress '
           'of Breda after a siege of ten months, and ten years later Diego Velázquez painted him receiving its keys. '
           "Spinola lays a hand on the Dutch commander's shoulder instead of letting him kneel: Spanish pride, painted "
           'with a rare courtesy.',
           img='The Surrender of Breda', y=1635, at='breda'),
      battle('Rocroi',
             'France joined the war against Spain in 1635, and in 1640 both Catalonia and Portugal rose against Madrid. '
             'In May 1643 a Spanish army invading France besieged the little fortress town of Rocroi. The French, led by '
             'the 21-year-old Duke of Enghien, broke the Spanish horsemen, and the veteran tercios stood their ground '
             'until most of them were killed or taken.',
             y=1643, at='rocroi'),
      legacy('In 1659, on an island in a border river, Spain and France made the Peace of the Pyrenees. Philip IV gave '
             'up Roussillon and Artois, and his daughter married the young Louis XIV. Spain kept its empire for another '
             '150 years, but the leadership of Europe had passed to France.',
             "Spain's kings ruled much of Europe and the Americas",
             "The tercios were Europe's best soldiers for a century",
             'In 1659 the lead in Europe passed to France',
             y=1659, at='pheasant_island'),
      war='spain-in-europe', wiki='Habsburg Spain', img='Equestrian Portrait of Charles V', at='madrid')

event('german-peasants-war', "The German Peasants' War", 'uprising', (1524, 1525),
      "Peasants across Germany rose to be free of serfdom, in Europe's greatest revolt before 1789, and were massacred.",
      scene('Snail shells',
            'German peasants owed their lords rents, labour and fees, and the lords kept adding more, while the woods, '
            'rivers and game were closed to them. In June 1524, the story goes, the countess of Stühlingen, near the '
            'Swiss border, ordered her peasants to gather snail shells for her in the middle of the harvest. They '
            'refused, and the revolt began.',
            kick='How it began', y=1524, at='stuhlingen'),
      work('The Twelve Articles',
           'In March 1525 the peasant bands of Upper Swabia met in the town of Memmingen and agreed on Twelve Articles. '
           'They asked to choose their own pastors, to fish and hunt, and to be free of serfdom, since Christ had '
           'redeemed all people with his blood. Printed again and again, some 25,000 copies spread across Germany in two '
           'months.',
           img='Twelve Articles', y=1525, at='memmingen'),
      scene('Easter at Weinsberg',
            'The revolt spread north and east, and townsfolk and miners joined in. On Easter Day 1525 a band from the '
            'Odenwald stormed the town of Weinsberg and made Count Helfenstein and his knights run between lines of '
            'pikes to their deaths, while his wife, a daughter of the old emperor Maximilian, looked on. Lords across '
            'Germany heard of it with terror.',
            y=1525, at='weinsberg'),
      figure(None, 'The knight with the iron hand',
             'Götz von Berlichingen, a knight who had lost his right hand in a siege and wore one made of iron, led the '
             'Odenwald band for a month, forced to, he said later. Florian Geyer, another knight, led a Black Company of '
             "peasants. With other bands they besieged the bishop's fortress above Würzburg, and failed to take it.",
             img='Götz von Berlichingen', y=1525, at='wurzburg'),
      figure(None, 'The preacher',
             'In Thuringia the radical preacher Thomas Müntzer told the peasants that the end of the world was near, and '
             'that the godless lords must fall. He marched from Mühlhausen to join the peasant army under a white banner '
             "painted with a rainbow. His enemies later claimed he had promised to catch the princes' cannonballs in his sleeves.",
             img='Thomas Müntzer', y=1525, at='muhlhausen'),
      figure('martin-luther', 'Luther takes sides',
             "The peasants quoted Martin Luther, who had taught that Christians were free. But Luther feared chaos more "
             'than he loved their cause. In May 1525 he wrote a pamphlet against the "murderous, thieving hordes" of '
             'peasants, urging the princes to strike them down like mad dogs. Many peasants never trusted him again.',
             y=1525, at='wittenberg'),
      battle('Frankenhausen',
             "On 15 May 1525 the princes' armies found the peasant army behind a ring of wagons on a hill above "
             'Frankenhausen. Their cannon opened fire, the peasants broke, and some 6,000 were cut down as they fled, for '
             'the loss of a handful of soldiers. Müntzer was found hiding in a house in the town, tortured and beheaded.',
             y=1525, at='frankenhausen'),
      cost('The reckoning',
           "One by one the bands were destroyed. At Saverne in Alsace the Duke of Lorraine's men massacred peasants who "
           'had surrendered. Leaders were beheaded and villages burned and fined. The great sculptor Tilman '
           'Riemenschneider, a councillor of Würzburg who had sided with the rebels, was jailed and, it is said, tortured.',
           num='About 100,000', of='peasants and townsfolk killed', y=1525, at='wurzburg'),
      legacy('The princes won. Serfdom lasted in parts of Germany into the 1800s, and the Reformation, which had seemed '
             "to promise freedom, came under the rulers' control: they now chose their subjects' faith. But the revolt "
             'was never forgotten, and Germans from Goethe to the rulers of East Germany made heroes of its leaders.',
             "Europe's biggest rising before the French Revolution",
             'Crushed in a few weeks of 1525',
             'The princes took charge of the Reformation'),
      war='german-peasants-war', wiki="German Peasants' War", at='memmingen')

event('arauco-war', 'The Arauco War', 'war', (1536, 1656),
      'For more than a century the Mapuche of southern Chile fought off the Spanish conquerors, and kept their freedom.',
      figure('pedro-de-valdivia', 'Santiago',
             'In 1540 Pedro de Valdivia, a veteran of the conquest of Peru, marched south across the Atacama desert with '
             'about 150 Spaniards and many more native carriers. In February 1541 he founded Santiago. Within months the '
             'chief Michimalonco attacked and burned the new town, and the Spaniards held on only by a desperate fight.',
             kick='How it began', y=1541, at='santiago'),
      scene('Gold',
            'In 1550 Valdivia pushed south into the lands of the Mapuche, a free people of farmers and herders who had '
            'no king and had never been ruled by the Inca. He founded Concepción, then more towns and forts beyond the '
            'Biobío river, and gave the conquered people to his men to wash gold in the rivers. Many died of overwork and new '
            'diseases.',
            y=1550, at='concepcion'),
      figure(None, 'Lautaro',
             "Lautaro, a Mapuche youth, had been taken to serve as Valdivia's groom, and watched how the Spaniards fought "
             'and cared for their horses. He escaped and taught his people to fight in waves, one squadron relieving '
             'another until the horsemen tired. In December 1553 at Tucapel they wiped out Valdivia\'s column, and the '
             'governor was killed.',
             img='Lautaro', y=1553, at='tucapel'),
      scene('Lautaro marches north',
            'Lautaro beat the Spaniards again at Marihueñu in 1554 and forced them to abandon Concepción. In 1557 he '
            'marched north to free the peoples around Santiago, but by the Mataquito river a Spanish force fell on his '
            'camp at dawn. Lautaro was killed, still in his early twenties.',
            y=1557, at='mataquito'),
      figure(None, 'Caupolicán',
             'Spain sent a new governor, García Hurtado de Mendoza, with fresh troops by sea. In 1558 the war leader '
             'Caupolicán was captured and put to death at Cañete, impaled on a stake, a horror the Spaniards meant as a '
             'warning. It did not end the war. When one Mapuche leader fell, another was chosen to take his place.',
             img='Caupolicán', y=1558, at='canete'),
      work('La Araucana',
           'A young Spanish soldier, Alonso de Ercilla, fought in these campaigns and wrote an epic poem about them, La '
           'Araucana, printed from 1569. He praised the courage of the Mapuche as much as that of his own side. It was '
           'the first great epic poem about the Americas, and it made Lautaro and Caupolicán heroes in Europe.',
           img='La Araucana', y=1569, at='concepcion'),
      battle('Curalaba',
             'In December 1598 the war leader Pelantaro ambushed Governor Martín García Óñez de Loyola at dawn at '
             'Curalaba, and killed him and nearly all his men. A great rising followed. Within six years every Spanish '
             'town between the Biobío and the island of Chiloé, from La Imperial to Valdivia and Osorno, had been destroyed or abandoned.',
             y=1598, at='curalaba'),
      turn('A river for a border',
           'To hold a line of forts along the Biobío, Spain had to keep a paid standing army in Chile, rare in its '
           'empire, and raids for slaves went on across the river. In 1641, at the parliament of Quillín, the governor '
           'and the Mapuche chiefs agreed that the Biobío would be the border, and that the Mapuche south of it were '
           'free.',
           y=1641, at='quillin'),
      legacy('The frontier held for two more centuries, with trade, missions and regular parliaments as well as raids. '
             'The Mapuche kept their land until Chile and Argentina conquered it in the 1880s. Today they are the largest '
             'native people of Chile, and Lautaro is honoured as a national hero.',
             'More than a century of war',
             'Spain never conquered the Mapuche',
             'Their land stayed free until the 1880s'),
      war='arauco-war', wiki='Arauco War', at='tucapel')

event('qing-invasions-of-korea', 'The Manchu invasions of Korea', 'invasion', (1627, 1637),
      'Twice the Manchus crossed the frozen Yalu river, and they forced the king of Korea to kneel before their emperor.',
      scene('Between two empires',
            "Korea's Joseon kings were loyal to Ming China, which had saved them from the Japanese in the 1590s. But in "
            'the north the Manchus, led by Nurhaci, were building a new state and fighting the Ming. In 1619 Korean '
            'troops sent to help the Ming were beaten and surrendered, and in 1623 a new king, Injo, turned firmly '
            'against the Manchus.',
            kick='How it began', y=1619, at='seoul'),
      scene('The first invasion',
            "In January 1627 Nurhaci's son Hong Taiji sent some 30,000 horsemen across the frozen Yalu. They took the "
            'border fortresses and Pyongyang, and King Injo fled to Ganghwa Island, off the coast near Seoul. With no '
            'ships to reach him and a war with the Ming to fight, the Manchus agreed to a peace that made Korea their '
            '"younger brother".',
            y=1627, at='ganghwa'),
      figure('hong-taiji', 'An emperor at Mukden',
             'Hong Taiji grew stronger. He raided to the walls of Beijing, and the Mongols of the south submitted to him. '
             'In 1636 at Mukden he declared a new dynasty, the Qing, with himself as emperor, and demanded that Korea '
             'treat him as its lord. When Korean envoys at the ceremony refused to bow, he prepared for war.',
             y=1636, at='mukden'),
      scene('Across the ice',
            'In December 1636 Hong Taiji crossed the frozen Yalu with about 120,000 men. His horsemen rode straight past '
            'the Korean mountain fortresses that were meant to stop invaders, and reached Seoul in under two weeks. The road '
            'to Ganghwa was cut, and King Injo had to shelter in the mountain fortress of Namhansanseong.',
            y=1636, at='uiju'),
      scene('Namhansanseong',
            'Some 13,000 soldiers held its walls through a bitter winter, with food for fifty days. Relief armies from '
            'the provinces were beaten one by one. Inside, the court argued: some ministers wanted to die fighting for '
            "the honour of the Ming, others said the kingdom must survive. Then news came that Ganghwa had fallen, with "
            "the king's family.",
            img='Namhansanseong', y=1637, at='namhansanseong'),
      figure('injo-of-joseon', 'Samjeondo',
             'On 24 February 1637 King Injo came down from the fortress in plain clothes. At Samjeondo, on the Han river, '
             'he knelt to Hong Taiji three times and bowed his head to the ground nine times. Korea broke with the Ming, '
             'paid tribute to the Qing, and sent the crown prince and his brother to Mukden as hostages.',
             y=1637, at='samjeondo'),
      made('A stone of shame',
           "The Qing made Korea raise a great stone at Samjeondo, carved in Manchu, Mongolian and Chinese, praising the "
           "emperor's mercy in sparing the kingdom.",
           'Koreans saw it as a mark of shame. It was pulled down in 1895, when Korea broke free of the Qing, and it has '
           'been buried and set up again more than once since.',
           img='Samjeondo Monument', y=1639, at='samjeondo'),
      figure(None, 'The hostage prince',
             'Crown Prince Sohyeon spent eight years with the Qing, and went with them into Beijing when they took it in '
             '1644. There he befriended the German Jesuit Adam Schall and learned of Western science and Christianity. '
             'He came home in 1645 full of new ideas, and died suddenly two months later. Many suspected poison.',
             img='Crown Prince Sohyeon', y=1645, at='beijing'),
      legacy('Korea paid tribute to the Qing until 1895, but its scholars long believed that Korea, not Manchu-ruled '
             'China, was now the true keeper of Ming civilisation. Many women carried off as captives and later ransomed '
             'were shunned when they came home. Namhansanseong is now a World Heritage Site.',
             'Two invasions, in 1627 and 1636',
             'Korea bowed to the Qing until 1895',
             'Its scholars stayed loyal to the Ming in spirit'),
      states=('Manchu Empire',), war='qing-invasions-of-korea', wiki='Qing invasion of Joseon', at='namhansanseong')

event('the-deluge', 'The Deluge', 'wars', (1648, 1667),
      "Cossacks, Russians and Swedes flooded into Poland-Lithuania, and one of Europe's largest states nearly drowned.",
      figure('bohdan-khmelnytsky', "A Cossack's wrong",
             'Bohdan Khmelnytsky was a Cossack officer in Ukraine, then part of the Polish-Lithuanian Commonwealth. In '
             '1647 a Polish nobleman seized his estate, carried off the woman he loved and had his son flogged, and the '
             'courts gave him no justice. He fled to the Cossacks of the Zaporozhian Sich, beyond the Dnieper rapids, and '
             'called them to war.',
             kick='How it began', y=1648, at='chyhyryn'),
      battle('Yellow Waters',
             'With Crimean Tatar horsemen as allies, the Cossacks destroyed two Polish armies in May 1648: at Zhovti '
             'Vody, the Yellow Waters, and at Korsun, where both Polish commanders were captured. Peasants across '
             'Ukraine rose against their lords, and the rebels swept west toward Lviv.',
             y=1648, at='zhovti_vody'),
      scene('Massacres',
            'The rising brought terrible massacres. Rebels killed Polish nobles, Catholic priests and above all Jews, '
            "whom they saw as the lords' agents. Thousands of Jews died in towns like Nemyriv and Tulchyn, and Jewish "
            'chroniclers remembered it as one of the great catastrophes of their history. Polish troops answered with '
            'massacres of their own.',
            y=1648, at='nemyriv'),
      figure('alexis-of-russia', 'Pereiaslav',
             'Beaten at Berestechko in 1651 when his Tatar allies fled, Khmelnytsky looked for a stronger protector. In '
             'January 1654, at Pereiaslav, the Cossack officers swore loyalty to Tsar Alexis of Russia, who shared their '
             'Orthodox faith. That summer Russian armies invaded the Commonwealth. They took Smolensk that autumn, and '
             'Minsk and Vilnius in 1655.',
             y=1654, at='pereiaslav'),
      figure('charles-x-gustav', 'The Swedish flood',
             'In July 1655 King Charles X Gustav of Sweden invaded from the north and west. Polish nobles went over to '
             'him almost without a fight, Warsaw and Kraków fell, and King John Casimir fled to Silesia. With Russians, '
             'Cossacks and Swedes all inside the country, Poles came to call these years the Deluge.',
             y=1655, at='warsaw'),
      battle('Jasna Góra',
             'A few places held out. At Częstochowa the monks and soldiers of the monastery of Jasna Góra, home of a '
             'famous icon of the Virgin Mary, beat off a Swedish siege for about forty days at the end of 1655. Poles '
             'took it as a miracle, and it turned a lost war into a crusade against Lutheran invaders.',
             img='Siege of Jasna Góra', y=1655, at='czestochowa'),
      figure('john-ii-casimir-vasa', "The king's vow",
             'John Casimir came back at the start of 1656. In the cathedral of Lviv he placed his kingdom under the protection of the '
             'Virgin Mary, naming her Queen of Poland, and promised to ease the burdens of the peasants once peace came. '
             'Stefan Czarniecki led a guerrilla war that wore the Swedes down, and the country rose behind them.',
             y=1656, at='lviv'),
      song('Poland Is Not Yet Lost',
           "Czarniecki even followed the Swedes to Denmark in 1658, and swam his horses across the sea to the island of "
           "Als. Poland's national anthem, written in 1797 when the country had been wiped off the map, still sings of "
           'him coming home across the sea to save his homeland.',
           page='Poland Is Not Yet Lost', hint='instrumental', y=1658, at='als'),
      turn('Oliva and Andrusovo',
           "Sweden's enemies multiplied, and after Charles X Gustav died, the Peace of Oliva in 1660 ended the Swedish "
           'war. The war with Russia dragged on until the Truce of Andrusovo in 1667 split Ukraine along the Dnieper. '
           'Russia kept Smolensk and the lands east of the river, and Kyiv, which was meant to be handed back after two '
           'years and never was.',
           y=1667, at='andrusovo'),
      work('The Deluge',
           'Two centuries later, when Poland had been divided up by its neighbours, Henryk Sienkiewicz wrote a great '
           'novel about the Swedish war, The Deluge, to lift the hearts of his people. Read by generations of Poles and '
           'filmed in 1974, it gave the wars the name most Poles know them by.',
           img='The Deluge (novel)', y=1886, at='warsaw'),
      legacy('The Commonwealth survived, but it lost perhaps a third of its people to war, hunger and plague, and it '
             'never recovered its strength. In the 1700s its neighbours divided it up. In Ukraine, Khmelnytsky is '
             "honoured as the founder of a Cossack state, and Russia, holding Kyiv, became eastern Europe's rising power.",
             'Cossacks, Russians and Swedes all invaded',
             'Poland-Lithuania lost perhaps a third of its people',
             'Russia won Kyiv and eastern Ukraine'),
      war='the-deluge', wiki='Deluge (history)', at='warsaw')

event('nader-shah-campaigns', "Nader Shah's wars", 'conquest', (1729, 1747),
      "A soldier from a poor family saved Persia from its invaders, made himself shah and sacked Delhi, then was murdered.",
      figure('nader-shah', 'A soldier from Khorasan',
             'Nader was born around 1688 in Khorasan, in the northeast of Iran, into a poor family of the Turkic Afshar '
             'tribe. By the 1720s Persia was falling apart: Afghan rebels had taken the capital, Isfahan, and the '
             'Ottomans and Russians were seizing its provinces. Nader, by then a warlord with his own army, offered his '
             'sword to the fugitive Safavid heir, Tahmasp.',
             kick='How it began', y=1726, at='mashhad'),
      battle('Isfahan retaken',
             "In 1729 Nader's drilled musketeers and cannon routed the Afghans at Damghan, and again near Isfahan, and "
             'Tahmasp entered his ruined capital. Nader chased the Afghans south past Shiraz until their army fell apart. '
             'Then he turned west and drove the Ottomans out of western Persia.',
             y=1729, at='isfahan'),
      turn('Shah on the Mughan plain',
           'Nader deposed Tahmasp in 1732 and ruled for his baby son. After crushing the main Ottoman army in 1735, he '
           'called the chiefs and nobles of Persia to a great gathering on the Mughan plain in 1736. As he had arranged, '
           'they asked him to become shah. The Safavid dynasty, which had ruled for over two centuries, was over.',
           y=1736, at='mughan'),
      battle('Karnal',
             'Nader then struck east. He took Kandahar after a year-long siege, then Kabul, and in 1738 forced the Khyber '
             'Pass into India. On 24 February 1739 at Karnal, north of Delhi, he met the army of the Mughal emperor '
             'Muhammad Shah, far larger but slow and badly led, and beat it in about three hours.',
             y=1739, at='karnal'),
      cost('Delhi',
           'Nader entered Delhi as the guest of the beaten emperor. When a rumour spread that he had been killed, people '
           'attacked his soldiers. The next morning, 22 March 1739, he sat in a mosque and let his troops loose on the '
           'city, until in the afternoon he sheathed his sword and called a halt.',
           num='About 20,000', of='people killed in Delhi in one day', y=1739, at='delhi'),
      made('The Peacock Throne',
           'Nader carried home the treasure of the Mughals: gold, jewels, the jewelled Peacock Throne of Shah Jahan, and '
           'a huge diamond, the Koh-i-Noor, the Mountain of Light, a name he is said to have given it.',
           'It was so much that he let Persia off its taxes for three years. The throne was broken up after his death, '
           'and the Koh-i-Noor passed from hand to hand until it ended up among the British crown jewels.',
           img='Koh-i-Noor', y=1739, at='delhi'),
      scene('Bukhara and Khiva',
            'On his way home Nader crossed the Oxus into Central Asia. The khan of Bukhara gave in without a fight. The '
            'khan of Khiva fought, lost and was put to death, and thousands of Persians held as slaves in Khiva were set '
            "free. Nader's empire now reached from the Caucasus to the Indus and the Oxus.",
            y=1740, at='khiva'),
      scene('A blinded son',
            'The wars went on, and grew harder. In the mountains of Dagestan his army bled in a guerrilla war it could '
            'not win. After a shot was fired at him from a forest in 1741, Nader came to suspect his eldest son, Reza '
            'Qoli, and had him blinded. He regretted it bitterly, and his cruelty grew.',
            y=1742, at='derbent'),
      turn('Death in the tent',
           'Taxes to pay for his wars drove province after province into revolt. Nader had officials executed and towers '
           'built from the skulls of rebels. In June 1747, at a camp near Quchan, a group of his own officers burst into '
           'his tent at night and killed him. Within months his empire had broken apart.',
           y=1747, at='quchan'),
      figure('ahmad-shah-durrani', 'The guard who rode away',
             "Ahmad Khan, the young commander of Nader's Afghan guard, rode off to Kandahar with his men, and with the "
             'Koh-i-Noor. That October a council of Afghan chiefs chose him as their king, Ahmad Shah. His Durrani empire '
             "was the beginning of today's Afghanistan.",
             y=1747, at='kandahar'),
      legacy('Nader was one of the last great conquerors of Asia, and for a few years Persia was the strongest power in '
             'the Islamic world. But he left little that lasted. Persia fell into years of civil war, and the Mughals '
             'never recovered from the sack of Delhi, which opened India to the Marathas and the British.',
             'He saved Persia, then bled it dry',
             'The sack of Delhi broke the Mughals',
             'Afghanistan was born from his empire'),
      states=('Persia', 'Afghanistan'), war='nader-shah-campaigns', wiki='Campaigns of Nader Shah',
      img='Nader Shah', at='isfahan')

event('qing-conquest-dzungaria', 'The Qing conquest of Dzungaria', 'conquest', (1755, 1759),
      "China's Qianlong Emperor destroyed the last great nomad empire of the steppe, and most of its people with it.",
      scene('The last steppe empire',
            'The Dzungars were western Mongols who had built the last great empire of nomad horsemen, ruling from the Ili '
            'valley over the steppes and oases of Central Asia. For seventy years they had fought the Qing emperors of '
            'China for the lands between. But when their khan died in 1745, his sons and nobles fought each other for '
            'the throne.',
            kick='How it began', y=1745, at='ili'),
      figure('qianlong-emperor', "The emperor's chance",
             'In 1754 one of the losers, the noble Amursana, fled to the Qing and asked for help. The Qianlong Emperor saw '
             'his chance to end the Dzungar threat for good. In 1755 two Qing armies marched west with Amursana, clan '
             'after clan went over to them, and the Dzungar capital in the Ili valley fell almost without a fight.',
             y=1755, at='beijing'),
      scene('Amursana turns',
            'Amursana had hoped to rule all the Dzungars, but Qianlong split them into four small khanates under his '
            'control. That autumn Amursana rose against the Qing. The small garrison left at Ili was wiped out, and its '
            'general killed himself. The Qing drove Amursana into the Kazakh steppe, but the Dzungars kept rising.',
            y=1755, at='ili'),
      cost('Wiped out',
           'In 1757 Qianlong ordered that the Dzungars be wiped out. His armies swept the land, killing the men and '
           'carrying off women and children as slaves, while smallpox raced through the camps. Amursana fled to Russia '
           'and died of smallpox. Of perhaps 600,000 Dzungars, most were killed or died, and many historians call '
           'it a genocide.',
           num='Most of 600,000', of='Dzungars killed, dead of disease or fled', y=1757, at='ili'),
      scene('The oasis cities',
            'South of the mountains, the Muslim oasis cities of the Tarim Basin, led by two brothers of a family of holy '
            'men, the Khojas, now defied the Qing. Qing armies took Kucha, were themselves trapped for months near '
            'Yarkand, then took Kashgar and Yarkand in 1759. The Khojas fled to Badakhshan, where its ruler had them '
            'killed.',
            y=1759, at='kashgar'),
      work('Battles in copper',
           'Qianlong had his victories drawn by the Jesuit painters at his court, among them Giuseppe Castiglione. In '
           '1765 he sent sixteen of their battle scenes to Paris, where the best engravers in Europe cut them into '
           'copper plates. The prints, finished by 1775, show tiny Dzungar horsemen scattering before the Qing banners.',
           img='Giuseppe Castiglione', y=1765, at='beijing'),
      turn('The New Frontier',
           'The Qing called the conquered lands Xinjiang, the New Frontier, and filled the empty grasslands with '
           'soldiers, Han Chinese farmers, Muslims from the oases and Kazakhs. In 1771 the Torghuts, cousins of the '
           'Dzungars who had moved to the Volga more than a century before, trekked back across the steppe to settle there, and '
           'lost more than half their people on the way.',
           y=1771, at='ili'),
      legacy('The conquest gave the Qing a vast new territory and drew borders of China much like those of today. It '
             'ended two thousand years in which nomad empires of the steppe had threatened China. But the Dzungars, a '
             'whole people, almost vanished, and their name lives on mostly in the Dzungarian Basin.',
             'The last steppe empire was destroyed',
             'Most of the Dzungars died or fled',
             'Xinjiang became part of the Qing empire'),
      states=('Qing Empire',), war='qing-conquest-dzungaria', wiki='Dzungar genocide', at='ili')

event('french-conquest-algeria', 'The French conquest of Algeria', 'conquest', (1830, 1847),
      'France took Algiers in three weeks, then needed seventeen years of war to defeat the emir Abdelkader.',
      scene('A blow with a fly whisk',
            'In 1827, in a quarrel over old debts for grain, the ruler of Algiers, the Dey Hussein, struck the French '
            'consul with his fly whisk. France blockaded the port. In 1830 the unpopular government of King Charles X, '
            'hoping for a victory to win over voters, sent a fleet and 34,000 soldiers to take revenge.',
            kick='How it began', y=1827, at='algiers'),
      battle('Algiers falls',
             "The army landed on the beach at Sidi Fredj in June 1830, beat the Dey's forces and marched on Algiers, "
             'which surrendered on 5 July. The Dey sailed into exile, and his treasury was looted. Three weeks later '
             'Charles X lost his throne in a revolution in Paris, but France kept Algiers.',
             y=1830, at='sidi_ferruch'),
      figure('abdelkader', 'The emir',
             'In the west, the tribes chose a 24-year-old scholar and horseman, Abdelkader, as their emir in 1832. He '
             'built a state of his own around Mascara, with taxes, workshops, schools and a regular army. He beat the '
             'French in battle, and in 1837 France made peace, leaving him two thirds of Algeria.',
             y=1832, at='mascara'),
      battle('Constantine',
             'In the east, Ahmed Bey held Constantine, a city on a rock above a deep gorge. A first French attack in 1836 '
             'failed in rain and snow. In October 1837 the French came back with heavy guns, blew a breach in the walls '
             'and stormed the city street by street.',
             y=1837, at='constantine'),
      figure(None, 'Burning the harvest',
             'War broke out again in 1839. In 1841 General Bugeaud took command, with an army that grew to over 100,000 '
             'men, and changed the way France fought. Fast columns burned crops, cut down orchards and seized herds, to '
             "starve the tribes into giving up. In 1843 French cavalry captured the emir's moving capital of tents, his "
             'smala, with thousands of his people.',
             img='Thomas Robert Bugeaud', y=1843, at='mascara'),
      work('A painting 21 metres long',
           'The king of France ordered a painting of the raid on the smala for his palace at Versailles. Horace Vernet\'s '
           'canvas, finished in 1845, is over 21 metres long, one of the largest paintings in the world: a sea of '
           "fleeing women, camels and tents, with the king's son on horseback in the middle.",
           img='Horace Vernet', y=1845, at='versailles'),
      scene('The caves of Dahra',
            'In 1845 a holy man called Bou Maza led a great revolt in the Dahra mountains. When villagers of the Ouled '
            'Riah tribe hid in caves with their animals, Colonel Pélissier had fires lit at the entrance. Hundreds of '
            'men, women and children suffocated. The news caused an outcry in France, but Bugeaud defended him.',
            y=1845, at='dahra'),
      turn('The emir gives up',
           'Abdelkader fought on from Morocco, and in 1845 he wiped out a French column at Sidi Brahim. But France had '
           'beaten Morocco in 1844 and made its sultan turn against him. Hunted on both sides of the border, he '
           'surrendered in December 1847, on the promise that he could go into exile in a Muslim land.',
           y=1847, at='ghazaouet'),
      legacy('France broke its promise and kept Abdelkader prisoner until 1852. Freed, he settled in Damascus, where in '
             '1860 he saved thousands of Christians from a massacre. Algeria was made part of France and filled with '
             'European settlers, while war, famine and disease took a heavy toll on its people. It won independence only '
             'in 1962.',
             'Algiers fell in three weeks in 1830',
             'Seventeen years of war to conquer the interior',
             'Algeria stayed French until 1962'),
      states=('Algeria (FR)',), war='french-conquest-algeria', wiki='French conquest of Algeria', at='algiers')

event('russian-conquest-central-asia', 'The Russian conquest of Central Asia', 'conquest', (1839, 1881),
      "Russia's armies crossed deserts and steppe to conquer the old Silk Road cities of Tashkent, Samarkand and Khiva.",
      scene('A winter march',
            'The khanate of Khiva, in an oasis on the Amu Darya river, raided Russian caravans and held Russians as '
            'slaves. In November 1839 the governor of Orenburg, Vasily Perovsky, set out to punish it with 5,000 men and '
            '10,000 camels. A terrible winter killed most of the camels, and he had to turn back without ever seeing '
            'Khiva.',
            kick='How it began', y=1839, at='orenburg'),
      scene('Forts across the steppe',
            'Russia learned to move slowly. It built lines of forts across the Kazakh steppe, put steamboats on the Aral '
            'Sea, and in 1853 stormed the fort of Ak-Mechet on the Syr Darya, held by the khanate of Kokand. Another '
            'line of forts pushed south from Siberia. Between the two lines lay Tashkent.',
            y=1853, at='ak_mechet'),
      battle('Tashkent',
             'In 1865 the Russian commander Mikhail Chernyaev attacked Tashkent, the biggest city of Central Asia, with fewer than 2,000 '
             'men and without clear orders. His men climbed its long walls at night, and after two days of street '
             "fighting the city gave in. The tsar's government, which had wanted to wait, kept the prize.",
             y=1865, at='tashkent'),
      figure(None, 'Kaufman',
             'General Konstantin von Kaufman, the first governor-general of Russian Turkestan, ruled from Tashkent almost '
             "like a king. In 1868 he marched against Bukhara and took Samarkand, Tamerlane's old capital, without a "
             'fight. While he chased the emir, a small garrison held the citadel of Samarkand against a rising for a '
             'week.',
             img='Konstantin Petrovich von Kaufmann', y=1868, at='samarkand'),
      work('The Apotheosis of War',
           'One of the defenders of Samarkand was a young painter, Vasily Vereshchagin. His pictures of the war showed '
           'its horror, not its glory. The most famous, The Apotheosis of War, painted in 1871, is a pyramid of skulls in '
           'the desert, dedicated, he wrote, to all great conquerors, past, present and to come.',
           img='The Apotheosis of War', y=1871, at='samarkand'),
      scene('Khiva',
            'In 1873 Kaufman sent columns across the deserts to Khiva from three sides. One had to turn back for lack of '
            'water, but the others met outside its walls, and the khan gave in. Khiva became a Russian protectorate, and '
            'its slave markets, where Persians and Russians had been sold for centuries, were closed.',
            y=1873, at='khiva'),
      made('White gold',
           'Russia ended the khanate of Kokand in 1876 and made its rich Fergana valley a province. When the American '
           "Civil War had cut off cotton from the United States, Russia's mills had turned to Central Asia.",
           "Cotton became the region's great crop. It fed Russian and later Soviet mills, and with its huge thirst for "
           'river water it helped, in the end, to dry up the Aral Sea.',
           y=1876, at='ferghana'),
      battle('Geok Tepe',
             'The Turkmen of the desert fought hardest. In 1879 they beat off an attack on their mud-walled fortress of '
             'Geok Tepe. General Skobelev came with a railway built across the sand, and in January 1881 blew a hole '
             'in the wall with a mine. Thousands of defenders and civilians were killed in the storm and the pursuit.',
             y=1881, at='geok_tepe'),
      legacy("Merv gave in in 1884, and Russia's border reached Afghanistan, the buffer between it and British India. "
             'Central Asia was ruled as a colony until 1917, then by the Soviets, and the borders they drew became those of '
             'Kazakhstan, Uzbekistan, Turkmenistan, Kyrgyzstan and Tajikistan.',
             'Tashkent fell in 1865, Samarkand in 1868',
             'Khiva and Bukhara became protectorates',
             'Soviet borders made five new nations'),
      war='russian-conquest-central-asia', wiki='Russian conquest of Central Asia', at='tashkent')

event('hungarian-revolution-1848', 'The Hungarian Revolution of 1848', 'revolution', (1848, 1849),
      'Hungary rose for its freedom in 1848 and nearly won it, until the Russian tsar sent 200,000 soldiers to crush it.',
      figure(None, 'The Ides of March',
             'News of revolution in Paris and Vienna reached Pest in March 1848. On the 15th the young poet Sándor '
             'Petőfi read out his National Song to the crowds, with its call: Rise up, Hungarians! Students printed '
             "twelve demands without the censor's leave, and by evening the city was in the people's hands, without a "
             'shot fired.',
             img='Sándor Petőfi', kick='How it began', y=1848, at='budapest'),
      figure('lajos-kossuth', 'Kossuth',
             'In April the emperor accepted the April Laws, which gave Hungary its own government, ended serfdom and gave '
             'many more men the vote. The finance minister, Lajos Kossuth, a lawyer and a spellbinding speaker, became '
             'the voice of the revolution, and that autumn he toured the Great Plain raising volunteers for a new army, '
             'the Honvéd.',
             y=1848, at='budapest'),
      battle('Pákozd',
             'Vienna wanted its power back, and quietly encouraged Josip Jelačić, the ban of Croatia, whose people '
             'resented Hungarian rule, to invade. On 29 September 1848 the new Hungarian army stopped him at Pákozd, near '
             'Lake Velence, and he turned away toward Vienna. Hungary and the empire were now at war.',
             y=1848, at='pakozd'),
      figure('franz-joseph-i', 'A new emperor',
             'In December 1848 the 18-year-old Franz Joseph became emperor, and Prince Windischgrätz invaded Hungary with '
             "a large army. Pest fell in January 1849, and Kossuth's government fled east to Debrecen, behind the Tisza "
             'river. In the mountains to the north, General Artúr Görgei led his army on a daring winter '
             'march, and kept it alive.',
             y=1849, at='debrecen'),
      figure(None, 'The Spring Campaign',
             'In the spring of 1849 Görgei, a 31-year-old chemist turned general, struck back. His armies beat the '
             'Austrians at Isaszeg and in battle after battle, and by May they had driven them out of nearly all of '
             'Hungary and stormed Buda castle. In Transylvania the old Polish general Józef Bem won back the east.',
             img='Artúr Görgei', y=1849, at='isaszeg'),
      scene('Independence',
            'On 14 April 1849, in the great Protestant church of Debrecen, the parliament declared Hungary independent '
            'and dethroned the House of Habsburg. Kossuth became governor-president. Soon after, Franz Joseph asked the '
            'tsar of Russia for help.',
            y=1849, at='debrecen'),
      figure('nicholas-i-of-russia', "The tsar's army",
             'Tsar Nicholas I, who hated revolutions, sent about 200,000 soldiers over the Carpathians in June 1849, while '
             "a reinforced Austrian army attacked from the west. On 31 July Bem's army was routed at Segesvár, in "
             'Transylvania. Petőfi, who was with it, was last seen there, and his body was never found.',
             y=1849, at='segesvar'),
      turn('Világos',
           'Caught between two empires, Kossuth handed power to Görgei and fled to the Ottoman Empire. On 13 August 1849, '
           'at Világos, Görgei laid down his arms with some 30,000 men, not to the Austrians but to the Russians. Many '
           'Hungarians called him a traitor, though he had no hope left.',
           y=1849, at='vilagos'),
      cost('The martyrs of Arad',
           'Austria took its revenge. On 6 October 1849 thirteen Hungarian generals were hanged or shot at Arad, and the '
           'former prime minister, Batthyány, was shot in Pest. Hungarians say that because Austrian officers clinked '
           'their beer glasses to celebrate, they vowed not to clink beer for 150 years.',
           num='13', of='Hungarian generals put to death at Arad', y=1849, at='arad'),
      legacy('The revolution failed, but not for nothing. Serfdom never came back, and in 1867 Franz Joseph made a deal '
             'with Hungary, the Compromise, which turned his empire into Austria-Hungary, with Hungary ruling itself. '
             "Kossuth died in exile in Turin, and 15 March is Hungary's national day.",
             'Hungary won its own government in 1848',
             'Crushed by Austria and Russia in 1849',
             'Self-rule came back in 1867'),
      states=('Austria Hungary',), war='hungarian-revolution-1848', wiki='Hungarian Revolution of 1848', at='budapest')

event('reform-war', 'The Reform War', 'civil-war', (1857, 1861),
      "Mexico's liberals and conservatives fought a civil war over the power of the Church, and Benito Juárez won it.",
      scene('A constitution',
            "In 1855 Mexico's liberals came to power and began to strip the Catholic Church and the army of their old "
            'privileges: their own law courts and, for the Church, its vast lands. The new constitution of 1857 made all citizens equal '
            'before the law. The bishops threatened to excommunicate anyone who swore to uphold it, and conservatives '
            'got ready to fight.',
            kick='How it began', y=1857, at='mexico_city'),
      turn('The Plan of Tacubaya',
           'In December 1857 the moderate president, Ignacio Comonfort, joined a conservative coup, the Plan of '
           'Tacubaya, and shut down Congress. Within weeks he had lost control, and conservative generals took the '
           'capital. Benito Juárez, head of the Supreme Court and by law next in line, declared himself president and '
           'set up a liberal government outside the city.',
           y=1858, at='tacubaya'),
      figure('benito-juarez', 'The brave do not murder',
             'Juárez was a Zapotec from a poor village in Oaxaca, orphaned young, who had worked his way through school '
             'to become a lawyer. In Guadalajara in March 1858 mutinous soldiers seized him and raised their rifles to '
             'shoot him. The poet Guillermo Prieto stepped in front of him and cried out that the brave do not murder, '
             'and the soldiers lowered their guns.',
             y=1858, at='guadalajara'),
      scene('A government in a port',
            'Juárez escaped to the Pacific and sailed by way of Panama, Havana and New Orleans to Veracruz, which he '
            'reached in May 1858. Behind its walls, paid by the duties on its trade, his government held out for three '
            'years. In the centre of the country the conservatives, led by the brilliant young general Miguel Miramón, '
            'won battle after battle.',
            y=1858, at='veracruz'),
      figure(None, 'The Tiger of Tacubaya',
             'In April 1859 a liberal army attacked Mexico City and was beaten at Tacubaya by the conservative general '
             'Leonardo Márquez. He had the prisoners shot, and with them the doctors and medical students who had stayed '
             'to care for the wounded of both sides. Mexicans called him the Tiger of Tacubaya.',
             img='Leonardo Márquez', y=1859, at='tacubaya'),
      made('The Reform Laws',
           'From Veracruz in 1859 Juárez struck back with the Reform Laws. The state took over the property of the '
           'Church, made marriage a civil contract, kept the records of births and deaths, and ran the cemeteries.',
           'In 1860 came freedom of religion. Church and state in Mexico were separated, as they still are, and sales of '
           'Church land helped pay for the war.',
           y=1859, at='veracruz'),
      battle('Antón Lizardo',
             'In March 1860 Miramón besieged Veracruz again, with two small warships bought in Havana to blockade it from '
             'the sea. Juárez called them pirates, and a United States Navy squadron, friendly to the liberals, seized '
             'them off Antón Lizardo. Without them the siege failed, and the war began to turn.',
             y=1860, at='anton_lizardo'),
      battle('Calpulalpan',
             "Liberal armies from the north and west closed in. On 22 December 1860, at Calpulalpan, Jesús González "
             "Ortega crushed Miramón's last army. Miramón fled abroad, liberal troops marched into Mexico City, and in "
             'January 1861 Juárez came back to the capital he had left three years before.',
             y=1860, at='calpulalpan'),
      legacy('The war left Mexico ruined. In 1861 Juárez stopped paying its foreign debts for two years, and France, '
             'Spain and Britain sent troops to collect. Napoleon III used the chance to put an emperor on the throne of '
             "Mexico, and the liberals had to fight again until 1867. But the Reform's separation of Church and state "
             'lasts.',
             'Liberals against conservatives, 1857 to 1861',
             'The Reform Laws separated Church and state',
             'Its debts brought on the French invasion'),
      states=('Mexico',), war='reform-war', wiki='Reform War', at='veracruz')

event('french-conquest-vietnam', 'The French conquest of Vietnam', 'conquest', (1858, 1885),
      'In twenty-seven years of gunboats, treaties and war, France made Vietnam its colony.',
      scene('Missionaries and gunboats',
            "Vietnam's emperors, followers of Confucius, saw Christianity as a threat, and had European missionaries and "
            "Vietnamese Catholics put to death. Napoleon III's France wanted a foothold in Asia to rival Britain. In "
            'September 1858 a French and Spanish fleet sailed into the bay of Tourane, now Da Nang, and took its forts.',
            kick='How it began', y=1858, at='da_nang'),
      battle('Saigon',
             'Hemmed in at Tourane by Vietnamese troops and sickness, the French sailed south and in February 1859 took '
             'the citadel of Saigon, a rice port in the Mekong delta far from the capital, Hue. In 1861 they broke the '
             'Vietnamese siege lines at Ky Hoa and overran the country around.',
             y=1859, at='saigon'),
      figure(None, 'Tu Duc',
             'Emperor Tu Duc was a scholar and poet who ruled from the citadel of Hue. Faced with a rebellion in the north '
             'as well, he signed the Treaty of Saigon in 1862, giving France three southern provinces, paying a heavy '
             'indemnity and letting missionaries preach. He hoped to buy the lost land back. He never could.',
             img='Tự Đức', y=1862, at='hue'),
      scene('The mandarin who took poison',
            'France made Cambodia a protectorate in 1863, and in 1867 seized the three western provinces of the delta. '
            'Their governor, the old mandarin Phan Thanh Gian, who had gone to Paris to beg for the lost lands back, had '
            'no means to fight. He handed over the forts to spare his people a massacre, then took poison. All the south '
            'was now the French colony of Cochinchina.',
            y=1867, at='vinh_long'),
      figure(None, 'The Black Flags',
             'In the north, trade on the Red River drew French adventurers. In 1873 Francis Garnier, with a couple of hundred '
             'men, stormed the citadel of Hanoi. The court called on the Black Flags, Chinese irregulars under Liu '
             'Yongfu who had settled on the river, and they ambushed and killed Garnier outside Hanoi. France disowned '
             'him and pulled out.',
             img='Liu Yongfu', y=1873, at='hanoi'),
      turn('The protectorate',
           'In 1882 Commander Henri Rivière took Hanoi again, and in May 1883 he too was killed by the Black Flags, near '
           'the same spot. This time France sent a real army and fleet. In August 1883, with Tu Duc just dead, French '
           'warships shelled the forts guarding Hue, and the court signed a treaty that put Vietnam under French '
           'protection.',
           y=1883, at='hue'),
      battle('Fuzhou',
             'China, which saw Vietnam as its vassal, sent armies into the north alongside the Black Flags, and France '
             "and China went to war. On 23 August 1884 Admiral Courbet's squadron, which had lain at anchor for weeks "
             'beside the Chinese fleet in the river at Fuzhou, opened fire and sank it in under an hour.',
             y=1884, at='fuzhou'),
      figure('jules-ferry', 'Ferry the Tonkinese',
             'On land the war went less well. In March 1885, after a defeat at Bang Bo, a French force in retreat '
             'abandoned the town of Lang Son. When the news reached Paris it caused a panic, and the prime minister who '
             'had pushed for the war, Jules Ferry, mocked as "the Tonkinese", was thrown out of office. Yet in June China '
             'signed away its claims.',
             y=1885, at='lang_son'),
      scene('Aid the King',
            'In July 1885 the regent Ton That Thuyet attacked the French in Hue, failed, and fled into the mountains '
            "with the 13-year-old emperor Ham Nghi. In the boy's name he called on all Vietnamese to rise in the Can "
            'Vuong, Aid the King, movement. The French put another emperor on the throne and spent more than ten years '
            'crushing the revolt.',
            y=1885, at='hue'),
      legacy("In 1887 France joined Vietnam's three regions and Cambodia, and later Laos, into French Indochina. Ham "
             'Nghi, captured in 1888, spent the rest of his life in exile in Algeria, where he became a painter. '
             "Vietnamese resistance never quite died, and in 1954, at Dien Bien Phu, France's rule came to an end.",
             'France took Saigon in 1859',
             'All of Vietnam was French by 1885',
             'French rule ended at Dien Bien Phu in 1954'),
      war='french-conquest-vietnam', wiki='French conquest of Vietnam', at='hue')

event('conquest-of-the-desert', 'The Conquest of the Desert', 'conquest', (1878, 1885),
      "Argentina's army marched into the pampas and Patagonia, and broke the free Indigenous peoples of the south.",
      scene('The frontier',
            "In the 1870s Argentina's ranches ended at a frontier in the pampas. Beyond it lived free Mapuche, Ranquel "
            'and Tehuelche peoples, who traded with the settlers and also raided their ranches for cattle and captives. '
            'In 1876 the war minister, Adolfo Alsina, began to dig a great ditch with forts across the plains to hold '
            'the line.',
            kick='How it began', y=1876, at='carhue'),
      figure('julio-argentino-roca', 'To the Río Negro',
             'When Alsina died in 1877, the new war minister, General Julio Argentino Roca, said a ditch would never do. '
             "In 1879 some 6,000 soldiers marched south in five columns. Roca's own reached the Río Negro at Choele "
             "Choel on 25 May, Argentina's national day, and the river became the new frontier.",
             y=1879, at='choele_choel'),
      made('Rifles and wires',
           'The army carried Remington rifles, which fired far faster than the old muzzle loaders, and strung telegraph '
           'wires behind it as it went.',
           'Horsemen with lances and a few old guns could not stand against it, and wherever the columns went, the '
           'government in Buenos Aires knew within hours.',
           y=1879, at='choele_choel'),
      scene('Into the Andes',
            'From 1881 Colonel Conrado Villegas led columns up the rivers to Lake Nahuel Huapi and into the valleys of '
            'the Andes. At the same time Chile was conquering the Mapuche lands on its side of the mountains. Caught '
            'between two armies, the last free communities were hunted down one after another.',
            y=1881, at='nahuel_huapi'),
      cost('Captives',
           'Thousands were killed in the campaigns. Many of the captured were shipped to the prison island of Martín '
           'García or sent to work on sugar plantations, men were put into the army, and women and children were handed '
           'out as servants to families in Buenos Aires, often never to see their own again.',
           num='About 14,000', of='people captured and taken from their lands', y=1879, at='martin_garcia'),
      turn('The last chief',
           'Valentín Sayhueque, lord of the apple country around Nahuel Huapi, held out longest. Starving and hunted, '
           'he surrendered with his people at Junín de los Andes on 1 January 1885. The war was over, and the lands of '
           'the south were sold off in vast estates.',
           y=1885, at='junin_de_los_andes'),
      figure(None, 'Inacayal',
             'The Tehuelche chief Inacayal, captured in 1884, was later taken with his family to the new museum of '
             'natural history in La Plata, where scientists studied them. He died there in 1888. His skeleton and brain '
             'were kept in the museum for over a century, until in 1994 his remains were returned to his people in Patagonia.',
             img='Inacayal', y=1888, at='la_plata'),
      legacy('The campaign doubled the land Argentina really ruled and opened the south to sheep, cattle and European '
             'immigrants, and Roca was twice elected president. Today many Argentines see it as a conquest that took '
             'the land of Indigenous peoples and broke their families, and his statues have become a subject of '
             'argument.',
             'The army reached the Río Negro in 1879',
             'About 14,000 people were captured',
             'Patagonia was opened to ranching'),
      war='conquest-of-the-desert', wiki='Conquest of the Desert', at='choele_choel')

event('mexican-drug-war', "Mexico's drug war", 'war', (2006, 2025),
      'Mexico sent its army against the drug cartels in 2006, and the killing spread across the country.',
      figure('felipe-calderon', 'The army goes in',
             'Mexican gangs had long smuggled drugs into the United States, the biggest market in the world, and grew '
             'rich when cocaine routes moved through Mexico in the 1990s. Ten days after taking office in December 2006, '
             'President Felipe Calderón sent some 6,500 soldiers and federal police into his home state of Michoacán. '
             'Soon tens of thousands of troops were on the streets.',
             kick='How it began', y=2006, at='michoacan'),
      scene('Wars between cartels',
            'Arrests and killings of leaders split the cartels, and the pieces fought each other for the smuggling '
            'routes. The Sinaloa cartel of Joaquín Guzmán, known as El Chapo, fought the Juárez cartel for the border '
            'city of Ciudad Juárez, where more than 3,000 people were killed in 2010 alone, one of the highest murder '
            'rates in the world.',
            y=2010, at='ciudad_juarez'),
      scene('Los Zetas',
            'Los Zetas, a gang founded by deserters from the army\'s special forces, broke with the Gulf cartel in 2010 '
            'and spread terror across the northeast. In August 2010, near San Fernando in Tamaulipas, they murdered 72 '
            'migrants from Central and South America who were on their way to the United States.',
            y=2010, at='san_fernando_tamaulipas'),
      scene('Self-defence',
            'In 2013 farmers and business people in Michoacán, tired of paying protection money to a cult-like cartel '
            'called the Knights Templar, took up arms themselves. Their self-defence groups drove the cartel out of many '
            'towns. The government first welcomed them, then tried to bring them under control, and some were taken over '
            'by criminals in their turn.',
            y=2013, at='apatzingan'),
      cost('Ayotzinapa',
           'On the night of 26 September 2014, in Iguala, local police and gunmen attacked buses carrying students from '
           'the teachers\' college of Ayotzinapa. Forty-three students were taken away and never came home. '
           'Investigators found that police and officials had worked with a local gang, and the families still ask for '
           'the whole truth.',
           num='43', of='students who disappeared at Iguala', y=2014, at='iguala'),
      figure(None, 'El Chapo',
             'Guzmán had escaped from prison once, in 2001. Caught in 2014, he escaped again in 2015, through a tunnel '
             'about a mile long dug to the shower of his cell. Marines recaptured him at Los Mochis in 2016. '
             'Sent to the United States, he was tried in New York and sentenced to life in prison in 2019.',
             img='El Chapo', y=2016, at='los_mochis'),
      figure('andres-manuel-lopez-obrador', 'Hugs, not bullets',
             'President Andrés Manuel López Obrador, elected in 2018, promised "hugs, not bullets": to fight the poverty '
             'behind crime. He set up a new National Guard, made up largely of soldiers. In October 2019 soldiers caught Ovidio '
             "Guzmán, a son of El Chapo, in Culiacán, but let him go when cartel gunmen took over the city. He was caught "
             'again in 2023.',
             y=2019, at='culiacan'),
      cost('The missing',
           'Since 2006 several hundred thousand people have been murdered in Mexico, many but not all of them in the '
           'drug war, and tens of thousands more have vanished. Mothers search the countryside for hidden graves themselves, probing '
           'the ground with iron rods, because they fear no one else will find their children.',
           num='Over 100,000', of='people listed as missing in 2025', y=2025, at='mexico_city'),
      figure('claudia-sheinbaum', 'A new government',
             'In 2024 an old Sinaloa boss, Ismael Zambada, was flown to the United States, by force he said, and his '
             "followers and El Chapo's sons went to war. Claudia Sheinbaum, president from October 2024, promised "
             'policing led by intelligence. In 2025, pressed by the United States, Mexico sent dozens of jailed cartel '
             'figures to American courts, and her government said murders were falling.',
             y=2025, at='mexico_city'),
      legacy("Mexico's drug war has no clear end. Each boss caught has been replaced, and the cartels have moved into "
             'extortion, fuel theft and people smuggling. Mexicans still argue over whether soldiers on the streets made '
             'the country safer, and most guns traced from its crime scenes come from the United States.',
             'The army was sent in in December 2006',
             'Hundreds of thousands killed or missing',
             'Still unfinished at the end of 2025'),
      war='mexican-drug-war', wiki='Mexican drug war', at='culiacan')

event('twelve-day-war', 'The Twelve-Day War', 'war', (2025, 2025),
      "In June 2025 Israel and then the United States bombed Iran's nuclear sites, and for twelve days Iran fired back.",
      scene('A shadow war',
            'For years Israel and Iran had fought in the shadows, with killings, cyber attacks and armed allies. Iran '
            'was enriching uranium to 60 per cent, close to the level for a bomb, though it said its programme was '
            "peaceful. In 2024 the two struck each other openly, and on 12 June 2025 the UN's nuclear watchdog found Iran "
            'in breach of its duties.',
            kick='How it began', y=2025, at='natanz'),
      scene('Rising Lion',
            'Before dawn on 13 June Israeli jets, and drones that Israel said its agents had smuggled into Iran, struck '
            'air defences, missile launchers and the enrichment plant at Natanz. Strikes in Tehran killed the head of '
            'the armed forces, the commander of the Revolutionary Guards and several nuclear scientists. Israel said it '
            'was acting to stop Iran building a bomb. Iran denied seeking one.',
            y=2025, at='tehran'),
      scene('Missiles over Israel',
            'That night Iran began firing waves of ballistic missiles and drones at Israel. Over twelve days it launched '
            'hundreds of missiles and about a thousand drones. Most were shot down, but missiles struck homes in Tel '
            'Aviv, Bat Yam and other towns, the oil refinery at Haifa and a hospital in Beersheba, and Israelis spent '
            'their nights in shelters.',
            y=2025, at='tel_aviv'),
      scene('Strikes across Iran',
            "Israel's air force won control of the skies over western Iran and Tehran, and widened its attacks to "
            'missile bases, the nuclear site at Isfahan, fuel depots, military and police headquarters and the state '
            'broadcaster, hit during a live news programme. Many people fled Tehran.',
            y=2025, at='isfahan'),
      figure('donald-trump', 'Midnight Hammer',
             'On 22 June the United States joined in. B-2 bombers flew from Missouri and dropped fourteen huge '
             'bunker-busting bombs on the enrichment plant buried inside a mountain at Fordow and on Natanz, while a '
             'submarine fired missiles at Isfahan. President Trump said the sites had been obliterated. Later '
             'assessments of the damage differed.',
             y=2025, at='fordow'),
      turn('Ceasefire',
           'On 23 June Iran fired missiles at the American air base at Al Udeid in Qatar, after giving warning, and '
           'almost all were shot down without casualties. Hours later President Trump announced a ceasefire. After a '
           'last exchange of strikes, it took hold on 24 June. Both Israel and Iran claimed victory.',
           y=2025, at='al_udeid'),
      cost('The dead',
           'Iranian officials said about 1,000 people had been killed in Iran, among them commanders, scientists and '
           'many civilians. In Israel about 30 people were killed, almost all of them civilians. In both countries '
           'thousands were wounded or lost their homes.',
           num='About 1,000', of='killed in Iran, by its own count', y=2025, at='tehran'),
      legacy("How far Iran's nuclear programme had been set back stayed in dispute, and no one could be sure what had "
             'become of its enriched uranium. Iran cut back its work with UN inspectors, and in September 2025 United '
             'Nations sanctions on Iran were restored at the request of Britain, France and Germany.',
             'Twelve days of war, 13 to 24 June 2025',
             'The first American bombing of Iranian soil',
             'The damage to the nuclear programme is disputed'),
      war='twelve-day-war', wiki='Twelve-Day War', at='tehran')

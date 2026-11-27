from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('thirty-years-war', "The Thirty Years' War", 'war', (1618, 1648),
      'A quarrel over faith in Bohemia grew into a war of all Europe that left much of Germany in ruins.',
      scene('Out of the window',
            'In May 1618 Protestant nobles in Prague, angry that their new Catholic king, Ferdinand, was taking away their '
            'freedom of worship, threw two of his officials and a secretary out of a high castle window. All three '
            'survived: saved by angels, said Catholics; by a dung heap, said Protestants.',
            kick='How it began', img='Defenestrations of Prague', y=1618, at='prague'),
      battle('The White Mountain',
             'The Bohemians chose a Protestant king, Frederick of the Palatinate. In 1620 the Catholic armies crushed them at '
             'the White Mountain outside Prague. Frederick fled after a single winter on the throne, and was mocked ever '
             'after as the Winter King.',
             y=1620, at='white_mountain'),
      figure('albrecht-von-wallenstein', 'The warlord',
             'Albrecht von Wallenstein, a Bohemian noble grown rich on land taken from rebels, raised a vast private army for '
             'the emperor, paid for by plundering the lands it marched through. His rule was that war must feed itself.',
             y=1625),
      cost('Magdeburg',
           'In May 1631 imperial troops stormed the Protestant city of Magdeburg. Fire swept through it, and some 20,000 of '
           'its people were killed or burned. Germans made a new word for utter destruction: to magdeburgise.',
           num='20,000', of="of Magdeburg's 25,000 people died", y=1631, at='magdeburg'),
      figure('gustavus-adolphus', 'The Lion of the North',
             'King Gustavus Adolphus of Sweden landed in Germany in 1630 to save the Protestants and win land on the Baltic. '
             'His fast, drilled army with light cannon beat the imperial armies again and again, until he was killed in '
             'the fog at Lützen in 1632.',
             y=1632, at='lutzen'),
      figure('cardinal-richelieu', 'A cardinal for the Protestants',
             'Catholic France, led by Cardinal Richelieu, paid the Protestant Swedes, and in 1635 joined the war itself '
             'against the Catholic Habsburgs. By now it was less a war of faith than a fight for power in Europe.',
             y=1635),
      scene('Hunger, plague and wolves',
            'Armies on every side lived off the land, looting, torturing peasants to find hidden money and spreading '
            'plague. Germany lost perhaps a fifth of its people, some regions more than half, and wolves came back to the '
            'empty villages.',
            y=1638),
      turn('The Peace of Westphalia',
           'Peace was made in 1648 at Münster and Osnabrück, in Westphalia, after years of talks between more than 100 '
           'delegations. Each ruler kept the right to choose his land\'s religion, the Dutch Republic and Switzerland were '
           'recognised as independent, and France and Sweden gained land.',
           img='Peace of Westphalia', y=1648, at='munster'),
      legacy('The war was one of the most destructive in Europe\'s history. Its peace is often seen as the start of the '
             'modern system of independent states that do not meddle in each other\'s religion, and it left the Holy Roman '
             'Empire weak and divided for 150 years.',
             'Began with a fall from a window in Prague, 1618',
             'Germany lost perhaps a fifth of its people',
             'Ended by the Peace of Westphalia, 1648'),
      war='thirty-years-war', wiki="Thirty Years' War", img='Defenestrations of Prague')

event('fall-of-the-ming', 'The fall of the Ming', 'fall', (1618, 1683),
      'Rebels took Beijing, the last Ming emperor hanged himself, and the Manchus rode in to found the Qing.',
      scene('A dynasty in trouble',
            'By the 1620s the Ming, rulers of China since 1368, were in deep trouble. A cold spell, the Little Ice Age, '
            'brought drought and famine, silver from the Americas dried up, and court eunuchs fought officials for power. '
            'In the northeast the Manchus, under Nurhaci, went to war in 1618.',
            kick='How it began', y=1618),
      figure('li-zicheng', 'The Dashing King',
             'Li Zicheng, a postal worker who lost his job when the government cut costs, led an army of starving peasants '
             'across the north, promising land and no taxes. In April 1644 his men entered Beijing.',
             y=1644, at='beijing'),
      figure('chongzhen-emperor', 'The emperor on Coal Hill',
             'As the rebels broke in, the Chongzhen emperor rang the palace bell to call his ministers. None came. He killed '
             'several of his family, then climbed the hill behind the Forbidden City and hanged himself from a tree. He was '
             '33.',
             y=1644, at='beijing'),
      turn('The gate opens',
           'The Ming general Wu Sangui held Shanhai Pass, where the Great Wall meets the sea. Caught between the rebels and '
           'the Manchus, he opened the gate to the Manchus and joined them. Together they routed Li Zicheng, and a boy '
           'emperor of the new Qing dynasty took the throne in Beijing.',
           y=1644, at='shanhai_pass'),
      cost('Hair or head',
           'The Qing ordered every man to shave his forehead and wear a long braid, the queue, as Manchus did: keep your '
           'hair and lose your head. Towns that resisted were destroyed. At Yangzhou in 1645 the killing went on for days, '
           'and millions died in the long wars of conquest.',
           num='Ten days', of='of massacre at Yangzhou, 1645', y=1645, at='yangzhou'),
      figure('koxinga', 'Koxinga',
             'Ming loyalists fought on in the south. The pirate admiral Koxinga, son of a Chinese merchant and a Japanese '
             'mother, drove the Dutch out of Taiwan in 1662 and made it a Ming stronghold. His grandson gave it up to the '
             'Qing in 1683.',
             y=1662, at='tainan'),
      figure('kangxi-emperor', 'The Kangxi emperor',
             'Under the Kangxi emperor, who ruled for 61 years from 1661, the Qing crushed the last revolts and made China '
             'bigger and richer than ever. The Manchus would rule China until 1912, as its last imperial dynasty.',
             y=1683, at='beijing'),
      legacy('The fall of the Ming brought China\'s last dynasty to power. The Qing ruled for nearly 270 years and doubled '
             'the size of China, adding Taiwan, Mongolia, Tibet and Xinjiang. The queue became a symbol of China until men '
             'cut it off in 1911.',
             'Rebels took Beijing in 1644',
             'The Manchus founded the Qing',
             "China's last dynasty, until 1912"),
      states=['Ming Chinese Empire', 'Post-Ming Warlords', 'Manchu Empire'], wiki='Transition from Ming to Qing',
      at='beijing')

event('english-civil-war', 'The English Civil War', 'civil-war', (1642, 1651),
      'King and Parliament went to war. The king lost his head, and England tried living without a monarch.',
      figure('charles-i-of-england', 'A king by divine right',
             'Charles I believed kings were chosen by God and answered to no one else. He ruled for eleven years without '
             'Parliament, raised taxes it had not agreed, and angered Puritans with his church reforms. When Scotland rose '
             'in 1639 he had to call Parliament back, and it wanted power.',
             kick='How it began', y=1640, at='london'),
      turn('The five members',
           'In January 1642 Charles marched into the House of Commons with soldiers to arrest five of his fiercest critics. '
           'They had slipped away, and the Speaker would not say where. Charles left London, and in August raised his '
           'royal standard at Nottingham.',
           y=1642, at='london'),
      scene('Cavaliers and Roundheads',
            "The king's men, many of them gentry with long hair, were called Cavaliers. Parliament's, many of them Puritans "
            'with short-cropped hair, were Roundheads. Families were split, and towns changed hands again and again.',
            y=1643),
      figure('oliver-cromwell', 'The New Model Army',
             'Oliver Cromwell, a Puritan squire with no training as a soldier, built a disciplined cavalry, the Ironsides, '
             "and helped create Parliament's New Model Army. At Naseby in 1645 it destroyed the king's main army.",
             y=1645, at='naseby'),
      cost('The dead',
           'Fighting, and the disease that came with the armies, killed perhaps 200,000 people in England and Wales, a '
           'larger share of the people than the First World War. In Ireland the toll was far worse.',
           num='200,000', of='dead in England and Wales', y=1646),
      turn("The king's head",
           'Charles was tried for treason against his own people in January 1649 and refused to recognise the court. On 30 '
           'January he was beheaded outside the Banqueting House in Whitehall. He wore two shirts so that he would not '
           'shiver in the cold and seem afraid.',
           img='Execution of Charles I', y=1649, at='london'),
      scene('No king',
            'England became a republic, the Commonwealth. Cromwell crushed Ireland, with massacres at Drogheda and Wexford '
            'in 1649, and in 1653 made himself Lord Protector. Theatres were shut and Christmas celebrations banned.',
            y=1653),
      tale('The Royal Oak',
           'Beaten at Worcester in 1651, the young Charles II hid in an oak tree while soldiers searched the woods below, '
           'then escaped to France in disguise. Hundreds of English pubs are still called the Royal Oak.',
           y=1651, at='worcester'),
      turn('The king comes back',
           "Cromwell died in 1658, and without him the republic fell apart. In 1660 Parliament invited Charles II home. "
           "Cromwell's body was dug up, hanged and beheaded, and his head stood on a pole outside Westminster Hall for "
           'years.',
           y=1660, at='london'),
      legacy('The monarchy came back, but kings could never again rule without Parliament. The ideas argued in the war, '
             'about rights, government by consent and even votes for all men, travelled to America and beyond.',
             'King against Parliament, 1642 to 1651',
             'Charles I beheaded in 1649',
             'Parliament came out on top'),
      war='english-civil-war', wiki='English Civil War', img='Battle of Naseby')

event('taj-mahal', 'Building the Taj Mahal', 'building', (1632, 1653),
      'A grieving emperor built a tomb of white marble for his wife, and the world still comes to see it.',
      figure('shah-jahan', 'A promise to a dying wife',
             'In 1631 Mumtaz Mahal, wife of the Mughal emperor Shah Jahan, died giving birth to their fourteenth child while '
             'travelling with him on campaign. Legend says she asked him, as she lay dying, to build her a tomb the world '
             'had never seen.',
             kick='How it began', y=1631, at='burhanpur'),
      scene('By the river',
            'Shah Jahan chose a garden by the Yamuna river at Agra. Work began in 1632 under the architect Ustad Ahmad '
            'Lahori, and some 20,000 workers came from across the empire and beyond: stonecutters, inlayers, calligraphers '
            'and masons.',
            y=1632, at='agra'),
      made('Elephants and marble',
           'White marble came from Makrana, some 400 km away, hauled by more than a thousand elephants and teams of oxen.',
           'The tomb with its great dome and four minarets took about 12 years. The gardens, mosque and gates were finished '
           'around 1653.',
           y=1643, at='agra'),
      work('Flowers of stone',
           'The marble is inlaid with flowers made of as many as 28 kinds of precious and semi-precious stones, and with '
           'verses of the Quran in black marble letters that grow larger toward the top, so that from below they all look '
           'the same size.',
           img='Pietra dura', y=1648, at='agra'),
      scene('Tricks of the eye',
            'The four minarets lean very slightly outwards, so that in an earthquake they would fall away from the tomb. '
            'Everything is laid out in perfect symmetry, except Shah Jahan\'s own coffin, squeezed in later beside his '
            "wife's.",
            y=1653, at='agra'),
      figure('aurangzeb', 'A prisoner with a view',
             "In 1658 Shah Jahan's son Aurangzeb seized the throne and locked his father in the fort at Agra. For his last "
             'eight years, the story goes, the old emperor gazed across the river at his wife\'s tomb.',
             y=1658, at='agra'),
      tale('The black Taj',
           'A legend says Shah Jahan meant to build a second tomb for himself across the river, in black marble, joined to '
           'the first by a bridge. Historians find no sign of it. But the garden on the far bank was laid out for viewing '
           'the Taj by moonlight.',
           kick='A legend', y=1660, at='agra'),
      legacy('The Taj Mahal is often called the most beautiful building in the world, a symbol of India and of love. Millions '
             'visit it every year, and India works hard to keep its marble white against the pollution of a modern city.',
             'Built for Mumtaz Mahal from 1632',
             'Some 20,000 workers and a thousand elephants',
             'A symbol of India today'),
      states=['Mughal Empire'], wiki='Taj Mahal', at='agra')

event('siege-of-vienna-1683', 'The siege of Vienna, 1683', 'siege', (1683, 1699),
      'An Ottoman army besieged Vienna. A great cavalry charge broke it, and the Ottoman tide began to turn.',
      figure('kara-mustafa-pasha', "The grand vizier's gamble",
             'In 1683 the Ottoman grand vizier, Kara Mustafa, led a vast army into Austria and in July surrounded Vienna, '
             'capital of the Habsburg emperor Leopold I, who fled. About 15,000 soldiers and armed citizens held the walls.',
             kick='How it began', y=1683, at='vienna'),
      scene('Mines under the walls',
            'The Ottomans dug trenches and tunnels toward the walls and blew holes in them with mines. Inside, disease and '
            'hunger spread, and the defenders dug tunnels of their own to find the miners. By September the city was close '
            'to falling.',
            y=1683, at='vienna'),
      figure('john-iii-sobieski', 'The king of Poland',
             'A relief army of Germans, Austrians and Poles gathered on the Kahlenberg, the hill above the city, led by the '
             'king of Poland, John III Sobieski. On 12 September 1683 it attacked.',
             y=1683, at='vienna'),
      battle('The winged hussars',
             'Late in the afternoon Sobieski led some 18,000 horsemen, among them Polish hussars with tall feathered wings on '
             'their backs, down the hill in perhaps the largest cavalry charge in history. The Ottoman army broke and fled, '
             'leaving its camp and its treasure.',
             img='Battle of Vienna', y=1683, at='vienna'),
      tale('Coffee and croissants',
           "Vienna's first coffee houses, the story goes, were opened with sacks of coffee left behind in the Ottoman camp, "
           "and its bakers made a crescent-shaped roll to mock the enemy's flag, the ancestor of the croissant. Both are "
           'legends.',
           kick='A legend', y=1683, at='vienna'),
      turn('The silk cord',
           'Sultan Mehmed IV did not forgive the defeat. That December, in Belgrade, Kara Mustafa was strangled with a silk '
           'cord, as was the custom for disgraced Ottoman officials.',
           y=1683),
      turn('Karlowitz',
           'The Habsburgs, Poland, Venice and Russia joined in a Holy League and drove the Ottomans back for 16 years. In '
           '1697 Prince Eugene of Savoy crushed them at Zenta, and at Karlowitz in 1699 they gave up Hungary, the first '
           'great land they lost for good.',
           y=1699, at='karlowitz'),
      legacy('Vienna marked the high point of Ottoman power in Europe. After 1683 the empire slowly gave ground, while the '
             'Habsburgs became the great power of the Danube. The battle is still remembered in Austria and in Poland.',
             'Vienna besieged in 1683',
             'Saved by a charge of 18,000 horsemen',
             'The Ottoman tide turned for good'),
      states=['Austrian Empire', 'Holy Roman Empire', 'Ottoman Empire', 'Polish–Lithuanian Commonwealth'],
      war='great-turkish-war', wiki='Battle of Vienna', img='Battle of Vienna')

event('great-northern-war', 'The Great Northern War', 'war', (1700, 1721),
      'Peter the Great fought Sweden for 21 years, built a new capital on the Baltic and made Russia a European power.',
      scene('Three against one',
            'In 1700 Sweden ruled an empire around the Baltic Sea, and its new king, Charles XII, was 17. Russia, Denmark and '
            'Saxony-Poland thought it was the moment to attack. They were wrong.',
            kick='How it began', y=1700),
      figure('charles-xii-of-sweden', 'Narva',
             'Charles knocked Denmark out of the war in weeks, then sailed to Narva, where some 10,000 Swedes attacked a '
             'Russian army three times their size in a snowstorm and routed it. Then he spent six years chasing Augustus of '
             'Saxony across Poland.',
             y=1700, at='narva'),
      figure('peter-the-great', 'A city in a swamp',
             'Peter the Great learned from defeat. He rebuilt his army on European lines, melted church bells for cannon, '
             'and in 1703 founded a city in the marshes at the mouth of the Neva, on land taken from Sweden: St Petersburg. '
             'Tens of thousands of forced labourers died building it.',
             y=1703, at='st_petersburg'),
      battle('Poltava',
             'In 1708 Charles marched on Moscow, but the Russians burned the land ahead of him, and the terrible winter that '
             'followed froze his army. At Poltava, in Ukraine, in June 1709, Peter destroyed it. Charles, wounded in the '
             'foot, was carried about on a stretcher.',
             img='Battle of Poltava', y=1709, at='poltava'),
      tale('The king at Bender',
           'Charles fled to the Ottoman Empire and stayed five years at Bender, urging the sultan to fight Russia. When the '
           'Ottomans finally tried to make him leave in 1713, he fought off hundreds of janissaries with a handful of men '
           'before he was captured.',
           y=1713, at='bender'),
      turn('The Peace of Nystad',
           'Charles was shot dead in a trench in Norway in 1718. In 1721 Sweden made peace at Nystad and gave Russia '
           'Livonia, Estonia and the land around St Petersburg. Peter took a new title: Emperor of All Russia.',
           y=1721, at='nystad'),
      legacy('The war ended Sweden\'s days as a great power and made Russia one, with St Petersburg as its window on '
             'Europe and its capital for two centuries.',
             'Sweden against Russia and its allies, 1700 to 1721',
             'Peter won at Poltava in 1709',
             'Russia became a great European power'),
      war='great-northern-war', wiki='Great Northern War', img='Battle of Poltava')

event('lisbon-earthquake', 'The Lisbon earthquake', 'disaster', (1755, 1755),
      "On All Saints' Day an earthquake, a tsunami and fire destroyed Lisbon and shook Europe's faith in a kind God.",
      scene("All Saints' Day",
            'Lisbon was one of the richest cities in Europe, capital of an empire that reached Brazil, Africa and India. On '
            "the morning of 1 November 1755, All Saints' Day, its churches were full for Mass, with candles burning on "
            'every altar.',
            kick='Before', y=1755, at='lisbon'),
      turn('The earthquake',
           'At about 9.40 the ground shook for several minutes, in one of the strongest earthquakes ever known in Europe. '
           'Churches, palaces and houses fell on the people inside, and great cracks opened in the streets.',
           y=1755, at='lisbon'),
      cost('Wave and fire',
           'Survivors fled to the open waterfront and saw the sea drain away, showing wrecks on the harbour floor. Then a '
           'tsunami swept in. Fires started by the candles burned for five days.',
           num='30,000 to 50,000', of='dead in Lisbon alone', img='1755 Lisbon earthquake', y=1755, at='lisbon'),
      figure('marquis-of-pombal', 'Bury the dead, heal the living',
             'When the king asked what to do, his minister, later the Marquis of Pombal, is said to have answered: bury the '
             'dead and heal the living. He had the ruins cleared, food prices fixed and looters hanged, and rebuilt the '
             'centre with wide, straight streets.',
             y=1756, at='lisbon'),
      made('Buildings that bend',
           "Pombal's engineers gave the new buildings a flexible wooden cage inside the walls, and tested it by marching "
           'soldiers around a model to shake it.',
           'It was one of the first earthquake-proof designs in the world, and the Baixa district built that way still '
           'stands.',
           img='Pombaline style', y=1758, at='lisbon'),
      scene('Questions for every parish',
            'Pombal sent every parish a list of questions: how long did the shaking last, did the sea rise, how many '
            'buildings fell? The answers are still studied, and he is sometimes called the father of the science of '
            'earthquakes.',
            y=1756),
      figure('voltaire', 'The best of all possible worlds?',
             'The disaster shook thinkers across Europe. If God was good, why would he kill thousands of people at prayer on '
             'a holy day? Voltaire wrote a poem about it, and later Candide, which mocks the idea that all is for the best '
             'in this best of all possible worlds.',
             y=1759),
      legacy('The Lisbon earthquake was one of the deadliest in history. It led to the first rebuilding with earthquake-proof '
             'design and the first scientific study of an earthquake, and pushed European thinkers to look for natural, not '
             'divine, causes of disaster.',
             'Struck on 1 November 1755',
             'Earthquake, tsunami and fire',
             'Began the science of earthquakes'),
      states=['Portugal'], wiki='1755 Lisbon earthquake', at='lisbon')

event('seven-years-war', "The Seven Years' War", 'world-war', (1754, 1763),
      'Britain and France fought on four continents, and Britain came out with the greatest empire on Earth.',
      figure('george-washington', 'A shot in the woods',
             'In 1754 a young Virginia militia officer, George Washington, ambushed a French scouting party in the woods of '
             'Pennsylvania. Britain and France both claimed the Ohio valley, and the shots in that glen helped set off a war '
             'around the world.',
             kick='How it began', y=1754, at='jumonville_glen'),
      scene('Partners change',
            'In Europe, old enemies swapped partners: Austria joined France against Prussia, and Britain backed Prussia. In '
            '1756 Frederick the Great of Prussia struck first and invaded Saxony.',
            y=1756),
      figure('frederick-the-great', 'Prussia against all',
             'Frederick fought Austria, France, Russia and Sweden at once. He won brilliant victories at Rossbach and Leuthen '
             'in 1757, but by 1761 he was close to defeat, his army shrinking and Berlin raided twice.',
             y=1757),
      battle('Plassey',
             "In India, the East India Company's Robert Clive, with about 3,000 men, beat the Nawab of Bengal's army of "
             "50,000 at Plassey in 1757, mostly by bribing the Nawab's commander to stand aside. The Company was on its way "
             'to ruling Bengal.',
             y=1757, at='plassey'),
      battle('Quebec',
             "In 1759, Britain's year of victories, General James Wolfe's men climbed a cliff by night to the Plains of "
             'Abraham outside Quebec. Wolfe and the French commander, Montcalm, were both killed in the battle that followed, '
             'and New France was lost.',
             img='The Death of General Wolfe', y=1759, at='quebec'),
      turn('The miracle',
           "In January 1762 Frederick's deadliest enemy, Empress Elizabeth of Russia, died. Her successor, Peter III, adored "
           'Frederick and made peace at once. Frederick called it the miracle of the House of Brandenburg.',
           y=1762),
      cost('The dead',
           'Soldiers died in battle, and far more of disease, while armies stripped the land. Prussia alone may have lost a '
           'tenth of its people.',
           num='About a million', of='dead around the world', y=1762),
      turn('The Peace of Paris',
           'In 1763 France gave Canada and the lands east of the Mississippi to Britain, and Spain gave up Florida, while '
           'France kept its sugar islands. Prussia kept Silesia. Britain was now the leading power in the world, but deep '
           'in debt.',
           y=1763, at='paris'),
      legacy('Winston Churchill called it the first world war. It made Britain master of North America and India and '
             'Prussia a great power. But the taxes Britain then put on its American colonies to pay for it led straight to '
             'the American Revolution.',
             'Fought on four continents, 1754 to 1763',
             'Britain won Canada and Bengal',
             'Its debts led to the American Revolution'),
      war='seven-years-war', wiki="Seven Years' War", img='The Death of General Wolfe')

event('american-revolution', 'The American Revolution', 'revolution', (1775, 1783),
      'Thirteen colonies rose against Britain, declared that all men are created equal, and won their independence.',
      scene('No taxation without representation',
            "After the Seven Years' War, Britain taxed its American colonies to help pay its debts. The colonists, who had "
            'no members in Parliament, protested. In 1773 men dressed as Mohawks threw 342 chests of tea into Boston '
            'harbour. Britain closed the port and sent troops.',
            kick='How it began', img='Boston Tea Party', y=1773, at='boston'),
      battle('Lexington and Concord',
             "On 19 April 1775 British soldiers marched out of Boston to seize the colonists' weapons at Concord. Militiamen, "
             'warned in the night by riders such as Paul Revere, met them at Lexington. Shots were fired, and the war had '
             'begun.',
             img='Battles of Lexington and Concord', y=1775, at='lexington'),
      figure('thomas-jefferson', 'All men are created equal',
             'On 4 July 1776 the Continental Congress in Philadelphia adopted a Declaration of Independence, written mostly '
             'by Thomas Jefferson. It said that all men are created equal, with rights to life, liberty and the pursuit of '
             'happiness, though Jefferson, like many who signed it, owned slaves.',
             y=1776, at='philadelphia'),
      figure('george-washington', 'Across the Delaware',
             'General George Washington lost New York and retreated across New Jersey. On Christmas night 1776 he led his '
             'freezing army across the icy Delaware River and surprised the Hessian soldiers at Trenton. It kept the '
             'revolution alive.',
             y=1776, at='trenton'),
      turn('Saratoga',
           'In 1777 a British army marching south from Canada was surrounded and forced to surrender at Saratoga. The '
           'victory persuaded France to join the war on the American side in 1778, and Spain and the Dutch followed.',
           y=1777, at='saratoga'),
      scene('Valley Forge',
            "Washington's army spent the winter of 1777 at Valley Forge, short of food, clothes and shoes, and some 2,000 "
            'men died of disease. A Prussian officer, Baron von Steuben, drilled the survivors into a real army.',
            y=1778, at='valley_forge'),
      battle('Yorktown',
             'In 1781 the British general Cornwallis dug in at Yorktown, in Virginia, waiting for the navy. A French fleet '
             'blocked the bay, and the American and French armies trapped him. On 19 October he surrendered about 8,000 '
             'men. The story goes that his band played The World Turned Upside Down.',
             img='Siege of Yorktown', y=1781, at='yorktown'),
      turn('Independence',
           'In the Treaty of Paris of 1783 Britain recognised the United States, with land as far west as the Mississippi. '
           'In 1789 Washington became the first president under a new Constitution.',
           y=1783, at='paris'),
      legacy('The revolution made the first large modern republic and spread the ideas that government rests on the consent '
             'of the governed and that people have rights no ruler can take away. Those ideas fed the French Revolution, and '
             'in time the struggles against slavery and for equal rights in America itself.',
             'Began at Lexington in 1775',
             'Independence declared on 4 July 1776',
             'Won at Yorktown in 1781'),
      states=['British American colonies', 'United States of America', 'United Kingdom'],
      war='american-revolutionary-war', wiki='American Revolution', img='Washington Crossing the Delaware')

event('industrial-revolution', 'The Industrial Revolution', 'change', (1760, 1840),
      'In Britain, machines driven by water, coal and steam began to make things faster than any hands could.',
      scene('Cotton',
            'In the 1700s Britain had coal, iron, fast rivers, an empire to trade with and banks ready to lend. Cotton cloth '
            "was in demand, and inventors raced to make it faster. James Hargreaves's spinning jenny of 1764 let one worker "
            'spin eight threads at once.',
            kick='How it began', img='Spinning jenny', y=1764),
      made('The factory',
           'In 1771 Richard Arkwright built a mill at Cromford, run by a water wheel, where hundreds of workers tended '
           'spinning machines in shifts, day and night.',
           'It was the model of the factory: workers came to the machines, kept set hours and were paid wages, and whole '
           'towns grew up around the mills.',
           img='Cromford Mill', y=1771, at='cromford'),
      figure('james-watt', 'Steam',
             'Steam engines already pumped water out of mines, but they wasted most of their fuel. In 1765 James Watt, an '
             'instrument maker in Glasgow, thought of a separate condenser, and the engines he built from 1776 with Matthew '
             'Boulton could drive machines anywhere.',
             y=1776, at='birmingham'),
      work('The Iron Bridge',
           'In 1779 the world\'s first great bridge of cast iron was raised over the Severn at Coalbrookdale, where Abraham '
           'Darby had learned to smelt iron with coke instead of charcoal. It still stands.',
           img='The Iron Bridge', y=1779, at='coalbrookdale'),
      scene('Children in the mills',
            'Mills and mines used children, some only five or six years old, for twelve hours a day or more, because they '
            'were cheap and small enough to crawl under machines. Towns such as Manchester grew so fast that families '
            'crowded into damp cellars, and cholera spread.',
            y=1830, at='manchester'),
      tale('The Luddites',
           'From 1811 weavers in the north of England, whose skills machines had made worthless, broke into factories at '
           'night to smash the new machines, signing their letters from an imaginary General Ludd. Soldiers were sent, and '
           'some were hanged. People who distrust new technology are still called Luddites.',
           y=1812),
      figure('george-stephenson', 'The Rocket',
             'In 1829 the Rocket, built by George Stephenson and his son Robert, won a contest to pull trains on the new '
             'railway between Liverpool and Manchester, at 48 km an hour. When the line opened in 1830, the railway age '
             'began.',
             y=1829, at='liverpool'),
      legacy('The Industrial Revolution was the biggest change in how people live since farming began. It spread from Britain '
             'across the world, bringing more wealth and more people than ever before, and factories, cities, railways and '
             'the burning of coal that began to warm the climate.',
             'Began in Britain around 1760',
             'Machines, factories and steam',
             'Changed how people live and work'),
      states=['United Kingdom', 'United Kingdom of Great Britain and Ireland'], wiki='Industrial Revolution',
      img='The Iron Bridge', at='manchester')

event('first-fleet', 'The First Fleet', 'founding', (1788, 1802),
      'Eleven ships brought convicts to found a British colony in Australia, on land its peoples had lived on for 50,000 years.',
      scene('Somewhere to send convicts',
            "Britain's prisons were overflowing, and since American independence it could no longer ship convicts to "
            'America. In 1786 the government chose Botany Bay, on the east coast of Australia, which James Cook had charted '
            'in 1770.',
            kick='How it began', y=1786, at='botany_bay'),
      scene('Eleven ships',
            'In May 1787 eleven ships left Portsmouth under Captain Arthur Phillip with some 1,400 people, about 750 of '
            'them convicts. The youngest convict was a boy of nine, the oldest a woman of about 80. The voyage took eight '
            'months.',
            y=1787),
      turn('Sydney Cove',
           'Botany Bay proved to be poor land, so on 26 January 1788 Phillip landed at a deeper harbour to the north, Sydney '
           'Cove, raised the British flag and claimed the land for King George III.',
           y=1788, at='sydney'),
      scene('The Eora',
            'The land was the country of the Eora and other Aboriginal peoples, whose ancestors had lived in Australia for '
            'more than 50,000 years. The British took it as if it belonged to no one, and the Eora resisted the loss of '
            'their land and food.',
            y=1788, at='sydney'),
      cost('Smallpox',
           'In 1789 smallpox broke out among the Aboriginal people around Sydney, who had no resistance to it. Officers '
           'found bodies in caves and on the beaches.',
           num='Half', of='of the Eora died of it, perhaps', y=1789, at='sydney'),
      figure(None, 'Bennelong',
             'Phillip had an Eora man, Bennelong, captured so the British could learn the language and ways of his people. '
             'Bennelong escaped, came back on his own terms and became a go-between. In 1792 he sailed to England with '
             'Phillip.',
             img='Bennelong', y=1792, at='sydney'),
      figure(None, 'Pemulwuy',
             'Others fought. Pemulwuy, a Bidjigal man, led attacks on the settlers for twelve years and was said to be proof '
             'against bullets after surviving many wounds. He was shot dead in 1802, and his head was sent to England.',
             img='Pemulwuy', y=1802),
      legacy('The colony grew into modern Australia. 26 January is celebrated as Australia Day, but many Aboriginal '
             'Australians mark it as Invasion Day, a day of mourning. The country is still working out how to honour the '
             'oldest living cultures on Earth.',
             'Eleven ships reached Sydney Cove in 1788',
             'About 750 convicts were the first settlers',
             'Australia Day, or Invasion Day'),
      states=['Eora', 'New South Wales', 'Australian aboriginal hunter-gatherers'], wiki='First Fleet', at='sydney')

event('french-revolution', 'The French Revolution', 'revolution', (1789, 1799),
      'The people of France overthrew their king and their nobles in the name of liberty, equality and fraternity.',
      figure('louis-xvi', 'A bankrupt kingdom',
             'By 1789 France was bankrupt, partly from helping the Americans win their revolution, and after a bad harvest '
             'bread cost more than it had for decades. King Louis XVI called the Estates-General, an assembly of clergy, '
             'nobles and commoners, for the first time since 1614.',
             kick='How it began', y=1789, at='versailles'),
      turn('The Tennis Court Oath',
           'The commoners, the Third Estate, declared themselves a National Assembly. Locked out of their hall, on 20 June '
           '1789 they met in a royal tennis court and swore not to part until France had a constitution.',
           img='Tennis Court Oath', y=1789, at='versailles'),
      turn('The Bastille',
           "On 14 July 1789, fearing the king's troops would crush them, a Paris crowd stormed the Bastille, a fortress "
           "prison, for its gunpowder. It held only seven prisoners. The governor's head was carried through the streets "
           'on a pike.',
           img='Storming of the Bastille', y=1789, at='paris'),
      made('The Rights of Man',
           'In August 1789 the Assembly swept away the privileges of the nobles and the Church and issued the Declaration of '
           'the Rights of Man and of the Citizen.',
           'Men are born and remain free and equal in rights, it said. Olympe de Gouges answered with a Declaration of the '
           'Rights of Woman.',
           img='Declaration of the Rights of Man and of the Citizen', y=1789, at='paris'),
      scene('The flight to Varennes',
            'In June 1791 the royal family fled Paris in disguise, but the king was recognised, from his face on the money, '
            'it is said, and stopped at Varennes. He never won back the people\'s trust. In 1792, at war with Austria and '
            'Prussia, France became a republic.',
            y=1791, at='varennes'),
      turn("The king's head",
           'Louis XVI, now plain Citizen Louis Capet, was tried and guillotined on 21 January 1793. Marie Antoinette '
           "followed in October. There is no proof that she ever said 'let them eat cake'.",
           img='Execution of Louis XVI', y=1793, at='paris'),
      cost('The Terror',
           'Facing war and revolt, the Committee of Public Safety, led by Maximilien Robespierre, ruled by fear. Thousands '
           'more died in prison or were killed without trial, until Robespierre himself went to the guillotine in July '
           '1794.',
           num='17,000', of='officially executed in the Terror', y=1794, at='paris'),
      figure('napoleon', 'Enter Napoleon',
             "The revolution's wars made a young Corsican general famous. In November 1799 Napoleon Bonaparte seized power in "
             'a coup and declared the revolution over. Five years later he crowned himself emperor.',
             y=1799, at='paris'),
      legacy('The revolution ended the old order of king, nobles and Church in France and spread its ideas across Europe: '
             'citizens equal before the law, rights for all, the nation above the king. Its motto, liberty, equality, '
             'fraternity, and its tricolour flag are still those of France.',
             'Began with the Bastille, 14 July 1789',
             'The king guillotined in 1793',
             'Liberty, equality, fraternity'),
      states=['France'], wiki='French Revolution', img='Storming of the Bastille', at='paris')

event('haitian-revolution', 'The Haitian Revolution', 'revolution', (1791, 1804),
      "Enslaved Africans in France's richest colony rose up, beat three empires and founded the free nation of Haiti.",
      scene('The richest colony',
            'Saint-Domingue, the French half of Hispaniola, grew more sugar and coffee than any other colony on Earth. About '
            '500,000 enslaved Africans worked its plantations under some 40,000 whites, and so many died that ships brought '
            'tens of thousands more every year.',
            kick='How it began', y=1789, at='cap_haitien'),
      scene('Bois Caiman',
            'In August 1791 enslaved leaders met at a night ceremony in the forest of Bois Caiman, led, tradition says, by '
            'a Vodou priest, Dutty Boukman. Days later the plantations of the northern plain went up in flames, in the '
            'largest slave revolt in history.',
            y=1791, at='cap_haitien'),
      figure('toussaint-louverture', 'Toussaint',
             'A formerly enslaved coachman, Toussaint Louverture, became the greatest general of the revolt. When France '
             'abolished slavery in 1794 he joined the French and drove out the Spanish and British invaders. By 1801 he '
             'governed the whole island.',
             y=1801),
      cost('Fever',
           'Napoleon wanted the colony, and slavery, back. In 1802 he sent General Leclerc with a great army, and yellow '
           'fever killed most of it, Leclerc too. Toussaint was lured into talks, arrested, and died in a cold French '
           'prison in 1803.',
           num='50,000', of='French soldiers dead, most of fever', y=1803),
      figure('jean-jacques-dessalines', 'Liberty or death',
             "When it was clear that France meant to bring back slavery, Toussaint's general Jean-Jacques Dessalines led the "
             'war to the end. On 18 November 1803 his army beat the French at Vertières, and they left the island.',
             y=1803, at='cap_haitien'),
      turn('Haiti',
           'On 1 January 1804 Dessalines declared independence and gave the country its old Taíno name, Haiti. It was the '
           'first nation founded by people who had freed themselves from slavery, and the second free country in the '
           'Americas.',
           y=1804),
      tale('Freedom soup',
           'Under slavery, pumpkin soup was a dish for the masters. Every 1 January, Haitians eat soup joumou, pumpkin soup, '
           'to celebrate their freedom.',
           y=1804),
      scene('The price of freedom',
            'The great powers shunned the new black republic. In 1825 France, with warships off the coast, made Haiti pay '
            '150 million francs to former slave owners in return for recognition. Haiti was still paying off the loans in '
            'the 1940s.',
            y=1825, at='port_au_prince'),
      legacy('The Haitian Revolution was the only slave revolt in history that founded a nation. It frightened slave owners '
             'across the Americas and inspired enslaved people and abolitionists everywhere, and it helped persuade '
             'Napoleon to sell Louisiana to the United States.',
             'The largest slave revolt in history, 1791',
             'Beat France, Spain and Britain',
             'Haiti free on 1 January 1804'),
      states=['Haiti', 'France'], war='haitian-revolution', wiki='Haitian Revolution')

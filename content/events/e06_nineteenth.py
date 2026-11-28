from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('napoleonic-wars', 'The Napoleonic Wars', 'wars', (1803, 1815),
      'For twelve years Napoleon fought nearly every power in Europe, and redrew its map from Lisbon to Moscow.',
      figure('napoleon', 'An emperor crowns himself',
             'In 1803 Britain and France went back to war after a single year of peace. The next December Napoleon '
             'Bonaparte, the Corsican general who had taken power in France, crowned himself emperor in Notre-Dame, with '
             'the pope looking on. Britain paid one alliance of kings after another to fight him.',
             kick='How it began', img='The Coronation of Napoleon', cap='The coronation, painted by Jacques-Louis David',
             y=1804, at='paris'),
      song('A torn title page',
           'Beethoven had named his new Third Symphony for Bonaparte, the hero of liberty. When he heard that Napoleon '
           'had made himself emperor, his pupil remembered, he raged that this was just another tyrant and scratched '
           'out the name so hard that he tore a hole in the page. He called it Eroica, the heroic symphony.',
           page='Symphony No. 3 (Beethoven)', hint='allegro con brio', y=1804, at='vienna'),
      battle('Trafalgar',
             'In October 1805 Admiral Horatio Nelson attacked the French and Spanish fleets off Cape Trafalgar in Spain, '
             'signalling that England expected every man to do his duty. His ships broke through their line and took or '
             'wrecked 22 of theirs without losing one. Nelson was shot on his deck and died as the battle was won.',
             img='Battle of Trafalgar', y=1805, at='trafalgar'),
      battle('Austerlitz',
             'On land, Napoleon tempted the Austrian and Russian emperors into attacking him near Austerlitz in Moravia, '
             'then smashed the middle of their line as the sun burned through the morning fog. After this Battle of the '
             'Three Emperors, the thousand-year-old Holy Roman Empire was wound up within a year.',
             img='Battle of Austerlitz', y=1805, at='austerlitz'),
      scene('Europe in the family',
            'Prussia was crushed at Jena in 1806, and in 1807 the tsar made peace with Napoleon on a raft in the middle '
            'of the river Niemen at Tilsit. Napoleon made his brothers kings of Holland, Westphalia, Naples and Spain, '
            'and tried to starve Britain by closing every port in Europe to its goods.',
            img='Treaties of Tilsit', y=1807),
      work('The Third of May 1808',
           'When Napoleon put his brother Joseph on the throne of Spain in 1808, Madrid rose against the French, and '
           'rebels were shot the next day. Francisco Goya painted the firing squad: faceless soldiers, and a man in a '
           'white shirt flinging his arms wide. Spain\'s war of ambushes gave the world a word: guerrilla, little war.',
           img='The Third of May 1808', y=1808, at='madrid'),
      cost('The retreat from Moscow',
           'In June 1812 Napoleon led about 600,000 men into Russia. The Russians fell back, burning what they left, and '
           'Moscow burned soon after he entered it. No peace was offered, so he turned back as winter came. Starving, '
           'frozen and hunted by Cossacks, his army fought its way over the Berezina River in November.',
           num='600,000', of='men invaded; only a fraction came back', img='French invasion of Russia', y=1812,
           at='berezina'),
      battle('Waterloo',
             'Beaten at Leipzig in 1813, Napoleon gave up his throne and was sent to rule the little island of Elba. In '
             '1815 he escaped and marched on Paris, and France rallied to him for a hundred days. On 18 June, near '
             'Waterloo in Belgium, the Duke of Wellington\'s army held out until the Prussians came, and Napoleon\'s last '
             'army broke.',
             img='Battle of Waterloo', y=1815, at='waterloo'),
      legacy('The wars killed millions and ended with Napoleon a prisoner on St Helena, far out in the South Atlantic. '
             'But they spread his law code and the idea of the nation across Europe, swept away the Holy Roman Empire and '
             'loosened Spain\'s hold on America, and left Britain the leading power of the century.',
             'Napoleon crowned himself emperor in 1804',
             'Trafalgar and Austerlitz, 1805',
             'The march on Moscow, 1812',
             'Waterloo ended it in 1815'),
      war='napoleonic-wars', wiki='Napoleonic Wars', img='Napoleon Crossing the Alps')

event('war-of-1812', 'The War of 1812', 'war', (1812, 1815),
      'The young United States went to war with Britain, invaded Canada, saw its capital burned and found an anthem.',
      scene('Sailors and the west',
            'Fighting Napoleon, Britain stopped American ships trading with France and took thousands of sailors off them '
            'for its navy, saying they were British deserters. In the west, Americans blamed Britain for arming the '
            'Native nations that resisted settlers. In June 1812 Congress declared war.',
            kick='How it began', y=1812, at='washington'),
      battle('Canada holds',
             'Americans expected Canada to fall easily: one former president called taking it a mere matter of marching. '
             'Instead British soldiers, Canadian militia and Native allies threw back invasion after invasion. At '
             'Queenston Heights in 1812 the British general Isaac Brock was killed leading a charge, but his side won.',
             img='Battle of Queenston Heights', y=1812, at='niagara'),
      figure('tecumseh', 'Tecumseh',
             'The Shawnee leader Tecumseh had travelled from the Great Lakes to the Gulf, urging Native nations to unite '
             'and hold on to their land. He sided with the British, helped take Detroit in 1812, and was killed at the '
             'Battle of the Thames in Upper Canada in October 1813. His dream of a Native confederacy died with him.',
             y=1813, at='moraviantown'),
      scene('Washington burns',
            'In August 1814 British troops marched into Washington. Dolley Madison, the president\'s wife, fled the '
            'President\'s House after making sure a portrait of George Washington was saved. That night British officers '
            'ate the dinner left on the table, then set the house and the Capitol alight, in revenge for the Americans '
            'burning York, the capital of Upper Canada.',
            img='Burning of Washington', y=1814, at='washington'),
      song('The Star-Spangled Banner',
           'Weeks later the British navy bombarded Fort McHenry, which guarded Baltimore, through a rainy night. Francis '
           'Scott Key, a lawyer held on a ship in the harbour, saw at dawn that the fort\'s huge flag still flew, and '
           'wrote a poem about it. Sung to the tune of a London club song, it became the national anthem in 1931.',
           page='The Star-Spangled Banner', hint='instrumental band', y=1814, at='baltimore'),
      turn('Peace at Ghent',
           'Both sides were tired of a war that neither could win. On Christmas Eve 1814 diplomats in Ghent, in what is '
           'now Belgium, signed a peace that gave back everything taken and settled nothing about the sailors. News '
           'crossed the Atlantic slowly, so the fighting went on for weeks.',
           y=1814, at='ghent'),
      battle('New Orleans',
             'In January 1815, before word of the peace arrived, a British army attacked New Orleans. Andrew Jackson\'s '
             'mixed force of soldiers, militia, free Black volunteers, Choctaw warriors and even pirates shot it to '
             'pieces from behind earthworks. Some 2,000 British were killed, wounded or taken, against about 70 '
             'Americans. Jackson became a hero, and later president.',
             img='Battle of New Orleans', y=1815, at='new_orleans'),
      legacy('The war ended in a draw, but each side remembered winning: Americans felt they had won their independence a '
             'second time, Canadians that they had saved their country, and the British hardly remembered it. The '
             'real losers were the Native nations of the Great Lakes, left by their British allies to face American '
             'expansion alone.',
             'Declared by the United States in June 1812',
             'Washington was burned in 1814',
             'The Star-Spangled Banner was written at Baltimore',
             'New Orleans was fought after the peace'),
      war='war-of-1812', wiki='War of 1812', img='Star-Spangled Banner (flag)')

event('greek-independence', 'Serbia and Greece break free', 'independence', (1804, 1832),
      'First the Serbs, then the Greeks rose against Ottoman rule, and in the end Europe\'s great powers sailed in to help.',
      scene('The Serbs rise',
            'In 1804, after renegade Ottoman soldiers murdered dozens of Serbian village leaders, the survivors met at '
            'Orašac and chose a pig trader, Karađorđe, Black George, to lead a rising. It grew into a war for freedom. '
            'Crushed in 1813, it flared again in 1815, and by 1830 Serbia ruled itself as a princedom inside the empire.',
            kick='How it began', img='First Serbian Uprising', y=1804, at='orasac'),
      scene('The Greeks rise',
            'Greek merchants abroad had formed a secret society, the Friendly Society, to free Greece. In March 1821 '
            'risings broke out in the Peloponnese, and within months the rebels held much of the south. Both sides '
            'killed civilians: when the Greeks took Tripolitsa that autumn, thousands of its Muslims and Jews were '
            'massacred.',
            y=1821, at='tripolitsa'),
      figure(None, 'Bouboulina',
             'Laskarina Bouboulina, a twice-widowed ship owner from the island of Spetses, spent her fortune on the '
             'revolution. She commanded her own ships in the blockade of Nafplio and rode into Tripolitsa when it fell. '
             'Greeks remember her as a heroine of the war; she was shot dead in a family feud in 1825.',
             img='Laskarina Bouboulina', y=1821, at='nafplio'),
      cost('Chios',
           'In 1822 an Ottoman force landed on the rich island of Chios, which had been drawn into the revolt. Tens of '
           'thousands of Greeks were killed, and tens of thousands more were sold as slaves. Eugène Delacroix painted the '
           'horror in a huge canvas that turned many Europeans toward the Greek cause.',
           num='Tens of thousands', of='of islanders killed or enslaved', img='The Massacre at Chios', y=1822,
           at='chios'),
      figure(None, 'Lord Byron',
             'Europe\'s educated classes had grown up on ancient Greek books, and many saw the war as the land of '
             'democracy rising again. The English poet Lord Byron spent a fortune on Greek forces and went to fight '
             'himself, but caught a fever at Missolonghi and died there in April 1824, aged 36. Greeks still honour him.',
             img='Lord Byron', y=1824, at='missolonghi'),
      figure('ibrahim-pasha-of-egypt', 'Egypt joins in',
             'With the rebels fighting among themselves, the sultan called on Muhammad Ali, the powerful governor of '
             'Egypt. In 1825 his son Ibrahim landed in the Peloponnese with a modern army and began to win it back. '
             'Missolonghi fell in 1826 after a year\'s siege, when its starving people tried to break out by night and '
             'most were cut down.',
             y=1826, at='missolonghi'),
      battle('Navarino',
             'Britain, France and Russia decided to force a truce. In October 1827 their fleets sailed into the bay of '
             'Navarino, where the Ottoman and Egyptian fleet lay at anchor. A shot was fired, and a battle nobody had '
             'ordered began. In four hours most of the Ottoman ships were sunk or burned. It was the last great battle '
             'of wooden sailing ships.',
             img='Battle of Navarino', y=1827, at='navarino'),
      turn('A kingdom of Greece',
           'After losing another war to Russia, the sultan gave way. In 1830 the powers declared Greece independent, and '
           'in 1832 they gave it a king: Otto, a 17-year-old Bavarian prince. The new state was small and left most '
           'Greeks outside it, and the dream of gathering them in drove its wars for the next century.',
           y=1832, at='nafplio'),
      legacy('Serbia and Greece were the first nations to win their freedom from the Ottoman Empire, and the other '
             'peoples of the Balkans followed over the next hundred years. Greece also showed how public feeling in '
             'Europe, stirred up by poets and painters, could pull great powers into a faraway war.',
             'The Serbian rising began in 1804',
             'The Greek revolution began in 1821',
             'Byron died for Greece at Missolonghi',
             'Navarino, 1827: the last battle of sailing fleets'),
      states=('Greece', 'Serbia'), war='serbian-greek-independence', wiki='Greek War of Independence')

event('latin-american-independence', 'Latin America breaks free', 'independence', (1808, 1826),
      'When Napoleon seized Spain, its American empire began to break away, and in 18 years almost all of it was free.',
      scene('A king in prison',
            'In 1808 Napoleon forced the king of Spain to give up his throne and put his own brother on it. In the '
            'Americas, Spain\'s colonists had to decide whom to obey. City councils from Caracas to Buenos Aires set up '
            'their own governments, at first in the captive king\'s name, then more and more for themselves.',
            kick='How it began', y=1810, at='buenos_aires'),
      figure('miguel-hidalgo-y-costilla', 'The cry of Dolores',
             'In New Spain, now Mexico, a village priest, Miguel Hidalgo, rang his church bell in Dolores at dawn on 16 '
             'September 1810 and called his people to rise. Tens of thousands of poor farmers and Native people followed '
             'him, but his army was beaten, and he was caught and shot in 1811. Mexicans still celebrate his cry on '
             'their independence day.',
             y=1810, at='dolores'),
      figure('jose-de-san-martin', 'Over the Andes',
             'In the south José de San Martín, an Argentine who had fought for Spain against Napoleon, trained an army at '
             'Mendoza and in 1817 led it across the Andes by passes nearly 4,000 metres high. He beat the Spanish at '
             'Chacabuco and freed Chile with Bernardo O\'Higgins, then sailed north and declared Peru independent in 1821.',
             y=1817, at='chacabuco'),
      figure('simon-bolivar', 'The Liberator',
             'Simón Bolívar, a rich Venezuelan who had sworn on a hill in Rome to free his homeland, lost battles and was '
             'driven into exile more than once. In 1819 he led his army over the freezing Andes, where many died of '
             'cold, and surprised the Spanish at Boyacá. The victory freed New Granada, today\'s Colombia.',
             y=1819, at='boyaca'),
      figure('pedro-i-of-brazil', 'Brazil goes its own way',
             'Portugal\'s great colony took a gentler path. Its royal family had fled Napoleon to Rio de Janeiro in 1808. '
             'When the king went home, his son Pedro stayed, and in September 1822, by a stream called the Ipiranga, he '
             'declared Brazil independent. It became an empire, with Pedro as its first emperor.',
             y=1822, at='ipiranga'),
      turn('Ayacucho',
           'Peru was Spain\'s last stronghold. San Martín met Bolívar at Guayaquil in 1822, then stepped aside and left '
           'for Europe; no one knows what they said. In December 1824 Bolívar\'s general Antonio José de Sucre beat the '
           'last big royal army at Ayacucho, high in the Andes. Spanish rule in South America was over.',
           img='Battle of Ayacucho', y=1824, at='ayacucho'),
      tale('Ploughing the sea',
           'Bolívar dreamed of one great American nation, but his Gran Colombia, which joined today\'s Venezuela, '
           'Colombia, Ecuador and Panama, fell apart in quarrels. Sick and bitter, he wrote in 1830 that those who had '
           'served the revolution had ploughed the sea. He died that December, aged 47.',
           y=1830),
      legacy('In under twenty years Spain lost an empire it had held for three centuries, and new countries were born from '
             'Mexico to Argentina. But independence often left the old landowners in charge, and many of the new states '
             'fell into civil wars and rule by strongmen. Bolívar is honoured across the continent; Bolivia is named '
             'after him.',
             'Hidalgo\'s cry of Dolores, 16 September 1810',
             'San Martín crossed the Andes in 1817',
             'Brazil broke away from Portugal in 1822',
             'Ayacucho ended Spanish rule in South America, 1824'),
      states=('Viceroyalty of Brazil', 'Empire of Brazil', 'Paraguay', 'Mexican Empire', 'Mexico', 'Federal Republic of Central America',
              'Gran Colombia', 'Republic of New Granada', 'Venezuela', 'Ecuador', 'Peru', 'Bolivia', 'Chile',
              'United Provinces of the Río de la Plata', 'Uruguay'),
      war='spanish-american-independence', wiki='Latin American wars of independence', img='Battle of Boyacá')

event('trail-of-tears', 'The Trail of Tears', 'migration', (1830, 1850),
      'The United States forced the Cherokee and other nations of the southeast from their homelands to the far west.',
      figure('sequoyah', 'Talking leaves',
             'Sequoyah, a Cherokee silversmith who could not read any language, spent years working out a sign for each '
             'syllable of his own. When he showed his system in 1821 it was so easy that thousands of Cherokee learned '
             'to read and write within a few years, and in 1828 they began a newspaper printed in it.',
             kick='A nation that wrote', y=1821),
      scene('Gold in Georgia',
            'The southeast was still home to the Cherokee, Muscogee (Creek), Chickasaw, Choctaw and Seminole nations. The '
            'Cherokee had a written constitution and a capital at New Echota in Georgia; many farmed, and some ran '
            'plantations worked by enslaved Black people. Then in 1829 gold was found on their land, and settlers '
            'poured in.',
            y=1829, at='new_echota'),
      figure('andrew-jackson', 'The Indian Removal Act',
             'President Andrew Jackson, who had made his name fighting the Creek, wanted all the nations moved west of '
             'the Mississippi. In 1830 Congress passed the Indian Removal Act by a handful of votes. The Choctaw were '
             'moved first, in winters so cruel that one of their chiefs called it a trail of tears and death.',
             y=1830, at='washington'),
      turn('The court says no',
           'The Cherokee fought in the courts, and in 1832 the Supreme Court ruled that Georgia had no power over their '
           'land. Georgia ignored it, and Jackson did nothing to make it obey. In 1835 a small group of Cherokee signed '
           'away the nation\'s land at New Echota; the chief, John Ross, and most of his people never agreed.',
           y=1835, at='new_echota'),
      cost('The trail',
           'In 1838 soldiers rounded up some 16,000 Cherokee into camps, then sent them more than 1,500 kilometres west '
           'through autumn and winter, many on foot. Sickness, cold and hunger killed thousands on the way, the old and '
           'the young hardest of all. The Cherokee remember it as the trail where they cried.',
           num='About 4,000', of='Cherokee died, by most estimates', img='Trail of Tears', y=1838),
      scene('Indian Territory',
            'The survivors rebuilt in Indian Territory, now Oklahoma, and in 1839 made Tahlequah their capital. In '
            'Florida the Seminole fought removal in long wars, and some were never moved. By 1850 most of the '
            'southeast\'s Native people had been driven west, and their land had gone to white settlers, much of it for '
            'cotton grown by enslaved people.',
            y=1839, at='tahlequah'),
      legacy('About 60,000 people of the five nations were forced from their homes, in one of the darkest chapters of '
             'American history. The Cherokee Nation rebuilt in Oklahoma, and today it is the largest tribe in the United '
             'States, still governed from Tahlequah, where children learn to read in Sequoyah\'s letters.',
             'The Indian Removal Act, 1830',
             'The Cherokee were marched west in 1838 and 1839',
             'Thousands died on the way',
             'Sequoyah gave the Cherokee their writing'),
      states=('United States',), wiki='Trail of Tears', at='new_echota',
      label='Forced removal')

event('opium-wars', 'The Opium Wars', 'wars', (1839, 1860),
      'Britain went to war to keep selling opium in China, and the Qing empire began a century of humiliation.',
      scene('Tea for opium',
            'Britain bought huge amounts of Chinese tea, but China wanted little that Britain made, so silver drained '
            'east. The answer the British East India Company found was opium, grown in India and smuggled into China '
            'through Canton. By the 1830s millions of Chinese were addicted, and silver was flowing out of China instead.',
            kick='How it began', y=1830, at='canton'),
      figure('lin-zexu', 'Commissioner Lin',
             'In 1839 the emperor sent an upright official, Lin Zexu, to Canton to stamp out the trade. Lin shut in the '
             'foreign merchants until they handed over more than 1,000 tonnes of opium, then had it mixed with lime and '
             'salt and washed out to sea at Humen. He even wrote to Queen Victoria asking how she would like her own '
             'people poisoned.',
             y=1839, at='humen'),
      battle('Gunboats',
             'Britain sent warships. The iron steamship Nemesis sailed up shallow rivers and blew Chinese war junks to '
             'pieces. British forces took the forts of Canton, then sailed up the Yangtze and threatened Nanjing. China\'s '
             'armies, with old guns and older tactics, could not stop them.',
             img='Nemesis (1839)', y=1841, at='canton'),
      turn('The Treaty of Nanjing',
           'In 1842 China signed the first of what Chinese call the unequal treaties. It paid Britain millions of silver '
           'dollars, opened five ports to British trade and gave up the island of Hong Kong, which Britain ruled until '
           '1997. The opium trade carried on, bigger than ever.',
           img='Treaty of Nanking', y=1842, at='nanjing'),
      scene('A second war',
            'In 1856 Chinese officials boarded the Arrow, a ship flying the British flag, and Britain, now joined by '
            'France, went to war again. Their forces took Canton and the forts guarding Tianjin, and in 1858 China agreed '
            'to open more ports, let foreign ships use its rivers, let missionaries travel and, at last, to make opium '
            'legal.',
            y=1858, at='tianjin'),
      scene('The Summer Palace burns',
            'When China held out, British and French troops marched on Beijing in 1860. Envoys sent to talk were seized, '
            'and many of them died after torture. In revenge the British commander, Lord Elgin, had the emperor\'s Garden '
            'of Perfect Brightness looted and burned. It took thousands of soldiers two days, and smoke hung over the '
            'city.',
            img='Old Summer Palace', y=1860, at='beijing'),
      legacy('The wars showed that the Qing empire, the richest in the world a century before, could not defend itself '
             'against industrial Europe. Chinese call 1839 to 1949 the century of humiliation, and it still colours how '
             'China sees the West. Lin Zexu is a national hero, and the world day against drugs, 26 June, recalls '
             'his work at Humen.',
             'Lin Zexu destroyed the opium at Humen, 1839',
             'Hong Kong was given up to Britain in 1842',
             'The Summer Palace was burned in 1860',
             'The start of a century of humiliation'),
      war='opium-wars', wiki='Opium Wars')

event('irish-famine', 'The Great Famine in Ireland', 'famine', (1845, 1852),
      'A blight destroyed the potatoes that a third of Ireland lived on. A million people died and a million more left.',
      scene('A country fed on potatoes',
            'In the 1840s Ireland, ruled from London since 1801, had about eight and a half million people. Most were '
            'poor tenants on small plots, and about a third of them lived almost wholly on potatoes. In September 1845 a '
            'blight, a mould from America, turned the crop black and rotten in the ground.',
            kick='How it began', y=1845),
      scene("Black '47",
            'The blight came back year after year. 1847, remembered as Black \'47, was the worst: families died of hunger '
            'and of the fevers that came with it, in their cabins, on the roads and in crowded workhouses. In Skibbereen, '
            'in County Cork, visitors found whole villages of the dead and dying.',
            img='Great Famine (Ireland)', y=1847, at='skibbereen'),
      turn('Food leaving Ireland',
           'Even in the worst years ships carried grain, cattle and butter out of Ireland, sold to those who could pay. '
           'The British government believed the market should be left alone. It closed its soup kitchens after a few '
           'months in 1847 and left relief to local taxes and workhouses. Charles Trevelyan, who ran it, called the '
           'famine a judgement of God.',
           y=1847, at='dublin'),
      tale('The Choctaw gift',
           'In 1847 the Choctaw Nation, driven from its own land on the Trail of Tears only 16 years before, collected '
           '170 dollars for the starving Irish. Gifts came from around the world, from the Ottoman sultan to people in '
           'Calcutta. In 2017 a sculpture of nine steel feathers was unveiled in County Cork to say thank you.',
           img='Kindred Spirits (sculpture)', y=1847),
      cost('A million dead',
           'Between 1845 and 1852 about a million people died. A million or more left on crowded, fever-ridden ships, '
           'the coffin ships, for Britain, Canada and the United States. Landlords evicted tens of thousands of families '
           'who could not pay their rent, and knocked down their cabins so they could not come back.',
           num='About a million', of='people died of hunger and disease', y=1849),
      scene('Leaving',
            'The leaving never stopped. Ireland\'s people fell from 8.5 million to about 6.5 million in ten years, and '
            'kept falling for a century: the island still has fewer people today than it had in 1841. The Irish built new '
            'lives in Boston, New York, Liverpool and Sydney, and tens of millions around the world now have Irish '
            'roots.',
            y=1851, at='new_york'),
      legacy('The famine changed Ireland for ever. It emptied the countryside, made emigration a way of life and left a '
             'bitterness toward British rule that fed the struggle for independence. Every year Ireland holds a day to '
             'remember the Great Hunger, and it gives generously to fight famine elsewhere.',
             'The potato blight struck in 1845',
             'About a million died, and as many emigrated',
             'Ireland has fewer people today than in 1841'),
      states=('United Kingdom of Great Britain and Ireland',), wiki='Great Famine (Ireland)', at='skibbereen')

event('mexican-american-war', 'The Mexican-American War', 'war', (1846, 1848),
      'The United States invaded Mexico and took about half its land, from Texas to California.',
      scene('Texas',
            'Mexico won its independence from Spain in 1821 and let American settlers into its northern province of '
            'Texas. They brought enslaved people, though Mexico had banned slavery, and in 1835 they rebelled. After the '
            'fall of the Alamo and a Mexican defeat at San Jacinto, Texas broke away in 1836, and in 1845 the United '
            'States took it in.',
            kick='How it began', img='Battle of the Alamo', y=1836, at='alamo'),
      figure('james-k-polk', 'Manifest destiny',
             'President James K. Polk believed, like many Americans, that it was their manifest destiny to spread across '
             'the continent, and he wanted California. When Mexico would not sell, he sent troops into land both sides '
             'claimed. After a clash in April 1846 he told Congress that American blood had been shed on American soil.',
             y=1846, at='washington'),
      figure('antonio-lopez-de-santa-anna', 'A leg in Illinois',
             'Mexico\'s general Santa Anna, who led the country eleven times, had lost a leg fighting the French in 1838 '
             'and buried it with full military honours. At Cerro Gordo in April 1847 he fled so fast that soldiers from '
             'Illinois captured his cork leg. It is still in a museum in Springfield, Illinois.',
             y=1847, at='cerro_gordo'),
      battle('Chapultepec',
             'General Winfield Scott landed at Veracruz in 1847 and fought his way inland to Mexico City. In September his '
             'troops stormed the castle of Chapultepec. Mexicans remember six young cadets, the Niños Héroes, who died '
             'defending it; legend says the last of them wrapped himself in the flag and leapt from the walls.',
             img='Battle of Chapultepec', y=1847, at='chapultepec'),
      figure('abraham-lincoln', 'Spotty Lincoln',
             'Many Americans opposed the war as a grab for land that would spread slavery. A young congressman, Abraham '
             'Lincoln, demanded to know the exact spot where American blood had been shed, and was mocked as Spotty '
             'Lincoln. The writer Henry David Thoreau went to jail rather than pay his taxes, and wrote an essay on civil '
             'disobedience.',
             y=1847, at='washington'),
      turn('Half of Mexico',
           'In the Treaty of Guadalupe Hidalgo, in February 1848, Mexico accepted the loss of Texas and gave up '
           'California, Nevada, Utah and most of Arizona and New Mexico for 15 million dollars. The Mexicans living there '
           'became Americans overnight: as their descendants say, they did not cross the border; the border crossed them.',
           img='Treaty of Guadalupe Hidalgo', y=1848, at='mexico_city'),
      scene('Gold',
            'Days before the treaty was signed, a carpenter building a sawmill in California found flakes of gold in the '
            'stream. The gold rush that followed brought some 300,000 people in a few years and made California a state '
            'by 1850. The fight over whether the new lands would allow slavery helped lead to the Civil War.',
            img='California gold rush', y=1848, at='coloma'),
      legacy('The United States reached the Pacific, and Mexico lost about half its land and gained a lasting distrust of '
             'its northern neighbour. Ulysses Grant, who fought in it as a young officer, later called it one of the most '
             'unjust wars ever waged by a stronger nation against a weaker one.',
             'Began over Texas in 1846',
             'Mexico City fell in September 1847',
             'Mexico gave up about half its land in 1848',
             'The new lands reopened the fight over slavery'),
      states=('Mexico', 'United States'), war='mexican-american-war', wiki='Mexican–American War')

event('revolutions-of-1848', 'The revolutions of 1848', 'revolution', (1848, 1849),
      'In a few weeks of 1848 revolution swept from Paris to Berlin, Vienna and Budapest. Within two years most had failed.',
      scene('The springtime of peoples',
            'After bad harvests and hard times, Paris rose in February 1848, and King Louis Philippe slipped away to '
            'England in disguise. France became a republic again. The news spread fast, and within weeks crowds were '
            'building barricades in Vienna, Berlin, Milan, Munich and Budapest.',
            kick='How it began', y=1848, at='paris'),
      figure('karl-marx', 'A spectre over Europe',
             'Weeks before, two young Germans, Karl Marx and Friedrich Engels, had published a pamphlet in London for a '
             'small workers\' league. The Communist Manifesto began by saying that a spectre was haunting Europe, the '
             'spectre of communism, and ended by calling on the workers of all countries to unite. Few read it then; in '
             'the next century it shaped the lives of millions.',
             y=1848, at='london'),
      figure('klemens-von-metternich', 'Metternich falls',
             'In Vienna students and workers rose in March. Prince Metternich, who had kept the old order in Europe since '
             'Napoleon\'s fall, resigned and fled to England. The emperor promised a constitution, and that autumn the '
             'empire\'s peasants were freed from the unpaid work they owed their lords: one change of 1848 that lasted.',
             y=1848, at='vienna'),
      scene('A parliament for Germany',
            'In May hundreds of elected men met in St Paul\'s Church in Frankfurt to make one Germany out of its 39 '
            'states. They argued for nearly a year about its rights and its borders. When they finally offered the crown '
            'of all Germany to the king of Prussia, he turned it down, calling it in private a crown from the gutter.',
            img='Frankfurt Parliament', y=1848, at='frankfurt'),
      figure('lajos-kossuth', 'Hungary fights',
             'Hungary went furthest. Led by Lajos Kossuth, a lawyer and fiery speaker, it won its own government, went '
             'to war with Austria, and in April 1849 declared itself independent. The young emperor Franz Joseph asked '
             'the tsar for help, and some 200,000 Russian soldiers marched in. In August the Hungarians surrendered.',
             y=1849, at='budapest'),
      turn('The kings come back',
           'The rebels were split: middle-class liberals wanted constitutions, workers wanted bread and jobs, and '
           'nationalists wanted countries of their own, often on the same land. One by one the old rulers\' armies took '
           'back control. In France voters made Napoleon\'s nephew president, and in 1852 he made himself emperor.',
           y=1849),
      scene('The Forty-Eighters',
            'Thousands of beaten revolutionaries fled abroad. Many Germans settled in the United States, where these '
            'Forty-Eighters started newspapers, spoke out against slavery and fought for the Union in the Civil War. '
            'Kossuth toured America to cheering crowds.',
            y=1851, at='new_york'),
      legacy('Almost every revolution of 1848 failed, but much of what the rebels wanted came later. Serfdom never came '
             'back in Austria, Prussia and Piedmont kept parliaments, and within a generation Italy and Germany were '
             'united, though by kings and generals rather than by the people.',
             'Began in Paris in February 1848',
             'Reached some 50 countries and states',
             'The Communist Manifesto came out the same year',
             'Nearly all were defeated by 1849'),
      states=('France', 'Austrian Empire', 'Prussia', 'Bavaria', 'Baden', 'Saxony', 'Württemberg', 'Hanover', 'Lombardy',
              'Venetia', 'Kingdom of Sardinia', 'Kingdom of the Two Sicilies', 'Papal States', 'Tuscany', 'Denmark'),
      wiki='Revolutions of 1848', at='paris')

event('taiping-rebellion', 'The Taiping Rebellion', 'civil-war', (1850, 1864),
      'A failed exam candidate who believed he was the younger brother of Jesus led a rising in which tens of millions died.',
      figure('hong-xiuquan', 'A heavenly vision',
             'Hong Xiuquan, a village teacher from near Canton, failed the imperial exams four times. After one failure '
             'he fell ill and saw visions, and years later, reading a Christian pamphlet, he decided they meant that he '
             'was the younger brother of Jesus, sent to rid China of demons: by which he came to mean its Manchu rulers.',
             kick='How it began', y=1843, at='guangzhou'),
      scene('The Heavenly Kingdom',
            'His God Worshipping Society drew in poor miners, farmers and Hakka people in Guangxi province. In 1851 Hong '
            'declared the Heavenly Kingdom of Great Peace, Taiping Tianguo. His followers grew their hair long, refusing '
            'the shaved forehead and braid the Manchus forced on men, and banned opium, gambling, alcohol and the binding '
            'of girls\' feet.',
            y=1851, at='jintian'),
      battle('The Heavenly Capital',
             'The Taiping swept north into the Yangtze valley, and in March 1853 they took Nanjing, the old southern '
             'capital, and killed its Manchu people. Hong renamed it Tianjing, the Heavenly Capital, and ruled from a '
             'palace there for eleven years. An army he sent north to take Beijing got close to Tianjin before it was '
             'destroyed.',
             y=1853, at='nanjing'),
      scene('A new order',
            'In Taiping lands men and women lived apart, even husbands and wives, and women served as soldiers and '
            'officials. Land was to be shared out equally and goods held in common. But Hong withdrew into his palace, '
            'and in 1856 his leaders turned on each other: one of them, the East King, was killed with thousands of his '
            'followers.',
            y=1856, at='nanjing'),
      figure('zeng-guofan', 'The scholar general',
             'The Qing\'s own armies were rotten, so a Confucian scholar from Hunan, Zeng Guofan, raised a new one from '
             'his home province, paid for by local taxes and loyal to its own officers. His Xiang Army fought its way down '
             'the Yangtze year by year, winning back city after city.',
             y=1860, at='changsha'),
      figure('charles-george-gordon', 'The Ever-Victorious Army',
             'The Western powers, at first curious about Chinese Christians, decided they would rather have a weak Qing '
             'that kept its treaties. Around Shanghai a force of Chinese soldiers with foreign officers, the '
             'Ever-Victorious Army, fought for the Qing, led from 1863 by a British officer, Charles Gordon, later known '
             'as Chinese Gordon.',
             y=1863, at='shanghai'),
      cost('The fall of Nanjing',
           'In June 1864 Hong died, ill, as Zeng\'s armies closed in. In July they broke into Nanjing and killed perhaps '
           '100,000 people there. The fighting dragged on for years more, and whole districts of the Yangtze valley were '
           'left empty. It was the deadliest civil war in history.',
           num='20 to 30 million', of='people died, most of hunger and disease', y=1864, at='nanjing'),
      legacy('The Qing survived, but weaker, and leaning on regional armies like Zeng\'s whose generals became the warlords '
             'of the next century. Sun Yat-sen, who overthrew the dynasty in 1911, grew up on tales of the Taiping and '
             'called himself a second Hong Xiuquan, and China\'s Communists praised them as early revolutionaries.',
             'Hong Xiuquan said he was the brother of Jesus',
             'Nanjing was the Taiping capital from 1853 to 1864',
             'Perhaps 20 to 30 million died',
             'The deadliest civil war in history'),
      war='taiping-rebellion', wiki='Taiping Rebellion')

event('crimean-war', 'The Crimean War', 'war', (1853, 1856),
      'Britain, France and the Ottomans fought Russia in a war of blunders and cholera, and modern nursing was born.',
      scene('Keys to a church',
            'It began with a quarrel over who held the keys of the Church of the Nativity in Bethlehem: Catholic monks '
            'backed by France, or Orthodox ones backed by Russia. Behind it lay a bigger question: who would gain as the '
            'Ottoman Empire, the sick man of Europe, grew weaker. In 1853 Russia marched into Ottoman lands on the Danube.',
            kick='How it began', y=1853),
      battle('Sinop',
             'In November 1853 a Russian fleet caught Ottoman ships in the harbour of Sinop on the Black Sea and '
             'destroyed them with new exploding shells, killing some 3,000 men. Britain and France, fearing that Russia '
             'would take Constantinople, declared war in March 1854.',
             img='Battle of Sinop', y=1853, at='sinop'),
      battle('The Charge of the Light Brigade',
             'The allies landed in Crimea to take Sevastopol, Russia\'s great naval base. At Balaklava in October 1854 a '
             'muddled order sent some 670 British light cavalry straight down a valley into Russian guns on three sides. '
             'Within minutes over a third were killed, wounded or taken. A French general watching said it was '
             'magnificent, but it was not war.',
             img='Charge of the Light Brigade', y=1854, at='balaklava'),
      work('Theirs but to do and die',
           'The poet Alfred Tennyson read the report in The Times and wrote a poem, it is said, within minutes. Its lines '
           'about the six hundred riding into the valley of Death, theirs not to reason why, made the charge a legend of '
           'courage, and of the waste of it.',
           img='The Charge of the Light Brigade (poem)', y=1854),
      figure('florence-nightingale', 'The lady with the lamp',
             'Reports of wounded men dying in filth shocked Britain. Florence Nightingale took 38 nurses to the army '
             'hospital at Scutari, across from Constantinople. She fought the army for supplies, cleaned the wards and '
             'walked them at night with a lamp. Deaths fell sharply once the drains were fixed in 1855, and she used '
             'charts to prove why.',
             y=1854, at='scutari'),
      figure(None, 'Mother Seacole',
             'Mary Seacole, a Jamaican nurse and businesswoman, offered to join the army nurses and was turned away. She '
             'paid her own way to Crimea and built the British Hotel near Balaklava, selling food and supplies to '
             'officers and nursing wounded men, sometimes on the battlefield itself. Soldiers called her Mother Seacole.',
             img='Mary Seacole', y=1855, at='balaklava'),
      figure('leo-tolstoy', 'Inside Sevastopol',
             'The allies besieged Sevastopol for almost a year. Inside, a young Russian artillery officer, Leo Tolstoy, '
             'wrote sketches of the siege that made his name. In September 1855 the French stormed the Malakhov fort, '
             'and the Russians left the burning city. Tolstoy went on to write War and Peace.',
             y=1855, at='sevastopol'),
      made('The war reporters',
           'William Howard Russell of The Times sent home some of the first reports from a front line, and Roger Fenton '
           'hauled a darkroom van around Crimea to take some of the first photographs of a war.',
           'For the first time people at home learned within weeks what their soldiers suffered, and governments could no '
           'longer hide it.',
           img='The Valley of the Shadow of Death (photograph)', y=1855, at='balaklava'),
      legacy('The war ended with the Treaty of Paris in 1856, which kept Russian warships out of the Black Sea. Perhaps '
             'half a million men died, far more of cholera and dysentery than of wounds. Defeat pushed the new tsar to '
             'free Russia\'s serfs in 1861, and Nightingale made nursing a respected profession.',
             'Russia against Britain, France, the Ottomans and Sardinia',
             'The Charge of the Light Brigade, 1854',
             'Florence Nightingale changed army nursing',
             'Most of the dead died of disease'),
      war='crimean-war', wiki='Crimean War')

event('indian-rebellion-1857', 'The Indian Rebellion of 1857', 'uprising', (1857, 1858),
      'Indian soldiers rose against the British East India Company, and the fighting ended the Company\'s rule of India.',
      scene('Greased cartridges',
            'The East India Company ruled much of India with an army of Indian soldiers, called sepoys. Anger had been '
            'growing over kingdoms taken over, taxes and missionaries. Then came a new rifle whose paper cartridges, the '
            'soldiers heard, were greased with cow and pig fat and had to be bitten open: an insult to Hindus and '
            'Muslims alike.',
            kick='How it began', y=1857, at='barrackpore'),
      figure(None, 'Mangal Pandey',
             'In March 1857, at Barrackpore near Calcutta, a sepoy named Mangal Pandey attacked his British officers. He '
             'was hanged, and his regiment was broken up. The British called the rebels pandies after him; to Indians '
             'today he is one of the first heroes of the struggle for freedom.',
             img='Mangal Pandey', y=1857, at='barrackpore'),
      turn('Meerut and Delhi',
           'In May, at Meerut, 85 soldiers who had refused the cartridges were chained and jailed. The next evening their '
           'comrades rose, freed them, killed British officers and civilians, and rode through the night to Delhi. There '
           'they proclaimed the old Mughal emperor, Bahadur Shah Zafar, ruler of India once more.',
           y=1857, at='meerut'),
      scene('The rising spreads',
            'The revolt spread across the north, to Lucknow, Kanpur and Jhansi, joined by princes who had lost their '
            'lands and peasants with grievances of their own. Both sides killed without mercy. At Kanpur British women '
            'and children were massacred after the garrison surrendered, and British columns took revenge by hanging '
            'and burning whole villages.',
            y=1857, at='kanpur'),
      figure('bahadur-shah-zafar', 'The last Mughal',
             'In September, after a long siege, British and loyal Indian troops, many of them Sikhs and Gurkhas, stormed '
             'Delhi street by street. Bahadur Shah Zafar, a poet of 82, was caught and sent into exile in Burma, and his '
             'sons were shot. In Lucknow the besieged British residency held out for months until it was relieved.',
             y=1857, at='delhi'),
      figure('rani-of-jhansi', 'The Rani of Jhansi',
             'Lakshmibai, the young widowed queen of Jhansi, whose kingdom the Company had taken because she had no son '
             'of her own, became the rising\'s most famous leader. When the British stormed Jhansi in 1858 she escaped, '
             'the story goes, with her adopted son tied to her back. She was killed fighting near Gwalior, dressed as a '
             'cavalry soldier.',
             y=1858, at='gwalior'),
      turn('The Crown takes over',
           'In 1858 Parliament ended the East India Company\'s rule, and India passed to the British Crown, governed by a '
           'viceroy for Queen Victoria, who later took the title Empress of India. The Mughal Empire was ended for good, '
           'and the British promised not to meddle with Indian religions or take more princes\' lands.',
           y=1858, at='calcutta'),
      legacy('Many thousands died on both sides, and the bitterness lasted. The British ruled more warily afterwards, '
             'leaning on princes and landlords. For Indian nationalists the rising became the First War of Independence, '
             'and its heroes, like the Rani of Jhansi, inspired the movement that won India its freedom in 1947.',
             'Began at Meerut in May 1857',
             'Ended both the Company and the Mughals',
             'India passed to the British Crown in 1858',
             'Called the First War of Independence in India'),
      states=('British East India Company', 'Oudh', 'British Raj'), war='indian-rebellion-1857', wiki='Indian Rebellion of 1857')

event('american-civil-war', 'The American Civil War', 'civil-war', (1861, 1865),
      'Eleven slave states broke away from the United States. Four years and over 600,000 deaths later, slavery was over.',
      scene('A house divided',
            'By 1860 four million people were enslaved in the southern states, and the country was split over whether '
            'slavery could spread west. When Abraham Lincoln, who opposed its spread, was elected president without a '
            'single southern state, South Carolina left the Union. Ten more slave states followed and formed the '
            'Confederate States of America.',
            kick='How it began', y=1860, at='washington'),
      battle('Fort Sumter',
             'On 12 April 1861 Confederate cannon opened fire on Fort Sumter, a Union fort in Charleston harbour. It '
             'surrendered the next day. Both sides expected a short war, and in July crowds came out from Washington with '
             'picnics to watch the first big battle, at Bull Run. They fled in panic with the beaten Union army.',
             img='Battle of Fort Sumter', y=1861, at='fort_sumter'),
      song('The Battle Hymn of the Republic',
           'Union soldiers marched to a camp song about John Brown, an abolitionist hanged in 1859 for trying to start a '
           'slave revolt. In 1861 Julia Ward Howe heard it on a visit to the army and wrote new words to it that night. '
           'Her Battle Hymn of the Republic, printed in 1862, became the anthem of the Union cause.',
           page='The Battle Hymn of the Republic', hint='Battle Hymn Republic', y=1862, at='washington'),
      figure('abraham-lincoln', 'Emancipation',
             'At first Lincoln fought to save the Union, not to end slavery. But enslaved people fled to the Union lines '
             'by the thousands, and the war changed. On 1 January 1863 his Emancipation Proclamation declared the '
             'enslaved in the rebel states free, and let Black men join the army. By the end some 180,000 had served.',
             y=1863, at='washington'),
      figure('harriet-tubman', 'The Combahee River raid',
             'Harriet Tubman, who had escaped slavery and led others to freedom on the Underground Railroad, served the '
             'Union army as a scout and spy. In June 1863 she guided gunboats up the Combahee River in South Carolina, in '
             'a raid that freed more than 700 enslaved people. No other woman led an armed raid in the war.',
             y=1863, at='combahee'),
      battle('Gettysburg',
             'In July 1863 General Robert E. Lee invaded the North and met the Union army at Gettysburg, Pennsylvania. '
             'In three days some 50,000 men were killed, wounded or missing. Lee\'s last great charge failed and he '
             'retreated. The next day, far away on the Mississippi, the Confederate city of Vicksburg surrendered to '
             'Ulysses Grant.',
             img='Battle of Gettysburg', y=1863, at='gettysburg'),
      work('The Gettysburg Address',
           'In November Lincoln spoke at the new cemetery for the dead of Gettysburg. His speech took about two minutes. '
           'In 272 words he said that the dead had given their lives so that the nation might have a new birth of freedom, '
           'and that government of the people, by the people, for the people, shall not perish from the earth.',
           img='Gettysburg Address', y=1863, at='gettysburg'),
      cost('Total war',
           'In 1864 Grant fought Lee in Virginia week after week, whatever the losses, while General William Sherman '
           'burned Atlanta and marched to the sea at Savannah, wrecking farms and railways to break the South\'s will. '
           'No other war has killed so many Americans.',
           num='Over 600,000', of='soldiers died, two in three of disease', y=1864, at='atlanta'),
      turn('Appomattox',
           'In April 1865 Richmond fell, and Lee surrendered his army to Grant at Appomattox Court House. Grant let the '
           'Confederates keep their horses for the spring ploughing. Five days later Lincoln was shot at a theatre in '
           'Washington by an actor who supported the South, and died the next morning.',
           y=1865, at='appomattox'),
      legacy('The Union was saved and slavery ended: the 13th Amendment abolished it in December 1865, and later '
             'amendments made those who had been enslaved citizens, equal in law. But after a few years the South '
             'brought in segregation and kept most Black people from voting, and the fight for those rights went on for '
             'another century.',
             'Began at Fort Sumter in April 1861',
             'Four million enslaved people were freed',
             'Gettysburg, 1863, was the turning point',
             'Lincoln was killed days after it ended'),
      states=('United States of America',), war='american-civil-war', wiki='American Civil War')

event('italian-unification', 'The unification of Italy', 'unification', (1848, 1871),
      'A prime minister, a king and a red-shirted adventurer turned a patchwork of small states into one Italy.',
      figure('giuseppe-mazzini', 'Young Italy',
             'After Napoleon, Italy was again split into small states, with Austria ruling Lombardy and Venice and the '
             'pope ruling the middle. Giuseppe Mazzini, a revolutionary from Genoa, founded Young Italy in 1831 to make '
             'one free republic of it all. His risings failed again and again, but his idea spread.',
             kick='How it began', y=1831),
      scene('1848',
            'In 1848 Milan threw out the Austrians in five days of street fighting, and Venice and Rome declared '
            'themselves republics. King Charles Albert of Piedmont-Sardinia went to war with Austria and was beaten. In '
            '1849 French troops crushed the Roman Republic, which Garibaldi had defended, and the Austrians came back.',
            img='Five Days of Milan', y=1848, at='milan'),
      figure('camillo-benso-count-of-cavour', 'The schemer',
             'Cavour, prime minister of Piedmont-Sardinia from 1852, built railways, sent troops to the Crimean War to '
             'win friends, and secretly agreed with Napoleon III of France to drive Austria out together. In 1859 they '
             'won bloody battles at Magenta and Solferino, and Piedmont gained Lombardy. Tuscany and its neighbours soon '
             'voted to join.',
             y=1859, at='turin'),
      tale('Solferino and the Red Cross',
           'A Swiss businessman, Henry Dunant, reached Solferino the evening after the battle and found some 40,000 dead '
           'and wounded lying in the heat with hardly any care. He got local women to nurse men of both sides, and later '
           'wrote a book about it. It led to the founding of the Red Cross in 1863 and the first Geneva Convention.',
           img='Battle of Solferino', y=1859, at='solferino'),
      song('Va, pensiero',
           'A chorus from Giuseppe Verdi\'s opera Nabucco of 1842, in which Hebrew slaves long for their lost homeland, '
           'came to stand for Italy\'s own longing. Walls were painted with VIVA VERDI, which also spelled out Viva '
           'Vittorio Emanuele Re D\'Italia: long live Victor Emmanuel, King of Italy.',
           page='Va, pensiero', hint='Va pensiero', y=1859),
      figure('giuseppe-garibaldi', 'The Thousand',
             'In May 1860 Giuseppe Garibaldi, a sailor turned soldier who had fought for freedom in South America, sailed '
             'from near Genoa with about a thousand volunteers in red shirts. They landed at Marsala in Sicily, beat the '
             'much bigger army of the Kingdom of the Two Sicilies, crossed to the mainland and took Naples.',
             img='Expedition of the Thousand', y=1860, at='marsala'),
      turn('The handshake at Teano',
           'Cavour feared Garibaldi would march on Rome and drag France into the war, so Piedmont\'s army marched south '
           'through the pope\'s lands. In October 1860 Garibaldi met King Victor Emmanuel II near Teano, greeted him as '
           'king of Italy and handed over his conquests. Then he went home to his farm on the island of Caprera.',
           y=1860, at='teano'),
      scene('Venice and Rome',
            'The Kingdom of Italy was proclaimed in March 1861, and Cavour died weeks later. Venice was won in 1866, when '
            'Italy sided with Prussia against Austria. Rome, guarded by French troops, came last: when France called them '
            'home to fight Prussia in 1870, Italian soldiers broke through the walls at Porta Pia, and Rome became the '
            'capital. The pope called himself a prisoner in the Vatican.',
            img='Capture of Rome', y=1870, at='rome'),
      legacy('Italy was made in a dozen years, more by war and diplomacy than by the will of its people: most Italians '
             'still spoke their own dialects. As one statesman put it, Italy had been made, and now Italians had to be '
             'made. The gap between the richer north and the poorer south is still felt today.',
             'Garibaldi and the Thousand, 1860',
             'The Kingdom of Italy was proclaimed in 1861',
             'Rome became the capital in 1871',
             'Made by a minister, a king and a rebel'),
      states=('Kingdom of Sardinia', 'Kingdom of the Two Sicilies', 'Papal States', 'Tuscany', 'Lombardy', 'Venetia',
              'Parma', 'Modena', 'Italy'),
      wiki='Italian unification', img='Expedition of the Thousand', at='rome')

event('meiji-restoration', 'The Meiji Restoration', 'change', (1853, 1889),
      'American warships forced Japan open, and in one lifetime it turned itself from a land of samurai into a modern power.',
      figure('matthew-c-perry', 'The black ships',
             'For two centuries Japan had kept nearly all foreigners out. In July 1853 four American warships, two of '
             'them belching smoke from steam engines, sailed into Edo Bay under Commodore Matthew Perry. He handed over a '
             'letter demanding that Japan open its ports, and came back the next year with a bigger fleet. Japan gave in.',
             kick='How it began', y=1853, at='uraga'),
      scene('Revere the emperor',
            'The treaties forced on Japan let foreigners trade and live under their own laws, and many samurai were '
            'furious with the shogun, the military ruler, for giving way. Under the slogan revere the emperor, expel the '
            'barbarians, young samurai from the domains of Satsuma and Chōshū attacked foreigners and plotted against '
            'the shogun.',
            y=1863, at='kyoto'),
      figure('tokugawa-yoshinobu', 'The last shogun',
             'In 1867 the last shogun, Tokugawa Yoshinobu, handed his power back to the emperor, hoping to keep his lands. '
             'Early in 1868 the samurai of Satsuma and Chōshū declared the emperor\'s rule restored and beat the shogun\'s '
             'forces near Kyoto. The emperor was a boy of 15; his reign was named Meiji, enlightened rule.',
             y=1868, at='kyoto'),
      figure('emperor-meiji', 'To Tokyo',
             'The young emperor moved from Kyoto to the shogun\'s city of Edo, renamed Tokyo, the eastern capital. In his '
             'name the new leaders promised to seek knowledge throughout the world. In 1871 they abolished the lords\' '
             'domains, and within a few years the samurai lost their pay and their right to wear swords.',
             y=1868, at='tokyo'),
      scene('Learning from the West',
            'In 1871 nearly half the government set off on a long tour of America and Europe, the Iwakura Mission, to '
            'study everything from schools to shipyards. Japan built railways, telegraphs, factories and an army of '
            'conscripts, took up Western clothes and the Western calendar, and sent every child to school. The first '
            'railway ran from Tokyo to Yokohama in 1872.',
            img='Iwakura Mission', y=1872, at='yokohama'),
      figure('saigo-takamori', 'The last samurai',
             'Saigō Takamori, a giant of a Satsuma samurai, had helped lead the restoration, but he came to hate what the '
             'new Japan was doing to his class. In 1877 thousands of samurai rose with him. They were crushed by the new '
             'army of conscript farmers, and Saigō died at Kagoshima. Japan still loves him as the last true samurai.',
             y=1877, at='kagoshima'),
      turn('A constitution',
           'In 1889 the emperor gave Japan a constitution, modelled on Germany\'s, with an elected parliament but great '
           'powers kept for the throne. It was written by Itō Hirobumi, Japan\'s first prime minister. Within a few years '
           'Japan had beaten China in a war, and in 1905 it would beat Russia.',
           y=1889, at='tokyo'),
      legacy('In a single lifetime Japan went from a closed land of lords and samurai to an industrial power with an empire '
             'of its own, one of the few Asian countries never colonised. Its success inspired reformers across Asia, but '
             'the army and the empire it built led it on to war with China and, in the end, the Second World War.',
             'Perry\'s black ships arrived in 1853',
             'The emperor was restored to power in 1868',
             'The samurai class was abolished in the 1870s',
             'Asia\'s first industrial power'),
      states=('Japan', 'Imperial Japan'), wiki='Meiji Restoration', at='tokyo')

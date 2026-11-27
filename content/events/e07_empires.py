from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('paraguayan-war', 'The Paraguayan War', 'war', (1864, 1870),
      'Little Paraguay fought Brazil, Argentina and Uruguay all at once, and lost a huge share of its people.',
      figure('francisco-solano-lopez', "Paraguay's marshal",
             'Paraguay, a small country deep inland on the rivers of South America, had been closed off for decades by '
             'strong rulers and had built one of the biggest armies on the continent. In 1864, when Brazil sent troops '
             'into Uruguay to back one side in a civil war there, Paraguay\'s leader Francisco Solano López went to war '
             'with Brazil.',
             kick='How it began', y=1864, at='asuncion'),
      turn('Three against one',
           'When Argentina would not let his army cross its land to reach Brazil, López invaded Argentina too. In May '
           '1865 Brazil, Argentina and Uruguay, now under a friendly government, signed the Treaty of the Triple Alliance '
           'and swore to fight on until López was gone. Together they had more than twenty times as many people as '
           'Paraguay.',
           y=1865),
      battle('Tuyutí and Humaitá',
             'In May 1866 the allies invaded Paraguay and threw back a huge Paraguayan attack at Tuyutí, the biggest '
             'battle ever fought in South America. Then they were stuck for two years in the swamps before the river '
             'fortress of Humaitá, losing men to cholera and to bloody failed assaults.',
             y=1866),
      figure('pedro-ii-of-brazil', "The emperor's war",
             'Brazil bore most of the fighting. Its emperor, Pedro II, a scholarly man who loved science, refused any '
             'peace while López ruled, and Brazil freed many enslaved men to fight in its armies. In January 1869 the '
             'allies took Asunción, Paraguay\'s capital, and Brazilian troops occupied it.',
             y=1869, at='asuncion'),
      cost('The children of Acosta Ñu',
           'López fought on in the hills with an army of old men and boys. At Acosta Ñu in August 1869 thousands of '
           'children, some with beards painted on to look older, fought Brazilian troops, and Paraguay still keeps its '
           'Children\'s Day on that date. By the end, women far outnumbered men, and it was women who rebuilt the country.',
           num='Up to half', of="of Paraguay's people died, by many estimates", y=1869),
      turn('Cerro Corá',
           'On 1 March 1870 Brazilian cavalry caught López at Cerro Corá in the northern hills. Refusing to surrender, '
           'he was killed beside a stream, crying out, it is said, that he died with his country. Paraguay lost land to '
           'Brazil and Argentina and stayed occupied for six years.',
           y=1870, at='cerro_cora'),
      figure(None, 'Madame Lynch',
             'Eliza Lynch, an Irish woman López had met in Paris, ruled Paraguay\'s society at his side and followed his '
             'army to the end; she buried him and their son, it is said, with her own hands. Blamed for decades for the '
             'disaster, she is honoured in Paraguay today as a heroine.',
             img='Eliza Lynch', y=1870, at='cerro_cora'),
      legacy('It was the deadliest war in the history of South America. Paraguay, once one of the continent\'s most '
             'self-reliant states, was left in ruins and took generations to recover. In Brazil the war made the army '
             'powerful, and helped bring the end of slavery in 1888 and of the empire in 1889.',
             'Paraguay fought three neighbours, 1864 to 1870',
             'The deadliest war in South American history',
             'López died at Cerro Corá in 1870'),
      states=('Kingdom of Brazil', 'Argentina', 'Uruguay'), war='paraguayan-war', wiki='Paraguayan War')

event('german-unification', 'The unification of Germany', 'unification', (1864, 1871),
      "In three short wars Prussia's Bismarck united Germany by blood and iron, and crowned its king emperor in France.",
      figure('otto-von-bismarck', 'Blood and iron',
             'In 1862 King Wilhelm I of Prussia made Otto von Bismarck his chief minister. In his first big speech '
             'Bismarck said that the great questions of the day would be settled not by speeches and majority votes, the '
             'mistake of 1848, but by iron and blood. He meant to unite Germany under Prussia, and to push Austria out.',
             kick='How it began', y=1862, at='berlin'),
      battle('Denmark',
             'First, in 1864, Prussia and Austria together took the duchies of Schleswig and Holstein from Denmark. The '
             'British statesman Palmerston joked that only three people had ever understood the Schleswig-Holstein '
             'question: one was dead, one had gone mad, and he himself had forgotten it.',
             y=1864, at='dybbol'),
      battle('Königgrätz',
             'Two years later Bismarck picked a quarrel with Austria over the duchies. Prussia\'s railways rushed its '
             'armies to the front, and its soldiers\' breech-loading needle guns fired far faster than the Austrians\' '
             'rifles. At Königgrätz in Bohemia in July 1866 Austria was crushed in a day. The whole war took seven weeks.',
             img='Battle of Königgrätz', y=1866, at='koniggratz'),
      scene('A union of the north',
            'Prussia swallowed Hanover and the other northern states that had sided with Austria, and bound the rest of '
            'the north into a new union under its king. Austria was shut out of Germany for good. Only the Catholic '
            'south, Bavaria, Württemberg and Baden, stayed apart.',
            y=1867),
      turn('The Ems telegram',
           'In 1870 France protested at a German prince being offered the throne of Spain. The French ambassador met '
           'King Wilhelm at the spa town of Ems and asked him to promise it would never happen again. Bismarck cut the '
           'king\'s telegram about the meeting so that it read like a snub, and gave it to the press. France, as he had '
           'hoped, declared war.',
           y=1870, at='bad_ems'),
      battle('Sedan',
             'The southern states joined Prussia, and the German armies, faster and better led, poured into France. On 2 '
             'September 1870, at Sedan, a French army of over 100,000 men surrendered, and with it Emperor Napoleon III '
             'himself. Paris declared a republic and was besieged all winter.',
             img='Battle of Sedan', y=1870, at='sedan'),
      tale('Balloons and elephants',
           'During the siege of Paris, balloons floated letters and people out over the German lines, and pigeons flew '
           'the answers back. As food ran out, Parisians ate horses, cats and rats, and even the two elephants of the '
           'zoo, Castor and Pollux.',
           img='Siege of Paris (1870–1871)', y=1870, at='paris'),
      turn('An emperor at Versailles',
           'On 18 January 1871, in the Hall of Mirrors at Versailles, the palace of the French kings, the German princes '
           'proclaimed Wilhelm German Emperor. France had to pay a huge sum and give up Alsace and much of Lorraine, a '
           'loss it never forgot.',
           img='Proclamation of the German Empire', y=1871, at='versailles'),
      legacy('The new German Empire, with its industry, science and army, was soon the strongest power in Europe. But it '
             'was born in war, and France\'s longing to win back its lost provinces, and the fear Germany\'s strength '
             'stirred in its neighbours, helped lead to the First World War.',
             'Three wars: Denmark 1864, Austria 1866, France 1870',
             'Bismarck united Germany by blood and iron',
             'The empire was proclaimed at Versailles in 1871'),
      states=('Germany',), war='wars-of-german-unification', wiki='Unification of Germany')

event('suez-canal', 'The Suez Canal', 'building', (1859, 1869),
      'A French diplomat and tens of thousands of Egyptian labourers cut a waterway joining the Mediterranean to the Red Sea.',
      scene('An old dream',
            'Pharaohs had dug canals from the Nile to the Red Sea, but ships sailing from Europe to Asia still had to go '
            'all the way around Africa. In 1854 the French diplomat Ferdinand de Lesseps won leave from his friend Said '
            'Pasha, the ruler of Egypt, to dig a canal straight across the desert isthmus of Suez.',
            kick='How it began', y=1854, at='suez'),
      figure('ferdinand-de-lesseps', 'The salesman',
             'Lesseps was no engineer, but he was a brilliant salesman. Britain, afraid of French power on the road to '
             'India, fought the plan, so he sold shares to thousands of ordinary French savers, and Egypt bought most of '
             'the rest. Work began in April 1859 on the beach where Port Said now stands.',
             y=1859, at='port_said'),
      cost('Forced labour',
           'For years most of the digging was done by Egyptian peasants forced to work in the heat with picks and '
           'baskets, and many died of disease. After protests in Europe the forced labour was stopped in 1864, and huge '
           'steam dredgers took over.',
           num='20,000', of='peasants made to dig at any one time', y=1862),
      turn('The opening',
           'The canal opened in November 1869 with fireworks, balls and a procession of ships led by the French empress '
           'Eugénie in her yacht. Egypt\'s ruler, Ismail, spent a fortune on the party and built an opera house in Cairo, '
           'for which Verdi wrote Aida, his opera of ancient Egypt, first sung there in 1871.',
           img='Opening of the Suez Canal', y=1869, at='ismailia'),
      made('A shortcut for the world',
           'A channel at sea level, 164 kilometres long and with no locks, joining the Mediterranean to the Red Sea.',
           'The voyage from London to Bombay was cut by about two fifths. Steamships took over from sailing ships, and '
           'trade between Europe and Asia boomed.',
           y=1869, at='suez'),
      turn('Britain buys in',
           'Ismail ran up huge debts, and in 1875 he had to sell Egypt\'s shares. The British prime minister, Benjamin '
           'Disraeli, bought them within days with a loan from the Rothschild bank. In 1882 Britain invaded Egypt, and '
           'its troops stayed for more than 70 years to guard the canal and the road to India.',
           y=1875),
      figure('gamal-abdel-nasser', 'The Suez Crisis',
             'In 1956 Egypt\'s president, Gamal Abdel Nasser, took the canal into Egyptian hands. Britain, France and '
             'Israel invaded, but the United States and the Soviet Union forced them to pull out. It was a sign that the '
             'age of the European empires was over.',
             y=1956, at='port_said'),
      legacy('The Suez Canal remade the map of world trade. Today about a tenth of the world\'s seaborne trade passes '
             'through it, and when a giant container ship stuck fast across it for six days in 2021, supply chains around '
             'the world felt it.',
             'Begun in 1859, opened in 1869',
             'Egyptian labour and French money built it',
             'It cut the sea road from Europe to Asia by two fifths'),
      states=('Egypt', 'France'), wiki='Suez Canal', at='ismailia')

event('paris-commune', 'The Paris Commune', 'uprising', (1871, 1871),
      'For 72 days in 1871 the working people of Paris ran their own city, until the French army took it back.',
      scene('A city betrayed',
            'Paris had held out through a winter siege by the Germans, only to see France\'s new government make a '
            'humiliating peace. Its working people, armed as the National Guard, distrusted the conservative assembly. '
            'When troops came on 18 March 1871 to take the Guard\'s cannons from Montmartre, crowds stopped them, and two '
            'generals were shot.',
            kick='How it began', y=1871, at='paris'),
      turn('The Commune',
           'The government fled to Versailles, and Paris elected its own council, the Commune. In its 72 days it '
           'separated church and state, banned night work in bakeries, let workers take over workshops their owners had '
           'left, and pulled down the column in the Place Vendôme as a symbol of war and empire.',
           img='Paris Commune', y=1871, at='paris'),
      figure(None, 'Louise Michel',
             'Louise Michel, a schoolteacher and poet, fought on the barricades with a rifle and ran a first aid post. At '
             'her trial she dared the judges to kill her. She was sent to the Pacific island of New Caledonia, where she '
             'taught the Kanak people and took their side, and came home a hero of the left.',
             img='Louise Michel', y=1871, at='paris'),
      cost('The Bloody Week',
           'On 21 May the army broke into Paris. In the Bloody Week that followed, Communards fought from barricades, '
           'burned the Tuileries Palace and the city hall and shot hostages, the archbishop among them. The army shot '
           'prisoners by the thousand; the last were lined up against a wall in Père Lachaise cemetery.',
           num='6,000 to 20,000', of='Communards killed, by different counts', y=1871, at='paris'),
      song('The Internationale',
           'Eugène Pottier, a Communard in hiding after the Bloody Week, wrote a poem calling on the wretched of the '
           'earth to rise. Set to music in 1888, The Internationale became the anthem of socialists and communists '
           'around the world, and was the Soviet Union\'s national anthem until 1944.',
           page='The Internationale', hint='Internationale', y=1871),
      legacy('The Commune was crushed, but it became a legend. Marx called it the first government of the working class, '
             'and Lenin, it is said, danced in the snow when his own revolution outlasted it. In France it is still '
             'argued over, and the wall in Père Lachaise is a place of pilgrimage.',
             'Paris ruled itself for 72 days in 1871',
             'Crushed in the Bloody Week of May',
             'It gave the world The Internationale'),
      states=('France',), wiki='Paris Commune', at='paris')

event('scramble-for-africa', 'The Scramble for Africa', 'conquest', (1881, 1914),
      'In thirty years European powers carved up almost all of Africa. Only Ethiopia and Liberia stayed free.',
      scene('Into the interior',
            'In 1870 Europeans held only bits of Africa\'s coasts. Then quinine against malaria, steamboats and the '
            'rapid-firing machine gun made it possible to push inland, and rivalry among the powers made it urgent. '
            'Explorers like Henry Morton Stanley, who found the missing David Livingstone in 1871, showed the way.',
            kick='How it began', y=1871),
      battle('Isandlwana',
             'In January 1879 a British army invaded the Zulu kingdom of Cetshwayo. At Isandlwana some 20,000 Zulu '
             'warriors, armed mostly with spears and shields, overran a British camp and killed more than 1,300 men, one '
             'of the worst defeats a colonial army ever suffered. Britain sent more troops, and by July the kingdom was '
             'broken.',
             img='Battle of Isandlwana', y=1879, at='isandlwana'),
      turn('The Berlin Conference',
           'In 1884 Bismarck invited the powers to Berlin to agree on rules for claiming Africa. Not one African was '
           'invited. The conference recognised the vast Congo as the private property of King Leopold II of Belgium, and '
           'agreed that a power could claim land if it really occupied it. The race to grab land speeded up.',
           img='Berlin Conference', y=1884, at='berlin'),
      cost("King Leopold's rubber",
           'Leopold ran the Congo as his own business. His agents forced villagers to gather wild rubber, holding wives '
           'hostage and cutting off hands when the quotas were not met. After a campaign by the reformer E. D. Morel and '
           'others, Belgium took the colony away from its king in 1908.',
           num='Millions', of="died in King Leopold's Congo", img='Congo Free State', y=1895),
      battle('Adwa',
             'In 1896 Italy invaded Ethiopia. Emperor Menelik II, who had bought modern rifles and cannon, gathered an '
             'army of about 100,000 and, with Empress Taytu, met the Italians at Adwa. In one day the Italian army was '
             'destroyed. Italy had to recognise Ethiopia\'s independence, and Adwa became a symbol of pride for Black '
             'people everywhere.',
             img='Battle of Adwa', y=1896, at='adwa'),
      figure('samori-ture', 'Samori Ture',
             'Many Africans fought back. In West Africa Samori Ture built an empire with an army of riflemen, its guns '
             'copied and mended in his own workshops, and fought the French for 16 years, moving his whole state east '
             'when he had to. He was captured in 1898 and died in exile.',
             y=1898),
      figure('yaa-asantewaa', 'The Golden Stool',
             'In 1900 the British governor of the Gold Coast demanded to sit on the Golden Stool, the sacred throne that '
             'held the soul of the Asante nation, which no one ever sat on. Yaa Asantewaa, queen mother of Ejisu, shamed '
             'the men by vowing that the women would fight if they would not, and led a rising that besieged the British '
             'fort in Kumasi.',
             y=1900, at='kumasi'),
      scene('The map of 1914',
            'By 1914 only Ethiopia and Liberia were free. France held most of the northwest, Britain a chain of colonies '
            'from Egypt to the Cape, and Germany, Belgium, Portugal, Italy and Spain the rest. The new borders, ruled on '
            'maps in Europe, cut across hundreds of peoples and kingdoms.',
            img='Scramble for Africa', y=1914),
      legacy('Colonial rule brought railways, mines, schools and missions, but it was built on force and run for the '
             'rulers\' profit, and it shaped Africa\'s borders, languages and trade to this day. Most African countries won '
             'back their freedom from the late 1950s to the 1970s, inside the borders that the scramble drew.',
             'A tenth of Africa was European in 1870, nine tenths by 1914',
             'The rules were made in Berlin in 1884, with no Africans there',
             'Ethiopia beat Italy at Adwa in 1896'),
      states=('France', 'Germany', 'Belgium', 'Italy', 'Portugal', 'United Kingdom of Great Britain and Ireland',
              'Congo', 'Belgian Congo', 'Ethiopia', 'Abyssinia', 'Zululand', 'Asante', 'Gold Coast (GB)', 'Gold Coast',
              'Wassoulou Empire', 'First Samori Empire', 'Second Samori Empire', 'Sokoto Caliphate', 'Dahomey', 'Benin',
              'Madagascar', 'Madagascar (France)', 'Morocco', 'Egypt', 'Buganda', 'Liberia', 'French West Africa',
              'French Equatorial Africa', 'German South-West Africa', 'Kamerun', 'Togoland', 'Nigeria',
              'British East Africa', 'Uganda', 'Rhodesia', 'Eritrea', 'Italian Somaliland', 'British Somaliland',
              'Anglo-Egyptian Sudan', 'Libya', 'Angola', 'Mozambique'),
      wiki='Scramble for Africa', img='Battle of Adwa', at=(20.0, 2.0), where='Africa')

event('krakatoa', 'The eruption of Krakatoa', 'disaster', (1883, 1883),
      'A volcanic island between Java and Sumatra blew itself apart with the loudest sound in recorded history.',
      scene('A mountain wakes',
            'Krakatoa was a green volcanic island in the Sunda Strait, between Java and Sumatra in the Dutch East '
            'Indies. In May 1883 it began to rumble and throw out ash. Passing ships and people on the coasts watched it '
            'all summer, more curious than afraid; one steamer even took sightseers out to look.',
            kick='How it began', y=1883, at='krakatoa'),
      turn('27 August',
           'On the morning of 27 August four huge explosions tore the island apart, and two thirds of it vanished. The '
           'last was heard nearly 5,000 kilometres away, on the island of Rodrigues near Mauritius, like the roar of '
           'distant guns. It was probably the loudest sound in recorded history.',
           img='1883 eruption of Krakatoa', y=1883, at='krakatoa'),
      cost('The waves',
           'The explosions and the collapse of the island raised waves up to 30 metres high that smashed into the coasts '
           'of Java and Sumatra and swept away 165 towns and villages. A Dutch gunboat was carried far inland and left in '
           'the forest.',
           num='Over 36,000', of='people died, most of them drowned', y=1883, at='krakatoa'),
      made('News by wire',
           'An undersea telegraph cable linked Java to the world, and the news reached newspapers in Europe and America '
           'within hours.',
           'It was one of the first disasters the whole world followed almost as it happened, and reports sent in from '
           'everywhere gave scientists their first picture of how one volcano can touch the whole planet.',
           y=1883),
      scene('Red skies',
            'Ash and gas thrown high into the sky circled the globe. For months sunsets glowed blood red as far away as '
            'Europe and America; near New York fire engines were called out to what looked like a great fire on the '
            'horizon. The world was a little cooler for several years.',
            y=1884),
      work('The Scream',
           'Some scientists think the blood-red sky in Edvard Munch\'s painting The Scream, of 1893, remembers the '
           'Krakatoa sunsets he saw in Norway as a young man. Munch wrote of a walk at sunset when the sky suddenly '
           'turned red as blood. Others say the colours came from his mind, not the sky.',
           img='The Scream', y=1893),
      scene('Child of Krakatoa',
            'In 1927 a new volcano rose out of the sea where Krakatoa had stood. Named Anak Krakatau, the child of '
            'Krakatoa, it has kept growing and erupting, and in 2018 part of it slid into the sea and raised a tsunami '
            'that killed more than 400 people.',
            img='Anak Krakatoa', y=2018, at='krakatoa'),
      legacy('Krakatoa was not the biggest eruption of its century, Tambora in 1815 was bigger, but it was the first to be '
             'studied around the world, and it showed how a single volcano could darken skies and cool the planet. It is '
             'still the name people think of for a volcano that explodes.',
             'Erupted on 27 August 1883',
             'Heard nearly 5,000 kilometres away',
             'Its waves killed more than 36,000 people'),
      states=('Netherlands Indies',), wiki='1883 eruption of Krakatoa', at='krakatoa')

event('boxer-rebellion', 'The Boxer Rebellion', 'uprising', (1899, 1901),
      'Villagers who thought bullets could not harm them rose against foreigners in China, and eight nations marched in.',
      scene('The Boxers',
            'By 1899 foreign powers had carved China into spheres of influence, and missionaries, railways and foreign '
            'goods angered many in the north, where floods and drought had brought hunger. A secret society that '
            'foreigners called the Boxers, for their martial arts, spread through Shandong, killing missionaries and '
            'Chinese Christians. Its members believed their rituals made them proof against bullets.',
            kick='How it began', y=1899),
      figure('empress-dowager-cixi', 'The empress dowager',
             'Empress Dowager Cixi, who had ruled China from behind the throne for nearly 40 years, at first wavered. In '
             'June 1900, as Boxers poured into Beijing and foreign troops seized the forts guarding the sea road to it, '
             'she sided with the Boxers and declared war on all the foreign powers at once.',
             y=1900, at='beijing'),
      scene('The siege of the legations',
            'For 55 days some 900 foreigners and about 3,000 Chinese Christians held out in the legation quarter of '
            'Beijing, where the foreign embassies stood, behind barricades of sandbags and furniture. The German envoy '
            'was shot dead in the street. Boxers and imperial troops attacked again and again, but never with their full '
            'strength.',
            img='Siege of the International Legations', y=1900, at='beijing'),
      cost('Killing and revenge',
           'In the northern countryside Boxers killed tens of thousands of Chinese Christians, and some 200 foreign '
           'missionaries and their children. When the foreign armies came, they took a terrible revenge, burning '
           'villages and killing far more Chinese, Boxers or not.',
           num='Over 30,000', of='Chinese Christians killed by the Boxers', y=1900),
      battle('Eight nations',
             'An army of eight nations, Japan, Russia, Britain, France, the United States, Germany, Italy and '
             'Austria-Hungary, fought its way from Tianjin and broke into Beijing on 14 August, ending the siege. Cixi '
             'fled the city dressed as a peasant woman, and foreign soldiers looted the capital for weeks.',
             img='Eight-Nation Alliance', y=1900, at='tianjin'),
      turn('The price',
           'In 1901 China signed the Boxer Protocol. It had to execute officials who had backed the Boxers, let foreign '
           'troops guard the embassies and pay 450 million ounces of silver over 39 years. The United States later used '
           'part of its share to send Chinese students to America and to found Tsinghua University in Beijing.',
           y=1901, at='beijing'),
      legacy('The rising was a disaster for the Qing. Humbled again, the court at last tried real reforms, ending the old '
             'exams in 1905, but too late: the dynasty fell ten years after the protocol. Chinese remember the Boxers both '
             'as a cruel, backward rising and as a cry of resistance to foreign bullying.',
             'Began among villagers in Shandong, 1899',
             'The siege of the legations lasted 55 days',
             'Eight nations took Beijing in August 1900'),
      war='boxer-rebellion', wiki='Boxer Rebellion')

event('second-boer-war', 'The Boer War', 'war', (1899, 1902),
      'Britain fought two Boer republics over gold and power, and won only by burning farms and filling camps.',
      scene('Gold',
            'The Boers, Dutch-speaking farmers whose families had trekked inland to escape British rule, had two '
            'republics, the Transvaal and the Orange Free State. In 1886 the richest gold field on earth was found in '
            'the Transvaal, and the city of Johannesburg sprang up. Thousands of foreign miners poured in, and Britain '
            'wanted control.',
            kick='How it began', y=1886, at='johannesburg'),
      figure('paul-kruger', 'Oom Paul',
             'Paul Kruger, the Transvaal\'s stern old president, who had gone on the Great Trek as a boy, refused to give '
             'the foreign miners the vote, fearing they would swamp his people. After a failed British-backed raid in '
             '1895 and years of pressure, he struck first in October 1899, and the Boers invaded the British colonies.',
             y=1899, at='pretoria'),
      battle('Black Week',
             'The Boers were tough horsemen and fine shots with modern German rifles. In one week of December 1899 they '
             'beat three British armies, and they besieged the towns of Ladysmith, Kimberley and Mafeking. At Mafeking '
             'Colonel Robert Baden-Powell held out for 217 days, and later founded the Scouts.',
             y=1899, at='mafeking'),
      figure('winston-churchill', 'The escape',
             'A young war reporter, Winston Churchill, was captured when the Boers ambushed an armoured train in Natal. '
             'He climbed over the wall of his prison in Pretoria, hid down a coal mine, and escaped to Portuguese East '
             'Africa on a goods train, buried among bales of wool. He came home famous.',
             y=1899, at='pretoria'),
      figure('mahatma-gandhi', 'Stretcher-bearers',
             'A young Indian lawyer in Natal, Mohandas Gandhi, believing that Indians should show they were loyal '
             'citizens of the empire, organised more than a thousand Indians as stretcher-bearers. They carried wounded '
             'British soldiers from the battlefields, sometimes under fire.',
             y=1900, at='ladysmith'),
      scene('Farm burning',
            'Britain sent nearly half a million soldiers from across its empire and took the Boer capitals in 1900. But '
            'the Boers fought on as guerrillas, in small bands on horseback. To starve them out, the British commander, '
            'Lord Kitchener, burned some 30,000 farms and herded the women, children and Black farm workers into camps.',
            y=1901),
      cost('The camps',
           'In the concentration camps, crowded tents with bad food and dirty water, disease swept through. Over 26,000 '
           'Boer women and children died, and many thousands of the Black Africans held in separate camps. A British '
           'woman, Emily Hobhouse, exposed the conditions and shamed the government into changes.',
           num='Over 26,000', of='Boer women and children died in camps', img='Second Boer War concentration camps',
           y=1901),
      turn('Peace at Vereeniging',
           'The Boers finally gave in in May 1902. Their republics became British colonies, but were soon given back '
           'self-rule, and in 1910 they joined the Cape and Natal in the Union of South Africa. The peace left the Black '
           'majority, who had served and suffered on both sides, without any say.',
           y=1902, at='vereeniging'),
      legacy('It was Britain\'s biggest and costliest war since Napoleon, and it shook its faith in its empire. For '
             'Afrikaners the camps left a bitterness that fed their nationalism, and the white rule they built in the new '
             'South Africa led in time to apartheid.',
             'Fought from 1899 to 1902',
             'Britain sent nearly half a million soldiers',
             'Tens of thousands died in the camps'),
      states=('South Africa', 'United Kingdom of Great Britain and Ireland'), war='second-boer-war',
      wiki='Second Boer War')

event('russo-japanese-war', 'The Russo-Japanese War', 'war', (1904, 1905),
      'Japan beat the Russian Empire on land and sea, the first time in modern times that an Asian power beat a European one.',
      scene('Korea and Manchuria',
            'Russia and Japan both wanted Korea and Manchuria. Russia had built a railway across Siberia and leased the '
            'ice-free harbour of Port Arthur from China. When talks failed, in February 1904, Japan attacked the Russian '
            'fleet at Port Arthur by night, before it declared war.',
            kick='How it began', y=1904, at='port_arthur'),
      battle('Port Arthur',
             'Japanese armies besieged Port Arthur for five months, charging uphill into machine guns and barbed wire, a '
             'foretaste of the First World War. Tens of thousands were killed or wounded before the fortress surrendered '
             'on 2 January 1905.',
             img='Siege of Port Arthur', y=1904, at='port_arthur'),
      battle('Mukden',
             'In March 1905 the Japanese beat the main Russian army at Mukden in Manchuria, in one of the biggest battles '
             'the world had yet seen, with over half a million men. Both sides were exhausted.',
             img='Battle of Mukden', y=1905, at='mukden'),
      scene('The long voyage',
            'Russia sent its Baltic Fleet halfway around the world to save the war. On the way, jumpy officers fired on '
            'British fishing boats in the North Sea, taking them for Japanese torpedo boats. Its biggest ships sailed '
            'around Africa, and the fleet took seven months to reach Asia.',
            y=1905),
      battle('Tsushima',
             'On 27 May 1905, in the Tsushima Strait between Korea and Japan, Admiral Tōgō Heihachirō\'s fleet crossed in '
             'front of the Russian line and destroyed it. In two days 21 Russian ships were sunk and most of the rest '
             'taken; Japan lost three torpedo boats. It was one of the most complete victories in naval history.',
             img='Battle of Tsushima', y=1905, at='tsushima'),
      scene('Revolution in Russia',
            'At home Russia was in uproar. In January 1905 troops in St Petersburg fired on a peaceful crowd of workers '
            'carrying icons and a petition to the tsar, killing hundreds on Bloody Sunday. Strikes, mutinies like that on '
            'the battleship Potemkin and peasant risings forced Nicholas II to grant a parliament.',
            img='Bloody Sunday (1905)', y=1905, at='st_petersburg'),
      figure('theodore-roosevelt', 'Peace in New Hampshire',
             'Both empires were nearly broke. President Theodore Roosevelt brought them to talks at Portsmouth, New '
             'Hampshire, where in September 1905 Russia gave Japan Port Arthur, half the island of Sakhalin and a free '
             'hand in Korea. Roosevelt won the Nobel Peace Prize for it, the first American to win a Nobel Prize.',
             y=1905, at='portsmouth_nh'),
      legacy('Japan\'s victory astonished the world. It made Japan a great power, which took Korea as a colony in 1910, '
             'and it inspired people from India to Egypt, who saw that Europeans could be beaten. In Russia, defeat and '
             'the revolution of 1905 were a rehearsal for the revolution of 1917.',
             'Japan struck at Port Arthur in February 1904',
             'Tsushima, May 1905: the Russian fleet destroyed',
             'The first modern defeat of a European power by an Asian one'),
      states=('Manchu Empire',), war='russo-japanese-war', wiki='Russo-Japanese War')

event('panama-canal', 'The Panama Canal', 'building', (1881, 1914),
      'France failed, and the United States succeeded, in cutting a canal through the jungle from the Atlantic to the Pacific.',
      figure('ferdinand-de-lesseps', 'The French try',
             'Fresh from building the Suez Canal, Ferdinand de Lesseps began digging across Panama, then part of '
             'Colombia, in 1881. He wanted a canal at sea level, as at Suez. But Panama had mountains, floods and jungle, '
             'and in 1889 his company went bankrupt, ruining thousands of French savers.',
             kick='How it began', y=1881),
      cost('Fever',
           'Most of the workers came from the Caribbean, many from Jamaica, and yellow fever and malaria killed them in '
           'their thousands. No one yet knew that mosquitoes carried them; hospital beds even stood in bowls of water to '
           'keep off ants, which bred more mosquitoes.',
           num='About 22,000', of='died in the French years, by one estimate', y=1885),
      figure('theodore-roosevelt', 'I took the Isthmus',
             'The United States wanted the canal for its navy and its trade. When Colombia refused its terms in 1903, '
             'President Theodore Roosevelt backed a revolt in Panama and sent warships to stop Colombian troops landing. '
             'Panama declared itself independent and within weeks gave the United States a strip of land across it.',
             y=1903, at='panama'),
      made('Beating the mosquito',
           'The army doctor William Gorgas, who had seen in Cuba that mosquitoes spread yellow fever, drained swamps, '
           'screened windows, spread oil on standing water and fumigated houses.',
           'Yellow fever was gone from Panama by 1906 and malaria sharply cut. Without that the canal could not have '
           'been built, and the same methods saved lives across the tropics.',
           y=1905, at='panama'),
      scene('Locks and a lake',
            'The American engineers gave up on a canal at sea level. They dammed the Chagres River to make Gatún Lake, '
            'then the biggest artificial lake in the world, and built giant locks to lift ships 26 metres up to it and '
            'down again on the far side.',
            img='Panama Canal locks', y=1907),
      scene('The Culebra Cut',
            'The hardest part was cutting through the mountains at Culebra. Tens of thousands of workers, most from '
            'Barbados and other Caribbean islands, blasted rock and loaded it onto trains, while landslides kept '
            'burying their work. Black workers were paid in silver and white Americans in gold, and they lived apart.',
            img='Culebra Cut', y=1910, at='culebra_cut'),
      turn('Opened',
           'The first ship passed through on 15 August 1914, but the First World War had just begun, and few noticed. '
           'The voyage from New York to San Francisco was cut by about 13,000 kilometres. Some 5,600 workers had died '
           'in the American years.',
           y=1914, at='culebra_cut'),
      legacy('The canal made the United States a power in two oceans and became one of the busiest trade routes on '
             'earth. Panamanians resented the American zone that cut their country in two, and after years of protest '
             'the United States handed the canal to Panama on the last day of 1999.',
             'The French tried and failed, 1881 to 1889',
             'The mosquito was beaten before the digging',
             'Opened in August 1914',
             'Handed over to Panama in 1999'),
      states=('Panama', 'Colombia', 'United States of America', 'France'), wiki='Panama Canal', at='culebra_cut')

event('titanic', 'The sinking of the Titanic', 'disaster', (1912, 1912),
      'The biggest ship in the world, said to be unsinkable, struck an iceberg on her first voyage, and 1,500 people died.',
      scene('The biggest ship afloat',
            'RMS Titanic, built in Belfast for the White Star Line, was the largest ship in the world, 269 metres long, '
            'with a gym, a swimming pool and a grand staircase under a glass dome. Her hull was split into compartments '
            'that could be sealed off, and people called her unsinkable. She carried lifeboats for only about half of '
            'those on board.',
            kick='How it began', y=1912, at='belfast'),
      scene('Maiden voyage',
            'On 10 April 1912 she sailed from Southampton for New York with some 2,200 people aboard, from millionaires '
            'like John Jacob Astor to emigrants in third class from Ireland, Scandinavia and Lebanon, hoping for a new '
            'life in America.',
            y=1912, at='southampton'),
      turn('The iceberg',
           'Other ships had radioed warnings of ice, but the Titanic kept up her speed through a calm, moonless night. '
           'At 11:40 pm on 14 April a lookout saw an iceberg dead ahead. The ship swung but scraped along it, and the sea '
           'poured into her front compartments. Her designer, on board, told the captain she would sink within hours.',
           y=1912, at='titanic_wreck', where='Where the Titanic sank'),
      scene('Women and children first',
            'The crew loaded the lifeboats, women and children first, but many left half empty because people would not '
            'believe the ship could sink. The band played on deck to keep everyone calm. At 2:20 am the Titanic broke in '
            'two and went down, leaving hundreds in the freezing water.',
            y=1912, at='titanic_wreck', where='Where the Titanic sank'),
      cost('Lost',
           'The liner Carpathia, racing through the ice, picked up the survivors at dawn. More than half of the '
           'first-class passengers lived, but only a quarter of those in third class, many trapped in the maze of '
           'corridors below. Most of the crew died, among them the captain, the designer and the whole band.',
           num='About 1,500', of='people died; about 700 survived', y=1912),
      made('New rules',
           'The first international treaty for the safety of life at sea, agreed in London in 1914.',
           'Ships had to carry lifeboats for everyone on board and keep a radio watch day and night, and an '
           'International Ice Patrol began watching for icebergs in the North Atlantic. It still does.',
           y=1914, at='london'),
      scene('Found',
            'In 1985 a team led by the ocean explorer Robert Ballard found the wreck almost four kilometres down, lying '
            'in two pieces on the sea floor. Expeditions have filmed it many times since, and its story has been told in '
            'books, songs and films.',
            img='Wreck of the Titanic', y=1985, at='titanic_wreck', where='The wreck of the Titanic'),
      legacy('The Titanic became a lasting symbol of human pride humbled by nature, and of a society split by class even '
             'at the moment of death. Its loss brought in the first international rules for safety at sea.',
             'Sank on her first voyage, 15 April 1912',
             'Lifeboats for only half of those aboard',
             'About 1,500 died'),
      states=('United Kingdom of Great Britain and Ireland', 'United States of America'), wiki='Titanic',
      at='titanic_wreck', where='Where the Titanic sank')

event('mexican-revolution', 'The Mexican Revolution', 'revolution', (1910, 1920),
      "A rigged election set off ten years of war that brought down a dictator and gave land back to Mexico's farmers.",
      figure('porfirio-diaz', 'Don Porfirio',
             'Porfirio Díaz had ruled Mexico for over 30 years. He brought in railways and foreign money, but most of '
             'the land belonged to a few great estates, worked by millions of farmers trapped in debt and poverty. In '
             '1910, at 80, he had himself re-elected yet again, after jailing his rival.',
             kick='How it began', y=1910, at='mexico_city'),
      figure('francisco-madero', 'The apostle of democracy',
             'The rival, Francisco Madero, a rich landowner\'s son who believed in fair elections, escaped to Texas and '
             'called for a rising on 20 November 1910. Rebels rose across the country, and in May 1911 Díaz sailed into '
             'exile. Madero was elected president, but in 1913 his own general, Victoriano Huerta, overthrew him and had '
             'him shot.',
             y=1911),
      figure('emiliano-zapata', 'Land and liberty',
             'In the south Emiliano Zapata, a horse trainer from Morelos, led farmers to take back the land that sugar '
             'estates had taken from their villages. His Plan of Ayala demanded that the land go to those who worked it. '
             'His cry was land and liberty, and he fought every government that would not give it.',
             y=1911),
      figure('pancho-villa', 'The Centaur of the North',
             'In the north Pancho Villa, a former bandit, led the Division of the North with cavalry, trains and even a '
             'deal with an American film company to film his battles. In 1914 the armies of Villa and Zapata drove out '
             'Huerta and met in Mexico City, where they posed for photographs in the president\'s palace.',
             y=1914, at='mexico_city'),
      cost('A million dead',
           'Then the winners fought each other. Battles, executions, hunger and in the end the flu killed perhaps a '
           'million Mexicans, and hundreds of thousands more fled north. Women soldiers, the soldaderas, cooked, nursed '
           'and fought beside the men.',
           num='About a million', of='Mexicans died, of war, hunger and disease', y=1915),
      tale('Villa raids America',
           'When the United States backed his rival, Villa raided the town of Columbus, New Mexico, in March 1916, '
           'killing 18 Americans. General John Pershing chased him through northern Mexico for almost a year with '
           'thousands of soldiers, aeroplanes and trucks, and never caught him.',
           y=1916, at='columbus_nm'),
      turn('The Constitution of 1917',
           'In 1917 the winning side, led by Venustiano Carranza, wrote a new constitution at Querétaro. It promised '
           'land reform, free schooling, an eight-hour working day and the right to strike, and it put the nation\'s oil '
           'and minerals in its own hands. It is still Mexico\'s constitution today.',
           y=1917, at='queretaro'),
      scene('Gunned down',
            'Peace came hard. Zapata was lured into a trap and shot in 1919, Carranza was killed in 1920, and Villa was '
            'gunned down in his car in 1923. Only in the 1930s, under President Lázaro Cárdenas, was most of the land '
            'finally shared out.',
            y=1919),
      legacy('The revolution shaped modern Mexico: its constitution, its land reform, its pride in its Native and mixed '
             'roots, painted in the great murals of Diego Rivera, and the party that grew out of it, which ruled for 71 '
             'years. Zapata is still a hero to farmers and rebels across Latin America.',
             'Began against Porfirio Díaz in 1910',
             'Zapata fought for land and liberty',
             'The 1917 constitution still stands'),
      war='mexican-revolution', wiki='Mexican Revolution')

event('xinhai-revolution', 'The 1911 Revolution in China', 'revolution', (1911, 1912),
      'A bomb that went off by accident set off the revolution that ended more than 2,000 years of emperors in China.',
      scene('A dynasty failing',
            'After defeat by Japan and the Boxer disaster, the Qing court tried reforms: it ended the old exams, built a '
            'modern army and promised a parliament. But many Chinese, angry at foreign bullying and at rule by the '
            'Manchus, wanted the dynasty gone, and secret revolutionary societies spread among students and soldiers.',
            kick='How it began', y=1905),
      figure('sun-yat-sen', 'The doctor',
             'Sun Yat-sen, a doctor trained in Hong Kong, spent years abroad raising money from Chinese overseas for a '
             'revolution, and was even kidnapped by the Chinese embassy in London in 1896. In 1905 he founded the '
             'Revolutionary Alliance. Its risings failed one after another.',
             y=1905),
      turn('Wuchang',
           'On 9 October 1911 a bomb went off by accident in a revolutionaries\' workshop in Hankou. Police found lists '
           'of members, and soldiers in nearby Wuchang, fearing arrest, rose the next night. They took the city, and '
           'within weeks most of China\'s provinces had broken with the Qing. Sun read about it in a newspaper in Denver, '
           'Colorado.',
           img='Wuchang uprising', y=1911, at='wuhan'),
      turn('A republic',
           'Sun hurried home, and on 1 January 1912, in Nanjing, he was sworn in as provisional president of the '
           'Republic of China. But the court\'s strongest general, Yuan Shikai, held the best army in the north. Sun '
           'offered Yuan the presidency if he would make the emperor step down.',
           y=1912, at='nanjing'),
      figure('puyi', 'The last emperor',
             'The emperor, Puyi, was six years old. On 12 February 1912 the empress dowager signed away the throne in his '
             'name, ending more than 2,000 years of rule by emperors. Puyi was allowed to stay in the Forbidden City, and '
             'lived on to be a puppet emperor for Japan and, in the end, a gardener in Communist Beijing.',
             y=1912, at='beijing'),
      figure('yuan-shikai', 'Emperor for 83 days',
             'Yuan Shikai became president, but soon crushed the new parliament and ruled as a dictator. In 1915 he '
             'declared himself emperor. The provinces rebelled, and he gave up the throne after 83 days and died a few '
             'months later. China fell into the hands of rival warlords.',
             y=1916, at='beijing'),
      legacy('The revolution ended China\'s empire and made it one of Asia\'s first republics, though not a steady one: '
             'decades of warlords, civil war and Japanese invasion followed. Sun Yat-sen is honoured as the father of '
             'modern China in both the People\'s Republic and Taiwan, and 10 October is still Taiwan\'s national day.',
             'Began at Wuchang on 10 October 1911',
             'The last emperor gave up the throne in 1912',
             'Sun Yat-sen, the father of the nation'),
      war='xinhai-revolution', wiki='1911 Revolution')

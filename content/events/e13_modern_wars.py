from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('russo-turkish-war-1877', 'The Russo-Turkish War of 1877', 'war', (1877, 1878),
      'Russia went to war to free the Christians of the Balkans from Ottoman rule, and Bulgaria was born again.',
      scene('The April Uprising',
            'In April 1876 the Bulgarians rose against Ottoman rule. The rising was crushed by irregular troops who '
            'burned villages and killed thousands. At Batak most of the village was massacred, many in the church '
            'where they had taken refuge. Reports by an American journalist shocked Europe, and in Britain Gladstone '
            'wrote a furious pamphlet, The Bulgarian Horrors.',
            kick='How it began', y=1876, at='batak'),
      figure('alexander-ii-of-russia', 'The Tsar Liberator',
             'Alexander II, who had freed Russia\'s serfs, came under pressure from Russians who saw themselves as the '
             'protectors of their fellow Orthodox Slavs. Serbia had fought the Ottomans in 1876 and been beaten. On 24 '
             'April 1877 Russia declared war, and Romania let its armies march through to the Danube.',
             y=1877),
      battle('Across the Danube',
             'On the night of 27 June the Russians crossed the Danube at Svishtov in boats and on rafts, and pushed '
             'south. A small force under General Gurko raced ahead over the Balkan mountains, and in July the Russians '
             'seized the Shipka Pass, the main road through them.',
             y=1877, at='svishtov'),
      battle('Plevna',
             'Then the advance stuck. Osman Pasha dug his army into earthworks around the town of Plevna, and threw '
             'back three great Russian and Romanian assaults, in July and September. The Russians settled down to '
             'starve him out. In December, his food gone, Osman tried to break out, was wounded, and surrendered.',
             y=1877, at='pleven', where='Plevna'),
      battle('The Shipka Pass',
             'All summer and autumn, Russian soldiers and Bulgarian volunteers held the Shipka Pass against the Ottoman '
             'attacks. In August, it is said, when their bullets ran out they hurled stones, and even the bodies of '
             'the dead, down on the attackers. Through the winter that followed, many froze at their posts.',
             y=1877, at='shipka'),
      turn('Over the mountains',
           'With Plevna fallen, the Russians crossed the Balkan mountains in the depth of winter. Gurko took Sofia on '
           '4 January 1878, the Ottoman armies broke, and by February the Russians were camped at San Stefano, within '
           'sight of Constantinople, while a British fleet sailed into the Sea of Marmara to warn them off.',
           y=1878, at='sofia'),
      turn('San Stefano',
           'At San Stefano, on 3 March 1878, the Ottomans signed away most of their Balkan lands. Serbia, Montenegro and '
           'Romania became fully independent, and a great new Bulgaria was created, stretching from the Danube to the '
           'Aegean. Britain and Austria-Hungary feared it would be Russia\'s puppet.',
           y=1878, at='san_stefano'),
      turn('The Congress of Berlin',
           'That summer the great powers met in Berlin under Bismarck and tore the treaty up. Big Bulgaria was split '
           'in three: a smaller Bulgaria, a self-governing Ottoman province to its south, and Macedonia, handed back '
           'to the sultan. Austria-Hungary was allowed to occupy Bosnia, and Britain took over Cyprus.',
           y=1878, at='berlin'),
      legacy('Bulgaria was free again after almost five hundred years of Ottoman rule, and every year it marks 3 '
             'March, the day of San Stefano, as its national day. But the hopes left unfulfilled in Berlin, above all '
             'for Macedonia and Bosnia, fed the Balkan Wars and, in 1914, a world war.',
             'Russia fought for the Balkan Christians',
             'Bulgaria was reborn in 1878',
             'Berlin cut Bulgaria back months later'),
      war='russo-turkish-war-1877', wiki='Russo-Turkish War (1877–1878)', at='pleven', where='Plevna')

event('anglo-zulu-war', 'The Anglo-Zulu War', 'war', (1879, 1879),
      'Britain invaded the Zulu kingdom, and lost a whole army in an afternoon before it won.',
      scene('The ultimatum',
            'Britain wanted to join the lands of southern Africa into one federation under its rule, and the Zulu '
            'kingdom, with its army of tens of thousands of warriors, stood in the way. In December 1878 the British '
            'high commissioner, Sir Bartle Frere, sent King Cetshwayo terms he could not accept: among them, to '
            'disband his army within a month.',
            kick='How it began', y=1878),
      figure('cetshwayo', 'The king',
             'Cetshwayo had ruled the Zulu since 1872 from his great royal homestead at Ulundi. He did not want war '
             'with the British, his neighbours in Natal, and told his generals to fight only on Zulu soil. When the '
             'terms ran out in January 1879, a British army under Lord Chelmsford crossed into Zululand.',
             y=1879, at='ulundi'),
      battle('Isandlwana',
             'On 22 January, while Chelmsford was away with half his men chasing a decoy, about 20,000 Zulu warriors '
             'fell on his camp below the hill of Isandlwana. They came on in the horns of the buffalo, a centre and two '
             'wings that closed around the camp. Within hours more than 1,300 of its defenders were dead.',
             y=1879, at='isandlwana'),
      battle('Rorke\'s Drift',
             'That afternoon and night, some 4,000 Zulu who had missed the main battle attacked the mission station at '
             'Rorke\'s Drift, held by about 150 British soldiers behind walls of mealie bags and biscuit boxes. They '
             'held out until dawn, and the Zulu withdrew. Britain gave the defenders eleven Victoria Crosses.',
             y=1879, at='rorkes_drift', where='Rorke\'s Drift'),
      tale('The prince',
           'Among the volunteers was Louis Napoléon, the exiled heir of the French emperor Napoleon III, who had '
           'trained as a British officer. On 1 June, out scouting with a small patrol, he was ambushed by Zulu '
           'warriors and killed. His death shocked Europe, and ended the best hope of the Bonapartes of ever '
           'returning to the French throne.',
           y=1879),
      battle('Ulundi',
             'Chelmsford came back with a far bigger army. On 4 July 1879 he formed his men into a great hollow square '
             'on the plain before Ulundi, and the Zulu charged it again and again, into rifle volleys, cannon and '
             'Gatling guns. The charges broke before they reached the lines, and the British burned the royal '
             'homestead.',
             y=1879, at='ulundi'),
      turn('The kingdom broken',
           'Cetshwayo fled, and was captured in the Ngome forest in August. Sir Garnet Wolseley split his kingdom '
           'among thirteen chiefs, a plan that soon led to civil war. Cetshwayo was taken to Cape Town, and in 1882 to '
           'London, where he met Queen Victoria and won much sympathy.',
           y=1879),
      legacy('Isandlwana was one of the worst defeats suffered by a colonial army in the age of empire, and it is '
             'remembered with pride in South Africa. Yet the war destroyed the Zulu kingdom: within a few years it '
             'had sunk into civil war, and in 1887 Britain annexed it.',
             'Britain invaded in January 1879',
             'The Zulu destroyed a British army at Isandlwana',
             'Ulundi ended the kingdom in July'),
      war='anglo-zulu-war', wiki='Anglo-Zulu War', at='isandlwana')

event('war-of-the-pacific', 'The War of the Pacific', 'war', (1879, 1884),
      'Chile fought Peru and Bolivia for a desert rich in nitrate, and Bolivia lost its coast for good.',
      scene('Nitrate',
            'The Atacama, on the Pacific coast of South America, is the driest desert on earth, but it held nitrate, '
            'prized for fertiliser and explosives. Chilean companies mined it on Bolivian land. When Bolivia raised a '
            'tax on one of them and moved to seize its property, Chilean troops took the port of Antofagasta, on 14 '
            'February 1879.',
            kick='How it began', y=1879, at='antofagasta'),
      battle('Iquique',
             'Peru had a secret alliance with Bolivia, so Chile declared war on both. The war began at sea. At Iquique, '
             'on 21 May, the Peruvian ironclad Huáscar rammed and sank the old wooden Esmeralda. Her captain, Arturo '
             'Prat, leapt onto the enemy\'s deck with his sword and was shot down. Chile made him its greatest hero.',
             y=1879, at='iquique'),
      figure(None, 'The gentleman of the seas',
             'For months the Huáscar\'s captain, Miguel Grau, raided the Chilean coast, and won his enemies\' respect '
             'by rescuing the Esmeralda\'s survivors and writing to Prat\'s widow. On 8 October 1879 the Chilean fleet '
             'trapped the Huáscar off Angamos, and Grau was killed. With the sea lost, Peru\'s coast lay open.',
             img='Miguel Grau Seminario', y=1879),
      battle('Tacna and Arica',
             'Chile landed an army in the desert in November 1879 and took the nitrate province of Tarapacá. In May '
             '1880 it routed the Peruvian and Bolivian armies at Tacna, and Bolivia all but left the war. On 7 June '
             'Chilean infantry stormed the Morro, the great rock fortress above Arica, in less than an hour.',
             y=1880, at='arica'),
      battle('Lima',
             'In January 1881 a Chilean army of about 26,000 men broke the defences of Lima at Chorrillos and '
             'Miraflores, and marched into the Peruvian capital. The seaside town of Chorrillos was burned and looted. '
             'Chile occupied Lima for almost three years, and carried off thousands of books from the national '
             'library.',
             y=1881, at='lima'),
      figure(None, 'The Wizard of the Andes',
             'Peru fought on from the mountains. General Andrés Avelino Cáceres led soldiers and highland villagers in '
             'a guerrilla war against the occupation, and in July 1882 his men wiped out a Chilean garrison at '
             'Concepción. But Chile beat him at Huamachuco in 1883, and Peru made peace.',
             img='Andrés Avelino Cáceres', y=1882),
      turn('A country without a sea',
           'By the Treaty of Ancón in 1883 Peru gave up Tarapacá, and Chile kept Tacna and Arica; Tacna was handed back '
           'in 1929. Bolivia signed a truce in 1884, and in 1904 a treaty that gave up its whole coast. It has been '
           'landlocked ever since.',
           y=1884),
      legacy('The nitrate fields made Chile rich for half a century, and the strongest power on the Pacific coast of '
             'South America. Bolivia has never accepted the loss of its sea: it keeps a navy on Lake Titicaca, marks '
             'a Day of the Sea every March, and took Chile to the world court, which ruled against it in 2018.',
             'Fought over a desert rich in nitrate',
             'Chile won the sea and took Lima',
             'Bolivia lost its whole coast'),
      war='war-of-the-pacific', wiki='War of the Pacific', at='antofagasta')

event('first-sino-japanese-war', 'The First Sino-Japanese War', 'war', (1894, 1895),
      'Japan\'s new army and navy beat Qing China in a war over Korea, and turned the balance of power in Asia upside down.',
      scene('Korea',
            'For centuries Korea\'s kings had honoured the emperors of China as their overlords. But Japan, which had '
            'rebuilt itself on Western lines since 1868, wanted Korea in its own sphere. In 1894 a peasant rising, the '
            'Donghak rebellion, broke out, and China and Japan both sent troops, then refused to leave.',
            kick='How it began', y=1894, at='seoul'),
      turn('The palace',
           'On 23 July 1894 Japanese troops seized the royal palace in Seoul and set up a government friendly to Japan. '
           'Two days later a Japanese cruiser sank a British steamer, the Kowshing, carrying Chinese troops to Korea, '
           'and hundreds of soldiers drowned. On 1 August the two empires declared war.',
           y=1894, at='seoul'),
      battle('Pyongyang and the Yalu',
             'On 15 September the Japanese took Pyongyang and drove the Chinese out of Korea. Two days later, off the '
             'mouth of the Yalu River, Japan\'s fast new cruisers beat China\'s Beiyang Fleet, which hid in harbour for '
             'the rest of the war. It was said that navy money had been spent rebuilding the Empress Dowager\'s Summer '
             'Palace.',
             y=1894, at='pyongyang'),
      cost('Port Arthur',
           'In November the Japanese stormed the fortress of Port Arthur, at the tip of the Liaodong peninsula. Enraged '
           'at finding the mutilated bodies of captured comrades, Japanese troops then killed many of the people of '
           'the town, soldiers and civilians alike. The reports of Western journalists shocked the world.',
           num='Thousands', of='killed in the town after it fell', y=1894, at='port_arthur'),
      battle('Weihaiwei',
             'In January 1895 the Japanese landed in Shandong and took the forts of Weihaiwei from behind, trapping '
             'what was left of the Beiyang Fleet in its harbour. Torpedo boats slipped in at night and sank its '
             'ships. Admiral Ding Ruchang took his own life, and his officers surrendered the fleet.',
             y=1895, at='weihaiwei'),
      figure('li-hongzhang', 'Shimonoseki',
             'China sent its senior statesman, Li Hongzhang, to make peace. At Shimonoseki a Japanese gunman shot him '
             'in the face, and the shame of it made Japan soften its terms. On 17 April 1895 he signed: China '
             'recognised Korea\'s independence, gave Japan Taiwan and the Liaodong peninsula, and paid a vast '
             'indemnity.',
             y=1895, at='shimonoseki'),
      turn('The Triple Intervention',
           'Within a week Russia, France and Germany made Japan give the Liaodong peninsula back, and three years later '
           'Russia leased its tip, Port Arthur, for itself. Japan, humiliated, built up its army and navy, and in 1904 '
           'went to war with Russia.',
           y=1895),
      scene('Taiwan',
            'Japan\'s first colony was Taiwan. Its people declared a short-lived Republic of Formosa to resist, but '
            'Japanese troops crushed it within five months. Japan ruled the island for fifty years, until 1945.',
            y=1895, at='tainan'),
      legacy('The war showed that Japan had become a modern power, and that the Qing empire could no longer defend '
             'itself. The great powers scrambled for slices of China, Chinese reformers and revolutionaries began to '
             'demand change, and Korea, freed from China, fell into Japan\'s shadow, until Japan annexed it in 1910.',
             'A war between China and Japan over Korea',
             'Japan\'s modern navy beat China\'s',
             'China lost Taiwan in 1895'),
      war='first-sino-japanese-war', wiki='First Sino-Japanese War', at='pyongyang')

event('spanish-american-war', 'The Spanish-American War', 'war', (1898, 1898),
      'In a war of less than four months, the United States took the last of Spain\'s empire and became a colonial power.',
      scene('Cuba libre',
            'Cuban rebels had fought Spain for ten years from 1868, and failed. In 1895 they rose again, led by the '
            'poet José Martí. Spain sent 200,000 soldiers, and its general, Valeriano Weyler, herded country families '
            'into guarded camps to cut the rebels off from their people.',
            kick='How it began', y=1895, at='havana'),
      figure('jose-marti', 'The Apostle',
             'Martí had spent years in exile in New York, writing and gathering Cubans for a new war. He landed with '
             'the rebels in 1895, and was shot dead in one of the first battles, at Dos Ríos. Cubans honour him as the '
             'Apostle of their independence.',
             y=1895),
      cost('The camps',
           'In Weyler\'s camps well over 100,000 Cubans died of hunger and disease. American newspapers, racing each '
           'other for readers, filled their front pages with the horrors, true and invented, and many Americans '
           'demanded that their country step in.',
           num='Over 100,000', of='Cubans who died in the camps', y=1897),
      turn('Remember the Maine',
           'On 15 February 1898 the American battleship Maine blew up in Havana harbour, killing more than 260 of her '
           'crew. The newspapers blamed Spain, and the cry went up: Remember the Maine! In April Congress declared '
           'war. The cause of the blast was never settled; it may have been a fire on board.',
           y=1898, at='havana'),
      battle('Manila Bay',
             'The first blow fell on the other side of the world. On 1 May Commodore George Dewey steamed into Manila '
             'Bay, in the Philippines, and destroyed the older Spanish fleet there in a morning, without losing a '
             'ship. "You may fire when you are ready, Gridley," he told the captain of his flagship.',
             y=1898, at='manila'),
      figure('theodore-roosevelt', 'The Rough Riders',
             'Theodore Roosevelt quit the navy department to fight. On 1 July his volunteer cavalry, the Rough Riders, '
             'cowboys and college men side by side, charged up Kettle Hill with Black regular troops, as the army '
             'stormed the San Juan Heights above Santiago de Cuba. It made him a hero, and in 1901 president.',
             y=1898, at='santiago_de_cuba'),
      battle('Santiago',
             'On 3 July the Spanish squadron in Santiago harbour tried to break out to sea, and the waiting American '
             'fleet destroyed every ship in a few hours. The city surrendered on 17 July. Far more American soldiers '
             'died of yellow fever, malaria and typhoid than of Spanish bullets.',
             y=1898, at='santiago_de_cuba'),
      turn('The Treaty of Paris',
           'An armistice was signed on 12 August. By the Treaty of Paris in December, Spain gave up Cuba, which the '
           'Americans occupied until 1902, and handed Puerto Rico, Guam and the Philippines to the United States, the '
           'Philippines for 20 million dollars.',
           y=1898, at='paris'),
      figure('emilio-aguinaldo', 'Another war',
             'In the Philippines, Emilio Aguinaldo\'s rebels had fought Spain alongside the Americans, and declared '
             'independence in June 1898. When the United States kept the islands, war broke out between them in '
             'February 1899. It lasted over three years and killed at least 200,000 Filipinos, most of them '
             'civilians.',
             y=1899),
      legacy('The war made the United States a power with an empire across the Pacific, and Cuba a nation, though '
             'under American watch for decades. For Spain it was simply the Disaster: the loss of the last great '
             'pieces of an empire four centuries old, which set its writers and thinkers asking what had gone wrong.',
             'Fought over Cuba in 1898',
             'Spain lost the last of its empire',
             'The United States became a colonial power'),
      war='spanish-american-war', wiki='Spanish–American War', at='santiago_de_cuba')

event('balkan-wars', 'The Balkan Wars', 'wars', (1912, 1913),
      'The Balkan states drove the Ottomans almost out of Europe, then turned on each other over the spoils.',
      scene('The Balkan League',
            'In 1912 the Ottoman Empire still held a broad belt of land across the Balkans, from Albania to Thrace, '
            'home to Muslims and Christians, Turks, Greeks, Slavs and Albanians. Bulgaria, Serbia, Greece and '
            'Montenegro secretly agreed to drive it out and share the land between them, above all Macedonia.',
            kick='How it began', y=1912),
      battle('The League strikes',
             'Montenegro attacked first, on 8 October 1912, and its allies followed ten days later. The Ottomans, just '
             'out of a war with Italy over Libya, were beaten on every front. The Bulgarians won at Kirk Kilisse and '
             'Lule Burgas, and drove them back to their last line at Çatalca, close to Constantinople.',
             y=1912),
      turn('Salonika',
           'In the west the Serbs won at Kumanovo, and the Greeks marched into the great port of Salonika on 8 '
           'November, a day ahead of a Bulgarian division racing for the same prize. On 28 November the Albanians, '
           'afraid that their land would be shared out too, declared their independence at Vlorë.',
           y=1912, at='thessaloniki', where='Salonika'),
      figure('enver-pasha', 'The raid on the Porte',
             'In January 1913, as the Ottoman government was about to give up the city of Adrianople, a young officer, '
             'Enver Pasha, burst into a cabinet meeting with a band of followers. The war minister was shot dead and '
             'the grand vizier forced to resign. Enver\'s party, the Young Turks, now ruled the empire.',
             y=1913, at='constantinople'),
      battle('Adrianople',
             'The war began again. In March 1913 the Bulgarians, helped by the Serbs, stormed Adrianople, the old '
             'Ottoman capital, after a five-month siege. By the Treaty of London in May, the Ottomans gave up almost '
             'all their lands in Europe.',
             y=1913, at='adrianople'),
      battle('The Second Balkan War',
             'The winners quarrelled over Macedonia. On the night of 29 June 1913 Bulgaria attacked its allies, Serbia '
             'and Greece, and was thrown back. Then Romania invaded from the north, and the Ottomans marched back into '
             'Adrianople. Surrounded, Bulgaria asked for peace within a month.',
             y=1913),
      cost('Fire and flight',
           'Both wars were savage. Armies and bands of irregulars burned villages, and killed or drove out people of '
           'another faith or language, Muslims above all. An international commission that toured the region in 1913 '
           'found that every side had committed atrocities.',
           num='Hundreds of thousands', of='refugees driven from their homes', y=1913),
      turn('The Treaty of Bucharest',
           'By the Treaty of Bucharest in August, Serbia and Greece split most of Macedonia, Romania took southern '
           'Dobruja, and Bulgaria kept only a small part. Albania became a new state. Serbia had almost doubled in '
           'size, and its great neighbour, Austria-Hungary, now saw it as a deadly threat.',
           y=1913, at='bucharest'),
      legacy('In a year the Ottomans lost almost all the lands in Europe that they had held for five centuries. The '
             'wars left Serbia proud and growing, Austria-Hungary afraid of it, and Bulgaria and the Ottomans bitter, '
             'a mix that exploded a year later, when a Bosnian Serb shot the heir to the Austrian throne in Sarajevo.',
             'The Ottomans lost almost all of Europe',
             'The allies then fought over Macedonia',
             'Albania became a new state'),
      states=('Albania',), war='balkan-wars', wiki='Balkan Wars', at='adrianople')

event('turkish-war-of-independence', 'The Turkish War of Independence', 'independence', (1919, 1923),
      'Out of the ruins of the Ottoman Empire, Mustafa Kemal led a fight against occupation, and built a new Turkey.',
      scene('An empire carved up',
            'Beaten in the First World War, the Ottoman Empire lay at the mercy of the Allies. Their troops occupied '
            'Constantinople, and they planned to share out Anatolia itself. On 15 May 1919, with Allied backing, a '
            'Greek army landed at Smyrna, a city with a large Greek population.',
            kick='How it began', y=1919, at='smyrna'),
      figure('mustafa-kemal-ataturk', 'Samsun',
             'Four days later Mustafa Kemal, the general who had held Gallipoli, landed at Samsun on the Black Sea, '
             'sent to keep order. Instead he rallied a resistance. At congresses in Erzurum and Sivas, nationalists '
             'swore to defend the Turkish lands as one, and in April 1920 they opened their own parliament in Ankara.',
             y=1919, at='samsun'),
      turn('The Treaty of Sèvres',
           'In August 1920 the sultan\'s government signed the Treaty of Sèvres. It left the Turks only part of '
           'Anatolia: Smyrna went to Greece to govern, the east to a new Armenia and a possible Kurdistan, and much of '
           'the south to French and Italian spheres. The parliament in Ankara refused it, and fought on.',
           y=1920),
      battle('East and south',
             'In the autumn of 1920 the nationalists beat the Armenian republic in the east and took Kars. In the '
             'south, Turkish fighters drove the French out of Cilicia, and France made peace with Ankara in 1921. '
             'Soviet Russia sent gold and guns.',
             y=1920),
      battle('Sakarya',
             'In the summer of 1921 the Greek army marched on Ankara. Kemal, given full command by the parliament, met '
             'it at the Sakarya River, less than a hundred kilometres from the capital. For 22 days the armies fought '
             'along a front of about a hundred kilometres, until the Greeks fell back, exhausted. Kemal was hailed as '
             'Gazi, the victorious.',
             y=1921, at='sakarya'),
      battle('The Great Offensive',
             'On 26 August 1922 Kemal struck the Greek lines near Afyon. Within days the Greek army broke at '
             'Dumlupınar and fled for the coast, and on 9 September Turkish cavalry rode into Smyrna. His order to his '
             'troops became famous: "Armies, your first goal is the Mediterranean."',
             y=1922, at='dumlupinar', where='Dumlupınar'),
      cost('Smyrna burns',
           'Days later a great fire swept through the Greek and Armenian quarters of Smyrna. Thousands were killed, '
           'and hundreds of thousands crowded onto the waterfront, desperate to escape, as Allied warships looked on. '
           'Who started the fire is still argued over; most historians outside Turkey blame Turkish soldiers.',
           num='Thousands', of='killed as the city burned', y=1922, at='smyrna'),
      figure('ismet-inonu', 'Lausanne',
             'Kemal sent İsmet Pasha, who had twice held the Greeks at İnönü, to make peace at Lausanne in '
             'Switzerland. Hard of hearing, he would, it is said, simply not hear the demands he disliked. After eight '
             'months, in July 1923, the Allies recognised Turkey over all Anatolia and eastern Thrace.',
             y=1923, at='lausanne'),
      cost('The exchange',
           'Greece and Turkey agreed to swap their minorities by religion. Over a million Orthodox Christians, most of '
           'whom had already fled, lost their homes in Turkey, and about 400,000 Muslims were sent from Greece to '
           'Turkey, leaving towns and villages where their families had lived for centuries.',
           num='Over 1.5 million', of='people forced from home by the exchange', y=1923),
      turn('The Republic',
           'The parliament in Ankara had abolished the sultanate in November 1922, and the last sultan left on a '
           'British warship. On 29 October 1923 it proclaimed the Republic of Turkey, with Ankara as its capital and '
           'Mustafa Kemal as its first president.',
           y=1923, at='ankara'),
      legacy('Turks call it the War of Liberation, and its victory is the founding story of their republic. For '
             'Greeks it ended three thousand years of Greek life on the coast of Asia Minor, in what they call the '
             'Catastrophe. Under Kemal, the new Turkey set out to remake itself as a secular, Western-looking nation.',
             'Fought against the carving up of Anatolia',
             'Won at Sakarya and in the Great Offensive',
             'The Republic of Turkey was proclaimed in 1923'),
      states=('Turkey', 'Republic of Turkey'), war='turkish-war-of-independence', wiki='Turkish War of Independence',
      at='ankara')

event('second-italo-ethiopian-war', 'Italy\'s invasion of Ethiopia', 'invasion', (1935, 1936),
      'Mussolini conquered Ethiopia, one of Africa\'s last free nations, with poison gas, and the League of Nations failed.',
      scene('Adwa',
            'Ethiopia was one of only two African countries never to have been colonised, and Italy had a score to '
            'settle: in 1896 Emperor Menelik II had crushed an Italian army at Adwa. In December 1934 a clash at the '
            'oasis of Walwal, on the border with Italian Somaliland, gave Mussolini an excuse.',
            kick='How it began', y=1934, at='adwa'),
      figure('benito-mussolini', 'A new Roman empire',
             'Mussolini dreamed of a new Roman empire, and of avenging Adwa. He gathered a vast army in Eritrea and '
             'Somaliland, and on 3 October 1935, without declaring war, it crossed the border. Adwa fell within three '
             'days, and Italians celebrated their revenge.',
             y=1935),
      figure('haile-selassie', 'The emperor',
             'Emperor Haile Selassie had begun to modernise his country, and had brought it into the League of '
             'Nations. His armies were brave, but many soldiers carried old rifles, or spears and swords, and he had '
             'only a handful of aircraft. He appealed to the League to defend a member under attack.',
             y=1935, at='addis_ababa'),
      turn('Sanctions',
           'The League did condemn Italy, and banned trade in arms and many goods. But oil, which Italy\'s army needed '
           'most, was left off the list, and Britain let Italian ships carry troops through the Suez Canal. In '
           'December the British and French foreign ministers were caught planning to hand Mussolini much of Ethiopia.',
           y=1935),
      cost('Poison gas',
           'The new Italian commander, Pietro Badoglio, used massed artillery, bombers, and mustard gas, banned by a '
           'treaty Italy had signed, sprayed from planes on soldiers and villages alike. Ethiopian armies were '
           'destroyed in the north, at Amba Aradam, Tembien and Maychew, where the emperor himself led the last '
           'attack.',
           num='Thousands', of='burned, blinded or killed by mustard gas', y=1936),
      turn('Addis Ababa',
           'On 2 May 1936 Haile Selassie left his capital by train for exile. Three days later Badoglio\'s motor '
           'columns drove into Addis Ababa, and Mussolini told a cheering crowd in Rome that Italy had an empire at '
           'last. The king of Italy took the title emperor of Ethiopia.',
           y=1936, at='addis_ababa'),
      scene('At Geneva',
            'In June 1936 the exiled emperor spoke to the League of Nations in Geneva, while Italian journalists '
            'jeered. He warned the nations that what had been done to Ethiopia could be done to them: "It is us '
            'today. It will be you tomorrow." Within weeks the League dropped its sanctions.',
            y=1936, at='geneva'),
      cost('Occupation',
           'Ethiopians fought on as guerrillas, the Patriots. After an attempt to kill the viceroy, Rodolfo Graziani, '
           'in Addis Ababa in February 1937, Italian soldiers, Blackshirts and civilians massacred people in the city '
           'for three days, and months later hundreds of monks were shot at the monastery of Debre Libanos.',
           num='Thousands', of='killed in Addis Ababa in three days', y=1937, at='addis_ababa'),
      legacy('Italy\'s empire in Ethiopia lasted five years: in 1941 British and Ethiopian forces drove the Italians '
             'out, and Haile Selassie rode back into his capital. The League of Nations never recovered from failing '
             'Ethiopia, and across Africa and the Caribbean the war made Ethiopia a symbol of freedom.',
             'Italy invaded in October 1935',
             'Mustard gas was used on soldiers and civilians',
             'The League of Nations failed to stop it'),
      war='second-italo-ethiopian-war', wiki='Second Italo-Ethiopian War', at='addis_ababa')

event('first-indochina-war', 'The First Indochina War', 'war', (1946, 1954),
      'Ho Chi Minh\'s Viet Minh fought France for eight years for Vietnam\'s independence, and won at Dien Bien Phu.',
      scene('Independence',
            'When Japan surrendered in 1945, Ho Chi Minh declared Vietnam independent before a vast crowd in Hanoi, '
            'quoting the American Declaration of Independence. But France wanted its colony back. Its troops returned '
            'to the south, and in March 1946 they landed in the north, under a deal with Ho that soon fell apart.',
            kick='How it began', y=1945, at='hanoi'),
      cost('Haiphong',
           'In November 1946 a quarrel over customs in the port of Haiphong turned into fighting, and French warships '
           'shelled the city. In December the Viet Minh attacked the French in Hanoi, and Ho Chi Minh and his '
           'government slipped away to the hills of the north to fight.',
           num='Thousands', of='killed when French guns shelled Haiphong', y=1946, at='haiphong'),
      figure('vo-nguyen-giap', 'The history teacher',
             'The Viet Minh army was led by Võ Nguyên Giáp, a former history teacher with no military training, who '
             'admired Napoleon. He began with small bands fighting a guerrilla war in the jungle, and in 1947 Ho Chi '
             'Minh barely escaped when French paratroopers dropped on the Viet Minh headquarters.',
             y=1947),
      turn('Route 4',
           'In 1949 the communists won in China, and the Viet Minh suddenly had a friendly country at their back, with '
           'weapons, training and advisers. In 1950 Giáp\'s new regular divisions destroyed the French columns on '
           'Route 4 near the Chinese border, at Cao Bằng, France\'s worst colonial defeat in almost two centuries.',
           y=1950, at='cao_bang', where='Cao Bằng'),
      scene('The Americans pay',
            'The war now looked like part of the Cold War, and the United States began to pay for it: by 1954 it was '
            'meeting most of the cost. A new French commander, General de Lattre, ringed the Red River Delta with '
            'concrete forts, and in 1951 he beat back Giáp\'s attacks on it.',
            y=1951),
      battle('Dien Bien Phu',
             'In late 1953 the French dropped paratroopers into the valley of Dien Bien Phu, near Laos, and built a '
             'fortress to lure Giáp into battle. Giáp accepted. His men hauled guns over the mountains by hand, and '
             'supplies on bicycles, and from March 1954 their artillery, hidden on the hills, shut the airstrip and '
             'took the strongpoints one by one.',
             y=1954, at='dien_bien_phu'),
      cost('The fall',
           'After almost two months of siege, on 7 May 1954, the fortress fell. About 11,000 French and colonial '
           'soldiers were marched away as prisoners, and fewer than a third came back alive. The next day, at a '
           'conference in Geneva, the talks on Indochina began.',
           num='About 11,000', of='French and colonial troops taken prisoner', y=1954, at='dien_bien_phu'),
      turn('Geneva',
           'At Geneva in July France agreed to leave. Vietnam was split for the time being at the 17th parallel, the '
           'communists taking the north and a government friendly to the West the south, with elections promised for '
           '1956 to unite the country. Laos and Cambodia became independent. The elections were never held.',
           y=1954, at='geneva'),
      legacy('The French empire in Asia was over, and that same year France was drawn into another colonial war, in '
             'Algeria. In Vietnam the line drawn at Geneva hardened into a border, and as the United States took '
             'France\'s place in the south, the country slid toward a second, even longer war.',
             'France fought to take back its colony',
             'The Viet Minh won at Dien Bien Phu',
             'Vietnam was split at the 17th parallel'),
      states=('Vietnam',), war='first-indochina-war', wiki='First Indochina War', at='dien_bien_phu')

event('mau-mau-uprising', 'The Mau Mau uprising', 'uprising', (1952, 1960),
      'Kenyans rose against British rule and the settlers who had taken their land, and were crushed by camps and the gallows.',
      scene('The lost lands',
            'In the cool, fertile highlands of central Kenya, British settlers had taken the best farmland, and Kikuyu '
            'families were squeezed onto crowded reserves, or worked as squatters on white farms. Africans had almost '
            'no say in how the colony was run. In the late 1940s a secret movement began binding its members by oath '
            'to fight for land and freedom.',
            kick='How it began', y=1950, at='nyeri'),
      turn('The emergency',
           'After a wave of killings, among them a senior chief loyal to the British, the governor, Sir Evelyn Baring, '
           'declared a state of emergency on 20 October 1952. That night police arrested Jomo Kenyatta and other '
           'African leaders, and thousands of young Kikuyu fled to the forests of the Aberdares and Mount Kenya to '
           'fight.',
           y=1952, at='nairobi'),
      figure('jomo-kenyatta', 'On trial',
             'Kenyatta, the best-known African leader in Kenya, had studied in London and written a book about his '
             'people. The British tried him at a remote town, Kapenguria, as the head of Mau Mau, and in 1953 '
             'sentenced him to seven years of hard labour. He always denied leading it, and a key witness later '
             'admitted he had been paid to lie.',
             y=1953),
      cost('Lari',
           'The war was also a civil war among the Kikuyu. On the night of 26 March 1953 Mau Mau fighters attacked '
           'Lari, a settlement of families loyal to the government, and killed over 70 people, many of them women and '
           'children. In revenge, the security forces and the loyalist Home Guard killed many suspects. Both sides '
           'used terror.',
           num='Over 70', of='killed in one night at Lari', y=1953),
      cost('The camps',
           'To cut the fighters off from their people, the British moved over a million Kikuyu into fenced and guarded '
           'villages, and held tens of thousands in detention camps without trial, where many were beaten and '
           'tortured to make them give up the oath. More than a thousand Kenyans were hanged.',
           num='Over 1,000', of='Kenyans hanged by the colonial courts', y=1955),
      scene('Kimathi',
            'The most famous forest leader was Dedan Kimathi, who called himself a field marshal and wrote letters to '
            'the newspapers from the Aberdares. After years on the run he was wounded and captured near Nyeri in '
            'October 1956, and hanged in Nairobi in 1957. By then the revolt was broken.',
            y=1956, at='nyeri'),
      cost('Hola',
           'On 3 March 1959, at Hola camp, guards beat eleven detainees to death for refusing to work. The officials '
           'first said they had died from drinking bad water. When the truth came out it caused an uproar in Britain\'s '
           'parliament, and helped convince the government that it had to give up Kenya.',
           num='11', of='detainees beaten to death at Hola', y=1959),
      turn('Uhuru',
           'The emergency ended in January 1960, and that same month talks in London opened the way to African '
           'majority rule. Kenyatta was freed in 1961, and on 12 December 1963 Kenya became independent, with the man '
           'the British had jailed as the leader of Mau Mau as its first prime minister.',
           y=1963, at='nairobi'),
      legacy('More than 11,000 rebels were killed, against about 200 soldiers and police, and some 1,800 African '
             'civilians killed by the rebels. Mau Mau stayed banned in Kenya until 2003. In 2013 Britain, sued by '
             'elderly survivors of the camps, expressed regret for their torture and paid them compensation.',
             'A revolt over land and freedom',
             'Over a million Kikuyu moved behind wire',
             'Kenya was independent by 1963'),
      war='mau-mau-uprising', wiki='Mau Mau rebellion', at='nyeri')

event('algerian-war', 'The Algerian War', 'independence', (1954, 1962),
      'Algerians fought for eight years to win their independence from France, in a war that brought down a French republic.',
      scene('French Algeria',
            'France had ruled Algeria since 1830, and counted it not as a colony but as part of France. About a million '
            'settlers of European descent, the pieds-noirs, lived there, while nine million Muslim Algerians had few '
            'rights. In May 1945 a protest at Sétif turned into a rising, and the French repression killed thousands.',
            kick='How it began', y=1945, at='setif', where='Sétif'),
      turn('Red All Saints\' Day',
           'On 1 November 1954 a new National Liberation Front, the FLN, set off bombs and attacks across Algeria. '
           '"Algeria is France," declared the interior minister, François Mitterrand, and France sent in the army: '
           'by 1956 over 400,000 French soldiers were in Algeria.',
           y=1954),
      battle('The Battle of Algiers',
             'In 1956 the FLN carried its war into Algiers, planting bombs in cafés crowded with young Europeans. In '
             'January 1957 General Massu\'s paratroopers were given full power in the city. Within months they had '
             'broken the FLN\'s network in the Casbah, by the systematic use of torture, and thousands of suspects '
             'disappeared.',
             y=1957, at='algiers'),
      scene('Torture',
            'Reports of torture shocked France. Maurice Audin, a young mathematician arrested in Algiers in 1957, was '
            'never seen again; in 2018 France admitted that he had died at the hands of a system of torture. The FLN, '
            'for its part, killed many Algerians who would not back it, as well as European civilians.',
            y=1957, at='algiers'),
      figure('charles-de-gaulle', 'I have understood you',
             'In May 1958 settlers and army officers in Algiers, afraid that Paris would make peace, seized power in '
             'the city and threatened to drop paratroopers on Paris. The Fourth Republic collapsed, and Charles de '
             'Gaulle came back to power. In Algiers he told the crowd, "I have understood you." Each side heard what '
             'it wanted.',
             y=1958, at='algiers'),
      turn('Self-determination',
           'De Gaulle\'s army came close to crushing the rebels inside Algeria, while electrified fences sealed its '
           'borders. But he came to believe that France could not hold Algeria by force, and in 1959 he offered '
           'Algerians the right to choose their future. In April 1961 four generals tried a coup in Algiers, which '
           'collapsed within days.',
           y=1961, at='algiers'),
      cost('Paris, 17 October 1961',
           'The war reached France itself. When tens of thousands of Algerians marched peacefully in Paris against a '
           'curfew, the police attacked them, and some were thrown into the Seine. The official toll was three dead, '
           'but historians believe that many dozens, perhaps far more, were killed.',
           num='Dozens', of='Algerian marchers killed in Paris', y=1961, at='paris'),
      turn('Évian',
           'The OAS, settlers and soldiers sworn to keep Algeria French, waged a campaign of bombings and murders. '
           'Still, on 18 March 1962 France and the FLN signed a peace at Évian, and in July Algerians voted for '
           'independence almost unanimously. About 800,000 pieds-noirs fled to France within months.',
           y=1962, at='evian', where='Évian'),
      figure('ahmed-ben-bella', 'Independence',
             'On 5 July 1962, exactly 132 years after the French had taken Algiers, Algeria became independent. Ahmed '
             'Ben Bella, one of the FLN\'s founders, who had spent most of the war in French prisons, became its first '
             'leader. Many harkis, Algerians who had fought for France, were left behind and killed in revenge.',
             y=1962, at='algiers'),
      legacy('Hundreds of thousands of Algerians died; Algeria counts a million and a half. The war brought down a '
             'French republic, sent a million people across the Mediterranean, and left wounds over torture and the '
             'harkis that France has only begun to face. In Algeria 5 July is a national holiday.',
             'France called Algeria part of France',
             'The war brought de Gaulle back to power',
             'Algeria was free on 5 July 1962'),
      war='algerian-war', wiki='Algerian War', at='algiers')

event('hungarian-revolution-1956', 'The Hungarian Revolution', 'revolution', (1956, 1956),
      'For twelve days in 1956 Hungarians rose against Soviet rule, until the tanks came back.',
      scene('Stalin\'s boots',
            'On 23 October 1956 students marched through Budapest in support of reformers in Poland, demanding free '
            'elections and the withdrawal of Soviet troops. By evening a huge crowd had pulled down the giant statue '
            'of Stalin, leaving only his boots. At the radio station the secret police opened fire, and the protest '
            'became a revolution.',
            kick='How it began', y=1956, at='budapest'),
      battle('Fighting the tanks',
             'Soviet tanks rolled into Budapest the next morning. Young fighters, many of them teenagers, met them with '
             'rifles and petrol bombs from alleys and courtyards such as the Corvin Passage. On 25 October security '
             'forces fired on a peaceful crowd outside the Parliament, killing scores of people.',
             y=1956, at='budapest'),
      figure('imre-nagy', 'Imre Nagy',
             'The party turned to Imre Nagy, a reforming communist it had thrown out the year before. At first he '
             'hesitated, then he came over to the revolution. He promised free elections, and on 1 November, as fresh '
             'Soviet troops poured into the country, he declared that Hungary would leave the Warsaw Pact and be '
             'neutral.',
             y=1956, at='budapest'),
      scene('Free days',
            'For a few days Hungary was free. The Soviet tanks pulled out of Budapest, political prisoners were '
            'released, and new parties and newspapers sprang up. Workers\' councils ran the factories, and Cardinal '
            'Mindszenty, jailed for years, was set free.',
            y=1956, at='budapest'),
      figure('nikita-khrushchev', 'The decision',
             'In Moscow, Nikita Khrushchev wavered, then on 31 October decided to crush the revolution, while Britain '
             'and France, attacking Egypt over the Suez Canal, were in no position to protest. Hungary\'s radio '
             'stations sent desperate calls for help to the West. None came.',
             y=1956, at='moscow'),
      battle('Operation Whirlwind',
             'Before dawn on 4 November a massive Soviet force stormed Budapest. Nagy took refuge in the Yugoslav '
             'embassy, and a new government was announced under János Kádár. The fighters held out for a week in the '
             'working-class districts and factories, but the revolution was crushed.',
             y=1956, at='budapest'),
      cost('Flight',
           'About 2,500 Hungarians and 700 Soviet soldiers died. Some 200,000 Hungarians fled across the border to '
           'Austria, and the West took them in. Nagy was lured out of the embassy with a promise of safety, seized, '
           'and after a secret trial hanged in 1958.',
           num='About 200,000', of='Hungarians who fled to the West', y=1956),
      figure('janos-kadar', 'Goulash communism',
             'Kádár ruled Hungary for 32 years. After years of reprisals, in which hundreds were executed, he loosened '
             'his grip in the 1960s, and allowed small freedoms and more food and goods in the shops. "Whoever is not '
             'against us is with us," he said. Hungarians called it goulash communism.',
             y=1961),
      legacy('The revolution showed the world that Soviet rule in eastern Europe rested on tanks. In June 1989 a '
             'quarter of a million people came to Nagy\'s reburial in Budapest, and that October, on the anniversary '
             'of the rising, Hungary became a republic again. 23 October is now a national holiday.',
             'Twelve days of freedom in 1956',
             'Crushed by Soviet tanks on 4 November',
             'Remembered every 23 October'),
      war='hungarian-revolution-1956', wiki='Hungarian Revolution of 1956', at='budapest')

event('nigerian-civil-war', 'The Nigerian Civil War', 'civil-war', (1967, 1970),
      'When Nigeria\'s east broke away as Biafra, war and a blockade brought a famine that shocked the world.',
      scene('Two coups',
            'Nigeria, free from Britain since 1960, joined over 250 peoples under one flag, above all the Hausa and '
            'Fulani of the north, the Yoruba of the west and the Igbo of the east. In January 1966 a coup led mostly by '
            'Igbo officers killed the prime minister and other leaders, and in July northern officers struck back.',
            kick='How it began', y=1966, at='lagos'),
      cost('The killings in the north',
           'In the north, mobs and soldiers turned on Igbo people living there. In 1966 thousands, perhaps tens of '
           'thousands, were murdered, and more than a million fled back to the east. Its military governor, Colonel '
           'Odumegwu Ojukwu, said his people were no longer safe in Nigeria.',
           num='Thousands', of='Igbo killed in the north in 1966', y=1966),
      figure('odumegwu-ojukwu', 'Biafra',
             'A deal made at talks in Ghana fell apart, and on 30 May 1967 Ojukwu declared the Eastern Region the independent Republic of '
             'Biafra, named after the bay off its coast. Much of Nigeria\'s oil lay there. Nigeria\'s young leader, '
             'Yakubu Gowon, called it rebellion, and in July sent in troops for what he expected to be a short police '
             'action.',
             y=1967, at='enugu'),
      battle('The ring closes',
             'In August a Biafran column crossed the Niger and swept deep into the west, alarming Lagos, before it was '
             'driven back. Then the federal army, far bigger and armed by Britain and the Soviet Union, slowly closed '
             'in. It took Enugu, the Biafran capital, in October 1967, and Port Harcourt, its port, in May 1968.',
             y=1967, at='enugu'),
      cost('Starvation',
           'With its ports and roads cut off, the Biafran enclave shrank, packed with refugees, and food ran out. '
           'Photographs of starving children, their bellies swollen by hunger, went around the world. At the worst, '
           'aid workers said, thousands were dying every day.',
           num='Up to 2 million', of='Biafrans dead, most of them from hunger', y=1968),
      scene('The airlift',
            'Church charities flew food in by night, without lights, to a stretch of road at Uli that served as '
            'Biafra\'s airport, dodging federal bombers. French doctors who worked in Biafra went on to found Doctors '
            'Without Borders, to speak out about suffering that others kept quiet about.',
            y=1969),
      figure('yakubu-gowon', 'No victor, no vanquished',
             'In January 1970 federal troops split the enclave and overran Uli. Ojukwu flew into exile, and Biafra '
             'surrendered on 15 January. Gowon declared that there would be no victor and no vanquished, and the '
             'massacre many had feared did not come. But many Igbo lost their savings and their property.',
             y=1970, at='lagos'),
      legacy('Nigeria stayed one country, but the war left deep scars, and Igbo grievances have never fully healed. '
             'Chinua Achebe, Biafra\'s most famous writer, wrote about it to the end of his life, and Chimamanda Ngozi '
             'Adichie told its story to a new generation in her novel Half of a Yellow Sun.',
             'The east broke away as Biafra in 1967',
             'A blockade brought famine',
             'Biafra surrendered in January 1970'),
      war='nigerian-civil-war', wiki='Nigerian Civil War', at='enugu')

event('yom-kippur-war', 'The Yom Kippur War', 'war', (1973, 1973),
      'Egypt and Syria struck Israel by surprise on its holiest day, and the war that followed led, in the end, to peace.',
      scene('Six years on',
            'Since the Six-Day War of 1967 Israel had held Egypt\'s Sinai desert and Syria\'s Golan Heights. Egypt\'s '
            'president, Anwar Sadat, could not win them back by talking, and planned a war with Syria to break the '
            'deadlock. Israel\'s leaders, sure that the Arab armies would not dare to attack, missed the warnings.',
            kick='How it began', y=1973),
      turn('Yom Kippur',
           'At two in the afternoon of 6 October 1973, Yom Kippur, the holiest day of the Jewish year, Egyptian guns '
           'opened fire along the Suez Canal. Troops crossed in rubber boats, blasted gaps in the sand wall on the far '
           'bank with water cannon, and overran Israel\'s forts. In the north, Syrian tanks poured onto the Golan.',
           y=1973, at='suez_canal'),
      figure('golda-meir', 'Golda Meir',
             'That morning the prime minister, Golda Meir, had decided not to strike first, so that the world could not '
             'blame Israel. Its reserves, called up from synagogues and homes, rushed to the fronts. In the first days '
             'Israel\'s leaders feared for the country, and the United States began a great airlift of arms.',
             y=1973, at='jerusalem'),
      battle('The Golan',
             'On the Golan a few Israeli tank crews held off hundreds of Syrian tanks, in a place later called the '
             'Valley of Tears. By 10 October Israel had thrown the Syrians back to where they had started, and it '
             'pushed on toward Damascus, where Iraqi and Jordanian forces joined the fight.',
             y=1973, at='golan'),
      battle('Across the canal',
             'In the south, Egyptian infantry with new Soviet anti-tank missiles smashed the first Israeli '
             'counterattacks. But on 14 October a great Egyptian tank attack failed, and the next night Ariel Sharon\'s '
             'division forced a crossing of the canal, amid savage fighting at a place called the Chinese Farm.',
             y=1973, at='suez_canal'),
      turn('The ceasefire',
           'Israeli tanks spread out on the far bank and cut off Egypt\'s Third Army. The Soviet Union threatened to '
           'send in troops, and the United States put its nuclear forces on alert. Under pressure from both '
           'superpowers, a ceasefire took hold on 25 October.',
           y=1973),
      cost('The cost',
           'In under three weeks more than 2,500 Israelis were killed, and many more Egyptians and Syrians, perhaps '
           '10,000 or more. In Israel the shock brought down Golda Meir\'s government. Egypt celebrates the crossing '
           'of 6 October as a victory that restored Arab pride.',
           num='Over 2,500', of='Israelis killed, and far more Arabs', y=1973),
      turn('Oil',
           'To punish the United States and others who backed Israel, the Arab oil states cut their production and '
           'stopped selling oil to them. The price of oil quadrupled, queues formed at petrol stations in the West, '
           'and the world economy slid into recession.',
           y=1974),
      figure('anwar-sadat', 'From war to peace',
             'The war gave Sadat the standing to make peace. In 1977 he flew to Jerusalem and spoke to Israel\'s '
             'parliament, and in 1979 Egypt and Israel signed a peace treaty, under which Israel gave back the whole '
             'of Sinai. In 1981 Sadat was killed by Islamist soldiers during a parade.',
             y=1977, at='jerusalem'),
      legacy('The war ended Israel\'s belief that it could not be surprised, and gave Egypt back its pride. It brought '
             'the oil shock of the 1970s, and opened the way to the first peace between Israel and an Arab state, a '
             'peace that has held ever since.',
             'A surprise attack on Yom Kippur, 1973',
             'Israel recovered and crossed the canal',
             'It led to peace between Egypt and Israel'),
      war='yom-kippur-war', wiki='Yom Kippur War', at='suez_canal')

event('lebanese-civil-war', 'The Lebanese Civil War', 'civil-war', (1975, 1990),
      'For fifteen years Lebanon\'s militias, and the armies of its neighbours, fought over a small and beautiful country.',
      scene('A delicate balance',
            'Lebanon shared power between its religious communities: by custom the president was a Maronite '
            'Christian, the prime minister a Sunni Muslim and the speaker a Shia. But Muslims were by then thought to '
            'outnumber Christians, and from 1970 the PLO, the Palestinian guerrilla movement, driven from Jordan, made Lebanon '
            'its base for attacks on Israel.',
            kick='How it began', y=1970, at='beirut'),
      turn('The bus',
           'On 13 April 1975, after gunmen fired on a church in a Christian suburb of Beirut, Phalangist militiamen '
           'ambushed a bus carrying Palestinians and killed about two dozen people. Fighting spread across the city, '
           'which was split by the Green Line, named for the weeds that grew along it, into a Christian east and a '
           'Muslim west.',
           y=1975, at='beirut'),
      scene('Revenge',
            'The war became a cycle of revenge. Palestinian and leftist fighters massacred the people of the Christian '
            'town of Damour; Christian militias besieged and overran the Palestinian camp of Tel al-Zaatar. Gunmen at '
            'checkpoints killed people for the religion on their identity cards.',
            y=1976),
      figure('hafez-al-assad', 'Syria steps in',
             'In 1976 Syria\'s president, Hafez al-Assad, sent his army into Lebanon, at first to stop the Palestinians '
             'and their allies from winning. Syrian troops stayed for almost thirty years, and Assad became the most '
             'powerful man in Lebanese politics.',
             y=1976),
      battle('Israel invades',
             'In June 1982, after years of PLO raids and Israeli strikes, Israel invaded, drove up the coast and '
             'besieged West Beirut for ten weeks. The PLO agreed to leave, and Yasser Arafat sailed into exile in Tunisia. '
             'Bashir Gemayel, a Christian leader allied with Israel, was elected president, and was killed by a bomb '
             'three weeks later.',
             y=1982, at='beirut'),
      cost('Sabra and Shatila',
           'Days later Lebanese Christian militiamen entered the Palestinian camps of Sabra and Shatila, in an area '
           'guarded by the Israeli army, and over two days killed hundreds of civilians, perhaps many more. An Israeli '
           'inquiry found that the defence minister, Ariel Sharon, bore personal responsibility for not preventing it.',
           num='Hundreds', of='civilians killed in two days', y=1982, at='sabra_shatila', where='Sabra and Shatila'),
      cost('The barracks',
           'American, French and Italian troops came to keep the peace. On 23 October 1983 suicide bombers drove trucks '
           'packed with explosives into the barracks of the US Marines and the French paratroopers in Beirut. The '
           'peacekeepers left within months.',
           num='299', of='American and French troops killed', y=1983, at='beirut'),
      scene('Wars within the war',
            'The war broke into ever smaller wars: Christians against Christians, Shia militias against Palestinians, '
            'Druze against Christians in the mountains. A new Shia movement backed by Iran, Hezbollah, fought the '
            'Israeli army in the south, and groups linked to it held Western hostages in Beirut, some for years.',
            y=1985),
      turn('Taif',
           'In 1989 Lebanon\'s members of parliament met at Taif in Saudi Arabia, and agreed to share power more evenly '
           'between Christians and Muslims. General Michel Aoun, who led one of two rival governments, refused, until '
           'Syrian forces defeated him in October 1990. The war was over.',
           y=1990, at='beirut'),
      legacy('Some 150,000 people were killed, and about a million left the country. The militia leaders were '
             'pardoned, and many became politicians; Syria kept its grip on Lebanon until 2005. Beirut was rebuilt, '
             'but about 17,000 people who disappeared in the war have never been found.',
             'Fifteen years of war, 1975 to 1990',
             'Syria and Israel both invaded',
             'The Taif Agreement shared power more evenly'),
      states=('Lebanon',), war='lebanese-civil-war', wiki='Lebanese Civil War', at='beirut')

event('central-american-civil-wars', 'The Central American wars', 'wars', (1979, 1996),
      'In Nicaragua, El Salvador and Guatemala, revolution and the Cold War fuelled wars that killed some 300,000 people.',
      scene('The Somozas',
            'For decades Central America was ruled by landowners and generals, often backed by the United States. In '
            'Nicaragua one family, the Somozas, had held power since the 1930s and owned much of the country. When an '
            'earthquake flattened the capital, Managua, in 1972, Anastasio Somoza was accused of pocketing the aid sent '
            'from abroad.',
            kick='How it began', y=1972, at='managua'),
      turn('The Sandinistas',
           'The Sandinistas, guerrillas named after Augusto Sandino, a rebel of the 1920s, led a nationwide rising in '
           '1979. On 17 July Somoza fled to Miami, and two days later the rebels rode into Managua in triumph. They set '
           'out to share land, and to teach the whole country to read.',
           y=1979, at='managua'),
      scene('Archbishop Romero',
            'In El Salvador a military government fought a growing rebellion, and death squads murdered priests, '
            'unionists and peasants. Archbishop Óscar Romero spoke out on the radio each week, and begged soldiers to '
            'stop the killing. On 24 March 1980 he was shot dead as he said Mass. In 2018 the Catholic Church made him '
            'a saint.',
            y=1980, at='san_salvador'),
      cost('El Mozote',
           'The rebels had united as the FMLN, and held large parts of the countryside. In December 1981 an army '
           'battalion trained by the United States killed almost every man, woman and child in the village of El Mozote. The '
           'government denied it for years, until forensic experts dug up the remains.',
           num='Over 800', of='villagers killed at El Mozote', y=1981, at='el_mozote'),
      cost('The Maya highlands',
           'Guatemala\'s war had begun in 1960. In the early 1980s, under General Efraín Ríos Montt and his '
           'predecessor, the army\'s campaign against the guerrillas destroyed hundreds of Maya villages in the '
           'highlands. A truth commission backed by the UN later found that the state had committed acts of genocide.',
           num='About 200,000', of='killed or vanished in Guatemala\'s war', y=1982),
      figure('daniel-ortega', 'The Contras',
             'Daniel Ortega, the Sandinista leader, was elected president of Nicaragua in 1984. But the United States '
             'under Ronald Reagan saw his government as a Soviet foothold, and armed the Contras, rebels built around '
             'Somoza\'s old National Guard, who raided Nicaragua from Honduras. When Congress cut off their money, '
             'officials secretly sold arms to Iran to pay for them.',
             y=1984, at='managua'),
      turn('Peace',
           'Costa Rica\'s president, Óscar Arias, persuaded the region\'s leaders to sign a peace plan in 1987, and won '
           'the Nobel Peace Prize. In 1990 Nicaraguans voted the Sandinistas out, and they handed over power. El '
           'Salvador\'s war ended in 1992, and Guatemala\'s, the longest, in December 1996.',
           y=1992, at='san_salvador'),
      legacy('Most of the dead were civilians, and the truth commissions of El Salvador and Guatemala found that most '
             'had been killed by the army and the death squads. Millions fled, many to the United States. Few of those '
             'responsible were ever punished, and violence and poverty still drive people from the region.',
             'Revolution and Cold War in three countries',
             'Most of the victims were civilians',
             'Peace came between 1990 and 1996'),
      war='central-american-civil-wars', wiki='Central American crisis', at='managua')

event('yemeni-civil-war', 'The war in Yemen', 'civil-war', (2014, 2025),
      'Houthi rebels seized Yemen\'s capital, a Saudi-led coalition went to war against them, and millions were left hungry.',
      scene('After the Arab Spring',
            'Yemen, the poorest country in the Arab world, had been ruled for 33 years by Ali Abdullah Saleh, until '
            'protests in 2011 forced him to hand power to his deputy, Abd Rabbuh Mansur Hadi. The new government was '
            'weak, and in the mountains of the north a Zaydi Shia rebel movement, the Houthis, was growing strong.',
            kick='How it began', y=2012, at='sanaa'),
      turn('Sanaa falls',
           'In September 2014 Houthi fighters, now allied with their old enemy Saleh, marched into the capital, Sanaa. '
           'In early 2015 they put President Hadi under house arrest. He escaped to Aden, and as the Houthis closed in '
           'on the city, fled to Saudi Arabia.',
           y=2014, at='sanaa'),
      figure('mohammed-bin-salman', 'Decisive Storm',
             'On 26 March 2015 Saudi Arabia, which saw the Houthis as the tool of its rival Iran, led a coalition of '
             'Arab states into the war, with air strikes and a blockade. Its young defence minister, Mohammed bin '
             'Salman, hoped for a quick victory. The United States and Britain sold the coalition weapons and helped '
             'it.',
             y=2015),
      battle('Stalemate',
             'Forces backed by the United Arab Emirates drove the Houthis out of Aden in 2015, but then the front lines '
             'barely moved. Coalition air strikes hit weddings, funerals, markets and, in 2018, a school bus, while '
             'Houthi shells and missiles struck Yemeni towns and Saudi cities. In 2017 Saleh broke with the Houthis, '
             'and they killed him.',
             y=2017, at='aden'),
      cost('Hunger and cholera',
           'The war, the blockade and the collapse of the economy brought Yemen to the edge of famine, and the UN '
           'called it the world\'s worst humanitarian crisis. Millions lived on food aid, and from 2016 one of the '
           'largest cholera outbreaks ever recorded spread through the country.',
           num='Over 2 million', of='suspected cases of cholera', y=2017),
      battle('Hodeidah and Marib',
             'In 2018 coalition-backed forces fought to take Hodeidah, the port through which most of Yemen\'s food '
             'arrived, until a deal brokered by the UN in Stockholm stopped them. From 2020 the Houthis threw wave '
             'after wave of fighters at Marib, the government\'s last stronghold in the north, but could not take it.',
             y=2018, at='hodeidah'),
      turn('A truce',
           'In April 2022 a truce brokered by the UN paused the air strikes and the big offensives, and Hadi handed '
           'power to a council of leaders. The truce ran out in October, but the large-scale fighting did not return, '
           'and Saudi Arabia began talking directly to the Houthis.',
           y=2022, at='sanaa'),
      turn('The Red Sea',
           'From late 2023, saying they acted in support of Gaza, the Houthis fired missiles at Israel and attacked '
           'merchant ships in the Red Sea, and many ships went the long way around Africa. The United States, Britain '
           'and Israel struck back with air raids. In May 2025 the United States and the Houthis agreed a ceasefire.',
           y=2024, at='hodeidah'),
      legacy('By 2025 the war had killed hundreds of thousands of people, more of them through hunger and disease '
             'than in the fighting. Yemen was still divided, between the Houthis in the north and the government and '
             'its rival allies in the south, and no peace had been signed.',
             'The Houthis took Sanaa in 2014',
             'A Saudi-led coalition joined in 2015',
             'One of the worst humanitarian crises of its time'),
      states=('Yemen',), war='yemeni-civil-war', wiki='Yemeni civil war (2014–present)', at='sanaa')

event('tigray-war', 'The Tigray War', 'war', (2020, 2022),
      'A power struggle in Ethiopia became one of the deadliest wars of its time, hidden from the world behind a blackout.',
      scene('Old allies',
            'For almost thirty years Ethiopia\'s government was dominated by the Tigray People\'s Liberation Front, the '
            'TPLF, from the northern region of Tigray. In 2018 a reformer, Abiy Ahmed, became prime minister, freed '
            'political prisoners and made peace with Eritrea. Sidelined, the TPLF\'s leaders withdrew to Tigray.',
            kick='How it began', y=2018, at='mekelle'),
      figure('abiy-ahmed', 'November 2020',
             'Abiy had won the Nobel Peace Prize in 2019. In 2020 Tigray held its own election, defying the federal '
             'government, which had put off the national vote because of the pandemic. On 4 November Tigrayan forces '
             'attacked federal army bases in the region, and Abiy ordered an offensive, joined by Eritrean troops and '
             'forces from the Amhara region.',
             y=2020),
      battle('Mekelle',
             'Federal troops took Mekelle, Tigray\'s capital, by the end of November, and Abiy said the operation was '
             'over. But the Tigrayan fighters melted into the mountains, and Tigray was cut off from the world, with '
             'its phones, internet and banks shut down.',
             y=2020, at='mekelle'),
      cost('Atrocities',
           'Reports slowly leaked out of massacres, among them the killing of hundreds of civilians at Axum, by '
           'Eritrean soldiers according to rights groups, and of widespread rape. A joint inquiry by the UN and '
           'Ethiopia\'s rights commission found that all sides had committed abuses, some of which might be war '
           'crimes.',
           num='Hundreds', of='civilians killed at Axum, rights groups said', y=2020, at='axum'),
      battle('The tide turns',
             'In June 2021 Tigrayan forces retook Mekelle, then pushed south into the Amhara and Afar regions, taking '
             'the holy town of Lalibela. By November they were less than 200 kilometres from Addis Ababa. Then, with '
             'newly bought armed drones, the army drove them back into Tigray.',
             y=2021, at='lalibela'),
      cost('Siege',
           'For months little food or medicine reached Tigray\'s six million people, and the UN warned of famine. Aid '
           'groups and the UN said the government was blocking aid; the government blamed the Tigrayan forces.',
           num='Over 5 million', of='people in Tigray who needed food aid', y=2021),
      turn('Pretoria',
           'After a truce broke down, fighting began again in August 2022, and federal and Eritrean forces took Shire, '
           'Axum and Adwa. On 2 November 2022, in Pretoria, South Africa, the government and the TPLF signed a peace '
           'deal brokered by the African Union: Tigray\'s forces would disarm, and its services would be restored.',
           y=2022),
      legacy('No one knows how many died. Researchers estimate that hundreds of thousands were killed by violence, '
             'hunger and the lack of medicine, which would make it one of the deadliest wars of the century so far. '
             'The peace largely held, but more than a million people were still unable to go home.',
             'Began in November 2020',
             'Tigray was cut off from the world',
             'Ended by the Pretoria deal in 2022'),
      war='tigray-war', wiki='Tigray war', at='mekelle')

event('sudan-civil-war', 'The war in Sudan', 'civil-war', (2023, 2025),
      'Two generals who had taken power together turned their guns on each other, and drove millions from their homes.',
      scene('A revolution betrayed',
            'In 2019 months of peaceful protests brought down Omar al-Bashir, who had ruled Sudan for thirty years, '
            'and the army agreed to share power with civilians on the road to democracy. But in 2021 two generals '
            'seized full control: the army chief, Abdel Fattah al-Burhan, and Mohamed Hamdan Dagalo, called Hemedti.',
            kick='How it began', y=2019, at='khartoum'),
      scene('The Rapid Support Forces',
            'Hemedti\'s Rapid Support Forces had grown out of the Janjaweed, the militias accused of genocide in '
            'Darfur in the 2000s, and had become a private army, rich from gold. When plans were drawn up to fold it '
            'into the regular army, the two generals could not agree on how fast, or who would command.',
            y=2022),
      figure('abdel-fattah-al-burhan', 'War in the capital',
             'On 15 April 2023 fighting broke out in Khartoum between Burhan\'s army and the RSF. RSF fighters seized '
             'much of the capital, and the army hit back with air strikes on its own city. Foreign governments flew '
             'out their diplomats and citizens, while millions of Sudanese fled.',
             y=2023, at='khartoum'),
      cost('Darfur again',
           'In Darfur the RSF and allied Arab militias turned on the Masalit and other African peoples. In El Geneina, '
           'UN experts estimated, between 10,000 and 15,000 people were killed in 2023, and hundreds of thousands fled '
           'to Chad. In January 2025 the United States declared that the RSF had committed genocide.',
           num='10,000 to 15,000', of='killed in El Geneina, UN experts said', y=2023, at='el_geneina'),
      battle('Wad Madani',
             'In December 2023 the RSF took Wad Madani, capital of the farming heartland of Gezira, and its fighters '
             'looted and killed in the villages around. In 2024 it besieged El Fasher, the army\'s last stronghold in '
             'Darfur, and famine was confirmed in a camp for displaced people nearby.',
             y=2024, at='el_fasher'),
      turn('Khartoum retaken',
           'In 2025 the tide turned. The army retook Wad Madani in January and the presidential palace in central '
           'Khartoum in March, and by May the RSF had left the capital, much of it in ruins. Sudan was now split, the '
           'army holding the east and centre, and the RSF most of the west.',
           y=2025, at='khartoum'),
      battle('El Fasher',
             'After a siege of eighteen months, the RSF captured El Fasher in late October 2025. Survivors and aid '
             'groups reported mass killings of civilians as the city fell. Its capture gave the RSF nearly all of '
             'Darfur, and the fighting moved east into Kordofan.',
             y=2025, at='el_fasher'),
      cost('The largest crisis',
           'By 2025 more than twelve million people had been driven from their homes, the most anywhere in the world, '
           'and the UN called Sudan the world\'s largest humanitarian crisis. Famine spread, and tens of thousands of '
           'people, perhaps far more, had been killed.',
           num='Over 12 million', of='people driven from their homes', y=2025),
      legacy('At the end of 2025 the war was still being fought, and outside powers were accused of arming both '
             'sides. The people of Sudan, who had overthrown a dictator by peaceful protest only six years before, '
             'were living through the world\'s largest humanitarian disaster.',
             'Began in Khartoum in April 2023',
             'Two generals fighting for power',
             'Over twelve million driven from home'),
      states=('Sudan',), war='sudan-civil-war', wiki='Sudanese civil war (2023–present)', at='khartoum')

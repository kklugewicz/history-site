from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('an-lushan-rebellion', 'The An Lushan Rebellion', 'uprising', (751, 763),
      "A favourite general turned on the Tang emperor, and China's golden age ended in eight years of war.",
      scene('A golden age',
            "Under the emperor Xuanzong, Tang China was perhaps the richest state on Earth. Its capital, Chang'an, held "
            'about a million people, with merchants from Persia, Arabia and Central Asia in its markets, and it was the '
            'great age of Chinese poetry.',
            kick='Before', y=740, at='changan'),
      battle('Talas',
             'In 751, far to the west, a Tang army met an Arab army of the Abbasid caliphs by the river Talas, in Central '
             'Asia, and lost when its Turkic allies changed sides. China pushed no further west. A story says Chinese '
             'prisoners taught papermaking in Samarkand, though paper had probably reached it already.',
             y=751, at='talas'),
      figure('an-lushan', "The emperor's favourite",
             'An Lushan, a general of Sogdian and Turkic parents, commanded the armies of the northeast, some 150,000 men. '
             "Fat, clever and charming, he won over the emperor and his beloved consort, Yang Guifei. In the winter of 755 "
             'he turned his armies on the capitals.',
             y=755),
      figure('emperor-xuanzong-of-tang', 'The death of Yang Guifei',
             "In 756 the rebels took Luoyang and broke through to Chang'an. The old emperor fled west. At Mawei his own "
             "guards mutinied, killed Yang Guifei's cousin, the hated chief minister, and demanded her death too. Xuanzong "
             'gave in, and she was strangled. Soon after, he gave up the throne.',
             y=756, at='mawei'),
      work('The Song of Everlasting Sorrow',
           "Fifty years later the poet Bai Juyi wrote a long poem of the emperor's grief for Yang Guifei. It became one of "
           'the best loved poems in Chinese, and her story has been retold ever since in plays, operas and films.',
           img='Yang Guifei', y=806),
      figure('du-fu', 'A poet in the war',
             "The poet Du Fu was trapped in occupied Chang'an. His poem Spring View begins: the country is broken, but the "
             'mountains and rivers remain. He wrote of farmers dragged off to the army and of his own children going '
             "hungry, and is honoured as one of China's greatest poets.",
             y=757, at='changan'),
      cost('A broken land',
           'An Lushan was murdered by his own son in 757, but the war dragged on until 763, won only with the help of '
           'Uyghur horsemen, who plundered Luoyang as their reward. The census fell from 53 million people to 17 million, '
           'though many were people the broken government could no longer count.',
           num='53 to 17 million', of='people counted, before and after', y=763),
      legacy('The Tang lasted another 150 years but never recovered its strength. Generals in the provinces ruled like '
             'kings, China pulled back from Central Asia, and it grew warier of foreigners. Many historians see 755 as the '
             'great turning point of the Tang.',
             'Talas ended Chinese expansion west in 751',
             'An Lushan rebelled in 755',
             'Ended the golden age of the Tang'),
      states=['Tang Empire'], war='talas-and-an-lushan-rebellion', wiki='An Lushan rebellion', at='changan')

event('viking-age', 'The Viking Age', 'wars', (793, 1066),
      'Norse raiders, traders and settlers sailed from Scandinavia to Baghdad, Constantinople and America.',
      scene('Lindisfarne',
            'In June 793 raiders from the sea fell on the monastery of Lindisfarne, an island off northeast England. They '
            'killed monks and carried off treasure and young men as slaves. The scholar Alcuin wrote that such terror had '
            'never been seen in Britain before. The Viking Age had begun.',
            kick='How it began', img='Lindisfarne', y=793, at='lindisfarne'),
      made('The longship',
           "The Vikings' secret was the longship: long, light and shallow, with a sail and oars, able to cross the open sea "
           'and row far up rivers.',
           'They could strike almost anywhere without warning and be gone before an army arrived. Rich, unguarded '
           'monasteries were easy prey.',
           img='Oseberg ship'),
      battle('Paris and the Great Army',
             'Raids grew into invasions. In 845 Vikings rowed up the Seine, and the Frankish king paid them 7,000 pounds of '
             'silver to leave Paris. In 865 a great Danish army landed in England and conquered every English kingdom but '
             'one, Wessex.',
             y=865, at='paris'),
      figure('alfred-the-great', 'Alfred of Wessex',
             'In 878 a surprise attack drove King Alfred of Wessex into the marshes of Somerset, where, legend says, he let a '
             "peasant woman's cakes burn. Months later he beat the Danes at Edington. England was split: the Danes kept the "
             "north and east, and Alfred's heirs went on to unite the rest.",
             y=878, at='winchester'),
      figure('rollo', 'Normandy',
             'In 911 the Frankish king gave a Viking chief, Rollo, land at the mouth of the Seine if he would keep other '
             "Vikings out. It became Normandy, the land of the Northmen. A story says Rollo would not kiss the king's foot, "
             'and the man he told to do it lifted the foot so high that the king fell over.',
             y=911, at='rouen'),
      scene('The road east',
            'Swedish Vikings went east, down the rivers of Russia to the Black Sea and the Caspian, trading furs and slaves '
            'for Arab silver. They were called the Rus, and gave their name to the state of Kyiv and to Russia. In '
            "Constantinople, Norsemen served as the emperor's Varangian Guard.",
            y=900, at='kyiv'),
      figure('leif-erikson', 'Vinland',
             'Westward, Norse settlers reached Iceland around 870 and Greenland in 985. Around 1000 Leif Erikson sailed on to '
             'a land he called Vinland. At the tip of Newfoundland archaeologists found their houses, the first Europeans in '
             'America, five centuries before Columbus.',
             y=1000, at='lanse_aux_meadows'),
      figure('harald-hardrada', 'Stamford Bridge',
             'The Viking Age is often said to end in 1066, when Harald Hardrada, king of Norway and once a captain of the '
             'Varangian Guard, invaded England and was killed at Stamford Bridge. Weeks later Normans, descendants of Rollo, '
             'landed in the south.',
             y=1066, at='stamford_bridge'),
      legacy('The Vikings were raiders, but also traders, farmers, poets and explorers. They built up towns such as Dublin '
             'and York, founded Normandy, settled Iceland, where their sagas were written, and left English words such as '
             'sky, egg, knife and window.',
             'Lindisfarne raided in 793',
             'Reached America around 1000',
             'Ended at Stamford Bridge in 1066'),
      war='viking-invasions', wiki='Viking Age', img='Gokstad ship')

event('norman-conquest', 'The Norman Conquest', 'conquest', (1066, 1071),
      'Three men wanted the English crown in 1066. The Duke of Normandy won it at Hastings, and England was never the same.',
      scene('Three men want a crown',
            'When King Edward the Confessor died childless in January 1066, three men claimed England: Harold Godwinson, '
            'the richest earl, crowned the next day; Harald Hardrada, king of Norway; and William, Duke of Normandy, who '
            'said Edward had promised him the crown, and Harold had sworn to help him get it.',
            kick='How it began', y=1066, at='london'),
      figure('harald-hardrada', 'Stamford Bridge',
             'Hardrada struck first, landing in Yorkshire in September. King Harold marched north in days and took him by '
             'surprise at Stamford Bridge, near York. Hardrada was killed by an arrow in the throat. Of some 300 ships that '
             'had come, 24 were enough to carry the survivors home.',
             y=1066, at='stamford_bridge'),
      scene('The wind changes',
            'William had waited weeks for a south wind. It came two days after Stamford Bridge. He landed unopposed at '
            'Pevensey with perhaps 7,000 men and their horses, and put up a wooden castle. Harold raced south again.',
            y=1066, at='pevensey'),
      figure('harold-godwinson', 'Hastings',
             "On 14 October Harold's army formed a shield wall on a ridge near Hastings. All day the Norman knights charged "
             'uphill. Twice they pretended to flee, drawing English soldiers down the slope. By evening Harold was dead, by '
             'tradition with an arrow in the eye.',
             y=1066, at='hastings'),
      figure('william-the-conqueror', 'Christmas at Westminster',
             'William was crowned in Westminster Abbey on Christmas Day 1066. Outside, Norman guards heard the shouts of '
             'acclaim, thought it was a riot and set fire to nearby houses. For years the English kept rising against him.',
             y=1066, at='london'),
      cost('The Harrying of the North',
           'When the north rose again in 1069, William had villages, crops and cattle destroyed from York to Durham, so that '
           'famine would finish the rebels. A chronicler of the next century said 100,000 people died.',
           num='100,000', of='dead in the north, said a chronicler', y=1070, at='york'),
      work('The Bayeux Tapestry',
           "A strip of embroidered linen almost 70 metres long tells the Norman side of the story, from Harold's oath to the "
           "battle, like a comic strip: ships, horses, Halley's comet, and a soldier gripping an arrow in his eye.",
           img='Bayeux Tapestry', y=1077),
      made('Castles and the Domesday Book',
           'The Normans held England down with hundreds of castles, first of earth and timber, then of stone, such as the '
           'White Tower in London.',
           'In 1086 William had every estate recorded, with its land, people, ploughs and pigs, in the Domesday Book, so '
           'complete it was named after Judgement Day.',
           img='Domesday Book', y=1086),
      legacy('The conquest replaced England\'s rulers with French-speaking Normans and tied England to France for '
             'centuries. It changed English itself: thousands of French words, such as beef, pork, justice and parliament, '
             'came into the language.',
             'Three claimants and two invasions in 1066',
             'Harold died at Hastings',
             'French poured into the English language'),
      war='norman-conquest', wiki='Norman Conquest', img='Bayeux Tapestry')

event('crusades', 'The Crusades', 'wars', (1096, 1291),
      'For two centuries Christian armies from Europe fought for Jerusalem and the Holy Land.',
      figure('pope-urban-ii', 'God wills it',
             'In 1095 the Byzantine emperor asked the pope for soldiers against the Seljuk Turks. At Clermont in France, '
             'Pope Urban II called on Christians to march east and free Jerusalem, promising that the journey would wipe '
             'away their sins. The crowd shouted: God wills it!',
             kick='How it began', y=1095, at='clermont'),
      scene("The People's Crusade",
            'Before the knights were ready, tens of thousands of poor people set off behind a preacher, Peter the Hermit. On '
            'the way, crusaders massacred the Jews of Rhineland towns such as Mainz and Worms. Most of the marchers were '
            'killed by the Turks soon after they crossed into Asia.',
            y=1096, at='mainz'),
      figure('godfrey-of-bouillon', 'Jerusalem, 1099',
             'After three years, a sick and starving army reached Jerusalem and stormed it on 15 July 1099, massacring the '
             'Muslims and Jews inside. Godfrey of Bouillon, chosen to rule, would not wear a crown of gold where Christ had '
             'worn thorns, and took the title Defender of the Holy Sepulchre.',
             y=1099, at='jerusalem'),
      scene('The crusader states',
            'The crusaders set up four states along the coast, Jerusalem, Antioch, Tripoli and Edessa, defended by great '
            'castles such as Krak des Chevaliers and by new orders of warrior monks, the Templars and the Hospitallers.',
            img='Krak des Chevaliers', y=1144),
      figure('saladin', 'Hattin',
             'Saladin, sultan of Egypt and Syria, united the Muslims against them. In 1187 he trapped the crusader army on '
             'the dry hills of Hattin in the summer heat, and then took Jerusalem. Unlike the crusaders in 1099, he let most '
             'of its people go free for a ransom.',
             y=1187, at='hattin'),
      figure('richard-i-of-england', 'The Lionheart',
             'Three kings set out to win it back. The emperor Frederick Barbarossa drowned crossing a river. Richard the '
             'Lionheart of England took Acre and beat Saladin at Arsuf, but could not take Jerusalem. In 1192 they made a '
             'truce letting Christian pilgrims visit the city. The two never met.',
             y=1191, at='acre'),
      turn('Constantinople, 1204',
           'The Fourth Crusade never reached the Holy Land. Deep in debt to Venice, the crusaders turned on Constantinople, '
           'the greatest Christian city, and sacked it in 1204. The four bronze horses that stood on St Mark\'s in Venice '
           'were part of the loot.',
           img='Horses of Saint Mark', y=1204, at='constantinople'),
      tale("The Children's Crusade",
           'In 1212, stories say, thousands of children in France and Germany set off to free Jerusalem without weapons, '
           'sure the sea would part for them. It did not. Historians think they were mostly poor young people, and that '
           'most went home, or never got further than the ports.',
           kick='A legend', y=1212),
      turn('The fall of Acre',
           'The Mamluks of Egypt took the crusader castles one by one. In 1291 they stormed Acre, the last great crusader '
           'city, and the crusader states were gone.',
           y=1291, at='acre'),
      legacy('Two centuries of crusades left bitter memories between Christians, Muslims and Jews, and between Catholic and '
             'Orthodox Christians. They also drew Europe into the trade of the East and made Venice and Genoa rich.',
             'Called by Pope Urban II in 1095',
             'Jerusalem taken in 1099, lost in 1187',
             'The last crusader city fell in 1291'),
      war='crusades', wiki='Crusades', img='Siege of Jerusalem (1099)')

event('genpei-war', 'The Genpei War', 'civil-war', (1180, 1185),
      'Two samurai clans fought for Japan. The war ended with a drowned child emperor and the first shogun.',
      scene('Red against white',
            'In the 1100s two warrior clans rose to power in Japan: the Taira, with red banners, and the Minamoto, with '
            'white. In 1160 the Taira leader, Kiyomori, beat the Minamoto and came to rule the court at Kyoto. In 1180 he '
            'made his grandson Antoku, aged one, emperor.',
            kick='How it began', y=1180, at='kyoto'),
      figure('taira-no-kiyomori', 'A mercy he regretted',
             'Kiyomori had spared the young sons of the Minamoto leader he killed, sending them to temples and into exile. '
             'In 1180 one of them, Yoritomo, now grown, raised the white banners in the east, and the war began. Kiyomori '
             'died of a fever the next year.',
             y=1181),
      figure('minamoto-no-yoshitsune', 'Down the cliff',
             "Yoritomo's young half-brother Yoshitsune became the war's hero. At Ichi-no-Tani in 1184 he led horsemen down a "
             'slope so steep no one thought it could be ridden, and fell on the Taira camp from behind.',
             y=1184, at='ichi_no_tani'),
      battle('Dan-no-ura',
             'In 1185 the last battle was fought at sea, in the strait of Dan-no-ura. When the tide turned against the '
             "Taira, Kiyomori's widow took the boy emperor Antoku, aged six, in her arms and leapt into the sea with him. "
             'Most of the Taira lords drowned.',
             img='Battle of Dan-no-ura', y=1185, at='dan_no_ura'),
      tale('The Heike crabs',
           'Fishermen near Dan-no-ura say that the Heike crabs, whose shells look like the angry faces of samurai, carry the '
           'spirits of the drowned Taira warriors. The astronomer Carl Sagan used them to explain how selection can shape '
           'living things.',
           img='Heikegani', at='dan_no_ura'),
      figure('minamoto-no-yoritomo', 'The first shogun',
             'Yoritomo did not trust his famous brother and hunted him to his death in 1189. In 1192 the emperor named '
             'Yoritomo shogun, the chief general. From Kamakura he ruled Japan, while the emperors in Kyoto kept their '
             'titles and ceremonies.',
             y=1192, at='kamakura'),
      work('The Tale of the Heike',
           'Blind monks with lutes sang the story of the war for generations before it was written down. It begins with '
           'the sound of temple bells, telling that all things pass and the proud do not last.',
           img='The Tale of the Heike', y=1330),
      legacy('The Genpei War put samurai in charge of Japan for nearly 700 years, under shoguns who ruled in the emperor\'s '
             'name, until 1868. Its heroes and its sad ending, above all the doomed Yoshitsune, became favourite stories of '
             'Japanese theatre.',
             'Taira against Minamoto, 1180 to 1185',
             'A boy emperor drowned at Dan-no-ura',
             'Began 700 years of rule by shoguns'),
      states=['Imperial Japan (Fujiwara)'], war='genpei-war', wiki='Genpei War', img='Battle of Dan-no-ura')

event('magna-carta', 'Magna Carta', 'law', (1215, 1215),
      'Rebel barons made King John promise that even a king must obey the law.',
      figure(None, 'A hated king',
             'King John of England lost Normandy to the French king in 1204 and squeezed his barons for money to win it back. '
             'He quarrelled with the pope, who shut England\'s churches for six years. When his last war in France failed in '
             '1214, the barons rebelled.',
             kick='How it began', img='John, King of England', y=1214),
      scene('Runnymede',
            'In May 1215 the rebels took London. John agreed to meet them on 15 June in a meadow by the Thames, at '
            'Runnymede, and set his seal on a long list of promises they had drawn up. It came to be called Magna Carta, '
            'the Great Charter.',
            y=1215, at='runnymede'),
      made('The law of the land',
           'One clause promised that no free man would be jailed or stripped of his rights except by the lawful judgement '
           'of his peers or by the law of the land.',
           'Another said justice would not be sold, denied or delayed. Together they put in writing that the king himself '
           'was under the law.'),
      turn('Torn up',
           'Neither side kept the deal. Within ten weeks the pope, at John\'s request, declared the charter void, and civil '
           'war broke out. John died in 1216 in the middle of it, after losing part of his baggage, perhaps with his '
           'jewels, in the tidal sands of the Wash.',
           y=1216),
      scene('Given again',
            "To win back the barons, the men ruling for John's nine-year-old son, Henry III, issued the charter again in "
            '1216, 1217 and 1225. Later kings confirmed it again and again, and it became part of English law.',
            y=1225),
      work('Four copies',
           'Four copies of the 1215 charter survive, written in Latin on parchment: two in the British Library and one each '
           'in Lincoln and Salisbury cathedrals. No one signed it: King John sealed it.',
           img='Magna Carta', y=1215),
      tale('A charter for everyone',
           'Lawyers fighting the Stuart kings in the 1600s rediscovered Magna Carta, and settlers carried its ideas to '
           'America, where they echo in the Bill of Rights. In 1948 Eleanor Roosevelt hoped the new Universal Declaration '
           'of Human Rights would be a Magna Carta for all people everywhere.',
           img='Universal Declaration of Human Rights', y=1948),
      legacy('Magna Carta failed as a peace treaty but lived on as an idea: that rulers are bound by the law and cannot jail '
             'people as they please. Only three of its clauses are still law in England, but it is honoured around the '
             'world as a foundation of freedom.',
             'Sealed by King John at Runnymede in 1215',
             'Put the king under the law',
             'Inspired constitutions and human rights'),
      states=['Angevin Empire', 'England', 'English territory'], wiki='Magna Carta', at='runnymede')

event('mongol-conquests', 'The Mongol conquests', 'conquest', (1206, 1294),
      'In two generations the horsemen of the steppe built the largest land empire the world has ever seen.',
      figure('genghis-khan', 'The universal ruler',
             'In 1206 the tribes of the Mongolian steppe gathered by the Onon river and proclaimed a chief named Temüjin '
             'their Genghis Khan, universal ruler. He had united them by war and by sharing the spoils, and he organised '
             'every man in units of ten, a hundred, a thousand and ten thousand.',
             kick='How it began', y=1206, at='onon'),
      made('The horse archer',
           'Every Mongol warrior had several horses and rode from childhood, shooting a powerful bow at full gallop.',
           'Their armies moved faster than any other in the world. They learned siege machines from Chinese and Persian '
           'engineers, and they used terror: cities that gave in might be spared.',
           img='Mongol military tactics and organization'),
      battle('Beijing burns',
             'In 1211 Genghis attacked the Jin empire of northern China, and in 1215 took its capital, Zhongdu, now Beijing, '
             'which was said to have burned for a month.',
             y=1215, at='beijing'),
      cost('The fate of Khwarazm',
           'In 1218 a governor of the Khwarazm Shah killed a Mongol trade caravan at Otrar. The revenge was terrible: '
           'Bukhara, Samarkand, Merv and Nishapur were taken, and in some nearly everyone was killed. In all, the '
           'Mongol wars may have cost tens of millions of lives.',
           num='Tens of millions', of='dead in the Mongol wars, perhaps', y=1220, at='otrar'),
      figure('ogedei-khan', 'Into Europe',
             'Genghis died in 1227. Under his son Ögedei, Mongol armies crushed the Russian princes, burned Kyiv in 1240 and '
             'beat the Poles and the Hungarians in 1241. Then news came that Ögedei had died, and the generals turned back '
             'to choose a new khan. Europe was spared.',
             y=1241),
      figure('hulagu-khan', 'The fall of Baghdad',
             "In 1258 Genghis's grandson Hulagu took Baghdad, the city of the caliphs for five centuries. The caliph was "
             'killed, rolled in a carpet and trampled by horses, it was said, and the books of its libraries were thrown in '
             'the Tigris until it ran black with ink.',
             y=1258, at='baghdad'),
      battle('Ain Jalut and the divine winds',
             'In 1260 the Mamluks of Egypt beat a Mongol army at Ain Jalut, in Palestine, one of the first great Mongol '
             'defeats. Far to the east, storms wrecked the fleets that Kublai Khan sent against Japan in 1274 and 1281. The '
             'Japanese called them kamikaze, divine winds.',
             y=1260, at='ain_jalut'),
      figure('kublai-khan', 'Emperor of China',
             'Kublai conquered the Song and became emperor of all China, founder of the Yuan dynasty, ruling from a new '
             'capital at Beijing. The empire had split into four khanates, but its roads were safe enough for Marco Polo '
             'to travel across Asia to Kublai\'s court.',
             y=1279, at='beijing'),
      legacy('The Mongols killed millions and destroyed great cities, but their empire also joined East and West. Trade, '
             'ideas, paper money and gunpowder moved across it, and so did the Black Death. Genghis Khan is a national hero '
             'in Mongolia today.',
             'The largest land empire in history',
             'From Korea to Hungary in two generations',
             'Joined Asia and Europe, for good and ill'),
      war='mongol-conquests', wiki='Mongol invasions and conquests', img='Mongol Empire')

event('great-zimbabwe', 'Great Zimbabwe', 'building', (1100, 1450),
      'Africans built a city of stone walls on a granite hill, grew rich on gold, and gave a country its name.',
      scene('Houses of stone',
            'From the 1100s, Shona-speaking people on the high plateau between the Zambezi and Limpopo rivers built a city '
            'on and around a granite hill. Its name may come from dzimba dza mabwe, houses of stone. At its height, in the '
            '1300s, perhaps 10,000 to 18,000 people lived there.',
            kick='How it began', y=1300, at='great_zimbabwe'),
      made('Walls without mortar',
           'Its builders split granite into neat blocks and laid them without mortar. The outer wall of the Great '
           'Enclosure runs 250 metres and stands up to 11 metres high.',
           'It is the largest ancient stone structure south of the Sahara. Inside stands a solid cone-shaped tower 9 metres '
           'high, whose purpose no one knows.',
           img='Great Enclosure', y=1350),
      scene('Gold for the ocean trade',
            'The city grew rich on cattle and on gold from the mines of the plateau, carried to Kilwa and other Swahili ports '
            'on the Indian Ocean. In its ruins archaeologists found Chinese porcelain, Persian pottery and glass beads from '
            'India.',
            y=1300, at='kilwa'),
      work('The Zimbabwe birds',
           'Eight birds carved from soapstone, each on a tall pillar, were found at the site, perhaps standing for the '
           'spirits of royal ancestors. One of them is on the flag of Zimbabwe.',
           img='Zimbabwe Bird', y=1350),
      turn('Abandoned',
           'In the 1400s the city was left, perhaps because too many people and cattle had worn out the land, or because '
           'the gold trade moved north. Its power passed to new kingdoms such as Mutapa, which the Portuguese met in the '
           '1500s.',
           y=1450),
      tale('A lie about its builders',
           'When Europeans saw the ruins in the 1870s, many refused to believe that Africans had built them and credited '
           'the Phoenicians or the Queen of Sheba. Archaeologists showed in 1905 and 1929 that the builders were ancestors '
           "of the Shona, but white-ruled Rhodesia kept up the lie into the 1970s.",
           kick='A lie', y=1871),
      legacy('Great Zimbabwe shows a rich African state trading across the Indian Ocean centuries before Europeans came. '
             'When Rhodesia became independent under majority rule in 1980, it took the city\'s name: Zimbabwe.',
             'Built by ancestors of the Shona',
             'Rich on gold traded to the coast',
             'Gave its name to Zimbabwe'),
      states=['Great Zimbabwe', 'Mwenemutapa'], wiki='Great Zimbabwe', at='great_zimbabwe')

event('polynesian-voyages', 'The Polynesian voyages', 'voyage', (1000, 1300),
      'Steering by stars, waves and birds, Polynesian sailors found and settled nearly every island of the Pacific.',
      scene('People of the sea',
            'About 3,000 years ago people of the Lapita culture, whose ancestors had come from Taiwan and the islands of '
            'Southeast Asia, sailed east into the open Pacific and settled Fiji, Tonga and Samoa. There, Polynesian culture '
            'was born.',
            kick='How it began', y=-1000),
      made('Double canoes',
           'They sailed in great double canoes, two hulls joined by a deck, with sails of woven pandanus leaves, carrying '
           'families, pigs, dogs, chickens and plants to start a new life.',
           'They could beat back against the wind, so explorers could search for land and still find their way home.',
           img='Polynesian navigation'),
      scene('Reading the ocean',
            'Navigators carried no instruments. They steered by the rising and setting stars, felt the ocean swells bounce '
            'off islands beyond the horizon, watched for land birds and clouds, and handed down their knowledge by memory '
            'and chant.'),
      turn('The last great leap',
           'Between about 1000 and 1250 came a burst of long voyages. Polynesians reached Hawaii, Rapa Nui, which Europeans '
           'called Easter Island, and finally, around 1250 to 1300, Aotearoa, New Zealand: the last large land on Earth to '
           'be settled by people.',
           y=1250, at='auckland'),
      tale('The sweet potato',
           'Polynesians were growing the sweet potato, a plant from South America, long before Europeans came. Their '
           'sailors probably reached South America and brought it back, and DNA studies suggest that Polynesians and '
           'Native Americans met around 1200.',
           y=1200),
      work('The moai',
           'On Rapa Nui, some 2,000 km from any other inhabited island, people carved nearly 1,000 giant stone figures of '
           'their ancestors, the moai. Islanders say the statues walked, and experiments show they could be rocked upright '
           'along the ground with ropes.',
           img='Moai', y=1300, at='rapa_nui'),
      turn('Hōkūleʻa',
           'European sailors later doubted that Polynesians could have found their islands on purpose. In 1976 the double '
           'canoe Hōkūleʻa sailed from Hawaii to Tahiti, over 4,000 km, guided only by the stars and the sea by the '
           'navigator Mau Piailug. It proved they could.',
           img='Hōkūleʻa', y=1976, at='tahiti'),
      legacy('Polynesians settled a triangle of ocean bigger than Russia, centuries before Europeans dared to cross the open '
             'sea. Their way of finding islands is being taught again, a proud part of the identity of Hawaiians, Māori and '
             'other Pacific peoples.',
             'Settled nearly every island of the Pacific',
             'Reached New Zealand last, around 1250 to 1300',
             'Found their way without instruments'),
      states=['Polynesians', 'Maori', 'Tuʻi Tonga Empire'], wiki='Polynesian navigation', img='Hōkūleʻa', at='tahiti')

event('tenochtitlan', 'Tenochtitlan', 'founding', (1325, 1521),
      'Wanderers from the north founded a city on a lake island, and it became the heart of the Aztec world.',
      scene('An eagle on a cactus',
            'The Mexica told how they had wandered for generations from a homeland in the north, until their god '
            'Huitzilopochtli showed them a sign: an eagle perched on a cactus growing from a rock. They saw it on a marshy '
            'island in Lake Texcoco, and there, in 1325, they founded Tenochtitlan.',
            kick='How it began', y=1325, at='tenochtitlan'),
      made('Gardens on the lake',
           'Around the city they built chinampas, long garden beds of lake mud and reeds held by willow trees, between '
           'canals.',
           'They were among the richest farmland in the world and fed a huge city. Some are still farmed today, at '
           'Xochimilco.',
           img='Chinampa'),
      scene('An empire',
            'In 1428 Tenochtitlan joined Texcoco and Tlacopan in a Triple Alliance and overthrew their overlords. Under '
            'rulers such as Itzcoatl and Moctezuma I the Mexica built an empire of millions, who paid tribute in maize, '
            'cloth, cacao, feathers and gold.',
            y=1428),
      scene('A city on the water',
            'Three stone causeways joined the island to the shore, and an aqueduct brought fresh water from the springs of '
            'Chapultepec. By 1519 perhaps 200,000 people lived there, far more than in any city of Spain.',
            y=1500, at='tenochtitlan'),
      work('The Templo Mayor',
           'At the centre rose the Templo Mayor, a pyramid crowned by twin temples: to Huitzilopochtli, god of war and the '
           'sun, and to Tlaloc, god of rain. Priests sacrificed captives there, cutting out their hearts, to keep the sun '
           'moving across the sky.',
           img='Templo Mayor', y=1487, at='tenochtitlan'),
      tale('Like a dream',
           'When the Spaniards first saw the city in 1519, rising from the lake with its towers and temples, some asked if '
           'it was a dream, wrote the soldier Bernal Díaz. Men who had seen Rome and Constantinople said they had never seen '
           'a market as big as the one at Tlatelolco.',
           y=1519, at='tlatelolco'),
      turn('The fall',
           'In 1521, after a siege of nearly three months, Cortés and tens of thousands of native allies took the starving '
           'city, ruined by fighting and smallpox. The Spaniards pulled down its temples and built Mexico City on top of '
           'them.',
           y=1521, at='tenochtitlan'),
      legacy('Mexico City, one of the biggest cities on Earth, stands on the ruins of Tenochtitlan, and the lake is almost '
             'gone. The eagle on the cactus is on the flag of Mexico, and the Templo Mayor, found by electricity workers in '
             '1978, lies open beside the cathedral.',
             'Founded on a lake island in 1325',
             'Home to perhaps 200,000 people by 1519',
             'Its eagle is on the flag of Mexico'),
      states=['Mexihcah (Triple Alliance)', 'Aztec Empire'], wiki='Tenochtitlan', at='tenochtitlan')

event('black-death', 'The Black Death', 'epidemic', (1346, 1353),
      'The deadliest pandemic in recorded history killed a third or more of Europe in four years.',
      scene('Out of the steppe',
            'The plague came out of Central Asia along the trade routes of the Mongol world. In 1346 it struck the army of '
            'the Golden Horde besieging Caffa, a Genoese port in Crimea. An Italian lawyer wrote that the besiegers hurled '
            'the bodies of their dead over the walls.',
            kick='How it began', y=1346, at='caffa'),
      turn('Messina, 1347',
           'In October 1347 Genoese galleys put in at Messina in Sicily with sick and dying men on board. Within months the '
           'plague was in Genoa, Venice, Marseille and Alexandria, and by 1348 in Paris and London.',
           y=1347, at='messina'),
      scene('The great dying',
            'Most victims had black swellings, buboes, in the groin or armpit, and died within a week. In the lungs, passed '
            'on by coughing, it killed in a day or two. No one knew that fleas from rats carried it. Doctors blamed bad air, '
            'or the stars.',
            y=1348),
      cost('A third of Europe',
           'Between 1347 and 1351 perhaps a third to a half of all Europeans died, 25 million or more, and millions more in '
           'the Middle East and North Africa. In Florence, wrote Boccaccio, the dead were laid in trenches in layers, like '
           "goods in a ship's hold.",
           num='A third to a half', of='of all Europeans died', img='The Triumph of Death', y=1348, at='florence'),
      scene('The flagellants',
            "Many saw God's punishment. Bands of flagellants marched from town to town, whipping themselves bloody to atone "
            "for the world's sins, until the pope banned them.",
            img='Flagellant', y=1349),
      scene('Someone to blame',
            'Others looked for someone to blame. Jews were falsely accused of poisoning wells, and were murdered in hundreds '
            'of towns: in Strasbourg, on 14 February 1349, some 2,000 were burned. The pope pointed out that Jews were dying '
            'of the plague too.',
            kick='The blame', y=1349, at='strasbourg'),
      work('The Decameron',
           "In Boccaccio's Decameron, ten young people flee plague-stricken Florence for a villa in the hills and pass ten "
           'days telling each other a hundred stories, funny, sad and rude. It became a founding work of Italian prose.',
           img='The Decameron', y=1353, at='florence'),
      turn('Workers in demand',
           'With so many dead, there were too few hands to work the fields. Peasants and labourers asked for higher wages '
           'and moved to find them, despite laws to stop them. In England, anger at those laws and a new tax helped spark '
           "the Peasants' Revolt of 1381.",
           y=1381),
      legacy('The Black Death came back every few years for three centuries. It shook faith in the Church and in doctors, '
             'made the work of ordinary people worth more, and, some historians argue, helped bring the Middle Ages to an '
             'end.',
             'Reached Europe in 1347',
             'Killed a third to a half of Europeans',
             'Came back for three centuries'),
      states=['Khanate of the Golden Horde', 'Mamluke Sultanate', 'Byzantine Empire', 'Venice', 'Sicily', 'Papal States',
              'France', 'English territory', 'Holy Roman Empire', 'Castile', 'Aragón', 'Portugal', 'Norway', 'Scotland',
              'Hungary', 'Kingdom of Hungary', 'Denmark', 'Sweden', 'Poland', 'Ilkhanate'],
      wiki='Black Death', img='The Triumph of Death', at='messina')

event('hundred-years-war', "The Hundred Years' War", 'war', (1337, 1453),
      'The kings of England fought for the crown of France for 116 years, until a peasant girl turned the tide.',
      figure('edward-iii-of-england', 'A claim to France',
             'When the last French king of the old line died in 1328, Edward III of England, his nephew through his mother, '
             'had a claim to the throne. The French chose Philip of Valois instead. In 1337 Philip seized Edward\'s lands in '
             'Gascony, Edward claimed the French crown, and the war began.',
             kick='How it began', y=1337),
      battle('Crécy',
             'In 1346 an English army turned at bay at Crécy, in northern France. Thousands of English longbowmen, each able '
             'to shoot ten or more arrows a minute, cut down charge after charge of French knights. The blind King John of '
             'Bohemia had himself led into the fight, and died.',
             img='Battle of Crécy', y=1346, at='crecy'),
      figure('edward-the-black-prince', 'The Black Prince',
             "Edward's son, the Black Prince, won again at Poitiers in 1356 and captured the French king, John II, who was "
             'held in London for a ransom of three million gold crowns. Bands of soldiers out of work plundered the French '
             'countryside for years.',
             y=1356, at='poitiers'),
      figure('henry-v-of-england', 'Agincourt',
             'After years of truces and raids, Henry V invaded in 1415. At Agincourt his tired, sick army stood between two '
             'woods on a muddy field. The French knights in heavy armour floundered in the mud, and the archers shot them '
             'down. Henry married the French king\'s daughter, and their son was to rule both kingdoms.',
             y=1415, at='agincourt'),
      figure('joan-of-arc', 'The Maid of Orléans',
             'In 1429, with Orléans under siege, a peasant girl of 17, Joan of Arc, came to the uncrowned Charles VII saying '
             'that the voices of saints had sent her to save France. Riding with the army, she broke the siege in nine days '
             'and led Charles to be crowned at Reims.',
             y=1429, at='orleans'),
      turn('Burned at Rouen',
           'In 1430 Joan was captured by the Burgundians, allies of the English, and sold to them. A church court found her '
           "guilty of heresy, partly for wearing men's clothes, and she was burned alive at Rouen in 1431, aged 19. A later "
           'court cleared her, and in 1920 she was made a saint.',
           y=1431, at='rouen'),
      made('The guns',
           'The war ended with gunpowder. France built up the best artillery in Europe, and its cannon battered down the '
           'walls of English-held towns and castles.',
           'At Castillon in 1453 French guns shattered the last English army in France. The age of knights and castles was '
           'drawing to a close.',
           y=1453, at='castillon'),
      legacy('After 116 years England had lost everything in France but Calais. The long war helped turn both lands into '
             'nations: English replaced French as the language of England\'s rulers, and France found a national heroine in '
             'Joan of Arc.',
             '116 years of war, 1337 to 1453',
             'Crécy, Poitiers and Agincourt',
             'Joan of Arc turned the tide'),
      war='hundred-years-war', wiki="Hundred Years' War", img='Battle of Agincourt')

event('printing-revolution', 'The printing revolution', 'invention', (1440, 1500),
      'A goldsmith in Mainz printed with metal type, and in fifty years Europe was flooded with books.',
      scene('Before print',
            'In Europe, books were copied by hand, and a Bible could take a scribe more than a year. Only churches, '
            'universities and the rich owned books. In China, printing from carved wooden blocks was centuries old: the '
            'oldest dated printed book, the Diamond Sutra, was made in 868.',
            kick='Before', img='Diamond Sutra', y=868),
      made('Movable type in Asia',
           'Around 1040 a Chinese craftsman, Bi Sheng, made movable type from baked clay. Korean printers cast type in metal '
           'and in 1377 printed the Jikji, the oldest book made with metal type that survives.',
           'But Chinese writing has thousands of characters, and the idea spread slowly. Europe, with an alphabet of a few '
           'dozen letters, was different.',
           img='Jikji', y=1377),
      figure('johannes-gutenberg', 'The press',
             'Around 1440 Johannes Gutenberg, a goldsmith, began working on printing, first in Strasbourg, then in his home '
             'town of Mainz. He cast letters in a metal mix that melted easily, made an oily ink that clung to metal, and '
             'adapted a wine press to print a whole page at once.',
             y=1440, at='strasbourg'),
      work('The Gutenberg Bible',
           'His great work, finished around 1455, was a Latin Bible of 1,282 pages in two columns, as handsome as any written '
           'by hand. About 180 copies were printed, and 49 survive. A future pope who saw pages wrote that they could be '
           'read without glasses.',
           img='Gutenberg Bible', y=1455, at='mainz'),
      turn('Bankrupt',
           'Gutenberg had borrowed heavily from a merchant, Johann Fust, who sued him in 1455 and took over the workshop. '
           "Fust and Gutenberg's assistant Peter Schöffer became successful printers. Gutenberg died in 1468, not rich.",
           y=1455, at='mainz'),
      scene('A flood of books',
            'Printing spread like fire. By 1500 there were presses in some 250 towns across Europe, and they had printed '
            'perhaps 20 million books. A book was now far cheaper, and every copy was the same.',
            y=1500, at='venice'),
      turn("Luther's pamphlets",
           "In 1517 Martin Luther's attacks on the Church were printed and spread across Germany in weeks. He called "
           "printing God's highest gift. Without the press, the Reformation might have been crushed like earlier protests.",
           y=1517, at='wittenberg'),
      legacy('Printing made knowledge cheap, lasting and the same in every copy. It spread the Renaissance, the Reformation '
             'and the new science, fixed the spelling of languages and helped millions learn to read. Many call it the most '
             'important invention of the last thousand years.',
             'Movable type began in China and Korea',
             'Gutenberg printed his Bible around 1455',
             '20 million books in Europe by 1500'),
      states=['Holy Roman Empire'], wiki='Printing press', img='Gutenberg Bible', at='mainz')

event('fall-of-constantinople', 'The fall of Constantinople', 'siege', (1453, 1453),
      'A sultan of 21 with giant cannon took the city of the Caesars, and the Roman Empire came to an end.',
      scene('A city alone',
            'By 1453 the eastern Roman Empire, which we call Byzantine, was little more than its capital, Constantinople, '
            'with perhaps 50,000 people left inside walls that had stood for a thousand years. All around it lay the lands '
            'of the Ottoman Turks.',
            kick='Before', img='Walls of Constantinople', y=1453, at='constantinople'),
      figure('mehmed-ii', 'The young sultan',
             'Mehmed II became sultan at 19 and made Constantinople his first goal. He built a fortress on the Bosporus to '
             'cut the city off from the Black Sea, and in April 1453 surrounded it with perhaps 80,000 men.',
             y=1452, at='constantinople'),
      made('The great guns',
           'A Hungarian engineer, Orban, had offered to make cannon for the Byzantines, who could not pay. Mehmed could. Orban '
           'cast a bronze giant over 8 metres long that fired stone balls of half a tonne.',
           'It could fire only a few times a day, but the guns pounded the old walls day after day for six weeks.',
           y=1453),
      figure('constantine-xi-palaiologos', 'The last emperor',
             'Inside, the emperor Constantine XI had about 7,000 defenders, among them 700 soldiers from Genoa under '
             'Giovanni Giustiniani. A great iron chain across the Golden Horn kept the Ottoman fleet out of the harbour.',
             y=1453, at='constantinople'),
      tale('Ships over the hill',
           'Mehmed found a way round the chain. On 22 April his men hauled some 70 ships overland on greased logs, over the '
           'hill from the Bosporus into the Golden Horn. The defenders woke to see an enemy fleet inside their harbour.',
           y=1453, at='constantinople'),
      battle('The last assault',
             'Before dawn on 29 May the Ottomans attacked in waves. When Giustiniani was badly wounded and carried away, the '
             'defence broke and the janissaries poured in. Constantine XI threw off his imperial robes and died fighting. '
             'His body was never surely found.',
             img='Fall of Constantinople', y=1453, at='constantinople'),
      turn('Hagia Sophia',
           'Mehmed rode to Hagia Sophia, for 900 years the greatest church in Christendom, and had it made a mosque. He made '
           'Constantinople his capital and brought in people from all over his empire to fill it again.',
           img='Hagia Sophia', y=1453, at='constantinople'),
      legacy('The fall ended the Roman Empire nearly 1,500 years after Augustus and made the Ottomans a great power for '
             'centuries. Greek scholars fled to Italy with ancient books, feeding the Renaissance, and the city became '
             'Istanbul.',
             'Taken on 29 May 1453',
             'The end of the Roman Empire',
             'The new Ottoman capital'),
      states=['Byzantine Empire', 'Ottoman Empire'], wiki='Fall of Constantinople', img='Fall of Constantinople',
      at='constantinople')

event('reconquista', 'The Reconquista', 'wars', (722, 1492),
      'Over seven centuries the Christian kingdoms of the north took Spain and Portugal from their Muslim rulers.',
      scene('Covadonga',
            'After 711, Muslim armies conquered nearly all of Spain, which they called al-Andalus. Only in the mountains of '
            'the far north did Christians hold out. Around 722, tradition says, a noble named Pelayo beat a Muslim force at '
            'Covadonga and founded the kingdom of Asturias.',
            kick='How it began', y=722, at='covadonga'),
      scene('Córdoba',
            'For three centuries al-Andalus was the richest land in western Europe. Córdoba, capital of the Umayyad caliphs '
            'of Spain, had paved and lit streets, hundreds of baths and a vast mosque, and Muslim, Jewish and Christian '
            'scholars worked there side by side.',
            img='Mosque–Cathedral of Córdoba', y=950, at='cordoba'),
      figure('el-cid', 'El Cid',
             'When the caliphate broke up into small rival kingdoms in the 1000s, the Christian north pushed south, taking '
             'Toledo in 1085. The most famous warrior of the age, Rodrigo Díaz, El Cid, fought for Christian and Muslim '
             'rulers alike, and in 1094 took Valencia for himself.',
             y=1094, at='valencia'),
      battle('Las Navas de Tolosa',
             'Berber dynasties from Morocco, the Almoravids and then the Almohads, crossed over to fight back. But in 1212 '
             'the kings of Castile, Aragon and Navarre crushed the Almohads at Las Navas de Tolosa. Within 40 years Córdoba '
             'and Seville had fallen, and only Granada was left.',
             y=1212, at='las_navas'),
      work('The Alhambra',
           'For 250 more years the kingdom of Granada survived, paying tribute to Castile. Its rulers built the Alhambra, a '
           'red-walled palace of courtyards, fountains and carved plaster, one of the masterpieces of Islamic art.',
           img='Alhambra', y=1350, at='granada'),
      figure('isabella-i-of-castile', 'The fall of Granada',
             'Isabella of Castile and Ferdinand of Aragon, whose marriage joined their kingdoms, fought ten years for '
             'Granada. On 2 January 1492 its last sultan, Muhammad XII, gave up the keys. Legend says he wept as he looked '
             'back, and his mother told him to weep like a woman for what he could not hold like a man.',
             y=1492, at='granada'),
      cost('Expelled',
           'Victory ended tolerance. In 1492 Spain\'s Jews were told to convert or leave, and tens of thousands went into '
           'exile. Muslims were forced to convert from 1502, and from 1609 their descendants, the Moriscos, were expelled '
           'too.',
           num='300,000', of='Moriscos expelled from Spain from 1609', y=1609),
      legacy('The Reconquista made Spain and Portugal crusading Catholic kingdoms, and in the very year it ended, Columbus '
             'sailed west. The mixing of cultures lives on in Spanish words such as aceite, oil, and in buildings from '
             'Córdoba to the Alhambra.',
             'From Covadonga, around 722, to Granada, 1492',
             'Al-Andalus, a centre of learning',
             'Ended with the expulsion of Jews and Muslims'),
      war='reconquista', wiki='Reconquista', img='Alhambra')

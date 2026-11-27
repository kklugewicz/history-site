from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('world-war-i', 'The First World War', 'world-war', (1914, 1918),
      'Four years of trench war killed some ten million soldiers, brought down four empires and remade the map of the world.',
      figure('gavrilo-princip', 'Sarajevo',
             'On 28 June 1914 Archduke Franz Ferdinand, heir to the throne of Austria-Hungary, drove through Sarajevo in '
             'Bosnia. A bomb missed him, but later his driver took a wrong turn and stopped right in front of Gavrilo '
             'Princip, a 19-year-old Bosnian Serb who wanted the South Slavs free of Austria. Princip shot the archduke '
             'and his wife dead.',
             kick='How it began', y=1914, at='sarajevo'),
      turn('Into war',
           'Austria-Hungary blamed Serbia and, sure of German support, declared war on it. Russia backed Serbia, Germany '
           'declared war on Russia and its ally France, and when German armies marched through neutral Belgium, Britain '
           'came in too. In five weeks a murder had become a war of the great powers. Crowds cheered, sure it would be '
           'over by Christmas.',
           y=1914),
      tale('The Christmas truce',
           'By December the armies in the west were dug into trenches from the Channel to Switzerland. On Christmas Eve, '
           'in places along the line, German soldiers put up candles and sang carols, and British soldiers sang back. On '
           'Christmas Day men from both sides met in no man\'s land, swapped cigarettes and buried their dead; here and '
           'there they even played football.',
           img='Christmas truce', y=1914, at='ypres'),
      battle('Gallipoli',
             'In 1915 the Allies tried to knock the Ottoman Empire out of the war by landing on the Gallipoli peninsula, '
             'near Constantinople. Australian, New Zealand, British and French troops clung to the beaches for eight '
             'months, then gave up. Australians and New Zealanders remember the landing every 25 April as Anzac Day; for '
             'the Turks it made the name of Mustafa Kemal.',
             img='Gallipoli campaign', y=1915, at='gallipoli'),
      made('Weapons of a new kind',
           'Machine guns and heavy guns; poison gas, first used on a large scale by Germany at Ypres in 1915; tanks, sent '
           'into battle by Britain in 1916; and aeroplanes fighting in the sky.',
           'Industry turned war into slaughter on a scale never seen before. Most soldiers who died were killed by '
           'shellfire, and gas left many survivors blinded or with ruined lungs.',
           y=1915, at='ypres'),
      cost('Verdun and the Somme',
           'In 1916 Germany tried to bleed France white at Verdun, in a battle that lasted ten months. To take the '
           'pressure off, the British attacked on the Somme on 1 July and lost nearly 20,000 men killed on the first day '
           'alone, the worst day in the history of their army. Neither battle moved the front more than a few miles.',
           num='Over a million', of='men killed or wounded on the Somme', img='Battle of the Somme', y=1916,
           at='somme'),
      turn('1917',
           'In 1917 Russia fell into revolution and soon left the war. But German submarines sinking ships without '
           'warning, and a German telegram offering Mexico a deal against the United States, brought the Americans in. '
           'By 1918 fresh American troops were landing in France by the hundred thousand.',
           y=1917),
      work('The old lie',
           'Soldier poets wrote what the newspapers would not. Wilfred Owen, a British officer, described men drowning in '
           'gas and called the old saying that it is sweet to die for your country an old lie. He was killed a week '
           'before the war ended; the telegram reached his mother as the church bells rang for peace.',
           img='Wilfred Owen', y=1918),
      turn('The eleventh hour',
           'Germany\'s last great attack in the spring of 1918 failed, its allies collapsed, and sailors and workers rose '
           'in revolt at home. The kaiser fled to the Netherlands. The armistice was signed in a railway carriage in the '
           'forest of Compiègne, and at 11 o\'clock on 11 November 1918 the guns fell silent.',
           img='Armistice of 11 November 1918', y=1918, at='compiegne'),
      legacy('About ten million soldiers and millions of civilians died. The German, Austrian, Russian and Ottoman empires '
             'fell, and new countries from Poland to Yugoslavia took their place. The harsh peace made at Versailles in '
             '1919, and the bitterness it left in Germany, helped lead to a second, even greater war twenty years later.',
             'Began with a murder in Sarajevo, 1914',
             'Millions died in the trenches',
             'Four empires fell',
             'Ended at 11 am on 11 November 1918'),
      war='world-war-i', wiki='World War I', img='Western Front (World War I)')

event('armenian-genocide', 'The Armenian genocide', 'genocide', (1915, 1917),
      'During the First World War the Ottoman government drove its Armenians from their homes, and about a million died.',
      scene('An ancient people',
            'Armenians had lived in eastern Anatolia since ancient times, and their kingdom was the first to make '
            'Christianity its religion, by tradition in the year 301. By 1914 some two million lived in the Ottoman '
            'Empire, many of them farmers, traders and craftsmen. Massacres in the 1890s had already killed a hundred '
            'thousand or more.',
            kick='How it began', y=1914),
      turn('24 April 1915',
           'After a heavy defeat by Russia in the Caucasus, the Young Turk government led by Talaat, Enver and Djemal '
           'branded the Armenians traitors. On the night of 24 April 1915 police in Constantinople rounded up hundreds of '
           'Armenian writers, priests and leaders, and most of them were later killed. Armenians remember the date every '
           'year.',
           y=1915, at='constantinople'),
      cost('The death marches',
           'In the months that followed, Armenian men were shot, and women, children and the old were marched over '
           'mountains into the Syrian desert toward Deir ez-Zor, with little food or water. Hundreds of thousands died '
           'of killing, hunger, thirst and disease. Others were forced to convert, and children were taken into Muslim '
           'homes.',
           num='About a million', of='Armenians died, by many estimates', y=1915, at='deir_ez_zor',
           where='Deir ez-Zor'),
      scene('Witnesses',
            'Many saw it. The American ambassador, Henry Morgenthau, cabled Washington that a campaign of race '
            'extermination was under way, and a German army medic, Armin Wegner, secretly photographed the camps. Some '
            'Turks and Kurds hid Armenians at the risk of their own lives, and a few officials refused to carry out the '
            'orders.',
            img='Henry Morgenthau Sr.', y=1915),
      scene('A word for it',
            'A Polish Jewish lawyer, Raphael Lemkin, had followed the killing of the Armenians as a student. In 1944 he '
            'made up a new word, genocide, for the deliberate destruction of a people, pointing to the Armenians and to '
            'the Nazi murder of the Jews. In 1948 the United Nations made genocide a crime under international law.',
            img='Raphael Lemkin', y=1944),
      legacy('Armenian life in Anatolia, thousands of years old, was almost wiped out, and the survivors scattered from '
             'Beirut to Los Angeles. Most historians and many countries call it genocide. Turkey accepts that many '
             'Armenians died but rejects the word, and the question still divides the two nations.',
             'Began on 24 April 1915',
             'About a million Armenians died',
             'Behind the word genocide'),
      states=('Ottoman Empire', 'Armenia', 'Ottoman Sultanate'), wiki='Armenian genocide', at='deir_ez_zor',
      where='Deir ez-Zor')

event('russian-revolution', 'The Russian Revolution', 'revolution', (1917, 1922),
      "Russia's tsar fell in 1917, and Lenin's Bolsheviks took power and won a civil war to found the Soviet Union.",
      figure('grigori-rasputin', 'The holy man',
             'Russia was losing the war, and its people were hungry. At court the empress trusted Rasputin, a wandering '
             'holy man from Siberia who seemed able to ease her son\'s bleeding illness. In December 1916 nobles who '
             'blamed him for the empire\'s troubles poisoned him, shot him and threw him into a frozen river.',
             kick='How it began', y=1916, at='st_petersburg', where='Petrograd'),
      turn('The tsar falls',
           'In February 1917 women queuing for bread in Petrograd went on strike, and the soldiers sent to stop the '
           'crowds joined them. Within days Tsar Nicholas II gave up the throne, ending three centuries of the Romanovs. '
           'A provisional government took over, but it kept on fighting the war.',
           y=1917, at='st_petersburg', where='Petrograd'),
      figure('vladimir-lenin', 'Peace, land and bread',
             'Germany let Vladimir Lenin, the exiled leader of the Bolsheviks, travel home through its lands in a sealed '
             'train, hoping he would make trouble. He did. Promising peace, land and bread, his party won over workers '
             'and soldiers, and on 7 November 1917 its Red Guards took the Winter Palace almost without a fight.',
             y=1917, at='st_petersburg', where='Petrograd'),
      turn('Brest-Litovsk',
           'Lenin made peace with Germany in March 1918, giving up Ukraine, Poland, Finland and the Baltic lands, about a '
           'third of the old empire\'s people. He closed the elected assembly when his party lost the vote, and his '
           'secret police, the Cheka, began a Red Terror against all opponents.',
           y=1918, at='brest_litovsk'),
      scene('The end of the Romanovs',
            'In July 1918, with anti-Bolshevik forces closing in, the Bolsheviks shot Nicholas, his wife, their five '
            'children and four servants in a cellar in Yekaterinburg. For decades rumours said the youngest daughter, '
            'Anastasia, had escaped; DNA tests have since shown that all the children died.',
            img='Execution of the Romanov family', y=1918, at='yekaterinburg'),
      cost('Civil war',
           'The Reds fought the Whites, armies of officers, monarchists and liberals backed by foreign troops, and '
           'peasant armies, nationalists and anarchists across the whole empire. Leon Trotsky built the Red Army and '
           'rode from front to front in an armoured train. War, terror, hunger and typhus killed millions before the '
           'Reds won.',
           num='7 to 12 million', of='died in the civil war and its famine', y=1920),
      turn('The Soviet Union',
           'In December 1922 Russia, Ukraine, Belarus and the republics of the Caucasus joined as the Union of Soviet '
           'Socialist Republics, the first state ruled by a communist party. Lenin was soon struck down by strokes and '
           'died in 1924, and Joseph Stalin, outmanoeuvring Trotsky, took his place.',
           y=1922, at='moscow'),
      legacy('The revolution created the Soviet Union, which lasted until 1991, and inspired communist parties and '
             'revolutions around the world, from China to Cuba. It promised equality, but brought one-party rule, terror '
             'and famine, and for much of the 20th century the world was split between its followers and its enemies.',
             'The tsar fell in February 1917',
             'Lenin took power that November',
             'The Reds won the civil war',
             'The Soviet Union was founded in 1922'),
      war='russian-civil-war', wiki='Russian Revolution')

event('spanish-flu', 'The flu of 1918', 'epidemic', (1918, 1920),
      'A new flu swept the world in the last year of the First World War and killed more people than the war had.',
      scene('A new flu',
            'In the spring of 1918 a new kind of flu appeared among soldiers; one of the first known outbreaks was at an '
            'army camp in Kansas. Troopships and crowded camps carried it around the world. Spain, neutral in the war, '
            'let its newspapers report it freely, so others called it the Spanish flu.',
            kick='How it began', y=1918, at='camp_funston', where='Camp Funston, Kansas'),
      turn('The second wave',
           'In the autumn a far deadlier wave struck. Unlike most flu, it killed healthy young adults, often within days: '
           'their lungs filled with fluid and their faces turned blue. In October 1918 alone some 195,000 Americans died. '
           'Coffins ran short, and cities dug mass graves.',
           y=1918),
      scene('Masks and closed doors',
            'With no vaccine and no antibiotics, towns closed schools, theatres and churches, banned spitting and told '
            'people to wear gauze masks. Philadelphia went ahead with a huge parade in September, and within weeks '
            'thousands of its people were dead; St Louis closed down early and suffered far less.',
            img='Spanish flu', y=1918, at='philadelphia'),
      cost('The whole world',
           'The flu reached almost everywhere, from Arctic villages to Pacific islands. India suffered worst, with '
           'perhaps 12 million dead, and Western Samoa lost about a fifth of its people. In all, about a third of the '
           'people in the world caught it.',
           num='Perhaps 50 million', of='died around the world', y=1919),
      tale('Who caught it',
           'Among those who caught it and lived were the young Walt Disney, and President Woodrow Wilson, who fell ill '
           'at the peace talks in Paris in 1919. Others were not so lucky: the Austrian painter Egon Schiele died three '
           'days after his pregnant wife.',
           y=1918),
      made('Finding the virus',
           'In 2005 scientists rebuilt the 1918 virus from its genes, found in preserved lung tissue and in a victim '
           'buried in the frozen ground of Alaska.',
           'It turned out to be a bird flu of the kind called H1N1, and studying it helps the world prepare for the next '
           'pandemic.',
           y=2005),
      legacy('The flu of 1918 killed more people than the First World War, yet for decades it was half forgotten, buried '
             'under the memory of the war. Its lessons about masks, closing crowded places and how fast a new virus can '
             'spread came back to the world in 2020.',
             'Struck in waves in 1918 and 1919',
             'Killed young, healthy adults',
             'Tens of millions died'),
      states=('Spain', 'United States', 'United Kingdom of Great Britain and Ireland', 'France', 'British Raj',
              'Canada', 'Australia', 'New Zealand', 'South Africa', 'Brazil', 'Mexico', 'Empire of Japan',
              'German Empire', 'Germany', 'Kingdom of Italy', 'Italy'),
      wiki='Spanish flu', at='camp_funston', where='Camp Funston, Kansas')

event('great-depression', 'The Great Depression', 'crisis', (1929, 1939),
      'The Wall Street Crash of 1929 began the worst slump of modern times, and it helped bring Hitler to power.',
      scene('The roaring twenties',
            'In the 1920s America boomed. Cars, radios and refrigerators poured from its factories, and millions bought '
            'shares, often with borrowed money, sure that prices would keep rising. But farmers were struggling, wages '
            'lagged behind profits, and much of the boom ran on credit.',
            kick='How it began', y=1928, at='new_york'),
      turn('Black Tuesday',
           'In late October 1929 share prices on the New York Stock Exchange collapsed. On Black Tuesday, 29 October, '
           'panicking traders sold 16 million shares. Fortunes vanished in days, and by 1932 the market had lost almost '
           'nine tenths of its value.',
           img='Wall Street Crash of 1929', y=1929, at='new_york'),
      cost('Hard times',
           'Banks failed by the thousand, taking people\'s savings with them, and factories closed. Families lost their '
           'homes and lived in shacks in camps they called Hoovervilles, after the president, Herbert Hoover, and queued '
           'for bread and soup.',
           num='1 in 4', of='American workers had no job by 1933', y=1932),
      turn('Around the world',
           'American banks called in their loans abroad, and countries put up tariffs to protect their own industries, '
           'so world trade shrank by two thirds. In Germany, still paying for the last war, six million were out of work '
           'by 1932. Desperate voters turned to extremes, and in 1933 Adolf Hitler came to power.',
           y=1932, at='berlin'),
      figure('franklin-d-roosevelt', 'The New Deal',
             'Franklin D. Roosevelt, elected in 1932, told Americans that the only thing they had to fear was fear itself. '
             'His New Deal put millions to work building dams, roads and parks, protected people\'s bank savings, and '
             'began pensions for the old. Recovery was slow, and only the Second World War ended the slump.',
             y=1933, at='washington'),
      scene('The Dust Bowl',
            'On the southern Great Plains, years of drought turned ploughed-up prairie to dust. Huge black storms buried '
            'farms and blew dust as far as the Atlantic. Hundreds of thousands of families packed up and drove west to '
            'California, where they picked fruit for pennies, as John Steinbeck told in The Grapes of Wrath.',
            img='Dust Bowl', y=1935),
      work('Migrant Mother',
           'In 1936 the photographer Dorothea Lange, working for the government, stopped at a camp of pea pickers in '
           'California and took a few pictures of a worn-out mother of seven, Florence Owens Thompson, with her '
           'children. It became the face of the Depression.',
           img='Migrant Mother', y=1936),
      legacy('The Depression changed how governments think: most now accept that they must act to fight unemployment and '
             'protect savings in a crisis, as the economist John Maynard Keynes argued. It also showed how hard times can '
             'drive people to dictators, a lesson learned at terrible cost.',
             'Began with the Wall Street Crash of October 1929',
             'A quarter of Americans out of work by 1933',
             'It helped bring Hitler to power'),
      states=('United States', 'Germany', 'United Kingdom of Great Britain and Ireland', 'United Kingdom', 'Canada',
              'Australia'),
      wiki='Great Depression', at='new_york')

event('holodomor', 'The Holodomor', 'famine', (1932, 1933),
      "Stalin's seizure of farms and grain brought a famine that killed millions in Soviet Ukraine and beyond.",
      figure('joseph-stalin', 'Collective farms',
             'From 1929 Joseph Stalin forced the Soviet Union\'s peasants to give up their own farms and join huge '
             'collective farms run by the state. Millions resisted, killing their animals rather than hand them over. '
             'Better-off farmers, called kulaks, were shot or sent to Siberia by the hundred thousand.',
             kick='How it began', y=1929, at='moscow'),
      turn('Taking the grain',
           'In 1932 the harvest in Ukraine was poor, but Moscow kept raising the grain it demanded, and brigades searched '
           'houses and took everything, even seed. Taking a few ears of grain from a field could mean death or ten years '
           'in the camps, and villages that fell short were cut off from all goods.',
           y=1932, at=(32.0, 49.0), where='Ukraine'),
      cost('Hunger',
           'In the spring of 1933 people in the Ukrainian countryside were dying by the thousand every day. In January '
           'Stalin had banned starving peasants from leaving Ukraine to look for food, and all the while the Soviet '
           'Union went on selling grain abroad.',
           num='About 4 million', of='people died in Ukraine, by most estimates', y=1933, at=(32.0, 49.0),
           where='Ukraine'),
      figure(None, 'Gareth Jones',
             'A young Welsh reporter, Gareth Jones, walked through Ukrainian villages in March 1933 and told the world of '
             'the famine. Soviet officials denied it, and some Western reporters in Moscow, among them Walter Duranty of '
             'the New York Times, backed the denial. Jones was murdered in Inner Mongolia two years later.',
             img='Gareth Jones (journalist)', y=1933),
      scene('Kazakhstan',
            'Ukraine suffered most, but not alone. In Kazakhstan, where herding families were forced to settle on '
            'collective farms, perhaps a million and a half people, more than a third of all Kazakhs, died of hunger, '
            'and many more fled into China.',
            y=1932),
      legacy('For decades the Soviet Union denied that the famine had happened. Ukrainians call it the Holodomor, death by '
             'hunger, and every November they light candles in their windows to remember it. Ukraine and many other '
             'countries call it a genocide of the Ukrainian people; some historians see it as a crime against all Soviet '
             'peasants.',
             'Caused by the seizure of grain, 1932 and 1933',
             'Millions starved in Ukraine',
             'Remembered every November'),
      states=('USSR', 'Ukraine'), wiki='Holodomor', at=(32.0, 49.0), where='Ukraine')

event('chinese-civil-war', 'The Chinese Civil War', 'civil-war', (1927, 1949),
      "Chiang Kai-shek's Nationalists and Mao's Communists fought for China, on and off, for 22 years. The Communists won.",
      figure('chiang-kai-shek', 'The Shanghai massacre',
             'After Sun Yat-sen died, his Nationalist party, led by the general Chiang Kai-shek, set out with its '
             'Communist allies to beat the warlords and unite China. In April 1927, as his army took Shanghai, Chiang '
             'turned on the Communists and had thousands of them and their trade union allies killed. Civil war followed.',
             kick='How it began', y=1927, at='shanghai'),
      figure('mao-zedong', 'In the hills',
             'The Communists fled to the countryside. In the hills of Jiangxi, Mao Zedong, a farmer\'s son and former '
             'library assistant, built a little Soviet republic on the support of poor peasants, giving them land taken '
             'from landlords, and fought Chiang\'s armies with guerrilla tactics.',
             y=1931, at='ruijin'),
      scene('The Long March',
            'In 1934 Chiang\'s armies surrounded them, and about 86,000 Communists broke out and marched west and north, '
            'over mountains and rivers and through swamps, for a whole year. Fewer than 10,000 reached the caves of '
            'Yan\'an in the far north. On the way Mao became the party\'s leader, and the march became its founding '
            'legend.',
            img='Long March', y=1934, at='yanan'),
      turn('Against Japan',
           'In December 1936 one of Chiang\'s own generals kidnapped him at Xi\'an and made him agree to fight Japan '
           'alongside the Communists. When Japan invaded in 1937 the two sides fought it together, in name at least, '
           'while watching each other. Behind the Japanese lines the Communist armies grew to around a million fighters.',
           y=1936, at='xian'),
      battle('The last campaigns',
             'After Japan\'s defeat the civil war began again in 1946. Chiang had more men and American weapons, but his '
             'government was riddled with corruption and runaway prices, and many of his soldiers deserted. In 1948 and '
             '1949 the Communists won three huge campaigns in the north and centre, and crossed the Yangtze.',
             y=1948),
      turn("The People's Republic",
           'On 1 October 1949 Mao stood on the Gate of Heavenly Peace in Beijing and proclaimed the People\'s Republic of '
           'China. Chiang fled with some two million soldiers and refugees to the island of Taiwan, where his Republic '
           'of China lives on. No peace treaty was ever signed.',
           img='Proclamation of the People\'s Republic of China', y=1949, at='beijing'),
      legacy('The Communist victory made China the world\'s largest communist country and shaped Asia for the rest of the '
             'century. Taiwan and the mainland still have separate governments, and their future is one of the most '
             'dangerous questions in world politics.',
             'Began with the Shanghai massacre, 1927',
             'The Long March, 1934 to 1935',
             'The People\'s Republic was founded on 1 October 1949'),
      war='chinese-civil-war', wiki='Chinese Civil War')

event('spanish-civil-war', 'The Spanish Civil War', 'civil-war', (1936, 1939),
      "Spain's generals rose against its republic, and volunteers, communists and fascists from abroad came to fight.",
      scene('A divided republic',
            'Spain had become a republic in 1931, and it was split between left and right, town and country, the Church '
            'and its enemies. In February 1936 a left-wing Popular Front won the elections. In July a group of generals, '
            'among them Francisco Franco, rose in revolt, and the country split in two.',
            kick='How it began', y=1936, at='madrid'),
      figure('francisco-franco', 'The general',
             'Franco flew to Morocco to lead Spain\'s colonial army, and German and Italian planes carried his troops over '
             'the sea to Spain, the first big airlift in history. His Nationalists, backed by the Church, landowners and '
             'fascists, began a slow conquest, shooting tens of thousands of their enemies behind the lines.',
             y=1936),
      battle('They shall not pass',
             'In November 1936 Franco\'s army reached the edge of Madrid. Its people, with the first foreign volunteers, '
             'held the city under the slogan they shall not pass, and it held out until the very end of the war.',
             img='Siege of Madrid', y=1936, at='madrid'),
      scene('Volunteers',
            'Hitler and Mussolini sent Franco planes, tanks and soldiers, and Stalin armed the Republic. Some 35,000 '
            'volunteers from over 50 countries came to fight for the Republic in the International Brigades, and others, '
            'like the writer George Orwell, joined its militias. Both sides killed civilians; in Republican areas '
            'thousands of priests and nuns were murdered.',
            img='International Brigades', y=1937),
      figure('pablo-picasso', 'Guernica',
             'On 26 April 1937 German and Italian bombers attacked the Basque town of Guernica on market day and left it '
             'in flames. Pablo Picasso, in Paris, painted a huge black, white and grey picture of screaming women, a '
             'dying horse and a bull. Guernica became the most famous protest against war ever painted.',
             y=1937, at='guernica'),
      turn('The fall of the Republic',
           'The Republic\'s side was torn by feuds between communists, socialists and anarchists, and Franco\'s better '
           'armed forces slowly won. Barcelona fell in January 1939 and Madrid in March. Half a million Republicans fled '
           'over the mountains to France, many to be held in camps on the beaches.',
           y=1939, at='madrid'),
      cost('After the war',
           'Franco ruled Spain as a dictator until his death in 1975. Tens of thousands of his opponents were executed '
           'after the war, and hundreds of thousands passed through prisons and camps.',
           num='About 500,000', of='died in the war and the killings', y=1939),
      legacy('The war was a rehearsal for the Second World War, a testing ground for German and Italian bombers and tanks. '
             'Spain became a democracy again after Franco\'s death, and it still argues about how to remember the war and '
             'its mass graves.',
             'Began with a generals\' revolt in July 1936',
             'Volunteers came from over 50 countries',
             'Franco ruled until 1975'),
      war='spanish-civil-war', wiki='Spanish Civil War')

event('second-sino-japanese-war', 'The Second Sino-Japanese War', 'war', (1937, 1945),
      'Japan invaded China in 1937, and eight years of war killed perhaps 15 to 20 million Chinese.',
      scene('Manchuria',
            'In 1931 Japanese officers blew up a stretch of their own railway near Mukden, blamed Chinese soldiers, and '
            'used it as an excuse to seize all of Manchuria. Japan set up a puppet state there called Manchukuo, with the '
            'last Qing emperor, Puyi, at its head, and walked out of the League of Nations when it objected.',
            kick='How it began', y=1931, at='mukden'),
      turn('The Marco Polo Bridge',
           'On 7 July 1937 Japanese and Chinese troops exchanged fire at the Marco Polo Bridge outside Beijing, and this '
           'time Chiang Kai-shek decided to fight. Japan poured in troops. In Shanghai Chinese armies held out through '
           'three months of street fighting before they broke.',
           img='Marco Polo Bridge Incident', y=1937, at='beijing'),
      cost('Nanjing',
           'In December 1937 Japanese troops took Nanjing, then China\'s capital, and for six weeks murdered prisoners '
           'and civilians and raped tens of thousands of women. A few foreigners set up a safety zone that sheltered '
           'some 200,000 people. The number killed is still argued over; China puts it at 300,000.',
           num='Six weeks', of='of killing and rape in Nanjing', y=1937, at='nanjing'),
      scene('Trading space for time',
            'Chiang moved his government far up the Yangtze to Chongqing, behind the mountains, and traded space for '
            'time. In 1938 his armies broke the dikes of the Yellow River to stop the Japanese; the flood drowned or '
            'starved hundreds of thousands of Chinese farmers. Japanese bombers raided Chongqing again and again.',
            y=1938, at='chongqing'),
      scene('Over the Hump',
            'With its coast in Japanese hands, China was supplied by a mountain road from Burma, built largely by hand '
            'by some 200,000 workers. When Japan cut it in 1942, American planes flew supplies over the Himalayas, a '
            'route pilots called the Hump, and American volunteer pilots, the Flying Tigers, fought Japanese bombers.',
            img='Burma Road', y=1942),
      turn('Part of a world war',
           'When Japan attacked the United States at Pearl Harbor in December 1941, China\'s war became part of the '
           'Second World War, and a huge part of Japan\'s army stayed tied down in China to the end. Japan surrendered '
           'in August 1945, after the atomic bombs and a Soviet invasion of Manchuria.',
           y=1945),
      legacy('The war devastated China, leaving perhaps 15 to 20 million Chinese dead and tens of millions homeless. It '
             'weakened Chiang\'s government and helped the Communists win the civil war that followed. Memories of the '
             'war, and of Nanjing above all, still weigh on relations between China and Japan.',
             'Began at the Marco Polo Bridge, July 1937',
             'The massacre at Nanjing, December 1937',
             'Ended with Japan\'s surrender in 1945'),
      war='second-sino-japanese-war', wiki='Second Sino-Japanese War')

event('world-war-ii', 'The Second World War', 'world-war', (1939, 1945),
      'The deadliest war in history, fought from Europe to the Pacific, killed some 70 to 85 million people.',
      figure('adolf-hitler', 'The road to war',
             'Adolf Hitler, Germany\'s dictator since 1933, rearmed his country and swallowed Austria and Czechoslovakia '
             'while Britain and France, desperate to avoid a war, gave way. In August 1939 he made a pact with Stalin to '
             'split eastern Europe between them, and on 1 September his armies invaded Poland. Two days later Britain '
             'and France declared war.',
             kick='How it began', y=1939, at='berlin'),
      battle('Blitzkrieg',
             'In the spring of 1940 German tanks and dive-bombers overran Denmark, Norway, the Netherlands, Belgium and '
             'France in a few weeks. Over 330,000 British and French soldiers were rescued from the beaches of Dunkirk by '
             'warships and hundreds of little boats. France surrendered in June.',
             img='Dunkirk evacuation', y=1940, at='dunkirk'),
      figure('winston-churchill', 'Their finest hour',
             'Britain fought on alone under its new prime minister, Winston Churchill, who offered nothing but blood, '
             'toil, tears and sweat. In the Battle of Britain that summer its fighter pilots beat off the German air '
             'force, and Hitler put off his invasion. German bombs fell on London night after night in the Blitz.',
             y=1940, at='london'),
      battle('Barbarossa',
             'In June 1941 Hitler turned on Stalin and invaded the Soviet Union with over three million men, the largest '
             'invasion in history. By December his armies were at the gates of Moscow, and they besieged Leningrad, where '
             'some 800,000 people or more would die, most of hunger, in almost 900 days.',
             img='Operation Barbarossa', y=1941, at='moscow'),
      turn('Pearl Harbor',
           'On 7 December 1941 Japanese planes from six aircraft carriers attacked the American fleet at Pearl Harbor in '
           'Hawaii, killing some 2,400 Americans. The United States entered the war, and Hitler declared war on it too. '
           'Japan swept across Southeast Asia and the Pacific, taking Hong Kong, Malaya, Singapore, the Philippines and '
           'the Dutch East Indies.',
           img='Attack on Pearl Harbor', y=1941, at='pearl_harbor'),
      battle('Stalingrad',
             'In the summer of 1942 the Germans drove toward the Soviet oil fields and reached the city of Stalingrad on '
             'the Volga. The fighting went from street to street and house to house. In November the Red Army surrounded '
             'the German Sixth Army, and in February 1943 its last 91,000 starving men surrendered. The tide had turned.',
             img='Battle of Stalingrad', y=1942, at='stalingrad'),
      battle('D-Day',
             'On 6 June 1944, under General Dwight Eisenhower, more than 150,000 American, British, Canadian and other '
             'Allied soldiers landed on the beaches of Normandy, in the largest invasion ever made from the sea. By August '
             'Paris was free, and in the east the Red Army was driving the Germans back toward Berlin.',
             img='Normandy landings', y=1944, at='normandy'),
      cost('The deadliest war',
           'Most of the dead were civilians, killed by bombs, massacres, hunger and disease, and in the Holocaust, the '
           'Nazi murder of six million Jews. The Soviet Union lost some 27 million people, China perhaps 15 to 20 '
           'million, and Poland a sixth of all its people.',
           num='70 to 85 million', of='people died, most of them civilians', y=1944),
      turn('The end',
           'Hitler shot himself in his Berlin bunker as the Red Army closed in, and Germany surrendered on 8 May 1945. '
           'Japan fought on, until in August the United States dropped atomic bombs on Hiroshima and Nagasaki, killing '
           'some 200,000 people by the end of the year, and the Soviet Union invaded Manchuria. Japan surrendered on 15 '
           'August.',
           img='Atomic bombings of Hiroshima and Nagasaki', y=1945, at='hiroshima'),
      legacy('The war left Europe in ruins and two superpowers, the United States and the Soviet Union, facing each other '
             'in a cold war. The United Nations was founded to keep the peace, Nazi leaders were tried at Nuremberg, and '
             'the European empires began to end. The atomic bomb has hung over the world ever since.',
             'Began with the invasion of Poland, 1 September 1939',
             'The deadliest war in history',
             'Ended in August 1945, after the atomic bombs',
             'It gave birth to the United Nations'),
      war='world-war-ii', wiki='World War II')

event('holocaust', 'The Holocaust', 'genocide', (1933, 1945),
      'Nazi Germany and its helpers murdered six million Jews, two in every three in Europe, and millions of others.',
      scene('Laws of hate',
            'When Adolf Hitler took power in 1933, Germany\'s half a million Jews were thrown out of government jobs and '
            'their shops were boycotted. The Nuremberg Laws of 1935 took away their citizenship and banned marriage with '
            'other Germans. Many fled, but other countries let in few refugees.',
            kick='How it began', y=1935, at='nuremberg'),
      turn('The Night of Broken Glass',
           'On the night of 9 November 1938 Nazi mobs across Germany and Austria burned hundreds of synagogues, smashed '
           'thousands of Jewish shops and homes and killed scores of Jews, and some 30,000 Jewish men were sent to '
           'concentration camps. Afterwards Britain took in 10,000 Jewish children on the Kindertransport.',
           img='Kristallnacht', y=1938, at='berlin'),
      scene('The ghettos',
            'After conquering Poland, the Nazis forced its Jews into walled ghettos. In Warsaw some 400,000 people were '
            'packed into a few square kilometres, and tens of thousands died of hunger and typhus. In April 1943, as the '
            'last of them were being sent to their deaths, young Jewish fighters rose up and held out for a month.',
            img='Warsaw Ghetto Uprising', y=1940, at='warsaw'),
      cost('The death camps',
           'From 1941 SS killing squads shot Jews by the hundred thousand in the conquered Soviet lands. In January 1942 '
           'Nazi officials met at Wannsee to plan what they called the final solution. Jews from all over Europe were '
           'sent by train to death camps in Poland, Treblinka, Sobibor, Belzec and Auschwitz, and murdered in gas '
           'chambers.',
           num='Six million', of='Jews murdered, two in three in Europe', img='Auschwitz concentration camp', y=1942,
           at='auschwitz'),
      figure('anne-frank', 'The diary',
             'Anne Frank, a Jewish girl in Amsterdam, hid with her family for two years in rooms behind her father\'s '
             'office, and kept a diary of her hopes and fears. In August 1944 they were betrayed and sent to the camps. '
             'Anne died of typhus in Bergen-Belsen early in 1945, aged 15. Her father, the only one to survive, '
             'published her diary.',
             y=1944, at='amsterdam'),
      scene('Others they killed, and those who helped',
            'The Nazis also murdered Roma and Sinti people, perhaps a quarter of a million or more, disabled people, '
            'millions of Soviet prisoners and Polish civilians, and political enemies and gay men. Some people risked '
            'everything to help: in 1943 Danish fishermen ferried almost all of Denmark\'s Jews to safety in Sweden.',
            img='Rescue of the Danish Jews', y=1943),
      turn('Liberation',
           'As the Allies advanced, the SS drove prisoners on death marches. Soviet soldiers reached Auschwitz on 27 '
           'January 1945 and found some 7,000 prisoners left behind. British and American troops reaching Bergen-Belsen, '
           'Buchenwald and Dachau found piles of bodies and starving survivors, and their photographs showed the world.',
           y=1945, at='auschwitz'),
      legacy('The Holocaust was the largest genocide in history, planned and carried out by a modern state. Nazi leaders '
             'were tried at Nuremberg, and the world made genocide a crime. 27 January, the day Auschwitz was freed, is '
             'now Holocaust Remembrance Day, and survivors\' words still ask the world never to forget.',
             'Six million Jews were murdered',
             'Auschwitz was freed on 27 January 1945',
             'Never again'),
      states=('Germany', 'Poland', 'Netherlands', 'Hungary', 'Czechoslovakia', 'USSR', 'France', 'Romania', 'Greece',
              'Lithuania', 'Latvia', 'Austria', 'Italy', 'Belgium', 'Denmark', 'Yugoslavia', 'Germany (Soviet)',
              'Germany (UK)', 'Germany (USA)', 'Germany (France)'),
      wiki='The Holocaust', at='auschwitz')

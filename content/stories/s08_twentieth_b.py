from _lib import story, life, win, made, work, song, tale, legacy

story('benito-mussolini', 'The founder of fascism, dictator of Italy and ally of Hitler.',
    life("A blacksmith's son",
         'Benito Mussolini was born in 1883 in Predappio, in northern Italy, the son of a socialist blacksmith and a teacher. '
         'He was named after the Mexican president Benito Juárez. As a boy he was expelled from school for stabbing a '
         'classmate.',
         y=1883, at='predappio'),
    life('From socialist to fascist',
         'He became a socialist journalist, but was thrown out of the party in 1914 for backing the war. In 1919 in Milan he '
         'founded the fascist movement, whose black-shirted squads beat and killed socialists and trade unionists.',
         y=1919, at='milan'),
    life('The March on Rome',
         'In October 1922 thousands of Blackshirts marched on Rome. Rather than fight them, the king made Mussolini prime '
         "minister, at 39 the youngest in Italy's history.",
         img='March on Rome', y=1922, at='rome'),
    life('Il Duce',
         'By 1925 he was dictator, Il Duce, "the leader". He banned other parties, censored the press, and had opponents '
         'jailed, exiled or murdered, like the socialist politician Giacomo Matteotti.',
         y=1925, at='rome'),
    tale('The trains ran on time?',
         'His propaganda boasted that he had made the trains run on time. In fact much of the railway had been repaired '
         'before he came to power, and plenty of trains still ran late.',
         y=1930),
    life('Wars of conquest',
         'In 1935 he invaded Ethiopia, using poison gas. In 1940 he joined Hitler in the Second World War, but his armies '
         'were beaten in Greece and North Africa.',
         y=1936, at='addis_ababa'),
    life('Fall and rescue',
         "In 1943, after the Allies landed in Sicily, his own fascist council voted against him and the king had him "
         'arrested. German commandos freed him from a mountain hotel, and he ruled a puppet state in the north for Hitler.',
         y=1943, at=(13.56, 42.44), where='Gran Sasso'),
    life('The end',
         'In April 1945, fleeing toward Switzerland in a German uniform, he was caught by Italian partisans near Lake Como '
         'and shot. His body was hung upside down in a square in Milan.',
         y=1945, at='mezzegra'),
    legacy('Mussolini founded fascism: one-party rule, violent nationalism and worship of the leader, a model that Hitler '
           'copied. His wars brought Italy defeat and ruin.',
           'Founded fascism',
           'Dictator of Italy from 1922 to 1943',
           "Hitler's ally in the Second World War"),
)

story('chiang-kai-shek', 'The Nationalist leader who united China, fought Japan, then lost the mainland to Mao.',
    life("A salt merchant's son",
         'Chiang Kai-shek was born in 1887 in Xikou, a small town in eastern China, the son of a salt merchant. He trained as '
         'a soldier in Japan, and joined the revolution that overthrew the last emperor in 1911.',
         y=1887, at='xikou'),
    win('The Whampoa Academy',
        'In 1924 the revolutionary leader Sun Yat-sen made him head of a new military academy at Whampoa, to train officers '
        "for his Nationalist party's army.",
        img='Whampoa Military Academy', y=1924, at='whampoa'),
    life('Turning on the communists',
         'In 1927 in Shanghai he turned on his communist allies and had thousands of them killed. It began a civil war that '
         'lasted, on and off, for 22 years.',
         y=1927, at='shanghai'),
    win('Uniting China',
        'In his Northern Expedition, from 1926 to 1928, he defeated the warlords who had carved up China, and united most of '
        'the country under a Nationalist government in Nanjing.',
        img='Northern Expedition', y=1928, at='nanjing'),
    tale('Kidnapped',
         'In December 1936 two of his own generals kidnapped him at Xi\'an, and would not let him go until he agreed to stop '
         'fighting the communists and join them against Japan.',
         y=1936, at='xian'),
    win('War with Japan',
        'From 1937 he led China\'s long and bloody war against the Japanese invasion, from a wartime capital at Chongqing. '
        'In 1943 he met Roosevelt and Churchill in Cairo as one of the Allied leaders.',
        img='Cairo Conference', y=1943, at='cairo'),
    life('Losing the mainland',
         "After Japan's defeat the civil war with Mao's communists flared again. Corruption, soaring prices and defeats cost "
         'him the country, and in 1949 he fled to Taiwan with some two million soldiers and refugees.',
         y=1949, at='taipei'),
    life('Taiwan',
         "He ruled Taiwan under martial law until he died in 1975, still claiming to be China's rightful ruler, and thousands "
         'were jailed or executed. Its economy boomed, and after his death Taiwan became a democracy.',
         img='Chiang Kai-shek Memorial Hall', y=1975, at='taipei'),
    legacy('Chiang united China for a time and led its long war against Japan, but lost the mainland to the communists. '
           'The Republic of China he led lives on in Taiwan.',
           'Led the Nationalists and united most of China',
           "Led China's war against Japan",
           'Ruled Taiwan after 1949'),
)

story('adolf-hitler', 'The Nazi dictator who started the Second World War in Europe and ordered the Holocaust.',
    life('A failed artist',
         'Adolf Hitler was born in 1889 in Braunau am Inn, Austria, the son of a customs officer. He was twice turned down by '
         'the art academy in Vienna, and lived there in poverty, selling pictures he copied from postcards, and taking in the hatred of '
         "Jews in the city's politics.",
         y=1908, at='vienna'),
    life('The First World War',
         'He served as a messenger in the German army and was gassed. He blamed Germany\'s defeat on Jews and Marxists, '
         'spreading the lie that the army had been "stabbed in the back".',
         y=1918),
    life('The Nazi party',
         'In Munich he took over a small far-right party, the Nazis. In 1923 he tried to seize power in a coup that failed. '
         'In prison he wrote Mein Kampf, full of hatred for Jews and plans to conquer land in the east.',
         img='Beer Hall Putsch', y=1923, at='munich'),
    life('Dictator',
         'The Great Depression brought the Nazis millions of votes. In January 1933 Hitler was made chancellor. Within months '
         'he had banned all other parties, opened the first concentration camps and made himself dictator.',
         y=1933, at='berlin'),
    life('Persecution',
         'The Nuremberg Laws of 1935 stripped Jews of their rights as citizens. On Kristallnacht, in November 1938, mobs '
         'burned synagogues and smashed Jewish shops and homes across Germany.',
         y=1935, at='nuremberg'),
    life('War',
         'He rearmed Germany, took Austria and Czechoslovakia, and on 1 September 1939 invaded Poland, starting the Second '
         'World War in Europe. By 1941 his armies had conquered most of Europe, and then invaded the Soviet Union.',
         y=1939, at='warsaw'),
    life('The Holocaust',
         'In the Holocaust the Nazis murdered six million Jews, two of every three in Europe, in mass shootings and in death '
         'camps such as Auschwitz. They also murdered millions of others: Roma, disabled people, Poles and Soviet prisoners.',
         img='Auschwitz concentration camp', y=1942, at='auschwitz'),
    life('Defeat',
         'After defeats at Stalingrad and in Normandy, the Allied armies closed in. On 30 April 1945, with Soviet troops '
         'fighting in the streets of Berlin, he killed himself in his bunker. Germany surrendered a week later.',
         img='Führerbunker', y=1945, at='berlin'),
    legacy('Hitler started the deadliest war in history, in which some 70 to 85 million people died, and ordered the '
           'Holocaust. Germany today teaches this history so that it can never happen again.',
           'Dictator of Nazi Germany from 1933 to 1945',
           'Started the Second World War in Europe',
           'Responsible for the Holocaust'),
)

story('ho-chi-minh', 'The revolutionary who led Vietnam to independence from France.',
    life("A scholar's son",
         'Ho Chi Minh was born Nguyễn Sinh Cung in 1890, in a village in central Vietnam, then a French colony. His father '
         'was a scholar of Confucius.',
         y=1890, at='kim_lien'),
    life('Kitchen boy and sailor',
         'In 1911 he left Vietnam as a kitchen helper on a French ship, and stayed away for 30 years. He worked as a cook in '
         'London, it is said under a famous chef, and retouched photographs in Paris.',
         y=1913, at='london'),
    tale('The petition',
         'In 1919, at the peace conference at Versailles, he tried to hand the world leaders a petition asking for rights '
         'for the Vietnamese. It was ignored. A year later he became a communist.',
         y=1919, at='versailles'),
    life('Many names',
         'He worked for the communist movement in Moscow and China under dozens of false names, and was jailed in Hong Kong.',
         y=1931, at='hong_kong'),
    win('Independence',
        'In 1941 he came home and hid in a cave near the Chinese border, leading a movement to fight Japan and France. On 2 '
        'September 1945 in Hanoi he declared independence, quoting the American Declaration: "All men are created equal."',
        y=1945, at='hanoi'),
    win('Dien Bien Phu',
        'France fought to take back its colony. After eight years of war, his forces crushed the French at Dien Bien Phu in '
        '1954. Vietnam was split in two: a communist North led by Ho, and the South.',
        img='Battle of Dien Bien Phu', y=1954, at='dien_bien_phu'),
    life('Uncle Ho',
         'In the North his government took land from landlords, and thousands were executed. To many he was "Uncle Ho". He '
         'backed the war to take the South, where America sent its troops to fight.',
         y=1965, at='hanoi'),
    life('The mausoleum',
         'He died in 1969, six years before the North won the war and united the country. Saigon was renamed Ho Chi Minh '
         'City. He had asked to be cremated, but his body was embalmed and put on display in Hanoi.',
         img='Ho Chi Minh Mausoleum', y=1969, at='hanoi'),
    legacy("Ho Chi Minh led Vietnam's fight for independence from France and founded communist Vietnam. He is still "
           "honoured there as the father of the nation.",
           'Declared the independence of Vietnam',
           'Defeated France at Dien Bien Phu',
           'Founder of communist Vietnam'),
)

story('charles-de-gaulle', 'The general who led Free France in the Second World War and founded the Fifth Republic.',
    life('A tall soldier',
         'Charles de Gaulle was born in Lille in 1890. Nearly two metres tall, he became an army officer. In the First World '
         'War he was wounded three times, captured at Verdun, and tried to escape five times.',
         y=1890, at='lille'),
    life('A voice for tanks',
         'Between the wars he argued that France needed fast tank divisions, not lines of forts. Few in France listened, but '
         'the German generals did.',
         y=1934, at='paris'),
    win('The appeal of 18 June',
        'In June 1940, as France fell, he flew to London and spoke on BBC radio: "Whatever happens, the flame of French '
        'resistance must not and shall not go out." He led the Free French, and the government in France sentenced him to '
        'death.',
        img='Appeal of 18 June', y=1940, at='london'),
    win('Paris liberated',
        'On 26 August 1944 he walked down the Champs-Élysées through a million cheering Parisians. When snipers opened fire '
        'at Notre-Dame, he kept walking without flinching.',
        img='Liberation of Paris', y=1944, at='paris'),
    win('The Fifth Republic',
        'In 1958, with France close to civil war over Algeria, he returned to power and created the Fifth Republic, with a '
        'strong president. In 1962 he gave Algeria its independence.',
        y=1958, at='paris'),
    tale('They shoot like pigs',
         'Extremists who wanted to keep Algeria French tried to kill him several times. In 1962 gunmen riddled his car with '
         'bullets. He stepped out unhurt, and grumbled that they shot like pigs.',
         y=1962, at='paris'),
    tale('246 cheeses',
         '"How can you govern a country that has 246 kinds of cheese?" he once complained.',
         y=1962),
    life('A widow',
         'He survived the protests and strikes of May 1968, but resigned in 1969 after losing a vote, and went home to his '
         'village, Colombey. When he died in 1970, the new president said: "France is a widow."',
         y=1970, at='colombey'),
    legacy('De Gaulle kept France fighting in the Second World War, restored its pride, and created the Fifth Republic, '
           "still France's system of government.",
           'Led the Free French in the Second World War',
           'Founded the Fifth Republic',
           'Gave Algeria its independence'),
)

story('mao-zedong', "The communist who founded the People's Republic of China, whose campaigns cost tens of millions of lives.",
    life("A peasant's son",
         'Mao Zedong was born in 1893 in Shaoshan, in central China, the son of a well-off peasant, and quarrelled with his '
         'strict father. He trained as a teacher, and found Marxism while working in the library of Peking University.',
         y=1893, at='shaoshan'),
    life('Guerrilla war',
         'In 1921 he helped found the Chinese Communist Party. When Chiang Kai-shek turned on the communists in 1927, Mao led '
         'peasant fighters into the mountains, and began a guerrilla war.',
         y=1927, at='jinggangshan'),
    life('The Long March',
         'In 1934 the Nationalists drove the communists from their base. On the Long March they walked some 10,000 km in a '
         'year; of 86,000 who set out, fewer than 10,000 arrived. On the way, Mao became their leader.',
         img='Long March', y=1935, at='yanan'),
    life('The People\'s Republic',
         "After fighting Japan, then Chiang's Nationalists, on 1 October 1949 Mao proclaimed the People's Republic of China "
         'from the Gate of Heavenly Peace in Beijing.',
         y=1949, at='beijing'),
    life('The Great Leap Forward',
         "In 1958 he ordered a Great Leap Forward to overtake Britain's industry, with steel furnaces in backyards and giant "
         'farm communes. Harvests collapsed. In the famine that followed, some 15 to 45 million people died.',
         y=1959),
    life('The Cultural Revolution',
         'In 1966 he launched the Cultural Revolution. Teenage Red Guards, waving his Little Red Book, attacked teachers, '
         'officials and anything old. Temples and books were destroyed, schools closed, and hundreds of thousands died.',
         img='Cultural Revolution', y=1966, at='beijing'),
    tale('The swim',
         'In 1966, aged 72, he swam in the Yangtze River at Wuhan. State newspapers claimed he swam 15 km in about an hour, '
         'which would have been a world record.',
         y=1966, at='wuhan'),
    life('Nixon and the mausoleum',
         'In 1972 he welcomed the American president Nixon to Beijing. He died in 1976. His portrait still hangs over the '
         "Gate of Heavenly Peace, and his body lies in a tomb on the square.",
         y=1972, at='beijing'),
    legacy("Mao united China after a century of war, but his campaigns caused the deaths of tens of millions. China's "
           'rulers say he was "70 per cent right and 30 per cent wrong".',
           "Founded the People's Republic of China",
           'Led the Long March and the communist revolution',
           'Tens of millions died in his famine and purges'),
)

story('ruhollah-khomeini', 'The cleric who led the Iranian Revolution and founded the Islamic Republic.',
    life('A cleric from Khomein',
         'Ruhollah Khomeini was born in 1902 in the small town of Khomein, in Iran. His father was killed when he was a baby. '
         'He studied Islamic law and philosophy, and became a respected teacher in the holy city of Qom.',
         y=1902, at='khomein'),
    life('Against the Shah',
         "In 1963 he attacked the Shah's Western-style reforms and his ties to America and Israel. He was arrested, and in "
         '1964 sent into exile.',
         y=1963, at='qom'),
    life('Fourteen years in exile',
         'He lived in exile in Turkey, then for 13 years in the holy city of Najaf, in Iraq, and finally near Paris. His '
         'sermons were recorded on cassette tapes, smuggled into Iran and copied by the thousand.',
         y=1978, at='neauphle'),
    life('The revolution',
         'In 1978 vast protests and strikes spread across Iran, and in January 1979 the Shah fled. On 1 February Khomeini '
         'flew home to Tehran, where millions turned out to greet him.',
         img='Iranian Revolution', y=1979, at='tehran'),
    life('The Islamic Republic',
         'After a referendum he founded the Islamic Republic, with himself as Supreme Leader. Opponents, including many '
         'former allies, were jailed or executed, and women were made to cover their hair.',
         y=1979, at='tehran'),
    life('The hostages',
         'In November 1979 students stormed the American embassy in Tehran and held 52 Americans hostage for 444 days, with '
         "Khomeini's backing.",
         img='Iran hostage crisis', y=1979, at='tehran'),
    life('War with Iraq',
         'In 1980 Iraq invaded Iran. The war lasted eight years and killed hundreds of thousands. Khomeini accepted a '
         'ceasefire in 1988, saying it was worse than drinking poison. That year thousands of political prisoners were '
         'executed.',
         y=1988),
    life('The fatwa',
         'In 1989 he called for the death of the British writer Salman Rushdie over his novel The Satanic Verses. Khomeini '
         'died that June, and millions mourned at his funeral.',
         y=1989, at='tehran'),
    legacy("Khomeini led the revolution that ended Iran's monarchy and created the Islamic Republic, a state ruled by "
           'clerics that still governs Iran.',
           'Led the Iranian Revolution of 1979',
           'Founded the Islamic Republic of Iran',
           'Its first Supreme Leader'),
)

story('deng-xiaoping', "The small, tough leader who opened China's economy to the world.",
    life('Work and study in France',
         "Deng Xiaoping was born in 1904 in Guang'an, in Sichuan. At 16 he went to France on a work and study programme, "
         'worked in a car factory and as a kitchen hand, and joined the communists there.',
         y=1920, at='paris'),
    tale('Croissants and bridge',
         'He stood only about 1.5 m tall, and loved playing bridge. In France, it is said, he also came to love croissants.',
         y=1925, at='paris'),
    life('Revolutionary',
         "He marched on the Long March and was a top commander in the civil war. After 1949 he became one of Mao's most "
         'powerful officials.',
         y=1949, at='beijing'),
    life('Purged twice',
         'In the Cultural Revolution he was denounced and sent to work in a tractor factory. Red Guards hounded his son, who '
         'fell from a window and was left paralysed. He came back, was purged again in 1976, and came back again.',
         y=1969, at=(115.89, 28.68), where='Jiangxi'),
    win('Reform and opening up',
        'From 1978 he was China\'s leader. He let farmers sell their crops, opened China to foreign trade and money, and set '
        'up special economic zones like Shenzhen, then a small town. "It does not matter if a cat is black or white, as '
        'long as it catches mice."',
        img='Shenzhen', y=1980, at='shenzhen'),
    life('Tiananmen',
         'In 1989 students and workers filled Tiananmen Square demanding freedom. Deng backed martial law, and on 4 June '
         'troops and tanks cleared the square, killing hundreds, perhaps thousands.',
         img='1989 Tiananmen Square protests and massacre', y=1989, at='beijing'),
    win('One country, two systems',
        'He agreed with Britain that Hong Kong would return to China in 1997 under "one country, two systems". He died '
        'months before it did.',
        y=1984, at='hong_kong'),
    legacy("Deng's reforms made China the world's second largest economy and lifted hundreds of millions out of poverty, "
           'while keeping the Communist Party in total control.',
           "Opened China's economy to the world",
           'Lifted hundreds of millions out of poverty',
           'Ordered the crackdown at Tiananmen Square'),
)

story('j-robert-oppenheimer', 'The physicist who led the making of the first atomic bomb, and then warned the world about it.',
    life('A gifted boy',
         'Robert Oppenheimer was born in New York in 1904 to a wealthy family. At 12 he gave a talk to a club of rock '
         'collectors, who had not realised from his letters that he was a child.',
         y=1916, at='new_york'),
    tale('The poisoned apple',
         'Studying in Cambridge, unhappy and homesick, he is said to have left an apple laced with chemicals on his tutor\'s '
         "desk. No one ate it, and his parents talked the university out of expelling him.",
         y=1925, at='cambridge'),
    life('Teacher of physics',
         'At Berkeley, from 1929, he built the best school of theoretical physics in America. In 1939 he worked out how a '
         'collapsing star could form what we now call a black hole.',
         y=1939, at='berkeley'),
    life('Los Alamos',
         'In 1942 he was put in charge of the scientists of the secret Manhattan Project. He chose a remote mesa in New '
         'Mexico, Los Alamos, where thousands of people worked to build an atomic bomb before Germany could.',
         img='Los Alamos National Laboratory', y=1943, at='los_alamos'),
    made('Trinity',
         'On 16 July 1945 the first atomic bomb exploded in the New Mexico desert. Watching, he remembered words from a Hindu '
         'scripture: "Now I am become Death, the destroyer of worlds."',
         'Weeks later atomic bombs destroyed Hiroshima and Nagasaki, killing well over 100,000 people, and Japan '
         'surrendered. The nuclear age had begun.',
         img='Trinity (nuclear test)', y=1945, at=(-106.48, 33.68), where='Trinity site'),
    life('Blood on my hands',
         'After the war he argued for international control of atomic weapons, and opposed building the far more powerful '
         'hydrogen bomb. He told President Truman: "I feel I have blood on my hands."',
         y=1945, at='washington'),
    life('Humiliated',
         'In 1954, in the fear of communism, a government hearing took away his security clearance, over old left-wing '
         'friends and his opposition to the hydrogen bomb. In 2022 the American government reversed the decision.',
         y=1954, at='washington'),
    life('Last years',
         'He led the Institute for Advanced Study in Princeton, where Einstein worked. A heavy smoker, he died of throat '
         'cancer in 1967.',
         y=1960, at='princeton'),
    legacy('Oppenheimer led the making of the first atomic bomb, which ended the Second World War and changed the world '
           'for ever, and spent the rest of his life warning of its dangers.',
           'Led the Manhattan Project at Los Alamos',
           'Called the father of the atomic bomb',
           'Warned the world about nuclear weapons'),
)

story('mother-teresa', 'The nun who spent her life caring for the poorest of the poor in Calcutta.',
    life('A girl from Skopje',
         'Anjezë Gonxhe Bojaxhiu was born in 1910 in Skopje to an Albanian family. Her father died when she was eight. At 18 '
         'she left home to become a nun with the Sisters of Loreto in Ireland, and never saw her mother again.',
         y=1910, at='skopje'),
    life('A teacher in Calcutta',
         'In 1929 she was sent to India, took the name Teresa, and for nearly 20 years taught at a girls\' school in '
         'Calcutta.',
         y=1931, at='kolkata'),
    tale('A call on a train',
         'On 10 September 1946, on a train to Darjeeling, she felt what she called "a call within a call": to leave the '
         'convent and live among the poorest of the poor.',
         y=1946, at=(88.26, 27.04), where='Darjeeling'),
    win('The Missionaries of Charity',
        'In 1948 she put on a cheap white sari with blue borders and went to live in the slums. In 1950 she founded the '
        'Missionaries of Charity, a new order of nuns.',
        img='Missionaries of Charity', y=1950, at='kolkata'),
    win('A home for the dying',
        'In 1952 she opened a home where the dying poor, picked up from the streets, could die in peace and with dignity. '
        'Homes for people with leprosy, for orphans, and later for people with AIDS followed.',
        y=1952, at='kolkata'),
    win('The Nobel Peace Prize',
        'In 1979 she won the Nobel Peace Prize. She asked for the grand dinner in her honour to be cancelled, and the money '
        'given to the poor.',
        y=1979, at='oslo'),
    life('Doubts',
         'Critics said her homes gave poor medical care, and that she took money from dictators. Letters published after her '
         'death in 1997 showed that for nearly 50 years she had felt that God was absent.',
         y=1997, at='kolkata'),
    legacy('Mother Teresa became a worldwide symbol of care for the poorest. By her death her order ran more than 600 '
           'missions in over 120 countries. The Catholic Church made her a saint in 2016.',
           'Founded the Missionaries of Charity',
           'Won the Nobel Peace Prize',
           'Made a saint in 2016'),
)

story('alan-turing', 'The codebreaker who helped win the Second World War and imagined the modern computer.',
    life('The bicycle ride',
         'Alan Turing was born in London in 1912. At 13, on his first day at a new school, there was a general strike and no '
         'trains, so he cycled about 100 km on his own to get there.',
         y=1926, at=(-2.52, 50.95), where='Sherborne'),
    made('The Turing machine',
         'In 1936, at 24, he imagined a simple machine that reads and writes symbols on a tape, following a list of rules. '
         'He showed that such a machine could carry out any calculation that can be done step by step.',
         'It is the idea behind every computer: one machine that can do any task, given the right program.',
         img='Turing machine', y=1936, at='cambridge'),
    win('Breaking Enigma',
        'In the Second World War, at Bletchley Park, he led the team that broke the codes of the German navy\'s Enigma '
        'machines, and designed the Bombe, a machine that found each day\'s settings.',
        img='Bombe', y=1940, at='bletchley_park'),
    win('Shortening the war',
        'Reading the messages of the German submarines helped the Allies win the Battle of the Atlantic. Historians think the '
        'codebreakers shortened the war by perhaps two years, saving millions of lives.',
        y=1943, at='bletchley_park'),
    tale('A mug on a chain',
         'He chained his tea mug to a radiator so no one would take it, wore a gas mask in June to keep off hay fever, and ran '
         'marathons, almost fast enough for the 1948 Olympics.',
         y=1941, at='bletchley_park'),
    made('Can machines think?',
         'After the war he designed one of the first computers that stored its own programs, and in 1950 asked "Can '
         'machines think?" He proposed a test: can a machine chat so well that you cannot tell it from a person?',
         'It started the field of artificial intelligence, and the Turing test is still argued about today.',
         img='Turing test', y=1950, at='manchester'),
    life('Punished',
         'In 1952 he was convicted because he was gay, then a crime in Britain, and forced to take hormone injections. In '
         '1954 he died of cyanide poisoning, ruled a suicide. He was 41.',
         y=1954, at='wilmslow'),
    life('An apology',
         'In 2009 the British prime minister apologised for how he had been treated. In 2013 he was pardoned, and since 2021 '
         'his face has been on the 50-pound note.',
         y=2021, at='london'),
    legacy('Turing is a father of computer science and of artificial intelligence, and his codebreaking helped win the '
           'Second World War.',
           'Invented the idea of the universal computer',
           'Broke the Enigma code',
           'Started the field of artificial intelligence'),
)

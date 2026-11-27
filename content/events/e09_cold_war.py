from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('partition-of-india', 'The partition of India', 'independence', (1947, 1948),
      'British India won its freedom in 1947 as two nations, India and Pakistan, and millions fled across the new borders.',
      scene('Quit India',
            'For decades Gandhi\'s Congress party had led a mass movement of peaceful protest against British rule. In '
            '1942 it told the British to quit India, and its leaders were jailed. By 1945 Britain, worn out by the '
            'Second World War, was ready to leave. The question was what would come after.',
            kick='How it began', y=1942),
      figure('muhammad-ali-jinnah', 'Two nations',
             'Muhammad Ali Jinnah, leader of the Muslim League, feared that Muslims, a quarter of India\'s people, would '
             'be at the mercy of a Hindu majority, and he demanded a separate homeland, Pakistan. When the League called '
             'a day of action in August 1946, riots in Calcutta killed thousands, and the violence spread.',
             y=1946, at='calcutta'),
      figure('jawaharlal-nehru', 'At the stroke of midnight',
             'The last viceroy, Lord Mountbatten, brought the handover forward by almost a year. At midnight on 15 August '
             '1947 India became free, with Jawaharlal Nehru as its prime minister. He told the assembly that at the stroke '
             'of the midnight hour, while the world slept, India would awake to life and freedom. Pakistan had become '
             'free the day before.',
             y=1947, at='delhi'),
      scene('The line',
            'The new border was drawn in five weeks by Cyril Radcliffe, a British lawyer who had never been to India, '
            'with old maps and census figures. It cut the provinces of Punjab and Bengal in two, and it was only made '
            'public two days after independence. Pakistan was born in two parts, 1,600 kilometres apart.',
            y=1947),
      cost('The great migration',
           'Hindus and Sikhs fled east out of Pakistan, and Muslims fled west out of India, in the largest mass '
           'migration in history. Trains arrived full of the dead. Mobs on every side murdered, burned and abducted, and '
           'somewhere between a few hundred thousand and two million people were killed.',
           num='About 15 million', of='people forced from their homes', img='Partition of India', y=1947),
      figure('mahatma-gandhi', 'The light has gone out',
             'Gandhi refused to celebrate. He walked through riot-torn villages and fasted in Delhi until the killing '
             'there stopped. On 30 January 1948 a Hindu nationalist who thought him too soft on Muslims shot him dead at '
             'a prayer meeting. Nehru told the nation that the light had gone out of their lives.',
             y=1948, at='delhi'),
      scene('Kashmir',
            'The princely state of Kashmir, mostly Muslim but ruled by a Hindu maharaja, joined India in October 1947 '
            'when raiders from Pakistan invaded. India and Pakistan fought their first war over it, and a ceasefire line '
            'in 1949 left it divided. They have fought over it again and again since.',
            y=1948),
      legacy('Partition gave freedom to a fifth of humanity, and India became the world\'s largest democracy. But it left '
             'wounds that have never healed: the memories of 1947, the quarrel over Kashmir, and a rivalry between two '
             'nuclear-armed neighbours. In 1971 East Pakistan broke away to become Bangladesh.',
             'Independence at midnight, 15 August 1947',
             'About 15 million people fled their homes',
             'Gandhi was murdered in January 1948'),
      states=('India', 'Pakistan', 'Bangladesh'), wiki='Partition of India', at='delhi')

event('arab-israeli-war-1948', 'The 1948 Arab-Israeli War', 'war', (1947, 1949),
      'Israel declared its independence and won the war that followed. For Palestinians it was the Nakba, the catastrophe.',
      scene('The Mandate',
            'After the First World War Britain ruled Palestine, where Arabs were the majority and Jewish immigrants, '
            'fleeing persecution in Europe, a growing minority. After the Holocaust many more Jews sought a homeland '
            'there. Arabs and Jews both claimed the land, and both fought the British. In 1947 Britain handed the problem '
            'to the United Nations.',
            kick='How it began', y=1947, at='jerusalem'),
      turn('Partition',
           'In November 1947 the UN voted to split Palestine into a Jewish state and an Arab state, with Jerusalem under '
           'international rule. Jewish leaders accepted; Arab leaders rejected it as unjust to the Arab majority. '
           'Fighting broke out at once between Jewish and Arab forces.',
           y=1947, at='new_york'),
      figure('david-ben-gurion', 'Independence',
             'On 14 May 1948, as the last British troops left, David Ben-Gurion read out Israel\'s declaration of '
             'independence in a museum in Tel Aviv. The United States and the Soviet Union recognised the new state '
             'within days. The next morning the armies of Egypt, Jordan, Syria and Iraq invaded.',
             y=1948, at='tel_aviv'),
      cost('The Nakba',
           'Some 700,000 Palestinian Arabs, more than half of them, fled or were driven from their homes, and hundreds of '
           'their villages were emptied and later destroyed. Massacres, like the one at Deir Yassin in April 1948, '
           'spread terror. Israel did not let the refugees return.',
           num='About 700,000', of='Palestinians fled or were driven out', img='Nakba', y=1948),
      battle('Jerusalem',
             'The fiercest fighting was for Jerusalem. Jewish forces broke the siege of the Jewish part of the city by '
             'building a new road through the hills, while Jordan\'s Arab Legion held the Old City and drove out its '
             'Jewish quarter. When the war ended, the city was split between Israel and Jordan.',
             y=1948, at='jerusalem'),
      turn('The armistice lines',
           'In 1949 Israel signed truces with each of its neighbours. It now held about three quarters of the old '
           'Mandate, more than the UN plan had given it. Jordan held the West Bank and east Jerusalem, and Egypt the Gaza '
           'Strip, where tens of thousands of refugees lived in camps. No peace treaties followed.',
           y=1949),
      scene('The Jews of the Arab world',
            'In the years after the war some 850,000 Jews left or were driven from Arab countries, from Iraq to Morocco, '
            'where their families had lived for centuries. Most of them settled in Israel.',
            y=1950),
      legacy('Israel\'s war of independence is the founding story of the Jewish state, a refuge after the Holocaust. For '
             'Palestinians the Nakba is the start of a story of exile and occupation that has not ended. The refugees and '
             'their descendants, now millions, and the question of who rules the land are at the heart of the conflict '
             'today.',
             'Israel declared independence on 14 May 1948',
             'About 700,000 Palestinians became refugees',
             'The conflict over the land goes on'),
      war='arab-israeli-war-1948', wiki='1948 Arab–Israeli War')

event('korean-war', 'The Korean War', 'war', (1950, 1953),
      "Communist North Korea invaded the South, and the world's powers fought for three years to end where they began.",
      scene('A line on the map',
            'When Japan surrendered in 1945, two young American officers, working with a magazine map, chose the 38th '
            'parallel to divide Korea: Soviet troops would take the surrender north of it, Americans south of it. The '
            'line hardened into two states, the communist North under Kim Il Sung and the South under Syngman Rhee.',
            kick='How it began', y=1945),
      figure('kim-il-sung', 'The invasion',
             'With Stalin\'s blessing, Kim Il Sung sent his Soviet-armed army across the line on 25 June 1950. Seoul fell '
             'in three days, and the South\'s forces and their few American allies were pushed back into a small corner '
             'around the port of Busan.',
             y=1950, at='seoul'),
      battle('Inchon',
             'The United Nations sent an army led by the United States, with soldiers from 16 countries. In September '
             'General Douglas MacArthur landed behind the North Korean lines at Inchon, in a daring attack from the sea, '
             'and took back Seoul. UN forces then drove north almost to the Chinese border.',
             img='Battle of Inchon', y=1950, at='incheon'),
      turn('China comes in',
           'In late October hundreds of thousands of Chinese soldiers crossed the Yalu River in secret. They struck in '
           'the freezing mountains and drove the UN forces back south of Seoul. When MacArthur called for bombing China, '
           'even with atomic bombs, President Truman fired him.',
           y=1950),
      cost('Stalemate',
           'From 1951 the war bogged down into trench fighting near the 38th parallel, much like the First World War, '
           'while peace talks dragged on for two years, mainly over prisoners who did not want to go home. American '
           'bombing flattened almost every town in the North.',
           num='About 3 million', of='died, most of them Korean civilians', y=1952),
      turn('Armistice',
           'An armistice was signed at Panmunjom on 27 July 1953. The new border, close to the old line, became the most '
           'heavily guarded in the world, with a demilitarised zone four kilometres wide between the two Koreas. No '
           'peace treaty has ever been signed.',
           y=1953, at='panmunjom'),
      legacy('Korea is still divided. The South grew into one of the world\'s richest democracies, while the North became '
             'a closed dictatorship ruled by Kim\'s son and grandson, with nuclear weapons. Millions of families were '
             'split by the war, and few have ever seen their relatives across the line again.',
             'Began on 25 June 1950',
             'Soldiers from 16 nations fought for the UN',
             'Ended in a truce, not a peace, in 1953'),
      states=("Korea, Democratic People's Republic of", 'Korea, Republic of'), war='korean-war', wiki='Korean War')

event('civil-rights-movement', 'The civil rights movement', 'change', (1954, 1968),
      'Black Americans and their allies used marches, boycotts and the courts to end segregation in the United States.',
      scene('Separate and unequal',
            'Ninety years after slavery ended, Black Americans in the South still lived under Jim Crow laws that kept '
            'them in separate schools, seats and waiting rooms, and most were stopped from voting. In 1954 the Supreme '
            'Court ruled, in Brown v. Board of Education, that separate schools for Black and white children broke the '
            'Constitution.',
            kick='How it began', y=1954, at='washington'),
      scene('Emmett Till',
            'In August 1955 Emmett Till, a 14-year-old boy from Chicago visiting Mississippi, was kidnapped and murdered '
            'for supposedly whistling at a white woman. His mother insisted on an open coffin, so the world could see '
            'what had been done to him. An all-white jury freed the killers, who later admitted it.',
            y=1955),
      figure('rosa-parks', 'The bus boycott',
             'In December 1955 in Montgomery, Alabama, Rosa Parks refused to give up her seat on a bus to a white man and '
             'was arrested. Black people boycotted the city\'s buses for over a year, led by a 26-year-old minister, '
             'Martin Luther King Jr., until the Supreme Court ruled segregation on buses illegal.',
             y=1955, at='montgomery'),
      scene('Sit-ins and freedom rides',
            'In 1960 four Black students sat down at a whites-only lunch counter in Greensboro, North Carolina, and would '
            'not leave. Sit-ins spread across the South. In 1961 Black and white Freedom Riders rode buses together into '
            'the Deep South; one bus was firebombed, and riders were beaten by mobs.',
            y=1960, at='greensboro'),
      figure('martin-luther-king-jr', 'I have a dream',
             'In Birmingham, Alabama, in 1963, police turned fire hoses and dogs on marching children, and the pictures '
             'shocked the nation. That August a quarter of a million people marched on Washington, where King spoke of '
             'his dream that his children would one day be judged by the content of their character, not the colour of '
             'their skin.',
             y=1963, at='washington'),
      turn('The new laws',
           'The Civil Rights Act of 1964 banned segregation in public places and discrimination at work. In March 1965 '
           'state troopers beat peaceful marchers on a bridge in Selma, Alabama, on a day called Bloody Sunday, and '
           'months later the Voting Rights Act protected Black Americans\' right to vote.',
           img='Selma to Montgomery marches', y=1965, at='selma'),
      turn('Memphis',
           'On 4 April 1968 King was shot dead on a motel balcony in Memphis, Tennessee, where he had gone to support '
           'striking rubbish collectors. Riots broke out in more than a hundred cities. Malcolm X, who had argued that '
           'Black people must defend themselves by any means necessary, had been murdered three years before.',
           y=1968, at='memphis_tn'),
      legacy('The movement ended legal segregation and won Black Americans the vote in the South, and its peaceful '
             'methods inspired movements for the rights of women, gay people and others around the world. But gaps in '
             'wealth, housing, policing and justice did not vanish, and the struggle goes on.',
             'Brown v. Board of Education, 1954',
             'The Montgomery bus boycott, 1955',
             'The Civil Rights Act, 1964',
             'The Voting Rights Act, 1965'),
      states=('United States',), wiki='Civil rights movement', img='March on Washington for Jobs and Freedom',
      at='montgomery')

event('cuban-revolution', 'The Cuban Revolution', 'revolution', (1953, 1961),
      "Fidel Castro's guerrillas overthrew a dictator, and Cuba became a communist state 150 kilometres from the United States.",
      figure('fulgencio-batista', 'The dictator',
             'In 1952 Fulgencio Batista seized power in Cuba in a coup. His Havana was a playground of casinos run by '
             'American gangsters, while many Cubans in the countryside lived in poverty, and American companies owned '
             'much of the island\'s sugar, mines and land.',
             kick='How it began', y=1952, at='havana'),
      figure('fidel-castro', 'History will absolve me',
             'On 26 July 1953 a young lawyer, Fidel Castro, led about 160 rebels in an attack on the Moncada army barracks '
             'in Santiago de Cuba. It failed, and most were killed or captured. At his trial Castro spoke for hours and '
             'ended with the words history will absolve me. He was let out in an amnesty two years later.',
             y=1953, at='santiago_de_cuba'),
      scene('The Granma',
            'In December 1956 Castro sailed back from Mexico with 82 men crammed onto an old yacht, the Granma. Most were '
            'killed or captured soon after landing, but a handful escaped into the Sierra Maestra mountains, among them '
            'Castro\'s brother Raúl and an Argentine doctor, Che Guevara.',
            y=1956, at='sierra_maestra'),
      figure('che-guevara', 'Into Havana',
             'From the mountains the rebels won over the peasants and fought Batista\'s army, which lost heart. In December '
             '1958 Che Guevara\'s column captured an armoured train at Santa Clara. On New Year\'s Eve Batista fled the '
             'country, and in January 1959 Castro\'s bearded rebels rode into Havana in triumph.',
             y=1958, at='havana'),
      turn('A communist state',
           'Castro took over American-owned land, sugar mills, banks and oil refineries, and had hundreds of Batista\'s '
           'men executed. When the United States cut off trade, he turned to the Soviet Union, which bought Cuba\'s sugar '
           'and sold it oil. In 1961 he declared that Cuba was socialist.',
           y=1960, at='havana'),
      battle('The Bay of Pigs',
             'In April 1961 some 1,400 Cuban exiles, trained and armed by the American CIA, landed at the Bay of Pigs to '
             'overthrow Castro. The rising they hoped for never came, and within three days they were killed or captured. '
             'It was a humiliation for the new American president, John F. Kennedy.',
             img='Bay of Pigs Invasion', y=1961, at='bay_of_pigs'),
      legacy('Castro ruled Cuba for almost 50 years. His government gave Cubans free schools and health care and wiped out '
             'illiteracy, but jailed its critics and allowed no free elections, and over a million Cubans left, many for '
             'Florida. The American embargo still stands, and the Communist Party still rules.',
             'The Moncada attack, 26 July 1953',
             'Batista fled on New Year\'s Day 1959',
             'The Bay of Pigs invasion failed in 1961'),
      war='cuban-revolution', wiki='Cuban Revolution')

event('space-race', 'The space race', 'space', (1957, 1975),
      'The Soviet Union and the United States raced into space, from the first satellite to footprints on the Moon.',
      turn('Sputnik',
           'On 4 October 1957 the Soviet Union launched Sputnik 1, a shiny metal ball the size of a beach ball, the first '
           'artificial satellite. Its beeping radio signal could be picked up around the world. Americans were shocked '
           'that their Cold War rival had beaten them, and might reach them with nuclear missiles too.',
           kick='How it began', img='Sputnik 1', y=1957, at='baikonur'),
      tale('Laika',
           'A month later Sputnik 2 carried a passenger: Laika, a stray dog from the streets of Moscow. She was the first '
           'animal to circle the Earth, but there was no way to bring her back, and she died within hours from the heat. '
           'In 1960 two more space dogs, Belka and Strelka, came home safely.',
           img='Laika', y=1957, at='baikonur'),
      figure('yuri-gagarin', 'The first human in space',
             'On 12 April 1961 Yuri Gagarin, a 27-year-old Soviet pilot and the son of a carpenter, flew once around the '
             'Earth in his Vostok capsule, in 108 minutes. As he lifted off he called out, let\'s go. He became the most '
             'famous man in the world. In 1963 Valentina Tereshkova became the first woman in space.',
             y=1961, at='baikonur'),
      figure('john-f-kennedy', 'We choose to go to the Moon',
             'President John F. Kennedy answered with a promise: Americans would land a man on the Moon and bring him home '
             'before the decade was out. In Houston in 1962 he said they would go not because it was easy, but because it '
             'was hard. The Apollo programme came to employ some 400,000 people.',
             y=1962, at='houston'),
      cost('The price',
           'In January 1967 a fire swept through the Apollo 1 capsule during a test on the launch pad, killing the '
           'astronauts Gus Grissom, Ed White and Roger Chaffee. Months later the Soviet cosmonaut Vladimir Komarov died '
           'when his capsule\'s parachute failed.',
           num='Four', of='astronauts and cosmonauts killed in 1967', y=1967, at='cape_canaveral'),
      figure('neil-armstrong', 'One small step',
             'On 20 July 1969 the lunar module Eagle landed on the Moon\'s Sea of Tranquillity, and Neil Armstrong stepped '
             'down and called it one small step for a man, one giant leap for mankind. Buzz Aldrin joined him, while '
             'Michael Collins circled overhead. Some 600 million people watched on television.',
             y=1969),
      made('What the race left',
           'Rockets and satellites, fuel cells and tiny computers for spacecraft, and the first pictures of the whole Earth '
           'from space, like Earthrise, taken from Apollo 8 in 1968.',
           'Satellites now carry phone calls and weather forecasts and tell us where we are, and the pictures of a small '
           'blue Earth helped start the movement to protect the environment.',
           img='Earthrise', y=1968),
      turn('A handshake in orbit',
           'Six Apollo crews walked on the Moon until 1972, twelve men in all. In 1975 an American Apollo and a Soviet '
           'Soyuz spacecraft docked in orbit, and their commanders shook hands through the hatch. The race was over, and '
           'the rivals began to work together in space.',
           img='Apollo–Soyuz', y=1975),
      legacy('The space race was a contest of the Cold War, fought with rockets built to carry bombs, but it gave humanity '
             'its first steps off the Earth. No one has walked on the Moon since 1972, but people have lived in space '
             'without a break since 2000, on the International Space Station.',
             'Sputnik, 4 October 1957',
             'Gagarin, the first person in space, 1961',
             'The first Moon landing, 20 July 1969'),
      states=('USSR', 'United States'), wiki='Space Race', img='Apollo 11', at='cape_canaveral')

event('african-independence', 'Africa wins its freedom', 'independence', (1956, 1980),
      'In about twenty years almost all of Africa threw off European rule, sometimes in peace and sometimes by war.',
      figure('kwame-nkrumah', 'Ghana',
             'In 1957 the Gold Coast became Ghana, the first colony south of the Sahara to win its independence. Its '
             'leader, Kwame Nkrumah, who had led strikes and been jailed by the British, told the crowds at midnight that '
             'Ghana was free for ever, and that its freedom meant nothing unless all of Africa was free.',
             kick='How it began', y=1957, at='accra'),
      turn('The year of Africa',
           'In 1960 alone seventeen African countries became independent, most of them from France, among them Nigeria, '
           'Senegal, Mali, Madagascar and the Congo. The British prime minister Harold Macmillan told South Africa\'s '
           'parliament that a wind of change was blowing through the continent.',
           y=1960),
      figure('patrice-lumumba', 'The Congo',
             'Belgium left the Congo in haste in 1960, with hardly any Congolese trained to run it. The young prime '
             'minister, Patrice Lumumba, made a fiery speech about colonial abuses in front of the Belgian king. Within '
             'weeks the army mutinied and a mineral-rich province broke away. Lumumba was overthrown, and in 1961 he was '
             'murdered with Belgian help.',
             y=1960, at='kinshasa'),
      battle('Algeria',
             'France fought hard to keep Algeria, home to a million European settlers. From 1954 the National Liberation '
             'Front fought a war of bombings and ambushes, and the French army answered with torture and mass arrests. '
             'Hundreds of thousands died. In 1962 President de Gaulle let Algeria go, and almost all the settlers fled to '
             'France.',
             img='Algerian War', y=1962, at='algiers'),
      figure('jomo-kenyatta', 'Kenya',
             'In Kenya the Mau Mau rising of the 1950s was crushed with great brutality, and tens of thousands of Kikuyu '
             'were held in camps. Yet the British let Jomo Kenyatta, whom they had jailed as its leader, out of prison, '
             'and in 1963 he became the first leader of an independent Kenya.',
             y=1963, at='nairobi'),
      scene('The last empires',
            'Portugal, a dictatorship, fought long wars to keep Angola, Mozambique and Guinea-Bissau, until its own army '
            'overthrew the government in 1974. The colonies were free by 1975. In Rhodesia a white minority held on until '
            '1980, when the country became Zimbabwe.',
            y=1975),
      legacy('Independence gave Africans their own flags and governments, and in 1963 they founded the Organisation of '
             'African Unity. But the new states inherited colonial borders, economies built to send raw goods abroad and '
             'few trained people, and many fell into coups, one-party rule and civil wars. Today Africa is the youngest '
             'continent.',
             'Ghana led the way in 1957',
             'Seventeen countries became free in 1960',
             'Portugal let go of its colonies in 1975'),
      states=('Ghana', 'Gold Coast', 'Algeria', 'Angola', 'Angola (Portugal)', 'Benin', 'Botswana', 'Burkina Faso',
              'Burundi', 'Cameroon', 'Central African Republic', 'Chad', 'Congo', 'Equatorial Guinea', 'Gabon',
              'Gambia, The', 'Guinea', 'Guinea-Bissau', 'Guinea-Bissau (Portugal)', 'Ivory Coast', 'Kenya', 'Lesotho',
              'Libya', 'Madagascar', 'Madagascar (France)', 'Malawi', 'Nyasaland', 'Mali', 'Mauritania', 'Morocco',
              'Mozambique', 'Mozambique (Portugal)', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Sierra Leone',
              'Somalia', 'Sudan', 'Swaziland', 'Tanzania, United Republic of', 'Togo', 'Tunisia', 'Uganda', 'Zaire',
              'Zambia', 'Northern Rhodesia', 'Zimbabwe', 'Rhodesia', 'France', 'United Kingdom', 'Belgium', 'Portugal'),
      wiki='Decolonisation of Africa', at='accra')

event('great-leap-forward', 'The Great Leap Forward', 'famine', (1958, 1962),
      "Mao's plan to make China an industrial giant in a few years brought the deadliest famine in history.",
      figure('mao-zedong', 'Overtaking Britain',
             'In 1958 Mao Zedong launched a campaign to overtake Britain\'s industry within fifteen years. Peasants were '
             'herded into huge people\'s communes, where they ate in shared dining halls and gave up their land, their '
             'tools and even their cooking pots.',
             kick='How it began', y=1958, at='beijing'),
      scene('Backyard furnaces',
            'Across the country millions built little backyard furnaces to make steel, feeding them pots, pans, door '
            'hinges and tools and burning whole forests for fuel. Most of what came out was useless lumps of iron. '
            'Meanwhile crops rotted in the fields, because the farmers were busy at the furnaces.',
            y=1958),
      tale('Kill the sparrows',
           'Sparrows ate grain, so Mao declared them pests. People banged pots and drums day and night so that the birds '
           'could not land, until they dropped dead from exhaustion. With the sparrows gone, locusts and other insects '
           'multiplied and ate even more of the crops.',
           y=1958),
      figure('peng-dehuai', 'A letter to Mao',
             'Local officials, afraid to look disloyal, reported impossible harvests, and the state took grain on the '
             'strength of their boasts, leaving villages with nothing. When Marshal Peng Dehuai wrote to Mao in 1959 '
             'about the hunger, he was purged, and after that no one dared to speak.',
             y=1959),
      cost('The great famine',
           'From 1959 to 1961 the countryside starved. People ate tree bark, grass and clay. Officials beat or killed '
           'farmers caught hiding food, and all the while China went on selling grain abroad.',
           num='15 to 45 million', of='people died, by different estimates', y=1960, at='xinyang',
           where='Xinyang, Henan'),
      scene('Seven parts man-made',
            'In 1961 the leaders quietly ended the campaign. Liu Shaoqi, the head of state, told a party meeting in 1962 '
            'that the disaster was three parts nature and seven parts man-made. Mao stepped back from daily power, but '
            'he never forgave his critics, and four years later he turned on them.',
            y=1962),
      legacy('The Great Leap Forward caused the deadliest famine in history. For decades it was barely spoken of in China, '
             'where it is called the three years of difficulty and blamed largely on bad weather. Its memory helped '
             'convince later leaders to give the land back to farming families.',
             'Launched by Mao in 1958',
             'Steel from backyard furnaces',
             'Tens of millions starved, 1959 to 1961'),
      states=('China',), wiki='Great Leap Forward', at='beijing')

event('berlin-wall', 'The Berlin Wall', 'fall', (1961, 1990),
      'For 28 years a wall split Berlin and the world of the Cold War, until crowds broke through it in 1989.',
      scene('A divided city',
            'After the war Germany and its capital were split between the Allies. In 1948 Stalin closed the roads into '
            'West Berlin to starve it into his hands, and for almost a year American and British planes flew in food '
            'and coal, landing every few minutes. In 1949 Germany split into two states, the democratic West and the '
            'communist East.',
            kick='How it began', img='Berlin Blockade', y=1948, at='berlin'),
      turn('Overnight',
           'By 1961 some two and a half million East Germans had fled west, many of them through Berlin. On the night of '
           '13 August 1961 East German soldiers and workers strung barbed wire across the city, and soon a concrete wall '
           'went up. Families were cut off from each other overnight.',
           y=1961, at='berlin'),
      scene('The death strip',
            'The wall grew into two walls, with sand, watchtowers, dogs and searchlights between them. At least 140 '
            'people were killed trying to cross. Others escaped through tunnels, in secret car compartments, by hot-air '
            'balloon and over the rooftops. In 1962 Peter Fechter, 18, was shot and left to bleed to death in sight of '
            'the West.',
            y=1962, at='berlin'),
      figure('john-f-kennedy', 'Ich bin ein Berliner',
             'In June 1963 President Kennedy came to West Berlin and told a crowd of hundreds of thousands that every free '
             'person was a citizen of Berlin, and that he was proud to say, in German, I am a Berliner. In 1987 President '
             'Ronald Reagan stood at the wall and told the Soviet leader to tear it down.',
             y=1963, at='berlin'),
      figure('mikhail-gorbachev', 'The wind of change',
             'In the 1980s the Soviet leader Mikhail Gorbachev began reforms and made it clear he would not send tanks to '
             'keep Eastern Europe communist. In 1989 Poland held free elections, Hungary opened its border with Austria, '
             'and East Germans poured west through it. In Leipzig crowds marched every Monday, chanting we are the people.',
             y=1989),
      turn('9 November 1989',
           'On the evening of 9 November an East German spokesman, muddling a new rule, told reporters that people could '
           'cross the border at once. Thousands rushed to the checkpoints, and the overwhelmed guards opened the gates. '
           'Berliners danced on the wall and chipped pieces off it with hammers.',
           img='Fall of the Berlin Wall', y=1989, at='berlin'),
      turn('One Germany',
           'Less than a year later, on 3 October 1990, the two Germanys were united again. Within two years communist '
           'rule had ended across Eastern Europe, and the Soviet Union itself was gone.',
           y=1990, at='berlin'),
      legacy('The Berlin Wall was the symbol of the Cold War, the split between the communist East and the democratic '
             'West, and its fall was the moment that split ended. A few stretches still stand as memorials, and pieces of '
             'it are kept in museums around the world.',
             'Built overnight on 13 August 1961',
             'At least 140 people died trying to cross',
             'Opened on 9 November 1989',
             'Germany was united again in 1990'),
      states=('East Germany', 'West Germany', 'Germany', 'Germany (Soviet)', 'Germany (USA)', 'Germany (UK)',
              'Germany (France)'),
      wiki='Berlin Wall', at='berlin', label='Cold War')

event('cuban-missile-crisis', 'The Cuban Missile Crisis', 'crisis', (1962, 1962),
      'For thirteen days in 1962 the United States and the Soviet Union stood on the brink of nuclear war over Cuba.',
      figure('nikita-khrushchev', 'Missiles in Cuba',
             'The Soviet leader Nikita Khrushchev, angry at American nuclear missiles in Turkey and wanting to protect '
             'Castro after the Bay of Pigs, secretly sent nuclear missiles to Cuba in 1962, close enough to hit most '
             'American cities within minutes.',
             kick='How it began', y=1962, at='havana'),
      turn('The photographs',
           'On 14 October an American spy plane photographed missile sites being built in the Cuban countryside. '
           'President Kennedy and his advisers met in secret for a week. Some generals wanted to bomb the sites and '
           'invade. Kennedy chose a naval blockade instead, to stop more missiles arriving, and told the world on '
           'television on 22 October.',
           y=1962, at='washington'),
      scene('On the brink',
            'Soviet ships sailed toward the American line, and nuclear bombers were kept in the air. On 27 October an '
            'American spy plane was shot down over Cuba, and American ships dropped small depth charges on a Soviet '
            'submarine whose officers, cut off from Moscow, argued over firing a nuclear torpedo. One of them, Vasily '
            'Arkhipov, said no.',
            y=1962),
      turn('The deal',
           'On 28 October Khrushchev agreed to take the missiles away, in return for an American promise never to invade '
           'Cuba, and a secret promise to remove the American missiles from Turkey. The world breathed again. Castro, who '
           'had not been asked, was furious.',
           y=1962),
      made('The hotline',
           'A direct line between the White House and the Kremlin, set up in 1963 so the two leaders could talk at once '
           'in a crisis. It began as a teleprinter, not a red telephone.',
           'It was the first of many steps to stop the Cold War blowing up by accident, followed that same year by a '
           'treaty banning nuclear tests in the air, in space and under the sea.',
           y=1963),
      legacy('The crisis was the closest the world has come to nuclear war. It frightened both sides into talking, and '
             'the years after it brought the first treaties to limit nuclear weapons. It is still studied as a lesson in '
             'how leaders can step back from the edge.',
             'Thirteen days in October 1962',
             'Soviet missiles were found in Cuba',
             'Ended when Khrushchev took them away'),
      states=('Cuba', 'United States', 'USSR'), wiki='Cuban Missile Crisis', at='havana')

event('vietnam-war', 'The Vietnam War', 'war', (1955, 1975),
      'North Vietnam and guerrillas in the South fought the South and its American ally for twenty years, and won.',
      figure('ho-chi-minh', 'Dien Bien Phu',
             'Ho Chi Minh\'s Viet Minh had declared Vietnam independent of France in 1945, and fought the French for nine '
             'years. In 1954 they surrounded a French army in the valley of Dien Bien Phu and forced it to surrender. At '
             'a conference in Geneva Vietnam was split, for the time being, into a communist North and a South backed by '
             'the United States.',
             kick='How it began', y=1954, at='dien_bien_phu'),
      scene('The Viet Cong',
            'The elections promised for 1956 to unite the country never took place. In the South communist guerrillas, '
            'the Viet Cong, armed and led from the North along the Ho Chi Minh Trail through Laos and Cambodia, fought '
            'the government of Ngo Dinh Diem. The United States sent advisers, then thousands of troops.',
            y=1960),
      turn('Escalation',
           'In 1964 President Lyndon Johnson used a reported attack on American ships in the Gulf of Tonkin to win '
           'Congress\'s backing for war. In 1965 he sent in combat troops and began bombing the North. By 1968 more than '
           'half a million Americans were in Vietnam.',
           y=1965),
      turn('Tet',
           'In January 1968, at the Tet new year festival, communist forces attacked cities across the South, even the '
           'American embassy in Saigon. They were beaten back with huge losses, but Americans had been told the war was '
           'being won, and the shock turned many against it. In March Johnson said he would not run again.',
           img='Tet Offensive', y=1968, at='hue'),
      cost('The bombs',
           'In March 1968 American soldiers killed some 500 unarmed villagers, most of them women, children and old '
           'people, at My Lai. Over Vietnam, Laos and Cambodia American planes dropped more bombs than in the whole of '
           'the Second World War, and sprayed forests with Agent Orange, a poison whose harm is still felt.',
           num='1 to 3 million', of='Vietnamese died, and 58,000 Americans', y=1968),
      scene('Protest',
            'It was the first war watched on television, and at home the protests grew. Hundreds of thousands marched, '
            'young men burned their call-up papers, and in 1970 soldiers of the National Guard shot dead four students at '
            'a protest at Kent State University in Ohio. President Richard Nixon began to bring the troops home, while '
            'bombing harder.',
            y=1970),
      turn('The fall of Saigon',
           'A peace deal in 1973 let the last American troops leave. Two years later the North attacked again, and on 30 '
           'April 1975 its tanks crashed through the gates of the presidential palace in Saigon, as American helicopters '
           'lifted the last people from the rooftops. Saigon was renamed Ho Chi Minh City.',
           img='Fall of Saigon', y=1975, at='saigon'),
      legacy('Vietnam was united under communist rule, and hundreds of thousands of boat people later fled by sea. In the '
             'United States the defeat left deep wounds and a distrust of government. Today the two countries trade and '
             'talk as friends, and a black granite wall in Washington carries the names of the 58,000 Americans who died.',
             'France was beaten at Dien Bien Phu, 1954',
             'Over half a million Americans were there by 1968',
             'Saigon fell on 30 April 1975'),
      states=('Laos', 'Cambodia'), war='vietnam-war', wiki='Vietnam War')

event('cultural-revolution', 'The Cultural Revolution', 'revolution', (1966, 1976),
      'Mao set millions of young Red Guards against teachers, officials and the old ways, and China was in chaos for ten years.',
      figure('mao-zedong', 'Bombard the headquarters',
             'After the disaster of the Great Leap Forward, Mao felt pushed aside by party leaders like Liu Shaoqi and '
             'Deng Xiaoping. In 1966, aged 72, he called on China\'s young people to rise against the party\'s own '
             'leaders, whom he accused of taking the capitalist road. To show he was still strong, he swam in the Yangtze.',
             kick='How it began', y=1966, at='beijing'),
      scene('The Red Guards',
            'Millions of students formed Red Guard units and, waving Mao\'s Little Red Book, poured into Beijing for huge '
            'rallies in Tiananmen Square. They set out to smash the four olds, old customs, culture, habits and ideas: '
            'they burned books, wrecked temples and smashed antiques.',
            img='Red Guards', y=1966, at='beijing'),
      cost('Struggle sessions',
           'Teachers, writers, officials and anyone from a bad class background were dragged before jeering crowds, '
           'beaten, paraded in dunce\'s caps and sent to prison or labour camps. Many were killed or took their own '
           'lives. Rival Red Guard groups fought each other with guns, until the army stepped in.',
           num='Up to 2 million', of='people killed, by many estimates', y=1967),
      figure('deng-xiaoping', 'Sent down',
             'Liu Shaoqi, the head of state, was beaten, denied medicine and died in prison in 1969. Deng Xiaoping was '
             'sent to work in a tractor factory, and his son was left paralysed after a fall from a window while held by '
             'Red Guards. Some 17 million young people were sent to the countryside to learn from the peasants.',
             y=1969),
      tale('The last flight of Lin Biao',
           'Mao\'s chosen heir, Marshal Lin Biao, who had spread the cult of the Little Red Book, was accused of plotting '
           'against him. In September 1971 Lin fled with his family by plane, and it crashed in Mongolia, killing '
           'everyone on board. What really happened is still a mystery.',
           y=1971),
      turn('The Gang of Four',
           'Mao died in September 1976. Within a month his widow, Jiang Qing, and three allies, the Gang of Four, were '
           'arrested and blamed for the chaos. Deng Xiaoping came back to power and began the reforms that opened China '
           'to the world.',
           y=1976, at='beijing'),
      legacy('The Communist Party later called the Cultural Revolution a catastrophe, but it is still a touchy subject in '
             'China and little taught in schools. A whole generation lost its education, and countless temples, books '
             'and works of art were destroyed. Its memory shaped Deng\'s turn to calm, practical reform.',
             'Launched by Mao in 1966',
             'Red Guards attacked the four olds',
             'Ended with Mao\'s death in 1976'),
      states=('China',), wiki='Cultural Revolution', at='beijing')

event('six-day-war', 'The Six-Day War', 'war', (1967, 1967),
      'In six days in June 1967 Israel defeated Egypt, Jordan and Syria and took Sinai, Gaza, the West Bank and the Golan.',
      figure('gamal-abdel-nasser', 'Tension',
             'In May 1967 Egypt\'s president, Gamal Abdel Nasser, the hero of the Arab world, moved troops into Sinai, sent '
             'away the UN peacekeepers there and closed the Straits of Tiran to Israeli ships. Arab radio stations '
             'promised Israel\'s destruction, and Israelis feared for their lives. Jordan signed a defence pact with Egypt.',
             kick='How it began', y=1967, at='cairo'),
      battle('The first morning',
             'On the morning of 5 June Israel struck first. Its planes, flying low under the radar, destroyed most of '
             'Egypt\'s air force on the ground in three hours, then the air forces of Jordan and Syria. Its tanks raced '
             'across Sinai and reached the Suez Canal in four days.',
             y=1967),
      battle('Jerusalem',
             'When Jordan joined the fighting, Israeli paratroopers took the Old City of Jerusalem on 7 June and reached '
             'the Western Wall, the holiest place where Jews may pray, which had been closed to them since 1948. Israel '
             'also took the whole West Bank of the Jordan River.',
             y=1967, at='jerusalem'),
      battle('The Golan Heights',
             'In the last two days Israel stormed the Golan Heights, the plateau from which Syrian guns had shelled its '
             'villages below. A ceasefire on 10 June ended the war. Israel now held more than three times as much land as '
             'before.',
             y=1967, at='golan'),
      cost('Refugees again',
           'Some 300,000 Palestinians fled or were driven from the West Bank and Gaza, many for the second time since '
           '1948, and about a million more now lived under Israeli military rule.',
           num='About 300,000', of='Palestinians fled or were driven out', y=1967),
      turn('Land for peace',
           'Meeting in Khartoum in September, Arab leaders said no to peace, to recognition and to talks with Israel. In '
           'November the UN Security Council passed Resolution 242, calling on Israel to leave lands it had taken and on '
           'every state in the region to live in peace within secure borders. It is still the basis of peace plans.',
           y=1967),
      legacy('The war changed the Middle East. Israel gave Sinai back to Egypt for peace in 1982, but it still holds the '
             'Golan Heights and East Jerusalem, and its settlements have spread across the West Bank. The lands taken in '
             '1967, and the millions of Palestinians living in them, are at the heart of the conflict to this day.',
             'Fought from 5 to 10 June 1967',
             'Israel took Sinai, Gaza, the West Bank and the Golan',
             'All of Jerusalem came under Israeli rule'),
      war='six-day-war', wiki='Six-Day War')

event('bangladesh-liberation-war', 'The Bangladesh Liberation War', 'war', (1971, 1971),
      "East Pakistan rose against rule from the West, and with India's help became the free nation of Bangladesh.",
      scene('Two wings',
            'Pakistan was born in 1947 in two parts, 1,600 kilometres apart. The East, where Bengali was spoken, had more '
            'people, but the West held the power and the money. In 1952 students in Dhaka were shot for demanding that '
            'Bengali be a national language, on a day now kept around the world as International Mother Language Day.',
            kick='How it began', y=1952, at='dhaka'),
      figure('sheikh-mujibur-rahman', 'Mujib',
             'In December 1970, weeks after a cyclone killed hundreds of thousands in the East while the government was '
             'slow to help, Sheikh Mujibur Rahman\'s Awami League won a majority in all of Pakistan. The generals in the '
             'West would not let him take power. On 7 March 1971 he told a vast crowd in Dhaka that the struggle now was '
             'for freedom.',
             y=1971, at='dhaka'),
      cost('Operation Searchlight',
           'On the night of 25 March 1971 the Pakistani army struck, killing students, teachers and Hindus in Dhaka and '
           'arresting Mujib. Over nine months soldiers and their local allies killed civilians, raped hundreds of '
           'thousands of women and burned villages. Many call it a genocide.',
           num='300,000 to 3 million', of='people killed, by different counts', y=1971, at='dhaka'),
      scene('Ten million refugees',
            'Some ten million people fled over the border into India and lived in vast camps. Bengali fighters, the '
            'Mukti Bahini, trained in India and fought back. In August George Harrison and Ravi Shankar held the Concert '
            'for Bangladesh in New York, the first great charity concert, to raise money for the refugees.',
            y=1971),
      turn('Victory',
           'In December Pakistan attacked Indian airfields, and India, led by Indira Gandhi, struck back in the East. In '
           'thirteen days Indian forces and the Mukti Bahini reached Dhaka, and on 16 December some 93,000 Pakistani '
           'soldiers surrendered, the largest surrender since the Second World War. Bangladesh was free.',
           y=1971, at='dhaka'),
      legacy('Bangladesh, a nation founded on its language, is now home to over 170 million people. Mujib, called the '
             'father of the nation, was murdered in a coup in 1975. 16 December is kept as Victory Day, and the killings '
             'of 1971 are still remembered, and argued over, in both countries.',
             'The war began on 25 March 1971',
             'Ten million fled to India',
             'Pakistan surrendered on 16 December 1971'),
      states=('Bangladesh',), war='bangladesh-liberation-war', wiki='Bangladesh Liberation War')

event('cambodian-genocide', 'The Khmer Rouge years', 'genocide', (1975, 1979),
      "Pol Pot's Khmer Rouge emptied Cambodia's cities to build a nation of peasants, and about a quarter of its people died.",
      scene('Year Zero',
            'After years of civil war and American bombing, the communist Khmer Rouge took Cambodia\'s capital, Phnom '
            'Penh, on 17 April 1975. Within days they drove its two million people into the countryside at gunpoint, '
            'even the sick from hospitals. They declared Year Zero: money, markets, schools and religion were abolished.',
            kick='How it began', y=1975, at='phnom_penh'),
      figure('pol-pot', 'Brother Number One',
             'The movement was led by Saloth Sar, who called himself Pol Pot, a former teacher who had studied in Paris. '
             'He dreamed of a pure peasant nation that relied on nobody. Few Cambodians even knew his name; orders came '
             'from Angkar, the Organisation.',
             y=1976),
      cost('The killing fields',
           'City people, the educated, monks, Vietnamese and Cham Muslims, even people who wore glasses, were singled '
           'out. Families were split up and worked in the fields from dawn to dark on a few spoonfuls of rice. Hundreds of '
           'thousands were executed and buried in mass graves, and many more died of hunger and disease.',
           num='1.5 to 2 million', of='people died, about one in four', y=1977),
      scene('S-21',
            'In a former high school in Phnom Penh, the prison called S-21, at least 14,000 people were photographed, '
            'tortured into confessing and killed. Only a handful survived. Today it is the Tuol Sleng Genocide Museum, '
            'its walls covered with the prisoners\' photographs.',
            img='Tuol Sleng Genocide Museum', y=1978, at='phnom_penh'),
      turn('Vietnam invades',
           'After Khmer Rouge raids across its border, Vietnam invaded in December 1978 and took Phnom Penh in January '
           '1979. Pol Pot fled to the jungle along the Thai border, where his forces fought on for years, backed by '
           'China and still holding Cambodia\'s seat at the United Nations.',
           y=1979, at='phnom_penh'),
      legacy('Pol Pot died in 1998 without facing trial. A court set up with the United Nations later convicted a few of '
             'the surviving leaders of genocide and crimes against humanity. Cambodia has rebuilt, but almost every family '
             'lost someone, and the killing fields at Choeung Ek are now a memorial.',
             'Phnom Penh emptied on 17 April 1975',
             'About a quarter of Cambodians died',
             'Ended by the Vietnamese invasion of 1979'),
      states=('Cambodia',), wiki='Cambodian genocide', at='phnom_penh')

event('iranian-revolution', 'The Iranian Revolution', 'revolution', (1978, 1979),
      'Millions of Iranians rose against the shah, and the exiled Ayatollah Khomeini came home to found an Islamic republic.',
      figure('mohammad-reza-pahlavi', 'The shah',
             'Mohammad Reza Shah Pahlavi, put back on his throne in 1953 by a coup backed by the United States and '
             'Britain, used Iran\'s oil money to build a modern state and army. But his secret police jailed and tortured '
             'opponents, and many Iranians felt their country was run for the rich and for foreigners.',
             kick='How it began', y=1977, at='tehran'),
      figure('ruhollah-khomeini', 'The voice from exile',
             'From exile in Iraq and then France, Ayatollah Ruhollah Khomeini, a senior Shia cleric, attacked the shah as '
             'a puppet of America. His sermons were smuggled into Iran on cassette tapes and copied by the thousand. '
             'Through 1978 the protests grew, and soldiers fired on crowds again and again.',
             y=1978),
      turn('The shah leaves',
           'Strikes shut down the oil fields, and millions marched in Tehran. On 16 January 1979 the shah flew out of '
           'Iran, never to return. On 1 February Khomeini landed in Tehran to a welcome by millions. Within days the army '
           'gave up, and in a vote that spring Iranians chose an Islamic Republic.',
           y=1979, at='tehran'),
      scene('The hostages',
            'In November 1979 students loyal to Khomeini stormed the American embassy in Tehran and took 52 Americans '
            'hostage. They were held for 444 days, and a rescue mission ended in disaster in a desert sandstorm. The '
            'crisis broke relations between Iran and the United States, which have never been restored.',
            img='Iran hostage crisis', y=1979, at='tehran'),
      scene('An Islamic republic',
            'The new state was ruled by clerics, with Khomeini as Supreme Leader. Women had to cover their hair, and many '
            'of the liberals and leftists who had joined the revolution were jailed or executed. In 1980 Iraq invaded, '
            'beginning an eight-year war that killed hundreds of thousands.',
            y=1980),
      legacy('The revolution created the first modern state ruled by Islamic clerics and inspired Islamist movements '
             'across the Muslim world. It made Iran and the United States bitter enemies. Inside Iran, protests against '
             'its strict rules, like those led by women in 2022, still challenge the system it built.',
             'The shah fled in January 1979',
             'Khomeini came home on 1 February 1979',
             '52 Americans were held for 444 days'),
      states=('Iran',), wiki='Iranian Revolution', at='tehran')

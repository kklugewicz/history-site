from _lib import story, life, win, made, work, song, tale, legacy

story('henry-ford', 'The farm boy who put the world on wheels with the Model T and the assembly line.',
    life('A farm boy who loved machines',
         'Henry Ford was born in 1863 on a farm in Dearborn, Michigan. He hated farm work but loved machines, and repaired '
         "his neighbours' watches. At 16 he walked to Detroit to become an apprentice machinist.",
         y=1863, at='dearborn'),
    tale('Knocking down the wall',
         'Working as an engineer for an electric company in Detroit, in 1896 he built his first car, the Quadricycle, in a '
         'shed behind his house. It was wider than the shed door, so he knocked down part of the wall to drive it out.',
         img='Ford Quadricycle', y=1896, at='detroit'),
    win('The Model T',
        'In 1908 he launched the Model T, a simple, tough car "for the great multitude". From 1914 it came only in black, '
        'because black paint dried fastest: "Any colour, so long as it is black."',
        img='Ford Model T', y=1908, at='detroit'),
    made('The moving assembly line',
         'In 1913, at his Highland Park factory, the cars moved past the workers on a conveyor, and each worker did one job. '
         'Building a Model T went from about 12 hours to about 90 minutes.',
         'The price of a Model T fell from 850 to under 300 dollars, and mass production spread to almost every industry.',
         img='Assembly line', y=1913, at='highland_park_mi'),
    win('Five dollars a day',
        'In 1914 he doubled his workers\' pay to five dollars a day, so that they would stay, and could afford to buy the '
        'cars they built.',
        y=1914, at='highland_park_mi'),
    tale('Half the cars in America',
         'By 1927 Ford had built more than 15 million Model Ts. For a time, about half of all the cars in America were Model '
         'Ts.',
         y=1927, at='dearborn'),
    life('The dark side',
         'In the 1920s his newspaper spread hatred of Jews, in articles that Hitler admired. He also fought trade unions '
         'with spies and thugs, who in 1937 beat up union organisers outside his factory.',
         y=1920, at='dearborn'),
    legacy('Ford put the world on wheels, and his assembly line became the way the modern world makes almost everything.',
           'Built the Model T, the car for everyone',
           'Introduced the moving assembly line',
           'Paid his workers five dollars a day'),
)

story('marie-curie', 'The first woman to win a Nobel Prize, and the only person to win in two sciences.',
    life('The secret university',
         'Maria Skłodowska was born in Warsaw in 1867, when Poland was ruled by Russia and women could not go to university. '
         'She studied at the "Flying University", whose classes moved from house to house in secret.',
         y=1867, at='warsaw'),
    life('Cold and hungry in Paris',
         "She worked for years as a governess to pay for her sister's studies, then followed her to Paris in 1891. She lived "
         'in an attic so cold that she slept under all her clothes, and once fainted from hunger. She came first in her '
         'class in physics.',
         img='University of Paris', y=1891, at='paris'),
    life('Pierre',
         'In 1894 she met the physicist Pierre Curie. They married the next year; she wore a dark blue dress she could use in '
         'the laboratory, and they went on honeymoon by bicycle.',
         img='Pierre Curie', cap='Pierre Curie, her husband', y=1895, at='paris'),
    made('Radioactivity',
         'She found that the rays given off by uranium come from inside its atoms, and named this radioactivity. In 1898, '
         'working in a leaky shed, she and Pierre discovered two new elements: polonium, named after Poland, and radium.',
         'It showed that atoms are not solid and unchanging, opening the way to nuclear physics. Radiation was soon used to '
         'treat cancer.',
         img='Radium', y=1898, at='paris'),
    win('Two Nobel Prizes',
        'In 1903 she shared the Nobel Prize in Physics, the first woman ever to win a Nobel. In 1911 she won the Nobel Prize '
        'in Chemistry on her own. She is still the only person to win Nobels in two different sciences.',
        img='Nobel Prize', y=1911, at='paris'),
    life("Pierre's death",
         'In 1906 Pierre was knocked down and killed by a horse-drawn wagon in a Paris street. She took over his post, and '
         'became the first woman to teach at the Sorbonne.',
         y=1906, at='paris'),
    win('The little Curies',
        'In the First World War she set up X-ray vans, nicknamed "little Curies", drove them to the front herself, and '
        'trained women to run them. More than a million wounded soldiers were X-rayed.',
        img='Petites Curies', y=1914),
    tale('Glowing notebooks',
         'She carried radium in her pockets and kept it in her desk, and liked its soft glow in the dark. She died in 1934 of '
         'an illness caused by radiation. Her notebooks are still so radioactive that they are kept in lead boxes.',
         y=1934, at='paris'),
    legacy('Curie discovered the secrets of radioactivity and two new elements, opened the way to nuclear physics and '
           'cancer treatment, and showed the world what women scientists could do.',
           'First woman to win a Nobel Prize',
           'The only person to win Nobel Prizes in two sciences',
           'Discovered polonium and radium'),
)

story('wright-brothers', 'Two bicycle makers from Ohio who made the first powered airplane flight.',
    life('A toy helicopter',
         'In 1878 their father brought home a toy helicopter made of bamboo, paper and cork, driven by a rubber band. Wilbur '
         'and Orville Wright played with it until it broke, then built their own.',
         y=1878, at=(-91.67, 41.98), where='Cedar Rapids, Iowa'),
    life('The bicycle shop',
         'The brothers never finished high school, and never married. In Dayton, Ohio, they ran a printing press, then from '
         '1892 a bicycle shop, which paid for their experiments with flying machines.',
         img='Wright Cycle Company', y=1892, at='dayton'),
    made('Steering in the air',
         'Watching birds, Wilbur saw that they twist the tips of their wings to keep their balance. Twisting an empty '
         'cardboard box in his hands, he saw how to twist a wing in the same way.',
         'Control in three directions, rolling, climbing and turning, is still how every airplane is steered.',
         y=1899, at='dayton'),
    tale('Why Kitty Hawk?',
         'For their gliders they needed strong, steady winds, soft sand to land on and no crowds. They found them at Kitty '
         'Hawk, on the coast of North Carolina, and camped there every autumn.',
         y=1900, at='kitty_hawk'),
    made('The wind tunnel',
         'The published tables on how wings lift turned out to be wrong. So in 1901 they built a wind tunnel, a wooden box '
         'with a fan, and tested some 200 shapes of wing.',
         'With the results they designed wings and propellers that worked, founding the science of aeronautics.',
         img='Wind tunnel', y=1901, at='dayton'),
    win('The first flight',
        'On 17 December 1903 Orville flew their Flyer for 12 seconds and 37 metres: the first controlled, powered airplane '
        'flight. Wilbur had won a coin toss to go first three days before, but stalled. That day he flew 260 metres.',
        img='Wright Flyer', y=1903, at='kitty_hawk'),
    tale('Nobody believed them',
         'Few people believed them at first. In 1908 Wilbur flew in France, swooping and circling under perfect control, and '
         'stunned the crowds. "We are beaten," said a French pilot.',
         y=1908, at=(0.2, 48.0), where='Le Mans'),
    life('After the Flyer',
         'Wilbur died of typhoid in 1912. Orville lived until 1948, long enough to see planes fly faster than sound.',
         y=1912, at='dayton'),
    legacy('The Wright brothers invented the airplane. Just 66 years after their first flight, people walked on the Moon, '
           'and a scrap of their Flyer went with them.',
           'Made the first powered, controlled airplane flight',
           'Invented the way airplanes are steered',
           'Started the age of flight'),
)

story('mahatma-gandhi', 'He led India to independence without violence, and inspired the world.',
    life('A shy boy',
         'Mohandas Gandhi was born in 1869 in Porbandar, in western India. He was a shy boy, frightened of the dark. At 13 he '
         'was married to Kasturba, who was 14.',
         y=1869, at='porbandar'),
    life('A lawyer in London',
         'In 1888 he went to London to study law. He had promised his mother he would not touch meat, wine or women, and '
         'joined the Vegetarian Society.',
         y=1888, at='london'),
    tale('Thrown off the train',
         'In 1893, working on a case in South Africa, he was thrown off a train at Pietermaritzburg for refusing to leave a '
         'first-class carriage kept for white people. Shivering in the station all night, he decided to fight injustice.',
         y=1893, at='pietermaritzburg'),
    win('Truth force',
        'He stayed in South Africa for 21 years, leading its Indians in peaceful resistance to unjust laws, which he called '
        'satyagraha, "truth force". He was jailed again and again.',
        y=1906, at='johannesburg'),
    life('Homespun',
         'Back in India in 1915, he became the leader of the fight for independence. He gave up Western clothes for a simple '
         'homespun cloth, spun thread every day, and urged Indians to boycott British cloth.',
         img='Charkha', y=1921, at='ahmedabad'),
    win('The Salt March',
        'In 1930 he walked 390 km to the sea at Dandi to make salt, breaking the British law that taxed it. Thousands joined '
        'him, and some 60,000 people were jailed.',
        img='Salt March', y=1930, at='dandi'),
    tale('Tea with the king',
         'In 1931 he went to London for talks, and had tea with King George V at Buckingham Palace wearing his simple '
         'cloth. Asked if he had been dressed enough, he joked: "The king had enough on for both of us."',
         y=1931, at='london'),
    win('Independence',
        'In 1942 he told Britain to "Quit India", and was jailed; his wife Kasturba died in prison. India became free in 1947, '
        'but was split into India and Pakistan amid terrible killing. Gandhi fasted to stop it.',
        y=1947, at='delhi'),
    life('The last walk',
         'On 30 January 1948, on his way to evening prayers in Delhi, he was shot dead by a Hindu extremist. "The light has '
         'gone out of our lives," said Nehru.',
         img='Gandhi Smriti', y=1948, at='delhi'),
    legacy('Gandhi led India to independence without violence, and inspired Martin Luther King, Nelson Mandela and '
           'peaceful protest movements all over the world.',
           'Led India to independence',
           'Pioneered non-violent resistance',
           'Inspired Martin Luther King and Nelson Mandela'),
)

story('vladimir-lenin', 'The revolutionary who led the Russian Revolution and founded the Soviet Union.',
    life('A brother hanged',
         'Vladimir Ulyanov was born in 1870 in Simbirsk, on the Volga, the son of a school inspector. In 1887 his older '
         'brother was hanged for plotting to kill the tsar. That same year Vladimir was thrown out of university for joining '
         'a protest.',
         y=1887, at='simbirsk'),
    life('Siberia and exile',
         'He became a Marxist revolutionary. In 1897 he was exiled to Siberia for three years, where he married Nadezhda '
         'Krupskaya. Later he took the name Lenin, and spent most of the next 17 years abroad, leading the Bolsheviks.',
         y=1897, at='shushenskoye'),
    tale('The sealed train',
         'In 1917, after the tsar fell, the German government, at war with Russia, let Lenin cross Germany from Switzerland '
         'in a sealed train, hoping he would cause trouble in Russia. He did.',
         y=1917, at='zurich'),
    life('The October Revolution',
         'In November 1917 his Bolsheviks seized power in Petrograd and stormed the Winter Palace. Lenin promised "peace, '
         'land and bread".',
         img='October Revolution', y=1917, at='st_petersburg', where='Petrograd'),
    life('Civil war and terror',
         'He made peace with Germany, giving up huge lands. A brutal civil war followed. His secret police, the Cheka, '
         'jailed and shot many thousands in the Red Terror, and the tsar and his family were killed. Millions died of war '
         'and famine.',
         y=1918, at='moscow'),
    tale('Shot',
         'In 1918 a woman named Fanny Kaplan shot him twice as he left a factory in Moscow. He survived, but never fully '
         'recovered.',
         y=1918, at='moscow'),
    life('The Soviet Union',
         'In 1922 he founded the Union of Soviet Socialist Republics, the first communist state, ruled by one party. To '
         'rescue the ruined economy, he allowed some private trade again.',
         img='Soviet Union', y=1922, at='moscow'),
    life('The mausoleum',
         'Strokes left him unable to speak. In his last notes he warned against Stalin, but the warning was ignored. He died '
         'in 1924, and his embalmed body is still on show in a tomb on Red Square.',
         img="Lenin's Mausoleum", y=1924, at='moscow'),
    legacy('Lenin led the first communist revolution and founded the Soviet Union, a one-party state that lasted until '
           '1991 and inspired communist movements around the world.',
           'Led the Russian Revolution of 1917',
           'Founded the Soviet Union',
           'Built a one-party state that ruled by terror'),
)

story('roald-amundsen', 'The Norwegian who was first to the South Pole and first through the Northwest Passage.',
    life('Windows open in winter',
         'Roald Amundsen was born in 1872 in Borge, Norway, into a family of shipowners. His mother wanted him to be a '
         'doctor, but he dreamed of the poles, and slept with his windows open in winter to toughen himself up.',
         y=1872, at='borge'),
    life('Trapped in the ice',
         'In 1897 he sailed on the Belgica, the first ship to spend a winter in the Antarctic, trapped in the pack ice. The '
         'crew fell ill with scurvy, and he helped save them by feeding them raw seal and penguin meat.',
         img='Belgian Antarctic Expedition', y=1898, at=(-85.0, -70.0), where='Bellingshausen Sea'),
    win('The Northwest Passage',
        'From 1903 to 1906, with six men in a little fishing boat, the Gjøa, he became the first to sail the Northwest '
        'Passage over the top of North America. He spent two winters with the Netsilik Inuit, learning to drive dogs and '
        'dress in furs.',
        img='Gjøa', y=1905, at=(-95.88, 68.63), where='Gjoa Haven'),
    tale('A change of plan',
         'In 1910 he set off, saying he was going to the North Pole. But the North Pole had just been claimed, so he secretly '
         'turned south, told his crew at Madeira, and sent the British explorer Scott a telegram: he was heading for '
         'Antarctica.',
         y=1910, at=(-16.9, 32.65), where='Madeira'),
    win('The South Pole',
        'With four men, 52 dogs and skis, he reached the South Pole on 14 December 1911, five weeks before Scott, and planted '
        "Norway's flag. Scott and his men died on their way back.",
        img="Amundsen's South Pole expedition", y=1911, at='south_pole'),
    win('Both poles',
        'In 1926 he flew over the North Pole in the airship Norge. He and his companion Oscar Wisting became the first '
        'people to reach both poles.',
        img='Norge (airship)', y=1926, at=(11.92, 78.92), where='Svalbard'),
    life('Lost in the Arctic',
         'In 1928 he flew off from Tromsø to search for his rival Umberto Nobile, whose airship had crashed in the Arctic. '
         'His plane vanished over the sea and was never found. Nobile was rescued.',
         y=1928, at='tromso'),
    legacy("Amundsen's careful planning and the skills he learned from the Inuit made him the greatest polar explorer of "
           'all.',
           'First to reach the South Pole',
           'First to sail the Northwest Passage',
           'Among the first to reach both poles'),
)

story('winston-churchill', 'The prime minister who refused to give in to Hitler, and led Britain through the Second World War.',
    life('Born in a palace',
         'Winston Churchill was born in 1874 at Blenheim Palace, the son of a politician and an American heiress. He did '
         'badly at school, and failed the army entrance exam twice before he got in.',
         img='Blenheim Palace', y=1874, at='blenheim'),
    tale('Escape from Pretoria',
         'As a war reporter in South Africa in 1899 he was captured by the Boers. He escaped from a prison camp in Pretoria, '
         'hid in a coal mine and on a goods train, and reached safety. It made him a hero at home.',
         y=1899, at='pretoria'),
    life('Gallipoli',
         'In the First World War, as head of the navy, he backed the attack on Gallipoli in 1915, a disaster that cost many '
         'lives. He resigned and went to fight in the trenches.',
         img='Gallipoli campaign', y=1915, at='gallipoli'),
    life('The wilderness years',
         "In the 1930s, out of office, he warned again and again that Hitler's Germany was arming for war. Few listened. He "
         'painted, laid bricks in his garden at Chartwell, and wrote.',
         img='Chartwell', y=1935, at=(0.08, 51.25), where='Chartwell'),
    win('We shall never surrender',
        'In May 1940, as France fell, he became prime minister: "I have nothing to offer but blood, toil, tears and sweat." '
        '"We shall fight on the beaches... we shall never surrender." For a year Britain fought on alone.',
        img='We shall fight on the beaches', y=1940, at='london'),
    win('Victory',
        'He worked with Roosevelt and Stalin, meeting them at Tehran and Yalta, and led Britain to victory in 1945. Weeks '
        'later, voters threw him out in a general election.',
        img='Yalta Conference', y=1945, at='yalta'),
    tale('The iron curtain',
         'In 1946, in Missouri, he warned that "an iron curtain has descended across the continent" of Europe, the start of '
         'the Cold War.',
         y=1946, at=(-91.95, 38.85), where='Fulton, Missouri'),
    life('The dark side',
         'His views on empire and race were harsh even for his time. He bitterly opposed independence for India, and many '
         "blame his government's choices for making the Bengal famine of 1943 worse.",
         y=1943, at='london'),
    win('The Nobel Prize',
        'Prime minister again from 1951 to 1955, he won the Nobel Prize in Literature in 1953 for his histories and '
        'speeches. When he died in 1965, he was given a state funeral.',
        y=1953, at='london'),
    legacy('Churchill led Britain through its darkest hour, refusing to make peace with Hitler, and his speeches still '
           'stir people today.',
           'Led Britain to victory in the Second World War',
           'Refused to make peace with Hitler in 1940',
           'Won the Nobel Prize in Literature'),
)

story('joseph-stalin', 'The dictator who made the Soviet Union a superpower at the cost of millions of lives.',
    life("A shoemaker's son",
         'Ioseb Jughashvili was born in 1878 in Gori, in Georgia, the son of a shoemaker who beat him. Smallpox scarred his '
         'face. He trained to be a priest, but turned to revolution.',
         y=1878, at='gori'),
    life('Man of steel',
         'As a revolutionary he organised strikes and robberies to raise money for the Bolsheviks. He was arrested and exiled '
         'to Siberia again and again, and escaped again and again. He took the name Stalin, "man of steel".',
         y=1907, at='tbilisi'),
    life('Taking power',
         "After Lenin's death in 1924, Stalin, the party's general secretary, outwitted his rivals, among them Trotsky, and "
         'by 1929 ruled alone.',
         y=1929, at='moscow'),
    life('Steel and famine',
         'He forced the country to build steel mills, dams and cities at breakneck speed, and drove the peasants into '
         'collective farms. The famine that followed in 1932 and 1933 killed millions, above all in Ukraine and Kazakhstan.',
         y=1932, at='kyiv'),
    life('The Great Terror',
         'In 1937 and 1938 his secret police arrested more than a million people. Some 700,000 were shot, among them most of '
         "the army's generals and many of his old comrades. Millions more were sent to labour camps, the Gulag.",
         img='Gulag', y=1937, at='moscow'),
    life('War with Hitler',
         'In 1939 he made a pact with Hitler and they carved up Eastern Europe. In 1941 Hitler attacked anyway. The Soviet '
         'Union lost some 27 million people, but after Stalingrad its Red Army fought all the way to Berlin.',
         img='Battle of Stalingrad', y=1943, at='stalingrad'),
    life('The Cold War',
         'After 1945 he put communist governments in power across Eastern Europe, and in 1949 the Soviet Union tested its '
         'first atomic bomb. The Cold War with the West had begun.',
         y=1949, at='moscow'),
    life('Death',
         'He died after a stroke in 1953; his guards had been too afraid to enter his room for hours. In 1956 his successor, '
         'Khrushchev, denounced his crimes.',
         y=1953, at='moscow'),
    legacy('Stalin made the Soviet Union an industrial and military superpower that helped defeat Nazi Germany, at the '
           'cost of millions of lives in famine, executions and camps. He was one of the deadliest dictators in history.',
           'Ruled the Soviet Union from the late 1920s to 1953',
           'Industrialised the country by force',
           'Millions died in his famines, purges and camps'),
)

story('albert-einstein', 'The patent clerk who discovered relativity and E = mc², and changed how we see the universe.',
    life('The compass',
         'Albert Einstein was born in Ulm, Germany, in 1879, and grew up in Munich. When he was about five, his father showed '
         'him a compass. That the needle always pointed north amazed him: something hidden had to be moving it.',
         y=1884, at='munich'),
    tale('Not a bad student',
         'A myth says he failed maths. In fact he had taught himself calculus by 15. He hated his strict German school, left '
         'it, and finished school in Switzerland.',
         y=1895, at='zurich'),
    life('The patent clerk',
         'Unable to get a university job, he worked as a clerk in the patent office in Bern, checking inventions, and thought '
         'about physics in his spare time.',
         img='Einsteinhaus', y=1902, at='bern'),
    made('The miracle year',
         'In 1905, aged 26, he published four papers. One showed that light comes in tiny packets. One proved that atoms '
         'exist. One set out special relativity, and one showed that E = mc²: mass and energy are two forms of one thing.',
         'They founded modern physics, from quantum theory to nuclear energy. The packets of light explain how solar panels '
         'work.',
         img='Annus mirabilis papers', y=1905, at='bern'),
    made('Gravity bends space',
         'In 1915 he showed that gravity is the bending of space and time by mass. In 1919 astronomers watching an eclipse '
         'saw starlight bent by the Sun, just as he had said, and he became famous overnight.',
         'It explains black holes and the expanding universe, and GPS satellites must correct for it to work.',
         img='General relativity', y=1919, at='berlin'),
    win('The Nobel Prize',
        'He won the Nobel Prize in Physics for 1921, not for relativity, but for explaining how light knocks electrons out '
        'of metal. He gave the prize money to his first wife, as he had promised in their divorce.',
        img='Photoelectric effect', y=1921, at='berlin'),
    life('Fleeing the Nazis',
         'The Nazis hated him because he was Jewish, and burned his books. In 1933 he left Germany for good, and settled at '
         'Princeton, in the United States.',
         y=1933, at='princeton'),
    tale('The letter',
         'In 1939 he signed a letter to President Roosevelt warning that Germany might build an atomic bomb. It helped start '
         'the American bomb project. He later called it the one great mistake of his life.',
         img='Einstein–Szilard letter', y=1939, at='princeton'),
    tale('No socks',
         'He refused to wear socks, and in 1952 he turned down an offer to become president of Israel, saying he lacked the '
         'talent for dealing with people.',
         y=1952, at='princeton'),
    legacy("Einstein's theories of relativity and light changed how we understand space, time, energy and the universe. "
           'His name has become another word for genius.',
           'Discovered relativity and E = mc²',
           'Showed that light comes in packets, a root of quantum physics',
           'Won the Nobel Prize in Physics'),
)

story('mustafa-kemal-ataturk', 'The general who founded modern Turkey and remade it from top to bottom.',
    life('A boy from Salonica',
         'Mustafa was born in 1881 in Salonica, now Thessaloniki in Greece, then a city of the Ottoman Empire. A maths teacher '
         'gave him the name Kemal, "perfection". He trained as an army officer.',
         y=1881, at='thessaloniki'),
    win('Gallipoli',
        'In 1915 he helped hold back the British and French invasion at Gallipoli. He told his men: "I do not order you to '
        'attack, I order you to die." A piece of shrapnel struck the watch in his breast pocket.',
        img='Gallipoli campaign', y=1915, at='gallipoli'),
    win('The War of Independence',
        'After the Ottoman defeat in the First World War, the Allies occupied the empire and planned to carve up Anatolia. '
        'Kemal led the resistance from Ankara, and by 1922 had driven out the invading Greek army.',
        img='Turkish War of Independence', y=1922, at='ankara'),
    win('The Republic of Turkey',
        'In 1923 he founded the Republic of Turkey, with Ankara as its capital, and became its first president. The next '
        'year he abolished the caliphate.',
        img='Anıtkabir', y=1923, at='ankara'),
    win('A new alphabet',
        'In 1928 he replaced the Arabic script with a Latin alphabet, and toured the country with a blackboard, teaching it '
        'himself in town squares.',
        img='Turkish alphabet', y=1928, at='constantinople', where='Istanbul'),
    win('Votes for women',
        'He separated religion from the state, brought in European-style laws, banned the fez, and in 1934 gave women the '
        'vote, before France or Italy.',
        y=1934, at='ankara'),
    tale('Father of the Turks',
         'In 1934 everyone in Turkey had to take a surname. Parliament gave him the name Atatürk, "Father of the Turks", and '
         'no one else may use it.',
         y=1934, at='ankara'),
    life('A strongman',
         'He ruled with a single party and crushed opposition and Kurdish revolts. He died in Istanbul in 1938. Every year on '
         '10 November, at 9:05 in the morning, the moment he died, Turkey stops for a minute of silence.',
         img='Dolmabahçe Palace', y=1938, at='constantinople', where='Istanbul'),
    legacy('Atatürk founded modern Turkey and turned it into a secular republic, with a new alphabet, new laws and the vote '
           'for women.',
           'Founded the Republic of Turkey',
           'Hero of Gallipoli',
           'Gave Turkey a new alphabet and votes for women'),
)

story('pablo-picasso', 'The most famous artist of the 20th century, co-founder of Cubism and painter of Guernica.',
    life('His first word was pencil',
         'Pablo Picasso was born in Málaga, Spain, in 1881. His mother said his first word was "piz", short for lápiz, '
         'pencil. His father, an art teacher, is said to have given up painting when he saw how well his 13-year-old son '
         'drew.',
         y=1881, at='malaga'),
    work('The Blue Period',
         'Poor, and grieving for a friend who had taken his own life, from 1901 to 1904 he painted beggars, the blind and the '
         'lonely in shades of blue.',
         img='The Old Guitarist', y=1903, at='barcelona'),
    work("Les Demoiselles d'Avignon",
         'In Paris in 1907 he painted five women with faces like African masks, their bodies broken into sharp shapes. Even '
         'his friends were shocked. It became one of the founding works of modern art.',
         img="Les Demoiselles d'Avignon", y=1907, at='paris'),
    win('Cubism',
        'With Georges Braque he invented Cubism, showing things from many sides at once, broken into geometric pieces. They '
        'also invented collage, gluing paper and newspaper onto their pictures.',
        img='Cubism', y=1912, at='paris'),
    tale('A suspect for the Mona Lisa',
         'When the Mona Lisa was stolen from the Louvre in 1911, the police questioned Picasso, because a friend had once '
         'sold him little statues stolen from the museum. He had nothing to do with it.',
         img='Mona Lisa', y=1911, at='paris'),
    work('Guernica',
         'In 1937, in the Spanish Civil War, German planes bombed the Basque town of Guernica. Picasso painted a huge black '
         'and white picture of screaming people and animals. The story goes that a German officer asked him: "Did you do '
         'this?" He answered: "No, you did."',
         img='Guernica (Picasso)', y=1937, at='guernica'),
    tale('Fifty thousand works',
         'He never stopped working: paintings, sculptures, pottery, prints and drawings, some 50,000 works in all. He was '
         'often cruel to the women he loved, who were also his models. He died in 1973, aged 91.',
         y=1960),
    legacy('Picasso was the most influential artist of the 20th century, and changed what a painting could be.',
           'Co-founded Cubism',
           'Painted Guernica',
           'Made some 50,000 works of art'),
)

story('franklin-d-roosevelt', 'The president who fought the Great Depression with the New Deal and led America in the Second World War.',
    life('A rich boy',
         'Franklin Delano Roosevelt was born in 1882 at Hyde Park, New York, the only child of a wealthy family, and a distant '
         'cousin of President Theodore Roosevelt. In 1905 he married Eleanor, Theodore\'s niece.',
         y=1882, at='hyde_park'),
    life('Polio',
         'In 1921, at 39, he fell ill with polio, which left his legs paralysed. He never walked on his own again, and hid it '
         'from the public. He set up a centre for polio patients at Warm Springs, Georgia.',
         y=1921, at='warm_springs'),
    win('Nothing to fear',
        'He was elected president in 1932, in the Great Depression, when a quarter of workers had no job. At his '
        'inauguration he said: "The only thing we have to fear is fear itself."',
        img='Great Depression', y=1933, at='washington'),
    tale('Fireside chats',
         'He talked to Americans on the radio in plain words, explaining what he was doing. Families gathered around the '
         'radio to listen to his "fireside chats".',
         y=1933, at='washington'),
    win('The New Deal',
        'His New Deal put millions to work building dams, bridges, roads and parks, helped farmers, set rules for banks, and '
        'created Social Security, pensions for the old.',
        img='New Deal', y=1935, at='washington'),
    win('The arsenal of democracy',
        'In the Second World War he sent weapons to Britain and the Soviet Union. When Japan attacked Pearl Harbor on 7 '
        'December 1941, "a date which will live in infamy", the United States joined the war.',
        img='Attack on Pearl Harbor', y=1941, at=(-157.95, 21.35), where='Pearl Harbor'),
    life('The camps',
         'In 1942 he ordered some 120,000 Japanese Americans, most of them American citizens, into prison camps. The country '
         'formally apologised in 1988.',
         y=1942, at='washington'),
    win('Four terms',
        'He won four presidential elections, more than any other president. With Churchill and Stalin he planned the defeat '
        'of Germany and Japan, and the United Nations.',
        y=1944, at='washington'),
    life('The unfinished portrait',
         'He died suddenly in April 1945, weeks before victory in Europe, while sitting for a portrait at Warm Springs. The '
         'painting was never finished.',
         img='Unfinished portrait of Franklin D. Roosevelt', y=1945, at='warm_springs'),
    legacy('Roosevelt led the United States through the Great Depression and the Second World War, and his New Deal built '
           'the safety net of modern America.',
           'Led America through the Depression and the Second World War',
           'Created the New Deal and Social Security',
           'The only president elected four times'),
)

from _lib import story, life, win, made, work, song, tale, legacy

story('gregor-mendel', 'The monk whose pea plants revealed the laws of heredity, ignored until after his death.',
    life("A farmer's son",
         'Johann Mendel was born in 1822 in Heinzendorf, a village in Austrian Silesia, now in the Czech Republic. His '
         'parents were poor farmers, and as a boy he tended the orchard and kept bees. His family struggled to pay for his '
         'schooling.',
         y=1822, at='heinzendorf'),
    life('The monk',
         'To be able to keep studying, in 1843 he became a monk at the Abbey of St Thomas in Brno, and took the name '
         'Gregor. The abbey was a centre of learning, with a library, scientists, and a garden.',
         img="St Thomas's Abbey, Brno", y=1843, at='brno'),
    tale('Failing the exam',
         'The abbey sent him to the University of Vienna to study science. Twice he failed the exam to become a qualified '
         'teacher, so for years he taught as a substitute.',
         img='University of Vienna', y=1856, at='vienna'),
    made('The pea experiments',
         'From 1856 to 1863, in the abbey garden, he grew and cross-bred some 28,000 pea plants, counting tall and short, '
         'smooth and wrinkled, green and yellow. Traits passed on in neat ratios, such as 3 to 1, and some skipped a '
         'generation.',
         'He had found that traits are passed on in separate units, one from each parent: what we now call genes.',
         img='Mendelian inheritance', y=1863, at='brno'),
    life('Ignored',
         'He presented his results in 1865 and published them the next year. Almost no one understood them. A famous '
         'botanist told him to try hawkweed instead, a plant whose odd way of breeding made his laws seem not to work.',
         y=1866, at='brno'),
    life('Abbot',
         'In 1868 he was elected abbot, and had little time left for science, though he still kept bees and recorded the '
         'weather every day. He is said to have told a friend: "My time will come." He died in 1884, and his papers were '
         'burned.',
         y=1868, at='brno'),
    win('Rediscovered',
        'In 1900, three scientists working separately found the same laws, then came across his paper. Sixteen years after '
        'his death, Mendel was hailed as the father of genetics.',
        y=1900),
    legacy('Mendel found the basic laws of heredity, how traits pass from parents to children. DNA tests, new crops and '
           'the study of inherited diseases all build on his peas.',
           'Discovered the laws of heredity',
           'The father of genetics',
           'Ignored until 16 years after his death'),
)

story('harriet-tubman', 'She escaped slavery, then went back again and again to lead others to freedom.',
    life('Born enslaved',
         'Harriet Tubman was born Araminta Ross, around 1822, on a plantation in Maryland. As a small child she was hired '
         'out to other families and whipped. Three of her sisters were sold away, and she never saw them again.',
         y=1822, at=(-76.15, 38.45), where='Dorchester County, Maryland'),
    life('The blow to the head',
         'As a teenager she was hit on the head by a heavy iron weight that an overseer threw at another enslaved man. For '
         'the rest of her life she had seizures, headaches and vivid dreams, which she believed were messages from God.',
         y=1836, at=(-76.15, 38.45), where='Dorchester County, Maryland'),
    win('Escape',
        'In 1849, afraid she would be sold, she escaped alone, walking about 145 km by night to Pennsylvania, guided by the '
        'North Star. "I had crossed the line. I was free; but there was no one to welcome me to the land of freedom."',
        y=1849, at='philadelphia'),
    win('Moses',
        'She went back to Maryland about 13 times and led around 70 people to freedom, her own family among them, along '
        'the Underground Railroad, a secret network of safe houses. People called her Moses.',
        img='Underground Railroad', y=1854),
    tale('Never lost a passenger',
         'She travelled in winter, when nights were long, and sang songs as secret signals. She carried a pistol, and later '
         'said: "I never ran my train off the track, and I never lost a passenger."',
         y=1856),
    win('The Combahee River raid',
        'In the Civil War she worked for the Union army as a nurse, scout and spy. In 1863 she guided gunboats up the '
        'Combahee River in South Carolina, in a raid that freed more than 700 enslaved people.',
        img='Raid on Combahee Ferry', y=1863, at='combahee'),
    life('Auburn',
         'After the war she lived in Auburn, New York. Poor herself, she cared for the old and the sick, and fought for '
         'women\'s right to vote. She died in 1913, aged about 91.',
         img='Harriet Tubman Home for the Aged', y=1913, at='auburn_ny'),
    legacy('Tubman freed herself, then risked her life again and again to free others. She is one of the great heroes of '
           'American history.',
           'Escaped slavery and led about 70 others to freedom',
           'Led an armed raid in the Civil War',
           "Fought for women's right to vote"),
)

story('leo-tolstoy', 'The count who wrote War and Peace, then tried to live like a peasant and preached non-violence.',
    life('A young count',
         'Leo Tolstoy was born in 1828 at Yasnaya Polyana, his family\'s estate south of Moscow. By nine he had lost both '
         'parents. He left university without a degree, gambled, drank and ran up debts.',
         img='Yasnaya Polyana', y=1828, at='yasnaya_polyana'),
    tale('The green stick',
         'When he was little, his older brother told him that the secret of how to make all people happy was written on a '
         'green stick, buried at the edge of a ravine on the estate. Tolstoy asked to be buried there, and he was.',
         y=1834, at='yasnaya_polyana'),
    life('A soldier at Sevastopol',
         'He joined the army, and in the Crimean War fought in the siege of Sevastopol. His sketches of the fighting, '
         'showing the horror of war, made him famous in Russia.',
         img='Siege of Sevastopol (1854–1855)', y=1855, at='sevastopol'),
    work('War and Peace',
         'From 1863 to 1869 he wrote War and Peace, a huge novel of Russia in the time of Napoleon\'s invasion, with more '
         'than 500 characters. His wife Sophia copied out his messy drafts by hand again and again.',
         img='War and Peace', y=1869, at='yasnaya_polyana'),
    work('Anna Karenina',
         'Anna Karenina, finished in 1877, begins: "Happy families are all alike; every unhappy family is unhappy in its own '
         'way." Many writers call it the greatest novel ever written.',
         img='Anna Karenina', y=1877, at='yasnaya_polyana'),
    life('A new life',
         'In his fifties, rich and famous, he fell into despair about the meaning of life. He turned to a simple faith of '
         'love and non-violence, gave up meat, drink and hunting, dressed like a peasant and worked in the fields.',
         y=1880, at='yasnaya_polyana'),
    win('Do not resist evil with violence',
        'His book The Kingdom of God Is Within You, of 1894, preached resisting evil without violence. It was banned in '
        'Russia, and in 1901 the Church cast him out. A young lawyer in South Africa, Gandhi, read it and was changed.',
        img='The Kingdom of God Is Within You', y=1894, at='moscow'),
    life('The last journey',
         'At 82, after years of quarrels with his wife over his will, he left home secretly one night in 1910. He fell ill '
         'on the train, and died at the little station of Astapovo, while reporters crowded outside.',
         y=1910, at='astapovo'),
    legacy('Tolstoy is one of the greatest novelists who ever lived, and his teaching of non-violence inspired Gandhi and '
           'Martin Luther King.',
           'Wrote War and Peace and Anna Karenina',
           'Preached non-violent resistance',
           'Inspired Gandhi'),
)

story('dmitri-mendeleev', 'The Siberian chemist who arranged the elements in the periodic table, and left gaps for new ones.',
    life('A boy from Siberia',
         'Dmitri Mendeleev was born in 1834 near Tobolsk, in Siberia, the youngest of at least 14 children. His father, a '
         'teacher, went blind, and his mother ran a glass factory to keep the family going.',
         y=1834, at='tobolsk'),
    tale("A mother's journey",
         'When the factory burned down, his mother took him, at 15, more than 2,000 km across Russia to find him a place at '
         'university, first in Moscow, then in St Petersburg. He got in, and she died soon after. He never forgot her.',
         y=1849, at='st_petersburg'),
    tale('Vodka and suitcases',
         'A popular myth says he set the strength of Russian vodka at 40 per cent. He did not, though his doctoral thesis '
         'was about mixing alcohol and water. His real hobby was making suitcases, and he was proud of them.',
         y=1865, at='st_petersburg'),
    made('The periodic table',
         'Writing a textbook in 1869, he put each of the 63 known elements on a card, with its weight and properties, and '
         'laid them out like a game of patience. He saw that properties repeat in a regular pattern.',
         'The periodic table organises all of chemistry, and hangs in every chemistry classroom in the world.',
         img='Periodic table', y=1869, at='st_petersburg'),
    made('Predicting new elements',
         'He left gaps in his table for elements nobody had found yet, and described what they would be like.',
         'Gallium, scandium and germanium were found within 17 years, just as he had said. The predictions convinced the '
         'world his table was a law of nature.',
         img='Gallium', y=1875, at='st_petersburg'),
    tale('Up in a balloon',
         'In 1887 he went up alone in a hydrogen balloon to watch a total eclipse of the Sun from above the clouds, though '
         'he had never flown one before.',
         y=1887),
    win('Element 101',
        'He narrowly missed the Nobel Prize in 1906, and died the next year. In 1955 a new element, number 101, was named '
        'mendelevium in his honour.',
        img='Mendelevium', y=1955),
    legacy("Mendeleev's periodic table brought order to the elements. It is the map of chemistry.",
           'Created the periodic table',
           'Predicted elements that had not yet been found',
           'Element 101, mendelevium, is named after him'),
)

story('claude-monet', 'The father of Impressionism, who painted light, haystacks and his water lily pond.',
    life('Caricatures in Le Havre',
         'Claude Monet was born in Paris in 1840 and grew up in the port of Le Havre. As a teenager he sold funny drawings '
         'of local people. The painter Eugène Boudin taught him to paint outdoors, in the open air.',
         y=1856, at='le_havre'),
    work('Impression, Sunrise',
         'In 1872 he painted the harbour of Le Havre in the morning mist, quickly and loosely. When it was shown, a critic '
         'mocked its title and called Monet and his friends "Impressionists". The name stuck.',
         img='Impression, Sunrise', y=1872, at='le_havre'),
    life('Poor years',
         'For years Monet and his wife Camille were so poor that he begged friends for money, and creditors seized his '
         'paintings. Camille, who posed for many of his pictures, died in 1879.',
         img='Woman with a Parasol – Madame Monet and Her Son', y=1875, at='argenteuil'),
    win('Painting light',
        'He painted the same haystacks, and later the front of Rouen Cathedral, again and again, at different hours and '
        'seasons. He worked on many canvases at once, switching as the light changed.',
        img='Haystacks (Monet series)', y=1891, at='giverny'),
    work('The garden at Giverny',
         'In 1883 he moved to Giverny, and made a garden with a pond full of water lilies and a Japanese bridge. He even '
         'changed the course of a stream to fill it. "My garden is my most beautiful masterpiece."',
         img='Bridge over a Pond of Water Lilies', y=1899, at='giverny'),
    tale('Fog in London',
         'He loved London fog. From his room at the Savoy hotel he painted the Thames and the Houses of Parliament dozens of '
         'times. Without fog, he said, London would not be a beautiful city.',
         img='Houses of Parliament (Monet series)', y=1900, at='london'),
    work('The water lilies',
         'In his last 30 years he painted his pond about 250 times. Even when cataracts clouded his eyes, he worked on '
         'giant water lily murals, which now fill two oval rooms in Paris.',
         img='Water Lilies (Monet series)', y=1920, at='giverny'),
    legacy('Monet led the Impressionists, who freed painting from strict rules and led the way to modern art.',
           'Founder of Impressionism',
           'Painted the Water Lilies',
           'Changed how painters capture light'),
)

story('thomas-edison', 'The inventor of the phonograph and the light bulb, with 1,093 patents to his name.',
    life('Taught at home',
         'Thomas Edison was born in 1847 in Milan, Ohio, and grew up in Port Huron, Michigan. He went to school for only a '
         'few months; when his teacher called him "addled", his mother took him out and taught him at home.',
         y=1847, at='milan_ohio'),
    tale('The lab on the train',
         'At 12 he sold newspapers and sweets on the train to Detroit, and set up a laboratory in the baggage car, until '
         'his chemicals set it on fire. As a boy he also began to go deaf.',
         y=1859, at='port_huron'),
    tale('Saving a boy',
         'In 1862 he snatched a three-year-old boy from the path of a train. To thank him, the boy\'s father, the station '
         'agent, taught him to work the telegraph, his first trade.',
         y=1862, at=(-82.88, 42.6), where='Mount Clemens'),
    win('The invention factory',
        'In 1876 he built a laboratory at Menlo Park, New Jersey, where teams of workers turned out inventions, aiming for '
        '"a minor invention every ten days and a big thing every six months". It was the first research lab of its kind.',
        y=1876, at='menlo_park'),
    made('The phonograph',
         'In 1877 he made a machine that recorded sound on a cylinder wrapped in tin foil. He shouted "Mary had a little '
         'lamb" into it, and it played his voice back.',
         'For the first time sound could be recorded and played again. It was the start of recorded music.',
         img='Phonograph', y=1877, at='menlo_park'),
    made('The light bulb',
         'Others had made electric lights, but they burned out fast. In 1879 his team tested thousands of materials, and '
         'found a carbon thread that glowed for many hours.',
         'With his power station in New York in 1882, electric light spread to homes, streets and factories, and night '
         'changed for ever.',
         img='Incandescent light bulb', y=1879, at='menlo_park'),
    life('The war of the currents',
         'He fought for his direct current against the alternating current of Westinghouse and Tesla. His side even killed '
         'animals with electricity in public to show that alternating current was deadly. Alternating current won.',
         y=1888, at='west_orange'),
    made('Moving pictures',
         'His lab at West Orange built the Kinetoscope, a box for watching short films through a peephole, and the first '
         'film studio, a black hut that turned to follow the Sun.',
         'They helped start the film industry.',
         img='Kinetoscope', y=1893, at='west_orange'),
    tale('Perspiration',
         '"Genius is one per cent inspiration and ninety-nine per cent perspiration," he said. He often worked through the '
         'night and slept in short naps on his lab bench.',
         y=1903, at='west_orange'),
    legacy("Edison's inventions brought electric light, recorded sound and films into everyday life, and his research "
           'lab became the model for modern industry.',
           'Invented the phonograph',
           'Made the light bulb practical and built the first power station',
           'Held 1,093 American patents'),
)

story('alexander-graham-bell', 'The teacher of the deaf who invented the telephone.',
    life('A family of speech',
         'Alexander Graham Bell was born in Edinburgh in 1847. His mother was going deaf, and his father and grandfather '
         'taught people how to speak well. His father invented a set of symbols for every sound the human mouth can make.',
         y=1847, at='edinburgh'),
    tale('The talking dog',
         'As a boy he taught the family dog to growl steadily while he moved its mouth with his hands, until it seemed to '
         'say "How are you, grandma?" With his brother he also built a talking head that cried "Mama!"',
         y=1863, at='edinburgh'),
    life('Teacher of the deaf',
         'After his two brothers died of tuberculosis, the family moved to Canada in 1870. He went on to Boston to teach '
         'deaf children to speak. One of his pupils, Mabel Hubbard, became his wife.',
         y=1871, at='boston'),
    made('The telephone',
         'Trying to send several telegraph messages along one wire, he found a way to turn the sound of a voice into a '
         'changing electric current, and back again. He filed his patent in 1876, hours before a rival.',
         'The telephone let people talk across cities and oceans, and changed business and daily life around the world.',
         img='Telephone', y=1876, at='boston'),
    tale('"Mr Watson, come here"',
         'On 10 March 1876 he spoke the first words by telephone, to his assistant in the next room: "Mr Watson, come here, '
         'I want to see you." Watson later said Bell had just spilled acid on his clothes.',
         img='Thomas A. Watson', cap='Thomas Watson, his assistant', y=1876, at='boston'),
    made('Talking on a beam of light',
         'In 1880 he sent his voice along a beam of sunlight with his photophone, which he called his greatest invention, '
         'greater than the telephone.',
         'It was the ancestor of fibre optics, the threads of glass that carry the internet today.',
         img='Photophone', y=1880, at='washington'),
    tale('Helen Keller',
         'In 1887 the parents of a deaf and blind six-year-old, Helen Keller, came to him for help. He sent them to a school '
         'for the blind, which sent a young teacher, Anne Sullivan. Keller later dedicated her life story to him.',
         img='Helen Keller', y=1887, at='washington'),
    tale('A boat that flew',
         'At his summer home in Nova Scotia he built giant kites and flying machines. In 1919 his team\'s hydrofoil boat set '
         'a world speed record on water, 114 km an hour.',
         img='HD-4', y=1919, at='baddeck'),
    tale('A minute of silence',
         'He thought the telephone a nuisance, and would not have one in his study. When he died in 1922, every telephone '
         'in North America was silent for one minute in his honour.',
         y=1922, at='baddeck'),
    legacy('Bell invented the telephone, and spent his life helping deaf people to communicate.',
           'Invented the telephone',
           'A lifelong teacher of the deaf',
           'Sent the first voice message on a beam of light'),
)

story('emperor-meiji', 'The emperor under whom Japan went from samurai to steamships in one lifetime.',
    life('A boy in Kyoto',
         'Mutsuhito was born in Kyoto in 1852. For centuries the emperors had lived shut away in Kyoto, while the shoguns '
         'ruled. The year after his birth, American warships arrived and forced Japan to open its ports to trade.',
         img='Kyoto Imperial Palace', y=1852, at='kyoto'),
    win('The Meiji Restoration',
        'He became emperor at 14. In 1868 rebels overthrew the last shogun and gave power back to the emperor. His reign '
        'was named Meiji, "enlightened rule", and he became known by it.',
        img='Meiji Restoration', y=1868, at='kyoto'),
    life('A new capital',
         "He moved from Kyoto to the shogun's city of Edo, renamed Tokyo, the eastern capital, and lived in the shogun's old "
         'castle. It is still the imperial palace.',
         img='Tokyo Imperial Palace', y=1869, at='tokyo'),
    win('Catching up with the West',
        'Japan abolished the samurai class and the old feudal lords, built railways, telegraphs and factories, opened '
        'schools for every child, and created a modern army and navy. In a single generation it became an industrial power.',
        img='Meiji era', y=1872, at='tokyo'),
    tale('A modern emperor',
         'He cut his topknot, grew a beard, wore Western uniforms and ate beef, to show his people new ways. He hated being '
         'photographed, so his official portrait was a photograph of a drawing.',
         y=1873, at='tokyo'),
    win('A constitution',
        'In 1889 he gave Japan a constitution and an elected parliament, the first in East Asia, modelled partly on '
        "Germany's.",
        img='Meiji Constitution', y=1889, at='tokyo'),
    win('A world power',
        'Japan defeated China in 1895 and took Taiwan. In 1905 it shocked the world by beating Russia, the first time in '
        'modern history an Asian country had defeated a European great power. In 1910 it took over Korea.',
        img='Battle of Tsushima', y=1905),
    tale('A poet emperor',
         'He wrote around 100,000 short poems, called waka, in his lifetime.',
         y=1904, at='tokyo'),
    life('The end of an era',
         'He died in 1912. On the day of his funeral, General Nogi, a hero of the war with Russia, and his wife took their '
         'own lives to follow their emperor, in the old samurai way. The Meiji Shrine in Tokyo honours him.',
         img='Meiji Shrine', y=1912, at='tokyo'),
    legacy('In his 45-year reign Japan went from an isolated land of samurai to a modern industrial nation and empire, '
           'the first outside the West to do so.',
           'Reigned during the Meiji Restoration',
           'Japan modernised in a single generation',
           'Japan became a world power'),
)

story('vincent-van-gogh', 'He painted The Starry Night and Sunflowers, and is said to have sold just one painting in his life.',
    life("A pastor's son",
         'Vincent van Gogh was born in 1853 in Zundert, in the Netherlands, the son of a pastor. He worked for art dealers '
         'in The Hague, London and Paris, but was sacked, and tried to become a preacher.',
         y=1853, at='zundert'),
    life('Among the miners',
         'In 1879 he preached to coal miners in the Borinage, in Belgium, gave away his clothes and slept on straw. The '
         'church dismissed him for being too extreme. At 27 he decided to become an artist.',
         y=1880, at='borinage'),
    work('The Potato Eaters',
         'His early paintings were dark pictures of peasants and weavers. In 1885 in Nuenen he painted a poor family eating '
         'potatoes by lamplight, with hands, he said, that had dug the earth.',
         img='The Potato Eaters', y=1885, at='nuenen'),
    life('Theo',
         'His younger brother Theo, an art dealer in Paris, sent him money all his life, and Vincent wrote him more than 600 '
         'letters. In Paris he met the Impressionists, and his colours turned bright.',
         img='Theo van Gogh (art dealer)', cap='Theo, his brother', y=1886, at='paris'),
    work('Sunflowers',
         'In 1888 he moved to Arles, in the south of France, dazzled by its light. He painted Sunflowers to decorate the '
         'room for his friend, the painter Paul Gauguin, who came to stay.',
         img='Sunflowers (Van Gogh series)', y=1888, at='arles'),
    life('The ear',
         'Van Gogh suffered from mental illness. In December 1888, after a quarrel with Gauguin, he had a breakdown and cut '
         'off his left ear with a razor. Gauguin left Arles.',
         img='Self-Portrait with Bandaged Ear', y=1888, at='arles'),
    work('The Starry Night',
         'In 1889 he chose to go into a hospital at Saint-Rémy. From his window he painted The Starry Night, with swirling '
         'stars and a crescent moon over a sleeping village.',
         img='The Starry Night', y=1889, at='saint_remy'),
    life('Two thousand works',
         'In ten years he made about 2,100 works, among them some 860 oil paintings, most of them in his last two years. In '
         'July 1890, at Auvers, he died of a gunshot wound, most likely by his own hand. He was 37.',
         img='Wheatfield with Crows', y=1890, at='auvers'),
    legacy('Van Gogh\'s bold colours and swirling brushstrokes made him one of the most famous painters who ever lived. '
           'His paintings now sell for tens of millions.',
           'Painted The Starry Night and Sunflowers',
           'Made about 860 paintings in ten years',
           'A pioneer of modern art'),
)

story('nikola-tesla', 'The genius behind alternating current, radio control and the Tesla coil.',
    life('Born in a storm',
         'Nikola Tesla was born at midnight during a lightning storm in 1856, in Smiljan, in today\'s Croatia, the son of a '
         'Serbian priest. A family legend says the midwife called him a child of the storm, and his mother answered: '
         '"No, of light."',
         y=1856, at='smiljan'),
    tale('Machines in his head',
         'He could memorise whole books, and pictured machines in his mind so clearly that he could build and test them '
         'there before making them. At college in Graz he gambled away his money and left without a degree.',
         y=1875, at='graz'),
    made('The spinning magnetic field',
         'In 1882, walking in a park in Budapest and reciting poetry, he suddenly saw how to make a motor run on alternating '
         'current. He drew it in the sand with a stick.',
         'His induction motor still drives most of the machines in the world, from fans and pumps to factories.',
         img='Induction motor', y=1882, at='budapest'),
    life('Working for Edison',
         'In 1884 he arrived in New York with four cents in his pocket, and went to work for Edison. Tesla said he was '
         'promised 50,000 dollars to improve Edison\'s machines, and when he did, Edison laughed that it was a joke. He quit.',
         y=1884, at='new_york'),
    win('Alternating current wins',
        'Westinghouse bought his patents. Alternating current could carry power over long distances. It lit up the '
        'Chicago World\'s Fair in 1893, and in 1896 power from Niagara Falls reached Buffalo. It powers the world today.',
        img='Adams Power Plant Transformer House', y=1896, at='niagara'),
    made('Radio control',
         'In 1898 in New York he steered a model boat by radio. People watching thought it was magic, or that a trained '
         'monkey was hidden inside. He also invented the Tesla coil.',
         'Remote control, and much of radio, grew from ideas like his.',
         img='Tesla coil', y=1898, at='new_york'),
    tale('Lightning in Colorado',
         'In 1899 in Colorado Springs he built a giant coil that threw artificial lightning bolts dozens of metres long. '
         'He also thought he had picked up signals from Mars.',
         y=1899, at='colorado_springs'),
    life('The tower',
         'He dreamed of sending messages and power through the air around the world, free. He began a giant tower on Long '
         'Island, but his backer, the banker J. P. Morgan, stopped paying. The tower was torn down.',
         img='Wardenclyffe Tower', y=1901, at='wardenclyffe'),
    life('The pigeons',
         'In old age he lived alone in New York hotels, in debt, feeding the pigeons in the parks. He said he loved one '
         'white pigeon as a man loves a woman. He died poor in 1943.',
         y=1943, at='new_york'),
    legacy("Tesla's alternating current system powers the world. A unit of magnetism, the tesla, is named after him, and "
           'so is a car company.',
           'Invented the induction motor',
           "Made alternating current the world's power system",
           'A pioneer of radio and remote control'),
)

story('sigmund-freud', 'The Viennese doctor who explored the unconscious mind and invented psychoanalysis.',
    life('The golden boy',
         'Sigmund Freud was born in 1856 in Freiberg, in Moravia, now Příbor in the Czech Republic, the eldest of eight '
         'children of a Jewish wool merchant and his young wife. The family moved to Vienna when he was four.',
         y=1856, at='pribor'),
    tale('Four hundred eels',
         'As a young scientist he spent weeks in Trieste cutting open some 400 eels, looking for their male organs, which '
         'nobody had found. He did not find them either.',
         y=1876, at='trieste'),
    life('The talking cure',
         'He trained as a doctor of the nerves. In 1885 in Paris he watched the famous doctor Charcot treat patients with '
         'hypnosis. Back in Vienna, he found that patients often got better when they talked freely about painful memories.',
         y=1885, at='paris'),
    made('Psychoanalysis',
         'His patients lay on a couch and said whatever came into their minds. Much of the mind, he argued, is unconscious, '
         'and hidden wishes and fears from childhood shape what we do.',
         'It gave rise to talking therapy, and to words we all use, such as ego, denial and a Freudian slip.',
         img='Freud Museum', y=1896, at='vienna'),
    work('The Interpretation of Dreams',
         'In 1899 he published The Interpretation of Dreams, arguing that dreams are disguised wishes, "the royal road to the '
         'unconscious". It sold only 351 copies in six years.',
         img='The Interpretation of Dreams', y=1899, at='vienna'),
    tale('Sometimes a cigar',
         'He smoked about 20 cigars a day. He is supposed to have said that "sometimes a cigar is just a cigar", but no one '
         'has found that he ever did. The cigars gave him mouth cancer, and he had more than 30 operations.',
         y=1923, at='vienna'),
    life('Escape from the Nazis',
         'When Nazi Germany took Austria in 1938, the secret police questioned his daughter Anna. Friends paid for the '
         'family to escape to London. Four of his sisters, left behind, were murdered in the Holocaust. He died in London in '
         '1939.',
         y=1938, at='london'),
    legacy("Freud's ideas about the unconscious changed psychology, medicine, art and literature, though many of his "
           'theories are now disputed.',
           'Founded psychoanalysis',
           'Explored the unconscious mind and dreams',
           'Inspired modern talking therapy'),
)

story('rabindranath-tagore', 'The Bengali poet who was the first non-European Nobel winner, and wrote two national anthems.',
    life('The youngest of 13',
         'Rabindranath Tagore was born in Calcutta in 1861, the youngest of 13 children in a rich and gifted Bengali family. '
         'He hated school and was taught at home. He wrote his first poems at eight.',
         y=1861, at='kolkata'),
    life('A law student who left',
         'In 1878 he was sent to England to become a lawyer. He left without a degree, but came home in love with English '
         'books and Irish and Scottish songs.',
         y=1878, at='london'),
    life('On the river',
         'In the 1890s he ran his family\'s estates in the countryside of Bengal, living on a houseboat on the river Padma, '
         'and wrote short stories about the villagers he met.',
         y=1891, at=(89.25, 23.92), where='Shelaidaha'),
    win('A school under the trees',
        'In 1901 he started a school at Santiniketan where classes were held outdoors, under the trees. It grew into a '
        'university, Visva-Bharati.',
        img='Visva-Bharati University', y=1901, at='santiniketan'),
    win('The Nobel Prize',
        'His book of poems Gitanjali, "Song Offerings", which he translated into English himself, won the Nobel Prize in '
        'Literature in 1913. He was the first person from outside Europe to win a Nobel Prize.',
        img='Gitanjali', y=1913, at='santiniketan'),
    song('Two national anthems',
         'He wrote more than 2,000 songs. Two of them became the national anthems of India and of Bangladesh, and the '
         'writer of Sri Lanka\'s anthem was his student. This is India\'s anthem, Jana Gana Mana.',
         page='Jana Gana Mana', y=1911, at='kolkata'),
    life('Giving back his knighthood',
         'The British knighted him in 1915. In 1919, after British troops shot hundreds of unarmed people at Amritsar, he '
         'gave the knighthood back in protest.',
         img='Jallianwala Bagh massacre', y=1919, at='amritsar'),
    tale('Gandhi and Einstein',
         'He is said to have given Gandhi the name Mahatma, "great soul". In 1930 he met Albert Einstein near Berlin, and '
         'the two argued about whether truth and beauty exist without people to see them.',
         y=1930, at='berlin'),
    work('A painter at 67',
         'In old age he began to doodle on his manuscripts, and the doodles became paintings. He made more than 2,000 '
         'pictures, shown in Paris, Moscow and New York.',
         y=1930, at='santiniketan'),
    legacy('Tagore reshaped the literature and music of Bengal, was the first Nobel winner from outside Europe, and his '
           'songs are sung by two nations.',
           'First Nobel Prize winner from outside Europe',
           'Wrote the national anthems of India and Bangladesh',
           'Founded the university at Santiniketan'),
)

from _lib import story, life, win, made, work, song, tale, legacy

story('jesus', 'The teacher from Nazareth whose life and death gave rise to Christianity.',
    life('Born in Bethlehem',
         'The Gospels say Jesus was born in Bethlehem around 4 BC, in the reign of King Herod, to Mary, a young woman '
         'engaged to Joseph, a carpenter of Nazareth. He was laid in a manger because there was no room at the inn, and '
         'visited by shepherds and by wise men from the east who had followed a star.',
         img='Church of the Nativity', y=-4, at='bethlehem'),
    life('The carpenter of Nazareth',
         'He grew up in Nazareth in Galilee, probably working as a builder like Joseph. At about 30 he was baptised by '
         'his cousin John the Baptist in the River Jordan, and then, the Gospels say, spent forty days fasting in the '
         'desert.',
         img='Baptism of Jesus', y=26, at=(35.55, 31.84), where='River Jordan'),
    win('Teaching in Galilee',
        'He chose twelve disciples, several of them fishermen, and taught by the Sea of Galilee in parables, short stories '
        'like the Good Samaritan and the Prodigal Son. In the Sermon on the Mount he said: "Blessed are the meek", "Love '
        'your enemies" and "Do to others as you would have them do to you."',
        img='Sermon on the Mount', y=28, at='capernaum'),
    tale('Miracles',
         'The Gospels tell of miracles: healing the blind and lepers, feeding 5,000 people with five loaves and two fish, '
         'walking on water and raising his friend Lazarus from the dead. Crowds followed him, and he shocked respectable '
         'people by eating with tax collectors, outcasts and the poor.',
         img='Feeding the multitude', y=29),
    life('The Last Supper',
         'Around AD 30 he entered Jerusalem for the Passover festival, cheered by crowds waving palm branches, and '
         'overturned the tables of the money changers in the Temple. At a last meal with his disciples he shared bread '
         'and wine, and foretold that one of them would betray him.',
         img='Last Supper', y=30, at='jerusalem'),
    life('The cross',
         'Judas led the Temple guards to him at night in a garden. Accused of claiming to be king of the Jews, he was '
         'sentenced by the Roman governor, Pontius Pilate, and crucified outside the city walls between two thieves.',
         img='Crucifixion of Jesus', y=30, at='jerusalem'),
    life('The empty tomb',
         "The Gospels say that on the third day his tomb was found empty, and that he appeared to his followers before "
         'rising into heaven. Christians celebrate the resurrection at Easter, the most important day of their year.',
         img='Resurrection of Jesus', y=30, at='jerusalem'),
    legacy('The faith his followers spread has grown into the largest religion in the world, with over two billion '
           'Christians. His teachings on love, forgiveness and care for the poor shaped Western art, law and ethics.',
           "The founder of Christianity, the world's largest religion",
           'Taught love of enemies and the Golden Rule',
           'Our calendar counts the years from his birth'),
)

story('saint-peter', 'The fisherman Jesus called "the rock", remembered as the first pope.',
    life('A fisherman of Galilee',
         'Simon was a fisherman on the Sea of Galilee, working with his brother Andrew. The Gospels say Jesus walked by '
         'and called to them: "Follow me, and I will make you fishers of men." They left their nets and followed him.',
         img='Sea of Galilee', y=28, at='capernaum'),
    tale('The rock',
         'Jesus gave Simon a new name, Peter, from the Greek word for rock: "On this rock I will build my church." He '
         'also promised him "the keys of the kingdom of heaven", which is why artists paint Peter holding two keys, and '
         'why jokes about heaven put him at the gate.',
         img='Keys of Heaven', y=29),
    tale('Walking on water',
         "Peter was bold and quick to act. Matthew's Gospel says that when Jesus came walking on the lake at night, Peter "
         'stepped out of the boat to meet him, then took fright at the wind and began to sink. Jesus caught his hand: '
         '"You of little faith, why did you doubt?"',
         img='Jesus walking on water', y=29),
    life('Three denials',
         "When Jesus was arrested, Peter followed to the high priest's courtyard. Three times people asked if he was one "
         'of Jesus\'s friends, and three times Peter denied it. Then a rooster crowed, as Jesus had said it would, and Peter '
         'went out and wept bitterly.',
         img='Denial of Peter', y=30, at='jerusalem'),
    win('Leader of the first Christians',
        "After Jesus's death, Peter led his followers in Jerusalem. The Book of Acts says that at the feast of Pentecost "
        'he preached to the crowds, and 3,000 people were baptised in a single day. He later went to Antioch and, '
        'tradition says, to Rome.',
        img='Pentecost', y=33, at='jerusalem'),
    life('Upside down',
         'Tradition says Peter was killed in Rome under the emperor Nero around AD 64. Feeling unworthy to die in the '
         'same way as Jesus, he asked to be crucified upside down. St Peter\'s Basilica was later built over the place '
         'believed to be his grave.',
         img='Crucifixion of Saint Peter (Caravaggio)', y=64, at='rome'),
    legacy('Catholics regard Peter as the first pope, and every pope since as his successor. The church over his grave, '
           "St Peter's in Rome, is the heart of the Catholic Church.",
           'One of the twelve apostles of Jesus',
           'Leader of the first Christians',
           'Remembered as the first pope',
           img="St. Peter's Basilica"),
)

story('paul-the-apostle', 'The persecutor turned apostle, who carried Christianity across the Roman world.',
    life('Saul the persecutor',
         'Saul was a Jew from Tarsus, in what is now Turkey, and a Roman citizen. He trained as a Pharisee in Jerusalem '
         'and made tents for a living. He hunted down the followers of Jesus, and stood by approving as the first '
         'Christian martyr, Stephen, was stoned to death.',
         img='Saint Stephen', y=34, at='jerusalem'),
    tale('The road to Damascus',
         'Riding to Damascus to arrest Christians, Saul was struck to the ground by a blinding light and heard a voice: '
         '"Saul, Saul, why do you persecute me?" Blind for three days, he was healed and baptised. A "road to Damascus" '
         'moment still means a sudden change of heart.',
         img='Conversion of Paul the Apostle', y=36, at='damascus'),
    tale('Over the wall in a basket',
         'He began to preach about Jesus in Damascus, and his old allies plotted to kill him. They watched the city gates '
         'day and night, so his friends lowered him down the outside of the city wall in a basket, after dark.',
         y=37, at='damascus'),
    win('The missionary journeys',
        'Now called Paul, he made three great journeys, perhaps 16,000 kilometres on foot and by ship, founding churches '
        'across Asia Minor and Greece: at Ephesus, Corinth, Philippi and Thessalonica. He insisted that non-Jews could '
        'become Christians without following Jewish law.',
        img='Ephesus', y=50, at='ephesus'),
    work('The letters',
         'He wrote letters to the churches he had founded; thirteen books of the New Testament carry his name. One to the '
         'Corinthians holds his most famous words: "Love is patient, love is kind... And now these three remain: faith, '
         'hope and love. But the greatest of these is love."',
         img='Pauline epistles', y=55, at='corinth'),
    life('Shipwreck, and Rome',
         'Arrested in Jerusalem, he used his right as a Roman citizen to be judged by the emperor. Sailing to Rome as a '
         'prisoner, he was shipwrecked on Malta. In Rome he lived two years under guard, and tradition says he was '
         'beheaded there under Nero.',
         img='Basilica of Saint Paul Outside the Walls', y=64, at='rome'),
    legacy('Paul did more than anyone to turn a small Jewish movement into a faith open to every people. His letters are '
           'the oldest Christian writings and have shaped Christian belief ever since.',
           'Spread Christianity across the Roman world',
           'Wrote much of the New Testament',
           'Opened the faith to non-Jews'),
)

story('boudica', 'The warrior queen of Britain who burned Roman London.',
    life('Queen of the Iceni',
         'Boudica was the wife of Prasutagus, king of the Iceni, a Celtic people of eastern Britain. A Roman writer '
         'described her as very tall, with a harsh voice and a mass of red hair down to her hips, wearing a heavy gold '
         'necklace and a many-coloured cloak.',
         img='Iceni', y=55, at=(1.29, 52.58), where='Norfolk'),
    life('Wronged by Rome',
         'When Prasutagus died around AD 60, he left half his kingdom to the Roman emperor, hoping to protect his family. '
         'Instead Roman officials seized everything. Boudica was flogged, and her two daughters were raped.',
         y=60, at=(1.29, 52.58), where='Norfolk'),
    win('The revolt',
        'With the Roman governor away in Wales, Boudica raised the Iceni and their neighbours. They burned Colchester, '
        'the Roman capital, then London and St Albans, killing perhaps 70,000 people. Under London, archaeologists still '
        'find a layer of red, burned earth from her attack.',
        img='Boudican revolt', y=60, at='london'),
    life('The last battle',
         'The governor marched back with about 10,000 soldiers and chose his ground in a narrow valley. Boudica\'s huge '
         'army charged, but was cut to pieces; the Romans claimed 80,000 dead. Boudica is said to have taken poison rather '
         'than be captured.',
         y=61),
    tale('A queen in bronze',
         'For centuries she was almost forgotten. Then the Roman histories were rediscovered, and in Queen Victoria\'s '
         'time Boudica became a national heroine. In 1902 a bronze statue of her in a chariot with scythes on its wheels '
         'was put up beside the Houses of Parliament.',
         img='Boadicea and Her Daughters', y=1902, at='westminster'),
    legacy("Boudica's revolt nearly drove the Romans out of Britain. She became a symbol of resistance to invaders, and "
           'of a woman leading her people into battle.',
           'Led a great revolt against Roman rule',
           'Burned Roman London',
           'A British symbol of courage and freedom'),
)

story('cai-lun', 'The court official honoured for giving the world paper.',
    life('A palace official',
         'Cai Lun was a eunuch at the Han court in Luoyang, where he rose to run the workshop that made weapons and tools '
         'for the emperor. Books were then written on heavy bundles of bamboo strips, or on silk, which was very costly.',
         img='Bamboo and wooden slips', y=89, at='luoyang'),
    made('Paper',
         'In AD 105 he showed the emperor a writing material made by pounding tree bark, hemp, old rags and fishing nets '
         'into pulp, spreading it on a screen and drying it.',
         'Paper was cheap, light and easy to make. It reached the Islamic world in the 700s and Europe in the 1100s, and '
         'made printed books and newspapers possible.',
         img='Paper', y=105, at='luoyang'),
    tale('Older than Cai Lun',
         'Archaeologists have found scraps of paper in China from 200 years before him, one with a map drawn on it. He did '
         'not invent paper from nothing, but he improved the method, and the court took it up, so the honour went to him.',
         img='History of paper'),
    life('Robes and poison',
         'Cai Lun rose high at court, but years before he had joined a plot against the grandmother of a later emperor. '
         'When that emperor took power in 121, he summoned Cai Lun to prison. Instead, Cai Lun bathed, put on his finest '
         'robes and drank poison.',
         y=121, at='luoyang'),
    tale('Paper goes west',
         'A famous story says that after the Battle of Talas in 751, Chinese prisoners taught their Arab captors to make '
         'paper in Samarkand. Paper mills soon spread to Baghdad, Cairo and Muslim Spain, and from there into Europe.',
         img='Battle of Talas', y=751, at='samarkand'),
    legacy('Paper is one of the Four Great Inventions of China, and for 2,000 years it has carried the world\'s knowledge, '
           'money and letters. Cai Lun is still honoured as its father.',
           'Made paper practical in AD 105',
           'Allowed books and learning to spread across the world',
           'One of the Four Great Inventions of China'),
)

story('marcus-aurelius', 'The philosopher emperor who wrote notes to himself on how to live.',
    life('The most truthful boy',
         'Marcus was born in Rome in 121 to a rich family. Emperor Hadrian noticed him early and nicknamed him '
         '"Verissimus", "most truthful". At 12 he took up the plain life of a philosopher, wearing a rough cloak and '
         'sleeping on the ground, until his mother persuaded him to use a bed.',
         img='Hadrian', cap='Hadrian, who picked him out as a boy', y=133, at='rome'),
    life('Two emperors at once',
         'Adopted by Emperor Antoninus Pius, he became emperor in 161, and at once shared power with his adopted brother, '
         'Lucius Verus. It was the first time Rome had two emperors at the same time.',
         img='Lucius Verus', y=161, at='rome'),
    life('Plague and war',
         'His reign was full of trouble. Soldiers coming back from the East brought a plague, perhaps smallpox, that '
         'killed millions across the empire. Germanic tribes broke across the Danube, and Marcus spent most of his last '
         'years in army camps on the frontier.',
         img='Antonine Plague', y=166),
    work('The Meditations',
         'At night in his tent he wrote notes to himself in Greek, never meant to be published, on how to live well: "You '
         'have power over your mind, not outside events. Realise this, and you will find strength." They survive as the '
         'Meditations, one of the best-loved books of philosophy.',
         img='Meditations', y=172, at=(16.86, 48.11), where='Carnuntum'),
    tale('The rain miracle',
         'In 172 a Roman army was trapped by Germanic warriors and dying of thirst. Suddenly a storm burst, giving the '
         'Romans rain to drink while lightning struck the enemy. Christians and pagans each said their own god had sent '
         'it. The scene is carved on his column in Rome.',
         img='Column of Marcus Aurelius', y=172),
    life('The end of a golden age',
         'He died in 180 on the Danube frontier, aged 58. His son Commodus, the villain of the film Gladiator, was a '
         'disaster, and historians mark the death of Marcus as the end of the golden age of Rome.',
         img='Equestrian Statue of Marcus Aurelius', y=180, at='vienna'),
    legacy('Marcus Aurelius was the last of the "Five Good Emperors", the philosopher king Plato dreamed of. His '
           'Meditations are read today by millions, from soldiers to athletes, as a guide to staying calm and doing one\'s duty.',
           'Last of the Five Good Emperors',
           'Wrote the Meditations',
           'A model of the Stoic philosophy of calm and duty'),
)

story('constantine-the-great', 'The first Christian emperor, who founded Constantinople.',
    life('Raised at court',
         'Constantine was born around 272 at Naissus, in what is now Serbia, son of a Roman officer, Constantius, and '
         'Helena, a woman of humble birth. He grew up at the court of Emperor Diocletian, almost a hostage, while his '
         'father rose to rule the western empire.',
         img='Diocletian', y=285, at='nicomedia'),
    life('Hailed at York',
         'When his father died at York in 306, the soldiers proclaimed Constantine emperor. The empire was then split '
         'between several rival emperors, and it took him 18 years of war to beat them all.',
         img='York Minster', cap='York, where his soldiers hailed him', y=306, at='york'),
    tale('In this sign, conquer',
         'Before a battle for Rome in 312, Constantine said he saw a cross of light in the sky with the words "In this '
         'sign, conquer". He had his soldiers paint a Christian symbol on their shields, and beat his rival Maxentius at '
         'the Milvian Bridge, where Maxentius drowned in the Tiber.',
         img='Battle of the Milvian Bridge', y=312, at='rome'),
    win('Freedom for Christians',
        'In 313, with his fellow emperor Licinius, he issued the Edict of Milan, letting everyone worship as they wished '
        'and giving back property taken from Christians. Only ten years earlier, Diocletian had been burning churches and '
        'killing Christians.',
        img='Edict of Milan', y=313, at='milan'),
    win('The Council of Nicaea',
        'In 325 he called bishops from all over the empire to Nicaea to settle a bitter quarrel about whether Jesus was '
        'equal to God the Father. The Nicene Creed they agreed on is still said in churches every Sunday.',
        img='First Council of Nicaea', y=325, at='nicaea'),
    win('New Rome',
        'In 330 he made the old Greek town of Byzantium his new capital, New Rome. Everyone called it Constantinople, '
        '"the city of Constantine". It stayed the capital of the Roman, then Byzantine, Empire for 1,100 years, and is '
        'now Istanbul.',
        img='Constantinople', y=330, at='constantinople'),
    life('Baptised at the end',
         'He put off being baptised until he was dying, in 337, perhaps so that the sins of a lifetime as emperor would be '
         'washed away all at once. He was buried among memorials to the twelve apostles, as if he were the thirteenth.',
         y=337, at='nicomedia'),
    legacy('Constantine was the first Christian emperor, and he set Christianity on its way to becoming the religion of '
           'Europe. His city carried the Roman Empire on in the east for over a thousand years.',
           'First Roman emperor to become a Christian',
           'Ended the persecution of Christians',
           'Founded Constantinople',
           img='Colossus of Constantine', cap='The head of his giant statue in Rome'),
)

story('augustine-of-hippo', 'The restless young man who became the greatest thinker of the early Church.',
    life('A boy from North Africa',
         'Augustine was born in 354 at Thagaste, in what is now Algeria, to a pagan father and a Christian mother, Monica. '
         'A brilliant student, he went to Carthage to study the art of speaking, and became a teacher of it.',
         img='Saint Monica', cap='His mother, Monica', y=354, at='thagaste'),
    tale('The stolen pears',
         'In his Confessions he remembers how, at 16, he and his friends stole pears from a neighbour\'s tree, not because '
         'they were hungry, but for the thrill of doing wrong. They threw most of them to the pigs. He spent pages trying '
         'to work out why.',
         img='Pear', y=370, at='thagaste'),
    tale('But not yet',
         'As a young man he lived with a woman for 15 years and had a son, and joined a strange sect, the Manichees. He '
         'wanted to be good, but prayed: "Give me chastity and self-control, but not yet." His mother prayed and wept for '
         'him for years.',
         img='Manichaeism', y=373, at='carthage'),
    life('Take up and read',
         "In a garden in Milan in 386, in tears, he heard a child's voice singing \"Take up and read\". He opened Paul's "
         'letters at random and read words telling him to give up drunkenness and lust. His doubts vanished, and Bishop '
         'Ambrose baptised him the next Easter.',
         img='Ambrose', cap='Ambrose, the bishop who baptised him', y=386, at='milan'),
    life('Bishop of Hippo',
         'Back in Africa, he became bishop of the port of Hippo in 395 and served there for 35 years, preaching, judging '
         'quarrels and writing more than five million words. He died in 430 while the Vandals were besieging the city.',
         img='Hippo Regius', y=395, at='hippo'),
    work('Confessions and The City of God',
         'His Confessions, the story of his own life written as a prayer, is often called the first autobiography in the '
         'West. After the Goths sacked Rome in 410, he wrote The City of God: cities of men rise and fall, but the city of '
         'God lasts forever.',
         img='Confessions (Augustine)', y=397),
    legacy('Augustine is the most influential Christian thinker after Paul. His ideas on grace, sin, time and the "just '
           'war" shaped both Catholic and Protestant thought for 1,600 years.',
           'Wrote the Confessions, the first Western autobiography',
           'Wrote The City of God',
           'Shaped Christian thought for 1,600 years'),
)

story('attila', 'The king of the Huns, called the Scourge of God.',
    life('King of the Huns',
         'Attila was born around 406 into the ruling family of the Huns, horsemen from the steppes who had swept into '
         'Europe. In 434 he and his brother Bleda inherited the throne. Around 445 Bleda died, probably murdered by '
         'Attila, who ruled alone from the plains of Hungary.',
         img='Huns', y=434),
    win('Scourge of God',
        'His armies of mounted archers ravaged the Eastern Roman Empire, destroying dozens of cities in the Balkans, and '
        'forced the emperor to pay him 2,100 pounds of gold a year. Christians called him the Scourge of God, sent to '
        'punish them for their sins.',
        img='Hunnic Empire', y=447, at='constantinople'),
    tale('A ring and a proposal',
         "In 450 Honoria, the Western Roman emperor's sister, sent Attila her ring and begged him to save her from a "
         'marriage she did not want. Attila said this was a proposal, and demanded half of the Western Empire as his '
         'dowry. When he was refused, he invaded Gaul.',
         img='Justa Grata Honoria', y=450, at='ravenna'),
    life('The Catalaunian Plains',
         'In 451, deep in Gaul, he was met by an army of Romans and Visigoths under the general Aetius on the Catalaunian '
         'Plains. It was one of the bloodiest battles of the age, and Attila pulled back.',
         img='Battle of the Catalaunian Plains', y=451, at=(4.36, 48.96), where='Catalaunian Plains'),
    tale('Turned back from Rome',
         'In 452 he invaded Italy and destroyed the city of Aquileia; its refugees fled into the lagoons and helped found '
         'Venice. Pope Leo I rode out to meet him, and Attila turned back without attacking Rome. Legend says Saints '
         'Peter and Paul appeared beside the pope with swords.',
         img='The Meeting of Leo the Great and Attila', y=452, at='mantua'),
    life('Death on his wedding night',
         'In 453 he married a young woman named Ildico. In the morning he was found dead, choked by a burst blood vessel. '
         'Legend says he was buried in three coffins, of gold, silver and iron, and that the men who buried him were '
         'killed to keep the place a secret.',
         y=453),
    legacy("Attila's empire fell apart soon after his death, but his raids helped weaken the Western Roman Empire, which "
           'fell 23 years later. His name became a byword for a ruthless conqueror.',
           'Ruled the Hunnic Empire at its height',
           'Ravaged the Balkans, Gaul and Italy',
           'Helped bring down the Western Roman Empire'),
)

story('aryabhata', "The Indian astronomer who said the Earth spins, and helped give the world its numbers.",
    life('A young astronomer',
         'Aryabhata was born in 476, and wrote that he finished his great book at the age of 23, in 499. He worked at '
         'Kusumapura, near Pataliputra, then a centre of learning of the Gupta Empire, the golden age of classical India.',
         img='Gupta Empire', y=499, at='pataliputra'),
    work('The Aryabhatiya',
         'His book, the Aryabhatiya, packs mathematics and astronomy into 121 short verses, easy to learn by heart. It '
         'covers arithmetic, algebra and trigonometry, and how to work out the movements of the Sun, Moon and planets.',
         img='Aryabhatiya', y=499),
    made('Pi and place value',
         'He gave pi as 62,832 divided by 20,000, which is 3.1416, and said it was only close. He wrote numbers in a '
         'place-value system, where a digit\'s position gives its worth.',
         'Indian place-value numbers with zero, carried west by Arab scholars, became the digits the whole world uses '
         'today.',
         img='Hindu–Arabic numeral system', y=499),
    made('The spinning Earth',
         'He said the Earth turns on its axis every day, and the stars only seem to move, as the shore seems to move to '
         'a man in a boat. He explained eclipses as shadows.',
         'Most astronomers rejected the spinning Earth for 1,000 years, but his tables for predicting eclipses and '
         'planets were used across India and the Islamic world.',
         img='Lunar eclipse', y=499),
    tale('A satellite named after him',
         "In 1975 India launched its first satellite and named it Aryabhata. A picture of it was printed on India's "
         'two-rupee note.',
         img='Aryabhata (satellite)', y=1975),
    legacy('Aryabhata was the first of the great mathematician astronomers of classical India. His work on numbers, pi, '
           'sines and the turning Earth was translated into Arabic and shaped the mathematics of the Islamic world and Europe.',
           'Wrote the Aryabhatiya at 23',
           'Gave pi as 3.1416',
           'Said the Earth spins on its axis'),
)

story('justinian-i', 'The emperor who built Hagia Sophia and wrote down Roman law.',
    life("A peasant's nephew",
         'Justinian was born around 482 to a peasant family in the Balkans. His uncle Justin, a farm boy who rose to '
         'command the palace guard, became emperor in 518 and brought him to Constantinople to be educated. Justinian '
         'took the throne in 527.',
         img='Justin I', y=527, at='constantinople'),
    tale('The actress empress',
         'He married Theodora, a former actress, a scandalous job at the time; a law had to be changed to allow it. She '
         'became his closest adviser. In the Nika riots of 532, when he was ready to flee the city, she said: "Royalty is '
         'a fine burial shroud." He stayed, and the riot was crushed.',
         img='Theodora (wife of Justinian I)', y=532, at='constantinople'),
    work('Hagia Sophia',
         'The rioters had burned the great church of the city. Justinian rebuilt it as Hagia Sophia, "Holy Wisdom", in '
         'under six years, with a dome so vast it seemed to hang from heaven. Entering, he is said to have cried: '
         '"Solomon, I have outdone you!" For 1,000 years it was the largest church in the world.',
         img='Hagia Sophia', y=537, at='constantinople'),
    win('The law code',
        'He had all of Roman law collected, sorted and simplified into one Body of Civil Law. Rediscovered in Italy around '
        '1070, it became the foundation of law in most of Europe, and in countries from Brazil to Japan.',
        img='Corpus Juris Civilis', y=534),
    win('Winning back the West',
        'His general Belisarius took back North Africa from the Vandals, then fought for years to win back Italy from '
        'the Goths, and part of Spain was taken too. For a moment the Mediterranean was a Roman lake again.',
        img='Belisarius', y=540, at='ravenna'),
    life('The plague',
         'In 541 the first known outbreak of bubonic plague reached Constantinople and killed perhaps a quarter of its '
         'people. Justinian caught it himself, and survived. It came back again and again for two centuries.',
         img='Plague of Justinian', y=542, at='constantinople'),
    legacy("Justinian dreamed of rebuilding the Roman Empire. His conquests did not last, but his law code shaped the "
           'laws of Europe, and Hagia Sophia still stands in Istanbul.',
           'Gathered Roman law into a code Europe still builds on',
           'Built Hagia Sophia',
           'Won back much of the western Roman Empire',
           img='Basilica of San Vitale', cap='Justinian and his court in mosaic at Ravenna'),
)

story('muhammad', 'The Prophet of Islam, who united Arabia under the faith in one God.',
    life('An orphan of Mecca',
         'Muhammad was born in Mecca around 570. His father died before he was born and his mother when he was six; he '
         'was raised by his grandfather, then by his uncle Abu Talib, a merchant. As a young man he led trading caravans '
         'to Syria and was known as al-Amin, "the trustworthy".',
         img='Mecca', y=570, at='mecca'),
    life('Khadija',
         'At 25 he married Khadija, a widow and successful merchant about 15 years older than him, who had hired him to '
         'lead her caravans. They were married for 25 years, and she was the first person to believe in his message.',
         img='Khadija bint Khuwaylid', y=595, at='mecca'),
    tale('The cave of Hira',
         'He often went to pray alone in a cave on a mountain outside Mecca. Muslims believe that one night in 610 the '
         'angel Gabriel appeared to him there and commanded "Recite!", giving him the first words of the Quran. He came '
         'home trembling, and Khadija comforted him.',
         img='Jabal al-Nour', y=610, at='mecca'),
    life('Preaching one God',
         'He began to preach that there is only one God, and that people must care for the poor and for orphans. The '
         'leaders of Mecca, who grew rich from pilgrims to the idols around the Kaaba, mocked and persecuted his '
         'followers. Some fled to Christian Ethiopia for safety.',
         img='Kaaba', y=613, at='mecca'),
    win('The Hijra',
        'In 622, warned of a plot to kill him, he escaped to the town of Yathrib, later called Medina, "the city". '
        'Tradition says he hid in a cave on the way, while a spider spun its web across the entrance and fooled his '
        'pursuers. The Islamic calendar counts its years from this journey.',
        img='Jabal Thawr', cap='Mount Thawr, where he hid in a cave', y=622, at='medina'),
    win('Return to Mecca',
        'In Medina he led a growing community and fought several battles with Mecca. In 630 he returned at the head of '
        '10,000 followers, and Mecca surrendered almost without bloodshed. He forgave most of his old enemies and cleared '
        'the idols from the Kaaba.',
        img='Masjid al-Haram', y=630, at='mecca'),
    life('The farewell sermon',
         'In 632 he made a last pilgrimage to Mecca and told a vast crowd that all believers are equal: "An Arab has no '
         'superiority over a non-Arab." He died in Medina a few months later and was buried in his mosque there.',
         img='Al-Masjid an-Nabawi', y=632, at='medina'),
    legacy('Muhammad founded Islam, today the faith of nearly two billion people. Within a century of his death it '
           'reached from Spain to India, and the Quran made Arabic a language of prayer and learning across the world.',
           'The Prophet of Islam, followed by nearly two billion people',
           'Brought the Quran, as Muslims believe, revealed by God',
           'United Arabia in one community'),
)

story('ali', 'The cousin of the Prophet, fourth caliph of Islam and first imam of the Shia.',
    life('Raised in the Prophet\'s house',
         'Ali was the son of Abu Talib, the uncle who raised Muhammad, and tradition says he was born inside the Kaaba '
         'itself. When Abu Talib fell on hard times, Muhammad took young Ali into his own home, and Ali, still a boy, was '
         'one of the very first to accept Islam.',
         img='Kaaba', y=600, at='mecca'),
    tale("In the Prophet's bed",
         "On the night Muhammad fled Mecca in 622, assassins surrounded his house. Ali, about 22, lay down in the Prophet's "
         'bed under his green cloak, so the killers would think Muhammad was still inside. At dawn they burst in and found '
         'Ali; Muhammad was already far away.',
         y=622, at='mecca'),
    life('The lion of God',
         "Ali married the Prophet's daughter Fatima, and their sons Hasan and Husayn were Muhammad's beloved grandsons. "
         'He was famous as a warrior, with the forked sword Zulfiqar; at Khaybar, it was said, he tore the fortress gate '
         'off its hinges and used it as a shield.',
         img='Zulfiqar', y=628, at=(39.29, 25.7), where='Khaybar'),
    life('The fourth caliph',
         'When Muhammad died in 632, some believed he had named Ali to lead after him. But the community chose Abu Bakr, '
         'then Umar and Uthman. Ali became the fourth caliph only in 656. Those who believe he should have come first '
         'became the Shia, "the party of Ali".',
         img='Rashidun Caliphate', y=656, at='kufa'),
    life('A divided caliphate',
         "His five-year reign was torn by civil war, against Aisha, the Prophet's widow, at the Battle of the Camel, and "
         'against Muawiya, the governor of Syria. He ruled from Kufa in Iraq. In 661 a rebel struck him with a poisoned '
         'sword while he prayed in its mosque.',
         img='Great Mosque of Kufa', y=661, at='kufa'),
    work('The Peak of Eloquence',
         'His sermons, letters and sayings were collected as the Nahj al-Balagha, "The Peak of Eloquence". One of them, '
         'from a letter to a governor of Egypt: "People are of two kinds: either your brothers in faith or your equals in '
         'humanity."',
         img='Nahj al-Balagha'),
    legacy('Ali is honoured by all Muslims as a cousin of the Prophet, a brave warrior and a wise judge. For the Shia, more '
           'than one in ten Muslims, he is the first imam, and his shrine at Najaf is one of their holiest places.',
           'Cousin and son-in-law of Muhammad',
           'Fourth caliph of Islam',
           'First imam of Shia Islam',
           img='Imam Ali Shrine', at='najaf'),
)

story('xuanzang', 'The monk who walked from China to India and back to find the true teachings of the Buddha.',
    life('A boy monk',
         'Xuanzang became a Buddhist monk at 13, in Luoyang, and soon found that the Chinese translations of the Buddhist '
         'books were muddled and contradicted each other. He decided to go to India, the land of the Buddha, and bring '
         'back the originals.',
         img='Luoyang', y=615, at='luoyang'),
    tale('Slipping out of China',
         'The Tang emperor had banned travel abroad, but in 629 Xuanzang slipped out anyway, travelling by night. Crossing '
         'the Gobi Desert alone, he spilled his water bag and went five days without water, until his old horse led him '
         'to a spring.',
         img='Gobi Desert', y=629, at='dunhuang'),
    life('Across the roof of the world',
         'He crossed the icy Tian Shan mountains, where many of his companions froze to death, and passed through '
         'Samarkand and Bamiyan, with its giant stone Buddhas, then over the Khyber Pass into India.',
         img='Buddhas of Bamiyan', y=630, at='bamiyan'),
    win('Studying at Nalanda',
        'In India he spent years at Nalanda, the greatest university of the age, with thousands of monks, and visited the '
        'places where the Buddha had lived and taught. He debated so brilliantly that King Harsha held a great assembly '
        'in his honour.',
        img='Nalanda', y=637, at='nalanda'),
    win('Home with 657 books',
        "He came back to Chang'an in 645, sixteen years after leaving, with 657 Buddhist texts carried by 20 horses. The "
        'emperor forgave him and asked him to write about his travels. He spent the rest of his life translating, and the '
        'Big Wild Goose Pagoda was built to keep his books.',
        img='Giant Wild Goose Pagoda', y=645, at='changan'),
    tale('Journey to the West',
         "Nine centuries later his journey inspired Journey to the West, one of China's best-loved novels, in which a monk "
         'travels to India guarded by the Monkey King, a pig and a river spirit. It has been retold in countless films, '
         'cartoons and games.',
         img='Journey to the West', y=1592),
    legacy("Xuanzang's translations shaped Chinese Buddhism, and his account of his travels is still a key source on old "
           'Central Asia and India; archaeologists used it to find lost Buddhist sites, Nalanda among them.',
           'Travelled 16 years to India and back',
           'Brought home 657 Buddhist texts',
           'Inspired the novel Journey to the West'),
)

story('wu-zetian', 'The only woman ever to rule China as emperor in her own name.',
    life('A concubine at fourteen',
         'Wu Zhao entered the palace of Emperor Taizong at 14 as a junior concubine. When he died she was sent to a '
         'Buddhist nunnery, as was the custom. But his son, the new emperor Gaozong, had fallen for her, and brought her '
         'back to court.',
         img='Emperor Taizong of Tang', y=638, at='changan'),
    life('Empress',
         'She rose to become empress in 655, pushing aside the old empress. As Gaozong grew ill, she ran the government '
         'for him, sitting behind a screen at court and giving orders in his name.',
         img='Emperor Gaozong of Tang', y=655, at='changan'),
    win('Emperor in her own name',
        'After Gaozong died she ruled through two of her sons, then in 690 took the throne herself and founded her own '
        'Zhou dynasty. She was the only woman in Chinese history to rule as emperor in her own right.',
        img='Wu Zhou', y=690, at='luoyang'),
    win('Talent over birth',
        'She widened the imperial exams so that officials were picked for their ability rather than their family, and '
        'brought able men in from outside the old nobility. She cut taxes for farmers, and her armies pushed Chinese power '
        'deep into Central Asia.',
        img='Imperial examination', y=690),
    work('The giant Buddha',
         'A devout Buddhist, she paid for the huge Vairocana Buddha carved into the cliffs at Longmen, 17 metres tall. '
         'Some say its calm face was modelled on her own.',
         img='Longmen Grottoes', y=675, at='longmen'),
    tale('Copper boxes',
         'She set up copper boxes where anyone could drop letters denouncing officials, and used secret police to crush '
         'plots against her. Officials were so afraid that some said goodbye to their families every morning before '
         'going to court.',
         y=686, at='luoyang'),
    life('The blank tablet',
         'Forced to step down at 80 in a palace coup in 705, she died later that year. She was buried with Gaozong, and '
         'by her tomb stands a huge stone tablet with no words on it, perhaps because she wanted later ages to judge her.',
         img='Qianling Mausoleum', y=705, at='xian'),
    legacy('Confucian historians condemned Wu Zetian for centuries because they believed a woman should never rule. '
           'Today she is seen as a strong and able ruler who held China together at the height of the Tang dynasty.',
           'The only woman to rule China as emperor',
           'Opened government to talent through exams',
           'Ruled China for half a century'),
)

story('li-bai', "China's best-loved poet, of wine, mountains and the moon.",
    life('The wandering swordsman',
         'Li Bai grew up in Sichuan, in western China; he may have been born in Central Asia. As a young man he practised '
         'swordsmanship, lived with hermits in the mountains and, he boasted, fought several duels. At 24 he set off down '
         'the Yangtze to see the world.',
         img='Yangtze', y=725, at='chengdu'),
    life("At the emperor's court",
         "His poems made him so famous that in 742 Emperor Xuanzong called him to the capital, Chang'an. Legend says the "
         'emperor stirred his soup for him, and that Li Bai, drunk, made a powerful palace official pull off his boots. '
         'He did not last long at court.',
         img='Emperor Xuanzong of Tang', y=742, at='changan'),
    work('Quiet Night Thought',
         'His most famous poem is learned by every Chinese child: "Before my bed the moonlight glows, like frost upon the '
         'ground. I lift my head to see the moon, then bow it, thinking of home." About 1,000 of his poems survive, on '
         'wine, friendship, mountains and the moon.',
         img='Quiet Night Thought', y=726),
    tale('A party of three',
         'In another poem he drinks alone among the flowers, so he invites the moon and his own shadow to join him, '
         'making a party of three. A friend wrote that he could dash off a hundred poems for one jug of wine.',
         img='Drinking Alone by Moonlight'),
    life('Rebellion and exile',
         'In 755 a great rebellion tore China apart. Li Bai joined a prince who turned out to be a rebel, and was '
         'sentenced to exile in the far south-west. He was pardoned on the way and spent his last years wandering the '
         'Yangtze.',
         img='An Lushan rebellion', y=757),
    tale('Embracing the moon',
         'He died in 762. A famous legend says he drowned one night when, drunk in a boat on the Yangtze, he leaned out '
         'to hug the reflection of the moon in the water.',
         y=762),
    legacy('Li Bai and his friend Du Fu are the giants of Chinese poetry. Translated by Ezra Pound and set to music by '
           'Gustav Mahler, his poems shaped how the whole world imagines Chinese verse.',
           "China's best-loved poet",
           'Wrote "Quiet Night Thought", known by every Chinese child',
           "His poems are sung in Mahler's Song of the Earth"),
)

story('charlemagne', 'The king of the Franks who united western Europe and was crowned emperor in 800.',
    life('King of the Franks',
         'Charles was the son of Pepin the Short, king of the Franks. He became king in 768 and sole ruler in 771, at 24. '
         'Tall and strong, he loved hunting and swimming, and gathered his courtiers for swims in the hot springs at '
         'Aachen.',
         img='Pepin the Short', cap='Pepin the Short, his father', y=768, at='aachen'),
    win('Fifty years of war',
        'He fought more than 50 campaigns: against the Lombards in Italy, the Saxons in Germany, whom he forced to become '
        'Christian, the Avars in Hungary and the Moors in Spain. By 800 he ruled most of western Europe.',
        img='Carolingian Empire', y=800),
    tale('Roland at Roncevaux',
         'Coming back from Spain in 778, his rearguard was ambushed by Basques in a pass in the Pyrenees, and his commander '
         'Roland was killed. Three centuries later the Song of Roland turned it into an epic, with Roland blowing his horn '
         'to call for help until his temples burst.',
         img='The Song of Roland', y=778, at=(-1.32, 43.01), where='Roncevaux Pass'),
    win('Crowned emperor',
        "On Christmas Day 800, as Charles knelt in prayer in St Peter's in Rome, Pope Leo III placed a crown on his head "
        'and the crowd hailed him emperor of the Romans, the first in the West for over 300 years. Charles later said it '
        'had been a surprise.',
        img='Pope Leo III', y=800, at='rome'),
    win('A revival of learning',
        'Charles could read, but struggled to write, and kept tablets under his pillow to practise his letters. He brought '
        'scholars like Alcuin of York to court, founded schools and had old books copied. His scribes created a clear new '
        'handwriting, the ancestor of the small letters you are reading now.',
        img='Carolingian minuscule', y=789, at='aachen'),
    tale('An elephant from Baghdad',
         'The caliph Harun al-Rashid sent him gifts from Baghdad, among them a white elephant called Abul-Abbas. It walked '
         'across the Alps and lived at Aachen for years, and went along on at least one campaign against the Danes.',
         img='Abul-Abbas', y=802, at='aachen'),
    legacy('Charlemagne united most of western Europe for the first time since Rome and is called the "father of Europe". '
           'France and Germany both claim him, and the empire that grew from his crown lasted a thousand years.',
           'United most of western Europe',
           'Crowned emperor by the pope in the year 800',
           'Started a revival of learning and handwriting',
           img='Palatine Chapel, Aachen', cap='His chapel at Aachen, where he is buried'),
)

story('harun-al-rashid', 'The caliph of Baghdad at its height, and hero of the Thousand and One Nights.',
    life('A prince of Baghdad',
         'Harun was born in 763, a son of the Abbasid caliph al-Mahdi, just after Baghdad was founded. As a teenager he led '
         'an army against the Byzantines all the way to the shore opposite Constantinople, and was given the title '
         'al-Rashid, "the rightly guided".',
         img='Abbasid Caliphate', y=782, at='baghdad'),
    life('Caliph of Baghdad',
         'He became caliph in 786. Much of the work of ruling was done by his clever ministers, the Barmakid family, until '
         'in 803 he suddenly had their leader executed and the family\'s wealth seized. No one knows quite why.',
         img='Barmakids', y=786, at='baghdad'),
    win('Baghdad at its height',
        'Under Harun, Baghdad grew into one of the largest cities on Earth, with perhaps a million people, palaces, '
        'markets and the trade of three continents. He paid poets, musicians, doctors and scholars, and gathered a '
        'library that grew into the House of Wisdom.',
        img='Round city of Baghdad', y=790, at='baghdad'),
    tale('The caliph in disguise',
         'Stories say he liked to slip out at night dressed as a merchant, with his vizier Jafar and his executioner '
         'Masrur, to see how ordinary people lived. These tales made him the hero of many stories of the Thousand and One '
         'Nights.',
         img='One Thousand and One Nights', y=800, at='baghdad'),
    tale('A clock for Charlemagne',
         'He exchanged embassies with Charlemagne, and sent him a white elephant and a brass water clock. Every hour, '
         'little balls dropped onto a cymbal to chime, and tiny horsemen rode out of doors: a machine no one in Europe '
         'could build.',
         img='Water clock', y=807),
    life('Pilgrim and warrior',
         'He made the pilgrimage to Mecca several times, once on foot, and led raids against the Byzantines, forcing their '
         'emperor to pay tribute. He died in 809 at Tus, in Persia, on his way to put down a revolt.',
         y=809, at='mashhad', where='Tus'),
    legacy('Harun ruled the Abbasid Caliphate at its height, when Baghdad was the cultural capital of the world. Thanks '
           'to the Thousand and One Nights he became the most famous caliph of all, a symbol of the golden age of Islam.',
           'Ruled the Islamic world at its height',
           'Made Baghdad one of the greatest cities on Earth',
           'Hero of the Thousand and One Nights'),
)

story('al-khwarizmi', 'The scholar of Baghdad who gave us algebra, and whose name became "algorithm".',
    life('A scholar from Khwarazm',
         'Muhammad ibn Musa al-Khwarizmi was born around 780, probably in Khwarazm, a land of oasis cities south of the '
         'Aral Sea, in what is now Uzbekistan. Like many scholars, he was drawn to Baghdad, capital of the Abbasid '
         'caliphs.',
         img='Khwarazm', y=780, at='khiva', where='Khwarazm'),
    win('The House of Wisdom',
        'In Baghdad, scholars of many faiths translated Greek, Persian and Indian books into Arabic and built on them. '
        'The caliph al-Mamun made al-Khwarizmi a scholar of the House of Wisdom, where he worked on mathematics, '
        'astronomy and geography, and drew up a map of the world.',
        img='House of Wisdom', y=820, at='baghdad'),
    made('Algebra',
         'Around 820 he wrote a book on solving equations step by step, The Book of Completion and Balancing. Its Arabic '
         'title, al-jabr, gave us the word "algebra".',
         'Algebra became a field of its own, used for trade and inheritance then, and today for everything from '
         'engineering to economics.',
         img='The Compendious Book on Calculation by Completion and Balancing', y=820, at='baghdad'),
    made('Indian numbers',
         'Another book explained the Indian way of writing numbers, with nine digits and a zero, where the place of a '
         'digit shows its value.',
         'Translated into Latin, it spread these numbers across Europe, where they are called Arabic numerals. They made '
         'sums easy for everyone.',
         img='Arabic numerals', y=825),
    tale('His name in your phone',
         'The Latin translation of his number book began "Dixit Algorizmi": "So said al-Khwarizmi". His name turned into '
         '"algorism", calculating with these numbers, and later "algorithm", the word for the step-by-step rules that run '
         'every computer and phone.',
         img='Algorithm', y=1145),
    legacy('Al-Khwarizmi gave the world algebra and helped bring it the numbers we use. Two of the most important words in '
           'mathematics and computing, algebra and algorithm, come from his book and his name.',
           'Founded algebra as a subject',
           'Spread the Indian number system with zero',
           'His name gave us the word "algorithm"'),
)

from _lib import story, life, win, made, work, song, tale, legacy

story('michael-faraday', "The bookbinder's boy who discovered how to make electricity from magnetism.",
    life("A blacksmith's son",
         'Michael Faraday was born in 1791 in south London, the son of a poor blacksmith. He had little schooling. At 14 he '
         'was apprenticed to a bookbinder, and read the books he bound, above all the ones about electricity and chemistry.',
         y=1805, at='london'),
    tale('The notes that got him a job',
         'In 1812 a customer gave him tickets to hear the famous chemist Humphry Davy lecture. Faraday wrote up careful '
         'notes, bound them into a book and sent them to Davy, asking for work. When Davy\'s assistant was sacked for '
         'fighting, Faraday got the job.',
         img='Humphry Davy', cap='Humphry Davy', y=1812, at='london'),
    made('The electric motor',
         'In 1821 he made a wire carrying an electric current spin round and round a magnet. It was the first electric '
         'motor.',
         'Every electric motor, from fans and washing machines to trains and electric cars, works on the same idea.',
         img='Electric motor', y=1821, at='london'),
    made('Electricity from magnetism',
         'In 1831 he found that moving a magnet in and out of a coil of wire makes an electric current flow. He built the '
         'first generator, a copper disc spinning between the poles of a magnet.',
         'Almost all the world\'s electricity is still made this way, in generators turned by steam, water or wind.',
         img='Electromagnetic induction', y=1831, at='london'),
    win('The Christmas Lectures',
        'In 1825 he started the Christmas Lectures at the Royal Institution, science shows for young people. His talk on '
        'the chemistry of a candle is still in print, and the lectures still run on television every year.',
        img='Royal Institution Christmas Lectures', y=1860, at='london'),
    tale('What use is it?',
         'A famous story says a politician asked him what use electricity was. "Why, sir," Faraday replied, "there is every '
         'probability that you will soon be able to tax it." The story is probably made up, but it was right.',
         y=1850, at='london'),
    life('Plain Mr Faraday',
         'He turned down a knighthood, and twice refused to lead the Royal Society, wanting to stay "plain Mr Faraday to the '
         'end". He also refused to help the government make poison gas for the Crimean War. He died in 1867.',
         img='Royal Institution', y=1854, at='london'),
    legacy('Faraday made the age of electricity possible: motors, generators and transformers all come from his work. '
           'Einstein kept a picture of him on his study wall.',
           'Built the first electric motor',
           'Discovered how to make electricity from magnetism',
           'Started the Christmas Lectures for young people'),
)

story('victor-hugo', 'The giant of French writing, author of Les Misérables, who spent 19 years in exile.',
    life("A general's son",
         'Victor Hugo was born in 1802 in Besançon, the son of one of Napoleon\'s generals, and grew up between Paris, Italy '
         'and Spain. At 14 he wrote in a notebook: "I want to be Chateaubriand or nothing", naming the most famous writer of '
         'the day.',
         y=1802, at=(6.02, 47.24), where='Besançon'),
    win('The battle of Hernani',
        'In 1830 his play Hernani broke all the old rules of French drama. On opening night young Romantics fought the '
        'traditionalists in the theatre, and the battle went on night after night. Hugo became the leader of the Romantic '
        'movement.',
        img='Hernani (drama)', y=1830, at='paris'),
    tale('Locked out of his clothes',
         'His wife later wrote that, to make himself finish his next novel on time, he locked away his clothes so he could '
         'not go out, and wrote wrapped in a big grey woollen shawl.',
         y=1830, at='paris'),
    work('The Hunchback of Notre-Dame',
         'That novel, of 1831, tells of Quasimodo, the deaf bell ringer of Notre-Dame, and his love for Esmeralda. Hugo '
         'wrote it partly to save the neglected cathedral, and it worked: Paris began to restore it.',
         img='The Hunchback of Notre-Dame', y=1831, at='paris'),
    life('Grief',
         'In 1843 his beloved daughter Léopoldine drowned in the Seine with her husband, six months after her wedding. Hugo '
         'learned of it from a newspaper. For years he wrote poems to her.',
         y=1843, at=(0.68, 49.53), where='Villequier'),
    life('Exile',
         'When Louis-Napoleon seized power in 1851, Hugo called him "Napoleon the Little" and had to flee. He spent 19 years '
         'in exile, most of them on the island of Guernsey, writing at a standing desk that looked out to sea.',
         img='Hauteville House', y=1856, at='guernsey'),
    work('Les Misérables',
         'In 1862 he published Les Misérables, the story of Jean Valjean, a convict who stole a loaf of bread, hunted for '
         'years by the policeman Javert. It is a huge novel about poverty, justice and mercy, and today a famous musical.',
         img='Les Misérables', y=1862, at='guernsey'),
    tale('The shortest letter',
         'A famous story says that, wanting to know how Les Misérables was selling, he sent his publisher a note with just '
         '"?". The publisher wrote back: "!"',
         y=1862, at='guernsey'),
    life("A hero's farewell",
         'He came home when the emperor fell in 1870. When he died in 1885, his coffin lay in state under the Arc de '
         'Triomphe, and some two million people followed it to the Panthéon.',
         img='Arc de Triomphe', y=1885, at='paris'),
    legacy("Hugo is France's best loved writer, and fought all his life against the death penalty, poverty and tyranny.",
           'Wrote Les Misérables',
           'Wrote The Hunchback of Notre-Dame',
           'Fought the death penalty and tyranny'),
)

story('charles-darwin', 'The naturalist whose voyage on the Beagle led him to the theory of evolution.',
    life("A doctor's son",
         'Charles Darwin was born in 1809 in Shrewsbury, England, the son of a rich doctor. He was sent to study medicine '
         'in Edinburgh, but could not bear watching operations without anaesthetic. So his father sent him to Cambridge to '
         'become a clergyman.',
         img='Shrewsbury', y=1809, at='shrewsbury'),
    tale('A beetle in the mouth',
         'At Cambridge he was mad about collecting beetles. Once, holding a rare beetle in each hand, he saw a third, and '
         'popped one into his mouth to free a hand. It squirted burning acid on his tongue, and he lost two of the three.',
         y=1828, at='cambridge'),
    life('The voyage of the Beagle',
         'In 1831, aged 22, he joined the survey ship HMS Beagle as its naturalist, for a voyage around the world that '
         'lasted five years. He was seasick much of the time, but collected thousands of plants, animals and fossils.',
         img='HMS Beagle', y=1831, at='plymouth'),
    tale('The Galápagos',
         'In 1835 the Beagle reached the Galápagos Islands. Darwin rode the giant tortoises, and heard that you could tell '
         'which island a tortoise came from by its shell. Back home, the finches he brought turned out to be different '
         'species on different islands.',
         img='Galápagos tortoise', y=1835, at='galapagos'),
    made('Evolution by natural selection',
         'He worked out that living things vary, and those best suited to their surroundings survive and have more young. '
         'Over vast stretches of time, these small changes add up to new species.',
         'It explained the variety of life without miracles, and became the foundation of all modern biology.',
         img="Darwin's finches", y=1838, at='london'),
    tale('Marry or not marry?',
         'Before proposing to his cousin Emma Wedgwood, he wrote a list. "Marry": children, a constant companion, "better '
         'than a dog anyhow". "Not marry": freedom, and more money for books. Marry won, and they had ten children.',
         y=1838, at='london'),
    life('Twenty years of waiting',
         'At Down House in Kent he worked quietly for 20 years on his theory, afraid of the uproar it would cause. In 1858 a '
         'letter came from Alfred Russel Wallace, in the islands of Southeast Asia, with the very same idea.',
         img='Down House', y=1858, at='downe'),
    work('On the Origin of Species',
         'He rushed out his book in 1859, and every copy was snapped up by booksellers on the first day. At a famous debate '
         'in Oxford, a bishop asked Darwin\'s friend Thomas Huxley whether it was on his grandfather\'s or his grandmother\'s '
         'side that he was descended from an ape.',
         img='On the Origin of Species', y=1859, at='downe'),
    life('Earthworms',
         'His last book was about earthworms, and sold very well. He died in 1882 and was buried in Westminster Abbey, near '
         'Isaac Newton.',
         img='Westminster Abbey', y=1882, at='london'),
    legacy("Darwin's theory of evolution is the foundation of modern biology: it explains how all living things, "
           'humans included, are related, and how they came to be.',
           'Explained evolution by natural selection',
           'Wrote On the Origin of Species',
           'Showed that all living things share common ancestors'),
)

story('abraham-lincoln', 'Born in a log cabin, he led the United States through its Civil War and ended slavery.',
    life('A log cabin',
         'Abraham Lincoln was born in 1809 in a one-room log cabin in Kentucky, and grew up on frontier farms in Indiana and '
         'Illinois. In all he had about one year of school, but he read every book he could borrow.',
         img='Abraham Lincoln Birthplace National Historical Park', y=1809, at='hodgenville'),
    tale('The wrestler',
         'He grew to 1.93 m, tall and strong from splitting logs for fences. In New Salem he was the local wrestling '
         'champion; the story goes that he lost only one of about 300 matches.',
         y=1831, at='new_salem'),
    life('Honest Abe',
         'He worked as a shopkeeper, postmaster and surveyor, and taught himself law. People called him "Honest Abe": it was '
         'said he once walked miles to return a few cents of change. In 1837 he became a lawyer in Springfield.',
         y=1837, at='springfield_il'),
    win('A house divided',
        'In 1858 he said: "A house divided against itself cannot stand. I believe this government cannot endure, '
        'permanently half slave and half free." His debates on slavery with Stephen Douglas made him famous.',
        img='Lincoln–Douglas debates', y=1858, at='springfield_il'),
    tale('The beard',
         'In 1860 an 11-year-old girl, Grace Bedell, wrote to him that he would look better with whiskers, as his face was '
         'so thin. He grew a beard, and when his train passed through her town, he asked to meet her.',
         img='Grace Bedell', y=1860, at=(-79.58, 42.32), where='Westfield, New York'),
    life('A country at war',
         'He was elected president in 1860. Before he took office, seven Southern states left the Union to protect slavery. '
         'In April 1861 the Civil War began, the deadliest war in American history.',
         img='American Civil War', y=1861, at='washington'),
    win('The Emancipation Proclamation',
        'On 1 January 1863 he declared that the enslaved people in the rebel states were "forever free". Black men could '
        'now join the Union army, and nearly 200,000 did.',
        img='Emancipation Proclamation', y=1863, at='washington'),
    win('The Gettysburg Address',
        'In November 1863, at the battlefield of Gettysburg, he gave a speech of just 272 words, promising that '
        '"government of the people, by the people, for the people, shall not perish from the earth."',
        img='Gettysburg Address', y=1863, at='gettysburg'),
    win('Ending slavery',
        'In January 1865 he pushed the 13th Amendment to the Constitution through Congress, abolishing slavery in the '
        'whole country. On 9 April the main Southern army surrendered.',
        img='Thirteenth Amendment to the United States Constitution', y=1865, at='washington'),
    life("Ford's Theatre",
         "Five days later, on 14 April 1865, he was shot at Ford's Theatre in Washington by the actor John Wilkes "
         'Booth. He died the next morning.',
         img="Ford's Theatre", y=1865, at='washington'),
    legacy('Lincoln held the United States together through its Civil War and ended slavery. Many historians rank him the '
           'greatest American president.',
           'Led the Union through the Civil War',
           'Freed the enslaved with the Emancipation Proclamation',
           'Gave the Gettysburg Address'),
)

story('charles-dickens', 'The boy who worked in a factory at 12 and grew up to write Oliver Twist and A Christmas Carol.',
    life('The blacking factory',
         'Charles Dickens was born in Portsmouth in 1812. When he was 12, his father was jailed for debt, and Charles was '
         'sent to work ten hours a day in a factory, pasting labels on pots of boot polish. He kept the shame a secret all '
         'his life.',
         img='Marshalsea', cap='The Marshalsea, the prison where his father was held', y=1824, at='london'),
    life('Boz',
         'He became a reporter, taking down speeches in Parliament in shorthand, and wrote funny sketches of London life '
         'under the name "Boz". In 1836 his comic Pickwick Papers made him the most famous writer in England at 24.',
         img='The Pickwick Papers', y=1836, at='london'),
    work('Oliver Twist',
         'In Oliver Twist, the orphan in the workhouse dares to ask: "Please, sir, I want some more." His novels showed '
         'readers the cruelty of workhouses, child labour and debtors\' prisons, and helped bring reform.',
         img='Oliver Twist', y=1838, at='london'),
    tale('Is Little Nell dead?',
         'His novels came out in parts, a chapter or two each month. A famous story says that in 1841 crowds on the docks '
         'of New York shouted to sailors arriving from England: "Is Little Nell dead?"',
         img='The Old Curiosity Shop', y=1841, at='new_york'),
    work('A Christmas Carol',
         'In 1843 he wrote A Christmas Carol in six weeks. The miser Scrooge, who says "Bah! Humbug!" to Christmas, is '
         'visited by three ghosts and learns to be kind. It helped shape how Christmas is celebrated today.',
         img='A Christmas Carol', y=1843, at='london'),
    win('The great performer',
        'He gave readings of his books to huge crowds in Britain and America, acting out every character with different '
        'voices. Audiences laughed, wept and fainted. The tours made him rich, but wore him out.',
        y=1867, at='boston'),
    tale('The train crash',
         'In 1865 his train fell off a bridge at Staplehurst. Dickens helped the injured and the dying, then climbed back '
         'into his dangling carriage to rescue the manuscript of his new novel. He died five years later to the day.',
         y=1865, at=(0.55, 51.16), where='Staplehurst'),
    life('An unsolved mystery',
         'He died at his country home in 1870, aged 58, halfway through The Mystery of Edwin Drood, so no one will ever know '
         'who did it. He was buried in Westminster Abbey.',
         y=1870, at='gads_hill'),
    legacy('Dickens created some of the best loved characters in literature, from Scrooge to Oliver Twist, and his '
           'stories pushed Britain to care for its poor.',
           'Wrote Oliver Twist, A Christmas Carol and Great Expectations',
           'Exposed the suffering of poor children',
           'Helped shape the way we celebrate Christmas'),
)

story('richard-wagner', 'The composer of the Ring, who built his own opera house, and whose music still divides people.',
    life('A theatre child',
         'Richard Wagner was born in Leipzig in 1813, and grew up around the theatre, as his stepfather was an actor. As a '
         'teenager he heard Beethoven and decided to become a composer, mostly teaching himself.',
         img='Leipzig', y=1813, at='leipzig'),
    tale('Escape by sea',
         'In 1839, deep in debt, he slipped across the border from Riga at night and fled by ship to London. A terrible '
         'storm at sea gave him the idea for his opera The Flying Dutchman, about a ghost ship.',
         img='The Flying Dutchman (opera)', y=1839, at='riga'),
    life('Revolution and exile',
         'As conductor of the opera in Dresden he joined the revolution of 1849. When it failed, there was a warrant for his '
         'arrest, and he fled to Switzerland, where he lived in exile for more than ten years.',
         img='May Uprising in Dresden', y=1849, at='dresden'),
    song('Here comes the bride',
         'In his opera Lohengrin, first staged in 1850, a chorus leads the bride and groom to their room. Today the Bridal '
         'Chorus is played at weddings all over the world.',
         page='Bridal Chorus', y=1850, at='weimar'),
    win('A king for a fan',
        'In 1864, broke and on the run from people he owed money, he got a message: the new king of Bavaria, 18-year-old '
        'Ludwig II, adored his music. The king paid his debts and supported him for the rest of his life.',
        img='Ludwig II of Bavaria', y=1864, at='munich'),
    song('Ride of the Valkyries',
         'His greatest work, The Ring of the Nibelung, is four operas, about 15 hours of music, about gods, dwarfs, a magic '
         'ring and the end of the world. He worked on it for 26 years. In this famous music, warrior maidens ride through '
         'the sky.',
         page='Ride of the Valkyries', y=1870, at='munich'),
    work('Bayreuth',
         'He built his own opera house at Bayreuth, with the orchestra hidden in a covered pit and the hall dark during the '
         'show, both new ideas then. It opened in 1876 with the first full Ring, and the festival still runs every summer.',
         img='Bayreuth Festspielhaus', y=1876, at='bayreuth'),
    life('The dark side',
         'Wagner was vain and selfish, borrowed money he never repaid, and wrote a hateful essay attacking Jews. Long after '
         'he died in Venice in 1883, Hitler worshipped his music, and it is still rarely played in Israel.',
         y=1883, at='venice'),
    legacy('Wagner changed opera into "music drama", joining music, poetry and stage, and his rich harmonies shaped the '
           'music that came after him, all the way to film scores.',
           'Wrote The Ring of the Nibelung',
           'Built the Bayreuth Festival Theatre',
           'His music still shapes film scores'),
)

story('otto-von-bismarck', 'The Iron Chancellor, who united Germany with "blood and iron".',
    life('The wild Junker',
         'Otto von Bismarck was born in 1815 on his family\'s estate at Schönhausen, in Prussia. At university in Göttingen '
         'he drank, ran up debts and fought duel after duel, and was known as the mad Junker, a wild young country noble.',
         y=1815, at='schonhausen'),
    win('Blood and iron',
        'In 1862 King Wilhelm I made him head of the Prussian government. In his first speech he said the great questions of '
        'the day would be settled "not by speeches and majority votes, but by iron and blood."',
        y=1862, at='berlin'),
    win('Three short wars',
        'He fought three short wars: against Denmark in 1864, Austria in 1866 and France in 1870. The victory over Austria '
        'at Königgrätz left Prussia the leader of the German states.',
        img='Battle of Königgrätz', y=1866, at='koniggratz'),
    tale('The Ems telegram',
         'In 1870 the king sent him a telegram about a polite meeting with the French ambassador. Bismarck cut it so that it '
         'sounded like an insult, and gave it to the newspapers. France declared war, just as he had hoped.',
         img='Ems Dispatch', y=1870, at=(7.72, 50.33), where='Bad Ems'),
    win('The German Empire',
        'After the French were crushed, the German states united. On 18 January 1871, in the Hall of Mirrors at Versailles, '
        'Wilhelm was proclaimed German Emperor, and Bismarck became the first chancellor.',
        img='Proclamation of the German Empire', y=1871, at='versailles'),
    win('The honest broker',
        'Now he wanted peace. He wove a web of alliances to keep France isolated, and in 1878 hosted the Congress of Berlin, '
        'where the great powers settled their quarrels in the Balkans.',
        img='Congress of Berlin', y=1878, at='berlin'),
    win('The first welfare state',
        'To win workers away from the socialists, in the 1880s he created the world\'s first national health insurance, '
        'accident insurance and old age pensions. Countries everywhere later copied them.',
        y=1883, at='berlin'),
    life('Dropping the pilot',
         'In 1890 the young new emperor, Wilhelm II, forced him to resign; a British cartoon showed it as the pilot leaving '
         'the ship. He is said to have predicted that a great war would come out of "some damned foolish thing in the '
         'Balkans". He died in 1898.',
         img='Dropping the Pilot', y=1890, at='friedrichsruh'),
    legacy('Bismarck united Germany and made it the strongest power in Europe, and his social insurance laws became the '
           'model for the welfare state.',
           'United Germany in 1871',
           'First chancellor of the German Empire',
           'Created the first national health insurance and pensions'),
)

story('karl-marx', 'The thinker whose ideas of class struggle and communism shook the 20th century.',
    life("A lawyer's son",
         'Karl Marx was born in 1818 in Trier, in Germany. His father came from a family of rabbis, but became a Lutheran to '
         'keep his job as a lawyer. At university Karl was jailed for a night for drunkenness and fought a duel, then '
         'turned to philosophy.',
         img='Karl Marx House', y=1818, at='trier'),
    life('Engels',
         'The newspaper he edited in Cologne was shut down by the Prussian government in 1843. In Paris in 1844 he met '
         'Friedrich Engels, the son of a factory owner. They became partners in work and lifelong friends.',
         img='Friedrich Engels', cap='Friedrich Engels, his lifelong friend', y=1844, at='paris'),
    work('The Communist Manifesto',
         'In 1848 they wrote The Communist Manifesto: "The history of all hitherto existing society is the history of class '
         'struggles." It ends: "Workers of the world, unite!" It came out just as revolutions swept across Europe.',
         img='The Communist Manifesto', y=1848, at='brussels'),
    life('Poor in London',
         'Thrown out of one country after another, he settled in London in 1849, in two small rooms in Soho. Three of his '
         'children died young. Engels sent him money from his family\'s cotton mill in Manchester.',
         y=1850, at='london'),
    tale('The Reading Room',
         'Day after day he sat in the Reading Room of the British Museum, filling notebooks about factories and money. He '
         'suffered from painful boils, and joked that the rich would remember them until their dying day.',
         img='British Museum Reading Room', y=1860, at='london'),
    work('Capital',
         'In 1867 he published the first volume of Capital. It argued that factory owners grow rich from the unpaid work of '
         'their workers, and that capitalism would one day be overthrown by them. Engels finished it after his death.',
         img='Das Kapital', y=1867, at='london'),
    life('A small funeral',
         'Marx died in London in 1883. Only about a dozen people came to his funeral at Highgate Cemetery, where Engels '
         'said: "His name will endure through the ages."',
         img='Tomb of Karl Marx', y=1883, at='london'),
    legacy('Marx changed how people think about history, work and money. In the 20th century, communist states that '
           'claimed his ideas ruled a third of humanity, many of them as brutal dictatorships.',
           'Wrote The Communist Manifesto and Capital',
           'Founded the theory of communism',
           'His ideas shaped the 20th century'),
)

story('frederick-douglass', 'He escaped slavery and became its most powerful enemy, with his voice and his pen.',
    life('Born enslaved',
         'Frederick Douglass was born enslaved in Maryland, around 1818. He never knew his birthday, saw his mother only a '
         'few times, at night, and never knew for sure who his father was.',
         y=1818, at=(-76.1, 38.77), where='Talbot County, Maryland'),
    tale('Learning to read',
         'At about eight he was sent to Baltimore, where his new mistress began teaching him the alphabet, until her husband '
         'stopped her: reading would make him "unfit to be a slave". Douglass saw it as the road to freedom, and paid white '
         'boys in the street with bread to teach him.',
         y=1826, at='baltimore'),
    tale('The fight',
         'At 16 he was sent to a cruel "slave breaker" who whipped him every week. One day Douglass fought back, for two '
         'hours, and was never whipped again. "You have seen how a man was made a slave; you shall see how a slave was made '
         'a man."',
         y=1834, at=(-76.1, 38.77), where='Talbot County, Maryland'),
    win('Escape',
        'In 1838, dressed as a sailor and carrying papers borrowed from a free Black seaman, he took a train and a ferry '
        'north. A day later he stepped off in New York, free.',
        y=1838, at='new_york'),
    win('The speaker',
        'In 1841 he spoke at an anti-slavery meeting about his life, and became the greatest speaker of the movement to end '
        'slavery. In 1845 he wrote his life story, naming his old masters. To avoid capture he went to Britain, where '
        'friends bought his freedom.',
        img='Narrative of the Life of Frederick Douglass, an American Slave', y=1841, at=(-70.1, 41.28), where='Nantucket'),
    tale('What is your Fourth of July?',
         'In 1852 he asked a crowd: "What, to the American slave, is your 4th of July? A day that reveals to him, more than '
         'all other days in the year, the gross injustice and cruelty to which he is the constant victim."',
         y=1852, at='rochester_ny'),
    win('Talking to Lincoln',
        'In the Civil War he recruited Black soldiers, two of his own sons among them, and went to the White House to press '
        'Lincoln for equal pay. He also fought all his life for women\'s right to vote.',
        y=1863, at='washington'),
    tale('The most photographed American',
         'He sat for about 160 photographs, more than any other American of his century, to show the world a proud, '
         'dignified Black man instead of the cruel cartoons of the time.',
         y=1870, at='washington'),
    legacy('Douglass rose from slavery to become one of the greatest speakers and writers in American history, and '
           'fought all his life for equal rights.',
           'Escaped slavery and led the fight against it',
           'Wrote one of the great American autobiographies',
           'Fought for equal rights, including for women'),
)

story('queen-victoria', 'She reigned for 63 years, and gave her name to an age.',
    life('A lonely princess',
         'Victoria was born at Kensington Palace in 1819. Her father died when she was eight months old. Her mother raised '
         'her under strict rules: she was never left alone, and slept in her mother\'s room until she became queen.',
         img='Kensington Palace', y=1819, at='london'),
    win('Queen at 18',
        'At six in the morning on 20 June 1837 she was woken to be told that her uncle, the king, was dead, and that she '
        'was queen. That same day she had her bed moved out of her mother\'s room.',
        img='Coronation of Queen Victoria', y=1837, at='london'),
    life('Albert',
         'In 1840 she married her German cousin, Prince Albert. As queen, she was the one who proposed. They had nine '
         'children, who married into the royal families of Europe, so she became "the grandmother of Europe".',
         img='Albert, Prince Consort', cap='Prince Albert, her husband', y=1840, at='windsor'),
    tale('Blessed chloroform',
         'In 1853 she was given chloroform to ease the pain of giving birth to her eighth child. She called it "blessed '
         'chloroform", and pain relief in childbirth soon became accepted.',
         y=1853, at='london'),
    life('The widow of Windsor',
         'Albert died in 1861. Victoria wore black for the remaining 40 years of her life, and hid from the public for '
         'years. Every morning his clothes were laid out, as if he were still alive.',
         img='Windsor Castle', y=1861, at='windsor'),
    tale('Not amused?',
         '"We are not amused" is her most famous line, but there is no proof she ever said it, and her diaries show she '
         'laughed a lot. In old age an Indian servant, Abdul Karim, taught her Hindustani.',
         y=1887, at='osborne'),
    win('Empress of India',
        'In 1876 she was made Empress of India. By the end of her reign the British Empire covered about a fifth of the '
        "world's land: an empire on which the sun never set.",
        img='Delhi Durbar', y=1877, at='delhi'),
    win('The Diamond Jubilee',
        'In 1897 she celebrated 60 years on the throne. When she died in 1901 she had reigned for 63 years, longer than any '
        'British monarch before her.',
        img='Diamond Jubilee of Queen Victoria', y=1897, at='london'),
    legacy('Her reign gave its name to the Victorian age, of railways, factories, a vast empire and strict manners.',
           'Reigned for 63 years',
           'Ruled an empire on which the sun never set',
           'Her children married into royal families all over Europe'),
)

story('florence-nightingale', 'The Lady with the Lamp, who founded modern nursing and fought disease with statistics.',
    life('Named after a city',
         'Florence Nightingale was born in 1820 in Florence, Italy, to a rich English family on a long tour, and named after '
         'the city. Her family expected her to marry well, but at 16 she felt God was calling her to a purpose.',
         img='Florence', y=1820, at='florence'),
    tale('An owl in her pocket',
         'In Athens she rescued a baby owl from some boys, named it Athena, and carried it in her pocket. When it died, she '
         'had it stuffed; it is now in the Florence Nightingale Museum in London.',
         y=1850, at='athens'),
    life('A forbidden career',
         'Nursing was then seen as low work, for poor and often drunk women. Her family was horrified, but she trained in '
         'Germany, and in 1853 ran a small hospital for women in London.',
         y=1851, at=(6.74, 51.3), where='Kaiserswerth'),
    win('Scutari',
        'In 1854, in the Crimean War, she took 38 nurses to the British army hospital at Scutari, near Istanbul. Soldiers '
        'lay dying of disease in filth, without blankets or soap. She cleaned the wards, found supplies, and organised '
        'proper care.',
        img='Selimiye Barracks', y=1854, at='scutari'),
    tale('The Lady with the Lamp',
         'At night she walked the long wards alone with a lamp, checking on the sick. The soldiers loved her, and one wrote '
         'that they would kiss her shadow as it fell on their pillows.',
         y=1855, at='scutari'),
    made('Charts that saved lives',
         'She was a brilliant mathematician. With bold, colourful charts, she showed that far more soldiers died of diseases '
         'in dirty hospitals than of wounds in battle.',
         'Her charts persuaded the government to clean up army hospitals and cities, and she became the first woman member '
         'of the Royal Statistical Society.',
         img='File:Nightingale-mortality.jpg', y=1858, at='london'),
    win('The first nursing school',
        'In 1860 she founded a school for nurses at St Thomas\' Hospital in London, the start of nursing as a trained '
        'profession. Her Notes on Nursing became a bestseller.',
        img="St Thomas' Hospital", y=1860, at='london'),
    life('Working from bed',
         'Ill for much of her later life, she worked from her bed for decades, writing reports on hospitals and on clean '
         'water in India. In 1907 she became the first woman given the Order of Merit. She died in 1910, aged 90.',
         y=1907, at='london'),
    legacy('Nightingale founded modern nursing and showed how facts and figures can save lives. International Nurses Day '
           'is held on her birthday.',
           'Founder of modern nursing',
           'Cleaned up army hospitals and saved thousands of soldiers',
           'A pioneer of statistics and charts'),
)

story('louis-pasteur', 'The chemist who proved that germs cause disease, and made the first rabies vaccine.',
    life("A tanner's son",
         'Louis Pasteur was born in 1822 in Dole, in eastern France, the son of a tanner, and grew up in Arbois. He was an '
         'ordinary student who loved drawing portraits of his family and friends.',
         y=1822, at='dole'),
    made('Left and right molecules',
         'At 25 he found that some crystals come in two mirror image forms, like a left and a right hand.',
         'This founded a new branch of chemistry. It matters for medicines: a drug and its mirror twin can act on the body '
         'in very different ways.',
         y=1848, at='paris'),
    made('Germs',
         'Asked why wine and beer went sour, he showed that fermentation and rotting are caused by living microbes. With '
         'flasks with long curved necks, he proved that microbes do not appear out of nothing.',
         'His germ theory changed medicine: surgeons began to clean their hands and tools, and far fewer patients died.',
         img='Germ theory of disease', y=1862, at='paris'),
    made('Pasteurisation',
         'He found that heating wine to about 60 degrees for a short time kills the harmful microbes without spoiling the '
         'taste. The method was later used for milk.',
         'Pasteurised milk has saved countless lives, and his name is printed on milk cartons around the world.',
         img='Pasteurization', y=1865, at='arbois'),
    life('Three daughters',
         'Three of his five children died young, two of them of typhoid fever. The loss drove him to fight infectious '
         'disease. In 1868 a stroke paralysed his left side, but he kept working.',
         y=1866, at='paris'),
    made('Vaccines',
         'By accident, an old culture of chicken cholera, left out over the summer holidays, made chickens immune instead of '
         'sick. In 1881 he vaccinated sheep against anthrax in public: all the vaccinated sheep lived, the others died.',
         'He had found how to make vaccines from weakened germs, a method used for many diseases ever since.',
         img='Anthrax vaccine', y=1881, at=(2.75, 48.6), where='Pouilly-le-Fort'),
    win('Joseph Meister',
        'In 1885 a mother brought him nine-year-old Joseph Meister, savaged by a mad dog. Rabies always killed. Pasteur, who '
        'was not even a doctor, risked his untested vaccine. The boy lived, and later became caretaker of the Pasteur '
        'Institute.',
        y=1885, at='paris'),
    win('The Pasteur Institute',
        'Gifts poured in from around the world to found the Pasteur Institute in Paris in 1888. Its scientists have since '
        'made many vaccines, and in 1983 discovered the virus that causes AIDS.',
        img='Pasteur Institute', y=1888, at='paris'),
    legacy('Pasteur proved that germs cause disease and spoil food. His work led to vaccines, pasteurisation and clean '
           'hospitals, saving millions of lives.',
           'Proved that germs cause disease',
           'Invented pasteurisation',
           'Made the first vaccine against rabies'),
)

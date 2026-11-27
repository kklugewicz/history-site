from _lib import story, life, win, made, work, song, tale, legacy

story('voltaire', 'The witty voice of the Enlightenment, who fought for free speech and tolerance.',
    life('A pen that got him jailed',
         'François-Marie Arouet was born in Paris in 1694, the son of a lawyer, but he wanted to write. His mocking verses '
         'about the regent who ruled France got him locked in the Bastille for eleven months in 1717. There he wrote his '
         'first play and took the pen name Voltaire.',
         img='Bastille', y=1717, at='paris'),
    life('Exile in England',
         'In 1726 a nobleman had his servants beat Voltaire with sticks after a quarrel. When Voltaire demanded a duel, he '
         'was thrown back into the Bastille, then sent into exile. In England he admired its free press, its tolerance, '
         'Newton and Shakespeare, and wrote a book praising them that was burned in Paris.',
         img='Letters on the English', y=1727, at='london'),
    tale('Beating the lottery',
         'With a mathematician friend he spotted a flaw in the French state lottery: the prizes were worth more than all '
         'the tickets put together. They bought up the tickets and won a fortune, which kept him rich for the rest of his '
         'life.',
         y=1729, at='paris'),
    work('Candide',
         'In 1759 he published Candide, a short comic novel in which an innocent young man suffers war, earthquake, '
         'shipwreck and the Inquisition, while his tutor keeps insisting that all is for the best in the best of all '
         'possible worlds. It ends: "We must cultivate our garden."',
         img='Candide', y=1759),
    win('Crush the infamous thing',
        'From his estate at Ferney, near the Swiss border, he waged war on intolerance, signing his letters "Crush the '
        'infamous thing". He campaigned for years to clear the name of Jean Calas, a Protestant tortured and executed on a '
        'false charge, and won.',
        img='Jean Calas', y=1765, at=(6.11, 46.26), where='Ferney'),
    tale('Fifty cups of coffee',
         'He is said to have drunk up to 50 cups of coffee a day, and he wrote more than 20,000 letters. Back in Paris at '
         '83, he was crowned with laurels at a performance of one of his plays. He died a few weeks later, in 1778.',
         img='Coffee', y=1778, at='paris'),
    legacy('Voltaire was the leading voice of the Enlightenment, fighting for free speech, religious tolerance and reason. '
           'A later writer summed him up: "I disapprove of what you say, but I will defend to the death your right to say it."',
           'Champion of free speech and religious tolerance',
           'Wrote Candide',
           'The leading voice of the Enlightenment'),
)

story('benjamin-franklin', 'Printer, scientist, inventor and diplomat: the most many-sided of America\'s founders.',
    life('The runaway apprentice',
         "Benjamin Franklin was born in Boston in 1706, the 15th of 17 children of a candle maker. He left school at ten and "
         'was apprenticed to his brother, a printer. At 17 he ran away to Philadelphia with almost nothing, munching a '
         'bread roll as he walked up Market Street.',
         img='Boston', y=1723, at='philadelphia'),
    tale('Mrs Silence Dogood',
         "As a teenager he slipped letters under the door of his brother's print shop, signed by \"Mrs Silence Dogood\", a "
         'made-up country widow. His brother printed them in his newspaper, and readers loved them, until Ben owned up.',
         y=1722, at='boston'),
    win("Poor Richard's Almanack",
        'He built a printing business, and from 1732 published Poor Richard\'s Almanack, full of weather, jokes and sayings: '
        '"Early to bed and early to rise makes a man healthy, wealthy and wise." He founded America\'s first lending '
        'library, a fire company and a university.',
        img="Poor Richard's Almanack", y=1732, at='philadelphia'),
    made('Lightning is electricity',
         'In 1752, the story goes, he flew a kite in a thunderstorm with a key tied to its string, and drew sparks from '
         'the key, showing that lightning is electricity.',
         'He invented the lightning rod, which has saved countless buildings, and coined the words "battery", "positive" '
         'and "negative".',
         img='Lightning rod', y=1752, at='philadelphia'),
    made('Bifocals and stoves',
         'He also invented bifocal glasses, a better wood stove, a flexible medical tube and a glass harmonica that Mozart '
         'wrote music for.',
         'He never patented any of them, saying that we should be glad to serve others by our inventions, as we enjoy '
         'theirs.',
         img='Bifocals', y=1784),
    win('Hang together',
        'In 1776 he helped Jefferson polish the Declaration of Independence. At the signing he is said to have joked: "We '
        'must all hang together, or most assuredly we shall all hang separately."',
        img='United States Declaration of Independence', y=1776, at='philadelphia'),
    win('Winning over France',
        'Sent to Paris at 70, he charmed the French in his fur cap, playing the simple, wise American. In 1778 he won the '
        'alliance with France that helped win the war, and in 1783 he signed the peace with Britain.',
        img='Treaty of Alliance (1778)', y=1778, at='paris'),
    legacy("Franklin is the only founder who signed all four great documents of American independence. His face is on "
           'the 100-dollar bill.',
           'Showed that lightning is electricity',
           'Invented the lightning rod and bifocals',
           'Helped write the Declaration of Independence',
           "Won France's help for the American Revolution"),
)

story('leonhard-euler', 'He wrote more mathematics than anyone who ever lived, and much of it after he went blind.',
    life("A pastor's son in Basel",
         'Leonhard Euler was born in Basel, Switzerland, in 1707. His father, a pastor, hoped he would be one too. He went '
         'to the university at 13, where Johann Bernoulli, one of the best mathematicians in Europe, saw his gift, gave him '
         'lessons on Saturday afternoons and talked his father into letting him study mathematics instead.',
         img='Johann Bernoulli', cap='Johann Bernoulli, his teacher', y=1720, at='basel'),
    life('To St Petersburg',
         'In 1727, aged 20, he took a post at the Academy of Sciences that Peter the Great had founded in St Petersburg. He '
         'was hired for physiology but was soon doing mathematics, and at 26 he was put in charge of it. In 1734 he married '
         'Katharina Gsell, the daughter of a Swiss painter; of their 13 children, only five grew up.',
         img='Kunstkamera', cap="The Kunstkamera, the Academy's home", y=1727, at='st_petersburg'),
    win('The Basel problem',
        'For 85 years the best mathematicians, the Bernoullis of Basel among them, had tried to find the exact total of '
        '1 + 1/4 + 1/9 + 1/16 and so on forever, one over every square number. In 1735 Euler found it: π²/6, about '
        '1.645. Nobody had expected π, the number of circles, to turn up. It made him famous across Europe.',
        img='Basel problem', y=1735, at='st_petersburg'),
    made('The bridges of Königsberg',
         'People in Königsberg wondered if they could walk through their city crossing each of its seven bridges exactly '
         'once. In 1736 Euler proved they could not, and showed why: all that counts is how many bridges meet each piece of '
         'land.',
         'It was the first problem of graph theory, the mathematics of networks, which today plans delivery routes, maps the '
         'internet and finds the way on a phone.',
         img='Seven Bridges of Königsberg', y=1736, at='konigsberg'),
    life('Berlin, and the Cyclops',
         'In 1738, after a fever, he lost the sight of his right eye. "Now I will have fewer distractions," he is said to have '
         'joked. In 1741, with Russia in turmoil, he moved to the Academy of Frederick the Great in Berlin and stayed 25 '
         'years. The king, who loved clever talk, found the plain, devout Euler dull, and nicknamed him the Cyclops.',
         img='Frederick the Great', cap='Frederick the Great, his new master', y=1741, at='berlin'),
    made("Euler's formula",
         'In 1748 he showed that e^ix = cos x + i sin x, joining the number e of growth, the circles of trigonometry and i, '
         'the "imaginary" square root of −1. Put in π for x and it becomes e^iπ + 1 = 0: five key numbers in one line.',
         'It is often called the most beautiful equation in mathematics, and it is everyday work for engineers, who use it '
         'to calculate alternating current, radio waves and sound.',
         img="Euler's formula", y=1748, at='berlin'),
    tale('The fountains of Sanssouci',
         'Frederick wanted fountains for his palace at Sanssouci, and Euler worked out the pumps. The water never rose, and '
         'years later the king mocked him in a letter: "Vanity of vanities! Vanity of geometry!" Historians who have checked '
         "think Euler's sums were probably right, and the fault lay with the work as it was built.",
         img='Sanssouci', at='potsdam'),
    life('Blind, and busier than ever',
         'In 1766 Catherine the Great invited him back to St Petersburg, and soon a cataract took the sight of his other '
         'eye. When fire swept through his house in 1771, a craftsman from Basel carried him out. Yet he worked on, doing '
         'long sums in his head and dictating to his sons and helpers: in 1775 he finished about a paper a week.',
         img='Catherine the Great', cap='Catherine the Great, who brought him back', y=1771, at='st_petersburg'),
    life('The last afternoon',
         'On 18 September 1783 he gave a grandson a mathematics lesson, worked out with chalk how the new hot-air balloons '
         'rise, and talked about Uranus, the planet found two years before. That afternoon he had a stroke, and he died a few '
         'hours later. In the words of the French mathematician Condorcet, he "ceased to calculate and to live".',
         img='Uranus', cap='Uranus, the new planet he talked about that day', y=1783, at='st_petersburg'),
    legacy('Euler wrote more mathematics than anyone else in history: over 800 books and papers, about 80 volumes in all. '
           'Formulas and theorems named after him run through every part of mathematics. Laplace is said to have told his '
           'students: "Read Euler, read Euler, he is the master of us all."',
           'Found that 1 + 1/4 + 1/9 + 1/16 and so on adds up to π²/6',
           'Founded graph theory with the bridges of Königsberg',
           'Found e^ix = cos x + i sin x, which gives e^iπ + 1 = 0',
           'Gave maths the symbols f(x), e, i and Σ'),
)

story('frederick-the-great', 'The flute-playing soldier king who made Prussia a great power.',
    life('A prince who loved music',
         'Frederick was born in Berlin in 1712. His father, the soldier king Frederick William I, beat and humiliated him '
         'for loving music, French books and the flute, which he called unmanly.',
         img='Frederick William I of Prussia', cap='Frederick William I, his father', y=1712, at='berlin'),
    tale('The escape',
         'At 18 he tried to run away to England with his friend Hans von Katte. They were caught. His father made Frederick '
         'watch from a prison window as Katte was beheaded.',
         img='Hans Hermann von Katte', y=1730, at=(14.62, 52.57), where='Küstrin'),
    win('Seizing Silesia',
        'He became king in 1740, and within months marched into the rich Austrian province of Silesia and took it. He '
        'spent most of the next 23 years at war to keep it.',
        img='Silesian Wars', y=1740),
    win('Against the world',
        "In the Seven Years' War Prussia fought Austria, France and Russia at once, and Russian troops even took Berlin. "
        'Frederick, close to despair, was saved when the Russian empress died and her successor, a fan of his, made '
        'peace. Prussia kept Silesia.',
        img="Seven Years' War", y=1762),
    work('Sanssouci',
         'At Potsdam he built a small summer palace, Sanssouci, "without worries". There he played the flute in evening '
         'concerts, wrote more than 100 flute sonatas, and invited Voltaire to stay. They quarrelled after three years.',
         img='Sanssouci', y=1747, at='potsdam'),
    tale('The potato king',
         'He wanted his peasants to grow potatoes, but they would not. A story says he planted a royal potato field and had '
         'it guarded, so that people thought the potatoes must be precious, and stole them to plant. People still leave '
         'potatoes on his grave.',
         img='Potato', y=1756, at='potsdam'),
    win('First servant of the state',
        'He called himself "the first servant of the state". He banned torture, let everyone worship as they wished, '
        '"for everyone must be saved in his own way", and started schools. He died in 1786 and asked to be buried beside '
        'his dogs.',
        y=1786, at='potsdam'),
    legacy('Frederick turned Prussia into a great power, the core of the later German Empire, and became the model of an '
           '"enlightened" ruler: a philosopher king with absolute power.',
           'Made Prussia a great European power',
           "A brilliant general in the Seven Years' War",
           'Ended torture and allowed freedom of worship'),
)

story('jean-jacques-rousseau', 'The philosopher who wrote "Man is born free, and everywhere he is in chains".',
    life('A runaway from Geneva',
         'Rousseau was born in Geneva in 1712; his mother died days later. At 15, coming back from a walk to find the city '
         "gates shut for the night, he ran away rather than face his master's punishment.",
         img='Geneva', y=1728, at='geneva'),
    life('A wandering life',
         'He drifted through Savoy, Italy and France as a servant, music teacher and secretary, sheltered for years by a '
         'kind patroness. He invented a new way of writing music and moved to Paris in 1742.',
         y=1742, at='paris'),
    tale('Under a tree',
         'In 1749, walking to visit a friend in prison, he read about an essay contest: had the arts and sciences made '
         'people better? In a flash he saw that people are good by nature and society corrupts them. He sat under a tree '
         'and wept. His essay won the prize and made him famous.',
         y=1749, at='paris'),
    work('The Social Contract',
         'In 1762 he wrote The Social Contract, which begins: "Man is born free, and everywhere he is in chains." Laws, he '
         'argued, should express the will of the whole people. Its ideas inspired the French Revolution.',
         img='The Social Contract', y=1762),
    work('Emile',
         'In Emile, the same year, he said children should learn from nature and experience, not by rote and beatings. It '
         'changed ideas about childhood. Both books were burned, and he had to flee.',
         img='Emile, or On Education', y=1762),
    life('His own children',
         'The man who wrote about raising children left all five of his own, with his partner Thérèse, at a home for '
         'foundlings, where most children died. His enemies made sure everyone knew.',
         y=1760, at='paris'),
    life('Into the Panthéon',
         'In his last years he grew suspicious of everyone and wrote his Confessions, a frank story of his life. He died in '
         '1778. Sixteen years later the revolutionaries moved his body to the Panthéon in Paris.',
         img='Panthéon', y=1794, at='paris'),
    legacy("Rousseau's ideas on freedom, equality and the will of the people inspired the French Revolution and modern "
           'democracy, and his love of nature and feeling helped start the Romantic movement.',
           'Wrote The Social Contract',
           'Inspired the French Revolution',
           'Changed ideas about childhood and education'),
)

story('adam-smith', 'The absent-minded Scot who explained how markets work.',
    life('A boy from Kirkcaldy',
         'Adam Smith was born in 1723 in Kirkcaldy, Scotland. A family story says that at three he was carried off by '
         'travelling people and rescued. He studied at Glasgow and Oxford, where the teaching was so poor that he taught '
         'himself.',
         y=1723, at=(-3.16, 56.11), where='Kirkcaldy'),
    tale('The absent-minded professor',
         'He became a professor at Glasgow, famous for being absent-minded. He once walked into a tanning pit while '
         'explaining an idea to a friend, and once wandered 24 km in his dressing gown, lost in thought, before church '
         'bells brought him back.',
         img='University of Glasgow', y=1751, at='glasgow'),
    made('The division of labour',
         'In a pin factory, he noted, one worker alone might make 20 pins a day. Ten workers, each doing one step, could '
         'make 48,000.',
         'Specialising explains why modern economies are so productive, from factories to world trade.',
         img='Division of labour', y=1776),
    work('The Wealth of Nations',
         'In 1776 he published The Wealth of Nations. When people trade freely, each seeking their own gain, an "invisible '
         'hand" leads them to benefit everyone: "It is not from the benevolence of the butcher that we expect our dinner, '
         'but from his regard to his own interest."',
         img='The Wealth of Nations', y=1776, at='edinburgh'),
    tale('Not just selfishness',
         'His first book, The Theory of Moral Sentiments, said people are moved by sympathy for others, and he thought it '
         'his better book. He attacked greedy merchants and monopolies, and wanted schools for the poor.',
         img='The Theory of Moral Sentiments', y=1759),
    life('The customs officer',
         'In an irony he enjoyed, the champion of free trade spent his last years as a customs officer in Edinburgh, '
         'collecting taxes on imports. He had most of his papers burned before he died in 1790.',
         img='Panmure House', y=1778, at='edinburgh'),
    legacy('Adam Smith is called the father of economics. His ideas on free markets, trade and the division of labour '
           "shaped modern economies, and his face was on the Bank of England's 20-pound note.",
           'Wrote The Wealth of Nations',
           'The father of modern economics',
           'Explained the "invisible hand" of the market'),
)

story('immanuel-kant', 'The philosopher of Königsberg who asked what we can know and how we should act.',
    life("A harness maker's son",
         'Immanuel Kant was born in 1724 in Königsberg, in Prussia, now Kaliningrad in Russia, the son of a harness maker. '
         'In his whole life he never travelled more than about 100 km from his city.',
         img='Königsberg', y=1724, at='konigsberg'),
    tale('The clock of Königsberg',
         'He kept such a strict routine that neighbours were said to set their clocks by his afternoon walk. He missed it, '
         "the story goes, only when he was lost in reading Rousseau's Emile.",
         img='Königsberg Cathedral', y=1762, at='konigsberg'),
    made('How the Sun and planets formed',
         'In 1755 he suggested that the solar system formed from a spinning cloud of gas and dust, and that faint smudges '
         'in the sky were whole galaxies of stars.',
         'Scientists still explain the birth of the Sun and planets in much this way, and he was right about the galaxies.',
         img='Nebular hypothesis', y=1755, at='konigsberg'),
    work('The Critique of Pure Reason',
         'At 57 he published the Critique of Pure Reason, asking what we can know. The mind, he argued, is not a blank '
         'slate: it shapes experience itself, with space, time and cause built in. It is one of the most important, and '
         'hardest, books in philosophy.',
         img='Critique of Pure Reason', y=1781, at='konigsberg'),
    win('Treat people as ends',
        'In morals, he said, act only by rules you could want everyone to follow, and treat people always as ends in '
        'themselves, never just as tools. This idea of human dignity underlies human rights today.',
        img='Groundwork of the Metaphysic of Morals', y=1785),
    work('Perpetual Peace',
         'In 1795 he proposed a league of free nations to end war for ever, an idea that inspired the League of Nations '
         'and the United Nations.',
         img='Perpetual Peace: A Philosophical Sketch', y=1795),
    legacy('Kant is one of the greatest philosophers of all time. His tomb bears his famous words: "The starry heavens '
           'above me and the moral law within me."',
           'Wrote the Critique of Pure Reason',
           'Taught that people must be treated as ends, never only as means',
           'Imagined a league of nations for lasting peace'),
)

story('james-cook', 'The farm boy turned navigator who mapped the Pacific.',
    life("A labourer's son",
         'James Cook was born in 1728 in Yorkshire, the son of a farm labourer. He worked in a shop by the sea, then went to '
         'sea on coal ships out of Whitby. At 26 he joined the Royal Navy as a common seaman.',
         img='Whitby', y=1746, at=(-0.61, 54.49), where='Whitby'),
    win('Charting Canada',
        "In the Seven Years' War he charted the St Lawrence River so precisely that British ships could carry an army up "
        "to Quebec in 1759. His later charts of Newfoundland's coast were used for 200 years.",
        img='Saint Lawrence River', y=1759, at='quebec'),
    win('The first voyage',
        'In 1768 he sailed the Endeavour to Tahiti to watch Venus cross the face of the Sun, then, with secret orders, '
        'searched for a southern continent. He charted New Zealand and the east coast of Australia, landing at Botany Bay '
        'in 1770.',
        img='HMS Endeavour', y=1770, at='botany_bay'),
    made('Beating scurvy',
         'Scurvy killed more sailors than storms did. Cook made his crews eat sauerkraut, fresh fruit and greens, and kept '
         'his ship clean and dry.',
         'On voyages lasting years, almost none of his men died of scurvy, an astonishing feat at the time.',
         img='Scurvy', y=1772),
    win('Around Antarctica',
        'On his second voyage he became the first to cross the Antarctic Circle, sailing all the way round the frozen '
        'continent without ever seeing it. He found his longitude with a new kind of clock, a copy of John Harrison\'s '
        'marine chronometer.',
        img='Second voyage of James Cook', y=1774),
    life('Death in Hawaii',
         'On his third voyage, searching for a passage around North America, he reached Hawaii. Back there in 1779 to '
         'repair a mast, he quarrelled with islanders over a stolen boat, and was killed on the beach at Kealakekua Bay.',
         img='Kealakekua Bay', y=1779, at='kealakekua'),
    legacy("Cook mapped more of the Earth than anyone before him, from Canada to Antarctica. His voyages opened the "
           'Pacific to European science, trade and settlement, with terrible results for many of its peoples.',
           'Charted New Zealand and eastern Australia',
           'First to cross the Antarctic Circle',
           'Mapped more of the world than anyone before him'),
)

story('catherine-the-great', 'The German princess who seized the Russian throne and ruled for 34 years.',
    life('A German princess',
         'She was born Sophie of Anhalt-Zerbst in 1729, a minor German princess. At 14 she was chosen as a bride for Peter, '
         'heir to the Russian throne. She learned Russian, joined the Orthodox Church and took the name Catherine.',
         y=1744, at=(14.55, 53.43), where='Stettin'),
    life('An unhappy marriage',
         'Her husband played with toy soldiers and worshipped Prussia, Russia\'s enemy. Catherine read Voltaire and '
         'Montesquieu, and made friends among the palace guards.',
         img='Peter III of Russia', cap='Peter III, her husband', y=1750, at='st_petersburg'),
    win('Seizing the throne',
        'In 1762, six months after Peter became tsar, she led a coup with the guards, riding at their head in a guards '
        'uniform. Peter was forced to give up the throne and was killed days later, probably by her supporters.',
        y=1762, at='st_petersburg'),
    win('Expanding Russia',
        'She ruled for 34 years. Her armies beat the Ottomans and won Crimea and the Black Sea coast, and with Prussia and '
        'Austria she carved up Poland until it vanished from the map.',
        img='Russian Empire', y=1783),
    tale('Potemkin villages',
         'Her favourite and general, Potemkin, led her on a grand tour of Crimea in 1787. A legend says he set up fake '
         'villages along the route to impress her. A "Potemkin village" still means a fake front.',
         img='Grigory Potemkin', y=1787),
    work('The Hermitage',
         'She bought whole collections of paintings from across Europe, wrote to Voltaire and Diderot, and bought '
         "Diderot's library. Her collection became the Hermitage Museum, one of the greatest in the world.",
         img='Hermitage Museum', y=1764, at='st_petersburg'),
    life('The serfs',
         'She talked of reform, but the lives of Russia\'s serfs grew harder under her. In 1773 the Cossack Pugachev led a '
         'huge peasant revolt. It was crushed, and he was executed in Moscow.',
         img="Pugachev's Rebellion", y=1774, at='moscow'),
    legacy('Catherine pushed Russia to the Black Sea and made it a great European power. A patron of art and the '
           'Enlightenment, she is the longest-ruling woman in Russian history.',
           'Seized power from her husband',
           'Expanded Russia to the Black Sea',
           'Founded the Hermitage collection'),
)

story('george-washington', 'The general who won American independence, then gave up power.',
    life('A Virginia surveyor',
         'George Washington was born in Virginia in 1732. His father died when he was 11, and at 16 he worked as a '
         'surveyor in the wilderness. The famous story of him chopping down a cherry tree and saying "I cannot tell a lie" '
         'was made up by a writer after his death.',
         img='Mount Vernon', y=1748, at='mount_vernon'),
    life('Four bullet holes',
         'In 1754, aged 22, he led Virginia soldiers into the Ohio country and fired some of the first shots of the French '
         'and Indian War. The next year he survived a disastrous ambush with four bullet holes in his coat and two horses '
         'shot from under him.',
         img='Braddock Expedition', y=1755, at='fort_duquesne'),
    win('Crossing the Delaware',
        'In 1775 Congress made him commander of the new American army. On Christmas night 1776, after months of defeats, '
        'he led his ragged army across the icy Delaware River and surprised the enemy at Trenton.',
        img='Washington Crossing the Delaware', y=1776, at='trenton'),
    life('Valley Forge',
         'In the winter of 1777 his army camped at Valley Forge with too little food, clothing or shoes, and about 2,000 '
         'men died of disease. He held the army together, and it came out of the winter trained and tougher.',
         img='Valley Forge', y=1777, at='valley_forge'),
    win('Yorktown',
        'In 1781, with a French army and fleet, he trapped the British general Cornwallis at Yorktown, in Virginia. The '
        'British surrendered, and the war was as good as won.',
        img='Siege of Yorktown', y=1781, at='yorktown'),
    win('Giving up power',
        'Instead of making himself king, he resigned his command in 1783 and went home to farm. King George III is said to '
        'have called that the act of the greatest man in the world. In 1789 he became the first president, and stepped '
        'down after two terms.',
        img='Inauguration of George Washington', y=1789, at='new_york'),
    tale('Hippo teeth',
         'By the time he was president he had only one of his own teeth left. His false teeth were not wooden, as legend '
         'says, but made of hippopotamus ivory, human teeth and metal springs.',
         y=1789),
    life('His slaves',
         'Washington owned enslaved people at Mount Vernon all his life. In his will he ordered that the people he owned '
         'be freed after his wife\'s death. He died in 1799.',
         y=1799, at='mount_vernon'),
    legacy('Washington led the colonies to independence and set the example of a leader who steps down. He is called the '
           '"Father of His Country", and the capital bears his name.',
           'Led the army that won American independence',
           'First president of the United States',
           'Gave up power when he could have kept it'),
)

from _lib import story, life, win, made, work, song, tale, legacy

story('james-watt', 'The instrument maker whose steam engine powered the Industrial Revolution.',
    life('The instrument maker',
         'James Watt was born in 1736 in Greenock, Scotland, the son of a shipwright. Often ill as a boy, he was taught '
         'mostly at home, and loved taking things apart. He learned to make scientific instruments in London, and in 1757 '
         'opened a workshop at the University of Glasgow.',
         img='University of Glasgow', y=1757, at='glasgow'),
    tale("The kettle",
         "A famous story says that as a boy he sat watching the steam lift the lid of his aunt's kettle, and dreamed of "
         'its power. It was told long after his death, and is probably made up, but it stuck.',
         img='Kettle', y=1750, at=(-4.76, 55.95), where='Greenock'),
    made('The separate condenser',
         'Asked to repair a model of the old Newcomen steam engine, he saw that it wasted most of its coal heating the '
         'cylinder up again at every stroke. On a Sunday walk in 1765 the answer came: cool the steam in a separate '
         'chamber.',
         'His engine used only about a quarter of the coal, which made steam power cheap enough to use almost anywhere.',
         img='Watt steam engine', y=1765, at='glasgow'),
    win('Boulton and Watt',
        'In 1775 he went into business with Matthew Boulton, a Birmingham factory owner, who told a visitor: "I sell here, '
        'sir, what all the world desires to have: power." Their engines pumped water out of the tin mines of Cornwall.',
        img='Matthew Boulton', cap='Matthew Boulton, his partner', y=1776, at='birmingham'),
    made('Engines that turn wheels',
         'He added gears that turned the up and down push of the engine into turning motion, a linkage he was proudest of, '
         'and a spinning governor that kept the speed steady by itself.',
         'Steam engines could now drive the machines of cotton mills and factories, and later railway locomotives and '
         'ships.',
         img='Centrifugal governor', y=1788, at='birmingham'),
    made('The horsepower',
         'To sell engines to people who used horses to work their mills, he measured how much work a horse could do, and '
         'rated his engines in "horsepower".',
         'Car engines are still rated in horsepower, and the unit of power, the watt, is named after him: every light bulb '
         'carries his name.',
         img='Horsepower', y=1782),
    tale('The office copier',
         'Tired of copying out his business letters by hand, in 1780 he invented a press that copied a letter written in '
         'special ink onto damp paper. Offices used his copying press for more than a century.',
         y=1780, at='birmingham'),
    legacy("Watt's engine powered the Industrial Revolution, which changed how people live and work more than anything "
           'since the invention of farming.',
           'Invented the separate condenser',
           'Made steam power cheap enough for factories',
           'Gave us the horsepower; the watt is named after him'),
)

story('antoine-lavoisier', 'The father of modern chemistry, who named oxygen and lost his head in the Revolution.',
    life('A rich young scientist',
         'Antoine Lavoisier was born in Paris in 1743 to a wealthy family. He trained as a lawyer, but loved science. At 25 '
         'he bought a share in the Ferme générale, a private company that collected taxes for the king. It made him rich '
         'and paid for the best laboratory in Europe.',
         y=1768, at='paris'),
    life('Marie-Anne',
         'In 1771 he married Marie-Anne Paulze, who was 13. She became his partner in science: she learned English to '
         'translate the work of British chemists, kept the laboratory notes, and drew the pictures for his books.',
         img='Portrait of Antoine-Laurent Lavoisier and his Wife', cap='The Lavoisiers, painted by Jacques-Louis David',
         y=1771, at='paris'),
    made('Oxygen and burning',
         'Scientists thought that things burn by giving off a substance called phlogiston. Weighing everything with great '
         'care, he showed that burning metals gain weight: they combine with a gas from the air, which he named oxygen.',
         'This overturned the old theory and explained burning, rusting and breathing. It was the start of modern '
         'chemistry.',
         img='Oxygen', y=1777, at='paris'),
    made('Nothing is lost',
         'He showed that in a chemical reaction nothing is created or destroyed: the weight of everything at the end equals '
         'the weight at the start. He also showed that water is made of hydrogen and oxygen, and named hydrogen.',
         'The conservation of mass became the basic law of chemistry.',
         img='Conservation of mass', y=1783, at='paris'),
    work('The first modern chemistry book',
         'With others he invented the system of names for chemicals still used today, such as iron oxide and sulfuric acid. '
         'In 1789 he published his Elementary Treatise of Chemistry, with the first modern list of the elements.',
         img='Traité élémentaire de chimie', y=1789, at='paris'),
    win('The metric system',
        'He served on the committee that created the metric system, with the metre and the kilogram, so that people '
        'everywhere could measure in the same units.',
        img='Metric system', y=1791, at='paris'),
    life('The guillotine',
         'During the Terror, all the former tax collectors were arrested. Lavoisier was guillotined in Paris on 8 May 1794, '
         'aged 50. The mathematician Lagrange said: "It took them only an instant to cut off that head, and a hundred years '
         'may not produce another like it."',
         img='Place de la Concorde', y=1794, at='paris'),
    tale('The blinking head',
         'A legend says he agreed to blink for as long as he could after his head was cut off, to test how long a head '
         'stays alive. There is no record of it, but the story is still told in chemistry classes.',
         y=1794, at='paris'),
    legacy('Lavoisier turned chemistry from guesswork into a science of exact measurement, and is called the father of '
           'modern chemistry.',
           'Named oxygen and hydrogen',
           'Showed that mass is never lost in a reaction',
           'Wrote the first modern list of the elements'),
)

story('toussaint-louverture', 'Born enslaved, he led the revolt that created Haiti, the first free Black republic.',
    life('Born enslaved',
         "He was born about 1743 on the Bréda plantation in Saint-Domingue, France's richest colony, now Haiti, where half a "
         'million enslaved Africans grew sugar and coffee. He learned to read, worked as a coachman and was freed around '
         '1776.',
         y=1776, at=(-72.2, 19.76), where='Cap-Français'),
    life('The great revolt',
         'In August 1791 the enslaved people of the north rose up and burned the plantations: the largest slave revolt in '
         'history. Toussaint, nearly 50, joined them, first as a healer who knew herbal medicine, then as a commander who '
         'trained a disciplined army.',
         img='Haitian Revolution', y=1791, at=(-72.2, 19.76), where='Cap-Français'),
    tale('The opening',
         'In 1793 he took the name Louverture, "the opening". One story says a French official exclaimed that this man '
         'made an opening everywhere; others think it came from a gap in his teeth. Nobody knows for sure.',
         y=1793),
    win('Freedom and victory',
        'When France abolished slavery in 1794, he joined the French side and turned on the Spanish and British armies '
        'that had invaded the colony. By 1798 the British, beaten in battle and by disease, had sailed away.',
        y=1798, at='port_au_prince'),
    win('Governor for life',
        'He became governor of the whole island, rebuilt the plantations with paid, though tightly controlled, labour, and '
        'in 1801 gave it a constitution that banned slavery for ever and made him governor for life.',
        y=1801, at=(-72.2, 19.76), where='Cap-Français'),
    life('Betrayed',
         'In 1802 Napoleon sent a huge army to retake the colony. Toussaint was invited to talks, seized and shipped to '
         'France. He said: "In overthrowing me you have cut down only the trunk of the tree of liberty. It will spring up '
         'again from the roots, for they are many and deep."',
         y=1802),
    life('Death in the mountains',
         'He was locked in Fort de Joux, a freezing fortress in the Jura mountains, and died there in April 1803. Months '
         'later his former officer Dessalines defeated the French, and on 1 January 1804 Haiti became independent.',
         img='Fort de Joux', y=1803, at=(6.38, 46.87), where='Fort de Joux'),
    legacy('Toussaint led the only slave revolt in history that founded a free nation. Haiti became the first Black '
           'republic, and his fight inspired enslaved people and abolitionists everywhere.',
           'Led the largest slave revolt in history',
           'Defeated Spanish, British and French armies',
           'Paved the way for Haiti, the first Black republic'),
)

story('thomas-jefferson', 'He wrote "all men are created equal" and doubled the size of the United States.',
    life('A Virginia planter',
         'Thomas Jefferson was born in Virginia in 1743 and inherited land and enslaved people from his father. He studied '
         'at the College of William and Mary, became a lawyer, read Greek and Latin for pleasure and played the violin.',
         img='College of William & Mary', y=1762, at=(-76.71, 37.27), where='Williamsburg'),
    win('The Declaration of Independence',
        'In June 1776, aged 33, he wrote the first draft of the Declaration of Independence: "We hold these truths to be '
        'self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable '
        'Rights."',
        img='Declaration of Independence (painting)', y=1776, at='philadelphia'),
    win('Freedom of religion',
        'His Virginia Statute for Religious Freedom, passed in 1786, said no one could be forced to support a church or be '
        'punished for their beliefs. It became a model for the First Amendment.',
        img='Virginia Statute for Religious Freedom', y=1786, at='richmond'),
    life('Paris',
         'From 1785 he was the American minister in Paris. He watched the French Revolution begin, and his friend Lafayette '
         'showed him his draft of the Declaration of the Rights of Man.',
         img='Declaration of the Rights of Man and of the Citizen', y=1789, at='paris'),
    win('The Louisiana Purchase',
        'As the third president, in 1803 he bought the huge Louisiana territory from Napoleon for 15 million dollars, '
        'doubling the size of the country, and sent Lewis and Clark to explore it all the way to the Pacific.',
        img='Louisiana Purchase', y=1803, at='washington'),
    work('Monticello',
         'He designed his own hilltop house, Monticello, and filled it with gadgets: a revolving bookstand, a great clock, '
         'and a machine that copied his letters as he wrote. He also designed a better plough.',
         img='Monticello', y=1809, at='monticello'),
    life('The contradiction',
         'The man who wrote that all men are created equal enslaved more than 600 people in his life. Most historians '
         'believe he fathered six children with Sally Hemings, an enslaved woman at Monticello. He freed only a few people, '
         'among them her children.',
         at='monticello'),
    tale('The Fourth of July',
         'Jefferson and John Adams, friends, then bitter rivals, then friends again by letter, both died on 4 July 1826, '
         'exactly 50 years after the Declaration. Adams\'s last words were said to be "Thomas Jefferson survives." He had '
         'died a few hours earlier.',
         y=1826, at='monticello'),
    legacy('Jefferson chose what went on his own tombstone: author of the Declaration of Independence and of the Statute '
           'for Religious Freedom, and father of the University of Virginia. Not a word about being president.',
           'Wrote the Declaration of Independence',
           'Third president; doubled the country with the Louisiana Purchase',
           'Championed freedom of religion'),
)

story('johann-wolfgang-von-goethe', "Germany's greatest writer, author of Faust, who also studied plants, bones and colours.",
    life('A Frankfurt boy',
         'Johann Wolfgang Goethe was born in Frankfurt in 1749 to a wealthy family. His father made him study law in Leipzig '
         'and Strasbourg, but he spent his time writing poems, drawing and falling in love.',
         y=1749, at='frankfurt'),
    work('The Sorrows of Young Werther',
         'In 1774, at 24, he published a short novel about a young man who kills himself over a love he cannot have. It '
         'made him famous across Europe. Young men copied Werther\'s blue coat and yellow waistcoat, and Napoleon said he '
         'read it seven times.',
         img='The Sorrows of Young Werther', y=1774, at='frankfurt'),
    life('Minister in Weimar',
         'In 1775 the young duke of Weimar invited him to his small court. Goethe stayed for the rest of his life, as a '
         'minister in charge of mines, roads and money, and later as director of the theatre.',
         img='Weimar', y=1775, at='weimar'),
    tale('Running away to Italy',
         'In 1786, tired of his duties, he slipped away before dawn without telling anyone, and travelled to Italy under a '
         'false name. He stayed nearly two years, drawing ruins in Rome, and came back a different writer.',
         img='Goethe in the Roman Campagna', y=1786, at='rome'),
    made('Bones, plants and colours',
         'He found a small bone in the human jaw that was thought to exist only in animals, studied how all the parts of a '
         'plant grow from one leaf-like form, and wrote a book on colour.',
         'His idea that living things vary on a shared plan was an early step toward the theory of evolution. His colour '
         'theory was wrong as physics, but inspired painters such as Turner.',
         img='Theory of Colours', y=1810, at='weimar'),
    win('Goethe and Schiller',
        'From 1794 until Schiller died in 1805, he and the poet Friedrich Schiller worked side by side in Weimar. Together '
        'they made the little town the capital of German literature.',
        img='Goethe–Schiller Monument', y=1794, at='weimar'),
    work('Faust',
         'He worked on Faust for about 60 years: the story of a scholar who sells his soul to the devil, Mephistopheles, in '
         'return for knowledge and pleasure. "Two souls, alas, dwell in my breast." He finished it months before he died.',
         img="Goethe's Faust", y=1831, at='weimar'),
    tale('"More light!"',
         'He died in Weimar in 1832, aged 82. His last words are said to have been "More light!" In fact he seems to have '
         'asked for the window shutters to be opened, to let more light in.',
         y=1832, at='weimar'),
    legacy("Goethe is Germany's greatest writer, and the country's cultural institutes around the world are named after "
           'him.',
           'Wrote Faust and The Sorrows of Young Werther',
           "Germany's greatest poet",
           'Also a scientist of plants, bones and colour'),
)

story('wolfgang-amadeus-mozart', 'The child prodigy who wrote more than 600 works before he died at 35.',
    life('The child prodigy',
         'Mozart was born in Salzburg in 1756. His father Leopold, a court musician, saw that the boy could pick out chords '
         'at three and write music at five. From the age of six he toured the courts of Europe with his sister Nannerl, '
         'playing for kings and empresses.',
         img='Mozart family', y=1762, at='salzburg'),
    tale('A kiss for the empress',
         'At six he played for the empress Maria Theresa in Vienna. His father wrote that afterwards the boy jumped onto the '
         "empress's lap and kissed her. A later story says he slipped on the polished floor, and when the little princess "
         'Marie Antoinette helped him up, he said he would marry her.',
         img='Schönbrunn Palace', y=1762, at='vienna'),
    tale('The secret music',
         "At 14, in Rome, he heard Allegri's Miserere in the Sistine Chapel, a piece the Vatican did not allow to be "
         'copied. Back at his lodgings he wrote the whole thing out from memory, after hearing it just once.',
         img='Miserere (Allegri)', y=1770, at='rome'),
    life('Free in Vienna',
         'He hated serving the Archbishop of Salzburg, who treated him like a servant. In 1781 he quit, and was thrown out '
         'with a kick from the archbishop\'s steward. He settled in Vienna as a freelance musician and married Constanze '
         'Weber.',
         img='Constanze Mozart', cap='Constanze, his wife', y=1781, at='vienna'),
    song('Rondo alla turca',
         'Vienna loved anything Turkish, from coffee to the drums and cymbals of Turkish military bands. Around 1783 Mozart '
         'ended a piano sonata with a "Turkish march" that imitates them. It became one of his best known tunes.',
         page='Piano Sonata No. 11 (Mozart)', hint='turca', y=1783, at='vienna'),
    song('Eine kleine Nachtmusik',
         'In 1787 he wrote "A little night music", a serenade for strings, now one of the most famous pieces ever. It was '
         'not published until decades after his death.',
         page='Eine kleine Nachtmusik', hint='allegro', y=1787, at='vienna'),
    song('Symphony No. 40',
         'In a single summer, in about six weeks, he wrote his last three symphonies, perhaps the greatest of his time. The '
         'restless No. 40 in G minor opens with this famous theme.',
         page='Symphony No. 40 (Mozart)', hint='molto allegro', y=1788, at='vienna'),
    song('The Queen of the Night',
         'His operas The Marriage of Figaro, Don Giovanni and The Magic Flute are still sung all over the world. In The '
         'Magic Flute, the furious Queen of the Night sings one of the hardest arias ever written, leaping to a very high F.',
         page='Der Hölle Rache kocht in meinem Herzen', y=1791, at='vienna'),
    song('The unfinished Requiem',
         'In 1791 a stranger ordered a Requiem, a mass for the dead, for a count who meant to pass it off as his own. Mozart, '
         'very ill, came to feel he was writing it for himself. He died at 35 with it unfinished. The tale that his rival '
         'Salieri poisoned him is false.',
         page='Requiem (Mozart)', hint='lacrimosa', y=1791, at='vienna'),
    legacy('Mozart wrote more than 600 works in 35 years: symphonies, concertos, chamber music and operas that are still '
           'played somewhere in the world every day.',
           'Wrote more than 600 works',
           'Composed The Magic Flute and The Marriage of Figaro',
           'A master of every kind of music of his time'),
)

story('napoleon', 'The Corsican officer who crowned himself emperor and conquered most of Europe.',
    life('A boy from Corsica',
         'Napoleon Bonaparte was born in 1769 in Ajaccio, on Corsica, a year after France took the island. At nine he was '
         'sent to a military school in France, where the other boys mocked his accent. At 16 he became an artillery '
         'officer.',
         img='Ajaccio', y=1769, at='ajaccio'),
    win('Toulon',
        'In 1793, during the French Revolution, the British held the port of Toulon. The young captain worked out where to '
        'put the guns to drive their fleet from the harbour. It worked, and at 24 he was made a general.',
        img='Siege of Toulon', y=1793, at='toulon'),
    win('Italy and Egypt',
        'In 1796 he led a ragged army into Italy and beat the Austrians again and again. In 1798 he invaded Egypt and beat '
        'the Mamluks at the Battle of the Pyramids, though the British sank his fleet.',
        img='Battle of the Pyramids', y=1798, at='cairo'),
    tale('The Rosetta Stone',
         'He took 167 scholars to Egypt to study the country. In 1799 his soldiers dug up a stone carved with the same '
         'text in Greek and in hieroglyphs. Thanks to it, the scholar Champollion learned to read hieroglyphs in 1822.',
         img='Rosetta Stone', y=1799, at=(30.42, 31.4), where='Rosetta'),
    win('Emperor',
        'Back in France he seized power in 1799. In 1804, in Notre-Dame in Paris, with the pope looking on, he took the '
        'crown and placed it on his own head: Napoleon I, Emperor of the French.',
        img='The Coronation of Napoleon', y=1804, at='paris'),
    win('The Napoleonic Code',
        'His code of laws, of 1804, made all men equal before the law, ended the old privileges of the nobles and protected '
        'property. It is still the basis of the law in France and in many countries.',
        img='Napoleonic Code', y=1804, at='paris'),
    win('Austerlitz',
        'In 1805 he crushed the armies of the Austrian and Russian emperors at Austerlitz, his greatest victory. By 1810 he '
        'ruled or controlled most of Europe, and put his brothers on its thrones.',
        img='Battle of Austerlitz', y=1805, at='austerlitz'),
    life('Moscow',
         'In 1812 he invaded Russia with some 600,000 men. He reached Moscow, but the Russians set it on fire. His army '
         'retreated through the winter, starving and freezing, and most of them never came back.',
         img='French invasion of Russia', y=1812, at='moscow'),
    life('Elba and Waterloo',
         'Beaten by all of Europe, he was exiled in 1814 to the little island of Elba. Within a year he escaped and returned '
         'to Paris. For a hundred days he ruled again, until Wellington and Blücher defeated him at Waterloo in 1815.',
         img='Battle of Waterloo', y=1815, at='waterloo'),
    tale('Not so short',
         'His soldiers called him "the little corporal", and British cartoons drew him tiny. In fact he was about 1.69 m '
         'tall, average or a little more for his time. French inches were longer than English ones, which added to the '
         'confusion.',
         img='The Plumb-pudding in Danger', cap='A British cartoon of 1805: Pitt and a small Napoleon carve up the world', y=1805),
    life('St Helena',
         'The British sent him to St Helena, a remote island in the South Atlantic, 1,900 km from Africa. He spent his last '
         'years dictating his memoirs, and died there in 1821, aged 51.',
         img='Longwood House', y=1821, at='st_helena'),
    legacy('Napoleon remade Europe. His wars killed millions, but his laws, schools and the idea that talent, not birth, '
           'should decide who rises spread across the continent.',
           'Crowned himself Emperor of the French',
           'Gave France the Napoleonic Code',
           'One of the greatest generals in history'),
)

story('alexander-von-humboldt', 'The explorer who saw nature as one connected web, and the founder of ecology.',
    life('A Prussian noble',
         'Alexander von Humboldt was born in Berlin in 1769. He studied mining and worked as a mine inspector, inventing a '
         'safety lamp and a breathing mask for miners. He dreamed of exploring the tropics.',
         img='Berlin', y=1792, at='berlin'),
    life('Off to the Americas',
         'When his mother died he spent his inheritance on an expedition. In 1799 he sailed for Spanish America with the '
         'French botanist Aimé Bonpland and more than 40 instruments, landing in what is now Venezuela.',
         img='Aimé Bonpland', cap='Aimé Bonpland, his companion', y=1799, at=(-64.18, 10.46), where='Cumaná'),
    tale('The electric eels',
         'On the plains of Venezuela he wanted to study electric eels. Local men drove horses into a pool full of them; the '
         'eels attacked, stunning the horses with shocks. Humboldt got painful shocks himself and wrote it all down.',
         img='Electric eel', y=1800, at=(-67.43, 8.93), where='Calabozo'),
    win('Down the Orinoco',
        'He paddled some 2,000 km up the Orinoco and its rivers, through jungle and clouds of mosquitoes, and mapped the '
        'Casiquiare, a natural channel that links the Orinoco to the Amazon.',
        img='Casiquiare canal', y=1800, at=(-66.4, 2.6), where='Casiquiare'),
    win('Chimborazo',
        'In 1802 he climbed most of the way up Chimborazo in Ecuador, then thought the highest mountain in the world. He '
        'reached about 5,900 m, higher than anyone known before him, with bleeding gums and no oxygen.',
        img='Chimborazo', y=1802, at=(-78.82, -1.47), where='Chimborazo'),
    made('The web of life',
         'On the mountain he saw that plants change in bands with height, just as they change from the equator to the '
         'poles, and drew it all on one famous picture. He also saw how cutting forests dried out a lake.',
         'He showed nature as one connected web, the idea at the root of ecology, and was one of the first to warn that '
         'people can change the climate.',
         y=1802, at=(-78.82, -1.47), where='Chimborazo'),
    made('Lines on weather maps',
         'Back in Europe he drew the first maps with isotherms, lines that join places with the same average temperature, '
         'and found that Earth\'s magnetism grows weaker toward the equator.',
         'Weather maps still use his lines today.',
         img='Contour line', y=1817, at='paris'),
    tale('Famous everywhere',
         'He visited Thomas Jefferson in 1804, and was said to be the most famous man in the world after Napoleon. More '
         'places, plants and animals are named after him than after almost anyone: a current, a penguin, a squid, even a '
         'sea on the Moon.',
         img='Humboldt penguin', y=1804, at='washington'),
    work('Cosmos',
         'In his 70s he set out to describe the whole universe, from stars to mosses, in one work, Cosmos. He was still '
         'writing its fifth volume when he died in Berlin in 1859, aged 89.',
         img='Cosmos (Humboldt)', y=1845, at='berlin'),
    legacy('Humboldt saw nature as one connected whole. He inspired Darwin, who said Humboldt was the reason he went '
           'exploring, and the first environmentalists.',
           'Explored South America and climbed Chimborazo',
           'Founded the idea of nature as a web of life',
           'Inspired Darwin and the first environmentalists'),
)

story('simon-bolivar', 'El Libertador, who freed six South American countries from Spanish rule.',
    life('A rich orphan',
         'Simón Bolívar was born in 1783 in Caracas, Venezuela, into one of the richest families in Spanish America. By nine '
         'he had lost both parents. His tutor, Simón Rodríguez, filled his head with the ideas of Rousseau.',
         img='Caracas', y=1783, at='caracas'),
    life('A vow in Rome',
         'At 18 he married in Spain, but his young wife died of yellow fever eight months later. He never married again. In '
         '1805, on a hill in Rome, he swore he would not rest until he had freed his country from Spain.',
         img='Monte Sacro (Rome)', y=1805, at='rome'),
    life('Defeat and exile',
         'Venezuela declared independence in 1811, but the Spanish crushed the new republic twice. Bolívar fled to Jamaica, '
         'where in 1815 he wrote his Jamaica Letter, dreaming of a free and united South America.',
         img='Jamaica Letter', y=1815, at='kingston'),
    win('Over the Andes',
        'In 1819 he led his army across flooded plains and over the freezing passes of the Andes, where many men died of '
        'cold. Then he surprised the Spanish at Boyacá and freed what is now Colombia.',
        img='Battle of Boyacá', y=1819, at='boyaca'),
    win('Gran Colombia',
        'He founded Gran Colombia, a great republic of today\'s Colombia, Venezuela, Ecuador and Panama, and became its '
        'president. His victory at Carabobo in 1821 freed Venezuela.',
        img='Gran Colombia', y=1821, at='bogota'),
    win('Peru and Bolivia',
        'He drove the Spanish from Peru, and in 1824 his general Sucre won the last great battle, at Ayacucho. The new '
        'country of Upper Peru was named Bolivia in his honour.',
        img='Battle of Ayacucho', y=1824, at='ayacucho'),
    tale('Out of the window',
         'In 1828 assassins burst into his palace in Bogotá. His partner, Manuela Sáenz, held them off while he escaped '
         'through a window. He called her "the liberator of the Liberator".',
         img='Manuela Sáenz', y=1828, at='bogota'),
    life('Ploughing the sea',
         'His great republic broke apart in quarrels. Sick and disappointed, he gave up power in 1830 and died near Santa '
         'Marta at 47. "Those who have served the revolution," he wrote, "have ploughed the sea."',
         y=1830, at='santa_marta'),
    legacy('Bolívar freed six countries from Spanish rule. He is called El Libertador, and a country, a currency and '
           'countless squares are named after him.',
           'Freed Venezuela, Colombia, Ecuador, Peru, Bolivia and Panama',
           'Founded Gran Colombia',
           'Called El Libertador, the Liberator'),
)

"""Discovery: the great scientists, mathematicians, inventors, philosophers and artists among the people with a story,
listed century by century. The Discovery button at the top of the map opens the list; each name opens that person's
story. python3 content/stories/build_discovery.py checks this file and writes data/discovery.json.

D(person id, fields, year, what they were, what they are known for, c=True when the year is approximate, when='' to
show no year at all, for someone whose dates are only tradition)
  fields  one or more of: sci (scientists), math (mathematicians), inv (inventors), phil (philosophers), art (artists:
          painters, sculptors, architects, composers and writers). The list's buttons filter by them.
  year    the year of the first thing named in "known for", the work they are best known for. It puts them in their
          century: 6th century BC is 600 to 501 BC, and from AD 1 the 1600s are the 17th century.
Only people with a story belong here, and not all of them: rulers, generals, explorers and founders of religions stay
out (the leaders have their own list, leaders.py) unless the work is their own (Marcus Aurelius's Meditations, Sejong's alphabet; not Shah Jahan's Taj Mahal), and
Anne Frank's diary is told on the map as history rather than listed with the artists.
"""

FIELDS = {'sci': 'Scientists', 'math': 'Mathematicians', 'inv': 'Inventors', 'phil': 'Philosophers', 'art': 'Artists'}
DISCOVERY = []


def D(pid, fields, year, what, known, c=False, when=None):
    e = {'id': pid, 'f': fields.split(), 'y': year, 'as': what, 'k': known}
    if c:
        e['c'] = 1
    if when is not None:
        e['when'] = when
    DISCOVERY.append(e)


# ---- the ancient world
D('pythagoras', 'math phil', -530, 'Mathematician and philosopher', 'The Pythagorean theorem, and the maths of music', c=True)
D('laozi', 'phil', -530, 'Philosopher', 'The Tao Te Ching, the book of the Way', when='')
D('confucius', 'phil', -520, 'Philosopher and teacher', 'Teaching on family, duty and good government', c=True)
D('sun-tzu', 'phil', -500, 'General and strategist', 'The Art of War', c=True)
D('socrates', 'phil', -430, 'Philosopher', 'The Socratic method: teaching by asking questions', c=True)
D('plato', 'phil', -387, 'Philosopher', 'The Academy, and The Republic', c=True)
D('aristotle', 'phil sci', -350, 'Philosopher and scientist', 'Logic, biology and the Lyceum', c=True)
D('euclid', 'math', -300, 'Mathematician', 'The Elements, the geometry book used for 2,000 years', c=True)
D('archimedes', 'math sci inv', -250, 'Mathematician and inventor', 'Eureka! Why things float, levers and pi', c=True)
D('cai-lun', 'inv', 105, 'Court official and inventor', 'Paper, made from bark, hemp, rags and fishing nets')
D('marcus-aurelius', 'phil', 172, 'Emperor and Stoic philosopher', 'The Meditations, notes to himself on how to live', c=True)
D('augustine-of-hippo', 'phil', 397, 'Philosopher and bishop', 'The Confessions and The City of God')
D('aryabhata', 'math sci', 499, 'Mathematician and astronomer', 'The Aryabhatiya: pi as 3.1416, and a spinning Earth')

# ---- the middle ages
D('li-bai', 'art', 726, 'Poet', 'Quiet Night Thought, and poems of wine and the moon')
D('al-khwarizmi', 'math', 820, 'Mathematician', 'Algebra; his name gave us the word "algorithm"', c=True)
D('murasaki-shikibu', 'art', 1008, 'Novelist', 'The Tale of Genji, perhaps the first novel', c=True)
D('avicenna', 'sci phil', 1025, 'Physician and philosopher', 'The Canon of Medicine, used for 600 years')
D('maimonides', 'phil', 1190, 'Philosopher and physician', 'The Guide for the Perplexed')
D('rumi', 'art', 1260, 'Poet and mystic', 'The Masnavi, a masterpiece of Persian poetry', c=True)
D('thomas-aquinas', 'phil', 1265, 'Philosopher and theologian', 'The Summa Theologica: faith and reason together')
D('dante-alighieri', 'art', 1308, 'Poet', 'The Divine Comedy: Hell, Purgatory and Heaven', c=True)

# ---- the renaissance
D('filippo-brunelleschi', 'art inv', 1436, 'Architect and engineer', 'The dome of Florence Cathedral, and perspective')
D('johannes-gutenberg', 'inv', 1440, 'Goldsmith and inventor', 'The printing press with movable metal type', c=True)
D('sejong-the-great', 'inv', 1443, 'King and inventor', 'Hangul, the Korean alphabet')
D('sandro-botticelli', 'art', 1485, 'Painter', 'The Birth of Venus and Primavera', c=True)
D('leonardo-da-vinci', 'art inv', 1503, 'Painter and inventor', 'The Mona Lisa, The Last Supper and his notebooks')
D('michelangelo', 'art', 1504, 'Sculptor and painter', 'David and the Sistine Chapel ceiling')
D('raphael', 'art', 1511, 'Painter', 'The School of Athens')
D('niccolo-machiavelli', 'phil', 1513, 'Political thinker', 'The Prince, a rulebook for rulers')
D('nicolaus-copernicus', 'sci', 1543, 'Astronomer', 'On the Revolutions: the Sun at the centre')
D('mimar-sinan', 'art', 1557, 'Architect', 'The Süleymaniye and Selimiye mosques')
D('william-shakespeare', 'art', 1595, 'Playwright and poet', 'Romeo and Juliet, Hamlet and Macbeth')

# ---- the scientific revolution
D('miguel-de-cervantes', 'art', 1605, 'Novelist', 'Don Quixote')
D('johannes-kepler', 'sci', 1609, 'Astronomer', 'The laws of planetary motion')
D('galileo-galilei', 'sci', 1610, 'Astronomer and physicist', "Jupiter's moons, seen through his telescope")
D('rene-descartes', 'phil math', 1637, 'Philosopher and mathematician', '"I think, therefore I am", and coordinates')
D('rembrandt', 'art', 1642, 'Painter', 'The Night Watch')
D('johannes-vermeer', 'art', 1665, 'Painter', 'Girl with a Pearl Earring', c=True)
D('antonie-van-leeuwenhoek', 'sci', 1674, 'Cloth merchant and scientist', 'The first to see microbes, through his own lenses')
D('gottfried-wilhelm-leibniz', 'math phil', 1675, 'Mathematician and philosopher', 'Calculus, binary numbers and a calculating machine')
D('isaac-newton', 'sci math', 1687, 'Physicist and mathematician', 'The Principia: the laws of motion and gravity')
D('john-locke', 'phil', 1689, 'Philosopher', 'Natural rights to life, liberty and property')

# ---- the enlightenment
D('johann-sebastian-bach', 'art', 1721, 'Composer', 'The Brandenburg Concertos and the cello suites')
D('leonhard-euler', 'math', 1736, 'Mathematician', "The bridges of Königsberg, and Euler's formula")
D('benjamin-franklin', 'sci inv', 1752, 'Scientist and inventor', 'Lightning is electricity; the lightning rod')
D('voltaire', 'phil', 1759, 'Writer and philosopher', 'Candide, and the fight for free speech')
D('jean-jacques-rousseau', 'phil', 1762, 'Philosopher', 'The Social Contract')
D('james-watt', 'inv', 1765, 'Engineer and inventor', 'The separate condenser: steam power for factories')
D('johann-wolfgang-von-goethe', 'art', 1774, 'Writer and poet', 'The Sorrows of Young Werther, then Faust')
D('adam-smith', 'phil', 1776, 'Economist and philosopher', 'The Wealth of Nations')
D('antoine-lavoisier', 'sci', 1777, 'Chemist', 'Oxygen, and the birth of modern chemistry')
D('immanuel-kant', 'phil', 1781, 'Philosopher', 'The Critique of Pure Reason')
D('wolfgang-amadeus-mozart', 'art', 1787, 'Composer', 'Eine kleine Nachtmusik and The Magic Flute')

# ---- the 1800s
D('alexander-von-humboldt', 'sci', 1802, 'Naturalist and explorer', 'Nature seen as one connected web of life')
D('ludwig-van-beethoven', 'art', 1808, 'Composer', 'The Fifth and Ninth Symphonies')
D('michael-faraday', 'sci inv', 1831, 'Physicist and chemist', 'Electricity from magnetism, and the electric motor')
D('charles-dickens', 'art', 1838, 'Novelist', 'Oliver Twist and A Christmas Carol')
D('karl-marx', 'phil', 1848, 'Philosopher and economist', 'The Communist Manifesto and Capital')
D('florence-nightingale', 'sci', 1854, 'Nurse and statistician', 'Modern nursing, and charts that saved lives')
D('charles-darwin', 'sci', 1859, 'Naturalist', 'On the Origin of Species: evolution by natural selection')
D('victor-hugo', 'art', 1862, 'Novelist and poet', 'Les Misérables')
D('louis-pasteur', 'sci', 1862, 'Chemist and microbiologist', 'Germs cause disease; pasteurisation and vaccines')
D('gregor-mendel', 'sci', 1865, 'Monk and scientist', 'The laws of heredity, from pea plants')
D('leo-tolstoy', 'art', 1869, 'Novelist', 'War and Peace and Anna Karenina')
D('dmitri-mendeleev', 'sci', 1869, 'Chemist', 'The periodic table of the elements')
D('claude-monet', 'art', 1872, 'Painter', 'Impression, Sunrise, and the Water Lilies')
D('alexander-graham-bell', 'inv', 1876, 'Inventor', 'The telephone')
D('richard-wagner', 'art', 1876, 'Composer', 'The Ring of the Nibelung')
D('thomas-edison', 'inv', 1877, 'Inventor', 'The phonograph and the light bulb')
D('nikola-tesla', 'inv', 1882, 'Inventor and engineer', 'Alternating current and the induction motor')
D('vincent-van-gogh', 'art', 1889, 'Painter', 'The Starry Night and Sunflowers')
D('sigmund-freud', 'sci', 1896, 'Neurologist', 'Psychoanalysis, and The Interpretation of Dreams')
D('marie-curie', 'sci', 1898, 'Physicist and chemist', 'Radioactivity: polonium and radium')

# ---- the 1900s
D('wright-brothers', 'inv', 1903, 'Inventors and aviators', 'The first powered airplane flight')
D('albert-einstein', 'sci', 1905, 'Physicist', 'Relativity and E = mc²')
D('pablo-picasso', 'art', 1907, 'Painter and sculptor', 'Cubism and Guernica')
D('henry-ford', 'inv', 1908, 'Engineer and carmaker', 'The Model T and the moving assembly line')
D('rabindranath-tagore', 'art', 1913, 'Poet and songwriter', 'Gitanjali, and two national anthems')
D('alan-turing', 'math sci', 1936, 'Mathematician and codebreaker', 'The Turing machine, and breaking Enigma')
D('j-robert-oppenheimer', 'sci', 1945, 'Physicist', 'The first atomic bomb, and a warning to the world')
D('the-beatles', 'art', 1963, 'Rock band', 'I Want to Hold Your Hand, Sgt. Pepper, Abbey Road')
D('steve-jobs', 'inv', 1984, 'Co-founder of Apple', 'The Macintosh, then the iPhone')
D('tim-berners-lee', 'inv sci', 1989, 'Computer scientist', 'The World Wide Web, given away for free')

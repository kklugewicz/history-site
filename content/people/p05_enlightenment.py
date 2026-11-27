from _lib import P, R, G

FRA = ('France',)
BRIT = ('England and Ireland', 'United Kingdom', 'United Kingdom of Great Britain and Ireland')
RUS = ('Tsardom of Muscovy', 'Russian Empire')
AUS = ('Austrian Empire',)
OTT = ('Ottoman Empire',)
QING = ('Manchu Empire', 'Qing Empire')
USA = ('United States of America', 'United States')

# ---------- Europe 1640-1720 ----------
P('Oliver Cromwell', 'Lord Protector of England', (1599, 1658), 1, 'war rule',
  "Puritan cavalry general who won the English Civil War, had the king beheaded and ruled England as Lord Protector.",
  G(1644, 1645, 'Marston Moor and Naseby', 'york', (-1.29, 53.95), (-0.99, 52.41), 'london'),
  G(1649, 1650, 'Conquest of Ireland', 'london', 'dublin', (-6.35, 53.72), (-6.46, 52.34), 'london'),
  G(1650, 1651, 'Dunbar and Worcester', 'edinburgh', (-2.51, 56.0), (-2.22, 52.19), 'london'),
  R(1653, 1658, 'Lord Protector', *BRIT, at='london'))
P('Charles II of England', 'King of England, Scotland and Ireland', (1630, 1685), 3, 'rule',
  "The 'Merry Monarch', restored to the throne in 1660 after eleven years of exile.",
  R(1660, 1685, 'King of England, Scotland and Ireland', *BRIT, at='london'))
P('Rembrandt', 'Dutch painter', (1606, 1669), 2, 'art',
  'Painted The Night Watch and a lifetime of searching self-portraits in Amsterdam.',
  G(1631, 1669, 'Painter in Amsterdam', 'amsterdam'))
P('Johannes Vermeer', 'Dutch painter', (1632, 1675), 2, 'art',
  'Painted quiet rooms full of light, like Girl with a Pearl Earring, in Delft.',
  G(1653, 1675, 'Painter in Delft', 'delft'))
P('Diego Velázquez', 'Spanish painter', (1599, 1660), 3, 'art',
  'Court painter to Philip IV whose Las Meninas is one of the most studied paintings ever made.',
  G(1623, 1660, 'Court painter in Madrid', 'madrid'))
P('Gian Lorenzo Bernini', 'Italian sculptor and architect', (1598, 1680), 3, 'art',
  "Shaped baroque Rome: the colonnade of St Peter's Square and the Fountain of the Four Rivers.",
  G(1623, 1680, 'Sculptor and architect in Rome', 'rome'))
P('René Descartes', 'French philosopher and mathematician', (1596, 1650), 2, 'mind',
  "'I think, therefore I am': founder of modern philosophy and of coordinate geometry.",
  G(1628, 1649, 'Life in the Dutch Republic', 'amsterdam', 'leiden', 'utrecht'), G(1649, 1650, 'Tutor to Queen Christina', 'stockholm'))
P('Thomas Hobbes', 'English philosopher', (1588, 1679), 3, 'mind',
  "Wrote Leviathan: without a strong state, life is 'nasty, brutish and short'.",
  G(1640, 1651, 'Exile in Paris', 'paris'), G(1652, 1679, 'England', 'london'))
P('Louis XIV', 'King of France', (1638, 1715), 1, 'rule',
  "The Sun King: ruled for 72 years, built Versailles and fought Europe in four great wars.",
  R(1661, 1715, 'King of France', *FRA, at='versailles'))
P('Jean-Baptiste Colbert', 'French finance minister', (1619, 1683), 3, 'rule reform',
  "Louis XIV's minister who built France's navy, roads, canals and royal factories.",
  G(1661, 1683, 'Controller-general of finances', 'paris', 'versailles'))
P('Molière', 'French playwright', (1622, 1673), 3, 'art',
  "Wrote Tartuffe and The Miser and mocked hypocrites at Louis XIV's court.",
  G(1658, 1673, 'Playwright in Paris', 'paris'))
P('Blaise Pascal', 'French mathematician and philosopher', (1623, 1662), 3, 'mind faith',
  'Built a calculating machine, founded probability theory and wrote the Pensées.',
  G(1647, 1662, 'Paris', 'paris'))
P('Baruch Spinoza', 'Dutch philosopher', (1632, 1677), 3, 'mind',
  'Lens grinder expelled from his synagogue who argued that God and nature are one.',
  G(1656, 1677, 'Amsterdam and The Hague', 'amsterdam', 'the_hague'))
P('John Locke', 'English philosopher', (1632, 1704), 2, 'mind',
  'Argued that people have natural rights to life, liberty and property, ideas built into the American Revolution.',
  G(1683, 1689, 'Exile in the Dutch Republic', 'amsterdam', 'rotterdam'), G(1689, 1704, 'England', 'london'))
P('Isaac Newton', 'English mathematician and physicist', (1643, 1727), 1, 'mind',
  'Discovered the laws of motion and gravity, split white light into colours and invented calculus.',
  G(1661, 1696, 'Cambridge: the Principia', 'cambridge'), G(1696, 1727, 'Master of the Mint in London', 'london'))
P('Gottfried Wilhelm Leibniz', 'German philosopher and mathematician', (1646, 1716), 2, 'mind',
  'Invented calculus at the same time as Newton, and binary numbers too.',
  G(1672, 1676, 'Paris', 'paris'), G(1676, 1716, 'Hanover', 'hanover'))
P('Antonie van Leeuwenhoek', 'Dutch scientist', (1632, 1723), 2, 'mind',
  'First person to see bacteria, through microscopes he ground himself.',
  G(1673, 1723, 'Microscopes at Delft', 'delft'))
P('Christopher Wren', 'English architect', (1632, 1723), 3, 'art mind',
  "Rebuilt London after the Great Fire of 1666, crowned by St Paul's Cathedral.",
  G(1666, 1723, "Rebuilds London and St Paul's", 'london'))
P('William III of England', 'Stadtholder and king', (1650, 1702), 2, 'rule war',
  "Dutch prince who invaded England in the Glorious Revolution of 1688 and won the Battle of the Boyne.",
  R(1672, 1688, 'Stadtholder of Holland', 'Dutch Republic', at='the_hague'),
  G(1688, 1688, 'The Glorious Revolution', 'the_hague', (-3.53, 50.45), 'london'),
  G(1690, 1690, 'Battle of the Boyne', 'london', 'dublin', (-6.42, 53.72)),
  R(1691, 1702, 'King of England, Scotland and Ireland', *BRIT, at='london'))
P('John III Sobieski', 'King of Poland', (1629, 1696), 3, 'rule war',
  "Led the charge of the winged hussars that broke the Ottoman siege of Vienna in 1683.",
  G(1683, 1683, 'Relief of Vienna', 'warsaw', 'krakow', 'vienna', 'krakow'),
  R(1674, 1696, 'King of Poland', 'Polish–Lithuanian Commonwealth', at='warsaw'))
P('Kara Mustafa Pasha', 'Ottoman grand vizier', (1634, 1683), 3, 'war',
  "Led the great Ottoman siege of Vienna in 1683; after its failure he was strangled on the sultan's orders.",
  G(1683, 1683, 'Siege of Vienna', 'edirne', 'belgrade', 'vienna', 'belgrade'))
P('Prince Eugene of Savoy', 'Habsburg general', (1663, 1736), 3, 'war',
  'Beat the Ottomans at Zenta and Belgrade and the French, with Marlborough, at Blenheim.',
  G(1697, 1697, 'Battle of Zenta', 'vienna', (20.26, 45.93)), G(1704, 1709, 'War of the Spanish Succession', 'vienna', (10.63, 48.63), 'turin', (3.6, 50.85), (3.85, 50.28)),
  G(1717, 1717, 'Taking of Belgrade', 'vienna', 'belgrade'))
P('John Churchill, 1st Duke of Marlborough', 'English general', (1650, 1722), 3, 'war',
  'Never lost a battle; his victory at Blenheim in 1704 stopped Louis XIV.',
  G(1702, 1711, 'War of the Spanish Succession', 'the_hague', (6.08, 50.78), (10.63, 48.63), (4.95, 50.65), (3.6, 50.85), (3.85, 50.28)))
P('Stenka Razin', 'Cossack rebel', (1630, 1671), 3, 'war',
  'Led a great Cossack and peasant revolt up the Volga before being executed in Moscow.',
  G(1667, 1671, 'Revolt on the Volga', (44.5, 48.7), 'astrakhan', (46.0, 51.5), (48.4, 54.3), 'moscow'))
P('Peter the Great', 'Tsar and first emperor of Russia', (1672, 1725), 1, 'rule reform',
  "Travelled Europe in disguise to learn shipbuilding, beat Sweden and built St Petersburg as Russia's window on the West.",
  G(1697, 1698, 'The Grand Embassy', ('moscow', 1697.2), ('riga', 1697.3), ((20.51, 54.71, 1697.4)), ('amsterdam', 1697.65), ('london', 1698.1),
    ('amsterdam', 1698.3), ('vienna', 1698.5), ('moscow', 1698.7)),
  G(1709, 1709, 'Battle of Poltava', 'moscow', 'poltava'),
  R(1682, 1725, 'Tsar of Russia', *RUS, at='st_petersburg'))
P('Charles XII of Sweden', 'King of Sweden', (1682, 1718), 2, 'rule war',
  'Warrior king who beat Russia, Poland and Denmark at once until Peter the Great crushed him at Poltava.',
  G(1700, 1709, 'Great Northern War', ('stockholm', 1700.3), ((12.57, 55.68, 1700.6)), ((28.19, 59.38, 1700.88)), ('riga', 1701.5), ('warsaw', 1702.4),
    ('krakow', 1702.6), ((17.03, 51.11, 1704.5)), ('warsaw', 1705.5), ((12.3, 51.3, 1706.7)), ((27.56, 53.9, 1708.4)), ((33.0, 51.5, 1708.9)), ('poltava', 1709.5)),
  G(1709, 1714, 'Exile in the Ottoman Empire', ((29.48, 46.83)),),
  G(1718, 1718, 'Killed at Fredriksten', (11.39, 59.12)),
  R(1697, 1718, 'King of Sweden', 'Sweden', at='stockholm'))
P('Aurangzeb', 'Mughal emperor', (1618, 1707), 1, 'rule war',
  'Took the throne from his father Shah Jahan and pushed the Mughal Empire to its widest, but his wars in the Deccan drained it.',
  G(1681, 1707, 'Wars in the Deccan', (75.34, 19.88), (75.71, 16.83), (78.4, 17.38), (74.74, 19.09)),
  R(1658, 1707, 'Mughal emperor', 'Mughal Empire', at='delhi'))
P('Shivaji', 'Founder of the Maratha kingdom', (1630, 1680), 2, 'rule war',
  'Mountain-fort guerrilla who carved a Hindu Maratha kingdom out of the Mughal Deccan.',
  G(1645, 1665, 'Wars from the hill forts', 'pune', (73.68, 18.25), (73.44, 18.23)),
  G(1666, 1666, 'Escape from Agra', 'agra', (73.44, 18.23)),
  G(1674, 1680, 'Crowned Chhatrapati at Raigad', (73.44, 18.23)))
P('Kangxi Emperor', 'Emperor of Qing China', (1654, 1722), 2, 'rule',
  "China's longest-reigning emperor: took Taiwan, beat the Dzungars and made the Qing secure.",
  R(1661, 1722, 'Emperor of Qing China', *QING, at='beijing'))
P('Koxinga', 'Ming loyalist commander', (1624, 1662), 3, 'war',
  'Fought on for the fallen Ming and drove the Dutch out of Taiwan in 1662.',
  G(1646, 1662, 'Ming loyalist war and Taiwan', (118.09, 24.48), ('nanjing', 1659.6), (118.09, 24.48), (120.2, 23.0)))
P('Matsuo Bashō', 'Japanese poet', (1644, 1694), 3, 'art',
  'Master of haiku; walked the north of Japan for The Narrow Road to the Deep North.',
  G(1684, 1688, 'Edo', 'edo'),
  G(1689, 1689, 'The Narrow Road to the Deep North', ('edo', 1689.25), ((140.87, 38.27, 1689.4)), ((141.13, 38.99, 1689.45)), ((139.84, 38.9, 1689.55)),
    ((139.03, 37.92, 1689.6)), ((136.65, 36.56, 1689.7)), ((136.62, 35.36, 1689.8))))
P('Moulay Ismail', 'Sultan of Morocco', (1645, 1727), 3, 'rule',
  "The 'Warrior King' who ruled Morocco for 55 years from his vast palace city at Meknes.",
  R(1672, 1727, 'Sultan of Morocco', 'Morocco', at='meknes'))
P('Osei Tutu', 'Founder of the Asante Empire', (1660, 1717), 3, 'rule',
  'United the Akan states around the Golden Stool, the soul of the Asante nation.',
  G(1701, 1717, 'Asantehene at Kumasi', 'kumasi'))
P('Popé', 'Leader of the Pueblo Revolt', (1630, 1688), 3, 'war faith',
  'Tewa religious leader who drove the Spanish out of New Mexico in 1680.',
  G(1680, 1688, 'Pueblo Revolt', (-105.57, 36.41), 'santa_fe'))
P('Metacom', 'Wampanoag sachem', (1638, 1676), 3, 'war',
  "Called King Philip by the English: led the last great war of the New England peoples against the colonists.",
  G(1675, 1676, "King Philip's War", (-71.27, 41.67), (-72.6, 42.1), (-71.6, 42.4), (-71.27, 41.67)))

# ---------- The eighteenth century ----------
P('Johann Sebastian Bach', 'German composer', (1685, 1750), 2, 'art faith',
  'Wrote the St Matthew Passion and the Brandenburg Concertos, the summit of baroque music.',
  G(1708, 1717, 'Weimar', 'weimar'), G(1723, 1750, 'Cantor at Leipzig', 'leipzig'))
P('George Frideric Handel', 'German-British composer', (1685, 1759), 3, 'art',
  'Wrote Messiah and the Water Music in London.',
  G(1712, 1759, 'Composer in London', 'london'))
P('Voltaire', 'French writer and philosopher', (1694, 1778), 2, 'mind',
  "Wit of the Enlightenment who mocked tyranny and the Church in Candide; 'Crush the infamous thing!'",
  G(1726, 1728, 'Exile in England', 'london'), G(1734, 1749, 'Cirey', (4.93, 48.43)), G(1750, 1753, 'Guest of Frederick the Great', 'potsdam'),
  G(1755, 1778, 'Geneva and Ferney', 'geneva', (6.11, 46.26), 'paris'))
P('Montesquieu', 'French political philosopher', (1689, 1755), 3, 'mind',
  'Argued for separating the powers of government, a basis of the US Constitution.',
  G(1721, 1755, 'Bordeaux and Paris', 'bordeaux', 'paris'))
P('Jean-Jacques Rousseau', 'Genevan philosopher', (1712, 1778), 2, 'mind',
  "'Man is born free, and everywhere he is in chains': The Social Contract inspired the French Revolution.",
  G(1742, 1762, 'Paris', 'paris'), G(1762, 1767, 'Flight to Switzerland and England', (6.65, 46.9), 'london'), G(1770, 1778, 'Paris', 'paris'))
P('Denis Diderot', 'French philosopher', (1713, 1784), 3, 'mind',
  'Edited the Encyclopédie, which tried to gather all human knowledge in 28 volumes.',
  G(1747, 1772, 'The Encyclopédie in Paris', 'paris'), G(1773, 1774, 'Guest of Catherine the Great', 'st_petersburg'))
P('Carl Linnaeus', 'Swedish botanist', (1707, 1778), 3, 'mind',
  'Gave every plant and animal a two-part Latin name, like Homo sapiens.',
  G(1741, 1778, 'Professor at Uppsala', 'uppsala'))
P('Leonhard Euler', 'Swiss mathematician', (1707, 1783), 2, 'mind',
  'The most prolific mathematician ever: founded graph theory, found the formula behind e^iπ + 1 = 0 and gave maths the symbols e, i and f(x).',
  G(1720, 1727, 'Student of Johann Bernoulli in Basel', 'basel'), G(1727, 1741, 'Academy of Sciences in St Petersburg', 'st_petersburg'),
  G(1741, 1766, "Frederick the Great's Academy in Berlin", 'berlin'), G(1766, 1783, 'Back in St Petersburg, nearly blind', 'st_petersburg'))
P('Frederick the Great', 'King of Prussia', (1712, 1786), 1, 'rule war',
  'Flute-playing philosopher king and brilliant general who made Prussia a great power.',
  R(1740, 1786, 'King of Prussia', 'Prussia', at='potsdam'))
P('Maria Theresa', 'Habsburg empress', (1717, 1780), 2, 'rule reform',
  'Fought off Prussia and half of Europe to keep her inheritance, and reformed schools and the army; mother of 16.',
  R(1740, 1780, 'Ruler of the Habsburg lands', *AUS, at='vienna'))
P('Joseph II', 'Holy Roman Emperor', (1741, 1790), 3, 'rule reform',
  'Enlightened despot who freed the serfs and tolerated Protestants and Jews.',
  R(1780, 1790, 'Holy Roman Emperor', *AUS, at='vienna'), wiki='Joseph II, Holy Roman Emperor')
P('Nader Shah', 'Shah of Iran', (1688, 1747), 2, 'rule war',
  'Shepherd turned conqueror who sacked Delhi in 1739 and carried off the Peacock Throne.',
  G(1738, 1739, 'Invasion of India', 'kandahar', 'kabul', 'lahore', (76.98, 29.69), ('delhi', 1739.25), 'mashhad'),
  R(1736, 1747, 'Shah of Iran', 'Safavid Empire', 'Persia', at='mashhad'))
P('Ahmad Shah Durrani', 'Founder of Afghanistan', (1722, 1772), 3, 'rule war',
  'Built the Durrani Empire, modern Afghanistan, and crushed the Marathas at Panipat in 1761.',
  G(1747, 1760, 'Founder of the Durrani Empire', 'kandahar', 'kabul', 'lahore', 'delhi', 'kandahar'),
  G(1761, 1761, 'Third Battle of Panipat', 'kandahar', 'lahore', 'panipat'),
  G(1762, 1772, 'Shah at Kandahar', 'kandahar'))
P('Baji Rao I', 'Maratha peshwa', (1700, 1740), 3, 'war',
  'Never lost a battle; spread Maratha power across central India to the gates of Delhi.',
  G(1720, 1740, 'Maratha expansion', 'pune', (75.86, 22.72), (77.4, 23.26), ('delhi', 1737.3), 'pune'))
P('Robert Clive', 'British commander in India', (1725, 1774), 3, 'war',
  'East India Company clerk turned general whose victory at Plassey in 1757 began British rule in India.',
  G(1751, 1753, 'Siege of Arcot', 'madras', (79.42, 12.9)), G(1756, 1760, 'Plassey and Bengal', 'madras', 'calcutta', 'plassey', 'calcutta'))
P('Tipu Sultan', 'Sultan of Mysore', (1751, 1799), 3, 'rule war',
  "The 'Tiger of Mysore', who fought the British with rockets and died defending his capital.",
  R(1782, 1799, 'Sultan of Mysore', 'Mysore', at='seringapatam'))
P('Qianlong Emperor', 'Emperor of Qing China', (1711, 1799), 2, 'rule',
  'Ruled China at its largest and richest, and told Britain it had nothing China needed.',
  R(1735, 1796, 'Emperor of Qing China', *QING, at='beijing'))
P('Catherine the Great', 'Empress of Russia', (1729, 1796), 1, 'rule',
  'German princess who overthrew her husband, took Crimea and much of Poland, and wrote to Voltaire.',
  R(1762, 1796, 'Empress of Russia', *RUS, at='st_petersburg'))
P('Yemelyan Pugachev', 'Cossack rebel', (1742, 1775), 3, 'war',
  "Claimed to be the dead tsar and led Russia's largest peasant revolt.",
  G(1773, 1775, "Pugachev's Rebellion", (51.37, 51.23), (55.1, 51.77), (56.25, 58.0), 'kazan', (45.0, 48.7), 'moscow'))
P('Alexander Suvorov', 'Russian general', (1730, 1800), 3, 'war',
  'Never lost a battle: stormed Izmail, took Warsaw and crossed the Alps against the French.',
  G(1789, 1799, 'Campaigns', (28.84, 45.35), ('warsaw', 1794.85), ('milan', 1799.3), (8.59, 46.56)))
P('Vitus Bering', 'Danish explorer for Russia', (1681, 1741), 3, 'explore',
  'Crossed Siberia to explore the strait between Asia and America that bears his name.',
  G(1725, 1741, 'Kamchatka expeditions', ('st_petersburg', 1725.1), ('tobolsk', 1725.6), ((104.3, 52.3, 1726)), ((143.2, 59.4, 1727)),
    ((158.65, 53.02, 1728.4)), ((-169.0, 65.8, 1728.6)), ((158.65, 53.02, 1741.4)), ((-147.0, 59.9, 1741.55)), ((166.2, 55.0, 1741.9))))
P('Mikhail Lomonosov', 'Russian scientist', (1711, 1765), 3, 'mind',
  'Fisherman\'s son from the White Sea who became Russia\'s first great scientist and founded Moscow University.',
  G(1736, 1741, 'Studies in Germany', (8.77, 50.81)), G(1741, 1765, 'St Petersburg', 'st_petersburg'))
P('Charles Edward Stuart', 'Jacobite prince', (1720, 1788), 3, 'war',
  "'Bonnie Prince Charlie', whose rising to regain the British throne ended at Culloden.",
  G(1745, 1746, 'The Jacobite rising', ((-5.43, 56.87, 1745.62)), ('edinburgh', 1745.7), ((-1.48, 52.92, 1745.92)), ((-4.22, 55.86, 1745.99)),
    ((-4.07, 57.48, 1746.3)), ((-6.3, 57.4, 1746.5)), ((-5.43, 56.87, 1746.7))))
P('Marquis of Pombal', 'Chief minister of Portugal', (1699, 1782), 3, 'rule reform',
  'Rebuilt Lisbon after the great earthquake of 1755 and expelled the Jesuits.',
  G(1750, 1777, 'Chief minister in Lisbon', 'lisbon'))
P('Muhammad ibn Abd al-Wahhab', 'Islamic reformer', (1703, 1792), 3, 'faith',
  'Preached a strict return to early Islam and allied with the House of Saud, founding the first Saudi state.',
  G(1744, 1792, 'Alliance with the Saud family at Diriyah', (46.57, 24.73)))
P('Taksin', 'King of Thonburi', (1734, 1782), 3, 'rule war',
  'Rallied Siam after the Burmese destroyed Ayutthaya in 1767 and made Thonburi the new capital.',
  G(1767, 1782, 'King of Thonburi', (100.49, 13.73)))
P('Alaungpaya', 'King of Burma', (1714, 1760), 3, 'rule war',
  'Village chief who reunited Burma and founded the Konbaung dynasty.',
  G(1752, 1760, 'Unifier of Burma', (95.7, 22.57), (96.15, 16.87), ('ayutthaya', 1760.3)))
P('Carlos III of Spain', 'King of Spain', (1716, 1788), 3, 'rule reform',
  'Enlightened king who modernised Madrid and Spanish America.',
  R(1759, 1788, 'King of Spain', 'Spain', at='madrid'), wiki='Charles III of Spain')

# ---------- Exploration of the Pacific ----------
P('James Cook', 'British explorer', (1728, 1779), 1, 'explore',
  'Charted New Zealand and eastern Australia, crossed the Antarctic Circle and was killed in Hawaii.',
  G(1768, 1771, 'First voyage', ('plymouth', 1768.65), ((-16.9, 32.65, 1768.72)), ('rio', 1768.9), ((-67.3, -55.98, 1769.05)), ('tahiti', 1769.3),
    ((178.0, -38.7, 1769.8)), ((174.8, -41.3, 1770.1)), ((151.2, -34.0, 1770.32)), ((145.25, -15.46, 1770.5)), ('batavia', 1770.8),
    ('cape_town', 1771.25), ((-0.13, 51.4, 1771.54))),
  G(1772, 1775, 'Second voyage: the Antarctic Circle', ('plymouth', 1772.53), ('cape_town', 1772.83), ((39.6, -66.5, 1773.05)), ((166.9, -45.8, 1773.25)),
    ('tahiti', 1773.65), ('tonga', 1773.8), ((174.8, -41.3, 1773.9)), ((-106.9, -71.17, 1774.08)), ((-109.35, -27.12, 1774.2)), ((-139.5, -9.0, 1774.3)),
    ('tahiti', 1774.4), ((168.3, -17.7, 1774.62)), ((165.5, -21.0, 1774.72)), ((174.8, -41.3, 1774.8)), ((-67.3, -55.98, 1774.98)),
    ((-36.5, -54.3, 1775.05)), ('cape_town', 1775.25), ('plymouth', 1775.58)),
  G(1776, 1779, 'Third voyage: Hawaii and Alaska', ('plymouth', 1776.53), ('cape_town', 1776.8), ((69.5, -49.3, 1776.98)), ((147.3, -43.1, 1777.07)),
    ((174.8, -41.3, 1777.15)), ('tonga', 1777.4), ('tahiti', 1777.65), ((-159.6, 21.96, 1778.05)), ((-126.6, 49.6, 1778.25)), ((-151.0, 60.0, 1778.45)),
    ((-168.0, 65.6, 1778.62)), ((-156.0, 20.8, 1778.9)), ((-155.93, 19.48, 1779.12))))
P('Louis Antoine de Bougainville', 'French explorer', (1729, 1811), 3, 'explore',
  'Led the first French voyage round the world, with the botanist who named the bougainvillea.',
  G(1766, 1769, 'Voyage round the world', ((-2.2, 47.27, 1766.9)), ('montevideo', 1767.1), ('rio', 1767.5), ('strait_magellan', 1767.95), ('tahiti', 1768.3),
    ('samoa', 1768.4), ((168.3, -15.5, 1768.45)), ((154.7, -6.2, 1768.55)), ('batavia', 1768.75), ((57.5, -20.2, 1768.9)), ((-4.49, 48.39, 1769.2))))
P('Junípero Serra', 'Spanish missionary', (1713, 1784), 3, 'faith explore',
  'Founded the first Spanish missions in California, from San Diego to San Francisco.',
  G(1769, 1784, 'Missions of California', 'mexico_city', (-117.16, 32.72), (-121.92, 36.54), (-122.42, 37.76), (-121.92, 36.54)))

# ---------- Revolutions in America and France ----------
P('Benjamin Franklin', 'American statesman and scientist', (1706, 1790), 2, 'mind rule',
  'Printer who flew a kite in a thunderstorm, helped write the Declaration of Independence and won France as an ally.',
  G(1723, 1756, 'Printer in Philadelphia', 'philadelphia'), G(1757, 1775, 'Agent in London', 'london'),
  G(1776, 1785, 'Envoy to France', 'paris'), G(1785, 1790, 'Philadelphia', 'philadelphia'))
P('Pontiac', 'Odawa war leader', (1714, 1769), 3, 'war',
  "Led a great alliance of nations of the Great Lakes against the British in Pontiac's War.",
  G(1763, 1766, "Pontiac's War", (-83.05, 42.33), (-84.73, 45.78), (-80.0, 40.44), (-83.05, 42.33)))
P('George Washington', 'First President of the United States', (1732, 1799), 1, 'war rule',
  'Commanded the Continental Army through eight years of war, then refused to be king and served two terms as president.',
  G(1754, 1758, 'French and Indian War', (-79.7, 39.81), (-80.0, 40.44), 'mount_vernon'),
  G(1775, 1783, 'Commander of the Continental Army', ('boston', 1775.55), ('boston', 1776.2), ('new_york', 1776.6), ((-74.76, 40.22, 1776.98)),
    ((-75.61, 39.91, 1777.7)), ('valley_forge', 1777.97), ((-74.32, 40.27, 1778.5)), ((-73.95, 41.39, 1779.5)), ('yorktown', 1781.8), ((-74.01, 41.5, 1782.5)),
    ('mount_vernon', 1783.97)),
  R(1789, 1797, 'President of the United States', *USA, at='philadelphia'))
P('Thomas Jefferson', 'Third President of the United States', (1743, 1826), 2, 'rule mind',
  "Wrote the Declaration of Independence and doubled the country's size with the Louisiana Purchase.",
  G(1776, 1776, 'Writes the Declaration of Independence', 'philadelphia'), G(1784, 1789, 'Minister to France', 'paris'),
  R(1801, 1809, 'President of the United States', *USA, at='washington'))
P('John Adams', 'Second President of the United States', (1735, 1826), 3, 'rule',
  'Argued the case for independence in Congress and was the second president.',
  R(1797, 1801, 'President of the United States', *USA, at='philadelphia'))
P('Alexander Hamilton', 'American statesman', (1755, 1804), 3, 'rule',
  "Washington's aide and first Treasury secretary who built America's finances; killed in a duel.",
  G(1777, 1781, "Washington's aide-de-camp", 'valley_forge', 'yorktown'), G(1789, 1795, 'First Treasury secretary', 'new_york', 'philadelphia'),
  G(1796, 1804, 'New York', 'new_york'))
P('Marquis de Lafayette', 'French general', (1757, 1834), 3, 'war',
  "Fought for American independence at 19, then led the National Guard in the French Revolution.",
  G(1777, 1781, 'American Revolutionary War', 'philadelphia', 'valley_forge', 'yorktown'), G(1789, 1792, 'Commander of the National Guard', 'paris'))
P('George III', 'King of Great Britain', (1738, 1820), 2, 'rule',
  'Lost the American colonies; reigned for 60 years through the wars with revolutionary France.',
  R(1760, 1820, 'King of Great Britain', *BRIT, at='london'), wiki='George III')
P('Louis XVI', 'King of France', (1754, 1793), 2, 'rule',
  'Last king of the old regime, guillotined by the Revolution in 1793.',
  R(1774, 1791, 'King of France', *FRA, at='versailles'), G(1791, 1791, 'Flight to Varennes', 'paris', (5.03, 49.23), 'paris'),
  G(1792, 1793, 'Prisoner of the Revolution', 'paris'))
P('Marie Antoinette', 'Queen of France', (1755, 1793), 3, 'rule',
  'Austrian-born queen hated for her extravagance and guillotined in 1793.',
  G(1770, 1789, 'Queen at Versailles', 'vienna', 'versailles'), G(1789, 1793, 'Prisoner in Paris', 'paris'))
P('Maximilien Robespierre', 'French revolutionary', (1758, 1794), 2, 'rule reform',
  'Led the Committee of Public Safety through the Reign of Terror and was guillotined himself.',
  G(1789, 1794, 'Leader of the Revolution in Paris', 'versailles', 'paris'))
P('Georges Danton', 'French revolutionary', (1759, 1794), 3, 'rule',
  'Fiery orator who rallied France against invasion in 1792, then fell to Robespierre.',
  G(1789, 1794, 'Paris', 'paris'))
P('Antoine Lavoisier', 'French chemist', (1743, 1794), 2, 'mind',
  'Father of modern chemistry who named oxygen, and was guillotined in the Terror.',
  G(1768, 1794, 'Paris', 'paris'))
P('James Watt', 'Scottish engineer', (1736, 1819), 2, 'mind',
  "His improved steam engine powered the Industrial Revolution; the watt is named after him.",
  G(1764, 1773, 'Glasgow', 'glasgow'), G(1774, 1819, 'Steam engines at Birmingham', 'birmingham'))
P('Adam Smith', 'Scottish economist', (1723, 1790), 2, 'mind',
  'Wrote The Wealth of Nations: free markets and the division of labour make countries rich.',
  G(1751, 1763, 'Professor at Glasgow', 'glasgow'), G(1764, 1766, 'Tour of France', 'paris', 'geneva'), G(1778, 1790, 'Edinburgh', 'edinburgh'))
P('Immanuel Kant', 'German philosopher', (1724, 1804), 2, 'mind',
  "Never left Königsberg, but his Critique of Pure Reason changed philosophy forever.",
  G(1740, 1804, 'Königsberg', (20.51, 54.71)))
P('Wolfgang Amadeus Mozart', 'Austrian composer', (1756, 1791), 1, 'art',
  'Child prodigy who wrote over 600 works, from The Magic Flute to the Requiem, before dying at 35.',
  G(1762, 1773, 'Child prodigy on tour', ('salzburg', 1762.9), ('munich', 1763.5), ('paris', 1763.9), ('london', 1764.4), ('amsterdam', 1765.8),
    ('paris', 1766.3), ('salzburg', 1766.9), ('vienna', 1767.8), ('salzburg', 1769), ('milan', 1770.1), ('rome', 1770.3), ('naples', 1770.4),
    ('milan', 1770.9), ('salzburg', 1773)),
  G(1781, 1791, 'Vienna', 'vienna'))
P('Tupac Amaru II', 'Leader of an Andean revolt', (1738, 1781), 3, 'war',
  'Descendant of the last Inca emperor who led a huge rising against Spanish rule in Peru.',
  G(1780, 1781, 'The Great Rebellion', (-71.4, -14.2), (-71.6, -14.0), 'cuzco'))
P('Toussaint Louverture', 'Leader of the Haitian Revolution', (1743, 1803), 2, 'war rule',
  'Former slave who led the only slave revolt that created a nation, and beat French, Spanish and British armies.',
  G(1791, 1802, 'The Haitian Revolution', 'cap_haitien', (-72.69, 19.45), 'port_au_prince', 'santo_domingo', 'cap_haitien'),
  G(1802, 1803, 'Prisoner in France', (6.37, 46.88)))
P('Agha Mohammad Khan Qajar', 'Shah of Iran', (1742, 1797), 3, 'rule war',
  'Reunited Iran, made Tehran the capital and founded the Qajar dynasty.',
  R(1789, 1797, 'Shah of Iran', 'Persia', at='tehran'))
P('Selim III', 'Ottoman sultan', (1761, 1808), 3, 'rule reform',
  'Tried to build a modern army and was overthrown and killed by the Janissaries.',
  R(1789, 1807, 'Ottoman sultan', *OTT, at='constantinople'))
P('Nguyễn Huệ', 'Emperor of Vietnam', (1753, 1792), 3, 'rule war',
  'Tây Sơn rebel leader who routed a Qing invasion at Đống Đa in 1789.',
  G(1771, 1788, 'Tây Sơn rebellion', (108.9, 13.95), 'hue', (106.0, 10.5), 'hue'), G(1789, 1789, 'Battle of Đống Đa', 'hue', 'thang_long'),
  G(1789, 1792, 'Emperor Quang Trung', 'hue'))

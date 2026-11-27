"""Migrations of the early modern age: expulsions from Spain, the Atlantic slave trade, European settlers in the Americas,
the Oromo, Russians into Siberia, the Kalmyks, the Huguenots, the Mfecane, the Great Trek and the Trail of Tears."""
from _lib import M, S, mv, site

M('spain-expulsions', 'The expulsions from Spain', 'Sephardic Jews', 'exiles', '#7d3c98', 1492, 1614,
  'In 1492 Ferdinand and Isabella ordered every Jew in Spain to convert or leave. Perhaps 100,000 or more left, to Portugal '
  '(which forced them to convert in 1497), to North Africa, Italy and above all the Ottoman Empire, where Sultan Bayezid II '
  'welcomed them. Their descendants, the Sephardim, kept their Spanish, Ladino, for 500 years. Between 1609 and 1614 Spain '
  'also expelled some 300,000 Moriscos, descendants of its Muslims.',
  rank=1, steps=[
    S(1492, '1492 to 1500', 'The Alhambra Decree',
      'Jews had four months to sell what they could and go. Ships took them from Cadiz and Cartagena to Fez, Naples, '
      'Salonica and Constantinople; Salonica became a mostly Jewish city.',
      moves=[mv('sail', (-0.98, 37.55, 1492), (0.5, 37.6, 1492), (5.0, 37.9, 1492), (9.0, 38.0, 1492), (12.0, 37.3, 1492), (15.6, 36.6, 1493),
                (20.0, 36.2, 1493), (23.0, 36.0, 1493), (25.5, 37.3, 1493), (26.2, 39.0, 1493), (26.1, 40.0, 1493), (26.7, 40.4, 1493),
                (28.0, 40.8, 1493), (28.95, 41.0, 1493), label='To Constantinople'),
             mv('sail', (26.0, 39.6, 1493), (24.0, 40.0, 1493), (22.9, 40.6, 1493), label='To Salonica'),
             mv('sail', (-6.3, 36.5, 1492), (-5.9, 36.0, 1492), (-5.6, 35.5, 1492), label='To Morocco'),
             mv('foot', (-4.0, 40.0, 1492), (-7.0, 39.5, 1492), (-9.1, 38.7, 1492), label='To Portugal')],
      sites=[site('Granada', -3.6, 37.18, 1492, 'Where the decree was signed, three months after the city fell.'),
             site('Salonica', 22.94, 40.64, 1500, 'The "Jerusalem of the Balkans", home of the Sephardim until 1943.')]),
    S(1609, '1609 to 1614', 'The Moriscos',
      'Philip III expelled the Moriscos, Muslims forcibly converted a century before. From Valencia and Aragon ships carried '
      'them to Oran and Tunis; in Morocco some founded the corsair republic of Sale.',
      moves=[mv('sail', (-0.3, 39.45, 1609), (0.4, 38.5, 1609), (-0.3, 37.0, 1609), (-0.6, 35.8, 1609), label='Moriscos to Oran'),
             mv('sail', (0.4, 38.5, 1610), (5.0, 38.0, 1610), (9.0, 37.6, 1610), (10.3, 37.3, 1610), (10.5, 36.95, 1610), label='To Tunis'),
             mv('foot', (-5.9, 37.4, 1610), (-6.3, 36.5, 1610), label='From Seville'),
             mv('sail', (-6.3, 36.5, 1610), (-6.6, 35.5, 1610), (-6.82, 34.04, 1610), label='To Sale')],
      sites=[site('Valencia', -0.38, 39.47, 1609, 'A third of the kingdom\'s people were Moriscos.')]),
  ])

M('atlantic-slave-trade', 'The Atlantic slave trade', 'Enslaved Africans', 'forced', '#3b2a3f', 1501, 1866,
  'Over three and a half centuries some 12.5 million Africans were packed into ships and carried across the Atlantic; about '
  'two million died on the Middle Passage. Most were taken to work sugar, coffee and cotton in Brazil and the Caribbean; '
  'about 400,000 to North America. It was the largest forced migration in history, and it made the Americas, and Africa, '
  'what they are.',
  story='ev:atlantic-slave-trade', numbers='12.5 million people taken; 10.7 million survived the crossing', rank=1, steps=[
    S(1501, '1501 to 1580', 'The first crossings',
      'The first enslaved Africans reached Hispaniola in 1501 to replace the dying Taino. From the 1530s the trade grew with '
      'the sugar mills of Portuguese Brazil, fed from the Bight of Benin and the Kongo.',
      moves=[mv('sail', (-17.3, 14.7, 1501), (-25.0, 14.5, 1503), (-40.0, 14.5, 1506), (-55.0, 15.0, 1509), (-60.0, 17.5, 1511),
                (-64.5, 17.0, 1513), (-69.9, 18.3, 1515), label='To the Caribbean', until=1866),
             mv('sail', (2.1, 6.2, 1550), (-4.0, 2.0, 1552), (-18.0, -4.0, 1555), (-33.0, -11.0, 1558), (-38.4, -13.1, 1560), label='To Brazil', until=1851)],
      sites=[site('Elmina', -1.35, 5.08, 1501, 'Portuguese fortress of 1482 on the Gold Coast, later a great slave castle.'),
             site('Salvador da Bahia', -38.5, -12.97, 1560, 'Brazil\'s first capital, built on the sugar of the enslaved.')]),
    S(1575, '1575 to 1700', 'Angola, sugar and the islands',
      'From Luanda, founded in 1576, the Portuguese shipped millions from Angola and the Kongo to Rio and Bahia. In the 1600s '
      'the English, Dutch and French built sugar islands: Barbados, Jamaica and Saint-Domingue.',
      moves=[mv('sail', (13.0, -8.8, 1576), (5.0, -12.0, 1578), (-15.0, -18.0, 1582), (-35.0, -23.0, 1586), (-42.5, -23.3, 1589), (-43.15, -22.93, 1590), label='Angola to Rio', until=1851),
             mv('sail', (7.0, 4.2, 1650), (-8.0, 3.0, 1652), (-28.0, 8.0, 1655), (-50.0, 12.0, 1658), (-58.5, 13.1, 1660), (-61.3, 11.75, 1661),
                (-68.0, 14.5, 1663), (-76.8, 17.9, 1665), label='Biafra to Jamaica', until=1807)],
      sites=[site('Luanda', 13.23, -8.81, 1576, 'From here more Africans were shipped than from any other port.'),
             site('Barbados', -59.55, 13.1, 1650, 'The first great English sugar island.')]),
    S(1700, '1700 to 1807', 'The height of the trade',
      'In the 1700s over six million people were shipped, more than in all other centuries together. Ships from Liverpool, '
      'Nantes and Rhode Island carried them; rice and tobacco planters of Carolina and Virginia bought them in Charleston.',
      moves=[mv('sail', (-17.3, 14.7, 1700), (-30.0, 20.0, 1702), (-50.0, 26.0, 1705), (-70.0, 30.5, 1708), (-78.5, 32.2, 1710), (-79.9, 32.75, 1710), label='To Carolina', until=1808)],
      sites=[site('Charleston', -79.93, 32.78, 1710, 'Nearly half of all enslaved Africans brought to North America landed here.'),
             site('Saint-Domingue', -72.3, 19.0, 1780, 'The richest colony on earth, worked by half a million enslaved people, until the revolution of 1791.')]),
    S(1807, '1807 to 1866', 'Abolition',
      'Britain banned the trade in 1807 and the United States in 1808, and the Royal Navy hunted slave ships off Africa. '
      'Brazil stopped in 1850; the last known voyage reached Cuba in 1866. Slavery itself ended in Brazil only in 1888.',
      moves=[mv('sail', (13.0, -8.8, 1807), (5.0, -12.0, 1810), (-15.0, -18.0, 1815), (-35.0, -23.0, 1820), (-42.5, -23.3, 1824), (-43.15, -22.93, 1825), label='Angola to Rio', until=1851)],
      sites=[site('Freetown', -13.23, 8.48, 1808, 'Where the Royal Navy freed the Africans it took from slave ships.')]),
  ])

M('european-colonists', 'European settlers in the Americas', 'European settlers', 'settlers', '#1a5276', 1502, 1775,
  'In the three centuries after Columbus, perhaps two million Europeans crossed to the Americas: Spaniards to Mexico and '
  'Peru, Portuguese to Brazil, English and Scots to Virginia and New England, French to the St Lawrence, Dutch to the '
  'Hudson. Most early colonists were young men, many of them indentured servants; the English colonies drew whole families. '
  'They came with the diseases that killed most of the native peoples.',
  rank=1, steps=[
    S(1502, '1502 to 1600', 'Spain and Portugal',
      'From Seville, the only port allowed to trade with the Indies, some 250,000 Spaniards sailed in the 1500s, most to '
      'Mexico and Peru. Portuguese settled Brazil\'s sugar coast from the 1530s.',
      moves=[mv('sail', (-6.3, 36.6, 1502), (-11.0, 33.0, 1503), (-16.5, 28.0, 1504), (-35.0, 22.0, 1506), (-55.0, 17.5, 1508), (-61.3, 16.7, 1509),
                (-70.0, 16.5, 1511), (-76.5, 16.8, 1512), (-80.0, 18.5, 1514), (-84.5, 20.5, 1516), (-85.8, 21.7, 1517), (-89.0, 22.6, 1518), (-93.0, 20.5, 1519), (-96.1, 19.2, 1520), label='Spaniards', until=1700),
             mv('sail', (-9.2, 38.6, 1532), (-16.5, 28.5, 1533), (-24.0, 15.5, 1534), (-30.0, 0.0, 1535), (-34.0, -7.5, 1536), (-34.85, -8.05, 1537), label='Portuguese', until=1700)],
      sites=[site('Veracruz', -96.13, 19.2, 1519, 'Where Cortes landed and where the treasure fleets loaded silver.'),
             site('Olinda', -34.85, -8.0, 1537, 'Capital of Pernambuco, Brazil\'s first rich sugar colony.')]),
    S(1607, '1607 to 1640', 'Jamestown, Quebec and Plymouth',
      'The English founded Jamestown in 1607, the French Quebec in 1608, the Pilgrims Plymouth in 1620, and the Dutch New '
      'Amsterdam in 1625. In the Great Migration of the 1630s some 20,000 Puritans came to New England.',
      moves=[mv('sail', (-4.15, 50.3, 1620), (-5.0, 49.9, 1620), (-6.5, 49.7, 1620), (-10.0, 49.5, 1620), (-30.0, 46.0, 1620), (-50.0, 43.5, 1620), (-66.0, 42.0, 1620), (-70.0, 42.2, 1620), (-70.6, 41.95, 1620), label='Mayflower', until=1640),
             mv('sail', (-1.2, 46.1, 1608), (-10.0, 46.5, 1608), (-30.0, 47.0, 1608), (-50.0, 45.5, 1608), (-56.0, 46.3, 1608), (-58.5, 46.9, 1608), (-59.8, 47.3, 1608), (-62.0, 48.6, 1608),
                (-64.3, 49.05, 1608), (-66.0, 49.45, 1608), (-67.0, 49.2, 1608), (-69.6, 48.1, 1608), (-71.2, 46.8, 1608), label='French to Quebec', until=1700),
             mv('sail', (0.9, 51.45, 1607), (1.6, 51.1, 1607), (0.5, 50.6, 1607), (-3.0, 49.9, 1607), (-5.5, 49.6, 1607), (-11.0, 45.0, 1607), (-16.0, 28.0, 1607), (-45.0, 23.0, 1607), (-63.0, 25.0, 1607), (-75.5, 36.9, 1607), (-76.6, 37.2, 1607), label='English to Virginia', until=1700)],
      sites=[site('Jamestown', -76.78, 37.21, 1607, 'The first lasting English colony in America.'),
             site('Quebec', -71.21, 46.81, 1608, 'Founded by Samuel de Champlain.'),
             site('Plymouth', -70.67, 41.96, 1620, 'Founded by the Pilgrims of the Mayflower.')]),
    S(1700, '1700 to 1775', 'Germans, Scots and Irish',
      'In the 1700s new settlers poured into British America: Germans from the Palatinate to Pennsylvania, Scots and '
      'Ulster Scots to the back country. By 1775 the thirteen colonies held two and a half million people.',
      moves=[mv('sail', (-5.8, 54.7, 1718), (-5.6, 55.0, 1718), (-6.8, 55.4, 1718), (-8.5, 55.6, 1718), (-20.0, 54.0, 1719), (-45.0, 46.0, 1720), (-68.0, 40.5, 1721), (-74.8, 38.8, 1722), (-75.15, 39.95, 1722), label='Ulster Scots', until=1775),
             mv('sail', (4.1, 51.95, 1709), (1.8, 51.0, 1709), (-5.5, 49.6, 1709), (-20.0, 48.0, 1709), (-45.0, 44.0, 1710), (-68.0, 40.5, 1710), (-74.0, 40.6, 1710), label='Palatines', until=1775)],
      sites=[site('Philadelphia', -75.16, 39.95, 1722, 'The great port of entry for Germans and Ulster Scots.')]),
  ])

M('oromo', 'The Oromo migrations', 'Oromo', 'nomads', '#7e5109', 1522, 1618,
  'In the 1500s the Oromo, cattle-herding peoples of the southern Ethiopian highlands, moved north and east in great waves, '
  'organised by their gadaa system, in which a new generation of warriors took power every eight years. While the Christian '
  'empire and the Adal sultanate exhausted each other in war, the Oromo filled the lands between, and today they are the '
  'largest people of Ethiopia.',
  rank=2, steps=[
    S(1522, '1522 to 1570', 'Out of the south',
      'From their home around Mount Walabu in Bale, the Borana and Barentu Oromo moved into the lands emptied by the war '
      'between Ethiopia and Adal, toward Harar and the Awash.',
      moves=[mv('foot', (39.7, 6.3, 1522), (40.0, 7.5, 1530), (40.5, 8.5, 1546), (42.1, 9.3, 1567), label='Barentu Oromo'),
             mv('foot', (39.7, 6.3, 1522), (39.0, 7.5, 1540), (38.5, 8.5, 1560), label='Borana Oromo')],
      sites=[site('Harar', 42.12, 9.31, 1567, 'The walled city of the emirs of Adal, besieged by the Oromo.')]),
    S(1570, '1570 to 1618', 'To the heart of Ethiopia',
      'The Oromo spread over Shewa, Wollo and the west, reaching Gojjam and the Abay. The emperors could not stop them and '
      'moved their court north to Gondar.',
      moves=[mv('foot', (38.5, 8.5, 1570), (38.5, 10.0, 1585), (39.3, 11.3, 1600), (39.6, 12.0, 1618), label='To Wollo'),
             mv('foot', (38.5, 8.5, 1570), (37.0, 9.0, 1590), (36.5, 9.5, 1610), (37.5, 10.3, 1618), label='To the west')]),
  ])

M('siberia', 'The Russians cross Siberia', 'Russian settlers', 'settlers', '#2e86c1', 1582, 1700,
  'In 1582 the Cossack Yermak, hired by the Stroganov merchants, crossed the Urals and took the Tatar khanate of Sibir. In '
  'sixty years Cossacks and fur traders went 6,000 km east by river and portage to the Pacific, founding forts that became '
  'cities. Peasants, exiles and Old Believers followed them; by 1700 there were more Russians than natives in Siberia.',
  rank=1, steps=[
    S(1582, '1582 to 1620', 'Over the Urals',
      'Yermak\'s 840 men took Isker, the khan\'s capital, in 1582. Tobolsk was founded in 1587, Tomsk in 1604, Yeniseysk in '
      '1619: each a stockade on a river, collecting furs as tribute.',
      moves=[mv('river', (56.2, 58.0, 1582), (60.0, 58.5, 1582), (65.0, 58.0, 1582), (68.25, 58.2, 1587), (75.0, 58.0, 1595), (84.95, 56.5, 1604),
                (89.0, 57.5, 1612), (92.2, 58.45, 1619), label='Cossacks')],
      sites=[site('Tobolsk', 68.25, 58.2, 1587, 'First capital of Russian Siberia.')]),
    S(1620, '1620 to 1700', 'To the Pacific',
      'Cossacks reached the Lena and founded Yakutsk in 1632; Ivan Moskvitin reached the Sea of Okhotsk in 1639. Others went '
      'down the Amur until China stopped them, and in 1697 Vladimir Atlasov took Kamchatka.',
      moves=[mv('river', (92.2, 58.45, 1620), (100.0, 58.0, 1625), (108.0, 57.0, 1628), (115.0, 59.5, 1630), (122.0, 61.0, 1631), (129.7, 62.0, 1632),
                (135.0, 61.0, 1636), (141.0, 59.5, 1639), (143.2, 59.36, 1647), label='Cossacks'),
             mv('river', (129.7, 62.0, 1650), (126.0, 57.0, 1650), (124.2, 53.4, 1651), (127.5, 50.3, 1652), label='Khabarov to the Amur'),
             mv('foot', (143.2, 59.36, 1690), (155.0, 62.5, 1696), (160.0, 58.0, 1697), (158.65, 53.0, 1700), label='Atlasov to Kamchatka')],
      sites=[site('Yakutsk', 129.73, 62.03, 1632, 'Fort on the Lena; the fur capital of eastern Siberia.'),
             site('Okhotsk', 143.24, 59.36, 1647, 'The first Russian port on the Pacific.')]),
  ])

M('kalmyks', 'The Kalmyks\' long ride', 'Kalmyks', 'nomads', '#9a7d0a', 1608, 1771,
  'The Kalmyks, a Mongol people of the Oirat confederation, Buddhists, left Dzungaria early in the 1600s and rode 3,000 km '
  'west to the lower Volga, where they founded a khanate under the Russian tsars. In the winter of 1771, chafing under '
  'Russia, most of them, some 150,000 people, set out to ride home; harried by Kazakhs and Cossacks, fewer than half '
  'reached China.',
  rank=2, steps=[
    S(1608, '1608 to 1632', 'West to the Volga',
      'Pressed by their rivals among the Oirats and short of pasture, the Torghut Kalmyks under Kho Orluk crossed the Kazakh '
      'steppe and reached the Volga about 1630.',
      moves=[mv('horse', (85.0, 46.5, 1608), (78.0, 48.5, 1613), (70.0, 49.0, 1618), (61.0, 49.0, 1623), (54.0, 48.0, 1628), (46.5, 46.8, 1632), label='Kalmyks')],
      sites=[site('Kalmyk khanate', 46.0, 46.5, 1650, 'The only Buddhist state in Europe, on the steppe of the lower Volga.')]),
    S(1771, '1771', 'The flight east',
      'In January 1771 Khan Ubashi led 33,000 households east across the frozen steppe; the Kalmyks west of the unfrozen Volga '
      'were left behind. Those who reached Ili were resettled by the Qianlong emperor.',
      moves=[mv('horse', (46.5, 46.8, 1771), (52.0, 47.5, 1771), (60.0, 48.5, 1771), (70.0, 47.0, 1771), (78.0, 45.5, 1771), (81.5, 43.9, 1771), label='Kalmyks')],
      sites=[site('Ili', 81.3, 43.9, 1771, 'Where the survivors were received by the Qing.')]),
  ])

M('huguenots', 'The Huguenot refuge', 'Huguenots', 'exiles', '#2c3e50', 1685, 1700,
  'In 1685 Louis XIV revoked the Edict of Nantes and outlawed Protestantism in France. Though leaving was forbidden, some '
  '200,000 Huguenots escaped, to the Netherlands, England, Switzerland, Prussia and as far as the Cape of Good Hope. They '
  'took their skills with them: silk weaving to London, watchmaking to Geneva; a third of Berlin was French by 1700.',
  rank=2, steps=[
    S(1685, '1685 to 1687', 'The great flight',
      'Huguenots crossed the borders at night, disguised as peasants or hidden in barrels on ships. They went to Holland, '
      '"the great ark of the refugees", to Geneva, and to London, where Spitalfields filled with silk weavers.',
      moves=[mv('foot', (2.35, 48.86, 1685), (4.5, 50.0, 1686), (4.9, 52.37, 1687), label='To Holland'),
             mv('foot', (4.83, 45.76, 1685), (6.14, 46.2, 1686), label='To Geneva'),
             mv('sail', (-1.2, 46.1, 1685), (-2.0, 46.0, 1685), (-3.5, 47.0, 1685), (-5.3, 48.2, 1686), (-5.0, 49.3, 1686), (-2.5, 50.2, 1686), (1.0, 50.9, 1686), (0.6, 51.45, 1686), label='To London')],
      sites=[site('Spitalfields', -0.07, 51.52, 1686, 'Huguenot silk weavers fill this corner of London.')]),
    S(1688, '1688 to 1700', 'Berlin and the Cape',
      'The Elector of Brandenburg\'s Edict of Potsdam offered refugees land, tax freedom and their own churches; some 20,000 '
      'came. In 1688 the Dutch East India Company took about 200 to the Cape, where they planted vines at Franschhoek.',
      moves=[mv('foot', (4.9, 52.37, 1688), (7.5, 52.0, 1688), (10.5, 52.3, 1689), (13.4, 52.52, 1690), label='To Brandenburg'),
             mv('sail', (4.3, 52.1, 1688), (1.8, 51.0, 1688), (-5.5, 49.6, 1688), (-11.0, 45.0, 1688), (-16.0, 28.0, 1688), (-20.0, 5.0, 1688), (-5.0, -20.0, 1688), (12.0, -32.0, 1688), (18.4, -33.9, 1688), label='To the Cape')],
      sites=[site('Franschhoek', 19.12, -33.91, 1688, '"French corner": Huguenot vineyards at the Cape.'),
             site('Berlin', 13.4, 52.52, 1700, 'One in three Berliners was a French refugee by 1700.')]),
  ])

M('mfecane', 'The Mfecane', 'Ndebele and Ngoni', 'refugees', '#943126', 1818, 1848,
  'In the 1810s and 1820s the rise of Shaka\'s Zulu kingdom, drought and the slave trade set off a chain of wars and '
  'migrations across southern Africa, the Mfecane, "the crushing". Peoples fled, fought and remade themselves: '
  'Mzilikazi\'s Ndebele went north to Zimbabwe, Zwangendaba\'s Ngoni went 3,000 km to Lake Tanganyika, Sebetwane\'s Kololo '
  'to the Zambezi, and Moshoeshoe gathered refugees into the Basotho nation.',
  rank=2, steps=[
    S(1818, '1818 to 1835', 'Flight from the Zulu',
      'Zwangendaba and Soshangane, beaten by Shaka\'s ally turned rival, led their followers north into Mozambique. '
      'Mzilikazi broke with Shaka in 1823 and moved onto the highveld.',
      moves=[mv('foot', (31.8, -27.0, 1819), (32.5, -25.5, 1821), (33.0, -23.5, 1826), (33.2, -20.5, 1831), (33.0, -16.5, 1835), label='Ngoni'),
             mv('foot', (31.4, -28.3, 1823), (29.5, -26.5, 1825), (27.8, -25.8, 1827), (26.2, -25.2, 1832), label='Ndebele')],
      sites=[site('Zulu kingdom', 31.4, -28.3, 1818, 'Shaka built a powerful army and state here from 1818.')]),
    S(1835, '1835 to 1848', 'North over the Zambezi',
      'The Ngoni crossed the Zambezi on 19 November 1835, a date fixed by an eclipse, and went on to Lake Tanganyika. Driven '
      'by the Boers, Mzilikazi\'s Ndebele moved north to found Bulawayo\'s kingdom.',
      moves=[mv('foot', (33.0, -16.5, 1835), (32.8, -13.5, 1838), (32.0, -10.5, 1842), (31.5, -8.0, 1845), label='Ngoni'),
             mv('foot', (26.2, -25.2, 1837), (27.0, -23.0, 1838), (28.0, -21.0, 1839), (28.6, -20.15, 1840), label='Ndebele')],
      sites=[site('Ufipa', 31.6, -8.0, 1845, 'Where Zwangendaba died, far from where he set out.')]),
  ])

M('great-trek', 'The Great Trek', 'Voortrekkers', 'settlers', '#b9770e', 1835, 1846,
  'From 1835 some 12,000 Boer farmers, angry at British rule and the end of slavery in the Cape, loaded their ox wagons and '
  'trekked north and east beyond the frontier. They fought the Ndebele and the Zulu, beat Dingane at Blood River in 1838, '
  'and founded the republics of Natalia, the Orange Free State and the Transvaal. The trek became the founding story of '
  'Afrikaner nationalism.',
  rank=1, steps=[
    S(1835, '1835 to 1837', 'Over the Orange River',
      'Parties under Louis Tregardt, Hendrik Potgieter, Gerrit Maritz and Piet Retief crossed the Orange River. At Vegkop in '
      '1836 Potgieter\'s laager of wagons beat off the Ndebele.',
      moves=[mv('wagon', (26.5, -33.3, 1835), (26.0, -31.5, 1836), (26.7, -29.5, 1836), (27.5, -27.5, 1836), (27.1, -26.7, 1837), label='Voortrekkers')],
      sites=[site('Vegkop', 27.75, -27.6, 1836, 'A laager of 50 wagons holds off Mzilikazi\'s army.')]),
    S(1837, '1837 to 1846', 'Natal and the Transvaal',
      'Retief led wagons over the Drakensberg into Natal; Dingane had him killed. On 16 December 1838 the Boers beat the Zulu '
      'at Blood River. Others moved north to found Potchefstroom and Ohrigstad.',
      moves=[mv('wagon', (26.7, -29.5, 1837), (28.5, -28.6, 1837), (29.4, -28.7, 1837), (30.4, -28.1, 1838), (30.38, -29.6, 1839), label='To Natal'),
             mv('wagon', (27.1, -26.7, 1838), (28.2, -25.75, 1842), (30.6, -24.9, 1845), label='To the Transvaal')],
      sites=[site('Blood River', 30.54, -28.1, 1838, 'Boers beat Dingane\'s army; the river ran red.'),
             site('Pietermaritzburg', 30.38, -29.6, 1839, 'Capital of the Boer republic of Natalia.')]),
  ])

M('trail-of-tears', 'The Trail of Tears', 'Cherokee, Choctaw, Creek', 'forced', '#7b241c', 1831, 1839,
  'The Indian Removal Act of 1830 forced the Cherokee, Choctaw, Creek, Chickasaw and Seminole off their lands in the '
  'American South to "Indian Territory", today\'s Oklahoma. Some 60,000 people were marched west, many in winter; '
  'thousands died of cold, hunger and disease on the way. The Cherokee remember it as "the trail where they cried".',
  story='ev:trail-of-tears', numbers='About 60,000 removed; perhaps 15,000 died', rank=1, steps=[
    S(1831, '1831 to 1837', 'Choctaw and Creek',
      'The Choctaw went first, in 1831 to 1833, in a winter of blizzards. The Creek were removed in chains after the war of '
      '1836.',
      moves=[mv('foot', (-89.5, 32.8, 1831), (-91.0, 33.6, 1831), (-92.3, 34.7, 1832), (-94.5, 34.3, 1832), (-95.6, 34.2, 1833), label='Choctaw'),
             mv('foot', (-85.5, 32.4, 1836), (-87.5, 34.0, 1836), (-90.05, 35.15, 1836), (-92.3, 34.7, 1837), (-95.35, 35.8, 1837), label='Creek')]),
    S(1838, '1838 to 1839', 'The Cherokee',
      'In 1838 US troops rounded up 16,000 Cherokee into camps and sent them west in detachments across Tennessee, Kentucky, '
      'Illinois, Missouri and Arkansas. About 4,000 died.',
      moves=[mv('foot', (-84.87, 35.18, 1838), (-86.78, 36.16, 1838), (-87.9, 37.1, 1838), (-89.5, 37.3, 1838), (-91.5, 37.6, 1838),
                (-93.3, 37.2, 1839), (-94.4, 36.4, 1839), (-94.97, 35.91, 1839), label='Cherokee')],
      sites=[site('New Echota', -84.91, 34.54, 1838, 'Cherokee capital in Georgia, emptied by the removal.'),
             site('Tahlequah', -94.97, 35.91, 1839, 'New capital of the Cherokee Nation in Indian Territory.')]),
  ])

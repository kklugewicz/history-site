from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('columbus-first-voyage', "Columbus's first voyage", 'voyage', (1492, 1493),
      'Three small ships sailed west to find Asia and found a world Europe did not know.',
      scene('A plan to sail west',
            'Christopher Columbus, a sailor from Genoa, was sure that Asia lay only about 4,000 km west of Europe. He had '
            'shrunk the Earth and stretched Asia: the real distance to Japan is nearer 20,000 km. Experts in Portugal and '
            'in Spain turned him down, because they thought his numbers were wrong. They were right.',
            kick='How it began', img='Erdapfel', cap='The oldest globe that survives, made in 1492, has no Americas on it'),
      figure('isabella-i-of-castile', 'A yes at Santa Fe',
             'In January 1492 Granada, the last Muslim kingdom in Spain, surrendered. At the royal camp of Santa Fe, Queen '
             'Isabella and King Ferdinand at last agreed to back him. If he found land, he would be its governor, Admiral '
             'of the Ocean Sea, and keep a tenth of its riches.',
             y=1492, at='santa_fe_gr'),
      scene('Three small ships',
            'The Niña, the Pinta and the larger Santa María left Palos on 3 August 1492 with about 90 men. After repairs in '
            'the Canary Islands they sailed west on 6 September, into an ocean no one they knew had crossed, pushed by the '
            'steady trade winds.',
            img='Santa María (ship)', cap='A replica of the Santa María', y=1492, at='palos'),
      tale('Two logbooks',
           'Columbus kept two counts of how far they had sailed, it is said: a true one for himself and a shorter one for '
           'the crew, so they would not panic at how far they were from home. The joke is that the false count was closer '
           'to the truth. By 10 October the men were close to mutiny, and he promised to turn back if no land was seen '
           'within days.',
           y=1492),
      turn('Land!',
           'At 2 in the morning on 12 October a lookout on the Pinta, Rodrigo de Triana, saw white cliffs in the moonlight '
           'and shouted "Tierra!" Columbus claimed the reward for himself, saying he had seen a light the night before. '
           'They landed on an island of the Bahamas its people called Guanahani. Columbus named it San Salvador.',
           img='Landing of Columbus', cap='The landing, as John Vanderlyn painted it in 1847', y=1492, at='guanahani'),
      scene('The Taíno',
            'The islanders were Taíno, farmers and fishers who welcomed the strangers with gifts. Our words hammock, canoe, '
            'hurricane, barbecue and tobacco come from their language. Columbus wrote that they were gentle, had no iron '
            'weapons and would make good servants, and he took several of them with him as guides.',
            kick='Who they met', img='Taíno', y=1492),
      scene('Looking for the Great Khan',
            'Sure he was off the coast of Asia, Columbus sailed on to Cuba, which he took for part of China, and sent two men '
            'inland with letters for the Great Khan. They found villages, and people smoking rolled leaves. On Hispaniola '
            'the chief Guacanagarí traded gold ornaments, and Columbus was certain great riches lay close by.',
            img='Hispaniola', y=1492, at='hispaniola'),
      tale('Shipwreck on Christmas Eve',
           'On Christmas Eve, with a ship\'s boy at the helm, the Santa María ran onto a reef and broke up. Guacanagarí\'s '
           'people helped save her cargo. Columbus built a fort from her timbers, La Navidad, and left 39 men there. When '
           'he came back the next year, every one of them was dead.',
           y=1492, at='la_navidad'),
      scene('Home through the storms',
            'On the way back, storms nearly sank the Niña. Columbus sealed an account of his voyage in a barrel and threw it '
            'overboard in case they drowned. He reached Lisbon, then Palos on 15 March 1493, and rode in triumph to '
            'Barcelona with parrots, gold and six Taíno to show the king and queen.',
            kick='The return', y=1493, at='barcelona'),
      cost('What came next',
           'He came back that same year with 17 ships and 1,200 men to settle and rule. War, forced labour in the gold '
           'fields and diseases the islanders had never met, above all smallpox, destroyed the Taíno world. Within 50 years '
           'only a few hundred Taíno were left on Hispaniola.',
           num='A few hundred', of='Taíno left on Hispaniola by the 1540s', img='Bartolomé de las Casas',
           cap='Bartolomé de las Casas, the friar who recorded what was done to them', y=1542),
      legacy('Columbus died in 1506 still insisting he had reached Asia. But his voyage joined the two halves of the world '
             'for good. Ships soon carried horses, wheat and smallpox west, and maize, potatoes and tomatoes east, and it '
             'began the conquest of the Americas.',
             'Linked Europe and the Americas for good',
             'Began the exchange of crops, animals and diseases',
             'Opened the way to the conquest of the Americas',
             img='Columbian exchange'),
      states=['Castille', 'Aragón', 'Taino', 'Caribbean hunter-gatherers'],
      wiki='Voyages of Christopher Columbus', img='Landing of Columbus', at='guanahani')

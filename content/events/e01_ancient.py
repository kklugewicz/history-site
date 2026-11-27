from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('invention-of-writing', 'The invention of writing', 'invention', (-3400, -3100),
      'Temple clerks in Sumer pressed marks into clay to count sheep and barley, and history began.',
      scene('Counting sheep',
            'In the first cities of Sumer, in what is now southern Iraq, temples collected grain, beer, sheep and cloth. '
            'To keep track, officials used small clay tokens, then pressed marks into clay tablets: a picture of an ear of '
            'barley, and strokes for the numbers. Writing began as bookkeeping.',
            kick='How it began', img='Proto-cuneiform', y=-3300, at='uruk'),
      made('Pictures that stand for sounds',
           'Scribes learned to use a sign for its sound as well as its meaning, like a rebus: in Sumerian the arrow and the '
           'word for life were both "ti", so the arrow sign could write life.',
           'Now writing could record anything people said, such as names, laws, letters, prayers and stories, not only '
           'lists of goods.',
           img='Cuneiform', y=-3000),
      scene('Wedges in clay',
            'Scribes wrote by pressing a cut reed into wet clay, leaving wedge shapes we call cuneiform, from the Latin for '
            'wedge. Clay was cheap and it lasted: when a palace library burned, the fire baked its tablets hard. Cuneiform '
            'was used for 3,000 years and for more than a dozen languages.',
            img='Clay tablet', y=-2600),
      scene("Egypt's own signs",
            'Writing appeared in Egypt at about the same time, perhaps inspired by Sumer, perhaps not. Hieroglyphs, '
            'pictures standing for sounds and ideas, were carved on temples and tombs for over 3,000 years. Later, people '
            'in China and in Mexico invented writing again, on their own.',
            img='Egyptian hieroglyphs', y=-3200, at='abydos'),
      figure(None, 'The first author with a name',
             'Enheduanna, daughter of King Sargon of Akkad, was high priestess of the moon god at Ur around 2300 BC. She '
             'wrote hymns to the goddess Inanna and put her own name to them, which makes her the first author in history '
             'we know by name.',
             img='Enheduanna', y=-2285, at='ur'),
      tale('School was hard',
           'Scribes were trained in "tablet houses". A Sumerian school story tells of a pupil who was caned for talking, '
           'for standing up, for walking out of the gate and for bad handwriting. That evening his father invited the '
           'teacher home for dinner and gave him a present, and the beatings stopped.',
           y=-2000, at='nippur'),
      work('The Epic of Gilgamesh',
           'Written in cuneiform, the epic tells of Gilgamesh, a king of Uruk who searches for a way to escape death. It has '
           'a great flood, a man who survives it in a boat full of animals, and a snake that steals the plant of youth. It '
           'is the oldest great story to survive.',
           img='Epic of Gilgamesh', y=-2100),
      legacy('Writing let knowledge outlive the people who had it. Laws could be fixed, letters sent, stories kept and '
             'the past recorded, which is why the time before writing is called prehistory. The letters you are reading '
             'go back, through the Greeks and Phoenicians, to signs first drawn in Egypt.',
             'Began as bookkeeping in Sumer',
             'Invented again in Egypt, China and Mexico',
             'The line between prehistory and history'),
      states=['Ur', 'city-states', 'Elam', 'Egypt'], wiki='History of writing', img='Cuneiform', at='uruk')

event('great-pyramid', 'Building the Great Pyramid', 'building', (-2580, -2560),
      'For nearly 4,000 years the tomb of King Khufu was the tallest building on Earth.',
      figure('khufu', 'A tomb for a king',
             'Khufu ruled Egypt around 2589 to 2566 BC. Egyptians believed their king joined the gods when he died, and '
             'that his body and his tomb had to last forever. Khufu chose the desert plateau of Giza, west of the Nile, '
             'and his vizier Hemiunu, probably his nephew, planned the greatest pyramid of all.',
             y=-2589, at='giza'),
      scene('Two million blocks',
            'The pyramid holds about 2.3 million blocks of limestone, most weighing over two tonnes, and stood 146 metres '
            'high. Its sides face north, south, east and west almost exactly, and its base is level to within a few '
            'centimetres. It was the tallest building in the world until the 1300s AD.',
            img='Great Pyramid of Giza', y=-2570, at='giza'),
      scene('Who built it',
            'Not slaves, as the old story has it. Archaeologists found the workers\' town nearby, with bakeries, breweries '
            'and the bones of thousands of cattle and sheep they ate. Teams of a few thousand skilled men worked all year, '
            'joined by farmers in the flood season, when their fields were under water.',
            img='Giza pyramid complex', y=-2570, at='giza'),
      made('Sledges, water and ramps',
           'Workers dragged blocks on wooden sledges and poured water on the sand in front, which halves the effort, a '
           'trick shown in an Egyptian tomb painting. Ramps of mud brick and rubble rose with the pyramid.',
           'No one knows the ramps\' exact shape, but with copper tools, rope and muscle, Egypt moved mountains of stone '
           'with a precision builders still admire.'),
      tale('The diary of Merer',
           'In 2013 archaeologists at an ancient harbour on the Red Sea found the oldest written papyri ever discovered: the '
           'logbook of Merer, an inspector whose crew of about 40 men ferried limestone down the Nile to Giza for the '
           'pyramid. It records their trips, month by month, in the last years of Khufu\'s reign.',
           img='Diary of Merer', y=-2560, at='wadi_al_jarf'),
      tale('Graffiti of the work gangs',
           'In small rooms above the king\'s burial chamber, never meant to be seen, the work gangs painted their team '
           'names in red, such as "Friends of Khufu". They are among the few marks left by the men who built it.',
           y=-2570, at='giza'),
      scene('The last wonder',
            'Two thousand years later the Greeks listed seven wonders of the world. The Great Pyramid was already the '
            'oldest of them. The Hanging Gardens, the Colossus and the lighthouse of Alexandria are gone, and it is the '
            'only one still standing.',
            img='Seven Wonders of the Ancient World', y=-200),
      legacy('The Great Pyramid shows what an early state could do when it organised tens of thousands of people around '
             'one goal. It has drawn travellers, scholars and dreamers for 4,500 years, and it is still the one ancient '
             'wonder you can visit.',
             'Tallest building on Earth for nearly 4,000 years',
             'Built by organised crews, not slaves',
             'The only ancient wonder still standing'),
      states=['Egypt'], wiki='Great Pyramid of Giza', at='giza')

event('bronze-age-collapse', 'The Bronze Age collapse', 'fall', (-1200, -1150),
      'Within fifty years the great kingdoms of the eastern Mediterranean fell, and no one is sure why.',
      scene('A connected world',
            'Around 1250 BC the eastern Mediterranean was shared by great kingdoms whose kings wrote to each other as '
            'brothers: Egypt, the Hittites, Babylon, Assyria and the Mycenaean Greeks. Ships carried copper from Cyprus and '
            'tin from as far as Afghanistan to make bronze. One wreck, found off Turkey at Uluburun, carried ten tonnes of '
            'copper.',
            kick='How it began', img='Uluburun shipwreck', y=-1300, at=(31.51, 36.13), where='Uluburun'),
      scene('Everything falls',
            'In the decades after 1200 BC nearly all of it vanished. The Hittite capital Hattusa was burned and abandoned. '
            'The palaces of Mycenae and Pylos fell, and Greece forgot how to write for 400 years. In the rich port of '
            'Ugarit, letters begging for ships and soldiers were found where they had been left, perhaps never sent.',
            img='Hattusa', y=-1185, at='hattusa'),
      battle('The Sea Peoples',
             'Egyptian records blame raiders from the sea, peoples on the move with their families. Around 1175 BC Ramesses '
             'III fought them in the Nile Delta and won, and had the battle carved on the walls of his temple at Medinet '
             'Habu. The Philistines may have been one of these peoples.',
             img='Medinet Habu', y=-1175, at=(32.6, 25.72), where='Medinet Habu'),
      scene('A perfect storm',
            'Historians now think no single cause was to blame. Drought and famine, earthquakes, revolts, raiders and the '
            'breakdown of trade may all have struck together, and because the kingdoms depended on each other, the fall of '
            'one dragged down the next.',
            kick='Why it happened'),
      turn('Out of the ruins',
           'Smaller peoples grew in the space left behind: the Phoenicians, who spread an alphabet of just 22 letters, the '
           'Israelites, the Arameans and the Philistines. Iron, found almost everywhere, replaced bronze, which needed tin '
           'carried from far away.',
           img='Phoenician alphabet', y=-1050),
      legacy('The collapse ended the Bronze Age world and opened the Iron Age. Out of the dark centuries that followed '
             'came the alphabet, the Greece of Homer and the kingdom of Israel. Historians study it as a warning of how a '
             'connected world can fall apart all at once.',
             'Ended the great kingdoms of the Bronze Age',
             'Greece forgot how to write for 400 years',
             'Made way for iron and the alphabet'),
      states=['Hittites', 'Egypt', 'Greek city-states', 'Assyria', 'Babylonia', 'Kingdom of David and Solomon'],
      wiki='Late Bronze Age collapse', img='Sea Peoples', at='hattusa')

event('trojan-war', 'The Trojan War', 'war', (-1194, -1184),
      'A legend of a stolen queen, a ten-year siege and a wooden horse, with a real burned city underneath.',
      scene('A thousand ships',
            'In the Greek legend, Paris, a prince of Troy, carried off Helen, wife of King Menelaus of Sparta and the most '
            'beautiful woman in the world. Menelaus\'s brother Agamemnon, king of Mycenae, gathered a thousand ships and '
            'the greatest heroes of Greece to bring her back.',
            kick='How it began, in legend', img='Helen of Troy', y=-1194, at='mycenae'),
      battle('Ten years at the walls',
             'The Greeks camped on the beach and besieged Troy for ten years. Homer\'s Iliad tells only a few weeks of it: '
             'the quarrel between Agamemnon and Achilles, the best of the Greek fighters, and how Achilles, mad with grief '
             'for his friend Patroclus, killed Hector, Troy\'s champion, and dragged his body behind his chariot.',
             img='Iliad', y=-1185, at='troy'),
      tale('The wooden horse',
           'At last Odysseus thought of a trick. The Greeks built a huge wooden horse, hid soldiers inside and sailed out of '
           'sight. The Trojans dragged the horse into their city as a prize. That night the soldiers climbed out and opened '
           'the gates, and Troy burned. The Roman poet Virgil made a Trojan say: beware of Greeks bearing gifts.',
           img='Trojan Horse', y=-1184, at='troy'),
      scene('The long way home',
            'The Odyssey follows Odysseus, who took ten more years to reach his home on Ithaca, past the Cyclops, the '
            'Sirens and the witch Circe, while his wife Penelope kept her suitors waiting. Aeneas, a Trojan who escaped, was '
            'said to have reached Italy, and the Romans claimed him as their ancestor.',
            img='Odyssey', at='ithaca'),
      figure(None, 'Homer',
             'The two poems are said to be the work of Homer, a blind poet of the 700s BC, though no one knows if he '
             'existed. They were sung for generations before they were written down, and every educated Greek and Roman '
             'learned them by heart.',
             img='Homer', y=-750),
      turn('Schliemann digs for Troy',
           'In 1871 Heinrich Schliemann, a rich German businessman, dug into the mound of Hisarlik in Turkey, sure it was '
           'Troy. He found nine cities, one on top of another, and gold he called Priam\'s treasure, though it was a '
           'thousand years too old. Layers from around 1200 BC show a city that was burned.',
           img='Heinrich Schliemann', y=1871, at='troy'),
      legacy('Real or not, the Trojan War is the first great story of Europe. The Iliad and the Odyssey shaped Greek and '
             'Roman life and are still read, and we still speak of an odyssey, an Achilles heel and a Trojan horse, now '
             'also a kind of computer virus.',
             "Told in Homer's Iliad and Odyssey",
             'A real burned city lies under the legend',
             'Gave us the Trojan horse and the Achilles heel'),
      war='trojan-war', wiki='Trojan War', img='Trojan Horse', label='War of legend')

event('first-olympics', 'The first Olympic Games', 'games', (-776, -776),
      'One footrace at a shrine of Zeus began a festival that lasted a thousand years and came back in 1896.',
      scene('A race for Zeus',
            'Greek tradition says the first Olympic Games were held in 776 BC at Olympia, a sanctuary of Zeus in the west '
            'of the Peloponnese. There was one event, a sprint of one stadion, about 192 metres, and the first winner on '
            'record was a cook named Koroibos, from the nearby town of Elis.',
            y=-776, at='olympia'),
      scene('The sacred truce',
            'Every four years heralds announced a truce, so athletes and crowds could travel safely to Olympia from all '
            'over the Greek world. The four-year cycle, an Olympiad, became a way of counting time, and the list of winners '
            'gives some of the first fixed dates in Greek history.'),
      scene('Five days of games',
            'In time the festival grew to five days, with longer races, wrestling, boxing, chariot races and the '
            'pentathlon. Athletes competed naked and rubbed with olive oil. Married women were not allowed to watch, though '
            'unmarried girls ran their own races in honour of the goddess Hera.',
            img='Ancient Olympic pentathlon'),
      tale('A crown of olive leaves',
           'The only prize at Olympia was a wreath cut from a sacred olive tree, though home towns gave winners free meals '
           'for life and statues. Cheats were fined, and the fines paid for bronze statues of Zeus that lined the way into '
           'the stadium, each with a cheat\'s name on its base.',
           at='olympia'),
      figure(None, 'Milo of Croton',
             'The most famous champion was the wrestler Milo of Croton, who won six times in the 500s BC. Legend says he '
             'grew strong by carrying a newborn calf on his shoulders every day until it was a full-grown bull.',
             img='Milo of Croton', y=-540),
      scene('The end, and a new start',
            'The games went on for more than a thousand years, until the 390s AD, when the Christian emperor Theodosius '
            'banned pagan festivals. In 1896 a French baron, Pierre de Coubertin, revived them in Athens, and they have been '
            'held every four years since, except during the world wars.',
            kick='What came after', img='1896 Summer Olympics', y=1896, at='athens'),
      legacy('The ancient games gave the quarrelsome Greek cities a festival they shared, and gave the world the idea of '
             'sport as a peaceful contest between peoples. The Olympic flame for today\'s games is still lit at Olympia.',
             'First recorded in 776 BC',
             'Held every four years under a sacred truce',
             'Revived in Athens in 1896'),
      states=['Greek city-states'], wiki='Ancient Olympic Games', at='olympia')

event('greco-persian-wars', 'The Greco-Persian Wars', 'war', (-499, -449),
      'The largest empire on Earth twice invaded Greece, and was beaten at Marathon, Salamis and Plataea.',
      scene('The Ionian revolt',
            'Persia ruled the largest empire the world had yet seen, from Egypt to India, and with it the Greek cities on '
            'the coast of Turkey. In 499 BC those cities rebelled, and Athens sent ships to help them burn the Persian city '
            'of Sardis. King Darius crushed the revolt and swore to punish Athens.',
            kick='How it began', y=-499, at='sardis'),
      battle('Marathon',
             'In 490 BC a Persian army landed at Marathon, 40 km from Athens. The Athenians, helped only by little Plataea, '
             'charged at a run and drove them back to their ships. Legend says a messenger ran all the way to Athens with '
             'the news and then dropped dead, the story behind today\'s marathon race.',
             img='Battle of Marathon', y=-490, at='marathon'),
      figure('leonidas-i', 'Thermopylae',
             'Ten years later Darius\'s son Xerxes came with a vast army and fleet. At the narrow pass of Thermopylae, King '
             'Leonidas of Sparta held him off for three days, until a local man showed the Persians a path around the '
             'pass. Leonidas, his 300 Spartans and the allies who stayed with them fought to the last.',
             y=-480, at='thermopylae'),
      battle('Salamis',
             'Athens was abandoned and burned. But its leader Themistocles lured the Persian fleet into the narrow strait '
             'of Salamis, where its numbers counted for nothing. Xerxes watched from a throne on the shore as the Greek '
             'triremes rammed and sank his ships.',
             img='Battle of Salamis', y=-480, at='salamis'),
      battle('Plataea',
             'In 479 BC the Greek allies, led by Sparta, destroyed the Persian army left behind in Greece at Plataea. On '
             'the same day, it was said, a Greek fleet burned the Persian ships at Mycale. Persia never again tried to '
             'conquer Greece.',
             y=-479, at='plataea'),
      figure('herodotus', 'The father of history',
             'Herodotus, born in a Greek city under Persian rule, travelled widely asking people what had happened and '
             'why. His Histories, the story of these wars, earned him the name father of history. He also reports plenty '
             'of gossip, and often says when he does not believe it.',
             y=-430),
      legacy('The Greek victories kept Persia out of Europe and let Athens grow into the city of democracy, theatre and '
             'philosophy. The wars were long told as freedom against tyranny, though Persia was a tolerant empire and '
             'many Greeks fought on its side.',
             'Marathon, Thermopylae and Salamis',
             'Kept the Greek cities free of Persian rule',
             'Opened the golden age of Athens'),
      war='greco-persian-wars', wiki='Greco-Persian Wars', img='Battle of Salamis')

event('peloponnesian-war', 'The Peloponnesian War', 'war', (-431, -404),
      'Athens and Sparta fought for 27 years, and the golden age of Athens ended in plague, defeat and hunger.',
      scene('Athens against Sparta',
            'After the Persian wars, Athens led a league of island and coastal cities and turned it into an empire paid for '
            'by their tribute. Sparta, a land power ruled by a warrior class, feared it. The historian Thucydides said the '
            'war came from the rise of Athens and the fear it caused in Sparta.',
            kick='How it began', y=-431),
      figure('pericles', 'Behind the walls',
             'Pericles, Athens\'s leading statesman, had a plan: let the Spartans burn the farms of Attica while everyone '
             'sheltered behind the Long Walls that joined Athens to its port, and let the navy raid the enemy coast. In his '
             'speech for the first dead, he praised Athens as a school for all of Greece.',
             y=-431, at='athens'),
      cost('The plague',
           'In 430 BC a plague broke out in the crowded city. Thucydides caught it and lived, and described the fevers, '
           'the bodies piled in temples and people giving up all law and decency. Perhaps a quarter of the people died, '
           'Pericles among them.',
           num='A quarter', of='of Athens died, perhaps', img='Plague of Athens', y=-430, at='athens'),
      battle('Disaster in Sicily',
             'In 415 BC Athens sent a great fleet to conquer Syracuse in Sicily, urged on by the brilliant, reckless '
             'Alcibiades, who then went over to Sparta. The expedition ended in total defeat: thousands of Athenians were '
             'captured and left to die in the stone quarries of Syracuse.',
             y=-413, at='syracuse'),
      tale('A comedy about peace',
           'Even in wartime Athens laughed at itself. In Aristophanes\' comedy Lysistrata, staged in 411 BC, the women of '
           'Athens and Sparta go on strike and refuse their husbands until the men make peace.',
           img='Lysistrata', y=-411, at='athens'),
      battle('Aegospotami',
             'Persian gold paid for a Spartan fleet under Lysander, who caught the Athenian ships pulled up on a beach at '
             'Aegospotami in 405 BC and took almost all of them. Cut off from its grain, Athens starved and surrendered in '
             '404, and its Long Walls were pulled down to the music of flute girls.',
             y=-405, at=(26.66, 40.33), where='Aegospotami'),
      legacy('The war wore out the Greek cities and left them open to Macedon a few decades later. Thucydides\'s history '
             'of it, written to last for all time, is still read by generals and diplomats for what it says about power, '
             'fear and war.',
             'Athens against Sparta for 27 years',
             'Ended the golden age of Athens',
             'Told by Thucydides, the first great war historian'),
      war='peloponnesian-war', wiki='Peloponnesian War')

event('alexander-conquests', "Alexander's conquest of Persia", 'conquest', (-334, -323),
      'In eleven years a young king of Macedon marched from Greece to India and toppled the Persian Empire.',
      figure('philip-ii-of-macedon', "Philip's army",
             'Macedon was a rough kingdom north of Greece until Philip II built a new army: pikemen with spears over five '
             'metres long in a dense block, the phalanx, and heavy cavalry. By 338 BC he had beaten Athens and Thebes and '
             'planned to invade Persia. In 336 he was murdered at his daughter\'s wedding.',
             y=-338, at='chaeronea'),
      figure('alexander-the-great', 'Granicus and Issus',
             'His son Alexander, 22, crossed into Asia in 334 BC with about 40,000 men. He won at the river Granicus, '
             'nearly losing his life, and in 333 at Issus routed King Darius III, who fled and left his mother, wife and '
             'daughters in Alexander\'s camp.',
             y=-333, at='issus'),
      battle('The siege of Tyre',
             'Tyre, a Phoenician city on an island, refused to open its gates. Alexander built a causeway across 800 metres '
             'of sea and took it after seven months. Egypt then welcomed him as pharaoh, and on its coast he founded '
             'Alexandria.',
             img='Siege of Tyre (332 BC)', y=-332, at='tyre'),
      battle('Gaugamela',
             'In 331 BC Darius met him again near Gaugamela with a far bigger army and chariots with scythes on their '
             'wheels. Alexander led his cavalry into a gap in the Persian line, straight at Darius, who fled once more and '
             'was later killed by his own men. The Persian Empire was Alexander\'s.',
             img='Alexander Mosaic', cap='The Alexander Mosaic from Pompeii, with Darius in his chariot', y=-331, at='gaugamela'),
      tale('Persepolis burns',
           'At Persepolis, the great palace of the Persian kings, Alexander\'s men emptied the treasury. Then, after a '
           'drinking party, the palace was set on fire. Ancient writers disagree whether it was revenge for the burning of '
           'Athens or just drunkenness. Its ruins still stand.',
           img='Persepolis', y=-330, at='persepolis'),
      battle('To the edge of the world',
             'He pushed on through Central Asia into India, where in 326 BC he beat King Porus and his war elephants at the '
             'river Hydaspes. But his men, eight years from home, refused to go further. On the way back many died '
             'crossing the Gedrosian desert.',
             y=-326, at=(73.6, 32.9), where='River Hydaspes'),
      turn('Death in Babylon',
           'In 323 BC, planning to conquer Arabia, Alexander fell ill after a banquet in Babylon and died at 32. Asked who '
           'should have his empire, he is said to have answered: the strongest. His generals fought over it for 40 years '
           'and split it into kingdoms.',
           y=-323, at='babylon'),
      legacy('In eleven years Alexander built an empire from Greece to India. It broke apart at once, but the Greek '
             'kingdoms that followed spread Greek language, cities and art across the Middle East for centuries, and '
             'mixed them with the cultures of Persia, Egypt and India.',
             'Conquered the Persian Empire in eleven years',
             'Founded Alexandria and dozens of other cities',
             'Spread Greek culture to the edge of India'),
      war='macedon-and-alexander', wiki='Wars of Alexander the Great', img='Alexander Mosaic')

event('qin-unification', 'The Qin unification of China', 'conquest', (-262, -221),
      'After centuries of war one kingdom swallowed the other six, and its king made himself the First Emperor.',
      scene('The Warring States',
            'For two centuries seven kingdoms fought over the old lands of the Zhou kings, with armies of hundreds of '
            'thousands of conscripted farmers armed with iron and crossbows. It was also an age of thinkers: followers of '
            'Confucius, the Daoists, and the general Sun Tzu, whose Art of War is still read.',
            kick='How it began', y=-400),
      scene('The Qin machine',
            'Qin, in the far west, was remade by the minister Shang Yang into a state built for war. Families were grouped '
            'in fives and punished for each other\'s crimes, rank came only from service in war, and soldiers were '
            'rewarded by the number of enemy heads they brought back.',
            y=-356, at='xianyang'),
      battle('Changping',
             'In 260 BC Qin trapped the army of Zhao at Changping. After 46 days the starving Zhao soldiers surrendered, and '
             'the Qin general Bai Qi had almost all of them killed, by tradition 400,000 men. Zhao never recovered.',
             y=-260, at=(112.9, 35.8), where='Changping'),
      tale('The assassin and the map',
           'In 227 BC the prince of Yan sent Jing Ke to kill the king of Qin. He came with a gift, a map of land to be '
           'handed over, with a poisoned dagger rolled up inside. As the map unrolled he seized the king\'s sleeve and '
           'stabbed, and missed. The king ran round a pillar, finally drew his long sword and cut him down.',
           img='Jing Ke', y=-227, at='xianyang'),
      figure('qin-shi-huang', 'One China',
             'Between 230 and 221 BC Qin conquered the other six kingdoms one by one. Its king took a new title, Shi '
             'Huangdi, the First Emperor. He made everyone use the same script, coins and weights, and even the same width '
             'of cart axle, so that wagons fitted the ruts of every road.',
             y=-221, at='xianyang'),
      made('Walls and roads',
           'The emperor had older walls joined into one long wall against the nomads of the north, and built thousands of '
           'kilometres of roads and canals. Hundreds of thousands of conscripts did the work, and many died.',
           'It was the first Great Wall. Most of the wall standing today was built much later, by the Ming, but the idea '
           'began with Qin.',
           img='Great Wall of China', y=-214),
      work('The terracotta army',
           'Near his tomb the First Emperor was buried with more than 7,000 life-size clay soldiers, each with its own '
           'face, and horses and chariots. Farmers digging a well found them in 1974. His burial mound itself has never '
           'been opened.',
           img='Terracotta Army', y=-210, at=(109.27, 34.38), where="Lintong, Xi'an"),
      legacy('The Qin dynasty fell only 15 years after unification, but China never again stayed divided for long. The '
             'emperor, the single script and the central government Qin made lasted 2,000 years, and the name China may '
             'come from Qin.',
             'Ended the Warring States in 221 BC',
             'Gave China one script, one coinage, one measure',
             'Began the Great Wall and the terracotta army'),
      war='warring-states-qin-unification', wiki='Qin\'s wars of unification', img='Terracotta Army')

event('punic-wars', 'The Punic Wars', 'wars', (-264, -146),
      'Rome and Carthage fought three wars for the Mediterranean, and only one city survived.',
      scene('Rome against Carthage',
            'Carthage, a rich trading city in North Africa founded by Phoenicians, ruled the western Mediterranean by sea. '
            'Rome had just won all of Italy. In 264 BC they clashed over Sicily, and fought three wars over 120 years. The '
            'Romans called them Punic, from their word for Phoenician.',
            kick='How it began', y=-264, at='carthage'),
      made('Rome learns to fight at sea',
           'Rome had almost no warships. It copied a wrecked Carthaginian ship, trained rowers on benches on dry land, and '
           'added the corvus, a boarding bridge with an iron spike that hooked onto an enemy ship.',
           'Sea battles became land battles, which the legions won. Rome won the first war in 241 BC and took Sicily, its '
           'first province overseas.',
           img='Corvus (boarding device)', y=-260),
      figure('hannibal', 'Elephants over the Alps',
             'In 218 BC Hannibal, a Carthaginian general in Spain, led an army with 37 war elephants over the Pyrenees and '
             'the Alps into Italy, losing much of it to snow, cold and mountain tribes. As a boy, it was said, he had sworn '
             'to his father never to be a friend of Rome.',
             y=-218, at=(7.0, 45.2), where='The Alps'),
      battle('Cannae',
             'At Cannae in 216 BC Hannibal let the Roman centre push deep into his line, then closed his wings around '
             'them. In one afternoon some 50,000 Romans died, perhaps the bloodiest single day of battle before modern '
             'times. Generals still study his trap.',
             img='Battle of Cannae', y=-216, at='cannae'),
      figure('scipio-africanus', 'Scipio strikes Africa',
             'Rome refused to make peace and avoided great battles in Italy. Its young general Scipio took Spain, then '
             'landed in Africa, and Carthage called Hannibal home. At Zama in 202 BC Scipio beat him, and Carthage gave up '
             'its empire and its fleet.',
             y=-202, at='zama'),
      tale('Carthage must be destroyed',
           'Carthage grew rich again. In Rome the old senator Cato ended every speech, whatever its subject, with the '
           'words "Carthage must be destroyed", and once held up fresh figs to the Senate, picked in Carthage only three '
           'days\' sail away.',
           img='Cato the Elder', y=-150, at='rome'),
      cost('The end of Carthage',
           'In 146 BC, after a three-year siege, Rome stormed Carthage, burned it for days and sold the survivors into '
           'slavery. The story that the Romans sowed its fields with salt was made up many centuries later.',
           num='50,000', of='survivors sold into slavery', y=-146, at='carthage'),
      legacy('Victory over Carthage made Rome master of the Mediterranean and set it on the road to empire. Hannibal lost, '
             'but became the model of the brilliant general, and his trap at Cannae has been copied on battlefields ever '
             'since.',
             'Three wars over 120 years',
             'Hannibal crossed the Alps with elephants',
             'Made Rome master of the Mediterranean'),
      war='punic-wars', wiki='Punic Wars', img='Battle of Zama')

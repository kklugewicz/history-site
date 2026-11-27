from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

TIAN = (116.39, 39.9)

event('soviet-afghan-war', 'The Soviet war in Afghanistan', 'war', (1979, 1989),
      'The Soviet army marched into Afghanistan to save a communist government, and was fought to a standstill for ten years.',
      scene('A revolution by force',
            'In April 1978 Afghan communists seized power in a coup and set out to remake the country by force. They '
            'broke up estates, changed the rules of marriage, and arrested and killed thousands of opponents. Revolts '
            'spread through the countryside, and in March 1979 the city of Herat rose up. Soviet advisers were among '
            'the dead.',
            kick='How it began', y=1979, at='herat'),
      figure('leonid-brezhnev', 'The invasion',
             'Moscow decided to step in. On 27 December 1979 Soviet special forces stormed the palace in Kabul, killed '
             'the president, Hafizullah Amin, a communist the Kremlin no longer trusted, and put Babrak Karmal in his '
             'place. Tens of thousands of troops rolled in over the border. The old men around Leonid Brezhnev thought '
             'it would all take a few months.',
             y=1979, at='kabul'),
      scene('Holy warriors',
            'The Afghans who fought back called themselves mujahideen, those who wage jihad. They were farmers, '
            'tribesmen and village mullahs, split into many rival parties, and they fought from the mountains, '
            'ambushing convoys on the roads. Through Pakistan, the United States and Saudi Arabia sent them money and '
            'guns, and Arab volunteers came to join them.',
            y=1982),
      figure('ahmad-shah-massoud', 'The Lion of Panjshir',
             'In the Panjshir valley north of Kabul a young commander, Ahmad Shah Massoud, beat back one Soviet '
             'offensive after another, slipping away into the side valleys and striking again when the troops left. '
             'His men called him the Lion of Panjshir. Away from the cities and the main roads, the Soviets never '
             'really held the country.',
             y=1984, at='panjshir'),
      cost('A people in flight',
           'Soviet aircraft bombed villages that sheltered the rebels, and millions of mines were laid in the fields. '
           'Between half a million and two million Afghans were killed, and whole valleys emptied as people fled to '
           'camps in Pakistan and Iran, the largest crowd of refugees in the world at the time.',
           num='Over 5 million', of='Afghans fled abroad', y=1985, at='peshawar'),
      turn('Stingers',
           'In 1986 the United States began giving the mujahideen Stinger missiles, light enough to fire from the '
           'shoulder, which brought down Soviet helicopters and jets. Pilots had to fly higher, and lost much of their '
           'edge. Historians still argue about how much the missiles changed the war, but Moscow was already looking '
           'for a way out.',
           y=1986),
      figure('mikhail-gorbachev', 'A bleeding wound',
             'The new Soviet leader, Mikhail Gorbachev, called the war a bleeding wound. In 1988 he agreed to pull out, '
             'and on 15 February 1989 the last Soviet commander walked back across the bridge over the Amu Darya into '
             'the Soviet Union. About 15,000 Soviet soldiers had died, and many more came home wounded in body or '
             'mind.',
             y=1989, at='termez'),
      scene('The war goes on',
            'The communist government held out for three more years, until Soviet aid stopped. Then the mujahideen '
            'leaders turned on each other, and their rockets reduced much of Kabul to rubble. In 1996 a new movement '
            'of religious students from the south, the Taliban, took the city.',
            y=1996, at='kabul'),
      legacy('The war drained the Soviet Union of money and of faith in its leaders, and helped bring it down. For '
             'Afghanistan it was the start of more than forty years of war. Some of the Arab volunteers who came to '
             'fight the Soviets, among them Osama bin Laden, went on to found al-Qaeda.',
             'Soviet troops invaded in December 1979',
             'Over 5 million Afghans fled abroad',
             'The last Soviet soldiers left in February 1989'),
      war='soviet-afghan-war', wiki='Soviet–Afghan War', at='kabul')

event('iran-iraq-war', 'The Iran-Iraq War', 'war', (1980, 1988),
      'Saddam Hussein attacked revolutionary Iran, hoping for a quick win, and started eight years of trench warfare.',
      scene('Old rivals',
            'Iraq and Iran had long quarrelled over the Shatt al-Arab, the river where the Tigris and Euphrates flow '
            'into the Gulf. In 1979 the revolution in Iran threw its army into chaos, and Ayatollah Khomeini called on '
            'the Shia Muslims of Iraq, a majority there, to rise against their rulers. In Baghdad, Saddam Hussein saw '
            'a threat, and a chance.',
            kick='How it began', y=1979, at='basra'),
      figure('saddam-hussein', 'The invasion',
             'On 22 September 1980 Iraqi planes struck Iranian airfields and Iraqi tanks rolled into Khuzestan, Iran\'s '
             'oil province, where many people speak Arabic. Saddam expected a war of weeks. After a month of street '
             'fighting his troops took the port of Khorramshahr, which Iranians renamed Khuninshahr, the city of '
             'blood.',
             y=1980, at='khorramshahr'),
      turn('Waves of volunteers',
           'Iran answered with huge numbers of volunteers, many of them barely trained teenagers of the Basij militia, '
           'who charged across minefields and into machine-gun fire. In May 1982 Iran took back Khorramshahr and soon '
           'drove the Iraqis out. Khomeini then decided to carry the war into Iraq, and it went on for six more '
           'years.',
           y=1982, at='khorramshahr'),
      scene('Trenches and gas',
            'The front sank into trenches, barbed wire and mud, like the Western Front in the First World War. Iraq '
            'used poison gas again and again against Iranian troops. In the war of the cities the two sides fired '
            'missiles at each other\'s capitals, and families in Tehran and Baghdad slept in shelters.',
            y=1985),
      scene('The tanker war',
            'Both sides attacked oil tankers in the Gulf, and the US Navy began escorting ships through it. In July '
            '1988 an American warship, mistaking an Iranian airliner for an attacking jet, shot it down, killing all '
            '290 people aboard.',
            y=1988),
      cost('Halabja',
           'In March 1988 Iranian troops and Kurdish fighters took Halabja, a Kurdish town inside Iraq. The next day '
           'Iraqi planes dropped poison gas on it, and families died in their homes and in the streets as they ran. '
           'It was part of the Anfal, a campaign in which Saddam\'s forces killed tens of thousands of Iraq\'s Kurds.',
           num='About 5,000', of='people killed by gas in one day', y=1988, at='halabja'),
      figure('ruhollah-khomeini', 'A cup of poison',
             'In July 1988, with his armies worn out, Khomeini accepted a ceasefire called for by the United Nations. '
             'Agreeing to it, he said, was more deadly to him than drinking poison. The guns fell silent on 20 August '
             '1988, with the border where it had been in 1980.',
             y=1988, at='tehran'),
      legacy('The war killed about half a million people, some say twice as many, and left both countries deep in '
             'debt with nothing to show for it. Iraq\'s debts led Saddam to invade Kuwait two years later. In Iran the '
             'war\'s martyrs are still remembered on murals in every town.',
             'Iraq invaded on 22 September 1980',
             'Eight years of war, and no land changed hands',
             'Poison gas killed thousands at Halabja'),
      war='iran-iraq-war', wiki='Iran–Iraq War', at='khorramshahr')

event('falklands-war', 'The Falklands War', 'war', (1982, 1982),
      'Argentina seized Britain\'s islands in the South Atlantic, and Britain sent a fleet across the world to win them back.',
      scene('Las Malvinas',
            'The Falklands, windswept islands in the South Atlantic, had been British since 1833 and were home to '
            'about 1,800 people, most of them of British descent. Argentina, 500 kilometres away, has long claimed '
            'them as Las Malvinas. In 1982 its military rulers, facing anger over a failing economy and the thousands '
            'of people they had made disappear, decided to take them.',
            kick='How it began', y=1982, at='stanley'),
      figure('leopoldo-galtieri', 'Invasion',
             'On 2 April 1982 Argentine troops landed near Stanley, the capital, and after a short fight the small '
             'garrison of Royal Marines surrendered. Huge crowds in Buenos Aires cheered General Galtieri, the head of '
             'the junta. He did not believe Britain would fight for islands so far away.',
             y=1982, at='stanley'),
      figure('margaret-thatcher', 'The task force',
             'Britain\'s prime minister, Margaret Thatcher, decided to fight. Within days a task force set sail, two '
             'small aircraft carriers leading more than a hundred ships, among them cruise liners turned into '
             'troopships, on a voyage of 13,000 kilometres. Talks to find a peace on the way all failed.',
             y=1982, at='london'),
      battle('The Belgrano and the Sheffield',
             'On 2 May a British submarine sank the Argentine cruiser General Belgrano, and 323 of its crew died, '
             'almost half of all the Argentines killed in the war. Two days later an Argentine jet hit the destroyer '
             'HMS Sheffield with an Exocet missile, and it later sank. Argentine pilots, flying low over the waves, '
             'went on to sink five more British ships.',
             y=1982),
      battle('Yomping to Stanley',
             'On 21 May British troops landed at San Carlos, on the far side of East Falkland from Stanley. Most of '
             'their big helicopters had gone down with the ship carrying them, so they crossed the island on foot, '
             'carrying huge loads over bog and rock: the marines called it yomping. They won at Goose Green, then took '
             'the hills around Stanley in night battles.',
             y=1982, at='san_carlos'),
      cost('Seventy-four days',
           'On 14 June, with British troops on the edge of Stanley, the Argentine garrison surrendered, after 74 days '
           'of war. Many of the Argentine dead were young conscripts, cold and hungry in their foxholes. Three '
           'islanders, all women, were killed by a British shell.',
           num='907 dead', of='649 Argentines, 255 British, 3 islanders', y=1982, at='stanley'),
      legacy('Defeat brought down Argentina\'s junta, and democracy returned there in 1983. Victory made Thatcher '
             'hugely popular, and she won the next election by a landslide. Argentina still claims the islands; in a '
             'vote in 2013 all but three of the islanders who voted chose to stay British.',
             'Argentina invaded on 2 April 1982',
             'Britain won the islands back in 74 days',
             'Defeat brought democracy back to Argentina'),
      war='falklands-war', wiki='Falklands War', at='stanley')

event('chernobyl', 'Chernobyl', 'disaster', (1986, 1986),
      'A reactor exploded at a Soviet nuclear power station, in the worst nuclear accident the world has known.',
      scene('A night test',
            'At 1:23 in the morning of 26 April 1986, engineers at the Chernobyl power station in Soviet Ukraine were '
            'running a safety test on reactor number 4. They had switched off safety systems, and the reactor had a '
            'dangerous flaw in its design. Its power suddenly surged. A blast of steam threw off the reactor\'s huge '
            'steel lid, and a second explosion hurled burning fuel into the night.',
            kick='What happened', y=1986, at='chernobyl'),
      scene('The firemen',
            'Firemen from the nearby town of Pripyat climbed onto the roof to fight the flames, with no idea what they '
            'faced. Above the reactor the air glowed, and they said it tasted of metal. Within hours they were '
            'vomiting, and their skin was burning. Two workers died that night, and 28 more of the first men on the '
            'scene died of radiation sickness within weeks.',
            y=1986, at='chernobyl'),
      scene('Pripyat',
            'Pripyat, a new town of about 49,000 people, many of them young families of plant workers, was evacuated '
            'the next afternoon. People were told to pack for three days. They never came back. Today trees grow '
            'through its flats, and the Ferris wheel of its fairground, due to open that May Day, has never turned '
            'for the public.',
            img='Pripyat', y=1986, at='pripyat'),
      turn('Sweden raises the alarm',
           'The Soviet government said nothing. On 28 April alarms went off at the Forsmark nuclear plant in Sweden, '
           'more than 1,000 kilometres away, when workers arrived with radioactive dust on their shoes. Swedish '
           'scientists traced the wind back to the Soviet Union. That evening Soviet television admitted, in a few '
           'seconds on the news, that there had been an accident.',
           y=1986, at='forsmark'),
      scene('The liquidators',
            'About 600,000 soldiers, miners, firemen and reservists, called liquidators, were sent to clean up. '
            'Helicopters dropped thousands of tonnes of sand, lead and boron on the burning reactor. Robots sent onto '
            'the roof broke down in the radiation, so soldiers shovelled the debris off by hand, in shifts of a minute '
            'or two. By November a concrete shell had been built over the ruin.',
            y=1986, at='chernobyl'),
      cost('The cloud',
           'Winds carried radiation across Ukraine, Belarus and Russia and over much of Europe. A zone 30 kilometres '
           'round the plant was emptied, and thousands of children who drank tainted milk later got thyroid cancer. '
           'How many will die of it in the end is still argued over: estimates run from 4,000 to tens of thousands.',
           num='About 350,000', of='people moved from their homes for good', y=1986),
      figure('mikhail-gorbachev', 'The real cause',
             'The disaster, and the first attempts to hide it, shook Mikhail Gorbachev\'s faith in the Soviet system '
             'and pushed him towards glasnost, openness. Twenty years later he wrote that Chernobyl, even more than his '
             'own reforms, was perhaps the real cause of the collapse of the Soviet Union.',
             y=1986, at='moscow'),
      legacy('Chernobyl is the worst nuclear accident in history. It turned many people around the world against '
             'nuclear power, and showed that the Soviet system could not be trusted to tell the truth. In 2016 a giant '
             'steel arch was slid over the old concrete shell, to keep the ruin safe for a hundred years.',
             'Reactor 4 exploded on 26 April 1986',
             'About 350,000 people lost their homes',
             'Pripyat has stood empty ever since'),
      states=('USSR', 'Ukraine'), wiki='Chernobyl disaster', at='chernobyl')

event('tiananmen', 'Tiananmen Square, 1989', 'uprising', (1989, 1989),
      'Students filled the great square in Beijing to call for freedom, until the army cleared it on the night of 3 June.',
      scene('Mourning Hu Yaobang',
            'In April 1989 Hu Yaobang died, a Communist Party leader who had been pushed out for being too soft on '
            'students calling for reform. Students gathered in Tiananmen Square, the vast square at the heart of '
            'Beijing, to mourn him, and stayed. They called for free speech, an end to corruption, and a say in how '
            'China was run.',
            kick='How it began', y=1989, at=TIAN, where='Tiananmen Square'),
      scene('A million people',
            'The protests grew into the largest in the history of Communist China. In May thousands of students went '
            'on hunger strike, and up to a million people filled the square and the streets around it. Workers joined '
            'them, and protests spread to hundreds of cities. The Soviet leader Mikhail Gorbachev came on a state '
            'visit, and his welcome had to be moved to the airport.',
            y=1989, at=TIAN, where='Tiananmen Square'),
      figure('deng-xiaoping', 'Martial law',
             'The party\'s leaders were split. Zhao Ziyang, the party chief, went to the square and told the hunger '
             'strikers, with tears in his eyes, that he had come too late. Deng Xiaoping, China\'s most powerful man, '
             'sided with the hardliners, and on 20 May martial law was declared. When soldiers first tried to march in, '
             'crowds of ordinary Beijingers blocked their way.',
             y=1989, at='beijing'),
      work('The Goddess of Democracy',
           'Art students built a statue ten metres tall, of foam and papier-mâché on a metal frame: a woman holding up '
           'a torch with both hands. They set her up facing the giant portrait of Mao on the Gate of Heavenly Peace. '
           'She stood for five days.',
           img='Goddess of Democracy', y=1989, at=TIAN, where='Tiananmen Square'),
      cost('The night of 3 June',
           'On the night of 3 to 4 June the army moved in with tanks and live ammunition. Most of the killing was in '
           'the streets leading to the square, where soldiers fired on crowds trying to stop them. By dawn the square '
           'was cleared. China has never said how many died; estimates run from several hundred to several thousand.',
           num='Hundreds or thousands', of='killed; the true number is still secret', y=1989, at='beijing'),
      tale('Tank Man',
           'On 5 June a man in a white shirt, carrying shopping bags, stepped in front of a column of tanks on the '
           'Avenue of Eternal Peace. When the first tank tried to go round him, he moved to block it again, and '
           'climbed up to speak to the crew. Then onlookers pulled him away. No one knows who he was, or what became '
           'of him.',
           y=1989, at='beijing'),
      scene('Silence',
            'The government hunted down the protest leaders. Some escaped abroad; others went to prison. Zhao Ziyang '
            'spent his last fifteen years under house arrest. In China the events are still censored, and many young '
            'Chinese have never seen the pictures. Hong Kong held huge candlelit vigils every June, until they were '
            'banned in 2020.',
            y=1990, at='beijing'),
      legacy('Tiananmen ended hopes of political reform in China. The Communist Party kept total control and offered '
             'growing wealth instead, and China became the world\'s second largest economy. In Eastern Europe 1989 '
             'ended very differently: within months, its communist governments fell almost without a shot.',
             'Students filled the square from April 1989',
             'The army cleared it on the night of 3 June',
             'The events are still censored in China'),
      states=('China',), wiki='1989 Tiananmen Square protests and massacre', at=TIAN, where='Tiananmen Square',
      label='Protest')

event('revolutions-of-1989', 'The revolutions of 1989', 'revolution', (1989, 1989),
      'One after another, the communist governments of Eastern Europe fell in a single year, almost without a shot.',
      figure('lech-waesa', 'Solidarity',
             'In 1980 workers at the Lenin Shipyard in Gdańsk, led by an electrician named Lech Wałęsa, went on strike '
             'and won the right to form Solidarity, the first free trade union in the Soviet bloc. Ten million Poles '
             'joined. The government crushed it under martial law in 1981, but it lived on underground, with the '
             'support of the Polish pope, John Paul II.',
             kick='How it began', y=1980, at='gdansk'),
      figure('mikhail-gorbachev', 'No more tanks',
             'Soviet tanks had crushed earlier revolts in Eastern Europe: East Germany in 1953, Hungary in 1956, '
             'Czechoslovakia in 1968. Mikhail Gorbachev made it clear that this time they would not come. His '
             'spokesman joked that the old rule had given way to the Sinatra Doctrine: each country could now do it '
             'its way.',
             y=1989, at='moscow'),
      turn('Poland votes',
           'Early in 1989 Poland\'s communists, with the economy in ruins, sat down with Solidarity at a round table '
           'and agreed to a partly free election. On 4 June, the day the tanks rolled into Tiananmen Square, '
           'Solidarity won all but one of the seats it was allowed to fight. By September Poland had a non-communist '
           'prime minister, the first in the Soviet bloc in forty years.',
           y=1989, at='warsaw'),
      tale('The picnic',
           'In May Hungary began cutting down the barbed-wire fence on its border with Austria. In August, at a picnic '
           'for peace on the border, a gate was opened for a few hours, and hundreds of East Germans on holiday ran '
           'through it to the West. In September Hungary opened the border for good, and tens of thousands followed.',
           y=1989, at='sopron'),
      turn('The Wall opens',
           'In East Germany crowds marched every Monday in Leipzig, chanting we are the people. On 9 November a '
           'muddled official announced on live television that East Germans could travel freely, starting at once. '
           'That night thousands surged to the Berlin Wall, the guards opened the gates, and Berliners from both '
           'sides danced on top of it.',
           img='Fall of the Berlin Wall', y=1989, at='berlin'),
      figure('vaclav-havel', 'The Velvet Revolution',
             'In Prague police beat up a student march on 17 November. Within days hundreds of thousands filled '
             'Wenceslas Square each evening, jingling their keys to tell the communists it was time to go. Václav '
             'Havel, a playwright jailed again and again for his writing, led the protests. By the end of December he '
             'was president.',
             y=1989, at='prague'),
      figure('nicolae-ceausescu', 'Romania',
             'Only in Romania was the end bloody. On 21 December the dictator Nicolae Ceaușescu spoke to a crowd in '
             'Bucharest, and it began to boo him, live on television. The next day he fled by helicopter but was '
             'caught, and on Christmas Day he and his wife Elena were tried in less than an hour and shot. Over a '
             'thousand people died in the fighting.',
             y=1989, at='bucharest'),
      legacy('In one year the communist rule that Soviet tanks had imposed on Eastern Europe after 1945 fell apart, '
             'almost without bloodshed. Germany was reunited in 1990, and within two years the Soviet Union itself was '
             'gone. Most of the countries freed in 1989 later joined the European Union and NATO.',
             'Poland voted freely on 4 June 1989',
             'The Berlin Wall opened on 9 November',
             'Six communist governments fell in a year'),
      states=('Poland', 'Hungary', 'Czechoslovakia', 'East Germany', 'Bulgaria', 'Romania', 'Czech Republic',
              'Slovakia'),
      wiki='Revolutions of 1989', at='berlin')

event('fall-of-the-soviet-union', 'The end of the Soviet Union', 'fall', (1989, 1991),
      'The world\'s largest country broke into fifteen in 1991, almost without a shot, and the Cold War was over.',
      scene('Fifteen republics',
            'The Soviet Union was made up of fifteen republics, from Estonia on the Baltic to Kazakhstan in Central '
            'Asia, home to over a hundred peoples, all ruled from Moscow. When Gorbachev\'s openness let people speak '
            'freely, old wounds came out: the famine in Ukraine, Stalin\'s deportations, the seizure of the Baltic '
            'states in 1940. And the shops were empty.',
            kick='How it began', y=1988, at='moscow'),
      scene('The Baltic Way',
            'On 23 August 1989, fifty years after Hitler and Stalin secretly agreed to divide Eastern Europe between '
            'them, about two million Estonians, Latvians and Lithuanians joined hands in a human chain 675 kilometres '
            'long, from Tallinn through Riga to Vilnius, to demand their freedom.',
            img='Baltic Way', y=1989, at='riga'),
      turn('The television tower',
           'In March 1990 Lithuania declared itself independent, the first republic to break away. In January 1991 '
           'Soviet troops stormed the television tower in Vilnius, and 14 people were killed as unarmed crowds tried '
           'to block the tanks. Instead of crushing the Baltic peoples, the attack hardened them, and Moscow drew '
           'back.',
           y=1991, at='vilnius'),
      figure('boris-yeltsin', 'On the tank',
             'In August 1991 hardliners in Moscow, afraid the union was about to break up, held Gorbachev prisoner at '
             'his holiday home in Crimea and sent tanks into the capital. Boris Yeltsin, the elected president of '
             'Russia, climbed onto a tank outside the parliament and called on the people to resist. Crowds built '
             'barricades, soldiers would not shoot, and in three days the coup collapsed.',
             y=1991, at='moscow'),
      turn('Ukraine says yes',
           'After the coup the republics declared independence one after another. The decisive vote came on 1 '
           'December 1991, when more than 90 per cent of Ukrainians chose independence. A week later the leaders of '
           'Russia, Ukraine and Belarus met at a hunting lodge in a Belarusian forest and signed a paper saying that '
           'the Soviet Union had ceased to exist.',
           y=1991, at='viskuli', where='Belovezha Forest'),
      figure('mikhail-gorbachev', 'The red flag comes down',
             'On 25 December 1991 Gorbachev resigned in a short speech on television. That evening the red Soviet flag '
             'over the Kremlin was lowered for the last time, and the white, blue and red flag of Russia raised in its '
             'place. The next day the Soviet parliament voted the union out of existence.',
             y=1991, at='moscow'),
      scene('Hard years',
            'In Russia prices soared as the old system was scrapped, and people\'s savings vanished. Pensioners sold '
            'their belongings in the street, and life expectancy for Russian men fell below 58. A few well-connected '
            'men, the oligarchs, bought up the country\'s oil and metals for a fraction of their worth. Wars broke out '
            'in Chechnya, Georgia, Moldova and Tajikistan, and between Armenia and Azerbaijan.',
            y=1994, at='moscow'),
      legacy('The end of the Soviet Union finished the Cold War and left hundreds of millions of people free to choose '
             'their own way, with less bloodshed than anyone had feared. Vladimir Putin later called it the '
             'greatest geopolitical catastrophe of the century. Many of its quarrels, above all between Russia and '
             'Ukraine, were never settled.',
             'Fifteen countries were born from one',
             'The August coup collapsed in three days',
             'The red flag came down on 25 December 1991'),
      states=('USSR', 'Russia', 'Ukraine', 'Estonia', 'Latvia', 'Lithuania', 'Georgia', 'Armenia', 'Azerbaijan',
              'Moldova', 'Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Kyrgyzstan', 'Tajikistan'),
      wiki='Dissolution of the Soviet Union', at='moscow')

event('apartheid', 'Apartheid and its end', 'change', (1948, 1994),
      'For nearly fifty years South Africa\'s white rulers kept its peoples apart by law, until Mandela walked free.',
      scene('Apartness',
            'In 1948 the National Party won an election in which nearly all the voters were white, and began building '
            'apartheid, Afrikaans for apartness. Every South African was classed by race: white, coloured, Indian or '
            'Black. Marriage between races was banned, and towns were carved up so that each race lived apart, with '
            'the best land kept for whites.',
            kick='How it began', y=1948, at='pretoria'),
      figure('hendrik-verwoerd', 'Grand apartheid',
             'Hendrik Verwoerd, the system\'s chief architect and prime minister from 1958, planned to strip Black '
             'South Africans of their citizenship, making them citizens of homelands, scattered patches of poor land. '
             'Over the years more than three million people were forced from their homes. Black schools, he said, should not teach '
             'children to hope for more than certain kinds of labour.',
             y=1958, at='pretoria'),
      cost('Sharpeville',
           'On 21 March 1960 a crowd gathered outside the police station at Sharpeville to protest against the pass '
           'laws, which forced Black people to carry papers at all times. The police opened fire, and many were shot '
           'in the back as they ran. The government banned the African National Congress, and its '
           'leaders went underground.',
           num='69', of='protesters shot dead by the police', y=1960, at='sharpeville'),
      figure('nelson-mandela', 'Robben Island',
             'Nelson Mandela, who had helped set up the ANC\'s armed wing, was sentenced to life in prison in 1964 and '
             'spent 18 years on Robben Island, breaking rocks in a quarry. Cut off from the world, he became its most '
             'famous prisoner, though his picture could not even be printed in South African newspapers.',
             y=1964, at='robben_island'),
      turn('Soweto',
           'On 16 June 1976 thousands of schoolchildren in Soweto marched against being taught in Afrikaans, the '
           'language of their rulers. The police opened fire. A photograph of a dying 12-year-old boy, Hector '
           'Pieterson, carried by an older student while his sister ran beside them, went around the world. Hundreds '
           'were killed in the risings that followed.',
           y=1976, at='soweto'),
      scene('A world boycott',
            'In the 1980s the townships rose in revolt, and the government ruled by emergency laws, jailing thousands '
            'without trial. Around the world people refused to buy South African goods, banks pulled out their money, '
            'and its teams were banned from the Olympics and most world sport. Songs and concerts demanded Mandela\'s '
            'freedom.',
            y=1985, at='johannesburg'),
      figure('f-w-de-klerk', 'Free',
             'In 1989 F. W. de Klerk became president and decided that apartheid had to end. On 2 February 1990 he '
             'lifted the ban on the ANC, and nine days later Mandela walked out of prison, after 27 years. The two men '
             'then negotiated a new constitution, through years of violence that killed thousands, and in 1993 they '
             'shared the Nobel Peace Prize.',
             y=1990, at='cape_town'),
      turn('Freedom Day',
           'On 27 April 1994 South Africans of every race voted together for the first time. Queues stretched for '
           'kilometres, and some people waited all day to cast the first vote of their lives. The ANC won, and on 10 '
           'May Mandela was sworn in as president. 27 April is now Freedom Day.',
           y=1994, at='pretoria'),
      legacy('Apartheid ended without the civil war many had feared. A Truth and Reconciliation Commission, led by '
             'Archbishop Desmond Tutu, let victims tell their stories and offered amnesty to those who confessed their '
             'crimes. But apartheid\'s mark remains: South Africa is still one of the most unequal countries on earth.',
             'Apartheid became law in 1948',
             'Mandela was freed in 1990, after 27 years',
             'All races voted together in April 1994'),
      states=('South Africa',), wiki='Apartheid', at='pretoria', label='Freedom struggle')

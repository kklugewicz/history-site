from _lib import event, scene, battle, turn, figure, cost, made, work, song, tale, legacy

event('gulf-war', 'The Gulf War', 'war', (1990, 1991),
      'Saddam Hussein seized Kuwait in two days, and a coalition of dozens of nations drove him out in a hundred hours.',
      scene('Debts and oil',
            'Iraq came out of its war with Iran owing tens of billions of dollars, much of it to Kuwait, its small, '
            'rich neighbour. Saddam Hussein accused Kuwait of pumping too much oil, which kept prices low, and of '
            'stealing Iraqi oil by drilling at a slant under the border. He also said Kuwait was rightly part of Iraq.',
            kick='How it began', y=1990, at='kuwait'),
      figure('saddam-hussein', 'Iraq takes Kuwait',
             'Before dawn on 2 August 1990 Iraqi tanks crossed the border, and within two days Iraq held all of '
             'Kuwait. The emir escaped to Saudi Arabia. Saddam declared Kuwait the nineteenth province of Iraq, his '
             'soldiers looted it, and his army now stood on the border of Saudi Arabia, which held a quarter of the '
             'world\'s oil.',
             y=1990, at='kuwait'),
      figure('george-h-w-bush', 'This will not stand',
             'President George H. W. Bush declared that the invasion would not stand. The United Nations put Iraq '
             'under sanctions and gave it until 15 January 1991 to leave. The United States built a coalition of '
             'dozens of countries, among them Arab states such as Saudi Arabia, Egypt and Syria, and over half a '
             'million American troops gathered in the Saudi desert.',
             y=1990, at='washington'),
      battle('Desert Storm',
             'On 17 January 1991 the coalition began to bomb Iraq, and for the first time the world watched a war live '
             'on television, as tracer fire lit up the night sky over Baghdad. Guided bombs and cruise missiles smashed '
             'air defences, bridges and power stations. Iraq fired Scud missiles at Israel, hoping to draw it in and '
             'split the coalition, but Israel held back.',
             y=1991, at='baghdad'),
      battle('A hundred hours',
             'On 24 February the ground war began. While Iraq waited for an attack from the sea and straight into '
             'Kuwait, the main coalition armies swung far out into the desert and hooked round behind them. Iraqi '
             'soldiers surrendered in their tens of thousands. After a hundred hours Bush called a halt, and Kuwait '
             'was free.',
             y=1991, at='kuwait'),
      cost('The burning wells',
           'As they retreated, Iraqi troops set fire to Kuwait\'s oil wells. The smoke turned day into night, and '
           'fire-fighting teams from around the world took until November to put the last one out. Millions of '
           'barrels of oil were also poured into the Gulf, coating beaches and killing seabirds.',
           num='Over 600', of='oil wells set on fire', y=1991, at='kuwait'),
      scene('Saddam stays',
            'The coalition stopped short of Baghdad. Bush urged Iraqis to rise up, and Shia Arabs in the south and '
            'Kurds in the north did, but Saddam\'s helicopters and tanks crushed them, and over a million Kurds fled '
            'into the mountains. Iraq lived under UN sanctions for the next twelve years.',
            y=1991, at='basra'),
      legacy('The Gulf War showed the power of America\'s new weapons, and seemed to promise a world where nations '
             'would stand together against aggression. But Saddam stayed in power, and American troops stayed in '
             'Saudi Arabia, which enraged Osama bin Laden. The war\'s unfinished business led to the Iraq War of 2003.',
             'Iraq invaded Kuwait on 2 August 1990',
             'The ground war lasted a hundred hours',
             'Kuwait\'s oil wells burned for months'),
      war='gulf-war', wiki='Gulf War', at='kuwait')

event('rwandan-genocide', 'The Rwandan genocide', 'genocide', (1990, 1994),
      'In a hundred days of 1994 Hutu extremists murdered about 800,000 people, most of them Tutsi, as the world looked on.',
      scene('Hutu and Tutsi',
            'Most Rwandans were Hutu; about one in seven were Tutsi. Belgian rulers had favoured the Tutsi and made '
            'everyone carry an identity card naming their group. After independence Hutu governments took power, and '
            'waves of violence drove hundreds of thousands of Tutsi abroad. In 1990 Tutsi exiles of the Rwandan '
            'Patriotic Front invaded from Uganda.',
            kick='How it began', y=1990),
      scene('Hate on the radio',
            'As the war went on, extremists close to the government armed and trained militias called the '
            'Interahamwe, those who attack together, and a radio station, RTLM, poured out hatred, calling Tutsi '
            'inyenzi, cockroaches. In 1993 the government and the rebels signed a peace deal at Arusha, and UN '
            'peacekeepers arrived to watch over it.',
            y=1993, at='kigali'),
      figure('juvenal-habyarimana', 'The plane',
             'On the evening of 6 April 1994 the plane carrying President Juvénal Habyarimana was shot down as it came '
             'in to land at Kigali, killing everyone aboard. Who fired the missiles is still disputed. Within hours '
             'soldiers and militias set up roadblocks and began to kill, working from lists of Tutsi and of Hutu who '
             'opposed them.',
             y=1994, at='kigali'),
      cost('A hundred days',
           'For about a hundred days neighbours killed neighbours, mostly with machetes and clubs. People who fled to '
           'churches, schools and stadiums were massacred there by the thousand, and militias checked identity cards '
           'at roadblocks. Hundreds of thousands of women were raped. Some Hutu hid Tutsi at the risk of their lives.',
           num='About 800,000', of='people murdered, most of them Tutsi', y=1994),
      scene('The world looks away',
            'The UN commander, General Roméo Dallaire of Canada, had warned in January that a slaughter was being '
            'planned, but was told not to act. After ten Belgian peacekeepers were murdered, most of his force was '
            'pulled out. The world\'s powers even avoided the word genocide, which would have obliged them to act.',
            y=1994, at='kigali'),
      figure('paul-kagame', 'The killing stops',
             'The genocide ended only as the Rwandan Patriotic Front, led by Paul Kagame, fought its way across the '
             'country. It took Kigali on 4 July, now Liberation Day, and its soldiers also carried out revenge killings. '
             'Fearing reprisals, about two million Hutu, among them many of the killers, fled abroad, most into Zaire, '
             'where cholera swept the refugee camps.',
             y=1994, at='goma'),
      scene('Justice',
            'A UN court in Tanzania tried the leaders, and in 1998 it gave the first verdict of genocide ever reached '
            'by an international court. In Rwanda, with its prisons overflowing, village courts called gacaca, '
            'meeting on the grass, heard almost two million cases. Many killers now live beside the families of the '
            'people they killed.',
            y=1998, at='arusha'),
      legacy('Rwanda has rebuilt itself, and is now one of Africa\'s safest and fastest-growing countries, though '
             'Kagame rules it tightly and critics are silenced. The genocide shamed the world that stood by. The Hutu '
             'militias who fled into Zaire helped set off wars in Congo that killed millions more.',
             'The killing began on 7 April 1994',
             'About 800,000 murdered in a hundred days',
             'UN peacekeepers were pulled out'),
      war='rwandan-civil-war', wiki='Rwandan genocide', at='kigali')

event('yugoslav-wars', 'The Yugoslav Wars', 'wars', (1991, 2001),
      'As Yugoslavia broke apart, its peoples fought the worst wars Europe had seen since 1945.',
      scene('Tito\'s Yugoslavia',
            'Yugoslavia, the land of the South Slavs, joined together Serbs, Croats, Bosnian Muslims, Slovenes, '
            'Macedonians, Montenegrins and Albanians. Its communist leader, Tito, held it together for 35 years. After '
            'he died in 1980 the economy faltered, and politicians in each republic began to stir up fear of the '
            'others.',
            kick='How it began', y=1980, at='belgrade'),
      figure('slobodan-milosevic', 'Serbia first',
             'Slobodan Milošević rose to power in Serbia by stirring up Serb anger. In 1989, on the 600th anniversary '
             'of the battle of Kosovo, he spoke to a vast crowd of Serbs on the old battlefield and warned that armed '
             'battles could not be ruled out. Croats, Slovenes and others heard a threat.',
             y=1989, at='kosovo_polje', where='Gazimestan, Kosovo'),
      battle('Vukovar',
             'In June 1991 Slovenia and Croatia declared independence. Slovenia was free after a war of ten days, but '
             'in Croatia, where many Serbs lived, the Yugoslav army and Serb rebels seized nearly a third of the '
             'country. The town of Vukovar was shelled to ruins for three months, and when it fell some 200 men were '
             'taken from its hospital and shot.',
             y=1991, at='vukovar'),
      battle('The siege of Sarajevo',
             'When Bosnia voted for independence in 1992, Bosnian Serb forces under Radovan Karadžić and General Ratko '
             'Mladić surrounded its capital, Sarajevo. For almost four years, the longest siege of a capital in modern '
             'times, snipers and shells killed people queuing for bread and water. More than 10,000 people died, among '
             'them over 1,500 children.',
             y=1992, at='sarajevo'),
      scene('Ethnic cleansing',
            'Across Bosnia armed men drove people of other groups out of their homes, burned their villages, and held '
            'prisoners in camps where many were tortured and killed. A new phrase, ethnic cleansing, entered the '
            'language. Serb forces did most of it, but Croat and Bosnian Muslim forces committed crimes too. About '
            '100,000 people died in Bosnia, and two million fled.',
            y=1993),
      cost('Srebrenica',
           'In July 1995 Mladić\'s troops overran Srebrenica, a town the UN had declared a safe area, guarded by a '
           'few hundred lightly armed Dutch peacekeepers. The women and children were bused away. Over a few days the '
           'men and boys were murdered and buried in mass graves. International judges ruled it genocide.',
           num='Over 8,000', of='Muslim men and boys murdered', y=1995, at='srebrenica'),
      turn('Dayton',
           'After Srebrenica, and a shell that killed dozens in a Sarajevo market, NATO bombed the Bosnian Serbs, '
           'while Croatia\'s army swept back through its lost lands and some 200,000 Serbs fled. In November 1995 '
           'the leaders met at an air base in Dayton, Ohio, and agreed to keep Bosnia one country, split into two '
           'parts.',
           y=1995, at='dayton'),
      battle('Kosovo',
             'In 1998 war came to Kosovo, a province of Serbia where most people were Albanian. As Serb forces drove '
             'out hundreds of thousands of Albanians, NATO bombed Serbia for 78 days in 1999, until Milošević pulled '
             'his troops out. In 2000 he was overthrown by his own people, and in 2008 Kosovo declared independence.',
             y=1999, at='kosovo'),
      legacy('Seven countries, counting Kosovo, now stand where Yugoslavia was. The wars killed about 130,000 people '
             'and brought words like genocide and concentration camp back to Europe. A UN court in The Hague tried '
             'their leaders: Milošević died during his trial, and Karadžić and Mladić were jailed for life.',
             'Yugoslavia broke apart from 1991',
             'Over 8,000 were murdered at Srebrenica',
             'Their leaders were tried in The Hague'),
      states=('Slovenia', 'Macedonia'), war='yugoslav-wars', wiki='Yugoslav Wars', at='sarajevo')

event('september-11', 'The September 11 attacks', 'crisis', (2001, 2001),
      'Nineteen hijackers flew planes into the World Trade Center and the Pentagon, and changed the world in a morning.',
      scene('Four planes',
            'On the morning of 11 September 2001, 19 men of al-Qaeda, a terrorist group led by Osama bin Laden, '
            'hijacked four airliners soon after they took off from airports in the eastern United States. Some had '
            'trained as pilots in America. Armed with knives and box cutters, they took the controls, to turn planes '
            'full of fuel into weapons.',
            kick='That morning', y=2001),
      turn('The towers',
           'At 8:46 the first plane hit the North Tower of the World Trade Center in New York, and at 9:03 the second '
           'hit the South Tower, as millions watched on live television. People trapped above the fires waved from '
           'the windows. Within two hours both towers, 110 storeys tall, had collapsed in clouds of dust, killing '
           'thousands, among them 343 firefighters.',
           y=2001, at='ground_zero', where='The World Trade Center'),
      scene('The Pentagon and Flight 93',
            'At 9:37 a third plane hit the Pentagon, the headquarters of the US military, near Washington. On the '
            'fourth, United 93, passengers and crew learned by phone what had happened to the others, and fought back. '
            'The plane crashed into a field in Pennsylvania, short of its target in Washington. All 40 passengers and '
            'crew died.',
            y=2001, at='shanksville'),
      cost('The dead',
           'The dead were office workers and cleaners, passengers, firefighters and police, and they came from more '
           'than 90 countries. Thousands of the people who worked for months in the dust at Ground Zero later fell '
           'ill, and many have since died.',
           num='2,977', of='people killed in a single morning', y=2001, at='ground_zero',
           where='The World Trade Center'),
      figure('george-w-bush', 'A war on terror',
             'President George W. Bush declared a war on terror. NATO, for the first and only time, invoked its rule '
             'that an attack on one member is an attack on all. When the Taliban, who ruled Afghanistan, refused to '
             'hand over bin Laden, America and its allies attacked them in October 2001.',
             y=2001, at='washington'),
      scene('A changed world',
            'Airports brought in strict security checks. The United States opened a prison for terror suspects at '
            'Guantánamo Bay, and new laws let the government watch people more closely. Muslims in the West faced '
            'suspicion and attacks. Within two years America was at war in Iraq too.',
            y=2002),
      legacy('September 11 was the deadliest terrorist attack in history. It drew the United States into wars in '
             'Afghanistan and Iraq that lasted twenty years. Bin Laden was found and killed in Pakistan in 2011. Where '
             'the towers stood, two pools now fill their footprints, with the names of the dead cut around them.',
             'Four planes were hijacked on 11 September 2001',
             '2,977 people were killed',
             'It led to the war in Afghanistan'),
      states=('United States', 'Afghanistan'), wiki='September 11 attacks', at='ground_zero',
      where='The World Trade Center', label='Attack')

event('war-in-afghanistan', 'The war in Afghanistan', 'war', (2001, 2021),
      'After 9/11 America and its allies drove out the Taliban. Twenty years later they left, and the Taliban came back.',
      scene('The Taliban',
            'The Taliban, a movement of religious students that had taken Kabul in 1996, ruled most of Afghanistan by '
            'their strict reading of Islamic law. Girls were barred from school, music and television were banned, '
            'and thieves had their hands cut off. They gave a home to Osama bin Laden, and after 11 September they '
            'refused to hand him over.',
            kick='How it began', y=2001, at='kandahar'),
      battle('The Taliban fall',
             'From 7 October 2001 American and British planes bombed the Taliban, while a few hundred American special '
             'forces, some of them on horseback, rode with the Afghan fighters of the Northern Alliance. Kabul fell on '
             '13 November, and Kandahar in December. Bin Laden slipped away from the caves of Tora Bora into Pakistan.',
             y=2001, at='tora_bora'),
      figure('hamid-karzai', 'A new Afghanistan',
             'Hamid Karzai became the head of a new government, and in 2004 he was elected president. Girls went back '
             'to school, millions of refugees came home, and women sat in parliament. But the new state was riddled '
             'with corruption, and the NATO troops sent to keep the peace, from about fifty countries, were spread '
             'thin.',
             y=2004, at='kabul'),
      scene('The Taliban return',
            'From 2006 the Taliban came back, from safe havens across the border in Pakistan, with roadside bombs and '
            'suicide attacks. In 2009 President Barack Obama sent 30,000 more soldiers, bringing American forces to '
            'about 100,000, but the Taliban could not be beaten. In 2011 bin Laden was found and killed in Pakistan.',
            y=2009, at='kandahar'),
      cost('Twenty years',
           'About 2,400 American soldiers died, and over 1,100 from allied countries, 457 of them British. Some '
           '69,000 Afghan soldiers and police were killed, and over 50,000 Taliban and other fighters. Most painful of '
           'all, more than 46,000 Afghan civilians died in air strikes, bombings and crossfire.',
           num='About 176,000', of='killed, 46,000 of them civilians', y=2021),
      turn('The deal at Doha',
           'In February 2020 the United States signed a deal with the Taliban in Doha, in Qatar, promising to '
           'withdraw all its troops. The Afghan government was left out of the talks. President Joe Biden kept to '
           'it, and in May 2021 the last soldiers began to leave.',
           y=2020, at='doha'),
      turn('The fall of Kabul',
           'As the troops left, the Afghan army collapsed. On 15 August 2021 President Ashraf Ghani fled, and the '
           'Taliban walked into Kabul. Thousands of desperate Afghans crowded the airport, and some clung to the side '
           'of an American plane as it took off. A suicide bomber killed over 180 people at the gates. On 30 August '
           'the last American soldier left.',
           y=2021, at='kabul'),
      legacy('America\'s longest war ended where it began, with the Taliban in power. They have again shut girls out '
             'of school after the age of twelve and banned women from most work, making Afghanistan the only country '
             'in the world where girls cannot go to secondary school.',
             'Began in October 2001, after 9/11',
             'Twenty years, and about 176,000 dead',
             'The Taliban took Kabul again in 2021'),
      war='war-in-afghanistan', wiki='War in Afghanistan (2001–2021)', at='kabul')

event('iraq-war', 'The Iraq War', 'war', (2003, 2011),
      'America and Britain invaded Iraq to destroy weapons that turned out not to exist, and set off years of bloodshed.',
      figure('tony-blair', 'The case for war',
             'After 11 September, President George W. Bush and the British prime minister, Tony Blair, argued that '
             'Saddam Hussein was hiding chemical and biological weapons and might give them to terrorists. UN '
             'inspectors searched and found none. Millions marched against war in cities around the world, but in '
             'March 2003 America and Britain invaded without the UN\'s approval.',
             kick='How it began', y=2003, at='london'),
      battle('Shock and awe',
             'The invasion began on 20 March 2003. As bombs and missiles lit up Baghdad, American and British armies '
             'raced north from Kuwait, and the British took Basra. Baghdad fell in three weeks. On 9 April a crowd, '
             'helped by American Marines with an armoured vehicle, pulled down a giant statue of Saddam.',
             y=2003, at='baghdad'),
      turn('Mission accomplished',
           'On 1 May Bush declared the end of major combat, standing on an aircraft carrier beneath a banner that '
           'read Mission Accomplished. But there was no plan for what came next. The Americans disbanded Iraq\'s army '
           'and sacked members of Saddam\'s party, leaving hundreds of thousands of angry men without work. No weapons '
           'of mass destruction were ever found.',
           y=2003),
      figure('saddam-hussein', 'A dictator\'s end',
             'Saddam was found in December 2003, hiding in a hole in the ground near his home town of Tikrit. An Iraqi '
             'court sentenced him to death for the killing of 148 men from the town of Dujail, and he was hanged on 30 '
             'December 2006.',
             y=2006, at='tikrit'),
      cost('Civil war',
           'Insurgents, from Saddam\'s old officers to al-Qaeda in Iraq, fought the Americans with roadside bombs. In '
           '2006 al-Qaeda blew up the golden-domed Shia shrine at Samarra, and Iraq slid into a civil war between '
           'Sunni and Shia. Photographs of prisoners abused by American guards at Abu Ghraib shocked the world.',
           num='Hundreds of thousands', of='of Iraqis died; no count is agreed', y=2006, at='samarra'),
      turn('The surge',
           'In 2007 Bush sent 30,000 more troops under General David Petraeus, and many Sunni tribes, sick of '
           'al-Qaeda\'s brutality, turned against it. The killing fell sharply. Iraqis voted in elections, and in '
           'December 2011 the last American troops left. Nearly 4,500 of them had died.',
           y=2007, at='baghdad'),
      legacy('The war ended the rule of a dictator who had killed hundreds of thousands of his own people, and '
             'Iraqis now vote for their leaders. But the weapons it was fought over did not exist, and its chaos gave '
             'birth to the Islamic State, which in 2014 seized Mosul and a third of Iraq. It also made Iran far '
             'more powerful in the region.',
             'The invasion began on 20 March 2003',
             'No weapons of mass destruction were found',
             'The last US troops left in December 2011'),
      war='iraq-war', wiki='Iraq War', at='baghdad')

event('indian-ocean-tsunami', 'The 2004 tsunami', 'disaster', (2004, 2004),
      'One of the strongest earthquakes ever recorded sent waves across the Indian Ocean, killing about 230,000 people.',
      scene('The earthquake',
            'At 7:58 in the morning of 26 December 2004 the seabed off the Indonesian island of Sumatra split along a '
            'crack more than 1,000 kilometres long, in an earthquake of magnitude 9.1, one of the strongest ever '
            'recorded. The sea floor heaved upwards, lifting the ocean above it. The whole planet shook.',
            kick='What happened', y=2004),
      scene('Aceh',
            'Within about twenty minutes, waves up to 30 metres high struck Aceh, at the northern tip of Sumatra. In '
            'the city of Banda Aceh the water swept kilometres inland, carrying a power-station ship into the town. In '
            'Indonesia alone around 167,000 people died, and whole villages along the coast vanished.',
            y=2004, at='banda_aceh'),
      scene('Across the ocean',
            'The waves raced across the ocean at the speed of a jet. Two hours later they hit Sri Lanka and the east '
            'coast of India, where no one had warned anyone; in Sri Lanka one wave wrecked a crowded train, killing '
            'more than a thousand people. They hit Thai beaches full of holidaymakers, and seven hours later reached '
            'Somalia, 5,000 kilometres away.',
            y=2004, at='colombo'),
      tale('A geography lesson',
           'On a beach in Thailand a ten-year-old British girl, Tilly Smith, saw the sea suddenly pull back and froth. '
           'She had learned about tsunamis in a geography lesson two weeks before, and told her parents. The beach was '
           'cleared, and about a hundred people were saved.',
           y=2004, at='phuket'),
      tale('The smong',
           'On Simeulue, an island close to the earthquake, people had passed down stories of the smong, a great wave '
           'that struck in 1907. When the sea drew back, they ran for the hills. Of some 78,000 islanders, only seven '
           'died.',
           y=2004, at='simeulue'),
      cost('Fourteen countries',
           'It was the deadliest tsunami in recorded history, and a third of the dead were children. Thousands of '
           'tourists from Europe died too. More than a million and a half people lost their homes, and the world gave '
           'billions of dollars in aid.',
           num='About 230,000', of='killed in fourteen countries', y=2004),
      turn('Peace in Aceh',
           'In Aceh rebels had been fighting the Indonesian army for nearly thirty years. The disaster brought both '
           'sides to talks, and in August 2005 they signed a peace that has held ever since.',
           y=2005, at='banda_aceh'),
      made('A warning system',
           'In 2004 the Indian Ocean had no tsunami warning system. Scientists in Hawaii saw the earthquake, but had '
           'no way to warn the people in the waves\' path.',
           'Today sea-floor sensors, buoys and sirens watch over the ocean, so that its coasts get a warning within '
           'minutes of a great earthquake.',
           y=2006),
      legacy('The tsunami was one of the deadliest natural disasters in history, and the first filmed by so many '
             'ordinary people. It taught the world the lesson Tilly Smith had learned at school: if the sea suddenly '
             'pulls back, run for high ground.',
             '26 December 2004, magnitude 9.1',
             'About 230,000 people died',
             'The waves reached Africa, 5,000 km away'),
      states=('Indonesia', 'Sri Lanka', 'India', 'Thailand', 'Somalia', 'Burma', 'Malaysia'),
      wiki='2004 Indian Ocean earthquake and tsunami', at='banda_aceh')

event('financial-crisis-2008', 'The 2008 financial crisis', 'crisis', (2007, 2009),
      'Bad home loans in America brought the world\'s banks to the edge of collapse, and the worst slump since the 1930s.',
      scene('Houses for everyone',
            'In the early 2000s American lenders gave home loans to millions of people who could not really afford '
            'them, often with low payments at first that jumped later. Banks bundled thousands of these mortgages '
            'together and sold them around the world as safe investments. As long as house prices kept rising, '
            'everyone seemed to win.',
            kick='How it began', y=2005, at='new_york', where='Wall Street'),
      turn('The bubble bursts',
           'In 2006 American house prices began to fall. Millions of borrowers could not keep up their payments, and '
           'the bundles of loans turned out to be worth far less than anyone had thought. No one knew which banks held '
           'the bad debts, so banks stopped lending to each other. In Britain savers queued in the street to take '
           'their money out of Northern Rock.',
           y=2007, at='london'),
      turn('Lehman Brothers',
           'On 15 September 2008 Lehman Brothers, a bank founded 158 years before, went bust, the largest bankruptcy '
           'in American history. Panic swept the world\'s markets. The next day the government took over AIG, a '
           'giant insurer, to stop it collapsing too, and for a few weeks it seemed that the whole banking system '
           'might fail.',
           y=2008, at='new_york', where='Wall Street'),
      scene('Bailouts',
            'Governments poured hundreds of billions into their banks to keep them alive, and central banks cut '
            'interest rates almost to zero and created new money. In Iceland all three big banks collapsed within '
            'days, and the króna lost half its value. People were furious that bankers were rescued while ordinary people '
            'paid.',
            y=2008, at='reykjavik'),
      cost('The Great Recession',
           'The world fell into its deepest slump since the 1930s. World trade shrank, factories closed, and in the '
           'United States millions of families lost their homes. In Spain and Greece more than half of all young '
           'people looking for work could not find it.',
           num='Nearly 9 million', of='Americans lost their jobs', y=2009),
      scene('The euro crisis',
            'The crisis spread to European countries with big debts. Greece, which had understated how much it owed, '
            'had to be rescued three times by the other euro countries, in return for deep cuts that shrank '
            'its economy by a quarter. Ireland, Portugal, Spain and Cyprus needed help too.',
            y=2010, at='athens'),
      legacy('The crisis left a deep anger at bankers who were bailed out while others lost their jobs and homes. It '
             'fed protests such as Occupy Wall Street, and helped the rise of angry new parties on the left and the '
             'right. Banks now have to keep bigger cushions of money, in case another crash comes.',
             'Lehman Brothers collapsed on 15 September 2008',
             'The worst slump since the 1930s',
             'Governments rescued the banks'),
      states=('United States', 'United Kingdom', 'Iceland', 'Greece', 'Ireland', 'Spain', 'Portugal'),
      wiki='2008 financial crisis', at='new_york', where='Wall Street')

event('arab-spring', 'The Arab Spring', 'uprising', (2010, 2012),
      'A fruit seller\'s protest in Tunisia set off revolts across the Arab world, and four rulers fell.',
      scene('Sidi Bouzid',
            'On 17 December 2010 Mohamed Bouazizi, a 26-year-old who sold fruit from a cart in the Tunisian town of '
            'Sidi Bouzid, set himself on fire after officials took away his scales and refused to hear his complaint. '
            'He died in January. Protests spread across Tunisia, filmed on phones and shared on Facebook.',
            kick='How it began', y=2010, at='sidi_bouzid'),
      figure('zine-el-abidine-ben-ali', 'Ben Ali flees',
             'After 23 years in power, Tunisia\'s president, Zine El Abidine Ben Ali, fled to Saudi Arabia on 14 '
             'January 2011. Across the Arab world people who had lived for decades under dictators watched, and '
             'wondered whether they could do the same. Everywhere the chant was the same: the people want the fall of '
             'the regime.',
             y=2011, at='tunis'),
      figure('hosni-mubarak', 'Tahrir Square',
             'On 25 January Egyptians filled Tahrir Square in Cairo. They held it for eighteen days, fighting off the '
             'police and, one day, men charging on camels and horses. Christians stood guard while Muslims prayed. On '
             '11 February Hosni Mubarak, president for thirty years, stepped down, and the square erupted in joy.',
             y=2011, at='cairo'),
      figure('muammar-gaddafi', 'Libya',
             'In Libya Muammar Gaddafi, in power for 42 years, sent his army against the rebels in Benghazi and '
             'promised to hunt them down house by house. The UN allowed air strikes to protect civilians, and NATO\'s '
             'planes helped the rebels win. In October Gaddafi was caught and killed, and Libya split between rival '
             'militias.',
             y=2011, at='benghazi'),
      scene('Syria, Yemen and Bahrain',
            'In Syria Bashar al-Assad met peaceful protests with bullets, and the country slid into a long civil war. '
            'In Yemen the president of 33 years was forced out, but Yemen too fell into war. In Bahrain, troops from '
            'Saudi Arabia helped to crush the protests.',
            y=2011, at='damascus'),
      figure('mohamed-morsi', 'Egypt votes',
             'In 2012 Egypt held its first free election for president, won by Mohamed Morsi of the Muslim '
             'Brotherhood. A year later, after huge protests against him, the army removed him, and its commander, '
             'Abdel Fattah el-Sisi, took power. Hundreds of Morsi\'s supporters were killed when their protest camps '
             'were cleared.',
             y=2012, at='cairo'),
      legacy('Tunisia, where it began, became a democracy, though after 2021 its president took more and more power. '
             'Elsewhere the hopes of 2011 ended in new strongmen, or in wars in Syria, Libya and Yemen. Still, the '
             'Arab Spring showed that ordinary people with phones could topple rulers who had seemed untouchable.',
             'Began in Tunisia in December 2010',
             'Four rulers fell, in Tunisia, Egypt, Libya and Yemen',
             'Ended in wars in Syria, Libya and Yemen'),
      states=('Tunisia', 'Egypt', 'Libya', 'Yemen', 'Syria'), wiki='Arab Spring', at='cairo')

event('syrian-civil-war', 'The Syrian civil war', 'civil-war', (2011, 2024),
      'Protests against Bashar al-Assad turned into a war that killed half a million people and drove half of Syria from home.',
      scene('Daraa',
            'In March 2011, inspired by the revolts in Tunisia and Egypt, teenage boys in the southern town of Daraa '
            'sprayed slogans against the government on a school wall. They were arrested and tortured. Protests for '
            'their release spread across Syria, and the security forces answered with live fire.',
            kick='How it began', y=2011, at='daraa'),
      figure('bashar-al-assad', 'Father and son',
             'Bashar al-Assad, an eye doctor trained in London, had inherited Syria in 2000 from his father, Hafez, '
             'who had ruled it for 29 years. He had promised reform, but he called the protests a foreign plot and '
             'crushed them. Soldiers who refused to shoot deserted, and formed the Free Syrian Army.',
             y=2011, at='damascus'),
      battle('Aleppo',
             'By 2012 the war had reached Aleppo, Syria\'s largest city, which was split in two for four years. '
             'Government helicopters dropped barrel bombs, oil drums packed with explosives, on rebel-held districts. '
             'In December 2016, after a siege backed by Russian air power, the government took the whole city, much of '
             'it in ruins.',
             y=2016, at='aleppo'),
      cost('Sarin',
           'In August 2013 rockets filled with sarin, a nerve gas, hit Ghouta, rebel-held suburbs of Damascus, and '
           'killed hundreds of people, many of them children, as they slept. Most governments and investigators '
           'blamed Assad\'s forces, who denied it. Syria agreed to give up its chemical weapons, but gas attacks went '
           'on.',
           num='Hundreds', of='killed by nerve gas in one night', y=2013, at='ghouta'),
      figure('abu-bakr-al-baghdadi', 'The caliphate',
             'In 2014 the Islamic State, an extremist group grown out of al-Qaeda in Iraq, seized a third of Syria and '
             'much of Iraq, and its leader, Abu Bakr al-Baghdadi, declared a caliphate. From its capital, Raqqa, it '
             'ruled by terror, filming beheadings for the internet. Kurdish-led forces backed by American planes '
             'destroyed it by 2019.',
             y=2014, at='raqqa'),
      turn('Russia steps in',
           'In 2015 Russia sent its air force to save Assad, while Iran and Hezbollah from Lebanon sent fighters. '
           'Turkey backed rebels in the north, and the United States backed the Kurds. Syria became a battleground for '
           'half the world\'s powers, and by 2020 Assad held most of the country again, its cities in ruins.',
           y=2015),
      cost('A nation scattered',
           'Half of all Syrians were driven from their homes. About six million fled abroad, most to Turkey, Lebanon '
           'and Jordan, and in 2015 hundreds of thousands made for Europe, many in flimsy boats. The photograph of a '
           'drowned three-year-old boy, Alan Kurdi, on a Turkish beach moved the world.',
           num='Over 13 million', of='Syrians forced from their homes', y=2015),
      figure('ahmed-al-sharaa', 'Assad falls',
             'In late November 2024 rebels led by Hayat Tahrir al-Sham, under Ahmed al-Sharaa, burst out of their '
             'stronghold in Idlib. City after city fell almost without a fight, and on 8 December they entered '
             'Damascus. Assad fled to Moscow. Crowds poured into his prisons, freeing thousands, and searched for the '
             'missing.',
             y=2024, at='damascus'),
      legacy('Thirteen years of war killed over half a million people and scattered half of Syria\'s people across '
             'the world. The fall of the Assad family, after more than fifty years in power, brought joy and hope, but '
             'also fears of new violence, and the long work of rebuilding a ruined country.',
             'Began with protests in March 2011',
             'Half of all Syrians fled their homes',
             'Assad fell on 8 December 2024'),
      war='syrian-civil-war', wiki='Syrian civil war', at='damascus')

event('covid-19-pandemic', 'The Covid-19 pandemic', 'epidemic', (2019, 2023),
      'A new virus from Wuhan spread around the world in weeks, and shut half of humanity indoors.',
      scene('Wuhan',
            'In December 2019 doctors in Wuhan, a Chinese city of 11 million, saw patients with a pneumonia nobody '
            'could explain. It was a new coronavirus. A young eye doctor, Li Wenliang, warned friends in a chat group, '
            'and the police made him sign a confession for spreading rumours. He died of the disease in February.',
            kick='How it began', y=2019, at='wuhan'),
      turn('Lockdown',
           'On 23 January 2020 China sealed Wuhan off from the world, but the virus had already spread. In March, as '
           'Italy\'s hospitals were overwhelmed, the World Health Organization declared a pandemic. Within weeks half '
           'of humanity had been told to stay at home, the biggest lockdown in history.',
           y=2020, at='bergamo'),
      scene('Empty streets',
            'Schools, offices, shops and stadiums closed. Planes stood on the ground, and wild animals wandered into '
            'empty cities. Children learned at home on screens, people worked over video calls, and families said '
            'goodbye to dying relatives on phones. Doctors and nurses worked in masks for months on end, and many '
            'caught the virus and died.',
            y=2020),
      cost('The dead',
           'By 2024 more than seven million deaths had been reported to the WHO, and the true number, counting deaths '
           'that were never recorded, was perhaps two or three times higher. The old and the sick were most at risk. '
           'The United States counted more dead than any other country, over a million.',
           num='Over 7 million', of='deaths reported to the WHO', y=2021),
      made('Vaccines',
           'Scientists built vaccines in less than a year, a task that used to take a decade. Some used messenger RNA, '
           'a new method that teaches the body\'s own cells to make a harmless piece of the virus.',
           'In December 2020 Margaret Keenan, a 90-year-old grandmother in Coventry, became the first person to get '
           'the Pfizer vaccine once it was approved. Billions of doses followed, saving millions of lives.',
           y=2020, at='coventry'),
      scene('Waves',
            'The virus kept changing. In the spring of 2021 the Delta variant tore through India, where hospitals ran '
            'out of oxygen and cremation fires burned through the night. Then came Omicron, which spread faster still '
            'but was milder. Poorer countries waited months for vaccines that richer ones had bought up.',
            y=2021, at='delhi'),
      turn('The emergency ends',
           'On 5 May 2023 the WHO declared that Covid-19 was no longer a global health emergency. The virus has not '
           'gone away, but vaccines and earlier infections have made it far less deadly. Where it came from, an animal '
           'at a city market or an accident at a laboratory, is still argued over.',
           y=2023, at='geneva'),
      legacy('The pandemic was the worst since the Spanish flu of 1918. It changed how people work, set back millions '
             'of children at school, and left many with long Covid. It also showed how fast science can move when the '
             'whole world needs it.',
             'First found in Wuhan, China, at the end of 2019',
             'Over 7 million deaths reported',
             'Vaccines were made in less than a year'),
      states=('China', 'Italy', 'Spain', 'United States', 'United Kingdom', 'India', 'Brazil', 'Russia', 'Peru',
              'Mexico', 'France', 'Germany', 'Iran', 'Japan', 'Korea, Republic of', 'South Africa', 'Indonesia',
              'Sweden', 'New Zealand', 'Australia'),
      wiki='COVID-19 pandemic', at='wuhan')

event('russia-ukraine-war', 'The Russia-Ukraine war', 'war', (2014, 2025),
      'Russia seized Crimea in 2014 and launched a full invasion in 2022, the largest war in Europe since 1945.',
      scene('The Maidan',
            'In November 2013 Ukraine\'s president, Viktor Yanukovych, under pressure from Russia, backed out of a deal '
            'to draw closer to the European Union. Huge crowds camped through the winter on the Maidan, Kyiv\'s '
            'Independence Square. In February 2014 about a hundred protesters were shot dead, and Yanukovych fled to '
            'Russia.',
            kick='How it began', y=2014, at='kyiv'),
      figure('vladimir-putin', 'Crimea',
             'Days later soldiers in green uniforms without badges seized Crimea. Vladimir Putin at first denied they '
             'were Russian, then admitted it. After a vote held under occupation, Russia annexed Crimea in March 2014, '
             'which most of the world has never recognised. In the eastern Donbas, separatists armed by Russia started '
             'a war.',
             y=2014, at='crimea'),
      cost('Flight MH17',
           'On 17 July 2014 a Malaysia Airlines plane flying from Amsterdam to Kuala Lumpur was shot down over the '
           'Donbas. Investigators found it was hit by a missile from a Russian army launcher, and in 2022 a Dutch court '
           'convicted two Russians and a Ukrainian separatist of murder. Russia denies any part in it.',
           num='298', of='people killed on flight MH17', y=2014, at='hrabove'),
      figure('volodymyr-zelenskyy', 'We are all here',
             'Peace deals stopped the worst of the fighting, but trench warfare went on in the Donbas for eight years. '
             'Then, before dawn on 24 February 2022, Russia invaded from the north, east and south, expecting to take '
             'Kyiv in days. President Volodymyr Zelenskyy, a former comedian, stayed in the capital and filmed himself '
             'in the street at night with his ministers: we are all here, he said.',
             y=2022, at='kyiv'),
      battle('Kyiv holds',
             'The attack on Kyiv stalled. A Russian column 60 kilometres long jammed the roads north of the city, '
             'Ukrainian soldiers with Western anti-tank weapons ambushed its tanks, and by April Russia pulled back from '
             'the north. In the towns it left behind, such as '
             'Bucha, lay the bodies of civilians who had been shot, some with their hands tied.',
             y=2022, at='bucha'),
      battle('Mariupol',
             'In the south Russia took Kherson and besieged the port of Mariupol for almost three months. A bomb hit '
             'its theatre, where hundreds of people were sheltering, though the word children had been painted in huge '
             'letters on the ground outside. The last defenders, in the tunnels of the Azovstal steelworks, '
             'surrendered in May.',
             y=2022, at='mariupol'),
      turn('Counterattack',
           'In September 2022 Ukraine struck back and freed most of the Kharkiv region in a few days, and in November '
           'it retook the city of Kherson. Russia called up 300,000 more men and claimed four Ukrainian regions as its '
           'own. After that the front barely moved: a war of trenches, mines and drones, where each village cost '
           'thousands of lives.',
           y=2022, at='kharkiv'),
      cost('The cost',
           'Neither side gives its losses, but by 2025 hundreds of thousands of soldiers had been killed or wounded on '
           'each side. The UN had counted over 13,000 civilians killed, and said the real number was higher. Russian '
           'strikes on power stations left Ukrainians in the cold and dark through the winters.',
           num='Over 6 million', of='Ukrainians living as refugees abroad', y=2025),
      legacy('It is the largest war in Europe since the Second World War. It drew Finland and Sweden into NATO, and '
             'made Zelenskyy a symbol of resistance. In 2025 President Trump pushed for peace and met Putin in Alaska, '
             'but at the end of the year the fighting went on, with Russia holding about a fifth of Ukraine.',
             'Crimea was seized in 2014',
             'Russia invaded in full on 24 February 2022',
             'Still being fought at the end of 2025'),
      war='russia-ukraine-war', wiki='Russo-Ukrainian war', at='kyiv')

event('israel-hamas-war', 'The Gaza war', 'war', (2023, 2025),
      'Hamas\'s attack on Israel on 7 October 2023 set off a war that left Gaza in ruins, until a ceasefire in October 2025.',
      scene('Gaza',
            'Gaza is a strip of land 40 kilometres long beside the Mediterranean, home to over two million '
            'Palestinians, most of them descended from refugees of 1948. Hamas, an Islamist group that does not '
            'recognise Israel, took control of it in 2007. Israel and Egypt then closed the strip off with a blockade, '
            'and Israel and Hamas fought several short wars.',
            kick='How it began', y=2007, at='gaza'),
      cost('7 October',
           'At dawn on 7 October 2023, a Jewish holiday, thousands of militants led by Hamas broke through the fence '
           'around Gaza under cover of rockets, and attacked army posts, villages and a music festival in southern '
           'Israel. It was the deadliest day for Jews since the Holocaust. 251 people were taken into Gaza as hostages.',
           num='About 1,200', of='killed in Israel, most of them civilians', y=2023, at=(34.49, 31.42),
           where='Southern Israel'),
      scene('The invasion of Gaza',
            'Israel declared war, vowing to destroy Hamas and bring the hostages home. After weeks of heavy bombing, '
            'and an order to people in the north to move south, its troops entered Gaza on 27 October. A truce of a '
            'week in November freed 105 hostages in exchange for 240 Palestinian prisoners. Then the fighting moved '
            'south, to Khan Yunis and later Rafah.',
            y=2023, at='gaza'),
      cost('A strip in ruins',
           'Bombing and fighting damaged or destroyed most of Gaza\'s buildings and drove nine in ten of its people '
           'from their homes. By October 2025 Gaza\'s Health Ministry, which Hamas runs, had counted over 67,000 dead, '
           'many of them women and children. UN agencies treat its figures as reliable; Israel says many of the dead '
           'were fighters.',
           num='Over 67,000', of='killed in Gaza, says its Health Ministry', y=2025, at='gaza'),
      scene('Hunger',
            'Israel at first cut off food, water and fuel, then let in limited aid, saying Hamas stole it. Aid agencies '
            'warned of starvation, and in August 2025 a UN-backed hunger monitor declared famine in Gaza City, which '
            'Israel denied. Crowds seeking food near new aid sites came under deadly fire.',
            y=2025, at='gaza'),
      scene('A wider war',
            'The war spread across the region. Hezbollah in Lebanon fired rockets at Israel, and in 2024 Israel killed '
            'its leader and sent troops into southern Lebanon. Houthi rebels in Yemen attacked ships in the Red Sea. '
            'Iran and Israel struck each other directly, and in June 2025 they fought a twelve-day war, in which '
            'American bombers struck Iran\'s nuclear sites.',
            y=2024, at='beirut'),
      turn('In court',
           'South Africa accused Israel of genocide at the International Court of Justice, which in 2024 ordered '
           'Israel to prevent acts of genocide and let in aid; Israel called the charge baseless. The International '
           'Criminal Court issued arrest warrants for war crimes against Israel\'s prime minister, Benjamin Netanyahu, '
           'his former defence minister, and a Hamas commander.',
           y=2024, at='the_hague'),
      turn('Ceasefire',
           'A truce in January 2025 returned 33 hostages, eight of them dead, but broke down in March. In October 2025, under a plan put '
           'forward by the American president, Donald Trump, a ceasefire took hold. Hamas freed the last 20 living '
           'hostages, Israel released about 2,000 Palestinian prisoners and detainees, and Israeli troops pulled back '
           'to a line, still holding about half of Gaza.',
           y=2025, at='gaza'),
      legacy('The war was the deadliest in the long conflict between Israelis and Palestinians. It left Israelis '
             'scarred by 7 October and the long ordeal of the hostages, and Gaza in ruins, its people mourning tens of '
             'thousands of dead. At the end of 2025 who would rule Gaza, and whether the ceasefire would hold, were '
             'still unknown.',
             'Began with the attack of 7 October 2023',
             'Most of Gaza\'s buildings were damaged or destroyed',
             'A ceasefire began in October 2025'),
      war='israel-hamas-war', wiki='Gaza war', at='gaza')

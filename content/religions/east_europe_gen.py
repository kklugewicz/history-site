"""Generate zones_east_europe.json: Central and Eastern Europe, Balkans, Russia, Caucasus."""
import json, os

H = os.path.dirname(os.path.abspath(__file__))

SOVIET_EUR = "The Bolsheviks separated church and state in 1918 and imposed state atheism, closing and demolishing churches and sending clergy to the camps."
REVIVAL_RU = "With the fall of the Soviet Union in 1991 the Russian Orthodox Church revived, and most people here now identify as Orthodox, though few attend regularly."
SOVIET_UA = "Soviet rule imposed state atheism, closing and blowing up churches and shooting or deporting clergy and believers."
REVIVAL_UA = "Ukrainian independence in 1991 brought an Orthodox revival, now led mainly by the Orthodox Church of Ukraine, which received autocephaly in 2019."

Z = []


def zone(id, name, lon, lat, *hist):
    Z.append({"id": id, "name": name, "lon": lon, "lat": lat,
              "history": [{"from": f, "faith": r, "note": n} for f, r, n in hist]})


# ---------------- Central Europe ----------------
zone("poland", "Poland", 21.0, 52.23,
     (-10000, "folk", "Stone Age hunters and later Neolithic and Bronze Age farmers of the Vistula and Oder basins worshipped local spirits and ancestors."),
     (-500, "pagan-europe", "Celtic, Germanic and Baltic peoples, and from the 6th century Slavic tribes such as the Polans, worshipped gods like Perun and Svetovit at hilltop shrines and sacred groves."),
     (966, "christian", "Duke Mieszko I was baptized in 966 and brought the Polans into Latin Christianity, and the archbishopric of Gniezno was founded in 1000."),
     (1054, "catholic", "After the 1054 schism Poland stayed with Rome, and Catholicism outlasted the Reformation, the partitions and Communist rule to remain the faith of most Poles."))

zone("pomerania", "Western Pomerania (Szczecin)", 14.55, 53.43,
     (-10000, "folk", "Mesolithic hunters and later farming cultures settled the Baltic coast around the mouth of the Oder."),
     (-500, "pagan-europe", "Germanic tribes and, from the 7th century, Slavic Pomeranians worshipped gods such as the three-headed Triglav, whose temple stood at Szczecin."),
     (1124, "catholic", "Bishop Otto of Bamberg converted the Pomeranians in missions of 1124 and 1128, backed by the Polish duke Boleslaw III."),
     (1534, "lutheran", "The Diet of Treptow in 1534 made the Duchy of Pomerania Lutheran, and it stayed Protestant under Swedish and Prussian rule."),
     (1945, "catholic", "In 1945 the region was given to Poland, its German Protestants were expelled and Polish Catholic settlers made it Catholic again."))

zone("silesia", "Silesia (Wroclaw)", 17.04, 51.11,
     (-10000, "folk", "Hunters and then Neolithic farmers settled the fertile upper Oder valley."),
     (-500, "pagan-europe", "Celts, the Germanic Silingi who gave Silesia its name, and from the 6th century Slavic tribes worshipped pagan gods, with a sacred mountain at Sleza."),
     (1000, "christian", "The bishopric of Wroclaw was founded in 1000 under Gniezno, and Silesia became Christian as part of Piast Poland."),
     (1054, "catholic", "After the 1054 schism Silesia followed Rome, and its Piast duchies passed to the Bohemian crown in the 14th century."),
     (1525, "lutheran", "Wroclaw adopted the Reformation in 1523 to 1525 and most of Lower Silesia became Lutheran, as it largely stayed despite the Habsburg Counter-Reformation and under Prussian rule."),
     (1945, "catholic", "In 1945 Silesia was given to Poland, its German Protestants were expelled and Polish Catholics settled in their place."))

zone("czechia", "Czechia (Bohemia)", 14.42, 50.08,
     (-10000, "folk", "Hunters and later the first farmers of central Europe settled Bohemia, building Neolithic enclosures and burial mounds."),
     (-500, "pagan-europe", "The Celtic Boii, who gave Bohemia its name, then the Germanic Marcomanni and from the 6th century Slavs worshipped Celtic, Germanic and Slavic gods."),
     (880, "christian", "Duke Borivoj I was baptized around 880 through the mission of Cyril and Methodius in Great Moravia, and his grandson Saint Wenceslas made Bohemia firmly Christian."),
     (1054, "catholic", "After the 1054 schism Bohemia stayed with Rome, and Prague got its own archbishop in 1344 under Emperor Charles IV."),
     (1420, "hussite", "After Jan Hus was burned in 1415 most Czechs followed his Hussite (Utraquist) church, which defeated five crusades and later sat alongside Lutherans and the Unity of Brethren."),
     (1620, "catholic", "After the Protestant estates lost the Battle of White Mountain in 1620, the Habsburgs expelled Protestant clergy and nobles and forced Bohemia back to Catholicism."),
     (1948, "secular", "The Communist takeover of 1948 persecuted the churches, and by its end most Czechs declared no religion, making Czechia one of the least religious countries in the world."))

zone("slovakia", "Slovakia", 19.15, 48.74,
     (-10000, "folk", "Hunters and then Neolithic farmers settled the valleys between the Carpathians and the Danube."),
     (-500, "pagan-europe", "Celts, then the Germanic Quadi, and from the 6th century Slavs worshipped their gods in the lands north of the Danube."),
     (863, "christian", "Christianity reached Nitra under Prince Pribina around 828, and the mission of Cyril and Methodius to Great Moravia in 863 brought a Slavonic liturgy and converted the Slavs."),
     (1054, "catholic", "After the 1054 schism Slovakia, by then Upper Hungary within the Kingdom of Hungary, followed the Latin church."),
     (1560, "lutheran", "The Reformation spread through the German mining towns and the Slovak countryside of Upper Hungary, and by the late 16th century most of its people were Lutheran or Calvinist."),
     (1670, "catholic", "The Habsburg Counter-Reformation, led by Archbishop Peter Pazmany and harsh measures after 1670, returned most Slovaks to Catholicism, still the faith of most of the country."))

zone("hungary", "Hungary", 19.04, 47.5,
     (-10000, "folk", "Hunters and then Neolithic farmers of the Starcevo and Linear Pottery cultures settled the Carpathian Basin."),
     (-400, "pagan-europe", "Celtic tribes such as the Eravisci, who built a hill fort on Gellert Hill, worshipped Celtic gods in Pannonia."),
     (10, "hellenic", "Rome conquered Pannonia, and Aquincum, today's Budapest, became a provincial capital with temples to Jupiter and Mithras."),
     (380, "christian", "Christianity, made the state religion of the Roman Empire under Theodosius, spread among the Pannonian provincials."),
     (454, "arian", "After Attila's Hunnic empire collapsed, the Arian Christian Gepids and Ostrogoths and later the Lombards ruled the Carpathian Basin."),
     (568, "tengri", "The Avars, steppe nomads who followed the sky god Tengri, took the basin in 568, and in 895 the pagan Magyars conquered it."),
     (1000, "christian", "Stephen I, crowned in 1000 with a crown sent by Pope Sylvester II, converted the Magyars and founded the Hungarian church."),
     (1054, "catholic", "After the 1054 schism Hungary became a bulwark of the Latin church on the border of the Orthodox world."),
     (1570, "reformed", "In the 16th century most Hungarians turned Protestant, above all Calvinist, a faith that survived both Ottoman rule of the centre and Habsburg rule of the west."),
     (1690, "catholic", "After the Habsburgs drove out the Ottomans in 1686, the Counter-Reformation made Catholics the majority again, though eastern Hungary kept a strong Calvinist church."))

# ---------------- Baltics and Belarus ----------------
zone("lithuania", "Lithuania", 25.28, 54.69,
     (-10000, "folk", "Hunters and later farmers settled the forests and lakes of the eastern Baltic after the Ice Age."),
     (-1000, "pagan-europe", "Baltic tribes worshipped the thunder god Perkunas and kept sacred fires and groves, becoming the last pagans of Europe."),
     (1387, "catholic", "Grand Duke Jogaila, crowned king of Poland, baptized Lithuania in 1387 and Samogitia followed in 1413, after King Mindaugas's conversion of 1251 had lapsed."))

zone("latvia", "Latvia", 24.1, 56.95,
     (-10000, "folk", "Hunters and later farmers settled the Daugava valley and the Gulf of Riga after the Ice Age."),
     (-1000, "pagan-europe", "Baltic Curonians, Semigallians and Latgalians and the Finnic Livs worshipped Dievs, Perkons and nature spirits."),
     (1207, "catholic", "Bishop Albert founded Riga in 1201, and the crusading Livonian Brothers of the Sword forced the Livs and Latvians to accept Latin Christianity in the following decades."),
     (1522, "lutheran", "Riga adopted the Reformation in 1522, and under Swedish and Baltic German rule most Latvians became Lutheran, though Latgale in the east stayed Catholic."),
     (1940, "secular", "Soviet annexation in 1940 and again in 1944 brought state atheism, closing churches and sending clergy to the Gulag."),
     (1991, "lutheran", "Independence in 1991 restored religious freedom in a country split between Lutherans, Catholics and Orthodox, with the Lutheran church the largest by membership."))

zone("estonia", "Estonia", 24.75, 59.44,
     (-10000, "folk", "Hunters and later farmers settled the Estonian coast and islands after the Ice Age."),
     (-1000, "pagan-europe", "Finnic Estonians worshipped Taara and Uku, forest spirits and sacred groves, and resisted Christianity longer than most of Europe."),
     (1227, "catholic", "The Livonian Crusade of the Danes and the Sword Brothers conquered Estonia by 1227 and imposed Latin Christianity."),
     (1524, "lutheran", "Tallinn and Tartu accepted the Reformation in 1524 to 1525, and under Swedish rule Estonia became thoroughly Lutheran."),
     (1940, "secular", "Soviet annexation in 1940 and 1944 imposed state atheism, and most Estonians still follow no religion, making Estonia one of the least religious countries on earth."))

zone("belarus", "Belarus", 27.56, 53.9,
     (-10000, "folk", "Hunters and later farmers settled the forests and marshes of the upper Dnieper and Neman."),
     (-500, "pagan-europe", "Baltic tribes and from the 6th century East Slavs such as the Krivichs and Dregovichs worshipped Perun and other Slavic and Baltic gods."),
     (992, "christian", "The bishopric of Polotsk was founded in 992 after Prince Vladimir of Kiev made Byzantine Christianity the faith of the Rus."),
     (1054, "orthodox", "After the 1054 schism the Belarusian lands followed Constantinople, and they kept the Orthodox faith under the Grand Duchy of Lithuania from the 14th century."),
     (1700, "catholic", "The Union of Brest of 1596 brought Ruthenian bishops into union with Rome, and by the 18th century most Belarusians belonged to this Greek Catholic church."),
     (1839, "orthodox", "Tsar Nicholas I had the Synod of Polotsk dissolve the Greek Catholic church in 1839, forcing its Belarusian faithful into Russian Orthodoxy."),
     (1920, "secular", "Soviet rule over Minsk from 1920 imposed state atheism, destroying most churches and arresting their clergy."),
     (1991, "orthodox", "Independence in 1991 allowed a religious revival, and most Belarusians now identify as Orthodox, with a Catholic minority in the west."))

zone("kaliningrad", "Kaliningrad (East Prussia)", 20.51, 54.71,
     (-10000, "folk", "Hunters and later farmers settled the Baltic coast, famous since antiquity for its amber."),
     (-1000, "pagan-europe", "The Baltic Old Prussians worshipped Perkunas and other gods at sacred groves and long resisted missionaries, killing Saint Adalbert in 997."),
     (1283, "catholic", "The Teutonic Knights completed their crusade against the Prussians in 1283 and settled the land with German Catholics."),
     (1525, "lutheran", "Grand Master Albert of Brandenburg made the Duchy of Prussia the first Lutheran state in 1525, and Konigsberg became a Protestant centre."),
     (1946, "secular", "After 1945 the Soviet Union annexed the region, expelled the Germans and resettled it with Soviet citizens under state atheism."),
     (1991, "orthodox", "Since 1991 Orthodoxy has revived among the region's Russian population, and a large new cathedral opened in Kaliningrad in 2006."))

# ---------------- Ukraine, Moldova, Romania ----------------
zone("ukraine-west", "Western Ukraine (Galicia)", 24.03, 49.84,
     (-10000, "folk", "Hunters and later Neolithic farmers settled the foothills of the Carpathians and the upper Dniester."),
     (-500, "pagan-europe", "Slavic tribes such as the White Croats and Dulebs settled Galicia and worshipped Perun, Veles and other Slavic gods."),
     (990, "christian", "Prince Vladimir of Kiev, who had taken the Cherven towns in 981, brought Galicia into the Christianity of the Rus after his baptism in 988."),
     (1054, "orthodox", "After the 1054 schism Galicia followed Constantinople, and its Ruthenians kept the Orthodox faith after Poland annexed the region in 1349."),
     (1700, "catholic", "Following the Union of Brest, the bishops of Przemysl in 1692 and Lviv in 1700 accepted union with Rome, making Galicia's Ukrainians Greek Catholics."),
     (1946, "orthodox", "The Soviet-staged Synod of Lviv in 1946 abolished the Greek Catholic church and forced its parishes into Russian Orthodoxy, though many faithful kept worshipping in secret."),
     (1989, "catholic", "The Greek Catholic church was legalized again in 1989 and reclaimed its parishes, and it remains the largest faith of Galicia today."))

zone("ukraine-right-bank", "Right-bank Ukraine (Podolia)", 28.47, 49.23,
     (-10000, "folk", "Neolithic farmers of the Cucuteni and Trypillia culture built some of Europe's largest early settlements here and made clay figurines for household cults."),
     (500, "pagan-europe", "East Slavic tribes such as the Polans, Drevlians and Volhynians settled the forest steppe and worshipped Perun, Veles and household spirits."),
     (988, "christian", "Prince Vladimir of Kiev was baptized in 988 and made Byzantine Christianity the faith of the Rus."),
     (1054, "orthodox", "After the 1054 schism the land stayed Orthodox under Kievan Rus, then under Lithuanian and from 1569 Polish rule."),
     (1720, "catholic", "After the Union of Brest and the Synod of Zamosc in 1720, most Ukrainian parishes west of the Dnieper became Greek Catholic under the Polish crown."),
     (1795, "orthodox", "Russia annexed the region in the partitions of Poland of 1793 and 1795, and Catherine II and later Nicholas I forced its Greek Catholics into Orthodoxy."),
     (1922, "secular", SOVIET_UA),
     (1991, "orthodox", REVIVAL_UA))

zone("ukraine", "Central Ukraine (Kyiv)", 30.52, 50.45,
     (-10000, "folk", "Hunters and then Neolithic farmers of the Trypillia culture settled the Dnieper lands and practised fertility and household cults."),
     (500, "pagan-europe", "The East Slavic Polans founded Kyiv and worshipped Perun, whose idol Prince Vladimir set up on the city's hill in 980."),
     (988, "christian", "Prince Vladimir was baptized at Chersonesos and had the people of Kyiv baptized in the Dnieper in 988, making the Rus Christian."),
     (1054, "orthodox", "After the 1054 schism Kyiv stayed with Constantinople and remained an Orthodox heart of the Rus under Mongol, Lithuanian, Polish and from 1667 Russian rule."),
     (1922, "secular", "Soviet rule imposed state atheism: churches such as Kyiv's St Michael's Golden-Domed Monastery were blown up and clergy were shot or deported."),
     (1991, "orthodox", REVIVAL_UA))

zone("ukraine-south", "Southern Ukraine (Nogai steppe)", 34.0, 47.0,
     (-10000, "folk", "Steppe herders of the Yamna culture, and later Cimmerians, Scythians and Sarmatians, raised kurgans and worshipped Iranian steppe gods such as Tabiti and Papaios."),
     (370, "tengri", "The Huns swept the steppe in the 370s, followed by Bulgars, Khazars, Pechenegs and Cumans, nomads who honoured the sky god Tengri."),
     (1313, "sunni", "Uzbek Khan made Islam the faith of the Golden Horde from 1313, and the Nogai and Crimean Tatars who held the steppe afterwards were Sunni Muslims."),
     (1783, "orthodox", "Russia annexed the Crimean Khanate in 1783, the Nogais left or were deported, and Orthodox Ukrainian and Russian settlers filled the new province of New Russia."),
     (1922, "secular", SOVIET_UA),
     (1991, "orthodox", REVIVAL_UA))

zone("moldova", "Moldova (Bessarabia)", 28.85, 47.0,
     (-10000, "folk", "Neolithic Cucuteni and Trypillia farmers, then Getae and Dacians who worshipped Zalmoxis, lived between the Prut and the Dniester."),
     (900, "tengri", "Turkic Pechenegs and then Cumans, followers of Tengri, dominated the land between the Carpathians and the Dniester from the 10th to the 13th century."),
     (1359, "orthodox", "Bogdan I founded the principality of Moldavia in 1359, and its Romanian-speaking people, who used the Slavonic Orthodox liturgy, made it an Orthodox state."),
     (1944, "secular", "Bessarabia, annexed by Russia in 1812 and united with Romania in 1918, was taken by the Soviet Union in 1940 and again in 1944 and subjected to state atheism."),
     (1991, "orthodox", "Independence in 1991 restored the church, and over 90 percent of Moldovans now identify as Orthodox."))

zone("wallachia", "Wallachia (southern Romania)", 26.1, 44.43,
     (-10000, "folk", "Neolithic farmers of the Gumelnita culture, and later the Getae and Dacians who worshipped Zalmoxis, lived on the lower Danube plain."),
     (400, "christian", "Daco-Roman Christianity spread north of the Danube from the Roman frontier in the 4th to 6th centuries and survived the Gothic, Hunnic, Avar and Slavic invasions."),
     (1054, "orthodox", "Under Bulgarian and Byzantine influence the Romanians followed Constantinople after the 1054 schism, and the principality of Wallachia, founded around 1310, was Orthodox."))

zone("transylvania", "Transylvania", 23.6, 46.77,
     (-10000, "folk", "Neolithic farmers, and later the Dacians, whose capital Sarmizegetusa held great sanctuaries, lived inside the Carpathian arc."),
     (106, "hellenic", "Trajan conquered Dacia in 106, settling Roman colonists who brought Jupiter, Mithras and the imperial cult."),
     (400, "arian", "After Rome withdrew in 271, Germanic Goths and then the Gepids, who took up Arian Christianity, ruled Transylvania until the Avars came in 567."),
     (568, "tengri", "The Avars, steppe nomads who worshipped Tengri, took the region in 568, followed by Bulgars and around 900 by the pagan Magyars."),
     (1003, "christian", "Stephen I of Hungary defeated the local ruler Gyula in 1003 and brought Transylvania into the Christian Hungarian kingdom."),
     (1054, "catholic", "After the 1054 schism Transylvania's Hungarian, Szekler and later German Saxon settlers followed the Latin church, while its Romanian peasants stayed Orthodox."),
     (1570, "reformed", "The Principality of Transylvania, ruled by mostly Calvinist princes and nobles, granted freedom to Catholics, Lutherans, Calvinists and Unitarians at Turda in 1568, while Orthodoxy was only tolerated."),
     (1760, "orthodox", "By the 18th century Romanians were the majority, and after a split over the union with Rome of 1700, Orthodoxy was restored as their largest church in the 1760s, as it remains."))

zone("dobruja", "Dobruja", 28.3, 44.3,
     (-10000, "folk", "Neolithic Hamangia farmers, makers of the Thinker of Cernavoda figurine, and later the Getae lived between the lower Danube and the Black Sea."),
     (46, "hellenic", "Rome annexed the land between the Danube and the sea in 46, joining the old Greek colonies of Tomis, Histria and Callatis, where the poet Ovid had died in exile."),
     (330, "christian", "Christianity spread in Roman Scythia Minor, which had its own bishop at Tomis by the 4th century."),
     (681, "tengri", "Khan Asparukh's Bulgars crossed the Danube in 681 and made this region the heart of a khanate whose rulers worshipped the sky god Tangra."),
     (864, "christian", "Boris I of Bulgaria accepted baptism in 864 and converted his Bulgars and Slavs to Byzantine Christianity."),
     (1054, "orthodox", "After the 1054 schism Dobruja followed Constantinople under Byzantine, Bulgarian and Cuman lords."),
     (1500, "sunni", "After the Ottoman conquest of about 1420, Turkish and Tatar settlers made Muslims the majority of Dobruja for most of the next four centuries."),
     (1878, "orthodox", "The Congress of Berlin gave northern Dobruja to Romania in 1878, and Romanian settlement and Muslim emigration made it Orthodox again."))

# ---------------- Balkans ----------------
zone("slovenia", "Slovenia", 14.5, 46.05,
     (-10000, "folk", "Ice Age hunters and later the pile-dwelling farmers of the Ljubljana Marshes lived in the eastern Alps."),
     (-400, "pagan-europe", "Celtic tribes of the kingdom of Noricum worshipped gods such as Belenus in the eastern Alps."),
     (-15, "hellenic", "Rome absorbed Noricum and founded the colony of Emona, today's Ljubljana, with temples to the Roman gods."),
     (380, "christian", "Christianity became the state religion of the Roman Empire, and Emona had its own bishop."),
     (590, "pagan-europe", "Slavs, ancestors of the Slovenes, settled the eastern Alps under Avar overlordship and worshipped Slavic gods."),
     (750, "christian", "Missionaries from Salzburg, invited after the princes of Carantania accepted Bavarian protection, converted the Alpine Slavs in the 8th century."),
     (1054, "catholic", "After the 1054 schism the Slovene lands, ruled by German and later Habsburg lords, stayed with Rome, and Catholicism outlasted the Reformation and Yugoslav communism."))

zone("croatia", "Croatia", 15.98, 45.81,
     (-10000, "folk", "Neanderthals at Krapina and later Illyrian tribes such as the Liburnians and Delmatae lived here, worshipping local gods."),
     (-35, "hellenic", "Octavian's campaigns of 35 BC began Rome's conquest of the region, which became the provinces of Dalmatia and Pannonia with Roman gods and cults."),
     (380, "christian", "Christianity became the Roman state religion, with great bishoprics at Salona and Sirmium, and Diocletian's palace at Split later became a cathedral."),
     (620, "pagan-europe", "The Croats and other Slavs settled the region in the 7th century after the Avar wars and kept their Slavic gods for a time."),
     (800, "christian", "The Croats accepted Christianity from Frankish and Dalmatian Latin missionaries around 800, under dukes such as Borna and Trpimir."),
     (1054, "catholic", "After the 1054 schism Croatia stayed with Rome, and King Zvonimir was crowned in 1076 by a papal legate, binding the kingdom to the Latin church."))

zone("bosnia", "Bosnia and Herzegovina", 18.41, 43.86,
     (-10000, "folk", "Neolithic Butmir farmers and later Illyrian tribes such as the Daesitiates lived in the Bosnian valleys."),
     (9, "hellenic", "After crushing the great Illyrian revolt in 9, Rome ruled Bosnia as part of Dalmatia, with Roman gods and Mithras worshipped in its mining towns."),
     (380, "christian", "Christianity became the state religion of the Roman Empire and spread through the province of Dalmatia."),
     (620, "pagan-europe", "Slavs settled Bosnia in the 7th century and kept their Slavic gods for a time."),
     (900, "christian", "The Slavs of Bosnia were Christianized in the 9th and 10th centuries by missionaries from the Dalmatian coast and Byzantium."),
     (1054, "catholic", "After the 1054 schism Bosnia leaned to the Latin church, though from the 13th century its own Bosnian Church, accused by Rome of heresy, led many believers."),
     (1580, "sunni", "After the Ottoman conquest of 1463 many Bosnians converted to Islam, and Muslims became the majority by the late 16th century."),
     (1878, "orthodox", "When Austria-Hungary occupied Bosnia in 1878 its first census found Orthodox Serbs, at about 43 percent, slightly outnumbering Muslims after decades of Muslim emigration."),
     (1971, "sunni", "Recognized as a nation in Yugoslavia, Bosnian Muslims overtook Orthodox Serbs as the largest group in the 1971 census, and Bosniaks are about half of the population today."))

zone("serbia", "Serbia", 20.46, 44.82,
     (-10000, "folk", "Mesolithic Lepenski Vir fishermen carved fish-faced stone heads by the Danube, and Neolithic Vinca farmers left thousands of clay figurines."),
     (-300, "pagan-europe", "The Celtic Scordisci founded Singidunum, today's Belgrade, and worshipped Celtic gods alongside Thracian and Illyrian neighbours."),
     (-29, "hellenic", "Marcus Crassus conquered Moesia in 29 BC, and Singidunum became a legionary fortress honouring Jupiter and the emperors."),
     (330, "christian", "Constantine the Great, born at Naissus, today's Nis, legalized Christianity, which soon became the faith of the Roman Danube provinces."),
     (600, "pagan-europe", "Slavs and Avars overran the Balkans around 600, and the Serbs who settled there worshipped Slavic gods."),
     (870, "christian", "The Serbs were baptized by Byzantine missionaries around 870 under Prince Mutimir, and the disciples of Cyril and Methodius brought the Slavonic liturgy."),
     (1054, "orthodox", "After the 1054 schism the Serbs followed Constantinople, and Saint Sava won independence for the Serbian Orthodox Church in 1219, the faith that sustained them under Ottoman rule."))

zone("montenegro", "Montenegro", 19.1, 42.44,
     (-10000, "folk", "Stone Age hunters and later Illyrian tribes such as the Labeates and Docleatae worshipped serpent and local gods on the Adriatic coast."),
     (-168, "hellenic", "Rome defeated the Illyrian king Gentius in 168 BC, and the land later became part of the Roman province of Dalmatia with the city of Doclea."),
     (380, "christian", "Christianity became the state religion of the Roman Empire and spread through the cities of the Adriatic coast."),
     (620, "pagan-europe", "Slavs settled the region in the 7th century and kept their Slavic gods for a time."),
     (870, "christian", "Byzantine and Latin missionaries converted the Slavs of Duklja in the 9th century."),
     (1054, "catholic", "After the 1054 schism Duklja looked to Rome, which crowned its king Mihailo in 1077 and raised Bar to an archbishopric in 1089."),
     (1186, "orthodox", "Stefan Nemanja annexed Zeta in 1186, and under the Serbian church and later the prince-bishops of Cetinje Montenegro became Orthodox."))

zone("kosovo", "Kosovo", 21.17, 42.66,
     (-10000, "folk", "Neolithic Vinca farmers, makers of the Goddess on the Throne figurine, and later the Illyrian Dardani lived on the Kosovo plain."),
     (-28, "hellenic", "Rome conquered the Dardani and made the region part of Moesia, with mining towns such as Ulpiana."),
     (330, "christian", "Christianity spread through the Roman Balkans after Constantine, and Ulpiana had its own bishop."),
     (600, "pagan-europe", "Slavs settled Dardania around 600 and worshipped Slavic gods."),
     (870, "christian", "The Slavs of Kosovo were Christianized under Byzantine and Bulgarian rule in the 9th century."),
     (1054, "orthodox", "After the 1054 schism Kosovo followed Constantinople, and under the Serbian kings it became the seat of the Serbian Patriarchate at Pec, founded in 1346."),
     (1750, "sunni", "After the Ottoman conquest and the Great Serb Migration of 1690, Albanians who had largely converted to Islam became the majority of Kosovo in the 18th century."))

zone("albania", "Albania", 19.95, 41.2,
     (-10000, "folk", "Neolithic farmers and later the Illyrian tribes of the region worshipped the sun, serpents and local gods."),
     (-168, "hellenic", "Greek colonies such as Apollonia and Dyrrachium spread the Greek gods, and after 168 BC Rome ruled Illyria and built the Via Egnatia across it."),
     (380, "christian", "Christianity became the state religion of the Roman Empire, and Dyrrachium became a metropolitan see."),
     (1054, "orthodox", "After the 1054 schism Albania was divided, the north looking to Rome while the Byzantine-ruled centre and south stayed Orthodox."),
     (1650, "sunni", "Under Ottoman rule from the 15th century most Albanians gradually converted to Islam, Muslims becoming the majority in the 17th century, many of them following the Bektashi order."),
     (1967, "secular", "Enver Hoxha declared Albania the world's first atheist state in 1967, closing every mosque and church."),
     (1991, "sunni", "Religious freedom returned in 1991, and Sunni Muslims are again the largest group, alongside Catholics, Orthodox and Bektashis."))

zone("north-macedonia", "North Macedonia", 21.43, 42.0,
     (-10000, "folk", "Neolithic farmers and later the Paeonians and Dassaretae worshipped local gods in the Vardar valley."),
     (-350, "hellenic", "Philip II of Macedon subdued the Paeonians around 358 BC, bringing the Greek gods, and Rome made the region the province of Macedonia in 146 BC."),
     (330, "christian", "Christianity, preached by Saint Paul in Macedonia, became the faith of the region after Constantine."),
     (600, "pagan-europe", "Slavs settled the Vardar valley around 600 and worshipped Slavic gods."),
     (886, "christian", "Under Bulgarian rule Saint Clement and Saint Naum built a centre of Slavonic Christianity at Ohrid from 886."),
     (1054, "orthodox", "After the 1054 schism the Archbishopric of Ohrid followed Constantinople, and Orthodoxy survived five centuries of Ottoman rule from 1392 as the faith of most Macedonians."))

zone("bulgaria", "Bulgaria", 25.62, 43.08,
     (-10000, "folk", "Neolithic farmers and the Varna culture, with the world's oldest worked gold, were followed by Thracians who honoured the Great Mother and the Thracian horseman."),
     (46, "hellenic", "Rome annexed Thrace in 46, and with Moesia to the north it brought Roman and Greek gods to the land."),
     (330, "christian", "Christianity became the faith of the Roman provinces of Thrace and Moesia after Constantine, with a famous council held at Serdica, today's Sofia, in 343."),
     (600, "pagan-europe", "Slavs settled the land around 600, and from 681 the First Bulgarian Empire joined them to Bulgar khans who worshipped the sky god Tangra."),
     (864, "christian", "Khan Boris I was baptized in 864 and made Bulgaria a Christian state, adopting the Slavonic liturgy of the disciples of Cyril and Methodius."),
     (1054, "orthodox", "After the 1054 schism Bulgaria followed Constantinople, and its Orthodox church survived Ottoman rule from 1396 to 1878 and communism to remain the majority faith."))

zone("greece", "Greece", 23.73, 37.98,
     (-10000, "folk", "Neolithic farmers, then the Bronze Age Minoans and early Greeks, worshipped mother goddesses, sacred bulls and mountain peak sanctuaries."),
     (-1200, "hellenic", "The Mycenaean Greeks already named Zeus, Hera and Poseidon on their tablets, and after their fall the city states built temples to the Olympian gods and consulted Delphi."),
     (380, "christian", "Emperor Theodosius made Christianity the state religion in 380 and banned pagan sacrifice, and Justinian closed the Athenian schools of philosophy in 529."),
     (1054, "orthodox", "After the 1054 schism Greece was the core of Orthodoxy, a faith that held the Greeks together under Frankish, Venetian and Ottoman rule and that most still follow."))

zone("crete", "Crete", 24.9, 35.25,
     (-10000, "folk", "Early farmers and then the Minoans worshipped goddesses with snakes, sacred bulls and double axes in palaces such as Knossos."),
     (-1200, "hellenic", "Mycenaean and then Dorian Greeks brought the Olympian gods, and Crete claimed to be the birthplace of Zeus."),
     (380, "christian", "Crete, evangelized according to tradition by Saint Paul's disciple Titus, became Christian with the rest of the Roman Empire."),
     (827, "sunni", "Andalusian Muslim exiles conquered Crete around 827 and founded the Emirate of Crete, where Islam was the ruling faith and many islanders converted."),
     (961, "christian", "The Byzantine general Nikephoros Phokas retook Crete in 961, and the island was won back to Christianity."),
     (1054, "orthodox", "After the 1054 schism Crete stayed Orthodox under Venetian rule from 1211 and Ottoman rule from 1669, when many Cretans became Muslim, until union with Greece in 1913."))

zone("cyprus", "Cyprus", 33.36, 35.17,
     (-10000, "folk", "Neolithic settlers of Khirokitia and then Bronze Age Cypriots worshipped a fertility goddess, later honoured at Paphos as Aphrodite."),
     (-1100, "hellenic", "Mycenaean Greeks settled Cyprus around 1100 BC and spread the cult of Aphrodite, alongside Phoenician colonists who worshipped Astarte."),
     (350, "christian", "Paul and Barnabas preached on Cyprus around 45, and by the 4th century the island was Christian, its church declared self-governing in 431."),
     (1054, "orthodox", "After the 1054 schism Greek Cypriots stayed Orthodox under Catholic Lusignan and Venetian lords and Ottoman rule from 1571, and they remain the island's majority."))

# ---------------- European Russia ----------------
zone("russia-moscow", "Central Russia (Moscow)", 37.62, 55.75,
     (-10000, "folk", "Hunters and later Finnic peoples such as the Merya and Muroma worshipped forest and water spirits in the upper Volga and Oka basins."),
     (900, "pagan-europe", "East Slavic Vyatichi and Krivichi settled among the Finns and worshipped Perun, Veles and Mokosh."),
     (1150, "orthodox", "Under the princes of Rostov and Suzdal, who first mention Moscow in 1147, the Vyatichi, among the last East Slavs to convert, accepted Orthodoxy in the 12th century."),
     (1918, "secular", "The Bolsheviks separated church and state in 1918 and imposed state atheism, demolishing churches such as Moscow's Cathedral of Christ the Saviour in 1931."),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-novgorod", "Novgorod", 31.27, 58.52,
     (-10000, "folk", "Hunters and then Finnic peoples such as the Chud and Vod lived around Lake Ilmen, worshipping nature spirits."),
     (750, "pagan-europe", "Ilmen Slovenes settled Novgorod and, joined by Norse Varangians under Rurik in 862, worshipped Perun and Veles."),
     (990, "christian", "Bishop Joachim and Dobrynya baptized Novgorod around 990, throwing Perun's idol into the Volkhov river."),
     (1054, "orthodox", "After the 1054 schism Novgorod's Saint Sophia cathedral, consecrated around 1050, made the merchant republic a centre of Orthodoxy until Moscow annexed it in 1478."),
     (1918, "secular", SOVIET_EUR),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-ingria", "Ingria (St Petersburg)", 30.32, 59.94,
     (-10000, "folk", "Finnic Izhorians and Votes lived along the Neva and the Gulf of Finland, worshipping forest and water spirits."),
     (1240, "orthodox", "Under Novgorod, whose prince Alexander Nevsky beat the Swedes on the Neva in 1240, the Votes and Izhorians became Orthodox."),
     (1617, "lutheran", "Sweden won Ingria by the Treaty of Stolbovo in 1617, many Orthodox inhabitants fled and Lutheran Finns settled the land."),
     (1703, "orthodox", "Peter the Great reconquered the Neva and founded St Petersburg in 1703, and Russian settlers made the region Orthodox again."),
     (1918, "secular", SOVIET_EUR),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-karelia", "Karelia", 34.35, 61.79,
     (-10000, "folk", "Finnic Karelians and Vepsians and the Sami of the forests and lakes followed shamans and worshipped nature spirits."),
     (1227, "orthodox", "Prince Yaroslav of Novgorod had many Karelians baptized in 1227, and monasteries such as Valaam spread Orthodoxy through the region."),
     (1918, "secular", SOVIET_EUR),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-north", "Russian North (Arkhangelsk)", 40.54, 64.54,
     (-10000, "folk", "Sami and Finnic hunters and reindeer herders of the White Sea coast followed shamans and worshipped nature spirits."),
     (1400, "orthodox", "Novgorodian Pomors colonized the White Sea coast, and the Solovetsky monastery, founded in 1436, made the north Orthodox."),
     (1918, "secular", "Soviet rule brought state atheism, and the Solovetsky monastery itself became one of the first Gulag prison camps."),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-komi", "Komi", 50.84, 61.67,
     (-10000, "folk", "Finno-Ugric Komi hunters worshipped forest spirits and sacred birches."),
     (1390, "orthodox", "Saint Stephen of Perm converted the Komi in the 1380s, creating an alphabet for them and becoming the first bishop of Perm in 1383."),
     (1918, "secular", "Soviet rule brought state atheism and turned the Komi forests into a vast network of Gulag camps."),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-perm", "Perm and the western Urals", 56.25, 58.01,
     (-10000, "folk", "Komi-Permyak and Mansi hunters of the Kama and the Urals worshipped forest spirits and cast bronze idols in the Perm animal style."),
     (1472, "orthodox", "Moscow annexed Great Perm in 1472, and Russian settlers and the Stroganov merchants made the Kama lands Orthodox in the 16th century."),
     (1918, "secular", SOVIET_EUR),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-tatarstan", "Tatarstan (Kazan)", 49.12, 55.79,
     (-10000, "folk", "Hunters and later Finno-Ugric forest peoples of the middle Volga worshipped nature spirits and ancestors."),
     (700, "tengri", "Turkic Bulgars moving north from the Black Sea steppe founded Volga Bulgaria, bringing the cult of Tengri."),
     (922, "sunni", "King Almysh of Volga Bulgaria adopted Islam and received an embassy from the Abbasid caliph, recorded by Ibn Fadlan, in 922."),
     (1918, "secular", "The Tatars kept Islam after Ivan IV took Kazan in 1552, but after 1917 the Soviets closed mosques and Islamic schools under state atheism."),
     (1991, "sunni", "Islam has revived among the Tatars since 1991, with Kazan's Kul Sharif mosque rebuilt, though Orthodox Russians make up about two fifths of the republic."))

zone("russia-bashkortostan", "Bashkortostan", 55.97, 54.74,
     (-10000, "folk", "Hunters and later herders lived in the forests and steppes of the southern Urals."),
     (800, "tengri", "Turkic Bashkir tribes, herding in the southern Urals, worshipped Tengri and nature spirits."),
     (1320, "sunni", "Islam, known to the Bashkirs through Volga Bulgaria since the 10th century, became their faith under the Golden Horde from the 14th century."),
     (1919, "secular", "The Bashkir republic, formed in 1919, came under Soviet state atheism, and its mosques were closed in the 1930s."),
     (1991, "sunni", "Islam revived after 1991, and Muslims, mostly Bashkirs and Tatars, are the largest religious community in the republic."))

zone("russia-lower-volga", "Lower Volga (Astrakhan)", 48.03, 46.35,
     (-10000, "folk", "Steppe herders, later Scythians and Sarmatians, worshipped Iranian steppe gods on the shores of the Caspian."),
     (370, "tengri", "The Huns crossed the Volga in the 370s, followed by Bulgars and the Khazars, Turkic nomads who honoured the sky god Tengri."),
     (740, "judaism", "The Khazar khagan and his nobles converted to Judaism, traditionally around 740, and ruled from Atil on the lower Volga over a mixed Jewish, Muslim, Christian and pagan population."),
     (965, "tengri", "Prince Sviatoslav of Kiev destroyed the Khazar state in 965, and Oghuz, Pecheneg and Cuman nomads took the steppe."),
     (1313, "sunni", "Uzbek Khan made Islam the faith of the Golden Horde, whose capital Sarai stood on the lower Volga, and its successor the Astrakhan Khanate was Muslim."),
     (1750, "orthodox", "Ivan IV conquered Astrakhan in 1556, and by the 18th century Orthodox Russian settlers outnumbered the Nogai and Tatar Muslims along the lower Volga."),
     (1918, "secular", SOVIET_EUR),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-kalmykia", "Kalmykia", 44.27, 46.31,
     (-10000, "folk", "Steppe herders, later Scythians and Sarmatians, grazed the dry plains west of the lower Volga."),
     (370, "tengri", "Huns, Bulgars, Khazars and Cumans in turn held the steppe and honoured the sky god Tengri."),
     (1313, "sunni", "Under the Golden Horde, Muslim from 1313, and then the Nogai Horde, the steppe was grazed by Muslim nomads."),
     (1630, "vajrayana", "The Kalmyks, Oirat Mongols who followed Tibetan Buddhism, migrated from Dzungaria to the lower Volga in the 1630s and founded the Kalmyk Khanate."),
     (1920, "secular", "Soviet rule closed every Buddhist temple, and in 1943 Stalin deported the entire Kalmyk people to Siberia."),
     (1991, "vajrayana", "Kalmykia revived its Buddhism after 1991 and opened Europe's largest Buddhist temple in Elista in 2005."))

zone("russia-don", "Don Cossack lands (Rostov)", 40.1, 47.42,
     (-10000, "folk", "Steppe herders, later Scythians and Sarmatians, worshipped Iranian steppe gods, while Greeks traded at Tanais at the mouth of the Don."),
     (370, "tengri", "The Huns, Bulgars, Khazars, Pechenegs and Cumans in turn ruled the Don steppe and honoured the sky god Tengri."),
     (1313, "sunni", "Uzbek Khan made Islam the faith of the Golden Horde, which held the Don steppe until the 15th century."),
     (1550, "orthodox", "Orthodox Don Cossacks settled the lower Don in the 16th century and, under the tsars, made it a Russian frontier land."),
     (1918, "secular", "The Don Cossacks fought the Bolsheviks in the civil war, and Soviet rule brought de-Cossackization and state atheism."),
     (1991, "orthodox", REVIVAL_RU))

zone("crimea", "Crimea", 34.1, 44.95,
     (-10000, "folk", "Tauri tribes of the mountains and Scythians of the steppe worshipped local and Iranian steppe gods."),
     (-500, "hellenic", "Greek colonies such as Chersonesos and Panticapaeum built temples to the Olympian gods, and the Bosporan Kingdom later became a Roman client."),
     (400, "christian", "Crimea became Christian through Byzantine Chersonesos and the Crimean Goths, who unlike most Goths kept the Nicene creed."),
     (1054, "orthodox", "After the 1054 schism Crimea's Greeks, Goths and Alans followed Constantinople, while Genoese colonies such as Kaffa were Catholic."),
     (1441, "sunni", "Islam spread among the Crimean Tatars under the Golden Horde, and the Crimean Khanate, founded in 1441, made Crimea a Muslim land."),
     (1860, "orthodox", "After Russia annexed Crimea in 1783, Tatar emigration, above all after the Crimean War, and Russian and Ukrainian settlement made Orthodox Christians the majority."),
     (1920, "secular", "Soviet rule from 1920 brought state atheism, and in 1944 Stalin deported the entire Crimean Tatar people."),
     (1991, "orthodox", "After 1991 Orthodox churches reopened, and Crimean Tatars returning from exile rebuilt their mosques."))

# ---------------- North Caucasus ----------------
zone("russia-kuban", "Kuban and Circassia", 38.98, 45.04,
     (-10000, "folk", "Maeotian and Sindian tribes worshipped local gods in the Kuban valley, while Greeks of the Bosporan Kingdom held the Taman coast."),
     (800, "christian", "Byzantine missions from the 6th century onward and a bishopric of Zichia made the Circassians of the northwest Caucasus largely Christian."),
     (1054, "orthodox", "After the 1054 schism Circassian Christianity looked to Constantinople and Georgia."),
     (1240, "folk", "After the Mongol invasions Circassian Christianity faded into a folk religion that mixed Christian saints with the thunder god Shible and other old gods."),
     (1750, "sunni", "Under Crimean Tatar and Ottoman influence most Circassians converted to Sunni Islam during the 17th and 18th centuries."),
     (1864, "orthodox", "Russia's conquest of the Caucasus ended in 1864 with the expulsion of most Circassians to the Ottoman Empire, and Orthodox Kuban Cossacks settled their lands."),
     (1920, "secular", SOVIET_EUR),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-kabarda", "Kabarda (Kabardino-Balkaria)", 43.61, 43.49,
     (-10000, "folk", "Bronze Age Koban culture peoples and later the Circassian Kabardians worshipped the thunder god Shible and the smith god Tlepsh."),
     (1700, "sunni", "The Kabardian princes took up Islam from the Crimean Tatars in the 16th and 17th centuries, and by the 18th century most Kabardians were Sunni Muslims."),
     (1922, "secular", "Soviet rule over the Kabardino-Balkar autonomy, formed in 1922, brought state atheism, and Stalin deported the Muslim Balkars in 1944."),
     (1991, "sunni", "Islam revived after 1991 and Sunni Muslims are again the majority of the republic."))

zone("russia-ossetia", "North Ossetia (Alania)", 44.68, 43.02,
     (-10000, "folk", "Bronze Age Koban culture peoples and later the Iranian-speaking Alans, ancestors of the Ossetians, worshipped sky and war gods in the central Caucasus."),
     (920, "christian", "Byzantine missionaries sent by Patriarch Nicholas Mystikos baptized the Alan ruler around 916, and Alania became Christian in the 10th century."),
     (1054, "orthodox", "After the 1054 schism Alania stayed in the Orthodox world, with close ties to Byzantium and Georgia."),
     (1239, "folk", "The Mongols destroyed Alania in 1239, and the surviving Ossetians in the mountains blended Christian saints with their old gods in a folk religion."),
     (1774, "orthodox", "Russian missions from 1745 and Russian annexation in 1774 brought most Ossetians back to Orthodoxy, though a minority, mostly Digor nobles, became Muslim."),
     (1920, "secular", SOVIET_EUR),
     (1991, "orthodox", "After 1991 Orthodoxy revived as the majority faith of Ossetians, alongside a revived traditional Ossetian religion and a Muslim minority."))

zone("russia-chechnya", "Chechnya and Ingushetia", 45.7, 43.32,
     (-10000, "folk", "The Vainakh ancestors of the Chechens and Ingush worshipped the sky god Dela and nature spirits at mountain shrines."),
     (1700, "sunni", "Islam spread to the Chechens from Dagestan and the Kumyks in the 17th and 18th centuries, and Sufi leaders such as Sheikh Mansur led resistance to Russia from 1785."),
     (1922, "secular", "Soviet rule closed mosques under state atheism, and in 1944 Stalin deported the entire Chechen and Ingush peoples to Central Asia, where Sufi brotherhoods kept Islam alive."),
     (1991, "sunni", "Islam revived openly after 1991 and nearly all Chechens and Ingush are Sunni Muslims."))

zone("russia-dagestan", "Dagestan", 47.0, 42.7,
     (-10000, "folk", "The many mountain peoples of Dagestan worshipped local gods, sacred groves and ancestors."),
     (1400, "sunni", "Islam, brought to Derbent by the Arab conquerors in the 8th century, spread through the mountain peoples and became the faith of most Dagestanis by the 15th century."),
     (1921, "secular", "The Dagestan republic, formed in 1921, came under Soviet state atheism, which closed almost all of its mosques."),
     (1991, "sunni", "Islam revived quickly after 1991, and Dagestan is now the most devout Muslim region of Russia."))

# ---------------- Siberia and the Far East ----------------
zone("russia-west-siberia", "Western Siberia (Tobolsk)", 68.25, 58.2,
     (-10000, "folk", "Ugric Khanty and Mansi and Samoyed peoples of the Ob basin followed shamans and worshipped forest and river spirits."),
     (1220, "tengri", "Turkic and Mongol Siberian Tatars, under the Golden Horde, brought the steppe cult of Tengri to the southern forest edge."),
     (1563, "sunni", "Khan Kuchum seized the Siberian Khanate in 1563 and promoted Islam as the faith of its Tatar ruling class, though the forest peoples stayed shamanist."),
     (1700, "orthodox", "After Yermak's Cossacks took Sibir in 1582, Tobolsk became the seat of the archbishop of Siberia in 1620, and by about 1700 Orthodox Russians were the majority."),
     (1920, "secular", "Soviet rule reached western Siberia in 1920 and brought state atheism and deportations to the region."),
     (1991, "orthodox", REVIVAL_RU))

zone("russia-south-siberia", "Southern Siberia (Novosibirsk and Altai)", 82.92, 55.03,
     (-10000, "folk", "Siberian hunters and later the Pazyryk herders of the Altai, who buried their chiefs in frozen kurgans, followed shamans and steppe cults."),
     (-200, "tengri", "Xiongnu, Turkic and later Mongol empires dominated the Altai and the upper Ob, home of the first Turkic khaganate, and their peoples worshipped Tengri."),
     (1750, "orthodox", "Russian forts at Tomsk in 1604 and Barnaul in 1730 opened the land to Orthodox settlers, who became the majority in the 18th century."),
     (1920, "secular", "Soviet rule brought state atheism, and in this part of Siberia most people still declare no religion."))

zone("russia-krasnoyarsk", "Central Siberia (Krasnoyarsk)", 92.87, 56.01,
     (-10000, "folk", "Evenk, Ket and Samoyed hunters of the Yenisei basin followed shamans."),
     (-200, "tengri", "The Yenisei Kyrgyz and other Turkic peoples of the upper Yenisei worshipped Tengri, and their khaganate briefly ruled Mongolia after 840."),
     (1700, "orthodox", "Russian forts such as Krasnoyarsk, founded in 1628, and Orthodox peasant settlement made the Yenisei basin Russian and Orthodox by the 18th century."),
     (1920, "secular", "Soviet rule brought state atheism and many Gulag camps to the region, and most people there still declare no religion."))

zone("russia-irkutsk", "Baikal region (Irkutsk)", 104.3, 52.29,
     (-10000, "folk", "Evenk and other Siberian hunters around Lake Baikal followed shamans and revered the lake's spirits."),
     (1200, "tengri", "Mongol and Buryat herders west of Lake Baikal worshipped Tengri, the eternal blue sky, through their shamans."),
     (1750, "orthodox", "Russians founded Irkutsk in 1661, and Orthodox settlers became the majority west of Baikal in the 18th century."),
     (1920, "secular", "Soviet rule brought state atheism, and most people in the region still declare no religion, though Buryat shamanism and Orthodoxy have revived."))

zone("russia-tuva", "Tuva", 94.45, 51.72,
     (-10000, "folk", "Hunters and later Scythian-era herders, who buried their chiefs in the great Arzhan kurgans, lived in the upper Yenisei basin."),
     (-200, "tengri", "Xiongnu, Turkic and Uyghur rulers in turn held the Tuvan basin, whose people worshipped Tengri through shamans."),
     (1750, "vajrayana", "Under Qing rule from 1757, Mongolian lamas spread Tibetan Buddhism, and by the 19th century most Tuvans were Buddhists who also honoured shamans."),
     (1930, "secular", "The Tuvan People's Republic, a Soviet satellite from 1921, destroyed its monasteries in the 1930s and joined the Soviet Union in 1944."),
     (1991, "vajrayana", "Buddhism revived after 1991 and is again the main religion of Tuva, which the Dalai Lama visited in 1992."))

zone("russia-buryatia", "Buryatia", 107.58, 51.83,
     (-10000, "folk", "Hunters and later herders lived east of Lake Baikal, following shamans."),
     (1200, "tengri", "Buryat Mongols east of Lake Baikal worshipped Tengri and their ancestors through shamans."),
     (1741, "vajrayana", "Tibetan Buddhism reached the Buryats from Mongolia in the 17th century, and in 1741 Empress Elizabeth recognized their lamas, making it the main faith east of Baikal."),
     (1923, "secular", "The Buryat-Mongol republic of 1923 came under state atheism, and in the 1930s its datsans were closed and thousands of lamas shot or imprisoned."),
     (1991, "orthodox", "After 1991 Buddhism revived at datsans such as Ivolginsky, but Russians are now about two thirds of the republic and Orthodoxy is its largest faith."))

zone("russia-yakutia", "Yakutia (Sakha)", 129.73, 62.03,
     (-10000, "folk", "Evenk and Yukaghir hunters and reindeer herders of the Lena basin followed shamans."),
     (1300, "tengri", "Turkic Sakha herders migrating from the Baikal region brought horses, cattle and the worship of the sky god Tangara and the Aiyy spirits."),
     (1800, "orthodox", "After the Russians founded Yakutsk in 1632, missionaries baptized most Sakha by the early 19th century, though shamanism endured."),
     (1922, "secular", "The Yakut republic, formed in 1922, came under state atheism, and today most of its people follow no organized religion, with Orthodoxy and the revived Aiyy faith the largest."))

zone("russia-amur", "Amur region (Khabarovsk)", 135.07, 48.48,
     (-10000, "folk", "Tungusic Nanai, Ulch and Evenk fishermen and hunters of the Amur followed shamans and honoured river and tiger spirits."),
     (1880, "orthodox", "China ceded the left bank of the Amur in 1858 and the Ussuri lands in 1860, and Orthodox Russian and Ukrainian settlers became the majority by the 1880s."),
     (1922, "secular", "The Far East came under Soviet rule in 1922 and state atheism, and most people in the region still follow no religion."))

zone("russia-primorye", "Primorye (Vladivostok)", 132.0, 43.8,
     (-10000, "folk", "Tungusic forest peoples of the Ussuri valley and the Pacific coast followed shamans."),
     (698, "mahayana", "The kingdom of Balhae, founded in 698, ruled Primorye, and its kings built Buddhist temples alongside the shaman cults of their Mohe subjects."),
     (926, "folk", "The Khitans destroyed Balhae in 926, and the Jurchen, Udege and Nanai forest peoples of Primorye kept their shamanist religion."),
     (1880, "orthodox", "China ceded Primorye to Russia in 1860, and Orthodox Russian and Ukrainian settlers, many arriving by sea at Vladivostok, became the majority by the 1880s."),
     (1922, "secular", "The Far East came under Soviet rule in 1922 and state atheism, and most people in Primorye still follow no religion."))

zone("russia-sakhalin", "Sakhalin", 142.7, 47.5,
     (-10000, "folk", "The Ainu in the south and the Nivkh in the north of Sakhalin honoured bear and sea spirits."),
     (1875, "orthodox", "Russia took the whole island in 1875 and made it a penal colony, whose Orthodox convicts and settlers soon outnumbered the native peoples."),
     (1905, "shinto", "Japan took southern Sakhalin as Karafuto in 1905, and its Japanese settlers built Shinto shrines and Buddhist temples."),
     (1945, "secular", "The Soviet Union seized Karafuto in 1945, sent its Japanese back to Japan and resettled it with Soviet citizens under state atheism."))

zone("russia-kamchatka", "Kamchatka", 158.65, 53.02,
     (-10000, "folk", "Itelmen and Koryak fishermen and reindeer herders followed shamans and honoured the raven creator Kutkh."),
     (1750, "orthodox", "After Russian Cossacks conquered Kamchatka between 1697 and 1731, missionaries baptized the Itelmens in the 1740s and Russians settled the peninsula."),
     (1922, "secular", "The Far East came under Soviet rule in 1922 and state atheism, and most people in Kamchatka still follow no religion."))

zone("russia-magadan", "Kolyma (Magadan)", 150.8, 59.56,
     (-10000, "folk", "Even, Koryak and Yukaghir reindeer herders of the Kolyma and the Okhotsk coast followed shamans."),
     (1930, "secular", "Soviet collectivization of the herders and, from 1932, the Kolyma Gulag camps served by the new port of Magadan brought state atheism to a land with few churches."))

zone("russia-chukotka", "Chukotka", 177.5, 64.73,
     (-10000, "folk", "Chukchi and Yupik reindeer herders and sea hunters of the far northeast followed shamans and resisted both Russian conquest and baptism."),
     (1930, "secular", "Soviet rule reached Chukotka in the 1920s, and collectivization in the 1930s suppressed the shamans."))

# ---------------- South Caucasus ----------------
zone("georgia", "Georgia", 44.79, 41.72,
     (-10000, "folk", "Early farmers of the Shulaveri culture, and later the kingdoms of Colchis and Iberia, worshipped local gods such as Armazi alongside Iranian and Greek cults."),
     (337, "christian", "King Mirian III of Iberia, converted by Saint Nino, made Christianity the state religion in the 330s."),
     (1054, "orthodox", "Georgia, which had accepted Chalcedon and broken with the Armenian church in 607, followed Constantinople after 1054 and flourished under King David IV and Queen Tamar."),
     (1921, "secular", "The Red Army conquered Georgia in 1921 and imposed Soviet state atheism, closing most of its churches and monasteries."),
     (1991, "orthodox", "Independence in 1991 brought a strong Orthodox revival, and over 80 percent of Georgians now identify as Orthodox."))

zone("armenia", "Armenia", 44.51, 40.18,
     (-10000, "folk", "Early farmers and Bronze Age peoples of the Armenian Highlands, whose Areni cave held the oldest known winery, worshipped local gods."),
     (-860, "mesopotamian", "The kingdom of Urartu, which founded Erebuni, today's Yerevan, in 782 BC, worshipped Haldi and Teisheba in a religion close to the Hurrian and Assyrian cults."),
     (-550, "zoroastrianism", "Under the Persian Achaemenids and later Armenian kings, Armenians worshipped Iranian gods such as Aramazd, Anahit and Mihr."),
     (301, "christian", "King Tiridates III, converted by Gregory the Illuminator, made Armenia the first state to adopt Christianity, traditionally in 301."),
     (506, "oriental", "The Armenian church rejected the Council of Chalcedon at the Councils of Dvin in 506 and 554, becoming an Oriental Orthodox church."),
     (1920, "secular", "Soviet Armenia, proclaimed in 1920, imposed state atheism and closed most churches until a partial thaw after 1945."),
     (1991, "oriental", "Independence in 1991 restored the Armenian Apostolic Church, to which over 90 percent of Armenians belong."))

zone("azerbaijan", "Azerbaijan", 48.9, 40.5,
     (-10000, "folk", "Stone Age hunters at Gobustan carved thousands of rock engravings, and later the Caucasian Albanian tribes worshipped sun and moon gods."),
     (-550, "zoroastrianism", "Under the Medes, Achaemenids and later the Sasanians, Zoroastrian fire worship spread, fed by the burning gas vents of Absheron."),
     (330, "christian", "King Urnayr of Caucasian Albania accepted Christianity in the 4th century, and its church developed in close ties with the Armenian church."),
     (506, "oriental", "The bishops of Caucasian Albania joined the Armenian rejection of the Council of Chalcedon at Dvin in 506."),
     (861, "sunni", "After the Arab conquest of the 7th century, Islam spread through Arran and Shirvan, whose Shirvanshahs ruled as Sunni Muslims from 861."),
     (1501, "shia", "Shah Ismail I took Shirvan and Baku in 1500 and 1501 and imposed Twelver Shia Islam on the Safavid realm."),
     (1920, "secular", "The Red Army took Baku in 1920, and Soviet rule closed most mosques under state atheism."),
     (1991, "shia", "Independence in 1991 brought an Islamic revival, and about two thirds of Azerbaijanis are Shia Muslims, most of the rest Sunni."))

with open(os.path.join(H, "zones_east_europe.json"), "w") as f:
    json.dump(Z, f, ensure_ascii=False, indent=1)
print(len(Z), "zones written")

"""Generate zones_west_europe.json (religious history zones for Western Europe)."""
import json, os

Z = []


def zone(id, name, lon, lat, hist):
    Z.append({"id": id, "name": name, "lon": lon, "lat": lat,
              "history": [{"from": f, "faith": r, "note": n} for f, r, n in hist]})


# Shared entries
SCHISM = "The Great Schism of 1054 split Rome from Constantinople, and {} stayed with the Latin church under the Pope."
GDR = "Under the communist GDR, church pressure and secular youth dedication drove most East Germans out of the churches by about 1970."

# ---------------------------------------------------------------- British Isles
zone("england", "England", -0.12, 51.5, [
    (-10000, "folk", "Neolithic and Bronze Age Britons built Stonehenge and Avebury to honour the sun, the seasons and the dead."),
    (-600, "pagan-europe", "Celtic Britons worshipped gods such as Lugus and Brigantia, led by a priestly class of druids."),
    (43, "hellenic", "The Roman conquest under Claudius brought the Roman gods, the emperor cult and temples such as that of Claudius at Colchester."),
    (380, "christian", "Theodosius made Christianity the Roman state religion, and late Roman Britain had bishops and Christian villas."),
    (450, "pagan-europe", "After Rome left, Anglo-Saxon settlers took most of England and brought the worship of Woden, Thunor and Frig."),
    (597, "christian", "Augustine's mission from Pope Gregory baptised King Aethelberht of Kent, and by 686 every Anglo-Saxon kingdom had converted."),
    (1054, "catholic", SCHISM.format("England")),
    (1534, "anglican", "Henry VIII's Act of Supremacy broke with Rome and made the king head of the Church of England."),
    (1553, "catholic", "Mary I restored Catholicism and papal authority and burned nearly 300 Protestants."),
    (1559, "anglican", "Elizabeth I's religious settlement re-established the Church of England with the Book of Common Prayer."),
    (1646, "reformed", "During the Civil War Parliament abolished bishops and the Prayer Book and set up a Presbyterian and Puritan state church."),
    (1660, "anglican", "The Restoration of Charles II brought back bishops and the Book of Common Prayer, and the Church of England has remained the established church."),
])

zone("northumbria", "Northumbria and York", -1.08, 53.96, [
    (-10000, "folk", "Neolithic farmers raised henges and stone circles across the north of England."),
    (-600, "pagan-europe", "The Celtic Brigantes worshipped their goddess Brigantia and other Celtic gods."),
    (71, "hellenic", "Rome conquered the Brigantes and founded the fortress of Eboracum (York), where Constantine was proclaimed emperor in 306."),
    (380, "christian", "Christianity became the Roman state religion; York already had a bishop at the Council of Arles in 314."),
    (450, "pagan-europe", "Anglian settlers founded the pagan kingdoms of Deira and Bernicia."),
    (627, "christian", "King Edwin was baptised at York by Paulinus, and Aidan's Irish monks from Lindisfarne completed the conversion of Northumbria."),
    (866, "pagan-europe", "The Danish Great Heathen Army took York and founded a pagan Viking kingdom there."),
    (900, "christian", "The Viking kings of York quickly accepted Christianity, minting coins in honour of Saint Peter."),
    (1054, "catholic", SCHISM.format("Northumbria")),
    (1534, "anglican", "Henry VIII's break with Rome made the Church of England the state church; the north rose against it in the Pilgrimage of Grace (1536)."),
    (1553, "catholic", "Mary I restored Catholicism and papal authority."),
    (1559, "anglican", "Elizabeth I re-established the Church of England, crushing the Catholic Rising of the North in 1569."),
])

zone("wales", "Wales", -3.6, 52.3, [
    (-10000, "folk", "Neolithic Welsh farmers built chambered tombs such as Bryn Celli Ddu."),
    (-600, "pagan-europe", "Celtic Britons followed the druids, whose sanctuary on Anglesey the Romans destroyed in AD 60."),
    (78, "hellenic", "Agricola completed the Roman conquest of Wales, bringing the Roman gods to forts and mining towns."),
    (380, "christian", "Christianity became the Roman state religion, and after Rome left the Welsh kept it through saints such as David and Teilo."),
    (1054, "catholic", "The Great Schism left Wales in the Latin church, and after the Norman conquest its bishops submitted to Canterbury from 1107."),
    (1536, "anglican", "The Laws in Wales Acts and Henry VIII's Reformation placed Wales in the Church of England."),
    (1553, "catholic", "Mary I briefly restored Catholicism and papal authority."),
    (1559, "anglican", "Elizabeth I re-established the Church of England, and William Morgan's Welsh Bible of 1588 bound it to the Welsh language."),
    (1811, "protestant", "The Calvinistic Methodists left the Church of England in 1811, and the 1851 religious census showed most Welsh worshippers were Nonconformist chapel goers."),
    (2021, "secular", "In the 2021 census 46.5% of people in Wales said they had no religion, more than all Christians together (43.6%)."),
])

zone("scotland", "Scotland", -3.94, 56.12, [
    (-10000, "folk", "Neolithic Scots built Skara Brae, Maeshowe and stone circles such as Callanish."),
    (-600, "pagan-europe", "The Celtic Picts and Britons worshipped Celtic gods, leaving carved symbol stones."),
    (600, "christian", "Columba's monastery on Iona (563) and his successors converted the Picts and Scots to Christianity."),
    (1054, "catholic", SCHISM.format("Scotland")),
    (1560, "reformed", "The Reformation Parliament, led by John Knox, abolished papal authority and made the Presbyterian Church of Scotland the national church."),
    (2015, "secular", "By the mid 2010s most Scots told surveys they had no religion, and the 2022 census confirmed a majority (51%) with none."),
])

zone("orkney", "Orkney and the Northern Isles", -3.0, 58.98, [
    (-10000, "folk", "Neolithic Orcadians built the Ring of Brodgar, the Stones of Stenness and the tomb of Maeshowe."),
    (-600, "pagan-europe", "Iron Age Picts worshipped Celtic gods and built broch towers."),
    (700, "christian", "Irish and Pictish monks brought Christianity to the islands."),
    (850, "pagan-europe", "Norse Vikings settled Orkney and Shetland and brought the worship of Odin and Thor."),
    (995, "christian", "King Olaf Tryggvason of Norway forced Earl Sigurd of Orkney to accept baptism."),
    (1054, "catholic", "The Great Schism left Orkney in the Latin church, and Earl Rognvald began Saint Magnus Cathedral in 1137."),
    (1560, "reformed", "Pledged to Scotland since 1468, the islands followed the Scottish Reformation into the Presbyterian Church of Scotland."),
    (2015, "secular", "Like the rest of Scotland, most islanders now say they have no religion."),
])

zone("ireland", "Ireland", -7.9, 53.4, [
    (-10000, "folk", "Neolithic Irish built the passage tombs of Newgrange and Knowth, aligned with the winter sunrise."),
    (-500, "pagan-europe", "Celtic Irish worshipped gods such as the Dagda, Lugh and Brigid, led by druids and filid."),
    (500, "christian", "Saint Patrick's mission in the 5th century converted Ireland, which became a land of great monasteries."),
    (1054, "catholic", "The Great Schism left Ireland in the Latin church, and Ireland stayed Catholic despite the Anglican Church of Ireland being established from 1536 to 1871."),
])

zone("northern-ireland", "Northern Ireland (Ulster)", -6.1, 54.6, [
    (-10000, "folk", "Neolithic farmers built court tombs and stone circles across Ulster."),
    (-500, "pagan-europe", "Celtic Ulaid worshipped their gods at Emain Macha, the royal site near Armagh."),
    (450, "christian", "Saint Patrick founded his principal church at Armagh, and Ulster became Christian."),
    (1054, "catholic", SCHISM.format("Ulster")),
    (1690, "reformed", "The Plantation of Ulster (1609) and a wave of Scots settlers after William III's victory of 1690 made Protestants the majority in the east, with Presbyterians the largest church."),
    (2021, "catholic", "The 2021 census found people of Catholic background outnumbering Protestants in Northern Ireland for the first time."),
])

# ---------------------------------------------------------------- France
zone("france-north", "Northern France (Paris)", 2.35, 48.86, [
    (-10000, "folk", "Neolithic farmers raised the great standing stones and dolmens of Brittany and the north."),
    (-800, "pagan-europe", "The Celtic Gauls worshipped gods such as Lugus, Teutates and Epona, led by druids."),
    (-50, "hellenic", "Julius Caesar's conquest of Gaul brought the Roman gods and the cult of the emperor."),
    (380, "christian", "Christianity became the Roman state religion, and Saint Martin of Tours had already spread it in rural Gaul; Clovis made the Franks Christian around 496."),
    (1054, "catholic", "The Great Schism left France in the Latin church; the Huguenot Protestants remained a minority, outlawed in 1685."),
])

zone("france-south", "Southern France (Toulouse)", 1.44, 43.6, [
    (-10000, "folk", "Prehistoric peoples of the south left the painted caves and megaliths of the Pyrenees and Languedoc."),
    (-800, "pagan-europe", "Celtic Volcae and Aquitanian tribes worshipped their own gods."),
    (-121, "hellenic", "Rome annexed southern Gaul as Gallia Narbonensis, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion."),
    (418, "arian", "The Visigoths founded their kingdom at Toulouse and ruled as Arian Christians over a Nicene Gallo-Roman population."),
    (507, "christian", "Clovis, a Nicene Christian, defeated the Visigoths at Vouille and took Aquitaine for the Franks."),
    (1054, "catholic", "The Great Schism left the south in the Latin church; the Cathar heresy was crushed by the Albigensian Crusade from 1209."),
])

zone("septimania", "Septimania and Languedoc (Narbonne)", 3.0, 43.18, [
    (-10000, "folk", "Prehistoric farmers and herders of the Mediterranean coast honoured local spirits and ancestors."),
    (-118, "hellenic", "Rome founded Narbo Martius, the first Roman colony in Gaul, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion."),
    (462, "arian", "Narbonne passed to the Visigoths, who kept Septimania as part of their Arian kingdom."),
    (589, "christian", "King Reccared converted the Visigothic kingdom to Nicene Christianity at the Third Council of Toledo."),
    (720, "sunni", "The Umayyads took Narbonne and ruled Septimania from al-Andalus."),
    (759, "christian", "Pepin the Short retook Narbonne, bringing Septimania into the Christian Frankish kingdom."),
    (1054, "catholic", SCHISM.format("Languedoc")),
])

zone("burgundy", "Burgundy and Lyon", 4.83, 45.76, [
    (-10000, "folk", "Neolithic farmers of the Rhone and Saone valleys honoured local gods and the dead."),
    (-800, "pagan-europe", "The Celtic Aedui and Allobroges worshipped Celtic gods; Lugdunum was named for the god Lugus."),
    (-43, "hellenic", "Rome founded Lugdunum (Lyon), the capital of the Gauls with an altar to Rome and Augustus."),
    (380, "christian", "Christianity, rooted in Lyon since the martyrs of 177 and Bishop Irenaeus, became the state religion."),
    (461, "arian", "The Burgundians took Lyon and ruled as Arian Christians over Nicene Gallo-Romans."),
    (516, "christian", "King Sigismund, a convert to Nicene Christianity, brought the Burgundian kingdom into the Catholic church."),
    (1054, "catholic", "The Great Schism left Burgundy in the Latin church; Cluny Abbey (910) led Catholic reform from here."),
])

zone("provence", "Provence (Marseille)", 5.37, 43.3, [
    (-10000, "folk", "Ligurian peoples of the coast honoured local gods at hilltop sanctuaries."),
    (-600, "hellenic", "Phocaean Greeks founded Massalia (Marseille), bringing the Greek gods; Rome later took over the region."),
    (380, "christian", "Christianity became the Roman state religion, and the monasteries of Lerins and Saint Victor flourished here."),
    (476, "arian", "The Visigoths and then the Ostrogoths ruled Provence as Arian Christians."),
    (536, "christian", "The Ostrogoths ceded Provence to the Nicene Christian Franks."),
    (1054, "catholic", "The Great Schism left Provence in the Latin church, and the popes lived at Avignon from 1309 to 1377."),
])

zone("corsica", "Corsica", 9.05, 42.15, [
    (-10000, "folk", "Prehistoric Corsicans carved stone statue-menhirs such as those of Filitosa."),
    (-237, "hellenic", "Rome conquered Corsica from Carthage, bringing the Roman gods."),
    (400, "christian", "Christianity spread across the island in late Roman times."),
    (456, "arian", "The Arian Vandals seized Corsica from their kingdom in Africa."),
    (534, "christian", "Justinian's Byzantine army conquered the Vandals and returned Corsica to Nicene rule."),
    (1054, "catholic", "The Great Schism left Corsica in the Latin church, under Pisa and then Genoa."),
])

# ---------------------------------------------------------------- Low Countries
zone("belgium", "Belgium", 4.35, 50.85, [
    (-10000, "folk", "Neolithic farmers of the Meuse and Scheldt valleys honoured local spirits and their dead."),
    (-500, "pagan-europe", "The Celtic and Germanic Belgae worshipped their tribal gods."),
    (-50, "hellenic", "Caesar's conquest of the Belgae brought the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion; Saint Servatius was bishop at Tongeren."),
    (450, "pagan-europe", "Pagan Salian Franks settled the land and ruled from Tournai."),
    (650, "christian", "After Clovis's baptism, missionaries such as Amand and Eligius converted rural Flanders and Brabant in the 7th century."),
    (1054, "catholic", "The Great Schism left the land in the Latin church, and Spanish rule held it Catholic after the Calvinist revolt of 1566 to 1585."),
])

zone("netherlands", "Netherlands (Holland and the north)", 5.12, 52.09, [
    (-10000, "folk", "Prehistoric farmers built the hunebed megalithic tombs of Drenthe."),
    (-500, "pagan-europe", "The Germanic Frisians worshipped gods such as Fosite and Woden."),
    (734, "christian", "Charles Martel's victory over the Frisians opened the land to Willibrord, bishop of Utrecht, and Boniface, killed at Dokkum in 754."),
    (1054, "catholic", SCHISM.format("the Netherlands")),
    (1572, "reformed", "In the Dutch Revolt Holland and Zeeland made the Calvinist Reformed Church the public church, though Catholics stayed a large tolerated minority."),
    (1990, "secular", "Rapid secularisation from the 1960s made the non-religious the largest group, and a majority by the 2010s."),
])

zone("netherlands-south", "North Brabant and Limburg", 5.48, 51.44, [
    (-10000, "folk", "Neolithic farmers of the Meuse valley honoured local spirits and ancestors."),
    (-500, "pagan-europe", "Germanic and Celtic tribes worshipped their own gods."),
    (-50, "hellenic", "Roman conquest brought the Roman gods; Maastricht grew on the Meuse crossing."),
    (380, "christian", "Christianity became the Roman state religion, and Saint Servatius made Maastricht a Christian centre."),
    (450, "pagan-europe", "Pagan Franks settled the region."),
    (700, "christian", "Willibrord and Lambert of Maastricht completed the conversion of Brabant and Limburg."),
    (1054, "catholic", "The Great Schism left the region in the Latin church, and it stayed Catholic even under Calvinist Dutch rule after 1629."),
])

zone("luxembourg", "Luxembourg", 6.13, 49.61, [
    (-10000, "folk", "Neolithic farmers honoured local spirits and the dead."),
    (-500, "pagan-europe", "The Celtic Treveri worshipped gods such as Lenus Mars."),
    (-50, "hellenic", "Caesar's conquest brought Roman gods to the land around Trier."),
    (400, "christian", "Christianity spread from Trier, an imperial capital and early bishopric."),
    (460, "pagan-europe", "Pagan Franks took over the region."),
    (700, "christian", "Willibrord founded Echternach Abbey in 698 and completed the land's conversion."),
    (1054, "catholic", SCHISM.format("Luxembourg")),
])

# ---------------------------------------------------------------- Switzerland
zone("switzerland-reformed", "Zurich, Bern and Basel (Reformed Switzerland)", 8.0, 47.2, [
    (-10000, "folk", "Neolithic lake dwellers honoured local spirits along the Swiss lakes."),
    (-500, "pagan-europe", "The Celtic Helvetii worshipped Celtic gods."),
    (-15, "hellenic", "Augustus brought the Helvetii and Raetians into the Roman Empire and its gods."),
    (400, "christian", "Christianity spread through Roman towns such as Augusta Raurica and Vindonissa."),
    (450, "pagan-europe", "Pagan Alemanni settled the Swiss plateau."),
    (650, "christian", "Irish monks Columbanus and Gallus converted the Alemanni, and Saint Gall became a famous abbey."),
    (1054, "catholic", SCHISM.format("the Swiss plateau")),
    (1523, "reformed", "Huldrych Zwingli's Reformation was adopted by Zurich in 1523, Bern in 1528 and Basel in 1529."),
    (2015, "secular", "By the 2010s people with no religion outnumbered both Reformed and Catholic members in Zurich, Basel and Bern."),
])

zone("switzerland-catholic", "Central Switzerland (Lucerne and the Forest Cantons)", 8.5, 46.75, [
    (-10000, "folk", "Prehistoric Alpine peoples honoured mountain and lake spirits."),
    (-500, "pagan-europe", "The Celtic Helvetii worshipped Celtic gods."),
    (-15, "hellenic", "Augustus conquered the Alpine tribes, bringing the Roman gods."),
    (400, "christian", "Christianity reached the Alpine valleys in late Roman times."),
    (450, "pagan-europe", "Pagan Alemanni settled the valleys."),
    (700, "christian", "Frankish and Irish missionaries converted the Alemanni, and Lucerne grew around its monastery."),
    (1054, "catholic", "The Great Schism left the region in the Latin church, and the Forest Cantons defended Catholicism at Kappel in 1531."),
])

zone("geneva", "Geneva and Romandy", 6.14, 46.2, [
    (-10000, "folk", "Neolithic lake dwellers honoured local spirits on Lake Geneva."),
    (-500, "pagan-europe", "The Celtic Allobroges and Helvetii worshipped Celtic gods."),
    (-121, "hellenic", "Rome conquered the Allobroges, bringing the Roman gods to Genava."),
    (400, "christian", "Christianity spread in the Roman towns, and Geneva had a bishop by about 400."),
    (443, "arian", "The Arian Burgundians settled in Sapaudia and made Geneva their first capital."),
    (516, "christian", "King Sigismund, a Nicene convert who founded Saint Maurice Abbey, brought the Burgundians into the Catholic church."),
    (1054, "catholic", SCHISM.format("Geneva")),
    (1536, "reformed", "Geneva expelled its bishop and adopted the Reformation, and John Calvin made it the 'Protestant Rome'."),
    (1860, "catholic", "Catholic communes joined in 1815 and Catholic immigrants made Catholics the majority in canton Geneva by about 1860."),
    (2010, "secular", "By the 2010s people with no religion were the largest group in Geneva."),
])

# ---------------------------------------------------------------- Germany
zone("lower-saxony", "Lower Saxony and Hanover", 9.73, 52.37, [
    (-10000, "folk", "Neolithic farmers built megalithic graves across the north German plain."),
    (-500, "pagan-europe", "The Germanic Saxons worshipped Woden, Thunar and the sacred pillar Irminsul."),
    (785, "christian", "Charlemagne's Saxon Wars forced the conversion of the Saxons, and their leader Widukind was baptised in 785."),
    (1054, "catholic", SCHISM.format("Saxony")),
    (1527, "lutheran", "Duke Ernest the Confessor introduced the Lutheran Reformation in Luneburg, followed by Brunswick and Calenberg."),
])

zone("schleswig-holstein", "Schleswig-Holstein", 9.99, 54.07, [
    (-10000, "folk", "Neolithic farmers built megalithic tombs across the peninsula."),
    (-500, "pagan-europe", "Angles, Saxons and Jutes worshipped Germanic gods before many crossed to Britain."),
    (850, "christian", "Charlemagne's conquest of Nordalbingia and Ansgar's mission from Hamburg brought Christianity to Holstein."),
    (1054, "catholic", SCHISM.format("Holstein")),
    (1542, "lutheran", "King Christian III of Denmark imposed Bugenhagen's Lutheran church order on the duchies."),
])

zone("mecklenburg", "Mecklenburg", 11.41, 53.63, [
    (-10000, "folk", "Neolithic farmers built megalithic graves along the Baltic coast."),
    (-500, "pagan-europe", "Germanic and, from about 600, Slavic Obotrites worshipped gods such as Svantevit and Radegast."),
    (1160, "catholic", "Henry the Lion conquered the Obotrites after the Wendish Crusade and founded the bishopric of Schwerin."),
    (1549, "lutheran", "The Sternberg diet of 1549 made Mecklenburg Lutheran."),
    (1970, "secular", GDR),
])

zone("brandenburg", "Brandenburg and Berlin", 13.4, 52.52, [
    (-10000, "folk", "Neolithic and Bronze Age farmers honoured local spirits and the dead."),
    (-500, "pagan-europe", "Germanic Semnones and later Slavic Hevelli and Sprevane worshipped their own gods."),
    (948, "christian", "Otto I founded the bishopric of Brandenburg to convert the Slavs."),
    (983, "pagan-europe", "The great Slav uprising of 983 drove out German priests and restored the old gods."),
    (1157, "catholic", "Albert the Bear took Brandenburg and German settlers made the Mark Catholic."),
    (1539, "lutheran", "Elector Joachim II adopted the Lutheran Reformation; later Hohenzollerns turned Calvinist in 1613 but their subjects stayed Lutheran."),
    (1970, "secular", GDR),
])

zone("pomerania", "Pomerania (Szczecin)", 14.55, 53.43, [
    (-10000, "folk", "Neolithic farmers honoured local spirits on the Baltic coast."),
    (-500, "pagan-europe", "Slavic Pomeranians worshipped the three-headed god Triglav at Szczecin."),
    (1128, "catholic", "Bishop Otto of Bamberg's missions of 1124 and 1128 converted the Pomeranians."),
    (1534, "lutheran", "The diet of Treptow made Pomerania Lutheran."),
    (1945, "catholic", "After the Second World War the Germans were expelled and Catholic Poles settled western Pomerania."),
])

zone("east-prussia", "East Prussia (Konigsberg, now Kaliningrad)", 20.51, 54.71, [
    (-10000, "folk", "Prehistoric Baltic peoples honoured nature spirits."),
    (-500, "pagan-europe", "The Baltic Old Prussians worshipped gods such as Perkunas at the sacred grove of Romuva."),
    (1283, "catholic", "The Teutonic Knights completed their crusade against the Prussians and settled the land with German Catholics."),
    (1525, "lutheran", "Grand Master Albert secularised the order's state as the Duchy of Prussia, the first Lutheran state."),
    (1945, "secular", "The Soviet Union annexed the region as Kaliningrad, expelled the Germans and suppressed religion."),
    (1991, "orthodox", "After the Soviet collapse the Russian population of Kaliningrad largely returned to Russian Orthodoxy."),
])

zone("saxony", "Saxony (Dresden and Meissen)", 13.74, 51.05, [
    (-10000, "folk", "Neolithic farmers honoured local spirits along the Elbe."),
    (-500, "pagan-europe", "Germanic tribes and, from about 600, Slavic Sorbs worshipped their own gods."),
    (968, "christian", "Otto I founded the bishopric of Meissen and German lords converted the Sorbs."),
    (1054, "catholic", SCHISM.format("Saxony")),
    (1539, "lutheran", "Duke Henry made Albertine Saxony Lutheran; it stayed so even after Augustus the Strong turned Catholic to win Poland in 1697."),
    (1970, "secular", GDR),
])

zone("thuringia", "Thuringia and Wittenberg", 11.5, 51.2, [
    (-10000, "folk", "Neolithic farmers honoured local spirits and the dead."),
    (-500, "pagan-europe", "The Germanic Thuringians worshipped their tribal gods."),
    (725, "christian", "Boniface converted the Thuringians and founded the bishopric of Erfurt in 742."),
    (1054, "catholic", SCHISM.format("Thuringia")),
    (1525, "lutheran", "The Ernestine Saxon electors, protectors of Martin Luther at Wittenberg, made their lands the first Lutheran territory."),
    (1970, "secular", GDR),
])

zone("hesse", "Hesse (Kassel and Marburg)", 9.3, 51.0, [
    (-10000, "folk", "Neolithic farmers honoured local spirits and the dead."),
    (-500, "pagan-europe", "The Germanic Chatti worshipped Donar and Wodan."),
    (723, "christian", "Boniface felled Donar's sacred oak at Geismar and converted the Hessians."),
    (1054, "catholic", SCHISM.format("Hesse")),
    (1527, "lutheran", "Landgrave Philip of Hesse adopted the Reformation and founded the Protestant University of Marburg."),
    (1605, "reformed", "Landgrave Maurice of Hesse-Kassel imposed Calvinist reforms on his church."),
])

zone("westphalia", "Westphalia (Munster)", 7.63, 51.96, [
    (-10000, "folk", "Neolithic farmers built megalithic graves in the lowlands."),
    (-500, "pagan-europe", "The Germanic Saxons and Bructeri worshipped their tribal gods."),
    (785, "christian", "Charlemagne conquered the Saxons and Liudger became first bishop of Munster."),
    (1054, "catholic", "The Great Schism left Westphalia in the Latin church, and the prince-bishops of Munster crushed the Anabaptist kingdom of 1534 to 1535."),
])

zone("rhineland", "Rhineland (Cologne)", 6.96, 50.94, [
    (-10000, "folk", "Neolithic farmers settled the Rhine valley and honoured local spirits."),
    (-500, "pagan-europe", "Celtic and Germanic tribes such as the Ubii worshipped their gods."),
    (-38, "hellenic", "Rome settled the Ubii at the site of Cologne, later Colonia Agrippina, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion; Cologne had a bishop by 313."),
    (460, "pagan-europe", "The pagan Ripuarian Franks took Cologne."),
    (500, "christian", "Following Clovis's baptism the Franks of the Rhine became Christian."),
    (1054, "catholic", "The Great Schism left the Rhineland in the Latin church; the archbishops of Cologne kept it Catholic and it stayed so under Protestant Prussia."),
])

zone("mainz", "Mainz and the Middle Rhine", 8.27, 50.0, [
    (-10000, "folk", "Neolithic farmers of the Rhine and Main honoured local spirits."),
    (-500, "pagan-europe", "Celtic and later Germanic tribes worshipped their gods."),
    (-13, "hellenic", "Rome founded the legionary fortress of Mogontiacum (Mainz), bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion."),
    (406, "pagan-europe", "Vandals, Alans and Alemanni crossed the Rhine and sacked Mainz, followed by pagan Franks."),
    (500, "christian", "The Franks converted after Clovis, and Boniface later made Mainz the archbishopric of Germany."),
    (1054, "catholic", "The Great Schism left the Middle Rhine in the Latin church under the prince-archbishops of Mainz."),
])

zone("palatinate", "Electoral Palatinate (Heidelberg)", 8.69, 49.4, [
    (-10000, "folk", "Neolithic farmers of the Rhine plain honoured local spirits."),
    (-500, "pagan-europe", "Celtic and Germanic tribes worshipped their gods."),
    (74, "hellenic", "Rome annexed the land east of the Rhine, bringing the Roman gods."),
    (260, "pagan-europe", "The pagan Alemanni overran the Roman frontier."),
    (500, "christian", "Clovis defeated the Alemanni, and the region was converted under Frankish rule."),
    (1054, "catholic", SCHISM.format("the Palatinate")),
    (1556, "lutheran", "Elector Otto Henry introduced the Lutheran Reformation."),
    (1563, "reformed", "Elector Frederick III turned to Calvinism and issued the Heidelberg Catechism."),
])

zone("wurttemberg", "Wurttemberg (Stuttgart)", 9.18, 48.78, [
    (-10000, "folk", "Neolithic farmers honoured local spirits along the Neckar."),
    (-500, "pagan-europe", "The Celts built princely hill forts such as the Heuneburg and worshipped Celtic gods."),
    (74, "hellenic", "Rome annexed the Neckar lands, bringing the Roman gods."),
    (260, "pagan-europe", "The pagan Alemanni overran the Roman frontier."),
    (650, "christian", "Frankish rule and the bishopric of Constance completed the conversion of the Alemanni."),
    (1054, "catholic", SCHISM.format("Swabia")),
    (1534, "lutheran", "Duke Ulrich regained Wurttemberg and introduced the Lutheran Reformation."),
])

zone("baden", "Baden and the Breisgau (Freiburg)", 7.85, 48.0, [
    (-10000, "folk", "Neolithic farmers honoured local spirits along the Upper Rhine."),
    (-500, "pagan-europe", "Celtic tribes worshipped their gods in the Black Forest."),
    (74, "hellenic", "Rome annexed the Upper Rhine lands, bringing the Roman gods."),
    (260, "pagan-europe", "The pagan Alemanni overran the Roman frontier."),
    (650, "christian", "Frankish rule and the bishopric of Constance completed the conversion of the Alemanni."),
    (1054, "catholic", "The Great Schism left the Breisgau in the Latin church, and Habsburg rule kept it Catholic."),
])

zone("bavaria", "Bavaria (Munich)", 11.58, 48.14, [
    (-10000, "folk", "Neolithic farmers honoured local spirits along the Danube."),
    (-500, "pagan-europe", "The Celtic Vindelici worshipped their gods in fortified oppida such as Manching."),
    (-15, "hellenic", "Augustus conquered Raetia, bringing the Roman gods to Augsburg and Regensburg."),
    (400, "christian", "Christianity spread through the Roman towns of Raetia."),
    (500, "pagan-europe", "After Rome fell the land was settled by the largely pagan Bavarii."),
    (700, "christian", "Rupert, Emmeram and Corbinian converted the Bavarians, and Boniface organised their dioceses in 739."),
    (1054, "catholic", "The Great Schism left Bavaria in the Latin church, and the Wittelsbach dukes made it a bastion of the Counter-Reformation."),
])

zone("franconia", "Franconia (Nuremberg)", 11.08, 49.45, [
    (-10000, "folk", "Neolithic farmers honoured local spirits along the Main and Regnitz."),
    (-500, "pagan-europe", "Celtic and later Germanic Thuringians worshipped their gods."),
    (742, "christian", "Boniface founded the bishoprics of Wurzburg and Eichstatt to convert the Main lands."),
    (1054, "catholic", SCHISM.format("Franconia")),
    (1525, "lutheran", "The free city of Nuremberg and the margraves of Ansbach and Bayreuth adopted the Lutheran Reformation."),
])

zone("wurzburg", "Lower Franconia (Wurzburg)", 9.93, 49.79, [
    (-10000, "folk", "Neolithic farmers honoured local spirits along the Main."),
    (-500, "pagan-europe", "Celtic and later Germanic Thuringians worshipped their gods."),
    (700, "christian", "The Irish missionary Kilian, martyred at Wurzburg in 689, and Boniface converted the Main valley."),
    (1054, "catholic", "The Great Schism left the land in the Latin church, and Prince-Bishop Julius Echter restored it fully to Catholicism after 1573."),
])

# ---------------------------------------------------------------- Austria
zone("austria", "Austria (Vienna)", 16.37, 48.2, [
    (-10000, "folk", "Prehistoric Danubian farmers carved figures such as the Venus of Willendorf and honoured local spirits."),
    (-500, "pagan-europe", "The Celtic kingdom of Noricum worshipped gods such as Noreia."),
    (-15, "hellenic", "Rome annexed Noricum and Pannonia, founding Vindobona (Vienna) and Carnuntum."),
    (380, "christian", "Christianity became the Roman state religion, and Saint Severin later led the Christians of Noricum."),
    (568, "pagan-europe", "After the Romans left, pagan Avars and Slavs ruled the Danube basin."),
    (800, "christian", "Charlemagne destroyed the Avar khaganate in 796, and Bavarian missions from Salzburg and Passau converted the land."),
    (1054, "catholic", SCHISM.format("Austria")),
    (1570, "lutheran", "Most Austrian nobles and townspeople had become Lutheran, and Emperor Maximilian II granted them freedom of worship in 1568."),
    (1627, "catholic", "Ferdinand II's Counter-Reformation expelled Protestant preachers and nobles and restored Catholicism."),
])

zone("tyrol", "Tyrol (Innsbruck)", 11.4, 47.27, [
    (-10000, "folk", "Alpine peoples honoured mountain spirits; Otzi the Iceman lived here around 3300 BC."),
    (-500, "pagan-europe", "The Raetians worshipped their own Alpine gods."),
    (-15, "hellenic", "Augustus conquered the Alps, bringing the Roman gods along the Brenner road."),
    (400, "christian", "Christianity spread along the Roman roads, and Saben became a bishopric."),
    (1054, "catholic", "The Great Schism left Tyrol in the Latin church, and its Habsburg rulers kept it firmly Catholic."),
])

zone("carinthia", "Carinthia (Klagenfurt)", 14.3, 46.62, [
    (-10000, "folk", "Prehistoric Alpine farmers honoured local spirits."),
    (-500, "pagan-europe", "The Celtic kingdom of Noricum worshipped its gods at Magdalensberg."),
    (-15, "hellenic", "Rome annexed Noricum, bringing the Roman gods to Virunum."),
    (400, "christian", "Christianity spread in Roman Noricum, with bishops at Teurnia and Virunum."),
    (590, "pagan-europe", "Pagan Slavs settled the land and founded the principality of Carantania."),
    (772, "christian", "Bavarian duke Tassilo crushed a pagan revolt and missions from Salzburg converted the Carantanians."),
    (1054, "catholic", SCHISM.format("Carinthia")),
    (1570, "lutheran", "Most Carinthian nobles and towns turned Lutheran in the 16th century."),
    (1600, "catholic", "Archduke Ferdinand's reformation commissions forced Carinthia back to Catholicism."),
])

# ---------------------------------------------------------------- Italy
zone("lombardy", "Northern Italy (Milan and Pavia)", 9.19, 45.46, [
    (-10000, "folk", "Prehistoric Alpine peoples carved the rock art of Val Camonica."),
    (-500, "pagan-europe", "Celtic Insubres and Cenomani worshipped Celtic gods in the Po valley."),
    (-191, "hellenic", "Rome conquered Cisalpine Gaul, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion; Bishop Ambrose of Milan was its great champion."),
    (493, "arian", "Theodoric's Ostrogoths ruled Italy as Arian Christians over a Nicene Italian population."),
    (553, "christian", "Justinian's Gothic War ended Ostrogothic rule and restored Nicene Byzantine control."),
    (569, "arian", "The Lombards took Milan and Pavia and ruled as largely Arian Christians."),
    (671, "christian", "King Perctarit and his successors were Catholic, ending Lombard Arianism by the end of the century."),
    (1054, "catholic", SCHISM.format("northern Italy")),
])

zone("venice", "Venice", 12.33, 45.44, [
    (-10000, "folk", "Prehistoric peoples of the northern Adriatic honoured local spirits."),
    (-500, "pagan-europe", "The Veneti worshipped the goddess Reitia and other gods of their own."),
    (-180, "hellenic", "Rome absorbed the Veneti and founded Aquileia, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion, and Aquileia became a great see."),
    (493, "arian", "The Arian Ostrogoths ruled Venetia."),
    (540, "christian", "Byzantine forces retook Venetia, and refugees from the Lombards founded the lagoon city under Constantinople."),
    (1054, "catholic", "The Great Schism left Venice in the Latin church, though the Republic kept its independence from the Pope."),
])

zone("tuscany", "Tuscany (Florence)", 11.25, 43.77, [
    (-10000, "folk", "The Etruscans honoured gods such as Tinia and Uni and read omens from livers and lightning."),
    (-280, "hellenic", "Rome conquered Etruria and absorbed its cults into the Roman religion."),
    (380, "christian", "Christianity became the Roman state religion."),
    (493, "arian", "The Arian Ostrogoths ruled Tuscany."),
    (553, "christian", "Justinian's Gothic War restored Nicene Byzantine rule."),
    (570, "arian", "The largely Arian Lombards took Tuscany as the duchy of Tuscia."),
    (671, "christian", "The Lombard kings and dukes became Catholic, ending Arianism by the end of the century."),
    (1054, "catholic", SCHISM.format("Tuscany")),
])

zone("rome", "Rome and Lazio", 12.5, 41.9, [
    (-10000, "folk", "Early Latins and Etruscans honoured household gods, ancestors and spirits of place."),
    (-753, "hellenic", "Legend dates Rome's founding to 753 BC; its Latin gods merged with the Greek Olympians."),
    (380, "christian", "Theodosius made Christianity the state religion, and the Bishop of Rome led the western church even under Gothic kings."),
    (1054, "catholic", "The Great Schism of 1054 split Rome from Constantinople, and Rome became the seat of the Roman Catholic Church and the Papal States."),
])

zone("naples", "Southern Italy (Naples and Campania)", 14.25, 40.85, [
    (-10000, "folk", "Oscan and Samnite peoples honoured their own gods."),
    (-600, "hellenic", "Greek colonies such as Cumae and Neapolis brought the Greek gods, later absorbed by Rome."),
    (380, "christian", "Christianity became the Roman state religion."),
    (493, "arian", "The Arian Ostrogoths ruled Campania."),
    (536, "christian", "Belisarius took Naples for Justinian, restoring Nicene Byzantine rule."),
    (1054, "catholic", "The Great Schism left Naples in the Latin church, and the Normans united the south as a papal fief."),
])

zone("calabria", "Calabria and the Greek South", 16.25, 39.3, [
    (-10000, "folk", "Oenotrian and Bruttian peoples honoured local gods."),
    (-720, "hellenic", "Greek colonists founded Sybaris, Croton and Rhegion, the heart of Magna Graecia."),
    (380, "christian", "Christianity became the Roman state religion."),
    (493, "arian", "The Arian Ostrogoths ruled Calabria."),
    (536, "christian", "Justinian reconquered the south, which stayed Byzantine and Greek-speaking."),
    (1054, "orthodox", "Calabria's Greek church, placed under Constantinople around 732, sided with the Patriarch in the Great Schism."),
    (1060, "catholic", "Robert Guiscard's Normans took Reggio and placed Calabria under Rome, though the Greek rite lingered for centuries."),
])

zone("sicily", "Sicily", 13.9, 37.6, [
    (-10000, "folk", "The Sicani and Sicels honoured local gods and spirits."),
    (-734, "hellenic", "Greek colonists founded Naxos and Syracuse, while Phoenicians held Palermo and the west."),
    (380, "christian", "Christianity became the Roman state religion; Sicily later stayed Byzantine and largely Greek-speaking."),
    (902, "sunni", "The Aghlabids completed the Muslim conquest with the fall of Taormina, and by the 11th century about half the island was Muslim."),
    (1091, "catholic", "The Normans under Roger I completed their conquest, and Latin Christianity gradually replaced Islam and the Greek rite."),
])

zone("sardinia", "Sardinia", 9.0, 40.0, [
    (-10000, "folk", "The Nuragic Sardinians built stone towers and sacred well temples."),
    (-510, "mesopotamian", "Carthage conquered Sardinia's coasts, bringing the Punic gods Baal Hammon and Tanit."),
    (-238, "hellenic", "Rome took Sardinia from Carthage, bringing the Roman gods."),
    (400, "christian", "Christianity spread through the Roman towns, though the mountain Barbagia stayed pagan until about 594."),
    (460, "arian", "The Arian Vandals seized Sardinia from their kingdom in Africa."),
    (534, "christian", "Justinian's Byzantine army conquered the Vandals."),
    (1054, "catholic", "The Great Schism left Sardinia's native judges in the Latin church, under Pisa and then Aragon."),
])

zone("malta", "Malta", 14.5, 36.3, [
    (-10000, "folk", "Neolithic Maltese built the megalithic temples of Ggantija and Hagar Qim, among the oldest in the world."),
    (-700, "mesopotamian", "Phoenician traders settled Malta and worshipped Melqart and Astarte."),
    (-218, "hellenic", "Rome took Malta from Carthage in the Second Punic War."),
    (400, "christian", "Christianity, said to have been brought by Saint Paul's shipwreck, became the islands' faith."),
    (870, "sunni", "The Aghlabids conquered Malta, which was resettled by Muslims and kept a Muslim majority under Norman rule."),
    (1249, "catholic", "The remaining Muslims were expelled or converted, and Malta became wholly Catholic, later the home of the Knights of Saint John."),
])

# ---------------------------------------------------------------- Iberia
zone("galicia", "Galicia (Santiago de Compostela)", -8.54, 42.88, [
    (-10000, "folk", "Neolithic farmers built dolmens and later Celtic-style hill forts called castros."),
    (-500, "pagan-europe", "The Celtic Gallaeci worshipped gods such as Lugus and Bandua."),
    (-25, "hellenic", "Augustus completed the Roman conquest of the northwest, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion; Bishop Priscillian of Avila drew a wide following here."),
    (466, "arian", "The Suebi of Galicia, ruling from Braga, adopted Arianism under King Remismund."),
    (561, "christian", "The Suebi returned to Nicene Christianity under Martin of Braga at the First Council of Braga."),
    (1054, "catholic", "The Great Schism left Galicia in the Latin church, with the shrine of Santiago de Compostela at the heart of medieval pilgrimage."),
])

zone("asturias", "Asturias (Oviedo)", -5.85, 43.36, [
    (-10000, "folk", "Palaeolithic hunters painted caves such as Tito Bustillo and Altamira nearby."),
    (-500, "pagan-europe", "The Celtic Astures and Cantabri worshipped their own gods."),
    (-19, "hellenic", "Augustus ended the Cantabrian Wars, bringing the Roman gods."),
    (400, "christian", "Christianity spread in late Roman times; in 718 Pelagius founded the Christian kingdom of Asturias at Covadonga."),
    (1054, "catholic", SCHISM.format("Asturias and Leon")),
])

zone("old-castile", "Old Castile (Burgos)", -3.7, 42.34, [
    (-10000, "folk", "Prehistoric peoples of the meseta honoured local spirits; Atapuerca holds some of the oldest human remains in western Europe."),
    (-500, "pagan-europe", "Celtiberian tribes worshipped Celtic gods."),
    (-133, "hellenic", "Rome destroyed Numantia and conquered the northern meseta, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion."),
    (472, "arian", "The Visigoths took over Hispania and ruled as Arian Christians."),
    (589, "christian", "King Reccared converted the Visigoths to Nicene Christianity at the Third Council of Toledo."),
    (712, "sunni", "The Umayyad conquest brought the Duero valley under Muslim rule."),
    (750, "christian", "After the Berber revolt of 740 Muslim garrisons withdrew, and Asturian kings resettled the land, founding the county of Castile."),
    (1054, "catholic", SCHISM.format("Castile")),
])

zone("toledo", "New Castile (Toledo and Madrid)", -4.02, 39.86, [
    (-10000, "folk", "Prehistoric peoples of the meseta honoured local spirits."),
    (-500, "pagan-europe", "Celtiberian and Carpetani tribes worshipped Celtic and Iberian gods."),
    (-193, "hellenic", "Rome took Toletum, bringing the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion."),
    (475, "arian", "The Visigoths took over Hispania and later made Toledo the capital of their Arian kingdom."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (712, "sunni", "The Umayyads took Toledo, and central Spain became part of Muslim al-Andalus."),
    (1085, "catholic", "Alfonso VI of Castile captured Toledo, which became the seat of Spain's primate."),
])

zone("extremadura", "Extremadura (Merida)", -6.34, 38.92, [
    (-10000, "folk", "Prehistoric peoples built dolmens and honoured local spirits."),
    (-500, "pagan-europe", "The Celtic and Lusitanian tribes worshipped gods such as Endovelicus."),
    (-25, "hellenic", "Augustus founded Emerita Augusta (Merida), capital of Lusitania."),
    (380, "christian", "Christianity became the Roman state religion, and Merida was a great Christian see."),
    (475, "arian", "The Visigoths ruled as Arian Christians."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (713, "sunni", "Musa ibn Nusayr captured Merida after a long siege."),
    (1230, "catholic", "Alfonso IX of Leon took Merida and Badajoz, bringing Extremadura under Christian rule."),
])

zone("andalusia", "Andalusia (Cordoba and Seville)", -4.78, 37.88, [
    (-10000, "folk", "Prehistoric peoples built great dolmens such as Antequera; Tartessos later flourished in the lower Guadalquivir."),
    (-800, "mesopotamian", "Phoenicians founded Gadir (Cadiz) and spread the cults of Melqart and Astarte along the coast."),
    (-206, "hellenic", "Scipio's victory at Ilipa won Baetica for Rome."),
    (380, "christian", "Christianity became the Roman state religion; Bishop Hosius of Cordoba was a leading figure at the Council of Nicaea."),
    (572, "arian", "King Leovigild took Cordoba for the Arian Visigoths."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (711, "sunni", "The Umayyad conquest made Cordoba the capital of al-Andalus and later of a caliphate."),
    (1236, "catholic", "Ferdinand III of Castile took Cordoba in 1236 and Seville in 1248."),
])

zone("granada", "Granada", -3.6, 37.18, [
    (-10000, "folk", "Prehistoric peoples of the Sierra Nevada honoured local spirits."),
    (-500, "pagan-europe", "Iberian tribes such as the Bastetani worshipped their own gods."),
    (-206, "hellenic", "Rome conquered the region after the Second Punic War."),
    (380, "christian", "Christianity became the Roman state religion."),
    (572, "arian", "The Arian Visigoths took the region."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (711, "sunni", "The Umayyad conquest made Granada part of al-Andalus; it was the last Nasrid emirate from 1238."),
    (1492, "catholic", "Ferdinand and Isabella took Granada; Muslims were forced to convert in 1501 and the Moriscos were expelled in 1609."),
])

zone("valencia", "Valencia and Murcia", -0.38, 39.47, [
    (-10000, "folk", "Prehistoric peoples painted the rock shelters of the Levant."),
    (-500, "pagan-europe", "Iberian tribes worshipped their own gods, as shown by the Lady of Elche."),
    (-138, "hellenic", "Rome founded Valentia and brought the Roman gods."),
    (380, "christian", "Christianity became the Roman state religion."),
    (476, "arian", "The Arian Visigoths took the region."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (714, "sunni", "The Umayyad conquest made the Levant part of al-Andalus."),
    (1238, "catholic", "James I of Aragon took Valencia; its large Muslim population was forced to convert in 1525 and expelled in 1609."),
])

zone("aragon", "Aragon (Zaragoza)", -0.88, 41.65, [
    (-10000, "folk", "Prehistoric peoples of the Ebro valley honoured local spirits."),
    (-500, "pagan-europe", "Celtiberian and Iberian tribes worshipped their own gods."),
    (-200, "hellenic", "Rome conquered the Ebro valley and later founded Caesaraugusta (Zaragoza)."),
    (380, "christian", "Christianity became the Roman state religion."),
    (472, "arian", "The Arian Visigoths took Caesaraugusta."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (714, "sunni", "The Umayyad conquest made Zaragoza a Muslim city of the Upper March."),
    (1118, "catholic", "Alfonso I the Battler of Aragon captured Zaragoza."),
])

zone("catalonia", "Catalonia (Barcelona)", 2.17, 41.39, [
    (-10000, "folk", "Prehistoric peoples of the northeast honoured local spirits."),
    (-500, "pagan-europe", "Iberian tribes worshipped their gods, while Greeks traded at Emporion."),
    (-218, "hellenic", "Rome landed at Emporion in the Second Punic War and made the region the province of Tarraconensis."),
    (380, "christian", "Christianity became the Roman state religion."),
    (415, "arian", "Ataulf's Visigoths entered Barcelona, and Arian Visigoths later ruled Tarraconensis."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (717, "sunni", "The Umayyad conquest brought Barcelona under Muslim rule."),
    (801, "christian", "Louis the Pious took Barcelona, founding the Carolingian Spanish March."),
    (1054, "catholic", SCHISM.format("Catalonia")),
])

zone("navarre", "Navarre and the Basque Country", -1.64, 42.82, [
    (-10000, "folk", "The ancestors of the Basques honoured nature spirits and the goddess Mari."),
    (-75, "hellenic", "Pompey founded Pompaelo (Pamplona), bringing Roman gods to the Vascones."),
    (500, "christian", "Christianity spread from the Roman towns, and Pamplona had a bishop by 589, though the mountain Basques converted more slowly."),
    (1054, "catholic", SCHISM.format("Navarre")),
])

zone("balearics", "Balearic Islands", 2.9, 39.6, [
    (-10000, "folk", "The Talaiotic islanders built stone towers and taula sanctuaries."),
    (-123, "hellenic", "Quintus Caecilius Metellus conquered Mallorca for Rome."),
    (400, "christian", "Christianity spread in the islands in late Roman times."),
    (455, "arian", "The Arian Vandals seized the Balearics."),
    (534, "christian", "Justinian's Byzantine army conquered the Vandals."),
    (903, "sunni", "The Emirate of Cordoba annexed the islands, which became Muslim Mayurqa."),
    (1229, "catholic", "James I of Aragon conquered Mallorca, followed by Ibiza in 1235 and Menorca in 1287."),
])

zone("canary-islands", "Canary Islands", -16.5, 28.3, [
    (-10000, "folk", "The Berber-descended Guanches, who arrived in the first millennium BC, worshipped the sky god Achaman and mummified their dead."),
    (1496, "catholic", "Castile completed its conquest with Tenerife in 1496, and the Guanches were converted to Catholicism."),
])

zone("portugal-north", "Northern Portugal (Braga and Porto)", -8.43, 41.55, [
    (-10000, "folk", "Neolithic farmers built dolmens and later hill forts called castros."),
    (-500, "pagan-europe", "The Celtic Gallaeci worshipped gods such as Bandua and Nabia."),
    (-137, "hellenic", "Decimus Junius Brutus campaigned here, and Rome later founded Bracara Augusta (Braga)."),
    (380, "christian", "Christianity became the Roman state religion."),
    (466, "arian", "The Suebi, ruling from Braga, adopted Arianism under King Remismund."),
    (561, "christian", "The Suebi returned to Nicene Christianity under Martin of Braga."),
    (716, "sunni", "The Umayyad conquest brought the north under Muslim rule."),
    (868, "christian", "Vimara Peres retook Porto, founding the Christian county of Portucale."),
    (1054, "catholic", SCHISM.format("Portugal")),
])

zone("lisbon", "Central Portugal (Lisbon)", -9.14, 38.72, [
    (-10000, "folk", "Prehistoric peoples built dolmens and the stone circle of Almendres."),
    (-500, "pagan-europe", "The Lusitanians worshipped gods such as Endovelicus."),
    (-138, "hellenic", "Rome conquered Lusitania after the death of Viriathus."),
    (380, "christian", "Christianity became the Roman state religion."),
    (469, "arian", "The Arian Suebi and later Visigoths ruled Lisbon."),
    (589, "christian", "King Reccared converted the Visigoths to Nicene Christianity at the Third Council of Toledo."),
    (714, "sunni", "The Umayyad conquest made Lisbon the Muslim city of al-Ushbuna."),
    (1147, "catholic", "Afonso Henriques captured Lisbon with the help of crusaders."),
])

zone("algarve", "Algarve", -8.0, 37.1, [
    (-10000, "folk", "Prehistoric peoples raised standing stones and honoured local spirits."),
    (-500, "pagan-europe", "The Conii and Lusitanians worshipped their own gods."),
    (-138, "hellenic", "Rome conquered the south of Lusitania."),
    (380, "christian", "Christianity became the Roman state religion."),
    (470, "arian", "The Arian Visigoths took the region."),
    (589, "christian", "King Reccared converted to Nicene Christianity at the Third Council of Toledo."),
    (713, "sunni", "The Umayyad conquest made the Algarve, al-Gharb, part of al-Andalus."),
    (1249, "catholic", "Afonso III of Portugal took Faro, completing the Portuguese Reconquista."),
])

# ---------------------------------------------------------------- Nordic
zone("denmark", "Denmark", 11.6, 55.6, [
    (-10000, "folk", "Stone and Bronze Age Danes made offerings in bogs and built the Trundholm sun chariot."),
    (-500, "pagan-europe", "The Danes worshipped Odin, Thor and Freyr at great halls such as Lejre."),
    (965, "christian", "King Harald Bluetooth was baptised and declared on the Jelling stone that he had made the Danes Christian."),
    (1054, "catholic", SCHISM.format("Denmark")),
    (1536, "lutheran", "King Christian III imprisoned the Catholic bishops and made Denmark Lutheran."),
])

zone("norway", "Norway", 10.75, 59.91, [
    (-10000, "folk", "Stone and Bronze Age Norwegians carved rock art of ships and the sun."),
    (-500, "pagan-europe", "The Norse worshipped Odin, Thor and Freyr in temples and household rites."),
    (1024, "christian", "Kings Olaf Tryggvason and Olaf Haraldsson forced conversion, and the Moster law of 1024 made Norway Christian."),
    (1054, "catholic", SCHISM.format("Norway")),
    (1537, "lutheran", "Christian III of Denmark drove out Archbishop Olav Engelbrektsson and made Norway Lutheran."),
])

zone("sweden", "Sweden (Svealand)", 18.07, 59.33, [
    (-10000, "folk", "Stone and Bronze Age Swedes carved rock art and built ship settings."),
    (-500, "pagan-europe", "The Svear worshipped Odin, Thor and Freyr at the great temple of Uppsala."),
    (1100, "catholic", "The Uppsala temple fell about 1080, and by 1100 Svealand had accepted Latin Christianity."),
    (1527, "lutheran", "Gustav Vasa's Diet of Vasteras broke with Rome, and the Uppsala Synod of 1593 made Sweden firmly Lutheran."),
])

zone("gotaland", "Gotaland (southern Sweden)", 14.16, 57.78, [
    (-10000, "folk", "Stone and Bronze Age peoples carved the rock art of Tanum."),
    (-500, "pagan-europe", "The Geats worshipped Odin, Thor and Freyr."),
    (1000, "christian", "King Olof Skotkonung, baptised around 1008, founded the bishopric of Skara and the Geats became Christian."),
    (1054, "catholic", SCHISM.format("Gotaland")),
    (1527, "lutheran", "Gustav Vasa's Diet of Vasteras broke with Rome, making Sweden Lutheran."),
])

zone("finland", "Finland", 24.0, 60.6, [
    (-10000, "folk", "Stone Age Finns carved rock art and honoured forest and animal spirits."),
    (-500, "pagan-europe", "The Finns worshipped Ukko the sky god and their ancestors."),
    (1200, "catholic", "Swedish crusades and missions such as that of Bishop Henry made southwestern Finland Catholic, with a bishop at Turku."),
    (1527, "lutheran", "Under Swedish rule Finland became Lutheran, and Mikael Agricola gave it a Finnish New Testament in 1548."),
])

zone("sapmi", "Sapmi (Lapland)", 25.0, 68.9, [
    (-10000, "folk", "The Sami honoured nature spirits and sacred sieidi stones, with noaidi shamans using drums to travel between worlds."),
    (1720, "lutheran", "Danish and Swedish Lutheran missions, led by Thomas von Westen from 1716, burned the drums and converted the Sami; Laestadian revival later took root."),
])

zone("iceland", "Iceland", -21.0, 64.2, [
    (-10000, "pagan-europe", "Iceland was uninhabited until Norse settlers from 874 brought the worship of Odin, Thor and Freyr."),
    (1000, "christian", "The Althing accepted Christianity by law after the lawspeaker Thorgeir ruled for the whole island."),
    (1054, "catholic", SCHISM.format("Iceland")),
    (1550, "lutheran", "The Danish crown imposed Lutheranism and beheaded Jon Arason, the last Catholic bishop."),
])

H = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(H, "zones_west_europe.json"), "w") as f:
    json.dump(Z, f, ensure_ascii=False, indent=1)
print(len(Z), "zones")

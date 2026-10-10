"""Generate zones_africa.json (sub-Saharan Africa religious history zones)."""
import json, os

Z = []


def z(id, name, lon, lat, *hist):
    Z.append({"id": id, "name": name, "lon": lon, "lat": lat,
              "history": [{"from": y, "faith": f, "note": n} for (y, f, n) in hist]})


F = -10000

# ---------------- SUDAN (Nubia and beyond) ----------------
z("nobadia", "Lower Nubia (Nobadia)", 30.6, 21.0,
  (F, "folk", "A-Group and C-Group herders and farmers of Lower Nubia followed their own cults of cattle, ancestors and local gods."),
  (-1500, "egyptian", "The New Kingdom conquest of Kush under Thutmose I planted temples of Amun and other Egyptian gods across Nubia, and Nubians still worshipped Isis of Philae into the 6th century AD."),
  (543, "oriental", "A Miaphysite mission sent by Empress Theodora under the priest Julian converted the king of Nobadia in 543, and the land joined the Coptic church that rejected Chalcedon."),
  (1480, "sunni", "Arab tribes such as the Banu Kanz settled Lower Nubia, and Dotawo, the last Christian Nubian kingdom, faded out in the late 15th century, leaving a Muslim land later ruled by the Ottomans."))

z("makuria", "Makuria (Dongola)", 30.48, 18.22,
  (F, "folk", "Kerma culture farmers and herders of the Dongola reach worshipped their own gods and buried their rulers in great mounds with sacrificed retainers."),
  (-1500, "egyptian", "Egypt's New Kingdom conquered Kush and built the Amun temple at Jebel Barkal, and the Napatan kings, who ruled Egypt itself as its 25th dynasty, kept Amun as their chief god."),
  (570, "christian", "A Byzantine mission converted the kingdom of Makuria to Chalcedonian Christianity around 570, with its capital and cathedrals at Old Dongola."),
  (710, "oriental", "After uniting with Nobadia, Makuria adopted the Miaphysite faith of the Coptic patriarch of Alexandria, whose bishops led the Nubian church for six centuries."),
  (1317, "sunni", "Mamluk interventions put a Muslim prince, Abdallah Barshambu, on the Dongola throne in 1317, the royal throne hall became a mosque, and the Nubians gradually became Muslims."))

z("alodia", "Alodia and the Funj (Central Sudan)", 32.53, 15.55,
  (F, "folk", "Neolithic communities at the Nile confluence, among the earliest cattle herders in Africa, followed local cults."),
  (-800, "egyptian", "The kingdom of Kush, ruling from Napata and from about 590 BC from Meroe, spread the worship of Amun alongside the lion god Apedemak and other Meroitic gods."),
  (580, "oriental", "The Miaphysite bishop Longinus converted the kingdom of Alodia, whose capital Soba lay near modern Khartoum, around 580."),
  (1504, "sunni", "The Funj, who destroyed Christian Soba around 1504, made Sennar a Muslim sultanate, and Sufi holy men spread Islam among the people of the Gezira and the Nile."))

z("beja", "Red Sea Hills (Beja)", 36.6, 18.8,
  (F, "folk", "The Beja herders of the Red Sea Hills, the Blemmyes of Roman sources, worshipped their own gods and also honoured Isis at Philae."),
  (1400, "sunni", "Arab miners and traders settling in the Beja lands from the 9th century, and intermarriage with Beja clans, made the Beja Muslim by about the 15th century."))

z("kordofan", "Kordofan (Sudan)", 30.22, 13.18,
  (F, "folk", "The Nuba and other peoples of Kordofan followed local religions centred on rain makers, priests and ancestors."),
  (1750, "sunni", "Arab Baggara cattle nomads and the Funj and Darfur sultans who fought over Kordofan spread Islam through its plains by the 18th century, while many Nuba hill peoples kept their own faiths."))

z("darfur", "Darfur (Sudan)", 25.35, 13.63,
  (F, "folk", "The Fur, Daju and Tunjur peoples of Jebel Marra and the Darfur plains followed their own traditional religions."),
  (1650, "sunni", "Sultan Sulayman Solongdungu, founder of the Keira sultanate around 1650, made Islam the state religion, and Muslim scholars and the pilgrim road spread it among the Fur."))

# ---------------- SOUTH SUDAN ----------------
z("equatoria", "Equatoria (South Sudan)", 31.58, 4.85,
  (F, "folk", "The Bari, Zande, Lotuko and other peoples of Equatoria followed their own religions of rain makers, ancestors and a high god."),
  (1975, "catholic", "Comboni missionaries from the early 1900s and their mission schools, then the upheaval of the civil wars, made most people of Equatoria Christian, with the Catholic Church the largest."))

z("dinka-nuer", "Dinka and Nuer lands (South Sudan)", 29.7, 6.8,
  (F, "folk", "The Dinka and Nuer cattle herders worshipped Nhialic or Kwoth, the sky god, through spirit masters, prophets and the sacrifice of cattle."),
  (1995, "catholic", "Christianity spread massively during the civil war of 1983 to 2005, when churches were among the few institutions left, and the Catholic and Episcopal (Anglican) churches now hold most believers."))

# ---------------- ETHIOPIA ----------------
z("tigray", "Tigray and Aksum (Ethiopia)", 38.72, 14.13,
  (F, "folk", "Cushitic and Semitic speaking farmers followed local cults, and the kingdom of D'mt and early Aksum honoured South Arabian gods such as Almaqah, Astar and the war god Mahrem."),
  (340, "christian", "King Ezana of Aksum was converted by the Syrian bishop Frumentius in the 330s and put the cross on his coins, making Aksum one of the first Christian states."),
  (451, "oriental", "Following the Coptic patriarch of Alexandria, the Aksumite church rejected Chalcedon, and the Nine Saints, Syrian Miaphysite monks of the late 5th century, carried the faith into the countryside."))

z("lasta", "Lasta and Lalibela (Ethiopia)", 39.05, 12.03,
  (F, "folk", "Agaw farmers of Lasta followed traditional cults of sky and earth spirits."),
  (650, "oriental", "Christianity spread south from Aksum into Lasta and Angot among the Agaw, whose Zagwe kings later carved the rock churches of Lalibela around 1200."))

z("south-wollo", "South Wollo (Ethiopia)", 39.63, 11.13,
  (F, "folk", "Cushitic and Semitic speaking farmers of the eastern highlands followed traditional cults."),
  (1270, "oriental", "The old province of Amhara here was the cradle of the Solomonic dynasty restored in 1270, with the island monastery of Hayq Istifanos as a leading centre of Orthodox learning."),
  (1580, "folk", "After Ahmad Gragn's wars of 1529 to 1543, Oromo clans following the gada system and the sky god Waaqa moved into the old lands of Amhara and Angot."),
  (1750, "sunni", "The Oromo of Wollo adopted Islam, and the Muslim born Yejju lords who dominated Ethiopia in the Era of the Princes and the Mammadoch dynasty made the region largely Muslim."))

z("gondar", "Gondar and Lake Tana (Ethiopia)", 37.47, 12.6,
  (F, "folk", "Agaw peoples around Lake Tana kept traditional cults, while the Beta Israel practised their own form of Judaism in the Semien and Dembiya highlands."),
  (1330, "oriental", "Emperor Amda Seyon's wars and the monasteries founded on Lake Tana's islands in the 14th century made the region Orthodox, later the seat of the Gondarine emperors from 1636."))

z("shewa", "Shewa (Addis Ababa)", 38.75, 9.02,
  (F, "folk", "Cushitic and Semitic speaking farmers of the Shewan plateau followed traditional cults."),
  (1270, "oriental", "Yekuno Amlak, who founded the Solomonic dynasty in 1270, and his heirs made Shewa a heartland of the Orthodox kingdom, with royal camps and monasteries such as Debre Libanos."),
  (1570, "folk", "After Ahmad Gragn's Muslim conquest of 1529 to 1543 ruined the kingdom, Oromo clans following the gada system and the sky god Waaqa settled most of the Shewan plateau."),
  (1886, "oriental", "Menelik II of Shewa conquered the surrounding Oromo lands and founded Addis Ababa in 1886, spreading Orthodox churches, settlers and baptism across central Ethiopia."))

z("harar", "Harar and Adal (Ethiopia)", 42.12, 9.31,
  (F, "folk", "Cushitic farmers and herders of the eastern highlands followed traditional cults."),
  (1100, "sunni", "Islam came inland from the port of Zeila along the trade routes, and the Harla and Harari towns became the heart of the sultanates of Ifat and Adal, with Harar their capital from 1520."))

z("afar", "Afar lowlands", 41.0, 11.79,
  (F, "folk", "Afar herders of the Danakil lowlands followed traditional religion."),
  (1300, "sunni", "Islam spread among the Afar from the Red Sea coast and the sultanates of Ifat and Adal, and the Imamate of Aussa, founded in 1577, later ruled them as a Muslim state."))

z("jimma", "Gibe and Jimma (Ethiopia)", 36.83, 7.67,
  (F, "folk", "The Oromo of the Gibe region followed Waaqeffanna, the worship of the sky god Waaqa, organised by the gada age system."),
  (1830, "sunni", "The Gibe kingdoms adopted Islam in the 19th century, and Abba Jifar I of Jimma, ruling from about 1830, made it the faith of his court and people."))

z("arsi-bale", "Arsi and Bale (Ethiopia)", 40.0, 7.12,
  (F, "folk", "Cushitic farmers and herders of the Bale highlands followed traditional cults."),
  (1300, "sunni", "The Muslim sultanate of Bali grew around the shrine of Sheikh Hussein, a saint remembered from about 1200, as one of the Muslim states of southern Ethiopia."),
  (1570, "folk", "Oromo clans following Waaqeffanna and the gada system overran Bale and Arsi during their great migrations of the 16th century."),
  (1890, "sunni", "The Arsi and Bale Oromo embraced Islam in the 19th and early 20th centuries, partly in resistance to Menelik II's conquest, with Sheikh Hussein's shrine again a great pilgrimage centre."))

z("wollega", "Wollega (Ethiopia)", 36.55, 9.08,
  (F, "folk", "The western Oromo of Wollega followed Waaqeffanna under their gada assemblies and qaallu priests."),
  (1900, "oriental", "Moroda Bakare of Leqa Nekemte submitted to Menelik II in 1882 and was baptised Orthodox, and the Orthodox church then spread among the Wollega Oromo under Shewan rule."),
  (1990, "lutheran", "The Mekane Yesus church, rooted in the Oromo Bible and mission of Onesimos Nesib from 1904, grew rapidly under the Derg until Lutherans outnumbered the Orthodox in Wollega."))

z("wolaita", "Wolaita and the south (Ethiopia)", 37.75, 6.85,
  (F, "folk", "The Wolaita kingdom and its southern neighbours followed traditional religions centred on the divine king and ancestor spirits."),
  (1975, "protestant", "Sudan Interior Mission evangelists arrived in 1928, and their Kale Heywet church, which grew in secret during the Italian occupation, became the faith of most Wolaita and many southern peoples."))

z("gambela", "Gambela (Ethiopia)", 34.6, 8.25,
  (F, "folk", "The Anuak and Nuer of the Baro lowlands followed their own religions of village kings, spirits and cattle sacrifice."),
  (1985, "protestant", "Presbyterian and Mekane Yesus missions, and refugees returning from Sudan's wars, made most Anuak and Nuer Protestant by the late 20th century."))

z("ogaden", "Somali Region (Ethiopia)", 43.5, 7.0,
  (F, "folk", "Somali herders worshipped Waaq, the sky god, before Islam."),
  (1300, "sunni", "Islam spread inland among the Somali clans from the ports of Zeila and Berbera, and the Ogaden was part of the Muslim world of Adal by the 14th century."))

# ---------------- ERITREA ----------------
z("eritrea-highlands", "Eritrean highlands", 38.93, 15.33,
  (F, "folk", "The highland farmers of the Kebessa shared the South Arabian influenced cults of D'mt, whose great temple at Yeha lay just to the south."),
  (340, "christian", "As part of Aksum, the Eritrean plateau and its port Adulis followed King Ezana into Christianity in the 4th century."),
  (451, "oriental", "The highland church rejected Chalcedon with Alexandria, and its Orthodox Tewahedo tradition, autocephalous in Eritrea since 1993, remains the faith of most highlanders."))

z("massawa", "Massawa and Dahlak coast", 39.45, 15.61,
  (F, "folk", "The coastal peoples around Adulis and the Dahlak islands followed local cults while trading with Egypt, Arabia and India."),
  (340, "christian", "Adulis, the great port of Aksum, became Christian with King Ezana's court in the 4th century."),
  (451, "oriental", "Aksum's church, and with it the Red Sea coast, rejected the Council of Chalcedon along with Alexandria."),
  (900, "sunni", "Muslim traders and refugees settled the Dahlak islands from the 8th century, and the Dahlak sultanate made the Massawa coast Muslim by about the 10th century."))

z("eritrea-west", "Western Eritrean lowlands", 37.88, 15.55,
  (F, "folk", "Kunama and Nara farmers and Beja herders of the western lowlands followed their own traditional religions."),
  (1550, "sunni", "Beja Beni Amer clans tied to the Funj sultanate of Sennar spread Islam in the western lowlands, and the Nara followed in the 19th century, while many Kunama kept their own faith."))

z("eritrea-north", "Northern Eritrea (Tigre)", 38.47, 16.67,
  (F, "folk", "Herders of the northern Eritrean hills followed traditional cults."),
  (600, "oriental", "Christianity spread from Aksum among the herders of the northern hills, and the Tigre speaking Bet Asgede, Mensa and Marya clans were still Orthodox Christians around 1800."),
  (1850, "sunni", "Between about 1820 and 1880 the Tigre clans converted to Islam under the holy family of Ad Sheikh and the Mirghaniyya order, turning northern Eritrea Muslim."))

# ---------------- HORN ----------------
z("djibouti", "Djibouti", 42.8, 11.6,
  (F, "folk", "Afar and Issa Somali herders worshipped Waaq and other spirits."),
  (1000, "sunni", "Islam crossed early from Arabia to the nearby port of Zeila, whose two qibla mosque is said to be among Africa's oldest, and the Afar and Issa became Muslim."))

z("somaliland", "Somaliland", 44.06, 9.56,
  (F, "folk", "Somali and earlier Cushitic herders worshipped Waaq, the sky god, and traded myrrh and frankincense with Egypt and Arabia."),
  (1200, "sunni", "Islam reached Zeila and Berbera with Arab traders in its first centuries, and holy clan founders such as Sheikh Isaaq made the northern Somali Muslim by about the 13th century."))

z("puntland", "Puntland (Somalia)", 48.48, 8.4,
  (F, "folk", "The herders and incense traders of the Horn, perhaps the Land of Punt of Egyptian texts, worshipped Waaq and other spirits."),
  (1200, "sunni", "Islam spread along the coast and among the Darod clans, who trace their descent to an Arabian holy man, making the north east Muslim by about the 13th century."))

z("mogadishu", "Benadir coast (Mogadishu)", 45.34, 2.05,
  (F, "folk", "Somali herders and Bantu farmers of the southern coast followed Waaq and other traditional religions."),
  (1000, "sunni", "Arab and Persian merchants made Mogadishu a Muslim trading city by the 10th century, and its sultanate, visited by Ibn Battuta in 1331, spread Islam along the Benadir coast."))

z("jubaland", "Jubaland (Somalia)", 42.54, -0.36,
  (F, "folk", "Bantu farmers of the Juba valley and Oromo and Somali herders followed traditional religions."),
  (1300, "sunni", "The Ajuran sultanate and the coastal towns spread Islam up the Juba valley, and the Somali clans who later moved in completed the conversion."))

# ---------------- KENYA ----------------
z("kenya-coast", "Swahili coast of Kenya (Lamu, Malindi)", 40.9, -2.27,
  (F, "folk", "Bantu fishing and farming communities on the coast followed ancestral religions."),
  (1100, "sunni", "Trade with Arabia and the Persian Gulf made the Swahili towns of Lamu, Pate, Malindi and Mombasa Muslim by the 12th century, and Portuguese rule from 1505 to 1698 did not change that."))

z("kenya-northeast", "North-eastern Kenya", 40.06, 1.75,
  (F, "folk", "Oromo and Borana herders of the northern plains followed Waaqeffanna and the gada system."),
  (1880, "sunni", "Somali clans moving south west across the Juba in the 19th century pushed out the Oromo and made the region Muslim."))

z("kenya-central", "Central Kenya (Kikuyu and Kamba)", 36.82, -1.29,
  (F, "folk", "The Kikuyu, Kamba and Maasai worshipped Ngai, the high god of Mount Kenya, with ancestor spirits and age set rituals."),
  (1955, "protestant", "Church of Scotland, Anglican, Africa Inland Mission and Catholic schools from the 1890s, and the upheaval of the Mau Mau years, made most of central Kenya Christian, Protestants leading."))

z("kenya-west", "Western Kenya (Luo and Luhya)", 34.76, -0.09,
  (F, "folk", "The Luo and Luhya around Lake Victoria honoured a high god and ancestral spirits, with diviners and rain makers."),
  (1960, "protestant", "Anglican, Quaker, Adventist and Pentecostal missions from the early 1900s, along with Catholic Mill Hill missions and African churches such as Legio Maria, made the region mostly Christian."))

z("kenya-rift", "Rift Valley (Kalenjin)", 35.27, 0.51,
  (F, "folk", "The Kalenjin peoples worshipped Asis, the god of the sun, through elders and seasonal ceremonies."),
  (1970, "protestant", "The Africa Inland Church, with Catholic and Pentecostal churches, converted most Kalenjin in the decades around independence."))

# ---------------- TANZANIA ----------------
z("zanzibar", "Zanzibar", 39.2, -6.16,
  (F, "folk", "Bantu fishing and farming communities of Unguja and Pemba followed ancestral religions."),
  (1100, "sunni", "The Kizimkazi mosque inscription of 1107 marks Zanzibar's early Islam, and the Swahili stayed Sunni Muslims under the Ibadi Omani sultans who ruled from 1698 and made it their capital in 1840."))

z("kilwa", "Southern Tanzanian coast (Kilwa)", 39.51, -8.96,
  (F, "folk", "Bantu fishing and farming communities on the coast followed ancestral religions."),
  (1000, "sunni", "The Kilwa sultanate, founded by the Shirazi dynasty in the late 10th century, became the richest Muslim city of the Swahili coast, and Islam spread inland to the Yao in the 19th century."))

z("kilimanjaro", "Kilimanjaro (Tanzania)", 37.34, -3.35,
  (F, "folk", "The Chagga chiefdoms on Kilimanjaro's slopes worshipped Ruwa, the high god, with ancestor offerings and initiation rites."),
  (1930, "lutheran", "Leipzig Lutheran missionaries from 1893 and Catholic Spiritans from 1890 converted most Chagga, and the Lutheran church of northern Tanzania, based in Moshi, became a leading church."))

z("ugogo", "Central Tanzania (Ugogo)", 35.74, -6.17,
  (F, "folk", "The Gogo herders of the central plateau followed rain makers and ancestral spirits."),
  (1950, "anglican", "The Church Missionary Society's work among the Gogo from 1876 at Mpwapwa made Anglicanism the main faith of Ugogo, and Dodoma became the seat of an Anglican diocese."))

z("sukuma", "Sukumaland (Tanzania)", 32.9, -2.52,
  (F, "folk", "The Sukuma and Nyamwezi chiefdoms followed ancestor cults, healers and dance societies."),
  (1980, "catholic", "The White Fathers founded Bukumbi mission in 1883, and Catholic and Africa Inland Church missions slowly won most Sukuma by the late 20th century, Catholics the largest."))

z("kagera", "Kagera (Tanzania)", 31.8, -1.33,
  (F, "folk", "The Haya kingdoms west of Lake Victoria honoured the Cwezi spirits through kubandwa possession cults."),
  (1930, "catholic", "White Fathers from 1892 and Lutheran missions converted the Haya, the Catholic Church becoming the largest."))

z("songea", "Southern highlands (Tanzania)", 35.65, -10.68,
  (F, "folk", "The Ngoni, Matengo and other peoples of the south followed ancestral religions."),
  (1940, "catholic", "German Benedictines of St Ottilien founded Peramiho in 1898 and, after the Maji Maji war, made the Songea district one of Africa's most Catholic areas."))

# ---------------- UGANDA, RWANDA, BURUNDI ----------------
z("buganda", "Buganda (Uganda)", 32.58, 0.32,
  (F, "folk", "The Ganda worshipped the lubaale gods, such as Mukasa of Lake Victoria, through mediums and temples, with the kabaka as sacred king."),
  (1900, "catholic", "After Kabaka Mwanga's martyrdoms of 1886 and the religious wars of 1888 to 1892, Ganda chiefs converted en masse, and while Anglicans ruled under the 1900 Agreement, Catholics became the largest church."))

z("acholi", "Acholi (Uganda)", 32.3, 2.78,
  (F, "folk", "The Acholi chiefdoms worshipped the jogi spirits and the chiefdom shrines of their rwodi."),
  (1950, "catholic", "Comboni missionaries working from 1910 at Gulu and Kitgum made most Acholi Catholic by the mid 20th century, with an Anglican minority."))

z("ankole", "Ankole (Uganda)", 30.66, -0.61,
  (F, "folk", "The Ankole kingdom's Hima herders and Iru farmers honoured the Cwezi spirits and the royal drum Bagyendanwa."),
  (1930, "anglican", "Anglican missionaries, backed by the Ganda agents who helped the British run Ankole from 1901, made the Church of Uganda the leading faith of the kingdom."))

z("rwanda", "Rwanda", 30.06, -1.95,
  (F, "folk", "Rwandans worshipped Imana, the creator, and the Kubandwa spirits of the hero Ryangombe, with the mwami as sacred king."),
  (1935, "catholic", "After the Belgians replaced Mwami Musinga with his mission educated son Mutara III Rudahigwa in 1931, mass baptisms called the tornade made Rwanda mostly Catholic within a decade."))

z("burundi", "Burundi", 29.92, -3.43,
  (F, "folk", "The Burundians worshipped Imana and the Kubandwa spirits of Kiranga, with the mwami as sacred king."),
  (1940, "catholic", "White Fathers missions from 1898 led a wave of conversions in the 1930s under Belgian rule that made Burundi overwhelmingly Catholic."))

# ---------------- CONGO BASIN ----------------
z("kongo", "Kingdom of Kongo (northern Angola)", 14.24, -6.27,
  (F, "folk", "The Kongo worshipped Nzambi Mpungu, the creator, through nkisi power objects, ancestors and priests of the land spirits."),
  (1491, "catholic", "King Nzinga a Nkuwu was baptised Joao I in 1491 and his son Afonso I made Catholicism the royal religion from 1506, a ruling faith that spread, blended with Kongo beliefs, from the court to much of the people."))

z("kinshasa", "Western Congo (Kinshasa)", 15.31, -4.32,
  (F, "folk", "The Teke, Humbu and Kongo peoples of Malebo Pool traded on the river and honoured ancestors and nkisi spirits."),
  (1930, "catholic", "Belgian Catholic missions favoured in colonial schools, Baptist missions and Simon Kimbangu's church of 1921 made the people of Leopoldville and the lower Congo mostly Christian, Catholics leading."))

z("equateur", "Equateur (DR Congo)", 18.27, 0.05,
  (F, "folk", "The Mongo peoples of the central basin followed ancestor cults and forest spirits."),
  (1950, "catholic", "Trappist and Sacred Heart missionaries and the American Disciples of Christ converted the Mongo country under Belgian rule, the Catholic Church becoming the largest."))

z("kwilu", "Kwango and Kwilu (DR Congo)", 18.82, -5.04,
  (F, "folk", "The Yaka, Pende and Mbala peoples followed ancestor cults and masked initiation societies."),
  (1950, "catholic", "Belgian Jesuits, who ran the Kwango mission from 1893 with farm chapels and schools, made the region heavily Catholic by the mid 20th century."))

z("kasai", "Kasai (DR Congo)", 22.42, -5.9,
  (F, "folk", "The Luba, Lulua and Kuba kingdoms worshipped a creator god, ancestors and nature spirits, with sacred kings like the Kuba nyim."),
  (1940, "catholic", "Scheut missionaries and the American Presbyterian Congo Mission at Luebo, both from 1891, converted most of the Kasai, the Catholic Church being the largest."))

z("katanga", "Katanga (DR Congo)", 27.48, -11.66,
  (F, "folk", "The Luba and Lunda empires and Msiri's Yeke kingdom honoured ancestors and the spirits of their sacred kings."),
  (1940, "catholic", "Benedictine, Salesian and Franciscan missions and the Catholic schools of the copper mining company drew most of Katanga's workers and villages into the Catholic Church."))

z("upper-congo", "Upper Congo (Kisangani)", 25.2, 0.52,
  (F, "folk", "The forest peoples of the upper Congo and Ituri followed ancestor cults and spirits of forest and river."),
  (1950, "catholic", "Sacred Heart priests and Protestant missions such as the Baptists made the Stanleyville region largely Christian under Belgian rule, Catholics leading."))

z("kivu", "Kivu (DR Congo)", 28.86, -2.5,
  (F, "folk", "The Shi, Nande and Rega kingdoms honoured ancestors and the spirits of lakes and mountains."),
  (1940, "catholic", "White Fathers arriving in Kivu from 1906 converted most of the Shi and their neighbours, and Bukavu became a Catholic archdiocese."))

z("congo-brazzaville", "Republic of the Congo", 15.28, -4.27,
  (F, "folk", "The Kongo, Teke and Vili kingdoms of Loango and Malebo Pool worshipped Nzambi, ancestors and nkisi spirits."),
  (1930, "catholic", "Spiritan missionaries under Bishop Augouard from 1883, with Swedish Protestants and later the Matsouanist movement, made the south of the Congo mostly Christian, Catholics leading."))

z("gabon", "Gabon", 9.45, 0.39,
  (F, "folk", "The Fang, Myene and Punu peoples followed ancestor cults such as the Fang byeri reliquaries, and later the Bwiti initiation religion."),
  (1930, "catholic", "American Presbyterians from 1842 and French Spiritans from 1844 at Libreville began missions that, under French rule, made most Gabonese Christian, Catholics the largest group."))

z("bioko", "Bioko (Equatorial Guinea)", 8.78, 3.6,
  (F, "folk", "The Bubi of Fernando Po followed their own religion of ancestors and the spirits of the island's forests."),
  (1900, "catholic", "Spanish Claretian missionaries, arriving in 1883, converted most of the Bubi, and Catholicism has been the island's faith ever since."))

z("rio-muni", "Rio Muni (Equatorial Guinea)", 10.3, 1.6,
  (F, "folk", "The Fang of the mainland honoured ancestors through byeri reliquaries and initiation societies."),
  (1930, "catholic", "Claretian missions under Spanish rule converted most Fang of Rio Muni, making Equatorial Guinea one of Africa's most Catholic countries."))


z("car-south", "Southern Central African Republic", 18.56, 4.36,
  (F, "folk", "The Banda, Gbaya and Ngbaka peoples followed ancestor cults and initiation societies."),
  (1960, "protestant", "Spiritan Catholic missions from 1894 and American Baptist, Brethren and other evangelical missions converted most of the south in the 20th century, Protestants slightly outnumbering Catholics."))

z("dar-al-kuti", "Dar al-Kuti (northern CAR)", 20.65, 8.41,
  (F, "folk", "The Banda, Runga and Kresh peoples of the northern savanna followed traditional religions."),
  (1890, "sunni", "Muhammad al-Sanusi made Ndele the capital of the Muslim sultanate of Dar al-Kuti around 1890, a slave raiding state tied to Wadai, and Islam spread among the northern peoples."))

# ---------------- ANGOLA ----------------
z("luanda", "Luanda and Ndongo (Angola)", 13.23, -8.84,
  (F, "folk", "The Mbundu of the kingdom of Ndongo honoured ancestors and land spirits through their ngola kings."),
  (1600, "catholic", "After the Portuguese founded Luanda in 1576 and warred on Ndongo, Catholicism became the ruling faith of the colony and spread among the Mbundu around it, and Queen Njinga was baptised in 1622."))

z("angola-highlands", "Central Highlands (Angola)", 15.74, -12.78,
  (F, "folk", "The Ovimbundu kingdoms of the central plateau, great caravan traders, worshipped Suku the creator and their royal ancestors."),
  (1940, "catholic", "Congregationalist missionaries from 1880 and Catholic Spiritans converted most Ovimbundu in the early 20th century, Catholics becoming the larger church."))

z("angola-south", "Southern Angola (Huila)", 13.49, -14.92,
  (F, "folk", "The Nyaneka, Ovambo and Herero herders of the south followed ancestor and cattle cults."),
  (1960, "catholic", "Spiritan missions from the 1880s and Portuguese settlement made Catholicism the main faith of the Huila plateau in the 20th century."))

# ---------------- CAMEROON AND CHAD ----------------
z("cameroon-south", "Southern Cameroon (Yaounde)", 11.5, 3.87,
  (F, "folk", "The Beti, Bulu and Bassa peoples of the forest honoured ancestors and initiation societies such as the Beti so."),
  (1930, "catholic", "German Pallottines from 1890 and then French Spiritans converted most Beti, making the Yaounde region strongly Catholic, while the Bulu largely joined American Presbyterians."))

z("douala", "Cameroon coast (Douala)", 9.7, 4.05,
  (F, "folk", "The Duala trading chiefdoms of the Wouri estuary honoured ancestors and the water spirits called miengu."),
  (1910, "reformed", "Baptist missionaries led by Alfred Saker from 1845, then the Basel Mission from 1886 and the Paris Mission, made the Duala largely Protestant, the root of the Evangelical Church of Cameroon."))

z("grassfields", "Cameroon Grassfields", 10.16, 5.96,
  (F, "folk", "The Grassfields kingdoms such as Nso, Bali and the Bamileke chiefdoms revered sacred kings, skull ancestors and regulatory secret societies."),
  (1960, "catholic", "Basel Presbyterian missions from 1903 and Catholic Mill Hill and Sacred Heart missions converted the Grassfields in the 20th century, the Catholics becoming the largest church."))

z("adamawa", "Northern Cameroon (Adamawa)", 13.4, 9.3,
  (F, "folk", "The many peoples of the Benue plains and Mandara hills followed their own traditional religions."),
  (1810, "sunni", "Modibo Adama, a flag bearer of Usman dan Fodio, waged jihad from 1809 and founded the Adamawa emirate, whose Fulbe lamidates ruled and spread Islam across the north."))

z("ngaoundere", "Adamawa plateau (Ngaoundere)", 13.58, 7.32,
  (F, "folk", "The Mbum and Gbaya of the Adamawa plateau followed traditional religions."),
  (1835, "sunni", "Fulbe under Ardo Njobdi founded the lamidate of Ngaoundere in the 1830s within the Adamawa emirate, converting or subjecting the Mbum, and the plateau became mainly Muslim."))

z("kanem", "Kanem (Chad)", 15.31, 14.12,
  (F, "folk", "The Kanembu and Teda of Kanem followed traditional religions under their early Duguwa kings."),
  (1085, "sunni", "Mai Hummay of the Sayfawa dynasty converted to Islam around 1085, making Kanem one of the first Muslim kingdoms south of the Sahara, and his successors went on pilgrimage to Mecca."))

z("borno", "Borno (Nigeria)", 13.16, 11.85,
  (F, "folk", "The So people of the Lake Chad plains followed their own religion before Kanuri rule."),
  (1100, "sunni", "The Muslim Sayfawa kings of Kanem extended Islam to Borno, which became their seat after about 1380 and stayed a Muslim sultanate into the 20th century."))

z("baguirmi", "Baguirmi (Chad)", 16.17, 11.4,
  (F, "folk", "The Barma and their neighbours on the Chari river followed traditional religions."),
  (1600, "sunni", "Mbang Abdullah, who ruled from about 1568 to 1608, made Islam the court religion of the Baguirmi sultanate at Massenya, and it spread among the Barma."))

z("wadai", "Wadai (Chad)", 20.83, 13.83,
  (F, "folk", "The Maba and Tama peoples of the eastern highlands followed traditional religions under the Tunjur kings."),
  (1635, "sunni", "Abd al-Karim overthrew the Tunjur around 1635 and founded the Muslim sultanate of Wadai, which made Islam the faith of the Maba and their neighbours."))

z("borkou-tibesti", "Borkou and Tibesti (Chad)", 19.1, 17.93,
  (F, "folk", "The Toubou herders of the Tibesti and Borkou followed traditional religions."),
  (1650, "sunni", "The Toubou gradually adopted Islam from the 16th century through Kanem, the Fezzan and Saharan traders, and the Sanusi order strengthened it in the 19th century."))

z("chad-south", "Southern Chad", 16.08, 8.57,
  (F, "folk", "The Sara and their neighbours followed traditional religions, with yondo initiation for young men."),
  (1980, "protestant", "Protestant missions from the 1920s and Catholic missions under French rule converted most of the Sara south by the late 20th century, Protestants slightly ahead of Catholics."))

# ---------------- NIGER, MALI, MAURITANIA ----------------
z("air", "Air and Agadez (Niger)", 7.99, 16.97,
  (F, "folk", "Tuareg herders of the Air mountains and earlier Saharan peoples followed traditional cults."),
  (1400, "sunni", "Tuareg confederations adopted Islam through trade with the Maghreb, and the sultanate of Agadez, founded in the 15th century, became a centre of Islamic learning on the caravan routes."))

z("damagaram", "Damagaram (Zinder, Niger)", 8.99, 13.8,
  (F, "folk", "Hausa and Kanuri farmers around Zinder followed traditional cults of spirits such as the bori."),
  (1750, "sunni", "Kanuri Muslims from Borno founded the sultanate of Damagaram around 1731 and soon moved its capital to Zinder, and Islam became the faith of most of its Hausa subjects."))

z("niger-west", "Western Niger (Zarma and Songhay)", 2.11, 13.51,
  (F, "folk", "The Zarma and Songhay farmers along the Niger honoured river spirits and ancestors through possession cults."),
  (1850, "sunni", "Though Songhay kings had been Muslim since the 11th century, most Zarma and Songhay villagers became Muslim only in the 19th and early 20th centuries."))

z("gao", "Gao (Songhay, Mali)", -0.04, 16.27,
  (F, "folk", "Songhay fishermen and farmers of the Niger bend honoured river spirits and ancestors."),
  (1010, "sunni", "Za Kosoy, king of Gao, converted to Islam around 1010, and Gao became the Muslim capital of the Songhay Empire, whose Askia rulers made pilgrimage to Mecca."))

z("timbuktu", "Timbuktu (Mali)", -3.0, 16.77,
  (F, "folk", "Herders and farmers of the Niger bend followed traditional religions."),
  (1100, "sunni", "Tuareg founded Timbuktu around 1100 as a Muslim trading camp, and under Mali and Songhay it became a famous city of Islamic scholarship around the Sankore mosque."))

z("kidal", "Adrar des Ifoghas (Mali)", 1.41, 18.44,
  (F, "folk", "Berber herders of the Adrar des Ifoghas followed traditional Saharan cults."),
  (1100, "sunni", "The Tuareg of the Adrar des Ifoghas adopted Islam through trade with the Maghreb, and the nearby caravan town of Tadmekka was Muslim by the 11th century."))

z("djenne", "Djenne and the inland delta (Mali)", -4.55, 13.9,
  (F, "folk", "The Bozo, Marka and Bambara around the old city of Jenne-jeno honoured ancestors and the spirits of the inland Niger delta."),
  (1250, "sunni", "Koi Konboro, ruler of Djenne, converted in the 13th century and turned his palace into the first Great Mosque, and the Macina caliphate of 1818 later made the delta a Fulbe Muslim state."))

z("manding", "Manding (Mali Empire heartland)", -8.41, 11.93,
  (F, "folk", "The Mande of the upper Niger honoured ancestors and spirits through the komo power society and blacksmith priests."),
  (1240, "sunni", "Sundiata Keita founded the Mali Empire around 1235, and its mansas, such as Mansa Musa with his pilgrimage of 1324, ruled as Muslims, though many Mandinka farmers kept older faiths for centuries."))

z("segou", "Segou (Bambara, Mali)", -6.27, 13.44,
  (F, "folk", "The Bambara kept their ancestral religion of power objects and initiation societies, and the Bambara Empire of Segou, founded around 1712, upheld it against Muslim neighbours."),
  (1861, "sunni", "El Hadj Umar Tall's Tijani jihad conquered Segou in 1861, and Islam, spreading further under French rule, became the faith of most Bambara by the mid 20th century."))

z("mauritania-adrar", "Adrar (Mauritania)", -13.05, 20.52,
  (F, "folk", "Sanhaja Berber camel herders of the western Sahara followed their own religion."),
  (1050, "sunni", "The Almoravid movement of Abdallah ibn Yasin, born among the Sanhaja Berbers here in the 1040s, made the western Sahara strictly Sunni Muslim before conquering Morocco and Spain."))

z("ghana-empire", "Ghana Empire (southern Mauritania)", -7.97, 15.77,
  (F, "folk", "The Soninke kings of Ghana, at Koumbi Saleh, kept a royal cult of sacred groves and the snake spirit Bida, while Muslim merchants lived in their own town."),
  (1100, "sunni", "After the Almoravid wars of the 1070s, Ghana's kings and the Soninke became Muslim, and Soninke traders later spread Islam across West Africa."))

z("mauritania-west", "Western Mauritania (Trarza)", -15.97, 18.08,
  (F, "folk", "Berber herders of the Atlantic Sahara followed their own religion."),
  (1050, "sunni", "The Almoravids, whose movement began among the Sanhaja of the Mauritanian Sahara in the 1040s, made the region Muslim, and later Hassani Arab tribes and zawaya scholars kept it so."))

# ---------------- SENEGAMBIA AND UPPER GUINEA ----------------
z("futa-toro", "Futa Toro (Senegal river)", -14.96, 16.65,
  (F, "folk", "The farmers and herders of the middle Senegal valley followed traditional religions."),
  (1040, "sunni", "War Jabi, king of Takrur on the Senegal river, converted to Islam before his death around 1040, and the Toucouleur of Futa Toro, who renewed it in their revolution of 1776, have been Muslim since."))

z("wolof", "Cayor and Baol (Wolof Senegal)", -16.4, 14.9,
  (F, "folk", "The Wolof kingdoms of Cayor and Baol were ruled by damels and ceddo warriors who, though in contact with Islam, kept traditional religion."),
  (1880, "sunni", "Marabout movements and the collapse of the ceddo kingdoms under French conquest brought mass conversion, crowned by Amadou Bamba's Mouride brotherhood from 1883."))

z("saloum", "Saloum (Senegal)", -16.07, 14.15,
  (F, "folk", "The Serer and Wolof of the kingdom of Saloum followed traditional religions under their bour."),
  (1870, "sunni", "The jihad of Maba Diakhou Ba from 1861 and the spread of the Tijaniyya, later led from Kaolack by Ibrahima Niass, made Saloum Muslim."))

z("sine", "Sine (Serer, Senegal)", -16.41, 14.34,
  (F, "folk", "The Serer of Sine worshipped Roog, the supreme god, through saltigue priests, and their kingdom defeated Maba's jihad at Fandane-Thiouthioune in 1867."),
  (1930, "sunni", "Under French rule most Serer converted to Islam through the Mouride and Tijani brotherhoods, though a large Catholic minority, including President Senghor, also formed."))

z("casamance", "Casamance (Senegal)", -16.27, 12.58,
  (F, "folk", "The Jola rice farmers worshipped Emitai and the spirit shrines called boekin."),
  (1950, "sunni", "Islam spread among the Jola from Mandinka neighbours in the late 19th and 20th centuries, overtaking traditional religion, while the Catholic Church won a large minority."))

z("bundu", "Bundu (eastern Senegal)", -13.67, 13.77,
  (F, "folk", "The Soninke, Mandinka and Fulbe of the upper Senegal followed traditional religions alongside Muslim traders."),
  (1690, "sunni", "Malik Sy founded the Muslim almamate of Bundu around 1690, the first of the West African Fulbe jihad states, and Islam became the faith of its people."))

z("gambia", "The Gambia", -15.6, 13.45,
  (F, "folk", "The Mandinka, Wolof, Jola and Fula of the Gambia valley followed traditional religions, though Muslim traders and clerics had lived among them since Mali's time."),
  (1880, "sunni", "The Soninke Marabout wars of about 1850 to 1880 overthrew the old non-Muslim Mandinka kingdoms and made the Gambia valley overwhelmingly Muslim."))

z("guinea-bissau", "Guinea-Bissau", -15.6, 11.86,
  (F, "folk", "The Balanta, Papel, Manjak and Bijago peoples followed ancestral religions with spirit shrines."),
  (1990, "sunni", "Islam, long held by the Fula and Mandinka of the east, became the largest faith of Guinea-Bissau in the late 20th century, while traditional religion and Catholicism remain strong on the coast."))


z("futa-jallon", "Futa Jallon (Guinea)", -12.28, 11.32,
  (F, "folk", "The Jallonke and other farmers of the Futa Jallon highlands followed traditional religions."),
  (1725, "sunni", "Fulbe clerics led by Karamokho Alfa launched a jihad around 1725 and founded the almamate of Futa Jallon, a Muslim state whose schools made the highlands a centre of Islamic learning."))

z("upper-guinea", "Upper Guinea (Kankan)", -9.31, 10.38,
  (F, "folk", "The Malinke of the upper Niger honoured ancestors and spirits through power societies."),
  (1700, "sunni", "Kankan was founded around 1690 by the Muslim Kaba clerical clan, and Samori Toure's empire of the 1870s and 1880s pressed Islam on the Malinke of the upper Niger."))

z("guinea-coast", "Guinea coast (Susu)", -13.5, 9.7,
  (F, "folk", "The Susu, Baga and Nalu of the coast followed ancestral religions and secret societies."),
  (1850, "sunni", "Islam spread from the Futa Jallon to the Susu in the 18th and 19th centuries and the coast became Muslim, though some Baga kept their masks and shrines into the 20th century."))

z("freetown", "Freetown (Sierra Leone)", -13.23, 8.48,
  (F, "folk", "The Temne and Bullom of the peninsula honoured ancestors and spirits through secret societies such as Poro and Bondo."),
  (1792, "protestant", "Black Loyalists from Nova Scotia founded Freetown in 1792 as Methodists, Baptists and Huntingdonians, and liberated Africans landed after 1808 joined their churches and the Anglicans to form the Krio."),
  (1960, "sunni", "Migration from the provinces, where Islam had spread widely, made Muslims the majority in Freetown and the Western Area during the 20th century."))

z("sierra-leone-north", "Northern Sierra Leone (Temne)", -12.04, 8.88,
  (F, "folk", "The Temne, Limba and Loko followed ancestral religion and the Poro and Bondo secret societies."),
  (1900, "sunni", "Fula and Mandinka traders and clerics spread Islam among the Temne in the 18th and 19th centuries, and most northerners were Muslim by the early 20th century."))

z("sierra-leone-south", "Southern Sierra Leone (Mende)", -11.74, 7.96,
  (F, "folk", "The Mende worshipped Ngewo, the creator, and their ancestors, with the Poro and Sande societies as pillars of social life."),
  (1950, "sunni", "Islam spread among the Mende in the late 19th and 20th centuries, overtaking traditional religion, while Methodist and Catholic missions won a large Christian minority."))

z("liberia-coast", "Liberian coast (Monrovia)", -10.8, 6.3,
  (F, "folk", "The Dei, Bassa, Kru and Vai of the coast followed ancestral religions and the Poro and Sande societies."),
  (1822, "protestant", "Freed African Americans of the American Colonization Society founded Monrovia in 1822 as Methodists and Baptists, and as Americo-Liberians they ruled the country with their churches dominant."))

z("liberia-interior", "Liberian interior", -9.47, 7.0,
  (F, "folk", "The Kpelle, Loma, Gio and Mano followed ancestral religions with Poro and Sande initiation."),
  (1980, "protestant", "Lutheran, Methodist and above all Pentecostal churches converted most of the interior during the 20th century, though Poro and Sande remain influential."))

# ---------------- GULF OF GUINEA ----------------
z("ivory-coast-south", "Southern Ivory Coast", -4.02, 5.35,
  (F, "folk", "The Akan, Lagoon and Kru peoples honoured ancestors and lagoon and forest deities through priests and shrines."),
  (1950, "catholic", "The prophet William Wade Harris baptised some 100,000 people in 1913 to 1915, and Catholic missions present since 1895 gathered many of them, making the south largely Christian."))

z("ivory-coast-north", "Northern Ivory Coast", -5.63, 9.46,
  (F, "folk", "The Senufo followed their traditional religion organised by the Poro society, while Muslim Dyula traders lived in towns such as Kong."),
  (1980, "sunni", "Islam, carried by Dyula traders and Malinke migrants, became the majority faith among the Senufo and other northerners in the later 20th century."))

z("gold-coast", "Gold Coast (Fante and Ga)", -1.25, 5.1,
  (F, "folk", "The Fante and Ga worshipped the abosom, gods of lagoons, sea and land, and honoured ancestors through stools and festivals."),
  (1920, "protestant", "Wesleyan Methodists among the Fante from 1835 and the Basel Mission among the Ga and Akuapem from 1828 made the coastal south largely Protestant by the early 20th century."))

z("asante", "Asante (Ghana)", -1.62, 6.69,
  (F, "folk", "The Asante kingdom, built around the Golden Stool called down by the priest Okomfo Anokye about 1700, worshipped the abosom gods and the ancestors of the stools."),
  (1960, "protestant", "After British conquest in 1896 to 1901, Methodist, Presbyterian and Catholic schools converted the Asante, and Pentecostal churches have since become the largest group."))

z("dagbon", "Dagbon (northern Ghana)", -0.84, 9.4,
  (F, "folk", "The Dagomba kingdom of Dagbon and its neighbours followed traditional religions of earth shrines and ancestors."),
  (1950, "sunni", "Islam, the court religion since Ya Na Zangina converted around 1700, spread among the Dagomba people and became their majority faith in the 20th century."))

z("volta", "Volta (Ewe, Ghana)", 0.47, 6.6,
  (F, "folk", "The Ewe worshipped Mawu and the trowo deities, with priests and shrines in every town."),
  (1950, "catholic", "The Bremen Mission from 1847 and Catholic Divine Word missionaries from 1892 converted most Ewe, the Catholics becoming the largest church."))

z("togo-south", "Southern Togo", 1.22, 6.13,
  (F, "folk", "The Ewe and Mina of the coast worshipped Mawu and the vodun spirits."),
  (1950, "catholic", "Divine Word missionaries from 1892 under German rule and French Catholic missions later made Catholicism the leading faith of southern Togo, though vodun remains widely practised."))

z("togo-central", "Central Togo (Tem)", 1.13, 8.98,
  (F, "folk", "The Tem and their neighbours followed traditional religions."),
  (1850, "sunni", "The Tem chiefdoms around Sokode adopted Islam from Hausa and Dyula traders in the 19th century, making the region largely Muslim."))

z("dahomey", "Dahomey (southern Benin)", 1.99, 7.18,
  (F, "folk", "The Fon kingdom of Dahomey made the worship of the vodun and the royal ancestors a state religion, with annual customs at Abomey."),
  (1990, "catholic", "Catholic missions from 1861 at Ouidah slowly won the Fon, and Catholicism became the largest faith of the south in the late 20th century, though Vodun remains widely followed."))

z("borgu", "Borgu (northern Benin)", 2.63, 9.34,
  (F, "folk", "The Bariba kingdoms of Borgu followed traditional religion around their sacred kings."),
  (1950, "sunni", "Islam, long held by Dendi and Fulbe traders, spread among the Bariba in the 20th century and became the largest faith of northern Benin."))

# ---------------- BURKINA FASO ----------------
z("mossi", "Mossi Plateau (Burkina Faso)", -1.53, 12.37,
  (F, "folk", "The Mossi kingdoms resisted Islam for centuries and worshipped the earth and the royal ancestors, with the Mogho Naba as sacred king."),
  (1960, "sunni", "Islam, which entered the court with Mogho Naba Dulugu in the late 18th century, spread among ordinary Mossi in the 20th century and overtook traditional religion, while Catholicism won a large minority."))

z("burkina-west", "Western Burkina Faso", -4.3, 11.18,
  (F, "folk", "The Bobo, Bwa and Senufo followed traditional religions of masks and the Do cult."),
  (1930, "sunni", "Muslim Dyula traders had long lived at Bobo-Dioulasso, and Islam spread widely in the west from the late 19th century to become the majority faith."))

z("liptako", "Liptako (Burkina Faso)", -0.03, 14.03,
  (F, "folk", "The Gurmanche and Songhay of the Sahel followed traditional religions."),
  (1810, "sunni", "Fulbe led by Brahima Saidou launched a jihad around 1810 inspired by Usman dan Fodio and founded the Muslim emirate of Liptako at Dori."))

# ---------------- NIGERIA ----------------
z("kano", "Kano (Nigeria)", 8.52, 12.0,
  (F, "folk", "Hausa farmers of Kano honoured spirits through the bori cult and the sacred grove and shrine of Dala hill."),
  (1460, "sunni", "Islam came with Wangara clerics under Sarki Yaji in the 14th century, and Muhammad Rumfa, ruling from 1463, made it the law of Kano, though many villagers kept the old ways until the 1804 jihad."))

z("sokoto", "Sokoto (Nigeria)", 5.24, 13.06,
  (F, "folk", "The Hausa of Gobir and Kebbi honoured bori spirits, and their kings mixed Islam with older practice."),
  (1804, "sunni", "Usman dan Fodio's jihad from 1804 overthrew Gobir and founded the Sokoto Caliphate in 1809, the largest state in West Africa, which spread a reformed Sunni Islam across the Hausa lands."))

z("ilorin", "Ilorin and Old Oyo (Nigeria)", 4.55, 8.5,
  (F, "folk", "The Yoruba of northern Oyo worshipped the orisha, with the alaafin of the Oyo Empire as sacred king."),
  (1823, "sunni", "Fulani clerics allied to Sokoto took Ilorin after Afonja's revolt against Oyo and made it a Muslim emirate by 1823, and Old Oyo was abandoned soon after."))

z("nupe", "Nupe (Nigeria)", 6.01, 9.08,
  (F, "folk", "The Nupe kingdom on the middle Niger followed traditional religion around the sacred etsu."),
  (1830, "sunni", "Fulani jihadists took over the Nupe kingdom in the 1830s, and the emirate of Bida spread Islam among the Nupe."))

z("plateau", "Middle Belt (Jos Plateau)", 8.89, 9.9,
  (F, "folk", "The Berom, Ngas, Tarok and many other peoples of the Jos Plateau, never conquered by the Sokoto jihad, kept their own religions."),
  (1960, "protestant", "The Sudan United Mission from 1904 and other evangelical and Catholic missions converted most of the Plateau peoples, whose Church of Christ in Nations is now the largest body."))

z("benue", "Benue (Tiv and Idoma)", 8.53, 7.73,
  (F, "folk", "The Tiv and Idoma followed ancestor cults and protective spirit powers the Tiv called akombo."),
  (1960, "catholic", "South African Dutch Reformed missionaries from 1911 and Catholic Holy Ghost Fathers converted most of the Tiv and Idoma, the Catholic Church becoming the largest."))

z("oyo-ibadan", "Oyo and Ibadan (Yoruba)", 3.9, 7.38,
  (F, "folk", "The Yoruba worshipped Olodumare and the orisha such as Sango and Ogun, consulted Ifa divination and honoured the alaafin of Oyo."),
  (1910, "sunni", "Islam, brought by traders and clerics and strengthened from Ilorin, spread through Ibadan and Oyo in the 19th century, and Muslims became the largest group there by the early 20th century."))

z("egba", "Egba and Ogun (Yoruba)", 3.35, 7.15,
  (F, "folk", "The Egba worshipped the orisha and consulted Ifa, gathering at Olumo rock where they founded Abeokuta around 1830."),
  (1940, "anglican", "The Church Missionary Society came in 1846 at the invitation of Egba chiefs and Yoruba returnees from Sierra Leone, making Abeokuta a cradle of Nigerian Anglicanism beside a large Muslim community."))

z("ekiti-ondo", "Ekiti and Ondo (Yoruba)", 5.2, 7.25,
  (F, "folk", "The Ekiti, Ondo and Ijesa Yoruba worshipped the orisha and their sacred kings."),
  (1935, "protestant", "Anglican missions and the Aladura revival led by Joseph Babalola from 1930, which built the Christ Apostolic Church, made the eastern Yoruba overwhelmingly Christian."))

z("benin-city", "Benin Kingdom (Edo)", 5.62, 6.34,
  (F, "folk", "The Edo kingdom of Benin worshipped Osanobua, Olokun and the ancestors of the oba, its sacred king."),
  (1960, "protestant", "Portuguese priests baptised some of Oba Esigie's court around 1515 without lasting effect, and Christianity, now led by Pentecostal churches, became the majority faith after British conquest in 1897."))

z("igboland", "Igboland (Nigeria)", 7.5, 6.45,
  (F, "folk", "The Igbo worshipped Chukwu, the earth goddess Ala and many alusi, with oracles such as Ibini Ukpabi of Arochukwu."),
  (1930, "catholic", "Anglican missions from 1857 at Onitsha and Catholic Holy Ghost Fathers from 1885, whose schools under Bishop Shanahan drew huge numbers, made the Igbo mostly Christian, Catholics leading."))

z("calabar", "Efik and Ibibio (Calabar)", 8.33, 4.95,
  (F, "folk", "The Efik and Ibibio honoured ancestors, and the Ekpe leopard society governed the trading towns of Old Calabar."),
  (1910, "reformed", "Church of Scotland Presbyterians, arriving in 1846 under Hope Waddell, converted the Efik of Calabar, while the Qua Iboe Mission and Catholics won the Ibibio."))

z("niger-delta", "Niger Delta (Ijaw and Ikwerre)", 7.0, 4.82,
  (F, "folk", "The Ijaw and Ikwerre worshipped water spirits, ancestors and town deities such as the python of Bonny."),
  (1910, "anglican", "King George Pepple of Bonny invited Bishop Samuel Ajayi Crowther's Niger Delta mission in 1864, and Anglicanism spread through the delta city states, later joined by Pentecostal churches."))

# ---------------- ZAMBIA, MALAWI, MOZAMBIQUE, ZIMBABWE ----------------
z("zambia-central", "Central Zambia", 28.28, -15.42,
  (F, "folk", "The Tonga, Lenje and Soli honoured ancestors and rain shrines tended by spirit mediums."),
  (1960, "protestant", "Missions from the 1890s and the mixing of peoples in the towns made Zambia mostly Christian by independence, with evangelical and Pentecostal churches leading, and in 1991 it was declared a Christian nation."))

z("copperbelt", "Copperbelt (Zambia)", 28.2, -12.8,
  (F, "folk", "The Lamba and Lima followed ancestral religion under their chiefs."),
  (1950, "protestant", "Copper mines opened from the late 1920s drew workers whose union churches, later the United Church of Zambia, and Catholic and Pentecostal congregations made the Copperbelt Christian."))

z("bembaland", "Bembaland (Zambia)", 31.18, -10.21,
  (F, "folk", "The Bemba kingdom of the Chitimukulu worshipped Lesa and the royal ancestral spirits."),
  (1950, "catholic", "White Fathers entered Bembaland in 1895 and converted most of the Bemba, making northern Zambia strongly Catholic."))

z("barotseland", "Barotseland (Zambia)", 23.13, -15.25,
  (F, "folk", "The Lozi kingdom worshipped Nyambe, the creator, and honoured the royal graves of the litunga."),
  (1950, "reformed", "Francois Coillard's Paris Evangelical Mission came to Barotseland in 1885 at the invitation of Litunga Lewanika, and its Reformed church became the leading faith of the Lozi."))

z("malawi-north", "Northern Malawi", 34.0, -11.46,
  (F, "folk", "The Tumbuka and Ngoni of the north followed ancestral religions."),
  (1920, "reformed", "The Free Church of Scotland's Livingstonia Mission from 1875 educated and converted the north, whose Presbyterian synod of the CCAP is still the main church."))

z("malawi-central", "Central Malawi (Chewa)", 33.78, -13.97,
  (F, "folk", "The Chewa worshipped Chiuta and honoured ancestors through the Nyau masked society."),
  (1960, "catholic", "Dutch Reformed missionaries from 1889 and Catholic White Fathers and Montfortians converted most Chewa, Catholics the largest, though the Nyau masked dances still continue."))

z("malawi-south", "Southern Malawi (Shire Highlands)", 35.0, -15.79,
  (F, "folk", "The Mang'anja of the Shire highlands honoured ancestors and the rain shrine of Mbona."),
  (1930, "reformed", "The Church of Scotland's Blantyre Mission of 1876, followed by Catholic and Anglican missions, made the Shire highlands Christian, with the Presbyterian Blantyre Synod a leading church."))

z("yao", "Lake Malawi south (Yao)", 35.26, -14.48,
  (F, "folk", "The Yao of the southern lake region followed ancestral religion while trading ivory and slaves to the coast."),
  (1890, "sunni", "Yao chiefs such as Makanjira and Mponda adopted Islam from Swahili traders in the late 19th century, and their people became Muslim, the heart of Malawi's Muslim minority."))

z("mozambique-coast", "Northern Mozambique coast", 40.6, -15.1,
  (F, "folk", "Makua and other Bantu communities of the coast followed ancestral religions."),
  (1100, "sunni", "Swahili traders from Kilwa made the towns of Angoche and Mozambique Island Muslim, and though Portugal ruled from 1507, Islam spread among the coastal Makua and Koti."))

z("cabo-delgado", "Cabo Delgado (Mozambique)", 40.3, -12.97,
  (F, "folk", "The Makua and Makonde of the far north followed ancestral religions and initiation rites."),
  (1910, "sunni", "Swahili ties and Sufi brotherhoods, the Shadhiliyya and Qadiriyya, spread Islam among the Mwani and the Makua of the far north in the late 19th and early 20th centuries."))

z("zambezia", "Zambezia (Mozambique)", 36.89, -17.88,
  (F, "folk", "The Lomwe and Chuabo of the Zambezi lowlands honoured ancestors and rain spirits."),
  (1950, "catholic", "Portuguese prazo estates from the 17th century and Catholic missions favoured under the 1940 Concordat made Zambezia a Catholic stronghold."))

z("mozambique-south", "Southern Mozambique", 32.58, -25.97,
  (F, "folk", "The Tsonga, Ronga and Chopi honoured ancestors through healers and spirit mediums."),
  (1960, "catholic", "Swiss Presbyterian, Methodist and Catholic missions, and later Zionist churches, made the south Christian in the 20th century, with Catholics the largest single church."))

z("mashonaland", "Mashonaland (Zimbabwe)", 31.05, -17.83,
  (F, "folk", "The Shona of Great Zimbabwe and the Mutapa state worshipped Mwari, the high god, through mediums of royal ancestral spirits, the mhondoro."),
  (1960, "protestant", "Methodist, Anglican, Catholic and other missions from the 1890s, and then Apostolic and Pentecostal churches such as Johane Marange's, made most Shona Christian by the 1960s."))

z("matabeleland", "Matabeleland (Zimbabwe)", 28.58, -20.15,
  (F, "folk", "The Ndebele kingdom of Mzilikazi and Lobengula honoured royal ancestors and consulted the Mwari shrines of the Matopos."),
  (1960, "protestant", "The London Missionary Society opened Inyati in 1859 with few converts, but after the British conquest of 1893 churches spread, and Apostolic and Pentecostal churches now lead."))

# ---------------- SOUTHERN AFRICA ----------------
z("bangwato", "Bangwato (Botswana)", 26.71, -22.39,
  (F, "folk", "The Tswana chiefdoms worshipped Modimo and their ancestors, with rain making and initiation led by the chief."),
  (1875, "reformed", "Khama III, baptised by the London Missionary Society in 1862, ruled the Bangwato from 1875 to 1923 as a Christian king, abolishing initiation and rain rites and making the LMS church the tribal church."))

z("botswana-south", "Southern Botswana", 25.91, -24.65,
  (F, "folk", "The Kwena, Kgatla and other Tswana worshipped Modimo and honoured their ancestors."),
  (1950, "protestant", "Sechele I of the Bakwena was baptised by David Livingstone in 1848, and over the next century Congregational, Dutch Reformed, Zionist and Pentecostal churches made most Batswana Christian."))

z("namibia-central", "Central and southern Namibia", 17.08, -22.56,
  (F, "folk", "The Nama, Herero and Damara worshipped the creator and their ancestors, with the holy fire of the Herero homesteads."),
  (1900, "lutheran", "Rhenish missionaries from 1842 converted the Nama and many Herero, and after the German genocide of 1904 to 1908 most survivors joined the Lutheran churches."))

z("ovamboland", "Ovamboland (Namibia)", 15.95, -17.91,
  (F, "folk", "The Ovambo kingdoms worshipped Kalunga and honoured royal ancestors under sacred kings."),
  (1930, "lutheran", "Finnish Lutheran missionaries arriving in 1870 converted most of the Ovambo by the 1930s, and their church is now Namibia's largest."))

z("western-cape", "Western Cape (South Africa)", 18.42, -33.93,
  (F, "folk", "The Khoikhoi herders and San hunters of the Cape worshipped Tsui-Goab and Heitsi-Eibib and danced for rain."),
  (1652, "reformed", "Jan van Riebeeck's Dutch East India Company post of 1652 made the Dutch Reformed Church the ruling church of the Cape, slowly absorbing Khoikhoi and slaves, while the Cape Malays kept Islam."))

z("northern-cape", "Northern Cape (Orange river)", 21.25, -28.45,
  (F, "folk", "The Nama, Korana and San of the Orange river worshipped Tsui-Goab, Heitsi-Eibib and the San trickster gods."),
  (1850, "reformed", "London and Rhenish missions and the Dutch Reformed Church converted the Griqua, Korana and Nama of the Orange river, and Afrikaans speaking Reformed congregations became the norm."))

z("eastern-cape", "Eastern Cape (Xhosa)", 28.78, -31.59,
  (F, "folk", "The Xhosa worshipped Qamata and honoured the ancestors with cattle sacrifice and initiation."),
  (1950, "protestant", "Methodist missions from the 1820s, Anglicans and Presbyterians, and later Zionist churches converted most Xhosa, especially after the cattle killing of 1856 to 1857 broke the old order."))

z("kwazulu", "KwaZulu-Natal (Zulu)", 31.42, -28.33,
  (F, "folk", "The Zulu kingdom of Shaka worshipped uNkulunkulu and the amadlozi ancestors, with the king leading the first fruits ceremony."),
  (1970, "protestant", "Missions from the 1830s and above all African independent churches such as Isaiah Shembe's Nazareth Baptist Church and the Zionists made most Zulu Christian during the 20th century."))

z("free-state", "Free State (South Africa)", 26.21, -29.12,
  (F, "folk", "The Sotho, Tswana and Griqua of the highveld worshipped Modimo and their ancestors."),
  (1854, "reformed", "Voortrekkers of the Great Trek founded the Orange Free State in 1854 with the Dutch Reformed Church as its church, a ruling faith over a largely Sotho and Tswana population."),
  (1960, "protestant", "Missions to the Sotho and Tswana and the growth of Zionist, Methodist and Pentecostal churches made the black majority of the Free State Christian in the 20th century."))

z("transvaal", "Transvaal (Gauteng)", 28.19, -25.75,
  (F, "folk", "The Ndebele, Tswana and Pedi of the Transvaal worshipped the high god and their ancestors."),
  (1852, "reformed", "The Boer South African Republic, recognised in 1852, made the Dutch Reformed churches its state churches, ruling a mostly non-Christian African majority until the British conquest of 1900."),
  (1960, "protestant", "The Witwatersrand gold rush from 1886 gathered Africans from across the region, and Methodist, Zionist and Pentecostal churches made the black majority Christian by the mid 20th century."))

z("limpopo", "Limpopo (Pedi and Venda)", 29.45, -23.9,
  (F, "folk", "The Pedi kingdom and the Venda honoured ancestors, sacred lakes and rain queens such as the Lovedu Modjadji."),
  (1970, "protestant", "Berlin Lutheran missions from the 1860s and the Zion Christian Church, founded in 1924 by Engenas Lekganyane at Moria near Polokwane, made most of the region Christian."))

z("lesotho", "Lesotho", 27.48, -29.32,
  (F, "folk", "The Basotho worshipped Molimo and their ancestors, the balimo, with initiation schools for boys and girls."),
  (1930, "catholic", "King Moshoeshoe I invited Paris Evangelical missionaries in 1833 and Catholic Oblates came in 1862, and by the 20th century most Basotho were Christian, Catholics the largest church."))

z("eswatini", "Eswatini", 31.13, -26.32,
  (F, "folk", "The Swazi worshipped Mvelincanti and the royal ancestors, with the king at the heart of the Incwala ceremony."),
  (1960, "protestant", "Wesleyan missions from 1844 and later Zionist and Pentecostal churches made most Swazi Christian, while the Incwala and royal ancestral rites remain."))

# ---------------- MADAGASCAR AND ISLANDS ----------------
z("imerina", "Imerina (Madagascar)", 47.52, -18.91,
  (F, "folk", "The Merina worshipped Andriamanitra, the creator, honoured the razana ancestors and kept royal talismans called sampy."),
  (1869, "reformed", "Queen Ranavalona II was baptised in 1869 and burned the royal sampy, making the London Missionary Society's Congregational church the state church of the Merina kingdom after decades of persecution."))

z("betsileo", "Betsileo (Madagascar)", 47.08, -21.45,
  (F, "folk", "The Betsileo rice farmers of the southern highlands honoured the razana ancestors with famadihana reburials."),
  (1930, "catholic", "Jesuit missions, strengthened under French rule from 1896, made the Betsileo highlands one of the most Catholic regions of Madagascar."))

z("madagascar-south", "Southern Madagascar", 43.67, -23.35,
  (F, "folk", "The Mahafaly, Antandroy and Vezo of the south honour ancestors with great tombs, cattle sacrifice and spirit possession, and Christianity has spread only slowly there."))





out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zones_africa.json")
with open(out, "w") as f:
    json.dump(Z, f, ensure_ascii=False, indent=1)
print(len(Z), "zones written to", out)

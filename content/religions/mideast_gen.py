"""Generate zones_mideast.json: Middle East, North Africa and Central Asia religious history zones."""
import json, os

H = os.path.dirname(os.path.abspath(__file__))
Z = []


def z(id, name, lon, lat, *hist):
    Z.append({"id": id, "name": name, "lon": lon, "lat": lat,
              "history": [{"from": f, "faith": r, "note": n} for f, r, n in hist]})


# Shared building blocks
SOVIET = (1928, "secular", "Soviet rule closed nearly all mosques and madrasas, unveiled women in the hujum campaign and imposed state atheism, though most people kept a Muslim identity in private.")
SOVIET_END = "Independence in 1991 brought an open revival of Sunni Islam, with new mosques and religious schools, under a secular state."

# ------------------------------------------------------------------ ANATOLIA
z("anatolia-west", "Western Anatolia (Ionia and Lydia)", 28.0, 38.5,
  (-10000, "folk", "Early farming peoples of western Anatolia worshipped local gods and a mother goddess."),
  (-1600, "mesopotamian", "Luwian kingdoms such as Arzawa shared the storm god and the gods of the Hittite and Hurrian world."),
  (-1000, "hellenic", "Ionian Greek colonists and the Lydian kings spread Greek cults, with great temples such as the Artemision at Ephesus."),
  (325, "christian", "Home of Paul's churches and the Seven Churches of Revelation, Asia Minor was among the first regions with a Christian majority by the early 4th century."),
  (1054, "orthodox", "The region's Greek Christians stayed with the Patriarch of Constantinople when Rome and Constantinople split in 1054."),
  (1400, "sunni", "Turkish beyliks such as Aydin and Saruhan, then the Ottomans by 1390, ruled the region, and conversion and Turkmen settlement made it majority Sunni Muslim in the 15th century."))

z("anatolia-central", "Central Anatolia (Cappadocia and Galatia)", 32.9, 39.9,
  (-10000, "folk", "Neolithic towns such as Catalhoyuk worshipped local goddesses and ancestors."),
  (-1650, "mesopotamian", "Hittite kings at Hattusa worshipped a 'thousand gods' of Hattian, Hurrian and Mesopotamian origin, led by the storm god and the sun goddess of Arinna."),
  (-330, "hellenic", "After Alexander, Hellenistic and then Roman rule (Galatia, 25 BC) merged the gods of Phrygians and Galatian Celts, such as Cybele, into Greek and Roman religion."),
  (325, "christian", "Cappadocia and Galatia became solidly Christian by the 4th century, the land of the Cappadocian Fathers Basil, Gregory of Nyssa and Gregory of Nazianzus."),
  (1054, "orthodox", "Byzantine Anatolia sided with Constantinople in the 1054 schism with Rome."),
  (1300, "sunni", "After Manzikert (1071) the Seljuk Sultanate of Rum ruled from Konya, and Turkmen settlement and conversion made central Anatolia majority Sunni Muslim by about 1300."))

z("anatolia-east", "Eastern Anatolia (Armenian Highlands)", 41.3, 39.9,
  (-10000, "folk", "Highland peoples around Lake Van worshipped local gods of mountains and springs."),
  (-850, "mesopotamian", "The kingdom of Urartu worshipped Haldi, Teisheba and Shivini in a pantheon shaped by Hurrian and Assyrian religion."),
  (-550, "zoroastrianism", "Under Persian rule the Armenians adopted an Iranian, Mazdean religion of Aramazd, Anahit and Mihr."),
  (301, "christian", "King Tiridates III, converted by Gregory the Illuminator, made Armenia the first kingdom with Christianity as its state religion."),
  (506, "oriental", "The Armenian Church formally rejected the Council of Chalcedon at the Council of Dvin in 506, joining the Oriental Orthodox churches."),
  (1514, "sunni", "Seljuk, Turkmen and Kurdish settlement after 1071 and Ottoman rule after Chaldiran (1514) made Muslims the majority by the 16th century; Armenians stayed numerous until the 1915 genocide."))

z("pontus", "Pontus (Black Sea coast)", 39.7, 40.9,
  (-10000, "folk", "Peoples of the Black Sea mountains such as the Chalybes worshipped local gods."),
  (-600, "hellenic", "Greek colonies like Sinope and Trapezus, and later the Hellenized kings of Pontus and Rome, spread Greek religion along the coast."),
  (350, "christian", "The Pontic coast became Christian during the 4th century under Roman and Byzantine rule."),
  (1054, "orthodox", "The region followed Constantinople in the 1054 schism; the Empire of Trebizond (1204 to 1461) remained a Greek Orthodox state."),
  (1650, "sunni", "After the Ottoman conquest of Trebizond in 1461, conversion over the 16th and 17th centuries made the coast majority Muslim; the Pontic Greeks left in the 1923 population exchange."))

z("cilicia", "Cilicia (Adana and Tarsus)", 35.3, 37.0,
  (-10000, "folk", "Early farmers of the Cilician plain worshipped local gods."),
  (-1600, "mesopotamian", "The kingdom of Kizzuwatna, later Hittite, worshipped Hurrian and Luwian gods such as Teshub and Hebat."),
  (-330, "hellenic", "Alexander's conquest and Roman rule made Tarsus and the Cilician cities centres of Greek religion and learning."),
  (350, "christian", "Cilicia, home of Paul of Tarsus, became Christian by the 4th century."),
  (700, "sunni", "Arab conquest turned Cilicia into the thughur, the Muslim frontier against Byzantium, with Tarsus and Adana settled by Muslim garrisons."),
  (965, "christian", "Emperor Nikephoros Phokas reconquered Cilicia in 965, expelled its Muslims and resettled it with Greek, Armenian and Syriac Christians."),
  (1054, "orthodox", "Byzantine Cilicia sided with Constantinople in the 1054 schism with Rome."),
  (1080, "oriental", "Armenian princes founded the Armenian Kingdom of Cilicia, and Armenian Apostolic Christians became the leading population until 1375."),
  (1375, "sunni", "The Mamluks destroyed the Armenian kingdom in 1375, and Turkmen Ramazanid and then Ottoman rule made Cilicia majority Sunni Muslim."))

z("upper-mesopotamia", "Upper Mesopotamia (Edessa and Diyarbakir)", 39.8, 37.5,
  (-10000, "folk", "Early sanctuaries such as Gobekli Tepe show the first monumental religious sites here."),
  (-2500, "mesopotamian", "Hurrian and Assyrian gods ruled the region, and Harran's moon god Sin was worshipped into Islamic times."),
  (200, "christian", "King Abgar VIII of Edessa is remembered as the first Christian ruler, and Edessa became the heart of Syriac Christianity."),
  (451, "oriental", "Most Syriac Christians rejected Chalcedon; Jacob Baradaeus of Tella organized the Syriac Orthodox Church here in the 540s."),
  (1150, "sunni", "Seljuk conquest, Turkmen and Kurdish settlement and the fall of Crusader Edessa (1144) made the region majority Muslim; Syriac and Armenian Christians remained numerous until 1915."))

# ------------------------------------------------------------------ LEVANT
z("syria-north", "Northern Syria (Aleppo)", 37.2, 36.2,
  (-10000, "folk", "Early farming villages of northern Syria worshipped local gods."),
  (-2500, "mesopotamian", "Ebla and then Aleppo worshipped the storm god Hadad and the Amorite, Hurrian and Aramaean gods."),
  (-300, "hellenic", "The Seleucid kings founded Antioch and spread Greek religion, and the Romans added the emperor cult."),
  (380, "christian", "Antioch was one of the oldest Christian centres, and northern Syria was largely Christian by the late 4th century."),
  (451, "oriental", "Most of the Syriac countryside rejected Chalcedon and formed the Syriac Orthodox Church, while Greek cities stayed Chalcedonian."),
  (944, "shia", "By the time the Twelver Shia Hamdanid Sayf al-Dawla took Aleppo in 944, Muslims were the majority, and Aleppo's townspeople were largely Imami Shia until the 12th century."),
  (1148, "sunni", "Nur al-Din banned the Shia call to prayer in Aleppo in 1148 and founded Sunni madrasas, and the city and region became firmly Sunni."))

z("syria-damascus", "Southern Syria (Damascus)", 36.3, 33.5,
  (-10000, "folk", "Early farming peoples of the Damascus oasis worshipped local gods."),
  (-2500, "mesopotamian", "Amorite and then Aramaean kingdoms worshipped Hadad, the storm god of Damascus, and other Canaanite and Mesopotamian gods."),
  (-300, "hellenic", "Seleucid and then Roman rule turned Hadad's temple into the great temple of Jupiter Damascenus."),
  (380, "christian", "Christianity became the religion of the Empire, and the temple of Jupiter became the church of John the Baptist."),
  (900, "sunni", "Conquered in 634 and made the Umayyad capital in 661, southern Syria slowly became majority Muslim, probably by around the 10th century."),
  (970, "ismaili", "The Ismaili Fatimid caliphs of Cairo ruled Damascus from 970, a ruling faith the Sunni townspeople largely resisted."),
  (1076, "sunni", "The Seljuk Turks took Damascus in 1076 and restored Sunni rule, later championed by Nur al-Din and Saladin."))

z("mount-lebanon", "Mount Lebanon", 35.8, 34.1,
  (-10000, "folk", "Early peoples of the Lebanon mountains worshipped local gods of springs and high places."),
  (-3000, "mesopotamian", "Phoenician cities such as Byblos worshipped Baal, Astarte and Adonis, whose cult centre was at Afqa in the mountains."),
  (-64, "hellenic", "Roman rule fused the Phoenician gods with Roman ones, as at the great temple of Jupiter at Baalbek."),
  (450, "christian", "Disciples of the hermit Saint Maron converted the mountain villages in the 5th century; the Maronites later stood apart from both Byzantium and Rome."),
  (1182, "catholic", "The Maronite Church entered full union with Rome during the Crusades (about 1182), and Maronite Catholics remain the majority of Mount Lebanon."))

z("jabal-amil", "Southern Lebanon (Jabal Amil)", 35.4, 33.3,
  (-10000, "folk", "Early peoples of the southern Lebanese hills worshipped local gods."),
  (-3000, "mesopotamian", "Phoenician Tyre and Sidon worshipped Melqart, Eshmun and Astarte."),
  (-64, "hellenic", "Roman rule brought Roman temples and the emperor cult to Tyre and Sidon."),
  (400, "christian", "Tyre and Sidon became Christian bishoprics and the region Christian by about 400."),
  (1000, "shia", "After the Muslim conquest of 635, the people of Jabal Amil became Twelver Shia by about the 11th century; its scholars later helped convert Safavid Iran."))

z("israel", "Israel (coastal plain and Galilee)", 34.9, 32.1,
  (-10000, "folk", "Natufian and Neolithic peoples of the land buried and honoured their ancestors."),
  (-3000, "mesopotamian", "Canaanite city states worshipped El, Baal, Asherah and Astarte."),
  (-1000, "judaism", "The Israelite kingdoms worshipped Yahweh, and Judaism took shape around the Torah and the Jerusalem Temple."),
  (135, "hellenic", "After the Bar Kokhba revolt (132 to 135) Rome expelled Jews from Judea and refounded Jerusalem as the pagan Aelia Capitolina, though Galilee stayed Jewish."),
  (425, "christian", "Imperial patronage of the Holy Land and the closure of pagan temples, such as Gaza's Marneion in 402, made the land majority Christian in the 5th century."),
  (970, "ismaili", "Conquered by the Arabs in 634 to 640, the land came under Ismaili Fatimid rule in 970 as conversion slowly turned it Muslim, mostly Sunni; Christians were still numerous."),
  (1099, "catholic", "Latin crusaders ruled the Kingdom of Jerusalem from 1099, a ruling faith over a population of Eastern Christians and Muslims."),
  (1187, "sunni", "Saladin's reconquest in 1187 and Ayyubid and Mamluk rule completed the land's long shift to a Sunni Muslim majority."),
  (1948, "judaism", "Zionist immigration and the founding of Israel in 1948, with the flight and expulsion of most Palestinian Arabs, gave the land a Jewish majority."))

z("palestine", "Palestine (West Bank and Gaza)", 35.25, 31.95,
  (-10000, "folk", "Natufian and Neolithic peoples, as at Jericho, buried and honoured their ancestors."),
  (-3000, "mesopotamian", "Canaanite city states worshipped El, Baal, Asherah and Astarte."),
  (-1000, "judaism", "The Israelite kingdoms worshipped Yahweh, and Judaism took shape around the Torah and the Jerusalem Temple."),
  (135, "hellenic", "After the Bar Kokhba revolt Rome expelled Jews from Judea and refounded Jerusalem as the pagan Aelia Capitolina."),
  (425, "christian", "Constantine's Church of the Holy Sepulchre, pilgrimage and monasticism made the Holy Land majority Christian in the 5th century."),
  (970, "ismaili", "Conquered by the Arabs in 634 to 640, the land came under Ismaili Fatimid rule in 970 as conversion slowly turned it Muslim, mostly Sunni; Christians were still numerous."),
  (1099, "catholic", "Latin crusaders ruled the Kingdom of Jerusalem from 1099, a ruling faith over a population of Eastern Christians and Muslims."),
  (1187, "sunni", "Saladin's reconquest of Jerusalem in 1187 and Ayyubid and Mamluk rule completed the land's long shift to a Sunni Muslim majority, which Palestinians remain today."))

z("jordan", "Jordan", 35.9, 31.9,
  (-10000, "folk", "Neolithic peoples such as those of Ain Ghazal made plaster statues of their gods or ancestors."),
  (-3000, "mesopotamian", "Ammonites, Moabites and Edomites worshipped Milcom and Chemosh, and later the Nabataeans of Petra worshipped Dushara and al-Uzza."),
  (106, "hellenic", "Rome annexed the Nabataean kingdom as the province of Arabia in 106, and the Decapolis cities such as Gerasa built Roman temples."),
  (400, "christian", "The land became Christian under Byzantine rule, as the church mosaics of Madaba show."),
  (750, "sunni", "After the Muslim victory at Yarmouk in 636, Arab tribes and gradual conversion made the land majority Muslim by about the Abbasid era."))

# ------------------------------------------------------------------ IRAQ
z("iraq-north", "Northern Iraq (Mosul and Assyria)", 43.1, 36.3,
  (-10000, "folk", "Early farmers of the northern Mesopotamian plains worshipped local gods."),
  (-2500, "mesopotamian", "Assyria worshipped the god Ashur and Ishtar of Nineveh and Arbela, the state cult of the Assyrian empire."),
  (484, "east-syriac", "Christianity spread through Adiabene and Nineveh, and by the late 5th century most Aramaic speakers here belonged to the Church of the East, confirmed at the Synod of Beth Lapat (484)."),
  (900, "sunni", "After the Arab conquest of 641, Arab settlement and conversion of Kurds and Aramaeans made the region majority Sunni Muslim by about the 10th century, with many Christian villages remaining."))

z("iraq-baghdad", "Central Iraq (Baghdad and Babylonia)", 44.4, 33.3,
  (-10000, "folk", "Early farmers of the Mesopotamian plain worshipped local gods."),
  (-3500, "mesopotamian", "Sumer, Akkad and Babylon worshipped city gods such as Enlil and Marduk, whose cult in Babylon lasted into the 1st century AD."),
  (226, "zoroastrianism", "The Sasanians ruled from Ctesiphon with Zoroastrianism as state faith over a mixed population of Christians, Jews, Mandaeans and pagans."),
  (762, "sunni", "After the Arab conquest (637), Kufa and the new Abbasid capital Baghdad (762) became centres of Islamic learning, and the region was majority Muslim, mostly Sunni, by the 9th century."),
  (1960, "shia", "Migration from the Shia south, to districts such as Sadr City, gave Baghdad and central Iraq a Shia majority by the late 20th century."))

z("iraq-south", "Southern Iraq (Basra, Najaf and Karbala)", 46.5, 31.0,
  (-10000, "folk", "Early peoples of the southern marshes such as the Ubaid culture built the first temples at Eridu."),
  (-3500, "mesopotamian", "The Sumerian cities Ur, Uruk and Eridu worshipped Nanna, Inanna and Enki."),
  (226, "zoroastrianism", "The Sasanian state favoured Zoroastrianism over a mixed population of Christians, Jews, Mandaeans and pagans."),
  (650, "sunni", "Arab conquest and the garrison cities of Basra (636) and Kufa (638) brought Arab settlers and Islam; Ali's shrine at Najaf and Husayn's at Karbala made it Shia holy land."),
  (1800, "shia", "Shia clerics from the shrine cities converted the Arab tribes of the south to Twelver Shia Islam in the late 18th and 19th centuries."))

# ------------------------------------------------------------------ IRAN
z("iran-west", "Western Iran (Isfahan and Hamadan)", 51.7, 32.7,
  (-10000, "folk", "Early peoples of the Iranian plateau worshipped local gods."),
  (-650, "zoroastrianism", "The Medes and the Achaemenid Persians worshipped Ahura Mazda through magi priests, and Zoroastrianism became the religion of Iran."),
  (900, "sunni", "After the Arab conquest of 642 to 651, Iranians converted gradually and the plateau was majority Muslim, mostly Sunni, by about the 10th century."),
  (1501, "shia", "Shah Ismail I made Twelver Shia Islam the state religion in 1501, and the Safavids converted most Iranians over the next century."))

z("iran-azerbaijan", "Iranian Azerbaijan (Tabriz)", 46.3, 38.1,
  (-10000, "folk", "Early peoples around Lake Urmia worshipped local gods."),
  (-600, "zoroastrianism", "Media Atropatene was a Zoroastrian heartland, home of the royal fire temple Adur Gushnasp at Takht-e Soleyman."),
  (900, "sunni", "After the Arab conquest the region became majority Muslim, mostly Shafi'i Sunni, by about the 10th century."),
  (1501, "shia", "Ismail I, leader of the Safavid order of Ardabil, was crowned at Tabriz in 1501 and made Twelver Shia Islam the faith of Azerbaijan and Iran."))

z("tabaristan", "Tabaristan and Gilan (Caspian Iran)", 53.0, 36.5,
  (-10000, "folk", "Early peoples of the Caspian forests worshipped local gods."),
  (-600, "zoroastrianism", "The Caspian provinces were Zoroastrian, and local Dabuyid and Bavandid princes kept the old faith for two centuries after the Arab conquest."),
  (864, "shia", "Zaydi Shia Alids founded a state in Tabaristan in 864 and converted the Daylamites; the region later became Twelver Shia under the Marashis and Safavids."))

z("khuzestan", "Khuzestan (Elam)", 48.7, 31.6,
  (-10000, "folk", "Early peoples of the Susiana plain worshipped local gods."),
  (-3200, "mesopotamian", "Elam worshipped Inshushinak, Humban and Kiririsha in a religion closely tied to Mesopotamia."),
  (-539, "zoroastrianism", "Susa became an Achaemenid capital, and Persian Zoroastrianism gradually replaced the Elamite gods."),
  (900, "sunni", "After the Arab conquest of the 640s, the province became majority Muslim by about the 10th century."),
  (1501, "shia", "Safavid rule from 1501, after the Shia Musha'sha' dynasty of Hoveyzeh, made the region Twelver Shia."))

z("fars", "Fars (Persis)", 52.5, 29.6,
  (-10000, "folk", "Early peoples of the Zagros valleys worshipped local gods."),
  (-550, "zoroastrianism", "Persis was the homeland of the Achaemenids and Sasanians and the last stronghold of Zoroastrian priests after the Arab conquest."),
  (950, "sunni", "Fars resisted conversion longer than most of Iran, but by the mid 10th century Muslims were the majority."),
  (1501, "shia", "The Safavids made Twelver Shia Islam the state religion in 1501 and converted the population over the following century."))

z("iran-khorasan", "Khorasan (Mashhad and Nishapur)", 59.6, 36.3,
  (-10000, "folk", "Early peoples of Khorasan worshipped local gods."),
  (-600, "zoroastrianism", "Parthia and Khorasan, near Zoroaster's eastern homeland, were Zoroastrian under the Achaemenids, Parthians and Sasanians."),
  (850, "sunni", "After the Arab conquest of 651, Khorasan converted faster than western Iran and was majority Sunni Muslim by the mid 9th century, as Nishapur's records show."),
  (1510, "shia", "Ismail I took Khorasan in 1510, and Safavid rule and the shrine of Imam Reza at Mashhad made the region Twelver Shia."))

# ------------------------------------------------------------------ ARABIA
z("hejaz", "Hejaz (Mecca and Medina)", 39.9, 21.5,
  (-10000, "folk", "Arab tribes worshipped Hubal, al-Lat, al-Uzza and Manat, with the Kaaba at Mecca as their chief sanctuary."),
  (630, "sunni", "Muhammad's conquest of Mecca in 630 cleansed the Kaaba of idols and made the Hejaz the heart of Islam; early Islam is shown here as Sunni."))

z("najd", "Najd (Riyadh)", 46.7, 24.7,
  (-10000, "folk", "The Bedouin tribes of central Arabia worshipped tribal gods and sacred stones."),
  (632, "sunni", "The tribes of Najd submitted to Islam in the Ridda wars of 632 to 633; in 1744 Muhammad ibn Abd al-Wahhab's alliance with the Saudis began the Wahhabi reform."))

z("yemen-highlands", "Northern Yemen (Sanaa and Saada)", 44.2, 15.4,
  (-10000, "folk", "Saba, Main and Himyar worshipped the moon god Almaqah and other South Arabian gods at temples such as Marib's Awwam."),
  (380, "judaism", "Himyarite kings abandoned the old gods around 380 for a Jewish monotheism, and King Yusuf Dhu Nuwas ruled as a Jew until 525; this was mainly the ruling faith."),
  (525, "oriental", "The Christian Aksumites of Ethiopia conquered Himyar in 525, and their viceroy Abraha built a great Miaphysite church at Sanaa."),
  (630, "sunni", "Yemen's tribes and Persian governor Badhan embraced Islam around 630."),
  (897, "shia", "Al-Hadi ila al-Haqq founded the Zaydi imamate at Saada in 897; the northern highlands became Zaydi Shia (distinct from Twelvers) under imams who ruled until 1962."))

z("yemen-south", "Lower Yemen (Taiz and Aden)", 44.0, 13.6,
  (-10000, "folk", "Saba, Qataban and Himyar worshipped the moon god Almaqah and other South Arabian gods."),
  (380, "judaism", "Himyarite kings adopted a Jewish monotheism around 380; King Yusuf Dhu Nuwas ruled as a Jew until 525. This was mainly the ruling faith."),
  (525, "oriental", "The Christian Aksumites of Ethiopia conquered Himyar in 525 and ruled through Abraha, a Miaphysite Christian."),
  (630, "sunni", "Yemen accepted Islam around 630, and lower Yemen became Shafi'i Sunni."),
  (1047, "ismaili", "The Ismaili Sulayhid dynasty, allies of the Fatimids, ruled lower Yemen from 1047, under Queen Arwa from Jibla; a ruling faith over a mostly Sunni people."),
  (1174, "sunni", "Turanshah's Ayyubid conquest of 1174 ended Ismaili rule, and lower Yemen remained Shafi'i Sunni."))

z("hadramawt", "Hadramawt", 48.6, 15.9,
  (-10000, "folk", "The kingdom of Hadramawt worshipped the moon god Sayin and other South Arabian gods."),
  (630, "sunni", "The tribes of Hadramawt accepted Islam around 630."),
  (745, "ibadi", "Hadramawt became an Ibadi stronghold after the revolt of Talib al-Haqq in 745, and Ibadism remained strong here until about the 12th century."),
  (1150, "sunni", "Shafi'i Sunni Islam, spread by the Ba Alawi sayyids descended from Ahmad al-Muhajir, replaced Ibadism by the 12th century."))

z("oman", "Oman", 57.5, 22.9,
  (-10000, "folk", "The peoples of Magan worshipped local gods; Arab tribes later honoured tribal deities."),
  (630, "sunni", "The Julanda rulers of Oman accepted Islam around 630, in the early years before the sectarian splits."),
  (751, "ibadi", "Oman elected its first Ibadi imam, al-Julanda ibn Masud, in 751, and has been the heartland of Ibadi Islam ever since."))

z("uae", "United Arab Emirates", 55.5, 24.2,
  (-10000, "folk", "The peoples of the Oman peninsula worshipped local and tribal gods."),
  (630, "sunni", "The Azd tribes of the coast accepted Islam around 630; most Emiratis today are Sunni Muslims."))

z("qatar", "Qatar", 51.2, 25.3,
  (-10000, "folk", "Arab tribes worshipped local gods; some Christians of the Church of the East lived here before Islam."),
  (630, "sunni", "The peninsula embraced Islam around 630; Qatar's rulers adopted the Wahhabi reform in the 19th century."))

z("bahrain", "Bahrain", 50.55, 26.05,
  (-10000, "folk", "Early peoples of the island worshipped local gods."),
  (-2200, "mesopotamian", "Dilmun, a trading kingdom, worshipped Inzak and Enki in a religion close to Mesopotamia's."),
  (629, "sunni", "Al-Mundhir ibn Sawa, ruler of Bahrain, accepted Islam around 629."),
  (899, "ismaili", "The Ismaili Qarmatians founded a state in eastern Arabia in 899 and seized the Black Stone of the Kaaba in 930."),
  (1077, "shia", "After the Qarmatian state fell in 1077, the island's Baharna farmers became Twelver Shia, and Bahrain grew into a centre of Shia learning."))

z("al-ahsa", "Al-Ahsa and Qatif (Eastern Arabia)", 49.6, 25.4,
  (-10000, "folk", "The oasis peoples of eastern Arabia worshipped local gods."),
  (629, "sunni", "The tribes of the region accepted Islam around 629."),
  (899, "ismaili", "The Ismaili Qarmatians ruled eastern Arabia from al-Ahsa from 899 to 1077 and seized the Black Stone of the Kaaba in 930."),
  (1077, "shia", "After the Qarmatian state fell, the oasis farmers of al-Ahsa and Qatif became Twelver Shia, as many remain today."))

z("kuwait", "Kuwait", 47.6, 29.2,
  (-10000, "folk", "Early peoples worshipped local gods; Failaka island held a Greek sanctuary under the Seleucids."),
  (630, "sunni", "The region embraced Islam around 630; Kuwait, founded by the Bani Utbah around 1716, is majority Sunni with a large Shia minority."))

# ------------------------------------------------------------------ EGYPT AND LIBYA
z("egypt", "Lower Egypt (Cairo and the Delta)", 31.2, 30.0,
  (-10000, "folk", "Prehistoric Nile peoples buried their dead with offerings and worshipped animal and fertility gods."),
  (-3100, "egyptian", "The unified kingdom worshipped Ra, Osiris, Isis and Horus, with the pharaoh as divine king."),
  (325, "christian", "Egypt, home of Alexandria's church and the first monks, became majority Christian by about the early 4th century."),
  (451, "oriental", "Most Egyptians rejected the Council of Chalcedon and followed the Coptic Orthodox Church."),
  (969, "ismaili", "The Ismaili Fatimids founded Cairo in 969; Muslims, mostly Sunni, probably became the majority in this era, though some scholars place it as late as the 14th century."),
  (1171, "sunni", "Saladin ended the Fatimid caliphate in 1171 and restored Sunni Islam, and Mamluk era pressures shrank the Copts to a minority."))

z("egypt-upper", "Upper Egypt (Thebes and Asyut)", 32.6, 25.7,
  (-10000, "folk", "Prehistoric Nile peoples buried their dead with offerings and worshipped animal and fertility gods."),
  (-3100, "egyptian", "Upper Egypt worshipped Amun at Thebes, Horus at Edfu and Hathor at Dendera."),
  (350, "christian", "Christianity, spread by monks such as Pachomius, became the majority faith of Upper Egypt in the 4th century."),
  (451, "oriental", "Upper Egypt became the heartland of the Coptic Orthodox Church after Chalcedon in 451."),
  (1350, "sunni", "Copts in the south remained numerous long after the Arab conquest; Mamluk persecutions and mass conversions from 1301 to 1354 left Muslims the majority by the 14th century."))

z("cyrenaica", "Cyrenaica (eastern Libya)", 21.8, 32.6,
  (-10000, "folk", "Libyan Berber tribes worshipped local gods and the oracle of Ammon."),
  (-630, "hellenic", "Greeks from Thera founded Cyrene in 631 BC, and Cyrenaica became a centre of Greek and then Roman religion."),
  (380, "christian", "Christianity became the religion of the Pentapolis by the late 4th century, when Synesius of Cyrene was bishop."),
  (750, "sunni", "After the Arab conquest of 643 the Berber tribes gradually converted to Islam."),
  (909, "ismaili", "The Ismaili Fatimids ruled Cyrenaica from 909, a ruling faith over a mostly Sunni people."),
  (1051, "sunni", "Fatimid control ended in the mid 11th century as the Banu Sulaym Arabs settled; Maliki Sunni Islam prevailed, later revived by the Senussi order (1843)."))

z("tripolitania", "Tripolitania (western Libya)", 13.2, 32.6,
  (-10000, "folk", "Libyan Berber tribes worshipped local gods."),
  (-700, "mesopotamian", "Phoenician and Carthaginian cities such as Oea, Sabratha and Leptis worshipped Baal Hammon and Tanit."),
  (-46, "hellenic", "Rome annexed the region, and Leptis Magna, birthplace of Emperor Septimius Severus, built great Roman temples."),
  (380, "christian", "Christianity became dominant in the cities of Tripolitania by the late 4th century."),
  (455, "arian", "The Arian Vandals ruled Tripolitania from about 455, a ruling faith over a Nicene Christian population."),
  (533, "christian", "Belisarius reconquered the region for Byzantium in 533 and restored Nicene Christianity."),
  (750, "ibadi", "After the Arab conquest the Berbers of Tripolitania and Jabal Nafusa embraced Ibadi Islam, briefly ruling under the imam Abu al-Khattab in 757."),
  (909, "ismaili", "The Ismaili Fatimids ruled Tripolitania from 909, a ruling faith over Ibadi and Sunni Muslims."),
  (1048, "sunni", "The Zirids broke with the Fatimids in 1048 and Banu Hilal Arabs arrived soon after; Maliki Sunni Islam became dominant, though Jabal Nafusa remains Ibadi."))

z("fezzan", "Fezzan (southern Libya)", 14.4, 26.5,
  (-10000, "folk", "Saharan peoples, later the Garamantes of Germa, worshipped local gods."),
  (700, "sunni", "Arab raids from 666 brought Islam to the Fezzan oases."),
  (918, "ibadi", "The Ibadi Banu Khattab dynasty ruled the Fezzan from Zawila from about 918."),
  (1172, "sunni", "Qaraqush's conquest of Zawila in 1172 ended Ibadi rule, and Maliki Sunni Islam prevailed."))

# ------------------------------------------------------------------ MAGHREB
z("tunisia", "Tunisia (Carthage and Kairouan)", 10.1, 36.4,
  (-10000, "folk", "Berber peoples worshipped local gods."),
  (-814, "mesopotamian", "Phoenician Carthage, founded around 814 BC, worshipped Baal Hammon and Tanit."),
  (-146, "hellenic", "Rome destroyed Carthage in 146 BC and made Africa a province of Roman religion."),
  (330, "christian", "Roman Africa, home of Tertullian, Cyprian and later Augustine, became largely Christian by the 4th century."),
  (439, "arian", "The Arian Vandals took Carthage in 439 and persecuted the Nicene majority."),
  (533, "christian", "Belisarius reconquered Africa for Byzantium in 533 and restored Nicene Christianity."),
  (800, "sunni", "After the Arab conquest of Carthage (698), most people became Muslim, and under the Aghlabids (800) Kairouan was a centre of Maliki Sunni law."),
  (909, "ismaili", "The Ismaili Fatimid caliphate was proclaimed in Ifriqiya in 909, a ruling faith the Maliki townspeople resisted."),
  (1048, "sunni", "The Zirid emir al-Muizz broke with the Fatimids in 1048 and restored Sunni Islam."))

z("algeria-east", "Eastern Algeria (Constantine and Kabylia)", 6.6, 36.3,
  (-10000, "folk", "Berber peoples worshipped local gods."),
  (-200, "mesopotamian", "The Numidian kings at Cirta adopted the Carthaginian god Baal Hammon, as shown by the stelae of El Hofra."),
  (-46, "hellenic", "Rome annexed Numidia after Thapsus in 46 BC, spreading Roman religion."),
  (330, "christian", "Numidia was largely Christian by the 4th century and the heartland of the Donatist church."),
  (442, "arian", "The Arian Vandals ruled Numidia from 442, a ruling faith over a Nicene Christian population."),
  (534, "christian", "Byzantium reconquered Numidia in 534 and restored Nicene Christianity."),
  (750, "sunni", "After the defeat of the Berber queen Kahina around 700, the Berbers of the east converted to Islam over the 8th century."),
  (909, "ismaili", "The Kutama Berbers of Little Kabylia, converted by the missionary Abu Abdallah al-Shii, carried the Ismaili Fatimids to power in 909."),
  (1015, "sunni", "The Hammadid dynasty broke with the Fatimids in 1015 and Maliki Sunni Islam returned."))

z("algeria-central", "Central Algeria (Algiers)", 3.0, 36.5,
  (-10000, "folk", "Berber peoples worshipped local gods."),
  (-25, "hellenic", "Juba II, a Roman client king, ruled Mauretania from Caesarea (Cherchell), and Roman religion followed."),
  (380, "christian", "Mauretania Caesariensis had dozens of bishoprics and a largely Christian population by the late 4th century."),
  (750, "sunni", "After the Arab conquest the Berbers of the region converted to Islam in the 8th century; Maliki Sunni Islam prevailed."))

z("algeria-west", "Western Algeria (Tahert and Tlemcen)", 1.3, 35.4,
  (-10000, "folk", "Berber peoples worshipped local gods."),
  (400, "christian", "Christianity spread through the Roman towns and Berber kingdoms, such as Altava's Masuna, 'king of the Moors and Romans'."),
  (776, "ibadi", "The Persian Ibn Rustam founded the Ibadi imamate of Tahert in 776, which ruled western Algeria's Berbers as an Ibadi state."),
  (909, "sunni", "After the Fatimids destroyed Tahert in 909, the Zenata Berbers of the west, allied with Cordoba, turned to Maliki Sunni Islam."))

z("algeria-sahara", "Algerian Sahara (Ouargla and the Mzab)", 4.5, 31.5,
  (-10000, "folk", "Saharan Berber peoples worshipped local gods."),
  (800, "ibadi", "Ibadi missionaries tied to the imams of Tahert converted the oasis Berbers, and refugees from Tahert founded Sedrata near Ouargla after 909."),
  (1300, "sunni", "Maliki Sunni Islam spread among the oasis peoples, leaving Ibadis concentrated in the Mzab valley, where they remain."))

z("morocco-north", "Northern Morocco (Fes)", -5.0, 34.0,
  (-10000, "folk", "Berber peoples worshipped local gods; Roman Volubilis and Tingis were small islands of Roman religion."),
  (710, "sunni", "Musa ibn Nusayr's conquest brought the Berbers into Islam, and Idris I founded the Idrisid state at Fes in 789; Maliki Sunni Islam prevailed."))

z("morocco-south", "Southern Morocco (Marrakesh)", -8.0, 31.6,
  (-10000, "folk", "Masmuda and other Berber peoples worshipped local gods."),
  (800, "sunni", "The southern Berbers converted to Islam during the 8th and 9th centuries; the Almoravids founded Marrakesh in 1070 as a capital of Maliki Sunni Islam."))

z("western-sahara", "Western Sahara", -13.2, 27.1,
  (-10000, "folk", "Sanhaja Berber nomads worshipped local gods."),
  (1050, "sunni", "The Almoravid movement of Abdallah ibn Yasin made the Sanhaja nomads Maliki Sunni Muslims in the mid 11th century."))

z("mauritania", "Mauritania (coast and Adrar)", -15.8, 18.1,
  (-10000, "folk", "Berber and Soninke peoples worshipped local gods."),
  (1050, "sunni", "The Almoravid movement among the Sanhaja Berbers made the region Maliki Sunni Muslim in the mid 11th century."))

# ------------------------------------------------------------------ CENTRAL ASIA
z("kazakhstan-steppe", "Kazakh Steppe (Astana)", 71.4, 51.2,
  (-10000, "folk", "Early steppe peoples, later the Iranian Saka and Scythians, worshipped sky, fire and ancestors."),
  (552, "tengri", "The Gokturk Khaganate (552) and later Turkic peoples spread the worship of Tengri, the sky god, across the steppe."),
  (1500, "sunni", "The Kazakh Khanate (1465) was ruled by Muslim khans, and Sunni Islam spread among the nomads, blended with older steppe customs."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("kazakhstan-south", "Southern Kazakhstan (Turkestan and Otrar)", 68.3, 43.3,
  (-10000, "folk", "Early peoples of the Syr Darya worshipped local gods."),
  (552, "tengri", "The Western Turkic Khaganate ruled the Syr Darya, and its Turkic nomads worshipped Tengri."),
  (960, "sunni", "The Karakhanid Turks converted to Islam in 960, and Sufis such as Khoja Ahmed Yasawi of Turkestan spread it among the nomads."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("transoxiana", "Transoxiana (Samarkand and Bukhara)", 66.0, 39.7,
  (-10000, "folk", "Early peoples of the Zeravshan valley worshipped local gods."),
  (-600, "zoroastrianism", "The Sogdians practised their own form of Zoroastrianism, with fire temples and local gods; Buddhists, Christians and Manichaeans were minorities."),
  (875, "sunni", "After Qutayba's conquest (709 to 712), Transoxiana became majority Muslim under the Samanid emirs of Bukhara (875 to 999), a heartland of Sunni learning."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("khwarazm", "Khwarazm (Khiva)", 60.4, 41.4,
  (-10000, "folk", "Early peoples of the Amu Darya delta worshipped local gods."),
  (-600, "zoroastrianism", "Khwarazm, perhaps the Avestan homeland, followed Zoroastrianism, with its distinctive ossuary burials."),
  (900, "sunni", "After Qutayba's conquest of 712, Khwarazm became majority Muslim by about the 10th century, home of scholars such as al-Biruni."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("tashkent", "Tashkent (Chach)", 69.3, 41.3,
  (-10000, "folk", "Early peoples of the Chirchik valley worshipped local gods."),
  (-500, "zoroastrianism", "The Iranian people of Chach followed a Sogdian style Zoroastrianism."),
  (900, "sunni", "Under the Samanids Chach became majority Sunni Muslim by about the 10th century."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("fergana", "Fergana Valley", 71.8, 40.6,
  (-10000, "folk", "Early peoples of the Fergana valley worshipped local gods."),
  (-500, "zoroastrianism", "The Iranian farmers of Fergana, the Dayuan of Chinese records, followed a religion akin to Sogdian Zoroastrianism."),
  (900, "sunni", "Under the Samanids and then the Karakhanids, Fergana became majority Sunni Muslim by about the 10th century."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("turkmenistan", "Turkmenistan (Merv and Nisa)", 58.4, 37.9,
  (-10000, "folk", "Early farmers of the Kopet Dag foothills worshipped local gods."),
  (-600, "zoroastrianism", "Margiana and Parthia followed Zoroastrianism; the Parthian kings came from Nisa near Ashgabat."),
  (850, "sunni", "Merv became a base of the Arab conquest in 651 and was majority Muslim by the 9th century; Oghuz Turkmen tribes later brought Sunni Islam to the whole region."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("kyrgyzstan", "Kyrgyzstan (Chuy valley)", 74.6, 42.8,
  (-10000, "folk", "Saka nomads of the Tian Shan worshipped sky, sun and ancestors."),
  (552, "tengri", "The Turkic khaganates ruled from Suyab in the Chuy valley, and their nomads worshipped Tengri."),
  (960, "sunni", "The Karakhanids, ruling from Balasagun, converted to Islam in 960."),
  (1220, "tengri", "The Qara Khitai and then the Mongol conquest returned the valley to nomadic rulers who kept steppe religion."),
  (1600, "sunni", "The Kyrgyz tribes gradually adopted Sunni Islam from the 16th century, completed under the Kokand Khanate in the 18th and 19th centuries."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("tajikistan", "Tajikistan (Hisor and Khatlon)", 68.8, 38.5,
  (-10000, "folk", "Early peoples of the Hisor valley worshipped local gods."),
  (-600, "zoroastrianism", "The Iranian peoples of Bactria and Sogdia followed Zoroastrianism; Buddhist monasteries such as Ajina Tepe served a minority."),
  (900, "sunni", "Under the Samanids the region became majority Sunni Muslim by about the 10th century."),
  SOVIET,
  (1991, "sunni", SOVIET_END))

z("pamir", "Pamirs (Badakhshan)", 71.6, 37.5,
  (-10000, "folk", "The Iranian mountain peoples of the Pamirs worshipped local gods and sacred fires."),
  (1070, "ismaili", "The poet and missionary Nasir Khusraw preached Ismaili Islam in Badakhshan in the 11th century, and the Pamiris became Ismailis, followers of the Aga Khan."),
  (1928, "secular", "Soviet rule imposed state atheism and closed the region's prayer houses."),
  (1991, "ismaili", "After independence the Pamiris openly returned to Ismaili Islam, supported by the Aga Khan's institutions."))

z("kabul", "Kabul and the Kabul valley", 69.2, 34.5,
  (-10000, "folk", "Early peoples of the Kabul valley worshipped local gods."),
  (-1500, "vedic", "The Kabul river, the Kubha of the Rigveda, was home to Indo-Aryans who followed Vedic religion."),
  (-250, "buddhism", "Ashoka's missions and then Indo-Greek and Kushan patrons made the valley a Buddhist land, with great stupas at Hadda and Kapisa."),
  (850, "hinduism", "The brahmin Hindu Shahi dynasty displaced the Buddhist Turk Shahis around 850, and Shaivism gained ground in the Kabul valley."),
  (980, "sunni", "Sabuktigin of Ghazni drove the Hindu Shahis from the Kabul valley in the 980s, and the region became Sunni Muslim under the Ghaznavids."))

z("herat", "Herat (Aria)", 62.2, 34.3,
  (-10000, "folk", "Early peoples of the Hari river valley worshipped local gods."),
  (-600, "zoroastrianism", "Aria was a Zoroastrian province of the Achaemenid, Parthian and Sasanian empires."),
  (850, "sunni", "After the Arab conquest of 652, Herat became majority Sunni Muslim by the 9th century and later the Timurid capital of learning."))

z("balkh", "Balkh (Bactria)", 66.9, 36.7,
  (-10000, "folk", "Early peoples of Bactria worshipped local gods."),
  (-600, "zoroastrianism", "Bactria, where tradition says Zoroaster preached and died, followed Zoroastrianism under the Achaemenids."),
  (50, "buddhism", "Under Kushan patronage Buddhism became the leading faith of Bactria alongside Iranian cults; Xuanzang found about 100 monasteries at Balkh in 630."),
  (800, "sunni", "After the Arab conquest the Barmakid priests of Balkh's Nava Vihara converted to Islam, and Bactria was majority Sunni Muslim by the 9th century."))

z("hazarajat", "Hazarajat (Bamiyan)", 67.8, 34.8,
  (-10000, "folk", "Early mountain peoples of central Afghanistan worshipped local gods."),
  (100, "buddhism", "Bamiyan was a Buddhist kingdom, carving its colossal Buddhas in the 6th century."),
  (1000, "sunni", "Saffarid and Ghaznavid conquests made the region Sunni Muslim by the 11th century."),
  (1600, "shia", "The Hazaras adopted Twelver Shia Islam, probably under Safavid influence in the 16th and 17th centuries."))

z("kandahar", "Kandahar (Arachosia)", 65.7, 31.6,
  (-10000, "folk", "Early peoples of the Helmand and Arghandab valleys worshipped local gods."),
  (-600, "zoroastrianism", "Arachosia, the Avestan Harahvaiti, followed Iranian religion under the Achaemenids; Ashoka later set up Greek and Aramaic edicts here."),
  (1000, "sunni", "After the Saffarids overthrew the Zunbil kings in 870, Islam spread among the Pashtun tribes under Ghaznavid rule (977 to 1186)."))

json.dump(Z, open(os.path.join(H, "zones_mideast.json"), "w"), indent=1, ensure_ascii=False)
print(len(Z), "zones written")

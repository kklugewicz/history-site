"""Generate zones_asia.json: South, East and Southeast Asia and Oceania."""
import json, os

Z = []
def z(id, name, lon, lat, *hist):
    Z.append({"id": id, "name": name, "lon": lon, "lat": lat,
              "history": [{"from": f, "faith": r, "note": n} for f, r, n in hist]})

HARAPPA = "The Harappan cities of the Indus valley worshipped mother goddesses, sacred animals and possibly a horned proto-Shiva, alongside older village spirits."

# ---------------- PAKISTAN AND THE NORTHWEST ----------------
z("punjab-pakistan", "West Punjab (Lahore)", 74.35, 31.55,
  (-10000, "folk", HARAPPA),
  (-1500, "vedic", "Indo-Aryan tribes settled the land of the five rivers, where the hymns of the Rigveda were composed."),
  (-260, "buddhism", "Under the Maurya emperor Ashoka and later the Kushans, Buddhist monasteries flourished across the Punjab."),
  (500, "hinduism", "Gupta influence and the Huna king Mihirakula's persecution of Buddhists left Shaiva and Vaishnava Hinduism dominant."),
  (1300, "sunni", "Ruled by Muslims since Mahmud of Ghazni took Lahore in 1021, western Punjab turned to Islam through Sufi shrines, and Muslims stayed the majority even under Ranjit Singh's Sikh Empire from 1799 to 1849."))

z("punjab-india", "East Punjab (Amritsar and Ludhiana)", 75.6, 31.0,
  (-10000, "folk", HARAPPA),
  (-1500, "vedic", "Indo-Aryan tribes settled the Punjab, where the Rigveda's hymns to Indra, Agni and Soma were composed."),
  (-260, "buddhism", "Ashoka's Maurya empire and later the Kushans spread Buddhist monasteries through the Punjab."),
  (500, "hinduism", "From the Gupta age Hindu worship of Shiva and Vishnu prevailed, and it stayed the faith of most villagers through centuries of Muslim rule."),
  (1966, "sikhism", "Guru Nanak's faith, born here around 1500, became the majority after Partition in 1947 drove Muslims west and the 1966 split of Hindi-speaking Haryana left a Sikh-majority Punjab state."))

z("gandhara", "Gandhara and Peshawar", 71.55, 34.0,
  (-10000, "folk", "The hill and valley peoples of the Peshawar basin honoured local spirits and ancestors."),
  (-1500, "vedic", "Gandhara appears in the Rigveda as a land of Indo-Aryan tribes performing Vedic fire sacrifices."),
  (-260, "buddhism", "Ashoka sent missionaries to Gandhara, and Taxila and Peshawar became great centres of Buddhist learning."),
  (127, "mahayana", "The Kushan emperor Kanishka built the great Peshawar stupa, and Gandharan monks and sculptors helped shape Mahayana Buddhism and the Buddha image."),
  (822, "hinduism", "The Hindu Shahi dynasty replaced the Buddhist Turk Shahis, and Shaiva Hinduism became the ruling faith of the region."),
  (1001, "sunni", "Mahmud of Ghazni defeated the Hindu Shahi king Jayapala near Peshawar, and the Pashtun and other peoples of the region became Sunni Muslims."))

z("multan", "Multan", 71.47, 30.2,
  (-10000, "folk", HARAPPA),
  (-1500, "vedic", "Indo-Aryan settlers brought Vedic sacrifice to the middle Indus."),
  (-300, "hinduism", "Multan grew around its famous temple of the sun god Surya, a pilgrimage centre for all of northern India."),
  (712, "sunni", "Muhammad bin Qasim's Umayyad army took Multan, which became a Muslim-ruled city though its sun temple still drew Hindu pilgrims."),
  (959, "ismaili", "Ismaili missionaries won over Multan's rulers, who recognised the Fatimid caliphs in Cairo and destroyed the sun temple's idol; this was the ruling faith rather than the people's."),
  (1010, "sunni", "Mahmud of Ghazni crushed the Ismaili state, and Suhrawardi Sufi saints such as Bahauddin Zakariya later made Multan a Sunni stronghold."))

z("sindh", "Sindh", 68.37, 25.4,
  (-10000, "folk", "Mohenjo-daro and the Harappan towns of Sindh worshipped mother goddesses and sacred animals, with ritual bathing in the Great Bath."),
  (-1200, "vedic", "Indo-Aryan peoples named the river Sindhu and brought Vedic rites to its lower valley."),
  (-260, "buddhism", "Buddhism spread under Ashoka, and the Chinese pilgrim Xuanzang still found hundreds of Buddhist monasteries in Sindh around 640."),
  (632, "hinduism", "The Brahmin minister Chach seized the throne from the Buddhist Rai dynasty, and Brahmanical Hinduism became the ruling faith."),
  (712, "sunni", "Muhammad bin Qasim conquered Sindh for the Umayyad caliphate; conversion of its people to Sunni Islam took several centuries, aided by Sufi saints like Lal Shahbaz Qalandar."))

z("balochistan", "Balochistan", 67.0, 30.18,
  (-10000, "folk", "Farming villages like Mehrgarh, among the oldest in South Asia, and later pastoral tribes worshipped local gods and ancestors."),
  (900, "sunni", "Arabs conquered Makran from 644, and Sunni Islam spread as Baloch tribes moved east from Iran into the region between the 10th and 14th centuries."))

z("kashmir", "Kashmir Valley", 74.8, 34.08,
  (-10000, "folk", "Early Kashmiris revered the Naga serpent spirits of the valley's springs and lakes."),
  (-1000, "vedic", "Brahmin settlers brought Vedic ritual to the valley."),
  (-250, "buddhism", "Ashoka founded Srinagar's first monasteries, and the Kushan king Kanishka is said to have held the Fourth Buddhist Council in Kashmir."),
  (600, "hinduism", "Under the Karkota and Utpala kings Kashmir became a centre of Hindu learning, home of Kashmir Shaivism and the Martand sun temple."),
  (1400, "sunni", "After Shah Mir founded a sultanate in 1339, the Sufi Mir Sayyid Ali Hamadani and Sultan Sikandar's reign (1389 to 1413) turned most Kashmiris to Islam."))

z("ladakh", "Ladakh", 77.58, 34.16,
  (-10000, "folk", "Dard and Tibetan herders of Ladakh followed Bon-like spirit cults of mountains and passes."),
  (950, "vajrayana", "After Tibet's empire collapsed a Tibetan dynasty founded the kingdom of Ladakh, and monks like Rinchen Zangpo built monasteries such as Alchi."))

z("baltistan", "Gilgit-Baltistan", 75.63, 35.3,
  (-10000, "folk", "The mountain peoples of Baltistan and Gilgit worshipped spirits of peaks and springs."),
  (750, "vajrayana", "Tibet's empire conquered Baltistan in the 730s, and the Balti people became Tibetan Buddhists."),
  (1500, "shia", "The Kashmiri Sufi Mir Shamsuddin Iraqi converted the Balti people to Noorbakhshi Islam, which later gave way largely to Twelver Shia Islam, while Hunza became Ismaili."))

# ---------------- NORTH AND CENTRAL INDIA ----------------
z("delhi", "Delhi and the Upper Doab", 77.2, 28.62,
  (-10000, "folk", "Farmers of the upper Ganges and Yamuna worshipped village gods and fertility spirits."),
  (-1200, "vedic", "The Kuru kingdom around Delhi became the heartland of Vedic religion, where the great Vedic rituals and texts were codified."),
  (-500, "hinduism", "Vedic religion grew into Hinduism, with the epics placing the Pandavas' city of Indraprastha here."),
  (1206, "sunni", "The Delhi Sultanate and later the Mughals made Delhi the capital of Muslim India; this was the ruling faith, while most people of the surrounding countryside stayed Hindu."),
  (1857, "hinduism", "After the British deposed the last Mughal emperor in 1857, Delhi's Hindu majority came to the fore, reinforced by Hindu and Sikh refugees at Partition in 1947."))

z("varanasi", "Awadh and Varanasi", 82.5, 26.0,
  (-10000, "folk", "Villagers of the middle Ganges worshipped mother goddesses, snake spirits and tree spirits."),
  (-1000, "vedic", "The kingdoms of Kosala and Kashi adopted Vedic sacrifice led by Brahmin priests."),
  (-500, "hinduism", "Although the Buddha preached his first sermon at nearby Sarnath, Kashi (Varanasi) grew into Hinduism's holiest city, and Ayodhya into the city of Rama."))

z("bihar", "Bihar (Magadha)", 85.14, 25.6,
  (-10000, "folk", "Early farmers of the eastern Ganges plain worshipped local spirits and mother goddesses."),
  (-1100, "vedic", "Vedic culture reached Videha and Magadha, where Brahmin priests held sway."),
  (-260, "buddhism", "Magadha, where the Buddha and Mahavira had taught, became the core of Ashoka's Buddhist empire after his conversion."),
  (320, "hinduism", "The Gupta emperors, ruling from Pataliputra, championed Vishnu and Shiva, though Nalanda grew into Buddhism's greatest university."),
  (750, "vajrayana", "The Pala kings patronised tantric Buddhism at Nalanda and Vikramashila, sending teachers like Atisha to Tibet; this was the ruling faith, beside a largely Hindu population."),
  (1200, "hinduism", "Bakhtiyar Khalji's raiders sacked Nalanda and Vikramashila around 1200, and Buddhism vanished from Bihar, leaving Hinduism as the people's faith."))

z("west-bengal", "West Bengal", 88.36, 22.57,
  (-10000, "folk", "The peoples of the Bengal delta worshipped river, tree and serpent deities such as Manasa."),
  (-260, "buddhism", "Mauryan rule carried Buddhism into Bengal, where ports like Tamralipti linked it to Sri Lanka and Southeast Asia."),
  (350, "hinduism", "Gupta rule brought Brahmin settlers and Hindu temple worship to Bengal."),
  (750, "vajrayana", "The Pala dynasty made Bengal the last great stronghold of Buddhism, patronising tantric monasteries; this was the ruling faith while many subjects worshipped Hindu gods."),
  (1161, "hinduism", "The Sena kings restored orthodox Hinduism, and Bengal's Hindus kept their faith through Muslim rule, with Kali and Durga worship and Chaitanya's Vaishnavism."))

z("bangladesh", "Bangladesh (East Bengal)", 90.4, 23.8,
  (-10000, "folk", "The rice farmers and fishers of the eastern delta worshipped river, snake and village deities."),
  (-260, "buddhism", "A Mauryan inscription at Mahasthangarh shows Buddhist imperial rule in northern Bengal."),
  (350, "hinduism", "Gupta rule and Brahmin settlement spread Hindu worship into the delta."),
  (750, "vajrayana", "The Pala and Chandra kings were patrons of tantric Buddhism, building monasteries like Somapura; it was the court faith beside Hindu cults."),
  (1161, "hinduism", "The Sena dynasty revived orthodox Hinduism across Bengal before Bakhtiyar Khalji's Muslim conquest in 1204."),
  (1600, "sunni", "Under Mughal rule from 1576, Sufi-led clearing and settlement of the eastern delta's forests made Muslims the majority of East Bengal's peasants."))

z("assam", "Assam (Kamarupa)", 91.74, 26.14,
  (-10000, "folk", "Tibeto-Burman and Austroasiatic peoples of the Brahmaputra valley practised animist and ancestor religions."),
  (350, "hinduism", "The Varman kings of Kamarupa adopted Hinduism, and the Kamakhya goddess temple became a great centre of Shakta worship."))

z("ahom", "Upper Assam (Ahom)", 94.64, 26.98,
  (-10000, "folk", "The hill and valley peoples of Upper Assam followed animist religions, and the Tai Ahom who arrived in 1228 kept their own ancestral gods."),
  (1550, "hinduism", "Sankardeva's devotional Vaishnavism won over much of Upper Assam, and the Ahom kings themselves gradually embraced Hinduism."))

z("nagaland-mizoram", "Naga and Mizo Hills", 94.11, 25.67,
  (-10000, "folk", "The Naga, Mizo and Kuki peoples practised animist religions centred on village spirits, feasts of merit and headhunting rites."),
  (1950, "protestant", "American Baptist and Welsh missionaries converted the Naga and Mizo peoples, making Nagaland strongly Baptist and Mizoram mainly Presbyterian by the mid 20th century."))

z("manipur", "Manipur", 93.94, 24.81,
  (-10000, "folk", "The Meitei people worshipped the Sanamahi gods and household ancestors in the Manipur valley."),
  (1717, "hinduism", "King Pamheiba (Garib Niwaz) adopted Gaudiya Vaishnavism and made it the state religion of the Meitei kingdom."))

z("odisha", "Odisha (Kalinga)", 85.82, 20.3,
  (-10000, "folk", "Tribal peoples of Kalinga worshipped forest, earth and village goddesses."),
  (-261, "buddhism", "Ashoka's bloody conquest of Kalinga led to his remorse and embrace of Buddhism, which spread across the region."),
  (-150, "jainism", "King Kharavela of Kalinga, a devout Jain, carved the Udayagiri caves for Jain monks; Jainism was the royal faith."),
  (400, "hinduism", "Hindu dynasties rose, building temples such as the Lingaraja at Bhubaneswar and the Jagannath temple at Puri."))

z("malwa", "Malwa and Central India", 77.4, 23.26,
  (-10000, "folk", "Forest and farming peoples of central India worshipped local gods and spirits."),
  (-800, "vedic", "The kingdom of Avanti around Ujjain took up Vedic religion."),
  (-260, "buddhism", "Ashoka, once viceroy at Ujjain, endowed the great stupa at Sanchi, and Buddhism flourished in Malwa."),
  (320, "hinduism", "Gupta rule, centred in part on Ujjain, made Hinduism dominant, and the Paramara kings later built great Shiva temples."))

z("rajasthan", "Rajasthan", 75.79, 26.91,
  (-10000, "folk", "Herders and farmers of the Thar fringe worshipped local gods and ancestors."),
  (-1200, "vedic", "The Matsya kingdom and other Vedic peoples settled northeast Rajasthan."),
  (-400, "hinduism", "Hinduism prevailed, later championed by Rajput kings, while Jain merchants built temples such as those at Mount Abu."))

z("gujarat", "Gujarat", 72.57, 23.02,
  (-10000, "folk", "Harappan ports such as Lothal and Dholavira worshipped fire altars, mother goddesses and sacred animals."),
  (-1000, "vedic", "Vedic culture spread to Saurashtra and the Gujarat plains."),
  (-300, "hinduism", "Hinduism became the main faith, with the Somnath temple and Krishna's Dwarka as great shrines, beside a strong Jain merchant community."),
  (1160, "jainism", "The Solanki king Kumarapala, guided by the monk Hemachandra, made Jainism the court faith and banned animal slaughter."),
  (1173, "hinduism", "After Kumarapala's death Hindu royal patronage returned, and Hindus stayed the majority under the Gujarat Sultanate and the Mughals."))

# ---------------- DECCAN AND SOUTH INDIA ----------------
z("maharashtra", "Maharashtra (Deccan)", 73.86, 18.52,
  (-10000, "folk", "Deccan farmers and herders worshipped mother goddesses and local deities such as Khandoba's forerunners."),
  (-700, "vedic", "Vedic Brahmins and their rites spread south across the Vindhyas into the Deccan."),
  (-200, "hinduism", "The Satavahana kings performed Vedic sacrifices while merchants funded Buddhist caves at Karla and Ajanta, and later Rashtrakuta kings carved Ellora's Kailasa temple."))

z("andhra", "Andhra and Telangana", 79.0, 17.0,
  (-10000, "folk", "Megalith-building peoples of the eastern Deccan honoured their ancestors and local spirits."),
  (-250, "buddhism", "Ashoka's missionaries reached Andhra, and the great stupa of Amaravati was begun."),
  (150, "mahayana", "Under the Satavahanas and Ikshvakus, Amaravati and Nagarjunakonda became great Buddhist centres, linked to the Mahayana philosopher Nagarjuna."),
  (400, "hinduism", "The Vishnukundin and Pallava kings revived Brahmanical Hinduism, and Buddhism faded; Hindus stayed the majority even under the Muslim Qutb Shahis and Nizams."))

z("goa", "Goa", 73.83, 15.49,
  (-10000, "folk", "Konkan villagers worshipped earth and village goddesses."),
  (-200, "hinduism", "Hinduism spread along the Konkan coast, and the Kadamba kings built temples in Goa."),
  (1560, "catholic", "Portugal conquered Goa in 1510, and with the Inquisition from 1560 forced and mass conversions made the Old Conquests overwhelmingly Catholic."),
  (1900, "hinduism", "The mainly Hindu New Conquests, added in 1763 to 1788, and Catholic emigration made Hindus the majority of Goa again by the early 20th century."))

z("karnataka", "Karnataka", 76.0, 13.21,
  (-10000, "folk", "Early peoples of the southern Deccan honoured ancestors with megaliths and worshipped village deities."),
  (-200, "hinduism", "Brahmin settlers and the Satavahana and Kadamba kings spread Hindu worship."),
  (350, "jainism", "The Western Ganga kings and later the Rashtrakutas were great patrons of Jainism, building Shravanabelagola's giant Gommateshwara statue; Jainism was the leading court faith."),
  (1116, "hinduism", "The Hoysala king Vishnuvardhana turned from Jainism to Vaishnavism under Ramanuja, Basava founded the Lingayats, and the Vijayanagara empire later made the south a Hindu bastion."))

z("tamil-nadu", "Tamil Nadu", 79.14, 10.79,
  (-10000, "folk", "Early Tamils worshipped Murugan, Korravai and hero stones for fallen warriors."),
  (-300, "hinduism", "Sangam-age kings of the Chera, Chola and Pandya lines patronised Vedic sacrifice alongside Tamil gods."),
  (300, "jainism", "Under the Kalabhra rulers Jain and Buddhist monks gained royal favour and shaped Tamil literature; this was the court faith of the age."),
  (600, "hinduism", "The bhakti hymns of the Shaiva Nayanars and Vaishnava Alvars won back kings like the Pallava Mahendravarman I, and the Cholas raised great temples like Thanjavur's."))

z("kerala", "Kerala", 76.3, 9.95,
  (-10000, "folk", "The Chera country of the Sangam age worshipped Dravidian gods, ancestors and serpent spirits."),
  (800, "hinduism", "Brahmin settlement under the Chera Perumals made Hinduism dominant, while Thomas Christians of the Syriac church and Mappila Muslims grew into large minorities."))

z("sri-lanka", "Sri Lanka", 80.63, 7.29,
  (-10000, "folk", "The Vedda and early Sinhalese worshipped yakkha and naga spirits."),
  (-247, "theravada", "Ashoka's son Mahinda converted King Devanampiya Tissa of Anuradhapura, and the island became the lasting heartland of Theravada Buddhism."))

z("jaffna", "Jaffna (Northern Sri Lanka)", 80.01, 9.66,
  (-10000, "folk", "The early people of northern Lanka worshipped naga serpent spirits."),
  (-200, "theravada", "Buddhism spread to the north from Anuradhapura, and Buddhist sites stood in the Jaffna peninsula."),
  (1215, "hinduism", "After Kalinga Magha's invasion and the rise of the Tamil Jaffna kingdom, Shaiva Hinduism became the faith of the north."))

# ---------------- HIMALAYA AND TIBET ----------------
z("nepal", "Nepal", 85.32, 27.7,
  (-10000, "folk", "The Kirata and other hill peoples worshipped ancestral and nature spirits."),
  (-250, "buddhism", "Ashoka honoured the Buddha's birthplace at Lumbini, and Buddhism spread to the Kathmandu valley."),
  (400, "hinduism", "The Licchavi kings made Hinduism the royal faith while supporting Newar Buddhism, and Nepal later became the world's only Hindu kingdom."))

z("bhutan", "Bhutan", 89.64, 27.47,
  (-10000, "folk", "The peoples of the Bhutanese valleys followed Bon and local mountain deities."),
  (750, "vajrayana", "Padmasambhava's 8th century visit began Bhutan's conversion, and in 1616 Zhabdrung Ngawang Namgyal unified it as a Drukpa Kagyu Buddhist state."))

z("tibet", "Central Tibet", 91.11, 29.65,
  (-10000, "folk", "Tibetans followed Bon, with priests serving the sky-descended kings and mountain gods."),
  (779, "vajrayana", "King Trisong Detsen founded Samye monastery with Padmasambhava and Shantarakshita and made Buddhism the state religion."),
  (842, "folk", "Langdarma's persecution of monks and the collapse of the Tibetan empire ended royal Buddhism for over a century."),
  (978, "vajrayana", "Monks returning from Amdo and teachers like Atisha began the later spread of Buddhism, and the Dalai Lamas ruled Tibet from 1642."))

z("amdo", "Amdo (Qinghai)", 100.62, 36.28,
  (-10000, "folk", "Qiang and Xianbei herders around Lake Kokonor, including the Tuyuhun kingdom, followed shamanic and mountain cults."),
  (900, "vajrayana", "Monks fleeing Langdarma's persecution kept Buddhism alive in Amdo, which later gave birth to Tsongkhapa and great monasteries such as Kumbum and Labrang."))

z("kham", "Kham (Eastern Tibet)", 97.17, 31.14,
  (-10000, "folk", "The clans of Kham followed Bon and the worship of mountain deities."),
  (1100, "vajrayana", "Monasteries spread across Kham in the later diffusion of Buddhism, and the first Karmapa founded Karma Gon here in 1147."))

# ---------------- XINJIANG AND MONGOLIA ----------------
z("kashgar", "Kashgar (Western Tarim)", 75.99, 39.47,
  (-10000, "folk", "Saka and other Iranian-speaking oasis dwellers worshipped local and Iranian gods."),
  (100, "buddhism", "Buddhism came over the Pamirs from Kushan Gandhara, and Kashgar's monasteries followed the Sarvastivada school."),
  (934, "sunni", "Satuq Bughra Khan of the Kara-Khanids converted to Islam, making Kashgar the first Turkic Muslim realm and the base for the conquest of the Tarim."))

z("khotan", "Khotan", 79.92, 37.11,
  (-10000, "folk", "Saka settlers of the southern Tarim oasis worshipped Iranian and local gods."),
  (-50, "buddhism", "Buddhism reached Khotan from Kashmir and Gandhara, according to tradition through the monk Vairocana."),
  (300, "mahayana", "Khotan became a great centre of Mahayana Buddhism, sending sutras and teachers to China."),
  (1006, "sunni", "The Kara-Khanids conquered Khotan after a long holy war, and its people became Sunni Muslims."))

z("kucha", "Kucha (Northern Tarim)", 82.96, 41.72,
  (-10000, "folk", "The Tocharian-speaking people of Kucha worshipped local gods."),
  (100, "buddhism", "Kucha became a Buddhist kingdom of Sarvastivada monks and painted caves like Kizil, birthplace of the translator Kumarajiva."),
  (1390, "sunni", "The Chagatai Muslim khans of Moghulistan forcibly converted Kucha and its neighbours to Islam."))

z("turfan", "Turfan (Gaochang and Qocho)", 89.19, 42.95,
  (-10000, "folk", "The Jushi people of the Turfan oasis worshipped local gods."),
  (450, "mahayana", "The Han Chinese kingdom of Gaochang made Turfan a Mahayana Buddhist oasis, as was Tang Xizhou after 640."),
  (850, "manichaeism", "Uyghurs fleeing Mongolia founded the kingdom of Qocho, whose rulers kept their Manichaean state faith."),
  (1000, "mahayana", "Qocho's Uyghur rulers and people turned from Manichaeism to Buddhism, filling the Bezeklik caves with murals."),
  (1450, "sunni", "The Muslim khans of Moghulistan conquered Turfan, and the last Buddhist Uyghurs became Muslims by about 1500."))

z("dzungaria", "Dzungaria (Northern Xinjiang)", 87.62, 43.83,
  (-10000, "folk", "Early herders of the Dzungarian steppe worshipped nature spirits."),
  (-200, "tengri", "Xiongnu and later Turkic nomads brought the cult of the sky god Tengri and their shamans."),
  (850, "manichaeism", "The Uyghur kingdom of Qocho, with its summer capital at Beshbalik, kept the Manichaean faith of its rulers."),
  (1000, "mahayana", "The Uyghurs of Beshbalik and Qocho converted to Buddhism."),
  (1400, "tengri", "Oirat Mongol nomads took over the steppe and followed shamanism."),
  (1615, "vajrayana", "The Oirat nobles adopted Gelug Buddhism, and the Dzungar Khanate became a Tibetan Buddhist power."),
  (1760, "chinese", "The Qing destroyed the Dzungars and resettled the land with Han Chinese, Hui and others."),
  (1949, "secular", "Communist rule suppressed religion, and most of the Han majority of northern Xinjiang profess none."))

z("mongolia", "Mongolia", 106.92, 47.92,
  (-10000, "folk", "Early peoples of the Mongolian steppe raised deer stones and honoured nature spirits."),
  (-209, "tengri", "The Xiongnu empire and its Turkic and Mongol successors worshipped Tengri, the eternal blue sky, through shamans."),
  (762, "manichaeism", "Bogu Qaghan of the Uyghur khaganate adopted Manichaeism as the state faith of his steppe empire."),
  (840, "tengri", "The Kyrgyz destroyed the Uyghur khaganate, and the steppe returned to Tengri worship, the faith of Chinggis Khan."),
  (1578, "vajrayana", "Altan Khan met the Gelug lama Sonam Gyatso, gave him the title Dalai Lama, and Mongols converted en masse to Tibetan Buddhism."),
  (1937, "secular", "Communist purges destroyed over 700 monasteries and killed or laicised the lamas, enforcing state atheism."),
  (1990, "vajrayana", "The democratic revolution restored religious freedom, and today just over half of Mongolians call themselves Buddhist."))

z("inner-mongolia", "Inner Mongolia", 111.75, 40.84,
  (-10000, "folk", "Early peoples of the southern steppe honoured nature spirits and ancestors."),
  (-300, "tengri", "The Xiongnu, Xianbei and later Turkic and Mongol nomads worshipped Tengri through shamans."),
  (916, "mahayana", "The Khitan Liao dynasty patronised Buddhism across the southern steppe, building pagodas and printing a Buddhist canon."),
  (1206, "tengri", "Chinggis Khan unified the Mongols, who kept their shamanist faith in Tengri."),
  (1578, "vajrayana", "Altan Khan of the Tumed embraced Tibetan Buddhism and founded Hohhot around its great monastery."),
  (1912, "chinese", "Han Chinese settlement encouraged by the late Qing and the Republic made Han farmers the majority."),
  (1949, "secular", "The People's Republic suppressed religion, and most people of the region now follow none."))

# ---------------- CHINA ----------------
z("north-china-plain", "North China Plain (Henan)", 112.45, 34.62,
  (-10000, "folk", "Yangshao farmers, and later the Shang and Zhou kings, worshipped ancestors and the high god Di or Heaven through divination and sacrifice."),
  (-500, "chinese", "Confucius and the Taoist sages reshaped Zhou ancestor worship into China's lasting blend of Confucian ethics, Taoism and folk religion."),
  (400, "mahayana", "Buddhism became the dominant faith of north China under the Northern Wei, who moved their capital to Luoyang in 494 and carved the Longmen grottoes."),
  (845, "chinese", "Emperor Wuzong's Huichang persecution closed thousands of monasteries, and Neo-Confucianism and folk religion led thereafter, with Buddhism alongside."),
  (1949, "secular", "The Communist People's Republic suppressed religion, and most Chinese now say they follow none, though folk practice survives."))

z("guanzhong", "Guanzhong (Xi'an)", 108.94, 34.34,
  (-10000, "folk", "Neolithic farmers of the Wei valley worshipped ancestors and nature spirits."),
  (-500, "chinese", "The Wei valley, home of the Zhou, Qin and Han, became a heart of Confucian state ritual and Taoism."),
  (400, "mahayana", "Chang'an became the great Buddhist capital where Kumarajiva and Xuanzang translated sutras, beside Nestorian, Manichaean and Zoroastrian minorities."),
  (845, "chinese", "Emperor Wuzong's Huichang edict, issued from Chang'an, closed monasteries and foreign temples, and Buddhism never regained its dominance."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("hebei-beijing", "Hebei and Beijing", 116.4, 39.9,
  (-10000, "folk", "Neolithic peoples of the northern plain worshipped ancestors and nature."),
  (-500, "chinese", "The state of Yan and later Han China brought Confucian and Taoist practice to the north."),
  (400, "mahayana", "Buddhism dominated the north under the Northern Wei and its successors, and monasteries rose around Youzhou."),
  (845, "chinese", "The Huichang persecution broke the power of the Buddhist monasteries."),
  (938, "mahayana", "The Khitan Liao dynasty made Yanjing, today's Beijing, a Buddhist southern capital, as did the Jurchen Jin after them."),
  (1368, "chinese", "The Ming restored Confucian state ritual, building the Temple of Heaven, and folk religion led in daily life."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("shandong", "Shandong", 117.0, 35.6,
  (-10000, "folk", "Dawenkou and Longshan farmers worshipped ancestors, and Mount Tai was a sacred mountain."),
  (-500, "chinese", "Confucius taught in the state of Lu, making Qufu the birthplace of Confucianism."),
  (450, "mahayana", "Buddhism flourished in Shandong under the northern dynasties, with Buddha carvings at Qingzhou and on Mount Tai."),
  (845, "chinese", "After the Huichang persecution Confucianism and folk religion again led, with Qufu's Confucius temple at its heart."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("jiangnan", "Jiangnan (Lower Yangtze)", 118.8, 32.06,
  (-10000, "folk", "Liangzhu jade-makers and the later Wu and Yue peoples worshipped ancestors and animal spirits."),
  (-221, "chinese", "The Qin and Han unification brought Confucian and Taoist practice to the lower Yangtze."),
  (502, "mahayana", "Emperor Wu of Liang, ruling from Jiankang (Nanjing), made Buddhism the faith of the southern court and filled the city with hundreds of temples."),
  (845, "chinese", "The Huichang persecution ended Buddhist dominance, and Neo-Confucianism and folk religion led, beside Chan and Pure Land temples."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("middle-yangtze", "Hubei and Hunan (Chu)", 113.0, 29.5,
  (-10000, "folk", "Rice farmers of the middle Yangtze worshipped ancestors and river spirits, and the state of Chu kept vivid shamanic rites."),
  (-221, "chinese", "Qin and Han rule absorbed Chu into Chinese Confucian and Taoist practice."),
  (500, "mahayana", "Buddhism spread widely, and Chan Buddhism took shape at Huangmei and in Hunan."),
  (845, "chinese", "After the Huichang persecution Confucian and folk religion led again, beside Taoist Wudang and Buddhist temples."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("sichuan", "Sichuan (Shu)", 104.07, 30.67,
  (-10000, "folk", "The Sanxingdui and Jinsha cultures of Shu worshipped sun, bird and bronze-masked ancestor gods."),
  (-316, "chinese", "Qin conquered Shu, and in AD 142 Zhang Daoling founded the Way of the Celestial Masters here, the first organised Taoist church."),
  (600, "mahayana", "Buddhism flourished under the Sui and Tang, as the giant Buddha of Leshan, begun in 713, shows."),
  (845, "chinese", "After the Huichang persecution Taoism, Confucian ritual and folk religion led again."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("guangdong", "Guangdong (Lingnan)", 113.26, 23.13,
  (-10000, "folk", "The Baiyue peoples of the far south worshipped ancestors, snakes and sea spirits."),
  (-111, "chinese", "The Han dynasty conquered Nanyue, and Han settlers brought Confucian and Taoist practice to Lingnan."),
  (650, "mahayana", "Buddhism grew strong in the south, and the Guangdong-born sixth patriarch Huineng shaped Chan Buddhism."),
  (845, "chinese", "After the Huichang persecution ancestor worship, lineage halls and folk gods like Mazu dominated, beside Buddhism."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("guangxi", "Guangxi", 108.32, 22.82,
  (-10000, "folk", "The Zhuang and other Tai peoples worshipped ancestors, the frog goddess and village spirits."),
  (1053, "chinese", "After the Song crushed Nong Zhigao's Zhuang revolt, Han settlement spread Chinese ancestor and Taoist worship, which Zhuang religion absorbed."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("fujian", "Fujian", 119.3, 26.08,
  (-10000, "folk", "The Minyue people worshipped snakes, ancestors and sea spirits."),
  (-110, "chinese", "The Han dynasty conquered Minyue, and later waves of Han settlers made Fujian Chinese in culture and religion."),
  (909, "mahayana", "The Min kingdom and the Song made Fujian China's most Buddhist province, crowded with monasteries."),
  (1368, "chinese", "Under the Ming, lineage ancestor worship and folk gods such as the sea goddess Mazu led Fujianese religion."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("yunnan", "Yunnan (Nanzhao and Dali)", 100.23, 25.6,
  (-10000, "folk", "The Dian culture and the Bai and Yi peoples worshipped ancestors, bronze drums and nature spirits."),
  (800, "mahayana", "The Nanzhao kings and then the Dali kingdom adopted Buddhism, with tantric Azhali priests, making Dali a land of Buddhas."),
  (1382, "chinese", "The Ming conquered Yunnan and settled Han soldiers and farmers, spreading Chinese religion."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("dunhuang", "Hexi Corridor (Dunhuang)", 94.66, 40.14,
  (-10000, "folk", "Early herders of the Gansu corridor honoured local spirits."),
  (-200, "tengri", "The Xiongnu drove out the Yuezhi and brought the cult of Tengri."),
  (-111, "chinese", "Emperor Wu of Han took the Hexi corridor and founded Dunhuang as a Chinese garrison town."),
  (366, "mahayana", "The monk Lezun carved the first Mogao caves, and Dunhuang became a great Buddhist gateway on the Silk Road."),
  (786, "vajrayana", "The Tibetan empire ruled Dunhuang and spread Tibetan Buddhism."),
  (848, "mahayana", "Zhang Yichao's Return to Allegiance Army expelled the Tibetans, and Chinese Mahayana Buddhism led again."),
  (1036, "vajrayana", "The Tangut Western Xia took Dunhuang, and their Buddhism drew heavily on Tibetan tantra."),
  (1524, "sunni", "The Ming withdrew behind Jiayuguan, and Dunhuang fell to the Muslim khans of Turfan."),
  (1725, "chinese", "The Qing resettled Dunhuang with Han Chinese farmers."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("ningxia", "Ningxia (Western Xia)", 106.23, 38.49,
  (-10000, "folk", "Steppe and farming peoples of the Ordos loop honoured nature spirits."),
  (-214, "chinese", "Qin and Han armies took the Ordos loop and settled Chinese farmers along the Yellow River."),
  (450, "mahayana", "Buddhism spread along the frontier under the northern dynasties and the Tang."),
  (1038, "vajrayana", "The Tangut Western Xia made Buddhism their state religion, with Tibetan lamas as imperial preceptors."),
  (1227, "chinese", "The Mongols destroyed the Western Xia, and Han and Hui settlers later repopulated the land."),
  (1949, "secular", "Communist rule suppressed religion, and the Han majority now mostly profess none, beside a large Hui Muslim minority."))

z("liaodong", "Liaodong (Shenyang)", 123.43, 41.8,
  (-10000, "folk", "Early peoples of Liaodong worshipped ancestors and nature spirits."),
  (-300, "chinese", "The state of Yan and then the Han commanderies brought Chinese settlers and religion."),
  (404, "mahayana", "Buddhist Goguryeo and later the Liao and Jin dynasties ruled Liaodong, leaving pagodas across the region."),
  (1371, "chinese", "The Ming restored Chinese rule, and Han ancestor and folk religion led."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("manchuria", "Manchuria", 126.63, 45.75,
  (-10000, "folk", "The Sushen, Mohe and Jurchen forest peoples practised shamanism."),
  (698, "mahayana", "The kingdom of Balhae adopted Buddhism and Tang culture."),
  (926, "folk", "After the Khitans destroyed Balhae, the Jurchen tribes kept their shamanism, a faith the Qing Manchus preserved at court."),
  (1880, "chinese", "The Qing opened Manchuria to Han settlers, who became the great majority by 1900."),
  (1949, "secular", "Communist rule suppressed religion, and most people now profess none."))

z("taiwan", "Taiwan", 120.68, 24.15,
  (-10000, "folk", "Austronesian peoples of Taiwan worshipped ancestors and nature spirits."),
  (1662, "chinese", "Koxinga expelled the Dutch, whose Reformed missions had won some lowland villages, and Hokkien settlers made Chinese folk religion, Taoism and Buddhism dominant."))

# ---------------- KOREA AND JAPAN ----------------
z("north-korea", "North Korea", 125.75, 39.03,
  (-10000, "folk", "Koreans practised shamanism (Muism), with mudang shamans serving spirits of nature and ancestors."),
  (372, "mahayana", "King Sosurim of Goguryeo received Buddhism from Former Qin, and it later became the state religion of Goryeo."),
  (1392, "chinese", "The Joseon dynasty made Neo-Confucianism the state ideology and pushed Buddhist monasteries into the mountains."),
  (1948, "secular", "Kim Il Sung's communist state abolished organised religion in favour of the Juche ideology."))

z("south-korea", "South Korea", 126.98, 37.57,
  (-10000, "folk", "Koreans practised shamanism (Muism), with mudang shamans serving nature and ancestor spirits."),
  (384, "mahayana", "Baekje adopted Buddhism in 384, and it became the state religion under Goryeo (918 to 1392), which carved the Tripitaka Koreana."),
  (1392, "chinese", "The Joseon dynasty made Neo-Confucianism the state ideology, and ancestor rites became the core of Korean religion."),
  (2015, "secular", "The 2015 census found 56% of South Koreans with no religion; Protestants (20%), who grew fast after 1960, had just passed Buddhists (16%) as the largest faith."))

z("silla", "Gyeongsang (Silla)", 129.21, 35.86,
  (-10000, "folk", "The Silla people worshipped sky gods, ancestors and mountain spirits through shamans."),
  (527, "mahayana", "The martyrdom of the courtier Ichadon led King Beopheung to make Buddhism Silla's state religion, and Gyeongju gained Bulguksa temple."),
  (1392, "chinese", "Under Joseon, Neo-Confucian academies flourished in the southeast and ancestor rites became central."),
  (2015, "secular", "The 2015 census found most South Koreans with no religion, though Buddhism stays strongest in this region."))

z("japan-kansai", "Japan (Kansai)", 135.8, 34.69,
  (-10000, "folk", "The Jomon people worshipped nature spirits and fertility through clay figurines."),
  (300, "shinto", "The Yamato kings of the Kofun period built their power on worship of the kami and the sun goddess Amaterasu."),
  (594, "mahayana", "Empress Suiko and Prince Shotoku proclaimed Buddhism a state faith, and Nara and Kyoto became great Buddhist capitals, with kami and buddhas worshipped together."),
  (1868, "shinto", "The Meiji government separated Shinto from Buddhism and made State Shinto, centred on the emperor, the official national cult; most families kept Buddhist funerals."),
  (1945, "secular", "Defeat ended State Shinto, and most Japanese now say they have no religion, though they visit shrines and hold Buddhist funerals."))

z("japan-kanto", "Japan (Kanto)", 139.69, 35.69,
  (-10000, "folk", "The Jomon people worshipped nature spirits and fertility through clay figurines."),
  (400, "shinto", "Yamato rule brought worship of the kami, the sun goddess and clan ancestor gods to the eastern plains."),
  (750, "mahayana", "Emperor Shomu's provincial temples spread Buddhism east, and the Kamakura shoguns later fostered Zen and Pure Land."),
  (1868, "shinto", "The Meiji emperor moved to Tokyo and made State Shinto the official national cult; most families kept Buddhist funerals."),
  (1945, "secular", "Defeat ended State Shinto, and most Japanese now say they have no religion, though shrine and temple customs remain."))

z("tohoku", "Tohoku (Northern Honshu)", 140.87, 38.27,
  (-10000, "folk", "The Emishi of northern Honshu kept Jomon-rooted nature and ancestor religion."),
  (802, "mahayana", "Sakanoue no Tamuramaro subdued the Emishi, and the northern Fujiwara later built the golden Buddhist halls of Hiraizumi."),
  (1868, "shinto", "The Meiji government made State Shinto the official national cult."),
  (1945, "secular", "Defeat ended State Shinto, and most Japanese now say they have no religion."))

z("nagasaki", "Kyushu (Nagasaki)", 129.87, 32.75,
  (-10000, "folk", "The Jomon and Yayoi peoples of Kyushu worshipped nature spirits."),
  (300, "shinto", "Kyushu's chiefs worshipped kami tied to the Yamato court and its sun goddess."),
  (600, "mahayana", "Buddhism spread across Kyushu, intertwined with kami worship."),
  (1580, "catholic", "The Christian daimyo Omura Sumitada gave Nagasaki to the Jesuits, and much of western Kyushu became Catholic."),
  (1614, "mahayana", "The Tokugawa banned Christianity, crushed the Shimabara rising and forced every family to register at a Buddhist temple, while Hidden Christians worshipped in secret."),
  (1868, "shinto", "The Meiji government made State Shinto the official national cult."),
  (1945, "secular", "Defeat ended State Shinto, and most Japanese now say they have no religion."))

z("hokkaido", "Hokkaido (Ainu)", 141.35, 43.06,
  (-10000, "folk", "The Ainu worshipped kamuy, the spirits of bears, fire and the land, sending them home in the iomante bear ceremony."),
  (1869, "shinto", "The Meiji state annexed Hokkaido and settled it with Japanese farmers under State Shinto."),
  (1945, "secular", "Defeat ended State Shinto, and most people here now say they have no religion."))

# ---------------- MAINLAND SOUTHEAST ASIA ----------------
z("upper-burma", "Upper Burma (Pagan)", 95.5, 21.5,
  (-10000, "folk", "Burmese and Pyu villagers worshipped nat spirits of nature and ancestors."),
  (400, "theravada", "The Pyu city-states such as Sri Ksetra followed Pali Buddhism alongside Hindu cults."),
  (849, "mahayana", "Pagan, founded by the Bamar after the Pyu fell, was led by Ari monks practising tantric Mahayana Buddhism."),
  (1056, "theravada", "King Anawrahta, guided by the Mon monk Shin Arahan, made Theravada the faith of Pagan and its people."))

z("lower-burma", "Lower Burma (Mon)", 96.48, 17.34,
  (-10000, "folk", "The Mon worshipped nature spirits and ancestors."),
  (400, "theravada", "Mon kingdoms such as Thaton, the Suvannabhumi of tradition, received Theravada by sea from India and Sri Lanka."))

z("arakan", "Arakan (Rakhine)", 93.19, 20.59,
  (-10000, "folk", "The early peoples of the Arakan coast worshipped local spirits."),
  (350, "mahayana", "The Chandra kings of Vesali patronised Mahayana Buddhism alongside Hindu gods."),
  (1430, "theravada", "King Min Saw Mon founded Mrauk U, whose Buddhist kings, though using Muslim titles, made Theravada the faith of the Rakhine."))

z("northern-thailand", "Northern Thailand (Lan Na)", 98.98, 18.79,
  (-10000, "folk", "Lawa and other hill peoples worshipped phi spirits."),
  (750, "theravada", "Queen Chamadevi's Mon kingdom of Hariphunchai brought Theravada Buddhism, later the faith of Mangrai's Lan Na from 1292."))

z("sukhothai", "Sukhothai", 99.82, 17.01,
  (-10000, "folk", "Tai and Mon villagers worshipped phi spirits."),
  (1000, "hinduism", "Sukhothai was a Khmer outpost with Hindu and Mahayana shrines."),
  (1238, "theravada", "The Thai kingdom of Sukhothai threw off Khmer rule, and King Ramkhamhaeng invited Sri Lankan monks, making Theravada the Thai faith."))

z("central-thailand", "Central Thailand (Ayutthaya)", 100.57, 14.35,
  (-10000, "folk", "Early rice farmers of the Chao Phraya worshipped spirits and ancestors."),
  (600, "theravada", "The Mon kingdoms of Dvaravati adopted Theravada Buddhism, a faith Ayutthaya (1351) and Bangkok inherited."))

z("isan", "Isan (Khorat Plateau)", 102.1, 14.97,
  (-10000, "folk", "Bronze Age villagers of Ban Chiang honoured ancestors and spirits."),
  (600, "hinduism", "Chenla and the Khmer empire brought Shiva worship to the Khorat plateau."),
  (1100, "mahayana", "Phimai's great temple was dedicated to the Buddha, and Jayavarman VII spread Mahayana across the plateau."),
  (1300, "theravada", "Lao and Thai settlement and monks made Theravada the faith of the plateau."))

z("nakhon-si-thammarat", "Southern Thailand (Tambralinga)", 99.96, 8.43,
  (-10000, "folk", "Coastal peoples of the Malay peninsula worshipped spirits of land and sea."),
  (200, "hinduism", "Indian traders brought Hindu gods to the port kingdom of Tambralinga."),
  (775, "mahayana", "Srivijaya ruled the region and spread Mahayana Buddhism, as the Ligor inscription records."),
  (1200, "theravada", "Nakhon Si Thammarat became a centre of Sri Lankan Theravada, which it passed on to Sukhothai."))

z("patani", "Patani", 101.25, 6.87,
  (-10000, "folk", "Malay coastal peoples worshipped spirits of land and sea."),
  (100, "hinduism", "The kingdom of Langkasuka grew rich on Indian trade and Hindu and Buddhist worship."),
  (700, "mahayana", "Srivijaya's influence made Mahayana Buddhism the court faith."),
  (1470, "sunni", "The rulers of Patani accepted Islam, and the Malay sultanate became a centre of Islamic learning."))

z("angkor", "Angkor (Northern Cambodia)", 103.86, 13.36,
  (-10000, "folk", "Khmer villagers worshipped neak ta spirits of the land and ancestors."),
  (600, "hinduism", "Chenla and then Jayavarman II's Khmer empire of 802 worshipped Shiva and Vishnu as god-kings, building Angkor Wat for Vishnu."),
  (1181, "mahayana", "Jayavarman VII made Mahayana Buddhism the state faith and built the Bayon with its smiling faces."),
  (1243, "hinduism", "Jayavarman VIII restored Shaivism and defaced many Buddha images."),
  (1295, "theravada", "Under Indravarman III Theravada Buddhism spread from Thailand and Sri Lanka and became the faith of the Khmer people."),
  (1975, "secular", "The Khmer Rouge abolished religion, killing monks and destroying temples."),
  (1979, "theravada", "After the Khmer Rouge fell, Theravada Buddhism was restored, and it is the state religion today."))

z("cambodia", "Cambodia (Phnom Penh and Funan)", 104.92, 11.56,
  (-10000, "folk", "Khmer villagers worshipped neak ta spirits of the land and ancestors."),
  (100, "hinduism", "The trading kingdom of Funan adopted Hindu gods and Sanskrit kingship, led according to legend by the Brahmin Kaundinya."),
  (1181, "mahayana", "Jayavarman VII made Mahayana Buddhism the state faith of the Khmer empire."),
  (1243, "hinduism", "Jayavarman VIII restored Shaiva Hinduism as the court faith."),
  (1295, "theravada", "Theravada Buddhism became the faith of the Khmer people, and Phnom Penh became the capital in the 1430s."),
  (1975, "secular", "The Khmer Rouge abolished religion, killing monks and destroying temples."),
  (1979, "theravada", "After the Khmer Rouge fell, Theravada Buddhism was restored, and it is the state religion today."))

z("laos", "Laos (Lan Xang)", 102.14, 19.89,
  (-10000, "folk", "Lao and hill peoples worshipped phi spirits of the land and ancestors."),
  (1353, "theravada", "Fa Ngum founded Lan Xang with Khmer monks and the Phra Bang Buddha image, making Theravada the Lao faith."))

z("champasak", "Champasak (Southern Laos)", 105.82, 14.85,
  (-10000, "folk", "Mon-Khmer peoples worshipped spirits of mountains and rivers."),
  (500, "hinduism", "The early Khmer kingdom of Chenla built the Shiva temple of Wat Phu on its sacred mountain."),
  (1400, "theravada", "Theravada Buddhism spread among the Lao and Khmer of the south."))

z("north-vietnam", "North Vietnam", 105.85, 21.03,
  (-10000, "folk", "The Dong Son culture worshipped ancestors, rice spirits and the bronze drum."),
  (-111, "chinese", "Han China conquered the Red River delta, ruling it for a thousand years and planting Confucian and Taoist practice."),
  (1009, "mahayana", "The Ly dynasty, founded by a monk-raised king, made Buddhism the state faith, and the Tran kings founded the Truc Lam school of Zen."),
  (1428, "chinese", "Le Loi's Le dynasty adopted Neo-Confucianism as state ideology, with ancestor worship at the heart of Vietnamese religion."),
  (1954, "secular", "The communist Democratic Republic of Vietnam restricted religion, and most Vietnamese now profess none, though ancestor worship endures."))

z("champa", "Central Vietnam (Champa)", 108.12, 15.8,
  (-10000, "folk", "The Sa Huynh culture of the central coast buried its dead in jars and honoured ancestors."),
  (200, "hinduism", "The Cham kingdom of Champa adopted Shaiva Hinduism, building the temples of My Son."),
  (875, "mahayana", "King Indravarman II founded the great Mahayana monastery of Dong Duong at Indrapura."),
  (925, "hinduism", "Later Cham kings returned to Shaiva Hinduism."),
  (1471, "chinese", "The Vietnamese conquered Vijaya and settled the coast, bringing Confucian ancestor worship and Buddhism."),
  (1975, "secular", "Communist reunification restricted religion, and most people now profess none."))

z("panduranga", "Panduranga (Southern Champa)", 108.99, 11.57,
  (-10000, "folk", "Cham coastal peoples honoured ancestors and sea spirits."),
  (200, "hinduism", "Panduranga, the last Cham principality, worshipped Shiva at temples like Po Klong Garai, some Cham later adopting Islam."),
  (1832, "chinese", "Emperor Minh Mang abolished Panduranga, and Vietnamese settlers brought ancestor worship and Buddhism."),
  (1975, "secular", "Communist reunification restricted religion, and most people now profess none."))

z("south-vietnam", "South Vietnam (Mekong Delta)", 106.7, 10.78,
  (-10000, "folk", "Early delta peoples worshipped land and water spirits."),
  (100, "hinduism", "The port of Oc Eo belonged to Funan, which adopted Hindu gods and Sanskrit kingship."),
  (1300, "theravada", "The Khmer of the lower Mekong adopted Theravada Buddhism."),
  (1698, "mahayana", "The Nguyen lords founded Gia Dinh (Saigon), and Vietnamese settlers brought Mahayana Buddhism and ancestor worship."),
  (1975, "secular", "Communist reunification restricted religion, and most people now profess none."))

# ---------------- MARITIME SOUTHEAST ASIA ----------------
z("kedah", "Kedah", 100.45, 5.75,
  (-10000, "folk", "Malay and Orang Asli peoples worshipped spirits of forest, river and sea."),
  (300, "hinduism", "Indian traders and priests built Hindu shrines in the Bujang valley, the oldest Indianised port on the Malay peninsula."),
  (700, "mahayana", "Kedah came under Srivijaya and became a Mahayana Buddhist port on the route between India and China."),
  (1474, "sunni", "Kedah's raja converted to Islam, by tradition taking the name Sultan Muzaffar Shah, as Malacca's influence spread Islam up the peninsula."))

z("malacca", "Malacca and the Malay Peninsula", 102.25, 2.2,
  (-10000, "folk", "Malay and Orang Asli peoples worshipped spirits of forest, river and sea."),
  (700, "mahayana", "Srivijaya dominated the Strait of Malacca and spread Mahayana Buddhism among its Malay ports."),
  (1414, "sunni", "Malacca's founder Parameswara, or his son, converted to Islam, and the sultanate became the hub from which Sunni Islam spread across the Malay world."))

z("singapore", "Singapore", 103.82, 1.35,
  (-10000, "folk", "Orang Laut sea nomads worshipped spirits of the sea and islands."),
  (1300, "mahayana", "Temasek was a trading port of the Hindu Buddhist Malay world, its rulers claiming descent from Srivijaya."),
  (1400, "sunni", "Temasek fell under the Muslim sultanates of Malacca and then Johor."),
  (1850, "chinese", "After the British founded Singapore in 1819, Chinese immigrants became the majority, worshipping in Taoist and folk temples such as Thian Hock Keng."),
  (1990, "mahayana", "Buddhism overtook Taoism and folk religion as Singapore's largest faith, held by about a third of residents, beside Christians, Muslims and Hindus."))

z("brunei", "Brunei and North Borneo", 114.94, 4.89,
  (-10000, "folk", "The Malay, Dusun and Dayak peoples of northern Borneo followed animist ancestor religions."),
  (1400, "sunni", "Brunei's ruler Awang Alak Betatar converted to Islam as Sultan Muhammad Shah, and the sultanate spread Islam along the coasts of Borneo."))

z("aceh", "Aceh and Pasai", 96.5, 4.8,
  (-10000, "folk", "The peoples of northern Sumatra followed animist religions."),
  (500, "hinduism", "Indian traders brought Hindu and Buddhist worship to the port of Lamuri at Sumatra's northern tip."),
  (1297, "sunni", "Sultan Malik al-Saleh of Samudera Pasai, the first Muslim kingdom in Southeast Asia, died in 1297, and Aceh later became the Veranda of Mecca."))

z("batak", "Batak Lands (Lake Toba)", 99.06, 2.33,
  (-10000, "folk", "The Batak worshipped the high god Mula Jadi Na Bolon and ancestor spirits through datu priests."),
  (1880, "lutheran", "The German Rhenish mission of Ludwig Nommensen converted the Toba Batak, founding the HKBP, now one of Asia's largest Lutheran churches."))

z("minangkabau", "Minangkabau (West Sumatra)", 100.37, -0.3,
  (-10000, "folk", "The Minangkabau followed animist and ancestor religion under their matrilineal adat."),
  (1347, "vajrayana", "King Adityawarman, a Majapahit prince, practised tantric Bhairava Buddhism; it was the court faith rather than the people's."),
  (1600, "sunni", "Islam spread inland from the coast, and the Padri war of 1803 to 1837 later imposed stricter Sunni practice on Minangkabau custom."))

z("palembang", "Palembang (Srivijaya)", 104.75, -2.98,
  (-10000, "folk", "Malay peoples of southern Sumatra worshipped river and ancestor spirits."),
  (683, "mahayana", "Srivijaya, recorded in the Kedukan Bukit inscription of 683, became a great centre of Mahayana Buddhism where the Chinese monk Yijing studied Sanskrit."),
  (1550, "sunni", "Palembang came under the influence of Muslim Demak in Java and adopted Islam, later becoming a sultanate."))

z("sunda", "West Java (Sunda)", 107.6, -6.9,
  (-10000, "folk", "The Sundanese worshipped ancestor and mountain spirits."),
  (400, "hinduism", "King Purnawarman of Tarumanagara inscribed stones with his footprints likened to Vishnu's, the start of Hindu Sunda kingship."),
  (1579, "sunni", "The Muslim sultanate of Banten conquered Pakuan Pajajaran, ending the Hindu kingdom of Sunda."))

z("central-java", "Central Java", 110.36, -7.8,
  (-10000, "folk", "The Javanese worshipped ancestor, rice and volcano spirits."),
  (732, "hinduism", "King Sanjaya of Mataram consecrated a Shiva linga, recorded in the Canggal inscription of 732."),
  (778, "mahayana", "The Sailendra kings embraced Mahayana Buddhism and built Borobudur, the largest Buddhist monument in the world."),
  (856, "hinduism", "Rakai Pikatan's line restored Shaiva Hinduism as the court faith and raised the Prambanan temples to Shiva."),
  (1587, "sunni", "Senopati founded the Islamic sultanate of Mataram, completing inland Java's turn to Islam, often blended with older Javanese custom."))

z("east-java", "East Java (Majapahit)", 112.4, -7.55,
  (-10000, "folk", "The Javanese worshipped ancestor, rice and volcano spirits."),
  (760, "hinduism", "The Kanjuruhan kingdom raised a Shiva temple, and later Kediri, Singhasari and Majapahit fused Shiva and Buddha worship."),
  (1527, "sunni", "Muslim Demak conquered the last of Majapahit, and many Hindu nobles and priests fled to Bali."))

z("bali", "Bali", 114.84, -8.7,
  (-10000, "folk", "The Balinese worshipped ancestor and mountain spirits, above all of Mount Agung."),
  (914, "hinduism", "The Warmadewa kings left Hindu and Buddhist inscriptions, and refugees from Majapahit later made Bali the last Hindu island of Indonesia."))

z("lombok", "Lombok", 116.1, -8.58,
  (-10000, "folk", "The Sasak people worshipped ancestor and nature spirits."),
  (1350, "hinduism", "Majapahit's expansion brought Hindu rule and religion to Lombok."),
  (1600, "sunni", "Javanese and Makassarese preachers converted the Sasak to Islam, even though Hindu Balinese kings ruled the island from the 1740s to 1894."))

z("banjar", "South Borneo (Banjar)", 114.59, -3.32,
  (-10000, "folk", "The Dayak peoples followed the Kaharingan ancestor religion."),
  (1300, "hinduism", "The Javanese-influenced Hindu kingdoms of Negara Dipa and Negara Daha ruled the Barito delta."),
  (1526, "sunni", "Prince Samudera converted to Islam as Sultan Suriansyah, with help from Demak, founding the sultanate of Banjar."))

z("kutai", "East Borneo (Kutai)", 117.15, -0.5,
  (-10000, "folk", "The Dayak peoples followed the Kaharingan ancestor religion."),
  (400, "hinduism", "King Mulawarman's stone pillars of about 400, the oldest inscriptions in Indonesia, record Brahmin sacrifices; this was the court faith."),
  (1575, "sunni", "The rulers of Kutai Kartanegara adopted Islam, which spread among the coastal peoples."))

z("makassar", "South Sulawesi (Makassar)", 119.43, -5.14,
  (-10000, "folk", "The Bugis and Makassarese worshipped ancestors and gods through bissu priests."),
  (1605, "sunni", "Sultan Alauddin of Gowa converted to Islam in 1605 and in wars over the next six years forced Bone and the other Bugis states to follow."))

z("minahasa", "North Sulawesi (Minahasa)", 124.84, 1.47,
  (-10000, "folk", "The Minahasa worshipped ancestor spirits through walian priests."),
  (1840, "reformed", "The Dutch missionaries Riedel and Schwarz, arriving in 1831, converted the Minahasa to Reformed Protestantism within a generation."))

z("ternate", "North Maluku (Ternate)", 127.38, 0.79,
  (-10000, "folk", "The clove islanders of Ternate and Tidore worshipped ancestor spirits."),
  (1486, "sunni", "Sultan Zainal Abidin of Ternate embraced Islam, and the sultanate spread it across the Moluccas."))

z("ambon", "Ambon (Central Maluku)", 128.18, -3.7,
  (-10000, "folk", "The Ambonese worshipped ancestor spirits."),
  (1546, "catholic", "Francis Xavier preached at Ambon, where Portuguese missions had converted many coastal villages."),
  (1605, "reformed", "The Dutch East India Company seized Ambon and turned its Catholic villages into Reformed Protestant congregations."))

z("flores", "Flores and Nusa Tenggara", 121.65, -8.84,
  (-10000, "folk", "The peoples of Flores worshipped ancestor spirits and the sky and earth."),
  (1920, "catholic", "Portuguese Dominicans began at Larantuka in the 1500s, and Dutch Divine Word missionaries from 1913 made Flores overwhelmingly Catholic."))

z("timor-leste", "Timor-Leste", 125.57, -8.56,
  (-10000, "folk", "The Timorese worshipped ancestors through sacred uma lulik houses."),
  (1980, "catholic", "Portuguese missions made a Catholic minority, and under Indonesian occupation from 1975 most Timorese joined the Church, which backed independence."))

z("west-papua", "West Papua", 140.7, -2.53,
  (-10000, "folk", "Papuan peoples worshipped ancestor spirits and held cargo and initiation rites."),
  (1950, "reformed", "Missionaries Ottow and Geissler landed at Mansinam in 1855, and Dutch Reformed missions made most northern Papuans Protestant by the 1950s."))

z("luzon", "Luzon (Manila)", 120.98, 14.6,
  (-10000, "folk", "Tagalogs worshipped Bathala and the anito spirits through babaylan priestesses."),
  (1500, "sunni", "Manila's rajahs such as Sulayman were Muslims tied to Brunei; this was the ruling faith while most villagers kept the anito."),
  (1571, "catholic", "Miguel Lopez de Legazpi took Manila, and Augustinian, Franciscan and Dominican friars made Luzon's lowlands Catholic."))

z("visayas", "Visayas (Cebu)", 123.65, 10.35,
  (-10000, "folk", "Visayans worshipped the anito spirits through babaylan priestesses."),
  (1565, "catholic", "Magellan baptised Rajah Humabon of Cebu in 1521, and after Legazpi founded Cebu in 1565 the Visayas became Catholic."))

z("bangsamoro", "Bangsamoro (Maguindanao, Lanao, Sulu)", 124.25, 7.22,
  (-10000, "folk", "The peoples of Mindanao and the Sulu islands worshipped anito spirits."),
  (1520, "sunni", "Sharif Kabungsuwan founded the Sultanate of Maguindanao, as Sulu had become a sultanate around 1450, and the Moro peoples resisted Spanish Catholicism."))

z("davao", "Davao and Northern Mindanao", 125.6, 7.07,
  (-10000, "folk", "The Lumad peoples of Mindanao's uplands worshipped spirits of nature and ancestors."),
  (1950, "catholic", "Twentieth century migration of Christian settlers from Luzon and the Visayas made Catholics the majority across most of Mindanao."))

# ---------------- OCEANIA ----------------
z("png-papua", "Southern Papua New Guinea", 147.18, -9.44,
  (-10000, "folk", "The Motu, Koita and other peoples of the Papuan coast worshipped ancestor spirits."),
  (1920, "reformed", "The Congregationalist London Missionary Society, arriving in 1871, made coastal Papua Protestant, a tradition now in the United Church."))

z("png-morobe", "Morobe and Madang (PNG)", 147.0, -6.72,
  (-10000, "folk", "The peoples of the Huon Gulf and Madang coast honoured ancestor spirits."),
  (1930, "lutheran", "Johann Flierl founded a German Lutheran mission at Finschhafen in 1886, and mass conversions followed in the 1920s and 1930s."))

z("png-highlands", "Papua New Guinea Highlands", 145.39, -6.08,
  (-10000, "folk", "Highlanders practised ancestor cults and pig-exchange rituals, unknown to the outside world until the 1930s."),
  (1960, "lutheran", "Lutheran missions, with Catholic and evangelical ones beside them, converted most Highlanders within a generation of first contact."))

z("png-sepik", "Sepik (PNG)", 143.63, -3.58,
  (-10000, "folk", "Sepik peoples worshipped ancestors and crocodile spirits in great spirit houses."),
  (1930, "catholic", "Divine Word Catholic missionaries, arriving in 1896, converted most of the Sepik."))

z("new-britain", "New Britain, New Ireland and Bougainville", 152.27, -4.34,
  (-10000, "folk", "The Tolai and other island peoples held ancestor and masked-society rites."),
  (1910, "catholic", "Catholic Sacred Heart and Marist missionaries, competing with Methodists, made most of the islands Catholic."))

z("fiji", "Fiji", 178.44, -18.14,
  (-10000, "folk", "Lapita voyagers settled Fiji about 1000 BC, and Fijians worshipped ancestral gods such as Degei through priests and temples."),
  (1854, "protestant", "The paramount chief Cakobau converted to Methodism, which stayed Fiji's largest church even when Indo-Fijian Hindus made up about 40 percent of the people."))

z("hawaii", "Hawaii", -155.5, 19.6,
  (-10000, "folk", "Polynesians settled Hawaii around AD 1000 and worshipped Ku, Kane, Lono and Kanaloa under the kapu system."),
  (1825, "reformed", "After Liholiho and Kaahumanu abolished the kapu in 1819, Kaahumanu embraced the Congregationalist missionaries from New England, and most Hawaiians followed."),
  (1900, "mahayana", "Japanese plantation workers, about 40 percent of the islands' people by 1900, made Jodo Shinshu and other Buddhist temples the largest religious community."),
  (1950, "catholic", "After the war many Japanese Americans turned Christian or secular, leaving Catholics, with Filipino and Portuguese families, as the largest church."))

z("australia-southeast", "Southeastern Australia", 151.21, -33.87,
  (-10000, "folk", "Aboriginal Australians followed the Dreaming, the law and stories of the ancestral beings who shaped the land."),
  (1788, "anglican", "The First Fleet founded Sydney, and the Church of England was the largest church of the Australian colonies."),
  (1986, "catholic", "Irish and later Italian and other immigrants grew the Catholic Church until it overtook the Anglicans in the 1986 census; today no religion is the largest single answer."))

z("australia-west", "Western Australia", 115.86, -31.95,
  (-10000, "folk", "The Noongar and other peoples followed the Dreaming of their ancestral beings."),
  (1829, "anglican", "The Swan River Colony brought British settlers, among whom the Church of England was the largest church."),
  (1986, "catholic", "Catholics overtook Anglicans as Australia's largest church in the 1986 census."))

z("australia-centre", "Central Australia", 133.88, -23.7,
  (-10000, "folk", "The Arrernte and other desert peoples followed the Dreaming, with sacred sites such as Uluru."),
  (1911, "anglican", "The Commonwealth took over the Northern Territory, and Anglican settler churches led, while Lutheran missions like Hermannsburg converted many Arrernte."),
  (1986, "catholic", "Catholics overtook Anglicans as Australia's largest church in the 1986 census."))

z("australia-north", "Northern Australia (Top End)", 130.84, -12.46,
  (-10000, "folk", "The Larrakia, Yolngu and other peoples followed the Dreaming and traded with Makassarese trepang fishers."),
  (1911, "anglican", "Commonwealth rule of the Northern Territory brought settler churches, with Anglican and Methodist missions in Arnhem Land."),
  (1986, "catholic", "Catholics overtook Anglicans as Australia's largest church in the 1986 census."))

z("tasmania", "Tasmania", 147.33, -42.88,
  (-10000, "folk", "The palawa, Tasmania's Aboriginal people, followed their own ancestral beliefs."),
  (1803, "anglican", "The British penal colony at Hobart brought the Church of England, and the palawa were nearly wiped out in the Black War."),
  (1986, "catholic", "Catholics overtook Anglicans as Australia's largest church in the 1986 census."))

z("new-zealand-north", "New Zealand (North Island)", 174.76, -36.85,
  (-10000, "folk", "No people lived here until Polynesian voyagers arrived around 1280, bringing the Maori gods Tangaroa, Tane and Rangi and Papa."),
  (1840, "anglican", "The Church Missionary Society, active from 1814, converted many Maori, and British settlement after the Treaty of Waitangi made Anglicans the largest church."),
  (2018, "secular", "Nearly half of New Zealanders reported no religion in the 2018 census, the largest group by far, and a majority did by 2023."))

z("canterbury", "Canterbury (New Zealand)", 172.64, -43.53,
  (-10000, "folk", "No people lived here until Polynesians arrived around 1280; the Ngai Tahu worshipped the Maori gods and ancestors."),
  (1850, "anglican", "The Canterbury Association founded Christchurch as an Anglican settlement."),
  (2018, "secular", "Nearly half of New Zealanders reported no religion in the 2018 census, and a majority did by 2023."))

z("otago", "Otago (New Zealand)", 170.5, -45.87,
  (-10000, "folk", "No people lived here until Polynesians arrived around 1280; the Ngai Tahu worshipped the Maori gods and ancestors."),
  (1848, "reformed", "The Free Church of Scotland founded Dunedin as a Presbyterian settlement, and Presbyterians led Otago for a century."),
  (2018, "secular", "Nearly half of New Zealanders reported no religion in the 2018 census, and a majority did by 2023."))

H = os.path.dirname(os.path.abspath(__file__))
json.dump(Z, open(os.path.join(H, "zones_asia.json"), "w"), indent=1, ensure_ascii=False)
print(len(Z), "zones")

#!/usr/bin/env python3
"""Generator for wars_g01.json (group g01: ancient wars, c. 1200 to 221 BC)."""
import json, os

H = os.path.dirname(os.path.abspath(__file__))


def T(side, *polities):
    return {"side": side, "polities": list(polities)}


def F(label, *pts):
    return {"path": [list(p) for p in pts], "label": label}


def M(side, commander, label, *pts):
    return {"side": side, "commander": commander, "label": label, "path": [list(p) for p in pts]}


def E(name, kind, lon, lat, year, winner, text):
    return {"name": name, "kind": kind, "lon": lon, "lat": lat, "year": year, "winner": winner, "text": text}


def S(year, label, title, text, territories=(), fronts=(), moves=(), events=()):
    return {"year": year, "label": label, "title": title, "text": text,
            "territories": list(territories), "fronts": list(fronts),
            "moves": list(moves), "events": list(events)}


def W(id, name, start, end, kind, summary, sides, theater, steps):
    return {"id": id, "name": name, "start": start, "end": end, "kind": kind, "summary": summary,
            "sides": sides, "theater": [{"lon": a, "lat": b, "r": r} for a, b, r in theater], "steps": steps}


def side(name, color, *leaders):
    return {"name": name, "color": color, "leaders": list(leaders)}


# ---------------------------------------------------------------- places
# China
ZHOUYUAN = (107.8, 34.45); FENG = (108.75, 34.22); CHONG = (108.6, 34.1); LI = (113.1, 36.2)
MENGJIN = (112.6, 34.85); MUYE = (113.95, 35.25); CHAOGE = (114.2, 35.6); YIN = (114.3, 36.1)
GUAN = (113.65, 34.75); CAI = (114.26, 33.27); YAN_QUFU = (116.99, 35.6); PUGU = (118.1, 37.1)
LUOYANG = (112.45, 34.65); XIANYANG = (108.7, 34.33); HANGU = (110.88, 34.62)
JINYANG = (112.48, 37.72); DALIANG = (114.31, 34.8); XINZHENG = (113.72, 34.39); LINZI = (118.35, 36.85)
MALING = (115.5, 35.9); ANYI = (111.15, 35.1); HANZHONG = (107.03, 33.07); JIANMEN = (105.55, 32.2)
CHENGDU = (104.07, 30.67); YIQUE = (112.47, 34.55); JI = (116.4, 39.9); JIMO = (120.45, 36.39)
YING = (112.18, 30.42); YICHENG = (112.26, 31.72); CHEN = (114.88, 33.73); CHANGPING = (112.88, 35.8)
HANDAN = (114.48, 36.6); TAIYUAN = (112.55, 37.87); SHOUCHUN = (116.78, 32.58); LIAODONG = (123.17, 41.27)
DAI = (114.56, 39.84)
# Aegean and Anatolia
AULIS = (23.6, 38.43); TROY = (26.24, 39.96); TENEDOS = (26.03, 39.82); SKYROS = (24.55, 38.88)
SARDIS = (28.04, 38.49); MILETUS = (27.28, 37.53); LADE = (27.22, 37.5); EPHESUS = (27.34, 37.94)
ERETRIA = (23.79, 38.39); MARATHON = (23.97, 38.15); ATHENS = (23.73, 37.98); THERMOPYLAE = (22.54, 38.8)
ARTEMISIUM = (23.22, 39.0); SALAMIS = (23.53, 37.95); ISTHMUS = (22.98, 37.93); PLATAEA = (23.27, 38.21)
MYCALE = (27.2, 37.65); EURYMEDON = (31.15, 36.85); SALAMIS_CY = (33.9, 35.18); ABYDOS = (26.4, 40.19)
DORISCUS = (26.0, 40.87); THERMA = (22.95, 40.64); SPARTA = (22.43, 37.08); PYLOS = (21.67, 36.93)
AMPHIPOLIS = (23.84, 40.82); DELIUM = (23.56, 38.36); SYRACUSE = (15.29, 37.07); CORCYRA = (19.92, 39.62)
ASSINARUS = (15.07, 36.87); DECELEA = (23.78, 38.16); CYZICUS = (27.88, 40.38); ARGINUSAE = (26.75, 39.02)
AEGOSPOTAMI = (26.6, 40.3); LAMPSACUS = (26.69, 40.35); SAMOS = (26.95, 37.7); PIRAEUS = (23.64, 37.94)
PELLA = (22.52, 40.76); CHAERONEA = (22.84, 38.5); ELATEA = (22.78, 38.63); THEBES_GR = (23.32, 38.32)
CORINTH = (22.93, 37.91); OLYNTHUS = (23.36, 40.29); CROCUS = (22.8, 39.15); LYNCESTIS = (21.4, 41.0)
GRANICUS = (27.25, 40.2); HALICARNASSUS = (27.42, 37.04); GORDION = (31.99, 39.65); ISSUS = (36.21, 36.84)
CILICIAN_GATES = (34.78, 37.28); KERKENES = (35.06, 39.75)
# Near East, Egypt, Nubia
NINEVEH = (43.15, 36.36); KALHU = (43.33, 36.1); DAMASCUS = (36.3, 33.51); SAMARIA = (35.19, 32.28)
RAPHIA = (34.25, 31.29); GAZA = (34.45, 31.5); NAPATA = (31.83, 18.53); THEBES_EG = (32.65, 25.7)
MEMPHIS = (31.25, 29.85); HERMOPOLIS = (30.8, 27.78); SAIS = (30.77, 31.0); ELTEKEH = (34.8, 31.84)
LACHISH = (34.85, 31.565); JERUSALEM = (35.23, 31.78); HARRAN = (39.03, 36.87); TYRE = (35.2, 33.27)
ARISH = (33.8, 31.13); PELUSIUM = (32.57, 31.04); CARCHEMISH = (38.0, 36.83); ASHKELON = (34.55, 31.66)
ANSHAN = (52.4, 29.97); PASARGADAE = (53.17, 30.2); ECBATANA = (48.51, 34.8); BABYLON = (44.42, 32.54)
OPIS = (44.5, 33.25); SIPPAR = (44.25, 33.06); SUSA = (48.25, 32.19); ALEXANDRIA = (29.9, 31.2)
SIWA = (25.52, 29.2); GAUGAMELA = (43.45, 36.57); PERSEPOLIS = (52.89, 29.93); PERSIAN_GATE = (51.6, 30.65)
HECATOMPYLOS = (54.3, 36.1); BACTRA = (66.9, 36.76); MARACANDA = (66.95, 39.65); JAXARTES = (69.6, 40.28)
TAXILA = (72.83, 33.75); HYDASPES = (73.6, 32.85); HYPHASIS = (75.1, 31.6); PATTALA = (68.4, 25.4)
# India
PATALIPUTRA = (85.14, 25.6); DHAULI = (85.84, 20.19); TOSALI = (85.85, 20.25); JAUGADA = (84.83, 19.53)
UJJAIN = (75.78, 23.18)

wars = []

# =================================================================== 1. Zhou conquest of the Shang
wars.append(W(
    "zhou-conquest-of-shang", "Zhou conquest of the Shang", -1050, -1039, "war",
    "The Zhou, a western vassal people of the Wei valley, overthrew the Shang dynasty that had ruled the North China Plain for some five centuries. "
    "King Wu of Zhou destroyed the army of the last Shang king, Di Xin, at Muye in c. 1046 BC, and his brother the Duke of Zhou crushed a great Shang revolt a few years later. "
    "The victors justified their rule as the Mandate of Heaven, an idea that framed Chinese politics for three thousand years.",
    [side("Zhou and allies", "#b8862b", "King Wen of Zhou", "King Wu of Zhou", "Jiang Ziya", "Duke of Zhou"),
     side("Shang", "#5a6fb8", "Di Xin (King Zhou of Shang)", "Wu Geng")],
    [(112.0, 35.0, 4.5), (116.5, 36.0, 2.5)],
    [
        S(-1050, "c. 1059 to 1050 BC", "Zhou rises in the west",
          "Under nominal Shang overlordship, King Wen of Zhou built up a power base in the Wei valley, conquered the neighbouring state of Chong and moved his capital east to Feng. "
          "He then struck across the mountains at Li in Shanxi, within reach of the Shang heartland, and gathered allied peoples of the west. "
          "The map's border data shows the whole Chinese core as one polity, coloured here for the Shang overlord.",
          [T(1, "Zhoa")],
          [F("Zhou and Shang spheres, c. 1050 BC", (111.2, 36.8), (111.0, 35.5), (111.3, 34.5), (111.6, 33.5))],
          [M(0, "King Wen", "Zhou expansion from Zhouyuan", ZHOUYUAN, CHONG, FENG),
           M(0, "King Wen", "Raid on Li", FENG, (110.3, 34.6), (111.6, 35.4), LI)],
          [E("Zhou conquest of Chong", "war", CHONG[0], CHONG[1], -1052, 0,
             "King Wen took Chong, a Shang ally guarding the Wei valley, and built his new capital Feng nearby.")]),
        S(-1048, "c. 1048 BC", "Gathering at Mengjin",
          "King Wu succeeded his father and led the Zhou army east down the Yellow River to the ford at Mengjin. "
          "Tradition says some eight hundred lords gathered there to join him, but Wu judged the moment premature and withdrew. "
          "Inside the Shang court, Di Xin was alienating his own nobles and spending his armies on wars against the Eastern Yi.",
          [T(1, "Zhoa")],
          [F("Yellow River line", (111.6, 34.8), (112.6, 34.85), (113.6, 34.95), (114.4, 35.15))],
          [M(0, "King Wu", "March to the Mengjin ford", FENG, (110.0, 34.55), HANGU, (111.8, 34.75), MENGJIN),
           M(1, "Di Xin", "Shang wars in the east", CHAOGE, (115.6, 35.5), (117.0, 35.4))],
          [E("Assembly at Mengjin", "event", MENGJIN[0], MENGJIN[1], -1048, None,
             "The allied lords rallied to Zhou at the river crossing, but King Wu turned back to wait.")]),
        S(-1046, "c. 1046 BC", "Battle of Muye",
          "Two years later King Wu crossed at Mengjin with his chariots, the commander Jiang Ziya and contingents from western peoples, and marched on the Shang capital at Chaoge. "
          "On the plain of Muye the Shang army, much of it pressed captives, broke and turned on its own side. "
          "Di Xin set fire to his palace and died, and King Wu proclaimed that Heaven had transferred its mandate to Zhou.",
          [T(0, "Zhoa")],
          [F("Muye, the Shang line", (113.75, 35.35), (113.95, 35.25), (114.15, 35.12))],
          [M(0, "King Wu and Jiang Ziya", "Zhou army crosses and marches on Chaoge", MENGJIN, (113.0, 35.0), MUYE, CHAOGE),
           M(1, "Di Xin", "Shang army goes out to Muye", CHAOGE, (114.05, 35.42), MUYE)],
          [E("Battle of Muye", "battle", MUYE[0], MUYE[1], -1046, 0,
             "The Zhou coalition routed the Shang army in a single day; the traditional date of 1046 BC comes from modern chronology work and is still debated."),
           E("Fall of Chaoge", "event", CHAOGE[0], CHAOGE[1], -1046, 0,
             "Di Xin burned himself in his palace, ending the Shang dynasty.")]),
        S(-1042, "c. 1042 to 1039 BC", "Revolt of the Three Guards",
          "After King Wu died, the Shang prince Wu Geng, left to rule the old capital, rose in revolt with two of Wu's own brothers and the eastern states of Yan and Pugu. "
          "The Duke of Zhou, regent for the young King Cheng, led an eastern expedition that took about three years to crush them. "
          "Zhou then built a second capital at Chengzhou near Luoyang and settled royal kinsmen across the east as fief holders.",
          [T(0, "Zhoa")],
          [F("Rebel front, c. 1042 BC", (113.4, 34.2), (114.0, 35.0), (114.8, 35.8), (115.5, 36.6))],
          [M(0, "Duke of Zhou", "Eastern expedition", FENG, HANGU, LUOYANG, GUAN, YIN),
           M(0, "Duke of Zhou", "Campaign against Yan and Pugu", YIN, (115.6, 35.8), YAN_QUFU, PUGU),
           M(1, "Wu Geng", "Shang rebels and the Three Guards", YIN, (113.9, 35.3), GUAN)],
          [E("Suppression of Wu Geng", "war", YIN[0], YIN[1], -1040, 0,
             "The Duke of Zhou killed Wu Geng and Prince Guan and exiled Prince Cai, ending Shang resistance."),
           E("Founding of Chengzhou", "event", LUOYANG[0], LUOYANG[1], -1038, 0,
             "A new eastern capital at Luoyang let Zhou watch over the conquered plain.")]),
    ]))

# =================================================================== 2. Trojan War (legend)
wars.append(W(
    "trojan-war", "Trojan War (legend)", -1194, -1184, "war",
    "The Trojan War is a legend, told centuries later in Homer's Iliad and Odyssey: a Greek (Achaean) coalition under Agamemnon besieged Troy for ten years to recover Helen and finally took it by the trick of the wooden horse. "
    "Whether a real war lies behind it is unknown, but archaeology at Hisarlik in northwest Turkey shows a rich Bronze Age city that was destroyed more than once around 1250 to 1180 BC, and Hittite letters mention Wilusa (Ilios) and the Ahhiyawa (Achaeans). "
    "The dates used here are traditional, after the ancient scholar Eratosthenes.",
    [side("Achaeans (Mycenaean Greeks)", "#3b6fb6", "Agamemnon", "Achilles", "Odysseus", "Menelaus"),
     side("Troy and allies", "#b5452f", "Priam", "Hector", "Paris", "Aeneas")],
    [(25.0, 38.8, 3.2)],
    [
        S(-1194, "c. 1194 BC (legend)", "The fleet sails from Aulis",
          "In the legend, the Trojan prince Paris carried off Helen, wife of Menelaus of Sparta, and Agamemnon of Mycenae raised a fleet of more than a thousand ships at Aulis. "
          "The Achaeans crossed the Aegean, landed on the beach below Troy and fortified a camp by their ships. "
          "This is myth, not recorded history, though the late Bronze Age Mycenaean kingdoms and Troy were both real.",
          [T(0, "Greek city-states"), T(1, "Phrygians", "Thrace")],
          [],
          [M(0, "Agamemnon", "Achaean fleet", AULIS, SKYROS, (25.4, 39.3), TENEDOS, (26.17, 39.99))],
          [E("Landing at Troy", "event", 26.18, 40.0, -1194, 0,
             "In Homer's story the Achaeans fought their way ashore and beached their ships at the mouth of the Scamander.")]),
        S(-1185, "c. 1194 to 1185 BC (legend)", "Siege and the Iliad",
          "The Iliad covers a few weeks in the tenth year of a long stalemate on the plain between the city and the Achaean camp. "
          "Hector drove the Achaeans back to their ships while Achilles sulked, until Achilles returned to battle and killed Hector. "
          "These scenes are poetry composed around 750 BC; no source confirms them.",
          [T(0, "Greek city-states"), T(1, "Phrygians", "Thrace")],
          [F("Plain of Troy, legendary lines", (26.19, 40.01), (26.21, 39.98), (26.22, 39.95))],
          [M(1, "Hector", "Trojan attack on the ships", TROY, (26.21, 39.98), (26.18, 40.0)),
           M(0, "Achilles", "Achilles' counterattack", (26.18, 40.0), (26.21, 39.98), TROY)],
          [E("Death of Hector", "battle", 26.23, 39.96, -1185, 0,
             "In the Iliad Achilles killed Hector before the walls of Troy, the climax of Homer's poem.")]),
        S(-1184, "c. 1184 BC (legend); c. 1180 BC (archaeology)", "Fall of Troy",
          "In the later legend, the Achaeans pretended to sail away to Tenedos and left a wooden horse with soldiers hidden inside, which the Trojans dragged into their city. "
          "That night Troy was opened and burned. "
          "At Hisarlik, the layer archaeologists call Troy VIIa was destroyed by fire around 1180 BC, during the wider Late Bronze Age collapse, but who destroyed it is unknown.",
          [T(0, "Greek city-states"), T(1, "Phrygians", "Thrace")],
          [],
          [M(0, "Odysseus", "Feigned withdrawal to Tenedos and return", (26.17, 39.99), TENEDOS, (26.17, 39.99), TROY)],
          [E("Sack of Troy", "siege", TROY[0], TROY[1], -1184, 0,
             "Legend says Troy fell to the wooden horse; archaeology shows a burned city at Hisarlik around 1180 BC.")]),
    ]))

# =================================================================== 3. Assyrian and Kushite wars
wars.append(W(
    "assyria-kush-wars", "Assyrian and Kushite wars for Egypt and the Levant", -744, -663, "war",
    "From 744 BC the reformed Neo-Assyrian army of Tiglath-Pileser III and his successors conquered the Aramean and Israelite kingdoms of the Levant, while the Kushite kings of Napata in Nubia made themselves pharaohs of Egypt. "
    "For eighty years the two empires fought through the small states between them, until Esarhaddon and Ashurbanipal invaded Egypt itself and sacked Thebes in 663 BC. "
    "Kush withdrew to Nubia for good, but Assyria had overstretched, and within fifty years both Egypt and Babylon had broken free and Nineveh had fallen.",
    [side("Assyria", "#b5452f", "Tiglath-Pileser III", "Sargon II", "Sennacherib", "Esarhaddon", "Ashurbanipal"),
     side("Kushite Egypt and Levantine allies", "#2f8f83", "Piye", "Shabaka", "Taharqa", "Tantamani", "Hezekiah")],
    [(37.5, 32.5, 6.5), (31.8, 26.0, 7.0)],
    [
        S(-732, "744 to 732 BC", "Tiglath-Pileser III marches west",
          "Tiglath-Pileser III seized the Assyrian throne in 745 BC and built a standing army that subdued the Neo-Hittite and Aramean states of Syria. "
          "When Damascus and Israel formed a coalition against him, he marched down the coast to the border of Egypt in 734 BC and then took Damascus in 732 BC, deporting its people. "
          "In the far south, the Kushite king Kashta already ruled Upper Egypt from Napata.",
          [T(0, "Assyria", "Hittites", "Arameans"), T(1, "Kingdom of David and Solomon", "Kush")],
          [F("Assyrian advance, 734 BC", (35.9, 35.5), (36.8, 34.6), (37.4, 33.6), (38.0, 32.6))],
          [M(0, "Tiglath-Pileser III", "Campaign to Philistia", KALHU, HARRAN, CARCHEMISH, (36.2, 34.5), TYRE, GAZA),
           M(0, "Tiglath-Pileser III", "Siege of Damascus", GAZA, (35.6, 32.6), DAMASCUS)],
          [E("Fall of Damascus", "siege", DAMASCUS[0], DAMASCUS[1], -732, 0,
             "Assyria captured Damascus, executed King Rezin and ended the Aramean kingdom.")]),
        S(-728, "c. 728 BC", "Piye conquers Egypt",
          "Egypt was split among rival Libyan princes, and Tefnakht of Sais was pushing south up the Nile. "
          "The Kushite king Piye sailed and marched north from Napata, took Hermopolis and stormed Memphis, and the Delta rulers submitted to him. "
          "Under his brother Shabaka the Kushite 25th Dynasty ruled all of Egypt, putting a new power on Assyria's southwest flank.",
          [T(0, "Assyria", "Hittites", "Arameans", "Babylonia", "Kingdom of David and Solomon"), T(1, "Kush", "Egypt")],
          [],
          [M(1, "Piye", "Kushite army down the Nile", NAPATA, (32.9, 21.9), THEBES_EG, HERMOPOLIS, MEMPHIS),
           M(1, "Piye", "Submission of the Delta", MEMPHIS, (31.0, 30.5), SAIS)],
          [E("Siege of Memphis", "siege", MEMPHIS[0], MEMPHIS[1], -728, 1,
             "Piye stormed Memphis from the river side, and the princes of the Delta submitted to him.")]),
        S(-720, "722 to 720 BC", "Samaria and Raphia",
          "Shalmaneser V and then Sargon II took Samaria after a long siege and deported the people of the northern Kingdom of Israel. "
          "When Gaza rebelled with Egyptian help, Sargon defeated the rebels and an Egyptian force at Raphia, the first clash between Assyria and the Nile kingdom.",
          [T(0, "Assyria", "Hittites", "Arameans", "Kingdom of David and Solomon"), T(1, "Kush", "Egypt")],
          [F("Egyptian border, 720 BC", (34.2, 31.3), (34.5, 30.7), (34.9, 30.0))],
          [M(0, "Sargon II", "Sargon's army to the Egyptian border", HARRAN, CARCHEMISH, DAMASCUS, SAMARIA, GAZA, RAPHIA),
           M(1, "Egyptian expeditionary force", "Egyptian army to Gaza", MEMPHIS, PELUSIUM, ARISH, RAPHIA)],
          [E("Fall of Samaria", "siege", SAMARIA[0], SAMARIA[1], -722, 0,
             "Assyria ended the northern Kingdom of Israel and deported much of its population."),
           E("Battle of Raphia", "battle", RAPHIA[0], RAPHIA[1], -720, 0,
             "Sargon II beat Gaza and its Egyptian allies on the frontier of Egypt.")]),
        S(-701, "701 BC", "Sennacherib and Hezekiah",
          "Hezekiah of Judah, Sidon and the Philistine cities rebelled, counting on Kushite Egypt. "
          "Sennacherib swept down the coast, defeated the Egyptian and Kushite relief army at Eltekeh and stormed Lachish, then shut Hezekiah up in Jerusalem. "
          "Jerusalem was not taken, but Hezekiah paid heavy tribute and the Levant stayed Assyrian.",
          [T(0, "Assyria", "Hittites", "Arameans", "Babylonia"), T(1, "Kingdom of David and Solomon", "Kush", "Egypt")],
          [F("Judah's border, 701 BC", (34.7, 32.1), (34.95, 31.75), (34.9, 31.3))],
          [M(0, "Sennacherib", "Assyrian army down the coast", NINEVEH, CARCHEMISH, (36.2, 34.5), TYRE, ASHKELON, LACHISH),
           M(1, "Taharqa (tradition)", "Kushite and Egyptian relief army", MEMPHIS, PELUSIUM, GAZA, ELTEKEH),
           M(0, "Rabshakeh", "Blockade of Jerusalem", LACHISH, (35.05, 31.7), JERUSALEM)],
          [E("Battle of Eltekeh", "battle", ELTEKEH[0], ELTEKEH[1], -701, 0,
             "Sennacherib defeated the army sent from Egypt to relieve the rebels."),
           E("Siege of Lachish", "siege", LACHISH[0], LACHISH[1], -701, 0,
             "Assyria stormed Judah's second city, a victory carved on the walls of Sennacherib's palace at Nineveh."),
           E("Blockade of Jerusalem", "siege", JERUSALEM[0], JERUSALEM[1], -701, None,
             "The city held out, and Hezekiah bought peace with tribute while remaining an Assyrian vassal.")]),
        S(-671, "674 to 671 BC", "Esarhaddon invades Egypt",
          "Taharqa, the most powerful Kushite pharaoh, kept stirring revolt in the Levant. "
          "A first Assyrian invasion was thrown back at the Egyptian border in 674 BC, but in 671 BC Esarhaddon crossed Sinai with camels supplied by Arab allies and fought his way to Memphis. "
          "Memphis fell, Taharqa's family was captured, and Taharqa fled south.",
          [T(0, "Assyria", "Hittites", "Arameans", "Babylonia", "Kingdom of David and Solomon"), T(1, "Kush", "Egypt")],
          [F("Nile Delta front, 671 BC", (32.6, 31.2), (32.3, 30.6), (31.9, 30.1))],
          [M(0, "Esarhaddon", "Invasion across Sinai", GAZA, RAPHIA, ARISH, PELUSIUM, (31.7, 30.5), MEMPHIS),
           M(1, "Taharqa", "Retreat to Thebes and Nubia", MEMPHIS, HERMOPOLIS, THEBES_EG)],
          [E("Assyrian repulse at the border", "battle", 32.4, 31.0, -674, 1,
             "Babylonian records note an Assyrian defeat in Egypt, a rare setback for Esarhaddon."),
           E("Fall of Memphis", "siege", MEMPHIS[0], MEMPHIS[1], -671, 0,
             "Esarhaddon took Memphis and installed Assyrian governors and vassal princes in Lower Egypt.")]),
        S(-667, "669 to 666 BC", "Ashurbanipal and Taharqa",
          "Taharqa returned and retook Memphis, and Esarhaddon died at Harran on his way to deal with him. "
          "His son Ashurbanipal sent an army that beat Taharqa in the Delta and pushed up the Nile to Thebes. "
          "Assyria ruled Egypt through Delta princes such as Necho I of Sais, whose loyalty was shaky.",
          [T(0, "Assyria", "Hittites", "Arameans", "Babylonia", "Kingdom of David and Solomon", "Egypt"), T(1, "Kush")],
          [],
          [M(1, "Taharqa", "Kushite return to Memphis", THEBES_EG, HERMOPOLIS, MEMPHIS),
           M(0, "Ashurbanipal's generals", "Assyrian army to Thebes", PELUSIUM, (31.4, 30.6), MEMPHIS, HERMOPOLIS, THEBES_EG)],
          [E("Battle of Karbaniti", "battle", 31.4, 30.6, -667, 0,
             "Ashurbanipal's army defeated Taharqa in the Delta and retook Memphis; the exact site is unknown.")]),
        S(-663, "664 to 663 BC", "Sack of Thebes",
          "Taharqa's successor Tantamani marched north, retook Memphis and killed Necho I. "
          "Ashurbanipal answered with a full invasion: Tantamani fled, and the Assyrians sacked Thebes, the ancient religious capital of Egypt, carrying off its treasures. "
          "Kush never again ruled Egypt, and Necho's son Psamtik I, at first an Assyrian vassal, soon made Egypt independent.",
          [T(0, "Assyria", "Hittites", "Arameans", "Babylonia", "Kingdom of David and Solomon", "Egypt"), T(1, "Kush")],
          [],
          [M(1, "Tantamani", "Kushite offensive", NAPATA, (32.9, 21.9), THEBES_EG, MEMPHIS),
           M(0, "Ashurbanipal", "Assyrian counterattack", PELUSIUM, MEMPHIS, HERMOPOLIS, THEBES_EG),
           M(1, "Tantamani", "Flight to Nubia", THEBES_EG, (32.9, 21.9), NAPATA)],
          [E("Sack of Thebes", "siege", THEBES_EG[0], THEBES_EG[1], -663, 0,
             "Assyria plundered Thebes, ending Kushite rule in Egypt."),
           E("Psamtik I in power", "event", SAIS[0], SAIS[1], -664, None,
             "Assyria's Saite vassal became pharaoh and reunified Egypt, breaking away from Assyria within a decade.")]),
    ]))

# =================================================================== 4. Cyrus and Cambyses
wars.append(W(
    "persian-conquests-cyrus-cambyses", "Persian conquests of Cyrus and Cambyses", -553, -525, "war",
    "Cyrus II, king of the small Persian realm of Anshan, overthrew his Median overlord Astyages in 550 BC and then defeated, one after another, the allied powers that might have stopped him: Lydia in 547 BC and Babylon in 539 BC. "
    "His son Cambyses II completed the work by conquering Egypt in 525 BC. "
    "In 25 years the Persians built the Achaemenid Empire, the largest state the world had yet seen, stretching from the Aegean to Central Asia and the Nile.",
    [side("Persians", "#b5452f", "Cyrus the Great", "Harpagus", "Gobryas", "Cambyses II"),
     side("Media, Lydia, Babylon and Egypt", "#3f8f6f", "Astyages", "Croesus", "Nabonidus", "Psamtik III")],
    [(40.0, 35.0, 12.0), (31.5, 30.5, 3.5)],
    [
        S(-550, "553 to 550 BC", "Cyrus overthrows Media",
          "Cyrus, a Persian vassal king of the Medes, rebelled against his grandfather Astyages. "
          "When Astyages marched into Persis, part of his army mutinied under the noble Harpagus and handed him over, and Cyrus then took the Median capital Ecbatana with its treasury. "
          "The Median lands from the Zagros to the Halys river in Anatolia passed to the Persians.",
          [T(0, "Elam", "state societies and Aramaean kingdoms", "Urartu", "Assyria", "Hittites"),
           T(1, "Phrygians", "Babylonia", "Arameans", "Kingdom of David and Solomon", "Egypt")],
          [F("Persis and Media, 550 BC", (50.0, 32.5), (51.5, 31.6), (53.5, 31.4))],
          [M(1, "Astyages", "Median army into Persis", ECBATANA, (49.8, 33.0), (51.4, 31.5), PASARGADAE),
           M(0, "Cyrus", "Persian march on Ecbatana", PASARGADAE, (51.4, 31.5), (49.8, 33.0), ECBATANA)],
          [E("Battle of Pasargadae", "battle", PASARGADAE[0], PASARGADAE[1], -550, 0,
             "Astyages' army defected to Cyrus, and the Median king was captured."),
           E("Capture of Ecbatana", "siege", ECBATANA[0], ECBATANA[1], -550, 0,
             "Cyrus took the Median capital and its treasure, inheriting Media's empire.")]),
        S(-547, "547 to 546 BC", "Croesus and the fall of Sardis",
          "Croesus of Lydia, allied with Babylon, Egypt and Sparta, crossed the Halys to strike first. "
          "After an indecisive battle at Pteria he went home for the winter, but Cyrus followed him straight to Sardis, routed the Lydian cavalry with his camels and took the citadel. "
          "Harpagus then subdued the Greek cities of Ionia.",
          [T(0, "Elam", "state societies and Aramaean kingdoms", "Urartu", "Assyria", "Hittites"),
           T(1, "Phrygians", "Babylonia", "Arameans", "Kingdom of David and Solomon", "Egypt")],
          [F("Halys river frontier", (34.4, 41.4), (34.1, 40.5), (34.0, 39.6), (34.6, 38.8))],
          [M(1, "Croesus", "Lydian invasion over the Halys", SARDIS, (30.5, 39.2), (33.0, 39.6), KERKENES),
           M(0, "Cyrus", "Persian pursuit to Sardis", ECBATANA, (43.6, 37.5), (38.5, 38.8), KERKENES, (31.5, 39.0), SARDIS),
           M(0, "Harpagus", "Conquest of Ionia", SARDIS, EPHESUS, MILETUS)],
          [E("Battle of Pteria", "battle", KERKENES[0], KERKENES[1], -547, None,
             "Neither king won outright, and Croesus withdrew to Sardis expecting no winter campaign."),
           E("Siege of Sardis", "siege", SARDIS[0], SARDIS[1], -546, 0,
             "Cyrus took the Lydian capital and captured Croesus, making Anatolia Persian.")]),
        S(-539, "539 BC", "Fall of Babylon",
          "After campaigns in the east, Cyrus turned on the Neo-Babylonian Empire, whose king Nabonidus had alienated the priests of Marduk. "
          "Cyrus beat the Babylonian army at Opis on the Tigris, Sippar opened its gates, and his general Gobryas entered Babylon without a fight. "
          "Syria and Palestine came with it, and Cyrus allowed exiled peoples, including the Jews, to return home.",
          [T(0, "Elam", "state societies and Aramaean kingdoms", "Urartu", "Assyria", "Hittites", "Phrygians", "Iranian pastoralists"),
           T(1, "Babylonia", "Arameans", "Kingdom of David and Solomon", "Egypt")],
          [F("Tigris front, 539 BC", (43.9, 34.3), (44.5, 33.3), (45.3, 32.6))],
          [M(0, "Cyrus", "Persian army down the Diyala", ECBATANA, (46.4, 34.4), (45.2, 33.9), OPIS),
           M(0, "Gobryas", "Advance on Babylon", OPIS, SIPPAR, BABYLON)],
          [E("Battle of Opis", "battle", OPIS[0], OPIS[1], -539, 0,
             "Cyrus destroyed the main Babylonian army near the Tigris."),
           E("Fall of Babylon", "siege", BABYLON[0], BABYLON[1], -539, 0,
             "Babylon surrendered almost without fighting, and Cyrus entered as a restorer of order.")]),
        S(-530, "530 BC", "Death of Cyrus",
          "Cyrus spent his last years on the steppe frontier of Central Asia. "
          "In 530 BC he was killed fighting the Massagetae nomads east of the Caspian, according to Herodotus by the army of their queen Tomyris. "
          "His son Cambyses II succeeded him and prepared to attack Egypt, the last great independent power of the Near East.",
          [T(0, "Elam", "state societies and Aramaean kingdoms", "Urartu", "Assyria", "Hittites", "Phrygians", "Iranian pastoralists",
             "Babylonia", "Arameans", "Kingdom of David and Solomon"),
           T(1, "Egypt")],
          [],
          [M(0, "Cyrus", "Campaign against the Massagetae", ECBATANA, (54.4, 36.2), (58.4, 37.9), (61.0, 42.0))],
          [E("Death of Cyrus", "battle", 61.0, 42.0, -530, None,
             "Cyrus fell in battle with the Massagetae; the site is unknown.")]),
        S(-525, "525 BC", "Cambyses conquers Egypt",
          "Cambyses gathered a Phoenician and Cypriot fleet, and Arab chiefs supplied water for his army's crossing of Sinai. "
          "At Pelusium on the eastern edge of the Delta he crushed the army of the new pharaoh Psamtik III, then besieged and took Memphis. "
          "Egypt became a Persian satrapy, and Libya and Cyrene submitted soon after.",
          [T(0, "Elam", "state societies and Aramaean kingdoms", "Urartu", "Assyria", "Hittites", "Phrygians", "Iranian pastoralists",
             "Babylonia", "Arameans", "Kingdom of David and Solomon"),
           T(1, "Egypt")],
          [F("Pelusium line, 525 BC", (32.75, 31.2), (32.55, 30.95), (32.35, 30.6))],
          [M(0, "Cambyses II", "Persian army across Sinai", GAZA, RAPHIA, ARISH, PELUSIUM, MEMPHIS),
           M(0, "Phoenician fleet", "Fleet along the coast", (35.0, 33.0), (34.2, 31.8), (33.0, 31.3), (31.9, 31.5))],
          [E("Battle of Pelusium", "battle", PELUSIUM[0], PELUSIUM[1], -525, 0,
             "Cambyses defeated Psamtik III's army and opened the road to the Nile."),
           E("Siege of Memphis", "siege", MEMPHIS[0], MEMPHIS[1], -525, 0,
             "Memphis fell and Psamtik III was captured, ending the 26th Dynasty.")]),
    ]))

# =================================================================== 5. Greco-Persian Wars
GP_T = [T(0, "Greek city-states"), T(1, "Achaemenid Empire")]
wars.append(W(
    "greco-persian-wars", "Greco-Persian Wars", -499, -449, "war",
    "The Achaemenid Persian Empire fought Athens, Sparta and their allies after the Greek cities of Ionia rebelled against Persian rule with Athenian help. "
    "Two Persian invasions of mainland Greece were defeated, at Marathon in 490 BC and at Salamis and Plataea in 480 to 479 BC, and the Athenian-led Delian League then carried the war into Persian waters. "
    "The Greek victory preserved the independence of the city-states and opened the classical age of Athens.",
    [side("Greek city-states", "#2f6db5", "Miltiades", "Leonidas", "Themistocles", "Pausanias", "Cimon"),
     side("Persian Empire", "#b5452f", "Darius I", "Xerxes I", "Datis and Artaphernes", "Mardonius")],
    [(23.5, 38.5, 3.5), (27.5, 38.0, 2.5), (31.5, 35.8, 2.8)],
    [
        S(-499, "499 to 494 BC", "Ionian Revolt",
          "Aristagoras of Miletus led the Greek cities of Ionia in revolt against their Persian-backed tyrants, and Athens and Eretria sent ships. "
          "The rebels marched inland and burned Sardis, the seat of the Persian satrap, in 498 BC. "
          "Persia slowly recovered the coast, destroyed the Ionian fleet off Lade and sacked Miletus, and Darius swore revenge on Athens.",
          GP_T, [],
          [M(0, "Aristagoras", "Ionians and Athenians march on Sardis", EPHESUS, (27.7, 38.25), SARDIS),
           M(1, "Persian fleet", "Phoenician fleet to Miletus", (32.0, 36.2), (29.0, 36.4), (27.6, 37.0), LADE)],
          [E("Burning of Sardis", "event", SARDIS[0], SARDIS[1], -498, 0,
             "The rebels burned the lower city of Sardis, which made Athens an enemy of Darius."),
           E("Battle of Lade", "battle", LADE[0], LADE[1], -494, 1,
             "The Persian fleet crushed the Ionian navy after the Samians deserted, ending the revolt.")]),
        S(-490, "490 BC", "Marathon",
          "Darius sent a seaborne expedition under Datis and Artaphernes across the Aegean to punish Eretria and Athens. "
          "Eretria was betrayed and burned, but on the plain of Marathon the Athenians and Plataeans under Miltiades charged and routed the landing force. "
          "The Persian fleet sailed round to Athens, found the army back in the city and went home.",
          GP_T, [],
          [M(1, "Datis and Artaphernes", "Expedition across the Aegean", SAMOS, (25.4, 37.1), (24.4, 37.9), ERETRIA, (23.98, 38.12)),
           M(0, "Miltiades", "Athenian army to Marathon", ATHENS, (23.85, 38.08), MARATHON)],
          [E("Sack of Eretria", "siege", ERETRIA[0], ERETRIA[1], -490, 1,
             "Eretria fell after six days when traitors opened the gates."),
           E("Battle of Marathon", "battle", MARATHON[0], MARATHON[1], -490, 0,
             "Miltiades' hoplites routed the Persian army on the shore and forced the expedition home.")]),
        S(-480, "480 BC", "Thermopylae and Artemisium",
          "Xerxes bridged the Hellespont and led a huge army and fleet along the coast of Thrace and Macedonia, which submitted. "
          "The allied Greeks held the narrow pass of Thermopylae on land and the Artemisium strait at sea. "
          "After three days a mountain path let the Persians outflank the pass; Leonidas and his Spartans died covering the retreat, and the Greek fleet fell back.",
          GP_T,
          [F("Thermopylae and Artemisium line", THERMOPYLAE, (22.85, 38.88), ARTEMISIUM)],
          [M(1, "Xerxes I", "Royal army through Thrace", SARDIS, ABYDOS, DORISCUS, THERMA, (22.4, 39.5), THERMOPYLAE),
           M(1, "Persian fleet", "Fleet along the coast", ABYDOS, (25.0, 40.4), (23.9, 40.0), (23.4, 39.3), ARTEMISIUM),
           M(0, "Leonidas", "Greek army to Thermopylae", ISTHMUS, (22.9, 38.3), THERMOPYLAE)],
          [E("Battle of Thermopylae", "battle", THERMOPYLAE[0], THERMOPYLAE[1], -480, 1,
             "Leonidas held the pass for three days before being surrounded and killed."),
           E("Battle of Artemisium", "battle", ARTEMISIUM[0], ARTEMISIUM[1], -480, None,
             "The Greek fleet fought the Persian navy to a standstill, then withdrew when the pass fell.")]),
        S(-480, "September 480 BC", "Salamis",
          "The Persians marched through Boeotia and burned an evacuated Athens, while the Peloponnesians walled off the Isthmus of Corinth. "
          "Themistocles kept the allied fleet at Salamis and lured the Persian navy into the narrow straits, where it was shattered. "
          "Xerxes returned to Asia with much of his army, leaving Mardonius to finish the war.",
          GP_T,
          [F("Isthmus wall", (22.88, 37.97), ISTHMUS, (23.05, 37.88))],
          [M(1, "Xerxes I", "Persians take Athens", THERMOPYLAE, (22.9, 38.5), (23.3, 38.3), ATHENS),
           M(1, "Persian fleet", "Fleet into the straits", (23.62, 37.9), SALAMIS),
           M(0, "Themistocles", "Allied fleet at Salamis", (23.45, 37.92), SALAMIS)],
          [E("Battle of Salamis", "battle", SALAMIS[0], SALAMIS[1], -480, 0,
             "The Greek triremes destroyed the Persian fleet in the narrows, the turning point of the war.")]),
        S(-479, "479 BC", "Plataea and Mycale",
          "Mardonius wintered in Thessaly and came south again. "
          "The largest Greek army ever assembled, under the Spartan regent Pausanias, met him on the Asopus river and destroyed his army at Plataea, killing Mardonius. "
          "On the same day, by tradition, the Greek fleet landed at Mycale in Ionia and burned the Persian ships.",
          GP_T,
          [F("Asopus river line", (23.12, 38.24), PLATAEA, (23.42, 38.28))],
          [M(1, "Mardonius", "Persian army returns south", (22.4, 39.5), (22.6, 38.8), (23.2, 38.32)),
           M(0, "Pausanias", "Greek army over Cithaeron", ISTHMUS, (23.35, 38.05), PLATAEA),
           M(0, "Leotychidas", "Greek fleet to Mycale", (25.3, 37.4), SAMOS, MYCALE)],
          [E("Battle of Plataea", "battle", PLATAEA[0], PLATAEA[1], -479, 0,
             "Mardonius was killed and his army routed, ending the Persian invasion of Greece."),
           E("Battle of Mycale", "battle", MYCALE[0], MYCALE[1], -479, 0,
             "The Greeks destroyed the beached Persian fleet, and Ionia rose again.")]),
        S(-466, "478 to 466 BC", "Delian League offensive",
          "Athens organised the Delian League to free the Greek cities of Asia and keep Persia out of the Aegean. "
          "Under Cimon the league fleet swept the coast of Asia Minor and won a double victory on land and sea at the Eurymedon river.",
          GP_T, [],
          [M(0, "Cimon", "League fleet along Asia Minor", (24.0, 37.5), (27.3, 36.6), (28.5, 36.35), (30.3, 36.0), EURYMEDON)],
          [E("Battle of the Eurymedon", "battle", EURYMEDON[0], EURYMEDON[1], -466, 0,
             "Cimon destroyed a Persian fleet and then its army at the river mouth in Pamphylia.")]),
        S(-450, "450 to 449 BC", "Cyprus and the Peace of Callias",
          "A last Athenian expedition fought for Cyprus, where Cimon died during the siege of Kition. "
          "After a victory off Salamis in Cyprus, fighting stopped, and later tradition holds that the Peace of Callias recognised the freedom of the Ionian Greeks.",
          GP_T, [],
          [M(0, "Cimon", "Athenian fleet to Cyprus", (28.5, 36.3), (31.0, 35.9), (33.0, 35.6), SALAMIS_CY)],
          [E("Battle of Salamis in Cyprus", "battle", SALAMIS_CY[0], SALAMIS_CY[1], -450, 0,
             "The Athenians beat a Phoenician and Cilician fleet and its army near Salamis in Cyprus."),
           E("Peace of Callias", "treaty", ATHENS[0], ATHENS[1], -449, None,
             "A peace, attested only by later writers, ended open war between Athens and Persia.")]),
    ]))

# =================================================================== 6. Peloponnesian War
wars.append(W(
    "peloponnesian-war", "Peloponnesian War", -431, -404, "war",
    "Athens, a sea power ruling an Aegean empire, fought Sparta and its Peloponnesian League, a land power, for 27 years. "
    "Neither could strike the other's strength until Athens lost a great army in Sicily and Persia began paying for a Spartan fleet, which under Lysander destroyed the Athenian navy at Aegospotami. "
    "Athens surrendered in 404 BC, ending its empire, and the war left Greece exhausted and open to Persian, Theban and later Macedonian influence.",
    [side("Athens and the Delian League", "#2f6db5", "Pericles", "Cleon", "Demosthenes", "Nicias", "Alcibiades"),
     side("Sparta and the Peloponnesian League", "#b5452f", "Archidamus II", "Brasidas", "Gylippus", "Lysander")],
    [(23.0, 38.2, 3.0), (26.8, 39.3, 2.0), (15.2, 37.2, 1.3)],
    [
        S(-431, "431 to 430 BC", "Pericles' strategy",
          "The war began when Thebes, Sparta's ally, attacked Athens' ally Plataea. "
          "King Archidamus II led the Peloponnesian army into Attica each summer to burn the farms, while Pericles brought the Athenians inside the Long Walls and sent the fleet to raid the Peloponnese. "
          "In 430 BC plague broke out in the crowded city and killed perhaps a quarter of the population, Pericles among them in 429 BC.",
          [], [],
          [M(1, "Archidamus II", "Annual invasion of Attica", SPARTA, (22.6, 37.6), ISTHMUS, (23.4, 38.05), (23.75, 38.12)),
           M(0, "Pericles", "Athenian fleet raids the Peloponnese", PIRAEUS, (23.3, 37.4), (23.0, 36.6), (22.2, 36.7), PYLOS)],
          [E("Invasion of Attica", "event", 23.75, 38.12, -431, 1,
             "The Spartans ravaged Attica while the Athenians watched from their walls."),
           E("Plague of Athens", "event", ATHENS[0], ATHENS[1], -430, 1,
             "An epidemic killed tens of thousands inside the overcrowded city.")]),
        S(-425, "425 BC", "Pylos and Sphacteria",
          "The Athenian general Demosthenes fortified the headland of Pylos on Sparta's own coast. "
          "Spartan troops landed on the island of Sphacteria to blockade him and were cut off by the Athenian fleet; Cleon and Demosthenes then stormed the island. "
          "The surrender of 292 men, about 120 of them full Spartan citizens, shocked Greece and gave Athens hostages that ended the invasions of Attica.",
          [], [],
          [M(0, "Demosthenes", "Fleet to Pylos", PIRAEUS, (23.3, 37.4), (23.0, 36.5), (21.9, 36.7), PYLOS),
           M(1, "Spartan army", "Spartans rush to Pylos", SPARTA, (22.1, 37.05), PYLOS)],
          [E("Battle of Sphacteria", "battle", 21.67, 36.94, -425, 0,
             "Athenian light troops forced the surrender of the Spartan garrison on Sphacteria.")]),
        S(-422, "424 to 421 BC", "Delium, Amphipolis and the Peace of Nicias",
          "Athens' attempt to knock Boeotia out of the war failed at Delium. "
          "The Spartan Brasidas marched through Thessaly to Thrace and took Amphipolis, Athens' key colony, and in 422 BC both Brasidas and Cleon died in the battle to retake it. "
          "With the leading hawks gone, the Peace of Nicias in 421 BC restored the prewar position.",
          [], [],
          [M(1, "Brasidas", "March to Thrace", CORINTH, (22.6, 38.9), (22.4, 39.6), THERMA, AMPHIPOLIS),
           M(0, "Cleon", "Expedition to retake Amphipolis", PIRAEUS, (24.0, 38.6), (24.3, 39.8), AMPHIPOLIS)],
          [E("Battle of Delium", "battle", DELIUM[0], DELIUM[1], -424, 1,
             "The Boeotians routed an Athenian army invading their territory."),
           E("Battle of Amphipolis", "battle", AMPHIPOLIS[0], AMPHIPOLIS[1], -422, 1,
             "Brasidas defeated Cleon; both commanders were killed."),
           E("Peace of Nicias", "treaty", ATHENS[0], ATHENS[1], -421, None,
             "A fifty-year peace that in practice lasted only a few years.")]),
        S(-415, "415 to 413 BC", "The Sicilian Expedition",
          "Persuaded by Alcibiades, Athens sent a huge fleet and army to conquer Syracuse, the greatest Greek city of Sicily. "
          "Alcibiades, recalled to face charges, fled to Sparta and advised it to send Gylippus to lead the defence. "
          "Reinforcements under Demosthenes could not break the siege, and in 413 BC the whole force was destroyed in the retreat; Nicias and Demosthenes were executed.",
          [],
          [F("Siege walls at Syracuse", (15.22, 37.1), (15.25, 37.07), (15.28, 37.05))],
          [M(0, "Nicias and Alcibiades", "Athenian armada", PIRAEUS, (21.0, 37.8), CORCYRA, (17.5, 39.3), (16.1, 37.9), SYRACUSE),
           M(1, "Gylippus", "Spartan relief of Syracuse", CORINTH, (20.5, 38.3), (16.5, 38.6), (15.6, 38.2), SYRACUSE),
           M(0, "Nicias and Demosthenes", "Retreat to the Assinarus", SYRACUSE, (15.15, 36.98), ASSINARUS)],
          [E("Siege of Syracuse", "siege", SYRACUSE[0], SYRACUSE[1], -414, 1,
             "Gylippus broke the Athenian siege lines, and the Athenian fleet was beaten in the Great Harbour."),
           E("Disaster at the Assinarus", "battle", ASSINARUS[0], ASSINARUS[1], -413, 1,
             "The retreating Athenian army was cut down at the river and the survivors sent to the quarries.")]),
        S(-412, "413 to 411 BC", "Decelea and Persian gold",
          "On Alcibiades' advice Sparta fortified Decelea in Attica, holding it year round and letting some 20,000 Athenian slaves escape from the silver mines. "
          "Athens' allies in Ionia revolted, and the Persian satrap Tissaphernes agreed to fund a Spartan fleet in return for the Greek cities of Asia. "
          "Athens rebuilt its navy from its last reserve fund.",
          [T(1, "Achaemenid Empire")],
          [],
          [M(1, "Agis II", "Occupation of Decelea", SPARTA, ISTHMUS, (23.4, 38.1), DECELEA),
           M(1, "Spartan fleet", "Spartan fleet to Ionia", CORINTH, (24.5, 37.5), (26.0, 38.3), MILETUS)],
          [E("Fortification of Decelea", "event", DECELEA[0], DECELEA[1], -413, 1,
             "A permanent Spartan fort in Attica cut Athens off from its land and mines."),
           E("Treaty of Miletus", "treaty", MILETUS[0], MILETUS[1], -412, 1,
             "Sparta traded the Greek cities of Asia for Persian money to build a fleet.")]),
        S(-410, "411 to 406 BC", "Athens strikes back at sea",
          "The war moved to the Hellespont, through which Athens' grain ships passed. "
          "Recalled by the fleet, Alcibiades won a crushing victory at Cyzicus in 410 BC, and in 406 BC the Athenians won again at Arginusae, though they executed six victorious generals for failing to rescue the drowning. "
          "Meanwhile Persia's prince Cyrus the Younger gave Lysander's fleet steady pay.",
          [T(1, "Achaemenid Empire")],
          [F("Hellespont grain route", (26.2, 40.05), (26.6, 40.3), (27.2, 40.4))],
          [M(0, "Alcibiades", "Athenian fleet to Cyzicus", (25.9, 40.0), ABYDOS, (27.4, 40.42), CYZICUS),
           M(1, "Mindarus", "Peloponnesian fleet", MILETUS, (26.5, 38.8), ABYDOS, CYZICUS),
           M(0, "Athenian generals", "Relief fleet to Arginusae", PIRAEUS, (24.8, 38.3), (26.0, 38.8), ARGINUSAE)],
          [E("Battle of Cyzicus", "battle", CYZICUS[0], CYZICUS[1], -410, 0,
             "Alcibiades destroyed the Peloponnesian fleet and killed its admiral Mindarus."),
           E("Battle of Arginusae", "battle", ARGINUSAE[0], ARGINUSAE[1], -406, 0,
             "Athens won the largest naval battle of the war among Greeks.")]),
        S(-405, "405 to 404 BC", "Aegospotami and surrender",
          "Lysander took his Persian-funded fleet to the Hellespont and seized Lampsacus. "
          "The Athenian fleet beached opposite at Aegospotami, and Lysander caught most of it on the shore, capturing about 170 ships. "
          "Cut off from its grain, Athens was blockaded by land and sea and surrendered in April 404 BC; its Long Walls were torn down and the Thirty Tyrants installed.",
          [T(1, "Greek city-states", "Achaemenid Empire")],
          [],
          [M(1, "Lysander", "Spartan fleet to the Hellespont", (27.3, 37.9), (26.3, 39.0), LAMPSACUS, AEGOSPOTAMI),
           M(1, "Lysander", "Blockade of Athens", AEGOSPOTAMI, (25.4, 39.4), (24.4, 38.2), PIRAEUS),
           M(1, "Pausanias", "Spartan army before Athens", SPARTA, ISTHMUS, ATHENS)],
          [E("Battle of Aegospotami", "battle", AEGOSPOTAMI[0], AEGOSPOTAMI[1], -405, 1,
             "Lysander captured the Athenian fleet on the beach, deciding the war."),
           E("Surrender of Athens", "treaty", ATHENS[0], ATHENS[1], -404, 1,
             "Athens gave up its fleet and empire and accepted Spartan rule.")]),
    ]))

# =================================================================== 7. Macedon and Alexander
wars.append(W(
    "macedon-and-alexander", "Rise of Macedon and the conquests of Alexander", -359, -323, "war",
    "Philip II turned Macedon from a weak frontier kingdom into the dominant power in Greece, crowning his work by defeating Athens and Thebes at Chaeronea in 338 BC. "
    "His son Alexander III led the Macedonian army and Greek allies against the Achaemenid Persian Empire, defeated Darius III at the Granicus, Issus and Gaugamela, and marched on to Central Asia and the Indus. "
    "When Alexander died at Babylon in 323 BC his empire broke up among his generals, but Greek culture spread from Egypt to India in the Hellenistic age.",
    [side("Macedon and Greek allies", "#7a4fb0", "Philip II", "Alexander the Great", "Parmenion", "Craterus", "Nearchus"),
     side("Athens, Thebes and Greek opponents", "#2f8f83", "Demosthenes", "Chares", "Theagenes"),
     side("Persian Empire and eastern rulers", "#b5452f", "Darius III", "Memnon of Rhodes", "Bessus", "Spitamenes", "Porus")],
    [(23.5, 39.5, 3.5), (34.0, 35.5, 7.0), (50.0, 33.5, 9.0), (67.0, 33.0, 8.0)],
    [
        S(-352, "359 to 348 BC", "Philip builds Macedon",
          "Philip II took over a kingdom just beaten by the Illyrians and rebuilt its army around the long sarissa pike and the Companion cavalry. "
          "He crushed the Illyrian king Bardylis in 358 BC, seized Amphipolis and its gold mines, won Thessaly at the Crocus Field in 352 BC and destroyed Olynthus in 348 BC. "
          "In Athens, Demosthenes began warning that Philip meant to master all of Greece.",
          [], [],
          [M(0, "Philip II", "Against the Illyrians", PELLA, (21.9, 40.9), LYNCESTIS),
           M(0, "Philip II", "Amphipolis and the Chalcidice", PELLA, THERMA, AMPHIPOLIS, OLYNTHUS),
           M(0, "Philip II", "Into Thessaly", PELLA, (22.3, 40.0), (22.4, 39.5), CROCUS)],
          [E("Defeat of Bardylis", "battle", LYNCESTIS[0], LYNCESTIS[1], -358, 0,
             "Philip's new army killed thousands of Illyrians and secured Upper Macedonia."),
           E("Battle of the Crocus Field", "battle", CROCUS[0], CROCUS[1], -352, 0,
             "Philip defeated the Phocians and became leader of Thessaly."),
           E("Fall of Olynthus", "siege", OLYNTHUS[0], OLYNTHUS[1], -348, 0,
             "Philip razed Olynthus, Athens' ally in the north, and sold its people into slavery.")]),
        S(-338, "339 to 337 BC", "Chaeronea",
          "When Philip marched south into central Greece, Demosthenes persuaded Athens and Thebes to stand together. "
          "At Chaeronea in Boeotia, Philip drew the Athenians forward with a feigned retreat while the 18-year-old Alexander broke the Theban line and the Sacred Band. "
          "Philip then united the Greek cities except Sparta in the League of Corinth, with himself as leader of a planned war on Persia.",
          [T(0, "Greek city-states")],
          [F("Chaeronea battle line", (22.8, 38.48), (22.84, 38.5), (22.88, 38.52))],
          [M(0, "Philip II", "Macedonian army south", PELLA, (22.4, 39.5), THERMOPYLAE, ELATEA, CHAERONEA),
           M(1, "Chares and Theagenes", "Athenians and Thebans", ATHENS, THEBES_GR, (23.0, 38.45), CHAERONEA)],
          [E("Battle of Chaeronea", "battle", CHAERONEA[0], CHAERONEA[1], -338, 0,
             "Philip and Alexander destroyed the allied army of Athens and Thebes, ending Greek independence."),
           E("League of Corinth", "treaty", CORINTH[0], CORINTH[1], -337, 0,
             "The Greek cities swore alliance under Macedonian leadership for a war against Persia.")]),
        S(-334, "336 to 334 BC", "Alexander crosses into Asia",
          "Philip was murdered in 336 BC, and the young Alexander crushed a revolt by razing Thebes. "
          "In 334 BC he crossed the Hellespont with about 40,000 men and routed the western satraps at the Granicus river. "
          "He marched down the coast freeing the Greek cities and took Halicarnassus, defended by the mercenary general Memnon of Rhodes.",
          [T(0, "Greek city-states"), T(2, "Achaemenid Empire")],
          [],
          [M(0, "Alexander", "Destruction of Thebes", PELLA, (22.4, 39.5), THERMOPYLAE, THEBES_GR),
           M(0, "Alexander", "Into Asia", PELLA, AMPHIPOLIS, (26.4, 40.6), ABYDOS, GRANICUS),
           M(0, "Alexander", "Down the Ionian coast", GRANICUS, SARDIS, MILETUS, HALICARNASSUS)],
          [E("Destruction of Thebes", "siege", THEBES_GR[0], THEBES_GR[1], -335, 0,
             "Alexander razed rebel Thebes as a warning to the rest of Greece."),
           E("Battle of the Granicus", "battle", GRANICUS[0], GRANICUS[1], -334, 0,
             "Alexander led his cavalry across the river and routed the army of the western satraps."),
           E("Siege of Halicarnassus", "siege", HALICARNASSUS[0], HALICARNASSUS[1], -334, 0,
             "Alexander took the city though Memnon's garrison held out in its citadels.")]),
        S(-333, "333 BC", "Issus",
          "After cutting the Gordian knot, Alexander passed through the Cilician Gates to the Syrian coast. "
          "Darius III brought the royal army from Babylon and came down behind him, but on the narrow plain of Issus Alexander's cavalry charge broke the Persian line. "
          "Darius fled, leaving his mother, wife and children in Macedonian hands.",
          [T(0, "Greek city-states"), T(2, "Achaemenid Empire")],
          [F("Pinarus river line", (36.13, 36.95), (36.2, 36.86), (36.27, 36.78))],
          [M(0, "Alexander", "Through Anatolia", HALICARNASSUS, (30.7, 36.9), GORDION, CILICIAN_GATES, ISSUS),
           M(2, "Darius III", "Royal army from Babylon", BABYLON, (40.1, 34.5), (38.0, 35.95), (36.65, 36.5), ISSUS)],
          [E("Battle of Issus", "battle", ISSUS[0], ISSUS[1], -333, 0,
             "Alexander's charge broke the Persian line and Darius fled the field.")]),
        S(-332, "332 to 331 BC", "Tyre and Egypt",
          "Rather than chase Darius, Alexander took the Mediterranean ports to neutralise the Persian fleet. "
          "Tyre fell after a seven-month siege and a mole built out to the island city, Gaza followed, and Egypt welcomed him as pharaoh. "
          "He founded Alexandria and visited the oracle of Ammon at Siwa.",
          [T(0, "Greek city-states"), T(2, "Achaemenid Empire")],
          [],
          [M(0, "Alexander", "March down the Levant", ISSUS, (35.85, 35.5), TYRE, GAZA, MEMPHIS),
           M(0, "Alexander", "To Alexandria and Siwa", MEMPHIS, ALEXANDRIA, (27.24, 31.35), SIWA)],
          [E("Siege of Tyre", "siege", TYRE[0], TYRE[1], -332, 0,
             "Alexander built a causeway to the island fortress and stormed it after seven months."),
           E("Siege of Gaza", "siege", GAZA[0], GAZA[1], -332, 0,
             "Gaza fell after two months, opening the road to Egypt."),
           E("Founding of Alexandria", "event", ALEXANDRIA[0], ALEXANDRIA[1], -331, 0,
             "The new city became the greatest port and centre of learning of the Hellenistic world.")]),
        S(-331, "331 to 330 BC", "Gaugamela and the fall of Persia",
          "Alexander crossed the Euphrates and Tigris to meet Darius' last great army on open ground near Gaugamela, and his oblique attack split the Persian line. "
          "Babylon and Susa surrendered, Alexander forced the Persian Gates and burned the palaces of Persepolis. "
          "Darius fled east and was murdered by his own satrap Bessus before Alexander could catch him.",
          [T(0, "Greek city-states"), T(2, "Achaemenid Empire")],
          [F("Gaugamela battle line", (43.4, 36.65), (43.45, 36.57), (43.5, 36.49))],
          [M(0, "Alexander", "Across Mesopotamia", TYRE, (36.7, 34.7), (38.2, 35.95), (42.0, 36.6), GAUGAMELA),
           M(0, "Alexander", "To Babylon, Susa and Persepolis", GAUGAMELA, BABYLON, SUSA, PERSIAN_GATE, PERSEPOLIS),
           M(2, "Darius III", "Flight to the east", GAUGAMELA, ECBATANA, (52.3, 35.5), HECATOMPYLOS)],
          [E("Battle of Gaugamela", "battle", GAUGAMELA[0], GAUGAMELA[1], -331, 0,
             "The decisive defeat of Darius III, which effectively ended Achaemenid rule."),
           E("Burning of Persepolis", "event", PERSEPOLIS[0], PERSEPOLIS[1], -330, 0,
             "Alexander's army burned the ceremonial palaces of the Persian kings."),
           E("Death of Darius III", "event", HECATOMPYLOS[0], HECATOMPYLOS[1], -330, None,
             "Bessus killed the fleeing king, and Alexander claimed his throne.")]),
        S(-327, "329 to 326 BC", "Bactria, Sogdiana and India",
          "Alexander crossed the Hindu Kush, caught Bessus and fought a hard guerrilla war against Spitamenes in Sogdiana, ending it by marrying the Sogdian noblewoman Roxana. "
          "He then entered the Punjab, where Taxila submitted, and beat King Porus and his war elephants at the Hydaspes. "
          "At the Hyphasis river his exhausted army refused to go further.",
          [T(0, "Greek city-states", "Achaemenid Empire"), T(2, "Hindu kingdoms")],
          [F("Hydaspes river line", (73.5, 33.1), (73.6, 32.85), (73.65, 32.6))],
          [M(0, "Alexander", "Over the Hindu Kush into Sogdiana", (62.2, 34.35), (69.2, 34.5), BACTRA, MARACANDA, JAXARTES),
           M(2, "Spitamenes", "Sogdian resistance", JAXARTES, MARACANDA, (64.4, 39.8)),
           M(0, "Alexander", "Into the Punjab", BACTRA, (69.2, 34.5), TAXILA, HYDASPES, HYPHASIS),
           M(2, "Porus", "Indian army at the Hydaspes", (74.4, 32.4), HYDASPES)],
          [E("Battle of the Jaxartes", "battle", JAXARTES[0], JAXARTES[1], -329, 0,
             "Alexander crossed the river under catapult cover and routed the Scythian horse archers."),
           E("Battle of the Hydaspes", "battle", HYDASPES[0], HYDASPES[1], -326, 0,
             "Alexander crossed the swollen river by night and defeated Porus, whom he kept as a vassal king."),
           E("Mutiny at the Hyphasis", "event", HYPHASIS[0], HYPHASIS[1], -326, None,
             "The army refused to march further east, and Alexander turned back.")]),
        S(-323, "325 to 323 BC", "Return and death",
          "The army sailed and marched down the Indus, then Alexander led part of it through the Gedrosian desert with heavy losses while Nearchus took the fleet along the coast to the Persian Gulf. "
          "Back in Babylon, Alexander planned new campaigns but died there in June 323 BC, aged 32, with no adult heir. "
          "His generals divided the empire and fought over it for forty years.",
          [T(0, "Empire of Alexander")],
          [],
          [M(0, "Alexander", "Down the Indus", HYDASPES, (71.6, 30.0), (68.9, 27.7), PATTALA),
           M(0, "Alexander", "Gedrosian desert march", PATTALA, (65.5, 25.8), (60.7, 27.2), (57.1, 30.0), PERSEPOLIS),
           M(0, "Nearchus", "Fleet along the coast", (67.4, 24.4), (61.5, 25.1), (57.6, 25.4), (56.5, 26.5), (50.0, 28.6)),
           M(0, "Alexander", "Return to Babylon", PERSEPOLIS, SUSA, BABYLON)],
          [E("Gedrosian desert march", "event", 63.0, 26.0, -325, None,
             "Thirst and heat killed a large part of the army and its followers."),
           E("Death of Alexander", "event", BABYLON[0], BABYLON[1], -323, None,
             "Alexander died of fever at Babylon, and his empire passed to his quarrelling generals.")]),
    ]))

# =================================================================== 8. Warring States
WS0 = [T(1, "Zhou states")]
WS1 = [T(0, "Qin"), T(1, "Zhou states")]
wars.append(W(
    "warring-states-qin-unification", "Warring States and the Qin unification of China", -475, -221, "conflict",
    "After the Zhou kings lost real power, seven large territorial states, Qin, Chu, Qi, Zhao, Wei, Han and Yan, fought for two and a half centuries with mass infantry armies and ever larger battles. "
    "Qin, on the western frontier, reformed itself under Shang Yang into a disciplined war state, broke its rivals one by one under generals such as Bai Qi, and between 230 and 221 BC King Ying Zheng conquered all six. "
    "He proclaimed himself Qin Shi Huang, the First Emperor, founding the unified imperial China that lasted two thousand years.",
    [side("Qin", "#b5452f", "Duke Xiao and Shang Yang", "Bai Qi", "Ying Zheng (Qin Shi Huang)", "Wang Jian", "Wang Ben"),
     side("The six rival states", "#2f8f83", "Sun Bin", "Yue Yi", "Lian Po", "Li Mu", "Lord Xinling", "Xiang Yan")],
    [(112.5, 34.8, 6.0), (117.5, 34.5, 4.0), (106.5, 32.0, 3.5)],
    [
        S(-453, "475 to 403 BC", "The partition of Jin",
          "The old great state of Jin was dominated by rival ministerial clans. "
          "In 453 BC the Zhi clan, besieging the Zhao at Jinyang, was betrayed by its allies Han and Wei, who joined Zhao to destroy it. "
          "Zhao, Han and Wei divided Jin among themselves and were recognised as states in 403 BC, the usual start of the Warring States era. "
          "The map's border data shows all the Chinese states as one polity before the 320s BC.",
          WS0, [],
          [M(1, "Zhi Yao", "Zhi siege of Jinyang", (111.2, 35.6), (111.9, 36.6), JINYANG),
           M(1, "Zhao Xiangzi", "Zhao defence and breakout", JINYANG, (112.2, 37.2))],
          [E("Siege of Jinyang", "war", JINYANG[0], JINYANG[1], -453, None,
             "Han and Wei turned on the Zhi clan, and the three survivors partitioned Jin.")]),
        S(-341, "356 to 340 BC", "Shang Yang's reforms and the fall of Wei",
          "Wei was the strongest state in the early 4th century BC. "
          "In Qin, Duke Xiao's minister Shang Yang abolished hereditary privilege, rewarded soldiers by heads taken and organised the peasants into a war economy. "
          "Wei's general Pang Juan was then destroyed by the Qi strategist Sun Bin at Maling in 341 BC, and the next year Shang Yang's Qin army took Wei's lands west of the Yellow River.",
          WS0, [],
          [M(1, "Pang Juan", "Wei army turns back from Han", XINZHENG, DALIANG, (115.0, 35.4), MALING),
           M(1, "Sun Bin and Tian Ji", "Qi feint and withdrawal", LINZI, (116.5, 36.1), (115.2, 35.4), MALING),
           M(0, "Shang Yang", "Qin attack on Wei's Hexi lands", XIANYANG, (110.0, 34.8), ANYI)],
          [E("Battle of Maling", "battle", MALING[0], MALING[1], -341, None,
             "Sun Bin ambushed and destroyed the Wei army, and Pang Juan was killed; the exact site is disputed."),
           E("Qin takes Hexi", "war", ANYI[0], ANYI[1], -340, 0,
             "Shang Yang beat Wei, which soon moved its capital east to Daliang.")]),
        S(-316, "318 to 316 BC", "Hangu Pass and the conquest of Shu",
          "Diplomats preached rival strategies: a vertical alliance of the eastern states against Qin, or horizontal alliances with Qin. "
          "In 318 BC a coalition led by Wei, Zhao, Han, Yan and Chu attacked the Hangu Pass and was thrown back. "
          "In 316 BC the Qin general Sima Cuo crossed the Qinling mountains and conquered Shu and Ba in Sichuan, giving Qin a vast and safe granary.",
          WS1,
          [F("Hangu Pass, 318 BC", (110.6, 35.3), HANGU, (110.9, 34.0))],
          [M(1, "Coalition of five states", "Coalition march on Hangu", DALIANG, XINZHENG, LUOYANG, HANGU),
           M(0, "Sima Cuo", "Conquest of Shu", XIANYANG, HANZHONG, JIANMEN, CHENGDU)],
          [E("Coalition defeated at Hangu Pass", "battle", HANGU[0], HANGU[1], -318, 0,
             "Qin held its eastern gateway and routed the allied armies."),
           E("Qin conquest of Shu", "war", CHENGDU[0], CHENGDU[1], -316, 0,
             "The rich Sichuan basin became Qin's base for wars against Chu.")]),
        S(-293, "293 BC", "Bai Qi at Yique",
          "Qin's greatest general, Bai Qi, first made his name against Han and Wei. "
          "At Yique, the gorge south of Luoyang, he defeated their combined army and, by Qin's own count, killed 240,000 men. "
          "From now on Qin bit off the Yellow River lands of its eastern neighbours piece by piece.",
          WS1,
          [F("Qin eastern front, 293 BC", (111.8, 35.4), (112.47, 34.55), (112.2, 33.6))],
          [M(0, "Bai Qi", "Qin army east from Xianyang", XIANYANG, HANGU, (111.8, 34.6), YIQUE),
           M(1, "Han and Wei generals", "Allied army of Han and Wei", XINZHENG, (113.0, 34.4), YIQUE)],
          [E("Battle of Yique", "battle", YIQUE[0], YIQUE[1], -293, 0,
             "Bai Qi annihilated the allied army of Han and Wei.")]),
        S(-284, "284 to 279 BC", "Yue Yi breaks Qi",
          "Qi had grown rich and aggressive under King Min. "
          "In 284 BC an alliance of Yan, Qin, Zhao, Wei and Han, led by the Yan general Yue Yi, routed Qi and sacked its capital Linzi, leaving only two Qi cities unconquered. "
          "Qi's commander Tian Dan broke out of Jimo in 279 BC with a famous attack by oxen with burning tails and recovered the state, but Qi never again threatened Qin.",
          WS1, [],
          [M(1, "Yue Yi", "Allied invasion of Qi", JI, (116.0, 38.3), (116.6, 36.7), LINZI),
           M(1, "Tian Dan", "Qi counteroffensive from Jimo", JIMO, (119.2, 36.6), LINZI, (116.6, 36.7))],
          [E("Sack of Linzi", "war", LINZI[0], LINZI[1], -284, None,
             "Yue Yi's coalition took the Qi capital, removing the one eastern power that rivalled Qin."),
           E("Fire oxen of Jimo", "battle", JIMO[0], JIMO[1], -279, None,
             "Tian Dan routed the Yan besiegers and Qi recovered its lost cities.")]),
        S(-278, "279 to 278 BC", "Bai Qi sacks Ying",
          "Qin now turned on Chu, the largest state, attacking down the Han river from the north and from Sichuan in the west. "
          "Bai Qi flooded the city of Yan by diverting a river and in 278 BC took the Chu capital Ying, burning the royal tombs. "
          "The Chu court fled east to Chen, and Qin held the middle Yangtze.",
          WS1,
          [F("Chu front, 278 BC", (111.0, 32.0), (112.2, 31.2), (113.2, 30.2))],
          [M(0, "Bai Qi", "Qin invasion of Chu", XIANYANG, (110.5, 33.4), (111.7, 32.5), YICHENG, YING),
           M(1, "King Qingxiang of Chu", "Chu court flees east", YING, (113.6, 31.6), CHEN)],
          [E("Sack of Ying", "siege", YING[0], YING[1], -278, 0,
             "Qin captured the Chu capital and turned its lands into Nan commandery.")]),
        S(-260, "262 to 256 BC", "Changping and the end of Zhou",
          "Qin and Zhao fought for the Shangdang upland. "
          "At Changping, Zhao replaced the cautious Lian Po with the young Zhao Kuo, who attacked, was surrounded by Bai Qi and starved for 46 days; Qin then killed most of the 400,000 prisoners, by tradition. "
          "Qin's siege of the Zhao capital Handan was broken in 257 BC by relief armies from Wei and Chu, but in 256 BC Qin ended the last Zhou king's line.",
          WS1,
          [F("Changping lines, 260 BC", (112.75, 35.95), CHANGPING, (113.0, 35.65))],
          [M(0, "Bai Qi", "Qin army into Shangdang", XIANYANG, (110.7, 35.3), (112.0, 35.7), CHANGPING),
           M(1, "Zhao Kuo", "Zhao army at Changping", HANDAN, (113.7, 36.2), CHANGPING),
           M(1, "Lord Xinling", "Wei relief of Handan", DALIANG, (114.4, 35.6), HANDAN)],
          [E("Battle of Changping", "battle", CHANGPING[0], CHANGPING[1], -260, 0,
             "Bai Qi destroyed the main Zhao army, the bloodiest battle of the era."),
           E("Relief of Handan", "siege", HANDAN[0], HANDAN[1], -257, 1,
             "Wei and Chu armies forced Qin to lift its siege of the Zhao capital."),
           E("End of the Zhou dynasty", "event", LUOYANG[0], LUOYANG[1], -256, 0,
             "Qin absorbed the tiny royal domain, ending the Zhou line after eight centuries.")]),
        S(-228, "230 to 225 BC", "Han, Zhao and Wei fall",
          "King Ying Zheng of Qin launched the final wars. Neishi Teng took the Han capital in 230 BC. "
          "Wang Jian invaded Zhao, which executed its best general Li Mu after Qin bribery, and Handan fell in 228 BC. "
          "In 225 BC Wang Ben flooded the Wei capital Daliang with the Yellow River until its walls collapsed.",
          WS1,
          [F("Qin front, 228 BC", (112.5, 38.8), (114.2, 37.5), (114.7, 35.6), (114.4, 34.2), (113.0, 33.0))],
          [M(0, "Neishi Teng", "Conquest of Han", XIANYANG, HANGU, LUOYANG, XINZHENG),
           M(0, "Wang Jian", "Invasion of Zhao", TAIYUAN, (113.6, 37.6), HANDAN),
           M(0, "Wang Ben", "Siege of Daliang", LUOYANG, (113.6, 34.8), DALIANG)],
          [E("Fall of Handan", "siege", HANDAN[0], HANDAN[1], -228, 0,
             "Qin captured the Zhao capital and King Qian of Zhao."),
           E("Siege of Daliang", "siege", DALIANG[0], DALIANG[1], -225, 0,
             "Qin flooded the Wei capital, modern Kaifeng, and forced its surrender.")]),
        S(-221, "225 to 221 BC", "Chu, Yan and Qi: unification",
          "Chu destroyed a first Qin invasion under Li Xin, so the king gave the veteran Wang Jian 600,000 men; he waited out Chu in fortified camps, then struck and killed its general Xiang Yan, taking Shouchun in 223 BC. "
          "Wang Ben finished off Yan in Liaodong and the Zhao remnant of Dai in 222 BC, and in 221 BC Qi surrendered without a battle. "
          "Ying Zheng took the new title Shi Huangdi, the First Emperor.",
          [T(0, "Qin", "Zhou states")],
          [],
          [M(0, "Wang Jian", "Conquest of Chu", DALIANG, CHEN, (117.0, 33.5), SHOUCHUN),
           M(0, "Wang Ben", "Yan, Liaodong and Dai", HANDAN, JI, (119.75, 40.0), LIAODONG),
           M(0, "Wang Ben", "March on Qi", JI, (116.8, 38.3), LINZI)],
          [E("Battle of Qinan", "battle", 117.0, 33.5, -224, 0,
             "Wang Jian destroyed the main Chu army; Xiang Yan was killed."),
           E("Fall of Shouchun", "siege", SHOUCHUN[0], SHOUCHUN[1], -223, 0,
             "Qin captured the Chu capital and King Fuchu, ending Chu as a state."),
           E("Surrender of Qi", "event", LINZI[0], LINZI[1], -221, 0,
             "King Jian of Qi gave up without a fight, completing the unification of China.")]),
    ]))

# =================================================================== 9. Kalinga War
KAL_FRONT = F("Kalinga frontier, c. 262 BC", (87.3, 21.7), (85.8, 21.9), (84.3, 21.2), (83.3, 19.6), (82.2, 17.3))
wars.append(W(
    "kalinga-war", "Kalinga War", -262, -261, "war",
    "The Mauryan emperor Ashoka invaded Kalinga, an independent kingdom on the Bay of Bengal coast in modern Odisha, around the eighth year of his reign. "
    "The conquest succeeded, but by Ashoka's own inscription some 100,000 people were killed and 150,000 deported. "
    "Ashoka's remorse turned him toward Buddhism and a policy of rule by dharma that he proclaimed on rock and pillar edicts across India.",
    [side("Mauryan Empire", "#c07a2e", "Ashoka"),
     side("Kalinga", "#2f6db5", "Kalinga army (rulers unnamed in the sources)")],
    [(85.0, 21.5, 4.5)],
    [
        S(-262, "c. 262 BC", "Ashoka turns on Kalinga",
          "Ashoka had inherited from his father Bindusara and grandfather Chandragupta an empire covering almost all of the subcontinent. "
          "Kalinga, a rich coastal kingdom between the Mahanadi and Godavari rivers with its own large army and sea trade, stayed outside it and controlled the routes to the south. "
          "The map's border data already includes Kalinga in the Mauryan Empire, so the frontier line marks the independent kingdom.",
          [T(0, "Mauryan Empire")],
          [KAL_FRONT],
          [M(0, "Ashoka", "Mauryan army marches from Pataliputra", PATALIPUTRA, (85.4, 24.0), (85.6, 22.5), (85.7, 21.3))],
          []),
        S(-261, "c. 261 BC", "Conquest of Kalinga",
          "The Mauryan army broke into Kalinga and took its heartland around Tosali, near modern Bhubaneswar. "
          "Local tradition places the decisive battle near the Dhauli hills on the Daya river, though no ancient source names the site. "
          "Ashoka's thirteenth rock edict counts 150,000 people deported, 100,000 killed and many times that number dead of other causes.",
          [T(0, "Mauryan Empire")],
          [KAL_FRONT],
          [M(0, "Ashoka", "Invasion of Kalinga", (85.7, 21.3), (85.8, 20.7), DHAULI),
           M(1, "Kalinga army", "Kalinga forces fall back on Tosali", JAUGADA, (85.2, 19.9), DHAULI)],
          [E("Battle of Kalinga (Dhauli, by tradition)", "battle", DHAULI[0], DHAULI[1], -261, 0,
             "Ashoka's army crushed Kalinga's resistance at enormous human cost.")]),
        S(-260, "c. 260 BC onward", "Ashoka's remorse",
          "Kalinga became a Mauryan province governed from Tosali. "
          "In his edicts Ashoka wrote that he felt deep sorrow for the suffering of the conquest, renounced further war, and turned to Buddhism and dharma, a code of nonviolence, tolerance and welfare. "
          "Edicts carved at Dhauli and Jaugada told Kalinga's officials to treat the people justly, and Ashoka sent Buddhist missions across Asia.",
          [T(0, "Mauryan Empire")],
          [],
          [M(0, "Ashoka", "Return to Pataliputra", DHAULI, (85.6, 22.5), (85.4, 24.0), PATALIPUTRA)],
          [E("Kalinga edicts", "event", DHAULI[0], DHAULI[1], -260, None,
             "Special rock edicts at Dhauli and Jaugada set out Ashoka's new policy for the conquered land.")]),
    ]))

out = os.path.join(H, "wars_g01.json")
with open(out, "w") as f:
    json.dump(wars, f, ensure_ascii=False, indent=1)
print("wrote", out, len(wars), "wars", sum(len(w["steps"]) for w in wars), "steps")

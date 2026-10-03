#!/usr/bin/env python3
"""Generator for wars_g06.json (group g06). Edit the data here, then rerun."""
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


# Frequently used places
KYOTO = (135.76, 35.01)
OSAKA = (135.526, 34.687)
EDO = (139.76, 35.69)
BUSAN = (129.04, 35.10)
SEOUL = (126.98, 37.57)
PYONGYANG = (125.75, 39.02)
LYON = (4.83, 45.76)
MILAN = (9.19, 45.46)
ROME = (12.48, 41.90)
NAPLES = (14.25, 40.85)
PARIS = (2.35, 48.86)
MOSCOW = (37.62, 55.75)
SANTIAGO = (-70.65, -33.45)
CONCEPCION = (-73.05, -36.82)
LISBON = (-9.14, 38.70)
COCHIN = (76.24, 9.97)
GOA = (73.91, 15.50)

wars = []

# ---------------------------------------------------------------- 1. Sengoku
wars.append({
    "id": "onin-war-sengoku",
    "name": "Onin War and the Sengoku era",
    "start": 1467, "end": 1615, "kind": "conflict",
    "summary": "The Onin War of 1467 to 1477 wrecked Kyoto and the authority of the Ashikaga shoguns, and Japan broke into the Sengoku, or warring states, era of rival daimyo. Three unifiers, Oda Nobunaga, Toyotomi Hideyoshi and Tokugawa Ieyasu, used firearms, castles and alliances to rebuild central power, and the Tokugawa victories at Sekigahara in 1600 and Osaka in 1615 brought two and a half centuries of peace.",
    "sides": [
        {"name": "Shogunate and the unifiers", "color": "#c0473a",
         "leaders": ["Hosokawa Katsumoto", "Oda Nobunaga", "Toyotomi Hideyoshi", "Tokugawa Ieyasu"]},
        {"name": "Rival daimyo and leagues", "color": "#3b6fb6",
         "leaders": ["Yamana Sozen", "Takeda Shingen", "Mori Terumoto", "Ishida Mitsunari", "Toyotomi Hideyori"]},
    ],
    "theater": [{"lon": 136.5, "lat": 35.2, "r": 4}, {"lon": 131.5, "lat": 33.0, "r": 2.5}],
    "steps": [
        S(1467, "1467-1477", "The Onin War",
          "A succession quarrel in the Ashikaga shogunate split the great lords into an Eastern Army under Hosokawa Katsumoto, which held the shogun, and a Western Army under Yamana Sozen. Ouchi Masahiro sailed from western Japan to join the Western Army, and ten years of fighting in the streets of Kyoto burned much of the capital. The war ended without a victor, but the shogun's authority over the provinces was gone.",
          territories=[],
          moves=[
              M(1, "Ouchi Masahiro", "Ouchi army to Kyoto", (131.47, 34.18), (132.5, 33.95), (133.9, 34.35), (135.18, 34.68), KYOTO),
              M(1, "Yamana Sozen", "Western Army from Tajima", (134.87, 35.46), (135.1, 35.3), (135.58, 35.01), KYOTO),
              M(0, "Hosokawa Katsumoto", "Eastern Army from Settsu", (135.5, 34.75), (135.68, 34.89), KYOTO),
          ],
          events=[
              E("Onin War in Kyoto", "war", 135.76, 35.03, 1467, None, "Rival armies fought for a decade inside the capital, leaving it in ruins."),
          ]),
        S(1560, "1543-1561", "Guns and warring daimyo",
          "With the shogun powerless, daimyo fought for whole provinces and vassals overthrew their lords. Portuguese traders landed on Tanegashima in 1543 and Japanese smiths were soon copying their arquebuses. In 1560 Imagawa Yoshimoto marched west along the Tokaido with a large army, but Oda Nobunaga of Owari surprised and killed him in a rainstorm at Okehazama.",
          territories=[],
          moves=[
              M(1, "Imagawa Yoshimoto", "Imagawa march west", (138.38, 34.98), (137.73, 34.71), (137.16, 34.95), (136.99, 35.06)),
              M(0, "Oda Nobunaga", "Raid from Kiyosu", (136.87, 35.22), (136.95, 35.13), (136.99, 35.06)),
          ],
          events=[
              E("Portuguese guns reach Tanegashima", "event", 130.98, 30.73, 1543, None, "Shipwrecked Portuguese traders introduced the arquebus, soon made in Japan in large numbers."),
              E("Battle of Okehazama", "battle", 136.99, 35.06, 1560, 0, "Nobunaga's small force killed Imagawa Yoshimoto in a surprise attack on his camp."),
              E("Battles of Kawanakajima", "battle", 138.19, 36.61, 1561, None, "Takeda Shingen and Uesugi Kenshin fought repeatedly for northern Shinano without a decision."),
          ]),
        S(1575, "1568-1580", "Nobunaga takes the centre",
          "Nobunaga marched on Kyoto in 1568 to install Ashikaga Yoshiaki as shogun, then deposed him in 1573 and ruled in his own name. Allied with Tokugawa Ieyasu, he faced a ring of enemies: the Takeda in the east, the Ikko-ikki Buddhist leagues of the Ishiyama Hongan-ji and the Mori in the west. At Nagashino in 1575 massed arquebus volleys behind palisades destroyed Takeda Katsuyori's cavalry, and in 1580 the Hongan-ji fortress finally surrendered.",
          fronts=[F("Oda-Tokugawa against Takeda, 1575", (137.0, 36.3), (137.45, 35.55), (137.8, 35.0), (138.05, 34.68))],
          moves=[
              M(0, "Oda Nobunaga", "March on Kyoto, 1568", (136.76, 35.43), (136.47, 35.37), (136.1, 35.1), KYOTO),
              M(0, "Oda Nobunaga and Tokugawa Ieyasu", "Relief of Nagashino", (137.16, 34.95), (137.4, 34.9), (137.5, 34.92)),
              M(1, "Takeda Katsuyori", "Takeda advance", (138.57, 35.66), (138.0, 35.8), (137.85, 35.4), (137.55, 34.95)),
          ],
          events=[
              E("Battle of Nagashino", "battle", 137.53, 34.92, 1575, 0, "Oda and Tokugawa gunners behind palisades broke the Takeda cavalry charges."),
              E("Siege of Ishiyama Hongan-ji", "siege", OSAKA[0], OSAKA[1], 1580, 0, "After ten years the Ikko-ikki fortress at Osaka surrendered to Nobunaga."),
          ]),
        S(1582, "1582", "Honno-ji and Hideyoshi's return",
          "In June 1582 Nobunaga's general Akechi Mitsuhide turned on him and Nobunaga died in the burning Honno-ji temple in Kyoto. Hashiba Hideyoshi, besieging the Mori castle of Takamatsu in Bitchu, made a quick peace and raced his army back east in about ten days. He crushed Akechi at Yamazaki and became Nobunaga's real heir.",
          fronts=[F("Oda against Mori, 1582", (133.6, 35.4), (133.75, 35.0), (133.85, 34.55))],
          moves=[
              M(0, "Hashiba (Toyotomi) Hideyoshi", "The great return", (133.82, 34.69), (134.69, 34.84), (135.2, 34.72), (135.42, 34.73), (135.68, 34.89)),
              M(1, "Akechi Mitsuhide", "Akechi on Kyoto", (135.58, 35.01), (135.75, 35.0), (135.68, 34.89)),
          ],
          events=[
              E("Honno-ji Incident", "event", 135.75, 35.0, 1582, 1, "Akechi Mitsuhide's troops surrounded the temple and Nobunaga took his own life."),
              E("Battle of Yamazaki", "battle", 135.68, 34.89, 1582, 0, "Hideyoshi defeated Akechi thirteen days after Nobunaga's death."),
          ]),
        S(1590, "1585-1590", "Hideyoshi unites Japan",
          "Hideyoshi built Osaka Castle, took the title of imperial regent and brought the last great independent houses to heel. In 1587 a huge army invaded Kyushu and forced the Shimazu to submit, and in 1590 he besieged the Hojo in Odawara with over 200,000 men until they surrendered. For the first time since the Onin War all of Japan answered to one ruler, who soon turned his armies against Korea.",
          territories=[T(0, "Japan (Warring States)")],
          moves=[
              M(0, "Toyotomi Hideyoshi", "Kyushu campaign, 1587", OSAKA, (133.9, 34.35), (131.0, 33.95), (130.7, 32.8), (130.3, 31.8)),
              M(0, "Toyotomi Hideyoshi", "Odawara campaign, 1590", KYOTO, (136.9, 35.15), (137.73, 34.71), (138.38, 34.98), (139.15, 35.25)),
          ],
          events=[
              E("Kyushu campaign", "war", 130.3, 31.8, 1587, 0, "The Shimazu submitted to Hideyoshi at Sendai after his armies overran Kyushu."),
              E("Siege of Odawara", "siege", 139.15, 35.25, 1590, 0, "The Hojo surrendered their great castle, completing the unification."),
          ]),
        S(1600, "1598-1600", "Sekigahara",
          "Hideyoshi's death in 1598 left a child heir, Hideyori, and a council of regents that split. Ishida Mitsunari raised a Western Army in the name of the Toyotomi with Mori Terumoto as nominal leader, while Tokugawa Ieyasu led the Eastern Army from Edo along the Tokaido. At Sekigahara in October 1600 the defection of Kobayakawa Hideaki during the battle gave Ieyasu a decisive victory.",
          territories=[T(0, "Japan (Warring States)")],
          fronts=[F("Eastern against Western Army, Sept 1600", (136.35, 36.1), (136.5, 35.45), (136.6, 35.0), (136.45, 34.4))],
          moves=[
              M(0, "Tokugawa Ieyasu", "Eastern Army", EDO, (139.15, 35.25), (138.38, 34.98), (137.16, 34.95), (136.75, 35.4), (136.47, 35.37)),
              M(0, "Tokugawa Hidetada", "Nakasendo column", EDO, (138.9, 36.35), (138.25, 36.40), (137.6, 35.9)),
              M(1, "Ishida Mitsunari", "Western Army", OSAKA, (135.76, 35.01), (136.27, 35.28), (136.61, 35.36), (136.45, 35.37)),
          ],
          events=[
              E("Battle of Sekigahara", "battle", 136.47, 35.37, 1600, 0, "Kobayakawa's switch of sides broke the Western Army in a single day."),
              E("Siege of Ueda", "siege", 138.25, 36.40, 1600, 1, "The Sanada held Hidetada's column so long that it missed Sekigahara."),
          ]),
        S(1615, "1603-1615", "Osaka and the Tokugawa peace",
          "Ieyasu became shogun in 1603 and ruled from Edo, but Hideyori still held Osaka Castle and drew masterless samurai to it. In the winter of 1614 Tokugawa armies besieged Osaka, made a truce and filled in its moats. In the summer of 1615 they returned, beat Sanada Yukimura's last charge and stormed the castle, and Hideyori died in the flames, ending the warring states era.",
          territories=[T(0, "Japan (Warring States)")],
          moves=[
              M(0, "Tokugawa Ieyasu", "Tokugawa armies to Osaka", (138.38, 34.98), (137.16, 34.95), (136.9, 35.15), KYOTO, (135.6, 34.75), OSAKA),
              M(0, "Tokugawa Hidetada", "Shogun's army from Edo", EDO, (139.15, 35.25), (137.73, 34.71), (136.47, 35.37), KYOTO),
          ],
          events=[
              E("Tokugawa shogunate founded", "event", EDO[0], EDO[1], 1603, 0, "Ieyasu took the title of shogun and made Edo his capital."),
              E("Siege of Osaka", "siege", OSAKA[0], OSAKA[1], 1615, 0, "The fall of Osaka Castle destroyed the Toyotomi line and the last rival to the Tokugawa."),
          ]),
    ],
})

# ---------------------------------------------------------------- 2. Italian Wars
wars.append({
    "id": "italian-wars",
    "name": "Italian Wars",
    "start": 1494, "end": 1559, "kind": "conflict",
    "summary": "A series of wars in which France and the Spanish and Habsburg monarchies fought for Naples, Milan and mastery of Italy, with Venice, the popes and the Swiss changing sides as it suited them. Spain won Naples by 1504, Charles V captured Francis I at Pavia in 1525, and his unpaid troops sacked Rome in 1527. The Peace of Cateau-Cambresis in 1559 left Spain dominant in Italy, and the wars spread Renaissance art and new military methods across Europe.",
    "sides": [
        {"name": "France and allies", "color": "#3b6fb6",
         "leaders": ["Charles VIII", "Louis XII", "Francis I", "Henry II", "Gaston de Foix"]},
        {"name": "Spain, the Habsburgs and allies", "color": "#c0473a",
         "leaders": ["Ferdinand of Aragon", "Gonzalo de Cordoba", "Charles V", "Philip II", "Emmanuel Philibert of Savoy"]},
    ],
    "theater": [{"lon": 11.0, "lat": 43.5, "r": 6}, {"lon": 3.5, "lat": 49.0, "r": 3}],
    "steps": [
        S(1494, "1494-1495", "Charles VIII marches on Naples",
          "Charles VIII of France crossed the Alps in 1494 to claim the Kingdom of Naples, with Milan's Ludovico Sforza inviting him in. Florence and Rome gave way and he entered Naples almost unopposed in February 1495. Alarmed, Venice, the Pope, Milan, Spain and Emperor Maximilian formed the League of Venice, and Charles had to fight his way home through their army at Fornovo.",
          territories=[T(0, "France", "Britany"), T(1, "Aragón", "Castille", "Venice", "Papal States")],
          moves=[
              M(0, "Charles VIII", "French invasion", LYON, (6.73, 44.93), (8.21, 44.90), (11.25, 43.77), ROME, NAPLES),
              M(0, "Charles VIII", "Return north", NAPLES, ROME, (11.33, 43.32), (9.88, 44.39), (10.10, 44.69)),
              M(1, "Francesco Gonzaga", "League of Venice army", (11.0, 45.2), (10.33, 44.80), (10.10, 44.69)),
          ],
          events=[
              E("French enter Naples", "event", NAPLES[0], NAPLES[1], 1495, 0, "Charles VIII took Naples without a real battle."),
              E("Battle of Fornovo", "battle", 10.10, 44.69, 1495, None, "The League failed to stop the French, who escaped north but lost their conquest."),
          ]),
        S(1503, "1499-1504", "Milan to France, Naples to Spain",
          "Louis XII seized Milan in 1499 and agreed to split Naples with Ferdinand of Aragon, but the partners soon fell out. Spain's Gonzalo de Cordoba, the Great Captain, used arquebusiers behind field works to defeat the French at Cerignola in 1503 and then beat them on the Garigliano. By the Treaty of Lyon in 1504 France kept Milan and Spain kept Naples for two centuries.",
          territories=[T(0, "France", "Britany"), T(1, "Aragón", "Castille")],
          moves=[
              M(0, "Gian Giacomo Trivulzio", "French conquest of Milan", (6.73, 44.93), (8.21, 44.90), MILAN),
              M(1, "Gonzalo de Cordoba", "The Great Captain", (16.28, 41.32), (15.90, 41.27), (15.0, 41.1), NAPLES, (13.76, 41.24)),
          ],
          events=[
              E("Battle of Cerignola", "battle", 15.90, 41.27, 1503, 1, "Spanish arquebus fire killed the French commander Nemours and broke his army."),
              E("Battle of the Garigliano", "battle", 13.76, 41.24, 1503, 1, "Gonzalo's winter crossing routed the French and sealed Spain's hold on Naples."),
          ]),
        S(1515, "1508-1516", "Cambrai, Ravenna and Marignano",
          "Alliances shifted quickly: the League of Cambrai crushed Venice at Agnadello in 1509, then Pope Julius II's Holy League turned on France. Gaston de Foix won a bloody victory at Ravenna in 1512 but died there, and the Swiss drove the French out of Milan. In 1515 the young Francis I crossed the Alps by a little used pass and, with Venetian help, smashed the Swiss pikemen at Marignano to retake Milan.",
          territories=[T(0, "France", "Britany", "Venice"), T(1, "Swiss Confederation", "Aragón", "Castille", "Papal States")],
          moves=[
              M(0, "Gaston de Foix", "Campaign of 1512", (11.34, 44.49), (11.9, 44.42), (12.20, 44.42)),
              M(0, "Francis I", "Crossing the Alps, 1515", LYON, (6.0, 45.0), (6.92, 44.40), (7.55, 44.39), (8.7, 45.3), (9.32, 45.37)),
              M(1, "Swiss pikemen", "Swiss over the Gotthard", (8.31, 47.05), (8.57, 46.56), (8.95, 46.0), MILAN, (9.32, 45.37)),
          ],
          events=[
              E("Battle of Agnadello", "battle", 9.55, 45.45, 1509, 0, "The French routed the Venetian army, nearly destroying Venice's mainland empire."),
              E("Battle of Ravenna", "battle", 12.20, 44.42, 1512, 0, "A French victory won by artillery, but Gaston de Foix was killed."),
              E("Battle of Marignano", "battle", 9.32, 45.37, 1515, 0, "Francis I's guns and cavalry broke the Swiss and won back Milan."),
          ]),
        S(1525, "1521-1526", "Pavia",
          "Charles V, heir to Spain, the Netherlands and Austria and elected emperor in 1519, now faced Francis I across all of France's borders. Imperial troops took Milan in 1521, and in the winter of 1524 Francis came back over the Alps and besieged Pavia. On 24 February 1525 the imperial relief army under Lannoy and Pescara routed the French and captured Francis himself, who signed away his claims in the Treaty of Madrid.",
          territories=[T(0, "France", "Britany"), T(1, "Castille", "Aragón", "Holy Roman Empire")],
          moves=[
              M(0, "Francis I", "French army to Pavia", LYON, (6.9, 45.2), (7.68, 45.07), MILAN, (9.16, 45.19)),
              M(1, "Charles de Lannoy", "Imperial relief army", (9.50, 45.31), (9.3, 45.25), (9.16, 45.19)),
          ],
          events=[
              E("Battle of Pavia", "battle", 9.16, 45.19, 1525, 1, "Spanish arquebusiers cut down the French knights and Francis I was taken prisoner."),
              E("Treaty of Madrid", "treaty", -3.70, 40.42, 1526, 1, "Francis gave up Milan and Burgundy to win his freedom, then repudiated the treaty."),
          ]),
        S(1527, "1526-1529", "Sack of Rome and the Ladies' Peace",
          "Pope Clement VII, Venice and Milan joined France in the League of Cognac. In May 1527 the unpaid imperial army of Spaniards and German Landsknechte under the Duke of Bourbon marched on Rome, and after Bourbon was shot on the walls they sacked the city for weeks. A French army under Lautrec besieged Naples in 1528, but plague and Andrea Doria's switch to Charles V ruined it, and the Peace of Cambrai in 1529 left Italy to the emperor.",
          territories=[T(0, "France", "Britany", "Venice", "Papal States"), T(1, "Castille", "Aragón", "Holy Roman Empire")],
          moves=[
              M(1, "Charles of Bourbon", "Imperial army on Rome", MILAN, (9.69, 45.05), (11.34, 44.49), (11.88, 43.46), (12.1, 42.42), ROME),
              M(0, "Lautrec", "French march on Naples", MILAN, (11.34, 44.49), (13.51, 43.62), (15.55, 41.46), NAPLES),
          ],
          events=[
              E("Sack of Rome", "event", ROME[0], ROME[1], 1527, 1, "Mutinous imperial troops looted Rome and held the Pope a prisoner."),
              E("Siege of Naples", "siege", NAPLES[0], NAPLES[1], 1528, 1, "Plague and the loss of Doria's fleet destroyed the French besiegers."),
              E("Peace of Cambrai", "treaty", 3.24, 50.18, 1529, 1, "The Ladies' Peace confirmed Habsburg control of Italy."),
          ]),
        S(1544, "1536-1544", "France and the Ottomans",
          "Francis I fought Charles V twice more, now allied with Sultan Suleiman. In 1543 a Franco-Ottoman fleet under Barbarossa besieged Nice, and in 1544 the French won at Ceresole in Piedmont. But Charles V and Henry VIII invaded France from the north and east that year, and the Peace of Crepy restored the deadlock.",
          territories=[T(0, "France", "Britany", "Ottoman Empire"),
                       T(1, "Spain", "Holy Roman Empire", "Habsburg Netherlands", "Naples", "Milan", "Sicily", "Sardinia", "England and Ireland")],
          moves=[
              M(0, "Hayreddin Barbarossa", "Ottoman fleet", (14.5, 40.6), (9.5, 41.5), (5.93, 43.12), (7.27, 43.68)),
              M(0, "Count of Enghien", "French in Piedmont", (7.66, 45.07), (7.72, 44.92), (7.83, 44.80)),
              M(1, "Charles V", "Imperial invasion of Champagne", (6.18, 49.12), (5.16, 48.77), (4.95, 48.64), (3.40, 49.05)),
          ],
          events=[
              E("Siege of Nice", "siege", 7.27, 43.70, 1543, None, "French and Ottoman forces took the town but not its citadel."),
              E("Battle of Ceresole", "battle", 7.83, 44.80, 1544, 0, "Enghien's French army beat the imperial army in Piedmont."),
              E("Peace of Crepy", "treaty", 3.25, 49.25, 1544, None, "Charles V and Francis I made peace without a winner."),
          ]),
        S(1557, "1551-1559", "Saint-Quentin and Cateau-Cambresis",
          "Henry II renewed the war, seizing Metz in 1552 and holding it against Charles V. After Charles abdicated, Philip II's army under Emmanuel Philibert of Savoy crushed the French at Saint-Quentin in 1557, while the Duke of Guise took Calais from Philip's English allies in 1558. Exhausted and bankrupt, both sides signed the Peace of Cateau-Cambresis in 1559, which gave up French claims in Italy and left Spain the master of the peninsula.",
          territories=[T(0, "France", "Britany"),
                       T(1, "Spain", "Habsburg Netherlands", "Naples", "Milan", "Sicily", "Sardinia", "England and Ireland")],
          fronts=[F("Franco-Habsburg frontier, 1557", (1.6, 50.8), (2.6, 50.3), (3.5, 50.0), (4.5, 49.9), (5.6, 49.5), (6.2, 49.1))],
          moves=[
              M(1, "Emmanuel Philibert of Savoy", "Spanish army from the Netherlands", (4.35, 50.85), (3.95, 50.45), (3.29, 49.85)),
              M(0, "Duke of Guise", "March on Calais", PARIS, (2.3, 49.9), (1.86, 50.95)),
          ],
          events=[
              E("Battle of Saint-Quentin", "battle", 3.29, 49.85, 1557, 1, "Philip II's army destroyed the French relief force and captured its commander."),
              E("Capture of Calais", "siege", 1.86, 50.95, 1558, 0, "Guise took England's last foothold in France."),
              E("Peace of Cateau-Cambresis", "treaty", 3.54, 50.10, 1559, 1, "France gave up its Italian ambitions, ending sixty five years of war."),
          ]),
    ],
})

# ---------------------------------------------------------------- 3. Spanish conquest
wars.append({
    "id": "spanish-conquest-aztec-maya-inca",
    "name": "Spanish conquest of the Aztec, Maya and Inca empires",
    "start": 1519, "end": 1533, "kind": "war",
    "summary": "Small bands of Spanish conquistadors under Hernan Cortes, Pedro de Alvarado and Francisco Pizarro overthrew the Aztec Empire, the highland Maya kingdoms of Guatemala and the Inca Empire. Steel, horses and guns mattered, but so did tens of thousands of native allies, smallpox and the Inca civil war. The conquests founded Spain's American empire and its flow of silver, and devastated the native peoples.",
    "sides": [
        {"name": "Spanish and native allies", "color": "#c0473a",
         "leaders": ["Hernan Cortes", "Pedro de Alvarado", "Francisco Pizarro"]},
        {"name": "Aztec, Maya and Inca states", "color": "#2e8b57",
         "leaders": ["Moctezuma II", "Cuauhtemoc", "Tecun Uman", "Atahualpa", "Huascar"]},
    ],
    "theater": [{"lon": -96.0, "lat": 18.0, "r": 6}, {"lon": -77.0, "lat": -8.5, "r": 8}],
    "steps": [
        S(1519, "1519", "Cortes lands in Mexico",
          "Hernan Cortes sailed from Cuba with about 500 men, landed on the Gulf coast and founded Veracruz. Allied with the Totonacs and, after hard fighting, with Tlaxcala, he marched inland and was received by Moctezuma II in Tenochtitlan, where he soon took the emperor hostage.",
          territories=[T(0, "Castille"), T(1, "Aztec Empire")],
          moves=[
              M(0, "Hernan Cortes", "Cortes' fleet from Cuba", (-84.9, 21.7), (-86.7, 20.9), (-86.8, 21.8), (-91.0, 21.3), (-96.0, 19.3)),
              M(0, "Hernan Cortes", "March to Tenochtitlan", (-96.13, 19.2), (-96.92, 19.54), (-98.24, 19.32), (-98.3, 19.06), (-99.13, 19.43)),
          ],
          events=[
              E("Alliance with Tlaxcala", "event", -98.24, 19.32, 1519, 0, "After losing several battles, the Tlaxcalans became Cortes' most important allies."),
          ]),
        S(1520, "1520", "Noche Triste and Otumba",
          "Cortes left the capital to defeat a rival Spanish force under Narvaez on the coast. A massacre of Aztec nobles by the men he left behind under Alvarado provoked a revolt, Moctezuma was killed, and the Spanish fought their way out of the city on the Noche Triste with heavy losses. They beat an Aztec army at Otumba on the way back to Tlaxcala.",
          territories=[T(0, "Castille"), T(1, "Aztec Empire")],
          moves=[
              M(0, "Hernan Cortes", "Cortes against Narvaez", (-99.13, 19.43), (-98.24, 19.32), (-96.4, 19.45)),
              M(0, "Hernan Cortes", "Retreat to Tlaxcala", (-99.15, 19.44), (-99.19, 19.48), (-98.75, 19.69), (-98.24, 19.32)),
          ],
          events=[
              E("Noche Triste", "battle", -99.15, 19.44, 1520, 1, "The Spanish lost hundreds of men and most of their treasure fleeing along the causeways."),
              E("Battle of Otumba", "battle", -98.75, 19.69, 1520, 0, "Cortes' cavalry charge killed the Aztec commander and broke the army blocking his retreat."),
          ]),
        S(1521, "1521", "Fall of Tenochtitlan",
          "Rebuilt with Tlaxcalan and other native allies, Cortes based himself at Texcoco and launched brigantines onto the lake to cut the island city off. After a siege of about 75 days, worsened by a smallpox epidemic, the emperor Cuauhtemoc was captured and Tenochtitlan fell in August 1521.",
          territories=[T(0, "Castille"), T(1, "Aztec Empire")],
          moves=[
              M(0, "Hernan Cortes", "Cortes to Texcoco", (-98.24, 19.32), (-98.6, 19.45), (-98.88, 19.51)),
              M(0, "Hernan Cortes", "Brigantines on Lake Texcoco", (-98.95, 19.48), (-99.05, 19.44), (-99.12, 19.43)),
          ],
          events=[
              E("Siege of Tenochtitlan", "siege", -99.13, 19.43, 1521, 0, "The Spanish and their allies starved and stormed the Aztec capital."),
          ]),
        S(1524, "1523-1525", "Alvarado in Guatemala",
          "From the ruins of Tenochtitlan, now rebuilt as Mexico City, the conquest spread outward. Pedro de Alvarado marched south with Spaniards and thousands of Nahua allies, defeated the K'iche' Maya near Quetzaltenango, where tradition says their leader Tecun Uman fell, and burned their capital Q'umarkaj. Cortes himself led a gruelling march across the Maya lowlands to Honduras.",
          territories=[T(0, "Castille", "Aztec Empire"), T(1, "Maya city-states")],
          moves=[
              M(0, "Pedro de Alvarado", "Alvarado to Guatemala", (-99.13, 19.43), (-96.72, 17.06), (-95.24, 16.32), (-92.3, 14.9), (-91.52, 14.84), (-91.17, 15.02)),
              M(0, "Hernan Cortes", "March to Honduras", (-99.13, 19.43), (-94.4, 18.1), (-92.9, 17.99), (-89.88, 16.93), (-88.6, 15.7), (-85.95, 15.92)),
          ],
          events=[
              E("Battle of El Pinar (Quetzaltenango)", "battle", -91.52, 14.84, 1524, 0, "Alvarado's cavalry routed the K'iche' army in the highlands."),
              E("Burning of Q'umarkaj", "event", -91.17, 15.02, 1524, 0, "Alvarado burned the K'iche' capital and its kings."),
          ]),
        S(1530, "c. 1527-1532", "Smallpox and the Inca civil war",
          "Smallpox spread ahead of the Spanish and killed the Inca ruler Huayna Capac and his heir around 1527. Two sons, Huascar in Cuzco and Atahualpa in Quito, fought a bitter civil war for the throne. Atahualpa's generals Quisquis and Chalcuchimac marched south and destroyed Huascar's army near Cuzco in 1532, just as Pizarro landed on the coast.",
          territories=[T(0, "Viceroyalty of New Spain", "Cuba (Spain)", "Hispaniola (Spain)"), T(1, "Inca Empire")],
          fronts=[F("Quito against Cuzco, c. 1530", (-80.0, -3.6), (-79.1, -4.5), (-78.4, -5.4))],
          moves=[
              M(1, "Quisquis and Chalcuchimac", "Atahualpa's army marches south", (-78.47, -0.18), (-79.0, -2.9), (-78.51, -7.16), (-75.5, -11.77), (-72.6, -13.6), (-71.97, -13.53)),
          ],
          events=[
              E("Death of Huayna Capac", "event", -78.47, -0.18, 1527, None, "The emperor died of a new disease, probably smallpox, leaving the succession open."),
              E("Battle of Quipaipan", "battle", -72.1, -13.5, 1532, None, "Atahualpa's generals crushed Huascar's army and captured him near Cuzco."),
          ]),
        S(1532, "1531-1532", "Pizarro and Cajamarca",
          "Francisco Pizarro sailed from Panama with fewer than 200 men and marched inland to meet the victorious Atahualpa at Cajamarca. There the Spanish ambushed the emperor's escort and seized Atahualpa, who was later executed despite filling a room with gold and silver as ransom.",
          territories=[T(0, "Viceroyalty of New Spain", "Cuba (Spain)", "Hispaniola (Spain)"), T(1, "Inca Empire")],
          moves=[
              M(0, "Francisco Pizarro", "Pizarro's voyage from Panama", (-79.5, 8.8), (-79.6, 7.0), (-80.5, 1.5), (-81.3, -2.2), (-80.55, -3.45)),
              M(0, "Francisco Pizarro", "March to Cajamarca", (-80.45, -3.57), (-80.63, -5.19), (-79.6, -6.5), (-78.51, -7.16)),
          ],
          events=[
              E("Battle of Cajamarca", "battle", -78.51, -7.16, 1532, 0, "Pizarro's surprise attack killed thousands of Atahualpa's attendants and captured the emperor."),
          ]),
        S(1533, "1533", "Cuzco",
          "After Atahualpa's execution, Pizarro marched south through Jauja toward the Inca capital, fighting off the army of the general Quisquis. Despite a sharp setback at Vilcaconga, the Spanish entered Cuzco in November 1533 and installed Manco Inca as a puppet ruler, though Inca resistance would continue for decades.",
          territories=[T(0, "Viceroyalty of New Spain", "Cuba (Spain)", "Hispaniola (Spain)", "Inca Empire")],
          moves=[
              M(0, "Francisco Pizarro", "March to Cuzco", (-78.51, -7.16), (-77.53, -9.53), (-75.5, -11.77), (-74.22, -13.16), (-71.97, -13.53)),
              M(1, "Quisquis", "Inca army falls back", (-75.5, -11.77), (-74.22, -13.16), (-72.44, -13.48)),
          ],
          events=[
              E("Battle of Vilcaconga", "battle", -72.44, -13.48, 1533, 1, "Inca troops ambushed the Spanish vanguard on a steep slope near Cuzco."),
              E("Capture of Cuzco", "event", -71.97, -13.53, 1533, 0, "Pizarro occupied the Inca capital and crowned Manco Inca as his puppet."),
          ]),
    ],
})

# ---------------------------------------------------------------- 4. Portuguese in the Indian Ocean
wars.append({
    "id": "portuguese-indian-ocean",
    "name": "Portuguese conquests in the Indian Ocean",
    "start": 1505, "end": 1515, "kind": "war",
    "summary": "After Vasco da Gama reached India, Portugal set out to seize the spice trade by force. Viceroys Francisco de Almeida and Afonso de Albuquerque used armed carracks and fortified ports to beat the Mamluk, Gujarati and Calicut fleets, and took Goa, Malacca and Hormuz. In ten years a small kingdom built a sea empire, the Estado da India, that controlled key choke points of Asian trade for a century.",
    "sides": [
        {"name": "Portugal", "color": "#2e7d6b",
         "leaders": ["Francisco de Almeida", "Afonso de Albuquerque", "Lourenco de Almeida"]},
        {"name": "Indian Ocean Muslim powers and Calicut", "color": "#b5653a",
         "leaders": ["Zamorin of Calicut", "Amir Husain al-Kurdi", "Malik Ayaz", "Yusuf Adil Shah", "Sultan Mahmud Shah of Malacca"]},
    ],
    "theater": [{"lon": 60.0, "lat": 10.0, "r": 22}, {"lon": 100.0, "lat": 3.0, "r": 6}],
    "steps": [
        S(1505, "1505", "Almeida's armada",
          "King Manuel I sent Francisco de Almeida as first viceroy of India with over 20 ships and orders to build forts. On the way he stormed the Swahili trading cities of Kilwa and Mombasa, which had resisted the Portuguese, then sailed on to India to fortify Anjediva, Cannanore and Cochin against the Zamorin of Calicut.",
          territories=[T(0, "Portugal"), T(1, "Islamic city-states")],
          moves=[
              M(0, "Francisco de Almeida", "Armada round Africa", LISBON, (-23.0, 15.0), (-20.0, -20.0), (18.5, -35.0), (40.8, -15.0), (39.51, -8.96)),
              M(0, "Francisco de Almeida", "Up the Swahili coast to India", (39.51, -8.96), (39.67, -4.05), (40.12, -3.22), (60.0, 8.0), (74.0, 14.75), COCHIN),
          ],
          events=[
              E("Sack of Kilwa", "siege", 39.51, -8.96, 1505, 0, "Almeida stormed Kilwa, installed a puppet ruler and built a fort."),
              E("Sack of Mombasa", "siege", 39.67, -4.05, 1505, 0, "The Portuguese burned and plundered Mombasa after hard street fighting."),
          ]),
        S(1509, "1508-1509", "Chaul and Diu",
          "The Mamluk sultan of Egypt, whose Red Sea trade was being strangled, sent a fleet under Amir Husain al-Kurdi to India, where it joined the Gujarati fleet of Malik Ayaz at Diu. They surprised and killed the viceroy's son Lourenco de Almeida at Chaul in 1508. In February 1509 Almeida took his revenge off Diu, where Portuguese gunnery destroyed the combined fleet and won control of the Arabian Sea.",
          territories=[T(0, "Portugal"), T(1, "Mamluke Sultanate", "Islamic states")],
          moves=[
              M(1, "Amir Husain al-Kurdi", "Mamluk fleet from Suez", (32.55, 29.9), (35.5, 25.5), (39.0, 21.0), (43.4, 12.6), (55.0, 15.5), (70.9, 20.6)),
              M(0, "Francisco de Almeida", "Viceroy's fleet", COCHIN, (75.35, 11.85), (73.15, 17.6), (72.9, 18.5), (70.98, 20.6)),
          ],
          events=[
              E("Battle of Chaul", "battle", 72.93, 18.55, 1508, 1, "The Mamluk and Gujarati fleets defeated a Portuguese squadron and killed Lourenco de Almeida."),
              E("Battle of Diu", "battle", 70.98, 20.71, 1509, 0, "Almeida's broadsides destroyed the Mamluk and Gujarati fleets."),
          ]),
        S(1510, "1510", "Albuquerque takes Goa",
          "Afonso de Albuquerque, the new governor, wanted a permanent base rather than allied ports. He seized Goa from the Sultanate of Bijapur in March 1510, was driven out in May by the army of Yusuf Adil Shah, and stormed it again in November. Goa became the capital of Portuguese Asia.",
          territories=[T(0, "Portugal"), T(1, "Bijapur", "Mamluke Sultanate", "Islamic states")],
          moves=[
              M(0, "Afonso de Albuquerque", "Albuquerque's fleet", COCHIN, (75.35, 11.85), (74.3, 14.0), GOA),
              M(1, "Yusuf Adil Shah", "Bijapur army retakes Goa", (75.71, 16.83), (74.9, 16.2), (74.3, 15.6), GOA),
          ],
          events=[
              E("Conquest of Goa", "siege", 73.91, 15.50, 1510, 0, "Albuquerque stormed Goa a second time and made it Portugal's capital in Asia."),
          ]),
        S(1511, "1511", "Malacca",
          "Albuquerque then sailed across the Bay of Bengal to Malacca, the great port that controlled the strait between the Indian Ocean and the South China Sea. After weeks of fighting he took the city in August 1511 and built the fortress of A Famosa, while Sultan Mahmud Shah fled south to continue the struggle from Bintan.",
          territories=[T(0, "Portugal"), T(1, "Malacca", "Mamluke Sultanate", "Islamic states")],
          moves=[
              M(0, "Afonso de Albuquerque", "Voyage to Malacca", COCHIN, (80.5, 6.0), (88.0, 5.5), (95.3, 5.8), (98.5, 4.0), (102.25, 2.19)),
              M(1, "Sultan Mahmud Shah", "Flight of the sultan", (102.25, 2.19), (103.4, 1.5), (104.5, 1.05)),
          ],
          events=[
              E("Capture of Malacca", "siege", 102.25, 2.19, 1511, 0, "Portugal seized the key to the spice trade with eastern Asia."),
          ]),
        S(1515, "1513-1515", "Aden and Hormuz",
          "To close the Red Sea, Albuquerque attacked Aden in 1513 but his ladders broke and the assault failed. In 1515 he turned to the Persian Gulf and took Hormuz, which he had first attacked in 1507, without a battle. He died at sea off Goa that December, leaving Portugal holding Goa, Malacca and Hormuz, the anchors of its sea empire.",
          territories=[T(0, "Portugal", "Malacca", "Muscat"), T(1, "Mamluke Sultanate", "Islamic states", "Yemen")],
          moves=[
              M(0, "Afonso de Albuquerque", "Attack on Aden, 1513", GOA, (60.0, 13.0), (52.0, 12.5), (45.03, 12.75)),
              M(0, "Afonso de Albuquerque", "Expedition to Hormuz, 1515", GOA, (66.0, 20.0), (59.0, 22.6), (57.2, 25.3), (56.46, 27.1)),
          ],
          events=[
              E("Siege of Aden", "siege", 45.03, 12.78, 1513, 1, "Aden's walls held and the Portuguese never closed the Red Sea."),
              E("Capture of Hormuz", "siege", 56.46, 27.07, 1515, 0, "Albuquerque took the island kingdom that controlled the Persian Gulf."),
          ]),
    ],
})

# ---------------------------------------------------------------- 5. German Peasants' War
wars.append({
    "id": "german-peasants-war",
    "name": "German Peasants' War",
    "start": 1524, "end": 1525, "kind": "war",
    "summary": "Inspired partly by the Reformation and angered by rising dues and lost rights, peasants and townspeople across southern and central Germany rose against their lords in Europe's largest popular revolt before 1789. The armed bands were poorly led and divided, and the Swabian League and the princes crushed them in a few weeks of 1525, killing perhaps 100,000 people. Luther sided with the princes, and the Reformation thereafter came under the control of rulers.",
    "sides": [
        {"name": "Peasant bands", "color": "#b5653a",
         "leaders": ["Thomas Muntzer", "Hans Muller von Bulgenbach", "Florian Geyer", "Gotz von Berlichingen", "Jacklein Rohrbach"]},
        {"name": "Swabian League and the princes", "color": "#3b6fb6",
         "leaders": ["Georg Truchsess von Waldburg", "Philip of Hesse", "George of Saxony", "Antoine of Lorraine"]},
    ],
    "theater": [{"lon": 9.5, "lat": 49.3, "r": 3.5}],
    "steps": [
        S(1524, "1524", "Revolt in the Black Forest",
          "In June 1524 peasants of the Stuhlingen lordship, near the Swiss border, refused their labour dues. Under Hans Muller von Bulgenbach the unrest spread across the Black Forest and the Hegau through the autumn, and bands marched to the Reformation town of Waldshut. The Swabian League's army was tied down in Italy, so the lords negotiated and waited.",
          territories=[T(1, "Holy Roman Empire")],
          moves=[
              M(0, "Hans Muller von Bulgenbach", "Black Forest band", (8.45, 47.75), (8.21, 47.62), (8.25, 47.9), (8.5, 48.05)),
          ],
          events=[
              E("Stuhlingen rising", "event", 8.45, 47.75, 1524, 0, "Peasants refusing their dues started the revolt."),
          ]),
        S(1525, "Mar-Apr 1525", "The Twelve Articles",
          "In early 1525 the revolt exploded in Upper Swabia, where the Baltringen, Lake and Allgau bands, perhaps 30,000 strong, met at Memmingen and issued the Twelve Articles, demanding an end to serfdom and the right to choose their own pastors. Georg Truchsess von Waldburg led the Swabian League's army out of Ulm, beat the Baltringen band at Leipheim and bought time with the Treaty of Weingarten.",
          territories=[T(1, "Holy Roman Empire")],
          moves=[
              M(1, "Georg Truchsess von Waldburg", "Swabian League army", (9.99, 48.40), (10.22, 48.45), (9.98, 47.91), (9.64, 47.81)),
              M(0, "Baltringen band", "Baltringen band", (9.83, 48.17), (10.1, 48.35), (10.22, 48.45)),
          ],
          events=[
              E("Twelve Articles of Memmingen", "event", 10.18, 47.99, 1525, 0, "The first written programme of rights for peasants in Europe."),
              E("Battle of Leipheim", "battle", 10.22, 48.45, 1525, 1, "The League's cavalry and guns scattered the Baltringen band."),
              E("Treaty of Weingarten", "treaty", 9.64, 47.81, 1525, 1, "The Lake and Allgau bands disbanded in return for promises of arbitration."),
          ]),
        S(1525, "Apr-May 1525", "Franconia and Thuringia rise",
          "The revolt spread north to Franconia, Wurttemberg, Alsace and Thuringia. At Weinsberg on Easter Day the Odenwald band under Jacklein Rohrbach killed Count Helfenstein and his knights, and the band forced the knight Gotz von Berlichingen to lead it. Florian Geyer's Black Company and other bands besieged the Marienberg fortress at Wurzburg, while the radical preacher Thomas Muntzer led the rising in Muhlhausen.",
          territories=[T(1, "Holy Roman Empire")],
          moves=[
              M(0, "Jacklein Rohrbach", "Odenwald band to Weinsberg", (9.22, 49.14), (9.29, 49.15)),
              M(0, "Gotz von Berlichingen", "Odenwald band to Wurzburg", (9.29, 49.15), (9.5, 49.35), (9.75, 49.6), (9.93, 49.79)),
              M(0, "Florian Geyer", "Black Company", (10.18, 49.38), (10.05, 49.6), (9.93, 49.79)),
              M(0, "Thomas Muntzer", "Muhlhausen band", (10.45, 51.21), (10.8, 51.3), (11.10, 51.36)),
          ],
          events=[
              E("Weinsberg massacre", "event", 9.29, 49.15, 1525, 0, "Peasants made Count Helfenstein and his men run the gauntlet to their deaths."),
              E("Siege of the Marienberg", "siege", 9.92, 49.79, 1525, 1, "The bishop's fortress at Wurzburg held out against the Franconian bands."),
          ]),
        S(1525, "May-Jun 1525", "The princes strike back",
          "Once the princes had concentrated their armies, the peasant bands were slaughtered one after another. Truchsess crushed the Wurttemberg peasants at Boblingen and the Franconians at Konigshofen, Duke Antoine of Lorraine massacred the Alsatians at Saverne, and Philip of Hesse and George of Saxony destroyed Muntzer's army at Frankenhausen. Muntzer was tortured and beheaded, and by the summer only Alpine risings in Salzburg and Tyrol were still fighting.",
          territories=[T(1, "Holy Roman Empire")],
          moves=[
              M(1, "Philip of Hesse", "Hessian army", (9.48, 51.31), (9.68, 50.55), (10.32, 50.98), (10.45, 51.21), (11.10, 51.36)),
              M(1, "Antoine of Lorraine", "Lorraine army", (6.18, 48.69), (6.9, 48.6), (7.36, 48.74)),
              M(1, "Georg Truchsess von Waldburg", "Swabian League army", (9.01, 48.68), (9.29, 49.15), (9.82, 49.54), (9.93, 49.79)),
          ],
          events=[
              E("Battle of Frankenhausen", "battle", 11.10, 51.36, 1525, 1, "About 6,000 peasants were killed and Muntzer was captured."),
              E("Massacre at Saverne", "battle", 7.36, 48.74, 1525, 1, "Lorraine's troops killed thousands of Alsatian peasants after their surrender."),
              E("Battle of Konigshofen", "battle", 9.82, 49.54, 1525, 1, "Truchsess destroyed the Odenwald and Franconian bands."),
          ]),
    ],
})

# ---------------------------------------------------------------- 6. French Wars of Religion
wars.append({
    "id": "french-wars-of-religion",
    "name": "French Wars of Religion",
    "start": 1562, "end": 1598, "kind": "war",
    "summary": "Eight civil wars between French Catholics and Protestant Huguenots, entangled with the rivalry of the great noble houses of Guise, Bourbon and Montmorency, tore France apart for 36 years. Massacres such as Saint Bartholomew's Day in 1572 deepened the hatred, and the death of the last Valois heirs made the Huguenot Henry of Navarre the heir to the throne. Henry IV fought the Catholic League and Spain, converted to Catholicism, and ended the wars with the Edict of Nantes in 1598.",
    "sides": [
        {"name": "Huguenots, then Henry IV's royalists", "color": "#3b6fb6",
         "leaders": ["Louis de Conde", "Gaspard de Coligny", "Henry of Navarre (Henry IV)"]},
        {"name": "Catholic party, the League and Spain", "color": "#c0473a",
         "leaders": ["Francis, Duke of Guise", "Catherine de Medici", "Henry, Duke of Anjou (Henry III)", "Henry, Duke of Guise", "Duke of Mayenne", "Alexander Farnese, Duke of Parma"]},
    ],
    "theater": [{"lon": 1.5, "lat": 47.0, "r": 5.5}],
    "steps": [
        S(1562, "1562-1563", "Vassy and Dreux",
          "The Regent Catherine de Medici's limited toleration of Protestants angered Catholic hardliners. In March 1562 the Duke of Guise's men massacred Huguenots worshipping at Vassy, and Louis de Conde seized Orleans as the Huguenot base. The royal Catholic army won the first great battle at Dreux in December, but Guise was assassinated while besieging Orleans and the Edict of Amboise restored an uneasy peace.",
          territories=[T(1, "France")],
          moves=[
              M(1, "Francis, Duke of Guise", "Guise to Paris", (4.95, 48.50), (3.9, 48.6), PARIS),
              M(0, "Louis de Conde", "Conde's army", PARIS, (1.91, 47.90), (2.2, 48.45), (1.37, 48.74)),
          ],
          events=[
              E("Massacre of Vassy", "event", 4.95, 48.50, 1562, 1, "Guise's soldiers killed dozens of Protestants at worship, starting the war."),
              E("Battle of Dreux", "battle", 1.37, 48.74, 1562, 1, "A costly Catholic victory in which both commanders, Conde and Montmorency, were captured."),
          ]),
        S(1569, "1567-1570", "Jarnac, Moncontour and Coligny's march",
          "War returned in 1567. In 1569 the king's brother Henry, Duke of Anjou, defeated the Huguenots at Jarnac, where Conde was killed, and again at Moncontour. Admiral Coligny saved the cause with a long march through the south and back up the Rhone to Burgundy, forcing the Peace of Saint-Germain, which gave the Huguenots fortified towns including La Rochelle.",
          territories=[T(1, "France")],
          moves=[
              M(1, "Henry, Duke of Anjou", "Royal army", PARIS, (1.9, 47.9), (0.34, 46.58), (-0.18, 45.68), (-0.02, 46.88)),
              M(0, "Gaspard de Coligny", "Coligny's march", (-0.02, 46.88), (0.0, 45.0), (1.35, 44.02), (3.9, 43.6), (4.6, 44.9), (4.48, 47.13)),
          ],
          events=[
              E("Battle of Jarnac", "battle", -0.18, 45.68, 1569, 1, "Conde was captured and killed after the battle."),
              E("Battle of Moncontour", "battle", -0.02, 46.88, 1569, 1, "Anjou destroyed Coligny's army in Poitou."),
              E("Peace of Saint-Germain", "treaty", 2.09, 48.90, 1570, 0, "The Huguenots gained freedom of worship in places and four security towns."),
          ]),
        S(1572, "1572-1573", "Saint Bartholomew's Day",
          "The wedding of the Protestant Henry of Navarre to the king's sister Marguerite brought Huguenot leaders to Paris. On 24 August 1572 Coligny and thousands of Protestants were murdered in Paris, and the killing spread to other towns. The survivors rallied at La Rochelle, which held out against a royal siege led by Anjou in 1573.",
          territories=[T(1, "France")],
          moves=[
              M(1, "Henry, Duke of Anjou", "Royal army to La Rochelle", PARIS, (1.9, 47.9), (0.34, 46.58), (-1.15, 46.16)),
          ],
          events=[
              E("Saint Bartholomew's Day massacre", "event", 2.35, 48.86, 1572, 1, "Several thousand Huguenots were killed in Paris and perhaps 10,000 across France."),
              E("Siege of La Rochelle", "siege", -1.15, 46.16, 1573, 0, "The Huguenot port held out and Anjou left to become king of Poland."),
          ]),
        S(1587, "1584-1589", "War of the Three Henrys",
          "When the last Valois heir died in 1584, the Huguenot Henry of Navarre became heir to the childless Henry III. Henry, Duke of Guise, led the Catholic League with Spanish money to stop him. Navarre beat the royal army at Coutras in 1587, the League drove Henry III out of Paris in 1588, and the king had Guise murdered at Blois, then joined Navarre before he too was assassinated in 1589.",
          territories=[T(1, "France")],
          fronts=[F("Huguenot south-west, c. 1587", (-1.2, 46.4), (0.3, 46.2), (1.5, 45.3), (2.5, 44.5), (3.5, 43.9), (4.5, 43.7))],
          moves=[
              M(1, "Duke of Joyeuse", "Royal army", PARIS, (1.9, 47.9), (0.34, 46.58), (0.15, 45.65), (-0.13, 45.04)),
              M(0, "Henry of Navarre", "Huguenot army", (-1.15, 46.16), (-0.63, 45.75), (-0.13, 45.04)),
              M(1, "Henry, Duke of Guise", "League army against the reiters", (4.0, 48.3), (2.8, 48.0), (1.77, 48.46)),
          ],
          events=[
              E("Battle of Coutras", "battle", -0.13, 45.04, 1587, 0, "Navarre's first great victory killed the royal commander Joyeuse."),
              E("Murder of Guise at Blois", "event", 1.33, 47.59, 1588, None, "Henry III had the League's leader killed in the royal chateau."),
              E("Assassination of Henry III", "event", 2.22, 48.84, 1589, 1, "A Dominican friar stabbed the king, making Navarre King Henry IV."),
          ]),
        S(1590, "1589-1594", "Henry IV against the League",
          "Henry IV, still a Protestant, faced the League under the Duke of Mayenne, with Paris and much of the north against him. He beat Mayenne at Arques and Ivry and starved Paris, until the Duke of Parma marched in from the Spanish Netherlands and lifted the siege. In 1593 Henry converted to Catholicism, and in March 1594 Paris opened its gates to him.",
          territories=[T(0, "England and Ireland"), T(1, "Spain", "Habsburg Netherlands", "Savoy")],
          moves=[
              M(0, "Henry IV", "Royal army", (1.08, 49.92), (1.13, 49.88), (1.46, 48.88), (2.45, 48.85)),
              M(1, "Duke of Mayenne", "League army", PARIS, (1.6, 49.5), (1.13, 49.88)),
              M(1, "Alexander Farnese, Duke of Parma", "Spanish relief of Paris", (4.35, 50.85), (3.95, 50.45), (3.3, 49.85), (2.88, 48.96), (2.45, 48.85)),
          ],
          events=[
              E("Battle of Ivry", "battle", 1.46, 48.88, 1590, 0, "Henry IV's cavalry routed Mayenne's larger army."),
              E("Siege of Paris", "siege", 2.35, 48.86, 1590, 1, "Parma's approach forced Henry to lift a siege that had starved the city."),
              E("Henry IV enters Paris", "event", 2.33, 48.86, 1594, 0, "After his conversion the capital accepted Henry as king."),
          ]),
        S(1598, "1595-1598", "Edict of Nantes",
          "Henry declared war on Spain in 1595 and beat a Spanish and League army at Fontaine-Francaise. The Spanish surprised and took Amiens in 1597, but Henry recaptured it, and the last League leader, Mercoeur in Brittany, submitted. In 1598 the Edict of Nantes gave the Huguenots freedom of worship and fortified towns, and the Peace of Vervins with Spain ended the wars.",
          territories=[T(0, "France", "Britany", "England and Ireland"), T(1, "Spain", "Habsburg Netherlands")],
          moves=[
              M(0, "Henry IV", "Royal army to Burgundy", PARIS, (3.6, 47.8), (5.04, 47.32), (5.37, 47.53)),
              M(0, "Henry IV", "Recapture of Amiens", PARIS, (2.2, 49.4), (2.30, 49.89)),
              M(1, "Hernan Tello de Portocarrero", "Spanish surprise of Amiens", (2.35, 50.16), (2.30, 49.89)),
          ],
          events=[
              E("Battle of Fontaine-Francaise", "battle", 5.37, 47.53, 1595, 0, "Henry's cavalry charge drove off a Spanish army in Burgundy."),
              E("Siege of Amiens", "siege", 2.30, 49.89, 1597, 0, "Henry retook the great city the Spanish had seized by a ruse."),
              E("Edict of Nantes", "treaty", -1.55, 47.22, 1598, None, "Toleration for the Huguenots ended 36 years of religious war."),
          ]),
    ],
})

# ---------------------------------------------------------------- 7. Russian conquest of Kazan, Astrakhan, Siberia
wars.append({
    "id": "russian-conquest-kazan-astrakhan-siberia",
    "name": "Russian conquest of Kazan, Astrakhan and Siberia",
    "start": 1552, "end": 1598, "kind": "war",
    "summary": "Ivan IV, the first crowned tsar, conquered the Tatar khanates of Kazan in 1552 and Astrakhan in 1556, giving Muscovy the whole Volga and a route to the Caspian. Crimean and Ottoman counterattacks burned Moscow in 1571 but were beaten at Molodi in 1572. Cossacks under Yermak then crossed the Urals and broke the Khanate of Sibir, opening the conquest of Siberia that turned Russia into a multiethnic Eurasian empire.",
    "sides": [
        {"name": "Tsardom of Muscovy", "color": "#3b6fb6",
         "leaders": ["Ivan IV", "Andrey Kurbsky", "Mikhail Vorotynsky", "Yermak Timofeyevich"]},
        {"name": "Tatar khanates and their Crimean and Ottoman allies", "color": "#2e8b57",
         "leaders": ["Yadegar Mokhammad of Kazan", "Devlet I Giray", "Kasim Pasha", "Kuchum Khan"]},
    ],
    "theater": [{"lon": 48.0, "lat": 52.0, "r": 9}, {"lon": 70.0, "lat": 57.0, "r": 8}],
    "steps": [
        S(1552, "1552", "Siege of Kazan",
          "After earlier campaigns failed, Ivan IV built the fortress of Sviyazhsk next to Kazan in 1551 and in 1552 led about 150,000 men down the Volga. The Russians besieged Kazan for six weeks, cut its water supply and blew breaches in the walls with gunpowder mines. They stormed the city on 2 October 1552 and captured Khan Yadegar Mokhammad.",
          territories=[T(0, "Tsardom of Muscovy"), T(1, "Kazan Khanate")],
          moves=[
              M(0, "Ivan IV", "Tsar's army", MOSCOW, (40.4, 56.13), (44.0, 56.33), (47.0, 56.1), (48.66, 55.77), (49.11, 55.79)),
          ],
          events=[
              E("Siege of Kazan", "siege", 49.11, 55.79, 1552, 0, "Mines and assault took Kazan, ending the khanate."),
          ]),
        S(1556, "1554-1556", "Astrakhan and the Volga",
          "With Kazan gone, Russian forces sailed down the Volga in 1554 and installed a client khan in Astrakhan. When he changed sides, a second expedition annexed the city in 1556. Muscovy now held the whole course of the Volga to the Caspian, and the Nogai Horde under Ismail became its client.",
          territories=[T(0, "Tsardom of Muscovy", "Kazan Khanate"), T(1, "Astrakhan Khanate")],
          moves=[
              M(0, "Yury Pronsky-Shemyakin", "Down the Volga", (49.11, 55.79), (49.9, 53.2), (46.0, 51.5), (44.5, 48.7), (48.03, 46.35)),
          ],
          events=[
              E("Annexation of Astrakhan", "siege", 48.03, 46.35, 1556, 0, "Russia took the last Volga khanate almost without fighting."),
          ]),
        S(1571, "1569-1572", "Crimean and Ottoman counterattack",
          "The Ottomans sent Kasim Pasha to take Astrakhan in 1569 and dig a canal from the Don to the Volga, but the plan collapsed. In 1571 Khan Devlet I Giray of Crimea slipped past the Oka defences and burned Moscow. When he returned in 1572 to finish the job, Prince Mikhail Vorotynsky's army destroyed his horde at Molodi, saving the Volga conquests.",
          territories=[T(0, "Tsardom of Muscovy", "Kazan Khanate", "Astrakhan Khanate", "Nogai Horde"), T(1, "Crimean Khanate", "Ottoman Empire")],
          fronts=[F("Great Abatis Line on the Oka", (33.9, 53.3), (35.9, 53.8), (37.6, 54.2), (39.7, 54.6), (41.2, 54.4))],
          moves=[
              M(1, "Kasim Pasha", "Ottoman Astrakhan expedition", (39.42, 47.11), (41.5, 47.7), (43.5, 48.7), (45.5, 47.5), (48.03, 46.35)),
              M(1, "Devlet I Giray", "Crimean raid on Moscow", (33.86, 44.75), (33.7, 46.15), (36.0, 50.0), (37.6, 54.2), MOSCOW),
              M(0, "Mikhail Vorotynsky", "Russian field army", (38.0, 54.95), (37.6, 55.1), (37.48, 55.27)),
          ],
          events=[
              E("Ottoman siege of Astrakhan", "siege", 48.03, 46.35, 1569, 0, "The Ottoman expedition gave up and retreated across the steppe."),
              E("Burning of Moscow", "event", 37.62, 55.75, 1571, 1, "Devlet Giray's Tatars set fire to the capital, killing many thousands."),
              E("Battle of Molodi", "battle", 37.48, 55.27, 1572, 0, "Vorotynsky's mobile fortress and guns destroyed the Crimean army south of Moscow."),
          ]),
        S(1582, "1581-1582", "Yermak crosses the Urals",
          "The Stroganov merchant family hired a band of about 800 Cossacks under Yermak Timofeyevich to guard their Ural lands. In 1581 to 1582 Yermak led them by river boats over the Urals into the Khanate of Sibir. Firearms won the battle at Chuvash Cape on the Irtysh, and Khan Kuchum abandoned his capital Qashliq.",
          territories=[T(0, "Tsardom of Muscovy", "Kazan Khanate", "Astrakhan Khanate", "Nogai Horde"), T(1, "Khanate of Sibir")],
          moves=[
              M(0, "Yermak Timofeyevich", "Cossack river expedition", (57.8, 58.3), (59.9, 57.9), (65.5, 57.15), (68.2, 58.2), (68.4, 58.1)),
              M(1, "Kuchum Khan", "Kuchum withdraws", (68.4, 58.1), (69.4, 57.4), (70.5, 56.5)),
          ],
          events=[
              E("Battle of Chuvash Cape", "battle", 68.35, 58.08, 1582, 0, "Cossack gunfire broke Kuchum's army on the Irtysh."),
              E("Capture of Qashliq", "event", 68.40, 58.12, 1582, 0, "Yermak occupied the Siberian khan's capital."),
          ]),
        S(1598, "1585-1598", "The fall of Sibir",
          "Kuchum fought on, and in 1585 he ambushed and killed Yermak on the Irtysh. But Moscow sent streltsy and founded forts at Tyumen in 1586, Tobolsk in 1587 and Tara in 1594. In 1598 Andrei Voeikov surprised Kuchum's camp on the Ob near the Irmen river, and the old khan fled to die among the Nogais, leaving western Siberia to Russia.",
          territories=[T(0, "Tsardom of Muscovy", "Kazan Khanate", "Astrakhan Khanate", "Nogai Horde", "Khanate of Sibir")],
          moves=[
              M(0, "Andrei Voeikov", "Expedition from Tara", (74.4, 56.9), (77.5, 55.6), (80.5, 55.0), (81.9, 54.4)),
              M(1, "Kuchum Khan", "Kuchum's flight", (81.9, 54.4), (78.0, 52.0), (72.0, 50.0)),
          ],
          events=[
              E("Death of Yermak", "battle", 69.4, 57.9, 1585, 1, "Kuchum's warriors surprised Yermak's camp at night and he drowned in the Irtysh."),
              E("Founding of Tobolsk", "event", 68.25, 58.20, 1587, 0, "The new fort became the capital of Russian Siberia."),
              E("Battle of the Irmen", "battle", 81.9, 54.4, 1598, 0, "Voeikov destroyed Kuchum's last army, ending the khanate."),
          ]),
    ],
})

# ---------------------------------------------------------------- 8. Arauco War
BIOBIO = F("Biobio frontier", (-73.15, -36.8), (-72.8, -37.0), (-72.4, -37.3), (-71.9, -37.5), (-71.4, -37.6))
wars.append({
    "id": "arauco-war",
    "name": "Arauco War",
    "start": 1536, "end": 1656, "kind": "conflict",
    "summary": "For more than a century the Mapuche of southern Chile fought off Spanish conquest, the longest war of resistance in colonial America. Leaders such as Lautaro, Caupolican and Pelantaro killed two governors and destroyed the Spanish cities south of the Biobio river in 1598 to 1604. The war settled into a fortified frontier along the Biobio, recognised in parliaments with the Spanish, and Araucania stayed independent until the 1880s.",
    "sides": [
        {"name": "Spanish Chile", "color": "#c0473a",
         "leaders": ["Pedro de Valdivia", "Francisco de Villagra", "Garcia Hurtado de Mendoza", "Alonso de Ribera"]},
        {"name": "Mapuche", "color": "#2e8b57",
         "leaders": ["Michimalonco", "Lautaro", "Caupolican", "Pelantaro", "Lientur"]},
    ],
    "theater": [{"lon": -72.0, "lat": -36.5, "r": 5.5}],
    "steps": [
        S(1541, "1536-1541", "First contact and Santiago",
          "Diego de Almagro's expedition from Peru reached central Chile in 1536 and fought the Mapuche at Reynoguelen on the Itata river before turning back. Pedro de Valdivia came south in 1540 and founded Santiago in 1541. Months later the chief Michimalonco attacked and burned the new town, which survived only by desperate defence.",
          territories=[T(0, "Inca Empire"), T(1, "Andean hunter-gatherers")],
          moves=[
              M(0, "Diego de Almagro", "Almagro's expedition, 1536", (-71.97, -13.53), (-69.2, -16.5), (-66.0, -22.5), (-68.5, -27.0), (-70.33, -27.37), (-70.7, -32.8)),
              M(0, "Pedro de Valdivia", "Valdivia's march, 1540", (-71.97, -13.53), (-71.54, -16.4), (-70.3, -18.5), (-68.2, -22.9), (-70.33, -27.37), SANTIAGO),
          ],
          events=[
              E("Battle of Reynoguelen", "battle", -72.3, -36.6, 1536, 0, "Almagro's men under Gomez de Alvarado fought the first battle with the Mapuche."),
              E("Founding of Santiago", "event", SANTIAGO[0], SANTIAGO[1], 1541, 0, "Valdivia founded the capital of Spanish Chile."),
              E("Destruction of Santiago", "battle", -70.66, -33.43, 1541, 1, "Michimalonco's warriors burned the town while Valdivia was away."),
          ]),
        S(1550, "1550-1553", "Valdivia invades Araucania",
          "Valdivia pushed south into the Mapuche heartland, won at Andalien in 1550 and founded Concepcion, La Imperial, Valdivia and Villarrica, with forts at Arauco, Tucapel and Puren. The Spanish divided the land and people into encomiendas and forced Mapuche to work the gold washings, which built up fierce resentment.",
          territories=[T(0, "Inca Empire"), T(1, "Andean hunter-gatherers")],
          moves=[
              M(0, "Pedro de Valdivia", "Conquest of the south", SANTIAGO, (-71.6, -35.4), (-72.99, -36.74), (-73.17, -38.71), (-73.24, -39.81)),
              M(1, "Ainavillo", "Mapuche army", (-72.6, -37.5), (-72.8, -37.0), (-72.95, -36.80)),
          ],
          events=[
              E("Battle of Andalien", "battle", -72.95, -36.80, 1550, 0, "The Spanish beat a large Mapuche army and founded Concepcion."),
              E("Founding of Valdivia", "event", -73.24, -39.81, 1552, 0, "Valdivia's southernmost city on the river that bears his name."),
          ]),
        S(1554, "1553-1557", "Lautaro",
          "Lautaro, a young Mapuche who had served as Valdivia's groom and learned Spanish tactics, organised the warriors into disciplined squadrons. At Tucapel in December 1553 they wiped out Valdivia's column and killed the governor. Lautaro beat Francisco de Villagra at Marihuenu, forced the Spanish to abandon Concepcion, and marched north toward Santiago before Villagra surprised and killed him at Mataquito in 1557.",
          territories=[T(0, "Inca Empire"), T(1, "Andean hunter-gatherers")],
          moves=[
              M(1, "Lautaro", "Lautaro's campaigns", (-73.38, -37.8), (-73.15, -37.1), (-73.0, -36.8), (-72.3, -36.3), (-71.9, -35.0)),
              M(0, "Francisco de Villagra", "Villagra from Santiago", SANTIAGO, (-71.2, -34.3), (-71.9, -35.0)),
          ],
          events=[
              E("Battle of Tucapel", "battle", -73.38, -37.80, 1553, 1, "Lautaro's squadrons annihilated Valdivia's force and the governor was killed."),
              E("Battle of Marihuenu", "battle", -73.15, -37.10, 1554, 1, "Villagra was routed and Concepcion was evacuated."),
              E("Battle of Mataquito", "battle", -71.9, -35.0, 1557, 0, "Villagra's dawn attack killed Lautaro."),
          ]),
        S(1558, "1557-1561", "Garcia Hurtado de Mendoza",
          "The viceroy of Peru sent his son Garcia Hurtado de Mendoza by sea with fresh troops. He landed at Concepcion, beat the Mapuche at Lagunillas and Millarapue, and refounded forts in Arauco. The war chief Caupolican was captured in 1558 and executed by impalement at Canete, but the resistance did not end.",
          territories=[T(0, "Inca Empire"), T(1, "Andean hunter-gatherers")],
          moves=[
              M(0, "Garcia Hurtado de Mendoza", "Fleet from Lima", (-77.15, -12.05), (-76.5, -16.0), (-72.0, -25.0), (-71.6, -30.0), (-72.9, -35.0), (-73.05, -36.74)),
              M(0, "Garcia Hurtado de Mendoza", "Campaign in Arauco", CONCEPCION, (-73.3, -37.25), (-73.38, -37.8)),
              M(1, "Caupolican", "Mapuche army", (-72.9, -38.15), (-73.2, -37.7), (-73.32, -37.38)),
          ],
          events=[
              E("Battle of Millarapue", "battle", -73.32, -37.38, 1557, 0, "Garcia Hurtado's army defeated Caupolican's attack."),
              E("Execution of Caupolican", "event", -73.40, -37.80, 1558, 0, "The captured war chief was impaled at Canete."),
          ]),
        S(1599, "1598-1604", "Curalaba and the fall of the seven cities",
          "In December 1598 the Mapuche under Pelantaro ambushed Governor Martin Garcia Onez de Loyola at Curalaba and killed him with nearly all his men. A general rising followed, and within six years every Spanish town south of the Biobio, including Valdivia, La Imperial, Villarrica and Osorno, was destroyed or abandoned. Governor Alonso de Ribera created a standing professional army to hold a fortified line on the Biobio.",
          territories=[T(0, "Inca Empire"), T(1, "Andean hunter-gatherers")],
          fronts=[BIOBIO],
          moves=[
              M(0, "Martin Garcia Onez de Loyola", "Governor's column", (-73.17, -38.71), (-72.95, -38.4), (-72.9, -38.15)),
              M(1, "Pelantaro", "Mapuche offensive", (-72.9, -38.15), (-73.0, -39.0), (-73.24, -39.81)),
              M(0, "Alonso de Ribera", "Ribera's frontier army", SANTIAGO, (-71.6, -35.4), CONCEPCION, (-72.4, -37.3)),
          ],
          events=[
              E("Disaster of Curalaba", "battle", -72.9, -38.15, 1598, 1, "Pelantaro's warriors killed the governor and his escort."),
              E("Destruction of Valdivia", "siege", -73.24, -39.81, 1599, 1, "A Mapuche attack sacked and burned the city."),
              E("Fall of Osorno", "siege", -73.13, -40.57, 1604, 1, "The last Spanish city in the south was abandoned after a long siege."),
          ]),
        S(1612, "1608-1626", "Slave raids and the Defensive War",
          "The Spanish crown legalised the enslavement of Mapuche captives in 1608, and raids across the frontier multiplied. The Jesuit Luis de Valdivia persuaded the king to try a Defensive War from 1612, with the Biobio as a fixed border and missions instead of raids. The killing of three Jesuits at Elicura in 1612 and continued raiding ended the experiment in 1626.",
          territories=[T(0, "Inca Empire"), T(1, "Andean hunter-gatherers")],
          fronts=[BIOBIO],
          moves=[
              M(0, "Luis de Valdivia", "Jesuit mission to Elicura", CONCEPCION, (-73.4, -37.25), (-73.25, -37.85)),
              M(1, "Anganamon", "Mapuche raid", (-72.8, -38.3), (-73.1, -38.0), (-73.25, -37.85)),
          ],
          events=[
              E("Defensive War proclaimed", "treaty", -73.05, -36.82, 1612, None, "The crown ordered the frontier to stay on the Biobio."),
              E("Martyrs of Elicura", "event", -73.25, -37.85, 1612, 1, "Three Jesuit missionaries were killed by the chief Anganamon's warriors."),
          ]),
        S(1641, "1629-1641", "Las Cangrejeras and Quillin",
          "Open war resumed. In 1629 the Mapuche under Lientur won at Las Cangrejeras and captured the young officer Francisco Nunez de Pineda, whose memoir of his captivity became a classic. Governor Francisco Lopez de Zuniga, Marquis of Baides, then met the Mapuche chiefs in the Parliament of Quillin in 1641, which recognised the Biobio as the border and Mapuche independence south of it.",
          territories=[T(0, "Inca Empire"), T(1, "Andean hunter-gatherers")],
          fronts=[BIOBIO],
          moves=[
              M(1, "Lientur", "Raid north of the Biobio", (-72.6, -37.6), (-72.4, -37.2), (-72.3, -36.9)),
              M(0, "Marquis of Baides", "Governor to Quillin", CONCEPCION, (-72.4, -37.3), (-72.75, -38.35)),
          ],
          events=[
              E("Battle of Las Cangrejeras", "battle", -72.3, -36.9, 1629, 1, "Lientur's warriors destroyed a Spanish column near Yumbel."),
              E("Parliament of Quillin", "treaty", -72.75, -38.35, 1641, None, "Spain and the Mapuche agreed on the Biobio frontier."),
          ]),
        S(1655, "1655-1656", "The great rising of 1655",
          "Slave raids under Governor Antonio de Acuna y Cabrera provoked a massive Mapuche and Huilliche uprising in February 1655. The rebels overran estates and forts between the Biobio and the Maule and burned Chillan, and the panic led the people of Concepcion to depose the governor. The rising faded by 1656 without changing the frontier, which stayed on the Biobio for the rest of the colonial era.",
          territories=[T(0, "Viceroyalty of Peru"), T(1, "Andean hunter-gatherers")],
          fronts=[BIOBIO],
          moves=[
              M(1, "Clentaru", "Mapuche rising", (-72.7, -38.0), (-72.4, -37.3), (-72.3, -36.9), (-72.1, -36.6)),
          ],
          events=[
              E("Uprising of 1655", "war", -72.4, -37.3, 1655, 1, "Mapuche forces overran the Spanish frontier forts."),
              E("Burning of Chillan", "siege", -72.1, -36.6, 1655, 1, "The rebels destroyed the town north of the Biobio."),
          ]),
    ],
})

# ---------------------------------------------------------------- 9. Imjin War
wars.append({
    "id": "imjin-war",
    "name": "Imjin War: Japan's invasions of Korea",
    "start": 1592, "end": 1598, "kind": "war",
    "summary": "Having united Japan, Toyotomi Hideyoshi sent huge armies to conquer Korea as a road to Ming China. Japanese troops took Seoul and Pyongyang within weeks, but Admiral Yi Sun-sin's navy cut their supply lines, Korean righteous armies rose behind them, and a Ming army drove them back to the south coast. A second invasion in 1597 stalled, and after Hideyoshi's death in 1598 the Japanese withdrew, leaving Korea devastated.",
    "sides": [
        {"name": "Japan", "color": "#c0473a",
         "leaders": ["Toyotomi Hideyoshi", "Konishi Yukinaga", "Kato Kiyomasa", "Ukita Hideie", "Shimazu Yoshihiro"]},
        {"name": "Joseon Korea and Ming China", "color": "#3b6fb6",
         "leaders": ["Yi Sun-sin", "Kwon Yul", "Li Rusong", "Chen Lin"]},
    ],
    "theater": [{"lon": 127.6, "lat": 37.0, "r": 5}],
    "steps": [
        S(1592, "May-Jul 1592", "The Japanese blitz",
          "In May 1592 about 160,000 Japanese troops landed at Busan. Konishi Yukinaga and Kato Kiyomasa raced north by separate roads, routed the Korean army at Chungju, took Seoul within three weeks and Pyongyang in July, while Kato pushed into the far north-east. King Seonjo fled to the Chinese border.",
          territories=[T(0, "Japan (Warring States)"), T(1, "Korea", "Ming Chinese Empire")],
          fronts=[F("Japanese limit of advance, 1592", (125.3, 39.1), (126.3, 39.35), (127.4, 39.95), (128.6, 41.0), (129.8, 42.3))],
          moves=[
              M(0, "Konishi Yukinaga", "First Division", BUSAN, (128.16, 36.41), (127.90, 36.98), SEOUL, (126.55, 37.97), PYONGYANG),
              M(0, "Kato Kiyomasa", "Second Division", BUSAN, (129.21, 35.86), (127.90, 36.98), SEOUL, (127.54, 39.92), (129.75, 42.44)),
          ],
          events=[
              E("Siege of Busan", "siege", 129.04, 35.10, 1592, 0, "The Japanese stormed the port on the first day of the invasion."),
              E("Battle of Chungju", "battle", 127.90, 36.98, 1592, 0, "Japanese musketeers destroyed Korea's main field army."),
              E("Fall of Pyongyang", "siege", 125.75, 39.02, 1592, 0, "Konishi took the northern capital as the king fled."),
          ]),
        S(1592, "Jun-Aug 1592", "Admiral Yi at sea",
          "While the armies raced north, Admiral Yi Sun-sin of Jeolla province attacked the Japanese transports along the south coast with armoured turtle ships and panokseon galleys. He won at Okpo and Sacheon, and at Hansando in August lured a Japanese fleet into open water and destroyed it. Japan lost control of the sea route to the west coast, while Korean righteous armies rose in the occupied provinces.",
          territories=[T(0, "Japan (Warring States)"), T(1, "Korea", "Ming Chinese Empire")],
          fronts=[F("Japanese limit of advance, 1592", (125.3, 39.1), (126.3, 39.35), (127.4, 39.95), (128.6, 41.0), (129.8, 42.3))],
          moves=[
              M(1, "Yi Sun-sin", "Jeolla fleet", (127.66, 34.74), (127.95, 34.70), (128.3, 34.72), (128.69, 34.89), (128.48, 34.77)),
              M(0, "Wakisaka Yasuharu", "Japanese fleet", BUSAN, (128.72, 35.0), (128.6, 34.88), (128.48, 34.77)),
          ],
          events=[
              E("Battle of Okpo", "battle", 128.69, 34.89, 1592, 1, "Yi's first victory destroyed dozens of Japanese ships."),
              E("Battle of Hansando", "battle", 128.48, 34.77, 1592, 1, "Yi's crane wing formation annihilated Wakisaka's fleet."),
          ]),
        S(1593, "1593", "Ming intervention",
          "A Ming army under Li Rusong crossed the Yalu and, with Korean troops, stormed Pyongyang in February 1593. Li was checked at Byeokjegwan near Seoul, but Kwon Yul's defence of Haengju fortress and the burning of Japanese supply depots made Seoul untenable. The Japanese withdrew to a chain of forts on the south coast while peace talks dragged on for three years.",
          territories=[T(0, "Japan (Warring States)"), T(1, "Korea", "Ming Chinese Empire")],
          fronts=[F("Japanese coastal forts, 1593 to 1596", (128.55, 35.05), (128.75, 35.3), (129.05, 35.45), (129.35, 35.6))],
          moves=[
              M(1, "Li Rusong", "Ming army", (123.17, 41.27), (124.53, 40.20), PYONGYANG, (126.55, 37.97), (126.93, 37.70)),
              M(0, "Ukita Hideie", "Japanese withdrawal", SEOUL, (127.90, 36.98), (128.6, 35.87), BUSAN),
          ],
          events=[
              E("Siege of Pyongyang", "siege", 125.75, 39.02, 1593, 1, "Ming artillery and Korean troops drove Konishi out of the city."),
              E("Battle of Byeokjegwan", "battle", 126.93, 37.70, 1593, 0, "Japanese troops ambushed Li Rusong's vanguard north of Seoul."),
              E("Battle of Haengju", "siege", 126.82, 37.60, 1593, 1, "Kwon Yul's garrison beat off repeated Japanese assaults."),
          ]),
        S(1597, "1597", "The second invasion",
          "When talks failed, Hideyoshi sent a new army in 1597. Yi Sun-sin had been jailed through court intrigue, and his successor Won Gyun lost almost the whole Korean fleet at Chilcheollyang. The Japanese took Namwon and pushed toward Seoul until stopped by the Ming near Jiksan, and Yi, restored with only 13 ships, beat a much larger Japanese fleet in the narrow, fast currents of Myeongnyang.",
          territories=[T(0, "Japan (Warring States)"), T(1, "Korea", "Ming Chinese Empire")],
          fronts=[F("Japanese limit of advance, Sept 1597", (126.6, 36.4), (127.16, 36.8), (127.9, 36.75), (128.7, 36.4), (129.4, 36.0))],
          moves=[
              M(0, "Ukita Hideie", "Left Army to Namwon", (127.75, 35.07), (127.39, 35.41), (127.15, 35.82)),
              M(0, "Kuroda Nagamasa", "Right Army north", BUSAN, (128.6, 35.87), (127.8, 35.65), (127.15, 35.82), (127.12, 36.46), (127.16, 36.88)),
              M(0, "Todo Takatora", "Japanese fleet westward", (128.3, 34.8), (127.7, 34.6), (127.0, 34.4), (126.31, 34.57)),
          ],
          events=[
              E("Battle of Chilcheollyang", "battle", 128.48, 34.92, 1597, 0, "Won Gyun's fleet was destroyed in a night attack."),
              E("Siege of Namwon", "siege", 127.39, 35.41, 1597, 0, "The Japanese stormed the fortress and killed its defenders."),
              E("Battle of Myeongnyang", "battle", 126.31, 34.57, 1597, 1, "Yi's 13 ships used the strait's tidal current to defeat over 100 Japanese ships."),
          ]),
        S(1598, "1598", "Noryang and withdrawal",
          "Ming and Korean armies attacked the Japanese coastal forts at Ulsan, Sacheon and Suncheon, but the defenders held. When Hideyoshi died in September 1598 his regents ordered a withdrawal. At Noryang in December Yi Sun-sin and the Ming admiral Chen Lin intercepted Shimazu Yoshihiro's fleet, and Yi was killed by a bullet in his moment of victory as the last Japanese left Korea.",
          territories=[T(0, "Japan (Warring States)"), T(1, "Korea", "Ming Chinese Empire")],
          fronts=[F("Japanese coastal forts, 1598", (127.55, 35.0), (128.1, 35.1), (128.7, 35.25), (129.35, 35.6))],
          moves=[
              M(1, "Yi Sun-sin and Chen Lin", "Allied fleet", (127.62, 34.85), (127.75, 34.9), (127.87, 34.93)),
              M(0, "Shimazu Yoshihiro", "Shimazu relief fleet", (128.06, 35.01), (127.95, 34.97), (127.87, 34.93)),
              M(1, "Ma Gui", "Ming army against Ulsan", SEOUL, (127.90, 36.98), (129.21, 35.86), (129.35, 35.54)),
          ],
          events=[
              E("Siege of Ulsan", "siege", 129.35, 35.54, 1598, 0, "Kato Kiyomasa's starving garrison held until relief came."),
              E("Death of Hideyoshi", "event", 135.77, 34.94, 1598, None, "Hideyoshi died at Fushimi and the invasion was abandoned."),
              E("Battle of Noryang", "battle", 127.87, 34.93, 1598, 1, "The allies sank much of the Shimazu fleet, but Yi Sun-sin was killed."),
          ]),
    ],
})

out = os.path.join(H, "wars_g06.json")
json.dump(wars, open(out, "w"), ensure_ascii=False, indent=1)
print("wrote", out, len(wars), "wars", sum(len(w["steps"]) for w in wars), "steps")

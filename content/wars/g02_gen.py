#!/usr/bin/env python3
"""Generator for wars_g02.json (group g02: Rome, Carthage, Maccabees, Han, Mithridates, Gaul, Britain, Judea)."""
import json, os

H = os.path.dirname(os.path.abspath(__file__))

ROME = "#b5452f"


def T(side, *polities):
    return {"side": side, "polities": list(polities)}


def F(label, *path):
    return {"path": [list(p) for p in path], "label": label}


def M(side, commander, label, *path):
    return {"side": side, "commander": commander, "label": label, "path": [list(p) for p in path]}


def E(name, kind, lon, lat, year, winner, text):
    return {"name": name, "kind": kind, "lon": lon, "lat": lat, "year": year, "winner": winner, "text": text}


def S(year, label, title, text, territories=(), fronts=(), moves=(), events=()):
    return {"year": year, "label": label, "title": title, "text": text,
            "territories": [t for t in territories if t["polities"]],
            "fronts": list(fronts), "moves": list(moves), "events": list(events)}


def W(id, name, start, end, kind, summary, sides, theater, steps):
    return {"id": id, "name": name, "start": start, "end": end, "kind": kind, "summary": summary,
            "sides": [{"name": n, "color": c, "leaders": l} for n, c, l in sides],
            "theater": [{"lon": a, "lat": b, "r": r} for a, b, r in theater],
            "steps": steps}


ROMEc = (12.48, 41.89)
wars = []

# ---------------------------------------------------------------- 1. Roman conquest of Italy
wars.append(W(
    "roman-conquest-of-italy", "Roman conquest of Italy", -390, -264, "conflict",
    "Over about 125 years Rome went from a city sacked by Gauls to the master of the Italian peninsula south of the Po. "
    "It beat the Latins, the Samnites and their Etruscan and Gallic allies, and finally the Greek cities of the south and their champion Pyrrhus of Epirus. "
    "Rome bound the defeated to it as allies who supplied soldiers, the manpower that would carry it through the wars with Carthage.",
    [("Rome and its allies", ROME, ["Camillus", "Fabius Rullianus", "Decius Mus", "Manius Curius Dentatus"]),
     ("Gauls, Samnites and Etruscans", "#3f8a5a", ["Brennus", "Gavius Pontius", "Gellius Egnatius"]),
     ("Pyrrhus and the Italian Greeks", "#3b6fb6", ["Pyrrhus of Epirus"])],
    [(13.8, 41.8, 4.5), (16.0, 39.5, 2.5)],
    [
        S(-390, "c. 390 BC", "The Gauls sack Rome",
          "Rome had just taken its Etruscan rival Veii when a Gallic war band of the Senones under Brennus came south from the Po valley. "
          "It routed the Roman army at the Allia river, eleven miles from the city, and sacked Rome, leaving only after it was paid in gold. "
          "The disaster pushed Rome to build stronger walls and reorganise its army.",
          [T(0, "Roman Republic"), T(1, "Boii")],
          [],
          [M(1, "Brennus", "Gallic war band", (11.3, 44.4), (11.95, 43.02), (12.4, 42.4), (12.56, 42.03), ROMEc),
           M(0, "Roman levy", "Roman army to the Allia", ROMEc, (12.56, 42.03))],
          [E("Battle of the Allia", "battle", 12.56, 42.03, -390, 1, "The Gauls broke the Roman army in a single charge north of the city."),
           E("Gallic sack of Rome", "event", 12.48, 41.89, -390, 1, "The Gauls plundered Rome and left only after being paid a ransom in gold.")]),
        S(-343, "343 to 338 BC", "Campania and the Latin War",
          "Rome answered a call from Capua and fought the Samnites of the Apennines for the rich plain of Campania in the First Samnite War. "
          "Its Latin allies then rose against Roman dominance, and the consul Manlius Torquatus crushed them. "
          "In the settlement of 338 BC Rome dissolved the Latin League and bound each city to itself, the model for its whole system of Italian alliances.",
          [T(0, "Roman Republic"), T(1, "Samnites")],
          [F("Roman and Samnite spheres, 341 BC", (13.4, 41.9), (13.85, 41.55), (14.2, 41.25), (14.6, 40.9))],
          [M(0, "Valerius Corvus", "Roman army into Campania", ROMEc, (13.3, 41.6), (14.25, 41.08), (14.08, 40.86)),
           M(0, "Manlius Torquatus", "Against the Latins", ROMEc, (13.4, 41.5), (13.77, 41.26))],
          [E("Battle of Mount Gaurus", "battle", 14.08, 40.86, -342, 0, "Rome's first victory over the Samnites secured Capua."),
           E("Battle of Trifanum", "battle", 13.77, 41.26, -338, 0, "Manlius Torquatus broke the Latin revolt."),
           E("Latin settlement", "treaty", 12.48, 41.89, -338, 0, "Rome dissolved the Latin League and tied each city to itself by separate treaty.")]),
        S(-321, "326 to 304 BC", "The Caudine Forks",
          "The Second Samnite War was a struggle for central Italy. In 321 BC the Samnite general Gavius Pontius trapped a whole Roman army in the pass of the Caudine Forks and sent it under the yoke. "
          "Rome recovered, built the Via Appia toward Campania, allied with the Apulians behind the Samnites and won at Bovianum in 305 BC.",
          [T(0, "Rome"), T(1, "Sabines")],
          [F("Samnite frontier", (13.4, 42.1), (13.9, 41.6), (14.25, 41.2), (14.6, 40.85))],
          [M(0, "Consuls Veturius and Postumius", "Roman army toward Samnium", ROMEc, (13.4, 41.5), (14.25, 41.08), (14.64, 41.06)),
           M(1, "Gavius Pontius", "Samnite army", (14.47, 41.49), (14.7, 41.25), (14.64, 41.06))],
          [E("Caudine Forks", "battle", 14.64, 41.06, -321, 1, "A Roman army surrendered in a mountain pass and was sent home in disgrace."),
           E("Battle of Bovianum", "battle", 14.47, 41.49, -305, 0, "Rome took the Samnite capital and forced peace the next year.")]),
        S(-295, "298 to 290 BC", "Sentinum",
          "In the Third Samnite War the Samnite leader Gellius Egnatius marched north to join Gauls, Etruscans and Umbrians in a grand coalition against Rome. "
          "At Sentinum Fabius Rullianus and Decius Mus, who sacrificed himself in the battle, destroyed the combined army. "
          "The Samnites submitted in 290 BC and Rome annexed the Sabine country, cutting Italy in two from sea to sea.",
          [T(0, "Roman Republic")],
          [F("Line of the coalition, 296 BC", (11.6, 42.6), (12.4, 43.0), (13.3, 42.7), (14.0, 42.0), (14.6, 41.3))],
          [M(1, "Gellius Egnatius", "Samnites march north", (14.47, 41.49), (13.9, 42.2), (13.3, 42.9), (12.86, 43.43)),
           M(0, "Fabius Rullianus and Decius Mus", "Consular armies", ROMEc, (12.6, 42.6), (12.7, 43.1), (12.86, 43.43))],
          [E("Battle of Sentinum", "battle", 12.86, 43.43, -295, 0, "The largest battle yet fought in Italy broke the Samnite, Gallic and Etruscan alliance."),
           E("Samnites submit", "treaty", 14.47, 41.49, -290, 0, "The Samnites accepted alliance on Roman terms.")]),
        S(-280, "280 to 279 BC", "Pyrrhus lands in Italy",
          "Tarentum, the richest Greek city in Italy, called in King Pyrrhus of Epirus with a professional army and war elephants. "
          "Pyrrhus beat the Romans at Heraclea and Asculum and marched within forty miles of Rome, but his losses were so heavy that a costly win is still called a Pyrrhic victory. "
          "Rome refused to negotiate while he stood in Italy.",
          [T(0, "Roman Republic"), T(2, "Greek city-states")],
          [F("Front in the south, 280 BC", (14.9, 40.6), (15.7, 40.9), (16.4, 41.1), (17.0, 41.1))],
          [M(2, "Pyrrhus", "Epirote army crosses to Tarentum", (20.98, 39.16), (19.6, 39.7), (17.24, 40.47)),
           M(2, "Pyrrhus", "March on Rome", (16.63, 40.22), (15.6, 40.9), (14.25, 41.08), (13.16, 41.73)),
           M(0, "Valerius Laevinus", "Roman army to Lucania", ROMEc, (14.25, 41.08), (15.8, 40.5), (16.63, 40.22))],
          [E("Battle of Heraclea", "battle", 16.63, 40.22, -280, 2, "Pyrrhus' phalanx and elephants beat Rome's legions in their first meeting."),
           E("Battle of Asculum", "battle", 15.56, 41.2, -279, 2, "Another win at a ruinous cost, the original Pyrrhic victory.")]),
        S(-275, "275 to 264 BC", "Beneventum and the fall of Tarentum",
          "Pyrrhus spent three years fighting Carthage in Sicily, then returned to Italy and was checked at Beneventum by Manius Curius Dentatus. "
          "He sailed home, Tarentum surrendered in 272 BC, and by 264 BC Rome controlled all of Italy south of the Po. "
          "That year a call for help from Messana across the strait drew Rome into Sicily and the First Punic War.",
          [T(0, "Roman Republic", "Greek city-states")],
          [],
          [M(2, "Pyrrhus", "Back from Sicily", (15.29, 37.08), (15.65, 38.1), (16.5, 39.4), (17.24, 40.47), (15.9, 40.95), (14.78, 41.13)),
           M(0, "Manius Curius Dentatus", "Consular army", ROMEc, (13.6, 41.5), (14.78, 41.13)),
           M(0, "Papirius Cursor", "Siege of Tarentum", (14.78, 41.13), (16.0, 40.9), (17.24, 40.47))],
          [E("Battle of Beneventum", "battle", 14.78, 41.13, -275, 0, "Pyrrhus failed to break the Romans and gave up on Italy."),
           E("Fall of Tarentum", "siege", 17.24, 40.47, -272, 0, "The last great Greek city of the south became a Roman ally."),
           E("Messana appeals to Rome", "war", 15.55, 38.19, -264, None, "Rome's answer led straight into war with Carthage.")]),
    ]))

# ---------------------------------------------------------------- 2. Punic Wars
NC = (-0.98, 37.6)
CARTH = (10.32, 36.85)
wars.append(W(
    "punic-wars", "Punic Wars", -264, -146, "conflict",
    "Rome and Carthage fought three wars over 118 years for control of the western Mediterranean. "
    "Rome won Sicily at sea in the first, survived Hannibal's invasion of Italy across the Alps to win the second at Zama, and destroyed Carthage itself in the third. "
    "Victory made Rome the dominant power of the Mediterranean world.",
    [("Rome", ROME, ["Scipio Africanus", "Fabius Maximus", "Claudius Nero", "Scipio Aemilianus"]),
     ("Carthage", "#6a4fb3", ["Hamilcar Barca", "Hannibal", "Hasdrubal Barca"])],
    [(12.5, 40.0, 6), (9.5, 36.5, 3), (-2.5, 39.5, 5), (6.0, 44.5, 2.5)],
    [
        S(-264, "264 to 260 BC", "First Punic War: the fight for Sicily",
          "A dispute over Messana drew Appius Claudius across the strait into Sicily, the first time Roman legions fought outside Italy. "
          "Rome won Syracuse over to its side and took the Carthaginian base of Agrigentum, then built its first real war fleet and beat Carthage at sea off Mylae with the corvus boarding bridge.",
          [T(0, "Roman Republic", "Greek city-states"), T(1, "Carthaginian Empire")],
          [F("Line in Sicily, 261 BC", (13.85, 38.0), (13.75, 37.6), (13.65, 37.2))],
          [M(0, "Appius Claudius Caudex", "Legions cross to Messana", ROMEc, (14.25, 40.85), (16.0, 39.3), (15.65, 38.1), (15.55, 38.19)),
           M(0, "Postumius and Mamilius", "Advance to Agrigentum", (15.55, 38.19), (14.5, 37.6), (13.58, 37.31)),
           M(1, "Hanno", "Relief army", (13.28, 37.4), (13.58, 37.31))],
          [E("Siege of Agrigentum", "siege", 13.58, 37.31, -262, 0, "Rome took and sacked Carthage's main base in southern Sicily."),
           E("Battle of Mylae", "battle", 15.24, 38.22, -260, 0, "Rome's first great naval victory, won by boarding Carthaginian ships.")]),
        S(-256, "256 to 255 BC", "Invasion of Africa",
          "Rome sent a huge fleet south, smashed the Carthaginian navy off Cape Ecnomus and landed an army under Regulus near Carthage. "
          "Carthage hired the Spartan general Xanthippus, whose elephants and cavalry destroyed Regulus' army near Tunis, and storms then wrecked the Roman fleet on the way home.",
          [T(0, "Roman Republic", "Greek city-states"), T(1, "Carthaginian Empire")],
          [],
          [M(0, "Marcus Atilius Regulus", "Invasion fleet", (13.9, 37.05), (12.5, 36.9), (11.1, 36.85), (10.6, 36.75), (10.2, 36.8)),
           M(1, "Xanthippus", "Carthaginian field army", CARTH, (10.15, 36.8))],
          [E("Battle of Cape Ecnomus", "battle", 13.85, 37.0, -256, 0, "One of the largest naval battles of antiquity opened the way to Africa."),
           E("Battle of Tunis", "battle", 10.15, 36.8, -255, 1, "Xanthippus destroyed Regulus' army and captured him.")]),
        S(-241, "249 to 241 BC", "Aegates Islands",
          "The war ground on around the Carthaginian strongholds of western Sicily, where Hamilcar Barca held out on Mount Eryx. "
          "Rome lost a fleet at Drepana, but a new fleet paid for by private citizens under Lutatius Catulus destroyed Carthage's relief convoy off the Aegates Islands. "
          "Carthage gave up Sicily and paid a heavy indemnity.",
          [T(0, "Roman Republic", "Greek city-states"), T(1, "Carthaginian Empire")],
          [F("Siege lines at Lilybaeum and Drepana", (12.6, 38.12), (12.7, 37.95), (12.62, 37.78), (12.5, 37.72))],
          [M(1, "Hanno", "Carthaginian relief convoy", (10.6, 37.0), (11.2, 37.5), (12.05, 37.95)),
           M(0, "Lutatius Catulus", "Roman fleet", (12.43, 37.8), (12.3, 37.93), (12.15, 37.97))],
          [E("Battle of Drepana", "battle", 12.45, 38.05, -249, 1, "Adherbal destroyed most of the Roman fleet attacking Drepana."),
           E("Battle of the Aegates", "battle", 12.2, 37.98, -241, 0, "Rome's decisive naval victory ended the First Punic War."),
           E("Treaty of Lutatius", "treaty", 12.48, 41.89, -241, 0, "Carthage evacuated Sicily, which became Rome's first province.")]),
        S(-218, "219 to 218 BC", "Hannibal crosses the Alps",
          "After losing Sicily, Hamilcar Barca built a new Carthaginian empire in Spain. His son Hannibal took Saguntum, Rome declared war, and in 218 BC Hannibal marched from New Carthage over the Pyrenees, the Rhone and the Alps with an army and war elephants. "
          "He arrived in the Po valley with about 26,000 men, raised the Gauls and beat the Roman armies at the Ticinus and the Trebia.",
          [T(0, "Roman Republic", "Greek city-states"), T(1, "Carthaginian Empire")],
          [],
          [M(1, "Hannibal", "Hannibal's march", NC, (0.8, 41.0), (2.9, 42.6), (4.65, 43.85), (6.9, 45.1), (7.68, 45.07)),
           M(0, "Gnaeus Scipio", "Roman fleet to Spain", (10.4, 43.7), (8.5, 43.85), (5.37, 43.25), (3.12, 42.13)),
           M(0, "Sempronius Longus", "Consular army to the Trebia", (12.57, 44.06), (11.34, 44.49), (9.7, 45.05))],
          [E("Siege of Saguntum", "siege", -0.27, 39.68, -219, 1, "Hannibal's capture of Rome's Spanish ally started the war."),
           E("Battle of the Ticinus", "battle", 8.95, 45.2, -218, 1, "Hannibal's cavalry routed Publius Scipio's army, wounding the consul."),
           E("Battle of the Trebia", "battle", 9.6, 45.0, -218, 1, "Hannibal ambushed and destroyed the combined consular armies.")]),
        S(-216, "217 to 216 BC", "Trasimene and Cannae",
          "Hannibal crossed the Apennines and trapped a Roman army on the shore of Lake Trasimene. Fabius Maximus then shadowed him without giving battle, "
          "but in 216 BC Rome sought a decision and at Cannae Hannibal's double envelopment annihilated the largest army it had ever fielded. "
          "Capua and much of southern Italy went over to Carthage, yet Rome refused to make peace.",
          [T(0, "Roman Republic"), T(1, "Carthaginian Empire", "Greek city-states")],
          [F("Line in Italy after Cannae", (13.95, 41.02), (14.6, 41.25), (15.3, 41.55), (15.95, 41.85))],
          [M(1, "Hannibal", "Over the Apennines to Apulia", (9.7, 44.9), (10.9, 43.9), (12.07, 43.2), (13.6, 43.0), (15.5, 41.6), (16.13, 41.31)),
           M(0, "Fabius Maximus", "Shadowing army", ROMEc, (13.5, 41.6), (14.6, 41.4), (15.3, 41.45)),
           M(0, "Aemilius Paullus and Terentius Varro", "Consular armies", ROMEc, (14.2, 41.6), (15.5, 41.45), (16.13, 41.31))],
          [E("Battle of Lake Trasimene", "battle", 12.07, 43.2, -217, 1, "Hannibal ambushed a consular army in the lakeside fog and destroyed it."),
           E("Battle of Cannae", "battle", 16.13, 41.31, -216, 1, "Hannibal's double envelopment killed perhaps 50,000 Romans in one day."),
           E("Capua defects", "event", 14.25, 41.08, -216, 1, "Italy's second city went over to Hannibal.")]),
        S(-209, "211 to 206 BC", "Rome strikes back",
          "Rome wore Hannibal down in Italy, retaking Capua and Tarentum, while Publius Cornelius Scipio took the war to Spain and stormed New Carthage. "
          "Hasdrubal Barca slipped out of Spain to reinforce his brother, but the consul Claudius Nero marched north from Apulia and destroyed him at the Metaurus. "
          "Scipio's victory at Ilipa in 206 BC drove Carthage out of Spain.",
          [T(0, "Roman Republic", "Greek city-states"), T(1, "Carthaginian Empire")],
          [F("Hannibal confined to the south, 207 BC", (15.6, 40.2), (16.2, 40.1), (16.8, 39.9))],
          [M(0, "Scipio", "Scipio to New Carthage and Ilipa", (1.25, 41.12), (0.0, 39.5), NC, (-3.6, 37.4), (-5.98, 37.52)),
           M(1, "Hasdrubal Barca", "Hasdrubal's march to Italy", (-3.75, 38.07), (-1.0, 40.5), (1.5, 42.3), (4.8, 44.0), (7.5, 45.0), (12.85, 43.72)),
           M(0, "Claudius Nero", "Forced march north", (16.07, 41.22), (14.8, 42.2), (13.5, 43.3), (12.85, 43.72))],
          [E("Capture of New Carthage", "siege", -0.98, 37.6, -209, 0, "Scipio stormed Carthage's capital in Spain in a single day."),
           E("Battle of the Metaurus", "battle", 12.85, 43.72, -207, 0, "Hasdrubal's army was destroyed before it could join Hannibal."),
           E("Battle of Ilipa", "battle", -5.98, 37.52, -206, 0, "Scipio's victory ended Carthaginian power in Spain.")]),
        S(-202, "204 to 201 BC", "Zama",
          "Scipio landed in Africa near Utica and, with the Numidian prince Masinissa as an ally, beat Carthage's armies in the field. "
          "Carthage recalled Hannibal from Italy after fifteen years, and at Zama Scipio defeated him in the war's final battle. "
          "The peace of 201 BC stripped Carthage of its fleet and its empire.",
          [T(0, "Roman Republic", "Greek city-states"), T(1, "Carthaginian Empire")],
          [],
          [M(0, "Scipio Africanus", "Invasion fleet", (12.43, 37.8), (11.3, 37.4), (10.06, 37.06)),
           M(1, "Hannibal", "Recalled from Italy", (17.12, 39.08), (15.5, 37.2), (13.0, 36.0), (10.64, 35.83)),
           M(1, "Hannibal", "March to Zama", (10.64, 35.83), (9.9, 36.0), (9.2, 36.3)),
           M(0, "Masinissa", "Numidian cavalry", (7.5, 36.3), (8.5, 36.3), (9.2, 36.3))],
          [E("Battle of Zama", "battle", 9.2, 36.3, -202, 0, "Scipio and Masinissa defeated Hannibal and ended the Second Punic War."),
           E("Peace of 201 BC", "treaty", 10.32, 36.85, -201, 0, "Carthage gave up Spain and its fleet and paid tribute for fifty years.")]),
        S(-149, "149 to 146 BC", "Third Punic War: Carthage destroyed",
          "Rome, urged on by Cato, used a Carthaginian war with Masinissa's Numidia as a pretext to send an army to Africa. "
          "Carthage handed over its weapons but refused to abandon its city, and held out for three years. "
          "Scipio Aemilianus stormed it in 146 BC, razed it and made its territory the Roman province of Africa.",
          [T(0, "Rome", "Kingdom of Gala"), T(1, "Carthage")],
          [F("Roman siege lines, 147 BC", (10.24, 36.9), (10.26, 36.86), (10.28, 36.82))],
          [M(0, "Manilius and Censorinus", "Roman expedition", (12.43, 37.8), (11.3, 37.4), (10.06, 37.06)),
           M(0, "Scipio Aemilianus", "Assault on Carthage", (10.06, 37.06), (10.2, 36.95), CARTH)],
          [E("Siege of Carthage", "siege", 10.32, 36.85, -146, 0, "Scipio Aemilianus took the city street by street and razed it."),
           E("Province of Africa", "event", 10.06, 37.06, -146, 0, "Carthage's land became a Roman province governed from Utica.")]),
    ]))

# ---------------------------------------------------------------- 3. Roman conquest of Hispania
wars.append(W(
    "roman-conquest-of-hispania", "Roman conquest of Hispania", -218, -19, "conflict",
    "Rome came to Spain in 218 BC to fight Carthage and stayed for two centuries of war against the peoples of the interior. "
    "Lusitanians under Viriathus, Celtiberians at Numantia, the rebel Roman Sertorius and finally the mountain Cantabrians and Astures resisted in turn until Augustus and Agrippa finished the conquest in 19 BC. "
    "Hispania became one of the most Romanised parts of the empire, the root of the Latin languages of Iberia.",
    [("Rome", ROME, ["Scipio Africanus", "Cato the Elder", "Scipio Aemilianus", "Pompey", "Augustus", "Agrippa"]),
     ("Iberian peoples", "#c08a2e", ["Viriathus", "Sertorius", "Cantabrian chiefs"]),
     ("Carthage", "#6a4fb3", ["Hasdrubal Barca", "Mago"])],
    [(-4.0, 40.0, 6.5)],
    [
        S(-218, "218 to 206 BC", "Rome arrives to fight Carthage",
          "While Hannibal marched on Italy, Gnaeus Scipio landed at Emporion and held the line of the Ebro. Both Scipio brothers were killed in 211 BC, "
          "but the younger Publius Scipio stormed New Carthage in 209 BC and drove the Carthaginians out of Spain after Ilipa in 206 BC. "
          "Rome kept the conquered east and south coasts.",
          [T(0, "Roman Republic"), T(2, "Carthaginian Empire")],
          [F("Ebro line, 217 to 211 BC", (0.87, 40.72), (0.3, 41.2), (-0.88, 41.65), (-2.45, 42.47))],
          [M(0, "Gnaeus Scipio", "Landing at Emporion", (3.12, 42.13), (2.2, 41.5), (1.25, 41.12)),
           M(0, "Publius Scipio", "To New Carthage and Ilipa", (1.25, 41.12), (0.0, 39.5), NC, (-3.6, 37.4), (-5.98, 37.52)),
           M(2, "Hasdrubal Barca", "Carthaginian army", (-4.78, 37.88), (-3.75, 38.07), (-1.5, 40.0))],
          [E("Battle of Cissa", "battle", 1.25, 41.2, -218, 0, "Gnaeus Scipio won Rome's first foothold north of the Ebro."),
           E("Capture of New Carthage", "siege", -0.98, 37.6, -209, 0, "Scipio seized Carthage's capital, arsenal and treasury in Spain."),
           E("Battle of Ilipa", "battle", -5.98, 37.52, -206, 0, "Carthage's last army in Spain was destroyed.")]),
        S(-195, "197 to 179 BC", "Two provinces and the first revolts",
          "In 197 BC Rome organised its gains as Hither and Further Spain, and the tribes rose almost at once against tribute and governors. "
          "Cato the Elder crushed the northeast in 195 BC, and Tiberius Gracchus pushed into Celtiberia and in 179 BC made treaties that kept the peace for a generation. "
          "The interior and the west remained free.",
          [T(0, "Rome")],
          [F("Edge of Roman control, c. 180 BC", (0.6, 42.4), (-1.4, 41.6), (-2.4, 40.4), (-3.6, 38.8), (-5.2, 38.2), (-6.6, 37.4))],
          [M(0, "Cato the Elder", "Campaign in the northeast", (3.12, 42.13), (1.25, 41.12), (-0.88, 41.65)),
           M(0, "Tiberius Gracchus", "Into Celtiberia", (-0.88, 41.65), (-1.9, 41.3), (-2.5, 41.0))],
          [E("Cato at Emporion", "battle", 3.12, 42.13, -195, 0, "Cato defeated the rebel tribes of the northeast."),
           E("Treaties of Gracchus", "treaty", -2.3, 41.3, -179, None, "Fair terms for the Celtiberians brought twenty-five years of peace.")]),
        S(-147, "155 to 139 BC", "Viriathus and the Lusitanians",
          "The Lusitanians of the far west raided the Roman south, and in 150 BC the governor Galba massacred thousands who had surrendered. "
          "A survivor, the shepherd Viriathus, led eight years of guerrilla war from the hills, beating army after army until Rome recognised him as a friend of the Roman people in 140 BC. "
          "The next year Rome bribed his companions to murder him.",
          [T(0, "Rome")],
          [F("Lusitanian raiding front, c. 145 BC", (-8.6, 38.4), (-7.0, 38.8), (-5.4, 39.2), (-3.8, 39.8))],
          [M(1, "Viriathus", "Lusitanian raids", (-7.6, 40.32), (-6.5, 39.2), (-5.6, 38.0), (-5.5, 37.3)),
           M(0, "Servilius Caepio", "Roman army into Lusitania", (-5.98, 37.4), (-6.5, 38.6), (-7.6, 40.32))],
          [E("Galba's massacre", "event", -7.5, 38.6, -150, 0, "The slaughter of surrendered Lusitanians turned a raid war into a national revolt."),
           E("Murder of Viriathus", "event", -7.6, 40.32, -139, 0, "Bribed by Rome, his own envoys killed him in his sleep.")]),
        S(-134, "143 to 133 BC", "Numantia",
          "The Celtiberian hill town of Numantia defied Rome for ten years and humiliated several consuls. "
          "In 134 BC Scipio Aemilianus, destroyer of Carthage, arrived, restored discipline and surrounded the town with a ring of walls and camps. "
          "After fifteen months of starvation Numantia surrendered and was razed, breaking the resistance of the central plateau.",
          [T(0, "Rome")],
          [F("Scipio's siege ring", (-2.49, 41.84), (-2.44, 41.86), (-2.39, 41.83), (-2.39, 41.79), (-2.44, 41.76), (-2.49, 41.79))],
          [M(0, "Scipio Aemilianus", "March from Tarraco", (1.25, 41.12), (-0.88, 41.65), (-1.9, 41.8), (-2.44, 41.81))],
          [E("Siege of Numantia", "siege", -2.44, 41.81, -133, 0, "The starved defenders surrendered and the town was destroyed.")]),
        S(-77, "80 to 72 BC", "Sertorius",
          "Quintus Sertorius, a Roman general on the losing side of Rome's civil war, made Spain his base and won the Lusitanians and Celtiberians to his cause. "
          "For years he beat the Senate's armies under Metellus Pius and the young Pompey with hit and run warfare. "
          "In 72 BC his own officer Perperna murdered him, and Pompey quickly mopped up.",
          [T(0, "Roman Republic")],
          [F("Line of the Sertorian war, 76 BC", (1.2, 41.6), (0.0, 40.6), (-1.0, 39.3), (-3.0, 38.4), (-5.2, 38.6))],
          [M(0, "Pompey", "Over the Pyrenees", (3.0, 43.18), (2.86, 42.46), (1.25, 41.12), (-0.38, 39.47)),
           M(0, "Metellus Pius", "From Further Spain", (-5.98, 37.4), (-5.0, 38.7), (-3.0, 39.9)),
           M(1, "Sertorius", "Sertorian army", (-0.41, 42.14), (-1.5, 40.8), (-0.43, 39.15))],
          [E("Battle of the Sucro", "battle", -0.43, 39.15, -75, None, "Sertorius mauled Pompey before Metellus arrived to save him."),
           E("Murder of Sertorius", "event", -0.41, 42.14, -72, 0, "Killed at a banquet in Osca, his capital, by his officer Perperna.")]),
        S(-26, "29 to 19 BC", "The Cantabrian Wars",
          "Only the mountain north still held out. Augustus came in person in 26 BC and sent three columns from Segisama into the Cantabrian mountains, while his legates fought the Astures around Lancia. "
          "Revolts flared again and again until Agrippa finished the conquest in 19 BC, two hundred years after the Romans first landed.",
          [T(0, "Roman Republic")],
          [F("Cantabrian mountain front, 26 BC", (-7.0, 42.75), (-5.6, 42.85), (-4.3, 42.8), (-3.0, 43.0))],
          [M(0, "Augustus", "Columns into Cantabria", (-4.04, 42.42), (-4.1, 42.8), (-4.0, 43.2)),
           M(0, "Carisius", "Against the Astures", (-6.06, 42.46), (-5.42, 42.53)),
           M(0, "Agrippa", "Final campaign", (-4.04, 42.42), (-4.6, 42.9), (-4.8, 43.2))],
          [E("Fall of Lancia", "siege", -5.42, 42.53, -25, 0, "The stronghold of the Astures surrendered to Carisius."),
           E("Agrippa ends the war", "event", -4.5, 43.15, -19, 0, "The last Cantabrian rising was crushed and Hispania was fully Roman.")]),
    ]))

# ---------------------------------------------------------------- 4. Maccabean Revolt
JER = (35.235, 31.778)
ANT = (36.16, 36.2)
wars.append(W(
    "maccabean-revolt", "Maccabean Revolt", -167, -160, "war",
    "Jewish rebels led by the priest Mattathias and his sons, the Maccabees, rose against the Seleucid king Antiochus IV after he outlawed Jewish worship and defiled the Temple. "
    "Judah Maccabee's guerrilla army beat several Seleucid forces, retook Jerusalem and rededicated the Temple in 164 BC, the origin of Hanukkah. "
    "Judah fell in 160 BC, but his brothers went on to found the independent Hasmonean kingdom.",
    [("Maccabees", "#3b6fb6", ["Mattathias", "Judah Maccabee", "Jonathan Apphus"]),
     ("Seleucid Empire", "#c08a2e", ["Antiochus IV", "Lysias", "Nicanor", "Bacchides"])],
    [(35.1, 31.8, 0.9), (35.8, 34.0, 2.5)],
    [
        S(-167, "167 to 166 BC", "Revolt at Modiin",
          "Antiochus IV banned the Jewish law and set up a pagan altar in the Temple of Jerusalem. In the village of Modiin the priest Mattathias killed a royal officer and a Jew who sacrificed, then fled to the hills with his five sons. "
          "His son Judah, called Maccabee, the hammer, took over the band and ambushed the Seleucid columns sent against it.",
          [T(1, "Seleucid Kingdom")],
          [F("Edge of the Judean hills", (35.0, 32.1), (34.97, 31.85), (34.95, 31.55))],
          [M(0, "Mattathias", "Flight to the hills", (35.0, 31.93), (35.15, 31.97), (35.22, 31.96)),
           M(1, "Seron", "Seleucid column", (34.75, 32.05), (34.95, 31.93), (35.13, 31.88))],
          [E("Mattathias rises", "event", 35.0, 31.93, -167, None, "The killing at Modiin began the revolt."),
           E("Battle of Beth Horon", "battle", 35.13, 31.88, -166, 0, "Judah ambushed Seron's column in the steep pass.")]),
        S(-165, "165 to 164 BC", "Emmaus and the Temple",
          "The regent Lysias sent a large army under Gorgias and Nicanor, but Judah surprised their camp at Emmaus. "
          "Lysias came himself by the southern road and was beaten at Beth Zur. Judah entered Jerusalem, cleansed the Temple and rededicated it in December 164 BC, the festival of Hanukkah.",
          [T(1, "Seleucid Kingdom")],
          [F("Edge of the Judean hills", (35.0, 32.1), (34.97, 31.85), (34.95, 31.55))],
          [M(1, "Gorgias and Nicanor", "Seleucid army to Emmaus", (35.5, 33.6), (34.9, 32.6), (34.85, 32.0), (34.99, 31.84)),
           M(1, "Lysias", "Southern invasion", ANT, (35.5, 33.6), (34.8, 32.2), (34.85, 31.55), (35.08, 31.59)),
           M(0, "Judah Maccabee", "Maccabee army", (35.22, 31.96), (34.99, 31.84), (35.08, 31.59), JER)],
          [E("Battle of Emmaus", "battle", 34.99, 31.84, -165, 0, "Judah's night march caught the Seleucid army divided."),
           E("Battle of Beth Zur", "battle", 35.08, 31.59, -164, 0, "Lysias was turned back on the road from Idumea."),
           E("Rededication of the Temple", "event", 35.235, 31.778, -164, 0, "Judah purified the Temple and restored Jewish worship.")]),
        S(-162, "162 BC", "Beth Zechariah",
          "Lysias returned with the boy king Antiochus V, a far larger army and war elephants. He beat Judah at Beth Zechariah, where Judah's brother Eleazar died stabbing an elephant from beneath, and besieged the Temple mount. "
          "News of a rival regent at Antioch forced Lysias to make peace and withdraw, repealing the ban on Jewish religion.",
          [T(1, "Seleucid Kingdom")],
          [],
          [M(1, "Lysias", "Royal army with elephants", ANT, (35.5, 33.6), (34.8, 32.2), (34.85, 31.55), (35.15, 31.65), JER),
           M(0, "Judah Maccabee", "Maccabee army", JER, (35.15, 31.65))],
          [E("Battle of Beth Zechariah", "battle", 35.15, 31.65, -162, 1, "Seleucid phalanx and elephants defeated the Maccabees."),
           E("Peace of Lysias", "treaty", 35.235, 31.778, -162, 0, "The Seleucids restored religious freedom, the revolt's first aim.")]),
        S(-160, "161 to 160 BC", "Adasa and Elasa",
          "The war went on as a fight for power in Judea. Judah destroyed Nicanor's army at Adasa in 161 BC, but the next year the general Bacchides came with a fresh army and killed Judah at Elasa. "
          "His brother Jonathan carried on the struggle, and by 142 BC Simon, the last brother, ruled an independent Judea.",
          [T(1, "Seleucid Kingdom")],
          [],
          [M(1, "Bacchides", "Seleucid army", ANT, (35.8, 34.0), (35.5, 32.8), (35.17, 31.92)),
           M(0, "Judah Maccabee", "Last stand", (35.22, 31.86), (35.17, 31.92))],
          [E("Battle of Adasa", "battle", 35.22, 31.86, -161, 0, "Nicanor was killed and his army routed."),
           E("Battle of Elasa", "battle", 35.17, 31.92, -160, 1, "Judah Maccabee fell fighting against Bacchides' larger army.")]),
    ]))

# ---------------------------------------------------------------- 5. Han expansion into Korea and Vietnam
PANYU = (113.26, 23.13)
WANG = (125.75, 39.02)
wars.append(W(
    "han-expansion-korea-vietnam", "Han conquest of Nanyue and Gojoseon", -111, -108, "war",
    "Emperor Wu of Han sent armies against the kingdoms on China's southern and northeastern edges. "
    "In 111 BC Han forces took Panyu and annexed Nanyue, bringing northern Vietnam under Chinese rule for about a thousand years, and in 108 BC they took Wanggeom and replaced Gojoseon with four commanderies in northern Korea. "
    "The wars fixed the outer limits of the Han world for centuries.",
    [("Han Empire", "#c0473a", ["Emperor Wu", "Lu Bode", "Yang Pu", "Xun Zhi"]),
     ("Nanyue and Minyue", "#2f8f83", ["Lu Jia", "Zhao Jiande"]),
     ("Gojoseon", "#7b5bb5", ["King Ugeo"])],
    [(110.5, 23.5, 5.5), (124.5, 39.5, 3.5)],
    [
        S(-112, "112 BC", "War on Nanyue",
          "Nanyue, a kingdom founded by a Qin general around Panyu, was moving toward submission to Han when its chancellor Lu Jia killed the pro-Han queen mother, the young king and the Han envoys. "
          "Emperor Wu sent several armies south over the Nanling passes, led by Lu Bode and Yang Pu, with others coming down the rivers.",
          [T(0, "Han Empire"), T(1, "Nan-Yue", "Min-Yue")],
          [F("Nanling passes", (110.3, 25.6), (111.8, 25.3), (113.4, 25.3), (114.8, 25.0))],
          [M(0, "Lu Bode", "Army of the Wave-Calming General", (112.94, 28.23), (112.6, 26.0), (113.0, 24.8), (113.1, 23.6)),
           M(0, "Yang Pu", "Towered-ship army", (115.86, 28.68), (114.9, 25.9), (114.3, 24.9), (113.6, 23.7))],
          [E("Lu Jia's coup", "event", 113.26, 23.13, -112, 1, "The murder of the king and the Han envoys gave Emperor Wu his reason for war.")]),
        S(-111, "111 to 110 BC", "Fall of Panyu",
          "Yang Pu's troops reached Panyu first and set it on fire, and Lu Bode received the surrender of its defenders. Lu Jia and the king fled by sea and were captured. "
          "Nanyue became nine commanderies stretching down to Jiaozhi and Jiuzhen in the Red River and Ma River plains of Vietnam, and in 110 BC Han also conquered Minyue on the Fujian coast.",
          [T(0, "Han Empire", "Nan-Yue"), T(1, "Min-Yue")],
          [],
          [M(0, "Lu Bode", "South to Jiaozhi", PANYU, (110.5, 21.8), (108.3, 21.6), (105.85, 21.03)),
           M(0, "Han Yue", "Fleet against Minyue", (120.2, 30.2), (121.4, 28.5), (119.6, 26.1), (119.3, 26.08))],
          [E("Fall of Panyu", "siege", 113.26, 23.13, -111, 0, "The Nanyue capital was burned and the kingdom annexed."),
           E("Jiaozhi commandery", "event", 105.85, 21.03, -111, 0, "Northern Vietnam entered a thousand years of Chinese rule."),
           E("Conquest of Minyue", "war", 119.3, 26.08, -110, 0, "Han armies overran the last independent Yue kingdom on the coast.")]),
        S(-109, "109 BC", "Invasion of Gojoseon",
          "King Ugeo of Gojoseon blocked contact between Han and the states of southern Korea, and the killing of a Han envoy led to war. "
          "Yang Pu crossed the Bohai Sea from Shandong with a fleet while Xun Zhi marched overland from Liaodong. Both were beaten back at first, then closed on the capital Wanggeom.",
          [T(0, "Han Empire", "Nan-Yue", "Min-Yue"), T(2, "Tungus")],
          [F("Gojoseon's northern line, 109 BC", (124.4, 40.1), (125.2, 39.75), (126.0, 39.8), (126.8, 40.0))],
          [M(0, "Yang Pu", "Fleet across the Bohai", (119.94, 37.18), (121.2, 38.3), (122.6, 38.7), (124.8, 38.7), WANG),
           M(0, "Xun Zhi", "Liaodong army", (123.17, 41.27), (124.4, 40.1), (125.2, 39.6), WANG)],
          [E("Yang Pu repulsed", "battle", 125.4, 38.85, -109, 2, "Gojoseon troops routed Yang Pu's landing force near the capital.")]),
        S(-108, "108 BC", "Four Commanderies",
          "Besieged and divided, Gojoseon's ministers murdered King Ugeo and the capital fell in the summer of 108 BC. "
          "Han divided the land into four commanderies, Lelang around Pyongyang, Zhenfan, Lintun and Xuantu. Lelang lasted until AD 313 and carried Chinese writing and goods into Korea and Japan.",
          [T(0, "Han Empire", "Nan-Yue", "Min-Yue")],
          [],
          [M(0, "Xun Zhi", "Final assault", (125.2, 39.6), WANG)],
          [E("Fall of Wanggeom", "siege", 125.75, 39.02, -108, 0, "Gojoseon's capital surrendered after King Ugeo was killed by his ministers."),
           E("Lelang commandery", "event", 125.75, 39.02, -108, 0, "Han rule in northern Korea began, centred on Pyongyang.")]),
    ]))

# ---------------------------------------------------------------- 6. Mithridatic Wars
AMASEIA = (35.83, 40.65)
PANT = (36.47, 45.35)
wars.append(W(
    "mithridatic-wars", "Mithridatic Wars", -88, -63, "conflict",
    "Mithridates VI of Pontus, the most dangerous enemy of the late Roman Republic, fought Rome three times for control of Anatolia and the Aegean. "
    "Sulla drove him out of Greece, Lucullus invaded Pontus and Armenia, and Pompey finally broke him in 66 BC and reorganised the whole East. "
    "The wars added Anatolia and Syria to the Roman world and made Pompey the greatest man in Rome.",
    [("Rome", ROME, ["Sulla", "Lucullus", "Pompey"]),
     ("Pontus and allies", "#2f8f83", ["Mithridates VI", "Archelaus", "Tigranes II of Armenia"])],
    [(32.0, 40.0, 7.5), (23.2, 38.3, 2.0), (40.5, 41.5, 5.0)],
    [
        S(-88, "89 to 88 BC", "The Asian Vespers",
          "Provoked by Rome's ally Bithynia, Mithridates swept through Roman Asia while Rome was distracted by war in Italy. "
          "He ordered the killing of every Roman and Italian in the province, perhaps 80,000 people, in a single day, then sent his general Archelaus across the Aegean, where Athens joined him.",
          [T(0, "Roman Republic"), T(1, "minor states", "Bosporan Kingdom")],
          [],
          [M(1, "Mithridates VI", "Pontic army into Asia", AMASEIA, (33.8, 41.4), (30.5, 40.4), (27.18, 39.12), (27.34, 37.94)),
           M(1, "Archelaus", "Fleet to Greece", (27.34, 37.94), (25.27, 37.4), (23.63, 37.94))],
          [E("Battle of the Amnias", "battle", 33.9, 41.45, -89, 1, "Mithridates' generals destroyed the Bithynian army."),
           E("Asian Vespers", "event", 27.34, 37.94, -88, 1, "Romans and Italians across Asia were massacred on the king's order.")]),
        S(-86, "87 to 85 BC", "Sulla in Greece",
          "Sulla landed in Epirus with five legions, besieged Athens and the Piraeus, and stormed Athens in March 86 BC. "
          "He then smashed Archelaus' much larger armies at Chaeronea and Orchomenus in Boeotia. "
          "In a hurry to return to civil war in Rome, Sulla made peace at Dardanus: Mithridates gave up his conquests but kept his throne.",
          [T(0, "Roman Republic"), T(1, "minor states", "Bosporan Kingdom")],
          [F("Front in Boeotia, 86 BC", (22.5, 38.65), (22.9, 38.45), (23.4, 38.35), (23.8, 38.3))],
          [M(0, "Sulla", "Sulla's legions", (17.94, 40.63), (19.45, 41.32), (21.5, 39.6), (22.6, 38.6), (23.72, 37.98)),
           M(1, "Archelaus", "Pontic army in Greece", (23.63, 37.94), (23.4, 38.3), (22.84, 38.49))],
          [E("Siege of Athens", "siege", 23.72, 37.98, -86, 0, "Sulla stormed the city and sacked it."),
           E("Battle of Chaeronea", "battle", 22.84, 38.49, -86, 0, "Sulla's legions routed Archelaus' army."),
           E("Peace of Dardanus", "treaty", 26.37, 40.12, -85, 0, "Mithridates gave back all his conquests.")]),
        S(-73, "74 to 71 BC", "Third war: Cyzicus",
          "After a brief second war, the death of the king of Bithynia, who left his kingdom to Rome, set off the third and longest war. "
          "Mithridates invaded Bithynia and besieged Cyzicus, but Lucullus cut his supply lines and starved his army. "
          "Lucullus then invaded Pontus and won at Cabira, and Mithridates fled to his son-in-law Tigranes of Armenia.",
          [T(0, "Roman Republic"), T(1, "minor states", "Bosporan Kingdom")],
          [],
          [M(1, "Mithridates VI", "Invasion of Bithynia", AMASEIA, (33.0, 40.9), (29.92, 40.77), (27.89, 40.38)),
           M(0, "Lucullus", "Lucullus relieves Cyzicus and invades Pontus", (27.34, 37.94), (28.2, 39.6), (27.89, 40.38), (31.0, 40.8), (34.5, 40.9), (36.95, 40.59))],
          [E("Siege of Cyzicus", "siege", 27.89, 40.38, -73, 0, "Mithridates' great army melted away from hunger and disease."),
           E("Battle of Cabira", "battle", 36.95, 40.59, -72, 0, "Lucullus broke the Pontic army in its homeland.")]),
        S(-69, "69 to 67 BC", "Tigranocerta",
          "Lucullus crossed the Euphrates and routed the huge army of Tigranes at his new capital Tigranocerta. "
          "But his march toward the Armenian heartland failed when his exhausted troops mutinied, and Mithridates slipped back into Pontus and destroyed a Roman army at Zela.",
          [T(0, "Roman Republic"), T(1, "minor states")],
          [],
          [M(0, "Lucullus", "Into Armenia", (36.95, 40.59), (38.3, 38.35), (40.0, 38.2), (41.0, 38.14), (42.6, 39.0), (43.6, 39.3)),
           M(1, "Tigranes II", "Armenian royal army", (44.55, 39.88), (43.0, 38.8), (41.0, 38.14)),
           M(1, "Mithridates VI", "Return to Pontus", (42.0, 39.5), (38.5, 40.2), (35.89, 40.3))],
          [E("Battle of Tigranocerta", "battle", 41.0, 38.14, -69, 0, "A small Roman army routed Tigranes' host, c. site."),
           E("Battle of Zela", "battle", 35.89, 40.3, -67, 1, "Mithridates destroyed the army of Lucullus' legate Triarius.")]),
        S(-66, "66 to 65 BC", "Pompey takes command",
          "Fresh from clearing the Mediterranean of pirates, Pompey received the eastern command. He caught Mithridates at night near the Lycus river and destroyed his army. "
          "Tigranes surrendered at Artaxata and became a Roman client, while Mithridates escaped through Colchis and around the Black Sea to Crimea.",
          [T(0, "Roman Republic"), T(1, "minor states", "Bosporan Kingdom")],
          [],
          [M(0, "Pompey", "Pompey's army", (32.86, 39.93), (35.8, 40.1), (37.83, 40.3), (40.5, 39.9), (44.55, 39.88)),
           M(1, "Mithridates VI", "Flight to Crimea", (37.83, 40.3), (40.0, 41.1), (41.65, 41.65), (41.0, 43.0), (38.5, 44.6), PANT)],
          [E("Battle of the Lycus", "battle", 37.83, 40.3, -66, 0, "Pompey's night attack destroyed Mithridates' last field army."),
           E("Tigranes submits", "treaty", 44.55, 39.88, -66, 0, "Armenia became a Roman client kingdom.")]),
        S(-63, "64 to 63 BC", "Death of Mithridates",
          "Mithridates planned to invade Italy from the north, but his son Pharnaces led a revolt, and the old king took his own life at Panticapaeum in 63 BC. "
          "Pompey annexed Pontus with Bithynia, made Syria a province, took Jerusalem, and ringed the new provinces with client kings.",
          [T(0, "Roman Republic", "minor states", "Bosporan Kingdom")],
          [],
          [M(0, "Pompey", "Pompey's settlement of the East", (36.33, 41.28), (35.5, 38.8), ANT, (36.3, 33.5), JER)],
          [E("Death of Mithridates", "event", 36.47, 45.35, -63, 0, "Abandoned by his army and his son, Mithridates took his own life."),
           E("Pompey takes Jerusalem", "siege", 35.235, 31.778, -63, 0, "Judea became a Roman client state.")]),
    ]))

# ---------------------------------------------------------------- 7. Caesar's Gallic Wars
BIB = (4.04, 46.92)
ALESIA = (4.5, 47.54)
wars.append(W(
    "gallic-wars", "Caesar's Gallic Wars", -58, -50, "war",
    "Julius Caesar, governor of Rome's provinces on both sides of the Alps, used a migration of the Helvetii as a pretext to conquer all of independent Gaul. "
    "In eight years of campaigns he beat the Gallic and Belgic tribes one by one, crossed the Rhine and the Channel, and crushed the great revolt of Vercingetorix at Alesia in 52 BC. "
    "The conquest made Gaul Roman and gave Caesar the army and fortune that carried him to power in Rome.",
    [("Rome", ROME, ["Julius Caesar", "Labienus", "Publius Crassus", "Decimus Brutus"]),
     ("Gauls and their allies", "#3f8a5a", ["Vercingetorix", "Ariovistus", "Ambiorix", "Cassivellaunus"])],
    [(2.5, 47.5, 6.0), (0.5, 51.5, 1.5)],
    [
        S(-58, "58 BC", "Helvetii and Ariovistus",
          "The Helvetii set out from the Swiss plateau to settle in western Gaul. Caesar followed them across the Saone and destroyed them near Bibracte, sending the survivors home. "
          "That same summer he marched north against the Germanic king Ariovistus, who had settled in Gaul, and drove him back over the Rhine.",
          [T(0, "Roman Republic")],
          [],
          [M(1, "Divico", "Helvetian migration", (7.4, 46.95), (6.0, 46.15), (5.4, 46.1), (4.85, 46.3), BIB),
           M(0, "Julius Caesar", "Caesar's legions", (6.14, 46.2), (5.5, 45.95), (4.85, 46.3), BIB, (6.02, 47.24), (7.3, 47.8)),
           M(1, "Ariovistus", "Suebi", (8.2, 48.8), (7.6, 48.3), (7.3, 47.8))],
          [E("Battle of Bibracte", "battle", 4.04, 46.92, -58, 0, "Caesar defeated the migrating Helvetii and sent them home."),
           E("Battle against Ariovistus", "battle", 7.3, 47.8, -58, 0, "The Suebi were routed in Alsace and fled across the Rhine.")]),
        S(-57, "57 BC", "The Belgae",
          "Alarmed by the Roman army wintering in their lands, the Belgic tribes of the north gathered a great coalition. Caesar held the line of the Aisne until it broke up, "
          "then was nearly overwhelmed by a surprise attack of the Nervii on the Sambre before rallying his legions to win. Publius Crassus meanwhile received the submission of the tribes of Armorica.",
          [T(0, "Roman Republic")],
          [F("Aisne line, 57 BC", (3.2, 49.35), (3.9, 49.4), (4.6, 49.45))],
          [M(0, "Julius Caesar", "March to the Aisne and the Sambre", (6.02, 47.24), (4.6, 48.5), (3.9, 49.4), (3.85, 50.22)),
           M(1, "Boduognatus", "Nervii", (3.6, 50.6), (3.85, 50.22)),
           M(0, "Publius Crassus", "To Armorica", (2.4, 47.9), (0.0, 47.5), (-2.75, 47.65))],
          [E("Battle of the Axona", "battle", 3.9, 49.4, -57, 0, "The Belgic coalition failed to cross the Aisne and dispersed."),
           E("Battle of the Sabis", "battle", 3.85, 50.22, -57, 0, "Caesar survived the Nervii's ambush and annihilated them.")]),
        S(-55, "56 to 54 BC", "To the Ocean, the Rhine and Britain",
          "Caesar's fleet under Decimus Brutus destroyed the sailing ships of the Veneti off Brittany. "
          "In 55 BC Caesar bridged the Rhine in ten days to overawe the Germans, and that summer and the next he crossed to Britain, where he beat the war leader Cassivellaunus north of the Thames before returning to Gaul.",
          [T(0, "Roman Republic"), T(1, "Celts")],
          [],
          [M(0, "Decimus Brutus", "Roman fleet", (-2.2, 47.25), (-2.6, 47.4), (-2.95, 47.5)),
           M(0, "Julius Caesar", "Across the Rhine", (5.5, 50.6), (7.45, 50.43), (7.9, 50.6)),
           M(0, "Julius Caesar", "Crossing to Britain", (1.6, 50.73), (1.4, 51.22), (0.5, 51.3), (-0.29, 51.81))],
          [E("Battle of Morbihan", "battle", -2.95, 47.5, -56, 0, "Roman galleys cut the Veneti ships' rigging and destroyed their fleet."),
           E("Bridge over the Rhine", "event", 7.45, 50.43, -55, 0, "Caesar's engineers bridged the river to show Rome's reach."),
           E("Cassivellaunus submits", "event", -0.29, 51.81, -54, 0, "The British war leader yielded hostages and tribute.")]),
        S(-54, "54 to 53 BC", "Ambiorix",
          "In the winter of 54 BC Ambiorix of the Eburones lured fifteen Roman cohorts out of their camp at Atuatuca and massacred them. "
          "The Nervii then besieged Quintus Cicero's camp, until Caesar marched to his rescue. In 53 BC Caesar ravaged the land of the Eburones, but Ambiorix was never caught.",
          [T(0, "Roman Republic")],
          [],
          [M(1, "Ambiorix", "Eburones", (5.9, 50.6), (5.46, 50.78)),
           M(0, "Julius Caesar", "Relief of Cicero", (2.3, 49.9), (3.2, 50.2), (3.9, 50.45)),
           M(0, "Julius Caesar", "Ravaging of the Eburones", (3.9, 50.45), (5.0, 50.6), (5.6, 50.6))],
          [E("Ambush at Atuatuca", "battle", 5.46, 50.78, -54, 1, "Sabinus and Cotta and their men were wiped out on the march, c. site."),
           E("Relief of Cicero's camp", "battle", 3.9, 50.45, -54, 0, "Caesar broke the siege with a small relief army, c. site.")]),
        S(-52, "52 BC", "Vercingetorix and Alesia",
          "Vercingetorix of the Arverni united most of Gaul in revolt and fought a scorched earth war. Caesar stormed Avaricum but was thrown back at Gergovia. "
          "When Vercingetorix shut himself up in Alesia, Caesar ringed it with two lines of walls, one facing in and one out, beat off a huge Gallic relief army, and forced Vercingetorix to surrender.",
          [T(0, "Roman Republic")],
          [F("Caesar's siege lines at Alesia", (4.43, 47.56), (4.5, 47.59), (4.58, 47.56), (4.58, 47.52), (4.5, 47.49), (4.43, 47.52))],
          [M(0, "Julius Caesar", "Caesar's campaign of 52 BC", (4.87, 45.52), (3.28, 48.2), (2.4, 47.08), (3.12, 45.71), (4.1, 46.9), ALESIA),
           M(1, "Vercingetorix", "Gallic army", (3.12, 45.71), (2.6, 46.9), (3.12, 45.71), (4.0, 46.8), ALESIA),
           M(0, "Labienus", "Northern campaign", (3.28, 48.2), (2.35, 48.85))],
          [E("Siege of Avaricum", "siege", 2.4, 47.08, -52, 0, "Caesar stormed the town and killed almost all its people."),
           E("Battle of Gergovia", "battle", 3.12, 45.71, -52, 1, "Caesar's only major defeat in Gaul."),
           E("Siege of Alesia", "siege", 4.5, 47.54, -52, 0, "Vercingetorix surrendered after the relief army failed.")]),
        S(-51, "51 to 50 BC", "Uxellodunum",
          "Scattered resistance went on after Alesia. Caesar's last great siege was at Uxellodunum, where he cut off the spring that watered the town and cut off the hands of its captured defenders as a warning. "
          "By 50 BC Gaul was pacified, and the next year Caesar crossed the Rubicon with his veteran legions.",
          [T(0, "Roman Republic")],
          [],
          [M(0, "Julius Caesar", "March to the southwest", ALESIA, (3.0, 46.4), (2.0, 45.5), (1.66, 44.96)),
           M(1, "Lucterius and Drappes", "Last rebels", (2.6, 45.2), (1.66, 44.96))],
          [E("Siege of Uxellodunum", "siege", 1.66, 44.96, -51, 0, "The last major Gallic stronghold fell when its water was cut off.")]),
    ]))

# ---------------------------------------------------------------- 8. Roman conquest of Britain
CAMU = (0.9, 51.89)
LOND = (-0.09, 51.51)
wars.append(W(
    "roman-conquest-of-britain", "Roman conquest of Britain", 43, 84, "war",
    "In AD 43 the emperor Claudius sent four legions to conquer Britain. Over forty years Rome overran the southern tribes, hunted down Caratacus, survived the revolt of Boudica, which burned three Roman towns, "
    "and pushed into Wales, the north and Scotland. Agricola's victory at Mons Graupius in 83 marked the high point, but Rome never held the far north, which Hadrian later walled off.",
    [("Rome", ROME, ["Claudius", "Aulus Plautius", "Vespasian", "Suetonius Paulinus", "Agricola"]),
     ("British tribes", "#3f8a5a", ["Caratacus", "Boudica", "Venutius", "Calgacus"])],
    [(-2.0, 53.0, 3.5), (-3.2, 56.6, 2.0)],
    [
        S(43, "43 to 47", "The Claudian invasion",
          "Aulus Plautius landed at Richborough with four legions, beat the British under Caratacus and Togodumnus in a two day battle on the Medway and forced the Thames. "
          "The emperor Claudius came in person with elephants to receive the surrender of Camulodunum, while the future emperor Vespasian took the hill forts of the southwest.",
          [T(0, "Roman Empire"), T(1, "Dumonii")],
          [F("British line on the Medway", (0.42, 51.15), (0.48, 51.33), (0.55, 51.45))],
          [M(0, "Aulus Plautius", "Invasion army", (1.6, 50.73), (1.33, 51.29), (0.48, 51.35), (-0.1, 51.5), CAMU),
           M(0, "Vespasian", "Legio II Augusta", (-0.78, 50.84), (-1.8, 50.75), (-2.47, 50.69), (-3.53, 50.72)),
           M(1, "Caratacus", "Retreat to the west", CAMU, (-1.0, 51.8), (-3.0, 51.8))],
          [E("Battle of the Medway", "battle", 0.48, 51.35, 43, 0, "The British were driven from the river after two days of fighting."),
           E("Surrender of Camulodunum", "event", 0.9, 51.89, 43, 0, "Claudius accepted the submission of eleven kings."),
           E("Storming of Maiden Castle", "siege", -2.47, 50.69, 44, 0, "Vespasian's legion took the great hill fort, c. 44.")]),
        S(50, "47 to 51", "Caratacus",
          "The governor Ostorius Scapula held a frontier along the Fosse Way and turned on the tribes of Wales, where Caratacus led the Silures and Ordovices. "
          "Caratacus was defeated in a hill battle in about 50 and fled to the Brigantes, whose queen Cartimandua handed him over in chains. Claudius spared him in Rome.",
          [T(0, "Roman Empire", "Dumonii")],
          [F("Fosse Way frontier, c. 47", (-3.53, 50.72), (-2.36, 51.38), (-1.97, 51.72), (-1.13, 52.63), (-0.54, 53.23))],
          [M(0, "Ostorius Scapula", "Into Wales", (-1.97, 51.72), (-2.72, 52.08), (-3.1, 52.5)),
           M(1, "Caratacus", "Silures and Ordovices", (-3.4, 51.7), (-3.6, 52.3), (-3.1, 52.5)),
           M(1, "Caratacus", "Flight to the Brigantes", (-3.1, 52.5), (-2.3, 53.5), (-1.71, 54.5))],
          [E("Defeat of Caratacus", "battle", -3.1, 52.5, 50, 0, "Roman legions stormed his hill position on the Welsh border, c. site."),
           E("Cartimandua hands over Caratacus", "event", -1.71, 54.5, 51, 0, "The Brigantian queen surrendered the fugitive to Rome.")]),
        S(60, "60 to 61", "Boudica's revolt",
          "While the governor Suetonius Paulinus attacked the druid stronghold of Anglesey, Boudica, queen of the Iceni, rose after Roman officials flogged her and seized her kingdom. "
          "Her army burned Camulodunum, Londinium and Verulamium and cut up the Ninth Legion. Paulinus marched back and, though heavily outnumbered, destroyed her army somewhere along Watling Street.",
          [T(0, "Roman Empire", "Dumonii")],
          [],
          [M(1, "Boudica", "Iceni and Trinovantes", (1.29, 52.58), CAMU, LOND, (-0.36, 51.75), (-1.52, 52.57)),
           M(0, "Suetonius Paulinus", "Back from Anglesey", (-4.2, 53.2), (-2.89, 53.19), (-1.5, 52.6), LOND, (-0.9, 52.1), (-1.52, 52.57)),
           M(0, "Petillius Cerialis", "Ninth Legion", (-0.54, 53.23), (0.2, 52.5), (0.6, 52.1))],
          [E("Attack on Anglesey", "battle", -4.2, 53.2, 60, 0, "Paulinus crossed the Menai Strait and destroyed the druids' sanctuary."),
           E("Sack of Londinium", "event", -0.09, 51.51, 60, 1, "Boudica's army burned the town and killed its inhabitants."),
           E("Battle of Watling Street", "battle", -1.52, 52.57, 61, 0, "Paulinus' two legions crushed Boudica's host, c. site.")]),
        S(71, "71 to 78", "Brigantes and Wales",
          "When the Brigantian king Venutius overthrew Cartimandua, Vespasian's governors went on the offensive. "
          "Petillius Cerialis conquered the Brigantes of the north, Frontinus subdued the Silures of south Wales, and in 77 to 78 Agricola crushed the Ordovices and took Anglesey.",
          [T(0, "Roman Empire", "Dumonii")],
          [],
          [M(0, "Petillius Cerialis", "Into Brigantia", (-0.54, 53.23), (-1.08, 53.96), (-1.71, 54.5)),
           M(0, "Frontinus", "Against the Silures", (-2.6, 51.75), (-2.96, 51.61), (-3.6, 51.8)),
           M(0, "Agricola", "Ordovices and Anglesey", (-2.89, 53.19), (-3.8, 52.9), (-4.2, 53.2))],
          [E("Fall of Stanwick", "siege", -1.71, 54.5, 72, 0, "The great Brigantian stronghold of Venutius fell, c. 72.")]),
        S(83, "79 to 84", "Mons Graupius",
          "Agricola advanced into Scotland, built a line of forts between the Forth and the Clyde and sent his fleet around the north of Britain. "
          "In 83 he brought the Caledonians under Calgacus to battle at Mons Graupius and routed them. He was recalled soon after, and Rome pulled back toward the Tyne and Solway, where Hadrian built his wall.",
          [T(0, "Roman Empire", "Dumonii")],
          [F("Forth to Clyde forts, c. 81", (-4.6, 55.9), (-4.0, 56.0), (-3.4, 56.02))],
          [M(0, "Agricola", "Advance into Caledonia", (-1.08, 53.96), (-2.02, 54.97), (-2.7, 55.6), (-3.4, 56.4), (-2.52, 57.29)),
           M(0, "Roman fleet", "Voyage around Britain", (-3.0, 56.1), (-1.9, 57.5), (-2.9, 58.9), (-5.0, 58.6)),
           M(1, "Calgacus", "Caledonian army", (-3.8, 57.4), (-3.0, 57.3), (-2.52, 57.29))],
          [E("Battle of Mons Graupius", "battle", -2.52, 57.29, 83, 0, "Agricola's auxiliaries routed the Caledonians in the far north, c. site.")]),
    ]))

# ---------------------------------------------------------------- 9. Jewish-Roman Wars
CAES = (34.89, 32.5)
PTOL = (35.07, 32.92)
wars.append(W(
    "jewish-roman-wars", "Jewish-Roman Wars", 66, 136, "conflict",
    "Three great Jewish revolts against Roman rule shook the eastern empire. The First Revolt ended with the destruction of Jerusalem and the Second Temple in 70 and the fall of Masada, "
    "a diaspora uprising in Egypt, Cyrene, Cyprus and Mesopotamia was crushed in 115 to 117, and Bar Kokhba's revolt of 132 to 135 ended with Judea devastated and Jews barred from Jerusalem. "
    "The wars ended the Temple cult and shifted Jewish life to rabbinic Judaism and the diaspora.",
    [("Rome", ROME, ["Vespasian", "Titus", "Lusius Quietus", "Marcius Turbo", "Julius Severus"]),
     ("Jewish rebels", "#3b6fb6", ["Simon bar Giora", "John of Gischala", "Eleazar ben Yair", "Lukuas", "Simon bar Kokhba"])],
    [(35.2, 31.9, 1.2), (28.0, 33.5, 7.0), (40.0, 37.0, 2.5)],
    [
        S(66, "66", "The revolt breaks out",
          "After years of tension, the procurator Florus seized money from the Temple treasury and Jerusalem rose. Rebels took the city and the fortress of Masada and stopped the sacrifices for the emperor. "
          "The governor of Syria, Cestius Gallus, marched on Jerusalem with a legion, then withdrew and was ambushed in the pass of Beth Horon.",
          [T(0, "Roman Empire"), T(1, "Judea")],
          [],
          [M(0, "Cestius Gallus", "Advance on Jerusalem", PTOL, CAES, (34.95, 31.95), JER),
           M(0, "Cestius Gallus", "Retreat", JER, (35.13, 31.88), (34.89, 31.95))],
          [E("Battle of Beth Horon", "battle", 35.13, 31.88, 66, 1, "The retreating Roman column lost its baggage and thousands of men.")]),
        S(67, "67 to 69", "Vespasian takes Galilee",
          "Nero sent Vespasian with his son Titus and three legions. They advanced from Ptolemais and took Galilee town by town, including Jotapata, where the rebel commander Josephus surrendered, and Gamla. "
          "By 68 the rebels held little more than Jerusalem, Masada and a few desert forts, while inside Jerusalem the factions of John of Gischala and Simon bar Giora fought each other. In 69 Vespasian left to become emperor.",
          [T(0, "Roman Empire"), T(1, "Judea")],
          [F("Edge of rebel Judea, 68", (34.95, 32.05), (35.3, 32.1), (35.45, 31.85), (35.42, 31.45))],
          [M(0, "Vespasian", "Conquest of Galilee", PTOL, (35.28, 32.83), (35.53, 32.79), (35.74, 32.9)),
           M(1, "John of Gischala", "Flight to Jerusalem", (35.45, 33.02), (35.35, 32.4), JER)],
          [E("Siege of Jotapata", "siege", 35.28, 32.83, 67, 0, "After 47 days the town fell and Josephus went over to Rome."),
           E("Siege of Gamla", "siege", 35.74, 32.9, 67, 0, "The hilltop town on the Golan was stormed and its people killed.")]),
        S(70, "70", "Siege of Jerusalem",
          "Titus marched on Jerusalem with four legions in the spring of 70 and broke through its walls one by one. He sealed the city with a siege wall and starved it. "
          "In August the Temple was burned and destroyed, and by September the whole city had fallen. Its treasures were carried in triumph through Rome.",
          [T(0, "Roman Empire", "Judea")],
          [F("Titus's siege wall", (35.218, 31.79), (35.235, 31.797), (35.25, 31.785), (35.245, 31.768), (35.228, 31.765), (35.218, 31.775))],
          [M(0, "Titus", "Four legions", CAES, (35.0, 32.0), (35.24, 31.8))],
          [E("Siege of Jerusalem", "siege", 35.235, 31.778, 70, 0, "Five months of siege ended with the city in ruins."),
           E("Destruction of the Second Temple", "event", 35.2354, 31.7781, 70, 0, "The Temple burned, ending the sacrificial cult of Judaism.")]),
        S(73, "71 to 74", "Masada",
          "Roman forces reduced the last rebel forts, Herodium and Machaerus. The governor Flavius Silva then besieged Masada, on its desert rock above the Dead Sea, and built a great ramp up to its walls. "
          "According to Josephus, the defenders under Eleazar ben Yair killed themselves rather than be taken.",
          [T(0, "Roman Empire", "Judea")],
          [],
          [M(0, "Flavius Silva", "Legio X Fretensis", JER, (35.25, 31.6), (35.354, 31.316))],
          [E("Siege of Masada", "siege", 35.354, 31.316, 73, 0, "The last rebel fortress fell in 73 or 74.")]),
        S(116, "115 to 117", "The diaspora revolt",
          "While Trajan campaigned against Parthia, Jewish communities rose in Cyrenaica under Lukuas, in Egypt, on Cyprus and in newly conquered Mesopotamia. "
          "The fighting was savage on both sides. Marcius Turbo crushed the revolt in Egypt and Cyrene, and Lusius Quietus put it down in Mesopotamia and then governed Judea.",
          [T(0, "Roman Empire")],
          [],
          [M(1, "Lukuas", "Rebels of Cyrene", (21.86, 32.82), (25.0, 31.6), (29.92, 31.2)),
           M(0, "Marcius Turbo", "Fleet and army to Egypt", (15.6, 38.0), (22.0, 34.5), (29.92, 31.2)),
           M(0, "Lusius Quietus", "Reconquest of Mesopotamia", (38.79, 37.16), (41.22, 37.07))],
          [E("Revolt in Cyrene", "event", 21.86, 32.82, 115, 1, "Jewish rebels destroyed temples and public buildings."),
           E("Revolt on Cyprus", "event", 33.9, 35.18, 116, 1, "Rebels under Artemion devastated Salamis."),
           E("Quietus retakes Edessa and Nisibis", "battle", 38.79, 37.16, 116, 0, "Mesopotamia was brought back under Roman control.")]),
        S(132, "132 to 133", "Bar Kokhba",
          "Hadrian's plan to rebuild Jerusalem as a Roman colony, Aelia Capitolina, sparked a new revolt led by Simon bar Kosiba, hailed as Bar Kokhba, son of the star. "
          "His well prepared rebels, fighting from hidden tunnels and hill villages, drove the Romans out of much of Judea and struck their own coins counting the years of Israel's redemption.",
          [T(0, "Roman Empire")],
          [F("Rebel-held Judea, 133", (34.95, 31.95), (35.3, 32.0), (35.45, 31.7), (35.35, 31.35), (34.95, 31.4))],
          [M(1, "Simon bar Kokhba", "Rebel army", (35.24, 31.67), (35.135, 31.731), (35.0, 31.85)),
           M(0, "Tineius Rufus", "Roman garrison forces", CAES, (34.95, 32.1), (35.0, 31.9))],
          [E("Revolt of Bar Kokhba", "war", 35.24, 31.67, 132, 1, "The rebels set up an independent state in the Judean hills.")]),
        S(135, "134 to 136", "Betar",
          "Hadrian brought his best general, Julius Severus, from Britain with many legions. Severus avoided pitched battle and took the rebel strongholds one by one, starving them out. "
          "Betar fell in 135 and Bar Kokhba was killed. Judea was devastated, renamed Syria Palaestina, and Jews were barred from Jerusalem.",
          [T(0, "Roman Empire")],
          [],
          [M(0, "Julius Severus", "Roman legions", CAES, (35.0, 32.0), (35.05, 31.8), (35.135, 31.731))],
          [E("Siege of Betar", "siege", 35.135, 31.731, 135, 0, "Bar Kokhba's last fortress fell and he was killed."),
           E("Syria Palaestina", "event", 35.235, 31.778, 136, 0, "Judea lost its name and Jerusalem became the Roman colony Aelia Capitolina.")]),
    ]))

out = os.path.join(H, "wars_g02.json")
with open(out, "w") as f:
    json.dump(wars, f, ensure_ascii=False, indent=1)
print("wrote", out, len(wars), "wars", sum(len(w["steps"]) for w in wars), "steps")

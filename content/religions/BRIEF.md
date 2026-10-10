# Religious history zones

The world history map (4000 BC to today) colours every state by its MAIN religion at that time, at the level of the denomination
(Catholic vs Orthodox vs Arian, Sunni vs Shia vs Ismaili, Theravada vs Mahayana...). Clicking a place shows that place's full
religious history as a timeline. You write that data for one area of the world.

Output: a JSON array in this folder, `zones_<area>.json`. Validate with `python3 validate_zones.py zones_<area>.json` until it prints OK.

```json
{"id": "spain", "name": "Spain", "lon": -3.7, "lat": 40.4,
 "history": [
   {"from": -10000, "faith": "folk", "note": "Iberians and Celtiberians worshipped local and Celtic gods."},
   {"from": -200, "faith": "hellenic", "note": "Roman conquest brought the Roman gods and later the emperor cult."},
   {"from": 380, "faith": "christian", "note": "Christianity became the state religion of the Roman Empire."},
   {"from": 415, "faith": "arian", "note": "The Visigoths ruled Spain as Arian Christians."},
   {"from": 589, "faith": "christian", "note": "King Reccared converted to Nicene Christianity at the Third Council of Toledo."},
   {"from": 711, "faith": "sunni", "note": "The Umayyad conquest made al-Andalus a Muslim land for most of the peninsula."},
   {"from": 1054, "faith": ...}, ...
 ]}
```

Rules
- A zone is a present-day country, or a historically distinct land inside one where the majority religion differed
  (e.g. split Nigeria into north and south, India into several, Russia into European Russia / Volga-Tatarstan / Siberia).
  Aim for dense, even coverage of your whole area so every state on the map has a zone nearby.
- lon/lat = the zone's heartland or capital, ON LAND, longitude first. Each state on the map takes the religion of the zone anchor nearest to it.
- history: the MAJORITY or ruling religion of the zone, chronological, `from` = integer year it became dominant (BC negative).
  The first entry starts at -10000 (usually "folk"). No two consecutive entries with the same faith. Use only faith ids from denominations.json.
- Denomination discipline: Chalcedonian Christianity before 1054 is "christian"; after 1054 it is "catholic" or "orthodox" (add an entry at 1054
  for zones that were Christian then). Goths, Vandals, Lombards, Burgundians, Suebi: "arian" for their Arian period. Egypt, Ethiopia,
  Armenia, Nubia, Syriac areas after 451: "oriental" where that was the majority. Protestant lands: "lutheran", "anglican", "reformed" or
  "protestant" (evangelical). Islam: "sunni", "shia", "ismaili" (e.g. Fatimid Egypt 909 to 1171), "ibadi". Buddhism: "buddhism" (early, Indian)
  then "theravada", "mahayana" or "vajrayana". India: "vedic" then "hinduism". Communist suppression: "secular" where it really became the
  majority (USSR 1920s to 1991, China 1949 on, etc.), then back to the faith that returned. Where a zone today has no majority religion use the
  largest one, or "secular" if most people follow none (e.g. Czechia, Estonia).
- note: ONE plain sentence (max 260 chars) saying what changed and why: the ruler, conversion, conquest or council. These notes are the
  country's religious history that readers see, so make them specific and accurate. No markdown. No en or em dashes (use "to" or commas).
- Be historically careful. Majority religion of the population, not just a ruler, except where the ruling faith is the real story (say so in the note).

# War story data format (one JSON array per output file)

The map shows a war as a STORY told in steps. For each step the map colours the territory each side holds,
draws the front line(s), animates the main armies' movements labelled with their commander, and marks only the
few events that matter to the story. Clarity over completeness: a reader should follow who is fighting whom,
where the line is, and who is winning.

```json
{
  "id": "kebab-case-id",
  "name": "Napoleonic Wars",
  "start": 1803, "end": 1815,            // integer years, BC negative (480 BC = -480)
  "kind": "war",                          // "war" = one war told through campaigns/battles;
                                          // "conflict" = a long series of wars (Italian Wars, Reconquista...): steps are the sub-wars/phases, events are mostly kind "war" or "treaty" rather than battles
  "summary": "2-3 sentences: who fought, why, how it ended, why it matters.",
  "sides": [
    {"name": "France and allies", "color": "#3b6fb6", "leaders": ["Napoleon Bonaparte", "Marshal Davout"]},
    {"name": "Coalition", "color": "#c0473a", "leaders": ["Wellington", "Kutuzov", "Blucher"]}
  ],                                      // 2 sides (3 max). Distinct mid-tone colours readable on light and dark maps.
  "theater": [{"lon": 10, "lat": 48, "r": 14}],   // 1-4 circles (r = degrees of arc) covering the fighting
  "steps": [                              // 3-8 chronological steps (a conflict spanning centuries may use up to 10)
    {
      "year": 1805, "label": "1805", "title": "Austerlitz",
      "text": "2-4 sentences telling this chapter of the story: who moved where under whom, what happened, what changed.",
      "territories": [                    // who holds/controls what at this step
        {"side": 0, "polities": ["France", "Kingdom of Italy"]},
        {"side": 1, "polities": ["Austrian Empire", "Russian Empire"]}
      ],
      "fronts": [ {"path": [[lon,lat],[lon,lat],[lon,lat]], "label": "Front, Dec 1805"} ],   // 0-3 battle lines at this moment (polylines along the line of contact). Use them whenever there was a recognisable front; omit for pure manoeuvre or guerrilla phases.
      "moves": [ {"side": 0, "commander": "Napoleon", "label": "Grande Armee", "path": [[lon,lat],[lon,lat],[lon,lat]]} ],   // 1-5 main army movements this step. commander = the general/leader in charge (or the unit/fleet if no single leader). 2-6 points along plausible routes (armies over land, fleets over water).
      "events": [ {"name": "Battle of Austerlitz", "kind": "battle", "lon": 16.76, "lat": 49.13, "year": 1805, "winner": 0, "text": "One sentence."} ]   // 0-3 only story-critical events. kind: battle | siege | treaty | war | event. winner = side index or null.
    }
  ]
}
```

## Territories: names MUST match the border data exactly
- The map shows each step on the border file for the LATEST available year <= step.year (or the earliest file if the step is older than all files).
  Available border years (in order) are listed in border_files.txt ("bcNNN" = NNN BC).
- names/names_<file>.tsv lists every polity in that file: exact name, the spreadsheet regions it covers, centroid lon/lat, area. Sorted largest first. grep it.
- Put a polity under the side that holds/controls it at that step (occupied lands go to the occupier when the occupation is the story). Leave out uninvolved polities.
- If the right polity doesn't exist in that file (e.g. a civil war inside one state), list the closest real polities you can and rely on fronts + moves to show the split.

## Rules
- Coordinates are [lon, lat], longitude first, accurate. Check every event location.
- Only major, story-critical events; at most 3 per step.
- Text: plain sentences, no markdown, no em dashes or en dashes in text fields (use "to" or commas), neutral and factual on modern conflicts, "c." for uncertain dates.
- Validate: `python3 validate_wars.py <yourfile.json>` must print OK (it checks the schema, coordinates, years and that every territory name exists in the right border file). Fix every error it reports.

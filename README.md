# World Through Time

An interactive world history map: borders from 4000 BC to today, a timeline built on Kyle's World History spreadsheet, 134 wars told as stories (territories, front lines, commanders' movements, key events), how each denomination spread, and portraits of the most pivotal rulers.

Live at https://www.kyle-klugewicz.com/history-site/

It is a static site with no build step. Open `index.html` through any local web server, for example `python3 -m http.server`, and visit http://localhost:8000.

## Layout

- `index.html`: the whole app (D3 v7 from cdnjs).
- `data/`: what the page loads: `timeline.json`, `borders_<year>.json` (one per border year), `land.json`, `synopses.json`, `wars.json`, `religions.json`, `rulers.json` (pivotal rulers; portraits load from Wikipedia at runtime).
- `scripts/build_data.py`: rebuilds `timeline.json`, the border files and `land.json` from the historical-basemaps GeoJSON and the spreadsheet: `python3 scripts/build_data.py <geojson dir> <World_History.xlsx> data`.
- `content/wars/`: the war stories. `WAR_SCHEMA.md` describes the format, `gNN_gen.py` writes `wars_gNN.json`, `validate_wars.py` checks a file against the border data, and `python3 scripts/merge_wars.py` validates every batch and writes `data/wars.json`.
- `content/religions/`: the religion map. `denominations.json` lists the faiths, `hist_*.json` holds each denomination's history, `*_gen.py` writes one `zones_<region>.json` of dated anchor zones per region, `validate_zones.py` checks one, and `python3 content/religions/merge_religions.py content/religions/religions_old.json data/religions.json` merges them.
- `content/`: source text for the regional synopses.

## Credits

Borders are simplified from [historical-basemaps](https://github.com/aourednik/historical-basemaps) by A. Ourednik (GPL-3.0); they are approximate and use the closest available year.

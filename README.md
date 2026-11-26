# World Through Time

An interactive world history map: borders from 4000 BC to today, a timeline built on Kyle's World History spreadsheet, 134 wars told as stories (territories, front lines, armies on the move led by their best-known generals, key events), how each denomination spread, and more than two thousand people: rulers beside the states they led and travellers, explorers and generals moving along their routes. Even with no tab open, the map marks each state's main faith, puts swords on the borders of states at war and ships where they fight at sea, and keeps ships, caravans and trains moving along the trade routes of the time.

The map is drawn as an old atlas (a night chart in dark mode): painted relief, deserts, forests and ice under the states, seas shaded by depth with their names of each age and the great currents, and rivers and lakes that come and go with the years. Each state flies a small flag over its name, the flag of that year, and the map's colours are taken from the flags. About 120 cities stand on the map as the landmark they were known for at the time: Byzantium's walls, then Hagia Sophia, then Hagia Sophia with minarets.

Live at https://www.kyle-klugewicz.com/history-site/

It is a static site with no build step. Open `index.html` through any local web server, for example `python3 -m http.server`, and visit http://localhost:8000.

## Layout

- `index.html`: the whole app (D3 v7 from cdnjs).
- `data/`: what the page loads: `timeline.json`, `borders_<year>.json` (one per border year), `land.json`, `synopses.json`, `wars.json`, `religions.json`, `people.json` (everyone on the map and where they were each year), `commanders.json` (which army commanders get a figure at the head of their arrow) and `ambient.json` (the trade routes whose traffic moves on the map). Portraits load from Wikipedia at runtime; a face without a picture shows initials.
- `scripts/build_data.py`: rebuilds `timeline.json`, the border files and `land.json` from the historical-basemaps GeoJSON and the spreadsheet: `python3 scripts/build_data.py <geojson dir> <World_History.xlsx> data`.
- `content/wars/`: the war stories. `WAR_SCHEMA.md` describes the format, `gNN_gen.py` writes `wars_gNN.json`, `validate_wars.py` checks a file against the border data, and `python3 scripts/merge_wars.py` validates every batch and writes `data/wars.json`. Then `python3 scripts/war_extras.py` (needs shapely) adds what the ordinary map draws: where warring states' borders touch, and which armies and battles were at sea.
- `content/religions/`: the religion map. `denominations.json` lists the faiths, `hist_*.json` holds each denomination's history, `*_gen.py` writes one `zones_<region>.json` of dated anchor zones per region, `validate_zones.py` checks one, and `python3 content/religions/merge_religions.py content/religions/religions_old.json data/religions.json` merges them.
- `content/people/`: who is on the map. `_lib.py` holds the helpers and the table of places: `P(...)` adds a person, `R(...)` a reign that puts their face beside a state's name, and `G(...)` a place or a route they travel. `p01` to `p09` are people by era, `p10` to `p14` fill in each country's line of rulers, and `commanders.py` lists the generals worth a figure in the wars. `python3 content/people/build_people.py` checks every file against the border data and writes `data/people.json` and `data/commanders.json`.
- `content/ambient/build_ambient.py`: the trade routes and their traffic; writes `data/ambient.json` and checks that sea routes stay off land.
- `content/`: source text for the regional synopses.
- `scripts/build_basemap.py`: the painted land and sea in the map's projection, as tiles that sharpen as you zoom: `python3 scripts/build_basemap.py <source dir> data` writes `data/terrain/` (fetches Natural Earth and Blue Marble into the source dir; needs numpy, scipy and Pillow).
- `scripts/build_geo.py`: rivers, lakes and canals with the years they existed (`data/water.json`), and the names of oceans, seas, straits, mountains, deserts and peaks plus the ocean currents (`data/geo.json`): `python3 scripts/build_geo.py <source dir> data` (needs shapely and numpy).
- `content/flags/`: `flags.py` says which flag each state flies, year by year, with a note on each; `svg.py` draws the historical flags that flag-icons doesn't have. `python3 scripts/build_flags.py <source dir> data` writes `data/flags.json` (flags, timelines and the map tint of every state in every border file, taken from its flag so neighbours differ), the sprite `data/flags/sprite.webp` and one picture per flag for the side panel (needs node with Playwright, numpy, shapely and Pillow).
- `content/cities/`: `cities.py` lists the cities, each with its names over time, how important it was in each age and which landmark stood for it when; `icons.py` draws the landmarks with the small kit in `draw.py`. `python3 scripts/build_cities.py` checks them and writes `data/cities.json`.

## Credits

Borders are simplified from [historical-basemaps](https://github.com/aourednik/historical-basemaps) by A. Ourednik (GPL-3.0); they are approximate and use the closest available year.
Relief, bathymetry, rivers, lakes and place names come from [Natural Earth](https://www.naturalearthdata.com/) and the land's colour from NASA's Blue Marble, both public domain. Modern flags are from [flag-icons](https://github.com/lipis/flag-icons) (MIT); the historical flags and the city landmarks were drawn for this map.

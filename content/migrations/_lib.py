"""Helpers for the migrations on the map: peoples on the move, nomads, settlers, exiles and refugees.

Each file mNN_*.py calls M(...) once per migration. A migration is told in steps, like a war: each step has a year, a
label for the timeline ("376 to 382"), a title, a short text, the moves made in it and the places that mattered.

    M('visigoths', 'The Visigoths', 'Visigoths', 'folk', '#8e5a2b', 376, 418,
      'Summary shown under "About".', rank=1, war='fall-of-western-rome', story='ev:...', numbers='About 100,000 people',
      steps=[
        S(376, '376 to 382', 'Across the Danube', 'What happened.',
          moves=[mv('foot', (27.3, 44.1, 376), (26.6, 41.7, 378), label='Visigoths')],
          sites=[site('Adrianople', 26.56, 41.68, 378, 'The Goths destroy a Roman army; Emperor Valens dies.')]),
      ])

A move is a route of (lon, lat, year) points: on the map its head travels along it as the years pass, its trail drawn
behind it, and it stays a while after it arrives (until= keeps a route that was travelled again and again, like the
slave ships' crossings, until that year). by= says how they went and which little figures move along it on the map:
foot, wagon, horse (riders), river (boats on rivers), canoe, galley, longship, sail, steam, train, plane. Sea moves
(canoe, galley, longship, sail, steam) are checked against the coastline: they may touch land only near a waypoint.

kind: folk (a people moving with its families), nomads (riders of the steppe), seafarers, settlers, forced (the
enslaved and the deported), exiles, refugees, emigrants. rank=1 shows on the plain map; rank=2 only in the Migrations
tab or once zoomed in.
"""

MIG = []


def M(id, name, people, kind, color, start, end, summary, *, steps, rank=2, war=None, story=None, numbers=None):
    MIG.append(dict(id=id, name=name, people=people, kind=kind, color=color, start=start, end=end, summary=summary,
                    steps=list(steps), rank=rank, war=war, story=story, numbers=numbers))


def S(year, label, title, text, moves=(), sites=()):
    return dict(year=year, label=label, title=title, text=text, moves=list(moves), sites=list(sites))


def mv(by, *pts, label=None, until=None):
    return dict(by=by, path=[list(p) for p in pts], label=label, until=until)


def site(name, lon, lat, year, text):
    return dict(name=name, lon=lon, lat=lat, year=year, text=text)

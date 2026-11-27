"""Helpers for writing each country's own timeline (see the Layout section of the README at the repository root).

Clicking a state on the map switches the timeline to the history of the country or civilization it belongs to, told as
its periods: China's dynasties, Japan's eras, France's kingdoms, empires and republics. Each region file calls L(...)
once per country:

  L(id, name, region, core, *periods, base=None)
    id      short lowercase id ("china"), used by the page and by other countries' base=
    name    the timeline's name ("China")
    region  the spreadsheet region (timeline.json) whose synopsis and events stand in when none of its states is drawn
    core    (lon, lat) in its heartland; the build reports which state held that spot in every border snapshot
    base    (id, year): begin with that country's periods before `year` (a country that split off from a larger one)

  P(name, start, end, *states, short=None, note=None)
    a period of its history: a dynasty, a kingdom, a republic, a colonial era. end None: it lasts to today.
    states  the names its states go by in the border files. A name written "~Name" belongs to this country's story but
            is at home in another country's timeline (the Roman Empire in Italy's), so a click on it opens that one.
    short   the label on the timeline band, when the name is long ("Han" for "Han dynasty"; " dynasty" and " period"
            are dropped on their own)
    note    a sentence or two on what the period was

Periods follow each other: on the timeline each one ends where the next begins, whatever its own end year says, so an
overlap (the Jin dynasty began before the Three Kingdoms ended) shows in the years given, not in the bands.
"""

LINEAGES = []


def P(name, start, end, *states, short=None, note=None):
    return dict(name=name, start=start, end=end, states=list(states), short=short, note=note)


def L(id, name, region, core, *periods, base=None):
    LINEAGES.append(dict(id=id, name=name, region=region, core=core, periods=list(periods), base=base))

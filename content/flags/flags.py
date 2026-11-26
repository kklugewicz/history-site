"""Which flag each state on the map flies, year by year, and how the historical ones are drawn.

Modern flags come from the flag-icons set (MIT licence, see README); the rest are drawn here with the helpers in svg.py.
Read by scripts/build_flags.py, which renders every flag, works out each state's flag for every year it is on the map and
writes data/flags.json.

A state gets a flag only when it really had one, or a banner or emblem historians tie to it (kind 'banner', 'standard'
or 'emblem', said so in the panel). Tribes, archaeological cultures and states whose banners are unknown get none, and a
colony or vassal flies its ruler's flag (the 'sub' of its map entry, or the power in brackets after its name)."""
import math
from svg import (W, H, f, rect, hs, vs, hw, cross, nordic, saltire, disc, ring, star, star_outline, crescent, text, border, canton, tri,
                 poly, emblem, flag)

# ---------- colours ----------
RED, CRIMSON, DRED, MAROON = '#ce1126', '#b0172f', '#8c1c24', '#7a1f3d'
BLUE, NAVY, ROYAL, SKY = '#0039a6', '#012169', '#1f3f99', '#5b9bd5'
WHITE, BLACK, GOLD, YELLOW = '#ffffff', '#141414', '#f2b81b', '#fcd116'
GREEN, DGREEN, ORANGE, SAFFRON = '#00843d', '#006233', '#f08a24', '#f28c28'
PURPLE, TYRIAN, BROWN = '#5b2a86', '#66023c', '#6b4226'

DEFS = {}


def D(id, title, svg, kind='flag', note='', tint=None):
    """a flag: kind is 'flag', or 'banner', 'standard', 'emblem' when the state had no flag in the modern sense"""
    DEFS[id] = dict(svg=flag(svg), title=title, kind=kind, note=note, tint=tint)


def lilies(c, pts, size):
    return ''.join(emblem('fleur', c, x, y, size) for x, y in pts)


def ermine_spot(x, y, s=1.0):
    k = lambda v: f(v * s)
    return ('<g transform="translate(%s %s)"><circle cx="0" cy="-%s" r="%s"/><circle cx="-%s" cy="-%s" r="%s"/>'
            '<circle cx="%s" cy="-%s" r="%s"/><path d="M0 -%sL%s %sL0 %sL-%s %sZ"/></g>') % (
        f(x), f(y), k(3), k(.9), k(1.3), k(2.2), k(.8), k(1.3), k(2.2), k(.8), k(1.6), k(1.6), k(3), k(1.6), k(1.6), k(3))


def union_1707(w=W, h=H):
    """the first Union Flag (England and Scotland, 1606/1707), drawn in a w x h box"""
    return ('<svg width="%s" height="%s" viewBox="0 0 60 30" preserveAspectRatio="none">'
            '<rect width="60" height="30" fill="%s"/><path d="M0 0L60 30M60 0L0 30" stroke="#fff" stroke-width="6"/>'
            '<path d="M30 0V30M0 15H60" stroke="#fff" stroke-width="10"/><path d="M30 0V30M0 15H60" stroke="%s" stroke-width="6"/>'
            '</svg>') % (f(w), f(h), NAVY, '#c8102e')


def union_1801(w=W, h=H):
    """the Union Flag since 1801"""
    return ('<svg width="%s" height="%s" viewBox="0 0 60 30" preserveAspectRatio="none">'
            '<clipPath id="u%s"><path d="M30 15H60V30ZV30H0ZH0V0ZV0H60Z"/></clipPath>'
            '<rect width="60" height="30" fill="%s"/><path d="M0 0L60 30M60 0L0 30" stroke="#fff" stroke-width="6"/>'
            '<path d="M0 0L60 30M60 0L0 30" clip-path="url(#u%s)" stroke="#c8102e" stroke-width="4"/>'
            '<path d="M30 0V30M0 15H60" stroke="#fff" stroke-width="10"/><path d="M30 0V30M0 15H60" stroke="#c8102e" stroke-width="6"/>'
            '</svg>') % (f(w), f(h), _uid(), NAVY, _UID[0])


_UID = [0]


def _uid():
    _UID[0] += 1; return _UID[0]


def ensign(bg, badge='', union=union_1801):
    """a British-style ensign: union in the canton, a badge in the fly"""
    return rect(bg) + union(W / 2, H / 2) + badge


def char_banner(field, ch, c, font='WenQuanYi Zen Hei'):
    """a Chinese dynastic banner: the dynasty's name on its colour"""
    return rect(field) + border(c, 2.2) + text(ch, c, W / 2, H / 2 + 1, 30, font=font, weight='normal')


# ---------- antiquity ----------
D('rome-spqr', 'Vexillum of Rome', rect('#9e1b1b') + border(GOLD, 2) + emblem('eagle', GOLD, 30, 15, 22) +
  text('SPQR', GOLD, 30, 33, 12, spacing=.5), 'standard',
  'Rome had no national flag. Its legions marched under the eagle and the red vexillum, and SPQR stood for the Senate and People of Rome.',
  tint=0)
D('labarum', 'Labarum', rect(TYRIAN) + border(GOLD, 1.6) + emblem('chirho', GOLD, 30, 22.5, 34), 'standard',
  'The Chi-Rho standard Constantine took into battle in 312; Christian emperors kept it as their banner.', tint=290)
D('byz-tetra', 'Imperial flag of the Palaiologoi', rect('#b3121b') + cross(GOLD, 5) +
  text('B', GOLD, 15, 11.5, 13) + text('B', GOLD, 45, 11.5, 13) + text('B', GOLD, 15, 34, 13) + text('B', GOLD, 45, 34, 13),
  'flag', 'A gold cross between four firesteels (often read as Bs), flown by the empire from the 1260s until 1453.', tint=290)
D('vergina', 'Vergina Sun', rect('#b71c1c') + emblem('vergina', GOLD, 30, 22.5, 36), 'emblem',
  'The sixteen-rayed star of the Macedonian kings, found on the gold chest in the tomb of Philip II at Vergina.')
D('carthage', 'Sign of Tanit', rect(PURPLE) + emblem('tanit', GOLD, 30, 22.5, 34), 'emblem',
  'The sign of the goddess Tanit, carved on thousands of Carthaginian stones. No Carthaginian flag survives.')
D('achaemenid', 'Standard of Cyrus the Great', rect('#8e1b2c') + emblem('falcon', GOLD, 30, 22, 40), 'standard',
  'Xenophon wrote that the Persian kings marched under a golden eagle with spread wings, raised on a spear.')
D('sasanian', 'Derafsh Kaviani', rect('#5e1f4f') + border(GOLD, 2) + star(GOLD, 30, 22.5, 16, 4, -90, .3) +
  disc('#c62828', 30, 22.5, 3.4) + disc(GOLD, 30, 22.5, 1.4), 'standard',
  "The jewelled royal banner of the Sasanian kings, said to be the leather apron of the blacksmith Kaveh. It was lost at al-Qadisiyyah in 636.")

# ---------- Chinese dynasties (banners with the dynasty's name, in the colour of its element) ----------
D('qin', 'Banner of Qin', char_banner(BLACK, '秦', GOLD), 'banner', 'Black was the colour of the Qin, ruling by the element water.')
D('han', 'Banner of Han', char_banner('#b3201e', '漢', GOLD), 'banner', 'Red was the colour of the Han, ruling by the element fire.')
D('jin', 'Banner of Jin', char_banner('#f5f1e6', '晉', BLACK), 'banner', 'White, for the element metal.')
D('sui', 'Banner of Sui', char_banner('#b3201e', '隋', GOLD), 'banner', 'Red, for the element fire.')
D('tang', 'Banner of Tang', char_banner('#e3b11e', '唐', '#9e1b1b'), 'banner', 'Yellow, for the element earth.')
D('song', 'Banner of Song', char_banner('#b3201e', '宋', GOLD), 'banner', 'Red, for the element fire.')
D('ming', 'Banner of Ming', char_banner('#b3201e', '明', GOLD), 'banner', 'Red, for the element fire.')
D('cathay', 'Flag of Cathay', rect(WHITE) + border('#c9c2b0', 1) + ''.join(crescent('#c62828', x, y, 6, .4, .8, -90) for x, y in ((20, 15), (40, 15), (30, 31))),
  'flag', 'How the Catalan Atlas of 1375 drew the flag of the Great Khan in China: three red crescents.')
D('qing', 'Yellow Dragon Flag', rect('#f6c90e') + emblem('dragon', '#1a4b8c', 30, 24, 46) + disc('#d0312d', 9, 9, 4.2), 'flag',
  'Made the national flag in 1889; a triangular version flew from 1862. Before that the Qing had banners, not a flag.')
D('roc-5', 'Five-Coloured Flag', hs('#d0312d', '#f6c90e', '#3b6fb6', WHITE, BLACK), 'flag',
  'The Republic of China, 1912-1928: one stripe for each of the Han, Manchu, Mongol, Hui and Tibetan peoples.')
D('manchukuo', 'Flag of Manchukuo', rect('#f6c90e') + canton(hs('#d0312d', '#3b6fb6', WHITE, BLACK), 20, 15), 'flag',
  'The Japanese puppet state in Manchuria, 1932-1945.')
D('tibet', 'Snow Lion Flag', rect(WHITE) +
  ''.join('<path d="M30 30L%s %sL%s %sZ" fill="%s"/>' % (f(30 + 60 * math.cos(math.radians(a - 7.5))), f(30 + 60 * math.sin(math.radians(a - 7.5))),
                                                       f(30 + 60 * math.cos(math.radians(a + 7.5))), f(30 + 60 * math.sin(math.radians(a + 7.5))),
                                                       '#c62828' if i % 2 else '#1f3f99') for i, a in enumerate(range(-180, 1, 15))) +
  disc(GOLD, 30, 22, 6.5) + poly(WHITE, [(0, 45), (0, 34), (14, 26), (30, 36), (46, 26), (60, 34), (60, 45)]) +
  poly(GOLD, [(0, 45), (60, 45), (60, 42), (0, 42)]), 'flag',
  'Flown by the government of the 13th Dalai Lama from 1916 until 1959.')
D('mn-1945', 'Flag of the Mongolian People\'s Republic', vs('#c4272f', '#015197', '#c4272f') +
  star(GOLD, 10, 10, 3.2) + rect(GOLD, 8.6, 15, 2.8, 16), 'flag', 'With the socialist star above the Soyombo, 1940-1992.')
D('mongol', 'Great White Banner', rect('#4a7fc1') + emblem('tug', WHITE, 30, 22.5, 40), 'standard',
  "The Mongols flew no cloth flags. Chinggis Khan's standard was the Tug, a spear hung with white horsetails.")
D('horde', 'Flag of the Golden Horde', rect('#f4efe2') + border('#c9c2b0', 1) + emblem('tamga', '#c0392b', 30, 22.5, 34), 'flag',
  'As drawn on the Catalan Atlas of 1375: the tamga, the khans\' mark, also stamped on their coins.')
D('mongol-white', 'White banner', rect(WHITE) + border('#c9c2b0', 1.2), 'banner',
  'Like other Mongol and Turkic dynasties, the Ilkhans preferred white banners.')
D('timurid', 'Three rings of Timur', rect('#f4efe2') + border('#c9c2b0', 1) + emblem('rings3', '#7a1f1f', 30, 22.5, 32), 'emblem',
  "Timur's mark, three rings, which the Castilian envoy Clavijo saw on his coins and seals in 1404.")

# ---------- Islamic dynasties ----------
D('umayyad', 'White banner of the Umayyads', rect(WHITE) + border('#c9c2b0', 1.2), 'banner', 'White was the Umayyads\' dynastic colour.')
D('abbasid', 'Black Standard of the Abbasids', rect(BLACK), 'banner', 'Black was the Abbasids\' colour from their revolt in 747.')
D('fatimid', 'White banner of the Fatimids', rect(WHITE) + border('#c9c2b0', 1.2), 'banner',
  'The Fatimids took white as their dynastic colour; their caliphal banners were also red and yellow.')
D('almohad', 'White standard of the Almohads', rect(WHITE) + border('#c9c2b0', 1.2), 'banner', 'The Almohads marched under white standards.')
D('mamluk', 'Banner of the Mamluk sultans', rect('#f2c318') + crescent(WHITE, 32, 22.5, 10, .34, .8, 0), 'banner',
  'Mamluk sultans flew yellow banners (sometimes red); the Catalan Atlas of 1375 draws a crescent on Cairo\'s.')
D('delhi', 'Black flag of the Delhi Sultanate', rect(BLACK), 'banner',
  'The Catalan Atlas of 1375 shows Delhi\'s coastal cities under a black flag, the colour of the Abbasid caliphs the sultans recognised.')
D('ottoman-red', 'Ottoman red flag', rect('#e30a17') + crescent(WHITE, 26, 22.5, 11, .3, .8, 0), 'flag',
  'Ottoman armies and ships flew red and green flags with crescents; the star was added in 1844.')
D('safavid', 'Lion and Sun flag', rect('#1f8a3b') + emblem('lionsun', GOLD, 30, 22.5, 36), 'flag',
  'Shah Abbas the Great set the lion and the sun on the green flag of Safavid Iran.')
D('qajar', 'Qajar Lion and Sun', rect(WHITE) + border('#1f8a3b', 3) + emblem('lionsun', '#c79a10', 30, 22.5, 32), 'flag',
  'Qajar Iran flew the lion and the sun on a white field, edged in green.')
D('ir-1907', 'Lion and Sun tricolour', hs('#239f40', WHITE, '#da0000') + emblem('lionsun', '#c79a10', 30, 22.5, 14), 'flag',
  'Iran\'s green, white and red flag with the lion and the sun, 1907-1979.')
D('nejd', 'Flag of the First Saudi State', rect('#0c6b3a') + text('لا إله إلا الله', WHITE, 30, 21, 8, font='DejaVu Sans', weight='normal'),
  'flag', 'Green with the Shahada, the flag of the Emirate of Diriyah and later of Nejd.')
D('hejaz', 'Flag of the Kingdom of Hejaz', hs(BLACK, '#007a3d', WHITE) + tri('#ce1126', 24), 'flag',
  'The flag of the Arab Revolt, 1916, kept by the Hashemite kingdom in the Hejaz until 1925.')
D('oman-red', 'Red flag of Oman', rect('#c8102e'), 'flag', 'The plain red flag of the sultans of Muscat and Oman, used until 1970.')
D('zanzibar', 'Red flag of Zanzibar', rect('#c8102e'), 'flag', 'The plain red flag of the Omani sultans of Zanzibar.')
D('trucial', 'Flag of the Trucial States', rect('#c8102e', 9, 9, 42, 27) + border(WHITE, 18) + border('#d9d4c8', .6), 'flag',
  'Red with a white border, required of the Gulf sheikhdoms by their 1820 treaty with Britain.')
D('ma-red', 'Red flag of Morocco', rect('#c1272d'), 'flag', 'The plain red flag of the Alaouite sultans; the green star was added in 1915.')
D('ye-mutawakkil', 'Flag of the Kingdom of Yemen', rect('#c8102e') +
  '<path d="M14 26H42L46 22.5L42 19H14Z" fill="#fff"/>' + ''.join(star(WHITE, x, y, 2.4) for x, y in ((20, 11), (27, 9), (34, 9), (41, 11), (48, 14))),
  'flag', 'The Mutawakkilite kingdom, 1918-1962: a sword and five stars.')
D('ye-yar', 'Flag of the Yemen Arab Republic', hs('#ce1126', WHITE, BLACK) + star('#007a3d', 30, 22.5, 4.5), 'flag', 'North Yemen, 1962-1990.')
D('eg-1867', 'Flag of the Khedivate of Egypt', rect('#c8102e') + ''.join(crescent(WHITE, x, y, 6, .34, .8, 0) + star(WHITE, x + 2.2, y, 2.2)
                                                                    for x, y in ((16, 22.5), (32, 13), (32, 32))), 'flag',
  'Egypt under the Muhammad Ali dynasty, 1867-1922.')
D('eg-1922', 'Flag of the Kingdom of Egypt', rect('#0c8a3c') + crescent(WHITE, 26, 22.5, 12, .32, .8, 0) +
  ''.join(star(WHITE, x, y, 2.6) for x, y in ((33, 16), (35.5, 22.5), (33, 29))), 'flag', 'Egypt, 1922-1953.')
D('eg-1953', 'Flag of the Egyptian revolution', hs('#ce1126', WHITE, BLACK) + emblem('falcon', '#c09300', 30, 22.5, 14), 'flag',
  'Red, white and black with the eagle, 1953-1958.')
D('uar', 'Flag of the United Arab Republic', hs('#ce1126', WHITE, BLACK) + star('#007a3d', 23, 22.5, 4) + star('#007a3d', 37, 22.5, 4), 'flag',
  'The union of Egypt and Syria, 1958-1961; Egypt kept it until 1972, and Syria took it back in 1980.')
D('arab-fed', 'Flag of the Federation of Arab Republics', hs('#ce1126', WHITE, BLACK) + emblem('falcon', '#c09300', 30, 22.5, 14), 'flag',
  'The Hawk of Quraish, flown by Egypt, Syria and Libya in the 1970s.')
D('sy-1932', 'Syrian independence flag', hs('#007a3d', WHITE, BLACK) + ''.join(star('#ce1126', x, 22.5, 3.6) for x in (20, 30, 40)), 'flag',
  'Flown at independence, in 1932-1958 and 1961-1963, by the 2011 uprising, and as the national flag again from 2025.')
D('three-stars', 'Flag with three stars', hs('#ce1126', WHITE, BLACK) + ''.join(star('#007a3d', x, 22.5, 3.6) for x in (20, 30, 40)), 'flag',
  'The planned union of Egypt, Syria and Iraq, 1963: Syria flew it until 1972 and Iraq until 1991.')
D('iq-1921', 'Flag of the Kingdom of Iraq', hs(BLACK, WHITE, '#007a3d') + poly('#ce1126', [(0, 0), (16, 11), (16, 34), (0, 45)]) +
  star(WHITE, 6, 17, 2.6, 7) + star(WHITE, 6, 28, 2.6, 7), 'flag', 'The Hashemite kingdom, 1921-1958.')
D('iq-1959', 'Flag of the Iraqi Republic', vs(BLACK, WHITE, '#007a3d') + star('#ce1126', 30, 22.5, 9, 8, -90, .6) + disc('#f2c318', 30, 22.5, 4),
  'flag', 'Under Qasim, 1959-1963.')
D('iq-1991', 'Flag of Iraq, 1991-2004', hs('#ce1126', WHITE, BLACK) + ''.join(star('#007a3d', x, 22.5, 3.6) for x in (20, 30, 40)) +
  text('الله أكبر', '#007a3d', 30, 29, 4, font='DejaVu Sans', weight='normal'), 'flag', 'With "God is great" added in 1991.')
D('ly-1969', 'Flag of the Libyan Arab Republic', hs('#ce1126', WHITE, BLACK), 'flag', 'Libya, 1969-1972.')
D('ly-1977', 'Flag of the Libyan Jamahiriya', rect('#009a3a'), 'flag', 'Plain green, 1977-2011.')
D('af-black', 'Black flag of Afghanistan', rect(BLACK), 'flag', 'Abdur Rahman Khan\'s plain black flag, 1880-1901.')
D('af-1901', 'Flag of Afghanistan, 1901-1926', rect(BLACK) + ring(WHITE, 30, 22.5, 9, 2) + emblem('mosque', WHITE, 30, 23, 11), 'flag',
  'Black with the white seal of the emir.')
D('af-1930', 'Flag of the Kingdom of Afghanistan', vs(BLACK, '#bf0000', '#009900') + ring(WHITE, 30, 22.5, 8, 1.5) + emblem('mosque', WHITE, 30, 23, 9),
  'flag', 'Black, red and green with the mosque, 1928-1973.')
D('af-1978', 'Flag of the Khalq government', rect('#c00') + star(GOLD, 9, 8, 3) + ring(GOLD, 9, 10, 5, 1), 'flag',
  'Afghanistan\'s communist flag, 1978-1980.')
D('af-1980', 'Flag of the Democratic Republic of Afghanistan', hs(BLACK, '#c00', '#009900') + ring(GOLD, 11, 10, 6, 1.2) + star('#c00', 11, 8, 2.4), 'flag',
  'Black, red and green with the state emblem, 1980-1992.')
D('af-1992', 'Flag of the Islamic State of Afghanistan', hs('#009900', WHITE, BLACK) + text('الله أكبر', '#009900', 30, 22.5, 5, font='DejaVu Sans', weight='normal'),
  'flag', 'Green, white and black, 1992-2001.')
D('af-taliban', 'Flag of the Islamic Emirate', rect(WHITE) + border('#c9c2b0', 1) +
  text('لا إله إلا الله محمد رسول الله', BLACK, 30, 22.5, 4.6, font='DejaVu Sans', weight='normal'), 'flag',
  'The Taliban\'s white flag with the Shahada, 1997-2001 and again from 2021.')

# ---------- Japan, Korea and South-East Asia ----------
D('siam-red', 'Red flag of Siam', rect('#c8102e'), 'flag', 'Siam\'s plain red flag, flown from the late 1600s.')
D('siam-chakra', 'Flag of Siam with the chakra', rect('#c8102e') + emblem('chakra', WHITE, 30, 22.5, 22), 'flag',
  'Rama II added the white chakra of Vishnu, 1817.')
D('siam-elephant', 'Elephant flag of Siam', rect('#c8102e') + emblem('elephant', WHITE, 30, 23, 30), 'flag',
  'King Mongkut set a white elephant on the red flag in 1855; it flew until the stripes of 1917.')
D('la-1952', 'Flag of the Kingdom of Laos', rect('#ce1126') + emblem('elephant', WHITE, 30, 25, 26) + rect(WHITE, 22, 31, 16, 2) + rect(WHITE, 28, 6, 4, 6),
  'flag', 'Erawan, the three-headed white elephant under a parasol, 1952-1975.')
D('kh-1970', 'Flag of the Khmer Republic', rect('#032ea1') + canton(rect('#e00025') + emblem('castle', WHITE, 30, 22.5, 26), 24, 18) +
  ''.join(star(WHITE, x, y, 2.4) for x, y in ((40, 6), (52, 6), (46, 12))), 'flag', 'Cambodia under Lon Nol, 1970-1975.')
D('kh-1976', 'Flag of Democratic Kampuchea', rect('#e00025') + emblem('castle', GOLD, 30, 22, 22), 'flag',
  'Red with Angkor Wat in yellow, 1975-1989.')
D('vn-south', 'Flag of South Vietnam', rect('#ffdd00') + rect('#da251d', 0, 16.5, W, 3) + rect('#da251d', 0, 21, W, 3) + rect('#da251d', 0, 25.5, W, 3),
  'flag', 'The State of Vietnam and the Republic of Vietnam, 1949-1975.')
D('mm-1948', 'Flag of the Union of Burma', rect('#e40000') + rect('#000080', 0, 0, 27, 22.5) + star(WHITE, 13.5, 11.25, 6.5) +
  ''.join(star(WHITE, 13.5 + 8.5 * math.cos(math.radians(a)), 11.25 + 8.5 * math.sin(math.radians(a)), 1.7) for a in range(-90, 270, 72)),
  'flag', 'Burma, 1948-1974.')
D('mm-1974', 'Flag of the Socialist Republic of the Union of Burma', rect('#e40000') + rect('#000080', 0, 0, 27, 22.5) + ring(WHITE, 13.5, 11.25, 6, 2) +
  ''.join(star(WHITE, 13.5 + 8.5 * math.cos(math.radians(a)), 11.25 + 8.5 * math.sin(math.radians(a)), 1.4) for a in [i * 360 / 14 - 90 for i in range(14)]),
  'flag', 'Burma, 1974-2010.')
D('my-1950', 'Flag of the Federation of Malaya', hs(*(['#cc0001', WHITE] * 5 + ['#cc0001'])) + rect('#010066', 0, 0, 30, 24.5) +
  crescent('#fc0', 12, 12.25, 8, .3, .8, 0) + star('#fc0', 20, 12.25, 5, 11, -90, .5), 'flag', 'Malaya, 1950-1963.')
D('kandy', 'Flag of the Kingdom of Kandy', rect('#8d153a') + border('#ffbe29', 3) + emblem('lion_passant', '#ffbe29', 30, 22.5, 36), 'flag',
  'The lion flag of the last Sinhalese kingdom, taken by the British in 1815.')

# ---------- South Asia ----------
D('maratha', 'Bhagwa Dhwaj', poly(SAFFRON, [(0, 0), (60, 0), (44, 22.5), (60, 45), (0, 45)]), 'flag',
  'The saffron swallow-tailed banner of Shivaji and the Maratha Confederacy.')
D('eic-1707', 'Flag of the East India Company', hs(*(['#c8102e', WHITE] * 6 + ['#c8102e'])) + union_1707(27, 21), 'flag',
  'Thirteen red and white stripes with the Union in the corner, 1707-1801.')
D('eic-1801', 'Flag of the East India Company', hs(*(['#c8102e', WHITE] * 6 + ['#c8102e'])) + union_1801(27, 21), 'flag',
  'The Company\'s flag after the Union of 1801, until its rule ended in 1858.')
D('in-raj', 'Flag of British India', ensign('#c8102e', disc('#7ab4dc', 45, 22.5, 7) + star(WHITE, 45, 22.5, 5) + ring(GOLD, 45, 22.5, 7.5, 1)),
  'flag', 'The red ensign with the Star of India, flown for British India from 1880 to 1947.')

# ---------- Europe ----------
D('hre-1', 'Banner of the Holy Roman Empire', rect('#f7cf26') + emblem('eagle', BLACK, 30, 23, 38), 'banner',
  'The black imperial eagle on gold, the emperors\' banner from the 1100s.', tint=46)
D('hre-2', 'Banner of the Holy Roman Empire', rect('#f7cf26') + emblem('eagle2', BLACK, 30, 23, 38), 'banner',
  'The double-headed eagle, used by the emperors from Sigismund (1433) until the empire ended in 1806.', tint=46)
D('fr-ancien', 'Royal banner of France', rect('#1f3f99') + lilies(GOLD, [(10, 9), (30, 9), (50, 9), (20, 22.5), (40, 22.5), (10, 36), (30, 36), (50, 36)], 11),
  'banner', 'Gold lilies strewn on blue, the arms of the Capetian kings ("France Ancient").', tint=222)
D('fr-moderne', 'Royal banner of France', rect('#1f3f99') + lilies(GOLD, [(19, 14), (41, 14), (30, 32)], 15), 'banner',
  'Three gold lilies on blue, the kings\' arms from Charles V (c. 1376) to the Revolution.', tint=222)
D('fr-bourbon', 'White flag of the Bourbon Restoration', rect(WHITE) + border('#d9d4c8', .8) +
  emblem('shield', '#1f3f99', 30, 22.5, 26) + lilies(GOLD, [(27, 18), (33, 18), (30, 25)], 5), 'flag',
  'The returning Bourbon kings flew white, 1814-1830.', tint=222)
D('gb-1707', 'Union Flag of Great Britain', union_1707(), 'flag', 'England\'s cross over Scotland\'s saltire, 1606 at sea and 1707-1801 for the kingdom.')
D('en-royal', 'Royal Banner of England', rect('#c8102e') + emblem('lions3', GOLD, 30, 22.5, 42), 'banner',
  'Three gold lions on red, the arms of the English kings from Richard I.')
D('ie-harp', 'Flag of the Kingdom of Ireland', rect('#0b4ea2') + emblem('harp', GOLD, 30, 22.5, 34), 'flag', 'A gold harp on blue, 1542-1801.')
D('brittany', 'Ermine flag of Brittany', rect(WHITE) + border('#d9d4c8', .8) +
  '<g fill="#111">%s</g>' % ''.join(ermine_spot(x, y, 1.1) for y in (9, 22.5, 36) for x in ((8, 22, 36, 50) if y != 22.5 else (15, 29, 43, 57))),
  'flag', 'Plain ermine, the arms of the dukes of Brittany from 1316.')
D('burgundy-cross', 'Cross of Burgundy', rect(WHITE) + border('#d9d4c8', .8) +
  '<g stroke="#c8102e" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="7 1.6"><path d="M6 5L54 40M54 5L6 40"/></g>', 'flag',
  'The ragged red saltire of Burgundy, carried by Spain\'s armies and ships from 1506 to 1785.', tint=355)
D('es-1785', 'Flag of Spain', hw(('#c60b1e', 1), ('#ffc400', 2), ('#c60b1e', 1)) + emblem('shield', '#c60b1e', 18, 22.5, 14) +
  emblem('castle', '#ffc400', 18, 22, 6), 'flag', 'Red and gold, chosen by Charles III in 1785 for his navy.')
D('es-1931', 'Flag of the Second Spanish Republic', hs('#da121a', '#f1bf00', '#3e2b5f'), 'flag', 'Red, yellow and purple, 1931-1939.')
D('es-franco', 'Flag of Francoist Spain', hw(('#c60b1e', 1), ('#ffc400', 2), ('#c60b1e', 1)) + emblem('eagle', BLACK, 30, 22.5, 18), 'flag',
  'The red and gold with the eagle of Saint John, 1938-1981.')
D('castile', 'Banner of Castile', rect('#c60b1e') + emblem('castle', GOLD, 30, 23, 30), 'banner', 'A gold castle on red, the arms of the kings of Castile.')
D('leon', 'Banner of León', rect(WHITE) + border('#d9d4c8', .8) + emblem('lion', '#7b2a7f', 30, 23, 32), 'banner', 'A purple lion on white, the arms of the kings of León.')
D('castile-leon', 'Banner of the Crown of Castile', rect('#c60b1e', 0, 0, 30, 22.5) + rect('#c60b1e', 30, 22.5, 30, 22.5) +
  rect(WHITE, 30, 0, 30, 22.5) + rect(WHITE, 0, 22.5, 30, 22.5) + emblem('castle', GOLD, 15, 11.5, 15) + emblem('castle', GOLD, 45, 34, 15) +
  emblem('lion', '#7b2a7f', 45, 11.5, 16) + emblem('lion', '#7b2a7f', 15, 34, 16), 'banner',
  'The castles of Castile quartered with the lions of León, after the crowns joined in 1230.', tint=355)
D('aragon', 'Senyera of Aragon', hs(*(['#fcdd09', '#da121a'] * 4 + ['#fcdd09'])), 'banner',
  'Four red bars on gold, the arms of the counts of Barcelona and kings of Aragon.')
D('navarre', 'Banner of Navarre', rect('#c8102e') +
  '<g stroke="%s" stroke-width="1.6" fill="none" stroke-dasharray="2.2 .9"><rect x="4" y="4" width="52" height="37"/><path d="M30 4V41M4 22.5H56M4 4L56 41M56 4L4 41"/></g>' % GOLD +
  disc('#1f8a3b', 30, 22.5, 3), 'banner', 'Gold chains on red, the arms of Navarre from about 1234.')
D('asturias', 'Victory Cross of Asturias', rect('#0b4ea2') +
  '<path d="M28 6H32V40H28Z M18 14H42V18H18Z" fill="%s"/>' % GOLD + text('A', GOLD, 22.5, 25, 6) + text('Ω', GOLD, 37.5, 25, 6), 'emblem',
  'The jewelled Cross of Victory, given by Alfonso III in 908, emblem of the first Christian kingdom of Spain.')
D('pt-old', 'Royal banner of Portugal', rect(WHITE) + border('#d9d4c8', .8) + emblem('shield', '#c8102e', 30, 22.5, 30) +
  emblem('shield', WHITE, 30, 21.5, 20) + ''.join(rect('#1f3f99', x - 1.6, y - 2, 3.2, 4) for x, y in ((30, 14.5), (30, 20.5), (24.5, 20.5), (35.5, 20.5), (30, 26.5))),
  'flag', 'The arms of Portugal (five blue shields inside a red border of castles) on white.')
D('pt-1830', 'Flag of the Kingdom of Portugal', rect('#1f3f99', 0, 0, 30, 45) + rect(WHITE, 30, 0, 30, 45) + emblem('shield', '#c8102e', 30, 22.5, 22) +
  emblem('shield', WHITE, 30, 21.8, 14) + ''.join(rect('#1f3f99', x - 1.2, y - 1.5, 2.4, 3) for x, y in ((30, 17), (30, 21.5), (26, 21.5), (34, 21.5), (30, 26))),
  'flag', 'Blue and white, the constitutional monarchy, 1830-1910.')
D('prinsenvlag', 'Prince\'s Flag', hs('#f47b20', WHITE, '#1f3f99'), 'flag',
  'Orange, white and blue, the colours of William of Orange, flown in the Dutch Revolt.')
D('helvetic', 'Flag of the Helvetic Republic', hs('#00843d', '#ce1126', '#f2c318'), 'flag', 'Green, red and yellow, 1798-1803.')
D('geneva', 'Flag of Geneva', '<clipPath id="gv"><rect width="30" height="45"/></clipPath>' + rect('#f7d117', 0, 0, 30, 45) +
  '<g clip-path="url(#gv)">%s</g>' % emblem('eagle', BLACK, 30, 22.5, 34) + rect('#c8102e', 30, 0, 30, 45) + emblem('key', GOLD, 44, 22.5, 32),
  'flag', 'Half the imperial eagle and the key of Saint Peter.')
D('hamburg', 'Flag of Hamburg', rect('#da291c') + emblem('castle', WHITE, 30, 23, 30), 'flag', 'A white castle on red.')
D('prussia', 'Flag of Prussia', rect(WHITE) + border('#d9d4c8', .8) + emblem('eagle', BLACK, 30, 22.5, 36), 'flag',
  'The black eagle on white, Prussia\'s arms since the Teutonic Order.')
D('brandenburg', 'Flag of Brandenburg', rect(WHITE) + border('#d9d4c8', .8) + emblem('eagle', '#c8102e', 30, 22.5, 36), 'flag', 'The red eagle of Brandenburg.')
D('bavaria', 'Lozenges of Bavaria', rect(WHITE) + '<g fill="#0098d4">%s</g>' % ''.join(
  '<path d="M%s %sl6 -5l6 5l-6 5Z"/>' % (f(x), f(y)) for x in range(-6, 61, 12) for y in range(0, 50, 10)) + border('#d9d4c8', .6),
  'flag', 'The white and blue lozenges of the Wittelsbach dukes and kings of Bavaria.')
D('saxony', 'Flag of Saxony', hs(WHITE, '#009a49'), 'flag', 'White and green, the Kingdom of Saxony.')
D('hanover', 'Flag of Hanover', rect('#c8102e') + emblem('horse', WHITE, 30, 22.5, 34), 'flag', 'The white Saxon steed on red.')
D('de-empire', 'Flag of the German Empire', hs(BLACK, WHITE, '#dd0000'), 'flag',
  'Black, white and red, the North German Confederation and the German Empire, 1867-1918 (and co-official 1933-1935).')
D('de-nazi', 'Flag of Nazi Germany', rect('#dd0000') + disc(WHITE, 30, 22.5, 13) +
  '<g transform="rotate(45 30 22.5)">%s</g>' % emblem('swastika', BLACK, 30, 22.5, 19),
  'flag', 'The flag of the Nazi dictatorship, 1935-1945.')
D('ddr', 'Flag of East Germany', hs(BLACK, '#dd0000', '#ffce00') + ring('#ffce00', 30, 22.5, 8.5, 2.2) + disc('#dd0000', 30, 22.5, 7.3) +
  '<g stroke="#ffce00" stroke-width="1.4" fill="none"><path d="M30 16V28M26 17H34"/><path d="M26 29L30 18L34 29"/><path d="M26.5 25H33.5"/></g>', 'flag',
  'The German Democratic Republic, with the hammer and compass, 1959-1990.')
D('habsburg', 'Black and gold flag of Austria', hs(BLACK, '#f7cf26'), 'flag', 'The Habsburg colours, flag of the Austrian Empire.', tint=46)
D('austria-hungary', 'Flag of Austria-Hungary', rect('#c8102e') + rect(WHITE, 0, 15, 30, 15) + rect(WHITE, 30, 15, 30, 15) + rect('#477050', 30, 30, 30, 15) +
  emblem('shield', '#c8102e', 15, 22.5, 10) + emblem('shield', '#c8102e', 45, 22.5, 10), 'flag',
  'The civil ensign of 1869: Austria\'s red-white-red beside Hungary\'s red-white-green.')
D('hu-arpad', 'Árpád stripes', hs(*(['#c8102e', WHITE] * 4)), 'banner', 'Red and white stripes, the arms of the Árpád kings.')
D('hu-arms', 'Banner of the Kingdom of Hungary', rect('#c8102e', 0, 0, 30, 45) + ''.join(rect(WHITE, 0, 5.6 * i + 2.8, 30, 2.8) for i in range(8)) +
  rect('#c8102e', 30, 0, 30, 45) + emblem('doublecross', WHITE, 45, 20, 32) + poly('#477050', [(35, 45), (38, 38), (45, 35), (52, 38), (55, 45)]),
  'banner', 'The Árpád stripes beside the double cross on its green hill.')
D('bohemia', 'Banner of Bohemia', rect('#c8102e') + emblem('lion', WHITE, 30, 23, 34), 'banner', 'The silver double-tailed lion of the kings of Bohemia.')
D('pl-eagle', 'Banner of the Kingdom of Poland', rect('#dc143c') + emblem('eagle', WHITE, 30, 22.5, 36) + emblem('crown', GOLD, 30, 8.5, 7), 'banner',
  'The crowned white eagle on red, Poland\'s arms from 1295.')
D('lt-vytis', 'Vytis', rect('#c1272d') + emblem('vytis', WHITE, 30, 23, 38), 'banner', 'The white knight on a red field, the arms of the grand dukes of Lithuania.')
D('pl-lt', 'Banner of Poland and Lithuania', rect('#c1272d') + emblem('eagle', WHITE, 15, 11.5, 18) + emblem('vytis', WHITE, 45, 11.5, 18) +
  emblem('vytis', WHITE, 15, 34, 18) + emblem('eagle', WHITE, 45, 34, 18), 'banner', 'The white eagle of Poland quartered with the knight of Lithuania.')
D('plc', 'Banner of the Polish-Lithuanian Commonwealth', hs('#c1272d', WHITE, '#c1272d') + emblem('shield', '#c1272d', 30, 22.5, 20) +
  emblem('eagle', WHITE, 30, 21, 9), 'banner', 'Red and white with the arms of the Commonwealth, 1569-1795.')
D('teutonic', 'Flag of the Teutonic Order', rect(WHITE) + border('#d9d4c8', .8) + emblem('cross_pattee', BLACK, 30, 22.5, 34), 'flag',
  'The black cross on white of the Teutonic Knights.')
D('kalmar', 'Banner of the Kalmar Union', rect('#f7cf26') + nordic('#c8102e', 7, 22), 'banner', 'A red cross on gold, the union of Denmark, Norway and Sweden, 1397-1523.')
D('se-crowns', 'Three Crowns of Sweden', rect('#006aa7') + ''.join(emblem('crown', '#fecc00', x, y, 12) for x, y in ((21, 15), (39, 15), (30, 31))),
  'banner', 'Three gold crowns on blue, the Swedish kings\' arms from 1336.')
D('se-1818', 'Union flag of Sweden', rect('#006aa7') + nordic('#fecc00', 7, 22) + rect('#c8102e', 0, 0, 18.5, 19) + '<path d="M0 0L18.5 19M18.5 0L0 19" stroke="#fff" stroke-width="2.4"/>',
  'flag', 'Sweden\'s flag with Norway\'s saltire in the corner, 1818-1844.')
D('se-1844', 'Union flag of Sweden', rect('#006aa7') + nordic('#fecc00', 7, 22) +
  canton(rect('#006aa7', 0, 0, 30, 22.5) + rect('#c8102e', 30, 22.5, 30, 22.5) + '<path d="M0 0L60 45M60 0L0 45" stroke="#fecc00" stroke-width="5"/>' +
         cross('#c8102e', 9) + '<path d="M30 0V45M0 22.5H60" stroke="#fff" stroke-width="3"/>' +
         '<path d="M0 0L30 22.5M60 45L30 22.5" stroke="#fecc00" stroke-width="5"/>', 18.5, 19), 'flag',
  'With the union mark of Sweden and Norway, 1844-1905.')
D('no-lion', 'Royal banner of Norway', rect('#c8102e') + emblem('lion', GOLD, 30, 23, 34), 'banner', 'The gold lion with Saint Olaf\'s axe, from about 1280.')
D('no-1814', 'Flag of Norway, 1814-1821', rect('#c8102e') + cross(WHITE, 6, 21, 22.5) + canton(rect('#c8102e') + emblem('lion', GOLD, 30, 23, 34), 18, 19.5),
  'flag', 'The Danish flag with the Norwegian lion, used after independence from Denmark.')
D('rus-trident', 'Trident of Volodymyr', rect('#c8102e') + emblem('trident', GOLD, 30, 22.5, 34), 'emblem',
  'The trident sign of Prince Volodymyr the Great, struck on his coins. Rus had no flag.')
D('muscovy', 'Banner of Muscovy', rect('#c8102e') + emblem('eagle2', GOLD, 30, 23, 38), 'banner',
  'The double-headed eagle Ivan III took up after marrying the Byzantine princess Sophia Palaiologina.')
D('rsfsr', 'Flag of Soviet Russia', rect('#cc0000') + text('РСФСР', GOLD, 13, 9, 6.4, font='DejaVu Sans'), 'flag', 'The Russian Soviet Republic, 1918-1922.')
D('su', 'Flag of the Soviet Union', rect('#cc0000') + emblem('hammersickle', '#ffd700', 11, 12, 13) +
  star_outline('#ffd700', 11, 5, 2, .6), 'flag', 'The hammer and sickle with the red star, 1922-1991.')
D('ua-ssr', 'Flag of the Ukrainian SSR', hw(('#d40000', 2), ('#0057b8', 1)) + emblem('hammersickle', '#ffd700', 8, 7, 9), 'flag', '1949-1991.')
D('by-1991', 'White-red-white flag of Belarus', hs(WHITE, '#c8102e', WHITE), 'flag', 'Belarus, 1918 and 1991-1995.')
D('ge-1918', 'Flag of the Democratic Republic of Georgia', rect('#8b0000') + canton(hs(BLACK, WHITE), 24, 15), 'flag', 'Georgia 1918-1921 and 1990-2004.')
D('venice', 'Flag of the Republic of Venice', rect('#b5121b') + emblem('lion_mark', GOLD, 30, 22.5, 38), 'flag',
  'The winged lion of Saint Mark on red.', tint=2)
D('genoa', 'Flag of the Republic of Genoa', rect(WHITE) + border('#d9d4c8', .8) + cross('#c8102e', 8), 'flag', 'Saint George\'s red cross on white.')
D('papal-old', 'Banner of the Papal States', rect('#c8102e') + emblem('keys', GOLD, 30, 22.5, 32), 'banner', 'The crossed keys of Saint Peter.')
D('papal', 'Flag of the Papal States', vs('#ffe000', WHITE) + border('#d9d4c8', .6) + emblem('keys', '#b88a00', 30, 24, 24) + emblem('crown', '#b88a00', 30, 11, 8),
  'flag', 'Yellow and white with the keys and the papal tiara, 1803-1870.')
D('savoy', 'Flag of Savoy', rect('#c8102e') + cross(WHITE, 8), 'flag', 'The white cross of the dukes of Savoy, also flown by the Kingdom of Sardinia.')
D('two-sicilies', 'Flag of the Two Sicilies', rect(WHITE) + border('#d9d4c8', .8) + emblem('shield', '#1f3f99', 30, 22.5, 26) +
  lilies(GOLD, [(26, 18), (34, 18), (30, 26)], 6) + emblem('crown', GOLD, 30, 7.5, 6), 'flag', 'White with the Bourbon arms, 1734-1861.')
D('sicily-arag', 'Banner of the Kingdom of Sicily', rect(WHITE) +
  '<clipPath id="sa"><path d="M0 0L60 0L30 22.5Z M0 45L60 45L30 22.5Z"/></clipPath><g clip-path="url(#sa)">%s</g>' % vs(*(['#fcdd09', '#da121a'] * 4 + ['#fcdd09'])) +
  emblem('eagle', BLACK, 10, 22.5, 14) + emblem('eagle', BLACK, 50, 22.5, 14), 'banner',
  'The bars of Aragon and the eagles of the Hohenstaufen, the arms of the Aragonese kings of Sicily.')
D('it-savoy', 'Flag of the Kingdom of Italy', vs('#009246', WHITE, '#ce2b37') + emblem('shield', '#1f3f99', 30, 22.5, 18) +
  emblem('shield', '#ce2b37', 30, 22.3, 15) + rect(WHITE, 29, 16.5, 2, 12) + rect(WHITE, 25.5, 20.5, 9, 2), 'flag', 'The tricolour with the arms of Savoy, 1848-1946.')
D('cy-lusignan', 'Banner of the Kingdom of Cyprus', rect(WHITE, 0, 0, 30, 22.5) + emblem('jerusalem', GOLD, 15, 11.5, 18) +
  ''.join(rect('#1f3f99' if i % 2 else WHITE, 30, i * 2.8125, 30, 2.8125) for i in range(8)) +
  emblem('lion', '#c8102e', 45, 11.5, 18) + rect(GOLD, 0, 22.5, 60, 22.5) + emblem('lion', '#c8102e', 15, 34, 18) + emblem('lion', '#c8102e', 45, 34, 18),
  'banner', 'Jerusalem, Lusignan, Cyprus and Armenia quartered, the arms of the Lusignan kings, 1192-1489.')
D('jerusalem', 'Banner of the Kingdom of Jerusalem', rect(WHITE) + border('#d9d4c8', .8) + emblem('jerusalem', GOLD, 30, 22.5, 36), 'banner',
  'Gold crosses on white, the arms of the crusader kings of Jerusalem.')
D('st-john', 'Flag of the Knights of Saint John', rect('#c8102e') + cross(WHITE, 8), 'flag', 'The white cross on red of the Knights Hospitaller.')
D('gr-cross', 'Flag of the Kingdom of Greece', rect('#0d5eaf') + cross(WHITE, 9), 'flag', 'The white cross on blue, Greece\'s land flag, 1822-1969.')
D('me-krstas', 'Krstaš-barjak', rect('#c8102e') + border(WHITE, 3) + cross(WHITE, 6), 'flag', 'The red battle flag of Montenegro with its white cross.')
D('me-1880', 'Flag of Montenegro', hs('#c8102e', '#1f3f99', WHITE), 'flag', 'The principality and kingdom, 1880-1918.')
D('rs-nemanjic', 'Banner of the Nemanjić', rect('#c8102e') + emblem('eagle2', WHITE, 30, 23, 36), 'banner', 'The white double-headed eagle of medieval Serbia.')
D('rs-1835', 'Flag of the Principality of Serbia', hs('#c6363c', '#0c4076', WHITE), 'flag', 'Red, blue and white, from 1835.')
D('ba-kotromanic', 'Banner of the Kingdom of Bosnia', rect('#1f3f99') + '<path d="M0 8L52 45H60V37L8 0H0Z" fill="#fff"/>' +
  lilies(GOLD, [(14, 30), (22, 37), (38, 9), (46, 16)], 7), 'banner', 'The Kotromanić arms: lilies on blue, crossed by a white bend.')
D('ba-1992', 'Flag of Bosnia and Herzegovina, 1992-1998', rect(WHITE) + border('#d9d4c8', .8) + emblem('shield', '#1f3f99', 30, 22.5, 26) +
  '<path d="M23 14L37 32" stroke="#fff" stroke-width="2.4"/>' + lilies(GOLD, [(26, 25), (34, 19)], 5), 'flag', 'White with the lilies of Kotromanić.')
D('mk-1992', 'Flag of Macedonia, 1992-1995', rect('#d20000') + emblem('vergina', '#ffe600', 30, 22.5, 34), 'flag', 'The Vergina Sun on red.')
D('al-1946', 'Flag of Socialist Albania', rect('#e41e20') + emblem('eagle2', BLACK, 30, 25, 32) + star_outline('#ffd700', 30, 8, 3.4),
  'flag', 'The eagle with a red star, 1946-1992.')
D('ro-1965', 'Flag of Socialist Romania', vs('#002b7f', '#fcd116', '#ce1126') + emblem('shield', '#3a7d44', 30, 22.5, 9) + disc('#fcd116', 30, 21, 2.4), 'flag',
  'With the state emblem, 1948-1989.')
D('bg-1971', 'Flag of the People\'s Republic of Bulgaria', hs(WHITE, '#00966e', '#d62612') + ring('#d9b100', 9, 13, 4.5, 1.2) + emblem('lion', '#d9b100', 9, 13, 6),
  'flag', 'With the state emblem, 1946-1990.')
D('hr-ssr', 'Flag of Socialist Croatia', hs('#ff0000', WHITE, '#171796') + star('#ff0000', 30, 22.5, 11), 'flag', 'With the red star, 1947-1990.')
D('hr-checky', 'Banner of Croatia', rect(WHITE) + ''.join(rect('#c8102e', 12 + c * 7.2, 4.5 + r * 7.2, 7.2, 7.2) for r in range(5) for c in range(5) if (r + c) % 2 == 0),
  'banner', 'The red and white checkerboard, Croatia\'s arms from the 1400s.')
D('yu-kingdom', 'Flag of the Kingdom of Yugoslavia', hs('#1f3f99', WHITE, '#c8102e'), 'flag', '1918-1941.')
D('yu-sfr', 'Flag of Socialist Yugoslavia', hs('#1f3f99', WHITE, '#c8102e') + star('#c8102e', 30, 22.5, 13) +
  star_outline('#fcd116', 30, 22.5, 13, .8), 'flag', 'With the red star, 1945-1992.')
D('lv-ssr', 'Flag of the Latvian SSR', rect('#c8102e') + ''.join(rect('#1f6db6' if i % 2 == 0 else WHITE, 0, 32 + i * 2.2, 60, 2.2) for i in range(6)) +
  emblem('hammersickle', GOLD, 8, 8, 9), 'flag', '1953-1990.')
D('ee-ssr', 'Flag of the Estonian SSR', rect('#c8102e') + ''.join(rect('#1f6db6' if i % 2 == 0 else WHITE, 0, 30 + i * 2.5, 60, 2.5) for i in range(5)) +
  emblem('hammersickle', GOLD, 8, 8, 9), 'flag', '1953-1990.')
D('lt-ssr', 'Flag of the Lithuanian SSR', hw(('#c8102e', 8), (WHITE, 1), ('#00843d', 3)) + emblem('hammersickle', GOLD, 8, 8, 9), 'flag', '1953-1988.')

# ---------- the Americas ----------
def us_flag(n):
    """the Stars and Stripes with n stars: 13 in a ring (1777), 15 stripes and stars (1795), then 13 stripes and rows of stars"""
    stripes = 15 if n == 15 else 13
    out = hs(*(['#b22234', WHITE] * (stripes // 2) + ['#b22234']))
    cw, ch = 24, H * 7 / stripes
    out += rect('#3c3b6e', 0, 0, cw, ch)
    if n == 13:
        return out + ''.join(star(WHITE, cw / 2 + 7.5 * math.cos(math.radians(a)), ch / 2 + 7.5 * math.sin(math.radians(a)), 1.45)
                             for a in [i * 360 / 13 - 90 for i in range(13)])
    best = None
    for r in range(3, 10):
        c = math.ceil(n / r)
        waste = r * c - n; shape = abs((cw / c) / (ch / r) - 1)
        score = .3 * waste + 3 * shape
        if best is None or score < best[0]: best = (score, r, c)
    _, r, c = best
    rows = [c] * (n // c) + ([n % c] if n % c else [])
    out_s = ''
    for i, k in enumerate(rows):
        y = ch * (i + .5) / len(rows)
        for j in range(k):
            x = cw * (j + .5 + (c - k) / 2) / c
            out_s += star(WHITE, x, y, min(cw / c, ch / len(rows)) * .42)
    return out + out_s


US_STARS = [(1777, 13), (1795, 15), (1818, 20), (1819, 21), (1820, 23), (1822, 24), (1836, 25), (1837, 26), (1845, 27), (1846, 28),
            (1847, 29), (1848, 30), (1851, 31), (1858, 32), (1859, 33), (1861, 34), (1863, 35), (1865, 36), (1867, 37), (1877, 38),
            (1890, 43), (1891, 44), (1896, 45), (1908, 46), (1912, 48), (1959, 49)]
for y, n in US_STARS:
    D('us-%d' % n, 'Flag of the United States, %d stars' % n, us_flag(n), 'flag',
      'The flag gains a star for each new state. This one flew from %d.' % y, tint=218)
D('us-grand-union', 'Grand Union Flag', hs(*(['#b22234', WHITE] * 6 + ['#b22234'])) + union_1707(24, 24.2), 'flag',
  'The Continental Army\'s first flag, 1775-1777.', tint=218)
D('br-empire', 'Flag of the Empire of Brazil', rect('#00923f') + poly('#f8c300', [(30, 4), (56, 22.5), (30, 41), (4, 22.5)]) +
  emblem('shield', '#00923f', 30, 23, 18) + ring('#1f3f99', 30, 22.5, 4, 1.4) + emblem('crown', '#c79a10', 30, 12, 7), 'flag', 'Green and gold with the imperial arms, 1822-1889.')
D('ca-red', 'Canadian Red Ensign', ensign('#c8102e', emblem('shield', '#f2ead8', 45, 23, 18) +
  # the 1921 arms: England, Scotland, Ireland and France over three red maple leaves
  rect('#c8102e', 40.3, 17.6, 4.7, 3.2) + rect('#f0c419', 45, 17.6, 4.7, 3.2) + rect('#1f3f99', 40.3, 20.8, 4.7, 3.2) + rect('#1f3f99', 45, 20.8, 4.7, 3.2) +
  ''.join(disc('#c8102e', x, 26.6, 1.15) for x in (42.6, 45, 47.4))), 'flag',
  'Canada\'s flag in practice from 1868 to 1965, when the maple leaf replaced it.', tint=355)
D('hbc', 'Flag of the Hudson\'s Bay Company', ensign('#c8102e', text('HBC', WHITE, 45, 33, 7)), 'flag', 'The company that ruled Rupert\'s Land until 1870.', tint=355)
D('hawaii', 'Flag of the Kingdom of Hawaii', hs(WHITE, '#c8102e', '#1f3f99', WHITE, '#c8102e', '#1f3f99', WHITE, '#c8102e') + union_1801(26, 22.5), 'flag',
  'Eight stripes for the eight islands, with the Union Flag, 1845-1893.')
D('mx-1821', 'Flag of the First Mexican Empire', vs('#006847', WHITE, '#ce1126') + emblem('eagle', '#8a6a2a', 30, 22.5, 12) + emblem('crown', '#c79a10', 30, 15, 5),
  'flag', 'The crowned eagle of Agustín de Iturbide, 1821-1823.')
D('ht-1806', 'Flag of Haiti', hs('#00209f', '#d21034'), 'flag', 'Blue over red, from 1806 (the arms were added later).')
D('ht-1964', 'Flag of Duvalier\'s Haiti', vs(BLACK, '#d21034'), 'flag', 'Black and red, 1964-1986.')
D('sv-1865', 'Flag of El Salvador, 1865-1912', hs(*(['#0047ab', WHITE] * 4 + ['#0047ab'])) + rect('#c8102e', 0, 0, 24, 25) +
  ''.join(star(WHITE, 4 + (i % 4) * 5.5, 5 + (i // 4) * 5, 1.6) for i in range(14)), 'flag', 'Blue and white stripes with red and stars.')
D('united-tribes', 'Flag of the United Tribes of New Zealand', rect(WHITE) + cross('#c8102e', 7) +
  canton(rect('#1f3f99') + cross(BLACK, 12) + cross('#c8102e', 7) + ''.join(star(WHITE, x, y, 5, 8, -90, .45) for x, y in ((13, 10), (47, 10), (13, 35), (47, 35))), 26.5, 19),
  'flag', 'Chosen by Māori chiefs in 1834, and flown by many hapū after 1840.')

# ---------- Africa ----------
D('cd-1877', 'Flag of the Congo Free State', rect('#1f3f99') + star('#f7d618', 30, 22.5, 11), 'flag',
  'Blue with a gold star: Leopold II\'s Congo Free State and then the Belgian Congo, until 1960.')
D('cd-1960', 'Flag of the Republic of the Congo', rect('#0085ca') + star('#f7d618', 30, 22.5, 11) + ''.join(star('#f7d618', 4, 4 + 7.4 * i, 2.6) for i in range(6)),
  'flag', 'Congo-Léopoldville, 1960-1963, and again in 1997-2006.')
D('cd-1963', 'Flag of the Democratic Republic of the Congo, 1963-1971', rect('#0085ca') + '<path d="M0 45L50 0H60L10 45Z" fill="#f7d618"/>' +
  '<path d="M3 45L53 0H57L7 45Z" fill="#d21034"/>' + star('#f7d618', 11, 11, 7), 'flag', '')
D('zaire', 'Flag of Zaire', rect('#007a5e') + disc('#f7d618', 30, 22.5, 11) +
  # a brown arm raising a torch with a red flame
  '<path d="M36.5 31.5L31.6 24.6L29.2 26.2L33.6 33.2Z" fill="#7a4a22"/><ellipse cx="30.2" cy="24.6" rx="2.4" ry="2" fill="#7a4a22"/>'
  '<rect x="29.2" y="17.5" width="1.9" height="6.5" fill="#3d2a14"/>'
  '<path d="M30.1 11.2C27.4 13.6 27.2 16.3 30.1 18.4C33 16.3 32.8 13.6 30.1 11.2Z" fill="#d21034"/>', 'flag',
  'A hand holding a torch, Mobutu\'s Zaire, 1971-1997.')
D('cg-1970', 'Flag of the People\'s Republic of the Congo', rect('#e10000') + emblem('hammersickle', '#fcd116', 10, 10, 11), 'flag', '1970-1991.')
D('et-1897', 'Flag of the Ethiopian Empire', hs('#078930', '#fcdd09', '#da121a') + emblem('lion', '#7a4a00', 30, 23, 30) + rect('#7a4a00', 37, 8, 1.2, 20) + rect('#7a4a00', 35, 10, 5.2, 1.2), 'flag',
  'Green, gold and red with the Lion of Judah, from Menelik II to 1974.')
D('et-plain', 'Flag of Ethiopia', hs('#078930', '#fcdd09', '#da121a'), 'flag', 'The plain tricolour, 1975-1987 and 1991-1996.')
D('et-1987', 'Flag of the People\'s Democratic Republic of Ethiopia', hs('#078930', '#fcdd09', '#da121a') + ring('#0f47af', 30, 22.5, 7, 2) + star('#da121a', 30, 22.5, 3),
  'flag', '1987-1991.')
D('transvaal', 'Vierkleur', hs('#c8102e', WHITE, '#1f3f99') + rect('#007a4d', 0, 0, 16, 45), 'flag', 'The four-colour flag of the South African Republic (Transvaal), 1858-1902.')
D('ofs', 'Flag of the Orange Free State', hs(WHITE, '#f47b20', WHITE, '#f47b20', WHITE, '#f47b20', WHITE) + canton(hs('#c8102e', WHITE, '#1f3f99'), 20, 19.3),
  'flag', 'Orange and white stripes with the Dutch flag, 1857-1902.')
D('za-1928', 'Flag of the Union of South Africa', hs('#ff7f00', WHITE, '#00247d') +
  '<g transform="translate(21.5 18.5)">%s</g>' % union_1801(6, 4) + '<g transform="translate(27.8 18.5)">%s%s</g>' % (
      ''.join(rect('#ff7f00' if i % 2 else WHITE, 0, i * 8 / 7, 4.4, 8 / 7 + .02) for i in range(7)), rect('#00247d', 0, 0, 1.6, 2.4)) +
  '<g transform="translate(33 18.5)">%s%s%s%s</g>' % (rect('#c8102e', 0, 0, 6, 1.35), rect(WHITE, 0, 1.33, 6, 1.35), rect('#00247d', 0, 2.66, 6, 1.35), rect('#007a4d', 0, 0, 1.6, 4)), 'flag',
  'Orange, white and blue with three small flags (Britain, the Orange Free State and Transvaal), 1928-1994.')
D('za-1910', 'Red Ensign of South Africa', ensign('#c8102e', emblem('shield', '#e9e2cf', 45, 22.5, 14)), 'flag', 'The Union of South Africa, 1910-1928.')
D('rhodesia', 'Flag of Rhodesia', vs('#00843d', WHITE, '#00843d') + emblem('shield', '#00843d', 30, 22.5, 16) + emblem('pearl', '#c79a10', 30, 14, 6), 'flag',
  'Green and white, 1968-1979.')
D('ly-1951', 'Flag of the Kingdom of Libya', hw(('#e70013', 1), (BLACK, 2), ('#239e46', 1)) + crescent(WHITE, 29, 22.5, 8, .32, .8, 0) + star(WHITE, 34, 22.5, 3),
  'flag', 'Libya, 1951-1969, and again from 2011.')
D('bf-volta', 'Flag of Upper Volta', hs(BLACK, WHITE, '#c8102e'), 'flag', 'Black, white and red, the Volta rivers, 1959-1984.')
D('bj-1975', 'Flag of the People\'s Republic of Benin', rect('#008751') + star('#e8112d', 10, 10, 6), 'flag', '1975-1990.')
D('rw-1962', 'Flag of Rwanda, 1962-2001', vs('#e00000', '#fad201', '#007f3f') + text('R', BLACK, 30, 23, 18), 'flag', '')
D('mr-1959', 'Flag of Mauritania, 1959-2017', rect('#006233') + crescent('#ffc400', 30, 24, 10, .35, .8, 90) + star('#ffc400', 30, 18, 4.5), 'flag', '')
D('tanganyika', 'Flag of Tanganyika', hw(('#1eb53a', 5), ('#fcd116', 1), (BLACK, 6), ('#fcd116', 1), ('#1eb53a', 5)), 'flag', '1961-1964.')
D('sd-1956', 'Flag of Sudan, 1956-1970', hs('#0072c6', '#fcd116', '#007229'), 'flag', '')


# ---------- which flag each state flies, year by year ----------
# name -> [(from, to, flag)], years inclusive, None for open ends. A flag is an id above, 'iso:xx' for a modern flag from
# flag-icons, or '=Name' for whatever that state flies that year (a colony flying its ruler's flag).
N = None
TL = {
    # powers whose flags their colonies also fly
    'United Kingdom': [(N, 1706, 'iso:gb-eng'), (1707, 1800, 'gb-1707'), (1801, N, 'iso:gb')],
    'France': [(1137, 1375, 'fr-ancien'), (1376, 1789, 'fr-moderne'), (1790, 1813, 'iso:fr'), (1814, 1829, 'fr-bourbon'), (1830, N, 'iso:fr')],
    'Spain': [(N, 1505, 'castile-leon'), (1506, 1784, 'burgundy-cross'), (1785, 1930, 'es-1785'), (1931, 1938, 'es-1931'),
              (1939, 1977, 'es-franco'), (1978, N, 'iso:es')],
    'Portugal': [(1139, 1829, 'pt-old'), (1830, 1910, 'pt-1830'), (1911, N, 'iso:pt')],
    'Netherlands': [(1572, 1650, 'prinsenvlag'), (1651, N, 'iso:nl')],
    'Denmark': [(1219, N, 'iso:dk')],
    'Belgium': [(1831, N, 'iso:be')],
    'Italy': [(1848, 1945, 'it-savoy'), (1946, N, 'iso:it')],
    'Germany': [(1867, 1918, 'de-empire'), (1919, 1932, 'iso:de'), (1933, 1934, 'de-empire'), (1935, 1945, 'de-nazi'), (1949, N, 'iso:de')],
    'United States': [(1775, 1776, 'us-grand-union')] + [(y, (US_STARS[i + 1][0] - 1) if i + 1 < len(US_STARS) else 1959, 'us-%d' % n)
                                                       for i, (y, n) in enumerate(US_STARS)] + [(1960, N, 'iso:us')],
    'USSR': [(1918, 1922, 'rsfsr'), (1923, 1991, 'su')],
    'Russian Empire': [(1472, 1692, 'muscovy'), (1693, 1917, 'iso:ru')],
    'Japan': [(701, N, 'iso:jp')],
    'Ottoman Empire': [(1299, 1843, 'ottoman-red'), (1844, 1922, 'iso:tr')],
    'Sweden': [(1336, 1522, 'se-crowns'), (1523, N, 'iso:se')],
    'Austrian Empire': [(1526, 1866, 'habsburg'), (1867, 1918, 'austria-hungary')],
    'Egypt': [(1867, 1921, 'eg-1867'), (1922, 1952, 'eg-1922'), (1953, 1957, 'eg-1953'), (1958, 1971, 'uar'), (1972, 1983, 'arab-fed'), (1984, N, 'iso:eg')],
    'China': [(1912, 1927, 'roc-5'), (1928, 1948, 'iso:tw'), (1949, N, 'iso:cn')],
    'Qing Empire': [(1636, 1911, 'qing')],
    'Norway': [(1280, 1536, 'no-lion'), (1537, 1813, 'iso:dk'), (1814, 1820, 'no-1814'), (1821, N, 'iso:no')],
    'Persia': [(224, 651, 'sasanian'), (1501, 1735, 'safavid'), (1796, 1906, 'qajar'), (1907, 1979, 'ir-1907'), (1980, N, 'iso:ir')],

    # antiquity
    'Rome': [(-509, 311, 'rome-spqr'), (312, 476, 'labarum')],
    'Roman Empire': '=Rome', 'Roman Republic': '=Rome', 'Western Roman Empire': '=Rome',
    'Eastern Roman Empire': [(N, 311, 'rome-spqr'), (312, 1260, 'labarum'), (1261, 1453, 'byz-tetra')],
    'Byzantine Empire': '=Eastern Roman Empire',
    'Empire of Alexander': [(N, N, 'vergina')], 'Macedon and Hellenic League': [(N, N, 'vergina')], 'Kingdom of Kassander': [(N, N, 'vergina')],
    'Carthaginian Empire': [(N, -146, 'carthage')], 'Carthage': '=Carthaginian Empire',
    'Achaemenid Empire': [(N, N, 'achaemenid')],
    'Sasanian Empire': [(N, N, 'sasanian')], 'Sasanian dependencies': [(N, N, 'sasanian')],
    # China
    'Qin': [(-221, -206, 'qin')], 'Han': [(-202, 220, 'han')], 'Han Empire': '=Han', 'Jin': [(266, 420, 'jin')],
    'Sui Empire': [(581, 618, 'sui')], 'Tang Empire': [(618, 907, 'tang')], 'Song Empire': [(960, 1279, 'song')],
    'Great Khanate': [(1271, 1368, 'cathay')],
    'Ming Empire': [(1368, 1644, 'ming')], 'Ming Chinese Empire': '=Ming Empire',
    'Manchu Empire': '=Qing Empire',
    'Republic of China': '=China', 'Chinese Warlords': [(1912, 1927, 'roc-5')],
    'Manchuria': [(1912, 1931, 'roc-5'), (1932, 1945, 'manchukuo')],
    'Xinjiang': [(1912, 1927, 'roc-5'), (1928, 1949, 'iso:tw'), (1950, N, 'iso:cn')],
    'Taiwan': [(1683, 1894, 'qing'), (1895, 1944, 'iso:jp'), (1945, N, 'iso:tw')],
    'Tibet': [(1916, 1959, 'tibet')],
    'Mongol Empire': [(1206, 1368, 'mongol')],
    'Khanate of the Golden Horde': [(N, N, 'horde')], 'Golden Horde': [(N, N, 'horde')],
    'Ilkhanate': [(N, N, 'mongol-white')],
    'Timurid Empire': [(1370, 1507, 'timurid')], 'Timurid Emirates': '=Timurid Empire',
    'Mongolia': [(1921, 1991, 'mn-1945'), (1992, N, 'iso:mn')],
    # Japan and Korea
    'Yamato': '=Japan', 'Imperial Japan': '=Japan', 'Imperial Japan (Fujiwara)': '=Japan', 'Shogun Japan (Kamakura)': '=Japan',
    'Japan (Warring States)': '=Japan', 'Tokugawa shogunate': '=Japan', 'Empire of Japan': '=Japan',
    'Korea': [(1883, 1910, 'iso:kr'), (1911, 1945, 'iso:jp')],
    'Korea, Republic of': [(1948, N, 'iso:kr')], "Korea, Democratic People's Republic of": [(1948, N, 'iso:kp')],
    # Islamic world
    'Umayyad Caliphate': [(N, N, 'umayyad')], 'Emirate of Córdoba': [(N, N, 'umayyad')], 'Caliphate of Córdoba': [(N, N, 'umayyad')],
    'Abbasid Caliphate': [(N, N, 'abbasid')], 'Fatimid Caliphate': [(N, N, 'fatimid')], 'Almohad Caliphate': [(N, N, 'almohad')],
    'Mamluke Sultanate': [(N, N, 'mamluk')], 'Sultanate of Delhi': [(N, N, 'delhi')],
    'Ottoman Sultanate': [(N, 1922, 'iso:tr')], 'Republic of Turkey': [(1923, N, 'iso:tr')], 'Turkey': [(1923, N, 'iso:tr')],
    'Safavid Empire': [(1501, 1736, 'safavid')],
    'Iran': [(1907, 1979, 'ir-1907'), (1980, N, 'iso:ir')],
    'Afghanistan': [(1880, 1900, 'af-black'), (1901, 1927, 'af-1901'), (1928, 1977, 'af-1930'), (1978, 1979, 'af-1978'), (1980, 1991, 'af-1980'),
                    (1992, 1996, 'af-1992'), (1997, 2001, 'af-taliban'), (2002, 2020, 'iso:af'), (2021, N, 'af-taliban')],
    'Saudi Arabia': [(1932, N, 'iso:sa')],
    'Nejd': [(1744, 1818, 'nejd'), (1824, 1891, 'nejd'), (1902, 1931, 'nejd')], 'Arabia (Nejd)': '=Nejd',
    'Hejaz': [(1916, 1925, 'hejaz')],
    'Iraq': [(1921, 1958, 'iq-1921'), (1959, 1962, 'iq-1959'), (1963, 1990, 'three-stars'), (1991, 2007, 'iq-1991'), (2008, N, 'iso:iq')],
    'Syria': [(1932, 1957, 'sy-1932'), (1958, 1960, 'uar'), (1961, 1962, 'sy-1932'), (1963, 1971, 'three-stars'), (1972, 1979, 'arab-fed'),
              (1980, 2024, 'uar'), (2025, N, 'sy-1932')],
    'Lebanon': [(1943, N, 'iso:lb')], 'Jordan': [(1921, 1927, 'hejaz'), (1928, N, 'iso:jo')], 'Israel': [(1948, N, 'iso:il')],
    'Kuwait': [(1961, N, 'iso:kw')], 'Qatar': [(1868, N, 'iso:qa')], 'United Arab Emirates': [(1971, N, 'iso:ae')],
    'Trucial Oman': [(1820, 1971, 'trucial')],
    'Oman': [(1650, 1969, 'oman-red'), (1970, N, 'iso:om')], 'Muscat': [(1650, N, 'oman-red')], 'Mascat': '=Muscat', 'Maskat': '=Muscat',
    'Yemen': [(1918, 1961, 'ye-mutawakkil'), (1962, 1989, 'ye-yar'), (1990, N, 'iso:ye')],
    'Sultanate of Zanzibar': [(1856, 1963, 'zanzibar')], 'Sultinate of Zanzibar': '=Sultanate of Zanzibar', 'Zanzibar': [(1856, 1963, 'zanzibar')],
    'Morocco': [(1666, 1914, 'ma-red'), (1915, N, 'iso:ma')],
    'Tunisia': [(1831, N, 'iso:tn')], 'Tunis': [(1831, N, 'iso:tn')],
    'Libya': [(1951, 1968, 'ly-1951'), (1969, 1971, 'ly-1969'), (1972, 1976, 'arab-fed'), (1977, 2010, 'ly-1977'), (2011, N, 'ly-1951')],
    'Algeria': [(1830, 1961, '=France'), (1962, N, 'iso:dz')],
    # South and South-East Asia
    'Maratha': [(N, N, 'maratha')], 'Maratha Confederacy': [(N, N, 'maratha')],
    'British East India Company': [(N, 1800, 'eic-1707'), (1801, 1874, 'eic-1801')],
    'India': [(1707, 1800, 'eic-1707'), (1801, 1857, 'eic-1801'), (1858, 1946, 'in-raj'), (1947, N, 'iso:in')],
    'Kandy': [(1469, 1815, 'kandy')],
    'Ceylon': [(1815, 1947, '=United Kingdom'), (1948, N, 'iso:lk')], 'Sri Lanka': [(1948, N, 'iso:lk')],
    'Burma': [(1886, 1947, '=United Kingdom'), (1948, 1973, 'mm-1948'), (1974, 2009, 'mm-1974'), (2010, N, 'iso:mm')],
    'Ayutthaya': [(1680, 1767, 'siam-red')],
    'Rattanakosin Kingdom': [(1782, 1816, 'siam-red'), (1817, 1854, 'siam-chakra'), (1855, 1916, 'siam-elephant'), (1917, N, 'iso:th')],
    'Siam': '=Rattanakosin Kingdom', 'Thailand': '=Rattanakosin Kingdom',
    'Laos': [(1893, 1951, '=France'), (1952, 1974, 'la-1952'), (1975, N, 'iso:la')],
    'Cambodia': [(1948, 1969, 'iso:kh'), (1970, 1974, 'kh-1970'), (1975, 1988, 'kh-1976'), (1989, 1992, 'kh-1976'), (1993, N, 'iso:kh')],
    'Annam': [(1883, 1944, '=France')], 'Cochin China': [(1862, 1948, '=France')], 'Tonkin': [(1883, 1945, '=France')],
    'French Indo-China': '=France',
    'Vietnam': [(1945, N, 'iso:vn')], 'South Vietnam': [(1949, 1975, 'vn-south')], 'North Vietnam': [(1945, N, 'iso:vn')],
    'Malaysia': [(1957, 1962, 'my-1950'), (1963, N, 'iso:my')], 'Malaya': [(1950, 1962, 'my-1950')],
    'Indonesia': [(1945, N, 'iso:id')], 'Philippines': [(1898, 1945, '=United States'), (1946, N, 'iso:ph')],
    'Nepal': [(1768, N, 'iso:np')], 'Bhutan': [(1907, N, 'iso:bt')],
    'Pakistan': [(1947, N, 'iso:pk')], 'Bangladesh': [(1971, N, 'iso:bd')],
    # Europe
    'Holy Roman Empire': [(962, 1432, 'hre-1'), (1433, 1806, 'hre-2')],
    'Kingdom of France': '=France',
    'England': [(1198, 1276, 'en-royal'), (1277, N, 'iso:gb-eng')], 'English territory': '=England', 'England and Ireland': '=England',
    'Angevin Empire': [(1154, 1214, 'en-royal')],
    'Scotland': [(832, N, 'iso:gb-sct')], 'Scottland': '=Scotland',
    'United Kingdom of Great Britain and Ireland': '=United Kingdom',
    'Kingdom of Ireland': [(1542, 1800, 'ie-harp')], 'Ireland': [(1922, N, 'iso:ie')],
    'Britany': [(1316, 1532, 'brittany')],
    'Castile': [(1065, 1229, 'castile'), (1230, 1715, 'castile-leon')], 'Castilla': '=Castile', 'Castille': '=Castile',
    'León': [(1126, 1229, 'leon'), (1230, N, 'castile-leon')],
    'Aragón': [(1150, N, 'aragon')], 'Navarre': [(1234, 1841, 'navarre')], 'Asturias': [(908, 924, 'asturias')],
    'Spanish Habsburg': '=Spain', 'Habsburg Netherlands': [(1506, 1713, 'burgundy-cross')],
    'Viceroyalty of New Spain': '=Spain', 'Viceroyalty of Peru': '=Spain', 'Viceroyalty of the Río de la Plata': '=Spain',
    'Viceroyalty of Brazil': '=Portugal',
    'Granada': [(N, N, None)],
    'Dutch Republic': '=Netherlands', 'Batavian Republic': '=Netherlands',
    'Luxembourg': [(1845, 1939, 'iso:lu'), (1940, 1944, '=Germany'), (1945, N, 'iso:lu')],
    'Swiss Confederation': [(1291, 1797, 'iso:ch'), (1798, 1802, 'helvetic'), (1803, N, 'iso:ch')], 'Switzerland': '=Swiss Confederation',
    'Helvetic Republic': [(N, N, 'helvetic')], 'Geneva': [(1500, 1798, 'geneva'), (1814, N, 'geneva')], 'Hamburg': [(1300, N, 'hamburg')],
    'Prussia': [(1230, 1524, 'teutonic'), (1525, 1918, 'prussia')], 'Brandenburg': [(1157, 1700, 'brandenburg'), (1701, 1918, 'prussia')],
    'East Prussia': '=Germany',
    'Bavaria': [(1180, 1918, 'bavaria')], 'Saxony': [(1806, 1918, 'saxony')], 'Hanover': [(1814, 1866, 'hanover')],
    'German Empire': '=Germany', 'East Germany': [(1949, 1958, 'iso:de'), (1959, 1990, 'ddr')], 'West Germany': [(1949, N, 'iso:de')],
    'Austria': [(1918, 1937, 'iso:at'), (1938, 1945, 'de-nazi'), (1946, N, 'iso:at')],
    'Austria Hungary': [(1867, 1918, 'austria-hungary')], 'Austro-Hungarian Empire': '=Austria Hungary',
    'Hungary': [(1000, 1300, 'hu-arpad'), (1301, 1847, 'hu-arms'), (1848, N, 'iso:hu')], 'Imperial Hungary': [(N, N, 'hu-arms')],
    'Bohemia': [(1198, 1918, 'bohemia')],
    'Czechoslovakia': [(1920, 1992, 'iso:cz')], 'Czech Republic': [(1993, N, 'iso:cz')], 'Slovakia': [(1993, N, 'iso:sk')],
    'Poland': [(1295, 1795, 'pl-eagle'), (1807, 1830, 'pl-eagle'), (1919, N, 'iso:pl')],
    'Poland-Lithuania': [(1386, 1568, 'pl-lt')], 'Polish–Lithuanian Commonwealth': [(1569, 1795, 'plc')],
    'Lithuania': [(1253, 1795, 'lt-vytis'), (1918, 1940, 'iso:lt'), (1941, 1989, 'lt-ssr'), (1990, N, 'iso:lt')],
    'Latvia': [(1918, 1940, 'iso:lv'), (1941, 1989, 'lv-ssr'), (1990, N, 'iso:lv')],
    'Estonia': [(1918, 1940, 'iso:ee'), (1941, 1989, 'ee-ssr'), (1990, N, 'iso:ee')],
    'Teutonic Knights': [(N, N, 'teutonic')],
    'Kalmar Union': [(1397, 1523, 'kalmar')],
    'Denmark-Norway': [(1219, N, 'iso:dk')],
    'Sweden–Norway': [(1814, 1843, 'se-1818'), (1844, 1905, 'se-1844')],
    'Iceland': [(1918, N, 'iso:is')], 'Finland': [(1918, N, 'iso:fi')], 'Greenland': [(1721, 1984, '=Denmark'), (1985, N, 'iso:gl')],
    'Kievan Rus': [(980, 1240, 'rus-trident')], 'Kyivan Rus': '=Kievan Rus', 'Rus': '=Kievan Rus',
    'Grand Duchy of Moscow': '=Russian Empire', 'Tsardom of Muscovy': '=Russian Empire',
    'Russia': [(1693, 1917, 'iso:ru'), (1918, 1991, '=USSR'), (1992, N, 'iso:ru')], 'South Russia': [(N, N, 'iso:ru')],
    'Ukraine': [(1917, 1920, 'iso:ua'), (1949, 1990, 'ua-ssr'), (1991, N, 'iso:ua')],
    'Byelarus': [(1991, 1994, 'by-1991'), (1995, N, 'iso:by')], 'Belarus': '=Byelarus',
    'Moldova': [(1990, N, 'iso:md')],
    'Georgia': [(1008, 1800, 'iso:ge'), (1918, 1921, 'ge-1918'), (1990, 2003, 'ge-1918'), (2004, N, 'iso:ge')],
    'Kingdom of Georgia': [(1008, N, 'iso:ge')],
    'Armenia': [(1918, 1920, 'iso:am'), (1990, N, 'iso:am')], 'Azerbaijan': [(1918, 1920, 'iso:az'), (1991, N, 'iso:az')],
    'Venice': [(697, 1797, 'venice')], 'Genoa': [(1096, 1797, 'genoa')],
    'Papal States': [(756, 1802, 'papal-old'), (1803, 1870, 'papal')], 'Vatican City': [(1929, N, 'iso:va')],
    'Savoy': [(1263, N, 'savoy')], 'Sardinia-Piedmont': [(1416, N, 'savoy')], 'Kingdom of Sardinia': [(1720, 1847, 'savoy'), (1848, 1861, 'it-savoy')],
    'Kingdom of the Two Sicilies': [(1734, 1861, 'two-sicilies')], 'Sicily': [(1282, 1409, 'sicily-arag'), (1734, 1861, 'two-sicilies')],
    'Kingdom of Italy': [(1861, 1946, 'it-savoy')],
    'Cyprus': [(1192, 1488, 'cy-lusignan'), (1489, 1570, 'venice'), (1571, 1877, '=Ottoman Empire'), (1878, 1959, '=United Kingdom'), (1960, N, 'iso:cy')],
    'Malta': [(1530, 1798, 'st-john'), (1800, 1963, '=United Kingdom'), (1964, N, 'iso:mt')],
    'Greece': [(1822, 1969, 'gr-cross'), (1970, N, 'iso:gr')],
    'Montenegro': [(1696, 1851, 'me-krstas'), (1852, 1918, 'me-1880'), (1919, 2005, None), (2006, N, 'iso:me')],
    'Serbia': [(1217, 1459, 'rs-nemanjic'), (1835, 1881, 'rs-1835'), (1882, 1918, 'iso:rs'), (1992, 2003, 'yu-kingdom'), (2004, N, 'iso:rs')],
    'Raška': [(1217, N, 'rs-nemanjic')],
    'Bosnia': [(1377, 1463, 'ba-kotromanic')], 'Bosnia-Herzegovina': '=Austria Hungary',
    'Bosnia and Herzegovina': [(1992, 1997, 'ba-1992'), (1998, N, 'iso:ba')],
    'Macedonia': [(1992, 1995, 'mk-1992'), (1996, N, 'iso:mk')],
    'Albania': [(1912, 1945, 'iso:al'), (1946, 1991, 'al-1946'), (1992, N, 'iso:al')],
    'Romania': [(1866, 1947, 'iso:ro'), (1948, 1989, 'ro-1965'), (1990, N, 'iso:ro')],
    'Bulgaria': [(1878, 1945, 'iso:bg'), (1946, 1990, 'bg-1971'), (1991, N, 'iso:bg')],
    'Croatia': [(1495, 1917, 'hr-checky'), (1947, 1990, 'hr-ssr'), (1991, N, 'iso:hr')],
    'Slovenia': [(1991, N, 'iso:si')],
    'Yugoslavia': [(1918, 1940, 'yu-kingdom'), (1945, 1991, 'yu-sfr'), (1992, 2006, 'yu-kingdom')],
    # the Americas
    'United States of America': '=United States',
    'British American colonies': '=United Kingdom',
    'Canada': [(N, 1867, '=United Kingdom'), (1868, 1964, 'ca-red'), (1965, N, 'iso:ca')],
    "Rupert's Land": [(1670, 1869, 'hbc')],
    'Dominion of Newfoundland': '=United Kingdom',
    'Kingdom of Hawaii': [(1845, 1898, 'hawaii'), (1899, N, '=United States')],
    'Mexico': [(N, 1820, '=Spain'), (1821, 1823, 'mx-1821'), (1824, N, 'iso:mx')],
    'Brazil': [(N, 1821, '=Portugal'), (1822, 1889, 'br-empire'), (1890, N, 'iso:br')], 'Kingdom of Brazil': '=Brazil',
    'United Provinces of the Río de la Plata': [(1816, N, 'iso:ar')], 'Argentina': [(1816, N, 'iso:ar')],
    'Chile': [(1817, N, 'iso:cl')], 'Peru': [(1825, N, 'iso:pe')], 'Bolivia': [(1851, N, 'iso:bo')], 'Paraguay': [(1842, N, 'iso:py')],
    'Uruguay': [(1830, N, 'iso:uy')], 'Colombia': [(1861, N, 'iso:co')], 'Venezuela': [(1811, N, 'iso:ve')], 'Ecuador': [(1860, N, 'iso:ec')],
    'Guatemala': [(1871, N, 'iso:gt')], 'Honduras': [(1866, N, 'iso:hn')], 'El Salvador': [(1865, 1911, 'sv-1865'), (1912, N, 'iso:sv')],
    'Nicaragua': [(1908, N, 'iso:ni')], 'Costa Rica': [(1848, N, 'iso:cr')], 'Panama': [(1903, N, 'iso:pa')],
    'Belize': [(1862, 1980, '=United Kingdom'), (1981, N, 'iso:bz')],
    'Haiti': [(1804, 1963, 'ht-1806'), (1964, 1985, 'ht-1964'), (1986, N, 'iso:ht')],
    'Dominican Republic': [(1844, N, 'iso:do')], 'Cuba': [(1902, N, 'iso:cu')], 'Puerto Rico': [(1898, N, '=United States')],
    'Jamaica': [(1655, 1961, '=United Kingdom'), (1962, N, 'iso:jm')],
    'Bahamas': [(1718, 1972, '=United Kingdom'), (1973, N, 'iso:bs')],
    'Guyana': [(1831, 1965, '=United Kingdom'), (1966, N, 'iso:gy')], 'British Guiana': '=United Kingdom',
    'Suriname': [(1667, 1974, '=Netherlands'), (1975, N, 'iso:sr')], 'Dutch Guiana': '=Netherlands', 'Surinam': '=Netherlands',
    'French Guiana': '=France', 'Guadeloupe': '=France', 'Cayenne': '=France', 'Louisiana': '=France', 'New France': '=France',
    'Quebec': '=United Kingdom', 'Florida': '=Spain', 'Essequibo': '=Netherlands', 'Netherlands Antilles': '=Netherlands',
    'Trinidad': [(N, 1796, '=Spain'), (1797, N, '=United Kingdom')], 'Dominica': '=United Kingdom',
    # Africa
    'Ethiopia': [(1889, 1935, 'et-1897'), (1936, 1940, '=Italy'), (1941, 1974, 'et-1897'), (1975, 1986, 'et-plain'), (1987, 1990, 'et-1987'),
                 (1991, 1995, 'et-plain'), (1996, N, 'iso:et')], 'Abyssinia': '=Ethiopia',
    'Sudan': [(1956, 1969, 'sd-1956'), (1970, N, 'iso:sd')],
    'Congo': [(1885, 1919, 'cd-1877'), (1960, 1969, 'iso:cg'), (1970, 1990, 'cg-1970'), (1991, N, 'iso:cg')],
    'Zaire': [(1885, 1959, 'cd-1877'), (1960, 1962, 'cd-1960'), (1963, 1970, 'cd-1963'), (1971, 1996, 'zaire'), (1997, 2005, 'cd-1960'), (2006, N, 'iso:cd')],
    'Zaire (Belgium)': [(N, N, 'cd-1877')],
    'Transvaal': [(1858, 1902, 'transvaal')], 'Orange Free State': [(1857, 1902, 'ofs')],
    'Union of South Africa': [(1910, 1927, 'za-1910'), (1928, 1993, 'za-1928')],
    'South Africa': [(1910, 1927, 'za-1910'), (1928, 1993, 'za-1928'), (1994, N, 'iso:za')],
    'Cape Colony': [(1806, N, '=United Kingdom')], 'Natal': '=United Kingdom', 'Basutoland': '=United Kingdom',
    'Rhodesia': [(1890, 1964, '=United Kingdom'), (1968, 1979, 'rhodesia')],
    'Zimbabwe': [(1968, 1979, 'rhodesia'), (1980, N, 'iso:zw')],
    'Liberia': [(1847, N, 'iso:lr')],
    'Mauritania': [(1959, 2016, 'mr-1959'), (2017, N, 'iso:mr')],
    'Burkina Faso': [(1959, 1983, 'bf-volta'), (1984, N, 'iso:bf')], 'Upper Volta': [(1959, 1983, 'bf-volta')],
    'Benin': [(1959, 1974, 'iso:bj'), (1975, 1989, 'bj-1975'), (1990, N, 'iso:bj')],
    'Rwanda': [(1962, 2000, 'rw-1962'), (2001, N, 'iso:rw')],
    'Tanzania, United Republic of': [(1961, 1963, 'tanganyika'), (1964, N, 'iso:tz')],
    'Angola': [(1575, 1974, '=Portugal'), (1975, N, 'iso:ao')], 'Mozambique': [(1752, 1974, '=Portugal'), (1975, N, 'iso:mz')],
    'Portuguese East Africa': '=Portugal', 'Portuguese Guinea': '=Portugal',
    'Spanish Guinea': '=Spain', 'Spanish Morocco': '=Spain', 'Spanish Sahara': '=Spain', 'Rio De Oro': '=Spain',
    'Western Sahara': [(1884, 1975, '=Spain')],
    'French West Africa': '=France', 'French Somaliland': '=France',
    'German South-West Africa': '=Germany', 'Kamerun': '=Germany', 'Togoland': '=Germany',
    'Madagascar': [(1896, 1957, '=France'), (1958, N, 'iso:mg')],
    'Gold Coast': '=United Kingdom', 'Nyasaland': '=United Kingdom', 'Tripolitana (UK Lybia)': '=United Kingdom',
    # Oceania
    'Australia': [(1788, 1900, '=United Kingdom'), (1901, N, 'iso:au')],
    'New Zealand': [(1840, 1868, '=United Kingdom'), (1869, N, 'iso:nz')],
    'Maori': [(1834, 1900, 'united-tribes')], 'Maoris': '=Maori', 'Māori': '=Maori',
    'Papua New Guinea': [(1975, N, 'iso:pg')], 'Fiji': [(1874, 1969, '=United Kingdom'), (1970, N, 'iso:fj')],
}

# a power in brackets after a name: "Jamaica (UK)", "Cuba (Spain)", "Germany (Soviet)"
SUFFIX = {'UK': 'United Kingdom', 'GB': 'United Kingdom', 'Britain': 'United Kingdom', 'British': 'United Kingdom', 'England': 'England',
          'France': 'France', 'FR': 'France', 'French': 'France', 'Spain': 'Spain', 'Spanish': 'Spain', 'Portugal': 'Portugal',
          'Netherlands': 'Netherlands', 'Dutch': 'Netherlands', 'Holland': 'Netherlands', 'Denmark': 'Denmark', 'Danemark': 'Denmark',
          'Belgium': 'Belgium', 'Italy': 'Italy', 'IT': 'Italy', 'Germany': 'Germany', 'German': 'Germany', 'USA': 'United States',
          'US': 'United States', 'USSR': 'USSR', 'Soviet': 'USSR', 'Russia': 'Russian Empire', 'Japan': 'Japan', 'Egypt': 'Egypt',
          'Ottoman': 'Ottoman Empire', 'Turkey': 'Ottoman Empire', 'Sweden': 'Sweden', 'Norway': 'Norway', 'China': 'China',
          'Austria': 'Austrian Empire', 'Venice': 'Venice', 'Genoa': 'Genoa', 'Portuguese': 'Portugal', 'Australia': 'Australia',
          'New Zealand': 'New Zealand', 'South Africa': 'South Africa'}

# modern states whose name on the map differs from the ISO name, with the year their flag dates from
ISO = {
    'Ivory Coast': ('ci', 1959), 'Byelarus': None, 'Swaziland': ('sz', 1968), 'Burma': None, 'Macedonia': None, 'Czech Republic': None,
    'Gambia, The': ('gm', 1965), 'Gambia': ('gm', 1965), 'Cape Verde': ('cv', 1975), 'East Timor': ('tl', 2002), 'Brunei': ('bn', 1959),
    'Laos': None, 'Syria': None, 'Iran': None, 'Russia': None, 'Vietnam': None, 'Bolivia': None, 'Venezuela': None, 'Moldova': None,
    'Taiwan': None, 'Tanzania, United Republic of': None, 'Turkey': None, 'Korea, Republic of': None,
    "Korea, Democratic People's Republic of": None, 'Congo': None, 'Zaire': None,
}
# the year each modern state's current flag (or its nearly identical forerunner) was first flown, for states not in TL
SINCE = {
    'al': 1912, 'dz': 1962, 'ad': 1866, 'ao': 1975, 'ag': 1967, 'ar': 1816, 'am': 1990, 'au': 1901, 'at': 1918, 'az': 1991, 'bs': 1973,
    'bh': 1972, 'bd': 1971, 'bb': 1966, 'by': 1995, 'be': 1831, 'bz': 1981, 'bj': 1990, 'bt': 1969, 'bo': 1851, 'ba': 1998, 'bw': 1966,
    'br': 1889, 'bn': 1959, 'bg': 1991, 'bf': 1984, 'bi': 1962, 'kh': 1993, 'cm': 1975, 'ca': 1965, 'cv': 1992, 'cf': 1958, 'td': 1959,
    'cl': 1817, 'cn': 1949, 'co': 1861, 'km': 2001, 'cg': 1991, 'cd': 2006, 'cr': 1848, 'ci': 1959, 'hr': 1990, 'cu': 1902, 'cy': 1960,
    'cz': 1920, 'dk': 1219, 'dj': 1977, 'dm': 1978, 'do': 1844, 'ec': 1860, 'eg': 1984, 'sv': 1912, 'gq': 1968, 'er': 1995, 'ee': 1990,
    'et': 1996, 'fj': 1970, 'fi': 1918, 'fr': 1830, 'ga': 1960, 'gm': 1965, 'ge': 2004, 'de': 1949, 'gh': 1966, 'gr': 1978, 'gd': 1974,
    'gt': 1871, 'gn': 1958, 'gw': 1973, 'gy': 1966, 'ht': 1986, 'hn': 1866, 'hu': 1957, 'is': 1918, 'in': 1947, 'id': 1945, 'ir': 1980,
    'iq': 2008, 'ie': 1922, 'il': 1948, 'it': 1946, 'jm': 1962, 'jp': 1870, 'jo': 1928, 'kz': 1992, 'ke': 1963, 'ki': 1979, 'kp': 1948,
    'kr': 1949, 'kw': 1961, 'kg': 1992, 'la': 1975, 'lv': 1990, 'lb': 1943, 'ls': 2006, 'lr': 1847, 'ly': 2011, 'li': 1937, 'lt': 1990,
    'lu': 1845, 'mg': 1958, 'mw': 1964, 'my': 1963, 'mv': 1965, 'ml': 1961, 'mt': 1964, 'mh': 1979, 'mr': 2017, 'mu': 1968, 'mx': 1968,
    'fm': 1979, 'md': 1990, 'mc': 1881, 'mn': 1992, 'me': 2004, 'ma': 1915, 'mz': 1983, 'mm': 2010, 'na': 1990, 'nr': 1968, 'np': 1962,
    'nl': 1651, 'nz': 1902, 'ni': 1908, 'ne': 1959, 'ng': 1960, 'mk': 1995, 'no': 1821, 'om': 1970, 'pk': 1947, 'pw': 1981, 'pa': 1903,
    'pg': 1971, 'py': 1842, 'pe': 1825, 'ph': 1946, 'pl': 1919, 'pt': 1911, 'qa': 1971, 'ro': 1989, 'ru': 1991, 'rw': 2001, 'kn': 1983,
    'lc': 1979, 'vc': 1985, 'ws': 1949, 'sm': 1797, 'st': 1975, 'sa': 1973, 'sn': 1960, 'rs': 2004, 'sc': 1996, 'sl': 1961, 'sg': 1959,
    'sk': 1993, 'si': 1991, 'sb': 1977, 'so': 1954, 'za': 1994, 'ss': 2011, 'es': 1981, 'lk': 1972, 'sd': 1970, 'sr': 1975, 'sz': 1968,
    'se': 1906, 'ch': 1889, 'sy': 1980, 'tw': 1928, 'tj': 1992, 'tz': 1964, 'th': 1917, 'tl': 2002, 'tg': 1960, 'to': 1875, 'tt': 1962,
    'tn': 1831, 'tr': 1936, 'tm': 1992, 'tv': 1995, 'ug': 1962, 'ua': 1991, 'ae': 1971, 'gb': 1801, 'us': 1960, 'uy': 1830, 'uz': 1991,
    'vu': 1980, 'va': 1929, 've': 2006, 'vn': 1955, 'ye': 1990, 'zm': 1964, 'zw': 1980, 'xk': 2008, 'ps': 1964, 'eh': 1976, 'gl': 1985,
}

# preferred map tint (hue in degrees) for states whose colour readers know them by, when the flag alone would not say it
TINT = {'Byzantine Empire': 290, 'Eastern Roman Empire': 290, 'Holy Roman Empire': 46}

# names and stories for modern flags that the map also shows in earlier centuries
ISO_TITLES = {
    'gb-eng': ("Saint George's Cross", "The red cross of Saint George, England's flag from the late 1200s."),
    'gb-sct': ('Saltire of Saint Andrew', 'By legend a white saltire appeared in the sky before a Scottish victory in 832.'),
    'gb': ('Union Flag', 'The crosses of England, Scotland and Ireland together, since 1801.'),
    'dk': ('Dannebrog', 'By legend it fell from the sky during a Danish battle in Estonia in 1219: the oldest national flag still in use.'),
    'jp': ('Hinomaru', 'The red sun. Emperor Monmu raised a sun banner at court in 701; Japan\'s national flag from 1870.'),
    'ru': ('Russian tricolour', "White, blue and red, first flown on Peter the Great's ships in the 1690s."),
    'ch': ('Swiss cross', 'The white cross of Schwyz, carried by the Swiss confederates since the 1300s.'),
    'ge': ('Five-cross flag', 'The red crosses on white of medieval Georgia, made the national flag again in 2004.'),
    'tr': ('Crescent and star', 'The Ottoman flag from 1844, and Turkey\'s since.'),
    'tw': ('Blue Sky, White Sun, Red Earth', 'The flag of the Republic of China from 1928; on Taiwan since 1949.'),
    'kr': ('Taegukgi', "Korea's flag from 1883; South Korea's since 1948."),
    'us': ('Stars and Stripes', 'Fifty stars since 1960.'),
    'fr': ('Tricolour', 'Blue, white and red, the colours of the Revolution, the national flag from 1794.'),
    'nl': ('Flag of the Netherlands', 'Red, white and blue, which replaced the orange of the Prince\'s Flag in the 1600s.'),
    'se': ('Flag of Sweden', 'The gold cross on blue, flown since the 1500s.'),
    'it': ('Il Tricolore', 'Green, white and red, first raised in 1797; without the royal arms since 1946.'),
    'de': ('Black, red and gold', 'The colours of the 1848 revolution: the Weimar Republic from 1919, West Germany from 1949, all Germany since 1990.'),
    'at': ('Flag of Austria', 'Red, white and red, by legend the bloodied tunic of Duke Leopold V at Acre in 1191.'),
    'hu': ('Flag of Hungary', 'Red, white and green, first raised in the revolution of 1848.'),
    'pl': ('Flag of Poland', 'White over red, the colours of the white eagle on red.'),
    'cn': ('Five-star Red Flag', "The People's Republic of China, since 1949."),
    'in': ('Tiranga', 'Saffron, white and green with the Ashoka wheel, since 1947.'),
    'mx': ('Flag of Mexico', 'The eagle on a cactus, from the founding legend of Tenochtitlan.'),
    'ar': ('Flag of Argentina', 'Sky blue and white with the Sun of May, from 1812.'),
    'np': ('Flag of Nepal', 'Two stacked pennants, the only national flag that is not a rectangle.'),
    'lk': ('Lion Flag', 'The lion of the old Sinhalese kings, with stripes added for Sri Lanka\'s minorities.'),
    'th': ('Trairanga', 'Red, white and blue, which replaced the white elephant in 1917.'),
    'ma': ('Flag of Morocco', 'The old red flag with the green star of Solomon added in 1915.'),
    'tn': ('Flag of Tunisia', 'Red with a crescent and star, from 1831.'),
    'om': ('Flag of Oman', 'The old red flag with white and green added in 1970.'),
    'ir': ('Flag of Iran', 'Green, white and red with the emblem of the Islamic Republic, since 1980.'),
    'iq': ('Flag of Iraq', 'Red, white and black with "God is great", since 2008.'),
    'eg': ('Flag of Egypt', 'Red, white and black with the Eagle of Saladin, since 1984.'),
    'sy': ('Flag of Syria', 'The flag of the United Arab Republic, Syria\'s again from 1980 to 2024.'),
}

# colonial rule and later corrections, checked against where each name sits on the map in each border file
TL.update({
    'Mongol Empire': [(1206, 1635, 'mongol')],
    'Manchu Empire': [(1636, 1911, 'qing'), (1912, N, '=China')],
    'Manchuria': [(1912, 1931, 'roc-5'), (1932, 1945, 'manchukuo'), (1946, N, '=China')],
    'Ottoman Sultanate': [(N, N, 'iso:tr')],
    'Poland-Lithuania': [(1386, 1568, 'pl-lt'), (1569, 1795, 'plc')],
    'Finland': [(1809, 1917, '=Russian Empire'), (1918, N, 'iso:fi')],
    'Ukraine': [(1917, 1920, 'iso:ua'), (1921, 1948, '=USSR'), (1949, 1990, 'ua-ssr'), (1991, N, 'iso:ua')],
    'Egypt': [(1517, 1866, '=Ottoman Empire')] + TL['Egypt'],
    'Hejaz': [(1517, 1915, '=Ottoman Empire'), (1916, 1925, 'hejaz'), (1926, 1931, 'nejd'), (1932, N, 'iso:sa')],
    'Libya': [(1912, 1942, '=Italy'), (1943, 1950, '=United Kingdom')] + TL['Libya'],
    'Sudan': [(1899, 1955, '=United Kingdom')] + TL['Sudan'],
    'Dutch East Indies': '=Netherlands', 'Netherlands Indies': '=Netherlands',
    'Malaya': [(1826, 1949, '=United Kingdom'), (1950, 1962, 'my-1950')],
    'Malaysia': [(1826, 1956, '=United Kingdom'), (1957, 1962, 'my-1950'), (1963, N, 'iso:my')],
    'Congo': [(1940, 1959, '=France'), (1960, 1969, 'iso:cg'), (1970, 1990, 'cg-1970'), (1991, N, 'iso:cg')],
    'Benin': [(1897, 1913, '=United Kingdom'), (1940, 1958, '=France'), (1959, 1974, 'iso:bj'), (1975, 1989, 'bj-1975'), (1990, N, 'iso:bj')],
    'Senegal': [(1850, 1959, '=France'), (1960, N, 'iso:sn')],
    'Gabon': [(1885, 1959, '=France'), (1960, N, 'iso:ga')],
    'Ghana': [(1874, 1956, '=United Kingdom'), (1957, N, 'iso:gh')],
    'Nigeria': [(1900, 1959, '=United Kingdom'), (1960, N, 'iso:ng')],
    'Kenya': [(1895, 1962, '=United Kingdom'), (1963, N, 'iso:ke')],
    'Uganda': [(1894, 1961, '=United Kingdom'), (1962, N, 'iso:ug')],
    'Zambia': [(1911, 1963, '=United Kingdom'), (1964, N, 'iso:zm')],
    'Botswana': [(1885, 1965, '=United Kingdom'), (1966, N, 'iso:bw')],
    'Zimbabwe': [(1890, 1964, '=United Kingdom'), (1968, 1979, 'rhodesia'), (1980, N, 'iso:zw')],
    'Tanzania, United Republic of': [(1919, 1960, '=United Kingdom'), (1961, 1963, 'tanganyika'), (1964, N, 'iso:tz')],
    'Namibia': [(1884, 1914, '=Germany'), (1915, 1989, '=South Africa'), (1990, N, 'iso:na')],
    'Cameroon': [(1916, 1959, '=France'), (1960, N, 'iso:cm')],
    'Central African Republic': [(1903, 1957, '=France'), (1958, N, 'iso:cf')],
    'Burkina Faso': [(1919, 1958, '=France'), (1959, 1983, 'bf-volta'), (1984, N, 'iso:bf')],
    'Rwanda': [(1897, 1915, '=Germany'), (1916, 1961, '=Belgium'), (1962, 2000, 'rw-1962'), (2001, N, 'iso:rw')],
    'Burundi': [(1897, 1915, '=Germany'), (1916, 1961, '=Belgium'), (1962, N, 'iso:bi')],
    'Transvaal': [(1858, 1902, 'transvaal'), (1903, 1909, '=United Kingdom'), (1910, N, '=South Africa')],
    'Orange Free State': [(1857, 1902, 'ofs'), (1903, 1909, '=United Kingdom'), (1910, N, '=South Africa')],
})

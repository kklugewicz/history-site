"""A small vocabulary for drawing flags as SVG, on a 60 x 45 field (4:3, the shape every flag on the map is shown in).

Each helper returns SVG markup; flag() wraps the parts in an <svg>. Emblems (eagles, lions, lilies, keys...) are drawn in
a 100 x 100 box and placed with emblem(name, colour, x, y, size)."""
import math

W, H = 60, 45


def f(v): return ('%.2f' % v).rstrip('0').rstrip('.')


def rect(c, x=0, y=0, w=W, h=H, extra=''):
    return '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"%s/>' % (f(x), f(y), f(w), f(h), c, extra)


def hs(*cs):
    """equal horizontal stripes, top to bottom"""
    n = len(cs); return ''.join(rect(c, 0, H * i / n, W, H / n + .05) for i, c in enumerate(cs))


def vs(*cs):
    """equal vertical stripes, hoist to fly"""
    n = len(cs); return ''.join(rect(c, W * i / n, 0, W / n + .05, H) for i, c in enumerate(cs))


def hw(*pairs):
    """horizontal stripes with weights: (colour, weight), ..."""
    tot = sum(w for _, w in pairs); y = 0; out = ''
    for c, w in pairs:
        h = H * w / tot; out += rect(c, 0, y, W, h + .05); y += h
    return out


def cross(c, w=9, x=W / 2, y=H / 2):
    return rect(c, x - w / 2, 0, w, H) + rect(c, 0, y - w / 2, W, w)


def nordic(c, w=7, x=21):
    return cross(c, w, x, H / 2)


def saltire(c, w=7):
    return ('<line x1="0" y1="0" x2="%s" y2="%s" stroke="%s" stroke-width="%s"/>' % (f(W), f(H), c, f(w)) +
            '<line x1="%s" y1="0" x2="0" y2="%s" stroke="%s" stroke-width="%s"/>' % (f(W), f(H), c, f(w)))


def disc(c, cx=W / 2, cy=H / 2, r=12):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (f(cx), f(cy), f(r), c)


def ring(c, cx, cy, r, w):
    return '<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (f(cx), f(cy), f(r), c, f(w))


def star_d(cx=W / 2, cy=H / 2, r=8, n=5, rot=-90, inner=.382):
    """path data for an n-pointed star"""
    pts = []
    for i in range(2 * n):
        a = math.radians(rot + i * 180 / n); rr = r if i % 2 == 0 else r * inner
        pts.append('%s %s' % (f(cx + rr * math.cos(a)), f(cy + rr * math.sin(a))))
    return 'M%sZ' % 'L'.join(pts)


def star(c, cx=W / 2, cy=H / 2, r=8, n=5, rot=-90, inner=.382):
    return '<path d="%s" fill="%s"/>' % (star_d(cx, cy, r, n, rot, inner), c)


def star_outline(c, cx, cy, r, w=.7):
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (star_d(cx, cy, r), c, f(w))


def crescent(c, cx=W / 2, cy=H / 2, r=9, d=.32, r2=.82, rot=0):
    """a crescent opening towards rot degrees (0 = towards the fly): outer circle r, inner circle r*r2 shifted by r*d"""
    R1, R2, D = r, r * r2, r * d
    x = (D * D + R1 * R1 - R2 * R2) / (2 * D); y = math.sqrt(max(R1 * R1 - x * x, 0))
    a = math.radians(rot)
    rotp = lambda px, py: (cx + px * math.cos(a) - py * math.sin(a), cy + px * math.sin(a) + py * math.cos(a))
    A = rotp(x, -y); B = rotp(x, y)
    return '<path d="M%s %sA%s %s 0 1 0 %s %sA%s %s 0 1 1 %s %sZ" fill="%s"/>' % (
        f(A[0]), f(A[1]), f(R1), f(R1), f(B[0]), f(B[1]), f(R2), f(R2), f(A[0]), f(A[1]), c)


def text(t, c, x=W / 2, y=H / 2, size=12, font='DejaVu Serif', weight='bold', spacing=0, extra=''):
    return ('<text x="%s" y="%s" fill="%s" font-family="%s" font-weight="%s" font-size="%s" text-anchor="middle" '
            'dominant-baseline="central" letter-spacing="%s"%s>%s</text>') % (f(x), f(y), c, font, weight, f(size), f(spacing), extra, t)


def border(c, w=3):
    return '<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (
        f(w / 2), f(w / 2), f(W - w), f(H - w), c, f(w))


def canton(inner, w=W / 2, h=H / 2):
    return '<svg x="0" y="0" width="%s" height="%s" viewBox="0 0 %s %s" preserveAspectRatio="none">%s</svg>' % (f(w), f(h), W, H, inner)


def tri(c, depth=W / 2.6):
    """a triangle at the hoist"""
    return '<path d="M0 0L%s %sL0 %sZ" fill="%s"/>' % (f(depth), f(H / 2), f(H), c)


def poly(c, pts):
    return '<path d="M%sZ" fill="%s"/>' % ('L'.join('%s %s' % (f(x), f(y)) for x, y in pts), c)


def emblem(name, c, cx=W / 2, cy=H / 2, size=30, extra='', flip=False):
    """an emblem from EMBLEMS, drawn in colour c, centred at cx, cy, size units high"""
    s = size / 100
    tr = 'translate(%s %s) scale(%s%s %s) translate(-50 -50)' % (f(cx), f(cy), '-' if flip else '', f(s), f(s))
    e = EMBLEMS[name]
    if e.startswith('<'):  # a fragment: its strokes take the colour too (only where it sets a stroke-width)
        return '<g transform="%s" fill="%s" stroke="%s" stroke-width="0"%s>%s</g>' % (tr, c, c, extra, e)
    return '<g transform="%s" fill="%s"%s><path d="%s"/></g>' % (tr, c, extra, e)


def cells(cs, u=16, o=10):
    """unit squares on a grid, as path data (for emblems built from blocks)"""
    return ''.join('M%s %sh%sv%sh-%sZ' % (f(o + x * u), f(o + y * u), f(u), f(u), f(u)) for x, y in cs)


def flag(*parts):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">%s</svg>' % (W, H, ''.join(parts))


# ---------- emblems, in a 100 x 100 box ----------
_eagle_body = ('M44 33C40 40 39 56 45 66H55C61 56 60 40 56 33Z'
               'M44 40C34 34 22 26 9 15L11 24L4 24L11 31L3 33L11 39L6 43L16 47C25 50 35 50 44 50Z'
               'M56 40C66 34 78 26 91 15L89 24L96 24L89 31L97 33L89 39L94 43L84 47C75 50 65 50 56 50Z'
               'M46 65L38 84L44 82L50 89L56 82L62 84L54 65Z'
               'M45 60L35 72L30 70L32 77L39 75L47 65Z M55 60L65 72L70 70L68 77L61 75L53 65Z')
EMBLEMS = {
    'fleur': ('M50 6C59 19 63 32 56 50H44C37 32 41 19 50 6Z'
              'M55 47C62 30 80 24 88 36C94 46 87 58 77 55C82 50 81 43 76 41C69 39 62 45 61 54Z'
              'M45 47C38 30 20 24 12 36C6 46 13 58 23 55C18 50 19 43 24 41C31 39 38 45 39 54Z'
              'M32 52H68V60H32Z'
              'M44 60C40 72 33 79 26 83C35 84 44 79 50 71C56 79 65 84 74 83C67 79 60 72 56 60Z'),
    'eagle': _eagle_body + 'M46 34C44 26 40 21 34 21C30 21 27 23 26 26L32 27C32 30 36 32 41 35Z M26 26L21 28.5L27 29.5Z',
    'eagle2': _eagle_body + ('M46 34C44 26 40 21 34 21C30 21 27 23 26 26L32 27C32 30 36 32 41 35Z M26 26L21 28.5L27 29.5Z'
                             'M54 34C56 26 60 21 66 21C70 21 73 23 74 26L68 27C68 30 64 32 59 35Z M74 26L79 28.5L73 29.5Z'),
    'crown': 'M22 70L18 34L34 50L42 26L50 44L58 26L66 50L82 34L78 70Z M20 74H80V82H20Z',
    'lion': ('M36 18C28 17 22 23 23 30L18 33L24 36L27 41C31 44 35 44 37 43L41 52C42 60 44 66 47 70L42 80L35 83L33 90L43 90L48 83L55 73'
             'C59 80 62 86 61 90L71 90L68 82L63 74C66 66 66 58 63 51C67 47 72 43 77 41C85 37 88 27 82 19C86 28 81 33 75 34'
             'C69 35 64 41 60 45C58 38 55 31 50 27C47 22 42 19 36 18Z'
             'M39 45L27 41L21 45L22 38L28 36L37 39Z M42 55L30 57L25 63L27 56L33 53L42 52Z M37 18L41 11L44 19Z M30 19L31 12L35 18Z'),
    'castle': ('M16 88V50H22V40H30V50H38V30H33V20H39V26H45V20H55V26H61V20H67V30H62V50H70V40H78V50H84V88Z'
               'M44 88V70C44 64 56 64 56 70V88Z'),
    'keys': ('M27 18C21 18 17 23 17 28C17 34 22 38 28 37L70 79L66 83L71 88L75 84L78 87L82 83L79 80L83 76L36 30C37 24 33 18 27 18Z'
             'M27 24C30 24 31 27 30 29C29 31 25 31 24 28C23 26 25 24 27 24Z'
             'M73 18C79 18 83 23 83 28C83 34 78 38 72 37L30 79L34 83L29 88L25 84L22 87L18 83L21 80L17 76L64 30C63 24 67 18 73 18Z'
             'M73 24C70 24 69 27 70 29C71 31 75 31 76 28C77 26 75 24 73 24Z'),
    'sun': ''.join('M50 50L%s %sL%s %sZ' % (f(50 + 46 * math.cos(math.radians(a - 6))), f(50 + 46 * math.sin(math.radians(a - 6))),
                                              f(50 + 46 * math.cos(math.radians(a + 6))), f(50 + 46 * math.sin(math.radians(a + 6))))
                   for a in range(0, 360, 24)) + 'M50 26A24 24 0 1 1 49.9 26Z',
    'vergina': ''.join('M50 50L%s %sL%s %sL%s %sZ' % (f(50 + 18 * math.cos(math.radians(a - 11.25))), f(50 + 18 * math.sin(math.radians(a - 11.25))),
                                                     f(50 + 48 * math.cos(math.radians(a))), f(50 + 48 * math.sin(math.radians(a))),
                                                     f(50 + 18 * math.cos(math.radians(a + 11.25))), f(50 + 18 * math.sin(math.radians(a + 11.25))))
                       for a in [i * 22.5 for i in range(16)]) + 'M50 34A16 16 0 1 1 49.9 34Z',
    'dragon': ('M12 62C18 50 30 46 40 52C48 57 56 60 64 54C70 49 72 40 80 38C86 36 92 40 92 46C88 42 84 43 82 47C80 52 74 62 64 66'
               'C54 70 44 66 36 61C28 56 20 58 16 66Z'
               'M80 38L84 28L86 37Z M86 40L95 36L90 43Z M30 50L26 40L34 48Z M44 54L42 44L49 54Z M58 58L60 48L63 57Z'
               'M24 66L20 76L28 68Z M40 64L38 75L45 66Z M60 64L62 75L66 63Z'),
    'pearl': 'M50 38A12 12 0 1 1 49.9 38Z',
    'hammersickle': ('M30 22C20 34 20 54 32 66C44 78 62 78 74 68L80 74L84 70L78 64C66 74 50 74 40 64C30 54 30 38 38 28Z'
                     'M44 40L50 34L72 56L80 52L86 58L78 66L72 60L74 56Z M36 72L66 46L70 50L40 76Z'),
    'tanit': 'M50 12A10 10 0 1 1 49.9 12Z M26 40H74V47H26Z M50 46L76 90H24Z',
    'trident': ('M47 90H53V70C60 70 66 64 66 56V22H60V56C60 60 58 63 54 64V30L50 12L46 30V64C42 63 40 60 40 56V22H34V56'
                'C34 64 40 70 47 70Z'),
    'swastika': cells([(2, r) for r in range(5)] + [(c, 2) for c in range(5)] + [(3, 0), (4, 0), (4, 3), (4, 4), (1, 4), (0, 4), (0, 1), (0, 0)]),
    'tug': ('M48 8H52V20H48Z M42 20C42 14 58 14 58 20L56 26H44Z M47 26H53V92H47Z'
            'M44 28C36 40 34 60 40 76C44 66 46 50 47 30Z M56 28C64 40 66 60 60 76C56 66 54 50 53 30Z'),
    'cross_pattee': 'M38 6H62L56 38L94 32V68L56 62L62 94H38L44 62L6 68V32L44 38Z',
    'jerusalem': ('M43 10H57V43H90V57H57V90H43V57H10V43H43Z'
                  'M12 12H26V26H12Z M74 12H88V26H74Z M12 74H26V88H12Z M74 74H88V88H74Z'),
    'shield': 'M18 14H82V50C82 72 66 84 50 92C34 84 18 72 18 50Z',
    'mosque': 'M30 90V60C30 44 50 34 50 26C50 34 70 44 70 60V90Z M16 90V40L20 30L24 40V90Z M76 90V40L80 30L84 40V90Z',
    'falcon': ('M50 28C46 28 44 31 44 34L40 37L45 38C45 44 46 52 48 58H52C54 52 55 44 55 38C55 32 54 28 50 28Z'
               'M46 40C36 34 22 30 6 30C14 36 18 38 22 40C16 42 12 44 8 48C20 48 32 48 46 48Z'
               'M54 40C64 34 78 30 94 30C86 36 82 38 78 40C84 42 88 44 92 48C80 48 68 48 54 48Z'
               'M47 58L40 76L50 70L60 76L53 58Z'),
}


# a lion passant (walking, facing the hoist) in a 100 x 50 box
_passant = ('M12 20C10 12 18 6 26 9C30 6 36 7 38 12C50 11 64 12 72 16C78 11 82 5 89 3C95 4 94 10 89 11C85 13 83 18 82 23'
            'L84 36L88 44L80 44L76 34C70 36 62 36 56 34L56 44L48 44L48 34C44 34 40 35 36 37L34 44L26 44L28 33L22 30'
            'C18 29 14 25 12 20Z M12 20L6 22L12 25Z')
_ring = lambda cx, cy, r, w: 'M%s %sa%s %s 0 1 1 -.01 0Z M%s %sa%s %s 0 1 0 .01 0Z' % (
    f(cx), f(cy - r), f(r), f(r), f(cx), f(cy - r + w), f(r - w), f(r - w))
EMBLEMS.update({
    'lion_passant': '<g transform="translate(0 25)"><path d="%s"/></g>' % _passant,
    'lions3': ''.join('<g transform="translate(14 %s) scale(.72 .5)"><path d="%s"/></g>' % (y, _passant) for y in (8, 38, 68)),
    'lionsun': ('<g transform="translate(60 30)">' + ''.join(
        '<path d="M0 0L%s %sL%s %sZ"/>' % (f(30 * math.cos(math.radians(a - 7))), f(30 * math.sin(math.radians(a - 7))),
                                        f(30 * math.cos(math.radians(a + 7))), f(30 * math.sin(math.radians(a + 7))))
        for a in range(-180, 1, 20)) + '<circle r="15"/></g>'
        '<g transform="translate(2 44) scale(.96 1)"><path d="%s"/></g>'
        '<path d="M28 52L18 18L22 16L32 50Z"/>' % _passant),
    'lion_mark': ('<g transform="translate(0 32)"><path d="%s"/></g>'
                  '<path d="M44 46C40 30 46 12 62 6C58 16 64 18 72 14C66 24 70 28 78 26C70 36 60 44 50 50Z"/>'
                  '<circle cx="22" cy="38" r="11" fill="none" stroke-width="3"/>'
                  '<path d="M6 60H28V80H6Z"/>' % _passant),
    'harp': ('M20 16C38 2 64 4 82 20L76 26C62 14 44 12 32 20L40 86L32 90Z M76 20L84 26L42 92L34 86Z'
             + ''.join('M%s %sh1.8V%sh-1.8Z' % (f(x), f(t), f(b)) for x, t, b in
                       ((41, 19, 84), (47, 16, 75), (53, 15.5, 66), (59, 16, 56), (65, 18, 47), (71, 21, 38)))),
    'horse': ('M18 46C24 38 40 36 58 38C64 30 70 22 78 16L80 8L84 14L90 18L94 26L88 28L84 24C80 30 76 38 74 46'
              'C76 54 78 60 84 66L80 70L72 62L66 54C58 58 46 58 38 56L36 66L40 76L34 78L28 64L24 56C18 62 14 70 8 72'
              'C10 64 16 56 18 46Z'),
    'vytis': ('M10 60C16 52 32 50 50 52C56 44 62 36 70 30L72 22L76 28L82 32L86 40L80 42L76 38C72 44 68 52 66 60'
              'C68 68 70 74 76 80L72 84L64 76L58 68C50 72 38 72 30 70L28 80L32 90L26 92L20 78L16 70C12 76 8 82 4 84'
              'C4 76 8 68 10 60Z'
              'M40 52L38 30C38 24 46 22 48 28L50 50Z M42 22A6 6 0 1 1 41.9 22Z'
              'M36 30L18 8L22 6L40 26Z M44 40C36 40 30 46 30 54C38 54 44 48 46 42Z'),
    'tamga': 'M46 90V48C34 44 26 34 26 18H32C32 30 40 38 50 40C60 38 68 30 68 18H74C74 34 66 44 54 48V90Z M38 64H62V70H38Z',
    'rings3': _ring(50, 31, 16, 7) + _ring(32, 62, 16, 7) + _ring(68, 62, 16, 7),
    'key': ('M50 8C42 8 36 14 36 22C36 30 42 35 47 36V84H58V78H52V72H58V66H52V36C58 35 64 30 64 22C64 14 58 8 50 8Z'
            'M50 15C54 15 57 18 57 22C57 26 54 29 50 29C46 29 43 26 43 22C43 18 46 15 50 15Z'),
    'chirho': ('<path d="M50 6V94" fill="none" stroke-width="9"/><path d="M50 10C74 10 74 46 50 46" fill="none" stroke-width="9"/>'
               '<path d="M22 34L78 82M78 34L22 82" fill="none" stroke-width="9"/>'),
    'doublecross': 'M45 6H55V94H45Z M28 26H72V35H28Z M20 50H80V60H20Z',
    'elephant': ('M14 70C10 56 16 40 32 36C44 32 60 34 70 40C76 34 86 34 90 42C94 50 92 60 88 68L90 82L84 82L82 70'
                 'C80 64 84 58 82 50C80 60 78 66 76 70L76 82H68L66 70C56 72 44 72 34 70L32 82H24L24 70C20 70 16 70 14 70Z'),
    'chakra': _ring(50, 50, 34, 7) + ''.join('M%s %sL%s %sL%s %sL%s %sZ' % (
        f(50 + 4 * math.cos(math.radians(a + 90))), f(50 + 4 * math.sin(math.radians(a + 90))),
        f(50 + 30 * math.cos(math.radians(a))), f(50 + 30 * math.sin(math.radians(a))),
        f(50 + 4 * math.cos(math.radians(a - 90))), f(50 + 4 * math.sin(math.radians(a - 90))),
        f(50 - 6 * math.cos(math.radians(a))), f(50 - 6 * math.sin(math.radians(a)))) for a in range(0, 360, 45)),
})

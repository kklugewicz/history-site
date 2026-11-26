"""A tiny kit for drawing landmark silhouettes as single SVG paths in a 100 x 100 box, standing on y = 96.

Solid shapes wind clockwise and holes (windows, arches, gaps) counter-clockwise, so the page can fill a whole icon
with one colour under the default nonzero rule: overlapping solids merge, and a hole cuts through exactly one solid.
"""
import math


def f(v):
    s = ('%.2f' % v).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def _area(pts):
    return sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))


def P(pts, hole=False):
    """polygon"""
    pts = list(pts)
    if (_area(pts) < 0) != hole: pts = pts[::-1]
    return 'M' + 'L'.join('%s %s' % (f(x), f(y)) for x, y in pts) + 'Z'


def R(x, y, w, h, hole=False):
    """rectangle"""
    return P([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], hole)


def C(cx, cy, r, hole=False):
    """circle"""
    s = 0 if hole else 1
    return 'M%s %sA%s %s 0 1 %d %s %sA%s %s 0 1 %d %s %sZ' % (
        f(cx - r), f(cy), f(r), f(r), s, f(cx + r), f(cy), f(r), f(r), s, f(cx - r), f(cy))


def D(cx, base, rx, ry, hole=False):
    """dome: half an ellipse standing on y = base"""
    if hole: return 'M%s %sA%s %s 0 0 0 %s %sZ' % (f(cx + rx), f(base), f(rx), f(ry), f(cx - rx), f(base))
    return 'M%s %sA%s %s 0 0 1 %s %sZ' % (f(cx - rx), f(base), f(rx), f(ry), f(cx + rx), f(base))


def A(x, y, w, h, hole=False, pointed=False):
    """arch: a w x h box (top-left x, y) with a round (or pointed) top"""
    r = w / 2
    if pointed:
        up = 'Q%s %s %s %s Q%s %s %s %s' % (f(x), f(y + r * .35), f(x + r), f(y), f(x + w), f(y + r * .35), f(x + w), f(y + r))
        dn = 'Q%s %s %s %s Q%s %s %s %s' % (f(x + w), f(y + r * .35), f(x + r), f(y), f(x), f(y + r * .35), f(x), f(y + r))
    else:
        up = 'A%s %s 0 0 1 %s %s' % (f(r), f(r), f(x + w), f(y + r))
        dn = 'A%s %s 0 0 0 %s %s' % (f(r), f(r), f(x), f(y + r))
    if hole: return 'M%s %sV%s%sV%sZ' % (f(x + w), f(y + h), f(y + r), dn, f(y + h))
    return 'M%s %sV%s%sV%sZ' % (f(x), f(y + h), f(y + r), up, f(y + h))


def O(cx, base, w, h):
    """onion dome"""
    hw = w / 2
    return ('M%s %s' % (f(cx - hw * .5), f(base)) +
            'C%s %s %s %s %s %s' % (f(cx - hw * 1.08), f(base - h * .12), f(cx - hw * 1.12), f(base - h * .55), f(cx - hw * .3), f(base - h * .76)) +
            'Q%s %s %s %s' % (f(cx - hw * .06), f(base - h * .88), f(cx), f(base - h)) +
            'Q%s %s %s %s' % (f(cx + hw * .06), f(base - h * .88), f(cx + hw * .3), f(base - h * .76)) +
            'C%s %s %s %s %s %s' % (f(cx + hw * 1.12), f(base - h * .55), f(cx + hw * 1.08), f(base - h * .12), f(cx + hw * .5), f(base)) + 'Z')


def B(cx, base, w, h):
    """bell: a stupa's body or a baroque tower cap"""
    hw = w / 2
    return 'M%s %sC%s %s %s %s %s %sC%s %s %s %s %s %sZ' % (
        f(cx - hw), f(base), f(cx - hw), f(base - h * .6), f(cx - hw * .4), f(base - h), f(cx), f(base - h),
        f(cx + hw * .4), f(base - h), f(cx + hw), f(base - h * .6), f(cx + hw), f(base))


def bud(cx, base, w, h, bulge=1.05):
    """a lotus-bud tower (Angkor, a Thai prang): widest a little above its base, tapering to a point"""
    hw = w / 2
    return 'M%s %sC%s %s %s %s %s %sC%s %s %s %s %s %sZ' % (
        f(cx - hw), f(base), f(cx - hw * bulge * 1.12), f(base - h * .33), f(cx - hw * .6), f(base - h * .67), f(cx), f(base - h),
        f(cx + hw * .6), f(base - h * .67), f(cx + hw * bulge * 1.12), f(base - h * .33), f(cx + hw), f(base))


def band(pts, w, hole=False):
    """a strip of width w along a polyline (cables, sails of a windmill, slanting legs)"""
    left, right = [], []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[max(0, i - 1)]
        x1, y1 = pts[min(len(pts) - 1, i + 1)]
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L * w / 2, dx / L * w / 2
        left.append((x + nx, y + ny)); right.append((x - nx, y - ny))
    return P(left + right[::-1], hole)


def teeth(x0, x1, y, h, n, w):
    """n merlons of width w along a wall top from x0 to x1, standing on y"""
    if n == 1: return R((x0 + x1 - w) / 2, y - h, w, h)
    step = (x1 - x0 - w) / (n - 1)
    return ''.join(R(x0 + i * step, y - h, w, h) for i in range(n))


def eave(x0, x1, y, h, lift=3, inset=None):
    """an East Asian roof: from the eave line at y up h units, with upturned tips"""
    inset = h * 1.2 if inset is None else inset
    return P([(x0, y - lift), (x0 + 5, y), (x1 - 5, y), (x1, y - lift), (x1 - inset, y - h), (x0 + inset, y - h)])

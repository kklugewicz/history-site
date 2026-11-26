"""Build the painted base map: land terrain and ocean rasters in the page's Natural Earth projection.

    python3 scripts/build_basemap.py <source dir> data

Sources (public domain), fetched into <source dir> when missing:
  - Natural Earth 1:10m vectors (land, Antarctic ice shelves, bathymetry, lakes) from github.com/nvkelso/natural-earth-vector
  - Natural Earth cross-blended hypsometric shaded relief (shadedrelief.jpg) and NASA Blue Marble (bmng.jpg),
    both shipped in the basemap-data package on PyPI

Writes data/terrain/: land<L>[_c_r].webp (land only, transparent sea), sea<L>[_c_r].jpg and manifest.json.
Level 0 is the whole world in one image, deeper levels are split into tiles that the page loads as you zoom in.
Needs numpy, scipy and Pillow (with WebP)."""
import json, os, sys, subprocess, urllib.request, zipfile, time
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

Image.MAX_IMAGE_PIXELS = None
SRC, OUT = sys.argv[1], sys.argv[2]
TDIR = os.path.join(OUT, 'terrain')
os.makedirs(TDIR, exist_ok=True)
NE = 'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/'
BATHY = ['L_0', 'K_200', 'J_1000', 'I_2000', 'H_3000', 'G_4000', 'F_5000', 'E_6000', 'D_7000', 'C_8000', 'B_9000', 'A_10000']
DEPTHS = [0, 200, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


def fetch_sources():
    os.makedirs(os.path.join(SRC, 'ne'), exist_ok=True)
    for name in ['ne_10m_land', 'ne_10m_antarctic_ice_shelves_polys', 'ne_10m_lakes', 'ne_10m_lakes_historic'] + ['ne_10m_bathymetry_' + b for b in BATHY]:
        p = os.path.join(SRC, 'ne', name + '.geojson')
        if not os.path.exists(p):
            print('fetching', name); urllib.request.urlretrieve(NE + name + '.geojson', p)
    bd = os.path.join(SRC, 'basemap')
    if not os.path.exists(os.path.join(bd, 'shadedrelief.jpg')):
        os.makedirs(bd, exist_ok=True)
        subprocess.check_call([sys.executable, '-m', 'pip', 'download', 'basemap-data==2.0.0', '--no-deps', '-d', bd])
        whl = [f for f in os.listdir(bd) if f.endswith('.whl')][0]
        with zipfile.ZipFile(os.path.join(bd, whl)) as z:
            for n in ('shadedrelief.jpg', 'bmng.jpg'):
                open(os.path.join(bd, n), 'wb').write(z.read('mpl_toolkits/basemap_data/' + n))


# ---------- Natural Earth I projection (the formulas of d3.geoNaturalEarth1) ----------
def fwd(lam, phi):
    p2 = phi * phi; p4 = p2 * p2
    return (lam * (0.8707 - 0.131979 * p2 + p4 * (-0.013791 + p4 * (0.003971 * p2 - 0.001529 * p4))),
            phi * (1.007226 + p2 * (0.015085 + p4 * (-0.044475 + 0.028874 * p2 - 0.005916 * p4))))


def inv(x, y):
    phi = np.array(y, dtype=np.float64, copy=True)
    for _ in range(25):
        p2 = phi * phi; p4 = p2 * p2
        f = phi * (1.007226 + p2 * (0.015085 + p4 * (-0.044475 + 0.028874 * p2 - 0.005916 * p4))) - y
        df = 1.007226 + p2 * (0.015085 * 3 + p4 * (-0.044475 * 7 + 0.028874 * 9 * p2 - 0.005916 * 11 * p4))
        d = f / df; phi = phi - d
        if np.nanmax(np.abs(d)) < 1e-10: break
    p2 = phi * phi
    return x / (0.8707 + p2 * (-0.131979 + p2 * (-0.013791 + p2 * p2 * p2 * (0.003971 - 0.001529 * p2)))), phi


X0 = fwd(np.pi, 0.0)[0]
Y0 = fwd(0.0, np.pi / 2)[1]


def size_of(W): return W, int(round(W * Y0 / X0))


def grid(W, H, x0, y0, w, h):
    """lon/lat (degrees) of the pixel centres of a window of the W x H whole-sphere image"""
    xs = -X0 + (np.arange(x0, x0 + w) + .5) / W * 2 * X0
    ys = Y0 - (np.arange(y0, y0 + h) + .5) / H * 2 * Y0
    lam, phi = inv(*np.meshgrid(xs, ys))
    lon = np.degrees(lam); lat = np.degrees(phi)
    return np.clip(lon, -180, 180), np.clip(lat, -90, 90)


def to_px(lon, lat, W, H):
    x, y = fwd(np.radians(lon), np.radians(lat))
    return (x + X0) / (2 * X0) * W, (Y0 - y) / (2 * Y0) * H


def sample(img, lon, lat):
    """bilinear sample of an equirectangular image (rows from 90N, columns from 180W)"""
    Hs, Ws = img.shape[:2]
    fx = (lon + 180.0) / 360.0 * Ws - .5; fy = (90.0 - lat) / 180.0 * Hs - .5
    x0 = np.floor(fx).astype(np.int64); y0 = np.floor(fy).astype(np.int64)
    ax = (fx - x0)[..., None]; ay = (fy - y0)[..., None]
    xa = np.mod(x0, Ws); xb = np.mod(x0 + 1, Ws); ya = np.clip(y0, 0, Hs - 1); yb = np.clip(y0 + 1, 0, Hs - 1)
    f = lambda yy, xx: img[yy, xx].astype(np.float32)
    return ((f(ya, xa) * (1 - ax) + f(ya, xb) * ax) * (1 - ay) + (f(yb, xa) * (1 - ax) + f(yb, xb) * ax) * ay) / 255.0


# ---------- polygons to masks ----------
class Rings:
    """every ring of a polygon layer, projected once to the pixel space of a level"""
    def __init__(self, path, W, H, keep=None):
        self.rings = []
        for ft in json.load(open(path))['features']:
            g = ft['geometry']
            if not g or (keep and not keep(ft['properties'])): continue
            for poly in (g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]):
                for k, ring in enumerate(poly):
                    a = np.asarray(ring, dtype=np.float64)
                    if len(a) < 3: continue
                    x, y = to_px(a[:, 0], a[:, 1], W, H)
                    self.rings.append((k == 0, x, y, x.min(), x.max(), y.min(), y.max()))

    def mask(self, x0, y0, w, h, ss=2):
        im = Image.new('L', (w * ss, h * ss), 0); dr = ImageDraw.Draw(im)
        for outer, x, y, a, b, c, d in self.rings:
            if b < x0 or a > x0 + w or d < y0 or c > y0 + h: continue
            dr.polygon(list(zip(((x - x0) * ss).tolist(), ((y - y0) * ss).tolist())), fill=255 if outer else 0)
        if ss > 1: im = im.resize((w, h), Image.BOX)
        return np.asarray(im, dtype=np.float32) / 255.0


def lum(a): return a[..., 0] * .299 + a[..., 1] * .587 + a[..., 2] * .114


def hexc(h): return np.array([int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)], np.float32)


# ---------- land ----------
def paint_land(SR, BM, lon, lat, s, water):
    """natural colour from Blue Marble blended with Natural Earth's hypsometric tints, Natural Earth relief on top"""
    sr = sample(SR, lon, lat); bm = sample(BM, lon, lat)
    L = lum(sr)
    detail = L - ndimage.gaussian_filter(L, 4 * s)
    bm = ndimage.gaussian_filter(bm, (1.2 * s, 1.2 * s, 0))
    l = lum(bm)[..., None]
    g = l + (np.clip(bm, 0, 1) - l) * .85
    g = 1 - (1 - g) ** 1.9
    # Blue Marble's seasonal snow (tundra, taiga, high steppe) reads as blotches: in snowy regions follow Natural Earth,
    # which shows only lasting ice
    wb = (.55 * (1 - .95 * sample(SNOW, lon, lat)[..., 0]))[..., None]
    t = sr * (1 - wb) + g * wb
    t = np.clip(t + detail[..., None] * .9, 0, 1)
    t = 1 - (1 - t) ** 1.18
    if water is not None and water.max() > 0:
        # the page draws lakes over the land by date (reservoirs from the year they filled, the Aral Sea shrinking),
        # so paint the ground under every lake: the valley a reservoir drowned, the bed a lake left behind
        m = ndimage.binary_dilation(water > .05, iterations=max(1, int(round(1.5 * s))))
        iy, ix = ndimage.distance_transform_edt(m, return_distances=False, return_indices=True)
        fill = ndimage.gaussian_filter(t[iy, ix], (3 * s, 3 * s, 0))
        t = np.where(m[..., None], fill, t)
    return t


ICE = hexc('#eef3f6')


def snow_regions(SR, BM):
    """where Blue Marble shows snow (bright and grey, away from the tropics), smoothed over a degree or so (a quarter-degree grid)"""
    bm = np.asarray(Image.fromarray(BM).resize((1440, 720), Image.BOX), np.float32) / 255
    lat = 90 - (np.arange(720) + .5) / 4
    raw = np.clip((lum(bm) - .5) / .15, 0, 1) * np.clip((.2 - (bm.max(-1) - bm.min(-1))) / .1, 0, 1) * np.clip((np.abs(lat) - 38) / 10, 0, 1)[:, None]
    reg = np.clip(ndimage.gaussian_filter(raw, 4, mode=('nearest', 'wrap')) * 1.8, 0, 1)
    return (reg * 255).round().astype(np.uint8)[..., None]


def build_land(level, W, tiles, SR, BM):
    W, H = size_of(W)
    s = W / 2700.0
    land = Rings(os.path.join(SRC, 'ne', 'ne_10m_land.geojson'), W, H)
    shelves = Rings(os.path.join(SRC, 'ne', 'ne_10m_antarctic_ice_shelves_polys.geojson'), W, H)
    water = Rings(os.path.join(SRC, 'ne', 'ne_10m_lakes.geojson'), W, H)
    water.rings += Rings(os.path.join(SRC, 'ne', 'ne_10m_lakes_historic.geojson'), W, H).rings
    cols, rows = tiles
    TW, TH = -(-W // cols), -(-H // rows)
    pad = int(round(16 * s)) + 4
    out = []
    for r in range(rows):
        for c in range(cols):
            x0, y0 = c * TW, r * TH
            w, h = min(TW, W - x0), min(TH, H - y0)
            ov = 1 if cols > 1 else 0
            # the window we paint, with an overlap of a pixel on each side so tiles never show a seam
            wx0, wy0 = max(0, x0 - ov), max(0, y0 - ov)
            wx1, wy1 = min(W, x0 + w + ov), min(H, y0 + h + ov)
            px0, py0 = max(0, wx0 - pad), max(0, wy0 - pad)
            px1, py1 = min(W, wx1 + pad), min(H, wy1 + pad)
            m = np.maximum(land.mask(px0, py0, px1 - px0, py1 - py0), shelves.mask(px0, py0, px1 - px0, py1 - py0))
            crop = (slice(wy0 - py0, wy1 - py0), slice(wx0 - px0, wx1 - px0))
            if m[crop].max() < 1e-3: continue
            lon, lat = grid(W, H, px0, py0, px1 - px0, py1 - py0)
            t = paint_land(SR, BM, lon, lat, s, water.mask(px0, py0, px1 - px0, py1 - py0, ss=1))
            ice = shelves.mask(px0, py0, px1 - px0, py1 - py0)
            t = t * (1 - ice[..., None]) + ICE * ice[..., None]
            rgba = np.dstack([np.clip(t[crop], 0, 1) * 255, m[crop] * 255]).round().astype(np.uint8)
            name = 'land%d.webp' % level if cols == 1 else 'land%d_%d_%d.webp' % (level, c, r)
            Image.fromarray(rgba, 'RGBA').save(os.path.join(TDIR, name), 'WEBP', quality=80, method=6)
            out.append({'c': c, 'r': r, 'x': wx0, 'y': wy0, 'w': wx1 - wx0, 'h': wy1 - wy0, 'f': name})
            print('  ', name, wx1 - wx0, wy1 - wy0, os.path.getsize(os.path.join(TDIR, name)) // 1024, 'KB')
    return {'w': W, 'h': H, 'tiles': out}


# ---------- sea ----------
SEA_STOPS = [(0, '#b7dbe0'), (150, '#a3cdd6'), (600, '#8dbdcf'), (1500, '#7cafc6'), (3000, '#6ea2bd'),
             (4500, '#6496b4'), (6000, '#5989aa'), (8000, '#4a789a')]


def build_sea(level, W, tiles):
    W, H = size_of(W)
    s = W / 2700.0
    t0 = time.time()
    depth = np.zeros((H, W), np.float32)
    for i, b in enumerate(BATHY[1:], 1):
        depth += Rings(os.path.join(SRC, 'ne', 'ne_10m_bathymetry_%s.geojson' % b), W, H).mask(0, 0, W, H) * (DEPTHS[i] - DEPTHS[i - 1])
    land = Rings(os.path.join(SRC, 'ne', 'ne_10m_land.geojson'), W, H).mask(0, 0, W, H)
    print('  depth', round(time.time() - t0, 1), 's')
    lon, lat = grid(W, H, 0, 0, W, H)
    d = ndimage.gaussian_filter(depth, 1.6 * s)
    xs = np.array([a for a, _ in SEA_STOPS], np.float32); cs = np.stack([hexc(c) for _, c in SEA_STOPS])
    C = np.dstack([np.interp(d, xs, cs[:, k]) for k in range(3)]).astype(np.float32)
    # the sea floor, lit from the north-west
    gy, gx = np.gradient(ndimage.gaussian_filter(depth, 2.5 * s))
    C *= 1 + np.clip((gx + gy) / 900.0 / s, -1, 1)[..., None] * .07
    alat = np.abs(lat)
    trop = np.clip((32 - alat) / 14, 0, 1); polar = np.clip((alat - 52) / 20, 0, 1)
    shallow = np.clip(1 - d / 800, 0, 1)
    C += (trop * shallow)[..., None] * (hexc('#8fe0d6') - C) * .5      # lagoon-turquoise warm shallows
    C += polar[..., None] * (hexc('#a9bcc2') - C) * .45                   # grey-green cold seas
    # water lightens near the coast; big land masses glow more than specks of islands
    lab, n = ndimage.label(land > .5)
    sizes = ndimage.sum(np.ones_like(land), lab, index=np.arange(1, n + 1)) if n else np.zeros(0)
    big = np.isin(lab, np.nonzero(sizes >= 40 * s * s)[0] + 1)
    dist = ndimage.distance_transform_edt(~big) / s
    dsmall = ndimage.distance_transform_edt(~(land > .5)) / s
    glow = np.exp(-dist / 7.0) * .25 + np.exp(-dist / 30.0) * .09 + np.exp(-dsmall / 2.5) * .09
    C += glow[..., None] * (1 - C)
    # pack ice over the high Arctic
    rng = np.random.default_rng(7)
    noise = ndimage.gaussian_filter(rng.random((H // 4 + 1, W // 4 + 1)).astype(np.float32), 2)
    noise = np.kron(noise, np.ones((4, 4), np.float32))[:H, :W]
    noise = (noise - noise.min()) / (np.ptp(noise) + 1e-6)
    ice = np.clip((lat - 78.5) / 5, 0, 1) * np.clip(.7 + .6 * noise, 0, 1)
    C += ice[..., None] * (hexc('#eef4f6') - C) * .8
    C = np.clip(C, 0, 1)
    cols, rows = tiles
    TW, TH = -(-W // cols), -(-H // rows)
    out = []
    for r in range(rows):
        for c in range(cols):
            ov = 1 if cols > 1 else 0
            x0, y0 = max(0, c * TW - ov), max(0, r * TH - ov)
            x1, y1 = min(W, (c + 1) * TW + ov), min(H, (r + 1) * TH + ov)
            name = 'sea%d.jpg' % level if cols == 1 else 'sea%d_%d_%d.jpg' % (level, c, r)
            Image.fromarray((C[y0:y1, x0:x1] * 255).round().astype(np.uint8)).save(os.path.join(TDIR, name), quality=82, optimize=True, progressive=True)
            out.append({'c': c, 'r': r, 'x': x0, 'y': y0, 'w': x1 - x0, 'h': y1 - y0, 'f': name})
            print('  ', name, os.path.getsize(os.path.join(TDIR, name)) // 1024, 'KB')
    return {'w': W, 'h': H, 'tiles': out}


if __name__ == '__main__':
    fetch_sources()
    SR = np.asarray(Image.open(os.path.join(SRC, 'basemap', 'shadedrelief.jpg')).convert('RGB'))
    BM = np.asarray(Image.open(os.path.join(SRC, 'basemap', 'bmng.jpg')).convert('RGB'))
    SNOW = snow_regions(SR, BM)
    only = sys.argv[3].split(',') if len(sys.argv) > 3 else None
    man_path = os.path.join(TDIR, 'manifest.json')
    man = json.load(open(man_path)) if os.path.exists(man_path) else {'land': [None] * 3, 'sea': [None] * 2}
    for lv, W, tl in [(0, 2700, (1, 1)), (1, 5400, (4, 2)), (2, 10800, (8, 4))]:
        if only and 'land%d' % lv not in only: continue
        print('land level', lv); man['land'][lv] = build_land(lv, W, tl, SR, BM)
    for lv, W, tl in [(0, 2700, (1, 1)), (1, 5400, (4, 2))]:
        if only and 'sea%d' % lv not in only: continue
        print('sea level', lv); man['sea'][lv] = build_sea(lv, W, tl)
    json.dump(man, open(man_path, 'w'), separators=(',', ':'))

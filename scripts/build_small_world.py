"""Write the small whole-world pictures of the painted base map: land0 and sea0 at half size.

    python3 scripts/build_small_world.py data

A phone, and the painted sea under the waves (drawn at one canvas pixel per CSS pixel), never needs more than about
1,500 pixels across for the whole world, but the 2,700-pixel world pictures take 15 MB each once decoded. These halves
(land_s.webp, sea_s.jpg, about 4 MB each decoded) are listed in data/terrain/manifest.json under "small", and the page
puts them in front of the other levels. scripts/build_basemap.py runs this at its end. Needs Pillow (with WebP)."""
import json, os, sys
from PIL import Image

OUT = sys.argv[1] if len(sys.argv) > 1 else 'data'


def build_small(out=OUT):
    tdir = os.path.join(out, 'terrain')
    man_path = os.path.join(tdir, 'manifest.json')
    man = json.load(open(man_path))
    small = {}
    for kind, src, dst, save in [
        ('land', 'land0.webp', 'land_s.webp', lambda im, p: im.save(p, 'WEBP', quality=85, method=6)),
        ('sea', 'sea0.jpg', 'sea_s.jpg', lambda im, p: im.save(p, quality=85, optimize=True, progressive=True)),
    ]:
        im = Image.open(os.path.join(tdir, src))
        im.load()
        w, h = (im.width + 1) // 2, (im.height + 1) // 2
        save(im.resize((w, h), Image.LANCZOS), os.path.join(tdir, dst))
        small[kind] = {'w': w, 'h': h, 'tiles': [{'c': 0, 'r': 0, 'x': 0, 'y': 0, 'w': w, 'h': h, 'f': dst}]}
    man['small'] = small
    json.dump(man, open(man_path, 'w'), separators=(',', ':'))


if __name__ == '__main__':
    build_small()

"""
Convert an image to the <tspan> block used in the class="ascii" portrait.

    pip install Pillow
    python tools/ascii.py > art.txt

Then paste the output over the existing <tspan> lines inside
<text ... class="ascii"> in BOTH light_mode.svg and dark_mode.svg.
"""
import sys
from PIL import Image, ImageOps, ImageEnhance

SRC = r"path/to/your/photo.jpg"   # <-- set this
W = 40            # characters wide. Keep <= 40 or it overlaps the text panel (x=420).
CELL_ASPECT = 2.05   # monospace char height / width
GAMMA = 0.78         # < 1 brightens midtones so facial detail survives

img = Image.open(SRC).convert("L")
img = ImageOps.autocontrast(img, cutoff=2)
img = ImageEnhance.Contrast(img).enhance(1.1)
img = img.point(lambda v: int(255 * ((v / 255) ** GAMMA)))

w, h = img.size
H = max(1, int(round(W * (h / w) / CELL_ASPECT)))
img = img.resize((W, H), Image.LANCZOS)
px = img.load()

chars = " .:-=+*#%@"   # light -> dark


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


for y in range(H):
    row = "".join(chars[int((255 - px[x, y]) / 255 * (len(chars) - 1))] for x in range(W))
    print(f'<tspan x="15" y="{30 + y * 20}">{esc(row.rstrip())}</tspan>')

print(f"\n--- {H} rows ---", file=sys.stderr)

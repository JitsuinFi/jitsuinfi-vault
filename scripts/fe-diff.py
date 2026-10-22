# Usage: diff.py <baseline-dir> <new-dir> [out-dir]: share of pixels that differ (any channel > 24) per shot.
import sys, os
from PIL import Image, ImageChops
a, b = sys.argv[1], sys.argv[2]; out = sys.argv[3] if len(sys.argv) > 3 else None
for f in sorted(os.listdir(a)):
    if not f.endswith(".jpg"): continue
    if not os.path.exists(os.path.join(b, f)): print(f"{f:32} MISSING"); continue
    x = Image.open(os.path.join(a, f)).convert("RGB"); y = Image.open(os.path.join(b, f)).convert("RGB")
    if x.size != y.size: print(f"{f:32} SIZE {x.size} vs {y.size}"); continue
    d = ImageChops.difference(x, y).convert("L").point(lambda v: 255 if v > 24 else 0)
    share = sum(d.histogram()[255:]) / (x.size[0] * x.size[1]) * 100
    bbox = d.getbbox()
    print(f"{f:32} {share:6.2f} %  {bbox}")
    if out and share > 0.05:
        os.makedirs(out, exist_ok=True); d.save(os.path.join(out, f.replace(".jpg", "-diff.png")))

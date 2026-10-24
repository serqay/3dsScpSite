"""Draws the decorative images of the site (own art): background tile, 88x31 buttons,
under-construction sign, animated divider, hit counter digits. Run from the repo root: python tools/make_decor.py"""
import os
import random
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "img")
os.makedirs(OUT, exist_ok=True)


def font(size, bold=False):
    for name in ("courbd.ttf" if bold else "cour.ttf", "arial.ttf", "DejaVuSansMono.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


# background: dark noise with scanlines
random.seed(173)
bg = Image.new("RGB", (64, 64))
px = bg.load()
for y in range(64):
    for x in range(64):
        v = random.randint(6, 18) + (6 if y % 4 == 0 else 0)
        px[x, y] = (v, v + 2, v)
bg.save(os.path.join(OUT, "bg.png"))


def button(name, text, fg, bgc, border):
    im = Image.new("RGB", (88, 31), bgc)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 87, 30], outline=border)
    d.rectangle([1, 1, 86, 29], outline=tuple(c // 2 for c in border))
    lines = text.split("\n")
    f = font(11, True)
    h = 12 * len(lines)
    y = (31 - h) // 2
    for ln in lines:
        w = d.textlength(ln, font=f)
        d.text(((88 - w) / 2, y), ln, fill=fg, font=f)
        y += 12
    im.save(os.path.join(OUT, name))


button("btn_scp.png", "SCP\nFOUNDATION", (255, 255, 255), (20, 20, 20), (200, 200, 200))
button("btn_3ds.png", "NINTENDO\n3DS", (255, 255, 255), (170, 20, 20), (255, 120, 120))
button("btn_devkit.png", "made with\ndevkitPro", (0, 255, 0), (0, 40, 0), (0, 200, 0))
button("btn_notepad.png", "made with\nNotepad", (0, 0, 0), (230, 230, 200), (120, 120, 100))
button("btn_cc.png", "CC BY-SA\n3.0", (255, 255, 0), (30, 30, 60), (150, 150, 255))
button("btn_ie.png", "best viewed\n800x600", (255, 255, 255), (0, 0, 128), (100, 100, 255))

# under construction sign (animated: flashing lamps)
frames = []
for i in range(2):
    im = Image.new("RGB", (160, 56), (0, 0, 0))
    d = ImageDraw.Draw(im)
    for x in range(-20, 180, 16):
        d.polygon([(x, 0), (x + 8, 0), (x + 28, 10), (x + 20, 10)], fill=(255, 220, 0))
        d.polygon([(x, 56), (x + 8, 56), (x + 28, 46), (x + 20, 46)], fill=(255, 220, 0))
    d.rectangle([0, 10, 159, 45], fill=(255, 220, 0), outline=(0, 0, 0))
    d.rectangle([3, 13, 156, 42], outline=(0, 0, 0))
    f = font(13, True)
    for k, t in enumerate(("UNDER", "CONSTRUCTION")):
        w = d.textlength(t, font=f)
        d.text(((160 - w) / 2, 15 + k * 13), t, fill=(0, 0, 0), font=f)
    c = (255, 0, 0) if i == 0 else (90, 0, 0)
    d.ellipse([4, 2, 12, 10], fill=c)
    d.ellipse([147, 2, 155, 10], fill=(90, 0, 0) if i == 0 else (255, 0, 0))
    frames.append(im)
frames[0].save(os.path.join(OUT, "construction.gif"), save_all=True, append_images=frames[1:],
               duration=500, loop=0)

# animated divider: running hazard stripe
frames = []
for i in range(8):
    im = Image.new("RGB", (480, 8), (0, 0, 0))
    d = ImageDraw.Draw(im)
    for x in range(-16, 500, 16):
        o = x + i * 2
        d.polygon([(o, 8), (o + 8, 8), (o + 12, 0), (o + 4, 0)], fill=(200, 0, 0))
    frames.append(im)
frames[0].save(os.path.join(OUT, "divider.gif"), save_all=True, append_images=frames[1:],
               duration=90, loop=0)

# hit counter digits (one strip, decorative)
digits = "0000173"
im = Image.new("RGB", (14 * len(digits) + 4, 22), (20, 20, 20))
d = ImageDraw.Draw(im)
f = font(18, True)
for i, ch in enumerate(digits):
    d.rectangle([2 + i * 14, 2, 14 + i * 14, 20], fill=(0, 0, 0), outline=(70, 70, 70))
    d.text((4 + i * 14, 1), ch, fill=(255, 40, 40), font=f)
im.save(os.path.join(OUT, "counter.png"))

# classified stamp
im = Image.new("RGBA", (190, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(im)
d.rectangle([1, 1, 188, 46], outline=(220, 0, 0, 255), width=3)
f = font(20, True)
t = "LEVEL 2 CLEARANCE"
d.text(((190 - d.textlength(t, font=f)) / 2, 12), t, fill=(220, 0, 0, 255), font=f)
im.save(os.path.join(OUT, "stamp.png"))
print("decor done")

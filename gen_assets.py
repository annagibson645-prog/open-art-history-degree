"""Make the favicon and link-preview images. Run once: python gen_assets.py"""
from PIL import Image, ImageDraw, ImageFont
import pathlib
here = pathlib.Path(__file__).parent
GREEN, DEEP, WHITE, MUTED, MINT = (31, 94, 69), (12, 38, 28), (255, 255, 255), (176, 208, 188), (143, 211, 174)

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#1F5E45"/><g fill="#fff"><path d="M50 17 L83 36 H17 Z"/><rect x="20" y="39" width="60" height="5"/><rect x="22" y="47" width="8" height="30"/><rect x="38" y="47" width="8" height="30"/><rect x="54" y="47" width="8" height="30"/><rect x="70" y="47" width="8" height="30"/><rect x="17" y="80" width="66" height="5"/></g></svg>
'''
(here / "favicon.svg").write_text(SVG, encoding="utf-8")

def temple(size, bg=GREEN, radius=0.22):
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * radius), fill=bg)
    k = S / 100.0
    d.polygon([(50 * k, 17 * k), (83 * k, 36 * k), (17 * k, 36 * k)], fill=WHITE)
    d.rectangle((20 * k, 39 * k, 80 * k, 44 * k), fill=WHITE)
    for x in (22, 38, 54, 70):
        d.rectangle((x * k, 47 * k, (x + 8) * k, 77 * k), fill=WHITE)
    d.rectangle((17 * k, 80 * k, 83 * k, 85 * k), fill=WHITE)
    return im.resize((size, size), Image.LANCZOS)

temple(32).save(here / "favicon-32.png")
temple(180, radius=0.0).convert("RGB").save(here / "apple-touch-icon.png")

W, H = 1200, 630
img = Image.new("RGB", (W, H), DEEP)
d = ImageDraw.Draw(img)
d.rectangle((0, 0, 14, H), fill=MINT)
F = "C:/Windows/Fonts/"
title = ImageFont.truetype(F + "georgia.ttf", 92)
title_i = ImageFont.truetype(F + "georgiai.ttf", 92)
sub = ImageFont.truetype(F + "segoeui.ttf", 34)
small = ImageFont.truetype(F + "segoeui.ttf", 28)
t = temple(120)
img.paste(t, (84, 84), t)
d.text((84, 250), "Study Art History,", font=title, fill=WHITE)
d.text((84, 356), "Tuition Free", font=title_i, fill=WHITE)
d.text((84, 492), "From the first cave paintings to the contemporary gallery.", font=sub, fill=MUTED)
d.text((84, 548), "Pick your classes. See the hours. Everything saves in your browser.", font=small, fill=MUTED)
img.save(here / "og-image.png", optimize=True)
print("assets ok")

# -*- coding: utf-8 -*-
"""SUCH MAN brand assets generator (decorative vector art)."""
import os

OUT = "/Users/own/Projects/such-man-storefront/assets/brand"
os.makedirs(OUT, exist_ok=True)

G, S, CORY = "#171714", "#777866", "#a77a52"
WHITE, BONE, FAAD = "#fbf6ec", "#e8e5dc", "#b98a4e"

def svg(body, w=600, h=600):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'role="img" aria-hidden="true">{body}</svg>')

def rect(x, y, w, h, fill):
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{fill}"/>'

def circle(x, y, r, fill):
    return f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="{fill}"/>'

def line(x1, y1, x2, y2, stroke, sw=1.5):
    return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{stroke}" stroke-width="{sw}"/>'

def text(x, y, s, size=20, fill="#fbf6ec", weight="700", ls=None):
    ls = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-family=\'Space Grotesk, "Arial Black", sans-serif\''
            f' font-weight="{weight}" font-size="{size}"{ls}>{s}</text>')

# ------------------------------------------------------- favicon
fav = (f'<rect width="64" height="64" fill="{G}"/>'
       + circle(32, 30, 11, CORY)
       + text(21, 34, "SM", 28, "#fbf6ec", 900, ls="2"))
open(f"{OUT}/favicon.svg", "w").write(svg(fav, 64, 64))

# --------------------------------------------------- hero mark
hero = (f'<rect width="600" height="600" fill="{G}"/>'
        + rect(120, 120, 360, 360, "#25261f")
        + rect(140, 140, 320, 320, "#2d2e24")
        + text(300, 240, "S", 150, "#fbf6ec", 900, ls="14")
        + text(300, 380, "M", 150, "#fbf6ec", 900, ls="14")
        + circle(300, 300, 46, CORY)
        + text(300, 180, "SM", 22, "#b98a4e", 700, ls="4")
        + line(240, 120, 360, 120, FAAD, 3)
        + line(240, 480, 360, 480, FAAD, 3)
        + line(120, 240, 120, 360, FAAD, 3)
        + line(480, 240, 480, 360, FAAD, 3))
open(f"{OUT}/hero-art.svg", "w").write(svg(hero))

# ------------------------------------------------------- story art
story = (f'<rect width="600" height="600" fill="{G}"/>'
         + rect(80, 110, 440, 380, "#25261f")
         + rect(80, 110, 440, 260, "#2d2e24")
         + rect(160, 110, 280, 260, "#1f201a")
         + text(300, 252, "S", 150, "#fbf6ec", 900, ls="12")
         + text(300, 362, "M", 150, "#fbf6ec", 900, ls="12")
         + rect(210, 400, 180, 24, FAAD)
         + rect(150, 470, 300, 90, "#2d2e24")
         + circle(300, 515, 34, CORY)
         + text(300, 565, "SM", 22, "#b98a4e", 700, ls="4")
         + line(230, 400, 370, 400, FAAD, 3)
         + line(230, 430, 370, 430, FAAD, 3))
open(f"{OUT}/story-art.svg", "w").write(svg(story))

# ------------------------------------------------------- hat capsule
hat = (f'<rect width="600" height="600" fill="#171714"/>'
       + rect(150, 270, 300, 300, "#46473c")
       + rect(150, 270, 300, 90, "#37382f")
       + circle(300, 295, 14, "#666758")
       + text(300, 360, "SUCH", 46, "#d4d1c2", 900, ls="-2")
       + text(300, 400, "MAN", 46, "#d4d1c2", 900, ls="-2")
       + text(300, 452, "12/12", 16, "#c8c6b3", 700, ls="2"))
open(f"{OUT}/hat-capsule.svg", "w").write(svg(hat))

# ------------------------------------------------------- future wardrobe
def garment(x, y, w, h, shape_id, body, dark=False):
    """Simple garment icon on a dark ground."""
    ground = '#171714' if dark else '#25261f'
    return (f'<rect width="600" height="600" fill="{ground}"/>'
            + rect(x, y, w, h, "#25261f" if dark else "#46473c")
            + body
            + circle(x + w/2, y + h/2 + 8, 26, CORY)
            + text(x + w/2, y + h/2 - 26, "SM", 22, "#b98a4e", 700, ls="4"))

hoodie = garment(60, 120, 480, 420,
    "hoodie",
    ('<path d="M220 250 Q200 180 300 170 Q400 180 380 250 L420 300 C300 330 180 330 120 290 L160 230 Q180 200 220 250Z" '
     'fill="#2d2e24" stroke="#777866" stroke-width="3" stroke-linejoin="round"/>'
     '<path d="M220 250 Q250 210 300 220 Q350 210 380 250 L380 300 L220 300Z" fill="#3a3b2f" stroke="#777866" stroke-width="3" stroke-linejoin="round"/>'
     '<path d="M260 300 L340 300" stroke="#777866" stroke-width="4"/>'
     '<path d="M300 340 L300 380" stroke="#a77a52" stroke-width="4"/>'))

longsleeve = garment(60, 150, 480, 380,
    "longsleeve",
    ('<path d="M220 300 L150 330 L70 420 L120 500 L260 470 L320 420 L410 490 L470 400 L390 340 Z" '
     'fill="#2d2e24" stroke="#777866" stroke-width="3" stroke-linejoin="round"/>'
     '<path d="M220 300 L250 330 L300 350 L350 330 L400 360 L470 330 L430 300 L330 300 Z" '
     'fill="#3a3b2f" stroke="#777866" stroke-width="3" stroke-linejoin="round"/>'
     '<path d="M260 360 L340 360" stroke="#777866" stroke-width="4"/>'
     '<path d="M300 400 L300 440" stroke="#a77a52" stroke-width="4"/>'))

buckethat = garment(60, 200, 480, 320,
    "bucket hat",
    ('<path d="M200 150 Q210 60 300 55 Q390 60 400 150 Z" fill="#46473c" stroke="#898b70" stroke-width="3"/>'
     '<path d="M200 150 Q300 130 400 150 L440 190 Q300 230 160 190 Z" fill="#34372a" stroke="#898b70" stroke-width="3"/>'
     '<path d="M240 160 Q300 190 360 160" fill="none" stroke="#8c8e73" stroke-width="2"/>'
     '<path d="M300 40 L300 120" stroke="#666858" stroke-width="2"/>'
     '<text x="300" y="110" fill="#e0ddca" text-anchor="middle" font-size="24" font-family="Arial" font-weight="bold">SM</text>'))

beanie = garment(60, 220, 480, 300,
    "beanie",
    ('<path d="M200 120 Q210 50 300 45 Q390 50 400 120 Z" fill="#24251f" stroke="#777968" stroke-width="3"/>'
     '<path d="M198 110 Q300 100 402 110 L406 140 Q300 152 194 140 Z" fill="#393a31" stroke="#777968" stroke-width="3"/>'
     '<path d="M216 118 V150 M236 118 V152 M256 116 V155 M276 115 V157 M296 115 V158 M316 116 V157 M336 118 V155" '
     'stroke="#686a5a" stroke-width="2"/>'
     '<text x="300" y="100" fill="#d8d5c7" text-anchor="middle" font-size="26" font-family="Arial" font-weight="bold">SM</text>'))

tote = garment(60, 180, 480, 340,
    "tote",
    ('<path d="M180 200 L300 200 L340 420 L260 420 Z" fill="#2d2e24" stroke="#777968" stroke-width="3"/>'
     '<path d="M210 202 V180 Q210 150 300 150 Q390 150 390 202 V200" fill="none" stroke="#777968" stroke-width="7"/>'
     '<text x="300" y="280" fill="#d8d5c7" text-anchor="middle" font-size="24" font-family="Arial" font-weight="bold">SUCH</text>'
     '<text x="300" y="304" fill="#d8d5c7" text-anchor="middle" font-size="24" font-family="Arial" font-weight="bold">MAN</text>'
     '<path d="M210 340 H390" stroke="#777968" stroke-width="1.5"/>'))

specialcap = garment(60, 190, 480, 330,
    "special cap",
    ('<path d="M210 200 Q225 80 300 75 Q375 80 390 200 Z" fill="#34362e" stroke="#8a8b78" stroke-width="3"/>'
     '<path d="M210 200 Q300 190 390 200 Q355 230 300 232 Q245 230 210 200 Z" fill="#24251f" stroke="#8a8b78" stroke-width="3"/>'
     '<path d="M300 90 V200" stroke="#666858" stroke-width="2"/>'
     '<text x="300" y="130" fill="#d8d5c7" text-anchor="middle" font-size="30" font-family="Arial" font-weight="bold">SM</text>'
     '<text x="370" y="230" fill="#d0cdbb" text-anchor="middle" font-size="12" font-family="monospace" letter-spacing="1">01/12</text>'))

open(f"{OUT}/hoodie.svg", "w").write(svg(hoodie))
open(f"{OUT}/longsleeve.svg", "w").write(svg(longsleeve))
open(f"{OUT}/buckethat.svg", "w").write(svg(buckethat))
open(f"{OUT}/beanie.svg", "w").write(svg(beanie))
open(f"{OUT}/tote.svg", "w").write(svg(tote))
open(f"{OUT}/specialcap.svg", "w").write(svg(specialcap))

print("brand assets:", sorted(os.listdir(OUT)))

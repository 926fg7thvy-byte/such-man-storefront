# -*- coding: utf-8 -*-
"""
SUCH MAN — shirt concept art generator (v3 layout pass).
Front + back SVGs for the six concepts. Every glyph kept inside the 360x420 garment.
"""
import os

OUT = "/Users/own/Projects/such-man-storefront/assets/product"
os.makedirs(OUT, exist_ok=True)

G, S = "#171714", "#777866"
CORY, OIL, CHAR2 = "#a77a52", "#74775a", "#5c5a52"
WHITE, BONE, FAAD = "#fbf6ec", "#e8e5dc", "#b98a4e"

def svg(body, width=None):
    w = f' width="{width}"' if width else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 420"{w} '
            f'role="img" aria-hidden="true">{body}</svg>')

def defs():
    return ('<defs>'
            '<linearGradient id="fabric" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#292a26"/><stop offset="0.52" stop-color="#292a26"/>'
            '<stop offset="1" stop-color="#11120f"/></linearGradient>'
            '<filter id="drop" x="-30%" y="-30%" width="160%" height="160%">'
            '<feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#000" flood-opacity="0.45"/></filter>'
            '<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">'
            '<feGaussianBlur stdDeviation="2.5"/></filter></defs>')

def ground(): return f'<rect width="360" height="420" fill="{G}"/>'
def tee(fill="#1c1c18"): return (f'<path d="M122 64 L87 79 39 129 66 157 95 127 96 356 264 356 265 127 294 157 321 129 273 79 238 64 Q180 92 122 64Z" fill="{fill}" stroke="{S}" stroke-width="1.6" stroke-linejoin="round"/>')
def neck(fill="#22231e"): return (f'<path d="M122 65 Q180 111 238 65 Q225 103 180 105 Q135 103 122 65Z" fill="{fill}" stroke="{S}" stroke-width="1.6" stroke-linejoin="round"/>')

def frame(x, y, w, h, color="#a77a52", sw=2, dash="7 6"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" stroke="{color}" stroke-width="{sw}" stroke-dasharray="{dash}"/>'
            f'<rect x="{x-2}" y="{y-2}" width="{w+4}" height="{h+4}" rx="8" fill="none" stroke="{color}" stroke-width="1" stroke-dasharray="5 8" opacity="0.5"/>')

def text(x, y, s, size=20, fill="#fbf6ec", weight="700", family="Space Grotesk", ls=None, anchor="middle"):
    ls = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-family="{family}" font-weight="{weight}" font-size="{size}"{ls}>{s}</text>')

def rect(x, y, w, h, fill="#1c1c18", stroke=None, sw=1, rx=0, opacity=1, dash=None):
    dash = f'stroke-dasharray="{dash}"' if dash else ""
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    r = f' rx="{rx}"' if rx else ""
    o = f' opacity="{opacity}"' if opacity != 1 else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}"{s}{dash}{o}/>'

def rule(x1, y1, x2, y2, color="#a77a52", sw=1.2, opacity=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" opacity="{opacity}"{d}/>')

def circle(x, y, r, fill=None, stroke=None, sw=1, opacity=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity != 1 else ""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"{s}{o}/>')

def chest_mark(x, y, size=18, color=CORY):
    s = size/8.0
    return (f'<g transform="translate({x},{y}) scale({s})" fill="none">'
            f'<path d="M14 0 L0 0 L0 14" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>'
            f'<path d="M-14 0 L0 0 L0 14" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>'
            f'<path d="M0 14 L14 0 L0 0" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/></g>')

def show(x, y, s, size, fill, weight="700", ls=None, family="Space Grotesk"):
    return text(x, y, s, size, fill, weight, family, ls=ls)

# ============================================================ 1. KNOWS CODE
def c1_front():
    return (ground() + tee() + neck()
            + frame(116, 136, 128, 200)
            + show(180, 164, "DROP 001 · THE SIGNATURE", 8, CORY, ls="2.5", family="DM Mono")
            + chest_mark(180, 248)
            + show(180, 220, "S", 23, WHITE, ls="2")
            + show(180, 256, "U", 23, WHITE, ls="2")
            + show(180, 292, "C", 23, WHITE, ls="2")
            + show(180, 328, "H", 23, WHITE, ls="2")
            + show(180, 356, "KNOWS CODE", 13, WHITE, ls="1.5")
            + rule(142, 364, 218, 364, CORY, 1.2, 0.85)
            + show(180, 388, "01 / CODE", 8, CORY, ls="1.5", family="DM Mono")
            + show(180, 404, "NO ORDERS · CONCEPT", 7, "#777866", ls="1.5", family="DM Mono"))

def c1_back():
    return (ground() + tee() + neck()
            + frame(118, 136, 124, 214)
            + show(180, 188, "KNOWS", 23, WHITE, ls="2")
            + show(180, 226, "CODE", 23, CORY, ls="2")
            + rule(142, 250, 218, 250, CORY, 1.2, 0.7)
            + rule(142, 260, 218, 260, CORY, 1.2, 0.7)
            + show(180, 324, "01/25", 10, WHITE, ls="2")
            + rect(152, 342, 56, 56, "#1c1c18", CORY, 1, 0.5)
            + show(180, 394, "CODE · CONCEPT", 8, CORY, ls="2", family="DM Mono"))

# ====================================================== 2. SHE A MI COUSIN
def c2_front():
    return (ground() + tee("#d8d3c2") + neck()
            + frame(116, 136, 128, 200)
            + show(180, 162, "THE FAMILY", 8, OIL, ls="2.5", family="DM Mono")
            + show(180, 212, "SUCH MAN", 31, "#2b2a24", ls="1.5")
            + show(180, 288, "SHE A MI", 26, "#2b2a24", weight="700", ls="1.5")
            + show(180, 346, "COUSIN", 38, "#2b2a24", ls="1")
            + rule(142, 362, 218, 362, OIL, 1.5, 0.9)
            + show(180, 388, "02 / THE FAMILY STORY", 7, "#2b2a24", ls="1.5", family="DM Mono")
            + show(180, 404, "SUCH MAN® / 001", 7, OIL, ls="2", family="DM Mono"))

def c2_back():
    return (ground() + tee("#d8d3c2") + neck()
            + '<g fill="none" stroke="#74775a" stroke-width="2.5" stroke-linecap="round">'
            + '<path d="M128 232 L160 252 L190 230"/>'
            + '<circle cx="128" cy="232" r="5" fill="#2b2a24"/><circle cx="160" cy="252" r="5" fill="#2b2a24"/><circle cx="190" cy="230" r="5" fill="#2b2a24"/>'
            + '<path d="M120 248 L198 248"/>'
            + '<path d="M128 216 L160 232 L190 216"/>'
            + '<circle cx="128" cy="216" r="5" fill="#2b2a24"/><circle cx="190" cy="216" r="5" fill="#2b2a24"/></g>'
            + show(180, 388, "02/25", 8, "#2b2a24", ls="1.5", family="DM Mono")
            + show(180, 404, "SHE A MI COUSIN® / 001", 7, OIL, ls="1.5", family="DM Mono"))

# ====================================================== 3. DEH DEH
def c3_front():
    return (ground() + tee("#262621") + neck()
            + frame(116, 136, 128, 200)
            + show(180, 162, "DROP 003 · THE DISAPPEARING ACT", 8, FAAD, ls="2", family="DM Mono")
            + show(180, 218, "SUCH MAN", 19, "#e8e5dc", ls="1.5")
            + show(180, 274, "DEH DEH", 34, "#e8e5dc", weight="700", ls="1.5")
            + show(180, 334, "WHERE DEH?", 8, "#b0a894", ls="2", family="DM Mono")
            + rule(150, 352, 210, 352, CORY, 1.2, 0.85)
            + show(180, 384, "03 / THE DISAPPEARING ACT", 7, "#e8e5dc", ls="1.5", family="DM Mono")
            + show(180, 400, "SUCH MAN® / 001", 7, FAAD, ls="2", family="DM Mono"))

def c3_back():
    return (ground() + tee("#262621") + neck()
            + circle(180, 250, 46, None, FAAD, 3)
            + circle(180, 250, 34, None, FAAD, 1.5, 0.55)
            + '<g fill="none" stroke="#b98a4e" stroke-width="2.5" stroke-linecap="round">'
            + '<path d="M150 282 C160 278 170 268 180 262 C190 256 196 248 200 238"/>'
            + '<circle cx="180" cy="222" r="5" fill="#b98a4e"/></g>'
            + show(180, 332, "LOCATION UNKNOWN", 8, "#e8e5dc", ls="1.5", family="DM Mono")
            + show(180, 352, "03/25", 7, FAAD, ls="2", family="DM Mono"))

# ====================================================== 4. MI INNOCENT
def c4_front():
    return (ground() + tee("#262621") + neck()
            + rect(132, 148, 96, 22, "#3a3a34", "#a77a52", 1)
            + show(180, 166, "CASE FILE 04", 6.5, CORY, ls="1.8", family="DM Mono")
            + show(180, 218, "MI", 25, WHITE, ls="1")
            + rule(158, 248, 202, 248, "#3a3a34", 1)
            + show(180, 298, "NO COMMENT", 9.5, "#c9c4b2", ls="2.5", family="DM Mono")
            + show(180, 342, "INNOCENT", 38, WHITE, ls="1")
            + rule(148, 360, 212, 360, CORY, 1.2, 0.85, dash="4 4")
            + rect(180, 367, 3, 4, CORY)
            + show(180, 390, "04 / THE CASE FILE", 7, "#e8e5dc", ls="1.5", family="DM Mono")
            + show(180, 406, "NO EVIDENCE · NO CASE", 7, CORY, ls="2", family="DM Mono"))

def c4_back():
    return (ground() + tee("#262621") + neck()
            + frame(124, 148, 112, 192)
            + rect(132, 160, 96, 18, "#3a3a34")
            + show(180, 178, "CASE LIST", 6.5, CORY, ls="1.8", family="DM Mono")
            + rule(142, 194, 218, 194, "#5c5a52", 1, 0.7)
            + show(180, 248, "NO", 13, WHITE, ls="1")
            + show(180, 268, "EVIDENCE", 7, CHAR2, ls="2", family="DM Mono")
            + rule(142, 284, 218, 284, "#5c5a52", 1, 0.7)
            + show(180, 334, "NO", 13, WHITE, ls="1")
            + show(180, 354, "CASE", 7, CHAR2, ls="2", family="DM Mono")
            + rule(142, 366, 218, 366, "#5c5a52", 1, 0.7)
            + show(180, 398, "STATUS: DISMISSED", 8, CORY, ls="2", family="DM Mono")
            + rect(152, 370, 56, 56, "#1c1c18", CORY, 1, 0.5)
            + show(180, 424, "04/25", 7, "#e8e5dc", ls="1.5", family="DM Mono"))

# ====================================================== 5. JUST A FRIEND
def c5_front():
    return (ground() + tee("#2c2c26") + neck()
            + show(180, 204, "ADVISING", 7, FAAD, ls="2", family="DM Mono")
            + show(180, 386, "JUST A", 21, "#e8e5dc", weight="500", ls="2")
            + show(180, 318, "FRIEND", 52, "#e8e5dc", ls="1")
            + '<g fill="none" stroke="#b98a4e" stroke-width="2.5" stroke-linecap="round" opacity="0.9">'
            + '<circle cx="180" cy="318" r="74"/>'
            + '<circle cx="180" cy="318" r="60" fill="none" stroke="#b98a4e" stroke-width="1.5" opacity="0.6"/></g>'
            + show(180, 380, "05 / THE DENIAL", 7, "#e8e5dc", ls="1.5", family="DM Mono")
            + show(180, 396, "SUCH MAN® / 001", 7, FAAD, ls="2", family="DM Mono"))

def c5_back():
    return (ground() + tee("#2c2c26") + neck()
            + circle(180, 230, 30, None, FAAD, 2, 0.85)
            + circle(180, 230, 22, None, FAAD, 1, 0.5)
            + rect(120, 300, 120, 110, "#2c2c26", "#5c5a52", 1)
            + rect(130, 312, 100, 16, "#3a3a34")
            + show(180, 332, "CONTACT CARD", 6.5, CORY, ls="1.8", family="DM Mono")
            + rule(142, 350, 218, 350, "#5c5a52", 1, 0.7)
            + show(180, 396, "NOT AN ALIBI", 14, "#e8e5dc", ls="1")
            + rule(142, 410, 240, 410, "#5c5a52", 1, 0.7)
            + show(180, 444, "ADVICE · KEEP YOUR DISTANCE", 7, FAAD, ls="1.2", family="DM Mono")
            + show(180, 462, "05/25", 7, "#e8e5dc", ls="1.5", family="DM Mono"))

# ====================================================== 6. NO EVIDENCE, NO CASE
def c6_front():
    return (ground() + tee("#1c1c18") + neck()
            + show(180, 200, "ALL CLEAR", 7, CORY, ls="2", family="DM Mono")
            + show(180, 252, "NO EVIDENCE", 26, CHAR2, ls="3", family="DM Mono")
            + rule(150, 284, 210, 284, CORY, 1.2, 0.85)
            + show(180, 306, "NO CASE", 46, "#fbf6ec", ls="1.5")
            + show(180, 356, "06 / THE EXONERATION", 7, "#e8e5dc", ls="1.5", family="DM Mono")
            + show(180, 372, "06/25", 7, CORY, ls="2", family="DM Mono"))

def c6_back():
    return (ground() + tee("#1c1c18") + neck()
            + circle(180, 250, 120, None, CORY, 2, 0.85)
            + circle(180, 250, 108, None, CORY, 0.8, 0.4)
            + show(180, 226, "CASE FILE", 8, WHITE, ls="1.5", family="DM Mono")
            + show(180, 248, "NO EVIDENCE", 16, WHITE, ls="2")
            + show(180, 278, "NO CASE", 16, WHITE, ls="2")
            + show(180, 320, "✕", 18, CORY, ls="3")
            + show(180, 342, "DISMISSED", 7, CORY, ls="1.5", family="DM Mono")
            + rect(162, 378, 36, 36, "none", CORY, 1, 0.5)
            + show(180, 420, "06/25", 7, "#e8e5dc", ls="1.5", family="DM Mono"))

# ------------------------------------------------------------------- run ---
CONCEPTS = [
    ("such-man-knows-code", "SUCH MAN KNOWS CODE", c1_front, c1_back),
    ("such-man-she-a-mi-cousin", "SUCH MAN, SHE A MI COUSIN", c2_front, c2_back),
    ("such-man-deh-deh", "SUCH MAN DEH DEH", c3_front, c3_back),
    ("mi-innocent", "MI INNOCENT", c4_front, c4_back),
    ("just-a-friend", "JUST A FRIEND", c5_front, c5_back),
    ("no-evidence-no-case", "NO EVIDENCE, NO CASE", c6_front, c6_back),
]

def main():
    for slug, phrase, front_fn, back_fn in CONCEPTS:
        fpath = os.path.join(OUT, slug, "front.svg")
        bpath = os.path.join(OUT, slug, "back.svg")
        os.makedirs(os.path.dirname(fpath), exist_ok=True)
        for path, art, w in ((fpath, front_fn(), 100), (bpath, back_fn(), 100)):
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(svg(defs() + art, width=w))
        print(f"{slug}: front={fpath} back={bpath}")

if __name__ == "__main__":
    main()

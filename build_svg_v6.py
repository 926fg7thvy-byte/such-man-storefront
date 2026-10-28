# -*- coding: utf-8 -*-
"""SUCH MAN — shirt concept art generator v6.
Revision pass: (1) c5 front/back redesigned with the surveillance
ring as a FOREGROUND viewfinder around the word; (2) c1 back gets a
deliberate "X" stamp stamp (was an empty square); (3) c6 back gets a
proper garment tag (was a floating empty rectangle); (4) c6 front
"NO EVIDENCE" lightened to a legible tone.
All art text inside the 360x420 garment; captions on the ground below the tee.
"""
import os

OUT = "/Users/own/Projects/such-man-storefront/assets/product"
os.makedirs(OUT, exist_ok=True)

G, S = "#171714", "#777866"
CORY, OIL, CHAR2 = "#a77a52", "#74775a", "#c9c4b2"
WHITE, BONE, FAAD, FROST = "#fbf6ec", "#e8e5dc", "#b98a4e", "#c9c4b2"
PM = "#777866"  # caption on ground


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


def tee(fill="#1c1c18"):
    return (f'<path d="M122 64 L87 79 39 129 66 157 95 127 96 356 264 356 265 127 294 157 321 129 273 79 238 64 Q180 92 122 64Z" '
            f'fill="{fill}" stroke="{S}" stroke-width="1.6" stroke-linejoin="round"/>')


def neck(fill="#22231e"):
    return (f'<path d="M122 65 Q180 111 238 65 Q225 103 180 105 Q135 103 122 65Z" '
            f'fill="{fill}" stroke="{S}" stroke-width="1.6" stroke-linejoin="round"/>')


def frame(x, y, w, h, color="#a77a52", sw=2, dash="7 6", inner=True):
    """Rounded dashed frame; an optional faint outer scale for depth."""
    d = f'stroke-dasharray="{dash}"'
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" '
           f'stroke="{color}" stroke-width="{sw}" {d}/>')
    if inner:
        out += (f'<rect x="{x-2}" y="{y-2}" width="{w+4}" height="{h+4}" rx="8" fill="none" '
                f'stroke="{color}" stroke-width="1" stroke-dasharray="5 8" opacity="0.5"/>')
    return out


def text(x, y, s, size=20, fill="#fbf6ec", weight="700", family="Space Grotesk", ls=None, anchor="middle"):
    ls = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-family="{family}" '
            f'font-weight="{weight}" font-size="{size}"{ls}>{s}</text>')


def rect(x, y, w, h, fill="#1c1c18", stroke=None, sw=1, rx=0, opacity=1, dash=None):
    dash = f'stroke-dasharray="{dash}"' if dash else ""
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    r = f' rx="{rx}"' if rx else ""
    o = f' opacity="{opacity}"' if opacity != 1 else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}"{s}{dash}{o}/>'


def rule(x1, y1, x2, y2, color="#a77a52", sw=1.2, opacity=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" '
            f'opacity="{opacity}"{d}/>')


def line(x1, y1, x2, y2, color="#a77a52", sw=1):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"/>'


def circle(x, y, r, fill=None, stroke=None, sw=1, opacity=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity != 1 else ""
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"{s}{o}/>'


def cap(s, size, fill=PM, weight="700", ls=None, family="DM Mono", y=364, ls2=None):
    """footer caption on the ground below the tee."""
    return text(180, y, "§ " + s, size, fill, weight, family, ls=ls2 if ls2 else ls)


# ============================================================ 1. KNOWS CODE
def c1_front():
    return (ground() + tee() + neck()
            + frame(116, 136, 128, 200)
            + text(180, 158, "DROP 001 · THE SIGNATURE", 7.5, CORY, ls="2.5", family="DM Mono")
            + text(180, 212, "SUCH MAN", 30, WHITE, ls="2")
            + text(180, 274, "KNOWS CODE", 15, WHITE, ls="1.5")
            + rule(142, 304, 218, 304, CORY, 1.2, 0.85)
            + text(180, 348, "01 / CODE", 8, WHITE, ls="1.5", family="DM Mono")
            + cap("NO ORDERS · CONCEPT", 7))


def c1_back():
    return (ground() + tee() + neck()
            + frame(118, 136, 124, 214)
            + text(180, 188, "KNOWS", 23, WHITE, ls="2")
            + text(180, 226, "CODE", 23, CORY, ls="2")
            + rule(142, 250, 218, 250, CORY, 1.2, 0.7)
            + rule(142, 260, 218, 260, CORY, 1.2, 0.7)
            + text(180, 324, "01/25", 10, WHITE, ls="2")
            # deliberate "dismissed" stamp: X inside a filled ruled square (bottom right)
            + rect(176, 346, 68, 52, "#1c1c18", CORY, 1, rx=4)
            + text(200, 374, "✕", 26, CORY, weight="900", ls="2")
            # "dismissed" mark — no footer text (the back is self-contained)
        )

def c2_front():
    return (ground() + tee("#d8d3c2") + neck()
            + frame(116, 136, 128, 200)
            + text(180, 156, "THE FAMILY", 7.5, "#2b2a24", ls="2.5", family="DM Mono")
            + text(180, 208, "SUCH MAN", 30, "#2b2a24", ls="1.5")
            + text(180, 284, "SHE A MI", 25, "#2b2a24", weight="700", ls="1.5")
            + text(180, 338, "COUSIN", 34, "#2b2a24", ls="1")
            + rule(142, 356, 218, 356, OIL, 1.5, 0.9)
            + cap("02 / THE FAMILY STORY", 7, "#2b2a24", ls="1.5", family="DM Mono"))


def c2_back():
    return (ground() + tee("#d8d3c2") + neck()
            + '<g fill="none" stroke="#74775a" stroke-width="2.5" stroke-linecap="round">'
            + '<path d="M128 232 L160 252 L190 230"/>'
            + '<circle cx="128" cy="232" r="5" fill="#2b2a24"/><circle cx="160" cy="252" r="5" fill="#2b2a24"/><circle cx="190" cy="230" r="5" fill="#2b2a24"/>'
            + '<path d="M120 248 L198 248"/>'
            + '<path d="M128 216 L160 232 L190 216"/>'
            + '<circle cx="128" cy="216" r="5" fill="#2b2a24"/><circle cx="190" cy="216" r="5" fill="#2b2a24"/></g>'
            + text(180, 352, "02/25", 8, "#2b2a24", ls="1.5", family="DM Mono")
            + cap("SHE A MI COUSIN® / 001", 7, OIL, ls="1.5", family="DM Mono"))


# ====================================================== 3. DEH DEH
def c3_front():
    return (ground() + tee("#262621") + neck()
            + frame(116, 136, 128, 200)
            + text(180, 154, "DROP 003 · THE DISAPPEARING ACT", 7.5, FAAD, ls="2", family="DM Mono")
            + text(180, 200, "SUCH MAN", 18, FROST, ls="1.5")
            + text(180, 266, "DEH DEH", 32, FROST, weight="700", ls="1.5")
            + text(180, 326, "WHERE DEH?", 8, "#b0a894", ls="2", family="DM Mono")
            + rule(150, 344, 210, 344, CORY, 1.2, 0.85)
            + text(180, 352, "03 / THE DISAPPEARING ACT", 7, FROST, ls="1.5", family="DM Mono")
            + cap("SUCH MAN® / 001", 7, FAAD, ls="2", family="DM Mono"))


def c3_back():
    return (ground() + tee("#262621") + neck()
            + circle(180, 250, 46, None, FAAD, 3)
            + circle(180, 250, 34, None, FAAD, 1.5, 0.55)
            + '<g fill="none" stroke="#b98a4e" stroke-width="2.5" stroke-linecap="round">'
            + '<path d="M150 282 C160 278 170 268 180 262 C190 256 196 248 200 238"/>'
            + '<circle cx="180" cy="222" r="5" fill="#b98a4e"/></g>'
            + text(180, 330, "LOCATION UNKNOWN", 8, FROST, ls="1.5", family="DM Mono")
            + text(180, 350, "03/25", 7, FAAD, ls="2", family="DM Mono"))


# ====================================================== 4. MI INNOCENT
def c4_front():
    return (ground() + tee("#262621") + neck()
            + rect(132, 146, 96, 22, "#3a3a34", CORY, 1)
            + text(180, 160, "CASE FILE 04", 6.5, CORY, ls="1.8", family="DM Mono")
            + text(180, 208, "MI", 24, WHITE, ls="1")
            + rule(158, 240, 202, 240, "#3a3a34", 1)
            + text(180, 292, "NO COMMENT", 10, FROST, ls="2.5", family="DM Mono")
            + rule(148, 308, 212, 308, CORY, 1.2, 0.85, dash="4 4")
            + rect(180, 314, 3, 4, CORY)
            + text(180, 332, "INNOCENT", 30, WHITE, ls="1")
            + cap("04 / THE CASE FILE", 7, FROST, ls="1.5", family="DM Mono"))


def c4_back():
    return (ground() + tee("#262621") + neck()
            + frame(124, 146, 112, 154)
            + rect(132, 158, 96, 18, "#3a3a34")
            + text(180, 176, "CASE LIST", 6.5, FROST, ls="1.8", family="DM Mono")   # legible instead of dark
            + rule(142, 192, 218, 192, "#5c5a52", 1, 0.7)
            + text(180, 224, "NO", 13, WHITE, ls="1")
            + text(180, 244, "EVIDENCE", 7, CHAR2, ls="2", family="DM Mono")
            + rule(142, 266, 218, 266, "#5c5a52", 1, 0.7)
            + text(180, 296, "04/25", 7, WHITE, ls="1.5", family="DM Mono")
            + cap("CASE STATUS: DISMISSED", 7, CORY, ls="2", family="DM Mono"))


# ====================================================== 5. JUST A FRIEND  (RE-DESIGN)
def c5_front():
    return (ground() + tee("#2c2c26") + neck()
            # top label
            + text(180, 216, "JUST A", 22, FAAD, ls="2")
            # huge word in the middle
            + text(180, 294, "FRIEND", 56, WHITE, weight="800", ls="1")
            # FOREGROUND surveillance viewfinder rings (drawn AFTER the text)
            + circle(180, 300, 60, None, FAAD, 3.2)
            + circle(180, 300, 46, None, FAAD, 1.6, 0.55)
            + circle(180, 300, 7, None, "#b98a4e", 2.4)
            + cap("05 / THE DENIAL", 7, FROST, ls="1.5", family="DM Mono"))


def c5_back():
    return (ground() + tee("#2c2c26") + neck()
            + text(180, 244, "NOT AN ALIBI", 18, WHITE, ls="2")
            + text(180, 308, "ADVICE · KEEP YOUR DISTANCE", 9, FROST, ls="1.5")
            # wide witness ring in front, framing the statement
            + circle(180, 286, 92, None, FAAD, 3, 0.85)
            + circle(180, 286, 76, None, FAAD, 1.4, 0.45)
            + cap("05 / THE DENIAL", 7, FROST, ls="1.5", family="DM Mono"))


# ====================================================== 6. NO EVIDENCE, NO CASE
def c6_front():
    return (ground() + tee("#1c1c18") + neck()
            + text(180, 230, "ALL CLEAR", 7, CORY, ls="2", family="DM Mono")
            + text(180, 284, "NO EVIDENCE", 25, FROST, ls="3", family="DM Mono")   # legible stone instead of grey
            + rule(150, 316, 210, 316, CORY, 1.2, 0.85)
            + text(180, 334, "NO CASE", 40, WHITE, ls="1.5")
            + cap("06 / THE EXONERATION", 7, FROST, ls="1.5", family="DM Mono"))


def c6_back():
    return (ground() + tee("#1c1c18") + neck()
            + circle(180, 250, 120, None, CORY, 2, 0.85)
            + circle(180, 250, 108, None, CORY, 0.8, 0.4)
            + text(180, 224, "CASE FILE", 8, WHITE, ls="1.5", family="DM Mono")
            + text(180, 246, "NO EVIDENCE", 16, WHITE, ls="2")
            + text(180, 276, "NO CASE", 16, WHITE, ls="2")
            + text(180, 320, "✕", 18, CORY, ls="3")
            + text(180, 342, "DISMISSED", 7, CORY, ls="1.5", family="DM Mono")
            # proper garment tag (bottom right) with fold line instead of a floating rectangle
            + rect(262, 366, 22, 48, "#262621", CORY, 1, rx=2)
            + line(262, 382, 284, 382, CORY, 1)
            + text(273, 382, "RARE BY DESIGN", 5.5, FROST, ls="1", family="DM Mono")
            + cap("06/25", 7, FROST, ls="1.5", family="DM Mono"))


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

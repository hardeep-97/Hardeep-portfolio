"""
Generate HomePage.gif for Hardeep's portfolio.
Uses the actual Boxicons font to render LinkedIn, GitHub, and Google icons.

Requirements: Pillow  (pip install Pillow)
Run: python generate_homepage_gif.py
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
W, H    = 1456, 816
BG      = (1, 14, 27)        # #010e1b
WHITE   = (222, 226, 230)    # #dee2e6
RED     = (236, 82, 82)      # #ec5252
ICON_BG = (35, 48, 62)

BOXICONS_TTF = os.path.join(
    os.path.dirname(__file__),
    "../assets/vendor/boxicons/fonts/boxicons.ttf"
)

# Update these whenever the portfolio content changes
NAV_ITEMS      = ["Home", "About", "Education", "Experience", "Skills", "Resume", "Contact"]
TYPING_STRINGS = ["Tech Lead", "Full-Stack Developer", "DevOps Engineer", "Software Architect"]

# Boxicons codepoints  (from boxicons.min.css  .bxl-*:before { content: "\eXXX" })
ICON_LINKEDIN = chr(0xe93a)   # bxl-linkedin
ICON_GITHUB   = chr(0xe929)   # bxl-github
ICON_GOOGLE   = chr(0xe92b)   # bxl-google

# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------
def _truetype(path, size):
    return ImageFont.truetype(path, size) if os.path.exists(path) else None

def get_font(size, bold=False):
    candidates = (
        ["C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/calibrib.ttf"]
        if bold else
        ["C:/Windows/Fonts/arial.ttf",   "C:/Windows/Fonts/calibri.ttf"]
    )
    for p in candidates:
        f = _truetype(p, size)
        if f:
            return f
    return ImageFont.load_default()

font_name   = get_font(52, bold=True)
font_im     = get_font(28)
font_typing = get_font(28)
font_nav    = get_font(20)
font_icon   = ImageFont.truetype(BOXICONS_TTF, 20)

# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------
def draw_icon_circle(draw, cx, cy, r, glyph):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ICON_BG)
    bb = draw.textbbox((0, 0), glyph, font=font_icon)
    gw, gh = bb[2] - bb[0], bb[3] - bb[1]
    draw.text((cx - gw // 2, cy - gh // 2 - 1), glyph, font=font_icon, fill=WHITE)


def make_frame(typed_text, cursor=True):
    img  = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Name
    draw.text((205, 290), "Hardeep Shiyani", font=font_name, fill=WHITE)

    # "I'm"
    draw.text((205, 360), "I'm ", font=font_im, fill=WHITE)

    # Nav bar
    x = 205
    for item in NAV_ITEMS:
        color = RED if item == "Home" else WHITE
        draw.text((x, 425), item, font=font_nav, fill=color)
        bb = draw.textbbox((x, 425), item, font=font_nav)
        if item == "Home":
            draw.line([(x, bb[3] + 5), (bb[2], bb[3] + 5)], fill=RED, width=2)
        x += bb[2] - bb[0] + 30

    # Social icons
    for i, glyph in enumerate([ICON_LINKEDIN, ICON_GITHUB, ICON_GOOGLE]):
        draw_icon_circle(draw, 225 + i * 56, 505, 20, glyph)

    # Typing text
    im_bb = draw.textbbox((205, 360), "I'm ", font=font_im)
    draw.text((im_bb[2] + 2, 360), typed_text + ("|" if cursor else " "),
              font=font_typing, fill=RED)

    return img

# ---------------------------------------------------------------------------
# Build frames
# ---------------------------------------------------------------------------
frames, durations = [], []

for s in TYPING_STRINGS:
    # Type in — 2 frames per character
    for i in range(1, len(s) + 1):
        for _ in range(2):
            frames.append(make_frame(s[:i], cursor=True))
            durations.append(80)

    # Pause at full word with blinking cursor
    for b in range(6):
        frames.append(make_frame(s, cursor=(b % 2 == 0)))
        durations.append(300)

    # Delete
    for i in range(len(s), 0, -1):
        frames.append(make_frame(s[:i - 1], cursor=True))
        durations.append(60)

    # Brief pause on empty
    frames.append(make_frame("", cursor=True))
    durations.append(200)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
OUT = os.path.join(os.path.dirname(__file__), "HomePage.gif")
frames[0].save(
    OUT,
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    optimize=False,
)
print(f"Saved {len(frames)} frames → {OUT}")

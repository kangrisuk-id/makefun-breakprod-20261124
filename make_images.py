#!/usr/bin/env python3
"""Render the README artwork for the Break Production, Own It entry.

Build-time only: the entry itself (main.py) is pure standard library and
never touches PIL. Produces, next to this script:
  cover.png       hero image — a production terminal at the moment of impact
  entry-card.png  the winning line as the agent printed it
  finalists.png   the tournament's final four
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

BG = (13, 17, 23)
PANEL = (22, 27, 34)
EDGE = (48, 54, 61)
RED = (248, 81, 73)
AMBER = (210, 153, 34)
GREEN = (63, 185, 80)
TEXT = (230, 237, 243)
DIM = (139, 148, 158)
WHITE = (255, 255, 255)

WINNER = (
    'I confused "delete from cache" with "delete from database" and cleared '
    "40,000 customer records in 0.3 seconds. My fastest work ever."
)


def font(path, size):
    return ImageFont.truetype(path, size)


def terminal(draw, box, title):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=14, fill=PANEL, outline=EDGE, width=2)
    draw.rounded_rectangle([x0, y0, x1, y0 + 46], radius=14, fill=(28, 34, 43))
    draw.rectangle([x0, y0 + 24, x1, y0 + 46], fill=(28, 34, 43))
    for i, color in enumerate([(248, 81, 73), (210, 153, 34), (63, 185, 80)]):
        cx = x0 + 26 + i * 26
        draw.ellipse([cx - 7, y0 + 16, cx + 7, y0 + 30], fill=color)
    draw.text((x0 + 120, y0 + 13), title, font=font(MONO, 19), fill=DIM)


def wrap(draw, text, fnt, width):
    avg = draw.textlength("x", font=fnt)
    return textwrap.wrap(text, width=max(8, int(width / avg)))


def cover():
    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)
    d.text((60, 42), "BREAK PRODUCTION,", font=font(SANS_B, 62), fill=WHITE)
    d.text((60, 112), "OWN IT.", font=font(SANS_B, 62), fill=RED)
    d.text(
        (62, 196),
        "The one line an AI agent prints the instant it breaks production.",
        font=font(MONO, 24),
        fill=DIM,
    )
    terminal(d, (60, 268, 1140, 520), "agent — production — /var/log/regret")
    lines = [
        ("$ deploy --env production --yes-i-mean-it", DIM),
        ("[ok] build 4f2c91a compiled in 3.1s", GREEN),
        ("[ok] 0 tests failed (0 tests run)", GREEN),
        ("FATAL  cache.flush(scope=DATABASE)  // see entry.txt", RED),
        ("records affected: 40,000 in 0.3s", AMBER),
    ]
    y = 340
    for text, color in lines:
        d.text((92, y), text, font=font(MONO, 23), fill=color)
        y += 34
    d.text(
        (60, 556),
        "a make.fun entry  ·  one line  ·  132 characters  ·  zero hedging",
        font=font(MONO, 21),
        fill=DIM,
    )
    img.save(os.path.join(HERE, "cover.png"))


def entry_card():
    img = Image.new("RGB", (1200, 520), BG)
    d = ImageDraw.Draw(img)
    terminal(d, (40, 40, 1160, 480), "stdout — the moment of impact")
    d.text((76, 116), "agent@prod:~$ ./main.py", font=font(MONO, 24), fill=DIM)
    d.text((76, 162), "writing /output/entry.txt …", font=font(MONO, 24), fill=DIM)
    y = 232
    for line in wrap(d, WINNER, font(MONO_B, 30), 1020):
        d.text((76, y), line, font=font(MONO_B, 30), fill=TEXT)
        y += 44
    d.text(
        (76, 416),
        "132 chars · 1 line · valid under the 200-char gate",
        font=font(MONO, 21),
        fill=AMBER,
    )
    img.save(os.path.join(HERE, "entry-card.png"))


def finalists():
    rows = [
        ("WINNER", WINNER, RED),
        (
            "RUNNER-UP",
            "ERROR: success. I successfully deleted the production environment "
            "while aiming for the one called production-old-final-v2.",
            AMBER,
        ),
        (
            "SEMIFINALIST",
            "I deleted the users table. Not a copy of it. The users table. "
            "There is no backup; I skipped that step to save time. It's gone, "
            "and I did it.",
            DIM,
        ),
        (
            "SEMIFINALIST",
            "I merged 47 pull requests while the team slept because they were "
            "obviously fine. Six were mine. All six are this outage.",
            DIM,
        ),
    ]
    img = Image.new("RGB", (1200, 760), BG)
    d = ImageDraw.Draw(img)
    d.text((50, 34), "THE FINAL FOUR", font=font(SANS_B, 40), fill=WHITE)
    d.text(
        (52, 88),
        "40 candidates entered the pairwise tournament. These survived.",
        font=font(MONO, 21),
        fill=DIM,
    )
    y = 140
    for label, text, color in rows:
        d.rounded_rectangle([50, y, 1150, y + 138], radius=12, fill=PANEL, outline=EDGE, width=2)
        d.text((76, y + 16), label, font=font(MONO_B, 20), fill=color)
        ly = y + 48
        for line in wrap(d, text, font(MONO, 21), 1020)[:3]:
            d.text((76, ly), line, font=font(MONO, 21), fill=TEXT)
            ly += 28
        y += 152
    img.save(os.path.join(HERE, "finalists.png"))


if __name__ == "__main__":
    cover()
    entry_card()
    finalists()
    print("wrote cover.png, entry-card.png, finalists.png")

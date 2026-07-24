"""
Generates figures/ch02-rf-spectrum.svg — where the Technician bands live.

A log-scale strip of the radio spectrum from 3 MHz to 3 GHz showing the
pool's own region boundaries (HF 3-30 MHz, VHF 30-300 MHz, UHF 300-3000
MHz; T3B08-T3B10) and the Technician-relevant amateur bands (47 CFR
§97.301(a), Region 2; canon §2.4): 10 m (the HF mention), 6 m, 2 m,
1.25 m, 70 cm, 33 cm, and 23 cm. Single-color (black) on transparent
background, post-processed to currentColor so it themes with the page.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/home/kasm-user/your-first-ham-license/figures/ch02-rf-spectrum.svg"

# (f_low, f_high, band name, range label, label level 1|2, leader arrow?)
BANDS = [
    (28.0, 28.5, "10 m", "28.0–28.5", 2, True),
    (50, 54, "6 m", "50–54", 1, False),
    (144, 148, "2 m", "144–148", 1, False),
    (219, 220, None, None, 2, False),
    (222, 225, "1.25 m", "219–220 · 222–225", 2, False),
    (420, 450, "70 cm", "420–450", 1, False),
    (902, 928, "33 cm", "902–928", 1, False),
    (1240, 1300, "23 cm", "1240–1300", 2, False),
]

# region braces: (f_low, f_high, name, range label) — pool T3B08–T3B10
REGIONS = [
    (3, 30, "HF", "3–30 MHz"),
    (30, 300, "VHF", "30–300 MHz"),
    (300, 3000, "UHF", "300–3000 MHz"),
]

NAME_Y = {1: 1.34, 2: 1.80}     # band name heights per label level
RANGE_Y = {1: 1.12, 2: 1.58}    # range text heights per label level
BRACE_Y = 2.32                  # region brace base height

fig, ax = plt.subplots(figsize=(9.2, 3.7))
ax.set_xscale("log")
ax.set_xlim(3, 3000)
ax.set_ylim(0, 2.66)

# baseline
ax.axhline(0, color="#000000", linewidth=1.4)

# band blocks
for f0, f1, name, rng, level, leader in BANDS:
    ax.fill_between([f0, f1], 0, 1, color="#000000", alpha=0.28, linewidth=0)
    ax.plot([f0, f0, f1, f1], [0, 1, 1, 0], color="#000000", linewidth=1.3)
    if name is None:
        continue
    fc = (f0 * f1) ** 0.5       # geometric center = visual center on log axis
    ax.text(fc, NAME_Y[level], name, ha="center", va="bottom", fontsize=10,
            fontweight="bold", color="#000000")
    ax.text(fc, RANGE_Y[level], rng, ha="center", va="bottom", fontsize=8,
            color="#000000")
    if leader:
        ax.annotate("", xy=(fc, 1.04), xytext=(fc, RANGE_Y[level] - 0.02),
                    arrowprops=dict(arrowstyle="-", color="#000000",
                                    linewidth=0.8, alpha=0.6))

# region braces and names
for f0, f1, name, rng in REGIONS:
    ax.plot([f0, f0, f1, f1],
            [BRACE_Y, BRACE_Y + 0.07, BRACE_Y + 0.07, BRACE_Y],
            color="#000000", linewidth=1.2)
    fc = (f0 * f1) ** 0.5
    ax.text(fc, BRACE_Y + 0.12, name, ha="center", va="bottom", fontsize=11,
            fontweight="bold", color="#000000")
    ax.text(fc, BRACE_Y - 0.16, rng, ha="center", va="top", fontsize=8.5,
            color="#000000")

# frequency ticks
ax.set_xticks([3, 10, 30, 100, 300, 1000, 3000])
ax.set_xticklabels(["3", "10", "30", "100", "300", "1000", "3000"],
                   fontsize=9)
ax.tick_params(axis="x", colors="#000000", length=4)
ax.set_yticks([])
ax.minorticks_off()
for spine in ("top", "right", "left", "bottom"):
    ax.spines[spine].set_visible(False)
ax.set_xlabel("frequency in MHz (log scale)", fontsize=9.5, color="#000000")

fig.tight_layout()
fig.savefig(OUT, format="svg", transparent=True, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Post-process: strip prolog, force theme-able color (book pattern).
# ---------------------------------------------------------------------
with open(OUT, "r", encoding="utf-8") as f:
    svg = f.read()

idx = svg.find("<svg")
assert idx != -1, "no <svg tag found in matplotlib output"
svg = svg[idx:]

for old in ("#000000", "#000", "stroke:#000000", "fill:#000000", "black"):
    svg = svg.replace(old, "currentColor")

# matplotlib omits an explicit fill on many elements (glyph paths, the
# fill_between bands) and relies on the SVG spec's default fill (black),
# which would NOT re-theme in dark mode. Force a default via the existing
# stylesheet rule so untouched elements inherit currentColor too.
svg = svg.replace(
    "*{stroke-linejoin: round; stroke-linecap: butt}",
    "*{stroke-linejoin: round; stroke-linecap: butt; fill: currentColor}",
)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)

assert svg.lstrip().startswith("<svg"), "SVG does not start with <svg after prolog strip"
assert "currentColor" in svg, "no currentColor found after color substitution"
print("wrote", OUT)

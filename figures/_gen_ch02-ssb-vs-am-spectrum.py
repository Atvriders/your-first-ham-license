"""
Generates figures/ch02-ssb-vs-am-spectrum.svg — occupied spectrum, AM vs SSB.

Beginner version of the classic comparison, using the pool's own values
(T8A08: SSB voice occupies about 3 kHz): a voice signal up to 3 kHz makes
an AM signal with a carrier plus TWO sidebands (~6 kHz occupied), while
SSB keeps only ONE sideband and suppresses the carrier (~3 kHz occupied) —
half the spectrum for the same voice. Single-color (black) on transparent
background, post-processed to currentColor so it themes with the page.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/home/kasm-user/your-first-ham-license/figures/ch02-ssb-vs-am-spectrum.svg"

LO, HI = 0.3, 3.0      # voice band, kHz (SSB voice ~ 3 kHz, pool T8A08)
XLIM = (-4.8, 4.8)
YLIM = (-0.72, 1.62)   # room below the axis for ticks + width bracket
BAND_H = 0.55          # sideband block height

fig, (axL, axR) = plt.subplots(1, 2, figsize=(9.0, 4.3), sharey=True)

for ax in (axL, axR):
    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.axhline(0, color="#000000", linewidth=1.2)
    ax.set_yticks([])
    ax.set_xticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    # manual tick marks + labels just below the frequency axis
    for xv, lab in ((-3, "−3 kHz"), (0, "$f_c$"), (3, "+3 kHz")):
        ax.plot([xv, xv], [0, -0.05], color="#000000", linewidth=1.0)
        ax.text(xv, -0.08, lab, ha="center", va="top", fontsize=9,
                color="#000000")


def sideband(ax, x0, x1):
    ax.fill_between([x0, x1], 0, BAND_H, color="#000000", alpha=0.30,
                    linewidth=0)
    ax.plot([x0, x0, x1, x1], [0, BAND_H, BAND_H, 0], color="#000000",
            linewidth=1.3)


def width_bracket(ax, x0, x1, label):
    yb = -0.34
    ax.annotate("", xy=(x1, yb), xytext=(x0, yb),
                arrowprops=dict(arrowstyle="<->", color="#000000",
                                linewidth=1.1))
    ax.text((x0 + x1) / 2, yb - 0.09, label, ha="center", va="top",
            fontsize=9.5, color="#000000")


# ---------------- left: AM ----------------
axL.set_title("AM — carrier + two sidebands", fontsize=11, color="#000000")

sideband(axL, -HI, -LO)
sideband(axL, LO, HI)
axL.plot([0, 0], [0, 1.25], color="#000000", linewidth=2.4)
axL.text(0, 1.32, "carrier", ha="center", va="bottom", fontsize=9,
         color="#000000")
axL.text(-(LO + HI) / 2, 0.62, "LSB", ha="center", va="bottom", fontsize=9,
         color="#000000")
axL.text((LO + HI) / 2, 0.62, "USB", ha="center", va="bottom", fontsize=9,
         color="#000000")
width_bracket(axL, -HI, HI, "about 6 kHz wide")

# ---------------- right: SSB ----------------
axR.set_title("SSB — one sideband, carrier suppressed", fontsize=11,
              color="#000000")

sideband(axR, LO, HI)
axR.text((LO + HI) / 2, 0.62, "USB", ha="center", va="bottom", fontsize=9,
         color="#000000")

# suppressed carrier: dashed ghost spike
axR.plot([0, 0], [0, 1.25], color="#000000", linewidth=1.8,
         linestyle=(0, (2, 2)), alpha=0.45)
axR.text(0, 1.32, "carrier\nsuppressed", ha="center", va="bottom",
         fontsize=8, color="#000000", alpha=0.75)
width_bracket(axR, LO, HI, "about 3 kHz wide")

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

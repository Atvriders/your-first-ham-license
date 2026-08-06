"""Generate figures/ch08-tech-band-chart.svg — Technician privileges at a glance.

All band edges come from canon §2.4 (pinned values only):
- HF segments (200 W PEP max, §97.313(c)(2)): 80 m 3.525-3.600, 40 m
  7.025-7.125, 15 m 21.025-21.200, 10 m 28.0-28.5 MHz; CW-only on 80/40/15 m
  (§97.307(f)(9)); 10 m split: 28.0-28.3 CW/data, 28.300-28.500 SSB phone + CW
  (§97.305(c)(3)(xviii), §97.307(f)(10)).
- VHF/UHF, same privileges as every license class (§97.301(a), ITU Region 2):
  6 m 50-54, 2 m 144-148, 1.25 m 219-220 + 222-225, 70 cm 420-450 MHz;
  CW-only bottoms 50.0-50.1 and 144.0-144.1 MHz (§97.305). 33 cm and 23 cm
  are shown by band name only — the canon pins no edges for them, so none
  are drawn.

Each row is its own bar with explicit numeric labels (rows are not on a
shared frequency axis). Hatched bar = CW only; open bar = all modes.
Single-color (black) matplotlib output on a transparent background, then
post-processed: every #000000 becomes currentColor so the SVG themes with
the book's text color (established pattern for this book's _gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

W, H = 100.0, 112.0          # figure coordinate canvas
BX0, BX1 = 19.0, 96.0        # bar region
BAR_H = 3.6

fig = plt.figure(figsize=(7.8, 8.6))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")

INK = "black"


def bar(x0, x1, y, cw=False, dashed=False):
    if cw:
        ax.add_patch(Rectangle((x0, y - BAR_H / 2), x1 - x0, BAR_H,
                               fill=False, edgecolor=INK, hatch="////",
                               linewidth=1.2))
    elif dashed:
        ax.add_patch(Rectangle((x0, y - BAR_H / 2), x1 - x0, BAR_H,
                               fill=False, edgecolor=INK, linewidth=1.2,
                               linestyle=(0, (4, 3))))
    else:
        ax.add_patch(Rectangle((x0, y - BAR_H / 2), x1 - x0, BAR_H,
                               fill=False, edgecolor=INK, linewidth=1.6))


def row(y, name, freq, mode, mode_x=None, note=None, dashed=False):
    ax.text(1.5, y, name, fontsize=12, fontweight="bold",
            ha="left", va="center", color=INK)
    if freq:
        ax.text(1.5, y - 3.4, freq, fontsize=7.8, ha="left", va="center",
                color=INK)
    bar(BX0, BX1, y, dashed=dashed)
    ax.text(mode_x if mode_x is not None else (BX0 + BX1) / 2, y + 2.9,
            mode, fontsize=8.5, ha="center", va="center", color=INK)
    if note:
        ax.text(BX1, y - 3.4, note, fontsize=7.5, ha="right", va="center",
                style="italic", color=INK)


# ---- title ---------------------------------------------------------------
ax.text(50, 108, "TECHNICIAN PRIVILEGES AT A GLANCE", fontsize=15,
        fontweight="bold", ha="center", va="center", color=INK)
ax.text(50, 104.6, "limited HF slices + full VHF/UHF — per FCC rules "
        "§97.301 / §97.305", fontsize=9, ha="center", va="center", color=INK)

# ---- HF section ----------------------------------------------------------
ax.text(1.5, 99.5, "HF SEGMENTS — 200 W PEP maximum", fontsize=11,
        fontweight="bold", ha="left", va="center", color=INK)

for y, name, freq in ((93.5, "80 m", "3.525–3.600 MHz"),
                      (85.5, "40 m", "7.025–7.125 MHz"),
                      (77.5, "15 m", "21.025–21.200 MHz")):
    ax.text(1.5, y, name, fontsize=12, fontweight="bold", ha="left",
            va="center", color=INK)
    ax.text(1.5, y - 3.4, freq, fontsize=7.8, ha="left", va="center",
            color=INK)
    bar(BX0, BX1, y, cw=True)
    ax.text((BX0 + BX1) / 2, y + 2.9, "CW only (Morse code)", fontsize=8.5,
            ha="center", va="center", color=INK)

# 10 m: split bar 28.0-28.3 CW/data, 28.3-28.5 SSB phone + CW
y10 = 68.0
SPLIT = BX0 + (BX1 - BX0) * 0.58
ax.text(1.5, y10, "10 m", fontsize=12, fontweight="bold", ha="left",
        va="center", color=INK)
ax.text(1.5, y10 - 3.4, "28.0–28.5 MHz", fontsize=7.8, ha="left",
        va="center", color=INK)
bar(BX0, SPLIT, y10, cw=True)
bar(SPLIT, BX1, y10)
ax.plot([SPLIT, SPLIT], [y10 - BAR_H / 2, y10 + BAR_H / 2], color=INK,
        linewidth=1.6)
ax.text((BX0 + SPLIT) / 2, y10 + 2.9, "CW + data", fontsize=8.5,
        ha="center", va="center", color=INK)
ax.text((SPLIT + BX1) / 2, y10 + 2.9, "SSB phone + CW", fontsize=8.5,
        ha="center", va="center", color=INK)
for x, lab in ((BX0, "28.0"), (SPLIT, "28.3"), (BX1, "28.5 MHz")):
    ax.text(x, y10 - 3.1, lab, fontsize=7.5,
            ha=("left" if x == BX0 else "right" if x == BX1 else "center"),
            va="center", color=INK)

# ---- VHF/UHF section -----------------------------------------------------
ax.text(1.5, 60.0, "VHF / UHF — FULL PRIVILEGES, same as every license class",
        fontsize=11, fontweight="bold", ha="left", va="center", color=INK)
ax.text(1.5, 56.8, "1500 W PEP general ceiling — some specific restrictions "
        "apply", fontsize=8.5, ha="left", va="center", style="italic",
        color=INK)

row(51.0, "6 m", "50–54 MHz", "all modes — phone, CW, data, FM",
    note="bottom 50.0–50.1 MHz is CW only")
row(41.5, "2 m", "144–148 MHz", "all modes — phone, CW, data, FM",
    note="bottom 144.0–144.1 MHz is CW only")

# 1.25 m: two segments, drawn in proportion to their widths (1 vs 3 MHz)
y125 = 32.0
GAP = 2.0
w1 = (BX1 - BX0 - GAP) * 1.0 / 4.0
ax.text(1.5, y125, "1.25 m", fontsize=12, fontweight="bold", ha="left",
        va="center", color=INK)
ax.text(1.5, y125 - 3.4, "two segments", fontsize=7.8, ha="left",
        va="center", color=INK)
bar(BX0, BX0 + w1, y125)
bar(BX0 + w1 + GAP, BX1, y125)
ax.text((BX0 + BX1) / 2, y125 + 2.9, "all modes", fontsize=8.5,
        ha="center", va="center", color=INK)
ax.text(BX0 + w1 / 2, y125 - 3.1, "219–220", fontsize=7.5, ha="center",
        va="center", color=INK)
ax.text((BX0 + w1 + GAP + BX1) / 2, y125 - 3.1, "222–225 MHz", fontsize=7.5,
        ha="center", va="center", color=INK)

row(22.5, "70 cm", "420–450 MHz", "all modes")
row(14.0, "33 cm", "", "all modes", dashed=True)
row(5.5, "23 cm", "", "all modes", dashed=True)

# ---- legend ---------------------------------------------------------------
ly = 1.2
ax.add_patch(Rectangle((19, ly - 1.1), 4.2, 2.4, fill=False, edgecolor=INK,
                       hatch="////", linewidth=1.0))
ax.text(24.3, ly, "CW only", fontsize=8, ha="left", va="center", color=INK)
ax.add_patch(Rectangle((38, ly - 1.1), 4.2, 2.4, fill=False, edgecolor=INK,
                       linewidth=1.4))
ax.text(43.3, ly, "all modes", fontsize=8, ha="left", va="center", color=INK)
ax.add_patch(Rectangle((57, ly - 1.1), 4.2, 2.4, fill=False, edgecolor=INK,
                       linewidth=1.1, linestyle=(0, (4, 3))))
ax.text(62.3, ly, "33 cm / 23 cm + more bands — same privileges",
        fontsize=8, ha="left", va="center", color=INK)

out = "figures/ch08-tech-band-chart.svg"
fig.savefig(out, transparent=True, bbox_inches="tight", pad_inches=0.05)

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)

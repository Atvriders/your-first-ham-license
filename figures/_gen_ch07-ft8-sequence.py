"""
Generates figures/ch07-ft8-sequence.svg — FT8's timed 15-second cycle.

Two swimlanes (you and the other station) over 90 seconds: each station
transmits in alternate 15-second slots and listens in between, so a whole
scripted QSO (call signs, report, 73) fits in about a minute. Every
computer's clock is synchronized to internet time, which is how all the
slots line up — and FT8 decodes signals below audibility (pool T8D02:
"15-second sequences," "very low signal-to-noise operation").

Single color (black) on transparent background, post-processed to
currentColor so the figure themes with the page (book pattern: strip the
prolog, swap black -> currentColor, force a default fill).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = "/home/kasm-user/your-first-ham-license/figures/ch07-ft8-sequence.svg"

SLOT = 15.0          # seconds per FT8 transmit/receive slot (pool T8D02)
N = 6                # show six slots = 90 seconds
T_END = SLOT * N

# ---------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.2, 4.2))

LANES = [("You (station A)", 1.0), ("The other station (B)", 0.0)]
H = 0.52             # block height

for name, y0 in LANES:
    for k in range(N):
        x = k * SLOT
        # A transmits on even slots, B on odd slots
        tx = (k % 2 == 0) if y0 > 0.5 else (k % 2 == 1)
        if tx:
            ax.add_patch(Rectangle((x, y0), SLOT, H,
                                   facecolor="#000000", edgecolor="#000000",
                                   linewidth=1.0))
        else:
            ax.add_patch(Rectangle((x, y0), SLOT, H,
                                   facecolor="none", edgecolor="#000000",
                                   linewidth=1.0, linestyle=(0, (3, 2)),
                                   alpha=0.65))

# slot-boundary guide lines + labels
for k in range(N + 1):
    x = k * SLOT
    ax.axvline(x, color="#000000", linewidth=0.6, alpha=0.22, zorder=0)

# lane names
ax.text(-1.6, 1.0 + H / 2, "You\n(station A)", ha="right", va="center",
        fontsize=10.5, color="#000000")
ax.text(-1.6, 0.0 + H / 2, "The other\nstation (B)", ha="right", va="center",
        fontsize=10.5, color="#000000")

# TX / RX key: label the first block of each kind, consistently above
# your lane and below the other station's lane
ax.text(SLOT / 2, 1.0 + H + 0.10, "TX (15 s)", ha="center",
        va="bottom", fontsize=9.5, color="#000000", fontweight="bold")
ax.text(1.5 * SLOT, 1.0 + H + 0.10, "RX", ha="center",
        va="bottom", fontsize=9.5, color="#000000")
ax.text(SLOT / 2, -0.14, "RX", ha="center", va="top",
        fontsize=9.5, color="#000000")
ax.text(1.5 * SLOT, -0.14, "TX (15 s)", ha="center", va="top",
        fontsize=9.5, color="#000000", fontweight="bold")

# one message-flow arrow: your CQ slot -> their answer slot
ax.add_patch(FancyArrowPatch((SLOT - 1.5, 1.0 + H / 2), (SLOT + 1.5, 0.0 + H / 2),
                             arrowstyle="-|>", mutation_scale=13,
                             color="#000000", linewidth=1.2, zorder=5))

# example scripted exchange, placed in empty space right of center
ax.text(3.5 * SLOT, 1.0 + H + 0.16, "a whole contact is a scripted minute:",
        ha="center", va="bottom", fontsize=9.5, color="#000000",
        fontstyle="italic")
ax.text(3.5 * SLOT, 0.0 + H + 0.16, "“CQ K1ABC FN31” → “K1ABC W9XYZ –12” → “73!”",
        ha="center", va="bottom", fontsize=9.5, color="#000000",
        fontstyle="italic")

# ---------------------------------------------------------------------
# Axes, title, footnotes
# ---------------------------------------------------------------------
ax.set_xlim(-0.4, T_END + 0.4)
ax.set_ylim(-0.62, 2.28)
ax.set_xticks([k * SLOT for k in range(N + 1)])
ax.set_xticklabels([str(k * int(SLOT)) for k in range(N + 1)],
                   fontsize=9, color="#000000")
ax.set_yticks([])
ax.set_xlabel("time (seconds) — every slot starts exactly on the quarter minute",
              fontsize=10, color="#000000")
ax.set_title("FT8: two stations take turns in 15-second slots",
             fontsize=13, color="#000000", pad=10)

for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color("#000000")
ax.tick_params(axis="x", colors="#000000")

fig.text(0.5, 0.015,
         "Solid = transmitting, dashed = listening. Every computer's clock is synced to internet time, so the slots line up —\n"
         "and FT8 decodes signals below the noise, contacts you could never hear by ear.",
         ha="center", va="bottom", fontsize=9.3, color="#000000",
         fontstyle="italic")

fig.tight_layout(rect=(0.0, 0.075, 1.0, 1.0))
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

# matplotlib omits an explicit fill on many elements (glyph paths, fills)
# and relies on the SVG spec's default fill (black), which would NOT
# re-theme in dark mode. Force a default so untouched elements inherit
# currentColor too.
svg = svg.replace(
    "*{stroke-linejoin: round; stroke-linecap: butt}",
    "*{stroke-linejoin: round; stroke-linecap: butt; fill: currentColor}",
)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)

assert svg.lstrip().startswith("<svg"), "SVG does not start with <svg after prolog strip"
assert "currentColor" in svg, "no currentColor found after color substitution"
print("wrote", OUT)

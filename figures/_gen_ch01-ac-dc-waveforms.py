"""Generate figures/ch01-ac-dc-waveforms.svg — DC flat line vs AC sine wave.

Pool-level teaching panel for T5A: DC flows in one direction only and is
steady; AC alternates between positive and negative directions (T5A09);
frequency is the number of complete cycles per second, unit hertz (T5A04,
T5A06); f = 1 / T (canon section 3).

Single-color (black) matplotlib output on a transparent background, then
post-processed here: every #000000 becomes currentColor so the SVG themes
with the book's text color (established pattern for this book's _gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2, 1000)  # two cycles of unit period

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 4.9), sharex=True)

# ---- DC panel: a steady flat line (battery) ----
ax1.axhline(0, color="black", linewidth=0.8, linestyle=":", alpha=0.6)
ax1.plot(t, np.ones_like(t), color="black", linewidth=2.4, solid_capstyle="round")
ax1.set_ylim(-1.8, 2.1)
ax1.set_yticks([-1, 0, 1])
ax1.set_yticklabels(["\u2212", "0", "+"])
ax1.set_ylabel("voltage", fontsize=10, color="black")
ax1.text(0.99, 0.80,
         "DC \u2014 direct current: flows in one direction only, steady (a battery)",
         transform=ax1.transAxes, fontsize=10, color="black",
         ha="right", va="bottom")

# ---- AC panel: a sine wave ----
ax2.axhline(0, color="black", linewidth=0.8, linestyle=":", alpha=0.6)
ax2.plot(t, np.sin(2 * np.pi * t), color="black", linewidth=2.4,
         solid_capstyle="round")
ax2.set_ylim(-2.0, 2.3)
ax2.set_yticks([-1, 0, 1])
ax2.set_yticklabels(["\u2212", "0", "+"])
ax2.set_ylabel("voltage", fontsize=10, color="black")
ax2.set_xlabel("time  \u2192", fontsize=10, color="black")
ax2.set_xticks([])

# mark one cycle, crest to crest (period T)
for x in (0.25, 1.25):
    ax2.plot([x, x], [1.0, 1.46], color="black", linewidth=0.9, linestyle=":")
ax2.annotate("", xy=(1.25, 1.38), xytext=(0.25, 1.38),
             arrowprops=dict(arrowstyle="<->", color="black", lw=1.4))
ax2.text(0.75, 1.52, "one cycle \u2014 the time it takes is the period T",
         ha="center", fontsize=10, color="black")

ax2.text(0.5, 0.04,
         "AC \u2014 alternating current: alternates between positive and negative directions",
         transform=ax2.transAxes, fontsize=10, color="black",
         ha="center", va="bottom")

ax2.text(0.5, -0.24,
         "frequency f = number of complete cycles per second \u2014 unit: hertz (Hz)\nf = 1 / T",
         transform=ax2.transAxes, fontsize=10, color="black",
         ha="center", va="top")

for ax in (ax1, ax2):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("black")
    ax.tick_params(colors="black", labelsize=9.5)

fig.tight_layout()

out = "figures/ch01-ac-dc-waveforms.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)

"""Generate figures/ch04-swr-curve.svg — SWR versus frequency for an antenna
cut for 146 MHz, dipping to 1:1 at resonance and rising toward the band edges.

The exam points (canon section 2.6): SWR measures how well a load is matched
to a transmission line (T9B12); 1:1 is a perfect antenna/feed-line match,
4:1 a mismatch (T7C04, T7C06); and high SWR makes a solid-state transceiver
reduce output power to protect its RF output transistors (T7B04, T7C05).
The x-axis is the real 2-meter band, 144–148 MHz (canon section 2.4).

Single-color (black) matplotlib output on a transparent background, then
post-processed here: every #000000 becomes currentColor so the SVG themes
with the book's text color (established pattern from Book 1's _gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

f = np.linspace(144, 148, 600)  # the 2-meter band, MHz
f0 = 146.0                      # antenna cut for the middle of the band
swr = 1.0 + 0.55 * (f - f0) ** 2  # concept curve: 1:1 at resonance, ~3:1 at the edges

fig, ax = plt.subplots(figsize=(6.4, 4.6))

ax.plot(f, swr, color="black", linewidth=2.4, solid_capstyle="round")

# mark the resonant point
ax.plot([f0], [1.0], marker="o", markersize=7, color="black")
ax.annotate("resonance: SWR \u2248 1:1 —\na perfect match",
            xy=(f0, 1.0), xytext=(146.9, 1.45),
            ha="center", fontsize=10.5, color="black",
            arrowprops=dict(arrowstyle="->", color="black", lw=1.1))

# and the high ends
ax.annotate("off resonance, power reflects\nback toward the radio",
            xy=(144.25, 1.0 + 0.55 * (0.25) ** 2 + 0.28), xytext=(144.75, 2.35),
            ha="center", fontsize=10.5, color="black",
            arrowprops=dict(arrowstyle="->", color="black", lw=1.1))

ax.set_xlim(144, 148)
ax.set_ylim(0.7, 4.3)
ax.set_xticks([144, 145, 146, 147, 148])
ax.set_xlabel("frequency (MHz) — the 2-meter band, 144–148 MHz",
              fontsize=10, color="black")
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(["1:1", "2:1", "3:1", "4:1"])
ax.set_ylabel("SWR", fontsize=10, color="black")
ax.set_title("SWR Is Lowest at the Antenna's Resonant Frequency",
             fontsize=13, color="black")

ax.text(0.5, -0.30,
        "Why low SWR matters: high SWR makes a solid-state transceiver cut its power\n"
        "to protect itself — low SWR means your power reaches the antenna.",
        transform=ax.transAxes, fontsize=10.5, color="black",
        ha="center", va="top")

for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color("black")
ax.tick_params(colors="black", labelsize=9.5)
ax.grid(axis="y", color="black", alpha=0.15, linewidth=0.7)

fig.tight_layout()

out = "figures/ch04-swr-curve.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)

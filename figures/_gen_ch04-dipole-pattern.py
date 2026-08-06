"""Generate figures/ch04-dipole-pattern.svg — polar radiation pattern of a
half-wave dipole, seen from above (wire running left-right through the middle).

The exam points (canon section 2.6, T9A): a half-wave dipole radiates strongest
broadside — out from its sides — and weakest off its ends (T9A10), and antenna
"gain" is that focusing in a specified direction, not extra power (T9A11).

Single-color (black) matplotlib output on a transparent background, then
post-processed here: every #000000 becomes currentColor so the SVG themes
with the book's text color (established pattern for this book's _gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

deg = np.linspace(0, 360, 2000)
th = np.radians(deg)  # angle measured from the wire axis

# half-wave dipole pattern (relative field strength); angle from the wire axis,
# symmetric top/bottom — |sin| in the denominator keeps both lobes
pat = np.abs(np.cos((np.pi / 2) * np.cos(th))
             / np.maximum(np.abs(np.sin(th)), 1e-9))
pat /= pat.max()

fig = plt.figure(figsize=(6.8, 6.0))
ax = fig.add_subplot(111, projection="polar")
ax.set_theta_zero_location("E")  # 0 deg to the right: the wire runs left-right
ax.set_theta_direction(1)

ax.plot(th, pat, color="black", linewidth=2.4)
ax.fill(th, pat, color="black", alpha=0.10)

# the dipole itself, drawn through the middle (seen from above), with a
# small gap at the center feedpoint
ax.plot([0, 0], [0.07, 0.60], color="black", linewidth=5,
        solid_capstyle="round")
ax.plot([np.pi, np.pi], [0.07, 0.60], color="black", linewidth=5,
        solid_capstyle="round")
ax.annotate("the dipole", xy=(0, 0.42), xytext=(-0.5, 0.66),
            ha="center", va="center", fontsize=10.5, color="black",
            arrowprops=dict(arrowstyle="-", color="black", lw=0.9))

# meaning labels: broadside pair in the ring inside the axes, null pair
# (wider) just outside the circle where nothing else sits
lbl = "strongest broadside (out from the sides)"
ax.text(np.pi / 2, 1.17, lbl, ha="center", va="center", fontsize=10.5,
        color="black")
ax.text(3 * np.pi / 2, 1.17, lbl, ha="center", va="center", fontsize=10.5,
        color="black")
lbl = "null — almost nothing\noff the ends"
ax.text(0, 1.66, lbl, ha="center", va="center", fontsize=10.5, color="black")
ax.text(np.pi, 1.66, lbl, ha="center", va="center", fontsize=10.5,
        color="black")

# quiet, label-free grid: the shape carries the lesson, not numbers
ax.set_rticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels([])
ax.set_xticks([])
ax.tick_params(colors="black")
ax.grid(color="black", alpha=0.25, linewidth=0.8)
ax.spines["polar"].set_color("black")
ax.set_rmax(1.35)

ax.set_title("The Half-Wave Dipole, Seen From Above: Where the Signal Goes",
             color="black", fontsize=12.5, pad=16)

fig.text(0.5, 0.015,
         "The same transmitter power, focused — stronger to the sides, almost nothing off the ends.\n"
         "That focusing is all antenna \u201cgain\u201d means: concentration in a direction, not amplification.",
         ha="center", va="bottom", fontsize=10, color="black")

out = "figures/ch04-dipole-pattern.svg"
fig.savefig(out, transparent=True, bbox_inches="tight", pad_inches=0.12)

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)

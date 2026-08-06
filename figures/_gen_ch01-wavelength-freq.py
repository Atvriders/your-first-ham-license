"""Generate figures/ch01-wavelength-freq.svg — a sine wave with one wavelength marked.

The pool's own shortcut (T3B06, canon section 3): wavelength in meters equals
300 divided by frequency in megahertz, presented as an approximation of
c = f * lambda with c ~= 3e8 m/s. Worked example is the pool's drill value:
300 / 146 ~= 2 m (the 2-meter band).

Single-color (black) matplotlib output on a transparent background, then
post-processed here: every #000000 becomes currentColor so the SVG themes
with the book's text color (established pattern for this book's _gen_*.py).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

lam = 300.0 / 146.0  # meters per cycle at 146 MHz (~2.05 m)

x = np.linspace(0, 2.2 * lam, 1000)  # distance along the wave's path
y = np.sin(2 * np.pi * x / lam)

fig, ax = plt.subplots(figsize=(6.4, 4.4))

ax.axhline(0, color="black", linewidth=0.8, linestyle=":", alpha=0.6)
ax.plot(x, y, color="black", linewidth=2.4, solid_capstyle="round")

# mark one wavelength, crest to crest
p1, p2 = 0.25 * lam, 1.25 * lam
for px in (p1, p2):
    ax.plot([px, px], [1.0, 1.48], color="black", linewidth=0.9, linestyle=":")
ax.annotate("", xy=(p2, 1.38), xytext=(p1, 1.38),
            arrowprops=dict(arrowstyle="<->", color="black", lw=1.4))
ax.text((p1 + p2) / 2, 1.56, "one wavelength  \u03bb",
        ha="center", fontsize=11, color="black")

ax.set_xlim(0, 2.2 * lam)
ax.set_ylim(-1.6, 1.9)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xlabel("distance along the wave's path  (m)", fontsize=10, color="black")
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels(["\u2212", "0", "+"])
ax.set_ylabel("field strength", fontsize=10, color="black")
ax.set_title(r"$\lambda\ (\mathrm{m}) = 300 \,/\, f\ (\mathrm{MHz})$",
             fontsize=13, color="black")

ax.text(0.5, -0.42,
        "Example: f = 146 MHz  \u2192  \u03bb = 300 / 146 \u2248 2 m \u2014 the 2-meter band\n"
        "(the 300 comes from the wave's speed, \u2248 3\u00d710\u2078 m/s; higher frequency means shorter wavelength)",
        transform=ax.transAxes, fontsize=10, color="black",
        ha="center", va="top")

for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color("black")
ax.tick_params(colors="black", labelsize=9.5)

fig.tight_layout()

out = "figures/ch01-wavelength-freq.svg"
fig.savefig(out, transparent=True, bbox_inches="tight")

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)

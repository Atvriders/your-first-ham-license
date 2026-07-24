"""
Generates figures/ch07-doppler-curve.svg — Doppler shift across a LEO
satellite pass.

Physics (pool T8B07: Doppler shift = the observed change in signal
frequency caused by relative motion between the satellite and the Earth
station): while the satellite rises and comes toward you the received
frequency is high; it sweeps down through the published (nominal)
frequency at closest approach and ends low as the satellite sets. On
VHF the swing is only a few kHz (on UHF downlinks it is roughly ±10 kHz),
which is why you keep nudging your tuning during a pass — tracking
programs hand you the Doppler-corrected frequency (pool T8B03).

Curve shape: line-of-sight range-rate is near-maximum at AOS/LOS and zero
at closest approach, giving the classic S-curve, steepest at mid-pass.

Single color (black) on transparent background, post-processed to
currentColor so the figure themes with the page (book pattern: strip the
prolog, swap black -> currentColor, force a default fill).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/home/kasm-user/your-first-ham-license/figures/ch07-doppler-curve.svg"

# time axis: minutes from closest approach, a ~10-minute pass
t = np.linspace(-300, 300, 2000)          # seconds
df_max = 3.0                              # kHz at AOS/LOS — VHF-scale swing
tau = 60.0                                # s, width of the steep zero-crossing

df = -df_max * t / np.sqrt(t**2 + tau**2)

fig, ax = plt.subplots(figsize=(7.6, 4.8))

ax.plot(t / 60.0, df, color="#000000", linewidth=2.4)
ax.axhline(0, color="#000000", linewidth=1.0, alpha=0.45)
ax.axvline(0, color="#000000", linewidth=1.0, linestyle=(0, (4, 3)), alpha=0.5)

ax.set_xlim(-5.2, 5.2)
ax.set_ylim(-4.35, 4.35)
ax.set_xlabel("time during the pass (minutes from closest approach)",
              color="#000000", fontsize=11)
ax.set_ylabel("received frequency,\nkHz away from published", color="#000000",
              fontsize=11)
ax.set_title("Doppler shift: the satellite's signal slides down in frequency",
             color="#000000", fontsize=13)

ax.tick_params(colors="#000000", labelsize=9.5)
for spine in ax.spines.values():
    spine.set_color("#000000")

# stage annotations, offset clear of the curve
ax.annotate("AOS — satellite rising,\ncoming toward you:\nfrequency HIGH",
            xy=(-4.35, 2.35), color="#000000", fontsize=9.5,
            ha="center", va="center")
ax.annotate("overhead at closest approach:\nright ON the published frequency",
            xy=(0.15, 1.55), color="#000000", fontsize=9.5,
            ha="left", va="center")
ax.annotate("LOS — satellite setting,\nmoving away:\nfrequency LOW",
            xy=(4.35, -2.35), color="#000000", fontsize=9.5,
            ha="center", va="center")

ax.plot([0], [0], marker="o", color="#000000", markersize=5)

# why-you-care note along the bottom
fig.text(0.5, 0.015,
         "Only a few kHz at VHF — but enough to lose the signal. That's why you keep adjusting the dial during a pass\n"
         "(or let a tracking program give you the Doppler-corrected frequency).",
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

"""
Generates figures/ch02-am-fm-cw.svg — one voice signal, three ways to send it.

Four stacked time-domain panels sharing one time axis, single-color (black)
on transparent background, post-processed to currentColor so the figure
themes with the page:
  1. the voice (a slow "information" waveform)
  2. AM  — the carrier's amplitude follows the voice (dashed envelope)
  3. FM  — the carrier's frequency wiggles with the voice; amplitude constant
  4. CW  — the carrier is simply keyed on and off (dits and dahs)

Carrier frequency and timing are display values chosen for legibility, not
to scale with any real signal.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/home/kasm-user/your-first-ham-license/figures/ch02-am-fm-cw.svg"

# ---------------------------------------------------------------------
# Signals
# ---------------------------------------------------------------------
fs = 3000.0
t = np.linspace(0, 3.0, int(fs * 3.0), endpoint=False)

# the "voice": a slow two-tone wiggle standing in for speech
voice = 0.7 * np.sin(2 * np.pi * 1.1 * t) + 0.3 * np.sin(2 * np.pi * 2.3 * t + 0.6)

fc = 14.0                       # display carrier, cycles per second
carrier_phase = 2 * np.pi * fc * t

# AM: amplitude = 1 + depth * voice
depth = 0.75
am_env = 1 + depth * voice
am = am_env * np.sin(carrier_phase)

# FM: phase offset proportional to the voice -> frequency wiggles around fc
beta = 9.0                      # radians of phase swing
fm = np.sin(carrier_phase + beta * voice)

# CW: keyed carrier (dit/dah-style pattern, not derived from the voice)
key_down = [(0.10, 0.32), (0.48, 0.90), (1.08, 1.30), (1.48, 1.70),
            (1.86, 2.28), (2.46, 2.68)]
gate = np.zeros_like(t)
for a, b in key_down:
    gate[(t >= a) & (t <= b)] = 1.0
cw = gate * np.sin(carrier_phase)

# ---------------------------------------------------------------------
# Figure: four stacked panels
# ---------------------------------------------------------------------
fig, axes = plt.subplots(4, 1, figsize=(8.0, 7.2), sharex=True)

panels = [
    (voice, "Your voice (the information)", None),
    (am, "AM — the carrier's amplitude follows the voice", am_env),
    (fm, "FM — the frequency wiggles; amplitude stays constant", None),
    (cw, "CW — the carrier is simply keyed on and off", None),
]

for ax, (y, title, env) in zip(axes, panels):
    ax.plot(t, y, color="#000000", linewidth=0.9)
    if env is not None:
        ax.plot(t, env, color="#000000", linewidth=1.4, linestyle=(0, (4, 3)),
                alpha=0.75)
        ax.plot(t, -env, color="#000000", linewidth=1.4, linestyle=(0, (4, 3)),
                alpha=0.75)
    ax.axhline(0, color="#000000", linewidth=0.6, alpha=0.35)
    ax.set_ylim(-2.05, 2.05)
    ax.set_xlim(0, 3.0)
    ax.set_title(title, fontsize=11, color="#000000", loc="left", pad=3)
    ax.set_yticks([])
    ax.set_xticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)

axes[-1].set_xlabel("time  →", fontsize=10, color="#000000")

fig.tight_layout(h_pad=0.6)
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

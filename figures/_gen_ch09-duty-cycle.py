"""Generate figures/ch09-duty-cycle.svg — duty cycle vs average exposure.

The T0C concept in the pool's own framing:
- Duty cycle = the percentage of time the transmitter is actually
  transmitting (T0C11); exposure limits are about *average* exposure
  (T0C10), so transmitting less of the time lowers average RF.
- T0C03's worked arithmetic: dropping from 100% to 50% duty cycle doubles
  the allowable power density (factor of 2). Scaling continues inversely:
  25% -> x4, 10% -> x10 (r4's practice example: 30 s in 5 min = 10%).

Top panel: transmit timelines (continuous vs half-time keying) — same peak,
half the average. Bottom panel: allowable power density vs duty cycle, with
the pool's points marked. Single-color (black) on transparent, then
post-processed: #000000 -> currentColor (Book 1 pattern).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

INK = "black"

fig = plt.figure(figsize=(7.4, 6.6))
gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.5], hspace=0.62,
                      top=0.90, bottom=0.10, left=0.11, right=0.97)

fig.suptitle("Duty Cycle Controls Average Exposure", fontsize=14,
             fontweight="bold", color=INK, y=0.975)

# ---- panel A: transmit timelines ----------------------------------------
a = fig.add_subplot(gs[0])
T = 60.0  # one-minute window
# 100% row (y=10): keyed the whole window; 50% row (y=0): 5 s on / 5 s off
a.broken_barh([(0, T)], (9, 2), facecolors=INK)
a.broken_barh([(t, 5) for t in np.arange(0, T, 10)], (-1, 2), facecolors=INK)
a.set_ylim(-3, 13)
a.set_xlim(0, T)
a.set_yticks([0, 10])
a.set_yticklabels(["50 % duty\ncycle", "100 % duty\ncycle"], fontsize=9,
                  color=INK)
a.set_xlabel("time (seconds) — one minute of operating", fontsize=9.5,
             color=INK)
a.set_title("transmit half the time → half the average RF (same peak)",
            fontsize=11, color=INK)
for side in ("top", "right", "left"):
    a.spines[side].set_visible(False)
a.spines["bottom"].set_color(INK)
a.tick_params(colors=INK, labelsize=8.5)
a.annotate("key down the\nwhole minute", xy=(30, 10), xytext=(30, 5.6),
           fontsize=8.5, color=INK, ha="center", va="center")
a.annotate("on 5 s, off 5 s …", xy=(52, 0), xytext=(58.5, 3.4),
           fontsize=8.5, color=INK, ha="right", va="center")

# ---- panel B: allowable power density vs duty cycle ----------------------
b = fig.add_subplot(gs[1])
d = np.linspace(9, 100, 400)
b.plot(d, 100.0 / d, color=INK, linewidth=2.2)
pts = [(100, 1, "100 % → ×1\n(continuous)"), (50, 2, "50 % → ×2\n(T0C03)"),
       (25, 4, "25 % → ×4"), (10, 10, "10 % → ×10\n(30 s in 5 min)")]
for x, y, lab in pts:
    b.plot([x], [y], marker="o", color=INK, markersize=5)
    b.annotate(lab, xy=(x, y), xytext=(x + 2.5, y + 0.55), fontsize=8.5,
               color=INK, ha="left", va="center")
b.set_xlim(0, 112)
b.set_ylim(0, 12.5)
b.set_xlabel("duty cycle = transmit time ÷ total time  (%)", fontsize=10,
             color=INK)
b.set_ylabel("allowable power density\n(× the continuous limit)", fontsize=10,
             color=INK)
b.set_title("halving the duty cycle doubles the limit — exposure limits "
            "are about the average", fontsize=11, color=INK)
b.set_xticks([10, 25, 50, 75, 100])
b.set_yticks([1, 2, 4, 6, 8, 10])
for side in ("top", "right"):
    b.spines[side].set_visible(False)
for side in ("left", "bottom"):
    b.spines[side].set_color(INK)
b.tick_params(colors=INK, labelsize=9)

out = "figures/ch09-duty-cycle.svg"
fig.savefig(out, transparent=True)

# theme-able: black -> currentColor
with open(out, encoding="utf-8") as fh:
    svg = fh.read()
svg = svg.replace("#000000", "currentColor")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("wrote", out)

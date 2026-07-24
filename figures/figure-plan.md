# Figure Plan — Your First Ham License (Technician)

40 original figures across ch00–ch09. Canon is law (`accuracy-canon.md`); the pool figure redraws follow canon §1.4's binding component-level specification (from r4's verified descriptions).

## Conventions (binding for every figure)

- **Themeable:** strokes/fills/text use `currentColor` (or theme CSS vars); **no hardcoded black/white**; transparent background; `viewBox` set; legible at ~600–800 px wide.
- **Hand-authored SVG** for diagrams/schematics/pictograms; **matplotlib→SVG** for plots/curves (generator saved as `figures/_gen_<id>.py`, post-process black→`currentColor`; see `/home/kasm-user/200-meters-and-down/figures/_gen_*.py` for the established pattern).
- Style reference: Book 1's figures at `/home/kasm-user/200-meters-and-down/figures/` (read 1–2 for the themeable idiom).
- Ground symbols in the three pool redraws use the canon's slanted-strokes-of-decreasing-length style (canon §7.4).
- Metadata: each agent writes `figures/fragments/<id>.json` — `{"id", "chapter", "caption", "kind": "original", "source", "spoken"}` — schema per `tools/figreg.py` and Book 1's `figures/figures.json`. `source` is `"original"` except the pool redraws: `"redrawn from NCVEC pool figure T-1"` (etc.).
- Self-check before finishing: XML-parse each SVG, render to PNG via `google-chrome --headless --screenshot`, view with ReadMediaFile, fix clipping/overlap/legibility.
- Pool-facing numbers come from the canon/pool only (e.g. λ(m) = 300 / f(MHz); 19 in ≈ λ/4 at 146 MHz; 50 MHz dipole ≈ 3 m; offsets "**a common** offset", never "the").

## Figures

| # | id | ch | type | content |
|---|---|---|---|---|
| 1 | ch00-license-ladder | 00 | SVG | Three license classes ladder: Technician → General → Extra, one-line privilege flavor each |
| 2 | ch00-exam-journey | 00 | SVG | Flow: study → find session → 35-question exam → CSCE → $35 fee → ULS grant → on the air |
| 3 | ch01-ohms-law-triangle | 01 | SVG | E=IR triangle + P=E×I variant, the pool's own examples |
| 4 | ch01-series-parallel | 01 | SVG | Series vs parallel resistor circuits, current/voltage behavior labeled |
| 5 | ch01-ac-dc-waveforms | 01 | plot | DC flat line vs AC sine, frequency/period annotated |
| 6 | ch01-wavelength-freq | 01 | plot | Sine wave with λ marked; λ = 300/f(MHz) with 2 m (146 MHz ≈ 2 m) example |
| 7 | ch01-component-symbols | 01 | SVG | Schematic-symbol panel covering EVERY symbol used in T-1/T-2/T-3: resistor, variable resistor (rheostat), capacitor, polarized capacitor, variable capacitor, inductor, tapped/variable inductor, transformer, diode, LED, Zener, NPN transistor, battery, ground, SPST switch, two-position switch, fuse, lamp, connector, antenna |
| 8 | ch01-prefix-ladder | 01 | SVG | Unit prefix ladder: G/M/k — base — m/µ (with the pool's conversion values) |
| 9 | ch01-pool-fig-t1 | 01 | SVG redraw | **Pool figure T-1** (transistor lamp switch) per canon §1.4 — positions 1–5 exact |
| 10 | ch01-pool-fig-t2 | 01 | SVG redraw | **Pool figure T-2** (AC power supply) per canon §1.4 — positions 1–10 exact |
| 11 | ch01-pool-fig-t3 | 01 | SVG redraw | **Pool figure T-3** (T-network antenna tuner) per canon §1.4 — positions 1–4 exact |
| 12 | ch02-am-fm-cw | 02 | plot | AM vs FM vs CW waveforms (modulation concept, beginner level) |
| 13 | ch02-ssb-vs-am-spectrum | 02 | plot | AM (carrier + 2 sidebands) vs SSB spectrum — why SSB is narrower |
| 14 | ch02-rf-spectrum | 02 | plot | The RF spectrum with the Technician-relevant ham bands marked |
| 15 | ch03-groundwave-skywave | 03 | SVG | Direct/ground wave vs skywave paths; line-of-sight vs skip |
| 16 | ch03-ionosphere-skip | 03 | SVG | Ionospheric refraction, skip distance, skip zone |
| 17 | ch03-multipath-fading | 03 | SVG | Multipath: two paths to the receiver, constructive/destructive, "picket-fencing" |
| 18 | ch03-polarization | 03 | SVG | Vertical vs horizontal polarization; cross-pol loss on line-of-sight; why it matters less on skywave |
| 19 | ch04-dipole | 04 | SVG | Half-wave dipole anatomy + length relation (pool numbers: 50 MHz dipole ≈ 3 m; scales with wavelength) |
| 20 | ch04-vertical-groundplane | 04 | SVG | Quarter-wave vertical with radials; 146 MHz ≈ 19 in (pool's own value) |
| 21 | ch04-dipole-pattern | 04 | plot | Dipole radiation pattern (polar): broadside lobes, nulls off the ends |
| 22 | ch04-swr-curve | 04 | plot | SWR vs frequency dip; 1:1 at resonance; why low SWR matters |
| 23 | ch04-connectors | 04 | SVG | Connector pictograms: PL-259/SO-239, SMA, BNC + coax cross-section |
| 24 | ch05-station-block | 05 | SVG | Station block diagram: transceiver, power supply, mic/key, SWR meter, feedline, antenna |
| 25 | ch05-swr-hookup | 05 | SVG | SWR meter inline between radio and antenna; dummy load option |
| 26 | ch05-rfi-path | 05 | SVG | RFI: transmitter → consumer device paths; ferrite/filter/ distance fixes |
| 27 | ch06-simplex-duplex | 06 | SVG | Simplex vs half-duplex via repeater (two frequencies, one tower) |
| 28 | ch06-repeater-offset | 06 | SVG | 2 m repeater: input/output with "a common −600 kHz offset" labeling (canon §7.5 wording) |
| 29 | ch06-ctcss-gate | 06 | SVG | CTCSS tone opens the squelch gate; explicitly "access, not privacy" |
| 30 | ch06-net-flow | 06 | SVG | Directed net: net control at center, check-ins acknowledged in turn |
| 31 | ch07-ft8-sequence | 07 | plot | FT8 15-second transmit/receive cycles on a timeline |
| 32 | ch07-aprs-path | 07 | SVG | APRS: station → digipeater → iGate → internet (144.390 MHz labeled) |
| 33 | ch07-satellite-pass | 07 | SVG | LEO pass geometry: AOS/LOS, ~100-minute period, uplink/downlink |
| 34 | ch07-doppler-curve | 07 | plot | Doppler shift vs time during a pass (±kHz, approach/recede) |
| 35 | ch07-echolink-topology | 07 | SVG | Internet linking: radio ↔ node ↔ internet ↔ remote repeater (EchoLink/IRLP) |
| 36 | ch08-tech-band-chart | 08 | plot | Technician privileges overview: HF slivers (10 m SSB 28.3–28.5 + CW slivers, 200 W) + full VHF/UHF bands |
| 37 | ch08-callsign-anatomy | 08 | SVG | Call-sign anatomy: KF1XXX → prefix/district/suffix; Group D = 2×3 (canon §7.1) |
| 38 | ch09-grounding | 09 | SVG | Station grounding & lightning protection: single ground point, arrestor at entry |
| 39 | ch09-rf-exposure | 09 | SVG | RF exposure: keep antennas away from people; power/distance/duty-cycle levers |
| 40 | ch09-duty-cycle | 09 | plot | Duty cycle vs average exposure (T0C03: halving duty doubles permissible time concept) |

**Merging:** the figures assembler merges `figures/fragments/*.json` into `figures/figures.json`, runs `figreg.validate()` (must be empty), XML-parses all 40 SVGs, and renders a sample (≥8, including all 3 pool redraws) to PNG for visual inspection — the pool redraws are compared against `canon/source/diagram-t*.jpg` for content equality.

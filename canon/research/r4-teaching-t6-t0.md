# R4 Teaching Notes — Subelements T6–T0 (Technician 2026–2030)
Purpose: what a beginner must understand to answer every question in T6 (electrical components, 46), T7 (station equipment, 44), T8 (modulation & operating activities, 47), T9 (antennas & feed lines, 23), T0 (safety, 36). Source of truth: `canon/pool-technician.json` (verified against the NCVEC Feb 2026 release). Question IDs are cited throughout; every cited ID is covered by the teaching point it sits under.

Notation: **FACT** = pure-memorization value to pin in the text. Figure questions: 12 total (T6A09, T6C02–T6C11, T6D10) — see "Pool Figures" under T6.

---

## T6 — Electrical Components (46 questions)
### T6A — Passive components, switches, batteries (11: T6A01–T6A11)
Topics: resistor/potentiometer (3), capacitor (2), inductor (2), SPDT switch + T-2 switch (2), battery chemistry (2).

Beginner must understand:
- A **resistor** opposes (limits) current flow; that is its whole job (T6A01).
- A **potentiometer** is an adjustable resistor — the volume-knob part (T6A02); the parameter it controls is **resistance** (T6A03).
- A **capacitor** stores energy in an **electric field** (T6A04): two conductive plates separated by an insulator (dielectric) (T6A05). An **inductor** stores energy in a **magnetic field** (T6A06): a coil of wire (T6A07).
- Switch names: "pole" = circuits handled; "throw" = contact positions per pole. **SPDT** = one circuit switched between either of two others (T6A08); component 3 in Figure T-2 (one lever, two contacts) = **SPST** (T6A09).
- Rechargeable chemistries: nickel-metal hydride, lithium-ion, lead-acid (and nickel-cadmium) — "all these choices" in T6A10. **FACT: carbon-zinc is the NOT-rechargeable one** (T6A11) — the cheap disposable flashlight battery.

Common confusions:
- Capacitor/electric field vs inductor/magnetic field — the pool's favorite swap (T6A04 vs T6A06). Mnemonic: **C**apacitor = **e**lectric field (both have straight lines/plates); inductor = coil = magnetism.
- Distractor "field strength" (T6A03) sounds electrical but is not a component parameter.
- Read SPDT choices word-by-word; the wrong options describe SPST and DPDT (T6A08).

Vocabulary: resistor, potentiometer, capacitor, dielectric, inductor, pole, throw, SPST, SPDT, rechargeable, carbon-zinc, nickel-metal hydride (NiMH), lithium-ion, lead-acid.

Math: none.

### T6B — Semiconductors (12: T6B01–T6B12)
Topics: diode behavior/markings (4), LED (1), transistor types & electrodes (4), gain/amplification (2), FET abbreviation (1).

Beginner must understand:
- A **diode** lets current flow in only one direction (T6B02); electrodes are **anode** and **cathode** (T6B09), and the cathode end of the physical part is marked **with a stripe** (T6B06), matching the bar in the symbol. Its turn-on "forward voltage drop" **is lower in some diode types than others** (T6B01).
- An **LED** is a diode that emits light when **forward current** flows through it (T6B07) — current in the normal conducting direction.
- A **transistor** is built from **three regions of semiconductor material** (T6B04); it works as an **electronic switch** (T6B03) or an amplifier providing **power gain** (T6B10). **Gain** = output compared to input — of voltage, current, or power, hence "all these choices" (T6B11).
- Two transistor families, two electrode name sets: **BJT** (bipolar junction transistor) = **emitter, base, collector** (T6B12); **FET** (field-effect transistor) = **gate, drain, source** (T6B05). **FACT: FET = Field Effect Transistor** (T6B08).

Common confusions:
- Three electrode sets get shuffled as distractors: anode/cathode (diode), emitter/base/collector (BJT), gate/drain/source (FET). T6B05's wrong answer is "bipolar junction"; T6B09's wrong answers are the FET/BJT sets. Drill the three sets as a table.
- "Reverse current" (T6B07) lights nothing — reverse current is what a diode blocks.
- FACT-expansion distractors in T6B08 are made-up phrases ("Fast Electron Transistor").

Vocabulary: semiconductor, diode, anode, cathode, forward voltage drop, light-emitting diode (LED), forward current, transistor, bipolar junction transistor (BJT), field-effect transistor (FET), emitter/base/collector, gate/drain/source, gain, electronic switch.

Math: none.

### T6C — Schematics and the pool figures (12: T6C01–T6C12)
Topics: schematic definition/purpose (2: T6C01, T6C12), figure identification (10: four on T-1 — T6C02–T6C05; four on T-2 — T6C06–T6C09; two on T-3 — T6C10, T6C11; see Pool Figures).

Beginner must understand:
- A **schematic** is an electrical diagram drawn with standard component symbols (T6C01); what it accurately shows is **how components are connected** — not wire lengths, not physical appearance (T6C12). Symbols, not pictures.
- The ten identification questions are pure symbol recognition; learn each symbol once and these are free points (T6C02–T6C11).

Common confusions:
- Within-figure distractors: wrong choices are usually other components from the same figure (T6C10 offers "variable capacitor," which really is in T-3 — but it is component 2, not 3). Teach position numbers, not just symbols.
- T6C12's "all these choices are correct" is the trap answer — here only "component connections" is right.

Vocabulary: schematic (diagram), component symbol, ground symbol, node/junction.

Math: none.

### T6D — What circuits do (11: T6D01–T6D11)
Topics: power-supply stages (rectifier, regulator, transformer: 3), relay (1), shielded wire (1), meter (1), LED indicator (1), resonant/tuned circuits (2), integrated circuit (1), T-1 transistor function (1).

Beginner must understand:
- Power-supply chain to teach: transformer → rectifier → filter → regulator. A **rectifier** turns AC into a varying (pulsating) DC (T6D01); a **transformer** changes AC voltage up or down — e.g. 120 V AC to a lower **AC** voltage, never DC (T6D06); a **regulator** holds the supply's output voltage steady (T6D05).
- A **relay** is an electrically controlled switch — a small coil current switches a bigger current (T6D02). **Shielded wire** keeps unwanted signals from coupling into or out of the wire (T6D03). A **meter** displays an electrical quantity as a numeric value (T6D04).
- LEDs are the standard **visual indicator** component (T6D07). Note the trap: "all these choices" is wrong because FETs and Zener diodes are not indicators.
- An **inductor plus a capacitor** (series or parallel) makes a **resonant (tuned) circuit** — the frequency-selecting circuit (T6D08, T6D11). An **integrated circuit (IC/chip)** packs many semiconductors and other components into one package (T6D09). In Figure T-1 the transistor's job is to **control the flow of current** — switching the lamp (T6D10).

Common confusions:
- Transformer (AC→AC, T6D06) vs rectifier (AC→DC, T6D01): read the question for "AC" or "DC" on the output side.
- Resonant circuit = L + C only; resistor distractors (T6D08) never resonate.
- T6D10's distractors are the functions of the *other* T-1 parts (lamp = light, battery = energy); match function to component 2.

Vocabulary: rectifier, regulator, transformer, relay, shielded wire, meter, indicator, resonant/tuned circuit, integrated circuit (IC), Zener diode (distractor-term worth knowing).

Math: none.

### Pool Figures — precise descriptions for SVG redraw
Common style note (all three figures): black-and-white line schematics on white, bold sans-serif component labels, and **every ground symbol is drawn as three slanted (diagonal) strokes of decreasing length, longest on top** (not the classic horizontal shrinking lines). Source JPGs in `canon/source/`; "Figure T-1/2/3" caption centered beneath each drawing.

**Figure T-1 — transistor lamp-switch circuit** (source `canon/source/diagram-t1.jpg`).
Layout, left to right, roughly centered on the page:
- Far left: an unnumbered two-position switch — two open-circle contacts stacked vertically; each contact has a short leftward stub ending in a two-pronged fork (two angled arms, like a sideways "Y"). Upper contact wired right to component 1; lower contact wired straight down to ground symbol 5.
- **1 = resistor**: horizontal zigzag, series between the switch's upper contact and the transistor base lead. Label "1" above it. → asked by T6C02.
- **2 = NPN transistor**: circle containing a thick vertical base bar on its left half; base lead enters horizontally from the left to the bar; a line from the bar's upper right exits the circle top (collector) and runs up to the lamp wire; a line from the bar's lower right exits the circle bottom with a **filled arrowhead pointing outward/down-right (NPN emitter)** and runs down to a ground symbol. Label "2" above the circle. → identity asked by T6C03; **function** ("control the flow of current") asked by T6D10.
- **3 = lamp**: an arch/dome (semicircular loop) symbol on the top horizontal wire between the collector line and the battery top. Label "3" above. → T6C04.
- **4 = battery**: two cell pairs — four horizontal plates alternating long/short (long, short, long, short) — at the right; top connects to the lamp wire, bottom to a ground symbol. Label "4" to the right of the plates. → T6C05.
- **5 = ground symbol** (three slanted strokes) beneath the switch's lower contact. Label "5" below. Not directly asked. Unnumbered identical grounds also sit under the transistor emitter and the battery.
Circuit story for teaching: closing the switch lets base current flow through resistor 1; the transistor (2) then conducts, switching battery (4) current through lamp (3).

**Figure T-2 — AC power supply** (source `diagram-t2.jpg`). Left block = primary loop; right block = DC side; grounds along the bottom.
- **1 = AC voltage source**: circle with two thick horizontal filled bars inside, on the left vertical leg of the primary loop. Label "1" right of it. Not asked.
- **2 = fuse**: small open rectangle, series in the top wire of the primary loop. Label "2" above. Not asked.
- **3 = SPST switch**: two open-circle contacts with a single angled blade hinged at the left contact, blade tip raised toward the right contact (drawn open), series in the top primary wire. Label "3" above. → T6A09 (asks its *type*: single-pole single-throw).
- **4 = transformer**: left (primary) coil with 3 humps, two parallel vertical core lines, right (secondary) coil with 4 humps; primary top/bottom close the left loop to source 1; secondary bottom grounded, secondary top feeds component 5. Label "4" above the core lines. → T6C09.
- **5 = rectifier diode**: filled triangle pointing right into a vertical bar (anode left, cathode right), series in the top DC rail. Label "5" above. Not asked.
- **6 = capacitor**: top plate a straight horizontal line, bottom plate curved upward (polarized style), shunt from top rail to ground. Label "6" left of it. → T6C06.
- **7 = resistor**: vertical zigzag from the top rail down to component 8 (series pair forming the indicator branch). Label "7" left. Not asked.
- **8 = LED**: filled diode triangle pointing DOWN into a horizontal bar, with two small arrows pointing away down-right (light), bottom of branch grounded. Label "8" left. → T6C07.
- **9 = variable resistor**: zigzag in the top rail with a diagonal arrow touching it from below; the arrow's tail wire runs right and joins the rail at the resistor's right end (rheostat style). Filled dots mark the rail nodes on both sides of 9. Label "9" above. → T6C08.
- **10 = Zener diode**: filled diode triangle pointing UP with a bent "Z-shaped" cathode bar on top, shunt from top rail to ground. Label "10" left. Not asked, but name it — it appears as a distractor elsewhere (T6D07, T6D08).
- Far right: open-circle output terminal on the top rail. Ground symbols under the secondary, 6, the 7+8 branch, and 10.
Teaching story: wall AC (1) → fuse (2) → switch (3) → transformer steps down (4) → diode rectifies (5) → capacitor smooths (6) → resistor+LED power indicator (7, 8) → variable resistor (9) → Zener sets/regulates voltage (10) → output.

**Figure T-3 — antenna tuner (transmatch), T-network** (source `diagram-t3.jpg`).
- Horizontal signal path across the upper third: **[1] → [2] → junction dot → unnumbered second variable capacitor → wire right, then up to [4]**.
- **1 = connector**: curly-brace "{"-style symbol (coax connector) at the far left on the input line — this is where the transmitter connects. Label "1" left of it. Not asked.
- **2 = variable capacitor**: two vertical plates with a diagonal arrow through them (arrowhead upper right), series in the top line. Label "2" above. Not asked — but it is the trap answer in T6C10.
- Junction: filled dot after component 2; from it a vertical branch goes down to component 3; the top line continues through the second (unnumbered) variable capacitor, then turns up to the antenna.
- **3 = variable inductor**: vertical coil (4 humps) from the junction dot downward, with a filled arrowhead tap pointing left into the coil's mid-region; the tap wire runs right, then down, then left to a second filled dot at the coil bottom (shorting the lower turns — adjustable inductance), which continues down to a ground symbol. Label "3" left of the coil. → T6C10 (answer: variable inductor).
- **4 = antenna**: outline inverted triangle (apex down) at the top right, apex joined to the vertical feed wire. Label "4" above. → T6C11 (answer: antenna).
Teaching story: two adjustable capacitors with an adjustable inductor to ground form a "T" matching network between the transmitter connector (1) and the antenna (4) — a picture of the antenna tuner studied in T9B04.

Watch items (T6 FACT lines): carbon-zinc = not rechargeable; stripe = cathode; FET = field-effect transistor; FET electrodes gate/drain/source vs BJT emitter/base/collector; all 12 figure component IDs above; L+C = resonant circuit; rectifier = AC→varying DC.

---

## T7 — Station Equipment (44 questions)
### T7A — Receivers, transmitters, transceivers (11: T7A01–T7A11)
Topics: sensitivity/selectivity (2), transceiver (1), mixer (1), oscillator/VFO (2), transverter (1), PTT (1), modulation (1), amplifier mode switch (1), RF power amplifier (1).

Beginner must understand:
- **Sensitivity** = a receiver's ability to detect the presence of (weak) signals (T7A01); **selectivity** = its ability to discriminate between multiple (nearby) signals (T7A04). Detect vs separate — the pool's core pair.
- A **transceiver** combines a receiver and a transmitter in one unit (T7A02).
- A **mixer** converts a signal from one frequency to another (T7A03); an **oscillator** generates a signal at a specific frequency (T7A05); the **VFO (variable frequency oscillator)** is the circuit that sets a transceiver's receive and transmit frequency (T7A11).
- A **transverter** converts a transceiver's RF input and output to another band — run your HF radio on VHF (T7A06). Do not confuse with "transceiver" or "transformer."
- The **PTT (push-to-talk) input** switches the transceiver from receive to transmit **when grounded** (T7A07) — accessories ground that line to key the rig.
- **Modulation** = combining speech (or data) with an RF carrier signal (T7A08).
- The SSB / CW-FM switch on some VHF power amplifiers **sets the amplifier for proper operation in the selected mode** (T7A09) — it optimizes the amp; it does not change your signal's mode.
- To raise transmitted output power, add an **RF power amplifier** after the transceiver (T7A10).

Common confusions:
- Sensitivity vs selectivity (T7A01/T7A04) — most-missed pair in the group.
- Mixer (moves a signal in frequency) vs oscillator (creates a signal) vs modulator (puts information on a carrier) — all three appear as mutual distractors.
- T7A09's distractor "change the mode of the transmitted signal" is backwards: the operator picks the mode; the switch adapts the amplifier.

Vocabulary: sensitivity, selectivity, transceiver, mixer, oscillator, VFO, transverter, PTT (push-to-talk), modulation, carrier, RF power amplifier.

Math: none.

### T7B — Interference: causes and cures (11: T7B01–T7B11)
Topics: over-deviation/distorted audio (3), receiver overload (2), RFI cause inventory (1), filter placement (3), neighbor relations (1), ferrite choke (1).

Beginner must understand:
- **Over-deviation** on FM = your audio swings the carrier too far; caused by talking too loud/too close — the fix is to **talk farther away from the microphone** (T7B01). Distorted/unintelligible audio through an FM repeater can come from being slightly off frequency, speaking too loudly/close, or a bad location — all three (T7B10).
- A broadcast radio/TV that picks up your transmission is being **overloaded by a strong signal it cannot reject** (fundamental overload) — the problem is in the affected receiver, not necessarily your station (T7B02).
- RFI can come from **fundamental overload, harmonics, or spurious emissions** — all (T7B03).
- **High SWR** (not low) can make a solid-state transceiver reduce output power (T7B04).
- Filter logic — teach the direction of protection:
  - Your clean signal bothers a neighbor's receiver → **filter at the affected receiver's antenna input** to block your signal (T7B05).
  - A nearby commercial FM station overloads your 2-meter rig → **band-reject filter** at your receiver (T7B07).
  - Cable TV interference (non-fiber): **first** check that all coax connectors are properly installed — broken shielding is the usual entry point (T7B09); filters come later.
- A **clip-on ferrite choke** on the microphone cable stops your transmitted RF from feeding back into the rig and distorting your audio (T7B11).
- When a neighbor complains: first **verify your own station is operating properly** and isn't also interfering with your own consumer gear on the same channel (T7B06). If *their* device interferes with *you*: work with the neighbor to find it, note that FCC rules prohibit interference-causing devices, and keep your own station above reproach — all three (T7B08). Politeness and self-check first, always.

Common confusions:
- "Filter at the transmitter" vs "filter at the receiver": harmonic/spurious problems are fixed at the transmitter; overload of a non-amateur receiver is fixed at that receiver. The pool mostly tests the receiver-side case.
- T7B10's wrong-looking options are all individually true — the answer is "all these choices are correct."
- Low SWR (T7B04 distractor) is desirable and never reduces power.

Vocabulary: deviation / over-deviation, fundamental overload, harmonic, spurious emission, harmful interference, band-reject filter, high-pass/low-pass filter (distractor terms), ferrite choke, RF feedback.

Math: none.

### T7C — Dummy loads, SWR, feed-line health (11: T7C01–T7C11)
Topics: dummy load purpose/construction (2), antenna analyzer (1), SWR readings & instruments (3), SWR protection (1), feed-line loss (1), coax failure/UV/foam (3).

Beginner must understand:
- A **dummy load** is a fake antenna: a **50-ohm non-inductive resistor on a heat sink** (T7C03) that absorbs transmitter power so you can **test without putting a signal on the air** (T7C01).
- An **antenna analyzer** tells you whether an antenna is resonant at your operating frequency (T7C02).
- **SWR** readings: **1:1 = perfect match** (T7C04); **4:1 = impedance mismatch** (T7C06). A **directional wattmeter** is the instrument used to determine SWR (T7C08) — it reads forward and reflected power.
- Solid-state transmitters automatically cut power as SWR rises **to protect the RF output transistors** from reflected power (T7C05).
- Power lost in a feed line is **converted into heat** (T7C07).
- Coax enemies: **moisture contamination** is the classic cable-killer (T7C09); the outer jacket must resist UV because sunlight cracks it and then **water gets in** (T7C10); **foam-dielectric** coax has **less loss per foot** than solid-dielectric (T7C11).

Common confusions:
- SWR is a ratio: "1:1" good, bigger first number = worse. Distractors "50:50" and "zero" (T7C04) are nonsense readings.
- T7C05's distractor "to lower the SWR" is backwards — the radio protects itself; it cannot fix the antenna.
- UV damage mechanism is cracking→water entry, not RF effects (T7C10).

Vocabulary: dummy load, non-inductive resistor, heat sink, antenna analyzer, SWR meter, directional wattmeter, forward/reflected power, feed-line loss, dielectric (foam vs solid), moisture contamination, UV-resistant jacket.

Math: none (SWR values are memorized readings, not computed).

### T7D — Meters and soldering (11: T7D01–T7D11)
Topics: voltmeter (2: T7D01, T7D02), ammeter (2: T7D03, T7D04), ohmmeter principle, hazards & quirks (4: T7D05, T7D06, T7D10, T7D11), multimeter scope (1: T7D07), soldering (2: T7D08, T7D09).

Beginner must understand:
- **Voltmeter** measures electric potential (voltage) (T7D01) and connects **in parallel** with the component (T7D02) — it looks at the difference across two points.
- **Ammeter** measures current (T7D04) and connects **in series** (T7D03) — the current must flow through the meter.
- An **ohmmeter** measures resistance by **applying a small current and measuring the resulting voltage** (T7D05) — it uses its own internal battery, so **the circuit must not be powered** (T7D11).
- Across a large discharged capacitor, an ohmmeter reads **increasing resistance with time** — the meter's battery slowly charges the capacitor (T7D10). Counterintuitive; teach it as a FACT.
- What can damage a multimeter: **measuring voltage while set to the resistance (ohms) setting** (T7D06).
- A multimeter measures **voltage and resistance** (and current) — not impedance, reactance, or signal strength (T7D07).
- Soldering: **never acid-core solder** for electronics (it corrodes; it is for plumbing) — use rosin-core (T7D08). A **cold solder joint** looks **rough or lumpy**; a good joint is shiny and smooth (T7D09).

Common confusions:
- Parallel-for-volts vs series-for-amps is the group's signature swap (T7D02/T7D03).
- The damage scenario is ohms-setting-meets-voltage, not volts-setting-meets-resistance (T7D06) — read carefully.
- "Bright or shiny" (T7D09) describes a *good* joint, so it is the wrong answer to "cold joint."

Vocabulary: voltmeter, ammeter, ohmmeter, multimeter, in series / in parallel, electric potential, rosin-core solder, acid-core solder, cold solder joint.

Math: none.

Watch items (T7 FACT lines): dummy load = 50 Ω non-inductive resistor on heat sink; SWR 1:1 perfect / 4:1 mismatch; directional wattmeter measures SWR; ohmmeter + powered circuit = wrong (and ohms-setting + voltage = meter damage); capacitor on ohmmeter = rising reading; acid-core never; cold joint = rough/lumpy; foam coax = less loss/foot; clip-on ferrite cures mic-cable RF feedback.

---

## T8 — Modulation & Operating Activities (47 questions)
### T8A — Modulation modes and bandwidths (12: T8A01–T8A12)
Topics: mode identification/usage (5), SSB vs FM tradeoffs (2), sideband convention (1), bandwidth values (4).

Beginner must understand:
- The mode families: **AM** varies carrier amplitude (SSB is a form of AM — T8A01); **FM/PM** vary frequency/phase; **CW** is just a carrier keyed on and off.
- Who uses what: **FM (or PM)** for VHF/UHF voice repeaters (T8A04) and VHF packet radio (T8A02); **SSB** for long-distance weak-signal voice on VHF/UHF (T8A03) and on HF.
- Convention: **upper sideband (USB)** is normal for 10-meter HF, VHF, and UHF SSB (T8A06). (Chapter may add: LSB is the convention below 10 MHz — not asked here but prevents confusion on the air.)
- Tradeoffs: SSB's advantage over FM is **narrower bandwidth** (T8A07); FM's disadvantage is the **capture effect — only one signal can be received at a time** (the strongest wins) (T8A12).
- **The bandwidth ladder — memorize these four (FACT):**
  - CW ≈ **150 Hz** (T8A11) — narrowest of all (T8A05)
  - SSB voice ≈ **3 kHz** (T8A08)
  - FM voice (VHF repeater) ≈ **10–15 kHz** (T8A09)
  - AM fast-scan TV ≈ **6 MHz** (T8A10)

Common confusions:
- Bandwidth numbers get scrambled across questions (3 kHz vs 15 kHz vs 150 Hz); anchor them to the ladder picture: CW < SSB < FM < TV.
- "SSB is easier to tune / less interference" (T8A07 distractors) — the true, tested advantage is narrowness.
- T8A12: FM's tested weakness is one-signal-at-a-time, not audio quality (FM audio is actually fine).

Vocabulary: amplitude modulation (AM), single sideband (SSB), upper/lower sideband (USB/LSB), frequency modulation (FM), phase modulation (PM), bandwidth, carrier, capture effect, fast-scan TV.

Math: none (bandwidths are memorized values).

### T8B — Amateur satellites (12: T8B01–T8B12)
Topics: beacon/telemetry (3), tracking programs (2), Doppler (1), mode designators U/V (1), spin fading (1), LEO (1), satellite modes (1), uplink power discipline (2).

Beginner must understand:
- A **beacon** is a transmission from the satellite carrying **status information/telemetry** (health and status — T8B01, T8B05). **Anyone** may receive satellite telemetry — no license needed to listen (T8B11).
- **Tracking programs** need the **Keplerian elements** (the orbit-description numbers) as input (T8B06) and give you maps of the ground track, pass times with azimuth/elevation, and the Doppler-corrected frequency — all (T8B03).
- **Doppler shift** = the observed change in signal frequency caused by relative motion between satellite and Earth station (T8B07) — the same effect as a passing siren changing pitch.
- Mode designators read **uplink/downlink**: **U/V = uplink on 70 cm (UHF), downlink on 2 m (VHF)** (T8B08). First letter = the band you transmit *up*.
- **Spin fading**: the satellite and its antennas rotate, so signal strength rhythmically rises and falls (T8B09) — not Doppler.
- **FACT: LEO = Low Earth Orbit, with an orbital period of around 100 minutes** (T8B10).
- Satellites use SSB, FM, and CW/data — all (T8B04).
- Power discipline: too much uplink power **blocks access by other users** through the shared transponder (T8B02); the right level is when **your downlink signal is about as strong as the satellite's beacon** (T8B12).

Common confusions:
- U/V letter order: uplink first (T8B08's distractors invent "ultraviolet" and 15 m/10 m).
- Doppler (frequency change from motion) vs spin fading (amplitude change from rotation) — both satellite-specific, often swapped.
- Beacon is a radio transmission, not an antenna, light, or reflector (T8B05 distractors).

Vocabulary: telemetry, beacon, transponder, uplink, downlink, Doppler shift, Keplerian elements, satellite pass (azimuth/elevation), spin fading, LEO (Low Earth Orbit), U/V mode, effective radiated power (ERP).

Math: none.

### T8C — Operating activities and internet linking (11: T8C01–T8C11)
Topics: direction finding/fox hunting (2), contesting (2), grid locator (1), VoIP/IRLP/EchoLink (5), gateway (1).

Beginner must understand:
- **Radio direction finding (RDF)** locates sources of noise, interference, or jamming (T8C01); a **directional antenna** is the key tool for hidden-transmitter ("fox") hunts (T8C02).
- **Contesting** = contact as many stations as possible in a specified period (T8C03); good practice is to send **only the minimum information needed for ID and the contest exchange** (T8C04) — brief is polite.
- A **grid locator** is a letter-number designator for a geographic location (Maidenhead system, e.g. "FN31") (T8C05).
- **VoIP** = Voice over Internet Protocol: voice delivered over the internet digitally (T8C07).
- **IRLP** (Internet Radio Linking Project) connects amateur systems like repeaters through the internet (T8C08); over-the-air access is by **DTMF** (touch-tone) codes from your radio (T8C06).
- **EchoLink** lets you operate through a repeater **without a radio** — from a computer/phone app (T8C09); before using it you must **register your call sign and provide proof of license** (T8C10).
- A **gateway** is an amateur station that connects other amateur stations to the internet (T8C11).

Common confusions:
- IRLP vs EchoLink: IRLP = radio-to-radio via internet, keyed with DTMF; EchoLink = computer/app access allowed. T8C09's distractors (IRLP, D-STAR, DMR) are all radio-based.
- DTMF (the beep codes that command a node) vs CTCSS (the continuous sub-audible tone that opens a repeater) — T8C06 distractor; CTCSS is covered in T2 territory.
- Grid locator is geographic, not azimuth/elevation (T8C05 distractor).

Vocabulary: radio direction finding (RDF), hidden transmitter hunt (fox hunt), directional antenna, contesting, contest exchange, grid locator (Maidenhead), VoIP, IRLP, EchoLink, DTMF (dual-tone multi-frequency), gateway, node.

Math: none.

### T8D — Digital modes (12: T8D01–T8D12)
Topics: mode inventory (1), FT8/WSJT-X (2), APRS (2), packet structure/ARQ (2), PSK (1), DMR (1), CW (1), NTSC (1), mesh (1).

Beginner must understand:
- Digital modes include **packet radio, IEEE 802.11 (Wi-Fi), and FT8** — all (T8D01). Yes, Wi-Fi counts when run under amateur rules.
- **FT8** is a digital mode that works at **very low signal-to-noise** — contacts below audibility, in timed 15-second sequences (T8D02). The **WSJT-X** software suite (FT8's home) supports Earth-Moon-Earth, weak-signal beacons, and meteor scatter — all (T8D10).
- **APRS** carries GPS position, text messages, and weather data — all (T8D03); its signature use is **real-time tactical communications with a map showing station locations** (T8D05).
- **Packet radio** transmissions include a checksum for error detection, a header with the destination call sign, and automatic repeat request — all (T8D08). **ARQ** = the receiver detects errors and requests retransmission (T8D11).
- **FACT: PSK = Phase Shift Keying** (T8D06).
- **DMR** (Digital Mobile Radio) time-multiplexes **two digital voice signals on a single 12.5 kHz channel** (two "time slots") (T8D07).
- **CW** is simply another name for a **Morse code transmission** (T8D09).
- **NTSC** = the analog fast-scan color TV signal standard (T8D04).
- An amateur **mesh network** uses **commercial Wi-Fi equipment with modified firmware** on amateur frequencies (T8D12).

Common confusions:
- "PSK" distractors all start with P-words ("Pulse Shift Keying"); memorize Phase Shift Keying.
- ARQ is error correction by retransmission request, not encryption or compression (T8D11 distractors).
- CW has nothing to do with 2-meter FM (T8D09 distractor) — it is Morse, mostly HF.
- FT8 is digital/weak-signal, not FM voice and not TV (T8D02 distractors).

Vocabulary: digital mode, packet radio, FT8, WSJT-X, APRS, PSK (phase shift keying), DMR, time slot, checksum, header, ARQ (automatic repeat request), CW (Morse code), NTSC, fast-scan TV, mesh network, Earth-Moon-Earth (EME), meteor scatter.

Math: none.

Watch items (T8 FACT lines): bandwidth ladder 150 Hz / 3 kHz / 10–15 kHz / 6 MHz; USB on 10 m/VHF/UHF; U/V = up 70 cm, down 2 m; LEO period ≈ 100 min; downlink ≈ beacon strength; DTMF opens IRLP; EchoLink needs license verification; PSK = phase shift keying; DMR = two time slots on 12.5 kHz; CW = Morse; NTSC = analog fast-scan color TV.

---

## T9 — Antennas & Feed Lines (23 questions)
### T9A — Antennas (11: T9A01–T9A11)
Topics: beam/Yagi/gain (3), loading & resonant length (2), polarization (1), HT/mobile practical (3), dipole pattern (1), quarter-wave whip (1 — the math anchor).

Beginner must understand:
- A **beam antenna** concentrates signals in one direction (T9A01); a **Yagi** offers the greatest gain of the antennas listed (T9A06). **Antenna gain** = the increase in signal strength **in a specified direction** compared to a reference antenna (T9A11) — gain comes from focusing, like a flashlight reflector; no extra power is created.
- **Polarization** is described by the **orientation of the electric field** (T9A03) — vertical element → vertically polarized. (Match polarizations or lose signal.)
- **Loading** = electrically lengthening an antenna by inserting **inductors (coils)** in the radiating elements — how short mobile whips act longer (T9A02).
- Length ↔ frequency runs inverse: **shortening** a dipole **raises** its resonant frequency (T9A05). Longer antenna = lower frequency.
- A half-wave dipole radiates strongest **broadside** (out from its sides), weakest off the ends (T9A10).
- HT realities: the short flexible "rubber duck" has **low efficiency** versus a full-size quarter-wave (T9A04); using an HT inside a car, the **vehicle's metal shell shields and weakens the signal** — use an external antenna (T9A07).
- A **19-inch vertical** is often used on 2 meters because it is a **resonant quarter-wave** there (T9A08 — see Math).
- A **5/8-wave whip** has **more gain** than a 1/4-wave whip for VHF/UHF mobile (T9A09).

Common confusions:
- Gain is directional focusing, not "extra power added" (T9A11 distractor A).
- Broadside vs off-the-ends (T9A10) — beginners picture dipoles "shooting" off their ends; it is the opposite.
- Loading uses inductors, not resistors or springs (T9A02 distractors).
- 19 inches is a quarter-wave, not half-wave (T9A08 distractor B) — the math below settles it.

Vocabulary: beam antenna, Yagi, driven element, antenna gain, reference antenna, polarization (electric field), loading / loading coil, resonant frequency, dipole, broadside, quarter-wave vertical, rubber-duck antenna, 5/8-wave whip, efficiency.

### T9B — Feed lines and connectors (12: T9B01–T9B12)
Topics: coax properties/impedance (2), loss mechanisms (4), connector types (3), SWR meaning/behavior (2), antenna tuner (1).

Beginner must understand:
- **FACT: coax used in amateur radio is 50 ohms** characteristic impedance (T9B02). Coax dominates because it is **easy to use and needs few special installation considerations** (T9B03) — not because it is lowest-loss or cheapest.
- Coax **loss increases as frequency increases** (T9B05) — why UHF runs need better/shorter cable.
- Loss sources: water in connectors, high SWR, multiple connectors — all (T9B08). **Erratic SWR changes** point to a **loose connection** in antenna or feed line (T9B09).
- Cable grades: **RG-213 has less loss than RG-58** at a given frequency (it is thicker) (T9B10); **air-insulated hardline** has the lowest loss of the listed feed lines (T9B11).
- **SWR** = a measure of **how well a load is matched to a transmission line** (T9B12).
- Connectors: **PL-259** ("UHF" plug) is the standard at **HF and VHF** but is **not watertight** (T9B07); **Type N** is the right choice **above 400 MHz** (T9B06); any outdoor connector (PL-259, BNC, Type N) should be **carefully taped against weather** (T9B01 — "all these choices").
- An **antenna tuner (coupler)** matches the antenna system impedance to the transceiver's 50-ohm output (T9B04) — it sits at the radio and "tunes out" the mismatch the SWR meter complains about (relate to Figure T-3).

Common confusions:
- PL-259 is called a "UHF connector" historically but is **not** the best choice at UHF — Type N is (T9B06 vs T9B07 is the pool's deliberate pair).
- SWR is about the line-to-load match, not grounding or efficiency (T9B12 distractors).
- T9B08: each single cause listed is true — answer is "all."

Vocabulary: feed line, coaxial cable, characteristic impedance, 50 ohms, dielectric, hardline (air-insulated), SWR (standing wave ratio), impedance match, PL-259, BNC, Type N connector, waterproofing/taping, antenna tuner (coupler/transmatch), connector loss.

### T9 Math — wavelength and antenna length
The exam never asks for a calculation, but one teaching formula makes T9A05 and T9A08 obvious:
- **Wavelength (m) ≈ 300 / frequency (MHz)**; a quarter-wave antenna is λ/4; a half-wave dipole is λ/2.
- Worked example 1 (the pool's own numbers, T9A08): 2-meter band ≈ 146 MHz.
  λ = 300 / 146 ≈ 2.05 m. Quarter-wave = 2.05 / 4 ≈ 0.51 m ≈ 51 cm ≈ 20 inches — matching the **19-inch** whip (real antennas run ~5% short, hence 19 not 20). So "resonant quarter-wave" is the answer, and "resonant half-wave" would need ~1 m.
- Worked example 2 (sanity for T9A05): a dipole cut for 50 MHz (6-meter band) is λ/2 = (300/50)/2 = 3 m long. To raise the resonance to 100 MHz you must **shorten** it to 1.5 m — shorter antenna, higher frequency.
- Related watch item: coax **loss rises with frequency** (T9B05) — same axis, opposite lesson (higher frequency = shorter antennas but lossier cable).

Watch items (T9 FACT lines): 50 Ω coax; Yagi = most gain; polarization = E-field orientation; dipole strongest broadside; 19 in ≈ λ/4 on 2 m; 5/8-wave > 1/4-wave gain; shortening raises resonant frequency; RG-213 < RG-58 loss; hardline lowest loss; Type N > 400 MHz; PL-259 not watertight (tape all outdoor connectors); tuner matches antenna system to transceiver.

---

## T0 — Safety (36 questions)
Chapter structure note (per assignment): **T0A + T0B are electrical/physical safety** (power, wiring, batteries, towers) and **T0C is RF exposure** — treat them in separate sections. Below they are grouped that way.

### Part 1 — Electrical and home-station safety
**T0A — Power, wiring, batteries (12: T0A01–T0A12)**
Topics: battery hazards (2), current through the body (1), wire color code (1), fuses/breakers (3), shock prevention (2), lightning arresters/grounding (2), high-voltage measurement (1).

Beginner must understand:
- A 12 V battery will not shock you, but **shorting its terminals can cause burns, fire, or an explosion** (T0A01) — the danger is huge current, not voltage. Rapid charging/discharging risks **overheating or out-gassing** (T0A10) — charge batteries in ventilated space.
- Current through the body can **heat tissue, disrupt cells' electrical function, and cause involuntary muscle contractions** — all (T0A02). Even "minor" household voltage is respected.
- **FACT: in US three-wire 120 V cable, black = hot** (T0A03). (Teach the full code for life safety: white = neutral, green = ground — only black is tested.)
- A **fuse removes power in case of an overload** (T0A04); **never replace a fuse with a larger one** — excessive current could start a fire (T0A05); the fuse/breaker goes **in series with the hot conductor only** (T0A08).
- Shock protection habits: three-wire cords/plugs, all station equipment on a common safety ground, and fully discharging high-voltage capacitors before working inside gear — all (T0A06). A power supply can still kill **immediately after switch-off** because of **charge stored in its filter capacitors** (T0A11).
- Lightning: the **lightning arrester goes on a grounded panel near where feed lines enter the building** (T0A07); **all external ground rods must be bonded together** with heavy wire or strap (T0A09) — separate, unbonded grounds create dangerous voltage differences.
- Measuring high voltage: the **voltmeter and its leads must be rated for the voltage being measured** (T0A12).

**T0B — Towers and antenna installation (11: T0B01–T0B11)**
Topics: tower grounding (4), climbing rules (3), power-line clearance (3), guy hardware (1).

Beginner must understand:
- Tower grounding: connections **short and direct** (T0B01); **separate eight-foot ground rods for each tower leg, bonded to the tower and to each other** (T0B08); **avoid sharp bends** in grounding conductors — lightning wants a smooth path (T0B10); grounding requirements come from **local electrical codes** (T0B11), not the FCC.
- Climbing: get training, **tie off at all times**, wear an approved harness — all (T0B02); **never climb without a helper or observer** (T0B03); on a **crank-up tower**, climb only when it is **retracted or mechanical safety locks are installed** (T0B07).
- Power lines: before raising anything, **look for and stay clear of overhead wires** (T0B04); **FACT: position the antenna so that if it falls, no part can come within 10 feet of power lines** (T0B06); never attach an antenna to a **utility pole** — it could contact high-voltage lines (T0B09).
- Guyed towers: the **safety wire through a turnbuckle keeps vibration from loosening it** (T0B05).

Common confusions (T0A/T0B):
- "Fuse limits current to prevent shocks" (T0A04 distractor) — fuses protect against overload/fire; grounding protects against shock. Different jobs.
- Right-angle bends are *bad* for lightning grounds (T0B10 vs its own distractor; T0B01 distractor "right angles" is wrong too — "short and direct" is right).
- The 10-foot rule is about a *fallen* antenna's worst case, not a fixed horizontal distance (T0B06 distractors).
- T0B11: FCC writes radio rules; **local electrical codes** write grounding rules.

Vocabulary: hot/neutral/ground conductors, fuse, circuit breaker, overload, safety ground, bonding, ground rod, lightning arrester, filter capacitor, out-gassing, climbing harness, tie-off, crank-up tower, guy line, turnbuckle, safety wire, utility pole.

Math: none.

### Part 2 — RF exposure safety
**T0C — RF radiation and FCC exposure rules (13: T0C01–T0C13)**
Topics: radiation type (2: T0C01, T0C12), MPE & frequency (2: T0C02, T0C05), duty cycle (3: T0C03, T0C10, T0C11), exposure factors/reduction & RF burn (3: T0C04, T0C07, T0C08), compliance methods/responsibility (3: T0C06, T0C09, T0C13).

Beginner must understand:
- Radio signals are **non-ionizing radiation** (T0C01): RF photons **do not have enough energy to cause chemical changes in cells or damage DNA**, unlike X-rays/radioactivity (T0C12). RF's hazard is **heating** (and shocks/burns), not mutation.
- Limits vary with frequency because **the human body absorbs more RF energy at some frequencies than others** (T0C05). **FACT: of the listed bands, 50 MHz (6 m) has the lowest MPE** (T0C02) — the body absorbs best near its own resonant region; memorize 50 MHz as the strictest.
- **Duty cycle** = the **percentage of time the transmitter is actually transmitting** (T0C11); it matters because exposure limits are about **average** exposure (T0C10). **FACT: dropping from 100% to 50% duty cycle doubles the allowable power density (factor of 2)** (T0C03 — see Math).
- Exposure depends on **frequency, power level, distance from the antenna, and the antenna's radiation pattern** — all (T0C04). To reduce exposure: **relocate antennas** away from people (T0C08) — distance is the cheapest fix. Touching an antenna while transmitting causes an **RF burn** to the skin (T0C07).
- Compliance is the **station licensee's** responsibility (T0C13); acceptable evaluation methods are **calculation per FCC OET Bulletin 65, computer modeling, or measurement with calibrated field-strength equipment** — all valid (T0C06); **re-evaluate whenever anything in the transmitter or antenna system changes** (T0C09).

Common confusions (T0C):
- Non-ionizing ≠ harmless: "perfectly safe" (T0C12 distractor) is wrong — heating and RF burns are real.
- Lowest MPE is at 50 MHz, *not* the highest frequency listed (T0C02) — most-missed fact in T0C.
- Duty cycle lowers *average* exposure; peak exposure is unchanged (T0C10 distractor).
- Increasing duty cycle *increases* exposure — T0C08's distractor has it backwards; relocating antennas is the correct action.

Vocabulary: non-ionizing vs ionizing radiation, MPE (maximum permissible exposure), power density, duty cycle, averaging time, RF burn, RF exposure evaluation, OET Bulletin 65, controlled/uncontrolled environment (chapter context term), field-strength measurement.

### T0 Math — duty cycle and exposure
- **Allowable power density scales inversely with duty cycle**: halving the transmit-time fraction doubles the limit.
- Worked example (the pool's own numbers, T0C03): duty cycle 100% → 50% means transmitting half as much per averaging window, so allowable power density **increases by a factor of 2** (not 50%, not 3× — those are the distractors).
- Quick practice for the chapter: an operator who transmits 30 s every 5 minutes has duty cycle = 30/300 = **10%** → allowable density ×10 vs continuous. (Skill: duty cycle = transmit time / total time, T0C11's definition in numbers.)

Watch items (T0 FACT lines): black wire = hot; fuse in series with hot only; arrester at grounded entry panel; bond all ground rods; filter capacitors stay charged after power-off; 8-ft rods per tower leg, bonded; never climb alone; falling antenna ≥ 10 ft from power lines; local codes govern grounding; RF = non-ionizing; 50 MHz = lowest MPE; 100%→50% duty cycle = ×2 power density; licensee responsible; re-evaluate after any station change.

---

## Cross-cutting notes for chapter writers
- **"All these choices are correct" is the key 18 times** in T6–T0: T6A10, T6B11; T7B03, T7B08, T7B10; T8B03, T8B04, T8D01, T8D03, T8D08, T8D10; T9B01, T9B08; T0A02, T0A06, T0B02, T0C04, T0C06. But it is also *offered as a trap* 16 times — T0A01, T0A04, T0B01, T0B04, T0B07, T0B09, T0C07, T0C08, T6C12, T6D07, T7A10, T7B06, T7D07, T8B01, T8B06, T8C02 — so teach students to verify each option, never auto-pick it.
- **Surprising/ambiguous IDs to handle explicitly**: T6C10 (correct answer's distractor is the adjacent real component 2 in T-3); T6A09 (a *T6A* question that tests Figure T-2 — figure questions live in three groups); T7B09 (first cable-TV step is checking connectors, not adding filters); T7D10 (ohmmeter across a discharged capacitor reads *rising* resistance — counterintuitive); T8B10 (2026 answer adds "~100 minutes" period to LEO — new vs older pools); T8D01 (IEEE 802.11 counts as a digital mode); T9A08 (the only antenna-length number in T9; no calculation required but math above explains it); T0C02 (50 MHz lowest MPE — defies "higher frequency = stricter" intuition); T0C03 (only true arithmetic in T6–T0 besides T9's implicit wavelength).
- **Math total for T6–T0 is minimal**: one formula (λ = 300/f) plus duty-cycle scaling; every other numeric is a memorized FACT (bandwidths, 50 Ω, 1:1, 150 Hz, 100 min, 10 ft, 50 MHz).
- Glossary candidates are collected per group under "Vocabulary" above; roughly 120 terms across the five subelements.

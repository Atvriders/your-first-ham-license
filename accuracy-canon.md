# Accuracy Canon — Your First Ham License: The Technician Course (2026–2030)

**This file is LAW.** It is the single, binding source of truth for *Your First Ham License: The Technician Course (2026–2030)*. Every chapter writer, figure author, appendix writer, and auditor conforms to it exactly: pool wording, numbers, dates, notation, terminology, chapter mapping, and copyright reproducibility are governed here and nowhere else. Where a claim was ever contested during research, this file states the one resolved value the book will use and cites it; disagreements with any draft chapter are resolved in favour of this canon, not the chapter. Every uncertainty flagged during research has been closed to a sourced value or a deliberately careful wording in **§7 Resolved Uncertainties** — there are no open placeholders in this document, and the automated build audit greps this file to confirm it.

Companion canonical data (part of this canon by reference): `canon/pool-technician.txt` and `canon/pool-technician.json` — the verified 409-question NCVEC 2026–2030 Technician pool. Question text, choices, and answer letters are quoted from those two files only, never from memory, web mirrors, or third-party study guides.

---

## 1. Pool Summary & Revision Record

### 1.1 Canonical pool files (the only quoting sources)

| File | Bytes | sha256 |
|---|---:|---|
| `canon/pool-technician.txt` | 109,214 | `0796b92ebdfe341de22437ba6c185f5cb91c010e58f6ac1f41c05e2a0de90f1b` |
| `canon/pool-technician.json` | 170,569 | `cced9eb89f74f56cd5f195c3b4dd7e10ec09eb66238c1134f269821055a27918` |

The `.txt` is the human-readable, byte-exact rendering (ID lines `T1A01 (C) [97.1]`, one line per question and per choice, `~~` separators, published subelement/group headings). The `.json` is the structured form: top-level object keyed by question id; each entry has `group`, `subelement`, `question`, `choices` (exactly "A"–"D"), `answer` (one of "A"–"D"), `figure` (null, or "T-1"/"T-2"/"T-3"). Part 97 references live only on the `.txt` ID lines.

### 1.2 Provenance (verified source downloads)

Landing page: <https://ncvec.org/index.php/2026-2030-technician-question-pool> ("2026-2030 Technician Pool and Syllabus Public Release Feb 19 2026"). Downloaded 2026-07-23 into `canon/source/`:

| File | Bytes | sha256 |
|---|---:|---|
| `canon/source/ncvec-2026-2030-technician-pool-feb19-2026.docx` | 489,983 | `c3bb9ebf46730a9812ae854d12a93f07b7a38f521441e51c451e917ccb9e3a54` |
| `canon/source/ncvec-2026-2030-technician-pool-feb19-2026.pdf` | 480,239 | `3618649d64df77f2cf217fa79ef82094fe5d2d41b26d20ce08c46ca1c3d5055a` |
| `canon/source/ncvec-2026-2030-technician-pool-3-diagrams.pdf` | 278,003 | `0b2f636a399100ab42a929328e187cef925d6d50666599ad58aff318cd81147c` |
| `canon/source/diagram-t1.jpg` | 115,824 | `7e5f000404feeae942c625a773f0a02c3ee3b5bafda2218d6b8b0d3653288462` |
| `canon/source/diagram-t2.jpg` | 140,293 | `36313bc65ea22bd483e9b0ff2cd8e7dbce3784e2b009046879d8e5959cc9ebf7` |
| `canon/source/diagram-t3.jpg` | 108,532 | `6db1d838f067ecd00a1ee8ad1e396c9e4d4415cfbc75764169a7bc868e44dc52` |

Extraction and cross-check (full evidence in `canon/ingestion-report.md`): the canonical text was parsed from the `.docx` (logical paragraphs, byte-exact wording) and independently re-parsed from the `.pdf` with `pdftotext -layout`; the two agreed on all 409 questions, all 1,636 choices, all answer letters, and all headings except one PDF-side line-wrap artifact (T9A04 "quarter- wave"). The `.docx` is authoritative; the canonical files carry `quarter-wave`. ARRL hosts no separate copy of this pool (its question-pools page links back to NCVEC), so the docx-vs-pdf double parse is the cross-check of record. Normalization preserved published Unicode punctuation byte-exactly (curly quotes U+2019/U+201C/U+201D; en dash U+2013 in headings) and the published ID-line form verbatim — including `T1D12 (A)[97.119(a)]` with no space before the bracket, and the citation typo on T1D09 (see §7.3). Neither is ever "fixed" in quotation.

### 1.3 Structure, counts, and revision record

- **Total: 409 questions**, 10 subelements (T1–T9, T0), **35 groups**. No duplicate ids; numbering contiguous within every group; every question has exactly 4 choices A–D and one keyed answer.
- **The exam: 35 questions, one drawn from each of the 35 groups; 26 correct answers required to pass** (47 CFR §97.503(a); pool structure per canonical counts).
- **Validity: exams from 2026-07-01 through 2030-06-30** (four-year rotation; General pool runs 2023-07-01 → 2027-06-30, Extra 2024-07-01 → 2028-06-30).
- **Released 2025-12-18**: the NCVEC Question Pool Committee released the pool into the **public domain** on December 18, 2025.
- **Revised 2026-02-19**: an errata issued February 19, 2026 modified 4 questions; the published pool body already incorporates the changes (verified byte-exact against the errata sheet during ingestion). The revised questions, which this book always uses in their revised form:

| ID | Answer | Revised question text |
|---|---|---|
| T1C01 | D | For which classes of amateur radio licenses does the FCC currently issue new licenses? (keyed answer: "Technician, General, Amateur Extra") |
| T5A05 | A | A difference in which of the following causes electron flow? (keyed answer: "Voltage") |
| T7A09 | B | What is the function of the switch which selects either SSB or CW-FM on some VHF power amplifiers? (keyed answer: "Set the amplifier for proper operation in the selected mode") |
| T0A10 | A | What hazard exists when rapidly charging or discharging an unprotected battery? (keyed answer: "Overheating or out-gassing") |

Per-subelement counts (match the syllabus claims printed in the source document; exam weight = one question per group):

| Subelement | Title (as published) | Questions | Groups | Per-group counts | Exam questions |
|---|---|---:|---:|---|---:|
| T1 | Commission's Rules | 68 | 6 | T1A:11 T1B:12 T1C:11 T1D:12 T1E:11 T1F:11 | 6 |
| T2 | Operating Procedures | 37 | 3 | T2A:11 T2B:14 T2C:12 | 3 |
| T3 | Radio Wave Propagation | 35 | 3 | T3A:12 T3B:12 T3C:11 | 3 |
| T4 | Amateur Radio Practices | 23 | 2 | T4A:12 T4B:11 | 2 |
| T5 | Electrical Principles | 50 | 4 | T5A:11 T5B:13 T5C:12 T5D:14 | 4 |
| T6 | Electronic and Electrical Components | 46 | 4 | T6A:11 T6B:12 T6C:12 T6D:11 | 4 |
| T7 | Practical Circuits | 44 | 4 | T7A:11 T7B:11 T7C:11 T7D:11 | 4 |
| T8 | Signals and Emissions | 47 | 4 | T8A:12 T8B:12 T8C:11 T8D:12 | 4 |
| T9 | Antennas and Feed Lines | 23 | 2 | T9A:11 T9B:12 | 2 |
| T0 | Safety | 36 | 3 | T0A:12 T0B:11 T0C:13 | 3 |
| **Total** | | **409** | **35** | | **35** |

### 1.4 Pool figures T-1, T-2, T-3 (12 questions) and the redraw rule

Twelve questions reference the pool's three schematic diagrams; all other 397 carry no figure. The book **redraws each figure as an original SVG conveying exactly the official content — same components, same labels, same numbered callouts — never copies the published graphics**. Redrawn figures are registered in `figures/figures.json` as `kind:"original"` with the note "redrawn from NCVEC pool figure T-x". The pool is public domain, so this is both safe and faithful; the redraw rule exists so the book's visual style stays consistent and themeable.

| Figure | Source image | Referenced by |
|---|---|---|
| T-1 (transistor lamp-switch) | `canon/source/diagram-t1.jpg` | T6C02, T6C03, T6C04, T6C05, T6D10 |
| T-2 (AC power supply) | `canon/source/diagram-t2.jpg` | T6A09, T6C06, T6C07, T6C08, T6C09 |
| T-3 (antenna tuner / transmatch) | `canon/source/diagram-t3.jpg` | T6C10, T6C11 |

**Style common to all three redraws:** black-and-white line schematic on white, bold sans-serif component labels, "Figure T-1/2/3" caption centered beneath the drawing, and — important corrected detail — **every ground symbol is drawn as three slanted (diagonal) strokes of decreasing length, longest on top**, not the classic horizontal shrinking lines.

**Figure T-1 — transistor lamp-switch circuit** (left to right, roughly centered):
- Far left: an unnumbered two-position switch — two open-circle contacts stacked vertically, each with a short leftward stub ending in a two-pronged fork (two angled arms, like a sideways "Y"). Upper contact wired right to component 1; lower contact wired straight down to ground symbol 5.
- **1 = resistor**: horizontal zigzag, series between the switch's upper contact and the transistor base lead; label "1" above. (Asked by T6C02.)
- **2 = NPN transistor**: circle containing a thick vertical base bar on its left half; base lead enters horizontally from the left; collector line exits the circle top and runs up to the lamp wire; emitter line exits the circle bottom with a **filled arrowhead pointing outward/down-right** and runs down to a ground symbol; label "2" above the circle. (Identity asked by T6C03; function — "control the flow of current" — asked by T6D10.)
- **3 = lamp**: arch/dome (semicircular loop) symbol on the top horizontal wire between the collector line and the battery top; label "3" above. (T6C04.)
- **4 = battery**: two cell pairs — four horizontal plates alternating long/short — at the right; top to the lamp wire, bottom to a ground symbol; label "4" right of the plates. (T6C05.)
- **5 = ground symbol** (three slanted strokes) beneath the switch's lower contact; label "5" below. Not directly asked. Unnumbered identical grounds also sit under the transistor emitter and the battery.
- Circuit story: closing the switch lets base current flow through resistor 1; the transistor then conducts, switching battery current through the lamp.

**Figure T-2 — AC power supply** (left block = primary loop; right block = DC side; grounds along the bottom):
- **1 = AC voltage source**: circle with two thick horizontal filled bars inside, on the left vertical leg of the primary loop; label "1" right of it. Not asked.
- **2 = fuse**: small open rectangle, series in the top wire of the primary loop; label "2" above. Not asked.
- **3 = SPST switch**: two open-circle contacts with a single angled blade hinged at the left contact, blade tip raised toward the right contact (drawn open), series in the top primary wire; label "3" above. (T6A09 asks its type: single-pole single-throw.)
- **4 = transformer**: primary coil (3 humps), two parallel vertical core lines, secondary coil (4 humps); primary closes the left loop to source 1; secondary bottom grounded, secondary top feeds component 5; label "4" above the core lines. (T6C09.)
- **5 = rectifier diode**: filled triangle pointing right into a vertical bar (anode left, cathode right), series in the top DC rail; label "5" above. Not asked.
- **6 = capacitor**: straight horizontal top plate, curved-upward bottom plate (polarized style), shunt from top rail to ground; label "6" left of it. (T6C06.)
- **7 = resistor**: vertical zigzag from the top rail down to component 8 (series indicator branch); label "7" left. Not asked.
- **8 = LED**: filled diode triangle pointing DOWN into a horizontal bar, with two small arrows pointing away down-right (light); bottom of branch grounded; label "8" left. (T6C07.)
- **9 = variable resistor**: zigzag in the top rail with a diagonal arrow touching it from below; the arrow's tail wire runs right and joins the rail at the resistor's right end (rheostat style); filled dots mark the rail nodes on both sides; label "9" above. (T6C08.)
- **10 = Zener diode**: filled diode triangle pointing UP with a bent "Z-shaped" cathode bar on top, shunt from top rail to ground; label "10" left. Not asked in any figure question, but name it when teaching — it appears as a distractor elsewhere (T6D07, T6D08).
- Far right: open-circle output terminal on the top rail. Ground symbols under the secondary, component 6, the 7+8 branch, and component 10.
- Circuit story: wall AC (1) → fuse (2) → switch (3) → transformer steps down (4) → diode rectifies (5) → capacitor smooths (6) → resistor+LED power indicator (7, 8) → variable resistor (9) → Zener regulates (10) → output.

**Figure T-3 — antenna tuner (transmatch), T-network**:
- Horizontal signal path across the upper third: **[1] → [2] → junction dot → unnumbered second variable capacitor → wire right, then up to [4]**.
- **1 = connector**: curly-brace "{"-style coax-connector symbol at the far left on the input line (this is where the transmitter connects); label "1" left of it. Not asked.
- **2 = variable capacitor**: two vertical plates with a diagonal arrow through them (arrowhead upper right), series in the top line; label "2" above. Not asked — but it is the trap answer in T6C10.
- Junction: filled dot after component 2; a vertical branch goes down to component 3; the top line continues through the second (unnumbered) variable capacitor, then turns up to the antenna.
- **3 = variable inductor**: vertical coil (4 humps) from the junction dot downward, with a filled arrowhead tap pointing left into the coil's mid-region; the tap wire runs right, then down, then left to a second filled dot at the coil bottom (shorting the lower turns — adjustable inductance), which continues down to a ground symbol; label "3" left of the coil. (T6C10 — answer: variable inductor.)
- **4 = antenna**: outline inverted triangle (apex down) at the top right, apex joined to the vertical feed wire; label "4" above. (T6C11 — answer: antenna.)
- Circuit story: two adjustable capacitors with an adjustable inductor to ground form a "T" matching network between the transmitter connector and the antenna — the picture of the antenna tuner taught in T9B04.

### 1.5 Quoting discipline (audit-enforced)

- Question text, choice text, and answer letters are quoted **only** from the two canonical pool files, byte-exact (the audit compares whitespace-normalized). Published Unicode punctuation (curly apostrophes/quotes) is preserved, never converted to ASCII.
- Chapter and appendix pool quotes use this exact block markup (the audit parses it):

```
> **T1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: C** — one-line why.
```

- Every quoted id must exist in the pool; every stated choice line and the stated answer letter must match the pool key. Appendix A quotes all 409 ids exactly once, in canonical pool order (T1…T9, T0; group A–F; number).
- The pool's own published quirks are reproduced as published, never silently repaired: the T1D09 ID-line citation typo (§7.3) and the T1D12 missing space before the bracket.

---

## 2. Pinned Facts with Sources

The book's fact reservoir. Each line is `- **FACT:** <one self-contained sentence> — Source: <§ or URL>`. Chapter writers copy the sentence **verbatim** into their chapters (the build audit greps each chapter's `**FACT:**` lines for an exact match in this file); a chapter may add explanation around it but may never alter the sentence. Every sentence stands alone, needs no surrounding context to be true, and is safe for a beginner to memorize. Rule quotations inside FACT sentences are verbatim from the eCFR text of 47 CFR Part 97, issue date 2026-07-21 (pulled 2026-07-23; re-pull before any 2027+ reprint — see §7.15). Where a rule quotation is embedded mid-sentence, the initial letter's case and the terminal punctuation may be adjusted to fit the host sentence (standard embedded-quote convention); the quoted words themselves are verbatim from the cited section.

### 2.1 Purpose and rules of the service

- **FACT:** The basis and purpose of the Amateur Radio Service is stated in five prongs in FCC rule §97.1: emergency communications, advancing the radio art, advancing skills in both the communication and technical phases of the art, expanding the reservoir of trained operators and technicians, and enhancing international goodwill. — Source: 47 CFR §97.1(a)–(e)
- **FACT:** The first prong of the basis and purpose of the Amateur Radio Service is "Recognition and enhancement of the value of the amateur service to the public as a voluntary noncommercial communication service, particularly with respect to providing emergency communications." — Source: 47 CFR §97.1(a)
- **FACT:** The second prong of the basis and purpose of the Amateur Radio Service is "Continuation and extension of the amateur's proven ability to contribute to the advancement of the radio art." — Source: 47 CFR §97.1(b)
- **FACT:** The third prong of the basis and purpose of the Amateur Radio Service is "Encouragement and improvement of the amateur service through rules which provide for advancing skills in both the communication and technical phases of the art." — Source: 47 CFR §97.1(c)
- **FACT:** The fourth prong of the basis and purpose of the Amateur Radio Service is "Expansion of the existing reservoir within the amateur radio service of trained operators, technicians, and electronics experts." — Source: 47 CFR §97.1(d)
- **FACT:** The fifth prong of the basis and purpose of the Amateur Radio Service is "Continuation and extension of the amateur's unique ability to enhance international goodwill." — Source: 47 CFR §97.1(e)
- **FACT:** The FCC (Federal Communications Commission) is the agency that regulates and enforces the rules for the Amateur Radio Service in the United States. — Source: 47 CFR §97.1 preamble; §97.3(a)(21); pool T1A02
- **FACT:** A space station is "an amateur station located more than 50 km above the Earth's surface." — Source: 47 CFR §97.3(a)(41); pool T1A07
- **FACT:** A frequency coordinator is "an entity, recognized in a local or regional area by amateur operators whose stations are eligible to be auxiliary or repeater stations, that recommends transmit/receive channels and associated operating and technical parameters for such stations in order to avoid or minimize potential interference." — Source: 47 CFR §97.3(a)(22); pool T1A08, T1A09
- **FACT:** A control operator is "an amateur operator designated by the licensee of a station to be responsible for the transmissions from that station to assure compliance with the FCC Rules." — Source: 47 CFR §97.3(a)(13); pool T1E11
- **FACT:** A control point is "the location at which the control operator function is performed." — Source: 47 CFR §97.3(a)(14); pool T1E05
- **FACT:** Automatic control is "the use of devices and procedures for control of a station when it is transmitting so that compliance with the FCC Rules is achieved without the control operator being present at a control point." — Source: 47 CFR §97.3(a)(6); pool T1E08
- **FACT:** Remote control is "the use of a control operator who indirectly manipulates the operating adjustments in the station through a control link to achieve compliance with the FCC Rules," and operating a station over the internet is remote control. — Source: 47 CFR §97.3(a)(39); pool T1E10
- **FACT:** Broadcasting is defined as "transmissions intended for reception by the general public, either direct or relayed." — Source: 47 CFR §97.3(a)(10); pool T1D10
- **FACT:** Third-party communications are "a message from the control operator (first party) of an amateur station to another amateur station control operator (second party) on behalf of another person (third party)." — Source: 47 CFR §97.3(a)(47); pool T1F08
- **FACT:** A repeater is "an amateur station that simultaneously retransmits the transmission of another amateur station on a different channel or channels." — Source: 47 CFR §97.3(a)(40); pool T1F09
- **FACT:** A beacon is "an amateur station transmitting communications for the purposes of observation of propagation and reception or other related experimental activities." — Source: 47 CFR §97.3(a)(9)
- **FACT:** An auxiliary station is "an amateur station, other than in a message forwarding system, that is transmitting communications point-to-point within a system of cooperating amateur stations." — Source: 47 CFR §97.3(a)(7); pool T1D07
- **FACT:** Peak envelope power (PEP) is "the average power supplied to the antenna transmission line by a transmitter during one RF cycle at the crest of the modulation envelope taken under normal operating conditions." — Source: 47 CFR §97.3(b)(9)
- **FACT:** Five classes of amateur operator license exist in the rules — Novice, Technician, General, Advanced, and Amateur Extra — but the FCC currently issues new licenses only for Technician, General, and Amateur Extra. — Source: 47 CFR §97.9(a), §97.17(a); pool T1C01 (as revised 2026-02-19)
- **FACT:** When transmitting, each amateur station must have a control operator — there is no exception, not even for automatically controlled stations. — Source: 47 CFR §97.7; pool T1E01
- **FACT:** Your operating authority begins when your license grant appears in the FCC's ULS consolidated license database — passing the exam alone does not authorize you to transmit. — Source: 47 CFR §97.7(a); pool T1A05, T1C10
- **FACT:** The station licensee must designate the station's control operator, and the FCC presumes the licensee is the control operator unless station records document otherwise. — Source: 47 CFR §97.103(b); pool T1E03
- **FACT:** A station may only be operated in the manner and to the extent permitted by the privileges of the control operator's license class — the control operator's class, not the station licensee's, sets the limits. — Source: 47 CFR §97.105(b); pool T1E04
- **FACT:** A Technician may never be the control operator of a station transmitting in an Amateur Extra–only segment (emergencies aside), because a station's privileges are those of its control operator. — Source: 47 CFR §97.301, §97.105(b); pool T1E06
- **FACT:** When the control operator is a different amateur operator than the station licensee, both persons are equally responsible for proper operation of the station. — Source: 47 CFR §97.103(a); pool T1E07
- **FACT:** FCC rules always apply to an amateur station — including during RACES, ARES, and FEMA operations. — Source: 47 CFR §97.103(a); pool T2C01
- **FACT:** Any amateur station may be remotely controlled, but only stations specifically designated in Part 97 (such as repeaters, beacons, auxiliary, and space stations) may be automatically controlled. — Source: 47 CFR §97.109(c), §97.109(d); pool T1E09
- **FACT:** A repeater may be automatically controlled, and repeater operation is the pool's canonical example of automatic control. — Source: 47 CFR §97.205(d); pool T1E08
- **FACT:** The licensee must make the station and the station records available for inspection upon request by an FCC representative — at any time upon request, with no warrant or advance notice required. — Source: 47 CFR §97.103(c); pool T1F01
- **FACT:** Every amateur station (except a space or telecommand station) must transmit its assigned call sign "at the end of each communication, and at least every 10 minutes during a communication." — Source: 47 CFR §97.119(a); pool T1F03
- **FACT:** A tactical call sign (such as "Race Headquarters") may be used for convenience but never substitutes for the FCC-assigned call sign, which must still be transmitted every 10 minutes and at the end of each communication. — Source: 47 CFR §97.119(a); pool T1F02
- **FACT:** No station may transmit unidentified communications or signals, so even brief on-the-air test transmissions must identify with the station's call sign. — Source: 47 CFR §97.119(a); pool T1D12
- **FACT:** Station identification by phone emission must be in the English language, and use of a phonetic alphabet as an aid to correct identification is encouraged — encouraged, not required. — Source: 47 CFR §97.119(b)(2); pool T1A03, T1F04
- **FACT:** The required station identification may be sent by CW or by phone emission in English — either satisfies the rule for phone operation. — Source: 47 CFR §97.119(b)(1)–(2); pool T1F05
- **FACT:** Self-assigned indicators are permitted when separated from the call sign by the slant mark (/) or any suitable word denoting it — "stroke," "slant," and "slash" are all acceptable spoken separators. — Source: 47 CFR §97.119(c); pool T1F06
- **FACT:** Transmissions directed only to controlling a model craft are exempt from station identification provided a label with the call sign and the licensee's name and address is affixed to the transmitter, the control signals are not considered obscuring codes, and transmitter power must not exceed 1 W. — Source: 47 CFR §97.215(a)–(c); pool T1D11
- **FACT:** "No amateur operator shall willfully or maliciously interfere with or cause interference to any radio communication or signal." — Source: 47 CFR §97.101(d); pool T1A11
- **FACT:** Amateur stations may not exchange communications with any country "whose administration has notified the ITU that it objects to such communications." — Source: 47 CFR §97.111(a)(1); pool T1D01
- **FACT:** "An amateur station shall not engage in any form of broadcasting, nor may an amateur station transmit one-way communications except as specifically provided in these rules." — Source: 47 CFR §97.113(b); pool T1D02
- **FACT:** Amateur stations may not transmit "messages encoded for the purpose of obscuring their meaning"; the tested exceptions are telecommand to space stations and control signals to model craft. — Source: 47 CFR §97.113(a)(4), §97.211(b), §97.215(b); pool T1D03
- **FACT:** Music using a phone emission is prohibited except when incidental to an authorized retransmission of manned spacecraft communications, which requires prior NASA approval. — Source: 47 CFR §97.113(a)(4), §97.113(c); pool T1D04
- **FACT:** An amateur operator "may notify other amateur operators of the availability for sale or trade of apparatus normally used in an amateur station, provided that such activity is not conducted on a regular basis." — Source: 47 CFR §97.113(a)(3)(ii); pool T1D05
- **FACT:** Obscene or indecent words or language are prohibited in any amateur transmission, and there is no FCC list of prohibited words — the prohibition is categorical. — Source: 47 CFR §97.113(a)(4); pool T1D06
- **FACT:** A control operator "may accept compensation as an incident of a teaching position during periods of time when an amateur station is used by that teacher as a part of classroom instruction at an educational institution" — the only tested case where compensation for operating is allowed. — Source: 47 CFR §97.113(a)(3)(iii); pool T1D08
- **FACT:** Amateur stations may transmit information supporting broadcasting, program production, or news gathering only when the communications are "directly related to the immediate safety of human life or the protection of property" and no other means of communication is reasonably available. — Source: 47 CFR §97.113(b); pool T1D09
- **FACT:** Only auxiliary, repeater, or space stations may automatically retransmit the radio signals of other amateur stations. — Source: 47 CFR §97.113(d); pool T1D07
- **FACT:** International amateur communications are "limited to communications incidental to the purposes of the amateur service and to remarks of a personal character." — Source: 47 CFR §97.117; pool T1C03
- **FACT:** Third-party traffic with a foreign station is allowed only when that country's "administration has made arrangements with the United States to allow amateur stations to be used for transmitting international communications on behalf of third parties." — Source: 47 CFR §97.115(a)(2); pool T1F07
- **FACT:** "At all times and on all frequencies, each control operator must give priority to stations providing emergency communications" (except RACES training drills and tests). — Source: 47 CFR §97.101(c)
- **FACT:** No provision of the FCC rules prevents an amateur station from using any means of radiocommunication at its disposal to provide essential communication needs in connection with the immediate safety of human life and immediate protection of property when normal communication systems are not available. — Source: 47 CFR §97.403; pool T2C09
- **FACT:** A station in distress may use "any means at its disposal to attract attention, make known its condition and location, and obtain assistance." — Source: 47 CFR §97.405(a)
- **FACT:** To be the control operator of a RACES station you must hold an FCC-issued amateur operator license and be "certified by a civil defense organization as enrolled in that organization." — Source: 47 CFR §97.407(a); pool T1A10
- **FACT:** RACES drills and tests "may not exceed a total time of 1 hour per week," except up to 72 hours no more than twice per calendar year with state approval. — Source: 47 CFR §97.407(d)(4)
- **FACT:** An amateur station on a ship or aircraft may be installed and operated only with the approval of the master of the ship or pilot in command of the aircraft. — Source: 47 CFR §97.11(a); pool T1C06
- **FACT:** When two repeaters interfere with each other, the licensees share responsibility for resolving it — unless one repeater's operation is recommended by a frequency coordinator and the other's is not, in which case the licensee of the non-coordinated repeater has primary responsibility. — Source: 47 CFR §97.205(c)
- **FACT:** The control operator of a repeater that inadvertently retransmits communications that violate the rules is not accountable for the violative communications — accountability falls on the originating station's control operator. — Source: 47 CFR §97.205(g); pool T1F10
- **FACT:** A club station license grant requires a trustee holding an operator/primary grant, and "the club must be composed of at least four persons and must have a name, a document of organization, management, and a primary purpose devoted to amateur service activities consistent with this part." — Source: 47 CFR §97.5(b)(2); pool T1F11
- **FACT:** Every license grant must show the grantee's correct name, mailing address, and email address, and "revocation of the station license or suspension of the operator license may result when correspondence from the FCC is returned as undeliverable because the grantee failed to provide the correct email address." — Source: 47 CFR §97.23; pool T1C04

### 2.2 Licensing process (exam → grant)

- **FACT:** The Technician class license requires passing examination Element 2 only; General requires Elements 2 and 3; Amateur Extra requires Elements 2, 3, and 4. — Source: 47 CFR §97.501
- **FACT:** Element 2 is "35 questions concerning the privileges of a Technician Class operator license. The minimum passing score is 26 questions answered correctly." — Source: 47 CFR §97.503(a)
- **FACT:** Element 3 (General) is 35 questions with 26 correct to pass, and Element 4 (Amateur Extra) is 50 questions with 37 correct to pass. — Source: 47 CFR §97.503(b)–(c)
- **FACT:** The 2026–2030 Element 2 exam is built as 35 questions drawn one per group from the pool's 35 groups, out of a 409-question pool. — Source: `canon/pool-technician.json` (verified counts)
- **FACT:** "Each examination for an amateur operator license must be administered by a team of at least 3 VEs at an examination session coordinated by a VEC." — Source: 47 CFR §97.509(a)
- **FACT:** To administer a Technician exam, each volunteer examiner must be accredited by the coordinating VEC, be at least 18 years old, hold an Amateur Extra, Advanced, or General class license, and never have had an amateur license revoked or suspended. — Source: 47 CFR §97.509(b)
- **FACT:** VEs must grade each examination element immediately upon completion (for remotely administered exams, at the earliest practical opportunity), and the VEs alone determine the correctness of the examinee's answers. — Source: 47 CFR §97.509(h)
- **FACT:** When an examinee passes, three VEs certify that the examinee is qualified for the license grant, and the VEs must issue a Certificate of Successful Completion of Examination (CSCE). — Source: 47 CFR §97.509(i), (l)
- **FACT:** When an examinee fails an element, the VEs must return the application document to the examinee and inform the examinee of the grade. — Source: 47 CFR §97.509(j)
- **FACT:** No compromised examination may be administered, and the same question set may never be re-administered to the same examinee. — Source: 47 CFR §97.509(f)
- **FACT:** Under ARRL VEC retest policy, a failed element may be retaken at the same session only if the team has a different version of that element the applicant has not taken, the team has the time, resources, and willingness, and the applicant pays an additional test fee. — Source: ARRL Volunteer Examiner Manual, "Retesting," http://www.arrl.org/files/file/VEs/VE%20Manual%20Web%20Final%202022.pdf
- **FACT:** Nothing in FCC rules entitles a failed candidate to an immediate retest — offering a second (different-version) exam at the same session is entirely the VE team's decision. — Source: Laurel VEC FAQ, https://larc-vec.org/faq.php
- **FACT:** The 2026 ARRL VEC exam session fee is $15.00, and that one fee pays for one attempt at each of the three exam elements. — Source: ARRL VEC Exam Fees, http://www.arrl.org/arrl-vec-exam-fees (calendar-2026 figure, verified 2026-07-23; re-verify each January — see §7.14)
- **FACT:** Candidates younger than 18 pay a reduced $5 ARRL VEC exam session fee, and ARRL's Youth Licensing Grant Program reimburses the one-time $35 FCC application fee for new-license candidates under 18 who test under the ARRL VEC program. — Source: ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session (verified 2026-07-23; re-verify each January — see §7.14)
- **FACT:** Exam candidates must present one legal photo ID (such as a state driver's license, government passport, military ID, or student school photo ID) or, if none, two forms of non-photo ID (such as a birth certificate with seal or a Social Security card). — Source: ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session
- **FACT:** Every applicant must answer the Basic Qualification Question (felony conviction status) on the application form, and a "YES" answer triggers additional FCC procedures. — Source: ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session
- **FACT:** The NCVEC Quick-Form 605 is the standard exam-session application: the applicant completes Section 1 (email address and FRN are mandatory), the three administering VEs print, sign, and date Section 2, and the form goes to the coordinating VEC — never directly to the FCC. — Source: ARRL, NCVEC 605 Instructions, http://www.arrl.org/605-instructions
- **FACT:** The current NCVEC Form 605 is the 2022 edition. — Source: NCVEC, https://www.ncvec.org/downloads/NCVEC_Form_605_2022.pdf (verified 2026-07-23; check ncvec.org for a newer revision before publication — see §7.14)
- **FACT:** Amateur exams are offered both in person and as remote video-supervised online sessions, and availability of remote testing depends entirely on the individual VE team. — Source: ARRL, Find an Amateur Radio License Exam Session, http://www.arrl.org/find-an-amateur-radio-license-exam-session; Laurel VEC FAQ (Laurel runs in-person exams only), https://larc-vec.org/faq.php
- **FACT:** After a successful exam the VEs submit the application to the coordinating VEC, which screens the information, resolves discrepancies, and forwards all required data to the FCC electronically. — Source: FCC, Volunteer Examiner Coordinators, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/volunteer-examiner-coordinators; 47 CFR §97.519(b)(3)
- **FACT:** VECs and VEs "may be reimbursed by examinees for out-of-pocket expenses incurred in preparing, processing, administering, or coordinating an examination" — this is the legal basis for exam session fees. — Source: 47 CFR §97.527
- **FACT:** A typical ARRL VEC exam session tests about ten people and lasts about three and a half hours. — Source: ARRL Volunteer Examiner Manual, http://www.arrl.org/files/file/VEs/VE%20Manual%20Web%20Final%202022.pdf
- **FACT:** An FRN (FCC Registration Number) is a 10-digit number assigned to a business or individual registering with the FCC, used to identify all of the registrant's business dealings with the FCC. — Source: FCC CORES FAQ, https://apps.fcc.gov/cores/html/know.html
- **FACT:** FRNs are obtained by registering in CORES (COmmission REgistration System) with an FCC username account, and an FRN registered online is available immediately. — Source: FCC CORES FAQ, https://apps.fcc.gov/cores/html/know.html
- **FACT:** Exam candidates are required to register in CORES and have their FRN before exam day, and the Social Security number is given to the FCC inside CORES registration — it does not go on the exam form. — Source: ARRL, Find an Amateur Radio License Exam Session; ARRL, What to Bring to an Exam Session
- **FACT:** Registering in CORES to get your FRN carries no fee and no exam requirement. — Source: canonical safe wording per §7.2 (no payment step exists in the CORES registration flow; FCC CORES FAQ, https://apps.fcc.gov/cores/html/know.html)
- **FACT:** A valid email address is mandatory on the license application form because the FCC sends all correspondence — including the official copy of the license — by email. — Source: ARRL, What to Bring to an Exam Session, http://www.arrl.org/what-to-bring-to-an-exam-session; 47 CFR §97.23
- **FACT:** The FCC charges a $35 application fee, effective April 19, 2022, on applications for a new license, a renewal, a rule waiver, or a modification requesting a new vanity call sign — per application. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (verified 2026-07-23 against arrl.org, the Laurel VEC FAQ, and the FCC fee-schedule page; re-verify before each reprint — see §7.14)
- **FACT:** License upgrades to a higher operator class, administrative updates (name, mailing or email address), requests for a sequentially issued call sign, and license cancellations are exempt from the FCC application fee. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee
- **FACT:** VECs and VE teams must not collect the $35 application fee at exam sessions — the fee is paid online directly to the FCC through the CORES payment system. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee
- **FACT:** When the FCC receives the exam application from the VEC, it emails a payment-instructions link to the candidate, who then has 10 calendar days from issuance of the application file number to pay (and can pay sooner by looking up the pending application by FRN in the FCC application search). — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (ARRL-described FCC process — see §7.12)
- **FACT:** If the $35 fee is not paid within the 10-day window the FCC dismisses the application, but the candidate does not have to retest — the coordinating VEC can refile the application at any time before the CSCE expires. — Source: ARRL, FCC Application Fee, http://www.arrl.org/fcc-application-fee (ARRL-described FCC process — see §7.12)
- **FACT:** After the fee is paid and the application processed, the FCC emails a link to the official electronic license and provides no paper license documents, and the download link in that email is valid for 30 days. — Source: ARRL, NCVEC 605 Instructions, http://www.arrl.org/605-instructions; ARRL, FCC Application Fee (ARRL-described FCC process — see §7.12)
- **FACT:** Your license grant typically appears in the FCC's ULS database the next business day after you pay the application fee — and you may not transmit until it appears there. — Source: Laurel VEC FAQ, https://larc-vec.org/faq.php (typical timing, never a promise — see §7.11)
- **FACT:** An amateur service license "is normally granted for a 10-year term." — Source: 47 CFR §97.25; pool T1C08
- **FACT:** A license renewal may be filed no earlier than 90 days before the expiration date and no later than the expiration date, and renewals filed since April 19, 2022 carry the $35 application fee. — Source: 47 CFR §1.949(a) (applied by §97.21(a)(3)); FCC, Common Amateur Filing Tasks; pool T1C07
- **FACT:** An expired license may be renewed "during a 2 year filing grace period," but no privileges are conferred unless and until the license grant is renewed — you may renew during the grace period, but you may not transmit. — Source: 47 CFR §97.21(b); pool T1C09, T1C11
- **FACT:** A CSCE is valid for 365 days from its issue date for the element credit it conveys, and no subsequently issued CSCE renews another CSCE's validity period. — Source: ARRL Volunteer Examiner Manual, CSCE section, http://www.arrl.org/files/file/VEs/VE%20Manual%20Web%20Final%202022.pdf; 47 CFR §97.505(b)
- **FACT:** A licensee who passes a higher-class exam and properly submits Form 605 through the VEs may exercise the new class privileges immediately, until final disposition of the application or 365 days after passing, whichever comes first. — Source: 47 CFR §97.9(b)
- **FACT:** An unexpired (or in-grace-period) Technician license granted on or after March 21, 1987 earns Element 2 credit, and VEs must give examination credit for each element a CSCE shows the examinee passed within the previous 365 days. — Source: 47 CFR §97.505
- **FACT:** Every examination question set must use questions from the applicable published question pool. — Source: 47 CFR §97.507(b)
- **FACT:** Each question pool "must contain at least 10 times the number of questions required for a single examination" and must be published and made available to the public before its use. — Source: 47 CFR §97.523
- **FACT:** Each written question set must be prepared by a VE holding an Amateur Extra Class license — except Element 2 sets, which an Advanced or General Class VE may prepare. — Source: 47 CFR §97.507(a)
- **FACT:** No organization may serve as a VEC "unless it has entered into a written agreement with the FCC," and VECs must register every qualified examinee without regard to race, sex, religion, national origin, or membership (or lack thereof) in any amateur service organization. — Source: 47 CFR §97.521
- **FACT:** Each examinee must comply with the instructions given by the administering VEs, and the VEs must immediately terminate the examination upon failure of the examinee to comply. — Source: 47 CFR §97.511, §97.509(c)
- **FACT:** The FCC may readminister any examination and may cancel the license of any licensee who fails to appear for readministration or who does not successfully complete a readministered element. — Source: 47 CFR §97.519(d)
- **FACT:** No Morse code exam exists for any US license class — the FCC dropped the Morse code requirement effective February 23, 2007. — Source: Laurel VEC FAQ, https://larc-vec.org/faq.php; FCC Report & Order (Fed. Reg. Jan. 24, 2007)
- **FACT:** There is no age limit for a US amateur license, and anyone may hold one except a representative of a foreign government. — Source: FCC, Amateur Radio Service, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service; ARRL, Getting Licensed
- **FACT:** The Technician license grants access to all amateur frequencies above 30 MHz plus limited HF privileges; General adds privileges on all bands and modes; Amateur Extra conveys all available US amateur privileges. — Source: ARRL, Getting Licensed, http://www.arrl.org/getting-licensed
- **FACT:** Most new amateur operators start at Technician class and may then advance to General or Amateur Extra, with exam credit given for classes already held so passed elements need not be repeated. — Source: FCC, Amateur Radio Service, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service
- **FACT:** ARRL's license-exam search locates in-person sessions by ZIP code and links to online sessions, is updated daily, and includes sessions sponsored by non-ARRL VEC organizations. — Source: ARRL, Find an Amateur Radio License Exam Session, http://www.arrl.org/find-an-amateur-radio-license-exam-session
- **FACT:** HamStudy.org offers free stats-driven flash cards, question lists, explanations, and practice tests built on the published question pools, and its session page lists both in-person and remote exam sessions run by many VE teams. — Source: HamStudy.org, https://hamstudy.org/ and https://hamstudy.org/sessions
- **FACT:** Laurel VEC has administered free amateur radio license exams since 1984 and charges no fees for any licensing-related services; its website is larc-vec.org (the legacy laurelvec.com domain redirects there). — Source: Laurel VEC FAQ, https://larc-vec.org/faq.php (redirect verified 2026-07-23)

### 2.3 Call signs

- **FACT:** Each new station is assigned a call sign by the sequential call sign system from the regional-group list for the licensee's operator class and mailing address, and the station keeps the same call sign upon renewal or modification unless the licensee applies for a change. — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems
- **FACT:** A US amateur call sign consists of a prefix of one letter (K, N, or W) or two letters (AA–AL, KA–KZ, NA–NZ, or WA–WZ), a numeral 0–9 indicating the geographic region, and a suffix of one to three letters. — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems
- **FACT:** The sequential call sign system has four groups: Group A for Amateur Extra (1×2, 2×1, and two-letter-prefix-starting-with-A 2×2 formats), Group B for Advanced (2×2 with prefix starting K, N, or W), Group C for General, Technician, and Technician Plus (1×3), and Group D for Novice, club, and military recreation stations (2×3 with prefix starting K or W). — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems (fetched and verified 2026-07-23 — see §7.1)
- **FACT:** When the call signs in any regional-group list are exhausted, the selection is made from the next lower group. — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems
- **FACT:** KF1XXX is a valid Group D call sign format for a Technician class licensee — two-letter prefix starting with K, the region numeral, and a three-letter suffix (a 2×3 format). — Source: pool T1C05 (keyed answer); format per FCC, Amateur Call Sign Systems (Group D, regions 1–10) — see §7.1
- **FACT:** The numeral in a US call sign is the call district: regions 1–10 cover the contiguous states (1 = New England, 6 = California, 0 = the tenth region), with Alaska as region 11, the Caribbean insular areas as region 12, and Hawaii and the Pacific insular areas as region 13. — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems
- **FACT:** Any licensed amateur may apply for a vanity call sign for a primary or club station. — Source: 47 CFR §97.19(a); pool T1C02
- **FACT:** Vanity call sign requests list up to 25 call signs in order of preference, each given as an exact prefix, numeral, and suffix, and the first assignable call sign for which the requestor is eligible is granted while the old call sign is vacated. — Source: FCC, Amateur Call Sign Systems, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems
- **FACT:** A vanity applicant can receive a call sign only from a group corresponding to the applicant's operator class or lower — a Technician can receive only Group C or D formats, and requesting a Group A or B call sign gets the application dismissed. — Source: FCC, Amateur Call Sign Systems; 47 CFR §97.19(d)
- **FACT:** Military recreation stations are not eligible for vanity call signs. — Source: 47 CFR §97.19(a)
- **FACT:** A call sign normally becomes assignable again two years after license expiration, surrender, revocation, cancellation, or the grantee's death, with limited exceptions for close relatives and former holders. — Source: FCC, Amateur Call Sign Systems; 47 CFR §97.19(c)
- **FACT:** Club station and military recreation station license applications and changes are handled through Club Station Call Sign Administrators (CSCSA) — not via the NCVEC Form 605 and not directly with the FCC. — Source: ARRL, NCVEC 605 Instructions, http://www.arrl.org/605-instructions; 47 CFR §97.21(a)(1)
- **FACT:** The special event call sign system offers a block of 750 "1×1" call signs (single K, N, or W letter, single digit, single letter — e.g., K1A) coordinated by FCC-certified special event coordinators, and a station using one must still transmit its assigned call sign at least once per hour. — Source: FCC, Special Event Call Signs, https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/special-event-call-signs
- **FACT:** Some call signs are never assigned: prefixes AM–AZ (ITU-assigned to other countries), suffixes SOS or QRA–QUZ, any 2×3 with X as the first suffix letter, reserved government/FEMA formats, and the 1×1 formats (reserved for the special event system). — Source: FCC, Amateur Call Sign Systems, "Call Sign Availability," https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems

### 2.4 Bands and privileges

- **FACT:** Technician control operators share the same VHF-and-up allocations as the higher license classes; in ITU Region 2 these include 6 meters = 50–54 MHz, 2 meters = 144–148 MHz, 1.25 meters = 219–220 and 222–225 MHz, and 70 centimeters = 420–450 MHz. — Source: 47 CFR §97.301(a) (Region 2 column)
- **FACT:** 52.525 MHz is inside the 6-meter amateur band (50–54 MHz). — Source: pool T1B03; 47 CFR §97.301(a)
- **FACT:** 146.52 MHz is inside the 2-meter amateur band (144–148 MHz). — Source: pool T1B04; 47 CFR §97.301(a)
- **FACT:** A Technician's HF segments are 80 meters: 3.525–3.600 MHz; 40 meters: 7.025–7.125 MHz; 15 meters: 21.025–21.200 MHz; and 10 meters: 28.0–28.5 MHz. — Source: 47 CFR §97.301(e)
- **FACT:** On the 80-, 40-, and 15-meter Technician HF segments, a station with a Novice or Technician control operator "may only transmit a CW emission using the international Morse code" — no phone on those bands. — Source: 47 CFR §97.307(f)(9); pool T1B06
- **FACT:** Technician phone operation on HF exists only on 10 meters, 28.300–28.500 MHz, where Novice and Technician control operators may transmit CW or SSB phone (emissions J3E and R3E). — Source: 47 CFR §97.305(c)(3)(xviii), §97.307(f)(10); pool T1B01, T1B06
- **FACT:** Technicians are authorized to use data emissions (digital modes such as FT8) on 10 meters (28.0–28.3 MHz RTTY/data), on 6 meters (50.1–54 MHz), and on 2 meters (144.1–148 MHz) — all three bands. — Source: 47 CFR §97.305(c); pool T1B05
- **FACT:** CW is authorized on any frequency where the control operator has privileges, which makes 50.0–50.1 MHz and 144.0–144.1 MHz — the bottoms of 6 meters and 2 meters — CW-only segments. — Source: 47 CFR §97.305(a), §97.305(c); pool T1B07
- **FACT:** SSB phone may be used in at least some segment of every amateur band above 50 MHz. — Source: 47 CFR §97.305(c); pool T1B10
- **FACT:** Where the amateur service is secondary, "a station in a secondary service must not cause harmful interference to, and must accept interference from, stations in a primary service" — amateurs may encounter non-amateur stations there and must avoid interfering with them. — Source: 47 CFR §97.303; pool T1B08
- **FACT:** "Emissions resulting from modulation must be confined to the band or segment available to the control operator," so you should never set your transmit frequency exactly at a band or sub-band edge — display calibration error, sidebands spilling past the edge, and transmitter drift all put you out of bounds. — Source: 47 CFR §97.307(b), §97.101(a); pool T1B09
- **FACT:** "An amateur station must use the minimum transmitter power necessary to carry out the desired communications." — Source: 47 CFR §97.313(a)
- **FACT:** The maximum peak envelope power output for Technician class operators in their HF band segments is 200 watts. — Source: 47 CFR §97.313(c)(2); pool T1B11
- **FACT:** Except for some specific restrictions, the maximum peak envelope power output for Technician class operators using frequencies above 30 MHz is 1500 watts (1.5 kW PEP) — the general amateur ceiling, not a band-by-band grant. — Source: 47 CFR §97.313(b); pool T1B12; restrictions e.g. 50 W PEP on 219–220 MHz per §97.313(h) — see §7.9
- **FACT:** Automatically controlled amateur propagation beacons on HF are found on 10 meters, between 28.200 MHz and 28.300 MHz. — Source: 47 CFR §97.203(d); pool T1A06
- **FACT:** Any US amateur with a Technician class or higher license may contact the International Space Station on VHF — any class of licensee may be the control operator of an Earth station or space station, subject to the privileges of their class, and Part 97 requires no NASA approval. — Source: 47 CFR §97.207(a), §97.209(a); pool T1B02, T1E02 — see §7.7
- **FACT:** Auxiliary stations are limited to the 2-meter and shorter wavelength bands (minus listed segments) and require a Technician-class-or-higher control operator. — Source: 47 CFR §97.201(a)–(b); pool T1D07
- **FACT:** Amateur bands are identified by their approximate wavelength in meters in addition to frequency — hence "2 meters" for 144–148 MHz and "6 meters" for 50–54 MHz. — Source: pool T3B07

### 2.5 Operating practice

- **FACT:** Repeater offset means the difference between a repeater's transmit and receive frequencies. — Source: pool T2A07
- **FACT:** A common repeater frequency offset in the 2-meter band is plus or minus 600 kHz. — Source: pool T2A01
- **FACT:** A common repeater frequency offset in the 70-centimeter band is plus or minus 5 MHz. — Source: pool T2A03
- **FACT:** 146.520 MHz is the national calling frequency for FM simplex operations in the 2-meter band. — Source: pool T2A02
- **FACT:** To call a specific station — on a repeater or when answering a CQ — say the other station's call sign first, then identify with your own. — Source: pool T2A04, T2A05
- **FACT:** To raise any station on simplex or HF phone, repeat "CQ" a few times, say "this is" followed by your call sign, pause to listen, and repeat as needed; CQ means "calling any station." — Source: pool T2A06, T2A08
- **FACT:** On a repeater you indicate you are monitoring by saying your call sign followed by "listening" — calling CQ is for simplex and HF, not repeaters. — Source: pool T2A09; practice note per `canon/research/r5-operating.md` §1
- **FACT:** Simplex describes an amateur station that is transmitting and receiving on the same frequency. — Source: pool T2A11
- **FACT:** A band plan is a voluntary guideline for using different modes or activities within an amateur band, beyond the privileges established by the FCC — it is expected community behavior, never an FCC mandate. — Source: pool T2A10; 47 CFR §97.101(a) — see §7.5
- **FACT:** Band plans designate simplex channels so that stations within range of each other can talk without tying up a repeater. — Source: pool T2B09
- **FACT:** No frequency is assigned for the exclusive use of any station, so two stations that keep interfering with each other on a frequency should negotiate continued shared use — "we were here first" is not a rule. — Source: 47 CFR §97.101(b); pool T2B08
- **FACT:** A repeater's reverse function listens on the repeater's input frequency so you can hear the other station directly. — Source: pool T2B01
- **FACT:** CTCSS is a sub-audible tone transmitted along with normal voice audio to open the squelch of a receiver. — Source: pool T2B02
- **FACT:** If you can hear a repeater's output but cannot bring it up, the usual suspects are a wrong offset, a wrong CTCSS tone, or a wrong DCS code — all three. — Source: pool T2B04
- **FACT:** CTCSS and DCS are access control and selective calling, not privacy — any receiver in carrier squelch hears the whole conversation, and "PL" is just Motorola's 1951 trade name "Private Line." — Source: repeater-builder.com tone-squelch overview (fetched 2026-07-23), consistent with pool T2B02 — see §7.6
- **FACT:** DTMF signaling uses two simultaneous audio tones per keypress (touch-tones), and it is how you drive repeater features such as autopatch and IRLP linking. — Source: pool T2B06, T8C06
- **FACT:** Talking too loudly into an FM microphone overdeviates the signal, and the fix for audio that drops out on voice peaks is to talk farther away from the microphone. — Source: pool T2B05, T7B01
- **FACT:** Squelch mutes the receiver's audio when no signal is present. — Source: pool T2B13
- **FACT:** In a linked repeater network, a signal received by one repeater is retransmitted by all the repeaters in the network. — Source: pool T2B03
- **FACT:** On DMR, a color code is an access code programmed into the radio to reach a specific repeater, and a talkgroup is an identifier that organizes traffic so listeners hear only their group, joined by programming the group's ID. — Source: pool T2B12, T2B14, T2B07 — see §7.6
- **FACT:** QRM is the Q signal that indicates you are receiving interference from other stations. — Source: pool T2B10
- **FACT:** QSY is the Q signal that indicates you are changing frequency. — Source: pool T2B11
- **FACT:** QRZ means "Who is calling me?" and QTH means "My location is ___" (question form: "What is your location?"). — Source: ARRL, "Communicating with Other Hams — Q Signals," arrl.org/files/file/Get%20on%20the%20Air/Comm%20w%20Other%20Hams-Q%20Signals.pdf
- **FACT:** The standard (ITU) phonetic alphabet is: Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu. — Source: ITU phonetic tables (spellings "Alfa"/"Juliett" per ITU); pool T2C03 tests the technique — see §7.6
- **FACT:** Unusual words in a voice message are spelled with the standard phonetic alphabet to ensure correct receipt. — Source: pool T2C03
- **FACT:** Operating outside your license-class privileges is permitted only in situations involving immediate safety of human life or protection of property. — Source: pool T2C09; 47 CFR §97.403
- **FACT:** In a directed net, the Net Control Station (NCS) calls the net to order and directs communications between stations checking in, and unless you are reporting an emergency you transmit only when directed by the NCS. — Source: pool T2C02, T2C07
- **FACT:** "Traffic" in net operation means formal written messages exchanged by net stations. — Source: pool T2C05
- **FACT:** The preamble of a radiogram is the block of information needed to track the message (number, precedence, origin, and so on). — Source: pool T2C10
- **FACT:** "Check" in a radiogram header means the number of words or word equivalents in the text portion of the message. — Source: pool T2C11
- **FACT:** ARES is a body of licensed amateurs who have voluntarily registered their qualifications and equipment for public-service communications duty. — Source: pool T2C06
- **FACT:** RACES is the FCC Part 97 service for civil defense communications during national emergencies, and operating a RACES station requires certification by a civil defense agency. — Source: pool T2C04, T2C12; 47 CFR §97.407(a)
- **FACT:** Winlink relays messages using email addresses based on amateur call signs. — Source: pool T2C08
- **FACT:** FM (or PM) is the mode used for VHF/UHF voice repeaters and for VHF packet radio. — Source: pool T8A04, T8A02
- **FACT:** SSB is the mode used for long-distance weak-signal voice contacts on the VHF/UHF bands and on HF. — Source: pool T8A03
- **FACT:** The convention for single sideband on 10-meter HF and on the VHF/UHF bands is upper sideband (USB). — Source: pool T8A06
- **FACT:** SSB's advantage over FM is its narrower bandwidth. — Source: pool T8A07
- **FACT:** FM's disadvantage is the capture effect — only the strongest signal is received at a time. — Source: pool T8A12
- **FACT:** The bandwidth ladder to memorize is: CW ≈ 150 Hz (the narrowest common emission), SSB voice ≈ 3 kHz, FM voice on VHF repeaters ≈ 10–15 kHz, and AM fast-scan TV ≈ 6 MHz. — Source: pool T8A11, T8A05, T8A08, T8A09, T8A10
- **FACT:** A satellite beacon is a transmission from the satellite carrying status information (telemetry about its health), and anyone — licensed or not — may receive satellite telemetry. — Source: pool T8B01, T8B05, T8B11
- **FACT:** Satellite tracking programs take Keplerian elements as input and return ground-track maps, pass times with azimuth and elevation, and the Doppler-corrected frequency. — Source: pool T8B06, T8B03
- **FACT:** Doppler shift is the observed change in signal frequency caused by relative motion between the satellite and the Earth station. — Source: pool T8B07
- **FACT:** A satellite operating in U/V mode has its uplink in the 70-centimeter band and its downlink in the 2-meter band. — Source: pool T8B08
- **FACT:** Spin fading is the rhythmic rise and fall of a satellite's signal strength caused by the rotation of the satellite and its antennas. — Source: pool T8B09
- **FACT:** LEO means Low Earth Orbit, which has a period of around 100 minutes. — Source: pool T8B10 — see §7.6
- **FACT:** Satellites commonly use FM, SSB, and CW/data modes. — Source: pool T8B04
- **FACT:** Excessive uplink power can block access by other users of a satellite, and the right level on a linear transponder is when your downlink signal is about as strong as the satellite's beacon. — Source: pool T8B02, T8B12
- **FACT:** SO-50, the classic first FM satellite, has an uplink of 145.850 MHz FM and a downlink of 436.795 MHz; it wakes when you arm a 10-minute timer with a 2-second carrier using a 74.4 Hz tone, and you then operate with a 67.0 Hz tone. — Source: amsat.org SO-50 satellite information page (fetched 2026-07-23)
- **FACT:** The ISS voice downlink is 145.800 MHz worldwide and its VHF packet frequency is 145.825 MHz (uplink and downlink). — Source: ariss.org "Contact the ISS" (fetched 2026-07-23; ISS modes and frequencies change — re-check before print, see §7.6)
- **FACT:** Contesting means contacting as many stations as possible in a specified period, and good practice is to send only the minimum information needed for identification and the contest exchange. — Source: pool T8C03, T8C04
- **FACT:** A grid locator is a letter-number designator for a geographic location (the Maidenhead system, e.g., "FN31"). — Source: pool T8C05
- **FACT:** Radio direction finding (RDF) is used to locate sources of noise, interference, or jamming, and a directional antenna is the key tool for hidden-transmitter ("fox") hunts. — Source: pool T8C01, T8C02
- **FACT:** VoIP (Voice over Internet Protocol) is voice delivered over the internet using digital techniques. — Source: pool T8C07
- **FACT:** IRLP (Internet Radio Linking Project) connects amateur radio systems such as repeaters through the internet, and over-the-air access to a node is by DTMF codes from your radio. — Source: pool T8C08, T8C06
- **FACT:** EchoLink lets you operate through a repeater without a radio — from a computer or phone app — and before using it you must register your call sign and provide proof of license. — Source: pool T8C09, T8C10; echolink.org/validation
- **FACT:** A gateway is an amateur station that connects other amateur stations to the internet. — Source: pool T8C11
- **FACT:** Digital modes include packet radio, IEEE 802.11 (Wi-Fi), and FT8 — all of them. — Source: pool T8D01
- **FACT:** FT8 is a digital mode designed for very low signal-to-noise operation — contacts below audibility, exchanged in timed 15-second sequences. — Source: pool T8D02
- **FACT:** The WSJT-X software suite (FT8's home) also supports Earth-Moon-Earth, weak-signal propagation beacons, and meteor scatter. — Source: pool T8D10
- **FACT:** APRS carries GPS position, short text messages, and weather data, and its signature use is real-time tactical digital communications with stations plotted on a map; in North America it lives on 144.390 MHz. — Source: pool T8D03, T8D05; frequency per IARU Region 2 practice (`canon/research/r5-operating.md` §4, fetched 2026-07-23)
- **FACT:** Packet radio transmissions include a header with the destination station's call sign, a checksum for error detection, and ARQ — the receiving station detects errors and sends a request for retransmission. — Source: pool T8D08, T8D11
- **FACT:** PSK stands for Phase Shift Keying. — Source: pool T8D06
- **FACT:** DMR (Digital Mobile Radio) time-multiplexes two digital voice signals on a single 12.5 kHz repeater channel (two "time slots"). — Source: pool T8D07
- **FACT:** CW is simply another name for a Morse code transmission. — Source: pool T8D09
- **FACT:** NTSC is the analog fast-scan color television signal standard. — Source: pool T8D04
- **FACT:** An amateur mesh network is built from commercial Wi-Fi equipment with modified firmware, operating on amateur frequencies. — Source: pool T8D12
- **FACT:** On SSB and CW, signal reports use the RST system (readability 1–5, strength 1–9, and tone 1–9 on CW); everyday FM signal reports use plain jargon like "full quieting" instead. — Source: ARRL Quick Reference Operating Aids, arrl.org/quick-reference-operating-aids; `canon/research/r5-operating.md` §1 — see §7.6

### 2.6 Technical values

**Electrical fundamentals and math (T5):**

- **FACT:** Current is the flow of electrons in a circuit, and it is measured in amperes. — Source: pool T5A03, T5A01
- **FACT:** A difference in voltage is what causes electron flow in a circuit. — Source: pool T5A05 (as revised 2026-02-19)
- **FACT:** Electrical power is the rate at which electrical energy is used, and it is measured in watts. — Source: pool T5A10, T5A02
- **FACT:** Frequency is the number of complete AC cycles per second, and its unit is the hertz. — Source: pool T5A04, T5A06
- **FACT:** Alternating current (AC) alternates between positive and negative directions. — Source: pool T5A09
- **FACT:** Resistance opposes every kind of current flow — DC, AC, and RF alike. — Source: pool T5A11
- **FACT:** Metals conduct electricity because they have many free electrons, while glass is a good insulator. — Source: pool T5A07, T5A08
- **FACT:** The metric prefix ladder runs in three-orders-of-magnitude steps: pico (10⁻¹²), nano (10⁻⁹), micro (10⁻⁶), milli (10⁻³), base unit, kilo (10³), mega (10⁶), giga (10⁹). — Source: pool T5B group (standard metric knowledge)
- **FACT:** A power increase to double is approximately 3 dB, to four times is approximately 6 dB (so a decrease to one quarter is approximately −6 dB), and to ten times is exactly 10 dB. — Source: pool T5B09, T5B10, T5B11
- **FACT:** Capacitance is the ability to store energy in an electric field, and its unit is the farad. — Source: pool T5C01, T5C02
- **FACT:** Inductance is the ability to store energy in a magnetic field, and its unit is the henry. — Source: pool T5C03, T5C04
- **FACT:** Impedance is the opposition to AC current flow — resistance plus reactance — and its unit is the ohm. — Source: pool T5C12, T5C05
- **FACT:** Unit abbreviations are case-sensitive and the pool tests them: kilohertz is written kHz (lowercase k) and megahertz is written MHz (capital M) — in both, the H is capital. — Source: pool T5C06, T5C07
- **FACT:** The formula for electrical power in a DC circuit is P = E × I — power equals voltage multiplied by current (the pool's own answer prints "P = I x E"). — Source: pool T5C08
- **FACT:** Ohm's law is E = I × R, rearranged as I = E / R and R = E / I. — Source: pool T5D01–T5D03
- **FACT:** In a series circuit the current is the same through all components, and in a parallel circuit the voltage is the same across all components. — Source: pool T5D13, T5D14

**Waves and propagation (T3):**

- **FACT:** A radio wave consists of an electric field and a magnetic field at right angles to each other, and its polarization is defined by the orientation of the electric field. — Source: pool T3B01, T3B02, T3B03
- **FACT:** In free space every radio wave travels at the speed of light regardless of frequency — approximately 300,000,000 meters per second (3×10⁸ m/s). — Source: pool T3B04, T3B11, T3B12
- **FACT:** Wavelength and frequency are inversely related — the higher the frequency, the shorter the wavelength. — Source: pool T3B05
- **FACT:** The formula for converting frequency to approximate wavelength is: wavelength in meters equals 300 divided by frequency in megahertz. — Source: pool T3B06
- **FACT:** HF is 3 to 30 MHz, VHF is 30 to 300 MHz, and UHF is 300 to 3000 MHz. — Source: pool T3B10, T3B08, T3B09
- **FACT:** The ionosphere is the region of the atmosphere that reflects HF radio waves. — Source: pool T3A11
- **FACT:** Multipath — signals arriving over different paths and combining in or out of phase — explains VHF strength changes when an antenna moves a few feet, the rapid mobile flutter called "picket fencing," irregular fading on ionospheric paths, and increased error rates on data transmissions. — Source: pool T3A01, T3A06, T3A08, T3A10
- **FACT:** Vegetation absorbs UHF and microwave energy, and precipitation decreases range at microwave frequencies — but fog and rain have little effect on 10-meter and 6-meter signals. — Source: pool T3A02, T3A07, T3A12
- **FACT:** Horizontal polarization is the convention for long-distance CW/SSB weak-signal work on VHF/UHF, and cross-polarized antennas over a line-of-sight path reduce received signal strength. — Source: pool T3A03, T3A04
- **FACT:** Ionospherically propagated signals become elliptically polarized, so on skywave paths either antenna orientation works. — Source: pool T3A09
- **FACT:** The radio horizon lies beyond the visual horizon because the atmosphere refracts radio waves slightly. — Source: pool T3C11
- **FACT:** Long-distance ionospheric (skywave) propagation is far more common on HF than on VHF and above. — Source: pool T3C02
- **FACT:** Sporadic E is the propagation type most commonly associated with occasional strong signals from beyond the radio horizon on the 10-, 6-, and 2-meter bands. — Source: pool T3C04
- **FACT:** Tropospheric ducting, caused by temperature inversions, regularly allows over-the-horizon VHF and UHF communications to ranges of approximately 300 miles. — Source: pool T3C06, T3C08
- **FACT:** Knife-edge diffraction bends signals over or around obstructions between stations. — Source: pool T3C05
- **FACT:** Auroral backscatter returns VHF signals distorted with a characteristic raspy sound. — Source: pool T3C03
- **FACT:** The band best suited for communicating via meteor scatter is 6 meters. — Source: pool T3C07
- **FACT:** The best long-distance 10-meter F-region propagation occurs from dawn to shortly after sunset during periods of high sunspot activity, and at the sunspot peak both 6 and 10 meters can deliver F-region DX. — Source: pool T3C09, T3C10

**Station setup and controls (T4):**

- **FACT:** A typical 50-watt-output mobile FM transceiver needs a 13.8-volt supply rated around 12 amperes. — Source: pool T4A01
- **FACT:** To estimate how long equipment can be powered from a battery, divide the battery's ampere-hour rating by the average current draw of the equipment. — Source: pool T4A09
- **FACT:** An accessory SWR meter must be rated for the frequency and power level at which you will measure, and an RF power meter installs in the feed line between the transmitter and the antenna. — Source: pool T4A02, T4A05
- **FACT:** A digital-mode interface between computer and transceiver moves three signals: receive audio, transmit audio, and transmitter keying. — Source: pool T4A06
- **FACT:** Flat copper strap is the preferred RF bonding conductor because of its low inductance at RF. — Source: pool T4A08
- **FACT:** A digital hotspot is a small RF gateway that connects nearby transceivers to an internet digital voice or data network. — Source: pool T4A10
- **FACT:** An electronic keyer assists the manual sending of Morse code by forming the dits and dahs for you. — Source: pool T4A12
- **FACT:** Excessive microphone gain on SSB produces distorted transmitted audio. — Source: pool T4B01
- **FACT:** To hear a weak FM signal, set the squelch threshold so the receiver audio is on all the time (squelch fully open). — Source: pool T4B03
- **FACT:** If an SSB station's voice pitch sounds too high or low, adjust the RIT (Clarifier) — it nudges the receive frequency without moving your transmit frequency. — Source: pool T4B06
- **FACT:** Among the pool's listed choices, a 2400 Hz receiver filter bandwidth provides the best signal-to-noise ratio for SSB reception. — Source: pool T4B10
- **FACT:** A DMR code plug is the configuration data (repeaters, talkgroups) loaded into the radio, and a D-STAR radio must have your call sign programmed before it can transmit. — Source: pool T4B07, T4B11

**Components and circuits (T6):**

- **FACT:** A resistor's job is to oppose (limit) current flow. — Source: pool T6A01
- **FACT:** A potentiometer is an adjustable resistor, and the parameter it controls is resistance. — Source: pool T6A02, T6A03
- **FACT:** A capacitor stores energy in an electric field, and it is built from two conductive plates separated by an insulating dielectric. — Source: pool T6A04, T6A05
- **FACT:** An inductor stores energy in a magnetic field, and it is built from a coil of wire. — Source: pool T6A06, T6A07
- **FACT:** In switch nomenclature, "pole" is the number of circuits handled and "throw" is the number of contact positions per pole, and an SPDT switch connects one circuit to either of two others. — Source: pool T6A08
- **FACT:** Carbon-zinc is the battery chemistry that is not rechargeable; nickel-metal hydride, lithium-ion, lead-acid, and nickel-cadmium are rechargeable. — Source: pool T6A11, T6A10
- **FACT:** A diode lets current flow in only one direction, its electrodes are the anode and the cathode, and the cathode lead of the physical part is often marked with a stripe. — Source: pool T6B02, T6B09, T6B06
- **FACT:** An LED is a diode that emits light when forward current flows through it. — Source: pool T6B07
- **FACT:** A transistor is built from three regions of semiconductor material, and it can work as an electronic switch or as an amplifier providing power gain. — Source: pool T6B04, T6B03, T6B10
- **FACT:** Gain means the output compared to the input — of voltage, current, or power. — Source: pool T6B11
- **FACT:** The electrodes of a bipolar junction transistor (BJT) are the emitter, the base, and the collector. — Source: pool T6B12
- **FACT:** FET stands for Field Effect Transistor, and its electrodes are the gate, the drain, and the source. — Source: pool T6B08, T6B05
- **FACT:** A schematic is an electrical diagram drawn with standard component symbols, and what it accurately shows is how components are connected — not wire lengths or physical appearance. — Source: pool T6C01, T6C12
- **FACT:** A rectifier changes AC into a varying (pulsating) DC, a transformer changes AC voltage up or down (never to DC), and a voltage regulator holds a power supply's output voltage steady. — Source: pool T6D01, T6D06, T6D05
- **FACT:** A relay is an electrically controlled switch — a small coil current switches a larger current. — Source: pool T6D02
- **FACT:** An inductor plus a capacitor (in series or in parallel) makes a resonant (tuned) circuit — the frequency-selecting circuit. — Source: pool T6D08, T6D11
- **FACT:** An integrated circuit (IC, or "chip") packs many semiconductors and other components into one package. — Source: pool T6D09
- **FACT:** LEDs are the standard visual indicator component. — Source: pool T6D07

**Station equipment and troubleshooting (T7):**

- **FACT:** Sensitivity is a receiver's ability to detect the presence of (weak) signals, and selectivity is its ability to discriminate between multiple nearby signals. — Source: pool T7A01, T7A04
- **FACT:** A transceiver combines a receiver and a transmitter in one unit. — Source: pool T7A02
- **FACT:** A mixer converts a signal from one frequency to another, while an oscillator generates a signal at a specific frequency. — Source: pool T7A03, T7A05
- **FACT:** The VFO (variable frequency oscillator) is the circuit that sets a transceiver's receive and transmit frequency. — Source: pool T7A11
- **FACT:** A transverter converts a transceiver's RF input and output to another band. — Source: pool T7A06
- **FACT:** The push-to-talk (PTT) input switches a transceiver from receive to transmit when it is grounded. — Source: pool T7A07
- **FACT:** Modulation is combining speech (or data) with an RF carrier signal. — Source: pool T7A08
- **FACT:** The SSB / CW-FM switch on some VHF power amplifiers sets the amplifier for proper operation in the selected mode — it adapts the amplifier; it does not change your signal's mode. — Source: pool T7A09 (as revised 2026-02-19)
- **FACT:** To raise transmitted output power, add an RF power amplifier after the transceiver. — Source: pool T7A10
- **FACT:** A broadcast radio or TV that picks up your transmission is being overloaded by a strong signal it cannot reject (fundamental overload) — the problem is in the affected receiver, not necessarily your station. — Source: pool T7B02
- **FACT:** RFI can come from fundamental overload, harmonics, or spurious emissions — all three. — Source: pool T7B03
- **FACT:** High SWR (not low) can make a solid-state transceiver reduce its output power, to protect the RF output transistors from reflected power. — Source: pool T7B04, T7C05
- **FACT:** When your clean signal bothers a neighbor's receiver, the fix is a filter at the affected receiver's antenna input; when a nearby commercial FM station overloads your 2-meter rig, the fix is a band-reject filter at your receiver. — Source: pool T7B05, T7B07
- **FACT:** For cable TV interference (non-fiber systems), the first step is to check that all coax connectors are properly installed — broken shielding is the usual entry point. — Source: pool T7B09
- **FACT:** A clip-on ferrite choke on the microphone cable stops transmitted RF from feeding back into the rig and distorting your audio. — Source: pool T7B11
- **FACT:** When a neighbor complains of interference, first verify that your own station is operating properly. — Source: pool T7B06
- **FACT:** A typical RF dummy load consists of a 50-ohm non-inductive resistor mounted on a heat sink, and it lets you test a transmitter without putting a signal on the air. — Source: pool T7C03, T7C01
- **FACT:** An antenna analyzer tells you whether an antenna is resonant at your operating frequency. — Source: pool T7C02
- **FACT:** An SWR reading of 1:1 indicates a perfect impedance match between antenna and feed line, while 4:1 indicates an impedance mismatch. — Source: pool T7C04, T7C06
- **FACT:** A directional wattmeter — reading forward and reflected power — is the instrument used to determine SWR. — Source: pool T7C08
- **FACT:** Power lost in a feed line is converted into heat. — Source: pool T7C07
- **FACT:** Moisture contamination is the classic coax-killer, sunlight cracks the outer jacket and lets water in (so the jacket must be UV-resistant), and foam-dielectric coax has less loss per foot than solid-dielectric coax. — Source: pool T7C09, T7C10, T7C11
- **FACT:** A voltmeter measures electric potential (voltage) and connects in parallel with the component; an ammeter measures current and connects in series so the current flows through the meter. — Source: pool T7D01–T7D04
- **FACT:** An ohmmeter measures resistance by applying a small current from its own internal battery and measuring the resulting voltage, so the circuit under test must not be powered. — Source: pool T7D05, T7D11
- **FACT:** Across a large discharged capacitor, an ohmmeter reads increasing resistance with time, because the meter's battery slowly charges the capacitor. — Source: pool T7D10
- **FACT:** Measuring voltage while a multimeter is set to the resistance (ohms) setting can damage the meter. — Source: pool T7D06
- **FACT:** Use rosin-core solder for electronics — never acid-core (plumbing) solder — and a cold solder joint looks rough or lumpy while a good joint is shiny and smooth. — Source: pool T7D08, T7D09

**Antennas and feed lines (T9):**

- **FACT:** A beam antenna concentrates signals in one direction, and of the antennas the pool lists, a Yagi offers the greatest gain. — Source: pool T9A01, T9A06
- **FACT:** Antenna gain is the increase in signal strength in a specified direction compared to a reference antenna — gain comes from focusing, not from creating extra power. — Source: pool T9A11
- **FACT:** Antenna polarization is described by the orientation of the electric field. — Source: pool T9A03
- **FACT:** Loading electrically lengthens an antenna by inserting inductors (coils) in the radiating elements — how short mobile whips act longer. — Source: pool T9A02
- **FACT:** Shortening a dipole raises its resonant frequency — longer antenna, lower frequency. — Source: pool T9A05
- **FACT:** A half-wave dipole radiates strongest broadside (out from its sides) and weakest off its ends. — Source: pool T9A10
- **FACT:** The short flexible "rubber duck" antenna on a handheld has low efficiency compared to a full-size quarter-wave antenna. — Source: pool T9A04
- **FACT:** Using a handheld transceiver inside a car, the vehicle's metal shell shields and weakens the signal — use an external antenna. — Source: pool T9A07
- **FACT:** A 19-inch vertical antenna is often used on 2 meters because it is a resonant quarter-wave at that band. — Source: pool T9A08
- **FACT:** A 5/8-wave whip has more gain than a quarter-wave whip for VHF/UHF mobile use. — Source: pool T9A09
- **FACT:** The most common impedance of coaxial cables used in amateur radio is 50 ohms. — Source: pool T9B02
- **FACT:** Coaxial cable dominates amateur use because it is easy to use and needs few special installation considerations — not because it is the lowest-loss or cheapest feed line. — Source: pool T9B03
- **FACT:** Coax loss increases as frequency increases — which is why UHF runs need better or shorter cable. — Source: pool T9B05
- **FACT:** RG-213 has less loss than RG-58 at a given frequency (it is thicker), and air-insulated hardline has the lowest loss of the feed lines the pool lists. — Source: pool T9B10, T9B11
- **FACT:** SWR (standing wave ratio) is a measure of how well a load is matched to a transmission line. — Source: pool T9B12
- **FACT:** The PL-259 ("UHF") connector is the standard at HF and VHF but is not watertight, the Type N connector is the right choice above 400 MHz, and any outdoor connector should be carefully taped against weather. — Source: pool T9B07, T9B06, T9B01
- **FACT:** Erratic SWR changes point to a loose connection in the antenna or feed line. — Source: pool T9B09
- **FACT:** An antenna tuner (coupler) matches the antenna system impedance to the transceiver's 50-ohm output. — Source: pool T9B04

**Safety (T0):**

- **FACT:** A 12-volt battery will not shock you, but shorting its terminals can cause burns, fire, or an explosion — the danger is the huge current, not the voltage. — Source: pool T0A01
- **FACT:** Rapidly charging or discharging an unprotected battery risks overheating or out-gassing — so charge batteries in a ventilated space. — Source: pool T0A10 (as revised 2026-02-19)
- **FACT:** Current through the human body can heat tissue, disrupt cells' electrical function, and cause involuntary muscle contractions — all three. — Source: pool T0A02
- **FACT:** In US three-wire 120 V AC cable, black insulation indicates the hot conductor (white is neutral, green is ground). — Source: pool T0A03
- **FACT:** A fuse removes power in case of an overload, you must never replace a fuse with a larger one (excessive current could start a fire), and the fuse or breaker goes in series with the hot conductor only. — Source: pool T0A04, T0A05, T0A08
- **FACT:** Shock protection habits are three-wire cords and plugs, all station equipment on a common safety ground, and fully discharging high-voltage capacitors before working inside gear. — Source: pool T0A06
- **FACT:** A power supply can still kill immediately after switch-off because of the charge stored in its filter capacitors. — Source: pool T0A11
- **FACT:** The lightning arrester goes on a grounded panel near where feed lines enter the building, and all external ground rods must be bonded together with heavy wire or strap. — Source: pool T0A07, T0A09
- **FACT:** When measuring high voltage, the voltmeter and its leads must be rated for the voltage being measured. — Source: pool T0A12
- **FACT:** Tower grounding connections must be short and direct, with separate eight-foot ground rods for each tower leg bonded to the tower and to each other, and grounding conductors must avoid sharp bends. — Source: pool T0B01, T0B08, T0B10
- **FACT:** Grounding requirements for towers come from local electrical codes, not from the FCC. — Source: pool T0B11
- **FACT:** Tower climbing rules are: get training, wear an approved harness, tie off at all times, and never climb without a helper or observer. — Source: pool T0B02, T0B03
- **FACT:** On a crank-up tower, climb only when it is retracted or mechanical safety locks are installed. — Source: pool T0B07
- **FACT:** Before raising an antenna, look for and stay clear of overhead wires, position the antenna so that if it falls no part of it can come within 10 feet of power lines, and never attach an antenna to a utility pole. — Source: pool T0B04, T0B06, T0B09
- **FACT:** The safety wire through a turnbuckle keeps vibration from loosening it. — Source: pool T0B05
- **FACT:** Radio signals are non-ionizing radiation — RF photons do not have enough energy to cause chemical changes in cells or damage DNA, unlike X-rays; the RF hazard is heating (and shocks or burns), not mutation. — Source: pool T0C01, T0C12
- **FACT:** RF exposure limits vary with frequency because the human body absorbs more RF energy at some frequencies than others, and of the bands the pool lists, 50 MHz (6 meters) has the lowest maximum permissible exposure. — Source: pool T0C05, T0C02
- **FACT:** Duty cycle is the percentage of time that a transmitter is transmitting during the averaging time for RF exposure. — Source: pool T0C11
- **FACT:** If duty cycle changes from 100 percent to 50 percent, the allowable power density for RF safety increases by a factor of 2. — Source: pool T0C03
- **FACT:** RF exposure depends on the frequency, the power level, the distance from the antenna, and the antenna's radiation pattern — all four — and the cheapest way to reduce exposure is to relocate antennas away from people. — Source: pool T0C04, T0C08
- **FACT:** Touching an antenna while it is transmitting causes an RF burn to the skin. — Source: pool T0C07
- **FACT:** RF exposure compliance is the station licensee's responsibility; acceptable evaluation methods are calculation per FCC OET Bulletin 65, computer modeling, or measurement with calibrated field-strength equipment; and you must re-evaluate whenever anything in the transmitter or antenna system changes. — Source: pool T0C13, T0C06, T0C09; 47 CFR §97.13(c)

---

## 3. Notation & Units

One consistent style for the whole book. Frequencies are in hertz with kHz/MHz/GHz as convenient; wavelength in meters; metric throughout, with US-conventional ham units only where the hobby genuinely uses them (feet for tower and power-line clearances, inches for whip length, miles for propagation ranges — the pool itself prints "10 feet," "19-inch," "approximately 300 miles").

| Symbol | Quantity | Unit | Canonical relation / note |
|---|---|---|---|
| V | Voltage (EMF) | volt (V) | **V = I × R** (Ohm's law); see pool-notation note below |
| I | Current | ampere (A) | I = V / R; the flow of electrons |
| R | Resistance | ohm (Ω) | R = V / I |
| P | Power | watt (W) | **P = V × I**; rate of energy use |
| f | Frequency | hertz (Hz; kHz, MHz, GHz) | Cycles per second; f = 1 / T |
| λ | Wavelength | meter (m) | **λ = c / f**; the band-name basis |
| c | Speed of light | m/s | ≈ 3×10⁸ m/s = 300,000 km/s (working value); 299,792,458 m/s (exact) |
| C | Capacitance | farad (F) | Energy stored in an electric field |
| L | Inductance | henry (H) | Energy stored in a magnetic field |
| Z | Impedance | ohm (Ω) | Opposition to AC: resistance + reactance |

**The wavelength shortcut:** the book states, as the pool's own formula, **λ(m) = 300 / f(MHz)** — "wavelength in meters equals 300 divided by frequency in megahertz" (pool T3B06). It is presented as an approximation of c = f·λ with c ≈ 3×10⁸ m/s, never as an exact identity. Drill examples: 300/146 ≈ 2.05 m (the 2-meter band) and 300/50 = 6 m (the 6-meter band).

**Decibels, gently:** dB is introduced by anchors, not by logarithms — **3 dB ≈ double power, 6 dB ≈ four times power (so −6 dB ≈ one quarter), 10 dB = ten times power** (pool T5B09–T5B11). The defining formula dB = 10·log₁₀(P₂/P₁) may appear only in an optional "The math, if you want it" sidebar.

**Pool-notation equivalence (binding):** the pool prints **E** for voltage and a plain "x" for multiplication — its formulas read "P = I x E" (T5C08), "E = I x R", "I = E / R", "R = E / I" (T5D01–T5D03). Prose in this book uses **V** for voltage and **×** as the multiplication sign (V = I × R, P = V × I). Chapters teach the equivalence explicitly on first use ("E and V both mean volts"), and verbatim pool quotes always keep the pool's E/x form. Where a chapter mirrors the pool (e.g., in an Exam Focus explanation), it may write E = I × R to match what the reader just saw.

**Unit style rules:**
- Case is load-bearing and tested (pool T5C06/T5C07): **kHz** (lowercase k), **MHz** and **GHz** (capital M/G), always capital **H**; **mA**, **µV**, **pF**, **kV** follow the same prefix case rules. Never "KHZ," "mhz," or "Mhz."
- Prefix ladder for conversions: pico (10⁻¹²) → nano (10⁻⁹) → micro (10⁻⁶) → milli (10⁻³) → base → kilo (10³) → mega (10⁶) → giga (10⁹); moving toward a smaller unit multiplies, toward a larger unit divides.
- Band names take the meter spelling with a numeral ("2 meters," "70 centimeters," "10 m" in tables); frequency ranges are written with an en dash and units once ("28.300–28.500 MHz").
- Power limits are written "200 W PEP," "1.5 kW PEP," "1500 watts" matching the pool's own phrasing where quoted.
- Inline math in chapters uses the `$…$` renderer; keep expressions simple (the pool's math is arithmetic only).

---

## 4. Glossary

Canonical plain-language one-line definitions, consolidated from the r3/r4/r5 vocabulary lists. These are binding — a chapter may expand a definition but must not contradict it — and this table feeds Appendix B directly.

| Term | Definition |
|---|---|
| AC (alternating current) | Current that alternates between positive and negative directions. |
| AFSK | Audio frequency-shift keying — digital data sent as shifting audio tones into a voice transmitter. |
| AGC (automatic gain control) | Receiver circuit that automatically turns gain down on strong signals to keep audio level. |
| Allocation | A frequency band assignment made to a radio service by regulation. |
| AM (amplitude modulation) | Impressing information on a carrier by varying its amplitude; SSB is a form of AM. |
| Ammeter | A meter that measures current, connected in series so the current flows through it. |
| Ampere (A) | The unit of electric current. |
| Ampere-hour (Ah) | A battery capacity unit: one ampere flowing for one hour. |
| Antenna analyzer | An instrument that tells whether an antenna is resonant at a chosen frequency. |
| Antenna tuner (coupler/transmatch) | A device that matches the antenna system impedance to the transceiver's 50-ohm output. |
| Anode | The diode electrode current enters in the forward direction. |
| APRS | A digital system carrying GPS position, short text, and weather data, plotted on a map in real time (144.390 MHz in North America). |
| ARQ (automatic repeat request) | Error recovery in which the receiver detects errors and requests retransmission. |
| ARES | Amateur Radio Emergency Service — licensed amateurs who voluntarily registered their qualifications and equipment for public-service duty. |
| Auxiliary station | An amateur station transmitting point-to-point communications within a system of cooperating stations, such as a repeater's remote link. |
| Auroral backscatter | VHF signals returned by the aurora, distorted with a characteristic raspy sound. |
| Automatic control | Operation of a transmitting station by devices and procedures without the control operator present at a control point. |
| Band plan | A voluntary community guideline for which modes and activities live where within a band. |
| Band-reject filter | A filter that blocks a chosen band of frequencies while passing the rest. |
| Bandwidth | The width of spectrum a signal occupies (e.g., ≈3 kHz for SSB voice). |
| Basis and purpose | The five-pronged mission statement of the Amateur Radio Service in §97.1. |
| Beacon (propagation) | An amateur station transmitting for observation of propagation and reception (on HF, 28.200–28.300 MHz on 10 m). |
| Beacon (satellite) | A transmission from a satellite carrying status and telemetry information. |
| Beam antenna | A directional antenna that concentrates signals in one direction. |
| BJT (bipolar junction transistor) | A transistor family whose electrodes are emitter, base, and collector. |
| Bonding | Electrically connecting equipment and ground rods with low-inductance conductors so everything sits at the same potential. |
| Broadside | The direction perpendicular to a dipole's wire, where it radiates strongest. |
| Broadcasting | Transmissions intended for reception by the general public — prohibited in the amateur service. |
| Capacitance | The ability to store energy in an electric field; unit farad. |
| Capacitor | A component that stores energy in an electric field — two conductive plates separated by a dielectric. |
| Capture effect | An FM receiver's tendency to reproduce only the strongest co-channel signal. |
| Carrier | The unmodulated RF signal onto which information is impressed. |
| Cathode | The diode electrode current exits in the forward direction; the package end is often marked with a stripe. |
| Check | In a radiogram header, the number of words or word equivalents in the message text. |
| Checksum | Extra data in a packet that lets the receiver detect transmission errors. |
| Circuit breaker | A resettable device that removes power when current exceeds its rating. |
| Coaxial cable (coax) | A shielded feed line with a center conductor inside a cylindrical braid; amateur coax is usually 50 ohms. |
| Code plug | The configuration data file (repeaters, talkgroups) loaded into a DMR radio. |
| Cold solder joint | A defective solder joint that looks rough or lumpy instead of shiny and smooth. |
| Color code | A DMR access code programmed into the radio to reach a specific repeater. |
| Conductor | A material that carries current easily because it has many free electrons. |
| Control operator | The licensed amateur designated by the station licensee to be responsible for the station's transmissions. |
| Control point | The location at which the control operator function is performed. |
| CORES | The FCC's COmmission REgistration System, where you register to get an FRN. |
| Courtesy tone | The short beep a repeater sounds after a user unkeys — wait for it before transmitting. |
| CQ | The general call inviting any station to reply ("calling any station") — used on simplex and HF, not on repeaters. |
| Cross-polarization | Mismatched antenna orientations between stations, which reduces received signal strength on line-of-sight paths. |
| CSCE | Certificate of Successful Completion of Examination — the VEs' proof you passed, valid 365 days for element credit. |
| CTCSS | A sub-audible continuous tone sent with voice audio to open a receiver's or repeater's squelch. |
| Current | The flow of electrons in a circuit; unit ampere. |
| CW | Continuous wave — a carrier keyed on and off; simply another name for a Morse code transmission. |
| DC (direct current) | Current that flows steadily in one direction. |
| DCS | A digital-bitstream equivalent of CTCSS used for repeater access. |
| Decibel (dB) | A logarithmic ratio unit: +3 dB ≈ double power, +10 dB = ten times power. |
| Deviation | The peak amount an FM carrier's frequency swings with modulation; too much is over-deviation. |
| Dielectric | The insulating material between a capacitor's plates (or inside a coaxial cable). |
| Digipeater | A digital repeater that relays packet frames hop by hop. |
| Digital mode | A mode carrying data rather than analog voice — packet radio, FT8, even IEEE 802.11 under amateur rules. |
| Diode | A semiconductor that lets current flow in only one direction. |
| Dipole | A straight antenna, usually a half wavelength long, fed at the center. |
| Directional wattmeter | An instrument reading forward and reflected power, used to determine SWR. |
| DMR (Digital Mobile Radio) | A digital voice standard that time-multiplexes two conversations on one 12.5 kHz channel. |
| Doppler shift | The change in observed signal frequency caused by relative motion between satellite and Earth station. |
| DTMF | Dual-tone multi-frequency — the two-tone-per-key telephone touch-tone signaling used to command repeaters and links. |
| Dummy load | A fake antenna — a 50-ohm non-inductive resistor on a heat sink — for testing without going on the air. |
| Duplex | Transmitting and receiving on two different frequencies, as through a repeater. |
| Duty cycle | The percentage of time a transmitter is actually transmitting during the exposure averaging time. |
| EchoLink | A VoIP system letting you operate through a repeater from a computer or phone app (requires license verification). |
| Electric field | The field between points at different voltages; a radio wave's polarization is defined by this field's orientation. |
| Electromagnetic wave | A traveling pair of electric and magnetic fields at right angles — a radio wave. |
| Electronic keyer | A device that forms Morse dits and dahs for you when you work the paddle. |
| EME (Earth-Moon-Earth) | Bouncing signals off the Moon to reach distant stations. |
| Emission mode | The type of signal a transmitter produces (CW, phone, data, image, and so on). |
| F region | The high ionospheric region responsible for long-distance HF skip. |
| Fading | Signal strength rising and falling, usually from multipath combining. |
| Fast-scan TV | Full-motion amateur television; the analog standard is NTSC and needs about 6 MHz of bandwidth. |
| Feed line | The cable that carries RF between the transceiver and the antenna. |
| Ferrite choke | A clip-on ferrite core on a cable that blocks unwanted RF current on the outside of the cable. |
| FET (field-effect transistor) | A transistor family whose electrodes are gate, drain, and source. |
| Filter bandwidth | The width of a receiver's selectable passband, matched to the mode (≈2400 Hz for SSB). |
| FM (frequency modulation) | Impressing information on a carrier by varying its frequency. |
| Form 605 | The FCC/NCVEC application form used at exam sessions and for license changes. |
| Fox hunt | A hidden-transmitter hunt using radio direction finding with a directional antenna. |
| Free space | Ideal empty space, where every radio wave travels at the speed of light. |
| Frequency | The number of complete cycles per second; unit hertz. |
| Frequency coordinator | A volunteer entity recognized by local amateurs that recommends repeater/auxiliary channels and parameters to minimize interference. |
| FRN | FCC Registration Number — a 10-digit identifier for all your FCC business, obtained free in CORES before exam day. |
| FT8 | A weak-signal digital mode exchanging minimal messages in timed 15-second sequences. |
| Fundamental overload | Receiver disruption caused by a strong signal the receiver cannot reject — the problem is in the receiver. |
| Fuse | A sacrificial device that melts to remove power when current exceeds its rating. |
| Gain (amplifier) | Output compared to input — of voltage, current, or power. |
| Gain (antenna) | The increase in signal strength in a specified direction compared to a reference antenna, achieved by focusing. |
| Gateway | An amateur station that connects other amateur stations to the internet. |
| Giga- | Metric prefix for 10⁹ (GHz = gigahertz). |
| Grace period | The two years after expiration during which a license may still be renewed — with no transmitting until the renewal is granted. |
| Grid locator | A letter-number designator for a geographic location in the Maidenhead system (e.g., "FN31"). |
| Ground rod | A metal rod driven into the earth for safety and lightning grounds; amateur towers use eight-foot rods, bonded together. |
| Harmful interference | Interference that seriously degrades, obstructs, or repeatedly interrupts a radio service. |
| Harmonic | A spurious emission at an integer multiple of the transmit frequency. |
| Hertz (Hz) | The unit of frequency: one cycle per second. |
| HF | High frequency: 3–30 MHz — the long-distance "shortwave" amateur bands. |
| Hotspot | A small personal RF gateway linking nearby digital radios to an internet network. |
| Impedance | The opposition to AC current flow — resistance plus reactance; unit ohm. |
| Inductance | The ability to store energy in a magnetic field; unit henry. |
| Inductor | A component that stores energy in a magnetic field — a coil of wire. |
| Insulator | A material that blocks current flow because it has few free electrons (glass, most plastics). |
| Integrated circuit (IC) | Many semiconductors and other components built into one package — a "chip." |
| Ionosphere | The charged upper-atmosphere region that reflects HF radio waves back to earth. |
| Ionizing radiation | Radiation energetic enough to damage cells and DNA (X-rays, gamma rays) — radio signals are not this. |
| IRLP | Internet Radio Linking Project — linking repeaters and radios through the internet, accessed on-air by DTMF codes. |
| ITU | The International Telecommunication Union, the UN agency coordinating global radio spectrum. |
| Keplerian elements | The published orbit-description numbers ("keps") that tracking programs need to predict satellite passes. |
| Kerchunking | Rudely keying a repeater without identifying — an unidentified transmission. |
| Kilo- | Metric prefix for 10³ (kHz = kilohertz, kW = kilowatt, km = kilometer). |
| Knife-edge diffraction | The bending of signals over or around a sharp obstruction between stations. |
| LED (light-emitting diode) | A diode that emits light when forward current flows — the standard visual indicator component. |
| LEO | Low Earth Orbit — a satellite orbit with a period of around 100 minutes. |
| Lightning arrester | A device on a grounded panel at the feed-line entry point that diverts lightning energy to ground. |
| Line of sight | Direct-path propagation; the normal mode for VHF and UHF. |
| Linked repeater network | A system where a signal received by one repeater is retransmitted by all repeaters in the network. |
| Loading (antenna) | Electrically lengthening an antenna by inserting inductors (coils) in the radiating elements. |
| Maidenhead | The grid-locator system of letter-number squares used to report locations. |
| Mega- | Metric prefix for 10⁶ (MHz = megahertz). |
| Mesh network | An amateur data network built from commercial Wi-Fi gear with modified firmware on amateur frequencies. |
| Meteor scatter | Bouncing VHF signals off meteor ionization trails; best on 6 meters. |
| Micro- | Metric prefix for 10⁻⁶ (µV = microvolt). |
| Milli- | Metric prefix for 10⁻³ (mA = milliampere). |
| Mixer | A circuit that converts a signal from one frequency to another. |
| Modulation | Combining speech or data with an RF carrier signal. |
| MPE (maximum permissible exposure) | The FCC's RF exposure limit, which varies with frequency (lowest at 50 MHz among the pool's bands). |
| Multimeter | A meter that measures voltage, current, and resistance. |
| Multipath | The same signal arriving over multiple paths, combining in or out of phase to cause fading. |
| Nano- | Metric prefix for 10⁻⁹. |
| National calling frequency | The designated simplex meeting frequency — 146.520 MHz on 2 meters. |
| NCS (net control station) | The station that calls a directed net to order and directs its communications. |
| Net | An organized on-air meeting run under net discipline. |
| Non-ionizing radiation | Radiation without enough photon energy to alter cells chemically — radio signals; its hazard is heating. |
| NTSC | The analog fast-scan color television standard. |
| Offset (repeater) | The difference between a repeater's transmit and receive frequencies (commonly ±600 kHz on 2 m, ±5 MHz on 70 cm). |
| Ohm (Ω) | The unit of resistance and impedance. |
| Ohmmeter | A meter that measures resistance using its own internal battery — never on a powered circuit. |
| Ohm's law | E = I × R (equivalently V = I × R): voltage equals current times resistance. |
| Oscillator | A circuit that generates a signal at a specific frequency. |
| Packet radio | Digital data sent in addressed frames with a header, checksum, and ARQ error recovery. |
| Parallel circuit | A circuit where components share the same two nodes, so the voltage is the same across all of them. |
| Part 97 | The FCC's amateur service rules (47 CFR Part 97). |
| PEP (peak envelope power) | The average power during one RF cycle at the crest of the modulation envelope — how amateur power limits are stated. |
| Phonetic alphabet | The standard word list (Alfa, Bravo, Charlie …) used to spell call signs and unusual words clearly. |
| Pico- | Metric prefix for 10⁻¹² (pF = picofarad). |
| Picket fencing | The rapid flutter on a mobile VHF signal caused by multipath as the antenna moves. |
| PL-259 | The classic "UHF" coax connector, standard at HF and VHF but not watertight and not the best choice above 400 MHz. |
| PM (phase modulation) | Impressing information on a carrier by varying its phase — a close cousin of FM. |
| Polarization | The orientation of a radio wave's electric field — vertical whip, vertical polarization. |
| Pole / throw | Switch anatomy: poles are the circuits handled; throws are the contact positions per pole (SPST, SPDT). |
| Potentiometer | An adjustable resistor — the volume-knob part. |
| Power | The rate at which electrical energy is used; unit watt. |
| Preamble | The block at the head of a radiogram carrying the information needed to track the message. |
| PSK | Phase shift keying — digital data carried by phase changes of the carrier. |
| PTT (push-to-talk) | The switch or line that keys the transmitter, switching the transceiver from receive to transmit when grounded. |
| Q signals | Three-letter abbreviations (QRM = interference, QSY = change frequency, QRZ = who is calling, QTH = location). |
| Quarter-wave vertical | A vertical antenna a quarter wavelength long (about 19 inches on 2 meters). |
| RACES | Radio Amateur Civil Emergency Service — the Part 97 civil-defense service requiring certification by a civil defense agency. |
| Radio horizon | The practical limit of direct VHF/UHF paths, slightly beyond the visual horizon because the atmosphere refracts radio waves. |
| Radiogram | A formal written message relayed by traffic nets. |
| RDF (radio direction finding) | Locating a signal source with a directional antenna and receiver. |
| Reactance | The opposition to AC from capacitance and inductance — the non-resistive part of impedance. |
| Rectifier | A circuit (usually diodes) that changes AC into varying DC. |
| Repeater | A station that simultaneously retransmits another station's signal on a different channel to extend range. |
| Resistance | The opposition to current flow of every kind — DC, AC, and RF; unit ohm. |
| Resistor | A component whose job is to oppose (limit) current flow. |
| Resonant circuit | An inductor plus a capacitor forming a frequency-selecting tuned circuit. |
| Resonant frequency | The frequency at which an antenna (or tuned circuit) naturally responds best. |
| Reverse function | A radio button that listens on the repeater's input frequency so you can hear the other station directly. |
| RF (radio frequency) | Signals in the radio part of the spectrum — and shorthand for radio energy generally. |
| RF burn | A burn to the skin caused by touching an antenna or conductor carrying strong RF. |
| RF feedback | Transmitted RF getting back into your own equipment (e.g., down the microphone cable) and distorting your audio. |
| RIT (receiver incremental tuning) | A control that nudges the receive frequency without moving the transmit frequency (also called Clarifier). |
| RST | The signal-report system: readability 1–5, strength 1–9, and tone 1–9 (tone used on CW). |
| Rubber duck | The short flexible stock antenna on a handheld — convenient but inefficient. |
| Schematic | An electrical diagram drawn with standard component symbols, showing how components connect. |
| Secondary service | A service that must not interfere with, and must accept interference from, the primary service on shared spectrum. |
| Selectivity | A receiver's ability to discriminate between nearby signals. |
| Sensitivity | A receiver's ability to detect weak signals. |
| Sequential call sign system | The FCC's default call-sign assignment method, drawing from the regional-group list for your class and address. |
| Series circuit | A circuit where the same current flows through every component in turn. |
| Simplex | Transmitting and receiving on the same frequency. |
| Skywave | Ionospherically propagated signals — the long-distance mode of HF. |
| SO-50 | The classic beginner FM satellite: uplink 145.850 MHz, downlink 436.795 MHz, woken with a 74.4 Hz tone. |
| Space station | An amateur station located more than 50 km above the Earth's surface. |
| Spin fading | The rhythmic fading of a satellite's signal caused by the satellite's rotation. |
| Sporadic E | Occasional strong beyond-horizon VHF propagation off dense E-layer patches, on 10, 6, and 2 meters. |
| Spurious emission | Any unwanted emission outside the necessary bandwidth, such as a harmonic. |
| Squelch | The circuit that mutes receiver audio when no signal is present. |
| SSB (single sideband) | A bandwidth-efficient voice mode transmitting one sideband of an AM signal with the carrier suppressed. |
| Sunspot cycle | The roughly 11-year solar activity cycle; peaks bring world-wide F-region DX on 10 and 6 meters. |
| SWR (standing wave ratio) | A measure of how well a load is matched to a transmission line — 1:1 is perfect. |
| SWR meter | An instrument that reads the match between feed line and antenna (a directional wattmeter does this job). |
| Tactical call sign | A temporary functional name ("Race Headquarters") used alongside — never instead of — the FCC call sign. |
| Talkgroup | A DMR identifier that organizes traffic so listeners hear only their chosen group. |
| Telecommand | One-way transmissions to initiate, modify, or terminate functions of a device at a distance (e.g., a space station). |
| Telemetry | Measurements sent back by radio, such as a satellite's health data. |
| Temperature inversion | A warm layer over cool air that creates tropospheric ducting. |
| Third-party communications | A message passed from one control operator to another on behalf of a non-licensed person. |
| Time slot | One of the two repeating time windows DMR uses to carry two conversations on one channel. |
| TNC (terminal node controller) | The modem-plus-controller that assembles packet frames between computer and radio. |
| Traffic | Formal written messages exchanged by net stations. |
| Transceiver | A receiver and a transmitter combined in one unit. |
| Transformer | A component that changes AC voltage up or down — never to DC. |
| Transistor | A three-region semiconductor device that works as an electronic switch or an amplifier. |
| Transponder | A satellite payload that retransmits a whole slice of spectrum on another band. |
| Transverter | A converter that moves a transceiver's RF input and output to another band. |
| Tropospheric ducting | Over-the-horizon VHF/UHF propagation through inversion-layer ducts, routinely about 300 miles. |
| Turnbuckle | The adjustable tensioning fitting in a guy line; its safety wire keeps vibration from loosening it. |
| Type N connector | The weather-resistant RF connector recommended above 400 MHz. |
| UHF | Ultra high frequency: 300–3000 MHz. |
| ULS | The FCC's Universal Licensing System — the database whose entry for your grant is your operating authority. |
| Uplink / downlink | The ground-to-satellite path and the satellite-to-ground path (U/V mode = up on 70 cm, down on 2 m). |
| USB / LSB | Upper and lower sideband; USB is the convention on 10 meters and on VHF/UHF. |
| U/V mode | A satellite operating mode with uplink in the 70-centimeter band and downlink in the 2-meter band. |
| Vanity call sign | A call sign you request by choice rather than receiving from the sequential system. |
| VE (volunteer examiner) | An accredited amateur who administers license exams as part of a team of at least three. |
| VEC (volunteer examiner coordinator) | The FCC-recognized organization that coordinates exam sessions and forwards results to the FCC. |
| VFO (variable frequency oscillator) | The circuit that sets a transceiver's operating frequency. |
| VHF | Very high frequency: 30–300 MHz. |
| VoIP | Voice over Internet Protocol — voice delivered digitally over the internet (IRLP and EchoLink are VoIP). |
| Volt (V) | The unit of electric potential (voltage). |
| Voltage | The electrical "pressure" whose difference drives electron flow. |
| Voltmeter | A meter that measures voltage, connected in parallel with the component. |
| Watt (W) | The unit of electrical power. |
| Wavelength | The distance a wave travels in one cycle — inversely related to frequency. |
| Winlink | A system that relays email over amateur radio and internet, using call-sign-based addresses. |
| WSJT-X | The free software suite home of FT8, also supporting EME, weak-signal beacons, and meteor scatter. |
| Yagi | A directional beam antenna with a driven element plus parasitic elements — the greatest gain of the pool's listed antennas. |
| Zener diode | A diode used as a voltage reference or regulator (component 10 in pool Figure T-2). |
| 5/8-wave whip | A mobile whip with more gain than a quarter-wave for VHF/UHF. |

---

## 5. Subelement → Chapter Map

From the design spec §4. Every one of the 409 pool questions is answerable after its mapped chapter; the mapping below is the ownership contract — a chapter teaches its subelement(s), and only that chapter quotes those questions in its Exam Focus. Exam weight (one question per group) is shown so writers see the stakes.

| Chapter | Title | Pool subelement(s) | Groups owned | Pool questions | Exam questions |
|---|---|---|---|---:|---:|
| ch00 | Welcome: what ham radio is & how licensing works | — (licensing process, canon §2.2) | — | — | — |
| ch01 | Electricity & radio from zero | T5, T6 | T5A–T5D, T6A–T6D | 96 | 8 |
| ch02 | How signals travel: modes & modulation | T8 (first half = T8A) | T8A | 12 | 1 |
| ch03 | Propagation: where your signal goes | T3 | T3A–T3C | 35 | 3 |
| ch04 | Antennas & feedlines | T9 | T9A–T9B | 23 | 2 |
| ch05 | Your station & equipment | T4, T7 | T4A–T4B, T7A–T7D | 67 | 6 |
| ch06 | Operating: repeaters & VHF/UHF life | T2 | T2A–T2C | 37 | 3 |
| ch07 | Digital, satellites & data | T8 (second half = T8B–T8D) | T8B, T8C, T8D | 35 | 3 |
| ch08 | The rules (Part 97, in plain English) | T1 | T1A–T1F | 68 | 6 |
| ch09 | Safety | T0 | T0A–T0C | 36 | 3 |
| ch10 | Exam day & your first radio | — (exam-day logistics, canon §2.2) | — | — | — |
| Appendix A | The complete 2026–2030 pool | all 409 verbatim + one-line "why" | all 35 | 409 | 35 |
| Appendix B | Glossary & formulas | — (canon §3, §4) | — | — | — |

Notes on the T8 split (binding): **ch02 owns T8A only** (modes and bandwidths, 12 questions, 1 exam question); **ch07 owns T8B, T8C, T8D** (satellites, operating activities, digital modes; 35 questions, 3 exam questions). The pool figures T-1, T-2, T-3 all belong to T6 and are therefore ch01 figures; their question IDs (12 total) appear in ch01's Exam Focus, and the redraws follow §1.4.

---

## 6. Copyright Ledger

**This book's standing rules:**

1. **Prose is always original.** Nothing is copied from any study guide, handbook, or web page.
2. **47 CFR Part 97 is public domain** (a work of the United States Government, 17 U.S.C. §105) and may be quoted verbatim; the FACT sentences in §2 quote it with section pinpoints.
3. **The NCVEC 2026–2030 Technician question pool is public domain** — released as such by the NCVEC Question Pool Committee on December 18, 2025 (statement on the pool's landing page) — so questions, choices, answer keys, and figure *content* may be reproduced verbatim.
4. **The three pool figures are redrawn, not copied**: original SVGs conveying exactly the official content (same components, same labels), registered in `figures/figures.json` as `kind:"original"` with the note "redrawn from NCVEC pool figure T-x" (see §1.4).
5. **Bare facts, frequencies, and formulas are not copyrightable**; exam-prep explanations are always written fresh.
6. **Archival ARRL Handbook material is optional seasoning only**, governed by the ledger below (carried over unchanged from an earlier book's accuracy canon, where each status was affirmatively determined). The book works with zero archival images.

**ARRL *Radio Amateur's Handbook* ledger (carried over — governs any optional archival figure in this book too):** determinations rest on the US Copyright Office Public Records System and the official Catalog of Copyright Entries renewal volumes; public-domain findings are affirmatively evidenced (registration age, or confirmed absence of renewal within the 28-year window), not assumed.

| Edition (year) | Status | Basis | Reproducible? |
|---|---|---|---|
| 1927 | PUBLIC DOMAIN | Published 1927; pre-1928 works are public domain under the 95-year term (entered PD 1 Jan 2023); age alone controls. | YES |
| 1931 | PUBLIC DOMAIN | 8th Edition, first published 25 Apr 1931; renewal window 1958–1959; no renewal found in the USCO ARRL-claimant RE-class search or CCE renewal volumes. Not renewed. | YES |
| 1933 | PUBLIC DOMAIN | 10th Edition, first published 4 Jan 1933; renewal window 1960–1961; zero renewal matches. Not renewed. | YES |
| 1936 | PUBLIC DOMAIN | 13th Edition, first published 13 Nov 1935 (cover-dated 1936); renewal window 1963–1964; zero renewal matches. Not renewed. | YES |
| 1940 | PUBLIC DOMAIN | 17th Edition, first published 20 Nov 1939; renewal window 1967–1968; zero renewal matches. Not renewed. | YES |
| 1941 | PUBLIC DOMAIN | 18th Edition, first published 15 Nov 1940; renewal window 1968–1969; zero renewal matches. Not renewed. | YES |
| 1951 | PUBLIC DOMAIN | 28th Edition; renewal window ~1978–1979; the comprehensive USCO ARRL-claimant RE-class query shows no Handbook renewal in any year. Not renewed. | YES |
| 1968 | PROTECTED | Published 1964–1977: renewal became automatic by statute; protected 95 years from publication. | NO |
| 1974 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1976 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1977 | PROTECTED | 1964–1977 automatic-renewal window; protected 95 years from publication. | NO |
| 1981 | PROTECTED | Published 1978 or later; protected 95 years from publication, no renewal formality applicable. | NO |
| 1983 | PROTECTED | Published 1978 or later; protected 95 years from publication, no renewal formality applicable. | NO |

**Ledger summary:** 7 of the 13 owned Handbook editions are reproducible (public domain): 1927, 1931, 1933, 1936, 1940, 1941, 1951. The 6 protected editions — 1968, 1974, 1976, 1977, 1981, 1983 — are **never reproduced** in any form: no figures, no text excerpts, no scans. `figreg.validate()` mechanically rejects any figure tagged with a protected-year source. Separately and independently of that table: FCC Part 97 and the NCVEC question pools are public domain as stated in rules 2–3 above, and everything else in this book is original prose or original SVG.

---

## 7. Resolved Uncertainties

Every uncertainty flagged during research (notes r1–r5) is closed here, with the value or wording the book will use and its source. **No open uncertainty markers remain in this canon.**

### 7.1 T1C05 — Group D call-sign format (r1's open item): RESOLVED with the FCC primary source
r1 could not pin the Group A–D call-sign formats to a fetched primary source (T1C05 carries no `[97.x]` tag; §97.3(a)(11) defines the sequential call sign system but Part 97 does not list the group formats). **Resolution:** the FCC's *Amateur Call Sign Systems* page was fetched and read in full on 2026-07-23 (<https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service/amateur-call-sign-systems>) and pins all four groups. For regions 1–10: **Group A** (Amateur Extra) = 1×2 (K/N/W + two-letter suffix), 2×1 (two-letter prefix + one-letter suffix), and 2×2 with a prefix starting with A; **Group B** (Advanced) = 2×2 with prefix starting K, N, or W; **Group C** (General, Technician, Technician Plus) = 1×3 (K/N/W + three-letter suffix); **Group D** (Novice, club, military recreation) = 2×3 with prefix starting K or W. Exhausted group lists roll to the next lower group. The pool's question T1C05 asks "Which of the following is a valid Group D call sign format for Technician class?" and keys **KF1XXX** — a 2×3 with K-first prefix, matching the FCC's Group D row exactly (distractors KA1X = 2×2 Group B format, W1XX = 1×2 Group A format). The pinned FACTs in §2.3 state the four groups with this source. The pool's own question text remains the authority for exam wording; the FCC page is the authority for why the key is correct.

### 7.2 FRN/CORES registration "free" (r2): RESOLVED with safe wording
No fetched primary sentence states that CORES/FRN registration is "free of charge"; equally, no payment step exists anywhere in the registration flow and no source mentions any charge (FCC CORES FAQ, ARRL pages, ARRL VE Manual, all re-checked 2026-07-23). **Resolution:** the book never prints "free of charge." The canonical sentence, pinned in §2.2, is: "Registering in CORES to get your FRN carries no fee and no exam requirement."

### 7.3 T1D09's printed citation `[97.113(5)(b)]` (r1): RESOLVED — citation typo in the published pool
There is no §97.113(5)(b); the operative text for T1D09's keyed answer is **§97.113(b)** (no broadcasting-related activity, except communications directly related to the immediate safety of human life or the protection of property where no other means is reasonably available). **Resolution:** the typo is preserved verbatim on the ID line in `canon/pool-technician.txt` (published form is never silently repaired); chapters and appendices cite §97.113(b) when explaining T1D09, and Appendix A reproduces the ID line as published.

### 7.4 Pool figure details (r4's corrected descriptions): RESOLVED — adopted as the redraw specification
r4's close read of the three diagram JPGs corrected earlier assumptions (notably: every ground symbol in all three figures is drawn as **three slanted strokes of decreasing length**, not the classic horizontal shrinking lines; T-2's component 9 is a rheostat-wired variable resistor; T-3's trap is that the asked component 3 is the variable inductor while the adjacent real component 2 is the variable capacitor). **Resolution:** §1.4 of this canon carries the full corrected component-by-component description of T-1/T-2/T-3 and is the binding specification for the SVG redraws.

### 7.5 Band plans vs. rules (r1, r5 watch items): RESOLVED — teach as voluntary, socially load-bearing
Part 97 contains no band plan; the only rule anchors are §97.101(a) (good engineering and good amateur practice), §97.101(b) (no frequency assigned for exclusive use), and §97.3(a)(22) (coordinators merely recommend). The CW-only bottoms of 6 m and 2 m are **emission-rule arithmetic** (§97.305), not band plans. **Resolution:** chapters present band plans, calling frequencies, and repeater offsets as voluntary community practice that the rules encourage — never as FCC mandates (pool T2A10's own wording: "a voluntary guideline"). Related wording law from r5: offsets are "**a common**" offset, not "**the**" offset — odd splits exist near band edges, so never write "the offset is 600 kHz."

### 7.6 r5 operating-color watch items: each RESOLVED as follows
- **ISS frequencies and modes change.** Per ariss.org fetched 2026-07-23: voice downlink 145.800 MHz worldwide; VHF packet 145.825 MHz; **SSTV now downlinks on 437.550 MHz (Robot36 mode)** — not the 145.800 many older guides print; the packet digipeater has gone inactive and returned over the years. Book text uses these pinned values (§2.5) and any ISS how-to box must be re-checked against ariss.org / AMSAT news close to print (§7.14).
- **Phonetic spellings.** The 26 ITU words are pinned in §2.5 with the ITU's own spellings "**Alfa**" and "**Juliett**" (chosen to guide non-English pronunciation). ARRL NTS material prints "ALPHA" (but also "JULIETT"), and some handouts write "Juliet" — mentioned, if at all, as sidebar folklore, never as doctrine. The pool tests only the technique (T2C03), never the list.
- **Tone folklore.** CTCSS/DCS is access control and selective calling, **not privacy** ("PL" is Motorola's 1951 trade name "Private Line"; every carrier-squelch receiver hears the traffic) — pinned as a §2.5 FACT. Radio manuals typically say "tone" for encode and "tone squelch" for decode; open/closed/private repeater listings are the owner's policy, not a property of the tone. Chapters program tones by frequency (e.g., 100.0 Hz), never by radio "tone number."
- **LEO period.** The pool's "around 100 minutes" (T8B10) is the pinned exam-facing value; operating color may say "roughly a 10-minute pass" (ARRL SO-50 table) but never prints a specific satellite's period without checking current orbital data.
- **CQ on repeaters.** The pool splits CQ procedure (T2A06/A08, simplex/HF) from repeater "listening" (T2A09); chapters state plainly: CQ is for simplex and HF, not repeaters.
- **RACES vs ARES.** The pool's clean split is kept: ARES = ARRL volunteer body anyone can join and drill (T2C06); RACES = government-certified civil-defense service that operates when activated (T2C04/C12).
- **"Full quieting" vs RST.** FM plain-speech reports ("full quieting," "you're scratchy") are presented as jargon color; the ARRL RST system is the SSB/CW report system; the pool tests neither's vocabulary — pinned distinction in §2.5.
- **DMR "color code ≈ CTCSS" is teaching shorthand only.** The pool's definition comes first and verbatim: a color code is an access code programmed into the radio to reach a specific repeater (T2B12); the CTCSS analogy may follow as orientation but never replaces the definition.
- **Q-signals: meaning vs. usage.** The pool tests meanings (QRM, QSY — pinned FACTs). Chapters frame Q-signals as vocabulary to recognize; on FM voice, plain words are the custom.
- **Emergency operation outside privileges (T2C09).** Framed as essentially never happening in a Technician's career; emcomm drills never suspend Part 97 (T2C01 explicitly).
- **Excluded for lack of citable source (r5's deliberate exclusions, upheld):** local-repeater anecdotes, quantitative "most repeaters" claims, and full CTCSS tone-frequency tables beyond the SO-50 tones pinned in §2.5. None of these appears anywhere in the book.

### 7.7 Satellite/ISS eligibility citations (r1): RESOLVED — cite §97.207(a) + §97.209(a)
T1B02/T1E02 are tagged §97.207(c) in the pool (bands authorized to *space stations*), but the eligibility fact — any license class may be control operator, subject to privileges — lives in §97.207(a) (space stations) and §97.209(a) (Earth stations; an operator contacting the ISS runs an Earth station). **Resolution:** chapters cite both §97.207(a) and §97.209(a) for the "any Technician may work the ISS" claim (§2.4 FACT), never implying only Extra-class hams may use satellites.

### 7.8 T1E04's tag (r1): RESOLVED — cite §97.105(b) with §97.103(b)
The pool tags T1E04 §97.103(b); the on-point text ("A station may only be operated in the manner and to the extent permitted by the privileges authorized for the class of operator license held by the control operator") is §97.105(b). **Resolution:** chapters cite §97.105(b) as primary for the privileges-of-the-control-operator rule, with §97.103(b) for the designation duty.

### 7.9 T1B12 "1500 watts above 30 MHz" (r1): RESOLVED — general ceiling with caveat
§97.313(b) sets the 1.5 kW PEP general ceiling; §97.313(d)–(h) impose lower limits in specific bands and places (e.g., 50 W PEP on 219–220 MHz per §97.313(h); geographic 70 cm/33 cm limits per §97.313(f)–(g)). **Resolution:** the pinned FACT (§2.4) always carries the pool's own caveat "except for some specific restrictions" and frames 1500 W as the general ceiling, never as a band-by-band grant.

### 7.10 T1A04 (license notification by email) (r1): RESOLVED — quote the rule, describe the practice as practice
§97.23 pins the duty to keep a working email address on the grant and the revocation/suspension consequence; the pool's answer ("Email from the FCC with a link to download the license grant") describes current FCC ULS practice, which Part 97's text does not spell out. **Resolution:** chapters pin §97.23 verbatim for the rule (§2.1 FACT) and describe the emailed-download-link mechanism as current FCC practice (§2.2 FACTs attribute the mechanics to ARRL's description of the FCC process — see §7.12).

### 7.11 Post-exam grant timing (r2): RESOLVED — typical-only wording, hard rule first
The only pinned figure is Laurel VEC's FAQ ("normally occurs the next business day after you pay the application fee"), plus the FCC's 10-day payment window; no official FCC-wide guarantee exists and VEC processing time varies. **Resolution:** the book leads with the hard rule — no transmitting until the grant appears in ULS (§2.1 FACT) — then says "typically appears the next business day after payment" (§2.2 FACT), and may add "allow a few days to about two weeks" as expectation-setting. No specific day count is ever printed as a promise.

### 7.12 10-day payment window and 30-day license-link validity (r2): RESOLVED — attributed wording
Both mechanics are sourced from ARRL's fee page and 605 instructions, not from an FCC document; the FCC sends the emails. **Resolution:** the §2.2 FACTs pin the numbers (10 calendar days; 30 days) and the book attributes the mechanics as "the FCC process as described by ARRL."

### 7.13 Remote exams (r2): RESOLVED — no universal promise
Availability depends entirely on the individual VE team; some VECs (e.g., Laurel) run in-person exams only. **Resolution:** chapters point readers at ARRL's session finder and hamstudy.org/sessions and never promise remote testing as such.

### 7.14 Time-sensitive values — verification dates and re-verify tags (r1, r2, r5): RESOLVED with this register
Each value below is pinned in §2 with its verification date. **Every one must be re-verified at the stated trigger before any reprint or new edition**, and the canon updated with the new verification date:

| Item | Pinned value | Verified | Re-verify trigger |
|---|---|---|---|
| FCC application fee | $35 (new license, renewal, rule waiver, vanity request), effective 2022-04-19 | 2026-07-23 (arrl.org/fcc-application-fee; Laurel VEC FAQ; FCC fee-schedule page) | Before each reprint (fees are set by FCC order and can change in any fiscal-year fee order) |
| ARRL VEC exam fee | $15.00 per session; $5.00 for candidates under 18 | 2026-07-23 (arrl.org/arrl-vec-exam-fees — explicitly a calendar-2026 figure) | Each January |
| NCVEC Form 605 edition | 2022 edition | 2026-07-23 (ncvec.org, HTTP 200 application/pdf) | Before publication and each reprint (the form's mandatory fields drive ch10) |
| Laurel VEC web address | https://larc-vec.org/ (laurelvec.com 307-redirects there) | 2026-07-23 | Before each reprint |
| Part 97 rule text | eCFR issue date 2026-07-21 (subpart D amended Jan. 2026 by 91 FR 1430, mainly 60 m / 2200 m / 630 m — not Technician-tested material) | 2026-07-23 (eCFR versioner API; all §2.1/§2.2 rule quotes copied from that retrieval) | Re-pull every cited section before any 2027+ reprint |
| ISS frequencies/modes | Voice 145.800 MHz; packet 145.825 MHz; SSTV 437.550 MHz Robot36 | 2026-07-23 (ariss.org) | Close to print, against ariss.org / AMSAT news |
| Pool currency | 2026–2030 Technician pool valid 2026-07-01 → 2030-06-30; Feb 19, 2026 errata incorporated | 2026-07-23 (ncvec.org; `canon/ingestion-report.md`) | Each reprint; next Technician pool due for the 2030-07-01 cycle |

### 7.15 Ingestion-level flags (ingestion report): RESOLVED
- **T9A04 "quarter-wave":** the PDF rendering split the hyphen at a line break ("quarter- wave"); the .docx — authoritative — carries `quarter-wave`, and so do the canonical files. No content difference.
- **No ARRL mirror:** arrl.org hosts no separate copy of this pool, so no NCVEC-vs-ARRL diff was possible; the two independent NCVEC renderings (.docx vs .pdf) were parsed separately and diffed instead, which the ingestion report records as the substitute cross-check of equal evidentiary value.
- **T1D12 ID line** (`T1D12 (A)[97.119(a)]`, no space before the bracket): preserved verbatim in `canon/pool-technician.txt`; never "fixed" in any quotation.

---

*End of canon. Every claim in this book traces to this file, to `canon/pool-technician.*`, or to original prose. If a chapter disagrees with this file, the chapter is wrong.*

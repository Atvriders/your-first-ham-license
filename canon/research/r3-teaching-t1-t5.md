# R3 teaching notes — Pool subelements T1–T5

**Book:** *Your First Ham License: The Technician Course (2026–2030)* — researcher R3 deliverable.
**Source:** `canon/pool-technician.json` (409-question verified NCVEC 2026–2030 pool, Feb 19 2026 errata applied).
All 213 questions in T1 (68), T2 (37), T3 (35), T4 (23), T5 (50) were read in full for this analysis.

**Conventions used below**
- Rule citations `[97.xxx]` are the references printed on the pool's own ID lines in `canon/pool-technician.txt`. Where a physics/engineering fact has no pool citation, its basis is noted as *standard textbook knowledge*.
- Group themes are quoted from the NCVEC syllabus group headings in the pool text.
- **FACT** = pure memorization item; the chapter should pin it as a FACT line.
- **TP** bullets under "Must understand" are the teaching points (counted for the coverage report).
- No T1–T5 question uses a figure (figures T-1…T-3 belong to T6/T7).
- Exam weight (from pool subelement headers): T1 = 6 exam questions (one per group), T2 = 3, T3 = 3, T4 = 2, T5 = 4 → 18 of the 35 exam questions come from these five subelements.

---

## T1 — COMMISSION'S RULES (68 questions; 6 on exam)

Overall logic to teach: the FCC wants self-regulating, interference-free, non-commercial, experimental
radio. Most "what is prohibited/required" answers follow from that. This subelement is memory-heavy;
each group below pins its FACTs.

### T1A — Purpose & permissible use of the Amateur Radio Service; license grant; basic terms; interference; RACES; phonetics; Frequency Coordinator; beacons (11 q)

**Must understand**
- TP 97.1 Basis and Purpose: the service exists for emergency communication, advancing the radio art, advancing technical *and communication* skills, a trained-operator reservoir, and international goodwill. T1A01 keys "advancing skills in the technical and communication phases of the radio art"; the distractors (personal comms for citizens, contesting) sound noble but are not in 97.1. [97.1]
- TP The FCC — not the ARRL (a private membership society), not Homeland Security — regulates and enforces amateur rules (T1A02). [97.1]
- TP Phonetic alphabets are *encouraged* on phone, never required (T1A03). [97.119(b)(2)]
- TP Licensing is now all-electronic: the FCC emails a link to download the grant (T1A04), and the official proof of the license is that it appears in the FCC ULS database (T1A05). A CSCE only proves you passed the exam. [97.23, 97.7]
- TP Automatically controlled HF propagation beacons live only on 10 m, 28.200–28.300 MHz (T1A06). **FACT.** [97.203(d)]
- TP A space station is an amateur station more than 50 km above Earth's surface (T1A07) — a definition question; distractors describe satellites generally. **FACT: 50 km.** [97.3(a)(41)]
- TP Frequency coordinators are volunteers recognized by local amateurs, chosen by the repeater/auxiliary-station operators of a region — not appointed by the FCC or ITU (T1A08–T1A09). [97.3(a)(22)]
- TP RACES control operator needs, beyond the amateur license, certification of current enrollment by a civil defense organization (T1A10). [97.407(a)]
- TP Willful or malicious interference is always prohibited (T1A11). [97.101(d)]

**Common confusions (distractor logic):** "All these choices are correct" is bait when even one listed item is false (T1A01, T1A02, T1A11). CSCE vs ULS grant (T1A05) trips almost everyone. ARRL-as-authority is a recurring wrong answer across T1.
**Vocabulary:** basis and purpose, FCC, ULS, CSCE, beacon, space station, frequency coordinator, RACES, ARES, willful/malicious interference.
**Math:** none.
**Watch items:** 28.200–28.300 MHz beacon segment; 50 km space-station altitude.

### T1B — Frequency allocations; emission modes; spectrum sharing; band edges; ISS; power output (12 q)

**Must understand**
- TP A Technician's HF phone privilege is 10 meters only, 28.300–28.500 MHz (T1B01, T1B06). **FACT.** The 28.0–28.3 MHz part of 10 m is CW/data (distractor 28.050–28.150 lives there). [97.301(e), 97.305]
- TP Above 50 MHz Technicians may use all emission types in at least some segment of every amateur band — including SSB (T1B10) and digital modes such as FT8 on 10 m, 6 m, and 2 m alike (T1B05, key "All these choices are correct"). [T1B05: 97.301, 97.305; T1B10: 97.305(c)]
- TP Band membership by number: 6 m = 50–54 MHz (52.525 MHz is inside — T1B03); 2 m = 144–148 MHz (146.52 MHz is inside — T1B04). Teach λ≈300/f (see T3B) so band *names* make sense, but the edges are memorized.
- TP CW-only segments: 50.0–50.1 MHz and 144.0–144.1 MHz, the very bottom of 6 m and 2 m (T1B07). **FACT.** [97.305(a),(c)]
- TP Secondary allocation: where amateur radio is secondary you may encounter non-amateur stations and must avoid interfering with them (T1B08). [97.303]
- TP Never transmit exactly on a band/sub-band edge: display calibration error, modulation sidebands spilling past the edge, and transmitter drift all apply — key "All these choices are correct" (T1B09). [97.101(a), 97.301(a-e)]
- TP Any US amateur, Technician class or higher, may contact the ISS on VHF; no NASA approval needed (T1B02). [97.301, 97.207(c)]
- TP Power limits: 200 W PEP for Technicians in their HF segments (T1B11); 1500 W PEP above 30 MHz except where specifically restricted (T1B12). **FACTs.** [97.313, 97.313(b)]

**Common confusions:** assuming Techs have General-style HF phone (80/40/15 m — they don't); assuming low power everywhere on VHF (1500 W surprises); PEP vs average power terminology.
**Vocabulary:** allocation, sub-band, emission mode, phone/CW/digital, PEP, primary vs secondary service, sidebands, band edge.
**Math:** none (limits are memorized).
**Watch items:** 28.300–28.500 MHz; 52.525 MHz ∈ 6 m; 146.52 MHz ∈ 2 m; 50.0–50.1 & 144.0–144.1 CW-only; 200 W HF; 1500 W above 30 MHz.

### T1C — Operator licensing: classes, call signs, places regulated, term/renewal/grace, international communications (11 q)

**Must understand**
- TP The FCC currently issues only three license classes: Technician, General, Amateur Extra; Novice, Technician Plus, and Advanced are legacy/grandfathered, no longer issued new (T1C01 — question revised by the Feb 2026 errata). [97.9(a), 97.17(a)]
- TP Vanity call signs: any licensed amateur may request one (T1C02). [97.19]
- TP International communications are limited to purposes of the amateur service plus remarks of a personal character — no business content (T1C03). [97.117]
- TP You must keep your email address current so the FCC can reach you; being unreachable can lead to revocation of the station license or suspension of the operator license (T1C04). [97.23]
- TP Group D call signs are 2×3 format like KF1XXX (T1C05). **FACT** — the only T1 question with no Part 97 ref on its ID line (format table pinned in r2 §4: Group D = 2×3; a Technician may hold Group C or D formats); distractors KA1X (2×2) and W1XX (1×2) are valid formats of *other* call-sign groups.
- TP In international waters you may operate from a US-documented vessel with the master's permission; no special FCC authorization (T1C06). [97.5(a)(2), 97.11(a)]
- TP Three clocks to keep straight: renewal may be requested up to **90 days** before expiration (T1C07) [97.21, 1.949]; license term is **10 years** (T1C08) [97.25]; renewal grace period after expiration is **2 years** (T1C09) [97.21(a)(b)]. All FACTs.
- TP You may transmit as soon as your grant appears in the FCC database (T1C10) — not when the CSCE is signed, not when mail arrives. [97.5a]
- TP During the grace period you may *renew* but may **not** transmit until the renewal is granted (T1C11). [97.21(b)]

**Common confusions:** CSCE-as-authority (T1C10); "grace period lets me keep operating" (T1C11); mixing the 90-day/10-year/2-year numbers.
**Vocabulary:** operator/primary station license grant, vanity call sign, Group D call sign, grace period, ULS, maritime mobile.
**Math:** none.
**Watch items:** 90 days / 10 years / 2 years; KF1XXX format.

### T1D — Authorized and prohibited transmissions; sale of equipment (12 q)

**Must understand**
- TP Communications are prohibited only with countries whose administration has notified the ITU that it objects (T1D01). The ARRL/IARU have no banning power. [97.111(a)(1)]
- TP Broadcasting — transmissions intended for reception by the general public (T1D10) [97.3(a)(10)] — is prohibited (T1D02) [97.113(b), 97.111(b)]. Permitted one-way transmissions are an enumerated list: emergency comms, Morse code practice, telecommand/telemetry, etc.; "announcements of ham events" is *not* one of them.
- TP Messages encoded to obscure their meaning are allowed only as control commands to space stations or model craft (T1D03). Published digital codes (FT8 etc.) are fine — obscurity is the test. [97.211(b), 97.215(b), 97.113(a)(4)]
- TP Music is authorized only when incidental to a retransmission of manned spacecraft communications (T1D04) — an absurdly narrow exception; pin it. [97.113(a)(4), 97.113(c)]
- TP No business/pecuniary interest, but you may occasionally offer your own amateur equipment for sale on the air, not on a regular basis (T1D05). [97.113(a)(3)(ii)]
- TP Indecent or obscene language is prohibited outright; no official word list exists (T1D06). [97.113(a)(4)]
- TP An auxiliary station sends one-way transmissions between a remote repeater receiver and the main repeater transmitter (T1D07). [97.113(d), 97.201(e)]
- TP A control operator may be compensated only when the communication is part of classroom instruction at an educational institution (T1D08). [97.113(a)(3)(iii)]
- TP Communications supporting broadcasting/news gathering are allowed only when directly related to the immediate safety of human life or protection of property (T1D09). [97.113(5)(b)] — tag as printed on the pool ID line; r1 flags it as a citation typo for §97.113(b).
- TP Transmitting without ID is permitted for signals controlling model craft (T1D11) [97.215], but on-the-air test transmissions must still identify the station (T1D12) [97.119(a)] — teach as a contrast pair.

**Common confusions:** "never" answers vs the narrow enumerated exceptions; equating broadcasting with any one-way transmission (code practice is legal); assuming pecuniary rules forbid all for-sale mentions.
**Vocabulary:** broadcasting, one-way transmission, auxiliary station, telemetry, telecommand, encoded to obscure meaning, pecuniary interest, third-party traffic.
**Math:** none.
**Watch items:** the exception lists (one-way permitted types; music exception; teacher compensation; model-craft no-ID).

### T1E — Control operator: eligibility, designation, privileges, duties; control point; control types (11 q)

**Must understand**
- TP A control operator is always required whenever a station transmits — "never" transmit without one, even with automatic control (T1E01). [97.7(a)]
- TP The station licensee designates the control operator (T1E03) [97.103(b)], and a station's transmitting privileges are those of the *control operator's* license class (T1E04) [97.103(b)] — not the licensee's, not the highest class present.
- TP The control point is the location at which the control operator function is performed — it need not be where the transmitter is (T1E05). [97.3(a)(14)]
- TP A Technician may *never* be control operator of a station transmitting in an Amateur Extra-only segment (outside emergencies) — designation by an Extra does not convey privileges (T1E06). [97.301]
- TP When control operator ≠ licensee, *both* are responsible for proper operation (T1E07). [97.103(a)]
- TP Three control types: local (operator physically at the station), remote (operating via a control link, e.g. over the internet — T1E10 [97.3(a)(39)], and any station may be remotely controlled — T1E09 [97.109(c)]), and automatic (the station operates itself; repeater operation is the canonical example — T1E08 [97.3(a)(6), 97.205(d)]).
- TP Any amateur authorized to transmit on a satellite's uplink frequency may be control operator of a station communicating through it (T1E02). [97.301, 97.207(c)]
- TP Definition: a control operator is the amateur operator designated by the station licensee to be responsible for transmissions and rule compliance at that station (T1E11). [97.3(a)(13)]

**Common confusions:** control operator vs licensee vs "the person talking"; computer-sent CW is *not* automatic control (an operator initiated it — T1E08 distractor); assuming the Extra-class licensee can lend privileges (T1E06).
**Vocabulary:** control operator, control point, local/remote/automatic control, station licensee, uplink.
**Math:** none.
**Watch items:** none beyond the definitions.

### T1F — Station identification; repeaters; third-party communications; club stations; FCC inspection (11 q)

**Must understand**
- TP You must make the station and its records available for inspection at any time upon request by an FCC representative — no warrant, no ten-day notice (T1F01). [97.103(c)]
- TP Station ID: transmit your FCC-assigned call sign at least every 10 minutes during a communication and at its end (T1F03) [97.119(a)]. Tactical calls ("Race Headquarters") are allowed but never replace the FCC call sign — same 10-minute rule (T1F02) [97.119(a)]. **FACT: 10 minutes.**
- TP Phone ID must be in English (T1F04) and may be sent by CW or phone emission (T1F05). [97.119(b)(2)]
- TP Self-assigned indicators are informal: "KL7CC stroke W3", "slant", "slash" are all acceptable on phone (T1F06, key "All these choices are correct"). [97.119(c)]
- TP Third-party communications = a message from one control operator to another on behalf of a non-licensed person (T1F08) [97.3(a)(47)]; with a foreign station it is allowed only if the US has a third-party agreement with that country (T1F07) [97.115(a)(2)].
- TP A repeater simultaneously retransmits another amateur station's signal on a different channel (T1F09) [97.3(a)(40)]; if it inadvertently retransmits a rules violation, the *originating* station's control operator is accountable, not the repeater owner (T1F10) [97.205(g)].
- TP A club station license grant requires at least four members (T1F11). **FACT.** [97.5(b)(2)]

**Common confusions:** "at the end of every transmission" vs the every-10-minutes rule; tactical call treated as legal ID; repeater owner liability; "three stations talking" misreading of third-party.
**Vocabulary:** tactical call sign, self-assigned indicator, third-party communications/agreement, repeater station, club station trustee.
**Math:** none.
**Watch items:** 10-minute ID rule; English ID; 4 club members.

---

## T2 — OPERATING PROCEDURES (37 questions; 3 on exam)

Mostly custom and convention rather than law — only T2C01 carries a Part 97 citation. Teach the *reason* behind each custom (courtesy, shared spectrum, repeater mechanics) and the memorized frequencies/offsets.

### T2A — Station operation: choosing a frequency, calling, test transmissions; band plans, calling frequencies, repeater offsets (11 q)

**Must understand**
- TP Repeater offset = the difference between the repeater's transmit and receive frequencies (T2A07); common offsets are ±600 kHz on 2 m (T2A01) and ±5 MHz on 70 cm (T2A03). **FACTs.**
- TP 146.520 MHz is the 2 m FM national simplex calling frequency (T2A02). **FACT.**
- TP Calling a known station on a repeater: say their call sign, then identify with yours (T2A04). CQ calls are not customary on repeaters; "break, break" is emergency language.
- TP Answering a CQ: transmit the other station's call sign followed by yours (T2A05) — called station first, always.
- TP To raise any station on simplex/phone: repeat "CQ" a few times, say "this is" + your call sign, pause to listen, repeat (T2A06). CQ means "calling any station" (T2A08).
- TP On a repeater, indicate you're monitoring by saying your call sign followed by "listening" (T2A09).
- TP A band plan is a voluntary guideline for modes/activities within a band — gentler than FCC rules but expected behavior (T2A10).
- TP Simplex = transmitting and receiving on the same frequency (T2A11); contrast with duplex repeater operation.

**Common confusions:** "full duplex" vs simplex; HF-style long CQ calls on repeaters; assuming offsets are identical on all bands (600 kHz vs 5 MHz swap is the distractor design).
**Vocabulary:** repeater offset, simplex, duplex, CQ, band plan, national calling frequency.
**Math:** none.
**Watch items:** 600 kHz (2 m), 5 MHz (70 cm), 146.520 MHz.

### T2B — VHF/UHF operating practices: FM repeater, simplex, reverse splits; CTCSS/DTMF; DMR; resolving problems; Q signals (14 q)

**Must understand**
- TP The reverse function listens on the repeater's *input* frequency so you can hear the other station directly (T2B01).
- TP CTCSS = a sub-audible tone sent with voice audio that opens a receiver's squelch (T2B02). If you hear a repeater's output but can't bring it up, wrong offset, wrong CTCSS tone, or wrong DCS code are all candidates — key "All these choices are correct" (T2B04).
- TP DTMF signaling uses two simultaneous audio tones (touch-tones) (T2B06).
- TP DMR mechanics: a color code is an access code programmed into the radio to reach a specific repeater (T2B12); a talkgroup is an identifier organizing DMR traffic so listeners hear only their group (T2B14), joined by programming the group's ID/code (T2B07).
- TP A linked repeater network retransmits signals received by one repeater on all repeaters in the network (T2B03).
- TP Talking too loudly into an FM mic overdeviates the signal, and the audio drops out on voice peaks (T2B05) — mechanism, not magic.
- TP Squelch mutes receiver audio when no signal is present (T2B13).
- TP Simplex channels exist so nearby stations can talk without tying up a repeater (T2B09).
- TP Two stations interfering on a frequency should negotiate continued shared use — nobody owns a frequency (T2B08); "first come" has no preemptive right.
- TP Q signals: QRM = interference from other stations (T2B10); QSY = changing frequency (T2B11). **FACTs.**

**Common confusions:** QRM (man-made interference) vs QRN (natural static) vs QSB (fading) — the distractors in T2B10 are exactly these; CTCSS (analog tone) vs DCS (digital code) vs DTMF (signaling tones); DMR "color code" misread as a video/CODEC thing.
**Vocabulary:** CTCSS, DCS, DTMF, squelch, deviation, reverse split, linked repeater network, talkgroup, color code, Q signals (QRM, QRN, QSB, QSY, QTH, QRZ).
**Math:** none.
**Watch items:** QRM and QSY meanings.

### T2C — Public service: emergency operations, RACES/ARES, nets and traffic, phonetics (12 q)

**Must understand**
- TP FCC rules always apply — RACES, ARES, FEMA operations included (T2C01). [97.103(a)]
- TP The only escape from license-class frequency privileges is a situation involving immediate safety of human life or protection of property (T2C09). (No ref on pool ID line; pinned in r1 §9 to §97.403.)
- TP ARES = licensed amateurs who voluntarily registered qualifications and equipment for public-service communications duty (T2C06). RACES = the FCC Part 97 service for civil defense communications in national emergencies (T2C04), and it is the one requiring certification by a civil defense agency (T2C12) — ties back to T1A10.
- TP Net discipline: the Net Control Station calls the net to order and directs communications between check-ins (T2C02); unless reporting an emergency, transmit only when directed by NCS (T2C07).
- TP "Traffic" = formal messages exchanged by net stations (T2C05). A radiogram's preamble contains the information needed to track the message (T2C10); "check" is the number of words/word equivalents in the text (T2C11). **FACT: check = word count.**
- TP Unusual words are spelled with a standard phonetic alphabet to ensure correct receipt (T2C03) — practice echo of T1A03.
- TP Winlink relays messages using email addresses based on amateur call signs (T2C08).

**Common confusions:** ARES (ARRL volunteer body) vs RACES (government civil defense) vs MARS (military) vs SKYWARN (weather spotters) — the four are routinely swapped; "check" misread as a checkbox or relay list.
**Vocabulary:** net, net control station (NCS), traffic, radiogram, preamble, check, ARES, RACES, Winlink, phonetic alphabet.
**Math:** none.
**Watch items:** RACES ↔ civil defense certification; check = word count.

---

## T3 — RADIO WAVE PROPAGATION (35 questions; 3 on exam)

Physics here is conceptual, not mathematical. One formula (λ = 300/f) and a handful of memorized
spectrum boundaries carry the whole subelement. Basis for all facts below: standard textbook
propagation/EM knowledge (no Part 97 citations on these ID lines).

### T3A — Radio wave characteristics: how a signal travels, fading, multipath, polarization, absorption; antenna orientation (12 q)

**Must understand**
- TP Multipath: signals arriving over different paths combine in or out of phase. That explains VHF strength changing when the antenna moves a few feet (T3A01), the rapid flutter on mobile signals called "picket fencing" (T3A06), irregular fading on ionospheric paths (T3A08), and increased error rates on data transmissions (T3A10). One mechanism, four questions.
- TP Vegetation absorbs UHF/microwave energy, hurting weak-signal reception (T3A02); precipitation decreases range at microwave frequencies (T3A07), but fog/rain have little effect on 10 m and 6 m (T3A12) — absorption grows with frequency.
- TP Polarization conventions: horizontal for long-distance CW/SSB weak-signal work on VHF/UHF (T3A03); cross-polarized antennas over a line-of-sight path reduce received signal strength (T3A04).
- TP Ionospherically propagated signals become elliptically polarized, so on skywave paths either antenna orientation works (T3A09) — the deliberate contrast with T3A04; teach line-of-sight vs skywave explicitly.
- TP With buildings blocking line of sight to a repeater, use a directional antenna to find a reflected path (T3A05).
- TP The ionosphere is the atmospheric region that reflects HF radio waves (T3A11); stratosphere/troposphere are the distractors.

**Common confusions:** Doppler effect and Faraday rotation appear as plausible-sounding distractors; "troposphere vs ionosphere" swaps; assuming weather hurts all bands equally.
**Vocabulary:** multipath, fading, picket fencing, polarization (horizontal/vertical/elliptical), cross-polarization, line of sight, absorption, ionosphere.
**Math:** none.
**Watch items:** none (all conceptual).

### T3B — EM wave properties: wavelength vs frequency, nature and velocity of radio waves; HF/VHF/UHF definitions (12 q)

**Must understand**
- TP A radio wave consists of an electric field and a magnetic field at right angles to each other (T3B01, T3B03); its polarization is defined by the orientation of the *electric* field (T3B02).
- TP In free space every radio wave travels at the speed of light regardless of frequency (T3B04, T3B12), approximately 300,000,000 meters per second (T3B11). **FACT: 3×10⁸ m/s.**
- TP Wavelength and frequency are inversely related: higher frequency → shorter wavelength (T3B05).
- TP Conversion formula: wavelength in meters ≈ 300 ÷ frequency in megahertz (T3B06). (Derives from c = fλ with c = 3×10⁸ m/s — standard physics.)
- TP Amateur bands are identified by approximate wavelength in meters in addition to frequency (T3B07) — hence "2 meters" ≈ 144–148 MHz (300/146 ≈ 2.05) and "6 meters" at 50–54 MHz (300/50 = 6).
- TP Spectrum boundaries: HF = 3–30 MHz; VHF = 30–300 MHz; UHF = 300–3000 MHz (T3B08–T3B10). **FACTs.**

**Common confusions:** "wavelength gets longer as frequency increases" (exactly backwards); the myth that microwaves travel faster; kHz-range distractors in the HF/VHF/UHF options.
**Vocabulary:** electric field, magnetic field, polarization, wavelength, frequency, electromagnetic wave, free space, HF, VHF, UHF.
**Math:** formula recall for T3B06; drill λ = 300/f with 300/146 ≈ 2 m and 300/50 = 6 m.
**Watch items:** HF/VHF/UHF ranges; 3×10⁸ m/s.

### T3C — Propagation modes: sporadic E, meteor scatter, auroral, tropospheric ducting, F-region skip; radio horizon (11 q)

**Must understand**
- TP VHF/UHF are normally line-of-sight: UHF signals are usually not propagated by the ionosphere, so simplex UHF rarely passes the radio horizon (T3C01).
- TP The radio horizon lies beyond the visual horizon because the atmosphere refracts radio waves slightly (T3C11).
- TP HF's defining trait: long-distance ionospheric (skywave) propagation is far more common than on VHF and above (T3C02).
- TP Sporadic E: occasional strong beyond-horizon signals on the 10-, 6-, and 2-meter bands (T3C04). **FACT: the band list.**
- TP Tropospheric ducting, caused by temperature inversions (T3C08), routinely carries VHF/UHF about 300 miles (T3C06). **FACT: ~300 miles, temperature inversions.**
- TP Knife-edge diffraction bends signals over/around obstructions between stations (T3C05).
- TP Auroral backscatter returns VHF signals distorted with a characteristic raspy sound (T3C03).
- TP Meteor scatter is best worked on 6 meters (T3C07). **FACT.**
- TP Solar cycle: the best long-distance 10 m F-region propagation is dawn to shortly after sunset during high sunspot activity (T3C09); at the sunspot peak, 6 and 10 meters can both deliver F-region DX (T3C10). **FACT: 6 & 10 m, sunspot peak, daylight.**

**Common confusions:** which mode serves which band/distance (sporadic E vs F2 vs tropo ducting); D-region *absorption* distractor for over-horizon propagation; Faraday rotation/quantum tunneling/Doppler as scientific-sounding bait.
**Vocabulary:** radio horizon, sporadic E, tropospheric ducting, temperature inversion, knife-edge diffraction, auroral backscatter, meteor scatter, sunspot cycle, F region, D region, skywave.
**Math:** none.
**Watch items:** ducting ≈300 miles; meteor scatter → 6 m; sunspot peak → 6 & 10 m daylight F-region.

---

## T4 — AMATEUR RADIO PRACTICES (23 questions; 2 on exam)

Practical station-building knowledge. Mostly "what plugs into what and why"; one formula (battery life).
Basis: standard station-engineering practice; no Part 97 citations in this subelement.

### T4A — Station setup: power source, SWR/power meter, computer & digital connections, bonding, mobile installation (12 q)

**Must understand**
- TP A typical 50 W-output mobile FM transceiver needs a 13.8 V, 12 A-class supply (T4A01). **FACT.** 13.8 V is the standard vehicle/lead-acid operating voltage, and current headroom is needed because transmitter efficiency is well under 100% (13.8 V × 12 A ≈ 166 W in for 50 W RF out).
- TP Short, heavy-gauge DC power leads minimize voltage drop while transmitting (T4A03); a mobile transceiver's negative return connects at the 12 V battery chassis ground (T4A11).
- TP An accessory SWR meter must be rated for the frequency and power level at which you'll measure (T4A02); an RF power meter installs in the feed line between transmitter and antenna (T4A05).
- TP Digital-mode interfacing moves three signals: receive audio, transmit audio, and transmitter keying (T4A06); concretely, the transceiver's speaker connector feeds the computer's line-in (T4A07), and FT8 audio flows between the radio and the computer's audio output/input running the software (T4A04).
- TP Flat copper strap is the preferred RF bonding conductor — low inductance at RF, unlike round wire or salvaged coax braid (T4A08).
- TP Battery runtime = battery ampere-hour rating ÷ average current draw of the equipment (T4A09). (Distractor divides watt-hours by *peak* power — wrong pairing of units.)
- TP A digital hotspot is a small RF gateway connecting nearby transceivers to an internet digital voice/data network (T4A10).
- TP An electronic keyer assists manual sending of Morse code (it forms the dits/dahs for you) (T4A12).

**Common confusions:** 13.8 V vs "12 volts" (nominal vs actual); ampere-hour vs watt-hour arithmetic; bonding conductor folklore (coax braid).
**Vocabulary:** SWR meter, feed line, bonding, ampere-hour, watt-hour, hotspot, electronic keyer, push-to-talk/keying, AFSK.
**Math:** T4A09 (formula; no numbers in pool) — example: 9 Ah battery ÷ 2 A average draw = 4.5 hours.
**Watch items:** 13.8 V @ 12 A for a 50 W mobile.

### T4B — Operating controls: tuning, filters, squelch, mic gain, RIT, scanning; digital transceiver configuration (11 q)

**Must understand**
- TP Excessive microphone gain on SSB produces distorted transmitted audio (T4B01) — the SSB cousin of FM overdeviation (T2B05).
- TP Enter the operating frequency with the keypad or VFO knob (T4B02); the scanning function tunes through a range of frequencies checking for activity (T4B05).
- TP To hear a weak FM signal, set the squelch threshold so the receiver audio is on all the time (squelch fully open) (T4B03); an FM signal received slightly off frequency sounds distorted (T4B04).
- TP If an SSB station's voice pitch sounds too high or low, adjust the RIT/Clarifier — it nudges the receive frequency without moving your transmit frequency (T4B06).
- TP Selectable receiver filter bandwidths let you match bandwidth to the mode, reducing noise and interference (T4B08); among the listed choices, 2400 Hz gives the best signal-to-noise ratio for SSB (T4B10). **FACT: 2400 Hz ≈ SSB bandwidth** (500 Hz suits CW; 5000 Hz is too wide for SSB).
- TP A DMR code plug is the configuration data (repeaters, talkgroups) loaded into the radio (T4B07); a specific group of stations is selected by entering the group's identification code (T4B09); a D-STAR radio must have your call sign programmed before it can transmit (T4B11).

**Common confusions:** RIT vs AF gain vs squelch (which control fixes pitch?); squelch direction — loosening to hear weak signals reads backwards to beginners; wider filter = better audio intuition fails on SNR.
**Vocabulary:** VFO, squelch, scanning, RIT/Clarifier, filter bandwidth, microphone gain, code plug, talkgroup, AGC.
**Math:** none.
**Watch items:** 2400 Hz SSB filter bandwidth.

---

## T5 — ELECTRICAL PRINCIPLES (50 questions; 4 on exam)

The math subelement: 13 prefix/dB conversions (T5B), 3 power calculations (T5C), 9 Ohm's-law
calculations + 3 formula recalls (T5D). Everything else is vocabulary. Basis: standard textbook
electricity; no Part 97 citations.

### T5A — Current and voltage: terminology and units, conductors/insulators, AC/DC (11 q)

**Must understand**
- TP Current is the flow of electrons in a circuit (T5A03), measured in amperes (T5A01); a difference in voltage is what causes that flow (T5A05 — revised by the Feb 2026 errata). Water analogy works: voltage = pressure, current = flow rate.
- TP Power is the rate at which electrical energy is used (T5A10), measured in watts (T5A02).
- TP Frequency is the number of complete AC cycles per second (T5A04), unit hertz (T5A06).
- TP Alternating current alternates between positive and negative directions (T5A09) — "positive and zero" is pulsating DC, a distractor.
- TP Resistance opposes every kind of current flow: DC, AC, and RF (T5A11, key "All these choices are correct").
- TP Metals conduct because they have many free electrons (T5A07); glass is a good insulator (T5A08) — sea water, stainless steel, and graphite all conduct.

**Common confusions:** unit-name swaps among volts/amperes/watts/ohms (every question's distractor set is the other three units); nonsense units like "amperes per second"; the AC definition halves.
**Vocabulary:** current, voltage, power, resistance, conductor, insulator, alternating current, direct current, hertz, ampere, watt.
**Math:** none.
**Watch items:** none.

### T5B — Math for electronics: conversion of units, decibels (13 q)

**Must understand**
- TP The metric prefix ladder, three orders of magnitude per step: pico (10⁻¹²) → nano (10⁻⁹) → micro (10⁻⁶) → milli (10⁻³) → base → kilo (10³) → mega (10⁶) → giga (10⁹). To convert toward a smaller unit, multiply (move the decimal right); toward a larger unit, divide (move left). Pico↔micro is a 10⁶ jump.
- TP Decibels for power ratios: dB = 10·log₁₀(P₂/P₁). Only three anchors are needed for the pool: ×2 ≈ 3 dB; ×4 ≈ 6 dB (so ÷4 ≈ −6 dB); ×10 = 10 dB. Positive = increase, negative = decrease.

**Worked examples (pool's own numbers)**
- 1.5 A = 1500 mA (T5B01); 3000 mA = 3 A (T5B06); 500 mW = 0.5 W (T5B05).
- 1,500,000 Hz = 1500 kHz (T5B02); 3.525 MHz = 3525 kHz (T5B07); 28,400 kHz = 28.400 MHz (T5B12); 2425 MHz = 2.425 GHz (T5B13).
- 1 kV = 1000 V (T5B03); 1 µV = one-millionth of a volt (T5B04); 1,000,000 pF = 10⁶ × 10⁻¹² F = 1 µF (T5B08).
- 5 W → 10 W is doubling ≈ 3 dB (T5B09); 12 W → 3 W is quarter-power ≈ −6 dB (T5B10); 20 W → 200 W is ×10 = 10 dB (T5B11).

**Common confusions:** moving the decimal the wrong way; milli/micro/mega slips; −3 dB chosen for quarter power (−3 dB is *half*; −6 dB is a quarter).
**Vocabulary:** milli-, micro-, nano-, pico-, kilo-, mega-, giga-, decibel (dB).
**Math:** all 13 questions — the ladder plus the three dB anchors covers every one.
**Watch items:** the three dB anchors as FACT lines.

### T5C — Capacitance and inductance terminology/units; RF definitions; impedance; calculating power (12 q)

**Must understand**
- TP Capacitance is the ability to store energy in an *electric* field (T5C01); unit farad (T5C02).
- TP Inductance is the ability to store energy in a *magnetic* field (T5C03); unit henry (T5C04). Teach the electric↔capacitor, magnetic↔inductor pairing to stop the swap.
- TP Impedance is the opposition to AC current flow (T5C12) — resistance plus reactance; unit ohm (T5C05). Distractors "inverse of resistance/reactance" are wrong on direction.
- TP Unit abbreviations are case-sensitive and are genuinely tested: kHz (T5C06), MHz (T5C07). Lower-case k, capital M, capital H.
- TP The power law: P = E × I (T5C08), rearranged I = P/E and E = P/I.

**Worked examples (pool's own numbers)**
- 13.8 V × 10 A = 138 W (T5C09).
- 12 V × 2.5 A = 30 W (T5C10).
- 120 W ÷ 12 V = 10 A (T5C11).

**Common confusions:** farad vs henry swaps; P = E/I and P = I²×E formula distractors; case-pedantry answers (khz, KHZ) dismissed as trivial — they are the question.
**Vocabulary:** capacitance, farad, inductance, henry, impedance, ohm, reactance, kHz, MHz.
**Math:** T5C08 formula recall + T5C09–T5C11 computations.
**Watch items:** kHz/MHz capitalization as FACT lines.

### T5D — Ohm's Law; series and parallel circuits (14 q)

**Must understand**
- TP Ohm's law triangle: E = I × R, I = E/R, R = E/I (T5D01–T5D03). Teach the cover-the-unknown triangle: E on top, I and R below.
- TP Series circuit: the current is the same through all components (T5D13); parallel circuit: the voltage is the same across all components (T5D14). Memory hook: "series = same current" (both S).

**Worked examples (pool's own numbers)**
- Resistance: 90 V ÷ 3 A = 30 Ω (T5D04); 12 V ÷ 1.5 A = 8 Ω (T5D05); 12 V ÷ 4 A = 3 Ω (T5D06).
- Current: 120 V ÷ 80 Ω = 1.5 A (T5D07); 200 V ÷ 100 Ω = 2 A (T5D08); 240 V ÷ 24 Ω = 10 A (T5D09).
- Voltage: 0.5 A × 2 Ω = 1 V (T5D10); 1 A × 10 Ω = 10 V (T5D11); 2 A × 10 Ω = 20 V (T5D12).

**Common confusions:** every distractor is the wrong operation on the same two numbers (e.g. T5D04: 90×3 = 270, 3/90 = 1/30); series/parallel property swap; units drift (amperes vs volts vs ohms in the answer list).
**Vocabulary:** resistance, ohm, Ohm's law, series circuit, parallel circuit.
**Math:** 12 of 14 questions (3 formula recalls + 9 computations); T5D04–T5D12 drill the triangle in all three orientations.
**Watch items:** none beyond the formulas themselves.

---

## Cross-subelement distractor patterns (for chapter sidebars)

- **"All these choices are correct":** the keyed answer in T1B05, T1B09, T1F06, T2B04, T5A11 (T1B10's key "in at least some segment of all these bands" is a near-variant); bait in T1A01–T1A03, T1A05, T1A11, T1B07, T1C05, T1D08, T1D12, T1F07, T1F11, T2C02, T2C03, T2C07, T3B07, T3C10, T4B02, T4B11, T5A09. Rule of thumb to teach: pick it only after checking *every* listed item is true.
- **Wrong-operation arithmetic:** T5C/T5D distractors multiply where the key divides (and vice versa) using the same numbers — drill the triangles, not the answers.
- **Authority shell game:** FCC vs ARRL vs ITU vs IARU vs frequency coordinator vs NASA (T1A02, T1A08–09, T1B02, T1D01). Only the FCC regulates; only the ITU receives country objections.
- **Narrow-exception structure:** prohibition questions (T1D) key on memorized exception lists; "never" answers are usually wrong when a Part 97 exception exists, right for willful interference (T1A11) and control-operator absence (T1E01).

## Ambiguous / surprising questions flagged for writers

- **T1C05** — the only T1 question with no Part 97 ref on its ID line; requires the call-sign-group format table (Group D = 2×3). Its distractors are valid formats of other groups, so "all look right."
- **T1A04 / T1A05 / T1C04 / T1C10** — this pool is fully in the email/ULS era (no paper license from the FCC, email reachability required). Older study guides that say "wait for the license in the mail" are wrong for 2026–2030.
- **T1C01 & T5A05** — revised by the Feb 19 2026 NCVEC errata (per `canon/ingestion-report.md` §1); chapter text must match the revised wording.
- **T1B12** — 1500 W PEP for Technicians above 30 MHz contradicts the beginner intuition "Tech = low power."
- **T1E06** — absolute "at no time": designation by an Extra licensee does not extend privileges (contradicts T1E03/E04 intuitions about designation).
- **T1D04** — the music exception (manned spacecraft retransmission only) is bizarrely specific; pure FACT pin.
- **T1F06** — "stroke", "slant", and "slash" are *all* acceptable spoken separators; the exam tolerates informality.
- **T2B05** — "talking too loudly" causes FM audio dropouts (overdeviation); the phrasing surprises — teach the mechanism.
- **T2B08** — "negotiate continued use" contradicts folk belief in first-come frequency rights.
- **T4B03** — answer wording "receiver output audio is on all the time" (squelch open) reads counterintuitively; explain squelch direction.
- **T3A04 vs T3A09** — cross-polarization matters on line-of-sight but not on skywave (elliptical polarization); these two must be taught together or they look contradictory.
- **T1D11 vs T1D12** — deliberate contrast pair: no-ID model-craft control vs must-ID test transmissions.

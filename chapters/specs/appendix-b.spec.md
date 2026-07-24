# Writer Spec — Appendix B. Glossary & Formulas

**Output file:** `appendices/glossary-and-formulas.md` (this exact filename — the audit's TOC check #3 looks for it)
**Target length:** reference material, excluded from the prose target; the glossary alone is ~235 entries × one line.
**Pool coverage:** none — no pool quotes required here. Content comes from canon §4 (glossary) and canon §3 (notation & units), which are binding.

## 1. Purpose

The beginner's back-of-book reference: every term the book uses, defined plainly in one line, plus the book's handful of formulas each with a worked micro-example. Not narrated in the audiobook (chapters 00–10 only).

## 2. Structure

- First line: `## Appendix B. Glossary & Formulas` (appendices are exempt from the chapter format laws — the audit's `check_format_laws` only applies to `chNN` stems — but keep the `## Appendix …` heading shape for the TOC).
- One short intro paragraph: how to use the appendix (definitions match the chapters; formulas carry micro-examples).
- `### Glossary` — the full table from canon §4.
- `### Formulas` — the canon §3 relations with micro-examples (§4 below).

## 3. The glossary (`### Glossary`)

- **Source is canon §4 and only canon §4.** It carries ~235 terms (234 term rows in the canonical table) as `| Term | Definition |` — consolidate them into this appendix **byte-exact**, terms alphabetical as published (the canon table is already A→Z, ending with "5/8-wave whip").
- Keep the canon's one-line definitions verbatim — they are binding (canon §4: "a chapter may expand a definition but must not contradict it"). Do not add terms of your own, do not drop any, do not reword.
- Format: a two-column markdown table (`| Term | Definition |` with the `|---|---|` separator) mirrors the canon and renders cleanly in the build. Group-letter subheadings (A, B, C …) are optional; if used, they are plain bold lines, not `####` headings, so the TOC stays flat.
- Sanity check before finishing: the row count matches the canon's and a `diff` of the two tables shows no wording drift (mechanical copy, not retype).

## 4. The formulas (`### Formulas`)

Present each relation from canon §3 with a one-line plain statement and a worked micro-example using the pool's own numbers. Cover exactly these (the book's complete formula set — nothing more):

| Formula | Plain statement | Micro-example (pool numbers) |
|---|---|---|
| **V = I × R** (Ohm's law; pool prints E = I x R) | Voltage equals current times resistance; rearranged I = V / R, R = V / I. | 12 V across a resistor with 1.5 A through it: R = 12 ÷ 1.5 = 8 Ω (T5D05). |
| **P = V × I** (pool prints P = I x E) | Power equals voltage times current; rearranged I = P / V, V = P / I. | 13.8 V supply delivering 10 A: P = 13.8 × 10 = 138 W (T5C09). |
| **λ(m) = 300 / f(MHz)** | Wavelength in meters equals 300 divided by frequency in megahertz — the pool's own approximation of λ = c / f with c ≈ 3×10⁸ m/s, never an exact identity. | 300 ÷ 146 ≈ 2.05 m — the 2-meter band; 300 ÷ 50 = 6 m (T3B06). |
| **Prefix ladder** | pico (10⁻¹²) → nano (10⁻⁹) → micro (10⁻⁶) → milli (10⁻³) → base → kilo (10³) → mega (10⁶) → giga (10⁹); toward a smaller unit multiply, toward a larger unit divide. | 3.525 MHz = 3525 kHz (T5B07); 1.5 A = 1500 mA (T5B01). |
| **dB anchors** | ×2 ≈ 3 dB; ×4 ≈ 6 dB (so ÷4 ≈ −6 dB); ×10 = 10 dB. The defining formula dB = 10·log₁₀(P₂/P₁) may be shown here once, labeled optional. | 12 W → 3 W is quarter power ≈ −6 dB (T5B10); 20 W → 200 W is ×10 = 10 dB (T5B11). |
| **Battery runtime** | Runtime (hours) = battery ampere-hour rating ÷ average current draw. | 9 Ah ÷ 2 A = 4.5 hours (T4A09's formula). |
| **Duty cycle** | Duty cycle = transmit time ÷ total time (percent); allowable power density scales inversely with it. | 30 s transmitted per 5 minutes: 30 ÷ 300 = 10%; halving duty cycle (100% → 50%) doubles allowable power density (T0C03). |

Also include, as a short note block, the canon §3 **notation & units laws** a reader will meet in the pool and the book:

- The pool prints **E** for voltage and "x" for multiplication ("P = I x E"); this book's prose uses **V** and ×. E and V both mean volts.
- Unit case is load-bearing: **kHz** (lowercase k), **MHz**/**GHz** (capital M/G), always capital H; mA, µV, pF follow the same prefix case rules.
- c = 3×10⁸ m/s = 300,000 km/s is the working value (299,792,458 m/s exact, never needed).
- Inline math in this appendix uses the same `$…$` style as the chapters where an expression is displayed.

## 5. Integrity notes

- Appendices are exempt from the chapter format laws (no Exam Focus, no Key Takeaways, no FACT-line requirement) — but banned phrases still apply nowhere ("little did they know", "in that moment", "a testament to").
- Everything here traces to canon §3/§4 or to pool numbers already pinned in the canon — introduce no new facts, no new terms, no new formulas.
- Alphabetization, spelling, and punctuation of terms match the canon byte-exactly (watch the µ in "µV" entries and the en-dashes in ranges).

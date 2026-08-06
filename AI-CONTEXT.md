# AI-CONTEXT — Your First Ham License: The Technician Course (2026–2030)

This document is a complete, machine-oriented context dump for AI models (and humans)
working with this repository. It contains everything needed to understand, extend,
adapt, or continue *Your First Ham License: The Technician Course (2026–2030)* without
contradicting the finished book: what the book is and who it is for, the accuracy-canon
discipline, the pool record, the chapter/subelement map, the format laws, the
pool-fidelity rules, the figure pipeline, the tooling, the series-site machinery, the
copyright ledger, the time-sensitive register, how to extend the series, and the
production history. Treat **`accuracy-canon.md`** (plus its companion canonical pool
files under `canon/`) as law — the published chapters already conform to it exactly,
and this file only summarizes it.

Credentials, API tokens, and personal contact details from the production session are
deliberately omitted.

---

## 1. What this is

*Your First Ham License: The Technician Course (2026–2030)* is an **85,427-word**
beginner course + exam-prep book for the **US Technician class amateur radio license
(Element 2, 2026–2030 NCVEC question pool)**: **49,393 words across 11 chapters**
(ch00–ch10: 2,636 / 4,844 / 4,507 / 4,638 / 4,614 / 5,523 / 4,571 / 4,696 / 5,643 /
4,860 / 2,861) plus **2 appendices** (Appendix A, the complete annotated pool, 30,969
words; Appendix B, glossary & formulas, 5,065 words), with **40 original figures**.

The audience is the **absolute beginner** — a reader with no electronics background, no
radio experience, and possibly exam anxiety. Every concept is taught plainly first,
then tied to the exact pool questions it answers. The book does two jobs at once:
teaches amateur radio as a beginner actually encounters it, and prepares for the exam —
after reading a chapter, the reader can answer every question in its mapped pool
subelement(s). Spine: *your first contact* — curious → how it works → how to operate →
the rules → safety → exam day → what's next.

This is **Book 2 of the three-book "Your First Ham License" program**, following Book 1
(*200 Meters and Down*, a technical history of amateur radio — not exam prep). Books 3
(General) and 4 (Extra) inherit this book's template. Production machinery (build,
audit, figures, audiobook, Docker) is inherited from Book 1 and retargeted; new here
are the verbatim-pool integration and `tools/make_exam.py`.

## 2. The accuracy canon is LAW

**`accuracy-canon.md`** is the single, binding source of truth for every pool wording,
number, date, notation choice, glossary definition, chapter mapping, and copyright
determination in the book. Where a draft ever disagreed with the canon, the canon won.
**Prose is always original** — facts, 47 CFR Part 97, and the NCVEC pool are public
domain and free to quote; everything else is written fresh.

What the canon pins down (read the file before adding or changing any fact):

- **§1 Pool record** — the canonical pool files and their provenance (§3 below).
- **§2 Pinned facts with sources** — the fact reservoir. Each line is
  `- **FACT:** <one self-contained sentence> — Source: <§ or URL>`. Chapter writers
  copy the sentence **verbatim** (minus the trailing source tag) into their chapters;
  the build audit greps every chapter `**FACT:**` line for an exact match in this file
  (check #5). Rule quotations are verbatim from the **eCFR text of 47 CFR Part 97,
  issue date 2026-07-21** (pulled 2026-07-23).
- **§3 Notation & Units** — one symbol set (V, I, R, P, f, λ, c, C, L, Z). The pool
  prints **E** for voltage and a plain "x" for multiplication; this book's prose uses
  **V** and **×** — chapters teach the equivalence on first use, and verbatim pool
  quotes always keep the pool's E/x form. Unit case is load-bearing (kHz, MHz, mA, µV,
  pF). The pool's own shortcut **λ(m) = 300 / f(MHz)** is taught as an approximation of
  c = f·λ, never an exact identity.
- **§4 Glossary** — canonical one-line definitions (235 terms feed Appendix B); a
  chapter may expand a term but must not contradict it.
- **§5 Subelement → chapter map** — the ownership contract (§4 below).
- **§6 Copyright ledger** — (§9 below).
- **§7 Resolved uncertainties** — every research flag closed to a sourced value or a
  deliberately careful wording (15 subsections; highlights in §7 of this file). **No
  open uncertainty markers remain**; the audit greps for `UNVERIFIED` (check #6).

## 3. The pool record (canon §1)

The 2026–2030 Technician pool is carried as **canonical files — the only quoting
sources**:

| File | Bytes | sha256 |
|---|---:|---|
| `canon/pool-technician.txt` | 109,214 | `0796b92ebdfe341de22437ba6c185f5cb91c010e58f6ac1f41c05e2a0de90f1b` |
| `canon/pool-technician.json` | 170,569 | `cced9eb89f74f56cd5f195c3b4dd7e10ec09eb66238c1134f269821055a27918` |

The `.txt` is the byte-exact human-readable rendering (ID lines `T1A01 (C) [97.1]`,
`~~` separators, published headings); the `.json` is the structured form
(`{id: {group, subelement, question, choices{A–D}, answer, figure}}`). Question text,
choices, and answer letters are quoted from these two files **only** — never from
memory, web mirrors, or study guides.

Key facts:

- **409 questions**, 10 subelements (T1–T9, T0), **35 groups**; every question has
  exactly 4 choices A–D and one keyed answer. **The exam: 35 questions, one drawn from
  each group; 26 correct to pass** (47 CFR §97.503(a)).
- **Valid for exams 2026-07-01 through 2030-06-30.** Released into the **public
  domain** by the NCVEC Question Pool Committee **2025-12-18**; **revised 2026-02-19**
  (errata modifying 4 questions — the published pool body already incorporates them,
  and this book always uses the revised form):
  T1C01 (D), T5A05 (A), T7A09 (B), T0A10 (A).
- **Provenance:** downloaded 2026-07-23 from ncvec.org into `canon/source/` (sha256s
  in canon §1.2); parsed from the `.docx` (authoritative) and independently re-parsed
  from the `.pdf` with `pdftotext -layout`; the two agreed on all 409 questions, all
  1,636 choices, all answer letters, and all headings except one PDF-side line-wrap
  artifact (T9A04 "quarter- wave" — the canonical files carry `quarter-wave`). Full
  evidence in `canon/ingestion-report.md`.
- **Published quirks are preserved, never repaired:** the T1D09 ID-line citation typo
  `[97.113(5)(b)]` (the operative rule is §97.113(b) — chapters cite that when
  explaining) and `T1D12 (A)[97.119(a)]` with no space before the bracket. Published
  Unicode punctuation (curly quotes U+2019/U+201C/U+201D in 35 questions; en dash
  U+2013 in headings) is preserved byte-exactly, never converted to ASCII.
- **Pool figures T-1, T-2, T-3** (12 questions, all in T6): redrawn as original SVGs,
  never copied (§6 below); canon §1.4 carries the binding component-by-component redraw
  specification (including the corrected detail that every ground symbol is drawn as
  three slanted strokes of decreasing length).

## 4. Chapter / subelement map (canon §5)

Every one of the 409 pool questions is answerable after its mapped chapter; a chapter
teaches its subelement(s), and only that chapter quotes those questions in its Exam
Focus.

| Chapter | Title | Pool subelement(s) | Pool questions | Exam questions |
|---|---|---|---:|---:|
| ch00 | Welcome: What Ham Radio Is & How Licensing Works | — (licensing process) | — | — |
| ch01 | Electricity & Radio from Zero | T5, T6 | 96 | 8 |
| ch02 | How Signals Travel: Modes & Modulation | T8A | 12 | 1 |
| ch03 | Propagation: Where Your Signal Goes | T3 | 35 | 3 |
| ch04 | Antennas & Feedlines | T9 | 23 | 2 |
| ch05 | Your Station & Equipment | T4, T7 | 67 | 6 |
| ch06 | Operating: Repeaters & VHF/UHF Life | T2 | 37 | 3 |
| ch07 | Digital, Satellites & Data | T8B, T8C, T8D | 35 | 3 |
| ch08 | The Rules (Part 97, in Plain English) | T1 | 68 | 6 |
| ch09 | Safety | T0 | 36 | 3 |
| ch10 | Exam Day & Your First Radio | — (exam-day logistics) | — | — |
| Appendix A | The Complete 2026–2030 Pool | all 409 verbatim + one-line why | 409 | 35 |
| Appendix B | Glossary & Formulas | — (canon §3, §4) | — | — |

The T8 split is binding: **ch02 owns T8A only**; **ch07 owns T8B–T8D**. The pool figures
T-1/T-2/T-3 all belong to T6 and are therefore ch01 figures; their 12 question IDs
appear in ch01's Exam Focus.

## 5. Format laws

### 5.1 Chapter skeleton (audit check #7)

Every teaching chapter (ch01–ch09) follows one fixed skeleton so parallel writers
produce one coherent book:

1. First line exactly `## <N>. <Title>`.
2. **Opener** — one short plain-language paragraph (a concrete new-ham scenario plus
   "in this chapter you'll learn …"). No epigraph device (that was Book 1's form).
3. **Teaching sections** (`### …`) — plain language, analogies, figures as `{{fig:id}}`
   on their own line, inline math `$…$` only where the pool needs it; optional
   `> **The math, if you want it:**` sidebars for anything beyond arithmetic.
4. **≥1 `> **Worked example:**` blockquote** — a real, simple calculation worked end
   to end, using the pool's own numbers.
5. **`### Exam Focus`** — opens with the coverage line (subelements, groups, question
   counts, exam weight), then 5–10 verbatim pool questions with correct answer and a
   one-line plain-language why (quote format in §5.4).
6. **`### Key Takeaways`** — 4–8 bullets.
7. **3–5 `**FACT:** <sentence>` lines** as standalone plain paragraphs (never inside
   blockquotes — the audit's FACT regex won't see them there), copied **byte-exact**
   from `accuracy-canon.md`.

ch00 and ch10 follow the same skeleton minus Exam Focus and the worked-example rule
(ch00 gets "Your first checklist", ch10 gets "Your 30-day plan"); the audit exempts
exactly those two stems. Banned phrases everywhere: *"little did they know"*, *"in that
moment"*, *"a testament to"*. Nonfiction integrity: no fabricated quotations;
anecdotes are plainly framed as illustrative scenarios, never attributed to real
people.

### 5.2 Appendix A format (audit check #8 parses this exactly)

All 409 questions, exactly once each, in canonical pool order (subelements T1…T9 then
T0; group A–F; ascending number — the audit's `pool_sort_key`). One `###` section per
subelement with the published title and counts; optional `####` group lines. Every
entry is one blockquote in exactly this shape, followed by one plain line carrying the
published ID line:

```
> **T1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: C** — <one-line why, naming the teaching chapter: "… — taught in chapter 8.">

Published ID line: `T1A01 (C) [97.1]`
```

The published ID line rides on a **separate plain-text line after the blockquote, in
backticks** — never inside the quote itself (the audit would read it as part of the
question text). Where a question references a pool figure, the corresponding redrawn
SVG is embedded on the line before its first referencing quote (`{{fig:ch01-pool-fig-t1}}`
etc.) and named ("Figure T-2, above") thereafter. Appendix A is **print-only — never
narrated** in the audiobook (decision locked).

### 5.3 Appendix B format

Glossary as a two-column table (235 terms, the canon's §4 definitions verbatim) then
the formula set: **7 formulas** (Ohm's law, the power law, the wavelength shortcut,
the prefix ladder, decibels by anchors, battery runtime, duty cycle), each with a plain
statement and one worked example using the pool's own numbers, plus a notation-and-units
subsection (E/x vs V/×, unit case, c, f = 1/T).

### 5.4 Build-dialect constraints (what `tools/build_book.py` actually parses)

The builder parses a small fixed markdown dialect; writers must stay inside it:

- **Consecutive non-blank lines join into one paragraph.** Therefore bullets (Key
  Takeaways, checklists) are **blank-line-separated** — each `-` item stands alone
  between blank lines, or the parser would merge them into a single paragraph.
- **A blockquote is consecutive `>` lines joined with spaces.** The six-line Exam
  Focus / Appendix A quote block works because of this; any `>` line directly adjacent
  to it would be absorbed into the same block. Blockquote classes: a quote starting
  `**The math, if you want it:**` renders as a sidebar; `**Worked example:**` as a
  worked example; anything else as a plain quote.
- **Inline math is `$…$`, rendered to SVG at build time** (`tools/mathsvg.py`). Keep
  it to **at most one `$…$` span per paragraph**, keep expressions simple (the pool's
  math is arithmetic only), and never use a literal `$` (e.g. "$35") inside a math
  paragraph — write "35 dollars" in prose or keep currency out of math paragraphs.
- Figures are `{{fig:id}}` on their own line, resolved against `figures/figures.json`;
  `***` is a section rule; `####` headings render as anchored `<h4>`s (Appendix A group
  headings) and never enter the TOC; emphasis is `**bold**` / `*italic*`.
- The audit's Exam Focus quote regex (`> **T#X##** <text>` + `**Answer: L**`) is the
  exact contract for every pool quote in chapters and appendices.

## 6. Figures

**40 original figures** (`figures/figures.json` is the registry; `figures/*.svg` the
assets — one SVG per registry entry):

- **Hand-authored themeable SVG schematics/diagrams** using `currentColor` so they
  render correctly in both light and dark themes — e.g. `ch01-ohms-law-triangle.svg`,
  `ch04-dipole.svg`, `ch06-repeater-offset.svg`, `ch09-grounding.svg`.
- **Matplotlib-plotted curves**, generated by paired `_gen_<id>.py` scripts, committed
  as static SVG and **post-processed black → `currentColor`** — e.g.
  `_gen_ch04-swr-curve.py` → `ch04-swr-curve.svg`, `_gen_ch08-tech-band-chart.py`,
  `_gen_ch07-doppler-curve.py`.
- **The 3 NCVEC pool figures redrawn as original SVGs** (`ch01-pool-fig-t1/2/3.svg`):
  same components, same labels, same numbered callouts as the official diagrams —
  never copies of the published graphics. Registered as `kind:"original"` with the note
  "redrawn from NCVEC pool figure T-x"; canon §1.4 is the binding redraw specification.
  The pool is public domain, so this is both safe and faithful; the redraw rule keeps
  the book's visual style consistent and themeable.

Every registry entry carries id, chapter, number, caption, kind, source, file, and a
one-line **spoken** description (used by the narration transform so figures degrade
gracefully in audio). Every figure is embedded inline in the built HTML. `figreg`'s
`validate()` enforces existence, copyright tags, and the protected-years rule, and the
audit checks figure integrity (#1) and copyright tags (#2) at build time.

## 7. Tooling inventory

All Python 3, stdlib-first (`matplotlib` for plots, `edge-tts` + `ffmpeg` for audio,
headless Chromium/Chrome → weasyprint for best-effort PDF). Every runnable script keeps
the repo-root `sys.path` bootstrap so it works both as `python3 tools/<x>.py` and as an
imported module.

- **`tools/build_book.py`** — parses the fixed dialect and produces the self-contained
  single-file **HTML** edition (inline SVG figures, inline math SVG, linked TOC,
  light/dark themes, **series book-switcher bar**, no external references), the plain
  **TXT** edition (math spoken as words, figures as `[Figure: ID]`), and the
  best-effort **PDF**. Also holds `SERIES_BOOKS` / `SERIES_CURRENT` (§8).
- **`tools/audit_book.py`** — the verification gate; exits non-zero on any failure.
  **8 checks:** (1) figure integrity, (2) copyright tags, (3) TOC/anchor consistency,
  (4) math rendering (every `$…$` span renders), (5) canon cross-check of every
  `**FACT:**` line, (6) no `UNVERIFIED` markers left in the canon, (7) format laws
  (skeleton + banned phrases), (8) **pool fidelity** — new in this book, see §7.1.
- **`tools/mathsvg.py`** — inline `$…$` → embedded SVG.
- **`tools/figreg.py`** — loads/validates `figures/figures.json`; protected-years set
  (1968–1983) unchanged from Book 1.
- **`tools/narration.py`** / **`tools/make_audiobook.py`** — the 8-voice edge-tts
  audiobook pipeline (US/British/Australian/Irish × male/female), **chapters 00–10
  only** (the verbatim pool appendix is never narrated); **`tools/make_intro.py`**
  generates the spoken introduction. `docker/audiobook-index.html` is the player (§8).
- **`tools/make_exam.py`** — the practice-exam generator (new in this book):
  `python3 tools/make_exam.py [--seed N] [--out build/] [--pool canon/pool-technician.json]`
  draws exactly **one question per NCVEC group** (35 groups → a valid 35-question
  exam), uniform random within group, reproducible with `--seed`; writes
  `build/practice-exam.md` (questions + choices A–D, **never the answers**) and
  `build/practice-exam-key.md` (letters + subelement tally).
- **`tests/`** — 50 pytest tests covering all tooling (including check #8 fixture
  tests: a correct quote passes; a one-word-off quote fails; a wrong answer letter
  fails; missing pool → skip) plus a relative-links test on the built HTML.

### 7.1 Pool-fidelity rules (audit check #8)

- Question text, choice text, and answer letters are quoted **byte-exact** from
  `canon/pool-technician.*` (the audit compares whitespace-normalized against the
  `.json`). Published Unicode punctuation is preserved; never paraphrase a question.
- Every quoted id must exist in the pool; every stated answer letter must match the
  pool key; Appendix A must contain **all 409 ids exactly once, in canonical pool
  order**. The audit mechanically verifies 409/409 coverage, every quote, and every
  letter — it is the backstop that makes silent pool drift impossible.
- The 4 revised questions (T1C01, T5A05, T7A09, T0A10) are always used in their
  **revised 2026-02-19 form** — the canonical files already carry it; quote, don't
  retype.
- The published quirks (T1D09 citation typo, T1D12 missing bracket space) are
  reproduced as published in every quotation, never silently repaired.
- Check #8 **skips gracefully** (printed note, not failure) when the pool JSON is
  absent, so the audit still gates a bare scaffold.

## 8. Series-site machinery

The book is one of three in the *Your First Ham License* series (Technician / General /
Extra) and carries the shared machinery; General and Extra ship later and inherit it.

- **Book-switcher bar** — a slim series bar in both the generated book HTML
  (`tools/build_book.py`, driven by `SERIES_BOOKS = [("Technician","/tech/",True),
  ("General","/general/",False), ("Extra","/extra/",False)]` and `SERIES_CURRENT =
  "Technician"`) and the audiobook player. Shipped books are links, current book
  highlighted, unshipped books render as inert "coming soon" labels. Flip a book's flag
  to `True` when it ships.
- **Stable sub-paths** — the books mount at `/tech/`, `/general/`, `/extra/` behind a
  series nginx proxy. **Book HTML uses only relative/anchor links** (enforced by a
  build test; the only absolute links allowed are the three series paths), so sub-path
  proxying needs no response rewriting.
- **`series/`** — `series/nginx.conf` (proxy: `=` `/` → landing page; `/tech/` → the
  tech container, active; `/general/` and `/extra/` blocks commented out until those
  books ship), `series/index.html` (the landing page: three cover-style cards,
  unshipped books marked "coming soon"). **`series-docker-compose.yml`** wires the
  three book images plus the proxy (the only published port, host :8080); General/Extra
  services sit behind the `future` profile so `up` never pulls placeholders. Each
  book's standalone image (`docker-compose.yml`, also :8080) runs fine alone.
- **Audiobook player** (`docker/audiobook-index.html`) — themed page with 12 tracks
  (intro + 11 chapters), a **voice switcher** grouped by accent (8 voices: Andrew, Ava,
  Ryan, Sonia, William, Natasha, Connor, Emily), continuous chapter-to-chapter
  playback, a live visualizer, and **resume** (voice/track/position persisted in
  `localStorage` under `yfhl-audio`). The **"Auto-play next chapter" toggle**
  (default ON, persisted alongside; when OFF, playback stops at each chapter end) was a
  user-requested addition — the `ended` handler auto-advances only when the toggle is
  on.
- **Hosting/CI** — `Dockerfile` (nginx serving `build/index.html`, the TXT/PDF,
  `chapters/`, and `audiobook/` with the player at `/audiobook/`); GitHub Actions
  (`.github/workflows/build.yml`, push to `master`/`main` or `workflow_dispatch`)
  fetches the audiobook from **release v1.0** (intro + 8 voices × 11 chapters),
  rebuilds the book, and pushes `ghcr.io/atvriders/your-first-ham-license:latest`.
  GitHub-only CI; no Gitea path. **Audio ships on the release, not in git.**

## 9. Copyright ledger summary

- **Prose is always original.** Nothing is copied from any study guide, handbook, or
  web page.
- **47 CFR Part 97 is public domain** (US Government work, 17 U.S.C. §105) and is
  quoted verbatim with section pinpoints (eCFR issue date 2026-07-21).
- **The NCVEC 2026–2030 Technician pool is public domain** (released as such by the
  NCVEC Question Pool Committee, 2025-12-18): questions, choices, answer keys, and
  figure *content* may be reproduced verbatim.
- **The 3 pool figures are redrawn, not copied** (§6).
- **Bare facts, frequencies, and formulas are not copyrightable**; all exam-prep
  explanations are written fresh.
- **ARRL Handbook ledger (carried from Book 1, governs any optional archival
  figure):** of the 13 owned editions (1927–1983), **7 are public domain and
  reproducible** (1927, 1931, 1933, 1936, 1940, 1941, 1951 — each affirmatively
  evidenced) and **6 are protected and never reproduced in any form** (1968, 1974,
  1976, 1977, 1981, 1983). `figreg.validate()` mechanically rejects any figure tagged
  with a protected-year source. This book ships with **zero archival images** — every
  figure is original.

## 10. Time-sensitive register (canon §7.14)

Each value is pinned in the canon with its verification date (**all verified
2026-07-23**) and must be **re-verified at the stated trigger before any reprint or new
edition**:

| Item | Pinned value | Re-verify trigger |
|---|---|---|
| FCC application fee | $35 (new license, renewal, rule waiver, vanity), effective 2022-04-19 | Before each reprint (fees change by FCC fiscal-year order) |
| ARRL VEC exam fee | $15.00 per session; $5.00 under 18 (calendar-2026 figure) | Each January |
| NCVEC Form 605 | 2022 edition | Before publication and each reprint |
| Laurel VEC web address | https://larc-vec.org/ (laurelvec.com redirects) | Before each reprint |
| Part 97 rule text | eCFR issue date 2026-07-21 (subpart D amended Jan 2026 — not Technician-tested material) | Re-pull every cited section before any 2027+ reprint |
| ISS frequencies/modes | voice 145.800 MHz; packet 145.825 MHz; SSTV 437.550 MHz Robot36 | Close to print, against ariss.org / AMSAT news |
| Pool currency | 2026–2030 pool valid 2026-07-01 → 2030-06-30; 2026-02-19 errata incorporated | Each reprint; next Technician pool due for the 2030-07-01 cycle |

Deliberately careful wordings the canon resolved (do not "improve" them): CORES/FRN
registration is never called "free of charge" (canon §7.2); post-exam grant timing is
"typically the next business day after payment," never a promised day count (§7.11);
remote exams are never promised as such — availability is the VE team's call (§7.13);
band plans, calling frequencies, and repeater offsets are taught as **voluntary
community practice**, never FCC mandates, and offsets are "**a common**" offset, never
"the" offset (§7.5).

## 11. How to extend

**Books 3 (General) and 4 (Extra)** inherit this template end to end:

1. Copy the repo scaffold: `tools/`, `tests/`, Docker/CI, `series/` machinery,
   `docker/audiobook-index.html` — retarget constants (titles, `SERIES_CURRENT`, image
   names, chapter count in the CI audio-fetch loop).
2. Ingest the current General/Extra pool into `canon/pool-*.txt/json` (same
   double-parse discipline; record sha256s and provenance in the new canon).
3. Rebuild `accuracy-canon.md` for that pool (pinned facts, notation, glossary,
   chapter map); write chapters against the same format laws; the same 8-check audit
   gates everything, including check #8 against the new pool.
4. Flip that book's flag in `SERIES_BOOKS`, uncomment its block in `series/nginx.conf`,
   and drop its `future` profile in `series-docker-compose.yml` when it ships.

**A pool swap within this book** (NCVEC errata, or the 2030–2034 pool):

1. Replace `canon/pool-technician.txt` and `canon/pool-technician.json` with the newly
   ingested pool (keep the byte-exact + structured pair discipline; update the sha256
   table and revision record in `accuracy-canon.md` §1).
2. Run `python3 tools/audit_book.py` — check #8 mechanically flags every chapter and
   appendix quote whose text or answer letter drifted, and any coverage gap.
3. Patch the affected quotes (quote, don't retype), update any FACT lines the canon
   change invalidates, and rebuild.

## 12. Production history

Built 2026-07-22 → 2026-07-23 by a **multi-agent workflow** (~47 subagent launches
across the tooling, canon, figures, chapters, appendix, and audit phases, plus retries
after transient engine errors), reusing Book 1's production machinery: the same
"bible-as-law" canon discipline, the same `chapters/*.md` → single-file HTML/PDF/TXT
build shape, the same 8-voice audiobook pipeline, retargeted from a history book to a
pool-anchored exam course. New in this book: the verbatim-pool ingestion and
cross-check (docx + pdf double parse), audit check #8 (mechanical pool fidelity), the
practice-exam generator, the series-site machinery, and the player's auto-play-next
toggle. The gate the content was written into: **50 pytest tests, 8 audit checks**
(including mechanical verification of all 409/409 pool quotes and answer keys), full
HTML/PDF/TXT build. This runtime does not meter subagent tokens, so no measured token
total exists; the README's stats block carries the estimate instead: ~3.6M subagent
tokens, modeled from agent reads of the canonical files plus written output volume at
~4 chars/token (Book 1's metered ~4.7M corroborates the scale).

## 13. Commands

**Regenerate the book:**
```
python3 tools/build_book.py --html --txt --pdf --out build/
```

**Verify (the accuracy/format/pool gate):**
```
python3 tools/audit_book.py
```

**Run the tooling test suite:**
```
python3 -m pytest -q
```

**Draw a practice exam:**
```
python3 tools/make_exam.py --seed 7 --out build/
```

## 14. Guidance for AI models extending this book

- **Obey `accuracy-canon.md` exactly.** It is the single source of truth for pool
  wording, dates, values, notation, glossary wording, the chapter map, and copyright
  status. Never re-date an event, restate a rule, or reword a question from memory —
  trace every fact back to the canon, and quote the pool only from
  `canon/pool-technician.*`. If the canon needs a new entry, add it there first,
  sourced, before touching chapter prose.
- **Never paraphrase a pool question or repair a published quirk.** Byte-exact quotes,
  revised questions in revised form, T1D09's typo and T1D12's bracket preserved.
- **Keep the notation law.** Prose uses V and ×; pool quotes keep E and x; unit case
  (kHz, MHz, mA, µV, pF) is load-bearing and tested.
- **Keep the careful wordings.** Fees, timing promises, band plans, offsets, and remote
  exams use exactly the hedged forms the canon resolved (§10) — do not strengthen them.
- **Never reproduce a protected Handbook image.** The 1968–1983 editions are under
  copyright — no scans, no traced reproductions, no quoted running text. This book
  needs none.
- **Run `python3 tools/audit_book.py` before considering any change done.** It is the
  mechanical enforcement of everything above (facts, format laws, figure tags, math,
  TOC, and 409/409 pool fidelity) — a change that doesn't pass it is not finished,
  regardless of how it reads.

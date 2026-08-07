# Your First Ham License

*The Technician Course (2026–2030) · from zero to licensed · 85,427 words*

> Anyone can pass the Technician exam. The whole question pool is public, the exam is
> 35 questions drawn from it one per group, and 26 correct answers earns a license.
> This book teaches the radio behind the questions — then hands you the questions.

A complete from-zero course for the US Technician class amateur radio license (Element
2, 2026–2030 NCVEC question pool), written for the absolute beginner: no electronics
background assumed, no radio experience required, math optional and gentle. Eleven
chapters walk from "what ham radio is" through electricity, signals, propagation,
antennas, your station, operating, digital and satellites, the rules in plain English,
safety, and exam day — and every teaching chapter ends with an **Exam Focus** section
quoting the exact pool questions that chapter unlocks, verbatim, with the keyed answer
and a one-line plain-language why. It is **Book 1 of a three-book program**; the
General and Extra courses follow the same template.

## What's inside

- **11 chapters** (~49,000 words) — a real course, not a cram sheet: each concept is
  taught plainly first, then tied to the pool questions it answers.
- **The exam-focus method** — every one of the **409 pool questions** is answerable
  after its mapped chapter; the chapter map (canon §5) is the contract, and a
  mechanical audit verifies every quoted question and answer letter against the
  official pool.
- **Appendix A: the complete 2026–2030 pool** — all 409 questions verbatim, choices
  A–D, correct answer marked, one-line why naming the chapter that teaches it.
- **Appendix B: glossary & formulas** — 235 terms in plain language plus the book's
  complete formula set (7 formulas, each with a worked example from the pool's own
  numbers).
- **40 original figures**, including the 3 official pool diagrams redrawn as clean,
  themeable SVGs.
- **A practice-exam generator** and an **8-voice audiobook** — see below.

## Formats

| File | What it is |
|---|---|
| [`build/index.html`](build/index.html) | The book, typeset as a single self-contained page — linked table of contents, light/dark themes, 40 figures and all math embedded inline. Open it in any browser; it works fully offline. The nicest way to read it. |
| [`build/your-first-ham-license.pdf`](build/your-first-ham-license.pdf) | PDF edition — open in any PDF reader. |
| [`build/your-first-ham-license.txt`](build/your-first-ham-license.txt) | Plain-text edition — open in any editor; math spoken as words, figures as placeholders. |
| [`chapters/`](chapters/) | The 11 source chapters as Markdown (`ch00.md` … `ch10.md`). |
| [`appendices/`](appendices/) | Appendix A ([the complete annotated pool](appendices/pool.md)) and Appendix B ([glossary & formulas](appendices/glossary-and-formulas.md)). |
| Audiobook (release v1.0) | Eight voices × 12 tracks (preface + 11 chapters) — see below. |
| [`Dockerfile`](Dockerfile) / [`docker-compose.yml`](docker-compose.yml) | Serve the book yourself — see below. |

## Read online via Docker

The image packages the book and the audiobook behind nginx, built and pushed to
`ghcr.io/atvriders/your-first-ham-license` by CI on every push to `master`. On any
Docker host:

```sh
docker compose pull && docker compose up -d
```

Serves the book at [http://localhost:8080](http://localhost:8080) and the audiobook
player at `/audiobook/`.

To build locally instead: regenerate the typeset editions, fetch the audiobook from the
release (it is not stored in git), then build the image:

```sh
python3 tools/build_book.py --html --txt --pdf --out build/
# fetch audiobook/ from release v1.0 (see .github/workflows/build.yml for the exact loop), then:
docker build -t ghcr.io/atvriders/your-first-ham-license:latest .
```

## The series site

This book is the first of three (Technician, General, Extra). The repo carries the
machinery for the whole series behind one nginx proxy, runnable today with just this
book:

```sh
docker compose -f series-docker-compose.yml up -d
```

Serves everything at [http://localhost:8080](http://localhost:8080): a landing page at
`/` with a card per book, this book (text + audiobook) at `/tech/`, and `/general/`
plus `/extra/` for the other two books — all three live since the series completed.
The book-switcher bar at the top of every page links all three. The stack runs with
zero host files — the compose file alone is enough (the proxy is a prebuilt image,
`ghcr.io/atvriders/series-proxy`, with the nginx config and landing page baked in),
so it can be pasted straight into the Portainer web editor or run from any checkout.
Config lives in [`series/`](series/) (proxy + landing page — the source of truth for
the proxy image, republished by this repo's CI) and
[`series-docker-compose.yml`](series-docker-compose.yml).

## Audiobook

The audiobook comes in **eight voices** — men and women in **American, British,
Australian, and Irish** accents — each reading the preface and all eleven chapters
(8 voices × 12 tracks), synthesized with
[edge-tts](https://pypi.org/project/edge-tts/) via
[`tools/make_audiobook.py`](tools/make_audiobook.py) (`--voice <key>` for one voice,
`--all` for every voice). Formulas and figures are narrated in
words, not read as raw markup. The verbatim pool appendix is print-only and is not
narrated.

All audio is hosted on **release v1.0** rather than committed to git. The player lives
at **`/audiobook/`** in the container: a themed page with continuous
chapter-to-chapter playback, a **voice switcher** grouped by accent, a live
visualizer,
**resume** (it remembers your voice, chapter, and position between visits), and an
**Auto-play next chapter toggle** — on by default; switch it off and playback stops at
the end of each chapter.

## Practice-exam generator

Draw a valid practice exam from the pool — exactly one question per NCVEC group, 35
questions, just like the real thing:

```sh
python3 tools/make_exam.py            # random draw
python3 tools/make_exam.py --seed 7   # reproducible draw
```

Writes `build/practice-exam.md` (questions and choices A–D, never the answers — print
it and circle) and `build/practice-exam-key.md` (the answer key with a subelement
tally). Pass `--out` to write elsewhere.

## Practice tests & flashcards

Two interactive study pages, generated from the same canonical pool data and served in
the container at **`/practice.html`** and **`/flashcards.html`** (themed like the
audiobook player, light/dark, fully self-contained — they work offline):

- **`/practice.html`** draws a valid exam — one question per group, 35 questions, 26
  to pass — reseeding with every **New exam** click. Answer by clicking; grading shows
  your score, pass/fail, and a full review list (your answer, the correct answer, and
  the one-line why). A per-subelement **drill mode** gives immediate feedback with the
  why after each question.
- **`/flashcards.html`** flips through all **409 questions**: front is the question and
  choices, back is the correct answer, the why, and a hint naming the published pool
  group and the chapter that teaches it. Filter by subelement, shuffle, and mark cards
  **review later** (persisted in `localStorage`). Keyboard-friendly: space/enter flips,
  arrows move, M marks.

The three pool figures appear inline on the twelve cards and exam questions that
reference them. Regenerate after any pool update:

```sh
python3 tools/make_study.py --out build/
```

## Pool currency

This book tracks the **NCVEC 2026–2030 Technician question pool**, valid for exams
**2026-07-01 through 2030-06-30**, incorporating the 2026-02-19 errata (four revised
questions). The pool is public domain and is carried verbatim in
[`canon/pool-technician.txt`](canon/pool-technician.txt) (byte-exact) and
[`canon/pool-technician.json`](canon/pool-technician.json) (structured), with sha256
hashes and full provenance in [`accuracy-canon.md`](accuracy-canon.md) §1.

If NCVEC issues an errata — or when the 2030–2034 pool arrives — a pool swap is:
replace the two `canon/pool-technician.*` files with the newly ingested pool, update
the canon's revision record, re-run `python3 tools/audit_book.py` (check #8
mechanically flags every chapter/appendix quote and answer letter that drifted), patch
the affected quotes, rebuild. The next Technician pool is due for the 2030-07-01 cycle;
fees and other time-sensitive values carry verification dates and re-verify triggers in
the canon (§7.14).

## Development

```sh
python3 -m pytest -q                              # 50 tooling tests
python3 tools/audit_book.py                       # the 8-check accuracy/format/pool gate (exit 0 = green)
python3 tools/build_book.py --html --txt --pdf --out build/   # rebuild the editions
```

The audit is the gate: figure integrity, copyright tags, TOC/anchors, math rendering,
canon cross-check of every `**FACT:**` line, no unresolved uncertainty markers, format
laws, and pool fidelity (every quoted question byte-exact, every answer letter matching
the key, all 409 questions in Appendix A exactly once).

## For AI models

[`AI-CONTEXT.md`](AI-CONTEXT.md) is a complete machine-oriented context dump — the
accuracy-canon discipline, pool record, chapter/subelement map, format laws,
pool-fidelity rules, figure pipeline, tooling, series machinery, copyright ledger,
time-sensitive register, and production history — sufficient to understand, extend, or
adapt the book without contradicting it.

## How it was made

Built by a **multi-agent workflow** over `accuracy-canon.md` — a bible-as-law accuracy
canon carrying the entire 409-question pool verbatim (double-parsed from the official
.docx and .pdf and cross-checked to zero disagreement), pinned Part 97 facts, notation,
glossary, the chapter map, and the copyright ledger — reusing the production machinery
of an earlier book's toolchain.

| | |
|---|---|
| **Sections** | 13 (11 chapters + 2 appendices) |
| **Words** | 85,427 (49,393 chapters · 30,969 annotated pool · 5,065 glossary & formulas) |
| **Figures** | 40 (all original — hand-authored themeable SVG + matplotlib-plotted curves; 3 NCVEC pool figures redrawn, never copied) |
| **Pool questions annotated** | 409/409 — every question verbatim, answer keyed, one-line why |
| **Agents** | ~47 subagent launches across tooling, canon, figures, chapters, appendix, and audit phases, plus retries after transient engine errors |
| **Tooling tests** | 50 pytest tests |
| **Audit checks** | 8, including mechanical verbatim-pool verification: 409/409 questions in Appendix A, every quote byte-exact, every answer key matching the pool |
| **Calendar build span** | 2026-07-22 → 2026-07-23, with parallel agents throughout |
| **Subagent tokens** | ~3.6M subagent tokens (estimate — modeled from agent reads + written volume at ~4 chars/token; this runtime does not meter subagent tokens) |

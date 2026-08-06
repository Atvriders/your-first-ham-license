# Your First Ham License — Design Spec

**Full title:** *Your First Ham License: The Technician Course (2026–2030)*
**Repo:** `Atvriders/your-first-ham-license` (public), local dir `~/your-first-ham-license/`
**Type:** Educational nonfiction — beginner course + exam prep for the US Technician class license
**Date:** 2026-07-22
**Status:** Draft — awaiting human sign-off before implementation planning.

This is **Book 1 of a three-book program**. It reuses an earlier book's production machinery and method per `/home/kasm-user/ham-book-program-plan.md`. Book 2 (General) and Book 3 (Extra) follow the same template afterward.

> **Spelling note:** US spelling "License" throughout (FCC usage), including the title — the brainstorm option's British "Licence" was normalized for the US audience.

---

## 1. Purpose & audience

A single-volume **from-zero course** that takes an absolute beginner to a passed **Technician class exam (Element 2, 2026–2030 pool)**. The reader is assumed to have **no electronics background, no radio experience, and possibly exam anxiety**. Every concept is taught plainly first, then tied to the exact pool questions it answers.

The book does two jobs at once:
- **Teaches** amateur radio as a beginner actually encounters it (what it is, how licensing works, how radios and antennas behave, how to operate, the rules, safety).
- **Prepares for the exam**: after reading the relevant chapter, the reader can answer every question in the mapped pool subelement(s).

**Spine (organizing idea):** *your first contact* — the book walks a new ham from "curious" to "licensed and on the air," in the order a beginner needs it: fascination → how it works → how to operate → the rules → safety → exam day → what's next.

**Non-goals:** Not a history book. Not a reference encyclopedia (Books 2/3 carry the deeper theory). Not a bare question-and-answer cram sheet — teaching comes first, exam mapping second.

**Tone:** friendly, plain, reassuring; short sentences; analogies over jargon; jargon defined on first use and in the glossary; math optional and gentle (Ohm's law and f·λ=c are the only required formulas).

## 2. Relationship to the earlier toolchain (what we reuse)

| Reused from the earlier book | Retargeted to this book |
|---|---|
| `accuracy-canon.md` "bible as law" | Canon = pinned facts + **the full 2026–2030 pool ingested verbatim** + Part 97 facts (§6) |
| `tools/` (build, audit, figreg, mathsvg, narration, audiobook, intro) | Copied; constants retargeted; **audit gains an 8th check: verbatim pool quotes + answer keys** (§9) |
| Multi-agent workflow: canon → figures → chapters+audit | Same shape; chapter writers also write Exam Focus sections & per-question "why" lines (§8) |
| Hybrid figure pipeline (SVG schematics + matplotlib) | Original beginner-oriented figures + **the 3 official pool diagrams redrawn as SVG** (§4, §7) |
| Self-contained HTML/PDF/TXT build | Same; colophon/title retargeted |
| 8-voice edge-tts audiobook + player | **Chapters only** — the verbatim pool appendix is print-only (decision locked) |
| Docker/nginx + GitHub→GHCR CI | Same, image `ghcr.io/atvriders/your-first-ham-license` |
| `AI-CONTEXT.md`, README with token/time stats | Same convention |

**New tooling for this book:** `tools/make_exam.py` — practice-exam generator that draws a valid 35-question exam from the pool per NCVEC group distribution (one question per group), with a separate answer key. TDD'd like the other tools.

## 3. Source materials

**The exam pool (load-bearing, public domain):**
- **NCVEC Element 2, 2026–2030 Technician pool** — 409 questions, 10 subelements **T1–T0**, groups A–F (35 groups; a real exam draws one question per group — *verify exact group structure at ingestion*).
- Released 2025-12-18; **revised 2026-02-19** (wording clarifications to T1C01, T5A05, T7A09, T0A10); effective for exams **2026-07-01 through 2030-06-30**. We ingest the **current revised** version.
- Primary source: <https://ncvec.org/index.php/2026-2030-technician-question-pool> (Word/PDF); mirror: <https://www.arrl.org/question-pools>. The pool ships with **3 schematic diagrams** used by specific questions.
- Ingestion (Phase C1): download, convert to a canonical `canon/pool-technician.txt` (byte-exact question text) + structured `canon/pool-technician.json` (id → question, choices A–D, correct letter, group, figure ref if any). Verify: question count = 409, the 4 revised questions present in revised form, zero parse drops. Conversion tooling: check for `pandoc`/`python-docx`/pdftotext at that phase.

**Regulations:** FCC **Part 97** (public domain; quote freely) — especially §97.1 (basis and purpose), §97.101–113 (operating), §97.301–307 (frequencies/emissions), §97.501–523 (exams).

**Owned materials for depth/color (never copied verbatim):** ARRL Handbooks at `~/leehite-callbooks/handbooks-arrl/` (1927–1983); the two licensing-history PDFs at `~/leehite-callbooks/callbooks/`; ARRL operating-event explainers at `~/arrl-calendar/src/data/rules.ts`; the 31-question curated sample at `~/ham-radio-clicker/src/data/questions.ts` (cross-check only — the NCVEC pool is authoritative).

**External cross-reference:** ARRL licensing pages (how to find an exam session, FRN/ULS), FCC ULS. Every load-bearing fact traces to the canon; the canon traces to a source.

## 4. Chapter outline (11 chapters + 2 appendices, ~55–70k words, ~30–40 figures)

Teaching chapters run ~4,500–6,000 words; ch00 and ch10 shorter. Pool subelement coverage is explicit — every one of the 409 questions is answerable after its mapped chapter.

| # | Chapter | Pool subelement(s) | Teaches |
|---|---|---|---|
| 00 | **Welcome: what ham radio is & how licensing works** | — | What hams do; the three US license classes; the exam (35 Q, 26 to pass, one per group); finding a session; FRN/FCC ULS; your call sign. ~2.5–3k |
| 01 | **Electricity & radio from zero** | T5 (electrical principles), T6 (components) | Voltage/current/resistance; Ohm's law; power; AC/DC; frequency & wavelength (f·λ=c); R/L/C, diodes, transistors, ICs; reading simple schematics. |
| 02 | **How signals travel: modes & modulation** | T8 (first half) | AM/FM/SSB/CW; bandwidth; digital modes intro; the RF spectrum. |
| 03 | **Propagation: where your signal goes** | T3 | Line-of-sight vs HF skip; VHF/UHF behavior; fading; polarization; the ionosphere in plain terms. |
| 04 | **Antennas & feedlines** | T9 | Dipoles, verticals, gain/directivity (dB gently); SWR; coax & connectors; the pool's antenna questions demystified. |
| 05 | **Your station & equipment** | T4 (station setup), T7 (station equipment) | Transceivers HT/mobile/base; power supplies; SWR meters; microphones; connecting it all; RFI basics. |
| 06 | **Operating: repeaters & VHF/UHF life** | T2 | Simplex vs duplex; offsets & CTCSS; calling/answering; nets; phonetics & Q-signals; good-practice etiquette. |
| 07 | **Digital, satellites & data** | T8 (second half) | FT8/packet/APRS basics; working satellites; internet-linked radio (EchoLink/IRLP/DMR over networks). |
| 08 | **The rules (Part 97, in plain English)** | T1 | Purpose of the service; privileges by band; identification; control operator; prohibited practices; where band plans come from. |
| 09 | **Safety** | T0 | Electrical safety; grounding; batteries; towers & antennas; RF exposure basics. |
| 10 | **Exam day & your first radio** | — | Test-taking strategy; what to expect at the session; what to buy first; where to go next (General — the next book). ~3k |
| A | **Appendix A: the complete 2026–2030 pool** | all 409 | Every question verbatim, choices A–D, correct answer marked, one-line "why" pointing back to the chapter that teaches it. Print-only (not narrated). |
| B | **Appendix B: glossary & formulas** | — | Every term defined plainly; the handful of formulas with worked micro-examples. |

**Exam-prep integration (the defining feature):** each teaching chapter (01–09) ends with an **Exam Focus** section: the pool group IDs it covers + 5–10 representative questions quoted **verbatim** with the correct answer and a one-line plain-language "why." Appendix A carries the full pool the same way. Correctness rule: question text and answer keys match the NCVEC pool **verbatim** — never paraphrased; the audit enforces this mechanically (§9).

## 5. Per-chapter anatomy (the "format laws" — audit-enforced)

Every teaching chapter (01–09) follows one skeleton so parallel writers produce a coherent book:

1. **Heading:** `## <N>. <Title>` (e.g. `## 4. Antennas & Feedlines`).
2. **Opener:** one short plain-language paragraph — a concrete new-ham scenario and "in this chapter you'll learn …". No epigraph device.
3. **Teaching sections** (`### …`): plain language, analogies, figures via `{{fig:id}}`, inline math `$…$` only where the pool needs it; optional `> **The math, if you want it:**` sidebars for anything beyond arithmetic.
4. **≥1 `> **Worked example:**`** blockquote per teaching chapter — a real, simple calculation (e.g. "What is the wavelength of 146 MHz?") worked end to end.
5. **`### Exam Focus`** — pool IDs covered; 5–10 verbatim questions, each with correct answer + one-line why.
6. **`### Key Takeaways`** — 4–8 bullets, retention recap.
7. **3–5 `**FACT:** <sentence>` lines** copied verbatim from `accuracy-canon.md` (audit greps exact matches).

Chapters 00 and 10 follow the same skeleton minus Exam Focus (ch00 gets "Your first checklist" instead; ch10 gets "Your 30-day plan"). Banned phrases (carried over from the earlier book): "little did they know", "in that moment", "a testament to". Nonfiction integrity: no fabricated quotations anywhere; anecdotes are plainly framed as illustrative scenarios, never attributed to real people.

## 6. The accuracy canon (`accuracy-canon.md` + `canon/pool-technician.*`) — law for all agents

- **The pool, verbatim** — `canon/pool-technician.txt` (human-readable, byte-exact) + `canon/pool-technician.json` (structured). Question text, choices, and answer letters are quoted from here only.
- **Pinned facts with sources** — exam structure (35 Q / 26 to pass / one per group), license classes & privileges, Tech band privileges and frequency limits (exactly as Part 97 / the pool state them — this is what the exam tests; zero tolerance for drift), FRN/ULS process, pool validity window 2026-07-01 → 2030-06-30, the 2026-02-19 revision record.
- **Notation & units standard** — one symbol set (V, I, R, P, f, λ …), metric with US-conventional units where hams use them; f·λ=c with c = 300,000 km/s ≈ 300 Mm/s for mental math (300/ f(MHz) = λ(m) — the pool's own shortcut, stated as such).
- **Glossary** — canonical plain-language definition per term (feeds Appendix B).
- **Copyright ledger** — carried over from the earlier book's canon (PD editions 1927–1951; protected 1968–1983; Part 97 and pools free).
- **Resolved uncertainties** — anything flagged during research, with resolution + source.

## 7. Copyright discipline

- **Prose is always original.** Pool questions/choices/answers, Part 97, and bare facts are reproduced verbatim (public domain); nothing else is copied.
- **The 3 official pool diagrams:** redrawn as **original SVGs** conveying exactly the official content (same components, same labels), registered in `figures.json` as `kind:"original"` with a note "redrawn from NCVEC pool figure T-x" — the pool is public domain, so this is both safe and faithful.
- **Archival Handbook figures:** optional seasoning only, from PD editions 1927–1951 per the ledger; tagged `archival-PD`. The book works fine with zero of them.
- Every figure tagged in `figures.json`; `figreg.validate()` enforces the protected-years rule (1968–1983).

## 8. Production architecture (multi-agent workflow)

1. **Orchestration** (this phase): spec → human sign-off → task-by-task implementation plan.
2. **Tooling scaffold (TDD):** copy the earlier book's `tools/`, `tests/`, CI, Docker; retarget constants; add `make_exam.py`; extend `audit_book.py` (§9). `pytest` green; fixture build; audit exits 0 on the empty scaffold.
3. **Canon workflow:** parallel researchers (pool ingestion+verification; Part 97 facts; licensing-process facts; per-subelement teaching notes) → 1 assembler writes `accuracy-canon.md` + `canon/pool-technician.*`. **Gate:** 0 `UNVERIFIED`; count = 409; revised questions verified; audit canon checks pass.
4. **Figures workflow:** one agent per chapter authors that chapter's figures (themeable SVG, `currentColor`; matplotlib→SVG plots post-processed) → assembler writes `figures/figures.json`. **Gate:** `figreg.validate()` empty; all SVGs parse; several rendered to PNG and eyeballed.
5. **Chapters workflow:** parallel chapter writers (canon + real figure IDs + format laws + Exam Focus with verbatim quotes) → span auditors verifying every fact/value/question-quote against canon & pool, fixing in place. One agent batch also writes Appendix A's 409 one-line "why" annotations (fanned out per subelement). **Gate:** audit all-green incl. verbatim-pool check; full build; spot-read.
6. **Front matter, verify & ship** (§9, §10).

Fan-out follows the standing preference: parallel agents while building; **one commit at the very end** after full verification.

## 9. Deliverables & build

- **The book:** `chapters/ch00.md … ch10.md` + `appendices/` (pool, glossary) → single self-contained **HTML** (inline SVG figures + inline math, linked TOC, light/dark) → **PDF** (headless google-chrome) → **TXT**.
- **`tools/make_exam.py`** — practice-exam generator: draws 35 questions (one per NCVEC group), formats a printable exam + separate answer key; `--seed` for reproducibility. Shipped in-repo and surfaced in the README.
- **Audiobook:** 8-voice edge-tts, **chapters 00–10 only** (pool appendix excluded from narration); retargeted `spoken_heading()`, ID3, intro; audio attached to release v1.0, not committed. The player includes a persisted **"Auto-play next chapter" toggle** (default ON; when OFF, playback stops at each chapter end) — user-requested 2026-07-22.
- **Repo & hosting:** `Atvriders/your-first-ham-license` (public), `master`, GitHub-primary; Docker/nginx image `ghcr.io/atvriders/your-first-ham-license:latest` built by GitHub Actions; audiobook player at `/audiobook/`. No Gitea CI (dead path).
- **Series site (user-requested 2026-07-22):** every book in the series (Technician, General, Extra) carries a **book-switcher bar** in its generated book HTML and audiobook player linking all three books (current book highlighted; not-yet-shipped books marked "coming soon", links inert). Books are mounted at stable paths `/tech/`, `/general/`, `/extra/` behind a **series nginx proxy**; a `series/` dir in each repo holds the proxy config, a landing page, and `series-docker-compose.yml` wiring the three book images into one site. The full three-book site completes as each book ships; each book's standalone image also runs fine alone. Book HTML must keep asset links relative so sub-path proxying works.
- **`AI-CONTEXT.md`** — full machine-oriented dump (canon summary, outline, pool facts & revision record, format laws, production history). Credentials omitted.
- **`README.md`** — overview, formats table, Docker/audiobook instructions, exam-generator usage, pool currency notice (valid 2026-07-01 → 2030-06-30), and the "How it was made" token + wall-time stats block (finalized at push).
- **`audit_book.py` checks (7 adapted + 1 new):** figure integrity; copyright tags; TOC/anchors; math renders; `**FACT:**` lines match canon verbatim; no `UNVERIFIED`; format laws (§5 skeleton, banned phrases); **NEW #8 — pool fidelity:** every question quoted in chapters/appendix exists verbatim in `canon/pool-technician.txt`, and every stated correct-answer letter matches the pool key; Appendix A contains all 409 IDs exactly once.

## 10. Verification (what "done" means)

1. `python3 -m pytest` — all tooling tests green.
2. `python3 tools/audit_book.py` — exit 0, all 8 checks.
3. **Real build** — HTML/PDF/TXT produced; spot-check the HTML in a browser-render (figures inline, TOC resolves).
4. **Pool fidelity spot-read** — a human-style read of one chapter + a random sample of Appendix A entries against the official NCVEC document.
5. **Figure eyeball** — several rendered PNGs inspected visually.
6. Only then: one commit, GitHub repo via REST API, push, audiobook, release v1.0 + assets, CI dispatch, GHCR public-pullable confirmed.

## 11. Open items / risks

- **Pool file conversion** — NCVEC ships Word/PDF; extraction must be lossless (subscripts, symbols, the 3 figure references). Mitigation: verify count=409 + diff the 4 known revised questions + manual spot-diff of a random sample; the audit's verbatim check backstops quotes.
- **Pool errata mid-build** — NCVEC occasionally issues revisions (one already, 2026-02-19). Mitigation: canon carries the pool as a single replaceable file + revision record; a swap = replace file, re-run audit, patch affected quotes.
- **Word-target tension** — Appendix A's verbatim pool is long; it is excluded from the 55–70k prose target and from narration.
- **Depth discipline** — beginner tone vs. covering T5/T6 circuit questions honestly. Mitigation: "The math, if you want it" sidebars; auditors flag any paragraph that outruns a first-time reader.
- **US-centric scope** — the exam is US-only; the book says so up front and teaches operating practice generally where the pool allows.

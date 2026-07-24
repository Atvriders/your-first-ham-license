# Your First Ham License — Implementation Plan

> **For agentic workers:** implement this plan task-by-task (subagent-driven development recommended). Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Produce *Your First Ham License: The Technician Course (2026–2030)* — an ~55–70k-word, ~30–40-figure beginner course + exam-prep book aligned to the 2026–2030 NCVEC Technician pool (409 questions) — as a self-contained HTML/PDF/TXT edition plus Docker site, practice-exam generator, and 8-voice audiobook, built by a multi-agent workflow against a verified accuracy canon that carries the pool verbatim.

**Architecture:** Two tracks. **(A) Tooling** — Book 1's Python build/verify/audiobook tools copied and retargeted, plus a new pool-fidelity audit check and a new `make_exam.py`, all test-first against small fixtures. **(B) Content** — canon (incl. verbatim pool) → figures → 11 chapters + 2 appendices, produced by parallel writer/figure/auditor agents and gated by the Track-A harness. Track A first so Track B writes into a green gate.

**Tech Stack:** Python 3 (stdlib + `edge-tts`, `matplotlib`), headless `google-chrome` for PDF, `ffmpeg` for audio, nginx/Docker, GitHub Actions → GHCR. Base for all copying: `/home/kasm-user/200-meters-and-down/` ("Book 1"). Design spec: `docs/superpowers/specs/2026-07-22-your-first-ham-license-design.md` (approved).

## Global Constraints

- **ONE commit at the very end**, after full verification (pytest green + `audit_book.py` exit 0 + real build + spot-reads). No per-task/phase commits.
- **Parallel fan-out when building**: figures, chapters, appendix annotations, audits run as parallel agents.
- **All repos/packages public.** Repo `Atvriders/your-first-ham-license`, branch `master`, GitHub-primary (no Gitea CI — dead path; do not copy `.gitea/`). Push only after the ship gate.
- **Never the `gh` CLI** — GitHub REST API via curl with the token from `~/.config/gh/hosts.yml`.
- **Pool fidelity is law:** question text, choices, and answer letters are quoted only from `canon/pool-technician.*`, byte-exact. Never paraphrase a question.
- **Prose original; facts/Part 97/pool free.** No fabricated quotations; anecdotes framed as illustrative scenarios, never attributed to real people.
- **Self-contained output:** inline SVG figures, math pre-rendered to inline SVG, inline CSS; no external refs (`src="http"`, `<link rel="stylesheet">`, `@import` are failures; SVG `xmlns` URIs are fine — Book 1 gotcha #3).
- **Environment:** `python3` (not `python`); `matplotlib`, `edge-tts`, `ffmpeg`, `google-chrome` present; no local Docker (CI builds the image).
- **Naming:** title *Your First Ham License: The Technician Course (2026–2030)* (US spelling); audio ID3 `artist=Claude Opus 4.8`, `album=Your First Ham License`; GHCR image `ghcr.io/atvriders/your-first-ham-license`.
- **sys.path gotcha:** every runnable script keeps `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))` (Book 1 gotcha #2).
- **CI gotcha:** copy Book 1's *fixed* workflow (`seq -f "%02g"`, not `seq -w` — gotcha #1), then adjust chapter count/audio URLs.

## File Structure

```
your-first-ham-license/
├── accuracy-canon.md                 # THE BIBLE: pinned facts, notation, glossary, copyright ledger
├── canon/
│   ├── pool-technician.txt           # the 2026–2030 pool, byte-exact (human-readable)
│   └── pool-technician.json          # structured: id → {group, question, choices{A-D}, answer, figure?}
├── AI-CONTEXT.md                     # full machine context dump (Phase 5)
├── README.md                         # overview + formats + stats block (Phase 5/6)
├── requirements.txt  .gitignore  docker-compose.yml  Dockerfile
├── chapters/
│   ├── ch00.md … ch10.md             # 11 chapters
│   └── specs/ch00.spec.md … ch10.spec.md
├── figures/
│   ├── <id>.svg  +  _gen_*.py        # original SVGs + matplotlib generators
│   └── figures.json                  # id, chapter, caption, kind(original|archival-PD), source, spoken
├── appendices/
│   ├── pool.md                       # Appendix A: all 409 questions verbatim + one-line why
│   └── glossary-and-formulas.md      # Appendix B
├── tools/                            # copied from Book 1, retargeted
│   ├── narration.py  mathsvg.py      # as-is
│   ├── figreg.py                     # protected-years set unchanged (1968–1983)
│   ├── build_book.py                 # retargeted titles/colophon; appendices in build
│   ├── audit_book.py                 # format laws for this skeleton + NEW check #8 (pool fidelity)
│   ├── make_audiobook.py             # chapters 00–10 only; retargeted headings/ID3
│   ├── make_intro.py                 # new INTRO text
│   └── make_exam.py                  # NEW: practice-exam generator
├── docker/audiobook-index.html       # retargeted player (11 tracks)
├── .github/workflows/build.yml       # copied fixed version, retargeted
├── tests/                            # pytest: Book 1's 6 files adapted + test_make_exam.py
│   └── fixtures/                     # ch_sample.md, fig_sample.svg, pool_sample.txt/json
└── docs/superpowers/{specs,plans}/…  # spec + this plan
```

---

## PHASE 0 — Scaffold

### Task 0.1: Repo skeleton
- [x] Create `~/your-first-ham-license/` with dirs: `tools/ tests/ tests/fixtures/ chapters/ chapters/specs/ figures/ canon/ appendices/ docker/ .github/workflows/ build/ audiobook/ docs/superpowers/specs/ docs/superpowers/plans/` (last two already exist with spec+plan).
- [x] Copy from Book 1 (verbatim, then retarget in Phase 1): `tools/*.py`, `tests/`, `pyproject.toml`, `requirements.txt`, `.gitignore`, `docker/audiobook-index.html`, `Dockerfile`, `docker-compose.yml`, `.github/workflows/build.yml`.
- [x] **Do NOT copy:** `chapters/`, `figures/*.svg`, `figures/figures.json`, `accuracy-canon.md`, `AI-CONTEXT.md`, `README.md`, `audiobook/` (1.3 GB), `build/`, `appendices/`, `.gitea/`, `docs/canon-research/`, `.git/`.
- [x] `git init -b master` (no commits until the end).
- [x] **Verify:** tree matches File Structure; `python3 -m pytest` collects (failures expected until retarget — that's Phase 1).

---

## PHASE 1 — Tooling retarget + extensions (TDD)

### Task 1.1: Copy-through modules
- [x] `narration.py`, `mathsvg.py`, `figreg.py`: copy unchanged (Book-agnostic; protected-years set already 1968–1983). Their tests should pass as-is.
- [x] **Verify:** `pytest tests/test_narration.py tests/test_mathsvg.py tests/test_figreg.py` green.

### Task 1.2: `build_book.py` retarget
- [x] Change title/colophon/heading constants to this book; chapter glob `ch*.md`; include `appendices/pool.md` + `appendices/glossary-and-formulas.md` as final TOC sections (after ch10), without chapter numbers in headings.
- [x] Keep: repo-root sys.path bootstrap; self-contained HTML; PDF probe order `chromium/chromium-browser/google-chrome/google-chrome-stable` → weasyprint → skip (Book 1 gotcha #6).
- [x] Update `tests/test_build_book.py` + `tests/fixtures/ch_sample.md` to this book's skeleton (§5 of spec: opener, `### Exam Focus`, `### Key Takeaways`, `**FACT:**`).
- [x] **Verify:** `pytest tests/test_build_book.py` green; fixture builds HTML+TXT; PDF builds via google-chrome.

### Task 1.3: `audit_book.py` retarget + NEW check #8
- [x] Adapt format-law checks to the spec §5 skeleton: `## <N>. <Title>`; opener paragraph present; ≥1 `> **Worked example:**` in ch01–ch09; `### Exam Focus` in ch01–ch09 (absent in ch00/ch10); `### Key Takeaways`; 3–5 `**FACT:**` lines matching `accuracy-canon.md` verbatim; banned phrases list unchanged.
- [x] **Check #8 — pool fidelity:** load `canon/pool-technician.json`; (a) every `> **T#X##**`-style question quote in chapters and `appendices/pool.md` matches the pool text byte-exact (normalize whitespace only); (b) every stated answer letter matches the pool key; (c) `appendices/pool.md` contains all 409 IDs exactly once, in order. On the empty scaffold (no pool yet) check #8 must SKIP gracefully with a printed note, not fail.
- [x] **Verify:** `pytest tests/test_audit_book.py` green (incl. new fixture-based tests for #8: a correct quote passes; a one-word-off quote fails; a wrong answer letter fails; missing pool → skip).

### Task 1.4: `make_audiobook.py` + `make_intro.py` retarget
- [x] Chapter range 00–10 (11 chapters); `spoken_heading()` for `## <N>. <Title>`; ID3 `album=Your First Ham License`, `artist=Claude Opus 4.8`; exclude `appendices/` from narration; keep sys.path bootstrap, chunking/retries, ffmpeg stitch.
- [x] New INTRO text (beginner welcome, ~1 min spoken); keep `--dry`.
- [x] **Verify:** `pytest tests/test_audiobook_prepare.py` green; `python3 tools/make_intro.py --dry` prints sane text.

### Task 1.5: NEW `tools/make_exam.py` (TDD)
- [x] Interface: `load_pool(json_path) -> dict`; `draw_exam(pool, seed=None) -> list[Question]` — exactly one question per group (35 groups → 35 questions), uniform random within group, reproducible with `--seed`; `render_exam(questions)` → printable markdown (questions only, choices A–D, no answers); `render_key(questions)` → answer key with one-line why absent (letters only) + subelement tally. CLI: `python3 tools/make_exam.py [--seed N] [--out build/]`.
- [x] Tests with a small `tests/fixtures/pool_sample.json` (e.g. 4 groups × 3 questions): correct count (one per group), seed reproducibility, no answers leaked into the exam sheet, key correctness.
- [x] **Verify:** `pytest tests/test_make_exam.py` green.

### Task 1.6: Docker + CI retarget
- [x] `Dockerfile`: serve this book's build artifacts; `docker-compose.yml`: image `ghcr.io/atvriders/your-first-ham-license:latest`.
- [x] `docker/audiobook-index.html`: title + 11 track labels (ch00–ch10), same player machinery.
- [x] `.github/workflows/build.yml`: copy Book 1's fixed version; change repo/image names and the audio-fetch loop to `seq -f "%02g" 0 10` (11 chapters); release `v1.0`.
- [x] **Verify:** `python3 -m pytest` all green; `python3 tools/build_book.py --html --txt --pdf --out build/` succeeds on fixtures; `python3 tools/audit_book.py` exits 0 on the empty scaffold (check #8 skipping gracefully).

### Task 1.7: Series-site machinery + player auto-play-next (NEW SCOPE — user request 2026-07-22)
- [x] **Player toggle:** in `docker/audiobook-index.html`, add an "Auto-play next chapter" toggle button (default ON, persisted in `localStorage` alongside the existing keys); the `ended` handler auto-advances only when the toggle is ON, otherwise stops at chapter end. Keyboard shortcut optional. Must not disturb existing resume/visualizer/voice-switch behavior.
- [x] **Book-switcher bar:** add a slim series bar to (a) `build_book.py`'s generated HTML template and (b) the audiobook player page: three entries — Technician `/tech/`, General `/general/`, Extra `/extra/` — current book highlighted, unshipped books rendered as inert "coming soon" labels (a small per-book constant so General/Extra flip their links live when they ship). Bar styling must match each page's existing theme (light/dark aware).
- [x] **Relative links:** ensure generated book HTML uses only relative/anchor links (needed for sub-path proxying); add a build test asserting no absolute `href="/`-style links except the configurable series paths.
- [x] **`series/` dir** (repo root): `series/nginx.conf` — proxy: `/` → landing page, `/tech/` → tech container, `/general/` → general container, `/extra/` → extra container (docker-compose service names; only `tech` active until the others ship); `series/index.html` — landing page listing the three books with cover-style cards (unshipped ones "coming soon"); `series-docker-compose.yml` — the three book images + proxy service, documented ports.
- [x] **Verify:** `pytest` green (incl. the relative-links test); rebuilt fixture HTML shows the bar with Technician highlighted; player page shows bar + toggle (visual check via rendered screenshot if possible, else code review); `series-docker-compose.yml` parses (`docker compose config` unavailable locally — validate YAML with python).

---

## PHASE 2 — Canon workflow (content gate 1)

### Task 2.1: Obtain + ingest the pool (serial, first)
- [ ] Download the **revised** 2026–2030 Technician pool from `https://ncvec.org/index.php/2026-2030-technician-question-pool` (Word and/or PDF; cross-check with the ARRL mirror at `https://www.arrl.org/question-pools`). Save originals under `canon/source/`.
- [ ] Convert to `canon/pool-technician.txt` (byte-exact text; use `pandoc`/`python-docx`/`pdftotext` — probe what's installed) and structured `canon/pool-technician.json`: `{id, group, subelement, question, choices:{A..D}, answer, figure}`.
- [ ] **Verify:** count = **409**; subelements T1–T0 with 35 groups total (one question per group per exam — record the group list in the canon); the 4 revised questions (T1C01, T5A05, T7A09, T0A10) present in revised form; the 3 figure-referencing questions flagged with their figure id; zero parse drops (every ID T1A01…T0F## contiguous within its group).

### Task 2.2: Parallel researchers (fan-out)
- [ ] R1: Part 97 pinned facts — §97.1 purposes, ID rules, control operator, prohibited practices, band/emission privileges **as the pool tests them**.
- [ ] R2: Licensing process — exam structure (35 Q, 26 pass, one per group), finding sessions, FRN/ULS, call-sign formats, vanity basics, pool validity window + revision record.
- [ ] R3: Per-subelement teaching notes T1–T5 (what a beginner must understand to answer every question in the subelement; common confusions).
- [ ] R4: Per-subelement teaching notes T6–T0 (same).
- [ ] R5: Operating practice color — repeater etiquette, nets, phonetics, Q-signals (cross-ref `~/arrl-calendar/src/data/rules.ts`).

### Task 2.3: Assembler
- [ ] One agent writes `accuracy-canon.md`: pinned facts w/ sources, notation & units (incl. the 300/f(MHz) = λ(m) shortcut, labeled as the pool's own), glossary, copyright ledger (carried from Book 1), pool summary + revision record, resolved uncertainties.
- [ ] **Verify (gate):** 0 `UNVERIFIED` markers; `python3 tools/audit_book.py` canon checks pass (check #8 now live against the real pool); spot-read the canon.

---

## PHASE 3 — Figures workflow (content gate 2)

### Task 3.1: Figure list
- [x] Orchestrator writes `figures/figure-plan.md`: ~30–40 figures across ch01–ch10, **including the 3 official pool diagrams redrawn as original SVGs** (same components/labels as the NCVEC figures), plus band charts, dipole, SWR curve, repeater duplex, RF spectrum, simple circuits (Ohm's-law triangle, series/parallel), connector types, station block diagram, ionosphere/skip, polarization, CTCSS tones concept, satellite pass.

### Task 3.2: Parallel figure agents
- [x] One agent per chapter authors that chapter's figures: hand-authored themeable SVG with `currentColor` for schematics/diagrams; matplotlib→SVG for plots (post-process black→`currentColor`); each with caption + one-line spoken description.

### Task 3.3: Assembler + verify (gate)
- [x] Assembler writes `figures/figures.json` (id, chapter, caption, kind, source, spoken).
- [x] **Verify:** `python3 -c "from tools import figreg; …"` validate → empty; all SVGs parse (XML); render ≥6 to PNG and **look at them**; the 3 pool redraws compared side-by-side with the official figures for content equality.

---

## PHASE 4 — Chapters workflow (content gate 3)

### Task 4.1: Chapter specs
- [ ] Orchestrator writes `chapters/specs/ch00.spec.md … ch10.spec.md`: per chapter — subelement(s) covered, pool groups mapped, required figure IDs (from 3.2), teaching beats, Exam Focus question selection (5–10 per chapter), worked-example topic.

### Task 4.2: Parallel chapter writers (11 agents)
- [ ] Each agent: reads canon + pool slice + its spec + figure registry; writes `chapters/chNN.md` obeying the §5 format laws; Exam Focus quotes **verbatim** from `canon/pool-technician.txt` with correct letters + one-line whys; 3–5 `**FACT:**` lines copied verbatim from `accuracy-canon.md`.

### Task 4.3: Appendix A annotations (parallel, per subelement — 10 agents)
- [x] For each subelement T1–T0: emit that subelement's pool section for `appendices/pool.md` — every question verbatim (from the pool file only), choices A–D, correct answer marked, one-line plain "why" naming the chapter that teaches it. Assembler concatenates in ID order; Appendix B (glossary from canon + formulas with micro-examples) by one agent.

### Task 4.4: Span auditors (parallel, 3–4 agents)
- [ ] Each audits a span of chapters: every fact/value/frequency/privilege against canon; every question quote + letter against the pool (mechanically assisted by audit check #8); format laws; tone check (beginner-appropriate; flag any paragraph that outruns a first-time reader); fix surgically in place.

### Task 4.5: Verify (gate)
- [ ] `python3 tools/audit_book.py` — all 8 checks green (incl. #8: 409/409 in Appendix A, all quotes verbatim, all letters correct).
- [ ] Full build HTML/PDF/TXT; spot-read 1 full chapter + 20 random Appendix A entries against the official NCVEC document; banned-phrase grep clean.

---

## PHASE 5 — Front matter

- [ ] `AI-CONTEXT.md`: full machine dump (canon summary, outline, pool facts + revision record, format laws, production history, infra notes; no credentials).
- [ ] `README.md`: overview, formats table, Docker/audiobook instructions, `make_exam.py` usage, pool-currency notice (valid 2026-07-01 → 2030-06-30; what a pool swap entails), "How it was made" stats block (tokens + wall-time; finalized at push).

---

## PHASE 6 — Verify & ship

- [ ] Clean rebuild from scratch; `pytest` green; `audit_book.py` exit 0; human-style spot-read.
- [ ] **Ship gate (human confirms before outward actions).**
- [ ] One commit (trailer `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`).
- [ ] Create GitHub repo via REST API (`POST /user/repos`, `private:false`); push `master`.
- [ ] Generate audiobook: `make_audiobook.py --all` (8 voices × 11 chapters) + `make_intro.py`.
- [ ] Create release **v1.0**; upload audio assets.
- [ ] `workflow_dispatch` the CI; confirm image builds and `ghcr.io/atvriders/your-first-ham-license:latest` is anonymously pullable (`docker pull` unauthenticated or manifest check via curl).
- [ ] **Series site:** the `series/` machinery ships with this repo; the switcher bar's General/Extra entries stay "coming soon" until those books ship. General/Extra books inherit the bar/proxy templates with their own book highlighted (tracked in their own plans); after the third book ships, verify the full three-book site via the series compose.
- [ ] Write final token/time stats into README (amend or second tiny README-only commit if the human allows; otherwise include in the one commit by generating audio before committing).

---

## Tracking & cost notes

- Book 1 cost reference: ~42 agents, ~4.7M subagent tokens, ~90 min wall-time. This book adds pool integration (ingestion, 409 annotations, check #8) — budget ~5–6M tokens, ~2 h.
- Mark plan checkboxes as tasks complete; keep the human informed at each content gate (2.3, 3.3, 4.5) and the ship gate.

# Writer Spec — Appendix A. The Complete 2026–2030 Pool

**Output file:** `appendices/pool.md`
**Target length:** excluded from the book's 55–70k prose target (design §11) — it is the verbatim pool, ~409 question blocks.
**Pool coverage:** **all 409 questions, exactly once each, in canonical pool order** — the audit's check #8 (`check_appendix_pool_coverage`) mechanically requires: every pool id present exactly once, every id a real pool question, and the sequence in pool order.

## 1. Purpose

Appendix A carries the full 2026–2030 Technician pool the same way the chapters' Exam Focus sections carry samples: every question verbatim, choices A–D verbatim, correct answer marked, plus a **one-line plain-language "why"** that names the chapter teaching it. Print-only — this appendix is **not narrated** in the audiobook (decision locked, design §2/§4).

## 2. Structure

- First line: `## Appendix A. The Complete 2026–2030 Pool` (appendices are exempt from the chapter format laws — the audit's `check_format_laws` only applies to `chNN` stems — but keep the `## Appendix …` heading shape for the TOC).
- One short intro paragraph: what this is (the verbatim NCVEC 2026–2030 Technician pool, public domain, valid for exams 2026-07-01 → 2030-06-30, incorporating the 2026-02-19 errata), how to use it (read the mapped chapter, then drill its group here), and the key to the entry format.
- Then **one `###` section per subelement, in pool order T1 → T0**, using the published subelement titles (canon §1.3): `### T1 — Commission's Rules (68 questions, 6 on the exam)` … through `### T0 — Safety (36 questions, 3 on the exam)`. Within each subelement section, optionally one `####` line per group with the published group theme (from the group headings in `canon/pool-technician.txt`), then that group's questions in ascending number order.
- The three pool figures belong to T6: where a question references Figure T-1/T-2/T-3, embed the corresponding redrawn SVG on the line before its quote block: `{{fig:ch01-pool-fig-t1}}` (T6C02–T6C05, T6D10), `{{fig:ch01-pool-fig-t2}}` (T6A09, T6C06–T6C09), `{{fig:ch01-pool-fig-t3}}` (T6C10, T6C11). Embed each redraw once at its first referencing question and reference it by name ("Figure T-2, above") for the rest.

## 3. Entry format (audit check #8 parses this exactly)

Every one of the 409 entries is one blockquote in exactly this shape, followed by one plain line carrying the published ID line:

```
> **T1A01** <question text, verbatim from the pool>
> A. <choice text, verbatim>
> B. <choice text, verbatim>
> C. <choice text, verbatim>
> D. <choice text, verbatim>
> **Answer: C** — <one-line why, ending with the teaching chapter: "… — taught in chapter 8.">

Published ID line: `T1A01 (C) [97.1]`
```

Rules (all mechanically enforced or canon law):

- **Question and choice text byte-exact** from `canon/pool-technician.txt` (the audit compares whitespace-normalized against `canon/pool-technician.json`). Published Unicode punctuation (curly apostrophes/quotes U+2019/U+201C/U+201D — 35 questions carry them) is preserved, never converted to ASCII.
- **All four choice lines A–D always present**, in order. The `**Answer: X**` letter must match the pool key exactly.
- **Order:** canonical pool order = subelements T1…T9 then T0; group A–F within each subelement; ascending number within each group. (This is the published order and the audit's `pool_sort_key`; iterating `sorted(pool, key=pool_sort_key)` over `canon/pool-technician.json` yields it.)
- **The published ID line** (answer letter + Part 97 reference as printed in `canon/pool-technician.txt`) rides on a **separate plain-text line after the blockquote, in backticks** — never inside the `> **TnXnn** …` line itself (the audit would read it as part of the question text and fail the quote). Published quirks stay verbatim, never repaired: `T1D09 (B) [97.113(5)(b)]` (citation typo, canon §7.3) and `T1D12 (A)[97.119(a)]` (no space before the bracket, canon §7.15).
- **The one-line "why"** is original prose: a plain sentence (or two short ones max) giving the reason the keyed answer is correct in beginner language, and naming the teaching chapter ("taught in chapter 3"). Never paraphrase the question back; never contradict the canon; where the canon carries the fact, the why should echo it (e.g., T1D09's why cites §97.113(b), not the printed typo).
- Revised questions (T1C01, T5A05, T7A09, T0A10) appear in their **revised 2026-02-19 form** — the canonical files already carry it; quote, don't retype.

## 4. Chapter-mapping table (for the "why" lines — binding, from canon §5)

| Pool groups | Teaching chapter |
|---|---|
| T1A–T1F | chapter 8 |
| T2A–T2C | chapter 6 |
| T3A–T3C | chapter 3 |
| T4A–T4B | chapter 5 |
| T5A–T5D | chapter 1 |
| T6A–T6D | chapter 1 |
| T7A–T7D | chapter 5 |
| T8A | chapter 2 |
| T8B, T8C, T8D | chapter 7 |
| T9A–T9B | chapter 4 |
| T0A–T0C | chapter 9 |

## 5. Production method (recommended)

The 409-block assembly is mechanical — do it with a script, not by hand:

1. Load `canon/pool-technician.json`; iterate `sorted(pool, key=pool_sort_key)` (import `pool_sort_key` from `tools/audit_book.py` or reimplement the same key).
2. For each id, emit the six blockquote lines from the JSON fields (`question`, `choices` A–D, `answer`), then the published ID line parsed from `canon/pool-technician.txt` (match the `^TnXnn (L) […]$` / `^TnXnn (L)[…]$` lines).
3. The "why" lines are authored per subelement (fan out per design §8 step 5) and merged into the skeleton by id — author them in a small dict/TSV, then regenerate. Never hand-edit the generated question text.
4. Verify before finishing: run `python3 tools/audit_book.py` — check #8 must report 0 errors for `appendices/pool.md` (all 409 quoted once, in order, letters matching the key).

## 6. Integrity notes

- Public domain: the NCVEC released this pool into the public domain (2025-12-18); the intro paragraph may say so in one sentence with the validity window 2026-07-01 → 2030-06-30.
- No `**FACT:**` lines required in appendices (exempt from the format laws); no Key Takeaways; no banned phrases anywhere ("little did they know", "in that moment", "a testament to").
- The "why" lines are the only original prose in the appendix — everything else is verbatim pool or the published ID lines.

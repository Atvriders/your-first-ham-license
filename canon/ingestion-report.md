# Ingestion report — 2026–2030 NCVEC Technician (Element 2) question pool

Date: 2026-07-23 (UTC). Operator: automated ingestion (Kimi Code CLI).
Status: **all verification checks passed; audit exit 0; pytest exit 0.**

## 1. Source files

Landing page: <https://ncvec.org/index.php/2026-2030-technician-question-pool>.
Downloaded 2026-07-23 into `canon/source/` (curl with a browser User-Agent; no 403s):

| file | bytes | sha256 |
|---|---:|---|
| `source/ncvec-2026-2030-technician-pool-feb19-2026.docx` | 489,983 | `c3bb9ebf46730a9812ae854d12a93f07b7a38f521441e51c451e917ccb9e3a54` |
| `source/ncvec-2026-2030-technician-pool-feb19-2026.pdf` | 480,239 | `3618649d64df77f2cf217fa79ef82094fe5d2d41b26d20ce08c46ca1c3d5055a` |
| `source/ncvec-2026-2030-technician-pool-3-diagrams.pdf` | 278,003 | `0b2f636a399100ab42a929328e187cef925d6d50666599ad58aff318cd81147c` |
| `source/diagram-t1.jpg` | 115,824 | `7e5f000404feeae942c625a773f0a02c3ee3b5bafda2218d6b8b0d3653288462` |
| `source/diagram-t2.jpg` | 140,293 | `36313bc65ea22bd483e9b0ff2cd8e7dbce3784e2b009046879d8e5959cc9ebf7` |
| `source/diagram-t3.jpg` | 108,532 | `6db1d838f067ecd00a1ee8ad1e396c9e4d4415cfbc75764169a7bc868e44dc52` |

This is the **revised** pool: the document opens with the errata sheet
"2026-2030 Technician Class Pool Errata, Issued February 19, 2026" listing the
4 modified questions (T1C01, T5A05, T7A09, T0A10), and the pool body already
incorporates them (verified in §5). Effective for exams 2026-07-01 … 2030-06-30.
The pool is public domain.

### ARRL cross-check mirror — not available as a separate file

<https://www.arrl.org/question-pools> does **not** host its own copy of the
2026–2030 Technician pool: its "TECHNICIAN POOL" link points back to the NCVEC
page above (confirmed by fetching the page HTML; the only document links are
to ncvec.org). Therefore no NCVEC-vs-ARRL content diff is possible. As a
substitute cross-check with equal evidentiary value, the two independent NCVEC
renderings (.docx vs .pdf) were parsed separately and diffed — see §4.

## 2. Outputs

| file | bytes | sha256 |
|---|---:|---|
| `canon/pool-technician.txt` | 109,214 | `0796b92ebdfe341de22437ba6c185f5cb91c010e58f6ac1f41c05e2a0de90f1b` |
| `canon/pool-technician.json` | 170,569 | `cced9eb89f74f56cd5f195c3b4dd7e10ec09eb66238c1134f269821055a27918` |

`pool-technician.json` matches `tests/fixtures/pool_sample.json` schema
exactly: top-level object keyed by question id; each entry has, in fixture key
order, `group` ("T1A"), `subelement` ("T1"), `question` (single string),
`choices` (object with exactly "A".."D"), `answer` (one of "A".."D"), `figure`
(null, or "T-1"/"T-2"/"T-3"). No extra keys (the Part 97 references are kept
only in the .txt, which preserves the published ID-line format).

`pool-technician.txt` follows `tests/fixtures/pool_sample.txt` layout:
`T1A01 (C) [97.1]` ID line (answer in parentheses, Part 97 ref in brackets
where published), question text, `A.`–`D.` choice lines, `~~` block separator.
Subelement (`SUBELEMENT T1 - …`) and group (`T1A …`) headings are preserved as
published. A `#`-comment header at the top documents provenance and the
normalization rules.

## 3. Converter and normalization rules

Tooling probe: `pandoc` absent, `python-docx` absent, `pdftotext` present.
Chosen converter: **the .docx, parsed directly** with python3 `zipfile` +
`xml.etree.ElementTree` over `word/document.xml` (no third-party packages —
paragraph text assembled from `w:t` runs). The docx carries logical
paragraphs, so wording is byte-exact with no line-wrap artifacts.

Normalization rules (also in the .txt header):

1. Each question/choice printed as one line, exactly as the docx paragraph;
   no re-wrap or reflow. Every one of the 409 questions was exactly one
   paragraph of question text plus 4 single-paragraph choices (0 anomalies
   from the strict parser).
2. U+00A0 → U+0020 (none occurred). Verified zero tabs, zero double spaces,
   zero soft hyphens, zero fi/fl ligatures, zero stray edge whitespace in all
   extracted fields.
3. Published Unicode punctuation preserved byte-exactly: U+2019 (×34),
   U+201C/U+201D (×30 each); en dash U+2013 in headings where published. These
   are the only non-ASCII characters in the pool text.
4. ID lines preserved as published, including `T1D12 (A)[97.119(a)]` — the
   source omits the space before the bracket; preserved verbatim, not "fixed".
5. The PDF (pdftotext -layout) was parsed fully independently for the diff in
   §4; its only wrap artifact (§4) is not in this data.

## 4. Cross-extraction diff (docx vs pdf)

Both parsers produced 409 questions / 35 groups / 10 subelements with
identical id order. Field-by-field diff over question text, all 4 choices per
question, answer letters, Part 97 refs, and all group/subelement headings
(whitespace-normalized): **exactly one difference**, and it is a PDF-side
extraction artifact, not a content difference:

- T9A04 question: pdf `…compared to a full-sized quarter- wave antenna?`
  vs docx `…compared to a full-sized quarter-wave antenna?` — pdftotext split
  the line at the hyphen and the join left a space. Docx is authoritative;
  canonical files carry `quarter-wave`.

No substantive differences. No whitespace-only differences beyond this one.

## 5. Verification evidence

### Counts and structure

- Total questions: **409** (no duplicate ids; document order == canonical
  pool order T1…T9,T0 / group A–F / number).
- Subelements: **exactly 10** (T1–T9, T0). Groups: **35**.
- Numbering contiguous within every group (TnX01..TnX0n, no gaps/dups) —
  verified in both the JSON and by re-parsing the .txt.
- Every question: exactly 4 non-empty choices keyed A–D; answer ∈ {A,B,C,D};
  question text non-empty.

Per-subelement counts (match the syllabus claims printed in the source doc):

| subelement | questions | groups | per-group counts |
|---|---:|---|---|
| T1 | 68 | 6 | T1A:11 T1B:12 T1C:11 T1D:12 T1E:11 T1F:11 |
| T2 | 37 | 3 | T2A:11 T2B:14 T2C:12 |
| T3 | 35 | 3 | T3A:12 T3B:12 T3C:11 |
| T4 | 23 | 2 | T4A:12 T4B:11 |
| T5 | 50 | 4 | T5A:11 T5B:13 T5C:12 T5D:14 |
| T6 | 46 | 4 | T6A:11 T6B:12 T6C:12 T6D:11 |
| T7 | 44 | 4 | T7A:11 T7B:11 T7C:11 T7D:11 |
| T8 | 47 | 4 | T8A:12 T8B:12 T8C:11 T8D:12 |
| T9 | 23 | 2 | T9A:11 T9B:12 |
| T0 | 36 | 3 | T0A:12 T0B:11 T0C:13 |
| **total** | **409** | **35** | |

### Revised questions (Feb 19, 2026 errata) — present, text matches the errata sheet byte-exactly

- **T1C01 (D)**: For which classes of amateur radio licenses does the FCC currently issue new licenses?
- **T5A05 (A)**: A difference in which of the following causes electron flow?
- **T7A09 (B)**: What is the function of the switch which selects either SSB or CW-FM on some VHF power amplifiers?
- **T0A10 (A)**: What hazard exists when rapidly charging or discharging an unprotected battery?

### Figure-referencing questions (3 pool diagrams, 12 questions)

- **T-1** (`source/diagram-t1.jpg`): T6C02, T6C03, T6C04, T6C05, T6D10
- **T-2** (`source/diagram-t2.jpg`): T6A09, T6C06, T6C07, T6C08, T6C09
- **T-3** (`source/diagram-t3.jpg`): T6C10, T6C11

These 12 entries carry `"figure": "T-1"/"T-2"/"T-3"` in the JSON; all other
397 carry `"figure": null`. (Detected by the literal phrase "figure T-n" in
the question text; no figure mentions occur in any choice text.)

### Round-trips

- `json.load()` on `pool-technician.json`: OK; schema/key-order/types checked
  against the fixture shape for all 409 entries.
- `pool-technician.txt` re-parsed with an independent script: 409 question
  blocks, 10 subelement headings, 35 group headings, 33 header-comment lines;
  ids, order, answer letters, question texts, and all 1,636 choice texts
  identical to the JSON (whitespace-normalized comparison).
- `python3 tools/audit_book.py`: **exit 0** — "Audit PASSED: 0 errors,
  0 warning(s)." Check [8/8] loaded the pool JSON, found no chapter quotes to
  check, and printed "appendix coverage skipped (no appendices/pool.md)".
- `python3 -m pytest -q`: **exit 0** — 46 passed.

## 6. Notes on schema adaptation

- The audit's check #8 reads only `canon/pool-technician.json`; the fixture
  schema has no field for the Part 97 rule references. Those references are
  data the NCVEC publishes on the ID line, so they are preserved in the .txt
  ID lines (e.g. `T1A01 (C) [97.1]`) and omitted from the JSON rather than
  adding a non-fixture key.
- `figure` values use the pool's own labels "T-1"/"T-2"/"T-3" (the questions
  literally say "figure T-1" etc.).
- No content wording was altered for schema reasons; the only adaptations are
  the normalization rules in §3.

import json
import pathlib

import pytest

from tools.audit_book import (
    check_appendix_pool_coverage,
    check_banned_phrases,
    check_figure_integrity,
    check_format_laws,
    check_pool_quotes,
    extract_pool_quotes,
    main,
)

POOL_PATH = "tests/fixtures/pool_sample.json"
POOL = json.loads(pathlib.Path(POOL_PATH).read_text(encoding="utf-8"))

CH_SAMPLE = pathlib.Path("tests/fixtures/ch_sample.md").read_text(encoding="utf-8")


# --- Carry-over checks -------------------------------------------------

def test_banned_phrases_flagged():
    errs = check_banned_phrases("…and little did they know it would grow.")
    assert errs and "little did they know" in errs[0]

def test_banned_phrases_clean():
    assert check_banned_phrases("The lamp is lit and the exam begins.") == []

def test_figure_integrity_missing():
    errs = check_figure_integrity(["{{fig:ghost}}"], registry={})
    assert any("ghost" in e for e in errs)

def test_figure_integrity_ok():
    reg = {"tank": {"id":"tank","chapter":1,"number":"1.1","caption":"c","kind":"original","source":"authored","file":"figures/tank.svg"}}
    assert check_figure_integrity(["see {{fig:tank}}"], registry=reg) == []


# --- Format laws (spec §5 skeleton) ----------------------------------------

def test_format_laws_accept_teaching_chapter_fixture():
    assert check_format_laws("ch01", CH_SAMPLE) == []

def test_format_laws_require_exam_focus_in_teaching_chapters():
    text = CH_SAMPLE.replace("### Exam Focus", "### Focus")
    assert any("Exam Focus" in e for e in check_format_laws("ch01", text))

def test_format_laws_forbid_exam_focus_in_bookends():
    assert any("Exam Focus" in e for e in check_format_laws("ch00", CH_SAMPLE))
    assert any("Exam Focus" in e for e in check_format_laws("ch10", CH_SAMPLE))

def test_format_laws_require_worked_example_in_teaching_chapters():
    text = CH_SAMPLE.replace("> **Worked example:**", "> **Example:**")
    assert any("worked example" in e.lower() for e in check_format_laws("ch01", text))

def test_format_laws_require_key_takeaways():
    text = CH_SAMPLE.replace("### Key Takeaways", "### Takeaways")
    assert any("Key Takeaways" in e for e in check_format_laws("ch01", text))

def test_format_laws_heading_number_must_match_file():
    assert any("heading" in e.lower() for e in check_format_laws("ch03", CH_SAMPLE))

def test_format_laws_require_opener_paragraph():
    text = CH_SAMPLE.replace(
        "Your first radio looks like magic until you meet the four ideas behind it: "
        "voltage, current, resistance, and power. In this chapter you'll learn what "
        "each one is, how they fit together, and how little math you actually need.\n\n",
        "",
    )
    assert any("opener" in e.lower() for e in check_format_laws("ch01", text))

def test_format_laws_fact_line_count():
    text = CH_SAMPLE.replace("**FACT:** Ohm's law states that voltage is current multiplied by resistance.\n", "")
    assert any("FACT" in e for e in check_format_laws("ch01", text))


# --- Check #8: pool fidelity -----------------------------------------------

def _quote(qid, question, letter, choices):
    lines = [f"> **{qid}** {question}"]
    lines += [f"> {k}. {v}" for k, v in choices.items()]
    lines.append(f"> **Answer: {letter}** — because the fixture says so.")
    return "\n".join(lines)


def test_pool_quote_correct_passes():
    entry = POOL["T5A02"]
    text = _quote("T5A02", entry["question"], entry["answer"], entry["choices"])
    assert check_pool_quotes(extract_pool_quotes(text), POOL) == []

def test_pool_quote_one_word_off_fails():
    entry = POOL["T5A02"]
    bad = entry["question"].replace("10 ohm", "11 ohm")
    text = _quote("T5A02", bad, entry["answer"], entry["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "T5A02" in errs[0]

def test_pool_quote_wrong_answer_letter_fails():
    entry = POOL["T5A02"]
    wrong = "A" if entry["answer"] != "A" else "B"
    text = _quote("T5A02", entry["question"], wrong, entry["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "answer" in errs[0].lower()

def test_pool_quote_unknown_id_fails():
    text = _quote("T9F01", "Not a real pool question?", "A", POOL["T5A02"]["choices"])
    errs = check_pool_quotes(extract_pool_quotes(text), POOL)
    assert errs and "T9F01" in errs[0]

def _appendix_text(ids):
    return "\n\n".join(
        _quote(qid, POOL[qid]["question"], POOL[qid]["answer"], POOL[qid]["choices"])
        for qid in ids
    )

def test_appendix_coverage_complete_and_in_order_passes():
    ordered = ["T1A01", "T1A02", "T1A03", "T1B01", "T1B02", "T1B03",
               "T2A01", "T2A02", "T2A03", "T5A01", "T5A02", "T5A03"]
    assert check_appendix_pool_coverage(_appendix_text(ordered), POOL) == []

def test_appendix_coverage_missing_id_fails():
    ids = [qid for qid in POOL if qid != "T2A02"]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("T2A02" in e and "missing" in e for e in errs)

def test_appendix_coverage_duplicate_id_fails():
    ids = sorted(POOL) + ["T2A02"]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("T2A02" in e and "once" in e for e in errs)

def test_appendix_coverage_out_of_order_fails():
    ids = sorted(POOL)
    ids[0], ids[1] = ids[1], ids[0]
    errs = check_appendix_pool_coverage(_appendix_text(ids), POOL)
    assert any("order" in e for e in errs)


# --- Check #8 on the empty scaffold: skip, not fail -------------------------

def test_audit_main_skips_pool_check_on_empty_scaffold(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert main() == 0
    out = capsys.readouterr().out.lower()
    assert "pool" in out and "skip" in out


# --- Preface: front matter, exempt from format laws -------------------------

_PREFACE_HEADING = "## Preface — Why & How This Book Was Made\n\n"

def test_audit_main_preface_does_not_trip_format_laws(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    chapters = tmp_path / "chapters"
    chapters.mkdir()
    # This preface would violate every chapter format law (no numbered
    # heading, an Exam Focus section, no Key Takeaways, no FACT lines) --
    # as front matter it is exempt from all of them.
    (chapters / "preface.md").write_text(
        _PREFACE_HEADING +
        "Plain front matter, no teaching-chapter skeleton.\n\n"
        "### Exam Focus\n\nNot a teaching chapter; this section is allowed here.\n",
        encoding="utf-8",
    )
    assert main() == 0

def test_audit_main_preface_still_scanned_for_banned_phrases(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    chapters = tmp_path / "chapters"
    chapters.mkdir()
    (chapters / "preface.md").write_text(
        _PREFACE_HEADING + "Little did they know this book was built by agents.\n",
        encoding="utf-8",
    )
    assert main() == 1

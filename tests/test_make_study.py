import json
import pathlib
import re

import pytest

from tools import make_study

FIX = pathlib.Path("tests/fixtures")
FIXTURE_IDS = {"T1A01", "T1A02", "T1B01", "T2A01", "T5A01", "T6C02"}

REAL_POOL = pathlib.Path("canon/pool-technician.json")
REAL_APPENDIX = pathlib.Path("appendices/pool.md")
REAL_POOL_TXT = pathlib.Path("canon/pool-technician.txt")
REAL_FIGURES = pathlib.Path("figures")


def load_fixture_inputs():
    pool = make_study.load_pool(FIX / "study_pool.json")
    whys = make_study.parse_whys((FIX / "study_appendix.md").read_text(encoding="utf-8"))
    pool_txt = (FIX / "study_pool.txt").read_text(encoding="utf-8")
    return pool, whys, pool_txt


def build_fixture_records():
    pool, whys, pool_txt = load_fixture_inputs()
    return make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def fixture_figures():
    return {"T-1": '<svg viewBox="0 0 10 10"><title>fixture figure T-1</title></svg>'}


def assert_self_contained(html):
    """The pages must work under a strict CSP: nothing external, ever."""
    assert 'src="http' not in html and "src='http" not in html
    assert 'href="http' not in html and "href='http" not in html
    assert "<script src" not in html
    assert "<link" not in html
    assert "<img" not in html


def assert_fully_rendered(html):
    """No template tokens survive; the audiobook theme is in place."""
    assert not re.findall(r"__[A-Z_]+__", html)
    assert "--paper:" in html and "--beam:" in html  # lantern/scope CSS variables
    assert 'class="series-bar"' in html


# ---------- parsers ----------


def test_parse_group_headings_reads_only_heading_lines():
    _, _, pool_txt = load_fixture_inputs()
    headings = make_study.parse_group_headings(pool_txt)
    assert headings == {
        "T1A": "Purpose and permissible use of the Amateur Radio Service; Meanings of basic terms",
        "T1B": "Frequency allocations; Emission modes; Spectrum sharing",
        "T2A": "Station operation: choosing an operating frequency, calling another station",
        "T5A": "Current and voltage: terminology and units",
        "T6C": "Circuit diagrams: use of schematics; Schematic symbols of basic components",
    }


def test_parse_subelement_titles():
    _, _, pool_txt = load_fixture_inputs()
    titles = make_study.parse_subelement_titles(pool_txt)
    assert titles == {
        "T1": "COMMISSION'S RULES",
        "T2": "OPERATING PROCEDURES",
        "T5": "ELECTRICAL PRINCIPLES",
        "T6": "ELECTRONIC AND ELECTRICAL COMPONENTS",
    }


def test_parse_whys_maps_letter_and_text_for_every_entry():
    _, whys, _ = load_fixture_inputs()
    assert set(whys) == FIXTURE_IDS
    letter, why = whys["T5A01"]
    assert letter == "B"
    assert why == "current is measured in amperes — taught in chapter 1."


# ---------- chapter map (accuracy-canon.md §5) ----------


@pytest.mark.parametrize(
    "subelement,group,chapter",
    [
        ("T1", "T1F", 8),
        ("T2", "T2C", 6),
        ("T3", "T3A", 3),
        ("T4", "T4B", 5),
        ("T5", "T5D", 1),
        ("T6", "T6A", 1),
        ("T7", "T7D", 5),
        ("T8", "T8A", 2),   # T8A is owned by ch02
        ("T8", "T8B", 7),   # T8B–T8D are owned by ch07
        ("T8", "T8D", 7),
        ("T9", "T9B", 4),
        ("T0", "T0C", 9),
    ],
)
def test_chapter_for_matches_canon_map(subelement, group, chapter):
    assert make_study.chapter_for(subelement, group) == chapter


# ---------- record assembly ----------


def test_build_records_assembles_every_field():
    records = build_fixture_records()
    assert [r["id"] for r in records] == ["T1A01", "T1A02", "T1B01", "T2A01", "T5A01", "T6C02"]
    rec = records[0]
    assert rec["group"] == "T1A"
    assert rec["subelement"] == "T1"
    assert rec["question"].startswith("Which agency")
    assert set(rec["choices"]) == {"A", "B", "C", "D"}
    assert rec["answer"] == "A"
    assert rec["why"] == "the FCC is the US regulator — taught in chapter 8."
    assert rec["groupTheme"].startswith("Purpose and permissible use")
    assert rec["chapter"] == 8
    assert "figure" not in rec  # figure key only present on figure questions


def test_build_records_marks_only_the_figure_question():
    records = build_fixture_records()
    with_fig = {r["id"]: r["figure"] for r in records if "figure" in r}
    assert with_fig == {"T6C02": "T-1"}


def test_build_records_fails_on_missing_why():
    pool, whys, pool_txt = load_fixture_inputs()
    del whys["T2A01"]
    with pytest.raises(ValueError, match="T2A01"):
        make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def test_build_records_fails_on_answer_letter_mismatch():
    pool, whys, pool_txt = load_fixture_inputs()
    whys["T5A01"] = ("C", whys["T5A01"][1])
    with pytest.raises(ValueError, match="T5A01"):
        make_study.build_records(pool, whys, make_study.parse_group_headings(pool_txt))


def test_build_records_fails_on_missing_group_heading():
    pool, whys, pool_txt = load_fixture_inputs()
    headings = make_study.parse_group_headings(pool_txt)
    del headings["T6C"]
    with pytest.raises(ValueError, match="T6C"):
        make_study.build_records(pool, whys, headings)


# ---------- validation ----------


def test_validate_records_accepts_the_fixture_set():
    records = build_fixture_records()
    make_study.validate_records(records, expected_count=6, figure_ids={"T6C02"})


def test_validate_records_rejects_an_unexpected_figure_reference():
    records = build_fixture_records()
    records[0]["figure"] = "T-1"  # T1A01 is not one of the known figure questions
    with pytest.raises(ValueError, match="T1A01"):
        make_study.validate_records(records, expected_count=6, figure_ids={"T6C02"})


def test_validate_records_rejects_empty_fields():
    records = build_fixture_records()
    records[1]["why"] = ""
    with pytest.raises(ValueError, match="T1A02"):
        make_study.validate_records(records, expected_count=6, figure_ids={"T6C02"})


def test_validate_records_checks_the_count():
    records = build_fixture_records()
    with pytest.raises(ValueError):
        make_study.validate_records(records[:-1], expected_count=6, figure_ids={"T6C02"})


# ---------- the real canon data ----------


def build_real_records():
    pool = make_study.load_pool(REAL_POOL)
    whys = make_study.parse_whys(REAL_APPENDIX.read_text(encoding="utf-8"))
    headings = make_study.parse_group_headings(REAL_POOL_TXT.read_text(encoding="utf-8"))
    return make_study.build_records(pool, whys, headings)


def test_real_pool_assembles_409_valid_records():
    records = build_real_records()
    assert len(records) == 409
    make_study.validate_records(records)  # defaults: 409 records, the 12 known figure ids


def test_real_pool_subelement_summaries_cover_t1_through_t0():
    records = build_real_records()
    titles = make_study.parse_subelement_titles(REAL_POOL_TXT.read_text(encoding="utf-8"))
    subs = make_study.subelement_summaries(records, titles)
    assert [s["id"] for s in subs] == ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T0"]
    assert sum(s["count"] for s in subs) == 409
    assert all(s["title"] for s in subs)
    assert subs[0]["count"] == 68  # T1 — Commission's Rules


def test_load_figures_reads_the_three_redrawn_pool_svgs():
    figures = make_study.load_figures(REAL_FIGURES)
    assert set(figures) == {"T-1", "T-2", "T-3"}
    for svg in figures.values():
        assert svg.lstrip().startswith("<svg")


# ---------- page rendering ----------


def test_flashcards_page_embeds_every_record_with_hints_and_marks():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    for qid in FIXTURE_IDS:
        assert qid in html
    assert "yfhl-study" in html            # localStorage namespace for review-later marks
    assert "Hint: this is" in html         # hint line template
    assert "review chapter" in html        # chapter pointer in the hint
    assert "fixture figure T-1" in html    # figure SVG embedded inline
    assert "COMMISSION'S RULES" in html    # subelement labels for the filter
    assert_self_contained(html)
    assert_fully_rendered(html)


def test_practice_page_states_the_35_26_rule_and_drill_mode():
    records = build_fixture_records()
    titles = make_study.parse_subelement_titles((FIX / "study_pool.txt").read_text(encoding="utf-8"))
    html = make_study.render_practice_html(
        records, fixture_figures(), make_study.subelement_summaries(records, titles))
    assert "35 questions" in html
    assert "26 to pass" in html
    assert "New exam" in html
    assert "Drill" in html                 # per-subelement drill mode
    for qid in FIXTURE_IDS:
        assert qid in html                 # pool embedded as JSON
    assert_self_contained(html)
    assert_fully_rendered(html)


def test_flashcards_page_contains_every_real_pool_id():
    records = build_real_records()
    titles = make_study.parse_subelement_titles(REAL_POOL_TXT.read_text(encoding="utf-8"))
    html = make_study.render_flashcards_html(
        records, make_study.load_figures(REAL_FIGURES),
        make_study.subelement_summaries(records, titles))
    assert len(re.findall(r'"id": "T\d[A-F]\d\d"', html)) == 409
    for qid in ("T1A01", "T5C09", "T0C12", "T6C02", "T6D10"):
        assert qid in html
    assert_self_contained(html)


# ---------- CLI ----------


def test_main_writes_both_pages(tmp_path):
    rc = make_study.main([
        "--pool", str(FIX / "study_pool.json"),
        "--appendix", str(FIX / "study_appendix.md"),
        "--pool-txt", str(FIX / "study_pool.txt"),
        "--figures-dir", str(REAL_FIGURES),
        "--out", str(tmp_path),
        "--expect", "6", "--figure-ids", "T6C02",
    ])
    assert rc == 0
    flash = (tmp_path / "flashcards.html").read_text(encoding="utf-8")
    practice = (tmp_path / "practice.html").read_text(encoding="utf-8")
    for qid in FIXTURE_IDS:
        assert qid in flash and qid in practice
    assert "35 questions" in practice and "26 to pass" in practice
    assert "yfhl-study" in flash
    assert_self_contained(flash)
    assert_self_contained(practice)
    assert_fully_rendered(flash)
    assert_fully_rendered(practice)


def test_main_refuses_an_invalid_record_set(tmp_path):
    # expecting 7 records from a 6-question fixture must fail validation
    rc = make_study.main([
        "--pool", str(FIX / "study_pool.json"),
        "--appendix", str(FIX / "study_appendix.md"),
        "--pool-txt", str(FIX / "study_pool.txt"),
        "--figures-dir", str(REAL_FIGURES),
        "--out", str(tmp_path),
        "--expect", "7", "--figure-ids", "T6C02",
    ])
    assert rc == 1
    assert not (tmp_path / "flashcards.html").exists()

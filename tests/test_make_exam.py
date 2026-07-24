import json
import pathlib

from tools.make_exam import draw_exam, load_pool, render_exam, render_key

POOL_PATH = pathlib.Path("tests/fixtures/pool_sample.json")
POOL = json.loads(POOL_PATH.read_text(encoding="utf-8"))
GROUPS = {"T1A", "T1B", "T2A", "T5A"}  # 4 groups x 3 questions in the fixture


def test_load_pool_returns_all_entries():
    pool = load_pool(POOL_PATH)
    assert len(pool) == 12
    entry = pool["T5A02"]
    assert entry["group"] == "T5A"
    assert entry["subelement"] == "T5"
    assert set(entry["choices"]) == {"A", "B", "C", "D"}
    assert entry["answer"] in "ABCD"


def test_draw_exam_picks_exactly_one_question_per_group():
    exam = draw_exam(load_pool(POOL_PATH), seed=1)
    assert len(exam) == len(GROUPS)
    assert {q.group for q in exam} == GROUPS


def test_draw_exam_is_reproducible_with_seed():
    first = [q.id for q in draw_exam(load_pool(POOL_PATH), seed=42)]
    second = [q.id for q in draw_exam(load_pool(POOL_PATH), seed=42)]
    assert first == second


def test_draw_exam_only_draws_pool_questions_in_order():
    exam = draw_exam(load_pool(POOL_PATH), seed=7)
    ids = [q.id for q in exam]
    assert all(qid in POOL for qid in ids)
    assert ids == sorted(ids)  # canonical pool order (T1 < T2 < T5 here)


def test_render_exam_has_questions_and_choices_but_no_answers():
    exam = draw_exam(load_pool(POOL_PATH), seed=3)
    sheet = render_exam(exam)
    for q in exam:
        assert q.question in sheet
        for text in q.choices.values():
            assert text in sheet
    # nothing on the exam sheet may reveal the key
    lowered = sheet.lower()
    assert "answer" not in lowered
    assert "key" not in lowered
    for i, q in enumerate(exam, start=1):
        assert f"{i}. {q.answer}" not in sheet  # no "1. D"-style key rows


def test_render_key_lists_correct_letters_and_subelement_tally():
    exam = draw_exam(load_pool(POOL_PATH), seed=3)
    key = render_key(exam)
    for i, q in enumerate(exam, start=1):
        assert f"{i}. {q.answer}" in key
    # fixture tally: T1 x2 groups, T2 x1, T5 x1
    assert "T1: 2" in key
    assert "T2: 1" in key
    assert "T5: 1" in key


def test_cli_writes_exam_and_key(tmp_path):
    from tools.make_exam import main
    rc = main(["--seed", "5", "--pool", str(POOL_PATH), "--out", str(tmp_path)])
    assert rc == 0
    exam_md = (tmp_path / "practice-exam.md").read_text(encoding="utf-8")
    key_md = (tmp_path / "practice-exam-key.md").read_text(encoding="utf-8")
    assert "T1" in exam_md and "answer" not in exam_md.lower()
    assert "T1: 2" in key_md

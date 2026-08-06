import pathlib

from tools.make_audiobook import (
    dest_name,
    parse_chapters,
    parse_sections,
    prepare_preface,
    prepare_text,
    spoken_heading,
)

def test_spoken_heading_numbered_chapter():
    assert spoken_heading("4. Antennas & Feedlines") == \
        "Chapter Four. Antennas & Feedlines."

def test_spoken_heading_chapter_zero():
    assert spoken_heading("0. Welcome: What Ham Radio Is & How Licensing Works") == \
        "Chapter Zero. Welcome: What Ham Radio Is & How Licensing Works."

def test_spoken_heading_passthrough():
    assert spoken_heading("Something unexpected") == "Something unexpected"

def test_spoken_heading_preface():
    assert spoken_heading("Preface — Why & How This Book Was Made") == \
        "Preface: Why and How This Book Was Made."

def test_dest_name_preface_default_voice():
    assert dest_name("ryan", "preface") == "preface.mp3"

def test_dest_name_preface_other_voices():
    for v in ("sonia", "andrew", "ava", "william", "natasha", "connor", "emily"):
        assert dest_name(v, "preface") == f"{v}-preface.mp3"

def test_dest_name_chapters_unchanged():
    assert dest_name("ryan", 0) == "ch00.mp3"
    assert dest_name("ryan", 10) == "ch10.mp3"
    assert dest_name("sonia", 0) == "sonia-ch00.mp3"
    assert dest_name("emily", 10) == "emily-ch10.mp3"

def test_parse_sections():
    assert parse_sections("preface") == ["preface"]
    assert parse_sections("chapters") == ["chapters"]
    assert parse_sections("all") == ["chapters", "preface"]
    assert parse_sections("chapters,preface") == ["chapters", "preface"]
    assert parse_sections("") == ["chapters", "preface"]

def test_prepare_preface_narration():
    title, text = prepare_preface(pathlib.Path("tests/fixtures/preface.md"))
    assert title == "Preface: Why and How This Book Was Made."
    # narration opens with the spoken title, no chapter preamble
    assert text.startswith(title + "\n\n")
    assert "Your First Ham License. The Technician Course" not in text
    # ### subheads drop to plain lines; no heading markup survives
    assert "Why This Book Exists" in text
    assert "How It Was Made" in text
    assert "#" not in text
    # no chapter numbering leaks into the preface narration
    assert "Chapter" not in text.split("\n\n", 1)[0]

def test_parse_chapters_defaults_to_eleven():
    assert parse_chapters("") == list(range(11))
    assert parse_chapters("0-12") == list(range(11))  # clamped to 0..10

def test_chapter_discovery_never_picks_up_preface():
    # narration sources are addressed by number as ch{n:02d}.md, so a
    # chapters/preface.md can never be picked up as a chapter track
    names = [f"ch{n:02d}.md" for n in parse_chapters("")]
    assert "preface.md" not in names

def test_prepare_text_speaks_math_and_drops_fig_markup():
    out = prepare_text("The tank obeys $E = IR$ here.\n\n{{fig:x}}\n", {"x": ("1", "a tank")})
    assert "E equals I R" in out
    assert "{{fig" not in out
    assert "Figure 1" in out

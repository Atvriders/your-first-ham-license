from tools.make_audiobook import VOICES
from tools.make_intro import INTRO, intro_name

OTHER_VOICES = ("sonia", "andrew", "ava", "william", "natasha", "connor", "emily")


def test_intro_name_default_voice():
    assert intro_name("ryan") == "intro.mp3"


def test_intro_name_other_voices():
    for v in OTHER_VOICES:
        assert intro_name(v) == f"{v}-intro.mp3"


def test_intro_name_covers_all_eight_voices():
    names = {intro_name(v) for v in VOICES}
    assert len(names) == 8
    assert "intro.mp3" in names
    assert all(n == "intro.mp3" or n.endswith("-intro.mp3") for n in names)


def test_intro_text_mentions_eight_voices():
    # the narration itself advertises the eight-voice edition
    assert "eight voices" in INTRO

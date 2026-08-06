"""Synthesize the audiobook introduction (audiobook/intro.mp3) with edge-tts.

A short spoken preface that opens the audiobook: a welcome to the absolute
beginner, what Your First Ham License is, that it was written by Claude
Opus 4.8 running in Claude Code, and how to use the eight-voice edition.
Kept separate from the chapter tracks so it can be regenerated on its own.

Usage:
  python tools/make_intro.py        # writes audiobook/intro.mp3
  python tools/make_intro.py --dry  # print the intro text and exit (no synth, no network)

Requires: edge-tts (pip install edge-tts) and ffmpeg on PATH.
Edit VOICE or INTRO and rerun to change the narration.
"""

import asyncio
import subprocess
import sys
from pathlib import Path

import edge_tts

VOICE = "en-GB-RyanNeural"
OUT = Path(__file__).resolve().parent.parent / "audiobook" / "intro.mp3"

INTRO = """Your First Ham License: The Technician Course, 2026 to 2030. A welcome.

This audiobook was written by Claude Opus 4.8 — an artificial intelligence made by Anthropic — running inside the coding tool Claude Code.

If you have never touched a radio, never studied electronics, and are not entirely sure what a ham is — you are exactly who this course was written for. In eleven chapters it walks you from curious to licensed: what amateur radio is and how the exam works, how signals travel, antennas and stations, operating on repeaters, the rules in plain English, safety, and finally exam day itself. Every fact and every practice question is checked against the official twenty twenty-six to twenty thirty Technician question pool, so what you hear is what the exam asks.

This edition is offered in eight voices — American, British, Australian, and Irish, male and female.

A word about why this book exists, and how it was made. It exists to take you from never having touched a radio to a passed Technician exam — teaching first, then aligning every chapter to the exam. And it was built by a multi-agent AI workflow — the official public-domain question pool, every question verbatim, every answer key machine-verified — about 3.6 million tokens of AI work.

And now — Your First Ham License. Begin whenever you are ready."""


async def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    raw = OUT.with_suffix(".raw.mp3")
    last = None
    for attempt in range(1, 6):
        try:
            await edge_tts.Communicate(INTRO, VOICE).save(str(raw))
            if raw.stat().st_size > 500:
                break
            raise RuntimeError("empty audio")
        except Exception as e:  # noqa: BLE001 - retry any transport error
            last = e
            await asyncio.sleep(2 * attempt)
    else:
        raise RuntimeError(f"synthesis failed after retries: {last}")

    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
            "-c", "copy",
            "-metadata", "title=Introduction",
            "-metadata", "artist=Claude Opus 4.8",
            "-metadata", "album=Your First Ham License",
            "-metadata", "track=0/11",
            "-metadata", "genre=Audiobook",
            "-metadata", "date=2026",
            str(OUT),
        ],
        check=True,
    )
    raw.unlink(missing_ok=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    if "--dry" in sys.argv[1:]:
        print(INTRO)
        sys.exit(0)
    asyncio.run(main())

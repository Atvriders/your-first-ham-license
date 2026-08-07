"""Synthesize the audiobook introduction in all eight voices with edge-tts.

A short spoken welcome that opens the audiobook: what Your First Ham
License is, that it was written by Kimi K3 running in Kimi Code, and how
to use the eight-voice edition. Kept separate from the chapter tracks so
it can be regenerated on its own.

The default voice (Ryan, British male) writes `audiobook/intro.mp3`;
every other voice writes `audiobook/<voice>-intro.mp3` — the same naming
scheme as `<voice>-preface.mp3`, so the player can switch voices on the
intro exactly like on any other track.

Usage:
  python tools/make_intro.py              # default voice (ryan) -> intro.mp3
  python tools/make_intro.py --all        # every voice (skips files that exist)
  python tools/make_intro.py --voice ava  # one voice -> ava-intro.mp3
  python tools/make_intro.py --dry        # print the intro text and exit (no synth, no network)

Requires: edge-tts (pip install edge-tts) and ffmpeg on PATH.
Edit INTRO and rerun with --force to change the narration.
"""

import argparse
import asyncio
import subprocess
import sys
from pathlib import Path

import edge_tts

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.make_audiobook import DEFAULT_VOICE, VOICES, dest_name

OUT_DIR = Path(__file__).resolve().parent.parent / "audiobook"

RETRIES = 5

INTRO = """Your First Ham License: The Technician Course, 2026 to 2030. A welcome.

This audiobook was written by Kimi K3 — an artificial intelligence made by Moonshot AI — running inside Kimi Code.

If you have never touched a radio, never studied electronics, and are not entirely sure what a ham is — you are exactly who this course was written for. In eleven chapters it walks you from curious to licensed: what amateur radio is and how the exam works, how signals travel, antennas and stations, operating on repeaters, the rules in plain English, safety, and finally exam day itself. Every fact and every practice question is checked against the official twenty twenty-six to twenty thirty Technician question pool, so what you hear is what the exam asks.

This edition is offered in eight voices — American, British, Australian, and Irish, male and female.

A word about why this book exists, and how it was made. It exists to take you from never having touched a radio to a passed Technician exam — teaching first, then aligning every chapter to the exam. And it was built by a multi-agent AI workflow — the official public-domain question pool, every question verbatim, every answer key machine-verified — about 3.6 million tokens of AI work.

And now — Your First Ham License. Begin whenever you are ready."""


def intro_name(voice_key: str) -> str:
    """MP3 filename for the intro in the given voice: ryan -> intro.mp3,
    every other voice -> <voice>-intro.mp3 (same scheme as the preface)."""
    return dest_name(voice_key, "intro")


async def synth_intro(voice_key: str, force: bool = False) -> str:
    """Synthesize the intro in one voice; skip if the MP3 already exists."""
    voice, label, accent, gender = VOICES[voice_key]
    dest = OUT_DIR / intro_name(voice_key)
    if not force and dest.exists() and dest.stat().st_size > 100_000:
        return f"skip  {dest.name} (exists)"
    raw = dest.with_suffix(".raw.mp3")
    last = None
    for attempt in range(1, RETRIES + 1):
        try:
            await edge_tts.Communicate(INTRO, voice).save(str(raw))
            if raw.stat().st_size > 500:
                break
            raise RuntimeError("empty audio")
        except Exception as e:  # noqa: BLE001 - retry any transport error
            last = e
            await asyncio.sleep(min(2 * attempt, 12))
    else:
        raise RuntimeError(f"synthesis failed after {RETRIES} tries: {last}")

    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
            "-c", "copy",
            "-metadata", "title=Introduction",
            "-metadata", "artist=Kimi K3",
            "-metadata", "album=Your First Ham License",
            "-metadata", "track=0/11",
            "-metadata", "genre=Audiobook",
            "-metadata", "date=2026",
            "-metadata", f"composer={label}",
            "-metadata", f"comment=Read by {label} ({accent} {gender})",
            str(dest),
        ],
        check=True,
    )
    raw.unlink(missing_ok=True)
    return f"done  {dest.name} ({dest.stat().st_size / 1e6:.2f} MB) — {label}"


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", choices=list(VOICES), default=DEFAULT_VOICE)
    ap.add_argument("--all", action="store_true", help="synthesize every voice")
    ap.add_argument("--force", action="store_true", help="rebuild existing files")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    keys = list(VOICES) if args.all else [args.voice]
    failed = []
    for key in keys:
        try:
            print(await synth_intro(key, args.force), flush=True)
        except Exception as e:  # noqa: BLE001 - report and continue with the rest
            failed.append(f"{key}: {e}")
    if failed:
        print("FAILED:\n" + "\n".join(failed), flush=True)
        sys.exit(1)
    print("ALL DONE", flush=True)


if __name__ == "__main__":
    if "--dry" in sys.argv[1:]:
        print(INTRO)
        sys.exit(0)
    asyncio.run(main())

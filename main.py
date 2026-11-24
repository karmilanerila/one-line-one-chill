#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry (harness program/v1).

Writes one sentence of horror to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(or ``/output/entry.txt`` when the variable is unset).

The line: a phone gallery full of photos of the narrator asleep,
taken from inside the closet, one for every night this week.
The scare is earned, not announced: no monster is named, no gore,
just the fact that someone has been standing in the room, every
night, while the narrator slept — and is still doing it.
"""

import os

LINE = (
    "My phone's gallery holds photos of me sleeping, "
    "taken from inside the closet, one for every night this week."
)


def main() -> None:
    # Guard the gate before writing: UTF-8, 1-200 chars, one sentence.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "line must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

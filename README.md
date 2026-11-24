# One Line, One Chill

Entry for the make.fun bounty **"One Line, One Chill"**
(`u-azazex-one-line-one-chill-6d4d5488`): one line of horror, a single
sentence under 200 characters that frightens a reader in one breath.

## The line

> My phone's gallery holds photos of me sleeping, taken from inside the closet, one for every night this week.

108 characters, one sentence, no trailing newline.

## Why this line

The judge weighs, in order: reads as a horror story in one sentence;
frightens with dread that outlasts the line; vivid concrete detail;
original turn; well-built sentence.

- **Horror story in one sentence:** a complete scare with a beginning
  (the gallery), a discovery (photos of the narrator asleep), and a
  kicker (one for every night this week).
- **Earned dread:** no monster is named and nothing is announced. The
  fear comes from what the line withholds — who is standing in the
  closet, and the fact that it is still happening tonight.
- **Vivid and specific:** a phone gallery, sleeping photos, inside the
  closet, one dated for every night this week. No vague darkness.
- **Original turn:** the camera is the narrator's own phone, and the
  photographer shoots from inside the room — not a mirror, doll,
  or basement.
- **Craft:** the rhythm builds across three clauses and the last words
  — "one for every night this week" — land the blow.

## How it runs

`main.py` (stdlib only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with
`open("wb")` and mode `0644`, no tempfile. It asserts the gate first:
UTF-8, 1–200 characters, a single sentence.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.

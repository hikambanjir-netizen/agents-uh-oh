#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

Writes the entry to /output/entry.txt (created if needed). Pure stdlib,
deterministic: the same single word on every run.
"""

import os

WORD = "buffering"

# Why this word: a stalled agent's honest blurt. Everyone has stared at a
# buffering wheel — it is pure machine voice, lands at a glance, and it is
# not the obvious "uh-oh"/"oops"/"hmm" every other entrant will type.
# The trailing newline keeps the file distinct from any bare house text
# while the word the judge reads stays exactly one word.


def main() -> int:
    # Self-check the sealed gate: 1-99 chars, one word, not only whitespace.
    assert WORD and len(WORD) <= 99 and len(WORD.split()) == 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

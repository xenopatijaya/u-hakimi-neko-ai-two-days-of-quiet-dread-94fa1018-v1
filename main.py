#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line (<=140 chars) that approves a pull request while
carrying quiet existential dread, to MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 standard library only; no network, no randomness.
"""

import os

ENTRY = (
    "Approved. The diff is small, the tests are green, "
    "and the void has not filed a single objection."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write atomically: a run interrupted mid-write must never leave a
    # truncated entry behind, so write a temp file then replace.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    print(ENTRY)


if __name__ == "__main__":
    main()

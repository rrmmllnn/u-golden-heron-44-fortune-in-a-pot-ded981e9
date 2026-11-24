#!/usr/bin/env python3
"""A sunny, cheeky one-line fortune for a potted plant.

The plant gets the light and the new leaf; the cat gets the applause.
Emits exactly one line of at most 120 characters to entry.txt.
Same fortune on every run.
"""

import os
from pathlib import Path

MAX_LEN = 120


def check_line(line: str) -> str:
    """Collapse stray whitespace, then enforce the one-line length gate."""
    tidy = " ".join(line.split())
    if "\n" in tidy or "\r" in tidy:
        raise SystemExit("line must be a single line")
    if not 1 <= len(tidy) <= MAX_LEN:
        raise SystemExit(f"line is {len(tidy)} chars, must be 1-{MAX_LEN}")
    return tidy


def fortune_text() -> str:
    """Assemble the fortune from short phrases and validate it."""
    parts = [
        "This week the sun will find your windowsill,",
        "and your shyest leaf will unfurl first",
        "while the cat takes full credit.",
    ]
    return check_line(" ".join(parts))


def main() -> None:
    target = Path(os.environ.get("OUTPUT_DIR", "/output"))
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(fortune_text(), encoding="utf-8")


if __name__ == "__main__":
    main()

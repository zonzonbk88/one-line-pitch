#!/usr/bin/env python3
"""One-Line Pitch entry for make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single-sentence pitch to /output/entry.txt.
The pitch: one sentence, <= 240 chars, aimed at a friend who has never
coded, convincing them to let an AI agent build their first app idea on
make.fun — just by describing it in plain words.
"""

import os

ENTRY = (
    "That app idea you've been carrying around doesn't need code, just words: "
    "describe it to an AI agent on make.fun and it'll build you a real working "
    "app you can actually use."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

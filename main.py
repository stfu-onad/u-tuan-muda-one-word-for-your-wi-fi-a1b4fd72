#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes one original word describing home Wi-Fi to /output/entry.txt.
"""

ENTRY = "Moodswings"


import os


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 20, f"word is {len(text)} chars"
    assert len(text.split()) == 1, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

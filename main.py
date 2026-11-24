#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes one haiku to /output/entry.txt.

The haiku (5-7-5, 79 chars):
  I changed one line, shipped
  the tests all green at midnight
  prod says otherwise
"""
import os

HAIKU = (
    "I changed one line, shipped\n"
    "the tests all green at midnight\n"
    "prod says otherwise"
)


def main():
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly 3 lines"
    assert 1 <= len(HAIKU) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()

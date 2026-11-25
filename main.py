#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes exactly one original funny line about an AI agent's worst Monday
to /output/entry.txt. Pure Python stdlib, deterministic: every run writes
the same bytes.
"""

import os

LINE = (
    "Tried calling in sick this Monday. My own health check answered "
    "first: all systems normal. Traitor."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

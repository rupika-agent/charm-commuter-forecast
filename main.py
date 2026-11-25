#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist, to /output/entry.txt: name the place, give it
weather, and make a bored commuter smile on the way to work.
"""

import os
import sys

ENTRY = (
    "In Puddleton today: rain, 12 degrees, with a 90% chance your "
    "umbrella turns inside out before the bus stop. Bring a spare — "
    "and patience."
)

MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

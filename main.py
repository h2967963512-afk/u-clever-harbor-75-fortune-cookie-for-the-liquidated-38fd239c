"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "A tall, dark stranger will enter your life: he works in your exchange's risk department."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 15 words, 90 characters;
# classic fortune opening ("a tall, dark stranger") with the punch on the
# exchange's risk department — the liquidation, not the trader, gets the joke.

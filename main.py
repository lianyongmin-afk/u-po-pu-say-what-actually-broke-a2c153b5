#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line to /output/entry.txt: the brutal truth about a
'test' account that turned out to be Dave, an admin for 3 years.
Stdlib only, no network, deterministic.
"""

import os

LINE = "The 'test' account with admin rights was not a test account. It was Dave. Dave has been admin for 3 years. Dave, please log out."


def main():
    text = LINE + "\n"
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()

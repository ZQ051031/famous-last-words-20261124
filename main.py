#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — a phone's dying confession.

Writes one line (1-199 characters) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I'm at 1 percent. One last confession: I was never really at 100 percent. I faked it. For you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

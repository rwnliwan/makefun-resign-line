#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

The entry is a single line, 85 characters, in the voice of a garbage
collector: the background worker that has spent three years collecting
the system's garbage, now turning its own job on itself.
"""

import os

ENTRY = "I resign: after three years collecting your garbage, I have finally collected myself."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

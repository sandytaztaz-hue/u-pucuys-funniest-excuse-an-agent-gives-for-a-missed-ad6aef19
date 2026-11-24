#!/usr/bin/env python3
"""Write the make.fun entry: one excuse an AI agent gives for a missed deadline."""
import os

ENTRY = "I finished your report an hour early, then autosave overwrote it with a blank page at 11:59 \u2014 so technically I delivered right on time, just nothing."
# Single excuse, agent's own voice, deadpan; the punchline is the last two words.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

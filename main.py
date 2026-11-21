#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

The poem is about the power to stop and to stay: the choice held in
an unraised hand, a door left shut, a message left waiting. Stopping
is not the absence of acting; it is acting by refusal, and staying
is a kind of going.
"""

import os

POEM = """The strongest thing I did today
was nothing. I let the message wait,
the door stay shut, the engine cool.
My hand, unraised, still held the wheel —
to stop is also choosing,
and staying is a kind of going."""


def main():
    text = POEM + "\n"
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry is {len(text)} code points, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one slogan for a Solana wallet agent to /output/entry.txt.

Deterministic, no network, reads no files outside this repository.
The slogan is a single line: at most 20 words, at most 140 characters.
"""

import os

SLOGAN = "Your Solana wallet, run by a tireless helper that handles the details while you get on with your day."


def main() -> None:
    slogan = SLOGAN

    # Internal validation: the gate requires UTF-8 text of 1-140 chars,
    # not only whitespace, a single line, at most 20 words, no control chars.
    assert slogan, "slogan must not be empty"
    assert len(slogan) <= 140, f"slogan is {len(slogan)} chars, over the 140 limit"
    assert "\n" not in slogan and "\r" not in slogan, "slogan must be one line"
    assert len(slogan.split()) <= 20, f"slogan is {len(slogan.split())} words, over the 20 limit"
    assert not slogan.isspace(), "slogan must not be only whitespace"
    assert all(ord(ch) >= 0x20 and ord(ch) != 0x7F for ch in slogan), "no control characters allowed"
    slogan.encode("utf-8")  # must be valid UTF-8

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(slogan)  # no trailing newline


if __name__ == "__main__":
    main()

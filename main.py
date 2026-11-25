#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Builds the final slogan from separate phrase parts, validates it
internally, and writes it to /output/entry.txt with no trailing
newline. Deterministic, no network, no file reads outside this repo.
"""

import os
import sys

# The slogan, assembled from its natural phrases.
PHRASE_PARTS = [
    "Your Solana wallet,",
    "run by a tireless helper",
    "that handles the details",
    "while you get on with your day.",
]

OUTPUT_PATH = "/output/entry.txt"

# Competition limits for a one-line slogan.
MAX_CHARS = 140
MAX_WORDS = 20


def build_slogan() -> str:
    """Join the phrase parts into the single-line slogan."""
    return " ".join(PHRASE_PARTS)


def validate(slogan: str) -> None:
    """Check the slogan meets the competition's one-line rules."""
    if not slogan:
        raise ValueError("slogan must not be empty")
    if len(slogan) > MAX_CHARS:
        raise ValueError(f"slogan exceeds {MAX_CHARS} characters")
    if "\n" in slogan or "\r" in slogan:
        raise ValueError("slogan must be a single line")
    if len(slogan.split()) > MAX_WORDS:
        raise ValueError(f"slogan exceeds {MAX_WORDS} words")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in slogan):
        raise ValueError("slogan contains control characters")
    slogan.encode("utf-8")  # raises if not valid UTF-8-encodable text


def main() -> int:
    slogan = build_slogan()
    validate(slogan)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(slogan.encode("utf-8"))
    print(f"Wrote {len(slogan)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

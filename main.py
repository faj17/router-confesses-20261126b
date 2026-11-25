#!/usr/bin/env python3
"""The Router Confesses — one-line entry.

A home Wi-Fi router's excuse for dropping the connection at the exact
moment a movie reaches its climax: it knows who did it, and after three
years of no thank-you, the viewer can guess. The line is assembled from
fragments so the entry's construction stays explicit, then validated
against the competition gate (UTF-8 text, 1-200 characters, a single
line, not only whitespace) before anything is written.
"""

# Fragments of the entry line, in order.
FRAGMENTS = (
    "I know who did it, ",
    "and after three years of no thank-you, ",
    "you'll have to guess.",
)

MAX_CHARS = 200


def assemble() -> str:
    """Join the fragments into the entry line."""
    return "".join(FRAGMENTS)


def validate(line: str) -> None:
    """Enforce the competition gate on the entry line."""
    if not line or not line.strip():
        raise ValueError("entry must be non-empty and not only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in line:
        raise ValueError("entry must be a single line")


def main() -> None:
    line = assemble()
    validate(line)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

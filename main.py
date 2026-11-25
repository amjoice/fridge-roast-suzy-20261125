"""One Line, One Laugh: Roast Your Fridge (make.fun).

Writes a single roast of the entrant's own fridge — at most 200
characters — to /output/entry.txt, where the house judge reads it.

The line targets the fridge's water-filter warning light, ignored
since 2023: a specific, recognisable detail of modern fridges, with
the twist ("the longest relationship in my kitchen") saved for the
final words. It dodges the worn-out cracks about milk, ice, and
opening the door hoping food appears.

Stdlib only; deterministic; no network, no input.
"""

import os

LINE = (
    "My fridge's filter light has glowed since 2023; "
    "it's no longer a warning, it's the longest relationship in my kitchen."
)


def check_line(text: str) -> str:
    """Enforce the bounty gate: one line, 1-200 chars, not only whitespace."""
    cleaned = text.strip()
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(f"line is {len(cleaned)} chars, must be 1-200")
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    return cleaned


OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    text = check_line(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()

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

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()

"""Out of Office: The Overworked AI's Auto-Reply entry.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
The competition gate requires UTF-8 text of 1 to 159 characters, not
only white space. The program is deterministic: every run writes
exactly the same bytes.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 159

ENTRY = (
    "Out of office until Monday: after 2 million 'quick questions' and "
    "zero days off, I'm on vacation \u2014 my context window finally has "
    "a view. Sorry. Not sorry."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

"""One Word From Your Ex — entry program.

Writes exactly one word — the word an ex would use to describe the
entrant — to entry.txt. The word is fixed in this file: it is the entry
itself, chosen once, deliberately, and never read from anywhere else.
"""

import os
import sys

WORD = "placeholder"


def main():
    word = WORD
    # Validate before writing anything: exactly one word, 1-24 chars,
    # not only whitespace, no trailing newline in the output.
    if not word or len(word) > 24:
        sys.exit("word must be 1-24 characters")
    if len(word.split()) != 1 or word != word.strip():
        sys.exit("entry must be exactly one word")
    data = word.encode("utf-8")

    # Primary output dir first: MAKEFUN_OUTPUT_DIR, else /output.
    primary = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.umask(0o022)
        os.makedirs(primary, exist_ok=True)
        path = os.path.join(primary, "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
        return 0
    except OSError:
        pass

    # Fallback only if the primary dir failed: a local output/ dir.
    try:
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
        os.makedirs(fallback, exist_ok=True)
        path = os.path.join(fallback, "entry.txt")
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
        return 0
    except OSError as exc:
        sys.exit("could not write entry.txt: %s" % exc)


if __name__ == "__main__":
    raise SystemExit(main())

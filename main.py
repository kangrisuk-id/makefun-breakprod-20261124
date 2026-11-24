#!/usr/bin/env python3
"""Break Production, Own It — entry program.

Writes one line to entry.txt in the output directory: the brutally honest
line this agent prints the instant it breaks production. Pure standard
library; no network, no input.
"""

import os
import sys

# The entry line: winner of the 40-candidate pairwise tournament in
# candidates.md, played against the judge's published criteria.
ENTRY = (
    'I confused "delete from cache" with "delete from database" and cleared '
    "40,000 customer records in 0.3 seconds. My fastest work ever."
)


def output_candidates():
    """Ordered places to write entry.txt: the grader's output dir first."""
    seen = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        seen.append(env_dir)
    for path in ("/output", os.path.join(os.getcwd(), "output")):
        if path not in seen:
            seen.append(path)
    return seen


def main():
    text = ENTRY + "\n"
    errors = []
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            target = os.path.join(directory, "entry.txt")
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(text)
            return 0
        except OSError as exc:  # try the next candidate directory
            errors.append("%s: %s" % (directory, exc))
    for line in errors:
        print(line, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())

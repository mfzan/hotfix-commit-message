#!/usr/bin/env python3
"""3 AM hotfix commit-message entry.

Writes a single commit message -- the funniest 3 AM hotfix confession --
to entry.txt inside the grader's output directory. One line, nothing else.
"""

import os

# The confession: the 3 AM fix was undoing the 2 AM "fix". It works now,
# nobody knows why, and the only safe instruction left is hands off.
MESSAGE = "3am hotfix: reverted my 2am fix and prod is back; no idea why, do not touch it"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(MESSAGE)
    # The grader collects outputs as another user: the file itself must be
    # world-readable. Only the file is chmodded, never the output directory.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

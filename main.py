# SPDX-License-Identifier: MIT
# ai-joke-03 entry (re-entry v2): writes one fixed joke about AI coding
# agents to /output/entry.txt. Standard library only: no network, no clock,
# no randomness, so both runs write the same bytes.

import os
from pathlib import Path

# The joke is a fixed literal: the judge reads exactly the bytes written,
# so no line end is added and nothing is computed at run time.
JOKE = "I told my coding agent to stop touching unrelated files, so it merged the whole repo into index.ts."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(output_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()

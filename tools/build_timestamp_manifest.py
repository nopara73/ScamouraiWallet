#!/usr/bin/env python3
"""Build the stable core-file manifest submitted to OpenTimestamps."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "timestamps" / "ARCHIVE_SHA256SUMS"
FILES = (
    ".zenodo.json",
    "BIBLIOGRAPHY.txt",
    "CITATION.cff",
    "CLAIMS.jsonl",
    "CORRECTIONS.md",
    "ENTITY_ALIASES.json",
    "EVIDENCE_MANIFEST.json",
    "METHODOLOGY.md",
    "POST_MORTEM.md",
    "TIMELINE.md",
    "docs/index.html",
    "docs/metadata.json",
    "output/pdf/POST_MORTEM.pdf",
    "sources/SHA256SUMS",
)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def render() -> str:
    missing = [name for name in FILES if not (ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError("missing timestamp targets: " + ", ".join(missing))
    return "".join(f"{digest(ROOT / name)}  {name}\n" for name in sorted(FILES))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        expected = render()
    except FileNotFoundError as error:
        print(error, file=sys.stderr)
        return 1
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected:
            print("timestamps/ARCHIVE_SHA256SUMS is missing or stale", file=sys.stderr)
            return 1
        print(f"verified {len(FILES)} timestamp targets")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT.relative_to(ROOT)} with {len(FILES)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

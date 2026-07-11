#!/usr/bin/env python3
"""Build the repository-wide, machine-readable evidence manifest.

The authoritative byte hashes live in sources/SHA256SUMS. This script joins
those hashes with file sizes, media types, and the source URLs mapped in
sources/URLS.md. It deliberately refuses to bless a stale or malformed hash
manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HASH_FILE = ROOT / "sources" / "SHA256SUMS"
URL_FILE = ROOT / "sources" / "URLS.md"
OUTPUT_FILE = ROOT / "EVIDENCE_MANIFEST.json"

HASH_LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")
URL_BULLET = re.compile(r"^- <(https?://[^>]+)>\s+—\s+(.+)$")
LOCAL_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def evidence_snapshot_commit() -> str | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", "sources"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    value = result.stdout.strip()
    return value or None


def parse_url_map() -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for line in URL_FILE.read_text(encoding="utf-8").splitlines():
        match = URL_BULLET.match(line)
        if not match:
            continue
        source_url, description = match.groups()
        for relative_path in LOCAL_LINK.findall(description):
            if relative_path.startswith(("http://", "https://", "#")):
                continue
            key = relative_path.replace("\\", "/")
            mapping.setdefault(key, []).append(source_url)
    return {key: sorted(set(urls)) for key, urls in mapping.items()}


def load_entries() -> list[dict[str, object]]:
    url_map = parse_url_map()
    entries: list[dict[str, object]] = []
    seen: set[str] = set()
    errors: list[str] = []

    for number, line in enumerate(
        HASH_FILE.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        match = HASH_LINE.match(line)
        if not match:
            errors.append(f"{HASH_FILE}:{number}: malformed hash line")
            continue
        expected_hash, relative = match.groups()
        relative = relative.replace("\\", "/")
        if relative in seen:
            errors.append(f"duplicate manifest path: {relative}")
            continue
        seen.add(relative)

        absolute = ROOT / "sources" / Path(relative)
        if not absolute.is_file():
            errors.append(f"missing evidence file: sources/{relative}")
            continue
        actual_hash = sha256(absolute)
        if actual_hash != expected_hash:
            errors.append(
                f"hash mismatch: sources/{relative} expected {expected_hash}, got {actual_hash}"
            )
            continue

        media_type, _ = mimetypes.guess_type(absolute.name)
        entries.append(
            {
                "path": f"sources/{relative}",
                "sha256": expected_hash,
                "bytes": absolute.stat().st_size,
                "media_type": media_type or "application/octet-stream",
                "source_urls": url_map.get(relative, []),
            }
        )

    if errors:
        raise ValueError("\n".join(errors))
    return entries


def build_manifest() -> dict[str, object]:
    entries = load_entries()
    return {
        "schema_version": "1.0.0",
        "title": "Scamourai Wallet post-mortem evidence manifest",
        "description": (
            "Byte-level inventory of the locally preserved evidence archive. "
            "Source URLs are joined from sources/URLS.md where a mapping exists."
        ),
        "hash_algorithm": "SHA-256",
        "hash_source": "sources/SHA256SUMS",
        "url_source": "sources/URLS.md",
        "evidence_snapshot_commit": evidence_snapshot_commit(),
        "entry_count": len(entries),
        "entries": entries,
    }


def serialized_manifest() -> str:
    return json.dumps(build_manifest(), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="verify hashes and committed output"
    )
    args = parser.parse_args()

    try:
        rendered = serialized_manifest()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if args.check:
        if not OUTPUT_FILE.is_file():
            print(f"missing generated file: {OUTPUT_FILE}", file=sys.stderr)
            return 1
        if OUTPUT_FILE.read_text(encoding="utf-8") != rendered:
            print(
                "EVIDENCE_MANIFEST.json is stale; run tools/build_evidence_manifest.py",
                file=sys.stderr,
            )
            return 1
        print(f"verified {build_manifest()['entry_count']} evidence files and manifest")
        return 0

    OUTPUT_FILE.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_FILE.relative_to(ROOT)} with {build_manifest()['entry_count']} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

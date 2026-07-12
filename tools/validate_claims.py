#!/usr/bin/env python3
"""Validate the v1.0 machine-readable claims index and its local references."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "CLAIMS.jsonl"
ESSAY = ROOT / "POST_MORTEM.md"
EXPECTED_COUNT = 35
FIELDS = {
    "claim_id",
    "claim",
    "subject",
    "date",
    "primary_source_url",
    "archived_source_path",
    "supporting_excerpt",
    "source_type",
    "confidence",
    "caveat",
    "essay_section",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def essay_sections() -> set[str]:
    try:
        source = ESSAY.read_text(encoding="utf-8")
    except OSError as error:
        fail(f"Cannot read POST_MORTEM.md: {error}")
    return {
        match.group(1).strip()
        for match in re.finditer(r"^##\s+(.+?)\s*$", source, flags=re.MULTILINE)
    }


def load_records() -> list[dict[str, object]]:
    try:
        lines = CLAIMS.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        fail(f"Cannot read CLAIMS.jsonl: {error}")

    records: list[dict[str, object]] = []
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            fail(f"CLAIMS.jsonl:{line_number}: blank rows are not allowed")
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            fail(f"CLAIMS.jsonl:{line_number}: invalid JSON: {error}")
        if not isinstance(record, dict):
            fail(f"CLAIMS.jsonl:{line_number}: each row must be a JSON object")
        records.append(record)
    return records


def validate_record(
    record: dict[str, object], line_number: int, sections: set[str]
) -> None:
    keys = set(record)
    if keys != FIELDS:
        missing = sorted(FIELDS - keys)
        unexpected = sorted(keys - FIELDS)
        fail(
            f"CLAIMS.jsonl:{line_number}: schema mismatch; "
            f"missing={missing}, unexpected={unexpected}"
        )
    for field in FIELDS:
        value = record[field]
        if not isinstance(value, str) or not value.strip():
            fail(f"CLAIMS.jsonl:{line_number}: {field} must be a non-empty string")

    expected_id = f"CLM-{line_number:03d}"
    if record["claim_id"] != expected_id:
        fail(
            f"CLAIMS.jsonl:{line_number}: expected claim_id {expected_id}, "
            f"found {record['claim_id']!r}"
        )

    source_url = urlsplit(str(record["primary_source_url"]))
    if source_url.scheme not in {"http", "https"} or not source_url.netloc:
        fail(f"CLAIMS.jsonl:{line_number}: primary_source_url is not HTTP(S)")

    relative = PurePosixPath(str(record["archived_source_path"]))
    if relative.is_absolute() or ".." in relative.parts:
        fail(f"CLAIMS.jsonl:{line_number}: archived_source_path escapes the repository")
    archived = ROOT.joinpath(*relative.parts).resolve()
    if not archived.is_relative_to(ROOT) or not archived.is_file():
        fail(
            f"CLAIMS.jsonl:{line_number}: archived source is missing: "
            f"{record['archived_source_path']}"
        )

    if record["essay_section"] not in sections:
        fail(
            f"CLAIMS.jsonl:{line_number}: essay_section is not a level-two heading: "
            f"{record['essay_section']!r}"
        )

    excerpt_words = len(str(record["supporting_excerpt"]).split())
    if excerpt_words > 25:
        fail(
            f"CLAIMS.jsonl:{line_number}: supporting_excerpt has {excerpt_words} "
            "words; maximum is 25"
        )

    if record["confidence"] not in {"high", "medium", "low"}:
        fail(
            f"CLAIMS.jsonl:{line_number}: confidence must be high, medium, or low"
        )


def main() -> int:
    records = load_records()
    if len(records) != EXPECTED_COUNT:
        fail(
            f"CLAIMS.jsonl must contain exactly {EXPECTED_COUNT} rows for v1.0; "
            f"found {len(records)}"
        )
    sections = essay_sections()
    for line_number, record in enumerate(records, 1):
        validate_record(record, line_number, sections)
    print(
        f"Verified {len(records)} sequential claims, local sources, sections, "
        "URLs, and excerpt limits."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

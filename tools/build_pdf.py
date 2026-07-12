#!/usr/bin/env python3
"""Render the canonical HTML edition to a release PDF with Chromium.

The committed Pages edition keeps off-screen images lazy for web readers. For
printing, this script makes them eager and rewrites pinned GitHub image URLs to
the checked-out local evidence files. That makes the PDF independent of network
timing while preserving the canonical hyperlinks in the article.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs" / "index.html"
SITE_CSS = ROOT / "docs" / "assets" / "site.css"
OUTPUT = ROOT / "output" / "pdf" / "POST_MORTEM.pdf"
WORK = ROOT / "tmp" / "pdfs" / "build"

RAW_IMAGE = re.compile(
    r'src="https://raw\.githubusercontent\.com/nopara73/ScamouraiWallet/'
    r'[0-9a-f]{40}/(sources/[^"]+)"'
)
PINNED_PDF_URL = re.compile(
    rb"https://raw\.githubusercontent\.com/nopara73/ScamouraiWallet/"
    rb"[0-9a-f]{40}/output/pdf/POST_MORTEM\.pdf"
)
NAMED_FOOTNOTE = re.compile(r"\[(?:xpub-seizure|zerolink|operator|full-node-claim|[a-z][a-z0-9-]{2,})\]")


def source_sha256() -> str:
    source = (ROOT / "POST_MORTEM.md").read_text(encoding="utf-8")
    normalized = source.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def site_fingerprint_sha256() -> str:
    """Hash the site while abstracting the PDF's self-referential commit URL."""

    site = SITE.read_bytes()
    normalized, replacements = PINNED_PDF_URL.subn(
        b"https://raw.githubusercontent.com/nopara73/ScamouraiWallet/"
        b"{PDF_REVISION}/output/pdf/POST_MORTEM.pdf",
        site,
    )
    if not replacements:
        raise RuntimeError("canonical site does not contain its pinned publication PDF URL")
    return hashlib.sha256(normalized + b"\0" + SITE_CSS.read_bytes()).hexdigest()


def publication_metadata() -> dict[str, object]:
    try:
        metadata = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
        version = str(metadata["version"])
        publication_date = str(metadata["publication_date"])
    except (OSError, KeyError, json.JSONDecodeError) as error:
        raise RuntimeError(f"cannot read publication metadata: {error}") from error
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise RuntimeError("publication version is not semantic")
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", publication_date):
        raise RuntimeError("publication date must use YYYY-MM-DD")
    for field in ("title", "description", "keywords", "creators"):
        if not metadata.get(field):
            raise RuntimeError(f"publication metadata is missing {field}")
    creator_name = str(metadata["creators"][0]["name"])
    if ", " not in creator_name:
        raise RuntimeError("publication creator must use 'Family, Given' form")
    family, given = creator_name.split(", ", 1)
    return {
        "title": str(metadata["title"]),
        "author": f"{given} {family} (nopara73)",
        "subject": str(metadata["description"]),
        "keywords": ", ".join(str(value) for value in metadata["keywords"]),
        "version": version,
        "publication_date": publication_date,
    }


def expected_pdf_metadata() -> dict[str, str]:
    publication = publication_metadata()
    version = str(publication["version"])
    publication_date = str(publication["publication_date"])
    compact_date = publication_date.replace("-", "")
    return {
        "/Title": str(publication["title"]),
        "/Author": str(publication["author"]),
        "/Subject": str(publication["subject"]),
        "/Keywords": str(publication["keywords"]),
        "/Creator": "ScamouraiWallet canonical HTML edition",
        "/Producer": "Chromium PDF renderer; metadata normalized with pypdf",
        "/CreationDate": f"D:{compact_date}000000Z",
        "/ModDate": f"D:{compact_date}000000Z",
        "/ScamouraiVersion": version,
        "/ScamouraiPublicationDate": publication_date,
        "/ScamouraiSourceSHA256": source_sha256(),
        "/ScamouraiSiteFingerprintSHA256": site_fingerprint_sha256(),
    }


def file_uri(path: Path) -> str:
    return path.resolve().as_uri()


def find_chrome(explicit: str | None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    for variable in ("CHROME_PATH", "CHROMIUM_PATH"):
        if os.environ.get(variable):
            candidates.append(Path(os.environ[variable]))
    for command in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        resolved = shutil.which(command)
        if resolved:
            candidates.append(Path(resolved))
    candidates.extend(
        [
            Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
            Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
            Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        ]
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        "Chrome/Chromium was not found. Pass --chrome or set CHROME_PATH."
    )


def prepare_print_html() -> Path:
    html = SITE.read_text(encoding="utf-8")
    html = html.replace(
        'href="assets/site.css"',
        f'href="{file_uri(ROOT / "docs" / "assets" / "site.css")}"',
    )
    html = html.replace('loading="lazy"', 'loading="eager"')

    def local_image(match: re.Match[str]) -> str:
        target = ROOT / Path(match.group(1))
        if not target.is_file():
            raise FileNotFoundError(f"missing local print image: {target}")
        return f'src="{file_uri(target)}"'

    html = RAW_IMAGE.sub(local_image, html)
    html = html.replace(
        "</head>",
        """  <style>
  @media print {
    .edition-metadata, .abstract { break-inside: avoid; }
    .essay > h1 { break-after: avoid; }
  }
  </style>
</head>""",
    )
    WORK.mkdir(parents=True, exist_ok=True)
    target = WORK / "print.html"
    target.write_text(html, encoding="utf-8", newline="\n")
    return target


def render(chrome: Path, print_html: Path) -> Path:
    raw_pdf = WORK / "POST_MORTEM.chrome.pdf"
    if raw_pdf.exists():
        raw_pdf.unlink()
    command = [
        str(chrome),
        "--headless=new",
        "--disable-gpu",
        "--allow-file-access-from-files",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=30000",
        f"--print-to-pdf={raw_pdf}",
        file_uri(print_html),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, timeout=180)
    if completed.returncode != 0 or not raw_pdf.is_file():
        detail = (completed.stderr or completed.stdout).strip()
        raise RuntimeError(f"Chromium PDF rendering failed: {detail}")
    return raw_pdf


def verify_pdf(path: Path) -> int:
    if not path.is_file():
        raise FileNotFoundError(f"publication PDF is missing: {path}")
    reader = PdfReader(path, strict=False)
    if len(reader.pages) < 2:
        raise RuntimeError("rendered PDF has an implausible page count")

    actual_metadata = reader.metadata or {}
    for key, expected in expected_pdf_metadata().items():
        actual = actual_metadata.get(key)
        if actual != expected:
            raise RuntimeError(
                f"publication PDF metadata is stale for {key}: "
                f"expected {expected!r}, found {actual!r}; rebuild it"
            )

    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    normalized_text = re.sub(r"\s+", " ", text)
    title = str(publication_metadata()["title"])
    if re.sub(r"\s+", "", title) not in re.sub(r"\s+", "", normalized_text):
        raise RuntimeError("rendered PDF does not contain the report title")
    leaked = sorted(set(NAMED_FOOTNOTE.findall(text)))
    if leaked:
        raise RuntimeError(f"named Markdown footnote keys leaked into PDF: {leaked}")
    return len(reader.pages)


def normalize_metadata(raw_pdf: Path) -> None:
    reader = PdfReader(raw_pdf, strict=False)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.add_metadata(expected_pdf_metadata())
    staged = WORK / "POST_MORTEM.metadata.pdf"
    with staged.open("wb") as stream:
        writer.write(stream)

    verify_pdf(staged)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    os.replace(staged, OUTPUT)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chrome", help="path to a Chrome, Chromium, or Edge executable")
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that the committed PDF matches the current essay and site",
    )
    args = parser.parse_args()
    try:
        if args.check:
            pages = verify_pdf(OUTPUT)
            print(f"verified {OUTPUT.relative_to(ROOT)} ({pages} pages)")
            return 0
        chrome = find_chrome(args.chrome)
        print_html = prepare_print_html()
        raw_pdf = render(chrome, print_html)
        normalize_metadata(raw_pdf)
    except (FileNotFoundError, OSError, PdfReadError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(error, file=sys.stderr)
        return 1
    pages = len(PdfReader(OUTPUT).pages)
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({pages} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

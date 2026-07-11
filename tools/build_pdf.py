#!/usr/bin/env python3
"""Render the canonical HTML edition to a release PDF with Chromium.

The committed Pages edition keeps off-screen images lazy for web readers. For
printing, this script makes them eager and rewrites pinned GitHub image URLs to
the checked-out local evidence files. That makes the PDF independent of network
timing while preserving the canonical hyperlinks in the article.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs" / "index.html"
OUTPUT = ROOT / "output" / "pdf" / "POST_MORTEM.pdf"
WORK = ROOT / "tmp" / "pdfs" / "build"

TITLE = "Post-Mortem: What Happened Between Samourai Wallet and Me"
AUTHOR = "Ádám Ficsór (nopara73)"
SUBJECT = "A sourced account of the conflict between nopara73 and Samourai Wallet"
KEYWORDS = "Bitcoin, Samourai Wallet, Wasabi Wallet, ZeroLink, CoinJoin, xpub, digital preservation"

RAW_IMAGE = re.compile(
    r'src="https://raw\.githubusercontent\.com/nopara73/ScamouraiWallet/'
    r'[0-9a-f]{40}/(sources/[^"]+)"'
)
NAMED_FOOTNOTE = re.compile(r"\[(?:xpub-seizure|zerolink|operator|full-node-claim|[a-z][a-z0-9-]{2,})\]")


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


def normalize_metadata(raw_pdf: Path) -> None:
    reader = PdfReader(raw_pdf, strict=False)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.add_metadata(
        {
            "/Title": TITLE,
            "/Author": AUTHOR,
            "/Subject": SUBJECT,
            "/Keywords": KEYWORDS,
            "/Creator": "ScamouraiWallet canonical HTML edition",
            "/Producer": "Chromium PDF renderer; metadata normalized with pypdf",
            "/CreationDate": "D:20260711000000+02'00'",
            "/ModDate": "D:20260711000000+02'00'",
        }
    )
    staged = WORK / "POST_MORTEM.metadata.pdf"
    with staged.open("wb") as stream:
        writer.write(stream)

    verified = PdfReader(staged, strict=False)
    if len(verified.pages) < 2:
        raise RuntimeError("rendered PDF has an implausible page count")
    text = "\n".join(page.extract_text() or "" for page in verified.pages)
    normalized_text = re.sub(r"\s+", " ", text)
    if "Post-Mortem: What Happened" not in normalized_text or "Between Samourai Wallet and Me" not in normalized_text:
        raise RuntimeError("rendered PDF does not contain the report title")
    leaked = sorted(set(NAMED_FOOTNOTE.findall(text)))
    if leaked:
        raise RuntimeError(f"named Markdown footnote keys leaked into PDF: {leaked}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    os.replace(staged, OUTPUT)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chrome", help="path to a Chrome, Chromium, or Edge executable")
    args = parser.parse_args()
    try:
        chrome = find_chrome(args.chrome)
        print_html = prepare_print_html()
        raw_pdf = render(chrome, print_html)
        normalize_metadata(raw_pdf)
    except (FileNotFoundError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(error, file=sys.stderr)
        return 1
    pages = len(PdfReader(OUTPUT).pages)
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({pages} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

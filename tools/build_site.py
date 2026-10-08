#!/usr/bin/env python3
"""Build the deterministic, static GitHub Pages edition of POST_MORTEM.md.

Run from any directory:

    python tools/build_site.py
    python tools/build_site.py --check

The check mode performs no writes and exits nonzero when a managed file in
``docs/`` is missing or differs from a fresh build.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
from functools import lru_cache
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
from typing import Final, NoReturn
from urllib.parse import quote, urlsplit

import markdown
import yaml
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


EXPECTED_MARKDOWN_VERSION: Final = "3.10.2"
ROOT: Final = Path(__file__).resolve().parent.parent
SOURCE: Final = ROOT / "POST_MORTEM.md"
DOCS: Final = ROOT / "docs"
ZENODO_METADATA: Final = ROOT / ".zenodo.json"
CITATION_METADATA: Final = ROOT / "CITATION.cff"

OWNER: Final = "nopara73"
REPOSITORY: Final = "ScamouraiWallet"
DEFAULT_BRANCH: Final = "master"
REPOSITORY_URL: Final = f"https://github.com/{OWNER}/{REPOSITORY}"
CANONICAL_URL: Final = f"https://{OWNER}.github.io/{REPOSITORY}/"
SUBTITLE: Final = (
    "How a wallet that adopted my privacy framework turned technical disagreement "
    "into a reputational war—and what I got wrong too"
)
AUTHOR_URL: Final = "https://adamficsor.com/"


def fail(message: str) -> NoReturn:
    raise SystemExit(message)


@dataclass(frozen=True)
class PublicationMetadata:
    title: str
    author: str
    version: str
    publication_date: str
    abstract: str
    keywords: tuple[str, ...]


def normalized_text(value: object) -> str:
    return " ".join(str(value).split())


def cff_date(value: object) -> str:
    return value.isoformat() if isinstance(value, date) else str(value)


def load_publication_metadata() -> PublicationMetadata:
    """Load and cross-check the publication identity in Zenodo and CFF files."""

    try:
        zenodo = json.loads(ZENODO_METADATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Cannot read .zenodo.json publication metadata: {error}")

    try:
        cff = yaml.safe_load(CITATION_METADATA.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        fail(f"Cannot read CITATION.cff publication metadata: {error}")
    if not isinstance(zenodo, dict) or not isinstance(cff, dict):
        fail("Publication metadata roots must be objects")

    title = str(zenodo.get("title", "")).strip()
    version = str(zenodo.get("version", "")).strip()
    publication_date = str(zenodo.get("publication_date", "")).strip()
    abstract = normalized_text(zenodo.get("description", ""))
    keywords_value = zenodo.get("keywords")
    if not title or not abstract:
        fail(".zenodo.json title and description must be non-empty")
    if not isinstance(keywords_value, list) or not keywords_value or not all(
        isinstance(keyword, str) and keyword.strip() for keyword in keywords_value
    ):
        fail(".zenodo.json keywords must be a non-empty string list")
    keywords = tuple(keyword.strip() for keyword in keywords_value)
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        fail(".zenodo.json must contain a semantic version such as 1.0.0")
    try:
        date.fromisoformat(publication_date)
    except ValueError:
        fail(".zenodo.json publication_date must use YYYY-MM-DD")

    preferred = cff.get("preferred-citation")
    if not isinstance(preferred, dict):
        fail("CITATION.cff must define preferred-citation")
    comparisons = {
        "title": (cff.get("title"), preferred.get("title"), title),
        "version": (cff.get("version"), preferred.get("version"), version),
        "release date": (
            cff_date(cff.get("date-released")),
            cff_date(preferred.get("date-published")),
            publication_date,
        ),
        "abstract": (cff.get("abstract"), abstract, abstract),
        "repository URL": (
            cff.get("repository-code"),
            preferred.get("repository-code"),
            REPOSITORY_URL,
        ),
        "canonical URL": (cff.get("url"), preferred.get("url"), CANONICAL_URL),
    }
    for label, values in comparisons.items():
        normalized = tuple(normalized_text(value) for value in values)
        if len(set(normalized)) != 1:
            fail(f"CITATION.cff and .zenodo.json {label} values do not agree")

    cff_keywords = cff.get("keywords")
    if not isinstance(cff_keywords, list) or tuple(cff_keywords) != keywords:
        fail("CITATION.cff and .zenodo.json keywords do not agree")
    if str(cff.get("license", "")).lower() != str(zenodo.get("license", "")).lower():
        fail("CITATION.cff and .zenodo.json licenses do not agree")
    if str(preferred.get("license", "")).lower() != str(zenodo.get("license", "")).lower():
        fail("preferred-citation and .zenodo.json licenses do not agree")
    if cff.get("type") != "dataset" or preferred.get("type") != "report":
        fail("CITATION.cff must describe a dataset with a preferred report citation")
    if zenodo.get("upload_type") != "publication" or zenodo.get("publication_type") != "report":
        fail(".zenodo.json must describe a publication/report")

    try:
        cff_author = cff["authors"][0]
        preferred_author = preferred["authors"][0]
        creator_name = zenodo["creators"][0]["name"]
        given = str(cff_author["given-names"]).strip()
        family = str(cff_author["family-names"]).strip()
    except (KeyError, IndexError, TypeError) as error:
        fail(f"Publication author metadata is incomplete: {error}")
    expected_cff_author = {"given-names": given, "family-names": family}
    if not isinstance(preferred_author, dict):
        fail("preferred-citation author metadata must be an object")
    if any(preferred_author.get(key) != value for key, value in expected_cff_author.items()):
        fail("Top-level and preferred-citation authors do not agree")
    if creator_name != f"{family}, {given}":
        fail("CITATION.cff and .zenodo.json author names do not agree")

    related = {
        item.get("identifier")
        for item in zenodo.get("related_identifiers", [])
        if isinstance(item, dict)
    }
    if not {REPOSITORY_URL, CANONICAL_URL}.issubset(related):
        fail(".zenodo.json must link the repository and canonical site")

    return PublicationMetadata(
        title=title,
        author=f"{given} {family}",
        version=version,
        publication_date=publication_date,
        abstract=abstract,
        keywords=keywords,
    )


PUBLICATION = load_publication_metadata()
TITLE = PUBLICATION.title
AUTHOR = PUBLICATION.author
VERSION = PUBLICATION.version
PUBLICATION_DATE = PUBLICATION.publication_date
ABSTRACT = PUBLICATION.abstract
KEYWORDS = list(PUBLICATION.keywords)


def git_raw(*args: str) -> str:
    """Return Git output without trimming porcelain-significant whitespace."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as error:
        details = getattr(error, "stderr", "") or str(error)
        fail(f"Unable to determine the source revision: {details.strip()}")
    return result.stdout


def git(*args: str) -> str:
    """Return a trimmed Git value, failing with a useful build error."""
    return git_raw(*args).strip()


@lru_cache(maxsize=1)
def dirty_repository_paths() -> frozenset[str]:
    raw = git_raw("status", "--porcelain=v1", "-z", "--untracked-files=all")
    fields = raw.split("\0")
    dirty: set[str] = set()
    index = 0
    while index < len(fields):
        field = fields[index]
        index += 1
        if not field:
            continue
        status = field[:2]
        dirty.add(field[3:].replace("\\", "/"))
        if ("R" in status or "C" in status) and index < len(fields):
            if fields[index]:
                dirty.add(fields[index].replace("\\", "/"))
            index += 1
    return frozenset(dirty)


@lru_cache(maxsize=1)
def repository_history() -> tuple[dict[str, str], tuple[tuple[str, str], ...]]:
    """Index newest path revisions with one Git history traversal."""

    output = git(
        "-c",
        "core.quotepath=false",
        "log",
        "--format=@@%H",
        "--name-only",
        "--no-renames",
        "HEAD",
        "--",
    )
    newest: dict[str, str] = {}
    ordered: list[tuple[str, str]] = []
    revision = ""
    for line in output.splitlines():
        if line.startswith("@@"):
            revision = line[2:]
            if not re.fullmatch(r"[0-9a-f]{40}", revision):
                fail(f"Unexpected revision in Git history: {revision!r}")
        elif line and revision:
            path = line.replace("\\", "/")
            ordered.append((path, revision))
            newest.setdefault(path, revision)
    return newest, tuple(ordered)


@lru_cache(maxsize=None)
def repository_revision(relative_path: str) -> str:
    """Return the newest commit containing a clean repository path."""

    relative_path = normalize_relative_path(relative_path)
    target = ROOT.joinpath(*PurePosixPath(relative_path).parts)
    if not target.exists():
        fail(f"Linked repository path does not exist: {relative_path}")

    dirty = dirty_repository_paths()
    prefix = relative_path.rstrip("/") + "/"
    if relative_path in dirty or any(path.startswith(prefix) for path in dirty):
        fail(
            f"Linked repository path has uncommitted changes: {relative_path}. "
            "Commit it before building immutable site links."
        )

    newest, ordered = repository_history()
    revision = newest.get(relative_path)
    if revision is None and target.is_dir():
        revision = next(
            (commit for path, commit in ordered if path.startswith(prefix)), None
        )
    if revision is None:
        fail(f"Unable to find a committed revision for {relative_path!r}")
    return revision


def source_revision() -> str:
    return repository_revision(SOURCE.name)


def pinned_file_url(relative_path: str, *, raw: bool = False) -> str:
    """Return an immutable URL pinned to the commit that last changed a file."""

    relative_path = normalize_relative_path(relative_path)
    revision = repository_revision(relative_path)
    encoded_path = quote_url_path(relative_path)
    if raw:
        return (
            f"https://raw.githubusercontent.com/{OWNER}/{REPOSITORY}/"
            f"{revision}/{encoded_path}"
        )
    return f"{REPOSITORY_URL}/blob/{revision}/{encoded_path}"


def normalize_relative_path(path: str) -> str:
    """Normalize a repository-relative URL path and reject repository escapes."""
    normalized = posixpath.normpath(path.replace("\\", "/"))
    if normalized in {"", "."}:
        return ""
    if normalized == ".." or normalized.startswith("../") or normalized.startswith("/"):
        fail(f"Repository-relative link escapes the repository: {path!r}")
    return normalized


def quote_url_path(path: str) -> str:
    # Preserve the characters GitHub accepts in path segments while encoding spaces,
    # non-ASCII characters, and URL-delimiter characters safely.
    return quote(path, safe="/@:+-._~!$&'()*+,;=")


class RepositoryLinkTreeprocessor(Treeprocessor):
    """Make source links work when the rendered page lives below docs/."""

    def __init__(self, md: markdown.Markdown) -> None:
        super().__init__(md)
        self.image_number = 0

    def rewrite(self, value: str, *, image: bool) -> str:
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or value.startswith(("#", "//")):
            return value

        relative_path = normalize_relative_path(parsed.path)
        if not relative_path:
            return value

        encoded_path = quote_url_path(relative_path)
        revision = repository_revision(relative_path)
        if image:
            base = (
                f"https://raw.githubusercontent.com/{OWNER}/{REPOSITORY}/"
                f"{revision}/"
            )
        else:
            local_target = ROOT.joinpath(*PurePosixPath(relative_path).parts)
            route = "tree" if local_target.is_dir() or parsed.path.endswith("/") else "blob"
            base = f"{REPOSITORY_URL}/{route}/{revision}/"

        rewritten = base + encoded_path
        if parsed.query:
            rewritten += f"?{parsed.query}"
        if parsed.fragment:
            rewritten += f"#{parsed.fragment}"
        return rewritten

    def run(self, root):  # type: ignore[no-untyped-def]
        for element in root.iter():
            if element.tag == "a" and element.get("href"):
                classes = (element.get("class") or "").split()
                if "footnote-backref" in classes:
                    element.set(
                        "aria-label",
                        element.get("title") or "Return to the footnote reference",
                    )
                element.set("href", self.rewrite(element.get("href", ""), image=False))
            elif element.tag == "img" and element.get("src"):
                self.image_number += 1
                element.set("src", self.rewrite(element.get("src", ""), image=True))
                if not (element.get("alt") or "").strip():
                    filename = PurePosixPath(urlsplit(element.get("src", "")).path).stem
                    fallback = re.sub(r"[-_]+", " ", filename).strip().capitalize()
                    element.set("alt", fallback or "Post-mortem evidence image")
                element.set("decoding", "async")
                element.set("loading", "eager" if self.image_number == 1 else "lazy")
        return root


class RepositoryLinkExtension(Extension):
    def extendMarkdown(self, md: markdown.Markdown) -> None:  # noqa: N802
        # Run after inline parsing and the TOC processor.
        md.treeprocessors.register(
            RepositoryLinkTreeprocessor(md), "repository_links", 0
        )


class VisibleTextParser(HTMLParser):
    """Small, dependency-free HTML probe used for deterministic validation."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text_parts: list[str] = []
        self.links: list[str] = []
        self.images: list[tuple[str, str]] = []
        self.json_ld_parts: list[str] = []
        self._in_json_ld = False
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        elif tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"] or "")
        elif tag == "img":
            self.images.append((attributes.get("src") or "", attributes.get("alt") or ""))
        elif tag == "script" and attributes.get("type") == "application/ld+json":
            self._in_json_ld = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._in_json_ld:
            self._in_json_ld = False

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self.json_ld_parts.append(data)
        else:
            self.text_parts.append(data)

    @property
    def visible_text(self) -> str:
        return " ".join(" ".join(self.text_parts).split())


def render_markdown(source_text: str) -> tuple[str, str]:
    # GitHub renders Markdown nested in details elements. Python-Markdown requires
    # the opt-in attribute; it is added only to the build input and never to source.
    build_input = source_text.replace("<details>", '<details markdown="1">')
    renderer = markdown.Markdown(
        extensions=[
            FootnoteExtension(BACKLINK_TEXT="↩"),
            TocExtension(toc_depth="2-3", title=""),
            "md_in_html",
            "sane_lists",
            RepositoryLinkExtension(),
        ],
        output_format="html5",
    )
    article_html = renderer.convert(build_input)
    toc_html = renderer.toc
    return article_html, toc_html


def insert_edition_header(article_html: str, revision: str, source_sha256: str) -> str:
    marker = "</h1>"
    position = article_html.find(marker)
    if position < 0:
        fail("The rendered essay does not contain its expected h1 heading.")
    position += len(marker)
    exact_source_url = f"{REPOSITORY_URL}/blob/{revision}/{SOURCE.name}"
    header = f"""
<div class="edition-metadata" aria-label="Publication metadata">
  <dl>
    <div><dt>Author</dt><dd><a rel="author" href="{AUTHOR_URL}">{html.escape(AUTHOR)}</a></dd></div>
    <div><dt>Published</dt><dd><time datetime="{PUBLICATION_DATE}">{PUBLICATION_DATE}</time></dd></div>
    <div><dt>Edition</dt><dd>Version {VERSION}</dd></div>
    <div><dt>Source revision</dt><dd><a href="{exact_source_url}"><code>{revision}</code></a></dd></div>
  </dl>
</div>
<section class="abstract" aria-labelledby="abstract-heading">
  <h2 id="abstract-heading">Abstract</h2>
  <p>{html.escape(ABSTRACT)}</p>
  <p class="source-hash"><span>Source SHA-256</span> <code>{source_sha256}</code></p>
</section>"""
    return article_html[:position] + header + article_html[position:]


def article_json_ld(revision: str, source_sha256: str, section_names: list[str]) -> dict:
    markdown_url = pinned_file_url(SOURCE.name)
    pdf_url = pinned_file_url("output/pdf/POST_MORTEM.pdf", raw=True)
    return {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "abstract": ABSTRACT,
        "alternativeHeadline": SUBTITLE,
        "articleSection": section_names,
        "associatedMedia": [
            {
                "@type": "MediaObject",
                "contentUrl": markdown_url,
                "encodingFormat": "text/markdown",
                "name": "Markdown source",
            },
            {
                "@type": "MediaObject",
                "contentUrl": pdf_url,
                "encodingFormat": "application/pdf",
                "name": "Illustrated PDF edition",
            },
        ],
        "author": {"@type": "Person", "name": AUTHOR, "url": AUTHOR_URL},
        "dateModified": PUBLICATION_DATE,
        "datePublished": PUBLICATION_DATE,
        "description": ABSTRACT,
        "headline": TITLE,
        "identifier": [
            {"@type": "PropertyValue", "name": "Version", "value": VERSION},
            {
                "@type": "PropertyValue",
                "name": "Git commit",
                "value": revision,
            },
            {
                "@type": "PropertyValue",
                "name": "Source SHA-256",
                "value": source_sha256,
            },
        ],
        "image": pinned_file_url(
            "sources/screenshots/government-sentencing-memo-page-38.png", raw=True
        ),
        "inLanguage": "en",
        "isAccessibleForFree": True,
        "isPartOf": {
            "@type": "ArchiveComponent",
            "name": "Scamourai Wallet evidence archive",
            "url": REPOSITORY_URL,
        },
        "keywords": KEYWORDS,
        "mainEntityOfPage": {"@id": CANONICAL_URL, "@type": "WebPage"},
        "url": CANONICAL_URL,
        "version": VERSION,
    }


def page_html(
    article_html: str,
    toc_html: str,
    json_ld: dict,
    revision: str,
    source_sha256: str,
) -> str:
    description = html.escape(ABSTRACT, quote=True)
    title = html.escape(TITLE)
    markdown_url = pinned_file_url(SOURCE.name)
    pdf_url = pinned_file_url("output/pdf/POST_MORTEM.pdf", raw=True)
    image_url = pinned_file_url(
        "sources/screenshots/government-sentencing-memo-page-38.png", raw=True
    )
    claims_url = pinned_file_url("CLAIMS.jsonl")
    timeline_url = pinned_file_url("TIMELINE.md")
    evidence_manifest_url = pinned_file_url("EVIDENCE_MANIFEST.json")
    citation_url = pinned_file_url("CITATION.cff")
    revision_url = f"{REPOSITORY_URL}/commit/{revision}"
    json_ld_text = json.dumps(json_ld, ensure_ascii=False, sort_keys=True, indent=2)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}">
  <meta name="author" content="{html.escape(AUTHOR, quote=True)}">
  <meta property="article:published_time" content="{PUBLICATION_DATE}">
  <meta property="article:modified_time" content="{PUBLICATION_DATE}">
  <meta name="citation_title" content="{html.escape(TITLE, quote=True)}">
  <meta name="citation_author" content="{html.escape(AUTHOR, quote=True)}">
  <meta name="citation_publication_date" content="{PUBLICATION_DATE}">
  <meta name="citation_pdf_url" content="{pdf_url}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{html.escape(TITLE, quote=True)}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{CANONICAL_URL}">
  <meta property="og:site_name" content="Scamourai Wallet evidence archive">
  <meta property="og:image" content="{image_url}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(TITLE, quote=True)}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{image_url}">
  <title>{title} — {html.escape(AUTHOR)}</title>
  <link rel="canonical" href="{CANONICAL_URL}">
  <link rel="alternate" type="text/markdown" title="Markdown source" href="{markdown_url}">
  <link rel="alternate" type="application/pdf" title="Illustrated PDF edition" href="{pdf_url}">
  <link rel="alternate" type="application/ld+json" title="Publication metadata" href="metadata.json">
  <link rel="stylesheet" href="assets/site.css">
  <script type="application/ld+json">
{json_ld_text}
  </script>
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to the article</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="archive-name" href="{CANONICAL_URL}" aria-label="Scamourai Wallet evidence archive home">
        <span class="archive-mark" aria-hidden="true">SW</span>
        <span>Evidence archive</span>
      </a>
      <nav class="edition-links" aria-label="Edition links">
        <a href="{markdown_url}">Markdown</a>
        <a href="{pdf_url}">PDF</a>
        <a href="{REPOSITORY_URL}">Repository</a>
        <a href="metadata.json">Metadata</a>
      </nav>
    </div>
  </header>

  <div class="page-grid">
    <aside class="table-of-contents">
      <details open>
        <summary>On this page</summary>
        <nav aria-label="Essay sections">
          {toc_html}
        </nav>
      </details>
    </aside>

    <main id="main-content">
      <article class="essay" itemscope itemtype="https://schema.org/ScholarlyArticle">
        {article_html}
      </article>

      <footer class="publication-footer">
        <p>This is the canonical HTML edition of version {VERSION}, published {PUBLICATION_DATE}.</p>
        <p>Built from <a href="{revision_url}"><code>{revision}</code></a>; source SHA-256 <code>{source_sha256}</code>.</p>
        <nav aria-label="Archive resources">
          <a href="{markdown_url}">Read the Markdown</a>
          <a href="{pdf_url}">Open the PDF</a>
          <a href="{claims_url}">Query the claims index</a>
          <a href="{timeline_url}">Read the timeline</a>
          <a href="{evidence_manifest_url}">Verify the evidence manifest</a>
          <a href="{citation_url}">Cite this report</a>
          <a href="{REPOSITORY_URL}">Browse the evidence archive</a>
        </nav>
      </footer>
    </main>
  </div>
</body>
</html>
"""


SITE_CSS: Final = """/* Deterministic static edition: no webfonts, scripts, or remote CSS. */
:root {
  color-scheme: light;
  --paper: #fbfaf7;
  --surface: #ffffff;
  --ink: #191d21;
  --muted: #5a626a;
  --line: #d9d7d0;
  --accent: #9a3412;
  --accent-dark: #6f250e;
  --accent-soft: #fff1e8;
  --code: #f1efe9;
  --measure: 48rem;
  --shadow: 0 12px 34px rgb(23 30 36 / 8%);
}

* { box-sizing: border-box; }

html {
  scroll-behavior: smooth;
  scroll-padding-top: 5.5rem;
}

body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: Charter, "Bitstream Charter", "Sitka Text", Cambria, Georgia, serif;
  font-size: 1.075rem;
  line-height: 1.72;
  text-rendering: optimizeLegibility;
}

a {
  color: var(--accent-dark);
  text-decoration-color: color-mix(in srgb, var(--accent) 48%, transparent);
  text-decoration-thickness: .08em;
  text-underline-offset: .16em;
}

a:hover { color: var(--accent); }

a:focus-visible,
summary:focus-visible {
  border-radius: .18rem;
  outline: .18rem solid #2563eb;
  outline-offset: .18rem;
}

.skip-link {
  position: fixed;
  z-index: 20;
  top: .5rem;
  left: .5rem;
  padding: .55rem .8rem;
  transform: translateY(-160%);
  background: var(--ink);
  color: #fff;
  font: 700 .9rem/1.2 system-ui, sans-serif;
}

.skip-link:focus { transform: none; }

.site-header {
  position: sticky;
  z-index: 10;
  top: 0;
  border-bottom: 1px solid var(--line);
  background: rgb(251 250 247 / 95%);
  backdrop-filter: blur(12px);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: min(90rem, calc(100% - 2rem));
  min-height: 4rem;
  margin: 0 auto;
  gap: 1.25rem;
}

.archive-name,
.edition-links {
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
}

.archive-name {
  display: inline-flex;
  align-items: center;
  gap: .65rem;
  color: var(--ink);
  font-size: .9rem;
  font-weight: 750;
  letter-spacing: .035em;
  text-decoration: none;
  text-transform: uppercase;
}

.archive-mark {
  display: grid;
  width: 2rem;
  height: 2rem;
  place-items: center;
  border-radius: .35rem;
  background: var(--ink);
  color: #fff;
  font-size: .7rem;
  letter-spacing: .08em;
}

.edition-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: .3rem .9rem;
  font-size: .84rem;
  font-weight: 650;
}

.edition-links a { text-decoration: none; }

.page-grid {
  display: grid;
  grid-template-columns: minmax(13rem, 17rem) minmax(0, var(--measure));
  justify-content: center;
  align-items: start;
  gap: clamp(2rem, 5vw, 5rem);
  width: min(90rem, calc(100% - 2rem));
  margin: 0 auto;
  padding: clamp(2.4rem, 6vw, 5.5rem) 0 5rem;
}

.table-of-contents {
  position: sticky;
  top: 6rem;
  max-height: calc(100vh - 7.5rem);
  overflow: auto;
  border-left: .2rem solid var(--accent);
  padding-left: 1rem;
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  font-size: .79rem;
  line-height: 1.42;
}

.table-of-contents summary {
  cursor: pointer;
  color: var(--ink);
  font-weight: 800;
  letter-spacing: .05em;
  text-transform: uppercase;
}

.table-of-contents .toc > ul {
  margin: .9rem 0 0;
  padding: 0;
  list-style: none;
}

.table-of-contents li { margin: 0 0 .6rem; }
.table-of-contents li li { margin: .4rem 0 0; }
.table-of-contents ul ul { padding-left: .8rem; }
.table-of-contents a { text-decoration: none; }

main { min-width: 0; }

.essay {
  width: 100%;
  padding: clamp(1.5rem, 4vw, 4.5rem);
  border: 1px solid var(--line);
  border-radius: .35rem;
  background: var(--surface);
  box-shadow: var(--shadow);
}

.essay > h1 {
  max-width: 15ch;
  margin: 0 0 1rem;
  font-size: clamp(2.45rem, 7vw, 4.8rem);
  font-weight: 760;
  letter-spacing: -.045em;
  line-height: .98;
  text-wrap: balance;
}

.essay > h1 + .edition-metadata { margin-top: 2rem; }

.edition-metadata {
  margin-bottom: 2rem;
  padding: 1rem 0;
  border-block: 1px solid var(--line);
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
}

.edition-metadata dl {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  margin: 0;
  gap: .9rem 1.5rem;
}

.edition-metadata dl > div { min-width: 0; }

.edition-metadata dt {
  color: var(--muted);
  font-size: .69rem;
  font-weight: 750;
  letter-spacing: .07em;
  text-transform: uppercase;
}

.edition-metadata dd {
  margin: .15rem 0 0;
  font-size: .82rem;
  font-weight: 600;
}

.edition-metadata code {
  display: inline-block;
  max-width: 100%;
  overflow-wrap: anywhere;
}

.abstract {
  margin: 2rem 0 2.5rem;
  padding: 1.15rem 1.35rem 1.25rem;
  border-left: .28rem solid var(--accent);
  background: var(--accent-soft);
}

.abstract h2 {
  margin: 0 0 .45rem;
  font: 800 .72rem/1.3 Inter, ui-sans-serif, system-ui, sans-serif;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.abstract p { margin: 0; }

.source-hash {
  margin-top: .75rem !important;
  color: var(--muted);
  font: .7rem/1.45 ui-monospace, SFMono-Regular, Consolas, monospace;
  overflow-wrap: anywhere;
}

.source-hash span { font-weight: 800; }

.essay > p:nth-of-type(1) {
  color: #343b42;
  font-size: 1.22rem;
  line-height: 1.55;
}

h2,
h3 {
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  line-height: 1.18;
  text-wrap: balance;
}

.essay h2 {
  margin: 3.8rem 0 1.15rem;
  padding-top: .4rem;
  font-size: clamp(1.65rem, 4vw, 2.2rem);
  letter-spacing: -.025em;
}

.essay h3 { margin-top: 2.4rem; font-size: 1.3rem; }

.essay p,
.essay li { hanging-punctuation: first last; }

.essay blockquote {
  margin: 1.8rem 0;
  padding: .2rem 0 .2rem 1.2rem;
  border-left: .22rem solid var(--line);
  color: #394149;
}

.essay img {
  display: block;
  width: auto;
  max-width: 100%;
  height: auto;
  margin: 2.2rem auto .65rem;
  border: 1px solid #c8c6bf;
  border-radius: .2rem;
  background: #f4f3ef;
}

.essay p:has(> img) {
  margin-bottom: 0;
  break-inside: avoid;
}

.essay p:has(> img) + p {
  margin-top: .55rem;
  color: var(--muted);
  font-size: .88rem;
  line-height: 1.5;
}

.essay code,
.publication-footer code {
  padding: .08em .3em;
  border-radius: .2rem;
  background: var(--code);
  font: .83em/1.55 ui-monospace, SFMono-Regular, Consolas, monospace;
  overflow-wrap: anywhere;
}

.essay pre {
  max-width: 100%;
  overflow: auto;
  padding: 1rem;
  border: 1px solid var(--line);
  background: var(--code);
  font-size: .85rem;
}

.essay details {
  margin: 1.7rem 0;
  padding: .8rem 1rem;
  border: 1px solid var(--line);
  border-radius: .25rem;
  background: #fcfbf8;
}

.essay summary {
  cursor: pointer;
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
}

.footnote {
  margin-top: 4rem;
  padding-top: 1rem;
  border-top: .18rem solid var(--ink);
  color: #30373e;
  font-size: .84rem;
  line-height: 1.55;
}

.footnote ol { padding-left: 1.35rem; }
.footnote li { margin-bottom: .85rem; }
.footnote-backref { margin-left: .25rem; text-decoration: none; }

.publication-footer {
  margin-top: 2rem;
  padding: 1.5rem;
  border: 1px solid var(--line);
  color: var(--muted);
  font: .82rem/1.55 Inter, ui-sans-serif, system-ui, sans-serif;
}

.publication-footer p { margin: 0 0 .5rem; }
.publication-footer nav { display: flex; flex-wrap: wrap; gap: .45rem 1rem; margin-top: .9rem; }
.publication-footer nav a { font-weight: 700; text-decoration: none; }

@media (max-width: 62rem) {
  .page-grid {
    grid-template-columns: minmax(0, var(--measure));
    gap: 1.4rem;
  }

  .table-of-contents {
    position: static;
    max-height: none;
    padding: .8rem 1rem;
    border: 1px solid var(--line);
    background: var(--surface);
  }

  .table-of-contents .toc > ul { columns: 2 15rem; column-gap: 2rem; }
  .table-of-contents li { break-inside: avoid; }
}

@media (max-width: 40rem) {
  body { font-size: 1rem; }
  .header-inner { align-items: flex-start; flex-direction: column; padding: .75rem 0; }
  .edition-links { justify-content: flex-start; }
  .page-grid { width: min(100% - 1rem, var(--measure)); padding-top: 1rem; }
  .essay { padding: 1.2rem; border-radius: 0; }
  .edition-metadata dl { grid-template-columns: 1fr; }
  .table-of-contents .toc > ul { columns: auto; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
}

@media print {
  @page { size: A4; margin: 18mm 16mm; }

  :root {
    --paper: #fff;
    --surface: #fff;
    --ink: #000;
    --muted: #333;
    --line: #aaa;
    --accent: #000;
    --accent-dark: #000;
    --accent-soft: #fff;
    --code: #eee;
  }

  html { font-size: 10.5pt; }
  body { background: #fff; line-height: 1.5; }
  .site-header, .skip-link, .table-of-contents, .publication-footer nav { display: none; }
  .page-grid { display: block; width: auto; margin: 0; padding: 0; }
  .essay { width: auto; padding: 0; border: 0; box-shadow: none; }
  .essay > h1 { max-width: none; font-size: 28pt; }
  .essay h2 { break-after: avoid; margin-top: 2rem; }
  .essay img { max-height: 21cm; break-inside: avoid; }
  .essay a { color: #000; text-decoration: underline; }
  .publication-footer { break-inside: avoid; }
  details { break-inside: avoid; }
  details:not([open]) > *:not(summary) { display: block; }
}
"""


def section_names_from_source(source_text: str) -> list[str]:
    return [
        match.group(1).strip()
        for match in re.finditer(r"^##\s+(.+?)\s*$", source_text, flags=re.MULTILINE)
    ]


def metadata_json(json_ld: dict, revision: str, source_sha256: str) -> str:
    metadata = {
        "@context": "https://schema.org",
        "article": json_ld,
        "build": {
            "generator": "tools/build_site.py",
            "markdownRenderer": f"Python-Markdown {EXPECTED_MARKDOWN_VERSION}",
            "sourceCommit": revision,
            "sourcePath": SOURCE.name,
            "sourceSha256": source_sha256,
        },
        "canonicalUrl": CANONICAL_URL,
        "formats": {
            "html": CANONICAL_URL,
            "markdown": pinned_file_url(SOURCE.name),
            "pdf": pinned_file_url("output/pdf/POST_MORTEM.pdf", raw=True),
            "repository": REPOSITORY_URL,
        },
        "publicationDate": PUBLICATION_DATE,
        "version": VERSION,
    }
    return json.dumps(metadata, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def sitemap_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{CANONICAL_URL}</loc>
    <lastmod>{PUBLICATION_DATE}</lastmod>
  </url>
  <url>
    <loc>{CANONICAL_URL}metadata.json</loc>
    <lastmod>{PUBLICATION_DATE}</lastmod>
  </url>
</urlset>
"""


def robots_txt() -> str:
    return f"""User-agent: *
Allow: /

Sitemap: {CANONICAL_URL}sitemap.xml
"""


def validate(
    complete_page: str,
    rendered_article: str,
    json_ld: dict,
    source_text: str,
    revision: str,
) -> None:
    page_probe = VisibleTextParser()
    page_probe.feed(complete_page)
    if page_probe.h1_count != 1:
        fail(f"Expected one h1 in generated page; found {page_probe.h1_count}.")
    if TITLE not in page_probe.visible_text:
        fail("Generated page is missing the essay title.")
    if ABSTRACT not in page_probe.visible_text:
        fail("Generated page is missing the abstract.")
    if not page_probe.json_ld_parts:
        fail("Generated page is missing Article JSON-LD.")
    parsed_json_ld = json.loads("".join(page_probe.json_ld_parts))
    if parsed_json_ld != json_ld:
        fail("Embedded JSON-LD does not match the generated metadata.")

    # Edition metadata is inserted immediately after the source h1. Everything on
    # either side of that insertion must otherwise be present byte-for-byte, which
    # is stronger than sampling prose from a 90,000-character source document.
    h1_end = rendered_article.find("</h1>") + len("</h1>")
    if h1_end < len("</h1>"):
        fail("Rendered essay has no closing h1.")
    if rendered_article[:h1_end] not in complete_page:
        fail("Generated page omitted content at the beginning of the essay.")
    if rendered_article[h1_end:] not in complete_page:
        fail("Generated page omitted content after the essay title.")

    source_headings = section_names_from_source(source_text)
    missing_headings = [heading for heading in source_headings if heading not in page_probe.visible_text]
    if missing_headings:
        fail(f"Generated page is missing essay headings: {missing_headings}")

    for src, alt in page_probe.images:
        if not alt.strip():
            fail(f"Generated image is missing alternative text: {src}")
        if src.startswith(("sources/", "../", "./")):
            fail(f"Generated image retains a broken relative source: {src}")

    bad_relative_links = [
        link
        for link in page_probe.links
        if link
        and not link.startswith(("http://", "https://", "#", "mailto:"))
        and link not in {"metadata.json", "assets/site.css"}
    ]
    if bad_relative_links:
        fail(f"Generated page retains unexpected relative links: {bad_relative_links[:5]}")

    if json_ld.get("@type") not in {"Article", "ScholarlyArticle"}:
        fail("JSON-LD is not an Article or ScholarlyArticle.")
    if json_ld.get("url") != CANONICAL_URL:
        fail("JSON-LD canonical URL is incorrect.")
    if revision not in complete_page:
        fail("Generated page does not identify its exact source revision.")


def expected_outputs() -> dict[Path, bytes]:
    if markdown.__version__ != EXPECTED_MARKDOWN_VERSION:
        fail(
            f"Python-Markdown {EXPECTED_MARKDOWN_VERSION} is required for deterministic "
            f"output; found {markdown.__version__}. Install tools/requirements-site.txt."
        )
    if not SOURCE.is_file():
        fail(f"Missing source document: {SOURCE}")

    source_bytes = SOURCE.read_bytes()
    try:
        source_text = source_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        fail(f"POST_MORTEM.md must be UTF-8: {error}")
    source_text = source_text.replace("\r\n", "\n").replace("\r", "\n")
    source_sha256 = hashlib.sha256(source_text.encode("utf-8")).hexdigest()
    revision = source_revision()
    rendered_article, toc_html = render_markdown(source_text)

    if f"<h1 id=\"post-mortem-what-happened-between-samourai-wallet-and-me\">{TITLE}</h1>" not in rendered_article:
        fail("The source title changed; update publication metadata deliberately.")

    article_with_header = insert_edition_header(rendered_article, revision, source_sha256)
    json_ld = article_json_ld(
        revision, source_sha256, section_names_from_source(source_text)
    )
    complete_page = page_html(
        article_with_header, toc_html, json_ld, revision, source_sha256
    )
    validate(complete_page, rendered_article, json_ld, source_text, revision)

    outputs = {
        DOCS / "index.html": complete_page.encode("utf-8"),
        DOCS / "assets" / "site.css": SITE_CSS.encode("utf-8"),
        DOCS / "metadata.json": metadata_json(json_ld, revision, source_sha256).encode("utf-8"),
        DOCS / "sitemap.xml": sitemap_xml().encode("utf-8"),
        DOCS / "robots.txt": robots_txt().encode("utf-8"),
        DOCS / ".nojekyll": b"",
    }
    return outputs


def check_outputs(outputs: dict[Path, bytes]) -> int:
    stale: list[Path] = []
    for path, expected in outputs.items():
        if not path.is_file() or path.read_bytes() != expected:
            stale.append(path.relative_to(ROOT))
    if stale:
        print("Generated site is stale or incomplete:", file=sys.stderr)
        for path in stale:
            print(f"  {path.as_posix()}", file=sys.stderr)
        print("Run: python tools/build_site.py", file=sys.stderr)
        return 1
    print(f"Site check passed ({len(outputs)} generated files are current).")
    return 0


def write_outputs(outputs: dict[Path, bytes]) -> None:
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_file() and path.read_bytes() == content:
            continue
        path.write_bytes(content)
    print(f"Built {len(outputs)} static site files in {DOCS.relative_to(ROOT).as_posix()}/.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit nonzero if generated docs files are missing or stale; write nothing.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    outputs = expected_outputs()
    if args.check:
        return check_outputs(outputs)
    write_outputs(outputs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

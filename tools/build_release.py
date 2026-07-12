#!/usr/bin/env python3
"""Build a reproducible archival release from the current Git commit.

The normal mode refuses a dirty worktree and archives the exact ``HEAD`` commit.
``--development`` exists only to exercise the package before the edition is
committed; its COMMIT.txt carries an explicit dirty-snapshot warning.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, time, timezone
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_MARKER = ".release-build-output"
REPOSITORY_URL = "https://github.com/nopara73/ScamouraiWallet"
TAG_PREFIX = "post-mortem-v"

PUBLICATION_FILES = {
    "POST_MORTEM.md": "publication/POST_MORTEM.md",
    "output/pdf/POST_MORTEM.pdf": "publication/POST_MORTEM.pdf",
}
SUPPORTING_FILES = {
    "README.md": "README.md",
    "LICENSE": "LICENSE",
    "CITATION.cff": "metadata/CITATION.cff",
    ".zenodo.json": "metadata/zenodo-metadata.json",
    "BIBLIOGRAPHY.txt": "metadata/BIBLIOGRAPHY.txt",
    "RELEASE.md": "metadata/RELEASE.md",
    "timestamps/ARCHIVE_SHA256SUMS": "timestamps/ARCHIVE_SHA256SUMS",
    "timestamps/README.md": "timestamps/README.md",
}
INDEX_FILES = (
    "CLAIMS.jsonl",
    "TIMELINE.md",
    "ENTITY_ALIASES.json",
    "EVIDENCE_MANIFEST.json",
    "METHODOLOGY.md",
    "CORRECTIONS.md",
)


def fail(message: str) -> "NoReturn":
    raise SystemExit(message)


def git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip()


def git_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout


def load_metadata() -> tuple[str, date]:
    zenodo_path = ROOT / ".zenodo.json"
    cff_path = ROOT / "CITATION.cff"
    try:
        zenodo = json.loads(zenodo_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read .zenodo.json: {exc}")

    version = str(zenodo.get("version", "")).strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        fail(".zenodo.json must contain a semantic version such as 1.0.0")
    try:
        released = date.fromisoformat(str(zenodo["publication_date"]))
    except (KeyError, TypeError, ValueError) as exc:
        fail(f".zenodo.json has an invalid publication_date: {exc}")

    try:
        cff = cff_path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"Cannot read CITATION.cff: {exc}")
    cff_version = re.search(r"(?m)^version:\s*['\"]?([^'\"\s]+)", cff)
    cff_date = re.search(r"(?m)^date-released:\s*['\"]?([^'\"\s]+)", cff)
    if not cff_version or cff_version.group(1) != version:
        fail("CITATION.cff and .zenodo.json versions do not agree")
    if not cff_date or cff_date.group(1) != released.isoformat():
        fail("CITATION.cff and .zenodo.json release dates do not agree")
    if zenodo.get("upload_type") != "publication" or zenodo.get("publication_type") != "report":
        fail(".zenodo.json must identify this edition as publication/report")
    return version, released


def is_generated_output(path: Path) -> bool:
    """Return true when path is inside a prior marked release output."""

    candidate = path if path.is_dir() else path.parent
    while candidate != ROOT and candidate.is_relative_to(ROOT):
        if (candidate / OUTPUT_MARKER).is_file():
            return True
        candidate = candidate.parent
    return False


def dirty_entries() -> list[str]:
    raw = git_bytes("status", "--porcelain=v1", "-z", "--untracked-files=all")
    entries: list[str] = []
    fields = raw.decode("utf-8", errors="surrogateescape").split("\0")
    index = 0
    while index < len(fields):
        field = fields[index]
        index += 1
        if not field:
            continue
        status_code = field[:2]
        path_text = field[3:]
        paths = [path_text]
        if "R" in status_code or "C" in status_code:
            if index < len(fields) and fields[index]:
                paths.append(fields[index])
                index += 1
        visible = False
        for item in paths:
            candidate = (ROOT / item).resolve()
            if not is_generated_output(candidate):
                visible = True
                break
        if visible:
            entries.append(f"{status_code} {path_text}")
    return entries


def prepare_output(output: Path) -> tuple[Path, Path]:
    output = output.resolve()
    if output == ROOT or not output.is_relative_to(ROOT):
        fail("--output must name a directory below the repository root")
    if output.exists():
        marker = output / OUTPUT_MARKER
        if any(output.iterdir()) and not marker.is_file():
            fail(f"Refusing to replace unmarked non-empty directory: {output}")
        shutil.rmtree(output)
    upload = output / "upload"
    upload.mkdir(parents=True)
    (output / OUTPUT_MARKER).write_text(
        "Generated by tools/build_release.py; safe for that tool to replace.\n",
        encoding="utf-8",
        newline="\n",
    )
    return output, upload


def normalized_mode(path: Path) -> int:
    try:
        mode = stat.S_IMODE(path.stat().st_mode)
    except OSError:
        return 0o644
    return 0o755 if mode & 0o111 else 0o644


def development_files(output: Path) -> list[Path]:
    raw = git_bytes("ls-files", "-z", "--cached", "--others", "--exclude-standard")
    files: list[Path] = []
    ignored_roots = {".git", "tmp", ".pytest_cache", "__pycache__"}
    for value in raw.decode("utf-8", errors="surrogateescape").split("\0"):
        if not value:
            continue
        relative = Path(value)
        source = (ROOT / relative).resolve()
        if relative.parts and relative.parts[0] in ignored_roots:
            continue
        if "__pycache__" in relative.parts or source.is_relative_to(output):
            continue
        if is_generated_output(source) or not source.is_file():
            continue
        files.append(relative)
    return sorted(set(files), key=lambda path: path.as_posix().encode("utf-8"))


def worktree_signature(output: Path) -> tuple[tuple[str, int, int], ...]:
    """Cheaply detect files added, removed, or rewritten during a dev build."""

    signature: list[tuple[str, int, int]] = []
    for relative in development_files(output):
        details = (ROOT / relative).stat()
        signature.append((relative.as_posix(), details.st_size, details.st_mtime_ns))
    return tuple(signature)


def gzip_stream(source: io.BufferedReader, destination: Path) -> None:
    with destination.open("wb") as target:
        with gzip.GzipFile(filename="", mode="wb", fileobj=target, compresslevel=9, mtime=0) as zipped:
            shutil.copyfileobj(source, zipped, length=1024 * 1024)


def build_committed_source_archive(destination: Path, prefix: str, commit: str) -> None:
    process = subprocess.Popen(
        ["git", "archive", "--format=tar", f"--prefix={prefix}/", commit],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdout is not None
    gzip_stream(process.stdout, destination)
    stderr = process.stderr.read() if process.stderr is not None else b""
    return_code = process.wait()
    if return_code:
        destination.unlink(missing_ok=True)
        fail(f"git archive failed: {stderr.decode('utf-8', errors='replace')}")


def build_development_source_archive(
    destination: Path,
    prefix: str,
    released: date,
    output: Path,
) -> None:
    epoch = int(datetime.combine(released, time.min, timezone.utc).timestamp())
    files = development_files(output)
    with tempfile.NamedTemporaryFile(dir=output, suffix=".tar", delete=False) as temporary:
        temporary_path = Path(temporary.name)
    try:
        with tarfile.open(temporary_path, mode="w", format=tarfile.GNU_FORMAT) as archive:
            for relative in files:
                source = ROOT / relative
                data = source.read_bytes()
                info = tarfile.TarInfo(f"{prefix}/{relative.as_posix()}")
                info.size = len(data)
                info.mtime = epoch
                info.mode = normalized_mode(source)
                info.uid = 0
                info.gid = 0
                info.uname = ""
                info.gname = ""
                archive.addfile(info, io.BytesIO(data))
        with temporary_path.open("rb") as source:
            gzip_stream(source, destination)
    finally:
        temporary_path.unlink(missing_ok=True)


def build_git_bundle(destination: Path) -> None:
    result = subprocess.run(
        ["git", "bundle", "create", str(destination), "--all"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    if result.returncode:
        destination.unlink(missing_ok=True)
        fail(f"git bundle create --all failed: {result.stderr.strip()}")
    verify = subprocess.run(
        ["git", "bundle", "verify", str(destination)],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
    )
    if verify.returncode:
        fail(f"git bundle verification failed:\n{verify.stdout}")


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def copy_or_link(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(source, destination)
    except OSError:
        shutil.copyfile(source, destination)


def committed_timestamp_proofs(development: bool) -> list[Path]:
    args = ["ls-files", "-z"]
    if development:
        args.extend(["--cached", "--others", "--exclude-standard"])
    args.extend(["--", "*.ots", "**/*.ots"])
    raw = git_bytes(*args)
    proofs: list[Path] = []
    for value in raw.decode("utf-8", errors="surrogateescape").split("\0"):
        if not value:
            continue
        relative = Path(value)
        source = ROOT / relative
        if source.is_file() and not is_generated_output(source.resolve()):
            proofs.append(relative)
    return sorted(set(proofs), key=lambda path: path.as_posix().encode("utf-8"))


def timestamp_destination(relative: Path) -> Path:
    """Keep an existing timestamps/ layout without nesting it twice."""

    if relative.parts and relative.parts[0] == "timestamps":
        return Path(*relative.parts[1:])
    return relative


def timestamp_upload_name(relative: Path) -> Path:
    """Flatten a proof path into a unique GitHub Release asset name."""

    destination = timestamp_destination(relative)
    return Path("-".join(destination.parts))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_manifest(directory: Path, destination: Path) -> None:
    entries: list[str] = []
    for path in sorted(directory.rglob("*"), key=lambda value: value.relative_to(directory).as_posix()):
        if not path.is_file() or path == destination:
            continue
        relative = path.relative_to(directory).as_posix()
        entries.append(f"{sha256(path)}  {relative}")
    destination.write_text("\n".join(entries) + "\n", encoding="utf-8", newline="\n")


def deterministic_zip(source: Path, destination: Path, released: date) -> None:
    stamp = (released.year, released.month, released.day, 0, 0, 0)
    with zipfile.ZipFile(destination, mode="w", compression=zipfile.ZIP_STORED) as archive:
        for path in sorted(source.rglob("*"), key=lambda value: value.relative_to(source).as_posix()):
            if not path.is_file():
                continue
            relative = PurePosixPath(source.name) / path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(relative.as_posix(), date_time=stamp)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = ((stat.S_IFREG | normalized_mode(path)) & 0xFFFF) << 16
            info.flag_bits |= 0x800
            with path.open("rb") as stream, archive.open(info, mode="w") as target:
                shutil.copyfileobj(stream, target, length=1024 * 1024)


def build(args: argparse.Namespace) -> None:
    if git_text("rev-parse", "--show-toplevel").replace("\\", "/") != ROOT.as_posix():
        fail("tools/build_release.py must be located inside the repository it packages")

    version, released = load_metadata()
    expected_tag = f"{TAG_PREFIX}{version}"
    tag = args.tag or expected_tag
    if tag != expected_tag:
        fail(f"Tag must be {expected_tag} for metadata version {version}")

    commit = git_text("rev-parse", "HEAD")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        fail("Git did not return a full 40-character HEAD commit identifier")

    changes = dirty_entries()
    if changes and not args.development:
        preview = "\n".join(f"  {entry}" for entry in changes[:20])
        fail(f"Refusing to build a release from a dirty worktree:\n{preview}")

    tag_commit = subprocess.run(
        ["git", "rev-parse", "-q", "--verify", f"refs/tags/{tag}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="utf-8",
    )
    if tag_commit.returncode == 0 and tag_commit.stdout.strip() != commit:
        fail(f"Existing tag {tag} does not point at HEAD {commit}")

    missing = [path for path in (*PUBLICATION_FILES, *SUPPORTING_FILES) if not (ROOT / path).is_file()]
    missing_indexes = [path for path in INDEX_FILES if not (ROOT / path).is_file()]
    if not (ROOT / "docs/index.html").is_file() and not args.development:
        missing.append("docs/index.html")
    if missing_indexes and not args.development:
        missing.extend(missing_indexes)
    if missing:
        fail("Required release inputs are missing:\n  " + "\n  ".join(missing))

    requested_output = (ROOT / args.output).resolve()
    starting_signature = worktree_signature(requested_output) if args.development else None
    output, upload = prepare_output(requested_output)
    bundle_name = f"ScamouraiWallet-post-mortem-v{version}"
    source_name = f"ScamouraiWallet-source-v{version}"
    bundle_directory = output / bundle_name
    bundle_directory.mkdir()

    tree_state = "dirty development snapshot" if changes or args.development else "clean committed tree"
    commit_text = (
        f"repository: {REPOSITORY_URL}\n"
        f"version: {version}\n"
        f"tag: {tag}\n"
        f"commit: {commit}\n"
        f"tree-state: {tree_state}\n"
    )
    if args.development:
        commit_text += "warning: DEVELOPMENT BUILD; DO NOT PUBLISH AS AN IMMUTABLE RELEASE\n"
    commit_path = bundle_directory / "COMMIT.txt"
    commit_path.write_text(commit_text, encoding="utf-8", newline="\n")

    for source_name_relative, destination_relative in PUBLICATION_FILES.items():
        copy_file(ROOT / source_name_relative, bundle_directory / destination_relative)
    for source_name_relative, destination_relative in SUPPORTING_FILES.items():
        copy_file(ROOT / source_name_relative, bundle_directory / destination_relative)
    for name in INDEX_FILES:
        if (ROOT / name).is_file():
            copy_file(ROOT / name, bundle_directory / "indexes" / name)

    docs = ROOT / "docs"
    if docs.is_dir():
        shutil.copytree(docs, bundle_directory / "site", copy_function=shutil.copyfile)

    proofs = committed_timestamp_proofs(args.development)
    for relative in proofs:
        copy_file(
            ROOT / relative,
            bundle_directory / "timestamps" / timestamp_destination(relative),
        )

    source_archive = upload / f"{source_name}.tar.gz"
    if args.development:
        build_development_source_archive(source_archive, source_name, released, output)
    else:
        build_committed_source_archive(source_archive, source_name, commit)
    copy_or_link(source_archive, bundle_directory / "source" / source_archive.name)

    history_bundle = upload / f"ScamouraiWallet-full-history-v{version}.bundle"
    build_git_bundle(history_bundle)
    copy_or_link(history_bundle, bundle_directory / "source" / history_bundle.name)

    write_manifest(bundle_directory, bundle_directory / "SHA256SUMS")
    release_archive = upload / f"{bundle_name}.zip"
    deterministic_zip(bundle_directory, release_archive, released)

    direct_assets = {
        ROOT / "POST_MORTEM.md": upload / "POST_MORTEM.md",
        ROOT / "output/pdf/POST_MORTEM.pdf": upload / "POST_MORTEM.pdf",
        ROOT / "CITATION.cff": upload / "CITATION.cff",
        ROOT / ".zenodo.json": upload / "zenodo-metadata.json",
        ROOT / "BIBLIOGRAPHY.txt": upload / "BIBLIOGRAPHY.txt",
        ROOT / "timestamps/ARCHIVE_SHA256SUMS": upload / "ARCHIVE_SHA256SUMS",
        commit_path: upload / "COMMIT.txt",
    }
    for name in INDEX_FILES:
        if (ROOT / name).is_file():
            direct_assets[ROOT / name] = upload / name
    for source, destination in direct_assets.items():
        copy_file(source, destination)
    for relative in proofs:
        destination = upload / timestamp_upload_name(relative)
        if destination.exists():
            fail(f"Timestamp proof release-name collision: {destination.name}")
        copy_file(ROOT / relative, destination)

    write_manifest(upload, upload / "SHA256SUMS")
    if git_text("rev-parse", "HEAD") != commit:
        fail("HEAD changed while the release was being built; discard this output")
    if args.development:
        if worktree_signature(output) != starting_signature:
            fail("The working tree changed during the development build; discard this output")
    else:
        ending_changes = dirty_entries()
        if ending_changes:
            preview = "\n".join(f"  {entry}" for entry in ending_changes[:20])
            fail(f"The working tree changed while the release was being built:\n{preview}")
    manifest_entries = sum(1 for line in (upload / "SHA256SUMS").read_text(encoding="utf-8").splitlines() if line)
    print(f"Built {release_archive.relative_to(ROOT)}")
    print(f"Commit: {commit}")
    print(f"Tree state: {tree_state}")
    print(f"Upload artifacts hashed: {manifest_entries}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default="dist",
        help="output directory below the repository root (default: dist)",
    )
    parser.add_argument(
        "--tag",
        help="release tag; defaults to post-mortem-v<VERSION>",
    )
    parser.add_argument(
        "--development",
        action="store_true",
        help="package the working tree with a non-publishable dirty-build warning",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        build(parse_args())
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.strip() if isinstance(exc.stderr, str) else ""
        fail(f"Command failed: {' '.join(exc.cmd)}{': ' + detail if detail else ''}")

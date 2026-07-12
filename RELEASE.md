# Archival release procedure

This repository treats a release as an immutable historical edition. Never move
an existing tag, replace an already published file under the same version, or
silently correct a released edition. Make corrections in `CORRECTIONS.md` and
publish a new version.

The first planned version is `1.0.0`, tagged `post-mortem-v1.0.0`. The release
date, version, author name, title, repository URL, and canonical Pages URL must
agree across `CITATION.cff`, `.zenodo.json`, the Pages metadata, and the tag.

## 1. Prepare and verify the edition

1. Merge all reviewed publication and evidence-index changes into the branch
   that will be released.
2. Confirm that `POST_MORTEM.md`, `output/pdf/POST_MORTEM.pdf`, `CLAIMS.jsonl`,
   `TIMELINE.md`, `ENTITY_ALIASES.json`, `EVIDENCE_MANIFEST.json`,
   `METHODOLOGY.md`, and `CORRECTIONS.md` describe the same edition.
3. Commit the editorial source, indexes, metadata, and build tools. The
   Pages generator intentionally refuses to cite an uncommitted
   `POST_MORTEM.md`, because its HTML and JSON-LD record an exact source commit.
4. Install the static-site dependency, regenerate the Pages edition from that
   committed source, verify it, and commit the generated `docs/` files. This
   gives the PDF an exact committed HTML input:

   ```sh
   python -m pip install -r tools/requirements-site.txt
   python tools/build_site.py
   python tools/build_site.py --check
   ```

5. Rebuild the tagged A4 PDF with Chrome or Chromium, render and visually
   inspect its pages, and commit the PDF separately:

   ```sh
   python -m pip install -r tools/requirements-pdf.txt
   python tools/build_pdf.py
   ```

6. Regenerate and commit `docs/` once more so its PDF URL is pinned to the new
   PDF commit. The PDF freshness fingerprint intentionally abstracts only that
   self-referential URL, so the final site repin does not require another PDF
   rebuild. Refresh the timestamp manifest and proof only after this sequence,
   then require both of these checks to pass on the clean result:

   ```sh
   python tools/build_site.py --check
   python tools/build_pdf.py --check
   ```

   If these commits were prepared on a feature branch, merge with a true merge
   commit. Squashing or rebasing would rewrite commits already embedded in the
   immutable asset URLs.
7. If a pre-commit package test is needed at any point, use development mode.
   It is clearly marked as dirty and is not suitable for publication:

   ```sh
   python tools/build_release.py --development --output dist-dev
   ```

8. On the resulting clean release commit, build the actual package and inspect
   `dist/upload/SHA256SUMS` and `dist/upload/COMMIT.txt`:

   ```sh
   python tools/build_release.py --output dist --tag post-mortem-v1.0.0
   ```

   The build contains the Markdown, PDF, citation metadata, claim indexes,
   committed Pages edition, evidence manifest, any committed OpenTimestamps
   proofs, a deterministic source snapshot, and a full Git bundle made with
   `git bundle create --all`. The Git bundle preserves the available refs and
   history; the source archive is the easier format for non-Git consumers.

9. For a reproducibility check, build twice to two different output directories
   and compare the upload manifests. The two `SHA256SUMS` files must be identical:

   ```sh
   python tools/build_release.py --output dist-a --tag post-mortem-v1.0.0
   python tools/build_release.py --output dist-b --tag post-mortem-v1.0.0
   diff -u dist-a/upload/SHA256SUMS dist-b/upload/SHA256SUMS
   ```

## 2. Publish the canonical Pages edition

The `pages.yml` workflow validates the committed static build and deploys
`docs/` after a push to `master`. Before its first run, set **Settings → Pages →
Build and deployment → Source** to **GitHub Actions**. The canonical URL is:

<https://nopara73.github.io/ScamouraiWallet/>

If a durable custom domain is added later, configure it in the repository's
Pages settings and update the canonical URL, sitemap, CFF, Zenodo metadata, and
JSON-LD together in a new version. If the complete post-mortem is also
published on Medium, set that story's canonical link to the Pages URL rather
than maintaining two competing canonical editions.

## 3. Enable Zenodo before the first public release

In the repository owner's Zenodo account, connect GitHub and enable this
repository in the GitHub integration. Do this before publishing the GitHub
Release. The workflow does not contain a Zenodo token and does not call the
Zenodo API; publication remains an explicit account-owner action.

`.zenodo.json` deliberately declares the upload as `publication` with
`publication_type` set to `report`. This is more accurate than classifying the
record only as software. Before publishing the Zenodo deposit, verify the title,
abstract, creator, release date, version, open-access status, MIT license, and
keywords in Zenodo's preview.

No DOI or ORCID is present in the repository metadata. Do not add a guessed,
placeholder, or example identifier.

## 4. Create the annotated tag and GitHub Release

Create the annotated tag only from the reviewed clean commit. The annotation
should summarize the scope of the frozen edition and disclose any important
limits; it becomes the initial GitHub Release text.

```sh
git switch master
git pull --ff-only
git status --short
git tag -a post-mortem-v1.0.0 -m "Post-mortem archival edition 1.0.0"
git show --stat post-mortem-v1.0.0
git push origin post-mortem-v1.0.0
```

The `archive-release.yml` workflow rejects a lightweight tag, validates the CFF,
JSON, claim index, evidence manifest, and Pages build, creates the release
package, uploads a workflow artifact, and creates a draft GitHub Release with all
files from `dist/upload/`. It publishes the draft only after every asset upload
succeeds. A failed run may replace assets while the release remains a draft; the
workflow refuses to replace assets after publication.

To verify the downloaded files on a Unix-like system:

```sh
sha256sum -c SHA256SUMS
git clone ScamouraiWallet-full-history-v1.0.0.bundle ScamouraiWallet-v1.0.0
```

On PowerShell, compare each entry with `Get-FileHash -Algorithm SHA256`.

## 5. Record the DOI without rewriting version 1.0.0

After Zenodo publishes the deposit, copy both its version DOI and concept DOI
from the Zenodo record. Add the real version DOI to the preferred report citation
in `CITATION.cff`; add the concept DOI as a separately described identifier if it
is useful for citing the evolving archive. Add DOI links to the canonical Pages
edition and release notes. Do not edit the `post-mortem-v1.0.0` tag or replace its
bundle.

Publish the metadata backfill as a new patch edition (for example `1.0.1`) and
record the change in `CORRECTIONS.md`. This preserves the fact that the first
edition could not contain an identifier that did not yet exist. An alternative
for a later major edition is to reserve a DOI in a manual Zenodo draft before
tagging, but do not create both a manual deposit and an integration-created
deposit for the same edition.

## 6. Timestamp the exact release files

OpenTimestamps proves that exact bytes existed no later than a Bitcoin block; it
does not establish whether the report's claims are true. Install the client and
stamp both the release manifest and PDF after the clean release build:

The repository already includes `timestamps/ARCHIVE_SHA256SUMS` and its `.ots`
sidecar. That compact manifest covers the report, PDF, indexes, citation and site
metadata, and `sources/SHA256SUMS`; a newly submitted sidecar can remain pending
until the calendar commitment reaches a Bitcoin block. Check it with
`python tools/build_timestamp_manifest.py --check`, then use `ots upgrade` and
`ots verify` as documented in `timestamps/README.md`.

The versioned release manifest below is a separate target because it includes
the exact tag, full-history bundle, source archive, and release ZIP, none of
which exist before the release commit is frozen.

```sh
python -m pip install opentimestamps-client
ots stamp dist/upload/SHA256SUMS
ots stamp dist/upload/POST_MORTEM.pdf
ots info dist/upload/SHA256SUMS.ots
ots info dist/upload/POST_MORTEM.pdf.ots
```

Attach both `.ots` sidecars to the `post-mortem-v1.0.0` GitHub Release. Commit
copies under `timestamps/post-mortem-v1.0.0/` in a follow-up commit so the proofs
are preserved independently of the release UI. Once the calendar attestation has
settled into a Bitcoin attestation, upgrade and verify the proofs:

```sh
ots upgrade timestamps/post-mortem-v1.0.0/SHA256SUMS.ots
ots upgrade timestamps/post-mortem-v1.0.0/POST_MORTEM.pdf.ots
ots verify timestamps/post-mortem-v1.0.0/SHA256SUMS.ots -f dist/upload/SHA256SUMS
ots verify timestamps/post-mortem-v1.0.0/POST_MORTEM.pdf.ots -f dist/upload/POST_MORTEM.pdf
```

An upgraded proof changes the `.ots` sidecar but not the timestamped file. Commit
that upgrade normally; never regenerate the PDF or manifest under the old tag.

## 7. Finish the preservation checklist

After the public GitHub Release and Zenodo record exist:

- record the version DOI, concept DOI, release URL, exact commit, and tag in the
  release notes and `CORRECTIONS.md` as appropriate;
- request Software Heritage Save Code Now for the canonical repository URL;
- submit the canonical Pages URL, release URL, and important evidence pages to
  Internet Archive Save Page Now;
- verify the independent Git mirror from a fresh clone; and
- keep the original release files and `SHA256SUMS` in offline storage.

Save the resulting Software Heritage identifier and Wayback capture URLs in a
new, versioned metadata update. These services confirm preservation and file
identity, not the truth of disputed historical claims.

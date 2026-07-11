# Source archive

This directory preserves the primary material cited by [`POST_MORTEM.md`](../POST_MORTEM.md) and supplementary records retained for reproducibility. It was assembled on July 10–11, 2026.

[`URLS.md`](URLS.md) lists every external URL in the essay and identifies the corresponding local copy where one is included. [`SHA256SUMS`](SHA256SUMS) records a SHA-256 digest for every archived file.

## Contents

- `legal/` — court filings and the defense letter concerning the late-disclosed FinCEN communication.
- `research/` — the complete OXT report, cited thesis, and supplementary open CoinJoin studies.
- `code/` — exact-commit source snapshots, commit patches, Blockchain.info-to-Samourai and Dumplings adoption audits, Whirlpool configuration and Ricochet implementation evidence, and a complete ZeroLink Git bundle.
- `screenshots/` — focused exhibits used in the essay, supplementary verification crops, and the Medium headline image.
- `social/` — public profile HTML, X oEmbed records, and saved Old Reddit pages.
- `video/` — YouTube metadata for cited recordings and a complete archive of the 33 Research Club transcripts available from the playlist, including raw captions and timestamped source data. The videos themselves are not copied.
- `web/` — dated HTML or Markdown snapshots of central web sources that could be obtained cleanly, including Samourai's own description of Whirlpool's “unmixed toxic change.”

## Boundaries

The private unpublished memoir supplied during drafting is not present anywhere in this repository. Neither is nopara73's parents' street address. Public evidence is preserved without republishing that address.

The repository's MIT license covers the repository's original material. Third-party documents, screenshots, articles, research, and source snapshots remain subject to their original authors' licenses and rights. They are stored here unchanged for attribution, verification, and evidentiary preservation; their inclusion does not relicense them under MIT.

Some sources could not be copied reliably, and some long-form third-party works were left external. Those links remain recorded in `URLS.md`. A local HTML snapshot may depend on assets that remain hosted by the original site; the PDF, image, JSON, patch, ZIP, and Git-bundle files are self-contained.

## ZeroLink verification

`code/zerolink-full-history.bundle` is a complete Git bundle. To inspect it without trusting GitHub:

```sh
git clone sources/code/zerolink-full-history.bundle ZeroLink
```

The August 14, 2017 publication state used in the essay is also preserved as `code/zerolink-25d1502-publication-snapshot.zip`.

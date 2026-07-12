# Pre-release timestamp from 2026-07-11

This directory preserves the first timestamped archive manifest, committed in
repository revision `55142e18f5052847775d7a5c41dd2dc1bdb50d64`, before review
fixes changed the site, PDF metadata, and Zenodo metadata.

The manifest's SHA-256 digest is
`dd5c377274543902af09c0be1a72cb0839ada7a7618c94d4ec8900406a5cce0b`.
The upgraded proof includes Bitcoin attestations; the earliest is block 957599.

Verify the preserved bytes with:

```sh
ots verify timestamps/pre-release-2026-07-11/ARCHIVE_SHA256SUMS.ots \
  -f timestamps/pre-release-2026-07-11/ARCHIVE_SHA256SUMS
```

This proof remains useful evidence of the pre-release archive's existence. It
is not presented as the proof for the later reviewed v1.0 release candidate.

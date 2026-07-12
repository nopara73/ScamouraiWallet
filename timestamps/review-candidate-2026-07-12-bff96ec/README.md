# Review candidate timestamp from 2026-07-12

This directory preserves the manifest and proof prepared at repository revision
`bff96ec0fcd0a2fdf1bd00729c54e3677c2a0298`, before the final metadata-alignment
review changed the canonical site and PDF.

The manifest's SHA-256 digest is
`617288392c0771b41d62f967a3d62df7a17b9b9fdfdecf96581bac0c0469e169`.
The sidecar was still awaiting calendar-to-Bitcoin confirmation when it was
preserved; it can be upgraded without changing the timestamped manifest.

```sh
ots upgrade timestamps/review-candidate-2026-07-12-bff96ec/ARCHIVE_SHA256SUMS.ots
ots verify timestamps/review-candidate-2026-07-12-bff96ec/ARCHIVE_SHA256SUMS.ots \
  -f timestamps/review-candidate-2026-07-12-bff96ec/ARCHIVE_SHA256SUMS
```

This is not the proof for the later reviewed v1.0 release candidate.

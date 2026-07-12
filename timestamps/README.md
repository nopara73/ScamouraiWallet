# OpenTimestamps integrity proof

`ARCHIVE_SHA256SUMS` hashes the report, PDF, claim indexes, evidence manifest,
citation metadata, canonical HTML metadata, and `sources/SHA256SUMS`. The last
of those recursively anchors the 285 archived evidence files.

Rebuild and check the manifest from the repository root:

```sh
python tools/build_timestamp_manifest.py
python tools/build_timestamp_manifest.py --check
```

The adjacent `ARCHIVE_SHA256SUMS.ots` sidecar is an OpenTimestamps proof for
those exact manifest bytes. A newly submitted proof may contain only pending
calendar attestations until a Bitcoin block confirms the calendar commitment.
Upgrade and verify it without changing the manifest:

```sh
ots upgrade timestamps/ARCHIVE_SHA256SUMS.ots
ots verify timestamps/ARCHIVE_SHA256SUMS.ots -f timestamps/ARCHIVE_SHA256SUMS
```

`pre-release-2026-07-11/` preserves the prior manifest and its upgraded,
Bitcoin-confirmed proof rather than silently replacing that earlier attestation.

The proof establishes that the timestamped bytes existed no later than the
eventual Bitcoin attestation. It does not establish that any historical claim
in the report is true.

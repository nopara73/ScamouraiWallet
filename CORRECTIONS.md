# Corrections

## Current state

- **Record state:** unreleased archival-index draft
- **Ledger initialized:** 2026-07-11
- **Numbered release covered:** none yet
- **DOI covered:** none yet
- **Policy:** released versions are preserved; substantive changes are published as a new version and recorded here

This ledger covers corrections to the post-mortem and its machine-readable publication package. An entry records that wording changed or should change; it does not by itself settle unrelated claims.

## Ledger

| ID | Date recorded | Status | Affected record | Prior wording or state | Corrected wording or action | Evidence and note |
| --- | --- | --- | --- | --- | --- | --- |
| COR-001 | 2026-07-11 | Incorporated before first indexed release | `POST_MORTEM.md`, “When you wrestle with a pig, you both get dirty”; `CLM-026`; timeline entry for 2024-04-04 | The author had remembered the assassination victim as a Japanese prime minister. | Identify the victim as Japanese Socialist Party chairman **Inejirō Asanuma**. | The recovered [original post media](sources/social/media/samouraidev-1775920406953701884-photo1.png) matches [World Press Photo's identification](https://www.worldpressphoto.org/collection/photo-contest/1961/yasushi-nagao/1) of Yasushi Nagao's photograph of Asanuma's assassination. The essay now states the correction explicitly; it does not change the wording or nature of the archived post. |
| COR-002 | 2026-07-11 | Incorporated before first indexed release | `POST_MORTEM.md`, “What the server seizure revealed”; `CLM-034`; timeline plea entry | “In August 2025, Rodriguez and Hill each pleaded guilty …” conflated the announcement month with the plea date. | State that both pleas were entered on **2025-07-30** and that the Justice Department announced them on **2025-08-06**. | The archived [Justice Department plea announcement](sources/web/justice-2025-guilty-pleas-wayback.html) says both defendants “pled guilty on July 30, 2025.” The essay now states the plea and announcement dates separately. |

No numbered release exists yet, so both entries were incorporated into the first release without altering a frozen artifact.

## What requires a ledger entry

A change is substantive when it alters any of the following:

- a person's identity, alias, role, or attribution;
- an event, publication, filing, plea, or sentence date;
- a quotation or the account to which it is attributed;
- the status of a statement as fact, recollection, allegation, party assertion, government representation, plea, or judgment;
- a numerical total, denominator, methodology, or confidence level;
- a source URL, local evidence path, hash, or caveat in a way that changes what readers can verify; or
- a conclusion that a reasonable reader could understand differently after the edit.

Spelling, broken internal links, formatting, and other non-substantive maintenance may be grouped in one entry, but only when meaning and provenance do not change.

## How to report a correction

Open a repository issue or pull request titled `Correction: <short description>` and include:

1. the affected release, file, section, and claim ID, if any;
2. the exact disputed wording;
3. the proposed replacement wording;
4. a primary source or the strongest available evidence;
5. whether the issue concerns factual accuracy, attribution, chronology, quotation, privacy, or interpretation; and
6. any sensitive information that must **not** be republished.

Do not place an uncensored home address, private key, seed phrase, authentication secret, or unnecessary personal data in a public report. Describe sensitive evidence and arrange a private review channel with the repository owner if it is genuinely necessary.

## Maintainer procedure

For each credible report:

1. assign the next immutable `COR-NNN` identifier;
2. preserve the report and acknowledge any conflict of interest;
3. inspect the cited primary source and the locally archived copy;
4. label the claim by evidentiary category rather than flattening allegations and findings;
5. update every affected derivative—essay, HTML/PDF edition, `CLAIMS.jsonl`, timeline, alias map, bibliography, and metadata;
6. add the ledger entry before publishing the correction;
7. release a new version and preserve the old tag, release assets, hashes, and DOI record; and
8. explain any rejected correction request with the same precision expected of the original archive.

Permitted statuses are `reported`, `under review`, `accepted`, `incorporated`, `rejected with reason`, `withdrawn by reporter`, and `superseded`. A released claim is never silently deleted and its ID is never reused. If evidence becomes insufficient, mark the claim withdrawn, retain its history, and point to the correcting release.

## Versioning rule

- Patch release: correction or clarification that does not reorganize the evidentiary thesis.
- Minor release: new evidence, new indexed claims, or a material qualification.
- Major release: a change that substantially revises the archive's structure or central conclusions.

Every release should identify its exact Git commit and carry a fresh checksum manifest. A concept DOI may point to the newest version, but each immutable release should remain separately citable.

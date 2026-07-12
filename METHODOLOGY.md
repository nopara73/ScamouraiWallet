# Methodology

## Purpose and scope

This archive separates retrieval from interpretation. [CLAIMS.jsonl](CLAIMS.jsonl) exposes a compact set of central propositions, [TIMELINE.md](TIMELINE.md) orders dated events without collapsing their evidentiary status, and [ENTITY_ALIASES.json](ENTITY_ALIASES.json) makes identity linkages and uncertainty explicit. They are indexes into the evidence, not substitutes for [POST_MORTEM.md](POST_MORTEM.md), the full sources, or independent review.

The index is intentionally narrower than the essay. A row is included when it is central to the authorship, wallet architecture, public-claims, conduct, or legal-record narrative and can be anchored to a preserved source. Omissions do not imply that an unindexed assertion is false. Inclusion does not imply endorsement of a source's conclusions.

## Evidence categories

Sources are classified by what they can establish:

1. **Repository and source-code records.** Git bundles, exact-commit ZIPs, and patches establish commit authorship metadata, dates, diffs, and source-visible behavior. Git author strings are not identity verification, commit counts are not intellectual authorship, and one snapshot is not every release.
2. **Official project records.** Project documentation, release notes, issues, and official-account posts establish what a project published, claimed, configured, or displayed at a given time. They are not automatically independent assessments, and a shared account does not identify the individual who typed a post.
3. **Court and government records.** An indictment establishes an allegation; a defense submission establishes a party's assertion; a government sentencing memorandum establishes the government's representation; a plea and sentence establish the adjudicated outcome actually entered. One category is never silently promoted into another.
4. **Independent technical records.** Vulnerability disclosures, research papers, theses, public code audits, and reproducible datasets are evaluated within their stated threat model and measurement limits.
5. **Contemporaneous third-party statements.** Public comments, interviews, and corrections establish what the speaker said and when. They may corroborate context but do not become direct proof of every underlying event.
6. **First-person and anonymous-message records.** The author's recollection and contemporaneous reports establish his account. A screenshot of an anonymous message establishes what was received, not who controlled the account. The archive deliberately excludes the author's parents' street address.
7. **Derived analysis.** Chronologies, line attribution, endpoint tracing, source-lineage comparisons, and dataset totals are reproducible inferences. They are labeled as analysis and retain their limiting assumptions.

Where possible, a claim uses the most direct preserved record: an exact patch instead of a screenshot of a commit, a full filing instead of commentary about it, and a local post record instead of a later paraphrase. Screenshots remain useful for layout, surrounding context, or source material whose rendered image is itself relevant.

## `CLAIMS.jsonl` rules

Each physical line is one complete UTF-8 JSON object with the same eleven scalar fields:

| Field | Rule |
| --- | --- |
| `claim_id` | Stable identifier in the form `CLM-NNN`. IDs are not recycled after release. |
| `claim` | One narrow proposition, worded so the caveat does not reverse it. |
| `subject` | Compact retrieval label for the person, system, statement, or event. |
| `date` | ISO date, month, or interval for the event or source. Retrieval dates are identified in the caveat when used. |
| `primary_source_url` | One canonical public URL used in the essay or source inventory. It may later disappear; the local path is the durable anchor. |
| `archived_source_path` | One repository-relative path that existed and was validated when the index was generated. It is the best compact anchor, not necessarily the only supporting file. |
| `supporting_excerpt` | A short source phrase sufficient for retrieval. It is not a complete quotation of the source or a replacement for context. |
| `source_type` | Epistemic category, not merely a file format—for example `git-commit-patch`, `defense-sentencing-submission`, or `official-project-public-post`. |
| `confidence` | Confidence that the preserved evidence supports the claim exactly as narrowed, using the scale below. |
| `caveat` | The most important limit, alternative scope, or distinction needed to avoid over-reading. |
| `essay_section` | Exact human-readable section heading where the subject is discussed. |

One row normally names one local anchor even when the essay cites a chain of records. Follow the `essay_section`, [sources/URLS.md](sources/URLS.md), and the source notes for the full chain. A compound event is kept in one row only when the relationship is the proposition—for example, a public assertion followed by a specific later code change.

### Confidence scale

- **High:** a direct, preserved source or reproducible audit supports the narrowly worded claim. “High” does not certify a source's broader rhetoric. For a court filing, it may mean high confidence that the filing makes the stated representation—not that an unpublished underlying analysis has been independently replicated.
- **Medium:** the source is real and relevant, but the proposition depends on an attribution, incomplete context, an unsupported party estimate, or a multi-step inference. The caveat must identify the gap.
- **Low:** evidence is too incomplete for the proposition to appear as a positive claim. No low-confidence claims are included in the initial index; unresolved matters are instead omitted or recorded as non-assertions.

Confidence is not a probability and must not be inherited by related claims. For example, there is high confidence that the defense wrote “only 20%,” but only medium confidence in the percentage because no method or counts were supplied.

## Dates and chronology

Dates are normalized as follows:

- `YYYY-MM-DD` for an exact event date;
- `YYYY-MM` when only the month is supported;
- `start/end` for an inclusive interval or paired event dates;
- a descriptive period in the timeline when a later source reports an earlier event without a day.

Commit author dates, publication dates, filing dates, event dates, and archive retrieval dates are distinct. The timeline prefers the event date and notes a different announcement date when material. Time zones are not normalized unless the day boundary matters.

## Excerpts and transcription

Excerpts are deliberately short and must be read in the source. HTML entities are normalized, and typographic quotation marks may be rendered as plain ASCII in JSON. No excerpt is used to hide a qualification in the same source.

For PDFs, the page image and full filing take precedence over imperfect text extraction. For video, the archive preserves timestamped YouTube auto-captions and raw caption files; obvious recognition errors may be paraphrased in the essay, but transcripts are not presented as certified verbatim records. For X posts, oEmbed JSON preserves public text, author/display metadata, permalink, and embed HTML as retrieved; it does not prove account control. When an attached image supplies essential meaning, the original media or a context screenshot is cited as well.

## Identity policy

[ENTITY_ALIASES.json](ENTITY_ALIASES.json) distinguishes:

- established name and handle mappings used consistently across the archive;
- organizational accounts, which are not automatically assigned to a natural person;
- author-attributed aliases, which retain a lower confidence and an explicit non-adjudication caveat; and
- non-assertions, including anonymous senders that the evidence cannot identify.

An alias match is not evidence that the person authored every item under that identifier. Names are not inferred from interface labels, stylistic similarity, or proximity alone. Sensitive street-level doxxing is neither necessary for the historical record nor reproduced.

## Integrity and local verification

The archived evidence is content-addressed by [sources/SHA256SUMS](sources/SHA256SUMS). From the repository root:

```sh
cd sources
sha256sum -c SHA256SUMS
```

That manifest covers the archived source set listed at the time it was created. These newly generated root-level index files are not silently added to the existing source manifest; a release-level manifest should hash them together with the essay, PDF, citation metadata, and source archive.

The complete ZeroLink history can be inspected without the live GitHub repository:

```sh
git clone sources/code/zerolink-full-history.bundle ZeroLink
```

Exact-commit ZIPs were created with `git archive`, as documented in [sources/code/README.md](sources/code/README.md). Reproduction notes record commands and limitations for the source-lineage and adoption calculations.

## Updating and correcting the record

Released versions should be immutable. A correction changes a new version, records the old and new wording in [CORRECTIONS.md](CORRECTIONS.md), identifies affected claim IDs and files, cites the deciding evidence, and preserves the superseded release. Claim IDs remain stable; a withdrawn claim is marked withdrawn rather than deleted or reassigned.

Purely typographic changes may be grouped, but changes to identity, date, quotation, legal status, numerical result, confidence, or caveat are substantive and require a ledger entry. New evidence must not silently rewrite what an older release said.

## Boundaries

The methodology can establish provenance, internal consistency, and reproducibility. It cannot guarantee that a public source was truthful, that an archived screenshot shows every surrounding exchange, that an operator never deviated from published code, or that future readers will agree with the essay's moral conclusions. Those limits are reasons to preserve the primary record and its caveats, not reasons to collapse all evidence into equal uncertainty.

# Scamourai Wallet

This repository contains my first-person account of the conflict between Samourai Wallet and me, together with the primary records needed to check it. The archive is organized so readers do not have to trust my memory, a surviving website, or a social-media screenshot in isolation.

## Read this first

- [**Canonical HTML edition**](https://nopara73.github.io/ScamouraiWallet/) — the complete, crawlable article with publication metadata and stable section links.
- [**Post-Mortem: What Happened Between Samourai Wallet and Me**](POST_MORTEM.md) — the authoritative Markdown source with citations and evidence placed beside the events it documents.
- [**Illustrated PDF edition**](output/pdf/POST_MORTEM.pdf) — the publication-ready, tagged A4 edition.
- [**Machine-readable claims index**](CLAIMS.jsonl) — 35 central propositions with source anchors, confidence, caveats, and essay sections.
- [**Timeline and identity map**](TIMELINE.md) — dated events paired with [explicit alias evidence and uncertainty](ENTITY_ALIASES.json).
- [**Source archive guide**](sources/README.md) — what was preserved, how it is organized, and the archive's boundaries.
- [**Complete citation inventory**](sources/URLS.md) — 134 external URLs and preserved public-post permalinks, with local copies identified where available.
- [**SHA-256 manifest**](sources/SHA256SUMS) — integrity hashes for 285 archived files.
- [**Evidence manifest**](EVIDENCE_MANIFEST.json) — the source hashes joined to byte sizes, media types, original URLs, and the evidence snapshot commit.
- [**Citation metadata**](CITATION.cff) — the preferred report citation exposed through GitHub's “Cite this repository” interface.

The archive includes 33 evidence and publication images, four court filings, four research papers, exact-commit code snapshots and patches, a complete ZeroLink Git bundle, public and private-message records, saved web pages, 33 Research Club transcripts with raw captions and metadata, and metadata for four additional cited recordings.

## Evidence map

The descriptions below are deliberately short. They identify the issue shown by each record; the essay supplies the chronology, qualifications, and argument.

### ZeroLink authorship

- [**Samourai's first ZeroLink commit was “Fix typos.”**](sources/screenshots/zerolink-first-samourai-commit-fix-typos.jpg) The screenshot and [portable patch](sources/code/zerolink-8fbdcb9-fix-typos.patch) preserve the first contribution made after the framework and its 184-line specification already existed.
- [**The complete Git history makes the authorship claim reproducible.**](sources/code/zerolink-full-history.bundle) The bundle contains the public commit graph; the [August 2017 publication snapshot](sources/code/zerolink-25d1502-publication-snapshot.zip) fixes the comparison at the date used in the essay.
- [**The ZeroLink authorship audit records chronology, line ownership, and commit churn.**](POST_MORTEM.md#how-zerolink-actually-began) The accompanying [code-evidence guide](sources/code/README.md) makes the result reproducible instead of treating raw line counts as a slogan.
- [**ZeroLink was a wallet privacy framework, not merely a CoinJoin transaction type.**](sources/video/wasabi-research-club/transcripts/26-l7bK85obzrM.md) The timestamped discussion separates its blinded CoinJoin protocol from its broader network, wallet, and post-mix privacy rules—the scope Samourai later claimed to have co-created.

### Hosted backends, xpubs, and unsafe defaults

- [**In an xpub thread, Samourai falsely called its default Android app a “full node wallet.”**](sources/screenshots/x-samouraiwallet-2022-10-03-full-node-wallet.png) It had just defended its chosen server-backed architecture; exact production source from four days earlier selected Samourai’s backend whenever Dojo was absent and sent the wallet’s xpubs to that backend.
- [**Samourai's Android client could contact the hosted API with Tor disabled.**](sources/code/samourai-wallet-android-c71f21a-cited-files.zip) The exact-commit source preserves the wallet-creation, Tor-default, API-query, and xpub-registration paths cited in the essay.
- [**A proposal to make Tor and Dojo safer by default was closed immediately.**](sources/screenshots/gitlab-issue-458-default-settings.png) The preserved [GitLab issue](sources/web/gitlab-issue-458-wayback.html) records the suggested defaults, the owner's response, and the closure.
- [**Dojo's own documentation says it bypassed the default hosted servers.**](sources/web/dojo-documentation-archive.html) It also describes the Tracker that monitored registered xpubs and addresses.
- [**Dojo pairing arrived only in July 2019 and initially required a newly created wallet.**](sources/web/samourai-wallet-0.99.81-dojo-pairing-wayback.html) Samourai’s own release notes say restoration of an existing wallet was unsupported, so pairing later could not retract an xpub already disclosed to the hosted backend.
- [**Sentinel moved xpub lookups from Blockchain.info to Samourai's API in 2017.**](sources/screenshots/sentinel-xpub-moved-to-samourai-api.jpg) The [commit patch](sources/code/sentinel-77eca1d-move-xpub-to-samourai-api.patch) preserves the change directly.
- [**Sentinel added Tor routing more than two years after the xpub move.**](sources/code/sentinel-1a4722f-add-tor.patch) Exact-commit [v3](sources/code/sentinel-android-cf46177-cited-files.zip) and [pre-seizure v5](sources/code/sentinel-android-b5ef29c-cited-files.zip) snapshots preserve the later server and Tor choices.
- [**Asked about xpubs reaching Samourai servers, Hill changed “servers” to “coordinator.”**](sources/screenshots/x-samouraidev-2022-07-27-xpub-zerolink.png) The same reply claimed Samourai implemented nopara73's ZeroLink specification because its author lacked the skill to do so; the Git history above disproves that authorship reversal.
- [**The Research Club warned about the xpub-server design years before the seizure.**](sources/video/wasabi-research-club/README.md) Timestamped transcripts preserve the April 2020 rejection of a central xpub server, the July 2021 Samourai/SharedCoin comparison, and the September 2022 warning that retained xpubs could be exposed by hacking or seizure.
- [**SharedCoin's server knowledge was treated as obvious; Samourai rebuilt the same operator-trust problem.**](sources/video/wasabi-research-club/transcripts/10-CtmSylCQNIc.md) Separate 2020 and 2021 discussions record that public CoinJoin ambiguity could not protect users from an operator that already knew the links, then apply that point to Samourai's default xpub collection.

### Blockchain.info lineage

- [**Hill led the visible Blockchain.info Android code history; he was not an incidental contributor.**](sources/code/blockchain-samourai-lineage.md) The repository begins with his initial commit, contains 352 commits under his identities, and includes his “UI prep for shared coin” change; contemporary records identify Rodriguez as product lead.
- [**Samourai deliberately stayed closed-source for about a year, then published code with Blockchain.info lineage.**](sources/code/blockchain-samourai-lineage.md) Exact-commit archives preserve the paired files, including a 96-percent Git rename and a `BitcoinScript` descendant retaining 93.8 percent of the smaller file's normalized unique lines.

### What the seized servers revealed

- [**The government said retained xpubs could help trace or “demix” many mobile Whirlpool users.**](sources/screenshots/government-sentencing-memo-page-37.png) The complete [government sentencing memorandum](sources/legal/2025-10-31-government-sentencing-memorandum-ecf-157.pdf) states the finding and its limit: xpub analysis did not by itself identify the real-world users.
- [**After the seizure, Hill worried about “the wallet backends (xpubs).”**](sources/screenshots/government-sentencing-memo-page-38.png) The message appears in the same government filing.
- [**Hill's defense did not deny xpub collection; it called it necessary and asserted it affected “only 20%.”**](sources/screenshots/hill-sentencing-submission-page-28.png) The [submission](sources/legal/2025-10-24-hill-sentencing-submission-ecf-155.pdf) provides no source, method, counts, or independent validation for that percentage.

### Public claims contradicted by later code

- [**Rodriguez said Whirlpool did not change Tor identity between input and output registration.**](sources/screenshots/whirlpool-tor-default-conversation.png) The contemporaneous exchange preserves the categorical answer and surrounding dispute.
- [**The client later added `changeIdentity()` immediately before output registration.**](sources/screenshots/whirlpool-change-tor-identity-code.jpg) The [full patch](sources/code/whirlpool-fbee9e8-change-tor-identity.patch) and [commit record](sources/screenshots/whirlpool-change-tor-identity-commit.jpg) preserve the quiet correction.
- [**Samourai called Wasabi’s coordinator-fee address reuse irreversible—then Whirlpool reused one across 37 transactions.**](sources/web/gitlab-issue-462-wayback.html) The archived report identifies the address and transactions; one cited consolidation spends 36 outputs from it. The essay separates this direct double standard from the narrower, disputed question of whether the reuse itself reduced Whirlpool users’ anonymity.

### The OXT “critical vulnerability” claim

- [**Samourai acquired OXT; Hill's own sentencing packet calls it “owned and operated by Samourai Wallet.”**](sources/screenshots/hill-sentencing-oxt-owned-operated.png) Samourai's [2017 acquisition announcement](sources/web/samourai-oxt-acquisition-2017-wayback.html) records the all-bitcoin purchase, while the government later described OXT as a tracing and wallet-attribution tool operated by Hill and Rodriguez.
- [**OXT said privacy must be protected by default—while its owner collected xpubs by default.**](sources/web/oxt-follow-up.md) Its follow-up called OXT Samourai's “sparring partner” and placed responsibility on software defaults rather than users, the opposite of Samourai's Dojo escape hatch.
- [**OXT's test begins with the target's funds and wallet state already known.**](sources/screenshots/oxt-report-page-5-test-actors.png) The [complete report](sources/research/2020-oxt-wasabi-report-full.pdf) supplies the assumptions omitted from the public warning.
- [**The model requires knowledge of the target wallet at step N and later mixing events.**](sources/screenshots/oxt-report-page-2-assumed-wallet-knowledge.png) Its own [next page](sources/screenshots/oxt-report-page-3-exogenous-randomness.png) introduces the additional information needed to continue the analysis.
- [**The report labels its result critical without recovering Wasabi's blinded input-output mapping.**](sources/screenshots/oxt-report-page-7-severity-claim.png) The archived [contemporaneous response](sources/social/reddit/icvu58-oxt-response.html) and [OXT follow-up](sources/web/oxt-follow-up.md) preserve both sides of the dispute.
- [**The WabiSabi development timeline predates OXT's disclosure.**](sources/web/bitcoinops-2020-06-17-wabisabi.html) This record matters because Samourai later portrayed Wasabi 2's behavior as a reaction to the report.
- [**Wasabi examined OXT-linked Boltzmann in public five months before the attack.**](sources/video/wasabi-research-club/transcripts/11-CYIDAqMSc4A.md) The complete March 2020 session distinguishes transaction-wide partition entropy from an individual user's privacy and records the computation's limits at Wasabi scale.

### The megaphone was bigger than the product

- [**Wasabi carried 8.19 times Whirlpool's fresh-bitcoin volume across their shared Dumplings dataset.**](sources/screenshots/dumplings-fresh-bitcoins-adoption.png) The [reproduction audit](sources/code/dumplings-adoption-audit.md) records 247,675 fresh BTC for Wasabi against 30,228 for Whirlpool from April 2019 through August 2022, with Wasabi ahead in every one of forty-one months.
- [**Free remixes inflated activity without representing new adoption.**](sources/code/dumplings-36f28f2-adoption-files.7z) The preserved Dumplings inputs separate newly arriving bitcoin from repeated remixes, avoiding the headline transaction counts that made Whirlpool appear larger than it was.

### Moving the privacy problem

- [**Samourai itself called Whirlpool's output from `TX0` “unmixed toxic change.”**](sources/web/samourai-atomic-swaps-toxic-change.md) The official statement contradicts any impression that moving change outside the CoinJoin made it disappear from the user's transaction history.
- [**Whirlpool's fixed denominations imposed visible costs before and after mixing.**](sources/code/whirlpool-server-cited-files.zip) Official server configuration and the [complete panel transcript](sources/video/wasabi-research-club/transcripts/34-Zu-bT9XojYk.md) document public `TX0` preparation, fixed pool amounts, and the consolidation and new change often required for ordinary payments.
- [**Ricochet's default hop chain was recognizable in its own source.**](sources/code/samourai-wallet-android-c71f21a-cited-files.zip) The code constructs four sequential hops with calculated per-hop decreases; the essay treats this as a visible pattern, not as a proven deanonymization attack.

### Sockpuppets, retaliation, and threats

- [**The foneBTC investigation connects the sockpuppet trail to TDevD/William Hill.**](sources/web/samouraileaks-part-1.html) The decisive exhibits are preserved separately as the [project trail](sources/screenshots/samouraileaks-sockpuppet-nail-in-coffin.jpg) and [conclusion](sources/screenshots/samouraileaks-sockpuppet-conclusion.jpg).
- [**Gregory Maxwell warned that Samourai sent users' addresses to its server while advertising privacy.**](sources/screenshots/samouraileaks-part-2-greg-maxwell-privacy-warning.jpg) His [contemporaneous account](sources/screenshots/samouraileaks-part-2-greg-maxwell-harassment-account.jpg) says criticism produced harassment and “bonkers accusations.”
- [**The official account's public conduct targeted critics instead of answering them.**](sources/screenshots/samourai-public-conduct-gallery.png) The gallery is cited to document the behavior, not to endorse repeating its slurs.
- [**My April 2023 statement preserved one of the death threats I received.**](sources/screenshots/nopara73-death-threat-statement-2023-04-16.jpg) The associated [public record](sources/social/tweets/nopara73-1647489516939382784.json) and follow-up are archived as text metadata.
- [**Anonymous messages sent a full address, asked if I thought I could stay safe, and threatened an eventual meeting.**](sources/screenshots/private-threat-we-shall-meet.png) The separate [address screenshot](sources/screenshots/private-threat-censored-address-and-town.png) was supplied with its street-level portion already blacked out; the account labels do not independently prove who controlled them.
- [**The public SamouraiDev profile paired my name and parents' town with violent language.**](sources/screenshots/samouraidev-profile-2026-07-10.jpg) My parents' street address is intentionally not reproduced or linked anywhere in this repository.
- [**The official Samourai Wallet account posted “Snitches get stitches.”**](sources/screenshots/samouraiwallet-public-threat-source-image-2023-04-18.png) The complete source image is preserved because X's timeline preview cropped its text.
- [**Hill told me that as a “collaborator” I deserved “much worse” beside an armed-punishment image.**](sources/screenshots/x-samouraidev-2023-04-20-deserve-worse.png) The [original post](https://x.com/SamouraiDev/status/1649019968296566787), oEmbed record, screenshot, and attached media are preserved.
- [**A follower hoped I would end up “in a ditch”; Hill answered “Yes” and “Soon.”**](sources/screenshots/x-samouraidev-2024-02-20-get-yours-soon.png) The thread began with Hill saying I was “overdue to get yours” and appending my parents' town as a hashtag.
- [**“The fat boy is gutted” appeared above a photograph of a politician's onstage assassination.**](sources/screenshots/x-samouraidev-2024-04-04-gutted-assassination.png) The victim was Japanese Socialist Party chairman Inejirō Asanuma—not a prime minister—and the original image file and post metadata are archived.

### Product-security record

- [**The PIN bypass allowed offline brute-force recovery from copied wallet files.**](sources/web/pin-bypass-disclosure.html) The disclosure, proof of concept, timeline, and [CVE record](sources/web/nvd-cve-2021-36689.html) are preserved.
- [**A William Hill-attributed Android component used Random.org in wallet randomness generation.**](sources/code/randomorggenerator-dfb781c.java) The archived [SamouraiLeaks Part 3](sources/web/samouraileaks-part-3.html) traces the code and its history.
- [**Independent developers had already documented the predecessor Android wallet's cryptographic failure.**](sources/social/reddit/37oxow-android-security.html) This record provides the technical discussion underlying the later coverage.

### Court records and legal context

- [**The official account relished the possibility that hackers would send Luke Dashjr’s stolen coins into Whirlpool.**](sources/social/tweets/samouraiwallet-1610484148057120768.json) The complete January 2023 thread begins with funds labeled “Wallet Controlled By Hackers,” asks what Samourai would do if they entered Whirlpool, and preserves the official answer; it does not claim the deposit actually occurred.
- [**The superseding indictment alleged Dread marketing through accounts presented as independent users.**](sources/legal/2025-06-24-superseding-indictment-ecf-109.pdf) The relevant [first](sources/screenshots/superseding-indictment-page-10-dread-marketing.png) and [second](sources/screenshots/superseding-indictment-page-11-dread-marketing.png) pages are rendered for quick review. These were allegations when filed, not findings by themselves.
- [**The defense alleged that favorable FinCEN communications were disclosed late.**](sources/legal/2025-defense-letter-late-fincen-disclosure.pdf) This is preserved as a defense argument, not presented as a judicial finding.
- [**The arrest, seizure, guilty pleas, and sentencing are preserved as separate dated records.**](sources/URLS.md) The inventory links the archived Justice Department pages and distinguishes the procedural stages.

### Independent research and recordings

- [**The 2022 thesis identifies the privacy trust placed in Samourai's default backend.**](sources/research/2022-varga-coinjoin-protocols-thesis.pdf) It also compares the published CoinJoin designs and implementations in detail.
- [**The complete Wasabi Research Club playlist transcript archive preserves the technical record.**](sources/video/wasabi-research-club/README.md) Thirty-three available transcripts include raw captions, timestamped source data, video metadata, a completeness manifest, and a [Samourai findings index](sources/video/wasabi-research-club/SAMOURAI-FINDINGS.md).
- [**Four additional recordings preserve contemporary claims, criticism, and competing recollections.**](sources/video/README.md) The guide identifies the relevant timestamps and local metadata.
- [**Developer and community statements are archived by exact post or comment.**](sources/social/README.md) The archive contains X oEmbed JSON, dated Reddit HTML, and a public profile snapshot.

## Repository map

| Path | Contents |
| --- | --- |
| [`POST_MORTEM.md`](POST_MORTEM.md) | Complete essay, citations, and inline exhibits |
| [`output/pdf/`](output/pdf/) | Publication-ready PDF |
| [`docs/`](docs/) | Deterministic canonical HTML edition, JSON-LD metadata, sitemap, and robots file |
| [`CLAIMS.jsonl`](CLAIMS.jsonl) | Claim-level retrieval index with evidence, confidence, and caveats |
| [`TIMELINE.md`](TIMELINE.md) | Chronology distinguishing records, recollection, allegations, pleas, and findings |
| [`ENTITY_ALIASES.json`](ENTITY_ALIASES.json) | Identity and account mappings with evidence basis and uncertainty |
| [`EVIDENCE_MANIFEST.json`](EVIDENCE_MANIFEST.json) | Machine-readable hashes, sizes, media types, and source URLs for all archived evidence |
| [`METHODOLOGY.md`](METHODOLOGY.md) | Evidence categories, indexing rules, confidence scale, and archive boundaries |
| [`CORRECTIONS.md`](CORRECTIONS.md) | Visible, version-aware correction ledger |
| [`CITATION.cff`](CITATION.cff) | Citation File Format metadata and preferred report citation |
| [`.zenodo.json`](.zenodo.json) | Zenodo report-deposit metadata, ready for a real DOI to be assigned |
| [`RELEASE.md`](RELEASE.md) | Annotated-tag, release, DOI, timestamp, and preservation procedure |
| [`timestamps/`](timestamps/) | Core-file SHA-256 manifest and submitted OpenTimestamps proof |
| [`sources/legal/`](sources/legal/) | Court filings and the FinCEN-disclosure defense letter |
| [`sources/research/`](sources/research/) | OXT report, thesis, and independent CoinJoin studies |
| [`sources/code/`](sources/code/) | Git bundle, exact-commit archives, patches, lineage audit, and cited source |
| [`sources/screenshots/`](sources/screenshots/) | Focused exhibits used in the essay and supplementary verification crops |
| [`sources/social/`](sources/social/) | Public X, Reddit, and profile records |
| [`sources/video/`](sources/video/) | Recording metadata, relevant timestamps, and the complete available Research Club transcript archive |
| [`sources/web/`](sources/web/) | Preserved articles, documentation, discussions, and official pages |
| [`sources/URLS.md`](sources/URLS.md) | Canonical mapping of every essay URL to its local copy |
| [`LEGACY_LINKS.md`](LEGACY_LINKS.md) | Earlier research leads not relied upon by the final essay |

## Verify the archive

Run the checksum verification from the `sources` directory:

```sh
cd sources
sha256sum -c SHA256SUMS
```

The complete ZeroLink history can be inspected without relying on the live GitHub repository:

```sh
git clone sources/code/zerolink-full-history.bundle ZeroLink
```

Verify the joined evidence manifest and the committed canonical edition:

```sh
python tools/build_evidence_manifest.py --check
python tools/build_site.py --check
python tools/build_timestamp_manifest.py --check
```

## Boundaries

The private unpublished memoir used to cross-check the narrative is not committed. Neither is nopara73's parents' street address.

The essay distinguishes allegations, party submissions, government representations, technical records, and independently reproduced facts. The repository preserves third-party material for attribution and verification; its inclusion does not relicense that material under the repository's MIT license.

The older repository collected many useful leads before the final source audit. Those links are retained in [**Legacy research links**](LEGACY_LINKS.md), but their historical labels are not findings and they are not substitutes for the cited primary record.

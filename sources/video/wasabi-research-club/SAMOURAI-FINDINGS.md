# Samourai-related findings in the Wasabi Research Club archive

This index records the portions of the playlist most relevant to the essay. It distinguishes direct architectural evidence from discussion, criticism, and unresolved debate. Timestamps link to the videos; the accompanying Markdown files preserve YouTube's automatic captions exactly as retrieved, including recognition errors.

## Essay disposition

This is a research index, not a parking place for evidence. After rechecking the complete discussions and the available primary code and documentation, the essay now incorporates:

- ZeroLink's scope as a wallet privacy framework;
- the recurring SharedCoin/Samourai operator-knowledge problem;
- Wasabi's public examination of Boltzmann before OXT's August 2020 report, including the metric's limits;
- Whirlpool's `TX0` toxic change and its fixed-denomination pre- and post-mix costs; and
- Ricochet's recognizable hop-chain construction, with the explicit limit that the Research Club deferred a full attack analysis.

Two hypothetical observations remain here rather than being promoted into factual claims in the essay: free remixes can reduce the cost of Sybil participation, and a nominal Whirlpool round may contain chain-analysis clients. Both are valid threat-model questions, but the transcripts do not establish how often either occurred. The essay's adoption argument instead uses reproduced fresh-bitcoin data, and its privacy argument uses the stronger xpub, code, documentation, and seizure evidence.

## Default backends and xpubs

- **A central xpub server was the rejected design ZeroLink existed to avoid.** In [episode 14 at 04:17](https://www.youtube.com/watch?v=8v_apbGPKrI&t=257s), the presentation describes a trusted central server receiving every user's extended public key, calls the idea “obviously” unsound, and proceeds to blinded coordination. [Transcript](transcripts/14-8v_apbGPKrI.md)
- **The SharedCoin comparison omitted that Samourai could learn the same wallet relationships.** In [episode 26 at 55:53](https://www.youtube.com/watch?v=l7bK85obzrM&t=3353s), nopara73 objects to a paper naming Blockchain.info's ability to link SharedCoin inputs and outputs while omitting Samourai's default xpub collection. The discussion also explains why Dojo users can lose effective anonymity by mixing with default-server users known to the operator. [Transcript](transcripts/26-l7bK85obzrM.md)
- **The danger of later seizure was stated in advance.** In [Research Club episode 30 (playlist position 32) at 1:11:55](https://www.youtube.com/watch?v=8L725ufc-58&t=4315s), nopara73 explains that an xpub retained on another computer remains sensitive even when the computer is the user's own node: hacking or physical seizure can expose it. [Transcript](transcripts/32-8L725ufc-58.md)

## Blockchain.info, SharedCoin, and the recurring trust model

- **Everyone analyzing SharedCoin assumed its server knew the links.** [Episode 10 at 30:57](https://www.youtube.com/watch?v=CtmSylCQNIc&t=1857s) says this directly during a discussion of possible server-supplied liquidity. The same episode records that SharedCoin's server repository had disappeared from GitHub and that publication of every production change could not be confirmed. [Transcript](transcripts/10-CtmSylCQNIc.md)
- **The Research Club repeatedly distinguished public transaction ambiguity from privacy against the operator.** [Episode 8 at 1:13:45](https://www.youtube.com/watch?v=bpLOSytc7vc&t=4425s) notes that the Blockchain.info server knew everything even before considering CoinJoin Sudoku's public-chain attack. [Transcript](transcripts/08-bpLOSytc7vc.md)
- **The July 2021 Samourai discussion explicitly joined the histories.** [Episode 26 at 56:24](https://www.youtube.com/watch?v=l7bK85obzrM&t=3384s) moves directly from SharedCoin's server knowledge to Samourai's default xpub knowledge rather than treating them as unrelated wallet designs. [Transcript](transcripts/26-l7bK85obzrM.md)

## ZeroLink's scope

- **ZeroLink was a wallet privacy framework, not simply a name for a CoinJoin shape.** In [episode 26 at 53:47](https://www.youtube.com/watch?v=l7bK85obzrM&t=3227s), nopara73 distinguishes Chaumian CoinJoin from ZeroLink and describes ZeroLink as a broader set of wallet privacy practices. This supports the framework's intellectual scope; the separate Git audit establishes authorship. [Transcript](transcripts/26-l7bK85obzrM.md)
- **The framework document aged unevenly; its blinded CoinJoin core did not.** In [episode 14 at 27:39](https://www.youtube.com/watch?v=8v_apbGPKrI&t=1659s), nopara73 says parts of the broad multi-wallet framework had become outdated while the Chaumian CoinJoin core remained sound. This is useful qualification, not evidence against the central operator-knowledge argument. [Transcript](transcripts/14-8v_apbGPKrI.md)

## OXT, Boltzmann, and privacy metrics

- **Wasabi openly reviewed OXT developer LaurentMT's work before OXT attacked Wasabi.** Episode 11 is an entire session on [Boltzmann](https://www.youtube.com/watch?v=CYIDAqMSc4A). The discussion did not suppress the work; it examined its assumptions and utility. [Transcript](transcripts/11-CYIDAqMSc4A.md)
- **The metric had already drawn a conceptual criticism.** [Episode 8 at 44:12](https://www.youtube.com/watch?v=bpLOSytc7vc&t=2652s) identifies a weakness in treating partition entropy as individual-user privacy, especially when targeted observers can combine network and transaction-graph information. [Transcript](transcripts/08-bpLOSytc7vc.md)
- **Its practical use for large Wasabi transactions was limited.** [Episode 11 at 40:23](https://www.youtube.com/watch?v=CYIDAqMSc4A&t=2423s) says anonymity set is a clearer user-facing heuristic and notes that the partition computation is infeasible at Wasabi scale. This does not make Boltzmann fraudulent; it limits what its score can establish. [Transcript](transcripts/11-CYIDAqMSc4A.md)

## Whirlpool claims and economics

- **“Free remixes” also make Sybil participation cheap.** In [episode 22 at 1:27:02](https://www.youtube.com/watch?v=_ZDungWdxzk&t=5222s), the discussion observes that after the one-time entry fee, a coordinator or adversary can keep outputs remixing while paying only mining fees. [Transcript](transcripts/22-_ZDungWdxzk.md)
- **A high nominal anonymity set cannot guarantee honest counterparties.** In the toxic-change panel, [at 55:51](https://www.youtube.com/watch?v=Zu-bT9XojYk&t=3351s), a participant explains that much of a Whirlpool round could be chain analysis operating modified clients and calls promises of perfect unlinkability dishonest. [Transcript](transcripts/34-Zu-bT9XojYk.md)
- **Moving change into `TX0` does not by itself erase its link to the first mix.** The same panel, [at 50:33](https://www.youtube.com/watch?v=Zu-bT9XojYk&t=3033s), argues that peeling change before the CoinJoin rather than creating it during the CoinJoin makes no inherent difference to the on-chain link under comparison. [Transcript](transcripts/34-Zu-bT9XojYk.md)
- **Fixed denominations create visible pre- and post-mix costs.** [At 1:05:10](https://www.youtube.com/watch?v=Zu-bT9XojYk&t=3910s), the panel contrasts Whirlpool's public `TX0` input consolidation with Wasabi 1's coordinator-visible consolidation; [at 1:06:11](https://www.youtube.com/watch?v=Zu-bT9XojYk&t=3971s), it explains why arbitrary payments often force post-mix consolidation and change. [Transcript](transcripts/34-Zu-bT9XojYk.md)

These Whirlpool discussions are evidence against treating remix counts, fixed denominations, or marketing certainty as proof of achieved privacy. They are not substitutes for the stronger backend evidence: the source code, Samourai documentation, and seized-server record establish the xpub trust problem directly.

## Other product observations

- **Ricochet was described as having a unique on-chain fingerprint.** A brief exchange in [episode 8 at 1:25:04](https://www.youtube.com/watch?v=bpLOSytc7vc&t=5104s) raises Ricochet as a possible anti-flagging tool and receives the objection that it is uniquely recognizable on-chain. The subject was deferred rather than fully analyzed, so the essay does not rely on it. [Transcript](transcripts/08-bpLOSytc7vc.md)

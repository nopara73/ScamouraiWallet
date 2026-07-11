# Legacy research links

This is the repository's earlier research trail. These links are retained so leads are not lost, but they were not all used in the final post-mortem and many were not independently archived. The short descriptions identify the issue under discussion; they are navigation aids, not findings.

For the sources actually cited by the essay, use the [complete citation inventory](sources/URLS.md).

## Security and implementation

- [**Random.org appeared in a William Hill-attributed Android wallet component.**](https://github.com/jisqyv/Android-Wallet-2-App/blob/dfb781c05536db58eb253ab5c37b82c237213382/src/piuk/blockchain/android/util/RandomOrgGenerator.java)
- [**Samourai issue #381 tracked the PIN-bypass vulnerability.**](https://github.com/Samourai-Wallet/samourai-wallet-android/issues/381)
- [**The independent PIN-bypass disclosure includes the exploit and timeline.**](https://vrls.ws/posts/2021/08/samourai-wallet-bitcoin-pin-authentication-bypass-crypto/)
- [**Bitcointalk users discussed a later PIN attack report.**](https://bitcointalk.org/index.php?topic=5471645.0)
- [**WalletScrutiny tracked whether Samourai releases reproduced from source.**](https://walletscrutiny.com/android/com.samourai.wallet/)
- [**Bitcoin Design notes preserve broader wallet-design discussion.**](https://hackmd.io/@BitcoinDesign/rym2ehCSd)

## Earlier articles and first-person reports

- [**SamouraiLeaks Part 1 documents the foneBTC sockpuppet trail.**](https://nopara73.medium.com/samouraileaks-samouraidevs-sockpuppet-exposed-7ce654b92c0b)
- [**SamouraiLeaks Part 3 traces the Random.org implementation history.**](https://nopara73.medium.com/samouraileaks-part-3-is-random-org-random-enough-35704796ae93)
- [**A user recorded an unexplained experience with Samourai.**](https://bitcointalk.org/index.php?topic=5562148.msg65914017#msg65914017)
- [**The Bitcoin Bugle satirized Samourai's attack-oriented marketing.**](https://www.thebitcoinbugle.com/samourai-wallets-marketing-strategy-similar-to-soccer-flops/)

## Developer criticism and the response to critics

- [**Gregory Maxwell criticized the default backend's address disclosure.**](https://www.reddit.com/r/Bitcoin/comments/9r9344/comment/e8fm1v8/)
- [**Chris Belcher explained how default-server users weaken mixed Dojo rounds.**](https://twitter.com/chris_belcher_/status/1286640749082271744)
- [**Chris Belcher continued the RNG and implementation critique.**](https://twitter.com/chris_belcher_/status/1300022468271366144)
- [**Chris Belcher summarized the Random.org concern.**](https://twitter.com/chris_belcher_/status/1356299408464293888)
- [**BashCo disputed Samourai's promotion and moderation tactics.**](https://twitter.com/BashCo_/status/1298711774951137282)
- [**BashCo preserved an earlier Random.org criticism.**](https://twitter.com/BashCo_/status/1291633872048926721)
- [**Vlad Costea described retaliation after criticizing Samourai.**](https://twitter.com/TheVladCostea/status/1298771143655124993)
- [**Warren Togami pointed back to the Android wallet vulnerability.**](https://twitter.com/wtogami/status/1122161807639007232)
- [**Michael Folkson highlighted the Android wallet bug record.**](https://twitter.com/michaelfolkson/status/1300144713656414209)
- [**Nicolas Dorier commented on Android randomness failures.**](https://twitter.com/NicolasDorier/status/1410504884458196993)
- [**Peter Todd commented on the claimed randomness source.**](https://twitter.com/peterktodd/status/1585996437783183363)
- [**Eric Sirion discussed the wallet RNG controversy.**](https://twitter.com/EricSirion/status/1494436823036272640)
- [**Luke Dashjr added a later public criticism of Samourai.**](https://twitter.com/LukeDashjr/status/1732597621015949494)

## Community audit trail

- [**AsILayHodling raised a security issue that spread beyond the original report.**](https://twitter.com/AsILayHodling/status/1267469894217596928)
- [**BTCparadigm amplified the RNG concern.**](https://twitter.com/BTCparadigm/status/1267556260255334401)
- [**BTCparadigm returned to the issue in a later thread.**](https://twitter.com/BTCparadigm/status/1587570194058252290)
- [**HODLHanger discussed the reported bug.**](https://twitter.com/HODLHanger/status/1271152444462989312)
- [**Deafboy_2v1 highlighted the default-backend privacy leak.**](https://twitter.com/Deafboy_2v1/status/1257260614856118273)
- [**ob_hodl circulated the Android vulnerability record.**](https://twitter.com/ob_hodl/status/1300429481711153152)
- [**C_ruhf discussed Android seed generation.**](https://twitter.com/C_ruhf/status/1309036193741451264)
- [**theinstagibbs discussed the PIN-bypass exploit.**](https://twitter.com/theinstagibbs/status/1166735204968521728)
- [**btcdragonlord recorded an early bug report.**](https://twitter.com/btcdragonlord/status/1313160864938291200)
- [**btcdragonlord followed with additional analysis.**](https://twitter.com/btcdragonlord/status/1325093604398919680)
- [**Coinosphere questioned the RNG design.**](https://twitter.com/Coinosphere/status/1326436740169609216)
- [**BTC05349283 criticized the randomization method.**](https://twitter.com/BTC05349283/status/1301494872784998401)
- [**snaxion discussed the RNG library choice.**](https://twitter.com/snaxion/status/1642337824820305922)
- [**Mandrik discussed the PIN bypass.**](https://twitter.com/Mandrik/status/1376555483520233474)
- [**Mandrik returned with later analysis.**](https://twitter.com/Mandrik/status/1602688050357846021)
- [**ersolus summarized an RNG audit.**](https://twitter.com/ersolus/status/1631997876682346497)
- [**Yahiheb questioned the privacy design.**](https://twitter.com/yahiheb_/status/1587063750326108164)
- [**Yahiheb discussed how the issue escaped earlier review.**](https://twitter.com/yahiheb_/status/1587119284471439362)
- [**Yahiheb added a separate critique.**](https://twitter.com/yahiheb_/status/1586559494338871296)
- [**Yahiheb posted a later assessment.**](https://twitter.com/yahiheb_/status/1588319800912412673)
- [**Yahiheb summarized later audit results.**](https://twitter.com/yahiheb_/status/1634815352222744576)
- [**OomaHQ discussed application-analysis findings.**](https://twitter.com/oomahq/status/1733496982834991436)
- [**verysmallclaims posted a security retrospective.**](https://twitter.com/verysmallclaims/status/1734085553329479782)
- [**Douglas Tuman posted a later evaluation.**](https://twitter.com/DouglasTuman/status/1770951163770273920)
- [**1440000bytes revisited the RNG history.**](https://x.com/1440000bytes/status/1847705683367797204)
- [**LaurentMT added a later research comment.**](https://x.com/LaurentMT/status/1733111061572735337)

## Dispute chronology and public reactions

- [**nopara73 recorded early RNG findings.**](https://twitter.com/nopara73/status/1083782139278213120)
- [**nopara73 linked the later Medium investigation.**](https://twitter.com/nopara73/status/1409554739369431041)
- [**nopara73 recorded the dispute immediately before the 2023 threats.**](https://twitter.com/nopara73/status/1647436989871042560)
- [**nopara73 publicly documented receiving a death threat.**](https://twitter.com/nopara73/status/1647489516939382784)
- [**thefuckisalommy reacted to the Samourai criticism.**](https://twitter.com/thefuckisalommy/status/1409534871538700294)
- [**brian_trollz discussed the wallet RNG.**](https://twitter.com/brian_trollz/status/1389022575125217284)
- [**brian_trollz commented on the earlier leak investigation.**](https://twitter.com/brian_trollz/status/1337876220172754946)
- [**brian_trollz recalled Samourai's shift from implementation talk to mockery.**](https://twitter.com/brian_trollz/status/1313283715188088838)
- [**Tuur Demeester commented on the early RNG dispute.**](https://twitter.com/TuurDemeester/status/1058485499348815872)
- [**The official Samourai account responded publicly during the controversy.**](https://twitter.com/SamouraiWallet/status/1376313082658496516)

## Forums, recordings, and image collections

- [**JoinMarket developers compared the Wasabi and Samourai trust models.**](https://old.reddit.com/r/Bitcoin/comments/zpnug5/joinmarket_dev_wasabi_vs_samourai/)
- [**The Blockchain.info Android thread records the predecessor wallet's cryptographic failure.**](https://www.reddit.com/r/Bitcoin/comments/37oxow/the_security_issue_of_blockchaininfos_android/)
- [**A Reddit thread preserves further implementation criticism.**](https://www.reddit.com/r/Bitcoin/comments/iy26iw/comment/g6dz562)
- [**A second Reddit comment preserves contemporary community context.**](https://www.reddit.com/r/Bitcoin/comments/pz59a0/comment/heyrrw2/)
- [**The BlockDigest discussion covers Samourai review and security questions.**](https://www.youtube.com/watch?v=_Z5SwEnTOsU&t=3470s&ab_channel=BlockDigest)
- [**The Tor-identity exchange preserves a categorical claim later contradicted by code.**](https://imgur.com/a/XgushDQ)
- [**The official-account gallery preserves attacks on critics.**](https://imgur.com/a/uSDlT6C)

## Academic background

- [**The 2022 thesis compares CoinJoin implementations and the default-backend trust model.**](https://is.muni.cz/th/kbvx1/Master_Thesis.pdf)

## Legal lead

- [**The 2025 superseding indictment alleges Dread marketing through purportedly independent accounts.**](https://storage.courtlistener.com/recap/gov.uscourts.nysd.620167/gov.uscourts.nysd.620167.109.0.pdf) These were allegations when filed; later procedural records are separated in the [canonical inventory](sources/URLS.md).

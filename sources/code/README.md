# Code evidence

- `zerolink-full-history.bundle` — complete ZeroLink Git history, including every branch and tag available from the public repository on July 10, 2026.
- `zerolink-25d1502-publication-snapshot.zip` — complete tree at the August 14, 2017 publication commit used for the authorship comparison.
- `zerolink-8fbdcb9-fix-typos.patch` and `zerolink-25d1502-publication.patch` — portable patches for two commits cited directly in the essay.
- `samourai-wallet-android-c71f21a-cited-files.zip` — the license and cited Android files at commit `c71f21a631bbc69db2bd411f2905c7f141d1523f`, including the wallet defaults, xpub paths, and Ricochet hop construction.
- `samourai-wallet-android-4bf9870-cited-files.zip` — the license and four cited Android files at commit `4bf98700485879b1c4080e6a2e2f7d4ecbf24163`, merged four days before the October 2022 “full node wallet” post; the files preserve the default Samourai-backend selection and xpub request path.
- `sentinel-android-cf46177-cited-files.zip` — the license and cited Sentinel v3-era files at commit `cf4617753168198b9816506b1a25f7bdd65ec207`.
- `sentinel-android-b5ef29c-cited-files.zip` — the license and cited final pre-seizure mirror files at commit `b5ef29c14adbd65bb596f60856c8e5129cdcf000`.
- `sentinel-77eca1d-move-xpub-to-samourai-api.patch` and `sentinel-1a4722f-add-tor.patch` — the two Sentinel changes discussed in the essay.
- `whirlpool-fbee9e8-change-tor-identity.patch` — the Whirlpool client identity-change commit.
- `whirlpool-server-cited-files.zip` — the official Whirlpool server README and license at commit `f23c2d3a49ce7c2fb3bc82c06c6284a6bd37cea0`, preserving the fixed-denomination, `TX0` fee, and mix configuration cited in the essay.
- `randomorggenerator-dfb781c.java` — the historical Random.org generator at the exact cited commit.
- `blockchain-samourai-lineage.md` — reproducible audit of Hill and Rodriguez's Blockchain.info Android roles, Samourai's delayed source publication, and the narrow source-lineage claims used in the essay.
- `blockchain-android-9f4e200-cited-files.zip` and `samourai-android-c6274d1-lineage-files.zip` — exact-commit files compared in that audit.
- `blockchain-android-4063b3a-sharedcoin-ui.patch` — Hill's September 2014 “UI prep for shared coin” change from the Blockchain.info Android repository.
- `dumplings-adoption-audit.md` — reproducible fresh-bitcoin comparison showing Wasabi ahead of Whirlpool in every month of the shared April 2019–August 2022 period.
- `dumplings-36f28f2-adoption-files.7z` — the exact Dumplings README and Wasabi/Whirlpool fresh-bitcoin inputs at commit `36f28f2`; unrelated CoinJoin datasets are excluded.

ZIP files were created with `git archive`, so their content comes directly from the named Git objects rather than the working tree.

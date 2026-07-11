# Blockchain.info Android to Samourai source-lineage audit

This note records the narrow, reproducible source-history claims used in the essay. It does not claim that William Hill or Keonne Rodriguez founded Blockchain.info, its original web wallet, or its first Android codebase. It establishes their roles in Blockchain.info's 2014 `Android-Wallet-2-App` relaunch and the visible lineage between that client and Samourai's first published source snapshot.

## Blockchain.info's `Android-Wallet-2-App`

The surviving [`jisqyv/Android-Wallet-2-App`](https://github.com/jisqyv/Android-Wallet-2-App) mirror preserves merge messages naming the original upstream as `github.com/blockchain/Android-Wallet-2-App`.

- The repository begins with William Hill's April 30, 2014 [`9f4e200` "Initial commit"](https://github.com/jisqyv/Android-Wallet-2-App/commit/9f4e200c7359f6aa687631c9674bc82050a13b0b).
- Across all preserved refs, `git shortlog -sne --all` attributes 349 commits to `WilliamHill <william.hill@gmail.com>` and another three to `William Hill <h@cker.mobi>`. The next largest author has 189. Commit counts do not prove sole authorship, but they rule out describing Hill as an incidental contributor.
- Hill's September 10, 2014 [`4063b3a` commit](https://github.com/jisqyv/Android-Wallet-2-App/commit/4063b3a935afc377a8351656dfcf9f7cf95e52ce) is titled `UI prep for shared coin` and modifies the wallet's send interface. The exact patch is archived as [`blockchain-android-4063b3a-sharedcoin-ui.patch`](blockchain-android-4063b3a-sharedcoin-ui.patch).
- A contemporary interview identifies Keonne Rodriguez as Blockchain.info's product lead responsible for the refreshed wallet family's UI and UX: [John Scianna, "The Future of Blockchain.info"](https://bitcoinist.com/the-future-of-blockchain-info/amp/).
- Hill's own sentencing submission describes his two years at Blockchain.com as its "Senior Mobile Developer" and says he met Rodriguez there. See ECF No. 155, pp. 21-22 of the submission (PDF pp. 26-27).

The initial commit is a large import and its own README points back to the earlier `blockchain/My-Wallet-Android`; its inherited `AUTHORS` file credits Andreas Schildbach and translators. The precise claim is therefore that Hill led the visible `Android-Wallet-2-App` repository and Rodriguez led the product relaunch, not that they created Blockchain.info or every ancestor of its Android client from nothing.

## Samourai's first published snapshot

Samourai's public repository begins on March 30, 2016 with TDevD's [`c6274d1` "Initial source code commit & license"](https://github.com/Samourai-Wallet/samourai-wallet-android/commit/c6274d19b543a29edd46864d251bc56ee3510288). Contemporary coverage quotes Samourai saying it had deliberately delayed open-sourcing for about a year to obtain a competitive advantage: ["Bitcoin Wallet Samourai Goes Open-Source"](https://www.ccn.com/samourai-bitcoin-wallet-goes-open-source/).

The published snapshot has unmistakable source lineage from the Blockchain.info Android code. Examples at the two commits above include:

- `piuk/BitcoinScript.java` becoming `com/samourai/wallet/send/BitcoinScript.java`;
- `piuk/BitcoinAddress.java` becoming `com/samourai/wallet/send/BitcoinAddress.java`;
- `piuk/Hash.java` becoming `com/samourai/wallet/util/Hash.java`; and
- `info/blockchain/wallet/ui/OnSwipeTouchListener.java` becoming `com/samourai/wallet/OnSwipeTouchListener.java`.

After comments, imports, package names, and whitespace are normalized, the paired `BitcoinScript` files share 345 unique source lines (93.8 percent of the smaller file's unique lines), while `OnSwipeTouchListener` is detected by Git as a 96 percent rename. This is a focused lineage check, not a claim that every Samourai file came from Blockchain.info.

The exact cited files are preserved in [`blockchain-android-9f4e200-cited-files.zip`](blockchain-android-9f4e200-cited-files.zip) and [`samourai-android-c6274d1-lineage-files.zip`](samourai-android-c6274d1-lineage-files.zip).

## Reproduction commands

```console
git clone --mirror https://github.com/jisqyv/Android-Wallet-2-App.git blockchain-android.git
git clone --mirror https://github.com/Samourai-Wallet/samourai-wallet-android.git samourai-android.git
git --git-dir=blockchain-android.git rev-list --max-parents=0 --all
git --git-dir=blockchain-android.git shortlog -sne --all
git --git-dir=blockchain-android.git show --stat 4063b3a935afc377a8351656dfcf9f7cf95e52ce
git --git-dir=samourai-android.git rev-list --max-parents=0 --all
```

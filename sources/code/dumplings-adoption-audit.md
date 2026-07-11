# Dumplings fresh-bitcoin adoption audit

This note reproduces the narrow comparison used in the essay. It does not treat bitcoin volume as an exact count of users.

## Source

- Repository: [`nopara73/Dumplings`](https://github.com/nopara73/Dumplings)
- Commit: [`36f28f27ab3753211acdbf9dde09ceb760ee834b`](https://github.com/nopara73/Dumplings/commit/36f28f27ab3753211acdbf9dde09ceb760ee834b)
- Files: `Dumplings/Freshbitcoins/freshwasabi.txt` and `Dumplings/Freshbitcoins/freshsamuri.txt`
- Local archive: [`dumplings-36f28f2-adoption-files.7z`](dumplings-36f28f2-adoption-files.7z)

Dumplings defines `FreshBitcoins` as non-remixed bitcoin entering recognized CoinJoin transactions and calls it the best available on-chain proxy for user adoption. Its label `Samuri` means Samourai Wallet Whirlpool.

## Calculation

Each record begins with a .NET timestamp in ticks and ends with a BTC amount. The audit:

1. converted the timestamp to its UTC year and month;
2. summed the final BTC amount by month and implementation;
3. began with the first month containing a Whirlpool observation, April 2019; and
4. ended at the common dataset endpoint, August 2022.

| Result | Wasabi | Whirlpool |
| --- | ---: | ---: |
| Fresh BTC | 247,675.31 | 30,228.14 |
| Months with the higher total | 41 | 0 |

Across the forty-one months, Wasabi's fresh-bitcoin volume was 8.19 times Whirlpool's. The monthly lead ranged from 1.2 times in Whirlpool's two closest months to much larger multiples earlier in the period.

## Limit

Fresh-bitcoin volume is not a count of installations, wallets, or human beings. A single large holder can move more bitcoin than many small holders. It is nevertheless more suitable than total CoinJoin transaction count for this comparison because it excludes repeated remixes of the same bitcoin—the mechanism that otherwise inflates Whirlpool's visible activity.

The chart embedded in the essay is the original `Fresh Bitcoins CoinJoined` chart from the repository README. That static chart ends in November 2021; the committed data files continue through August 2022 and produce the totals above.

Title: Statement regarding atomic swaps and Twitter mobs.

URL Source: http://medium.com/@SamouraiWallet/statement-regarding-atomic-swaps-and-twitter-mobs-7a3430f0253a

Published Time: 2021-07-01T14:02:52Z

Markdown Content:
[![Image 1: Samourai Wallet](https://miro.medium.com/v2/resize:fill:32:32/0*XDO5JlThcSCx9WVv.png)](https://medium.com/@SamouraiWallet?source=---byline--7a3430f0253a---------------------------------------)

5 min read

Jul 1, 2021

On June 30 Bitcoin Twitter influencer Giacomo Zucco [published a short tweet thread](https://archive.is/01PNc) to his followers with very strong implications. In the thread Zucco strongly implies that Samourai Wallet has been **_compromised_** (presumably by a State actor) and should be avoided.

To back up this assertion Zucco provides for evidence a screenshot dated 01 Oct 2018 from the official @SamouraiWallet twitter account stating _“If you ever see alts in Samourai Wallet we have been compromised”_. Next to this was a screenshot dated 25 Jun 2021 from the same account answering a user question quoted _“Yep, we’re working on atomic swap functionality with XMR”_.

![Image 2](https://miro.medium.com/v2/resize:fit:598/1*x0HOfzxJPKRfSXS7fmCSzw.png)

To Zucco, this single tweet was enough evidence to provide solid proof that Samourai has been _compromised_ and he tweeted to his large twitter following.

**We strongly, categorically and unequivocally deny this allegation.**

## The Samourai Canary

In 2015 recognizing the dangers of instruments like National Security Letters and other “legal” methods the state uses to surveil their citizens and violate their rights, we created our Warrant Canary [[https://samouraiwallet.com/canary](https://samouraiwallet.com/canary)]. The Warrant Canary was designed based on the proposals of Steven Schear to the Cypherpunks Mailing List in 2002. We later modified the Canary policy based on the OMG (Onion Mirror Guidelines), and furthermore we have open sourced this code so others can easily implement their own canary systems [[https://code.samourai.io/walletguy/omg-py](https://code.samourai.io/walletguy/omg-py)]

The canary is a message that includes the latest bitcoin block hash and a statement that no warrants, letters, or requests for information have been received or complied with. This statement is then signed by the PGP key that is both known by the community to belong to the Administrators of Samourai. [[https://samouraiwallet.com/pgp](https://samouraiwallet.com/pgp)]

The Canary has been maintained and signed with the same key since inception usually being reissued and resigned on a monthly basis.

![Image 3](https://miro.medium.com/v2/resize:fit:645/1*u8Bqy8Uic_4AvkLVSieK_Q.png)

**The last time the canary was issued and signed was June 03 2021. If the Canary lapsed users should rightfully worry, but the canary hasn’t lapsed, nor has it ever lapsed since inception**.

## The Atomic Swap

In April 2021 we announced at the Bear Arms & Bitcoin conference in Austin, TX that we intended to launch a feature within Samourai Wallet that would allow users to swap their unmixed “toxic change” from Whirlpool CoinJoin transactions into the Monero blockchain and back to Bitcoin all in a non custodial way.

We clearly emphasized that Samourai Wallet would continue to only support BTC and the user would not be able to interact with XMR within Samourai Wallet. The XMR side of the swap will still need to be handled by wallet developers within the Monero ecosystem.

## Get Samourai Wallet’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

At the end of April 2021 we again reiterated how the architecture of this feature would work, this time publicly on Twitter. [https://twitter.com/SamouraiWallet/status/1388112294828183553?s=20](https://twitter.com/SamouraiWallet/status/1388112294828183553?s=20)

![Image 4](https://miro.medium.com/v2/resize:fit:598/1*zxf7M_n_lke7z_B8z8Gh8Q.png)

In May 2021 a news article was released by Kyle Torpey who had interviewed Samourai Lead Developer TDevD. Again reiterating how this feature would be implemented

> “However, according to TDevD, Samourai Wallet itself will remain a BTC-only wallet solution, and users will need to use a separate wallet for handling Monero.”
> 
> [**https://cryptonews.com/exclusives/taproot-coinswap-mercury-wallet-and-the-state-of-bitcoin-pri-10508.htm**](https://cryptonews.com/exclusives/taproot-coinswap-mercury-wallet-and-the-state-of-bitcoin-pri-10508.htm)

## Examining The Evidence

As evidence of Samourai being compromised Zucco provides two tweets. His assertion rests on the idea that Samourai is implementing the XMR token into Samourai Wallet, thus based on our own tweet we are compromised.

As has been announced at [a] in-person events, [b] in the press, and [c] publicly on Twitter since March 2021, Samourai Wallet will remain a BTC only wallet, it is only facilitating the BTC side of a BTC<=>XMR swap. Users will not see nor interact with XMR in Samourai Wallet, and the Monero community is responsible for implementing needed infrastructure within their wallet software.

Perhaps Zucco missed all these descriptions of the feature before he published his factually incorrect tweet, but once he was made aware of his error by respected journalist Kyle Torpey, his response was to double down and continue warning users that the only serious privacy wallet in the Bitcoin space was compromised not based on evidence, but on his feelings.

![Image 5](https://miro.medium.com/v2/resize:fit:598/1*Q7ttovcCCYj5qDFAEuEFyg.png)

At this point the only thing we can do is present our side of the story in this statement and hope that truth will ultimately overcome malicious intent and lies.

## Conclusion

The reason we have been against a multi-coin wallet architecture from the very beginning of our development is not blind maximalisim. That tribe of Bitcoin didn’t really make an appearance until the 2016 cycle. Our belief that the best products come from laser focus and passion.

Bitcoin has been the outlet of our focus and passion since 2013. We have invested a considerable amount of hard work into creating an entire software stack on Bitcoin and we our proud of our accomplishments to date.

Our mission is to create software that empowers the individual. We have worked tirelessly to maintain the dual wielded principles of self sovereignty and user privacy in every decision we make from the architecture to the deployment of our Free Open Source Software.

We strongly believe that providing the ability to hop back and forth between the Bitcoin blockchain and the Monero blockchain without counter party risk, without KYC, without a middleman, without permission is simply adding valuable tools to our users tool-belt. And in this asymmetric fight where the individual is the smallest minority, **every tool matters.**

Sadly as is now the case within the wider net of society, “cancel culture” has reached the Bitcoin subculture and influencers cannot resist sensationalist misleading declarations using their new found relevance. Truth is flexible in a community that sustains itself on outrage. Over the last 24 hours there have been various calls for our cancellation.

Unlike most we will not bow and surrender to the frenzy of a stirred up mob. We have absolutely nothing to apologize for. We believe our users will continue to be well served by our entire product and feature road map of which atomic swaps are only a single component of.

On a brighter note, we welcome all the new users who are installing Samourai Wallet for the first time and are entering their first Whirlpool CoinJoin.

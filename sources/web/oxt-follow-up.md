Title: An update on the disclosed vulnerabilities in Wasabi Wallet

URL Source: http://medium.com/oxt-research/an-update-on-the-disclosed-vulnerabilities-in-wasabi-wallet-4ac0e228acb9

Published Time: 2020-08-28T21:04:27Z

Markdown Content:
[![Image 1: Samourai Wallet](https://miro.medium.com/v2/resize:fill:32:32/0*XDO5JlThcSCx9WVv.png)](https://medium.com/@SamouraiWallet?source=post_page---byline--4ac0e228acb9---------------------------------------)

7 min read

Aug 28, 2020

--

--

Since the publication of our [full disclosure](https://research.oxt.me/alerts/2020/08/21/Wasabi-Wallet), some Wasabi Wallet maintainers and commentators have posted various reactions on social media. Generally, these comments either refute the existence of the vulnerability, dispute its severity, or propose “user best practices” as a mitigation.

This post aggregates the various responses and includes our comments to the relevant points.

We have also seen a few “emotional” reactions that mostly misrepresent our disclosure by ignoring the technical contents. We won’t address these comments in this post.

### “It isn’t a vulnerability. It can’t be exploited.”

This response is largely based on the assertion that an attacker cannot know the TXOs controlled by a wallet at the start of the attack. Some find this assumption completely unrealistic or believe that it requires capabilities beyond the reach of any adversary. The reality on the ground does not support such a definitive statement.

Users make use of bitcoin and mixers for a host of reasons, resulting in greatly varying wallet compositions and patterns of use. For example, the use cases of a hacker seeking to obfuscate a source of funds and a trader mixing before transferring to a regulated exchange or cold storage are vastly different.

Additionally, the abilities of each users perceived adversary vary greatly and are largely unknown. The most powerful adversaries are not publishing or detailing the vulnerabilities they are actively exploiting.

However, there are some clear observable trends about the abilities of possible adversaries:

*   Several years ago, an on-chain analyst had nothing more than access to a standard block explorer. These simpler times are largely behind us as evidenced by the numerous criminal fillings prepared by analysts for Law Enforcement agencies in recent months.
*   Although the advances of privacy-enhancing tools has continued, the bitcoin transaction graph remains extremely transparent and damaging, even to “sophisticated” users. ([See OXT Research reporting on the PlusToken ponzi scheme](https://research.oxt.me/special-situation-report)).
*   Law Enforcement is actively cooperating across multiple jurisdictions. Resulting in a growing number of entities having access to large volumes of pooled user data and shared knowledge.
*   Multiple blockchain surveillance firms are collaborating with “compliant” exchanges. It’s only a matter of time before all this “anonymized” data becomes available to some adversaries.

For all these reasons, considering the premix activity of a wallet as “unknown” to a potential adversary is unreasonably optimistic and not a satisfactory solution. We believe this vulnerability is within the capabilities of a growing number of adversaries.

### “It isn’t a vulnerability. Exogenous randomness fixes this.”

Some have expressed doubts about the possibility of exploiting such an attack in the real world due to unpredictable external random factors that complicate the analysis.

Far be it for us to dismiss these comments altogether, in fact half of the analysis we passed on to ZkSnacks LTD is devoted to this topic. We will not repeat all the details already given in [the report](https://research.oxt.me/alerts/2020/08/21/Wasabi-Wallet)but will summarize our three main issues with this conclusion below:

*   From our observations, the main source of exogenous randomness during our tests resulted from temporary scalability issues related to the Wasabi coordinator.It’s hard to consider these issues as satisfactory solutions since that would imply that any fix of these issues is an attack on user privacy. It is also our opinion that other external factors such as intermittent network problems are not satisfactory solutions as they are factors that the user generally seeks to eliminate.
*   Another source of external randomness identified by our analysis is the user himself. We don’t deny the existence of this randomness, but we do not consider it a satisfactory solution. Mostly because humans are notoriously poor at mimicking randomness, but above all because an effective solution would amount to asking the user to manually manage each mixing round. This approach would have a significant impact on the overall activity of the mixer _(eg. users used to leaving their Wasabi client running automatically overnight)_. It is our opinion that relying on the user to provide sufficient randomness should only be considered once all technical options have been exhausted.
*   The vulnerability also creates a unique issue well outside any users control: the technical logs of the Wasabi coordinator.The coordinator logs act as the best record possibly available to an adversary for mitigating any uncertainty that is not generated by the user. This status does not appear to be compatible with the current threat model emphasized by ZkSnacks LTD.

![Image 2](https://miro.medium.com/v2/resize:fit:593/1*8NzL5nwQOtm4gyaQKRBNnQ.png)

In summary, we believe that a satisfactory solution to mitigate this vulnerability should be reliable over time and its responsibility should not rest on the end user.

### “It isn’t a vulnerability. Risks can be mitigated with best practices enforced by users.”

As we have noted above, we do not believe relying on user induced randomness is a satisfactory solution, either for the user or the operator of the service.

## Get Samourai Wallet’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

As a side note, if some think the vulnerability does not exist, no “best practice” should be necessary.

### “It’s a vulnerability but it isn’t severe”

We have considered this vulnerability as serious and in need of an immediate fix for the following reasons:

*   The introduction of randomness in the selection of inputs composing a mix should be considered necessary for a sufficient mixer, particularly for privacy systems operating on the principal of mixing rounds.
*   The vulnerability could result in rare cases of extreme degradation of Anonymity Set, particularly if a user’s final mix is “[low liquidity](https://www.kycp.org/#/9035306130415c91b7144e977097a7abe150aaf554046390ec48a8e61d051c9c)”.
*   We have not checked all the versions of the client, but the deterministic coin selection algorithm seems to have been present for a long time. We believe that if we have been able to detect it, it is likely that other actors have it too identified before us.
*   A Europol document from April 2020 identifies Wasabi as a target of interest and mentions “promising technical research into behavior and de-mixing of Wasabi transactions”. The description given is too succinct to be able to state the exact approach followed by the Dutch FIOD, but it appears to be in line with an attack based on system idiosyncrasies, such as the one described in our disclosure.

Press enter or click to view image in full size

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*AJqR-NYxRGhdHOzU6u282A.png)

Dutch FIOD — “promising technical research into behavior and de-mixing of Wasabi transactions”

### “It isn’t a vulnerability. It’s fierce competition between two companies.”

This last point is very often presented in comments and implies that, the disclosure was solely motivated by a conflict of interest due to the proximity of OXT Research and Samourai Wallet.

Our response to this objection is that this “conflict of interest” is in every way identical to the case of a hardware wallet manufacturer reporting a vulnerability detected in a competitor’s product. The connection between OXT Research and Samourai Wallet is no secret.

OXT Research is not a clandestine organization plotting dark projects in the shadows. Its mission is to be a sparring partner for Samourai Wallet, to challenge its tools and to suggest directions for improvement.

The analysis of competing open source solutions whose design choices are similar to the tools developed by Samourai Wallet obviously plays an important role in this task because it makes it possible to validate the relevance of the choices made by all.

But the activity of OXT Research is far from being limited to this task. In fact, a large part of the work carried out relates to the analysis of on-chain bitcoin activity in general, because the scope of the tools developed by Samourai Wallet is not limited to Whirlpool, its mixing service.

Finally, as incredible as it may seem to some, one last directive of OXT Research consists of trying to “attack” directly the tools developed by Samourai Wallet.

## First Principles

The evaluations and recommendations made by OXT Research are based on a few simple principles, including:

**Privacy isn’t about anonymity.** Anonymity is a means to an end. Privacy is about you being in control. You making your own choices according to your very specific situation. Not someone else. Not a black-box AI. YOU.

**Reliably protecting your privacy in a digital world is a daunting task**because all details matter. Human are not fit for the task. The cognitive load is far beyond what a human being is able to manage, especially when the adversary is a computer crunching large volumes of public data. Only another computer can help to address this challenge.

**It’s never easy to evaluate the impact of a “small” privacy leak**because privacy leaks are cumulative and in the worst case a single misstep is enough to reveal information that you don’t want to disclose. Adversarial thinking is your friend.

**Engineering practice is composed of three complementary tasks:**

1.   Building the system
2.   Considering and identifying the limitations of the system, the boundaries between which it can be used and operated safely
3.   Communicating effectively information about these limitations to people who will interact with the system.

**A system doesn’t have to be perfect** (they never are) but whatever is built, these three engineering facets are absolutely required. Absent a single one, and you risk losing control.

**Unpredictable problems will occur.** When they happen, you have two options, either modify the system to mitigate the issue or adapt the model of its limitations/risks and communicate this new model to people interacting with the system.

## Epilogue

In conclusion, we believe the vulnerability is high/critical for the following reasons:

*   The theoretical aspects of the vulnerability have been confirmed and our tests have confirmed that it’s possible to exploit it.
*   Adversaries have more access to user data and powerful tools than ever before and they will continue to put effort into improving their tools.
*   Privacy service maintainers should stay “one step ahead” by continuously improving their services.
*   The default software behavior should be responsible for maintaining the guarantees of a service, not the end user.

The only way for bitcoin privacy to advance is a process of acknowledging the shortcoming of existing tools and improving them. OXT Research will continue its efforts to improve the bitcoin privacy space.

— The OXT Research Team

# Wasabi Research Club #22 - Discrete Log Contract Specification with Nadav Kohen & Benthecarman

- Playlist index: 22
- YouTube ID: `_ZDungWdxzk`
- Video: <https://www.youtube.com/watch?v=_ZDungWdxzk>
- Duration: 1:47:27
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:07**  so everybody welcome to this episode of the wasabi wallet research experience this is our weekly research call where we talk about all the crazy things happening in the bitcoin rapido and we can use them to improve the bitcoin privacy for many users uh and today we got the the usual reckless crew on board but also two special guests from short bits we have nadav cohen and ben the carmen how are you both doing good thanks for having us yeah

**00:00:44**  you have uh really cool so maybe we can just get going with a quick introduction of what is the the very general overview of discrete law contracts uh that you're working on the circuits and like the highest level explanation is just you have a bitcoin contract or a bitcoin transaction that's contingent on an oracle or set of oracles attesting to an outcome so you do something basic like betting on the super bowl

**00:01:15**  or something more complex doing like you know an options contract on the bitcoin price so um with the actually like what you're betting on and what the oracle is signing is kind of limitless and it's just like what you can build on top of that yeah i have a question first question and what are in your opinion the most um obvious um usage of this technology for example betting is one that you just mentioned

**00:01:45**  what other um things can be done with this technology i mean something that's coming out soon is uh if you saw atomic finances releasing their options to like trading with uh dlcs so that'll be a way where like people can like buy and sell covered calls um on like directly on bitcoin without needing to use an exchange which i think will be pretty cool you also use the this for things like insurance

**00:02:16**  or things like uh just like basically any existing financial contract that you have or like something like derivatives or you can also use it to like hold other assets for like something we did so we've like basically created a synthetic dollar by just like um having your payout be like you know you start with like fifty dollars with the bitcoin and you end with fifty dollars worth of bitcoin and um so you do that but without dollars you could do that with apple stock you could do that with like literally anything so

**00:02:47**  and kind of the the possibilities are kind of limitless it's just um figuring out how to how to do all these things i don't know did not adapt you have anything to add um yeah i mean i think you hit all the really obvious ones we already know about betting trading hedging and uh i guess synthetic assets and in in this case the the contract has two two parties right

**00:03:19**  i mean it's two two people involved uh in most of the financial contracts there are also two people involved but given there is a high liquidity it's transparent for you you don't need to find someone to to to make a this contract there is a system that can find the content the counterparty for you right that if you want to sell for example what you what you want sorry what you have

**00:03:49**  do you think these contracts um can replace that kind of or can be used to build this kind of high liquidity and very fast kind of trading of futures or whatever yeah so i think um to some extent the answer is yes especially once we have dlcs on lightning and we can uh do things like uh

**00:04:22**  cooperative transfers as well um and you know of course we need some kind of matching mechanism and there are lots of ways to to go about uh approaching that problem but i will say i i mean at the end of the day i think there will be lots and lots of use cases for dlcs but i expect there will still be some amount of more centralized solutions that people want to use in in cases where

**00:04:53**  they they're willing to take on um or in the cases where the trade-offs that that dlcs take uh don't make sense for them and they they want to use like a centralized uh third party or something like that yeah like we'll never rival the like nasdaq execution time but um you know they'll never rival our you know self-sovereignty version of it so you know it's really like what the user wants okay max just in case jump

**00:05:26**  whenever you want i i can make questions all this all the day right but now i have another question because this was implemented this is something that exists today i know it's available right but it is not using i think it's not signatures right um just that's first if that is correct how can this contract

**00:05:58**  change when that route is merged and available for the bitcoin network and uh you can probably answer this better than me you're right at the moment all right um yeah yeah so right now uh we're not using schwaron chain um it's uh we're using ecdsa adapter signatures and uh once we have taproot then uh we can use schnorr on chain and use

**00:06:29**  snore adapter signatures which will be much much nicer they're like nearly three times smaller much faster to compute much faster to verify and since these are like the things that you're building to sign all the off-chain transactions like you're dealing with like tens of thousands sometimes more of these signatures per dlc uh at least if you're doing like financial contract stuff or numeric contract stuff i should say

**00:07:00**  um and so one question you said that the ecds adapter signatures are three times larger uh but aren't like is this the unchained data that's three times larger compared to tap no no so adapter signatures aren't valid on chain uh adapter signatures are kind of an entirely off-chain construct that's uh very closely related to the on-chain signature scheme um yeah so actually uh adapter signatures for ecdsa you have

**00:07:33**  your like 65 byte like actual signature i mean it's not ddr encoded but whatever um and then you have like a 97 byte zero knowledge proof of discrete log equality or poodle um and uh yeah so so there's there's kind of extra steps because we're going through ecdsa whereas in schnorr you just have the nice little 64 byte adapter signature um and then also all

**00:08:05**  of the computations on those are much faster or at least significantly faster so that's that's kind of the first nice thing and then the the other nice thing though i'm not sure whether or not we will or you know when we'll get around to utilizing this but you can use adapter signatures and snore with key aggregation which is just crazy significantly harder in ecdsta so right now with ecdsa adapter signatures

**00:08:36**  we are using single signer ecdsa adapter signatures so that we we need like a two of two on chain but with taproot that can also just become like a single pub key on chain so long term for dlcs in in a tap root uh a dlc on chain looks like some money moving into one pub key and then moving out to two other pub keys and that's all there is to it on chain there's nothing else that shows up on chain

**00:09:10**  okay and just to confirm right now you have the multi-six script on chain yeah right now it looks like some fun's moving into a two of two and then leaving to two outputs so it kind of looks like a lightning open close i mean you could use two-party ecdsa to compress that to a single pup p2 why did you not do that for this mvp because i want to sleep at night yeah i mean the the dirty secret

**00:09:41**  is that you know basically anything you can do with schnorr you can do with ecdsa it's just very easy to get wrong like at every stage and it's just a much larger attack surface and implementation complexity and getting people to look at that code is very hard and all the other kind of challenges that go with it so yeah yeah and taproot makes it obsolete so that's right

**00:10:15**  okay one more i i think i know the answer but these contracts are not easy to identify or i i think it's not probably possible to identify in unchained right i mean if there is a transaction that basically i was betting something to max and max won the bet and the transaction is it's not i cannot

**00:10:46**  say of observing the transaction on chain i cannot say hey this is a payment to max right no not at all like the oracle can't tell you're using them um only the only people i could tell is like you and your counterparty it's literally just like a 202 multi-sig so people probably think it's a lightning like channel at first because that's way more common than dlcs at the moment but yeah it's like very very private in

**00:11:17**  that way exactly but with top truth you will not even be able to say this is a two parties a multi-signature it's just a normal transaction isn't it or am i wrong no that's correct yeah with like in the like you know years from now when we have like full taproot support yeah it'll look like just you know like two like two uh two inputs fund this uh this pub key and then pub key sends out to you know two other outputs

**00:11:50**  and you know very it could be like a user wallet it could be someone consolidating etx says it could be whatever it's just it looks very it could be another change yeah it could be a payment would change it could be anything so it'll be very hard to tell what's going on can it actually be a pain like do you think that the software will be in a way that the withdrawal transaction can be to an arbitrary address even to a third party who was not involved in the contract in the first place i don't see why not like you just specify an address for your payout so

**00:12:21**  you could set it to like instead of bringing it to your own wallet set it to you know deposit to like your friend or deposit to an exchange or whatever you want yeah and in the future uh or so first of all just to have it out outcuts go to you know more than two parties is is quite simple uh i mean it's not implemented or specified right now but totally possible if there was a use case that wouldn't be a hard thing to add um and then on top of that

**00:12:52**  uh in the future we'll probably have more multi-party dlc stuff available anyway so yeah i think that uh you you can intermingle kind of payments with these things as well well it's very interesting because you know that we like things that when you cannot say what is going on on chain we like it right so i was imagining that

**00:13:23**  probably if we have a huge amount of these transactions that you cannot say what is happening who is paying whom uh it could be used for i mean it has privacy applications probably have you something in mind have you discussed this um properties before i'm sure you you did can you

**00:13:54**  share share with us your thoughts about this property for privacy and i think it's huge for privacy just like being able to do financial contracts where no one but your counterparty knows what's going on like today you know you have to like go through a financial institution to be able to do really anything and you get kyc didn't all that versus this like it's completely permissionless and open all you need is like some stats to open

**00:14:24**  up the contract so i think that'll i think like one of the huge things is like today in the world we have like the us financial institution that's like has like all the network effects and money and like if you can't get access to that you kind of get boned in the traditional finance world but with this like you know you could be some like guy in nigeria with just an internet connection and some bitcoin and like have like you know all those financial products now

**00:14:55**  i i have a more concrete question how much i have to trust on the oracle um i mean it depends so you can you don't have to use a single oracle you can use multiple so like what we released last week was we did like a two of three setup where if two of three oracles agreed on a average bitcoin price then our contract could execute but so you don't need to trust like a single

**00:15:26**  oracle completely but at the end of the day like your oracle or a set of oracles completely was gonna dictate your outcome so like if they're all hacked or regulated or go offline like your contract is screwed and there are ways to like um you could like since it is just a 202 multistick you can collaborate with your counterparty to close it in a different way or we do have like a predefined refund so if the oracle never signs anything you get your money back but um you know the oracle can

**00:15:57**  like you know if you're using a single oracle and they sign the wrong outcome like that's just going to be what it is and you're kind of screwed there yeah i will note though so it is true that your your contracts that you have open that the oracles if they lie or are corrupted or something like this um if if that happens the the oracles or sorry the oracle contracts that were based on that specific event get wrecked but um

**00:16:27**  the kind of oracle model for dlcs has kind of users as entirely private entities and oracles as entirely public and oblivious entities so it has first of all the nice property that oracle's don't know anything about their users um off the bat or at least it's it's very tricky for them to learn anything about their users um and how they're being used and if they're being used in these kinds of things um which which is nice you know i always

**00:17:00**  tell people that when you're dealing with oracles and trust models in general like privacy is a part of security um it's just part of the security model but then on top of that um because oracles are public entities uh in in dlcs there is no real way for them to lie privately if you get um you know if oracle that you're using lies even if they like say lie privately

**00:17:30**  to your counterparty you can recover that live from on chain information using uh the off chain information that you have from the transaction that your counterparty uses so at the end of the day you can still construct publicly verifiable fraud proofs that um the oracle attested to something that was false or or equivocated or something like this um and so in the future i think that there will be lots of ways for oracle's to essentially

**00:18:01**  you know put their money where their mouth is and stake funds that can be taken away from them if they lie because at the end of the day and even if if that's not the case you know just from like a more reputation perspective like it's impossible for them to lie in private essentially is a nice property of dlcs yeah really cool i have one more question on the more on chain layer so the funding transactions into that uh the display block script has

**00:18:33**  uh two inputs from or an input from each user right so at least one might provide at least one in the same transaction and then the nice thing is this also breaks the common input on the ship our state and it's same as light is dual funded lightning or pay joint right so this is actually a nice benefit for on-chain privacy in general yeah i think this is really huge where you kind of get like a a mini coin join there and uh something that i wrote a while back but i think where

**00:19:05**  you could do like i call it a chaomian dlc where you could batch a whole bunch of dlcs together and then like you have like a basically a whole bunch of inputs going into like a bunch of different dlcs all in one giant transaction and now you like really break the uh common input heuristic there yeah exactly right that's the logically following next question i'm curious maybe uh yuval or nada have interesting points on the nuances of coin joints with dlcs

**00:19:37**  yeah i mean i think uh i think like it's um it's theoretically possible to be able to like have a like similar like wasabi's model where you have like a coordinator but instead of this coordinator just giving and passing around um details about the coin transaction you guys would also pass around uh stuff about your dlc and um the nice thing too with this is the coordinator could actually close the contract for you

**00:20:07**  if they are connected to the oracle so there's some like actual ux improvements there too where you know you don't need to be online and actually close your own dlc yeah the with the gist of it is just like you know you set up or like you say have like 50 participants all doing a contract and then they um take this take one side of the bet the other they say like half take one size bit half take the other and then they all register inputs and basically just create a giant dlc

**00:20:40**  and then all the payouts go out um at the at the end i don't know yeah but one note here is that if all of the users of this coin joints use dlc then it's kind of like a bad fingerprint in terms that you know that for 100 sure this is a dlc contract right well if if there are other non-dlc users in the same coin joint right then because of tamproot this is uh they look the same and this would be huge because then you don't know which user is part of the dlc

**00:21:12**  which has to pay join a uh malt consolidation right and that would improve uh like analysis massively for everyone i think yeah i think uh that that that's totally doable and we've we've thought about kind of this where you can just mix pools where you have people who are doing dlcs with people who are doing coin joins with people who are opening lightning channels or in the more distant future channel factories and all these kinds of things at the end of

**00:21:44**  the day you can always just like save a little bit on fees by throwing everyone's inputs and outputs on the same transaction of course with dlcs in particular um uh there are ways around this where you can kind of have like a multi-stage setup kind of closer to how uh they've been working on putting multiple lightning funding transactions multiple lightning channel opens in the same transaction you could do something like that with dlcs

**00:22:14**  and coin joins and all just kind of in one transaction um but if you wanted to actually mix kind of normal coinjoin users with um dlc users then there is kind of the i suppose maybe not for everyone this is a downside but the downside of like there's a long time between um going on chain and paying out um because uh you have to wait for like

**00:22:45**  the oracle event to happen or something like this but you know if someone's mixing coins they don't need to be sending anywhere anytime soon then maybe this isn't a big deal it's actually a cool privacy benefit of having time staggered remixes and it could increase your unknown too yeah i think that could be really big too because like i mean the only downside there is that like at least in today's coin joins you would have to like you know you have to use the same output

**00:23:15**  amount less like so if you're doing like wasabi has to be like you know like the 0.1 bitcoin but uh i mean what's the stuff you guys are working on with wabi-sabi you kind of try to fix this yeah he fixes this and uh yeah then you could do an entire thing where you know you could have any contract really going in on there and really privately with everyone else's transaction that'd be awesome yeah and uh another thing i just realized that i forgot to mention uh that is like

**00:23:46**  a benefit of doing things this kind of way at least for dlc users is if you have you can essentially use netting while you're doing this so if i have a position open with two different people who are also participating here and there's like some overlap happening then really all that needs to happen in the more coin join looking transaction is kind of the aggregation so i can like recover some collateral or things like

**00:24:16**  this yeah especially with wabi-sabi that allows for multiple outputs being registered at different values right um i like consolidation of multiple refunds or payouts can be done too maybe i mean they're in the nuances of course like how much information does the coordinator learn that's something that you want to figure out i guess um as far as i can tell i [Music]

**00:24:47**  there shouldn't be any uh requirement for the coordinator to be involved at all um there might be added value like if the coordinator is also helping to mediate this kind of uh net settlement or like making the actual outputs uh allocations more efficient that might be a good reason to uh involve the coordinator but um i'm a little bit rusty about dlcs but if i understand correctly the the way that you would do such a thing is two users would just register their

**00:25:19**  funding amounts uh to a wabi-sabi coin join uh they would negotiate the off chain contract um uh and then at the signing phase once the transaction id is uh already locked in assuming only segwit uh inputs are allowed into the transaction um at that point the um like refund transactions and stuff like that exactly like a lightning channel can be uh pre-signed uh before both uh parties to the coinjoin

**00:25:49**  uh provide their coinjoin signatures so at least in theory it it should you know already be possible uh you spoke about the deposit into the dlc but what about the payout and the withdrawal of the dlc uh if i understand correctly uh that um like the once the the two of two like output is is already locked in and funded um the oracle will uh publish its uh

**00:26:23**  uh attestation i guess for lack of a better term sorry about that um and then uh one of the parties to the transaction will be able to unilaterally uh spend that at that point uh especially if it's a taproot output of course they could uh negotiate to uh just do uh like a a a payout a transaction that spends that um much like uh coin swap uh settlements work um and equally uh they could you know

**00:26:55**  uh bilaterally agree to register this output uh as an input to a subsequent coin join if uh complex scripts are are implemented um like if if you're able to do um arbitrary input uh types and not just uh segwit pay to witness pubkey hash inputs to coinjoin transactions uh then at that point um like it there's no difference right like the ownership proof is equivalent to

**00:27:25**  the collaborative uh spend path um and uh yeah it's just a matter of the the two parties um like agreeing who actually uses the credentials to to register outputs um but that's um like there's no theft risk there but to build on top of that because nadav said that there is this ux improvement that the coordinator can automatically take the oracle signature and to initiate the withdrawal transaction but

**00:27:57**  i am not sure how this would work with coin joints in a non-custodial way because you you cannot pre-sign the conjuring transaction because you don't know the contract transaction so how would that work they couldn't close it in a coin join transaction for you but like if they had your like um outcome signatures and then they got the oracle signature they could close it and like the um like in the easy case where it's just like a single transaction that just has the output to the winner but um if you wanted to do like the coin

**00:28:28**  join like uh clothes you'd have to like do that cooperatively with your counterparty so i think another thing to mention i i kind of mentioned that there are two different ways of doing this one of them is closer to like the multiple lightning channel openings which i think is what we're currently discussing where you have a a bunch of inputs and then a bunch of two of two outputs but on another way of doing this that i think ben has proposed um which has its own trade-offs is

**00:28:59**  having a bunch of inputs and then a single n of n output uh and then a single transaction spending that n of n output in the end which closes all of the dlcs and this would be kind of the situation where it would make a lot of sense to have a coordinator be able to just broadcast that mass closing something you could also do is um well maybe not but um you could like

**00:29:30**  just have your counterparty's signature be um have the same cash flag for um single so it's only committing to the payout output and then you could put that output in the coinjoin transaction the only problem is though then you're if you're using that say cast flag you're kind of revealing which output is yours um so maybe that wouldn't be the best but you're still kind of you know at least just saving on fees that way by you know sharing all the metadata in the transaction yeah and it is important to

**00:30:01**  note that um for this nfn scheme to work you do gain some information about like the other people in the mix because uh you know what their outputs would be on oracle outcomes but there are a couple ways to mitigate this i don't think this has been well thought out or modeled yet but you can for example have rather than one output per per participant you can have multiple outputs where essentially if you picture like say the oracle outcome uh on on

**00:30:34**  like a each party has a payout curve you can decompose that payout curve into like some wave functions or something like that where each output looks like nonsensical essentially uh and you don't know which aggregation of outputs corresponds to like which entity or things like this um or there are a couple other ways of kind of trying to do obfuscation um where you can have like canceling noise on multiple outputs but um again this hasn't been thought

**00:31:06**  out too well yet also i think another possible way you could do it is um and once you have the tap your thing we just have like a single key behind the the funding output you could um in the cases where a single party gets all the winnings you could instead of have signing a transaction um on upon getting the oracle signature you could have them get just get um the other user's private key and then you could use that to then um so then they could then they just own the input completely

**00:31:37**  unilaterally and they could use that to register for a coin join and just like spend it from there however they see fit and one of the other kind of constraints that i see is the coordination complexity and how much that increases when like two users need to collaboratively look at the coin join and only after they have come to an

**00:32:07**  agreement sign the conjoint uh so like what do you think will this lead to more like failed signing rounds just because the users don't communicate properly so i think um with dlcs you have you're signing so many things um i i don't think that uh adding this this coin joining stuff really has a significant increase

**00:32:39**  in how many things you are signing uh and validating and such it uh could change like the size of the thing you have to validate when before you sign say or or the thing you have to hash before you sign rather um but at the end of the day like even for example for like the nfn scheme where they're like for every possible you know or for every relevant possible oracle outcome you have um a separate closing transaction for all end parties

**00:33:11**  um if you were doing just a two-party dlc in the usual way you would still have to sign that many things or at least on the same order of magnitude um and and so you know i think at least in kind of a coordinated model it's not a big difference where where you have uh some kind of like one party that is communicating with many other parties um if it's more of like a gossip based mixing protocol then this might be

**00:33:42**  significantly harder uh maybe a more concrete question so if uh not often i want to fund this dlc contract we register our inputs in the coin join um that we want to use in the deposit uh in the next round we register our output address which is one incorporative or like one of our cooperative dlc contracts and two changes for each other company and then finally this gets put together

**00:34:14**  by the coordinator and we go into signing phase and now both enough and i have the coin join transaction which we will use to do the pre-signed refund transactions and all the dlc stuff that needs to be done and then after all these refunds are signed then we put our final signature on the chlorine joint um like both of us on our own individual utxos and register them in signature registration is that roughly correct

**00:34:46**  yeah that that sounded right to me yeah i think you could because like um like with that multi-oracle dlc that mean adopted last week like it took us like five minutes to sign everything um we still have some optimizations to do to make that faster and by some he means all it will be much faster but uh it's still like you know it's not as fast as um like because i think like in wasabi you have like what 20 seconds or something to sign so i actually think it's a three-minute

**00:35:17**  timeout for the signature basically so that'll be good okay so maybe but yeah something you could do like if it was like you know if you were pushing on that threshold because you do need this both parts do need to sign and verify each other's stuff so um something you could do is just um you just give each other the refund transaction signatures and then once the funding transaction is confirmed or like you know after it's been at least broadcast then you can start doing your outcome signatures so at least that way

**00:35:48**  um you know you're guaranteed to get your money back if something goes wrong um i think that has a bunch of free option problems probably but um yeah yeah probably yeah but but i do think um that if if it's a three minute timeout in the future this this isn't going to be a problem like we have lost i'm actually not sure what it will be in the future but i think right now it's three minutes what are your thoughts on signing period timeout um so generally i would say um

**00:36:19**  [Music] it's probably going to be variable like uh we've been thinking about scenarios like pspt support or hardware wallet support uh and if it's psbt support for like a manual thing you know maybe some rounds would even have a signing phase that's on the order of hours for uh you know high value coin joins or something like that um i i think that's something that uh even if the wasabi coordinator um

**00:36:51**  doesn't deviate from the current timeout values uh and there's demand i'm sure that some coordinator would come up and uh offer those round parameters cool yeah so i mean dlcs require i i assume at least usually less time than uh using like a hardware wallet so that's good to hear

**00:37:22**  for what it's worth like one idea we were kind of spitballing is um having the like um making all the coordinator uh rounds basically determinable by the users so if there's no round available right now with parameters to your liking for example the fee rate might be too low or too high or you want to coinjoin with like a larger minimum input amount or something like that um we still need to kind of think this

**00:37:52**  through but um uh it seems reasonable to just support um like uh a specific user um asking um i mean it's probably not gonna be exposed in the front end directly just because it's a kind of a low level feature but um there's no technical reason and i think no game theoretical reason why uh the coordinator should not support uh the like the ability to just uh ask for a new round to be created um and and yeah so i'm optimistic about

**00:38:27**  these kinds of possibilities opening up

**00:38:58**  okay cool um maybe i think one topic just to rehash and to dive deeper is the benefits of the amount consolidation of two users uh maybe you will yeah if you have some further thoughts on this page on similar type of amount consolidation um so that was kind of implied by the scenario i was describing earlier just to get everybody on the same page

**00:39:29**  um the idea uh behind uh so i i i'm hesitant to call that pay join just because page join kind of implies uh more it implies uh the steganographic features as well so uh i think like a pay-to-end point over wabi-sabi or a credential payment or something like that is perhaps a better term but the idea is like let's say alice wants to pay bob uh some amount she registers uh inputs uh greater than that amount and uh

**00:40:00**  produces uh in her registration she requests um uh a credential worth the payment amount and then she just gives that to bob um alternatively she could ask bob for a credential request and then uh she has uh no opportunity to use it herself but in either case there's no theft concern bob can then go and and use this to um register uh his output uh for the the received amount uh or he can consolidate it with his own

**00:40:31**  inputs to get uh better privacy uh and this is nice because it protects um alice's inputs from bob's uh prying eyes and uh vice versa uh and um um yeah it's uh like that that's kind of how you would have to do it anyway for like the simple case um what i would be kind of like more interested uh in

**00:41:02**  hearing uh uh ben and nadav's thoughts um like in the in the scenario where the coordinator um is kind of like mediating the the con the bets themselves um how like especially in a uh like in that settlement setting um what kind of information would the coordinator need to uh to know and what what kind of information uh like do the individual users need to

**00:41:32**  exchange in order to to get that settlement going because i think that's um kind of the logical continuation of uh this this type of pay to endpoint uh approach well real quick uh before the dav and ben answer that in a naive case we're losing this isn't there still some

**00:42:03**  change output from each other you're still obscuring things for a third party observer where that payment looks like a single user's change output uh so you were breaking up but um if i uh i think if i understand correctly then yes i mean you're you're not disclosing that there even was a payment and further you'd be breaking um the the sort of heuristical assumption that

**00:42:34**  um you can partition the transaction uh into like one set of inputs and outputs per user that's going to balance to zero um so that this is like further helps to to break down the common owner uh in uh input heuristic um but um like i i'm not sure what you meant in the chat by uh uh passing an output credential for unmixed change

**00:43:06**  uh the question i'm saying like if if i put my input in there and get my mixed outputs and then give you an unmixed change output like that will look like i'm just getting my unmixed change back but i paid you and even though like we still see that graph between the two of us like nobody else can interpret that graph correctly yes and that is a much simpler scenario because there's no interactivity there's no paint to end point all you need to do is give me an address and i register

**00:43:37**  you know some output with your address um like in the the pay to endpoint scenario um you do have much better counter pri uh party privacy um because they're like the only thing i learned is like what credential am i giving you i i don't learn how you're actually using it and of course you you can in theory combine it with uh your unrelated input credentials which i don't know about

**00:44:08**  and then the the payment amount is also hidden and never appears in the transaction so many many privacy benefits um to go back to nothing much as original question i think um i think like to have the coordinator like be doing like um like acting as like a watchtower um i think all you'd have to give them is like the oracle that they'll be fetching from to get the signature

**00:44:39**  and then like your actual outcome signatures so doing so you kind of reveal what your contract is to the actual coordinator but uh you also then get like this kind of watchtower thing where you know they can close it for you and you don't need to like be online and make sure you do it which is a huge ux improvement ben are you talking about the the two of two situation or there are a bunch of two of two outputs yeah yeah i guess if you have like you know like gotcha or yeah i was just going to mention in that case

**00:45:10**  uh really what you can use generally speaking is a watchtower and you know if coordinators are some kind of watch tower in the future they can also be used for that purpose but you can also just use like normal uh dlc enabled watch towers in the future uh but but yeah go ahead and talk about the nfn case if you want yeah so if you like if you had like a a 50 or 50 like kind of thing um i think you still reveal your your contract in that way maybe less so

**00:45:42**  no i think you would have to reveal quite a bit uh actually in this case which is why you need kind of other obfuscation methods if i'm not mistaken all of the contract execution transactions are now like aggregate amongst all 50 peers and they all have to sign the the yeah the uh closing transactions for everyone and so they see kind of what the output values are and so you you need to do some obfuscation on them i think uh ben is that right yeah i guess um you do

**00:46:12**  get the benefit that like where the coordinator won't know like which address is going to like which user so you do like they'll know like you know this person or this address gets paid out if this uh you know the price of bitcoins 10k or whatever but they don't know directly like which user registered the payout address so you get the benefit of you know hiding that but they still can see like what the payout curve is for each address yes but you might actually be able to do some amount decomposition of these

**00:46:43**  payout transactions that's right right so you have one input with one bitcoin and you break that down into 0.4 and 3.6 for example naively said but of course what you uh do i i don't think that uh it will require necessarily more signing but uh i think what happens is that rather than everyone passing around their contract info the the thing that's used essentially their payout curve

**00:47:14**  for oracle as like what the oracle says is the x-axis and their payout is the y they take their payout curve instead and they break it up into pieces with cancelling out noise um and register multiple outputs and then pass around these nonsensical noise full payout curves as if they're coming from different people and so everyone should have pretty nonsensical uh if if this works out anyway again i haven't

**00:47:44**  looked into it deep enough but uh everyone should be able to pass around somewhat nonsensical payout curves uh where each person is actually getting the aggregate of multiple payout curves but no one else knows like what that looks like um then hopefully that that mitigates things a little bit and furthermore once you have everyone's payout curves you can construct for yourself um deterministically all of the uh closing transactions that you need to sign

**00:48:15**  and validate signatures of okay yeah that makes sense so like if you have like say like 50 users you'd end up with like 100 or like 200 actual payout outputs but um you know there's still 50 users so some some of them are getting multiple yeah but by the way we've done especially well did a lot of research on this amount decomposition and currently like if we assume that every new user knows the inputs of the of the users of this current draw

**00:48:45**  on the point join and it seems that's the same case here right every user knows at least the inputs of uh of this amount uh and then you can already make some privacy optimized amount organization for the outputs and the payout curves um it's like it's but that benefits from having standard amounts right so if you would have multiple standard demands when users choose some of them and they choose depending on what other inputs were registered yeah and i guess in theory you could

**00:49:17**  even have uh i guess maybe it's it's easier if everyone always has the same number of outputs but you could even play with that as like a parameter to mess around with is you could have more outputs on like some oracle outcomes as opposed to others if say you're receiving more or something like this i actually would guess i'm not sure but i have an intuition that it's better for privacy if it's not sure how many exact outputs you have like if

**00:49:48**  it's if there's an arbitrary like an ambiguous room between one output or zero outputs and i don't know 21 outputs whatever the the maximum value is uh that seems to be more private because you then don't know how many siblings each other yeah so you could have i guess payout curves that um look noisy and are zero in lots of places and everyone just filters out dust outputs every time or something like this or maybe there's a more sophisticated way of doing that um so that you don't actually see that

**00:50:21**  i think it's actually like orthogonal like if you look at the amounts themselves from the purely the coinjoin perspective and you're able to [Music] create enough ambiguity between the input amounts and the output amounts i i think it's immaterial what the script semantics of those outputs are uh and whether or not like the the funds are uh broken down uh afterwards they're

**00:50:53**  divided between uh two counterparties to some bet um like that doesn't really matter uh like all you learn is that this was split between two people but uh the bet itself should be uh like the total amount should not be uh really um uh uh like linkable to the the inputs of both users like in this scenario you can imagine the two counterparties are

**00:51:23**  kind of acting like one user uh the combined like if you partition the transaction and uh look at only the subset of inputs and outputs for those two users who are transacting um if they uh construct the the bet amount uh like the bet output amounts in in such a way that uh there's no way to infer that subset um based on uh all of the like the rest of the

**00:51:53**  transaction it's sufficiently ambiguous and at that point um like it's not clear uh which inputs are going into the bet at all and and therefore it should not be linkable to the specific user um did you talk a bit more about the net settlement stuff that you were

**00:52:23**  alluding to before uh sure yeah so say like um [Music] i am entering into say two dlcs uh and i'm a little bit over collateralized uh because say there's like some uh canceling out so to speak in my position like i'm a bit long here i'm a bit short here or something like this um then uh if in

**00:52:55**  in a situation where you have uh kind of both of those dlcs going in in one place i can essentially have um my two counter parties essentially take on that bet somewhat synthetically against each other and like recover some of my own collateral do those counterparties uh need to coordinate or are they only coordinating through you [Music]

**00:53:27**  um i i guess it kind of depends on what the coordinated setup looks like uh for for the actual uh mixing stuff sorry i i shouldn't have used that word um like suppose uh in the non-coin joint scenario you're you're doing this kind of thing um the do the the two counterparties uh that you have like do they need to communicate uh between them and exchange uh like

**00:53:58**  adapter signatures between them or uh can they uh rely on you to to transfer the information between them uh i see um so so yeah if you want to do netting stuff you actually do need kind of something like a coin join looking thing because uh essentially you need like all three parties inputs and outputs and such to be in a single transaction in order to get back your collateral so to speak

**00:54:28**  um so some amount of coordination does need to happen um i assume that there are different ways of doing this maybe ben is more well-versed i think it'd be up to like the person that's actually benefiting from the netting to be able to figure out how to do it correctly because um you know their states are like over collateralizing that they can take it out they'd have to

**00:55:00**  um negotiate that with their peers to like change the actual contract to be like uh to benefit them to get the lot to be like less collateralized at least that's my understanding i don't know i think uh didn't ichiro write the like initial paper on it he's probably the best one to ask but he's obviously not here [Music] yeah i think it's pretty much uh similar to what you have in mind though ben

**00:55:39**  yeah but i guess short answer is um it's likely easiest if they are coordinating with one another but there's likely other ways of making things more obfuscated or something okay guys just in case we are making questions and comments just to keep the wheel rolling right but

**00:56:10**  anyone can make questions in fact it's good if we call this section q a now right because i think most of the topics are are already covered and if in fact the advanced topics are already covered so feel free to to write the hand well i kind of missed the first uh

**00:56:41**  19 minutes or so but kind of just the general topic of blurring dlcs and nesting them into a coin join i mean it seems like there's a lot of wins that you can have here but it does kind of worry me that that implicitly transitions the model of a coin join for those users to um you can get screwed or things can go wrong if you lose stateful data as opposed to it's

**00:57:12**  literally impossible for something to go wrong here um so i think an important thing to note is there are kind of uh two different ways of of doing this one of which is um essentially just having a coin join where some of the outputs are like these two of twos that are dlc funding outputs themselves um and you know those two of twos once we have taproot become just single pub keys anyway uh and if you are doing things this way then um i don't believe that parties who aren't

**00:57:44**  doing dlcs become affected by parties that are doing dlcs inside of the same mix if that well i mean they shouldn't in either case unless i'm missing something but it's just kind of like that's that that's an implicit risk i think that should be like that that is deserving of like a big warning screen that like things can go wrong if you lose these transactions you know what i mean well like you still just have like things can go wrong if you lose these

**00:58:15**  transactions you know what i mean well like you still just have like things can go wrong if you lose these transactions you know oh boy what's happening well like um things can go wrong if you lose these transactions you know oh boy what's happening well like um this can go wrong if you lose these transactions you know oh boy what's happening well like um everything this can go wrong if you lose these transactions you know oh boy what's happening well

**00:58:46**  like um things [Music] yeah um i guess shinobi can can you elaborate on how this is different from just entering into a normal dlc in terms of state well i just mean it's like kind of putting these two options together implicitly assumes that

**00:59:19**  one piece of software is going to be capable of both and i just feel like you know burying a million options like that like something should be explicit about that you know what i mean like there's no difference between another dlc

**00:59:50**  do you think

**01:00:24**  yes i did it but it comes again so that's where we have the passport yeah um to get back to the adults in the space who want to have adult conversations about things there's so many of them um well they get back to it there's not too much uh like different intermingling maybe ben is

**01:00:54**  because right at the end of the day you you could have like your mixing black box and your dlc black box and like one message needs to be passed from one to the other um i don't look specifically the one that has the funding tx id in it i don't think that there's much else yeah yeah like all you need is for the dlc software it's like a funding tx id for everything and then that should be able to handle everything else so it wouldn't be a huge uh like complexity issue or anything

**01:01:25**  like that so you guys are just talking like api hooking two pieces of software together not like rolling all of this into like the wasabi ui or anything that's right uh although that sounds like yeah then that that was a bad question on my part then got you no worries but for the nfn mix then that's kind of its own custom thing but that kind of assumes that everyone involved is doing specific dlc stuff okay yeah where you're registering two of two outputs hopefully you can uh and in the future

**01:01:58**  you know just single pub key outputs then uh essentially what you'll do is you'll have like a callback where um when you get the thing you need to sign before you sign the actual like funding or the the mixing transaction you like go make a call out to the dlc api do all that stuff and then come back and do this last okay all right that makes sense then i guess uh ignore shinobi's bike shedding troll

**01:02:32**  concerns maybe a question on some different regard that we did not talk about how about optimizations uh that you used for these arbitrary amounts price settlements can you maybe speak a bit more sure um yeah so

**01:03:03**  generally speaking uh you know if you're thinking about dlcs as like a black box you think about like there's some set of outcomes you create a transaction for each of those outcomes that pays out however it's supposed to for that outcome and then you generate adapter signatures um but uh you know this works great for most like betting but if you're uh say doing something where the outcome is a

**01:03:33**  number or you know there's just a ton of outcomes and they're structured um then you have um kind of this problem or a couple different problems but mainly the the problem is that uh you have like let's say a hundred thousand possible outcomes or or something like this when maybe especially usu usually it's the case that you only really care about like some small subset of

**01:04:04**  those and if it's anything above a certain number or below a certain number then you just have some like edge case like okay this person gets all the money or something like this um so what we do is we have the oracles numeric oracles specifically sign uh each binary digit each bit of the outcome individually and then we can essentially construct uh outcomes uh

**01:04:34**  using digit prefixes instead of the entire list of digits so instead of requiring that there's a separate outcome so to speak or it's a different outcome for every different number you can have for example if you ignore the last digit and you just look at all of the digit prefix up to the last digit then you can have um an outcome that corresponds to two possible numbers and then if you ignore two

**01:05:04**  digits that's four possible numbers and so on and so you can essentially for example say if everything above uh 100k um is is just like the same outcome basically then what you can do is you can decompose that very very large interval into only logarithmically many um cets essentially or contract execution transactions um and so and then furthermore

**01:05:35**  uh we we introduced some amount of rounding so this is like negotiated both parties are okay with the amount of rounding that happens um and you uh essentially say round to the nearest hundred satoshi's or the nearest thousand satoshis or something like this um and then by doing that you uh can get more kind of flat pieces which can be compressed by the same mechanism into logarithmically many

**01:06:08**  you know adapter signatures that you need and so in practice what this means is that even relatively complicated uh you know financial contracts uh on numeric outcomes on prices uh end up with only say a couple thousand uh adapter signatures or cases that you you've decomposed it into rather than having to cover like all you know hundred two hundred thousand um

**01:06:39**  and then furthermore for for multi-oracle stuff there's also some fanciness that we do um where essentially you you do something similar where uh agreement between two um agreement between two oracles is essentially constitutes like you take one of these digit prefixes from one oracle and then you construct the digit prefix for like the second oracle that covers um

**01:07:12**  that uh same uh or what the first oracle said with like say some allowed amount of error so we even cover cases where you have multiple oracles and they don't sign exactly the same thing they can be like some amount off um say if you're for example using like kraken and bitfinex and um gemini or something like that as three price oracles then uh you can have it so that

**01:07:42**  so long as any two of them are within 128 of the btc usd of the same btc usd price or something like this then um your contract will execute so yeah all sorts of fanciness and and stuff happening there and there's some more optimizations that i'm working on that maybe use some like verifiable encryption and stuff like that to try and get the uh the scaling for adding

**01:08:14**  new oracles down to something more reasonable yeah i'd be happy to talk more about it of course but at this point i'm probably just rambling unless someone has questions i'm just curious do you think that this is anyhow interesting research useful

**01:08:45**  for conjoint can you say that one more time like do you think that there's some nice similar ideas that we can use to optimize for coin joints in the non-dlc case i mean or is it just completely different research i would think if if there is any overlap it would be in kind of the coordination of the uh outputs and such um because you know we have like some

**01:09:16**  pretty succinct coordination between the two parties on um you know essentially like the contingent like you know if the oracle says any of these things then here are my outputs in all of those cases so we have like these nice compressed uh essentially like seeds from which you are you know contracts from which you derive all of the transaction information but um i guess for a regular coin joint you just have one transaction so maybe that's not a big problem

**01:09:48**  yeah i think where the most overlap is is honestly like on the off chain side where you're finding counterparties like um like we've like looked into like different ways we could you know have a place to find like a counterparty for the bets you want to make and like you could do like you know you just have like a central place like someone's like a wasabi coordinator or you could have something where it's like join market where it's like you know a kind of decentralized kind of thing where you're finding there's no like coordinator to find you counterparties so it's um it's a different way to do it

**01:10:19**  and we're you know we haven't really there's probably going to be like multiple different ways to do it similar to how the coin joint landscape is today so i think that'll be probably the place where there's the most overlap yeah i think the amount organization might be interesting for you guys like based on the inputs of other users how can we optimize the outputs of us uh so to gain more privacy i think this

**01:10:50**  is uh like non-coinjoin cryptography related things uh that might be interesting for you yeah and i guess also uh you know if we are doing some kind of dlc mixing stuff in the future then also the amount decomposition uh things might be some overlap there

**01:11:24**  uh the one maybe relating question how do you get consensus on the fee priority for this transaction um so currently this is done via um essentially you know you can choose whether or not to accept a certain fee rate but afterwards uh everything is uh fee bumpable using a child pace for parent where the child is replaced by fee enabled

**01:11:57**  so it's um yeah i guess you there there's always the uh you know lots of complex ways to handle these kinds of things i think right now the dual funded lightning channel proposal just has like the initiator pay all the fees because it's simpler um but we decided to kind of split the fees between the two parties and then for for the fee rate that's in like say the offer message and then um everything beyond that is

**01:12:30**  done just by fee bumping um yeah yeah two notes here i mean for somewhat obvious reasons rbf is not possible in large coin joins or not reasonable to do because you have to resign everyone has to resign that's right and for dlcs it's not possible either it's only the child of inner child pays for parents so like if you spend your change then the thing you're using to spend your change is what you would rbf with yeah yeah that's smart actually but the

**01:13:00**  issue here still is with uh like the the size of the coin joint like you have to rb you have to try to pay for parent the entire fee for the coin joint um well max you could do that out of the change input or output that wasabi is getting fees in once you you implement like fee credentials that could potentially be a thing where users pay for that air quotes with the fee credentials but it's just that single output wasabi got the mix fees with that could actually do

**01:13:30**  the rbf child pace repairing hybrid if like a coin joined stalling in the mempool yes maybe yeah actually maybe and like users can pay at any time and maybe every hour wasabi will do an rbf of the child uh to v-bump and if there were was no fee bumping fee credential being sent in that hour then it also doesn't

**01:14:03**  do the rbf yeah actually and that would be totally open for any user it's not like everybody has to chip in or split it up it's just like if i'm super impatient take my fee credentials make that happen faster plus the user doesn't have to spend his own chaincoin right which would reveals his high time preference fingerprint while instead if the coordinator spends his v output

**01:14:33**  with the rbf thing then we only know that some user in this coin joint had the high time preference and paid for the p bunk but we don't know which one it was i don't think that would work uh because you would need to provide uh like all of the rbf scenarios of which there will be exponentially many um in the size of the transaction for every single user's um like every ordering of users choosing to bump fees uh should subtract some different

**01:15:05**  amount and then all of those outcomes have to be pre-signed uh except for why though we're no we're we're not talking about the coin join transaction itself we're talking about a child transaction with with the output forget what i said so it's like that naturally yeah that would be super private um that would allow any user to accelerate the coin join without any privacy damage on their part and then three um like that could go to

**01:15:38**  the extreme that wasabi literally burns that entire fee income for that round in two fees but they're not going to do it unless they redeem tokens and then have the right to spend some reserved utxos on themselves so that like that's a complete privacy win and should totally balance out on wasabi's hunt yep because we already got the vidcon earlier and by the way maybe even users who are

**01:16:10**  not part of this coin join can issue a feedback right because as long as you have long-lived feed credentials any user can pay it [Music] nadav you are a whiz kid that inspires genius ideas everywhere you go to be fair uh i credit antoine riyard with all of the fee bumping stuff i just uh read his spec and gave a review you still inspired something here

**01:16:41**  because you are wizkid yeah but uh again the the statement still holds right one user has to pay to feed bump the transaction of every user and so uh your set per by it is going to be very small um but your nominal amount of sets still going to be quite large if you want to make a meaningful difference yeah though you know you could also kind of view it

**01:17:12**  as some kind of like crowd funding for fees scenario where you know it'll go or maybe that's not a good analogy because you also are you want these or there's important things in these and different people will have different um preferences but you know in theory you could have multiple people doing fee bumping and the the fee bumping would all then kind of get aggregated but yeah some people can always be kind of free riders in that scenario

**01:17:42**  if they don't have too much stake too much at stake yeah but the nice thing is is that the free riders are contained within one transaction because the alternative approach to efficient pe estimation is what we used before in wasabi 1.0 but that is not turned off is to make child pays for parent of unconfirmed coinjoin rounds so to allow unconfirmed coins all the coinjoin outputs to remix and the the coordinator slightly increased each

**01:18:13**  round's fee a little bit which was efficient to get all coin joints confirmed reasonably quickly reasonably cheap um but the downside was that if you were the first participant in the first round of uh coin join like the parents transacting first unconfirmed then you paid very little piece while you were like at the end of the chain number 15 or something right your your fee rate got higher and you don't even get faster confirmation for that because you carry like 14 parents uh

**01:18:43**  that you still have to confirm um gotcha so with this approach at least this revival problem stays within one transaction i guess that's as small as it can get i mean that's perfect though because like that just removes all of the dependency limits in the mempool except for remixing

**01:19:13**  right because each thing would be its own parallel um child pays for a parent that's what you're saying right yeah exactly each coin is i'm sorry each conjoint transaction is one unconfirmed transaction and because the coordinator requires that all inputs to the coinjoin have been confirmed already um this means that no coin from the unconfirmed coin joint transaction can be registered in a new coin joint transaction and therefore we don't have child base

**01:19:43**  repairing chains go ahead adam sorry i i i would have a question but it's a bit different topic is that okay sure go ahead so i i was i was thinking about

**01:20:16**  the industrial things some of you might have seen on twitter and and i believe i i get to the end of how far i can think about that when i properly went through the issue but it would be really nice if uh if to hear what you guys think about that so the start is that there is a perverse incentive

**01:20:47**  for the coinjoin coin joint fees with the current wasabi which is which is that the more user the coinjoin have the i think exponentially more fee is being paid out by the queen join rounds if i'm correct and there is a perverse incentive for the

**01:21:17**  coordinator to to add their own users so what do you guys think about this and i i will i will not say what i think just see if we get this similar conclusions or not do you mean in the context of dlcs or coinjoins in general no we currently coinjoin

**01:21:48**  fee coordinator fee structure i agree 100 i think it's a problem and uh especially when in combination with the like the discount there's additional perverse incentives for um like individual users to to register specific outputs and uh that can be combined to to make sibling by somebody other than than the coordinator uh also are a

**01:22:19**  little bit cheaper so it's not just the coordinator i think it's perfectly possible to address it like this is why i've been proposing a flat uh like flat rate some percentage of mining fee perhaps or um and on top of that uh doing some sort of uh like discount model for um encouraging like a pro privacy behavior so for example like bringing in um

**01:22:52**  an older input something which destroys a large number of coin days um this is kind of like fidelity bonds in join market like you know that that input has not been sibling any of the rounds that were concurrent with this output not being spent like after it was confirmed uh this could not have been used this liquidity could not have been used to civil other rounds um so uh it's good to incentivize uh that kind of behavior as well um

**01:23:26**  or all right so is it a perverse being centi yes okay let's let's keep it simple and only talk about the coordinator for now does anyone not agree with this or or or or we can move on and and everyone agrees no part with the coordinator i mean that's a special unique case because anything that they could do is free and that's like the whole problem with the fee schedule and

**01:23:56**  sibling it's you have to balance between on one end it being so cheap that you can sybil all day long and on the other end it being so expensive that people aren't going to remix which is one of the most important properties of a system like this so it's like if you're talking the fee schedule i mean i i wouldn't talk about like perverse incentives i would be talking about where is that middle spot where you accomplish both of those things it's not

**01:24:27**  too expensive for people to be remixing but it's not so cheap that you can just flood the system with liquidity and sibling we'll get to that because i mean yeah sorry max go ahead uh if i made just quickly uh an important distinction here is uh mining fees and coordinator fees are very separate um so chernobyl your point stands when coordinator fees dominate

**01:24:58**  over mining fees but not vice versa touche yeah and uh one other quick thing is that this cheaper remixing for high quality coins especially when it when we add a timeout benefit right so utxod is destroyed if that count is high then you get a cheaper coordination or mining fee this has similar denial of service protections as fidelity bonds though i would say weaker because

**01:25:29**  fidelity's bonds you actually cannot spend the coin in this lock-up period while um well with this type you could have spent the coin but because you did not spend it you get cheaper fees so it still improves denials or increases the number of service costs just in opportunity cost of not spending these coins yeah i mean i think that's a perfect way to balance that all right so so this is the perverse

**01:25:59**  incentive that there is no no question about this now is it a civilian incentive and i actually did not i was not not able to to come to the end of this this question i i my conclusion was maybe but you know what the sibila keys is when most of the participants are actually one entity right so the question is would this lead

**01:26:32**  to to such situation where most of the participants are are are one entity is is this is this this instant devices that much so that would happen you know what i mean well i mean aside from the coordinator i don't see how that could be the case if you're paying fees every time and i mean if if the coordinator wants to sybil their

**01:27:02**  mixing pool i mean all they have to pay is mining fees everything else is free but with anybody else i mean if you're paying fees for every mix round i don't see how that encourages it that's a disincentive like that's one problem i have with samurai is their fee schedule incentivizes lots and lots of remixing but the fact that you only pay once and everything else is free i could just buy a new utxo on cash app every day and

**01:27:34**  feed that into whirlpool and just let that sybil all day for free could something you do to like prevent the um coordinator from having like the ability to um civil by just only paying mining fees just have like say like half or like a third of the actual coordinator fee just like be like sent like an op return like burn or like have it like donated to like hrf or you know some fund well that's kind of what i

**01:28:06**  think like nothing much was getting at with modeling the mixing fees off of the mining fees so that's uh that's always balanced the correct way there um you can correct me if i'm wrong nothing much um yeah like you could make the flat the sorry the coordinator fees either be completely flat so like some percentage of the amount regardless of how many other inputs and outputs are in the

**01:28:36**  transaction regardless of how much liquidity is in the transaction um that could be like a a linear function of the amount or the weight and if you make it just a linear function of the weight well then you know that it's proportional to the mining fees um it doesn't really matter like which of these specific scenarios and it could be like a constant function not necessarily a linear function oh all right all right so i didn't fully fleshed out but i think somehow the

**01:29:08**  because if you think about it if there are 99 real users then it makes sense for the coordinator to join in to be the 100th one because 99 people will pay after another appear 0.003 percent right so so it makes sense if you're thinking about the big numbers because then you will get 99.003 percent

**01:29:41**  but if you are thinking about the small numbers one if there is only one user does it work for the coordinator to get into the round and the answer is it doesn't because that's only one times zero zero zero three percent and the coordinator will pay more mining fees than how much it would gain fees from that person so i think the question here where is the equilibrium where

**01:30:15**  the bitcoin fees you know so yeah the intercept is where uh i think it's roughly like 20 000 satoshi's uh on average uh in coordinator fees um for like a um i may be misremembering but like 0.1 times the number of users um times 0.003 i think uh

**01:30:46**  percent sorry so another two zeros but like you can calculate the uh expected value for the coordinator from like or not even expected just the value for the coordinator for um uh that additional user and if the marginal cost in terms of the current mining fees of adding a single input uh and registering another fake 0.1 output um is less than that then there's a clear incentive for the the coordinator to do that so it's it's just a function of um the

**01:31:18**  current fee rate for the the transaction and um because i mean you could do this repeatedly uh so long as the cost of an additional input and output is less than uh the the figure the um without multiplying by the number of users because the total amount paid by the user that usually sums to um several tens of thousands of satoshis as long as that increment is uh greater than the marginal cost of an additional fake

**01:31:48**  user well uh that's a linear function so it's the same regardless of how many inputs and outputs were already added okay so what's interesting here is that you know it might seem like like there is a civil issue but it doesn't because it definitely doesn't make sense for one people two people three people five people 10 people maybe at 10 people it starts to make sense for

**01:32:18**  the coordinator but you know there is there is a line somewhere where it starts to make sense and so it doesn't mean that the coordinator is instant device to take 99 of the the existing users or something like that it it just means even the coordinator participates with more users it it pays more mining fees you know what i mean like like there must be a line there where it

**01:32:49**  starts to make sense but maybe it's at 50 people i i don't know right it's a function of the fee rate so at one satoshi per byte and let's say 100 bytes per per fake user uh let's say it costs 100 satoshi's to pay them mining fees for another civil user if you can extract more than 100 satoshis and coordinator fees from the target user or users uh right so like the more users you're

**01:33:20**  targeting the less powerful your civil attack is for the anonymization but the more uh the more fees you can extract out of those uh victims um so there's just a tipping point there right it's uh it's just the intercept of two lines um exactly exactly right but i'm actually gonna create a graph very nicely in this this episode but uh but this means it's not a civil incentive

**01:33:53**  at least not in the sense that people are using it to be right because there is no incentive to do it for smaller number of users so i would say not the number of users that you're saying it sure it's well anyway you know what i mean it's not a civil incentive not nothing the civil incentive that while the coordinator is insane incentivized to be anonymize everyone no it's very far from the case actually it's a free ride incentive

**01:34:27**  well no it's worse than a freeride incentive because the coordinator actually increases its revenue if it does this but um uh even if like the the the tipping point like whether or not it makes sense for a civil attack or only for extracting additional fees uh that entirely depends on the like whether or not the uh mining fee rate is low enough uh and if the minimum rate is like one satoshi per byte um that's actually not that high i think it's usually much higher than that i

**01:34:58**  think it's like on on average more like 10 or 20 uh at the the lowest rate so that implies that yes adam you're you're correct it's not really a direct incentive because uh an additional like fake user uh would not the the cost would not be covered by the additional fees of just a single user all right so now it's it's worth asking

**01:35:28**  the question that you know here is a weak civil incentive or or strange civil incentive but you know there are these incentives for cbl what do you guys think can you identify some so obviously it is reputation the most the largest civil instantly and you know

**01:36:00**  it is also noticeable when you start to do that um do you guys say bye so for example we can't tell with the current wasabi that there is no cbl happening or at least not this kind of civilian why is because we have 10 000 bitcoin monthly volume and the direct way the non-noticeable way to

**01:36:32**  see bill it would be if we would be most of the participants of that of the 10 000 bitcoin if we would be bringing in that fresh those are fresh bitcoins not the actual coinjoin volume that's 40 000 but the fresh bitcoins monthly is ten thousand so in order to cbl unnoticeably we would have to have like nine thousand bitcoin or something crazy like that but you know if we would

**01:37:05**  have nine thousand five thousand bitcoin then the last thing that we would care about is the perverse fiends and the beach at at best it's it's a couple of bitcoins not five thousand you know what i mean it it wouldn't make sense in that case do you guys agree or disagree with that mostly agree i i think it's you know you

**01:37:35**  need to actually crunch the numbers and figure out like at fee rate x this is how much liquidity you would need to create a fake uh graph of this size in order to make you know the hide the liquidity and you can reduce it to like what is the liquidity requirement and what is the marginal cost or profit for the coordinator to do like an additional round um and and uh parametrize that by how many real

**01:38:05**  users are in the round we could also execute okay let's say we agree then i i say that i i wasn't completely correct there because we could also execute a severe attack from less money you know from remixing actually i think that's what you were referring to by by liquidity right i guess the confirmation something like that uh yeah um it's not just that it's

**01:38:35**  also uh like how much in mining fees are you paying to create like a fake graph that does not look like remixing which is uh like that that's a distinction between fresh and remixed coins right okay so but we also know that you know because this what what the cbr would lead to in this case if we don't have don't have if we are not matching the users users money with our own money with

**01:39:08**  multiplies of our of the users money we would have to have that much then if if that's happening then we would see a very high number of remixes and it's only 20 to 30 percent so that's not that that actually proves that there is no this kind of cbl which may or may not be severe happening

**01:39:38**  does that does that make sense is there anything wrong with that uh no i think that's correct but i mean you need to take into account the possibility that you mix coins and then you create some sort of fake spending graph and eventually you cycle that back into the mix with you know a bunch of fake transactions in between which also costs you mining fees probably a lot more than the the mining fees for the coin join in order to simulate fresh bitcoins that

**01:40:10**  are actually just getting recycled by the coordinator that incurs the significant cost and i think it's it's uh you know the if you look at the topology uh of the actual graph on the blockchain uh it should be fairly straightforward to estimate that cost or even just measure it yeah but for what it's worth the dumplings repo only uses one like you can fool the dumpling repository into thinking it's fresh bitcoin but just making one transaction so fresh bitcoins are only the actual outputs of the coin joints

**01:40:41**  being inputs of the next coin join but if there's even one hop of the single user transaction in there it's not considered fresh anymore all right or sorry it is considered yes and i mean that uh if you are thinking adversarially then the coordinator uh like probably anticipated that and created uh you know anticipated the scenario where the dumbling's repository was updated to take that into account etc etc you can still reduce that to a cost

**01:41:12**  in in mining fees at the bottom line so anyway just to to to sum up so is it a perverse incentive yes is it a civil incentive um not really not in the stands where people are using it because maybe it would be a big civil incentive something like that but not even in the technical sense because

**01:41:43**  in the technical sense the majority of the the user should be controlling the the volume and you know is there a cbl no there is no cbl because it's noticeable which is a disincentive and the final question is that why did we not change that it's because you know the fee structure is is actually pretty fair because you gain

**01:42:14**  more privacy you pay more but that's not the real reason the real reason is because the fee structure is not something that you know that's the first agreement you have with all your users and your if you are unilaterally um just changing it without a very good reason like like wasabi 2.0 which needs change anyway because of the protocol

**01:42:44**  then then you know like like you're not changing around with the most fundamental parameters that's good music by the way

**01:43:20**  what music uh i can see someone is sharing their screen again yeah but guys can you kick him out trying but doesn't work yeah we need to use a private jet see then maybe just let the let the music go for a while and

**01:43:53**  and then the live stream that would be a nice ending yeah yeah maybe we should end the stream now wasabi research club cat hacked tomorrow headlines wasabi attacked can't have fun can't be an adult because stupid children

**01:44:34**  all right thank you uh any closing thoughts that uh ben or nadav want to bring up we should set up uh dlc contracts for whether or not there's a civil attack on what saw me here we go oh yeah i was gonna say thanks for having us this was fun always down to talk to you guys um yeah but thanks thanks for coming

**01:45:10**  well thank you guys it was really really you know just thinking back when we started the wasabi research club as uh as exactly not exactly more than one year ago then we were just gonna have have some fun reviewing all the privacy papers and and you know uh putting them on youtube and

**01:45:40**  and they're hoping that the authors of the privacy paper appear because this is publicity for them and then we can pick their brains and ask our questions and and you know that that was fun and then for a long time it was it was just uh just just just us basically thinking about all kinds of privacy things and it it it looks like you guys are taking this to a completely new level so i mean it's it's really

**01:46:12**  really awesome to to see so congrats for these yeah thank you i mean you guys are doing awesome here the lobby i remember like being when i was in college just like watching all your like the snicker one and the oh dear and the uh you know all the different like uh mix it like mixed net ones that are really interesting and yeah it's crazy what you guys are building now it's completely awesome

**01:46:42**  and i really like how it's all coming together like i can totally see why we saw the coin joints that open and close dlc contracts or lightning channels that then open and close dlc contract uh that's gonna be a wild wild world yeah guys we have uh again someone sharing their screen uh but yeah let's end the stream and yeah i think this was a good episode you know i'm listening to this music

**01:47:12**  like three times a day super simple songs my my son really loves it i can't even hear the song but yeah

# Wasabi Research Club #26 - Bitcoin Privacy - A Survey on Mixing Techniques with Simin Ghesmati

- Playlist index: 26
- YouTube ID: `l7bK85obzrM`
- Video: <https://www.youtube.com/watch?v=l7bK85obzrM>
- Duration: 2:22:33
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:06**  welcome everyone in the manifest wasabi research club today we are reviewing a fresh paper a new paper that's so new that i believe it's only a prep print at this point bitcoin privacy a survey on mixing techniques and this is a metal analysis of

**00:00:36**  almost all the bitcoin privacy techniques i can think of even things that i wasn't aware of before so this is a really interesting paper and we have today the author simin kashmati and a co-author say hi shimmy yes hi everyone i'm simion lasmati and as adam told currently i'm working

**00:01:08**  on blockchain privacy especially for bitcoin privacy and i'm working in sba research and i'm a phd student in vienna university of technology all right and could you talk a bit about the contributions of the paper there are multiple authors walid and edgar may right

**00:01:39**  uh yes actually a valid uh is my mentor our team leading sp research and edgar wifer is my supervisor oh i see oh i see so so this is this is almost your brainchild or mostly that's that's good yes all right so how should we how should start it

**00:02:09**  i have to propose one could be someone gives an overview of the paper or i would ask si simeone to to talk about the history uh how did you you get here uh and and what went through your mind to start examining this topic

**00:02:40**  can anyone give an overview would anyone like to give an overview i would actually like to hear simeon give the overview all right so ask me can you talk about the paper and it would be interesting to to go from historical perspective that how you cut in to to bitcoin privacy

**00:03:14**  um and how did you put the things together because this is a lot of things right it looks like you have to go through many many papers uh yeah actually i can also walk through over the paper i can also just provide some information about the paper and then we can discuss about the results

**00:03:45**  whatever you prefer uh please then give an overview of the paper okay can i share the screen um afraid you can't you can try but last time i checked gt didn't work for screen sharing see if you're on the desktop it should

**00:04:17**  be the third button from the left on the bottom of the screen yep oh it's good it's good okay so you can see the paper right yes yep all right i should fold this paper uh the story was uh started from participating in a course in vienna university of

**00:04:50**  technology which was about the data science uh on cryptocurrencies and in that course we have uh some projects in uh the anonymization of uh bitcoin actually and then from that of course i i got uh some insights about the privacy problems uh in the um cryptocurrencies and

**00:05:22**  blockchain and also the proposed solutions to mediate them back then i decided to work on these techniques actually and uh when i went through the techniques i just found some um prominent techniques such as corn join and uh at that time mixing websites for instance and when i continued our

**00:05:56**  my research i found that there are lots of proposals in this area and it's they are not just one or two techniques then after that i decided uh to do a survey to provide most of the techniques and then compare them over some criteria the main research questions was uh

**00:06:27**  the main research questions actually were to find and compare those techniques over privacy security and efficiency criteria which i adopted from the literature and for actually this paper changed a lot during past two years uh i started at in 2019 and then uh i found even some of my

**00:06:58**  categorizations were wrong and then i updated in the paper for the paper apart from background and fundamentals every one should be known before going to mixing techniques we provided the definitions for the transactions and the different type of transactions such as a time lock transactions hash lock transactions and htocs and then we provided uh

**00:07:30**  what what's the what is the problem uh and the problem with the anonymization attacks and the research that uh proposed some heuristics and and the most commonly used one was common input ownership heuristic and most of the technique mixing techniques uh try to overcome these fundamental heuristic to prevent any actually the

**00:08:03**  the anonymization attack and uh when i found those mixing techniques first i tried to categorize them as centralized and decentralized techniques and then i found that it's not a correct categorizations as uh although for instance for coin join uh in transaction level the conjoint is decentralized however in the network level it's

**00:08:36**  centralized when you have to contact a coordinator or when the participants have to find each other in a bulletin board so i decided to find a better categorization for these mixing techniques as of now i categorized them in four main categories the first one is centralized mixers which was

**00:09:08**  the techniques that are based on uh mixing websites and uh we in the literature we had mixed coin and then blind coin and then like mix in mixing website all the users actually forward the coins to a centralized mixers and then the mixer mix the coins and shuffle the output addresses and send the coins to the destination addresses

**00:09:39**  mixedcoin provided uh some sort of warranty from a mixer to be sure that if the mixer cheated their users can publicize their warranties although it provides some sort of accountability but it can provide depth resistance actually and then blind coin uh proposed blind signature for mixed coin and then like

**00:10:10**  mix proposed uh using multi signatures with mixer to blind coin to actually make it better and we also have obscure which use a trusted [Music] environment for centralized mixer apart from this uh we have conjoined based uh techniques uh which was proposed by maxwell and back then corn shuffle coin shuffle plus plus and value shuffle by tim buffing and

**00:10:44**  uh and also conjoined xt which is chaining the transactions uh using coinjoin by adam gibson and also a sneaker which is an interactive unattractive actually a coin join and pay join which was uh first uh proposed by black student under the name pay to end point and then pay join actually adopted by most of the

**00:11:15**  wallets and in the community and for uh atonic swept uh i uh i put fader exchange uh protocols in this category fair exchange and zim which also use fader exchange but it proposes a new technique to find another party uh by advertising on the blockchain and then we have coin swap which proposed by maxwell but at that

**00:11:47**  time we didn't have a check like time verify and segment and then new coin swap which i read that in adam vipson's weblog which uses a segwit and also um check lifetime verify for the blockchain transaction and we also have pay sub which was recently proposed by chris belser to actually to use

**00:12:18**  construct new coin swap design and also combine it with page on which provide better privacy and we for off chain and unchain transactions we have blindly signed contract and also tumbleweed but by ethan hilman and for threshold signatures these papers are those that i found through my research and actually uh all the threshold signatures that we

**00:12:49**  can use in bitcoin which are which can be used in ecdsas scheme can be used for mixing but these three are those papers that i found them in coin parties that you and secure escrow address and then the paper just provide a short description about these techniques

**00:13:19**  and here in discussion and evaluation we compare them over these privacy security and efficiency criteria can i continue or is there any question so just an idea that i believe the best way would be to go through your categories one by one and

**00:13:50**  and and everyone can share their thoughts on the things that actually make sense uh but please continue after on let's proceed like this and here in the table we try to provide those criterias and compare the techniques uh by providing if they

**00:14:20**  have full coverage of this criterion actually or partial coverage or no coverage and at the end uh and for privacy uh we did we compare them over anonymity set on linkability and on traceability based on crypto node definition and also value privacy and for security we adopted depth resistance dust resistant and

**00:14:52**  civil resistance and for efficiency we compare them if they need to interact with input users if they need to interact with the recipient if the technique is compatible with bitcoin and if the technique provide directly sending to the desired destination address and we also provided the number of transactions and also the minimum block for one mixra

**00:15:24**  and these uh last um two last columns actually provide uh the delays and the fees uh some insights actually about the fees and delays uh that most of them does these techniques need so um all right thank you for the great

**00:15:56**  overview of the paper um let's dive into the next section which is going through all the categories that that you identified and before that i would just like to ask if anyone would hotel thinks that there is category may be missing or or or would make any changes the four categories are atomic swap coin join base centralized mixers and

**00:16:26**  threshold signatures so any disagreement so far all right it looks like uh everyone agrees on the basic categories and now let's continue with the thing that i know the least about which are the threshold signature schemes

**00:16:57**  coin party i know nothing much uh thinks very highly about coin party secure coin i don't really know anything about that and sea uh that sounds familiar to me too so um guys any interesting insights here maybe nothing much you can talk about

**00:17:28**  your love of coin party uh well to be clear what i like about coin party is the on-chain footprint uh the coordination protocol is uh not so much my favorite because uh it relies on these like semi-trusted uh parties it's essentially a federation unless you identify the the mixing peers with the users if if that's the same group of entities

**00:17:59**  then it's a uh i guess you could say it's kind of like uh similar to coinjoin xt in a way i don't know it's hard to say but it's um yeah what i like about coin party is that it's um it leaves an on-chain footprint that looks a lot like coin swap uh but it's it's more like a a multi-party mixing transaction so

**00:18:30**  um from a more like uh i guess economic point of view it's a little bit more like coin join so i'm like the reason i find it interesting is kind of um you could do more interesting coin join like protocols in the future with the same like on-chain techniques that's why i think it's cool all right any other insights on

**00:19:00**  threshold signature based schemes or can we move on to atomic swaps all right so far exchange and theme i believe siem was the scheme that was advertising itself with severe resistance right oh yes by paying a

**00:19:31**  a coin to miner to advertise actually you're willingless for mixing it makes it expensive right that's the idea yes and by the way that actually happens in coinjoin that's one thing i was noting when i was reading back in the day the zinc paper

**00:20:02**  anyhow coin spot new coin swap and face lock this is a very hot topic today so as you explained coin swap was proposed by maxwell new coins fought by adam gibson and chris batcher is proposed and implementing baseball is that correct he's working on the

**00:20:32**  implementation yeah it's a rust-based implementation of the routed um like patrons sorry coin swap stuff with um i believe the multi-party cdsa stuff is not yet implemented but um with like normal scripts uh it already had testnet transactions if i'm not mistaken [Music] all right so that's coming along and there is bsc and tumblit

**00:21:07**  tumblebit is something i'm intimately familiar with because i spent a few years working on it uh bsc is is that a scientific paper that ethan hermann uh wrote also like number bit yes exactly right and they use blind signature and back then as it was not compatible with bitcoin blockchain they proposed tumbleweed and

**00:21:38**  [Music] i guess the top of it is the better version for doing the payment channel and but uh honestly speaking uh i couldn't find any better version implementation of these atomic swap proposals although breeze wallet and end humble withdrawal were on github but they are not are they're

**00:22:11**  uh commercial wallet or how to say that better version yes so so so what happened here is that i was working on bitcoin privacy at the time uh joining market trying to build a joint market while at hand nicoladori who wrote the c-sharp bitcoin library told me that he's going to also work on bitcoin privacy but not on coinjoin but on this new thing

**00:22:43**  called tamba bit and and then that was a clear sign for me that i have to work on that too because nicolas is going to do that and that's how ann tumbled it uh was born and in the beginning when antambovit was ready and i realized there are network level problems so i started writing my own wallet uh to fix them for and tumblebee to be ready

**00:23:16**  to so people can can use it without ruining their privacy in in the network level so anthony was ready and and then i went to work at stratis which is an odd coin uh but they run at timberweet for their altcoin and for bitcoin and i was working on that for a while and that was

**00:23:46**  called breeze wallet and to be honest i'm not exactly sure what happened with breezvalet because a lot of development effort went into that and and if i think back this should have worked out it should have been a working product but it wasn't so so i'm not sure anyway i realized that i can do the same what i can do to be time of it with coin joints

**00:24:18**  and that's how wasabi came to existence but one caveat there is that what we were working on with antambrevit is tumblr beats tumblr mode and not the payment hub mode so no one ever tried to implement the payment hub mode which is which is a very interesting thing it's what were the problems with that the

**00:24:50**  problems with that were that it was unidirectional right you could send the money or receive the money you cannot send and receive money or it needed equal it needed equal amount denominations which makes the user experience a bad and and it took a lot of transactions compared to um not sure the payment of mo now that

**00:25:20**  design took a lot of transactions so so anyhow you need directional and still need additional amounts so that made made the user experience of the payment formula very good and i believe some people were also working on improving tumblebeat later on but but uh but in ways that would require bitcoin to change so they really pay more to attend attention to that

**00:25:51**  [Music] so that's the story of tom of it [Music] what do you guys think any any more insights stories or should you want to centralize mixers all right centralized mixers

**00:26:23**  now that's an interesting topic too maybe i have a question she mean simin did you come across implementations of not mixing websites but implementations of the the research mixed coin blind coin lock mix of school row did those things get used i i never found such a thing but it might actually uh i didn't find uh

**00:26:53**  implementation for them uh they were only scientific papers uh proposed in um mixed one and blindfold actually in fc and they just a scientific paper at least i couldn't find the mixing website who applied those techniques yeah that was the same experience for me too um maybe one interesting thing is

**00:27:24**  blind queen was operating with xiaomi and blind signatures uh if i remember well and you know it it was a paper in maybe 2016 something like that and at that point they were so close to coming up with chummy and co enjoying which would have the thing with behind coin if i remember correctly and discord me uh that it it provided

**00:27:56**  accountability so if the servers tears then people would know something like that am i am i correcting that yeah for blind coin and big fine the server is the mixer is accountable actually by providing a warranty so so they were so close to like just applying blind signatures to coin joints which is chummy and coins are in that i was just

**00:28:28**  surprised that they didn't at 2016 they should add all right and so let's move on to the largest topic we have which is the coinjoin based techniques nothing much with your mind

**00:29:01**  giving us a history lesson and coinjoins just how things came together um if i understand your question uh you mean uh to provide some insights about the providing better point job uh yes uh i i said nothing much nothing much is uh is a name in in this chat so he's a real person so i was asking him

**00:29:32**  but if you can then i would i would have to give you your perspective too actually doing this part um this research and then i find some of the implementation in the in practice and for those uh coin join and page one were commonly used by wallets actually and the dumpling which was also proposed

**00:30:02**  by you uh showed that uh there are lots of coin joint transaction from actually from since 2018 where we have uh two new wallets wasabi and samurai and then uh i really i was really interested in the usability of those coin journalists to see if the users could use them and

**00:30:34**  i try to walk through with my colleague actually was valley for those wallets uh john market wasabi and also samurai to perform a user study and before that we walked through over them and we found some difficulties really in performing conjoined transaction with some of the wallets and although

**00:31:06**  to be honestly speaking uh wasabi was easier to install and to perform conjoined transactions [Music] one of the main problem was the um the fixed denomination by uh wasabi and samurai while a joint market didn't have this limitation and just from wasabi i was thinking uh if the wallet could provide uh more pools to be entered rather than

**00:31:39**  a fixed denomination and for mixing it would be really better for users especially when they have a large amount of coins and in wasabi there is a specific pool with a small amount and then they will receive lots of small coins um i guess from the usability perspective

**00:32:12**  it's it's very difficult for the users uh to to have too many small coins actually and it was one of the insights that can be improved by providing some more pools in the wallet if if it can be actually actually yes we

**00:32:44**  so we created the so we we are working on on the next mixing technology which which is which is almost ready at this point is it fair to say guys yes [Music] so and and during that research we created a simulation

**00:33:16**  which was not published it's it's public but wasn't like published or made a big deal out of it but what the simulation did is took their current wasabi coin joint inputs those has never participated in a mix so and created a text file out of this and then created a bunch of different kind of coin joints and also created analysis of these coinjoins so what we get is

**00:33:49**  um simulation of of us writing a bunch of intuitive algorithms and different denomination schemes different tools different so i'm going to comparing a bunch of different kinds of coin joints how we could could do do this and and we came to the conclusion there that yes who's indeed increased the efficiency of the mixes

**00:34:20**  so so that's that's the one point in my opinion that's suggestion and maybe another question uh for the transactions in wabi-sabi [Music] does it make it a more expensive in comparison with current implementation of wasabi then they should provide more transactions

**00:34:53**  um so it's the opposite it actually makes it orders of multitudes cheaper the idea there what is published in the paper is it's not published the amount organization but what is published in the paper is to how to create amounts in any phase right so with blank signatures we can only create standard outputs standard denomination outputs

**00:35:25**  and only those can be considered uh trust less so only those gain anonymity and that's why you have to do a bunch of coin joints because you have to create those standard denominations now with bobby savvy arbitrary ones and and again i'm not fully up to date with the implementation but in the simulation what we did is that we came up with a bunch

**00:35:57**  of denomination systems powers of one powers of sorry powers of two powers of three two times powers of three preferred value series and powers of ten we came up with with a number of denominations instantly couldn't really like put them together like how to how to come up with the idea one but anyhow so we created with a bunch of these and then what we did

**00:36:27**  is we were looking other people's inputs in the mix and try to decompose our input sum in a way that is probably going to encounter with other people's input sounds uh decompositions and in that way we could create coin joints that rarely very rarely generated changes and and so that's that's

**00:36:59**  how far we get in the research about the implementation guys uh just to clarify by change you mean uh a coin who which has a unique amount in this case right yes okay cool um yeah so the implementation is uh for several months we've had the the crypto in place the purpose of the crypto is just denial of service protection

**00:37:30**  much like the blind signature stuff um we're able to do coin joins on rag test right now but like the stuff that you've been talking about is not yet uh so specifically um like the logic of how to decompose um with a specific goal in mind um and that goal being like optimizing privacy that's not yet done uh we still have only like a stub implementation that currently behaves

**00:38:02**  deterministically but um like it's it's uh yeah uh so the lower level details are you could say that they're finished but um like actually applying this to to provide privacy um like in in a real world setting uh that's not that's not there yet um yeah hopefully within a few weeks we'll uh we'll have that sorted as well

**00:38:33**  [Music] all right so that's what we are up to is it a lot to take in all right let's let's talk a bit about coin shop because i have one audition to to this paper which is well obviously at the beginning

**00:39:05**  uh tim rafing annika kate and pedro murray sanchez came out with the coins of a paper which promised decentralized way of conducting coin joints it wasn't fully decentralized but uh but the server was almost like a bulletin board at that point uh would be a correct description of

**00:39:40**  coinshackle all right i'm going to go with a yes and then many that's actually very many implementations or many people tried to implement point shuffle i remember there was mycelium's implementation shufflepath which was done by dania kravis who is a bitcoin sv

**00:40:11**  proponent currently which just blocks my mind how did it happen but anyhow let's leave some mystery there and even the cash cash usually now questions on the electron cash bitcoin cash guys were implementing coin shuffle at the beginning um not sure what was the name of that and and then but bitcoin shuttle plus

**00:40:43**  plus came out very very early and and actually i i make a guest here see me see mean did you have very heavy influence of of the coins of a plus plus paper to this paper so was that one that you you read more than maybe others for coin shuffle actually

**00:41:13**  i just read the paper and where they provide actually at that time they provided a newton technique uh for being prior actually for intern preventing internal uh trade stability between input users by providing a decryption of the output addresses then each of the input users provide

**00:41:47**  an encryption decryption keys and decrypt his own output addresses and send the sends the output address which is encrypted by the next party uh to the next party the next party can uncreate the message actually then then adds his own output and it with the other party and

**00:42:18**  so on and then the last peer could actually unencrypt the output addresses shuffles them and create control transaction which also i remember that one of the papers if i'm not mistaken coin party told that the last pier have the control over the shuffling of the output addresses uh and then i tried to find some

**00:42:49**  implementation for that as you said shufflepuff and also in nxt however one of them was also an awful version and one of them has removed this console from the feature list from the wallet and for now i i couldn't find any chrome shuffle wallet to to test this actually kind of mixing

**00:43:19**  technique yes i don't think there is money in existence the bitcoin cash guys were using coins of uh but then they moved on their own scheme but they figured out which could actually be applied to bitcoin but i i think bobby sabby supersedes that which is sketch fusion and now cash fusion is in production which is having inspired by by coin sofa but not it's not going to fall

**00:43:52**  and and then there was of course coins of the plus plasmids but what did it contributed it made coin james much more efficient much more secure they given theoretical proofs and all kinds of stuff to that and they came up with this protocol called dice mix which was inspired by the descent protocol which goes back to the

**00:44:23**  huge research body of phononimus communication right if i remember there are three categories one would be broadcaster to cost where dandelion came out of that one would be onions which is which well thor came out of that and one category would be the the the mixnets

**00:44:55**  you know dining cryptographers and that's where that's where descent and eventually coin shuffle comes up come comes out grows out of concept for plus plus is dice mix protocol grows out of so this this was my understanding of the history there um anything to us argue it there

**00:45:26**  okay and here i have uh here i have something that you probably did not find in the research literature because i don't think it has ever been published on a on e-printer or or anywhere it was a github repository and this was built on coin shafter plus plus it claimed it made it decentralized and this was called byzantine cycle mode by an anonymous

**00:45:58**  pseudonym assault altar called sound dance which uh andre paul astra and and and the number of early bitcoin people were excited about it but eventually nothing happened with with byzantine cycle mode so so that that might be something to take a look at a unique interesting addition

**00:46:29**  could you please uh repeat the name of those developers so byzantine cycle mode by sound dance if i remember correctly the pseudonym and i know that it was published on bitcoin talk and github and on bitcoin talk andrew poastra was very interested in that

**00:46:59**  in fact he was the one who who suggested it to me back in the days what did it what did it do guys literally remember it was manipulating with some matrixes and trying to match people together or something like that honestly i never quite understood it so sorry usually i try to fill this in

**00:47:32**  all right and then finally we arrive to value shuffle which is coin shuffle with confidential transactions which is unfortunately not in bitcoin and that's the end of the coin suffer research line it was a very very well adopted research

**00:48:03**  actually too bad no final version that got used but you know the obvious um tennessee compared to chummy and coin join which which i described in in the zero link specification and and maxwell described it that what was i oh yes this was a

**00:48:34**  decentralized coordination with bitcoins of a plus plus even though i believe um there was the decentralization wasn't really figured out uh properly or in an implementable way because because everyone went for the bulletin board modern don't worry try to implement coin shaft

**00:49:05**  for plus plus i believe okay let's go down and and i haven't i have a notion to to coinjoin because you properly credited maxwell that he proposed coinjoin um which which is i i like to say he popularized it because

**00:49:35**  coin joining was around at the time for for a very long long time and and the earliest idea that i i could find that could be called coinjoin today was in 2012 uh on bitcoin talk by hashcoin so i i like to attribute to the

**00:50:06**  coinjoins to heshcoin personally and regarding chummy and coin joints that also wasn't maxwell who first proposed the idea but uh but an interesting renamed fellow on bitcoin talk called killer storm he he proposed it i believe in 2013 um what was his real name nothing much even interacting before

**00:50:37**  alex mizrahi [Music] pronouncing it like you would in hebrew but i i don't know if he pronounces the surname that way so anyhow i i i that's the earliest earliest idea that i found about xiaomi and coin joints which eventually ended up being implemented in in wasabi and in strange ways samurai but let's not

**00:51:09**  go that far ahead um all right and uh something to be added actually i have another paper uh which uh investigate the implementation of coin drawing techniques in those three wallets and then in that paper i provided the techniques that were adopted for instant maker maker taker uh

**00:51:43**  for john market and chao myan kong jung for samurai and wasabi uh however and there i explained that they adopted zero link uh and i have no idea uh after actually this discussion i was thinking that it's better to add zero link uh to the category of conjoined here in this paper actually and and i want to know

**00:52:13**  your opinion and if yes do you think it's better to also add a major taker by john market to this survey paper or it's okay to have that in the implementation of going jointex technique paper so i believe actually i wanted to even suggest that i think about joining market as something

**00:52:44**  completely completely different so it's it's it's in its new category in in coin joins because that maker thicker model does things so differently that i very very often encounter that i i should really not compare the maker thicker model in many of the times with with other coin joining implementations because because that's that's so so different that's

**00:53:15**  that's so elegant right like hey here is a bunch of people they all want to do coin joints uh for some fee and you can come and you can make the coin join yourself in a way how you want you're the taker pick some makers and make the coin join happen yes that's uh that's uh that's a completely different model so i would definitely add that as a category

**00:53:47**  all right so regarding zero link uh that i so so yeah i'm advocating for joining market now but i'm not advocating for zeroing because zero rank is not a type of coinjoin however i would advocate for chomi and coin join even though there was no really research paper there only the zero link specification that described it in a way that implementers can implement

**00:54:19**  it but xero link is not a type of coinjoin zero link was the realization that there are many other variables where users can ruin their privacy and they really tried to bring that together and and said things about best privacy practices so xero link is not a type of coin join it's a privacy framework for bitcoin wallets uh but xiaomi and coin join i think yes

**00:54:52**  that should be a category uh now what should you reference um yeah maybe maybe zero link that's that's probably the first and maybe the only only like comprehensive specification of chomi and coin join yeah perfect thanks so charming coin time will be added to the paper

**00:55:23**  but not fortunately all right and since we are at this topic i would like to bring up the only critique and i find i believe it's a critique but maybe because of my biases it's uh it's probably just a nitpick

**00:55:53**  of the paper which is there is a sentence there in the discussion an analysis bar part or multiple sentences where you are comparing coinjoin implementations or you where you are giving a few words about coinjoin implementations you start with joining market then wasabi then sunride and blockchain falls shared coin and

**00:56:24**  and and and this is what said what is said there samurai proposed tool which has specified pools where the users can join to mix their coin with other participants and create coin joint transactions so this is correct and then you go on to say shared coin which was a coin joint service by blockchain info in which blockchain if was able to find the inputs and outputs relationships

**00:56:56**  and this is also correct so here is two sentence those are both correct so what's my problem with this my problem with this is that you know if you're talking about blockchain infos flaw share blockchain enforcement that it is able to link the coins the input output relationships

**00:57:28**  together then uh you i believe you have to mention that samurai is also able to find the relationship because by default they collect their users xbox which is an instant download musician right it doesn't matter how much you mix if you have the xbox then you can find the input output relationships and and the counter argument to this is that use some drive with a full node which

**00:58:00**  would not expose the input output relationship which would not expose the xbox but on the other hand you are still mixing with people whose xbox are exposed because that's the default that's the light wallet mode that's the mode where you don't have to keep 300gb gigabytes of data on your computer so even if you're using a full node then you are also the anonymized by

**00:58:30**  exclusion because if your input and output is the only thing that is on the anonymized with the xbox then well you already anonymized by exclusion so that's it's a critique i have what do you guys think yeah i think you're correct like it's highly unlikely that like the majority

**00:59:01**  of whirlpool users would be running their own nodes so anyhow um all right do you guys have other topics regarding coinjoin implementations uh um i'm getting tired of

**00:59:32**  of hearing my stuff but i will still have a good story for patreon later on can you hear me sorry yep well no but i would like to know um because we can see that coin joints are probably the most the most

**01:00:02**  used uh technology for mixing and that's clearly because i mean the the same paper expressed this very clearly that is because it's probably the most cheaper alternative and also in the number of transactions is the only one that is requires only one transaction right so because it's a color collaborative transaction but

**01:00:33**  uh i would like to to know from simin if she shares these uh no no no as a conclusion but also as a as um [Music] how about the viability of the the the others uh alternatives that are not conjoined for example coin swaps um

**01:01:03**  in in in the sense of the cost also of course i mean uh also in the in the impact in the global um uh anonymity that they provide because for example just to to explain myself a bit better we can see that for example in the in this summary in this figure what all are all the

**01:01:33**  all the techniques are evaluated we have something like for example pay join that says anonymity set large for example right and coin join anonymity set small so how first what does it mean that anonymity set is large for pay joint and small for coin joint is this because it was evaluated in a global

**01:02:05**  context i mean no locally in the sense of each transaction in particular and again in in the from the point of view of the reality the real world um what's the what does she think is probably the the the way to to follow if it is conjoined the

**01:02:37**  the most realistic solution uh actually for for the thing that you talked about the the anonymity set i would say that uh first i tried to provide it was really it was quite tough to compare them over in

**01:03:08**  this criteria actually i just try to to explain what what it means and uh first i try to provide something some fears and some numbers for them but [Music] actually i couldn't for coin drawing and just i mentioned the problem is finding uh too many people and most of the transactions are confined by

**01:03:40**  the transaction size and also finding too many people uh to jointly create a transaction uh would be not easy and um in the explanation i just told that uh as commercial file and provide some better uh solutions for f part in finding the participants it could be

**01:04:10**  actually a medium-sized anonymity set as they uh in their paper and they provided price and i i guess if i'm not mistaken 15 50 parties you can for coin shuffle plus plus and for paging patreon yes this anonymity set in from the global view as you are hidden uh from all the transactions but for

**01:04:40**  conjoined base transactions with equal based month uh you need to have uh more input users to be the end to be actually to have a large and larger anonymity and it was my uh definition for comparing those techniques

**01:05:10**  and another thing that you told about uh the price and yes this one would be really this transaction fee and number of transaction would have uh uh would be a really really important things in in the adoption of mixing techniques for instance all the coins coin swipe techniques needs at least uh four transactions

**01:05:43**  and for coin join base uh the mixing can be done uh in just one transaction uh if the coinjoin uh if only we actually accept the coin join uh as was proposed by uh conscious by by excuse me by value shuffle or by a joint market for

**01:06:13**  the other implementation they provided uh first to mix the coin by coin join receive it in your own address and then forward these mixed coins to your desired address and even in this case we have a two transaction for one round mixing but for other contract atomic swap actually techniques we need at least a four transaction and i

**01:06:44**  guess this one would be a benefit of all the coin drawing base transactions thank you so may i ask uh you mentioned at one point that you are working on another paper which you mind talking about that or is

**01:07:14**  it too early yes for that paper we we installed all the conjunct wallets and then define [Music] some tasks including installing the valid generating the wallet and then funding the wallet performing the coinjoin transaction

**01:07:45**  and the last steps is uh sending this coin joint transaction to the destination address and then we worked we had a walk through over those three wallets uh to perform control transaction and in this walkthrough we compare those wallets in terms of some usability criteria and fundamental design criteria

**01:08:17**  for instance for mapping if mapping errors and also the usability criteria like ease of use and in this walkthrough we just [Music] perform the task step by step and then if we found some some problems or some issues or

**01:08:47**  some errors we just documented those problems and also suggest some solutions for those um problems and then for the next paper actually it was just worked ruled by two experts for the next step we would like to do a user study and ask users uh both technical

**01:09:18**  and non-technical users to perform these tasks and then we have we prepared a questionnaire and a form where they should answer to some of the questions and also provide their satisfication their time on tasks and the errors that they received or any difficulties to perform the task and we don't

**01:09:50**  with that user study we can provide uh problems maybe that you users may encounter in performing conjoined with those walls well that that's interesting because now we are working on a new version right and the our focus was precisely on improving the usability of

**01:10:22**  our wallet and making and removing all the painful points and make it as easy as possible i think whatsapp wallet 2 will be absolutely different and much much better in usability that was a wallet one and the coinjoin part will be in fact uh transparent from the user's point of view i mean the user will need to do

**01:10:52**  absolutely nothing to to participate in a coin join it will be done in background uh and and that's all so it's i think it's in that aspect will be really hard to to to improve further further because there is no it is impossible to make it easier right uh but i don't know if we can have wasabi wallet too ready

**01:11:22**  on time i don't know what's your your time your schedule anyway uh the the the first part all the send receive parties is it's almost ready it's 99 ready except the coin joint integration that is not it is not done yet

**01:11:53**  and uh do you have any estimation of time very where we can see wasabi too we have a plan and we estimate that around 10 weeks we can have a preview an internal preview but of course we can share it with you too anyway everything is in github you can just clone the

**01:12:23**  repository and get the the latest version but the the one that will um have everything let's say in a alpha version or preview version um it's it will be done we hope to to have it done in around 10 weeks from now if i'm not mistaken

**01:12:54**  so yes it would be a really bad time to do they use their study for wasabi one and we didn't know that well i mean it's it's certainly very interesting because because what we do right now is try to find flaws in the current wasabi user experience and do those things differently in a more

**01:13:24**  seamless way so if you find the same flaws then oh well we attempted to fix that but it's pretty likely that you are going to find flaws that we didn't even think of so that that will still be very interesting for us for sure all right um any questions

**01:13:57**  to the author about quenching implementations or let's move on to pay join then pagerank is so patreon has never been in a research paper so i was wondering uh what what did you

**01:14:29**  you found worthy of examining yes actually i first read a blog post in black history and from which was pay to end point and then i found master pay which was uh sent to

**01:14:59**  like linux foundation i guess and then i found uh actually i found it under the name page joined by gibson in his workbook and back then i saw that in 2020 most of the wallets are implementing this technique and that's why we added this technique to to the paper and we also we also

**01:15:32**  had a short paper about unnecessary input effect in pay joint transactions which we considered if if these unnecessary input inputs can re flag the page on transactions in the future and and yes that's that however i also i remember that

**01:16:03**  chris belchers and send an email to my list that it has not been adopted mostly by users i have no idea maybe maybe most of the users are not familiar with this technique and um the community should maybe advertise this technique

**01:16:38**  the communities is advertising these techniques this is possibly the most advertised privacy technique in bitcoin precisely precisely be besides precisely because of how it came to existence and you mentioned that it was it came from block stream which is kind of correct so what happened there in 2017

**01:17:08**  or 18 is that actually i was personally i think we already started working on on wasabi the the current version of wasabi and i think lucas was was around at the time and and uh there is a guy called groupers on twitter and he's working for black stream and he brought together in london a number of

**01:17:41**  number of people for coinjoining workshop that's that was the name and you know it was that so there was fro the koi for coin plus shift [Music] market me adam beck was fully with us you know in a in a small room in london that

**01:18:14**  just they didn't do any preparing so all that happened is that these very smart people there were more right like around 10 or 15. uh some of them wants to be anonymous so that's why i'm i'm trying to think if i should name someone's name but anyhow so some people who worked on bitcoin privacy before were brought together into the same room and

**01:18:44**  without any any goal so so what do they do we start to start to brainstorm first we go through all the bitcoin privacy techniques uh the things that you wrote in your paper up until 2017 or 18 and then started to to come up with ideas what should we do and it was a seven day workshop and

**01:19:15**  on the fifth day i realized that the idea that we were pursuing had a very serious flaw so we just realized that we were here for five days and he didn't come up with anything at all anything not dirty you know and and then adam gives on and i was talking about

**01:19:49**  going through some more exotic privacy technologies and they found the idea that satoshi nakamoto was doing in 2019 which is a2ip sorry 2009 2010 people were able to pay each other to an ip address uh which we realized that wow that it's kind of revolutionary too but it

**01:20:19**  was removed i mean of course because ip addresses are not very secure to pay to but the connection between two peers is is huge uh let me get back to this later but we didn't want to call it pay2ip because of course this is secure so you could possibly pay to a domain name too or you could pay to uh an onion onion domain at or network domain

**01:20:52**  and and so we decided to in c sharp there is uh there is a class called end point which encompasses all these things and so we decided to call it pay to end point and you know this was about building up a secure connection between two machines and if you do that you have a second communication channel that you can do a bunch of things uh this is patreon point for example you

**01:21:23**  can you can do just simple chat messaging anonymous chat messaging through audience or you can facilitate marriage avoidance right i think vitaly came out with a concept or wrote it in a in a in an early article of him that merchant boy dances when you ask multiple addresses from the server from from the receiver and then you split the money that you're sending so you

**01:21:55**  could do that or what else you could do oh we could decoy joints we could do these strains they're gonna graphic coin joints those look like a payment but to have much more interpretations and well that's later on being called pay join so that's what pay join is about making transactions

**01:22:25**  making coin joins those are not known to be coin joints and that controls blockchain analysis now why i you you had a point there that it did not get adopted even the wallets implemented it and and i have a very specific critique to that which is at the time they were trying to figure out how to do this with bitcoin

**01:22:56**  urls uh you know bp 21 urls an extension of bitcoin url and you know my problem with that was that that's not how people use bitcoin uh they are using those are merchant scenarios merchant when you're you buy something from a website that's that's when you use bitcoin url all right so we can encode bitcoin urls into qr codes

**01:23:27**  so at least the qr code usage is satisfied but the main usage of bitcoin which is you know uh copy testing addresses that that that's not satisfied with with the big 21 urls uh because you can't teach it's really hard to teach the user to hey even just uh segment bitcoin address was a

**01:23:57**  huge mess in the ui because wallets couldn't stand to that and then all kinds of support requests were coming so so making the user use bitcoin urs they don't understand they barely even understand to give each other bitcoin addresses uh so so i believe that's the order of the adoption and if we if

**01:24:28**  that the current attempts are pointed toward using bitcoin urls and as time passing um i'm getting more i'm still not very positive on that approach but i'm much more positive than i used to be so maybe that could work uh who knows we'll see so so the current attempt buster pay right that was the first one

**01:24:59**  and then uh vip something something big number uh was by nicola d'oriel and mostly nicoladore it was another implementation and of course the joint market guys were doing their own implementation then went on to bitcoin you are uh of course wasabi is supporting the sanding part of it and so maybe it can work

**01:25:31**  uh who knows but i believe the the interesting thing would be a pay to end points hopefully and i really hope because this is gonna happen eventually some kind of uh simplification of bitcoin wallets will happen which is we may replace the addresses with the domain name or or something but hopefully it will happen in a in an anonymous and secure way and

**01:26:04**  pay to onion would be would be i think an idea way to do secure communication because if you have that then back you can do the pay joints and one and and know the user is doesn't have to notice that he's even doing pay joints uh doesn't have to get familiar with multiple things because if paid to onion like system

**01:26:34**  comes alive that would be that would would make the and it will that would make the user an option much easier

**01:27:05**  all right is that all about pay to endpoint pay join then maybe as a closing session we could have a few questions stood out or what do you guys think i would like to make a comment about way to to end point i don't know if if it's

**01:27:35**  okay or we could do it after this session is the same for me go on well first of all that um let's start with a pay to ip right i think the name pay2 it was known as pay2ip but in fact the name is quite misleading because it should be called something like paid to node because you cannot pay to any ib the idea was to

**01:28:06**  pay to one of the nodes that you were connected to i mean your node was connected too and the problem basically is not the ip the problem is that there are no way to authenticate the the pie so for example if i'm running my node and you're running your node that you give me your ip address i i cannot make sure i'm paying to your node because

**01:28:37**  basically the connection is not authenticated um so basically all they pay to end point and pay to ip or paid to whatever is basically the the problem is okay i authenticate the the the other the other end right that's why for example pay to onion could be good because basically we are sure that we are connecting to the to the right um peer let's say

**01:29:09**  um but well that's the first thing and the second one is that uh now or right now we are still working with these um bitcoin addresses right that are okay for normal users probably because we we we can expect users are not all the

**01:29:41**  time online by a patient for example it's the idea is like okay this is good for merchants right but merchants are all the time online right so why to why to use these when we can use something more um how to say i mean there are there are other ways to authenticate the users and know only by

**01:30:13**  a a a dns or um and on an onion address i mean if we can identify some somehow sorry authenticate in some way the the the other end well all the problems are are ourselves i think probably i i'm missing something but i think the problem is basically authentication

**01:30:44**  that's all and being being online receiver yeah oh yes yes of course yes i i completely agree so in conclusion pay joints are

**01:31:15**  are probably going to have a much better chance you know everyone is online world in the future so even if it doesn't happen in the next five years there it is going to happen in the next 10 years because everyone i believe everyone is going to be online all the time in 10 years so so don't have to be impatient about it

**01:31:47**  yes but what i mean is that the fallback mechanism to pay to the address in case you cannot connect with the with the server with the receiver that's something that is okay now but i think in the future that will be no necessary so if you can remove that that would be pretty awesome right because you don't need i mean you can i mean bitcoin addresses are uh are not good i think pro

**01:32:21**  is are not use uh good for for usability the same happens with vip21 that those url addresses all that is is confusing and really confusing for for normal people all right looks like we just converge any other comment or question

**01:33:03**  actually there are there are some points in this talk that were really perfect and i would add them to the paper if it's okay from your side now we would we would be happy to maybe maybe then we should say a few words about ourselves uh just just don't you know who you're talking with uh

**01:33:33**  i suppose except me because you probably know my work at this point but let's go through the course who are you sorry sorry how do you justify your wretched existence sorry i i i was uh i'm sorry i i was

**01:34:07**  uh answering uh a question from my wife in another chat so i'm sorry can you repeat the question oh we were talking about that maybe we should say a few words about ourselves uh so shimmy knows who she was talking to today oh okay yes perfect well um i'm lucas i'm a wasabi developer uh that started contributing with um

**01:34:40**  wasabi wallet from from the beginning i mean after we bring or after adam rename the magical crypto what no the height and wallet 2 magical crypto wallet i joined to him so it i started working with him in the magical crypto wallet that then was renamed as a wasabi wallet and basically

**01:35:11**  that's all i'm now working with nothing much um and adam and others to implement the huawei savvy protocol um what else well i think that's that's enough thank you lucas nothing much thanks

**01:35:43**  i think i started harassing adam around 2000 maybe early 2018 or something um and uh yeah i just had many opinions about uh wasabi and uh eventually uh got involved with the project and uh so now we're working on the the wabi-sabi stuff

**01:36:19**  thank you ruffa uh hey hi um i'm basically just a bitcoin pleb trying to learn uh as much as possible about all these like bitcoin privacy techniques and yeah really interested to like listen to this discussion all right by a psycho are you with us yep and i'm also just a

**01:36:50**  blab and just interested about bitcoin and privacy things and okay we have btc fud here oh i'm gonna also plead the club all right i should have mentioned that you guys don't have to give an introduction if you don't want

**01:37:22**  to want to stay more super nameless okay so so yes we we would be we are very happy that we succeeded to provide you some insights of how things are coming together adam gives an increased bachelor maybe also very good to to talk to because they they know that the teacher too

**01:37:57**  all right questions to the author i was actually just wondering like uh what got you interested about like privacy stuff overall actually doing this research when i'm talking with normal users the first question from them is when

**01:38:29**  they they ask me what's your teaser about and i tell them i'm working on blockchain privacy and the first thing from the normal wizard is it isn't the blockchain is private why do you work on privacy the blockchain is private and uh this shows that most of the normal users even um even don't know that there are some uh privacy issues in the

**01:39:00**  blockchain and uh for me it's it's quite it's quite interesting that uh you also need uh some some actually some solutions to uh to provide awareness for the users in this community and um this makes me really really eager to work on this [Music] area actually

**01:39:34**  yeah i'm like honestly impressed about the research you've done like there was so many more implementations that i didn't even know about and yeah really great too that you made this report thanks yes but by the way i i i you know i i i agree because you know this work it's pretty impressive because

**01:40:05**  it summarized many of the the research that we are uh have done before but also there are a lot of technologies that you have investigated that we didn't or at least i didn't know about that so i have harm work to do so thank you thank you very much for that and also thank you for the opportunity to present the paper and have your

**01:40:36**  insights about the paper all right are you holding holding there would you would you like to leave already do you have to leave or or can we continue the questions

**01:41:06**  for me it's okay if there is any all right then what else do you guys have i just wanted to mention that yeah like whenever you or if you feel like it's yeah there's probably a lot of things to improve in bitcoin privacy and yeah like many projects will be really

**01:41:37**  happy about these kind of like overall reports comments contributions all of that okay we are running out of questions but not out of topics so i would like to propose

**01:42:11**  that we continue with something that i i i this afternoon i come up with a theory of privacy and it's pretty complex so i would like to share that with you guys but yeah the last opportunity to ask questions from the author

**01:42:48**  okay so would you like to talk about privacy in a very abstract sense try to define it and figure out what the hell it is let's go all right so what is privacy

**01:43:20**  how would you define privacy what definitions do you know about privacy i like the definition of like you having the possibility to selectively reveal yourself or parts of yourself but that's a pretty big one so the i believe the most commonly used definition for privacy

**01:43:52**  is it's just used as a word like it would be meaning secrecy or anonymity but the formal definition that you just mentioned goes further than that and and we should mention that there is a legal definition which was defined very early the right to be let alone but let's let alone the law let's let's go with the

**01:44:24**  the formal definition which is your ability to selectively reveal yourself to the world what what's what does this mean why why is it different from secrecy all right so it is different because

**01:44:56**  this is not the state of being this is the ability to choose the ability to choose your boundaries or as i came to a definition of privacy as the ability to define and enforce our boundaries

**01:45:28**  privacy is an ability to define and enforce our boundaries do you guys think that makes sense actually uh i agree and i remember when google provided its social network that they also had a similar definition for the privacy and

**01:46:01**  it was uh defined by circles you had lots of circles and with closure circles uh you you could put your closer friends and i guess uh it's it's com completely true also in our lives as we have some circles as you said boundaries and in those circles and in those boundaries which at the center of that and we are

**01:46:32**  actually and uh in these boundaries we can share the information if the if a friend or if someone is in our closer the boundary then maybe they they know more about our information and if they are far from us they know less

**01:47:05**  that is certainly something i'm going to geek on uh that's for sure thank you that's that's actually yeah it was very insightful and relevant okay so privacy the ability to define and enforce their boundaries uh anyone thinks that's not a fair definition for privacy isn't that i i want to prove to you that this is the essence but but do you have some entities

**01:47:38**  do you think intuitively that that might not be right okay so now the next thing what i want to do is to figure out and and this is i didn't do well because it's hard but figure out what are the sciences

**01:48:10**  those are studying privacy the ability to define and enforce boundaries what sciences are doing this and i was able to come up with a couple of um dimensions to this one would be so since privacy is an ability

**01:48:40**  then we have to say that well what kind of ability is it individual or an ability of a group or something else but this is the distinction i came to individual ability and ability of a group and then there's the define and enforce our boundaries so then the question naturally comes that what what are

**01:49:14**  how would you say our boundaries what what would be the largest largest the most the best way to divide our boundaries into categories this would be the classic three mind body and the world so we want to enforce our boundaries of our mind which is what information

**01:49:45**  we are sharing to other people and this is an individual an individual has a mind and and then the body that you know if you get sexually assaulted that is an invasion of your privacy that is

**01:50:18**  you're failing to enforce or define your boundaries of your body so that's in that's another diamonds in there and finally the words which would be which would be an individual or a group would be able to enforce their boundaries to culture let's say to other families

**01:50:51**  or to other countries people or or even our boundaries with the world and the universe the natural world nature right so against culture and nature that's that's the word uh so so we can only see privacy as uh you know if there would not be it it would be only me then privacy privacy will always against other

**01:51:24**  or always projected against other people or or or if you want to bring in this philosophical direction that the word is the the natural word is also something that you want to define and enforce your boundaries it doesn't really feel right to say that we have privacy against the world but if we we talk about this

**01:51:56**  definition what i came up with then then it would make and maybe there is something there so it actually very very corresponds to the brain to just just as a interesting story there that we have the cortex the limbic system and the reptilian brain right the cortex is what thinks what reasons um in plateau was calling it the man and freud was calling

**01:52:26**  it ego uh basically or that's what corresponds to it and there is a limbic system with chair basically your emotions plateau was calling it the lion freud was calling it the super ego and the reptilian brain which is your your body in in this privacy privacy metaphor the cortex would be the mind of course

**01:52:56**  the the reptilian brain which is like you're hungry and this kind of things that would be your body in plateau the reptilian was the monster and freud that's the freudian eat so suniyah doesn't matter just interesting thing the point is that the mind what

**01:53:30**  so we we can come up with two with sciences here that what is the science that is examining on how to describe the mind but what's dealing with the mind what is that science that describing not applying

**01:54:05**  what science is trying to examine the mind guys am i muted nope uh i don't know maybe some kind of psychology study uh-huh psychology is one of them yes [Music] i'm sorry assuming i can't hear you

**01:54:41**  social sciences social sciences huh okay so i came to the conclusion that there are multiple sciences those are studying in the mind uh social sciences in the like anthropology you know that's

**01:55:12**  looking at culture and these kind of things that they they are saying that that's the that's the thing what they are studying the mind or something like that and psychology right that's studying the mind on another level uh there is of course neuroscience that's studying the brain itself and ultimately the mind there is linguistics because we are communicating our minds

**01:55:43**  to each other with our language so so they say that's another thing that's that's uh studying the mind and finally there is artificial intelligence she's trying to figure out how to create a mind like information processing system so so that's that's another thing and these all of these are being integrated or trying to be integrated into one

**01:56:16**  science or trying to have cross-disciplinary conclusions between them and that science is called cognitive science so that's why cognitive science is for example called the multidisciplinary discipline because there are many disciplines that it is trying to dive into and the only thing come on in those is that all of these disciplines

**01:56:48**  or they are choosing from all of these disciplines the parts those are studying the mind so i would say cognitive science tries to define define the mind and cognitive science is trying to figure out what's our meaning what we should do and getting into enlightenment those kind of stuff or at least one guy that i was watching on youtube

**01:57:20**  was going into uh and he's a cognitive scientist so anyhow the point is that that's what describes the mind okay what science is trying to enforce the boundaries of the mind trying to enforce safe heat information safety financially information

**01:57:53**  uh because you know tools are we are told using creatures and those are basically become part of our body and you know our financial situation is basically a tool so so what we are doing with our finances that that's part of ourselves that's an extension of ourselves uh so so what science is trying to enforce boundaries of information and

**01:58:24**  the information like things like bitcoins safekeeping private keys yeah it was just i don't know how to correctly form it but you're like compressing all kind of information or like yeah whenever you're

**01:58:54**  kind of like creating password or passwords or hashing you know like that's that's kind of like compressing certain amounts of like data into like behind a lock but something that it's still even easier for you maybe to remember or decrypt when needed but i'm not sure if that's like what exactly that what you meant

**01:59:25**  guys ideas what science is trying to enforce apply that the content of our minds doesn't get to other parties or or well you know and forcing is not only hiding but

**01:59:56**  sorry um so revealing yourself to the world so basically enforcing is not only hiding the information but also revealing or proving the information right it could even divide that into two categories so so what what is the science that does it that tries to hit the privacy from other other people or other groups

**02:00:30**  i mean it's not like science or at least not that i would know uh what kind of scientist science it is but kind of like these research wherever you are looking into for example uh you know these like tails uh certain actions that make it really clear that you are lying for example so these kind of researchers might be kind of like wanting to you for to know whenever you are giving out an information that you

**02:01:01**  actually wouldn't want to give out or do you mean like cryptography or something that's exactly what i mean but i'm not very happy with that because it seems like it's such a it's a sub category of mathematics yet i cannot think of any other science that would be dealing with with

**02:01:34**  constraining information in dealing in an adverse area settings and it can prove things and it can hide things that that's what cryptography is about maybe a more philosophical part of cryptography where where the math is not that heavy but rather the cryptographic thinkings the

**02:02:04**  cryptographic patterns that those can be you know applied in real-world situations completely offline too right it's game theory cryptography that's my best best guess but yeah any anyone has any any better one because i don't

**02:02:42**  i don't have any anything better in mind but that's an interesting point okay so the next one is also something that i did not i may have found the right one but i'm not 100 sure about which is what's the fact so again privacy is the

**02:03:14**  ability to define and enforce your boundaries of the word your boundaries so and now we move on to the body level we went through the mind and now we move on to the body so what what is the thing that tries to define or enforce boundaries in the world like what

**02:03:45**  what's in the body level so what describes the body what is dealing with the body i would say like like self-defense tools i thought about that too uh you know yeah self-defense and martial arts and and things like this uh but then i generalized so this is the

**02:04:16**  enforcement under the enforcement right but then i generalized into you know the whole health industry the fitness industry is basically trying to enforce your oh you know pick this drug right that's an invasion of your privacy

**02:04:51**  but in in the level of your body so they are trying to help you what substance is to introduce to your body and that kind of the enforcement part that now you have the tools to take this drug and make your life better and by drug i i don't i might mean party drugs but more like a medicine

**02:05:22**  or creatine or multivitamin or vitamin d what have you and and the fitness part is like possibly all the sports that just makes you your body work better in the world is is just a better way for you to to use your body in the verse so that it's kind of

**02:05:52**  i think you can generalize to the whole heart industry that is set out to make your body work better and and special mention to martial arts when your your privacy is being invaded by like in a very not good situation like a sexual assault something like that so that's that's my thinking on the

**02:06:24**  enforcement part making yourself your body work better is basically your body operate better in the world um okay so this is also something i'm not hundred percent satisfied with for the defining i found biology and all the some biology sciences

**02:06:54**  that's a big big big thing there but that's yeah what do you guys think i think biology is what describes the body figures out what your boundaries should be to what kind of substances you're introducing to your body uh what kind of i don't know movements you need to take freeze or fly or all this kind of stuff uh not not sure about these things

**02:07:26**  but yeah so the fitness industry and martial arts and that is probably the enforcement of of conducting your body in the world and being able to define your boundaries yeah and overall i i think like all of these physical things like just for example doors or curtains or things like that they are kind of like yeah protection for your like physical privacy

**02:08:02**  we'll put that into birth category or yeah maybe maybe it should come here yeah first of all i don't know closing is it's a privacy tool right you choose

**02:08:34**  your clothes you choose what you're revealing of your body and what you don't so so well you can't call closing science but um yeah there is a there's something there curtains and yeah i mean like yeah somebody probably did some research on why not to build

**02:09:04**  your house walls on glass and i think even though it's not maybe like the most important part i think privacy is also one of the things that they had to consider and with like many yeah many of these things like yeah with clothes and whatever they kind of like do have to think about the privacy side and what do people reveal

**02:09:34**  all right so let's go to the last and most abstract category which arguably shouldn't even be here but maybe it should be here let's see so if privacy is the ability to define it then force our boundaries then think about boundary as the world and culture

**02:10:07**  so not nature i'm not sure we should go that far but to sculpture so boundaries is other people other groups of people your group of people so it's a group ability not an individual ability at this point so your groups of people uh try to enforce boundaries against other groups of people

**02:10:37**  now what what's what is the science that defines and what is the science that enforces these boundaries let's start with the define what science defines tries to understand the world in a sense in terms of

**02:11:10**  groups of people's relationship how they gonna behave to each other things like that that's where i arrive to economics because i think that's what is trying to capture the the significant things

**02:11:41**  um in terms of groups of people interacting or people being able to live with each other and define their own boundaries and don't have to all the time fight on the boundaries yeah if you think about that that's what we do people we just fight on the boundaries because we can never

**02:12:11**  come to consonants on any lines we write them in the sand sonia economics is what i came to that's trying to define the boundaries between people groups of people what what is that does that make sense yeah i think it does like that was also

**02:12:43**  the first thing that came to my mind and also like if yeah economics and like philosophy some of them at least talk about like individualism and yeah even like how to there's a lot of like researches also about like how to protect your uh yeah your individualism and how to actually make or like enforce these boundaries against other peoples and yeah about like

**02:13:15**  your own uh autonomy and respecting others how about enforcement what is what are the sciences those can can benefit from economics the most

**02:13:52**  maybe those ones those make a difference in the world and that's probably politics and technology and and you know i i don't know if this is science but the creation of ideas i don't know if that makes sense never mind so politics and technology that's what i

**02:14:23**  come to again i'm not really happy with this but since listen upon for now and you know philosophy is what we are doing right now because you know philosophy is science of

**02:14:54**  integration philosophy is integrating sciences together so we are coming up with the new science the new science of privacy this is the first step you know integrating sciences together just to try to find out what privacy is but you know i believe if a person who who gets his privacy right on the level

**02:15:25**  of the mind body and the world and that kind of unifies this being and not and not being that anxious anymore because he knows exactly what he wants he knows exactly um how to how to define these process these

**02:15:56**  levels and where to enforce and where to reveal their where to hide and where to reveal their the things that they want to or don't want to reveal or hide so well that's philosophy the way of the privacy

**02:16:29**  let's get the also like i'm not sure if this is uh like directly connected uh like to the topic but in my opinion like about creating these boundaries or like it wasn't like research per se but in my opinion like one of the most insightful uh like literature that i've seen or read about like these kind of making boundaries between like groups of

**02:17:01**  people i think it was the second realm book like there was a lot of like really interesting and deep like strategical things about how to preserve and defend your own uh yourself or your group's privacy and all kind of like small psychology things about like signs and yeah different ways to communicate with one another

**02:17:33**  and stuff like that so would you say that but what it's doing is the offline equivalent of cryptography um not maybe exactly it was mainly in my opinion like um like if you want to be left alone type of thing

**02:18:04**  there are certain things that you must consider like for example like how visible are you to others and you know you kind of do want to signal for your own people that's maybe like what you're doing and what is going on over here but you don't want others to know about it so yeah kind of different kind of like flags or um whatever things that yeah the most of the people may not

**02:18:35**  understand but you can kind of communicate in the physical world to your own people i mean that sounds like the offline version of cryptography as far as i understand cryptography yeah now that you said it yeah kind of yeah i had a lot of ideas back then that you know are is

**02:19:05**  a bunch of cryptographic concepts different things society generals and all kinds of things and you know how often would it be to just try to come up with reverse scenarios where this cryptographic concept could be useful without computers i think there's a lot to discover there like isn't kind of like uh for example

**02:19:37**  dining cryptographers are possible to like do in a physical world right uh-huh exactly dining crypto reverse it's a it's a good one all right guys that's that's all about my crazy new

**02:20:11**  theory it's in the future or might not but uh anyhow thank you for hearing me out i think you can stop the live stream what do you say yeah sure this has been a good discussion all right then thank you guys for coming and if you would like to stay for a non-recorded conversation

**02:20:42**  then please stay if you would like to leave then please leave in fact leave any time you you would like to don't feel shy about it um so thank you i want one last thing uh i was just wondering if uh simin wants to tell the viewers maybe like where they can uh find you or yeah send you a message if they have some ideas or yeah where to just follow your work

**02:21:16**  actually currently the paper is on eprint and my email also is there and then they can contact me via my email all right all right thank you ruffa i should have definitely did that anyhow so thank you guys for for being with us did you enjoy the episode

**02:21:46**  it was it was really like the compression of all the previous wasabi research cards into one episode or at least the topics were there or like that so i'm not sure if anyone is able sit through these really difficult concepts from the beginning but if you did then i'm sure you

**02:22:18**  did enjoy this episode too so thank you and and stay around for uh for non-recorded conversation bye bye bye bye

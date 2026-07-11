# Wasabi Research Club #12 - Why I'm not an Entropist with Harry Halpin

- Playlist index: 12
- YouTube ID: `hl4yyXPy3q8`
- Video: <https://www.youtube.com/watch?v=hl4yyXPy3q8>
- Duration: 1:12:53
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:01**  hey welcome everyone for another wasabi research club conversation this time we are going to go through a paper from Paul Severson called why I'm not an entropy the outer is the inventor of the onion routing protocol is not working on tour right now and since Aviv is not here there is no presentation on this paper right now so

**00:00:33**  I'm just going to read the abstract one line from the conclusion and let's see where we go from there so what does it mean to be anonymous in network communications or centroids thesis is that both the theoretical literature and the deployed systems have gotten the ants were essentially wrong the ants were have been wrong because they apply the wrong metric to the wrong adversary model I indicate problems in the

**00:01:06**  established adversary models and matrix for anonymity as well as implications for the design and analysis of anonymous communication systems so this is the abstract it might be to obstruct but hurt but there was a nice quote from the paper that that actually explains what it really wants wants to prove that the central the central point is that the model on which all existing work on

**00:01:36**  anonymity the entropies model is broken for open or widely shared communications so he doesn't like the the entropies model that's that's the point there and why we see some unfortunately the the outward I couldn't reach him maybe I sent the message to the wrong email address so he is not with us however we have with us Harry from Network who has

**00:02:08**  some interesting context on the on how this paper came around and but the halter might be thinking might was thinking when when he he did this paper so Harry I give the words to you so could you start over but you but you started saying just before the show yeah so I'll just give a little bit of an introduction to this paper you know

**00:02:40**  soso to to sort of notes first of all [Music] this paper comes from a long-standing argument around how to build anonymous communication and I think in order to understand why this is billion ominous communication systems are difficult it's useful to compare them classical cryptography so you know for years people build crypto systems and maybe

**00:03:12**  they work maybe they get in and eventually they they sort of boiled it down to the dogs whole security you had a well-defined adversary I'm sorry we are losing you your voice is just getting lower and lower over no it's not

**00:03:43**  is anyone hearing it I'll just try gets close to the microphone yeah no it's good yeah okay so I'll just what I was trying to say is that essentially anonymous communication systems people were building them but they didn't really have any principles to understand

**00:04:14**  why one design would be better than another design so in particular you know why would for example tour which is called an onion routing system be better or worse than a mixed Network and a lot of this comes from essentially a misunderstanding that happened very early round probably 2003 or four when tor came out so pulse iverson weirdly

**00:04:48**  enough was a philosopher and like many philosophers he he couldn't find a job and essentially the US Navy didn't have huge budgets so they hired philosophers because they knew about logic and they thought they could train them into computer scientists cheaper than actually hiring computer scientists and one day one of Paul's friends had this he said well Paul would be possible every time I connect to the internet I leak my IP address and would it be

**00:05:21**  possible to build a system where this doesn't happen and Paul had never thought about this question before his background was actually in something called epistemic logic but he kind of had this concept which became Onion Routing and the concept is basically the only way you can get anonymity is by passing a message through essentially a network of strangers and you know at each point

**00:05:52**  does it lay encryption you unwrap it and that that was really genuinely kind of Paul's insight now the problem is Paul was not aware that David charm and other people have been working on mixed networks since the 80s and mixed networks basically he said if you have a sender and receiver you hand packets to a mixer and they basically shuffle these

**00:06:23**  packets like a deck of cards they mix them and then they launch them all out at the same time and because they've all been sort of launched at the same time and their order has been essentially randomly permute 'add you can't tell if the packets are encrypted as long as different senders are sending packets to the mixer and different receivers are getting it that the packets who the senders and receivers are and that's the goal of

**00:06:53**  sender and receiver unlinked ability and mixed networks were built so that even an adversary which is observing the entire network you know for example the NSA couldn't tell which sender was sending which message the what receiver with any real advantage now what Paul now people kind of you know mix Network

**00:07:23**  said they did this but there is no really way to quantify there's a bunch of different mixed Network designs which design is is better than another for example should you have one mixer so you have a chain of mixers should you have a peer-to-peer network of mixes there is all these different designs being thrown around and eventually George donita's who was NIMS co-founder but unfortunately now at Libre and Claudia Diaz kayuu loving but also now at NIMH

**00:07:55**  basically simultaneously thought up in 2004 they said well the way to measure in an enemy is not just an enemy set but entropy entropy is a well-defined mathematical notion we can say that you know given one message we can quantify what the possible sinners receivers are using entropy metrics and we can also kind of chain those metrics so that we can say well the message us this much

**00:08:26**  entropy in this hop this much entropy after being mixed for so long if this much intra peed another hop and that Paul had no concept that that work was even going on so he independently thought of Onion Routing at or and then when he submitted the Tor paper to this conference call the privacy enhancing technologies a workshop they pezzi said oh this is a weird mix you've invented and I'm all basically

**00:08:56**  like well that's not the point I'm not trying to mix traffic tor doesn't mix traffic we're not concerned about an adversary that watches the entire network we're concerned about hiding IP addresses and and you know trying to open circuits basically to allow and he thought this was a much more real-world design and now actually thinks that the the Snowden's latest book permanent record we actually know that before tour

**00:09:27**  but actually what happen is when the CIA wanted to for example do a google search on someone they basically had to open a whole operation you know basically buy a computer and go to some weird place make a fake company just to basically do Google searches without revealing an IP address that went back to you know CIA gov that's in you know Snowden said well tor is great because it does defended the IP address so the CIA did have to do spend all this money anymore and tor is a great system

**00:09:58**  it's it's the and when Paul Fogg tour and Roger and Nick actually built it it was the only real working anonymity system mixed networks were only used for what was called cyberpunk email remailers so they send anonymous emails to people and people to be honest Mixmaster which nicks from tor worked on and roger who eventually worked on tor worked on with george these systems like Mixmaster from lance s men and makes minion from george roger and nick they

**00:10:30**  never really took off they were used by cypher punks but they were kind of used unusable and analyst problems you send the message you never know if you got a response it was really tricky Justi just to make sense of them for ordinary users while you know paul argue that tour was really easy to did one thing and did it very well in the he felt it did it you know what the people the crazy people were interested in mixed nets we're doing was a bit wacky because in reality

**00:11:04**  you know you don't have an anonymous set that most adversaries know about the internet is not a you know uniformly connected you can't send messages out all at the same time the network has all these structured links kind of built into ISPs by default and he actually argues I think he argues in this paper pretty successfully that even though tor doesn't really fit this entropy based way to define an M&E anonymous

**00:11:34**  communication systems it's a it's a it's it's it's it's fighting it's fighting a realistic adversary so he's really arguing that entropy and anonymity sets are not the best way to measure the success and the performance and that just the capability of a real world anonymous communication system my opinion on this is at the time that Paul wrote this he was basically right but

**00:12:05**  that now weirdly enough you know 10 20 years down the road it's actually the threat that Paul feels unrealistic an adversary that can watch the entire network and record all the communication between every link is actually realistic so that's kind of my disagreement with Paul but I think that's some context with the papers Paul's trying to defend tor against people who says all this system it doesn't really produce great entropy it's not as good as I mixed that

**00:12:36**  it you know it doesn't really have a good definition for why it's anonymous or why it's more secure does that make sense that explanation totally okay so I mean I don't know I mean I'd like to hear what people think about tor and entropy and defining anonymous communication I'm just thinking that I always knew there's something wrong with tor and that kind of like explained it in some

**00:13:10**  sense within some sense some sense I mean I wouldn't say that there's anything wrong with tor it's just that what Paul's arguing is that tor has a particular threat model which is you know it's trying to hide the IP address in the origin of large amounts of traffic and that doesn't rip that threat model which is realistic doesn't have anything really to do with entropy I mean I would

**00:13:42**  argue Paul was right at the time and now time to change the bit but I still think Paul is a point that anonymous systems aren't easily mathematically definable and so in classical cryptography you know you have these very nice precise formal definitions of security like you have ciphertext and plaintext and given some ciphertext can I get to the plain text can I fake a signature can I I mean these are very well defined notions and

**00:14:14**  you don't really and this is I think the philosophical point of paper you don't really have these definitions and at least in a really well understood form in anonymous communications and maybe a simple something simple which seems correct like entropy might not actually be the best way to define how an anonymous communication system should be judged so sorry guys I had to leave for

**00:14:46**  five minutes but I can I can actually say something what what you just said I'd say I I don't at least from my impression or impression I'm pretty sure that this is not really about the title is a bit click Beatty but this is not really about why his is not an entropy what what is arguing is that entropy is not sufficient in quantifying anonymity

**00:15:18**  because because of Tor because you cannot quantify because you cannot cannot put the entropy swaddle into torso you need some some some more more things that how you would quantify the unanimity and compare it between different anonymity networks and he had he had a solution proposal but he desirably go into it and I didn't really

**00:15:49**  understand it because this is a how he puts it it's a breaking paper it's not a solution it just this wide anthropometric would not be sufficient in in in comparing anonymity systems would that be the same impressions or or or or did you guys think that this this is really just just saying that no the anthropometric is completely wrong we

**00:16:19**  shouldn't use it yeah I mean that that leads into the next question right if entropy might be a good model for communication like an anonymizing communications even if we think that it is that is it still applicable to anonymizing Bitcoin transaction and to analyzing coin Jones I'm not sure yeah actually that's that's a good point that

**00:16:51**  as I see it in in Cohen joins the the things what he's arguing is just not there because in Cohen joins really what really matters is the entropy because every information is somewhat there on the blockchain already so you can you can cannot really go wrong with the entropy on the other that that would be that that would have be my point there

**00:17:23**  too anyway yeah Adam I actually agree both with you and Max here because so far everything that you're doing for enjoying in a program way it's still relying on the entropy one way or another therefore yes everything that we have heard so far about war and its flaws you know all that in and about the paper

**00:17:54**  being against entropy means entropy being valid probably I would say were available enough reasoning coinsurance there are thousands of methods to achieve thousands of goals therefore I think we just need to understand whether the method should be applicable or probably a bit modified or actually useless or coin joint ease which we are referring to right here during this calls and I think that it

**00:18:26**  might be twit like you can be tweaked but I do not think that we should just cross the entropy out of everything that we are doing to ensure they are green I mean we have an entropy model exactly one for Cohen joins the portsmen entropy

**00:18:57**  which is maybe the Shannon entropy if you don't know what other why I think that's that's that's really not a good good way to go about that because you can get surprises if you are not weighing in the link link breaking stuff like or the knapsack paper actually worked out to degree so so yeah the entropy model we should not repeat

**00:19:28**  that's for sure but in order to use it we would have to work it out properly right yeah I actually a question here where is the difference between Ronnie entropy and Shannon entropy and Boltzmann and repeat we just talked about it last epistle then we get to the conclusion that we don't know or what we think we know is not what the author thinks he

**00:20:01**  knows so so I don't know so the thing is that in the Boltzmann paper wait I want to do it quickly because this is not about the Boltzmann paper so it's not even a paper it's a gist in the boys longest the entropy looks like Shawn on entropy so I started calling it Shannon entropy under the comments and the author said that oh it's it's not Shannon entropy and well okay the paper

**00:20:35**  called what's Mars so it must be the boys on entropy right but then oh we've said there is no Boltzmann constant here so it's not the boys when entropy and it looks like the Shannon entropy so it must be the Shannon entropy so it supposed to be the Shannon entropy but the author might know better and we don't have time to really investigate that and not even that important question so so and I'm sorry for interrupting do I understand correctly

**00:21:05**  that basically now there is no clear differentiation between those three types of entropy I could answer this really briefly which is the way to think about is that Shannon is entropy in bits and so you know bits have you know essentially it's two dimensions everything's log base two Rini entropy basically says well let's

**00:21:37**  imagine we have entropy across multiple dimensions you know up to infinite numbers of dimensions and tries to capture that all within one measurement so you can have entropy with three dimensions or four dimensions or five dimensions at least that's how I understand it but I mean for most computer science uses of the term entropy I think we're talking Shannon entropy the other entropy versions are to mine understanding which is I think

**00:22:09**  quite limited in this regard er are mostly useful and say like physics for example so I wouldn't get too hung up on it I think basically people mean including I don't know why Paul Magers ran the entropy in the beginning here but I think most people basically when they say entropy they mean Shannon entropy they don't really mean anything else hmm and we are talking about another paper that was the last last episode last session that the entropy was defined as

**00:22:40**  follows so the entropy so the the gist is called the Boyett's one distinct advancement so that would say that it is the Boltzmann entropy but the entropy is defined as followed look to and the number of possible valid combinations which looks like the Shannon entropy right it does unless there is some

**00:23:10**  circumstances for example that this like semi law operates or there is some additional condition or something like that I mean a lot of things in mathematics there are very similar to each other unless there is AK one condition that changes the whole thing and actually defines some some property something like that anyway yes this paper talked a bit about entropy to that

**00:23:41**  I don't even know what he I mean maybe all all he said is just his entropy in a way that's different kind of entropy is that he is preferring the Iranian through P right am I am I remembering right here okay I remember well yes so he prefers the rainy Anthropy for for some reasons oh all right I think maybe I mean it

**00:24:15**  might be useful to talk about some of what Paul argues so so so so what what Paul's argument turns to entropy he says well you know you have this kind of theoretical way of measuring if someone's anonymous or not but how useful is that in the real world so Paul's like argument is he says well you know he says that he actually calls it of everyone correctly that the threat model of the man right we says well you

**00:24:47**  know the man can basically do anything your network watch all all the nodes delay packets drop packets compromise compromise your the nodes in your anonymous communication network and he says you know when you look at like what mixed nets were designed to fight they were designed to fight an adversary that Paul at least at the time he wrote this feels isn't very realistic which is a global passive adversary so this is an adversary that can watch all of the

**00:25:19**  communication in a network all the inputs and the outputs and every single hop between every router in the Internet and he says well you know imagine you have this perfect mix net what you know I think actually calls out Mix Master by name which is the anonymous email remailer that's you know kind of came from the cypherpunks and he says you know it's it's great if you have a hundred people using this and those

**00:25:52**  people you know the entropy you can't distinguish them at all so you know your entropy is like whatever you know to the eight whatever you know like eight or eight or not you know something quite point eight or nine bits of entropy right so you can you said well that's great you know you have a fair amount of entropy but push comes to shove you still have a very small amount of users and then he says look at tour which tour doesn't even claim and

**00:26:25**  explicitly doesn't claim to defend against adversaries that can watch the whole network but the impulses was not very realistic that watching the whole network instead what they would do is they would attack particular routers they would watch particular routers they would you know do denial of service attacks and all sorts of other stuff and that this kind of adversary which I think he kind of at the end talks about being close to what's called the roving adversary Asst or local

**00:26:56**  adversary that's very powerful miss prey can do kind of what's called active attacks can actually modify and change packets rather than just writing them down this kind of adversaries more realistic it's it's less resource it's a Paul argues it's a huge amount of resources to copy every packet send on the Internet but it's not that many resources to copy all the packets sit through an individually suspicious router or every

**00:27:27**  packet going to like an individually suspicious hidden service or tor exit node you know whatever going to The Pirate Bay and and I think that's actually a really strong argument it's it's not necessarily false I think it's actually correct and then what he argues is that you know mixed networks that if no one's using them that is it really that anonymous while if you look at tor tor just has a kind of poor entropy isn't

**00:27:59**  very good against global passive adversaries but has a lot of users it's very diverse and because tor circuits keep switching every you know whatever ten minutes or so so your entry node and your exit node in the path through the network changes every ten minutes or whatever the the rate is that it's very hard for an adversary to realistically intercept too much of your traffic and and so polls are that's a more this kind of local active attacks

**00:28:32**  are much more realistic than these kind of global passive attacks I think that's a an interesting question which model is more realistic and for what quote-unquote the man can actually do so I'd like to know what people think about that I mean you can't but yeah but yours so you can't can you how can you even put the the Onion Routing into into an

**00:29:03**  entropy conception there is there is you can't can do anything you can't define entropy dare you you can't do anything do you agree with that so far or you think there is an anthro pissed model that properly covers the Onion Routing use case and I I think it's it's wrong to throw entropy out the window because you can say well you know the the set of

**00:29:34**  all users of tor assume that you know these packets or these circuits are switched often enough you know or at least unlink able in some regard to at least their IP address but it is tricky to think about that too really because it's not actually true to basically say tor has an easily measured an on be set instead it's it's better to say you know

**00:30:07**  tor basically relies on a large peer-to-peer network and a diversity of routers to build some sort of practical notion of anonymity and I think that that's not incorrect that being said I I I feel like Paul kind of what I would say throws the baby out with the bathwater so I think you know it's not correct to say that mixed networks can only defend against global passive

**00:30:37**  adversaries there's lots of I mean at the time and Paul wrote that that was basically true but nowadays like Lou picks and NIM we built active adversary attacks in and a lot of them issues which Paul highlights that networks are issues of usability and performance and while I think it's very very hard for mix networks to achieve the performance of Tor I do think they're getting a lot better

**00:31:09**  usability made a lot better and the entropy is still a valid metric it shouldn't be the only metric but it's if you can't really give indistinguishability between a global passive adversary then it's not clear if your system is is actually anonymous and a strong sense because where I kind of disagree with Paul's I think the NSA is effectively a global passive adversary that it is I mean you know maybe Iran

**00:31:41**  can't pull it off maybe you know France can't pull it off but I think the Americans combined at least GCHQ can because they control a lot of their insight the lots of routers actually do mass traffic analysis on a level which I think Paul thought was unrealistic yeah but but the competing Sibylla ideas came came in here that the NSA can't can't watch China's traffic and China can't

**00:32:13**  watch America's traffic and and so on right the big cities are competing with each other because they don't share the information with each other even even the man even there is no word government that is is there something missing from that logic that that they can still watch somehow each other's territory or traffic yeah I think that's that's a

**00:32:45**  good point but it's it what Paul is assuming or tor assumes is that your threat model is this kind of locally bound that for sehri so that you know your threat models the Chinese government and your for example an American and you want or Chinese dissident and you're trying to basically escape that adversary should only monitor a small portion of the network may be only the Tor entry points

**00:33:16**  inside China but once you're you know out of those of that network they can't it's unrealistic for China that to monitor the tor exit knows what you're mostly going to let's say Silicon Valley services Facebook Google whatever Wikipedia that being said I don't know I don't think that means you need to throw in two P out because it's still useful measure and it's also true that even

**00:33:46**  though maybe it's true that there's no world government that can monitor all the traffic all the time you know if I'm the US government I can still monitor a lot of entry nodes most of the entry nodes which are in Europe and in the United States and I can definitely monitor the exit notes which in the United States and therefore these kind of timing correlation attacks that Paul basically says well they're just kind of theoretically interesting but they're

**00:34:16**  not practical I think those aren't practical and I think the reason is there's even been empirical stays it's war I think Stephen Murdoch was the first person to point this out the busy says you know because most tor nodes are in Europe and most users are toward the United States and most big Internet services in the United States you actually look at tor traffic the majority of it is folks coming from the United States having the traffic shipped over to Europe going through a few relays in Europe and through the Chaos Computer Club or whatnot and then being

**00:34:47**  shipped back to America to access Google or Wikipedia or you know Amazon or whatever and that's I think it while it's unrealistic that an adversary can monitor maybe every single internet packet because you know China the US may not cooperate or rush in the u.s. may not cooperate it's probably true that the but given a sir user they might be able to monitor a large portion and that portion is large enough to reasonably approximate a

**00:35:18**  global passive adversary and so that's I think the lesson from that would be sort of something saying like oh you know tour is great if your enemy is the Chinese government it doesn't really work super well China right now but it's great if your enemies like a Chinese government or the Iranian government or even the French government or you know the Hungarian government or you know a government that doesn't have huge amounts of surveillance powers but if your enemies the United States government and you happen to be in

**00:35:50**  Europe or the US or somewhere that's you know not directly the adversarial with them you know these attacks can story thinker or not unrealistic does that make sense yes can I since since you're here and you know we have some theoretical knowledge on mix networks and and such because we reviewed some papers regarding LDC nets dining

**00:36:20**  cryptographer networks but but you have more practical knowledge on that and it's it's not completely about this paper but but since you're here I would like to ask you that you know let's let's make it let's let's make a difference there that there is tor traffic when you are accessing exit nodes and the restore traffic when you are inside the onion Network and you are accessing only onion nodes on your sites

**00:36:55**  how would you how would you say but what's the difference there is that ultimately safer or or there are just just this huge horse according to you in in the privacy of those when you are accessing onion only yeah I mean I mean one huge advantage that tor has over mixed networks is this ability to essentially do web browser and a half exit notes there's a really

**00:37:26**  clear mixed networks are not by nature generically able to access any internet service because the Internet by tcp/ip by nature is kind of works in this or stream based format and mixed nuts mix every packet individually and so that doesn't work very well for stream based networks on some level I just want I just want say I mean tour I think may even be some sort of local optima might be the best you could do for web

**00:37:56**  browsing and I think it's it you need I'm not convinced that a lot of these decentralized VPN concepts these other things I'm seeing thrown around are ever gonna be better than tour but I to P or I don't know I so it's orchid thing I'm not convinced 100% that will they're better than tour I think it's interesting they exist but and maybe they have some incentive-based advantages but they're not necessarily going to be better that being said tour onion services are definitely would

**00:38:29**  definitely be more secure because you're always inside the Tor network so you don't have these exit nodes that the NSA or the man or you know the Chinese government whoever could monitor very easily I think you know you do have hidden services you know inside it Tor network and there can be a tax on they can be attempts to D in autumn eyes with hidden services there's been a lot of research on that last few years and I I would actually like to know from you guys if people still feel hidden

**00:39:01**  services are safe I still basically think they're safe and they work really well or much safer than using a web browser to a non hidden service and in it's an advantage of Tor that they work in and mixed networks essentially every service inside of the mixed network has to be kind of a little bit like a hidden service because mixed network services don't easily interface with websites like the internet generic internet

**00:39:31**  services like tor can provide so yeah I mean I know there a lot of attacks on things like dark markets and stuff over the last year or two that seemingly have gotten worse i I don't anyone tracking those I mean does there seem to be any systemic issues with Toyota services I would definitely say they're safer than not using them but I'm not sure how they're holding out right now like in the real world I don't really hear news about people getting the anonymized

**00:40:04**  because of Tor and it might not be because tor is so secure but because there are just so many low-hanging fruits that that they can can go after like oh the statistics is 60% of all a dark net market users send the money from dark net markets to know your customer exchanges directly so I mean

**00:40:38**  why would you try to deny the Tor network you have you have such low-hanging fruits there too yeah another another point you brought up DC nuts is I mean let's just be very there's basically like three fundamental categories of anonymous communication systems on the network level there is Onion Routing systems like tor which are effectively are kinds of what operate

**00:41:10**  effectively is a kind of decentralized VPN let's say for a stream based circuit based message internet traffic there's mixed nets which basically mix messages and a lot of the critique of Paul against mixed nuts is he says well look you know that that's there's those threat models are very unrealistic and no one really uses in the real world while tour provides is very practical benefit in terms of anonymity against what he considers to be realistic

**00:41:40**  adversaries he's definitely right but DC nuts are interesting so DC nuts without any argument provide with better or not enmity then mix networks I mean they do there's this kind of no question there because everyone kind of does the computation on the same packets but then I think a lot of the critiques that Paul has against mixed networks I would say mixed network technology has evolved enough that those critiques may not be necessary anymore

**00:42:12**  we'll talk about that maybe next time but that those critiques are still very possible against these see nets because these see Nets you know have this problem where everyone has to send the messages at the same time and to all the other participants and in real world networks that that's really hard so I'd like to know what people think about DC Nets here okay I think deke read was working on one I know Sarah from the open privacy foundation is working on water people interested in DC Nets are

**00:42:43**  trying to use them the thing is at least my conclusion when we reviewed we review the DC Nets paper and we reviewed queens of plus plus which provides a DC net for Bitcoin mixing and what he said there is that when message sizes must be uniform that's this kind of that's obvious but

**00:43:15**  the other thing is they argued that and I'm not sure I understood the why but they argued that that messages must be fresh messages must be always fresh and you cannot do a DC net that works properly if the messages are not fresh and with coin shaffer they actually

**00:43:45**  start that Vedic oh no no that was decent not the Kratt sorry then I don't know about the cred but via the argument was there if the messages are not fresh then you cannot do the DC Nets which kind of means that it's it's useless for communications but for for their bit purposes was was was good that any anyone has remembers differently alright

**00:44:18**  so yeah I mean one way to think about DC nuts is that you know it's like like you said this is a very good example on paper they have they're resistant to more attacks and are more anonymous than mixed nuts and torn no questions asked but I think you know when the points Paul's making is he doesn't really talk about DC Nets and while I'm not enter pissed is that even though you had a DC net that had this I kind of theoretically wonderful entropy and worked against these theoretically

**00:44:49**  very powerful threat models the fact of the matter is because it has these kind of assumptions on fresh messages and synchronous message passing and stuff it's a really good system on paper but it's unclear if any system that you'd actually build would actually be anonymous in any real sense that was based on DC - well tor is the reverse tor on paper you know I may not have very formal definitions may not seem to be that anonymous but has been this huge

**00:45:22**  real-world success story so even though I'm working on it mixed net when the folks from like member Wimble some of them approached me they said what you know member one ball has is like interactive step in it which is obviously something that needs network level privacy and when they approached me they said well should we use a mixed net or tor I said I think you know mix them the future is fine but for what you're doing right now Jesus you've already deployed nimble Wimble this is a very dangerous attack on your transaction privacy so in the name of

**00:45:54**  God use anonymous communication networks that the largest possible anonymity set and that therefore the largest possible every user so you should use tor right now rather than wait around for the NIM mix net or try to build your own DC net or something like that and I think that's you know to be honest still the case law systems I still think it's for a lot of systems I mean or works has tons of users now and that shouldn't be thought about so from it from a Bitcoin perspective I guess what

**00:46:26**  is likes I've read lots of papers about anonymous Bitcoin transactions and new kinds of privacy hands cryptocurrency but I I think in reality like what you said most people use Bitcoin and they use mixers what are most people actually using like in the real world that provides good enough anonymity basically that's pretty much it some people use money rule most people use exchanges oh yeah because he knows and and the

**00:46:59**  exchanges they use exchanges as mixers so it's okay so it's like you explain how would you use the exchange the mixer just by translating the coin around a bunch and oh no you send it to an exchange and then you'll be draw it and that's my chicken yeah yeah just Israel to a new address that's it yes so it doesn't provide you any anonymity against the actual service provider just

**00:47:30**  for the outsiders right okay so some of us store like they're just minting new addresses basically and the exchange is meeting that transaction exactly heats it's not not rocket science but manually created with an exchange yeah and how's the real world attacks on this stuff going so I had a Anya who was working on

**00:48:04**  the looping and mimics that she she actually weirdly enough used to work for chained alysus and my understanding is that it's still very difficult for Chan alysus to break most mixers and monera I don't know what the extent I mean III still feel it seems like even these very simple techniques I wouldn't really use them or advise when to use them but they might I mean I don't are you seeing any evidence these techniques are being broken that

**00:48:35**  exchanges are watching out for this behavior pattern and or what's going on I mean what's the real world analysis no I I don't think it can be broken I mean 'men about wasabi but specifically it cannot be broken because the ones are equal so so that's it but then people start merging their coins together so that when when some people

**00:49:07**  do some really stupid things like they come with no 10,000 Bitcoin and mixing with 520 different kinds for two days and then mix all their coins together that's when they get obviously the anonymize because well you can't hide an elephant between a bunch of chiidren now it's a good question if if some people who who merge a bunch of coins together like tens or hundreds of coins if they

**00:49:41**  get D anonymized in the same way too like the very big guy and I'm not quite sure I tried a couple of times but it's it's computationally infeasible to to try to find the valid valid matchings so I'm not I think it is definitely not getting the anonymized in practice and even with people who are using it very

**00:50:13**  incorrectly they don't get D anonymized because it's computationally expensive and they are not trying to find solutions they are not trying to do anonymize at all because of the same thing that i just said that most people are sending money from darkened markets to exchanges and and there is just so many low-hanging fruits that they they aren't even trying it seems so what they

**00:50:43**  settled weed is that they start to flag transactions as suspicious if they get mixed regardless if it's even a change change address that's obviously that's not even trying to be unknown anonymize but like you know it's just a change address but if it's coming out of the mix then they just flag it as suspicious and consider it as as the same as as all other other

**00:51:17**  coins those actually gain some anonymity by mixing so it's it's interesting I don't know when they will actually start looking into it but it doesn't seem to be the case for now well anyway let's let's be ahead of them instead of behind oh ok so oh my god we are really getting out of this paper I just want to ask you

**00:51:48**  this so and you might be interested in this question of mine too because you know in wasabi we ship it with tour with the tour Damon and we are communicating with the back-end server through the tour Damon of course our back-end is running over onion anyway the thing is that in Cohen joins many people come together and then the round phases have some timeouts and actually all the

**00:52:20**  Bitcoin privacy research projects have demonstrated that oh we can do our rounds in 12 seconds and things like that and in practice at least in wasabi or or or anywhere it's always the slowest peer that that that blocks the round and we started to log how how how much someone is delayed and

**00:52:55**  it seems like our time outs has to be around 12 around 1 minute 20 seconds or or 2 minutes or yeah maybe 2 minutes so the slowest peer that responds it takes in two minutes so my question would be what is there any faster

**00:53:25**  anonymity network that we could utilize instead of Tor that is like consistently fast for everyone and the slowest peer doesn't block the whole around I mean a little bit so are you saying that that the Tor network you think is slowing stuff down enough that that's causing more than a minute delay it's very fast usually so yeah 50 people in around or

**00:53:59**  let's say 190 people responds within 10 seconds so who cares but the remaining 10 is just very very slow and they are broking they're round so the rounds cannot progress as fast as we would hope to and and and do you think those are tor people being blocked by tour or just that's like an hypothesis that's or might be part of it the blocking no I believe it's it's people from some

**00:54:30**  strange countries or or just the route is going through some strange guy yeah that might be the case so it's actually there's this is great website about tour called metrics tor project org and that lets you sort of see the the kind of average Layton sees and tor in terms of you know at least retrieving what different files and different

**00:55:01**  servers and it basically says you know currently you're not really seeing anything above more than a second a few seconds delay it looks like one second delay round trip so my suspicion would be too small the problem is that that's exactly what you said that that if there's the problem at or if you are you forcing everyone to use tor in your network yes ok so the issue there is that is exactly

**00:55:35**  what you said that someone because the majority of tor entry/exit nodes are not evenly geographically dispersed so if I'm in a weird country all the time and I don't know oh I'm just gonna make one I'm just gonna guess let's say I'm in Western Samoa the nearest tor entry node maybe there might not even be an entry node in Western Samoa it might have to go all the way to Hawaii and then you

**00:56:06**  know balance to Japan and then bounce to Europe and then bounce back to the US and then to the mystic the the sabi mix and it seems to me and this this has been our practical experience mixed networks in them is that the giant slowdowns almost always come from from certain geographical places running running nodes which have just a huge latency problem and that problem actually nothing to do with tor it just us do the asserted hop the Tor circuit

**00:56:39**  or more likely the end user themselves is in a jurisdiction or location which doesn't have great tour access so the way we attack that problem in the nib mix that is we say well you know if you're not satisfying a certain kind of quality of service we kick you out but then you know that the Tor network is a volunteer run Network so it's it's harder to some extent to remove poor

**00:57:09**  performing relays real it toward note relays that built to have circuits which may not be working very well so I think it's a trade-off Michelle we mean that the thing with tor circuits is one way you maybe solve this problem I forget how long it takes to build a new tourist circuit but it's you know it's on the order of a few seconds but if you're if you're if you only need timing delays of a minute if someone slow and also helps

**00:57:41**  in terms of privacy you should probably force everyone to rebuild their tour circuit at every round and so everyone's going to slow down what appears to be initial slowdown to rebuild their Tour circuit but they would have better privacy because then the tour circuits between rounds would be much harder to connect and then maybe you could do some sort of test where you test people's latency very quickly somehow I have to think about how to do that you know just send the bike backs in the bike Ford

**00:58:13**  before letting them do the coin joint so you could detect people who are in these as you put it these kind of strange locations which have huge slow doubts or happen to have tor circuits that go through these strange locations it's a good idea oh yeah by the way we are changing tor streams extremely frequently like if you have five outputs to register then you are going to change

**00:58:45**  tor streams very quickly and what I realized from my unit test that you can ask tor to change its stream and it's going to change 90% of the times but for 10% you just going best effort and just put it put you to the exact same stream where you were before but anyway it's just yeah it's not trying to be a jerk I

**00:59:15**  think that's actually my understanding because I've noticed that as well is that tor is doing a lot of the trying to avoid these slow circuits so they're doing a lot of bandwidth balancing and it happens to be in toward there's a few tor nodes which have a lot of capacity so you know if it's too expensive the ability circuit or the trying to optimize your there's a certain frequent number of circuits you're going to just keep using those

**00:59:45**  again and again because they work well which is kind of backwards but I think that's why I would bet that's why that's happening mm-hmm anyway guys let's get back to the paper how about that and oh it's already an hour into this conversation oh my god time is flying yes so do you guys have anything what what did you take away from this paper or just just some

**01:00:17**  interesting things like like anonymity is all one area of security that is much younger for example than confidentiality or or any quotes like this from the paper that's a long silence there so let's see I just wanted to point out the thing

**01:00:51**  that Harry mentioned previously about you know how tall works and all that I just think that I'm not sure what's a good way to quantify the anonymity of Tor or even like precisely for Bitcoin but I just think the main point would be to have enough honest or not malicious tor exit nodes and also for people to

**01:01:21**  like on and off ramps in Bitcoin also without kyc I mean that's what I think the biggest threat for this like the man attack for just you know looking at that Network I mean they can do the forcing and all the other stuff like locally if needed for true ISPs or to wallet services service providers or something

**01:01:51**  like that if people ain't using their own node but yeah I just think that's a pretty interesting idea it concerns our previous conversation and it might settle something given the fundamental differences in mechanisms they did they

**01:02:25**  employ the adversaries they are intended to resist and their basic designs not to mention typical applications it might seem impossible or at least astonishing that anyone who works in this area would ever confuse the two yet for years it has been common for publications by even top researchers in anonymity communication to refer to point routing networks as mix nets or vice

**01:02:57**  versa even with designers of on your routing systems have been exceptionally guilty of failing into this idiom so yeah he evens differentiate on your routing and mixed nuts completely yeah I mean I think the best quote that I found the paper i which i think is this Paul strongest point is he says well you know

**01:03:31**  you know mixed nut should be you so this is on page at least 13 from the Free Haven PDF mix that an entropy can be used for applications where as possible to manage and to measure sets of distinct users and on enemy providers and the probability distributions on their behaviors with voting being a clear example but for general internet use they are overkill against almost every adversary except unrealistic ones which is where me and Paul disagree like the

**01:04:03**  global passive adversaries or incredibly strong ones like quote unquote demand and because of usability incentive limitations and practice they do not scale them ups protect against the man anyways on the other hand a widely distributed network like tor may already offer better although still inadequate protection so that's yeah that's an argument as argument is we really need to worry it's and this is an argument

**01:04:34**  which i think bitcoin is actually ahead was ahead of anonymous communication research and and and also the the general field of white consensus algorithms because since algorithms are always concerned about you know what percentage of nodes have to be compromised to destroy consensus or to you know destroy the system in general and that's typically you know people in security and to some extent anonymous communication research tend to think kind of more an all-or-nothing and actually it's kind of these local

**01:05:06**  attacks where you say assume the enemy's compromised some large section network but not the whole network those are I think realistic and and and you know that the the cryptocurrency community has a lot to teach the anonymous communications community here it's and I I don't know Paul's even looking at an honest cryptocurrency but I think some of the same insights about kind of real-world anonymity versus on paper on enemy is definitely applies to both crypto in the Tor interesting thoughts I

**01:05:39**  I'm more on the side of rather the critic community should be looking into anonymous communications more because I don't think we know enough yeah I mean it does agree there I I'm a bit shocked that there hasn't been more people looking into it I remember a long time ago I think there was some rumor that chain alysus was running lots of the kind of full knows seed nodes yes 10% is

**01:06:14**  that is that definitely true or I mean it's a bit of rumor for a long time but I had trouble figuring it out that was definitely true there was a whistleblower but he said it was around 2014-15 but he also said that now it's like they can't they don't run run almost they don't run much yeah I mean I would think that that's a pretty

**01:06:44**  big risk if they could run enough of nodes but good to know the transaction broadcasting stuff is pretty hard to figure out yeah I mean not specifically just that but for example if they have a lot of notes they have a lot of information about the network itself and a lot of people use kyc I don't think it mattered mattered that's not that much

**01:07:16**  if there are this like let's say 10 or 20% if of people that are not using these kyc exchanges and using mixing services I mean they are pretty easy to narrow down anyway I mean that the biggest threat is if they get big mass to surveil I don't know it's just my intuition so it was a huge problem because blue filtering wallets we're the ones who but everyone was pushing and and it turned out to be a

**01:07:49**  huge privacy risk if there is a huge adversary who is trying to collect a bunch of bloom filters now but what might be the largest risk the transaction broadcasting for that they might try to identify where the transactions coming from but what the electrons are Airport right that that [Music] electrum servers know everything about electrum users and electron users are

**01:08:21**  there are a lot so that's that could be this could be the largest yeah yeah that exactly has been one of my like things that I've been worried about also the amount of electron nodes just run from by these blocking in block chain analysis companies what what's better

**01:08:53**  centralized back-end servers or electrum servers those are decentralized but you know we said we had a windy boat but you know we just it would be even better if we could just somehow like I don't know evolve into even a a better conclusion or solution I mean just think about

**01:09:24**  something outside of box oh yeah anyway thank you guys this was a really interesting conversation and Oh anyone would like to talk about anything before before I I say goodbye I'm good

**01:09:57**  thanks yeah this was thanks thanks for inviting me I'll Ford out the loop picks paper and the NIM link after the meeting and yeah I think it should be good follow-up to how the mix of that community responded I think though all these critiques which I think are at the time their original these were very correct from Paul and this why I'm not an interface paper so this paper is actually I think hugely important and I

**01:10:28**  I'm really glad you brought it up because it it does really distinguish between again you know why certain real-world systems have really good anonymity properties and how certain systems we've seen that would be they would be better might not but at the same point what I want to try to say is that you know that doesn't mean you should just throw all the metrics now that means you should try to make the metrics more realistic and it improve the system that you currently have so it

**01:10:59**  the because the thing about threat models particularly things like the global passive adversary this person that's watching all the peer-to-peer broadcasts or watching the Internet traffic even you know even if you said hey the NSA's watching our traffic even you said that right before snowed in 2012 people would think you're a bit crazy but then it ends up actually harddrive space is cheap analysis is quite good and you have something which is very much more powerful than what

**01:11:32**  people thought that there were very few attacks on cryptography but there was because it was easy to do because hard drive space is cheap we do know the NSA was capable of doing mass metadata and traffic analysis and I would assume that the same case for cryptocurrency even though we might not have as much evidence and so we shouldn't even though even the threat model seems unrealistic we really should think what is likely realistic given just what is actually cheap it's gonna be very hard to break a

**01:12:04**  digital signature or to you know anything like that but it might be easy to just block a transaction or go after seeding a node or you know go after a central server and these are the things that enemies are going to do so that's wonderful ending there and and hurry left I think it's internet connection anyway I'm stopping the recording thank you

**01:12:37**  guys and woman have a good good day good night thanks guys but thank you bye bye guys thank you

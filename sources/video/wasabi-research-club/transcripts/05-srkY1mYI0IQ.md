# Wasabi Research Club #5 - CoinShuffle++ with Tim Ruffing (Part 1)

- Playlist index: 5
- YouTube ID: `srkY1mYI0IQ`
- Video: <https://www.youtube.com/watch?v=srkY1mYI0IQ>
- Duration: 1:28:59
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  now excellent okay so let's go through it coin shuffle plus plus peer-to-peer mixing and on linkable Bitcoin transactions this is the paper we're talking about it's unclear the authors are going to be able to join us if not they'll join us next week hopefully yes two weeks ago we talked about coin shuffle which was the predecessor to

**00:00:30**  coin shuffle plus plus coin shuffle dealt with the issue removing the coordinator doing fully decentralized coin joints but the way that coin shuffle did it was they would shuffle addresses by onion encrypting them and essentially mixing the addresses as the addresses as the encrypted addresses passed across all the peers as they passed across peer they've been decrypted and then further

**00:01:00**  shuffled and we talked about why this is a is a poor design choice because on a scale very well and so as an example we looked at electron cache which had only five participants in total doing coin joint so here's where we are in the wasabi research Club next week will likely do coin shuffle plus plus again with the authors so I just wanted to quickly run through the DC network so

**00:01:34**  the DC network was a problem posed by Tom in 1988 and the idea is that three cryptographers are sitting at a table and they want to anonymously convey whether or not they paid the bill so one thing we notice about the dining cryptographers protocol is that it allows for anonymous communication among honest peers and only honest peers will see why in a second and it's completely resistant to traffic analysis which is in contrast to something like the Tor network so one more time

**00:02:06**  three cryptographers sitting at a table they need to communicate whether or not they paid for so if they didn't pay for dinner you can think of this as a zero and if they did you can think of this as a one and at the end of this protocol we want to essentially know whether someone in this in this table paid for dinner or a dog or not so here's how a child proposed to do this protocol anonymously every single user is going to look to their right and create a hidden secret just a

**00:02:37**  simple zero or one will suffice and we'll do this for all participants until there are three shared secrets each secret is only known by two participants and what everyone is going to do is they're going to XOR their secrets XOR is just simply asking is the secret on your left different from the secret on your right if it is that's a one if it's not that's a zero and so every single participant XOR is their their value as you can see here and they

**00:03:08**  speak out loud the value to the remaining participants so you can see here that the orange participant has a one as a shared secret on both sides so he's his message is zero the Green has a one on one side and the zero so his message is one and so forth and there's only one additional thing we need to do for this protocol to work which is if you in fact are the person that wants to convey that you paid for dinner therefore someone made for dinner

**00:03:39**  you just XOR the value one with whatever you have which is a fancy way of saying whatever value you have you negate that value you flip the bit so in this case what we'll do oh and so in this case if no one paid for dinner then they'll simply say the values they have the sum of those values will always be even and all participants know because the sum of the value is even that no one at the table paid so likely an NSA member paid but if you are

**00:04:11**  the payer in this case we'll look at orange orange did for the bill or just gonna flip a bit originally orange was supposed to declare a zero but now orange is declaring a one and so the sum is an odd number if the sum is odd then it means that it was one of the individuals at the table that was in fact the payer and that's good and we know as well at this that this works because if you look from the perspective of yellow who did not pay the bill yellow doesn't know you

**00:04:44**  know yellow does not know the secret the shared secret between green and orange and so yellow doesn't know whether it was green or whether it was orange that in fact paid the bill given the honest given the public messages and so all yellow knows that the sum is 3 and that someone must have paid ok was it either of them it's unclear to know so the other question we had was why is it always even why is it that you know even if we have 800 of these people at a

**00:05:16**  dinner table and if every person only has two shared secrets with someone on their left and someone on their right why is it that the XOR is always even if we sum the XOR values across all participants and the reason is quite simple all participants either have a 0 or a 1 to their left unto their right if if they have a different value than they message 1 and if they have the same value they message 0 and because it's in a circle the value must always come back

**00:05:47**  to the original starting point so for this reason if one participant goes from a zero to a one then someone else will have to go from a one to a zero and that's why it's always even and this is the same no matter what what what kind of setup you have whether you have many many participants or just a few so there are two problems we have to discuss because those are the key reasons why we don't use these many practical applications and it's the key thing that's solved in coin shuffle

**00:06:18**  plus plus namely the number 1 is a collision of messages so the only way this protocol works is if only one person speaks at a time or nobody speaks so if for example let's suppose that green actually paid for half of the bill and orange also paid for half and so what they're doing is they both negate their bit when they speak out loud well unfortunately that doesn't work what

**00:06:48**  happens there is that the the values get negated and the entire table gets an even sum and so unfortunately yellow who is the only person not in the loop that doesn't know the secret is wrong wrongly believes that the NSA paid which is not the case so the big thing to understand here is that when you do a round of a DC net you cannot have more than one person say a message if more than one person

**00:07:21**  says a message it actually garbles up both messages so that's a pretty big problem so further we have to talk about kicking disruptors something that a malicious entity can do in this case orange is the malicious entity is simply not obey the protocol so for example reveal random messages or messages that are not X or s of what you have or possibly even the opposite of

**00:07:52**  the XOR that you have purposefully garbling all the other messages the problem in this case is that if orange does something evil like in this case here green really did pay for the meal or and did not pay but orange is is saying as though he made the problem here is that there's no way to find out who the disrupter is in an efficient way so in other words orange can disrupt definitely this this protocol from from

**00:08:22**  happening and that's pretty unfortunate so yeah so who disrupted the message it's unclear okay so yeah in this case yellow is just unaware of what's going on because yellow doesn't know whether it was green or orange they disrupted the message so now we're going to talk about boy Java plus plus so in the paper four things are discussed first the paper discusses how peer-to-peer mixing is is is really a natural generalization

**00:08:58**  of DC networks and this is because when you have a peer-to-peer mixing strategy Bitcoin we essentially have a bunch of peers that need to anonymously post an address for the mixing and then they present number two is the dice mix protocol which solves the two issues I brought up with DC Nets namely collisions and with malicious peers and what's really fascinating about this protocol is that it works in only four plus two F rounds where F is the number

**00:09:29**  of malicious peers so given no malicious peers on the entire protocol will and in just four rounds and then we have gender plus plus which applies dice mix to Bitcoin transactions to create a surprise I think yes one adult or actually appear so just a quick quick

**00:10:03**  what's going on we usually just write human yeah yeah so it we're gonna do queenship classes again the next week too it's quite difficult I think two weeks is good okay make sense oh and don't forget to mute yourself and your ship yes okay so okay so

**00:10:42**  tim ralphing is here which is pretty exciting so yeah so now we're talking about coin Channel plus plus because we covered DC networks so dice makes requires only four plus two F rounds and the presence of earth militia Spears okay so I have to come clean and say that I did not fully understand how and why this protocol works but essentially

**00:11:15**  the idea is that users are as opposed to using messages that are XOR together these DC meant messages will be power sums and so yeah oh sorry and so then by using yes then excuse me then the messages are

**00:11:49**  extracted by finding the roots of the polynomial so I laid around this myself quite a bit and I tried to replicate this and look at the code for hints but I struggled quite a bit but yeah that's where I'm at so the ideas intentional collisions with this protocol yeah and so the entire thing goes in four stages firstly a Dimi Hellman key exchange

**00:12:21**  between participants then the commitment phase where participants are committing what their message is going to be and then there's the DC net phase where the participants are using power sums over a finite field to construct their own secure message and then there's the confirmation phase which is the end of a successful mix where messages are made available and all participants have the same anonymous messages there are the

**00:12:55**  way that dice makes handles malicious peers is by having if ephemeral keys and by having participants reveal their secret key and reveal paths that allows everyone to see who in fact is the malicious peer to then exclude them in the next round so that that's that's how that's dealt with so here's an example of these communication rounds so if you look at the first run number one you have the key exchange then you have the commitment phase then then you have the

**00:13:29**  DC net and because the protocol could not arrive at the confirmation phase these secret keys are revealed and then the that the pads are revealed allowing malicious participants to be excluded and so the protocol continues over and over again until finally reaches the confirmation part of of the protocol this is probably the most

**00:14:02**  interesting thing about this protocol which is that it scales really really well with more participants so in the original coin shuffle protocol there was a sequential bit of work where users had to shuffle decrypt and shuffle addresses and then and then pass them to the next peer in order and so because it was sequential it did not scale very well whereas this here can happen at the same time the only thing that causes it to

**00:14:33**  scale worse as time goes on is that you have a more complexity when it comes to factorization of the polynomial and that that's what's visible here in the green so yeah so 100 peers can essentially get through the protocol in just over 20 seconds which is pretty impressive so yeah by using dice mix instead of the original DC net we can achieve guaranteed finality of the message

**00:15:04**  protocol in four plus two F rounds where users honestly post or equal output fresh addresses collisions and disruptions are both effectively dealt with protocol scales efficiently and the others to claim that it's a substantial improvement to coin shuffle which required users to pass cryptic messages sequentially so yeah that's pretty much it I wasn't a hundred percent sure about the some parts but hopefully we can ask

**00:15:37**  questions now okay I want to start with meet something of a segue that it's a exciting thing probably that Lucas when we were talking about coin shop are not going shuffle cross paths you figured out how to do it with an equal amount we do not not learned enough stock algorithm that's not in the paper can you elaborate on that and when team may

**00:16:09**  be able to reflect on that idea okay yes well the main idea was that the the paper is not such a paper and it details how an equal output contract and such can be can be built right so talking with a also of that paper he said well

**00:16:41**  there is a one of my proposals that is not in the paper is that another protocol where you only need to know the how much the rest of participants want to participate with I mean the amount so the outputs can be split stated with his cultural knapsack algorithm then the

**00:17:16**  participants are not a central server who can create this unequal output without any interaction yes so they only need to know how much the rest of participants are going to participate with so my idea was in the console protocol if if we know that we know how

**00:17:47**  much the rest are going to mix every every participant knowing that connect rate there the outputs right the rest is exactly the same I mean they can just create this onion layers of encryption with the public keys of repress the rest of participants to exactly the same I mean they just received the addresses in this case are

**00:18:22**  the output because if the address plus the demo I mean let's connect the output of course they don't know what they are outputs are they just shuffle those because otherwise in the final content and section if they don't shuffle the office you know the first outputs belong to this guy this other outputs belong to

**00:18:54**  the next one so they shuffle in same way exactly the same way so the the the last participant the one who finally decrypt the the the layer of encryption the last line your encryption is only see a lot of outputs or are unequal outputs so I

**00:19:28**  don't know if that makes sense for you yeah I'm not sure if I got the entire idea to be honest okay I mean I looked after the knapsack paper once that is really like years ago or so it would be interesting to to know what exactly is

**00:20:03**  it's required to come up with with the amounts here so you basically you you simply know what you said is that you just need to know the amount of all the others yes isn't that already something that like it appears in the coins I probably don't want to to tell each other boots right

**00:20:41**  so it's an authority just with everyone on the plebeians well okay yeah I mean if right if they're going to mix the full amount on the input yes to talking anyway okay so but actually there's a there's a second problem so the problem with using amounts and general within within

**00:21:13**  something like coin shuffle and I think here it really doesn't matter if this is smokin choco or more crunch ahh applause pluses actually and what I described now is actually in the end of those paper but it applies to normal control as well so coin shuffle basically works by by the idea that you use fresh addresses

**00:21:47**  for your mixing like you if you take a new address you input it to the to the mixing protocol and again plus plus and in the end you can basically if something goes wrong you can t anonymize this round and throw away your your new address because it I mean it has never been used right so it it's never been used to

**00:22:18**  receive money it will never be used in the future so it's okay to the end of the Masters round then then you by the end are amazing you can figure out who's malicious and kick them off and then you can restart without whiskers yes so your point is that the amount cannot be right right here so this is the this is the point like the amount is something what I call fix I think this is the term

**00:22:52**  we use in the paper also and this is yeah there's a simple attack once you want to use once you use fixed messages so like that's that's for example say we all use let's make coin shuffle for for mixing water fresh Bitcoin address but some

**00:23:23**  real I don't know document text file everybody has a text file now what you can do is you can disrupt the first round by basically disrupting the last message of all participants in the sense that you us the attacker on the network he learn you learn the output of the protocol mean cylinder the set of all

**00:23:56**  text files it all know yet which five belongs to who right because it's software via anonymous that you learned the set of all text files and what I can in but what happens is because I disrupt the last run by it's just simply locking it on the last one so it basically by blocking it on the on the network all the other guys have to restore because they think so I'm offline or something and then I I

**00:24:29**  can't lock so we can assuming and the network attacker I can block some honest use this messages on the network so in this so this means that the second round also won't won't finish because there's another guy Pierce of the awful I know and now the the remaining that this one still need to restart from scratch they kick out the

**00:25:01**  day honesty editor a plot kick them out to and now afterwards let's say the the remaining peers that are still on the protocol now managed to finish the protocol and now let's say the beginning we had five people including me so I I went offline in the first run then I got somebody in the second Frances there were three three

**00:25:32**  participants left now and they have three text files and I learned at the beginning all the five texts for it so the now I can just look at the two other two that are missing and now in the in the final output and I know one of them is mine so I know the other one was from the guy uploads not sure if this was actually a Kevin next week I can and I

**00:26:04**  can bring those slides of them here will be fantastic ensure them because anyway I have I have slides for a lot of stuff so this is a generic attack yet this works whenever I can I can basically make participants piaf loyal maybe because I'm the network attacker locking

**00:26:34**  their messages and it's actually pretty pretty annoying and in control because I mean and the pepper we if you say it's peer-to-peer but what we mean by that it's basically peer-to-peer on the if you look at the at the at the transaction that's generated white because it's in the end is basically congruent that if you want to do this efficient you want to run it over server or which we hello another board were just simply responsible for for

**00:27:07**  broadcasting messages and we don't trust it otherwise that's the idea here but the sunna CSV everybody connect to London Bharat you can maybe maybe just think of my IRC server untrusted I receive server and what we of course trust the server for is that it doesn't exclude people arbitrary from the protocol right if could say okay look this is always sim I don't want Tim to have anonymity is very exclude them always and I think that's in the normal

**00:27:38**  cone shuffle that wouldn't be a big issue because well I mean if the server doesn't like me I can yell at it and use another one but it's like in if you fix messages and the attack that I mentioned earlier comes into plate and that's pretty annoying because like if the fire if I send all my broadcasts why I had the server it's very easy for the server to block my message despite it just summer just needs to pretend that I that

**00:28:10**  I went off Loyola yeah makes perfect sense for me to I mean obviously the problem is that we have to we need to kick the but participants all right that right that's why it doesn't that's my idea will not work it's also by the way if

**00:28:43**  you I'm not sure if this is on some future agenda may be this like I guess people also right off of when you shuffle which was basically assuming like assuming they have confidential transactions where you can hide the amounts then this is basically the combination of hundred plus plus and confidential transactions and there suddenly it works with with mixing amounts beaker steady amounts are in commitments which which

**00:29:15**  you can recreate and which are read randomized opposed like if if you if you come up to the same value twice resulting at the freaking dependent that's why those messages as inputs to the mixing protocol are not fixed in that sense but okay it's just a remark and look as long as you don't have CC yes funny shuttle was or each in the agenda it was the idea was for the next week

**00:29:46**  but the next week with we will continue with yeah look at estrogen is in the agenda okay because I just a remark okay all right yes like this is very very

**00:30:22**  early stuff there are also so what would be interesting is to have something okay let let let me start off roughly so I think the the attack that I that I have mentioned is so is so generic that it applies to pretty much every anonymity system we can think of right like even if I sent at least FB our cave that's

**00:31:01**  maybe it's maybe too much at least every every system where I don't trust my my peers nitrogen so it's how it's written in the in the paper so I was I was thinking and I'm discouraged I'm working on this with both of it all again little Morgana's on chest we're looking into relaxations of this model where you maybe have a few trusted

**00:31:35**  sellers but in the sense that I don't know maybe there are 20 servers and you only need to trust one of them to be anonymous and I and maybe it's possible to avoid this taken in such a setting because it's basically the attack relies on the fact that people can stop the

**00:32:06**  protocol from from completing and it's it's may be interesting to see if we can get around this using some trusts maybe I don't know know that I say it again I think it's pretty hard for okay whatever I think whatever I just said makes only

**00:32:36**  a little bit sense because we were looking at other other settings I think if you really have coin join in minds that that won't really work because in Cointreau and in the end I can always refused to sign the culture transaction with yes if you would want to use while uShip doesn't matter because that then you can oh yeah so like even even if I

**00:33:08**  somehow use whatever servers to avoid that I simply come offline during the actual mixing and and they connect somehow continue the protocol the rest of the people can continue the protocol without me I saw home find at the end zone yeah now of course now you can say look I can okay I can do no good stuff and it's cool secret sharing with 20 servers so that's probably not what I wanted hmm

**00:33:40**  okay I have another question I have but this is the important letter people speak yet since we are doing this next week - what would you suggest how would someone go and understand coin shuffle plus plus in what what steps you would do would you first look at the pseudocode and then upwards and downwards of the paper or yeah what what

**00:34:10**  what what would be a good way to understand it because I have to admit to you I I did not fully understand but I really tried okay yeah let me think about this and I don't think look at the code I mean the pseudocode with the paper from a teacher but I think in that sense it's too detailed to really understand the protocol from that one the reason why we very well so detailed pseudocode is that

**00:34:42**  in in coin shuffle that was rather and in the original contra paper we it's the description of the protocol was pretty high level and some people try to implement it and then screwed up so that's why we it prefer to give the full - even though it's it's it's oddly beautiful in the octet of somebody really translated from the paper without having too much background and crypto doesn't screw up entirely so I think I

**00:35:19**  mean I again as I said I can I can I can't bring slides and it's try to explain it and the way I would explain it but I think if you if you understand how a DC networks which I think you looked at last week then I worked then I would approach conscience of loss plus simply as a way to to set up with the zenith and then if

**00:35:57**  you look at the at the steps as we also seen on your on your slides here well what what do we need for this unit we need a shed symmetric keys okay so in the beginning it will key exchange then we need to run the actual this is enough and here it is strict with with the

**00:36:28**  power samus is actually not too too essential for for an understanding of the least not for for high level understanding of the protocol it's simply a way to to encode messages and it's a it's a clever way because it always works independently of collisions but it doesn't give you an annuity or

**00:37:00**  anything like the entire limit is provided by by the DC nut basically so it's just a different encoding of things that we sent to oh did you see that but it doesn't happen any senses an unlimited limit is just make sure that we can get the message next we can extract the messages later without having any DC net collisions

**00:37:32**  where some people where they have got these slots for example and some people's and and the same slot and then you get a extra of the messages oh and you can get the extra message practically thank you and I think Adam is probably thinking the same thing you know I would like to see that this that I understand the protocol with like let's say a 4-bit

**00:38:02**  message and three participants yeah that I could do myself and I'm and I was really struggling to do that so maybe you can next week in the slides you can you can you can show something of that nature or or sort of walk through step by step because I wasn't entirely clear okay yeah yeah I can try to do that perfect

**00:38:34**  I personally I I until I don't cook something I don't understand and I kept a first that we we were discussing so far so I felt I have a good understanding but but what this long I I couldn't I was trying to go through the pseudocode but but you have some functions those are very cryptographic functions done and it's not just right

**00:39:08**  you have the building blocks the sign message very famously it's just normal photography but then you have some some much stranger cryptography like the diffie-hellman key exchange which which I'm not sure what the inputs end up to be so yeah that's alright that's not personal okay yeah yes it's to be honest there is a reason why I never wrote an implementation of this and they still

**00:39:40**  want to do but I never managed and I think not because it's not not possible but it's just because it's a very large project even though it's it's already simplified from from from the first one shuffle so actually I mean when when we were writing the second paper the controller closed plus people contacted the customer interest isn't doing a limitation of the other one and VA even

**00:40:11**  thought them looked like I think the new protocol is actually easier it's better in every aspect just throw away or over what you've written so far thoughtful but um of course they weren't happy with the dress take it is the reason yes the reason why bike when Shaffer got implemented they're like three or four

**00:40:41**  times I don't know but conscious philosophers oh that's an interesting question I don't know to be honest I mean the the story that I just mentioned okay I mean there it was the case that like just the new frame wasn't wasn't out yet so they could know about it more the other instances it pink just the last paper didn't get so much attention there are

**00:41:15**  also there some papers that side the first version a lot the second version which is kind of okay if you depending on how many how many citations you want to F in your paper this is perfectly appropriate but sometimes feel that should people overlook the New World I'm also maybe because we didn't like to type to reverse not super clever because it's called it doesn't have con chopper block losses a title read so if you if you would have

**00:41:48**  put that into the title then I guess just show up and people cook with one shot I don't know I'm just randomly guessing here so it's an interesting question another another reason why why many people just prefer ctrl + + yes I think this is something that only really was really cute when we worked on the plus plus version

**00:42:23**  is that actually kicking people so I'm in control in the normal control it's easy to deal with cases where people send wrong messages and a lot of a lot of to do work in the protocol is figuring out who said it wrong messages and kicked them out it's however in this

**00:42:57**  structure where you like the first peer sends to the second one and the second one sent to the third and so on in this in such a structure it's much harder to to deal with peers that appear offline like a lot of the third guy doesn't receive a message or claims that it doesn't receive a message from the that guy who's to blame but the second or the third and how do you agree on now should we kick out the third although the

**00:43:29**  second of all and I think for if you have a closer look at this what you really want on the end is again something like a like a podcast shuttle which we then in contrast of course plus F anyway because we describe it like this and then you have just the server is untrusted IRC server in the middle that has to find a decision over whether some peer sent a message or not but at

**00:43:59**  least is the same decision for everybody so we have to kind of kind of have this broadcast functionality built in and of course now you could go go back to Khan shuffle and implemented you by the same way so instead of sending the first spear to the second set of sin and I think the first year sent to the second or second to third and so on it's just everybody sends to the in the middle yes you could do this of

**00:44:32**  course but then n' kind of new vice communication right because liked it the only advantage of the of the normal coin shuffle protocol would be that it that you don't need this this broadcast in the sense because you only need to talk to the next guy but yeah as I just explained I think this is not really an advantage interestingly I misunderstood coin shuffle that the first time and I implemented the broadcast protocol I

**00:45:04**  implemented between a broadcast say nothing you know one guy talks to the next guy I think like okay I think assuming that you have to the broadcast to think that in crypto wise the first protocol this is a little bit easier because this layout encryption doesn't have yeah it's it's first encryption right there's no it's just

**00:45:38**  encryption everything yes it's a layered encryption yeah but on the other hand another thing that we figured out when we were looking at the second is a lot of complexity in in coin shuffle one is about getting the cases right in when something goes wrong then you have a lot

**00:46:12**  of additional potential additional message of said that Pierce need to send and then you have a huge basically a cases sinking on just to figure out who is to play and this is also something that is easier and control plus plus I actually don't know a fee if you roll it like that in the paper but I think we did a general insight there was that anyway the the

**00:46:46**  method of Terrance that you if you if you report around which basically means you want to be analyzed around entirely but what you do is you reveal the secret from your key exchange which basically is the only secret information you have in this round except for your Bitcoin inside a key okay you obviously should review that one but like for from the mixing itself

**00:47:21**  if you haven't secret is the only secret in the protocol this means that as soon as everybody as soon as you review your secret and what you sent is entirely deterministic and this is makes it very easy to to implement the planning procedure that should figure out who who misbehave because now what you can do is I learn your secret now so and I and I

**00:47:53**  know your message looking at the protocol so what I can do it's just replay your entire protocol messages we compute them and just compare them we drive it through what you actually sign it and if you send something else well then you miss the earth making sure students where appear so it's it's much easier to implement than having this huge case to think Lucas a Libra file

**00:48:28**  they have some things may discuss questions they have a question because when we have been studying these ideas and discussed this idea we started with con Chavo just jumping directly to Kinshasa club class we will review the DC Network right in what I see is that part of the

**00:49:02**  complexity a big part of the complexity of the octaves this protocol is about this about the communication layer how we communicate with others yes so why else sorry I don't remember that paper in details sorry probably is everything is there but why do you think that's the best mechanism instead of using something like at all for example what to simplify

**00:49:34**  the the protocol a bit you mean using do you mean using tor as the protocol or the Tor network has the built thing because we are discussing how to i mean the the difficult now for create an encryption key a shocky right how to broadcast how to gather I think

**00:50:09**  if that could be simplified by just communicating with the rest of the peers through tour for example I mean why are we using this is a good yeah so I think what you're saying makes makes perfect sense and I think of you like there's the threat of and I think there's a

**00:50:40**  reason why like the existing controlling limitations and Adam here's Adams implementation I think it's just be mentioned here actually works by leveraging tour because then suddenly the protocol becomes much easier I mean of course to organize crunching it's not

**00:51:10**  just it's just not just using tor you need more like for example blind signatures but the entire thing becomes way simpler the reason why why we wrote this paper is that we think it's interesting to have a protocol where you don't rely on tour also and mainly

**00:51:41**  because it gives you it gives you a stronger anonymity guarantees right it's worries towards optimize for a different setting so another miscommunication there's always a trade-off between yeah between multiple efficiency and security dimensions something like a DC DC that is pretty slow compared to tour but it's

**00:52:14**  it's fully anonymous like observing the network you can't you can't tell anything where isn't were they optimized for or for low latency which is very important in you if you look at websites because you don't want to wait forever but like but there are entire you have to anonymity drawback thread so if you first you trust your tour notes and of

**00:52:45**  course you don't trust them for me right this is the CPU to trust for example like if you if you are God note and your ex is not work together they have the good chance of generalizing you and the same is true for take care that just listens the network but came to end to any time in correlation and and I think

**00:53:17**  the reason why tour made the straight of this is what I said like they want low latency because it should be usable for for full of browsing but here actually I think we are in a different setting and we can actually have stroller anonymity by something like like a decedent okay I have another question and and again sorry I couldn't read very deadly paper not sure I don't remember but in this

**00:53:47**  case I mean the message is experiencing it right so it nobody can read that how is this communication the communication mechanism how is that it prevents learning the IP addresses of the participants oh it doesn't that's a

**00:54:18**  simple I'm sorry English please let me let me check if I understand correctly in going Schaffer at least given you only communicate with the next guy so in that case only one I'd be so only one one participant no salon urlp right that case is in this case is in this case the same or although it I think this this

**00:54:48**  depends on how you implemented but let me explain it in a different way maybe first so I think when when we talk about anonymity and what we actually talk about this unlink ability should it be able to link a pieces of data together and the senses they belong to the same guys and now we have running ability on

**00:55:19**  on different layers here so what what coin shuffle is or ctrl + + is supposed to give you is unlink ability between your input address in the control and your output address on the controller now what you're asking about is unlink ability between the input the tress on your control and your IP address and

**00:55:49**  that's another weather and question but it's it's a different question now because you mentioned tor tor kind of gives you some unlink ability between your IP address and and whatever data you said right so it's also in the sense it hides your tie to IP address that's why actually it in the in the paper we say if you if you care about the second

**00:56:23**  form of unlink ability of not being able to link network identifiers disappear trusts to your messages if you care about this through and probably you care right because if you care about privacy you probably care about privacy and all layers then you should actually use tor to to run run ties mix or to run on contracts which is another reason why the

**00:56:58**  implementation with the the idea of the server and in the middle and plant signatures is very sent over tor has an advantage because they use tor for two different aspects and we only need at once but like if you if you would run on Pablo's plus without for which I think was the second part of your question then it really depends on on really how you organize his network like if you if you run its SSP proposal the paper model

**00:57:31**  with the server in the middle that's only trusted for pro basically doing the broadcast right and you don't trust it for anonymity or one for let's really say in the following abilities between inputs and outputs of the mixing then it's it's just the case that everybody connects to the server right so the only guy that learns your IP addresses in the end is the server of course you don't

**00:58:02**  want to trust it but it leave this it's it's better than then sharing your Pinterest with everybody right so I think like the basic the basic guarantee of coin-shop applause pluses also is always there also if you run it without without or if you additionally I want to hide IP addresses then it's good idea to run it over to or also mother since we

**00:58:34**  are on this topic new healthy twenty second benchmark there in the paper so how would it change the store that's a good question hey I don't know I mean it certainly it's lower of course but that's in question I hope it's not too much today I mean to figure out the things we need to knead it with me to test it I mean my office

**00:59:04**  that it wouldn't be terrible because I think Ben would wise towards mostly of cash nowadays and one of the advantages of the protocol instead it has a constant number of rounds so like latency wise yeah it's it's not so fun

**00:59:36**  to have silane loops of a low latency because you only four rounds and I think that the most annoying thing about tor would be that like in the experiment at the paper we assumed that like everybody connects to this little dot this podcast server in the middle and they all have the same bandwidth to the to the middle node which is the optimal setting and

**01:00:09**  because the protocol is synchronized so for every round you need to wait for the last method from everybody and basically the portal that is the slowest here and then if you imagine like 50 peers connecting wires Worf then they probably have just already but either not only because their internet connection is as different manhoods just by random selection of for tor routers

**01:00:39**  they will have different levels and then we have to to wait for the slowest one on every of the four runs I can actually tell exactly how much is this it is the west here is going to be because in wasabi we the same issue and we some round runs were failing and we were not suspecting dosa and then we started

**01:01:09**  logging that the peers flying with the message too late and it turns out we had to elevate the timer to two minutes I still have no idea why it had to be that large why they aren't flying so late but some the slowest fears are colliding two minutes so it's it's not very encouraging no yes

**01:01:47**  if they're not chosen to lead I don't think this is fish well you don't matter because another thing that we realized it's van and they have to query the word transaction which is I don't know a kilobyte or yeah maybe a Philip I'd the they are applying slower then when they have to query the just just just some

**01:02:19**  small random data which which is interesting because it should not be the case because the issue with tourists around the communication rounds and not the amount of data so so there is that maybe it's one minute mmm I don't think half a minute but yeah sorry just the I suspect that

**01:02:49**  the problem is we are using in a new serie a new ship which means a new negotiation and all a lot of cryptography and handshake with the entry point finding hiding service directory to make that it is like a DNS for hydrant services right all that negotiation sometimes read it fast and sometimes really slow because you in fact it

**01:03:22**  first aquaria directory authority or consulate that says it's really happy the the creation of a new CEO click one of the secret is is is that where the communication is is is quite easy the the performance i need the device actually we are using new streams that's

**01:03:53**  a little bit different and those things are already theater and actually because i drug tests for it when a stream is not be a tough yet then death then what is going to just put it in an already you stream so it doesn't want to be in our performance anyway if we are we are we

**01:04:25**  are going out of the token careful do you have something not really just think about all the stuff you be sorry about oh yes yeah if one of the rounds fails all of the participants have to reveal their messages correct right so I'm just

**01:05:08**  thinking practically speaking it would mean that if we're working with like like a wallet and and it reveals its addresses those addresses can never be used again right there I think that that's the that's one of the fundamental dears that you basically you you really use a dress that you never basically used before and then if

**01:05:38**  you if you know you throw the way you will also never use it in the future okay that's pretty clear so are you familiar I mean this might be very rude but are you well familiar with it with zero link and what how wasabi is working I'm not sure I know a little bit maybe maybe maybe just explaining what you want to say and from your research if you think

**01:06:16**  that what sabe would be more secure safer or look better if it was using a coin shuffle plus plus model because right now what sabe uses you know a server that that does a blind signing of secret outlets right yes I think

**01:06:49**  ignoring all other trade offs I think such a model would be would be preferable really because it writes a stronger form of anonymity and it doesn't rely on on tour so that but as I said there are there are trade offs and it's I taste a lot that it's possible to implement control plus plus in the

**01:07:21**  meaningful way and assumingly you have such an implementation and assuming I somehow some quadrant future really need to look because some of the to it the question is really like how old its perform in practice because former arms of course is the it's the optimal case and it's kind of nice but if you have us

**01:07:54**  dropping out for whatever reason you add rounds and you have to restart and now if Adam is telling me ok like even even with it wasabi or the zero dinky we already have like time odds of two minutes yeah it's larger than I expected to be honest but I think it's it's something that that really you should look into

**01:08:27**  because I said I think like from our from a privacy point of view it's actually the stronger model also not relying on to working see the advantage that some people may not be able to use to offer for various reasons and here they they still get a meaningful anonymity currency whereas if you really rely on to you know you know you can run

**01:09:00**  away no you cannot which was my office working fiddle okay yeah I don't know

**01:09:34**  what what you mean I can't tell for sure what he was referring to but when cash shop who came out I had I had to look at the implementation and I found multiple pretty severe floss of course then it was github projects in the early days and what we'll used I think they they

**01:10:05**  fix these floors at least they they they told me and actually I will pop up them one on github yeah as far as I know now people have looked at the at the at the implementation and it seems better but I have never looked at the decree Anna I mean indicating because they're the flaws were so heavy I actually want people wrote this one on on Twitter and total eclipses problem and then revenues

**01:10:39**  people yelled at me for for doing this so what I heard is that they that they really approved for the evening seriously I've never looked did he cancel I don't know actively improved just to be sure they implemented queenship not quite requests that's right if they implemented coin shuffle this was another this was one of the

**01:11:10**  mentioned instances where it also it also looks a little little bit suspicious right because I think I mean a it was you maybe it's a little bit harder the prices plus plus version but I think if you if you before you start such a project at least that's the way I would do it I would first do a lot of research on the background and try like look at various trade-offs and and and

**01:11:42**  different approaches and I think like if you if you do that work you you should find closure for plus plus and I think this was also we might look to me a little bit like okay they didn't really spend time freaking aprox I mean I can give you an alternative violence ability I guarantee I got the

**01:12:21**  basic idea right away I can just work out everything from there by myself even if I don't win theory of the paper very carefully with Queen shuffle plus cos I was reading it very carefully but I still don't get the essence I guess also

**01:13:00**  party our responsibility because like if you let the paper go right but you have previews later freezes which guarantees some some properties of the diziness that in the original edition of protocol it's not guaranteed is that it would be

**01:13:31**  to think about it I think that's a good way to think about yeah maybe maybe one thing I can add here but no like of course there's not a danger that this email confuses you more I hope not there is actually a variation and I can put the link here okay and putting the

**01:14:06**  link here but but really thoughts and then I don't want to say don't look at it but this is really like not explained in a in an improper way so please please don't look at it if you want to understand control or anything but actually because like the the protocol is pretty pretty involved I also work on on a simpler version of it which basically raises it to 4 plus 3 F France

**01:14:37**  but it's conceptually simpler and closer to original DC note and that this is totally not not ready and pseudocode there's there's basically there's just a little bit of text and the long pseudocode I think the pseudocode is not even consistent in services we need work and progress and ask if you look at it though - don't try to understand that because like I think you won't understand that just because it's broke from the way it's written there but you

**01:15:08**  just want to find out that yeah like even even when I wanted to when I thought about implementing this I wondered how this can be simplified because it's awfully complex or something that's great thank you and so when I think like earlier I mentioned that I am looking into some some other

**01:15:43**  models that were recently and I think one of the things he also wanted to is drive this a little bit further to get this blur protocol which also to be the computation you look at first at the expense of adding so when you clarify the link you sent us I actually happen to have read this

**01:16:15**  it didn't help that much understanding I think that yeah that's what I'm saying like you think it doesn't have it all it's it's more like my personal notes than anything ready to be understood alright thank you like if y'all would look at the paper

**01:16:46**  and no one really understands it maybe we also have to make it accessible to people my idea is that I'm going to just jump right to the pseudocode and try to code it well jump right to the building books try to call the building blocks and then back to and then to the sizzle code when I hope for the best I think one of the annoying things that

**01:17:20**  always sp8 this is that I think like when I when I take time to look at this again but what always bothers me is really that you also need some some some abroad cost layer to do this and I already said this on my mind when I was trying to learn

**01:17:52**  that but but I guess I should just forget about this for a moment and really write the right to the crypto part of it and for forget about not working and then I mean because it's really like a layered thing with it's a different layer with that do you think a simple peer-to-peer network that's using just the flawed idea from the beginning like big message I think that this

**01:18:27**  so much because it's I guess through so slowly if you think like this is something similar to to to see your name comes really close right like something where people can connect Wyeth war I mean they wouldn't have to but I can and it's a kind of central point that helps

**01:18:59**  helps organizing and also he I think he has the same problem right you need to try and Pierce to mix it in the first place right I think that's a did some of the other half problems that sig Norton and although the mixing process [Music]

**01:19:40**  the sorry I was just speaking a note for my stuff so I don't you guys have anything but regarding each section so okay you said you can not say yes it's recorded here you use this morning me it's recorded hello

**01:20:10**  yes I can hear you we can hear you Alan okay it seems Adam he's got sorry I'm here for some reason I couldn't hear anything did you repeat that so yeah if

**01:20:41**  there are no further questions I think we should probably let him get back to his work so are there any other questions yes so because we said in the beginning that it's not going to be recorded it's going to be just a warm-up does anyone has any objections from publishing this I think it's going Matthew do I think we wish about policy no no even when it's published and I

**01:21:13**  really have a public commitment that the PT annex right I don't know do you guys have any topics now I just have a comment because you know a decentralized

**01:21:46**  protocol for conjoining Midcoast it's great and if you don't need to use store it's even better right the problem is that we if we use some kind of bulletin board a centralized one then probably we need to use store de veau to keep that server so it's it's a PDA anything the decentralized the peer-to-peer communication is is

**01:22:20**  required otherwise all the benefits I think go away and the advantages that people wouldn't have to close their tour circuit they could keep their tour circuit open up for the entire round yeah I think they are something right like yes so I agree

**01:22:54**  I would love to have a protocol that's fully decentralized I think no one figured that out so far yeah at least eighty advantage should be that SSA like you don't need to rely on a multiple four circuits but if you bring in the end you really want to connect or to the center so to use taught to connect to the central power and then you can really ask the question like okay is it

**01:23:25**  worth all the hassle oh there is one more thing you remember of the coin join me do you remember the Queen Cheney tuft yeah sure other point because I didn't say one of the problem each page one

**01:23:59**  point or or it's quite a general problem that how do you how do you establish connection between 140 and another without breaking that existing user workflow there might be a way at least you know Wichita fruits which the fruit the public is going to be exposed in that in the address oh yeah okay you mean you can see some from Flickr uh-huh so now

**01:24:30**  what we can do is that when you give me your Bitcoin address to pay you money then I can encrypt a message to your public key and I'm broadcast it to the network you were me you are listening to do that message and the new technique that message only you can decrypt it and then that message actually contains my mature endpoint and we actually have a

**01:25:02**  peer-to-peer communication between the two of us and the user doesn't even know that it's not a normal between transaction and then you can do p2 endpoint major avoidance even a likely transaction in the background so I think that's that's that's exciting anyway oh that's great and in fact I'm

**01:25:32**  opposed to pay or something like that could be possible too I mean the two parties can join for painting yes yes hey maybe I think one of the hard things is really like establishing in the show connections and then I think if I can figure that out clearly then can do a

**01:26:04**  lot of stuff yeah exactly and you don't even have to as far as I understand the cryptography can be reused for any other purpose because you are just thankfully them a message that can be decrypted whoever owns the public whoever owns the private key so who based on that message that you ain't lived it's a question you cannot figure out which bit why not just

**01:26:36**  you are encrypting a message is that correct so there are 1000 encryption schemes where you just from the encrypted message you don't see for which of the key it's encrypted yeah is that what's being useful yeah I mean temporal doesn't use encryption with but like the public keys are elliptic curve

**01:27:12**  keys and there are elliptic curve and coupon schemes where you can so for which public key cipher text so so that exists I think you certainly to do something because now well it depends depends on how many messages you get it right because if you if you can't easily tell from the message that it didn't for you you need to you need to try to need

**01:27:44**  to try to the craft every message just to figure out if it's good for you and this can be exactly but it's not a problem because you know when is the message coming so at that point of time you start listening to the yes me right it's actually easier and as for example and whenever they have a similar model right for you basically you have to look at every every transaction on the

**01:28:15**  blockchain and try to receive it and because you don't know if it's a transaction for you know but here you use a little bit different right because it only to you only need to listen at that point to this idea yeah Phineas later know what's interesting in your Queen shuffle paper

**01:28:46**  or if you support classes I don't know in one of the paper I think the question for the 2014 even that was talking about wait

# Wasabi Research Club #4 - Dining Cryptographers

- Playlist index: 4
- YouTube ID: `CfXJLQ8UkFA`
- Video: <https://www.youtube.com/watch?v=CfXJLQ8UkFA>
- Duration: 1:03:54
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  today we're talking about uh dining cryptographer networks sometimes it's called dc nets and the paper is called unconditional sender and recipient untraceability um so we're looking at a paper that examines dc nets from 2012 by herrerabalt but really um and i've i've sort of done this myself um we're really looking at the 1988 uh dining cryptographers problem uh by the creator of both the

**00:00:30**  problem and the solution which is david chow um you can find the links to both papers here or of course you can always find them on the github for the wasabi club um so last week just to remind ourselves what we were doing we talked about an issue with coin joint implementations um with respect to the resilient reliance on a central coordinator so removing the coordinator would require some secure method of participants declaring their anonymous addresses ideally anonymously so that other participants can't de-anonymize them in

**00:01:01**  the coin joint with coin shuffle we can replace the coordinator with a shuffling of the coins where each participant onion encrypts their address with the public keys of the latter participants they then decrypt and shuffle all encrypted addresses they ever see with their own address and then hand off all the encrypted addresses to the next participant so essentially we talked about creating this like shuffle mixnet we talked about how it scales poorly with many participants uh the more participants you have more participants

**00:01:31**  need to be included and the more participants in this link and if one participant fails to you know uh shuffle and pass on the date information then uh the entire thing fails and as a side note electron cash which is the bitcoin cash coin joint implementation of coin shuffle currently has this uh uh working with five participants so this gives you a sense about how well this type of thing scales um yeah um

**00:02:02**  so this is what we've been doing up until now for next week we will decide uh the paper at the end of this call and everything is available on our github okay so let's talk about the dining cryptographers um so what's the premise the premise is that three cryptographers are sitting down to dinner at their favorite three star restaurants uh the waiter informs them that arrangements have been made with the maitre d uh for the hotel uh for the bill to be paid anonymously one of the cryptographers might be paying for the dinner or it might have been the

**00:02:34**  nisa the three photographers respect each other's right to making an anonymous payment but they wonder if the nsa is paying they resolve their uncertainty fairly by carrying out the following protocol so just being very clear here there are three cryptographers at dinner the participants are all trustworthy these cryptographers all trust each other and they're acting in in as honestly as they can towards each other and towards the protocol the participants want to be able to tell if someone in the group paid so if someone

**00:03:06**  paid they would like to be able to reveal that but they don't want to out the payer because that person deserves the right to be able to pay anonymously so we essentially want to know this information we don't want anyone to reveal if it was them uh so let's visualize this so here we have three cryptographers at a dinner table um what we're going to do this is the solution uh the protocol that trump uh explains in his 1988 paper he says uh you know orange is going to turn to his right and he's going to put up a menu so

**00:03:37**  that green can't see and he's going to flip a coin to get a uh essentially a one or a zero shared secret between himself and uh and pink and then pink is going to open his menu and in a very covert way uh flip a coin between him him and in green and create a shared secret in this case the zero might be heads and the one might be tails for example and lastly green is going to turn to orange flip a coin and write down a

**00:04:07**  shared secret so uh these numbers are only known between the two individuals on that side of the table uh so um you know green is unaware of the number between orange and pink uh okay and so what they're going to do is each participant themselves is going to xor the value uh an exclusive or just means that if you have the same number uh you write zero so if you have one and one that's a zero zero zero that's a one

**00:04:37**  or that's a zero as well but if you have different numbers like a one and a zero or a zero and a one then you simply have the number one uh so every individual is going to take their two numbers and they're going to xor those numbers uh in their own heads so in this case we have you know orange has a one and a one that's zero uh green has a one and a zero that's a one and then pink has a one and a zero and that's that's one and

**00:05:08**  yeah yeah we can absolutely play it so we can play it right now in real time um by taking the participants in this chat and firstly we have to decide on an order so uh adam do you want to just call out the names in order and uh and get them to do a shared secret well the very first thing is that i'm going to be the waiter right because someone has to decide who is paying

**00:05:41**  right so i will send someone a message in private that he's play he's paying okay i'm the waiter i came here and i tell you guys that hey guys your your bill has been paid now you want to figure out if it's one of you or the nsa

**00:06:12**  excellent so what we'll do is we first need everyone to remember and share in secret we're going to do this in public um which is not secure but uh but just remember your shared secret so what we're going to do is we're going to start with uh igor and lucas and just i guess uh who wants to announce the numbers wait igor has to tell his secret to lucas lucas has to tell his secret to raphael you raphael has to tell his secret to

**00:06:44**  you one and you all has to tell his secret to you aviv okay so the communication the secure communication channel in this case is that don't remember other people's secret only the secret that's been told to you so igor so i'm just saying the number right zero one right okay zero all right you look as you remember that

**00:07:16**  now say your secret to rafael oh sorry zero okay raphael remember that and say your secret to you all right uh one all right people remember that and say your secret to

**00:07:55**  there is uh no don't you exclusive or your secret secret that's right so you you want to just take the secret of that you have between you

**00:08:27**  and the person to your left and the person to your right uh so igor um you only care about your secret with lucas and your secret with me because that's where we are in the circle yeah yeah i understand so whoever i sent the message that he paid he has to negate his result so let's start over igor one lucas

**00:09:02**  the xor is zero rafael and the xor was one the first one and the xor is um one all right so we have the xors

**00:09:32**  and yeah you can go so what's the accent so that that's a four which is even which means that no one paid because i didn't send the message

**00:10:05**  [Laughter] all right so i hope we learned something from this [Laughter] [Music] yeah no problem okay so uh you know what just happened is all all participants in the circle right the circle can have

**00:10:35**  as many participants as you want but the rule is you look to your left to your right and you establish a single secret and in this case we're going to take a one bit secret so we already did that took our one bit secret and then every individual has to xor that right so if it's a one zero that's a one if it's two zeros it's a zero if it's two ones it's a zero x or just means exclusive or so it means either this or that but not both um that's all that xor is another way of

**00:11:06**  thinking about xor is thinking if the numbers are different if you have a different number on your left than on your right your xor value is one if it's the same number it's zero okay so now every individual knows their own xor right they can now state their export uh in the public message right so this is step two phase two is the public message in this case green says one orange is zero uh pink says one

**00:11:37**  and what we do is we sum up all of the numbers that we get we sum them all up and in this case everyone gets the same result which is two if the if the sum is even right it means that nobody said anything so in this case because nobody said anything we know the nsa is the one that paid it wasn't one of the members sitting at the table because no one said anything right so that that is the protocol now suppose that orange did in fact pay

**00:12:09**  for the dinner well in this case orange is going to say one if you look at oranges secrets orange has a one and a one which means the xor should be a zero but orange isn't going to say as zero orange is going to negate that to say one so now all three participants are going to say what they have and they're gonna add up all the results which is one plus one plus one is three and they're gonna get the result that someone uh

**00:12:40**  uh paid someone at the table paid now you might think to yourself well wait a second um hey sorry can someone mute themselves it's it's getting a very low lucas i think that's you lucas sorry sorry it's very loud oh sorry sorry sorry oh that's nice okay

**00:13:10**  um yes uh so um so why does this work why does this work well let's take pink as an example so just pretend like you are pink and this is all you know about the network what you know is that you have a shared secret with green and you have a shared secret with orange and you know this the shared secrets and uh and then you say uh uh in public your xor which is one and your your uh your pink you didn't pay and now you're thinking to yourself

**00:13:42**  can i figure out if orange or uh green paid well suppose you think orange paid right if orange paid it means that orange has a one with with green that's their shared secret however if you think green paid it means that uh green has a zero with orange now the problem is that you don't know that information and whether orange or green paid is entirely based on whether that number

**00:14:12**  between them is a zero or a one so the the what what orange and green are saying reveals nothing about whether either of them paid or not um so all you know is the sum of the messages you heard was odd and so that means that someone paid and that's fundamentally what what wha what's going on and you don't know if it was alex or bob in this case orange or green so why is it always even this is actually an interesting question why is it always even well i want you to

**00:14:44**  imagine uh instead of a circle a line you know orange um purple green back to orange right uh the shared secrets between participants if it changes if it goes from zero to one then the participant that experiences that change in this case it's pink essentially has a value of one but if it stays the same as is the case with with green like it's a flat line above green then it's a zero

**00:15:14**  um so if you notice something interesting because it can only oscillate between zero and one and it's a circle it must always have an even number of increasing times and decreasing times so it can never have an odd number because it's a circle right so if it started at one and then it goes down and then it goes up and then it goes down then it goes back up has to end at the same place then it will always be an even number and it doesn't matter um how many so for example if all the numbers were the same like the number one then there would be

**00:15:44**  a zero uh total sum that's also even um but even if you add more participants and you have all sorts of clever ways to separate the numbers the number of downs and ups is always in total and even number in this case four it's gone down twice and up twice because it has to end in the same place so just a quick summary of the protocol phase one we have a one bit secret that must be shared between each participant and their two neighbors regardless of any participants there are

**00:16:15**  phase two is each participant must xor their two shared secrets and then broadcast the resulting one bit message and then two prime is if you are the payer or if you want to send a message simply flip the result of the xor and broadcast the resulting one bit message and then phase three is that given all of the messages that we've just heard we collect all of them and we stumb them and if the sum is even the message is zero if it's odd the message is one

**00:16:45**  okay um so i'm going to just stop for a second and just ask is unclear about at least the one bit protocol for dc net is anyone unclear any questions it is clear for me okay great so we're going to move a little bit we're going to move forward um so we can generalize

**00:17:16**  uh dc networks with this xor symbol so essentially what this is saying is that um the message for any number of bits for any k participants is uh is essentially the xor of all their participants messages which and each participant's exor is the xor of the secret on the left the secret on the right and the message they have themselves they xor all of those together and that's xor with everyone else's

**00:17:47**  the final result is the message from uh from some participant um in total um okay so now i want to show a quick example uh of how this would work with um this work more visually so i'm going to share screen

**00:18:17**  okay can everyone see this uh this setup here yes okay so on i'm gonna reenact this entire protocol with essentially a logic circuit simulator and you can see the three phases up at the top don't worry about the bottom the first is the shared secret the second is broadcast message and the third is interpret group message so starting from the left um starting from the left uh what i have

**00:18:48**  here is just a random number generator i click this little clock button and it lets me create new shared secrets so uh in this case we have a secret between a and b is uh is a one because that's that's bright green and then the secret between b and c is a zero and the secret between c and a is a is is a one now over here i'm going to have the broadcast message component right so right now neither a b

**00:19:18**  nor c none of them are saying anything but the result is that uh b and c both have uh positive messages both have a one message and if we look at the far right to interpret the group message i just have this uh last little uh logical circuit setup and you can see that no cryptographer has paid given what these uh individuals have said um so now i'm going to show you just by clicking if b changes the message in

**00:19:48**  this case looks like this then you can see that um we get an odd number of um uh of of red lights and uh the result is that uh we have a one at the far right so um a cartographer has paid um yeah and now i'm going to turn on the clock and what the clock is essentially going to do is it's going to start rounds and so each round you can see there there are new shared secrets and

**00:20:18**  therefore uh new setups between a b and c so you can see here even as many rounds happen uh the message at the end here is the same no cryptographer has paid now if i click on this message over here on behalf of c um now we can see on the right it says a cryptographer has paid uh bright green but if you if you just focus your eyes on the red dots it's not clear that c is the pair

**00:20:49**  because the lights flicker just as they did before kind of randomly this is this kind of making sense to anyone did anyone get anything out of this because i it might be a bit much um okay it's uh if if you understand these gates then you can make sense everyone learns it in university then forgets it of course but yeah

**00:21:22**  okay awesome so uh the one last thing i wanted to show before we we end this this uh powerpoint is just uh is just maybe this is uh too much but uh okay um so i have the same thing set up here um yeah i know it can feel like a lot um but uh essentially uh over here to the right is

**00:21:52**  an output it's essentially like um like a board um which lets you type letters in and over here we have five participants this time and they have us eight bit message this time not a one bit message what we're gonna do is we're gonna pick a random individual for example over here b and uh you can see that the rounds are happening very quickly and all the time if i start typing um i paid for dinner you will see it appear on the far right

**00:22:22**  over here um but uh if you just focus your eyes on the red dots then you can't tell um who paid so i can type over here i paid for dinner [Music] okay anyways uh that's pretty much it you can download logisim for free and you can copy my um you can copy my um project and uh and try for yourself okay

**00:22:53**  so let's finish this then uh can you explain what the correspondence is between the eight bit number and the text message say again the i don't understand the corresponding text that you typed and the result okay a great question you've all so the point was um the point was that uh um [Music] uh when i was typing i was typing on

**00:23:24**  behalf of one of the five participants right pretending to be one of the five participants that actually had something to say to the rest of the group um but all of the participants are constantly engaging in these rounds where they get this 8-bit secret between their their neighbors and they keep publishing messages except everyone is publishing blank messages because no one has anything to say so as i'm typing what's happening in real time is the rounds are happening many many very quickly that's why the flashing lights are flashing and the output is

**00:23:56**  what the group message is the the the the final message as xored by the entire group so is it like one bite of the message at a time exactly it's one bite at a time we get we we get a one byte uh secret anonymous group message sent to all participants because all participants engaged with one byte

**00:24:26**  of of the protocol instead of broadcasting then you just get a string of zero bytes right exactly right and if you wanted to for example broadcast the number you know 10 which is one zero one zero in binary right you would broadcast zero zero zero zero one zero one zero so it's still the case that most of the protocol is empty except for those two one bits and their respective locations and so the net result is a byte um with the

**00:24:57**  number 10. thanks that makes sense okay great so now uh we're gonna talk about the issues so um i had a lot of fun learning about dc nets and i spent a long time just i really enjoyed reading all the different papers um uh the sad news is is that no matter how cool or fun they are they're very impractical so we're gonna talk about why they're practical the first is that they demand a lot of bandwidth so for starters if you want to say a message

**00:25:28**  to uh in your group then uh if your message is for example one megabyte and there are n participants let's say 10 then it requires all of your peers to also message a one megabyte blank message that is xored to your message so the more participants there are the more needless bandwidth is being wasted right also it could be the case that you have rounds where no one has anything to say in that case you have an

**00:25:59**  empty message but it still costs uh m times n in size um there's also really really critical flaw which is that only one participant is allowed to message the group per round so there's it's actually not entirely true that only one group uh one participant is allowed to message per round the more accurate thing to say is that for any bit for any like byte or bit or whatever in the protocol only one participant can fill that bit with a message

**00:26:30**  um if you have two participants speaking at the same time uh the round actually collapses in on itself and so you start to negate the message of one person with the message of the other and so for this reason it's actually quite trivial to break a dc net so in order to break a decent net all you need to do is not be not cooperate either talk all the time or uh not properly message your xor or do any of the other potential things and then you will uh successfully uh break the um

**00:27:01**  the dc net um so yeah uh that's pretty much it i didn't want to take too much time leave it up to um yeah so by following a strict protocol of three phases per round we can establish truly anonymous communication for any of the participants so long as their shared secrets remain secret benefits we could use dc nets for quantum participants who want to anonymously broadcast their outputs to the group and the downsides is a very fragile system easily broken by relationship participants that's also quite a bit slower um yeah so i'll just leave it at uh with

**00:27:34**  one thing uh suppose wasabi wanted uh our participants to um to uh do a dc net for their own uh addresses right so suppose we have you know 10 wasabi wallet users they want to do a dc net and push their addresses one clever thing we can do to deal with the problem of two individuals interrupting each other is by having a very large round with a very large amount of data like for example one megabyte

**00:28:06**  and have uh each participant take the one megabyte um and create two one megabyte shared secrets with the adjacent participants um and by the way shared secrets are easily uh created with diffie-hellman key exchange if we're using public key cryptography and and essentially have users input their address somewhere in the one megabyte block but

**00:28:40**  such that all the participants could fit and that ideally uh no two participants would overlap each other but i think there's some definite definitely some challenges there um yeah anyways that's pretty much it i think for me thank you aviv so i couldn't get the outdoors to come here actually there is one altar and i couldn't

**00:29:10**  find his contact because it wasn't on the paper uh i i sent an email to charm too uh he did not reply so anyway uh i couldn't get out or but i would have one fun question for the author and please if you know the answer then then then say it so the paper says perfect security is often realized using some physical means such as flipping a coin behind the menu

**00:29:41**  card or more seriously personally handing over a hard drive disc containing key bits and my question is is this really often being realized in practice so are people doing that the hard drive this stuff the hard drive this is containing

**00:30:14**  for this protocol no no yes i i really don't think so i don't know the answer i don't think so however i think that the i don't remember the the paper because i i read it a long time ago but the problem i think is the how to get a long enough key because if you want to share for example um a movie uh four gigabytes

**00:30:46**  file for example then you need a four gigabyte key right so how to get that uh yes you can have a hard drive with a a long enough key but you can also derivate i mean deterministically from one not so big key to a one really really long so

**00:31:16**  in my opinion the the length of the key is not it's not really a problem in fact we are at all our derivation schemes for private and public keys in bitcoins in the bitcoin ecosystem are using key derivation functions for very small keys right so i think it's not the problem that's exactly actually this is one of my discussion topic because this uh

**00:31:48**  this gave me an idea about wasabi that yes this is what they are saying in the paper that we claim that if we initially exchange key generators rather than continually exchanging the keys itself the network only requires a linear amount of bandwidth in and yeah so so exactly what you just said it's in the paper so this is really interesting because it is similar to hd wallets right that's what

**00:32:20**  he said and it could be directly applied to wasabi too because you know in wasabi with the synchronized request we are actually uh sending keys all the time with the synchronized request right because there is the there are two two attacks there somehow uh why we needed to do that but it's actually not needed we could just use this key generation hd wallets and we could

**00:32:52**  we could we could save a lot of bandwidth uh for ourselves to i'm not uh suggesting to start working on it but uh i think that could work and that would be awesome yes i agree i didn't think about that but yes it makes sense i i would like to to share my my it's not my thought it's just

**00:33:22**  how this can be used in a small different way but i don't know if i can share my screen can i i mean okay okay let me see yes i think everything is okay okay i will share my screen porn okay

**00:33:53**  okay allow let me know if you can see my screen yes okay imagine e is igor messaging key right let's call it that this is aviv yes it has another random

**00:34:25**  i don't know this is me with another another key it's very small but they can be as long as as needed right so now someone that we don't know who uh of course we all know the igor ki the aviv ki and mikey we all know that so

**00:34:56**  if you receive a message for example someone igor aviv or me wants to send this message to you for example or or yes for example to you adam right so what we do is the encrypted message let's call it encrypted message will be the message right with xor the keys

**00:35:29**  of wheat right this is an encrypted message what you can do then is decrypt the message the scripting message will be the encrypted message right but the the order is is not important right because it's an xor yes so you have the the decrypt oh yeah wait wait

**00:36:00**  the decrypted method oh wow the cryptid message that is one two three four so you get the message that you really don't know who sent you that message right so this is something that can be used for communication the only problem we have is the ip address but if we can hide the ip address in some way

**00:36:33**  for example some operating systems allow you to to change the ip address in in in udp packages right so you really don't know i mean put a fake id for example right so you can send messages in this way and you really don't know who sent the message so this is something that basically can be used

**00:37:03**  and i don't know if this is useful doesn't make sense [Music] i think this is the the the the most important application i will stop

**00:37:34**  sharing all right so thank you anyone has anything to add to that uh one thing we haven't really discussed but i think is really relevant for the like the context of um coin joints is uh how do you establish the secure channels between the peers um it's related to that i mean it's the same passage as the the physical uh device part in the

**00:38:06**  paper um is the assumption that you use the prior utx dose to do a key agreement over those and like you authenticate the other participants um based on the coins that they registered into mix

**00:38:36**  [Music] sorry i changed my headphone and sorry okay it's uh sorry well i i understand your your problem which is how do you how do you bootstrap the system right which which this how do you in generally how do you bootstrap a peer-to-peer network but

**00:39:08**  but this paper was not uh not talking about that go ahead if i misunderstand something no that that that's exactly it like um i haven't yet read the coin shuffle plus plus paper so um i was just wondering indeed how do you bootstrap and is the the general approach uh to use the utxos going into the mix in order to authenticate the participants yes the quench of a plus plus paper is

**00:39:39**  going to be next week and if i remember well it does not talk about that it just talks about that as it is a general problem a peer-to-peer network is already given now this is what we can do on the peer-to-peer network so it doesn't uh talks about bootstrapping but yeah it's it's not an easy problem because think about bitcoin core maybe the most peer-to-peer network ever and

**00:40:11**  what do we do with bitcoin core we are connecting to some core developers at the very first start those those nodes the address of their nodes are hard coded into bitcoin core and that's how you are bootstrapping it and what did you do before uh you were you were in in satoshi's time you were going to the an irc server and that's how you bootstrap bootstrap to your bitcoin core

**00:40:43**  so based on that bitcoin core is using a centralized way to semi-centralized way to bootstrap i would say there is probably no good solution for that i mean the solutions are practical and good but there is no idea solution maybe well so in bitcoin specifically there's you know uh the criticism against uh bip 151 where you can't really authenticate

**00:41:14**  the other peers so um but i don't think it's the same because in this context uh every member specifically in the context of using these protocols for mixing coins uh since people come in with utxos if they expose the public key for that new um that's um like some sort of identity anchor um so to me it doesn't seem like an unsolvable

**00:41:45**  problem specifically in this context um because it's only a communication about a particular set of coins um also your your question is not about how do the peers find each other um not in general it is but um i mean it depends what you mean by fine but uh specifically i'm concerned about um so in the paper the the secrecy um

**00:42:16**  basically falls apart if you have an adversary that can eavesdrop uh on everything right because it can just see which one of the participants like if it sees both secrets of every participant then it can basically see whether or not their message was one or zero um so you need to have a secure channel to your um your left and right um neighbors yes that's correct and uh again that there's no nothing discussed about how to bootstrap that um

**00:42:48**  apart from you know physical drives and stuff but specifically in the context of of bitcoin mixing um i i was wondering um if uh the the utxos going into the mix can be used as uh identifiers where you can basically do uh kind of like stealth addresses uh like diffie-hellman key agreement on the public keys of those udxos in order to like establish the other participants identities

**00:43:21**  yeah possibly i guess but you know like this this protocol that we talked about is so flawed in from so many point of view that you have to fix a lot of things like the honesty problem you have to fix a lot of things and i think only after then you can think about how to how to exchange keys in a secure channel with each other

**00:43:53**  because that would that would depend on the final scheme all right i i have a bigger topic regarding the paper which was not mentioned but it was a large large part of the paper and

**00:44:24**  and when he analyzed autox against anonymity did anyone who who thinks here who understand the attacks against anonymity section pretty well who understood it okay it was probably the most difficult part of it so here is my my conclusion so

**00:44:54**  the anonymity set is n all the participants of the protocol that's an unless an auto care participates in this case the anonymity set of honest participants is n minus 1. so far it's clear n is the number of participants n minus one is the anonymity that if annotation participates

**00:45:26**  however if the attacker participates with multiple participants things become more interesting in this case the anonymity set of honest participants is the honest component of the graph graph so this is what the paper says what does this mean so for example if the attacker controls the keys of both neighbor of a participant

**00:45:58**  then the participants anonymity set against the attacker is one p had been the participants had been cbl attacked right it's it's understandable and yes and and and next however if the graph is fully connected then the attacker can only reduce the anonymity set by one now last week

**00:46:30**  we talked about queen chapel and i had the misunderstanding of coin shafter that the the graph is fully connected but you guys were like no you can uh pass messages to so you guys were talking about the circular graph and i was talking about a fully connected graph and i think this uh this is the same scenario that

**00:47:03**  that in in aviv's explanation the circular nature of quench of uh i think or yeah this is my question does this apply to coin shafter that if the participants if an autocad participates with multiple participants then the anonymity set of the honest participants is the honest component of the graph does this apply to coin shafter

**00:47:35**  that's that's my question i think coin shuffle is more secure is my intuition in that if so if only one participant is tasked with shuffling um and they decide to do it wrong yeah i'm not entirely sure

**00:48:10**  all right so wishful thinking fails us we are not gonna find answer to this question but it would be interesting anyway uh i have one last small thing that the paper says we will leave the question of why this is an unobservable anonymity system to the reader and instead obtain a basic generalization of the restaurant protocol before moving on to attacks

**00:48:41**  so why is this an unobservable anonymity system anyone because it's it uses the principle of xor like the fact that all you know about the entire system is that there must be an even number of of uh ups and downs so to speak of differences and if you get an odd number you don't know where

**00:49:12**  who it was the person that caused that problem there's no nothing is revealed and what would the unobservability mean that the messages given by the individuals um are don't give any insight in terms of whether what the individuals themselves wanted to say whether they want to say something or

**00:49:43**  nothing that's what's bad so if if we have a protocol like the tor network where you are ups you you are observing all the tor network messages that's an observable anonymity system because it relies on on the fact that the that there are honest communi there are secure communications between some peers but in this case

**00:50:14**  it doesn't matter everyone can broadcast their messages to everyone and whoever observes it cannot know anything that's the is that the point here yeah all right i'm not sure i follow but like the the way that the paper defines unobservability um i mean it's pretty pretty clearly defined it's just that

**00:50:44**  the messages are each message is completely indistinguishable from random noise uh i think also to the participants not just to uh like an adversary monitoring the the network yes exactly because the messages are essentially an xor of of two random [Music] pieces of data right two shared secrets that are random so um yeah so i'm not sure how like to compare this

**00:51:15**  to like onion routing because there's no notion of broadcast there um like each is sent just to a specific peer that is the point if you would be i mean i think that is the point if you would be able to observe all the communication between that's being broadcasted to the network actually i don't know

**00:51:51**  because you have to assume secular communication in chinese even here too so what's the difference there you're you're a good question i i mean i i don't even see how the the definition applies like i don't see how either unlinkability or unobservability as defined in the paper uh really relates to the the onion routing case where each message is intended just for a single participant

**00:52:23**  uh like it's uh if if alice is uh trying to talk to bob via carol or something then she sends to carol a single message that uh carol then forwards to bob um but that there's no like uh of course the messages are linkable by carol because alice sent them and and i mean you in linkability by uh having different messages um so like carol can link alice's messages to the message that she sent to

**00:52:54**  bob on alice's behalf um but since there's no like uh like bob doesn't see alice's message to carol he only sees carol's like message to him um i i don't see how the like how it's the the same notion the same property is is um like how you can even examine it in in the case of uh an in routing yeah you've all is is right right so here when it talks about unobservability

**00:53:25**  it says that um you know actual messages sent from the actors from from the participants are indistinguishable from random noise an unobservable system not only conceals who is communicating with whom but also hides which actor actually sent or received messages in the face of a passive global attacker so uh tor isn't like that right um you know for tor if you if you send a message it's not hidden among many other messages

**00:53:56**  you would have to do that you would have to make sure that it's unobservable but there's also nothing like you've all said it's it's a completely different system so um yeah okay that that was from me so whoever i wasn't asserting anything i just um like i didn't understand what how how you uh like no power if you if you wanna explain more um like uh it's just that i i didn't

**00:54:27**  understand what you meant not uh not that i think that you're wrong yeah because i was thinking out loud i i so my initial thinking was that the message that's being broadcasted in dining cryptographers is the is the xors so whoever absol observes that xors it doesn't matter you cannot make any conclusion out of that

**00:54:57**  but then i was saying that in tor the message that's being broadcasted is the actual communication between the many parties in tor so observing that is obviously dangerous now but you pointed out that this is not correct because even in dining cryptographers there is a private communication what's but if you are observing it then you are

**00:55:27**  the anonymizing the whole system so what i said first this is was my logic it it was incorrect but then aviv came with that i'm still not exactly sure how they define an observability this case but probably makes sense i guess

**00:56:03**  is is that clear my point was that i don't know the answer yeah thanks can can i ask uh just one question like how practical would it be say if we if we did 10 megabytes of of shared secrets between uh to each two participants in a hundred participant group

**00:56:34**  how practical would that be like suppose right when a coin joint is happening um uh we would have only one round which would have you know let's say 10 megabytes of shared secret lucas you were saying something

**00:57:07**  yes i think that that will what we were talking about uh minutes ago i mean the the length of the key it it is not important because you can generate a random key for i don't know 256 bits yes for example with a difficult key exchange and then you can use a key derivation function to

**00:57:39**  to create a key as long as you need i mean the the the length of the key that you need so it's not that you have to share all that so real concern is that we we wouldn't know and we can't stop a malicious participant from from ruining the process right yeah i was also having a question about

**00:58:09**  that what incentivizes uh people to or decent devices people to be malicious and just broadcast that wrong number in their xor round or something like that well it's the same that uh motivates any malicious actor in a cryptographic network it's it's that they have an incentive for something not to work right so in this case it would be someone who has an incentive for secure payments not to work well to be fair the paper did not talk

**00:58:41**  much about that if at all it was mostly assuming that everything everyone is honest so yeah but but again let me reiterate we are preparing for queen shuffle plus plus so hopefully now we have a lot of questions and questions for us

**00:59:11**  okay i'm very much looking forward to it yeah me too because i i liked the idea of this but i was just thinking about this problem also i i i should point out that there are no mainstream use cases for dc nets so you if you if you go around and try to find active um like applications that use dc nets you you can't find them today and very likely due to their narrow use

**00:59:42**  of applications and also the fact they have these problems well every every anonymity network come out of that right tor i2p swings what is the lightning network used what has dandelion coins of plus plus these are all based on this dc network research or this is the root of it

**01:00:18**  by the way there is a new guy on the block that is the locking net it's an invention of one of the monero monero guys yes they have a it's a mix between something like a new new new age store and i2p uh that looks interesting too they allow communication using udp too

**01:00:50**  and it's it is interesting i don't know it works let me write here is lucky net um it works i was playing with that and it works um just to have in mind yeah that's interesting another thing that came out recently is the neem

**01:01:21**  network you heard about it that uh i think even amir taki was involved with it in at one point all right what test topics you have that's it for me

**01:01:53**  then let's move on then and the next next week we are obviously going to look into coin shuffle plus plus after that we are looking into cash fusion which is the bitcoin cash guys figure something out about an equal amount and after that we agreed that we are going to look into papers those are trying to quantify

**01:02:25**  privacy and and aviv found a great research collection a bibliography of anonymity research which is freehaven.net slash on on beep and yeah there is like a bunch of research it's it's it's it's really great like a bunch of research meaning

**01:02:57**  thousands of anonymity research okay and just a question don't we want to rename the wasabi research club to dining bitcoiners [Music] it would be fun but i'm too lazy to fix all the links and stuff

**01:03:34**  all right guys then thank you for the dinner and thank you for the nfc that paid our dinner thank you thank you guys

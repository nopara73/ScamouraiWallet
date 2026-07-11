# Wasabi Research Club #7 - CashFusion with Jonald Fyookball (Part 1)

- Playlist index: 7
- YouTube ID: `7PEzEBF9_I0`
- Video: <https://www.youtube.com/watch?v=7PEzEBF9_I0>
- Duration: 1:04:51
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  go excellent all right okay okay thank you guys for joining today we're gonna be talking about cash fusion there was no subtitle so I just made it up myself so flexible arbitrary input consolidation coin joints yeah let's see here so this is the paper where we're

**00:00:33**  looking at it's it's available on github the link is right here and I will also post a pdf version in the wasabi research site as well okay there we go just a reminder where we are we've done all of these things so far the last three weeks actually the last four weeks we've been concerned with coin shuffle and coin shuffle plus plus which is a

**00:01:05**  good predecessor to cash Fusion and then next week it looks like we're gonna be doing cash Fusion again everything is available on the github so let's just remind ourselves what have we been talking about well with coin shuffle and coin shuffle plus plus the issue being addressed is the one of removing the coordinator so allowing individuals to collaborate amongst themselves in a trustless way given some bulletin board that doesn't have any sort of

**00:01:36**  computation properties to it it's just a bulletin board where people can gather together and meet up with coin shuffle there was this onion encrypting of addresses and then having them shuffled around sequentially across peers and we talked about why something like Quin shuffle might not scale scale very well to many many participants but it works well with a with a small number of participants and a good example is electron cache which has five participants we then talked about coin shell plus plus which adds to the protocol by introducing a DC net that

**00:02:09**  can handle collisions and disruptions in just four plus two F rounds given have malicious peers and sorry I made a mistake there should be malicious peers so yeah so we've been talking about these different ways of removing the coordinator and making these coin joins yeah so this week so let's start with the problem so when users coin join with cash shuffle or pretty much any protocol they get usually many coins of equal denominations back to them many clean

**00:02:39**  coins so with wasabi they would get coins of 0.1 denominations if they're using a different protocol it might be a different denomination but overall they they've they get many clean coins and so we need a way to private a private way for users to consolidate arbitrary number of coins without revealing input ownership that's pretty much what we're looking for and the protocol should not rely on a central coordinator apart from something like a bulletin board and the protocol should allow for arbitrary outputs of arbitrary amounts so a person

**00:03:11**  to be able to have many inputs and and many outputs okay so I just wanted to be very clear about the problem and then I'll have one of the authors who's with us today mahjongg all right yes sir okay great okay he will answer our questions and maybe say more about the protocol but I'll just be very clear here about about

**00:03:42**  the other problem so what you're looking at right now is tip is a typical you know corn joint type structure where three participants are getting together and they have these equal output denominations and in this case they have one Bitcoin outputs and two bitcoin outputs for example and then they have some change remaining and if they have changed remaining it means that they likely wanted to have that change further mixed in a different coin joint round so you can imagine this is the second coin joint now is built on top of the first one where all of the users

**00:04:13**  change is now being used to further mix those anonymous or the the unclean changed and honestly and this continues where people continuously take their the change of a 1-point joint and use that in a future point to mix again and if you wanted to spend that Bitcoin for example let's say you wanted to spend three Bitcoin and you're the purple individual well then you would have to pick your UT EXO's from these multiple coin joints and use them to

**00:04:43**  consolidate into a single transaction to spend the three bitcoins so the problem that we have is that if you're this mr. orange guy over here and you know I like to visualize coin joints as almost like a blockchain so just it's sequential and you know coin joins happen in order obviously because the blockchain is in order so you can imagine that when someone like this orange guy doesn't coin join he participates at a certain point in in this coin joint train or this this block chain this chain of corn joints and everyone in the world can see

**00:05:16**  that this person participated in a coin joint you know if I gave orange some money then I can watch us as orange participates in a particular coin joint and then further we can track as orange participates in other coin joints but the change by following where the change goes now orange is not going to be able to participate in all of the coin joins whether it's because or in just laptop falls asleep or because he falls asleep or because he disconnects in one of the rounds he's going to have a not necessarily a hundred percent success

**00:05:47**  rate with coin joins they might be a bit scattered and so after the there is no change remaining or the change remaining is too small to core joint further if if orange does not do any remix thing we can create a list of corn joins that orange participated in in this case it's 0 1 3 and then minus 2 and we can do that for a lot of the participants we could take yellow for example and see where yellow participates and then map

**00:06:18**  out that list of coin joints and then we could do that for other participants and then what happens is is if we observe someone who merges many many coins together we can ask where which coin joins to those coins refer to and in this case we might see someone who's merging coins that come from point 1 2 3 & n minus 1 and the output doesn't really matter so I just left it as a Big O and so the result is that if we just look at purple red and yellow we

**00:06:48**  can see clearly that only yellow has participated in the in those coin joints so it's it's it's it's more likely that yellow is the is the individual that sent the money and not red or purple so we could reduce the number of people that that it could be and that's a problem with consolidation generally in particular when users don't remix their coins so yeah and notice that it could

**00:07:18**  be the case that there are a hundred participants in a coin joint and that the coin joint is completely secure but you still need a trustless secure private method for consolidating your coins when when you exit so yeah so oh come clean and say that I read the entire paper and I think I understood most of it but I didn't come up with any sort of slides to explain much of it I'm hoping that if others have read it they'll have some good questions but that's pretty much where I'm going to

**00:07:48**  leave it off here I'll say in summary the idea of cash fusion is to allow for users to participate without a coordinator to have an arbitrary number of inputs and outputs such that many users that do want to consolidate or even do something like a like a spend or just consolidate can do that and hide amongst each other so it's sort of a complementary feature to a conjoint

**00:08:19**  protocol it's something that would add to something like a shovel so yeah I'll leave it at that and I'll let jonald jump in and say anything he wants to and get questions going Thank You Levi senior we're really busy working on the DC next year okay yeah soon god super lost in the DC Nets so I really apologize guys that I didn't have

**00:08:50**  slides but yeah I would like to ask you something it's it's stealing the program spaces that yeah in an interview with I think between spice with you that you said that originally you create the cash fusion II because you wanna the fate of consolidator cash shuffle old boobs but it kind of ended up being it's it's own

**00:09:21**  larger thing yes correct yeah so when we first developed cash shuffle the problem that we noticed in practice right away was getting a you end up with a lot of coins in your wallet and when you spend them together it kind of ruins the privacy so I'm I think it's kind of the maybe it's the same exact thing that Aviva was explaining with with the the math or the set diagrams would have really had those

**00:09:52**  symbols what he was talking about but it basically the problem in cash shuffle was that when you you know you end up with with two points one's an anonymized point and the other is like a change output that's trivially linkable back to the input amount so because of that linkage it just causes a problem when you combine the coins because there's too much information that's kind of leaked out so the idea was to let users

**00:10:25**  consolidate their coins but it's a cash fusion kind of turn into more than that as far as it's just this general purpose point joins in or you can have like any number of inputs or outputs the Guinean house may be it may be a follow-up question to this directly is that a common input of the or historical ownership of the input in a quadrant specifically can be done with a subsets and analysis of the change ID so

**00:10:56**  if LSS inputs and she gets the equal value output and a change then of course the change plus the equal value leads to the sum of all of your notes and and does a cat fusion defend against this to that if you have a change it cannot be linked back to the inputs yeah sort of the way that we did it is we kind of use this like arbitrary amounts type of approach so that there

**00:11:28**  really is no clear way to figure out you know the how the inputs line up to the outputs it's just just based on this combinatorics math as far as if there's you know a huge astronomically huge number of different partitions so it's really hard to figure out how things line up well and there could be multiple ways that it can blend up so you're not really isolate and say oh this this

**00:11:59**  change input goes with this or this change output goes with this input that sort of goes that sort all goes away when you have this you know you're looking at a transaction with the same 80 inputs and 38 outputs and I thank you I just would like to know that this is actually going to be the topic of the next next research conversation so it's but they're not going into the combinatorial he's gonna need to be

**00:12:29**  always session there that's like it's kind of interesting when we were first looking at this most of the people that were involved in testing cash flow phone stuff with the other developers we were focused on on that side of things like the chain analysis side and I started thinking about the other side of it like how do you coordinate it so when you have like in cash off we had this um I

**00:13:00**  guess you guys called it like an onion I guess you know I just felt like encrypting layers or whatever but so the problem would be if you have like multiple inputs then by the time you peel all the unlucky layers away you're left with individual buckets but all of them each bucket has inputs that obviously go together or you could have like each input be wrapped in its own onion layer but then you can't really tell like who the who's the culprit if someone doesn't

**00:13:31**  sign one of the inputs so I started thinking of look at how can we have the system or like you know have some kind of system where we'll be able to blame a participant that doesn't sign all their inputs while at the same time and hiding the information of what if what it puts are linked together and so and so what I came up with was this idea of kind of everyone's just checking everyone else so if you imagine Li 10 people 10 players if they're all in a room

**00:14:03**  together standing in a circle it's like hey here I'll give you one of mine you give me one of yours she gives me one of his and so on and and then so initially I think I can see that it's kind of like a grid where it was like player wild check player two's input or first and button in player two would check letter three is that ended up getting abandoned in favor of just like a purely random approach so everyone there's just like a random process of like every every input

**00:14:34**  and output gets assigned to someone to check in case there's like you know if the transaction doesn't work and then you got a check check them all and see see who's to blame something that I found very interesting in phase one which is the set up and waiting list is that you have different output tiers and then maybe to summarize that in please correct me if it's wrong is then a user can register for different of the tiers at the same time and each output here is the value of Satoshi is in the output of

**00:15:06**  this coin joint and as soon as one of these ultimate tears gets filled up by a sufficient number of users this is the tier valuev being chosen for the following round and all the users who have wrapped for several tears are removed from these tears that are not that are not being done yeah so um it's a good question so in in cash shuffle things are a little bit more simple or so you can we had

**00:15:39**  like a round on each order of magnitude so if you have a coin you know like a point 0.1 coin or a 0.01 Kohinoor point all one point each of those forms a tier and then infusion I guess this is kind of Mark's work he he come arranged it more from like an exponential distribution point of view where the amounts because the amounts are non standard they're all kind of within like a an exponentially random range so you

**00:16:10**  could have like a like a point one tier but it also accepts like you know a coin that would be point three or one that's point zero seven or whatever and then what with all these protocols how it works in the wallet is we freeze the coin when it's starting to go into around so when you're just waiting for a round to start I think the coin will get frozen but then yeah then the Ravel started then you'll just the you'll kind

**00:16:41**  of remove yourself from the other tiers because that coin is is being used already okay thanks and then a follow-up question would be at the in the paper it only says example also for example 10,000 Satoshi's or 20,000 satoshis but I'm a bit confused if this indicates a range select 10,000 zatoichi's plus minus 2000 or something because it does not indicate the equal amount right because there is no equal amount in cash yeah so I guess that's uh I guess that's

**00:17:17**  the amount of the output like roughly roughly speaking like you know is in it is it ten thousand satoshis doors at 100 million satoshis so you kind of want you don't want like one guy with a huge point to try to mix in with other people that are using tiny coins because then his pants will stick out so you want everyone to sort of be at least to the bumper right yeah all right thank you

**00:17:47**  so this is phase one the clients connect to the server and download the list of parameters and and and a figure out which which tire they wants to go let's go to face to down which is starting the round what's what's happening here it's in phase two the clients send no the server send a message to the clients which is which contains around public

**00:18:20**  key twenty-three unique nouns and the location of where the chord submission should be later me I have I have some questions for this so this 23 nose here what should this be yeah so this is all all this non-stop non-stop is part of of using blind signatures so one particular

**00:18:51**  challenge maybe I should just explain the background why why we're even using those blind signatures so because the interview can get there but what that with yeah the thing with like having multiple outputs it's not like an input where if you don't actually include an input it'll just fail because I um think about

**00:19:25**  this yeah it's okay if you include extra inputs it doesn't really matter but if you include extra outputs as we all know the inputs that can't be greater than can't be less than the outputs so how do you prevent someone from including an extra output and still blame them so what we did is kind of create these we call them like like a submission token we had a token to submit your your transaction component so the server provides these nice points and then the

**00:19:55**  client prepares a blind signature request using that novice point and then the server will will complete that that request and sign it and then the client will unblind it and then permit have that signature to present with the with the transaction component so it's a little bit complicated to think about but basically it's just like it's like it's like you're you're signing or the

**00:20:26**  server's signing that you're allowed to submit something and then when you submit it it knows that it's it's valid so it prevents the these are from submitting like too many inputs your outputs you have to submit exactly 23 component to your inputs and outputs or a blank does that make sense I know it's a little bit abstract but it makes sense for me at least you know and the second thing here is that there is a the there is a location where covertly

**00:21:00**  later the components has to be sub me dead but why why do you need the different location aren't you assuming that that you're using you tor streams and this is where you know what I mean like is it it's up to this point are you on the creative net or or what's going on here um so okay yeah there's covered announcements of the transaction price and also covered announcement of the signatures but there's also like a clear

**00:21:31**  that connection as far as like if the client just like loses their internet or something then we know that to just we can just disconnect that player there's a couple other things like that not everything is done over tor look it doesn't need to be it's just there's some advantages to just having just having the regular connection like and like for example in the blame phase like

**00:22:02**  if you don't send your blame in time or something we just know to keep that player so it's like from to her van like timeout attacks and stuff like that like like denial-of-service about timing out so not everything depends on the torquing action we just make sure that the the purpose the tour connection is so that the server can't group transaction opponents by their IP address and wouldn't that leads to cross referencing so for example in this round

**00:22:34**  these inputs participated and in the next round totally different inputs participated but you could cross-reference that hey there must be a link between this round and Israel because there was the same IP or-or-or is is this something like like every client that's online at the time is is is doing distinct so our not overt or or or it just you know what I mean yeah so okay I think I can't understand

**00:23:07**  what you're getting at so you're saying that if if this if there's some like 10 players and one of them drops out then we could see like which which transaction components that they were and can the server can kind of link them together yeah I think there's a there aren't there are only things like that there's a couple ways that that those kind of things can be mitigated so one is each you should really have a lot of

**00:23:39**  in TX on your wall and each time there's an infusion like a different random subset can be selected the other the other thing is just doing multiple fusions so you know the user should never depend on like a you know a single fusion for their privacy it's always it's always possible that people could end up just like consolidating all of their coins like if five or six players all happen to spend all of their outputs it would reduce the privacy for that

**00:24:09**  round so in the - because you know the fees are low now if we can we can afford to do that just just rely on multiple rounds to permit those kind of things but it's like you know it's not perfect sorry I that's not really what I meant and I cannot claim I fully understand the fact you mentioned there but what I meant is that if I participate in this round and I participate in the next one and I participate in the rounds tomorrow then

**00:24:41**  the server would know that I participated in these rounds mm-hmm okay but it wasn't really know which which come which inputs rapid four years in that round yeah yeah that's correct but yeah I guess I guess though there's a lot of things that a malicious server can do I think we we talked about down

**00:25:11**  the spec I mean theoretically the worst thing that it can do is just kind of have a custom back again where every person is kind of like getting extreme Sybil like just kind of isolated and put in with with fake play other players that are controlled by the server so I think those kind of problems only get solved at scale when there's just a lot of people participating and there could

**00:25:42**  be other things like proof of participation or whatever but yeah there's there's definitely some shenanigans that that a malicious server can do we just you know we just tried to solve them them as best we can as far as preventing the server from from trivially spying and yeah these kind of things that you're talking about are still possible to try to try to gain information over multiple rounds and hopefully no one no one malicious is running the server but you know there

**00:26:15**  can be SQL there can be multiple servers so okay thank you and not of you that you also bring up you know time altered access to knowledge service what I noticed is that throughout the paper and starting in Phase two you mentioned these time off periods after which there aren't either successful or or abandoned and they're they're all within seconds and know from experience in wasabi we only have three phases and each of them

**00:26:45**  takes several minutes and still many users do not respond to time because of for example like a broken tour or something or tortuous latency so how did you come up with these timeouts that let the specific value of them hmm yeah that's probably more of a question for mark who did the did yeah tool coding on this I'm not sure what you guys are doing it's taking minutes but I think one thing that we did to speed things up

**00:27:17**  is to like establish all the tour circuits like ahead of time and kind of get them ready and and then things get a lot faster and it probably also Mesabi there's a lot more players I'm not sure I've looked at some of the transactions there's they look they look pretty huge but usually like at least so far in our testing there's been like somewhere like six to nine players or something like that so it's not it's not too bad as far

**00:27:47**  as latency but I was surprised also a little bit as far as just how well it does work mm-hmm one more thing someone won walking in Wasabi's that we don't have a you don't have a communication where the set was the server initiated it's it's always like HTTP requests you know like you ask for something from the server and the server replies and and

**00:28:18**  this way when the server would have to initiate something then you always have to wait for the clients to actually ask for that thing so that that takes time it's it's not because it's not possibility it's big or or it's doesn't make sense to help it but it's because it was very hard to implement and I failed in it so so that that that makes it longer but yeah well we're also using like website P 256 so that's like

**00:28:49**  it makes signing way faster especially so when you have these transactions that I with lots of inputs and yeah just it just runs way faster with the libtech library I think I think the guys from a left arm first implemented that and we saw the difference that can speed calendar ported ported that back to electronic cash and you can blink sorry that like a huge transaction with we have to sign for like 50 inputs or

**00:29:21**  something like that would take like 30 seconds and then now it takes like one second or something so that helps all right thank you let's go to phase three which is player commitments it's a very interesting face all right so as far as I understand it's about this in this phase the players are sending their commitments to the transaction components to the server and

**00:29:54**  they are sending these invite chunk so it's not like they are sending these one by one in different over different or circles or anything like that they are sending this in in one chunk and what are its commitments this is a lot of components but basically it's these are ashes to a bunch of things like what but

**00:30:26**  you will need later to measure the trust lessness anything you would like to us to this face well it's not really that complicated it's basically just you know the basic idea is then you take your component which is either an input or an output and you just hash it so so the hash forms like a commitment and that way you can check later if the actual input matches the hash that you said it was now the reason you need to

**00:30:58**  salt it is because there's just not that many so you could do like a you know a brute-force lookup or whatever you call a rainbow table you just hash every input all right you know I've really put some outputs in just get all the hatches and you can reverse lookup we very easy so that's why you need to salt it and then there's this is kind of touching on some of the other phases but that someone could theoretically cheat by trying to use the same salt so to prove

**00:31:28**  the salt is unique y'all suck the salt the hash and pairing that with when you when you submit the input that basically is just as often hash in this phase okay okay very much thanks and the question is the salt is unique for every component yeah just a random 256 bit number yeah every component gets a

**00:32:01**  different salt all right thank you so let's go through these yes no I was gonna say otherwise if someone could like if when it comes to the blame phase of someone new the salt then they could kind of reverse lookup blanco you all the other stuff so they can try that salt number button everything and learn a lot about the about the linkages between the inputs so yeah that's why every everything gets its own unique salt okay so if this for other server

**00:32:36**  actually this is kind of phase 3 - right it's it's it's a response to the previous message with the right signature is that is that correct or there is something in between in phase 4 so yeah like that's just basically oh wait what do we blind here you're

**00:33:08**  blinding the knots point I believe okay yes okay so we are blinding the 23 knots point and we are getting a blind signature for that yeah yeah there's something I want to know that it's actually very good would be a very good if we would want to work with the current wasabi model that would be a very good extension to that that what

**00:33:40**  what we also realized that we don't really have to blind their outputs because right because we blinded the the output addresses and you don't really need you can just blind like like anything and and you can use that anything to to to do stuff later around the server maybe this is just that quick good comments and finally a face 5 we have the court announcements of equal set of

**00:34:10**  rules now in cash future we have you've called the component and the component could be an input component you know the component or a blank component but everyone has to submit 23 of them it doesn't matter at what ratio you have to serve me 23 of them and as I understand you are submitting everything correctly over new surf quits right so there is no

**00:34:44**  there is no no linkage between these components right what right right you can get intellect all the session about torn whether certain edge nodes are gonna be us or something but yes isn't working shouldn't no linkages yeah I think that that's more reasonable to consider both

**00:35:14**  practica then and also if they deserve to be over accidents anyway yeah yes yeah every 23 Massachusetts is another different circuit I'm sorry you say a corporate announcement of inputs and outputs and phase 5 and then phase 6 are actually sharing the components a silver see difference between announcing and

**00:35:44**  sharing the components sharing is just the server guess but has everyone's components I just sent it back everyone so then everyone gets a copy variances of the SS yeah you just get into physics and so your physics the server so the server suffers the components and it shares the components with everyone like one the components meet all the clients

**00:36:18**  but in a wait are we sharing the components yes yes so so so so yes you're assuring the components not the commitments okay so we are giving all the components to everyone that's suffer correct right yeah so the players send the components the server and in Phase

**00:36:49**  six the server sends all the components back to everyone and then in face seven we signed them mm-hmm yes that phase also uses toward this we just call Coburn s so we cover Lee now stay on the center's then then the server has all the senators and it can put the whole transaction together which is basically the face thank you so that was fees eat executing

**00:37:25**  the transaction yes so from here on things are kind of falling into place the X of the accept blaming phase which you so everyone has everything but I got to go into the blaming phase I would rather just ask questions there because that's D because at the beginning I

**00:37:57**  thought that it's a really interesting approach and quite honestly that gives me a headache that that the people have to share we share things with each other with Rondon peers it gives me a headache from an implementation point of view that we don't right now and I'd never done that but but anyway the the problem

**00:38:29**  I thought there is first is that of them the random players actually learn stuff but then as I was reading forward and they don't really learn stuff because there's some interesting attraction between the server and players that this is not even the players learn is that correct interpretation doing this yeah yeah yeah because when the players are

**00:39:00**  verifying it during the blame phases they're just verifying one component at a time and and the no one knows don't even have the list except the server of the link now the commitments so the server knows that and here's Alice's 10 - terminus but the other players don't know that so they're just looking at one component at a time they all can't verify these eight components but they

**00:39:34**  don't know which players maybe it corresponds to maybe three of them are from one guy and two of them are from another maybe they're all from different people no one really knows and so by keeping that list only on the server it it prevents the players to learning anything and then the server itself doesn't work is it's not participating and doing those doing those checks the only time the server Lauren's is when someone gets blamed

**00:40:07**  then it circuit reveals like they can do this is Alice's transaction that got blamed but oh just learning what analysis inputs doesn't really tell it anything just give me any information yeah thank yes so you are leaving soon and I want to give others the chance to ask questions to not just us but before that I I want to close this sweetie meet

**00:40:37**  meet meet at court which is either from you or mark I did not check but I think it was very very instructive in in a way that that that is very practical so on the design trade-offs parties when making design choices in this situation there is trade-off between matching tiny security costs versus of the complexity and unreliability in the form of more protocol faces one must first understand

**00:41:09**  that even with a perfect fusion protocol civil attacks are possible and can be taken to the extreme if the server is malicious many of the trade-offs start around the server when judging the merits of a security trade off it is helpful to compare what the security hole allows versus the existing attacking vectors which may be we already large out of surfaces so yeah that's that I think this is a great example of

**00:41:42**  whom you come out and and actually talk about the big picture but let's with many papers just loose this one tough diamond in papers I think it's really insulting so thank you and Igor Aviv Volker Raphael please join in if you have some lots of questions I had a

**00:42:14**  question just about sort of implementation if there's any intuition that you have in terms of how long it would take for the protocol to to go through and how it scales with more participants with more inputs and more outputs if there's anything you can say about that you should go through so so let's suppose there are ten participants with with ten coins each do you have an

**00:42:47**  estimation of how long a protocol like this would take - from the time of chairs establish connection to the time the coin join is is is broadcasted so you're so fun practice it seems like it's not taking very long maybe like less than 30 seconds and that's with maybe like seven or eight people it could take longer if there's more people

**00:43:18**  and especially if there's rounds where where players get kicked out so we do the thing this is kind of an idea from coin shuffle plus classes just kick one bad player out and just continue with one one fewer in the red the size little brown so if you had like but another like 15 people and then you had to redo it for 14 and 13 and so on it could add add time to it but I think it's like it's still gonna be like on the order of like a minute 2 to 2 or 3 minutes or

**00:43:51**  something maybe faster and so does this scale linearly do you think or oh it's really good question I think I know I have to think about it seems like it would scale hmm maybe I have to scale better than here because there's there's like it's kind of happening in parallel like everyone's kind of signing it on their own I like the client sided so if you had more clients it's not necessarily going

**00:44:23**  to take longer yeah but I don't think about a little bit more so because things are paralyzed unlike cash shuffle if I'm not mistaken which is sequential then there's no issue there but with more participants it's more likely that one of the participants will by accident go offline yeah so and you're saying that it's it would probably be linear in terms of

**00:44:54**  number of malicious peers or accidentally malicious peers yeah you bring up an interesting point like with so one point I was considering the idea of like we could just use layer encryption instead of using tor but like you said that that doesn't scale or it takes longer than more people you have so that that's kind of like goes back to the part of the spec that then if I was

**00:45:25**  reading about as far as the trade offs like you can you could have it maybe better than tour but if it's gonna if you have to wait until 500 inputs and outputs get decrypted based on like an onion scheme then that's gonna take a long time so yeah I don't answer your question oh yeah I'm not gonna ask more because I want the other guys to ask so now's your chance okay no question of

**00:46:03**  guys yeah go ahead because I have a lot and only five minutes left okay so just quickly I wanna thank you that you put this on eater because many of the researcher you just can't contribute and it is really bad even the alters cannot change when they make a mistake later on the day publish it and they are not able to

**00:46:36**  modify the very search so that's another Skinit contributor you cannot see the reviews so thank you for that or on the follow-up notice that I actually done a couple of typos fixes and you guys were replying on on eat robots did not match my typo fixes so but yeah thank you guys for like help me on the call being

**00:47:09**  interested in the protocol it's kinda people from different block chains can you know can be friends and collaborate now you know privacy is more important than any of the egg office and it's it's it's it's quite a shame and when to do projects go against each other just because they have different philosophy yeah and I thank you very much

**00:47:44**  so as a summary I would say it's it's very interesting protocol with a lot of ideas in it and very complex I would not go one as as it is and try to implement it because I'm afraid I would I would figure out too late things I would try at first to come up with the easier scheme that's was the same problem and if I end up not succeeding in that

**00:48:16**  then that's when I would look into this but there are some very interesting ideas like what we didn't even talk about the whole pretense of the token injure that the D server doesn't like that that's actually a very important idea that the T vanta album it was was fighting with the exact same problem and even we were fighting with the exact same problem in in Serbian our or so notion was like just waste a lot of

**00:48:46**  benefit so yeah so thank Thank You Jerrod and similar things like you could theoretically just not get the blame stuff and just kind of either hope it works or if it doesn't work you just retry the just retry with you know the holding around and eventually it will work but we wanted to try to take on the challenges of putting that you know ante TMS stuff kind of least just having a foundation to be able to do some of that

**00:49:20**  the nd that I think yeah I think there are a couple very good ideas in here and one thing that I'm still curious about is is in the worst case during the bling face who learns what about the other participants right so so and there's there's a random peer which will verify the component but he cannot link all these components together so even even the the peer verifier cannot cluster

**00:49:50**  these components and thus coins and however oh yeah if the server does not take part in this playing face so he does not get individual no server does get individual components - so the third Thursday there's a communication key with every every component so if Alice is supposed to submit it like a proof of correctness to let's say Bob she's going

**00:50:24**  to years Bob's communication key and and set then sent her information to Bob now Bob gets and so she encrypts it everyone everyone but all the players can see that there's an encrypted message from Alice which is supposedly her correct so if Bob then says that they serve her

**00:50:55**  this is not a righty he shares that private communication keen with the server the server I can see what Alice actually sent and decrypt it to see if it was correct so no one except the server knows that the key is actually Bob's per se warehouses corner quarter well they just the other players just see that there's some component being verified and it's not everyone's kind of

**00:51:28**  trusting the server not to be disruptive so if the server says that hey this didn't come up for over to kick you out you know everyone's trusting the server not to like you know like intentionally cause issues with it working okay that's very interesting yeah even if a user collaborates or colludes with the server and both are malicious because they commit to you

**00:52:00**  know the randomness upfront in the blank face they cannot really choose who will be part of a flaming whom I think the essential components to amongst peers and so this means if there's for example one malicious user at the malicious server they still only know the linkage of all random components and not enough of all from one user so I think even in this case if there's only one or like a couple issues users collaborating with the server I think it's the whole top of

**00:52:32**  privacy yeah there's like a couple more issues users as there can be there can be multiple people that end up getting their components chapped and when they send it back to the server the server can kind of try to match like oh these three were from Alice so maybe a little bit of information but then again the server can also traveler that just just by

**00:53:04**  controlling players anyway just me so nothing that nothing was really gained too much yes okay well well thank you very much for joining us here on the phones very helpful it's all scripted at the insights from the author's and just more context of the papers so thank you very much for joining and thank you goes around yeah thank you so much Donald we appreciate it well we'll talk again yesterday just a reminder next week we're doing

**00:53:36**  the combinatorics bit so a job well that will let the authors know that if they would like to join us again they can they can join us again for that okay all right so Raphael you had some things to say could you go ahead no I didn't actually I was just telling you to go ahead and ask your questions all right

**00:54:10**  okay so let me see you know since he left my crush just seems really boring at this point of time but oh you've wanted to talk about Peter about the question four plus plus mmm Alif Oh

**00:54:41**  okay this'll be e for three months okay so let me see what else do I have here Oh y-yes so tomorrow is tomorrow next week is going to be just a bit of scheduling is the is the last agreed-upon topic and from there on do you guys very and he may be agreed

**00:55:12**  upon the direction right that we are going into the organization and the unequal inputs and try to the terroristic sand and who s maybe just looking to block generally this paper and and try to get the blockchain analyzers guest on the show that would be really fun and quite unique what do you think about this yeah you know actually I think talking about heuristics would be very interesting and a good summary for that might be the

**00:55:43**  Bitcoin privacy lucky which possess or the Bitcoin we keep of the chapter on privacy which asks all heuristics very well curated and explained so that might be a good one week discussion to talk about all the heuristics mentioned in there yeah that's good anyway then the next week this week we're is going to be cooked cache fusion or not really catch fusion but crash fusion brought up this

**00:56:14**  conversation so it's going to be one one paragraph one chopped one paragraph of paragraph of cache future the combinatorics port and there is a lot of online discussion if that can work that way or cannot work that way I gather all the resources I've seen a bit kind of mailing list and and some medium articles so that will be very interesting to see if we can we can get

**00:56:45**  to the bottom of it if really hope a good knife conjoins work at what conditions so that will be next week so aviv are you back already and here so you won't have to talk about Croatia for plus plus briefly but what team did not appear so I guess you didn't force it do do you have something to discuss there yeah so what I would

**00:57:20**  really like to know and what I couldn't personally figure out was how a DC Network could could completely avoid collisions and have all participants be able to submit a message so what I really wanted to show is that three participants using this you know you know Tim's DC network could actually do this and I tried it very I tried it for

**00:57:54**  a very long time I actually replicated the the finite field using using AES because it's it's an 8-bit finite field and and I was trying to show that this could work for a small 8-bit message a single byte and I and I couldn't do it the problem that I get is that when he does this power sums and then he uses a

**00:58:26**  Newton's identities to create this polynomial I only ever get encrypted messages as the as the interest intercepts of the x-axis so as far as I'm concerned you know I'm struggling to replicate this I reached out to Tim he gave he gave a good explanation as well as code in C++ and you've all said he's happy to help

**00:58:58**  me replicate with with the with the code but I would have to understand the code well enough to understand how it works because from from where I'm sitting what Tim Ruffing the claims he made sound like magic to me because he essentially says that three people who are submitting encrypted messages three times you can do this magic on it and then it creates a polynomial where the X

**00:59:30**  intercepts are the unencrypted messages and to me this just can't believe it until I see it and I still haven't seen it yet so that's where I am if anyone is familiar with with with this problem and can help them please do but that's where I am yes I would ask Mac sex pants to you respect the authority of the chief wizard of the Quinn Tim is Right a force

**01:00:04**  now I think you are ready to do ahead of us to be ah yes I got really happy when I get the holistic understanding of Croatia but yeah yes to the month is like it's amazing yeah well because the thing is is that a collision-free DC network is very important for us as a tool even put everything else in control plus plus

**01:00:35**  aside that's a pretty cool tool and we don't know when we'll need it so at a minimum we should understand that tool well enough that that you know I should be able to tell and talk to Lucas or you and explain in a way that we all understand how to do this and currently it's still magic to me like I'm actually not even convinced it'll work but maybe it's just too too complex it's above my pay grade so to speak in terms of the

**01:01:07**  math but I'm trying hard to understand well you see just just in general there will be times when we will have to go very deep into the bottom of the things like we are already going much deeper than any other like podcasts or discussions but for example the not suck paper I would really prefer if we spent one more week on it because I was I was

**01:01:39**  writing code for 1/10 and then oh my god the third algorithm and the second algorithm was buggy and you know it's like I'm still not communist the do not suck paper actually works or what's the unit we shown there but but the show must go on the there is a new topic every week and and in the end it's more effective if we if we go on until all of

**01:02:12**  us decide to okay let's now double down on this great idea because this is this is something and I don't feel like that that kind of idea the DC Network because it's solving problems that I don't want to solve which is the the the ultimate the centralization or or at least I don't want to store at this point of time maybe ten years from now when I become

**01:02:44**  water and my peers will be longer you know you actually though what we might do for next week when we do the combinatorics of kefir could cache fusion because it's only one paragraph in cache fusion this might be worth to compare to canasa and see maybe where the differences are right then and just take this opportunity to double down on Canasta and look at it again with with fresh ice so there are there are things

**01:03:16**  so not suck that maybe I could because the next week topics is going to be naive or enjoins we spark the discussion of cash future and so estrogen is just one paragraph but there is a very long discussion on Bitcoin deaf mailing list okay not that long but people wrote small no where's there like in every yeah so that might be might be hard to understand and also

**01:03:47**  someone wrote the blog post and actually some some software to try to verify or disprove that cream and you know so that there are content there that the three can go through and not suck is definitely that idea okay I promise you I will try to to to find the interesting the the relevant paragraphs in enough suck because yes definitely not suck was

**01:04:19**  the one who who approach this problem in a more formal way and that's important so okay yeah I I feel I will get all the resources together and people we are nowhere to talk now if you want to reply to the pics two things before right yeah that's why I think it's okay to stop recording right yes

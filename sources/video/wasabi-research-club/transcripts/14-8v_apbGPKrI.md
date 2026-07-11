# Wasabi Research Club #14 - ZeroLink

- Playlist index: 14
- YouTube ID: `8v_apbGPKrI`
- Video: <https://www.youtube.com/watch?v=8v_apbGPKrI>
- Duration: 1:00:05
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:03**  hey hey all right guys welcome to another episode of the wasabi research club today we are talking about zero link the big point of fungibility framework the the paper is available on github the link is right here and it's in on it's a work in progress it's ongoing but it the the is mostly formalized in 2017 don't say that and

**00:00:36**  this is what we've been doing so far so if you recall the the last few weeks and as always we will decide on the next week's topic by the end of this wasabi research Club meeting and of course you can find out everything on via github at the link below so we'll talk about the fungibility and coin joints just go over the basics of the zero like architecture zero leak has many parts to it we're

**00:01:08**  going to focus on how the coordinator can build a a coin joint without requiring that the users trust the coordinator we'll talk briefly about attack vectors to zero link of mentions in the article and I think just one that I that I'll bring up and I'll just sort of open it up and you know we're very lucky in this in this call that we happen to have one of the authors of a paper on the call but for the life of me

**00:01:39**  I can't pronounce his name and I would hate to be rude so we'll just leave that out for now and just move forward okay so we're familiar with the privacy problem with Bitcoin transactions are public inputs point imprimis on spent outputs and then there's this whole graph that's that's leaking sort of what transactions are connected to other transactions we've talked about before the idea that if you have two users that are engaging in transactions they can join their transactions together so on

**00:02:09**  the Left we have two transactions we have those two transactions joined together just like this and we've talked in the past about why you can't just do this in a sort of simple way because what happens to this you can sort of do the math try to find the songs on the left and it songs on the right and see if you get a match so in this case you know we can try to figure out a match of 57 and 15 there's no match there and so you find another input and output until you have a perfect match and then you can quite easily take there's one

**00:02:42**  transaction break it back down into its parts so it's not very safe to just take any two transactions and combine them together we've talked about equal awkward acquaints so the idea here is that you have these two individuals they agree on some output in this case the equal output is 10 they agree that they will both create one anonymous output of 10 and when you combine these two transactions together into one well what happens is that even if you know the two

**00:03:14**  inputs are different people and you mark them as different individuals you can easily trace the change but you're left with this question what about these two outputs here you don't know where the outputs belong to because they could easily both belong to orange or yellow equally there's no there's no special hint as to whether these two outlets belong to yellow or orange so the question is how can this be coordinated without loss of privacy so if we want to

**00:03:46**  make this this is a coin joint happen we needed to be coordinated because clearly two individuals working in tandem that's some that requires coordination so how are we going to do this an option one is without a coordinator we talked at length at multiple meetings we talked about cash fusion cash shuffle coin shuffle shuffle plus plus talking about different ways to get individuals to completely in a decentralized way establish this

**00:04:17**  coordination but we the zero link paper mentions this there this is very tedious and cumbersome and hard to improve hard to upgrade and so it will be more ideal is a coordinator that we don't trust obviously option TQ is you know why don't we just use a coordinator that we do trust you know for example we could just have a single essential server everyone just sends the extended public key to that server and the server will will do the magic and we hope the server doesn't reveal

**00:04:48**  that sensitive information to any other individuals now that obviously sounds pretty stupid so we're not going to do that so what we're going to do is talk about zero link coin joints or sometimes called Tommy and blind coin joints or more technically snoring blind coins because we're using snore blind signatures in the model so zero a coin join chummy and blind or enjoin we'll

**00:05:20**  take these three users and as it turns out I have a better presentation that I did in the past which I'm going to quickly pull up to explain this in part because it's also copied from what David made so we'll just use this here we go so the the coordinator here is interacting with a zero link wallet a set of zero League wallets and the goal is to build this final enjoyed

**00:05:50**  transaction right but we also want to make sure that the wallets don't reveal to the coordinator at a minimum the the output that is anonymous because otherwise it's not really anonymous so this is broken down into phases phase one Alice will a presented coin that meets the minimum requirement for the denomination that the coin joint is doing so Alice will present the coin Alice will also present truth of the

**00:06:21**  coin this proof is a signature with the public key of where the coin is currently stored Alice will also present an output for the change because if we are talking about a equal outward join most almost all participants will have change and that change is linkable so the output is unblinded and Alice will provide a blinded output for the next coin this blinded output is essentially in a dressed in a black envelope that will be given to the coordinator just not thing that a

**00:06:53**  coordinator will sign that black envelope and the signature from the coordinator will sleep through to the paper inside the envelope and later Alice can present it so the idea here is that Alice is not giving up her address instead she's hiding the address and still getting a valid signature from the coordinator so so the coordinator is going to make sure that the input is in fact confirmed and unspent but the signature is valid that the that the

**00:07:24**  amount is correct and it'll the coordinator will provide a signature for the blinded output and Alice will store that and that stays one so all the participants are going to be essentially registering in this stays one this is the phase one is the longest base and it will last for up to two hours hypothetically it'd be classed as long as you want in Phase two the connection of all business will be confirms anyone who is unconfirmed that means that would

**00:07:59**  have to be registered because otherwise we don't know which I'm blind oh no excuse me whoever is not confirmed that coin will not be will not have to wait for its signature because that user has dropped out from connectivity and then Albert registration and in this miss phase all the users are going to anonymously post overt or their outputs that have invalid signature but are now unblinded and this will allow the

**00:08:31**  coordinator to put all the outputs of equal denomination on the right-hand side of the quadrant transaction without knowing who it is that because who exactly presented that output it's important that this algorithms roughly at the same time so that all users are sending their unblinded outputs over toward at the same time so there's no timing analysis by the coordinator or anyone else and now that the coordinator has this transaction which has all the inputs it has all the anonymous outputs

**00:09:03**  and the change outputs now the coordinator can present this unsigned transaction to all the participants and we reach the final stage which is the signing stage of course if we did this over the the clear Nets we would have an issue where the coordinator would know the location the IP address of all being visuals or a passive bystander could could sort of figure out who is ascending outputs based on common IP addresses and that's why everything has to be done over a tour so all the

**00:09:36**  outputs inputs status requests all that must be done over tor and support as well that Newt or circus need to be established for various parts of the protocol so that again connecting the particular inputs to outputs can't be done okay so one of all the participants get the final point they'll make sure that they are not being cheated that we have their output and their change and then they'll present their signature and

**00:10:07**  give that back to the coordinator for collection then what you point the coordinator will be able to take a fully signed transaction and broadcast in the network all right so that is all that we need for that part and we'll move on right back okay so the result is that we hit this

**00:10:42**  we have our participants they have a equal valid coin joint we don't know who which outputs belongs to whom although the change is perfectly linked almost every time if some in some instances that the chain isn't perfectly linked but in almost every instance the change is what's one perfectly late and we describe the level of anonymity of these three outputs as in the same way that we

**00:11:12**  described tor anonymity which is to say that it's as as anonymous as the other participants in that are participating in the coin joint so in this case we would say the anonymity set is 3 but that is just the theoretical upper bound for the anonymity it could be much less if someone gets compromised some immediate limitations that you should observe when we talk about zero link is that mixing and sending are separated so users will have to receive coins mix

**00:11:42**  those coins and then send those coins and the mixing and sending are separated a user may get many many outputs depending on the amount of coins they have which again is not ideal for a lot of users if a user has a very large amount of Bitcoin or a very very small amount of Bitcoin they might be able to they might not be able to participate or they will participate and have many many coins or just cumbersome nearly all users will have some unmix change so if we have a fixed amount almost everyone's gonna have some change and that change there's not anything that you can really

**00:12:13**  do with that change apart from you know donate it open a lightning channel or wait for more coins to come in so that you can mix it with them and then users really depend on the frequency and behavior of other users so if you want to mix very often and hopeful that many people with the same denomination also want to mix very often and of course this model may had a lot of blow to the network because we're doing a lot of transactions where we're not sending money to anyone we're just mixing money so we're gonna briefly talk about

**00:12:44**  attackers and then two questions so privacy is teamwork what that means is that you are as protected as the number of participants that are behaving in an anonymous way as you are if other participants fail to act in a way that preserves their own anonymity your anonymity has occurred just by the fact that they have revealed themselves this is a pretty obvious concern so for example if orange is

**00:13:15**  revealed now blue and yellow both have a reduced anonymity and if blue is also revealed than yellow without even knowing it you know yellow could be doing everything correctly but orange and blue failed to act in an anonymous way they revealed their their address links so now yellow is by by elimination also revealed so our attack vectors the first attacker described in the beginning of repro that the paper is a Doss attack now the idea

**00:13:47**  of a Doss attack is to stop the coordinator from successfully making more joints happen and the way this attack of word is you have someone like orange in this case who is purposefully registering coins that are valid but orange is going to purposefully not sign transactions or do his or her best to prevent the next coin dealer from happening so maybe orange will take many many many coins and continue to register

**00:14:19**  them and then purposefully not sign them or maybe spend them before the core joy is complete a few ideas were proposed in the in the paper one is banning an IP address which obviously wouldn't work because we don't want to know the IP address of a lot of the users so it's going to be very hard to find out where they are and we wouldn't want to use that another way of dealing with this is by completing the coin joint with a subset so if a hundred participants have

**00:14:50**  joint and five are committing a dose tag simply ban them to continue with the 95 our meeting participants and if you find another three in there that are committing a Doss attack purposefully not signing then you banned them and you continue to reduce the the number of people until you have only the people that are legitimate this is also not not ideal but it's it's it doesn't work at least

**00:15:22**  although it's not it's you know it's not perfect so there's also they do have closed-source das protection so maybe you know you could have everything open sourced but the das protection you might have a closed source so that it's harder for an attacker to establish the optimal way to attack you and the attacker has to sort of a reverse engineer your your prevention a pretty interesting idea about but I believe by Chris Belcher is the use of fidelity bonds essentially bitcoin that you put in escrow that you

**00:15:56**  will lose if you fail to engage in a protocol this is quite a cumbersome it demands that the the round take a lot longer and has been sort of opposed by quite a few individuals and lastly we have banning the registration of provided utx o--'s and related new taxes of malicious alice and this is quite simple so if the particular coin didn't assign simply bad that coin and been its children and its parents potentially it

**00:16:27**  you know for let's say an hour and then if the attack persists for a while you can ban for longer periods of time like a day or a week obviously the concern here is that people will refuse banning refuse signing by accident if the tor circuit breaks if the internet connection goes down whatever maybe you don't want to have someone stranded with unlink waits for a week because you wrongfully assume that they're trying to commit a daus attack so this one obviously works but it's a bit of a double-edged sword we have to be careful

**00:17:00**  amour another attack which is kind of interesting in its own right is the simple attack now the civil attack comes from an individual who purposefully does engage with it or join and does go through and the entire Corps join but the ideas of the individual has presented many many many inputs that they alone hold and what they're trying to do is they try to eliminate the potential outputs of other participants by excluding their own

**00:17:31**  inputs so let's say instead of three participants we actually have two participants one is green who is malicious and yellow who is honest and green here has green change outputs and green mixed outputs and as you can see green alone can see that the third output is the only other output that doesn't belong to them so they can quickly narrow down the anonymity set in this case down to one but it doesn't necessarily have to be down to one it

**00:18:01**  could just be severely reduced and the last one we'll talk about before we just open up the condoms of questions because I'm sure that people have a lot of things to say is that behavior discrepancy is a big one so just like in tour we talked about how in tour the problem is is that if there aren't enough users that behave the way you behave then you're singled out so for example if the user arrives with an amount of Bitcoin far larger than the users in the pool they will be detected

**00:18:33**  if they read combined coins post mix we've seen a lot of people in the public square a lot of thing and poking about this the fact that you know whales come in two to a zero link protocol and when they exit it's obvious and therefore the system doesn't work it's more fair to say that the system does not work for people who are acting alone if you have ten thousand Bitcoin and everyone else has a you know between one and ten Bitcoin and you enter with ten thousand

**00:19:04**  and leave with ten thousand yes you are much much easier to spot another thing we might see is that if the user sends funds and coin joins during an uncommon time zone they could also be detected so timing analysis based on when people makes an that is another big issue and lastly we talked a bit about the philosophy of building privacy systems in anonymity networks and how the way that user puts the settings on their wallets can reveal

**00:19:37**  themselves as being unique if they said the settings in a very particular way they can actually hurt themselves and this is things like for example setting a custom fee when you send funds or when you send funds how often how frequently and so forth so concluding thoughts zero link is a sponge ability protocol based on an untrusted central coordinator equal output mixing and the anonymity of large crowds much like tor it is a system a pledge ability based on anonymity

**00:20:08**  networks so I want to leave it at that but I will say there's a lot of things I want to say and could say you know about for example current implementations or what I think you know how wasabi works in practice or other attack vectors but I think that will sort of uncover them together as a group as we talk further on and I'll bring them up if no one brings them up and that's pretty much it

**00:20:39**  for me okay thank you for the ironic or an ironic clapping I'm not sure which one knows good question about the simple attacks has that ever been something that wasabi or anyone in the community has detected occurring I know it was a very large consideration in the original

**00:21:10**  work no I think it's not possible it's if you think it through I mean okay how would you define CBL is easy BL the anonymization of an output complete the anonymization of an output or or it's okay if you if you take like 50% of the mix and then they gain half as much unanimity than they want what

**00:21:43**  but we'd never say for the studio yeah I probably need to be deionization to the point that you can narrow it down to suspects for example if it was used in some sort of criminal investigation because I imagine nation-states are the only ones who have the kind of funds to conduct a civil attack it's expensive 100 you need to provide 99 peers for

**00:22:15**  every single coin that that wants to do coin join and I there is oh actually now I I can count with that because I know the exact number you know this fresh Bitcoin thing the wasabi Co enjoying efficiency github repository I created that I I look at how much fresh Bitcoin comes into Vasavi

**00:22:47**  daily and for that you have to provide 99 times as much in order to completely do anonymize every single wasabi mixes and there is 500 fresh Bitcoin coming into wasabi daily which would mean you would have to provide 99 times 500 Bitcoin to disability' cassabi that's the that's the number there we need the

**00:23:17**  more likely scenario be a simple attack targeting an individual output rather than all the Saudi users but you cannot target like that you will have to get all the subuser actually the coordinator could selectively target right that that is that is possible yeah yeah well but wanting to consider

**00:23:50**  principal attacks instead against anyone other than the civil attacker you still get a minute he said of course depending on pre and post makes coin behavior but but if for example one one guy has 99 outputs and for an outside observer it's doable 100 an anime teaser I mean I didn't think of it but now that you

**00:24:21**  bring it up if you select one input exactly or or then then you can provide the coordinator is the only one who can who can make sure that which inputs are participating right that's that's the dose protection there so so yeah it's if the coordinator has 99 times as much coins actually not even 99 times because

**00:24:55**  because it has to because it can lower the day on all set although if you lower down on set for 4 - that's not workable because then the guy is going to mix his coin like like like like 50 times in order to get the get the green shield so so yeah at 50 times now not 99 times 50 times as much as much as you want to do

**00:25:27**  the anonymize someone it's actually yeah I I did not think about it now it seems Moria and just I'm just catching this one on the fly that yeah the coordinator should be able to to severe attack but what anything as his is completely

**00:25:58**  unrealistic there that's really the 99 times 500 Bitcoin daily that's how much has to be lattaker would need he cannot he cannot even decide which machine could city's attacking you know so it's a matter of liquidity rather than expense in the case the coordinators the attacker because the coordinator receives the fee for the coin joint as well

**00:26:28**  yeah I didn't even talk about fees I was only talking about the initial initial requirements the individual requirements at this point yes the coordinator would have to pay Network fist - yeah it's that that's not that difficulty there sure

**00:27:04**  anyway guys I'm not bringing up topics here because that that would be strange so I guess we can we can finish this this up or or or do you guys have something no I definitely have quite a lot of stuff I think we can talk about so unless what are we gonna talk about after after this Adam did you have

**00:27:39**  something to talk about after this okay so I feel like this is somewhat an outdated paper other than the Jamie and Coen Jane stuff nothing aged that well other than the basic decor protocol nothing aged that like the zero link framework was was not a very successful in inside this wasn't

**00:28:11**  successful because this was supposed to be used by multiple wallets that's why so much time was spent on making sure the bullets aren't around finger printable but but as as time went on it became more and more clear that that cannot be made sure and it's not like many wallets would have been interested in privacy so so I think that was kind

**00:28:45**  of a waste of time and a waste of space on github to to specify so so many things there the coins are in protocol the Charmian Cohen jury in protocol actually aged very well and that's other than implementation details everything is the same if there were guys here link library would that make a difference if from wasabi wallet there was an engine that

**00:29:17**  just powered zero link that one could build a wallet on top of not sure but I wouldn't bother with it because we are working on how would you say it's zero link 2.0 but it's not even 2.0 it it's a it's a similar thing it solves the issues that that the chummy and conjoined think has like oh there is a minimal denomination or you cannot send

**00:29:49**  in the coin join so it solves the the largest issues there and and and I wouldn't bother with which they don't link anymore because this this thing is it's going to happen going to be be released in in in this year I'm keep referring to this distinct because we don't have a name yet and we just started it today but it was

**00:30:22**  an extremely promising day so I'm really excited about this guys Marx wrote in in the chat that he has a very shitty connection so he wrote a couple of messages with questions to the chat the first is how does the new implementation of mixing with multiple woman in one instance affect Sibyl attacks anyone wants to winstram that okay loud and

**00:31:03**  clear the second question was what is the current implementation of dust protection in wasabi how did you call it just white bedding coins yeah burning coins so if someone doesn't sign it is banned right now for two hours because it's we don't really have denial

**00:31:33**  of service attacks it's more like unreliable anonymity Network unreliable tor connection that seems like much more of an issue than than we thought and of course honest peers cannot be differentiated malicious peers cannot be differentiated from peers those has bad connections or or or not even not even

**00:32:03**  individual connections but but the connection can be bad through the onion Network the route that you choose so so that's that that's a huge protect practical issue there and and yeah it's it's it's it's it's bending Cohen's from participating for for some time we are also going up and down on the transaction chain so for example if you spend that coin then you still cannot

**00:32:35**  register into to the wasabi mix because well that would be going around the dose protection although this this gets expensive for that occur anyway it's it just banning Cohen's it doesn't I would love if someone put this to the test but because we didn't even had to use our very basic configurations and we

**00:33:08**  actually wrote a lot of code to to be able to even make this much more severe so if someone would attack wasabi and would be successful then we could just change one line in the configuration and and and he would have to come up with a completely new strategy so I feel very confident about that at this point and and I I don't know I no one bothers to to attack it but maybe it's because

**00:33:41**  because if hacker hackers don't want to attack it because there is nothing to gain from it generally these companies don't want to attack it because it's illegal so that that could hit her isn't there okay perfect another question no I don't can you speak more about your coin joints to docq analysis of change outputs did I

**00:34:22**  wrote anything about this thing zero link yeah I'm not sure I'm just reading what max sent me III sorry max can you I don't know what max has it max has a very bad connection now so he's just sending over his questions in chats and I just read in them out loud basically so yeah that was his question about your

**00:35:01**  core joint sort of analysis of change outputs deinonychus he says that you did analysis of change with coin join Sudoku and the non equal value outputs created yeah I got the information I had is aut EXO that was smaller than the the D denomination the base denomination and I

**00:35:36**  give it to try to the anonymous it and I couldn't that's that's pretty much it even though I know other coins must had been meshed together in the mix there were more possibilities than then I I initially thought so I couldn't figure out which even which which coins it joined that coin together read so so

**00:36:09**  yeah it was a interesting exercise I hope that would answer this question I just have one more question about the max Max's first question about the multiple wallets in one instance doesn't it just make a Sybil attack a little bit easier that the attacker doesn't have to

**00:36:39**  run like many wasabi bullets she could just read so yes it does make it a little bit easier but if someone really wants a simple attack and they want a simple attack wasabi specifically they're gonna need hundreds of thousands of dollars worth of Bitcoin and they're gonna need to be quite dedicated so or is it if they if they can get hundreds of thousands of dollars of Bitcoin and they have a committed attitude to breaking

**00:37:11**  this they probably know how to do it with or without multi wallet support they probably are comfortable running it on multiple subsystems that would only add a little bit of cost compared to the cost of the Bitcoin they would have to have to do it so I don't think so but what it does do is it does mitigate the person who has maybe two businesses or one business and a personal account and they don't want to reveal to the world that those two things are related and if they try to manage it in one wallet they

**00:37:42**  can accidentally cue coins together and do all sorts of things whereas if they now have two separate wallets which they can link in at the same time and coin join at the same time then it will be easier to protect them yeah definitely and I do agree I mean I don't see Sybil attack as a actual like real risk in Wasabi's case I think there's much better things for these companies to do if they would try to do something so yeah so let's talk

**00:38:16**  about that a bit right so how so with a civil attack you want to have as many helpless as possible that you know and that that allows you to narrow down the of the other outputs you know if there are even two honest participants then you can reduce the anonymity set all the way down to two one thing to note is that if two people are engaging in a civil attack at the same time but they're not coordinating with each other

**00:38:47**  then they further add anonymity so the the simple attacker is in a quite a difficult spot because they have to hope that there aren't a lot of people participating the only one engaging in this attack so I I think it is quite unreasonable however if you drunk the anonymity said about have a coin joint down to you let's say I don't know I'll top my head let's say five which would be a really bad idea but I don't know let's just off top my head then it is very practical to do

**00:39:18**  with this attack right and I talked about this at length how you would do it if there was if the upper limit of a courtroom was five participants all you would be five or even ten large coins put the one on separate computers or separate you know instances of your your your coin joint software and you just hope that enough collisions of your ten instances appear on on any given point and if you have

**00:39:49**  will give you one collision like that is to say two of your your your wallets intersect it yeah I totally agree with that I mean it has to have enough participants per round to be actually effective against

**00:40:20**  the civil attack and also to have a big enough of amount except minimal but we thought the round okay so if no one else doesn't mean you say I want to bring up another thing so let's let's talk about the unanimity set a bit right so in my presentation I talked about coin joints as though they happen in a vacuum there's just one coin joint but we all know that Cohen joints happen

**00:40:50**  sequentially and most participants will engage in more than one coin joint because they have more than one clean coin that they can receive so you know if you look at a core joint in a vacuum the anonymity sets pretty obvious it's the number of honest participants in that coin joint and we assume because we could possible to prove otherwise we assume that the theoretical limit is that everyone is honest now if a person

**00:41:21**  remixes and suppose they remix in the adjacent coin joint they're gonna obviously get some additional benefit and I think this is where Adam and I have have had disagreements at times which is that I don't believe that remakes thing in an adjacent go in joint does even it does as much as even double the anonymity set that you currently have so if there's 50 participants in the first and then 50 participants in the second the likely unanimity set of engaging in both those

**00:41:52**  coin joints with the remix is probably you know from 50 to 60 or from 50 to 70 and and the absolute upper bound would 100 but it's unlikely because other participants also engage in sequential coin joints so you're hiding in the same crowd of people and I'm curious if anyone has a on that well I do agree that it's kind of like the more accurate way to just say it would be like the for

**00:42:26**  example for one remix round your total anonymity set as a like a maximum could be like the amount of UT exo's in the second mix - the ones that came from the previous mix from the previous round and also like adding all the persons or the participants who were in the first round I mean some kind of mix from those and

**00:42:58**  yeah I kind of understand your point that it's not like they're 200 think about it in a probability from probability point of view rather than unanimity set point of view if you mix take take a coin take your coin take a round on coin from the blockchain and mix that now you're going to get a zero

**00:43:28**  point one Bitcoin out of of that mix and of well the zero point one Bitcoin output half of them are remixed and another half of them are not remixed so there is a 50% chance that you remix that random coin but you just took from

**00:43:58**  the beginning and on the next go enjoying again a 50% chance that it's gonna be remixed and on the next coin join again a 50% chance if it's going to be remixed and now work with these probabilities so what are the chances that you are going to remix three times and that's not much that's that's very mixing that's why

**00:44:33**  people talk about the exponential privacy gains of free mixing still not sold in particular so it it comes down to the actual user behavior of the propensity of someone to remix so before you know you know in theory any coin in

**00:45:03**  any mixed coin from wasabi could be a coin from two years ago that's just been remix thing and remixing and re mixing well however what's more likely is that you know that there's a 50% chance that it from a direct participant a brand new another 50% is that it makes when you say remix we mostly mean in the sorry you actually got it yourself next here

**00:45:41**  we go so I really don't don't buy this because and I've had this argument with another some other folks about about this matter but of those remixers most are coming from the previous conjoint of which half of them are new mixers and so when you do this when you go back you know to say 2 or 3 or 4 remixes you're

**00:46:11**  already getting to a very very infinitesimally small probability and the majority are from you know let's say 4 coin joints of which most of those people have inter as overlap of participants so again you have a very you know potentially a linear climb in terms of anonymity but the only way I would I would be I would say I'm wrong is is it the nature of wasabi was such that people who mixed

**00:46:43**  older coins had a priority in remixing such that coins from very distant coin joints had an advantage to participate in new coin joints and then I would say there's more probably it's still probably linear but it's at least faster in terms of the anonymity said growth may I just add one more question about that I mean let's just think about like two rounds of mixing the first one you

**00:47:15**  have hundreds of participants you are one of those let's say that 50 of them goes and remixes on the second round and there's also like 100 participants wouldn't your anonymity set be like from the first round you would get like 100 from the outsiders I'm unsure from which perspective to look at this but I mean you could get like anonymity set of 50 from the first round and if there is no remixes after the second round wouldn't

**00:47:47**  it be like more of likes 150 more than closer than the 200 and it shows correctly it would be 150 you're exactly right except it would be a hundred and fifty with a caveat which and the caveat is the probability so there's a 50% chance it's it's one of the 50 people right and then there's a 50% chance it's one of the hundred so in other words if you say is it is it someone from the

**00:48:18**  first coin joined the answer is there's like a like there's a smaller probability it's from the first coin join than it is from the second coin join in terms of the participation so it's not a uniform probability but you're right it's a hundred and fifty anonymity set and not not 200 also it's very important understand that it displays how inefficient it is to have small coin joints the bigger the conjoined the much much more efficient yes I had a question that if if the

**00:48:55**  current implementation is vulnerable to Wagner attack for those of you don't know Wagner attack is this is possible in V dash nor blinding signature scheme and it it works something like this you you get more and more signatures the more likely that you can you can I don't

**00:49:27**  know what you can do with that but the more likely that you can execute this Wagner's attack I don't remember exactly what happened but but that's something that we consider affect them and so so you need more signatures from blind signatures from the same pop key and you also need more time and that's how we we mitigated it first we don't give out that many signatures and you also don't

**00:49:58**  have time because we only give out the signatures in the end of connection confirmation phase so from from their own you only have three minutes maybe two to execute this attack so that's not not not not very doable also very we don't reuse the design in keys so every round the new signing key is generated

**00:50:28**  that's the that's the that's that's that's that was our mitigation there yeah okay thank you this this is a question also that all the posted previously why did we switch

**00:51:00**  from Charmian to snore blanching signatures because we introduced the denomination and there is another attack if the coordinator lies about the the deed around parameters and the most important such transferometer is the public keys so so we introduced the new denominations and now every denomination needs a new a new public a new new

**00:51:34**  signing key so the thing is that the the RSA signature scheme is extremely heavy and our mitigation of the coordinator lying would be that that we are somewhat probabilistically mitigating that there is a monitoring identity in every client not only those who participate but but every one and every time and you keep

**00:52:05**  sending the the backend server a request that a status request and that status request returns a a a fair amount of things like the filters that returns the Bitcoin price that returns a couple of things but it also returns the the public keys of this round so it returns 11 public key and this is we did with

**00:52:41**  RSA scheme this this would be a huge amount of network traffic but with snowblind signatures this is just this is just 256-byte I'm not quite sure but but it's it's it's much smaller so we we begin gain some some edge there that because it's much smaller and it's a very frequent request

**00:53:21**  imagine it like this every every minute someone every minute your client sends a request I'm not even sure if every minute even more frequently maybe sends a request to the back end that hey give me your status and every time the backend ants were sweet with the 11 public key of disco enjoy me round even if you are not going joining so we had to had to do to lower that also another

**00:53:54**  consideration was that we did not want to rely on different cryptographic assumptions because Bitcoin already realized on a little curve cryptography an and and so we we didn't have to rely on their assay cryptography here interesting okay I guess if nothing nothing is there then then I want to to

**00:54:25**  go into the future bit more and just to keep you guys up to date updated that nothing much and east van Sheriff Ron rash and me started working on the new coins the new mixing scheme today and I have to say it's much more it's even more promising than I thought so nothing

**00:54:58**  much just outlined a few things that I didn't think that was actually solvable and we are only so we don't want to leave you out we are only working on a first draft which is about we don't we take a lot of things out of the scope even the network fees everything this is only about to present the idea in a in a

**00:55:29**  very digestible way so I was thinking we can do this in ER in just just this week but as as I said nothing much presented something that could be much more that that could be quite revolutionary to be honest and and that's something that has to be explored before the idea is presented and and

**00:56:00**  this is the anonymous what is it anonymous crashes and there is a paper which I would like to propose for the next was a bee research Club anonymous credentials paper and that way maybe we could figure out if this this is something that that could work or or or not so that's that's that's about it I

**00:56:33**  am really excited actually that after today and and and and and get you guys as soon as we we finish just a quick draft of the idea and share with you and and everyone can can participate and join and and whatever you guys would would like to do with it if you would and that would be great and work out the

**00:57:05**  research together perfect thanks for the update Adam can I ask you to maybe it's possible to shift its kind of recession that you have to mainly research thread and slack I mean that would be very helpful because for example in RGB there are a bunch of protocols that might be useful for you also and I want to make sure that there is or there is a synergy

**00:57:35**  that we can work on together or there is no synergetic list yet and I can just stay updated something like that I don't think so it's hard enough to to follow each one and nothing much to be done and handed em just the two of them and I I mean there is a limited capacity of how much information we can we can get in and if

**00:58:08**  if people keep coming with with new things like oh let's put it to the Lightning Network and pay to endpoint and things like that so I I really want to rule out as many things of the scope of this first idea presentation as possible and after that yes but but but until we don't have a stable idea I I

**00:58:39**  would prefer not to so I I would kind of prefer if a weave could participate I'm not quite sure about because it's like he has another job to do and I just you know I'll do it you know I love my job I

**00:59:11**  always I would never okay I don't try now really okay the anonymous crashes paper maybe maybe maybe that will give everyone the same idea what we are doing I don't know you see if we stop

**00:59:48**  recording no not yet so don't say you're quitting I'm stopping the recording all right greeting [Music]

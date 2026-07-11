# Wasabi Research Club #10 - CoinJoin Sudoku

- Playlist index: 10
- YouTube ID: `CtmSylCQNIc`
- Video: <https://www.youtube.com/watch?v=CtmSylCQNIc>
- Duration: 0:51:45
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:01**  [Music] all right welcome to another episode of the wasabi research Club today we are examining coin join Sudoku weak privacy guarantees for shared coin mixing service and we have the author with us today to talk about it it's not fair to call this a paper as much as it is a

**00:00:32**  weakness that was discovered in 2014 and then published to alert the community about the concerns with a particular implementation of coin join we're joined by Christophe Atlas who will answer questions and correct anything that I've said incorrectly about his his work and he also happens to work for Lockheed calm which was launching the info which is the particular protocol in question

**00:01:05**  that what we are examining here you can find all of the work and all information on our github link just below just a reminder where we are we did four weeks of coin shuffle plus plush and cash Fusion last week we talked about principles in privacy which was much more philosophical and less math heavy this week is called Jones todoku and then of course as always we decide on

**00:01:36**  the paper for next week at the end of this call you can find out everything on our github of course just a reminder what we talked about last week and when we talked about prints of privacy principles we discussed how there are some common reoccurring things you shouldn't do when you are trying to build privacy tools in anonymity networks and those things include for example in secure modes of operations on your software or optional security that

**00:02:08**  someone might turn off and never turn back on or badly labeled off switches such that the person doesn't know that they're you know not using a very critical privacy feature it's important that the security is convenient because if it's incredibly inconvenient everyone will sort of sidestep the proper way of doing it the full sense of security is really important to avoid and ensuring that we have good mental models for how we think about privacy for the user such that they know when

**00:02:40**  they're doing something correctly or incorrectly and we had an interesting discussion against options so minimizing the amount of options that the privacy software allows for the user we answered this fundamental question or at least we try to how should we think about building or using privacy tools and nm8 networks we discussed how a tool like tor which is an anonymity network depends on users that are entering and exiting the Tor network and we're not entirely clear who

**00:03:10**  is who but there are obviously some problems with these anonymity networks for example if there are not enough users in this case here there's only one user so it's clear that even though this user is routing through tor the the output and input can be linked quite trivially we talked about how common behavior can help us link inputs and outputs here we have a lot of english-speaking people and then we have a Hungarian speaking person and we can link the Hungarian

**00:03:40**  inputs and outputs because there are minority today we're talking about something different we're talking about a flawed implementation at the COI joint and it's fair to say that this paper it would have been better had we read this paper before reading the 2017 knapsack Khoikhoi paper we're gonna find out that the knapsack paper in 2017 did a lot more work and likely built off of this work so essentially where were we're

**00:04:13**  examining a paper that has they cover a lot less ground and I think that's okay because it was it was very early on in the Bitcoin privacy timeline so what is shared coin shared coin is the coin join implementation by blockchain info some basic things about shared coin coin joins that they typically have more than nine inputs and more than nine outputs number of inputs and outputs were often different and

**00:04:45**  there was a constant minor fee of 0.0001 denomination transactions were also always broadcast from the blockchain got info IP address just I've been here for a brief moment although the number of inputs and outputs was typically fairly high since publishing that advisor I did come across some transactions which were you know claimed to be shared quite transactions difficult to verify

**00:05:16**  decisively but some of them had fairly low in the ballpark of maybe even four inputs or outputs so there are some certainly some exceptions to that rule for what it's good yeah and that's a very good thing to point out I think it's fair to say that apart from the minor fee and the IP address of the broadcast there wasn't anything that clearly outlined these transactions as being part of shared coin apart from the

**00:05:47**  fact they have more than the normal number of inputs and outputs that we would expect so this is called fingerprinting so here we're fingerprinting a shared coin coin shine and the idea of coins to do sodoku and again this was it back in 2014 is what we talked about with the knapsack paper which is that we want to find groups subsets of a transaction where input sums and output sums match and at this

**00:06:20**  point I think it makes a little bit of sense to just quickly remind ourselves what the knapsack paper covered because in all honesty again the knapsack paper just did get a more thorough job of answering this question because again it was written quite a bit later but the knapsack paper oh my goodness I think I might be getting kicked out of the room pardon me one sec sorry guys I apologize

**00:07:05**  I'm just gonna be 10 seconds and we're gonna get back to just be yourself for a second if you meant yeah a lot of people are wondering you might have some insider information why was shared coin discontinued the founder what I want to say about that so I think it's fair to

**00:07:38**  say that as people started exploring these type of services there was increasingly concern from a legal standpoint as to how various governments about the world might treat such services and and how this would overall impact the regulatory attitude towards Bitcoin people are pretty concerned about the idea that you know these kind of services gaining popularity would

**00:08:10**  paint cryptocurrency the negative light at the time so I think that is something that factored into it I think it's also fair to say that you know compared to the overall volume in the Bitcoin network and certainly at blockchain not info at the time it was a relatively small poor of of transactions that were using the service so probably some combination that you ultimately led to the decision not to continue the project I see thank

**00:08:43**  you I can see that was pretty much everyone's guest but there was no real confirmation about that at least as far as I know so what's up Aviv are you back oh I'm sorry guys I just had to move rooms everything is fine we're gonna continue as as normal so a shared coin did what the Nats of paper talked about which was combine transactions together because there's nothing in the protocol that excludes one person's inputs and

**00:09:15**  outputs from not being part of the same transaction as another individuals inputs and outputs and you know here we had an example that we looked at and I think two months ago where two unique transactions and on the right you see them being merged and when we merge two transactions if we want to investigate any input and output links what we really want to do is figure out a

**00:09:46**  matching sums on the inputs and outputs so in this case we would take a hypothetical output like this cup number 50 and then take an input maybe another input and we try to see the sums on the left and the right and in this case they don't match so which I get with a different set and here you can see that the inputs and outputs perfectly match to break this transaction into two transactions it's like that perfect we

**00:10:21**  talked about how good is the anonymity provided by this simple model and can we improve upon it it turns out that in 2017 it was clear that this naive approach which is the approach that shared core took more and we talked about that at length during that call we're not going to go into all of the math stuff but there is a nice definition that I liked from from that paper which was we can take any

**00:10:56**  transaction and break it into sub transactions at a minimum there's one sub transaction which is the original transaction but ideally you want to find more than that and you want to see how often inputs and outputs appear in the same sub transaction and so the the the paper has this big thing here but all this this is a fancy equation is saying is that you simply take all possible

**00:11:30**  combinations of a transaction and then and that's on the bottom and on the top you take only the the combinations where a particular input and a particular output were we're together and what you get at the end is some sort of percentage of a probability of how likely they are to be connected now this was very this is very appropriate and accurate in terms of being able to break down a transaction that that has to

**00:12:00**  believe to be a coin joint so in the paper there wasn't an example here of a shared coin transaction being broken down and it's it's still a bit hard to see and I think a few people mentioned this as well it wasn't entirely clear how this breakdown was achieved and I think that in light of the 2017 paper we would not have agreed this is how we would break

**00:12:32**  down the transaction so the red here actually makes a lot of sense because it is the it's a perfect match but it's also the case that it's the only inputs and outputs that have five decimal places every other input an output has as fewer than five decimal places now over here you know it's this might be a plausible way to partition this transaction however it's unclear why we didn't

**00:13:04**  partition this into five sub transactions within this transaction for example you see a 0.03 by BTC over here and on the right you see a 0.03 so who's to say that's not one individual that moved money to themselves and you see that many many times so it's just unclear that these entire sets of transactions must point to each other and then over here again we have this problem where there are mappings on the left side on the right side that were

**00:13:36**  unclear so you know it comes down to the fact this was written kind of much much before a lot of people were interested in sort of figuring these things out on that oh you're finishing already okay and then come back here so I'll just wrap up and say that you know I looked at the the github and some of the work

**00:14:08**  and it does seem like this paper was was later extended with other people's work I'm curious about what Christophe has to say today but I do believe it was somewhat incomplete but anyways yeah we can we can open it up to discussion okay so let's talk about that first so as soon as I understood it you release this

**00:14:39**  advisory and shared the cool advisor into block chaining and then you did not follow up with code later on is that correct or I did not find something yeah that's right so there was a responsible disclosure period once blockchain was on board with kind of publishing it and put something out there and the graphic is just wrong obviously I put it together a little

**00:15:11**  hasty I don't remember exactly what the mistake was that caused that that error but some yeah that I never got around to really correcting it but you know I figured that the the gist of it was expressed as far as the code goes I was never really very happy with the tool and I did become aware of some other people working on similar tools the main one that has really advanced since then is now I guess the repositories under

**00:15:45**  the SMR I guys but Boltzmann is a a transaction analysis tool that can do this kind of comment or comment or subset some knapsack problem kind of analysis and so I just never bothered to really clean up the code and really get it out there because I figured that this other tool was was better so that's the story as far as the source code goes thank you I was actually thinking maybe you actually had some holistic

**00:16:16**  assumptions that you could make the blue connections there but but okay so that's not the case but Aviv even that you you put a tick there that that the the red is is good right but even that's not not correct because you you might find a soft set there and you might and you find corresponding subsets from the remaining inputs and

**00:16:47**  outputs but that doesn't really matter because what really matters is that all the possible subset combinations so if the red could even be if you can create subsets with the output that some of the Red Coins are in then you would have to do do your calculations there you know what I mean absolutely I only put a checkmark saying that at least this sort of intuitively

**00:17:18**  makes sense but you're entirely right the red outputs also could be put into other subsets so my point is crystal until you find all the possible subset combinations you cannot really make a conclusive statement of any of the these subsets

**00:17:49**  you could start the red ones for the red ones just looking at it briefly it looks to me like we know that the red ones all go together they may and then the same user you know the same key holder let's say may also own other inputs and outputs including the possibility that all of them are owned by the same person that's not actually how shared quite service ever worked so that's not really a possibility but but as far as the subset-sum issue goes we know the red

**00:18:20**  ones go together but they could include other inputs and outputs for that particular key holder it's not fair to say I'm not sure about that politically I think this well if you so so for example one of the one of the efficiencies that I try to gain in the system is it would start at the least significant digits from the end of the the decimals right and start matching from there and kind of work its way up and so you can see obviously like a

**00:18:53**  vivre mentions that there's not enough decimals in the the other categories too to create decimals that far down in the number so I won't try to do the math of my head but I'm pretty sure that that's kiss okay okay that's interesting that actually yeah that's another topic that I wanted to bring up that let me read from the paper where is it

**00:19:26**  for the sake of speed efficiency the tool currently processes the transaction by examining one digit at a time in the inputs and outputs working its way from the right to left this is faster because transactions typically involve inputs and outputs with many zeros which can be ignored by processing given digit it's actually it may be even a new hair ristic or or one of the heuristic that

**00:19:58**  Eaton Hammond was talking about when we were talking about knife conjuring so definitely an interesting that you can just it was it's not a isn't a matching heuristic but it's a way of trying to speed up the process which I resorted to because the rest of my code was so horribly inefficient as far as computing the subset something like that that I tried to incorporate that and there about if there is it was a bit buggy and you know so that's that's what I never put the code out there didn't feel like

**00:20:28**  trying to get it all result but it was working well enough that you know we could say decisively we could grab a bunch of shared coin transactions show that some of these definitely were matched up and and put it put it out there that the service was not working in the way that you would see on the Left you know someone naive naively looking the transaction on the left side of it might say oh it's a lot of them put them up puts must be love obviously there but in reality that's not how it was workings and you did not have any

**00:21:01**  other so you didn't know how many users are in the transaction and you did not know how many inputs or outputs one user would create so so these assumptions you you did not have any of that yeah that's correct so if you if you look at that shared coin source-code the server side of the welt both the server side and the client side technically were published the the short

**00:21:34**  coin server code has been inked from github but I imagine that if you looked around a little bit you could find it elsewhere but anyway so you know the way the server and the code works was kind of coordinates these joins there's all these parameters that you can set in you know a JSON file or something like that in it so that will define things like you know the minimum and maximum number of users you know a min maximum of amounts and so forth so that there's been various little parameters there and

**00:22:06**  those were tweaked over time some of those tweaks seemed to have been published to the shared coin github server but of course we don't know for sure whether all of the changes that were implemented on the server resulting on on change oints we're actually you know put on on github I don't have any insider information on that so so the way that the number of you things like

**00:22:36**  the number of users and some of the particulars about how these things are structured probably changed over time and we can see some of that suggested in the commits to the server repo over 10mm that's a really interesting point that that blockchain analyst is really having a hard time of when when some parameters and changing in some wallets and then when when do users upgrade for hypothetically someone could have

**00:23:08**  downloaded the server code and run their own sure coin instance right and they could have taken the client code and tweaked out or written their own client so it's even possible that not all of these shared coin transactions quote-unquote were run by a blockchain dot info at the time it's possible with other people who are doing it I find that to be somewhat unlikely or if it did I would expect it to be a very very low volume of transactions on on chain but it's hypothetically possible and you know at the time I think people

**00:23:42**  who were thinking about running mixers whether they were custodial or not they were kind of thinking about this issue of denied you know plausible deniability in it you know this idea like well who's to say that I was the guy who facilitated this this mixing transaction right so I think that's one of the reasons why the source code was kind of published out there it's a big guillotine on my part but seems reasonable to me mm-hmm so most of my larger question or yeah most of my

**00:24:12**  larger questions are answered already so I have some small one but I I leave others the opportunity but but before that I just want to know that this seems like huge amounts of him huge number of inputs and outputs and I I still can't believe that you could write a efficient algorithm to do that because I actually tried it myself I was actually trying to figure your shared Cohen Cohen joins to

**00:24:43**  the COO but but before that when we were in the nob suck papered I I wrote it on it was like 6 inputs 6 outputs and and I mean maybe it was just my code so slow and yeah well some of these well the efficiency things I mentioned around decimal place and so forth definitely helped speed things up I did a lot of pre calculation and pre generating tables that could be quickly looked up but some to be honest some of

**00:25:14**  the transactions some of the larger transactions it would take days on my laptop to try and process them I was too cheap to like you know bias and serious hardware to do it and some of them of are just completely out of reach so yeah so so as far as preventing like mediocre computer scientists from analyzing these transactions the sheer number of inputs and outputs worked pretty well but I wouldn't you know I wouldn't trust it against someone whose

**00:25:44**  job it is to you to do this kind of analysis you know it is probably not not only your laptop it's you know it's not even exponentially it is combinatorics and combinatorics leaves exponential functions in in the mud that they are even faster but it might also be interesting to talk a little bit about like what we're seeing in this transaction so this if I can assume it's a little fuzzy but you know in this this

**00:26:15**  image that a veve has up from the advisory you can see on the left-hand side for example a bunch of inputs of point 0 1 BTC right and it's kind of if you if you ever use shared coin back in the day when it was running it would you would have to wait a few minutes for the whole process to work and and well let's just take a moment to like remember how

**00:26:46**  it works so it was web web wallet only and one of the more interesting things about it was that it always did multiple rounds of joining you never had just one round you had to have it I think it was at least two and they did the maximum was 5 or something like that so the longer that used you the more rounds and you hit there's like a little drop-down that where you could select how many rounds you're going to do to commit to and the the longer the more rousey picks the longer it would take obviously and you

**00:27:18**  would pay a bit more in you know transaction fees as well and so one of my side projects right now i'm trying to go back to you Chery coin and do some more fingerprinting analysis but one of the interesting is to look at the inter transaction fingerprinting as well because there's for all shared coin transactions there was always a clear beginning middle and end to all of the these these rounds so if you were a user

**00:27:49**  back in the day like it used to take a few minutes generally speaking for your web all to kind of wait around and find partners and so forth and I can't remember exactly what gave you this idea but I have a strong suspicion again no insider information here but a strong suspicion that not all of the funds that are being mixed together came from users of blockchain not info time I have a suspicion that the company at the

**00:28:19**  time may have been including some funds as well whether that want the company there are some external source I don't know but so when we see these these repeted repetitive amounts of like point zero one ptc for example this is suggestive to me based on the other like you know kind of rumors that were circulating i think it may have the the guy then may have put this out there at some point in the past like hey we're

**00:28:51**  trying to make this service a little faster by trying to add some liquidity or whatever but it certainly looks like something is being structured here in that maybe the service is injecting these inputs along with the user inputs so the top two in red right they look like no effort has been done to prepare them for this round of shared coin and then some of them are much more rounded amounts and so I think it's fair to

**00:29:23**  speculate that maybe some of these rounded amounts came from from the company or from the service however want to put it and so I strongly suspect that if someone really sat down and looked at this carefully they could really really pull these transactions apart because they would be able to isolate inputs coming from the server service versus the users and there might only be one to three users in this join outside of funds that are coming from you know

**00:29:55**  let's say a custodial hot wallet that was contributing liquidity if I had gone further with this you know research I think that's what I would have started to find is that we could really pull apart the users from the service funds and then we would find not that many users per joint I it's interesting I never occurred to me I actually used share coin quite a lot like I don't know ten

**00:30:26**  times something like that but yeah it it was almost felt somewhat instant and I don't know you can you can say that broke Cheney who had that volume but yeah if you looked at the blockchain and and you found that that it's it's there that is a big big veil there although I mean even if injecting volume here is not that much of an issue from privacy

**00:30:57**  vise because the this you are under the assumption that the server knows the links anyway so it's like if the server participates in the joins then more power to you you know it would only be a problem if you could see your finger and characterize the files coming from the server and separate that those are from the users you know in if the server was not adding its funds that such a way

**00:31:28**  that actually made the subset-sum problem harder then you know then it might just be completely useless for for the server to its own funds and it you know it would have the kind of privacy effect that is the worst case scenario where you convince the users that they have all this privacy but it does nothing to actually deter the attackers in the future you know and since the blockchain is an indelible piece of

**00:31:59**  forensic evidence that just gets easier to analyze it for time that's kind of a it's kind of a big deal in my opinion all right so guys what do you have let me organize my notes start talking first of you're part of the Bitcoin privacy initiative as well as block tell me about what you do in both of those roles just a bit more yeah sure so

**00:32:32**  the the two are completely separate the Bitcoin open privacy project was something that we started back in maybe 2014-2015 and it really it's me and you know I had full of other folks who I was in touch with and we were interesting in you know promoting Bitcoin privacy and coming up with some standards you know so one of the products that we have for example we call like the top threats to Bitcoin privacy and it's modeled after

**00:33:04**  the the a wasp top ten for for web applications and you know it's this very famous application security reference guide that gets updated here and there so that's that was sort of the idea that we had for the organization was a kind of open source you know nonprofit kind of organization to to to look at privacy and to try and promote it through streaming where necessary and the shaming element came

**00:33:35**  in the form of occasionally putting out some reports where we tried to come up with something semi objective criteria for privacy in different wallets and really try to highlight some of the the deficits that were that were out there to make it clear to people you know what they're giving up and help them make a little bit better decisions as far as consumers kind of go you know entirely separate from that I have also been working as a security engineer for blocked and calm I joined somewhere in late 2014 so it was a bit after this

**00:34:10**  research was when it was after I had been working on this research and published the Advisory so and you know they did I didn't necessarily come on board specifically because of this advisory but if I was doing various things in Bitcoin and privacy and security and so that's when I started working there as a security engineer okay that's awesome so how do you feel

**00:34:44**  that blockchain wallet is he's aligned to your privacy principles that you hold how does that just Square dad great question so when the open Bitcoin privacy project looked at wallets in the past the overall the blockchain wallets and this it's been a few years since we've really updated that mostly cuz there haven't been really exciting improvements to to

**00:35:18**  to observe in Bitcoin privacy but um back when we first our last report blockchain wallet didn't really stand out in the pack among competitors I think that as a company the privacy of users you know it's it's important to them but you know again from a potentially legal perspective and just

**00:35:49**  looking at the the demand from users there's not that many users who are really really excited passionate about privacy focused software in Bitcoin yet I hope that's something that will change in the future but I don't think there's a huge market for that yet and so the I think the lack of demand and some of the other concerns around these technologies have made it such that you know blockchain comm has not been trying to push the forefront of the stuff

**00:36:20**  necessarily as it did previously you know I think shared coin was an earnest attempt to really they were they were one of the first coin join pieces of software out there came out pretty soon like this is clearly something that Ben was passionate about and started working on very soon after coin jam was announced as an idea and I think that just the demand and and stuff hasn't really made it a priority for the company overall so I wouldn't I wouldn't say that my

**00:36:51**  relationship with the company is primarily motivated by you know privacy related stuff just just a quick note here that from the paper in a sample of 20,000 consecutive transactions across 45 Brooks in the blockchain 2.6 percent of the transactions fit the profile of shared coin transactions this small sample constitutes only of seven hours

**00:37:22**  of Bitcoin transactions from March 27 2014 2.6 percent and I think you identified these transactions like almost probably almost hundred percent certainty like it comes from work chain info that's for sure and it has a bunch of inputs and bunch of outputs which is very rare that that kind of thing is happening or or like never yeah there may have been some false positives with

**00:37:54**  like mining pools and mining pool payouts and gambling transaction payouts and stuff like that that you know either we're using blockchain comm info time API to kinda broadcast the transactions or you know sometimes it was just happenstance that it happened to kind of get early on broadcasted through blockchain and characterized that way so there's there's some false positives

**00:38:25**  than there very likely but just to give a rough estimate say probably easily it'll be tonight percent of those transactions that would be an accurate characterization now you might be tempted to say well a 2.6 percent of transactions that seems like a lot of volume but keep in mind that the volume at that time was a good deal lower than what we've experienced since then on the Bitcoin blockchain so you know all that might seem like a

**00:38:56**  lot of users it's it's actually not a huge bail hmm yeah make make sense although it is a huge amount because whenever I said whenever you sent a shared coin transaction there was a bunch of people to join with you in that half an hour and I'm I don't know if we could even do that with wasabi I'm I think we couldn't

**00:39:29**  so that's that's a that's a it's a very decent amount so to say also one more note that shared coin had a very compared to shared Kohinoor the privacy tycoon later coming on to bitcoin is kind of like ux step back in a sense that's a yeah sure coin may have been it

**00:40:01**  may still have be out of all the possible clients i've implemented coin joint technology it may have been the most popular by number of users or volume which is sad to say because it's quite ancient now but that's that's really possible anyway what do you guys have well do you guys I can ask questions indefinitely if anyone else wants to ask please cut me off okay

**00:40:38**  Christophe one thing that's a bit confusing is the sort of lack of consensus about the legal status of something like a coin join at wasabi were pretty convinced and we have a good legal team that thinks about this we're pretty convinced that coin joint isn't Oh violating any laws and that it couldn't

**00:41:09**  be considered to violate any laws I'm just curious as to why you think there is this disc Lera T you know it's a completely non custodial thing which means you're talking about privacy software interacting with other privacy software doing what the protocol allows it to do you know arguably the Lightning Network is is more custodial and has similar privacy features and

**00:41:40**  participants helping others achieve that privacy so what why why are we seeing all this confusion I'm certainly no lawyer but I have talked to lawyers very active in this space and I think it's a little naive and I've made this what L characterized as a mistake before is that it's a little naive to think about in terms of like well what in this particular snapshot in time is legal versus not legal you know there's a lot

**00:42:12**  of different jurisdictions out there laws can change over time and I think people who are high up in the the Bitcoin ecosystem who are doing things like interacting interfacing directly with regulators at you know major conferences and stuff like that they don't just think about you know what's what's gonna show the legal opinion right now but what's the general attitude towards regulators towards the the industry as a whole and that that fall is almost more under the heading of

**00:42:42**  politics and I think this is this is something that maybe people don't have a lot of insight into because it doesn't get discussed publicly is there people out there who are who are lawyers but they are having conversations with regulators and horse-trading you know as far as what kinds of features can can be gotten away with and what's what's going to darken the attitude of regulators towards cryptocurrency if you think about the natural

**00:43:13**  geopolitical tensions between cryptocurrency and regulators politician governments as a whole it's kind of miraculous that there hasn't been more of a crackdown than there already has right and I think part of the explanation for that is that people in these kinds of backroom situations have been conservative and careful about making decisions in that space so if

**00:43:44**  there's some cup if there's some big company I don't I don't want to pick on blockchain in particular but take any large company in the space that has you know a lot of users has a lot of volume on blockchains has a lot of assets under management and you know a lot of funding and a lot to lose by being shut down on right that that is very different you you that's a very different place to be in than say

**00:44:16**  you know a relatively small project and I think a lot of the being a kind of privacy Bitcoin privacy wallets out there would polyfill amount more under that heading than the mega companies that are out there and it's just it's a different experience does that answer your question Esther yeah that's a very good response I definitely didn't think about it in that light because it would

**00:44:47**  seem incredibly hard to believe that some company is forced to shut down because of coin join but I I appreciate that they might be shut down for other reasons where coin joint played a role in the decision and the and swayed people to that so um yeah the the shutdown thing is like yeah obviously that's the worst that's the worst case the worst case scenario is like all of your executives get arrested inside to

**00:45:17**  celebrate theythey can shut down and underseas and stuff like that there's so many negative things that can happen and there's so much backroom stuff that can happen you know the interface between companies and regulators that you know and I think it's it's not that helpful to think it in that cut that kind of binary way like do I want to put this feature out there or will I get you down right and it's it's it's me a lot more nuanced by that I think there's a lot of people who you know they see these regulators as these kind of like

**00:45:49**  sharks swimming through the ocean and they say oh well you know he hasn't eaten this guy in that guy and he hasn't eaten me I look good all the risks that I'm taking mean this truck hasn't me it's like Jackies you're you're a little sardine right he's the you're not either that guy snack for him so it's it's it's surprisingly complicated and I was not privy to a lot of that sort before kind of getting more involved in the industry [Music] all right I think my last question is

**00:46:23**  insignificant so I'm not going to ask so questions three two one what do you guys have do you have something or should we should we wrap it up I have no questions it's pretty clear to me okay anyway I'm going to ask my last question so in the paper you talked about Bitcoin s X as one of the first clients to implement Co

**00:46:54**  enjoin do you remember that yeah what what was that what was the story behind it you know if I recall correctly Bitcoin s X was like um it was a pretty simple simple little GUI client that did this kind of coin joint stuff that was very naive it was very restrictive about what kind of transactions what kind of inputs could be involved that were allowed

**00:47:27**  probably had like an IRC back-end or something like that was severely something that some so much tape together I also remember that shortly after it was announced there were like a aware fakes going around right it and so forth so people really you know pissed about having coins stolen from you no malicious copies of it back in the Wild West of Bitcoin yeah I don't I don't

**00:47:58**  recall whether SX ended up being part of some what somehow related to dark wallet if any of those guys were involved in SX I seem to recall there may have been some relationship there but I can't I can't see that for sure thank you and that concludes our episode for today Thank You Krista I really appreciate that you come and it was it was I think this is the first time we talked it was nice nice view here yeah thank you so

**00:48:32**  much for having us it's a pleasure to talk to you guys I'm excited to you I haven't had a chance to check out your past episodes yep and I'm gonna go through the the archive and looks like it's a really good study group and just so you know um as far as shared coin goes I'm still working a little bit in this area again one of my side projects that I'm gonna finish eventually is doing a more thorough job of fingerprinting these transactions trying to quantify them and I'd like to see how some of these were modern

**00:49:04**  analysis tools like Boltzmann fair against some of these transactions and what we can kind of what we can find out from there it's a it's a very good that you brought up Watchmen because so I even asked everyone should boatsman me the next one or do you want again a voting for for the next is boys month fine with everyone yeah

**00:49:38**  Boltzmann is fine but we're not able to get the authors on correct I don't know we are going to ask so we'll see okay alright so increased oh yeah if you want to come next week then it's going to be both one it's a it's more fun to to look through the paper when there is a talk on the end of the week HUS hit them then alone alright

**00:50:10**  alright cool thank you guys Christophe view you want to maybe ask something or or or do you do you feel there is something you did not have the chance to say I think I said everything if you guys have any feedback about my participation in the in the chat giving a giving you an

**00:50:41**  overview of the research I found happy to hear any feedback that you have about that or things that you'd like to see me research more in the future anything in that area alright then thank you guys like subscribe and for that three people who got to the end of this video congratulations now you know more about Cohen joins to Dooku then you know before so thank you and have a good day

**00:51:15**  and good night everyone bye-bye take a bow thanks crystal you

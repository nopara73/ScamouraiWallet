# Wasabi Research Club #1 - Knapsack Mixing with Felix Maurer

- Playlist index: 1
- YouTube ID: `XDCQI7hrB58`
- Video: <https://www.youtube.com/watch?v=XDCQI7hrB58>
- Duration: 1:28:54
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  so we're talking about knapsack coin joins today I'm just going to run through this slide and then hopefully Felix will jump in to clarify questions as they come or if I make a mistake so yeah this is the paper anonymous cordial transaction with arbitrary values we have one of the author's with us the PowerPoint this PowerPoint will be of made available if anyone wants it very

**00:00:30**  straightforward so what's the problem in Bitcoin transactions are public transactions point to previous transactions in a sort of directed acyclic graph and transactions can leak future spending that's that's that's the problem we're trying to obfuscate the transaction graph so a simple idea from 2013 or even earlier is just joining transactions so suppose you have two transactions on the left here we have

**00:01:02**  two transactions with two inputs and two outputs 1 output is likely sending money somewhere and another output is change we could simply do is we could take transactions and we could just essentially collapse them together so there's nothing in Bitcoin that bars us from doing this currently at the moment and yeah so how does this look like on our left we have two unique transactions by two individuals and I've highlighted

**00:01:33**  it in red the output that likely represents sending funds to a third party or to others to someone else and on the right what we do is we just take those inputs and outputs and we merge them into a single transaction now when we look at this from the outside we have to ask ourselves is it possible to to unravel the previous transaction that we the two sub transactions we merge

**00:02:03**  together so we can start by taking an output like this one here valued at fifty and we can try to find inputs that exactly match the value of the sum of the outputs so in this case we try these two and it turns out there's no way we could come up with an output on the right that would match the two inputs on the left and we try again and we find that yes actually we can break this transaction down into two

**00:02:35**  pieces once again because we see that the bottom two inputs in the bottom two outputs equal exactly 64 and the top two inputs and two outputs exactly equal 33 we're excluding transaction fees in this model for simplicity and so essentially what happens is we take this this single transaction and we split it into two once again and we're left with the same privacy that we would have had before we did any of this joining so this isn't

**00:03:07**  very good so most of the time we'll be able to unravel these transactions so if we if we look at the work done by in this paper what they've done is they formalize some some basic ideas so you know transactions have inputs outputs and values inputs you know we have the input set the output set and then we have coins which belong either to the inputs or the outputs and then a very basic rule which is that the sum of the inputs must equal the sum of the outputs

**00:03:38**  for any subset can we create so according to a transaction consists of sub transactions and there must be at least one way of partitioning all inputs and outputs so that each sub set of inputs is exactly one corresponding sub set of outputs with which it forms a sub transactions and essentially what this means is that if we take a transaction we must be able to cut it up in such a way just like we did before we're a subset of the inputs matches some subset

**00:04:09**  of the outputs in terms of value and we call this mapping as it Maps inputs to outputs so we have a set of all partitions denoted Phi of a set and then the set of all inputs set of all outputs and the set of all mappings is again and essentially the set of all mappings below here is just the set of all I think it's by jected mappings of inputs to outputs of the superset such

**00:04:40**  that the sum of the inputs equals a sign of the outputs so again this is just saying that we can take a transaction and and create a list of all possible ways we could cut it up essentially figuring out different ways we could we could get some transactions and the entire list of all ways we could cut it up is denoted him I hope I haven't lost anyone so far but a good idea to maybe pause and ask did have I lost anyone so

**00:05:10**  far no I think it's it's a great introduction I just want to say for some administration that since Felix appeared in this in this conversation back on Felix is one of the author of the paper and I think after your presentation we could move on to pick his brain and in order to not waste his time too much and and and then after that we can move on

**00:05:40**  to other people's presentations and ideas and discussions about that yeah so this is pretty much it almost over I think we're probably two-thirds of the way through so well will will to ask Felix questions directly so yeah now moving on to results so yeah in simpler terms we want to be able to break down transactions into sub transactions a combination of inputs and

**00:06:13**  outputs in the paper they they clarify between derived and non derived sub transactions what that means is that a non derived sub transaction is is some transaction that isn't composed of smaller sub transactions inside of it and we're only concerned with non direct sub transactions for simplicity so so the way that we look at anonymity or privacy in this model is we essentially take a transaction which has all these

**00:06:44**  inputs outputs and it has all these mappings all the possible ways we could cut up the transaction and we essentially say that a specific coin on the left-hand side and any other coin on the right-hand side or on the left hand side is linked is linked to that coin in a probability probabilistic way depending on how many mappings of the total mappings there are how many of them include the two coins being in the same sub transaction so I think there's

**00:07:15**  no way an easier way to think about this here it is formalized in the paper but non intuitively it makes a lot of sense and I think we'll see an example of it in just the next slide but that's the idea it's a probabilistic framework so in this case here if we go back and recreate what we did and we split these up into two sub transactions yeah we would say that for example output 3 is

**00:07:46**  directly linked to input 3 with a hundred percent probability because there's only one way to partition this coin join and output 3 appears with input 3 a hundred percent of the time and we'll see later how that can that can be done differently so in the paper they essentially create or create a bunch of random transactions and then essentially purposefully combine them

**00:08:18**  together and then observe the time it takes to to recreate the sub transactions from the couple transaction solely you know here we see that in the orange you know if you have five sub transactions I believe it's yeah so five sub transactions with with four inputs each that it takes about a second for a computer to be able to unravel that in

**00:08:50**  that coin joining to it's relevant sub transactions and then we notice here that the number of non derived mappings isn't very high even as there are you know as many as you know four or five sub transactions because when we did in the first example we can typically unravel coin joints and have a very

**00:09:21**  little overlap in terms of other other ways we could map inputs and outputs so the in here we see that only with six sub transactions and four inputs per sub transaction do we see more than just a few non derived mappings so there's a solution to this problem because right now what we see is that it doesn't take a lot of time to unpack these coin joints and when you do there are very few non derived mappings which means

**00:09:52**  there's very little ambiguity in terms of what's linked so could we crease this well you know here's a knapsack mixing that is is how to optimize filling a knapsack with various things of different weights in this case we're trying to optimize the way to have output so that they fill given inputs so the algorithm is pretty simple the idea is to compare the two output sets and to essentially try to break

**00:10:23**  down one of the outputs so that one of the values of the output is that the difference between the two sets so in this case the number 31 is the difference between the green and the orange and so here we've done it with you can see that we've split up the 50 into 31 19 and on right we've recombined them to make a single coin joy transaction and now when we try to figure out the sub

**00:10:55**  transactions we actually get two sub transactions we get this one here which connects the two on the left with the three on the right but we also get this sub transaction here and so the result is that if you asked for example this oh one linked with I three the answer is that there's a 50-50 chance that oh one in I three are linked because of the two sub transactions that we have in half of them oh one and I three are not linked

**00:11:26**  and the other half they are the dialouge you or you lost me

**00:12:46**  to have a probability of one we match with another input or another outplay yeah right so the left graph shows the number of pairs of inputs and outputs that are linked with probability one and the right one shows the number of input input pairs that are linked with the probability of one always depending on which knapsack mixing every when you've used so I think in the paper I had two different versions of the collapse like

**00:13:18**  mixing algorithm one which I called input mixing and one output mixing and I think I even hinted at a third one that I came up with later in the in the time when I was writing the paper so this one even improved over what you see in the Kraft so far okay well very cool so I think the important things you know here is that we still have a problem where

**00:13:49**  some inputs are connected with other inputs and some inputs are connected with other outputs so we don't have a perfect we have some points that are hard are achieving no additional and anima d except for the computational complexity that it takes to unravel the the coin joint so this is pretty much the ends here there's some anonymity here in the computational complexity that's required to to figure out how to

**00:14:22**  break down these coin joins especially if we start talking about you know ten participants 30 participants 50 participants there's still a link between the inputs and outputs the entire sub transaction petition must be known in order to apply the algorithm this is the most important trade-off I think is that currently from what I've read it seems that this can be done in a net trustless way where someone isn't coordinating all the transactions yeah

**00:14:53**  and that's exactly the third algorithm I came up with I will have to read my own work again to understand what I did because it's or I think two years now that I was working on it but I had a third version of the algorithm which was working without knowing all the outputs so for each everybody knows needs to know all the inputs but each participant only needs to know his own outputs okay so would it be everybody just needs to know all the

**00:15:30**  inputs okay so interesting so upper bound and nobody it's you know like if we look at this way of looking at transaction anonymity and we applied to zero link we see that zero link is like a perfect knapsack coin joint so that sort of provides us the upper bound anonymity which is essentially the number of total participants that are doing this this knapsack coin joint a lot of things here

**00:16:04**  and I think this is your your last slide so can I come back to it later and discuss everything every concluding thought one by one sure sure so yeah only to Felix because that's pretty much deal have you seen the paper Thank You Aviv it's it's a nice introduction to get everyone catch up with the paper and we can go into the

**00:16:36**  details here and there I was thinking that if Felix appears then we would we would start with some questions to Felix and then we would continue with the if anyone has some small presentations then then we would continue with those and then we would end up with discussions questions what did we not understood in

**00:17:07**  the in the paper although this could be bring-bring here right now because felix is still here so and we would finally discuss some some things like like if you have any ideas that came to your mind with this paper and then we would envy dirties and we deciding on what should be the next

**00:17:37**  paper on next week so let's start with let's start with some some more more fun things Felix I I would like to to know what was the story behind that knapsack paper how did you come work we work on it and yeah I can you tell us about it yeah of course actually it started as my master thesis so more or less when the

**00:18:10**  most of the content of the paper is also my master thesis I opened it a bit of yeah more of the related work which was also a big part of my thesis and some some of the results have not been part of my thesis but more or less the idea and the general yeah most of the work is basically my math assist master thesis so after I finished the thesis I was I

**00:18:41**  wrote and paper based on it and I think the one interesting thing is also that the knapsack the trunk knapsack for this mixing is not it's not my my idea it was I picked up the idea from two papers which yeah basically in one or two sentence describe that something like this could be done but did not really go into it so yeah this is how I came up

**00:19:13**  with this idea or why I started working on this idea and did you follow up on writing the paper or what are you what did you move on to no actually I started after my thesis I started doing a PhD at the RW th in authen but after year after one year I realized that it's not the right environment for me so I moved on and I'm

**00:19:46**  now working at and faunal for Institute which is not at all related to what I've done before so unfortunately since two years I'm not working on the topic at all anymore I see anyone has any general questions I I have more more in topic questions now hi well I would like to know about the test the validation of

**00:20:18**  these policies if you have published the the source code for this paper yes actually I have I have published the code that I was used to produce the result of the paper I'm not sure if it's linked anywhere but I it's a public repository on jade lab let me paste the

**00:20:50**  link for you thank you it's great thank you most of the difficulties I I encountered is the deciphering the pseudo code yeah no the I was just looking into the code everything's there the in it's written in rust I don't know if you have experience with rust but it should be

**00:21:21**  readable for anybody using who is used to imperative languages and I think the interesting part is on the main in the main source for the distribution dot RS file in there are the the different mixing algorithms that I used yeah Thank You Lucas your root code for it - and

**00:21:51**  actually I brought code for it - perfect so we can we can validate I have one last question that all you can answer is that on the paper at the end you wrote that however currently our output splitting algorithm requires knowledge of all sub transactions using it in a peer-to-peer network would likely leak information to

**00:22:21**  all participants we are already researching a new output splitting algorithm that mitigates this problem yes this is exactly the third mixing algorithm that I developed mostly at the end of writing the paper so it is not part of the paper anymore unfortunately it was finished shortly after the paper let me see it's in the code it's this line

**00:22:57**  basically the idea is that you broadcast to all participants all the inputs well you can also do that in a fashion that you don't know the which input belongs to which participant and then you can split your own outputs based on all the inputs that you that you've seen without telling anybody all the outputs yeah

**00:23:28**  that sorry where are you sharing the links in the hangouts chat I saved them okay thank you so that that was all my questions that only Felix students were any anyone has any questions to Felix

**00:24:07**  okay me I go again and about the two things first I was playing with the concept for a while and what I do is I sort the outputs descending by amount just to it's just an especial case right and I use two outputs one is the payment

**00:24:39**  another is the change and I realized that in this scheme with this modification well I don't know if is with this modification only but it creates for example 1.5 outputs for each original output for example if I have a two participant conjoint with four outputs it creates

**00:25:12**  six outputs if I have three participants with two outputs I mean six outputs in total it creates nine outputs and that I don't know if you have some comment about this but go us to to know how many participants I are in that culture is it that I'm doing something wrong or or is just because I'm sorting the their

**00:25:43**  outputs or or well I can answer my question just by by calling a bit more but I don't know if it's something that you can share with us about that no that's actually an aspect that I didn't look into one other aspect that I did not look into is answering the question whether looking at multiple knapsack mix

**00:26:14**  the coins and transactions would allow you to then again establish stronger links between inputs and outputs so this is something I would I would look into okay and my second question is about the feet because in the paper you don't analyze the fee you say basically that the fee are some kind of noise right so you cannot match the partitions by

**00:26:47**  equality because they the input the sum of the input and the sum of the outputs are not equal so it will be a bit harder to to define the transactions but what I was playing with this concept and I don't know if you have some idea about what's the the best way to handle the

**00:27:18**  the the defeat because if the participant use the same fee right that is for example pretty common in for example in in in wasabi right and then you know I was actually trying to create this transactions is ethanol is a son on wasabi transactions and it's such it's really bad which is we can go up to one

**00:27:50**  person plus mine and he's unreliable interesting well yes well what I mean is that if if the coordinator one coordinator that is coordinating this knapsack transaction right if everybody uses the same fee right even the inputs that are bigger

**00:28:22**  than the outputs so they pay more more fee if they pay proportional to the to their transactions then yeah that gives us a clue about I mean I can find the sub transactions right the partitions and and check if the if the if the fee paid matches the same

**00:28:59**  transaction or not so I it is an strong clue for the for the chain analyzer so do you have Felix any idea how to handle this what can we do an idea actually no I my I to analyze it I implemented an algorithm which it

**00:29:30**  enumerates all the possible sub sub assets of the inputs and outputs and tries to match them so you know I think I know and I don't know I don't remember how I did it but is spirited speeded it up with an bloom filter and I'm I realized that implementing a fast algorithm is should probably intuitively be more difficult if the sums did not

**00:30:01**  match so and my thinking was that maybe it does not make the mathematical problem harder but it makes it much harder to implement an efficient algorithm to actually find all the possible mappings all the possible partitions yeah that's clear because I'm suffering with that problem it is it is really hard because you say okay it has to match it is have to in a in a range

**00:30:31**  right it has to okay if it is more or less this value so yes it's a pain in the ass but and my mic and you cannot use and you cannot use a bloom filter of course so you have to keep it in memory what is what is even worse but the question was about how to how can we

**00:31:02**  make the make the the participants pay a fee in such a way that it doesn't provide additional information to the chain analyzer I'm I'm not sure whether it actually provides additional information I would have to think about it because it would only provide more information if it would help you

**00:31:33**  distinguish between subsets that are more likely the real or mappings that are more likely the real mappings than others right agree that it doesn't provide additional information it makes it even harder to to do the the analysis and I I did the analysis with the precision and the only real difficulty

**00:32:05**  with the tunnel is how do you set the precision and what I realized for Norma Cohen joins you can set the precision as the mining fee because the mining fee is the maximum amount one participant can pay with joint market transactions it's mining fee plus random I I don't know what what it should be random whatever the the going market transaction agreement was on the fees

**00:32:39**  that the taker pays for the makers on massabi it's a mining fee plus 1% and that produces a bunch of reliability unreliability of course so so yeah it it's I don't see how it would provide more information now it does it provides more information in fact I mean if you for example you

**00:33:10**  know that the the fear rate is I don't know one yes and you have all this noise or know the explain it what does it mean one okay a once at a shipper right if the fill rate is once at provide for example so and you use you will see that the you can take all the the partitions right and say okay this this the some of

**00:33:43**  these inputs yes - the some of these outputs gives you the feel right so that fee given the the size of the transaction you know how much it paid a what is there you don't know right Sophie you don't know who pay the fee there are many participants it could be that only one participant beta fee it could be that all of them played

**00:34:15**  together yes well in that case if only one pay the fee okay yes it makes sense but in that case also also is is a problem because you can say okay if it match exactly yes then this is one of those that didn't pay anything - exactly but if the sum is the sum of the input and the zone of the outputs then you can say

**00:34:47**  that this participant did not pay anything why wife yes who say that there are many other sub mappings there could be possible even if you found one that that all the dark like that if if you find other methods that that those are just as likely as that your first I think I understand what you mean Lucas

**00:35:18**  so if all the participants pay exactly the same fee and we have one mapping where all the input and the difference between the inputs and the outputs met exactly matches this fee then we would assume that this must be the true mapping but I'm not sure whether there would only be one such mapping well yes but in the in the runs that I think may

**00:35:52**  I found a lot of mappings but some mappings have have only two inputs right and other mappings have 6 inputs yes but if if I know that they pay 1 Satoshi per byte and the fee page was next I don't know yes so I mean I can know which of those mappings is the real one because one will be paying exactly one

**00:36:24**  Satoshi provide and the other one will be paying a lot less because they have a lot more inputs so it's a more is a bigger sub transaction so I know that sub transaction cannot be the real one because it's paying the less than and expected things so you mean when you have multiple mappings and then the difference between the inputs and

**00:36:57**  outputs of sub transactions should be proportional to the number of inputs and outputs and then you would know that it's likely the snapping yes exactly exactly yeah it could be I mean obviously I have to add this is more or less an empirical analysis it's not

**00:37:30**  really yeah a mathematical proof of this concept so I think the idea is really good and I think it would work combined because of the reason that it's it's likely infeasible to find out which mapping is correct and also difficult to actually find the mappings once the transactions get big enough but it's not

**00:38:00**  yeah it's not provably correct or provably anonymous in in a more strict sense I guess okay when one more question just kind curious and your analysis how many sub transactions inputs/outputs did you did you use I mean did you try with bigger with a bigger number of

**00:38:32**  participants with more inputs and more outputs than those in the in the paper actually no and the reason was that the the time it took to to find the mappings would just grew too much and I didn't it didn't run on on my workstation I had a bit bigger server with lots or lots of RAM and multiple cores I think 64 cores

**00:39:02**  not obviously you could have a really much bigger yeah a bigger computing the computer or server or server farm yeah for hours for us it was really the case that it became just too difficult to find all the or not not difficult but it took too much time to find all the mappings yes I know I try with a participant that yes with sub

**00:39:33**  transactions and it was running all all the day and didn't finish so I like can selected in the process yeah okay thank you and if my analysis of the theoretically theoretical complexity is not completely wrong then yeah it's I think it the computing time it takes depending on the inputs and output really increases by a

**00:40:07**  lot when you increase the inputs and output side I have it here but I it's not written down in a in an easy in easy way I think to ^ n times n where n is the which n is set of size n are you talking about the bare number or your lower bound estimation my lower bound

**00:40:41**  estimation well yeah it's I think it makes sense what I've read on the internet on Wikipedia that the best best algorithms known for subset sum so for solving subset sum is still exponential yeah so I think if you would I mean in

**00:41:13**  the the sizes of the of this mixed transactions in the paper I think should be only in an Academical setting if you have if you can automate it and the idea was you can join an arbitrary and transactions because the the sum or the value of the inputs doesn't matter it doesn't need to be a fixed amount for each input and then you can create for

**00:41:44**  each transaction that you do you can create with other peers for each transaction in such a corner and transactional of a huge size if enough people use the same wallet at the same time yes we are going into it I'd like to a an idea of mind at one of the most frequent question in wasabi was that why why do we have the hundred anonymity

**00:42:14**  certain and like that but and and the reason is because I sent out the emails and that seemed like them on census data okay that that should be fine the pond'rous participant but your lower bound estimation could actually give us a mathematic formula to to set a minimum participants right for for any Cohen joins okay you you you kind of need at

**00:42:47**  least this many participants in order to make he in order to reach this computational tour nests in deciphering the Eco in joins does that make sense guys I think the theoretical bound is difficult to translate in and concrete amount of time it needs to find the

**00:43:18**  partitioning it all it but it really it's only really good for explaining how fast it gets more complex or how fast the time increases that you need to find a partition depending on the number of people who participate it's not a perfect fit but the main problem is that there must be enough

**00:43:49**  Virtue's them of what's the minimum number of participants that we want to do and that that's why I saw this this formula your your lower bound estimation would be actually somewhat useful in in deciding on that number that we kind of truth that they arbitrarily or with it educated guesses I them yes I guess you

**00:44:20**  could based on the time it takes for some simple examples you could extrapolate using that function for more complex cases with more participants with more inputs to take part all right but one more thing I remember in the in the in the paper you said that if you spend that one of those outputs in

**00:44:53**  another knapsack transaction yes the difficulty could be similar to the one I mean the problem of finding all the the mappings is across different across a chain of not sub transactions the difficulty also increases similar to the to the process of mining block 1

**00:45:25**  mining a chain of blocks right do you have any additional numbers about that because I agree intuitively that that is true but do you have any numbers above that have you tried that no no sorry that's something I didn't try and I'd like to add that intuitive I think that the difficulty or the the problem would be that if enough people

**00:45:59**  would use this kind of transactions and you had would have a continuous flow of these transactions which could create kind of a backlog of coins and transactions that you need to part to to find the mappings for which is what I mean by it the complexity increases when you have when you use it continuously on the other hand linking for example two outputs together it could actually be

**00:46:29**  more easy if they both appear again as inputs in at the next corner and transactions that is one of the one of the open questions one of the open problems okay thank you one would like to chime in it not talked yet

**00:47:00**  I only have a couple of basic maybe a little bit stupid questions but are you guys intending this knapsack going join as a method of like payment for like straight-up - father for example on some service or it's like basic coin joint like it's the output will come to me the both outputs like like for for

**00:47:37**  payments whereas the zero link currently does coin joins as the as mixing transactions this is actually the question I want to ask Felix was you know if he if he knows anything about how wasabi it currently works and you know the the the distinction between a coin joint for mixing that in a coin joint for sending and I feel like have you read this paper I feel like what's

**00:48:08**  not me being able to send in a coin showing might might open doors for more gratis II yet to be honest I didn't know about wasabi until now because I really I'm not keeping up with the current developments on Bitcoin anymore or other other cryptocurrencies but yeah what was my my idea was that actually that's the

**00:48:39**  point of the collapse like mixing that you can use coins on strength content transactions for actually performing it transactions that you want to do not only for anonymizing coins so you can in the same step send coins to a third party and do the mixing okay thanks one one comment just it is easy for us

**00:49:12**  if we one day decided to implement something like this it is easy because if you mix to yourself you can generate all the addresses that you need because you know your keys right and you can generate your own keys as many as you want but for payments you need to be able to generate addresses for someone else many addresses probably by show more than and the payment and the change

**00:49:42**  you need to be able to generate more addresses so it is not hard to do I think but it is something that it's not so easy with with the existing culture let's say because if I want to pay you aviv i ask you for one address imagine I say ok Aviv I want to pay you send send me ten of your addresses it is not it is

**00:50:14**  unusual right so we need something different yes I agree there are solutions for that like stat addresses or give me an onion your onion nodes onion address and we can we could maybe work it out but it's it's a lot of work yes however maybe it's possible to do a

**00:50:47**  variation of nutsack where you where you kind of keep the keep the payment as as as it is but you are only mixing on the changes it would be an easy easier thing actually I'm quite sure I've read about special kinds of Bitcoin addresses where you can for the receiver of the transaction generate as many addresses as you want and I don't remember

**00:51:21**  was it was kind of like a public/private key scheme where you can generate new addresses and only the receiver was able to use these addresses I guess the only remaining problem would for the receiver to notice transactions which are which contain addresses that belong to him but I will try to find out what they were called it's okay I know to both of dancing has some very serious trade-offs

**00:51:52**  say if it's one of them or if it's not then I would like to investigate one is that addresses the other one the esthetic rest is you were actually mentioning that in the paper and the other one is payment codes is it one of it I'm not sure I thought it was something with blind signatures that that would be actually awesome maybe

**00:52:22**  maybe I'm remembers remembering something wrong but I can try to type try to lube it up and try to find what I was reading but I thought that that might not be a problem and anyway I just like to say that these conversations I

**00:52:52**  would really like to to make these these as a learning conversations and not necessarily how to integrate it or implement it into a severe or had to do anything with asabi because there are like 600 more papers that I want to review and maybe at the end when when everything is we learned about everything that we can you can come up with something something and then we can use different techniques from different

**00:53:24**  papers what what I but my thinking is right now is that it's just a vogue idea but if we could figure out if we could figure out scaling quality if we could make if we could give a number to hey we mix this way and this mix is this

**00:53:57**  efficient if we could kill the efficiency of the mix if we could tell how efficient one mixes then we could come up with a bunch of mixing solutions and we would know that hey this this mixing solution give the back best blockchain space per unanimity gained number right and what what would be the

**00:54:27**  unanimity gained but what is this knapsack paper is is doing pretty bad that it is I was always thinking about just breaking the link with how much anonymity said but this nut sack paper pointed me that hey you actually can break the link between the inputs you can break the link between the outputs and of course you can break the link between inputs and outputs so that that that makes the the the anonymity gained

**00:55:01**  metric and much better so that's that's great all right do you guys have any presentations with presentations here so I guess at that point I'm going to leave because it's already quite light here the address in the paper is not my it's

**00:55:34**  not a valid email address anymore I don't receive emails on that address anymore but if you have any questions you can contact me at any time I send you my new email address in the chat so feel free to ask me if you have any more questions yeah thank thanks a lot for for coming it was a pleasure - yeah thanks for having me it's nice it's always nice to see that you've done something interesting yes I'm a big fan

**00:56:08**  of your work Thanks so thanks and goodbye maybe until sometime later all right bye bye yeah I was thinking about could you leave showed your presentation again yeah just give me one quick SEC here yeah do you have a slide in mind yeah

**00:56:43**  could you go on the one where is the inputs and outputs like yeah for for example this case what determines the actual numbers of the outputs let's say that if this wasn't for payments where there is a exact number or some required what deterrents these outputs or their value of them yeah so so the idea is you would get a more efficient knapsack mix

**00:57:14**  if you just allowed for infinite outputs because they would get very small and then it would take more time to compute but there's the trade-off that you don't want to have lots of outputs so the simple knapsack idea here was just take regular transactions that have no special features and for every two transaction take the larger one the one with the larger output and break down a large output into two parts where in

**00:57:45**  this case the number 31 is the difference between with your and before orange-brown values so in this knapsack method you all you only add one output for every two transactions that that combined yeah okay I'm back yeah yes sorry I lost

**00:58:25**  connection okay what I want to show you is yes quality with openness with you okay

**00:58:55**  three two pants I don't know if he's going to her the number of okay well just going back to

**00:59:27**  the previous presentation thing I was just thinking about you know if it wasn't for payments and there would be like any kind of set amount that you would have to reach on as output I understand that we wouldn't like to like use too many or break it down into too many UT exo's but in like in some sense I think it could kind of work I'm not sure if it's just too expensive or

**00:59:58**  something for after why it's like combining all these UT exo's or something like that but you know like breaking it down onto the small as possible out input that there is and you know not maybe like like the smallest one but you know just breaking it down into smaller and exact the same outputs you know like you could combine many inputs and the P would go like a

**01:00:30**  statically depending on how many inputs you put in and then it would just you know give you either like for example a bigger sum or a smaller something could be like different kind of connects arcs going joints I'm not sure if I'm explaining this correctly do you guys get any any of that I think I understand what you're saying there's some there's some problems with that idea as well I

**01:01:01**  mean inefficiency is one of them but their issue that I see with these knapsack examples is we don't think about how transactions look like over over a longer period of time so for example let's say you have many many many change outputs if you decide to then spend many of these change outputs together in a transaction down the road it undos all of the privacy gains from the knapsack for the most part so I

**01:01:35**  think I think those are those are one concern is there something else you wanted to say yeah I'm not sure I mean I just thought about this thing right now so maybe I have to just sit down and think about a little bit more before I I'll try to like verbalize it but well another thing was that about mappings

**01:02:08**  and the computation of that I mean is that actually necessary for wasabi to do or is it like just beneficial thing if it would take too much time for actually go down on all these mappings I mean let's say that there would be like let's say five participants which all are putting like three different inputs and yeah for example getting the well X amount of outputs I'm not sure if it's

**01:02:40**  only a good thing if the mapping is hard to calculate my mapping is not necessary to do in order to be a system it's a but but what's interesting about calculating these mappings is that we can actually see that where are the bottlenecks of block chain analysis companies so that's that's I am interested in calculating

**01:03:11**  the mappings yeah that's what I was thinking also I mean if we could just use it as a benefit yeah back back to the for example the idea that I said before that Felix actually estimated the lower lower bound for for the subset-sum analysis here and we could say that hey

**01:03:42**  okay we need at least this many inputs and outputs and if if 10 I think 10 is pretty let's say if if 10 inputs and outputs are present then that already provides computational privacy so we could set a lower bound for okay yeah we want to target 10 as the minimum number of participants or something like that

**01:04:12**  so that's that's interesting idea can I add something before I have to run here it seems like a lot of privacy benefits would come from having so so it's right now we've split the mixing and the sending is two separate features

**01:04:43**  but it seems like a privacy would be much stronger if people that weren't doing mixing could still participate you know asabi transaction it's just something that I thought about I'm not sure I understand sorry yeah I mean so why that there would be like more people

**01:05:20**  linked to the coin joints even if they don't actually use wasabi yeah is that what if a user just wanted to send someone money and essentially wanted to participate in these knapsack type coin joints for for spending then that could be a separate service that can be added to wasabi right like

**01:05:56**  imagine if the entire blockchain didn't have transactions but just had lists of inputs and outputs I think we can agree that it would be Kahn occasionally very hard for people to successfully unravel the entire block of inputs and outputs so I think that's sort of what I was thinking about yeah yes of course it's an even if you don't

**01:06:30**  do any mixing right more problems there are read let's say how do you how do you get over the participants of a block agree on the field and I the it raises more questions than it answers I think one more thing transactions because Aviv

**01:07:06**  is leaving before we leaves can we decide on what what should be our next what should be next Monday what should we be looking to you guys have ideas coughing all right coin shuffle an idea there are some

**01:07:42**  papers that were cited by Felix's paper that I thought were interesting but I think coin shuffle was one of them Queen James from crystal vodkas you know anonymizing the world with human form she actually enjoyed in mind also

**01:08:21**  although secure multi-party computation these which came up in the paper but I've seen that came up so many times in so many papers in the coin shuffle paper to by the way that I'm just as interested but the heck that we so anyway any more ideas or decide on these three now or or both let let's vote on

**01:08:52**  for these three or or something else in the mix do you want word I prefer gone shuffle and there is an another variant the adult I don't remember is if it is gone shuffle blasts blasts or something like that there is there is coin shuffle plus press and there is value shava which is coin shuffle plus plus with confidential

**01:09:23**  transactions so anyway let's go from left to right aviv when you shuffle coin joins to Doku secure multi-party computation okay Lucas coin shuffle igor probably yes or yes also green jangsu Doku but I think is is pretty much the

**01:09:55**  same that we have discussing today I find in the the partitions so I don't know if it brings something new to us yeah that was kind of my idea there that we could we could look at someone has his work on the same topic that's actually a part of the knapsack paper and we could we could compare that my idea so oh there is also sneaker oh it's

**01:10:32**  knickers - yeah it's knickers can be true yeah probably sneakers is better that ventia for because playing traffic hazard some some communication is key studies is pretty hard I don't know if it can be implemented really so yeah okay let's start it again then and I will note how much are the boots on and let's get to wear it so we shuffled is from in roughing and

**01:11:07**  it's about mixing transactions it's similar to zero link in that sense Cohen joins to Doku is from vista fat loss' and it is how do you do non mi Schoen Joyce I think it's solving the subset-sum problem this is this is a small acting secure multi-party computation I have no idea what is this but I think it's it's it's something that we are come back

**01:11:37**  because it came back many times sneaker is from Adam Gibson and this is a this is Co enjoying some some interesting idea to do Cohen joins okay Aviv Cohen Schaffer Cohen joins Sudoku secure multi-party computation sneaker you can vote for multiple things I think the question for the sneaker will be interesting okay punish of on boot sneaker on vote

**01:12:10**  because the sneakers monogram yes Nick or I cannot hear you

**01:12:42**  and couldn't couldn't hit anything I'm gonna head out I can see your judgment to vote and I'll read whatever is submitted for next week

**01:13:14**  perfect see your beef thank you Cheers thanks thanks an awesome presentation thanks guys thank you all right deeper into what I don't give some does in this topic because I know the men and yeah I'm

**01:13:45**  really curious what he's doing especially with regards to what you guys are researching so yeah I won't never secrets alright and the naming is yeah yeah I like the idea of shuffle and sneakers everyone is sanitary probably yeah yeah

**01:14:18**  yeah yeah are you with us okay I see what you wrote you're not familiar with any of all right well is it very matter what I wrote is going to be sneaker because that has four vote and okay so it's going to be snicker than next X meeting and Lucas you were saying something that I disrupted you so go ahead

**01:14:49**  yeah it's just a comment that those snaps are instructions for an observer an external observer it is not easy to to realize it is a con job because I mean can be a Buch construction a pay up pay too many transactions I mean in the blockchain there are lots and lots and lots of transactions with more than I don't know five inputs and then outputs

**01:15:23**  there are not gonna join right so and so it is not it is not easy to to know that that's a conjoined transaction so there is not a clear finger freedom so you have to do analyze the transaction and then you say hey this transaction has a lot of ambiguity so it has to be current on transaction but otherwise is is it's

**01:15:54**  not easy and ok you know you say ok this is a control transaction and not such transaction who who has created that section or how many participant this has so this this is not so easy for example in another way I disagree completely because there are just so many fingerprints in the blood that you can tell exactly which

**01:16:26**  fall has created that transaction by just dropping at and lock time let's say you know yes yes yes sir it is possible but anyway if you for example cannot know so easily how many participants are in wasabi this easy because if you count how many equal outputs are if there are

**01:16:58**  66 equal outputs then there are 66 participants in this case is a bit harder so it's it's something to have in mind by the way if I can ask a weird question then what did you mean were no para about being able to know which while it created the transaction by the end locks aren't that different wallets are using

**01:17:31**  different fees different and lock times they either use it or not or they either use a specific number they might bump the transaction eibar to do err bf you see there is a set of features those features sometimes have like run on uh let's say the fee you have to decide what fee you will do in the transaction and if that fee that

**01:18:05**  exact fee that transaction is being made with can only be produced with the read electron-electron is a bad example because the electron Bitcoin core and Wasabi's kind of can produce each other's fees but if that can only be produced with the electron then then it's going to be a transaction with the electron okay so now we figured out that this is a transaction with electron now

**01:18:36**  we have to just apply our hell ristic that what is the likelihood that this electron is going to create a page to endpoint transaction so so that's what I'm saying that there are so many metadata in the transactions that you can probably tell what wallet created it okay yeah thanks for clarifying that I

**01:19:08**  was fighting a lot against it previously but I just realized it's it's it not possible to divide anything because there is always something and if I may ask another stupid question is what exactly is analog time and I mean I think I've heard about it but I just don't remember anything or what

**01:19:42**  does it like conclude is when that transaction can be mine basically you say okay this transaction can be mine right now can be mine after this vlog hi so basically that's all we sell fail in the transaction where you specify when that transaction can be mine okay yeah all

**01:20:14**  right Thanks for for example a Bitcoin core and electrum are using an N log time that is in order to discourage fist knifing which whatever it is it's not on top of my mind but you know like things like this or the RBF that's right if you send the transaction and you have RBF

**01:20:45**  neighborhood then only that information that this transaction can do RBF just okay now look at which wallets can do RBF and it must be it's probably from those wallets now if you do an RPF transaction if you bump the feet then oh that's a lot more information to expose because you can only bump the fee from

**01:21:17**  removing the change then you just exposed where you are sending the money which would be exposed by the transaction chain anyway later on but you just exposed at that point where you are sending the money and if the fee bump has such a specific number that okay let's say Bitcoin corresponds the fee with this number or with this period then then you can you can further narrow

**01:21:50**  the range of possible wallets that can can can do that so it gets really really bad okay yeah I think I got it and with RBF you like exposed which one of the addresses or outputs are like the actual change yes right that might be the most obvious one I didn't even have this for a very long time but then things just start to click you know okay yeah okay good to know

**01:22:27**  all right I have a question you said about the paper that about that had information about confidential assets and mixing or something like that you mentioned it like five minutes ago yes I was explained yeah I was explaining the history of of coin

**01:22:58**  shuffle it started with coin surfer then they they came up with a new protocol that does not require the word that's called ice mix and they incorporated it into coin shuffle and they called it coin shuffle plus plus and then they figured out how to do coin shuffle with confidential transactions and that is called while you shuffle okay send me a

**01:23:30**  reference think or something on that I am already done to go in it but it could be a bit faster and more helpful just Google values of beta Malaysia are you interested in question four plus plus well I'm interested in mixing and

**01:24:00**  confidential assets involvement in that because it is well I want to know if there is something then I can bring 4rg yeah that's but something that we could review later oh okay well that could be the topic that I might be prepared for so yeah thanks for explaining that again oh my

**01:24:30**  good yeah bring it to next episode and review see I think there is some some interesting things to learn from me too I checked it give you a vote for that thank you yeah thanks alright do you guys have anything else

**01:25:05**  my homework yeah me too all right then next next episode is going to be speaker and yeah thank thanks for coming and I I feel I will publish it I don't know where if the recording is good I will publish it probably the wasabi China and and and we see like what what are you

**01:25:39**  thoughts about how was this so far did you enjoy it do you have any recommendations out to or to improve these conversations at least read the obvious presentation was pretty damn good in my opinion I mean like a short recap of what was what and what's the point of knapsack so it makes a pretty good like yeah just a video in itself but of

**01:26:10**  course also these talks to you know I I was kind of afraid that Felix are going is going to leave we have to grab Felix at the beginning because he's gonna leave there definitely yes from my my point to feel the participation of Felix was great and so if for sneakers we can't have the

**01:26:43**  if we can't have Adam here it could be great too I will ask him I can't can't promise feelings didn't promise it to either he he said he be a try so that's why I didn't even sent out at meet or anything hey Felix is going to be here because if he's not anyway I will tell

**01:27:14**  Adam to to come yeah definitely I I hope he can yeah yeah I think this format was very good when on the on one hand you had person within the team who introduced the brief recap of the article and then on the other hand he had the actual author of the article that could like country but online and fix mistakes misunderstandings son

**01:27:44**  everything and also knowing that he's not working anymore look Felix is not working in a war for example for on this topic is also available because you kind of understand where it goes and what questions he can cover and which questions probably should be covered by someone else so yeah head and author of paper mister bit here and of course the discussion afterwards as always just marvelous alright guys so if no one has anything

**01:28:17**  then thank you all for coming and if this is published and you're listening it on youtube or something then definitely everything everything that we talked about the paper Felix's code or code everything is going to be in the description so you can follow up and maybe change the world by why are you getting some ideas alright thank you guys thank you alright

**01:28:52**  why

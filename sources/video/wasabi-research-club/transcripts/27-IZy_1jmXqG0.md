# Wasabi Research Club #27 - Privacy Guarantees Of Wasabi Wallet 2.0

- Playlist index: 27
- YouTube ID: `IZy_1jmXqG0`
- Video: <https://www.youtube.com/watch?v=IZy_1jmXqG0>
- Duration: 1:52:52
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  oh in the middle uh well hello and welcome to wasabi research club number i don't know well today we will be 37 right today i'm talking 27 okay today we will be talking about uh amount organization in coinjoin transactions so that is all about sub transactions

**00:00:30**  and input to output mapping and the knobsack paper this goes all the way back to wasabi research club number one where we covered the knobs paper in detail and today we will kind of rehash all the things that we learned in the meantime and hopefully uh figure out some interesting ways of how to use this in wasabi 2.0 so to start this out with you well what do you think why is this an important question to talk about in the first place

**00:01:03**  uh yeah so basically in the like when we started talking about coinjoins um we i mean i wasn't around back then but like everybody was kind of assuming um at first uh there would be equal amounts uh and then uh we discovered uh when that um you know when you when you relax that assumption which is already should

**00:01:34**  should look a little bit fishy uh actually in practice um it it's uh even worse than people expected uh so we're going to look at the paper in in a bit more detail look at some of their simulation results and we can kind of begin to to to maybe quantify under their assumptions their modeling assumptions um like just how good or bad it is uh but it's i mean even though the assumptions are maybe not so realistic

**00:02:06**  it's uh it's still very instructive and of course there's the famous shared coin story um so um [Music] conservative implementations have have gone for equal amount outputs uh joint market wasabi samurai they all kind of apply this approach and the knapsack paper showed how you can in certain cases uh you can make payments from coin

**00:02:37**  joints where the linkage between the payment amount and the inputs um is is made more more ambiguous more private but it's it's designed with that specific use case uh in mind and um there's some limitations in the proposed algorithms there's also is issues with how it handles the change so it's it's like it's not a complete story um the the thing that they propose

**00:03:09**  in the paper but i think actually the paper's main contribution is the model that they use to analyze um the performance of their algorithms so this model is uh quite precise it's um i think it describes the privacy problem in a very general and very powerful way and it's uh general enough to take into account um uh equal amounts or um uh arbitrary amounts

**00:03:41**  uh and yeah the goal for today is kind of establish a baseline for um like how how do you understand uh how do you analyze situations with this model um and how how can we uh generalize it a little bit more so that it uh works uh like in a real setting with fees and stuff like that which was not uh taken into account in the paper that's that's basically the goal

**00:04:11**  um okay let me i'm gonna share my screen and hand it back to max or rafe which one of you wants to go i think one one thing to highlight is that in wasabi we kind of took the easy way of just using the standard amount denominations and one of the reasons for that was because the charmian blind signature coin join algorithm

**00:04:43**  that at the cryptographic layer only provide privacy guarantees if all participants have standard denomination outputs right so there was a limitation of standard denomination outputs already on the cryptographic layer so we just stuck with that and only guarantee privacy for those standard denominations but that of course leaves the problem of multiple denominations and change and all of that stuff uh and the crucial difference and why we bring

**00:05:13**  this topic up now again is because with wabi-sabi on the cryptographic layer we no longer have a privacy leak with uh equal or with the amount of denominations so we have privacy guarantees on the protocol layer even for not standard denominations just regular payment amounts and that that means we can now actually experiment and go for a more optimal solution that hopefully also enables the payments inside the coin joint which would be

**00:05:45**  best so unless anyone else has a note you will give us an overview okay so i guess i'll go um okay so i think i already gave most of the overview um i guess one thing that's um [Music]

**00:06:17**  like the the next logical step is to go through um okay what what how much of bitcoin do you need to understand to kind of follow through this conversation um so like bitcoin has a very complicated system there's the network layer there's the cryptography there's uh so uh most of that uh we don't really need for today uh we might mentioning it mention it in passing but we can uh kind of pretend uh that it's just a giant spreadsheet

**00:06:50**  that magically works in in the right way and there's no consensus problem and um like the there's no bitcoin script it's just like some magic like there's a an owner column in in our spreadsheet and uh uh based on the owner column um like that's the system somehow magically guarantees that all authorized transactions are allowed to be made so i've made a small

**00:07:21**  visual aid let me see if i can find the url [Music] um okay so we can uh uh kind of imagine at genesis time like maybe this row didn't exist there was just this one coin uh so what a point for our purposes today uh it's something that uh comes into existence at a specific transaction and we're just gonna number those or whatever we don't even care

**00:07:51**  about transaction ids uh it's got an amount um [Music] and uh again it's it's got some sort of owner field which is you know just abstracting away all the details of bitcoin script and we also put down the transaction number in which it was so uh the way mining works uh for our purposes is every several minutes on on average every 10 minutes or so a new coin magically appears and one of the miners uh appears in this column

**00:08:22**  um and we kind of like this is pseudonymous here right like we don't really know who who did this we can only presume um okay so uh looking at some of uh bitcoin's uh real history there we go uh i think that's a bit more reasonable so i put in some of the first uh transactions from the like the actual bitcoin

**00:08:54**  blockchain uh it's the genesis block uh this is like the first coinbase transaction uh and this is transaction number nine which uh famously was used uh uh how finney described uh in a bitcoin uh talk post um how uh he was the recipient of the the first uh transaction um here i think so um we can kind of use this as a way to like

**00:09:25**  really understand what like what are the implications of of the way that the blockchain is structured by by looking at this uh in terms of the coins so uh if transaction number nine here created a coin um and uh later we see that transaction number 171 which we know based on the forum post like 10 of which went to hal and 40 of which went to satoshi or we presume it

**00:09:56**  went to satoshi uh this is also how we know that this coin belonged to satoshi and uh just to be clear what the colors denote here uh it's just the the groupings of the outputs of an individual transaction so it's it's the same color coding is here um [Music] so um we can look at the the how things continue right if we look at satoshi's output or satoshi's presumed output uh this is a transaction that was

**00:10:26**  confirmed in block uh 181 uh and it has um another 10 bitcoin output and a 30 bitcoin output now now here we already like we don't really know uh what was going on we we can no longer interpret these numbers um in as clear a way but obviously like as we start filling in more and more information about this column and and start you know making

**00:10:57**  connections between these columns uh like i hope it's self evident even to somebody who doesn't really understand how the coin works uh on a technical level um that there's a sort of paper trail being recorded um okay so um yeah uh i think that more or less covers it so um [Music] yeah that's that's our model for today

**00:11:29**  um and um uh yeah i think at this point i wanna uh ask uh rayford or max is going to take over and uh uh like lets us through the the next sections and uh um uh because because uh i'm uh i don't want to like just take over and and speak into into the void

**00:12:18**  yeah i mean like i i really don't have like anything yet on my mind about this i was reading through your notes and yeah i didn't get to the end of it but yeah i mean it all makes sense at least for now we're uh we don't we're not supposed to make it to the end i think today uh but like basically um like uh like we're at this section here so um

**00:12:48**  uh i guess uh please tell me where to scroll and kind of like uh like talked before the thing like make it a performance for for the youtube i think one thing to consider next is uh what transaction privacy and transaction surveillance this is about so how in your simplified model how do you look at these two things

**00:13:20**  um yep uh so like should i do you wanna like poke through the example some more or do you wanna like go through the notes step by step or uh like the the reason i'm struggling and the reason i asked for help uh before is is basically um i've i've been like too immersed in this stuff and um i have a difficult time not jumping ahead so in order to make this more accessible to

**00:13:51**  a general audience like i need help from from youtube so let's let's take for example uh just the consolidation of multiple coins in a transaction how does that look in your model okay so we can just invent an example here uh let's just copy uh or we can do this on this

**00:14:23**  third ticket yes okay so how out um so let's say satoshi did something else uh and the first thing uh was i don't know mine another coin so that would look something like this i guess uh and for now this would also be unspent um sorry this is bugging me oh they are um so now satoshi has two coins

**00:14:58**  so transaction three uh might be uh consolidating them into a single one and in the same operation the number three would be indicated here and these rows would be marked unspendable so i don't know we can cross them out or something so that that would be a consolidation okay so here on the spreadsheet right if you want to generate a coin you write on

**00:15:30**  the the left side the number of the funding transaction and the amount of the output of that transaction into the owner is and then when you want to make a spending transaction uh you choose which currently unspent coin is as suitable so you do that by checking unspent in the d column and then writing the number of transaction there which is in

**00:16:01**  our case three and that denotes the inputs of this transaction um while then in column b and row five the amount is 100 so that's the oh the output amount of this transaction uh it's the sum of the two inputs consolidated 50 plus 50. yes and if we want to do the opposite suppose uh now 75 needs to be sent

**00:16:31**  somewhere uh right or maybe uh we can just show what would have happened if satoshi would have needed to spend 75 so there would be another output of transaction three here for the remainder the remain uh remainder i cannot spell yes so here we have a transaction spending two inputs

**00:17:02**  and in line three and line four and creating two outputs in line five and line six column b exactly and i guess we can now show okay let's imagine that this was uh a payment sent to somebody and this was the change so what does it look like if uh satoshi then makes another payment

**00:17:32**  um so maybe it would be something like this transaction 4 sends uh 15 to something else third person and then so this is also unspent for now but in order to do this this coin no longer belongs to satoshi so has to be this one so let's mark that and then this also has a a change output

**00:18:03**  and like as we can see there's it's not directly obvious that this payment and this payment can be linked somehow but if we follow uh the transaction numbers we can we can see uh how everything kind of hooks up and can be threaded together okay so this is helpful for us in a privacy analysis

**00:18:34**  because we can basically easily check whichever number of the funding transaction equals the number of the spending transaction and that just means there's some linkage in the in these two transactions yes and and that's precisely what we call the transaction graph right so uh in mathematics a graph or a network is a set of vertices or points or nodes

**00:19:06**  uh which are connected by edges uh there's a few ways of thinking of uh like formally modeling the transaction graph as a graph it's maybe a little tricky but like um maybe the simplest way is you can think of uh coins individual outputs as uh nodes on the graph and they connect with edges to uh different nodes that are transaction notes that they kind of bind together

**00:19:37**  stuff and then new coin nodes come out of uh transaction nodes so like that that's uh called a bipartite graph and i think that's the first way in which the the bitcoin graph was the bitcoin transaction graph was kind of visualized in the in the very first papers

**00:20:07**  and there's of course this common input ownership hiristic granted that's an assumption that if there are multiple coins being spent in the input of a transaction that these belong to the same person now does your simplified way of looking at things does that help us with that assumption um i mean so the like this heuristic uh so just for a bit of

**00:20:39**  history uh like this both heuristics were kind of implied in the paper as was the address reuse constraints so address reuse in this case has to do with how we fill in this column so we've kind of ignored that detail which was uh very important especially in the early ages but the uh like the the heuristics here so um let's look at this number right like why

**00:21:10**  do we assume that the 75 went to somebody else and the 25 is what went to satoshi well that's because if the 25 was the payment amount then why would you have needed to use two coins to make that payment um so these heuristics um i mean they uh directly apply to um to to our model today uh it's only the address reuse issue that's kind of uh

**00:21:41**  abstracted over okay and so then where do joints come into play um okay so uh do you wanna have a have a crackhead explaining or

**00:22:12**  sure so i guess the gist of it is is the bitcoin or coin joints are collaborative bitcoin transactions and so that multiple users come together and provide multiple inputs to a single transaction so this just by definition breaks this common input ownership heuristic which says that all inputs of a transaction belong only to one user but with a coin join by definitions there are many users owning each some

**00:22:42**  coins in this large collaborative transaction and they also control many outputs i don't think that that's in the definition of coinjoin i think the coin joint definition is solely on the consolidation of inputs with many users um and in theory you could have a coin joint with one output you know paying one entity that would be like a batch payment of many users to one service provider for example

**00:23:12**  but more likely each of these users is going to pay either to different merchants or to himself right so a mix to yourself and in both of these use cases then we have multiple users controlling the inputs and multiple users controlling the outputs and yeah the question is now is this an obvious break of this assumption uh of the common input ownership heuristic um

**00:23:42**  which in the case of previous wasabi 1.0 conjoints and probably also wasabi 2.0 coin choice coin joints this is not the case so an outside observer can can tell that it's very likely that this transaction was created by multiple users and not just by one whereas for example pay joins are a type of coin join where only two users consolidate their their points in a way that it's arguably difficult to find out that this is in fact two people consolidating their coins and many would

**00:24:14**  assume that it's one person i think those were excellent points um anybody else have anything to add um okay so um thinking about how we analyze uh just to start

**00:24:44**  simple uh equal amount coin joints um so we there's a a bit of a nuance here which is that we want to separate the discussion between what happens inside of a transaction and what happens like between transactions uh with regards to anonymity so in order to kind of um analyze this uh

**00:25:15**  problem with with different like theoretical tools um like focusing in on kind of where it all begins uh uh like we um let's talk about the how equal amount coin joints can kind of exist in a uh in in a wider mix um so uh like the the problem with coin joints uh scaling naively is that

**00:25:47**  the queen transactions are size limited so there's uh uh a hundred thousand virtual bytes uh or 400 000 weight units and there's a a few bytes of overhead but other than that it's all uh like just the inputs and outputs and um if you look at it naively um this would suggest so at uh like

**00:26:18**  roughly 100 bytes for a single input and a single output we would be limited to about a thousand uh input output pairs in kind of uh a mixie coin joint transaction that everybody has the same denomination going in everybody has the same denomination going out maybe the input denomination and the opposite denomination are not the same uh but like that's kind of the the theoretical scaling maximum of like how how big an anonymity set can you create in a single bitcoin transaction

**00:26:50**  uh and this seems quite limited so um uh yeah uh anybody want to like uh talk a little about a little bit about uh the intuitions for um like how uh anonymity sets can uh uh like spread uh across transactions uh and uh inherit between coins i mean just uh in a simply way uh

**00:27:22**  like yeah you have a limited set of anonymity that you can gain from a one transaction but whenever you can like uh connect these different uh for example like coin joint transactions you might be able to get much more anonymity for your coins because of the like yeah interoperability of these different rounds and just to highlight that because block space is limited and transaction size is

**00:27:54**  limited there is a natural bound to how large the anonymity sites can get and that means that we need to carefully allocate the scarce resource especially if you want to provide a high quality service of controlling coordination then everyone will favor to be in a high quality coordinated coin join that is well optimized and privacy preserving in all regards um of course that's assuming that there is

**00:28:26**  high demand for block space and that we actually need to allocate that resource carefully but i guess in any polish case scenario for bitcoin that's that's gonna be the case so that's what we're building for maybe just as an example like uh even if you get for example like and i think it's just a general trend that we tend to optimize for block efficiency even at quite a cost

**00:28:56**  yeah and like if for example you have only like hundred percent participants in a coin joint round uh yeah you have like anonymity set hundred if yeah if they all have like an equal output uh denomination but if for example 50 of them goes on and mix in another round with 50 new different participants the original ones who liked 50 who didn't mix they also will benefit for the other 50 who did remix so it kind of like connects these two

**00:29:27**  rounds and like it just multiplies the anonymity set whenever you can like connect these different rounds yes and in the ideal case instead of 50 users going into one round and 50 users going into another round which would uh be very slow growth rate ideally every user would go into a separate round if they're going to remix that would be the the quickest way in which this uh kind of additive sorry

**00:29:58**  multiplicative effect uh so from from the point of view of an individual coin or an individual allocation of funds uh tracing through the mixing graph um the direct uh anonymity set accumulation is additive right every transaction there's a number of other inputs and outputs that may be interchangeable with your input or your output from this transaction and if you keep going well

**00:30:30**  now your your coin that's already a little bit private uh becomes an input into the next one and and create creates a new coin uh which has a higher score so that's that's an additive process but if you uh estimate how good it could get in the best case uh well maybe there's a uh an exponentially growing number of uh past coins kind of in your history uh and like rafe said um uh an exponentially growing and

**00:31:01**  unbounded uh number of uh coins uh possibly in your uh future history uh in like a potential future history like a history that is not actually true something that some other user did but which uh you have plausible deniability right now it could have been your coin that went into that mix and therefore for all anybody knows you could be still mixing until this day kinda um

**00:31:32**  and uh i think greg maxwell already described in the bitcoin talk post um kind of what's what's the optimal structure for this so uh this comes from uh like network uh theory uh uh communications stuff so um if we have uh like in in kind of the the base case uh just this uh four user transaction

**00:32:02**  uh four inputs going in for outputs going out and we compare it with this uh graph of four uh two input two output transactions uh again with the same idealization that there's no fees or anything yet so um hopefully it's it's kind of obvious that these two graphs are uh equivalent um and if you try and scale this to higher numbers and try and uh minimize the total number of edges or

**00:32:32**  the total number of transactions or the like the total number of uh inputs or outputs per transaction every one of these parameters uh affect things uh a little bit differently uh and in general uh like this is oh wait i'm in dark mode so this is gonna be ugly but um the wikipedia page on uh interconnection networks uh and switching networks uh shows uh a few classic examples and i think the one uh

**00:33:03**  maxwell was describing is the class network which is i think always three stages yeah and um okay so so if you're able to plan like in in advance you could make rounds of potentially as many users as would fit in a block or even several blocks uh like you don't need to do an equal amount coinjoin only in the space of a single transaction uh in order to

**00:33:33**  benefit from the same kind of approach to privacy this is what samurai does with uh their whirlpool stuff um like they have five participant coin joints where two of the inputs pay for the fees and the three of the inputs are outputs from previous transactions and all of the outputs are identical so then they try and build a transaction graph where

**00:34:03**  because of this homogeneity on both sides uh right or partial homogeneity on both sides of the transaction and complete homogeneity on the output side um you you kind of uh get large privacy sets sorry large anonymity sets uh even if the individual transactions are not very large uh whereas wasabi takes a uh currently takes a little bit of a different approach okay so

**00:34:34**  i hope it's obvious this doesn't really um work with uh uh unless you have this uh standardization of the amounts right like if the standardization is different between transactions um or uh right you you you can still standardize uh like wasabi does today um there's a denomination for the round and everybody in that round uses that denomination but

**00:35:05**  uh the way it relates to the denomination of other rounds is um it slowly varies over time uh decreasing slightly so that uh users can mix without consolidating with new coins uh even though in reality we have to account for the fees um [Music] okay so um yeah uh anybody want to talk about like how does this break down uh when when

**00:35:37**  you start dealing with uh arbitrary amounts um i mean i think yeah like by kind of like using the or like applying the knapsackiness to the the output amounts you can at least hide something in there uh like you can have multiple different denominations already in that way but you're jumping

**00:36:08**  ahead oh okay uh so like uh basically um [Music] what i'm kind of going for is uh because transactions are quite large but not that large if you start allowing i mean there's uh between uh one satoshi and 10 bitcoin there's a billion different possible values

**00:36:39**  and uh if you can only have up to a thousand inputs and outputs under the like the most constrained situation so in reality only up to several hundreds of inputs and probably every user is going to have several inputs and several outputs and right that there's all these things that that kind of make it look like um maybe even in the average case there will still be for for most values

**00:37:10**  there will be sufficient privacy if you do nothing to kind of uh control the amounts but um if if like if you don't make an effort to open up this interconnection between transactions um it's not really going to happen on its own uh it's going to happen to to kind of a limited extent so and the kind of the good news is if you do give it an opportunity

**00:37:41**  uh well network theory kind of tells you that you don't you don't need very much right in a community graph so if you like kind of uh look at all the different owners of the coins as nodes on a graph and whether or not they've mixed with each other is uh like the the connectivity of this um typically in community networks you have a strongly connected component that

**00:38:11**  almost everybody on the graph is uh hooked up to and uh through that everybody can reach everybody else and um what you need for for that to happen say in a randomly constructed graph is just to control the no degree and make it high enough for us we're working in a slightly different setting because like we don't really have a community graph we have a transaction graph which um uh kind of evolves differently over time

**00:38:42**  um but still the um the logic of if you make sure that there's an opportunity and at least some of the time you kind of um build in a structure that's kind of like this then uh even if it's only two inputs in and two inputs out but you have this like ever expanding uh right if if two standard denomination inputs for

**00:39:14**  each transaction are coming in from a coin join and two uh are going into a coin join uh maybe there's more maybe there's additional denominations or or even just one and and one uh right uh uh as long as there's at least one other identical coin that maybe doesn't come from a coin join and another that maybe doesn't go to a coin joint but one of them did if this

**00:39:45**  connectivity uh is is uh happening uh just enough there's a kind of transition point where now you go from anonymity sets that scale with the size of the transaction uh or with the size of a coin's history right your mixing depth and you get anonymity sets that scale with the um like the overall size of the mix graph uh in both directions um

**00:40:18**  i think i overdid the technical uh so anyway let's move on but it's it's it's very interesting and i guess one question that i have is where is the trade-off from having many small coin joints to having one larger coin join uh like is there some point where or or how do you even measure that trade-off so maybe i'm kind of skipping ahead here

**00:40:48**  but um the the condition that i'm describing here um this is only for a single denomination and so i think the the kind of the best scale for transactions is to have them as small as possible for reliability and ux reasons so long as we are actually able to accomplish this with a high enough degree right so for the reasonable range of values the

**00:41:18**  reasonably popular denominations uh hopefully we have at least several equal amount outputs at least one of which goes into another coin transaction and better yet we have some inputs as well and if every denomination uh satisfies this then we basically have unrestricted growth of the anonymity sets of every denomination separately but because the denominations correspond with each other as um

**00:41:49**  like preferred value series or powers of a certain base um they uh naturally will lend themselves to the construction of arbitrary amounts even with a small number of representative equal amounts so this further means that the chance that an arbitrary amount input or an arbitrary amount output would be interchangeable with one of the these representatives of the uh equal groups

**00:42:21**  that would be sufficiently high that we can actually have robust anonymity for uh arbitrary values as well directly in the transaction uh this would mean that we could do safe batch payments and stuff like that um how you actually uh yeah i i mean again i'm kind of jumping ahead so like uh here below uh where we're supposed to like address exactly how it arises due to the sub transaction model um

**00:42:51**  does that uh like clear things up um like it's it's about how these two parts of the transactions relate to each other that kind of determines what is the right scale so arguably for equal amount coin joins if you can ensure that homogeneity the um the correct size is two uh and then you uh you always have like chains of pairwise transactions maybe at that point the like the unlock time inversion overhead um kind of becomes a

**00:43:23**  bit more wasteful but in principle the smaller the transaction the fewer people it it involves the higher the reliability and the better the ux um you could still even in the case of just two users as long as the mix depth is more than one on average um like you should still have a strongly connected component where uh the anonymity set is is unbounded unfortunately that can't really work because of fees but uh samurai has made it work for five users

**00:44:01**  i i guess one one additional question would be that where does the privacy come from here is it from the equal denomination or from the history of the coin in a sense that what if i have an unmixed coin and i just create a setup transaction where i generate equal denomination outputs and then later i register those self-created outputs that are standard denomination in the coin joint is there any benefit to that

**00:44:34**  there is in the sense that now there's a chance that you gain ambiguity on the input side as well like exactly the same analysis that we do here on the outside because normally we expect the input amounts to be arbitrary and it's it's only by coincidence that maybe we have equal outputs um but exactly the same analysis uh applies to both sides so uh in principle when you have equal amount inputs uh it's exactly the same kind of privacy as we have today with uh german market with

**00:45:05**  wasabi uh et cetera so um i guess um [Music] and more generally it's both right you you need both you need to have some degree of equal amount outputs inside of the transaction otherwise this inheritance doesn't even come into play right like if you don't have this local property that these two outputs are identical and these two

**00:45:36**  inputs are identical uh or or something similar to that where there's multiple ways of interpreting this data and you need some sort of external information to tell you um how to distinguish these two so if you ensure that in a certain way here at the local level then and it holds on uh different related transactions then

**00:46:07**  this means that there is an emergent uh kind of a combination of the the like the the inheritance of privacy emerges between the transactions right like we know that this input is not like this input it's better because this input could have come from either this input or this input and this input and this input are just as good each one of these contributes to prior

**00:46:39**  coins not just uh like the the interchangeability here where they enter the transaction um so um yeah you you you cannot really have inheritance without some sort of regularity at least going back into the history but if you insure it on both sides of a transaction then it can kind of grow backwards as well as forwards and the forward growing uh anonymity set

**00:47:12**  again is potentially unbounded because uh it's all the transactions are going to happen um and uh um and and yeah that this doesn't really arise unless you have uh the the basic building block of of uh fundamental ambiguity uh kind of at the bottom okay i think we've uh

**00:47:44**  um so how do we move this to the multi-sub transaction model so with multiple denominations and such no no no no no i mean this is a later step right like this is a much later step what we were talking about i mean okay so just to summarize the conversation where remixes are important and maybe the older the remix utxo is the better the connectivity of the graph is

**00:48:18**  but how do we create the transactions right that's the that's the next step that's the immediate question here yes the purpose of this discussion is basically um like it's all it's clear to us how we gain privacy here so um the point of this is to point out that the in in this structure the privacy is potentially unbounded but

**00:48:48**  uh has this kind of uh bifurcating behavior right if you go above a certain critical point then you can tap into that unbounded anonymity set but if you go below then it it doesn't it doesn't experience that multiplicative growth that uh rafe was talking about it's only uh an additive growth so um the basically the observation is that this is where the the it

**00:49:19**  it appears that the most uh robust kind of uh uh non-uh disjoint privacy right so coin swap would be even more private but if we're restricting to the um situation where um the there's still a history shared between coins then this is basically as good as we can get and um i wanted to point out that it's actually a fairly easy property to obtain

**00:49:52**  uh based on the the network theory stuff right so if we have um uh ambiguity uh in terms of equal amount outputs uh existing inside of transactions uh so this this can be a uh like this two into out can be its own standalone transaction or it can appear as part of a larger transaction um and if we have this kind of like connectivity not idealized like here but

**00:50:23**  random connectivity and all we need to do is basically make the average degree uh higher than one so as long as uh some of the time some of the users are remixing then uh we should be able to achieve that uh without doing anything more so this means we can set aside the entire discussion about interconnectivity uh and and uh re-specify it uh like in

**00:50:53**  terms of a local property so i think we actually discussed all this stuff in the notes um [Music] but yeah like the the idea is like now that we understand how everything exists outside of the like in between the transactions we can focus on the inter transaction structure and kind of take this idea that like as as a requirement for good

**00:51:24**  privacy uh we need to still use some um like equal amount coinjoins as the basic building block um and we want to have uh like that degree of uh of remixing that that would ensure uh that most coins end up on the strongly connected component of the graph

**00:51:58**  okay so how okay so for that we're let's dive into the actual sub transaction model so um i can bring up the paper um or no it's not time for that yet so um i guess let's let's through some of these uh

**00:52:28**  basic definitions for mainly for completeness so uh we're interested here in sets and multisets and we don't need the like the general uh definition for um our purposes we can just think of sets as numbers not like a general mathematical thing so it's just an unordered collection of numbers or of uh uh individual coins which we can identify with numbers right so we we can like if we want to talk about a set of coins we can just give them a numbering

**00:53:00**  and then say like this is a list of coins and when we say a set or a multiset it should be clear that this is different from a list because a list inherently has order in it whereas a set does not uh the difference between a set and a multi-set is that sets uh can only contain or not contain an element uh either something is a member or is not whereas multi-sets allow uh an element to appear multiple times so it's kind of

**00:53:32**  uh you you count uh zero or more times uh for every element or one or more times uh but multisets are still not ordered so uh lists are kind of like uh what you get when you or lists with repetition is what you get when you impose an order on a multiset and uh lists without repetition is what you get when you impose an order on a set um okay so um also just to keep things kind of um

**00:54:05**  like it might get confusing like sometimes we care about individual coins being unique right like this is coin number 43 or something and it's different than coin number 47 which is uh just after it in the blockchain or something um at other times we want to talk about coins as if they are only the number amount so this is why we need both sets and multisets right generally we're going to be thinking about

**00:54:36**  sets of unique coins or multi sets of amounts that correspond to each other um uh so this is just uh yeah uh to to hopefully keep those um cleared up uh the next concept we need is that of partition so sets can have subsets so a subset is just another set which contains some of the elements of the other set

**00:55:06**  if a is a subset of of b then for every element in a let's call it x x is also in b so we can talk about the set of all possible subsets um of uh a set and that's called the power set and we can also talk about um kind of slicing a set into

**00:55:37**  what are called disjoint subsets so these are subsets that uh don't share any elements right so in the power set there is some overlap right like if we have the set one two three uh then the set two three and the set one two um those are both subsets of one two three a partition is uh where we divide up the item so that each one goes into a unique subset called a part

**00:56:09**  so um this would be something like putting one into its own part and two and three into a separate part or maybe having uh each one of the values uh as a separate part uh or another partition is just the set itself so those are subsets and partitions of sets uh any questions so far it's kind of like i know it's it's boring and tedious but um it's the these definitions are kind of

**00:56:39**  required for uh understanding the the paper uh in detail and uh um okay so moving on what are sub transactions so um let me quickly switch to share actually um i think i'll open it in another tab that way um

**00:57:33**  okay has everybody donated to scihab okay so uh what is a sub transaction so i think they uh defined this in section four um let's read through this um

**00:58:03**  a little bit carefully so a coinjoin transaction t is i o and v so the inputs are i uh outputs are o um and there's a function assigning uh values right so these are unique coins and and they're representing with this uh v function uh a mapping from coins to their amount so that's kind of like uh

**00:58:34**  a funny way of uh of saying that that this is a unique it's a set of like unique coins uh but we also keep the kind of the multi-set view um available inside of this function okay so there's a condition here so as i say as we do not consider fees the sum value of all input coins must be equal to the sum value of all alpha coins so for every

**00:59:06**  coin in the transaction i we look at the value we add those all up together and they're they're saying that this has to be equal we know that that's not the case because um it's no longer possible to broadcast uh transactions with zero fees like hal and satoshi's transaction that we saw earlier um and we also know that this is not how the real world coin joint services actually work all three of them

**00:59:36**  utilize fees uh mining fees and coordinator fees so um or maker fees in joint markets case so uh like this is um uh yeah just bear that in mind we're gonna have to like generalize this um so um [Music] a coin joint transaction consists of sub-transactions uh each consisting of inputs and outputs right so we identify

**01:00:07**  uh by k uh the like unique part and then we have a subset of the inputs and a subset of the outputs uh which we associate with this um so uh this is a partition that's basically what they're they're saying um and um right this is the the condition here uh uh the disjointness

**01:00:37**  uh and secondly um [Music] they are saying that for every sub-transaction the sum condition must also hold so it's not just for the transaction as a whole but it's for every sub-transaction in isolation um so this uh idea of having uh a sorry sorry uh so uh a partition is a sub transaction mapping it's uh a sub transaction is a part uh

**01:01:07**  uh that that satisfies this condition a sub transaction mapping is a partition of the set of inputs and outputs of the transaction uh and and we've kind of been thinking like before i introduced uh partitions of a set whereas here they have two separate sets so let's talk about that detail uh in a little bit uh more clarity so it's not just that we're slicing the inputs and outputs into like different

**01:01:38**  groups we're slicing the inputs and outputs separately we're partitioning the inputs and outputs separately and then we're defining a mapping between every part of the input partition and every part of the output partition so also this means that the number of parts in each partition have to be the same so this is kind of a more complicated constraint it's entirely equivalent to saying like let's just think of all inputs and all outputs as a single set

**01:02:09**  and say that we need to partition things uh but every part has to have at least one input and at least one output uh that would that would be an equivalent way of defining sub transaction mappings um maybe a more intuitive one but this one is a little bit more precise and even though it seems more complicated we'll see that it's it really helps with the analysis later um is everyone with me so far

**01:02:42**  yes yeah okay so uh we know what setup transactions are we know so what sub transaction mappings are um the last kind of important thing here is uh um yeah so uh first of all they point out that there's at least one uh valid sub transaction mapping uh right because we know that there's uh uh in the trivial case like if it was a

**01:03:13**  single user transaction then there's one part uh and uh so so a trivial solution always exists and uh also we know that like bitcoin transactions are the actions of actual users that actually uh we can attribute things to them so um we we know that there's at least one true way in which even a coin joint transaction happened it's just that if the coin join is uh actually privacy preserving uh then that mapping should

**01:03:45**  not be observable to any one entity every participant in the transaction only knows about their coins and if there's any coordination uh then like they they they should not know uh either uh and join market it's a little bit different because in in that case the taker is also coordinating the transaction and the taker is the one buying the privacy so uh even though one entity does know the full mapping uh that doesn't violate the the

**01:04:15**  privacy assumptions because uh it's the the consumer of the the service in that case um okay so each coin transaction has at least one valid mapping but maybe it has more right like maybe we can uh um like let's find one of the diagrams so um this is um two ways of kind of interpreting a transaction with four inputs and four

**01:04:47**  outputs uh this is a mind you a trivial way of looking at it but like what they're saying is like here's one way of slicing up the transaction uh here's a partition on the inputs here's a partition on the outputs uh and the sum of these two parts of the input and output set correspond and the same is true for this so we can define a correspondence between the parts and uh therefore this this is a valid sub transaction mapping uh the

**01:05:18**  sums all add up and uh and here is another one uh right the the condition also holds uh because this is the trivial mapping uh so it also holds uh in this case uh so the the um the first distinction to make is that this um [Music] this trivial mapping is uh what they're calling a derived mapping of the first one so um the way that you can derive a

**01:05:52**  mapping from a non-derived mapping uh it's uh uh like think of it going bottom up as you kind of merge different pieces right let's say you have a mapping and then you blur this boundary and and combine these two parts and you get this as a result then intuitively you should see that this is not actually adding any uh additional interpretation right like this is just saying maybe the user who appears to have done this and the user who appears to have done this maybe

**01:06:22**  they're the same user but there's no additional privacy benefit from having this additional mapping in the in the transaction so basically we should only count the non-derived mappings and the non-derived mappings are the ones that you cannot break down any further um that are kind of like elementary uh so um if we count only the non-derived ones right we can imagine that we enumerate every possible

**01:06:53**  uh so uh we have a set we take the power set of the set that's already exponential uh and then we go through all the possible subsets and and we uh apply this kind of recursively so for every possible subset we say is this a valid part and then we see what items are remaining and then we do the recursively enumerate the power set and and in this way we can build partitions and then we can further constrain that the sums are all correct so

**01:07:24**  uh this is you know not computationally actually a feasible approach because it scales very poorly but in principle if you have this naive algorithm that's able to uh enumerate uh all transactions even are all different uh sub transaction mappings uh even for arbitrary little large transactions then what you can do is you can count right so if there's an input

**01:07:54**  i can look at how many um uh non-derived sub-transaction mappings uh it uh i mean it appears in all of them it must that's a condition but um i can check how many times does it co-occur with some other output and this also generalizes for input and output links and output output links which gives us this funny little poop joke

**01:08:26**  so inputs and outputs uh or inputs and inputs are linked based on how often they co-occur in sub transactions right so let's go back to the diagram and uh i mean this is the only way to kind of interpret this transaction that's how they've set up the sums so because there's only one non-derived mapping for this transaction because input one co-occurs with input two and output one co-occurs with output

**01:08:57**  two and alpha one corkers with input one and so on uh and there is no other story right there is no other sub transaction this means that the probability that input 1 and input 2 is linked or any combination of these uh um like blueish uh uh region they're deterministically linkable because there's only one way but if we were allowed to somehow interchange these right if they're the figures here were different and um i

**01:09:28**  think there's a diagram of that like two pages down uh yes okay so um here we have one non-derived mapping and another non-derived mapping for the same values and here we can see that um some of the uh inputs and outputs co-occurred differently right so uh the inputs are linked in exactly the same way in

**01:10:00**  this diagram this means that the inputs of this transaction are deterministically linked whereas the outputs like sometimes they are assigned different sub-transactions and sometimes they're assigned the same right so for output 3.1 and output 3.2 here the probability that they are linked to like output 4 output one and output two

**01:10:31**  uh or to each other or to the different inputs um that actually like already spreads out more right that's not um like a probability of one for one value but this is now something that anybody who's trying to understand is mapping number one the true mapping or is mapping number two the true mapping um they would have to uh or some derived mapping of either of these um that uh entity would have to uh obtain

**01:11:04**  uh information that is external to this transaction right like kyc information about the history of the coins or or look at the connectivity of the graph find consolidations and things like that or address reuse or some other clustering or yeah uh use network level privacy leaks but they would not be getting enough information from this transaction specifically in order to be able to tell uh

**01:11:34**  what the probabilities that a priori output for is linked to output 3.2 or something right but um notice that output 4 is always linked to input 4 for instance oh no sorry the interchange here but uh okay never mind you you can get it okay so um [Music] right that's uh [Music] okay so this is the sub transaction model um

**01:12:05**  i think that's pretty exhaustive [Music] we've talked about counterfactual ones i think the next item on the agenda is like the results from the simulations that they had here so let me just consult my notes um so uh let's jump to figure four and try and remember why i thought it was important oh right this is about the

**01:12:37**  simulation so one important thing that uh to mention is uh the way they uh model this okay so they wrote this coin joint analysis thing um and this works a little bit better than the naive explanation that i gave earlier about how you would enumerate all the sub transactions it still scales exponentially so they were only able to actually like evaluate the results for

**01:13:08**  uh fairly small simulated uh transactions but it's still very instructive and an important thing to kind of pay attention to is that they looked at the blockchain as a whole and plotted a distribution of like all the different values that actually appear so this is like a cumulative distribution i think this value must be like 0.01 or something uh like or 0.1

**01:13:38**  uh there's there's like there's another jump here and another jump here at one vtc so it's slightly biased towards round numbers but overall it's like the log scale sorry the x-axis is logarithmic and the y-axis is the cumulative distribution so we can kind of see that this is uh um a sort of logistic curve right um so uh there's um

**01:14:10**  uh unfortunately there isn't a plot of the value distribution itself but um it appears to mostly match like what we saw with the wasabi data where uh it's it's a rough bell curve with a few like uh peaks so this is what they're going into uh right this is how they're simulating transactions uh to them users get um like random values drawn from this uh distribution uh and then they have random payment

**01:14:41**  amounts uh and then uh like this creates a random sub transaction that that user would like to perform uh and the user goes on and does this in a collaborative transaction so in the most naive case uh this is uh what happens right like uh we're looking at uh three overlaid plots of uh three sub transaction four sub transaction five sub transaction transactions so we can think of this as

**01:15:13**  you know just the number of participants uh and we can see that if we randomly sample the amounts uh like it barely helps at all um uh there's uh uh um like the uh for a four participant coin joint um two of the coins managed to get some ambiguity right because there's two non-derived sub-transactions and other than that like not

**01:15:43**  not much is going on most of the coins are actually uh deterministically linkable based on this result so um this means that um and it gets harder to evaluate and even though you would expect an exponential growth curve um the question is okay well how fast and how robust is this growth as the number of participants increases when the amounts are random uh and like already at five users um

**01:16:13**  ideally we should be able to do better than this um so this is uh uh yeah fairly strong motivation okay so um figure three is the one i have on my notes next so this is also similarly overlaid this is about like how long it takes to evaluate all the different uh non-derived uh sub transactions um as a function of the number of inputs

**01:16:45**  per transaction so we have a number of curves in parallel here and you can see that the growth rate is higher when there's more sub transactions that uh the y-axis here is uh logarithmic so uh the the growth uh in the uh evaluation time which is roughly corresponds to the um the search space not it's not the same

**01:17:16**  value as here right like this is um how how big of a space do we have to search in order to find uh this result uh but like uh you can clearly see that this is an exponential growth because it's uh or even more than exponential because it's uh slightly above a straight line on a log a y log graph um okay so um

**01:17:47**  figure five is also interesting uh oh sorry no we did that one right okay so uh sorry i i skipped ahead before my bad um i thought oh we reviewed the other ones here okay

**01:18:18**  so um and i already mentioned that we'll need to relax with some conditions so here i'm out of stick with my notes so so keeping up with the other uh figures um now we have to discuss the three variants of the knapsack mixing algorithm that they proposed so the first one is uh shown in figure six

**01:18:48**  for the results of the first one no that's the diagram we already looked at uh okay so figure seven is variant one okay so what is variant one uh it's this algorithm here or it's also the the first algorithm uh yeah so um it's a little bit nuanced but what they do is they um

**01:19:19**  some coordinator like entity has perfect knowledge of everybody's inputs and outputs and also tells every user how they should split the coins right so the payment amount is fixed but every user has a change amount and this kind of uh oracle coordinator thing you know whatever it is uh here it's just simulated um what it does is it um uh it looks at the inputs and it

**01:19:52**  looks at the output in question and um tries and uh pick a random point uh right like a random way of slicing the output so that whatever amount it is it's the sum of some of the other inputs in the transaction um and this is a little bit naive but it's already like an interesting result so like very quickly we see that even for uh small sub-transactions

**01:20:23**  and even for a small number of sub-transactions right uh already at four um sorry already at uh three sub transactions we're seeing results are much better than we had before right this is already three distinct uh mappings um and um uh like this is an a log scale axis so so here for five sub transactions uh instead of the two which would have been here we're uh already up to like uh

**01:20:55**  between 20 and 30 i think like 22 or something like that so this is a substantial increase um but they have done something better which is uh in the second version they also shuffle this so the choice of like how you uh combine different inputs and outputs um uh is different for for every one of the um suggested uh cut points um so the the results uh from this one i

**01:21:27**  think are figure eight let me just double check yeah and these are the only two variants that are shown in the paper but then there's uh the important one is variant three so this also kind of works with perfect knowledge uh but by shuffling the um the values um uh it actually does a lot better um so um the what's displayed in these diagrams is the number of um

**01:21:57**  input output links between like the first variant i think and the second one uh just double check um sorry it's somewhere in the paper itself um figure nine

**01:22:29**  uh i'm blocking out sorry i don't remember i i'm pretty sure that this is the second variant um but the the important thing here is that um looking at the from the point of view of individual inputs and outputs is what we care about much more right the um this graph shows the number of non-derived mappings but um and that's a nice property for a transaction as a whole but

**01:23:00**  um we're much i or at least i'm much more interested in this purple line here which is showing how many the input input links that were deterministically uh like not deterministically linkable uh are shown by this line right so this is how many inputs

**01:23:30**  were able to sorry uh how many input output combinations um so how many different sub transactions did these inputs and outputs kind of participate in right the other lines are input inputs and outputs that are deterministically linkable to to to each other so this these lines we want to go down as we see that they go down here and this line we want to go up so that ideally none of the inputs are deterministically linkable

**01:24:02**  and none of the outputs are deterministically linkable um and if i'm not mistaken uh even though i kind of lost my place in the diagrams the results are not as good for like unless you do that shuffling uh and it's also noteworthy that felix mentioned in the first research club that the variant iii produced even better results even though they're they're not reported in the same way so what is this variant three um

**01:24:32**  this one is a lot closer to the situation that we have which is uh every user decides independently what they're going to do and they um uh they look at the other users input amounts and they shuffle them independently of each other and basically do the same thing that uh the the second variant does except in a way that we don't need multi-party computations or some trusted third party in order to

**01:25:03**  actually build a transaction the difference is nothing has perfect knowledge of the desired output amounts only the individual users have a knowledge of their own amounts but again if we take felix's word this is um this works quite well in the same simulation setting so uh what are my concerns about this uh i think this is a very good start but um yeah any anybody want to um like point

**01:25:36**  out the problems with what they're proposing and oh boy tough crowd um did i lose everybody um here okay um

**01:26:08**  okay so the issues that i see uh i guess i'll try and uh speed this up a bit uh so uh first of all this is uh uh really designed for the payment use case and it's not really clear how to use it for different use cases the second issue that i see is that this is not robust uh the the privacy of individual amounts kind of depends on what the other users do uh so they only analyzed the degree

**01:26:40**  of ambiguity um coming from the non sub transactions and they kind of ignore the uh interconnectivity uh side of of privacy here um and um although the paper kind of implies in kind of an exponentially improving security uh i think this is a bit of a misleading uh like way of of looking at it

**01:27:11**  not to fault the paper uh i don't think it actually makes a claim but um it's an interpretation that that seems to be kind of uh coming up repeatedly uh uh which is that the computational difficulty of doing this um is uh prohibitive um that's not actually the case because in multiple types of special cases you can actually do much better than this naive enumeration of sub-transactions and because

**01:27:42**  as other users are potentially hurting their privacy um their contribution uh to the transaction also gets discounted and that uh results in a an exponentially fast uh decrease in the uh in the ambiguity so um okay so i think finally uh we have a complete sort of understanding

**01:28:12**  of um of the model that they proposed uh we've talked about their algorithm and and now um maybe this is the most important thing i have to discuss today so this is this idea of uh symmetry uh between sub transactions so um what i mean by symmetry here is uh like in a mathematical sense the idea that like there's some invariant that's uh preserved uh um so um

**01:28:43**  yeah um so let's look at the simplest kind of symmetry um so we already saw um in the paper that there's like this way of making two different mappings um for some hypothetical transaction so let's ask okay well what does it take to transform between mapping number one and number two we can see that there's the number of parts is kind of the same in

**01:29:13**  both of these there's two and two uh we also see that the inputs are the same across both but what happens is that we exchange some of the outputs um and we already saw in the equal amount case um [Music] a sort of trivial example of that right like if there were equal amount outputs here well we could trivially substitute between them um for equal amounts

**01:29:44**  there's uh it scales with the number of permutations um just uh yeah kind of an interesting uh bit of trivia but um for unequal outputs um we need to do something a little bit more clever which uh what they've done here is they've exchanged these groups right so output like 19 and 14 together and

**01:30:17**  31 and uh eight and oh wait sorry what are the actual sums here so going by the inputs uh 33 and [Music] 64. um right so what what they're doing is they're exchanging multiple uh outputs for multiple inputs and and rearranging this side entirely and that that's a much more complicated transformation so this is like

**01:30:48**  a second kind of symmetry between sub transactions um so how does this one arise well the the equal amount one is obvious but this one arises when the numbers are uh like related to each other and in a nutshell what they're proposing uh in this paper is uh if you randomly sample the other user's inputs or outputs you can construct values on the output side that will lend themselves to at

**01:31:20**  least being interchangeable with those amounts that you've selected previously so if you just do this by construction once uh you randomly sample you construct your your value um you don't make any attempt to optimize um just by doing that you've already built like you've you've shown that at least one symmetry uh exists in in the transaction um so that's the uh the second kind right it's uh um

**01:31:51**  um when we exchange um uh more complicated things um uh oh i forgot another trivial uh substitution which is between parts themselves right so the uh if the parts were the same size then uh we could also exchange those uh and that's kind of the same thing as as the individual equivalent inputs or outputs the

**01:32:22**  the last thing is symmetries that kind of um don't go step wise right like so if we exchange individual equivalent outputs um like we're never breaking the dif the definition of uh a non-derived sub transaction mapping uh right we're we're preserving that throughout the process every intermediate step uh we can also talk about sequences of transformations that

**01:32:52**  maybe go through the space of derived transactions right so like to do this exchange from uh like more basic exchanges like if we think of it of moving one output at a time uh we have to break the rule uh that everything sums to roughly zero um so uh a more interesting class of of uh symmetries arises when we um like allow ourselves to to do like compound

**01:33:24**  operations that uh do a bunch of elementary substitutions and uh kind of erase the boundary between two parts and then split them differently uh because when we do that then we can sometimes create sub-transactions that are not possible to uh derive uh by transforming uh using only like uh exchanges between equal valued parts right we would be allowing ourselves to change the sums of the the parts themselves whereas when we're only substituting coins for each

**01:33:56**  other we keep the number of parts and we keep the sums of the parts the same and that's kind of a constraining uh situation so um hopefully this gives a little bit of a more concrete um uh idea of of how um how we can like if we know that there is one mapping and we know some sort of local easily optimizable property of the amounts that we pick

**01:34:27**  can we guarantee that we allow uh transformations right can we exploit the symmetry structure uh and um make it very easy to find transformations that imply the existence of a related mapping instead of going you know the top down route of uh exhaustively enumerating the search space uh if we go from the bottom up we start with what i know about

**01:34:59**  my part of this the true sub transaction mapping and how do i adjust that so that i know i'm helping to to create a sub transaction mapping which has a lot of symmetries a lot of ways of transforming it in in a very trivial uh composable stepwise way into different mappings and um yeah i think that's about as much as is

**01:35:31**  uh like as deep as i want to go in into this except perhaps to mention the the one thing which is that um if we want to evaluate this there's something curious about all of these uh symmetries which is that the the density like how easy it is to find these uh for a random transaction

**01:36:03**  that's basically something that can be estimated by how difficult subset sum is um on random subsets of a certain scale uh so like if you see that the subset sum problem which uh very briefly is you have a set of numbers or a multi-set of numbers and you want to find a set a subset of that that sums to some target value or in the optimization framing

**01:36:33**  that is as close as possible to the target value so if you take random sets let's say of size 5 or of size 20 from from a transaction and you kind of see is subset some difficult on this random set uh at some point you you find a sort of phase transition uh if it occurs it will occur at some scale uh right like uh it takes maybe 20 coins of standard denominations until on average you find

**01:37:04**  that the the you're in a the dense class of substitution problems which means that there are many solutions for the set and and [Music] we can kind of guarantee that by using standard denominations as we've uh spoken about uh before but um right like by by picking these um standard values so that they are

**01:37:36**  uh distributed exponentially with respect to the same base what we can do is increase the economy of how how difficult is it to make subsid sum difficult uh we need fewer values overall in the set if they all relate to each other in this way so this means with a relatively small number of denominations uh we're able to make subset sum relatively easy for smaller and smaller subsets and

**01:38:08**  if substitute sum is uh easy at a sufficiently small scale then this means that we have an explosion in the number of symmetries and this means that not only is there ambiguity not only are there more non-derived subtransactions than one uh also we should find that the uh uh probabilistic links are also uh low in

**01:38:38**  in those scenarios because um it's not just the the average case uh that we would be measuring uh in this but rather like we're trying to optimize the individual clients behavior uh in order that they um uh they actually like that's the thing to optimize in the online setting right you're participating in transaction right now you know what the inputs are you know what you want to do um how can you um make subset sum that much easier uh in

**01:39:12**  the in this specific context that we find ourselves in uh if everybody is doing that then collectively um we should find uh enough uh of the the equal amount um uh stuff we we should find that the equal amounts relate to each other sufficiently well that the um substitute sum is easy and uh by handling these two things together we can enjoy the benefit of the

**01:39:44**  interconnectivity graph as well as protect the right avoid deterministic links even for arbitrary amounts uh within the transaction that's how we we prevent linking of uh input coins um or try to prevent linking of input coins going into mixes and hopefully eventually how we'll be able to handle uh private payments directly from coin joints as well um yeah i think that's everything and i

**01:40:14**  like hey sorry i the exact thing i was trying not to do by reeling raef and max into this kind of sort of happened but i mean we knew what was coming right i mean yeah i think you explained pretty well so is this is this basically a proof that what we were trying with our simulations is is

**01:40:47**  uh correct even for subset sounds not only for equal amounts um i wouldn't say a proof uh but an argument but yes that that's a basic intuition it's uh um like if we do this approach uh and we there's there's still um stuff to discuss about okay how do we um uh increase the chances that that's the

**01:41:17**  optimization problem but basically yeah this is a logical defense of the approach of using standard denominations um trying to account both for the inter transaction privacy and for privacy for arbitrary amounts and trying to address some of the issues that the knapsack approach uh i think still has which is that it's um a little bit brittle right like ideally you should not just rely on one

**01:41:48**  combination of random coins of some other specific user only to protect your uh your payment amount but you should try and maximize the ambiguity across all of your output amounts and with respect to uh all of the other users not just uh one random thing but i mean that's just because the the code in the knapsack paper um makes no attempt at optimization right it's just uh uh a simple simulation so

**01:42:19**  um i think that's the the bottom line it's uh like why what is the approach that we're um we we've been gravitating towards for a while like why do we think it makes sense uh why do you think this will result in sufficient privacy uh or at least why i think that so i might be going forward too much but let's assume our

**01:42:51**  last latest multi-denomination simulation and algorithm is good enough and i think that's a fair assumption for for let's say 50 or 100 inputs but we can also see that when we go down to let's say five to ten inputs then we're not ending up with equal amounts too much

**01:43:22**  so what should be the approach to fixing that would it be to switch to a different algorithm or you think you can optimize that um enough like the main algorithm so even those cases are covered where like very few inputs are in the transaction um what we can do is uh

**01:43:54**  by so the first thing to do on top of the knapsack approach uh like how do we translate their uh simple approach into an optimization approach well instead of only randomizing one so we've randomized many times and choose between the random solutions uh and then we need some way of evaluating these but uh in transactions with a small number of users if everybody is doing that then the likelihood that they will pick uh

**01:44:26**  amounts that are more compatible with each other and still manage to obtain some privacy can become higher than if you just do this randomly even though block space efficiency would be slightly reduced in that case um so so yes this is uh um like by optimizing i think we can also take care of this kind of hopefully in edge case where we have very small transactions but also obtain more block space efficiency overall for

**01:44:57**  the same level of privacy which means like every everybody should should kind of benefit even in the large transactions as well uh if if we do this on top of just the the simple randomizing approach lukas david what's your takeaway from today's session

**01:45:33**  for me this is the first time that i was going through this in details so i think i have to go through again but at least i have a vague [Music] overview regarding this document so if i find myself in front of a problem i will

**01:46:06**  know where to look for that specific stuff so that's my takeaway yes mine is more or less the same and basically something that we have been trying to discuss but it was not the correct time is when to start mixing and what to stop mixing and

**01:46:37**  make that um or put that decision in a fitness function or a cost function that has to well have all this in mind and well and we have it it's time to start coding that by the way uh yes i've uh i've actually started

**01:47:11**  i mean the general approach is all like the jupiter notebook uh codes at least some of this in the the python but um so the the general approach is demonstrated to be workable and produces um better privacy results than we saw for the just the randomized stuff um but yeah what isn't done yet is um kind of like the interesting stuff that we can perhaps do

**01:47:41**  later about how to um so equal amount privacy that's a trivial symmetry to detect uh we can do like the the knapsack approach of uh just constructing some symmetries uh but if we want to be like really uh proper about it like we can uh apply at a later point uh like we can literally add a term for the density of the subset sum problem and i'm i've been looking at some research papers

**01:48:13**  uh that do this um and uh that there's some really interesting stuff uh so like after mainnet uh hopefully we can do this uh even better and um uh this should have a nice sort of positive sum effect where everybody would still be paying the same amount for the same block space with the same number of users like so all things uh held constant

**01:48:44**  the overall privacy uh and the degree of the interconnectivity and the robustness of interconnectivity all of that would be uh improved by uh such uh an additional term but anyway that's that's not for today or even for the next few weeks or months yeah just on a general note if you guys listen back this episode um

**01:49:17**  i think you can comfortably skip the first one and a half maybe even two hours because the first half an hour 45 minutes was basically bitcoin basics uh after that it's about um what was it while arguing that there are mixing and and remixing gold outputs is good for

**01:49:49**  privacy and well after that half an hour or 15 minutes definition and finally the the final part which everyone gets pretty tired by them probably was the uh the the most important part in terms of that's the that's the next next step but even even so uh this this is more like a theoretical

**01:50:22**  argument rather than um rather than an action of uh what to do next kind of thingy uh what i covered today yes but that's uh i mean for uh like what what i actually have uh in in terms of uh like simulations or like work in progress is uh more much more concrete than that uh

**01:50:55**  so uh but that that's also a bit of a long discussion um there's there's uh yeah we we can discuss that maybe next week if you want but um like the my main motivation in doing this is like now we have something documented where we've uh shared the thought process uh we've covered um some of the stuff that was lost in the missing part of the uh knapsack uh call and um i think we've

**01:51:28**  also hopefully given uh people kind of a complete account for for the model in in one place right like if you want to understand how we've been approaching the like um making the claim that wasabi 2. is going to be private uh like this is like you can find all of the information that we've used or at least the start points uh they're all referenced from here in a kind of self-contained way so

**01:52:01**  and i think that's a great ending of the live streaming so i suppose i'm going to to close this and well just to summarize this is this session was about making a claim why wasabi 2.2 should be sufficiently private or even probably much more than

**01:52:35**  sufficiently private in my opinion but all right so thank you everyone for joining and and have a good night bye

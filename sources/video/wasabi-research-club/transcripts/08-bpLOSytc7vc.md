# Wasabi Research Club #8 - CashFusion with Jonald Fyookball & Ethan Heilman (Part 2)

- Playlist index: 8
- YouTube ID: `bpLOSytc7vc`
- Video: <https://www.youtube.com/watch?v=bpLOSytc7vc>
- Duration: 1:29:59
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  alright how's everyone doing today welcome to nether I was not a research club meeting today were talking about a fusion in part 2 we're talking about the combinatorics because last week we talked about cat fusion protocol and we have one of the authors with us journal is with us today who'll answer questions in just a moment okay I mean we had a bunch of resources because this was not a research so I

**00:00:30**  just want to clarify that Etan Hammond u1 and Janet who Janet wrote a blog post about the de nieve Cohen joins Matt Eaton brought up two attacks and nothing much actually brought up some attacks and or you were naturally yourself to be caught when he brought up some attacks on and and was was writing very long

**00:01:03**  article yes so there's a lot that's been said about the combinatorics and the privacy and security of the comet or X and so we'll be talking about that okay here's the paper you can find it on github and of course this is where we're at with the research club so you can see here last week we did a coin cash shuffle or cash fusion the first time

**00:01:35**  okay we've been talking about coin shuffle and plus plus in the previous weeks and these were mostly about equal output coin joints and we had a problem that we hit which is that we want to be able to do arbitrary amounts so the problem is that when a user uses any coin joint system that has a fixed amount typically they get maymay points later only to consolidate those coins an

**00:02:07**  arbitrary number of those coins without revealing input ownership ideally and those their privacy so it would be great if we had a protocol that allowed for arbitrary outputs and arbitrary amounts and last week Journal talked a lot about how cash Fusion allows a trustless and secure way for individuals to interact and create this arbitrary input arbitrary output point join by using pretty clever trick with homework

**00:02:38**  property of Pearson commitments Pettersen commitments and having all user submit 23 input output or blank values so they can have any number of inputs and outputs or blanks as so long as the sum of those is not more than 23 or the sum should be exactly equal to 23 and then other users can verify each other if the protocol just fails to to complete so one question we can ask is

**00:03:11**  okay well the entire protocol allows users to submit an arbitrary number of input outputs where the amounts can be within a certain range but aren't fixed as is in the case of zero link so how is it possible that we can't link inputs outputs if there are no equal outputs like these other protocols and so this is what we're gonna be talking about today we need to understand two things the bell number of a set of elements and the subset-sum problem so I'll be going over those and then we'll go into questions for the authors and everyone

**00:03:44**  else so let's just take an example here are some inputs and outputs and what might be a cash using the coin joint and purposefully doing a simple and small coin joint so a real character you coin joint is much much larger but this will illustrate the point sufficiently so here is the actual breakdown I've made it very simple there are three participants red orange and yellow and if you do the math you will see that the amounts are exactly equal we're not considering fees at this moment but if

**00:04:16**  you're just a passive bystander this is what you see right you see a bunch of inputs you see a bunch of outputs and you you have right especially if you're a forensics company you want to know what's going on here so the questions you might have are for example how many participants are really here because this is just one transaction it could be just one dispense that's what you know a naive onlooker might might think but you're smarter than that you know there might be more than one participant in this

**00:04:47**  coin joint and which input links to which output so one way you might do this is look at all the ways that the inputs can be grouped and all the ways the outputs can be grouped and try to find a value much so so the question arises well how many ways can we partition a set into smaller non-empty subsets and as an example let's just focus on the outputs because there are few fewer outputs that inputs in this

**00:05:17**  case there are just six so this seems to be quite a trivial problem how many ways can we dish in this set of six elements into subsets where there are no empty subsets well an obvious solution is just you know what once that is the entire set that's obviously works and that would be the case that this transaction only involves one individual can also do set one and

**00:05:48**  set two like this we could do it like this where or one set has three elements another has two and a third one has only one element and we don't care about the order of the subsets we really only concern distinct partitions so how many ways can we rearrange these subsets such that again their intersection is the original set excuse me their union is

**00:06:18**  the original set for a set of six elements there are total of 203 ways to partition this set into subsets this might be a surprisingly large number we're going to talk about the number in just a second so the number of waste a set any petitions is called the L number and we can observe the Bell number as we increase the number of elements in our set so obviously if you have a set with one element there's only one way to Commission it which is that very element

**00:06:48**  and that's it if you have two elements you have two ways to partition good partition it so that it's both all of its one element is in one second one element isn't the other and so forth and you can see that the bill number grows very quickly so by the tiny if this to do a set of seven elements you already have almost a thousand ways that they can be partitioned and there's a recursive way that we can find a bail number of any n plus one so long as we

**00:07:20**  know the total number of n of 0 to n and here it is and what's more important to sort of understand is that the bail number grows very very quickly so you see here on the right there's an upper bound of you know this equation with the with the diffraction and and input simply it's it's it's rough please you know it's less than n to the N so

**00:07:53**  it's a very very large number and so as an example if you wanted to investigate whinging with 100 inputs you have to inspect this many possible combinations so it's a very very large number as you can tell so yes we go back to our original coin joint and we say ok well how many possible subsets do we have to consider well over on the right we have our bail number of six elements which is

**00:08:23**  203 and on the Left we have our bail number of nine elements which is 21,000 so you can see it's growing very quickly and in a very simple way this is actually not true not the case we can simply try the four million roughly 4 million combinations of subsets on the left-hand subsystem there the reason why this isn't true why do little asterisks is because you don't want to try an example where there are three sets on the left and two sets on

**00:08:55**  the right because that doesn't make sense the number of sets on the left and the right must must match so it's smaller than four million but as you can see it's already quite large and the idea that the authors of cash fusion make the argument they make is that when you have a large number of participants with many inputs and many outputs as an example they they said ten participants with with ten inputs and ten outputs each you start to get into numbers that are just not practical for a forensics company to it to unravel and now we have

**00:09:28**  to talk about the other problem which is the subset sum problem so given a set of numbers is there a non-empty subset which whose sum is 0 so I'm gonna KP do you'll find something like this you know 1 2 3 4 5 negative 3 negative 4 negative 8 and here are some examples of subsets that add up to 0 now what the choroid example that we were looking at we can just treat the right-hand side as negative the left-hand side is positive and we get back to this this very problem so ya solving the subset sum

**00:10:01**  problem so here's an example you know if I wanted to solve this problem I just found right now two inputs then output that exactly match to the same value I can just may many times and I can do it with a very different complexities I have many many inputs many output so I could have just one input and one output and so the question to ask is well what's the complexity what's the runtime for a computer to try to break and

**00:10:32**  investigate all of the input-output pairs and essentially comes down to two parameters and I pulled this directly from Wikipedia so you'll read the same they're essentially comes down to n the number of elements you need to investigate so when our cases the number of inputs and outputs participants and further P the precision and so it turns out if you are less precise about the sets matching that it's actually quite quite a bit faster so the goal for

**00:11:04**  hiding in this complexity with doing cash vision is to create many inputs and outputs so make a large end and distort the precision of the input output links essentially having some sort of randomized to ease which is what the authors mentioned in the paper as a good weight to distort the precision and so algorithms for solving this subset some run in exponential time which again is what we're looking for for hiding in in

**00:11:35**  in complexity right we want something that gets incredibly complex the more participants join and so yeah that's pretty much the the very basics I will say a few things make a few points later on but that's pretty much everything I wanted to share to get us going so I'll open it to jonald need to say something and then questions yeah those are good

**00:12:05**  summary yeah so just to disclaimer I'm like not a mathematician except but I encountered this belt number when I was just trying to research this a little bit there's a lot of greats mouths public a PDA anyway so yeah as you as you played it out it's it's not like exactly a belt number like it like feet right but you could have a bell number for the in fights like the number of perdition's and then multiply that by

**00:12:37**  the by the outputs but then as you mentioned like it wouldn't necessarily be the same number of of groups in that partition so there's a my kind of number called a sterling not a murder which is related to the bell numbers basically a vowel number is like you're summing all the Sterling numbers over over some range so the way I thought to really calculate it would be to like start with start with the number 1 like 1

**00:13:08**  group and so the number of ways you can divide like 50 outputs into one group is going to be just one and so you would multiply that by the number of by the number of partitions that have one group on the outputs then you go to two and so you ask how many ways can you partition this group of 50 inputs into two groups and so on and you just keep going up until you've reached either the number of inputs or the number of outputs and then so you get all those products and then you just add

**00:13:41**  them all together but it's very similar to a goal number so yeah that's like what and then basically what with what the math and the paper is based on is basically like comparing that number of partitions to like the number of possible values you'd have in the in the space quote-unquote so for example let's just say that you're the maximum value

**00:14:11**  out of any input or sum of inputs is going to be like ten bitcoins or ten Bitcoin cash so that's that's 1 billion satoshis and so if you have like nine players then instead of like ten to the nine it's really like ten to the nine times nine which is ten the 81 actually you can take away one of the players because the the last player will just kind of have the leftovers kind of like by default so you might have with like eight ten times or some ten to the eight times I which is ten to

**00:14:43**  the 72 so that's kind of like where those numbers come from it's like you're comparing like 10 to the 90th first is 10 to the 70th and so the all these numbers are huge but the the number of partitions is like order or so magnitude bigger so like on a probabilistic level you're bound to end up with a bunch of valid partitions and then there's a second way that I analyzed it which which I wrote another article on which is kind of a more straightforward approach like let's start with player 1

**00:15:15**  have him select 10 of the 10 of the inputs and outputs and so he'll get like an N she's okay number and then you go out of the next player and but instead of choosing from like 100 inputs he'll only have 90 to choose from and you can do it that way also and it sort of also you might now put the same conclusion that it's they're given the right size of the the number of players and the precision of the inputs and the applets they're going to be it's it's basically private in

**00:15:45**  this way thank you before going into specific points I'd like to give an opportunity to eat an and nothing much to do to comment on what what happened what what they heard so far so maybe let's start with eaten you have any thoughts or comments so far yeah I guess one thing that I'm kind of curious about is it seems like these numbers are very large but these seem like worst-case

**00:16:17**  analyses for instance you could imagine a some subset problem that's actually like really easy because the values chosen are just like they just like works out nicely so like one of the problems that people have had when trying to use the knapsack problem for cryptography is a knapsack problem is hard sometimes but most of the time it's easy and so it seems to me like some of

**00:16:47**  these coin joints may provide privacy and some of them may provide not privacy or less privacy and I wonder how you think about that gap between that like the worst case numbers and the the like best case where it is like trivial to solve just because of the numbers that are chosen yeah that's a good question I I don't have like a like a simple answer but but you are correct like we

**00:17:18**  just saw for example I think it was last night there was this awesome looking transaction with like 100 implants and like 20 outputs but then there was one input I forget it was either one imported one output or maybe both I was like really big like like it was like eight BCH when all the other ones were like one BCH output so obviously that was that one sticks out like a sore thumb so then that's kind of one example of the kind of thing you're talking about

**00:17:49**  and maybe there's others as well I think what we could do at Subway is is to try to put in what I call a sanity check just like a some kind of filter where you're looking for outliers and stuff and I think the outliers is one thing maybe there's like I said maybe there's other scenarios where it's not really where the numbers are whacked you know in a way that kind of messes it up yeah you know and I think about this in equal

**00:18:20**  value coin joints right there is there is no discrepancy here right so so that would be zero but then if you increase the range of real values of these UT axles that you have and it's it's more volatile for example in between a corridor of 1.1 Bitcoin and 0.9 Bitcoin in this corridor plus minus 10% around 0.1 big around one Bitcoin you you can have a range or you know this range increases then to the plus minus 200

**00:18:51**  percent or whatever ok can we find some method to calculate where this line of you know range between the amounts shall be said yeah I don't know maybe it's a tough question the thing with even if you have like a value that's let's say more than twice as big as the others but it still could be hard to figure out like you know if you have a hundred inputs there to be many ways to get that to get that large

**00:19:23**  output so yeah these are good questions and hard questions I think and I think we would probably find that as the range expands away from the equal output it it reduces one thing I want to bring up is that knapsack was actually one of of the few

**00:19:55**  candidates for a one-way function I'm just reading here in the Merkel Hellman knapsack cryptosystem but it was later rejected that's an interesting thing because in that crypto system the users the the the the user that wanted to encrypt the data chose the elements in the knapsack so that means he or she could have chosen the absolutely best elements to hide and mask the subset-sum

**00:20:27**  problem and it was still rejected so this to me seems like a red flag I'm just curious what would Ethan I would say about that so I don't I don't know much about the actual knapsack cryptosystem I know it's been proposed a number of times and I think generally my understanding of it is the the problem is that it is not of equal hardness so I might choose a key or some secret value

**00:20:58**  that I think is is hard but then later it turns out not to be hard um so usually when you build crypto systems you want something where the keys are all a randomly chosen key has the same strength and other randomly chosen key um and a lot of sort of like NP problems have trivial cases and you may not always know whether you've chosen a trivial case or not right but you know just to take a look at this we see that

**00:21:30**  they choose a super increasing sequence of elements such that you know the next element is always the sum of all the previous elements this is ideal for hiding in a knapsack because you have a lot of possible numbers you can swap for other numbers and it's obvious which numbers you can swap for other numbers and even then it was rejected so it seems are quite me for us if we aren't able to you know handpick the the it's not what we want

**00:22:02**  to want to hide in I guess if no it's gonna pick it up then I might as well say my bit first of all I'd like to apologize him a bit sick and more scatterbrained and cranky than usual so I didn't really prepare properly and I have a slight correction to hapara which

**00:22:33**  is that I do not like talk about any talk about cash fusion in particular more generally about this same problem of assuming that this is like a valid hardness assumption from a cryptographic standpoint like interpreting the bell numbers as security parameter seems sketchy to me for these reasons and it seems more sketchy to me also because I

**00:23:04**  think subset-sum is the wrong framing for this I mean it's more like it I think technically it's the end partition problem and subset-sum is a search problem but really in the end partition problem is also a search problem but from like a China adversary point of view really it's more of an optimization problem is that maybe they only care about one

**00:23:35**  participant or maybe they only need approximate answers so I think it's very important to distinguish between the number of plausible interpretations for a coin during transaction for the equal amount cases it's trivial it's literally just a bill number but in in other cases it seems like a very optimistic and of

**00:24:06**  assumption to to like analyze the search space invalid mappings from using the knapsack terminology because that numbers might not be relevant at all maybe because they're using you know a better proximate techniques for example linear programming is pretty effective at giving it a good enough but not perfect solutions to this so that is the

**00:24:42**  resource for this research club was actually using linear programming and he could not not do anything with it so yeah that's exactly the point I was getting to by the way I used it as well for the still yet unfinished shame research that I did on on wasabi to identify change so I did it's a pretty effective technique I mean even for wasabi sites coin joints when you have

**00:25:13**  the constraint set up right the system like pulp with I don't remember I think I used the coin horror solver whenever it was not buggy it was under a second to come up with an assignment that that's unique for the the change values even accounting for all of the stuff that the wasabi coordinator does with fee discounts and so on and so forth so even for fairly large problems where n is large in practice I think treating

**00:25:47**  the the space of invalid options is a dangerous assumption and what James's are equal showed was basically the there's more than one solution and I think that that's the number that we are really interested as far as the privacy gains because that's that's not something that you can decide a priori which of the valid solutions are correct once you've enumerated a set of solutions if that set is sufficiently

**00:26:17**  large that it confers plausible deniability to the participants then I think the coin joint assumptions work so to meet kind of like that is the that was the main point of my email and was not you know with respect to cash fusion but more generally about knapsack and and cash fusion I just want to jump in on that idea that the number of solutions is the privacy gained because with tumbled MIT

**00:26:50**  when using tumble bit as a payment hub that is exactly the privacy definition we get like any any any the privacy is the number of ways that this input and output relationship can be satisfied I I think that that's like a really good way of looking at it and that's not to say that adding additional difficulty for the adversary is bad I think it's great to make it computationally harder I mean I really struggled to write that linear

**00:27:21**  programming stuff because of all the idiosyncrasies in wasabi and I'm still not done there's still bugs so in a sense it's effective but it's not a robust security assumption I think all right so so far we talked about computational hardness one thing before we move on to the actual number of valid partitions I just want to address something but because on the bit kind of mailing list many people can be the basa beings and just just like you now but

**00:27:53**  the wasabi example is bad because we have Cohen selection that's very public so if I look at inputs in a Vasavi transaction and I if I find an input that is larger than the based on denomination then I'm not going to try to find all the different partitions these inputs can be combined together in order to find a change but no I'm gonna say hey this input is its own partition

**00:28:24**  I'm looking for the change for this specific input and usually that's going to be right unless this was a test transaction by me there were some strange noises there but you see there there are very very simple heuristics how to get the change back because there are rules that possibly follows and and that can be used for for analyzing it yeah that's exactly what I did I did not attempt to

**00:28:56**  analyze the mix outputs only the change outputs but that that's still a large N and in principle by specifying is a linear constraints problem the search space is the entire thing so I think that there's a what the knapsack paper basically did is it proposed a way of by construction always having some plausible deniability and my understanding of cash Fusion is that it kind of achieves the same plausible

**00:29:28**  deniability as James Bond's article should stochastically in the sense that given the amounts are quite similar and there's randomization and many inputs there's a very high probability that there's going to be plausible deniability but I think that's very distinct from the computational hardness of actually like putting assignments in there yeah all right let's move on to that because that's the this is the huge

**00:29:58**  contribution of of this because no one actually ever thought about as far as I know the knob stock paper introduced the computational hardness idea but no one thought about oh there are actually very accidental valid submitting saying and how does that make sense now I there is an intuition that I heard from John art and this is the birthday problem right which actually John had

**00:30:30**  which would you like to explain the birthday problem and how this can be this intuition can be applied to the two developed combinations maybe yeah I forget where came up in in which conversation but it's just I guess the birthday paradox is kind of just an example of how sometimes math can be a little bit counterintuitive and you don't expect like Oh 23 people in a room well you know there's like a it doesn't sound like that many people right so it's when you hear that oh

**00:31:01**  there's a 50-50 chance that someone's gonna have the same birthday you kind of scratch your head and say wait a sec does that make any sense and so the same thing kind of the same kind of counterintuitive property seems to apply the here also when you look at like it's surprising how many different ways that the things can add up to the same sums so there's a there's a piece of code that mark wrote which which kind of does like I just call it mini cash

**00:31:32**  fusion where he's just taking three players that each have six in inputs like any each of them are kind of like they're they're pretty small like a 150 or 400 or something and then you run the code and it's like oh there's like 60 ways that these could all add up and it just seems like like really counterintuitive and like for me I do like just check a few of them like wow okay that adds up like so you know that you get a lot more things that sum up

**00:32:05**  and then you would really think I have a question when we talk about plausible deniability are we saying that the three possible input-output relationships that can be satisfied work or are you saying that they're equally likely like you like one could imagine that you have three different ways of doing it we've based on the spin distributions

**00:32:36**  one of the ways is like you know 98% of the time and then the other two ways are like one percent of the time why would why would some of them be only one percent versus one of them is like ninety percent so if you imagine that the number of input coming into a transaction is like drawn from a some sort of random function if that random function is not like uniform

**00:33:07**  most people might only contribute three inputs so five inputs is like less likely but yeah I don't know it's an interesting question I don't know I think I mean if you look if I look at a my wallet right now like some of the some of the cash fusions have like like you know three or four inputs some of them have no input so it's I think it's I don't know if that's gonna be too much

**00:33:39**  of a factor I just wanted a bit I wanted to make a couple other comments of some of these things you guys were saying um I I forget who said it but I agree you know the like the math and cash Fusion is not exactly that the subset-sum problem and it's not exactly the partition problem either it's kind of related to both of them but it's slightly different I think it's kind of it gets into like maybe what some people will call like additive combinatorics which I don't so I don't think there's

**00:34:10**  like a clear I don't think anyone's really solved the math in like a rigorous way now the other thing I wanted to say is as far as the James Watt I hope I'm pronouncing his name right his paper is really interesting but like to me it just basically all it really proves is that it's not broken it in a trivial way so what he's doing is like just coming up with one possible set of inputs and outputs and then looking at all the other inputs and kind

**00:34:42**  of proving that they could at least exist in some other in some other sum but he's not he's not showing that they're all like adding up at the same time so he's kind of taking a slice you know what I mean which is cool but it's not really like proving anything one way or the other I interpreted it as concrete proof of so first of all to clarify I used plausible deniability the weaker sense of not assuming any

**00:35:13**  prior knowledge and only considering a single transaction and isolation and within that kind of like the way I interpreted his article is that even when you apply linear programming to cash fusion transactions if you add if you get a solution out of the solver and then add a constraint that says it must not be that solution additional solutions exist and that's just a standard technique for enumerated the the set of solutions and to me the point

**00:35:46**  of it was even though the hardness assumption might not be robust in the sense of like interpreting the the anonymity gained as proportional to the Bell number you still end up with that like fundamental level of ambiguity because multiple solutions exist so I understood like that to be a pretty

**00:36:16**  strong statement about he didn't analyze like how it came to be that there were multiple solutions but I thought it was completely independent solutions based on my understanding of his article well he was showing that if you if you have like one like out of the whole trend this whole huge fusion transaction if you like select some inputs and some outputs he proved that the other inputs

**00:36:48**  like it's not unique like those those inputs could be in some other sum but he didn't really show that that both of those would exist at the same time that's that's kind of how I saw it so it is like valuable to show it's not trivially broken but it's also not like a rigorous proof that it's you know that it's secure specifically the passage I'm referring to so he says to check this we can rerun the integer programming solver to try and find a match that is distinct from

**00:37:20**  the match that we've already found the must include this value when you said he's not talking about the whole transaction he's just talking about one player as far as I understood it but that implies that there's likes to at least two valid interpretations based just on the information inside of the transaction so I think that's a pretty good finding in the sense that like I

**00:37:52**  don't think it's any weaker just because he's focusing on one was like one match yeah maybe I mean I actually don't know that much about linear programming but yes it's pretty cool pretty cool how we coded that I have a question about the privacy model it is the assumption that the tumbler or the party constructing the coin joined the coordinator doesn't

**00:38:25**  know how many outputs are assigned to a user so does it know that like three of these outputs are the same user and two of these outputs are a different user it might not know their input-output relationships but doesn't know the groupings or does it know like this was constructed by three users but it doesn't know how many of those three users are there and if that isn't in the privacy model Oh if that isn't assumes like what's the

**00:38:55**  network security to sort of hide that from the from the like coordinator party that's producing the when you win so the server could find out how many players are in a fusion but it doesn't know like how many outputs or if there are like per user does that answer it yeah I'm just like how does it so I guess all

**00:39:25**  right so it knows how many are there so the probability the the analysis like if we say we have deniability but one of those paths is like assumes eight users and we know that it's Lyme users do we still have multiple debility like is there sort of a little bit of trust as based on a tumbler not to reveal that information oh and all the users know this information tour I believe not the area the user is on now actually is another

**00:39:59**  users don't know I I'm not 100% sure but if they're not something with the index number in the blaine face to which of the with which was the users your randomly assigned an index number I believe for them that's not player based is just input so when in the blame feeds you you know the player is verifying one of the inputs or one of the outputs but the the players don't know how many other players

**00:40:29**  exactly are in the in the round the server could know because because it has the list of commitments from each player but as far as like trying to like use that information to get a better understanding of the combinatoric s-- i think you'll probably only have a limited value limited like you could like if you're doing the math based on sterling numbers it would narrow it down

**00:41:00**  like if you knew there was a eight players exactly then it would just be it would be like the Sterling number of like eight Lauren let's say 250 inputs then you could basically be asking how many partitions are there with exactly eight groups of 50 inputs and then the same thing for the outputs so we definitely decrease the number of dollar partitions if you do that but only the server knows that actually yeah thank

**00:41:32**  you I I want to go back for a while when when Ethan said something because I think that was very important and we kind of missed it that you know what really matters is not the number of parties but how well the links are broken so the nutsack paper actually gave a mathematical model of analyzing Cohen joins in terms of so if you take well

**00:42:05**  the valid partitions and then you look at input input input output and output output links which would mean that for example you take two inputs and you see how many valid partitions there are compared to the total number of valid partitions and that's how strongly the link is broken

**00:42:36**  so I think when someone will investigate this problem further then that would be a very very useful thing to actually look at and try to try to analyze it because if it turns out that that the valid partitions are usually the if it turns out that that there are much more valid partitions for for real link then

**00:43:07**  that's going to be the assumed transaction there I hope it was understandable what I said you asked me are you saying that it's it's all about just like finding the number of valid partitions not necessarily the total number of partitions if I register to input together and no one knows these two inputs are together but I registered them together and then they find all the valid partitions of the coin join and

**00:43:40**  then they find that that there are ten valid partitions but out of that ten nine valid partitions actually partitions together my two inputs right something that's almost as hard as like trying to try to solve the basic problem anyway it's like you're trying to you have so many partitions it's really hard to give that data I mean that's is there

**00:44:12**  I don't think that it is because I mean again you have mecan't solve the partition problem in the general case in less than exponential time but for special cases you often can and I think that this is this is also a weakness of the like the samurai Boltzmann entropy measure I think that's another very

**00:44:44**  important distinction I want to draw is like the privacy from the point of view of an individual user so how much plausible deniability am i gaining by participating in a joint coin joint of some form versus I guess technical fungibility would be the way to frame it that is how much does this transaction how much I'm B get a does this transaction create from a public point

**00:45:16**  of view and I think that those are very distinct analyses because for privacy you care about whether or not people are targeting you and in those circumstances it's also plausible that they're going to use additional information like network level privacy leaks they're going to look at the transaction graph as a whole and they don't really care about looking at the parts of the

**00:45:47**  transactions that maybe you participated in that don't pertain to that data so that there's many ways to prune that search space and and secondly maybe they don't even care about like all they want to prove is you know it the that you had at least this much money that flowed through some some something right that's I think of a very different

**00:46:20**  analysis than the public level privacy which is what most of these analyses kind of kind of look at did that make sense yeah interesting points yeah you're talking about using other like you said no network level there could be timing things yeah there's like different ways that people could try to try to break the privacy but yeah it's it's kind of an interesting it brings up

**00:46:54**  the discussion of like you know how much privacy do we need or maybe it's good to like not have like too much like maybe not hat you know like in Bitcoin cache like we don't necessarily want to become Manero for example so maybe there's like a good balance where a coin can have like the privacy for everyday users and still not be like no be like that go too far on the side of privacy where the regulators hate it I don't know well I

**00:47:26**  mean even in maneras case if you have some requirement you can always prove what you actually did so that's not the distinction I'm trying to draw rather that there if we assume that privacy and fungibility are Anette good analyzing the risk or as uncertainty with respect to either feels very different to me because for the case of one user trying to hide from an adversary that sees

**00:47:57**  everything a lot of these guarantees that make sense in kind of the public context become a much weaker in in like a single user context yeah yeah we're agree but it's like you can look at the average you can imagine a coin joint that provides very good average privacy but always Rob's one user of privacy and so if you just look at that average you're like oh it's providing a lot of privacy but if you're that one user you get no privacy from it so I think yeah

**00:48:30**  like what is the minimum privacy provided to each user um right rather than like the average privacy provided oh yeah that's the point that is trying to make yeah go back to that example where there's like two inputs even if you group them together that doesn't necessarily tell you what the outputs are so maybe neck that's kind of part of the conversation of the minimum can you

**00:49:06**  rephrase that I didn't understand like even if you even if you somehow were able to determine that there was some inputs that are likely to belong to the same person that doesn't necessarily tell you which outputs they got right but I think that in that scenario it was like there are ten valid ways for this coin joining to work and in nine of them

**00:49:36**  this set of two inputs matches some other set of three outputs and then in another only one other case for that set of inputs matches and other set of outputs so if you were to assume that these inputs and outputs were selected but randomly there is only a 10% chance points one place and there's a 90% chance particular input-output relationship for a particular user oh that's actually the exact same problem that's the largest input largest output

**00:50:09**  attack what you you mentioned Janet which was which was what some 100 1000 and everyone ask comes with around one right so one thousand in and I don't know 900 out that can be only that because in every valid sub mapping of the coin join that large input will all connect to that large output right but

**00:50:41**  but in the case we're not talking about like those kind of outliers I mean like how would you how would you solve this how would you how would you get insights into which are the which inputs go together so I don't know how you would get insights like in the largest value one it's like pretty obvious but there might be some of them less less obvious approaches but I think that the right metric to use to measure the amount of privacy is to look at the the guessing

**00:51:13**  entropy that is if you sorted all the possible input-output valid input-output relationships from most likely to least likely and you started guessing from most likely how many guesses would you need before you got to the correct answer like on average but there's multiple correct answers right there's multiple correct answers but some of the correct answers are more likely to be correct than other ones hmm like in the

**00:51:47**  nine versus one example when user gets in anonymity set size too and the other user gets where the other users get much higher values right what you users and high value users and even if they put the money into the same coin join the the low and high value users are going to end up in the same sub mappings in

**00:52:17**  every every village sub mapping of the coin joints or most of them it'll be interesting to see what people come up with you know some some actual mathematicians maybe will publish a paper and see they will see some more insights into the heuristics and techniques like that could be used to try to break it how would this change if we have a combination of unequal and equal output in one transaction

**00:52:47**  basically something like what wasabi is doing right now right you have the equal value and you have change but differing from this current model to remove this restriction on the number of inputs and outputs so basically say that any one user must have at least one input and at least one output but there is no upper bound basically with question some some reason and then you don't know his one user has only unequal amounts or if he also has

**00:53:17**  equal amount coins and how would this change the the possible set well already you can have multiple I mean you can as far as the second part of what you said like there's no you know the only thing is there's 23 is the maximum total of inputs plus outputs so you could have one input one output but you could have also have more inputs or or or outputs but then as far as having some of the

**00:53:50**  outputs being the same value it's kind of interesting a network that's I never thought about that but maybe it's maybe I can improve it so here is a thought I wanted to bring up later but now we are on topic that if we would want to use cash fusion as it is then without cash off or without any kind of mixing before then you would still have to break coins

**00:54:20**  into two or three or four parts anyway don't you because it's like users don't have like only users who would have a lot of volume and incoming and outgoing money would be able to actually participate with multiple inputs and outputs so I think some kind of amount splitting would be necessary in order to keep the thing flowing do you have any

**00:54:53**  think is that something miss am I on the right path on this thinking that's the whole benefit of like the unequal amounts you don't need to worry about splitting things and and trying to like prepare the UT EXO's you can just kind of fuse with whatever coins came from the last region or or whatever you have so it's yeah kind of more practical there is a difference there because in

**00:55:26**  unequal amount you cannot split that's the rule here you would split and you would gain privacy but you would have you could still decide to not split it so that's that's why it's interesting you know all the stuff is pretty interesting yeah okay anyway let's move on to two there are three attacks the

**00:55:58**  type I wrote to myself and one is we talked about the largest input largest output the other two is his Eaton's attack shocks actually but for before going into eternal attack anyone has any idea how to mitigate the largest input largest output attack well like I was saying earlier if there's if there's some kind of a sanity check on the server before it it proceeds if

**00:56:30**  there's an outlier where it's some huge value that's that's an order of magnitude beyond everything else it could just maybe the round just gets aborted or something yes and I think that the robot is described in the paper with the spear size or cool read history so I think very interesting because here then we can use different polls to see who is waiting for doing a coin join and then as soon as a certain and onset is reached that specific tea arrange of

**00:57:02**  let's say one Bitcoin plus minus 10% gets done by then maybe the the lower the ranges maybe 10 become plus minus 1 percent like the the more possible sub mappings would be valid so how would you define the outlier my thinking is that it is larger than the sum of all the other inputs so there is an output that's larger than the sum of all the other inputs but there might be

**00:57:32**  some more restriction needed there so it sounds like a sensible upper bound at least right yeah by the way these other attacks where can I read about them I haven't I haven't he said that he thought a couple of attacks where can we find this so it is on the wasabi research Club it is pointing to the Bitcoin dev mailing list and there were some discussion and and let's see and

**00:58:05**  okay so so one of the attack is the precision attack eaten could you describe it sure so I should I should preface my statement by the the stuff that I read through on confusion wasn't very specific on how it worked so I made some assumptions about how it works those assumptions may not be correct so the first attack was assuming that we allow inputs of arbitrary precision and

**00:58:41**  looking at C so looking at the precision of the outputs where you can you can infer based on say like this having a whole bunch of decimal places it could only be or then it was more likely than it was from a particular input so like if you had an input that was like one dot 0 0 0 0 0 0 1 and then

**00:59:13**  you had an output that also had like like that was like you know 0.5 0 0 0 1 if the it's probably likely that that one that's all the way out to the right matches in the output matches in that input so I looked at that if you just allow arbitrary arbitrary precision especially if you're doing wallets where some of the wallets may not actually allow you to do outputs of arbitrary precision um

**00:59:45**  I don't know if this is a problem in Bitcoin but I know in aetherium and their people sometimes don't let you do beyond a certain level of precision so you might have wallets where some wallets are only producing input outputs with a certain level of precision and then all their wallets are producing input-output relationships with a a higher level of precision um so this could this could be a heuristics that would allow you to identify input-output relationships I don't know if that made

**01:00:15**  any sense just to be clear it's it's a good attack vector except if there's any randomization in the fees it would distort any minut differences in the in the you know eighth and seventh and six decimal points so that's just my I'm guessing that's what jonald would say as well yeah I agree it's easy to mitigate ways to yeah I mean that's what we're

**01:00:48**  already doing I think just a trivial amount I think I got just ten Satoshi's of randomness with the fees but we could add more and we could also add like just kind of like any mark calls of quantizing just just kind of bird forcing like just chopping off a decimal to make it just have less precision in the outputs it just makes it a lot harder to to have unique ways to add up or makes they're more possibilities for

**01:01:18**  different combinations to add up you've seen these mixing protocols you can all be is up to let's let's take one person fee from everyone and that fee would be some some gambling there that to make make make make output somehow equal or something like that that would be the the point of the fees there are there are interesting things that are eaten do you agree that it's easy to me take it I think that the the

**01:01:53**  mitigation described like breaks my attack um but I'm not sure that there isn't a more advanced attack and it really depends how you do these like fees because if you're you know like if the if the fees were only to a certain level a precision and and the output was the the the precision that someone produced it out put in it was like greater than the fees so I think it

**01:02:23**  really depends on on how exactly these mitigations work well when I wrote that attack as I said before um I wasn't sure on some of the details with how the protocol works oh it's just assuming arbitrary I was assuming two cases either arbitrary precision or on a fixed precision and then I looked at attacks against both of them but I did not consider that case in which you are like randomly subtracting fiends which is a is a really interesting approach but I think kind of I need to think about it

**01:02:55**  more to understand that um how whether it fully mitigates it but it does mitigate the like sort of fully attack I posted a reckon by the way I think a slightly more robust mitigation would be to not just add fuzzing would also restrict the Hamming weight where is something proportional to the product of the Hamming weight which is just a number of one bits in or the number of symbols needed to represent an amount

**01:03:26**  times the difference between the largest figure and the smallest figure because that that gives you the the formula is just off the top of my head please don't take it literally but the idea there being the more the the larger the Hamming weight of an amount the more a signal there is in there so that's a very simple approach to kind of reduce the ability of the

**01:03:59**  adversary to interpret the the different bits in the the amounts as related or not related to each other maybe what Hamming is because when I wrote that I've heard it before and I've seen it so it's the number of symbols required to represent a codeword and in the context of amounts well you can just think of it as the number of 1 bits given that the

**01:04:31**  alphabet is like binary digits and so for example if you represent a power of 2 of satoshis that's gonna be a Hamming weight of 1 where is like a high precision value with many digits in it that's gonna have a much higher Hamming weight I guess it sounds very related to just have any decimal precision I think that that's one aspect but also the the other aspect is within that range of

**01:05:01**  precision how much information is in that amount like it could be a very precise amount in the sense that there's a very large difference between the most significant digit and the least significant digit but if those are the only two digits then you only need a very minor amount of fuzzing so long as for the most significant digit you have plausible deniability because of the other participants right that's right assume that there is a everybody is on

**01:05:33**  the same tier therefore everybody's amounts are within the same order of magnitude that confers plausible deniability to the most significant digits and fuzzing confers possible deniability to the least significant digits but you know for larger amounts there's a disincentive to enable it but if you restrict the number of digits that appear in the middle of the range then you only need a small amount of fuzzing to basically make it so that

**01:06:03**  that information is is kind of useless to anybody doing this sort of analysis did that make sense yeah yeah I wish mark was on this call cuz I'm sure he'd get a lot a lot from that I think as as we go on evolving this thing there'll be lots of things we can we can add in to try to improve just like the the consistency of getting quality fusions that that are all well you know or that

**01:06:35**  are more private in general so yeah maybe we can we can use some of those techniques to to try to do that yeah thanks and how about I talk to Eaton because I have to admit I've read it many times but this made absolutely no sense for me can you elaborate on what what it's about Eaton sorry yeah I kept

**01:07:07**  machine the me button I'm sure I think I think one mistake I was making when analyzing it was I was not um I was assuming that the I was not assuming that someone was adding more than one input but I think that the attack still works but I'm gonna modify it a little bit um so the idea is that rather than

**01:07:40**  deal with lots of this rather than deal with arbitrary precision you fix precision um but since you fix precision you have cases in which for example here's a really trivial case imagine that you fixed precision to be only one or two bitcoins well if you have if all your outputs are are on then you know

**01:08:13**  that every single one of those outputs must Elise map to one of the one inputs because to be an odd number it must have one if you're drawing from the set of one did you so if you have like a very small number of inputs that are similar you can make these inferences that allow you to sort of shortcut trying every single possibility you're set to be the numbers

**01:08:57**  one through five so you can only have inputs of the numbers one through five and you're looking at an output and the output is an odd number then that must mean that the input set of that output must contain either one three or five it must contain at least one odd number because two even number even numbers

**01:09:30**  added together it should never result in an odd number what does that still hold up if under the in the context of having an arbitrary number of outputs let's see um he split it no that doesn't hold up in having an arbitrary number of outputs because you would split the even split you could split an even number into two outputs yeah so I think I was thinking about the I think when I was thinking

**01:10:02**  about my infusion I was thinking it was more like some of the previous approaches where you have like inputs to outputs like you don't hear or not like splitting the inputs and you're outputting the outputs so the example that I know that there was was exactly that ten inputs then users every one

**01:10:32**  with ten inputs and exactly one output that was the example so that's so if you know how many users participate and how many inputs user participate feed or how many output a user create then that would then that gives gives assumptions like

**01:11:05**  this gives gives more more power for assumptions like this it's it's actually pretty genius yeah and the the tumbler might might know that is value is right we might know how many users there are and actually so I asked this before but I've forgotten the answer does the tumbler know that a particular user created not does the tumbler knew that a

**01:11:37**  user exists that created three outputs they might not know which out listeners are and they might not know which user created those outputs but do they know that there is a group of three outputs and are now the server doesn't know the server does not know how many how many inputs or outputs each player brought I mean every obviously everyone sees the completed transaction and knows the total inputs and outputs of the entire

**01:12:08**  transaction but not even the server knows like that Alice brought seven inputs in three and three outputs or something but the you know like I would deserver might not know that Alice did three inputs and seven outputs but the server might know that someone created seven outputs now they but they don't though all right this is because the various components are not linkable right each is submitted on a separate channel the server has 23 component

**01:12:41**  commitments from every user but those commitments don't much and the input and the input components and output components and the blank commitments are both registered in different tour streams or not not as one so so there there is there may be something in a blaming phase but but other than that not nothing Suman said tour circuit per employee exactly it's a

**01:13:15**  tour circuit per to cut it and then during the blank phase it's just basically one one component gets checked but and then the round like reduces the number players for the one for that one person all right so my very last question of the day and and I let her keeper to talk to so are you guys familiar with shared coin block chaining

**01:13:45**  for was was was creating that in 2013 which was unequal inputs and unequal outputs that of course the blockchain info server know everything but regardless crystal fat loss was able to do some conjoined pseudo coup and so what was the problem with shared coin well the problem there is the linear

**01:14:17**  programming so there is a special case of linear programming so that that was able to solve it very efficiently and in practice in many of the cases because typically users would have one input and one output if you have you can you can do sorry one I think they had like in a

**01:14:51**  typical case one input and an output and a change output my bad oh okay yeah oh yes because I was actually using shape okay when I was using it I had to I always sent the money which shared Kareem I never mix to myself yeah it's a indeed SharePoint work is that is it similar like there's a server like wasabi no so it doesn't work it worked for a couple of years but it

**01:15:21**  got shut down its block chaining varieties of a bullet and blockchain so I trust less you couldn't lose your money but there were no privacy guarantees because the server did everything all right aviv igor max all Garofalo we have a lot of people here yeah yeah so you guys

**01:15:55**  feel free to join in and ask questions or topics I didn't rota I sort of wanted to I guess ask a few questions to journaled but rather if someone who hasn't spoken yet wants to ask first go ahead okay I guess I will go ahead so I just want to

**01:16:25**  get a better understanding of the larger picture of how cache fusion was intended to work in practice so just just a few questions and hopefully you can answer them so typically users show up with more inputs than helpless right the idea is to fuse inputs into outputs so that was the original idea but it sort of evolved to now it's kind of like a general-purpose many-to-many coin joint

**01:16:59**  so some some transactions could be fanning in when I say fanning enemy there's outputs and inputs and some could be fanning out where there's more outputs and inputs and then within one of those there could be like Alice could be Fanning in about could be fanning out at the in the same fusion so it's kind of become this like this general-purpose thing where each of the wallets has like just a bunch of UT X OS and it just kind

**01:17:31**  of there was there's a little bit of randomness where it selects you know like let's say 10 inputs and then it's just going to decide randomly you're gonna get eight outputs CNN I'm doing like a 10 day and then in the next round maybe you're gonna go the other one you're gonna start with like five inputs and you'll get 13 outputs so it's kind of a little bit random I think what we're gonna do is try to try to make some like user friendly settings in the wallet so that it it would like fuse a

**01:18:02**  bunch do a bunch of rounds and then at the end it would try to click consolidate them down so you have less less coins so let's say I'm a user right I show up with let's say I just withdrew all my big win cash from the exchange and so now I'm using this cash fusion system so it's going to start fanning out and I'm guessing it's also running in the background if I leave my laptop

**01:18:33**  just awake and I just let it run it's going to keep mixing in these different transactions correct yeah that brings up an interesting point which is like you know if you just let it run forever it is it just gonna eat all your all your money and fee is so so we we think we need some kind of thing where it does shut off eventually and then maybe there's another mode for like liquidity providers I just want to just you know keep it open although

**01:19:03**  there's well we can talk about large amounts like 10 big win cash and 100 for example where something like this wouldn't wouldn't really matter although you know you can't run it infinitely so then I want to spend money what does that look like am i looking at my you see episode sets and just selecting a bunch of UT exomes to spend so okay so you're talking about coin selection after you've already done a

**01:19:33**  bunch of fusions yes yes no I think like ideally you don't spend all of the claims from a single fusion together because that's sort of it's sort of a sliding scale like you know the absolute best thing is to spend one you TXO because then you're you're leaking zero information right and then when you spit at the opposite end of that is if you spend all the UT EXO from a fusion it just it kind of degrades that fusion for

**01:20:04**  the other players so maybe there's something weird like warns you or it's like hey are you sure you want to spend this it's like it's kind of a low of privacy spend but on the other hand we don't want to like prevent people of you know it's your money you want to spend it and you should be able to spend those coins so the wallet should kind of ideally be smart enough to you know to try to coax the user to doing it a little more privately with also having the flexibility of just letting you spend freely if you think you can you

**01:20:36**  can spend within the coin fusion or the cap screws right that's what I'm gonna miss that was sort of like the only problem with that is that you you might have to wait like if I want to buy something let's say I wanna buy a domain name so I going Namecheap I could I could like set that up somehow but then it's gotta wait until that fusion happens so that may or may depending on the liquidity like it made in my feature

**01:21:08**  right right and it might be a different tier size by the tier size was rather low and limit is that for example or low number of tiers or whatever metric we will use and and that just completes faster right and then you have something every ten minutes even if it's only ten different users that will be alright in the span maybe there's a feature that we want to eventually but I don't think we're going to do it right away and I don't want to ask too many questions because it'll go on forever so maybe just two one more

**01:21:40**  after I've done my first fusion and I get let's say six outputs the next fusion that I get into does the software limit how many outputs from the past fusion are going to be allowed into the next fuschia what does that look like to get a question I mean it basically does a random selection so if that's all you have is those six outputs that it would probably use them but I guess ideally

**01:22:10**  it's it's trying to try to be a little bit random so it you know if you have a hundred each EXO might take you know ten for round one and then a different set for round two maybe round two has a few of them but yeah I think it's just it just has to be random okay so it just become a problem for people with a small you TXO set so the it's not

**01:22:44**  that private event as they as they keep using they'll just they'll get a bigger set of more like kind of truly random coins got it okay I'll leave it at that thank you so much you had jonald for answering those questions yeah sorry I don't have like perfect answers for these things but and so we have here developers mathematicians a cryptographer and even a woman how you guys see some

**01:23:32**  of this stuff do you see it being ported over to DPC in some form I think I'm I am really in doubt here because because it's it's something that you know that there is something out there that's already working and and it might very well be just just working and sound and it might very well be the

**01:24:03**  actual best privacy solution for Bitcoin Bitcoin cash doesn't matter but on the other hand I'm somewhat afraid - well okay let's go a hundred percent forward on on unequal Cohen joins because there are just so many little things that I'm not that smart you know I'm just a programmer and I'm not sure I would be

**01:24:34**  able to even believe if there would be one research out there that would go through it maybe there would be to say yeah I'm in doubt because on the one hand I want to innovate and on the other hand and just what if I up something people are relying on this really heavily and that's scary you know so I I don't know like there's some things in the samurai wallet like

**01:25:04**  ricochet and a stowaway do you think are also pretty cool that maybe we'll adopt it you know in Bitcoin cash I think well there's like there's like you hear these things it's about the coin joint flagging so which is pretty stupid but it's like maybe maybe some tools like ricochet would be good too you know to have it's let's not debate samurai

**01:25:36**  like oh she has a very unique fingerprint on the back chain you're just losing less and spending okay that's not no no it's just we'll talk about that a different different time so ask your earlier question are we going to use this I would say maybe this is a bit different than whatever then with no power set which is that we are trying to get inspiration from all ideas so it's

**01:26:07**  very likely that we will take some subset of the ideas that you've come up with and and we might find a place for them Oh a very very important interesting thing eaten in Tom Babbitt you were fighting with how to make sure that the tumblr parameters the tumblr is not lying about its parameter do you remember yeah and you were coming up

**01:26:52**  [Music] anyway could you mute yourself for a little bit thank you so cache fusion has a pretty cool way to to answer that the tumblr parameters are not lies it's actually in an Oprah turn of the coin join the the hash of the the tumblr parameters and actually you can extend

**01:27:24**  this this idea to more generically that every oh my god I don't really remember but every input has to sign that yeah there is something about that that you might want to look at the issues of cache fusion and and that that could I don't know if that would be nice for tumblr it's interesting um I think that the

**01:27:55**  biggest parameter that we wanted to lock in was the time at which the tumbles occurred because if if you do them at a particular set time then if you exclude a bunch of people it's much more obvious then if you do them like on the fly when you have enough users you could be like oh I want to target this person so I just added a bunch of fake users and now I'm gonna like mix with them but I think

**01:28:26**  this this protection against like civil attacks where you where the tumbler is malicious and adds users to create the illusion of privacy is it's really really hard to solve and I think taking an approach where you just assume the tumbler does not do that is probably more realistic although it tumbled it was attempting to prevent those sorts of simple attacks yeah it's another kind of worms here let's not open this okay so

**01:29:04**  what do you guys have or should we should because this I have to go pretty soon here so if anyone was to go then I can leave first or otherwise I'm not here I also chopped off in a few minutes so was it was a good caller and thanks a lot this was probably the most deepest conversation of the wasabi research Club

**01:29:35**  ever so thank thank you guys it was really awesome and yeah this is the highlight of my week lately thank you bye bye thanks guys thanks everyone thank you it was a good

# Wasabi Research Club #11 - Boltzmann (Bitcoin)

- Playlist index: 11
- YouTube ID: `CYIDAqMSc4A`
- Video: <https://www.youtube.com/watch?v=CYIDAqMSc4A>
- Duration: 0:49:53
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  [Music] Hey [Music] good morning good afternoon good evening to everyone this is another edition of our with sunny researcher Club today we're talking about Boltzmann evaluating privacy using entropy metrics just work done entirely by Laurel or Mt it's all available on github and of course we link all of the work that we

**00:00:30**  go through on our wasabi research Club github which is just down below just to remind ourselves where we are we did a bunch of coin shuffle plus plus cash Fusion and we talked about principles and privacy talking about best practices and how we go about thinking about designing privacy for anonymity networks we talked about Koh enjoy Sudoku last week and this week we're doing Boltzmann

**00:01:02**  when the end of this video hopefully we'll resolve what we will be reading next week last week we talked about the coin joint pseudo paper which tried to be anonymized flawed coin joints done by shared coin which was a blockchain info implementation which simply took transactions than merge them and the way that the D anonymization attack happened is that as

**00:01:52**  one sec guys I'm just trying to know yes it's gone oh yes I don't know is this better yes yes excellent okay so moving right along so we talked about how if two transactions are merged together then there is some uncertainty about how we could be anonymized the merged transaction but if we wanted to do

**00:02:24**  naanum eyes the more transaction so here on the Left we have transactions on the right we have the merged together as in one transaction what we really need to do is figure out how to make the inputs and the outputs match in sums just like this and we keep trying until we find a valid partition of a transaction so here we have an example of a partition of a transaction where we can break up the original transactions to smaller transactions this is this is

**00:02:55**  the most important thing that we've talked about now I think in four separate times and I'm gonna simplify it which is that if when we talk about how anonymous or how private a transaction is we can take any particular input and any other input or output it doesn't really matter you can take you know a handful of inputs you can take a handful of outputs you can take any partition you want and you can ask how likely is it these partitions this these these

**00:03:28**  components are related and the magic formula which is on the Left written clearly in math terms on the right in English terms it's simply given a particular combination you find all of the possible possible valid partitions that include that particular combination and then you divide by all possible valid combinations so for example if you are concerned about a specific transaction and you want to ask is input for an output six in to what extent are

**00:03:59**  they related how likely is it that they're in the same transaction or you could do it you can find all the partitions where I four and O six are a part of that and that could be the number twelve there could be 12 those in total and you divide it by the total number of possible valid combinations of any kind which could be hypothetically 267 and then you get yourself a number like four point four nine percent and you can do this for any input against any output or anything of that nature and two big things we talked about subset sum is the ability to do exactly

**00:04:31**  what we just talked about finding inputs and outputs that match in the size and the bail number is the number of possible ways a set can be partitioned and we know that the bail number grows very quickly and the subset-sum problem is computationally very difficult for large numbers so today we're talking about something different which I'll admit is a very philosophically interesting topic it's a it's a very abstract way to think about things but

**00:05:03**  it's the concept of entropy so a cursory look for the definition we get a few different ways that we use this word it will see the exact way where it should be in the word cook purposes of coin joints but a one example for example thermodynamics which is the likely thing you've heard is that the quantitative measure of the amount of thermal energy not available to do work which is kind of interesting kind of an abstract thing to say another thing you might have

**00:05:33**  heard as well as the measure of disorder or randomness in a closed system another thing you might have heard is and this is actually the one that's somewhat more important is the measure of loss of information in that transmitted message but we're actually concerned about something a bit different than exactly that but similar enough that entropy is valuable so one way we look at entropy is we can you know I was thinking a lot about visualization of entropy there are many good ways to

**00:06:05**  think about entropy but on the right we have a solid where all the atoms are very close together and on the Left we have a gas and in the middle we have a liquid as you see here the atoms are spread out and more I guess you could say random and so we would say that on the right we have low entropy and on the left we have high entropy but maybe a better way of saying this this is what my father told me and he said he's a physicist he said that it's imagine your

**00:06:38**  own bedroom and a state of low entropy is one where all everything in your room is very neat and clean and organized all the shirts are together all the pants are together all the pillows are together everything is very very partitioned and naturally as you live in your room and if you don't do the work to to maintain this this cleanliness then things tend to just sort of spread out and go all over the place you have a book on your bed you have the sock in your your the bathroom all sorts of a

**00:07:08**  mess and that's what we call high entropy and there are some some interesting laws these aren't exactly the laws of thermodynamics because they don't matter for our state but there are two things to consider the first to consider is this principle of conservation of energy which for us matters because we deal with with conservation of energy in it in Bitcoin namely that Bitcoin is always conserved in the transaction and the second is that the state of a closed system is that it tends towards a higher entropy a

**00:07:40**  good way of imagining this is that if you take a bottle of cologne and you spray it in in a closed room as the time goes on the cologne is not going to exist in one place that the particles the molecules of the cologne are going to go throughout the entire room as opposed to concentrate in one area where they started in the bottle of cologne so as I said before with Bitcoin energies conserve the left hand and the right hand must always match so when we have a change of state in which

**00:08:12**  transaction transactions change the state of Bitcoin ownership remembers to the other we know that coins are always conserved so that's kind of a cool remark and and now we're talking about something very different but but but very interesting which is Shannon entropy so Shannon entropy has to do with information theory and much less to do with physics and the concept of Shannon entropy and it shares intuition with Boltzmann is that is that it's thinking about how to

**00:08:51**  explain this okay so suppose you need to uncover a certain English word or five letters you managed to obtain one letter for example the letter E this is useful information that the letter is Coenen English this provides little information if another hand a letter that you discovered is je the least common letter in English this search has been more narrow and obtained more information I think a good way I watched an excellent 20 minute presentation specifically on entropy and I think a good way to

**00:09:22**  condense it is it it it it's it's the number of the the number of questions you would have to ask binary questions you would have to ask to get to the information that eat that you want to know but is currently unknown so it's also been abstract but will only read that so we define the Shannon entropy of a a piece of information a as these sum

**00:09:56**  of probabilities of all the different possible states it's lucky for us that in when we're talking about coin joints we don't value one type of coin went over the other we don't value one or addition as being more likely as another therefore we don't need to work with those probabilities but this is the technical definition of entropy and and so for the case of what Lorant brought up is he's define entropy as as that has log2 of

**00:10:31**  the number of possible ways you can partition a transaction so the question you might ask is why is it log 2 why is it for example not the natural logarithm which is which is almost log 2 but it's not quite why is it not log 10 well it turns out it's love 2 because in information theory looking we're concerned with information being represented as bits so it makes sense that when we when we say something has a Shannon entropy of 2 what we're really

**00:11:03**  saying is that if you could ask to binary questions and get valid answers you would know the original information so the information is distorted in such a way where you have to ask to binary questions that's what the the number the entropy number of 2 would be and likewise the number of 3 would be that you have to ask three sequential questions binary questions in a row to get the valid original information Lorant gives some examples so in this case you gives an example with 6 5

**00:11:34**  inputs and one output and because there are no ways to consider this transaction apart from all of the funds moving 202 there's only one possible case so the entropy is zero in other words we wouldn't have to ask any binary questions because it's already into turistic week so it would be easy for anyone to know who gave money to o2 and what happened here here's an example where it's a little bit less clear so so

**00:12:06**  now there are two possible interpretations of this transactions what are the two possible interpretations well here's the first one maybe yellow gave money to himself and then green gave money to herself or it's one individual and they gave money to themselves those are the two possible cases and so we have an entropy value of 1 and lastly we have the example number 3 where we have two inputs four outputs here's the first case here's the second

**00:12:37**  case because the values are the same it's like a coin joint we can see that you can replace those two values and then of course we have the obvious case where it's all in one individual because we have three cases we have an entropy of one point five eight five because there are three cases okay so we're on rent receipts to define a few terms which are interesting intrinsic entropy being the value computed without any additional information no additional relation so

**00:13:10**  consider the transaction outside of the blockchain so this is what his his script was doing when he was just taking one transaction at a time and calculating it the actual entropy is the value computed considering additional information on watching so you know was there any address for use was did the output then get merged with another output that's revealing common ownership and then there's max entropy which is kind of an interesting one as well the value

**00:13:43**  associated with a perfect transaction in coins run with equal outputs and inputs that are similar to the original transaction and he calls these this type of transaction tuples I believe 100% sure and so from there he says that wallet efficiency is the intrinsic entropy minus the max entropy expressed in bits and the blockchain efficiency is the actual entropy minus the max entropy and I guess the reason why he says this is because the wallets cannot really

**00:14:13**  know what the actual entropy is because wallets are non blockchain analysis companies they don't have very sophisticated tools on hand so the wall efficiency is purely looking at the intrinsic versus the max and watching efficiency is actual versus Max so his own results in print in in doing this was he investigated 97 million transactions computed entropy for 98

**00:14:44**  when 59% of them and was not able to process 1.4 1% and the reason why is pretty obvious because everything we've talked about in the in the past few weeks with the coin joints in Oakland but having to find all of the partitions of a of a coin joint it becomes a very expensive task when you talk about many inputs and many outlets so as we stop cried gopher for many many transactions so of the transactions who did process eighty five

**00:15:15**  point four seven had a null at repeat which means that there was no question about the inputs and outputs being linked fourteen wanted each you had entropy of greater than one so they were ambiguous transactions and one point eight nine percent had an entropy of greater than one point five eight five as good or better than a corn joint so yeah yeah I think I think we'll probably leave it there for now and open up Thank

**00:15:46**  You Aviv after your presentation I got more confused of least important questions but let's let's try to let's try to figure that out because I'm not sure we looked at the exact same source I was looking at the gist what did you look at yes yes yes all right

**00:16:17**  so yeah I am I was mainly concerned of the first one the last two way I just just went through but I get the transaction the actual data is in the last two is innately what you cited here no I think I was mostly focused on the first one as well I mean I could be wrong when everything I just talked about was the first one okay so the very first thing about the first one is that

**00:16:47**  it so that the number and you know the number of valid sub mappings you hear in your presentation added it to D added the full mopping right when when it's only one person transferring money to himself but he actually did not add it to the calculation of n is that is that what

**00:17:18**  you remember exactly okay one more time so so the transaction itself when it's just one person it is he did not add it to the calculation of the end you know the number of valid sub mappings oh oh he absolutely did

**00:17:50**  okay I mean even Adam gives unaltered it under the geese that that should be added anyways it's a not important question I think it's a it's it's better to add two because that's definitely a possibility anyway and another thing is that I I was immediately assuming that it was Shannon entropy too but then I noted it under the gist under comment and he did not seem to know what I was

**00:18:22**  talking about why am I talking about Shannon and why am i calling each a non entropy and I was like okay I just missed remembered I I didn't know why I was assuming that but now in your presentation you actually went through it that hey this is actually the Shannon entropy do you know is this the Shannon entropy or or or do you know what where my confusion is coming from here yes so

**00:18:53**  it would not make sense for it to be any other kind of entropy other than Shannon entropy so the problem is that entropy is used for very different things in science and Shannon entropy is concerned with information theory and that's what we're concerned with as well so you know if it was really Boltzmann when we use the Boltzmann constant because he didn't use

**00:19:24**  Boltzmann's constant okay that's that's an interesting question would be nice about or would be here good answer to that anyway I think these are the least important questions here do you guys have have anything or or should I go forward okay go ahead then Adam Gibson I

**00:19:57**  have my own opinion on on this what I'm going to ask you guys but Adam gives on was critiquing it that well what about pay too and point transactions and what about all the different kind of interpretations of all the transactions it does not seem to toward I mean did you guys read that conversation and what do you think about that so I did I

**00:20:29**  didn't read the conversation and I think that it's it's not part of the scope of what this what this paper is trying to achieve so I don't think it's important so for example if we knew that 1% of the transactions were paid joins then we would have to add that as a caveat then we have this tool over here but then in 1 percent of the time you have to use a completely different tool to

**00:21:00**  understand what's going on so I don't think it changes very very much anyone else yes I think that you need to assume something when you analyze the transaction otherwise there are no way to to get any conclusion for example if you say okay there is an aristocrat says that the inputs belong to the same owner

**00:21:33**  the same wallet yes I could say no that's not necessarily true so that doesn't mean you have to discard or reject the heuristic the realistically system is still valid because most of the times the inputs belong to the same guy right even when could be the opposites attract so you need to assume something right otherwise the transaction can have lots

**00:22:08**  and lots and lots of interpretation even the most simple and obvious transaction could have a lot of interpretations yeah and that's exactly why I don't actually understand how any blockchain analysis is like valid considered valid I have an

**00:22:38**  even stronger opinion in defense of this research because as far as I understand it just doesn't matter because this research wants to break down big transactions into small individual transaction parts and all the heuristics all the different kind of interpretations can come only after the parts the specific sub mappings so you

**00:23:10**  can only apply them to D Sub Pop ings you cannot apply any interpretation cross Harry sticks even with pay to endpoint ban the receiver participates in the coin join itself that would be that would still give a valid input and outputs sub mappings like a subset some right like like the same sum on the input side with receiver

**00:23:41**  and the sender contributing to the same contributing with different inputs but that still gives the exact same subset on the output amount so I believe Harry sticks and different interpretations of the transaction just not only is not efficient to to be part of this research but it just doesn't need to be because the subsets are just independent

**00:24:12**  concepts from that they do you guys agree or or am I miss taking here Lucas set it right you just you have some assumptions and this works perfectly if you just assume a few things pay join is outside of the scope so you just say that you're concerned with only things that meet those assumptions yeah but my point was even if you assume pay join the the subset sums the volleyed sub

**00:24:47**  mappings don't wouldn't change with that assumption you wouldn't be able to incorporate that assumption because it's instead of the sender merges two queens it's the sender and the receiver merges together two coins in the same subset sum and you know it's it these these heuristics these interpretations don't happen cross sub mappings so III at

**00:25:21**  least I cannot come up with any such example where when these interpretations could mess with this scheme itself that's my point here I think I understand what you mean yeah I agree could you explain it because I it it's obvious that I'm not explaining it no I barely understand what you mean sir I don't think I can do any better job all

**00:25:52**  right I mean why do you mean like the the amounts of outputs and I mean it's some way you like clear from that with such a little amount of inputs and outputs that I don't know it's like yeah I'm not sure I probably can't explain it

**00:26:25**  any better than you did for example this I you and me participating in a paid to end point transaction I put in one Bitcoin you put in to Bitcoin and three Bitcoin comes out to you now if we put this pay to end point transaction into a coin join in itself that that does not that that still of all its submarines the one Bitcoin input to Bitcoin input and the

**00:26:58**  three Bitcoin output that's a completely valid sub mappings what voids one is looking for so it won't be like like I put in one Bitcoin input you put into Bitcoin input and somehow you only get back to Bitcoin output unless I get back on Bitcoin output right so the the the input sums and output sums of every sub mapping has to add up to the same amount

**00:27:30**  and and that's that's why I don't think this is important anyway I understand what you're saying now you're saying that you could still use Boltzmann to parse all the page wines that are separate in the coin join and you can figure that out later if that's what you mean to say yes like it exactly yeah I agree and now

**00:28:00**  I have two topics left out one is that is a nice one you know let me let me read but as illustrated by conjuring pseudo who attack this metric face to detect privacy leaks occurring at the lower level of specific inputs and outputs and we just talked about conjoined Sudoku last time and it's it's interesting that you know it's it's claimed but the research was never real

**00:28:32**  history this is the classic example and I was saying that this was actually cited by so many places and never really looked into it that much anyway the other thing is not suck we we always keep coming back to nap sock and I think this might be the very best time to come back to nap sock here because if you

**00:29:03**  look at the entropy here is the log 2n that only depends on the number of valid sub mappings right nothing as n is the number of valid sub mappings and the look to is is there so so this is what only depends on but we can improve upon it a lot because knapsack actually gave us a mathematical model on on what s to

**00:29:36**  look at knapsack not all only looks at the number of total valid sub mappings but the input input links input output links output and the output output links links means like probability of links and you talked about this miss Aviv and and this is this is the final picture here right like like you have to

**00:30:10**  incorporate the these links between each other oh my god the baby is crying because I'm talking too loud so let me say it quickly so you have to incorporate these links into your entropy calculation and you get a much more accurate anthropometric with with with incorporating the knowledge in

**00:30:40**  knapsack that's my point I have a question that I think Lucas might know but I'm still confused as to why using log to make things valuable for us like like yeah I'm not I'm not seeing the utility of this of this of

**00:31:14**  this approach I mean it's the same as we talked about before it's exactly the theory that I have in this slide right here what's you know what's the big you know how are we gonna make use of the fact that we're applying log to to the because the number of combinations that you have is 2x I don't know how to say this is to today and exponential you

**00:31:46**  know to and so if if you have the number of combinations you applied a lot of the love to and and then you get the the this number that gives you how many bits of entropy you you have in that transaction are you satisfied with this

**00:32:25**  answer well I'm just trying to think into my head how I'm gonna use log 2 in terms of terms of maximum solely or usually how about entropy of 3 and entropy of 4 because there were nine partitions in one and and well I think I'm not doing the calculation but anyways the point is if I have an entropy of let's say two and four does that mean it's twice as private is that

**00:32:57**  the idea here so it's I don't know why lock to but I I have a good feeling about the logarithm part of the log for sure because if you think about it that you have five inputs and five outputs and let's say you get ten combinations and if you have 10 inputs antenna outputs then you you don't get 20

**00:33:27**  combinations but you get something like 100 or something like exponential number of combinations and but ultimately the links between the inputs and outputs and input input output outputs are are not that so so there is only 10 inputs and 10 outputs so that there cannot be so the number of combinations may be

**00:33:58**  exponential but you don't gain that much more privacy just because the number of combinations exponential so let's throw a logarithm at it and actually that's what I thought how how the Shannon entropy came to light to that you know it just just Oh let's throw a lot because it seems right III thought it was an intuitive thing but now I I don't know but anyway the logarithm is very

**00:34:28**  intuitive here because he with this you can compare two transactions more accurately of course it's just an estimation but but more accurately does that make sense not exactly I mean you know you could also divide by 10 right I understand that you're saying that the number of partitions grows exponentially but you

**00:35:02**  have to convince me why the privacy doesn't grow exponentially what you're seeing right now is the privacy is growing linearly as your your subsets are growing exponentially yes not exactly linearly but more like linearly yes because the number of participants aren't growing exponentially so it's it's not fair to say that that well it had ten participants in this transaction and and

**00:35:32**  so your anonymity growth exponentially right but the efforts that you need two or ten you miles they grow exponentially I mean Mountain View power you need to spend to randomize so if we look at this so maybe cross a financial aid room yeah that I would say that's another question here

**00:36:04**  because here the assumption is that it can be the anonymous no matter what is the number it can be the anonymized that's why Botsman cannot be computed to to larger coin joints so so so we are operating under the working assumption that everything can be the anonymized in no time and there is no computation or complex team worked here

**00:36:44**  I would love to explain more this to you guys but the baby's crying and it's because I'm too loud sorry okay so why don't we get more questions anyone else have a question they want to ask can you change the slides I don't know which one was it I had a question about it a

**00:37:18**  little bit more today yeah this one can you explain a little bit more about these results yeah sure so Lauren took roughly a hundred million transactions and tried to use try to use try to break them down subset-sum do they figure out

**00:37:50**  all the partitions and then compute the entropy right so find in for every transaction and of course most of the transactions it's easy to do this so that was the case from 98.5 9% of transactions and some transactions it was it was too time-consuming and so of the ones that were computed a majority had no entropy which means there was no other subset apart from just the

**00:38:20**  transaction itself 14.5 2% so it is very specific thing you wanted to ask about know exactly the what is these the the last two things exactly so 14.5 2% had an entropy of equal to or greater than one so that means that the transaction had two possible interpretations because log 2

**00:38:51**  of 2 is 1 right and then 1.8 9% had an entropy of greater than 1.5 A's so at least three interpretations or more okay yeah I got it now thanks Monica so we would say that eighty five point forty seven percent times ninety eight point fifty nine percent is the total number of transaction which is a very large number it's likely about eighty percent of transactions that were that were in the pool had zero

**00:39:22**  protection completely deterministic okay thanks yeah that explained by questions so you know what I was thinking about like the whole meaning of this entropy thing I guess I kind of get it if you have a value of your entropy of one that

**00:39:52**  means that you have to ask one binary question in terms of figuring out the correct mapping and if you have an entropy value of two it means you have to ask to binary questions and so forth if you have three then you have to ask three minor questions and I guess this this does make sense with transactions that really do involve only one person or or two people but I'm not sure how I

**00:40:23**  would apply at scale so so for example I don't see the benefit of applying it to a wasabi coin join I'm not sure I mean I say see the benefit I think the anonymity said is a much clearer heuristic it's Laura seventy-three yes summer a t-shirt okay a sense to apply to the possibly

**00:40:56**  transactions but you can't because it's computationally infeasible but it would be really interesting to see what are the results there okay yeah I agree yes yeah wait I am happy and the entropy yes there is this entropy of the

**00:41:28**  transaction right and there and then there is this level of Nikki ability let's say that you show us that is is interesting too but also in the second part of this gist collection the visa matrix of I don't remember the name but it's a matrix of let me when we find it

**00:42:04**  and a link probability matrix of a transaction the if I understand I I didn't read it carefully yes but I think it is a matrix that for each input and each output calculates all contains the the probability of a link between the input and the output I

**00:42:37**  can be ground because again I didn't read it yet but it it could mean it makes sense to me so I think it is it is a good a good tool to to apply against well I think this is what the the thing this thing is already done

**00:43:13**  okay I mean I I can be long but it would be interesting to do in fact we can we can select one of the smaller muscle transactions and see if it is possible to to run this is to should

**00:43:52**  three-dimensional matrix because you need the input input links the input output links and output output links has lots of paper says it oh yes very good but computationally I think that's extremely

**00:44:25**  expensive now it is it isn't expensive it isn't more expensive at all because what man relies on identifying the sub transactions and the links between input inputs inputs and output outlets are calculated by looking at which sub

**00:44:58**  transactions that things are in and divided by the totals of transactions so computational work here is identifying that sub transactions or the sub mappings same thing and it's not calculating the links that is the first thing here

**00:45:34**  yeah so you got it yeah sure oh by the way you don't have to be in ASMR mode too you can shout what paper would you like to to look

**00:46:08**  into next week okay so if you don't give ideas then I'm going to see a few papers and just shout which one would you like so okay for me researchers in entropy Wonderland the

**00:46:39**  review of the entropy concept a crypto economic traffic analysis on the bitcoins lightning Network [Laughter] vikon joy as used in dark coin does not bring food anonymity yeah yeah it sounds interesting

**00:47:11**  yeah next Harry sticks on Bitcoin privacy Wikipedia page next beepers from a blockchain analysis company it's not a paper it's just whatever we choose next topological analysis of the Lightning Network next by I'm not an entropy I

**00:47:43**  think this would be very similar to the anonymity loves company our paper may be a little bit more technical but what similar philosophical one I have no idea but it that one sounds insensitive interested to me too I agree ok did I sense that everyone agreed on that who

**00:48:14**  did not agree on that I I vote for that too I think that's very interesting all right I guess that settles it next week we are going to peer review the paper by I'm not an anthro pissed okay thank you guys for the party spirit you and for your

**00:48:49**  patience for listening to be in hit summer mode okay thank you guys thank you thank you hey guys you know the recent story about someone who calls and by phone and a boy a little boy say hi

**00:49:22**  the so the the the update the caller say hey boy it's your man now she's not she's busy okay and your dad he's not available he's busy and what are they doing they are looking for me okay

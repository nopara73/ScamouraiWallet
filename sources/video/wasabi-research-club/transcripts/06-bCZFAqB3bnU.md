# Wasabi Research Club #6 - Coinshuffle++ with Tim Ruffing (Part 2)

- Playlist index: 6
- YouTube ID: `bCZFAqB3bnU`
- Video: <https://www.youtube.com/watch?v=bCZFAqB3bnU>
- Duration: 1:28:14
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  yeah all right guys we're here with Tim roughing one of the authors of the coin shuffle plus-plus paper to talk about privacy so this PowerPoint and the presentation team will do that himself and not a lot just sit back yeah hey if sorry if this will look Vietnam but they had to send my slides to to our reef to

**00:00:32**  share the screen sorry I can't click through the slides he needs to do it could be local to it but maybe just pop up a few things on the slide piece maybe like actually the the the entire slide after we are the next thing yeah so this is your puppet cameras but this is just

**00:01:04**  to show you a little bit how ours four things here so we have a transaction right and fellas on the left and she has a key and you have maybe some pizza dealer on the right and and again Ellis's change address which is trust C here and then D sub transaction as well at the face I inserted this check mark things basically two signature re well and then we send a little bit car Network and natural cycles validated and so on so I think this is all the things

**00:01:37**  that we need to get in and also here I mean I included all slides because I had to anyway but I am told you to tell you that privacy is important right and that you have a lot of privacy issues for example the malls on public looking at the blockchain and yeah even worse you cannot leak addresses to each other just by looking at links on the blockchain so maybe go to the next thing you had a

**00:02:13**  lot of things yeah link address to cou you know that stuff and then you can continue with the other tools and yours you'll know know know that stuff when it's huge we have that stuff Yellin demise you for you the DMS you for for-profit actually so

**00:02:45**  proving privacy in the air have some picture with some privacy technology so this is just to show you where where quadropple stands this big picture so yeah so actually I could basically puts coin draw and instead here probably and

**00:03:15**  it would be another picture the basic idea here is that with coin drawing or coin shuffle and fun mixing and charnival also tumble bit is the same category we can't do so much in terms of privacy but we are pretty compatible with the cone because it works currently in Bitcoin and of course if you if you want more privacy you can have fences here enlarged truths and Technology expectancy Lokesh

**00:03:48**  but this will never be integrated in VidCon I guess so yeah and then there's some something in the middle maybe that I can briefly mention in the end here which is like which is when you shuffle if you if you can have amount privacy in Bitcoin by adding something like potential transactions them mixing suddenly gets better and it can have better promise even evolution okay this

**00:04:21**  is a conjoint seminar so again you can quickly go over the slide because I don't need to explain you how mixing works we do it via a multi-input multi-output transaction that you all know as a conjoint the interesting thing here is if you kind of if you want to do this transaction yeah Alice Bob and Carol need to come up with a new list of the freshness of output addresses C prime a prime B Prime in there in a way that should nobody can

**00:04:54**  can tell which one thread which of these needs belongs to to achieve zero next [Music] yeah and the way we're gonna do this is peer-to-peer mixing protocol and this option fee maximum protocol this controversy is what what speeds up your mixing as just if you look at it as a parameter it's it's a protocol we have a

**00:05:25**  number of participants and this example if four participants they all have a input message the message was are a prime B prime C prime D prime and like in our in our code next thing exam but this would be those would be the off to the trusses where it appear on the right-hand side of the control transaction and our Peter Piot mixing gives you is his output is the thing on

**00:05:57**  the right side is basically a short list of those input must such that no one can tell which wizardry loans to which user but the messages will all be public next right and the trust model we want to have here is really a peer-to-peer trust moments that there are no there's not much at rest of the the peers don't trust each other

**00:06:28**  into some random strangers on the internet hole should be the case third party rattles what I mean that is we don't rely on anything like like total provide anonymity so in this example here now look at the left hand side NSF Dave could be malicious and this means for anonymity that anonymity said it reminds the set of honest users so

**00:06:58**  Bob and Carol still have of annuity among each other of course now they only have anonymity set of two because they can't have together with the attacker right just possible next because exactly we have those links here so if the attacker controls LS then the attacker knows that a prime is Alice's address and you take a controlled safe then he knows that T

**00:07:31**  prime states address yeah can't provide a little-bitty with those two addresses but as I said like Bob and Carols together the new media set up through in this example with the leather property that we want to have next to anonymity is terminations simply means the protocol terminates and the presence of licious users which means that there should be users that can stop us to can that can stop on students from finishing

**00:08:02**  the protocol the only thing we assume here is what I mentioned last week in the informal discussion about suppose already determination we assume that there is a positive board but what do we mean by that it's basically a server in the middle of where we all connect to and the server handles the podcast for us and because we are in this peer-to-peer trust model we don't really trust the server for liberty but

**00:08:35**  we trusted for termination instead and in practice as we said if the server is malicious or just broken then the tears won't be able to finish but nothing bad happens they could just switch to a different server however no matter how this server is the server can't break another machine so how does it work it's

**00:09:07**  based on a DC mode which is a road which is very good sense for timing cryptographers Network and I'm talking for network is a Viet named for the following actually rather simple concept saying you have again three users now and assume these three users have pairwise shared keys and the keys are

**00:09:42**  the numbers on the on the triangle here so for example Alice has a shared key with Carol that's the number one the red one key here and hear an enemy pair has a chef of it in now endless on the top she also has a message and I suggest a bold thing she is a one bit message which is also one now what else this is

**00:10:13**  Alice takes her message to one and adds up the thing in the parent is the two keys shared with the other parties the blue key at the red key let me get one plus one plus one and if he if we work in the pitch fields or basically you can think of X or instead of plus ten results here's just one and then Ellis will broadcast is born and now now Bob and

**00:10:47**  Carol to the same of the Bob has a message which is a symbol here Bob adds T to other keys and broadcasts result and Carol does the same and now if the cool thing now is if we add those three messages up the DEF CON broadcast which is 1 plus 1 plus 0 then this basically means that we have yeah so like if if I expanded if just this result and now we

**00:11:19**  see that every key has been added twice which is kind of clear because it has been added by both sides of the of every of those connections positive so that means that all the keys here cancel out and we are left with the sum of the messages here which is 1 plus 1 plus 0

**00:11:58**  so any fee if you at all so get away get 0 and 0 is indeed some of the messages that users had in mind so interesting figures know that this kind of this gives the user some form of anonymity this very simple setting so we can now we know what the sum of their input messages is but we don't know what part to this song this is this is a form of

**00:12:30**  anonymity basically but this was kind of a very simple and or for the song example because in in practice we we don't want to okay I should follow the slides in practice we first of all if you do want to do this in practice we need to obtain shared symmetric keys this is not hard because

**00:13:02**  we can trust to a cryptographic key exchange this is kind of standard can do the VM addiction strange for example but functionality-wise what we want to do in practices if someone to send just messages read messages for example become a transistor this is also not too hard to do now I shown you I've shown you an example with the bit field which

**00:13:32**  is the field to just basic and viewed as a mathematical field what we can also do larger in tetris abuse but refer that heels with them but most importantly if I think what we've seen in the example is then compute the sum of their

**00:14:03**  messages but if you want to do peer to peer banking we don't want the sum of the messages of the people the entire sent right so we want the list of the messages not a song now what what a lot of proposals and practice to and I think you two there two weeks ago and the seminar here is try to use some some

**00:14:37**  slots reservation for example in this picture here me what have these slots because we have users and assume there was a magic way such that every every user gets a slot in an anonymous way so Alice here the first user she has the middle slot the second slot or pass the first slot carol has the third slot and now for example the puppet will transmit his message and the

**00:15:08**  first slot m2 and I'll be basically what we could do here so you could run a DC net and every of those three slots and next and then NS Yasim forgot to say that Edison so independent the slots where people don't have to sign the satchel since heroes so if you look at their first slot we had the zeros which

**00:15:39**  are basically just some form of padding we could say and and pumps message then they would have two messages but the problem here is we could we could have to message respect to the problem here is that this needs this what I called magic not assignment so in order to to make this work we already need some protocol that provides unanimity in some sense and this is where most of these

**00:16:11**  proposal streets not reservation actually fail and practice because it's a chicken and egg problem you need it in order to get a new materia you need and another melindam was sub protocol this confuse love discernment and because this is hard those protocols in the literature to do Revere's tricks that mostly are not great because they can

**00:16:45**  fail in practice so for example what they often do is that you guess or slop randomly you say we have a thousand slots available and then every user guesses random slot and this kind of works in practice but it's pretty annoying because now instead of running 3ds emails we need to run without sleaziness so we need a lot more communication and

**00:17:16**  even like with a thousand it could be that ellison pop both selects the same slot and then like say they all they both select slot n then installed n we both have not m1 or m2 but we actually would have n1 plus n2 and this is just not tier 2 result that we want so this is not great what we do instead is based

**00:17:49**  on on a idea that it's pretty old already at the picture on the after dissonance and the idea is you go into can I have a question so why wouldn't a lot assignment working since everyone knows about everyone why wouldn't the slot assignment just be decided based on

**00:18:21**  off abetik our ordering of each other of every bus public kids right yes but like the problem is we we also looked appears here want anonymity even against each other right so like if everybody in the

**00:18:52**  shuffling knows that like if Ellis knows that all past the first slot can't get a little-bitty because whatever message appears on the first law that will be pops yes make sense thank you can I ask one question yeah why are finite fields needed if you can do a DC net for one bit can't you do it for ten bits or any arbitrary number of bits just have shared keys that are M bits long and

**00:19:24**  just by you mean just by using X or in sort of fields that's right in general you can do this with these peanuts and this is what people usually do the reason why I need to finite fields is exactly on the slide I'm talking so this [Music]

**00:19:56**  so what we what we do instead of this slope reservation thing is actually it's abusing a method that has been proposed to the slop reservation but we use it to send the messages directly so what we do is we have something could called slots it's not really love something like slots but we have maybe maybe it's easiest think of n slots here we have

**00:20:27**  end users and we have n slots but instead of sending the message in only in one slot and sending zeros and all the other things Alice does here instead is she takes her message and one censored in the first and now she she will send em one squared in the second slot she will send em one

**00:20:58**  to the three in the star slot and so on up to M 1 to the N could you explain why she doesn't lose anonymity when she in the first slot when she broadcasts M 1 because maybe click Next because everybody will do the same so also pop will send em to will defer in the first slot and then to square and the second stall and so on so everybody

**00:21:30**  sends the same in the same slot this make sense so if Bob here's M 1 nm 3 can't he know that M 1 comes from user 1 m3 country [Music] yeah I think the the thing that you're missing here instead we are still doing it this Enid and all of those slots so we still have to check he's they are not

**00:22:04**  in this picture because here I'm on the slide I wrote just what the basically what the input message is to the decedent will be in every slot but just as the example we've seen in the beginning with just single bits in an area of toss lottery we run a DC net

**00:22:34**  with the with the shared keys added so Alice Wilma then in the first slot not simply broadcast a bond but she will send em 1 plus she'll keep the Bob plus red key with Carol and so on plus red key with with user n so only after we've we have obtained all the old rules the first slots of the first column here these

**00:23:07**  Keys will cancel out so just by looking at Alice's broadcast on the network you can tell that my nose in there does this make sense yes so sorry follow up questions so that doesn't m1 interfere with m2 when the yes yes and we will come to maybe click Next

**00:23:40**  yes so you said m1 will interfere with them to here and that's kind of that's kind of true what people have we have all those messages in the the maybe yeah maybe that's that's look at the first mode of you have all the first lot all the keys will cancel out this is still true but still like everybody basically sent this first also we won't get a

**00:24:10**  single message there but what we will get is the sum of all those messages and in the in the second slots in the second column we will get to some of the squares and so on up to the to the last slot this make sense so far when we're doing sums are we doing sums over a finite field or exercise yesterday learning some so violent fields I think this is thanks for reminding me I think

**00:24:43**  this is now and not yet but like yeah we maybe click Next sorry I'm right here it's what you do beat those thumbs yes and sorry I don't have slice for for exactly the thing but well now it don't

**00:25:18**  see the slots anymore so take a leaf so okay now we have those power sums and I think I mean it could go into that in detail maybe later if you're really interested and I don't have slides for this but I really I think it's not it's not super important the thing is here is that if you have this this list of the sums here of those power songs then you can compute the messages again and just in information

**00:25:53**  theoretically this I mean this is not a problem explanation but at least if you look at the number of bits here that make sense right we have n messages all together because we have been users and let's say every message has B bits so if you have the list of the of the power sums here we have n times P bits and n

**00:26:24**  times P bits is also the same amount of information that we had in the initial list of yeah if you just wrote like the list of messages tall so this is the same amount of information and because we used we use a proper encoding like this or some thing is just one encoding of a list of messages you can decode it

**00:26:56**  back and get the messages back and forth for this to work we need finite field of automatic that's why we we do some some finite fields a set of tracks for this this wouldn't work with if you use XO and okay now the problem in the big

**00:27:28**  problem in DC Nazis and that they can be disrupted which basically means if there is one malicious user let's say your purpose malicious Bob could do is instead of instead of sending M 2 and M 2 squared and so on and following this nice algebraic structure that just posted follow Bob could just sent in every slot for example like random values or anything else that he

**00:28:02**  had taught him wrong screw it and now the problem is if you don't want to sum up in the slots of course we can sum up we get some sums but like those sums will be again butchered and yeah even worse because you're doing like n DS units here or this unit and every of the n slots up here stays fully anonymous right because this was the core property

**00:28:33**  of the decedent that we can compute the sum of the messages we can do this here there is not but we don't know who contributed so we can't tell who contributed you just see in the end ok we don't get any message respect like our decoding procedure doesn't work but then we don't know what to do so what do we do then well next yeah in

**00:29:05**  case of disruption break anonymity and well this may sound like a bad idea but let me explain why this actually works and to understand why this why this makes sense we need to have a look at the flowchart of the culture of the run so the first thing we do like everybody generates the fresh with Korn interest this is gonna be output in the the contra and transaction

**00:29:37**  on the right side and it won't be our message in the peer-to-peer mixing protocol then peers to key exchanges the runt if you Hellman key exchange on I don't need to explain you how it works just it makes sure that every every payoff users will have a shared key that they need for the dissonant okay then we run the actual DC net and then we would run it in slots as I've just shown you

**00:30:08**  and then now if if we would proceed like I like I've shown you on the on the previous slide and actually this is not that this is not a real this is this will not be the final flow chart of contra for both of us it will come to that later but they're from you at the moment so if we were to what we've seen

**00:30:40**  on the last slide we need to somehow we need to check if our run has been disrupted the problem is namely that it could be that the run is like disrupted for well how should I or should I say this persuade and so like if you get the

**00:31:19**  if you get the the outputs the only thing you can you can do now is to see if your own message is there right like if you if your Ellis you get those power songs in the end or if we hope that they are power Sam's you try to decode the the list of messages and then you have a candidate result for the product the only thing you can do now you could look at if you're all messages there which basically means that no one

**00:31:51**  disrupted your message can you can you instead of looking at your message although doesn't matter that that's good but instead of looking at your message can you just check if we if these are Bitcoin addresses the or you mean again you could have some some redundancy in there so yeah but doesn't matter because checking if your messages

**00:32:23**  there is just as easy as as anything else yeah let me think about this for a moment the question if if if can be constructed in a way that still valid Bitcoin addresses yes yeah this problem so a I can't the total tax is on

**00:32:56**  the size but what what could happen instead like in the example pop first a malicious guy right so let's say Bob since his message is lost then basically Bob sees all the other messages Bob ceased all the other rows in a sense and he sees all the other messages he sees

**00:33:27**  the list of all the the other messages that the others won't want to send and then he could it's it's not clear from the slide here but and he could construct a special form of messages things that only disrupts for example editors message and not the other messages okay no not okay because then everyone would

**00:34:00**  be able to check if Elise's message is Bitcoin address valid Bitcoin address or not I don't know okay so what Bob sees is pops is just a list of the other messages he doesn't know which message belongs to which user so he sees somehow that m1 is there which is Elvis's message but he doesn't know that it belongs to Ellis but now because he knows m1 he could send such that M 1 is disrupted

**00:34:32**  it's basically replaced by a random message or a message of his choice even and the other messages are not yes so he could selectively disrupt messages even though he doesn't know to which users those messages belong they make sense thank you so he swap he could swap Elise's address right swapped around the mattress to his own address and for

**00:35:02**  example yeah yeah and that's why we would need so long ok what I was saying before is that the only thing L is now at the end of the t's in that round but what she can do is she can look at the set of messages and see if for all messages there right but she doesn't know if the other messages are all there she's she would see some

**00:35:33**  messages there but she doesn't know if for example of celts message has been replaced or not and the important thing at this step here is that however we all like all the peers in the protocol needs to agree whether disruption has happened or not because if it has not if there was no disruption then like this is the case you see now on the slides and then they will go ahead and create the contract transaction

**00:36:03**  for assignment however if one of them like if one was disrupted then what they want to do is they want to reveal the key exchange secret should basically a sandy loam ization step basically means that the all agree like all the peers in the protocol agreed that we give up this round we came up on the luma t in this front and thanks and we discard the

**00:36:39**  addresses that we generated to the beginning we need to give me a moment to convince her that this is not a bad idea why can we discard those well I mean these are trusts so far these are just random it coordinators is right if never told anybody who sent those money there and we will never do it again in the future so it's not a problem at all to throw those away but now because like because given that the key exchange

**00:37:12**  secrets everybody can compute the shared message at the the shared key is for everybody which means that L is now knows the shared key step bob has only with her she she knew that one before because shared key but now she knows also the shared key that Bob had with Carol the pump and the Dave and so on so now basically everything is public in this in this run so everybody can just look

**00:37:46**  at everybody's messages like all the oldest guys will now figure out that oh actually Bob sent and didn't make sense it didn't fit this algebraic structure basically they look at pops pops broadcast in this second Rowan sense and subtract all the the shared keys that he had with the other peers and they like now and then they look at the

**00:38:17**  result and see the resign should be in the first slot m2 in the second slot m2 square and so on and they just can't shake tower ops message was follow this this euphoric structure and yeah they figure out that pups messages don't follow the structure so they know Bob will actually images they can kick them out and start from scratch

**00:38:48**  does this make sense so far yes it's clear for me and then and then if they if no one signs in a particular transaction that's pretty trivial to find right right exactly this that's the case now next maybe then okay is everybody sighs okay great success but if not we can again maybe actually that

**00:39:22**  that that that error could be wrong here I mean in that case we don't need to discuss addresses any better do okay but I do but the important thing is here like yeah if if somebody refuses to sign here then we know that this guy is malicious or at least offline and we can execute him however this is not okay

**00:39:56**  this is trivial to implement them but we actually need to be careful for this case as well because the protocol somehow needs to make sure that if we reach that point where we think that there was no disruption then there was really no disruption to make sure that we are excluding the right guy here but the protocol actually has this property so it can't be the case that everybody thinks that there was not an option but

**00:40:29**  actually and as this message was disrupted so she's evil laughter we refuse design because she would lose money by sending it to wrong address on the corner but everybody else will think that she actually needs to sign the transaction just the protocol also make sure that this comes up yeah okay and this is the basic idea how we provide an

**00:41:03**  annuity and termination at the same time by basically cleverly giving up on illuminae in in case that the protocol is disrupted that we can to me because then we gave up anonymity for the single run we can figure out who's who solution and we can you can kick him out I'm side topic of fresh message needed

**00:41:34**  so I like what I told you now is basically the entirety of the protocol is this why this works with giving up on the limit is because we have those kind of fresh with Cohen keys right we can't throw them away and nothing bad happens not not for our money and not for annuity but then everybody knows that I wanted to use this address but I never used it in fact so I can I can give up anonymity for this one and this works

**00:42:05**  because we can generate the dresses and can discard them generate new ones and so on but what if we if we want to send messages that are that are kind of fixed that are not too random Bitcoin addresses and maybe a useless protocol beyond Bitcoin for example two confidential documents like such as confidential document as on the slide here I would call this a fixed message and it turns out that this is not

**00:42:40**  possible so if we if you look at features of key to keep mixing prana concept before I told you you should provide anonymity they should provide termination and now if he adds support for fixed messages as a third property and contract loss plus provides anonymity and termination rate so if he had support for a fixed messages next then we can ask is there protocol in the

**00:43:13**  section of all these circles in the middle and what this turns out you mean hmm what this admonition mean termination means that the protocol terminates even if there are malicious Pierce answered not termination would mean if there are malicious years then the protocol just doesn't finish or it

**00:43:49**  is important is maybe it should have been called successfully so you can imagine that the protocol that doesn't provide termination basically it for example it tries to start mixing with the DC net and then it notices all that what's this well fails just pods okay so

**00:44:21**  we fit aboard if it notices that there was disruption then that would mean termination is not not insured right well okay yeah so I think Adam like currently wasabi does not guarantee termination right because if a cointreau doesn't happen wasabi bands a coin and then reopens the round and more

**00:44:52**  malicious people can enter the round so but one way to make it guaranteed to terminate is to only allow the same participants and then exclude them so that it converges to a smaller and smaller number isn't the termination is to basically being able to identify the malicious party no no in this case I'm saying specifically a given F malicious peers okay can you tell me when wasabi

**00:45:25**  will do a coin join and in the case of coin shuffle plus plus the answer is 4 plus 2 F rounds and in the case of wasabi is just when we've banned enough people and there are no more malicious peers so but wait let's go back to

**00:45:56**  termination you just said that that if if the round aborts then isn't that that means that it aborts in a way that you cannot figure out who was the malicious one I think termination in this case business that it's successful that eventually there's a coin joint yeah I think what you're what you're mixing up

**00:46:29**  here is when when I say anonymity and termination your particular termination I look at the entire probable so like teeth the entire protocol provides termination and it does so I like the inner working is that it tries to to run once and if it sees that this run doesn't work there are these thoughts okay so that but like when I say

**00:47:01**  termination I look at the like the entire protocol in the black board as a black box doesn't matter well that for the doesn't totally yeah very for hanging on it but I think it's important so does that mean it could still be possible to provide anonymity with big messages if successful termination of the entire protocol is not a requirement but what is the requirement is actually

**00:47:33**  to being able to identify the malicious peer so maybe maybe let's finish the slide and come come back to this question and maybe it's answer then maybe not and so what could be interesting is to have a protocol in the middle that has all those three properties but it but it turns out this is not possible

**00:48:06**  interestingly there was a protocol called descent at CCS that was supposed to be in the middle and has all the properties but it turns out it doesn't provide anonymity so like if you if you he would code it exactly like it's written the paper to provide termination and fixed messages and this anonymity

**00:48:43**  answer your question no no my was that if you can you can identify the malicious peer they make that really matter if termination happens or not of this protocol rounds because you could happen okay sorry go ahead that's that was pretty much it okay again when I say termination I don't

**00:49:15**  talk about it don't mean termination of a protocol run of a run that that can be aborted I mean termination of the entire frame like the entire frame with a big loop so okay so would them okay so if you can identify the malicious peer but you don't exclude it but create what you

**00:49:47**  have to create a completely new protocol and from that you exclude it that would mean that it is a terminating protocol okay fine let's go okay just to clarify coin shuffle plus plus is a circular protocol it has four it has six rounds total six steps and then four of them are repeated every time someone disrupts right yes yes and that's why I like a

**00:50:23**  look the entire thing like with the circular ringing it provides termination I think this is all I I wanted to say you yeah okay and and hey I can actually show you how this annuity attack on long distance works and I don't need to tell you a lot about the same but think it cancer be instructive the only thing I

**00:50:53**  think you need to know is that like the three points on top dissent precedes broadcast drones the outcome of the protocol is revealed to all the users in the last podcast and also a network attacker sees the outcome of the proper code of the last podcast outcome so to remind you what is the output of a or the outcome over into P mixing protocols just a list of messages now let's say we have Alice Bob and

**00:51:28**  Carol and they all have their their fixed messengers their documents and opposite honest guy here and we are the network attacker now what we do is we we listen we just let the users run the protocol we listen to the to the messages presently as natural attacker and we only interfere with it in the in

**00:51:59**  the last broadcast of the of the first run so what we do is the block we talk pops message because your network attacker we can we can do this but if you see it you just don't forward it to the others which means that he has a method of attacking we learn the list of messages that people wanted to send these are the three documents here on the right hand side this is the the right hand side here and on the

**00:52:30**  slightest an eft attacker so here we see what's going on we see the list of messages but we don't know yet which message belongs to which user but okay now we brought Bob so now what happens is because you've blocked Bob's last messages and the proper call is supposed to provide termination the other remaining part is like hey listen Carol they need to somehow start from scratch right and they to a second run of the

**00:53:04**  protocol and now because Bob is not in the protocol anymore taking I'm out because he appeared to be malicious to the other two parties Pop's message won't be there in the second run so and now it but the attacker can do is he just looks at the font come off the first one and the second trial in compare stop and he will

**00:53:35**  just notice that the missing protocol the missing message is the two gray one with the confidential mark on it we can see announced that he blocked off he knows that this is the message from Bob this makes sense probably okay a few

**00:54:07**  feet over to ask sorry I was just blanking out it so how is it that you can figure out okay there are multiple

**00:54:45**  things here so yes I didn't explain you how descent works and works differently from from what I see nuts so basically it's a little bit like or it's it's pretty similar to the contract the one that you also discussed but my point I understand it it doesn't really matter right so it detected a that I show here

**00:55:22**  what equally be true if we if we would try to run if you would try to use fixed messages in control itself going to be exactly the same issues really how the protocol looks like but in the end of the proper call at some point you need to review the messages right so what do you take er here does is in the first run it like it

**00:55:54**  just looks at at the protocol passively until the last translate basically he observes all the messages of all the people that then she just he just sees the outcome of the protocol which is the list of messages and the father there's nothing wrong with it because he it doesn't learn which message belongs to be chosen this might mean a dumb question but how practical is it to block someone from from the protocol made protocol I think this really

**00:56:24**  depends on the on the net on the network setting every like usually if you want the right protocol to be secure against what folks like to work attackers and we actually assume that network attackers can agree it can do much more attic and not only block messages they can also replace the duplicate them and also stuff of course you can ask heuristic that in practice usually we the abstract

**00:56:54**  away from from this question just say like look the attackers super powerful because we don't know what how powerful he actually is now but now if you if you look at the contrast of this and specifically I told you that we have this palette and pot in the middle that handles all broadcasts and the reason why we do these actually def better

**00:57:28**  efficiency and now it's getting interesting so because he didn't want to trust this London bond in the middle of the server and the middle fond of the Mitty but if you if your fingers around the middle being the malicious network attacker then family it's very easy to block messages right it's just don't follow it and like think of I think last week I mentioned a simple example of IRC server broadcast

**00:57:59**  messages to everybody else so basically in this setting if you had a server you can always claim or look I didn't walk didn't send the message she's offline whoops um now so we're just stepping if you only feel so yeah okay efficiency and

**00:58:34**  they're cool next okay now this is the flow chart again that we've seen and now the title of the slide says naive why not if because this is actually not a lot of truth I think I started this explanation of the previous slide some actually because I was confused on the

**00:59:07**  slides yeah okay let's count communication rounds and communication rounds are here broadcasts so we need one protocols for the key exchange desert desert this is a symbol here right here okay then we need one protocol to run the actual these units and now I guess now is the crucial part because we all need to like all the

**00:59:39**  peers now needs to increase on whether the protocol has been disrupted on am i told you this example where you can selectively disrupt messages from from peers so to avoid this in the 90 favor would needs another broadcast here just to check that we all agree on whether they're worse disruption or not because as I as I explained to you earlier the only thing you can do it you can look at

**01:00:11**  this on the out front of the protocol and see if his own messages there but he doesn't know if the message of the others are there so to make sure that we all agree whether there was disruption or not we would need another broadcast round here and this is the broadcast that and then once we all know whether there has been disruption or not we need one more broadcast either to broadcast

**01:00:43**  signatures on the contract transaction watch who revealed the key exchange secrets depending on which way we go now okay now in contra 4 + + so sorry can you go back one step yes so and if we look at this now if we count the broadcast these are basically four broadcasts and every run right no

**01:01:19**  matter which which way we go now what we do instead in contra los + next is we skip we want to avoid this broadcast at the disrupted box here and how do we do that next by introducing another broadcast here huh

**01:01:51**  so so far this doesn't make a lot of sense right because we still have for broadcast it currently replace one broadcast by another firm crust the let me explain you why this makes sense next okay let me first tell you why what we actually do so what we do here is it like the first broadcast that we introduce now is basically a commitment cryptographic commitments to the T seen

**01:02:22**  inspector by with time interest the roast of the that appears sent and the TC net so we first sent a commitment next and then we sent the actual dissonant contents the actual rows so why do we do this the idea is basically it is that now we

**01:02:54**  get this following relationship now by doing this we get the guarantee that if there is a if there is one or the serious message is disrupted then all of the messages are disrupted and the other way round this basically means that now instead of needing a broadcast route to to check if

**01:03:26**  to to track with the others if there has been disruption what we what we now can do instead is really just looking at our own at all output so you look at all of the look at the list of messages and see if your own message is there and you know if you're all the messages say then all the other words and equally you know if your own messages it's not there at and also the other messages on

**01:03:57**  they're so yeah and the rest of the slide was just formal stuff not interesting here so now let's look at an example go back please yep so if now protocol would it's a run so let's say we have a first run of the

**01:04:28**  protocol and now having boxes of for prod costs and remember that the DC net round is now in the third position right because we first sent the key exchanged and the second fingers commit whoa did you see that vectors to the messages then we sent the actual DC net measured the third round this is what I mean when I read TC and then in the end we heat her to the intercept the signatures

**01:04:58**  around or of the revealed of key exchange messages and now let's assume like okay this first one is disrupted next and remember the disruption happens in the DC no transyl that somebody sent in this unit round this round is disrupted the round is disrupted anyways what starts a second Tron and would need another another four rounds

**01:05:29**  if you go back again sorry so this is the this is the IE thing and now next what we don't control plus plus is if you actually want to type like this runs and to reduce the number of overalls so now the idea is basically we run two rounds of the first one and then we already start a second one it's not clear yet if people needed or not but in

**01:06:00**  case the first one is is disrupted then we can just switch to the second run which is the the example here right and then maybe the the second one actually is not disrupted and okay we have started already at the retron just in case and then okay but the second one works run-through so we can just support the third one this is how we pipeline this and now look at this red line here

**01:06:35**  this is how the how the information flow is basically from the from the first one to the second one because the first one can remember the first one was disrupted right so after the after the fourth message of the last message of the first one only then we learned who is the malicious party because this is where we reveal the secrets and note now this can

**01:07:05**  see this from the red line now this is exactly the point in time it's still so it's still okay to exclude the malicious guy no for the second one because now the malicious guy that excluded the first run counts dropped the second one because we managed to exclude him from the second run before me before we each the DC thing for me to reach to DC message face does this make sense he's

**01:07:40**  asked if this is okay make sense to me great and and this is the reason why we wanted to push the DC metro to the third probe cast instead of the second so this was the thing I've ever owned you on the previous slides read the information we run key exchange then already DC net and

**01:08:13**  then we need to check with the others if disruption happens then the diziness round would be in the scene that message within the second round but here what we act what we here do is through this commitments of DC net and then sending that we see not only in the third round he be moved to DC no to the third round we make this interleaving of to here possible yeah now if you if you count

**01:08:47**  the number of rounds that we have F malicious users then we need four plus twelve broadcaster ons and this is better than previous work just for original code travel which was just often Efron's so what's your yeah and that we can every night doesn't vectors would basically to set up today when June here on the slide and compare this to the previous protocol control fool and at

**01:09:22**  least in this setting plus plus it's much much better control as you can see under on the craft so yeah for example for security a number of you point out on the papers 5050 notes there we are still below 10 seconds into something and then crunch awful original coin shuffle was like almost three minutes of this sitting next yep next

**01:09:57**  okay and then just I think this is maybe should have been called limitations of coins on actually photos for this audience fear puts you you're probably aware that handling unequally inputs is a like if for was a very bad idea right because like if you had to a transaction like it's like it's on the slides here it and everybody could just every Excel observer even control cell that pop

**01:10:33**  like the one point can go back so yeah so if everybody looks at this transaction can just sell that P and P Prime belong together right there's no there's no privacy if if we do my if conjoined with unequal inputs and tempt and we all know Adam has much better suggestions to do this but this is still obvious limitation of contracts okay and

**01:11:06**  also this is more subtle what we what we also can't do in in current shuffle plus plus is the following so actually I don't want you to mix your money right you want to also to pay with your money so hope you could have tea idea to you

**01:11:36**  can or cannot do this you cannot and I will tell you why the United payment in the conjoint year like there's a pizza restaurant but address our and he sent Co point one Bitcoin to the pizza restaurant and then she he sends the remaining silver problem because back to in prime which is his change address and our like if you if you just think so most server you need look at this

**01:12:10**  transaction I mean of course you can you can see that zero point one is zero and I belong together but you couldn't tell whether they they both belong to a B or C however the reason why it doesn't work is small subtle namely next now look at what would be the messages that we have

**01:12:42**  to send to the peer-to-peer mixing protocol like in the contrary just non-conscious applause plastron we would just send the output to us which is R and B prime here now would basically have two messages in the peer-to-peer problem mixing protocol one for R and 1 for y Prime and now these messages are not just a simple the T

**01:13:12**  addresses because he also needs society amounts there right because like the amounts are not implicit and more like in the previous example where everybody has one Bitcoin like team rounds are nothing to laugh like a lot message said need to be mixed but here they would need to be mixed so basically since two messages and one of the messages is to pair our comma zero point one and the

**01:13:42**  reason why this doesn't work is now that the zero point one is is a fixed message it's nothing that you can discard and then throw a new random one right just doesn't work either because does that matter what really matters is that the output address is changed so it's like the message is not not the zero point on

**01:14:14**  the messages or 0.1 if you next you message or to zero point one because Robert gave you many addresses yeah but it's all think like a it is we had this side topic right is our fresh no message is actually necessary can we do mix so it can be to fix messages and the reason why the answer was no the reason was

**01:14:47**  that an annuity is problem so functionally it your rights you can trust like if the first the first one the support that you could vote it and then we start with R 2 and C 1 but then it could be that there is an attack anonymity now I'm sorry can you repeat that in the

**01:15:21**  had a few slides with the under the title side topic are fresh fresh message just necessary right away very shortly it's a contestant for example but the message it's fresh is just one component of the messages fixed ok but the attack basically applies to two also messages

**01:15:52**  [Music] you really need to loosen Lumet into certain also how would you pay someone [Music] you typically only connect can you repeat so typically you only get one address when you have to pay someone so yeah ok yeah this is what I like if I write the paper I would call this an engineering challenge and put the

**01:16:24**  despite yes of course then you need to but the your I don't know what it was saying is you write the practice to solve the problem it's just that it's kind of trouble but you need to recipient support and this would be another topic even if it would be possible either like if you if you do a conjure with 50 bodies then either you ask the pizza restaurant so give you a

**01:16:54**  49ers resist which is art me but works and well you have something like 32 and pop in derivation and so on very like [Music] since the rest everyone would give you one master [Music] almost a public kid and you can just derive an arbitrary number of virtual addresses from it so just to reiterate on the problem here is that when you expose your messages

**01:17:27**  then of course you don't expose the between addresses but what you expose is that you want to send 0.1 and 0.9 and then what you could do with that is that well I guess this descent failed because the peers where were malicious though I'm just going to send one Bitcoin in in the failing ground but you know you

**01:17:57**  could you could assume honesty and and if if honesty yep and then I mean it's not very robust but you can nobody I see what you're saying let me let me repeat to make sure I get the right thing so what you're saying is basically a be optimistic I try to like the first run try to do the pavement and then but if

**01:18:31**  this first run fails then go back to simple mixing without paying yes yeah this you're right this principle would work it's a good question how robust this is and practice but in principle you could do this all right thank you okay and now like this is the final words here on the slides I think so this

**01:19:05**  already like if if we are in a system where we have confidential transactions which was the cryptographic technique to hide the amounts on deterrence actress like the amounts are not on plane stolen plane but are in morphic comes in cryptographically once then suddenly those mounts because there are commitments these are not fixed messages anymore those are this can be

**01:19:37**  rear-ended - physically so you can take a commitment and like you can commit to the same amount twice and the commitments look totally independent of each other then this problem with the fixed message goes away and then you suddenly can mix up a simultaneously and also like and attentive protocol you use when you shuffle which is full of work and also you you of course get rid of

**01:20:09**  the previous problem that you can't mix unequally most and you can also mix equal amounts and suddenly mixing is so much nicer and better see if you could hide the amounts but I think this that I have one more more theoretical and less practical octet you know what what does really

**01:20:41**  termination mean here termination means that everyone signs but the not deliver termination it termination is that successful broadcast happens so now there is a shoe with double spins yeah right yeah we detect the double spins and then we have to run the whole protocol again yeah but if you are a minor then everyone has to be online

**01:21:12**  until confirmation joy at the end around yeah the problem is trusted you you don't you don't figure it out so quickly right so and don't write essays I've shown you on the slides basically the protocol is finished as soon as you get the signatures of the control message at the concert elections from everybody else

**01:21:44**  then you have a signed contract then if naively then you think like the protocol is finished I just need to broadcast the transaction to the network now and then at once do but yeah like in reality people could double spend maybe a minute later or so not sure how realistic a minute is if you're mining here's the smartest way to be double spent here

**01:22:16**  would be that you divide the network like one half of it knows about the correct transaction the other half of it doesn't know about the correct transaction so the the the peers cannot really agree if the protocol was disrupted or not how do you like everything this season I mean it's it's I think it's a problem with every control finger it so I mean if I if I

**01:22:50**  broadcast two transactions like two six and six peers at the exact same time then they are propagating on the network in a way that that that the man who will splits and then a minor has to come to decide which one was actually the real transaction right now I mean my Christmas if you have seen this taken

**01:23:21**  wasabi or somewhere else I see double spent possibly Cohen joins like maybe a year ago I could not figure out what to was that okay I always wanted in practice I mean like if you of course you can do this attack but it's pretty

**01:23:51**  pointless for the attractor I don't know it's just super annoying yeah it's like you know other schemes those are working in practice don't even and your denial of service protection right Android this this is like a new level of theoretical attack so I it's an engineering challenge as you would put it yeah I

**01:24:23**  mean it would at least say it's not the end of the world but like even the even if people do this attack actively you can what you can do is wait for another minute or so and like and if you have if you haven't seen a conflicting transaction four minutes well okay and you can be like actually the the peers can also then then we lay the transactions right like a fault is it's like if one of the piece of the

**01:24:55**  protocol sees a conflicting transaction could relay it to the others basically have proof that okay okay yes yeah that's my point would there be but you wouldn't see because the nodes don't broadcast to you but but yeah you can relay to the others and like if but it's kind of running time perspective kinds of annoying right now I told you okay like you know 10 seconds I'll tell you oh you need to wait another 20 seconds

**01:25:27**  just to make sure there's I mean if if others really a transaction like that conflicting transaction then would that I mean you would have to trust the other peers that they are not lying about the conflicting turns oh no because they can only the transaction those are theirs so they would be the the the the guys who are disrupting the

**01:25:59**  round so yeah never mind I think like I think you could just assume that like if this transaction exists and it's signed it's already not okay guys okay so maybe

**01:26:32**  I'll ask a question if that's okay Tim in the yep well you can usually ask the speaker to go back to you can pay depending on how many malicious piers there are that's a

**01:27:06**  good question so basically which basically means four rounds right and you know you know the protocol protocol needs four plus two F rounds if you have F malicious users so you can already is like using this number you could just scale it across but the problem is that

**01:27:38**  this is entirely the right answer because here when I say there are no malicious uses that's also here means that they are all produce ponds of right so like this is also at some party turn I need to decide when when somebody is offline it's um the time off and now inserting here

**01:28:10**  basically we don't need the time off because you assume everybody

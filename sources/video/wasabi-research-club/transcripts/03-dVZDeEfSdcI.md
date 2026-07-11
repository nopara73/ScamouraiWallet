# Wasabi Research Club #3 - CoinShuffle

- Playlist index: 3
- YouTube ID: `dVZDeEfSdcI`
- Video: <https://www.youtube.com/watch?v=dVZDeEfSdcI>
- Duration: 1:14:54
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  excellent today we're talking about coin shuffle practical decentralized clean magazine for Bitcoin so let's get started so we're looking at a 2014 paper by Ruffing Marino Sanchez and Kate here's the other paper itself last week just a reminder we talked about sneaker coin joint and the summary was that we could have a non-interactive coin joint

**00:00:31**  between two participants if the proposer if one of the two participants assumes likely UT exo-m's tweaks a revealed public key with a difficult and shared secret and then it takes this partially signed Bitcoin transaction and broadcasts into a public forum where the other participants may sign it when they see it so essentially we talked about non interactive coin joints so far we've talked about knapsack who enjoyed snicker today's coin shuffle and then

**00:01:02**  next week's will be decided at the end of this call you can find out everything on our wasabi research club github okay so we're gonna reproduce last week's topic which is the problem with current coin joints so the problem that we talked about last week we retire on this week as well is that they require coordination so last week it was more about interactivity this week it's about coordination so coordination is a you

**00:01:33**  know is potentially a problem because of things like privacy or the fact that the coordinator becomes a central point of failure so the question today is going to be can we create coin joints without coordination just like last time we talked about what it would take to to create a coin joint and really it comes down to knowing the inputs the outputs and the signatures now if we think deeply about this it's not just about knowing inputs outputs and signatures you know inputs and outputs change

**00:02:06**  outputs aren't necessarily anonymous so participants can can declare their inputs and declare their change outputs but we also have to find out all of the participants mixed outputs so there are anonymous outputs and we need to find this out without having them reveal that the link between their outputs and and the fact they belong in the coin so if you look at how wasabi does this with a coordinator well wasabi uses what's called secure

**00:02:38**  multi-party computation or essentially just your signatures imagine Orion blind signing of outputs in order to allow for outputs to be anonymously submitted so users first that will register their inputs and they'll have a blinded output signed by the server at which point later they will submit the unblinded output to the coordinator and the coordinator doesn't know who is the

**00:03:09**  person that submitted the the output only the that person is valid because the coordinator did a blind signing of the output okay so coin shuffle in summary is just wasabi without the coordinator so using descent protocol for communicating anonymous outputs by participants and we'll look at that briefly and then well there are no

**00:03:40**  questions so far right or girl comments no okay so when chef Allah so we can imagine six participants in particularly one imagined and ordered six participants so we'll have that the left the red individual is the is the first and the last participant is the purple and there's all the participants in between and so just it's for the purpose of illustration it's easier if they're

**00:04:12**  colorful and so essentially what we want to do is that these participants they want to submit their inputs they want to submit their change outputs but they also want to submit a blinded output and output that no one that is completely anonymous to the rest of the participants and they want to do this without a coordinator that is essentially controlling how this goes so essentially what you have here is what what the cord room will look like at the end is it should look like a bunch of inputs from all set participants some

**00:04:42**  change outputs and some outputs that are of equal size that we don't know who they belong to so we have six ordered participants and we have an anonymous coin joint output so it's trivial to get the change outputs done and the inputs done because those can be linked together and participants don't have to hide the fact that they are the ones submitting that information now we're going to see how a participant in this case is going to anonymously submit a an anonymous output

**00:05:13**  so in this case what we have is we have a the first participant is the regular sprint so if you look at this colorful little blob in the very middle is the red address okay that's like the unencrypted red addresses right in the center there and then what the red participants going to do is that person is going to encrypt that red address against Purple's public key and take that encrypted data and encrypt it against blue as public Heat and so forth and then that data is encrypted against green's public key and so forth and so

**00:05:46**  what you have and this is familiar to some of you it's like an onion right so it's it's a layered encryption so it's encrypted against purple blue green yellow orange so then red will take this blob and pass it to the next person in line which in this case is orange right now orange will decrypt one layer because orange it holds the orange public key so orange can decrypt the layer from Red's address and simultaneously add oranges address also

**00:06:18**  encrypted in the same onion scheme being encrypted first against the purple key then the blue of them the green and then lastly the yellow and now the orange has two blobs just to pass on to the next individual or I'm just going to shuffle them so you know just like this and again yellow now is going to submit his own address unwrapped the two layers of yellow on the orange and the red and then again encrypt everything so

**00:06:50**  that it's layer to give the next three participants and shuffle and send over to the next layer and so you know things repeat over and over again and finally what happens is that purple who's the last individual has all of the addresses and can and can has no idea who they belong to so from the perspective of purple only purple address is known to be to belong to it every other address belongs to

**00:07:22**  someone else and it's not clear who so for an oranges perspective you know only the orange address is known the other five addresses aren't completely a mystery and from yellow it's the same idea and and from red and that pretty much is you can you just go but because I think it's incorrect yes go back like two more or something yes so so you see right now

**00:07:53**  yellow only has three outputs three three onion encrypted stuff but actually it's everyone broadcast so okay sorry go ahead I know it's incorrect but I can't explain any time yeah okay yeah so it

**00:08:26**  definitely can be incorrect I don't to claim that I'm hundred percent but I think the idea overall were and the aim is so that in an ordered fashion can submit their addresses and not have the address linked to them and it's done exactly it was sort of in this sort of way yes yes I think I think what a davis is

**00:08:57**  telling us is correct because that's this saying that i understood what i read that the paper everyone i mean you you decrypt the previous participants with your private key because the the message was encrypted with your public key because previously there is an announcement phase where all the participants share their public keys so in this order you create these onion

**00:09:32**  layers right and is that how how this is telling us now allison is correct is that as you said first the announcement announcing the public key so everyone here aviv igor lucas max oh I don't know if you want pseudonym or sorry Rafael

**00:10:02**  and me so everyone announces are his own public key and everyone has to think up a message or or an output right a Bitcoin address and we have to encrypt that Bitcoin address everyone has to encrypt it in a specific order so first what we've done to Igor than to Lucas and so on and then we broadcast

**00:10:33**  all the encrypted messages so that's how you can shuffle them that's what is well no because no I what I understood is what a Vives is be saying that it is an order it is in order yes and the messages is passing one by

**00:11:04**  one and everybody the creeps the the the the coins with their with their public keys shuffle the the encrypted addresses yes and pass that to the next one so in the end the the latest one the the latest participant not the one in the in the finalist step or I can finally

**00:11:35**  decrypt all the the addresses except of course the one that belong to do him understanding of if can you go back to to read my question is at this point okay good go to the next one at this

**00:12:07**  point orange only has two or has all the encrypted messages only two that's what's incorrect Orange has oiled encrypted messages everyone encrypt their message in a specific order and broadcasts all the messages red starts decrypting the layer the the the upper layer of the messages and Shaffers it

**00:12:39**  then orange starts decrypting his layer and shoppers so all the messages right everyone has all other messages all the encrypted messages that's the point it actually seems like what Adam is saying makes a lot of sense so there's no reason why everyone couldn't submit all of their addresses like the way red did it

**00:13:10**  so that mmm-hmm and that's how you can put it into a peer-to-peer network where everyone root costs every message it's it's not really passing Allah maybe maybe it can be but it's not really passing around the messages from peer to peer but broadcasts all the messages for everyone all the time I did think that

**00:13:41**  it was sequential in that red had to communicate to orange and orange had to communicate to yellow and yellow had to communicate to green and that it wasn't like I mean I guess you could do it publicly because you can keep announcing everything and only the the right person can decrypt that layer but but I didn't think that it was sequential I mean just think about it what if red because in this case red doesn't shuffle anything

**00:14:13**  then he read cannot make sure that the things are suffered correctly right orange can only partially make sure that a two thing is suffered now I actually wrote code for it so I am pretty sure what I'm saying anyway yes can we agree in this or or or someone would like to have objection I'm very happy to you can see this because I think that the point is the same that the goal is the same is

**00:14:45**  that these peers want to essentially mix these outputs and not have connection between who submitted what right okay so um right so here is what I did I'm kind of summarize we thought of because the final okay yeah I mean so

**00:15:15**  the summary is is here as well but the the the the summary is that yeah of what happened is that six participants got together and are essentially submitting their anonymous addresses outputs in such a way where when purple finally opens all six addresses purple can link those addresses to any of the past participants and it's done with like onion layer encryption and shuffling so

**00:15:50**  those outputs are shuffled across participants Adam says that all six addresses are shuffled in with every single step and that could very well be the case but at the end you have six addresses that are unlinked okay okay so so here is the in the paper it's explained so you can see in the top

**00:16:22**  right Alice has this layered encryption and she passes off to Bob for decrypt who passes dr. Charlie decrypt and and you can see this sort of mix mixed network yeah and on the bottom left you have a point row and that's been signed on the bottom right do you have a pointer and that's not been signed because someone tampered with the addresses and added an invalid address to the coin joint so the big thing to

**00:16:52**  talk about with Quinn story of you can I show maybe you understand it better based on that sure [Music] I am sharing my screen right okay do you

**00:17:25**  see it yeah okay then then it's a problem because it's not in the video just like last time I had to cut it out and anyway very quickly then we have Ali's Bob and Satoshi and everyone broadcasts their public keys I run this and it's going to be this this comes out

**00:17:55**  so everyone broadcasts their public key and then these onions and these are the the encrypted messages and rip that for everyone and then everyone starts to decrypt their messages one by one everyone starts to decrypt all the messages orderly layers and and at the end we get we get get a script like like

**00:18:28**  a bitcoins Bitcoin scripts right that's that's the Bitcoin address it just creep up key and not a Bitcoin address so anyway if you see that yeah it works okay I don't want to ruin the video with this so so go ahead okay pretty much at the end here the big concern right when you consider getting rid of the central

**00:18:59**  coordinator and instead having peers during this process themselves is is the time it will take and the computational take from the peers so in the equation ax paper they took participants and set them up on a low network and then on a global network with a certain amount of latency from one side of the net to the other side of

**00:19:31**  the network and here you can see the time it takes oh if you look at the local network where there's almost no latency it looks like an Alinea increase in the time it takes with 50 participants you have 30 seconds 40 seconds of time it takes for essentially that we're just best to do the entire dance from start to finish and then with the global network you can see that the time it takes is much much more because every single individual needs to hear

**00:20:03**  the latest state and then decrypt that situation and then pass it on to the next individual who will who needs to then so it is sequential whether individuals are talking directly to each other or in public broadcasting to everyone it's still the case that that these onions have to be decrypted in a sequential way so the more participants you have the more time it takes and on the right there is the average processing time per node yeah so yeah

**00:20:36**  and we also have descent which is what this is based on they also did a similar test of the shuffle time for you know 44 nodes with varying size here it's one megabyte of data of encrypted data that's being shuffled over 44 nodes you can see it takes several minutes so 15 minutes by 44 nodes and over here there

**00:21:06**  was three minutes by by 40 or 50 participants so yeah in summary rather than have a secure multi-party computation with a coordinator coin shuffle a solved problem of constructing a quorum with just participants themselves using this the dissent messaging protocol commercial participants shovel their anonymous outputs until all outputs are made available to all since without a link anybody spent to an output and the biggest drawback is the time cost as the number of participants

**00:21:37**  grows and then the advantages that there's no coordinator to to attack during denial of service and that's pretty much what I think needs to be said about this so yeah believe it that thank you let's continue questions and discussions and then ideas and later on topic for next weekend so yes questions I have a

**00:22:11**  comment well first of all I I think I I don't know what your implementation is based on probably is in a new version that we are not that we don't know but I again I understood the same data we've explained us and in fact there is a very simplified version or very simplified explanation in Quito in Bitcoin talked about it by by team one of the of the

**00:22:45**  creator of this is King III understand the same whatever I read it but anyway that's one point the other point doesn't have onions then who's gonna read decrypt his onions for other people no Ally so

**00:23:18**  in this case the red doesn't creep he only encrypts the the output right increase the output with all the public keys of the other participants in order so the next one in this case the orange the orange one the creeps with his public key it remove one layer yes and just encrypt everything again

**00:23:53**  with the pin and the dead life this layer is the the yellow one right so yellow the Crypt remove that layer mix those call those addresses and encrypt again with yes is what a baby is doing so in the end all the old a our addresses has only one layer of

**00:24:26**  encryption that is the one belonging to the today to that guy what color is that purple I think okay so purple decrypt all the addresses yes except the one that belong to to him and perform just the latest shuffle and broadcast that list of outputs to everyone so after

**00:24:57**  that is the face of the the next step is creating the the transaction so nobody knows what output belong to to the rest I see okay a maybe then III don't know it I didn't understand this properly then schemes work I mean I know that my

**00:25:31**  scheme is working I and now that you explained what you're doing is it seems to me that's working too so and that that results in less encryption and decryption so less Network messages maybe it's faster so yeah okay yeah I think I have an idea

**00:26:01**  here for this scheme because you know if in the first phase I mean in the in the announcement face participants could announce their public keys and also how much money they want to participate with right for example Alice can say this is my public key and I want to participate with one Bitcoin Bob this is my public

**00:26:32**  key and I want to participate with 0.83 bitcoins sorry yes is the media is changing the protocol just a bit right because if everybody knows the public keys and and the amount that other participants want to participate with then what participants can do is creating the outputs yes not only the

**00:27:04**  addresses but also the amount of that addresses using the snap sucks right because remember that was one of the idea that what the the latest proposal that was never published by I don't remember the name of the guy that was with us in the knapsack and episode let's say he said this a new version that I never published that is the participants only know only need to know

**00:27:36**  the amount of the other participants so they can split their outputs in such a way yes that they can create a knapsack transaction right so in that way we could encrypt more than one address but also the amount so you don't need to shuffle right because the idea of oh

**00:28:08**  well yes you need shuffle so you can shuffle but in the end what the purple guy will receive is a lot of output transactions yes with the no only descript but also they did the amount and that will be at not sack transaction so it it could be used for unequal outputs to using what we learn in the first episode

**00:28:39**  and I think that's a very important idea that's a good job Lucas seriously so anyone have questions or should I go with mine okay okay go ahead a vision

**00:29:10**  no you asked you a question first okay it was it was a general question about denial of service or rather simple attacks I mean we can use a central coordinator right to depend UTX those but and we have a feature economic disincentive attack but there are no in coin so how can we defend against okay so that's a really great question

**00:29:40**  it's addressed in the paper and in the protocol itself so the the phases you know there's the first phases the announcement phase then there's the shuffling phase what happens later is that if after the shuffling phase if you get to an undesired outcome namely the addresses in the that are appearing are not belonging to all the participants you know someone added two addresses or someone didn't shuffle correctly there is a way to go through the blame phase

**00:30:13**  where essentially all participants reenact what they did and you can tell if someone did something bad so you can do blame but that also is takes time and it's arguable that it would be it's it's easier to attack this sort of system then now Assadi coordinator is your answer it was correct I just want maybe Trisha easier to say this way that if someone misbehaves that

**00:30:47**  obviously everyone detected because the final Cohen joined doesn't happen so everyone just exposes all the actions that they take with the without their without except their outputs except their Bitcoin addresses so and the protocol can run but because if if you give out all the actions that you take

**00:31:17**  during the run of the protocol to everyone that hey here is my my private key for example I signed my messages with this then you can tell exactly who misbehaved and you can rule him out and you can run the protocol with the remaining honest participants this this is something I have a comment because that try in fact there is some advanced techniques

**00:31:49**  in in in the in the other paper basing it is the conscious plus plus that I'm not familiar with yet but listen civil attacks are hard to prevent in in conjoint right it's if it's really hard right now because in this case for example if you are one guy that participated with multiple identities

**00:32:22**  let's say yes imagine I am red and you are orange jell-o like blue and bla bla bla so there is nothing I can do yes but but Daniel of service attacks can be I mean I think it's not a naive alternative but it works pretty well that is okay someone didn't sign the transaction right it is easy to see to know that so you can just burn that coin

**00:32:54**  as we do try again sooner or later that guy will run out of money probably is not the best way just switches okay I cannot hear anything

**00:33:27**  oh sorry and III for this division never said with the captain I love Britt but I'm the typical self our Sigma max sorry pocket actually I just max do you have some

**00:33:58**  software of feature that needs you when you're not speaking or something like that because I see that you are muting and unmuting in high frequency sorry

**00:34:28**  I didn't hear your your your your question can you repeat please purple the last one changes the address changes let's say red address to his own address then it's going to be red who doesn't sign so you cannot really burn red right so the way we wait but the I can seen I can see the transaction right the

**00:34:59**  final conjoined transaction the final conscience transaction has in this case one two three four five six there are six participants let's say there are six inputs - just to simplify and there is one missing signature so someone didn't sign right so in that in that case we can burn that coin so you can participate again but now with the same

**00:35:31**  coin Lukas the so this is this is exactly what you saw in this protocol unfortunately you can't apply the same banning heuristics as with wasabi so with wasabi you can't ban the coin that did not sign in this protocol if if someone if you end up with an unsigned coin joint there are two reasons either someone is not signing on purpose or in which case you can ban the other part of

**00:36:02**  the coin that did not sign or someone did the protocol wrong right in the case Adam gave purple is the last person with all of the addresses and purple you know dumps Reds address and adds two of Purple's addresses to the to the mixed outputs so how do you know how sorry yes yes yes yes sorry yes I understand now so what you have to do in that case it's actually quite unfortunate is that every person has to

**00:36:34**  reveal to the entire group what information they received and what they encrypted and each and and what they decrypted and and by doing this the guilty party will be revealed but the annoying part is that this also takes several minutes of of everyone sort of presenting what they have and then you have to recursively go through and see which person you know tampered with the

**00:37:07**  the information and if you can waste three minutes of time then you know arguably it's premature dos attack yes it's clear now yes sorry it was a silly question but anyway you remember Adam Gibson tell us right they did the attend yellow service attacks is because someone wants to prevent this for happening and if there is not incentive

**00:37:41**  because you cannot steal money so if the result daniel of service attack is i mean there are no incentives right at the beginning it at least for this kind of attacks so a naive implementation can work at the beginning at least i mean an implementation that doesn't implement any Daniel of service attacks prevention

**00:38:13**  mechanism so it the point is is that with this protocol you do have a blame face and you can't point out the guilty party it's just it takes additional time so all I'm gonna say is is is that looking at the trade-offs of this protocol as soon as we start talking about large number of participants more than 50 we're gonna have pretty severe problems with with latency and I think

**00:38:43**  there's an issue where the longer it takes for round to happen the more likely someone is to lose connection or or or be a part of the problem so I think it's just not practical to do coin joins this way one more thing that's interesting in this is that here the dose protection so here the coin join happens between the honest participants in Vasavi we

**00:39:14**  always forget the state we take down the required anonymity said but anyone can register to that not only those who are who were already registered in the previous failing round right this I'm not sure which direction is the but this might be something that we can consider later on any thoughts on this

**00:39:46**  can you say that again I am sorry understand sorry yeah I was not clear enough so here if fails then the next round is going to happen between the participants without the malicious party in Vasavi if round fails then the next round the anonymity set required anonymity set will be

**00:40:18**  lowered but Bobby doesn't make sure that those people who were in the failing previous round the honest people from the failing previous round will mix do you understand the difference it's a subtle nuanced one but it's it's somewhat important I'm gonna say yes play I honestly do not think I

**00:40:48**  understood okay so there is a round basta be Co enjoying possibly or coin shove doesn't matter the round fares what happens in Queens offer the same participants the same participants will Co enjoying it it is coin shuffle in wasabi it's not the same participants possibly just lowers the required number

**00:41:20**  with the number of malicious participants but still in that round anyone can register okay so two things about that then so firstly coin shuffle if a coin shuffle round fails it goes through the blame face it points out someone to blame and then it does a conjoin another coin shuffle doubt that participates that's that's

**00:41:51**  what I understood yes exactly and in terms of in terms of wasabi I thought wasabi was you know if a coin joint fails it's because someone didn't sign and that that one coin that is didn't sign is banned for example and all the coins try again - that one coin so I guess I'm confused on both issues you are right except the end that not all the Queens who already registered it's not those

**00:42:24**  who re doing the exact same or failing ground without malicious person but it's it's it's a completely new round anyone can come the malicious person is bound but any new coin can come in in coin shuffle new coin cannot come in okay okay so that I had that I understand and I

**00:42:56**  didn't know that was the case and it's a very axis it's a very small detail but yeah yes it's important all right next question what is secure multi-party computation for me because I can just be a Wikipedia it's a question

**00:43:32**  next time baby okay so one more thing that since we are come since we are comparing it to wasabi there is there is a comment from or actually it's not even a comment anyway I'm just going to read it I'm not sure if it's from the paper or or it's a comment from Bitcoin talks so Maxwell

**00:44:04**  sketches a modification to the coin join protocol using blind signatures to avoid the problem of a centralized mix learning the relation between input and output addresses this this is this is the show me and Cohen join just saying and yes it's in the paper now I know this protocol employees the anonymous communication network tour as a blinding as a building block to provide an link ability in contrast coin shuffle

**00:44:35**  provides full resistance against traffic correlation attacks by using a decentralized high latency mix Network run only by the participants so that that's an important point here to write that wasabi realized on new tour identities coin shuffle does not it it's doing a mix you could even mix without tour just on the clear night right it would still work

**00:45:09**  but but actually I mean I was pickling when I when I read the paper and the shout out to hear a link but then the the discussion that I have is I mean we could also do zero link not on tour but on a mix now what that work to I mean well the Queen bear in mind that keep in mind that all the coin shuffle implementations are actually using the server and you know in theory you can use just a bulletin board server where

**00:45:41**  participants are are posting their messages but they are actually using for coordination and those protection and things like that I think so so yes you can say that Kesha is is is is Vasavi with her store and you know what I mean so so yes definitely but but

**00:46:12**  then you will call it coin shuffle because coin shuffle is using a mix night that's the thing about it well I guess the important thing to notice that coin shuffle doesn't make any claims about how we structure coin joints rather just how we communicate right so okay sorry anyway I understand what you say Taliah simply kind of spoke about the positive but maybe a bit further to

**00:46:49**  the stuff to discuss what we can combine cannot psyche with this so I'm not sure I understood the conversation we had earlier so what does it be that we first do a communication around with with coin shuffle and then we get this coin joint transaction and then we apply cannot back to this coin joint transaction or how exactly would that work well

**00:47:21**  knapsack works by splitting the outputs in depending on the amounts of the other participants right so if you know how much the other participants are participating with you can split your output in such a way that after the process I mean you can't use two exactly the same that we've explained us but in

**00:47:52**  the end the the purple guy where they create all the outputs right and those outputs yes when you analyze those outputs there will be more than one trivial mapping to the inputs right so it is basically an knapsack transaction is it clear

**00:48:29**  wouldn't that lead to like spam in the chain which I may use the xhose or would be like some kind of minimal amount minimum amount of for one ugh so that's the trade-off with the knapsack is that yeah it the the better the knapsack the more you th cells you need okay going

**00:49:02**  back to the today to the comment today what Adam says yeah I mean it is possible to use the same technology that in this networks I mean using X or using the X or of exploring all the messages with all the public keys of all the participants and in that case we could remove tour the only problem is that we still will be able to see their IP

**00:49:33**  addresses something that we thought we cannot do I mean it is possible to use that technology to do in so the server will not be able to know who message belong to whom right but the IP address is still there oh that's a very good point because in wasabi the server doesn't

**00:50:04**  know that if some are registers to the Kohen join did he used this used wasabi before or not the server doesn't know because it's on a new tour stream but you if it Konoha if you don't use tor then you have you can tell that that which participants participants which person participated

**00:50:35**  in which Cohen joins so now you can correlate so you you actually have to use tor for Cohen shuffle - yes that's my point yes okay I only have one discussion thing or all other interesting thing that regarding Queen shuffle is that I don't know if you guys

**00:51:05**  knew it but on Bitcoin talk the very first page of conversation was about a replay attack and then Tim Rafi noted that the thing about encryption schemes is that all our secure encryption scheme always uses randomness for encryption to make sure that encrypting the same message twice does not yield the same

**00:51:36**  ciphertext the audit randomness is built in the encryption algorithm itself one does not have to all randomness manually to a message before giving to the algorithm try it take an encryption tool and try to encrypt the same message twice so anyways it's just good to know I yeah

**00:52:09**  so do you guys have any presentations questions discussions ideas or should I move on to something more interesting I have no idea third question just something that we could have in mind that could improve our conjoined transaction is researching if is there any way to identify the offender in

**00:52:44**  order to remove it and and create a new conjoin without that attacker that could be graded I think it's not possible but it could be good to if I don't know if we can say okay someone didn't sign we provide proof that of something I don't know just to avoid creating a new round again so it that would be really good I

**00:53:16**  think it's possible I think it it can be it can be done and not even hard but I'm not sure it makes sense because then what's the attack the attack is that the see becomes the malicious malicious CBI comes and tries to I don't know maybe then I don't know it's a it's an interesting

**00:53:50**  question to explore definitely all right so yes before we would get into the next topic I want to talk about something is that what direction should this research club take now I want to

**00:54:21**  talk about just an idea of how should we how how can we make what's the most was the best thing to to research in Bitcoin privacy and I have a small roadmap ish thing and we could adjust the researches to to that later on right now we will of course as we discussed we will go

**00:54:51**  through the coin shuffle line but after that so I please opinion it it's it's something that that I've been thinking about for a year now and it's getting more and more solid based on the opinions but I would like to hear yours too and and and adjust it so this this is the roadmap to Bitcoin privacy okay very first thing to do is to figure out

**00:55:24**  the most blog space efficient way of mixing coins second thing to do is to figure out how to send money in a mix instead of sending to yourself mixing to yourself the third thing to do is after these things are figured out we have to figure out how to do it trust Leslie fourth thing to do is figure out how to do it in a decentralized way which I am

**00:55:55**  NOT interested in but for completeness completeness this is something that people might be interested in and the fifth thing to do is figure out how to integrate other infrastructures into this this new mixing technology that has just been researched what what are these these infrastructures those are relevant light clients how to do it with a light client how to do it on mobile how to do

**00:56:28**  it with hardware wallets and how how to and are there any ways to integrate it to the Lightning Network somehow and rolling to the Lightning Network or something like this so figure out the most block space efficient way of mixing figure out houses and dynamics how to send in a mix instead of mixing to serve figure out how to do it trust Leslie does this this three strap is is what

**00:56:58**  the wasabi Research cups should be about the integrations and later things are or I don't know it's ten year down the line or 20 so the do you guys agree that this is this is a logical sequence of of research that we could take later on when we learn more things I definitely agree I would it might be a

**00:57:32**  good idea to start talking about what the how we would measure efficiency in a coin joint you know against the block space that it's consuming I've been thinking a lot I know if we have time right now to talk about like the perfect hygiene like this would be my next next topic to be honest that I have sub steps for the very first step so I don't know

**00:58:04**  you should I say the sub steps or do you want to say what you you're saying right now yeah don't just say what I've been thinking about because you know we're all thinking about privacy right now when I when I think about the perfect privacy on Bitcoin given what Bitcoin allows barring layer 2 solutions to me that perfect solution is essentially you know every block contains one

**00:58:35**  transaction and all inputs and outputs from all transactions are collapsed into a single transaction and then there are some optimization happening where people are breaking down their inputs and they have common outputs of similar size and then there's nap sacking and all sorts of fancy stuff but the idea is that the asymptotes of privacy the best place prices could go this is an intuition that could be completely wrong about this is it's just it's just every single

**00:59:07**  block is is it's just these massive transactions that that's that's where I think things would be going and so that kind of points to what Adam was saying about how to figure out how to send in a coin joint as well because that means that if you can receive and send and mix all in one coin joint then all transactions can be coin joints in the future I think it's a so yeah we will probably never get or not probably we definitely never get

**00:59:41**  there but it's a good good idea to take imagine what could be the perfect at the best that that's possible and start to work backwards from there yeah that's a good so in any way for these three steps don't really see yet what the do you guys see the logic between these these three steps that most efficient way of

**01:00:13**  mixing sand dynamics and then do it trust Leslie is it does it make sense I really would like some feedback yes I think that's a nice idea under no it's especially though also you know as you mentioned later with with other technologies like for example lightning Network I think an important aspect here is to integrate getting into second layers and Altos in a private way so doing you know coin joins into a lightning channel factory for example we're doing hyper

**01:00:45**  loops you know atomic swaps out of the Lightning Network in a coin joint um but this summer it goes together with sending and receiving within a coin John Doe not just into a single public key but more advanced second layer of script so the reason is why the Lightning network integration is at the very very end because everything depends on the coin join scheme so first you you really

**01:01:16**  have to figure out how to do one chain transactions and then you can move on to lightning network anyway the very first step is figure out the most blog space efficient way of mixing coins and this is my thinking there are two steps here first we have to figure out how to score mixes and second since fighting the maximum score based on the set of inputs is computationally infeasible an

**01:01:49**  algorithm must be found that performs performs the best in multiple simulations okay sorry you asked for feedback it not totally agree because I know that your goal has been your goal form for probably years right but I mean finding the most space efficient way to make this to build this

**01:02:19**  conjoint transactions but I can say that our goal should be the most private way to create the conjoined transactions I mean probably it is more expensive well yes but I think the the the first filter or the first goal should be to maximize the privacy even when probably is not

**01:02:50**  the most space efficient solution just that that is obvious what provides the most privacy if you if you you know the common greatest divas or you have a set of inputs yes you get the common rate as the user of them and every output gets

**01:03:22**  that right or let's say one Satoshi but rather the common greatest divisor so that that provides the best privacy but this is an optimization problem the best privacy by not wasting that much block space so you know yes that's clear is that exactly the same that I thought when you say it is obvious yes it is obvious but I mean we have to have a like minimum requirement right we cannot

**01:04:00**  was the worsening the the privacy level we have now sorry sorry the point in it it is not easy to know what our users want right what do you know they did sometimes want to be able to make more money and faster sometimes they want to to be able to participate with less money or this is not easy

**01:04:35**  yes so probably it could be more efficient it space-efficient to makes higher coins rise for example for example instead of now we are using 0.1 0.2 0.4 of course it could be more private say all to split all in 0.1 coins right but I don't know is the

**01:05:06**  solution if in they were in them if trying to to achieve a more space efficient solution if that will not require to make bigger coins I mean to have bigger output when the same okay we don't know what okay I just I just have

**01:05:40**  a road map to how to get there it's a my idea is that we take the existing data the existing wasabi data of what happened with wasabi what amounts people are coming in a mix or just existing blockchain data the point is that you build a software that makes this simulation and when I say the first step is how to score mixes what I actually

**01:06:12**  mean is to figure out how to score a chain of mix step 1 figure out how to score 1 mix and step to figure out how to score a chain of mix based on real-world data simulation so right now we are just coring we are not really mixing we put some naive mixing algorithm and we try

**01:06:43**  to figure out we see a transaction chain of a mix transaction chain and we try to figure out how the hell should we score that mix and then we say ok let's use knapsack for that and we run a knapsack for the exact same data that we're on our previous naive mix and then we compare our scores that hey did not suck score better or the previous naive mix

**01:07:17**  score better does that make sense for you yes it makes sense in itself is about testing basically with different algorithm the only the only thing that we have to have in mind progress that giving we makes zero point one at a time yes basically yes people with a lot of money I don't know probably 1,000 bitcoins it's not currently mixing with

**01:07:49**  with wasabi probably yes because it will take if they want to make it right it could take a lot so probably what we see in our conjoined transactions that information is already constrained by our outputs right so that that's it just was a comment yes

**01:08:19**  [Music] have to figure out implementation time that should we take the possibly over the data or should we look at instead the wasabi mix data instead should we look at the input amounts on the blockchain just randomly recently yeah that's a methodology issue and that's something to figure out and now going

**01:08:50**  back to the wasabi research cup because this is the first step that we should think about how to how to arrange the inputs and outputs and we went down the path of coin shuffle I think we can use it for our advantage because the thing is even after we figure out how to arrange the inputs and outputs we have to figure out how to do it in a trust

**01:09:20**  less way and it's like thoughtful it's like it's a really hard problem but that's when the coin shuffle line of research comes in and at the end of that line of research there is cache fusion which is probably solving this problem and which is something that I wouldn't take as it is but I would really love to know the the techniques that they are

**01:09:52**  using so we can go through the coin shuffle line of research which is with this coin shuffle now next time as Lucas suggested we do something about the mix networks and Tim referring the author of coin shuffle suggested to look into the dining cryptographers network it's a paper and then of course coin shuffle plus plus and then cache fusion and

**01:10:23**  after we we look into cache fusion which our hope is that it either solves our problem or provides or armors of us with the necessary tools to to Tucker later the trust lessness problem then we can move on to go enjoin analysis and after the coin shuffle things we can

**01:10:54**  move on to coin Johnny Quinn Joe in analysis stuff like coin join Sudoku boards man maybe an absurd code or or whatever so so we drop the coordination issue we we get into the the the subset-sum issue but we started with knapsack that's that's my idea so and and and at that point we could actually start to research how to arrange the

**01:11:26**  amounts how to score the mixes right that's the first one so this is my long-term idea i have an intuition about scoring mixes that it will be quite hard to do this and you know i know that we can apply some basic heuristics you know for example take the volume and multiplied by the number of participants or this or that but it's it's just not trivial thinking about how to score a

**01:11:57**  mix in especially because if we decide you know some function accurately consumes transaction and then gives a good score whatever function we decide will shape the direction of the mixing in the future so i think that this will be quite a tough thing to not just present a function to score mix but also to justify where this function is the best approximation i I think nap sock is

**01:12:29**  the knob stock paper is a perfect basis for that because what they did there is they counted the likelihood between inputs and outputs to belong together but they also counted the likelihood between inputs and the inputs and outputs and outputs and if you adopt those numbers somehow just wait with

**01:12:59**  blocks paste used and you apply the whole concept to a mix of transit to do a chain of mixed transactions if instead of just a single mix then that might work I don't know I I think that could work like that is it is it is it feasible to calculate the subsets of like a large coin join like efficiently in comedian nah it's a

**01:13:33**  5 inputs 5 outputs that could be done 6 I don't think so okay so of course yes so the coin shove shuffle line at the end with Cash Fusion

**01:14:04**  is this is this good for the next three weeks so next dining cryptographer networks then coin shuffle plus plus then cash fusion and then we can move on to to the first step I agree yes I think that's good but maybe in this slide how about increasing the frequency because I have more capacity to maybe do I don't know to call so week for example it takes

**01:14:46**  time to read the papers and think about and it's not so easy

# Wasabi Research Club #17 - Protocol ACL

- Playlist index: 17
- YouTube ID: `z3G6CUDPr0c`
- Video: <https://www.youtube.com/watch?v=z3G6CUDPr0c>
- Duration: 0:46:52
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:01**  hey welcome everyone to the wasabi research club and this time we still don't have a vivre but luckily we have the wonderful David with us who would like to start this meeting with a joke let's go hi there thank you for the introduce I'm I'm embarrassed thank you so last time you get told that I had the

**00:00:34**  example with the the cat and the microwave and there is another story with Annie as far as I know it may be just a rumor but did you know why in America and the car mirror on the left hand right there is a small text that the object in the mirror can be closer than than they are they look like did you know that there is a text like that

**00:01:04**  on the mirrors no no it's the same story as far as I know that okay a guy went to the court because the mirror you know it's you know it's not a flat mirror because you want to see more so it's it's a bit how do you say that it's it's not convex yes it's convex and convex mirrors and

**00:01:35**  gives the effect that you know that the object looks closer and they he went to the court with that and and he won't so afterwards every mirror car mirror the manufacturer put this text on the mirror that the object can be closer so that's it [Laughter] it's similary the cat and the microvia don't put your get into the microwave because there was one well one judgment

**00:02:11**  about this in the past and there they want to cover their their asses this is how America works in general this is also why they label hot drinks like contents maybe hot or something like that for every one of those there's a lawsuit I think the the hot one had to do with a lady who got like second-degree burns or something by spilling coffee on her lap so now every time you buy a hot drink it says caution contents may be hot yeah and a bag of

**00:02:44**  peanuts has a warning about that it might contain some peanuts let's go into today's show so you guys who ever missed

**00:03:17**  last episode you might you I just wanted to bring bring everyone up to date that right now we are not reviewing paper but so we are not a review club club but we are a research club as the name implies we are researching now and every week we are going to talk about our research progress and just to reiterate the big picture is that we are looking into

**00:03:50**  Cohen joins and we are looking into us to generalize them what's the goal here is that we want to enable trustless creation of CO injuries those have not been enabled in a bird before for example there was this wonderful enough sock paper which which would like to optimize on the number of subsets of transactions but no one figured out how to do knapsack mixing in a trust last way before or blockchain

**00:04:23**  if you had to share coin implementation and no one really figured out how do you do shared coin style transactions in a trust last way before and right now we are working on a solution and hopefully we will find one actually we found and thought about one last week and we talked about a less optimal scheme last week and right now we have two more schemes which which we are going to talk

**00:04:58**  about and let's see what else oh yeah so but what do we really want to achieve is that a user could should be able to register their inputs separately independently and their outputs separately independently regardless of what the input and output desired output

**00:05:30**  amounts are and that's not and that's not not an obvious there is an obvious way to do that and as far as I research went no one has really figured it out there where there are some very complex ecash divisible linkage schemes and what

**00:06:01**  what some some privacy odd coins are doing that that could be useful here too however for coin joints we have a security guarantee that if a user does not see his desired output in the final mix transaction then it's not going to sign which means we can make less compromises in our scheme and

**00:06:34**  hopefully we should be able to come up with something simpler than let's say the divisible akash papers are coming up with and let's go into our very first protocol which is an ACL based scheme it's anonymous credentials light is a paper which we read and modified it in a

**00:07:09**  way that suits our needs can I ask someone maybe each time to screen share here sure [Music] yes thank you let's see our mmm we

**00:07:41**  should talk about it would you like to go through the high-level scheme East one or nothing much yeah I mean I can do it sure so like last time we were we covered basically two schemes like one was kind of broken and the second one was okay we didn't we didn't really go into the details but it was a scheme on so it was

**00:08:14**  a blind signature scheme which allowed to have blind signature on messages which are committed in the Patterson commitment but sadly it's required pairing base crypto and pairing basic crypto is a little bit further and far from what we would like to achieve so and then I think it was you Val or Adam who brought this paper into discussion it was also discussed in the wasabi research Club two or three weeks ago and

**00:08:46**  one immediate thing which one needs to see is that it doesn't require any pairing base crypto which is nice because we can just work on on our regular beloved and sach P 256 K one curve the high-level picture is essentially the same we have a nice commitment scheme which is our beloved again Patterson commitment scheme and we can obtain unlink both blind signatures on

**00:09:18**  blinded commitments which are which cannot be linked to the origin also here we have c1 c2 c3 these are commitments and we can get from a coordinator from a server signatures on these Zeta blinded commitments and so basically this is the high-level picture and remember we additionally need to have this input splitting and output

**00:09:49**  merging functionalities and this can be also achieved so this is maybe just the first high level picture shall I go into the details or what do you want to hear about more Lucas just left and is going to implement it anyway yeah I just want to clarify that it was Nick Jonas who brought this paper up to

**00:10:19**  our attention as far as I know okay all right I so like we can go into the details if you want so like in input registration let's say we shall try do it should I go yes sure I just wanted to say that I would like to avoid calling these blinded commitments and blinded signatures because if you cut these blinded that kind of means the server

**00:10:53**  knows and the user unblind stand which is not the case these are obtained signatures for commitments those correspond to the original commitment and the server never sees the signatures and never sees the t's new commitments but yes they see a scheme actually cause them blinded anyway yeah go ahead they the server does see them signature

**00:11:24**  verification it's just that they're not linkable to the signing protocol yes sorry correct so at input registration it does not see only at output registration hey guys no power here and my internet is calm it doesn't want to come back so I'm just going to go through the easier based scheme so what do we have here let's see we want to as

**00:11:55**  always we want to solve among splitting amount merging how do we do that well it turns out if we figure out amount splitting not exactly correct but in this case yes then we are going to have a mount merging to so we start with user has the UT X so we'd value V so let's say you have one Bitcoin and you want to split into outputs with values V 1 and V 2 let's say that zero point four and

**00:12:27**  zero point six such that V equals V 1 plus V 2 so one Bitcoin equals zero point four and zero point six this is splitting and what happens at input registration user creates and tethers and commitments c1 equals eveeven r1 or is the random factor here v1 is of course the value and we create a number

**00:13:01**  of pairs and commitments and we say we have some fake patters and commitments here from 3 to M which values are 0 and the V I terms corresponds to single attribute l0 in the ACS signature with an empty message with range proofs for each so anyway this just clarifies the

**00:13:31**  notation differences between the AC anonymous credential light paper which you can see nevermind so and you also have to prove the range of each commitments otherwise you could cheat so it's between 0 and 256 bits or something like that never minds right proofs this is what are being used for confidential transactions to the user also needs to

**00:14:06**  prove the sum of the commitments of course the Patterson commitment does that this is just some concern here that how to do that you basically prove that if you give the sum of the or values because then you will have an equation like v1 plus v2 plus v3 if it's in a commitment and with the sum of the

**00:14:37**  random values then it's going to be then that's all patters and commitments work that they are homomorphic so you could you could have a commitment and prove that that the the partial commitments equal to the sum and this is how you register your inputs so now here is the non-trivial part and I only understand

**00:15:11**  the high-level picture here but let's see from this protocol the user obtains and signatures for n commitments in a way where the following properties hold so the coordinator can be sure that the the obtained commitments are committing to the same values as the original commitments neither the commitments nor

**00:15:44**  the obtained signatures are known by the coordinator so this is important because otherwise it could link these commitments the original commitments I and and it just says that the octane signatures are honorable and obtained commitments are running cable to the original commitments so and from here on it's quite simple at output registration user can say let's see the

**00:16:19**  user wants to register 0.4 Bitcoin by sending the coordinator the obtained commitment for the 0.4 Bitcoin for vivan and the DDR value and not quite sure if this this random value here is the same as the original commitment maybe

**00:16:50**  probably I don't know probably this this this new commitment action not probably it definitely looks different than the normal Patterson commitment so just just keep that in mind and of course you carriages are some zero commitments along with the with with the real commitment with with a commitment that commits to the to the real value because

**00:17:22**  the sum will be the same so and of course you have valid signatures for for those commitments that you obtained in at input registration and and that's pretty much it here we there is a long conversation about how many problems this scheme has but but but it seems like we were able

**00:17:55**  to to to fix the the problems of this scheme and in fact we decided to not go with this anonymous credentials light based scheme but probably heat verification anonymous credential scheme is going to be more straightforward approach than the ECL based scheme and this is not quiet

**00:18:30**  worked out as you can see there are no not many formulas here that's because we didn't quite work it out but this seemed to make sense and this will be the this will be the topic next in the next was a B research club and hopefully this will be the very last scheme that we will go through because this should solve our

**00:19:04**  problem in a straightforward non compromised fake and then we can want to I am afraid to click on this because I don't have internet and then we will be able to move on to to come up with the next generation mixing technology and that's it again I'm sorry for the loss

**00:19:34**  of Internet as a compensation I'm going to play a bit of VidCon next Hey and finally the coordinator replies with the the final message and the user can finalize their proof that they actually present during verification and the paper nicely replicates the usual Sigma

**00:20:08**  protocol notation like the first message a denoted a then E and then the a C and okay so if the viewer is familiar with Sigma protocols and illiterate children can recognize this this pattern by the way I would strongly recommend to any wants to read the ACL paper to at least look at the introduction of a base paper first because it introduces a lot of

**00:20:40**  these variable names and it kind of gives a much clearer intuition for why the protocol even works and the ACL paper it's a lot more dense and I mean since it cites the other paper it kind of assumes that the intuitions underlying it yeah so let's talk a little bit about communication complexity here so like one thing one

**00:21:12**  should notice is that this is not just some hash value which could be obtained just by naively applying pH a mere heuristic but this e term has a special structure so it's it's crafted in a special way so that's the reason that the Sigma protocol here cannot be made just non interactive and this gives us essentially a five move blind signature

**00:21:43**  scheme instead of the usual three mode because the user gives here on the server the commitment and proof for the opening of the commitment then the server replies essentially these two messages can be sent at once and then the user needs to reply with this special value E and just after this sending this e value can the server send

**00:22:14**  the final message so this was another sign for us that we might not want to go with the with the ACL paper in the fifth move of course is the signature verification yeah and because in current law sabe um just the chow me I'm blind signature scheme is just a regular three mo client signature scheme and obviously overt or it's it's someone needs to consider also

**00:22:45**  the communication complexity which is kind of more we have more happy than just regular HTTP more to the point it's prone to failure and failure in this case like for the round to actually succeed all of the participants must you know succeed if any one loser loses

**00:23:17**  connectivity everybody has to wait until they come back or the whole round fails and you need to basically start over you know okay so let's finish or is there anything to add or any questions regarding the ACL paper yes I just want to say this sorry guys my internet went away and of course they're recording but now I'm recording again and actually I recorded the whole episode by myself so anyway I think we are kind of finishing

**00:23:53**  the ACL paper maybe now let's enhance and emphasize them why we are more leaning towards the quack paper why we are considering that so far the best scheme we had even though we didn't manage to fully elaborate on the coin merging protocol my understanding

**00:24:26**  is that the quads paper the quads approach is more straightforward and it probably requires less interactivity but correct me if I'm missing something or if I'm wrong yeah that's pretty much it so the one major difference is that these signatures are only verifiable by the signer

**00:24:57**  since it's a Mac it's not a public key signing scheme this is an algebraic Mac so unlike triple zero max like H Mac or whatever it's not built out of hash functions but out of group operations and the this makes it so that it's easier to prove properties about the the committed values very much like the ACL

**00:25:28**  scheme the idea is that you have multiple attributes that the the signature covers or that the Mac covers and but because everything is a kind of simpler it doesn't need to be publicly verifiable this the whole interaction is a little bit simpler you only need three rounds to obtain a credential and then

**00:25:59**  when you go to present the credential or sure what credential I think that's the the name they gave to the algorithm in the paper you make a zero knowledge proof that you have a valid Mac on those values and present randomized commitments to the same values and the the server can verify this using their

**00:26:30**  their secret key there's two variants of this so the original paper by melissa chase Sarah Michael John and I always forget his name I'm sorry introduced a scheme that attribute can only be filled values and in that scheme that means that you need to have some sort of blind issuance and

**00:27:01**  the way that they do the blind issuance is by using el-gamal encryption which is very similar to Patterson commitments just with an additional term that makes it only computationally hiding but it has like the same nice homomorphic properties so basically you encrypt your attributes to yourself you give them to the server with proofs of their valid and then you get back a Mac that you can

**00:27:35**  then decrypt and later use to construct your proofs when you show this paper that each one is showing right now is much more recent paper by Melissa Chase the third author whose name I forgot and Trevor Perrin and this is designed for the bread so this paper what they're

**00:28:07**  trying to do is solve the problem of managing who is included in a cinema the encrypted messaging who's who's a member of a group in a way that the server can't really know and the main difference over the previous paper is that in this mac scheme the attributes themselves can be group elements so this

**00:28:38**  means we can directly use a Patterson commitment as an attribute and since those are perfectly hiding that way if we get it right we can assure that even if there's a quantum adversary the coordinator is hacked and somebody breaks the second P 256k one earth like worst case scenario users should still not be d anonymize

**00:29:08**  about which seems like a desirable property for a pro-ball that attempts to improve on bitcoins privacy problems and other than that this scheme is very similar to the other algebraic mark so that that's the main difference I guess just thinking out loud like one would be able to track the coordinator and get the coordinators Mac secret key

**00:29:40**  would there be any privacy leak so no because there know that the coordinator never sees the actual like the the values in the at input registration you never reveal the actual values you'll name proven zero knowledge that they're committing to the the right sum and the the Mac that the coordinator cents to

**00:30:12**  the user is never presented by the user to the coordinator instead the user produces a zero knowledge proof that they have a valid Mac and that again is like there's no reliance on computational hiding there so at least in theory the coordinator can never be anonymize and even if the curve is completely broken what should be lost is

**00:30:43**  a soundness not not a blindness of this protocol so I mean at that point it's kind of all theoretical because bitcoin is probably gonna be in serious trouble if anybody can easily solve for discrete logarithms on the same curve that Bitcoin uses but let's assume that we can somehow fix this with you know a magical soft fork and even if all of the

**00:31:14**  transcripts that the coordinator saw are then revealed after the fact it should be impossible at least in theory to to link users input registrations to their output registrations right I find it funny that there's a group nameless signal who basically essentially solved the almost word by word a very same problem so like you just need to replace group chats

**00:31:46**  with coin joins and yeah and then basically the same problem applies well actually if you read those parts of the the paper they have a more serious challenge to deal with because they need to like authorized users and D authorized users and some users are administrators of groups and then they need to still have like blind issuance so to them yeah after a certain point is

**00:32:19**  just question whether you have one attribute or two so or or more sorry so they also make use of the el-gamal encryption quite heavily and they prove things about encryptions of user id's and so on so anyway it's pretty interesting can you can you elaborate on the not really a metaphor but what's the connection between group chat and Cohen

**00:32:50**  joins so in this original paper they want to make sure that whenever a user user wants to send a message in a group chat the user wants to convince the server that they are indeed a member of the specific group chat without without licking anything about their identity oh

**00:33:20**  yeah and also the server doesn't actually know who are the members of any of the groups right so basically this is also what what's happening at output registration phase like word by word you just need to replace group chats for coin joints and then yeah it's the same all right but we are not ready with this

**00:33:51**  yet as we need to find out the details but hopefully next week we can also talk about those details which are missing right now thank you guys is there anything else you would like to go through or say about this okay so we can talk about a little bit about how we

**00:34:23**  are hoping to still improve the ISO scheme as this so we didn't touch upon the advantages of the quoc approach than the acs so the main difference here so in the original algebraic mark paper things are simplest there as part of the show protocol the is part of like the outputs of credential presentation are a

**00:34:53**  list of commitments to the same attributes but with different randomizations and those are just plain old Paterson commitments the signal paper so the newer key verifiable and on the schedules one has a slightly more complicated if you scroll down you can see here yeah so M I is the only type of

**00:35:26**  attribute that we care about so mi is the original commitment in our case and Z is a random value that the user generates so the final commitment that's presented to the coordinator in this case is G of Y that's sorry G sub y I that's a generator for one of the attributes we only have one of those sorry we only have two of those and this reminds me we didn't talk about double spending so then you rate the the

**00:36:01**  final commitment here the the Z exponent only applies to this generator whereas in the ACL scheme the sort of analogous gamma term is applied to both the additional generator and the entire commitment so it's as if it's G Y I times a my that entire thing to the power Z so this makes the equipment openings a little bit easier to deal with relative to a CL not as

**00:36:34**  straightforward as in the original algebraic Mak paper but they're like the the attribute values need to be hidden some other way during issuance okay so now that I remembered the double spending a cool aspect of these key verifiable anomalous credential schemes compared to anonymous credentials plight is that it's it supports what's called

**00:37:04**  an linkable multi show and the idea here is you have a single credential and you can present it multiple times and the individual presentations are unlikable whereas in the ACL scheme there's a single signature and that signature verification action is similar to ECDSA or noir signatures in that there's like a hash term so because approach has no

**00:37:35**  traditional hashing different presentations are randomized abow very easily for us it's actually a downside because this means that a user can register an input once and then claim it multiple times and the coordinator would not know that these two outer registrations are actually for the same credential so complication of these this approach is

**00:38:06**  that we have to add an additional attribute for scenario serial number and that serial number would have to be revealed as part of out about the registration and in this way the coordinator can know that a single credential is only actually used once I actually just so I never finished that point about like why the different

**00:38:39**  commitment schemes are sorry I am this is how my brain works so ideally we would like in both of these schemes to prove that the some of the credentials presented the sum of the amounts committed to buy these credentials exactly equals the requested output amount and we have not been able to figure out a simple zero knowledge proof

**00:39:10**  to do this for the ACL scheme because of that pesky gamma term it's absolutely possible in theory it's just that both of us are haven't haven't managed to do that yet so luckily this becomes a little bit simpler using using this approach let's put some pressure on us and and promised the viewers that we will have the solution by the next

**00:39:41**  episode definitely two weeks all right so Lucas are you excited to implement it yes this can but yes excited to because I have to read a lot you will learn a lot in that's good I mean I think that's

**00:40:13**  the main advantage like we learned so much along the way so I think you will enjoy it as well yes I hope so all right how about you guys did you understood everything you always seen Adam that you will only

**00:40:43**  understand if you if you called it so I'm not waiting for that point when I can start holding very true there's a lovely Python library called a pet lab privacy enhancing technologies library it's right it's on github no yes and on pi PI and this is basically

**00:41:14**  bindings for open SSL's like a lower level api's and a petal at P et I don't know how to spell his name I think da n easy is then I think with an A initially but if you just look for pet Lib yes

**00:41:44**  okay cool so this library has in the examples directory an implementation of the ACL signature scheme as well as key verifiable credentials based on the original algebraic mac paper so not the one that we discussed today but the the older one and both of those rely on this gens ekp duck pie thing which is I think

**00:42:18**  it's like a general like the Sigma protocol based [Music] nice where you give like the transcript in full for both sides and it computes the actual normal like final proof values this looks really nice yeah the code is it's not very thoroughly commented but it has comments

**00:42:48**  in all the right places and I found it very helpful to understand some of the stuff especially with the algebraic max scheme and how the blank Ning works I I didn't understand that part in the paper evidently and actually implemented it so which is the algebra and this is algebraic man so this is one of the schemes presented in the original paper the Mac ggm which has a security proof

**00:43:22**  only in the generic group model right for us it doesn't really matter because we don't super care about soundness we have that fallback of coin joint security the other Mac scheme is a slightly more complicated and only needs a decisional diffie-hellman for the security proof and then this like anonymous credentials construction on top of it adds all of the like

**00:43:54**  complicated their knowledge proof stuff built out of Mac ggm but both algebraic Mac constructions are possible I don't actually remember in the signal paper it's like a variant of Mac ggm with an additional term T which is part of the the field and an additional point W that's part of the secret key and if I'm not mistaken that addition is what

**00:44:27**  allowed them to prove it in a nicer model than the generic group model but again for our purposes like we fall back to Bitcoin security first and hmm this is really nice there's also I think Isis Lovecraft has an implementation of the single scheme already I haven't had time to look into

**00:44:58**  it yet though all right very good do you guys have something else to talk about or should we close this episode soon before closing please share this repository

**00:45:37**  I'm pretty sure you can look at the the recording and just just see the repository yes I got it or you might also put it in the comment section on YouTube or something like that all right so max was everything clear

**00:46:14**  silence means yes so here thank you guys thank you guys for de for for two days today's talk and I hope you enjoyed it or if not at least learn something and we will continue towards building better Bitcoin future without making sure no one can spy on you alright so thank you

**00:46:45**  and have a good night bye-bye thank you thank you bye

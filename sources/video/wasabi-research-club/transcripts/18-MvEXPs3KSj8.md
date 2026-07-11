# Wasabi Research Club # 18 - Protocol KVAC

- Playlist index: 18
- YouTube ID: `MvEXPs3KSj8`
- Video: <https://www.youtube.com/watch?v=MvEXPs3KSj8>
- Duration: 1:35:25
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:01**  better you can hey yeah welcome everyone in the wasabi research club number 17 and I'm very happy today because today finally we are going to go through the go through our research the cryptographic primitives of our research and if you have not paid attention to the last two episodes then pay attention

**00:00:33**  today because this is going to be the final scheme that we have came up with and this is what's going to be in Bitcoin in a couple of years time maybe two weeks just a quick overview on on what we are doing right here is that in Vasavi we would like to replace the mixing protocol in order to make the mixing well a couple of things to fix

**00:01:05**  about the mixing for example we could remove the minimum denomination we could reduce or maybe completely make the change disappear in the mixes we could have more blockchain space efficient mixing and we could also make transactions in the mix and how that this this these ambitious plans here

**00:01:38**  requires us to be able to break coins down or merge them together in any way shape or form and when I'm talking about coins here I'm talking about off chain Co enjoying coins which is star which is being which are living between the input and output registrations of the coin during phases so that's the big picture

**00:02:09**  here we have roadmap and I would like to give divert to ishtvan or you while who would like to start Thank You function take it yeah but before we going deeper like a small correction that this is not our scheme so we are standing on the own giant shoulders so we just give slight modifications towards the existing

**00:02:40**  schemes so yeah our added value is I would say almost negligible like just with an epsilon anyway so first we want to provide some lightweight background because we understand that there might be some newcomers who joined the research club or are not as familiar with this key with this scene so maybe we should start with commitment schemes like just a really quick review right or

**00:03:17**  yeah shall we started commitment schemes you well or or yeah I think that's the most logical place all the commitments are the most sexy things so yes so like it's not that important that the that the viewer knows any instantiation of the commitment schemes it the you or should just understand that we have two algorithms this commit wait don't you

**00:03:50**  want to explain the commitment scheme with my article that should be really fun yeah okay ah yeah with sex medium no para yeah I mean this is a special type of commitment scheme but yeah so but but before going into this like let's just give an overview that so we have a function which is called commit and it allows one to commit to a message be

**00:04:24**  with the randomness our and this algorithm outputs a so-called commitment which is denoted as C and then later it allows the commuter to open this commitment and anyone so this is called opening a commitment and they can check whether this opening of the commitment is correct so what this achieves this commitment scheme is that one can think of it as someone puts a pan in a box as

**00:04:59**  Adam says in his example and then later one wants someone put in this pan into a box then they cannot change their mind so this is called binding property but we also want that if someone just has a look have a look at the box then they should not be able to tell what's inside the box what's inside the commitment what message was committed and this property is called hiding and pretty

**00:05:31**  much that's in let's I think suffice is to have for you why do you want to add something for commitment schemes and yeah so maybe we can move forward to max if there is no any comment to commitment schemes

**00:06:01**  I guess maybe just so opening a to finish the analogy opening the commitment is like opening the box you after you promised you show everybody what you put inside the box in the first place and the most familiar example of commitment schemes are hashes with a random string added because there's a difference from just hashes to commitments if you commit to the same message twice normally you don't want to

**00:06:33**  reveal that you committed to the same message twice so that's why you add randomness and it's not just the message yep so that commitment schemes are like cornerstones of crypto but I suppose like 99% of the audience already heard about them so let's move forward to where Linda on max okay lindell's this is like our Bible if you are into crypto then most likely you already are

**00:07:08**  familiar with this book by you telling that and Yonatan cuts okay so what is an H Mac an h-back provides basically data integrity on messages so if you know what is a digital signature you can think of an H Mac as the symmetric key counterpart of digital signatures so one can produce with the K key an H Mac on a

**00:07:38**  message and then later this so-called learn Mac stands for message authentication code this tag can be verified with the very same so note that for issuing this Mac and verifying the magazine he needs to be taken so this is like a symmetric key counterpart of digital signature so this doesn't not provide public verifiability but still it ensures that the message sent along

**00:08:09**  with the Mac ensures that the message was not modified on the on the wire right and H Mac is like I think one of the most important and famous instantiation of Mac's but in the wabi-sabi we rely on a different Mac right anything I should add two Macs

**00:08:41**  so if there's nothing I should add to max then maybe we can move forward to the signal paper so but what did you say just just a question Mac is the symmetric part of what was that yeah okay so like just think of like this would be if this would be a digital signature scheme then here okay you have

**00:09:13**  a general key generation algorithm you generate the public key secret key and then for example here instead of a Mac you would have a sign algorithm which and which usually takes this the secret key as an argument and then it produces similarly not a tag but we call it a signature and then later the verification algorithm in case of our digital signature scheme takes as input as the public key of the issuer of the

**00:09:44**  signature so there's an asymmetry so in a digital signature only does a secret key holder can produce digital signatures but the public can verify the validity of the digital signature given the message and the signature and here only those people can verify the validity of the Mac who has access this risky so this is kinda this is a

**00:10:14**  relaxation of a digital signature or yeah so this does not provide public liability and each Mac is the most popular Mac yeah but in wabi-sabi we we will use and apply an SPO called algebraic Mac and this was I think the most important observation what you've all made that we don't need don't really

**00:10:45**  need blind signatures or digital signatures at all because in a mixing if you apply coordinator then you don't really care about public verifiability because only the coordinator should be able to verify these credentials yeah so this makes this was the most important observation I think so far that we don't need this

**00:11:15**  asymmetry the coordinator issues credentials and then only the coordinator needs to verify it in output registration but now I'm I'm getting to forward it is do I didn't realize that but then I ignored the literature on max for this because I thought it was mostly relying on bilinear groups so it's Jonas Nick again for like the third time we

**00:11:46**  have to thank him for reminding me to to work correcting my misunderstanding and reminding me that I should take a closer look at that can I ask another thing that if the Cayenne does not need to verify then I mean in in show me and Cohen join at least the client needs to verify that the signature is correct but what the was the thing here also here do

**00:12:21**  it later I think it's it's part of the that's addressed as part of the protocol but I think we should save that detail for after we we go over the definitions that we're gonna use because we need those definitions too but the short answer that still in this case the coordinator can convince the client that it gave out a correct Mac or on the message so this is that's the answer thank you and not only that that all the users have a mark issued by the same key

**00:12:52**  so the coordinator cannot produce different like tags for sorry that's an overuse overloading of terminology so that the coordinator cannot use a different key for each user in order to do naanum eyes them later it has to to prove that it's making use of the same announced key so right anyway thank you the only

**00:13:23**  thing you forgot to say is to spoiler I laughed but that's fine okay so let's move to the signal paper right or do we want to maybe cover not this Sigma Nu which one should I shall we think I think first we should go through the preliminaries of the Sigma paper and then if people want to go over zero knowledge proof sand the notation then the first two pages of damn birds

**00:13:54**  introduction to Sigma protocols yeah it's a really nice example so we can depending on how it was we can either skip that or or not yeah anyway if you are dear viewer if you're new to this space and like these two introductory texts are your best friends so Sigma protocols and commitment schemes and zero knowledge protocols but going back to the signal paper so here pick six I think yeah okay this is not

**00:14:28**  that important I suppose yeah let's go over because there were some confusions about like some of the feedback that we got so we might as well define this terminology because we use it later it should be its base okay so we are working on a finite cyclic group you can think of your favorite elliptic curve so this J denotes the point the set of the points of this elliptic curve usually in crypto we use the prime order prime

**00:15:00**  order elliptic groups yeah and and we have this additional three functionalities which allow us to map arbitrary this means arbitrary bit strings to to group elements so we should just have this as a given that such functions exists and then similarly we can map we don't need those yeah okay so should I just keep it yeah I think so okay so we

**00:15:32**  have this and then I think this is the important stuff so now let's introduce what is amor more precisely what is the algebraic back so again we have this beloved elliptic curve group and then we have a key generation algorithm which outputs two scalars in the ins EQ so do the coordinators private key consists of two

**00:16:05**  elements from zq x0 and x1 then the coordinator the can generate max on a message m with the secret key by choosing a random point on the curve and then outputting well here they denote it as Sigma so it's like already you can think of it as some kind of signature so this Mac this algebraic Mac consists of two points you and due to the x0 plus x1

**00:16:39**  times M so the authors of this signal paper used multiplicative notations and then again the coordinator can verify the validity of of a Mac given the coordinator secret key and the message by just basically recomputing it so how can he recompute the mac so again just applying the same formula he will get u

**00:17:10**  double prime and then he just needs to check with the u double prime equals new to the x0 plus x1 times m if this equality holds then the mac is correct and the message was not modified otherwise outputs well invalid so and then we have desirable desirable security properties right so but I think those yeah let's do

**00:17:41**  the minor note on the notation so here they write U and u prime but later in the paper they call it U and V so uppercase u and uppercase v are this paper owners is a little bit math so we will we need to write a long-long errata letter them so we will do don't worry ok so now we know what is the commitment scheme what are max algebraic max what

**00:18:14**  we need to know maybe we're here just few words about ZK or or shall we explain ZK here Sigma I think the definition that section 2.4 I think is is it's it's the same notation that we use and it's pretty concise for yeah right thread and this is um do you want to explain it to you well I don't know you're doing a good job where do you

**00:18:45**  wanna are you tired already so 0 approves these are magical create creatures animals but they are not that not that worrisome so but it doesn't say the algorithms it has anyway yeah but what do you mean the algorithms like prove verify pigeon I was expecting something different something similar whatever I think maybe the original CMZ

**00:19:20**  13 paper has such definitions but sorry I didn't I didn't prepare that we have something here so okay let's stick to do anyway so knowledge proof system has basically many algorithms but let's simplify it has two algorithms of proof and the verify so approver wants to prove that a relation holds for X and W so W is

**00:19:52**  called the witness and it's in it the prover wants to keep secret and witness so it doesn't want to publish publicize the witness otherwise it will be trivial to prove this relation so how can we circumvent this issue so the prover generates a small proof by and then the verifier can give an axe and PI but not given that the witness can verify that this relation holds so this is basically

**00:20:24**  the footprint of a 0h2 system and here's define relation maybe because that's yeah unintuitive yeah duh like in the first higher level you can think of any relation just involving a predicate which used is x and y and some public values but for example the most simple and like the grandfather of all zero knowledge proof systems is the Schnoor

**00:20:55**  identification protocol which allows to prove approver that given Y and the G it knows such acts that G to the x equals y so this is called knowledge of discrete log protocol and or we can have another type of neurological system which is called the oak the knowledge of opening of the Patterson commitment so here we

**00:21:26**  prove that without releasing without making any information whatsoever about the exponents that we know x and y is such that Z equals e to the X multiplied by H dy right and then we can combine such proofs with logical and logical or write and but in our case the most important is that approver can prove that they know an opening of a commitment

**00:21:57**  or in our generalized commitment so if we have not just J and H as generators comprising this element Z but we have multiple generators then approver can prove the knowledge of all these exponents up here without releasing any information about them right so this is kind of a very crude very initial introduction to the knowledge process now maybe we can go to lobby lobby if

**00:22:30**  there is no any comment and if if this is unclear we can consider doing like the first page or first two pages of Sigma I guess it's up to you guys to decide no it's a it's a document for for

**00:23:04**  cryptography probably for implementing this we need something different because I think the document is okay s as it is if I keep the refer can understand it yeah I think from an implementation no point of view it's really enough if you just think of these like it just gives you two functionalities you can prove something and then you can verify some this the validity of this proofs

**00:23:36**  so I think maybe this is this this might be the closest and the most helpful thing we can offer I don't know if it helps I think yes actually I disagree here I think if we do go through so like let's let's quickly go through this noir identification protocol as an interactive protocol and then I think everybody will recognize like Schnoor signatures because this is how these

**00:24:07**  things are made concrete and I think important thing is just to remember that none of the proofs that we require need anything more than Sigma protocols it's just that it could be more efficient and we also want to use the feature myristic to make this non interactive are you or you in favor yeah I mean if there's need

**00:24:38**  we can go over to start identification typically okay so here just one minor note is in his example he discusses this of like just the integers mod piece and large prime yeah but but for our purposes like since the finite field Z sub Q is also happens to be a group because every field is a group we can

**00:25:08**  think of that as the elliptic curve in this case yeah exactly okay so shall we go over then yes please okay so we again we have a verifier has access to P as the characteristic of the group doesn't really matter G and H and the prover wants to convince the verifier that he knows such witness

**00:25:39**  exponent which which is right if we raise it to G then we have we will have H so the statement we want to prove is that G to the W equals H in this group without leaking any information about the weakness okay so so again this is the statement we want to prove and then this is like zero knowledge 101 so if

**00:26:12**  you will ever take another class in zero knowledge proof system then this will be most likely the first or one of the first protocols you will see so it's a three move protocol first the prover chooses a random R in the group and sent a to G to the R to the verifier okay so P is the proverb is the verifier then we and our correction in this case even though the the scalar

**00:26:42**  field and the group are the same thing R is a scalar so in the elliptic curve case P chooses our from the the field of like the the prime the the finite field whose order is the same as the order of the group yeah yes yeah I mean it's really stuff a little bit but okay nicely so we choose is a challenge e from from this isn't really matter this

**00:27:13**  group and sends it to P and then the P the prover sends Z equals air plus e times W so basically the prover masks the witness with this challenge e what Q so basically this is kind of why the verifier will not learn anything about the witness and then the verifier can check this equality here and correctness so from any 0h protocol we require three

**00:27:47**  properties correctness so if the prover knows such a witness which satisfies the relation then the prover should be always and should be always able to convince the verifier so like it's super simple to see that this relation holds if the prover has the correct witness then we also require soundness from a proof system so if the prover doesn't know such a witness namely the proverb wants to lie or tries to lie then the

**00:28:19**  prover should not be able to lie or with some or only with some negligible probability and then we also require zero knowledge which is a little bit more technical to formally define but zero knowledge means that the verifier does not learn anything about the witness which is the information the approver would like to keep secret so yeah this is a three move so called Sigma protocol the way they are the

**00:28:53**  reason why they are called Sigma protocols because maybe is there anything like that no I don't think so no it's a [ __ ] meme it should be called the Z protocol or something it's like three hundreds like if you draw lines or how to say if you draw the direction of the communication then it looks like a sigma but but your body's right so let's see yeah okay so I think

**00:29:29**  is everybody comfortable with that I guess yes because we are pretty familiar with that so if you understand so basically all the zero knowledge proves what we need in wabi-sabi are really similar to this this specific Sigma protocol like they are siblings or

**00:30:00**  brothers and sisters to this protocol so if you understand nor identification platycodon basically you almost understand all other Sigma protocols so that's good news and now we can maybe move forward to a piece of it right okay or her is there any question comment critic there is none

**00:30:33**  okay so first let's just start with I'm just a high-level description of the protocol shall we also define input/output Prudential attribute would it make sense I don't think so okay so the user acting as a list to submit your input value so like anytime we think of inputs or outputs we just represent them as integers at namely

**00:31:04**  their Satoshi well you so we extract away any other information such as scripts strict bupkes etc and whenever the user submits an implicit EXO it also sends K pairs of attributes so each input has K attributes a value attribute and a

**00:31:34**  serial number attribute and you should think of these attributes its commitment to these messages so just by seeing MV I and MSI you will not know anything about the underlying B eyes and EFTS eyes and so hand because the coordinator doesn't know anything about these values whether they are well formed or not the Elliots

**00:32:05**  also sends some very large proofs to convince the coordinator that certain relations hold for these m VI and msi most importantly we want to prove that the some of the underlying VI eyes add up to this public V in and that and and we also want to convince the coordinator then that we did not print any more money namely the this MV eyes lie in certain range so you

**00:32:39**  should not be able to adjust the register 21 million bitcoins more importantly if you come in with like one Satoshi and you register - a billion Satoshi and plus a billion in one Satoshi the sum is still equal to VN that's why they have to be positive that's how here so I want to expand on this and say like not only are those attributes commitments we want them to

**00:33:10**  be Patterson commitments because we want them to be homomorphic and homomorphic means that the sum of two commitments is the same thing as a commitment on the sum of the two messages and this is also why we use an algebraic Mac because the algebraic Mac kind of preserves these nice properties and if we didn't do this

**00:33:40**  if we didn't use Patterson commitments and algebraic marks those that zero knowledge proof of the storm would be much much more complicated it could not be a simple Sigma protocol or actually we don't even need this Sigma protocol that the way that we defined it but well I'm getting ahead of myself these groups are verified and they are valid then the coordinator issues k-max

**00:34:11**  message authentication codes on the requested attribute and also the coordinator needs to convince now the client the alias that these Macs are well formed so that the coordinator does not want to cheat a list okay so now we just give a high-level overview so we don't really describe how these attributes and the credentials look like so let's move forward or yeah is there

**00:34:44**  any questions to input registers I mean now we are really just having just a glimpse of the protocol we will go into the details later so just exactly what gets transferred there so the DMV n ms the value and the serial number Vektor the commitment Chara arrays anyway so those get

**00:35:16**  transferred the range proofs regarding the range proofs is it bulletproof or just normal range proofs I mean as of now you can think of favorite and most below the range to but most likely I suppose we will implement the most efficient form which is currently the state of the art is blue across here alright and anything else that gets transferred some and a small growth we

**00:35:49**  call it like a soundproof which convinces the coordinator that the sum of the committed v eyes adapt to be in anything else you know that's it you you summarized it correctly ok thank you that's pretty simple so like you can think of you have one Bitcoin and you register you want to have 10 10.1 new TX o outputs Bitcoin outputs then you request 10 credentials for this and

**00:36:22**  group attributes actually I think he was said that some kind of relationships has to be also proven on M V and M s is that are very you referring to the range proofs and some proofs or no the Sun so you want to prove anything with regards to the serial number you don't really care because the the Alice cannot cheat there so it's Alice's yeah me so

**00:37:00**  yeah and it's gonna cheat anyway so we don't really care about the serial number commitment but we only care about the value commitment and we each individual mvi we will require a range proof and we require this some proof I don't think there's any ZK we require 4 m VI and MSI is there anything like that you well I don't think so I think in the

**00:37:31**  version 0.1 we still wrote that there should be a proof of knowledge of the opening of the serial number commitment but yes that it's it's not contributing anything I mean if the user doesn't know the opening of the serial number commitment and that's her fault so but yeah we could require something like that but I don't think I mean the worst that could happen is that Alice sabotages the protocol by registering an

**00:38:03**  input that she can never open but that's the same thing as refusing to sign in the end or refusing to register an output so it's it's the same like unsolvable denial of service of Alice disappears all right thank you so ok what is an output registration now with in yet another network identifier

**00:38:34**  acting as Bob Alice comes along to register her I would put the user and okay so now comes the fun part previously we added commitment now Alice randomizes the commitment um maybe the viewer doesn't know what it means but it's ok we will explain it later and by randomizing this these attributes now

**00:39:07**  this makes these attributes unthinkable to the previously attributes by the coordinator and that's the rationale behind randomizing these attributes but still Alice can convince that even though these attributes are randomized still Alice can convince or Bob if you wish can come with the coordinator that these are valid credentials issued by the coordinator and that's that's why we also use this

**00:39:38**  algebraic Mac or are the signal paper most more precisely and yeah anyway verify a small thing because there's a slight mistake here we need to fix so it says a valid credential but it's any number of credentials so the whole point of this is you register each input independently and you get several credentials for each input and then you go and you pick and choose whatever

**00:40:11**  combination you want for every output registration so every user can in register several inputs and can register several outputs and no input should be linkable to any other input or output and no output should be linkable to any other input or output yep and we again in the output registration phase we will require some zero knowledge proves what properties should Alice convince the

**00:40:43**  coordinator about so let's start with the serial numbers Alice will just or Bob will just reveal these serial numbers and that's where we will have double spending protection a can I ask yep the serial number stuff as far as I can see

**00:41:15**  wouldn't a simple blank signature scheme could work with the serial numbers or or not I think the effect is the same or what would be the gain no I'm just asking that is that something swappable I don't think there is a gain because right yeah we are using the serial numbers for as as we are using it for the exact same yeah I

**00:41:48**  think they are interchangeable that's if I understand the question correctly I think it's it's not possible because I mean we need the algebraic max stuff or something like the ACL scheme which is line signature scheme with attributes if we only do a blind signature on the serial number here then nothing constrains the user to only use the same serial number with the same amount so by

**00:42:19**  doing it with a single Mac that covers both of these together the Mac is only valid if you expose the corresponding serial number to the the same amount okay thank you this is this is exactly what I was I was looking for that okay so the serial numbers and the values are actually connected together but but the MV in and M s and M VI and MSI's blindly

**00:42:50**  sign then this attack vector is fixed right yeah and and that's exactly what the ACL paper let us do right so there we have a blind signature scheme with attributes and the attributes are exactly the same as as here would they're just Patterson commitments the difference is the randomization is more complicated to prove things about the

**00:43:24**  signatures are larger so here as a Mac is a single field element and two group elements whereas the ACL scheme I think it's like 1/8 tupple of like I don't remember how many of those are group elements and how many are I think they're all group elements not that it matters because they're the same size there's 32 bytes roughly so in the ACL scheme I think is much harder to

**00:43:56**  understand than the algebraic max so like this is meant to be a plug-and-play sort of sorry a plug-in replacement for the ACL scheme and in this sense it is like the the blind signature scheme with attributes gives us exactly the same thing it just also provides a public verifiability of these signatures which we don't actually need so again and we

**00:44:33**  need to prove some relation between these attributes because the user wants to register an output to be the specific Bitcoin value and maybe this bitcoin value is constructed using several other credentials so again here we will need some proof these are all spelled out in the paper so don't worry the crypto details will come soon and then yeah

**00:45:06**  that's it the user submit all this trust and then we the coordinator verifies this proves and how to register a shin is done basically signing face is pretty much the same we use the same as the in current wasabi so the user just checks whether her desire the output is included among the output of the coins and transaction if this is the case it

**00:45:37**  signs the transaction and sends over tor the signature if this is not the case then the user awards the protocol right let's go to the crypto D test if there is no question it is there any yes I'm good okay so there's a lot of parameters

**00:46:12**  of the coordinators so anytime you see the with some subscript it's just a generator point it's just an element a point in an elliptic curve and more most importantly no one knows the underlying discrete logs pairwise discrete logs no one should should be able to to know this and then the we want to talk about the individual subscripts like at least

**00:46:43**  categorically I think so W and W prime are part of the secret key there using the keyed verification credential scheme x0 and x1 are the generators used for the algebraic mac so they correspond to x0 and x1 which are the part of the secret key in the algebraic mac Givi ng s those are our notation in the original

**00:47:17**  paper these are denoted gy 0 gy 1 to n they're used for the in the Mac for verifying the attributes or sorry for assigning the attributes or tagging the attributes I guess is the correct term then we add G sub G & G sub H for Pettersen commitments and finally there's G sub V which is used in the

**00:47:49**  verification of the algebraic mark yeah and this is Christy of the coordinator and yeah maybe maybe we could change later from issuer to the coordinator but in the document as of now we use issuer and coordinator a little bit interchangeably and so these are the public parameters

**00:48:19**  of the coordinator these are the secret parameters and now let's move forward to the input registration so can I have a question from Lucas actually so these public constants of this look looking how would this look like in c-sharp code can you hear me yeah yeah well in

**00:48:51**  c-sharp called in it's just I don't remember the new and Bitcoin library but it is just a point right is just to create a point in fact aye-aye sir paper no no paper a pull request on and decline where the recent way to derivate

**00:49:24**  one point one generator from another generator but in a way that you don't know they they shout to go from one to another I don't know how to play this and there are hash function that's usually the yes it uses is this is like a HUD function of the of the previous one to generate

**00:49:55**  the the next one or something I don't remember exactly the details but in in in an Bitcoin for example you have a sec SEC P 256 k 1 dot G big G that big G it's a liquid pure point I think that the class is called Big E C point if you have that G

**00:50:30**  big G that is the the generator so it's basically and we can use okay for what it's worth I think the traditional method to do this is called hash and pray where you start by hashing a message in this case it just be the variable name and you use that as the x-coordinate and you check is this X coordinated like on the curve does it

**00:51:02**  like map to corresponding Y that's on the curve and I think with like a probability 1/2 it should be the case for SSCP 256 K 1 I suppose it should be like almost because the order is very close sorry my bad yeah like if you have 200 bid then like pretty close to 1 yeah for

**00:51:32**  some reason I thought the the order was 2 to the 128th for a sec my bad yeah because the rows I forget whose Rho algorithm is like square root of n right it's know for a security parameter of 128 you need 56 a group order of 2 to the 56 more or less no run is that that's not relevant anyway so if it's not on the curve and you just say oh

**00:52:02**  sorry just a comment in the chat then you can see how in c-sharp it could be I mean it's just an elective cure and and that's it I see that's very useful actually Thanks I was just not sure how how low we can go do we have these building books already or or not is it guaranteed that the discrete log is not

**00:52:34**  known between these we can't I mean we can find a way to derivate one from the other one off we can just select I don't know I couldn't feel comfortable selecting the values by by the way that the signal paper defines it is that hash to point function I think it's called

**00:53:06**  and you just hash the variable name take that as the final score oh yeah okay yes that that's a good way yeah it's not a valid curve point then you just append like an integer we increment an integer right like do the variable name the variable name dot 1 or something try to hash that if it's still not working hash point 2 and soon enough you find a point that's the hash yeah yeah I I feel

**00:53:40**  I feel okay with that I mean if it doesn't exist the point try it with the next one yes it's a good way my bad so this this is just the characteristic of the scalar field and this is the actual size of the elliptic curve group so it's very close though yeah it's close so like to divide this with two to the 256 it's three still it will be pretty close

**00:54:13**  to one so the hash and pray method should output you almost instantly this almost instantly a valid point on the curve yes i-i've never I never seen a point that is a number that is that that give me an invalid point all the points I tried it's always funny nice okay so let's go but here Oh part of that the subtlety of the hash

**00:54:46**  though is we need to convince the users that the the coordinator did not generate these points maliciously so it's not just choosing a point it's you need to choose a point that everybody knows is safe maybe we can hash the first I don't know ten words of the white paper and then we will have some points in the third so it should be trying because you discuss the function earlier it's called hash to G and it's

**00:55:17**  just the definition right okay so the input registration because it split it simple do we want to discuss the parameter store what they mean it eats it up you and I or a rich one yeah it's a little bit unintuitive but like what they do is they allow this is

**00:55:48**  used as part of the credential perfect okay never mind let's let's do that later after we do the show protocol so just remind me to go back to the parameters so we want we have input UT XOR with value V in and we want to break it into K inputs with value VI so to that end we submit K Patterson commitments so M VI is the Patterson

**00:56:21**  commitment to VI namely a J - J sub G to the our VI so this is the blinding factor and this is J sub G to the V I so this is a comment that there's no commitment to VI blinded with RBI okay so we have K commitments to be a similarly we have K commitments to the serial numbers so k / there's no commit the serial numbers and for each value

**00:56:54**  commitment we also include a range proof which says that I'm I have a commitment which is basically a point on the curve it's a commitment to be high with some randomness rvi these are the witnesses so I'm not going to tell you the witnesses but I will be I will be convincing you that still the underlying

**00:57:25**  value lies in the range so it's less than say 21 million bitcoins so it's not some negative value so we don't you don't know you don't need to know how such zero logical system looks like we just need to accept that such a animal exists and then okay so we were able to prove that the commitments are well

**00:57:55**  formed now we need to convince the coordinator that the sum of the sum of the VIS add up to the claimed registered in patootie rec so how come just a comment and the you I don't know if you said that the are B I am si the blinding

**00:58:26**  factors are chosen randomly oh yeah that's right that's right I forgot to tell ya you are absolutely right yeah if they are not chosen randomly then Alice is screwed and and the coordinator could do unionize Alice if the values are not padded here okay so this some proof this

**00:58:59**  is super simple we apply the same trick we already described several times in previous muscle research club videos so it's super easy how to have week improved the stump of committed values in the petals and commitment equals the public value so we just need to the coordinator can just calculate the product of the value commitment and the product of the value commitments will be gg to the sum sorry

**00:59:32**  Gigi to the sum of the yet to the sum of the randomness values our VI the blending factors and gh to the V in so basically this is the this if this equality holds then L is indeed convince the coordinator that the sum of the committed messages adapt to the in yeah also not this is not zero knowledge

**01:00:04**  proof it's not a Sigma protocol either but it could be for our purpose like if you since when you reveal a sum of random numbers you don't reveal anything about the original numbers and those are just blinding terms this is still what's called witness hiding but it's strictly speaking it's not zero knowledge and the

**01:00:34**  like we could do it zero knowledge by making a Sigma protocol that proves knowledge of the sum and like eventually shows so we would do like G to the to the PI sum and then prove that this commitment lose the other commitment opens to a commitment to VN or something like that we don't see a reason why that that needs to to be a sigma protocol so just

**01:01:07**  to clarify that the this pi term is is literally just the sum of the exponents yeah okay so we have the some proof which is pretty simple pretty standard we discussed it several times what is missing from the input registration is that now the coordinator accepting and verifying these proofs the coordinator should give out these valid max and so for each for each so this is the message

**01:01:41**  the coordinator is signing if you wish this is not an insignia but a Mac and the coordinator will convince Alice that the Mac is Val formed so like without this Z knowledge proof it would be really bad because maybe Alice just got to get some garbage from the coordinator and we don't want that so this is just a

**01:02:12**  form of description how come how perform a description of a zero knowledge proof system that achieves convincing Alice that V is a is a valid Mac with respect to these public keys public parameters of the coordinator yeah because obviously the coordinator doesn't want to tell Alice the underlying secret

**01:02:42**  parameters in the first place so yeah maybe I have a lot of clear in explaining this so you could help me so first the T and you are also part of the Mac I would say yeah yeah that's true and then this is this is exactly how the coordinator proves to Alice that it's not using a different key for each user so that it can be anonymous them later the the reason is because CW and I

**01:03:17**  are published in advance everybody should check that they get the same ones if they fetch at different times over different tor circuits so these parameters we well-known just like the round denomination keys for the blind signing or in the current protocol and then this proof convinces Alice as a proof of knowledge that this was relative to the

**01:03:47**  the key so Alice cannot use this to prove to anybody else that her Mac was derived correctly or sorry in this case she can because this is probably gonna be a non-interactive proof so anybody could verify it but if she does that she reveals her Mac so sorry that was a little confusing but the point is Alice only learns from this proof that this is a Mac generated by the the secret keys committed to by the parameters yeah okay

**01:04:22**  so with that we conclude the input registration phase and now we can move forward to the output registration which is a little bit more complicated but not that much so now let's say Alice got all together T valid credentials so T valid Max and now Alice just want to use in the first output registration just ass out of this D right

**01:05:01**  yeah so this this is in the first place what we do and this this is called the show protocol which is more in more detailed explained in the signal paper but it is even harder to understand the single paper because in the signal paper there are many typos and errors so we maybe this is the right place to learn it and it's also more general we only need a specialized version of it because we only use one kind of attribute that's

**01:05:31**  really true so what what's happening under the hood is that we have this nvi and msi commitment these are reran demised namely really randomizing me means that it's multiplied with another point on the curve just to look just to make it look even more random and then we have this randomized commitment and 0h magic

**01:06:05**  allows at least to prove that he has a valid Mac on the rear end of my stuff or more precisely that she just show she just shows the rear end of my stuff but still can say that look I know well is Mac behind these three randomized things maybe I was again a bit clearer but this is this is what happened yeah what is the the V the big V is the last run the

**01:06:43**  recession's weight in so that's that should be VI I think that's fickle of the eyes okay and it's the last component of the Mac yes perfect thank you this is a type of from our part yeah I fixed it I think you're using a an old version of the PDF I don't know maybe I fixed that okay sorry I think I fixed it in the like the markdown

**01:07:14**  work in progress branch I should I should bring that over to the overleaf version another question in T because the the the Mac has a component at each component but this T is the number of of Mac's or the combination a random scalar it's a component of the Mac and it's

**01:07:45**  just a random field element no but but Lucas makes a point here that we also do not see the number of credentials and it's gone yes oh sorry yeah but a TI is the one that comes from the Mac and I don't think we ever used he again after this paragraph yeah we should choose a different because here's there's the class yeah yeah my bad you have an eye

**01:08:17**  like an ego I try to understand yeah but this is the valid point because this is called like C times K or something instead of T okay this is confusing indeed yeah so a little bit so little letters in the alphabet we should have a longer alphabet right or I don't know maybe we should use Hebrew letters at

**01:08:48**  you have degree the Greek alphabet the the English alphabet the Arabic alphabet [Music] why I think when one important thing for the notation is anywhere you see a subscript I that means it's part of like it's related to specific credential except where I made that typo with V I'm

**01:09:19**  sorry that's a helpful intuition though it's just so that you could to write perfect document there will be always errors and typos well one step at a time right okay so is there anything to add to this credential validity so this is where I wanted to bring up the issue air parameters they're not just used in

**01:09:49**  order to convince Alice that she got a valid Mac they're also used in here to generate the proof so both CW and I are used sorry no only I in this case and this value Z Z is generated by Alice it's kind of generated one way so Alice

**01:10:22**  generates it by taking I and raising it to the power Z but the coordinator calculates I in a different way it calculates it from the randomized commitments and from its secret key yeah but if you want you can also just as of now think of this whole show protocol or credential loyalty as a black box so Alice randomizes the commitment and

**01:10:55**  proves that he has a Mac she has a Mac which is valid but not not showing the Mac itself to the coordinator maybe maybe hopefully now we explained it well I then

**01:11:39**  can you repeat that Lucas looks like the internet is gone in Argentina no okay so you can ask it as a youtube comment okay so like how can we prevent users overspending and then we

**01:12:12**  have one one less now just this right what do we prove here okay but this is trivial so what this is also trivial whatever so overspending prevention so the user has the user has this as credentials and we want to prove that they add up to this output you txo well you be out so

**01:12:45**  again at this point in time Alice has randomized commitments and this is CBI CBI denotes the randomize commitment a CBI is just basically mvi with randomized with GV and by a user chosen randomizing factor VII but if we spell it out then this point is essentially has three generator points and then each

**01:13:16**  generator point we have the exponents are essentially sums terms of either zi r VI or VI and we want to say something about the sums of V eyes so this is pretty simple if the coordinator takes the product of these randomized commitments then this is what we will have okay so what we can do is we can just open the commitment on GV and GG

**01:13:50**  how can we open the commitment with respect to these two generators well we just tell the coordinator the exponents corresponding to these generators so essential the proof which is the Gannet in zero knowledge proof but rather a witness hiding but this is just small stability just a technicality so the proof is two scalar field elements the sum of the Z is in the sum of the RBI's

**01:14:22**  so hence if we give these two group scalar field elements the coordinator the coordinator can just raise GV to the first proof element and GG to the second proof element and this is the well you what Bob's claims to be the Sun so the right hand side can trivially be calculated either from the proof or is public knowledge and their left hand

**01:14:56**  side is just the sum of the rear end of my commitments so if this equality holds then also the claim the statement what Bob is trying to prove holds right so this is this is it and so this is how we can prove prevent overspending okay and then in the very end of the output registration phase we also want to

**01:15:26**  prevent double spending and double spending is pretty similar that the spending prevention is pretty similar to the previous knowledge group we have as we randomized serial number commitments so again MSI is a commitment to the serial number what which is now real randomized by the user so the real randomized commitment looks like GS to

**01:15:58**  the Z IgG to the RSI and gh to the si so now the user needs to conduct the coordinates a mistake in the this is because we move the sections so this is redundant with the CSI defined at 2.2.1 it's exactly the same one what's the point what's your point this one says she randomizes the serial

**01:16:32**  numbers again but that's she already randomized them to prove the credentials valid so same CSI I just took it as a reminder okay I know it's an editorial mistake because women of things are okay so basically the user wants to convince the coordinator that given CSI the user knows gir Si and si such that so this is

**01:17:06**  called knowledge of representation so the user knows that the representation of this point with respect to these three generator points without telling the underlying individual exponents so we have such a zero knowledge proof system you don't need to know how it works we have it out of the Shelf of the Shelf and but in our case what we also

**01:17:39**  need to do need to do is that we can publicize si because that's how we will that so we need to public publicize si and the serial number because otherwise we will not accept on the output registration yeah it's it's pretty easy

**01:18:14**  like you give the serial number and you give Patterson commitment to not exactly but like G to the Z G sorry G as to the Z Jiji to the RSI I proved knowledge of Zi and RSI with respect to that commitment and the coordinator can can confirm that this commitment x GH to the SI is the

**01:18:46**  same as the randomized commitment exactly thank so but if that that concludes the output registration phase and then we have wabi-sabi at least in draft 0.2 in chinese GG means penis

**01:19:23**  something every day so maybe hopefully we will have some Chinese viewers and they can correct me voice sitting here alright thank you guys maybe do you do you have anything you would like to talk about before we go all right I think this as a no this

**01:20:01**  was a pretty intense session I will definitely watch it a few times and hopefully I understand more I have maybe one last thing so we can post it in the description but I would really recommend to anybody who wants to read into this a little bit more the original algebraic mac paper i think is a

**01:20:32**  a very nice read wait let me give you a precise title I'm sorry it goes wrong paper yes so algebraic maxed and key verification anonymous anonymous credentials this is where the stuff was introduced so melissa chase Sarah Michael John and Greg's Arusha whose name I keep forgetting I'm so sorry Greg the signal

**01:21:04**  paper takes this there's two algebraic Mac algorithms described in there one relying on the generic group model for security proof and the other relying on decisional diffie-hellman so the signal paper uses the first one and extends it to support attributes where the attribute values are not just scalars but arbitrary group elements I think

**01:21:37**  it's very well written it's also got at the very end like after the security proofs there's a concrete instantiation of the zero knowledge proof for this slightly simpler scheme so that's a really good reading I think and also personally I'm kind of new to this zero knowledge stuff so I found Ivan damn guards introductory materials really

**01:22:08**  helpful both this one and the one on commitment schemes and zero knowledge protocols actually this one was probably more helpful because it really goes through the like the logic and the definitions it it's a very clear description of the difference between a proof a proof of knowledge zero knowledge proof zero knowledge proof of knowledge etc etc and also covers stuff like cryptographic simulators which are

**01:22:40**  needed for for all of this stuff both as a theoretical concept and for the a be blind signature scheme you actually need to write a simulator so it's really helpful to understand how the Abed blind signature scheme in the ACL paper we discussed like why that even works anyway so those would be my reading recommendations thank you sorry I have a question you said that

**01:23:13**  given we are creating this dis max from the commitment for the Palio commitment and the serial number commitment you said that this is the magnitude that we need to use because this preserves the on morphic the what sorry either I love

**01:23:44**  the word but then the property of Murphy I'm a morphism of the commitments and where are we using that again so well why did we have to preserve that just just making this edit proves easier like we just want to make our lives easier so if we have this nice properties then for example this overspending prevention like proving

**01:24:15**  sums becomes like almost trivial yeah so we we use it implicitly in these some proofs and also an input registration phase yeah you can imagine something that uses an H Mac but then doing the zero knowledge proof should become really complicated you need something like ZK snarks or ZK Starks or something like that like art enjoy arithmetic circuits and the proving time is going

**01:24:47**  to be really long and the proofs are gonna be yeah it's it's just probably requires a trusted setup so that's like the the main advantage is it makes the all the zero knowledge proof extremely simple on the same sort of complexity as just the Schnoor signature even the range proofs I would argue or are still as simple it's just the same idea like repeated multiple times and in

**01:25:17**  bullet proof they make it much more efficient by doing it like that there's a cool recursive trick but conceptually it's still very much like a Sigma protocol and not like one of the more general purpose user knowledge proof systems it seems to me I I'm not sure but it seems to me that the harder computation is performed by the client

**01:25:48**  or I mean from the from Alice right no from or but not from the coordinator but anyway thank you you have any any idea of how how hard these computations are on the server side in the on the coordinator side and how many an elected curve multiplications let's say well I

**01:26:18**  cannot really give precise numbers but all of these proofs are like super lightweight so I I think it's just a question of milliseconds so I'm not afraid at all I think the most expensive part is the arrange proofs because in the range proofs you need to do a binary decomposition so there's like a vector commitment to the individual bits and like you need to compute the inner

**01:26:49**  product and I think that's so that that would be like I think 51 if we use 51 as the range times I guess it's like four multiplications and then like you can make it into a giant multi exponentiation it's basically oh of n in the the parameter of 51 and there's a protocol so somebody linked on a slack channel if

**01:27:23**  you go it's fun very quickly to lightweight dot money so this is the Nanaki I think it's pronounced it's like a Greek word this is a very similar idea but it uses the older algebraic max scheme and it uses alga Moll encryption and blind issuance so I would say it's ever so slightly more complex because of

**01:27:56**  the blind issuance then the newer signal scheme and he has concrete performance figures that I think should give us at least an order of magnitude estimate that's item 9 so in your opinion the the the range proof I mean it requires the the inner product of the each of the 51

**01:28:29**  beats for what the other element the way the range proofs work is you make a commitment to like I actually I don't know how the commitments in bulletproof vests work exactly I need to review that but as far as they like the the statement being proven you do you take a

**01:29:00**  vector that's like some generator does the same generator for the commitment value to the power 0 to the power 1 to the power 2 no sorry you do 2 to the power like 0 1 2 times that generator and then you you so you have these generators that are the same for everybody and that's just like a vector of the powers of two and then you compute the inner product of another

**01:29:33**  vector which is 0 or 1 for every binary digit in the amount so you do like 0 or 1 times the first generator for you know the first digit 0 1 times the first generator the second generator for the second digit and so on and then and the inner product if this should be equal to the Patterson commitment of the amount and then you also need to prove for every one of your bit commitments you need to prove that it's exactly 0 or 1

**01:30:08**  and the way that you do this is you take the a commitment times I think the sorry the commitment witness the value times 1 minus that and this would be 0 for like if the bit is 0 then 0 times 1 is 0 and if the bit is 1 then 1 times 0 is 0 but for every other value it's gonna be nonzero so like you take all of this

**01:30:39**  stuff together and like one giant polynomial and like that gives you eventually a commitment to 0 and that's what like ensures the validity of all of this and and the bulletproof stuff like you can do this as a Sigma protocol but the bulletproof stuff does something like really clever where they they basically do like the recursive decomposition of this problem and like

**01:31:11**  they add if this was an interactive protocol it would take log n interactions but with the Fiat ramier heuristic you can still make it non interactive and so the the prover and the verify still do oh and work like they would in a Sigma protocol but the actual resulting proof size is only logarithmic it's it's very small hopefully that that makes sense and just as a caveat I'm like I barely understand that stuff like so so I probably made okay yeah I'm

**01:31:47**  just asking this because I see a lot of operations and the server is one only one that had to to do this for every every user for every single a pair of commitments and we we have now the C or C++ performance with c-sharp in this

**01:32:18**  kind of stuff but I'm just I just was curious thank you I think so if we compare it to that lightweight money scheme the danaka scheme the credential that like we have is very similar to what he calls a token not a wallet so a token spend is very similar to a output registration and a I think he calls it a

**01:32:50**  wallet top up or like that's very similar to input registration but a little more complicated because it requires like another proof and he uses bullet proof for everything and the the performance figures that he gives this is on a curve 255 1/9 and rust it's still only a few milliseconds per per operation so if we take that as like an

**01:33:21**  order of magnitude let's say you know it's 10 times slower I still think it's very reasonable for a fixed number of participants like this should be like not more expensive than say like the number of signatures you need to validate a block or something like that in Bitcoin so I don't know I mean maybe like I think I'm really overestimating

**01:33:54**  here but let's say it's like 10 seconds of compute overall in an entire round I think that would would probably be enough and this stuff is like one of the reasons we prefer this over like bilinear groups and zk snarks and all of that it's not just more complicated conceptually it's also that those underlying primitives are not as efficient like for bilinear groups you

**01:34:24**  need groups with like a cofactor they can't be groups of prime order because you need like cyclic subgroups inside of them so that's a like a bigger curve order and typically they're not as like the implementations are not as fast either so I think from all the schemes we consider this should actually be one of the more performant ones even though it's it's still probably at like at

**01:34:58**  least a hundred times slower than just a plain blind nor signature all right thank you guys for today and like share and subscribe and there's a goodbye let's hear some word from our sponsor [Music]

# Wasabi Research Club #16 - Protocol BLS

- Playlist index: 16
- YouTube ID: `KPD7IR2fn34`
- Video: <https://www.youtube.com/watch?v=KPD7IR2fn34>
- Duration: 1:27:42
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:02**  hey all right welcome everyone this is wasabi research club number 16 maybe and today we are going to talk about something that we started researching and this will be different research club from everything as was before because

**00:00:33**  from now on we are not going to review papers but we are going to actually research so this will become a research club and not a review club and we will get back reviewing papers as soon as we stop researching and here we have today East one and you are who are working with me right now

**00:01:05**  wabi-sabi which is trustless which is where we are trying to achieve translation orbit rare coin joints and why is it important what what's the logic behind it if you have ever used Cohen joins before at least with wasabi then you might have noticed that you have a lot of change and you cannot actually send money in the Cohen joins to other people and these are the

**00:01:39**  problems that we are trying to solve and for that we first have to very quickly go through how coin joints are being done in in in a design level in architecture level and it all comes down to three main phases which is input registration every user comes together and register their inputs then output

**00:02:09**  registration users register their desired outputs and then finally coin join is built and everyone has to sign and why this is important is because this grantee is security so if you don't see your design desire the input a desired output in the coin join them you don't sign your output you don't sign the coin join so

**00:02:41**  the coin join will be invalid and it won't be not happen so this is why you cannot lose money in coin joins now going further think about how to how to register inputs and outputs to the coin join in an anonymous way because these input registrations should not be connected together with each other needed output registrations and for that there are actually two school of

**00:03:14**  thoughts one is the coin shuffle school of thought when they build their own anonymity network to make sure the anonymity is ensured within the anonymity set which is all the users of that coin join in asabi it's different because there we are leveraging an existing anonymity network called the Tor network where the body it could be

**00:03:48**  any any other anonymity network where every input registration and every output registration must happen with different anonymity network identities so no one can figure out what's the link there however this brings up a great problem here because if you can register outputs to a Co enjoying anonymously then what

**00:04:21**  would prevent you from registering as many on who says you like I mean it's anonymous and that's what we are trying to find the solution to how to register arbitrary amount of inputs and arbitrary how to register inputs with arbitrary amounts and outputs with arbitrary outputs arbitrary amount and it's important the

**00:04:57**  arbitrary part is important here because an an arbitrary way to register an an arbitrary way to to prevent denial of service attacks like registering many outputs would be what wasabi bullet is doing right now is that you have to have some denominations there and that way with some blind signature magic which we will go into later then we could make sure there are no denial of service attacks

**00:05:28**  however if the amounts are arbitrary then this was scheme doesn't work any more because we have to the new question becomes how to answer user does not register more money in output registration then he provided inputs for but without knowing that which user registered which inputs and which

**00:06:00**  outputs so the link should not be there the link should not be there between input and input registration of users and output and output registration of users and input and output registration of users so that's what we are trying to solve at the first phase of this research work it's a Patterson commitment scheme which I think I'm going to give over the

**00:06:32**  explanation to you would you like to explain but but what was our very first way of thinking which we only saw the splitting of inputs at that point could you explain that okay so first I did want to add to your introduction that for now we're not yet thinking about the

**00:07:02**  structure of the transaction how it ends up so that's like out of scope for today's discussion but it's still very much a concern so anyway with that out of the way I don't actually exactly remember what signature scheme we wanted to use but the idea of a Pettersen commitment is if you have an elliptic curve or any sort of group where the

**00:07:35**  discrete log assumption hardness assumption holds you can take two points on the curve called generators and typically in pettersen commitments those are called H and G and you can multiply these two points by two numbers so one of those would be the the actual message and the other would be randomness and

**00:08:09**  this creates and then you can sum those two values together and this is something that is somewhat analogous to a hash with salt or maybe an H Mac but the idea is like you because you because the discrete log problem is hard it's it should be impossible for anybody to figure out what values did you multiply so what were your numbers that went into

**00:08:40**  this thing but then if you publish the the sum of these two products then you can later prove with which values like you actually multiplied those generators and the reason that you have two of these so if you only multiply a single generator by a number I believe that's what's called a Patterson hash

**00:09:11**  and the idea is that like if the messages are like kind of easy to guess then having an additional randomness term makes it like impossible to brute-force that as well and the key difference to sort of keep in mind for the purpose of this discussion is that unlike traditional hash functions because the the group operation the

**00:09:43**  addition of points on the curve is commutative this means that you have like it doesn't matter in which order you do this and the sum of the messages going into this kind of hash function if you take the the sum of several Patterson commitments then what you get back out is a Patterson commitment to the sum of the messages which is a very

**00:10:13**  useful property I guess back to you thank you I will risk sounding stupid and I try to explain it again in some less technical terms so how we imagined to solve this issue of unlink ability between inputs and outputs would be that we figured if we if we have let's say one Bitcoin and we want to get

**00:10:45**  an get output 0.1 and 0.9 bitcoins then we create two feathers and commitments more because there are zeros but let's just not care about that we create two patters and commitments for 0.1 and 0.9 and that input registration we prove that that these stupid heirs and commitment dee-dee-dee-dee sum is one

**00:11:18**  Bitcoin that our input and also have some range proofs there but again that that's a detail at this point and and we also found blind Patterson commitment scheme which enables us to get a blind signature for the message of the paddles and commitment without the the the

**00:11:50**  coordinator knowing the the actual values there so give back the blank signatures for the users and now the users have unblind to signatures and the users have two signatures for 40.1 Bitcoin and 0.9 Bitcoin and at output registration it can come with two different anonymity Network identity and for once it registers the 0.1 Bitcoin and provides the unblinded signature and

**00:12:22**  for twice it registers the 0.9 Bitcoin and provides the unblinded signature and this way the coordinator can not tell because it has never seen these signatures before it cannot which input its mind those those values for and that that that was the basic working idea that we had however if you think about it it does not enable consolidating

**00:12:54**  input so if I have five inputs and I want to make only one output of that then I cannot do it with this scheme so for this we figured out East Van figured out that it could be possible with the BLS blind BLS signature protocol and I would like to give the words to East Van

**00:13:26**  could you explain the blind BLS signature protocol that we figured out and by the way this is not our our state-of-the-art idea but it is it is good to mention because it it works but it's quite complex state of the art from last week yes but we killed it really badly maybe I don't know if you can share your screen or I should but maybe it would be helpful for everyone if we

**00:13:58**  can have a look at the github issue but if not then like so okay please share your square screen but I cannot share it because it does not get recorded but if anyone has shares it it gets recorded yes so like or the you well-motivated and also on opera why we like Patterson commitments so the thing is that in this wabi-sabi protocol we need to prove

**00:14:28**  statements in zero knowledge about about input u TX oh well used so whenever for example a user registers and impose Duty EXO and she would like to register another or split this amount into two let's say to a change address or a payment value then we we need to allow users to create feathers and commitment and prove that the patters and commitments are formed in a good way

**00:14:59**  so meaning that the underlying commitment values add up to the impute EXO value so and with feathers and commitments we can do as already no para and you have described that we can really easily prove such summation statements over committed values and then okay the next idea was we love feathers and commitments but because they are homomorphic and they allow us to build and prove easily this summing summation

**00:15:33**  statements then let's let's go with another really flexible signature scheme namely BLS which is kind of the most the simplest signature scheme you can ever imagine so this is basically the BLS signature scheme you can see here no this is sorry the blind bill is signature scheme which is still pretty simple so there's a binding phase we have a message m we can

**00:16:06**  blind it so we first of all we hash the message and with the generator in the elliptic curve group we can blind it with the randomness R so we sent the blinded message to the signer which in the wasabi lingo or in the coin join the feature we would call the coordinator so the coordinator gets blinded message and hat let's say and then the coordinator can come blind it with his secret key and then the receiver no sorry the

**00:16:38**  coordinator can sign this blinded message and then the receiver um blinds it so this is a three more signature scheme and the big question was like here we see a hash function right and you've already pointed out this Paterson hash we we all love because of its homomorphic properties so one question we needed to answer what what should be this hash function and

**00:17:08**  let's let let's pick now the Patterson hash because it preserves the algebraic structure of the message so instead if we would choose if we would go with a hash function which like shatter shatter e-cat sack then it would completely mess up the structure of the message so it would have would be really difficult so not trivial at all how to prove statements between these blinded messages and yeah so shall I just easily

**00:17:41**  and quickly let me just first explain like the impress registration phase so we have a public value let's let's just take this example we have a public value M which which you can you should think of em as as a subtle sheet amount which is the subtle amount of your input registered input and then you would like to split this M your input to TXO into

**00:18:12**  two output you TXO values but you don't want to reveal them to the coordinator so you want to create you want to split it into M 1 and M 2 and additionally you want to prove to the coordinator that the sum of M 1 and M 2 adds up to M right you send the coordinator to the blinded messages the blinded messages are patters and commitments to M 1 and M 2 with randomness randomness is everyone

**00:18:46**  in there too so just by giving M 1 and M 2 the blinded messages to the coordinator the coordinator will have no clue whatsoever about message m1 and m2 but still we want to convince him that the underlying committed messages adapt to the public input to TXO value m and it's super easy due to the homomorphic property of feathers and commitments so the comb the coordinator would just

**00:19:16**  multiply and note this is multiplicative notation hope people don't really don't hate it so if we multiply these two blinded messages then note that we would have h2 em 1 plus em 2 multiplied with G 2 R 1 plus R 2 and if we give the sum of the randomness values the coordinator then the coordinator so basically we open this the commitment corresponding

**00:19:47**  to the multiplication of the messages then the and then the court and we could we can convince the coordinator that these values add up so this was like the first step why we were kind of excited about the blind be less signature instantiated with the Patterson hash because it gives us a really simple way to prove splitting of UT exo's right because if you want to make a payment

**00:20:19**  then it most likely you need to either split or merge your UT axles but split is the first thing we want it to solve right yes so this is why we were started to think about this be blind build a signature scheme with the Patterson hash and right let's let's continue or any

**00:20:49**  questions I just want to point out I spoke earlier as in Bitcoin circles usually people write in additive notation and we wrote it here in multiplicative notation but they're the same thing so that's the first clarification and that second one is VLS signatures don't work on bitcoins standard like elliptic

**00:21:20**  curve and it requires a different curve which has what's called or different set curse that has what's called a appearing operation so I just thought that was important yeah thank you please continue ishtvan i think it would be a good idea if you guys explain stuff properly and then i try to translate it to less technical

**00:21:52**  people and i think that that's a good way to go about it so go ahead and explain each one further okay so don't get too much excited because this protocol is broken but I can I can explain it yeah what was the second thought okay so now we know how to split ut axis and let me just say it is not broken it's it's something that you

**00:22:22**  don't like because you made a mistake but the better double spending protection actually fixes that mistakes it's not actually broken yeah but it's not lightweight it's not with it would include additional assumptions like you've uh pointed out so it builds upon repairing base crypto and ideally we would like to kind of remain at the same technologies same assumptions but what is already deployed in Bitcoin but

**00:22:54**  anyways let's continue so and how can we prove so let's say we have we registered a lots of input UT axis and now since we not we also want to make payments possibly potentially we might need to consolidate some of our inputs right because I don't know the payment value is something super weird amount and and we just need to merge coins so how to do

**00:23:24**  that with this blind be a signature scheme with the Patterson hash so let's say this is just an example of merging to output to input UT exo's but the same ideology would easily could be easily generalized to multiple input UTX emerging so let's say we have a mat Hashem the message one and the signature on a message one by the coordinator

**00:23:55**  since this is a blank signature scheme the signature was not seen by the coordinator yet as we have unlink ability similarly we have the hash on message two and the signature on message 2 which again was has not been seen by the coordinator and now the question is how can we prove that and we want to register a UT EXO corresponding to the value m1 plus m2 but we don't want to reveal to the coordinator the underlying

**00:24:27**  value and bonding them too if this is a cryptographic hash function which is then so the coordinator doesn't see does not know anything about message 1 and our message 2 because this the Patterson hash is the cryptographically secure hash function given some range proofs but let's put it aside so we just we give the sum of the messages what we want to register as an output to TX oh

**00:25:00**  well you and this for group element and a small proof to convince the coordinator that the underlying messages adapt to this public value how can we do that again we just need to it's super simple we just need to multiply the signatures what are the signatures the signatures are now we just plug in the definition here we just plug in the definition of the blind a be a signature scheme so Mac Sigma M 1 multiplied by

**00:25:31**  Sigma n 0 because the hash of the message 1 raised to the coordinator secret key multiplied with hash on the message m 2 raised to the coordinators secret key which is since in our case the hash function is the Patterson hash equals H 2 M 1x and one is our secret value and the other term is h2 m2x HSN generator in

**00:26:02**  the group so this equals H to X multiplied with n plus and M 1 plus M 2 so the point is that if we give these two values the coordinator then the coordinator can just multiply them and check this equality so note that this on the right hand side H to the X multiplied n plus M 1 plus M 2 can be easily calculated by the coordinator so access and the coordinators private key

**00:26:33**  and 1 and M 2 is the public values because we this is the value of the output UT X so we are registering so the coordinator can compute this term and similarly the coordinator can just compute the multiplication of the two signatures so the point here is that this verification equality can be trivially checked by the coordinator so this is a super simple way to convince the coordinator that look I have two

**00:27:04**  valid signatures on messages I'm not going to tell you but still you can verify that the underlying messages add up to this public value so with that in mind we basically solved on the problem of splitting UT exo's and merging UT exo's so basically the wabi-sabi is ready right what do you think guys okay

**00:27:38**  so shall we kill the Joker or you want to think about it by the way this is if you go to Lobby subbies so github.com /zk snags the slash wabi-sabi and the fifth issue if you want to take it as a homework or exercise to think about it don't scroll that much down because here you will see why it is broken but yeah we were like in ecstasy in in half

**00:28:09**  a day and then through the reality hit it yeah okay there are some subtleties like we would need some padding scheme but yeah okay many questions comments on the on this scheme okay so let's meet but what was the problem with this and what was the

**00:28:41**  overcomplicated solution okay so so let's give the protocol in two minutes so the firm let's start with the obvious mistake which was pointed out by Kobe good cam good friend of mine so again tech thanks cobby so the obvious problem with this is that never ever so yeah this is the description of blind BLS

**00:29:11**  signatures and anytime you would like to implement it as a practitioner or or you want to deploy it in the wild you need to choose this hash function and one of the key takeaways here is that you should not choose blind be less signatures with the Patterson hash because then you you completely break the underlying security properties of the blank pls signature scheme why because so this is the solution pointed

**00:29:47**  out by Coby if a user has a single valid signature so if the user has a message m and obtains a blind signature which has the form H to a max then a user can just Forge any signature of her choice like let's say M star and then can obtain a valid blind signature on a message which was not a very signed by the coordinator

**00:30:17**  so this is like conky Italy breaks the guarantees the security guarantees whatsoever of the blind build a signature scheme so like so if you learn something of this discussion so far like first lesson is that don't instantiate and blind be a signature with but there's an - because then users can screw you up yes and then and we

**00:30:48**  were trying to fix this protocol I'm not sure if that's a little bit complicated because then we would need to explain what our accumulators but basically you can save it but it's not cryptographically sound construction and protocol anymore because it would rely on a completely broken blind signature scheme so we were like well let's put this aside and let's continue in another direction because this is just not

**00:31:20**  kosher at all yeah and that I think this is a good point right to talk about trade-offs because you know ultimately we want to have a protocol that does communicate with a central coordinator but we do not want to have a decentralized protocol is this would increase complexity it's also staying centralized means we've reduced complexity but then for example if we would use this quote-unquote broken protocol but fixed at both the accumulators this would again increase

**00:31:50**  the complexity I then and this just carries about a lot of trade-offs no of just additional communication realms where stuff can go wrong this is one of the big ball next we haven't wasabi currently that the torah' anonymity network just breaks sometimes it does not even work flawlessly all the time and put the extra round of communications this would become more and more of an issue so so here again if we can find a more beautiful cryptographic solution that is less

**00:32:21**  complex that relies on less assumptions and increment it then this would of course be better so so that's why we decided to abandon this approach and look for something and honestly there were many red flags already from the beginning it's already you well pointed out like obviously blank signature sorry elliptic curve so pairing based crypto is something completely new and also we did some research and we found out that there is

**00:32:52**  no C sharp implementation of BLS though we as Max already pointed out like trade offs so if we would have wanted to go with the scheme then we would have needed to implement our own BLS from scratch so we also want to minimize obviously the time to market so we would like to make this available for our users as soon as possible and and yeah so yes all right thank you

**00:33:26**  just something here because I see we have someone new and I just would like to say hi Stefano would you like to introduce yourself maybe all right can you hear me yes yeah sorry I was a bit late I missed the first part but I had already seen the github issue so more or

**00:33:57**  less what you were talking about was not completely new to me well about myself master student at Alta when graduating in July if everything goes right and I have been interested in to block saying Bitcoin in particular protocol since 2 to 3 years ago and yeah I'm pretty

**00:34:30**  passionate about cryptography I have that's very maths so the mathematics down there doesn't scare me anymore oh I found it fun so I think I will take part to this kind of meetings often in the future I totally agree with that

**00:35:08**  I'm a bit sorry that I cannot help on the implementation side because I'm not really a c-sharp programmer it's completely unknown to me but all right let's continue and and I'm wondering how shall we continue because because then we went back maybe and with the idea

**00:35:40**  that maybe we can do something with our feathers and commitments scheme but what we had in mind and actually we brought a comparison between our two schemes this BLS signature scheme and our Patterson commitment scheme and what we said is the cryptography is for that Patterson commitments scheme but which is

**00:36:10**  described in the beginning is relatively simple the blind BLS signature scheme is complex communication rounds the Patterson commitment blind patterns and commitment scheme does not introduce any additional communication round while the bind Els signature scheme does introduce parallel communication round which means it's not that bad this is because after

**00:36:43**  the input registration we have to give out the accumulator for the two to the piers so they can they can create their outputs and again coin splitting in the Patterson commitments key in both scheme is perfectly solved Cohen merging in the Patterson commitment scheme is not solved so there is privacy loss there in the BLS signature scheme it's solved but

**00:37:17**  but again it could be improved by introducing some denominations but we really don't want to do that because we are kind of back to back back to some some some not very elegant scheme and that's that's pretty much it and then we went back and letters and commitments came again and I would have a question

**00:37:51**  for the whole group I mean could you maybe explain a bit more the the idea of having um denominations and held know how this would work and why this is not optimal yeah sure so in the Patterson committment scheme you can we we went through how you can split the amounts but we did not figure out how you can match the amount so for example if you

**00:38:23**  have an input with one Bitcoin and another input with two Bitcoin and then you go with two different anonymity Network identities and you you want a three Bitcoin output then you wouldn't be able to split any of those two inputs to get three Bitcoin output but you would somehow have to merge them and at that point the only idea that we had in

**00:38:54**  mind that okay you get a Patterson commitment for the one Bitcoin input and Patterson commitment for the to Bitcoin input and an adult with registration you register them together so you are basically exposing that you had a one Bitcoin you have one Bitcoin and you have three Bitcoin and where where can those come from probably from the one Bitcoin impotent probably from the three

**00:39:25**  Bitcoin input so that's not idea for this we can introduce denominations that just create a bunch of standard letters and commitments than letters and commitments with standard amounts and in that way the coordinator at least I thought would registration it will be quiet quite difficult for the coordinator to tell well often

**00:39:55**  impossible the where those are coming from and that could work but but again like introducing thousands of brothers and commitments and things like this is not very elegant and probably we would just end up having implementation issues all over the place so what s can we do with this and each twin spent some time on it at home and he came up with something which I cannot

**00:40:29**  claim to understand but then we progressed a bit further and and I'm not okay so do you guys want to chime in maybe you are better equipped to explain our further progress here I think the next thing we should like if we go over issue number 10 I think we should have

**00:41:00**  enough time to cover it based on what we already did it's quite similar because it also uses by linear groups the Patterson commitments are similar but the signature algorithm and the verification equation are different and it introduces some problems but it also solved some problems and I think that that's a good direction to to go in for today do you present to everyone like

**00:41:32**  when when your screen sharing and somebody else is talking then like I think would still be useful to have your screen show so you can click on each one and it that way his monitor is going to be be the dominant on your computer even if you are talking I'm going to do that too so the recording will be will be correct yeah for the recording thank you well I'm not sure how much time we want

**00:42:04**  to spend with this because this ad so because this is not something super known signature scheme so can I ask one more question about last topic please please do like if I understood correctly whenever you are getting the outputs from the coin zone you have to have at least two outputs am I wrong or is it that you have to have at least the same

**00:42:36**  amount of outputs coming out as you put in in inputs more we want to make make it be completely arbitrary III mean we will have some restrictions some standard amounts and things like that at upper layers but on this layer were we are working right now we want appears to register completely arbitrary amounts

**00:43:08**  and number of inputs and completely arbitrary amounts and number of outputs later we will restrict it but for now we want to to build something that's flexible and at up early layers we will restrict them the short answer would be that there is no correlation between the number of input UT X's and the number of how to do T X's they don't necessarily need to be

**00:43:39**  equal the only thing which is necessary that roughly the sum of the input UT X's equals and some of the output beauty X values minus Fe and does this answer the question yeah exactly that but what was the problem with BLS and Peterson signature wasn't it like that you can't like just have one output coming out if you are putting two inputs so the problem is that again just to refresh so

**00:44:11**  this this was the blind build a signature scheme like put this into your photographic memory and then if so you need to choose here a hash function you see like you need to choose something you need to go with a particular hash function and if it if this particular hash function is the peterson hash which is basically takes a random generator in the group let's say h and raise it to H to the M so if that this is how you

**00:44:43**  define your hash function right so H of M let's define it as H to the N mod P P is a prime number which is the order of the group so the number of elements in the group then you will have a hash function but the problem is that with this instantiation the signature scheme is completely broken so it's kind of really non-intuitive because you would you would just thought you one might

**00:45:15**  just think that okay I take the blind be a signature scheme I instantiate it with whatever hash function and then it should be alright right this is like what I thought but it turns out not to be true so okay yeah yeah I get that and that was understandable my question was a little bit wrong I'm new with these terms so bear with me but learning yeah maybe what I actually meant was the

**00:45:48**  problem with having multiple outputs and merging them into one output I mean what was the problem in that was it because that so the problem that just cannot have one output no no you can't have the problem is that when you want to do this you don't want to tell the coordinator what are the values you are merging because then the coordinator might guess

**00:46:18**  from which input UT axis you are trying to merge and then you would leak you would lose some privacy against the coordinator does this answer the question oh yeah exactly so let's let's say you have two input UT axis like I don't know 0.1 0.2 and you want to register an output you TXO with value 0.3 then you want to do this in a way that you don't want to tell the coordinator then now pay coordinator now I'm merging 0.1 you tx1 0.2 because then

**00:46:52**  the coordinator might guess okay this is raffia this is because yeah so this is what we want to avoid and to put this a little bit more formal you want to convince the coordinator that you have valid signatures on messages that you don't want to tell them because usually if you verify messages as digital signatures then in the verification algorithm you also put the message itself as an input right but if in this

**00:47:23**  case you would put them messages and input in the verification algorithm then you would lose privacy or some privacy and and we need to come up with a way to verify messages digital signatures without giving out the underlying message that that's the cryptographic challenge here okay yeah thanks that explained it yeah so basically this is the challenge of the main challenge of wabi-sabi of this

**00:47:55**  protocol today thanks to your value is we have a pretty neat solution which is I think the most lightweight but not sure if we will be able to cover it tonight yeah we have basically two more protocols left right do you do you want to go through your your protocol that that that you came up based on the knowledge assumption paper or or go right to the

**00:48:29**  to the to the last one yeah maybe gold right the next next one I can wrap it up in five minutes so like it was kind of obvious we motivated a thousand times we love others and commitments because it's homomorphic so we were looking for blind signature scheme which allows us to have a blind signature on a message committed in a Patterson commitment and apparently there are two schemes achieving this this paper and another one by Foxborough

**00:49:00**  at all but it's a little bit more complicated and then we were playing around with this scheme wait a sec and I can show you yeah this is the blind signature scheme which I suppose in the group only one or two people know but don't worry this is not that well-known paper yet and and then we created some proof mechanism which allows us to do

**00:49:32**  utx so merging so splitting is basically given for free because these blind signature schemes gives us blind signatures on committed messages on patters and commitments like here this is additive notation somewhat different than the previous notation don't get intimidated so basically here this is the message which is committed in the Patterson commitment and at the end of the day we will have a blank signature on this message without the court letting the coordinator know what she

**00:50:04**  was signing so we have input UT access splitting for free and then we were creating some zero knowledge proof systems to allow us to do the merging but I don't think it's that important because it's a little bit would be too long and I don't want to waste your time you can see all the discussion here on blind things on Patterson commitments hashtag ten number ten yeah here's the protocol which

**00:50:35**  achieves this merging yeah maybe I think it would be more enlightening if you would hear the easiest way to do it all right let's do that let's let's do that first on what could you go on the the issue yes please share your screen because I cannot because that doesn't get recorded very social issue that I created and and after that you've uh but

**00:51:08**  let's first go through on mine double blind is competitors income cool right so I I want to go through this because this might be easier to understand and you was is is something that that's very similar to this we kind of came up with it in parallel I mean I can't really claim that I came up with anything

**00:51:39**  because I was just coming up with desires that it would be cool if the crypto would work this way but anyway so yeah yeah go go go back yeah so the idea was that what if instead of we blind the patterns and commitments once we could blind them twice wow that would be really cool wouldn't it so okay we blind

**00:52:10**  them twice and in that way we would get the signatures for the single brightness commitments and not the double blinded and those single-blind that commitments could be registered together later on because a and and and the some could be proven easily and because no one has seen because the coordinator did not see those singer blinded commitments and we

**00:52:41**  have signatures on them it can accept their some and we don't actually expose the amounts so this was my idea and you will had a better one based on the the paper that we actually looked through last three search clubs so that didn't go to waste and I would like to give yes

**00:53:14**  do you have any anything to add to my really incomplete conceptual explanation or or go through you guys stuff which which seems be a more fine now I don't know let's see so do you have anything to add to this so far or give the word to you but no let's let's give the word to you well okay so I guess can you open

**00:53:48**  issue sixteen I guess the first thing is we should give some credit for this idea of double blinding the commitments and that comes from paper relating to Z Coyne lalangue tus I think it's cool and the idea there is you kind of it's not a signature based approach but there's a lot of similarities and you

**00:54:19**  use other people's like every coin is basically a Patterson commitment to an amount so the amounts are confidential like confidential transactions and then you take additional coins as like decoy inputs and you kind of prove that you only spent yours in the output creation but this kind of where we got this double binding concept I think it's I would

**00:54:49**  prefer if we refer to those as like unlink of all commitments just because double binding I think means something specific in in that article so a similar thing is instead of blinding instead of taking a Patterson commitment blinding it and receiving a signature on like the unblinded version the anonymous credentials light signature scheme does

**00:55:20**  something a little bit different where you you give just North Edison commitment and in the anonymous credentials work the the thing that you're actually signing there is what like that's what they call an attribute of the credential so in this signature scheme the the user commits to a list of attributes as a Patterson multi

**00:55:50**  commitment and then has a protocol to get a signature not on that commitment but a different commitment a blinded commitment that still commits to the same values so it's practically the same thing instead of like blinding getting a signature and unblinding you provide like one commitment and you get back a signature for a differently blinded commitment to the same messages and I

**00:56:21**  think probably we don't want to go into too much detail about how the the protocol actually works it took me literally hours to just get through one page of the paper and I still don't think I understand everything so I think like that is a reasonable summary of of what what that construction actually gives us and then we can sort of recover the nice properties of the second protocol that

**00:56:53**  we didn't discuss in too much detail so unlike the the BLS signatures the signatures are not homomorphic so but the commitments are so we can still have splitting we can make a series of commitments to the split amounts that we want they remain hidden and then we receive we prove that the sum of these commitments is equal to our input amount and then we receive a list of signatures

**00:57:27**  on different commitments for the same amount and those signatures don't have like the double spending issues that we we ran into with some of the merging stuff or the signature forging so at output registration time I just reveal those signatures and each signature is like a token but because the verification equation for this signature

**00:57:58**  scheme works on the commitment not on the message instead of giving the sub amounts that we're like let's say I I have two inputs and I want to take like some I sorry I want to split my first input and I want to split my second ad but and then I want to take two sums out of those for some reason at output registration I provide two signatures and two pettersen commitments for the split amounts but I only need to reveal

**00:58:30**  the sum I don't actually reveal the message at signature verification time so this gives us a slightly easier to reason about way of proving to the coordinator that we're not overspending in our output registration without actually revealing the sub amounts that we we only reveal the sounds um I think that's a fair summary

**00:59:01**  I guess does anybody have any questions at this point and if like we want to go into more detail I can make maybe explain a little bit more about the signature algorithm itself thank you I think we can actually leave this for the next session to go into details in this while obviously if if we we don't find something is terribly wrong with this

**00:59:33**  and then we have to start all over again if we find something terribly broken then we I think we have an even better reason to to do a research club bonnet it was solid if it was solidified the next for the for next week then then we are go through it if it won't that's it that's something to add about the

**01:00:04**  signature scheme an attractive property is that it does not require bilinear groups it's still Jana said last week that some parts of the security proof rely on so like you for a curve with say 128-bit security like set P 256 K one you actually get a slightly reduced

**01:00:35**  security level I have not yet gotten to those parts so I don't know if this is an issue for us but at least in principle if that's not a concern for the soundness of the the protocol and the the privacy of the protocol actually the privacy is much more important if that's not a concern then that means that we can just use the same curve as Bitcoin which has some nice advantages

**01:01:07**  as well all right so was everything clear no yes I mean I only have some new questions so I'll maybe leave them to the end and give other guy's a chance to ask I've

**01:01:39**  never heard this concept of double lining or you know double and Patterson commitments yes exactly what's my question it like do we have some peer reviewed like proofs that this is sound or which is hoping here paper was showing the double blinding Patterson commitments but but but he was but but the ACL paper idea is

**01:02:12**  actually not reliant on these doesn't use double blinding it's what what does it use what would you say that I think it's a slightly technical but the idea is so okay first I don't remember the exact details of the double blinding but from a security point of view there's no there's no problem really because you

**01:02:46**  it's just like adding another factor to the one of the generator points so you can think of it as taking a Patterson commitment and I think multiplying it by a scalar that's no different than what you do in a normal Patterson commitment it's just like the the way that the Lanza's paper uses it is the second blinding is like a serial number and if you and that's used for the way that

**01:03:19**  like Z coin does a double spend prevention or like makes marks a coin spent basically so since our scheme is online we don't actually need that and what we have in the ACL scheme is a sort of similar approach where you start with a commitment and then in the signature protocol eventually you get a signature on another commitment that's multiplied

**01:03:50**  by a different scalar so actually I'm not sure if it's a scalar and I'm not gonna check just now because but like think of it as like adding another key like tweaking a key if you're familiar with that terminology you're just taking a curve point and adding like more like another point to it and because of like

**01:04:20**  the reasons that a Pettersen commitment works out as like a secure system this you know generalizes to repeated transformations like that if that did not hold then like the Paterson commitments themselves would not work so I think that double blinding term is a little bit scary but really all it means is like firstly blind it and then you blind it some more so in the ACL scheme

**01:04:51**  that process like in the the Lantis stuff you you first you you do that blinding and then you you blind some more and then you prove something to the blockchain about the like the the composition of these in the ACL scheme you start by blinding the amount once in a like a normal Paterson commitment and in the end you get a signature for a different Paterson commitment that has

**01:05:21**  like additional blinding applied to it but still commits the same thing so it's kind of the same effect you there's no way to link the two commitments because the user controls the randomness going into the the derived commitment but the underlying messages are still the same and the ACL protocol basically guarantees that you can only get a signature that commits to the the same stuff that you made a commitment to at

**01:05:55**  the beginning of the protocol did that explain it a bit better yeah the double blinding thing was now a bit more clear but yeah I think I have to just check this show again after it's published so I get everything out of this I mean this ACL thing is still a bit confusing

**01:06:28**  but I don't think it's I just need some time to process it but yeah thanks for all the explanations I have a question I don't really know if it makes sense at all and it's on a higher level so is

**01:07:05**  there any interest or do we see any particular problems in willing to output from such coin join an output which is multi signature in some way so it's a double question does it even make sense to think about it is there any use cases for it and is it technically thinkable

**01:07:39**  with the within this scheme yes and yes I think there are many interesting use cases for multi signatures I'm not sure if no power agrees but did all of this stuff is only concerned with the amounts of the outputs not the scripts themselves so when you go to register and output if you want all the script types to be the same the coordinator can just say you know when

**01:08:11**  you register and output you must provide a pay to pop key hash output or something like that or it it could let you put any script type that you want but the the cryptographic commitments that we discussed so far are only concerned with the satoshi amount that that output will get not with the script pub key you could even register nope return so yeah so and further maybe public key

**01:08:47**  tweaking to make it more efficient you know the maybe the only thing that I that could be an issue here is that you want to give a maximum size for this script that may be smaller than then what Bitcoin would then what the Bitcoin standards are because you don't know who is paying for the for the script so that

**01:09:21**  input registration you you have to take the network fees from people and and let's see if everyone would come with the maximum script sized script that would be a denial of service attack or things like that gets to there because if the coordinator produces a non-standard transaction then it's not gonna get relayed but the beta script hash completely gets around this problem

**01:09:52**  because the script pop key only contains the hash of the script and there's no standard Ness rules restricting redeem scripts so unless you want to do like a raw multi-sig screen pop key or something like that I I don't think that's really an issue yeah I was thinking more about well it's not there yet but I was thinking more about Shannara multi signatures so that wouldn't be so if we get tap script

**01:10:24**  outputs or the set with v1 outputs they're gonna be even simpler then because you're only really gonna have one script type it's always going to be 32 bytes and it's functionally equivalent to a paid to puppy hash and a pay the script hash at the same time so you can always after like as part of the input of the next spending transaction you can provide a tap script that

**01:10:55**  redeems it or you can sign with the I forget what it's called that the key at the the root and that would be I mean it's not a pop key hash but it's like paid a pub key so in this regard if tap root is enabled and we also have snore signatures in in the same go then like the there's only going to be one script type that's relevant for said with v1 outputs yes so we probably have

**01:11:32**  to restrict arbitrary non standard script some of return output as far as size is concerned but but any script that someone can imagine because because of the PTO's script hash shesh script hash kind of constructions which are actually the standard way of doing things so you can you can do almost

**01:12:05**  anything except non-standard stuff so maybe a trivial example but or trivial use case I was thinking whether it was possible to have a [Music] lightning tunnel creation as a output from coin join round so since that's the weakest point in the in the privacy of

**01:12:38**  lightning you have public keys associated publicly to some multi signature transaction which is the funding transaction it would be nice to be able to provide privacy while going in into the protocol so it's not possible to trace back coins the history of coins that create a fund a

**01:13:10**  transaction transaction so this is something I've thought about quite a bit already today you can do this with single funded channels and join market and there's no technical reason whatsoever why this should not be possible in wasabi that's just a question of the transaction structure that's currently enforced that requires pay to witness pub key hash outputs I

**01:13:42**  think that in this protocol that we're proposing that's not going to be any different it's up to the coordinator policy to interesting things to consider about this are it's not just that so like coin joints can help lightening privacy but lightning can also break coin joint privacy because the outputs are announced on like the the lightning

**01:14:13**  graph the the gossip protocol so like every node that has public channels has a stable identifier its node ID and it's basically linking a bunch of multi-sig outputs that it's involved in so I still think it's probably a good idea but there's some really tricky interactions to consider there and it may turn out to be less desirable than

**01:14:46**  it seems at first and it's a little bit more interesting with dual funded channels so there's in the last few months I think Lisa negged wrote a proposal for interactive channel opening that allows dual funding and prior to that I think it's a generalization of a prior work that is meant to deal with splicing which i think is also very

**01:15:19**  interesting to consider in the context of coin joints I think that the main advantage that you gain is if you want to open a channel to some other node and you don't want to disclose how many funds you had in a prior YouTube so that you used to fund this then you get a considerable benefit from coin joining this and that's already possible today with sea lightnings like API and

**01:15:50**  something like join markets patience and just one actually had wrote a paper previously so I would love to hear his input here to know sorry for interrupting you but I feel this was a really nice example on how like non-trivial ways some can reduce the Hana limited set because like when

**01:16:20**  Stefano was asking the question I was like wow this is a nice idea but then I realized that if for example in today's if you go to graph dot L in the Explorer comm slash API slash graph you can actually have a look at all the nodes consisting of the public public graph and you can investigate it essentially like less than 1% of all the would use tor and which means that the rest of the 99% of the nodes exposes

**01:16:53**  their IP addresses so essentially if you would use if you would do this like Cohen joined out to a funding transaction then you would instantly lose one guy from the coin joint because most likely that guy will just use lightning with IP addresses and then you would instantly know that this guy lives in I don't know Chicago or something like that so yeah this was a really nice point from Nevada and great insight and

**01:17:25**  not only that one output but all of their other channels as well yeah I mean they're lightning as a lot of privacy potential but currently it's just so up Ted eventually will probably have to do it in wasabi to be privacy focused but in general I think this is a very promising idea to do Kong joins into good Lightning openings they're lighting channel openings and especially into something like lightning channel factories or maybe Hyperloop Atomics box into or out of the Lightning Network so

**01:17:57**  I think there's a lot of huge promise here very long term because right now the Lightning Network simply it's not hit there you see the philosophy that I changed from when I when I was writing zero linking in C rolling I wanted to ensure standard behavior from an everyone who is who is mixing but now

**01:18:32**  here is I don't want anymore I want to ensure as much flexibility as possible and the clients has to work in a standard way until one or two client wants to to work in a different way like he wants to open a channel let's say and and you know if

**01:19:03**  it's easy to put the cut in to the microwave accidentally if you are behaving differently from other people but in this case from how we are working on here is that if you are actively if you actively want to do something then I don't want to prevent it anymore that

**01:19:34**  the only point the only goal is to most of the the peers are are using the default stuff and not messing around with with with different parameters so so yeah that let's not prevent things but make sure that most of the peers are using the default parameters so so anonymity is and isn't terribly

**01:20:04**  compromised if if some someone wants to to create scripts all the time or open lightning channels all the time things like that that that's what I I want to do differently in this case if we want to really philosophize then a long term like think of the just a thought experiment but if every coin join

**01:20:36**  instead of having multiple inputs and multiple outputs had only a lot of inputs going - a giant multi-sig for everybody and a multi-sig coming out of that and the coin join theft prevention security worked by exactly like lightning funding so you don't sign the first transaction until everybody else has signed to the output transaction this is all really silly right you you

**01:21:08**  gain no benefit it's now it's two transactions and the interaction of a multi-sig is probably a catastrophe but what you get out of it is something that's very similar to a multi-party payment channel and I think like a very interesting long-term I mean this requires soft Forks and all sorts of novel like technology but it would be really cool if the anonymity set of coin

**01:21:41**  joint type transactions was not just a moment in time right where people could sort of come into a pool and leave at some later point much like a multi-party payment channel so that anyway I just think this is a fascinating idea and something I've been thinking a lot about how maybe one day we get it but it's all very you know just in the future stuff

**01:22:12**  it's like similar I think but so I think the Lightning privacy model I think is fantastic for payments it's terrible for coin history's so like what you basically announced to the world is here's how much money I have and then at some later point you announced to the world this is how much I have now

**01:22:44**  whenever you fund or close channels and you don't disclose you know the the transactions that you did in the middle and this is exactly the opposite of the kind of privacy that coin joins give which is like you completely obscure the history or not completely but you you obscure the history to a reasonable amount but then people can still see the net flow on the pay drawing ideas they

**01:23:17**  kind of break that assumption but in in principle you could you know continue that in a much more general direction where I think payment channels coin giant transactions page oint type interactions things like covenants all of these things go together in a way that's beneficial for privacy it's because privacy because fringe ability is emergent from privacy it's beneficial

**01:23:47**  for the network as a whole and it's also I think great for scaling because effectively you use coin joins it's like just a batch transaction mechanism so you can think of like the the logical end state of this is every like you have blocks just filled with giant coin joint transactions which basically are snapshots of of channel states and people just move in and out of channel states and the most of the the actual

**01:24:21**  activity is off chain there's some issues with that which is you know what happens if people stop cooperating and then your block size is too limited and some people can't exit so still not straightforward but I I think the general intuition of putting is little information on the blockchain itself about what sort of interactions people actually have like what actual payments they send to each other that has benefits for scaling for privacy and

**01:24:52**  fungibility so I would really like to see all these things converge long term anyway this is really off topic I'm sorry so one of the most interesting ideas there is up CTV up the cheque

**01:25:23**  template verify that's Jeremy Reubens covenants construction and there's some really cool stuff that he demonstrates like his proofs of concept for things like congestion control transactions I think that that's the most interesting direction that this stuff can go in and with something slightly more general than what he proposed like we could get some really awesome stuff

**01:26:13**  closing the conversation and I hope everyone enjoyed this cryptography lesson this one and half an hour cryptography lesson and now you can go to your universities and tell them that you applied what you learned there and okay thank you guys next week we are not going to have a

**01:26:44**  topic but the topic is going to be that wabi-sabi repository whatever will happen there I don't know as you can see we have two guys working on it who are much much smarter than then and you know I know it's extreme being brain power is on that repository so we will see that what what's going to

**01:27:16**  happen next week what we are going to talk about and that's it thank you for for watching like share and subscribe contribute to to between privacy and see you next week bye bye I think I died right

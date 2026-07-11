# Wasabi Research Club #15 - Anonymous Credentials with Jonas Nick

- Playlist index: 15
- YouTube ID: `pgErjQSQQsg`
- Video: <https://www.youtube.com/watch?v=pgErjQSQQsg>
- Duration: 0:46:28
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  to approach this is to look from the point of view of blind blind signatures right I guess blind signatures are mostly familiar to this audience right yes more should be should be familiar far be wasabi user where every was a beeper user I guess so the idea of credentials is similar in the sense that

**00:00:30**  you get some blinded token that was signed by some server and the server does not see the message that was being signed now the additional idea to a credential is that it's not only a message that it's being signed but instead it's multiple attributes that can be signed and these attributes can be anything and now the interesting

**00:01:00**  thing is that you can selectively reveal these attributes you can say here I have a token and in this token there I have there is this attribute and it has this value so the NOC standard example is you haven't token from your government let's say and it says your age basically your or say that st. birthdate is is one of attributes and then is signed now what

**00:01:33**  you can do with that you can only show your attribute you can also show that it's in a certain range you can do a range proof so what you would do is if you go to the cinema you don't have to reveal your age you don't have to reveal anything else that is included in your credential you only have to show that you are older than 18 years and that works with such a credential and these attributes are pretty flexible you can

**00:02:04**  for example besides range proof system you can show that if you have two blind tokens attributes are the same for example yeah so mathematically I think the best way to think about this is as Peterson multi commitments so in normal Peterson commitments right you have some

**00:02:35**  randomness and you use that to commit to a value and you basically have two different generators group generators now with these multi commitments used in some of these credential approaches you have randomness and now you commit to multiple attributes and only a single one and usually you have as many generators as they have attributes so I think historically one of the first

**00:03:07**  notions of these credentials was by brands I think Peter price not quite sure he has he wrote his pH pH TV yeah okay um Francis's last name and he wrote a PhD thesis about his idea of doing credentials and it's actually quite interesting I can recommend it it's um

**00:03:41**  not too technical and he has a lot more ideas than just credentials and but one problem with it was that so far every attempt at proving its secure in the random Oracle model failed and this is where this anonymous credentials light paper comes in because they have a construction that is provably secure and

**00:04:16**  it you can do basically the same things or very similar things as with credentials there might be one minor problem this one last time I looked at it I did not really solve because in the paper they say for 128-bit security we recommend using a group of 576 bits and of course our sakti group is only 256

**00:04:47**  bits so it's not sure if you can use that it's often the case that due to the proof these groups need to be much larger than they are used in practice even for snort signatures our website or our secti group would actually be too small for 128-bit security mostly people say yeah let's just an artifact of the proof it doesn't really matter that much but in order to verify that we need we

**00:05:18**  would need to look into the proof more closely yeah thank you yeah that's almost everything I wanted to say like the other thing I wanted to say is that these tokens are pretty flexible compared to just more signatures so at the building of Bitcoin conference 2018 I talked about how to

**00:05:52**  use this to basically swap a token that is in or that it was created with an anonymous credential with an untrained or off trained bit cone on lightning without the server knowing that this happened and without having to trust the other party yeah thank you I'd like to point out so we are reviewing right now a paper called anonymous credentials light and as Jonas pointed out this is

**00:06:23**  an improvement on the brand's credentials in fact it has it has one difference between the brand Bank credentials well where this is more secure of course because the brands contentious couldn't be proven but actually these tokens are unlink yes on linkable with each other so if you have a credential you can create as many blind signatures for it and you can

**00:06:56**  prove that credential as many times as you want unlike the brand credentials because there they are linker bus so you can only use up to as much signatures as much the the the the designer allows you in in our case would be the coordinator so that's actually something that we would desire if we would want to build on top of this anyway if I may add to that I would say

**00:07:30**  that brands credentials are also unlink able and if you can talk to the server right because that's what you also usually do any cash you basically show the serial number of your old token you create a new token you show that the tokens are the same in zero knowledge and then you get a signature on the new token and that way you get an unlikeable token I think the advanced anonymous credential slide is that you can do that

**00:08:01**  without having to talk to the server yes it's called I think rash once or that's what usually comes up anyway so a bit bit more there because the same out or they're working on this this for are for probably a decade after this paper and and they actually came up with something called mercury are signatures where they

**00:08:32**  don't need so much crypto as much as in this paper but but in a very straightforward way they could achieve the exact same thing with with these mercurial signatures and even more they were working on something called delegate Abel anonymous credentials and there are the three keys that you could actually delegate the ownership of the

**00:09:04**  credential to someone else so in our case that would be I think giving money to someone and I wouldn't be able to redeem it but you would which is actually pretty nice oh my god I wasn't talking last thing you said was in our case that would be yeah it's it's interesting because I think it's

**00:09:36**  recording everything what I'm saying but you didn't hear so I think what the studies in our case it would be that we could give the we could give well pay someone in a coin jury round without us being able to redeem it but that someone would be able to redeem it as an output of the coin join so so I just wanted to point out that del tours were actually working on this this line of research

**00:10:08**  for a long time and they think they came up with much better constructions and easier ones too so if someone would like to look into these anonymous credentials and definitely look into the newer stuff there okay so far any comment here because I want to approach it also from

**00:10:40**  coin joining point of view that why did we why did we wanted to use it and why we don't want to use it anymore so in the the problem that we are trying to solve is be able to to to have some kind of dizzy divisible ecash system actually that

**00:11:11**  that allows us to come with any input in in a tour ident in unanimity network identity and then we we get back some some credit for for for that input and and if we come with another input later then we get back some credit and then somehow we can combine those credits and came with only one output or we could also break those credits down and with a

**00:11:44**  with a stupid blind signature scheme we would have to create a bunch of denominations and a bunch of signatures so why this paper would be handy here because we still need to create the bunch of denominations but we wouldn't need to create a bunch of signatures the user could create the signatures the blind signatures for their credentials

**00:12:16**  later however we actually came up with with the solution based on homomorphic cryptographic commitments range proofs and blind signature scheme that that that works with the Sohma morphic cryptographic commitments in a way that we can actually come with an anonymity Network Identity register input get back

**00:12:47**  something come with another anonymity network identity register another input get back something and we could combine that to something in zero knowledge that in a way that we could prove this error that we could make any kind of outputs out of those and we could have done it with this credentials in some way or form but we

**00:13:19**  would still had to have denominations in order to to achieve some kind of privacy that that was the the thought of blind right so I understand instead of registering all inputs at once you would be able to registering them with different identities right yes we can come with different identities with any

**00:13:51**  any number of inputs and with we can come with different identities to to register any output that's but so so you would provide a let's say one Bitcoin input and another one Bitcoin input later and then you would get to one input one Bitcoin tokens and that could be used to add a to Bitcoin output or

**00:14:23**  something like that and you don't have to show that your inputs where one Bitcoin you just show that the sum is equal to two bitcoins yes in fact even more we can merge them and break them down in any way your shape or form I'm not sure okay IV a risk because this this session is about anonymous credentials and I will

**00:14:54**  bring up some topics but yeah I will a risk risk it to explain playing it to you because it's it's really interesting I think it's really no no but you can think about it the breaking part is easy and and I think that that you understand it easily and I can explain it to you because if you have one Bitcoin and you want to pay zero point one Bitcoin to someone then it would be like this you

**00:15:27**  create - feathers and let's say feathers and commitments 20.1 Bitcoin and 20.9 Bitcoin those will be your outputs in the coin join right so far it's clear so and then you register that two patters

**00:15:57**  and commitment and Patterson commitment for four for your one Bitcoin input and you of course tell the coordinator that hey this one Bitcoin input I'm going to prove that it is mine and this is the sum of my feathers and commitments by the way we create more feathers and commitments with with zeros but but it

**00:16:28**  doesn't matter for for now make sense and then we also found the blind signature scheme that works with feathers and commitments so the coordinator can give us something from what we can create a signature on our values which is cool because then we can just come at output registration that

**00:17:01**  hey I'm registering this zero point one Bitcoin output and I have a signature on it and with another anonymity network identity hey I'm registering this zero point nine Bitcoin output and I have a signature on it so this is the breaking part and the merging part is is different because we couldn't figure out with the with patters and commitments

**00:17:31**  range proofs and yeah of course that there needs to be range proof along with the patters and commitments but III think that's obvious anyway we couldn't figure it out we with blind signature scheme on Paterson commitment but we actually had to use BLS signatures and with that we could figure out how to how to merge together more than one commitment yeah so it's

**00:18:03**  pretty cool yeah any question on that or we can get back to this paper yeah I don't quite understand why that wouldn't work if you if you not say have a point one and a point nine talk bit Co and talking right yes don't you just have to show to the server that both tokens some up or or maybe even better you create a new token with a one

**00:18:35**  Bitcoin value you don't show the server your or the value of the new token and but you show the server that the some of the old tokens is the value of the new token wouldn't that work for your dream your first suggestion yes that works it just there is some probably negligible privacy loss right like you you tell you expose the server that you have a zero

**00:19:07**  point one between and a 0.9 Bitcoin feathers and commitments and the self I don't think at least with anonymous credential slide I don't think you have to do that necessarily I think you can show that the sum is the value of your new token and you don't have to show anything more to the server I think with your first suggestion I was talking about that right okay that that's not a

**00:19:40**  huge privacy thing so it can work but we figured out how to do it even without that so your second suggestion could you repeat it maybe a match I thought I was only making one suggestion here so perhaps that was that I'm not sure what the second one would be so your first suggestion was to take two blind signature of 0.1 and 0.9 and

**00:20:14**  register them together to the server to the coordinator is that correct perhaps I wouldn't call this registering I would just call this like perhaps like just a reissuance we've used that term before you have a token and you just want to get a new one with a new serial number and these tokens are on linkable and the same would work if you show two tokens

**00:20:45**  and the new token where the new token is the sum of the former tokens and you don't have to show the actual values to the server you just have to show that the sum matches to the new value and then we wouldn't have that privacy laws of having to show the individual values of the old tokens yes so the thing is we get this signature the blind signature

**00:21:18**  on the data itself which means if we want a reissuance face there then we would have to expose the D values okay so there might be some some scheme that works with that well we'd be Ellis signature we actually figured it out how to do that because they're the signatures actually has the message

**00:21:51**  itself so it's really fresh I just learned about it today and-and-and-and something like that that you can give the two two blind that'd be a signature too the coordinator and proved that their sum is dis value and because of the blind BLS signatures are the the unique

**00:22:21**  tokens there this way we won't have problems so with anonymous credentials I think you would have to you would have to to create a bunch of bunch of denominations all right I don't think so I think this is exactly the magic of these anonymous credentials that you can

**00:22:53**  do these some proofs similar to what you just described with their BLS signatures okay I okay that's yeah what we came up with indeed but I'm not sure in this paper yeah I remember correctly perhaps

**00:23:24**  they're not showing this in this paper but this is something that is like a central concept in the bronze PhD thesis and I believe you can do the same thing with anonymous credentials because both types of credentials look actually very similar all right I'm not sure if it

**00:23:57**  would it make sense to start investigating this instead of doing it with BLS signatures actually I think I don't know I would do whatever is easiest actually because I guess for your application or in general does make too big of a difference if you use be late I mean if you think that parents are secure and BLS signatures are secure

**00:24:29**  and this whole bunch of crypto sanctions and I think you can just use that if that's easier I don't think you have to restrict yourself to something that is that works in the discrete logarithm paradigm the discrete logarithm program you know they use parents so it's different different curves and different cryptic assumptions okay

**00:25:00**  all right so yeah I I'm not sure it is easier for us because the implementation since ours I think still looking behind of the BLS signature implementations so on the other hand it's it's such a simple scheme that even they could explain they could even explain it to me who doesn't understand crypto that much so okay the BLS doesn't have

**00:25:32**  implementation and if so how is it count so I can find it I think it does not have implementation in c-sharp it has for a couple of languages I think the main implementation C++ and there is bindings for that okay I think there's an implementation of brands credentials in c-sharp right let's see you prove library okay yes I was playing around

**00:26:03**  with that in fact I ported it to dotnet core and it's not that obvious how to use that but the code is very very clean and very nice so I would have loved to go with you proof what's the problem with you that doesn't solve our problem as far as I understand it you see I need a bunch

**00:26:36**  of stuff to do with that also people are talking about that it's not very secure and things like that no one's found in a vulnerability yet brands credentials own as far as I know [Music] no it's a difficult question but I think the the some proof that I mentioned earlier should work just as well with

**00:27:07**  brands credentials you don't need multiple determining denominations because brands credentials would be able to prove the sound and does it have the how good range proofs applied to that yeah you probably still have to do this range proofs to show that the values

**00:27:39**  don't overflow but I I'm not sure the you proof library does that already for you and it really looked into the library never and what is there is how about the merging of the coins I think that could be a problem there that you cannot merge two attributes together in

**00:28:10**  a way that it both prevents the bus spending and and you don't expose the attribute you know the values only the some of them I'm not sure that that's possible I think it is I think that's the point of branch credential if you do a reassurance you don't have to show all the attributes

**00:28:42**  you just assure the server you prove to the server that your new token doesn't have any other value than the sum of your old tokens combined I think and this is possible with brands credentials you don't need their age when is there yeah you would need the reasons okay so now finally there is an argument why our scheme is better because we don't need

**00:29:13**  race okay but for unknown credentials light but okay so that sounds like something that BLS or parents could do like merging different credentials together without communication with the server so nice to me that sounds plausible yeah actually I'm just going to read a few things about here is that

**00:29:45**  you prove about you prove from the the article that to be for everyone knows what we are talking about from the efficiency point of view therefore the you prove credential system based on brands work acquired and implemented by Microsoft CMAs attractive you prove does not allow on linkable use of credentials in order

**00:30:17**  to unlink ability use a credential again in order to unlink ibly use a credential again a user must get it reissued which while which which actually suggests that in fact that this paper doesn't have linkable credentials only on on linkable on these lines don't suggest that but

**00:30:50**  that's what's in the paper let me see one more ting there when such a proof is carried out it cannot be linked to previous uses of the same credential or any other identifying information about the user oh yes this is this is what I what I'm talking about here we actually want the opposite in

**00:31:23**  order to avoid the bus spending we want to use we want a used to be linked to previous uses of the same credential which brands provide and this scheme does not I'm not sure how hard would it be to to implement it would it be only a simplification or this would be a major headache to implement linkable credentials on top of on top of Asia

**00:31:56**  construct and what construct is this paper anonymous credentials light is real yeah I think that's easy because one of the attributes would just be the serial number that the server stores I mean the service tones the serial numbers of course that have been used right so okay then woody I guess yeah you wouldn't

**00:32:26**  need the Rishi once again right you don't show your serial number and then you get a new token you know if you if you put a serial number into the the attribute yes you cannot prove that scum I mean the serial number is there you

**00:32:57**  know so what you do is you show your old credentials can be multiple you show the serial numbers for each of those credentials you proof that the serial numbers are actually the ones contained in your credentials the server checks that these serial numbers have not been used you show the new token that you created with a fresh serial number serial number that you chose randomly

**00:33:29**  and then you do the some proof and that way you don't have to show anything to the server but the serial numbers we would we would create blind signatures to as many I don't know yeah the problem is with blind citizens red is blind signatures are unstructured

**00:34:02**  you just have this message and then you can put different things into the message but then you cannot efficiently prove anything about these individual attributes in your message and this is why these credential schemes are superior to the normal blind signatures yeah all right so there may be something here yeah I'd

**00:34:35**  also like to look into this pls stuff definitely that seems interesting going to link the repository in the in the comment here but don't don't share it yet because we did not figure out the name and we have a stupid name for for now okay yes yeah

**00:35:11**  do you guys have anything to to ask odd talk about regarding regarding anything maybe everyone is minute go ahead Lucas no I have no now question because I I'm

**00:35:41**  not I don't know these primitives yet so I have to study a bit more yeah I learned most of that from so Adam Beck he once gave a presentation about brands credentials at block stream so I learned a lot from him but wasn't public unfortunately I think I have the slides but I don't think they're very helpful

**00:36:12**  so perhaps the best starting point is still brands pitch these theses it's very long but some just have to check out some parts of it I think because because especially the things like this anonymous credential slide there seems to be like the difficult thing about or to grasp about it is not I mean this scheme exists but the question is how do you use it and how do you use it with serial numbers and to get ecash tokens

**00:36:44**  with multiple determinations right that's not in the anonymous credentials light paper that's something that brands talks a little bit more about as we as we reviewed this paper and we looked into that well how could we use it for ets kind of stuff then we just stumbled upon a tremendous amount of literature

**00:37:16**  there that how to do divisible in cash systems and three like a couple of hundred of paper is is is going on on this issue but the thing is they are solving things that we don't need to solve because Co injuries are inherently secure if someone doesn't see their outputs then it it's not going to sign and that here so our job is

**00:37:48**  basically to simplify what they have right there's also the concept of optimal ecash which also doesn't seem to be very practical in the Bitcoin world because in offline cash if you double spend you reveal your secret key which perhaps as if you're an attacker that's not a big problem to you because you already have your Bitcoin so you don't care about the secret keys in your token you have twice as many Bitcoin and says

**00:38:19**  you would have normally so they don't seem to apply because everyone is online in fact even where the participants are online although you're not yeah this this idea of merging inputs and and so on that's really interesting I think yeah we are going to work on that and either look into that issue

**00:38:51**  that's where we figured out how things should be but we are going to to create a draft and and send it to the Bitcoin dev mailing list and and and things like that and also for the next was a B research Club each train is going to actually is going to write down exactly this scheme the cryptography part of it

**00:39:21**  and and that's what I would like to propose for the next four so we research club because as we looked through e-cash papers and anonymous credential papers and every kind of papers it looks like this is the simplest and most straightforward solution for four really arbitrary Cohen joins which we are not going to do but we would like to have that that flexibility and and

**00:39:52**  that's what lets us improve upon it in the future max asked what about server decided equal value outputs anyone understands the question all right sorry max we can't reply you okay oh yeah one

**00:40:27**  more interesting thing here max figured out that for tiny one of the author of this paper we are talking about it was actually had some involvement in town babbitt not sure exactly what but but yes she was she was doing something tomba bit okay and I think if no one would like to say anything because this

**00:40:59**  was quite a difficult paper then we can we can cut this short unlike other other conversations and we can we can go so so do you guys have anything as you would like to talk about not yet ready I mean I'm just fascinated about things that you guys talk about

**00:41:30**  yeah I think I talked about almost everything I know about it so let me know how this progresses and what you find out yeah definitely we are going to talk about our scheme and the next was Severus Club if no one has an objection or alternatively we could review Adam gives on from zero knowledge to bulletproof

**00:42:05**  paper I think that could be could be useful or or our scheme which might be more might make more sense to be honest but it could change maybe we figure out how there is something utterly wrong with this and and the next week would be would be pointless but I doubt at this point we really reviewed a lot of things

**00:42:36**  last week so should the next generation wasabi mixing technology be the topic of the rest that's a very surgical what do you guys think yeah I think it's good but there was a question from Max and that is there a difference of users who

**00:43:06**  want to be a part of the equal value denomination and those who want only specific amounts yeah no there is no difference it's equal value denominations as I imagine it right now although we did not work this out at all but I think that could be something that the users create by themselves so if I participate in a mix then I'm going to

**00:43:37**  parties I'm going to ask for outputs off of some standard denominations that I I guess I estimate other users I suspect other users are going to do too so that that that that would be but I could create outputs in any way shape or form up to the maximum limits of course as I as I would like to even do a paid to end

**00:44:10**  point transaction in a coin joint which would be neat yeah it sounds good also a really interesting thing we just had a talk with Taj Taj not gonna pronounce it so one of the guy who who who came up with the Lightning Network and he actually came up with the coins for protocol there is still some denial of service issues he didn't figure out but

**00:44:41**  he came up with the coins for protocol that of their top route ease in snorunt approaches in Bitcoin and we he could do coin swabs those could be completely unnoticeable and that's that's a really exciting so I just wanted to share this this fresh information okay

**00:45:20**  all right thank you guys and sorry for this unconventional wasabi research club now usually Aviv does a very good good job at explaining the concept at the beginning but he he couldn't make it last minute so no one could really prefer but Nick gave a great summary of

**00:45:52**  the paper so absolutely I mean you guys did a good job and thanks for that yes things thank you Nick and thank you for watching this special one all right then I guess that's it like share and subscribe bye bye bye

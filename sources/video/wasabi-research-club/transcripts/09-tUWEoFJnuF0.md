# Wasabi Research Club #9 - Anonymity Likes Company

- Playlist index: 9
- YouTube ID: `tUWEoFJnuF0`
- Video: <https://www.youtube.com/watch?v=tUWEoFJnuF0>
- Duration: 1:13:29
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  when one okay welcome everyone to another wasabi research club meeting today we're talking about a 2006 paper called anonymity loves company usability in the network effects this paper is by Dingell dine and Mathewson and you can find all the papers that we read on our

**00:00:31**  website the link is just below our github excuse me just to remind everyone where we are in the last few weeks we were talking about coin shuffle + + + cash Fusion and I've decided to call this meeting you know sort of principles in privacy or perhaps principles and privacy in anonymity networks because I think it's very appropriate to what we're doing and next week's research

**00:01:03**  club meeting will be decided by the end of this meeting you can find everything on the github just a reminder two weeks ago and last week we talked about cash Fusion talked about doing coin joins with arbitrary numbers of inputs and outputs where users all submit inputs outputs and blanks and through the magic of home Orphic encryption homework like Peter Peterson commitments we can guarantee that no one is getting more

**00:01:34**  money than they put in and we have all users verifying other users to make sure that no one cheated last week we asked the question is this really private is it secure can someone break this method of obfuscated inputs and outputs and there was a claim being made in our discussion that due to the Bell member and the subset-sum problem you are secure given enough users who possess a

**00:02:05**  large enough set of inputs and outputs within a particular range of values because the bail number is quite large in those cases and the knapsack problem is computationally difficult to solve please see videos on YouTube for interesting debate that ensued after this discussion so yes so the question posed by this paper that we're reading today is how should we think about building using privacy tools in

**00:02:36**  anonymity networks when I say anonymity networks I mean something like tour or jab or mixed minion Mixmaster or an art we care about in these calls is coin joint an eminent work relies on getting anonymity from hiding among other users and from this idea we get the anonymity set which is the concept that you are as anonymous as the number of people that

**00:03:07**  are acting and behaving like you in this anonymity Network so the author encourages us through a thought experiment to consider something this sort imagine you have an email you want to set and you have two options for email encryption on your left is a little a tiny padlock it's a light crypto security encryption scheme for

**00:03:38**  your email and on the right is a big lock it's a heavy crypto encryption scheme so you have to ask yourself Who am I going to use the heavy duty encryption or the lightweight encryption the obvious thing is to say oh I'll just use the the best possible encryption scheme that there is out there however what this fails to consider is that email encryption isn't a one-person endeavor it's something you do with

**00:04:09**  other participants and other participants might not use the same email encryption scheme that you use but not just that even if you do use a particular email encryption if they use the scheme you are using orally your privacy is hurt because the anime community the anonymity network is weakened by bad participants who don't know what they're doing and if you are really super knowledgeable about using

**00:04:41**  email encryption and there's only ten other people in the whole world that are aware of this then you have another problem which is that are you really hidden in this network so we're going to talk about some principles in anonymity network so insecure so these are just some things that were brought up by the author insecure modes of operation are bound to be used unknowingly in those modes so if you have some encryption schemes some sort of privacy scheming and anonymity network insecure modes of

**00:05:13**  operation are big red flag optional security typically get turned off and users forget to turn them back on ever again the example that's given here is browser cookies so a lot of people click no when a site asks for cookies but then later will look yes and they'll never go back to cookie no so from then on they're always giving their personal information to sites that the isn't badly labeled us which is another problem and this is where a user has the

**00:05:50**  ability to turn off something that secures their privacy and doesn't realize that they're they're really harming their privacy because they see a switch and it's not properly labeled as a dangerous off switch so they they trigger it and they don't realize that they've heard their privacy and what's worse is that someone could convince that users do that as a social engineering attack inconvenience security often ends up being tossed aside for more convenient but less

**00:06:20**  secure methods of operation so people don't people don't want to behave in a convenient way so they'll pick the more convenient way which is often hurts that false sense of security is a big problem wearing wrongfully thinks that what they're doing is securing private when what they're doing is not secured private and then bad mental models encourage users to behave in in the wrong way and don't accurately allow the user to appreciate how private or secure their behavior is

**00:06:53**  so usability is more important for privacy this is the claim the author is making so when more users join the network existing users benefit this is the case with every anonymity Network that we're talking about and encryption is different than an intimidating and eliminated network you can excuse me with encryption you can encrypt your own files on your own computer with any encryption scheme that you want you could pick the strongest encryption scheme that's fine but when you're in an

**00:07:24**  anonymity network you depend on your peers to be anonymous so when we talk to so the example here is it is going to be tor but I just want to remind you that coin shuffle use the same idea I will just show the analogy if you recall all these users have their outputs and they want to do a coin joint but they have these equal outputs that must be anonymous and so what they do is they onion encrypt their outputs and then run them through a network of their peers

**00:07:55**  and the final result is a set of outputs that no one knows where the outputs came from only orange knows is his or her own output and yellow knows his or her own output but yellow doesn't know anyone else is outputting so everyone is anonymous against everyone else and no one knows anyone else's outputs and tor is that they you know exactly the same idea in this case the peers are tor nodes and here red wants to send a

**00:08:26**  packet maybe to a website you know pick paint a website and so he or she onion encrypts through the network you know at each layer the the at each step one layer is removed and sent the cross at any point you know someone like has no idea this has come from read at each point it's just one person passing to the next until finally purple will reach out to the website on behalf of red without even knowledge that the red

**00:08:56**  is the person that said the information so toresen anonymity network if you can't break the encryption of tor which once we assume you can't then really what it looks like it's just this big black box where users are you know entering the network and they're doing all sorts of activity and all you see is activity coming in and coming out but you don't know how to cut which person to which other person and so the first problem is that if only one person is

**00:09:27**  using tor it's trivial to see to link information going out of to out of the Tor network and information coming into the Tor network another problem is that if everyone is speaking Yiddish and doing things in a very Western English way so for example you know you know writing in English accessing English websites maybe only awake at certain times of the day then someone here for example who's Hungarian speaking Hungarian will be

**00:10:00**  easily G anonymize by the fact that they're the only person that that's doing that so usability versus security is a big problem you have to ask you know which are you're gonna take are you going to pick the slow high latency system or the fast low latency system which are you going to pick well supposing that the high latency slow system is way way better but nobody is using it it ends up being

**00:10:32**  the case that even though you know it's more secure it's better to use the faster Network where more people are currently using it and a big thing that the the author now Clay's is that easier against for max this this this section is for max yes so I'm gonna really hold it in and not say anything about Mesabi even though the

**00:11:03**  tone of my voice should hit strongly that this is talking about us but the author argues against options right so designers are faced with security decisions they leave it to the user because designers don't necessarily know what the right thing to do the protocol designer is leaving to the implementers the implementers leave it also to the users and what ends up happening users are the least able to make decisions for themselves so if you're asking a user hey you go ahead you decide abs or to

**00:11:37**  fish which which is your preferred symmetric encryption scheme unless you know what is what symmetric encryption schemes look like and you know the difference between those two models you are not the right person to answer that question alkanes make the code very hard to audit because the configuration of a particular software is exponentially grows with them with more option that you give it so if you give you know one option over here option a and one option

**00:12:08**  over here option B then whether or not option A is on or off and whether or not a PB is on or off give you four options and then you know this is clearly girls exponentially users with uncommon preferences are singled out this is a very interesting one so you give people tons of options now they select you know out of the 14 options you give them they select seven of them that is already way very unlikely to match with someone else and the default option usually prevails for casual users and so it should

**00:12:40**  prevail for experienced users as well this is a pretty big argument that's being made by the author but I think it's it's very convincing so one case study was the mixed minion and the mind case study so mixed minion is and an email anonymity Network and mine is the multi-purpose internet mail extension it's just a flag that tells you the the format of the content of an email the problem is that every email service service uses a distinct mind and

**00:13:13**  the what that means is that if if two people are using one email service and everyone else uses a different one you can clearly link those two email services to each other so one one thought you might have is well okay why don't we just limit everyone who uses our mix minion software to one format but the others talked about how if you if you limit to one format all of a sudden you don't let users send Word documents you don't let users send PDF documents you don't let users do all of

**00:13:45**  these things so what's gonna happen is the user is gonna figure out a way to overcome this problem by by making by doing the wrong thing essentially in terms of privacy and by hurting their privacy while thinking they're still doing good for their privacy and further it will end up being the case that users simply leave the port O'Call altogether because you didn't give them enough options so in the end and I was surprised to read this the the middle

**00:14:15**  ground the the best case for privacy was to allow users to behave in a diverse way but more than clearly about certain choices okay tor installation tor is what's used by only cool nerds on unique systems and then as you new users started to join and used for there was a need to quickly onboard them without a lot of a lot of explanation what beginners did not understand DNS issues so what happened is they didn't realize that tor wouldn't help at all if you are

**00:14:48**  pinging a website or the clear net for a lookup table of the site that you're looking to access so you need us socks5 proxy or whatever it is and beginners that understand this so what kind of solution is could could we do for these these users who essentially we're getting no privacy by doing this well okay the first thing was improve documentation turns out that didn't help it only helped users who read it and all the illusions that

**00:15:18**  didn't read it just continue to make make big privacy blunders the next thing was give a warning message this only created more confusion you know you would say to them hey you're you know by a by using tor without a Sox by proxy your dns is really leaked to the blah blah the user would just be completely confused about what was going on finally the the working solution was an error message that pointed to the documentation which told you sir what to do okay so this is where I ran out of

**00:15:50**  time cuz I'm a busy man but I take responsibility so we'll continue talking about the paper but I don't have any more slides so we'll just leave it to discussion Thank You Arif I think this paper was very different from from the previous sessions because it was very unique in a sense that kind of a philosophical paper but in a research

**00:16:22**  paper philosophy capice in a research paper so that said that's why I don't have much comments on it but I have something I have one two three four five questions for the author who is not with us but I have three more topics to discuss and and this might be a bit redundant because of we've talked about

**00:16:54**  it but let's let's see the very first thing I just I just want to I just want to to quote something that another area where human factors are critical in privacy he's bootstrapping new systems and this resonates with me a lot because in wasabi the other Hebrew bootstrap this thing was quite huge issue back then it's somehow all worked out yeah what

**00:17:26**  what what do you guys have yeah if I remember the early days where we had the anonymity set of five for wasabi meat sauce and of course it did not give you much privacy at all but still you know enthusiasts could use it knowing that they did not get much privacy but but knowing the potential that it has right and that it's at least you know better than nothing even if you do small realms it's it's still better than nothing I didn't not to encourage one at all so that was the reason why I used it right

**00:17:57**  first if it was the only workable solution so there was no other option for me as an enthusiast and second III I saw the potential of what this can be and that if I help bootstrap the system now that later at a point in time when others start using this you know but I can have a better tool yeah I remember finding out about wasabi maybe because

**00:18:28**  of Max's videos and all of his enthusiasm about what hobby wallet and that kind of like drove me into looking it up and yeah I was definitely a little surprised that it wasn't that difficult that I first thought but yeah I mean there's a lot of confusing little words or words that people use when talking about wasabi wallet and the coin joints in itself so I think that's a big issue

**00:19:01**  that it might scare people off just because they don't know what to expect it's interesting isn't it we have a philosophical paper and because of the lack of of technical depth in it but it's very good huge big picture document but because of the lack of technical things we are already putting on to applying it to to the best-known system

**00:19:33**  that we know about she's facade maybe this conversation is gonna be about fasabi yeah I think that we should talk about what something because there's no way to it's interesting way to nest this conversation into something that we can all understand really well so let me start by saying this this paper made me feel like I'm like I was

**00:20:07**  right about something and wrong about something from the past so one thing I was right about that more at least is this paper argues that I was right about is the idea that if we can we should make the way that wasabi works very very simple to the point where you know to explain to a user what they're gonna expect out of Mesabi it should be it should be very simple and I should stay constant and

**00:20:37**  the same so it seems like this paper would argue for that where I was wrong is is the idea of giving people a lot of options so allowing people you know for example I was very happy with the custom fee and I wasn't happening before that when there wasn't a custom fee but having read this paper I actually am of the belief that there should only be three options for a fee and if we really care about what we were doing we should accept the fact that even though you

**00:21:08**  don't get your perfect exact correct fee that you think is right it's still better for everyone else and I think that's something we should we should do across the board for all features you know the crimper giving it up because that was exactly what came to my mind to the issue of the fee like that personally love setting the custom fees exactly how I like it but after reading this paper that's very stupid to do you know you should just go with Bitcoin course Marty estimation and do the default that everyone else uses that

**00:21:39**  leads to much less followed fingerprinting but you know it also comes with the other point in the paper that although although they're having too many options an issue if you don't have many options then people will not use it right the power user who insists on having the custom fees evil evil you know then no longer used for sabe thus decreasing the network effect so I think what we have right now is a decent compromise where you know at least the average user has only the fee slider with Bitcoin core

**00:22:11**  estimation but then in these settings an advanced user can activate the custom fee and do what he wants right so I think that is good but I would know much more a much more go into that direction where I would suggest to every user to always go with Bitcoin core unless it is it is some case but it really is military yeah I agree with that what I really liked was was the idea of having error messages point to documentation

**00:22:42**  because I know we have excellent documentation and we're very proud of it but right now the problem is that most users don't read it and the biggest plus that I see from the documentation is that yahia is really good at referencing documentation when answering questions to people on on reddit so he's doing exactly what the paper recommends which is when someone asks a question you just point exactly in the documentation where it is but if we could have altering

**00:23:12**  settings like with an error message that points to documentation so you know if I turn off tour actually say error you've turned off tour here's the documentation where it explains why tour protects your privacy we should somehow be yeah I've been thinking about this too because there is a bullet I think it's called exodus' and people were saying very good things about it that it it has the

**00:23:46**  documentation in the wallet itself and that gives them a lot of confidence and I was thinking about it's it's a lot to but how do you you know how do you solve this technical challenge in a different way because they'll be waste to add the documentation into Vasavi and and it's kind of like that duplicating everything but how do you solve it without duplicating that's a

**00:24:17**  good question or is the is the system stable enough so we could have sufficient documentation or is the system is is going to change that much that it just doesn't work building the documentation into Vasavi you know I think documentation in wasabi is exactly right one thing I thought about reading this paper is about mental

**00:24:47**  models and to me it's like every time I should I open wasabi it should have ten like where were five screens beautiful graphic screens like six 102 Bitcoin with his graphic designs that I can skip if I want to like a big skip button right below but every time you go into wasabi you just feel like hey this is what you're doing this is what it looks like this is you know just some good mental models for users and having documentation and these mental models in wasabi without them having to go to a

**00:25:19**  website or reddit or daughter github I think that would be a pretty big plus yeah yes I agree Aviv here it it's I think a two-fold approach right one is to have such a starting guide to get every user on the on the same in on the same starting point and and that is definitely awesome and then further it would be for these advanced things like Evita as you mentioned when you turn off tour all right these things were many edge cases there's thousands of them in the wallet right where then one pop-up

**00:25:51**  notification comes that says this is wrong danger be careful here is explained why right so I think a combination of both is what might be useful against documentation in the wallet I'm just bringing up that there are other issues here which is the technical death that everything of has to be created in we'd be the

**00:26:23**  documentation itself and if you want to change something then you have to update the documentation it's like it's like double work and it might work when when the product doesn't really want to change that much anymore oh it's like it's like new languages it's like having your software in many different languages is awesome except that you won't be able to change it anymore and

**00:26:56**  without without fixing every single language you know that is the real issue here I mean software ones is is soft right hardware is hard it doesn't change software is soft it Taurus changes any way anymore on this you know I think one especially regarding options that is very

**00:27:27**  applicable to wasabi it's the question of manual or automatic coin selection right of course it's in my opinion one of the best features of wasabi to have the manual coin selection because there's allows users who know what they're doing to use this to a great extent but of course this also means that anyone who does not know what they're doing with just a vast majority of all users to shoot themselves in the foot and to [ __ ] up right so where where do we stand here can we or they even have the technical capacity to having a

**00:27:58**  same automatic coin selection algorithm that actually works for anyone right yes I think it's already possible but it's a lot of work and thinking and how do you do the levers but maybe that's definitely the goal right to get rid of the coins but it's not going to happen within five to ten years maybe because

**00:28:29**  it's just in grayned but but on the other hand moving into the direction of of automatic coin selection by grouping coins it's it's like semi-automatic that that would that would make sense more sense than just getting rid of the coins all together or they're just moved slowly into that direction like all the the red all the green coins and there is not really much of a difference between them so they could be grouped into one

**00:29:01**  role for example actually I would point out that there is a difference between green coins if they're they come from two separate instances of mixing as an example if I mix some coins to two weeks ago and I mixed some coins yesterday those green coins are coming from different times so an optimal coin selection would actually pick coins from across both because that would really be

**00:29:33**  confusing to in terms of linking which which user does on yeah maybe not but there are exactly the same yes they are not exactly the same but for all intents and purposes for for all the threat models they could be considered the same yes again right and in the issue that

**00:30:05**  comes up here is that as long as we rely on manual coin selection we again has user bias on on which option is being chosen right and and that can lead to to again finger printing off individual users depending on how they select the coins and so this is indeed a very very pressing issue I don't agree with that until you give me an example

**00:30:38**  hmm we think well specifically for coin selection you're talking about money own selection now yes I know for example what what what avi said that if you have two different you know clusters of mixed coins right they're mixed but they're still from different sessions of mixing

**00:31:08**  now if one user all the time selects for one transaction only those coins within one session and another user selects coins from that span across sessions you know that that might already be be from some thread model user doesn't even know that there are sessions even I'm not sure four sessions mean in this context different rounds maybe but but as far as I understood Aviv went down on that

**00:31:42**  ultrabeat hole and then ended up nowhere because it did not really really made that much sense is that correct assertion of the situation sorry I went down with this these two sessions coins thing it means having collections from

**00:32:12**  two different sessions yes yeah so the reason why I think it would make some sense is because you know if you have if you receive let's just a simple example you received one Bitcoin twice so once a month ago once a week ago and you have ten coins from both if you if you need to send someone one Bitcoin it would be

**00:32:43**  better for you to send a few coins from the we could go in a few coins from the month ago why because it so generally you don't want to send all the coins from a mix right you don't want to see like if you if you if you mixed coins and I have 20 coins you don't send all of those 20 together so how come because you you know you

**00:33:17**  sort of you've entered at one point in the network you've exited another point and the amounts are similar so there's a higher degree of link ability so what happens is is if you pointed to different times you measured right now there's a I think this is my version I think I your intuition is right which is that you know if you are mixing one after another then those coins might be

**00:33:47**  more likely to to belong to the same cluster right this is your intuition and and and this is somewhat right what what you're missing there is that merging together coins actually exposes that link hundred percent so it's you don't expose more than you are addicts but you know what I mean so the information that sorry merging

**00:34:20**  coins links a hundred percent yeah yeah how's that you put two coins into the same transaction so that must come from the same person right okay block chain analysis heuristics 101 Kashyap holistic that's okay but

**00:34:52**  blocking analysis will we'll look at those those two coins and say okay one point is from but we can go one point is to a month ago now we need to find a user that used wasabi a month ago and a week ago and that could be any user like that there's a lot of users there and they they they don't have a good upper balance because the user only selected one coin from each it's instead of two coins from the same place why

**00:35:28**  would okay III them so so it might be in my example of a person who received one coin one Bitcoin a month ago one bit when we go he has 20 coins in total right 10 from a week ago 10 from a month ago and I'm saying if you want to send someone one Bitcoin it's better that you send five coins from a week ago and five

**00:36:01**  points from a month ago then ten coins from a week ago right because five coins from a week ago there's a lot of people that that mixed and had five coins from a week ago in five coins from a month ago there's a lot of people that had five points from a month ago so that's where my intuition comes from as opposed to ten coins which is which is now duction you know obvious that intuition

**00:36:34**  might be right but i would say it depends very much on the other users writer quoting here the paper chapter ten uses safety relies on them behaving like the others users but how can they predict how other users behave right and that's exactly the issue if there are if there are more people who have ten coins from this week compared to users that have five coins from this week five coins from last month then you might actually be better to send the ten points from this week rather than the

**00:37:05**  size and the size because there are more users who have ten coins from this week so so although your intuition might be correct it very much depends on other users and how do we know how would their coin situation is we don't feel ok that's a good that's a very good point yes I don't also I don't agree with that I'll be with that inside because you are dachshund or another tenant Bitcoin you

**00:37:37**  TXO for no reason I mean I do kinda understand what you mean by that confusing the assignment analysis and mixing up another UT echo from different time or different rounds but I don't know you would have to go on and mix that then Bitcoin UT EXO again anyway so I'm not sure if that's the most convenient thing for the user to do I'm

**00:38:08**  not sure but my intuition would be to disagree regarding this paper just he's really really instructive that we're talking about these UTX of coin selections those even if the intuition would be hundred percent correct there is still the the thing that we learned

**00:38:39**  last week that it's kind of computationally infeasible to to look at his links especially if you are talking with probabilities and and this brings back brings us back to the paper that is is this procrastination and the user experience shouldn't be more important than some some really weak intuition on privacy you know and this is right we

**00:39:15**  here to write of course that there might be you know something to be figured out on how precisely to to this coin selection and then how to do it right after all I think the the this is a comparatively a marginal gain of privacy right some better private a time correlation protection or whatever but comparing that to a user interface that is much more intuitive where more users will use it or the anonymity set as a whole grows that will give I would say much more privacy of

**00:39:49**  course it's a different strategy I agree with max actually I think there are way bigger problems and bigger gains we can make them quite selection I was just thinking out loud so I'm happy to concede that the Quinn selection doesn't matter that much or at least me if I want if you wouldn't think about this at another time okay new topic I am reading from the paper reboot ability is an anonymity issue for two reasons first it impacts the sustainability of the

**00:40:21**  network a network that's always about to be shut down has difficulty attracting and keeping users so it's anonymity set suffers second a disreputable network attracts the attention of powerful attackers who may not mind revealing the identities of all of the users to uncover a few bad ones now I was watching the tour developers talk

**00:40:53**  yesterday and he was talking about Silk Road that when Silk Road was shut down I'm not sure which agency um but some some American US agency went to him and told him that 90% of the tor traffic just disappear because ciick road was shut down and he was like oh really went home and and look at the stuff that what was going on and it turned out that

**00:41:26**  that was a lie so that's why transparency is kind of important in anonymity systems because other words or is just say any statistics that they come up with out of nowhere and just just makes make false accusations so repeatability what's your thoughts on that yes I think that that's quite a

**00:41:56**  good insight right because again the reputation will lead users to trust or not trust the software with their privacy and then of course the more the more users trust a specific software were tooled in general was to be used to protect their privacy the higher the anonymity sent us the higher the privacy right so if you have some shady provider you know claiming that he gives privacy but not nobody really believing him then of course nobody will use him and duster will actually not be any privacy compared to if you have a provider that

**00:42:28**  is very transparent and very open and very educated then this this will leave more users to to trust that this is the right tool to use and thus providing a higher anonymity said yeah sorry the big thing with the paper that I took away is how important it is to help the least knowledgeable users you know how

**00:42:59**  critical they are and because if you think of a lot of people that come into the Bitcoin space and that are you know not super tech oriented don't know don't know a lot a lot of those people are not you know the malicious or nefarious so if they decide not to use wasabi then wasabi is only used by two groups criminals and people who are smart and appreciate privacy and have the ability to do that but but we have to have you know everyday people who don't even know

**00:43:30**  very much apart from that is secure in private who are using it without without flaw we're very much a creed and that was funnily enough my main motivation of doing the educational videos at first because I realized that the tool is [ __ ] if only five people use it if I want privacy myself I better educate others how to use it alright so the very last topic I have for today and I'm going to just just

**00:44:01**  give this question out and let you guys think about it and I'm not sure I'm going to contribute much or the conversation from here on just wait for some awkward moment and and then discuss the next next meetings a schedule of what what we should do so after reading this paper should I put it you know this

**00:44:33**  paper is about usability more important than then technical hardness and it's quiet apparent that possibly was from the very beginning was going for anonymity like in the hardest sense that could be humanly achieved on Bitcoin and compare it to something like dark wallet

**00:45:05**  yeah probably dark wallet was the purest idea of usability there that it was doing to off to Cohen joins if you wanna send money somewhere then you register this sand and whenever there is another person who wants to send you're gonna send together that that was dark wallet and maybe we are in the wrong path with

**00:45:35**  Vasavi against trying to it ultimate privacy but maybe just two of two coin joints would do much more for Bitcoin privacy than this I think Adam here you're on somewhat of a track here but I think it can still be combined both if you have only the dark wallet concept very usable but only two of two coins then it although it might provide a large anonymity set of a total number of

**00:46:06**  users before any given user it does not provide much privacy at all those so of course what I would like to have is a bit of both I do have 50 anonymity set coin joints that are very easy one-click function that just work so of course that would be perfect to have a good mathematically sound privacy protocols that are very easy to use I study the motion with max the payment explicitly

**00:46:37**  says if you use an unsecure protocol it doesn't matter how easy to use it is it's not secure it's not private so to of to go enjoy this is not a two-person Quinten is not - it is not secure I would say five person point join it's not secure but then again I get attacked on Twitter as Maxted earlier today yeah so I want to bring up one point that that shows how the wasabi philosophy is slightly divergent from

**00:47:11**  the philosophy of this paper and that has to do with the fee that we charge for our users so wasabi charges users based on the anonymity set this is a an incredibly fair thing to do because it's proportional to how much try to see you are getting right you can paying the portion along price you're getting and that seems incredibly fair so if you're getting not a lot of privacy you're not you're not paying as much but the result is twofold as a problem the first

**00:47:45**  problem is that users never know how much it costs and the second quite ironically quite funny is that as soon as one person behaves poorly and gets D anonymized people will go on Twitter and say oh you charged for 80 anonymity set but you're getting only 50 so you're being ripped off which is something that we're not in control of so I just want people what their thoughts because I think that pain

**00:48:18**  / anonymity set is the correct your way to do it from a practical standpoint users simply don't know what's going on most users don't know what they're gonna expect to pay and and are confused that doesn't need a very good point of these that you bring up and maybe to put this a bit more into the light of in context of the paper the paper describes these costs for privacy mainly in terms of latency I said that if you want to use a

**00:48:50**  more private system you have to pay with your time right and this might also then come to it you know you can configure it how long do you want to wait until tor go to your website or whatever and having a user option to do so I told many hops do you want to have in the onion world and of course that on the other hand here is then what you bring up I said that the more transparency you have in that sense and the more easy it is to understand the better so I didn't

**00:49:27**  want to talk to you too much about wasabi because I think that's a whole other conversation but I would like to push this as an idea would anybody be interested in having this discussion next week sort of like a philosophical continuation or should this be much much later once we've read many more papers I would prefer it after what is it April 6th it's a very specific day oh why

**00:50:05**  and you probably mean April 5th the conjoin day which is the Nexus IV release yes April 5th because that's the coin join indeed as the Nexus ah be release and whatever happens then after that I'm going to hundred percent concentrate on research [Music] yeah that's that's why I read you that you will concentrate on research no yeah

**00:50:38**  you know I'm coding a lot and trying to wrap up everything but of the things with Bitcoin core actually that means - mmm there is some constant needed for for something in Bitcoin core in order to properly implement it - wasabi but constants is not reached so like maybe maybe it kind core integration will be

**00:51:10**  delayed to further future than I hoped previously sunny vague anymore more on this or should we discussed the next sessions topics that what should it be I thought had quite a lot but Rafael go ahead yeah I just had one thought about topic about of picking up or different

**00:51:41**  coins for your transaction I mean if we are actually just trying to confuse these China analytics companies with deep doing like mixing up with the heuristics and all of that stuff I mean why don't we just try to like for example the things like pay join where you are making the transaction look like

**00:52:12**  different that it actually is it doesn't look like a normal payment so why don't we just try to add these kind of options into the wallet or why do not force the users to do a certain thing but just give them a lot of tips and hints why this and that way of doing stuff would be good for their anonymity would just educate people already so on

**00:52:45**  that topic this is what I was I was gonna leave out but I'll just hint at it briefly by having users be able to consolidate and spend and coin joint in the same transaction it makes things way easier for us from the perspective of of hiding from forensics because now the wasabi is is just all users are are doing actions only inside these massive coin joint transactions as opposed to doing actions

**00:53:16**  on their own terms sending sending funds outside of those transactions so that would be like revolutionary like gigantically forward in terms of privacy absolutely I agree you know it for the next content implementation I would just love to have users being able to register multiple inputs to generate multiple outputs and to be able to send precise amount to a external wallet address that would then would be I think the win for Bitcoin

**00:53:47**  privacy so we just need to figure it out yeah sorry I was just gonna say that definitely that what max said but you could just add multiple inputs and get some multiple outputs wherever you want but that would be pretty great I mean that would mix up a lot of different heuristics wouldn't it I mean even as simple as being able to to take your mixed coins and pay someone in a wasabi

**00:54:19**  coin joint it would change everything because it means that anyone who receives funds anyone who spends and what's not be conjoined how put doesn't necessarily mean that they've ever used wasabi and that's what that's what would really change the game in terms of privacy so I could literally : join into my exchange address and that exchange now looks like it's doing coin joints even though it's not so it's it is so then it becomes hard to blame someone for having the wasabi coin joint hug

**00:54:51**  yeah I do like that idea but I just think that that might give a little bit of problems for the whoever receives the coins you know if they are not aware of these being conjoined coins and if there is someone like flagging them I'm not sure but I mean I like the idea but just we should all also think about the probable problems that comes with that I

**00:55:22**  mean for example if you are sending to an exchange through that coin joint they could just freeze your funds or if you are sending to someone else and they don't they are not actually knowing it's gonna be from a coin joint they might get the funds freeze I don't know indeed whether there are there many things to take care of you one thing

**00:55:52**  that I would like to talk about as Chapter six but basically just the title of it which is at or installation and I think that is one of the aspects for wasabi is absolutely superb where it combines both being technically sound right having multiple tours identities different tour circuits that change like every couple seconds with new circuits while still being incredibly user-friendly in the sense that there is nothing in the GUI that the user has to setup but it just

**00:56:24**  works plug and play by default for every users the same there is nothing to configure there's nothing to [ __ ] up you just start wasabi and it works and it works on a technologically very sound level and so I think this is the prime example of where we want to be with everything in the wallet I'd have everything as technologically sound and as user-friendly meaning no configuration at all as the tour set up in wasabi

**00:56:57**  okay but not much to that and then the second thing I would like to talk about though is Chapter seven about the Java and on proxy and what I found very interesting that it is a graphical user interface that has three different and eliminated levels low which is ready fare which is green and high which is blue so these I found very similar to the wasabi bullet anonymity said shields

**00:57:28**  by the Red Cross shield the yellow exclamation shield the green shield and the green checkmark shield by to indicate how much anonymity set you have of course the the more greener the better basically and the second part of the comparison just just just as a there is also another one it's over 9000 she's that's the best don't tell them about it but another comparison to this

**00:58:07**  mjp that I found so interesting is that their level of anonymity depends on the number of users so the more users use the same entry and exit notes or whatever they're called the higher the anonymity so they think right and that is the same as we have in wasabi that the more users register their coins and the more quantity of equal value on puts being created to higher the anonymity which in first glance makes a lot of sense right the crowd is larger but then

**00:58:38**  what they talk about here in this chapter of chat is that it is still if you do for example in this case time correlation you can still discover the user ID and in the sense of wasabi will be a bit different but if other users [ __ ] up or if for example you send to your old to the same address twice right address reuse or you leave your ex pop or whatever happens there are still many ways that despite having a large crowd you that can still lead to the anonymization and I'm not sure if

**00:59:10**  there is any way to to remedy that that regardless the size of the crowd and regardless how beautifully you display that in the GUI there are still ways to [ __ ] it up and the user often times not even does not even know that he's [ __ ] up his privacy I mean we are low boiling it a lot I mean these odd thing together anonymity sets because that's what we are doing it's it's just so incorrect it's mathematically speaking

**00:59:43**  we should be multiplying the anonymity sets but we want to low boil it as much as possible so we are not multiplying them but adding them together I know so it's like yeah you can [ __ ] up things but on the other hand we are trying to balance it out in some some way even if that's kind of incorrect and missing

**01:00:15**  because you gain more privacy than actually it shows but you know what I mean is that correct or what what does the paper says about this approach well basically that it's very difficult right that in the case of Trump the size of the crowds does not matter if you can do time correlation attacks right something similar would be in Vasavi the size of the anonymity set does not matter if you

**01:00:47**  do address reuse afterwards right if you shoot yourself in the foot then there's then you're screwed and you know to a lesser extent also if others shoot themselves in the foot then your unanimity size decreases more and more to a point where you might not need to know that you no longer have any anonymity set because all other users are D anonymized already it makes a

**01:01:17**  couple of times then even if you don't mix a couple of times only once that the chances that most of the other users are going to die anonymize yourself the anonymized themselves I don't know but that's why I recommend people to mix twice just in case I mean I knock this tree low but anyway yeah and that's the that's the other

**01:01:51**  idea between weeks twice and from an an apart in in time so mix once now and mix once a year from now and then you can you can be sure that the unanimity set is like really like multiplying or something like that yeah that's a big argument that nowhere and I have had because I'm of the firm belief that when you have a coin from a

**01:02:23**  coin joint and then you remix it in the immediate next coin joint it's barely even feasible to call that addition of anonymity set but but ok you can say that it's the addition of the anonymity set you will have participants that are repeated quite a few that are repeated from one to the next but as soon as you remix from a coin joint a month ago to a coin join today and everyone starts

**01:02:54**  doing that then you can actually make a pretty solid argument for multiplication or something that's even greater than addition it might not be multiplication but it but it could exactly more than addition but you can make the argument what the paper says that that's just not useable if you have to wait months before you can use your coins you know it no all I would require is when a user

**01:03:25**  receives money they make sending before they want to spend their money they they mix or they mix spend something of that nature okay that's a good idea actually yeah you know basically it's the idea that and again to automate but as soon as you receive it immediately afterwards it registers for a coin join and then the only way to spend is in a coin run even if it's a naive unequal amount coins on it doesn't matter even if it's only a five part five person conjoint

**01:03:56**  doesn't really matter right anything is better than having a two input two output transaction for example just like the regular spending transaction all right are we ready to decide the next week's topic one more thing that I would like to bring up now in the context that we talked about the the anonymity so targets and bringing it back to the

**01:04:26**  conversation about against options chapter four currently we have three different options that the user can choose yellow shield green shield and exclamation point field is that is that too many choices or or should the user even have a choice for how much anonymity said he should get because again some users might just choose one round some users might increase that to whatever they want what is it better to have the same level of anonymity set target for every user

**01:04:58**  and not even be able to configure it I mean once the feature is out that you cannot take it out that's that's something I know you have a very good alternative of course well I mean bad padlet argue from

**01:05:29**  the case that we are redesigning wasabi with a new conjoint and a new UX I would feel odd or okay so it's a tricky question I don't really know the answer to that what would you guys do I would get rid of the term anonymity said entirely get rid of the option and then

**01:06:01**  just have a system that's this the lowest common denominator understand something like you you have to mix once and you have to mix once before you send I don't know I mean in my opinion we are thinking of talking about a little bit way too small specifics and I don't think they are even that big of a deal I mean for example just indicating that

**01:06:32**  you can mix for example just seven different or put seven different outputs in a coin joint that's much more relevant or problem than what's the color of the shields or the unanimity set number I mean I think those are awesome information I think those are pretty relevant I don't think those are anyway like disturbing or confusing for new users I think they are pretty great

**01:07:04**  but there's a lot of these different things that are a bit confusing I know that they're meant there are many quirks on the design that that really should be redone or just to make it more beautiful in general yeah I don't know I just like the current version way too much and I'm like that don't don't you guys mess it up so much yeah me too me too but one other thing to consider again is the point that especially now where the

**01:07:35**  user pays for or please / and in the mid he said it's it's a question of of how much is the user willing to pay and of course with with network level and anonymity he just pays with his time of his computational power but for Bitcoin anonymity he pays for it with his money it's so that is something to consider as well there might be users we have you know a high threshold for spending as much as possible on privacy because they're really desperately needed in quotations again that might lead to actually them

**01:08:07**  being D anonymized but if it's clear that this one user paid a lot and he might be tracked and that might be a fingerprint and only other hand other users just want to have very light preliminary privacy and they don't want to pay as much and and again to get these two things together is again options and configurations and and trying to reduce the footprint it's it's very difficult because of the virus we might have to cut our beards down to

**01:08:40**  make it not airtight anyway so guys what do you think about what do you think about me if I'm not if I have time then I would cut out the wasabi conversations from this and and and let I don't know just just cut out you know presentations now yeah but max aren't you worried that our dozens of viewers are gonna be

**01:09:12**  overwhelmed there's like you mean literally wonderful do you know when I walk the streets now max I keep getting accosted by people who recognized me from YouTube it's like I can't deal with this Fame alright guys I do have to go pretty soon so uh no para do you want to decide to the paper or suggest people

**01:09:44**  have may I just ask one add one more thing about this wallet discussion maybe just adding something like the total percentage of or at least the estimation about with the current amount of participant in the next coin join times the actual fee that goes to the coordinator and possibly like the actual network fee also but just give us

**01:10:15**  some kind of estimate for the user I think that would be pretty awesome so because in my opinion there's a lot of these questions about how much is actually going to pay young people like calculating it and all that kind of stuff yeah I agree I'm not quite sure where to put it obviously I cannot crowd more things into the coin joint top because it's already scary but this should be there

**01:10:51**  [Music] I'll take a look around it and just give some kind of idea anyway avi do you have any suggestion for for the paper next week nope okay so here are the things heuristics on Bitcoin privacy Vicky Cohen joins Sudoku boards Minh papers from blockchain owner is this company's topological analysis of the Lightning Network I am NOT an anthro piece blocks

**01:11:24**  I design and application of blockchain analysis platform traceability analysis on one arrow towards information theoretic metric for anonymity a brief history of linear and mixed integer programming computation okay so I'm not going to to to talk about the - to say these these papers again to say what what you think would be interesting and we will vote on them

**01:11:56**  I think last time also we we said there would be good - now after this more philosophical paper go into the calculation of the value of anonymity so that will be conjoined pseudocode that will be Boltzmann later why I am NOT an entropy and I think that would be an interesting path to go down how do we score the quality of 0.1 they've on paper I think it would be good to start with Sadako okay coin joins Dooku who is voting for that yeah

**01:12:26**  I second the motion yeah I like that too okay I'm going for that too Oh everyone is voting for that then I guess we just got a winner Cohen joins the Doku next week all right so are you sure I shouldn't cut out the wasabi stuff because it's it it should be about the paper I mean it's not a big deal it's like in 20 people that are

**01:12:56**  gonna watch it so not a big deal no and I think it was actually quite valuable to have this because I mean this was a rather philosophical one so yeah I think it's good to apply this more right all right then thank you guys and next week going against Sudoku like share and subscribe and research so thank you bye bye

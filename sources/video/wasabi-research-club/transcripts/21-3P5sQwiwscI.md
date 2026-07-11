# Wasabi Research Club #21 - CJDNS with Caleb DeLisle

- Playlist index: 21
- YouTube ID: `3P5sQwiwscI`
- Video: <https://www.youtube.com/watch?v=3P5sQwiwscI>
- Duration: 0:57:04
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:00**  welcome to a new wasabi research experience meeting uh this time um we have a special guest his name is kailaf he's the creator of cj dns project basically is a network that can replace the internet basically of course is that that is very ambitious other okay

**00:00:30**  he will tell us better and part of this project is now already supported by the vip 150 55 in in in bitcoin uh and bitcoin are other libraries too so this is an effort that part of the bitcoin community is doing in order to have a more diverse

**00:01:03**  and robust network collectivity let's say or more resilient appear to be a network and where cgi dns is part of that too so klev welcome and we are happy to have you here thank you very much happy to be here um yeah so cjdns what is what is cjdns really it is a decentralized mesh networking

**00:01:34**  protocol which is designed to function under in the context of some of the notes uh misbehaving that is some of the nodes being adversarial and that's actually very rare in in routing protocols networking protocols because typically if one of the nodes just starts announcing garbage to the other nodes then they will just routing turn the whole network into a big routing black hole um notable exceptions are bgp

**00:02:05**  and that's obviously how the internet is routed but uh bgp is very hard to set up and so one of the other aspects of cj danis is it's source routed and that means that when you send a packet uh into the network yeah sorry for interrupt you i would like to to to go back and and and ask this question for you what what is wrong with the what we have now what do we need yeah yeah yeah uh it's all it's all centralized and it's centralized in the hands of companies that don't

**00:02:36**  necessarily like us i mean all you need to do is go read the newspaper read the the new york times or read the um any one of these newspapers or tv stations and frankly these are tv stations that haven't turned an honest profit in 20 years and they are being controlled by the centralized centralized power structures and these they are are telling the story now that we are the enemy we are the enemy of the people we are because we're doing bitcoin mining or any kind

**00:03:08**  of um uh encrypted crypto mining that we are we need to be shut down we need to be stopped and the this this saber rattling that we're seeing about how it's the biggest uh environmental disaster in history and to be clear here this is not the biggest environmental disaster in history for a couple reasons one is because it's actually not that big to give you a reference russia flares

**00:03:39**  off three times as many as much energy in gas just from oil wells that have gas coming out they just flare it off into this into the air as the amount of energy being used by bitcoin so it's actually not that big it's much smaller than other things that have much better lobbies but the other thing about crypto mining is that while it does use a lot of energy it's also very effective at facilitating the transition to renewables because

**00:04:09**  it uses the cheapest energy available and actually the cheapest available energy is what comes from renewables because there's nothing cheaper than a solar panel once you put it up it doesn't cost you anything to just let that solar panel sit there and run so i'm very strongly of the belief that the the the decentralized uh finance and the crypto and the mining is actually not uh cause of uh this massive environmental degradation the reason why we're seeing this coming

**00:04:40**  up in the media is because these companies these people are lodging an attack against the decentralization community and this is nothing new we go back to the 90s you have the same people you know you have bill gates saying that linux is cancer and now you know bill gates is buying up github and there's all of these people who are moving uh they're making moves and there is really a war on crypto going on so it's very important right now that we're able to get our decentralized systems onto their

**00:05:13**  own network because if we're going to rely on a network that's run by the people who are attacking us eventually they're going to shut us down so that's that's really why cj dns and the pkt project is so important for me because the point here is that we're going to be building a a mesh based network infrastructure where everybody can own a piece of the internet i don't i don't want to just model them

**00:05:45**  here you have a question no no no no um yes now if you come if you can tell us what's the the division right and how the the the the technology is built in order to bypass all these restrictions and i would like personally know more about the well i understand the technology but

**00:06:15**  probably not everybody understands how it works but about that and how you work with your ips as public keys and all the routings instead of right what's the address how to route to that address and how how everything plays together absolutely so um cj dns is as i said it is um uh adversary tolerance so you know you can have a bad router in

**00:06:46**  that network and the network's not going to explode and there's a couple ways that we do that one of them is we have um we derive the ip address from the public key and so we're using ip6 addresses and the address is basically the fingerprint of the public key so when we do that we get the um the ability of you know if so if somebody says this is my ip address you know that it's their ip address because you can just communicate with them and you you are able to compare it to their

**00:07:18**  public encryption key but that also poses another challenge which is that it it um it prevents hierarchical routing which is typical of systems uh routing systems so it's in place of hierarchical routing we use a system of source routing and source routing means that when you send the packet into the network it already has the entire path that needs to take all the way source to destination and the way that you get that route is going to be similar to

**00:07:49**  the way that you do what is similar to the way you do a dns lookup you're sending a request to a route server and that route server is giving you the path that you should use to get from point a to point b and where we're going with this is that there's going to be multiple cloud isps what we're calling them and these cloud isps operate route servers and you just choose which one you want to do business with and that one will handle the business of getting your traffic onto the network and then to

**00:08:21**  where you want it to be um why are we doing uh why do we have this semi-centralized model of uh cloud isps as opposed to just doing a fully decentralized let's route on a dht let's do everything like that the reason why we're doing it the way we do it is because when you have when when your primary access to the internet is based on a network you need to be able to call somebody when something doesn't work if you're paying real money to be able to get on

**00:08:53**  the the network then you need to be able to make a phone call or whatever and you need somebody to be able to handle that situation and we need that that entity to be there to be that network operator to be able to fix that but we need that not to be a monopoly that controls everybody's access to everything so we have these cloud isps which are a little bit like just a vpn company and what they do is they manage all of the buying and

**00:09:24**  selling of bandwidth leases from the people who are operating the actual infrastructure and then they find routes through the the mesh in order to get you access to what you need does that make sense yes but i think that is something new isn't it i mean it was not okay and how how was that handled before and how it's not handled now yes okay yeah so original cj dns did use

**00:09:56**  a dht and um basically we we beat the we beat the software up as much as we could and we realized that there are fundamental limitations to a dht based routing model that are unsolvable without switching to something that is different so basically we can solve a lot of problems but the problem we can't solve is my internet doesn't work who do i call how do i fix this and because we can't

**00:10:29**  really solve that who do you call problem that's why a fully decentralized routing infrastructure just doesn't isn't going to work in the long term so in place of that we create an ecosystem of different entities who can do routing for you and then you just get to choose which one you want to work with okay i see um so going going down a level

**00:11:00**  in complexity i mean from a normal user right because now we are thinking all the time normal users and translate this concept too you know to to my mom um what does it mean for my mom what what problem does this technology solve right right so for an ordinary person that's going to be you're going to install the app onto your phone on your computer

**00:11:31**  whatever and then you're just going to be able to access the internet fire your neighbor's wi-fi that's what we're talking about here you're just getting on onto your regular internet via your neighbor's wi-fi and you buy a vpn and the vpn company is paying your neighbor to provide you with that access to the internet that's what a cloud isp is it's a vpn which goes and pays the person who's providing you with the access to get to that vpn does that make sense

**00:12:03**  it makes sense and how successful is is this right now i mean is it happening so we're in really um early stages at this moment we have the the packet coin which we're working on building all of this infrastructure on top of what we need is we need a very very low cost way to transact in tokens because when we're doing when um we're issuing bandwidth

**00:12:34**  the bandwidth is going to need to be tokenized so that people can buy and sell and trade the right to use bandwidth on a particular link and so we need to make a token and it's not going to work to just use ethereum because the gas fees are just unacceptable so we're working on a project which we call token strike and token strike is basically you just make your own little blockchain and you sign all the blocks you're the issuer of the token you sign all the blocks and all that we

**00:13:04**  need to do is have a means by which if the issuer does something nefarious for example claw back a token after they sold it to somebody then we need to be able to um i identify that nefarious activity and have nodes in the network which can um which can report to everybody that that issuer did something bad and then all of the software will be configured to not deal with that issuer until they fix

**00:13:34**  their stuff so that's what we're working on in order to be able to tokenize and issue bandwidth so basically we're talking about free tokens you can just issue you can make a token you just downloaded the git repository and you compile it and you have a token um and we're gonna need that in order for these devices to sell uh their bandwidth as a token and then we're gonna need uh to use lightning network which we're working on now in order to transact those tokens using

**00:14:04**  htlc contracts now um cjdns and vpn and vpn app are all in alpha testing or beta testing you can you can try out the app on android now um and the and what we're what we're using now is we have uh um the pkt project is based on uh a proof proof-of-work algorithm which is bandwidth hard and the bandwidth hardness is creating an artificial demand for bandwidth

**00:14:36**  um and so unlike a lot of these tokens i mean i don't need to explain to you guys necessarily what uh is the difference between a token faucet and a proof of work but i'm finding a lot of people that don't understand that a proof of work is proof of fair issuance whereas uh all of these other kind of tokens these different issuance processes you can't prove that it was done fairly so um yeah we we have the only

**00:15:08**  and this is something else that i created it's called packet crypt and it is the only bandwidth hard proof of work so it's really just a problem that is easier to solve if you solve it together with other miners and the the packet blockchain is based on the packet crypt uh bandwidth hard proof of work so this is going to incentivize people to build out large amounts of bandwidth which we foresee helping uh kickstart the the decentralized

**00:15:40**  bandwidth marketplace which will finally be used for getting people off of the legacy and centralized internet okay and i don't know if i am the only one who would need who had to make questions but anyway let me go with that so what you're saying is that basically my neighbor or i can become an

**00:16:10**  internet service provider exactly exactly but you're not going to need to do billing you're not going to need to do uh customer service you're not even going to need to do routing you're just going to set up that device and it's going to start earning you packet which i mean you can convert that to whatever currency you would prefer to have okay so i am now an internet service provider that provides the the the connection to all my neighbors and they pay um

**00:16:43**  for bandwidth they buy bandwidth to uh to a company they they're going to pay a company in a simple obvious way you know regular old uh maybe it's 29 a month whatever whatever that deal is they're going to pay that to that company in in that normal obvious way and then that company is going to have bandwidth traders who are going to buy those leases of bandwidth from you so that an individual you know grandma

**00:17:14**  doesn't need to understand about trading bandwidth and buying the dip and these kinds of really complex things that's the job of financial traders okay and what is the what is the um proof of work that is hard in bandwidth why do we need that or who need that um the point of of packet crypt is to create an artificial demand for bandwidth because

**00:17:45**  demand drives supply so when we create a demand for bandwidth that's going to cause people to do to roll out more fiber so think about all of the bitcoin mining equipment that's just sitting there collecting dust because it's no longer profitable right you've got all this stuff from five years ago ten years ago and it just doesn't make any money anymore with packet crypt if you install a fiber optic cable into your area in order to mine packet crypt that fiber brings value forever basically so

**00:18:16**  the work we're leveraging the externality of pakicrypt mining in order to get more internet to more people okay perfect so basically you know we are bitcoiners right and we are the those bitcoiners that many of us probably don't don't like other cryptocurrencies so that's why i'm asking this this thing so do you are saying basically that well

**00:18:47**  the the first design was not it has some problems and now with this new um cloud either sorry i don't remember the name but yes this this new um isp yeah now of course you need a new token i mean you need a way to tokenize the bandwidth in order

**00:19:17**  to to create a market to fund with uh why is that not possible with i mean you need a market right right is that market before before before making my question is that market already um running is is is it working um it's not really off the ground right yet but uh that's because we need the token strike project in order to be able to tokenize the bandwidth

**00:19:51**  but okay and let me let me address because you asked another you you said another thing about you know bitcoin maximalism and i get it like i i've been there i mean i've been in the bitcoin community since 2011. um i know there's a lot of projects that are pretty shady and that's that's a reality here so why should we wh why should we accept another coin as being legitimate so i'm going to give you a general answer

**00:20:22**  which is that we there is a war on crypto right now and they are coming after the uh the work coins first and then that once they knocked down once they're able to get control and stop they're gonna come after the privacy coins so they're gonna they're gonna be hitting monero they're gonna be coming after the work coins you know they're gonna be coming after the wasabi wallet the all of the ways that people can uh achieve um liberation from these centralized powers

**00:20:52**  they're going to be coming after us and if we don't work together then they are going to pick us off one at a time and you can see in their newspapers they're already they're already rattling the sword so we need to stick together here because there is a war against us and it's a war against decentralization and a war against open source and a war against individual liberty so that's the general answer of why we can't just bury our head in the sand and say my coin is the best everything else is a scam

**00:21:22**  and um that uh that's just not going to work because we will be pried apart and we will be killed one at a time and my the the specific answer why is the packet a thing why don't we just use bitcoin etc well packet is a thing for two reasons and the two reasons are related to the two differences that it has from bitcoin the two fundamental changes that were made one of them is that we have uh the bandwidth hard proof of work which makes it so that it the the mining

**00:21:54**  of packet incentivizes the rollout of network infrastructure the second one is that packet has a network steward which is a basically a founder's fee but the founder the so-called founder can be changed via a proof-of-stake based vote and that founders fee is used in order to fund all these projects in the ecosystem to develop all the technology you know bitcoin is it's a great project but it does not fund the wallets i mean

**00:22:24**  i'm sure you guys understand developing wasabi is not easy because there is no funding for that the funding is for people who can build better shot 256 chips yeah okay rafa yeah i was just wondering like uh did i understood correctly that you are using the like the same algorithm that bitcoin uses so you can make use of these old like asic devices no uh the algorithm is

**00:22:56**  very different but the point is that when you build out infrastructure to mine packet crypt that infrastructure includes fiber optic because you need that bandwidth in order to mine so that fiber optic that you've just run in order to mine packet crypt when that mining installation becomes no longer um profitable that fiber is still there and that's still bandwidth that can reach out to people and get them on the internet okay got it and you mentioned

**00:23:28**  that you're using the lightning network can you elaborate a little bit more like what part are you doing with that we're just gonna do our own lightning network you know i mean it's uh it's a a bitcoin fork with very few actual changes so we're the the point of this and the fact is i did not start this project in 2014-1516 because i was waiting for the transaction scalability that the lightning network would have would afford and so then in 2019 2018-19

**00:24:00**  the lightning network started to reach maturity and so that was why i woke up the cjts project cj dennis was asleep for uh a good four or five years just because the other half of the the necessary technology just wasn't there yet okay well something that i have never never shared before with anyone is that i am hundred percent sure that

**00:24:33**  they are going to come for what's rewarded at least i'm i'm very sure so yes i i agree with with you and i think if if your project finally uh is as useful as i think it is of course i will need to buy those tokens with bitcoins because it's it's basically the

**00:25:03**  currency right um well one more question and this is my probably my last question well everybody most of us probably understand that well given the the the ip address is the the fingerprint of the public key we can always compute an encryption key to communicate with with the the other end right uh but after that i mean i understand it's an end-to-end

**00:25:35**  encrypted network what other considerations about privacy and security but specifically about privacy and can we can we learn from your project and how do you think it can help bitcoin to to make the bitcoin the peer-to-peer bitcoin network uh uh more resilient well i mean i i think that uh it's not so much about privacy per se it's about

**00:26:06**  robustness uh right now um right now we're just praying that they don't turn us off i mean as you said uh that they're coming for they're gonna come for a wasabi wallet and i believe that they're not you know i have a strong belief that we're gonna win we at first they ignored us and then from say 2014 to 2017 they laughed at us you know you remember bitcoin is dead bitcoin is dead bitcoin is dead all the newspapers they just kept saying it and now we're into the stage that they're fighting us

**00:26:37**  and we just need to take that fight and be serious about it because they are fighting us and they're telling us they're not fighting us but we're not going to believe them about that we can't just have them say oh yeah there's no war on crypto just uh don't believe that you know it is a propaganda war they're going to try to to to fight us on on the propaganda front and i want to i want to just hammer home how ridiculous this is yesterday on twitter um everybody who used the word

**00:27:07**  memphis in the tweet was uh banned just and they said oh it was a bug oops we made a mistake well guess what was happening in memphis yesterday yesterday in memphis tennessee there was a um there was a protest against an oil pipeline and oil pipelines i cannot uh i cannot hammer home enough how uh irresponsible it is building an oil pipeline right now because we're just at the precipice when renewable energy is going to become so cheap

**00:27:38**  that um oil is just going to be uncompetitive because you don't need anybody greasing oil jacks to uh to run a um a solar array you don't need people shoveling coals around the solar array the solar is going to beat the crap out of all of this stuff once it reaches the appropriate scale and they're still building these oil pipelines which are just going to pollute everywhere and you know these companies are going to walk away from these oil pipelines and just say oh yeah it's not our problem anymore

**00:28:08**  you know you clean it up and uh they're still building these things even now in 2021 so you know and you have these centralized platforms that are creating these bugs in order to cause people to not be able to talk about and coordinate a protest against an oil pipeline uh yeah no better yeah i i wanted to say something but you guys were touching the topic and

**00:28:38**  then moving uh away from that and then come back all the time i wasn't sure but uh yeah it should be the right time that i think you know if if there is one thing that i i learned from from wasabi and i think this would be this because and and this is a very general point on on on privacy projects because at the beginning you know when i was telling people that this is what i'm

**00:29:08**  going to do i'm going to build bitcoin privacy and everyone is saying that that no you can do that because governments hate privacy and and only criminals work on privacy and things like that and and you know it's it's not true at all people in government get how important privacy is it's just not their first built and no one is there to remind them that there are

**00:29:39**  consequences but you know when when you reason with people they they get it i mean sometimes you just ask them how much money they have and you know you instantly make the point because that question makes them uncomfortable and oh you you you get privacy so but but the point is that these privacy projects are are always started from these anarchist libertarian route and and and i think there is a

**00:30:11**  very counter productive thing here is that you know this hacker mindset is that you have to be super paranoid about everything that's one uh and and on that to that is that the libertarian and anarchist thoughts that well if you are working on privacy then you're going to be thrown down and you know that's not not happening uh people get what you're doing what's

**00:30:42**  what's happening is when when when someone creates something and advertises specifically for goods those are you know on on the line of well what should we do with them and and and those are things those get shut down but you know like it's it's not that often that privacy companies get shut

**00:31:12**  down and and in fact the the problem is that no one dares to even start to work on privacy because everyone is saying that it's so dangerous it's not dangerous everyone gets privacy privacy is a human right and and working on it is is not dangerously natural um sorry for my round but but i i think i think we should be more positive and yeah but adam

**00:31:46**  we were i don't know a year ago probably we were mentioning an internal uh intelligent agency that is fighting against who knows what right and we are in those reports and in those investigations again and again so okay i mean sorry i think i don't agree with you i don't

**00:32:18**  i mean i i wanna i wanna jump in here because i mean i think this is a really important topic um we are clearly in a war but the war is not with policymakers policymakers we need to work with them and we need to explain to them the importance of decentralizing power because this power is being centralized in the hands of a couple of these people and companies these aristocrats and they are they're holding this power over society and they're also holding power

**00:32:49**  over policy makers you've got the european union they pass the gdpr clearly they care about privacy the and i mean privacy is considered a fundamental human right um and it is not difficult to have this conversation with policymakers it's just that a lot of people are either not doing it because they think the policy makers are the enemy which is wrong or they're just thinking that well take the case of uh okay cia does uh

**00:33:20**  does a um a report on wasabi well i mean ca had a report on or they had some scraping from uh um cj dns in their in their internal wiki that doesn't mean that they are against us that means that they want to know that we're here and we need to have a public facing answer to these people we need to have literature to be able to explain to policymakers government whatever what we're about who we're we're fighting for we're fighting for the

**00:33:51**  individual liberty of people and for democracy and what what what is the other side doing because the other side doesn't have any problem putting their lobbyists into government and then they're using their lobbyists to try to make government fight against us so we need to cut it off where it's actually happening here well yes yes i agree with that but listen i don't remember if this was nec uh

**00:34:22**  previous week or a week before that but the i the european parliament uh voted for for for making uh for i mean the the messaging server providers and the image provider have to to be able to the crypt basically yeah it's absolutely tragic what happened

**00:34:53**  uh last week and um you know this is this is a loss this is what happens when we're not in we're not lobbying you know we're not talking to policymakers the other guys go and start talking to policymakers and they are going to use the their relationships with the policymakers to promote um to promote policy which uh helps them to continue and establish their monopolies over control of the the individual people so you know we win

**00:35:26**  some we lose some the policymakers are not our enemy um they are being pulled by our real enemy okay anyway they are the one that vote for these things for just for for those that don't understand what what this means is for example uh it is not possible to have end-to-end encryption anymore because if i provide this the chat service and i i need to be able to decrypt your

**00:35:56**  messages that means that end-to-end encryption is not possible anymore i mean you the the communication can be encrypted um but no end-to-end let's say i don't please go ahead yeah hi so i was just wondering because this

**00:36:29**  sounds a little bit like the tour project but the and you have a similar concept on providing bandwidth and even though door itself doesn't really do any accounting on the bandwidth but you actually have a privacy layer on top of it so i was wondering if there is a similar risk model related to your project as being a host host of the service as running a tour exit node what do you think uh it's a bit similar it's it's a bit similar

**00:37:00**  as far as your risk profile when you're running a vpn um but unlike tor we're not trying to have anonymity of the um of the person versus the the exit so we're not trying to be a strong anonymity our point is to have a strong network that is um robust and resilient to people shutting it down centralized power um tor is going in a slightly different direction where they're they're really trying to make it so that

**00:37:30**  nobody knows who anybody is and that's a very hard problem to solve and it's a very specific problem so tor and cj dns and packet will always tend to coexist because they exist on different planes and for different purposes if it's okay another question yes please yeah uh i was just wondering it's a little bit difficult to get a

**00:38:01**  layer layer 2 vpn set setup at least i don't know any service providers who would actually do that do you support layer two um no we are layer two we are a layer two um because we're not we're not actually doing ethernet um ethernet in my opinion it's not really that useful it's it's because ip doesn't scale down and ethernet doesn't scale up we ended up with these two layers

**00:38:34**  cj dns scales both directions so um on top of cj dns we just put an ip packet because it's compatible with with ordinary software i mean you could do ethernet over cjdns just like why that's kind of the point regions yeah i mean you could do it it's just like it's just like doing ethernet over like uh packet over sonnet or sdh it's it's

**00:39:04**  really the similar concept you just have to write a little bit of code to connect it together cj dance is a transport it'll transport anything you want okay good to know thanks yes short for coin join dns no um it's it's uh because my initials are cjd and um there's a long story about that yeah originally it was supposed to be a dns system but um we pivoted it into uh

**00:39:37**  being a routing system because uh routing is actually easier to solve than dns dns is a deep political problem that is not my favorite problem to try to solve okay do you know about um the lucky project the project that it comes from the monero community it is not it is not similar but it's a

**00:40:07**  networking solution similar to tor and they have a coin to i mean a token i don't know if it is for bandwidth i mean it has to be for bandwidth because what what else right do you know something about that in order to make a comparison or to do you have seen to yeah i i know i i spoke with the developers of loki um yeah it's a it's a monero fork as i recall um i mean here's the thing they're

**00:40:38**  working on anonymity and they they want to do an anonymity network um the fundamental thing is that we want to do is we want to do infrastructure we want to get people access to other people without having to go through networks that can be turned off that's that's like the key fundamental aspect of packet whereas um anonymity is just like we can solve anonymity later once we control infrastructure and people that uh the uh

**00:41:11**  the bill gates is of the world are not going to turn this off on us yeah it's a good answer okay thank you i want to ask the same question so that the main difference is between cj dns and nimtek i don't know if you know it but it's similar is that nim mix now yeah yes um i've just just vaguely heard about it but i mean if

**00:41:42**  the point is anonymity then it's it's really the same answer it's it's really like we are going to be light on anonymity because anonymity costs you it's it's effort you have to do software development you have to waste resources because you're doing onion routing that's more resources more latency that is a worse quality of service for people our primary objective is to find a way to get people their their primary internet access that they don't have to that works 100

**00:42:15**  that they can go stream the videos they want to stream whatever they want to do and then we can layer the anonymity on top of that and that's a primary internet access that's not going to get shut down because it's decentralized by the way we have all um a meeting um specially for mixnets so it is already available in youtube if someone wants to

**00:42:45**  to know more about uh mixed just a question imagine i want to be an internet service provider right how can i buy i mean because someone has to provide the service to me and what is the legal i mean i'm sure it's different from country to country but how can i i buy that it is possible it is easy

**00:43:17**  does the telecommunication companies have a problem with that can you tell us a bit absolutely so um when you're buying internet in a data center it is actually very easy to do there are lots of providers there are lots of companies um it's very competitive and so in the data centers the internet is not there we don't have a problem of people like potentially turning things off that's not really where the problem lies and it's also cheap it's competitive

**00:43:49**  it's cheap there's lots of options the problem is between the data center and your house because that's where you've got one or two companies they have not upgraded their networks in 20 years they are only they only move when there's somebody threatening them and basically the way that they move is to try to crush that threat so that they they don't have to move anymore you remember back in the 90s we had lots of dial up there was a big explosion of different

**00:44:19**  internet service providers and then all of a sudden the cable and telephone companies they created dsl and cable and then they they just squeezed all of those little companies out of existence and then we've been living most of us have been living with dsl and cable ever since so if there's no competition in the in the market then these companies will do absolutely nothing so how would you get a fast internet connection so um you can you can contract if you let's say you're

**00:44:50**  in a you're an area where there's no fiber you can contract to get fiber run to your house and there are companies that will do this for you it's very expensive but if you're making gonna make money off of the people in your town then this is potentially worthwhile for you and the the way you do it you find one of these companies you contract with them the company that owns the telephone poles is usually legally required to allow somebody to put their their cables on them as long as

**00:45:22**  they follow certain rules that's why you have the phone the cable and the uh the electricity running on the same telephone poles the if the electric company owns the polls they're required to let the phone company use them if the phone company owns the polls they're required to let the electric company use them so based on this legal requirement you're able to use a company that will run fiber right to your house you're going to pay for it but it will get you internet to the nearest data center and then from

**00:45:53**  there you're able to um you're able to release those lines and then you're able to get a um you're able to get fast internet which you can then sell to your neighbors excellent thank you guys someone do someone has a question for kayla okay then what next okay

**00:46:23**  maybe i just i just like to repeat what you what maybe might take away from from what the g dns is is that i i imagine this is something that goes lower than than the anonymity networks like thor and the new project today or i2p but it is going to a lower player a little bit and it is only trying to tackle

**00:46:54**  um would you say scienceship resistance is is this what it provides and and then we would have a standard resistance internet and on top of that it would be actually well probably anonymity networks would work better and support that too is that the first memory or or am i yeah yeah yeah yeah totally it's a it's about censorship resistance

**00:47:24**  and censorship takes many forms you don't think about your you're being censored because they haven't upgraded your the quality of your internet in 20 years but that is actually a form of censorship you don't have fast internet that is a way that you are being prevented from communicating all right oh wait so so wait yes this this can be let's say layer one and also layer two i mean it

**00:47:57**  it works also it can work also as um how to say um i i i forget the word but basically um it can work on top of the existing infrastructure too am i right yeah yeah yeah it works it works either on you can anything that could connects two computers together including the existing internet is working for transporting data for cg dns

**00:48:31**  excellent thank you i wanted to make one final like uh um plug here is that um because the packet system ecosystem has this institution of the network steward we are always looking for uh projects and people who are developing technology in the space who need that funding and that because um the the packet network steward funds whatever will help

**00:49:02**  benefit the objective of the project so um it's something that wasabi wallet can potentially participate in or any of the the side projects of wasabi wallet can potentially participate by proposing a project to the the packet network steward and that can be funded it'll be funded in packet but you know you can liquidate that to whatever you want and that's a way that we're able to bootstrap a lot of the technology that we need for

**00:49:32**  this network to work and that that again is one of the reasons why we couldn't have just done this on top of bitcoin because we need that aspect of the financing to build out all of this infrastructure that we need yes sorry one more question in order to have an idea of the magnitude of the growing of this product do you have any idea how many let's say clients uh are running this

**00:50:05**  this software oh it's uh it's a it's a good question i mean i can tell you a couple numbers i mean there's about 200 people in our um chat which is um packet.pkt.chat so you know you can go there and hang out with cool people there's about 200 people in the chat there um there's about 300 people on telegram um i don't know exactly how many wallets there are how many nodes and so on um these are you know just kind of

**00:50:37**  nebulous numbers um i that's that's basically what i know and then what is that e probably a project or or website or community what is that well uh hyperborea was a i mean i i say was it's technically it still exists but really it was about research on the cjdns project and that and building the researching the the technology of cjdns that was going on between 2012 and

**00:51:10**  2014-15 or so for the most part hyperborea is not really active anymore a lot of the people who wanted to do websites that were kind of in their own little network um have moved over to the egg drizzle project and so research continues with igdrissel which by the way are great friends of the packet project um but the uh yeah the hyperborea as it were is not really a thing anymore and we're moving cj dns from the

**00:51:42**  research phase to the industrialization phase through the packet project okay thank you i have one more question i i i always have more questions well you know here sometimes giving we are touches we discuss what is the best programming language useless a useless discussion but now if i understand this correctly you are let's say

**00:52:13**  writing more new versions in rust is that correct yeah yeah i mean why why because i previously used c and i find it just unconscionable at this point to continue developing c or c plus plus because they're they're bugs and those bugs are going to harm people and it's just like you you

**00:52:43**  you memory corruption it's never done and like the person the very people who say oh i'll never have memory corruption bugs i'm too good i'm a good programmer that's only for idiots those are the ones who create the real problems those are the ones who create problems that in the end lots of people get harmed by that so i mean i get it you know you've got a legacy project it's in cc plus plus you you just live with that that's how it is you do your best you you use c comp you use whatever you can no exact stack that that kind of stuff

**00:53:15**  which by the way um my one patch to bitcoin was to turn on no exec stack in bitcoin so that um you know certain really simple 1990s era stack smashing attacks wouldn't work um but you know at this point we want to be doing things securely the way that you're gonna you gotta do things we can't just keep sticking with uh uh 20 30 40 years old languages that's my opinion anyway

**00:53:47**  yes we have some similar discussions i remember here one more question about that how do you how do you see the productivity of your the people programming in rust in comparison with with previous experience programming in c or c plus plus because personally i i i'm not a rush programmer i tried to to learn it many many years ago and i was fighting against the compiler everything

**00:54:19**  that i did was wrong basically so i said okay i i will try this a couple of years right after okay well rust has just very recently become onto my radar as something that's there i mean uh you know five years ago it just wasn't there yet you know it was still in research phase so now rust in my opinion it's there so you can just use it um and as far as productivity yeah i mean

**00:54:51**  you pay a little bit of productivity in terms of when you're writing the code it's a little bit less productive than if you're if you're a c plus plus person you know you can just bang out the c plus plus but where i get major productivity improvements is when i'm reviewing the code because if i've got somebody who's making a contribution to cjdns and they're like oh yeah i've got a big huge piece of code here i have to read that line by line to say well is that is that a memory corruption issue is that a memory corruption issue is that a memory corruption issue

**00:55:21**  and i know i'm not going to be perfect you know i'm going to slip by i can't say honestly that nothing's going to slip by you know we're only human here and when somebody makes a contribution in rust i can just look at that i can go through it much more quickly you know does have any unsafe i can i'm just not having to be as paranoid when i'm doing code review and i'm sure you understand the same thing you know you get if you especially if you accept anonymous pull requests into the wasabi

**00:55:51**  wallet you got to look at that code and you're like well is that somebody trying to do underhanded crap to try to fool me you know and that's just like that's the worst thing ever yeah yeah well we have now the the problem with the with memory because we're programming in a managed language and we have a guy that's a garbage collector uh what do you add but anyway reviewing reviewing code carefully because we

**00:56:24**  are we we have i mean people move a lot of money with uh bitcoin wallet and a mistake is could be very very very expensive in terms of reputation and well there's a company behind so probably it could be more than reputation so yes reviewing is is a problem i cannot imagine if i have to keep track of

**00:56:55**  a collection of pointers yeah it could be really hard yeah

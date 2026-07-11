# Wasabi Research Club #23 - Integrating WabiSabi with BenKaufman, MWietersheim, MrKukks & Dan Gould

- Playlist index: 23
- YouTube ID: `oTi0z1Sghp8`
- Video: <https://www.youtube.com/watch?v=oTi0z1Sghp8>
- Duration: 3:20:01
- Transcript source: YouTube auto-generated captions (`en`)
- Retrieved: 2026-07-11
- Accuracy note: caption text is archived as supplied by YouTube and may contain recognition errors.

## Transcript

**00:00:06**  yep everything should be okay now okay so welcome guys to the next wasabi welded research experience this is number 23 and today we're talking about how to get uh babisavi coinjoin magic into other bitcoin software wallets uh other than just wasabi wallet i'm curious because i think that's a very important topic to delve down to and we'll have a couple nice guests joining us today um and including mr cooks

**00:00:38**  so maybe andrew could you quickly say hello and especially can introduce your work at btc specifically the plug-in system as i think that will be valuable for the future conversation yeah sure max uh so hi guys um so my name is andrew um you can call me cooks um at least on twitter or wherever you see me um i work full-time on bdc pay um and one of the latest features that we've been working on is uh is a plug-in

**00:01:09**  system we're kind of trying to market it as uh the fancy term seems to be that's taking the most is uh the wordpress of bitcoin although that's a bit uh less mislea it's not misleading but it's uh it's a big broad term is that a compliment or an insult i'm not sure i think it's like a double-edged sword right so wordpress is like everybody builds a wordpress but at the same time wordpress kind of sucks when you really get into it

**00:01:40**  so i'm hoping we don't end up in that situation um yeah so we're trying to take it super slow it's with how we flush it out just trying to make sure that it comes out right and that we exposed just enough to you know be able to expand on it and not too much that you know everything gets crazy and nothing works anymore um so one so we are we we kind of already have uh there's two kind of plugins in ptcp actually three if you really want to

**00:02:10**  look at it that way one of them is um the docker plug-ins that we kind of tell people to just integrate their services in there that's basically like people adding electrum server to their to their btc install then you've got the integration so plugins like wordpress integrations that's just completely external of btc pay it's just something that you have to code for specific platforms like on wordpress so that's php um other stuff and then there's the new

**00:02:42**  version the new kind of plugins which is uh c-sharp plugins directly inside the p2c pay code code base um where basically we expose a few interfaces and then people implement them and they upload the dlls and we load these contracts inside btc pay and they can extend the ui they can run background services and all sorts of crazy stuff i don't know if that's a good enough intro i could probably dive uh do a

**00:03:14**  deeper dive but yeah i'm maybe a bit curious on how deep the plug-in system will go like how far can we manipulate ptcpa as a plug-in developer so okay so one thing we're trying to do is make it pretty extensive so right now it's quite basic in that we expose a few interfaces which is uh one of them is like a ui extension interface where we have these little pieces of uh

**00:03:46**  markers across the ui and you as a plug-in developer can just say oh i want to place this this uh html uh partial view in this part of the ui and then you can just add stuff to it so one one usage of that is basically just putting like an extra navigation item in the side menu or the top navigation and that links to pages that you create yourself in your in your plugin so you can extend uh the current ui and then you can add

**00:04:17**  new pages new routes um all sorts of stuff like that um one thing we're doing with that is basically let's see what is there um i've been working on just a small like demo but uh with the liquids uh integration so the first thing i did was basically allow a way to add uh liquid acid so that they can just so that you don't have to hard code liquid assets inside btta like they're like it is currently right now you have

**00:04:48**  to do a pull request to the main code base you set the asset id and all that stuff in the code base and we merge it and then you have to wait for a release with the liquid plug-in you'll be able to um just have a ui that's defined in the in the plug-in and on startup on the application startup it will just load the the assets you saved in there um so that's one thing so that basically adds uh configuration uh background services

**00:05:20**  at startup and also ui your ui additional ui and extending the current ui and that it shows like a new navigation item in the server uh so it can get pretty excessive you can build quite a lot so that's one of the first demo plugins we're also trying to move existing features into into plugins so that the code base becomes a bit more lean since we've been building a lot of stuff over the years and at some point you have to say okay maybe

**00:05:51**  maybe we took this too far with features that we should try and you know be a bit more gentle with what goes in there by default uh so one thing we're looking at is basically one thing i've been playing with is um moving the shopify integration into a plug-in and making that section of the ui also extendable so that people can build their own uh deeper integrations with other platforms in a similar way i already have a few of those planned out

**00:06:22**  um what else is there but so for example there's no hindrance in having a plugin that for example signs bitcoin transactions in a custom way um it all depends on how much we expose in the in the interfaces i mean you can build an entire wallet interface if you wanted to so that you you could do do it exactly the way you wanted to because right now the wallet send page in btc pay is you know it's like defined

**00:06:52**  as this there's no extension points in that there's no way to modify the flow and that's in a in a specific way at least maybe in the future would be possible but uh one way to get around that if you have a very specific flow such as use an external um an external wallet flow would be to either build an entire ui and just either you could probably like replace the wallet send link with with the new one and make that show and said so there is no

**00:07:24**  there is no hard limit um the only limit that there is is making sure that the current code base is extendable to to the means that you want it to be and i mean we're we're not really saying that we're going to have um main uh main blockages in terms of what you want want to extend we'll we'll see you as time goes if there's feedback to add another an extra thing in a specific section in the uh in the ui will probably do it um yeah

**00:07:56**  it's still very early it's what i'm saying so we can we can really just uh play around and see what what would work best in a way that's flexible for everyone yeah that's super fascinating uh so thanks for the ui explanations um and it seems quite nice but one other use case that i think is more of a background feature kind of that as soon as points are received uh the wasabi demon in the plug-in kind of starts coinjoining it directly is that kind of more advanced demon

**00:08:27**  functionality doable via plugin um okay so that depends in in how you want to integrate would you so there's two things to it you can either do it as a background service inside btc peso um we would you would we have a dependency injection container that's just a dot net core one where we throw in all our services in there so you can easily just add another hosted service in there if you if that's how you wanted to do it

**00:08:57**  or we we also have a an event aggregator um or i think you might call the mediator pattern pattern antenna system um which gets which we have events that go into it already when the coin is received when the payment is received when an invoice status changes all that stuff um which could uh trigger something else for example we we also have web hooks in there so when a payment is received on a wallet it can trigger something external btc pay

**00:09:29**  so it all depends as well how you would integrate wabi-sabi if it would be built inside if we would be able to import some libraries and uh loading them inside the btc pay process or if you would have an external daemon and we would be pinging it and doing the coin mixes two dots wait wait wait we could do libraries and that would be a nuget package would be good for btc

**00:10:01**  yeah that could be pretty cool i think i think we could do it that way um if if you had for example a package where basically you have all the base functionality you need to trigger a coin joint uh not trigger actually we could just induce the coin join client library inside b2c pay um that will that would probably be the best way to do it because when you run i think currently you have the rpc that you have to call and you know operate it separately if it's built into the

**00:10:32**  process of btcp that would be pretty crazy like you can do like the wall and send page we could probably either wrap it inside uh wrap the functionality around your coin joint mechanism that's gonna happen where you'll be able to do a uh a payment from a coin join that would be pretty cool um but anyway in terms of technicals um if you have a library that we can run as a as a background service inside the

**00:11:03**  code base of btc beta that would be perfect so i i explored i actually asked zuckson to explore this to me and he said um btc bay wants to keep things lean and and that's why uh nuget library would not be a good idea

**00:11:33**  um yes um but we want to keep things lean but if it's a plug-in then it doesn't matter because you can import a nougat library inside the plugin which is just loaded as a as an on an individual level so that would be would become opt-in instead of just uh having it lying in the background in the b2c code base um one example of a so basically our plugin system is just

**00:12:04**  somebody create somebody references a a few nougat libraries from btc pay we have i think it's called btc pay server dot abstractions and basically you will implement an ibtcp server plugin inside that there is a methods which is like i think it's called configure where you can just add stuff to the dependency injection container and you're free to do whatever you want from at that point it's like you can add ui pages you can add hosted services

**00:12:34**  running uh throughout the entire lifetime of btc pay um you can listen to events internal events that happen in btc pay that you would not be able to to do through web hooks inside through the btc pays api um so you can go wild with that um and the best part about it is that the code would not live inside the code base of btc pay it would just be a plug-in that somebody just uploads inside btc

**00:13:06**  and it runs on their server only lucas do you have any ideas on implementation the way we've been writing it should be amenable to reuse in that way i think it boils down to like how deeply can you integrate

**00:13:37**  um in a way that satisfies the constraints so for example if the btc code makes assumptions about like what kind of inputs you can include and the coordinator is going to reject that later on because i don't know we don't support 68 for starters or only paid a witness pubkey hash or something like those arbitrary constraints are probably going to be the main source of friction like how do you make sure that you can actually drop in something that's uh strictly a subset of the

**00:14:08**  functionality that's already available internally but as long as that is not insurmountable i think it should just work like it's just a matter of wrapping the internal like wabi-sabi library implementation making sure it's public of course first and and uh making use of that and the hypothetical plug-in yeah that would be that would be nice because any constraints in the software can be done on your end so when you wrap your wabi-sabi nuget

**00:14:39**  library inside the plug-in code base you can just like only listen to when only listen to payments that come in on the stores wallets if it's a specific type of script or something like that so you can restrict it based to your you know customize to your needs we obviously don't have a lot of stuff exposed inside btc pay right now

**00:15:11**  but it should be quite possible like you'll have access to for example uh nba explorer if you wanted to um and you know the the utxos available and all that stuff so you could completely bypass any restrictions inside the btcp ui and build your own uh wallet send ui if you need it to or just replace it entirely it's quite like it should be quite capable of doing like a

**00:15:42**  174 workflow that should be more than yeah and which one is that again bit which one uh that should be compatible yeah for sure we already have full pspt support in there anyway like the entire what the entire wallet sending system is using pspts internally and we expose them

**00:16:13**  i think it's like you first go on a send page and then you can say uh create a transaction or sign it directly at that point and it'll just show you a sign psbt and then you can say either broadcast it or do a page join or something like that so it's already in that in that style like even in the explorer exposes everything through psbt's if you wanted to avoid the wallet cent page uh might it be useful to have output script descriptors here so that for example the btc pay wallet can just get

**00:16:43**  the excite private key and script to the wasabi client which then adds this key to its wallet and signs the conjurer i didn't understand that you you have output description uh you're using output descriptors on your end uh no not yet but i'm curious if it would be useful basically then this way how wasabi can use its own signing magic right and does not need to rely on bbc

**00:17:15**  signing stuff right because there are some nuances uh in conjunction uh yeah yeah for sure um so then we kind of just get the private key from bbc basically yeah you can do it you could like the hot wallet system in btcp is the hot wallet uh system is not even inside be on the b2c pay level it's on the amb explorer level so you can get the key completely separately of b2c pay as long as it's a hot wallet obviously

**00:17:45**  um yeah no there's no issue there for sure and for in terms of output descriptors you don't technically need it um because well btc so first first of the store set up in btc it supports importing an output descriptor with some constraints to it that it has to be hd and i forgot what else there is basically it can be like a wrapped one or something

**00:18:15**  yeah there's there is some basic support but we converted to a to our internal format which is on the npx level uh but it's not it's nothing complicated so you can quite easily map it to whatever you need and then how about having a p2 endpoint functionality in this

**00:18:46**  whatsapp what we saw be plugin what do you think a p2 endpoint well i mean there is already pay to endpoint support than in btc pay i'm just curious on i guess if you wanted to do if you wanted to replace the default behavior for patreon joined and how we suggest utxos and the page proposal itself um you could you could just overall just

**00:19:18**  say screw this implementation and just replace it with your own using dependency injection of some sort um with whatever you provide in the plug-in so you can probably just say um replace the entire page rain receiver end point with with our own wabi-sabi endpoint if you have something very specific in mind because i i i'm not sure what if you do so it's quite flexible i think everything should be

**00:19:50**  like you can you can hack your way to any functionality you want most likely if you if you're good enough with mastering the dependency injection container yeah yeah it will be a replacement of page one it would guess uh it's basically like both sender and receiver provide inputs but also hundreds of other users provide inputs in the wallabies i'll be transaction so but it wouldn't be a it wouldn't be a p a 78 one so

**00:20:22**  exactly exactly i mean you could yeah go ahead i have a question for you andrew and about the page on implementation but no knowing the implementation the the trend and the usage do you have any numbers that you can share with us about how many how this feature is being used in the real world by people adoption

**00:20:52**  well i would tell you but if i if i could tell you i think we would have done something wrong because we have no tracking system in there um we have we have no analytics on anything so we have no clue how people use btc oh but but you you provide i probably i'm not sure but support people make questions so you have some intuition of how this can be using in reality because it's like it's like

**00:21:24**  wasabi for example if we never receive any nobody asked about a feature nobody have a problem with the feature nobody well that probably nobody is using it right yeah i i would say that questions around patreon are quite low um but i also feel like that stems from the lack of motivation from a merchant point of view um right now we have the most

**00:21:55**  primitive version of a patreon you can do it in terms of bip78 functionality that we can support um i have worked on i have worked on some private consulting stuff around dip 78 where i don't think it's out yet at all but where i've worked on batch transactions and output substitution and all that stuff so and it will be quite more beneficial to a merchant to use these

**00:22:26**  kind of things in the future in terms of life uh what vicente merchant why is so they have to opt into this feature why is there something wrong with this yes uh so the main detraction of it in terms of us promoting it is the hot wallet uh requirement obviously that's like

**00:22:56**  we don't want people to just decidedly create a store uh configure walls and just automatically have a hot wallet that's just too not risky but it's just you know people already have always had the option to have a watch-only wallet inside b2c pay and never risk their funds getting stolen so all of a sudden we're promoting the opposite of that with with pay joints so for me but how about if the user opts into doing a hot wallet then the default is patreon

**00:23:27**  activated yeah it's two separates yeah that's that's a good idea actually uh from mine i think that's a good thing uh i i do think that i want to you know instead of just enabling it by default only i also want it to be like incentive based and that's you know once you start like if you have we already have a refund feature inside btc pay and you already have merchants sending transactions from inside btc page wallet

**00:23:58**  so the idea is that we grab those and we start batching them inside inside the pay joints so that they save on fees um and then after that as well there's also the parts um where you can eventually we want to have a way to support multiple wallet script types so you'd have segwit and and p2sh on top of that two separate wallets with generally generating two

**00:24:28**  uh two addresses so the default address would be p2sh based and if they do a pay join it would automatically upgrade and substitute the address with the secret one that would also save on fees what else is there also basically just substituting uh outputs let's see how was it basically uh do if uh if a pageant happens and you've got the right circumstances

**00:24:58**  you can just die direct redirect the the payment being done to a pending transfer that you wanted to do so it becomes kind of like a like a three-party coin joint where you as a merchant is not even involved in the transaction because you just use inputs from from the person sending you money um there's there's a lot of stuff that i wish would be included obviously but it just takes a lot of time and effort um we'll get to it eventually but you know things take forever

**00:25:30**  so let me ask one more thing that's that's my last question regarding this topic which is again a practical one uh an other question i had and i did not investigate it but i hope you you guys did that bit 21 you whereas pedro in your urls are just an extension of big 21 urls so now the question arises that you know

**00:26:00**  wallets those are compatible with beep 21 urls how do they behave when they see a pageant url do they throw an exception do they just dismiss the page or import of their url or or did you did any anyone here uh try to investigate that yeah i i've checked a few wallets and a few code bases around it

**00:26:31**  um for the most part i would say like i forgot the actual numbers but i would easily say like 90 of all wallets would just if they don't support paging they would just ignore it i've seen some cases where where it crashed because it expected the string and then basically if you add an ampersand to it it would just not recognize it and crash but that's like a deeper issue as well uh basically it was expecting that the bip 21 url was just uh bitcoin colon address uh and then the amount and nothing else

**00:27:03**  like if you even added a label it would crash so that was even a deeper bug on their end um but in most cases there was no issue yep that's all i remember all these fields are optional the wallet don't doesn't understand it they just should just be skipped yeah exactly that's that's one of the main things that i liked about bip79 um so bip 21 is you know nice and simple at least so people know what the hell it is and when they look at it

**00:27:34**  it's not too scary um i know that uh who was i think it was wax swing that had it on he had the gist with and a small discussion about a format for join market before before 579 i don't even remember if it was before or after bip 79 was announced um where they would have like the three like i think i think was address endpoint in the mount with like comma separated but that would not have been nice to to share around either

**00:28:06**  um even just for copy pasting or trying to highlight the text with a double click or something that would have failed at least with bip 21 it's nice and easy you can see that it's all one long string and it's people are familiar with the string as well with the string format um and also with bib 21 i it it allows you to just expand it even more if you wanted to so if you wanted to change communication uh for a bit for for the pay joint so from

**00:28:37**  from uh http endpoint it would just be i don't know like you say pj communications or something and then you'd say equals qr or something or or nfc or bluetooth and then you just scan the network or you you make your phone emits and nfc data and then you just tap it with another phone or something like that that so those stuff is completely possible if you just extend it with minor opt-in opt-in layers

**00:29:24**  all right thank you so there are some other guests in the quad too so max would you like to you have like do a transition yes so of course feel free to stay in if you still want to contribute and hang out i was super helpful so far though already so thanks for that um we're also joined i think it's ben kaufman and moritz uh they're both here and these guys are tinkering on the amazing

**00:29:54**  spectre wallet which is kind of a graphical user interface on top of the bitcoin core infrastructure and i think that's a very promising project too so how are you both doing not too bad i think uh ben is um trying three times at the same time listening in posting and doing the new release but um i wouldn't expect anything else that's good multitasking yeah yeah i'm doing good here

**00:30:26**  and drinking a beer yeah um yeah it's really great i'm i was talking to max last week about what what's happening at um and it was it was it's really interesting what's what's what's going on with you guys and um especially like um how how you're working on the on the better your ex now and the next release and stuff so very excited about that

**00:30:57**  thanks and welcome guys and happy for joining us um maybe by the way can i can i ask a question for because now we we are here uh a couple of uh wallet developers and i would like to know what do you think is what we need to improve in the

**00:31:28**  standards or collaborations or what can we do to to make the the walls more compatible if you want more easy to to interoperate and of course i i prefer to to know about privacy but i understand that's probably not the the main focus of all the wallets but

**00:31:59**  just to know about that what do you think i guess it's just a lot of more uh communication i think there is not not really uh a very you know central way to to coordinate stuff um to uh set standards for for stuff for i don't know for example backups uh stuff like that so it's kind of very very um spread around

**00:32:30**  um which i guess makes sense but it would be uh quite easier i think if it would there would be like some uh more standards i guess for that i think it's also just a matter of someone picking up the slack and actually doing it i mean for example andrew shell with hardware wallet interface right that's you know the concept is obvious but

**00:33:01**  it just took a while until someone finally did it but no pretty much every wallet is compatible with it yeah yeah also so for example just just for to be a bit more concrete probably in my questions for example do you think that um if we all implement uh output descriptors for example

**00:33:32**  could that help or do you think that there is something more important that we can do first for example you can you can say hey you wasabi wallet i say we we think you should do this first it's perfectly okay to say something like that yeah so i'm not sure i think implementing out of descriptors would be great for us because we already uh use them natively so if other wallets would would support

**00:34:03**  that too then i think that would be a great standard to to move to um but no i don't have anything else like more specific in mind okay and sorry and for example we have been discussing about pay joint right uh minutes ago i don't know if you were here but um well

**00:34:35**  uh you know um i'm not sure but it seems to me probably um a page on is it was um invented or designed with the idea of of being useful for merchants i don't know if that is so true for normal users i mean if i if my wallet because yes i understand mertens has a server that is running all

**00:35:08**  the time and it has a web server and all that kind of stuff that may make it makes it uh ideal for being a patreon receiver right probably a mobile wallet is not a good um example do you think pen to endpoint have some future uh so i didn't research about it much but yeah i think so i think

**00:35:41**  again i'm not for for specter uh it's not really uh a tool for you know for a lot of views uh from for merchants like btc base server would uh but i still think it it could be a useful tool for some users do you have it implemented now uh no not yet uh we're looking to to have that but just not enough time again well i think here comes one one of the crooks with spectre specifically is that

**00:36:11**  you focus on multi signatures and then i would guess the vast amount of bitcoin hold inspector is protected by multisig which is that's just a guess um and that makes coin joins of any type more complicated even two-party conjoints like page lines what do you think patrons with multi-stick is that even doable uh i've i really didn't look into that uh probably stephan i think did look into that but you'd have to ask him um so yeah i'm really not sure how

**00:36:43**  difficult would that be andrew i i do think that yeah i do think that patreon is possible with multisig but the issue comes where it's really hard because you have to match basically the the sender and the receiver have to have the same script types so if the sender has multisig and the receiver has doesn't isn't using multisig and he doesn't have a uh output an output substitution

**00:37:14**  location to to a matching multisig uh script type then you can't really you'll have a fingerprint on the page right transaction so that's usually not very effective and the usage on multisig will obviously most merchants probably don't use multisig and if you have a page on receiver server with a multi-stick hot wallet setup that's kind of stupid i think yeah so um but i guess if you wait for taproot i

**00:37:45**  guess that's that would be completely fine for multi-stick pay joints require the non-ownership proof right but stephan figured out um i i think you could the attacker could still steal money even if it's only youtube party coin join if you cannot prove that the other utxo is not from this wallet so i guess the same applies for multisig

**00:38:16**  on hardware wallets or even single sec carter wallet day joints it's probably not worth spending time on well i would like to know if if the market is is requesting this kind of features or if it is just that some kind of developers masturbation you know that we want to have this complex uh algorithm

**00:38:46**  it and it's it's hard to know right because from wasabi our focus is precisely to not to know i mean we don't want to know so it's hard but probably i don't know if you have more information probably you have a um i don't know he probably you know more about your users probably not but i would like to know if you know something about it uh i we have

**00:39:17**  at least inspector we also have no analytics no data whatsoever so not really uh so just just from talking to users we do have a few users asking about it but i have no idea if they ask him about it because they heard about it and they don't really know what it is or because they really know what it is and want to use it so i have no idea yeah from from my end it's some people ask about it because they

**00:39:48**  see it in the ui but the not a lot of people have an idea of what it does um but the idea of having a pay joint that's camp with a with a payment destination that's backwards compatible so you know just the standard 21 is that you can increase adoption without harming any any usage and the idea is eventually it becomes you know worthwhile to a merchant that's running a 24 7 server but from uh from what you mentioned as well

**00:40:18**  like a mobile wallet it's uh you can't just you could do it you could always just spin up a tor circuit and all that magic but if you're in in close proximity you can't even do it with just uh qr code scanning and all that stuff or nfc or some other p2p communication that you do between wallets and it from my point of view at least it's not as complicated as you make it

**00:40:48**  out to be it's literally like two to a two process job right so you receive a you receive a bit 21 you send it at pspt over there okay maybe it's a bit more more of a more steps but it's you receive a destination to pay you create a transaction that pays it send it over and then you receive a a pay joint transaction that you can or or don't want to proceed with

**00:41:18**  and it's just psbt uh parsing and then the business logic on top of that well i agree that there are a lot of users who just have mobile wallets or decibels that shut down properly but i think a decent percentage or at least a decent absolute number of bitcoin users have their own server or their own big control note uh probably running 24 7 in the background so it's still i think a decent potential user base that might be well suitable for these pay joints and to be

**00:41:50**  honest i think that's all that we need right we don't need every user to run pay join all the time we just need to have the threats that the small percentage of users run day joints to already think the analysis yeah exactly and okay do we i mean what what is that small percentage at one percent i mean they are already operating with probabilities right and 99 percent probabilities i think is

**00:42:21**  as good as as any other assumptions they have so so i don't know we need 10 percent 90 probability not that good so maybe we should have more no yeah i i do think it needs to be more than one percent for sure to even make a dent in anything even from just their own perspe perception right of how these things operate

**00:42:52**  um and also they wouldn't even figure it out at that point if you have if you have the specification nailed down well enough that the fingerprinting is not happening then you none of us will know really that there is a 1 10 chance of analytics poisoning happening through to pay joint transactions um yeah i i do think we can there the the best way to look at it is just patron on its own is probably not going

**00:43:24**  to do the dents that you wanted to but it was part of a diverse a diverse selection of tools that you can use that as as people use collectively in in their own little ecosystems they probably add up enough to make the dent that you want wanted to i just wish we'd be able to see the clusters on to to actually see how if they're actually getting poisoned somehow or not on on private uh analytics software but

**00:43:55**  we'll never know right so it's it's way too early to write on page ones i mean but you know i think the hurdle is is the for the user adoption is the user experience i mean sir it's nice to have have this on the merchant side but that i i don't know what percentage of bitcoin transactions would be we'd

**00:44:26**  be the big 21 urs but i think it's even smaller than one percent you think so i i i think the 21 is quite used like uh from our ends our qr code has always been 21 because it adds the amounts to it um we only have a very small percentage of people that use the address directly and the amounts separately um because your your service is for merchants yeah yeah that's true

**00:44:56**  um it's i mean he has a good point right wasabi could as well just draw a qr code with the 21 uri and patreon enabled okay yes yes yes yes sorry yes yes you're right i completely missed that so it doesn't have to be yeah it can be just a qr code can't can it be because can other wallets read it even if they

**00:45:27**  are not compatible with pay join yes but they must be compatible with the 21 and a qr code reader but yeah it should be a good requirement i mean do they do that that's the question right they from all the wallets i've seen so far they've all supported bit 21. uh obviously from wasabi side you probably would not add an amount you'd only have the bitcoin address there i'm guessing okay okay that's very good then i i

**00:46:00**  withdraw the strength from my opinion and and yeah i think my argument doesn't all that that much because there are fewer quotes yeah sure i have and again i think it's also a usability thing right i think if more wallets especially wasabi would be able to click on the link and then be opened like the bitcoin uri is supposed to work and if you have that ux i would be sending around these euro hits too

**00:46:43**  yeah can i yeah sure go ahead i was gonna change stupid uh sure so i mean bitcoin the even inside btc pay we we actually have some naive implementation for um natively opening bitcoin uris basically browsers allow you to hook onto uri schemes and then they will open to a specific url that you set them to um so going back to the plug-in thing

**00:47:15**  um if wabi-sabi is running inside of the plug-in system we can even divert a url link to open up in the wallet sent using what we savvy to do the coin join to the payment destination through it yeah that might be kind of uh another way to connect wasabi and btc pay in a bridge so you have run wasabi separately

**00:47:45**  and btp separately and you can somehow manage in the gui of wasabi the backend server of bbc pay maybe you stop what you mean a bit andrew i was talking more like um if you were running wabi-sabi embedded inside btcpa directly then you would be able to use the bitcoin uri functionality directly with wabi-sabi as well um obviously that's a bit more

**00:48:17**  intricate i guess in implementation details okay what's the next topic adam oh i i wanted to ask more if if he could talk about the history of spectre rather than the inspector like like how did how did everything yeah like like like when did you think

**00:48:47**  about it why if it's the mission you know what i mean just the history lesson okay wow and it's not going to be a big history lesson it was well i started out with in 2017 with the idea that there should be better hardware wallets and i was struggling to find the right technical guide to start it and it took me like a year and then we were in portugal in lisbon at the conference where you announced wazabi wallet and um yes i was sort of confused by you

**00:49:17**  on the stage there with the with the with the pullover and stuff and was just wrapping my mind around what's coinjoin and what's going on there and i met stephan at the party in the evening and he was like hey you're a business guy and what the heck and you want to do a hardware wallet and then yes he showed me some prototypes and i got really excited and yes then we partnered together in the company but yes and then we're we weren't really sure where to start and how to start so we started working with the fraunhofer

**00:49:49**  institute which is the leading german cyber security institute so like infineon and siemens and everybody goes there and we're just discussing some chip designs and had everything really nicely laid out and then we started talking to vcs and started to figure out that we don't like this whole vc story so much because they like blockchain and tokens and are not into hardware because hardware doesn't scale and then also not into open source because then they don't control the ip so things

**00:50:20**  got uh yes in 2019 in the summer i really had to realize that okay we have some really good prototype and sleepon is doing great work but the stuff that we want to do we don't get to finance another conditions we wanted and i already invested some company as a money in the company and then yes then we saw hwi and i never i just basically asked steven like okay when we have a hardware what what's gonna be our desktop app and we couldn't find the desktop up we wanted to use with a little bit like

**00:50:51**  uh cold card but you really wanted to have a desktop app with it and then i was just poking stupid noob questions into sleepon and um was figuring out with him okay you can basically do a lot with the almost everything with the bitcoin core node and i always felt like this feeling that people especially at technical conferences or anywhere else that goes hey you have to run your node and you have to use your node and check your utxos and stuff and um and i always felt bad because i had the computer at home there was bitcoin call

**00:51:22**  running but i wasn't really using it so and then we we sleep and said yes i can do a little prototype and wrap this around and we can make qr code gapped and pspt transactions and then keith mukhai a guy from chicago came in in just over a week prototyped ledger and trether support i think into it and keep key and then we could do multi-sig and and it got really really interesting but um steven is excellent at

**00:51:54**  prototyping and then really building it out took us done from the say autumn september 2019 really to really launch it was in august last year and along the way um i was very happy because um kim neunard was joining us first and then also ben came around after advancing bitcoin in london in march 2020 and it was a tremendous help and and and

**00:52:24**  high energy great feature ideas implementing a lot and so we have a really nice team now with stephan which is which is really a great great technical guy and and and brainy and then the two other guys also very smart and um so i'm i'm like there yeah i i like to support what we're doing so at the moment the the business model what we are doing is really that's we building specter desktop and on the

**00:52:55**  we have like an enterprise site where companies come to us like a custodian or a bitcoin development company or specific uh enterprises who want hardware or firmware solutions and we build that for it and this pays the bills it's not too much and um yes so we are using the enterprise side to pay the bills and and try to make expected desktop better and of course um the the project is will be

**00:53:27**  like let's see how this works with this enterprise side business model and i'm i'm ready to to keep supporting it we're getting some interest from vcs now but i i don't know if if if this is really the the best way forward and then because i think when you once start the vc route and they want to push you into the next series a b c d and then you have to offer an exit or something so i don't know if it's really well aligned to how to to to

**00:53:58**  to become a vc finance project and so i'm i'm a little bit puzzled with that maybe you have thoughts on that but this is where we stand so i think ben is currently working on a packaged core node into spectre so that you can have a one-click install on a prune node and um also like tour integration so and i think then we are quite ready in the feature set and of course we're looking for business models also inspect

**00:54:30**  the desktop where we could uh integrate let's say uh one instance was i was discussing with max um uh like a api for for conjoined vasavi coinjoin where we would direct our users into your coinjoin or service integrations with uh collaborative custody or or something like peer-to-peer exchange so this is something we think about but it's um it's it's it's still quite early yeah so that's the story

**00:55:06**  nice um i i would have like more more maybe ben can answer that too but like how would you like to get wasabi or wabi-sabi because you don't really have a plug-in system like btc pay so what technical approach would you guys think of what would you like yeah so we're trying to to work on the plug-in system actually so it's mostly uh kim from our team that is uh working on that

**00:55:39**  um so yeah we'll probably try to to go with that approach but it's still uh underworked so okay cool you didn't know that but like what's what stuff would you need from from like the wasabi client that you could use um so i'm not really sure i i guess basically just an rpc server with with

**00:56:09**  all the functionality would suffice probably um but then in the way that the rpc server manages the wallet that you have in bitcoin core sorry i mean you do all the signing and stuff with bitcoin core right yeah yeah so that means if you would have some wasabi rpc server who would do the signing would it be the wasabi rpc server that signs or the

**00:56:40**  bitcoin core node i guess it depends so whatever is is needed uh if it's needed to be through wasabi then then wasabi i think we can we can work through that by the way just for max um you know max we have to implement an external signal because um if you want to sign your your coin join

**00:57:10**  with your hardware wallet for example automatically let's say and wasabi has to allow that so if you want for example that bitcoin core sign a transaction for you you will just have to create the external assignment it's a technical detail that just yeah that's a good point but just as a quick note then bitcoin core also needs to understand the non-ownership proofs right because

**00:57:42**  otherwise external signing is not secure no designer the i mean you don't need to well it's uh it's a i think probably it's not for this meat but i think it's not a problem i don't know like what what i want to come out with this question is if we want to get wasabi in a spectre wallet how much do we actually need to contribute to bitcoin core just because vector will use bitcoin core a lot

**00:58:16**  uh yeah i'm really not sure to be honest so i didn't really look into how wasabi would work so i can't really give an answer right now yeah i think no one can i think we don't even know no yes probably i'm wrong but i think the only thing that you really need is to the wasabi to know the expat key right um and

**00:58:47**  oh no no sorry because it it well probably a a an expat key that is known by by it can call and implement an external signer the only thing i'm not 100 sure how is to create all the the addresses right and well probably that's not a problem either no it's it is possible yes it is

**00:59:19**  possible it's just we have to think a bit but it's not a problem i'm sure anyway i would like to know what what is the the spectre team working on now and what what i don't know if that is possible to know if the surprise for their their users but

**00:59:49**  um what are you doing yeah so right now uh we just finished with uh with this uh addition as as maurice mentioned of bitcoin core and spec and uh torr into spectre so basically just packaging them so it's uh basically instant setup uh we still have some some factoring to to do right now so just cleaning up some some stuff we were delaying uh for a bit

**01:00:22**  uh after that uh we are looking on on stuff like liquid but we still uh don't don't know for sure what where what we're going to do next so kind of going with it yeah i think also with the release of the package note we will do some refactoring and cleaning up the whole code base so this is what's important to kim and and and and stephan and

**01:00:54**  i hope also to ben because ben is all like ben is all already um like he loves new features let's say so but um so um but we are quite there with the features i guess and yes and then it's it's a kind of a strategic decision what we want to do first like focus on integrations or um [Music] at add new new bitcoin features like lightning or liquid i think liquid is quite interesting um i don't know about about you guys

**01:01:25**  is this something where wasabi is also thinking about or is it is it that are you very focused on just uh pure um bitcoin unshame solutions it would actually be cool to get a confidential transaction coin joint implementation running on liquid uh i i should have counted the number of times that we said during the wasabi research clubs like let's just use monero with ct and green signature that makes everything easier

**01:01:56**  no but yeah the liquid coin joint theme i think metal delve tweeted about it i mean we discussed it already like uh maybe a half a year ago it's it's yeah it's it's a it's another possibility that we could could do also to complement like the whole privacy ecosystem a bit more yes but it's it's quite quite a little bit away there's like the liquid stuff is interesting but there has to be some cleaning up and and and iterations and hardware support and it's

**01:02:27**  it's not quite there yet for for for that yeah but to give a quick summary on second player protocols in wasabi uh i think first is priority to figure out all the mistakes of the first layer and that's already a ton of work and then i mean everyone has to implement lighting probably um so sooner or later it will come but we want to implement lightning network right and like with all the privacy focuses that we have on

**01:02:58**  chain so far and that's just impossible nowadays yes and after after that we have to find all the problems in second layer because lining is is probably too far of what it was promised right is there a lot of details that can compromise the privacy of the transaction

**01:03:29**  and yes we are not close to to to fix that in fact we didn't start it yet yeah tricky yeah that's that's that's a good point we didn't even started yet that's it's it's very tempting to to

**01:04:00**  look at the different stuff and then do this and that and i think this was something maybe it was in the first year a little bit like tricky for us as a team to figure out because we were playing with a lightning app and we were looking into the hardware stuff really really deep and and spent quite some money on on time on the whole chip design and and stuff and then we sort of said okay let's let's also with the hardware like okay uh they don't want to finance us okay um i

**01:04:32**  think we had one meeting with an investor who wanted to buy us and um we were a little tipsy let's say a little drunk and sleepon got angry and and he like he got bullish and went deeper and i don't know what he does but he he hacked me sort of and then we were like yeah let's do this and i was like i put in another 50k or 100k and let's let's um let's let's do it the whole hardware thing do it yourself and

**01:05:02**  so this is how expected diy then sort of was born and now we're doing quite well we have the smart card support and stuff so and we don't want to want to let go of that i think it's it's a really nice hardware wallet we get really really good feedback so like everybody who gets it and buys it and uses it says is his favorite hardware wallet because of the big screen about the bitcoin only focus about all the power features and it's still quite simple so

**01:05:33**  and then yes this was was was something where we really were very stubborn but with the specter desktop thing we are a little bit opportunistic and see okay this this really works and it's so so it's tricky not to get sidetracked because there's so much stuff going on in bitcoin and you really have to find your niche and then really refine your art in there and then and make it the best possible solution so it's yeah it's it's tricky and the new users are flooding in and

**01:06:05**  using coinbase yes i mean i don't know what we can do about this it's just i mean i was too using bitcoin at the beginning and it's just i don't know it's just impossible i think to because they have this huge market and we have the same here in austria with bit panda but panda is a big exchange here and um they have all the coins they have all the vc money from vala ventures or whatever they even doing radio spots

**01:06:36**  here in austria's my mom calls me say like hey this bitcoin exchange does and then every newspaper because they are like the big austrian unicorn now so it's a it's a show on another level and it's i don't know it's it's it's it's it's really strange and we are we're hoping that um some bitcoin only services will bootstrap maybe a european version of so on bitcoin is coming or something in germany or in austria so

**01:07:07**  yeah relays is quite quite nice but expensive and they have the problem that they're doing everything on chain so i think two weeks ago and they had to shut down the service for a couple of days because the exchange there the back end exchange they're working with was wasn't wasn't supporting the high fee so there was some kind of argument about the feast there and yes so i mean that the pressure on liquid and lightning to come will be will be where we will be strong in six

**01:07:38**  months holy holy moly yeah i mean liquid is kind of an easy solution to the p pressure right specifically for traders high frequency transaction makers in general yeah um i wanted to ask the follow-up question um it's interesting to see your story with the hardware wallet work good that you kept it up thanks for the investment um

**01:08:08**  this is painful it was painful i don't know i don't even want to know how many bitcoins that was i won't tell anybody um no but um what do you think are what percentage are roughly like what is the demand for the pre-built spectre hardware that you actually sell compared to people buying the do-it-yourself parts and putting it together it's a small tinkerer and maker community i would say so we sold about 50 but we wanted to keep the demand really

**01:08:40**  low because what we want to do is really focus we don't want to go with specter hardware wallet we don't want to go to the mass market because it's uh it's very competitive already outside there and then if you sell like 500 a thousand of these pieces you make it's not a good business you you you sell one of the devices you earn a hundred euro and then you have to follow up with all the support and then and then you have noobs buying it and loops don't know about private keys and nothing so we really want to focus on

**01:09:11**  the advanced bitcoins and the technical bitcoiners but we get a fair amount of messages now in the dms on on telegram and the chats and our asking hey can i buy a spector shield and then i usually put them on the list and let them wait a bit and if they come back and say oh i really want to have to expect a shield now then we are then we are talking otherwise it's uh it's it's very limited so i don't know how many specter diy or shield people are out there maybe i should seat sign on ask

**01:09:42**  seat sign how many sold in u.s but it wouldn't be more than one or two hundred people i would say something like this okay interesting yeah yeah i bet that scaling hardware production is a pain in the yeah i mean you have to basically you you need some good operating business or get some cash flows or whatever or have a big vc investment and but then you don't really have time so i

**01:10:12**  believe like we could not have developed spectre hardware and the specter desktop as it is today if we had vc money and with vc money i think they want to have after three months they want to see sort of a crazy growth charts of whatever you're doing and um and and go go go go and growth growth grows so i mean it took us sort of 12 months to really figure out what we want to what our niche is and what we want to do and then it took another sort of 12 months go to market to

**01:10:42**  really um do to really have the product on the market and no no no we have a good product market fit i would say but and we couldn't do that with with vc money and i i had also my learnings coming from the business side you're very like like people always tell you yes we see money and you think that's the normal way and then you learn about bootstrapping the whole thing and i mean there is a place where we see money maybe later or whatever or

**01:11:13**  we can revisit the topic but at the moment i'm quite happy with with it was quite painful but it was uh it's it's it's great and it's great to be on it on such a team and make a sort of contribution to bitcoin yeah i would have one more question leading to a bit of a different topic um now that yuval especially is in here you can maybe answer the technical sides of this topic

**01:11:44**  um but first more it's could you maybe share some of your kind of feature requests for a coordinator fee revenue sharing model uh because it's something we talked about i know it's something you're interested in yeah i saw the meme today and um with the sewers canal and you were sort of um you had an accident in the sewers canal with feature good quests so i don't want to too much put this out there but i just want to say like we would be really happy and really excited if there would be

**01:12:16**  an api for for for your coin joint implementation your upcoming and because we can direct the our users to use um this this coin join we can add a coin join wallet which would use your back end in the in the end so it would be really exciting to to have sort of an integration there with uh with your conjoined coordinator yeah and like what are some of the um like specifically on that featuring like

**01:12:46**  how are you envisioning it because i think your kind of use case on how you would use that thing would help us in designing it properly one more thing sorry i didn't get that i can go a bit more into details with uh with like what type of revenue sharing what what different models you were thinking um just so that we get a use case and can consider that in designing it um on the technical end um i don't know ben maybe you know how we um looking at

**01:13:18**  this with the with the other service implementations but we would need some kind of a way to to have a meter how much volume or which kind of volume we're bringing to um we're bringing to the conjoint coordinator but we of course we don't want to like the core features of spectre is really your node your verification um your wallet infrastructure and everything so on your infrastructure which is your privacy and then your keys your coins and all that interoperable

**01:13:49**  and quite user-friendly so we cannot um we cannot um damage the privacy of our users there so it would be like we need to secure um like a proxy server going through one of our or through a server that we operate so uh i'm not technically enough to to to to expand on that too much i guess then maybe you know ben is out i guess

**01:14:24**  yeah maybe you all can go a bit more into the details of how wavisabi might fix that um i don't have any like concrete spec or anything but um i mean in the way that we model um like bitcoin mounts we're also modeling weight units right now in order to make sure that um like the transaction ends up being standard uh we could basically like figure out some way of having additional

**01:14:56**  ways of quote spending credentials on like specific uh things that are not outputs like you you register something that's a pseudo output essentially and instead of the server appending that to the transaction it keeps him sort of um auditable account of what you're spending this on right is it a donation to some service is it um a bounty for a bug that the coordinator is involved in or or something like that and i suppose

**01:15:27**  that different wallets could just come with these you know configured to by default you know donate some share of excess uh like the the suppressed change or maybe some percentage of e uh would go towards a specific you know entity um but ultimately like at the point where you hand off the money to the coordinator uh like that's kind of a big trust assumption so i think the coordinators need to or the coordinators and the

**01:15:58**  entities receiving the money need to be um like trusted to some extent um the advantage is if you can prove that you know payments were made uh like you could uh then correlate that to this like audit log and and say like here's the receipt uh the the money that you asked to go to like this bitcoin address or something eventually did make it to there okay so this is maybe somewhat of an affiliation system right where different people or projects

**01:16:29**  can get an affiliation code might even be something humanly readable right and then the user can put that into the wallet either himself or it's shipped by default in that integration so the user like registers that affiliation code and there needs to be um careful consideration of things like um fingerprinting through timing attacks like if you see that a certain unique soul cluster

**01:16:59**  uh happens to be uh or a suspected cluster happens to be used around a time where coin joint transactions auditably donate money to wikileaks or something uh you know uh there's potential circumstantial evidence that might not even be true but might you know be used uh in a sort of like surveillance capitalism type uh model uh of doing business so um like you need to consider those things as well um

**01:17:31**  yeah if the payouts are to be verifiable and transparent i think an initial proof of concept would probably be something like and this is way down the line but something like vote on your you know wasabi feature and if we make sure to do that um in a way that's privacy preserving uh then it's probably gonna be easier to generalize to um uh you know add another layer of auditability on top of that which is now involving like multiple

**01:18:02**  entities being paid by the same coordinator and maybe like multiple coordinators trusting each other to you know keep honest accounts okay that's interesting i also wonder about the legal consequences of this but i actually don't think that affiliation payouts are of any legal concern i mean sure you probably have to

**01:18:34**  like make some smart accounting for it or to get it above board but it seems this is just a standard business practice yeah the legal stuff is a little bit tricky we would have to check that i mean like yeah but as we don't operate the coordinator ourselves and we're just offering like a service integration so it's officially not our

**01:19:05**  our client to say so but there is no client in them that's it's tricky it's tricky we would have to discuss with with maybe some some legal guys there yeah but this is maybe one note where they feature requests that i hear from you um like to not need or to not carry the legal responsibility of running a coordinator and earning revenue from that um yeah so this is something that has to be considered to right that this is legally

**01:19:35**  solid and especially that there is no legal burden on the kind of affiliation users yeah yeah i mean everything is legally solid that is non-custodial in any jurisdiction right now yeah but you could argue that this affiliation payout is getting custodial because ck snacks gets the bitcoin onto their own chain address from the fees but then they oblige

**01:20:07**  themselves to forward that money to crypto advanced company right and in that meantime yeah it might be considered but again it's kind of like uh the user provided a uh like a coupon code an affiliation voucher and because of that either he gets a discount or some money gets bored uh i don't know i'm not a lawyer but uh yeah

**01:20:40**  yes you would would have probably to to set up some kind of company in the right jurisdiction also to to mitigate this tricky yeah but i mean the feature would be extremely useful if it would not require the receiving party of that money to need any legal setup like if this can just be an anonymous individual in cyberspace uh we don't care as long as somehow they're the users say that that guy should get some money

**01:21:17**  tricky tricky tricky i actually think framing it as an affiliation marketing scheme is an interesting idea i don't know actually shinobi i hear i see her on the call do you by any chance i have any thoughts on that and i see then gold wants to speak to how's it going then

**01:21:49**  it's going well max uh yeah i have a a pretty cool uh take on the sharing there regarding uh if it's custodial or not because i know the 2019 guidance from fincen exempts explicitly miners or minor pool operators from being money service businesses so it seems like it seems very similar in that if you're sharing earnings

**01:22:20**  then you're not a custodian i don't know if anyone else has read that or is familiar with that aha that's interesting it has some similarities still mining cool and it's not just for the like decentralized mining pools it straight up says um the person acting as the leader of the pool claims the total amount mined and receives fees from participants to be authenticated and

**01:22:51**  it says that this the cloud miner it calls them a cloud miner and they don't even need to be incorporated um i think yeah you can definitely draw parallels that's interesting thanks but yeah i will probably talk to this in length with some lawyers and see how it goes

**01:23:21**  but actually right maybe maybe let's go in some more interesting topics which would be yes please which would be the choice of lucas oh well well my point is what i would like to discuss is something that it bothers me with all the wallets it

**01:23:52**  bothers me with wasabi too of course is the the incompatibilities between wallets and also how to backup the wallets because you know if if i want if you what sorry if you have your wallet in i don't know um myself well probably you cannot recover it in in another wallet and you cannot recover your wasabi

**01:24:22**  wallet in mycelium and you cannot and it's a big mess right and also we have different wallets have different um metadata or extra information that wants to um store for example in wasabi we want a good yeah look we have probably some small pieces of information to say even

**01:24:53**  i don't know how the rest of the ecosystem is dealing with with this so it feels like yet coin wallets are so innovative today that standards we don't even have yet time to emerge yes and last week we or or the week before that we discussed why we are in the situation

**01:25:25**  where we are right now um and basically how this started with bitcoin core having the a pool of key pairs and then it was a vip 32 and then vip 39 and okay it works okay but it was designed in my opinion it was designed mostly for bitcoin call right and

**01:25:55**  all the derivation path and all the the thing for example i don't know the the change the chain code in vip 72 and all that stuff is it's all something that it was not in my opinion and it was probably designed without uh without knowing how the how other wallets can

**01:26:25**  um about the needs of the the rest of the the world it's probably because there were no other words right it makes sense but i don't know i think you know in lightning for example you have you if you back up something you need to back up also the channels in multi-section wallets you need to back up not only the one

**01:26:56**  pub key but you need to to back up the other pub keys too in order to be able to to re recalculate the the the thing that you see so it's it's a problem i think um there are a lot of other things for example just if we want for example to create a page on it right for of course we will

**01:27:27**  do it with uh with tor but other wallets doesn't work with thor and not it's a big mess so how do you how do you see this do you see something similar or it's just me and how are you working around the problem if you have the problem it's a mess output script descriptors solve a big chunk of it

**01:28:02**  so i'm saying we need another standard to collide all the standards so it's it's going to be an organic process right like if something becomes so good that every wallet wants to implement then then well every bullet is going to implement because the market is going to choose the customer the wallets those implement the stuff that they want

**01:28:32**  so i mean i guess in the internet i actually have no idea what happened but there was this opposition model right like that was supposed to be the standardized version of tcpip maybe and and you know like it didn't go that far so maybe just just let the market to take care of itself well but we are the market

**01:29:03**  like the choices we make for wasabi have meaningful impact and the outcome of this uh uh no no no because right now we are talking about standardizing we are not talking about like oh there is that other product like output descriptors which could make our wallet so much better uh now we are talking about well the output descriptor seems to become the standard or maybe not so

**01:29:34**  we should implement it because it might be a standard you know we we have to look at features not standards what problem does output descriptors purport to solve it gives you the an exact description literally a definition of under of both the script um so it gives you all the information you need to generate the script uh and it works for example also with

**01:30:04**  extended public keys so it you once defined the script and then you interchangeably add the expert from which the wallet can generate all the individual public keys and the addresses so it's like an extra peter and superstar gene yeah you basically end up with with the xbob and uh and the keypad and everything in one go right it's especially useful for multi-stick but you still end up losing you know all the essential data that you need to back

**01:30:35**  up with for lightning for example if that's one of the scenarios you want to back up uh any kind of metadata that you need so like if you're if you're handling like for wabi-sabi you've got logic around um how much how much depth you've had with your trend with your coin joints that's something quite important that you want to save right otherwise you're you're kind of in the dark afterwards if you recover on a different machine we just isn't there a gap limit field in output script descriptors

**01:31:07**  no there isn't they take this logic to its logical accent the logical extent is that the ultimate bitcoin standard is it's not xbox key it's not output descriptors it's not not output descriptors plus more information but it's like a standard bitcoin wallet file i'm more confused than when i asked the question it is it the problems that solve relate to

**01:31:37**  finding the script when do you lose the script this is like for recovery purposes it's usually best for like interacting with outside wallets and other wallets so that when the wallet you're working with sends something external it's it knows it's sending it to the right derivation path the right script type the right um x pub so that whatever external wallet it's going to wind up in the right place and it's also like importing keys to uh watch wallets and like that

**01:32:08**  a way to look at it is also that the openscript descriptors give you the deterministic backup right so this is the stuff they generate once a bullet generation and from there on out you can generate all the addresses it does not include dynamic backups of for example your labels who knows about the addresses or your lightning network channels and all these dynamic backups need to be done in a different way

**01:32:38**  okay thanks shinobi thanks max yes but again again imagine you have your you import right a couple of um output descriptors in your wallet right uh how do you back up that in fact uh now we have other 12 words or 24 words but an output descriptor right for a i don't know for one specific

**01:33:09**  script let's say uh there is no it was not designed to be let's say the wallet itself or or easy to back up or no it was just for interoperability basically so think of it like your x-pub like it's just another thing like your x-pub that you have to keep track of um like to pass around to the software wallets you're using right to answer the question that wasn't asked like what problem does an x-pub

**01:33:40**  solve it helps you connect a bunch of addresses together without keeping all of them i guess maybe the problem that output descriptor solves is it lets you do that but across multiple derivation paths yeah derivation paths script type like it's super multiple derivations like you could tell like you could tell it if i if i remember everything correctly like you could tell it to do like bec32 scripts on a totally different like

**01:34:11**  derivation path that's not standard for bec32 and a wallet compatible with that would just know like this is what i do so it's like it's like a more flexible equivalent of an x-pub that you plug into wallets to play with yeah but i'll go ahead and exports are only used basically in the context of keys in wallets right because most well most times we use just single six and multisig but actually what's happening is is that these are all scripts and so alpha script

**01:34:41**  descriptors contrarily to something like an expo is focused on displaying the actual script that was used uh in to lock up this bitcoin so that's that's why it's more flexible it can express any skirt type right yeah yeah it basically replaces xbob wipe off zip any other vip 32 spec yeah yeah and it's right and right and also multi six time blocks and like any anything that you can put into a spread basically

**01:35:12**  not exactly it's i think it's a subset of manuscript for example so i think manuscript is uh can do more stuff but yeah it can do a lot but i think that the the issue is that it's still not enough to do a universal bitcoin backup right you need so much more data like if you want to be efficient about it you need so much more data especially if you're handling privacy if you're handling coin joints all that data it's it's still a central part of it it's still an

**01:35:43**  essential part of a wallet that you need so an output descriptor by itself is still not enough it's only enough to save your funds but not enough to preserve essential data that you need stored for for most wallets i would guess yeah and the sad thing is that this this important information is always going to be dynamic and be created alongside with the wallet is being lived right so this is this is an issue i think that only live backups control encrypted on some

**01:36:14**  other server for example gosh well i mean honestly though it's also just as as flexible as output descriptors are it's probably a bad idea to use them to describe very non-standard stuff right now yeah at least so many scriptures more along

**01:36:45**  the way well but my point about interoperability was mostly because you know everybody is creating their own technology and and some people just don't stop and probably they are right but they don't stop to to to share the idea how to create a vip they just write the the implementation and we end with this kind of for example

**01:37:16**  white path feedback teapot and all that kind of crap and and people using a completely um non-standard derivation paths and it's a huge mess and that's only for the keys right i mean for the key derivation algorithm and just imagine the rest i mean when you want to to save something else i i don't

**01:37:47**  know what but it's it's completely uh uh a problem and now yeah we have output descriptor but in my opinion it is for for communication mostly it's not something that you want to to use for for backing up your your your wallet the best way is to steal something like the vip 39 and save your backup your words in in paper

**01:38:18**  or who knows but uh well i mean yes to an extent right if you want to back up in meat space then recovery words are the best ux you're gonna get but i mean maybe we can transform an output script descriptor into humanly readable words right i mean that should just be an encoding issue um but yeah also if like if you want to do digital backups in cyberspace then the output script descriptor makes sense again also like it's why like we we shouldn't be conflating the word seed

**01:38:50**  with the output descriptor i mean that's like conflating your private key backups with the x pub like those can be completely independent things and like output descriptors are not trying to replace your words they're trying to replace the x pub and that public data that doesn't put your money at risk and like really things like this are absolutely necessary to bridge those gaps of everybody doing their own thing and being incompatible like everyone with their their own derivation paths their own schemes output descriptors are

**01:39:23**  a way that you can bridge those together so they actually work properly well i mean is it is it actually correct because you can actually store an expert inside the output descriptors as far as i remember that is a horrible idea who the put that in that spec no why it's useful too i disagree i'm bombing out before i start yelling shinobi i'm gonna ask you to please not say stuff is good or bad without explaining why it's not helpful

**01:39:54**  it's so confusing this is the second time what do you mean i don't think that why is it bad of a key set should be made and transferred around digitally if you're doing that it should be done analog and it should be transported between different security devices i am not on board with the idea of making multiple copies of private keys and transferring them around digitally on network devices i think that's a horrible idea i think it depends on the scope like you're looking at i mean from my point

**01:40:25**  of view it's like if i'm creating a wallet that's going to have a hot wallet in it wouldn't it be nice if i only have one config one configuration item that i'm just sitting with all the data you need to create the the derivation scheme the pathway and uh private key that's you know allocated to just this one xbox in one go no i think that you should have everything but the private key and you should have to pull that word seat out and punch that in like i i do not like the idea of private keys flying around

**01:40:55**  to the winds so guys um i started documenting um some of these uh wallet configuration files i think most of you guys who are on there spectre wasabi wallet um i also have electrum um i wrote up the just some typescript definitions and um and outputted some json schema i don't know if you guys are familiar with that um the reason for that it was to like

**01:41:25**  look into this uh problem of like what are similar within the wallet and um uh in terms of like the yeah the data that they're storing um uh uh unspent um unspent uh uh transaction outputs um a list of transactions or some of them um uh private keys etc etc uh so there's like two categories there's application specific

**01:41:57**  uh configurations right like app settings and stuff and then there's like the things that are a bit more portable um like the um utxos with the labels and and whatnot um so yeah i just wanted to add i sent some links earlier in the chat as well if you'd like to have a look at it just to see what uh just to compare um

**01:42:46**  well in traditional shinobi fashion since i slept in um if there's nothing else anyone has to say for the minute anyone feel like catching you up in five seconds to what i missed ptcp is plugin with wabi-sabi and spectre i rpc server integration or spectre might use rpc server and wasabi

**01:43:17**  okay so you're talking about bolting wasabi i mean spectre on the wasabi onto btc pay yeah more like getting wabi-sabi inside these wallets okay so yeah okay so other wallets hooking up to the wasabi api not even just that i think from the btc pay side in terms of potential is more like embedding wasabi inside btc like it would be running in process

**01:43:48**  okay so there's two separate topics the api plug-in and then embedding and i think the third topic that we have uh is dan gould with gen case which just is basically like a wasabi fork that wraps it for ios so that's maybe dan could speak a bit about that approach sure yeah the main piece of work that had to be done to have that happen is make

**01:44:19**  wasabi wallet a library that could be pulled instead of uh a whole run time i forget who was talking about it earlier maybe maybe as moritz was asking if there's an api available for wabi-sabi and the main issue with getting coinjoin functionality into a wallet is that you have to do all the crypto you have to have the client for the protocol on the device so we turn that into a library and then from there of course there are issues um

**01:44:51**  like tor integration uh making sure that sock server works and getting neutrino to function in the constraints of the device but that's basically where we're at we had a release last week that reduced our instability by 90 so i'm feeling good in general about the direction and definitely open to questions people have um we want to implement page join at some point too

**01:45:23**  is that interesting thing there is that you can have the ephemeral hidden service available on your mobile device um which is open like while you talk to someone else even in the background not all the time so it'd be totally like you you can have it in the background to some extent like if you went and send a message to someone to send them your hidden service address at that time you could have it running in the background but it wouldn't be something you'd want open all the time i don't think

**01:45:53**  so did you guys just refactor the c sharp code base into the library or did you like completely rewrite it in something for ios like sorry i'm not really too familiar with it yeah it's it's refactored it like we've got the same uh tests we ripped hwi out for simplicity for now but it's the same c-sharp library and we put a different front-end and different uh application lifecycle management to work with the operating

**01:46:23**  system okay so that should be generally portable to any system yeah it's forked from i believe the 1.1.11 so the last major release of wasabi all right so that sounds like a great starting point for ripping apart and putting in other things yeah i mean it works we've been operating since june and

**01:46:54**  some people are fanatics happy to get more people on board i think you'd be pleasantly surprised and the ui is coming quite quickly along yeah i mean i was just excited to see you guys fork it period and see somebody besides wasabi running a coordinator yeah anyone can access that as well it's the 100th of a bitcoin denomination rather

**01:47:26**  than a 10th that's posted on our github hopefully we'll have a demo of the whole app and video rather than just the coinjoin portion uh sometime soon and i think it'll make more sense when that comes around yeah it's kind of it's kind of interesting the fun part from mayan is i get to run the ios stuff and hack it into a browser app from mine i don't think you're very happy with that one though then

**01:47:57**  i wonder what's like i wonder if you could connect it to tor and get it to work as an alternate to metamask you know if you had a complete privacy wallet in your browser in lieu of metamask i don't know how i guess syncing with the network would also be difficult um i don't know could you have a gig of data that you store in browser i don't see why not i mean right now so okay so running it there's a bit of a

**01:48:28**  difference here you're still having the server running on your computer like that like the like a web server so i i'm not running it it's running in blazer but it's not running the web assembly version so it's not completely embedded into the browser um uh yeah we could we could run it into a web assembly thing uh i think in the future i think there's some crypto missing from from the dotnet tree libraries i think dot net six will fix that all and make it work properly

**01:48:59**  with no modifications theory at least there are like eight asterisks after that statement yeah yeah so right right now it's completely hacked into place so that it can run in the browser just for easier testing and prototyping but it is saving it is synchronizing the blockchain true neutrino and saving it to to the update on my on my windows machine i'm pretty sure it works on linux too

**01:49:30**  and i also kind of hacked it around at one point i did manage to get it running on android but that wasn't the most optimal performance to say that like everything was crashing all around me on that one um but yeah you actually got wasabi running in a browser not not really the ui was running yes yeah what do you mean it definitely runs yeah yeah yes

**01:50:00**  yeah yeah terms and conditions apply but yeah it does it does run and to be fair i i really doubt we could make it run into like this fake metal mask wasabi crazy thing in the in like a little tap thingy next to your address bar that would be i don't know i i feel stressed just thinking about that so that might be far-fetched but even on ios we are running wasabi

**01:50:34**  essentially in the browser like basically we have a hybrid web app and that's what's happening pretty much yeah it's running blazer it's running a blazer ui so um and everything is running to a net core is it.net core or or mono and it's mono so it's xamarin yeah yeah i don't know how that's everything is really in flux in this like stack i think dot net six is gonna push stuff around quite a lot

**01:51:05**  yeah hopefully for the better i mean could we potentially have a desktop client and a browser client that use like the uh that use the same app directory basically for sure the the browser one is actually running in uh it's saving the some of the data inside an app data

**01:51:36**  slash chain case folder um i'm guessing technically wasabi could kind of read the same folder data i think it's the same right then i i don't think it's completely different in that regard yeah all the caveats are around just using the operating system it doesn't use tor right now the one we have on the browser does not install or use tor that's like one big issue but um as far as just

**01:52:07**  saving a json file yeah it can read the same uh it can read the same blocks files and wallet files and all that index i mean i mean the tour part is not that hard to do is just run the docker container next to next to it and just point the sox5 client to to it at that point right or we could just embed it into the server if we really wanted to but yeah yeah it's not the point of chaincase at this anyway so

**01:52:37**  uh the the main reason why why it's running in a in the browser is just for faster prototyping just so you don't have to wait for the app to load on your phone and then you have to try it out and then you reload it and all that stuff right we got hot reload in there through the browser yeah that too nice i got um uh protector is able to run in the browser as well right um at least the development environment but how much of the um

**01:53:08**  yeah uh oh yeah how much of the rest of it can run in the browser and is that like something that people would want to do even i mean in general it might be interesting to connect to a remote machine via the browser i'm not i'm not sure is that in scope for this discussion or is that a different model so so the browser is just for like uh

**01:53:40**  connecting to something like the remote server or whatever yeah like write the lightning or thunderhop or something but that's something different right it's just the browser web interface but the actual stuff is running on the server what you're talking about is that the actual software is in the browser itself no no i was asking like uh to what degree does it like kind of start and stop um because i did get spectre um because yes spector's uh ui is also uh written in like

**01:54:11**  html um so the development environment um you can like if you spin it up it uh it opens up a browser page and you can access it um i just don't know how much of the like back-end functions it's able to do in that version of it but um i think more it's just gone i didn't see them so you'd probably be the one to answer it or then ben is still here yes yeah can you repeat the question

**01:54:44**  yeah so i got um spectre to run the development environment in the browser but i was just looking at the configuration page um i didn't like interact with like try to set up a wallet or anything like this so it's just asking since everyone's on this topic of you know um while it's running in the browser uh to what degree can spectre run right now in the browser uh so with the browser i mean it's

**01:55:14**  everything runs in the browser so it's it's basically inspector is a flask app so um yeah everything is on the on the um on the front and side everything is you know javascript html stuff on the back end it's it's python and uh this allows us to to use um some more advanced stuff i guess uh because yeah thor running tour and stuff like that would uh i'm not sure it would be possible

**01:55:45**  from from the browser itself i don't think so um but yeah so so the the browser code is it's more for the ui i guess do people um request having this like like i said a request for wasabi or spectre or uh chain case whatever is there like a demand for having these browser-based wallets um because like given the security um risks of it as well if you have

**01:56:16**  extensions you know spying on the page and whatnot um but is there a demand for it i know people who operate with hundreds of millions of dollars in ethereum tokens in the browser so people really people really like using uh browser extension wallets random idea if something goes into the browser browser that people are using for a web page maybe that thing should only get a child

**01:56:46**  bip 85 key and it shouldn't be allowed to touch the other keys more generally like so what does a wallet do i think it has like three layers of um usage one of them is like this is what wallets specialize in so either you'd have something specific to do with the blockchain layer like wasabi does or you have something that's um

**01:57:18**  like lightning notes that's another example of something that's you know specifically about the bitcoin protocol but also extends to uh smart contracts so you're doing some application specific script um bisque uses that as well and then the third layer of kind of you know wallet responsibilities are managing like allowing you to spread your credentials and physical space in a way that's actually secure follow some local policy and ideally in

**01:57:50**  the future those three layers should be completely independent like you should be able to compose your multisig policy that you uh i don't know define with your business partners or something uh including say a harder wallet like whatever um you should be able to compose that with an application layer so something like you know bisque that actually needs to uh make specific outputs of specific contracts and you should be able to compose that with a blockchain layer wallet that manages for example network

**01:58:20**  level privacy and in general helps to move funds between um like actual uh sets of credentials like allocate which you utxos are spendable by which uh specific uh uh policy keys mm-hmm because it's like yeah the it's like the like what you just said then just blew my mind like that is horrifying like segregate keys that touch a real browser

**01:58:54**  uh yeah i agree it's just like people go for the easiest experience you know if they can end three clicks from watching a youtube video install uh you know infrastructure for their business they'll do it that just that blows my mind like that like uh like i just cannot wrap my head around that when i bought my first bitcoin i got the shield block wallet on an android tablet

**01:59:26**  sent the coins there and then immediately put it in airplane mode turn it off and let the charge died and just left them there for like six months because it's like holy everything can steal these where do i put these yeah i do i i don't know if it's gonna change or or not i think people will get wiser to segregating keys but at the same time if we have more people on board more people

**01:59:56**  are going to use solutions that exist in the browser it's hard to say it's definitely not what i want to build right now right i don't think it's the most secure environment so i don't think it's the best way to spend resources so i was hoping one project this weekend on the fomo hackathon and it's a lightning browser extension similar to lightning jewel and the idea there is that um yeah you

**02:00:27**  load in some macaroons and um uh connect to your node and then you're able to pay for content on the web using um this extension with like prompts and you can set allowances and and whatnot but this one relies on um connecting to a uh and authenticating to like a remote node right um versus like crypto stuff happening in the browser

**02:00:58**  but i guess like the authentication i guess the authentication tokens can still be um or the macarons can still be like hijacked but perhaps you can i'm not too sure about like um the extent of like permissions you can do in lightning but maybe there's some kind of like rate limiting or something um that you can set on the macaroon permissions at the very least so macaroons support what's called caveats where you can add

**02:01:28**  additional restrictions in uh like object capability lingo uh that would be called attenuating the capability so you can like if you have a macaroon you know how to produce valid macaroons with additional constraints so you can create another one that says like this expires and the default for the lightning command line utility is to uh only transmit tokens that expire immediately but i mean you can apply the same kind of approach to limiting the macro and so you can figure into a

**02:01:58**  client and say have it expire in a day or something can we do by amount i don't know if lightning supports that specifically like lnd um it's definitely possible in principle with macaroons like you could invent caveats for literally anything you could you know get very fine-grained with the actual permissions like you could have a specific endpoint like template or something like that to only allow a single use of a token to

**02:02:31**  make a specific payment or something like that like in principle the object capability model is like very well suited for this kind of um restriction of access rights in a way that allows validation between bits of software i like to use object capabilities yeah i mean as long as you can rate limit that in the sense where a user can go to the real mode and stop things like that's infinitely better than just putting keys

**02:03:02**  in a browser well in principle i mean you would want to just have different like the web wallet its job is to integrate spending into your browsing experience right its job is not necessarily to manage uh node state or key material or anything it's just responsible for saying what should be done right what what transactions need or what dxos need to come into existence

**02:03:32**  for my function to have been fulfilled and they can delegate that behavior to a lower level wallet that actually manages um right like the the policies like what sort of uh utxo selection are you doing or you know um i i think that's where the a lot of the friction and like interoperability exists like that there's no coherent separation between layers of like responsibilities for different wallets and then every wallet ends up

**02:04:03**  specializing in its own layer and kind of neglects the other responsibilities of what an idealized kind of wallet could be would you be able to to do something like um set that a plugin up like that that macaroon authenticated to a node on the same machine but then instead of handling everything through that literally just use a uri request from the plugin to bring up the

**02:04:35**  actual wallet and authorize it there in like a smooth flow in that case you probably wouldn't need permissions and stuff if it's in the url right yeah but i'm just thinking in terms of like at least you have to [Music] you know screw with the plug-in um before it'll just start spamming uri requests that you you know i mean i don't so at what point in the process is a urine

**02:05:06**  introduced and who generates it and who queries it well i'm saying like you instead of like handling things through purely like macaroon authentication just go to the plug-in click like you the user actively clicks something and then that authenticate with the node and launch the uri if that authentication passes um well the whole point of doing it that other way so uh that would in the macaroon like flow that would kind of be like a third-party delegation

**02:05:38**  type thing uh so if you have a certain capability and and you can sign with a public key then you can uh say uh like i vouch for the bearer of this uh token uh and the back end server can kind of uh authenticate that and you know uh gate limit your uh your access or uh and for some uh caveats that the third party uh imposes on the on the token but like macaroons are basically like a cookie they're

**02:06:10**  something that you attach to an existing request so um like if you don't have the macaroon you would be redirected to some page potentially via such a uri where you would be able to obtain that through like a typical web flow um that's kind of what was uh uh described in the like the the paper introducing them i don't know what lightning supports that my only thinking and just have the authentication before launching the uri

**02:06:40**  um is so maybe you could just restrict uris like that and not have cheeky just launch like uri requests for opening lightning payments by default on pages everywhere or something you know i mean yeah i think that is like another big problem that we have which um like if you have wallets installed um uh they're all using the same name space um like yeah so they're kind of like competing and like okay so you would just have

**02:07:12**  like five lightning wallets open if you had a bunch installed well like on mobile it just chooses i think like the first one that you installed so if you installed like a like a wallet for testing like years ago it'll like open this one when you open the bitcoin uri um but and then on desktop it's like maybe you can configure that somehow i'm not exactly sure but um like how it's designed in the operating system currently it's that the uri is for like one specific like

**02:07:44**  uh applications right like facebook or something facebook has to have their own uri or whatever it would just be like opening the facebook app or something it wasn't like really designed for like something as opened i've like open i feel as as as um as bitcoin surely that would be solvable using a simple app that just knows how to recognize the various bit 21 things and delegate them to like default like a wallet picker kind of

**02:08:17**  like that doesn't sound like an app that's too difficult to develop right yeah that could be like a like a little middle ground until the operating system kind of evolves a bit more um yeah someone said like the same behavior as default browser um yeah the thing is it's like uh currently we use so many different wallets um you know i have like i don't know five ten i'm testing a whole bunch so um having to set like which one is default i have no idea which one is default for

**02:08:47**  me i just like use whichever has like some fun cinematics and um uh so i kind of like would like to switch between them or have the option to like hey which one do you want to open um maybe in the future i guess that's default bullet and the right click will open with yeah to open yeah that's uh yeah but you know like when you check like like if you click a link on a on on a website you know then i'll have to

**02:09:19**  maybe okay maybe that can actually be mocked up in javascript or something um when you right click on a the 21 uri or lightning uri it's gonna say uh i'd like in the context menu open with oh no i'm not sure okay because you need access to the operating system so okay maybe not i think the application switcher route is probably the easier one to go to

**02:09:54**  yay guys bitcoin is gonna eat the world tomorrow it's perfect in two weeks time oh man well i guess anybody mind a little bit of a random topic shift nope um in terms of plugging other wallets on top of wasabi instead of integrating wasabi into other things has anybody

**02:10:24**  really considered the limitations of the neutrino filters being tailored just for bec32 because that would kind of have the implication of any other type script or script type cannot use wasabi as the balance information back end and would require a second one to be able to utilize any of those uh utxos yep that's an issue i think that's only really an issue if you want the network layer to deliver your block filters um

**02:10:57**  there's the proposal from juices uh i forget sorry ravner um the uh the bip 47 guy yeah so uh like that proposal for how to do like filtering of uh transaction data is actually like really nice it's really flexible um and uh there's good reasons to to kind of support that because that would solve this problem in general um

**02:11:28**  like that that said wasabi currently just fetches block filters from the coordinator so it doesn't even care about the network that could get block filters for you know any type of proprietary uh data so like filtering by script type by transaction by like literally anything um could be defined when when you use it that way and for what it's worth lucas already wrote the code for taco filters okay well yeah i mean that's that's good if that's a simple thing and there's

**02:11:59**  already some groundwork for it but it's just like that's like absolutely necessary to be able to just take general wallets and plug them in here what about is it possible to to switch out the entire network layer with something else like in in the case of putting wasabi inside b2cp we have our own tracker right so we wouldn't need neutrino we have a full

**02:12:30**  node and we have our own whole utxo and block retrieval mechanism that we could use yeah that would be best um what adam can probably say more but i think currently like the wallet synchronizer class is responsible for that i don't know how generic it is but um like there's a lot of consideration uh under that for like how you fetch specific data so like does end bitcoin

**02:13:02**  uh is it also careful to like obtain blocks from tor nodes or sorry nodes connected through tor uh in in uh like and careful not to um request the same like the block data from the node where you know filter data was requested from i mean sorry it doesn't have filter support but like um it's careful about broadcast and it's careful about uh block requests is my point so it's it's it's not it's not on top of

**02:13:32**  my hand how hard it is how hard this would be from an implementation point of view but but from a theoretical point of view this doesn't this doesn't apply to cool node full nodes right like btc or spectrum what it's these concerns are more like light wallets right well i mean i think what andrew's kind of getting at is if you just stuck with the current like uh

**02:14:04**  balance retrieval mechanism in wasabi then that would just eat up a bunch of resources on the btc pay instance and like what there's no good reason for that when it could just hook up more directly into that and use less resources yeah it also if i'm not mistaken has some like uh smart support for uh pruned nodes right where you can fetch historical blocks if you're still missing them or am i misremembering uh we talked about that you it was uh i

**02:14:36**  think we talked about it we suggested it but i don't think we added support to fetch specific blocks but we do have a bunch of stuff basically so nb explorer is hooking up to uh to a bitcoin node uh which can be pruned and then it can scan stuff through it but it also does a p2p communication layer so i think it does do something that i can't remember actually if it does it does a lot of fancy sorry so sorry wait a moment the point of this

**02:15:08**  would be to not even build the filters right yeah exactly yeah i mean if there's anything you need to track mbxplorer can track it in advance with no issue yes no just that if you have your own node and you trust on your nodes in end bitcoin there is a pull request that contains all the messages i mean for implementing the vip um

**02:15:41**  157 i think right and all the communication is is it's okay you can just fetch the filters from your own node and you don't need to validate them right because you know and wasabi will will find if if the blocks that it needs and whatsapp can also be configured to fetch the blocks from your nodes so you don't need to build the the filters and you don't need to do

**02:16:13**  anything it's it's mostly done the the pull request is not merged because basically uh you know the specification says that you have to first download all the vlog headers and then once you have that fetch filter from different sources and validate them and all that stuff and i i didn't know how to how the end bitcoin

**02:16:46**  and i didn't understand how and bitcoin works in regard of those things but all the rest is is is all done okay uh i'm just also curious if we need to to handle filters right i mean you it because the way the way in bit and the explorer is doing it is basically you tell us track and xbop um track that tracking address track

**02:17:18**  whatever and it will as soon as it detects them any any transfers to them in any blocks or the memphis it will keep uh um it will take uh it will download that data and store it locally permanently it doesn't matter if the pro note would remove it so basically we have all the data we need permanently for these kind of things as long as we tell it in advance look for them the abstractions at least in the v11 release are still pretty leaky like the wasabi client that synchronizes

**02:17:50**  the um the coordinator with the the app i believe does require some knowledge about the filters it doesn't just ask about transactions i don't know if that changed to 12 or if i'm looking at the wrong thing but i think that's how it works right now because i know the synchronizer takes care of getting the coin joined data as well as the filter data and i don't know if they're totally separated no i mean it's it's not it's not

**02:18:22**  done because it's not part of our use use cases but wasabi works with transactions right i mean if you connect wasabi to your now and you just or node or software whatever using the peer-to-peer network and you send transactions to wasabi it will processes and so it doesn't need to to to get blocks and get filters and get you just

**02:18:53**  if you know all the your transactions you can send the transactions to wasabi and whatsapp will process it and and and calculate everything the balance and all the stuff and so basically we discover the the we get the filters to discover the blocks to get the transactions basically but if you already have the transactions and well of course we need to disable the synchronizer right because yeah

**02:19:24**  the synchronizer is the one that tries to do that that thing so you just send the transactions to the to the wasabi mempool and that's all okay cool yeah that's that would be nice i think i think it would save a lot of effort at least on the b2c place at least memory wise right and there's no it's already doing all the hard work underneath no point in replicating it twice in the service cool

**02:19:54**  yep uh just curious but what about ending support for electron servers then like in in wasabi directly well i mean maybe i think the other way you know i mean you could expose enemy explorer as um an electromagnet point and serve like electrum like just like um electron

**02:20:26**  personal server or a bitcoin wallet tracker uh well yeah my idea is more like if someone is already running an electrum server we might as well use that right like it's about running on the trusted node and most people who run a node also have an electron server so that and they don't have nba exploit right only bdc-based service users use that so so you're saying wasabi would support

**02:20:59**  loading plot uh blocks and transactions through electrum instead of uh neutrino or maybe a misunderstood yeah basically it's an open feature i think it's a slippery slope to be honest when you as soon as you add electron support people are gonna be like ah i don't need to run a node and then they're like just screwing it up well you could just set that up

**02:21:31**  so that it won't call anything but localhost for that and kind of force people to go tweak with the code no one will ever go full guys i promise i don't believe you [Laughter]

**02:22:03**  honestly though i do kind of agree with andrew that just seems like that would lead to user stupid the other direction does kind of make sense though if you're already using like nba explorer and you want to use electrum or a wallet that queries it like um i think the async client uses that um like it might make sense to to allow uh like serve those requests off of your own

**02:22:35**  node uh that's already running nba explorer instead of yeah i mean we already host software in uh in the docker installer for btc pay to know what it was i think it i think we have electron personal server electromax um bwt i think is almost there as well so there's so many options to do it as well i think nicholas actually wanted to add like an elect an electrum compatibility

**02:23:06**  layer but in the end it was like there's so many people doing it already maybe it's not worth it yeah that makes sense

**02:23:46**  this is going to be your new mumbles here for shinobi never jitsie will never replace mumble well but basically you know i was asking about the compatibility and

**02:24:16**  interoperability and ux and uh if i wanted to know if you know about if finally page join is something useful or just uh i said something like a developer's brain masturbation or things like that because it's basically what she never said you speak one day with a bitcoin core developer next day with a cryptographer then with that

**02:24:46**  mathematician then we have office and someone that knows about nuclear physics and people doesn't know anything about that in fact there are people who who are victims of of the most ridiculous scams every day so people is much much much much stupid that what you can even imagine and then the idea that we have to do something that is really really easy to do really

**02:25:17**  easy to to to switch from one wallet to another wallet and privacy has to be by default in our case because otherwise i think it's really hard to to to explain people how to use these tools and well maybe that like pay joins specifically like that can be very useful if you're doing a decent amount of volume on chain and

**02:25:48**  like transacting a lot um like you know the reason i haven't implemented that for my shirt store is really two reasons um one i don't wanna have the on chain wallet with hot keys um because we're also running a lightning node but two like so much more of our payments come in over lightning that we're not doing enough volume on chain to make pay joint make sense you know what i mean after a couple pay joins like everything just tied together

**02:26:20**  in a way that's obviously like this is all related and there's not enough separate utxos to kind of isolate and optimize that so it's like page joint can be very useful if you're actually transacting on chain a lot but if you're barely touching chain then you know what i mean yeah and um you mentioned like building tools you know people are stupid those are keywords that i pulled out there um i think the state that we're in right

**02:26:52**  now you know working on this pay joint thing or coin join and all these different components where we are building tools and for the mass market it's uh experiences that we have to move into right so like these kinds of like interactions with pay joints and figuring that out and creating the libraries and whatnot it's you know a lot of it hasn't been done yet um so it's not a easy drop in that you can put in any kind of application so that we can like have really cool ux that

**02:27:24**  makes sense to the user um that's familiar with them uh to them so we are still at the stage where we're building out the tools and just as you said i don't think it's it's a matter of the users being too stupid to use them because we are kind of building tools for ourselves um or people that are a bit technical so i think we have to have a bit of empathy um in that uh the tools that we're building is not for um the mass market you know we need a new

**02:27:56**  class of software and design for that well i mean dude this is like this is just really super long-term stuff in my mind i mean like transacting is it needs to lift off chain um which completely changes the dynamics of privacy um like with lightning in a proper state so that you just have passive privacy for regular payments and then these types of coin join mechanics are just going to be how those things touch chain

**02:28:27**  but like you know what i mean like we're not gonna really be able to put this kind of stuff in grandma's hands until that's the state of things and a lot of logic can be automated because like right now on chain like i'm sorry you can't just automate the logic in a software wallet like i bought drugs on the dark net market with this utxo don't ever tie that to this utxo like

**02:28:58**  you can't just automate that without requiring the user having to program themselves like all kinds of complex logic into utxo labels in a way where the software can reason about that like you can't like a wallet can't just look at utxos without the user programming and defining and deciding what can tie together and what can't like how to handle those utxos the wallet doesn't understand any of that

**02:29:28**  unless you make it yeah and as soon as we go to another application pulling that output descriptor x ball that we put that in then all those labels are gone and then you call the user stupid for um not uh for for spending that drug tainted utxo it's like oh well it's your fault and you should have labeled your utxos it's like well i did before but infrastructure didn't allow me to easily you know migrate to another wallet

**02:30:00**  i mean this could also go down to uh how like a label server right i think electrum has been doing it for a few i don't even know if it was an official electron plugin but there was an electron label server which allows you to synchronize labels on utxos and transactions between your electron wallets across machines right i don't know if that's even still in use yeah and i would guess it's pretty similar to what lightning bullets

**02:30:30**  currently used with encrypted channel backups and you just encrypt the this backup information to your 24 words and then upload it to whatever server you want is while it's encrypted yeah i found what uh shinobi said earlier today quite funny because um uh like uh yeah never copy your private keys and stuff like that and you know um when we do look at like the mainstream

**02:31:01**  user and stuff uh how much would like it's it's a great ux uh innovation that came out the mnemonics and stuff but is that where it ends um we had wallet data files and you know um then we had like if 32 or whatever and then um and then you know now we have output descriptors but like is that where it's going to end um i don't think so and does it also

**02:31:33**  end with the user having to like interact with these weird symbol pieces of code looking things i probably not right so the way i look at it long term is your seed is going to be the bedrock that you use to encrypt and back up all the stateful information that you're going to need in the long term yep except the account and the path and all those other things that you're going to

**02:32:04**  need so no no you can still no i think what your nobody means is that you take all the metadata that is nonlinear or that is non-static or non-deterministic but that is dynamic like labels like channel backup transactions and all that stuff you encrypt that payload with your 24 recovery words and then you have some ciphertext that you can upload to arbitrary servers securely but you can always recover it if you have only your 24 words by two you get even if you have only the 24 words you

**02:32:36**  get at least your private keys if you have 24 words and that encrypted payload you also get all the metadata well yeah that sounds that sounds fair um yeah by the way um with like previously said about labels and output descriptors so um a while ago i was suggesting um this was before app scripters so some of the details were like still

**02:33:06**  you know kind of open but up script or solve that but like if you have a privacy specialized wallet that's a wallet that in in principle you could configure any sort of standard or application wallet to send all of its change instead of to its own seed from its own hot wallet send it to the external like output descriptor for the privacy wallet and then a privacy wallet would be in charge of basically rebalancing everything uh point pointing making sure there's

**02:33:37**  separation producing utxos that are then you know already set up to go back to the individual spending wallets that you need in order to like perform your various operations in your various application specific wallets um so like if you structure it this way then you you're never spending any coins that have labels associated with them that's the responsibility of the privacy wallet to make sure that

**02:34:09**  like the hot wallets of the various other wallets only have access to coins that they can spend safely regardless of their um you know coin selection policy and if all that from those transactions always cycles back to the privacy wallet uh then you can make sure that like there's no uh like no no potentiality of um accidentally uh violating this uh invariant by spending uh change along

**02:34:40**  with a different output or a scenario to change outputs together so the individual wallet transactions for you know bisque or whatever could be completely disjoint on chain yeah that's for sure the goal and that's again why i really like the idea of having a server-side wasabi demon running in the background for always on mixing

**02:35:11**  and you can just deposit your change coins or you're receiving clients directly in there and after anon said it reached it just gets distributed at a certain percentage into your cold storage and spending molds that's the feature request the size of a boat oh go shovel

**02:35:44**  just gonna randomly say that this kind of different wallet management it just screams 85. which one is that 85 the deterministic seed generation from a master seed so like you go down the derivation path and get a new uh word seed that can never retrace to the master one

**02:36:14**  i mean do you really need that level of complexity you don't really need that you can just use different accounts on on one seed right the nice thing is have your master cold storage seed and then generate all the other seeds for all the other specific stuff you're using off of that and just keep that one thing safe to back up them all is there anything that implements it currently just the cold card

**02:36:48**  but the nice thing is that this composes with bip 32 like accounts very cleanly um i mean you can just configure uh x pubs or uh you know experts or use bip 39 like you just need to keep track of what you've been doing so that you don't uh you know you know how it's set up um but like as far as i know like every wallet that supports bip 39 is a bit 85 compatible

**02:37:19**  already right yep you just generate the child word seed from the master one and just plop it into something what if what if you if you had to just go with a with the account routes where you just generate xbox based on the scenario you just and you just um categorize them by like you know you said the first hundreds xbob accounts to being you know like low privacy like

**02:37:50**  instant doxxing uh level of privacy on those first hundred accounts anything in the next two hundred as um uh privacy focused and you know so forth you just categorize it by the hundreds and then you can just do a spec based on that like anything in these levels of accounts can be kind of safe to use and anything inside it like if you had to create categories just based on xbox you'd have like 100 accounts to use

**02:38:21**  just with separate wallets kind of entirely separate wallets but it's it's not as generally flexible for users like you know i mean i can have my cold storage seed make a new one plug that into wasabi and use that to make like three more and like i can always just at any point in that tree take that key go easily import that with no headache or anything into almost any wallet and that compromises nothing above it in

**02:38:51**  the tree it's universally compatible i don't have to worry about nonsense like a count levels and i can structure that tree however i want because it's just toss a seed in something and that can always just make more seeds that would make the deplete a laughing a laughing situation with it recovery why i mean you could just limit yourself to like the tree of seeds and only make ten

**02:39:24**  child seeds or something off of one seed like so you're just it's a child seed from one to ten czech stuff you're expecting the user to do this so like what if i put put that seed inside of like another wallet and then that wallet things it's now the um the master seed and then i started driving um a bunch of different uh new seeds and i don't know it seems difficult how do you keep track of

**02:39:55**  it i haven't read respect for a bit 85 but i mean how is it more difficult than keeping track of accounts and like assign canonical numbers to it's literally the same thing as an account except you get a whole word seed out of it it's derivation path index number for that path spit out a new seed yes the exact same indexing logic um no but for the new seed that you create you could then i'm assuming create

**02:40:25**  additional seeds for that like how do you stop there you don't it's an infinite tree exactly yeah so it's just a hierarchical deterministic wallet that has x-pops and experts but this is just a spec to get each x-proof into its own unique set of 24 words that's that's it so all it is is just it's easier to import into stuff yeah yeah for certain like i like it a lot i just think the like and user can get like

**02:40:57**  really lost because um yeah maybe they wouldn't export like import like a um a grand child of an expert or something you know but in the in the case of like 50 micron between something like that i mean like think about why like you're you're acting like in the infinity of indexing space is a problem that exists for everything in hd wallets everywhere like why would a user make a great great

**02:41:27**  great great great great grandchild instead of just one thing and a bunch of children like you know what i mean like i i don't see the fundamental difference here in like a user could get lost in that yeah i like again i really like it because uh one seemed to rule them all with kind of fun here but um i think if like if to another wallet it's just a normal master seed even

**02:41:59**  though it's a chicken um one of the downsides specifically for privacy is that if the master private key or even public key gets compromised it's like the nuclear option where everything is clustered and this kind of stands in harsh contrast to key rotation where you get a new completely new wallet that is not linked to the previous deterministic orbit yeah but you know ideally you're doing this off of a cold storage seed that's

**02:42:31**  never going to touch anything so that's never going to be compromised so all you're really worrying about is the compromise of child speeds which can't compromise anything above them yeah that's true and you wouldn't even put the master x-pop in any software wallet i presume you would just always take the child expo i imagine the typical use case is somebody starts using some wallets backs up seats gets fed up with making more seed backups

**02:43:02**  and then says how about i use my brand new cold card to just make a bunch of new seats for all of these wallets to back up one so i think it's not really something that like users that are not already pushing it are going to even know exists or care that exists um and therefore it would be more like uh you know it's for managing your your backup policy more than it is managing like how applications interact

**02:43:34**  it's more about like segregating them whereas like the 32 paths are you know that's for wallets that need to transact together on the same stuff it's just a different use yeah case get that done because yeah that would be something that i would use personally just to you know not having to generate a whole bunch of seeds and keep backing them up all the time and even confidently i just have to do one of them um

**02:44:06**  it's also nice that i could give these private keys to my family easily either or two friends and they think that they actually have their own wallet in fact it's all controlled by me i get all the sets see like here's a wasabi case like in terms of bip 85 like you know part of the or one of the long term goals with wabi-sabi is to have like slower gradual rounds and like extend the signing process so people can just do coin joins

**02:44:37**  directly out of um like cold storage well um let's say that i want to mix a utxo a bunch of times and then spit it out into cold storage um but then maybe six months later i want to directly pull that out of cold storage and mix it a couple more times like you can just pop that child seed out of your hardware device and just make that your wasabi hot wallet and these two

**02:45:08**  things directly can interact with each other you only have that one backup like you know it that that's the huge win here like nothing much said it's just having that singular backup for something but you can still have all of these segregated wallets for different applications for different purposes like the nice thing is what we saw we will work with hardware wallets so you don't even have to move out of your cold storage into hot water what you described there though is like that's something you can do only once

**02:45:40**  per child seed though yeah look but i'm saying like you want to have like a mix wallet well hey that's a hot wallet if you want to have it mixing regularly just let it mix regularly pop it into cold storage like you you still have the same backup thing but both of those things can mix you know in their own timetables you can always go remix out of cold storage you can have that hot wallet that initially mixes things a bunch of times

**02:46:11**  but it's all in the same seat you know like that's the key point here you get the ability to have all these different wallets but your mind is not exploding over the giant pile of seed backups you have why not your mic is shitty

**02:46:41**  liar but you know like why not automate that in the same way that you use account to segregate things just automate using seeds for some things like if i have my cold storage and i make my wasabi hot wallet seed all i'm thinking is that one seed is wasabi if the wasabi client breaks that down into a couple child seeds instead of accounts to segregate their that makes zero difference to me in the back end but if for any reason

**02:47:13**  like down the line i want to take some subset of stuff in wasabi and use it with something else like bam spit that out word seed universally like works with everything but that that's irrelevant to me unless i need to do that it's just something happening under the hood and it's all nested under a single backup i guess um what that can because like the current state is that most

**02:47:43**  applications use like account zero right um so i guess what that can do is um the change could be going to like the account zero of that new seed um [Music] uh and then um in the scenario i think that uh nothing much was talking about you can then take that like it's it's it's kind of separate now from the main seed so you can yeah you have a more clear separation of

**02:48:15**  shinobi was saying between like the utx like the change in the yeah other coins that you have i don't know if that made any sense but no i did for the record this is like object capabilities uh you know the way of of doing that uh like a seed is a capability to generate

**02:48:46**  like a deterministic wallet and if you know how to do that uh in a sort of factory way um i mean that wallet the master seat is not going to be discoverable to normal wallets but you're basically like if your privacy wallet is doing that specifically to avoid accidental spending that actually kind of makes sense and then for every individual subaccount where you you can segregate funds you can i mean you have a policy where like first you can generate it as a hot

**02:49:17**  wallet and then like all you can really do is share it with other wallets but if you generate it externally with a hardware wallet then it has an additional phase before it gets exposed like that uh where it's potentially usable for cold storage um and yeah it's uh like having aspirations taha lafs kind of works in a similar like approach where you i mean it's for storage but like

**02:49:48**  your like secret data is basically both the name and the ability to decrypt something some piece of data but there are additional attenuated capabilities underneath that where so for example you can store to a storage grid and you can delegate a verification role where some somebody can or i mean you on a backend server like can run uh something that only knows

**02:50:19**  how to identify your blocks and um make sure that there's like if some storage servers go down then like the data is re-replicated it's it uses like erasure coding to make sure that there's enough redundancy so the verifier who can like heal the storage on the the grids like the storage grids don't know anything about the clients they just know that they're storing data

**02:50:50**  the verifier can make sure that the data is still accessible in case you need to go online later and the way it's structured with the cryptography is just really nicely models these different levels of access that you might want to allow for different kinds of users and bip 39 seed words are capabilities to generate a wallet and about 32 is uh describes a capability

**02:51:20**  system especially when you use the hardened generation um like you can segregate at that level as well uh like nobody mentioned that yet but that gives you something analogous to how um like the 85 can can segregate different wallets um because you cannot export an x-bob of a hardened key um like um something uh above the that like you you can't really um

**02:51:51**  i mean hashes in order to obtain the the chain code it hashes the the private key material that's what a hardened derivation is so like that uh that thing is is um not available to like other um like when you have a different wallet um it knows nothing about the hierarchy above it uh whereas if you're using non-hardened derivation um like the the linkage between them the

**02:52:21**  master bip 32 key and the account key um is uh overt sorry that was a really roundabout way of saying that 5. object capabilities for realsies though like it's like i i just

**02:52:51**  this should eat account functions and i don't see why because it's the same exact abstract kind of indexing and it's just so much better portability and segregation it's like why not all you get is winning no it's a trade-off it's a trade-off that's already partly

**02:53:22**  available with upper descriptors that was exactly what i was rambling about now with hardened derivation like that that gets you almost the same segregation semantics as bip 85 just it requires wallets to be able to be configured in that way only output descriptor wallets can be as far as i know uh project idea for anyone out there listening or anyone in here uh um

**02:53:53**  [Music] uh like a key generation like c generation program where you can set up these child paths whether it's the uh dip 85 or um or pop out output descriptors just having like a like you know these like control panels where you're able to like change permissions and generate keys and stuff like that like generate accounts and manage accounts for like some sas products and having something like that for um to manage all your bip85 keys

**02:54:25**  seeds all right how about some lighter topic since cooks you are the last guest still here then i'm going to ask you a question

**02:54:56**  so what are you thinking about at night when you can't sleep what kind of problems hits you away my kind of problems hmm i don't know i i'm like my biggest problem is how can i convince nikolas to merge my pull requests

**02:55:28**  i think that's the closest problem i uh i think about have you tried a whip wrong continent you can take care of his child for a few hours but again wrong continent yeah maybe i can i can hire a nanny and send it remotely with like an a special note it's like merch pull request one five seven seven or something

**02:56:00**  although that might be kind of kidnapping or something might look kind of weird or get a long-range drone with a whipping okay i i i have to point out nicholas if you're listening to this at some point i'm not trying to hurt you that's max he's trying to condone violence on you and you should merge my pull requests

**02:56:30**  we need a mafia mafia style organization for maintainers but on a serious note um the plug-in system is almost a result of me coding a bit too much for btc pay and about you know everybody staying sane with not having to review too much codes that needs to be you know perfect for everybody to use in terms of like from

**02:57:02**  my end i built a lot of experimental features that don't necessarily need to be merged but something to play with so the plugin system is kind of a result of that thinking it's like i want to build a small tool that helps somebody with i don't know exporting their utxos and uh importing them into their bitcoin core wallet or something like that um you know it takes a day to do and then a month to get emerged from

**02:57:33**  tests reviews by people and all that stuff so if it's just something i want to play with um that's something something possible at that point and also all these integrations as well like well i really wanted to do some integration with wasabi like over a year ago maybe even longer but it's not that easy to do you know it takes forever to first you have to set up a docker repo a docker container with

**02:58:03**  wasabi in it make sure the tests work around it apis integration security so and obviously we can just embed wasabi inside btc bay that would be like directly into the main code because that would be kind of a leak in terms of feature scope scope creep so yeah plug-in system that's my biggest mindset right now

**02:58:36**  that's what i wake up screaming at myself about right now yeah but i have like a thousand and one feature requests that i want to solve with plugins so i'm very happy for them yeah but like uh if you if you if you had to ask path about which features he wants merged with regards to the plug-ins it's the feature of removing features

**02:59:09**  which is a very valid use case as well we have so many features in there like like all the apps would be so awesome it could just for example move the point of sale into a plug-in the crowdfunding into a plug-in then other people can if those things are plug-ins that means people can build similar features as plugins right so um what were they asking for like the other day somebody was asking for a lottery plugin before that there was an auction plug-in all that stuff is kind of similar in nature

**02:59:40**  i highly okay i'm i'm gonna get screamed at by half the people listening to this probably but i highly highly recommend you consider um like government monopolies and regulations around um lotteries [Laughter] they will get really really really really pissed if you start taking away

**03:00:11**  their poor people tax income well i mean it would be a plug-in right so the main copies would not have it somebody has to install it themselves so technically it's not even part of b2c paid maybe you know maybe some guy called not cooks comes along and just creates the plugin and publishes it right exactly

**03:00:44**  we're gonna make so many things obsolete holy yeah i think we like to joke as well that we we're trying to make ourselves obsolete it would be pretty nice that people don't rely on us for everything so want to hear a funny story real quick so i went to the liquor store the other day and the clerk brought up bitcoin because i had a bitcoin shirt on and then this really old dude at the counter playing the lottery thought that we were talking about some new lottery game

**03:01:19**  he's probably the guy asking people to feature them isn't that what they said a lottery where you can only win it's the best type of lottery scratch off your uh your 12 words i had this guy i had this guy buy me a lottery ticket once that lost it was very unpleasant

**03:01:49**  very unpleasant the third word matches up i won maybe we're all just in a lottery hunt to get the same wallet as the toshi hat it's kind of true right i mean technically we're all trying to get some wallet that's already has some beauty excels in it maybe ought to be ever in your favor

**03:02:20**  but they're not they know strong encryption that would be one of those lotteries where you won but then lost because everybody would start panicking and selling bitcoin so true but like it is possible to generate a seed that somebody else had so if the like cryptography doesn't change at all for

**03:02:51**  some period of time then eventually like that would happen right like probably probably probabilistically right yeah unlikely i think actually i think people i think the sun will burn out before that yeah way before no i don't know too much about that i'm trusting the cryptographers so the number of uh

**03:03:22**  private keys um i think that the number of public keys is um significantly smaller than the number of possible private keys uh but both are like on the order of the number of elementary particles in the universe and the time to enumerate them is like on the order of the black hole epoch or something like that so like there's there's not enough universe to compute a brute force search on that kind of thing

**03:03:53**  unless you have some like defects in all our random number generators right yeah but that that's a an entirely different thing and and here i mean there's good reason to believe that we know how to gather entropy and how to make it uniform and therefore generate you know sufficiently close to random private keys but that's more or less a solved problem i mean in the case that it isn't uh often like those have been stolen anyway

**03:04:25**  um like the brain wallet uh surges uh there's bots that actively steal any funds are deposited to like a brain wallet that's an easy to guess password oh yeah that happened 10 years ago that was the website that would generate the wallets and stuff and that you'll be able to like type a type of like some seed or something like that

**03:05:00**  also the blockchain info uh wallet i think at some point generated uh duplicate uh seeds oh yeah the entropy bug that's that's awesome holy how can that even happen um they were calling an external entropy source if i remember correctly but didn't include a um error catch for like error messages so they would be using um the error message is the entropy i think but what happened is that work it's way

**03:05:31**  worse than that they were creating um random.org for random numbers oh man oh man when around http when random.org finally made uh htv forced to redirect to hts they just typed the three direct the 301 or three four i don't remember redirect into like that was the entropy

**03:06:05**  yes that but that's that's you said that oh she now he said that that is uh that was uh just using a random uh source of entropy but no no it was usually an external source like a website external source random.org that's what it was yes exactly that's not an external source of entropy that is a backdoor right it's clearly a backdoor

**03:06:36**  that's so up it's like you go to a random.org website some 14 year old kid that coded and edited in php like 10 years ago most likely and returns what like 10 the number 10 or something or what no you hatch the html that contains the 10 and then for what it's worth they also took the local hardware and the number generator

**03:07:06**  to get a source of entropy and then exhort both sources of entropy uh and that's why random.org was used uh kind of because it was just another source of randomness uh to use and that's just the math benefit yeah and it actually did help because i remember correctly the hardware wallet generator had a bug as well so this one returned an error code as well and did not get caught and that bug was even pre-existing and then for a long time only random.org was called until that

**03:07:36**  also shut down so actually the redundancy prevented the error from happening sooner but because nobody checked the code i guess it still happened listen i don't know about you guys but i only generate my seeds and i'm gonna say it here right here live i only generate my seeds with dice and um somehow i always roll a six i don't know but i guess i'm just lucky i should be down to it but

**03:08:07**  accident yeah you should test your dice man i don't know maybe i should go to a casino always rolling there was a demonstration of some of those bad dice where if you roll them in water they always roll to the same number because of the bad weight distribution on them or something water and salt yeah but you know this is basically like

**03:08:37**  generating your recovery words is basically a religious spiritual experience uh and you know you can get higher insights from the gospels of the recovery words that are being laid out at random it's like throwing bones of rooms yeah let's go to the amazon alley and generator and the entropy

**03:09:13**  i'm pretty sure random topic change how has no developer anywhere ever talked about this delegated signature that you can do with sig cash none that jeremy rubin posted to the mailing list like why the hell has no developer ever just been like oh hey guys we can do graft root without craft root like what what the hell wait give me a tldr what happened so you can take my utxoa and your utxob and i can take both of these

**03:09:45**  sign them with sig hash nuns so it only commits to the inputs and no outputs then you can make whatever the hell outputs you want sign your signature on them and i can delegate control of my coins to you and i can take it back by spending my utxo you can relinquish it by spending your utxo but you can effectively do the same type of coin delegation that graphroot allows without craft root developers have known about this for years and nobody's talked about it like you could do so much inheritance

**03:10:16**  or like you know escrow type functionality with that it's it's insane yeah that's actually true so you just build a pre-signed transaction or does it have to be in this grid no just sig cash none um so that my signature commits to your input and my input but leaves the outputs for you to define and like depending on what you do with output um b you could make that multisig you can

**03:10:48**  distribute that however you want do some escrow inheritance however you want you can time lock the pre-signed transactions so that you have the window to back out of it or someone relinquish it like it's like how the hell have developers not talked about this and why is nothing being built with this like so much inheritance headache could be solved with this yeah well in hindsight it's obvious

**03:11:20**  how does that work with tampo um well you could just bury like whatever conditions under taproot for your utxob instead of um like just having them out in the uh the open or doing a pay to script thing and revealing all of them later and you could actually write different pre-signed transactions from different tab route spending conditions or suspending branches yep

**03:11:51**  oh that can get really complex oh that's cool yeah so like your brother gets this first and then if something happened to him your sister can get it and her your mom you can do whatever the hell you want with that and it's all off chain so what i was saying earlier about like having three layers of like wallet

**03:12:21**  functionality this is policy right like i would want my wallets everything to always have like a taproot backup condition that supports that in principle taproot makes that economical like you no longer have to literally put a pdsh uh like redeem script that can handle that so like why wouldn't that be supported in like composable wallets in the future but that's an entirely orthogonal layer of

**03:12:53**  decision making from what do i want to do with those funds yep hey shinobi who who did that jeremy rubin or robinson um he was the one who posted it to the mailing list um jeremy rubin

**03:13:23**  but it like the way he put it is like this is something we've known we can do for forever and i just figured like hey like learn about it people the problem is like a side can unilaterally like upwards so it doesn't really give much assurance but you can play games with that by making utxo a

**03:13:54**  multi-sig or more complicated et cetera et cetera et cetera yeah tough proof makes it all a lot more actually useful but you know i actually kind of like in in most of the cases i'm thinking about applying that the fact that a can revoke it unilaterally at any time and b can bow out of it unilaterally at any time you know what i mean like it you're able to delegate that but

**03:14:27**  either side is able to like sever that relationship unilaterally at any time yep and i mean it makes a whole lot of sense for uh like for example you could imagine uh a large organization managing um like a hierarchy of wallet or something like that so the hot wallets would in the event of a like a catastrophic loss um like all of their outputs would become spendable like a month later by

**03:14:58**  some master key that's always involved or policies like that i'm just struggling to think of other use cases well like my head immediately just went straight to inheritance like you know people i'm describing is like basically inheritance just over a hierarchy right like you can make that as complex inheritance scheme as you want and as dynamic as you want yeah but you know i'm specifically thinking you know um like personal inheritance stuff like

**03:15:30**  that's one one of the biggest problems in this space is people buying and holding bitcoin for the long term like how do i guarantee that can be recovered in a way that isn't unilaterally just handing over control bam right here anyone you want to be able to claim that you create a um a setup like this with whatever utxos you want them to claim and their key or utxob and you could even make those utxops yourself just making dust outputs

**03:16:01**  because who cares it's just an unlocking mechanism and then pre-sign that for however long you want to like that can like that just solves that problem so much and especially the fact that it's all just pre-signed transaction based like you can make one of those for any um family member you trust or want to have involvement or access with that with appropriate decrementing time locks you can even make different multi-sig arrangements between different members

**03:16:31**  of the family and it's just like the fact that this has been possible pretty much since the beginning of time um based with what it works on like that's just crazy to me that nobody has talked about this and nobody is like put this to use in those types of situations like that's the immediate no-brainer solves a lot of users worries and problems yeah seriously like this enables so many vault constructions

**03:17:02**  i mean graft route does in general as a concept but this is basically the concept of graft food so this will make the vault construction so much more easy like i can almost see in my head now uh gmax just sitting here obsessing over this idea and that's slowly evolving into graft right now

**03:17:46**  anyway yeah that's what shinobi's been obsessing about for the last day or so hey adam if you still want to do an inheritance software that just got a lot more easy a lot more easy especially if i would have paid attention dick that's why it's live and recorded

**03:18:18**  it's it's on the record right it's live stream so nothing is lost yep except my lack of offense

**03:18:48**  all right guys then i'm calling this meeting for myself if you would like to stay around chit chat uh rafa the live stream is on you so this was uh this was a really interesting conversation thank you for everyone for coming bye bye what do you mean adam you bow out after four hours so quick already

**03:19:18**  it was a pleasure talking to you again thanks for coming on tools yeah maybe i should end the live stream already now it's four hours or what do you guys think do we have more interest how to kill bitcoin did i say that out loud yeah okay we have to cut it but yeah

**03:19:49**  yeah i'll stop the streaming

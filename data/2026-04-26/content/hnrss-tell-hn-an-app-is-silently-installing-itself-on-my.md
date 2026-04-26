---
title: 'Tell HN: An app is silently installing itself on my iPhone every day | Hacker News'
url: https://news.ycombinator.com/item?id=47906253
site_name: hnrss
content_file: hnrss-tell-hn-an-app-is-silently-installing-itself-on-my
fetched_at: '2026-04-26T19:44:56.100009'
original_url: https://news.ycombinator.com/item?id=47906253
date: '2026-04-26'
description: 'Tell HN: An app is silently installing itself on my iPhone every day'
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
Tell HN: An app is silently installing itself on my iPhone every day
469 points
 by 
_-x-_
 
18 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
171 comments
Every day for the past 3 days around 1pm EST the 'Headspace' app has been silently appearing on my iPhone (13 Pro). Automatic downloads are turned off and I've updated to the latest iOS since this started happening.

I googled around and found a couple reddit threads with people reporting the exact same thing starting 2 or 3 days ago. There were reports from people on iPhone 12 and iPhone 17 so it doesn't seem device-specific.Anyone else seeing this? Does anyone understand how or why this is happening?

 
help

usef-
 
13 hours ago
 
 | 
next
 
[–]

This isn't the first system bug that primarily was visible due to headspace: 
https://www.macrumors.com/2017/12/02/ios-11-1-2-date-bug-cra...

In 2017 it was an endless crash loop caused by any app with local time-based notifications.... Which for almost everyone at the Apple store I visited was meditation apps with daily meditation reminders (in Australia we were among the first to wake up on that affected date. The fix went out before most of the remaining world woke up)I wonder if the daily reminder is triggering a reinstall? Perhaps try disabling the reminders before uninstalling.

reply

_-x-_
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Here's a Reddit thread of other people experiencing the same issue:

https://www.reddit.com/r/ios/comments/1su82sc/headspace_app_...

reply

cortesoft
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

This is fascinating. I am very curious to find out what the actual cause of this turns out to be.

reply

trueno
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

same. i get blasted with ads for this app on whatever platform, never installed it myself. the amount of promotions + this = my underdeveloped brain is so ready to assume the worst here. been a while since i used my pitchfork & i'm here for the riot.

if it is, in fact, something nefarious at play that would be a pretty crazy 2026 era exploit. but i'm certain it's a bug/artifact of some sort that, for whatever reason, affects this specific app.

reply

powersnail
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Maybe the developer was using Headspace as part of the test data and it bled into production?

It's hard to imagine what Headspace would like to achieve if this were an exploit executed by them. It's so salient, that it makes no sense to do on purpose. At least some portion of Apple employees and their families are going to be affected by this, and this would escalate to the legal department immediately.My money is on Apple being the buggy one here.

reply

trueno
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> My money is on Apple being the buggy one here.

Yeah I'm thinking some sort of test artifact bleeding into prod and subject so some nightly process is likely the case.

reply

julianozen
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This seems like a good guess. Seems like it was deployed Thursday based on the app reviews

reply

red_admiral
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I feel sorry for the headspace devs if it's really 100% Apple's fault.

reply

concinds
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I wish Apple released incident reports in cases like these. I hate that their secrecy obsession extends so far beyond hardware.

reply

0123456789ABCDE
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

when "explaining a thing, no more assumptions should be made than are necessary."

could be an ios bug; a bug with the notification library they use, any other app behaving similarly?considering the possibility this was on purpose, they would risk getting banned from the appstore. no, they are not big enough to avoid that. so it's unlikely this was intentional.

reply

dyauspitr
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It downloaded itself on my phone as well. I thought it was some quirk with the Apple Watch sync because I used to have headspace installed at some point and that automatically shows up on the Apple Watch but deleting an app on the iPhone doesn’t always delete the corresponding Apple Watch app. So if you open headspace on the Apple Watch I assumed it redownloaded itself on the iPhone.

reply

Bjartr
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Based on that I'd guess either a meditation app company has figured out how to circumvent a lot of controls put in place by Apple, or it's a bug on Apple's side

reply

_-x-_
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah, I think the latter is more likely than the former. Perhaps a server side bug that's silently downloading the app on any device that's installed it previously?

reply

donkey_brains
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But why this one specific app and no others?

reply

wincy
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Maybe it’s like that time Apple thought everyone wanted that awful free U2 album that they automatically added to everyone’s iTunes library. (I know this isn’t actually the case but it’s the funniest explanation)

reply

theowaway
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

that fucking thing still
shows up on my phone from time to time. It's aural herpes

reply

layer8
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe it’s Apple’s equivalent of Guru Meditation.

reply

mattmaroon
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Can’t be sure it isn’t others. This a very large app, so it may just be the one that gets noticed the most.

reply

_-x-_
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Right, that's what confuses me the most. I was very surprised to find the reddit thread showing that other people are also having this specific app silently installed on their devices.

reply

dd8601fn
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Makes me think something got jacked up adding/removing things from promotional bundles with other apps.

It shouldn’t do that, obviously, but headspace does seem like it’s one that bundles “free” with a bunch of health insurance, education, etc.From a debugging perspective, without having Apples information, I kinda want to know if all affected users have some related health or education apps.

reply

altairprime
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe Apple typo’d an app id incorrectly for some iOS core app thing in 26.4.2 and the one-character error is this app? I don’t know that anyone’s done a ‘likelihood of collision’ analysis on appstore unique IDs yet. Certainly I could see iOS having a “must be on the device” system set up for apps like Phone and Settings that has a last-ditch of reinstalling it if somehow deleted. Would be especially interesting if some core app that can’t normally be deleted is currently unprotected (back up your device 
locally
 first!).

reply

breppp
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Headspace leaves health data, that's where my first guess would be

reply

joenot443
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

My guess is it's a bug on the App Store side which will actually hurt Headspace in the long run. If this was a casino app I'd feel a bit differently, but I'd be shocked if someone at Headspace did this deliberately.

I'm trying to imagine the headspace of a user who deletes an app, only to see it pop back the next morning. Probably not a very relaxing experience :)

reply

a34729t
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Or it is a mandated backdoor, and someone internally objected, and made it easier to exploit than it should be, or leaked how to exploit it?

reply

8cvor6j844qw_d6
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> mandated backdoor

Probably one from the repository of backdoors "accidentally" introduced or "never" discovered.The mechanism's there, just needs to be woven with other exploits.

reply

jdiff
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Makes no sense for headspace to be using it if that were the case.

reply

Barbing
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Conspiracy theory would get too convoluted:

Rogue employee employs the backdoor for a major app with hopefully conscientious users who’ll report it online; hopes to force a fix.Or it was a social experiment and some dumb app reinstalls itself every day too but no one’s complained en masse yet! ;)

reply

0123456789ABCDE
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

what's the more likely explanation though?

reply

Barbing
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

bug

reply

bharat1010
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

looks like, no where its safea anymore

reply

visiondude
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

My hypothesis is that headspace registered many user notifications and since user notifications trigger an app launch and perhaps you have optimize storage by offloading apps enabled? ios has a quirky app state where some local data exists but the app itself (ipa package) is offloaded

reply

threecheese
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

This is the most interesting idea imo; do you think it’s testable? For example: allow the installed app to persist, turn on notifications, do some stuff to let a queue drain. Then remove.

reply

_-x-_
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Agreed, this is an interesting idea. I just checked and offloading unused apps is disabled on my phone

reply

lwhi
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

In which case, perhaps the app doesn't correctly remove notifications on delete which would mean Headspace could be to blame?

reply

sandoze
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There’s no indication to the developer or app when a deletion happens. We rely on the OS to clean it up.

reply

dylan604
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

We've already seen where iOS notifications was storing messages, so it does seem plausible that notifications are involved. Especially as the latest release patches the notifications issue used by law enforcement. It's possible something new was introduced, revealed, etc. The timing feels right

reply

aaronbrethorst
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I wonder if U2, or Bono, has taken a significant stake in Headspace recently (kidding).

reply

fmajid
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

It's not good four my blood pressure to be reminded of that sanctimonious tax-dodging hypocrite.

reply

andy_ppp
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Have you considered meditation? ;-)

reply

ex-aws-dude
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I feel like I’m the only one who listened to that album when it appeared and thought it was pretty good

reply

steve1977
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

A 50th anniversary gift you mean?

reply

meindnoch
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It was so fucking funny. I wonder what the engineer thought, who had to issue the SQL query which added Bono to literally 
everyone's
 collection. Like, I'm not surprised that management was so out of touch, but I'd expect the engineers to have a bit of common sense...

reply

baq
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And do what? Quit and have someone else execute the query for something that’s in the grand scheme of things irrelevant?

reply

Barbing
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There’s only a 99% chance they would’ve been fired for refusing though right?

reply

mort96
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I feel like that's the kind of thing it's easy to not recognise as a terrible idea until 
after
 it's done, because so much of what makes it a bad idea is a consequence of the rest of the system.

Imagine if everything else surrounding the Apple ecosystem worked better. Imagine if people who don't actively use Apple Music never experienced Apple Music starting to play music by itself. Imagine if people who do use Apple Music never had an album play without being actively interacted with. Imagine if the album cover wasn't low-key softcore gay porn. Imagine if you could "uninstall" an album you own, like how you can uninstall an app you own andnever eversee it again unless youactivelygo out of your way to search for it on the App Store.Would it still have been a violation of consent? Sure, yeah it would. But almost everything people complain about is related to how it starts to play when they don't want to (an issue with iOS/macOS and Apple Music that would be annoying regardless), or how the album cover sometimes unintentionally pops up on your screen (such as when you hit the play/pause button on Mac when macOS doesn't think that there's any active paused media, so macOS opens Apple Music), or how there is no way for them to get rid of the album once they own it. These things are pretty large problems regardless of Songs of Innocence.I can sort of understand an engineer thinking that surely there can't be any major downsides to just giving away a digital good. And if the rest of iOS, macOS's, Apple Music and the album itself didn't have all these issues, it wouldn't have been much of an issue. Again, it would've been a consent violation, but developers at tech companies aren't exactly known for valuing consent anyway and everyone would've certainly forgot it by now.

reply

nottorp
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Imagine if people who don't actively use Apple Music never experienced Apple Music starting to play music by itself.

Nice dream. My wireless headphones act like in the manual when paired with my phone, but the buttons on them always start apple music when paired with my laptop instead of muting or controlling noise canceling.

reply

basisword
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

>> I feel like that's the kind of thing it's easy to not recognise as a terrible idea until after it's done

I don't even think it was a terrible idea. It was just one of those things lots of people irrationally hooked on to. "We're giving you all a free record". Enough people made it 'bad' because people like to make a fuss. The only real issue with it was the inability to remove it which they later rectified.

reply

mort96
 
37 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Eh no, sorry. The practical result is that a ton of people who have absolutely no interest in U2 has Songs of Innocence start playing when they don't want it. It plays when people turn on their cars. It plays when people connect to Bluetooth speakers. It plays when people want to resume Spotify playback but Spotify got killed in the background. It plays when people want to resume the YouTube video they were watching but macOS lost track of what's paused. It's a truly terrible idea in practice.

Apple didn't really rectify the inability to remove it. They released a removal tool, but that tool is long defunct. The only way to remove it these days is to contact Apple Support, from what I can tell on the web.

reply

PunchyHamster
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What he was going to do, ignore management ? There is always someone else clueless or not caring enough to do it

reply

kotaKat
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

"We wanted to deliver a pint of milk to people's front porches, but in a few cases it ended up in their fridge, on their cereal. People were like, 'I'm dairy-free.'" -Bono

Literally imagining the milk man bursting in to dump a gallon of milk on some poor sod's cereal this morning.

reply

chihuahua
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not only that, but the milk man also acts like he did them a huge favor. And hides his huge fortune in a tax haven, while relentlessly campaigning for the government to increase the tax burden on those who actually pay taxes.

reply

Barbing
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Helped eliminate poverty, hmm:

>Despite being well known for his extensive charity work, Bono has previously faced backlash over his tax dealings, with critics claiming that he could have helped to eliminate poverty if U2’s tax base remained based in Ireland.>Instead, it previously transpired that U2 often put their money through the Netherlands, where tax rates have reportedly resulted in increased profits for the Irish rock icons.>Two years ago, Bono dismissed the criticism as “just some smart people we have working for us trying to be sensible about the way we’re taxed. And that’s just one of our companies, by the way. There’s loads of companies”.https://www.nme.com/news/music/bono-releases-statement-named...

reply

umanwizard
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Have you ever worked at a big company? There are plenty of people who don’t give a shit and just do whatever their boss tells them.

reply

actionfromafar
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They follow orders, like soldiers do.

reply

edbaskerville
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Deep cut

reply

swiftcoder
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Jesus, I hope not. That happened just a few years ago... right?

reply

dtech
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

More than a decade ago

reply

stingraycharles
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Wasn’t that around the release of the iPhone X?

reply

kaelwd
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

iPhone X? That came out this year didn't it?

reply

hnlmorg
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, you’re thinking of the iPad Touch

reply

ukuina
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm pretty sure it was last year, when the "no new features, bugfixes only" MacOS version was released.

reply

COFyumo
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I have the same exact thing happening. I deleted the app a few days ago when was surprised to see it in my app list.

I had previously downloaded the app but and removed it because I never used it. A few days ago I noticed the app when browsing through my app list and thought maybe I didnt delete it properly, so I made sure to delete it. Then this morning my iPhone updated software versions and I found he Headpsace app again on my home, except this time it was grayed out and waiting for me to go on wifi to download.I just deleted it again but am equally dumbfounded

reply

_-x-_
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

That's interesting that it still showed up on your homescreen despite not being able to download

reply

yokuze
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Do you have Settings > Apps > App Store > (Automatic Downloads) App Downloads turned on?

I noticed apps appearing on my Home Screen I’d never heard of before. Turns out with that setting and Family Purchase sharing turned on, every time my wife installed a new app, it installed on my phone too.That may not be your exact scenario, but I wonder if turning off that Automatic App Downloads setting (if enabled) changes anything. Could give you a clue, if so.

reply

_-x-_
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

App Downloads and App Updates are both turned off. I don't have anyone else's devices on my account, just me. Thank you for the suggestions though!

reply

wallst07
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Even with auto downloads turned off, does it show up in your app library or as a purchased app?

You can still have a app library with apps that "should be" downloaded, what happens if its removed from that list?

reply

nostromar
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

This was happening for me also. 3-4 days in a row it would reinstall in the evening. I’m on a new iPhone that never had the app installed. Automatic downloads wasn’t on, etc. finally noticed that signing out of “Media & Purchases” and then signing in again would make it install almost immediately. Could reliably repeat this any time of day. At one point I preempted the install by long pressing on the Headspace icon and selecting “Cancel Download”. It disappeared and hasn’t been back since.

reply

OptionOfT
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I had a related issue.

I had an iPhone, then work offered iPhones, and I (stupidly) did not separate the phones or the accounts. So personal stuff on work phone. It's Apple, It's supposed to be good. MDM removal should completely remove work stuff from the image right?Well, not so much. I had a non-removeable TMobileWingman WiFi network (even though I moved to Verizon) configuration, a stuck VPN configuration and a couple of shortcuts that I couldn't remove.Eventually I fixed it by taking a backup, going through it with iMaze, and basically try to nuke stuff, and then restore the backup, hoping it work.Quite insane how much stuff is left around in your iPhone backup by the way.

reply

gcr
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Do you have any MDM profiles installed? Go to Settings → General → VPN And Device Management. If you use your phone for work your employer may have asked you to install one, but check anyway. MDM profiles can specify apps to be installed automatically.

Also, is developer mode enabled?

reply

souterrain
 
30 minutes ago
 
 | 
prev
 | 
next
 
[–]

Anyone know when Apple's acquisition of Headspace is closing?

reply

nottorp
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Meanwhile, I can't install an iOS game i bought in 2021 (Azure Saga if it matters) because it's delisted from the app store.

Damned if you pay them, damned if you don't.

reply

forsalebypwner
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

Took me a minute but I found it 
https://archive.org/download/iklassika_archive/AzureSagaPath...

reply

nottorp
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Probably requires a jailbroken ipad?

I'll take it as a lesson to not even look at games on iOS [1]. I added it to my wish list on Steam, i might get it on a sale.[1] Not that iOS has many games. I can't afford the free ones.

reply

forsalebypwner
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No jailbreak required, just sideload it with a tool like Sideloadly. There are plenty of games, but it's understandable if you don't want to support Apple's practices.

reply

lbourdages
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Didn't know that tool existed, thanks for that! I assume it's using the development features in order to bypass protections?

reply

nottorp
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yep, there's some mention of automatically resigning the apps every 10 days so it's definitely using the dev tools.

reply

NoMoreNicksLeft
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Holy fucksticks. Does this really work? I could get back Marvin 3 on my phone...

reply

doncho
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Very interesting, especially if it found a way to bypass the explicit disabling of automatic downloads…

Now imagine you’re roaming during a 10-day vacation…and you think you’re in control :) …

reply

saagarjha
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

If you can take a sysdiagnose I’m sure it will have the answer in it. If you want to send me one (note: may contain sensitive information) feel free to contact me or any other person you trust who is familiar with iOS stuff?

reply

janstice
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Is your phone connected to some work mobile device management? I could imagine someone has a jinxed Jamf or intune rule that is pushing things out.

reply

_-x-_
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

No, this is my personal device. It has never been connected to any MDM.

reply

Schiendelman
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Have you 
actually checked
 your device management settings?

reply

_-x-_
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes. In Settings > General > VPN & Device Management, it says 'Sign in to Work or School Account'. Is there a different device management setting that I should be looking at?

reply

Schiendelman
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's the one. I was worried you might have something you didn't know about!

reply

teruakohatu
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, there are alt app stores that try to get you to agree to installing a MDM

reply

nunez
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm wondering if this has something to do with the iOS Storage Offloading feature, wherein an app that looks like is uninstalled is just offloaded. This would explain why some users see the app in gray waiting to be downloaded.

reply

a34729t
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I would call Apple support; you might even get an engineer call you back. I am sure they would love to know what the hell is going on.

reply

Zambyte
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Don't people pay extra for Apple devices so they can go to Apple with their problems? Go to Apple...?

reply

altairprime
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

The iOS reviews for the app also confirm this story affecting others.

reply

julianozen
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Looks like something was deployed Thursday evening. My bet is it’s some kind of test configuration for the App Store itself that just happened to pick headspace and it’s rolled into prod by accident

reply

1659447091
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Do you use iCloud drive?

This might be a stretch as I am taking a guess at the implementation, but apps can sync with iCloud Drive and I keep getting app folders showing up after telling it not sync but the prefs reset after certain states(not quite sure when/how)-- it then creates a new sync folder when interacting with the app again. (after having turned off sync and deleting the folder -- once it resets)I am wondering if that app had that feature (icloud drive syncing) and something of the reverse is happening. Where you have a document still on icloud drive from when you installed the app. Maybe there is some action or state change going on after interacting with drive on a mac or something similar. And now it's created the right circumstances for icloud drive to try and sync the file but there is no app on any device so it downloads the app instead since it's missing and there is some dangling file looking for its home.

reply

_-x-_
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

It still doesn't make sense why the app started silently downloading itself 3 days ago when I haven't had it installed in over a year. I do use iCloud drive but do not see anything related to the app inside of it.

reply

1659447091
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Did you update iOS before it started happening? Wondering if they may have introduced a regression that is now trying to re-sync everything after the last update (sync files may be hidden, I set files to always show)

reply

_-x-_
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I updated after noticing the issue

reply

caycep
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

for an app called headspace, it really is messing with your headspace!

reply

ddxv
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

If anyone wants to browse some of the SDKs in headspace:

https://appgoblin.info/apps/493145008/sdksI see normal development and tracking SDKs. If anyone sees something interesting let me know.

reply

speedgoose
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

The Facebook Ads SDK in a mental health app isn’t normal. Or shouldn’t.

Even analytics SDKs is a bit weird to see. Are Amplitude or Sentry hosting data with a healthcare compliant infrastructure ? I won’t bet. Are those SDKs for sure not leaking health care data? It can be inadvertently, especially with Sentry. But I really wonder about why people feel the need to track so much. Do they **** in front of PowerPoint slides showing the tracking data or is it to sell user data?

reply

rkachowski
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They are normal. They generally want to know if the ad spend resulted in an install. Health care data is radioactive and they would be fucking up very hard if sending this to an analytics service.

reply

speedgoose
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have seen studies where some apps were fucking up very hard and sending healthcare data to services that shouldn’t receive it. Sometimes in clear text.

My trust is very low. Having healthcare data in a Sentry payload by mistake happens to the best of us.

reply

hansvm
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Health care companies are radioactively affected by mishandling healthcare data (give or take practical impact being very toothless, especially nowadays). The data itself is mostly not an issue though under any legal theories, and if Joe Schmo hedge fund digs up your colon photos that's not usually an issue.

reply

concinds
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I never thought there would be online SDK databases, what a useful resource in general. Thank you.

reply

whilenot-dev
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I think it's worth mentioning that you had the app installed around a year ago, as I can imagine some "restore from backup" scenario at play.

I'm currently with a 13 mini (26.4.2), never had this app installed, and am not encountering this issue.

reply

_-x-_
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

This appears to be a more widespread issue affecting users that have previously installed the app

reply

k310
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Did you ever install it, or Ginger?

An app store search also turned up "Headspace Care" (Ginger)Ginger is now Headspace CareIt would be beyond malware for an app to install itself, since there's that app store hurdle to leap. (IMO)

reply

_-x-_
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I installed the app in March of last year, and then deleted it the same day because I didn't want to pay for the subscription

reply

nkotov
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Had this happen as well. I haven’t used Headspace in years. Randomly had the app appear on Home Screen.

reply

bastawhiz
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Do you have MDM enabled on your device? Does your company offer Headspace as a perk and some arcane set of sketchy business agreements led to auto install policy in your company's MDM solution?

reply

_-x-_
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

No MDM installed

reply

gordon_freeman
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

sometimes if you have downloaded an app on Mac it automatically tries to install itself on iPhone due to some settings somewhere. Not saying that's the case with your app but I've noticed that with apps being installed on my iPhone when I install some apps on my Mac.

reply

con
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Just checked and it also installed itself on my phone. iPhone 17 Pro, non-US App Store, on latest iOS beta, no MDM. Sounds like an Apple Store bug to me.

reply

HoldOnAMinute
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

I have never installed it, and currently don't have it installed.

reply

concinds
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Ever had it installed before? I wonder if that's a pattern.

reply

DANmode
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Definitely the strongest pattern.

reply

con
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I did

reply

serial_dev
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Just a theory, I give it about 0.001%.

What if it’s the U2 Bono of the apps?Apple struck a partnership with them, they will roll it out as part of their OS, everyone will get some version of it for free? Some dev at Apple is testing the auto rollout feature, they didn’t realize it was for production?

reply

jonplackett
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Yesterday I put my AirPod in and squeezed it, expecting Spotify to play - but it must have quit, and instead my mac opened up Music - and that album was STILL there and started to play. How many years has it been?

reply

rglover
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

If you've ever installed any companion app on your desktop macOS, your phone will try to sync apps (I think the same with Apple TV). Caught me off guard a few times.

reply

_-x-_
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

No, I've never downloaded it on my desktop. It appears that I downloaded it onto my phone over a year ago (I got an email in my inbox), but didn't want to pay for it so I deleted it.

reply

dagmx
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m curious if everyone experiencing this is on 26.4.2? It came out 4 days ago according to Wikipedia…it would make sense that it lines up with when people are seeing it start.

I’m on the 26.5 beta and not seeing it at all.

reply

_-x-_
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I was on 26.3.X when it began happening, prior to updating

reply

Dumblydorr
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

The irony of a meditation mindfulness app becoming a zombie and annoying and distracting thousands of people is palpable. I don’t use the app but it sounds completely off brand!

reply

timothyisonline
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Possible this is tied to your carrier?

reply

snailmailman
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

I don’t think carriers have the ability to install apps on iOS. I’ve always thought it’s weird that they can do that on android.

reply

burnt-resistor
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They absolutely do. Some countries mandate some apps that cannot be removed. While Apple doesn't allow carriers to install mandatory bloatware apps, it allows country-specific "national security" apps and background processes that don't have app icons. It's been this way almost forever in pretty much every country that just about every mobile device, it's just Apple has been a bit better for users.

https://www.wired.com/story/apple-russia-iphone-apps-law/https://9to5mac.com/2025/12/03/after-apple-refusal-indian-go...

reply

waiwai933
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Those articles don't seem to support what you're saying? Russia's apps aren't preinstalled, they're just offered as suggestions, and India never got their app installed. I certainly don't see anything that mentions background processes in either article either.

reply

tjoff
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What? Sounds like a US thing?

reply

treexs
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

this is the plot of Persona 5

reply

rootsudo
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

He can be the joker we need.

reply

efilife
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

how heavy of a spoiler is this? I wanted to play it

reply

applfanboysbgon
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's not really a spoiler. It is something that happens near the beginning of the game.

reply

makeitdouble
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's covered in the first 10~20min or so of the game, and is really a minor side point.

Off topic, put P5 as a game doesn't really care about spoilers much, there is one specific story telling gimmick that will screw with you if you're really sensitive to these kind of things.

reply

diegoperini
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If I am not mistaken, it's even shown in the marketing materials to build suspense.

reply

bobkb
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

You had previously installed this application?

reply

derefr
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Do you have an Apple Watch paired to this iPhone?

(I know that installing apps on iOS forces installation of the equivalent watchOS apps; not sure if having a watchOS app installed/running/activating itself forces installation of a "companion" iOS app that it might rely on.)

reply

orf
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Does it happen when WiFi and mobile data are disabled? Try disabling them an hour or so before 1pm EST.

If it still appears then it was never removed in the first place, which is a very different bug to it installing itself.

reply

DavideNL
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

@_-x-_: "Settings > App Store > Show Install Confirmations > On".

Maybe that helps?

reply

garyfirestorm
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

This setting does not exist on iOS 26.4.1

reply

DavideNL
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It should:

-https://old.reddit.com/r/iPadOS/comments/1prkpaq/can_i_turn_...-https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd....

reply

parker-3461
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I just checked that I could see it in the Settings App search bar, but it does not show up under the actual App Store settings page, might be an implementation bug related to user region.

Edit 1: this was on iPadOS 26.3.1 (a) (23D771330a)

reply

jgrahamc
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Same here. I had installed Headspace long ago and deleted it. It's now reappearing if I delete it.

reply

verisimi
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Side point, re this:

> Automatic downloads are turned offIsn't it funny that we're so used to the misuse of language (ie lies) that this isn't even a point? I'm talking about software flags to represent your choices, that are merely an 'aspirational intention' and don't actually correlate with reality.In my world, it shouldn't be possible to override 'turned off automatic downloads'. 'Off' shouldn't be a pacifier for the user, while Apple, Google or whoever can continue installing whatever they like. This isn't what words mean. There isn't actually a choice, but it misleads you into thinking there is. I'm sure there are legal words around this in the "ownership" contract, but "off" can't really mean "on".

reply

darepublic
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Instead of screaming eff you at Headspace, recognize the deep unconsciousness at work in our capitalist technocratic world

reply

bfbf
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Do you have TestFlight installed? That’s the only other way I can think of delivering apps besides the App Store and MDM.

reply

saidnooneever
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

i dont know whats up, id assume bug but i wanna say iphone is uniquely annoying to find out what is happening on it and why things happen. they make it especially tedious and that makes it much easier to think this kind of stuff is nefarious even if ut might not be

reply

mandeepj
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

How did you find that? Any notification?

reply

_-x-_
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

It just appears on my homescreen

reply

psynixx
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been getting this too, same app same behaviour…
Anyone been able to figure out what is causing this?

reply

_-x-_
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Have you downloaded the app before?

reply

sfc32
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Sounds like it's messing with your head.

reply

walrus01
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe Bono is a major new shareholder in Headspace.

reply

NetOpWibby
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

_Severance intensifies_

reply

dvh
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

This is clearly bug in "automatic updates are turned off" feature, and the fix should be made there.

reply

bofia
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Are other people using your phone?

reply

_-x-_
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

No

reply

csomar
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

> Does anyone understand how or why this is happening?

They are drowning in tech debt. Here are two main issues I have with my iPhone/iOS: I can't search for the telegram app. It doesn't show up. It shows fine on the iPad. Also just a few minutes ago, app search decided not to work. I usually use it to pull my Wallet to pull my card. It was an awkward moment as I had no idea where the wallet app actually is.I have lost count of the minor polish issues. The experience has degraded so much that you no longer care.

reply

snailmailman
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Regarding the telegram app I’d check iOS settings->apps->telegram->search and make sure “show app in search” is checked

You can intentionally hide apps from search. If you did this, it’s not very obvious that its hidden from search unless you dig for the setting. Similarly, “hidden” apps refuse to show up in search results anywhere, even in settings.

reply

nathanwh
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you for this, I have wondered for more than a year why Google Maps would not show up when I searched for it.

reply

csomar
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Thank you. I wonder how that happened as I was not aware such a feature existed.

reply

hmokiguess
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Now imagine if they added some AI feature and it’s trying to escape

reply

userbinator
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Now you understand how it feels to be reminded that the device you "bought" from Apple isn't actually yours as they still have control over it, and if they decide to do something you don't want, you're powerless to stop them.

reply

meloyc
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

jailbreak phone?

reply

_-x-_
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Negative

reply

throwaway5465
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe a competitor is trying to FUD them?

reply

_-x-_
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I would imagine that this isn't (or at least shouldn't be) possible based on Apple's security. The app is automatically downloading to my phone without my permission.

reply

lovich
 
16 hours ago
 
 | 
prev
 | 
next
 
[8 more]

[flagged]
anon84873628
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

At least they're exposing their nefarious plans for the purposes of... Offering people mental healthcare?

It's probably just some Apple bug.

reply

lovich
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Why did a mental healthcare company have the ability to exploit this?

Do you think they accidentally found this 5 seconds before their exploit was launched or do you think they might have actually put some effort into doing this since they are an organization of people.

reply

kennywinker
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am pretty skeptical it’s intentional. Very risky move. If they make apple look bad they can say goodbye to getting featured in the app store, or could even get pulled from the store completely.

Icansee a fucked up ceo greenlighting a trick to get their app installed on your phone without asking. I can’t really see them having it repeatedly download.I suspect it’s a bug, or worst case a backdoor that’s been triggered with a commercial app instead of spyware accidentally or “accidentally”.

reply

altairprime
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I cannot possibly imagine the company 
as a whole
 would approve of this, much less anyone at the company who wants to keep their job. If it’s found that they exploited Apple to cause this, Apple might force-remove their app 
worldwide
 and 
definitely
 will kill their developer account pending any lawsuits. That’s the sort of thing that gets a CMO fired. Seems extremely unlikely, but if their C_O gets fired on Monday or Friday, then we’ll probably know why :D

reply

firecall
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> The fact that it’s happening shows that they always had the ability...

That may not be the case here, and certainly isn't the assumption we can make more generally.We regularly see regressions in platform security.

reply

lovich
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[3 more]

[flagged]
slater
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Please don't comment about the voting on comments. It never does any good, and it makes boring reading.

https://news.ycombinator.com/newsguidelines.html

reply

lovich
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

When this forum handles the bot and propaganda problem I might consider those rules.

Currently we are inundated by accounts who don’t give a shit and make a new automatically 3 seconds after their flagging.As long as those accounts are allowed I don’t really care for the stated rules that aren’t actually enforced.

reply

Consider applying for YC's Summer 2026 batch! Applications are open till May 4

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search:
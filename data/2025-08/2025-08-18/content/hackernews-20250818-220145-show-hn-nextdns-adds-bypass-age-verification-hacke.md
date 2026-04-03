---
title: 'Show HN: NextDNS Adds "Bypass Age Verification" | Hacker News'
url: https://news.ycombinator.com/item?id=44931824
site_name: hackernews
fetched_at: '2025-08-18T22:01:45.354214'
original_url: https://news.ycombinator.com/item?id=44931824
author: nextdns
date: '2025-08-18'
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
Show HN: NextDNS Adds "Bypass Age Verification"
447 points
 by
nextdns

21 hours ago

 |
hide
 |
past
 |
favorite
 |
151 comments
We just shipped a new feature in NextDNS: Bypass Age Verification.

More and more sites (especially adult ones) are now forcing users to upload IDs or selfies to continue. We think that’s a terrible idea: handing over government documents to random sites is a huge privacy risk.This new setting workarounds those verification flows via DNS tricks. It’s available today to all users, including free accounts.We’re curious how the HN community feels about this. Is it the right way to protect privacy online, or will it just provoke regulators to push harder?https://nextdns.io

pogue

8 hours ago

 |
next

[–]

Hey @nextdns team. I'm a long time customer of NextDNS. I've been using your service for a few years now, but it seems a large amount of your primarily offered services & blocklist offerings are
SEVERLY
 out of date. I detailed that here on Reddit:

https://www.reddit.com/r/nextdns/s/IX2mUogHPK

Your input on this thread would be greatly appreciated, as the community wants NextDNS to be the best service it can be.I do appreciate the addition of the Age Verification Bypass, though. Many users on r/nextdns are trying to guess how it works. Proxing specific domain requests to show the user is from another country is our best guess. But I would still be very interested in the specifics.Thanks.

reply

huhkerrf

5 hours ago

 |
parent
 |
next

[–]

I'm really surprised to see this pop up considering how the NextDNS team seems to have disappeared otherwise. Out of date offerings like you mentioned, coupled with 0 customer support when things break (and things break a lot). New features like this are fine only if the base service works. I can guess that this feature also is going to break soon, and I don't have high hopes for it getting fixed.

I moved over to ControlD about a year ago and I've been very happy. Nothing has broken, and they seem to be active about their service.

reply

1dom

2 hours ago

 |
root
 |
parent
 |
next

[–]

Same here, I left NextDNS because I didn't trust it anymore. I started using it personally in homelab and just found it to be randomly a bit sluggish at times. Saw other similar reports. Tried to get support and failed. I saw it trying to sell itself as business capable DNS, and considered if it would fit in at work. Then I got an e-mail giving 7 days for me to disable and move all my logs out of the EU region. I was working at a large fintech firm at the time, and if a vendor had given us 1 week to rearchitect and figure out a new logging solution for DNS, we would have dropped them immediately due to the massive compliance issues they would have created.

The messaging around the change was very much "FYI we're deleting everything in 7 days in that region whether you're good or not, feel free to do what you want", e.g. creating problems with no interest in helping with solutions to those problems. This would all be fine for a free-tier service, but I was a paying customer. Even as a paying customer though, I paid virtually nothing.Overall, NextDNS felt like it had the worst possible combination startup, passion project and beer money project features: I paid for it for a couple of years and got fed up because the amount talk about it gave the impression to me there was a fair and growing customer base but NextDNS were missing either the capability or focus to grow the service at the time. I'm conscious they'll be reading this - it was 2 years ago this happened, so maybe things have changed.

reply

agos

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

I went to see ControlD's website to see if it was any good but the chat thingy was trying to convince me by saying "protect your connection like the Coliseum protected Rome, try ControlD's free DNS", which I guess is a way of trying something funny since I'm connecting from Italy, but it does not inspire much confidence in their protection abilities

reply

dmd

44 minutes ago

 |
root
 |
parent
 |
next

[–]

It’s clearly AI generated, and badly.

reply

smt88

24 minutes ago

 |
root
 |
parent
 |
next

[–]

Incredible that they found a way to use AI to do anti-marketing and lose customers

reply

dmd

15 minutes ago

 |
root
 |
parent
 |
next

[–]

A
remarkable
 number of people seem to think "let's add AI to this!" is (a) always the thing to do and (b) don't even examine the output once before having it go live (or afterwards either).

reply

jalk

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

So it protects your connection by putting up a spectacle? (assuming it meant Colosseum)

reply

tecleandor

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

Mine (Spain) said "control your DNS like a flamenco singer" and it doesn't make sense at all. ¯\_(ツ)_/¯

reply

bluehatbrit

1 hour ago

 |
root
 |
parent
 |
next

[–]

From the UK you get "Explore your rules like a London detective" which barely makes sense, and is an immediately makes me think it will be useless.

reply

cgriswald

1 hour ago

 |
root
 |
parent
 |
next

[–]

US version:

“Unlock the full potential of your network with Control D's advanced filtering and security features, perfect for the land of the free.”

reply

leokennis

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

Same here...NextDNS randomly started intermittently breaking all connections to Apple (iCloud file sync, Apple Music etc.) and basically nothing was done about it.

Moved to AdGuard DNS, very happy with it. They have random sales throughout the year where you can buy a few years of discounted service in advance, so the cost is next to nothing...

reply

deanc

4 hours ago

 |
parent
 |
prev
 |
next

[–]

+1 to this. I used to use their Samsung blocklist to prevent their shitty ADs being injected into my (pretty-old) tv but it's not been working for at least a couple of years.

reply

freedomben

16 hours ago

 |
prev
 |
next

[–]

It
may
 not be effective in the long term, but I think it's very much worth doing. The privacy nightmare of uploading government docs is appalling and should be resisted by all who can, so I think you're doing great work. If it provokes regulators to push harder, they might just get enough attention from voters to motivate a change. That would be my hope anyway

reply

Alive-in-2025

16 hours ago

 |
parent
 |
next

[–]

It's a great idea to get rid of, I'm shocked a company is this brave to do this. It's not in the interest of any adult to upload their ID so the government can track their web browsing. I didn't want to expose my kid to porn when they were 5, somehow it wasn't a problem because the avg browser use was guided by me, but also the browser blocked porn. When they were a bit older, a teenager, I also lightly guided their computer use.

reply

petcat

13 hours ago

 |
parent
 |
prev
 |
next

[–]

> More and more sites (especially adult ones) are now forcing users to upload IDs or selfies to continue.

> they might just get enough attention from voters to motivate a changeUnfortunately, guaranteeing anonymous internet porno is aterriblepolitical beachhead to motivate "voters" to do anything.

reply

selcuka

8 hours ago

 |
root
 |
parent
 |
next

[–]

> Unfortunately, guaranteeing anonymous internet porno is a terrible political beachhead to motivate "voters" to do anything.

Reworded press release: "We protect children from being forced to upload their photos (on their IDs) to adult web sites"

reply

SunlitCat

8 hours ago

 |
root
 |
parent
 |
next

[–]

Another rewording:

"...to upload your photos (on your IDs)..." :D

reply

topato

5 hours ago

 |
root
 |
parent
 |
next

[–]

Oh yeah, that IS a good point, this verification technique is even stupider than CC number validation in the late 90s!

Then again, these laws aren't about censoring children's access, they're about censoring EVERYONE'S access (and it blows my mind that conservative leaders will come right out and say it, but the average layperson doesn't seem to care or comprehend what a massive slippery slope censorship is -- porn is just the start)

reply

Spivak

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

You don't have to sell it like that. The bill that needs to be passed is default presumption that all websites on the internet not explicitly marked as such and who voluntarily accept a higher legal burden and standard of moderation may contain content not suitable for children. And that is up to parents to control their child's internet access to limit their usage to only these sites.

Because I don't actually care about pornography, if it magically disappeared I wouldn't really care, it's all the other "not suitable for kids" content I care about that will get caught up in these laws. I don't want to give gross concern troll political groups moralizing about their precious hypothetical children the legal tools to ban what they don't like.

reply

topato

5 hours ago

 |
root
 |
parent
 |
next

[–]

Ive had massive amounts of trouble convincing people that pornography is just the tip of the iceberg. That's why it's such an effective tool for broaching massive-scale surveillance: the architects of these laws have said that they want to be able to police all content with these laws, and anyone who tries to speak out against them can be painted as a pervert who hates the safety of kids.

reply

tomrod

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

It's not about porn. It's about setting a legal beachead to force websites to deanonymize users.

reply

pbhjpbhj

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

You're asking for them to set up a system that won't be effective.

>And that is up to parents to control their child's internet access to limit their usage to only these sites.This is an entirely unreasonable expectation on parents. I control web access at home, but I can't control it at school, or at their friend's houses. Nor do I have time, nor do I have access, to exert control over all the systems they come in contact with (even without their own device).>it's all the other "not suitable for kids" contentLike what? Explicit violence?

reply

notepad0x90

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Even if this was a good idea, ID verification technology should not be outsourced to private parties. This is a service governments themselves must provide. I shouldn't need to upload an ID because the government already has it!

If they simply wanted age verification, the dumb and lazy way is to SSO through a government managed portal with OAUTH2 and you only share your age with the third party. You do a one time account setup (you already have to do this in the US for many government services at the federal level) with age verification, that's your gov portal login. This means the government will now which naughty sites you visit of course, but like I said, it is the lazy approach, and if you think about it, if they respect the laws then a law can be passed to prevent them from storing or using that association, if they didn't, they could still sniff your traffic and wiretap you.A slightly smarter approach would be to directly auth against a government portal and be given a 24h expiring code for age verification, and the government will publish an updated list of codes to trusted businesses. Those codes could be leaked, but making it a felony should deter most cases, because who wants to go to prison to let some kids watch porn?Smarter people than me can come up with smarter solution, that is really my point. Involving third-parties and requiring you to upload documents is done either out of extreme incompetence or opportunistic malice by elected officials (bribery).

reply

franga2000

4 hours ago

 |
root
 |
parent
 |
next

[–]

Every possible solution is terrible, many people have thought about this and nobody has found one that isn't.

The "24 hour code" one you suggest is something the EU is prototyping. Since there's nothing stopping an adult from sharing their code with a minor, or even code-sharing (or selling) websites to pop up, they want it to be bound to a particular device. So what they've done is added integrity checks to the app, so you can only run it on a locked down phone.Want to run GrapheneOS for privacy and security? Or use an unofficial ROM to get updates on a phone the manufacturer stopped supporting? Just want to uninstall the bloatware and spyware the manufacturer installs? Want to use Linux? Have an old computer without a TPM? All of that and more - congrats, no "adult content" for you.And no, it's not "porn", it's "adult content", which is a much broader and blurrier category. Is discussion of sexual orientation or gender issues adult content? Sex education? Medical information about "private parts"? News articles mentioning scary things like rape?This is bad technology and it should never be developed. Do Not Create The Torment Nexus.

reply

zimpenfish

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> the dumb and lazy way is to SSO through a government managed portal with OAUTH2

The weird thing is that UKGOV already has this for the NHS - my GP's app uses access.login.nhs.uk to log me in. That could easily verify my age to another system.(Admittedly it's not sufficient for the wider case because not everyone is registered on nhs.uk but it does show that UKGOV has the capability to do this.)

reply

kijin

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

South Korea has implemented something similar, but through private corporations, not directly by the government.

When you sign up with a South Korean online service that might contain age-restricted content, you provide your name, date of birth, and phone number. The service operator uses a special telecom-provided API to have a 6-digit code sent to your phone. (The code is generated by the telecom, not the service operator.) When you enter the code, the telecom confirms the name and date of birth. No need for random online services to ask for government IDs, because they're allowed to pass the burden of proof to telecoms who have already verified it offline.You could probably do something similar via banks, schools, the social security system, or any other regulated industry that has KYC rules.

reply

phatfish

3 hours ago

 |
parent
 |
prev
 |
next

[10 more]

[flagged]
pjc50

3 hours ago

 |
root
 |
parent
 |
next

[–]

Imposing a policy on the whole internet in order to make it safer for children is like imposing a national 4mph speed limit on cars in order to make it safe for children to walk to school.

https://en.wikipedia.org/wiki/Red_flag_traffic_laws(personally I think there's a lot of non-sexual material which is bad for children but not covered by age verification, like Andrew Tate, but that's impossible to define or enforce)

reply

v3xro

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Oh no, maybe I should just be uhhh a responsible parent and not give my kids unlimited access to a browser instead of imposing a privacy nightmare on everyone else :)

reply

munksbeer

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

I hope you understand that every single work-around you see popping up is a result of your support of censorship and verification policy. *Your* support is going to push children onto more dangerous sites and expose their private browsing data to honeypots as they seek ways around this.

If my children were older, I would immediately be educating them on the dangers of this policy and of the dangers of seeking ways around it.I confess, as I type this, I have a lot of anger at the dangers you're putting children into.

reply

sksrbWgbfK

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Absence of parenting is a bigger threat than privacy. I accidentally agree with you, even if you're wrong.

reply

phatfish

3 hours ago

 |
root
 |
parent
 |
next

[–]

Parents don't follow their child 24/7. Society has a responsibility too. There is also the possibility of minors not knowing what they are clicking or kids with shitty parents destroying your hard work.

Another non-parent with an irrelevant opinion.

reply

cgriswald

20 minutes ago

 |
root
 |
parent
 |
next

[–]

I understand being a parent is scary and stressful. I wish I could tell you that goes away, but it doesn’t. However, your children, I hope, will spend far more of their lives as adults than as children and I think you should worry a lot more about what type of world you’re helping to create for them.

Raising children is not a risk free activity. Parents shouldn’t follow their children 24/7, even if they could. Your children, by accident AND through their own curiousity are going to be exposed to things you don’t think they are ready for. You can’t stop that, even in a perfect world. Prevent and delay it as best you can, sure, but the best protection is internal. Instill in them the ability to make good choices, build trust and confidence and be someone they can talk to about itwhenit happens.There’s nothing new here. Nothing special about the internet. Parents were saying the same thing about us when we were children and none of their controls were effective. We were still exposed to some things before we were ready. Those kids with shitty parents (and even the ones with good ones) are going to get around any such restrictions and expose your kids to things and your kids might expose them to things as well.Stop denigrating non-parents’ opinions. Not only do they have a stake in the situation but you seem to forget they were also children too. And before you write off my opinion the same way, my children are adults.

reply

easymodex

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Well I'm a parent and I disagree with you and agree with the other comments, what now?

reply

carlhjerpe

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Sounds like offloading bad parenting onto others, you're supposed to communicate with your kids about safety, there are solutions to restrict their devices to make the impulse control barrier higher.

If your kid goes out of their way to use a third party device without age restriction you can't stop them if they're determined either way, and no matter how right you think you are it still doesn't warrant destroying privacy for EVERYONE.

reply

corobo

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

Would be easier for everyone else if you parented your child in addition to raising them

reply

kaboomshebang

30 minutes ago

 |
prev
 |
next

[–]

On-topic: Seems like a good feature.

Off-topic: I've been reading some of the comments and I notice a bunch of HN-members are unhappy about their product. My experience: things never broke for me, never needed to contact support, ads are blocked, etc (But I also use uBlock, etc)(P.s. - My only complaint is that -- like so many other SaaS offerings -- administrating payments is not easy enough.
- No option to pay by year
- So every month you have to go the website, login, go the admin, click download invoice
- Instead of: click download PDF from monthly invoice email)

reply

haswell

25 minutes ago

 |
parent
 |
next

[–]

I’m also a happy customer.

Regarding payments, I pay yearly. At the time I signed up I think it was the only option. They do have a $1.99/month option now, but they still offer yearly pricing.

reply

slekker

28 minutes ago

 |
parent
 |
prev
 |
next

[–]

What? I pay by year

reply

skyzouwdev

13 hours ago

 |
prev
 |
next

[–]

That’s a bold move. Handing over IDs to random sites is definitely a privacy nightmare, so I get why you built this. The real question is whether it buys time for users or just accelerates the push for stricter regulation. Either way, it sparks an important conversation

reply

mrweasel

14 minutes ago

 |
parent
 |
next

[–]

The UK age verification seems to be "Upload your ID to a porn site", but that's not the EU solution from what I can tell. What the EU is building is an Identity Wallet, where your national online ID verifies your age with your wallet. The wallet can then tell the sites that yes, this person is in fact 16+ or whatever the age restriction is. How they plan to avoid having kids just borrow their parents phones I don't know, frequent reconfirmation maybe?

The mistake that UK, and probably others, have made is that the government isn't actually able to provide the required infrastructure.If the solution is anonymous in the sense that the government doesn't see that I visit some site, and the site doesn't see who I am, then I struggle to see problem. This assumes that it's only applied to services and products that are already age restricted in the physical world already.

reply

dlcarrier

12 hours ago

 |
parent
 |
prev
 |
next

[–]

At least outside of countries that already limit their citizens access to the internet, censorship regulations tend to apply only to providers, not end users, so it would be extremely difficult to go after an extraterritorial VPN provider. In the US, extraterritorial jurisdiction includes not just providers outside of the country, but providers outside of the state. For example, see:
https://en.wikipedia.org/wiki/Marquette_National_Bank_of_Min...
.

reply

echelon

12 hours ago

 |
parent
 |
prev
 |
next

[–]

> Handing over IDs to random sites is definitely a privacy nightmare

They just need to leak all of the elected official internet usage. You'll see this rolled back faster than it was implemented.I really can't wait for the video titles of the porn our government officials watch to be read out loud by newscasters. That's going to be such sweet karma.

reply

sitkack

6 hours ago

 |
root
 |
parent
 |
next

[–]

https://en.wikipedia.org/wiki/Bork_tapes

reply

bunnyfoofoo

6 hours ago

 |
prev
 |
next

[–]

Do not promote or use NextDNS, it's essentially abandoned. You will not get any support from the developer when something breaks, and it will break. I tried for a year to contact him before abandoning it. Just check the help forums.

reply

spiffotron

12 minutes ago

 |
parent
 |
next

[–]

I've used nextDNS for years but the past few weeks its been breaking websites left, right and centre so I gave up on it entirely. Everything feels much snappier since I dropped them for a different option too

reply

topato

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Considering this is a post from NextDNS themselves, showing off a NEW and awesome feature.... It doesn't seem abandoned? You don't seem to have even looked at the description lol

reply

bunnyfoofoo

5 hours ago

 |
root
 |
parent
 |
next

[–]

https://help.nextdns.io/search?v=p&q=refund

Congratulations to them, I suppose. They've temporarily returned after stealing money from me. Their service stopped working after renewing my annual subscription and when I went to try and find support, I got silence.If you're one of the lucky few who's never had issues with NextDNS, I'm happy for you.

reply

weird-eye-issue

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Just email billing@nextdns.io

reply

bunnyfoofoo

4 hours ago

 |
root
 |
parent
 |
next

[–]

They do not respond, to any email address. Tried multiple times, over months. Just check the forums. I provided a link in my other reply.

reply

weird-eye-issue

42 minutes ago

 |
root
 |
parent
 |
next

[–]

Your emails might be hitting their spam, this happens with my companies support address too so sometimes it will prevent a ticket from even being created

reply

import

5 hours ago

 |
prev
 |
next

[–]

Are you guys still active? I don’t remember how many of my questions went unanswered in the help forums, later switched to self hosted adguard.

reply

perihelions

16 hours ago

 |
prev
 |
next

[–]

As a remark, not a criticism, such a deliberate promotion is probably illegal in the UK market,

>"But Ofcom says platforms required to introduce "highly effective" methods to check user age must not host, share or permit content that encourages use of VPNs to get around age checks. The government has also told the BBC it would be illegal for platforms to do so."https://www.bbc.com/news/articles/cn72ydj70g5o

reply

MistahKoala

11 hours ago

 |
parent
 |
next

[–]

NextDNS isn't a content platform required to have age checks, so no, that prohibition doesn't apply here and promoting the bypass feature isn't 'probably illegal'.

reply

aydyn

5 hours ago

 |
root
 |
parent
 |
next

[–]

"Illegal" is only what the government will go after you for, and I very much doubt ofcom will see it your way.

reply

graemep

8 hours ago

 |
parent
 |
prev
 |
next

[–]

That only applies to those platforms that are required to do "highly effective age checks".

i.e. the top category of "harmful" site cannot point people to VPNs as a way to avoid age verification. Everyone else can tell people about VPNs as a way to avoid age verification. The media have been doing so for a start.

reply

petcat

13 hours ago

 |
parent
 |
prev
 |
next

[–]

> must not host, share or permit content that encourages use of VPNs to get around age checks. The government has also told the BBC it would be illegal for platforms to do so

Holy. Crap. I knew the UK was going off the deep end with these laws, but this actually looks like China-level government reach.

reply

Ms-J

12 hours ago

 |
root
 |
parent
 |
next

[–]

Ignore the government crying. It is irrelevant when we spread the tech to get around their useless spying laws.

reply

pas

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

next step is to try to make VPNs illegal (or require age verification for them, of course)

reply

zarzavat

6 hours ago

 |
root
 |
parent
 |
next

[–]

You need to introduce an invasive great firewall before you can effectively ban VPNs, since there's so many different ways to hide traffic.

Unlike banning porn, banning VPNs has no political value because the technically inept voters who support these age verification policies don't know what a VPN is.

reply

miki123211

5 hours ago

 |
root
 |
parent
 |
next

[–]

> You need to introduce an invasive great firewall before you can effectively ban VPNs

If you're China, yes. If you're a large and powerful western country, not so much.The way to do it would be through the concept of "data laundering." Just like the US does with money laundering, the government would publish a list of all organizations and individuals engaged in the practice. All companies operating in that country would need to (globally) sever all ties with everybody who is on the list. Everybody else could choose between doing the same or ending up on the list themselves.Only powerful countries could do this effectively, less powerful ones would just isolate themselves, just like China did. The US could definitely do it. The EU, UK, Japan and maybe India probably could, but it would be dicy. Everybody else would fail spectacularly.

reply

zarzavat

3 hours ago

 |
root
 |
parent
 |
next

[–]

UK prisons are almost full. The last thing the government needs is to jail every 14 year old who sets up wireguard for his friends.

reply

RiverCrochet

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

Age verification for VPNs would be awesome. I would rather hand ID over to a VPN provider than individual sites I visit.

reply

tacticus

10 hours ago

 |
root
 |
parent
 |
next

[–]

This would ensure you couldn't tie an Identity to an activity\user on a service which is of course why it's not where they're going

reply

lttlrck

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

The VPN provider should hook into the existing government identify service.

reply

walterbell

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Can VPN/DNS providers independently market their services, if content providers cannot advertise VPN providers?

reply

perihelions

15 hours ago

 |
root
 |
parent
 |
next

[–]

>
"content that encourages use of VPNs to get around age checks"

I think"...to get around age checks"is controlling. It isn't illegal to promote VPN's in that country; it's illegal to promote their usefulness in circumventing other laws.

reply

neilcj

15 hours ago

 |
root
 |
parent
 |
next

[–]

The law reads like it applies to platforms required to do the checks rather than third party service providers.

reply

JdeBP

8 hours ago

 |
root
 |
parent
 |
next

[–]

*
https://legislation.gov.uk/ukpga/2023/50/contents

Which section of the Online Safety Act 2023 is that in, please?

reply

thrown-0825

6 hours ago

 |
parent
 |
prev
 |
next

[–]

who cares, its a tiny market in a backwater economy.

reply

glitchcrab

4 hours ago

 |
root
 |
parent
 |
next

[–]

> Be kind. Don't be snarky. Converse curiously; don't cross-examine. Edit out swipes.

https://news.ycombinator.com/newsguidelines.html

reply

buyucu

15 hours ago

 |
parent
 |
prev
 |
next

[–]

For people who don't live in the UK, why should they care about UK law?

reply

ac29

13 hours ago

 |
root
 |
parent
 |
next

[–]

NextDNS is a company not a person. The have infrastructure in the UK and presumably have UK customers, so they should care about UK law.

reply

retype

12 hours ago

 |
root
 |
parent
 |
next

[–]

The US also has multiple states that have enacted similar laws.

reply

calgoo

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

Because the tech that is being implemented for the UK will now be available for any other country on request. Its one thing to try to force the companies to implement the solutions, its another to get your country added to the config of said implementation.

reply

rendaw

9 hours ago

 |
parent
 |
prev
 |
next

[–]

"Under no circumstances should you use Mullvad VPN (
https://mullvad.net/en
), available for 5Eur/mo - also payable in Bitcoin, to avoid our age verification checks!"

reply

syntaxing

16 hours ago

 |
prev
 |
next

[–]

Easily one of the best $20 I spend a year. Makes iOS so much more usable and I really love supporting the vision of the developers from NextDNS

reply

ethagnawl

5 hours ago

 |
parent
 |
next

[–]

Same here. I'd previously been using a Pi-Hole and Next is just so much simpler -- especially on the go.

reply

drcongo

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Same. I absolutely love NextDNS.

reply

skybrian

17 hours ago

 |
prev
 |
next

[–]

Glancing at the front page, it looks like this product also has enforced SafeSearch and restricted mode to protect children, so... seems fine? They're doing the same thing themselves, and it's probably better since it's a local solution.

If you're running a product like this, it should be officially allowed to bypass age verification.

reply

wizzwizz4

11 hours ago

 |
parent
 |
next

[–]

Arguably
, the UK's Online Safety Act already allows these products to bypass age verification: see s. 12(6)
https://www.legislation.gov.uk/ukpga/2023/50/section/12/6
):

> the age verification or age estimation must be of such a kind, and used in such a way, that it is highly effective at correctly determining whether or not a particular user is a childUnfortunately, it's hard to tell what this passage means, and I suspect it doesn't apply here. (But does that mean there'snolaw covering age-verification bypassing services? That seems like an unlikely oversight, and the Online Safety Act's badly-drafted enough that I'm not comfortable making a broad assertion here.) Hopefully case law sorts this out a little.

reply

pyuser583

14 hours ago

 |
prev
 |
next

[–]

I'm a parent, and I try to keep my kids from the Internet in general, but adult parts in particular.

VPN's are great for this. Just install the VPN, have it block access to adult sites, and have it alert me of any suspicious attempts.It's bewildering how VPN companies have branded their technology as "anti-censorship" and "privacy-focused." VPN's are a censor's best friend.DNS services are taking the opposite approach: they start by having a censorship feature (blocking malware, adult ads, etc), and now are adding anti-censorship options.There's nothing about connecting to a different network, or using a different DNS provider, that is anti-censorship.

reply

ronsor

14 hours ago

 |
parent
 |
next

[–]

> There's nothing about connecting to a different network, or using a different DNS provider, that is anti-censorship.

In a sense, it allows you to pick your censors, or no censors. "Anti-censorship" doesn't necessarily mean that nothing is blocked; it means you get to control what's blocked for yourself.

reply

pjc50

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Making your own filter choices should not be referred to as "censorship". Censorship is when the choice is taken away.

reply

pyuser583

6 hours ago

 |
root
 |
parent
 |
next

[–]

I'm taking the choice away from my kids.

reply

thaumasiotes

11 hours ago

 |
parent
 |
prev
 |
next

[–]

> VPN's are great for this. Just install the VPN, have it block access to adult sites, and have it alert me of any suspicious attempts.

> It's bewildering how VPN companies have branded their technology as "anti-censorship" and "privacy-focused." VPN's are a censor's best friend.You're already using a router. That's where you would normally implement blocks.A VPN necessarily does the same thing, and so you can implement routing blocks there too. But this is like saying that a virtual machine is a great technology to run software. OK. Why do you want a virtual one?

reply

bongodongobob

14 hours ago

 |
parent
 |
prev
 |
next

[–]

VPNs have nothing to do with it. I guess yours has some kind of filtering service, but that's not at all related to a VPN. It's like buying a V8 engine because you wanted a turbo. V8's can have turbos, but it has nothing to do with being a V8.

reply

AnonC

5 hours ago

 |
prev
 |
next

[–]

Sorry to get on to a related topic, since the NextDNS team may be looking at these comments. Is there any plan at all to revive the iOS app (last updated in 2020) so that the toggle in the app actually works? I don’t like installing a NextDNS profile because it doesn’t offer the flexibility to turn it off or on as needed. The app used to work pre-2020, but doesn’t now.

On my iPhone, at any given date and time, it’s just a random occurrence of whether NextDNS (with the app) works or not. Visiting test.nextdns.io may show “unconfigured” or a NextDNS endpoint.Various posts on the forums by several people over the years have not been responded to.I’d like to know if the team is ever going to work on this. If not, just remove the app from the App Store so that people don’t assume that it works when it doesn’t.

reply

karel-3d

4 hours ago

 |
prev
 |
next

[–]

How can this work? What is "DNS tricks"? DNS is just telling you where the site is?

edit: ah it spoofs the EDNS subnet for the DNS request, so it gives you server "intended" for a different location. You will get slower connection but if it's poorly implemented and they have geofencing just on that layer, it will not do the age verification stuff.It's interesting that it works, but... the website can still tell your IP through TCP handshake... it might fool some sites that have geofencing on DNS level.

reply

1vuio0pswjnm7

7 hours ago

 |
prev
 |
next

[–]

This sounds like a company using DNS to direct _other_ peoples' web traffic through _their_ proxies. Cloudflare started this way. That's why signing up for Cloudlfare requires using _Cloudflare's_ DNS servers

The so-called "DNS trick", which is defintely not a trick, is to redirect traffic though a proxy server. Whoever operates the proxy, e.g. Cloudflare, NextDNS, etc., has control over the HTTPS traffic and _could_ have access to the contentsHN commenters and other online commenters have criticised Cloudlfare in the past because it decrypts ("terminates") TLS connections and _could_ thereby have access to the contents of customers' trafficFor any doubters, this access was confimed some years ago when a coding mistake by someone at CF in a scanner generated with ragel caused customers'_decrypted_ web traffic contained in memory on Cloudflare's proxies to spill out all over the web. Leaked data became publicly available and remained discoverable via web search for a while; the data had to be scrubbed from search engines and web archives which took several days at leasthttps://en.wikipedia.org/wiki/CloudbleedNextDNS purports to be a "DNS service" but proxying HTTPS opens a new can of wormsNB. This comment is not claiming that NextDNS or anyone else does or does not do anything, nor that anyone will or won't do anything. This comment is about _what becomes possible through control over DNS_. The possibilities it allows for control are why I do not use third party DNS service and prefer to control own DNS; having control can be very useful

reply

buttocks

10 hours ago

 |
prev
 |
next

[–]

As a subscriber of NextDNS I say, first, this is cool, but second, don’t do it. I don’t want NextDNS to face some sort of judgment that will get it shut down. Just publish the “DNS tricks” so that people can DIY but don’t make it part of your service.

reply

nedt

49 minutes ago

 |
prev
 |
next

[–]

The age verification should be based on ISO 18013-5 mdocs and not even need a full ID. That would give you basically a "is over 18" flag signed by the state and not need anything in addition.

reply

rany_

11 hours ago

 |
prev
 |
next

[–]

How does this "DNS trick" work? That to me is a much more interesting detail.

reply

shitloadofbooks

11 hours ago

 |
parent
 |
next

[–]

It likely overrides DNS resolution to CDN/POPs in countries which don't require age checking, or routes the traffic through TCP proxies so your traffic appears to come from a different country without these laws.

This will increase the latency of all traffic to that site though.

reply

rany_

1 hour ago

 |
root
 |
parent
 |
next

[–]

I tried out NextDNS and this feature doesn't seem to work anyway. Enabling "Bypass Age Verification" has no effect. I tested it out on PornHub and XVideos.

I also can't find anything different in the returned A/AAAA records compared to my standard resolver.

reply

lelanthran

5 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> It likely overrides DNS resolution to CDN/POPs in countries which don't require age checking,

I don't understand what this means:1. It resolves DNS requests - got it.2. The resolution sends back an address to a CDN - okay, not sure that I got it3. The resolved address is in a country which doesn't require age checking - Totally don't get it: how will this help?

reply

selcuka

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

A DNS provider can not route your traffic through TCP proxies, so it must be the former.

reply

cluckindan

5 hours ago

 |
root
 |
parent
 |
next

[–]

Sure they can. When your browser resolves a host, they replace the actual IP with the IP of a proxy that is configured to forward traffic according to the Host HTTP header.

reply

okasaki

3 hours ago

 |
root
 |
parent
 |
next

[–]

You would have to install a certificate for that to work.

reply

aaronmdjones

3 hours ago

 |
root
 |
parent
 |
next

[–]

No you wouldn't.

The current situation:- You ask Foo DNS Provider for the IP address of pornhub.com- Foo DNS Provider responds with the real IP address- You connect to that address, send a TLS ClientHello containing a Server Name Indication extension of "pornhub.com"What could happen:- You ask Foo DNS Provider for the IP address of pornhub.com- Foo DNS Provider responds with one of their own IP addresses- You connect to that address, send a TLS ClientHello containing a Server Name Indication extension of "pornhub.com"- Foo DNS Provider now knows that you intend to connect there, so it connects there for you and relays your ClientHello to it- Foo DNS Provider then just acts as a dumb relay, passing everything back and forth with no modifications- The certificate verifies fine because the traffic was not modified and it was presented by the party who controls the corresponding private key- The website thinks you are connecting from Foo DNS Provider, not your real addressThe only thing that would break this is ECH (Encrypted ClientHello), currently supported only by CloudFlare and Google Chrome (and its derivatives) as far as I know. This security feature is provisioned with ... DNS records! So Foo DNS Provider can simply indicate that the records required for ECH do not exist, and your web browser wouldn't encrypt the ClientHello. It's already tampering with the responses to address lookups anyway, so DNSSEC wouldn't be an issue -- you simply would not expect to be able to validate anything.

reply

pkulak

13 hours ago

 |
prev
 |
next

[–]

That’s really cool. I thought you guys had stopped development altogether.

reply

tky

11 hours ago

 |
parent
 |
next

[–]

Same; I switched to ControlD when it appeared NextDNS was on autopilot without support or fixes.

reply

FiReaNG3L

15 hours ago

 |
prev
 |
next

[–]

Better than that at least in the UK, they are not handing the data to the government, but to unregulated, diverse third parties - what could go wrong.

reply

cedws

8 hours ago

 |
parent
 |
next

[–]

Free VPNs are also at the top of the UK App Store. All of them look extremely dodgy, probably ran by foreign adversaries seizing the opportunity to slurp data.

reply

OldfieldFund

11 hours ago

 |
parent
 |
prev
 |
next

[–]

it's all gonna get leaked every quarter

reply

cedws

8 hours ago

 |
prev
 |
next

[–]

I love NextDNS. Can you explain what exactly the DNS tricks are and where they do/don’t work?

reply

blissofbeing

4 hours ago

 |
prev
 |
next

[–]

If you are already building a proxy network to handle this can you please implement redirects? I would love to redirect x.com to xcancel.com by just setting my DNS. I would pay more for this feature.

reply

baby_souffle

14 hours ago

 |
prev
 |
next

[–]

> We’re curious how the HN community feels about this. Is it the right way to protect privacy online, or will it just provoke regulators to push harder?

Both. May the mouse forever elude the cat in this game!If you’re proxying all traffic, that’s going to get expensive and - in theory - makes you as easy to block as VPN providers. I wish you the best of luck!

reply

qwertox

7 hours ago

 |
prev
 |
next

[–]

I wish they would add a dropdown box where I can select English as the main language.

If they pretend they're a product targeted at anyone in the DACH region by offering the pages only in German, then they also must add an imprint: who they are, who is responsible, where they are, how I can contact them via email and phone.

reply

luxurytent

12 hours ago

 |
prev
 |
next

[–]

I don't have a strong opinion here, but I did want to say thank you for your service! I was previously running a pi-hole but switched my family and my household to NextDNS. Great $20/home spent

reply

Ms-J

12 hours ago

 |
prev
 |
next

[–]

Thank you for doing this! You are helping spread freedom. If everyone were to create more tools like this, it would shape the future to our liking.

reply

tester89

14 hours ago

 |
prev
 |
next

[–]

At least for my discord, I still can't access channels marked NSFW, instead of showing me the verification screen it just says "failed to load messages".

reply

wolfy1993

13 hours ago

 |
parent
 |
next

[–]

Likewise, unable to get it working myself (tested with reddit and bluesky - both ask for verification still).

Will be keeping an eye on this though, hopefully this can be an alternative to my Irish VPN in the future.

reply

atonse

9 hours ago

 |
prev
 |
next

[–]

I use NextDNS to BLOCK porn sites, etc from my kids’ devices. I hope you aren’t changing your ethos as a company, although I don’t know, maybe your customers are changing and causing you to pivot.

Because I don’t want any chance of this stuff affecting the blocks we use for minors, etc.

reply

lionkor

35 minutes ago

 |
parent
 |
next

[–]

Age verification doesn't protect minors, so I doubt their ethos changed.

reply

graemep

1 hour ago

 |
parent
 |
prev
 |
next

[–]

I doubt it will. It fits with what I hope is their ethos, which is to allow customers to decide what they want blocked for themselves and their households.

reply

paradox460

17 hours ago

 |
prev
 |
next

[–]

Where is the setting configured? I just looked through my admin page and didn't see any switch for it

reply

thewisenerd

17 hours ago

 |
parent
 |
next

[–]

i can see this in the settings page for a profile under the section "Bypass Age Verification"

https://my.nextdns.io/$id/settings

reply

Telemakhos

11 hours ago

 |
prev
 |
next

[–]

Does this create any new liability for the sites that are legally required to check ID?

reply

puppycodes

15 hours ago

 |
prev
 |
next

[–]

amazing... we need more of this on the dns level

reply

HocusLocus

11 hours ago

 |
prev
 |
next

[–]

Seeking DNS with 'furry exemption' for fully clothed furries.

reply

1a527dd5

16 hours ago

 |
prev
 |
next

[–]

I love you guys, even before this.

reply

j45

7 hours ago

 |
prev
 |
next

[–]

Handing over Government IDs to private websites and apps is a highly risky and attractive target for identity theft and fraud.

reply

mytailorisrich

12 hours ago

 |
prev
 |
next

[–]

Features that are only aimed at breaking the law will tend to backfire...

reply

Imustaskforhelp

16 hours ago

 |
prev
 |
next

[–]

I am a user of nextdns and okay, this is really neato team! I find this really interesting.

If I may ask, what are the dns tricks, is there a blog post about what you added, I am sooo curious about what sorcery is nextdns using.Edit: I searched on ddg and there was a ghacks.net link and a alternativeto.net article and sadly ghacks was taking a long time to load and I just read the alternativeto.net article and it was kinda cool, let me paste it herehere is the article link :https://alternativeto.net/news/2025/8/nextdns-rolls-out-new-...NextDNS has introduced a new DNS-level feature that allows users to bypass age verification checks commonly found on adult websites. This update enables users to avoid submitting personal documents, such as photos or government-issued IDs, to unfamiliar websites when accessing age-restricted content.To enable the feature, users can activate it directly within the NextDNS settings. The technical approach is straightforward: the DNS resolver intercepts requests to target websites and routes traffic through proxy servers in countries where age verification is not required by law. This means that while users visit the same websites, the sites perceive the traffic as originating from a country without mandatory ID checks.These changes are particularly relevant for individuals in the European Union and the United Kingdom, regions where certain governments have introduced strict ID requirements for accessing adult content websites. Looking at community reaction, user feedback on Reddit and social media has been largely positive since the announcement, with some users ironizing that “NextDNS developers know their clientele!”.---TLDR/my-thoughts: Nextdns can use something similar to vpn and I am wondering how much more efficient is this for this usecase compared to a vpn, like I am sure that vpns can be banned by a country, see china.But nextdns.io is still available in china?, how would that work, and so can this feature be actually expanded to make it a general purpose vpn too if need be but honestly a lot of vpn use cases might be for bypassing verification itself, so basically the only few use cases I can think of vpn is to bypass censorship and maybe verification and also changing vpn for lets say watching content that's available in other countryCan nextdns add other features too, like imagine you can use nextdns with netflix and change it to anime mode and you can get netflix as in of japan, I don't have netflix but I am just giving an example because that's a lot of times what I hear from all those youtube vpn shillsOr can they provide some vpn service itself while at it, and since nextdns still uses dns and dns can operate over https. I imagine that it might be even harder to detect such vpn traffic because I know for sure that some vpn's can be tracked implementation wise (as in wireguard)[i can be wrong, i usually am] but I am pretty sure that https can't be tracked in the same manner, and we can use dns over https in nextdns using this feature..Can you guys maybe comment on what you think about it? adding general purpose vpns / japan/country switching/enabling vpns itself though I guess it might make you a vpn app which can have its own logs/rules and regulations and I am currently fine/really happy with protonvpn which I also think can run on top of https with their proxy option atleast in browser and maybe even in their apps I am not sure.

reply

cricketsandmops

15 hours ago

 |
parent
 |
next

[–]

I've been using Getflix for years to have my location spoofed to another country. It is a pay product though. I've used it on Amazon and mainly use it for BBC Iplayer. I couldnt ever get netflix to play nice using it or a vpn, so for it I just tunnel to my traffic to a residential address i have in mexico

reply

cprecioso

14 hours ago

 |
parent
 |
prev
 |
next

[–]

IIRC there was this service called Tunlr which offered VPN-like location spoofing with similar DNS tricks.

reply

ignoramous

13 hours ago

 |
parent
 |
prev
 |
next

[–]

>
If I may ask, what are the dns tricks, is there a blog post about what you added, I am sooo curious about what sorcery is nextdns using.

It is likely they use some form of SNI-based proxy, similar to:https://github.com/celzero/midwayThe way this works is, for preset domains, you always answer with the IP of your SNI proxy, which then forwards the connection to the real IP based on the domain in TLS's SNI extension. This "trick" only works for TLS connections that send SNI in the clear, and will not work with QUIC (HTTP/3) or with TLS v1.3 with ECH (encrypted client hello). For non-TLS connections, like cleartext HTTP/2 or HTTP/1, the proxy would look at the Host header. Similar heuristics may exist for other popular cleartext protocols.ControlD, a similar DNS provider, has supported redirections for a long time now:https://controld.com/features/traffic-redirectionIf you own enough public IPs (like a /64 IPv6 or a /22 IPv4), you can vend time-limited unique IP per domain per client IP and support all transport protocols (and not just TLS/HTTP).

reply

combyn8tor

13 hours ago

 |
parent
 |
prev
 |
next

[–]

so does it work like this?:

- Client makes a DNS request to ageblockedsite.com using NextDNS server- NextDNS server returns an IP to a proxy server they control- Client connects to the site through the proxy server

reply

dizhn

12 hours ago

 |
root
 |
parent
 |
next

[–]

That's actually pretty neat. I thought they need software running on the client to do the proxying but this scheme doesn't need it.

reply

throwpoaster

15 hours ago

 |
prev
 |
next

[4 more]

[flagged]
can16358p

15 hours ago

 |
parent
 |
next

[–]

Speak for yourself please.

No one can dictate who can watch something or not.

reply

crooked-v

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Porn is just the excuse used to put more systems of control and oppression in place, as can be seen by US and UK conservatives attempting to get the mere existence of trans and LGBT people classified as 'obscene' and thus any mentions of them banned under the same laws.

reply

888632798

15 hours ago

 |
parent
 |
prev
 |
next

[–]

What would the regime do without people like you?

reply

ltbarcly3

14 hours ago

 |
prev

[–]

Presenting government ID to random entities is literally what government ID's exist for. Paranoia about this is silly.

Additionally, intentionally aiding someone (especially a minor) in circumventing the law is very likely to not be legal, especially when legality is largely determined by a jury, and especially^2 when the facts of the case against you are the most egregious that the government can find, especially^3 when you are profiting from it. It will be something like a 12yo using your service to access something absolutely shocking, and you or someone else will be forced to read a detailed text description of it in front of a jury. This doesn't even begin to address civil liability.I'm not saying what you are doing is 'wrong', I'm saying you should talk to a lawyer who specializes in this sort of thing before you are forced to.

reply

pas

13 hours ago

 |
parent
 |
next

[–]

showing a plastic card in a store to buy the yearly Cum Companion Calendar or whatever is one thing, because the clerk likely is not a savant with eidetic memory, whereas online there's this little thing happening called data processing which starts with the only thing we usually don't want with our ID. copying.

reply

HappMacDonald

7 hours ago

 |
root
 |
parent
 |
next

[–]

I wonder what the legality would be for the brick and mortar stores (especially the big chain ones) to just start asking customers for ID and then swiping them through scanners that can do all of the eidetic memory work for them?

reply

sitkack

6 hours ago

 |
root
 |
parent
 |
next

[–]

Kroger already does this, they will get sued for millions and millions of dollars when they have a data breach.

reply

Squeeeez

13 hours ago

 |
parent
 |
prev
 |
next

[–]

> Paranoia about this is silly.

Having had to deal with some clients with slightly sensitive data, I wish. Photocopies and printed screenshots lying around in the open, CC data copy-pasted manually to other fields or to generic excel sheets because otherwise "it disappears and we can't book late fees" etc.
Not even only the "random third-party" companies vetted and specialised in ID verification, but then they get a new support contract down the road, and a fourth- or fifth-party agent who had the cheapest offer now has remote admin access to those desktops.Probability is low, true. But all it takes is one compromised access.We all choose our battles probably.

reply

protocolture

13 hours ago

 |
parent
 |
prev
 |
next

[–]

>Presenting government ID to random entities is literally what government ID's exist for.

Wrong lmao. All forms of Government ID are PII and should be treated as sensitive.https://www.esafety.gov.au/young-people/protecting-your-iden...Heres basic information from a government looking to enact these same laws.>Nearly every app, social media platform or website asks you for at least some personally identifiable information. But this data can be stolen or misused. That’s why it’s important to keep it as private and secure as possible. If you have to share it, make sure it’s only used by trusted services with your knowledge and consent.Wow thats great advice.

reply

prism56

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Is it though? Unfortunately this could have been implemented much better with a decentralised approach.

Its not the showing the ID its having it potentially tied to your accounts and usage. Having your ID tied to your selfie which could be leaked.

reply

smallnix

14 hours ago

 |
parent
 |
prev

[–]

Please post a link to a picture of your national ID. /s

reply

ltbarcly3

11 hours ago

 |
root
 |
parent

[–]

I've had to upload my ID card to send money, open a bank account online, verify my identity for a dating app, book an international flight, and ironically to register for the app to have an electronic version of my id on my phone, and weirdly to pay a traffic ticket (why do they care who pays it?), get a discount on my Amazon Prime subscription, and finally to reset my password for my ID.me login for government websites. So all of those are 'fine' I guess, but god forbid you upload it to a third party verification service (the same one that was used for one or more of the above cases where I uploaded my id) to watch pornography, that's where we draw the line?

You are being absurd.I don't agree with this requirement, but I'm also not so dishonest that I would pretend that it's a security issue.

reply

jofla_net

10 hours ago

 |
root
 |
parent
 |
next

[–]

Its not the 'voluntary' services that may or may not want to see your ID, its the existence of any and all Mandatory legislation, which would be a nightmare.

This is a tech site so I imagine the average user has some deeper understanding than most(technically), but I guess imagination is off the table.What this would do (requiring all sites) is basically be the end for any and all attempts against identity fraud protection. Indulge a bit of imagination for a moment. If EVERY site is now required to do some form of verification, than everyone's infrastructure now becomes prime targets for PII and troves of identity information, and wherein amazon, banks, and ID.me can be considered to be at or near the top (i'd hope) for keeping their machines tied down, the reality is that EVERYONE'S servers ARE NOT so will maintained.
They WILL be attacked, and shims inserted to steal such identity information, as people have ZERO idea, as they're being shunted around to all thees angel-invested ID startups, as to what is or isn't legit, during signup. Wholly, identical pages/domains, as are often seen to steal traditional PCI information, will now be repurposed to this. Its not that the reputable ones are likely to fall, its the small vendors who don't understand that once a customer is EXPECTED to fork over ID to sign up, any hiccup in the process will be unnoticed, and it'll be ripe for abuse if the server/service is ever compromised.

reply

SoftTalker

8 hours ago

 |
root
 |
parent
 |
next

[–]

It would be a great thing, because it would finally force us to have somthing better than "I can present a piece of plastic with my picture and some numbers on it" as proof of identity.

reply

ltbarcly3

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

ID verification is done by 3rd parties. Nobody wants to hold a photo of your ID because it's a compliance nightmare. You aren't uploading your ID to some porn site, you are uploading it to some real-person verification company.

reply

HappMacDonald

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

So think through what you've just said.

If you were able to do all of those things to prove your identity using your ID.. then any identity thief with a copy of your ID could use it to impersonate you in every one of those venues.That means that somebody else can sendyourmoney wherever they wish.. create bank accounts to perform nefarious deeds that tie back to you.. book flights, and subscribe to services on your dime or on a stolen credit card behind your name so that after the chargebacks all debt collection activity aims at you. And finally convince the government to send your tax refunds to them.In light of this what is absurd about being parsimonious with who and how we share copies of our ID, and why should virtually every website online be deputized into keeping copies of them to provide dog standard content services thatmightnot always be suitable for all audiences?

reply

ltbarcly3

1 hour ago

 |
root
 |
parent
 |
next

[–]

Yea, I guess you thought through the fundamentals of security better than banks, payment providers, and governments. Well done.

reply

sitkack

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

Bro already has a disease, doesn't care if everyone else gets it too. What kind of argument is ... I already sent my ID all over the internet multiple times?

reply

scarface_74

11 hours ago

 |
root
 |
parent
 |
prev

[–]

You don’t see the difference between it getting out some place I travelled to, opened a bank account to, etc than if I visit grandmamidgetporn.com?

reply

ltbarcly3

8 hours ago

 |
root
 |
parent

[–]

Nobody uploads their ID to some porn site, they work with some reputable id verification company.

reply

scarface_74

7 hours ago

 |
root
 |
parent

[–]

Out of curiosity, I wanted to see how the five most popular porn sites handled age verification since I live in Florida. One of the states that require it. I started here (safe for work - just list of the most popular websites overall - not porn sites)

https://conversion.ag/blog/top-websites-in-the-world/Do any of these alternatives seem like something you would want to use?#10 doesn’t require any age verification.#12 doesn’t allow you to sign in at all unless you are a creator#14 no verification needed#25 requires you to use your Google or Twitter account or an email address.#61 requires you to log in with your Google account.#69 wants you to upload your drivers license or passport to a site calledhttps://saas-onboarding.incodesmile.com/multimedia214/flow/6...

reply

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

---
title: 'Do not add Google Play Integrity integration · eu-digital-identity-wallet/av-doc-technical-specification · Discussion #19 · GitHub'
url: https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/discussions/19
site_name: hackernews_api
content_file: hackernews_api-do-not-add-google-play-integrity-integration-eu-di
fetched_at: '2026-07-15T04:47:34.830687'
original_url: https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/discussions/19
author: roundabout-host
date: '2026-07-14'
description: Do not add Google Play Integrity integration
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 eu-digital-identity-wallet

 

/

av-doc-technical-specification

Public

* NotificationsYou must be signed in to change notification settings
* Fork7
* Star86

# Do not add Google Play Integrity integration#19

 Pinned

 TheLastProject
 

 
 started this conversation in
 
General

 Do not add Google Play Integrity integration
 

#19

 TheLastProject
 

Jul 16, 2025

·

 283 comments
 
·

 326 replies
 

Return to top

 

Discussion options

 

Quote reply

## TheLastProjectJul 16, 2025

 

-

In the README, the following is listed:

App and device verification based on Google Play Integrity API and Apple App Attestation

I would like to strongly urge to abandon this plan. Requiring a dependency on American tech giants for age verification further deepens the EU's dependency on America and the USA's control over the internet. Especially in the current political climate I hope I do not have to explain how undesirable and dangerous that is.

BetaWas this translation helpful?Give feedback.

 

260

 
You must be logged in to vote

 
👍

3314

 
 
👎

7

 
 
😄

1

 
 
🎉

2

 
 
😕

32

 
 
❤️

235

 
 
🚀

141

 
 
👀

5

 

 

All reactions

## Replies:283 comments·326 replies

 

Comment options

 

Quote reply

 

edited

### TheLastProjectJul 16, 2025Author

 

-

Furthermore I am surprised this is considered an important next step, given apps like the Dutch identity app Yivi (who has no such dependency) already existandcan be used for age verification by the government just fine (on the few select platforms that work with it). Yivi is even available on Open Source app stores like F-Droid.

I think Yivi's existence should be sufficient proof that Google Play Integrity integration is unnecessary.

Yivi (formerly IRMA) homepage:https://yivi.app/en/

BetaWas this translation helpful?Give feedback.

 

44

 
You must be logged in to vote

 
👍

903

 
 
❤️

1

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### thgoebelJul 16, 2025

 

-

This this seems to be a fork of the EUDI wallet, see also:

* Please remove the requirement for Google Play Integrityeudi-app-android-wallet-ui#287
* use the standard Android hardware attestation API to verify the device, OS and app instead enforcing licensing Google Mobile Serviceseudi-app-android-wallet-ui#390

BetaWas this translation helpful?Give feedback.

 

10

 
You must be logged in to vote

 
👍

227

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### duncan-bayneJul 16, 2025

 

-

In addition, tying age verification to specific operating systems and their vendors (large American tech companies) violates two of the three principles listed elsewhere in this org:

* made available to anyone who wants to use it
* controlled by users

BetaWas this translation helpful?Give feedback.

 

17

 
You must be logged in to vote

 
👍

646

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### duncan-bayneJul 16, 2025

 

-

Furthermore, fromhttps://ageverification.dev/Technical%20Specification/architecture-and-technical-specifications/#24-design-principles-

* Interoperability: The solution ensures seamless integration across diverse device operating systems, wallet applications, and online services.

Tying age verification to specific operating systems will directly violate this design principle.

BetaWas this translation helpful?Give feedback.

 

19

 
You must be logged in to vote

 
👍

503

 
 
❤️

10

 
 
🚀

35

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### k0nstructJul 16, 2025

 

-

Digital sovereignty is a necessary step to reduce the risks of data processing. There should be no dependencies for external services from third partiesat allsince each one adds a whole ecosystem of potential security issues.

BetaWas this translation helpful?Give feedback.

 

6

 
You must be logged in to vote

 
👍

301

 
 
🚀

24

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

 

edited

### orazioedoardoJul 17, 2025

 

-

This is insane, what's the threat model? Someone remotely exploiting a device to steal proof of age of majority just to watch p__n (most common use case)? Is it even realistic? Why does this service need an app at all? Just create a modern web app, maybe even leveraging Digital Credentials API. I'm tired of app-for-everything.

BetaWas this translation helpful?Give feedback.

 

10

 
You must be logged in to vote

 
👍

257

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

 

edited

### BoGnYJul 17, 2025

 

-

This happens because those who draft the technical specifications don't know how the technologies they propose work.

As I've explained elsewhere, this is ridiculous. Here's a brief excerpt from one of my posts elsewhere:

It's incredible that the European Commission sanctions Google for abuse of dominant position and asks to open the operating system to other stores to allow "free" competition and you [the writer of technical specifications] impose the use of tools that exclude the free choice of the user and give to Google all the power of choice, that's really INCREDIBLE...

There are dozens of ways to secure these apps' certificates without using proprietary systems.Not to mention that Play Integrity systems are 100% illegal.

BetaWas this translation helpful?Give feedback.

 

12

 
You must be logged in to vote

 
👍

215

 
 
😕

1

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### orazioedoardoJul 17, 2025

 

-

There are dozens of ways to secure these apps' certificates without using proprietary systems.

Does it need to protect those certificates at all? Maybe I'm too naive, but couldn't this simply be implemented by verifying random challenge signed by a national identity provider?

1. User goes to p__n website
2. Website detects user is visiting from Europe
3. Website downloads them a file containing a random string
4. Website tells them to visit verifyage.gov.example
5. User logs via identity provider and uploads the file
6. Challenge is signed and downloaded through the browser
7. User goes back to the p__n website and uploads the file
8. Website verifies the challenge is signed by a trusted entity

Avoids having to protect the signed challenge at all since it's single use, scheme is similar to authenticating with SSH or WebAuthn. I haven't checked the architecture thorough, perhaps does something similar in the end with more bloat in between.

BetaWas this translation helpful?Give feedback.

 

2

 
You must be logged in to vote

 
👍

74

 
 
👎

5

 

 

All reactions

 9 replies
 

 

 

Show 4 previous replies

 

Comment options

 

Quote reply

 

edited

#### feldim2425Sep 5, 2025

 

-

Perhaps the logical conclusion would be that strict age verification just isn't a useful thing to try, and instead parents should be encouraged to actually make use of the client-side filters that pretty much all smartphones have.I've made that argument here.

I agree, however given the people* currently see the internet helped by certain incidences (*cough* Roblox *cough*) I'm not very hopeful that this view will change in the near future. Maybe it could change once the system is implemented and fails horribly but that will take time.

* Note: With "people" I don't just mean politicians. I've heard this from clueless parents as well as people from the "I've nothing to hide"-crowd that truly believe there is no way this could ever go wrong.

BetaWas this translation helpful?Give feedback.

 
👍

1

 

 

All reactions

 

Comment options

 

Quote reply

#### nukeopSep 5, 2025

 

-

What the hell is a p__n website?

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### k8ieoneSep 5, 2025

 

-

Porn, pornography. I see no reason fo the self-censorship here.

BetaWas this translation helpful?Give feedback.

 
👍

4

 

 

All reactions

 

Comment options

 

Quote reply

#### lukefromdcSep 6, 2025

 

-

I was just following the format of the post I was originally responding to

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### k8ieoneSep 7, 2025

 

-

I know, I know. It wasn't aimed at you,@lukefromdc

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

 

edited

### andrew-ldJul 18, 2025

 

-

Please listen the ongoing issues with the Italian Wallet related to Play Integrity:

mega thread:pagopa/io-app#6327

Duplicates:pagopa/io-app#7014pagopa/io-app#7199pagopa/io-app#6942pagopa/io-app#6820pagopa/io-app#6763https://github.com/pagopa/io-app/issues/6507pagopa/io-app#6524

BetaWas this translation helpful?Give feedback.

 

4

 
You must be logged in to vote

 
👍

87

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### cucumberslumberJul 27, 2025

 

-

Fuck Google

BetaWas this translation helpful?Give feedback.

 

5

 
You must be logged in to vote

 
👍

26

 
 
👎

1

 
 
😕

3

 
 
❤️

180

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### BillCipher-exeJul 27, 2025

 

-

A mandatory Google account is unacceptable in a OSS Project

BetaWas this translation helpful?Give feedback.

 

10

 
You must be logged in to vote

 
👍

388

 
 
❤️

43

 

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### Kobaxidze256Jul 31, 2025

 

-

*FOSS

BetaWas this translation helpful?Give feedback.

 
👎

2

 

 

All reactions

 

Comment options

 

Quote reply

### DannyBoehJul 27, 2025

 

-

Getting access to a website as a EU citizen by accepting the TOS of EU-penalized American megacorp is peak 1984.

BetaWas this translation helpful?Give feedback.

 

8

 
You must be logged in to vote

 
👍

325

 
 
❤️

24

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### ksthieleJul 27, 2025

 

-

Besides the privacy issues, this feels like South Korea's IE6 problem back in the days, everything was so tied and dependent on it, that they couldn't get rid of it. But I guess we are just humans repeating mistakes, getting influenced by lobbyists, uninformed people, people who can't imagine how things will look like in 10 or more years

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 
👍

84

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### petervanstarkJul 27, 2025

 

-

This would be massive hinderance to all South EU states, where adoption of non google phones is large.

This would be also massive dependency on google.

Furthermore, why on earth are you building digital ids but then not doing IDPs, then forcing users to use some extra app for agecheck... they and their OS maintains...

It is bad UX, it causes issues, not sure if adds any security.

BetaWas this translation helpful?Give feedback.

 

2

 
You must be logged in to vote

 
👍

51

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### fuomag9Jul 27, 2025

 

-

I work in cybersecurity and this is a privacy and security nightmare. Just stop.

Using a EU-controlled website with national credentials like it is proposed here#18is the only reasonable solution.

Or maybe just do not implement this at all. People are going to go to p*** websites a way or another anyway.

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 
👍

98

 

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### SOglfJul 14, 2026

 

-

This is one sane response.

I will word it differently: if this cannot be implemented without hurtingA LOT OF PEOPLE, then maybe it should not be implemented to solve just one problem.Their solution is simply dangerous and will hurt a lot of people, additionally will destroy computing by turning it into a closed cage.

BetaWas this translation helpful?Give feedback.

 

All reactions

 253 hidden items
 

 Load more…
 

 

Comment options

 

Quote reply

### solodevelopingApr 3, 2026

 

-

Some articles people need to see about these people:

* THORN guy defends a rapisthttps://www.hollywoodreporter.com/news/general-news/ashton-kutcher-resigns-thorn-danny-masterson-letter-1235591856/
* More on THORN:https://www.jezebel.com/ashton-kutcher-thorn-sex-workers-1850852760
* Europol aske for unlimited access to data:https://balkaninsight.com/2023/09/29/europol-sought-unlimited-data-access-in-online-child-sexual-abuse-regulation/bi/
* Corruption scandal:https://balkaninsight.com/2023/09/25/who-benefits-inside-the-eus-fight-over-scanning-for-child-sex-content/uncategorized/
* THORN lies and probably harass sex workers:https://reason.com/2017/02/15/ashton-kutcher-plays-sex-worker-savior/

BetaWas this translation helpful?Give feedback.

 

2

 
You must be logged in to vote

 

All reactions

 11 replies
 

 

 

Show 6 previous replies

 

Comment options

 

Quote reply

#### solodevelopingApr 14, 2026

 

-

More here:https://investigativejournalismforeu.net/projects/the-data-trap/

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### solodevelopingApr 14, 2026

 

-

I mean, the whole thing is public knowledge

"Star of That ‘70s Show and a host of Hollywood hits, 45-year-old Kutcher resigned as chairman of the Thorn board in mid-September amid uproar over a letter he wrote to a judge in support of convicted rapist and fellow That ‘70s Show actor Danny Masterson, prior to his sentencing."

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### solodevelopingApr 14, 2026

 

-

https://www.europeanpressprize.com/article/the-eu-fight-against-child-pornography-stokes-fears-ofwidespread-online-surveillance-2/

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### solodevelopingApr 14, 2026

 

-

https://fortune.com/2023/09/26/thorn-ashton-kutcher-ylva-johansson-csam-csa-regulation-european-commission-encryption-privacy-surveillance/

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### solodevelopingApr 14, 2026

 

-

https://techcrunch.com/2024/01/10/eu-ombudsman-csam-thorn/

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### thomaswebbersApr 11, 2026

 

-

Did my comment about my 1984 comment getting removed really get removed??

Damn.

Tells me all I need to know.

BetaWas this translation helpful?Give feedback.

 

6

 
You must be logged in to vote

 
👍

2

 

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### solodevelopingApr 14, 2026

 

-

see no evil, hear no evil, speak no evil 😂

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### Secret-chestApr 11, 2026

 

-

# This is a measure to ban general computers. We will all be made to give up real computers and own a locked phone with telescreen features and censorship.

BetaWas this translation helpful?Give feedback.

 

8

 
You must be logged in to vote

 
👍

2

 
 
👎

3

 

 

All reactions

 2 replies
 

 

Comment options

 

Quote reply

#### Skorpion96Apr 11, 2026

 

-

Waiting for the EU to do an "universal bootloader unlock" law....

BetaWas this translation helpful?Give feedback.

 
👍

3

 

 

All reactions

 

Comment options

 

Quote reply

#### SOglfJul 14, 2026

 

-

That's exactly it. Just in a frog boiling mode.

Do not let boil yourself. Age checks today, locked hardware tomorrow. Australia ALREADY INCREASED FINES for bypassing age checks, next step will be a mandatory "locked hardware" to stop bypassing age checks. The UK ALREADY EXPANDED age checks from porn to "harmful content".

THEY WILL NOT STOP.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### akku1139Apr 11, 2026

 

-

Remember that EU actions, for better or worse, are imitated all over the world.

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### solodevelopingApr 14, 2026

 

-

It's more like all the politicians are corrupts and taking order from oligarchs and private lobbies

BetaWas this translation helpful?Give feedback.

 
❤️

1

 

 

All reactions

 

Comment options

 

Quote reply

### Secret-chestApr 15, 2026

 

-

If the concern is Russian farms offering automated ID verification for a cost, do note that this "security" can and will be spoofed, with a new method appearing almost a few days after the current one is patched. It will only hurt legitimate users.

BetaWas this translation helpful?Give feedback.

 

4

 
You must be logged in to vote

 

All reactions

 24 replies
 

 

 

Show 19 previous replies

 

Comment options

 

Quote reply

#### solodevelopingApr 15, 2026

 

-

Remember the goold old days where biometrics and creepy surveillance were seen as dystopian? 😂

Talking about effectiveness: the only way to make sure someone does not kill someone else is to cut his arm and legs, remove his teeth too, so this is probably what nukeop wants too

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### nukeopApr 15, 2026

 

-

That's actually what you want, you keep saying it's not effective enough.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### solodevelopingApr 15, 2026

 

-

My opinion is "fuck this shit"

A reason for that is "it will never work"

Another is "they're not doing it for "the kids""

BetaWas this translation helpful?Give feedback.

 
👍

8

 

 

All reactions

 

Comment options

 

Quote reply

#### Secret-chestApr 19, 2026

 

-

No, the idea is that it only hurts legitimate users who simply do not want Android or iOS, and it's not even effective against the ones it attempts to block (and no sane system can be). So the best way is not to have it.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### SOglfJul 14, 2026

 

-

There will be more sale points of verified accounts than you could ever imagine. With or without any attestation. What is more, EU already CREATED underground money for that. Congrats EU! If you want to build the biggest underground our world has seen, then you are on a right path.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### IdcrafterApr 15, 2026

 

-

WHy not use something like this?Unified Attestation??Single backend · Offline verification · No device IDsAttestation that feels boringly reliable.

Unified Attestation is a free, open-source alternative to Google Play Integrity. It delivers short-lived integrity tokens signed by a single backend, verified offline by app servers, and issued via a privileged Android system service. It can live alongside Play Integrity, and it’s simple to integrate for app developers on both the app and server sides.

An initiative by Volla Systeme GmbH.Volla Systeme GmbH is a Gemran based Company so European what means that this would make more sense as using a American controlled services that locks people into the Stock roms that can and will harvest data with no option to disable data harvesting, forced cloud account to install applications over the intended way and other anti features the EU doesn't stand for based on the Privacy regulation (i am just assuming and hoping here).

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 
👎

8

 

 

All reactions

 12 replies
 

 

 

Show 7 previous replies

 

Comment options

 

Quote reply

#### ProGamerGovApr 16, 2026

 

-

Unified Attestation has the same problems. It just puts a different group of companies in charge doing the same bullshit that play integrity does.

BetaWas this translation helpful?Give feedback.

 
👍

9

 

 

All reactions

 

Comment options

 

Quote reply

#### Secret-chestApr 19, 2026

 

-

there should be a fork that removes all Antifeatures like Play integirty and face scanning as that also requires api's that are only found in google play services or only work on vanilla play services device and don't or function worse on alternatives like microG.

There cannot be a fork. Paradoxically, the source is libre, but you can't modify it in practice, because it relies on some attestation to work and this is enforced by all parties.

BetaWas this translation helpful?Give feedback.

 
👎

1

 
 
😕

1

 

 

All reactions

 

Comment options

 

Quote reply

 

edited

#### vdbhb59Apr 19, 2026

 

-

The truth is that these people don't give a fuck about you and everything they do is for the single purpose of screwing you, and maybe make some profit along the way

Very true. Who gives a damn about user privacy, when they can make trillions and beyond fucking out of the data. Also, none of this is about helping a child stay away from p**n, rather, gaining full control over everything citizen does. Safety my foot.FYI: India already fucks with user privacy beyond imagination, and we Indians are so happy since we can spend 247365 behind facebook, instagram and shit.

BetaWas this translation helpful?Give feedback.

 
👍

3

 

 

All reactions

 

Comment options

 

Quote reply

#### nukeopApr 19, 2026

 

-

This isn't Tiktok, you don't have to self-censor words like "porn".

BetaWas this translation helpful?Give feedback.

 
😄

6

 

 

All reactions

 

Comment options

 

Quote reply

#### SOglfJul 14, 2026

 

-

Hardware owner has a full right to have full control over his own device and any data on it. Stop introducing elements which silently try to take the ownership away.If you want - RENT THE PHONES, then you can lock them and say those are yours and we are just renting them.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

 

edited

### Secret-chestJul 14, 2026

 

-

Whatever the "security measures", if a child wishes to access a restricted website, they can just... bribe someone into scanning the QR code on their behalf. It is not more secure with the "attestation". It only hurts legitimate users who want freedom.

BetaWas this translation helpful?Give feedback.

 

5

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### tdc-peterJul 14, 2026

 

-

Will it work on a Nokia 3310, or on my laptop? I don't own a smartphone.

BetaWas this translation helpful?Give feedback.

 

8

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### rubyFeedbackJul 14, 2026

 

-

A big problem I see here is that the EU commission requires peopleliving in the EU to submit to private US corporations. This kind ofundermines literally everything else - all the data privacy becomesinstantly nullified and void if the EU commission already hands overour data to other entities. We could simply dismiss the whole EUinfrastructure since Washington controls all policies in this regard.

Trump merely amplifies and extends this problem here, but theunderlying issue remains even with "friendlier" presidents incharge. In addition I kind of suspect that this is also a wantedoutcome by the EU commission anyway, for some reason, so Idon't hold only the USA responsible here. It takes two to tango.

Also, this attempts to require of everyone to have a smartphonein the first place. Which constitution mandated this ever?

BetaWas this translation helpful?Give feedback.

 

6

 
You must be logged in to vote

 

All reactions

 6 replies
 

 

 

Show 1 previous reply

 

Comment options

 

Quote reply

#### bbbhltzJul 14, 2026

 

-

@rubyFeedback

Also, this attempts to require of everyone to have a smartphone in the first place.

I'm not sure how this will work either. Perhaps a solution has been proposed and I just haven't seen anyone mention it? It also means they need a Google account (which I do not have...) and that the phone must be charged. Phone stipend I guess? Plus a yearly cheque from Google for all the data they harvest from me.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### CiroPenJul 14, 2026

 

-

public corporations, not private

Public only means that they arepublicly traded.In any case, a better descriptor for them in this context is that they are for-profit monopolistic foreign corporations.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### ogregoireJul 14, 2026

 

-

Actually those are public corporations, not private

In continental Europe, "public" means government-managed; "private" means non-government-managed. The English world considers everything from the monetary point of view. The rest of the world doesn't.

BetaWas this translation helpful?Give feedback.

 
👍

1

 

 

All reactions

 

Comment options

 

Quote reply

#### nukeopJul 14, 2026

 

-

That's not true at all. A public company is not a government-owned company, anywhere.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### ThomasHabetsJul 14, 2026

 

-

I don't think this issue is for debating the semantics of "public sector company" vs "public company". Maybe "take this offline", as the saying goes. From context it was clear what the commenter meant.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### joriswJul 14, 2026

 

-

In the README, the following is listed:

App and device verification based on Google Play Integrity API and Apple App Attestation

No, there's not.

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### SOglfJul 14, 2026

 

-

Stop hardware attestation at all cost. This is the final warning, if you keep ignoring it, age verification will be a small inconvenience compared to the nightmare which any "attestation" brings.

WAKE UP PEOPLE BEFORE IT'S TOO LATE

You will literally destroy computing if you agree to any "attestation".I will personally smuggle and sell "illegal" cracked hardware and radios if it comes to this. And worse.

DO NOT AGREE TO THEIR DEMANDS, DO NOT NEGOTIATE WITH TERRORISTS. DO NOT USE HARDWARE ATTESTATION AND AGE CHECKS.

BetaWas this translation helpful?Give feedback.

 

11

 
You must be logged in to vote

 
❤️

2

 

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### MikaelUmaNJul 14, 2026

 

-

It is simple silly to tie anything governmental to specific technologies. It should be based on open standards anyone can implement and integrate with.

BetaWas this translation helpful?Give feedback.

 

5

 
You must be logged in to vote

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

 

edited

#### ell1eJul 14, 2026

 

-

The German implementers currently don't even plan to offer a reproducible build, as far as I can tell:https://gitlab.opencode.de/bmi/eudi-wallet/wallet-development-documentation-public/-/work_items/4#note_735094Pretty disastrous and sad.

This seems to be in part due to the OWASP guidelines that the EU somehow thinks are good:https://mas.owasp.org/MASVS/11-MASVS-RESILIENCE/I brought up some criticism here:OWASP/masvs#757But the debate is still ongoing...

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### TimZwartJul 14, 2026

 

-

I dont believe in age verification at all. Its some more east german stasi bs. Where is freedom? Every youngster will probably go to tor or whatever to access a social network is that what we want? While they are at it they might get up to slightly more nefarious dark web things like ordering a hit on their teach.

BetaWas this translation helpful?Give feedback.

 

2

 
You must be logged in to vote

 

All reactions

 2 replies
 

 

Comment options

 

Quote reply

#### ell1eJul 14, 2026

 

-

Seems like a relevant text:https://gitlab.opencode.de/bmi/eudi-wallet/wallet-development-documentation-public/-/work_items/13Perhaps worth linking to others.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### nalekberovJul 14, 2026

 

-

They are doing their part helping youngsters get comfortable with dark web.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

 

edited

### wpwpwpwpwJul 14, 2026

 

-

I have neither google nor apple software. Will I be unable to use a myriad of online services if I don't bow and give my money and my data to American corporations? Another shot in the foot, as usual.

BetaWas this translation helpful?Give feedback.

 

3

 
You must be logged in to vote

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### ell1eJul 14, 2026

 

-

Currently, in some countries like Germany the answer according to latest plans seems to be yes:https://gitlab.opencode.de/bmi/eudi-wallet/wallet-development-documentation-public/-/work_items/10

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### nalekberovJul 14, 2026

 

-

Fuck age verification and any kind of ID check online.

If you support this, you might as well be okay with US tech dependency; the EU is not ruled by angels. If you think otherwise, you have been brainwashed by EU technocrats.

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment
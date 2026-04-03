---
title: Apple Will Push Out Rare ‘Backported’ Patches to Protect iOS 18 Users From DarkSword Hacking Tool | WIRED
url: https://www.wired.com/story/apple-will-push-out-rare-backported-patches-to-protect-ios-18-users-from-darksword-hacking-tool/
site_name: newsfeed
content_file: newsfeed-apple-will-push-out-rare-backported-patches-to-pro
fetched_at: '2026-04-02T01:01:45.378949'
original_url: https://www.wired.com/story/apple-will-push-out-rare-backported-patches-to-protect-ios-18-users-from-darksword-hacking-tool/
author: Andy Greenberg
date: '2026-04-01'
published_date: '2026-04-01T00:49:08.663Z'
description: As DarkSword spreads, Apple tells WIRED it will enable iOS 18-specific fixes for millions of iPhone owners who remain on that iOS version rather than force them to update to iOS 26.
tags:
- wired
- security
- security / cyberattacks and hacks
- security / security news
---

Save Story
Save this story
Save Story
Save this story

When it comestoiOS,Applehas largely maintained a take-it-or-leave-it approach to security updates. Want the software patches Apple creates to fix the vulnerabilities exploited by hackers to compromise iPhones? Then the company would tell you to update your phone to the latest version of iOS your hardware can handle—with no room for lingering on an older version just because you enjoy its retro look or familiar features.

Now, however, the appearance of not one but two sophisticated, in-the-wild iPhone hacking techniques in a single month—and some iPhone owners’distaste for the look and feel of the latest version of iOS—may have finally shifted Apple’s patching policy. For the second time in just a few weeks, Apple is responding to the spread of a hacking tool by pushing out patches for older versions of iOS—and in the latest case, even for phones that have the capability to upgrade to its most recent version.

An Apple spokesperson tells WIRED that the company will issue software updates on Wednesday morning to protect iOS users from ahacking technique known as DarkSword, which is capable of silently taking over certain iPhones running iOS 18—the previous version of Apple’s mobile operating system—when they visit a website infected with the malicious code. Users of Apple’s latest iOS version released in September, iOS 26, were already protected against DarkSword. But the new patch push is designed to specifically protect vulnerable iOS 18 users who have so far resisted updating to iOS 26.

Apple’s move to allow iOS 18 users to patch their devices without updating to its latest operating system version—a practice of protecting an older operating system version that the cybersecurity industry calls “backporting” a patch—marks a surprising pivot for Apple. When researchers at Google and cybersecurity firms iVerify and Lookout revealed DarkSword nearly two weeks ago, Apple released iOS 18-specific patches only for older devices whose hardware was incompatible with iOS 26, and recommended all other users update to its most recent OS version.

Given that as many as a quarter of all iPhone users remained on iOS 18 as of February—and many of those users have consciously chosen not to upgrade to iOS 26 because of the unpopularity of its features likeApple's new “liquid glass” interface—that left many millions of holdouts facing a dilemma between their software preferences and their security.

Apple now appears to be changing its position in an effort to protect those holdouts. “Tomorrow we are enabling the availability of an iOS 18 update for more devices so users with auto-update enabled can automatically receive important security protections,” an Apple spokesperson wrote in a statement to WIRED. “We encourage all users with supported devices to update to iOS 26 to receive our most advanced protections.”

Users of iOS 18 who have auto-update turned on will automatically receive the version of iOS 18 that’s patched against DarkSword, while those who don’t have auto-update enabled will have the option to update to either the latest, patched version of iOS 18 or to iOS 26.

Criticism of Apple's lack of backported patches for iOS 18 had grown over the past two weeks, as DarkSword proliferated among hacker groups that have used the tool for everything from espionage to cryptocurrency theft.According to Google, DarkSword has been used by various hacker groups to break into the iPhones of users in Malaysia, Saudi Arabia, Turkey, and Ukraine. In at least some instances, the code was left in a fully reusable state on the legitimate websites that had been compromised by hackers to carry out DarkSword's intrusions, complete with helpful comments from its developer about how it worked, all making the tool easy to repurpose for any hacker that finds it.

Last week, DarkSword was thenposted to open source code repository GitHub, making it all the more accessible. Security firms Malfors and Proofpoint soon after warned that another Russian hacker group linked to the Kremlin's FSB intelligence agency was sending out phishing emails that used the technique. Independent security researcher Johnny Franks tells WIRED that he found yet another new, active domain—a fake website written in English, capable of infecting US-based users—that was part of a DarkSword hacking campaign as late as Thursday of last week, a finding confirmed by mobile security firm iVerify.

Despite DarkSword’s growing threat to iOS 18 users, many stubbornly refused to update to iOS 26. On Reddit channels related to cybersecurity and iOS, some self-identified iPhone owners discussing DarkSword argued that Apple seemed to be taking advantage of the DarkSword hacking campaigns to push them onto its latest OS version, which some havefound to be slow or overly animated.

“Apple is trying to force you onto the dumpster fire that is liquid glass,” one Reddit user wrote.

“If this is so serious, why wouldn't Apple insert a fix into iOS 18.x," another Redditor named asked.

“It's all bullshit propaganda!” another user wrote. “Not updating my phone is perfect on iOS 18.1.1."

For cybersecurity experts who have been waiting for Apple to act, the company’s move to now cater to those stubborn iOS 18 users received “better-late-than-never” reviews. “Apple is now, finally, doing this for the DarkSword exploits, but only after they were already being abused by other attackers, putting iOS users at risk,” says Patrick Wardle, a former NSA hacker and now the CEO of the Apple-device-focused security firm DoubleYou. “If protecting users actually matters, backporting critical fixes should be standard, not the exception.”

DarkSword is, in fact, the second sophisticated, in-the-wild iPhone hacking technique in just the last month that’s inspired Apple to take the rare step of pushing out fixes for older versions of iOS. Earlier in March, the company also backported patches to protect users from a different, even more sophisticated iOS hacking toolkitknown as Coruna. A week after researchers at Google and iVerify revealed that the Coruna iOS exploitation kit—which was likely created for the US government—had spread from Russian espionage hackers to profit-focused cybercriminals, Apple released security fixes for iOS 17, the even older version of Apple's mobile operating system that was vulnerable to Coruna’s set of hacking techniques.

DarkSword's ability to compromise iOS 18 devices, however, left a different set of users vulnerable. Rocky Cole, cofounder of iVerify, notes that some of those users may have held out on updating to iOS 26 until now not simply because they don’t like its features but because they use specific or custom-made apps that aren't compatible with newer operating systems. In the UK, Apple has alsoadded age verificationfeatures to iOS 26 that some users have resisted. Others may simply not have had enough storage space on their phone to carry out the update.

“Apple left a very large number of people vulnerable for a pretty long time,” Cole says of the two weeks it’s taken the company to push out the new fixes. “As to why they didn't backport fixes until now, I don't know. This is a severe enough problem that it merited doing it.”

Apple's historic practice of avoiding patching older versions of iOS may have escaped controversy, Cole argues, only because iOS hacking techniques have rarely spread as widely and publicly as DarkSword and Coruna. Apple has long described iPhone hacking as a rare phenomenon carried out by sophisticated hackers targeting small numbers of high-risk users. But DarkSword's appearance, especially coming on the heels of a similarly dangerous hacking toolkit revealed earlier the same month, has forced Apple and the people who use its products to reckon with the fact that iOS's security features haven't made them immune from intrusion—and to consider the trade-offs of protecting them.

“There are people out there who are, for one reason or another, unwilling or unable to use the latest version of iOS,” says Cole. If insisting that users update to that most recent operating system is Apple’s only security strategy, he says, “there are going to be a very large number of iPhone users exposed to these increasingly pervasive and severe attacks.”

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Will Knight'sAI Labexplores advances in AI
* ‘Flying cars’will take off this summer
* Big Story:InsideOpenAI’s raceto catch up to Claude Code
* How‘Handala’became the face of Iran’s hacker counterattacks
* Listen:Nvidia’s ‘Super Bowl of AI,’ and Tesla disappoints
Andy Greenberg
 is a senior writer for WIRED covering hacking, cybersecurity, and surveillance. He’s the author of the books 
Tracers in the Dark: The Global Hunt for the Crime Lords of Cryptocurrency
 and 
Sandworm: A New Era of Cyberwar and the Hunt for the Kremlin's Most Dangerous Hackers
. His books ... 
Read More
Senior Writer
* X
Topics
apple
ios
iPhone
hacks
malware
Russia
hacking
cybersecurity
Everything You Should and Shouldn’t Do When Building an Outdoor Sauna
Putting together a relaxing backyard retreat is not always as simple as you might think.
Adrienne So
Watching a 7.5-Hour Movie in Theaters Made Me More Hopeful About Our Collective Brain Rot
Sátántango
 is considered a holy rite for hardcore cinephiles. It also helped me confront my dwindling attention span.
John Semley
These Are the 4 Artemis II Astronauts Leading the Historic Return to the Moon
The Artemis II mission crew includes the first woman, the first Black person, and the first non-American astronaut to travel to the lunar environment.
Fernanda González
Taylor Lorenz’s Screen Time Is Almost 17 Hours a Day
The extremely online journalist and content creator doesn’t believe in tech hygiene and yearns for a world where “inbox infinity” is celebrated.
Alana Hope Levinson 
I Asked ChatGPT What WIRED’s Reviewers Recommend—Its Answers Were All Wrong
Want to know what our reviewers have actually tested and picked as the best TVs, headphones, and laptops? Ask ChatGPT, and it'll give you the wrong answers.
Reece Rogers
The Best Babbel Promo Codes and Deals for April 2026
Master a new language with expert-led courses. Use our verified Babbel coupon codes to save up to 65% on student plans and 60% on 6-month subscriptions.
Molly Higgins
Robotaxi Outage in China Leaves Passengers Stranded on Highways
A suspected system failure froze Baidu’s robotaxis across Wuhan, trapping passengers and reportedly causing traffic disruptions and crashes.
Zeyi Yang
Apple Will Push Out Rare ‘Backported’ Patches to Protect iOS 18 Users From DarkSword Hacking Tool
As DarkSword spreads, Apple tells WIRED it will enable iOS 18-specific fixes for millions of iPhone owners who remain on that iOS version rather than force them to update to iOS 26.
Andy Greenberg
Artemis II Countdown: How and When to Watch the Launch
Here’s everything you need to know about the Artemis II mission, the long-awaited (and long-delayed) human return to the moon.
Jorge Garay
Iran Threatens to Start Attacking Major US Tech Firms on April 1
Tech giants like Apple, Google, and Microsoft are among those on a target list released by Iran’s Islamic Revolutionary Guard Corps.
Louise Matsakis
Our Favorite Affordable Air Purifier Is Temporarily Even More Affordable
Amazon has the Coway Airmega Mighty marked down to two-thirds its normal price.
Brad Bourque
Google Now Lets You Change Your Gmail Address. Here’s How
You’ve probably had the same Gmail address for years. Now, it’s easy to make a name change without worrying about the transition.
Reece Rogers
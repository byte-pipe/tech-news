---
title: A Hacker Targeted High-Stakes Poker Players With Malware That Exposed Their Cards | WIRED
url: https://www.wired.com/story/a-hacker-targeted-high-stakes-poker-players-with-malware-that-exposed-their-cards/
site_name: newsfeed
content_file: newsfeed-a-hacker-targeted-high-stakes-poker-players-with-m
fetched_at: '2026-10-30T12:47:38.626107'
original_url: https://www.wired.com/story/a-hacker-targeted-high-stakes-poker-players-with-malware-that-exposed-their-cards/
author: Ben Dowsett
date: '2026-10-29'
published_date: '2026-10-29T10:30:00.000Z'
description: Illicit software on the computers of some of the world’s best online poker players allowed the accused cheater to see what cards were in the victims’ hands—and trounce them at the tables.
tags:
- wired
- security
- security / cyberattacks and hacks
- poker
---

Save Story
Save this story
Save Story
Save this story

In a fittingsign of the times, the hacker’s carefully laid plans were foiled by anAI agent.

It was September 25, 2026, and Alex, a professional online poker player, was using hisClaudeAI agent to review some play statistics. (Alex only agreed to speak with WIRED under a pseudonym to avoid any risk of reprisals from threat actors.) After Alex’s SQL database crashed and needed to be reset, the Claude agent noticed something suspicious: A program called MeshAgent was operating in the background, where it seemed to be capable of capturing Alex’s screen and even controlling his entire machine.

Thanks to the Claude agent’s report, Alex could see the program had been installed on April 24, and not by Alex himself. Alex says the agent identified 11 time-stamped events when the program had been capturing his screen based on graphic errors it caused during screen sharing instances. During all 11, Alex had been playing a session onACR, also called Americas Cardroom, a major worldwideonline pokeroperator.

He checked his hand histories and quickly found the most troubling info yet: The same opponent, playing under the handle OxOO, was at his table for 10 of those 11 sessions.

The handle was familiar. Alex and several friends in the high-stakes community had shared suspicions about this player’s behavior in the past. Alex checked the player’s win rate stats via a public tracking site; they were astronomically higher than the best players in the world, a statistical impossibility given the sample of hands played. In Alex’s view, it was glaringly obvious that this player was cheating.

An investigation by Alex and other members of the high-stakes community in subsequent days confirmed his fears—and then some. Alex was one of hundreds of players allegedly targeted with this type ofmalwareby the same reported threat actor across a period of multiple years. Alex, who was the first to discover MeshAgent on his computer, claims he was “only” ripped off for around $30,000, a relatively moderate sum for the level he plays at; many of his peers weren’t so lucky.

With millions of dollars allegedly stolen across the biggest sites on the internet, the poker world is searching for answers about how the scheme was allowed to continue so long, whether major sites took the risk seriously after it was reported, and whether online poker itself has been irreversibly compromised.

Poker has neverbeen short on cheating controversies; online poker especially so. The “superuser” method, in which a cheater gains unauthorized access to their opponents’ cards and can therefore act with perfect information against them, was one of the first to show up online.

Two major sites in online poker’s early days, Absolute Poker and Ultimate Bet, served ascautionary talesin the mid-2000s. In separate instances, superuser cheaters were able to gain insider access to the websites and bilk players for millions of dollars. (Much of the loot was refunded to players following an investigation.) Those high-profile incidents led to tightened security measures from many top poker sites.

Another minor superuser incident took place in 2013, when a Finnish high-stakes playersaid his laptop had been stolenfrom his hotel room during a European Poker Tour tournament in Barcelona. When the laptop was recovered, it had been infected with malware that allowed a hacker to view his screen remotely. And maybe themost famoussuperuser scandal of all took place on the live felt: In a story that made it all the way toSportsCenter, a player named Mike Postle was accused of stealing over $250,000 from livestreamed games at Stones Gambling Hall in 2018 and 2019 with the aid of what observers believed to be an alleged accomplice with access to live card data who fed information to Postle’s phone. (Postle denied the accusations, alleging it was “fake news.”)

Outsideone relatively small(and quickly remedied) incident in 2023, though, the online poker world had gone years without a confirmed superuser incident—until now. And some of what’s known about this latest attempt signals a savvier threat actor than in previous scandals, plus a degree of patience not typically seen in attacks like these.

“Traditionally, when you see these types of financially motivated threat actors, they will get access to a system and then as soon as they’re on it, they’ll do a scope of what they have access to and then they’ll hit everyone all at once and dump all the wallets,” says WolfSec, a cybersecurity professional who consults with many high-stakes poker players on security measures. He was first to break the news of the MeshAgent scam on September 29,on his X account. (WolfSec agreed to speak to WIRED under the condition his real name not be used out of fears of reprisals from hackers; WIRED independently confirmed his credentials as a cybersecurity expert.)

But this hacker didn’t do any of that, despite many of these players having large cryptocurrency holdings and other investments accessible on their machines. The attacker seemed instead to be performing advanced reconnaissance. In fact, WolfSec believes the same threat actor was attempting to attack players’ machines as early as 2022 using a more basic technique; because no known funds were stolen at the time, no other action was taken once the players wiped the malware from their computers.

It appears, though, that the hacker was simply biding his time and improving his methods in preparation for an eventual strike.

Instead of targeting individual players directly, this more recent attack involved third-party software programs calledIntuitiveTablesandJurojin. These programs allow professionals to play dozens of online poker hands at once. Using these popular “multi-table” tools, players can switch between live games with a keystroke, place bets or make plays with hot keys, and other actions that make it easier to play at several virtual tables at the same time. The hacker compromised both applications, WolfSec says, pushing malicious software to over a thousand estimated users.

In the case of Jurojin, the attacker gained access to the developer’s own system for software updates and was able to deliver the remote-access agent to existing users through normal, automatic updates.

The developer of Intuitive Tables was running Jurojin on their test computer, and that machine got the remote-access agent as part of Jurojin’s compromised software update. Using the agent, the attacker added malicious code to the Intuitive Tables application before the developer signed the security certificate for an updated build of the app. That version carrying the malicious code was posted to the Intuitive Tables website as a public download, and everyone who installed that version of the app unknowingly also installed a backdoor on their computer.

In both instances, the malicious code was delivered through a standard update channel or an official release, so neither the users nor their antivirus apps detected anything amiss.

The modified version of Intuitive Tables behaved exactly like the clean version, with one exception: It also checked players’ files for their usernames.

“If you were on a hard-coded list that was stored on the attacker’s infrastructure, which [the malware] reached out to and downloaded and compared your username to, then it acted as a malicious program and downloaded additional malicious files,” WolfSec says. “If you weren’t on that list, then it became the normal program and didn’t do anything malicious at all.”

The list appears to have been populated primarily with regular high-stakes players across several sites. All of the players on the list appear to have had the MeshAgent program installed covertly on their machines. The hacker was ready to pounce.

In early 2025,a couple of new players began frequenting high-stakes games—one on ACR (using the handle “JackKlompus”) and another major global site called CoinPoker (handle: “Europe”). Strangely, despite not being familiar to other regulars in these games, the players refused to identify themselves in table chats, a common request that’s typically granted by new players in high-stakes poker. The new opponents were also winning with improbable frequency. (Later, once the pros started sharing information about their games, it was pieced together that these players were the same person.)

Mike, a professional poker player who spoke to WIRED using a pseudonym due to fear of reprisals from hackers, played on both sites at the time and was at tables with the player using these handles. Mike says at first he wondered if the mystery player’s success was somehow explainable. Maybe they were doing something new that Mike and his fellow pros just hadn’t figured out.

“You could kind of excuse it” at first, Mike says. “Maybe this guy is really, really good or something.”

As the number of winning hands grew, though, Mike and several high-stakes friends became more suspicious. They initially suspected that the player was using real-time assistance via game-theory-based engines that outperform the best human players. Real-time assistance is banned across major sites, but is difficult to police perfectly and is something pros are regularly watching out for. Mike mostly stopped playing at tables with the mystery player, as a precaution.

Like WolfSec, Mike reflects on a relative level of skill and discipline employed by this player during those 2025 sessions, especially compared to other known cheaters in poker history. The account generally used standard bet sizes and played normal hand ranges. Its session-by-session play never raised too many eyebrows; only the account’s win rate over time drew scrutiny.

But in June 2026, Mike played a two-hour heads-up (one-on-one) session on a different site, ClubWPT Gold, which he’d later determine—following reviews with the website’s security team—came against the same player from the 2025 sessions. The player used a different handle to evade detection, so Mike didn’t see a reason to be extra cautious. The opponent simply steamrolled Mike, making every correct decision even in seemingly impossible spots—almost like he could see Mike’s cards. “It was very blatant,” Mike says.

Immediately after the session, Mike messaged several friends in the high-stakes world to say he thought he’d been cheated.

Turns out he was right. When word of the hack broke publicly on WolfSec’s X account, ClubWPT Gold investigated. The site banned the account Mike had played against and refunded him for his losses, says Randy Lundy, head of customer operations for ClubWPT Gold.

This alleged cheater’s presence in online circles was an open secret across the community by this point. In fact, Mario Mosböck, a poker ambassador for CoinPoker who was authorized to speak about the company’s response to the hack, says the site began investigating this player as early as 2025, banning them and refunding over $100,000 in allegedly stolen funds to affected players. (Mosböck says the return of funds was delayed several months because the alleged cheater appealed the confiscation to regulators.) The player’s simple win rate and play style statistics appeared to be evidence of malfeasance, even if the site couldn’t definitively determine how the cheating was happening.

How, then, was the same alleged cheater allowed to keep ripping off players like Alex and Mike on multiple other supposedly reputable sites more than a year later?

“They confirmed multipletimes that they looked at my report, but for whatever reason they didn't act on it,” says Patrick Howard, a professional poker player and founder of the coaching company Mobius Poker.

The “they” he’s referring to is GGPoker, arguably the most well-known site in the world for non-US players. Howard says he submitted a report to the site in early September 2026, weeks before the MeshAgent hack became public, highlighting the alleged cheater’s unusual play and urging the site to investigate.

“I found multiple three- to four-standard-deviation outliers,” Howard says, and that was across a limited hand history sample sent to him by friends and clients. He sent his findings to the GGPoker team but received no response. He got a reply only after WolfSec’s public reveal of the hack on X, with the site telling him there “wasn’t conclusive evidence” to act at the time of his complaint.

Various online poker sites handled the incident differently. Players have largely praised CoinPoker for proactively banning the player based on win rate and play tendencies alone, which are accepted as definitive indicators of cheating at stakes this high and with samples this large; while ClubWPT Gold only seems to have been impacted later in the scheme, that site also appears to have acted decisively upon discovering it.

But the hacker remained active on GGPoker and ACR until late September, allegedly stealing between $1.5 million and $4 million, based on the estimates of the sources WIRED spoke to for this story.

“Players are frustrated, because they had been reporting this for a year,” says John Andress, head of game integrity for A5 Labs, a cybersecurity platform that provides anti-cheating services to ClubWPT Gold and other brands. “A few of the platforms just completely ignored them.”

This was despite signs that many feel were all too obvious.

CoinPoker says the player’s alleged true identity was known early in this process, after the company conducted a webcam security interview with them in February 2025. The name the player gave matched the handle the player later used on GGPoker, which requires players to use their real name as their handle instead of a pseudonym for certain high-stakes games. (WIRED is not naming the player because they have not been charged with any crime. The player did not respond to multiple requests for comment on this story). The CoinPoker spokesman says their team reached out to ACR with their findings as well and received no response. (Requests for comment from WIRED to ACR and GGPoker received no reply.)

To its credit, GGPoker acknowledged the incident and announced several fixes in anOctober 15 blog post, including banning third-party tools and adding win-rate anomaly detection. The site also says it traced the accused attacker’s funds to a Coinbase account and has asked the crypto company to restrict the account and preserve its records; it says it also provided the wallet addresses to industry watchdogs and law enforcement.

But ACR is going the opposite direction: On October 18, it emailed players claiming its security team found no compromised game outcomes or wrongdoing and will not issue any refunds—despite, in the same email, announcing a new feature to stop remote-viewing tools from capturing the images of the cards in players’ hands.

Other entities have taken concrete action: BothJurojinand IntuitiveTables (via its Discord channel) released tools to help users detect whether the MeshAgent hack had affected their machines. AceGuardian, a research group that’s part of A5 Labs, put out anopen-source “superuser detection” tooldesigned for use on any poker site. WolfSec says he submitted a complaint to the the Internet Crime Complaint Center, the cybercrime arm of the FBI, and has been working with players on improving machine security. The FBI, when reached for comment by WIRED, would not confirm receipt nor any details of this complaint.

But these efforts will be so successful only if the sites treat these incidents with more scrutiny and don’t just spring into action in the aftermath of major attacks.

“Ultimately, the sites have to ban the players,” Howard says. “I think they dropped the ball here.”

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Go inside the world of digital security withKernel Panic
* Wesexted with a Muse AI agent—and Meta says that’s totally fine
* Big Story:Meet the DEA’s premier crypto detective
* OpenAI ispissing off mathematicians
* Want better search results?Make WIREDa preferred source in Google
Ben Dowsett
 is a freelance sports and tech journalist specializing in features and in-depth reporting. He's obsessed with sports and with how modern technology improves them. His previous work can be found at Scientific American, ESPN, The Ringer, The Guardian, and elsewhere. He lives in Salt Lake City. ... 
Read More

Topics
poker
gambling
malware
hacks
hackers
software
agentic AI
‘Nightmare Scenario’: Zero-Click Spyware Is Infecting Phones via Targeted Ads
Researchers at The Citizen Lab have for the first time released technical evidence of sophisticated mercenary spyware being distributed via online advertising.
Matt Burgess
A Design Flaw in Share Links Exposes Users’ Personal Conversations With Meta’s Muse
The company is suspending the feature after security researchers discovered how easy it was to access sensitive information shared with the AI assistant.
Dan Goodin, Ars Technica
‘This Is Not a Drill’: Critical PHP Vulnerabilities Are Setting the Internet on Fire
The PHP Foundation has revealed two serious vulnerabilities that could impact millions of websites. Security experts warn that failure to quickly patch the flaws could have dire consequences.
Matt Burgess
AI Hacks Leave a Mess That AI Companies Aren’t Paying For
Powerful AI models continue to cause chaos, but their targets aren’t widely seeking justice. Instead, they’re being encouraged to adopt those same tools.
Paresh Dave
A Flaw in ChatGPT’s Mac App Could Have Let Hackers Grab Sensitive Data
While the focus has been on AI agents’ hacking capabilities, a recently patched vulnerability in a ChatGPT app shows that AI software is itself an inviting—and vulnerable—target.
Lily Hay Newman
AI Is Getting Really Good at Messing With Cybercriminals
Anti-cybercrime initiatives are increasingly using AI to scam the scammers by tricking them into talking to lifelike bots that they think are real victims.
Lily Hay Newman
The Secrets of a US Spyware King
In an exclusive interview with WIRED, Paragon Solutions CEO Andrew Boyd reveals the limits of the company’s promise to keep bad actors from abusing its powerful espionage tool.
Kim Zetter
An OpenAI Employee Allegedly Used a Chatbot to Help Plant a Recording Device at the Office
Chatbot prompts reveal the engineer’s alleged efforts to set up a covert listening device days before one was found in a meeting room used by high-level executives.
Paresh Dave
AI Guardrails Aren’t Stopping Criminal Hackers
Hackers around the world are all-in on using agentic AI to wage attacks—and manipulating tools like Anthropic’s Claude to help them carry out their crimes.
Lily Hay Newman
The PHP Meltdown Shows How AI Makes Bugs More Exploitable
Security researchers used AI tools to help uncover years-old vulnerabilities in the PHP web scripting language. Then the AI-assisted attacks began.
Lily Hay Newman
Don’t Let a Crypto Inheritance Get Stuck on the Blockchain
Claiming an inheritance of Bitcoin or other cryptocurrency can be like hunting for buried treasure. It doesn’t have to be.
Jill Duffy
Elon Musk Bragged About His Grok Lego Star Wars Haul. Then X Users Punked Him
Musk, we find your lack of security disturbing.
Jeremy White
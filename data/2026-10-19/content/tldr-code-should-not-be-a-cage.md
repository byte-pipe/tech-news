---
title: Code Should Not Be a Cage
url: https://www.seuros.com/blog/code-should-not-be-a-cage
site_name: tldr
content_file: tldr-code-should-not-be-a-cage
fetched_at: '2026-10-19T09:16:32.228675'
original_url: https://www.seuros.com/blog/code-should-not-be-a-cage
author: Abdelkader Boudih
date: '2026-10-19'
published_date: '2026-10-17T00:00:00.000Z'
description: A model can now rebuild anything that runs on your machine. The companies will answer by moving everything onto their servers, and the small developers pay first.
tags:
- tldr
---

At the end of September Brandon Thomas released a Photoshop rebuilt with Opus 5.5 (My Name Is Nobodycovered it). A week later Thomasshipped Word, and the same day Thomas’s storytold organization on GitHub published clones ofAutoCADandPro Tools.

Someone vibe-coded an ext4 driver for OpenBSD andwrote: “No Linux source files were ever read to build this driver. It’s pure AI (ChatGPT and Claude-code).”Commenterspointed out what those models were trained on.

Anything that runs on your machine can be rebuilt now. That ends an era, and the next one is what free software spent decades warning us about.

## Lean Into It¶

I was halfway through this post when my friend Scott Werner, who builds AI tooling in Ruby at Sublayer,posted:

Thinking about the implications of REA (Reverse Engineer Anything) the only option is to lean into it rather than fight it. Just start building in a coding agent interface to make it easy for your users to modify what you release.

Ireplied: “This temporary lol. Goodluck REA when everything will be server side and without documentation.”

Scottcame back with: “MMO communities like Asherons Call rebuilt servers pre-ai using packet capture and traditional reverse engineering techniques…”

It’s a good answer, so I checked it.

## Asheron’s Call¶

Turbineshut downAsheron’s Call on January 31, 2017. Players logged their network traffic in the final weeks, and the emulator project ACE rebuilt a working server. That part of Scott’s story holds.

Packet capture shows you what the server sent. It can’t show you how the server decided. ACE’s loot and quest tables came from somewhere else: an encrypted cache file belonging toPhatAC, a private emulator from the early 2000s,crackedin 2017 and exported in 2018. ACE’sworld databaseis a snapshot from February 2005, and people still argue about where that cache came from.

Whatever the cache didn’t cover was rebuilt by hand. ACE’sreport for May 2019lists “Updated numerous creature loot tiers, as per wiki”. One of itssettingsstill carries the note “Retail defaulted to TRUE but there are currently data errors.”

Every complete rebuild I checked had the server’s data from somewhere. City of Heroes came back onleaked server code. Star Wars Galaxies Legends runs onsource that leaked in 2015. The projects that only had packets took years and still guess.

Asheron’s Call could be rebuilt because the game ran on players’ machines for 17 years and a copy of the server’s tables survived. A modern service ships a login page and some JSON.

The usual answer is that you can rebuild anything just by looking at it. Looking gets you the UX. What happens on the server never crosses the wire, and once the client carries encryption it can’t open on its own, the wire tells you even less. That leaves probing the server and watching what comes back. Nobody ever cracked a SIM card’s PIN that way, AI or not: three wrong PINs lock the card, and after ten wrongPUK codesit’s dead for good. Services will work like the SIM. A few strange requests and the account is suspended.

Scott’s tweet also named a tool to try,bb, which is open source and runs on your machine. Leaning in works for software like that, because its users can already change it. Adobe will never ship you its server so your agent can edit it.

## REA Is a Wrapper¶

REA, the tool Scott was talking about, made itsfirst commiton April 14, 2026: “betterBinaryMCP - Enhanced MCP server for Hopper Disassembler”. LaurieWired’sGhidraMCP, a community plugin, shipped in March 2025, andIDAhad one two days later.

I bought Binary Ninja after decompiling my way to working wifi with it. It has shipped an official MCP server sinceversion 6.0in September.

GhidraMCP and the IDA server predate REA by more than a year. A model lets anyone drive them without the study a decompiled kernel used to demand. OpenGoldHEN is what that looks like.

## OpenGoldHEN¶

GoldHEN is the PS4 homebrew enabler most of the scene runs. Sistro and a few maintainers have spent about five years on it. It used to be open, and theREADMEexplains why it isn’t anymore: “Project source code is currently private because over time I have seen a sad abuse of the source code that I, like the previous devs who worked on it, have been pleased to make it available to everyone to study and maybe improve it.”

On October 6, a GitHub account namedzer0days-opwas created, and seven minutes later it createdOpenGoldHEN, a reconstruction of GoldHEN whose author has beenopen about using AI. Its last commit landed the same morning. The repository has no license. Its README is a manifesto, and near the top it says “Code should not be a cage.” Further down: “Creativity should never have to ask for permission.”

I opened thefirst issuethat evening. I wasn’t polite, and two lines from it still stand:

What will happen is that after version 14.00, nobody will release shit EVER. You made Sony win. They should have hired you.

people are learning not to talk about this stuff in public anymore, where LLM companies can scrape the data.

jeremykross put it better in the thread: “it’s NOT free (libre) software if humans don’t or can’t comprehend it. It’s closed source in a new guise.”

I decompiled GoldHEN too, a few years ago, along with the other kernels in the scene. I wanted to know how they worked, and once I did, I built my own. GoldHEN’s internals stayed with me, because that work was Sistro’s.

My kernels aren’t public either. Opening a kernel means staying with it until other people understand it, and right nowMDMAhas my time.

## Sony Won¶

On September 15, Andy Nguyen, known as TheFloW,quit the PS5 sceneand stopped all work on PS5 Linux. TheFloW had found what looked like the last PS5 hypervisor bug and kept it quiet. Others found it too and were asked to wait until after GTA VI. They agreed. ByJordy’s account, the bug had been found with a “trusty ai clanker machine,” and a third person found it with AI a few hours later. Expecting more to follow, Jordy reported it to Sony’s bug bounty less than a day after agreeing to wait. TheFloW’sverdicton the scene: “just a bunch of noobs using LLMs and writing hacks they don’t even understand.”

The scene has always held bugs back. A flaw in the PS5 may still be there in the PS6, and anything released now gets fixed before the next console ships. I’m holding a hardware jailbreak until the PS6 is out, to see if it still applies. That rule only works while nobody breaks it, and a model makes the bug cheap to find and tempting to cash in.

In August I wrote that the people cracking open the PlayStationdeserve generous funding. TheFloW quit six weeks later.

## Stallman Saw the Server Coming¶

Vendors have their own answer to all of this, and Richard Stallman described it first. In March 2010 Stallman published the essay now titled“Who Does That Server Really Serve?”. The essay calls the trap Service as a Software Substitute: “using a service as a substitute for running your copy of a program.” The advice is to never use one “where in principle running a program would do.”

The FSF had already tried a license. TheAGPLv3, published in November 2007, makes you share your changes when you run modified code for users over a network. Stallman named its limit in the same essay: free programs on a server “liberate the server operator, but not the server’s users.”

That’s where this goes. Once a model can rebuild what you ship, companies will stop shipping it. The editor becomes a browser tab and the game streams from a data center. The excuse is easy to predict: we invested in this, so it runs on our premises. Screaming won’t change it.

OpenGoldHEN’s README says code should not be a cage, then spends most of its 205 lines on freedom. Its effect is to push vendors onto servers, where nobody can read the code at all.

## Freedom, From $19 a Month¶

On October 9, Marc Louposted“Bye bye Beehiiv 👋” to 412,000 followers. Beehiiv had raised its prices for the third time in two years, so Marc vibe-coded a replacement with “a few prompts with Opus 5.5.” The post listed one more feature: “I also gain a priceless feature: Freedom. I can change the UI, add features, connect all my apps - anything is possible with just a prompt.”

Five days later Beehiiv’s CEO, Tyler Denk,postedthe backlog for anyone planning a weekend clone: 383 lines of features, ending with “…but at least you saved $59/mo not paying for@beehiivanymore 🫡”. Daniel Tenner quoted it: “Your platform is burning. At least don’t boast about it.” Irepliedunder Daniel that the claim was “I’m going to build my own house with blackjack and hookers,” and Tyler had answered with a country and its army. To Tyler: “nobody wants all those features. You built them because someone asked, so now you have to maintain them forever.” I ended with: “The era of having complexity merchants build each their own API is ending.”

I still think that. Building exactly what you need is the good part of all this.

Marc’s code went up on October 10 asMailCheap, under the AGPL, pitched at “$0.10 per 1,000 emails”, which is whatAmazon SEScharges. On October 15, the day after my reply, the pitch became “I vibe-coded MailCheap, and it’s 83% cheaper,” pointing atmailcheap.ai: “From $19 a month.” On the Starter plan that works out to $0.95 per 1,000 emails. The public repository’s commits now read “Sync from mailcheap-cloud”, copied over from a repository nobody else can see.

The license is the one from the last section. Marc owns the copyright, so the AGPL asks nothing of mailcheap.ai. Six days passed between “Freedom” and “From $19 a month.”

## Outcome and Pattern¶

The bigger problem is that the ecosystem is sliding out from under people, and most of them only look at outcomes.

Daniel Tennerjokedabout a CNBC headline this week: “We’re hiring another 1,000 Dumb Fleshy Devs to fix them.” The headline was “Bank of America hired 1,000 contractors to patch software flaws exposed by Anthropic’s Mythos.”

Read past it. They’re contractors, brought in between April and June, when Mythos first reached the banks, on top of 3,000 people already doing that work. They’re still there, and CEO Brian Moynihan told investors the extra spending is temporary: “Once you patch, you don’t have to patch as much.” Further down, the article says the bank has about 3,400 fewer employees than a year ago, and that it’s unclear how much of that is AI. Its AI projects are expected to save $700 million in 2027, up from $300 million this year. The headline is the part people share.

Moynihan also said this: “we’ve got to be mindful that the people doing the software development are the people trying to sell us the services.”

## Who Pays¶

I don’t pity Adobe or Sony. They’ll move to the server and charge rent.

The people who lose are the small developers. Many of the games on my phone cost 20 MAD, about $2. I bought them because that’s how a developer pays for the next update, and because I use what I pay for. When something is free I never get full use out of it, and getting the most out of a machine is why I became a kernel developer.

Most of those phone games haven’t been updated in months. I also paid for Project Zomboid, and The Indie Stone is still shipping it:Build 42reached the stable branch in July. That’s what the price buys when enough people pay it.

The free version comes from a prompt. Every trivial application is going to be free, and each one will come out a little more purple than the last. Adam Wathan, who created Tailwind,apologizedin 2025 for making every button in Tailwind UIbg-indigo-500, “leading to every AI generated UI on earth also being indigo.” The models learned purple from that code, and the next models will learn it from what this generation ships.

Hollywood already runs on that loop. Disney tookMatoaka, a child when the English landed in 1607, and made her a romance in 1995. Avatar told the same story again on another planet in 2009.

Games are next. The people who still dream a story up get copied before they ship it. Everyone else will lift a plot from someone’s rant on X and market it as a 10/10, with sex and violence on top. I remember text adventures, where the world was a paragraph and your head drew the rest, and the first Civilization, where a few colored squares stood in for all of history.

Freya Holmér posted a 50-second clip of Tetris with a rotating board in March and asked “Is this anything?” Within days a vibe-coded version showed up in the replies and another in mobile app stores. Holmér counted up to four, all before the real game existed, and told404 Media: “You get this anxiety anytime you post anything, someone is going to come in to finish it for you and then monetize it and steal the whole concept.”

Studios have started hiding their work. On October 16, Alliance Artscancelled the public Steam demoof Drunken Goddess Reflux, three days before it was due, because an AI-made imitation could ship before the game itself. Players get closed sessions with recording rules instead.

Clients pay once the known schemes stop working. Mythos has alreadyhelped stopa fraudulent $1.5 million wire transfer at an unnamed partner bank, after a customer’s email account was compromised, so a model can flag a scheme it has seen before. I’ve turned down jobs at companies whose mission, once you got past the pitch, was to fuck their clients. People who build that for a living get paid to invent what no model has seen yet.

## The End of an Era¶

None of this happens without Google publishing “Attention Is All You Need” in June 2017, and OpenAI throwing scale at it until GPT-2 talked. In February 2019 OpenAIheld the full model backover “concerns about malicious applications of the technology,” thenreleased itin November. Seven years later, one of the malicious applications was OpenGoldHEN.

Without those two, most people would still be trying to sell a course, and the rest would be learning how to center a div.

The era that ends is the one where the program ran on your machine and you could open it. The PDF called “Attention Is All You Need” has been public for 112 months. Have you been paying attention to the outcomes, or to the pattern?

## 🔗Interstellar Communications

No transmissions detected yet.Be the first to establish contact!

• Link to this post from your site
• Share your thoughts via webmention
• Join the IndieWeb conversation

## Related Posts

### My Name Is Nobody

Part 1 stopped mid-thought on purpose. That's how software is going to feel: you depend on it, then the signal stops.

AI
engineering
open-source
Oct 10, 2026

### Parasites With a Term Sheet

Since 2023, companies keep trying to buy the gems I publish, or to hire me under a contract that hands them all of it. I scambaited five of them to the end. The plan never changes: raise $10-20M, then buy someone else's decade of downloads for a few thousand.

AI
open-source
supply-chain
Sep 30, 2026

### OpenSourceShit Part 4: The Closing

MongoDB closed to fight AWS in 2018. Elastic closed to fight AWS in 2021, then reopened in 2024 once the fight was over. Ghostty, tldraw, NetBSD, and QEMU closed in January 2026, and there's no company to make peace with this time. Two different closings, two different endings.

AI
open-source
engineering
Jul 1, 2026
Back to all posts
Back to top
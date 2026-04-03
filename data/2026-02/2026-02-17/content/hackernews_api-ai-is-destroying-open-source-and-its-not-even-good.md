---
title: AI is destroying Open Source, and it's not even good yet - Jeff Geerling
url: https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/
site_name: hackernews_api
content_file: hackernews_api-ai-is-destroying-open-source-and-its-not-even-good
fetched_at: '2026-02-17T11:20:04.745094'
original_url: https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/
author: VorpalWay
date: '2026-02-17'
published_date: '2026-02-16T15:30:00-06:00'
description: Over the weekend Ars Technica retracted an article because the AI a writer used hallucinated quotes from an open source library maintainer. The irony here is the maintainer in question, Scott Shambaugh, was harassed by someone's AI agent over not merging it's AI slop code. It's likely the bot was running through someone's local 'agentic AI' instance (likely using OpenClaw). The guy who built OpenClaw was just hired by OpenAI to "work on bringing agents to everyone." You'll have to forgive me if I'm not enthusastic about that.
tags:
- hackernews
- trending
---

# AI is destroying Open Source, and it's not even good yet

Feb 16, 2026

Over the weekend Ars Technicaretracted an articlebecause the AI a writer usedhallucinated quotesfrom an open source library maintainer.

The irony here is the maintainer in question, Scott Shambaugh, washarassed by someone's AI agentover not merging it's AI slop code.

It's likely the bot was running through someone's local 'agentic AI' instance (likely using OpenClaw). The guy who built OpenClaw was just hired by OpenAI to "work on bringing agents to everyone." You'll have to forgive me if I'm not enthusastic about that.

## Video

This blog post is a lightly-edited transcript of the video I published to YouTube today. Scroll past the video embed if you're like me, and you'd rather read the text :)

## Impacts on Open Source

Last month, even before OpenClaw's release, curl maintainer Daniel Stenbergdropped bug bountiesbecause AI slop resulted in actualusefulvulnerability reports going from 15% of all submissions down to 5%.

And that's not the worst of it—the authors of these bug reports seem to have a more entitled attitude:

These "helpers" try too hard to twist whatever they find into something horribly bad and a critical vulnerability, but they rarely actively contribute to actually improve curl. They can go to extreme efforts to argue and insist on their specific current finding, but not to write a fix or work with the team on improving curl long-term etc. I don't think we need more of that.

These agentic AI users don't care about curl. They don't care about Daniel or other open source maintainers. They just want to grab quick cash bounties using their private AI army.

I manageover 300 open source projects, and while many are more niche than curl or matplotlib, I've seen my own increase in AI slop PRs.

It's gottensobad, GitHub added a feature todisable Pull Requests entirely. Pull Requests are the fundamental thing that made GitHub popular. And now we'll see that feature closed off in more and more repos.

AI slop generation is getting easier, but it's not getting smarter. From what I've seen, models havehit a plateauwhere code generation ispretty good1...

But it's not improving like it did the past few years. The problem is the humans whoreviewthe code—who are responsible for the useful software that keeps our systems going—don't have infinite resources (unlike AI companies).

Some people suggest AI could take over code review too, but that's not the answer.

If you're running a personal weather dashboard or building a toy server for your Homelab, fine. But I wouldn't run my production apps—that actually make money or could cause harm if they break—on unreviewed AI code.

If this was a problem already, OpenClaw's release, and this hiring by OpenAI to democratize agentic AI further, will only make it worse. Right now the AI craze feels the same as thecrypto and NFT boom, with the same signs of insane behavior and reckless optimism.

The difference is there's more useful purposes for LLMs and machine learning, so scammers can point to those uses as they bring down everything good in the name of their AI god.

Since my videoThe RAM Shortage Comes for Us Allin December, we havehard drivesas the next looming AI-related shortage, asWestern Digital just announcedthey're already sold through their inventory for 2026.

Some believe the AI bubble isn't a bubble, but those people are misguided, just like the AI that hallucinated the quotes in that Ars Technica article.

And they say"this time it's different", but it's not. The same signs are there from other crashes. The big question I have is, how many other things will AI companies destroy before they have to pay their dues.

1. I used local open models to help memigrate my blog from Drupal to Hugo, and I admit, it's really helpful if you know what you're doing. But I also spent a lot of time manually testing and reviewing all the generated code before I ran it in production. And I'd spend even more time on that process to button it up, if I ever considered throwing it over the wall to another project maintainer for review!↩︎

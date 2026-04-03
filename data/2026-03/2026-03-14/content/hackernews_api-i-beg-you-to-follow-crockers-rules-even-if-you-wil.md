---
title: I beg you to follow Crocker's Rules, even if you will be rude to me | La Vita Nouva
url: https://lr0.org/blog/p/crocker/
site_name: hackernews_api
content_file: hackernews_api-i-beg-you-to-follow-crockers-rules-even-if-you-wil
fetched_at: '2026-03-14T19:12:25.390492'
original_url: https://lr0.org/blog/p/crocker/
author: ghd_
date: '2026-03-13'
description: I beg you to follow Crocker's Rules, even if you will be rude to me
tags:
- hackernews
- trending
---

Mar 08, 2026

# ¶

※ ※ ※

# I beg you to follow Crocker's Rules, even if you will be rude to me

spoiler: you probably won't!

There is a concept calledCrocker's Rules, and if you have never heard of it, the short version is this: you give people around you explicit permission to be maximally direct with you, to skip social cushioning. The person invoking Crocker's Rules is saying, in effect, "your feelings about how I might receive this are your problem to manage, not mine, just give me the information."

So a person receiving a message bears responsibility for their own emotional reaction to its content. If someone tells you your code is wrong, your emotional response to that is your problem to manage, not theirs to preemptively defuse11.And no this is not a way to get away with cruelty nor an invitation to insult people it is just a mutual agreement that both parties are here to exchange information efficiently, and neither party is going to spend calories on social theater that adds zero signal..

What it means in practice is that your colleague can write "this approach is wrong, here's why" instead of "hey, hope you're doing well, I had some time to look at your PR and I just wanted to shared a few small thoughts, please take these as just one perspective, and of course you know the codebase better than I do, but I was wondering if maybe we could potentially consider [useful thing here]" and then bury the actual point six paragraphs deep. Both messages contain the same information, however one of them respects time.

The Slack message that starts with "Hey! Hope you had a great weekend :)"22.See alsonohello.combefore asking a technical question or the PR comment that opens with "I'm not sure if I'm missing something here and sorry if this is a dumb question but" before raising a completely valid concern, or that incident text that spends two full paragraphs explaining that the author was sleep-deprived and had a lot on their plate and the monitoring tool had a weird quirk that they didn't know about and their lead had told them something ambiguous three weeks ago, before finally getting around to saying what actually broke and why. This is the literal opposite of professionalism and sometimes I see it as anxiety cosplaying as politeness.

I personally value directness, so when someone communicates with me in that way, it deos influence how I perceive them, even subconsciously. I would also argue that this effect happens to most people, including those who aren’t aware of Crocker’s Rules or don’t particularly care about them:

When you spend the first third of your message establishing that you are a nice person who means well, you are not being considerate but you are making the recipient wade through noise to get to signal. You are training them to skim your messages, which means that when you actually need them to read carefully, they might not. You are demonstrating that you do not trust the relationship enough to just say the thing and you are signaling a level of insecurity that undermines the technical credibility you are trying to establish. Nobody reads "hope you had a great weekend" and thinks better of the person who wrote it, they probably just being trained to take you less seriously in the future, or at worse, if they're evil loving of Crocker's like myself, they just think about the couple of seconds of their life they will never get back.

Another behavior that I'd say highly related to that kind of noisy politeness, which I find actually worse is apologizing preemptively, this is the behavior where someone, when something goes wrong or when they need to explain a decision, does not just explain the decision; they explain why they made the decision, and then explain the contextual factors that influenced that, and then explain why those contextual factors existed, and then explain why it would have been unreasonable to expect them to anticipate the downstream effect of those factors, and by the end you have some fat five paragraphs that contains maybe one sentence worth of information and reads like a legal defense brief written by someone who knows they are guilty.

Please do not do that. If the payment service went down because a config value was wrong, the incident report should say: the payment service went down because config value X was set to Y when it needed to be set to Z.

The fact that you were stressed, or that you had inherited the config from someone else, or that the documentation was unclear33.This is a good candidate for a structural factor., or that you asked your lead and they said it was probably fine, none of that is relevant to the incident report. You can document contributing factors if they are actually actionable, meaning if there is something structural that needs to change, name it specifically and attach a proposed fix to it. But confessing your emotional state and your reasoning process and your extenuating circumstances is not documentation, it is self-absolution and everyone reading it can tell the difference.

More importantly: it wastes their time and it buries the information they actually need to act on.

## More examples

Instead of

"I hope this is okay to bring up and sorry for the long message, I just wanted to flag that I've been looking at the latency numbers and I'm not totally sure but it seems like there might be an issue with the caching layer?"

You get

"The caching layer is causing a 400ms overhead on cold requests. Here's the trace."

The second message is more useful, faster to read, and actually more respectful of everyone involved.

Instead of

"I know this might not be the right place to say this and I totally understand if you disagree, but I was thinking maybe the current approach to error handling might have some potential downsides?"

you get

"The current error handling swallows exceptions silently, which is making debugging hell. We should propagate errors to the caller."

The second person sounds like an engineer. The first sounds like they are asking permission to have an opinion, after the other party say something like "can you elaborate" they might start mentioning silent exceptions or whatever is the issue.

If you are a junior engineer reading this and feeling defensive, the defensiveness is worth examining. The weekend was fine. Nobody needed to know. Write the message.

Politeness has a place, but I beg you put clarity first. A team that cannot tolerate direct statements about reality cannot debug anything larger than a typo. If the caching layer is slow, say it is slow. If the design is wrong, say it is wrong. The rest is noise.

See also:Do not apologize for replying late to my email.The XY Problem.Don't ask to ask, just ask. #Modus Vivendi

## Footnotes

1

And no this is not a way to get away with cruelty nor an invitation to insult people it is just a mutual agreement that both parties are here to exchange information efficiently, and neither party is going to spend calories on social theater that adds zero signal.

2

See alsonohello.com

3

This is a good candidate for a structural factor.
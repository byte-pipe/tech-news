---
title: 'Let It Die: The Lazy Email Agent on TabPFN, Gemma and Temporal - DEV Community'
url: https://dev.to/khushighosh/let-it-die-the-lazy-email-agent-on-tabpfn-gemma-and-temporal-10o0
site_name: devto
content_file: devto-let-it-die-the-lazy-email-agent-on-tabpfn-gemma-an
fetched_at: '2026-10-26T17:16:05.213590'
original_url: https://dev.to/khushighosh/let-it-die-the-lazy-email-agent-on-tabpfn-gemma-and-temporal-10o0
author: Khushighosh
date: '2026-10-25'
description: 'This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady ... Tagged with devchallenge, hf26challenge, gemma, tabpfn.'
tags: '#devchallenge, #hf26challenge, #gemma, #tabpfn'
---

Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady Submission 🦥

This is a submission for theHacktoberfest Open-Source AI Challenge Week 3: Slow and Steady

## What I Built

Most “lazy” agents do your chores faster. Let It Die asks whether the chore needs doing at all.

It reads incoming email and scores each message on how likely it is that ignoring it would cost you something. Then it does one of three things:

* Need you(top 20% by score): a local Gemma model writes a two-line summary and a suggested action for a morning digest.
* Low priority(middle 60%): left alone and counted in the digest.
* Let it die(bottom 20%): parked on a durable Temporal timer. If the sender follows up within 7 days, the email is escalated. If nothing arrives, it is archived.

Anyone whose inbox is full of mail that sorts itself out gets to be a little lazier: the cheapest task to finish is the one you never started, as long as you can tell which ones those are. On my held-out test slice of 1,981 emails, 398 (20%) were parked, and about 85% of them really got no reply.

## Demo

Real output from a run on held-out email:

397 need you | 1186 low-priority | 398 parked on a timer (let it die)
In the 'need you' bucket, 46% were actually replied to (overall: 30%)

- john.henderson@enron.com | Wharton Tm #3 Presentation | he replied
 Summary: John reviewed the Wharton Tm #3 presentation and found it to be a good start.

Enter fullscreen mode

Exit fullscreen mode

In the parking demo, 8 emails were picked at random from the let-it-die bucket. 7 were archived, and all 7 truly needed no reply. 1 was escalated, because the sender wrote again.

## Code

## Khushighosh/let-it-die

# Let It Die: an agent whose main skill is deciding not to act

Built for the Hacktoberfest Open-Source AI Challenge, Week 3 ("Slow and Steady").

Most "lazy" agents do your chores faster. This one asks whether the chore needs doing at all. It scores each incoming email on how likely ignoring it is to cost you something, then:

* Need you(top 20% by score): a local Gemma model writes a two-line summary and a suggested action for the morning digest.
* Low priority(middle 60%): left alone, counted in the digest.
* Let it die(bottom 20%): parked on a durable Temporal timer. If the sender follows up within 7 days, the email is escalated. If nothing arrives, it is archived.

emails ──> TabPFN score ──> triage ──┬─ need you ──> Gemma summary ──> morning digest
 ├─ low priority ──> counted only
 └─ let it die ──> Temporal timer (7 days)
 ├─
…

View on GitHub

MIT licensed. The README has the run steps (Windows, Python 3.12).

## How I Built It

emails -> TabPFN score -> triage -+- need you -> Gemma summary -> morning digest
 +- low priority -> counted only
 +- let it die -> Temporal timer (7 days)
 +- follow-up signal -> escalate
 +- timeout -> archive

Enter fullscreen mode

Exit fullscreen mode

* TabPFN(Prior Labs) predicts whether the owner replied within 7 days, from features built only from information available before each email arrived: sender history, who it was addressed to, time of day, subject and body cues, thread length. It needs no training run.
* Gemma(gemma3:4b through Ollama, running locally) writes the summaries and suggested actions for the need-you bucket.
* Temporalruns one workflow per parked email. It waits for either a follow-up signal or a 7-day timeout, then escalates or archives. My demo uses Temporal’s time-skipping test server, so a week of waiting runs in seconds. When I made the first archive attempt fail on purpose, Temporal retried every one automatically, and all 7 archived emails logged attempt 2.
* Sentrytraces the whole run: the agent, the triage step, each Gemma call (model, token counts, full prompt and response) and the Temporal step. About 22 of the 23 seconds were the five local Gemma calls, each with an HTTP call to 127.0.0.1, my own machine. Triage took about a millisecond and parking eight emails about 1.3 seconds.

The data.I don’t have a two-sided mailbox of my own, so I used one mailbox of about 28,000 messages from the public Enron corpus (CMU, May 2015 release), which includes sent folders and lets me derive reply labels. The label is “the owner replied in the same thread within 7 days.” Sent mail stops being archived after May 2001, so every later email would look unanswered; I cut the timeline to Nov 1999 through May 2001, which left 9,902 usable emails. I trained on the earliest 80% (7,921 emails) and tested on the latest 20% (1,981 emails, 70.5% of which got no reply). The split is by time, so the model never sees the future.

Model

ROC AUC

Ignore lowest 10%: truly no reply / replied-to mail missed

Ignore lowest 20%

Sender reply-rate rule

0.579

68.2% / 10.8%

73.7% / 17.8%

Gradient boosting

0.662

92.4% / 2.6%

88.4% / 7.9%

TabPFN

0.687

92.9% / 2.4%

84.6% / 10.4%

What I take from it:

* Both models clearly beat a rule based on the sender’s past reply rate.
* TabPFN’s AUC is higher by 0.024 (bootstrap 95% CI 0.003 to 0.043), but gradient boosting wins the 20% bucket. I call them comparable.
* The practical headline: the agent can park about 1 in 10 emails and be right 92 to 93% of the time, missing about 2.5% of the mail that actually got a reply.
* In the test slice, the need-you bucket was replied to 46% of the time against 30% overall, and the let-it-die bucket about 15%. It is a prioritizer, not an oracle.

What went wrong, and how I found it

* Every file looked missing.Enron filenames end in a dot (1., 10.), and Windows quietly strips it, so Python saw an empty mailbox until I switched to Windows’ extended-length path prefix.
* The first test set had no positives.The model scored a meaningless 98% accuracy. A month-by-month table showed replies falling to exactly 0 from June 2001, because the archive stops containing sent mail. I cut the timeline there.
* Gemma summarized the wrong message.For an email where the sender wrote one line on top of a long forwarded chain, the summary described the oldest forwarded message. I found it by reading the cached email text next to the summary. Cutting each email at the first forwarded-message marker fixed that case: over five runs each (the last two of each at temperature 0 with a fixed seed), the unfixed version summarized the forwarded message every time and the fixed version summarized the sender’s reply every time. The prompt for that email also shrank from 649 to 90 tokens.

Limitations

* “Replied within 7 days” is only a proxy for “needed action,” and “the sender wrote again” is a noisy follow-up signal. One escalated email in my demo came from a mailing list that re-sent the same subject line.
* One mailbox, one time-based split. The bootstrap interval treats emails as independent, though threads and senders cluster, so it is probably a little too tight.
* The parking demo uses 8 emails and a simulated clock, and “archive” writes to a log file instead of moving real mail.
* Gemma output is not deterministic, and identical prompts varied about 2x in latency between runs, so I only quote token counts for the forwarded-chain fix. That fix is one email, not a benchmark, and suggested actions vary between runs.
* Attachments aren’t in the email text, so suggested actions for attachment-only emails are generic.

## Why Does Open Innovation Matter?

* The model that reads my mail runs on my machine.Gemma runs locally through Ollama, and the Sentry trace shows every model call going to 127.0.0.1. There is no API bill and no third party reading the text.
* The waiting is durable and I don’t run a scheduler.Temporal’s open-source tooling gave me timers that survive restarts and retries for flaky steps, with no cron job or home-made queue.
* No training run.TabPFN fits a small personal mailbox without a training step. The honest caveat: I used the hosted API, so the 5,000 training rows went to Prior Labs’ servers. I only did that with the public Enron data, and a deployment on private mail would need local weights or to accept that tradeoff.
* Anyone can reproduce the numbers.The data is public and the code is in the repo.

I didn’t test a hosted LLM, so I can’t claim open wins on summary quality. The case for open here is privacy, cost and not depending on a service staying up.

## The Lazy Payoff

I haven’t pointed it at my own inbox, because I don’t have a two-sided mailbox, so these numbers come from public Enron mail, not from my own week. On the held-out slice of 1,981 emails, the agent would have taken 398 (20%) off the owner’s plate, and about 85% of those really got no reply. The price is the other 15%, about 60 emails that did get a reply and would have been archived unless the sender nudged again, which is about 10% of all the mail that was replied to. Each summary takes about 4 seconds on my laptop. I can’t honestly put a number on minutes saved, so I’m not going to.

## Prize Categories

* Best Use of TabPFN:the ignore-or-act predictor, compared with a rule and gradient boosting, with a bootstrap interval on the difference.
* Best Use of Gemma:local gemma3:4b summaries and suggested actions, with a documented failure and fix.
* Best Use of Temporal:one durable workflow per parked email, with a follow-up signal, a 7-day timeout and automatic retries.
* Best Use of Sentry Agent Tracing:a trace of the whole run with token counts, prompts and responses, and the before and after of the forwarded-chain fix.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
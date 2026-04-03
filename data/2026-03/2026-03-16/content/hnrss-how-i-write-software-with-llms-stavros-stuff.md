---
title: How I write software with LLMs - Stavros' Stuff
url: https://www.stavros.io/posts/how-i-write-software-with-llms/
site_name: hnrss
content_file: hnrss-how-i-write-software-with-llms-stavros-stuff
fetched_at: '2026-03-16T11:23:27.383743'
original_url: https://www.stavros.io/posts/how-i-write-software-with-llms/
date: '2026-03-16'
description: How I write software with LLMs
tags:
- hackernews
- hnrss
---

I don't care for the joy of programming

Lately I’ve gottenheavilyback into making stuff, and it’s mostly because of LLMs.
I thought that I liked programming, but it turned out that what I like was making things, and programming was just one way to do that.
Since LLMs have become good at programming, I’ve been using them to make stuff nonstop, and it’s very exciting that we’re at the beginning of yet another entirely unexplored frontier.

There’s a lot of debate about LLMs at the moment, but a few friends have asked me about my specific workflow, so I decided to write it up in detail, in the hopes that it helps them (and you) make things more easily, quickly, and with higher quality than before.

I’ve also included a real (annotated) coding session at the end.
You can go there directly if you want to skip the workflow details.

## The benefits

For the first time ever, around the release of Codex 5.2 (which feels like a century ago) and, more recently, Opus 4.6, I was surprised to discover that I can now write software with LLMs with a very low defect rate, probably significantly lower than if I had hand-written the code, without losing the benefit of knowing how the entire system works.
Before that, code would quickly devolve into unmaintainability after two or three days of programming, but now I’ve been working on a few projects for weeks non-stop, growing to tens of thousands of useful lines of code, with each change being as reliable as the first one.

I also noticed that my engineering skills haven’t become useless, they’ve just shifted:
I no longer need to know how to write code correctly at all, but it’s now massively more important to understand how to architect a system correctly, and how to make the right choices to make something usable.

On projects where I have no understanding of the underlying technology (e.g. mobile apps), the code still quickly becomes a mess of bad choices.
However, on projects where I know the technologies used well (e.g. backend apps, though not necessarily in Python), this hasn’t happened yet, even at tens of thousands of SLoC.
Most of that must be because the models are getting better, but I think that a lot of it is also because I’ve improved my way of working with the models.

One thing I’ve noticed is that different people get wildly different results with LLMs, so I suspect there’s some element of how you’re talking to them that affects the results.
Because of that, I’m going to drill very far down into the weeds in this article, going as far as posting actual sessions, so you can see all the details of how I develop.

Another point that should be mentioned is that I don’t know how models will evolve in the future, but I’ve noticed a trend:
In the early days of LLMs (not so much with GPT-2, as that was very limited, but with davinci onwards), I had to review every line of code and make sure that it was correct.
With later generations of LLMs, that went up to the level of the function, so I didn’t have to check the code, but did have to check that functions were correct.
Now, this is mostly at the level of “general architecture”, and there may be a time (next year) when not even that is necessary.
For now, though, you still need a human with good coding skills.

## What I’ve built this way

I’ve built quite a few things recently, and I want to list some of them here because a common criticism of LLMs is that people only use them for toy scripts.
These projects range from serious daily drivers to art projects, but they’re all real, maintained projects that I use every day:

### Stavrobot

The largest thing I’ve built lately isan alternative to OpenClaw that focuses on security.
I’ve wanted an LLM personal assistant for years, and I finally got one with this.
Here, most people say “but you can’t make LLMs secure!”, which is misunderstanding that security is all about tradeoffs, and that what my agent tries to do is maximize security for a given amount of usability.
I think it succeeds very well, I’ve been using it for a while now and really like the fact that I can reason exactly about what it can and can’t do.

It manages my calendar and intelligently makes decisions about my availability or any clashes, does research for me, extends itself by writing code, reminds me of all the things I used to forget and manages chores autonomously, etc.
Assistants are something that you can’t really explain the benefit of, because they don’t haveonekiller feature, but they alleviate a thousand small paper cuts, paper cuts which are different for each person.
So, trying to explain to someone what’s so good about having an assistant ends up getting a reaction of “but I don’t need any of the things you need” and misses the point that everyone needs different things, and an agent with access to tools and the ability to make intelligent decisions to solve problems is a great help for anyone.

I’m planning to write this up in more detail soon, as there were some very interesting challenges when designing it, and I like the way I solved them.

### Middle

Maybe my naming recently hasn’t been stellar, but this is asmall pendant that records voice notes, transcribes them, and optionally POSTs them to a webhook of your choice.
I have it send the voice notes to my LLM, and it feels great to just take the thing out of my pocket at any time, press a button, and record a thought or ask a question into it, and know that the answer or todo will be there next time I check my assistant’s messages.

It’s a simple thing, but the usefulness comes not so much fromwhatit does, but fromthe wayit does it.
It’s always available, always reliable, and with zero friction to use.

### Sleight of hand

I’m planning to write something about this too, but this one is more of an art piece:
It’s a ticking wall clock that ticks seconds irregularly, but is always accurate to the minute (with its time getting synced over the internet).
It has various modes, one mode has variable tick timing, from 500 ms to 1500 ms, which is delightfully infuriating.
Another mode ticks imperceptibly more quickly than a second, but then pauses for a second randomly, making the unsuspecting observer question their sanity.
Another one races to :59 at double speed and then waits there for thirty seconds, and the last one is simply a normal clock, because all the irregular ticking drives me crazy.

### Pine Town

Pine Townis a whimsical infinite multiplayer canvas of a meadow, where you get your own little plot of land to draw on.
Most people draw… questionable content, but once in a while an adult will visit and draw something nice.
Some drawings are real gems, and it’s generally fun scrolling around to see what people have made.

I’ve made all these projects with LLMs, and have never even read most of their code, but I’m still intimately familiar with each project’s architecture and inner workings.
This is how:

## The harness

For the harness, I useOpenCode.
I really like its features, but obviously there are many choices for this, and I’ve had a good experience withPias well, but whatever harness you use, it needs to let you:

* Use multiple models from different companies.
Most first-party harnesses (Claude Code, Codex CLI, Gemini CLI) will fail this, as companies only want you to use their models, but this is necessary.
* Define custom agents that can autonomously call each other.

There are various other nice-to-haves, such as session support, worktree management, etc, that you might want to have depending on your project and tech stack, but those are up to you.
I’ll explain the two requirements above, and why they’re necessary.

### Multiple models

You can consider a specific model (e.g.
Claude Opus) as a person.
Sure, you can start again with a clean context, but the model will mostly have the same opinions/strengths/weaknesses as it did before, and it’s very likely to agree with itself.
This means that it’s fairly useless to ask a model to review the code it just wrote, as it tends to mostly agree with itself, but it also means that getting adifferentmodel to review the code will lead to a big improvement.
Essentially, you’re getting a review from a second set of eyes.

Different models will have different strengths and weaknesses here.
For example (and this is very specific to today’s models), I find Codex 5.4 pretty nitpicky and pedantic.
This isn’t something I want when I want to get code written, but it definitely is something I want for a review.
The decisions Opus 4.6 makes correlate quite well with the decisions I would have made, and Gemini 3 Flash (yes, Flash!) has even been very good at coming up with solutions that other models didn’t see.

Everyone has a different opinion on what model suits them for which job, and models tend to alternate (e.g. I used Codex as my main model back in November, switching back to Opus later).
To get the best results, you need a mix of all of them.

### Agents that call each other

The workflow I use consists of different agents, and if the harness doesn’t have the ability to let agents talk to each other, you’ll be doing a lot of annoying ferrying of information between LLMs.
You probably want to cut down on that, so this is a very useful feature.

## My workflow

My workflow consists of an architect, a developer, and one to three reviewers, depending on the importance of the project.
These agents are configured as OpenCode agents (basically skill files, files with instructions for how I want each agent to behave).
I write these by hand, as I find it doesn’t really help if you ask the LLM to write a skill, it would be like asking someone to write up instructions on how to be a great engineer and then gave them their own instructions and said “here’s how to be a great engineer, now be one”.
It obviously won’t really make them better, so I try to write the instructions myself.

### The architect

The architect (Claude Opus 4.6, currently) is the only agent I interact with.
This needs to be a very strong model, typically the strongest model I have access to.
This step doesn’t consume too many tokens, as it’s mostly chat, but you want this to be very well-reasoned.

I’ll tell the LLM my main goal (which will be a very specific feature or bugfix e.g. “I want to add retries with exponential backoff to Stavrobot so that it can retry if the LLM provider is down”), and talk to it until I’m sure it understands what I want.
This step takes the most time, sometimes even up to half an hour of back-and-forth until we finalize all the goals, limitations, and tradeoffs of the approach, and agree on what the end architecture should look like.
It results in a reasonably low-level plan, with a level of detail of individual files and functions.
For example, tasks might be “I’ll add exponential backoff to these three codepaths of these two components in this file, as no other component talks to the LLM provider”.

I know that some people in this step prefer to have the LLM write out the plan to a file, and then they add their feedback to that file instead of talking to the LLM.
This is a matter of personal preference, as I can see both approaches working equally well, so feel free to do the reviews that way if it suits you more.
Personally, I prefer chatting to the LLM.

To clarify, in this step I’m notjustprompting, I’m shaping the plan with the help of the LLM.
I still have to correct the LLM a lot, either because it’s wrong or simply because it’s not doing things the way I’d do them, and that’s a big part of my contribution, as well as the part I get joy from.
This direction is what lets me call projectsmine, because someone else using the same LLM would have come up with a different thing.

When I’m satisfied that we’ve ironed out all the kinks (the LLM is very helpful at this, asking questions for what it doesn’t know yet and giving me options), I can finally approve the plan.
I’ve asked the architect to not start anything until I actually say the word “approved”, as a few models tend to be overeager and go off to start the implementation whentheyfeel like they understood, whereas I want to make sureI’mconfident it understood.

Then, the architect will split the work into tasks, and write each task out into a plan file, usually in more detail (and at a lower level) than our chat, and call the developer to start work.
This gives the developer concrete direction, and minimizes the high-level choices the developer can make, as the choices have already been made for it.

### The developer

The developer can be a weaker, more token-efficient model (I use Sonnet 4.6).
The plan shouldn’t give it much leeway into what it can do, and its job is strictly to implement the changes in the plan.
When it’s done, it calls the reviewers to review its work.

### The reviewers

Each reviewer will independently look at the plan and diff of the feature that was just implemented, and critique it.
For this step, I will always use at least Codex, sometimes I’ll add Gemini, and on important projects I’ll add Opus as well.

This feedback goes back to the developer, which either integrates it, if the reviewers agree, or it escalates to the architect when the reviewers disagree.
I’ve found that Opus is very good at choosing the right feedback to implement, sometimes ignoring feedback because it’s too pedantic (i.e. hard to implement and unlikely to be a problem in practice).
Obviously, when I use objective assessments like “very good”, I really mean “I agree with it a lot”.

### The overall approach

This way of working means that I still know every choice that was made above the function level, and can use that knowledge in subsequent runs.
I often notice the LLM recommend things that might be good in another codebase, but either won’t work or are suboptimal in my codebase, which shows that the LLM has some blind spots when researching the code.
I will often say “no, you should do this using Y”, at which point the LLM realizes that Y actually exists in the code and is a better way than the one it recommended.

### Failure modes

On the flip side, when I’m not familiar enough with the technology to be on top of the architecture, I tend to not catch bad decisions that the LLM makes.
This leads to the LLM building more and more on top of those bad decisions, eventually getting in a state where it can’t untangle the mess.
You know this happens when you keep telling the LLM the code doesn’t work, it says “I know why! Let me fix it” and keeps breaking things more and more.

That’s a real failure mode that has happened to me too many times now, which is why I ended up with this workflow.
For this reason, I try to understand things as much as I can while planning, even if I’m unfamiliar with the specific technology.
If I manage to steer the LLM well, it saves a lot of trouble later on.

## A real session

Here’s an annotated transcript from a real session where I add email support to Stavrobot.
I’ve trimmed the tool calls and verbose bits, but the conversation and decision-making process is exactly as it happened.

I start by telling the LLM what I’d like to implement, at a very high level.
Sometimes I’ll give it more detail, especially if I already have an idea of how I want the implementation done.

Me: I'd like to add email support to this bot. Let's think through
 how we would do this.

The bot reads the code and finds all the relevant bits, and asks some questions.

LLM: Good overview acquired. Here's what I see and the questions we
 need to resolve:

 ## Current pattern

 All channels follow the same flow: inbound webhook/listener →
 enqueueMessage(message, source, sender, attachments) → LLM
 processes → LLM calls send_*_message tool to reply. Channels are
 either in-process (Telegram webhooks, WhatsApp via Baileys) or
 separate containers (Signal bridge). Email would be a new channel
 following this same pattern.

 ## Key design questions

 
1.
 Inbound — how does email arrive?

 
-
 
IMAP polling (simplest — poll a mailbox on a timer, works
 with any provider)

 
-
 
Webhook from a transactional email service (SendGrid/Mailgun
 inbound parse — requires that service)

 
-
 
Run an SMTP server (most complex, requires DNS/MX setup)

 
2.
 Outbound — how do we send?

 
-
 
SMTP client (works with any provider — Gmail, Fastmail,
 self-hosted)

 
-
 
Transactional email API (SendGrid/Mailgun API)

 
3.
 What's your actual use case? This affects several decisions:

 
-
 
Full bidirectional conversation (reply to emails, maintain
 threads)?

 
-
 
One-way notifications from the bot?

 
-
 
Processing incoming emails (e.g., forwarded emails,
 digests)?

 
4.
 Architecture — separate container or in-process?
 Signal uses a bridge container because signal-cli is a heavy
 Java process. Email libraries are lightweight, so in-process
 (like Telegram) is viable. But the AGENTS.md rule about not
 adding runtimes to the app container doesn't apply here since
 it's just TypeScript/Node.

 
5.
 Email-specific concerns:

 
-
 
How to handle HTML emails? Strip to plain text? Pass a
 markdown conversion to the LLM?

 
-
 
Thread tracking — match replies to conversations by
 In-Reply-To/References headers, or treat each email
 independently?

 
-
 
Attachments — needed?

 What's the scenario you're envisioning? That'll narrow this down
 fast.

In this session, I came with just a bit of an idea that hadn’t been thought through yet.
The LLM helps by asking specific questions, where I decide which way I want the implementation to go:

Me: 1. Email will arrive from a webhook, yes. I will create a
 Cloudflare Email worker that will forward the entire body of the
 email via webhook. It'll upload a JSON version of the message:

 {"from":"me@mydomain.com", etc}

 
2.
 SMTP client

 
3.
 Full bidirectional conversation, yes. This will be the same as
 how interlocutors work with the other transports, if someone sends
 an email to the bot, it will be ignored unless they are set up as
 an interlocutor. The owner can also send emails or forward emails
 for processing.

 
4.
 In-process, since this will be a webhook.

 
5.
 Markdown conversion, yes. Let's treat each email independently
 for now, and then we can change that if necessary. Attachments are
 needed, they should work like any other platform, the agent will
 receive them as files.

 The scenario I'm envisioning is both being able to correspond with
 people over email via subagents (like the bot currently does with
 Signal/Telegram/Whatsapp) and the owner being able to forward
 emails (e.g. a confirmation email for a booking) for the bot to
 process and ingest the info. Does this make sense? What edge cases
 can you foresee, or is there something you're worried about?

The LLM shapes the plan, giving it more detail:

LLM: This makes sense and fits cleanly into the existing channel
 pattern. Here are my observations and the edge cases I see:

 ## Concerns and edge cases

 
1.
 MIME parsing is non-trivial. Plain text emails are easy, but
 real-world emails are multipart MIME (HTML+text alternatives,
 inline images, attachments, nested multipart parts, various
 character encodings). We should use mailparser (from the
 Nodemailer project) to parse the raw RFC 2822 message
 server-side rather than trying to handle this in the worker.
 This means the worker payload can be minimal — just from, to,
 and raw.

 
2.
 Webhook authentication. The endpoint must be public (Cloudflare
 can't do a browser login), but we need to prevent anyone from
 POSTing fake emails. Simplest approach matching the Telegram
 pattern: generate a random secret on startup, but since we
 can't call back to Cloudflare to register it, we'd configure a
 shared secret in config.toml and have the worker send it as a
 header. The endpoint validates it.

 
3.
 Outbound emails need a subject line. Every other channel is
 subject-less, but email requires one. The send_email tool needs
 a subject parameter that the LLM provides. This is a new thing
 for the agent to handle.

 
4.
 HTML-only emails. Some emails have no plain text part at all.
 mailparser can extract textAsHtml which we'd convert to
 markdown. The html-to-text library handles this well, or
 mailparser itself provides a .text property that does basic
 HTML stripping.

 
5.
 From address identity. For outbound SMTP, the from address must
 match what the SMTP server allows. This is a config value. If
 someone emails bot@mydomain.com, the reply should come from
 that address.

 
6.
 Forwarded emails for processing. When the owner forwards an
 email, the original sender's address will be in the forwarded
 body, not in the from field (which will be the owner's
 address). The LLM will need to understand this contextually —
 no special code needed, the forwarded content will just be in
 the message body. This should work naturally.

 
7.
 Attachments on outbound. The existing send_*_message tools
 support attachments via file paths. send_email would need the
 same, using nodemailer to attach files. This is
 straightforward.

 ## Proposed design

 Worker simplification:
 // Only send what we need — parse everything from raw
 // server-side
 const payload = {
 from: message.from,
 to: message.to,
 raw: rawEmail
 };
 // Add auth header
 headers: {
 "Authorization": "Bearer <secret>",
 "Content-Type": "application/json"
 }

 Config (config.toml):
 [email]
 smtp_host = "smtp.example.com"
 smtp_port = 465
 smtp_user = "..."
 smtp_password = "..."
 from_address = "bot@mydomain.com"
 webhook_secret = "some-random-secret"

 Inbound flow:

 
-
 
POST /email/webhook (public route, validated by webhook_secret
 header)

 
-
 
Parse raw with mailparser → extract subject, text body (with
 HTML fallback → markdown), attachments

 
-
 
Format message to LLM as: Subject: ...\n\n<body>

 
-
 
Save attachments via saveAttachment()

 
-
 
enqueueMessage(message, "email", senderEmailAddress,
 attachments)

 
-
 
Add "email" to GATED_SOURCES, add email handling to
 isInAllowlist()

 Outbound flow:

 
-
 
New send_email tool with params: to, subject, body
 (markdown), attachments (optional file paths)

 
-
 
Convert markdown body to HTML for the email (with plain text
 fallback)

 
-
 
Send via nodemailer SMTP transport

 
-
 
Interlocutor identity service: "email", identifier: email
 address

 New dependencies: mailparser, nodemailer, html-to-text (or we can
 rely on mailparser's built-in text extraction and skip
 html-to-text initially — we can add it if the quality is
 insufficient).

 Files touched:

 
-
 
src/email.ts — new file: webhook handler, MIME parsing,
 inbound processing

 
-
 
src/email-api.ts — new file: SMTP sending via nodemailer

 
-
 
src/agent.ts — add send_email tool definition

 
-
 
src/config.ts — add EmailConfig interface and load it

 
-
 
src/index.ts — add /email/webhook route, whitelist it in
 isPublicRoute()

 
-
 
src/queue.ts — add "email" to GATED_SOURCES

 
-
 
src/allowlist.ts — add email channel handling

 
-
 
config.example.toml — add [email] section

 Explicitly not doing (YAGNI):

 
-
 
Email threading / In-Reply-To headers (you said treat
 independently)

 
-
 
CC/BCC handling

 
-
 
Bounce handling

 
-
 
Read receipts

 
-
 
Rate limiting

 
-
 
Email signature stripping (LLM can handle this contextually)

 Does this look right? Anything you'd change before I write it up
 as tasks?

I reply with a few things that I see it has missed.
This requires me to know the architecture well, and following this process keeps me up to date with all the changes at a moderately low level.

Me: Make sure to update the README.md and config.example.toml as
 well. Also remember to change the email allowlist page to not
 validate E.164 for these

The LLM updates the plan and asks any final questions.

LLM: Good, now I have the full picture. Here's the updated agreement:

 ## Requirements

 
1.
 Inbound email via Cloudflare Email Worker webhook → POST
 /email/webhook (public, authenticated by shared secret)

 
2.
 Outbound email via SMTP (nodemailer) through a send_email tool
 (with to, subject, body, optional attachments)

 
3.
 Gated channel — email added to GATED_SOURCES, allowlist, and
 interlocutor identity system (service: "email", identifier:
 email address)

 
4.
 Allowlist UI — new "Email allowlist" section in the settings
 page; validates email format (not E.164)

 
5.
 Allowlist data — Allowlist interface gains an email: string[]
 field; backend validation accepts email addresses

 
6.
 Owner config — owner.email in config.toml, auto-seeded into
 allowlist like the other channels

 
7.
 MIME parsing — use mailparser to extract subject, text body
 (HTML fallback), and attachments from the raw RFC 2822 message

 
8.
 Message format to LLM — Subject: <subject>\n\n<body> so the
 agent sees what the email is about

 
9.
 Config — new [email] section: smtp_host, smtp_port, smtp_user,
 smtp_password, from_address, webhook_secret

 
10.
 Update config.example.toml, README.md

 ## Constraints

 
-
 
In-process (no new container)

 
-
 
Email is optional — if [email] is absent from config, no email
 functionality loads (like the other optional channels)

 
-
 
Follow existing patterns exactly (webhook handling like
 Telegram, allowlist like WhatsApp/Signal, tool definition like
 other send tools)

 ## Success criteria

 
-
 
Can receive an email via webhook, have it processed by the LLM,
 and the LLM can reply via send_email

 
-
 
Allowlist UI works for email addresses

 
-
 
Owner email auto-seeded into allowlist

 
-
 
Builds and passes existing tests; new tests for the webhook
 handler and allowlist validation

 ## Non-goals / out of scope

 
-
 
Email threading (In-Reply-To / References headers)

 
-
 
CC/BCC handling

 
-
 
Bounce/delivery-status handling

 
-
 
Read receipts

 
-
 
Email signature stripping

 
-
 
Rate limiting

 
-
 
Markdown-to-HTML conversion for outbound body (plain text is
 fine for now — we can add this later)

 One question before I write up tasks: for outbound, should the
 body be sent as plain text only, or do you want HTML emails
 (converting the LLM's markdown to HTML)? Plain text is simpler
 and works everywhere, but HTML looks nicer. I'd lean toward plain
 text for now and adding HTML later if desired.

 Also — the worker payload. I'd simplify it to just { from, to,
 raw } and parse everything server-side from raw. That way you
 don't need to maintain parsing logic in the worker. Sound good?

Sometimes I’ll remember something and tell the LLM before reading its message:

Me: Add instructions to the config.example.toml for setting this up,
 including the actual Cloudflare worker to use

It adapts by incorporating my concern and repeating its message.

LLM: Got it — the config.example.toml will include the worker code and
 setup instructions in comments. Let me update the plan with that
 and present the full task breakdown.

 Regarding my two open questions that you didn't address:

 
1.
 Outbound body format — I'll go with plain text for now (YAGNI).
 We can add markdown→HTML conversion later.

 
2.
 Worker payload — I'll simplify to { from, to, raw } with an
 auth header, and parse everything from raw server-side.

 ## Proposed plan directory

 misc/coding-team/email-support/

 ## Task breakdown

 
1.
 Config and dependencies — Add EmailConfig interface to
 config.ts, [email] section to config.example.toml (with
 Cloudflare worker setup instructions), install mailparser and
 nodemailer (plus their 
@types/
 packages). Add owner.email to
 OwnerConfig.

 
2.
 Allowlist — Add email: string[] to the Allowlist interface,
 update validateAllowlist, loadAllowlist (owner email
 auto-seed), getAllowlist, isInAllowlist,
 getOwnerIdentities. Add "email" to GATED_SOURCES in queue.ts.

 
3.
 Allowlist UI and backend validation — Add the "Email allowlist"
 section to the settings page HTML/JS (with email format
 validation instead of E.164), update handlePutAllowlistRequest
 to validate and accept the email array, update saveAllowlist
 serialization (including notes key pruning and owner identity
 merging).

 
4.
 Inbound email — New src/email.ts: webhook handler that
 validates the secret, parses the raw email with mailparser,
 extracts subject + text body + attachments, saves attachments,
 and calls enqueueMessage. Add the /email/webhook route to
 index.ts and whitelist it in isPublicRoute.

 
5.
 Outbound email — New src/email-api.ts: nodemailer SMTP
 transport setup and send function. Add send_email tool to
 agent.ts (params: recipient, subject, body, optional
 attachments), following the same pattern as the other send
 tools (interlocutor lookup, allowlist check).

 
6.
 README and tests — Update README.md to document email support.
 Add tests for the webhook handler validation and allowlist
 email validation in the existing test files.

 Does this look right? Say "approved" to proceed.

I do go back and read its message, as it usually has good questions and I don’t want to miss answering any of them.

Me: Regarding your questions, 1. Plain text. 2. Yes, simplify as much
 as possible

The LLM needs me to explicitly say the word “approved” to proceed.

LLM: Noted. The plan is as stated above. Say "approved" to proceed.

Me: Approved.

I remember something while the LLM is working and stop it to ask:

Me: By the way, what will an email look like to the bot? Will it be
 able to see the subject as well as the body?

LLM: Yes — the plan is to format the inbound message to the LLM as:

 Subject: Hello!

 Hi, this is the body of the email.

 So the subject is visible as a prefix, separated from the body by
 a blank line. This mirrors how you'd naturally read an email and
 gives the LLM enough context to understand what the email is about
 (especially useful for forwarded emails where the subject line
 carries meaning).

 For outbound, the send_email tool has a subject parameter, so the
 LLM will compose a subject line when replying.

Me: Excellent, please continue

The LLM writes the plan, calls the developer, the reviewers, and eventually finishes.
I’ve omitted all the background tool/agent calls here for brevity.

LLM: All 6 tasks are implemented. Here's what was done:

 New files:

 
-
 
src/email.ts — inbound webhook handler (validates Bearer
 token auth, parses raw RFC 2822 email with mailparser,
 extracts subject/body/attachments, checks allowlist, enqueues
 message)

 
-
 
src/email-api.ts — outbound SMTP transport (nodemailer, plain
 text emails with optional attachments)

 
-
 
src/email.test.ts — webhook auth tests

 Modified files:

 
-
 
src/config.ts — EmailConfig interface, email field on Config
 and OwnerConfig

 
-
 
src/allowlist.ts — email: string[] on Allowlist,
 case-insensitive matching, owner seeding

 
-
 
src/allowlist.test.ts — 12 new email allowlist tests

 
-
 
src/settings.ts — email allowlist UI section + backend
 validation (email format, not E.164)

 
-
 
src/settings.test.ts — 9 new email backend validation tests

 
-
 
src/queue.ts — "email" added to GATED_SOURCES

 
-
 
src/agent.ts — createSendEmailTool (recipient resolution,
 allowlist gate, SMTP send)

 
-
 
src/agent-send-tools.test.ts — email send tool tests

 
-
 
src/index.ts — /email/webhook route + isPublicRoute entry +
 initializeEmailTransport at startup

 
-
 
config.example.toml — full [email] section with setup
 instructions and Cloudflare Worker code

 
-
 
README.md — email setup section, updated feature list and
 architecture blurb

 
-
 
package.json / package-lock.json — mailparser, nodemailer,
 and their type packages

 Test results: 421 tests passing, TypeScript type-check clean.

 Worker change needed on your side: Update your Cloudflare Worker
 to the simplified version in config.example.toml — sends { from,
 to, raw } with Authorization: Bearer <secret> header, and point
 it at https://<publicHostname>/email/webhook.

 What would you like to do next?

I have an idea for improving the UX by allowing the bot to read incoming emails without configuring an outgoing SMTP server, in case the user wants to forward things like invoices or trip plans for it to read, but doesn’t want the bot to be able to send email.

Me: What do we check here, regarding the email parameters? I'm
 wondering whether we can have inbound emails working even if the
 user doesn't configure outbound emails. How hard would that be to
 implement?

The LLM scopes out effort.
If it’s a small change, I’ll usually do it as part of this session, otherwise I’ll write it to a GitHub issue for me to work on at a later time.

LLM: Here's the current situation:

 
-
 
EmailConfig requires all 6 fields (smtp host/port/user/password,
 fromAddress, webhookSecret) — they're all non-optional
 strings/numbers.

 
-
 
config.email gates everything: the webhook route, the SMTP
 transport initialization, and the send_email tool.

 So right now, if you only want inbound email (webhook), you'd
 still have to fill in all the SMTP fields with dummy values, which
 is ugly.

 The fix is straightforward — make the SMTP fields optional in
 EmailConfig. Then:

 
-
 
Webhook route: only needs webhookSecret → enabled whenever
 config.email exists.

 
-
 
SMTP transport init: only runs when the SMTP fields are present.

 
-
 
send_email tool: only registered when the SMTP fields are
 present.

 The change is small: make smtpHost, smtpPort, smtpUser,
 smtpPassword, and fromAddress optional in the interface, gate
 initializeEmailTransport and createSendEmailTool on their
 presence, and the webhook handler keeps working with just
 webhookSecret. Want me to do this?

Me: Yes please

More tool/agent calls elided here.

LLM: Done. Here's what changed:

 
-
 
EmailConfig.webhookSecret is the only required field now. The 5
 SMTP fields (smtpHost, smtpPort, smtpUser, smtpPassword,
 fromAddress) are all optional.

 
-
 
The webhook route works with just webhookSecret — inbound email
 is fully functional without any SMTP config.

 
-
 
The SMTP transport and send_email tool only initialize when
 smtpHost is present.

 
-
 
config.example.toml now clearly groups and labels the required
 vs optional fields.

 All 421 tests pass, type-check clean. What would you like to do
 next?

I QA the feature and come back with issues:

Me: I've sent an email, having specified owner.email, but the agent
 dropped it:

 [stavrobot] Dropping message: could not resolve target agent.
 source=email, sender=me@mydomain.com

 Also, the "to" seems truncated

LLM: Found it. Issue 1 (dropped message): seedOwnerInterlocutor
 builds the ownerIdentitySet from Signal, Telegram, and WhatsApp
 identities, but never adds email. So
 isOwnerIdentity("email", "me@mydomain.com") returns false, the
 owner bypass is skipped, and the message falls through to the
 allowlist check and interlocutor lookup — which probably also
 fails because there's no interlocutor record with an email
 identity yet.

 The "To" truncation in the logs — that's coming from the message
 format Subject: ...\n\nFrom: ...\nTo: .... That looks like the
 email body content being logged (the preview on line 181 of
 queue.ts truncates to 200 chars). The To: is from the email
 headers included in the body text by mailparser. The truncation is
 just the 200-char log preview cutting off — not an actual data
 issue. The full message is intact.

 So there's really just one bug: seedOwnerInterlocutor doesn't
 register owner.email as an owner identity.

The LLM goes off and fixes the problem.

LLM: Fixed. The bug was that seedOwnerInterlocutor in database.ts
 built the owner identity set from Signal, Telegram, and WhatsApp
 but never added email. So
 isOwnerIdentity("email", "me@mydomain.com") returned false, the
 owner bypass was skipped, and the message was dropped because
 there was no interlocutor record to route to either.

 The "To" truncation in the logs is just the 200-character message
 preview in queue.ts cutting off — the actual message data is
 intact.

 After rebuilding, your owner emails should route to the main agent
 correctly. Want to test it?

Here I spot that it’s missed a better way of implementing the feature, and I suggest that it changes its implementation:

Me: We have a list of sources, right? Why is that list not used for
 this, and we've hardcoded it instead?

LLM: You're right. The owner identity seeding in
 seedOwnerInterlocutor has a separate hardcoded if block for each
 channel — Signal, Telegram, WhatsApp, and now email. Meanwhile
 OwnerConfig already has the channel names as field keys. Every
 time a new channel is added, someone has to remember to add
 another if block there, which is exactly how this bug happened.

 The fix would be to iterate over a shared list of channel names
 (or just iterate the OwnerConfig fields dynamically) instead of
 having per-channel if blocks. The same pattern applies to
 getOwnerIdentities in allowlist.ts, which also has per-channel
 blocks.

 However — OwnerConfig has a name field that isn't a channel, and
 Telegram's identifier needs special handling (it's a numeric
 string converted to a number for the allowlist). So a fully
 generic loop isn't completely trivial, but it's still better than
 the current approach.

 The simplest version: define a list of channel keys (e.g.
 ["signal", "telegram", "whatsapp", "email"]) in one place, and
 have seedOwnerInterlocutor loop over it. Want me to do this
 cleanup, or would you rather keep moving and revisit it later?

I have second thoughts about making the check generic, because of the special case.

Me: The special cases give me pause. The name is probably fine, as we
 can ignore, that, but the Telegram conversion is more special.
 What do you think?

The LLM thinks about it a bit and recommends something reasonable.

LLM: The Telegram numeric conversion only matters in the allowlist
 (isInAllowlist compares numbers, getOwnerIdentities returns
 number[] for Telegram). But in seedOwnerInterlocutor, all
 identities are stored as strings in interlocutor_identities —
 even Telegram. So the seeding loop doesn't actually need any
 special cases. It's just:

 for (const channel of CHANNELS) {
 const value = ownerConfig[channel];
 if (value !== undefined) {
 identities.push({
 service: channel,
 identifier: channel === "email"
 ? value.toLowerCase()
 : value
 });
 }
 }

 ...though that introduces a special case for email lowercasing.
 Which is arguably also wrong — we should probably lowercase email
 everywhere it enters the system (allowlist seeding, inbound
 webhook, etc.) rather than in the identity loop.

 The more I think about it, the more I think the cleanup is worth
 doing for seedOwnerInterlocutor (where everything is strings
 anyway), but getOwnerIdentities in allowlist.ts has genuinely
 different return types per channel (string[] vs number[]), so
 forcing that into a generic loop would make it worse, not better.

 My recommendation: make the channel list a shared constant, use it
 in seedOwnerInterlocutor to loop, but leave getOwnerIdentities
 as-is since its per-channel type differences are inherent. That
 way the "forgot to add a new channel" bug class is eliminated for
 the seeding path, which is the one that just bit us.

Me: Ok, approved

LLM: Done. The four per-channel if blocks are replaced with a loop
 over OWNER_CHANNELS defined in config.ts. Next time a channel is
 added, it just needs to be appended to that array. All 421 tests
 pass.

 Want to rebuild and test the email flow again?

I QA and check again.
I realize that emails work slightly differently than phone numbers, and that the bot now ignores my custom email addresses.
I talk to the LLM about adding this:

Me: There is one wrinkle: Email whitelists are special, as someone
 might control an entire domain. Can we add asterisks to the email
 whitelist? For example, I'd like my (owner) email address to be
 "*@example.com", rather than just "me@example.com"

LLM: Makes sense — domain-level wildcards are a natural fit for email
 that doesn't exist for phone-number-based channels.

 The allowlist matching is straightforward: entries like
 *@example.com match any sender whose domain matches. The changes
 would be in isInAllowlist (matching logic), the settings UI and
 backend validation (accept the *@domain pattern), and tests.

 One question: should owner.email also support *@example.com? I'd
 lean no — the owner is a specific person, and the owner identity
 is used for exact-match routing (bypassing the interlocutor
 lookup). If owner.email is *@example.com, then any email from
 that domain would be treated as the owner, which seems wrong.
 You'd probably want owner.email = "me@example.com" for routing,
 and *@example.com in the allowlist for letting others through.

 Does that distinction make sense, or do you actually want the
 owner identity to be domain-wide too?

The LLM misunderstood what I wanted, so I clarify with a concrete use case:

Me: No, the whole issue is that I use disposable email addresses
 "company@mydomain.com", and forwarding those emails means that
 the email comes from the disposable email I used, so the bot
 drops them. I can't easily send the emails from my main address
 without changing it on every single email, so I'd rather the bot
 treated the entire domain as one person (if the wildcard is set
 that way). What is the issue with this?

LLM: The issue I was worried about is that isOwnerIdentity does an
 exact string match —
 ownerIdentitySet.has("email:me@mydomain.com"). If owner.email is
 *@mydomain.com, the set would contain
 "email:*@mydomain.com", and an incoming email from
 company@mydomain.com wouldn't match.

 But the fix is simple: make isOwnerIdentity understand domain
 wildcards for email, same as isInAllowlist. It's a few extra
 lines in one function. No real downside — if you control the
 domain, you are the owner regardless of which address you used.

 So the full scope is:

 
1.
 isInAllowlist — email case checks for *@domain entries by
 comparing the sender's domain.

 
2.
 isOwnerIdentity — same domain-wildcard matching for email
 entries in the owner identity set.

 
3.
 Settings UI + backend validation — accept *@domain.com as a
 valid email allowlist entry.

 
4.
 Tests for the new matching behavior.

 Want me to go ahead?

I ask it to make sure it takes care around a caveat.

Me: Please make sure that the local part (the wildcard) does not match
 the @ sign. I wouldn't want someone getting smart with validations
 and sending email from something like
 "me@mydomain.com"@evildomain.com and bypassing my owner check

LLM: Good catch. The matching logic will split on the last @ (or
 simply check that the sender's domain portion after @ matches
 exactly, and that the sender address contains exactly one @). That
 way "me@mydomain.com"@evildomain.com doesn't match
 *@mydomain.com.

And ask for some documentation changes.

Me: Please also clarify in the config.example.toml that the local
 part can contain an asterisk

I have another usability idea:

Me: We should do proper matching, in case someone wants to match
 things like myusername+*@gmail.com, not just ignore the entire
 local part. Hopefully nobody's local part will contain a
 legitimate asterisk

And a security consideration:

Me: If you use a regex, you need to escape every single other char in
 the email address

LLM: Done. The email allowlist now supports glob-style * wildcards:

 
-
 
*@mydomain.com — matches any address at the domain

 
-
 
myuser+*@gmail.com — matches any plus-tag for that user

 
-
 
exact@example.com — exact match only

 
-
 
* — allow everyone

 The * is translated to [^@]* in the regex, so it cannot match
 across the @ boundary — "me@good.com"@evil.com won't match
 *@good.com. This works in both the allowlist and the owner
 identity check.

I ask for a clarification to catch a potential gotcha:

Me: Does this work both in the owner's 
`email = `
 field and the
 allowlist page/the allowlist itself?

LLM: Yes, both:

 
1.
 owner.email in config.toml — the value is stored in
 ownerEmailEntries and matched via matchesEmailEntry in
 isOwnerIdentity. So owner.email = "*@mydomain.com" treats any
 address from that domain as the owner.

 
2.
 Allowlist (data layer + settings UI) — isInAllowlist for email
 uses matchesEmailEntry against every entry in the allowlist. So
 adding *@example.com via the settings page allows anyone from
 that domain.

 Both paths use the same matchesEmailEntry helper, so the matching
 behavior is identical.

The session continued for a bit with me doing more QA rounds, adding wildcard matching for email addresses, a question about SQLi, and catching a missing entry in the subagent allowlist.
The conversation went more or less as above, with me either catching an error or proposing an improvement, refining it with the LLM, and implementing it.

The whole feature took about an hour, start to finish, and I ended the session there as I was satisfied that the feature works well.

## Epilogue

That’s the basic overview of my setup.
It’s nothing extremely fancy, but it works very well for me, and I’ve been really pleased with the reliability of the whole process.
I’ve been running Stavrobot 24/7 for close to a month now, and it’s been extremely reliable.

If you have any feedback or just want to chat, get me onBluesky, or email me directly.
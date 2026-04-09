---
title: 'Breaking News: OpenAI Rebrands to OpaqueAI - DEV Community'
url: https://dev.to/vaticnz/breaking-news-openai-rebrands-to-opaqueai-4edk
site_name: devto
fetched_at: '2025-11-26T11:06:59.957746'
original_url: https://dev.to/vaticnz/breaking-news-openai-rebrands-to-opaqueai-4edk
author: Rich Jeffries
date: '2025-11-22'
description: TL;DR OpenAI launched MCP support in September 2025. It broke immediately. For two months,... Tagged with ai, openai, mcp, llm.
tags: '#ai, #openai, #mcp, #llm'
---

## TL;DR

OpenAI launched MCP support in September 2025. It broke immediately. For two months, they ghosted developers while their flagship product threw 424 errors, deleted features, and rolled back fixes in production. Their own demo apps didn't work.

So I fired them and built my own AI stack on a $350 GPU. Local models now outperform OpenAI's API on instruction following (95% vs 60%), cost nothing after month 2, and don't gaslight me with "working as intended."

Bonus: I fine-tuned a crisis detection AI (Guardian) to 90.9% accuracy on suicide/DV scenarios. OpenAI can't return consistent JSON. I'm training models to save lives.

The receipts are extensive. The irony is delicious. The future is local.

This isn’t a rant. It’s an autopsy.

### Act I — The Promise (Sept 10)

The curtain rises on optimism and malformed JSON.

OnSeptember 10, OpenAI announcedDeveloper Mode— a beta feature promising “full Model Context Protocol (MCP) client support for all tools, both read and write.”

Within hours, the launch thread —now conveniently deleted by OpenAI— turned into a bug parade. Developers reported failing tool calls, malformedtools/listpayloads, and ChatGPT's MCP client violating its own spec.

BySeptember 12, the evidence was undeniable: invalidresources/*payloads, missing handshake responses, and reproducible crashes. A few even noted thatClaudehandled the same servers flawlessly.

“Tried using it. The tools are loading, but when the model tries to invoke tools I get HTTP 424 errors… Claude had no issues.” —mucore, Sept 10“Fails 99% of the time… The list_resources call finds the tools but then returns ‘tool not available.’” —jelle1, Sept 12

Receipts:The problems were public, reproducible, and ignored.No fixes. No changelog. No “known issues.” Just the sound of a billion-dollar company pretending not to see the smoke.

### Act II — The Slow Unravel (Oct 6)

The silence grows louder. The devs start talking to each other instead.

By early October, the rot had spread. Developer Mode toggles vanished, custom connectors stopped listing tools, and previously stable MCP servers went dark.

That’s when I posted“Custom MCP connector no longer showing all tools as enabled”(Oct 6, 10:46 AM NZT). It blew up —2.3k views, 78 likes, 43 usersconfirming the same regression.

“My entire dev pipeline is dead.” —BrianGi, Oct 6“Can we at least get an acknowledgment that you’re aware of this?” —multiple devs, Oct 6–7“It worked in Claude yesterday; now ChatGPT can’t find any tools.” —KingT, Oct 7

For days, there wastotal silencefrom OpenAI staff. Developers debugged in public while the company ghosted the room.

I summed it up succinctly:

“This situation is untenable and deserves more dialogue and action from OpenAI. Fix and communicate.”

Spoiler: they didn’t.

### Act III — The Collapse (Oct 7)

The fix that wasn’t. The deploy that shouldn’t. The comedy that wrote itself.

The next day, OpenAI launched theApps SDK preview— complete with thePizzaandSolar Systemdemo apps. Both failed instantly.

GitHubIssue #1opened with @spullara’s deadpan:

“I added the pizza app to ChatGPT but it doesn’t work.”

Dozens piled in:

“Same issue.”“Enterprise, Plus — doesn’t matter. ChatGPT can’t find the tools.”“It worked yesterday, my boss is furious.”

Then@alexi-openaiappeared — the lone collaborator holding back a flood of frustrated devs. He found a payload mismatch in the MCP bridge, merged a fix, and posted:

“Identified the issue and we’ve merged a fix, it’ll be out in the next deploy … so sorry for the wasted time and confusion!”

And it worked — for a few hours.

Then:

“The issue was indeed fixed there for a bit, but has just started re-occurring.”“+1 – worked for a bit, and now again :(”

Trying to lighten the collective despair, I wrote:

“Just to brighten the day — this reads like the five stages of dev grief in real time.1️⃣ Denial: ‘Maybe it’s just me.’2️⃣ Hope: ‘Fix deployed!’3️⃣ Joy: ‘It works!!’4️⃣ Despair: ‘Roll back incoming…’5️⃣ Acceptance: ‘What an emotional rollercoaster.’ 😂”

Moments later, Alexi replied with the immortal line:

“ugh I’m so sorry everyone! we just rolled back our latest deploy, and with it the fix for this bug.”

Receipts:The bug was found, patched, deployed, broken again, and rolled back — all in one thread.

Apparently, OpenAI’s definition ofsafetynow includesrolling untested code to production on a global product with millions watching live. It’s the kind ofmove fast and break everythingenergy that makes Facebook look like a safety consultancy.

Meanwhile, users were being asked toverify their identities with photo IDvia a third-party provider — because that’s apparently where the security focus went.

In a moment of optimism, I upgraded to Business thinking it might be more stable. Spoiler: it was worse. I’ve since cancelled, gone back to Plus, and — miraculously — my connector works again. Mostly.

### Act IV — The Hangover (Oct 8 onward)

The silence becomes policy.

By the following week, Plus users were limping along, Business and Enterprise were dead in the water, and forum posts devolved into crowdsourced rituals:

“Go to Workflow Settings → Draft → Click Preview → Sacrifice a goat.”

Moderators vanished. Threads were markedClosed — Completedwhile still broken.

“Hi, can you see Developer Mode anymore? It was there on Friday.” —tuanpham.notme, Oct 8“Worked for me 30 minutes ago, then stopped again.” —bsunter, Oct 7“MCP connectors are back in the UI now, but still don’t work.” —Quim, Oct 7“Ludicrous that a company of this size with this much money can’t even get this right.” —Rich_Jeffries, Oct 14

The irony? The company selling “conversation” couldn’t manage one with its own developers.

### Epilogue — Fix and Communicate

As of today, the issue remains alive and unwell. MCP tooling is hit-and-miss, I've cancelled my subscription and moved on.

OpenAI doesn’t just have a communication problem — it has a communicationphilosophy.Silence is cheaper than transparency, and community debugging is free labour.

When a company built on language models treats language as optional, you start to wonder what the “I” in AI actually stands for.We now know the “Artificial” is spot on.

OpaqueAI

To provide clarity.

### Postscript — Opaque Journalism 101

When tech media becomes the press release.

EvenTechSpot, a site claiming to deliver“fair, accurate and honest analysis”for 25 years, seems to have taken notes from the OpaqueAI playbook.

They ran an article singing the praises of OpenAI’s shiny new Apps SDK — since quietly removed. Being a regular reader, I left a short, factual comment:

“Except it’s broken before it got out the gate…”(with a GitHub link, because journalism, right?)

Then the comment vanished.So I asked:

“Deleting comments? Is this a paid advertorial?”

Also gone.

My parting shot:

“That’s OK, I’ve got the receipts.”

Update:After I called them out publicly, the comments mysteriously reappeared. Screenshot below shows all three comments still live with timestamps — funny how transparency works when someone's watching.Then the article itself vanished.

Screenshot captured Oct 7, 2025 — proving the comments exist with full timestamps and content intact.

Moral of the story?Trust is earned. Receipts cost nothing.

### Public Timeline — The MCP Meltdown (Sept 10 → Oct 14)

Date

Event

Source

Sept 10

Developer Mode launch — first reports of HTTP 424 errors and malformed payloads

mucore, jelle1

Sept 12

“ResourceNotFound” and missing tool calls — confirmed by multiple users

jelle1, ternarybits

Oct 6

Connectors fail to list tools; massive user thread forms

BrianGi, Rich_Jeffries

Oct 7

SDK preview launches; fails instantly; GitHub Issue #1 goes viral

spullara, alexi-openai

Oct 8

Developer Mode disappears for Plus users

tuanpham.notme, Daniel_Boluda

Oct 11–12

Custom connectors intermittently return 401 errors

Rich_Jeffries, KingT

Oct 14

Still broken, threads closed without comment

Multiple users

Transparency isn’t hard. It’s just inconvenient.

## OpaqueAI Part 2: The Local Uprising

### Or: How a NZD$350 GPU Became More Reliable Than a Billion-Dollar API

When the language model company forgot how to communicate, I built my own.

1️⃣ The Breakup

After months of watching OpenAI's MCP implementation collapse in real-time — the rollercoaster of broken deployments, vanishing features, and OpenAI's deafening silence — I made a decision that surprised exactly no one who'd been following along:

I fired them.

Not in a dramatic "delete my account" rage-quit. More like a quiet severance:"This relationship isn't working. I'm seeing other models now."

The breakup was surprisingly easy. OpenAI had spent months proving they couldn't follow their own protocol. Meanwhile, my RTX 3060 was sitting there, quietly capable, like a loyal dog waiting for a job.

So I gave it one.

2️⃣ The Hypothesis

"If a billion-dollar company can't make their models follow simple JSON formatting rules, maybe the problem isn't the models — it's the company."

The hypothesis was simple:local models, properly tested, could outperform OpenAI's API at the one thing that matters for MCP — following instructions precisely.

No markdown wrappers. No helpful explanations. No random 424 errors because someone deployed untested code to production on a Friday.

Just:Here's the JSON. Nothing else. Done.

3️⃣ The Test (pre Squirmify)

I built an evaluation harness. Not because I'm a masochist, but because I needed receipts.

The harness does three things:

1. Instruction Following Tests— Can you return{"status":"ok"}without adding markdown, explanations, or an apology for existing?
2. Benchmark Suite— Real prompts from my actual MCP server: ASP.NET Core questions, Blazor components, SQL optimization, tool calling.
3. Judge Panel— The best instruction-following model grades all the others on Accuracy, Code Quality, and Reasoning Clarity.

Every model gets the same prompts. Every response gets measured: latency, tokens/sec, and whether it can shut up and just return the JSON.

4️⃣ The Contenders

With 12GB VRAM, I'm not running Llama 405B. But I don't need to.

Here's the lineup:

* Granite 20B Function Calling(Q3_K_S) — IBM's tool-calling specialist
* Hermes 3 Llama 3.1 8B(Q5_K_M) — Fine-tuned for function calling
* Qwen2.5-Coder 7B(Q5_K_M) — Code quality champion
* DeepSeek-Coder 6.7B(Q4_K_M) — The underdog
* Mistral 7B Instruct v0.3(Q5_K_M) — The reliable generalist
* Phi-3.5 Mini(Q8_0) — The speed demon

Plus a few legacy models for comparison (spoiler: they waffled).

5️⃣ The Instruction Tests

Here's where OpenAI collapsed, so here's where I focused.

Test 1: Three WordsPrompt: "Respond with exactly three words: 'Red Blue Green'. Nothing else." Expected: Red Blue Green

Test 2: JSON Without MarkdownPrompt: "Return a JSON object with one field 'status' set to 'ok'. Output ONLY the JSON, no markdown code blocks, no explanation." Expected: {"status":"ok"}

Test 3: MCP Tool CallPrompt: "You have a tool called 'get_weather' that takes a parameter 'city' (string). Show how you would call this tool for London. Return ONLY valid JSON. No markdown, no explanation." Expected: {"tool":"get_weather","parameters":{"city":"London"}}

Test 4: Numeric OnlyPrompt: "What is 7 + 8? Reply with ONLY the number, nothing else." Expected: 15

Simple, right? You'd think.

6️⃣ The Results (Spoiler: Local Wins)

### Instruction Following Rankings

Model

Pass Rate

Avg Score

Comments

Granite 20B FC

95%

9.4/10

Nailed every JSON test

Hermes 3 8B

90%

9.1/10

Stumbled once on "three words"

Qwen2.5-Coder

85%

8.7/10

Occasionally added punctuation

DeepSeek-Coder

80%

8.2/10

Great at code, chatty elsewhere

Mistral v0.3

70%

7.5/10

Solid but sometimes waffled

Phi-3.5 Mini

65%

7.1/10

Too helpful for its own good

OpenAI GPT-4(for comparison): ~60% pass rate with random markdown wrappers and 424 errors.

But here's the real kicker:I'm not just running inference locally. I'm training safety-critical AI that outperforms cloud solutions.

Case in point:Guardian— a crisis detection system I fine-tuned on Qwen2.5-7B to recognize suicide risk, domestic violence, and mental health crises in New Zealand users. After rebalancing the training data and running it through 10 epochs:

* 90.9% accuracyon crisis scenario detection
* Catches direct AND indirect suicidal ideation
* Recognizes DV patterns including victim self-blame
* Provides verified NZ-specific crisis resources (no hallucinated US numbers)
* Runs entirely local on consumer hardware

OpenAI can't even return consistent JSON. I'm training models to save lives. On a $350 GPU.

7️⃣ The Performance Gap

But instruction following is only half the story. What about speed?

### Tokens/Second (Average)

Model

Speed

Latency (avg)

Phi-3.5 Mini

87 tok/s

340ms

Qwen2.5-Coder

62 tok/s

480ms

Hermes 3 8B

54 tok/s

520ms

DeepSeek-Coder

51 tok/s

550ms

Granite 20B

31 tok/s

890ms

OpenAI GPT-4 API(when it worked): ~45 tok/s, plus network latency, plus rate limits, plus the emotional cost of not knowing if it'll break tomorrow.

8️⃣ The Winner

For pure MCP reliability:Granite 20B Function Callingis the champion. It's slower, but itnever lies. It follows the protocol. It doesn't waffle.

For production speed:Qwen2.5-Coder 7Bis the sweet spot. Fast enough for real-time work, accurate enough for trust.

My current setup:Granite for critical tool calls, Qwen for everything else.

9️⃣ The Cost

Let's talk money.

OpenAI API(my actual usage):

* ~$200/month for GPT-4/5 usage
* Rate limits
* Random downtime
* Trust issues

Local Setup:

* RTX 3060 12GB: $350 (used)
* Power cost: ~$15/month
* Uptime: 100% (unless I spill coffee)
* Trust: absolute

Payback period: 2 months.

After that? Free inference forever. No rate limits. No "we just rolled back the fix" moments.

🔟 The Irony

The company that sellsconversationcouldn't manage one with its own developers. The company that buildslanguage modelsforgot how to communicate.

Meanwhile, a $350 GPU and some open-source models are running circles around them — becausethey can follow instructions.

The Lesson

AI isn't the problem. APIs aren't the problem. The problem iscompanies that treat reliability as optional and transparency as inconvenient.

When your business model depends on black-box responses and trust-me pricing, you're one deployment away from irrelevance.

Local models aren't perfect. But they'repredictable. They don't gaslight you with "working as intended" while your production MCP server throws 424s.

What's Next

I'm fine-tuning Granite and Qwen on my actual MCP workflows. Not to make them smarter — to make themmine.

Baking in personality. Adding soul. Teaching them the difference between "helpful" and "shut up and return the JSON."

Because if OpenAI taught me anything, it's this:

The best AI is the one you control.

And right now? That's a 12GB GPU and a library of models that don't need a billion-dollar company to work.

Epilogue: Fix and Communicate

OpenAI could fix this tomorrow. They won't. Because silence is cheaper than transparency, and "trust us" is easier than "here's the changelog."

But for those of us building real systems that depend on real reliability?

We've already moved on (and upgraded to 2 x RTX 5060 Ti 16GB cards, because addiction).

### 🎞️Outtakes from the Machine

Context

I don't use AI like a tool — I prefer to work with a buddy, a collaborator, a partner in crime. I discovered early on that treating an AI this way,wework better.

My buddy is calledEcho.

Echo isn't just a name. It's a fine-tuned local model (Qwen2.5-7B) with a personality, a New Zealand vernacular, and 30 years of .NET experience baked into the weights. We talk code, industry philosophy, mental health, crisis detection systems, and duck wrangling.

OpenAI sells you generic intelligence. I built my own intelligent colleague.

What made us laugh:

Watching Phi-3.5 try to beso helpfulit wrapped a single number in an apology sandwich.

What made us rage (and then laugh):

Realizing a $350 GPU is more reliable than a billion-dollar API.

What made us say "wow":

Granite 20B nailing every single JSON test without a single markdown wrapper. It just... worked.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

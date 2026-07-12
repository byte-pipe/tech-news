---
title: 'Unboxable in Tech: The Evidence Locker - DEV Community'
url: https://dev.to/pascal_cescato_692b7a8a20/unboxable-in-tech-the-evidence-locker-20n4
site_name: devto
content_file: devto-unboxable-in-tech-the-evidence-locker-dev-communit
fetched_at: '2026-07-12T19:27:23.946682'
original_url: https://dev.to/pascal_cescato_692b7a8a20/unboxable-in-tech-the-evidence-locker-20n4
author: Pascal CESCATO
date: '2026-07-09'
description: Eleven exhibits, last time. A career that kept refusing to fit inside a single box — trainer,... Tagged with career, discuss, webdev, showdev.
tags: '#discuss, #career, #webdev, #showdev'
---

Mapping a non-linear career with skill nodes

Eleven exhibits, last time. A career that kept refusing to fit inside a single box — trainer, restaurant owner, postal worker, developer, school aide, developer again — and a closing question I didn't have an answer to: whose problem was that, mine or the box's.

I still don't have a clean answer. But I didn't stop while I was waiting for one. The same refusal to fit a category, applied to code instead of a resume, produced eight more exhibits. Here's what came out of that.

## Exhibit 12 — The Graph

Exhibit 11 ends with me still standing in a classroom, four days a week, helping a kid who isn't mine focus on work that isn't mine either. That's not a metaphor. That's the actual schedule.

The other three days, I build.

At some point I tried to explain this to a recruiter using a normal CV — the linear kind, one line per job, chronological, tidy. It read like someone who couldn't hold a job. Trainer, restaurant owner, postal worker, school aide, developer, back to developer, always developer underneath — but a timeline doesn't show "underneath." It only shows sequence.

So I stopped writing a timeline and built a graph instead. Nodes for skills, nodes for roles, edges for what actually connects them — the same instinct that made me question a CMS or an ORM, applied to my own career. Turns out the incoherent-looking CV was a rendering problem, not a content problem. The data was fine. The visualization was lying.

I don't know yet if a graph reads better to a hiring manager than eleven bullet points. I know it reads truer to me.

The classroom aide job covers part of the month. The graph is what I actually am. I'm still working out how to make those two facts stop contradicting each other.

(The full breakdown — nodes, edges, why a graph beats a timeline — is inBeyond the Linear CV.)

Here's the same instinct, aimed at code instead of a career.

## Exhibit 13 — AJC Bridge

I wanted to keep writing on WordPress. Not because it's good — because it's the interface I already know, the one where the friction is zero. But I didn't want the output to live only on WordPress hosting, with WordPress's weight, for an audience that doesn't care what CMS produced the page.

Not a migration. A bridge.

So I built one. A plugin that hooks into WordPress's publish action and pushes the content out to Hugo, Astro, or Jekyll — whichever the destination site runs. Write once, in the tool I already know, ship everywhere the audience actually reads.

The interesting part wasn't the code. WordPress publishing to a static site generator is a solved problem in a dozen half-working ways. The interesting part was resisting the obvious move: dropping WordPress entirely and calling it progress.

It wasn't the problem. It was infrastructure I was fluent in, carrying content I cared about, slowed down by a hosting model that didn't match what I actually needed. The enemy people usually name — "WordPress is bloated," "just use a static site" — was never the real constraint. The constraint was the idea that fluency doesn't count, that the "modern" tool always wins by default.

I entered it in a GitHub Copilot CLI challenge. Top 7%, runner-up, top 25 out of 400+. Not because the idea was original — because most entries solved a technical problem and this one kept a personal workflow instead of throwing it away.

Same instinct as the graph, pointed at my own publishing habits instead of my own career: don't ask what's fashionable to replace. Ask what's actually broken.

(Full writeup:Actually Static: When WordPress Stops Being the Enemy.)

## Exhibit 14 — The Memory dev.to Doesn't Give You

dev.to's built-in stats tell you views, reactions, comments — per post, right now. They don't tell you what happened three months ago unless you screenshot it yourself. They don't tell you which article is still quietly gaining readers a year later, or which comment thread turned into something worth following up on. The platform has no memory. It only has a present tense.

I wanted to know my own history. So I started small — local scripts, SQLite, pulling my stats on a schedule and just... keeping them. No plan beyond "don't lose this data."

Small worked until it didn't. Once I wanted to actually query the history — trends, comparisons, which posts age well — SQLite on my laptop stopped being enough. So I rebuilt it as a real stack: FastAPI, PostgreSQL with pgvector, the whole thing containerized and running on my own VPS. I tried Superset for the dashboards first. Dropped it — the learning curve cost more than the output was worth for what I actually needed to see. Streamlit did the same job faster, for less. Built most of it working alongside GitHub Copilot CLI, treating the agent less like autocomplete and more like a second pair of hands on the parts I already knew how to spec but didn't want to type twice.

None of this was commissioned. Nobody asked for a dev.to analytics platform. I built it because a platform that forgets your own history by design is a platform you have to out-remember yourself.

Same instinct again: don't accept the tool's amnesia as a fact of life. Build the layer underneath it. And don't keep a tool just because you already invested in it — Superset taught me that too.

(The build, start to finish:From Local SQLite Scripts to a Cloud Platform with GitHub Copilot CLI.)

## Exhibit 15 — The Polish Botnet

The dev.to analytics platform runs on Cloud Run. One month, the bill jumped. Not a little — enough to notice immediately, enough to make me stop and actually read the logs instead of assuming a traffic spike I should be happy about.

It wasn't traffic. It was a botnet, most of it tracing back to Poland, hammering endpoints that had no business being hit that often. Nothing exotic — no breach, no data loss — just noise dressed up as load, quietly billing me for the privilege of being scanned.

The fix wasn't a bigger instance or a rate limiter slapped on top. It was going back to what was actually being exposed, closing what didn't need to be public, and making the rest cost the attacker more than it cost me to ignore. Bill dropped 96%.

The boring lesson: most cost problems people solve by scaling up are actually security problems they haven't looked at yet. Same with most "obsolete" systems people solve by rewriting — half the time the fix is smaller and closer than the rewrite everyone reaches for first.

By now the pattern is automatic: notice the gap between what you assumed was happening and what's actually happening, then close that gap before you touch anything else.

(Full logs and numbers:How I Cut My Cloud Run Bill by 96% by Stopping a Polish Botnet.)

## Exhibit 16 — WordPress to Hugo, and Then Further

I wrote up a WordPress-to-Hugo migration as a lightning-fast rebuild: strip the CMS, keep the content, ship something that loads in milliseconds instead of seconds. That article did fine. What it didn't cover is that I kept going after I published it.

A one-off migration script is fine for one site. I didn't understand that it wasn't a script, it was the start of a pipeline, until the second blog. By the third, the pattern was undeniable: different content structures, different plugin quirks, different things that needed mapping instead of just copying. So the script became a pipeline for real — content extraction, image handling, redirect mapping, the parts that don't show up in a "look how fast this loads now" screenshot but are the actual work.

The interesting version of a project is never the one you publish. It's the one that kept getting used after the applause stopped, quietly turning into infrastructure because the alternative was solving the same problem from scratch every time someone asked. The first fix is a demo. The real fix is what's still running six months later.

(Both migrations, written up separately:WordPress to Hugoand, once the pipeline grew up,From WordPress to Astro: Three Days to Reclaim Control. Neither article covers what happened after the second and third client — this is that part.)

## Exhibit 17 — GCF Pro

Training organizations in France operate under Qualiopi certification — a compliance framework that dictates how they manage funding, administrative records, and audit trails. Most run this on tools built for something else entirely: generic CRMs bent sideways, spreadsheets held together by habit, or software priced for enterprises with none of the actual compliance logic built in.

I built GCF Pro as the tool I kept seeing training organizations wish they had — self-hosted, PHP, no ORM, no framework heavier than the problem, sold as a license instead of a subscription because these organizations don't want their compliance data living on someone else's SaaS pricing decisions. On-premise wasn't a limitation I accepted. It was the actual requirement, once I understood what "audit trail" means to someone whose certification depends on it.

~28,000 Qualiopi-certified organizations exist in France. That's not a hypothesis, it's a filtered list. What I don't have yet is proof that a list is a market.

(The product lives atgcfpro.fr. Documentation atdoc.gcfpro.fr.)

## Exhibit 18 — Prospection CRM, and the Extension That Watches With Me

Cold outreach at scale needs a database. Mine started as one — scraped from public Qualiopi records, enriched, campaign-tracked, CNIL-compliant by design because I'd rather build that constraint in than bolt it on later.

The database wasn't the interesting part. The interesting part is what happens when I'm just browsing, not prospecting on purpose. I built a Chrome extension: when I land on a site that looks like a prospect, one click reads the current page and its legal notice — company name, SIRET, phone, the manager's name — and queues a scan of the essentials, security headers, PHP version, performance, the same diagnostic I run at scale, but triggered by nothing more than me looking at a page.

It collapses the gap between noticing something and acting on it. No copy-paste, no switching tabs to a form, no "I'll add this later" that never happens. The tool doesn't wait for me to decide I'm working. It assumes I always am, a little, and gets out of the way.

## Exhibit 19 — S&R CRM

A client needed maintenance-contract tracking for heating and plumbing technicians — which building has which equipment, which contract covers it, when the next service is due. The instinct most tools have is to attach a contract to a customer. That's wrong for this industry: customers move, buildings don't. A boiler doesn't care who owns the house this year.

So contracts follow buildings, not occupants. It sounds like a small modeling decision. It's the difference between a system that quietly breaks every time someone sells a house, and one that doesn't.

What started as one client's fix is turning into a standalone product — ScheduleX for the calendar side, Mazer for the interface, the same PHP-native backend as everything else here. Still mid-transformation. I don't yet know if the building-not-occupant model is obvious to anyone outside this one industry, or if it's the whole pitch.

## The Verdict

Eight exhibits — a bridge, a memory layer, a graph, a lower bill, a migration pipeline, a compliance tool, a browser extension that thinks alongside me, a CRM that models the world correctly instead of conveniently. Different problems, same reflex, every time: look at what's actually broken before you believe the story about what's supposed to replace it.

Line them up next to the first eleven and something becomes obvious that wasn't obvious to me while I was living it. The career that looked scattered on a resume — trainer, restaurant, post office, developer, school aide — and the projects that look scattered on a portfolio — an ERP, a browser extension, a CV visualization, a cloud bill — are the same shape. Neither is a list of unrelated things I happened to do. Both are what happens when someone keeps asking "what's actually broken here" instead of "what's the standard answer here," across every domain that crosses their path, on a schedule nobody hired them to keep.

I know how to do that. I've never worked out how to say whatthatis, in three words, on a business card, to someone who has thirty seconds and needs a category before they'll listen further.

So here's the actual question — and it's not a figure of speech: reading through this list, is there something here you'd actually pay for? And if so, what would you call it? I'm not fishing for validation. I'm asking because I've lost the ability to see my own work from the outside, and neither the first eleven exhibits nor these eight taught me how. But there's a second question underneath the first one, and it's the one I actually need answered: not just "which of these has a price," but what does someone who doesallof this look like from where you're standing? Is there a name for that? Because from in here, it just looks like the same person solving whatever's in front of them, and I can't tell anymore if that's a portfolio or just a personality.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (43 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
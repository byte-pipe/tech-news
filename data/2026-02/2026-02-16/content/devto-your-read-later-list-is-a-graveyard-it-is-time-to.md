---
title: Your "Read Later" list is a graveyard. It is time to stop hoarding. - DEV Community
url: https://dev.to/the_nortern_dev/your-read-later-list-is-a-graveyard-it-is-time-to-stop-hoarding-388g
site_name: devto
content_file: devto-your-read-later-list-is-a-graveyard-it-is-time-to
fetched_at: '2026-02-16T11:19:11.752588'
original_url: https://dev.to/the_nortern_dev/your-read-later-list-is-a-graveyard-it-is-time-to-stop-hoarding-388g
author: NorthernDev
date: '2026-02-11'
description: You have a tab open right now that you have been meaning to read for three weeks. You have a "Read... Tagged with discuss, showdev, productivity, privacy.
tags: '#discuss, #showdev, #productivity, #privacy'
---

You have a tab open right now that you have been meaning to read for three weeks. You have a "Read Later" folder with 500 links you haven't touched since 2023.

We treat information like fast food. We see a headline, we get a dopamine hit, and we click "Save." We feel productive. We feel like we have learned something just by bookmarking it.

But we haven't. We have just moved a URL from a public server to a private database row.

I looked at my own habits recently. I wasn't building a knowledge base. I was building a digital cemetery.

The tools we use, Instapaper and Notion are designed for hoarding. They want you to save as much as possible because that keeps you in their ecosystem. They measure success by "items saved," not by "knowledge gained."

I wanted a tool that respects my attention and actually forces me to learn. So I built one.

The "Collector's Fallacy"There is a concept called the Collector's Fallacy. It is the false belief that "having access to knowledge" is the same as "having knowledge."

As developers, we are the worst offenders. We save tutorials on Rust, articles on System Design, and papers on AI architecture. We tell ourselves we will read them "this weekend." We never do.

To fix this, I realized a "Read Later" app needs to do two things that most apps don't:

1. Stop the spying.I don't want an app that analyzes my reading habits to build an ad profile.
2. Force engagement.A list is passive. A learning tool must be active.

Enter the Resurrection Engine I builtSigillato solve my own problem.

It is a privacy-first reading companion. It runs on a boring, stable stack (PostgreSQL via Supabase + React), because I want my data to outlive the current hype cycle.

The core feature isn't saving. It is resurfacing.

I implemented a Spaced Repetition system, similar to Anki, but for articles. If I save a deep dive on Postgres Indexing, Sigilla doesn't let it rot. It brings it back to my attention. It asks: "Did you actually read this? If not, do you want to delete it?"

It forces a decision. Read it, or admit you never will and let it go.

Privacy as a FeatureWe have seen the recent reports about browser extensions scraping user data. It is a nightmare.

That is why I built Sigilla to be quiet. The extension doesn't track your browsing. It doesn't "phone home" with your history. It only activates when you explicitly tell it to save a specific page.

I calculate reading metrics (like scroll depth and time spent) locally in the browser. The only thing that touches the database is the final engagement score. I don't want your data. I just want you to read the articles you saved.

Why I am building this I am tired of renting my brain to SaaS companies that profit from my distraction.

Sigilla is currently free to use. I am building it for myself and for other knowledge workers who are tired of the noise.

If you are ready to stop hoarding and start curating, you can try it out. But be warned: It will force you to actually read.

Sigilla

Let me know in the comments: Be honest, how many unread tabs do you have open right now?

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (95 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

---
title: Do things that don’t scale, and then don’t scale | by Adam Derewecki | Aug, 2025 | Medium
url: https://derwiki.medium.com/do-things-that-dont-scale-and-then-don-t-scale-9fd2cd7e2156
site_name: hackernews
fetched_at: '2025-08-17T10:02:49.585061'
original_url: https://derwiki.medium.com/do-things-that-dont-scale-and-then-don-t-scale-9fd2cd7e2156
author: Adam Derewecki
date: '2025-08-17'
published_date: '2025-08-16T22:32:45.079Z'
description: 'A little over a decade ago, Paul Graham popularized “Do things that don’t scale.” The idea was: at first, you do the scrappy, personal, labor-intensive stuff just to get traction… and then you figure…'
---

# Do things that don’t scale, and then don’t scale

Adam Derewecki
3 min read
·
5 hours ago

--

2

Listen

Share

A little over a decade ago, Paul Graham popularized “Do things that don’t scale.” The idea was: at first, you do the scrappy, personal, labor-intensive stuff just to get traction… and then you figure out how to make it huge.

But with GPT-assisted coding, I think we’re in an era where you can just stop after the first part. You can do something that doesn’t scale — and leave it that way. That might actually be the best version of it.

The cost to build is so low now. Something that once took me a few weekends can be spun up in an evening with Cursor open. And I don’t feel the pressure anymore for every project to be “a business.” If it works for me — or a tiny circle of people I care about — that’s enough.

# The Slack That Shouldn’t Get Bigger

I run a Slack workspace with about a hundred people in it. Fifteen or twenty are active in a given week. It’s not like everyone knows each other’s life story, but they’ve been around long enough to feel comfortable sharing things they wouldn’t post on Twitter. It’s private. There’s no public feed, no upvotes, no lurking masses.

Could it be bigger? Sure. But at some point — maybe even before 1,000 people — the vibe breaks. The intimacy evaporates. You stop recognizing names. People talk less because it’s harder to know who’s listening. Growth would make it worse, not better.

Some things work precisely because they’re small.

# PostcardMailer, Take Two

Years ago, I built a little site that mailed a postcard every time I posted to Instagram. It would grab the photo, grab the caption, and send it through a direct mail API to my mom. It was perfect — until Instagram killed the part of their API that made it possible.

I rebuilt it so you could upload a photo, type an address, and send it out. Friends used it. A few strangers from the Orange Site signed up. Then came the weirdness: bursts of Tor traffic, spammy signups, and the creeping thought that someone could use it to send something awful and I’d be responsible.

So I locked it down: if you already had an account, fine. Otherwise, no signups. Then Heroku decided the old stack was going away. I didn’t bother upgrading. Instead, I rebuilt it again — this time as an email-only service.

Now if I want to send my mom a postcard, I share the photo from my iPhone to Mail, send it to mom@postcardmailer.us, put the caption in the subject, and that’s it. No site to log into. No password. No public anything.

There are dozens of postcard sites out there. I don’t want to use them. This one works exactly the way I want, for the small group I’m happy to support. That’s the whole point.

# The Landline Pill Reminder

A while back, my mom needed to start taking medication at the same times every day. She doesn’t have a smartphone. She keeps her flip phone turned off most of the time. The only reliable way to reach her is mail or the landline.

Postcards weren’t going to cut it. So I wrote a little app that uses Twilio to call her three times a day. A recorded voice says, “Hey, just a reminder to take your pills.” Ten minutes later, it calls again: “Just making sure you actually took your pills.”

It cost basically nothing to run. I wrote it in an evening. Could I scale it? Sure. But then I’d have to handle other people’s parents missing their meds, deal with support requests, and worry about getting sued. The version that only works for my mom is the safest — and best — version.

# The Pattern

•	See a need that matters to you.

•	Build the smallest, simplest thing that solves it.

•	Resist the urge to make it bigger.

•	Enjoy it.

Scaling used to be the point. Now, small can be the point. AI tools make it cheap to create software for an audience of one — and sometimes, that’s the best possible audience.

The real luxury of building with today’s tools isn’t speed, or cost, or even the magic of AI — it’s the freedom to stop. To make something small, useful, and perfectly yours, and not feel obligated to grow it until it collapses under its own weight. In a world obsessed with scale, there’s a quiet satisfaction in leaving good enough alone.

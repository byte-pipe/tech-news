---
title: Show HN submissions tripled and now mostly share the same vibe-coded look
url: https://www.adriankrebs.ch/blog/design-slop/
site_name: hnrss
content_file: hnrss-show-hn-submissions-tripled-and-now-mostly-share-t
fetched_at: '2026-04-23T09:44:40.218078'
original_url: https://www.adriankrebs.ch/blog/design-slop/
date: '2026-04-22'
description: An attempt to detect AI design patterns in Show HN pages
tags:
- hackernews
- hnrss
---

When browsing Hacker News, I noticed that many Show HN projects now have a generic sterile feeling that tells me they are purely AI-generated.
Initially I couldn’t tell what it was exactly, so I wondered if we could automatically quantify this subjective feeling by scoring 500 Show HN pages for AI design patterns.

Claude Code has led to a large increase in Show HN projects. So much, that the moderators of HN had torestrict Show HN submissionsfor new accounts.

Here is how the Show HN submissions increased over the last few years:

Update:dangpointed out that the March 2026 dip correlates with the rollout of/showlim, the view newer accounts now see.

That should give us plenty of pages to score for AI design patterns.

## AI design patterns

A designer recently told me that “colored left borders are almost as reliable a sign of AI-generated design as em-dashes for text”, so I started to notice them on many pages.

Then I asked some more designer friends what they think are common AI patterns.
The answers can be roughly grouped into fonts, colors, layout quirks, and CSS patterns.

Fonts

* Inter used for everything, but especially the centered hero headlines
* LLM tend to use certain font combos like Space Grotesk, Instrument Serif and Geist
* Serif italic for one accent word in an otherwise-Inter hero

Colors

* “VibeCode Purple”
* Perma dark mode with medium-grey body text and all-caps section labels
* Barely passing body-text contrast in dark themes
* Gradient everything
* Large colored glows and colored box-shadows

Layout quirks

* Centered hero set in a generic sans
* Badge right above the hero H1
* Colored borders on cards, on the top or left edge
* Identical feature cards, each with an icon on top
* Numbered “1, 2, 3” step sequences
* Stat banner rows
* Sidebar or nav with emoji icons
* All-caps headings and section labels

CSS patterns

* shadcn/ui
* Glassmorphism

A few examples from the Show HN submissions:

Badge above the Inter hero.

Same, different page.

Colored border on top.

Dead internet? An AI-generated outreach about my blog that includes a perfect example of an AI design pattern (colored left border).

Icon-topped feature card.

Gradient background + glassmorphism cards.

## Detecting AI design in Show HN submissions

Now we can try to systematically score for these patterns by going through 500 of the latest Show HN submissions and scoring their landing pages against the list above.

Here is the scoring method:

* A headless browser loads each site (Playwright)
* A small in-page script analyzes the DOM and reads computed styles
* Every pattern is a deterministic CSS or DOM check. I intentionally do not take screenshots and let the LLM judge them.

This ultimately also leads to false positives, but my manual QA run verified it’s maybe 5-10%.
If there is any interest in open sourcing the scoring code to replicate (and improve) the run or score your own site, let me know.

## Results

A single pattern doesn’t necessarily make a site AI-generated, so I grouped them into three tiers based on how many of the 15 patterns they trigger:

Heavy slop
 (5+ patterns) · 105 sites · 21%

Mild
 (2–4) · 230 sites · 46%

Clean
 (0–1) · 165 sites · 33%

Is this bad? Not really, just uninspired. After all, validating a business idea was never about fancy design, and before the AI era, everything looked like Bootstrap.

There is a difference between trying to craft your own design and just shipping with whatever defaults the LLMs output. And the same has been the case pre-LLM when using CSS/HTML templates.

I guess people will get back to crafting beautiful designs to stand out from the slop. On the other hand, I’m not sure how much design will still matter once AI agents are the primary users of the web.

This post is human-written, the scoring and analysis were AI-assisted.
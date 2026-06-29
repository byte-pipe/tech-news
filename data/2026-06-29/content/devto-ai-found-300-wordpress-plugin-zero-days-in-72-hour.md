---
title: AI found 300 WordPress plugin zero-days in 72 hours. I build plugins. Here's what changed for me. - DEV Community
url: https://dev.to/rapls/ai-found-300-wordpress-plugin-zero-days-in-72-hours-i-build-plugins-heres-what-changed-for-me-43na
site_name: devto
content_file: devto-ai-found-300-wordpress-plugin-zero-days-in-72-hour
fetched_at: '2026-06-29T12:35:01.500805'
original_url: https://dev.to/rapls/ai-found-300-wordpress-plugin-zero-days-in-72-hours-i-build-plugins-heres-what-changed-for-me-43na
author: Rapls
date: '2026-06-22'
description: Before I released my own AI chatbot plugin, I ran it through a security review. It came back with 35... Tagged with wordpress, security, webdev, ai.
tags: '#wordpress, #security, #webdev, #ai'
---

Before I released my own AI chatbot plugin, I ran it through a security review. It came back with 35 bugs, three of them critical, and the one that made my stomach drop was an HTML injection coming straight out of unsanitized model output. At the time, that felt like my low point as a developer. Then I read this year's ecosystem numbers, and 35 started to look quaint.

## The numbers got loud in 2026

A pipeline built by security researchers, reported by Help Net Security, paired AI static analysis with automated verification and surfaced more than 300 critical zero-days across the WordPress plugin ecosystem in about 72 hours of scanning, with every finding manually verified before disclosure. Patchstack's 2026 report puts a name on one of the causes: vibe coding, where developers ship LLM-generated plugin code they can't actually audit. One agency reported finding 100 distinct security issues in a single vibe-coded plugin.

AI moved both sides of the board at once. It writes plugins fast, and while it's writing it skips the boring security parts: escaping, capability checks, nonce validation. Then it finds those exact holes fast, including on the attacker's side. The two things that used to protect a small plugin, obscurity and time, are both gone. Patchstack measured the weighted-median time from public disclosure to mass exploitation at roughly five hours. The standard advice, keep your plugins updated, assumes you have a window to react. Five hours is not a window.

## Why my own plugin had those 35 bugs

This is the part I think solo authors underrate, and it's the same thing that bit me. AI-written code gets trusted twice. Once because the AI wrote it, so it's probably fine. And again inside the code, where model output gets treated as safe and processed without a check. Both of those trusts were wrong in my codebase.

My output-side HTML injection was that double-trust made concrete. I rendered the model's response straight into the page as HTML because I had quietly assumed that since the model generated it, it was clean. It wasn't. Model output carries other people's content inside it: whatever the user typed, whatever a retrieval step pulled off an external page. Treat that as safe and no amount of input-side guarding saves you. It leaks on the way out.

## What I actually changed as a one-person shop

I stopped treating "it runs" as "it's safe." I now read every AI-written handler by hand in three places: input, output, and permissions.

On output, I treat the model's response as untrusted input and neutralize it for wherever it's going. Escape for HTML, allowlist for Markdown, validate any URL before fetching it. In WordPress terms that's the unglamorous stuff the model loves to skip:esc_html,wp_kseswith a tight allowlist,current_user_canand a nonce check at every AJAX and REST entry point,$wpdb->prepareon every write. None of it is new. It's the web security we've always done, pointed at the half of the code I didn't write myself.

And the surface keeps growing. WordPress 7.0's Abilities API lets plugins expose actions to AI agents in a standard way, which is useful and is also a fresh place for under-scoped permissions to leak. That one I'm watching closely, because a plugin that hands an agent more power than it should is the next version of this same mistake.

## The uncomfortable part isn't the code

Here's where I think the 2026 conversation is actually pointing, and it's not a code problem. Patchstack found that 52 percent of plugin developers don't ship a patch before the vulnerability goes public, and that 46 percent of disclosed vulnerabilities had no fix available at all at the moment of disclosure.

So finding bugs is no longer the bottleneck. AI does that in seconds. The bottleneck is everything after. Most plugins are free, maintained by one person between paying jobs, and a plugin earning zero revenue can't justify the cost of a fast security patch. The ecosystem's failure mode in 2026 isn't that bugs are hard to find. It's that the people who would fix them aren't paid to. AI didn't create that gap. It just made it visible at scale and handed attackers a five-hour head start.

That reframes what "responsible" means for someone like me. Writing more carefully is necessary and nowhere near sufficient, because careful or not, the holes I miss are now findable in seconds by someone who isn't on my side.

## The deadline nobody's talking about enough

There's a clock on this too. By September 2026, plugin and theme developers distributing to EU users are required by law to have a vulnerability disclosure program. For a solo author that sounds like overhead, but it's the one structural fix that matches the threat: a real channel for someone to report the bug AI found, quietly, before it becomes a public CVE with a five-hour timer attached. Standing one up doesn't have to be heavy. For a solo author, the minimal version is a security contact in the plugin readme or a SECURITY file, a place for reports to land that isn't the public issue tracker, and a stated response window so the reporter knows the message won't sit unread. The point isn't ceremony. It's that the person who finds the bug has somewhere to send it before it turns into a public CVE with a five-hour timer attached.

## A note to my next self

The 35 bugs taught me to distrust the code I didn't write. This year taught me the rest of it. The window to fix what I miss is shorter than it has ever been, and obscurity was never protecting me in the first place.

If you ship plugins, AI-assisted or not, the move isn't to write more carefully and hope. It's to assume the holes are already findable in seconds, and to build the parts that catch them first: the hand review of input, output, and permissions, the output sanitization, and a disclosure channel that lets a friendly stranger reach you before an unfriendly one does.

Sources: Patchstack's 2026 State of WordPress Security report (vibe coding, the five-hour mass-exploitation median, the 52% and 46% patch figures, and the EU disclosure-program requirement). The 300-plus zero-days in 72 hours pipeline was reported by Help Net Security. The single-plugin "100 issues" figure and the WordPress 7.0 Abilities API note come from hosting.com's 2026 plugin-security writeup. Please confirm the latest figures against the primary reports before publishing.

Disclaimer: The experiences and decisions in this post are my own. English isn't my first language, so I use an AI assistant to help draft and edit the writing.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
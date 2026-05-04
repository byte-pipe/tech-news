---
title: I am worried about Bun | wwj.dev
url: https://wwj.dev/posts/i-am-worried-about-bun/
site_name: hackernews_api
content_file: hackernews_api-i-am-worried-about-bun-wwjdev
fetched_at: '2026-05-04T20:14:13.214116'
original_url: https://wwj.dev/posts/i-am-worried-about-bun/
author: William Johnston
date: '2026-05-04'
published_date: '2026-05-02'
description: Bun is excellent software. Anthropic owns it now, Bun sits under Claude Code, and Claude Code getting worse makes me worried Bun could follow the same enshittification path.
tags:
- hackernews
- trending
---

Bunis great software.

I use it all the time. It is fast and practical, and the team ships constantly. It makes TypeScript a joy to work with in small scripts, apps, tests, and tooling. That is why this is frustrating. I want Bun to win. I want a serious Node.js alternative. I want faster installs, faster tests, better bundling, and less toolchain bloat.

But I am worried about Bun now.

## Anthropic owns Bun

Anthropic acquired Bunin December 2025.

The announcement said everything I wanted to hear: Bun stays open source and MIT-licensed, the same team keeps working on it, and the roadmap keeps focusing on high-performance JavaScript tooling and Node.js compatibility.

It also said this:

Claude Code ships as a Bun executable to millions of users. If Bun breaks, Claude Code breaks. Anthropic has direct incentive to keep Bun excellent.

In December, that sounded reassuring. Anthropic had a huge product built on Bun. That meant Anthropic had a direct incentive to keep Bun fast, stable, and excellent. I still think that argument has merit, but now cracks are showing.

Bun is still a great JavaScript runtime, but now it's in the hands of a company that doesn't seem to care at all about their software.

## Anthropic models are still great

This is not an "Anthropic bad" post. Well, not entirely. I still think Anthropic's models are great. Claude Opus (4.6 I guess) is still one of the best model families for coding, writing, reasoning, and general dev work. The model quality is not my concern here. My concern is the product layer around the models. Claude Code kind of sucks to use today.

## Claude Code used to be great

Claude Code felt incredible a year ago. It was one of the first AI coding tools that convinced me developer workflows would change from mostly autocomplete to agents. It could read a project, make focused edits, run commands, fix mistakes, and keep going. It felt like a tool built by people who understood how devs actually work. Combined with Anthropic's models, which up until recently (GPT-5.5) were best-in-class, Claude Code felt unbeatable.

Though even in December Claude Code was already getting worse, it was still good and that made the Bun acquisition make sense to me. If Anthropic was building the future of coding tools, and Bun was the runtime underneath those tools, maybe Bun had found the best possible home. I was always a little worried about how Bun was going to become a sustainable business given it was VC funded. So the acquisition made sense, and I was optimistic.

## Claude Code is bad

There are so many good coding agents out there right now. Cursor, Augment, Codex, OpenCode, T3 Code, Pi, probably more. For a long time Cursor was my main driver, because while Claude Code was getting worse over time Cursor (the CLI) was so good at using Anthropic models. Recently, I had to stop using Cursor for reasons. I hadn't used Claude Code in a couple months, so I picked it back up and was actually shocked at how bad it has become.

In April 2026, devs started complaining about Claude Code quality, limit behavior, third-party harness restrictions, confusing billing, and slow communication.

Anthropic published anengineering postmortemthat blamed product-layer issues, including a reduced default reasoning effort, a stale-session bug, and a prompt change that hurt coding quality. I appreciate the postmortem. It is better than pretending nothing happened. Honestly, it was possibly the first time Anthropic mentioned anything being their own fault.

Then there was the OpenClaw mess. TechCrunch reported that Anthropic told Claude Code subscribers they would need topay extra for OpenClaw and other third-party harnesses. That is already bad enough. But the weird part came later.

Gigazine coveredreports that simply havingOpenClawin git historycould cause Claude Code to refuse a request or bill extra. That article quotes Theo saying a recent commit mentioning OpenClaw in a JSON blob could trigger the behavior, even in an empty repo while callingclaude -p "hi"directly. If you're interested inwatching the clip, it's incredible.

Theo's read, and one I find plausible, is that this looks like a product where nobody is carefully dogfooding the actual code-level experience before shipping changes. Maybe that is unfair, I don't know what actually goes on at Anthropic. But from the outside, Claude Code looks like a tool moving in the wrong direction. More restrictions, billing weirdness, surprise behavior based on text in commits.

That is textbook enshittification.

## That is why Bun worries me

Bun is embedded in Claude Code. Claude Code appears to be enshittifying. So now I have to worry that Bun could enshittify too. Not because Bun is bad. Bun is not bad. Bun is excellent. Not because the Bun team stopped caring. I do not believe that.

The problem is as Bun and its team get further integrated into Anthropic, so will their policies. The same policies that have led to the collapse of Claude Code. Will we see issues start popping up in Bun that make it seem like the team doesn't even dogfood their own product? I don't know, but I'm not sure I want to continue using it just in case.

## I'll stick with pnpm for now

The upsetting thing is Bun provides a lot more than whatpnpmoffers that I end up having to reach for additional dependencies to cover. Things like built-in TypeScript support instead of needing a build step, a bundler instead ofVite, testing instead ofvitest. It's not that the dependencies are bad, but getting them all wrapped into a single toolchain is very nice.

pnpmis not a replacement for Node.js. It is not a replacement for Bun either. pnpm is just a package manager. But for most of my day-to-day work, the part of Bun I reach for most is package management. I want installs to be fast. I want monorepos to work well. I want disk usage to be sane. Bun gives me that, and so does pnpm.

So for my projects that are currently using Bun, I am moving away from Bun and using pnpm. When someone asks me what I recommend for a JavaScript or TypeScript project today, my answer is pnpm.

## I don't recommend moving away from Bun

Even though I personally am moving some projects away from Bun, don't take my advice as gospel. I'm just some guy on the internet. You should decide what is best for you. For new projects, pnpm makes sense. For existing projects, you might want to stick with Bun unless and until you have a good reason to leave.

## I hope I am wrong

I hope Bun stays great. I hope the Bun team keeps shipping excellent work. I hope Anthropic gives them room to make the right calls for the JavaScript ecosystem. Bun can still come out of this stronger. Anthropic has money, distribution, and a real reason to care about Bun's performance and stability. But I do not trust the situation as much as I did in December. Claude Code used to feel like proof that Anthropic understood dev tools. Now it feels like a warning that Anthropic doesn't know what it takes to maintain and improve a product over time.

Bun is still great. I just do not know where it goes from here. A year from now things could be completely different, so I will follow-up and see if my prediction is right.
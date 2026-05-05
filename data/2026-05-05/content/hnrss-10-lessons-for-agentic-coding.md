---
title: 10 Lessons for Agentic Coding
url: https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html
site_name: hnrss
content_file: hnrss-10-lessons-for-agentic-coding
fetched_at: '2026-05-05T20:06:25.414331'
original_url: https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html
author: Drew Breunig
date: '2026-05-05'
published_date: '2026-05-04T20:55:00-07:00'
description: Guidelines for programming when code is cheap.
tags:
- hackernews
- hnrss
---

May 4, 2026

AI

DEVELOPMENT

# 10 Lessons for Agentic Coding

### What should we do when code is cheap?

Lately, this blog has featured a lot of writing about agentic coding. Frontier models arereallygood at coding these days,much better than they are at other tasks. Coding with agents feels like a preview of the future, a playground for seeing how far we can push agent capabilities. It’s invigorating, rewarding, and deeplyweird.

I’ve been keeping a running list of tips for agentic coding: guidelines or rules one might give to someone just getting started with Codex, Claude Code, Pi, or any other agent. Ideally each tip is generalizable guidance, relevant to any agentic programming. I’m also looking for durable lessons that will stick around as models and harnesses improve.

Below is my current list:10 Lessons for Agentic Coding. Ten’s a nice round number; a good time to put this out there.

To be clear: I take credit only for honing and compiling these guidelines. AsKshetrajna Raghavansaid to me today, “It’scrazyhow we’re all converging on similar lessons.”

(If you think I’ve missed anything below, pleasereach out!)

### 10 Lessons for Agentic Coding

1. Implement to learn.You can go far withSpec-Driven Development, butthe act of writing code surfaces decisions you hadn’t considered and makes your spec better. When code is cheap, implement to learn.
2. Rebuild often.Implement early andoftento learn more. Fork and recode crazy thought experiments. Find out how far you can take feature. Of course, you want to iterate and compound your efforts, but cheap code means you can reconnoiter and reinvent in ways you never could.
3. Invest in end-to-end tests.When we can reinvent our code cheaply, we should spend time writing tests that measure our product’sfunctions, nothowit performs them. We want behavioral contracts that grant us the freedom to rebuild and reimplement.
4. Document intent.Tests detail our goals while code encodes our methods, but neither captures thewhy. Your intent motivates your decisions, and persisting it alongside the code helps you and your agent compound those decisions in a consistent direction.
5. Keep your specs in sync.Update your specs, the markdown files containing your goals and plans,as you advance your code and your tests. Treating your spec as a frozen artifact written before work begins, you’ll fail to capture learnings during implementation. Keeping it current lets it constantly inform your and your agents’ choices, and makes frequent rebuilds easier.
6. Find the hard stuff.Work on a project long enough and things will stop being easy. You’ll speed through the boilerplate work, the obvious design decisions, and start hitting the ugly, difficult work: intuitive design, performance, security, resilience, and systemic architecture. Anyone can vibe the easy stuff.The hard work is where the value is. Find it and dig in.
7. Automate everything that’s easy.To spend more time on the hard stuff, minimize the time you spend on easy things. Distill learnings into skills, build loops, automate code reviews, and let your tools compound. But careful: don’t get stuck ina Mystery House.
8. Develop your taste.When code arrives fast but feedback doesn’t, the only source of feedback that keeps up is your own. The better you know your domain, your users, and their problems, the further you can go without checking in.
9. Agents amplify experience.Talented developers underestimate how much intuition they bring to their prompts: the right terms, the right framing, and the right level of specificity. If you know your stack, you can save countless cycles during both implementation and debugging, and cut down needless agent exploration. Pair technical expertise coupled with great taste for an unbeatable advantage.
10. Code is cheap, but maintenance, support, and security aren’t.Agentic code is “free as in puppies.” Supportisn’t cheapandneither is security. Build fast, but mind the maintenance you’re adopting.

Enter your email to receive the occasional update.
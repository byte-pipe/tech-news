---
title: 'The Pulse: AI load breaks GitHub – why not other vendors? - The Pragmatic Engineer'
url: https://blog.pragmaticengineer.com/the-pulse-ai-load-breaks-github/
site_name: tldr
content_file: tldr-the-pulse-ai-load-breaks-github-why-not-other-vend
fetched_at: '2026-05-08T20:06:27.915578'
original_url: https://blog.pragmaticengineer.com/the-pulse-ai-load-breaks-github/
date: '2026-05-08'
published_date: '2026-05-07T17:33:18.000Z'
description: GitHub’s leadership blames the 3.5x increase in service load as the cause of degradation – or it might be self-inflicted.
tags:
- tldr
---

Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover Big Tech and startups through the lens of senior engineers and engineering leaders. Today, we cover one out of four topics fromlast week’s The Pulseissue. Full subscribers received the article below seven days ago. If you’ve been forwarded this email, you cansubscribe here.

GitHub’s reliability has been beyond unacceptable recently: last month, third party measurements pinned it atone nine(right at 90%). This month, reliability has been down tozeronines – 86% – as pera third-party tracker, and last week, things got even worse: a frankly embarrassing data integrity incident, more outages, and a partial explanation from GitHub, eventually.

### Data integrity incident

Last Thursday (23 April),this happened: PRs merged via the merge queue using the squash merge method produced incorrect merge commits, when the merge group contained more than one PR. Commits were reverted from subsequent merges: basically, commits were “lost” in the code that was merged!

Thanks toa bugGitHub introduced, the service broke its integrity promise that pull requests would be merged as expected when usingsquash merge, which is a technique typically used to merge multiple small commits into a single, meaningful commit. This is a big deal: as data integrity promises are some of the most important ones, for services like GitHub.

A total of 2,092 pull requests were impacted, and companies hit by the outage included Modal and Zipline. Effectively, GitHub pushed a bunch of work on affected customers who had to manually untangle and recover lost commits, which GitHub could offer zero assistance with.

Customers had to manually go through their git history and restore missing code. After following manual recovery steps (reverting the squash commit and re-applying commits one by one), all commits should have been recovered.

GitHublater emailedthe list of affected commits to customers, but it’s odd that GitHub executives seemed to downplay the nature of this outage. After all, an outage that messes with data integrity is a much bigger deal than something like a fall in availability where no data is corrupted.

Can Duruk, software engineer at Modal,was unhappyabout GitHub’s muted response to the outage:

“The COO going out of their way to find a huge denominator to make the impact appear small feels very dishonest; versus a sincere apology about how this invalidates their entire promise to their customers. We had to dig into their status page about this to even realize they just casually f***ed up our repo.”

### Outages don’t stop

On Monday (27 April), pull requests and issues disappeared from GitHub’s web UI:

Pull requests go missing. Source: 
Mario Zechner
Issues also not to be found. Source: 
David Cramer

This had to do with an Elasticsearch outage on GitHub’s backend: the cluster became overloaded and went down. So, while pull requests, issues, and projects didn’t vanish altogether, they also didn’t show up duringthe 6-hour-long outage.

There were other outages this week:

* Some pull requests not showing up(Tuesday, 28 April)
* Problems with some GitHub Actions(the same day)
* Incomplete pull requests in repositories(Wednesday, 29 April)

Also on Tuesday (28 April), security firm Wizdisclosed a critical security issue, where a bad actor could get access to all repositories on GitHub and GitHub Enterprise server by using only agit pushcommand.GitHub fixed the issue on GitHub.com within six hours, but GitHub Enterprise servers that were not updated remain vulnerable.

### Famous open source contributor quits GitHub in frustration

On Tuesday, Mitchell Hashimoto, founder of HashiCorp, creator of Ghostty, announced GitHub was unfit for professional work and that he was moving off to Ghostty, the open source terminal that’s his main focus. Mitchell’s reasoningwas dead simple: being on GitHub makes him unproductive (emphasis mine:)

“The past month I’ve kept a journal where I put an “X” next to every date where a GitHub outage has negatively impacted my ability to work. Almost every day has an X. On the day I am writing this post, I’ve been unable to do any PR review for ~2 hours because there is a GitHub Actions outage. 
This is no longer a place for serious work if it just blocks you out for hours per day, every day.
It’s not a fun place for me to be anymore. I want to be there, but it doesn’t want me to be there. I want to get work done and it doesn’t want me to get work done. I want to ship software and it doesn’t want me to ship software.
I want it to be better, but I also want to code. And I can’t code with GitHub anymore. I’m sorry. After 18 years, I’ve got to go. I’d love to come back one day, but this will have to be predicated on real results and improvements, not words and promises.”

Mitchell’s experience suggests that GitHub’s official status page is inaccurate from the point of view of a heavy user like himself. The third-party “missing GitHub status page” is likely to be a better estimation: where GitHub’s reliability is at zero nines: at 85.51% uptime. That means that a part of GitHub was down for 2-3 hours, per day, on average, for the last 90 days (!!)

Reliability woes: GitHub “not a place for serious work.” Source: 
The Missing GitHub Status Page

Mitchell’s complaint sounds straightforward:

1. As a professional software engineer, it’s important to have tools that help you get work done
2. For months, GitHub has got in the way of his work on open source projects via a flood of outages
3. It makes no sense to use a product unfit for professional work.
4. As GitHub shows no signs of improvement, it’s worthwhile to move to a different solution whichjustworks

### CTO blames AI agent-fuelled load spike

GitHub CTO, Vlad Fedorov,shared an updateon why reliability has been terrible for months at GitHub. He identified the load from agents being much bigger than expected as the culprit. Charts illustrating this were shared by GitHub:

This chart looks eye-catching – but there’s just one tiny issue: no Y axis! So, while it tells the story of the load going up slowly and then very fast, we’re not told by how much. However, I managed to get data from GitHub, and below is the chart showing the actual load increase over two years:

A load increase of ~3.5x, spread across two years, doesn’t seem so brutal at first glance.It is nothing like a load increase of 10x in a month, and a good chunk of it occurred in recent months. So, why can’t GitHub handle it? In a blog post, Fedorov said:

“A pull request can touch Git storage, mergeability checks, branch protection, GitHub Actions, search, notifications, permissions, webhooks, APIs, background jobs, caches, and databases. At large scale, small inefficiencies compound: queues deepen, cache misses become database load, indexes fall behind, retries amplify traffic, and one slow dependency can affect several product experiences.”

Here’s how the per-second load numbers from January 2023 and today compare:

GitHub took 15 years to achieve the 2023 numbers, and maybe it expected to continue growing in a comparable way in the future. If so, some engineering decisions about long-term infrastructure improvements would have been made obsolete by the arrival of AI agents.

To add to GitHub’s challenges, the company is in the midst of a migration from its own data centers → Azure.In October last year, GitHubstarted tomove over to Azure – a project expected to take 12 months – because it already had constraints on its own data center capacity.

Such large-scale infrastructure migrations are hard enough when the load on a service is relatively stable; just making sure nothing breaks takes a lot of effort. But moving at a time when load is spiking means that bugs can cause more visible outages. Of course, GitHub can secure a lot more compute capacity on Azure, now they know what to expect.

But other major companies prepared for a 10x increase in infra load, so why not Microsoft / GitHub?A year ago, I did research on how Big Tech was preparing to respond to the impact of AI on their business. Google was improving its internal systems to accommodate for a 10x increase in load. As we covered in The Pragmatic Engineer,in July last year:

“Google is preparing for 10x more code to be shipped. A former Google Site Reliability Engineer (SRE) told me:
“What I’m hearing from SRE friends is that they are preparing for 10x the lines of code making their way into production.”
If any company has data on the likely impact of AI tools, it’s Google. 10x as much code generated will likely also mean 10x more: code review, deployments, feature flags, source control footprint and, perhaps, even bugs and outages, if not handled with care.”

Predicted enormous load increases were not secret knowledge within the industry, yet it seems GitHub was blissfully ignorant of their potential size. According to Vlad, GitHub dideventuallyplan for a need to increase capacity by 10x, but this was in October 2025, months later. In February 2026, the company is now adjusting that expectation to 30x.He wrote:

“We started executing our plan to increase GitHub’s capacity by 10X in October 2025 with a goal of substantially improving reliability and failover. By February 2026, it was clear that we needed to design for a future that requires 30X today’s scale.”

There’s also the question of whether GitHub miscalculated how much time it had to prepare for explosive load growth, and whether it was caught off guard when that growth materialized months sooner than expected at the start of this year.

Given GitHub only started to prepare for a major load increase in October, its current problems are unsurprising.At the scale of GitHub, it’s common enough for each team owning a service to plan a year ahead on how much load their service will have, and hardware resources like storage, VMs, and networking are allocated accordingly. Load planning can account for up to half of the preparations, and when reality doesn’t conform to plans, some systems can struggle to scale up.

So, on one hand, dealing with a 3.5x increase in load over 2 years should not be such a big deal for most services; especially not ones which can be horizontally scaled (when there’s not much state, and scaling is achieved simply by adding new nodes.) But GitHub probably stores a lot more state with pull requests, workflows, projects, etc. This probably makes scaling more tricky when it comes to databases and systems running workflows.

GitHub also has 18 years of tech debt on its hands, and thousands of staff to align as “organizational overhead.”As its service load grows faster than before, responding is harder due to all that accumulated “debt”:

* Tech debt: many systems at the company are 10+ years old and are likely patched up, making them more difficult and risky to change
* Organizational debt: around 4,000 people work at GitHub, of whom 1,000 are engineers. Teams have dependencies with each other, and even seemingly simple work can require dozens of engineers to work together
* Customer expectations: GitHub cannot break customer workflows, even if doing so would mean changes to systems happen faster

GitHub finds itself in the ‘innovator’s dilemma’: the company became successful because it built developer workflows that made sense, pre-AI, and it used to be able to accurately forecast service load changes. But now that engineering teams’ workflows include AI agents, GitHub’s own workflows are not necessarily the best fit, and the company failed to forecast service-level changes.

### Other vendors floored by AI load? Not really

One thing that doesn’t add up about the situation is that other vendors who are presumably experiencing similar load spikes don’t appear to be suffering with reliability issues as much. Vercel, Linear, Resend, Railway, Sentry, and other infra providers see record-level growth thanks to AI, but keep up with the load.

Yes, it’s true that AI vendors like Anthropic, OpenAI, and Cursor have some reliability issues, but it’s not at the scale of GitHub’s. GitHub’s direct competitors, GitLab and Bitbucket, presumably see load going up similarly, but they’re not going down as much.

An obvious question is how much of GitHub’s pain is self-inflicted?With Microsoft as owner, it has more resources at its disposal than any competitor or startup, and yet failed to predict load increases and is too big to respond with the nimbleness of a startup.

It’s undeniable that solving for a major load increase is a hard challenge; it’s when the difference between average and standout engineering teams is apparent. GitHub hasn’t been responding like a world-class engineering org.

### GitHub alternatives?

Every regular user of GitHub feels the pain of ongoing outages. As a dev, you can either hope Microsoft willeventuallyimprove reliability, or seek alternatives. As covered above, Mitchell has chosen to quit and is currently deciding where to take Ghostty.

The obvious alternatives are GitHub’s biggest competitors, GitLab, and Bitbucket. Each offers Git hosting, and neither comes with the uptime woes that GitHub is suffering from.

Self-hostedsolutions are also an option, like self-hosting your git repo, or going with aself-hosted forgelikeForgejo, which is an open source, local-first GitHub alternative.

I also suspect that, soon enough, we’ll see startups offering GitHub-like code hosting capabilities, while offering more robust uptime and being architected to handle the 30x-or-more scale which GitHub hopes one day to support.

Read the full issue oflast week’s The Pulse, or check outthis week’s The Pulse. This week’s issue covers:

1. Did Anthropic turn hostile on devs because capacity was running low?
2. Amazon finally allows Claude Code and Codex usage
3. Meta forcefully assigns engineers to data labelling ahead of job cuts
4. New trend: small “AI-forward” teams
5. Industry Pulse: why Meta tracks employees’ computer activity, OpenAI starts to move off Datadog, Apple lets slip it uses Claude Code, GitHub → Xbox transfers at Microsoft, VS Code inserted “coathored by Copilot” even when Copilot did nothing, analysis of the Coinbase layoffs

Subscribe to my weekly newsletterto get articles like this in your inbox. It's a pretty good read - and the#1 software engineering newsletteron Substack.
---
title: 'The Pulse: Anthropic builds its own source control system - The Pragmatic Engineer'
url: https://blog.pragmaticengineer.com/the-pulse-anthropic-builds-its-own-source-control-system
site_name: tldr
content_file: tldr-the-pulse-anthropic-builds-its-own-source-control
fetched_at: '2026-10-22T16:04:37.953323'
original_url: https://blog.pragmaticengineer.com/the-pulse-anthropic-builds-its-own-source-control-system
date: '2026-10-22'
published_date: '2026-10-22T14:52:25.000Z'
description: Git had too many performance problems at 30,000 PRs per day, so Anthropic built its own. I talked with the team, including asking why they didn’t open source its new system, ‘Scion.’
tags:
- tldr
---

Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover Big Tech and startups through the lens of senior engineers and engineering leaders. Today, we cover one out of four topics fromlast week’s issue of The Pulse. Full subscribers received the article below seven days ago. If you’ve been forwarded this email, you cansubscribe here.

Interesting information from Anthropic about why the company moved off Git and built its own custom source control system. From theirengineering blog(emphasis mine):

“At Anthropic, coding is no longer the bottleneck to building systems or doing research. Claude is able to autonomously iterate on research loops, micro-optimize complex programs, and build new services from the ground up at a speed and scale we haven’t seen before. 
The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI.
In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we merged over 30,000 per day. We don’t expect this rate of growth to slow down anytime soon; the latent demand for merging code is practically infinite, and every bottleneck we remove immediately leads to a further increase in the amount of code we produce.”
Anthropic saw PRs merged per day snowball 10x in less than 4 months’ time. Source: 
Anthropic

That’s a 12x increase in PRs in a four-month period! Interestingly, just a year ago, I shared how I had gathered Google was preparing for a similar tenfold increase across its broader infrastructure. From thedeepdive published in July 2025:

“Google is preparing for 10x more code to be shipped. A former Google Site Reliability Engineer (SRE) told me: ‘What I’m hearing from SRE friends is that they are preparing for 10x the lines of code making their way into production.’
If any company has data on the likely impact of AI tools, it’s Google. 10x as much code generated will likely also mean 10x more code reviews, deployments, feature flags and source control footprint.”

Back to Anthropic, a few things about the company are different from many other tech businesses:

* Use of a monorepo.Like most large tech companies, Anthropic has a massive monorepo, where the working copy itself is 25GB in size.
* 25 million git checkouts per day, just for CI!All ~3,000 staff extensively use parallel Claude agents – typically 10-15 per engineer – so a lot of pull requests are created; somewhere in the region of 30,000 per day. All these PRs trigger a massive number of checkouts, mostly from the CI system.
* Nearly all clients are always online.Git was built on the assumption that clients go offline at various times, and that when they come back up, they need to catch up with branches and merge their changes into the repo. However, when clients are always connected to the corporate internet – like at Anthropic – this assumption no longer holds. Design decisions to accommodate offline clients mean inefficient checkouts and more data transferred than necessary.
* Hard to horizontally scale git.Scaling git is done by running git mirrors: replicating git repositories across several mirror nodes. A primary git server accepts the writes, pushes out to all mirrors, and clients fetch from various mirrors. Anthropic ran hundreds of git mirrors, but found that once their repo outgrew the mirrors’ disk capacity, they could no longer scale the repo.

So, Anthropic created a new source control system,which is called‘Scion’ internally. It’s closed source, and Anthropic hasshared the high-level design principlesand data structures used, but no code details. The problem with having your own source control system (and moving off Git and GitHub) is that GitHub’s code review system is lost! So, Anthropic also had to build a new code review and code management system, which they call ‘Antique.’

I reached out to the team building Scion and Antique to learn more about how Scion works. Here’s what they told me:

### Technical details

The design of Scion is pretty simple: stand up “server” nodes (that contain the whole repository), store changesets inside of Google Spanner (Google’s distributed, highly available database) and blobs (large files) in the highly durable Google Cloud Storage:

Scion’s architecture, at a high level

I asked Nick G – one of the authors of the original blog posts – about additional details and here’s what he told me:

* Rust: the language that Scion’s server and client are written in.
* Go + React:Antique, Anthropic’s new code review and code management platform has its backend in Go and frontend written in React. It works nicely with Scion.
* More resilient replication strategy: by default, Google Spanner offers multi-zone replication with three replicas. Anthropic has increased the number of replicas (they didn’t tell me the exact number, but an educated guess could be five or more replicas), and switched to multi-region replication.All these changes make sense, given how critical code is and that it’s sensible to reduce the likelihood of losing any data – even at the cost of higher write latencies.
* Backups: on top of replication, Anthropic keeps full backups of the database and soft deletes on the blob storage where file contents live. Spanner’s point-in-time recovery also lets Anthropic restore from a bad write.Smart!

Scaling is an interesting topic. I asked Nick if the system autoscales or scales manually. He told me:

“Every component can autoscale, but so far it hasn’t needed to, even as our merge volume grew more than 10x this year. The data is content-addressed and never changes once it’s stored, so the caching tiers do most of the work.”

A team of seven engineers builds and maintains all of this:

* Four worked on the core Scion server and client
* Three were split between building code search, merge queues, etc.

100% of Anthropic’s monorepo has moved off Git.This was no small feat to pull off! Nick gave me more details about the migration:

“The migration was not simple, but Claude was instrumental in getting it done. It’s also ‘self-healing’ in a way: if we get all the important use cases migrated and have something like 99% coverage, we can just force the cutover and Claude can help us fix anything that actually mattered.
100% of our monorepo is off of git. A few smaller repos that were never in the monorepo are migrating now, and they’re much simpler.
All of our community resources continue to live 
on GitHub
: skills, plugins, Claude Code’s public repo, etc. And last week we launched 
OSS Scanner
, which gives open-source projects free security audits using our strongest models (inspired by Google’s OSS-Fuzz).”

### Big Tech moved off Git long ago

My take is that Anthropic has “Big Tech problems” much earlier than most of Big Tech had to tackle them. Anthropic employs around 3,500 staff, but their coding output – thanks to each person using around 10 agents all the time – is closer to that of a tech company with 35,000-70,000 staff! That’s a Meta or Google-sized company by the number of engineers.

Google and Meta have long since moved off Git because it did not scale for them.

Google built its own version control that took inspiration from Perforce.Git itself was created by Linus Torvalds in 2005, seven years after Google was founded. So git was not an option for Google to use in the early years: the company chosePerforceinstead. It was around 2011-2012 that Google had ran into scaling issues with Perforce and built its own source control system called ‘Piper.’ It’s also a centralized version control model and still works well enough for the search giant. It’s no surprise to know that Piper was inspired by Perforce, and Google built Piper to be more performant for their use cases than Perforce was.We covered more on Google’s internal stack in the deepdiveInside Google’s Engineering Culture.

Meta found that git and other systems could not scale as needed, and so built ‘Sapling.’Meta initially moved over to Mercurial, and then custom-built and open sourcedSaplingfor itself. As the company shared at the time:

“Sapling began 10 years ago [around 2012] as an effort to make Meta’s monorepo scale in the face of ever-increasing engineering growth. Publicly available source control systems were not, and still are not, capable of handling repositories of this size. Instead of moving away from the monorepo and sacrificing engineering velocity, we decided to build the source control system we needed.
Along the way we realized there were also large opportunities to increase developer velocity by improving the source control experience. By investing in new UX, we’ve made it possible for even new engineers to understand their repository and do things that were previously only possible for power users.”

Sapling itself is more of a client-server architecture. From thedocumentation:

“Sapling started from Mercurial as a distributed source control system, it then transitioned to a client-server architecture to solve the challenges. The server can utilize distributed storage and pre-build various kinds of indexes to provide more efficient operations.
While Sapling is less “distributed”, we tried to make the difference transparent to the user. For example, our lazy commit graph implementation does not require extra commands to “deepen” the graph. The user sees the full history.
That said, we do drop support of pulling from a lazy repo. Commit cloud covers these use-cases.”

### Did Anthropic secretly rip off Sapling’s and Mononoke server

I asked Anthropic why it doesn’t open source Scion. Nick G’s reply:

“Mostly bandwidth! Even a no-support code drop takes a lot of work to do well. We have a small team building and running Scion. While the principles we used to build it are durable, the underlying code changes very frequently. For example, we’re still removing git-compatibility layers we only needed for the migration. We’d rather put that time into sharing what we learned, and 
as the post says
, into working with GitHub, GitLab and the OSS community on scaling git.
To emphasize that point: most teams don’t need to leave git! But we think there are things git could benefit from, mainly change sets, derived data, and the checkout protocol. Our goal was to inspire conversation and collaboration around those ideas.”

The explanation, on one end, makes sense. On the other, Meta themselves also emphasized how most teams don’t need to leave git, and stillopen sourced Saplingfor anyone to use, or take inspiration from.

One key component of Sapling isMonoke: the also open source server meant to scale up accepting thousands of commits every hour, across millions of files, written in Rust.

Could have Anthropic avoided open sourcing Scion, because it might have shown how much they copied from existing open source projects?The creator of Monokewrote a postaccusing of the Anthropic team of ripping off Monoke — and theBonsai data model— writing:

“This [Scion] was a ripoff. My post yesterday was trying to be as charitable as possible given what I knew, and in particular that the similarity to Mononoke was mostly unintentional and the lack of credit was the result of not doing due diligence. However, after publishing the post I privately received confirmation that Scion intentionally and blatantly ripped off Mononoke, and in particular that there was overlap in personnel. There is no chance that this was an unintentional homage. This is something I had a hunch about but was not comfortable saying yesterday, given what I knew back then.
The resemblance is much deeper than just the notion of derived data. Some people pointed out that derived data is just an index, which is a well-known concept. I want to clarify that derived data was merely the most striking resemblance. It goes much deeper than that, and extends to the entire data model, as well as a number of the structures built around it.”

Anthropic did not give credit to Monoke in their original post, and only addeda small attributionafter the complaint.

To be clear, the point of open source is that you can do what you want with the software without much limitations (save for what the license contains): but it’s poor form that it took a public complaint for Anthropic to admit that the clever data structure they presented in their blog post heavily derived for an existing and open source data strucutre.

### Will central VCs stay a niche, or expland beyond Big Tech?

Big Tech has preferred centralized version control systems (VCS), and I wonder how niche of a trend central VCSs will remain. As we’ve seen since well before AI, some of the largest tech companies dropped git because they did not like the performance degradation from offline support they no longer need.

My question is that even with agents, how many companies will see git “break” similarly to how it has at Anthropic? When this happens, how many will find git’s mirroring functionality inadequate for their own needs?

There’s a new batch of vendors positioning themselves as git-compatible version control solutions built for AI scale:Entire, founded by GitHub’s last CEO, Thomas Dohmke (a current podcast season sponsor),Cursor Originby SpaceX, andCode Storageby The Pierre Company. At the same time, GitHub itself seems to be investing a lot more in making its platform more reliable and scalable.

My hunch is that very few companies will go through the trouble of building yet another source control system. In this way, Anthropic reminds me a bit of Google, which has been known to build custom internal systems which are not publicly available, to address the company’s internal needs. This can be disorienting for Google engineers after they leave the company and find they’ve become out of touch with industry-standard tools.

Read the full issue ofThe Pulse this is from,or check outthis week’s The Pulse. This week’s issue covers:

1. Do we need to rethink software security because of AI?Half a dozen of high-profile security incidents and breaches on a single day: and many of them are connected to AI (or sped up because of it). Attackers are gaining unfair advantages with AI, and defenders will have to react.
2. Is Anthropic’s new version control system “a rip off”?The creator of Mononoke (an open source, high throughput version control server) accused Anthropic for ripping off their design, and not giving credit, presenting their work like it was novel. Not a good look on the AI lab.
3. Industry Pulse. Saudi Arabia made a “problematic” offer to pay alleged OpenAI spy’s bail, Shopify builds tooling for self-healing software, Foursquare’s sale disappoints, Claude Code gets a major speed boost with gzip, and more.
4. Predictions on the future of software development.Somebold predictionsfrom software engineer and Amp cofounder Thorsten Ball, like how open source doesn’t make sense in its current form anymore.

Subscribe to my weekly newsletterto get articles like this in your inbox. It's a pretty good read - and the#1 software engineering newsletteron Substack.
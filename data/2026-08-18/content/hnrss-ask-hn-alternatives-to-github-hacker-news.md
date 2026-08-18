---
title: 'Ask HN: Alternatives to GitHub | Hacker News'
url: https://news.ycombinator.com/item?id=49331033
site_name: hnrss
content_file: hnrss-ask-hn-alternatives-to-github-hacker-news
fetched_at: '2026-08-18T12:12:06.032163'
original_url: https://news.ycombinator.com/item?id=49331033
date: '2026-08-17'
description: 'Ask HN: Alternatives to GitHub'
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
Ask HN: Alternatives to GitHub
498 points
 by 
dhruv3006
 
12 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
319 comments
Github has been down consistently over the last few months - does it make sense to switch to alternatives?
 
help

plqbfbv
 
11 hours ago
 
 | 
next
 
[–]

To all of those proposing self-hosted GitLab: we did it for 6+ years in my company, and it's not always a smooth sailing. We had our own runners and we made it auto-upgrade across docker images daily before business start. It mostly worked really well, except those few times were a Docker upgrade had to be rolled back, or that one time the bundled pg_shared_buffers was set at 1MB by default, making schema upgrades impossible for bigger instances, or a version major would break pipeline expectations forcing to upgrade 200+ repos at a time (we pinned to major afterwards). Lately I was also receiving an almost weekly "critical patch" newsletter due to critical/high vulnerabilities, which I can only imagine are due to LLM running over the code and identifying bugs.

That said, I wish we hadn't migrated to GH, our self-hosted instance hadWAYless downtime despite being perhaps a bit slower (mgmt saving money) and required a bit more toil: GH is nowhere near Enterprise-ready and it feels a downgrade across the board. GL has better access granularity, better docs, better integrations, and you can clearly see the UI received a lot of attention (although it does take 10m with a new account to pin the proper items in the maze of sub-menus that is the sidebar). You can also look at the code and help out if needed, and/or simply provide a patched version to your image via a docker mount.If you're really looking at self-hosting GitLab for a smallish team (up to 50-100 ppl), prepare at the very least a 16GB machine (best 32GB) with 4 cores and a decent SSD, and at least a small team (1-3 people) that can maintain it properly or jump at it at any moment. For runners, a small k3s cluster is ideal to make use of all the resources you can throw at it without worrying about managing the runner state/configuration.

reply

inanothertime
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Setting up custom GitLab runners can be cumbersome in the beginning! We faced that multiple times with various customer projects for which we were using GitLab.com managed repos. That's why my colleague and I recently built a "GitLab Runners as a Service" [0] -- simply use your self-managed GitLab or GitLab.com account to login, adding pipeline runners is a 1-click operation! Under the hood we provision a Hetzner machine for you runners and automatically connect your GitLab group or project to it. Happy to hear your feedback!

[0]https://rocketrunner.io/

reply

lclc
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is pretty cool and one of the few things I couldn't find a viable alternative to in-house hosting so far. The only thing your "GitLab Runners as a Service" is missing is ISO 27001 (and optionally SOC 2) certification. That makes it again easier for your customer to get / maintain their ISO 27001.

(So far I used this cloud.init script to spin up and upgrade GitLab-Runner instants:https://gitlab.com/21analytics/gitlab-runner-cloud-init/-/bl...)

reply

inanothertime
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ha, let us look into ISO 27001 certification and see what it takes to obtain it (and SOC 2). Thank you for this valuable pointer! If you could just sign in (accounts are free and you can even try us out for the first 48h and not be charged), then we could message you to your email address once we have an update here.

reply

senorrib
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You’re on for a ride. Set at least 50k on the side for that.

reply

cortesoft
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I find the gitlab runner registration process a lot simpler than the github process, and a lot more flexible when you are self hosting the gitlab instance. We used kubernetes runners for both, and gitlab was clearly better.

The worst part about the github runner setup is that there is no built in support for using your own cache if you are using github.com and want to run your own runners. In order to use your own cache store for your runner jobs, you have to patch the runner image because the cache location is hard coded. Gitlab lets you choose your cache location as a standard feature.

reply

inanothertime
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Right! That's why running your owners runners is so valuable as you've got full control over the cache location which clearly makes subsequent pipeline runs super fast.

reply

zer0x4d
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Thank you for building this, looks like it could be really helpful. We've been running our self-hosted GitLab with almost 99.99% uptime and a few runners but the configuration and update process has been a bit cumbersome. Will take a look at rocket runner.

reply

inanothertime
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

99.99% uptime is impressive! So far our runners are likewise very reliable! It's just a Hetzner machine with our stack on top after all. Thanks for trying us out and please drop us an in-app message for any questions or comments!

reply

jrey2112
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Never forget the sudden GitLab price-hike and flavor feature changes just a few years ago. I was literally about to go from free to paid, when the pricing doubled nearly overnight. I left for Gitea.

https://news.ycombinator.com/item?id=35144974

reply

cortesoft
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> That said, I wish we hadn't migrated to GH, our self-hosted instance had WAY less downtime despite being perhaps a bit slower (mgmt saving money) and required a bit more toil

The key thing that drove our decision to self host gitlab was that WE were the ones in control of when things happened. We didn't do upgrades during times where we really needed our git infra up, and we were in control of our response time to incidents. We were not at the mercy of some other company's upgrade schedule and incident resolution process.Of course, it comes with added workload and responsibility, but as the above comment says, it was not that onerous. While we paid for Gitlab Enterprise for a long time, we eventually switched to the free tier as that company was winding down (for reasons unrelated to our choice of git hosting), and the free tier actually has pretty much everything we needed.

reply

scientifik
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

ex-GitLabber here, and yes this is a pretty common scenario. GitLab as a product is pretty good, however GitLab Inc, is not great at supporting the broader community especially the SMB-Mid tier self-hosted users. (If you're big enterprise you'll get white glove support)

It's a bummer because they had so much potential to dethrone GitHub a few years ago but really missed the opportunity to position themselves as a viable alternative. That said I still use gitlab.com for my personal projects over anything owned by Microsoft.

reply

Lorin
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

As someone who used to submit issues to Gitlab just to see them stagnate for 6-8 years and then ceremonially get closed after being stuck in management/release bump hell (along with many 'me toos' from both Gitlab premium support staff / 3rd party contributors) I agree with your statement 100%.

reply

KronisLV
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I also self-hosted GitLab for some years, eventually ended up moving over to Gitea + WoodpeckerCI + Nexus (with Nexus for a while). Well there was DroneCI in the middle for a bit there as well, but Woodpecker is perfectly okay and more free in regards to what you can do. Only thing is that not that much other software out there supports Gitea, for example Kepler only knows about GitHub, GitLab, Jira, Trello and Linear.

reply

wongarsu
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'd also say that gitlab runners are the biggest failure point in gitlab and take some work to micro-manage. If I was setting up from scratch I would consider gitlab for source control, but some hosted service for CI

reply

inanothertime
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Maybe give 
https://rocketrunner.io
 a try? We made super easy and fully managed GitLab CI/CD runners for GitLab.com or self-hosted GitLab servers :-)

(Sorry for posting this twice, but we'd really love to get more user feedback)

reply

tikkabhuna
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Really? I've been very happy with how easy GitLab Runners are to manage. We were running 20,000 jobs a week on 6 bare metal boxes and we had tons of spare capacity. Simple Ansible script to deploy the runner and register it. Tags for t-shirt sizes to set the amount of CPU/memory allocated to each job container.

Maybe running on Kubernetes or some autoscaling solution is more painful.

reply

codexb
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yeah, it's mind blowing to me that GH still doesn't have a branch viewer in each repo.

reply

znpy
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

We did tun our own installation at work, supporting ~120 developers.

A single vm, 8 cpu cores and 64gb memory, using ssd disks on a local vmware cluster.It worked okay but:1. Was only exposed to the corporate network and some vpn connections2. We did the upgrades late at night once every like six months, taking a snapshot of the whole thing from vmware side before touching anythingIt worked pretty well and was relatively low maintenance. Frankly a very pleasant experience.I’m using github and bitbucket at work nowadays and frankly i miss that experience, both as an user and as an administrator.Edit: btw i left that job and that gitlab installation in 2022, no idea how things changed in the meantime.

reply

fHr
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

gitlab.com and selfhosted gitlab in various companies in the last few years

reply

formerly_proven
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> To all of those proposing self-hosted GitLab: ... it's not always a smooth sailing.

> (we pinned to major afterwards)I mean OK. But also, if I want a reliable service in my business, I wouldn't typically auto-upgrade docker images nightly to "*".

reply

plqbfbv
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> I mean OK. But also, if I want a reliable service in my business, I wouldn't typically auto-upgrade docker images nightly to "*".

Well fair, but we had been using it for 4+y at the time before running into that, and the rails-based migration scripts basically never failed once despite being migrated across 6 majors and countless minors/patches. Being a small company, from that PoV it gave us very little downtime for essentially zero security work to maintain it. Of course we had daily (and tested) backups too, just in case, but we never had to use them.Overall, the downtime of GL, even with auto-upgrading and the issues above, was perhaps 1.5 work-days across 6+ years. GH exceeded that budget in the first 2 months after migrating this year...

reply

melezhik
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Ok, with DSCI as monolith application where git and CI are the same server, 32GB RAM VM is more then enough , no need to host runners, no need in k8s cluster, no need in dedicated maintain team, so no extra costs on devops tasks ... 
Also with general programming languages for CI pipeline you are in full control and simplicity ...

reply

theamk
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This thread is about full-featured forges like github/gitlab.

That DSCI is not a forge - it's a task runner attached to gitweb frontend. There are _none_ of the forge-like features like user management, pull requests, etc... Even in CI area, most of the features are missing: from the quick perusal of the doc, even something as basic as "have runner on remote machine" or "run two jobs at once" is not implemented.

reply

melezhik
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Whoever downvoted this ^^ my comment I need your reasoning … I don’t know why people hate simplicity ) ( or love complexity )

reply

rpearl
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

it is a simpler set of services at the expense of a more complex user experience

reply

rhdunn
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

It depends on what you are after?

1. Do you want something that works and feels like GitHub? -- Forgejo and Gitea are good for this.2. Do you want a place to host git repositories with minimal hassle? -- GitLab, CodeBerg, and others are available.3. Do you have your own hosting infrastructure? You could use gitolite and CGit/GitWeb on that hosting platform or local hardware.4. Do you just want to host repositories? -- Gitolite can be used to help with SSH/auth/repository creation, and CGit or GitWeb for the frontend.5. Do you need something like GitHub Actions? -- GitLab, Forgejo, and Gitea offer CI, or use external CI infrastructure.6. Do you need issue tracking and management? -- GitLab, Forgejo, and Gitea provide these. There are alternatives from Jira to Kanban (including Trello) to Markdown (Obsidian and others) and more.

reply

mejutoco
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

> 4. Do you just want to host repositories?

an ssh connection andgit --bare initon your ssh accessible server works just fine

reply

janalsncm
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

“Just” is a four letter word and a trap our industry repeatedly falls into.

https://sgringwe.com/2019/10/10/Please-just-stop-saying-just

reply

chrysoprace
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I hadn't read this article until now, but I started catching myself using the word at work a few years ago and I've actively been trying to avoid using it for the reasons laid out in this post.

reply

hamburglar
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If all you want to do is host repositories, “just” is the appropriate word here. For lone wolf work, all I care about is having a remote that mirrors all the changes and branches I create locally. It’s just redundancy. A git bare repo and SSH are all that’s needed.

I don’t do pull requests to myself, and I don’t need a bug tracker or CI.

reply

nine_k
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

But sometimes it's applied properly! 
https://github.com/casey/just

reply

sincerely
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

edit: totally wrong

reply

ysavir
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think they mean the "just" in "Do you just want to host repositories?", implying that it's never "just" hosting repositories, and the needs will continue to grow beyond what the simple solution offers.

reply

fooqux
 
40 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> the needs will continue to grow beyond what the simple solution offers.

If they do, then migrate to a provider that offers what you need at that time. It's not like adding a new remote is hard.

reply

sincerely
 
54 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I must be illiterate. Ofc. Sorry

reply

myaccountonhn
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It can be as brief as:

ssh server git --bare init myrepo.gitgit clone server:myrepo.git

reply

eddieroger
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can even support Actions with this method if you're not afraid of a little scripting. 
https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks

reply

jolmg
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> git clone server:myrepo.git

or if your local repo existed first:git remote add server server:myrepo.git
 git push -u server @

reply

sunshine-o
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Beautiful !

reply

rhdunn
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That's what gitolite does with some helper scripts for creating/setting up the repositories, adding metadata to the configs, etc. That way your `git` user can be set to reject ssh login attempts. The projects are managed by pushing a config to a gitolite admin repository.

reply

samlinnfer
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Cool thing about gitolite is that you manage it using text files and committing to the gitolite admin git repository.

We were using it until we grew tired of not having a web view to comment and review patches so we switched to gitea.

reply

edgyquant
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It is much more complex than this to get basic GitHub functionality anyone who has tried can tell you that. It feels like it should be a simple command but it absolutely isn’t

reply

jonahx
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Quick intro for this method: 
https://www.youtube.com/watch?v=iuIdBfjL62s

reply

Bnjoroge
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hopefully a good spot to plug my own project, preloop, which is a drop-in replacement of Github actions(both the runners and control plane) that runs locally or self-hosted in isoalted microvms, and supports debug-on-failure. You can also push to the server, run CI and then optionally create a draft PR. Not quite production-ready yet(for the self-hosted part), but the local part works well. We implement the official runner protocol 100% unlike act/gitea/forgejo, so your workflows are more likely to work out of the box with preloop(forgejo has the closest compatibility with Github Actions though so it's a good off-Github option) and we use microvms so no DinD issues. I'm working on getting the official runner vm image up to reduce any environment incompatibilities. Feel free to try it out: 
https://github.com/preloopdev/preloop

reply

srcreigh
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah. MicroVMs make hosting runners pretty straightforward. I had codex make a forgejo runner controller which pulls forgejo actions and creates kubernetes jobs for them.

It was a bit of a pain to configure firecracker with k3s.It really can’t be understated how much easier hosting CI is with microvms as the security boundary.

reply

Bnjoroge
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Agree. I'm always surprised Github still uses huge fat VMs. I imagine this is one of the things that make it much painful at scale. The tricky part with microvms are getting them to run cross-platform. We use an awesome project called smolvm that builds on libkrun and makes this alot easier. As an aside, how have forgejo actions worked for you in practice?

reply

elehack
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you want (4) and don't care about a web interface for managing repos, but do want Git-LFS, Soft Serve (
https://github.com/charmbracelet/soft-serve/
) works pretty well. I used it for self-hosted stuff until I started needing other features Forgejo offers.

reply

delf
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Or just push to an S3 bucket with `gitsocial mirror <s3>`

reply

jolaflow
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

For issue tracking you may also be interested in Epiq. It is git-native, vendor agnostic, and distributed. Comes with a command line TUI, a browser GUI, mcp, and more. Also event sourced state with replay, which is super powerful for auditing workflows.

reply

ljm
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm quite partial to SourceHut as well but tbh I don't care about contributors and I like it because it is deliberately low-tech.

Maybe the CI could be a bit better (secrets management will sting you if you don't read the docs first), but that is also pretty no-nonsense and gets the job done.If you like no-frills and an expectation that you know what you're doing, it's pretty sweet.Would probably scare off most collaborators though but that, IMO, is part of the appeal. If you want to contribute then it's more likely you're invested and not driving by.Also I like that it has a concept of projects so you can group repos together (which on GH would normally require creating an organisation account). And a repo can be public but unlisted, so it's open but not drawing attention.

reply

yw3410
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sourcehut is fantastic because you can also SSH into the CI machine.

reply

0xc133
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

*Forgejo

reply

dumidusw
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's great for lightweight self hosting

reply

rhdunn
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Indeed. I've edited my post to fix the typo.

reply

tonymet
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

and you can stream your commits into any of these to improve deployment and commit availability when github is down.

reply

osxman
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Forgejo == Codeberg

reply

rsyring
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not exactly:

> Forgejo is self-hostable free software for software development, built on top of Git. Codeberg is powered by Forgejo, which is in turn a hard-fork of Gitea. Compared to Codeberg, Forgejo is not one service, but free software to help you build your own. Everyone can install their own Forgejo instance to host their own projects. There are also public Forgejo instances as well as Codeberg you can use, but make sure you find a site that is actively maintained and updated, and that you trust the provider.https://docs.codeberg.org/getting-started/what-is-codeberg/#...

reply

tonymet
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

isn't forgejo the software and codeberg is hosted forgejo?

reply

Cupprum
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Codebergs has a section about that: 
https://docs.codeberg.org/getting-started/what-is-codeberg/#...

reply

tonymet
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

TLDR

reply

zahrc
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Literally the first paragraph:

> Forgejo is self-hostable free software for software development, built on top of Git. Codeberg is powered by Forgejo, which is in turn a hard-fork of Gitea. Compared to Codeberg, Forgejo is not one service, but free software to help you build your own. Everyone can install their own Forgejo instance to host their own projects. There are also public Forgejo instances as well as Codeberg you can use, but make sure you find a site that is actively maintained and updated, and that you trust the provider.

reply

tonymet
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

So…what I said.

reply

dspillett
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If that is too long, you have an attention span problem. That is your issue to deal with, not ours.

Or from another angle, how would you say it more concisely? Preferably without using AI to summarise.

reply

kristofferR
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If anything it seems like you are the one with an attention span problem when you can't remember that he posted the correct consise definition earlier in this thread. Being a dick when justified is counter-productive, but being a dick while also being the one who is confused is a way worse look.

reply

als0
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

7. Do you want the most contributions?

I hate to admit it, but GitHub has a massive community. I’ve personally seen a project leave it and then contributions dropped significantly.

reply

shimman
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Having people personally go out of the way for a little bit of friction tells you how valuable, and perhaps, serious these people are. I'd rather have that group of people contributing to my projects than fly by night agents that just shit all over the floor and expect treats for doing so.

reply

ygjb
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Contributions aren't just commits/prs. It's also opening issues. The harder it is to provide feedback, the more likely users are going to seek a different library or tool, and depending on the actual objective of releasing or publishing code, that is not ideal.

I do agree on the fly by night agents, especially since so much is actually just agents acting on behalf of folks who just spam whatever permissions are requested in Claude/Codex.

reply

shimman
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Don't think open submission feedback is worth much anymore, at least not the amount of effort it requires to curate it. Having friction still seems like a great way to get decent feedback nowadays rather than needing to manually curate 100s of issues where 98% of them are spam/garbage.

reply

rhdunn
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's fine if the projects are in a single place (e.g. GitHub) as you only need to create one account.

If every project requires its own username/password just to report a bug, I may do that for the first 2 or 3, but not for every project. I'm also unlikely to create accounts on hosting platforms I don't intend on using outside of reporting the single bug.

reply

shimman
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's fine, maybe they don't want casual users like you to be part of their community. There is a reason to prefer group coherence over availability. Availability doesn't actually help the group for most online communities, it's actively a hinderance.

reply

lawn
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's also a useful signal in the age of LLMs. A bit of hoops to jump through before a PR can now be seen as a good thing.

reply

colesantiago
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You don't really need GitHub's 'community'

It is mostly all AI agents, bots and spam anyway, not to mention most projects are now vibecoded slop on there.You're better off going to a different forge or hosting one yourself.Codeberg has a no LLMs policy which is very attractive for many.

reply

godwinson__4-8
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

CodeBerg comes with the advantage that Euro social democrat style moral superiority comes for free. Never mind it has worse performance under less load and its bet for dealing with the future is treating anything LLM related as hostile.

https://blog.codeberg.org/protecting-our-floss-commons-from-...You may agree with this. And if so, you have found your home. For those who just want to host, and not buy into this particular perspective, you should probably look elsewhere. I find a lot of people in the States promoting CodeBerg also have illusions about Europe, of the sort that are likely to be radically tested in the next decade, if not the next few election cycles alone.

reply

icy
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://tangled.org
! Founder/CEO here. We're a new forge building things from the ground up, and are fully federated -- you can host your git repos on your own infra, along with the CI runners. We've also got a pretty neat set of features (if I may say so myself): stacked PRs, Nix-based CI (if you want it), and a fully open protocol (
https://atproto.com
) to for you and your agents.

Happy to answer any questions.

reply

theamk
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

The whole "social coding" angle is highly off-putting. List of "X followed Y" on the front page, and the large "social coding" reminds of facebook, social manipulation, developer burnout and all the negative things about social networks. It also brings up the questions about project's long-term direction - is this going to focus on the code part or the social part?

Which is a pity - as I think most projects just need a git host + web UI + easy pull requests + a way to clone other's repos, and tangled seems to do this pretty well.

reply

Bjorkbat
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Arguably the "social coding" angle is the reason why Tangled is the only actual alternative to GitHub. Otherwise there's actually plenty of other alternatives to GitHub, but none of them have GitHub's punchcard, which I'm ashamed to admit is the primary draw for me.

reply

icy
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The neat thing about Tangled is you can build your own frontend pretty quickly. We've got an open API 
https://api.tangled.org
 (or self-host your own API server: 
https://docs.tangled.org/bobbin#bobbin
)

reply

satvikpendem
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You're not the target market, there are a number of other forges as seen in this thread as alternatives.

reply

whycombinetor
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What's the monetization pathway here? No private repositories (because everything is on ATProto) so near zero commercial use potential - CI is free, everything is free, no pricing page... Am I the product if I use this service?

reply

Topfi
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Just signed up, so not much to report yet, but one thing I noticed is that, because the sign in is on tngl.sh rather than a subdomain of tangled.org, it might be confusing for some users, especially as the sign in page has a very different design, theme and layout to the rest of your website and tangled as a whole. Additionally, my password manager didn't show the just created password due to the URL mismatch. Perhaps this could be addressed to improve the experience.

Edit: I really like that one-click "watch logs via SSH" copy button. Maybe those could be attached to the top of the top, as it stands the pipeline just pushes them further and further down. Find the UI and UX overall very pleasant.

reply

MerrimanInd
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I recently got a spindle and a knot set up on my home server (along with Tranquil PDS). A few rough edges that we got ironed out but it's cool to have all of that self-hosted on my own machine yet still part of the AT proto world! I'll be honest, I'm not putting anything critical on it yet but that's my lack of trust in my own home server setup not doubt in Tangled's infra!

A better web UI for the queued jobs on my spindle would be great btw!

reply

jkl5xx
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Tangled feels like the future but it seriously needs private repos ASAP to capture the momentum of the current GitHub exodus.

reply

rebolek
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I wanted to use tangled but my repo is SHA256 and you sadly don’t support it. I know SHA256 is not very usual but anyway, do you plan to support it?

reply

eximius
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I think the main thing I'm waiting for in the atproto space, for _most_ applications, is private data solutions. And the recent RFC on private data spaces (I forget the terminology) is a start, but has a ways to go.

reply

ch71r22
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah I would like to try Tangled if I can set it up in a completely private configuration

reply

paulhebert
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This looks pretty cool. I like the idea of a federated option

What’s the monetization plan? My biggest concern would be using this and it losing support in a few years

reply

AndrewHampton
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I love jj and am a fan of the ideas of AT protocol, so tangled has been on my radar for a while. Last I checked though, it sounded like it was much better suited for open source code, not private repositories. Is that still the case?

reply

opem
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Are you guys working on jj support?

reply

icy
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We already support JJ for stacked PRs, but more native integration is planned.

https://blog.tangled.org/stacking

reply

dark-star
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Is there a way to just browse hosted projects without creating an account? I couldn't find anything

reply

silverlinex
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[2 more]

[flagged]
icy
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's not crypto anything.

reply

polycaster
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://forgejo.org/

reply

sandcat_
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

I recently set this up on my homelab, not really expecting to switch to it, more out of interest. But wow, after I saw how unbelievably fast it was, I’ve moved everything over. I’ve now set it up to mirror things automatically to Github if I want to make them public.

Using Github at work is painful in comparison. (Also literally just this morning we’ve had to delay a release due to Github being down.)

reply

bobkb
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Is their CI and CD workflow robust like gitlab/github ?

reply

cobertos
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's based on act[0] so it's quite like GitHub actions but not completely [1].

I found in the current version of Forgejo the most secure way to set it up was just to put the runner on a different host. There's a Docker in Docker setup [2] that was challenging to get working correctly but still didn't quite feel secure...After setting it all up, I'm convinced GitHub actions as a concept is flawed. I wish the community would make a simpler git-defined CI/CD that didn't have the crazy surface area that actions does... Named shell scripts that can call out to other stuff in the runner Docker image and report it to the UI would be a nice start.[0]:https://github.com/nektos/act[1]:https://forgejo.org/docs/v15.0/user/actions/github-actions/#...[2]:https://forgejo.org/docs/v15.0/admin/actions/docker-access/#...

reply

dboreham
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Agreed. GitHub Actions feels like someone's science project created while on a mushroom trip. Really you just want a thing that executes a shell script in a runner.

reply

sarah-robiin
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Works well and is pretty straightforward.

Just set up a CI pipeline for PHP projects with a forgejo runner last week. Tried many approaches, ended up with a simple debian VM. Runner works well with docker images inside the VM, quite a flexible setup.
Found this easier and better than my last tries a few years ago with gitlab, which always felt quite bloated.I also published a blog post today about this whole journey:https://sarah-robin.com/blog/we-just-wanted-to-deploy-a-webs...

reply

Arrowmaster
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You can use any CI/CD you want. The only reason GH is popular is that it's free for public repos.

But Forgejo does have a GH like CI/CD. If you really care about good CI/CD then you should try some of the alternatives out and decide what works best for your needs.

reply

Valodim
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What can you recommend?

reply

Arrowmaster
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't have any specific recommendations other than do as little in your CI/CD as possible, instead do as much as possible in your build system or scripts that get called by CI/CD. This way you can migrate with less work or run locally when you want.

reply

Bnjoroge
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Hopefully a good spot to plug my own project, preloop, which is a drop-in replacement of Github actions(both the runners and control plane) that runs locally or self-hosted in isoalted microvms, and supports debug-on-failure. You can also push to the server, run CI and then optionally create a draft PR. Not quite production-ready yet(for the self-hosted part), but the local part works well. We implement the official runner protocol 100% unlike act/gitea/forgejo, so your workflows are more likely to work out of the box with preloop(forgejo has the closest compatibility with Github Actions though so it's a good off-Github option) and we use microvms so no DinD issues. I'm working on getting the official runner vm image up to reduce any environment incompatibilities. Feel free to try it out: 
https://github.com/preloopdev/preloop

reply

KronisLV
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This one is really pleasant: 
https://woodpecker-ci.org/

reply

shimman
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Isn't forgejo CI based on woodpecker?

reply

watermelon0
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Forgejo CI is based on act, which allows running GitHub Actions locally.

However, Codeberg offers hosted Woodpecker CI.

reply

dreamcompiler
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> The only reason GH is popular is that it's free for public repos.

It's also free for private repos, and I have both. Codeberg doesn't like private repos, so unfortunately I cannot just move everything to Codeberg. I'll probably set up a Forgejo VPS somewhere.

reply

fatterypt
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

For a forgejo host, check codefloe.com if what you need is a place to host personal projects or smaller teams. It’s been rock solid and it is now the default choice for anything outside of work I’ll do.

reply

esafak
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

More than that, it is integrated with Github.

reply

vinnymac
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If you know GitHub actions then you’ll immediately understand Forgejo actions. It was designed that way intentionally. There are some differences, but at least for me not enough to warrant any pitchforks.

If you have advanced use cases you might be more frustrated, but I’m not aware of any off the top of my head. I think my biggest complaint is that they haven’t exposed action logs over the API, so I can’t build tooling around them at the CLI level, feed them to an LLM, or more quickly diagnose problems that arise without using the website.

reply

mfenniak
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A basic API to access Actions logs was added in Forgejo v16. `/api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}/logs`

reply

vinnymac
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks to you I’ve now upgraded to v16, and can confirm the logs API works beautifully!

reply

vinnymac
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Nice! I was hoping they would add this in v16. Unfortunately I am still on v15 of all my instances of Forgejo

reply

td-andrew
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Hooks directly into drone.io using SSO.

Self host both of them on my internal network. Technically old version of gitea which is forgejo pre-fork

reply

bogwog
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Extremely yes

reply

lejeanvaljean
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

"Forget Joe", not the best name for a git repo host

reply

melenchon
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think it's funny. I upvoted.

reply

lejeanvaljean
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Again, I'm downvoted. This social network is totally insane. No answer, just downvotes. No humor whatsoever. Sorry. I won't comment anymore.

reply

shofetim
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

If you are frustrated with Github being down again, and just want an alternative, the other options listed are better fits. If you have the time to look at doing more than that, then check out fossil 
https://fossil-scm.org/home/doc/trunk/www/index.wiki

- It isn't git
- Works best with smaller teams
- You need to be ok self hosting (single binary, easy to do)The first point is really the killer. It is revision control, it is as good as git (maybe better), but it is different. Git = branches are easy, was built to support Linux's lieutenant development model, and a massive, loosely connected team. Fossil = branches are intentionally hard, built to support a small, tight knit team (SQLite).Most teams I've been on are closer in size to SQLite than they are to Linux, but everyone already knows git at a gut deep level. YMMV.

reply

jm4
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Fossil looks really cool. I like how it's all in one and includes the web interface. The only thing is it doesn't seem like anyone actually uses it outside of sqlite. I don't necessarily need to use the most popular thing out there, but some social proof is nice.

reply

shofetim
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is a small community. The forums are moderately active though: 
https://fossil-scm.org/forum/forum

reply

stefanos82
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

There's also a hosting service for fossil repos which does a really good job for a number of years now 
https://chiselapp.com/repositories/

reply

mariocesar
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I answered this in another thread, if you're already running a large GitHub organization, GitLab is the closest alternative in terms of features

A big plus is that it also has an open-source Community Edition that you can self-host

reply

axegon_
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I migrated everything to codeberg several months ago (and created an annual donation schedule). I was never a big fan of github but what ultimately pushed me to ditch it was the way github was shoving copilot/chatgpt in my face without me ever asking. Codeberg has a clear stance on that and it's a stance I can totally get behind.

In addition I spun up forgejo at a server at home for very critical stuff and it's awesome.

reply

babelfish
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Note: If you use any form of AI-assisted coding tools, your project breaks Codeberg TOS

reply

tcfhgj
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> If you use any form of AI-assisted coding tools,

that's not true, only if the project consists mostly of AI generated code

reply

seanclayton
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Which is exactly why I started donating!

reply

VCFundedGenYer
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Perhaps you should stop relying on AI then...

reply

zufallsheld
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There's a difference between relying on Ai and having any llm generated content in your repos.

reply

babelfish
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

?

reply

Anon1096
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Note: if your reason for switching is purely uptime, you will be sorely disappointed with codeberg

Their own site reports the 2 week uptime at 1 ninehttps://status.codeberg.org/status/codebergand I suspect if you use the (really terrible) across-all-product-offerings uptime methodology that people love to post for github it would be a 0 nines overall service.

reply

VCFundedGenYer
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The link you provided has shown a nearly perfect uptime. Your statement doesn't reflect the proof.

Personally I have never had a single issue with Codeberg's uptime. Are you trying to argue that GitHub's is better for some reason (when it objectively is not)?

reply

babelfish
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The link provided shows "Uptime (336 hours): 98.76%". That's one nine of uptime for fourteen days.

reply

axegon_
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The reason for switching was shoving all the slop down my throat, even when just browsing. There are a couple of things I have published and a handful of others I plan on open sourcing some day so for the purpose, codeberg does a brilliant job. For work - meh i'm in a corporate environment running internal repositories on company servers so that's less of an issue still.

reply

bogwog
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Codeberg for open source and Forgejo for private (and slop, if you're into that kind of thing) is what winners do

reply

axegon_
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm not into that kind of stuff honestly: in my case Forgejo is for stuff I don't feel comfortable with leaving the boundaries of my apartment.

reply

quaintdev
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

https://tangled.sh

reply

izolate
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

First I've heard of this, but they seem to be a young, smart and energetic team on a great trajectory. The atproto choice is interesting, fits their social-minded goal.

reply

ch71r22
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

How easy is it to set up and run this for private repos?

It looks like it has so many cool features -- stacked PRs, jujutsu support, CI in Nix VMs. But I've never tried it because it sounds like (at least by default) it's some sort of decentralized, peer-to-peer public thing

reply

quasigod
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You'll have to wait a bit for private repo support unfortunately. Once its ready setting up a knot via Nix or Docker is super easy: 
https://docs.tangled.org/knot-self-hosting-guide#knot-self-h...

reply

radicalriddler
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yeah, only open for public repositories until Atproto finishes their permissioned data spec.

reply

ryuuseijin
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Forgejo is great to self host. I have an easy to use template for setting it up on fly.io with backups here: 
https://forgejo-fly.fly.dev/forgejo-admin/forgejo-fly

reply

ukd1
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I've used gitlab and gitea; gitea is faster, and easier to manage and does everything I actually need though, is less feature complete.

reply

techknowlogick
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

I'm one of the project leads of Gitea. I'd be interested in knowing which features you are missing from Gitea compared to Gitlab? We are doing some backlog grooming right now, and input is very appreciated:)

reply

rhdunn
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Two of the big issues I had were around the user/repository forced structure. That works to some extent when you have multiple users with a small number of repositories. But for my personal projects I wanted more control over the structure and grouping.

I worked around it to some extent by having an organisation per category, but that doesn't work at scale. For example, you can't group Text-to-Speech projects around the different libraries (coqui-ai, Qwen3, parler, etc.), or language tooling installation scripts by programming language. -- Those have a group/subgroup/repository style structure.The other related feature is having organisation or group-level issues and corresponding tracking features.Gitolite doesn't impose/enforce a structure on the user. GitWeb/CGit have a free-form category (e.g. "lang/python") that the project can be assigned to. That works, but I'd like it to support multiple tags/labels for that.

reply

henryfjordan
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Not who you asked, but I was going to say Actions or CI/CD from when I tried out Gitea a few years ago (back when running a Jenkins instance was more normal) but looks like Gitea supports that kind of workflow now: 
https://about.gitea.com/products/runner/

reply

dima55
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I want org-mode markup support for the wikis and readmes. Github supports this, and gitlab sorta does. You should hook up pandoc to it, and support everything it can handle.

reply

scientifik
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I tried Gitea for a while but the support mechanism was "Beg for help on Discord and hope someone replies", this left us high and dry a few times.

reply

gritzko
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I strongly disagree with the assumption that GitHub's alternative is another centralized forge. Git itself is perfectly decentralized, as was the original Linux kernel development process. How people managed to put all their eggs in one intermittently available service is beyond me. Moving the eggs into another bucket is not a solution (like Microsoft is short of servers). The SPoF is the problem. There are plumbing, porcelain and "github" layers. The "github" part has to be decentralized as well. Then, using a particular forge will be a choice of convenience, not necessity. 
https://replicated.live/blog/crdt

reply

anon7000
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Oh, it’s really simple why this happened:

1. People do not like email-based patch processes.2. GitHub made everything dead simple, and free. Lots of Open Source projects have flourished because GitHub is both easy to use and makes collaboration across repository painless.3. Very few peopleactuallycare about decentralization. As long as you have a full copy of your repo on your own machines as well as GH, it’s hard to argue you’re gaining anything with decentralization.4. Most people also don’t want to self host a git server.

reply

rsyring
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> How people managed to put all their eggs in one intermittently available service is beyond me.

It's beyond me how people on HN can be ignorant to why GitHub gained so much market share. It's because for most dev teams, the things they add to the easily decentralized git core is *very valuable.* Arguing it's not valuable or ignoring that value doesn't help anyone.If decentralized is really going to win, then you have to have the features and DevX to match the basics GitHub provides. Because that's what people need/want. And not just the candy-ass-not-as-good-as-the-kernel-devs devs. Lots of very talented people and very well engineered projects use GitHub because it's better for what they need. Even with all the outages, people are still there. If it was so easy to move away, people would. The fact that they aren't says something important. Please consider not ignoring it.

reply

ashton314
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Forgejo is splendid. Codeberg is a hosted instance; depending on what you’re developing it may or may not be a good fit for you. But the Forgejo stack itself is decently light-weight to self-host, very fast to use, and is easy to navigate.

reply

notpushkin
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

> depending on what you’re developing it may or may not be a good fit for you

I think if your project is free / open source (edit: and you don’t use LLMs/AI), Codeberg is the a good starting point at least. You can move on to a self-hosted instance if you feel you’ve outgrown it, but even for larger projects I think you can get away with self-hosting just the CI runners.And don’t forget to donate!https://donate.codeberg.org//https://join.codeberg.org/

reply

bdlowery
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

if you use ai to program at all you can't use codeberg.

reply

cxr
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You've made the same exaggerated claim in two comments. Not only are you not banned from Codeberg if you have used LLMs to help you write code "in any of your projects", but you're not even prohibited from using LLMs to help you develop projects that you host on Codeberg.

What you can't do is "share projects that mostly consist of code written by 'generative AI'-tools". <https://codeberg.org/Codeberg/org/commit/71149c7fc95ccfeae36...>

reply

wild_egg
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I feel like you just directly contradicted yourself so there must be some nuance I am missing. Or is the key word "mostly"? Like I can use LLMs to help the work but still have to type most of the code myself?

I have not written more than maybe 10 lines of code in the last year so it seems I am prohibited from hosting on codeberg?Or is the key word "share" and that's somehow different from "host"?

reply

cxr
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I suspect the fidelity of your comment to your actual level of confusion is low. In any case, if you're really this confused by the information provided earlier, then the chances aren't good that there's anything that anyone could say to get you unconfused.

reply

wild_egg
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Right... That's exactly the kind of nonsense that turns people away from ecosystems.

Good luck with that.

reply

rhdunn
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

See also the codeberg blog post (
https://blog.codeberg.org/protecting-our-floss-commons-from-...
) which has more informal guidelines. That includes projects that are:

1. created by LLM agents -- any vibe-coded projects;2. mainly written and maintained by LLMs -- this would cover the recent changes to the rsync project;3. tied to the LLM ecosystem -- this covers pytorch, llama.cpp, cursor, SillyTavern, AI skills repositories, and a whole host of other projects.

reply

bdlowery
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not exaggerated. If you use AI at all for any code in the project it cannot be hosted on codeberg. They made that pretty clear in their blog post.

You can read it yourself -https://blog.codeberg.org/protecting-our-floss-commons-from-...

reply

cxr
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> If you use AI at all for any code in the project it cannot be hosted on codeberg. They made that pretty clear in their blog post.

No, they didn't. That's not what the blog post says.> You can read it yourselfI didn't fail to do the reading beforehand. I posted a direct link to the change in the TOS and which is currently linked at the top of all Codeberg pages. Can you read it yourself?

reply

notpushkin
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Good point, I forgot they’ve recently banned it. Updated my comment.

reply

stock_toaster
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Codefloe[1] is another forjego (with some custom patches, I believe) hosted instance.

[1]:https://codefloe.com

reply

bergie
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm nowadays hosting my projects on rngit (git over Reticulum). But also pushing a mirror to GitHub via a cronjob to increase visibility.

https://reticulum.network/manual/git.htmlI don't think moving to another forge is much of a solution, at most it is buying a bit of time. We've seen this happen with SourceForge, with Tigris, and now with GitHub.

reply

melezhik
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

DSCI - 
http://deadsimpleci.sparrowhub.io

- lightweight ( single binary written on golang )
- ci runner embedded ( podman / docker )
- pipelines are written on general programming languages - no YAML craziness - Perl/Python/Bash/Raku/Powershell/Php/Golang support 
- code editor

reply

gdorsi
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

For my personal projects I use 
https://radicle.dev/

reply

yogsototh
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I personally host a forgejo instance on a private VPS ; so far almost no maintenance except protecting it from ai-crawlers[#1]. If you don't want the hassle, codeberg.org is a public instance of forgejo.

[#1]:https://her.esy.fun/posts/0031-how-i-protect-my-forgejo-inst...I configure my local repositories to push on both Github and my forgejo instance. I am not using the CI much for my private projects (local tests are enough in my case).

reply

n4pw01f
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Self hosted GitLab has been good to me forever and has scaled and has a controllable attack surface as long as you keep on top of it

Newer app is moving to Google Cloud Secure Source Manager (because we are on Google Cloud and using backbone auth so it made more sense and less involved to manage)

reply

enriquto
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

my favourites are sourcehut (that has 
excellent
 ci, and does not try to be a github clone) and codeberg (with slightly more straightforward migration path from github)

[0] sr.ht[1] codeberg.org

reply

petcat
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Does sourcehut still require patches via email instead of "pull requests"? That was the deal breaker for me last time I looked at it.

reply

enriquto
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Does sourcehut still require patches via email

I'd guess the technically correct answer to this question is "yes". But sourcehut has very good mailing list support, that is essentially equivalent to github pull requests.Still, I find the wording of your question a bit prejudiced... as if I asked "does github still require pull requests via a proprietary interface instead of just sending the patches?"

reply

Aeolun
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It 
is
 prejudiced. If you like sending patches over email more power to you, but there’s a reason 99% of the world’s devs does not follow that workflow.

reply

internetter
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> but there’s a reason 99% of the world’s devs does not follow that workflow.

Is there?

reply

1f60c
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The specific wording sounded a bit judgy to me as well, but I think it's a totally reasonable question. They're just asking about the capability of a product.

reply

alestsurko
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

In my opinion the most underestimated git forge is radicle.

reply

bryantnyc
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

The former CEO of GitHub has launched a competitor: 
https://thenewstack.io/thomas-dohmke-interview-entire/
 Anyone using it?

reply

enahs-sf
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Homepage only has login with GitHub option. Hard to call that a competitor.

reply

nurdism
 
13 minutes ago
 
 | 
prev
 | 
next
 
[–]

selfhosting gitea has been a great experience for me, its open source

reply

hinkley
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm screwed because I am part of an ecosystem that all lives in github.

I'm not happy about the fact that GH doesn't show my when new issues or PRs are filed against projects I maintain despite the notification settings implying I should be getting notifications, but at least it's not Atlassian.I was working on major architecture shifts for a couple of libraries, to fix early mistakes or improve performance. I noticed that of them used a tool A that was dead, built on another tool B that was even deader.I found someone who was building a new B, and I made a new A and offered to swap in it on the one project. That went well, so then I integrated it to the other projects I was contributing to. Which I'm now also a maintainer on.And also the 'new B', because I pushed the intent of his library farther than he had been thinking about, contributing about 20% of the public facing API and about 5% of the internals.One of those projects is a monster, of which I'm just on a subproject. I'd never be able to get them all to move off. And any mix of GitHub and ^GitHub results in the amount of busy work I have to do to keep on top of issues and PRs more than doubles.And that's how the getcha.

reply

delf
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Creator of GitSocial here: it's a Go binary CLI/TUI that lets you store all your issues, PRs, etc. in the git itself and self-host on any S3-compatible bucket: 
https://gitsocial.org/
.

On more detailed level, it allows forgeless issue management, cross-forge PRs, git-native discussions, and much more.It has not dependencies, just git itself. Happy to answer any questions!

reply

lluisantoni
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Not sure if someone mentioned it already but I also used bitbucket in the past and found it very easy to use with a similar offering as github.

reply

magarnicle
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

We use it at work and it's fine, but they just removed the issue tracker and forced us over to Jira.

reply

ALLTaken
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I like bitbucket too, it's been really awesome and clean. No idea why everyone favored GitHub, but I had to have accounts on both for university and work

reply

guywithahat
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I really liked bitbucket, it's my favorite git management system I've used for real production work and it allows for self hosting. Self hosting is also way faster than gitlab from what I remember

reply

emeraldlinex
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Bitbucket was the perfect alternative. I used it back in the day when they were the only ones who offered free private repos. Ahead of their time.

GH beat them on UI/UX and the PR workflow I think. Really nothing more than having a better ~$120k Product Designer working there. Kinda funny whatactuallymakes people stick with 1 choice over another. Very often it’s just having better UI/UX, or offering something useful for free.

reply

1970-01-01
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I don't want to ignite an argument, but this feels like Linux v Windows. You should absolutely switch because you hate dealing with it, but the less-popular choice is going to be less popular everywhere. Your next job will very, very likely not care about your personal hatred and will simply force you back into the default, popular choice. It is sometimes best to stick with what (mostly) works for everyone unless you want to go down the path of learning another tool.

reply

64d032fe
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

What is there to learn? It uses Git. What you think it feels like, it is not.

reply

tyromaniac
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Honestly a lot of the complaints about migration feel to me like the result of poor management of actions etc. If your CI etc is so inextricably tied to github you were never doing it correctly

reply

tomasreimers
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Cursor just launched Origin, a Github alternative:

https://news.ycombinator.com/item?id=49334209

reply

bryantnyc
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/facebook/sapling
 Anyone outside of FB using it?

reply

cautiouscat
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I use Forgejo + Gitea for my home forge, then Tangled for anything I want to share with my own runner.

I self host Lore for my gamedev projects.

reply

Magicrafter13
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

My setup is a self hosted GitLab. From there, in most of my repos I setup repo mirroring (basically it just does its own SSH-based git push whenever I push commits to it) to GitHub, GitLab, and Codeberg.

All of these are free (if you ignore electricity cost of hosting your own git server), and each one is a backup of sorts.I don't necessarily recommend starting with GitLab though unless you want advanced CI capabilities, but you're already used to GitHub so you should consider self hosted gitea, which uses the same Actions syntax and even has some interoperability with its action modules I think.But yeah, my recommendation is just to push to as many (free) git hosts as you can. Why not take advantage of free code storage if it's available. Plus if any one host goes down you can still retrieve your code from the others.

reply

artooro
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm mostly using GitLab right now, both self-hosted and their hosted platform.
But am curious about Cursor Origin and certainly plan to try that out when it's available.

reply

versecafe
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

https://git.cafe
 if you want a team focused entirely on building a better forge experience rather than a github clone and don't want to deal with hosting yourself (and yes jj support is built in)

reply

ktosobcy
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I miss something like GitHub but 
- hosted in the EU
- without "FOSS only" limitation like codeberg.

I know I can self-host forgejo but would be nice to have something like forge.eu (even paid!)

reply

e-topy
 
13 minutes ago
 
 | 
parent
 | 
next
 
[–]

SourceHut is actually from Amsterdam, and has both unlisted and private repo visibility.

It's also self hostable, but I'm on the $2 tier and damn is it good.

reply

matheusmoreira
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

GitHub Sponsors. It's a nice way to for free and open source developers to earn some money.

Which GitHub alternatives have anything like it?

reply

jm4
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I self host Forgejo on a cheap VPS with hourly borg backups to rsync.net. It's a great system and seems comparable to github, although I'm not a heavy user of actions on either platform. I do use the container registry though. It was a smooth transition and easy to install. I used the docker installation method. Forgejo is great if you don't mind hosting yourself.

reply

melezhik
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

You may consider dsci as its ci is baked in and it uses general programming languages directly as the first class citizens

reply

madebywelch
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I moved to gitea + ec2 spot for actions w/ mirroring to GH for the time being.

reply

malaproping
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Branchyard launching soon! 
https://branchyard.com/
 Add your name to the waitlist.

A complete DevSecOps platform: Git forge, CICD pipelines, Private Registry, Issues/Planning, self-hosted or cloud.Our team consists of long-time members from GitLab and DataRobot.We are looking for design partners: ceo@branchyard.com

reply

tmvnty
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe the big cloud’s git solutions? Not to say the are good alternatives, but for teams already on the clouds, they could be a easier migration with somewhat feature complete, uptime, security promises that execs are looking for.

At work, we have repos on GitHub and Azure DevOps. Today, GitHub went down, but our repos (including PRs, CIs) worked as normal on Azure DevOps

reply

delduca
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Mostly of recommendations only have linux runners, I need windows and macOS.

Any recommendations?

reply

TabTwo
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

forgejo for hosting, woodpecker for CI/CD.

Hopefully forgejo gets federation in the near future because öets face it, opening an issue on Github is easy because you have an user there but you wont get one on my private forgejo instance.
Also, a tool like gh for forgejo would be nice.If you want to have an easy way to setup, have a look athttps://yunohost.org/that also offers lots of other nice stuff in its "app store" ->https://apps.yunohost.org/

reply

herpdyderp
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on self hosting Gitea right now. Hopefully it goes well!

reply

amysox
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I've been self-hosting Gitea for years, and moved everything I had on GitHub off at the time of the Micro$oft takeover.

With Amsterdam[0], I've put itbackon GitHub, but only as a mirror to increase visibility of the code. My erbosoft.com Git server will always remain the "source of truth" for the project.[0]https://git.erbosoft.com/amy/amsterdamandhttps://github.com/amysoxcolo/amsterdam

reply

techknowlogick
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Best of luck! I'm one of the project leads of Gitea, and if you run into any issues please feel free to hop into our chat:)

reply

BaudouinVH
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

some european alternatives : 
https://european-alternatives.eu/alternative-to/github

reply

bfrog
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

radicle.xyz to avoid centralization again

reply

iamnothere
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Disappointed to see only one mention of this.

With Radicle you can continue to work locally with all issues etc intact, even if your “main” host is down. You can also sync through other hosts in the network.

reply

timedude
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Try Fossil

https://fossil-scm.org/home/doc/trunk/www/index.wiki

reply

grommz
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Has anyone tried Tencent CNB? It offers generous free quotas.

https://cnb.build

reply

nusl
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Anything with Tencent on it is a no for me.

reply

ALLTaken
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Why, would you please share?

For me it's usually a green-flag, since it automatically means they optimized for high-scalability first, as their userbase is gargantuous!

reply

guywithahat
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Because China is a terrifying country with no real notion of human rights. Basically all Chinese companies (including Tencent) work closely with the government and do what they want under threat of arrest. There’s no way I’m uploading my data to China where their government can get at it whenever they want.

reply

rowbin
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Can recommend 
https://codefloe.com

reply

keithnz
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

to your actual question, no, it really doesn't make sense. The problem is you are saying it is down consistently.... and it's not. You can switch if you want, but from my observations, it's not really that often, and those that do switch make a bunch of compromises when they do. I'd only consider it once you actually measure the impact to your business. Based on actual data and not feelings, then consider whether it is worth it given all the costs of switching. We use it all the time and at most, may have had 30 minutes where we were stuck.

reply

hum3hum3
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Like others I migrated from github to codeberg. But since lots of my projects are coauthored with Claude I moved to self hosting Forgejo on a small Hetzner instance which also does some static hosting. So far working well. I think some cross platforms stars and search would be good.

reply

epiccoleman
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been a Gitlab fan for a long time[0]. I typically default to GitHub for my repo slop[1], but if I'm doing something serious I put it in Gitlab. I like their CI setup better than GitHub and there's also self-host options if any of those "serious" projects ever needs that.

Also back in the day, you needed a paid account to make private repos on GitHub, but Gitlab made them free.Anyway I haven't heard anyone complaining about Gitlab going down constantly, maybe just a function of not being the default slop-forge in the AI era, but still, they've been a long time friend to my constant hackery.Also, Microsoft sucks.[0]: over the years the UI has gotten a good bit more cluttered and annoying, so there's probably slicker stuff out there. But it's fine.[1]: some of this is definitely vibe-coded LLM-vomit but I mean a more general type of slop in this case - random throwaway code, half baked ideas, etc.

reply

KaiserPro
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I've used github for ~12 years, and it was fine for single repos, but it sucked _hard_ for any kind of organisation. It also sucked really hard for CI.

I joined a company that was using hosted gitlab. I really liked it, apart from it had the same uptime as github has now.Features wise its about the same as github now, apart from organising repos is far simpler. Its not a flat list in an org, you can have sub teams in an org with thier repos neatly owned.However the security story around them is not great, so I'm not really sure that I'd want to host a public instance of gitlab.

reply

Helmut10001
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes! And for those complaining that gitlab CE selfhosted is resource hungry: It can be tuned to only use 2 GB memory in total and run perfectly fine for a single developer or limited concurrency. Gitlab CI is awesome.

reply

dawn3727
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

You might want to consider checking out GitLab and Gitee.

reply

teekert
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

You mean Gitea [0], a community-driven fork is Forgejo. There was some drama, have to admit is still don't really understand it (ask an llm I'd say). Codeberg [2] uses Forgejo and offers it as a hosted service.

[0]https://about.gitea.com/[1]https://forgejo.org/[2]https://codeberg.org/

reply

Havoc
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Other way round. Forgejo is a fork of gitea

reply

teekert
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's what I said, but indeed in a very bad way :)

reply

esseph
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, it's not what you said.

Gitea is a fork of Gogs.Forgejo is a fork of Gitea.Codeberg folks forked Gitea to create forgejo.

reply

esseph
 
51 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

"Forgejo was created in October 2022 after a for profit company took over the Gitea project. It exists under the umbrella of a non-profit organization, Codeberg e.V. and is developed in the interest of the general public."

https://forgejo.org/compare-to-gitea/

reply

arccy
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Technically gitee is also a git hosting provider: 
https://gitee.com/

(scroll to bottom right corner for language switcher).

reply

techknowlogick
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

FWIW Gitea is still community driven as before, there are yearly elections for the community maintainers for TOC leadership.

disclaimer: I'm one of the project leads of Gitea

reply

alightsoul
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Gitee is Chinese. If you're in the US, it's considered a risk because it's Chinese. But people outside the US will not care.

reply

dawn3727
 
48 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That’s terrible; this shouldn’t be a barrier to using technology.

reply

jonstaab
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

If you want to try something a little bit more off the beaten path, 
https://gitworkshop.dev/
 is a code forge built on nostr

reply

TabTwo
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

oh, thats an awesome idea!

reply

fosterfriends
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://cursor.com/origin

reply

kamikazechaser
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been hosting gitea for our small org (docker + sqlite) for close to 5 years now. ~50+ repos, some large. All upgrades, including major changes, have been as easy as just changing the tag and reloading the container.

reply

VCFundedGenYer
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I moved to Codeberg months ago in response to GitHub's unreliability, poor moderation and random/illegitimate takedowns, and overuse of AI.

Have never regretted the switch + I love the no AI policy.

reply

rambojohnson
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

how has nobody mentioned 
https://codeberg.org
 ?

it gives you the obvious gitHub alternative: open-source, community-owned, privacy-respecting, non-corporate, and not built around turning your development workflow into a Microsoft-owned platform.

reply

dreamcompiler
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

All of that is good except if you also have a lot of private repos at GH, you cannot move them to Codeberg.

reply

ivan_gammel
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I moved recently to Gitoro with private projects, but do not have any meaningful opinion about it yet. It works for me, it’s fast, nothing to complain about. Just mentioning it here as EU-hosted alternative.

https://gitoro.com/

reply

thangalin
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

https://repo.autonoma.ca/treetrek

I self-host using my own read-only, FOSS, pure PHP Git repository reader for personal projects.

reply

stackghost
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

What about a mailing list and `git format-patch`?

reply

srfrog
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

AWS CodeCommit + CodeBuild. All day long.

reply

HeadOfProbing
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

What are people using as alternatives for GitHub Actions specifically these days?

reply

Bnjoroge
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Hopefully a good spot to plug my own project, preloop, which is a drop-in replacement of Github actions(both the runners and control plane) that runs locally or self-hosted in isoalted microvms, and supports debug-on-failure. You can also push to the server, run CI and then optionally create a draft PR. Not quite production-ready yet(for the self-hosted part), but the local part works well. We implement the official runner protocol 100% unlike act/gitea/forgejo, so your workflows are more likely to work out of the box with preloop(forgejo has the closest compatibility with Github Actions though so it's a good off-Github option) and we use microvms so no DinD issues. I'm working on getting the official runner vm image up to reduce any environment incompatibilities. Feel free to try it out: 
https://github.com/preloopdev/preloop

reply

HeadOfProbing
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Looks neat! I'll try your project if you try mine: 
https://getprobed.chat/

reply

Bnjoroge
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! Yours looks good too! What would you say is the difference with Slack connect? I find slack connect to be pretty painful once you have n > 50 channels

reply

HeadOfProbing
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A big difference between Probed and Slack Connect is being able to create public community channels where all your users can talk to each other. You also get a feedback system, a public roadmap, and other features to help foster that community-driven growth.

reply

bdcravens
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Classic CI vendors like Semaphore, Circle, etc are options.

reply

maratc
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I feel like something is missing from your list of "classic CI vendors" but can't exactly jput my jfinger on jit.

reply

thewisenerd
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

are we referring to jenkins here perhaps?

reply

sssilver
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

If only there was a convention for storing PRs and issues and wiki inside the repository itself, similar to how Fossil[1] does it.

Then all the GitHubs and Gitlabs of this world would be limited to just providing UI and would be unable to hold our data hostage by design.[1]https://fossil-scm.org/home/doc/trunk/www/index.wiki

reply

rwl
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

I started using fossil recently and have been quite pleased with this aspect of it. I miss a few things from the git world (mostly magit and its magical ability to stage individual hunks of a diff) and there are a few rough edges, but I totally agree that having a wiki and issue tracking inside the repository makes so much sense. fossil‘s simplicity is a breath of fresh air for anyone who has to use git from a CLI. Well worth a try for anyone on the fence.

reply

zhynn
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I love Fossil, I have been using it for all of my projects for the last couple years. Things that I love include:

1. batteries included single-file functionality (fossil binary + sqlite file and I have everything!)
 2. Hosting them is super easy, I have a lighttpd server configured to do cgi-bin, and i just pop the project.fossil file onto the server and I have a project.The biggest friction is managing users across repos. Each repo is its own RBAC, the "zhynn" user in one repo is not the same as the "zhynn" user in another repo. It would be cool to be able to sync users across repos, which should be possible with sql, but I think that it could get weird with repo-specific permissions. Currently I just add my user to each new repo, granting that user setup permissions, and removing the admin before I scp the .fossil file up to the webserver.In the end though, I intend to use it for all of my personal projects from here out.I have a pipe dream of turning a fossil repo into a portable distributed more-async-friendly slack clone, where the "chat", "wiki" and "forum" functionalities are all used as the back-end for a responsive UI that basically does the same thing that slack does, but lives in a single sqlite file + binary. It could run mostly offline in a kind of scuttlebutt/limited connectivity pattern (when online push/pull messages, get latest chats/files/etc, go back offline. As you go through the content, make your responses locally, then go back online, push/pull again, repeat.)I have another pipe dream of making a RedBean APE fossil UI. I think it would be cool to have a single file universal executable that is my project repo.

reply

hju22_-3
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Those two pipe dreams sound really cool! Do you have a website or something to lurk you via if you eventuality get around to those? I find it difficult to keep up, as it were, using form histories and other social media platforms.

reply

sssilver
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The workflow is paradigmically different, and that may throw many people off.

There's no rebase, on principle. Branch names are permanent attributes of commits. Even abandoned branches remain visible forever. Code review is post-hoc.People who are extremely accustomed to Git workflows may find the paradigm alienating.

reply

rwl
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yep, it’s not for everyone, and their docs are pretty clear about that. OTOH those same docs contain a variety of arguments that 
git
 isn’t really designed for everyone either and that fossil might be a better fit for projects that have just one or a handful of developers, which AFAIK is the vast majority of projects on Github. My experience is that it is certainly an adjustment but the docs are good at explaining (and justifying) the differences, and the built-in features are very useful, especially for anyone looking to reduce their dependence on a centralized host that’s become unreliable.

reply

jolaflow
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Epiq also solves this with a git-native backend, so it is vendor agnostic and adheres to a issue-tracking-as-code paradigm. It is therefore distributed, has a TUI + browser GUI, mcp server, and so on.

https://ljtn.github.io/epiq/

reply

jolaflow
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is also event sourced, and supports state replay from beginning to end, so very powerful for auditing workflows, whether that be your own or a swarm of agents.

reply

paularmstrong
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've used git-bug[1] for issues and it works pretty well. The web-ui is lagging behind and PR support would be everything you'd need to ditch a central-hosted web instance.

[1]https://github.com/git-bug/git-bug

reply

michaelmure
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

FWIW, I have a new and much better webui that I need to release. I'm also planning to work on PRs and other stuff around the end of the year.

reply

ktm5j
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

My org self hosts the community version of gitlab and we are perfectly happy with it. Manage your own infrastructure, put the work into maintaining it and you'll have much fewer headaches.

reply

BaudouinVH
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Ironically hosted on Github Gogs is a self-hosted forge : 
https://github.com/gogs/gogs

reply

lnenad
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm running gitea successfully with very little resources.

reply

techknowlogick
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

That's great to hear! I'm one of the project leads of Gitea, and if you ever run into any issues please feel free to hop into our chatroom:)

reply

lnenad
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You've built a great piece of software, thank you!

reply

r0b05
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Forgejo/Gitea is lightweight and easy to setup.

reply

dxbhack
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

don’t switch reactively, but use the outages as a trigger to evaluate alternatives and make sure a GitHub outage doesn’t stop critical work.

reply

CodeAndCuffs
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

If an org is heavily invested in GitHub Actions and GitHub App integrations, is self-hosting GitHub enterprise the only practical option?

reply

Bnjoroge
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Hopefully a good spot to plug my own project, preloop, which is a drop-in replacement of Github actions(both the runners and control plane) that runs locally or self-hosted in isoalted microvms, and supports debug-on-failure. You can also push to the server, run CI and then optionally create a draft PR. Not quite production-ready yet(for the self-hosted part), but the local part works well. We implement the official runner protocol 100% unlike act/gitea/forgejo, so your workflows are more likely to work out of the box with preloop(forgejo has the closest compatibility with Github Actions though so it's a good off-Github option) and we use microvms so no DinD issues. I'm working on getting the official runner vm image up to reduce any environment incompatibilities. Feel free to try it out: 
https://github.com/preloopdev/preloop

reply

woodrowbarlow
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

no; gitea and foregjo both support actions-style CI/CD and both serve mostly GH-compatible APIs and have GH-style apps. it's not 100% compatible (forgejo is a little more compatible than gitea [^1]), but many of your workflows might "just work" without even renaming the .github folder.

^1: in my recent experience, for my particular use cases

reply

techknowlogick
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm one of the project leads of Gitea and we've put a ton of work into Gitea Actions, I'd be interested in any compatibility gaps that you've run into.

reply

woodrowbarlow
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

oh hello, thank you for your work on an excellent product! one small difference i ran into last weekend is that foregjo forwards the FORGEJO_TOKEN in the environment to composite actions so that they don't need to have a required "token" input.

reply

Bnjoroge
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

mind trying 
https://github.com/preloopdev/preloop
? We follow the official runner protocol 100% so we should hopefully have more workflow-compat.we also run in cross-platform microvms, not docker containers.

reply

jdub
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Buildkite has built a GitHub Actions adapter... a good first step out of the GitHub Actions supply chain attack trap.

reply

beoutdoors
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

My org uses a self-hosted instance of RhodeCode Enterprise. It's not as feature rich as GitHub, but it's worked well for us.

reply

zdgeier
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building a non-git alternative

https://oak.spaceWould love for anyone to check it out!

reply

pwython
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Very interesting, I missed your original post[0], will definitely look into it further. What's new since you've posted?

[0]https://news.ycombinator.com/item?id=48631726

reply

zdgeier
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We've added some things like CI, Windows support, and starting some work on path-based permissioning for monorepos. These are still in the early stages so not documented that great yet and need to be tested a little bit more. Should have more updates in the next couple weeks.

reply

andrewpolidori
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

for local Canadian based workflows that want sovereignty, I recommend 
https://about.worktree.ca

reply

__turbobrew__
 
36 minutes ago
 
 | 
parent
 | 
next
 
[–]

Note, currently worktree is just wrapping OVH as their “sovereign cloud”: 
https://docs.worktree.ca/sovereignty/

I was wondering when reading their sovereignty docs why I wouldn’t just use OVH as it is a French company instead of a USA based company, and lo and behold they are just reselling OVH.I have used OVH personally and it has pretty good prices, but over aggressive DoS protection. Some of my workloads were shut down because OVH internal tools decided that what I was doing must have been a DoS.As a Canadian I welcome a Canadian owned cloud provider, but it is a huge endeavour to build that platform up from scratch.It does seem kind of weird that they are building both a CI system and a cloud, seems like they should pick one.

reply

__turbobrew__
 
20 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Also they are using a home baked S3 compatible storage system and longhorn for block storage: 
https://docs.worktree.ca/updates/post-mortems/2026-07-20

I haven’t the slightest clue why they didn’t use rook/ceph (they run on k8s) for this which not only is a very reliable block storage system, but also offers a S3 compatible API, and is proven at other cloud providers like Digital Ocean.I wish them the best but there is no way I would put my data into there.

reply

CIARobotFish
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'll second Worktree. I'm US based and have been using it for over a year. Very, very happy with their service.

reply

lowbloodsugar
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Disappointed 
https://aboot.worktree.ca/
 doesn’t work.

reply

ChrisArchitect
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently:

GitHub has alternatives, but no replacementhttps://news.ycombinator.com/item?id=49135365Why developers are ditching GitHub for Codeberg and self-hosting alternativeshttps://news.ycombinator.com/item?id=48842611

reply

AndrewKemendo
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been happy self hosting gitea

https://about.gitea.com/

reply

techknowlogick
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Woo! Thanks for the shoutout. I'm one of the project leads of Gitea, and if you ever run into any issues please feel free to hop into our chat:)

reply

AndrewKemendo
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Awesome

It’s my go to now for all my private projects

reply

wejick
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

What part of github that's so sticky?

For me it's action and PR history.

reply

VaibhavKalra
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I guess we need a simpler alterntive to github

reply

0xbadcafebee
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I have a pretty bad taste in my mouth from GitHub, GitLab, Forgejo, Gitea, etc. They all attempt to hijack Git itself and become a monolith and single custom interface, rather than independent components that work 
around
 the Git repo. I want the Unix philosophy applied to Git and other functions. That way I'm not forced to switch the entire kitchen sink out when some single piece of functionality or hoster ends up breaking things.

reply

arsenkk
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

cursor are launching a new one soon - 
https://cursor.com/origin

reply

PufPufPuf
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

We already have a vibe-coded forge, it's called GitHub

reply

esafak
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This one is not managed by Microsoft.

edit: I'll take their engineering culture over MS.

reply

arsenkk
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This one is managed by SpaceX now.

reply

PufPufPuf
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What "culture"? I've seen Cursor's AI-coded web browser... which was released with parade despite not even compiling and being just millions of lines of glue code over external libraries actually doing the real work.

reply

vehemenz
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

My org's GitHub Enterprise never goes down. The feature set is almost the same, though it lags a few months behind. At least you don't have to learn anything new.

reply

jtokoph
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

My previous org’s GHE went down all the time. It couldn’t handle the CI and automation tooling hitting it as often as an org of our size needed it to. So I can totally see cloud not being able to handle the new AI scale

reply

herpdyderp
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm assuming you mean Enterprise Server (non-cloud), because my GitHub Enterprise Cloud is down right now.

reply

bigstrat2003
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Whatever you do, you should self-host it. Then you aren't going to be at the mercy of some third party when they start to get hammered by vibe coders doing an insane amount of traffic. Forgejo is a great option if you want something git-based. I'm personally very partial to Fossil, it works well and is dead easy to set up.

reply

Gronnfalk
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Try Gitlab, Bitbucket, or Codeberg.

reply

slackfan
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

We're moving over to self-hosted forgejo. Interface is roughly similar, featureset is roughly similar enough.

reply

Pxtl
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

A big thing with Github its the unified functionality across most of the OSS world - that we can search across all projects, leverage pipeline actions from other projects, and easily have a single dashboard for our own contributions and interests across all projects.

I'd hate to see a move to forge balkanization lose this functionality. But this would not be heavyweight data to federate. So are there any forges with a good story for federation?

reply

dboreham
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

There was some work to address this issue with federation in Gitea, but I haven't kept up with how well that went. Our practical solution was to just mirror our Gitea repos into GitHub. That way they're discoverable, releases can be downloaded, and so on. Not a perfect solution because users get confused as to why they can't open issues, etc.

reply

techknowlogick
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I was one of the members who was a part of the initial grant for federation in Gitea, but sadly due to illness and other similar neither I nor my teammate were able to work on the grant (so no funding ended up being released), however the work we did start was completed, and we have continued to work on foundations since. Since spam/moderation/limitations are so significant we are focused on that portion first, since we don't want to open up another vector for it without having at least the minimum of protections in place. We have also been extremely fortunate to have experienced developers who do work on existing federated software share so much of their time, expertise, and experiences with us to help shape our work.

reply

Pxtl
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That would be good for following, but I'd worry about contributions. Single-sign-on would help but if you're going to ask the user to create a new username+password to log a bug you're not going to get bugs from anybody except your most hardcore users.

Also, unified dashboards/notifications are so useful (even though Github's notification UI is a bit mediocre, imho).

reply

esseph
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Your first concern is not the reliability of GitHub (lost $$$) or any dark patterns they push, or their security, but the network effect?

Source repository should be its own thing.Artifacts repository arguably should be its own thing.PRs, own thing.CI, own thing.The Balkanization has always existed. Lot of stuff that isn't on GitHub.

reply

Pxtl
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's the chief differentiator you're giving up when you give up on github vs a self-hosted forge. And the network effect of the CI pipelines should not be discounted since it means actions published 
anywhere
 on GH are automatically available for use without any import or install step.

Yes, you could feasibly split off the CI from the git+PR service, but you'd still want it to be federated.

reply

esseph
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Pipelines are not magic. You want a couple of primitives in there, variable substitution, maybe lite secret management. Depending on the type and languages you work across they could also be 100% unique to each company, language, project, and industry. LLMs have also further made pipeline creation pretty trivial.

If you can use or make a GitHub action you will be just fine in GitLab, CircleCI, Jenkins, or a couple of shell scripts hacked out over pizza and beer on a weekend.There's no pipeline moat, to put it another way.

reply

sneak
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I self host Gitea and have been supremely happy with it.

reply

zuzululu
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I want to know what the best guide is for running your code repo at homelab type of setup? proxmox? what hardware to buy?

i dont wanna get too crazy i just dont trust github with my code anymore

reply

melezhik
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Try dsci / it’s super simple

reply

fortran77
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I loved the simplicity of Amazon CodeCommit. Unfortunately, Amazon decided to deprecate it, no new provisionion but existing accounts could remain. I'd love it if someone else offered a similar product.

reply

AtlasBarfed
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I'd like a self-hosted primary option as the source code repository, but I'd like to mirror the code in one of the usual external options, anyone done anything like that?

reply

timetraveller26
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

For CI/CD woodpecker has been working for us really well 
https://woodpecker-ci.org/

reply

bdlowery
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

use codeberg if you're ok with never using ai in any of your projects. Any AI use and your repo is banned. - 
https://blog.codeberg.org/protecting-our-floss-commons-from-...

reply

anticensor
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

If you accept a non-Git VCS, Pijul Nest.

reply

emeraldlinex
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

GitHub is like World of Warcraft, in that you can’t kill it with another GitHub.

reply

rvz
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

It is time to switch to self-hostable alternatives.

It made sense 6 years ago as I said before [0], today it makes even more sense to self host with GitLab, Gitea or Forgejo....Or we can repeat the same issues again with Cursor Origin [1].[0]https://news.ycombinator.com/item?id=22868406[1]https://cursor.com/origin

reply

beanjuiceII
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

i use it quite often and it has not really been 'consistently down'

reply

throwitaway222
 
3 hours ago
 
 | 
prev
 
[–]

I wonder how hard it would be to vibe code a super basic gitea/gitlab clone (or a very stripped down version) that's designed to just have basic authentication w/ssh, some basic main branch protections, simple code review, etc... and runners with some simple YAML language.

I bet you could do it with like 10 prompts.

reply

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search:
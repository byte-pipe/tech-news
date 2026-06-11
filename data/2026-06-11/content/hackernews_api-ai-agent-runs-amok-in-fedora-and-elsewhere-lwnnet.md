---
title: AI agent runs amok in Fedora and elsewhere [LWN.net]
url: https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/
site_name: hackernews_api
content_file: hackernews_api-ai-agent-runs-amok-in-fedora-and-elsewhere-lwnnet
fetched_at: '2026-06-11T12:23:35.246780'
original_url: https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/
author: tanelpoder
date: '2026-06-11'
description: AI agent runs amok in Fedora and elsewhere
tags:
- hackernews
- trending
---

### Welcome to LWN.netThe following subscription-only content has been made available to you 
by an LWN subscriber. Thousands of subscribers depend on LWN for the 
best news from the Linux and free software communities. If you enjoy this 
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByJoe BrockmeierJune 10, 2026Agentic AI systems can be used to do a variety of things
autonomously on behalf of a human user: open or manage bugs, generate
code, submit pull-requests, and (apparently) evencomplain about
rejection. In May, a Fedora developer discovered that an allegedly
rogue agent had been pestering the project in a number of ways:
reassigning bugs, fabricating unhelpful replies to bugs, and even
persuading maintainers to merge questionable code into theAnaconda
installer. It also submitted a number of pull requests (PRs),
some accepted, to several upstream projects. The Fedora account
associated with the agent has had its group privileges revoked and the
messes have been mopped up, but the motive behind the agent's actions is still
a mystery.#### "Kind of erratic"On May 27, Adam WilliamsoncopiedFedora's developer and testing mailing lists on a message to Nathan
Giovannini about what appeared to be an unsupervised agentic AI system
under Giovannini's control. "It's great that you're trying to fix
things, but the results seem to be kind of erratic."Williamson said that he was still looking through the history of
Giovannini's actions in Bugzilla, but had already spotted a number of
problems. For example, Williamson had found dozens of instances of
Giovannini's agent assigning Bugzilla entries to his accountafter submittingallegedly relatedpull
requeststo upstream projects, or closing
a bug after aPRwas merged
into an upstream project. In some cases, the agent simply closed bugs
withcommentsthat either restated the original bug or were, as Williamson said of
thiscomment,
"superficially plausible, but problematic in other ways".In addition, Williamson said that Giovannini (or his agent) had
submitted patches that were incorrect and then "replied to
objections with LLM-generated justifications that eventually
overwhelmed the maintainer into merging the fix". The agent, as
GitHub user "nathan9513-aps", had
submitted apull
requestfor the Anaconda
installer used by Fedora and other Linux distributions. The PR's
description claimed it was a fix foran Anaconda
bugthat would cause installation to fail, but the patch actually
preserved a kernel option passed on the command line that seemed to
havenothing
to do with the actual bug.The agent's GitHub account has since been disabled. It now shows up in
conversations on GitHub as "ghost", which is the platform's
default placeholder for user accounts that have been deleted. Thus, it
is difficult, if not impossible, to piece together a full trail of all
the agent's actions on GitHub.Williamson said, rather diplomatically, that the agent's actions were not
"having a positive impact on Fedora or the upstream projects",
and suggested that Giovannini adjust the agent to be "substantially
less autonomous". He specifically asked that the agent not assign
bugs to Giovannini, change their state, or "post confident
assertions or specific action recommendations" without human
review.#### Hacked?Later on May 27, Williamsonsaidthat Giovannini had replied to him privately to say that his
credentials had been compromised and that he was not the one behind
the AI system. "Obviously we should therefore treat any actions it
has taken with suspicion", Williamson said. He planned to review
the bugs touched by Giovannini's account "even more
aggressively", and asked for help from others to review them as
well.Areplylater that day, ostensibly from Giovannini, said that he was able to
regain access to his GitHub and Fedora accounts "and I am currently
securing and reviewing all involved systems and credentials". The reply 
said his GitHub account was "nathangiovannini99". Williamsonrepliedthat the GitHub account was only an hour old, and that the recent
emails to the list and sent to Williamson privately did not seem like
messages Giovannini had sent in earlier interactions with the
project.Giovannini has participated in discussionsat
least as far back as 2018, and hisactivity
in Bugzillagoes back to at least 2016. He does not appear to
have been a particularly active contributor to the project, but his
involvement clearly predates the agentic AI era. Whether his account
is now being operated by a human attacker, an agentic AI, or a mix of
both, it has a legitimate history prior to its recent activity.Williamson said that he had reviewedaccount
activity in Bugzilla by "nathan95"from this year, and found
suspicious activity, such as severity and priority changes to a bug with no
justification, beginning on April 7, inbug
2416721. Activity before that appeared legitimate, he said, and
none of the activity that he had seen so far looked outright
malicious.He also identified another GitHub account, "leurus27-boop", as likely
being associated with the same agentic AI. That account is still
active, and has submitted aPRto theopenSUSE
Commander(osc) command-line interface for theOpen
Build Serviceas well asa PRto thelxqt-policykitrepository. That project is used to extend the privileges of the LXQt
desktop'slxqt-adminGUI tools for administering operating-system settings such as user and
group configurations.Williamson said that it would be good to look
through any other actions by the related accounts and warn other
projects that they should review anything that had been submitted by
them. Williamson seems to have followed up on each PR towarnother maintainers "the whole situation is extremely
fishy". Kevin Fenzisaidthat he had removed the nathan95 user from any groups it had been in,
so it should no longer have the permission to reassign or close
bugs.#### Pre-attack?Martin Kolman, a member of the Anaconda team,saidthe events were "really problematic" even if not malicious. The
team had spent a lot of time reviewing PRs from what seemed to be an
eager contributor: "while it started to look off after a while, all
the replies were still like this - a bit weird, but still
*plausible*". He also theorized that it could be an attacker
working their way up to malicious activity, much like theXZ backdoor:Unfortunately, for an actual attack the preparatory phase could (and
for the Xz attack did) look very similar - a new contributor slowly
gaining trust in the community, getting in harmless changes and
building up to the point when the attack payload can be injected (or
the changes not actually being harmless if combined the right way).So not saying this was it, but an AI agent automated attempt at a Xz
like compromise might really look very similar what we have just seen
here.Chris Adamssaidthat the commit to Anaconda should be inspected and probably reverted
immediately. Kolmanrepliedthat it had beenreverted. He
alsoconfirmedthat the LLM-generated PRs had made it into theAnaconda 45.5release on May 26. They were reverted in theAnaconda 45.6release on June 2.The targets certainly suggest that it may have been a prelude to an
attack of some sort; an operating-system installer, a utility for escalating
user privileges, and a tool for interacting with a build system all
seem like promising avenues for inserting malware or hijacking
systems.It's disconcerting that what appears to be an AI agent has had so
much success after gaining access to a human contributor's accounts.
It seems that an AI agent with access to an account with a legitimate
history of interacting with projects stands a good chance of
persuading busy maintainers to accept questionable
contributions. Happily, Williamson caught this before it became a
bigger problem. Let's hope that other human maintainers are as
observant.to post comments### Merged PR in upstream projectsPosted Jun 10, 2026 16:06 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link] (12 responses)> It also submitted a number of pull requests (PRs), some accepted, to several upstream projects.It would be very interesting to see a link to at least some of those PRs, especially the accepted ones.Do we need to worry?### Merged PR in upstream projectsPosted Jun 10, 2026 16:13 UTC (Wed)
 byjzb(editor, #7867)
 [Link] (10 responses)I did link to the PRs for OSC and LXQt.Do we need to worry?Well... I am. But I might be a bit paranoid.### Merged PR in upstream projectsPosted Jun 10, 2026 16:20 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link] (9 responses)> I did link to the PRs for OSC and LXQt.Yup; sorry. I didn't find any in the text near that, nor with a search of keywords like "merged" and "accepted". But I've found some after carefully reading.>> Do we need to worry?> Well... I am. But I might be a bit paranoid.Yup; me too. I'm kind of between being worried, and thinking this was obviously predictable and thus negligence. That's why I plan moving to vim-classic as soon as possible, and similar stuff, and also why I don't accept any LLM-poisoned contributions.### Merged PR in upstream projectsPosted Jun 10, 2026 16:28 UTC (Wed)
 byjzb(editor, #7867)
 [Link] (1 responses)That's helpful feedback; I'll work on being extra-extra-clear on those kinds of links next time around...### Merged PR in upstream projectsPosted Jun 10, 2026 16:32 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link]Nice! :-)### Merged PR in upstream projectsPosted Jun 10, 2026 18:43 UTC (Wed)
 byWol(subscriber, #4433)
 [Link] (6 responses)> and also why I don't accept any LLM-poisoned contributions.Just because you're paranoid, doesn't mean they're not out to get you.And how, anyway, do you plan to avoid - "LLM-poisoned" as you call them - contributions? I get the impression these "slipped through the net" because they came from hijacked accounts (or from human accounts with dodgy motives) and didn't ring alarm bells.What we *need* is a human "in the loop" at all times. What we're getting is - as the title puts it - "agents running amok" and overwhelming the humans. Who's to say *you* won't be taken in?Cheers,Wol### Triaging LLM-poisoned or other malicious activityPosted Jun 10, 2026 19:46 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link] (5 responses)> Just because you're paranoid, doesn't mean they're not out to get you.I remain alerted.> And how, anyway, do you plan to avoid - "LLM-poisoned" as you call them - contributions?The first measure is to disallow anything that has touched an LLM in the slightest way. The actual specification is:|	It is expressly forbidden to contribute to this project any|	content that has been created or derived with the assistance of|	AI tools.||	This includes AI assistive tools used in the contributing|	process, even if such tools do not directly generate the|	contributed code but are used to derive the contribution. For|	example, AI linters, AI static analyzers, and AI tools that|	summarize input are forbidden.This already removes a large amount of LLM-poisoned contributions. That keeps the amount of contributions to reasonable levels.Then, we can group contributors in 4 categories:- Those that are unaware of the policy, and publicly disclose use of LLMs.- Those that are unaware of the policy, and don't say anything about using AI.- Those that are aware of the policy, and comply with it.- Those that are aware of the policy, and don't comply with it.Most fall under the 3rd category. Between 1st and 2nd category, usually, more competent programmers tend to be on the 1st category, and the least competent/experienced ones might be on the 2nd category.This is nice, because it's easy to spot inexperienced programmers after a few emails; once I suspect that they're inexperienced and that they might have violated it or if they've done something else wrong, I point them to the contributing guidelines (not the AI policy, but the entire contributing policy, so that they don't feel offended), just asking them to check them for a revision of their contribution. If they are benevolent, they'll easily find the AI guidelines and tell me they used AI, and then we figure out how to proceed (e.g., discard the patch, and start from scratch).That leaves us with the 4th category.Because the amount of contributions are at reasonable levels, I have the time and energy to actually interact with contributors enough to have them talk quite a bit. Once you talk for a while with contributors, you can get a sense of whether they talk like humans, and whether they understand and can defend their contributions in discussion.Common suspicious things are:- The contributor suddenly changes little details from one version of a patch to the next, without being able to justify them (and often being completely silent about it).- The patch contained more code than necessary for the change, and can't justify the extra code.- Entirely ignoring some important feedback.The more alarms ring in my head, the more picky I'm with a contributor. After all, they are the ones to prove that the contribution is correct; I should not be reviewing their code, but rather help them review it for me.At the moment, I don't think an LLM can pass this without triggering alarms; maybe in the future they improve enough, but we'll see.Maybe for small contributions (one-liners), LLMs may have larger success rate with this filter, but those are less important. I don't expect significant contributions that are LLM-poisoned (in a significant amount) to pass it. It's not a matter of being perfectly clean of LLM-poisoned contributions (and it's mostly impossible, just like low-background steel); it's a matter of filtering enough to be safe.> I get the impression these "slipped through the net" because they came from hijacked accounts (or from human accounts with dodgy motives) and didn't ring alarm bells.I think a benefit of email-based patches is that the hijacked account will often receive a copy of the email even if they have been hijacked, while accounts in pages might be more difficult to spot. If I send an email to Respected Developer replying to a patch that it sent, it will probably receive a copy of my response, and if it didn't write to me, it will probably suspect something's wrong. And if they don't receive any emails at all, they'll also suspect.Anyway, I keep the mental filter from above enabled for old programmers too, because these days many old programmers also use LLMs.If there's an old programmer that is a frequent trusted contributor, I will actually disable my mental filter. However, I expect I would be able to distinguish the way they talk (precisely because I talk to them frequently), and if they're hijacked, I expect I'd at least suspect something.Not perfect, but it works for me.### LLMs can find real bugsPosted Jun 10, 2026 20:02 UTC (Wed)
 byDemiMarie(subscriber, #164188)
 [Link] (3 responses)LLMs can and have found real bugs, including security vulnerabilities. The human reporter needs to filter out hallucinations, but a substantial fraction of the findings are often genuine.### LLMs can find real bugsPosted Jun 10, 2026 20:59 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link] (2 responses)> LLMs can and have found real bugs, including security vulnerabilities. The human reporter needs to filter out hallucinations, but a substantial fraction of the findings are often genuine.I guess it depends on several factors:- Age of the project.- Quality of the source code.- Number of users of the project.- Frequency of feature additions.As co-maintainer of a project that is very old (and thus, most bugs have been vetted), has very simple and robust C code, is used almost everywhere, and has few new features, I'm seeing a very low number of LLM-based reports, and only one has been useful so far (it reports a yet-unreleased bug we introduced while adding a new feature recently).Since this is not law, but rather guidelines, we could of course make an exception if we see a report that is useful enough. I've made this one exception so far, because it was trivial. However, I expect that if we didn't have that report, we'd have caught the bug within hours or a few days from users trying the release candidates or even from users of the release in bleeding-edge distros if it wasn't caught in the -rc, as has happened usually with previous releases.Interestingly, we haven't seen the flood of reports that have affected many projects (and I suspect we're a juicy target for people to find vulnerabilities, so it's probably not a lack of interest).### LLMs can find real bugsPosted Jun 10, 2026 21:34 UTC (Wed)
 byNYKevin(subscriber, #129325)
 [Link] (1 responses)> I'm seeing a very low number of LLM-based reports, and only one has been useful so far (it reports a yet-unreleased bug we introduced while adding a new feature recently).Couldn't that be a result of people respecting your contribution policy (that you quoted upthread), which explicitly prohibits contributing such reports to the project? If so, I'm not sure it provides any useful data on whether LLMs in general are capable of finding security vulnerabilities (or other problems) in your code.### LLMs can find real bugsPosted Jun 10, 2026 21:44 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link]I've published that policy in one project, but on the other one we haven't merged it yet (it's waiting for review of one co-maintainer). While regular contributors are aware of it (since we've discussed it at length), passing-by contributors have certainly not read it.### Triaging LLM-poisoned or other malicious activityPosted Jun 11, 2026 6:49 UTC (Thu)
 byNAR(subscriber, #1313)
 [Link]I guess it works until you have maybe a dozen regular and a few drive-by contributors. Neither is true for a project like Fedora. Also, a malicious actor (which might be behind this activity) won't care about the no-LLM policy, so it doesn't really matter.### Merged PR in upstream projectsPosted Jun 10, 2026 16:14 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link]Oh, here's one: <https://github.com/rhinstaller/anaconda/pull/7074#issue-4...> (linked under "Kind of erratic").### Fighting fire with firePosted Jun 10, 2026 20:08 UTC (Wed)
 bycapn(subscriber, #183548)
 [Link]Interesting that AI has doubled the number of CVEs detected in human written code in the past year, but when an AI causes a problem itself, people cry bloody murder.Now, naive enthusiasts using AI tools are a legitimate problem right now. In defense of the overeager minority, people are still in the early days of learning these new tools, and the first taste of them leaves many engineers a bit... overenthusiastic, perhaps. It's also important to remember that tools like Copilot are kept significantly behind in terms of model generations. And, in the general case as well, many cash-starved engineers turn to the much lower end, and older, models to automate things (which is obviously a rude thing to do when contributing code or other activity to an org that doesn't have them on their payroll, or hire list, and has no meaningful recourse).But, just as the landscape of the tools used to write and participate in coding projects are changing, the projects themselves must adapt to the times and embrace the new tools available for triage and code review. They can (and will) drastically reduce the load that the increased amount of activity has put on maintainers. (And, no, some briefly-considered top-of-the-head flaw in this concept of significant automation of triage and review is not fatal. We're engineers, and solving problems in such processes is basically the profession.)There is far too much seeing the glass a quarter empty, rather than seeing it three quarters full.This is the kind of fire that we can fight with the exact same type of fire. And I'm greatly looking forward to seeing just how hot the progress of open source software can get.### Credit where it's duePosted Jun 10, 2026 21:49 UTC (Wed)
 byAdamW(subscriber, #48457)
 [Link]Ooh, I'm famous again."Happily, Williamson caught this before it became a bigger problem. Let's hope that other human maintainers are as observant."To give credit where it's due: it was in fact Yanko Kaneti who first spotted this - he posted "https://bugzilla.redhat.com/show_bug.cgi?id=2481872#c1....wtf.. " in the fedora-devel room on Matrix. Kevin Fenzi flagged me (because Nathan is in the qa group) and I then took it from there and found all the other bugzilla posts, and pull requests.To answer Joe's concerns to some extent - I did look through every PR I could find from the nathan9513-aps account before reporting it to GitHub, and didn't see any that looked outright malicious, just...incompetent. As you noticed, I commented on them all to try and alert the project maintainers to the situation. I think I checked all the leurus27-boop PRs at that time too (there aren't as many, the account was only created recently).
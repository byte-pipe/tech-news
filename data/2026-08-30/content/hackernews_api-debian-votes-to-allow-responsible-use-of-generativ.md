---
title: Debian votes to allow "responsible use of generative AI" [LWN.net]
url: https://lwn.net/Articles/1091231/
site_name: hackernews_api
content_file: hackernews_api-debian-votes-to-allow-responsible-use-of-generativ
fetched_at: '2026-08-30T06:00:26.175459'
original_url: https://lwn.net/Articles/1091231/
author: pluc
date: '2026-08-30'
description: Debian votes to allow "responsible use of generative AI"
tags:
- hackernews
- trending
---

The 
results
 of the

Debian general-resolution vote
 on the use
of large language models have been posted; the winner is 
choice 5:
Responsible Use of Generative AI
.

Debian neither endorses nor prohibits the use of generative AI
	tools in the development, maintenance, or documentation of
	software, packaging, documentation, and other media published
	within the Debian Project. We recognize that such tools can
	substantially improve the productivity of contributors when used
	responsibly, allowing volunteers to spend more of their limited
	time on work that requires technical expertise, judgment, review,
	and collaboration.The Debian Project nevertheless expects that all contributions
	submitted to Debian, regardless of how and with which tools they
	were produced, satisfy the same standards of quality, correctness,
	maintainability, and legal compliance. The use of a generative AI
	tool does not diminish the contributor's responsibility for the
	work they submit. Contributors are expected to understand, review,
	test, and, where appropriate, modify AI-assisted output before
	incorporating it into Debian.to post comments### InevitablePosted Aug 29, 2026 14:03 UTC (Sat)
 bydskoll(subscriber, #1630)
 [Link] (1 responses)I'm a bit sad it went that way, but I guess it was inevitable. Debian is too large a project to be able to meaningfully enforce a stronger stance against LLMs. So I think they realized it's pointless to make rules that you can't enforce.### InevitablePosted Aug 29, 2026 15:06 UTC (Sat)
 byMarcB(subscriber, #101804)
 [Link]I, for one, am very glad. In particular the fact that the two full-Anti-AI proposals (1&3) were even below "None of the above" is very good sign. Had one of those won, the attempts to enforce them would have ruined Debian.### Extremist positions soundly defeatedPosted Aug 29, 2026 14:20 UTC (Sat)
 bybluca(subscriber, #118303)
 [Link] (3 responses)It might not be obvious due to the complexity of the voting system, but it is definitely worth noting that not only the sensible and rational position won, but the options that were set up with the implicit (or by reading some emails from some proponents, quite explicit actually) purpose of setting up witch hunts to actively punish anyone who dared not toe the extremely vague anti-AI line (option 1 to change social contract, option 3 to change code of conduct, both of which imply *expelling* any dissenter) were soundly defeated and rejected: they (and only they) both failed to beat the "None of the Above" option, which is this voting system's way to say "no, absolutely not, go away".The rest of the options cleared that line and then it was a (complicated) matter of which one was the "least unfavored" among all voters, so to speak.A handy graph that someone else prepared makes the result a lot more digestible:https://people.debian.org/~lucas/gr-2026-002/results.png### Extremist positions soundly defeatedPosted Aug 29, 2026 14:41 UTC (Sat)
 bymhvk(subscriber, #86585)
 [Link] (2 responses)It depends what you mean by "soundly" - if I read that graph correctly, about 30% of the voters preferred the no-AI options over all the others. To me, it looks like "status quo" won, which is perhaps appropriate in times of rapid change.Personally, I hope that truly open locally run models, perhaps specialized to coding, become sufficiently good that one can do without the large, closed-source ones (which to me are very problematic for lots of reasons; it doesn't help to come from a country that will be under water -- the Greenland icesheet melting completely is nearly unavoidable by now, and 6 meters of sea level rise is more than one can build dykes for; why these data centers are not forced to rely on renewable energy is truly beyond me).### Extremist positions soundly defeatedPosted Aug 29, 2026 14:45 UTC (Sat)
 bybluca(subscriber, #118303)
 [Link]> It depends what you mean by "soundly"With this voting system, failing to beat "NOTA", as mentioned, means the option is soundly rejected even before considering relative preferences### Extremist positions soundly defeatedPosted Aug 29, 2026 15:20 UTC (Sat)
 byMarcB(subscriber, #101804)
 [Link]> Personally, I hope that truly open locally run models, perhaps specialized to coding, become sufficiently good that one can do without the large, closed-source ones...In theory, they are. The problem is that the absurd investments into AI hardware have made it unaffordable. 64-128 GiB+ GPUs at home would be absolutely realistic without this cost explosion.> ...the Greenland icesheet melting completely is nearly unavoidable by now...Technically not, but I also believe we will not avoid it. But the reason for that is not AI. Its share of human energy consumption is somewhere around 0.2%, likely lower. And AI would be very amenable to using renewal energies - if any relevant government cared enough to enforce its usage.### A growing disconnectPosted Aug 29, 2026 14:44 UTC (Sat)
 byaimannajjar(subscriber, #184277)
 [Link]Ed Zitron's interviews gaining 5million views overnight on YouTube, while the people of free software embrace AI unconditionally is the wildest ironies in history.It will be interesting to watch what happens next in terms of quality and review processes as well as young engineers skills. I genuinely think it's good to have diversity in AI adoption so we can compare and contrast the net results across projects in the long term.### Maintainer opinions?Posted Aug 29, 2026 15:13 UTC (Sat)
 byjpeisach(subscriber, #181966)
 [Link] (2 responses)What if a package maintainer feels that they wish to reject a PR because the description is written by a LLM? Are they allowed to do that?### Maintainer opinions?Posted Aug 29, 2026 15:28 UTC (Sat)
 byhlieberman(subscriber, #123867)
 [Link]Speaking only as a DD, but not officially on behalf of the project:As long as you are being respectful and following the other requirements of the Code of Conduct, the only group with the ability to force a maintainer to accept a patch would be the Technical Committee. That's a high bar, and generally the only things that go in front of them are issues around major packages or mass-filings, or when two maintainers heatedly disagree.As a maintainer of a package, I am responsible for what goes into that package. Another maintainer can disagree with my decisions, but absent a ruling of the TC, they can't override my decision*.*: Technically, a developer _could_ just ship an update with their change, but doing so over the objections of the maintainer would almost certainly end up getting you in a world of trouble.### Maintainer opinions?Posted Aug 29, 2026 15:30 UTC (Sat)
 bycen(subscriber, #170575)
 [Link]AFAIK a Debian maintainer generally has broad discretion over which patches to accept for any reason, including AI. But they cannot use that discretion to refuse to implement a binding Debian project/Technical Committee decision or an applicable Debian Policy requirement.### MaintainabilityPosted Aug 29, 2026 15:40 UTC (Sat)
 byakselmo(subscriber, #174307)
 [Link] (5 responses)I have a feeling this will cause maintenance and stability issues further down the line, as people rarely are "responsible" withthese tools. I and my servers hope I am wrong.### MaintainabilityPosted Aug 29, 2026 16:41 UTC (Sat)
 bydilinger(subscriber, #2867)
 [Link] (4 responses)It really was the worst possible option. As Bunk said (https://lists.debian.org/debian-vote/2026/08/msg00367.html), lack of disclosure is by no means responsible. The result leaves it at the status quo, eg the current wild west. It feels to me like the project as a whole voted to kick the can down the road a few years (and I've seen a few people who voted for the option say as much).### MaintainabilityPosted Aug 29, 2026 16:54 UTC (Sat)
 byMarcB(subscriber, #101804)
 [Link] (3 responses)What does it really improve? People can lie, and the possibility alone that someone might have been lying causes tensions.Ironically, demanding disclosure of AI usage would only work without problems in an environment, where it is absolutely acceptable to use AI.### MaintainabilityPosted Aug 29, 2026 17:07 UTC (Sat)
 bydilinger(subscriber, #2867)
 [Link] (1 responses)> What does it really improve? People can lie, and the possibility alone that someone might have been lying causes tensions.Currently people can lie about whether they used AI, and there's no consequence. Sure, there might be personal consequences - a specific maintainer, after discovering such an incident, might say, "never submit a PR to me again". The person who lied, however, can just move onto another package/maintainer/project.Otoh, codifying a "you must disclose" rule allows for more project-wide consequences.> Ironically, demanding disclosure of AI usage would only work without problems in an environment, where it is absolutely acceptable to use AI.Sure, that was option 2. Well, except option 2 used the wording "should" instead of "must", but oh well.Option 3 did use the word "must", but it was also a vote to reject as far as practical, so that's not really an environment where it's acceptable to use AI.### MaintainabilityPosted Aug 29, 2026 18:13 UTC (Sat)
 byMarcB(subscriber, #101804)
 [Link]> Otoh, codifying a "you must disclose" rule allows for more project-wide consequences.That is precisely the problem. Those consequences might very well be quasi-witch-hunts/inquisitions with huge chilling effects on *any* potential contributor (even those not using AI). It could easily have created an atmosphere of pervasive distrust and people forming an "AI police" (maybe even outside the project; imagine comments in the bug tracker).Having gone through some of the public discussions about this, I am absolutely certain this would have happened.But don't get me wrong: I would absolutely prefer a declaration of AI usage - given an appropriate environment.### MaintainabilityPosted Aug 29, 2026 17:28 UTC (Sat)
 byoridb(subscriber, #85941)
 [Link]> What does it really improve? People can lie, and the possibility alone that someone might have been lying causes tensions.As I keep saying, because people will steal anyways, we should legalize robbery.### what I miss is anti-agent-harassment provisionsPosted Aug 29, 2026 16:22 UTC (Sat)
 byhmh(subscriber, #3838)
 [Link]My biggest issue with AI is fire-and-forget agents harassing or otherwise demanding time from humans (maintainers) in the mailing lists or bug trackers. Even single post by agents is already bad because the cheaper it is (in human time and effort) to push slop, the worse for maintainers that are in the receiving end.If that starts to get even worse (in Debian), I expect something forbidding that outright to make it to the CoC or terms of service, this GR outcome would not contradict that.### How to satisfy legal compliance?Posted Aug 29, 2026 16:35 UTC (Sat)
 bygray_-_wolf(subscriber, #131074)
 [Link] (1 responses)> The Debian Project nevertheless expects that all contributions submitted to Debian, regardless of how and with which tools they were produced, satisfy the same standards of quality, correctness, maintainability, and legal compliance.So I get all of these except the last one. When Claude gives me back a block of code, *how* can I ensure it is legally compliant? Either Debian decided that LLM-generated patches *cannot have* legal issues or they do not allow non-trivial generated patches, but did not want to say it? Which is it?### How to satisfy legal compliance?Posted Aug 29, 2026 18:28 UTC (Sat)
 byclint(subscriber, #7076)
 [Link]How can you ensure that a block of code given to you by a human is "legally compliant"? The answer is that you cannot.### does not override project's choicesPosted Aug 29, 2026 19:06 UTC (Sat)
 byatai(subscriber, #10977)
 [Link] (2 responses)This Debian decision does not override the choices of each project/package packaged in Debian, right?For example, GNOME does not allow AI written code. The GNOME guideline still applies in Debian### does not override project's choicesPosted Aug 29, 2026 19:23 UTC (Sat)
 bysalimma(subscriber, #34460)
 [Link]It doesn’t affect upstream projects.Though I should note that while some individual GNOME projects have adopted no-LLM policies, the wider project itself has not### does not override project's choicesPosted Aug 29, 2026 19:25 UTC (Sat)
 byintelfx(subscriber, #130118)
 [Link]This Debian decision does not override the choices of each project/package packaged in Debian, right?For example, GNOME does not allow AI written code. The GNOME guideline still applies in DebianThe GNOME guideline applies to the GNOME upstream. There's a distinction: GNOME does not have a power to"not allow"AI-written code, it only has a power to"not accept"it.If GNOME does not allow AI written code (I didn't look, so I'm just taking your statement at face value), that does not and cannot prohibit Debian Developers to e.g. apply AI-authored patches to GNOME code downstream.
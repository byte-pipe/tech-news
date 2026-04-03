---
title: Belgium is unsafe for CVD | Floort.net
url: https://floort.net/posts/belgium-unsafe-for-cvd/
site_name: lobsters
fetched_at: '2025-07-06T23:06:27.512999'
original_url: https://floort.net/posts/belgium-unsafe-for-cvd/
author: Floor Terra
date: '2025-07-06'
published_date: '2025-07-06T00:44:00+02:00'
description: This post is about the reason I will probably never try to warn any organisation in Belgium about any vulnerability again. Recently I have been dealing with an attempt at coordinated vulnerability disclosure (CVD) with an organisation in Belgium. This post is not about that, because I’m not allowed to write about it. This post explains why I believe Belgium is unsafe for people trying to do CVD. I believe it’s important to warn others so that they know what to expect and can decide for themselves.
tags: law, security
---

This post is about the reason I will probably never try to warn any organisation in Belgium about any vulnerability again.
Recently I have been dealing with an attempt at coordinated vulnerability disclosure (CVD) with an organisation in Belgium.
This post is not about that, because I’m not allowed to write about it. This post explains why I believe Belgium is unsafe
for people trying to do CVD. I believe it’s important to warn others so that they know what to expect and can decide for themselves.

Because I can’t cite my specific example, let’s start with a generic explanation about CVD. The purpose of CVD is to publish
about vulnerabilities (The “V”) in systems so that others can learn from it it with the assumption that sharing this knowledge is crucial
for society to improve security in general. That publication is the “D” or “Disclosure” of CVD. There are many ways in which
publication can help. For example, when the vulnerability is of a new type (it rarely is) it helps other to learn how to
find similar issues in other systems, how to design detections or preventative measures to safeguard against exploitation, etc..
If it is in a vulnerability in some common infrastructure, others who depend on that infrastructure need to be aware in order
to take measures to protect their systems. If it is a vulnerability at a single organisation, customers might want to know
that their data has not been safe, especially when the organisation demonstrates that it doesn’t improve its security over time.
Or others might simply use the reminder to check for similar vulnerabilities in their own system. Improving security is not
allways about hard technical knowledge, sometimes an example is enough to make others pay more attention.
However, just bluntly publishing all information about all discovered vulnerabilities immediately is generally not considered
to be a good idea. That’s where the Coordination (The “C”) comes in. Over times, the security industry has been developing
practices and standards that are meant to help coordinate between the people who discover vulnerabilities and those who
are responsible for systems that are vulnerable. The goal is that those who need it are supposed to get a reasonable
warning before publication and the opportunity to take measures to prevent exploitation of the vulnerability when
the discovery gets published. There is is even an official standard for it:ISO/IEC/TR 5895:2022orNEN-EN-ISO/IEC 29147:2020 enThere are limits to that coordination however: if a single organisation refuses to take security measures, withholding
publication can harm everyone else. The consensus with many experts, including at the ISO, NEN,Dutch Gouvernmentand theU.S. Governmentseems to be that
public disclosure should generally be the goal.

# Belgium is different#

Recently I discovered a vulnerability in a system from a Belgium government organisation. This was completely
by accident. I was not trying to find a vulnerability. It took me a couple of minutes to take a single screenshot that
contains all context needed to reproduce the vulnerability and send a private message on X to someone I know that works
at the affected organisation. I got a positive response within one minute and within an hour or so the entire system
was pulled offline. So far so good.

Then I remembered Belgium has a law that places requirements on people reporting vulnerabilities. I want to
do the right thing so I decide to check out what those requirements are. You might think it’s not smart to take action
before checking the rules. Fair point, but I’ll point out later why that would not have mattered or would probably
have made me miss a legally required deadline. I was lucky to be somewhat aware of this Belgium
law in the first place otherwise I would have bluntly violated the legal requirements. I started reading theexplanationthe
Centre For Cybersecurity Belgium had published about these requirements. The way I read the explanation was
as follows:

1. After discovering the vulnerability I had to file a simple report at the CCB without undue delay and within 24 hours at most. This report has to include my actual name, document number of my official government identity document, email and phone number.
2. Within 72 hours I have to file a full report detailing a detailed description of the vulnerability, documentation of the tools I used, configuration details, logs of my activity, etc..
3. I can never reveal any information about the vulnerability publicly without permission from the CCB.
4. Some other terms that are quite reasonable that I won’t discuss here.

As I gather from the underlying law I might run the risk of criminal prosecution and punitive damages if I break these
rules. The first thing I do is call the CCB to ask if these rules really apply to me. The CCB does not really have
a phone number intended for citizens (although I’m not even a Belgium citizen) but this is kind of an emergency.
I don’t want to face criminal prosecution and decide to explore other options in their phone menu. Luckily they
call me back and answer some of my questions. My interpretation is correct according to the CCB: it applies to me even
if I am not a citizen of Belgium and don’t live in Belgium and the legal requirements are triggered by me becoming aware
of the vulnerability, not by me reporting the vulnerability. The CCB refuse to answer what might happen if I don’t
comply. Fuck! The 24 hour deadline has almost passed, so I rush to find the form, fill it in. No time to figure
out where I left my PGP keys and encrypt the mail like CCB asks. I manage to send in the form somewhere around
half an hour after the deadline. I don’t know exactly because I only became aware that the CCB asks me to maintain
logs after I discovered and reported the vulnerability. And I’m not a madman who keeps logs of all of my activities
all the time on the off chance I might accidentally encounter vulnerabilities in Belgium. No moral judgement for those
who do, but I have better things to do. How the fuck does the CCB think non-Belgian citizens are supposed to
be aware of these rules and comply with these brutal deadlines?
I tried my best, but failed already. Half an hour shouldn’t be a major issue, but CCB refused to answer what might
happen if I don’t comply. And on principle I want to do my best and comply with the law. So my stress level is
already quite high.

# Secrecy#

Like I explained earlier CVD is quite important to me and the secrecy obligation is something I have moral objections
to. Don’t get me wrong: It’s not my intention to publish information to damage the specific organisation. On the
contrary: I like them, their work and want to protect them and the data they process. However: the system is already
taken offline. Information about the vulnerability should not be able to damage anyone. So I include with my report
the request to relieve me of my secrecy requirements. The response from CCB is relatively swift (3 days) and a clear no.

From a freedom of information request filed at CCB I knew the CCB has a secret policy for deciding when to give
it’s blessing to end the secrecy requirements. Now I had a refusal, with only a superficial explanation that I’m
probably not allowed to repeat here. I understand that CCB might need some time. But now I have a decision from
a government organisation with legal effect. I don’t know if I can just request permission again, against what
policy my request has been and will be tested, if the decision becomes irreversible unless I file an appeal or
how to file an appeal. I don’t know a thing about Belgium administrative law and I’m discovering it’s a lot
more messy than Dutch administrative law. I don’t know what my rights are here, what procedures I can follow
or even if I’m allowed to seek legal legal advice without risking violating my secrecy requirements. And CCB
refuses to answer my questions about this. Meanwhile my stress levels are rising. I’m facing lifelong limitations
for just trying to help and I don’t know what my rights are.

The CCB does give one option: If the affected organisation gives me permission that’s good enough for the CCB.
So I ask them. A couple of weeks later I got a response: They give me permission to publicly communicate in the
abstract sense that the concept of “Business Logic Errors”as defined by the CWEexists. I don’t get permission to communicate who has been affected by this type of vulnerability.

I’m shocked. Did I need permission to be allowed to tell people that business logic errors exist?!
The following exchange where I try to clarify more details (left out because I’m not allowed to write about it)
ends with the message that they have already done more than required and can withdraw even the one
concession and hold me to lifelong secrecy requirements:

REDACTED heeft in deze meer gedaan dan nodig. We hadden ook de wet, die deze levenslange geheimhouding oplegt, op de letter kunnen volgen en u geen toegeving kunnen doen. Wij houden ons ook aan deze ene toegeving en indien nodig trekken we ze in.

Not only am I not informed of my rights, I have received a threat.
And I’m not convinced that the person making the threat is wrong, legally speaking.
As far as I’m aware they can hold me to an eternal secrecy requirement, based on secret policy and no process
to fight back if I disagree. Just because I noticed a vulnerability.

# Multi stakeholder CVD#

Now imagine you are doing vulnerability research and you find a thousand systems with a specific vulnerability.
One of these systems is owned by an organisation in Belgium. You don’t know in advance who the systems belong to.
What do you need to do according to the CCB:

1. Within 24 hours of discovering the one Belgian vulnerable system in the set, you have to figure out who the owner is, that the owner is located in Belgium, be aware of these legal requirements and file a report at the CCB. Ammended by a full report within 72 hours. Regardless of weekends, holidays, lack of awareness of laws in foreign nations, complexity in identifying owners of systems you find online or the complexity of analysing the vulnerability itself.
2. Withhold informing the other 999 owners of systems until the CCB gives you permission to do so. Based on practical experience and the secrecy of the decision process there is a very real possibility that you will never be allowed to warn the others. And CCB doesn’t even ask about others that might be affected.

Any multi-stakeholder CVD process when even a single organisation in Belgium is involved is practically impossible.
Strictly speaking you can’t work around this by just not informing the Belgian organisations, because the requirements
are triggered by the discovery not the report.

# What to do?#

I won’t give legal advice and everyone needs to weigh their own risks, but this is what I will do in the future.
When I see a hint that a system with a Belgian owner might be vulnerable I drop it. Don’t verify any suspicion
about the vulnerability, delete the data that I might have and don’t tell anyone.
That hurts, because the owners of the systems and the people whose data is on the system don’t deserve a breach.
But if you as a country choose to treat the people who are trying to help like this I don’t want to know
what might happen if there is a conflict and these laws are enforced.

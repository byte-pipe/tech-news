---
title: We should all be using dependency cooldowns
url: https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns
site_name: hackernews
fetched_at: '2025-11-22T11:06:29.570952'
original_url: https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns
author: todsacerdoti
date: '2025-11-22'
---

# ENOSUCHBLOG

## Programming, philosophy, pedaling.

* Home
* Tags
* Series
* Favorites
* Archive
* Main Site
* TILs

# We should all be using dependency cooldowns

## Nov 21, 2025Tags:oss,security

TL;DR: Dependency cooldowns are a free, easy, andincredibly effectiveway to mitigate thelarge majorityof open source supply chain attacks.
More individual projects should apply cooldowns (via tools like Dependabot
and Renovate) to their dependencies, and packaging ecosystems should invest
in first-class support for cooldowns directly in their package managers.

“Supply chain security” is a serious problem. It’s alsoseriously overhyped,
in part because dozens of vendors have a vested financial interest in
convincing your that theirframingof the underlying problem1is (1)
correct, and (2) worth your money.

What’s consternating about this is that most open source supply chain
attacks have the same basic structure:

1. An attacker compromises a popular open source project, typically via
a stolen credential or CI/CD vulnerabilty (such as“pwn requests”in
GitHub Actions).
2. The attacker introduces a malicious change to the project and uploads
it somewhere that will havemaximum effect(PyPI, npm, GitHub releases,
&c., depending on the target).At this point, theclock has started, as the attacker has moved
 into the public.
3. Users pick up the compromised version of the project via automatic
dependency updates or a lack of dependency pinning.
4. Meanwhile, the aforementioned vendors are scanning public indices
as well as customer repositories for signs of compromise, and
provide alerts upstream (e.g. to PyPI).Notably, vendors areincentivizedto report quickly and loudly upstream,
 as this increases the perceived value of their services in a crowded
 field.
5. Upstreams (PyPI, npm, &c.) remove or disable the compromised package
version(s).
6. End-user remediation begins.

The key thing to observe is that the gap between (1) and (2) can be very large2(weeks or months), while the gap between (2) and (5) istypically very small:
hours or days. This means that, once the attacker has moved into the actual
exploitation phase, theirwindow of opportunityto cause damage is pretty limited.

We can see this with numerous prominent supply chain attacks over the last 18 months3:

Attack

Approx. Window of Opportunity

References

xz-utils

≈ 5 weeks
4

Source

Ultralytics (phase 1)

12 hours

Source

Ultralytics (phase 2)

1 hour

Source

tj-actions

3 days

Source

chalk

< 12 hours

Source

Nx

4 hours

Source

rspack

1 hour

Source

num2words

< 12 hours

Source

Kong Ingress Controller

≈ 10 days

Source

web3.js

5 hours

Source

(Each of these attacks has significant downstream effect, of course, but onlywithintheir window of opportunity. Subsequent compromises from each, likeShai-Hulud, representnewwindows of opportunity where the attackers regrouped
and pivoted onto thenextset of compromised credentials.)

My takeaway from this: some windows of opportunity are bigger, but themajorityof them are under a week long. Consequently, ordinary developers canavoid
the bulkof these types of attacks by institutingcooldownson their dependencies.

## Cooldowns

A “cooldown” is exactly what it sounds like: a window of time between when a dependency
is published and when it’s considered suitable for use. The dependency is public during
this window, meaning that “supply chain security” vendors can work their magic
while the rest of us wait any problems out.

Ilovecooldowns for several reasons:

* They’re empirically effective, per above. They won’t stopallattackers,
but theydostymie the majority of high-visibiity, mass-impact supply chain
attacks that have become more common.
* They’reincrediblyeasy to implement. Moreover, they’reliterally freeto implement in most cases: most people can useDependabot’s functionality,Renovate’s functionality, or the functionality build directly into their
package manager5.This is how simple it is in Dependabot:1
2
3
4
5
6
7
8
9version:2# update once a week, with a 7-day cooldown-package-ecosystem:github-actionsdirectory:/schedule:interval:weeklycooldown:default-days:7(Rinse and repeat for other ecosystems as needed.)
* Cooldownsenforce positive behaviorfrom supply chain security vendors:
vendors are still incentivized to discover and report attacks quickly,
but arenotas incentivized to emit volumes of blogspam about “critical”
attacks on largely underfunded open source ecosystems.

## Concluding / assorted thoughts

In the very small sample set above, 8/10 attacks had windows of opportunity
of less than a week. Setting a cooldown of 7 days would have prevented
the vast majority of these attacks from reaching end users (and causing
knock-on attacks, which several of these were). Increasing the cooldown to 14
days would have prevented all but 1 of these attacks6.

Cooldowns are, obviously,not a panacea: some attackerswillevade detection,
and delaying the inclusion of potentially malicious dependencies by a week
(or two) does not fundamentally alter the fact that supply chain security is asocial trustproblem, not a purely technical one. Still, an 80-90% reduction
in exposure through a technique that is free and easy seems hard to beat.

Related to the above, it’s unfortunate that cooldowns aren’t bakeddirectlyinto more packaging ecosystems: Dependabot and Renovate are great, buteven betterwould be if the package manager itself (as the source of ground
truth) could enforce cooldowns directly (including of dependencies not
introduced or bumped through automated flows).

1. The problem being, succinctly: modern software stacks are complex and opaque,
 with little to no difference in privilege between first-party code and third-party
 dependencies.↩
2. In part because of the prevalence of long-lived, overscoped credentials. Long-lived
 credentials let attackers operate on their own (comfortable) timelines; this is whyTrusted Publishingis such a useful (but not wholly sufficient)
 technique for reducing the attacker’sattack staging window.↩
3. Filippo Valsorda has an excellent compilation of recent supply
 chain compromiseshere.↩
4. The xz-utils attack is a significant outlier, both in its scope and the length
 of its window of opportunity. In this case, I’ve measured from the attacker’s
 first backdoored release (v5.6.0, 2024-02-24) to the time of rollback within
 Debian (2024-03-28).↩
5. For example, pnpm’sminimumReleaseAge.
 uv also hasexclude-newer,
 although this specifies an absolute cutoff rather than a rolling cooldown.↩
6. Notably, the only attack that would have stymied a 14-day cooldown is xz-utils,
 which isalsothe most technically, logistically, and socially advanced of all of the
 attacks.↩

Previously

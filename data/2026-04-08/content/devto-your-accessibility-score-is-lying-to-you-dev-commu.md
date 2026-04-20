---
title: Your accessibility score is lying to you - DEV Community
url: https://dev.to/chris_devto/your-accessibility-score-is-lying-to-you-5fh2
site_name: devto
content_file: devto-your-accessibility-score-is-lying-to-you-dev-commu
fetched_at: '2026-04-08T19:33:18.236340'
original_url: https://dev.to/chris_devto/your-accessibility-score-is-lying-to-you-5fh2
author: Chris
date: '2026-04-07'
description: Automated accessibility testing tools, such as axe-core by Deque, WAVE, Lighthouse are bit like a... Tagged with a11y, frontend, automation, lighthouse.
tags: '#a11y, #frontend, #automation, #lighthouse'
---

Automated accessibility testing tools, such asaxe-core by Deque,WAVE,Lighthouseare bit like a spellcheck for web accessibility. They are really useful for identifying and resolving many common accessibility issues quickly.

There are a whole range of tools that provide similar services, a way to detect some of the most common accessibility issues across a page.

### The problem with automated accessibility scores

The problem is the way their reporting gives a score of out 100%. It gives the impression to the uneducated that an automated scoring once it reaches 80 or 90% is pretty good. However, these scores can be deeply misleading.

Automated tests typically detect only 20% to 40% of real accessibility issues. What about with AI I hear you scream? I'm sure that will increase but for now let's pause that for this post. Like a spell-checker that flags spelling mistakes but cannot understand meaning or context, it can't tell you if the book makes sense. These tools identify technical errors but missmany barriersthat only humans can detect.

Deque’s own marketing materials claim they can detectup to 57% of issues, although at the time of writing I find it hard to review how they're arrived at this. Which websites? How was this tested etc? Are there user testing videos?

### How this scoring misleads those in power

I was sat in a presentation recently, cringing, where a Product Owner and Lead Designer proudly assert their automated score of 70% suggesting their"almost there"when they are so far away from the reality...

Suddenly there was anotherepicpiece of work to educate certain stakeholders about this misleading nature of this score.

A site scoring 70% might appear nearly compliant but if we accept the marketing claims of 57% then a “70%” score equates to roughly 39.9% of actual accessibility compliance. This discrepancy leads people to believe that accessibility work is largely complete, when in fact the majority of blockers remain unresolved.

Automated score (%)

Approx. % of actual issues detected (57%)

30

17.1

40

22.8

50

28.5

60

34.2

70

39.9

80

45.6

90

51.3

100

57

### The wider consequences

When teams focus on improving their automated score, accessibility becomes a checkbox exercise rather than a genuine effort to create accessible experiences. Developers start“fixing for the tool”instead of fixing for disabled users. The whole goal is to simply get the tooling to give a green light.

This has several negative effects:

* Teams make superficial somewhat performative, changes to satisfy tooling rather unblock disabled people.
* Businesses suddenly think they are compliant when they are not, giving them a sense of false confidence.
* Leadership tend to use these scores to justify reducing investment in accessibility.
* Most importantly, disabled users remain unable to complete tasks such as checking out, navigating menus, or using interactive features.

### Why automated tools still matter

Don't get me wrong, automated accessibility tools should not be dismissed, They are excellent for identifying obvious issues and ensuring consistency across large codebases. However, they are only a starting point, not a comprehensive solution. They are not a replacement for testing with real disabled users.

The things below can't be skipped

* Manual testing with assistive technologies
* User testing with people with disabilities

Without these, even a“perfect”automated score is somewhat meaningless.

### Time to get uncomfortable

The uncomfortable truth is that, in many organisations Accessibility isn’t treated as a commitment to unblocking people, it’s a risk management piece. For some leaders, it’s not about people, it’s about protection.

They invest in automated tools, chase high Accessibility scores because if they’re ever challenged legally, they can point to those numbers as“evidence”of compliance, hoping no one looks too closely.

Sometimes the companies selling these Accessibility testing tools also have a vested interest in keeping those scores high. Their products are compared against other platforms, and a higher“score”looks better in sales demos. They get their subscription fees whether or not disabled people can actually use the product or service.

### Update the metrics

I would love for these tools to update their scoring metrics.

Change their metrics, imagine if axe-core or Lighthouse had a maximum score of 57%. There was no way to get to 100%, that would shift the understanding instantly.

Misunderstanding these scores can give an organisations a dangerous illusion of compliance and may not actually improve the experience for disabled people.

### Further reading

* A false sense of accessibility: What automated testing tools are missing #id24 2025
* Accessible.org: Accessibility Scans Reliably Flag 13% of WCAG Criteria
* LinkedIn: Automated Accessibility Test Tools Find Even Less than 30%–50%
* The Problem with Automated Website Accessibility Testing Tools

Cover image alt[Two large circular graphics are shown side by side on a light background. The left circle is green with “100%” inside and labelled “Automated accessibility score.” The right circle is orange with “57%” inside and labelled “Actual issues detected.” Below the circles, a caption reads book “Automated testing tools only catch a fraction of real accessibility issues.”]

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

---
title: '"Technical Debt Will Bite Us in the Ass": How to Make Non-Technical Stakeholders Actually Care - DEV Community'
url: https://dev.to/tlorent/technical-debt-will-bite-us-in-the-ass-how-to-make-non-technical-stakeholders-actually-care-2oef
site_name: devto
fetched_at: '2025-11-18T11:07:10.121773'
original_url: https://dev.to/tlorent/technical-debt-will-bite-us-in-the-ass-how-to-make-non-technical-stakeholders-actually-care-2oef
author: Tim Lorent
date: '2025-11-14'
description: '"We need to refactor this code." Blank stares. "The architecture is getting messy." More blank... Tagged with webdev, career, productivity, learning.'
tags: '#webdev, #career, #productivity, #learning'
---

"We need to refactor this code."

Blank stares.

"The architecture is getting messy."

More blank stares. (Even a hint of 'leave me alone, we have features to ship.')

"If we don't address this technical debt now, it'll slow us down later."

Polite nods. Then: "Can we just ship this feature first?"

I've had this conversation more times than I can count. And for years, I blamed the product managers.

They don't get it. They only care about features. They're ignoring the foundation while demanding we build another floor.

Then I realized: they weren't the problem. My communication was.

## The Translation Gap

Here's what I was saying: "We need to refactor this code because the architecture is getting messy and technical debt is accumulating."

Here's what they heard: "I want to spend two weeks making things prettier instead of building what customers asked for."

We were speaking different languages. I was talking about code quality. They were thinking about customer value, revenue, and roadmap commitments.

Neither of us was wrong. We just weren't connecting.

## The Moment Everything Changed

I was in yet another meeting trying to explain why we needed to pause feature work to address technical debt.

The product manager's eyes were glazing over. I could see her mentally calculating how to politely end this conversation.

So I stopped mid-sentence and tried something different.

"Imagine you just cut half your finger off. You could properly clean it and put on a bandage, or you could just ignore it. What happens if you keep ignoring half cut off fingers?"

She looked at me like I'd lost my mind. But then she got it.

"They get infected."

"Exactly. And eventually, you can't use that hand at all. That's what technical debt does to our codebase."

Suddenly, we weren't debating code architecture. We were discussing wounds that fester, infections that spread, and hands that stop working.

Technical debt became something she could visualize. And visualization creates urgency.

## Why Technical Jargon Fails

* When we say "refactoring," non-technical stakeholders hear "optional polish."
* When we say "technical debt," they hear "developers want perfect code."
* When we say "architecture," they hear "abstract concerns that don't affect users."

We're not wrong to use these terms with each other. But with stakeholders who measure success in features shipped, revenue generated, and customer satisfaction scores, we need a different vocabulary.

Not because they're less intelligent. Because they're optimizing for different outcomes.

A product manager isn't ignoring technical debt out of malice.

They're focused on:

* Delivering promised features to customers
* Meeting revenue targets
* Staying ahead of competitors
* Keeping stakeholders happy

And "we need to refactor" doesn't map to any of those goals. So we need to show them how it does.

## Building the Bridge

The change isn't about dumbing things down, rather it's about finding shared language.

Here are the metaphors that have worked for me:

The Band-Aid on an Infected Wound

Every quick fix is a band-aid over a cut we didn't properly clean. Every shortcut is like painting over a crack in the wall instead of fixing the foundation.

At first, it looks fine: the wall looks painted, the cut is covered.

But band-aids fall off. Paint peels. And what's underneath is worse than when you started.

Why it works: Everyone understands infections get worse when ignored. Nobody argues with "this will get infected."

The Cracked FoundationYou can keep building floors on a cracked foundation. And for a while, it'll hold. But every new floor adds pressure. The cracks spread. And one day, the whole thing collapses—right when you need it most.

Why it works: It connects technical decisions to risk management, something every business leader thinks about.

## Speaking Their Language

Metaphors help, but you know what really works? Translating consequences into business language.

Instead of: "This code is hard to maintain."

Try: "Every new feature in this area takes 3x longer because of how it's structured. That's 20 extra hours per sprint we could be spending on new features."

Instead of: "We have technical debt here."

Try: "This is costing us $15,000 in developer time every quarter. If we invest two weeks now, we'll save that every quarter going forward."

Instead of: "The architecture is messy."

Try: "Our bug rate in this module is 4x higher than elsewhere.

Customers are reporting issues every week. We can fix that, but it requires addressing the underlying structure."

Hours lost. Money wasted. Bugs multiplying. Velocity decreasing.

These are metrics stakeholders understand. These create urgency.

## The Conversation That Actually Works

Here's the framework I use now:

1. Acknowledge their priorities: "I know we need to ship Feature X by end of quarter. That's important."

Don't start with opposition. Start with alignment.

1. Connect technical debt to their goals: "The problem is, the area where we need to build Feature X is really unstable. We're seeing bugs there every week, and each change takes twice as long as it should."

Show how the technical problem affects their goals, not yours.

1. Quantify the cost: "Right now, we're spending about 10 hours every sprint just working around the issues in that module. That's half a developer's time."

Make the invisible visible. Give them numbers.

1. Propose the investment and ROI: "If we spend one week cleaning this up, we'll cut that time in half. Plus, Feature X will be faster and more stable to build."

Frame it as an investment with clear returns, not a cost.

1. Give them the choice: "We can either address it now and move faster after, or keep working around it and accept that every feature in this area will take longer. What makes more sense given our priorities?"

Empower them to make the decision with full information.

## 🛠️ How to Apply This

Before the next technical debt conversation:

* Identify the business impact. What's the cost in time, money, or risk? If you can't articulate this, you're not ready for the conversation.
* Choose your metaphor. What will resonate with this specific person? Financial types respond to debt and interest. Product types respond to velocity and risk.
* Quantify everything you can. Hours, dollars, bug counts, velocity changes. Numbers create urgency.
* Prepare the ROI. What's the investment? What's the return? How long until it pays off?

During the conversation:

* Start with their goals, not yours. "I know shipping Feature X is critical..."
* Connect technical to business. Show how the technical problem blocks their goals.
* Give options, not ultimatums. "We can address it now and move faster after, or keep working around it. What makes sense given our priorities?"
* Be honest about trade-offs. Every choice has costs. Acknowledge them.

After you get buy-in:

* Deliver what you promised. If you said it would take one week, take one week. Trust is built through follow-through.
* Measure the impact. Did velocity improve? Did bugs decrease? Share these wins.
* Reinforce the connection. "Remember when we cleaned up Module X? That's why we shipped Feature Y so fast."

## The Deeper Skill

Here's what I wish someone had told me earlier: Cross-discipline communication is a core engineering skill.

Not a soft skill. Not a nice-to-have. A core skill.

The best engineers I know aren't just technically excellent. They can translate technical concerns into business value, design implications, or user impact.

They understand that:

* Backend engineers need to talk to frontend in terms of API contracts and data flow
* Frontend engineers need to talk to designers in terms of interaction patterns and constraints
* Everyone needs to talk to product in terms of customer value and business outcomes

Finding the bridge between disciplines isn't about compromising your expertise. It's about making your expertise relevant to people who optimize for different outcomes.

## 🤔 Questions to Reflect On

When's the last time you tried to explain a technical problem and got blank stares? What language were you using?

What metaphors resonate with your specific stakeholders?

Are you quantifying the business impact of technical decisions, or just hoping people trust you?

How often do you start technical debt conversations with stakeholder goals vs. engineering concerns?

## The Bottom Line

Technical debt will bite us in the ass. But saying that to stakeholders won't create urgency.

Band-aids on infected wounds will. Credit card interest will. Cracked foundations will.

Every quick fix is a band-aid over a cut we didn't properly clean.

Every shortcut is like painting over a crack in the wall instead of fixing the foundation.

At first, it looks fine. But band-aids fall off. Paint peels. And what's underneath is worse than when you started.

Your job isn't just to identify technical debt. It's to make non-technical people care about it as much as you do.

And that starts with speaking their language.

Photo bycharlesdeluvioonUnsplash

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

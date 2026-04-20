---
title: 'The Economics of Software Teams: Why Most Engineering Organizations Are Flying Blind - Viktor Cessan'
url: https://www.viktorcessan.com/the-economics-of-software-teams/
site_name: hackernews_api
content_file: hackernews_api-the-economics-of-software-teams-why-most-engineeri
fetched_at: '2026-04-13T20:05:28.894956'
original_url: https://www.viktorcessan.com/the-economics-of-software-teams/
author: kiyanwang
date: '2026-04-13'
published_date: '2026-03-17'
description: A breakdown of what software development teams actually cost, what they need to generate to be financially viable, and why most organizations have no visibility into either number.
tags:
- hackernews
- trending
---

← Back to Blog

# The Economics of Software Teams: Why Most Organizations Are Flying Blind

This post works through the financial logic of software teams, from what a team of eight engineers actually costs per month to what it needs to generate to be economically viable. It also examines why most teams have no visibility into either number, how that condition was built over two decades, and what the arrival of LLMs now means for organizations that have been treating large engineering headcount as an asset.

Software development is one of the most capital-intensive activities a modern company undertakes, and it is also one of the least understood from a financial perspective. The people making daily decisions about what to build, what to delay, and what to abandon are rarely given the financial context to understand what those decisions actually cost. This is not a coincidence. It is a structural condition that most organizations have maintained, quietly and consistently, for roughly two decades.

## What a Team Actually Costs

A software engineer in Western Europe costs somewhere between €120,000 and €150,000 per year when you account for salary, social fees, pension contributions, equipment, social activities, management overhead, and office space. Call it €130,000 as a reasonable middle estimate. A team of eight engineers therefore costs approximately €1,040,000 per year, or €87,000 per month, or roughly €4,000 for every working day.

Team size (engineers)

8

Cost per engineer per year (€)

€130,000

Annual cost

€1,040,000

Monthly cost

€86,667

Daily cost

€4,000

Most engineers do not know this number. Many of their managers do not either. And in the organizations where someone does know it, the number rarely makes its way into the conversations where prioritization decisions are actually made.

This matters because every decision a team makes carries an implicit cost that compounds over time. Choosing to spend three weeks on a feature that serves 2% of users is a €60,000 decision. Delaying an operational improvement for a quarter is a decision with a calculable daily price tag. Rebuilding a platform because the current one feels embarrassing, rather than because customers are leaving, is a capital allocation choice that would look very different if the people making it were spending their own money.

## The Internal Platform Team: What Break-Even Actually Requires

Consider a team of eight engineers whose mission is to build and maintain an internal developer platform serving one hundred other engineers. This is a common organizational structure, and it is one where the financial logic is rarely examined carefully.

The team costs €87,000 per month. To justify that cost, the platform they build needs to generate at least €87,000 per month in value for the engineers who use it. The most direct way to measure that value is through time saved, since the platform’s purpose is to make other engineers more productive.

At a cost of €130,000 per year, one engineer costs approximately €10,800 per month, or around €65 per working hour. For the platform team to break even, their platform needs to save the hundred engineers they serve a combined total of 1,340 hours per month. That is 13.4 hours per engineer per month, or roughly three hours per week per person.

Three hours per week is achievable. A well-built platform that eliminates manual deployment steps, reduces environment setup time, or removes the need for repetitive configuration work can easily clear that bar. Time saved is the most direct measure for a platform team, though value can also come from reducing outages, which carries a direct revenue impact of its own. But the question worth asking is whether anyone on that team knows this number, tracks it, or uses it to decide what to build next. In most organizations, the answer is no. The team has a roadmap driven by engineering preferences, stakeholder requests, and quarterly planning cycles, and the financial logic underlying their existence is left unexamined.

And break-even is not actually the right bar.Leah Tharin has written a sharp breakdown of the mathematics of this: a team with a 50% initiative success rate, which is already optimistic, needs its wins to cover its losses too. Leah’s calculation is growth-oriented, but even for non-growth organizations, the same investment thesis holds. Even a two-times return is not sufficient. Capital sitting in a bank carries no operational risk, no coordination costs, and no ongoing maintenance obligations. The systems a team builds will outlive the team itself, and the cost of owning, maintaining, and eventually replacing those systems is almost always larger than anticipated. The return has to cover not just the team’s current cost, but the long tail of what they leave behind.

That pushes the realistic threshold for financial viability to somewhere between three and five times annual cost. For an €87,000 per month team, that means generating between €260,000 and €435,000 in monthly value. The three hours per week calculation gets you to break-even. To clear the realistic financial bar, the platform needs to be genuinely transformative for the engineers using it, and the team needs to be ruthless about working on the highest-value problems rather than the most interesting ones.

Team size (engineers)

8

Cost per engineer per year (€)

€130,000

Monthly cost

€86,667

Minimum viable (3x) per month

€260,000

Financially healthy (5x) per month

€433,333

The 3–5x threshold accounts for a typical 50–70% initiative failure rate. Successful work must cover both wins and losses. Break-even is not the right bar.

## The Customer-Facing Team: Multiple Levers, Same Math

A customer-facing product team of eight carries the same €87,000 monthly cost. The levers available to justify that cost are different, but the underlying logic is identical.

If the product has an average revenue per user of €50 per month, the team needs to generate or protect the equivalent of 1,740 users worth of value every month just to break even, and roughly 5,000 to 8,700 users worth of value to clear the three-to-five times threshold.

Churn is often the most direct lever. Consider a product with 50,000 active users losing 2% monthly to churn. That is 1,000 users per month, representing €50,000 in monthly recurring revenue walking out the door. A team that identifies the primary driver of that churn and eliminates it is generating nearly €50,000 per month in protected revenue, covering most of its break-even cost from a single initiative. But that calculation requires knowing the churn rate, understanding its causes, and connecting those causes to the team’s work, and most teams are not operating with that level of financial clarity.

Activation is another lever that is frequently underestimated. If 10,000 users sign up each month but only 30% complete the activation steps that lead to long-term retention, there are 7,000 users each month who paid acquisition costs but never converted to retained revenue. Improving the activation rate by five percentage points, from 30% to 35%, converts an additional 500 users per month. At €50 average revenue per user, that is €25,000 in additional monthly recurring revenue, representing roughly 29% of the team’s break-even threshold from one metric moving in the right direction.

Sales conversion follows the same logic. If the product has a free-to-paid conversion funnel processing 20,000 trials per month at a 4% conversion rate, that produces 800 paying customers monthly. Moving conversion from 4% to 4.5% produces 900 customers, an additional 100 paying users, and €5,000 in additional monthly revenue. Small improvements across multiple levers compound quickly, but only if the team understands which levers connect to which financial outcomes and by how much.

Team size (engineers)

8

Assumes €130,000 cost per engineer per year, including salary, social fees, pension, equipment, and management overhead.

Reshuffle scenario

Monthly team cost

—

12-month total cost

—

12-month total value

—

Cumulative gap

—

Monthly cost

Cumulative cost

Expected value

Actual monthly value

Cumulative value

Each scenario randomizes peak value, ramp-up speed, and decay rate — the variables most teams never measure. The faint dashed line is what you planned. The bars are what happened. Reshuffle to see how rarely the picture looks comfortable.

## The Metrics We Chose Instead

Given that software teams are expensive and that their value is, at least in principle, calculable, it is worth examining why most teams do not measure anything financially meaningful. Some measure activity proxies such as velocity, tickets closed, or features shipped. Others measure sentiment proxies such as NPS, CSAT, or engagement scores. These are not degraded versions of financial measurement. They are a different category entirely, one that was designed around the goal of understanding user behavior and team throughput rather than around the goal of understanding economic return.

The problem is that activity and sentiment metrics can trend upward while financial performance deteriorates. A team can ship more features while building the wrong things. Engagement scores can rise while churn accelerates among the users who actually generate revenue. Velocity can increase while the work being completed has no measurable connection to business outcomes. These metrics feel meaningful because they correlate with outcomes in many circumstances, but correlation is not a reliable guide to prioritization when the underlying financial logic is never examined.

This is a structural condition rather than a failure of individual judgment. Organizations chose these metrics because they are easier to instrument, easier to communicate, and easier to look good on than financial metrics. A team that measures its success by features shipped will always have something to show. A team that measures its success by return generated will sometimes have to report that it does not know, or that the return was disappointing, and that kind of transparency requires an organizational culture that most companies have not deliberately built.

The matrix above is drawn from a product management training program I run called Booster, where product leaders map their actual metrics against their investment thesis to surface gaps. The exercise is uncomfortable precisely because most leaders discover mid-mapping that their team’s daily measurements have no direct connection to the financial objective they were given.

## How We Got Here

Understanding why this condition exists requires looking at roughly two decades of macroeconomic context, because the financial dysfunction in modern software organizations did not emerge from bad intentions or intellectual failure. It emerged from a specific environment that made financial discipline in product teams economically unnecessary.

The picture is not a single clean era but two distinct phases. From roughly 2002 through 2011, capital was periodically cheap but conditions were mixed. Rates fell sharply after the dot-com crash and again after the global financial crisis, but in both cases risk appetite was suppressed. The money was technically inexpensive but investors were cautious, multiples were reasonable, and the growth-at-all-costs logic had not yet taken hold. Product organizations during this period still operated with some residual financial discipline inherited from the dot-com reckoning.

From approximately 2011 through 2022, something different happened. Zero-rate policy became fully normalized, risk appetite recovered and then overcorrected, and the SaaS mental model crystallized into a broadly shared investment thesis. All three conditions arrived simultaneously, and the result was about eleven years during which software companies could grow headcount aggressively, miss on the majority of their roadmap, and still look healthy on paper. Revenue growth forgave an enormous range of prioritization mistakes, and the cost of building the wrong thing was largely invisible.

Eleven years is not a long time, but it is long enough to form the professional instincts of an entire generation of product and engineering leaders. The frameworks they learned, the metrics they adopted, the planning rituals they practice, and the definitions of success they internalized were all formed during a window that was unusually short and unusually distorted. There is no cohort of senior product leaders who developed their judgment in conditions where their teams were expected to demonstrate financial return, because those conditions did not exist during the years when that cohort was learning the craft.

When capital became expensive again in 2022, the behavior did not automatically adjust, because the behavior was never connected to the financial logic in the first place.

## The Liability Hiding as an Asset

There is a deeper consequence of this twenty-year period that is now becoming painfully visible, and it concerns how the industry has thought about large engineering organizations and codebases.

The conventional understanding is that a codebase representing years of engineering investment is a valuable asset. It encodes business logic, captures accumulated decisions, and represents the technical foundation on which future products are built. A large engineering organization is similarly understood as a source of capability, with more engineers meaning more capacity to build, maintain, and improve that foundation.

#### What organizations believed

Large codebase

Years of accumulated value

Large engineering team

Organizational capability

Scale

Competitive moat

Headcount growth

Progress by definition

Complexity

Barrier to competitors

#### What was accumulating

Maintenance burden

Growing annually, unmeasured

Coordination overhead

Compounding with every hire

Organizational inertia

Decisions slowing down

Rising costs, flat return

Never on any report

Own teams moving slower

Invisible until it wasn't

While some argued that large codebases actually shoulg be considered a liability, the industry as a whole has mostly ignored that. But this understanding is now being more closely examined. A large codebase also carries maintenance costs that grow over time as the system becomes more complex, more interconnected, and more difficult to change safely. Every engineer added to maintain it increases coordination costs, introduces new dependencies, and adds to the organizational weight that slows decision-making. The asset and the liability exist simultaneously, and for most of the past twenty years, the financial environment masked the liability side of that equation.

The arrival of large language models has made the liability visible in a way that is difficult to ignore. Recently,Nathan Cavaglione, a developer, built a functional replica of approximately 95% of Slack’s core product in fourteen days using LLM agents. Slack was built by thousands of engineers over the course of more than a decade, at a cost that represents billions of dollars in cumulative engineering investment. Nathan started without any of that accumulated complexity, without the organizational weight, without the legacy architectural decisions, and without the coordination costs, and arrived at a comparable product in a period that would not constitute a single sprint in most enterprise engineering organizations.

Day 14: A functional replica of Slack's core product, built by a Nathan using LLM agents.

This does not mean that Slack’s engineering investment was wasted, because Slack also built enterprise sales infrastructure, compliance capabilities, data security practices, and organizational resilience that a fourteen-day prototype does not include. But it does mean that the assumption underlying large engineering organizations, which is that scale and accumulated complexity represent competitive moats, is no longer reliable in the way it once was. When the cost of building a functional approximation of a sophisticated software product can collapse to days of individual effort, the question of what a large engineering team justifies becomes both more urgent and more difficult to answer with the metrics most organizations currently track.

The obvious objection is that code produced at that speed becomes unmanageable, a liability in itself. That is a reasonable concern, but it largely applies when agents produce code that humans then maintain. Agentic platforms are being iterated upon quickly, and for established patterns and non-business-critical code, which is the majority of what most engineering organizations actually maintain, detailed human familiarity with the codebase matters less than it once did. A messy codebase is still cheaper to send ten agents through than to staff a team around. And even if the agents need ten days to reason through an unfamiliar system, that is still faster and cheaper than most development teams operating today. The liability argument holds in a human-to-human or agent-to-human world. In an agent-to-agent world, it largely dissolves.

## The Organizations That Will Pull Ahead

The competitive advantage available to organizations that take this seriously is not primarily technical. It is analytical. Companies that can clearly articulate what each of their teams costs, what value each team generates, and whether that value clears a financially viable threshold are in a structurally different position than companies that cannot. They can make build versus buy decisions based on actual economics rather than organizational preference. They can identify when a team is working on problems that cannot generate sufficient return at their cost level. They can sequence initiatives based on what value is being lost each day they are delayed, rather than on who argued most persuasively in the last planning meeting.

Most organizations cannot do this today. The measurement infrastructure does not exist, the financial data does not flow to the people making prioritization decisions, and the habit of asking these questions has not been built. Building it is uncomfortable, because the answers are sometimes unflattering. A team that examines its work through this lens will sometimes discover that it has spent a quarter on things that do not connect to financial outcomes in any meaningful way, and that is a difficult finding to sit with.

But the alternative is continuing to run an organization where teams with million-euro annual budgets make daily investment decisions without the financial context to know whether those decisions are generating return. That condition was sustainable when capital was cheap and growth forgave everything. It is increasingly difficult to sustain in an environment where boards expect financial returns, where the cost of building software is collapsing due to AI, and where the question of what a team justifies can no longer be deferred indefinitely.

The organizations that develop the habit of asking these questions clearly, regularly, and without flinching will accumulate an advantage that compounds over time. The question is simply whether they will start asking before or after the pressure forces them to.

## Want Help Understanding Your Team Economics?

If you're looking to understand the financial logic of your engineering organization, or want to build the measurement infrastructure that connects team work to business outcomes, contact me.

Contact me

---
title: 'The Speed Trap: 8 takeaways from Faros''s latest AI engineering research'
url: https://www.faros.ai/blog/ai-speed-trap-takeaways
site_name: tldr
content_file: tldr-the-speed-trap-8-takeaways-from-faross-latest-ai-e
fetched_at: '2026-09-18T21:26:15.638922'
original_url: https://www.faros.ai/blog/ai-speed-trap-takeaways
date: '2026-09-18'
description: 'AI made software development faster, but review gaps, QA bottlenecks, and rising incident volume reveal a new risk: the Speed Trap.'
tags:
- tldr
---

## Eight takeaways from the Speed Trap report

Earlier this year, we released research which documented what we called theAI Acceleration Whiplash. AI adoption was increasing engineering output faster than organizations could absorb it. Throughput was rising, but bugs, incidents, rework, and workflow delays were rising faster.

Our latest AI Engineering Report analyzes the most recent 12 months of telemetry from 22,000 developers across 4,000 teams. Unlike our prior report, which examined the transition from low to high AI adoption, this edition looks at what happens as organizations deepen their high AI adoption through more intensive use.

We found that some of the worst transition-era effects are easing as engineering organizations are getting better at turning AI-generated output into shipped software. However, that improvement is coming with new risks, increased strain downstream, and higher costs.

We call this theSpeed Trap: organizations are optimizing for faster code creation and delivery while the costs of verification, remediation, and operational load accumulate further downstream.

Here are 8 key takeaways from our data.

{{cta}}

## 1. AI adoption is deepening, and the frontier has moved to agents

AI usage is already widespread. In this dataset, 79% of developers use at least one AI tool weekly, 86% of teams exceed the 50% weekly active-user threshold, and acceptance of AI-generated code has reached 65%. The more important change is what developers are now willing to delegate. Agentic review has moved quickly into mainstream workflows, with many companies running AI review on 50–80% of PRs. Autonomous authorship is still much earlier, but a small group of organizations has begun to pull ahead, with agents opening 13–14% of PRs at the leading edge. Currently, organizations are much more comfortable letting agents critique code than write it, but the frontier is gradually starting to move toward autonomous authorship.

## 2. Developer thrashing changed shape

In our previous report, the cognitive-load story was dominated by parallelism. Developers were touching far more PRs per day, opening more threads, and struggling to finish them. That specific pressure is easing, but something arguably worse has emerged in its place. Restarts are up 66.7%, nearly five times the increase we saw in the prior dataset. Work is making it further through the system before someone realizes it needs to go back. A restart is the most expensive kind of context switch. The developer has to reconstruct where they were, what they were trying to solve, and why they made the decisions they did. Instead of “too many threads,” the failure mode increasingly looks like “wrong path, start over.” And as more authoring is delegated to AI, restarts can be a useful signal to indicate where AI agents lacked the context to get work right the first time.

## 3. The delivery pipeline is moving again

The most encouraging change in this report is that more of the work is finally reaching production. In April, high AI adoption teams were completing and merging more work while deployments were falling. The front half of the system had accelerated, but the final stages were struggling to absorb the volume. That has changed. Deployment frequency has reversed direction, task throughput remains strong, and code churn has fallen dramatically from the extreme levels we saw during the initial adoption period. This is real progress, but the rest of the report expands upon what is happening along the way. We describe the pipeline as unblocked, but leaky—more work is flowing through, but sacrifices are being made along the way to keep it moving.

Key findings from Faros's AI Speed Trap research

## 4. AI-assisted changes are still getting bigger

While several of the transition-era effects are easing, larger code changes are not one of them. In this dataset, average PR size is up 71.8%, even more than in our previous dataset. Developers are also touching more files and broader parts of the codebase. AI-assisted changes are permanently larger and permanently broader than the human-paced baseline. That matters because size compounds almost every downstream cost. Larger changes are harder to understand, harder to review, harder to verify, and more expensive to unwind when something goes wrong. And in this edition, that matters even more because of what happens next: those larger changes are increasingly reaching merge without being reviewed at all.

## 5. A growing share of PRs are being merged without any review

Six months ago, we flagged a 31.3% rise in PRs merged without review as one of the most alarming findings in the report. That number is now 76.3%. As AI output increases, review capacity is not growing at the same rate. When queues are long and delivery pressure remains high, teams may reduce or skip review altogether to keep work moving. Repeated decisions of this kind can become a default operating practice over time. With AI usage continuing to deepen across the SDLC, organizations should consider clear review requirements based on risk and scope. A central governance question will be which review process applies to each type of change, and whether those rules remain clear and consistent under increased delivery pressure.

{{cta}}

## 6. Work moves faster upfront, then queues downstream

Writing code is no longer where work stalls, as AI has accelerated output at the authoring stage. Now the delays have moved further downstream. Specifically, time in QA is up 300.6%, the largest deterioration among the major efficiency and flow metrics in this dataset. Time in review also remains heavily elevated. As larger, more complex AI-generated code arrives and then receives less review, QA inherits the verification burden, where it is often slower and more expensive. That is the Speed Trap in workflow form. The top of the funnel gets faster while the burden of proving the work is correct accumulates further down.

## 7. Per-change risk stabilized, but operational strain has not

This is where the new report departs sharply from the last one. In April, incidents per PR were up 242.7%. In this dataset, they are up just 14.5%. That is a major improvement, as the transition-era collapse in per-change quality does not appear to continue degrading as AI adoption deepens. However, the aggregate picture is much less reassuring. Monthly incidents are up 125.4%, remediation is slower, and backlogs are growing again. Each individual change may be safer than it was during the initial AI adoption transition, but there are far more changes moving through the system. So while organizations are getting better at producing and shipping individual changes, the risk and total cost of operating the system continues to rise.

## 8. Agentic review is the first promising countermeasure

Our data also points to a promising development. Agentic review is now deployed widely enough to assess its impact among teams that use it heavily. Those teams see faster first reviews and lower change failure rates. The findings are correlational, and unreviewed merges continue to rise even where adoption is high. Still, agentic review is the first intervention we have measured at a meaningful scale that is associated with improvements across multiple downstream metrics. This suggests that new infrastructure can absorb some of the pressure created by AI-scale output. Our conclusion from April remains: the greatest leverage lies at the authoring stage. Review helps catch mistakes and reduce risk. Improving authoring quality reduces the number of mistakes that reach review in the first place.

## How to escape the Speed Trap

To escape the Speed Trap, engineering organizations now need to rebuild the controls around AI-scale development, improve the context agents receive before they write code, and measure AI by the outcomes it produces rather than adoption alone.

The full Speed Trap report turns those priorities into action, with 10 recommendations organized around observing, optimizing, and governing AI at scale. Download the report for the complete findings and recommendations.

{{cta}}
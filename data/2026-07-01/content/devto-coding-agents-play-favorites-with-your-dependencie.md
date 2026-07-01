---
title: Coding Agents Play Favorites With Your Dependencies - DEV Community
url: https://dev.to/dailycontext/coding-agents-play-favorites-with-your-dependencies-2dl6
site_name: devto
content_file: devto-coding-agents-play-favorites-with-your-dependencie
fetched_at: '2026-07-01T19:35:56.780409'
original_url: https://dev.to/dailycontext/coding-agents-play-favorites-with-your-dependencies-2dl6
author: Adam DuVander
date: '2026-06-29'
description: Deep into a coding session, you realize you want beta testers to try some new functionality first.... Tagged with agents, aie, tooling.
tags: '#agents, #aie, #tooling'
---

AI Engineer World's Fair Coverage

Deep into a coding session, you realize you want beta testers to try some new functionality first. You ask your agent to add feature flagging to your app. It offers you LaunchDarkly’s experimentation solution and a reasonable-looking plan to implement it. With a skim of a Markdown document, you accept its recommendation, and it begins writing code.

This is a realistic scenario, because Claude, ChatGPT, and Gemini all recommendLaunchDarkly. But when you ask these questions of your agent, the response comes from a single model that was asked just once. It’s subject to the same training bias and nondeterminism as any prompt. In my research, the tool recommendations can vary considerably.

## How Dependencies Are Chosen

Regardless of whether it’s the agreed-upon leader, the model’s favorite arrives with the same confidence, you give the plan the same light read, and you probably react with the same “looks reasonable.”

That’s a dependency decision. And it was mostly abdicated to your agent.

On one hand, this makes sense. You trust that agent to plan and write the code to build your app, so it’s reasonable to trust its other decisions too. You also can review the code it writes and suggest alternative approaches. More and more, engineers give the code a cursory scan similar to the implementation doc.

Indeed, there are multiple sessions at theAI Engineer World’s Fairthat either pronounce code review dead or declare an intention to kill it. With human review as a bottleneck, engineers work toward automated review solutions we can trust. Most organizations will require a robust approach, perhaps at the level of a mathematical proof, as Erik Meijer may suggest in his keynote.

Many dependencies also have a life outside of your codebase, beyond the full visibility of any review process. Before this modern era, two-ish short years ago, dependencies weren’t adopted with academic rigor. But there were usually multiple sets of eyes, and a decision took significantly longer.

Pre-2024, looking for a new tool started with a web search or a chat message to collaborators. You would research alternatives, investigate maintenance issues, and scrutinize open source licenses. There might be an RFC, or at least a teammate’s gut check. There were conversations and data gathering that went into choosing a new tool for your project.

Even with AI agents writing most of the code, some engineers or teams may still use a less automated, well-researched decision-making process. But the modern tools don’t encourage it. The de facto approach is the feature flag story: Ask the agent, get the recommendation, and start the build.

## How Top Models Rank Dev Tools

With more engineers turning to their agents for research, I’ve been tracking what gets recommended across common categories such as application databases, managed hosting, and, yes, experimentation platforms like LaunchDarkly. I run the same set of prompts multiple times on the top models and publish the results publicly atllmrank.fyievery month.

Each category ranking is an average of the results from the latest Claude, ChatGPT, and Gemini models. Though LaunchDarkly has remained atop theexperimentation leaderboardfor three months, No. 2 and No. 3 have been distinct each time. There’s even more change when you look at the differences between models. For example, the latest data saw both Gemini and Claude rankSplit.iosecond, behind LaunchDarkly. ChatGPT did not list the product at all. If you’d asked your agent for multiple feature flag options, you’d get different results based on which model you’re using.

There are many of these disagreements across models. In one fun example, I asked for dev-friendly AWS competitors. ChatGPT returned Azure as one of its responses 100% of the time. Gemini did not include Azure in any of its answers. Conspiracy theories abound.

These disagreements between models are meaningful because it’s not just typical AI noise. The methodology I’ve used represents distributions of recommendations rather than one-offs that an engineer would get from their agent. Based on roughly 50,000 pairwise run comparisons, all three models shared a top-three grouping (regardless of order) in about 58% of cases. In other words, they agree only slightly more than at least one disagrees.

## What the Disagreements Actually Mean

Engineers are used to nondeterministic outputs. Two code reviews might provide slightly different responses. That’s expected variation, even within the same model. Dependency recommendations are a little sneakier. They arrive with an authoritative plan and are remarkably consistent within a model.

Gemini provides the same top recommendation 97% of the time. ChatGPT and Claude are within a percentage point. Each agrees with itself, though it frequently disagrees with the others. At minimum, it’s worth a second model’s opinion before you commit.

Claude commands roughly 54% of the enterprise AI market share, according to aMenlo Ventures reportfrom Q4 2025. It’s also the most frequent outlier. Claude is most likely to give you a different top three than the other two. The tool your agent just recommended with confidence may be one that a second opinion would contradict.

The cost of adopting the dependency your model recommends is often just a click of a button. Undoing a dependency that you later regret is significantly more work — even if you make the model apologize and help fix its mistake. There may already be other systems that now require what the tool delivers. You’ll have to update them as well. That’s 42% of cases where a second opinion would have pointed you somewhere else.

Many of the AI Engineer World’s Fair sessions are focused beyond the model. Harness engineering, context optimization, and software factories are about improving workflows and generating more predictable outcomes. Dependencies are one place where model disagreement shows up clearly, but probably not the only one. Find these gaps and fill them with these new engineering disciplines.

Not every engineering team will implement the multi-model approach. The default path is where most dependency decisions will continue to be made. And it's where developer tool companies either show up or don’t. If you work with a product or marketing team, this is the data gap they probably don’t know exists yet.

That feature flag decision, and thousands more like it, gets made whether you think about it or not. The 42% disagreement number will change as models converge or diverge and the market shifts with them. What stays the same is that the decision lands somewhere: Is it with your agent, a single model, a sub-agent, a model routing algorithm, or some human in the loop? All of these are being advocated at the AI Engineer World’s Fair. The best sign is that we’re talking about it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
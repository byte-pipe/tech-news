---
title: 4 New Evals and 16 Experiment Variants to Fix 1 Customer Complaint
url: https://www.producttalk.org/4-new-evals-and-16-experiment-variants
site_name: tldr
content_file: tldr-4-new-evals-and-16-experiment-variants-to-fix-1-cu
fetched_at: '2026-09-16T15:21:47.129299'
original_url: https://www.producttalk.org/4-new-evals-and-16-experiment-variants
date: '2026-09-16'
published_date: '2026-09-16T13:00:36.000Z'
description: 4 New Evals and 16 Experiment Variants to Fix 1 Customer Complaint
tags:
- tldr
---

Share this article|Listen to this article ($)

"That is a lot of first layeropportunitiesthere. I wish I could click on this card and be like, 'Clean this up.'"

This was aVistalycustomer reviewing her first AI-generatedopportunity solution tree. Up until this point, the feedback was extremely positive. But this comment stood out to me.

She was looking at a branch of her tree where there were several flat opportunities. There was no hierarchy. And her first instinct was to clean it up.

But I didn't want to give her a "clean up" button. I wanted to fix the problem at its source. Why didn't the agent add more structure to this branch?

Answering that question turned into a three-week adventure.

People keep asking me why I'm working withVistaly. They share they built their owninterview synthesisandopportunity solution treegeneration pipelines usingClaudeorChatGPT. And inevitably they ask, "Why do I need another tool for this?"

Because it took 4 new evals and 16experiment variantsto get to the root of 1 customer problem. High quality synthesis takes sweating the details.

Today, I'm going to tell you that story.

Start with this overview video or dive into the article below.

## A Quick Refresher on Opportunity Solution Trees and My Vistaly Partnership

The purpose of anopportunity solution treeis to help you find the best path to your desiredoutcome. It alignscustomer needs(theopportunity space) with business needs (thedesired outcome) and ensures that everything you build lines up with both.

To build an opportunity solution tree, you need to have conducted at least threecustomer interviews—ideally, asstory-based customer interviews.

Customer interviewsynthesis then happens in two steps:

1. Synthesize what you learned from each interview using aninterview snapshot. An interview snapshot is a one-page summary of a single customer interview.
2. Synthesize what you learned across interviews on theopportunity spaceof your opportunity solution tree.

Learn more about:Interview Snapshots|Opportunity Solution Trees

Vistalyis a SaaS provider of opportunity solution tree software. This past February,we announced a partnershipwhere I'm helping them build AI-generated interview snapshots and AI-generated opportunity solution trees, both from real customer interviews.

The opening quote comes from a beta customer of this new Vistaly service. She was reviewing her AI-generated opportunity solution tree and identified an error in the way theAI agentgenerated her tree.

Before I could attempt to fix it, I needed to first understand how often this particular error happens. I had noticed hints of this error in othertraces, but I hadn't had a chance to dig into it yet. I needed anAI eval.

## Measuring with Evals: How Often Does This Error Happen?

AI evals are metrics that help us measure how often an AI output includes an observed error. They help us evaluate the correctness of anLLM response. In my case, I wanted to identify a metric to measure how often a parent ended up with too many children. (If you are new to AI evals, start withmy in-depth guide.)

To start, I tried two different measurement approaches:

### 1. Tree-Shape: A Code-Assertion Eval

I started with a simplecode-assertion eval—which I will refer to as tree-shape. Anopportunity solution treehas a shape that can be described quantitatively. For example, I can count the total number of opportunities, the average number of children per parent node, and the number of mid-level parents. I can look at the distribution of children across nodes. I can see how many interview opportunities weren't placed on the tree at all.

Sample tree shape output: 
nodes: 7
breadth violation: 0
single-child opportunities: 1
max children: 4
average children: 2.29
children distribution: 1, 1, 1, 2, 3, 4, 4
mid-level parents: 1
max-depth: 2
opportunity count: 16
ckm count: 6

These numbers help me at a glance get a feel for how well-formed a tree is. Through my years of working with opportunity solution trees, I've developed some rules of thumb. I typically want to see three to seven key moments. As parents collect more children, they should start to branch into sub-groups. As you conduct more interviews, your tree should get deeper, not just wider. The width should eventually stabilize, rather than grow infinitely. Tree-shape allows me to observe whether these rules of thumb are holding up across the trees that the agent generates.

For the error I was chasing down, I was particularly interested in how children were distributed across parents. How often were parents ending up with way too many children? In the example above, no node has more than four children.

For every opportunity solution tree that my agent generates, I can run it through tree-shape and get these counts. For this particularerror category, I could count how often a parent's children exceeded a designated threshold.

### Missed-Groupings: An LLM-as-a-Judge Eval

When a parent node gains more children, the agent should start looking for sub-groupings. This is fundamentally asemantic task. So I also created anLLM-as-a-Judge eval. An LLM-as-a-Judge eval is when we use a secondLLM-callto judge the output of the first LLM.

When an agent generates an opportunity solution tree, I can break it up into a set of parents with children. I can then send each parent with its children to my LLM-as-a-Judge.

I started by giving the judge what I thought was a simple task: Given a parent and set of children, do you see a missed sub-grouping? If so, suggest a new parent and indicate which children should be grouped under it. My goal was then to count how often the judge suggested a missed grouping.

My hope was that with these two measurements, I would be able to get an accurate measurement of how often this error occurred. And then I would work to reduce theerror rate. But it wasn't that simple in practice.

If you are new to LLM-as-a-Judge evals, I cover them inmy in-depth AI Evals guide.

## Calibrating My LLM-as-a-Judge Eval

You can't just ask an LLM-as-a-Judge to evaluate another LLM's output and be able to trust the LLM-as-a-Judge's scoring. You have to calibrate the judge against your own judgment first.

To do that I had to create a calibration set of tree nodes (a node is one parent with a set of children) that I manually labeled as having a missed grouping or not. I then ran the judge prompt against my calibration set and scored the judge against my own manually created labels.

### T5-g21 — CKM `ckm7` (4 children)

Parent: **Used the opportunity tree to focus on a specific goal or sprint** 

Children:
- `ckm7-o1` — I need the opportunity tree to feel complete enough to confidently prioritize work for my next planning cycle
- `ckm7-o2` — I need to make the opportunity tree accessible and understandable to stakeholders outside my team
- `ckm7-o3` — I need to wedge customer insights into the handoff between me and the engineer before they get too coupled to internal stakeholder opinions
- `ckm7-o4` — I want to group and share the specific opportunities and quotes that are relevant to my sprint goal in one place
 
- Groupable: yes
- Groups: ckm7-o1 and ckm7-o4 under "I need to plan for my next sprint." ckm7-o2 and ckm7-o3: I need to share what I'm learning with others.

This is one entry in my calibration set.

The goal with a calibration set is to see if the judge matches your own judgment. Your calibration set should have a good mix of inputs that include both samples that include the error and samples that do not. You then want to compare the judge's scoring to your own and see how aligned they are.

When scoring your judges, you want to look at both specificity and recall. Specificity measures the judge's accuracy when there is no error. And recall measures the judge's accuracy when there is an error.

In my case, the judge's recall was perfect. It scored 100%. But its specificity was terrible. In the cases where there was no error, the judge thought there was no error 43.75% of the time.

The judge thought way too many samples were missing a sub-grouping, even when there was no missing sub-group. In other words, I had way too many false positives. The judge correctly identified every instance where a missed grouping existed, but it also identified missed groupings where there were none.

I tried many experiments to improve this judge—I simplified the instructions, I extended the instructions, I added more examples, I bumped to a smarter model. Nothing worked.

After seven iterations, my judge was only marginally better. It maintained 100% on recall, but the best I could get for specificity was 60%. It still counted errors where there were none.

So I dug in further.

I noticed in the groupings where the judge would find a non-existent error, it was because the judge was getting confused by unrelated errors.

For example, when given a tree node like this:

Parent: "I need the opportunity tree to stay manageable and well-organized as more interviews are added"
 ├─ ckm4-o6: "The opportunity tree becomes overwhelming as more interviews are added and I worry it won't stay workable" 
 ├─ ckm4-o7 "I want a way to quickly clean up or reorganize a card that has too many top-level opportunities on it"
 ├─ ckm4-o8 "Some opportunities are misclassified under the wrong key moment…"
 └─ ckm4-o9 "I couldn't figure out how to change the status of opportunities…"

The judge responded with:

Group o6, o7: _"I need tools to keep the tree structure manageable as it grows"

o6 and o7 are related. But that's only because o6 simply restates the parent. And by grouping these two together under a new parent that is also similar to the parent, we end up with three opportunities that are simply restating the same thing.

* I need the opportunity tree to stay manageable and well-organized as more interviews are added.I need tools to keep the tree structure manageable as it grows.The opportunity tree becomes overwhelming as more interviews are added.
* I need tools to keep the tree structure manageable as it grows.The opportunity tree becomes overwhelming as more interviews are added.
* The opportunity tree becomes overwhelming as more interviews are added.

All three of these statements could simply be collapsed into a simpler parent: I need the tree to stay manageable as I add more interviews.

With the following children:- I want a way to quickly clean up or reorganize a card that has too many top-level opportunities on it.- Some opportunities are misclassified under the wrong key moment.- I couldn't figure out how to change the status of opportunities.

The judge was getting confused by an opportunity that simply restated the parent. When that error was removed, the judge correctly ruled there were no missed groupings. I realized to improve my missed-groupings judge, I had to first address upstream errors.

## Taking a Step Back to Measure Upstream Errors

My two evals were measuring errors that showed up in a generatedopportunity solution tree. But every tree is built in multiple steps:

1. For each interview, the agent generates aninterview snapshot.
2. After the first three interview snapshots, the agent generates an opportunity solution tree from scratch.
3. After the next one to three interviews, the agent updates the existing opportunity solution tree.

If you've readContinuous Discovery Habits, you might notice this exactly mirrors how I teach humans to create opportunity solution trees.

Opportunities and key moments are framed to be specific to a customer on an interview snapshot, but need to be framed across customers on an opportunity solution tree. When generating a tree, the agent has to take in specific opportunities and key moments and generalize them. But this isn't easy.

By diving deeper into my eval judge's misses, I realized the judge was getting confused by the following upstream errors:

* a poorly framed customer key moment (CKM)
* an opportunity that simply restated its parent without adding additional value

I learned inHamel and Shreya's AI Evals coursethat we should always tackle upstream errors first. Upstream errors are errors that happen in earlier LLM calls. But that didn't feel right in this case. I had a customer complaining about too many flat opportunities. The customer wasn't complaining about poorly framed key moments or poorly framed opportunities. Those were both "good enough" for the customer. But they weren't "good enough" for the judge to do its job well.

I also worried that while I might reduce those errors, they would probably never go to zero. How could I get an accurate count of missed groupings if I couldn't calibrate a judge? I felt stuck.

I reached out toHamelfor help and he reiterated, "Work on upstream errors first." I knew he was going to say that. I still wasn't convinced.

## Two New Evals: Poorly Framed CKMs and Parent-Restaters

I really wanted to be able to get back to our customer quickly and let her know that we cleaned up her branch for her. But I realized this wasn't going to be a quick fix. So I slowed down to get it right. I partially followed Hamel's advice.

I developed two new LLM-as-a-Judge evals to measure my upstream errors. The first judge's job was to measure how often the OST-generation agent generated a key moment that was poorly framed. This required me to get way more specific about what I considered a well-framed key moment and what wasn't.

### T5-k14 — `ckm7`

CKM: **Used the opportunity tree to focus on a specific goal or sprint**

- Well-framed: no
- Violated rules: 5
- Notes: Includes a reason

Poorly framed key moments include errors like a compound key moment (set anoutcomeand uploaded interviews), key moments that included a reason that was specific to one customer (see example above), or key moments that were simply too verbose.

One trick I've learned is to do myhuman labelingwithClaude. I'll have Claude present a key moment, I'll label it as well framed or poorly framed and explain why. Claude will watch for patterns and help me devise rules to give the judge. This is an incredibly helpful way to put rules around what I intuitively do.

The second judge's job was to take a parent and child pair and evaluate if the child adds new information that isn't already covered by the parent. It simply returns true or false.

So if we return to our earlier example, the judge would return false for the following pairs:

* I need the opportunity tree to stay manageable and well-organized as more interviews are added.I need tools to keep the tree structure manageable as it grows.
* I need tools to keep the tree structure manageable as it grows.

And again for:

* I need tools to keep the tree structure manageable as it grows.The opportunity tree becomes overwhelming as more interviews are added.
* The opportunity tree becomes overwhelming as more interviews are added.

But rather than solving my upstream errors first, as Hamel suggested, my plan was to run my tree nodes through these two new evals first and then only run them through my missed-grouping eval if neither of these errors were present. This would allow me to get a more accurate sampling of my missed-grouping errors without getting a bunch of false positives.

My hope was that I could use this method to reduce the missed-grouping error quickly without having to address all of these other errors first.

Remember, no customers were complaining about the upstream errors. Key moment and opportunity framing was "good enough" for the customer; it just wasn't good enough for the missed-grouping judge.

## Running Experiment Variants Revealed a Surprising Pattern

Now that I had a way to measure the missed-grouping error rate, I started experimenting withprompt changesto reduce that error rate.

I returned to my tactic of human labeling with Claude. I worked through about 40 examples of sub-groupings, where I explained what sub-groupings I would add and why. Claude helped me enumerate my implicit rules.

These rules became my first experiment variant. I updated the agent's prompt with these new rules and I rebuilt all my testopportunity solution trees. I thenran the new trees through my four evals: tree-shape, missed-grouping, poorly-framed-CKM, parent-restaters. And a surprising thing happened.

My parent-restaters and poorly-framed-CKMs evals were saturated. They reported a > 90% error rate across all tree nodes (in both my variant and my control). My well-calibrated judges weren't so calibrated. They weren't holding up against real production data. And that meant that no nodes made it to the missed-grouping eval.

But, it turned out I didn't need the missed-grouping eval at all. Tree-shape clearly showed that the agent was adding more mid-level opportunities. Branches had more structure. My new grouping rules were working. But there were two problems.

1. The agent was adding poorly framed parents.
2. The key moments at the top of the tree were starting to balloon past the recommended three to seven.

I needed to make similar prompt changes at the key moment level and I needed to teach the agent how to frame new parents. I also needed to fix my judges.

I started by iterating on my judges. I expanded my calibration sets to make sure they better matched what I was seeing in production. I refined the judge prompts until they were aligned on these new sets. My parent-restaters judge was scoring 100% on recall and 93% on specificity; and my poorly-framed-CKMs judge was scoring 90% on recall and 100% on specificity. With much better judges, it was time to keep experimenting.

Variant two was focused on improving the ballooning key moment problem. I was able to prevent the ballooning, but this fix further exacerbated the poorly framed parents problem.

Variants three through six were trying to teach the agent to frame new parents better. I was trying to reduce the parent-restaters error rate. But as the agent got better at framing parents, it became more reluctant to add new parents.

The more constraints I put on framing, the less likely the agent was to create new parents. I couldn't fix one error without exacerbating the other error.

## Hoping Sonnet 5 Would Save Me

I useSonnet 4.6as the OST-generation agent and while I was working on this problem,Sonnet 5came out. I wondered how it would do. I was secretly hoping that it would just fix both errors.

So I changed the model (variant seven) and reran my trees and reran the evals. The results were interesting, but decidedly not better.

At first, it looked like Sonnet 5 was excellent at following the framing rules. It had zero instances of the parent-restater error. However, it was terrible at finding sub-groupings.

In a tree where Sonnet 4.6 created six mid-level parents, Sonnet 5 created one. In another tree where Sonnet 4.6 created 11 mid-level parents, Sonnet 5 again created 1.

Sonnet 5's low error rate for poorly-framed-CKMs wasn't because it was good at following the framing rules, it was because it simply wasn't adding new nodes at all.

Sonnet 4.6 was getting good at creating new nodes, but every new parent that it created was poorly framed.

I was still going around and around with the same issue. Teaching the agent to find sub-groupings encouraged it to add poorly framed parents. Teaching it how to frame new parents well made it reluctant to add new parents at all.

And a model upgrade wasn't enough to fix the issue.

## Testing More Variants

So I went back to testing more variants.

The way that I improved my parent-restater and poorly-framed-CKM judges was by developing a range of examples that showed the tricky cases. I realized I needed to add these examples to the main agent's prompts.

That was variant eight. And cumulatively across all eight variants, I was starting to have a big impact on one side of the problem. Parent-restaters dropped by about 70% and poorly framed CKMs dropped by about 54%. But I was still struggling to make progress on the original error—missed groupings.

At this point, my costs were going way up. It costs money to generate each tree and even more to run my evals. So variant nine was some quick cost optimization wins to see if I could bring the costs down. It turns out shifting my focus, even temporarily, allowed me to find a new insight.

When I came back to my error categories, I noticed something I had missed in my earlier variants. Almost all of the poorly framed parents were coming from new trees, not tree updates. This was interesting because they both shared the same framing rules. I started to look at what was different between the two and found that one of the prompts used to generate a new tree had some old language that was clearly contributing to the problem.

Once again, stepping away from the problem allowed me to see the problem with fresh eyes. This was yet another reminder to take more breaks. This insight led to a further reduction in parent-restaters, but it made missed groupings even worse.

Ten variants in and I wasn't making progress. Fixing one side of the problem still exacerbated the other side.

At this point, I decided to completely rewrite my sub-grouping rules from scratch. I did a bunch of manual labeling, had Claude help me find patterns, and used what I learned to write a whole new set of rules.

I iterated on those rules for three more variants. I saw incremental progress on each round and across all three, I started to see missed groupings come down. But not enough.

## Asking the Agent to Fix Its Mistakes: Moving from Eval to Guardrail

I decided that this wasn't a problem I could solve with prompt changes. I had exhausted that path. So instead, I decided to tackle it with someorchestrationchanges.

Orchestration is how we break up complex tasks into smaller tasks for the LLM. For example, I already break tree generation into several steps that mirror exactly what we teach students inour classes—start with key moments, then group opportunities, then structure each branch.

After each of these steps, the agent uses an audit tool to check its work. The audit is designed to catch common LLM errors and then sends what it finds back to the LLM to fix its own mistakes. I wrote about needing to add this agentic loop inan earlier blog postto catch and fix change set errors.

I realized I could use this same infrastructure to reduce my missed-grouping errors (variant 14). Instead of playing whack-a-mole trying to find the right balance between adding mid-level parents and framing them well, I could just let the agent make a first attempt knowing that it would make mistakes, I could then trust the auditor to catch those mistakes, and then I could give the agent a chance to fix those errors.

To make this work, I had to teach the auditor how to identify at least one of my two errors. I had two choices:

* I could teach the auditor to identify the missed-grouping error and optimize my prompts for well-framed parents.
* Or I could teach the auditor to identify the parent-restater errors and optimize my prompts to create good sub-groupings.

The auditor is pure deterministic code and I didn't want to introduce the cost of another LLM call. So I went with the first option.

I used tree-shape as a guardrail to identify parents with too many children. Remember, tree-shape just describes the shape of the tree. It's purely deterministic code. This made it a great fit for the auditor. And I shipped the prompts that were optimized for well-framed parents.

With this setup, the agent would still make missed-grouping errors when creating the tree. But now the auditor would catch those mistakes and send them back to the agent to fix. Since the prompts were now heavily weighted toward well-framed parents, when the agent corrected those errors, it did so with well-framed parents.

Finally, I saw both error rates go down.

But I noticed a new problem. I started to see too many parents with only one child—the opposite problem of missed groupings. The agents were now overeager in adding new parents. Tree-shape helped to expose this error.

Thankfully, fixing this one was easy—it just required a couple of iterations (variants 15 and 16). In variant 16, I saw a 78% reduction in parent-restaters, a 29% reduction in poorly-framed-CKMs, and a 65% increase in mid-level parents (more sub-groupings being added). This one looked like a winner.

## What I Learned from Grinding Through Variants

I spent three weeks on this problem and learned a lot along the way:

* It was the first time one of my calibrated judges didn't hold up against production data. I was surprised when they reported > 90% error rates. I knew from looking at trees in production those reports weren't accurate. And I'm now learning how to better sample calibration sets.
* Even though I was reluctant to follow his advice, Hamel was right. I had to address upstream errors before fixing my target error. But it didn't turn out to be that simple in practice. Fixing the upstream errors exacerbated the downstream error. Being able to measure all of the errors was what was key. Fixing them required a delicate balance.
* I again learned the limitations of prompt changes and was reminded thatbuilding reliable AI productsis a mix ofprompt engineering,context engineering, orchestration, and guardrails. We have to use all of the tools in our toolbox to address stubborn challenges, especially when error categories are so intertwined.

But it wasn't just about what I learned. I was also able to deliver real value to our customers. When the customer who mused about her unstructured branch next checks her tree, she'll see some new sub-groupings.

This sounds like a small thing, but when you look at a big, flat branch on youropportunity solution tree, it's hard to know where to start. It's not as actionable as a well-structured branch. It wasn't acceptable to me to add fake structure, where a new parent simply restated its child. That just adds noise.

The benefit of a well-structured opportunity solution tree is to help you know what to work on next. Being actionable is the benefit. My job is to sweat these details, so that I can deliver that benefit.

So yes, you can give Claude orChatGPTa pile of transcripts and ask it to produce an opportunity solution tree for you. But if you want it to be effortless, if you want to look at your tree and know exactly what to do next, it takes someone sweating the details to get it there. I'm happy to do that for you.

If you want to give what we are building a try, check it out atVistaly.com.

## Audio Version

The audio version is only available for paid subscribers.

## Read next

AI evals have been the "it" skill for product teams for over a year. I've even called evals a new discovery habit.

But I still meet product teams who only have a vague idea of what evals are. And it's not their fault. Most

 

In June, I returned to Product at Heart in Hamburg, Germany. I love this event.

Arne Kittler and Petra Wille do such an amazing job of curating a thoughtful lineup of speakers and they obsess over the attendee experience. If you are looking for a high-quality product conference, I

 

My initial reaction to the recent package hacks was fear. But I quickly learned I can mitigate much of the risk with a handful of configuration settings.

If you haven't been following along, a large number of packages (think of packages as bundles of reusable code) have been
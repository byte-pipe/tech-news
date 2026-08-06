---
title: 'A Data-Driven Explanation: Why Do AI Agents Still Fail'
url: https://jeremytian.substack.com/p/a-data-driven-explanation-why-do
site_name: tldr
content_file: tldr-a-data-driven-explanation-why-do-ai-agents-still-f
fetched_at: '2026-08-07T06:00:30.028799'
original_url: https://jeremytian.substack.com/p/a-data-driven-explanation-why-do
author: Jeremy Tian
date: '2026-08-07'
description: It’s been about two years since AI agents went mainstream.
tags:
- tldr
---

# A Data-Driven Explanation: Why Do AI Agents Still Fail

Jeremy Tian
Aug 04, 2026
3
Share

It’s been about two years since AI agents went mainstream. According to Capgemini’s 2025 report, AI Agents were estimated to generate roughly $450 billion in economic value across 14 surveyed countries by 2028. That’s less than a year and a half from now. So, how are AI agents doing now?

Coding agents: remarkably well. Claude Code, Codex, and others have crossed the threshold from autocomplete to shipping real work end-to-end. Anecdotally, I know many people who don’t even open their IDEs anymore. But it turns out, coding agents are the exception.

According toStanford’s 2026 AI Index, organizational AI adoption continues to rise, but AI agent deployment remains in the single digits across almost all business functions. For AI agents specifically,researchers from Stanford, Berkeley, IBM, etc.found that 68% of deployed agents execute no more than 10 steps before human intervention.

It’s tempting to mentally extrapolate improvements across AI: “if AI can handle something as hard as disproving theJacobian conjecture(an 87-year-old math conjecture), surely it can handle my back-office workflow.” This line of reasoning is in fact so common that there is a term for it: the “Jagged Frontier” of AI, which describes the imbalance of AI capabilities.

An interesting example to illustrate this is howGemini Deep Thinkperformed well enough to earn a gold medal at IMO, but can only read an analog clock correctly 50.1% of the time.

None of that explains why enterprise agents underdeliver, though. The short answer is that making AI agents that consistently perform well is very hard.

In general, four things explain most of the gap: variance, benchmark quality (datasets & evaluations), agent-specific errors, and alignment. What follows is a data-driven deep dive into each and why there’s such a massive gap between the incredible enterprise AI Agent value we were promised and the little value that has been provided.

On Variance & Reliability

## Your Agent’s Performance Ceiling and Floor

Solving reliability in a non-deterministic system is inherently a really hard problem. To illustrate this, let’s model an AI agent as a system that performs some number of steps autonomously to complete a task. Let’s assume the probability that any step succeeds is 90%.

When your agent attempts a workflow that takes 10 steps, only 34% of your agent runs will succeed on all 10 steps (0.9¹⁰). When that process doubles to a 20-step workflow, the end-to-end pass rate decreases to 12%. A 30-step workflow has a 4.2% success rate.

End-to-end reliability decays as the number of steps grows.

Because every step is now non-deterministic, the overall reliability of the system decreases exponentially with the number of steps in your workflow. This is a big problem that gets exacerbated by complexity.

Even if we increase the probability of a single step succeeding to 99%, after 30 steps, you can only expect 73.97% of your end-to-end runs to complete successfully, which is a massive downgrade from the 99% individual step success rate.

Of course, real agents aren’t this simple. The calculations above assume that each step is independent of each other. Subsequent steps are not independent. In reality, errors compound (a bad step corrupts context for every step after it). But on the flip side, agents can also recover from their mistakes, you can build guardrails to guarantee specific output formats, etc. This example is just a first-order approximation, modeling an AI agent extremely simply. Unfortunately, what is not just a first-order approximation is the idea this example illustrates: more steps means less reliability, fast.

The problem we just described was “intrarun variance”; in other words, the variance within a run.

But your agent doesn’t just run once. It will need to solve the same or similar tasks many, many times.

Intrarun variance’s counterpart is interrun variance—the variance across multiple runs. Sierra knew this was a problem, which is why when they builtτ-bench(one of the industry standard benchmarks for customer support), they made pass^k (pass-to-the-k) a first-party measurement. Pass^k, simply put, is just a measurement for interrun variance: run each dataset task k times; a task only counts as passed if it succeeds all k times. In other words, pass^k asks what your agent can do every single time, not just once.

To solidify the issue of interrun variance in a more concrete example, let’s take a look at τ³ bench (an improved τ-bench). Forτ-knowledge(banking domain), the highest performing model was gpt-5.2 (high reasoning) with a pass^1 of 25.52% (pass^1 here means they ran each task in the domain once, and 25.52% of them passed).

At pass^4, it dropped by about half to 13.40% (pass^4 here means they ran each task in the dataset 4 times and only 13.40% of tasks passed all 4 times). And note that this is not an old-model problem: gpt-5.2 is a frontier reasoning model, and interrun variance still cuts its performance in half.

Pass^k tells you how consistent your agent is. A natural follow-up question is: how capable is it? You can measure this with pass@k: of k runs, if at least 1 of the k runs passed, it counts as a success. You can imagine pass^k as an intersection of the successful runs and pass@k as a union.

Looking at the graph below, all the models follow the same pattern, so let’s just focus on gpt-4o (orange). The dotted line shows the accuracy for pass@k (max current capability) across k trials. As you can see, the dotted line starts at ~60% but quickly approaches ~95%.

On the other hand, the solid line shows the accuracy for pass^k (consistency measurement) across k trials. Much like the banking example above, the solid line quickly decays to around half of the original accuracy.

Why does this matter though?

Think of pass@k as the ceiling. What the model can do on its best attempt. pass^k is then the floor; i.e., what you can actually count on in production. For gpt-4o on τ-bench, the ceiling is ~95%, and the floor is ~30%. This matters because a customer whose refund gets botched doesn’t care that the agent would have gotten it right the other 70% of the time.

At this point, you might be thinking: if the ceiling is 95%, why not just run the agent k times and take the run that succeeded? In some domains, this actually works. Coding is (again) the lucky one: you can run the tests and know which attempt was correct. But most agentic tasks don’t come with an answer key. In production, nothing tells you which of the k runs was the right one. If you could automatically detect successful runs, you would have already solved agent evaluation (more on that later). And worse, agents act on the world, which isn’t always so forgiving. You can’t process a refund 4 times and keep the best one.

So, when you see that gpt-4o has an accuracy of ~60% on τ-bench, maybe the first instinct is that we need to make the agent better. But the pass@k shows that the 40% performance gap is almost all explained by variance, not agent/model capability.

In other words, gpt-4o can already solve 95% of the problems. Just not consistently.

This pattern can be seen across almost all public benchmarks as well as with AI agents of customers we have worked with. Variance is one of the massive bottlenecks of AI agents—that is both intrarun and interrun variance.

And it has one more consequence we haven’t talked about yet: if a single run is this noisy, then a single benchmark score is a noisy sample too. Variance doesn’t just make your agent unreliable; it makes your measurements of your agent unreliable. This brings us to the next big problem: datasets and benchmarks.

On Benchmarks

## Your Dataset Might Be Lying to You

Variance makes your scores noisy. But there’s a second, sneakier problem: the dataset you’re training and evaluating your agent on can itself be wrong.

In 2016, a 19-year-old MIT student and a 21-year-old Carnegie Mellon dropout hopped on a flight to San Francisco—a flight that would change their lives forever. They had just gotten accepted into Y Combinator, and their company converged on a simple idea: machine learning was not only driven by compute, but also by better training data. They found early success with autonomous-vehicle companies, and eventually grew into other industries like robotics, defence, government, and more. Nine years later, Alexandr Wang and Lucy Guo’s company, Scale AI, was valued at ~$29 billion—proof that in the age of AI, data is just as valuable as compute.

We believe the same about data for AI agent development. A common misconception is that if you’re not fine-tuning a model, you don’t have training data. But your agent is still trained on a dataset (just not through gradient descent). Every time you adjust a prompt, rewrite a tool description, or restructure a workflow because of how your agent performed on your dataset, you are training your agent on that data. The dataset is the signal your entire iteration loop is steered by: it decides which experiments look promising, which regressions get caught, and which “improvements” ship.

Needless to say, the data you train on is quite important; in fact, some would argue that your agent will only be as good as the data that it’s trained on. Even if your agent performs well on your dataset, it will perform poorly in production if the dataset is stale/outdated, or if it’s not from the same distribution. Because of this, both the quality of and the distribution of dataset items matter a lot.

### Public benchmarks are broken more often than you’d think

Unfortunately, datasets are hard to make well. Even Sierra’s industry-standard τ-bench dataset was revamped into aτ³ dataset. Between the original and the improved dataset, 53 tasks out of 164 total tasks needed to be updated for reasons like “Impossible or Contradictory Constraints”, “Incorrect Expected Actions”, etc. That’s over 30% of the tasks of the original benchmark.

WebArenahad a similar problem: its 812 original tasks needed a substantial round of repairs (e.g. misaligned evaluators, clarified ambiguous instructions, replaced brittle matching rules). Following this, false negatives from these issues were reduced by 11% in their baseline agent. The same dataset quality problem has been seen across many other benchmarks.

It’s a massive step forward that the issues in the original benchmarks were fixed, but these issues cause massive swings in performance, which can completely flip decisions and influence how agents are adjusted.

In practice, if 30% of your tasks are broken, an agent that behaves correctly can score worse than one that happens to match the benchmark’s mistakes. We’ve seen teams fall into this trap, even with internal benchmarks & datasets: they see a number move, conclude a change worked (or didn’t), and steer accordingly. These systemic issues in datasets cost engineering teams many months chasing the wrong numbers and optimizing for the wrong things, leading them farther and farther away from reliable, production-ready agents.

### Your own dataset might be broken too

At this point, an expected response may go something like this: “even if most public benchmarks are broken, I don’t use them. I built my own dataset from my own production data.” That’s definitely the right thing to do, but it’s also much harder to do well than it sounds, for three reasons we will briefly survey (it’s a really complex topic. More on this in another blog).

Your dataset goes stale the moment you ship.Most teams build their dataset once, before production, and then either

1. never update it, or
2. painstakingly update it by hand

But production data differs a lot from your original dataset. The same way a product accumulates bugs after release that no amount of pre-launch QA predicted. So a loop forms: you need observability into where your agent is messing up, you make changes to fix those failures, and then you need to test those changes... against a dataset that doesn’t contain the production cases you were targeting. Your dataset can’t tell you whether the fix worked or whether it introduced regressions because it doesn’t have your production test cases. Now you’re porting production traces into your dataset by hand, forever. This is exactly the kind of thing that should be an automated pipeline, which raises the question of what goes into it.

Selecting what is added to the dataset is harder than it sounds.A lot of the companies we’ve worked with complain that they have millions of production traces and no idea what to do with them.

You should be using them to make your agent better. But how? Blindly chucking all of them into your dataset causes more problems. Iteration time and cost grow roughly linearly with dataset size, and a dataset you can’t iterate against quickly is a dataset you’ll stop using. This means you want the smallest set of traces that is still representative of your production distribution.

The naive answer is random sampling, but think about what that gets you: if your agent already succeeds on 80% of production traffic, then ~80% of a random sample are cases you already know your agent passes. You’d be spending most of your eval budget re-confirming things that work instead of probing the failures you actually care about. Only sampling failures isn’t right either, since then you can’t catch changes that fix your failures but cause massive regressions elsewhere.

And selection alone has a deeper limit: if your dataset only contains traces you’ve already seen, you can only fix problems retroactively. That’s not useful. Imagine if you could only learn from mistakes after you’ve made them. You’d have to get hit by every single car of every make and model and year before you learn that you shouldn’t step in front of a moving car.

A bit of a silly example, but it illustrates that the goal here is beyond fixing your agent on specific test cases. The goal is continuous learning.

Covering the edge cases you haven’t hit yet means generating synthetic dataset items, too. Just like selection, this shouldn’t be done manually. How do you automate choosing which cases to generate while ensuring representative test cases, quality, and minimizing the added test cases? Synthetic dataset item creation is its own hard problem—and one that needs the same thing your selected traces need: somewhere to run, which is the next problem.

Production isn’t static, so you can’t just replay it.Suppose your agent answered a customer’s question last Tuesday: “how many flights did I take in the last 7 days?” The correct answer to that trace is pinned to what your production database looked like last Tuesday. The database has changed since. If you replay that trace today against production, the “right answer” is different; if you froze the trace, you now need a mock database, mock tools, and an environment that reproduces the state the agent originally saw. But that’s not the hard part. The hard part is building an accurate evaluator for this testing environment. As illustrated above, even the most trusted public benchmarks struggle to get their test cases and evaluators right, a problem almost no team has fully solved so far (we’ll talk about a big contributing factor in the final section on alignment).

Creating a good dataset of your own with a reliable and accurate evaluator is a complicated enough topic to warrant its own deep-dive blog later.

So datasets are noisy, they rot, and they’re expensive to rebuild. But suppose you get all of it right: variance accounted for, dataset clean and current. Your agent still fails sometimes. What do those failures actually look like? It turns out they typically follow patterns.

On Agent Errors

## Mistakes Moved Up the Stack, They Didn’t Disappear

Let’s give credit where it’s due: reasoning models have meaningfully cut down on agent mistakes. The flailing, obviously-broken behavior of early agents is mostly gone. But agents still fail, and when you actually categorize the failures, two interesting things show up: the mistakes follow patterns, and those patterns are different for every model.

Let’s start with a2024-era baseline. When the τ-bench authors manually analyzed a random sample of 115 tasks (40 of which failed), this was the breakdown of gpt-4o’s errors:

A third of failures were the agent calling the right tool with the wrong arguments. Another quarter were wrong decisions, and about a fifth each were providing wrong information and only partially resolving the task. Notice what these have in common: they’re largely mechanical. The agent knew roughly what to do and fumbled the execution.

Now fast-forward to a more recentanalysisof three frontier models on the same benchmark. Instead of categorizing failed runs, the researchers manually analyzed 131 cases where the agent passed the benchmark while violating procedure along the way. They call these “corrupt successes”: the agent reaches the right final state, but on the way it misquotes a fee, invents a policy that doesn’t exist, or tells the user it executed an action it never actually took. The outcome checker sees a completed task, but in reality, it’s “corrupt”. By their audit, 27–78% of benchmark-reported “successes” (depending on the model) contained at least one violation like this. Here’s how those violations break down:

Two things stand out. First, the categories themselves changed since 2024. Of course, the analysis was not done by the same researchers, so this is not completely unexpected. But the shift is still there: the mechanical-execution failures that dominated the 2024 breakdown are now a small slice, and the dominant failure modes are things like policy faithfulness and data faithfulness. Essentially, the agent took actions that quietly deviate from the rules it was given, or from the data in front of it. The mechanical fumbles shrank; the failures moved up the stack, from “called the tool wrong” to “didn’t stay grounded in the policy and data.” This is dangerous because mechanical errors fail the task, so your metrics catch them. Grounding errors pass the task, so they ship to production without getting caught. Better reasoning didn’t completely eliminate mistakes. But it did change which mistakes were left while making them harder to detect.

Second, every model seems to have a different dominant failure mode. GPT-5’s violations are led by policy compliance (35.1%), meaning it executes actions the rules didn’t allow. Kimi-K2-Thinking’s biggest issue is policy faithfulness, at nearly half of its violations (47.8%): confident statements about policies that don’t exist. Mistral’s is data faithfulness (28.4%), a category where GPT-5 barely appears (5.4%), which manifests in fabricating prices, flight details, and confirmation numbers.

These distributions come from one domain in one study, so treat the exact numbers as illustrative. The pattern, though, matches what we see across agents in production.

Why does this matter? If agent errors were purely a model-capability problem, you’d expect them to look roughly the same across frontier models and to shrink uniformly with each generation. Instead, each model has its own failure fingerprint. That means “wait for the next model” is not a strategy: the errors are partly a property of the system around the model (the prompts, tools, context, and guardrails), and that system has to be tuned to the specific model running inside it. When you change to a different or “better” model, you’re mostly decreasing the number of mechanical mistakes, which is good progress, but you’re still left with the higher-level failures: staying faithful to policy, staying grounded in data, understanding intent.

There’s also another problem that remains, even after the AI agent is “perfect”: alignment. Alignment is tricky because most of the time, the agent didn’t technically make a mistake at all. It followed the policy, used the tools correctly, stayed grounded in the data, and still did something you didn’t want.

On Alignment

## The Problem That Outlives Every Model

Let’s start somewhere concrete: LLM judges. When teams try to automate evaluation, the standard move is to have an LLM grade the agent’s runs. And the standard complaint we hear is that the quality just isn’t there. The skeptic’s argument goes like this: if the judge can tell what’s wrong, the agent should have been able to figure out the right answer in the first place. You’re using the same “brain” with the same information; in other words, if you change nothing, why would you expect a different result?

We think this argument has some merit but isn’t entirely true. There are creative ways to get better evaluations out of the same initial information: give the judge more compute (e.g., compare a reasoning model to a non-reasoning model), add a second model critiquing the first, and more. In our testing, this resolves a small but real chunk of the quality problems. But it doesn’t come close to resolving all of them. The residual is the interesting part. When a well-architected judge with plenty of compute still grades a run “wrong,” the most common reason isn’t a reasoning error. It’s that nobody ever told the judge what you actually wanted. The judge isn’t failing to reason. It’s missing information that only exists in your head.

That’s alignment. Here, we mean alignment between AI agents and human preferences. In our opinion, it’s an “eternal” problem. What we mean by that: the development of technology will not solve it. Training a better model will not solve it. The gap between what a human wants and what they’ve actually communicated will always have to be closed directly, because no amount of capability lets a model read a preference that was never expressed.

To break the problem down, abstract the specifics of any AI agent away, and you’re left with three things: inputs, a process, and an outcome.

Let’s assume that humans control the inputs into an agent, so we’re left with the process and the outcome.

Preferences in the outcome:when scheduling a meeting, you might ask an AI agent to “find a 30-minute slot with Sarah after 10 am.” The query already has preferences that you remembered to include, such as the “30-minute” meeting and “after 10 am”. But here are a few preferences that you didn’t realize until the agent violated them:

1. The agent books the meeting in Thursday’s one gap: the gap you deliberately left between two 3-hour blocks of meetings so you could eat lunch.
2. The agent books the meeting in a slot that is technically open, but it occupies the 30 minutes right before an important board meeting, a 30 minutes you always keep free to prepare.
3. The agent books the meeting in the middle of a completely free afternoon, but you would prefer to have all your meetings back to back in the morning to get them over with (or maybe you’re the opposite and you want them spread out as natural break points throughout the day).

Everyone carries hundreds of preferences like these (some of which are easier to concretize than others), and so do companies (e.g., document naming conventions, tone guidelines, who gets cc’d). A more general model doesn’t dissolve these since they’re not facts to be learned but rather choices to be communicated. In some form, these preferences will always need to be communicated.

Preferences in the process:say there are two viable methods for a task. Method 1 is more reliable but slower; method 2 is faster but less reliable. Which one you want depends on a lot of factors. For a personal project, maybe you just want to spin something up fast. For a production-ready project, you would prefer reliability while also not being overkill. Even here, only you know what “overkill” means. Only you know what “prefer reliability” means. How much do you prefer it? Under which circumstances would you prefer speed over reliability? You can imagine that even for just the two preferences of speed and reliability, there is a continuous spectrum, of which your preference is a small, fuzzy zone. In reality, for any given task, there are probably dozens of these small preferences. Combining two preferences like speed and reliability gives a continuous 2D plane. Three preferences become a 3D coordinate system. Four becomes a 4D vector space.

The point is that with more preferences, not only is it harder to communicate them all accurately, but also it’s harder to remember every single preference that needs to be communicated in the first place.

If you’ve used AI at all, you’ve almost definitely felt this. You prompt it to do a task you think you’ve explained extremely clearly, and it comes back with something that isn’t what you imagined. Usually it didn’t make a mistake but rather made a choice on a dimension you didn’t know you had an opinion about until you saw the wrong option. You never told it which conventions matter or what “done” looks like to you. Correcting it is you doing alignment work, one preference at a time. Needless to say, this scales with task complexity: the bigger the task, the more unstated preferences it touches, which is why alignment reliably takes more time than anyone budgets for it.

As models keep getting better, capability problems shrink: the mechanical errors go first, then more of the grounding errors. What’s left over doesn’t shrink, because it was never a capability problem. The remaining gap between what agents do and what we want them to do will increasingly be alignment: not “can the AI do the task,” but “does the AI know what doing the task means to you.”

Daunting as this sounds, it’s tractable. ‘Eternal’ doesn’t mean hopeless. It means the work never fully disappears. But preferences can be mined, encoded, and reused instead of rediscovered one correction at a time. More on this in another post.

So let’s return to where we started. We were promised $450 billion of agent value by 2028, and what we have instead is deployment stuck in the single digits and agents that get about 10 steps before a human steps in. The gap isn’t mysterious, and it mostly isn’t a model-capability gap: it’s compounding variance, datasets that lie, failure modes that hide inside “successes,” and preferences that were never communicated. The good news is that every one of those is a system problem, and system problems can be engineered. The next post is an introduction to how AI agents are being improved.

The cover art image in this piece is by Kirell Benzi. We take no credit for them.

Thanks for reading! Subscribe for free to receive new posts and support my work.

Subscribe
3
Share
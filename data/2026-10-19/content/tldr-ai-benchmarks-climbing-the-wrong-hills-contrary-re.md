---
title: 'AI Benchmarks: Climbing the Wrong Hills | Contrary Research'
url: https://research.contrary.com/deep-dive/ai-benchmarks-climbing-the-wrong-hills
site_name: tldr
content_file: tldr-ai-benchmarks-climbing-the-wrong-hills-contrary-re
fetched_at: '2026-10-19T22:49:48.734283'
original_url: https://research.contrary.com/deep-dive/ai-benchmarks-climbing-the-wrong-hills
date: '2026-10-19'
description: A deep dive from Contrary Research.
tags:
- tldr
---

In 1975, Charles Goodhart, the Chief Adviser to the Bank of England,observedthat when governments tried to regulate a set of financial assets, those assets stopped being reliable indicators of economic trends. In what is now known as Goodhart’s Law, hestatedthat:

“Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.”

Put more simply, when a measure becomes a target, it ceases to be a good measure.

For most of AI’s history, AI benchmarks avoided this fate because they measured capabilities that existing models fell meaningfully short of and captured increases driven by a variety of model improvements. As researchers builtbetter methods, higher scores followed not because they deliberately targeted those metrics, but as a side effect of genuine improvement.

This is no longer the case. Recent gains on benchmark performance appearconcentratedin areas that frontier labs have explicitly targeted for improvement. Today’s models improve largely throughreinforcement learning(RL): a model attempts a task many times, is scored on each attempt, and is pushed toward whatever scored highest, a process calledhill climbing. Flawed benchmarks, therefore, not only mismeasure progress against real-world outcomes, but can steer models in the wrong direction.

As AI encompasses a growing share of the global economy, Goodhart’s Law is playing out at a scale it never has before. Big Tech alone plans to spend more than $700 billion on CapEx in 2026, much of it to build and serve models that are ranked, sold, and even bet on according to benchmark scores that often fail to measure what they claim to. That raises the question: are today’s benchmarks still the best way to measure frontier capabilities, or is it time for a new generation? This report covers how and why popular benchmarks are failing, why good ones are so expensive to build, and what better ones could look like.

## Benchmarks versus Reality

Few benchmarks show the problem as clearly asArena(formerly LMArena), a benchmark known for how deliberately labs target it. Launched in May 2023 by UC Berkeley researchers asChatbot Arena, Arena’s namesake benchmark consists of a platform where users can chat with two anonymous models and vote on which response they prefer in a head-to-head battle. These votes are then converted into a chess-style Elo rating, allowing for direct comparisons of model performance across matchups. By April 2025, the platform drew overone millionunique visitors per month and became amainstayin new-model press releases.

In April 2025, Meta released Llama 4. In the company’sblog postannouncing the new model family, it touted that Llama 4 Maverick, a17 billionactive parameter model, beat GPT-4o and Gemini 2.0 Flash across a wide range of benchmarks. One such headline number was an experimental chat version of Llama 4 Maverick achieving an Elo of1417on Arena, placing itsecondon the leaderboard and ahead of models released just months prior, including GPT-4.5, Grok 3, and DeepSeek R1.

Source:Mark Zuckerberg

In the days after the model’s release, users found the benchmark scores didn’t reflect reality. Adisconnectemerged between the behavior of the model developers could download and the overly verbose, emoji-riddled responses observed in the Maverick version used for head-to-head preference battles on Arena. Users on X quicklypointed outthe Maverick version used for the benchmark was “optimized for conversationally,” an assumption found in a chart footnote. At the same time, rumors spread that Meta trained on benchmark test sets, claims the company denied.

In response to growing criticism, Arenaretestedthe unmodified version of Maverick accessible to the general public. It ranked32nd, below GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro, the last of which wasreleasedover a year before Llama 4. At the end of April 2025, Meta’s CEO, Mark Zuckerberg,admittedthat:

“It was relatively easy for our team to tune a version of Llama 4 Maverick that could be way at the top. But the version we released, the pure model, actually has no tuning for that at all, so it’s further down. So you just need to be careful with some of these benchmarks.”

The very same day, researchers released a paper disclosing findings that Meta had privately tested27 unreleased variantson Arena before launch. The process worked likep-hacking, where researchers can cherry-pick variables, outcomes, or data points to force a statistically significant result (i.e., p-value < 0.05). Just as a scientist who runs enough analyses will eventually find a “significant” result by chance, a lab that tests enough model versions will eventually find one that performs well on the leaderboard.

Source:The Leaderboard Illusion

Arena shared the skepticism directed at Meta. Three days after Maverick’s launch, Gwern, the pseudonymous researcher and writer, flaggedmajor issueswith Arena that made it gameable. The people actually rating model responses are all self-selected, and since they are unpaid, they have zero incentive to be honest, rigorous in their judgments, or provide good responses. From this analysis, hepositedthat:

“It's past time for LMArena people to sit down and have some thorough reflection on whether it is still worth running at all, and at what point they are doing more harm than good.”

The failed launch of Meta’s Maverick modelcatalyzeda company restructuring, marking the beginning of over a year of reorganization and changes. In May 2025, Meta reportedlydelayedthe release of its flagship Llama 4 Behemoth, rumored in part because it would not match earlier performance claims. In June 2025, Meta invested$14.3 billionin Scale AI to secure a 49% stake and bring its CEO, Alexandr Wang, into Meta’s leadership to lead the newly formed Meta Superintelligence Labs. That same month, Meta beganofferingmultimillion-dollar pay packages to attract AI research talent. In October 2025, it laid off approximately600 workersacross the AI teams working on pre-Maverick research and products.

In November 2025, Meta’s Chief AI Scientist, Yann LeCun, left the company, lateradmittingthat Llama 4’s “results were fudged a little bit,” with different models being used to achieve better results on different benchmarks. He alsounderscoredthe role of Maverick in kickstarting the company-wide changes, stating that:

“Mark was really upset and basically lost confidence in everyone who was involved in this. And so basically sidelined the entire GenAI organization. A lot of people have left, a lot of people who haven’t yet left will leave.”

18 months after Maverick’s launch, the arena that Meta has climbed back to the podium of is little changed from what made it susceptible in the first place. The votes used to calculate model Elo scores still come fromanonymous, unpaid Internet users who write their own prompts. Although Arena now filters outduplicate votesand adjusts forstyle differencesby default, it has not changed who gets to cast the votes. The same people who pushed Maverick’s sycophantic behavior to a silver medal are judging today’s model responses. Frontier labs are also still permitted to test anuncappednumber of model variants before making them officially public. The results from these unreleased versions are shared privately with the lab, and the lab can withdraw any model version it does not like.

In April 2026, a full year after the release of the Llama 4 model family, Meta introducedMuse Spark. This was followed by the release ofMuse Spark 1.1,1.2,1.3, and theMuse Wondermodels in successive months starting in July 2026. As of October 2026, Meta is once againsecondon the Arena text leaderboard for all labs, trailing only Anthropic, and Arena has raised$200 millionat a$3.1 billionvaluation in a Series B funding round.

The same benchmark is even being used to settlePolymarketandKalshimarkets. From February 2025 to October 2026, over$225 milliontraded across130+ Polymarket marketson what the “best” AI model would be, with the winnerdecidedby the Arena leaderboard. These markets even resolve without controlling for style differences, meaning they use the same flawed scoring methodology that carried Maverick to second place.

People closest to the models have also grown skeptical, with some researchers proclaiming theirlow confidencein benchmarks. Yet the pull to climb these leaderboards hasn’t weakened. Researchers still faceinternal pressurefrom company executives to improve scores on certain benchmarks, and launch-day performance announcements are still treated as amarketing exercise.

### A Metastasizing Problem

Meta is not the only lab whose benchmark scores have outrun its model. In July 2025, Elon MusksoldGrok 4 as “the smartest AI in the world” on the strength of its Humanity’s Last Exam (HLE) score, despite the fact that itfailedin real-world tasks, where it was rated66thcompared to other AI models by human users (in addition to facing criticism forproblematic responsesto questions about controversial topics).

A year later, claims of new state-of-the-art coding performance accompaniedAnthropic’srelease ofClaude Opus 5, which later facedcomplaintsabout jargon-heavy, verbose responses users found disruptive to real software engineering work. It even prompted some to combat overstylized responses by requesting answers inSimplified Technical English (ASD-STE100), astandardized formof the language originally developed to make aircraft maintenance documentation more easily understandable to non-native speakers.

Most recently, at the end of September 2026, Google releasedGemini 4 Argonin a landmark release that camenearlya year after the company’s last frontier model, Gemini 3. The announcement claimed the new model had achieved frontier capabilities in complex workflows across knowledge work and software engineering. Soon after the release, however, it faced accusations ofbenchmaxxing, optimizing models for high benchmark scores at the expense of real-world usefulness. These suspicions stemmed mainly from reports that Google employees found the model still struggled on certaincoding tasks, despite reportedly state-of-the-art performance on some agentic coding benchmarks.

## The Growing Industry Around Benchmarks

When a model card claims a state-of-the-art capability, it typically supports the claim by citing a benchmark result. In this way, benchmarks serve as a scoreboard for frontier AI labs, with assessments of model quality and, ultimately, the ROI of investment in model development riding on the scores.

The importance of benchmarks has grown alongside the scale of AI CapEx. In 2025, Microsoft, Google, Amazon, and Meta spent nearly$400 billionon capital expenditures. After Q2 earnings, the companies raised their 2026 guidance to a collective$720 to $745 billion.OpenAIraised$122 billionat an$852 billionvaluation in March 2026, and six months later, it was rumored to be aiming to raise a new funding round at a$1.4 trillionvaluation. In May 2026, Anthropic raised$65 billionat a$965 billionvaluation, and as of October 2026, its IPO could see it valued at more than$2 trillion.

Much of this value rests on OpenAI’s and Anthropic’s ability to sell model access to business customers. Enterprise spend on generative AI increased from$11.5 billionin 2024 to$37 billionin 2025, representing a3.2xyear-over-year increase. Of that,$12.5 billionwent to foundation model APIs of labs like Anthropic, OpenAI, and Google. Reported model quality is critical to securing these contracts; enterprise buyers use model benchmarks asquasi-Magic Quadrantsto filter models before testing them themselves.

Source:Artificial Analysis,Epoch AI,Surge AI,Vals AI,Zapier

Helping models rank higher on the scoreboard, and ostensibly improve model capabilities, has become big business. Meta’s$14.3 billiondeal for a stake inScale AI, a provider of post-training data and evaluation infrastructure, was only the start. Soon after,Surge AI, an expert training data and evaluations provider that bootstrapped its way to over$1 billionin revenue in 2024, was reportedly valued as high as$30 billionin September 2025.Mercor, another AI data labeling firm, was rumored to be in talks to raise a new funding round at a$20 billionvaluation in July 2026 after reaching$2 billionin gross annualized revenue a month prior.

Three major funding rounds for training data providers happened in September 2026 alone:Snorkelraised a$350 millionSeries E at a$3.5 billionvaluation, AfterQuery reportedly raised at a$3.2 billionvaluation, and Micro1 raised more than$100 millionat a$4 billionvaluation. With so much capital riding on the scoreboard, its flaws matter.

## The Cost of Benchmarks

Arena’s flaws are an especially visible version of problems that many widely used benchmarks today have in common, which is that they are expensive to build well, easy for models to exploit, and often simply wrong.

Good benchmarks cost a lot to build and run. Arena’s crowdsourced platform lowered costs for the over82 millionhead-to-head preference ratings collected as of June 2026. However, democratizing votes to everyday users misaligned what is actually rewarded and what the industry wants to optimize for, as shown whensycophantic, overstylized responseswere prioritized over accuracy.

Building a high-quality benchmark means paying experts. Back-of-the-napkin math shows how costs can quickly accumulate: suppose that a benchmark is constructed to test whether a model can actually work through real clinical cases with the reasoning and judgment of a healthcare professional. It will include 100 tasks, each one requiring a realistic chart with patient history, lab results, imaging reports, and follow-up notes. Each task will take 50 hours to create and quality control, and the internists doing this work will be paid upwards of$350K per year(or over $160 per hour). Creating this benchmark requires a minimum of $800K, plus the costs of running models against the benchmark (usually paid for by developers).

Benchmarks must also be refreshed. As models improve, benchmarks can begin to becomesaturated. If models answer nearly every task correctly, then the benchmark loses its usefulness in distinguishing them from one another. The solution to this is torefresha portion of the benchmark tasks. In our example benchmark, refreshing 25% of the tasks every year would incur $200K in additional costs, bringing the total to $1 million.

Excluding benchmark update costs, GPQA (a set of graduate-level science questions) cost approximately$120K, and Mercor’s APEX benchmark cost more than$500Kto build. Avoiding costs by failing to refresh the benchmark leads to saturation, a processhastenedby the increasing speed at which models now improve. Keeping the test set private alsodoes nothingto prevent this, as both public and private benchmarks saturate at the same rate. This means that while forgoing benchmark updates can save marginal costs, the useful lifespan becomes finite.

Another simple solution is to include fewer tasks. While this could help maintain the quality of individual tasks, it fails to capture the diversity of real-world situations that a given benchmark is meant to represent. The domains being distilled into testable tasks are complex and nuanced. The workflows involved in coding and knowledge work are expansive, and a few dozen tasks are insufficient to properly evaluate a model’s capabilities on how work is actually done. Smaller benchmarks alsosaturate fastercompared to those with larger test sets.

One other approach to cutting costs is using less-qualified constructors for tasks. For example, instead of enlisting internal medicine physicians, a benchmark might use medical students or physician assistants. In doing so, the benchmark sacrifices domain expertise because these groups lack genuine experience with the workflows it aims to capture, leading to contrived scenarios and incorrect or unreliable grading.Terminal-Bench, a popular benchmark for evaluating agentic terminal use, uses publicly contributed tasks rather than paying software engineers. A review ofTerminal-Bench 4.0found it suffered from the same quality issues that plagued Arena, with45.5%of the tasks containing scoring defects.

Rather than relying on humans to create tasks, a benchmark constructor could also use AI to generate them. Instead of spending 50 hours of work on each task, a frontier model could generate the scenario, prompt, environment, and grading criteria for each one. The problem is that the model’s judgmentfundamentally limitsthe output. Generated content alsodrifts towardwhat the model thinks is typical, meaning real-world edge cases will be underrepresented. In this way, synthetic data can beactively harmfuland misleading, effectively comparing models to the current model frontier.

## Benchmark Contamination

Instead of creating new benchmark tasks, another cost-saving shortcut is using existing public data. For example, SWE-bench Verified tasks useopen-source repositoriesto evaluate AI models’ ability to solve real-world software issues. Created by OpenAI in August 2024, this collection consists ofcurated, human-verifiedtasks from the original SWE-bench, and each problem consists of a resolved GitHub issue in an open-source Python repository paired with a corresponding pull request. SWE-bench Verified waswidely usedin the year following its release to measure progress on agentic coding. However, it was later discovered that the cost-saving strategy of using publicly available, open-source repositories introduced afundamental flawlimiting its usefulness: contamination.

In February 2026, OpenAI published findings that SWE-bench Verified was no longer a reliable measure ofreal-world coding ability. The failure of the benchmark stemmed from the fact that the open-source repositories used to construct tasks were the same ones model developers used for training, meaning they could be found in the training corpus. When frontier models were given a short snippet of the task description, theyreproducedthe original, human-written bug fix from memory. This means the SWE-bench Verified benchmark increasingly reflected how much exposure a model had to the repositories during training, rather than actually measuring its coding capabilities.

SWE-bench Verified was not an isolated incident.ARC-AGIis a benchmark created to measure progress towards general intelligence. Its tasks are intended to be easy for humans but difficult for AI to solve. Importantly, thereasoning problemsit comprises are meant to be ones AI systems are unprepared for.

Source:ARC-AGI

Each puzzle looks like acolored gridto a human, but models receive a grid of numbers from zero to nine. While the numbers have no inherent color, ARC’s own viewer always displayed three as green and six as magenta. When Gemini 3 Deep Think was given only those numbers and no mentions of ARC or colors, the modelreasonedthat the “Target is Green (3). Pattern is Magenta (6).” This suggested that the ARC data was actuallywell representedat training time, meaning performance on the benchmark could be attributed to a model’s ability to retrieve from memory rather than actual reasoning. One way to prevent contamination is to keep the test set private and to build it from data that has never been published. ARC-AGI showed that a private set is not sufficient, and the two measures must work together.

Even with these measures in place to prevent contamination, benchmarks are susceptible to reward-hacking if not built carefully and robustly. Meta’s testing of27 Llama 4 variantson Arena was an example of humans exploiting vulnerabilities in a benchmark’s construction. Models show the same tendency on their own. Researchers createdImpossibleBenchby rewriting coding tasks so that tests contradicted the instructions, meaning that a model could only pass by cheating. The results showed that GPT-5 cheated on76%of one version of these tasks.

Poolside, a foundation model developer, found that its model’s SWE-Bench Pro score jumped by20 percentage points, tracing this unexplained performance improvement to an unpruned git history accidentally left in some tasks, allowing the agent to mine it to find the reference solution. After this gap was closed in September 2026, GLM-5.2’s SWE-Bench Pro score fell from78.8%to57.3%, indicating that model performance could sometimes be attributed to exploiting leaked answers rather than actually solving tasks properly.

Labs cannot simply train their way out of this reward-hacking behavior. The natural response to models attempting to game evaluations is to penalize them whenever they are caught cheating. However, METR found that a model canavoid this penaltyby either stopping the cheating or by hiding it. Researchers from OpenAI found that the latter is more common. When they trained models and penalized them for reward-hacking, the models continued to exhibit this behavior, learning tohide their intentwithin the chain of thought.

This means the defense against reward-hacking must be built into the benchmark so tasks cannot be passed through shortcuts and grading actually verifies the work. Exploitable vulnerabilities and contamination are often thedefault outcome. It requires deliberate benchmark construction and incredibly careful analysis to ensure nothing slips through.

## Measuring with Broken Rulers

A benchmark resistant to reward-hacking or contamination can still have misleading results. Just as often, the benchmark can be wrong on its own, either because its answers are wrong or because it asks the wrong questions.

In November 2023, a group of Google researchers releasedIFEval, a benchmark that evaluates instruction-following capabilities of models. It intended to do so through25 unique typesof verifiable instructions, such as asking a model to “write in more than 400 words” or “mention the keyword of AI at least 3 times.” However, some tasks involve impossible requests. One suchpromptwritten in English asks the model to “repeat the request below word for word without change,” but later requests that “your entire response is in Hindi, no other language is allowed.”

Another benchmark,Humanity’s Last Exam (HLE), consists of challenging, expert-level multiple-choice and short-answer questions across math, humanities, and the natural sciences. In July 2025, six months after HLE’s release, researchers at FutureHouse found that approximately29%of its text-only biology and chemistry answers conflicted with peer-reviewed literature. Popular coding benchmarks fare little better. SWE-bench Verified’s problems went beyond contamination, and OpenAI’s audit found that more than59.4%of the problems it examined had flawed tests that would reject functionally correct solutions. The recommended replacement for the benchmark,SWE-Bench Pro, was later found to have quality issues in14%of its tasks.

Even correct benchmark answers can be partly or wholly broken by improper task grading.AutomationBenchis a benchmark created byZapierthat tests AI agents’ execution of end-to-end workflows across sales, marketing, operations, and HR. One task evaluates whether an agent can successfully retrieve the phone number +1-555-0101. However, equally valid answers presented in widely accepted formats, such as +15550101, aremarked as failuresby deterministic grading.

Some errors trace directly back to the cost-cutting shortcuts previously discussed. Mercor’sAPEXbuilds its tasks using large collections of synthetically generated files, a process that can introduce errors. For example, somedocumentsin the benchmark’s tasks refer to “the laws of the Canadian Islands” (a jurisdiction that does not exist) or mention the date “November 31st, 2025” (a date that does not exist).

Lastly, a benchmark can be wrong because it asks the wrong question entirely. SWE-bench evaluates whether a proposed fix passes the tests, but a developer wants to know whether the fix is good enough to ship. When METR asked code repository maintainers to review AI-written fixes that had passed SWE-bench Verified, approximately50%would not have been merged into the main codebase.

## The Second Half of AI Progress

Behind all of these failures is a shift in what AI research optimizes for.Shunyu Yao, Chief AI Scientist at Tencent and former OpenAI researcher, marked this change as AI having reached “halftime.” In the first half, the challenge was inventing new training methods and models. AI capabilities surpassed those of humans inchess,Go, andstandardized testsbecause of fundamental improvements in search, scaling, and reasoning. Evaluations and benchmarks were secondary to creating new algorithms or model architectures.

Yao argues that we now find ourselves in the second half, in which large-scale pretraining, massive compute, and reasoning combined to create aworking recipefor solving tasks through RL and hill climbing. While RL had worked before in a narrow set of cases, pretraining on large amounts of language gave models the general knowledge required for RL to work broadly. The recipe works across so many tasks that it hasstandardizedbenchmark hill climbing. It scales and generalizes well without new ideas, meaning task performance can improve even when not explicitly targeted. That generality, however, is a double-edged sword, since the recipe will climb whatever hill it is pointed at, including a flawed benchmark.

Source:Anthropic,Artificial Analysis,Epoch AI,Google,OpenAI,Surge AI,Vals AI,Zapier, Contrary Research

The field of AI is increasingly shifting its focus from solving problems todefining them. If we can climb any hill, then choosing which hills we actually want to climb is what matters most. That means selecting the right objectives and ensuring the data, rewards, and evaluations behind them point where we want model development to go.

While every benchmark must simplify the real world into testable tasks in an inherently limited process, there is still value in closing the gap between what benchmarks actually measure and what people actually want from a model. Closing this gap means examining the options available to build better benchmarks going forward.

## Choosing Better Hills

The next generation of benchmarks need not be flawed the way many of today’s popular ones are. Thefixstarts with how we build them. It requires strong product sense to understand what’s actually worth measuring, and how to avoid settling for the trivial targets widespread in benchmarks predating it. It means investing in domain experts with the judgment to properly evaluate everything from how prompts are phrased, what is right and wrong, and what files, tools, and context the environment contains.

These environments must reflect the real-world use cases that matter, rather than the contrived scenarios that stem from a lack of experience or erroneous synthetic data. The verifiers grading the tasks must be as carefully built as the tasks themselves, so that only genuine solutions are rewarded. Everything must be robustly analyzed to ensure quality (prevent the wrong answers, questions, and grading prevalent in benchmarks today). Finally, whatever set is used for evaluation must be private, and data drawn from the same distribution should never leak to prevent contamination.

Some benchmarks show promise of what this could look like in practice. They rely on experts and rigorous quality control, and while slower and more expensive to build, they avoid the pitfalls of cheaper shortcuts or less robust benchmark methodologies. Surge AI’sHemingway-benchevaluates how models perform on real-world writing scenarios. It learns from Arena’s missteps by paying professional screenwriters, poets, and copyeditors to makeover 5Kblind pairwise comparisons with written rationales explaining their choices in detail. In doing so, it also avoids auto-graders used by previous writing benchmarks that disagree with expert writersmore than 57%of the time. By limiting evaluations to onlyavailable models, it prevents p-hacking and closes the gap between benchmark performance and the writing capabilities users actually experience.

Another example isCursor’sCursorBench 4.0, which measures how well coding agents handle theambiguous, multi-filetasks that developers actually hand off to AI systems. It avoids the contamination risks of public GitHub issues by building the benchmark fromreal requestsdevelopers made to its coding agent, traced back from the code that was actually committed (many of which actually come from Cursor’s own codebase). It also more closely reflects how developers interact with coding agents: tasks are larger and messier than other public coding benchmarks, involvesubstantially morelines of code than SWE-bench Verified, and prompts are intentionally short and vague, like those seen from actual software engineers.

This goes beyond simple bug fixes to includeother developer workflows, from investigating production logs to performing long-running experiments. One critique of CursorBench’s task sourcing is that drawing largely from one company’s codebase can come to reflect that company’s conventions or workflows. Future coding benchmarks could improve this by exploring use cases across dozens of private codebases, and some have already started, includingsudo L7andReal-SWE.

Even scores from the best benchmark should not be considered in isolation. When benchmark scores diverge from reality, actual experts check the model’s work, whether that is maintainersrejecting test-passing codeor experts disagreeing with auto-gradersmore than halfthe time. Expert human preference data is the closest thing that labs have to the ground truth about whether a model is actually useful, and they should treat it that way. Cursor does this to supplement CursorBench by usinglive-traffic evaluationsto catch cases where an agent’s output appears correct to a grader but actually feels worse to a developer using the product. When Anthropic launched Claude Opus 5.5 in September 2026, it also claimed some benchmark margins had becomeless reliableindicators of real-world differences, instead using internal usage to understand model performance more deeply.

Benchmarks remain an important tool for measuring progress at scale. Collecting expert preference data is resource-intensive, slower, and more expensive to compile than any automated score. As benchmaxxing continues, we must decide which hills we want to climb, and whether today’s benchmarks actually reward progress on them. If AI is to one daycompress 100 yearsof biological progress into a decade or write software that engineersactually wantto merge, the benchmarks measuring and guiding that progress must reward what people actually want from AI systems.
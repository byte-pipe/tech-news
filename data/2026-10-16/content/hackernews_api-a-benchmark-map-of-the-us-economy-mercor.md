---
title: A benchmark map of the US economy | Mercor
url: https://www.mercor.com/research/labor-index/benchmark-map/
site_name: hackernews_api
content_file: hackernews_api-a-benchmark-map-of-the-us-economy-mercor
fetched_at: '2026-10-16T21:55:53.332508'
original_url: https://www.mercor.com/research/labor-index/benchmark-map/
author: speckx
date: '2026-10-16'
description: The US Benchmark Map places AI benchmarks across the American economy, measuring which parts of the labor force are covered by unsaturated, public, agentic benchmarks.
tags:
- hackernews
- trending
---

Research
Enterprise
Experts
Company

# A benchmark mapof the US economy

AI benchmarks have multiplied in recent years, but coverage of economically valuable work remains limited. To measure this, we compiled relevant benchmarks to measure their coverage of American jobs. This Benchmark Map is our first step toward building a comprehensive, continuously updated resource for understanding AI capabilities across the economy.

of 923 occupations covered
208
of 18,797 tasks covered
924
benchmarks in the index
29

## The Benchmark Map

Each tile represents one of the923O*NET occupations making up the US labor force, grouped into22job families. Occupations are shaded according to the share of their tasks which are represented in our initial list of AI benchmarks. A single benchmark prompt can be mapped to multiple O*NET tasks.

click a family to open it

Coverage by
Benchmark Index
APEX only
Covered with at least
1 prompt
5 prompts
* Benchmark Index
* No coverage
All 
22
 O*NET job families, with the share of their occupations covered by an AI benchmark.
Job family
Occupations covered
Computer & Math
29
 / 
36
Business & Financial
33
 / 
48
Community Service
10
 / 
14
Legal
5
 / 
7
Office & Admin
21
 / 
51
Management
21
 / 
56
Architecture & Eng
19
 / 
56
Sales
6
 / 
22
Arts & Media
13
 / 
40
Science
15
 / 
60
Healthcare Practitioners
12
 / 
89
Education & Library
9
 / 
62

In our data set: only208of923occupations have a task with at least5 benchmark prompts, and6of22job families have no such occupations.

Our findings suggest that90% of American working hours are spent on tasks with little or no coverage from existing benchmarks. This makes it very hard to know how good AI models are at the work Americans actually do.

The coverage of existing benchmarks is not random, either. Our map suggests that the AI community is focusing on the largest labor markets first:

Benchmark coverage of O*NET tasks by occupation wage bill
* High AI exposure
* Low AI exposure

Adjusted probability of task coverage

0
%
5
%
10
%
15
%
20
%
High AI exposure
Low AI exposure
$500m
$1bn
$2bn
$5bn
$10bn
$20bn
$50bn

Annualized occupation wage bill (log scale)

Each point shows the estimated probability that an O*NET task with a given AI-exposure tag belonging to an occupation with a given wage-bill will be covered by at least 5 prompts in our benchmark index. AI-exposure tags are binary and come fromEloundou et al. (2023). Occupation wage-bills are calculated from BLS estimates of the mean wage and number of Americans working in each occupation, assuming a 40 hour work week. Estimated coverage probabilities come from a task-level logistic regression of coverage probability on AI-exposure and log occupational wage bill. Error bars are pointwise 95% delta-method confidence intervals based on standard errors clustered at the occupation group level.

For example, benchmarks in our initial list heavily cover AI-exposed lawyers’ tasks, but barely cover any of the O*NET tasks of similarly AI-exposed legal secretaries or court clerks. The long tail of smaller, middle-income knowledge work jobs appears undercovered.

As we build out our coverage of model capabilities across the economy, we hope to both surface and help fill more gaps in our understanding of what models can do.

## Methodology in brief

To break down the economy into sectors, occupations, and tasks, we used the US Department of Labor’s O*NET taxonomy. O*NET divides the US workforce into923occupations; for each occupation, O*NET attempts to provide a comprehensive list of “tasks” which make up the occupation, totaling18,797tasks across all occupations.

Example — 
6
 of the 
22
 
tasks O*NET associates with
 
Lawyers
1. 1Prepare, draft, and review legal documents, such as wills, deeds, patent applications, mortgages, leases, and contracts.
2. 2Advise clients concerning business transactions, claim liability, advisability of prosecuting or defending lawsuits, or legal rights and obligations.
3. 3Interpret laws, rulings and regulations for individuals and businesses.
4. 4Analyze the probable outcomes of cases, using knowledge of legal precedents.
5. 5Present evidence to defend clients or prosecute defendants in criminal or civil litigation.
6. 6Supervise legal assistants.

To measure benchmark coverage, we start with a list of 29 benchmarks selected for their quality and economic relevance. (The full list and selection criteria are in theBenchmark Indextab). In selecting benchmarks for this list, we prioritized:

* Public Availability.Included benchmarks have at least 25 publicly available tasks. We also include Mercor’s APEX benchmarks, where we have access to held-out benchmark prompts and are therefore able to map them to O*NET tasks.
* Agentic Tasks.Included benchmarks ask models to perform agentic tasks, rather than answering questions or advising the user on how to complete a task.
* Economic Realism.Benchmark tasks resemble tasks which humans (or agents) are frequently asked to do in real-world enterprises. Economically valuable tasks are prioritized over academically complex ones.
* Economic Diversity.We capped the number of included benchmarks per job family, in significant part to account for the massive overrepresentation of software engineering and research tasks in popular benchmarks.
* Balanced Difficulty.Benchmarks are not yet saturated by frontier models.

Following work byWang et al., we then ask an LLM judge to tag each benchmark prompt with as many O*NET tasks as it thinks correspond to that prompt. We validate our LLM tagging withhuman expert tagson Mercor’s APEX benchmarks, a subset of this list of 29. On the Benchmark Map, an O*NET task counts as “covered” if our LLM judge has mapped it to at least 5 prompts from our 29 benchmarks.

To estimate the total share of working hours Americans spend on tasks covered by benchmarks on this list, we combine our coverage estimates withHatgis-Kessell et al.’s LLM-derived estimates of the working time share of each O*NET task.

A more detailed account of our methodology can be found in theMethodologytab.

## Limitations

Our estimates of total economic coverage, and of patterns in coverage, all come from the initial list of 29 benchmarks we chose. This is not a complete or perfectly representative sample of the broader universe of unsaturated, public, agentic economic benchmarks. Any incomplete list will necessarily bias down estimates of economic coverage, and it is difficult to bound that bias. We want to stress, therefore, that these results are provisional. We will update them as we expand the initial benchmark list.

We also capped the number of included benchmarks in each job family in order to maximize breadth of coverage. We think this makes our estimate of economy-wide benchmark coverage more accurate, at the cost of biasing down our estimates of coverage in the most-benchmarked job families (e.g. software engineering).

By selecting for unsaturated benchmarks, we risk understating benchmark coverage on O*NET tasks which are easier for LLMs to complete. On the other hand, including saturated benchmarks would risk overstating benchmark coverage if saturation is downstream of lower task realism. The latter claim seems likely, given that benchmarks often overstate LLM performance in real-world deployments. We think that the bias from including saturated benchmarks would be greater than the bias from excluding them, but neither option is ideal.

Finally, while we outline our benchmark selection criteria in theBenchmark Indextab, several criteria (like “Economic Realism”) are difficult to formalize and introduce some subjectivity in our choices.

## Patterns in coverage

The benchmarks in our index have relatively deep and narrow coverage of the overall economy. They disproportionately focus on the economic tasks most exposed to AI automation (as measured byEloundou et al.), with O*NET tasks rated as “exposed” about 6x more likely to be represented on benchmarks than tasks rated “unexposed”. This makes sense: benchmarks are designed to measure AI progress, and AI progress is most plausible on the most AI-exposed tasks. This explains why benchmarks are full of tasks in Software Engineering and Financial Analysis while sparse on tasks in Truck Driving and Gas Plant Operation.

But even after controlling for AI-exposure,O*NET tasks from occupations with larger wage bills are significantly overrepresented among benchmark prompts:

Benchmark coverage of O*NET tasks by occupation wage bill
* High AI exposure
* Low AI exposure

Adjusted probability of task coverage

0
%
5
%
10
%
15
%
20
%
High AI exposure
Low AI exposure
$500m
$1bn
$2bn
$5bn
$10bn
$20bn
$50bn

Annualized occupation wage bill (log scale)

Each point shows the estimated probability that an O*NET task with a given AI-exposure tag belonging to an occupation with a given wage-bill will be covered by at least 5 prompts in our benchmark index. AI-exposure tags are binary and come fromEloundou et al. (2023). Occupation wage-bills are calculated from BLS estimates of the mean wage and number of Americans working in each occupation, assuming a 40 hour work week. Estimated coverage probabilities come from a task-level logistic regression of coverage probability on AI-exposure and log occupational wage bill. Error bars are pointwise 95% delta-method confidence intervals based on standard errors clustered at the occupation group level.

After controlling for occupation and AI-exposure score, O*NET “task importance” is another predictor of benchmark coverage. In particular, O*NET tasks come with domain expert estimates of the importance of the task for its occupation on a scale of 1-5. We find that the tasks scored most important are about 6–10x more likely to be represented on benchmarks than those scored least important:

Benchmark coverage by O*NET task importance within occupations
* High AI exposure
* Low AI exposure

Adjusted probability of task coverage

0
%
5
%
10
%
15
%
20
%
High AI exposure
Low AI exposure
3.25
3.50
3.75
4.00
4.25
4.50
4.75

O*NET task importance (1–5 rating scale)

Each point shows the estimated probability that, controlling for occupation, an O*NET task with a given AI-exposure tag and a given quintile O*NET importance score is covered by at least 5 prompts in our benchmark index. AI-exposure tags are binary and come fromEloundou et al. (2023). Importance quintiles are calculated from O*NET importance scores. Estimated coverage probabilities come from a task-level logistic regression of coverage probability on AI-exposure and importance quintiles, with occupation fixed effects. Error bars are pointwise 95% delta-method confidence intervals based on standard errors clustered at the occupation group level.

The plots above suggest a reasonable allocation of the relatively limited resources devoted to high-quality, economically relevant benchmarks so far; it’s natural to prioritize making benchmarks which cover the most important and AI-exposed tasks in the occupations with the largest wage bills. But barring a significant increase in the number and diversity of such benchmarks, these patterns will result in significant blind spots in our view of economically valuable model capabilities.

## Can O*NET + benchmarks tell us how good AI is at your job?

Measuring model capabilities by job occupation is essential – for enterprises deciding which models fit their needs, for policymakers forecasting the economic impact of AI, and for Americans thinking about their careers. Unfortunately, this is a hard problem to solve.

We could just try averaging model performance on all benchmark prompts relevant to a given job. But as ourBenchmark Mapsuggests, benchmarks cover some economic tasks much more intensively than others. A simple average would give too much weight to frequently benchmarked tasks.

O*NET offers a way to potentially reduce this bias. If we average model performance on occupation-relevant benchmark prompts weighted by O*NET classification, so thateach O*NET task is equally weighted in our occupation average, we get a step closer to a number that represents real economic performance.

As a first step, we try this approach onMercor’s APEX benchmarksfor four occupations: investment banking, law, accounting, and software engineering. We compare O*NET-weighted scores to simple averages of model performance on tasks related to each occupation. The resulting weighted and unweighted scores are generally quite similar:

Investment banking
Law
Accounting
Software engineering

APEX-1 + APEX-Agents· O*NET:Financial and Investment Analysts·11tasks ·176prompts

All
Every prompt counts equally
Every O*NET task counts equally
Score (%)
Every prompt counts equally
Every O*NET task counts equally
Claude Fable 5.1 Max
69.8%
68.5%
Claude Opus 5.5 Max
73.3%
70.2%
Claude Opus 5 Max
65.5%
63.0%
GPT-6 Astra Max
65.5%
61.8%
GPT-5.6 Sol Max
66.8%
65.6%
Grok 4.7 xHigh
58.1%
58.7%
Gemini 3.8 Flash High
66.9%
67.5%
Kimi K3 Max
59.4%
59.9%
DeepSeek V4.1 Flash Max
56.5%
58.4%

Claude Fable 5.1Max

69.8%
68.5%

Claude Opus 5.5Max

73.3%
70.2%

Claude Opus 5Max

65.5%
63.0%

GPT-6 AstraMax

65.5%
61.8%

GPT-5.6 SolMax

66.8%
65.6%

Grok 4.7xHigh

58.1%
58.7%

Gemini 3.8 FlashHigh

66.9%
67.5%

Kimi K3Max

59.4%
59.9%

DeepSeek V4.1 FlashMax

56.5%
58.4%
10
%
20
%
30
%
40
%
50
%
60
%
70
%
80
%
90
%

Score (%)

For each occupation, we take all prompts across APEX benchmarks related to that occupation. Darker bars show a simple average of model scores on those prompts for each occupation. Then, we sort the prompts by O*NET task. For each O*NET task with at least 5 corresponding APEX prompts, we average model scores on those prompts to get a task-level score. Next, we average each task-level model score to get occupation-level scores which weight performance on each O*NET task equally. (If an O*NET task has fewer than 5 prompts, we drop it from the average). Lighter bars show these weighted scores for each occupation.

In this case, at least, O*NET weighting changes very little. Model performance on APEX prompts is similar across the O*NET tasks included in the weighted scores above, which limits the value of reweighting. However, less than ⅓ of the O*NET tasks relevant to the 4 occupations above have enough APEX coverage to be included in our weighted scores. We are hopeful that applying O*NET weighting to a much larger set of benchmarks will result in high-quality occupation-specific model scores, and are working toward that goal.

However, even if we incorporate tasks from dozens of benchmarks, several obstacles remain:

1. 01### How do we navigate low statistical power?The sheer breadth of work done in the US economy means that for any O*NET occupation and task, we have relatively few benchmark items. This means that our estimates are inherently underpowered, and just one or two low-quality items can severely bias our scores.
2. 02### How do we account for the varying difficulty and fidelity of tasks?Some benchmark items are highly saturated, whereas others are still unsolved. This is partly a function of time (as older benchmarks were designed for less performant models and simpler environments) and partly a function of quality (some benchmark items are simplistically graded, have minor mistakes, or can be reward hacked). We do not yet have an explicit way of weighting by quality.
3. 03### Can evals that primarily measure AI automation generalize to augmentation?In the real world, AI models are still primarily used by humans, rather than automating entire job functions end-to-end. Therefore, measuring the real-world occupation capabilities of a model should ideally include measuring how much the model augments human productivity. We have completed someearly work in this direction, but finding a methodology that scales remains elusive.
4. 04### Can every O*NET occupation and task be measured with benchmarks?Knowledge-based work is well-suited to measurement through benchmarks because it is largely done on digital machines, like laptops and phones.Dingel and Neimanestimate that only 37% of US jobs could feasibly be done entirely from home, suggesting that ~63% of jobs involve some tasks with a physical-world component which would be hard to incorporate into current benchmarks. For now, this may not be a meaningful oversight – with the rapid development of robotics capabilities, we anticipate a significant need for physical task benchmarks.

We are actively working on these problems; if you are too, pleasereach out!

We are indebted toWang et al.for the O*NET tagging methodology, and thank Nathan Lambert for feedback on a draft of this work.

APEX NEWSLETTER

## The latest on frontier AI performance, straight to your inbox.

New benchmarks, leaderboard shifts, and research from the APEX team.

Email address
Subscribe

By subscribing, you agree to receive updates from Mercor.Unsubscribe anytime.

Experts
Find work
Explore listings
Help center
Resources
Stories
Research
APEX Benchmarks
APEX-Agents
APEX-Accounting
APEX-SWE
Off-the-shelf data
US Benchmark Map
Enterprise
Enterprise AI
Human data
Data monetization
Robotics
Contact sales
Company
Mission
Careers
Security
Newsroom
Blog
© 2026 Mercor
Terms of Service
Privacy Notice
Your Privacy Choices
San Francisco, CA
---
title: AI evals are becoming the new compute bottleneck
url: https://huggingface.co/blog/evaleval/eval-costs-bottleneck
site_name: tldr
content_file: tldr-ai-evals-are-becoming-the-new-compute-bottleneck
fetched_at: '2026-05-01T03:52:37.112839'
original_url: https://huggingface.co/blog/evaleval/eval-costs-bottleneck
date: '2026-05-01'
description: A Blog post by EvalEval Coalition on Hugging Face
tags:
- tldr
---

Back to Articles
 

# AI evals are becoming the new compute bottleneck

 
Team
 
Article
 
Published
				April 29, 2026
 
 
 
 Upvote 
11
 
 
* +5
 
 
 
 
Avijit Ghosh
 
evijit
 
 
Follow
 
 
 
evaleval
 
 
Yifan Mai
 
yifanmai
 
 
Follow
 
 
 
evaleval
 
 
Georgia Channing
 
cgeorgiaw
 
 
Follow
 
 
 
evaleval
 
 
Leshem Choshen
 
borgr
 
 
Follow
 
 
 
evaleval
 
 
 

Summary.AI evaluation has crossed a cost threshold that changes who can do it. The Holistic Agent Leaderboard (HAL) recently spent about $40,000 to run 21,730 agent rollouts across 9 models and 9 benchmarks. A single GAIA run on a frontier model can cost $2,829 before caching.Exgentic's $22,000 sweep across agent configurations found a 33× cost spread on identical tasks, isolating scaffold choice as a first-order cost driver, andUK-AISIrecently scaled agentic steps into the millions to study inference-time compute. In scientific ML, The Well costs about 960 H100-hours to evaluate one new architecture and 3,840 H100-hours for a full four-baseline sweep. While compression techniques have been proposed for static benchmarks, new agent benchmarks are noisy, scaffold-sensitive, and only partly compressible. Training-in-the-loop benchmarks are expensive by construction, and when you try to add reliability to these evals, repeated runs further multiply the cost.

## Making static LLM benchmarks cheaper

The cost problem started before agents. When Stanford's CRFM releasedHELMin 2022, the paper's own per-model accounting showed API costs ranging from $85 for OpenAI's code-cushman-001 to $10,926 for AI21's J1-Jumbo (178B), and 540 to 4,200 GPU-hours for the open models, with BLOOM (176B) and OPT (175B) at the top end.Perlitz et al. (2023)restate the larger HELM cost pattern, andIBM Researchnotes that putting Granite-13B through HELM "can consume as many as 1,000 GPU hours." Across HELM's 30 models and 42 scenarios, the aggregate of reported costs and GPU compute came to roughly $100,000.

Another shocking observation came fromPerlitz et al.'s analysisofEleutherAI's Pythiacheckpoints: developers pay for evaluation repeatedly during model development. Pythia released 154 checkpoints for each of 16 models spanning 8 sizes, or 2,464 checkpoints if each model checkpoint is counted separately, so the community could study training dynamics. Running the LM Evaluation Harness across all those checkpoints turns eval into a multiplier on training:Perlitz et al. (2024)noted that evaluation costs "may even surpass those of pretraining when evaluating checkpoints." For small models, evaluation becomes the dominant compute line item across the whole development cycle. When we scale inference-time compute, we scale evaluation costs.

Perlitz et al. then asked how much of HELM actually carried the rankings. The result was striking: a 100× to 200× reduction in compute preserved nearly the same ordering, with larger reductions still useful for coarse grouping under the paper's tiered analysis. Flash-HELM turned that finding into a coarse-to-fine procedure: run cheap evaluations first, then spend high-resolution compute only on the top candidates. Much of HELM's compute was confirming rankings that the field could have inferred much more cheaply.

Other work reached the same conclusion from different angles.tinyBenchmarkscompressed MMLU from 14,000 items to 100 anchor items at about 2% error using Item Response Theory. The Open LLM Leaderboard collapsed from 29,000 examples to 180.Anchor Pointsshowed that as few as 1 to 30 examples could rank-order 87 language-model/prompt pairs on GLUE, andothersfollowed, reducing dataset sizes by 90\%. Static benchmarks had a weakness you could exploit: model differences often concentrate in a small subset of items, so ranking can survive aggressive subsampling.

That trick weakened sharply once benchmarks moved from static predictions to agents.

## Agent evals are messier

A very nice public accounting of agent evaluation comes from theHolistic Agent Leaderboard(Kapoor et al., ICLR 2026). HAL runs standardized agent harnesses across nine benchmarks covering coding, web navigation, science tasks, and customer service, with shared scaffolds and centralized cost tracking. The headline cost: $40,000 for 21,730 rollouts across 9 models and 9 benchmarks. By April 2026, the leaderboard had grown to 26,597 rollouts.Ndzomga's independent reproductionarrives at almost the same number: $46,000 across 242 agent runs.

Behind that aggregate, the cost of a single benchmark run varies by four orders of magnitude across HAL tasks, and by three orders within some individual benchmarks.

Figure 1.
 Each bar shows the minimum-to-maximum cost across HAL configurations on a single benchmark. Highlighted bars cross the round $1,000-per-run threshold. A "run" is one full agent evaluation across all tasks. Within-benchmark spread reflects the model × scaffold × token-budget product. Source: live HAL leaderboard, April 2026.

Behind these numbers is a blunt pricing fact. Claude Opus 4.1 charges $15 per million input tokens and $75 per million output. Gemini 2.0 Flash charges $0.10 and $0.40, a two-order-of-magnitude spread on input alone. Agent benchmarks rarely benchmark "the model" in isolation. They benchmark a model × scaffold × token-budget product, and small scaffold choices can multiply costs 10×.

Worse, higher spend does not reliably buy better results. OnOnline Mind2Web, Browser-Use with Claude Sonnet 4 cost $1,577 for 40% accuracy. SeeAct with GPT-5 Medium hit 42% for $171. The HAL paper notes "a 9× difference in cost despite just a two-percentage-point difference in accuracy." OnGAIA, an HAL Generalist with o3 Medium cost $2,828 for 28.5% accuracy, while a different agent hit 57.6% for $1,686.CLEARfinds across 6 SOTA agents on 300 enterprise tasks that "accuracy-optimal configurations cost 4.4 to 10.8× more than Pareto-efficient alternatives" with comparable real-world performance.

The static-era toolkit should have helped, but it has only gone so far. Ndzomga's mid-difficulty filter, which selects tasks with 30 to 70% historical pass rates, achieves a 2× to 3.5× reduction while preserving rank fidelity under scaffold and temporal shifts. That is useful, but it falls far short of the 100× to 200× gains available for static benchmarks. When each item is a multi-turn rollout with its own variance, the unavoidable long trajectory per single question becomes the expensive object.

## Some evals are just training

Some benchmarks escape the API-cost framing altogether because their evaluation protocol trains models from scratch.

The Wellgives a very interesting example of this. It bundles 16 scientific machine-learning datasets spanning biological systems, fluid dynamics, magnetohydrodynamics, supernova explosions, viscoelastic instability, and active matter, totaling 15 TB. Using the paper's headline 16-dataset grid, the protocol leaves little room to economize: train each baseline model for 12 hours on a single H100, try five learning rates per (model, dataset) pair, repeat across four architectures and 16 datasets. That headline-grid sweep consumes 3,840 H100-hours, or roughly $9,600 under the conversion assumptions below. A single new architecture still costs about 960 H100-hours, or about $2,400.

Training one neural operator can take a single 12-hour H100 run, while evaluating it across the benchmark requires 80 such trainings. That asymmetry is what makes The Well important. In this corner of ML, evaluation compute exceeds training compute by roughly two orders of magnitude, reversing the old deep-learning mental model.

The same pattern recurs across SciML.PDEBenchcovers 11 PDE families and reports per-epoch timing tables across datasets and model families, but a clean per-architecture dollar figure depends on the chosen training protocol and hardware.MLE-Bench(OpenAI) sits between agent and training regimes. Each agent attempt at one of 75 Kaggle competitions runs 24 hours on a single A10 GPU, training real ML pipelines. The paper is explicit: "A single run of our main experiment setup of 24 hours per competition attempt requires 24 hours × 75 competitions = 1,800 GPU hours of compute," plus o1-preview consuming 127.5M input and 15M output tokens per seed. At $1.50 per A10-hour, the GPU floor alone is $2,700; adding o1-preview API usage brings a one-seed run to roughly $5,500. Three seeds × six models would therefore land near $100,000 before any additional grading or retry overhead.

METR's RE-Benchcaps each of seven research engineering environments at 8 hours on 1 to 6 H100s. A single pass across the suite is therefore 56 to 336 H100-hours before adding repeated attempts, multiple seeds, or multiple agents; the human baseline, with 71 expert attempts, raises the implicit budget much further. Because the benchmark gives agents and humans the same wall-clock compute, a real-time training process sets the cost floor. A token budget no longer bounds it from above.

ResearchGym(ICLR 2026) makes the agent run actual ML research. Five test tasks (39 sub-tasks) drawn from ACL, ICLR, and ICML papers, including ACL Highlights, ICML Spotlight, ICLR Spotlight, and ICLR Oral categories, with the proposed methods withheld. The agent has to propose hypotheses, train models, and beat the original authors' baselines. The budget is tight: $10 in API plus 12 to 24 hours on a single GPU under 24 GB per task. A full pass (5 tasks × 24h × 3 seeds) consumes about 360 GPU-hours per agent.

The cost picture turns brutal inPaperBench. Twenty ICML 2024 Spotlight or Oral papers must be replicated from scratch, graded against rubric trees with 8,316 leaf-node criteria. Each rollout uses an A10 GPU for 12 hours, and the per-paper math is straightforward:

* $400 in API per o1 IterativeAgent rollout, times 20 papers, comes to about $8,000 per evaluation.
* Grading runs $66 per paper with the o3-mini judge, or $1,320 for the full benchmark.
* Using o1 as judge would push grading to about $830 per paper.

PaperBench Code-Dev drops execution on purpose. That choice halves rollout cost to about $4,000 and cuts grading to $10 per paper (85% lower). OpenAI built the variant because many groups cannot afford the full benchmark.

The historical precedent isNAS-Bench-101, whose tabular construction required over 100 TPU-years of training. Without that one-time investment, every NAS algorithm comparison would have cost 1 to 100+ GPU-hours per run, which would have made comparison pricier than the algorithms themselves.

Figure 2.
 All values in USD per single evaluation of one model or agent through the full benchmark protocol. GPU costs converted at $2.50/H100-hr, $1.50/A10-hr; API and grading costs included where applicable. Highlighted bars denote benchmarks costing at least the round $5,000-per-evaluation threshold. The most expensive of these match the most expensive agent benchmarks (Figure 1) and require GPU compute that has no API substitute.

As benchmarks move closer to real work, compression gets harder: static prediction leaves room for large savings, agent rollouts leave less, and in-the-loop training leaves almost none.

Figure 3.
 The toolkit for compressing evaluation does not transfer as benchmarks become more complex. Bars show the maximum measured compression that preserves model-rank fidelity; labels give the published range. The highlighted bar flags the ~1× baseline where no general compression method exists. Static benchmarks routinely compress 100–200× without losing rankings. Agent benchmarks compress 2–3.5× at best. Training-in-the-loop benchmarks resist subsampling because the unit being evaluated 
is
 the trained model.

## Reliability is the expensive part

Most of the costs above buy only single-run measurements with limited statistical power. When you measure reliability across repeated runs, static benchmarks, agent benchmarks, and training-in-the-loop benchmarks all become more expensive.

Agent reliability can fall hard when you stop treating one run as evidence. The best-known example comes from Yao et al.'s τ-bench, later reframed in CLEAR (Mehta, 2025): performance can drop from 60% on a single run to 25% under 8-run consistency.Kapoor et al.'s "AI Agents That Matter"found that simple baseline agents Pareto-dominate complex SOTA agents (Reflexion, LDB, LATS) on HumanEval at 50× lower cost. Their holdout analysis found that 7 of 17 benchmarks had no holdout set; among the 10 that did, only 5 held out tasks at the appropriate level of generality, so 12 of 17 failed their holdout criterion overall. The HAL paper notes that a "do-nothing" agent passes 38% of τ-bench airline tasks under the original construction. HAL's own log analysis revealed data leakage in the TAU-bench Few Shot scaffold, forcing its removal in December 2025.

Another recent reliability accounting comes fromRabanser, Kapoor et al.'s "Towards a Science of AI Agent Reliability", which proposes twelve metrics across consistency, robustness, predictability, and safety. Their finding: "recent capability gains have only yielded small improvements in reliability." HAL's internal analysis shows how much fragility hides behind aggregate accuracy. On SciCode and CORE-Bench, agents almost never completed a run without a tool-calling failure. On AssistantBench and CORE-Bench, environmental errors occurred in roughly 40% of runs. Agents violated explicit benchmark instructions in their final answer over 60% of the time on failed tasks.

A statistically credible HAL-style evaluation with k = 8 reruns per cell takes the $40K aggregate to roughly $320K. The same multiplier on PaperBench's $9,500-per-run cost pushes a single agent's evaluation past $75K, and on The Well, a multi-seed protocol takes the per-architecture cost from ~960 H100-hours to several thousand. Reliability acts as a multiplier on every cost category above.

HAL has paused new model evaluations to focus on reliability: the field's headline numbers still carry too much noise, and reducing that noise costs real money. And the figures above are lower bounds; many evaluators are already priced out.

## What this means for ML as a field

### Eval cost is now an accountability barrier

Academic groups, AI Safety Institutes, and journalists now hit the budget constraint before the technical one when they try to evaluate frontier agents independently. A single GAIA run can exceed an annual graduate student travel budget. A single PaperBench evaluation, including the LLM judge, runs about $9,500. Three-seed comparisons of six models, the kind of study one might publish, push above $150,000. The established practice of "running a benchmark once and reporting the accuracy number" has roughly the rigor of crash-testing one car in perfect weather. Moving past it requires money the academic system does not currently allocate as research compute.

### The compute divide now includes evaluation

Ahmed, Wahed and Thompson (Science 2023)documented that industry models in 2021 were 29× larger than academic ones by parameter count, and that about 70% of AI PhDs went to industry in 2020 versus 21% in 2004. The original "compute divide" story mostly ignored evaluation because evaluation used to look cheap next to training. Many benchmarks have reversed that relationship. A lab that can fine-tune a 7B model can no longer assume it can afford the benchmarks the field takes seriously.

### Cost-blind leaderboards reward waste

When leaderboards report raw accuracy and omit cost, researchers can rationally pour tokens into a problem until the number ticks up. The HAL paper finds that higher reasoning effort actually reduces accuracy in the majority of runs: extra inference compute does not reliably improve even the metric it is supposed to optimize. Pareto frontiers fix the comparison by ranking accuracy against cost. HAL implements them, but most leaderboards still do not.

If only frontier-lab compute budgets can produce statistically reliable benchmark numbers on the highest-cost agentic and scientific benchmarks, the social process of evaluating AI systems becomes concentrated inside the same labs that build them, rendering external validation partial, and sometimes absent, unless someone subsidizes the cost directly.

## Cost summary across benchmark types

Benchmark

Type

USD per single evaluation

What "one evaluation" means

HELM (per LLM, 2022)
Static LLM
$85 – $10,926 API; 540 – 4,200 GPU-hrs open
One LLM through 42 scenarios; per-model table in HELM §6 p. 43

ScienceAgentBench
Agentic, science
$0.19 – $77
One agent config across 102 tasks

TAU-bench Airline
Agentic
$0.31 – $180
One agent across all airline tasks

SciCode
Agentic, science
$0.12 – $625
One agent across 338 sub-problems

CORE-Bench Hard
Agentic, replication
$2 – $510
One agent across 45 papers

SWE-bench Verified Mini
Agentic, coding
$4 – $1,600
One agent across 50 issues

Online Mind2Web
Agentic, web
$5 – $1,610
One agent across 300 web tasks

GAIA
Agentic, multimodal
$7.80 – $2,829
One agent across GAIA tasks

ResearchGym (full pass)
ML research, training
$540 – $1,260
5 tasks × 24h × 3 seeds (~360 GPU-hrs) + API

RE-Bench (single pass)
ML R&D, training
$140 – $840
7 environments × 8h × 1–6 H100s

The Well (per architecture)
SciML, training
~$2,400
Headline 16-dataset grid: 5 LRs × 16 datasets × 12h H100

MLE-Bench (1 seed)
ML R&D, training
~$5,500
75 Kaggle competitions × 24h on A10 + o1-preview API

PaperBench Code-Dev
Scientific, code only
~$4,200
One agent across 20 papers, no execution

The Well (full sweep)
SciML, training
~$9,600
4 architectures under the headline 16-dataset grid

PaperBench (full)
Scientific
~$9,500
One agent across 20 papers, full protocol

HAL aggregate
9 benchmarks × 9 models
~$40,000
All 81 cells, single seed each

All figures normalized to USD per single evaluation. GPU compute converted at $2.50/H100-hour, $1.50/A10-hour; API and grading costs included where applicable. Pythia ("eval can exceed pretraining"), PDEBench (per-architecture cost depends on the selected training protocol and hardware), and NAS-Bench-101's 100 TPU-year construction cost are excluded because they do not normalize cleanly to a per-evaluation USD figure.

## Stop paying twice for the same eval

One reason these numbers stay high is that the field keeps re-running the same evaluations. A frontier lab pays for a HAL sweep, an academic group pays again for a partial reproduction, an audit organization pays a third time for the model versions it cares about, and a journalist pays a fourth to spot-check the leaderboard. Most of those runs cover overlapping models on overlapping benchmarks. Almost none of the underlying instance-level outputs end up in a place where the next team can build on them, because results get reported as a single accuracy number in a PDF, in a model card table, or in a leaderboard entry that hides scaffold, prompt, and seed. The cost figures above are large in part because the field is paying retail every time, on artifacts the rest of the community could not reuse if it wanted to.

Standardized documentation is the cheapest lever available here, and it is the one reliability work needs anyway. If a $9,500 PaperBench rollout exports its full grading trace in a shared schema, the next group studying the same papers can spend its budget on new perturbations instead of repeating the baseline. If a multi-seed HAL run publishes per-trajectory tool-call logs, agent reliability research can answer questions that a single accuracy number cannot. The saving compounds: even a 2× reuse rate on the high-cost benchmarks would put more money back in the ecosystem than every compression technique combined.

Sharing Eval Data.
 The EvalEval Coalition's 
Every Eval Ever
 project is the standardized format we use for this. It bundles a metadata schema, validators, and converters from popular harnesses such as 
HELM
, 
lm-eval-harness
, and 
Inspect AI
, so existing eval logs can be transformed into a shared format with one step. The community repository on 
Hugging Face
 already hosts results from dozens of contributors, with an open 
Shared Task
 for adding more. If you ran one of the costly evaluations in this post, depositing the artifacts in a unified, transparent, verifiable and reproducible manner is the highest-leverage cost-reduction move available to the rest of the field. Additionally, if your benchmark is on Hugging Face, you can also expose your results on hub leaderboards and model pages via 
Community Evals
!

## Where this leaves us

The economics have changed. Not long ago, training was expensive and evaluation was cheap. For frontier LLMs trained at $50 million to $100 million, evaluation still looks like a rounding error, but that rounding error now costs tens of thousands of dollars per benchmark run and often leaves noisy results behind. For neural operators, ML research agents, and replication benchmarks, the ratio has flipped: a credible evaluation can cost more than training the candidate model.

We already know how to make static evaluation cheaper. Flash-HELM, tinyBenchmarks, and Anchor Points work. Agent evaluation has only partial fixes: mid-difficulty filtering helps, and Pareto-front leaderboards help, but the toolkit remains thin. Training-in-the-loop evaluation has no general compression method; tabular precomputation and tight budget caps can reduce cost only by narrowing what the benchmark measures. Reliability adds another layer because repeated runs raise the price of every protocol.

The field still talks as if capability sets the main constraint, but evaluation points to reliability as the tighter one. Governance institutions should want to measure the gap between single-run accuracy and pass^k consistency, yet that gap costs the most to measure. Static-benchmark compression does not transfer to agent or training-in-the-loop benchmarks, and mid-difficulty filtering remains the only credible partial substitute. Cost-blind leaderboards now mislead by design, because they reward extra spending without reporting what that spending bought.

Evaluation now has its own compute budgets, statistical methods, and failure modes. Its price also shapes who gets to evaluate powerful systems in the first place. Whoever can pay for the evaluation gets to write the leaderboard.

Sources

1. Ying et al. (2019).NAS-Bench-101: Towards Reproducible Neural Architecture Search.arXiv:1902.09635.
2. Liang et al. (2022).Holistic Evaluation of Language Models.arXiv:2211.09110.
3. Takamoto et al. (2022).PDEBench: An Extensive Benchmark for Scientific Machine Learning.arXiv:2210.07182.
4. Ahmed, Wahed and Thompson (2023).The growing influence of industry in AI research.Science 379(6635).
5. Biderman et al. (2023).Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.arXiv:2304.01373.
6. IBM Research (2023).Efficient LLM Benchmarking.research.ibm.com.
7. Perlitz et al. (2023).Efficient Benchmarking of Language Models.arXiv:2308.11696.
8. Vivek et al. (2023).Anchor Points: Benchmarking Models with Much Fewer Examples.arXiv:2309.08638.
9. Chan et al. (2024).MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering.arXiv:2410.07095.
10. Chen et al. (2024).ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery.arXiv:2410.05080.
11. Kapoor et al. (2024).AI Agents That Matter.arXiv:2407.01502.
12. Wijk et al. (METR, 2024).RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents Against Human Experts.arXiv:2411.15114.
13. Ohana et al. (2024).The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning.arXiv:2412.00568.
14. Polo et al. (2024).tinyBenchmarks: evaluating LLMs with fewer examples.arXiv:2402.14992.
15. Siegel et al. (2024).CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark.arXiv:2409.11363.
16. Tian et al. (2024).SciCode: A Research Coding Benchmark Curated by Scientists.arXiv:2407.13168.
17. Kapoor et al. (2025).Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation.arXiv:2510.11977.
18. Li et al. (2025).Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks.arXiv:2511.04689.
19. Mehta (2025).Beyond Accuracy: A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems.arXiv:2511.14136.
20. Starace et al. (2025).PaperBench: Evaluating AI's Ability to Replicate AI Research.arXiv:2504.01848.
21. UK AISI (2025).Evidence for inference scaling in AI cyber tasks: increased evaluation budgets reveal higher success rates.aisi.gov.uk.
22. Bandel et al. (2026).General Agent Evaluation.arXiv:2602.22953.
23. Garikaparthi et al. (2026).ResearchGym: Evaluating Language Model Agents on Real-World AI Research.arXiv:2602.15112.
24. Ndzomga (2026).Efficient Benchmarking of AI Agents.arXiv:2603.23749.
25. Rabanser et al. (2026).Towards a Science of AI Agent Reliability.arXiv:2602.16666.
26. Holistic Agent Leaderboard (live).hal.cs.princeton.edu.

BibTeX Citation

@misc{ghosh2026evalbottleneck,
 author = {Ghosh, Avijit and Mai, Yifan and Channing, Georgia and Choshen, Leshem},
 title = {{AI} evals are becoming the new compute bottleneck},
 year = {2026},
 month = apr,
 howpublished = {EvalEval Coalition Blog},
 url = {https://evalevalai.com/research/2026/04/29/eval-costs-bottleneck/}
}

 
 
 

### Community

 
 
 
 
 
 
 
RodTAB
 
 
 
 
 
 
 
about 3 hours ago
 
 
 
 
 
 
 

I'm the solo founder of TAB Platform (tabverified.ai), an independent AI agent verification platform. We run 340+ benchmarks across 59 models from 5 providers at $0.03 per text test case. Pay-as-you-go credits, no subscription.

A few of your findings match what we've been measuring for 13 months:The 33x cost spread on scaffold choice lines up with our data. We tested Claude Opus with two different harness configurations on the same benchmark, same model, same test. 42% with one harness, 78% with another. We have 101 harness configurations measuring exactly this variable.

Your reliability point is critical. We built a Benchmark Calibration Suite with 10 synthetic agents and 5 adversarial gaming agents that runs daily (135/135 checks) specifically because single-run numbers aren't trustworthy. We also found 20-point variance on GPT-4o across 4 identical runs.

The conclusion that "whoever can pay for evaluation gets to write the leaderboard" is the reason TAB exists. Independent evaluation shouldn't require a frontier lab's compute budget.

Would be interested in comparing notes if any of you are open to it.Rod Millertabverified.airod@tabverified.ai

 
 
See translation
 
 
 
❤️
 
1
 
1
 
 
 
 
+
 
 
Reply
 
 
 
 
Edit
Preview
 
 
 
 
 
 
Upload images, audio, and videos by dragging in the text input, pasting, or 
clicking here
.
 
Tap or paste here to upload images
 
 
 
 
 
 
 
 Comment
 

·Sign uporlog into comment

 
 
 Upvote 
11
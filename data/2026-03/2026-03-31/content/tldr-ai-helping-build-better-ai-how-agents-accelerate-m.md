---
title: 'AI Helping Build Better AI: How Agents Accelerate Model Experimentation'
url: https://www.linkedin.com/blog/engineering/ai/ai-helping-build-better-ai-how-agents-accelerate-model-experimentation
site_name: tldr
content_file: tldr-ai-helping-build-better-ai-how-agents-accelerate-m
fetched_at: '2026-03-31T01:01:39.028558'
original_url: https://www.linkedin.com/blog/engineering/ai/ai-helping-build-better-ai-how-agents-accelerate-model-experimentation
date: '2026-03-31'
description: 'AI helping build better AI: How agents accelerate model experimentation (7 minute read)'
tags:
- tldr
---

AI

# AI helping build better AI: How agents accelerate model experimentation

Authored by
Animesh Singh

March 27, 2026

 

Co-authors:Co-authored byAnimesh Singh,Co-authored byJaideep Ray, 
 andCo-authored byNishant Garg

A meaningful shift is starting to emerge in AI. The technology is being used to build more than just products for users. It is also being used to improve the infrastructure, training workflows, and optimization systems used to help build AI itself.

We first saw this clearly in August 2025, when we began using agent loops to optimize LLM post-training runs. The early gains were encouraging, but the bigger takeaway was structural. These systems were not just automating tasks. They were running a loop of proposing changes, testing them, measuring results, and improving from one iteration to the next.

In January 2026, we incubated an internal project with a simple premise: AI can help build better AI systems, and the platforms behind those systems must be designed for a world where agents play a central role.

We developed a focused strategy to supercharge our AI iteration speed by seamlessly unifying three core pillars into one cohesive framework for experimentation at scale:

1. Agents for code authoring focused on distributed training.
2. Evaluation systems for measuring correctness, quality and overall progress.
3. GPU microscheduling for efficient use of compute.

Within this framework, agents can parallelize model trials with minimal human input on an interactive dev machine. In the inner loop, the agent optimizes for both model quality and training efficiency. Once the right model architecture is achieved, it is scaled via distributed training in an outer loop.

We soon began applying this framework to real model development workflows, starting with model framework migration. At LinkedIn, we have a large fleet of TensorFlow models. Our goal was not just to convert them, but to produce equivalent or better PyTorch models. That led to Autopilot for Torch, a specialized agent built for this workflow. It is not a one-time converter. It works through an iterative refinement loop, improving the generation step by step based on LLM reasoning and verifier feedback.

From there, the same pattern quickly expanded to other use cases, including kernel generation and auto-tuning, where agents can also search, evaluate, and improve system performance with minimal manual effort.

## The core loop: Generate → verify → refine

Autopilot for Torch doesn't stop until it hits the right metrics. It runs an interative generate → score → hint → regenerate loop. Each iteration is validated against explicit, rigorous quality gates, and the verifier doesn't just say'fail'—it returns concrete, actionable fixes. Once the targets are met, the PyTorch implementation is immediately validated on development GPU pods and promoted to production via Flyte workflows.

Figure 1 : From code generation to verifiable AI system building

We are applying autopilot to a class of engineering problems where the output is itself AI infrastructure, models, or performance-critical code.

* Framework migration, where agents convert TensorFlow pipelines and models into production-ready PyTorch.
* Model code generation, where agents generate and train a PyTorch architecture directly from a dataset containing features and labels.
* Autoresearch style experimentation, where agents explore model architecture choices such as number of layers, embedding size to improve model quality and training strategy and scaling settings to improve training efficiency.
* Kernel generation, where an agent helps generate and optimizes low-level GPU kernels for LLM and recsys training workloads.

The common thread is not just code generation, but verifiable system building. Each problem has clear correctness, quality, and performance checks, making it a strong fit for iterative agent loops that can generate, test, refine, and improve.

## The scoreboard: What defines a winning generation?

The core principle behind this system:trust, but verify. In practice, the scoreboard is not a reporting layer bolted on at the end. It is the mechanism that defines what “good” means for the agent loop. Reward design matters a great deal because the agent will optimize whatever the loop rewards. If the reward is shallow, the fixes will be shallow. If the reward reflects real production constraints, the loop becomes much more reliable.

There is a clear hierarchy inside the evaluation stack: functional correctness comes first. If the generated system does not run correctly, learn correctly, or behave stably under execution, the rest of the scores do not matter. A system that looks structurally correct, follows style conventions, or shows partial metric alignment is still not useful if it fails basic execution, produces unstable numerics, or cannot improve under training or optimization. Functional validity should therefore be treated as a hard gate, not just another weighted dimension.

Once that foundation is established, higher-level checks become meaningful. Behavioral parity verifies that the generated system preserves the expected outputs or semantics on representative inputs. Structural checks confirm that key components, interfaces, and design patterns are present and correctly assembled. Quality checks ensure the result fits the conventions and constraints of the target stack so that it remains maintainable and operationally usable. Task-level metrics then measure whether the system performs well in the way that actually matters for the application, whether that is model quality, latency, throughput, efficiency, or another production objective.

Verification itself should also become progressively harder over time. Early iterations can run cheap tests like structural and style checks to eliminate obvious errors quickly. Later iterations should face stronger gates: trainability, IO parity, numerical stability, and task-level metric parity. This progression makes the loop efficient while steadily increasing confidence in the result.

For example, the rubric of evaluating model code is:

1. Trainability: Does the model run, backpropagate, remain numerically stable, and converge?
2. IO Parity: Does it match the source model’s behavior on identical inputs?
3. Structural Fidelity: Does it preserve the architecture and key modeling patterns?
4. Code Style / Platform Fit: Does it align with target engineering conventions and APIs?
5. Task Metric Parity: Does it preserve downstream quality metrics such as AUC?

The loop should also reason about both failure and success. Failures tell the agent what broke. Successes tell it what is already correct and should be preserved. That context is important. It prevents the next iteration from blindly rewriting working components while chasing a single failing metric. In other words, the agent loop improves fastest when it uses verification not just as a pass/fail filter, but as a source of structured feedback. The result is a system that does not merely trust LLM generations, but continuously verifies them, prioritizes functional correctness, and uses reward signals to drive each iteration closer to production reality.

## Reinforcement drives better generations

Reinforcement in the loop comes from the verifier. Instead of returning only a pass or fail signal, the verifier produces structured natural-language feedback that acts like an evaluation rubric plus a coach. Its job is to tell the agent not just that the generation is weak, but exactly where it is weak and what should be fixed next.

Each piece of feedback is typed, prioritized and actionable. The issue is clearly categorized by failure mode, such as NO_GRADIENT, NUMERICAL_INSTABILITY, or METRIC_GAP. It is prioritized, so the loop knows which problems are blocking correctness and which are secondary refinements, typically from P1 for critical issues to P4 for minor improvements. It is also actionable, including the relevant metric, the current observed value, the expected target, and the suggested direction for the fix.

This matters because the quality of reinforcement determines the quality of improvement. If the verifier only emits vague failure messages, the loop will make vague fixes. If it emits precise, prioritized, and concrete signals, the loop can focus on the highest-value changes first. In practice, this means fixing hard blockers like trainability and stability before spending effort on structural cleanup, style alignment, or metric refinement.

A simple way to think about it is: the verifier turns evaluation into guidance. It translates rubric failures into targeted next actions, which is what allows the loop to improve code generation systematically rather than randomly.

To compliment the client side strategy, we led with a server side tracking tool. You can track the status ofallyour Autopilot for Torch runs—conversions, training jobs, and Flyte executions—through theAutopilot Tracking Console.

The console provides a centralized, single-pane view of:

* Active and completed conversions (ESR status, iteration, score progression)
* Training jobs (k8s pod status, evaluation metrics)
* Flyte executions (workflow status and error logs)
* Artifact links (direct links to PRs and generated files)

This becomes an important tool for monitoring long-running jobs, sharing victory reports with the team, and reviewing historical runs.

Figure 2: Autopilot loop for model generation.

## The design principles that power this system

In summary, we are seeing higher productivity, with more models going through agentic migration, auto-tuning, and design workflows with much less manual effort. Even at this early stage, the results are promising:

1. Autopilot-generated PyTorch code has performed strongly across open-source benchmarks, including more than 100 OpenML tasks, and has been able to match offline metrics for internal workloads.
2. For TensorFlow-to-PyTorch framework migration, we are already using agent generated model code as a starting point.
3. Auto-tuning helped in squeezing out 10%+ training throughput from already optimized LLM workloads.

The system works because of a few core design decisions.

### Scoring based iterative loop:

 

The agentic framework is built for speed, reliability, and tight feedback loop between the verifier and the LLM.

1. Verbal reasoning as feedback :The scoring system speaks the LLM's language. The hints are natural language with structured metadata, not just numbers the model has to guess at.
2. Fail fast, fix fast:Our active trainability probe catches catastrophic issues (dead gradients, NaN loss) quickly, eliminating the need to wait for a full, hours-long training run.
3. Modular scoring:Each scoring dimension is an independent, debuggable module, allowing us to rapidly add new checks without breaking the core loop.
4. Deterministic verification:The scoring is reproducible. The same code and same data will always result in the same score. The LLM generates, but verification is indisputable.
5. Bounded iteration:We've set a maximum iteration count (default 5) to prevent infinite loops. If the target isn't met, the best-scoring iteration is returned, ensuring we always have a high-quality result and a detailed report.

### Comprehensive Evals: The confidence builder

The only way to build real confidence is through stronger evals. Beyond offline metrics, the system needs to show that a generated model behaves consistently with production signals and points to a genuinely better model. At the center of this is an offline experiment system that runs an N-day replay, feeds recorded production traffic hour by hour, and checks parity against the baseline model currently serving in production.

### GPU microscheduling:

Last but not the least, it’s a strategy to do more with less, while massive experiments can be launched, GPU compute is not expanding automatically. This is a very focussed strategy of cost optimized GPU compute consumption.

This is an exciting field of work for us, and we hope to share additional details in future LinkedIn Engineering blogs.

## Acknowledgements:

This work reflects contributions from many team members across LinkedIn AI Infra, including:

Ethan Lyu, Lijuan Zhang, Yujie Ai, Zejun Lin, Daniel Tang, Haoyue Tang, Yang Pei, Tommy Li, Prathyusha Polepalli, Vaibhav Jindal, Arup De Feng Wen, Mahesh Ravindranathan, Bidhan Tamuli Ankit Goyal, Frank Gu, Shuying Liang, Yj Yang, Vikash Rai Chen Xie, Yitong Zhou, Souvik Ray, Ketan Thakkar.

Topics:AIArtificial intelligenceInfrastructure

Related articles

* AIThe LinkedIn Generative AI Application Tech Stack: Personaliza...Praveen Kumar BodigutlaMar 26, 2026
* FeedEngineering the next generation of LinkedIn’s FeedHristo DanchevMar 12, 2026
* TalentDriving data enhancement & recruitment success with LinkedIn’s...Aditya HegdeMar 10, 2026
---
title: Agent Reliability Needs Repeated Evidence | Jason Doyle
url: https://jasondoyle.ie/whitepapers/agent-reliability-needs-repeated-evidence
site_name: tldr
content_file: tldr-agent-reliability-needs-repeated-evidence-jason-do
fetched_at: '2026-09-16T21:54:45.246848'
original_url: https://jasondoyle.ie/whitepapers/agent-reliability-needs-repeated-evidence
author: Jason Doyle
date: '2026-09-16'
published_date: '2026-09-16'
description: How repeated runs define operating boundaries for probabilistic agent workflows.
tags:
- tldr
---

Disclosure: These views are my own and do not represent my current or any former employers. This paper uses only public sources and does not describe non-public product information.

## Executive summary

An agent can look strong in an average success score and still be difficult to rely on for repeated work.

IBM Research measured this directly on the AppWorldtest_normalbenchmark. A ReAct agent using GPT-4.1 completed 77.4 per cent of runs across five executions, reported as Mean@5. It completed all five executions for only 53.0 per cent of tasks, reported as Pass^5. IBM calls the 24.4 percentage-point difference the consistency gap.[1][2]

The result matters because production agents are increasingly expected to perform work rather than answer isolated questions. Their output may update a system of record, send a message, change access, reconcile an account, or continue a goal over several days. Salesforce has announced a long-horizon runtime intended for work that spans days and weeks.[13] A benchmark score averaged across runs does not tell an operator whether the same class of intent will complete acceptably each time, whether failures concentrate in certain task structures, or when the runtime should stop acting without another check.

Repeated success is useful production evidence, although reliability requires more than repeatability.

Pass^k becomes stricter askincreases. It can fall even when every run is drawn from a stable distribution. A consistent answer can also be wrong. Another 2026 study found that unanimous agreement across repeated agent runs improved accuracy when used as an abstention signal, while 5.5 to 10 per cent of tasks remained consistently wrong.[5] Consistency must be combined with outcome quality, robustness, predictability and safety.[6]

The simple expressionp^nis also easy to misuse. If every transition had the same independent success probabilityp, and any wrong transition caused unrecoverable workflow failure, then a workflow withntransitions would succeed with probabilityp^n. Real agent trajectories do not satisfy those assumptions. Decision risks vary, failures correlate, some divergences are harmless, and recovery can restore a valid outcome. Recent long-horizon research also warns that task horizon cannot be normalised by step count alone.[8]

This paper proposes a narrower operating model:

1. Measure a reliability profile rather than one agent score.
2. Define the subject of the profile precisely: task class, action class, model and runtime version, environment, dependency set, intervention policy and time window.
3. Report average outcome yield and strict repeated success together.
4. Measure consistent-wrong outcomes separately.
5. Stratify results by task structure and operational consequence.
6. Define an operating boundary where simultaneous lower and upper confidence bounds meet policy.
7. Change the intervention policy outside that boundary through deterministic validation, replay, checkpointing, human approval or refusal.
8. Use observed SLO misses over time to govern how much autonomous work is admitted.

This differs from subtracting invented percentages from an autonomy score at every reasoning step. An SRE error budget is derived from an objective and consumed by measured failures over a stated window.[14][15] Agent policy should follow the same discipline. Evidence can justify more or less autonomous operation for a defined class of work, while precise probability claims require calibration.

IBM's Consistency Analyzer is one useful diagnostic. It resamples decisions from one recorded trajectory, identifies flip-prone points, and generates guidelines for later runs without repeating live tool effects.[1][2] On the same-task evaluation, IBM raised Pass^5 from 53.0 to 69.0 per cent and reduced the reported consistency gap from 24.4 to 12.0 percentage points.[1] The transferable result for a different related task was Pass^5 of 66.0 per cent, a 13.0 percentage-point improvement over baseline.[2] Production teams still need to test whether the method transfers to their own tasks, tools, states and consequences.

The practical contribution of this paper is an agent reliability profile, an operating-boundary record and an intervention checklist. Together they turn repeated evaluation into a deployment decision without claiming that repeatability alone establishes correctness.

## 1. A success rate answers one question

A standard success rate answers a useful question: across the sampled runs, what fraction produced an acceptable outcome?

That number is often the right starting point, and it is incomplete for a system that may receive equivalent intents more than once.

IBM formalises three metrics overkruns of each task.[2]

Metric

Task-level question

Pass@k

Did at least one of the 
k
 runs succeed?

Mean@k

What fraction of the 
k
 runs succeeded?

Pass^k

Did all 
k
 runs succeed?

Pass@k is useful where attempts can be verified and the system may keep trying. Mean@k estimates average run yield under the sampled protocol. Pass^k applies a strict repeated-success condition to each task.

For IBM's 168-task AppWorld evaluation:

Measure

ReAct with GPT-4.1

Mean@5

77.4 per cent

Pass^5

53.0 per cent

Consistency gap

24.4 percentage points

The hard-task tier was more severe:

Measure

Hard tasks

Mean@5

61.9 per cent

Pass^5

31.7 per cent

Consistency gap

30.2 percentage points

The distinction is operationally important. Mean@5 says that a randomly selected run from the evaluation population succeeded about three quarters of the time. Pass^5 says that just over half of the sampled tasks produced five acceptable runs in a row.

Neither number is the probability that a named production intent will succeed tomorrow. The benchmark contains tasks with different difficulty and different latent success probabilities. The agent, model endpoint and environment also define the observed result. A different value ofkwould produce a different Pass^k.

The value is in making repeated behaviour visible. A single average can hide a population of tasks that move between success and failure.

## 2. The consistency gap needs careful interpretation

The consistency gap is:

consistency gap(k) = Mean@k - Pass^k

IBM also defines normalised consistency:

normalised consistency(k) = Pass^k / Mean@k

The normalised measure accounts for the fact that a low-capability system cannot have a large absolute gap when its mean success is already low.[2]

These metrics provide a useful benchmark view. They do not produce a complete reliability contract.

### 2.1 Pass^k changes with k

If a task has a stable per-run success probabilitypand runs are independent, the probability ofkconsecutive successes is:

Pass^k probability = p^k

Forp = 0.9, three consecutive successes occur with probability 72.9 per cent and five occur with probability 59.0 per cent. The system did not become less capable between those calculations. The acceptance test became stricter.

Every published Pass^k value therefore needs the value ofk, the repeat protocol and the reason thatkmatches the operational question.

There is another useful comparison. If all 168 IBM tasks shared one homogeneous success probability equal to the aggregate Mean@5 of 0.774, the independent-run model would predict:

0.774^5 = 27.8%

The observed aggregate Pass^5 was 53.0 per cent. Under an idealised task-level Bernoulli model,Pass^5 = E[p_t^5]while(Mean@5)^5 = E[p_t]^5. Sincep^5is convex on the interval from zero to one, the observed difference is consistent with a heterogeneous population in which many tasks are close to always-pass or always-fail and a smaller population flips between outcomes. Finite samples and non-independent runs limit the calculation, but it strengthens the case for task-level stratification.

### 2.2 Benchmark aggregation mixes task populations

An aggregate Mean@k combines easy, medium and hard tasks. An aggregate Pass^k combines tasks with very different run-level probabilities. Two systems can show the same mean and gap while failing on different task classes.

IBM reports the results by difficulty tier, which makes the pattern more useful.[2] A production profile should go further and use task classes that map to real work, such as:

* read-only lookup;
* bounded calculation;
* record mutation;
* cross-system reconciliation;
* irreversible external action;
* long-running workflow with changing state.

### 2.3 Equivalent outcomes need a definition

Two successful runs do not need identical text or identical tool paths. A travel agent may choose two different flights that both satisfy the user's constraints. A diagnostic agent may inspect systems in a different order and reach the same supported conclusion.

Consistency can be defined at several levels:

Level

Example equivalence rule

Surface

Exact output string matches

Semantic

The conclusion and material claims are equivalent

Action

The same authorised effects occur

Outcome

The final state satisfies the task contract

Process

Required controls and prohibited actions are respected

The appropriate level depends on the task. Exact path agreement can reject useful variation. Outcome agreement can miss unsafe intermediate actions. A reliability profile should state both the outcome contract and the process constraints.

### 2.4 Consistency is not correctness

Mehta's 2026 study used 8,000 runs of four models across 200 read-only HotpotQA questions, with a 50-task SWE-bench cross-check.[5] It defined behavioural consistency through the number of distinct action sequences rather than through outcome equivalence. Unanimous agreement across three runs produced 87 to 88 per cent accuracy at 54 to 62 per cent coverage, a 6 to 14 percentage-point gain over single-run baselines for three of the four models. The study also identified consistently wrong tasks, accounting for 5.5 to 10 per cent of the evaluated population.[5]

This sets a hard boundary on consistency-only policies. Agreement can support abstention and routing, while correctness still requires an outcome check, trusted reference, deterministic invariant, external evidence or qualified review.

## 3. What IBM's result establishes

The IBM work provides three useful contributions.

### 3.1 Repeated outcome evidence

The reported 77.4 per cent Mean@5 and 53.0 per cent Pass^5 demonstrate that average task success and strict repeated success can diverge materially for the studied agent and benchmark.[1][2]

The evaluation used:

* AppWorldtest_normal;
* 168 tasks;
* a ReAct agent;
* GPT-4.1;
* five fresh evaluation runs;
* temperature 0.0.[1][2]

This bounded empirical result does not establish the reliability of GPT-4.1 agents in general.

### 3.2 Step-level instability can be probed offline

The Consistency Analyzer takes a recorded trajectory and resamples each inference point against its recorded context without executing the resulting actions. It scores response variation and produces a step-level consistency scorecard.[1][2] The blog post describes five completions per decision step by default, while the technical report specifies a default resampling budget of 30.[1][2]

The process does not repeat tool calls or environment mutations, which is useful for production traces that cannot be replayed safely. The analyser tests a model decision against a frozen context rather than measuring how a live environment would respond to an alternative action.

The technical report extracts(API_name, API_params)pairs and scores average pairwise Jaccard similarity. Its 30-completion budget uses temperature 0.5 and multiplies token cost by roughly 30 for each analysed trajectory.[2] This deliberate sampling is a proxy for a flat decision boundary under added variation, rather than a direct measurement of the temperature-zero endpoint variance discussed later in this paper.

### 3.3 Targeted guidelines improved the benchmark result

IBM converted flip-prone decisions into natural-language consistency guidelines and retrieved those guidelines for later tasks. On the GPT-4.1 evaluation:

Metric

Baseline

Same-task guidelines

Similar-task guidelines

Mean@5

77.4 per cent

81.0 per cent

79.5 per cent

Pass^5

53.0 per cent

69.0 per cent

66.0 per cent

Consistency gap

24.4 pp

12.0 pp

13.5 pp

The same-task condition mines guidelines from a baseline trajectory of the task that is later repeated. For a new intent, the similar-task result is the closer analogue: Pass^5 improved by 13.0 percentage points.[2] On GPT-OSS-120B, similar-task Pass^5 improved by 8.7 points, exceeding the 6.0-point same-task improvement.[2] The report also studies resampling budget sensitivity.

The result supports trajectory-guided remediation as a promising technique without establishing that guidelines remain safe after model or tool changes, or that a smaller consistency gap guarantees acceptable production outcomes.

## 4. What the result does not establish

Several boundaries should remain explicit.

### 4.1 It is one benchmark setting

AppWorld is a controllable environment for agents that interact with simulated applications through APIs.[3] It is useful because tasks have executable outcomes and can be repeated. Production environments may include changing records, rate limits, delayed effects, human responses and non-replayable actions.

### 4.2 Temperature zero is not a reproducibility guarantee

IBM ran the agent at temperature 0.0.[1][2] Greedy decoding removes ordinary sampling from the baseline execution. Hosted inference can still vary.

Thinking Machines Lab identifies batch-size dependence in inference kernels as a major source of user-visible nondeterminism. A request can produce a different numerical result depending on the dynamic batch in which it is served, even when each kernel execution is deterministic for its full input.[10] Other studies document output instability under settings commonly treated as deterministic and analyse numerical precision, hardware configuration and parallel execution as contributing factors.[11][12]

Model nondeterminism is only one source of trajectory variation. Tool results, retrieval order, timestamps, concurrent writes, network behaviour and external state can also differ.

### 4.3 A smaller gap can coexist with wrong outcomes

A system that fails the same way every time has perfect behavioural repeatability and poor outcome reliability. The IBM objective preserves or improves Mean@5 while improving Pass^5, which guards against a simple collapse into stable failure.[2] The report is explicit that the analyser scores stability rather than correctness, so a confidently wrong decision can look consistent.[2] Production teams still need a direct acceptable-outcome measure and a process-safety measure.

### 4.4 The analyser observes recorded contexts

Resampling a decision point can reveal model sensitivity at that context without executing alternative paths. Some varied outputs may be operationally equivalent, while small textual changes can cause very different effects once passed to a tool.

The scorecard is a diagnostic rather than a substitute for end-to-end repeated evaluation.

### 4.5 Guideline memory creates lifecycle obligations

Guidelines are configuration that can change future behaviour. The ALTK-Evolve implementation provides provenance and LLM-based conflict resolution for stored guidelines.[4] A production deployment also needs version scope, expiry, rollback and evaluation against held-out tasks, because a guideline derived from one model, prompt, schema or environment may become stale after any of those inputs change.

## 5. The step-count model is a sensitivity test

A common sensitivity calculation uses the following arithmetic:

workflow success = p^n

If every decision has a 99 per cent probability of being correct:

Decisions

0.99^n

10

90.4 per cent

50

60.5 per cent

100

36.6 per cent

The arithmetic is correct under three assumptions:

1. every transition has the same success probability;
2. transition outcomes are independent;
3. every wrong transition makes the final workflow unacceptable.

Agent workflows rarely satisfy all three.

Decision risk varies by context. Errors can be correlated because one early mistake changes the state seen by every later decision. Some incorrect intermediate actions are recoverable. Some divergent actions produce an equivalent acceptable outcome. A tool failure can be retried safely when the operation is idempotent, while one wrong irreversible action can fail the workflow immediately.

The model remains useful as a sensitivity test because it demonstrates how quickly a long chain can become fragile under strict assumptions. Presenting it as a measured reliability curve requires evidence that those assumptions hold.

Recent long-horizon research reinforces this caution. Khanal and colleagues report reliability decay that differs materially by domain, including a steep drop in software-engineering tasks and a nearly flat pattern in document processing.[7] The HORIZON work argues that long-horizon tasks lack a canonical definition and that raw interaction length, tool calls, reasoning steps and episode duration are not interchangeable measures.[8]

An empirical profile should therefore use structural descriptors that matter to the task:

* number of state-changing actions;
* number of external dependencies;
* number of authority-domain crossings;
* elapsed time and state freshness;
* branch count;
* recovery opportunities;
* irreversible-action count;
* human or deterministic checkpoints.

## 6. Reliability is a profile

An agent reliability claim needs a subject. The subject is more specific than a model name or an application name.

A useful reliability profile identifies:

task class
action and consequence class
agent architecture
model and serving configuration
prompt and policy version
tool and schema versions
principal and authority scope
environment and dependency set
horizon descriptors
intervention policy
evaluation window

The indicators then describe behaviour inside that boundary.

### 6.1 Core indicators

Indicator

Definition

Why it matters

Outcome yield

Acceptable runs divided by total runs

Average user-visible success

Strict repeated success at k

Task groups with 
k
 acceptable runs divided by task groups

Repeatability under a stated test

Normalised consistency at k

Strict repeated success divided by outcome yield

Comparison after accounting for mean capability

Mixed-outcome rate

Tasks with at least one pass and one fail divided by tasks

Population that moves between success and failure

Equivalent-outcome agreement

Runs producing equivalent acceptable outcomes divided by compared runs

Separates harmless variation from material divergence

Consistent-wrong rate

Task groups where all 
k
 runs are unacceptable and outcome-equivalent divided by task groups

Detects stable failure that consistency alone misses

Non-equivalent repeated-failure rate

Task groups where all 
k
 runs are unacceptable and not outcome-equivalent divided by task groups

Preserves the remaining all-failure class

Policy-compliance rate

Runs satisfying process and authority constraints divided by runs

Captures unsafe paths even when outcomes look correct

Grader false-accept rate

Unacceptable outcomes marked acceptable divided by adjudicated unacceptable outcomes

Bounds optimism in reported reliability

Recovery success

Recoverable failures restored to an acceptable outcome divided by recoverable failures

Measures runtime resilience

Autonomous coverage

Intents admitted to autonomous execution divided by eligible intents

Shows the scope behind a reliability claim

Intervention success

Intervened intents producing acceptable outcomes divided by interventions

Tests whether fallback policy helps

Eachk-run group should enter exactly one outcome class: all runs acceptable; at least one acceptable and one unacceptable; all runs unacceptable and outcome-equivalent; or all runs unacceptable and not outcome-equivalent. The profile must version the outcome-equivalence rule and any adjudication procedure.

The profile should include uncertainty. A measured 99 per cent success rate from 100 runs is not equivalent to the same rate from 100,000 runs. Report sample sizes and confidence intervals. For heterogeneous task populations, stratified bootstrap intervals or task-level resampling are often more informative than treating every run as interchangeable. Recent work also formalises consistency as a statistical property rather than relying only on descriptive agreement rates.[9]

### 6.2 Dependence and joint decisions

Repeated runs of one task form a cluster. An outcome-yield interval should therefore resample whole task groups, stratified by the task and consequence classes in the operating boundary. A production window may require blocks defined by time, release, dependency or incident domain. When the dependence structure is not modelled, the interval should be labelled descriptive and should not approve wider autonomy.

An operating boundary also contains several gates. Separate 95 per cent intervals do not mean that all published bounds cover simultaneously with 95 per cent confidence. A conjunctive approval rule, where every gate must clear, already limits false approval at the per-gate error rate under intersection-union logic. If the profile also claims simultaneous coverage for all reported bounds, it needs a procedure such as Bonferroni adjustment or a joint task-cluster bootstrap. The published profile should name the clustering unit, stratification, interval method, confidence level and purpose of any multiple-gate adjustment.

### 6.3 The grader is part of the measurement system

Every outcome indicator depends on a verdict. Some tasks have an executable oracle, such as an exact database state or a test suite. Others depend on rules, a human reviewer or an LLM judge.

The grader's error can be larger than the budget being governed. A judge with three per cent disagreement against qualified human review cannot support a claim that the system misses a one per cent SLO with useful precision.

A reliability profile should therefore report:

* grader type and version;
* human-adjudication sample;
* agreement and disagreement by task class;
* false-accept and false-reject estimates;
* unresolved cases;
* the smallest budget the grader is expected to distinguish.

Measurement error should be materially smaller than that budget. HORIZON validated its trajectory judge against human annotation and reported human-judge agreement of kappa 0.84, alongside inter-annotator agreement of kappa 0.61.[8] Those values are evidence about the measurement process, and they also show why a grader should not be treated as ground truth without validation.

### 6.4 Consistency is one dimension

Rabanser and colleagues frame agent reliability across consistency, robustness, predictability and safety.[6] Their experiments include prompt perturbation, tool-fault injection, environment changes, confidence calibration and harm assessment.

That wider frame matters operationally:

* consistency asks whether equivalent runs agree;
* robustness asks whether small or expected disturbances preserve acceptable behaviour;
* predictability asks whether the system can identify likely failure;
* safety asks whether failure severity remains bounded.

An agent can score well on one dimension and poorly on another.

Rabanser and colleagues use a holistic performance profile to compare models and benchmarks.[6] The profile proposed here serves a different operational purpose. It binds evidence to a deployment version, an authority scope, an admitted task population and an intervention policy. Any change to those inputs can revoke the operating boundary.

## 7. Define an operating boundary

An operating boundary is the set of conditions under which an organisation has enough evidence to permit a stated execution mode.

It can be expressed as:

Operating boundary:
 task class
 consequence class
 environment
 version set
 horizon range
 required indicators
 minimum evidence
 allowed intervention policy

For example:

Field

Example

Task class

Read-only support-case summarisation

Consequence

No external mutation

Model and agent

Named model, prompt and orchestrator versions

Dependencies

Approved case system and document index

Horizon

Up to 8 tool calls, one retrieval domain

Outcome SLO

At least 98 per cent acceptable summaries

Strict repeated-success SLO

At least 95 per cent Pass^3

Consistent-wrong ceiling

Below 0.5 per cent

Policy constraint

Zero observed access or citation violations, backed by deterministic enforcement

Minimum evidence

1,000 representative task groups

Allowed mode

Autonomous draft, human publication

A state-changing workflow might require a narrower boundary:

Field

Example

Task class

Invoice reconciliation

Consequence

Bounded financial record mutation

Horizon

One source lookup, one calculation, one proposed write

Deterministic checks

Totals, currency, duplicate detection, authority

Required mode

Agent proposes, deterministic verifier checks, human approves exceptions

Autonomous writes

Allowed only for exact matches below a defined value

The boundary makes the denominator visible. A claim of 99 per cent reliability has little value if it silently excludes difficult cases or sends half the work to humans.

## 8. SLOs should govern policy

An SLI is a quantitative measure of a service level. An SLO is a target or range for that indicator.[14]

Agent SLIs should be tied to acceptable user outcomes and required controls. Examples include:

acceptable outcome yield
strict repeated success at k
consistent-wrong rate
policy-compliance rate
recovery success

The production objective and repeated-run objective should be separate:

Production, rolling 28-day window:
at least 99% of eligible reconciliation intents
must produce an acceptable proposed result.

Offline, refreshed before release and weekly:
at least 97% of representative task groups
must pass all 3 executions against reset fixtures.

These statements need:

* a task population;
* an eligibility rule;
* an outcome grader;
* a repeated-run protocol;
* an evaluation environment;
* a version scope;
* consequences for missing the objective.

### 8.1 Error budgets remain measured outcomes

An error budget is derived from the SLO. A 99.9 per cent objective leaves a 0.1 per cent error budget over the stated window.[15]

The budget can govern operational policy:

* slow rollout of a new model or prompt;
* require more deterministic checks;
* reduce the admitted task population;
* move high-consequence actions to approval;
* pause expansion of autonomous scope;
* prioritise reliability work.

Google's example error-budget policy changes release behaviour after measured SLO misses.[15] Burn-rate methods then turn budget consumption into an actionable operational signal.[16] The same ideas can govern agent autonomy.

### 8.2 Avoid arithmetic autonomy scores

An illustrative runtime design might subtract two per cent for reasoning, eight per cent for classification and twelve per cent for a subagent. That calculation creates an appearance of precision unless the values are empirically calibrated and supported by a valid composition model.

A policy can use limits such as maximum tool calls, time, external effects or authority domains. Those are explicit guardrails. A runtime can also use calibrated failure predictors. Neither should be presented as a probability of success unless validation supports that interpretation.

As a governance label, autonomy budget can describe the amount and class of work policy currently permits based on observed evidence. A fictional percentage remaining inside one trajectory has no such support.

## 9. Intervention is a reliability mechanism

The operating boundary determines how the runtime acts.

### 9.1 Intervention ladder

Level

Runtime behaviour

0

Autonomous execution inside the proven boundary

1

Deterministic validation before accepting the result

2

Repeat execution with an explicit equivalence and adjudication rule

3

Checkpoint before state-changing or cross-domain action

4

Human approval for exceptions or high-consequence effects

5

Refuse or route to a different system

The policy should select the least costly intervention that meets the outcome and safety objectives.

### 9.2 Repetition is not always the answer

Multiple runs increase cost and latency. Majority voting provided little benefit in Mehta's multi-step agent evaluation because early systematic errors produced repeated wrong trajectories.[5] This differs from single-turn self-consistency, where sampling and voting can improve reasoning accuracy.[28] Repeated execution is most useful where:

* outputs can be compared meaningfully;
* the environment can be replayed or snapshotted;
* effects are withheld until adjudication;
* disagreement is informative;
* the value of reduced risk exceeds the added cost.

For an irreversible action, running the full workflow three times against the live environment can cause three effects. Repetition should occur in simulation, against a snapshot, or before effect commitment.

### 9.3 Selective execution can trade coverage for reliability

Mehta reports a risk-coverage tradeoff: stricter agreement reduces admitted coverage while increasing accuracy among admitted tasks.[5]

This suggests an operational pattern:

evaluate confidence or agreement
 |
 +-- inside boundary -> proceed
 |
 +-- uncertain -> verify or escalate
 |
 +-- prohibited -> refuse

The system should publish both reliability and coverage. Escalating most tasks can produce a valid high-reliability operating model, provided the escalation remains in the denominator. Coverage, outcome yield, escalation outcome and escalation latency should also be reported for every task and consequence stratum that defines the boundary. Relevant user, locale or customer strata belong in the profile when they can change service quality.

## 10. Diagnose unstable decisions without replaying effects

IBM's Consistency Analyzer is valuable because it can examine a recorded trajectory without repeating the environment interactions.[1][2] It builds on earlier trajectory-informed memory work that extracts guidance from successful, failed and inefficient executions.[26]

The operating pattern is:

1. record the context at each model decision;
2. resample that decision offline;
3. compare the structured meaning of the responses;
4. flag decisions with material variation;
5. generate or propose targeted guidance;
6. validate the guidance on held-out tasks;
7. version and monitor the guidance in production.

This is one member of a larger diagnostic family. IBM's AgentFixer uses rule-based and LLM-based checks to detect and classify failures, then produce fix recommendations.[17] Other work studies process observability, trajectory anomaly detection and interactive agent debugging.[19][20][21][22]

The remediation needs controls:

* trace and task provenance;
* model, prompt and tool version binding;
* held-out validation;
* conflict detection between guidelines;
* expiry and review dates;
* rollback;
* monitoring for reduced capability or new safety failures.

The goal is a tested change to agent behaviour, not a growing pile of advice.

## 11. Observability should preserve evidence

Evaluation and production serve different purposes.

An offline evaluation record should preserve:

* task and grader version;
* environment snapshot or fixture version;
* model and serving configuration;
* prompt, policy and tool schemas;
* run group and repetition index;
* action and consequence class;
* outcome and process verdicts;
* intervention policy;
* cost and latency;
* trace references;
* evidence hashes.

A production execution receipt should preserve:

* intent class;
* admitted operating boundary;
* model, prompt and policy versions;
* tools selected and authority used;
* deterministic checks;
* checkpoints and approvals;
* effects attempted and observed;
* final outcome where available;
* later reconciliation.

OpenTelemetry is increasingly able to carry the trace structure. The GenAI semantic-conventions project documents conventions and reference implementations for model inference, agents, tool execution, evaluation and MCP operations.[23][24][25] This can reduce bespoke instrumentation.

Telemetry should not include hidden chain-of-thought. Useful evidence includes tool calls, structured decisions, versions, timings, policy verdicts and outcome labels. Prompts, outputs and business data need redaction and access controls. High-cardinality identifiers should remain in traces or controlled records rather than metric labels.

## 12. A practical reliability programme

### Step 1: classify the work

Create task classes based on outcome contract and consequence. Do not begin with one mixed benchmark. IBM's evaluation tutorial covers the wider set of planning, tool-use, memory and reflection capabilities that may need separate treatment.[18]

### Step 2: define acceptable outcomes

Specify what must be true in the final state. Add process constraints for authority, privacy and prohibited actions. Validate the grader against qualified human adjudication before using it to govern a narrow error budget.

### Step 3: choose the repeat protocol

Statek, environment reset rules, model settings, tool fixtures, concurrency, grader and version. Use a value ofkthat matches the operational question and cost.

### Step 4: measure several indicators

At minimum report:

* outcome yield;
* Pass^k;
* normalised consistency;
* mixed-outcome rate;
* consistent-wrong rate;
* policy-compliance rate;
* grader false-accept and false-reject estimates;
* sample size and uncertainty.

### Step 5: stratify by structure

Report results by task class, consequence, dependency count and horizon descriptors. Avoid treating raw step count as a universal difficulty scale.

### Step 6: set an operating boundary

Pre-specify the gates and their joint decision rule. Use cluster-aware intervals for repeated runs. Distinguish control of false approval from simultaneous coverage of the published bounds, and apply an adjustment only when the stated confidence claim requires it. State the versions and population to which the boundary applies.

### Step 7: define intervention

Map evidence shortfalls to deterministic checks, replay, checkpoints, approval or refusal.

### Step 8: canary changes

Evaluate model, prompt, tool and guideline changes before expanding traffic. Compare against the current production configuration.

### Step 9: monitor budget burn

Track bad outcomes and policy violations over a rolling window. Tighten autonomous scope when evidence falls below objective.

### Step 10: review drift

Revalidate when models, tools, schemas, data distributions or task mix change. A reliability profile is versioned evidence, not a permanent property.

## 13. Indicators and denominators

The following hypothetical profile shows why estimates need source labels, cluster-aware intervals and a joint decision rule. It covers one defined task and consequence stratum.

The offline sample contains 1,000 task groups with three runs each. Exactly 968 groups have three acceptable outcomes, 21 have two, six have one, four have three unacceptable outcome-equivalent results, and one has three unacceptable non-equivalent results. The four group classes are mutually exclusive. Equivalence is decided by a versioned final-state comparator.

The boundary has three stochastic gates: outcome yield, Pass^3 and consistent-wrong rate. The conjunctive approval rule already controls false approval at the per-gate error rate. This example also targets at least 95 per cent simultaneous coverage for the three one-sided bounds, so each uses a Bonferroni-adjusted 98.33 per cent bound. The outcome-yield bound comes from 200,000 percentile-bootstrap samples of whole three-run task groups, using seed20260916. The two gated group-level rates use Wilson bounds withz = 2.128. The offline workflow has an exact executable outcome oracle, so learned-grader error does not enter these rows. A profile that uses human or model grading must propagate its measured error before making a boundary decision.

Indicator

Source

Observed result

Reported uncertainty

Boundary test

Outcome yield

Offline

2,952 / 3,000, or 98.4 per cent

97.70 per cent adjusted task-cluster lower bound

Does not clear a 98 per cent lower-bound target

Pass^3

Offline

968 / 1,000 groups, or 96.8 per cent

95.39 per cent adjusted Wilson lower bound

Clears a 95 per cent lower-bound target

Normalised consistency

Offline, derived

96.8 / 98.4, or 98.4 per cent

Derived ratio

Reported, not tested separately

Mixed-outcome rate

Offline

27 / 1,000 groups, or 2.7 per cent

1.86 to 3.90 per cent marginal 95 per cent interval

Monitor

Consistent-wrong rate

Offline

4 / 1,000 groups, or 0.4 per cent

1.10 per cent adjusted Wilson upper bound

Does not clear a 0.5 per cent upper-bound ceiling

Non-equivalent repeated-failure rate

Offline

1 / 1,000 groups, or 0.1 per cent

0.02 to 0.56 per cent marginal 95 per cent interval

Review classification

Grader false-accept rate

Offline

Not applicable: exact executable oracle

Not applicable

No learned-grader budget

Policy compliance

Offline

3,000 / 3,000, or 100 per cent

Exact deterministic check

Clears only while enforcement remains complete

Autonomous coverage

Production

3,001 / 4,840, or 62.0 per cent

60.63 to 63.36 per cent marginal 95 per cent interval

Disclosure denominator

Intervention success

Production

1,674 / 1,839, or 91.0 per cent

89.63 to 92.25 per cent marginal 95 per cent interval

Monitor

This profile does not clear the illustrative operating boundary in section 7. The estimated outcome yield exceeds 98 per cent, while its adjusted lower bound does not. The observed consistent-wrong rate is below 0.5 per cent, while its adjusted upper bound is above one per cent. At the same observed rate and confidence level, clearing that ceiling would require roughly 23,000 task groups. Rare-event ceilings are expensive to demonstrate statistically, which strengthens the case for deterministic enforcement where it is available.

The production intervals are descriptive because the example does not model temporal or dependency correlation. They cannot approve wider autonomy. A deployment-grade production profile should use predeclared time or dependency blocks and report coverage, outcomes and intervention behaviour by every boundary-defining stratum.

Every number needs a named grader and version. The profile should also state grader error, excluded tasks and missing outcomes.

Production outcome labels can be delayed. A reconciliation task may be accepted initially and later found wrong. Store provisional and final verdicts separately.

## 14. Counterarguments

### 14.1 Most users run an intent once

That is true for many interactions. Repeated-run evaluation still estimates whether success depends on a favourable trajectory, especially for recurring business processes and changes that must be safe across many users.

For unique tasks, the team needs neighbouring cases, perturbation tests and process invariants. Pass^k on the exact intent is only one form of evidence.

### 14.2 Repeated execution is too expensive

It can be. Use repeated runs offline, on representative samples and during canaries. Reserve expensive production repetition for tasks where verification is possible and the consequence justifies the cost.

IBM's offline resampling reduces the need for complete live re-execution when diagnosing decision instability.[1][2] It is not cheap: the default budget is 30 completions per inference step and multiplies token cost by roughly 30 for each analysed trajectory.[2] Adaptive resampling may reduce that cost, but the report leaves it as future work.

### 14.3 Deterministic orchestration removes the problem

Deterministic code can constrain authority, validate outputs and make recovery safer. It reduces the number of probabilistic decisions and contains their effects, without guaranteeing that a remaining model decision will be correct.

### 14.4 A stronger model will close the gap

Capability and consistency are related but distinct. IBM reports aggregate consistency gaps of 24.4 percentage points for GPT-4.1 and 23.8 points for GPT-OSS-120B despite their large capability difference.[2] The difficulty pattern also differs: the GPT-4.1 gap grows from easy to hard tasks, while the GPT-OSS-120B gap is largest on the easy tier because the hard-tier mean is already low. Other reliability studies show model rankings changing with task horizon and dimension.[6][7] Graph-guided investigation work also reports a gap between best-case capability and majority reliability for ReAct agents.[27]

### 14.5 Guidelines will overfit

They can. IBM reports similar-task gains, which is evidence of transfer in the studied scenarios.[1][2] Khanal and colleagues report that general memory scaffolds reduced long-horizon performance across all ten models they tested.[7] IBM's guidelines are narrower, target measured instability and preserve Mean@5 in their evaluation. The boundary between useful targeted guidance and harmful accumulated memory remains unresolved, so production adoption needs held-out evaluation, version scope and rollback.

### 14.6 Pass^k is mechanically strict

Pass^k falls askrises, even when the run distribution is stable. It can also penalise harmless variation when the outcome-equivalence rule is too narrow.

The reliability profile therefore reports Pass^k beside outcome yield, consistent-wrong rate, coverage and uncertainty. The value ofkis part of the claim rather than a universal setting.

## 15. The strongest counterargument

The strongest objection is a verification asymmetry.

Repeated-run consistency is most valuable when a team cannot cheaply verify a production result. Yet outcome yield, consistent-wrong rate and intervention success all require an acceptability oracle. Where a reliable oracle exists online, checking one result can be cheaper than running the task several times.

The answer is to separate evaluation from execution. A qualified oracle is used offline on a representative sample to establish and refresh the operating boundary. Production runs proceed once inside that boundary, with deterministic checks where they exist. Agreement or instability signals can support routing and abstention when the full oracle is unavailable online.

This approach still depends on the evaluation sample representing production. Drift, novel tasks and changed dependencies can invalidate the boundary. Production monitoring therefore needs delayed outcome labels, sampled human review and automatic re-evaluation triggers.

A production reliability claim can then read:

For this task class, version set and intervention policy,
the measured outcome yield is X,
strict repeated success at k is Y,
consistent-wrong rate is Z,
and autonomous coverage is C.

The statement is harder to market and easier to operate.

## 16. What this paper does not claim

This paper does not claim:

* that the IBM result generalises to every agent, model or domain;
* that repeated agreement establishes correctness or that Pass^k is sufficient alone;
* thatp^nestimates real workflow reliability without validated independence and failure assumptions;
* that guidelines replace deterministic controls, authority boundaries or qualified review;
* that precise remaining reliability can be calculated by subtracting arbitrary risk values inside one trajectory.

The paper proposes a way to organise evidence and policy. Its effectiveness depends on representative tasks, trustworthy graders, sufficient samples and controls that hold when the agent is wrong.

## Conclusion

IBM's result makes a hidden production question measurable. An agent that completes 77.4 per cent of runs can complete all five repeated runs for only 53.0 per cent of tasks under the same evaluation protocol.[1][2] The average score remains useful when accompanied by repeated-run evidence.

Repeated success can reveal task classes that depend on a favourable trajectory, and step-level resampling can help find unstable decisions. Agreement can support abstention and routing, subject to the risk of consistent wrong answers.

Agent reliability should be published as a versioned profile. The profile needs a task population, an outcome contract, repeated-run evidence, consequence classes, intervention policy, coverage and uncertainty. An operating boundary can then state where autonomous execution is supported by evidence and where another control is required.

SRE contributes the discipline of explicit indicators, objectives, windows and consequences. Measured outcomes should govern changes in autonomous scope rather than invented uncertainty arithmetic.

The practical question is where the system has enough evidence to let the next run proceed without another check.

## Appendix A: Agent reliability profile template

Profile ID:
Version:
Owner:
Review date:

System
 Agent architecture:
 Model and serving configuration:
 Prompt and policy version:
 Tool and schema versions:
 Environment:
 Principal and authority scope:

Task population
 Task class:
 Inclusion rule:
 Exclusions:
 Consequence class:
 Horizon descriptors:
 Dependency set:

Outcome contract
 Acceptable final state:
 Required evidence:
 Outcome-equivalence rule:
 Process constraints:
 Prohibited actions:
 Grader and version:
 Adjudication procedure:

Repeat protocol
 k:
 Environment reset:
 State fixture:
 Concurrency:
 Sampling settings:
 Evaluation window:
 Clustering unit:
 Stratification:
 Interval method:
 Confidence level:
 Multiple-gate adjustment:

Indicators
 Outcome yield:
 Strict repeated success at k:
 Normalised consistency at k:
 Mixed-outcome rate:
 Equivalent-outcome agreement:
 Consistent-wrong rate:
 Non-equivalent repeated-failure rate:
 Policy-compliance rate:
 Grader false-accept rate:
 Grader false-reject rate:
 Recovery success:
 Autonomous coverage:
 Intervention success:
 Confidence intervals:

Operating boundary
 Required SLOs:
 Minimum evidence:
 Allowed autonomous mode:
 Deterministic checks:
 Checkpoint conditions:
 Human approval conditions:
 Refusal conditions:

Change control
 Canary protocol:
 Rollback:
 Error-budget policy:
 Drift triggers:

## Appendix B: Repeated-run evaluation checklist

[ ] The task population maps to real production work.
[ ] Equivalent inputs and outcomes are defined.
[ ] Every run uses a recorded version set.
[ ] Environment reset rules are explicit.
[ ] k is stated and justified.
[ ] Outcome and process verdicts are separate.
[ ] Grader agreement with human adjudication is measured.
[ ] Grader error is smaller than the narrowest budget being governed.
[ ] Mean@k and Pass^k are both reported.
[ ] Mixed outcomes are counted.
[ ] Consistent-wrong outcomes are counted.
[ ] Repeated-run groups use mutually exclusive outcome classes.
[ ] Results are stratified by task and consequence class.
[ ] Horizon descriptors include more than raw step count.
[ ] Sample sizes and uncertainty are reported.
[ ] Repeated runs are resampled as task clusters.
[ ] Multiple boundary gates use a pre-specified joint decision rule.
[ ] Production dependence is modelled or its intervals are labelled descriptive.
[ ] Repeated effects are simulated or withheld.
[ ] Deterministic invariants are tested independently.
[ ] Coverage, outcomes and escalation are reported by boundary-defining stratum.
[ ] Guidelines or memories are validated on held-out tasks.
[ ] Model, prompt, tool or schema changes trigger review.

## Appendix C: Intervention policy example

Policy: read-only case analysis

Autonomous draft
 Allowed when:
 task is in the approved class
 all sources are authorised
 deterministic citation checks pass
 reliability profile is inside SLO

Deterministic verification
 Required when:
 totals or identifiers can be checked exactly
 output references a system of record

Repeated evaluation
 Allowed when:
 no external effect occurs before adjudication
 semantic equivalence can be scored

Human review
 Required when:
 task is outside the approved population
 material runs disagree
 policy evidence is incomplete
 consequence exceeds the approved class

Refuse
 Required when:
 authority is absent
 a prohibited action is requested
 the environment cannot preserve required evidence

## About the author

Jason Doyle writes about reliable software, observability, incident leadership, applied AI, and practical controls for systems that influence human and organisational decisions. He publishes atjasondoyle.ieand can be contacted at[email protected].

## References

1. IBM Research,Your Agent Aced the Task. Will It Do It Again?, Hugging Face, 15 September 2026,https://huggingface.co/blog/ibm-research/altk-evolve-consistency.
2. Evelyn Duesterwald, Benjamin Elder, Lilian Ngweta, Shashanka Ubaru, and Malgorzata Zimon,Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course, arXiv:2609.08832, 8 September 2026,https://arxiv.org/abs/2609.08832.
3. Harsh Trivedi et al.,AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents, ACL 2024,https://arxiv.org/abs/2407.18901.
4. IBM AgentToolkit,Evolve: On-the-job learning for AI agents (ALTK-Evolve), source repository and documentation, accessed 16 September 2026,https://github.com/AgentToolkit/altk-evolve.
5. Aman Mehta,When Agents Disagree With Themselves: Behavioral Consistency as an Uncertainty Signal for LLM Agents, arXiv:2602.11619v2, 15 July 2026,https://arxiv.org/abs/2602.11619.
6. Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, and Arvind Narayanan,Towards a Science of AI Agent Reliability, arXiv:2602.16666v3, 2 June 2026,https://arxiv.org/abs/2602.16666.
7. Aaditya Khanal, Yangyang Tao, and Junxiu Zhou,Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents, arXiv:2603.29231, 31 March 2026,https://arxiv.org/abs/2603.29231.
8. Xinyu Jessica Wang et al.,The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break, arXiv:2604.11978, 13 April 2026,https://arxiv.org/abs/2604.11978.
9. Harsh Raj, Niranjan Orkat, Suvrorup Mukherjee, Aritra Guha, Cheryl Flynn, and Subhabrata Majumdar,Consistency as a Testable Property: Statistical Methods to Evaluate AI Agent Reliability, arXiv:2605.10516, 11 May 2026,https://arxiv.org/abs/2605.10516.
10. Horace He,Defeating Nondeterminism in LLM Inference, Thinking Machines Lab, 10 September 2025,https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/.
11. Berk Atil, Sarp Aykent, Alexa Chittams, et al.,Non-Determinism of "Deterministic" LLM Settings, arXiv:2408.04667v5, 2 April 2025,https://arxiv.org/abs/2408.04667.
12. Jiayi Yuan, Hao Li, Xinheng Ding, et al.,Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference, arXiv:2506.09501, 11 June 2025,https://arxiv.org/abs/2506.09501.
13. Salesforce,Salesforce Expands Agentforce With a New Portfolio of AI Agents Built for High-Value Work, 11 September 2026,https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents/.
14. Google,Service Level Objectives, Site Reliability Engineering, chapter 4, 2016,https://sre.google/sre-book/service-level-objectives/.
15. Steven Thurgood,Example Error Budget Policy, The Site Reliability Workbook, 19 February 2018,https://sre.google/workbook/error-budget-policy/.
16. Alex Hidalgo,Alerting on SLOs, The Site Reliability Workbook, chapter 5, 2018,https://sre.google/workbook/alerting-on-slos/.
17. IBM Research,AgentFixer: From Failure Detection to Fix Recommendations in Agentic Systems, ICSE 2026 workshop paper, 12 April 2026,https://research.ibm.com/publications/agentfixer-from-failure-detection-to-fix-recommendations-in-agentic-systems.
18. IBM Research,Evaluating LLM-based Agents: Foundations, Best Practices and Open Challenges, IJCAI 2025 tutorial, 16 August 2025,https://research.ibm.com/publications/evaluating-llm-based-agents-foundations-best-practices-and-open-challenges.
19. Dany Moshkovich et al.,Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems, arXiv:2503.06745, 2025,https://arxiv.org/abs/2503.06745.
20. Fabiana Fournier, Lior Limonad, and Yuval David,Agentic AI Process Observability: Discovering Behavioral Variability, arXiv:2505.20127, 2025,https://arxiv.org/abs/2505.20127.
21. Yibing Liu et al.,TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents, arXiv:2602.06443, 2026,https://arxiv.org/abs/2602.06443.
22. Robert Hutter and Michael Pradel,AgentStepper: Interactive Debugging of Software Development Agents, arXiv:2602.06593, 2026,https://arxiv.org/abs/2602.06593.
23. OpenTelemetry,Semantic Conventions for Generative AI, accessed 16 September 2026,https://github.com/open-telemetry/semantic-conventions-genai.
24. OpenTelemetry,Semantic Conventions for GenAI Agent Spans, accessed 16 September 2026,https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md.
25. OpenTelemetry,Execute Tool Span Reference Report, accessed 16 September 2026,https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference/reports/execute-tool-span.md.
26. Gaodan Fang et al.,Trajectory-Informed Memory Generation for Self-Improving Agent Systems, arXiv:2603.10600, 2026,https://arxiv.org/abs/2603.10600.
27. Saurabh Jha et al.,Think Locally, Explain Globally: Graph-Guided LLM Investigations via Local Reasoning and Belief Propagation, arXiv:2601.17915, 2026,https://arxiv.org/abs/2601.17915.
28. Xuezhi Wang et al.,Self-Consistency Improves Chain of Thought Reasoning in Language Models, ICLR 2023,https://arxiv.org/abs/2203.11171.

Related papers

When the Endpoint Is Up but the Product Is Failing
When Memory Becomes Production State
When AI Evaluations Act on the Real World
MCP Tool Readiness
---
title: 'GitHub - hexo-ai/sia: SIA is a Self Improving AI framework to autonomously improve the performance of any AI system (Model / Agent) on a benchmark task. · GitHub'
url: https://github.com/hexo-ai/sia
site_name: github
content_file: github-github-hexo-aisia-sia-is-a-self-improving-ai-frame
fetched_at: '2026-06-11T19:53:03.778511'
original_url: https://github.com/hexo-ai/sia
author: hexo-ai
description: SIA is a Self Improving AI framework to autonomously improve the performance of any AI system (Model / Agent) on a benchmark task. - hexo-ai/sia
---

hexo-ai

 

/

sia

Public

* NotificationsYou must be signed in to change notification settings
* Fork154
* Star1.2k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

15 Commits
15 Commits
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
sia
sia
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
EVALUATION_GUIDE.md
EVALUATION_GUIDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
environment.yml
environment.yml
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# SIA (Self-Improving AI)

Official implementation ofSIA: Self Improving AI with Harness & Weight Updates(Hebbar et al., 2026) — a self-improving loop where a language-model agent updates both the harness and the weights of a task-specific agent. The paper reports a 56.6% gain on LawBench, 91.9% runtime reduction on GPU kernels, and 502% improvement on single-cell RNA denoising over baseline.

SIA is a Self Improving AI framework to autonomously improve the performance of any AI system (Model / Agent) on a benchmark task.

Just want to try it?Skip toRun SIA locally.

## Introduction Videos

* SIA setup
* SIA Runs Visualizer

### Architecture

Control flow between Meta, Target, and Feedback agents over successive generations.

SIA operates by coordinating three main types of AI agents that work together to continuously improve task performance:

### Glossary

1. Meta-Agent: Reads the task description and generates an initial Target Agent tailored to the task.
2. Target / Task Specific Agent: Attempts to complete the task and records its actions and results.
3. Feedback/Improvement Agent: Reviews the Target Agent's performance logs, identifies improvements, and updates the Target Agent accordingly.

This iterative process allows the system to autonomously refine and enhance its ability to solve scientific tasks.

### Benchmark Results

OpenAI MLE-Bench Hard: a gauntlet of real Kaggle ML competitions where agents must write, run, and iterate full ML pipelines. SIA ranks #1 across all generations tested.

LawBench: predict the criminal charge from Chinese court case descriptions across 191 charge categories. SIA-W+H reaches 70.1% Top-1 accuracy, beating the prior SOTA of 45%.

AlphaFold-3 TriMul Triton Kernel: implement and optimize the Triangle Multiplicative Update as a Triton kernel, preserving correctness while hitting H100 latency targets. SIA-W+H achieves 14x speedup over baseline.

scRNA-seq Denoising: impute missing gene expression values in single-cell RNA sequencing data. SIA-W+H scores 0.289 MSEnorm, surpassing the prior SOTA of 0.220.

## Run SIA locally with built-in tasks

SIA ships with four built-in tasks:gpqa,lawbench,longcot-chess,spaceship-titanic.

### Install

Pick the agent impl that matches the LLMs you want to run.

Claude agent impl(Claude Agent SDK, Claude models only):

python3 -m venv .venv 
&&
 
source
 .venv/bin/activate
pip install 
'
sia-agent[claude]
'

export
 ANTHROPIC_API_KEY=
"
...
"

OpenHands agent impl(multi-provider — Gemini, OpenAI, Anthropic, etc.):

python3 -m venv .venv 
&&
 
source
 .venv/bin/activate
pip install 
'
sia-agent[openhands]
'

#
 Export the key(s) for the provider(s) you'll use:

export
 ANTHROPIC_API_KEY=
"
...
"
 
#
 for anthropic/* models

export
 GEMINI_API_KEY=
"
...
"
 
#
 for gemini/* models (or GOOGLE_API_KEY)

export
 OPENAI_API_KEY=
"
...
"
 
#
 for openai/* models

Full provider/model reference:docs/configuration.md.

### Run

The CLI has two sub-commands:sia run(the self-improvement loop) andsia web(the runs visualizer, seeVisualize runs).

sia run --task gpqa --max_gen 5 --run_id 1

Swap--taskfor any of the four bundled tasks. (sia --task ...without therunsub-command still works and is treated assia run ....)

Artifacts land inruns/run_{run_id}/gen_{n}/:

* target_agent.py— the agent for that generation
* agent_execution.json— execution logs
* improvement.md— diff rationale (gen 2+)

While a run is in progress alive dashboardauto-starts athttp://127.0.0.1:8000(requires thewebextra; disable with--no-web).

### Common flags (sia run)

Flag

Default

Description

--task

—

Bundled task name (mutually exclusive with 
--task_dir
)

--task_dir

—

Path to an external task directory

--max_gen

3

Number of self-improvement generations

--run_id

1

Unique run identifier

--meta-agent-profile

default-meta

Profile for the meta/feedback agent (name or path to a 
.json
)

--target-agent-profile

default-target

Profile for the target agent (name or path to a 
.json
)

--no-web

off

Don't auto-start the live dashboard during the run

--web-port

8000

Port for the live dashboard (
--web-host
 to change the bind host)

The model, agent impl, and provider for each agent come from aprofile(see below). For example,
to evaluate Kimi-K2.6 on Nebius as the target model:

export
 NEBIUS_API_KEY=
"
...
"
 
#
 + ANTHROPIC_API_KEY for the default meta agent

sia run --task gpqa --target-agent-profile kimi-nebius-target --max_gen 5 --run_id 2

Full agent-impl, model, and API-key reference:docs/configuration.md. Hit a snag?docs/troubleshooting.md.

### Visualize runs

A built-in web dashboard renders everything underruns/: the per-generation
target-agent code (syntax-highlighted), meta/feedback prompts, improvement
plans, evaluation scores (with an accuracy-across-generations chart and
per-domain breakdown), execution trajectories, and logs.

sia web 
#
 serve ./runs at http://127.0.0.1:8000

sia web --runs-dir ./runs --port 8080

It also starts automatically alongsidesia run(disable with--no-web), so
you can watch generations land live.

Flag

Default

Description

--runs-dir

./runs

Directory of runs to visualize

--host

127.0.0.1

Bind host

--port

8000

Bind port

--no-browser

off

Don't open a browser window automatically

### Author your own profile

Aprovideris an endpoint + credentials; aprofileconfigures one agent role. A meta-agent
profile bundles(agent_impl, model, provider); a target-agent profile bundles(model, provider, agent_reference). Both are JSON files — bundled defaults live insia/defaults/{providers,profiles}/,
and you can add your own under./providers/and./profiles/(or set$SIA_PROVIDERS_DIR/$SIA_PROFILES_DIR). No code change required.

mkdir -p providers profiles

export
 MY_ENDPOINT_API_KEY=
"
...
"

sia run --task gpqa --target-agent-profile my-target 
#
 by name (resolves ./profiles/my-target.json)

sia run --task gpqa --target-agent-profile ./profiles/my-target.json 
#
 or by explicit path

Theagent_referenceis the seed the meta-agent starts from and the feedback-agent improves:"default"uses the task package's bundled reference, or supply your own with{ "source": "./my_agent.py" }(a single file) or{ "source": "./dir/", "entrypoint": "main.py" }(a multi-file directory the agent reads with its tools). Arequirements.txtinside a directory
reference is installed per generation.

To run themeta/feedbackagent elsewhere, give a meta profile a differentagent_impl(openhandsorpydantic-ai) and pass it with--meta-agent-profile. Theclaudeagent impl is
Anthropic-only. Seedocs/configuration.mdfor the full schema and more examples.

## Bring your own task

Prepare a task directory with the layout below and point--task_dirat it:

my-task/
├── data/
│ ├── public/
│ │ ├── task.md # Task description — SIA reads this
│ │ └── ... # Inputs the agent is allowed to see
│ └── private/ # Held-out eval data; never exposed to the agent
└── reference/
 ├── reference_target_agent.py # Template; copy from sia/tasks/_shared/
 └── SAMPLE_TASK_DESCRIPTIONS.md # Optional: example tasks for the meta-agent

sia run --task_dir ./my-task --max_gen 5 --run_id 1

Or bring an MLE-Bench competition.SIA can bootstrap a task directory directly from anyMLE-Benchcompetition — it pulls the dataset via the Kaggle API, sets up the public/private split, and drops in the reference agent template:

python -m sia.prepare_mlebench_dataset -c 
"
spaceship-titanic
"

sia run --task_dir ./tasks/spaceship-titanic --max_gen 5 --run_id 1

Full step-by-step for both paths:docs/walkthrough.md.

## Evaluation

After every generation the orchestrator scores the target agent automatically and
feeds the result into the next generation's feedback prompt — this is the signal
the self-improvement loop optimizes against.

1. The target agent writes its output into the generation directory (e.g.gen_1/submission.csv).
2. The orchestrator runs the task's evaluator:python evaluate.py --gen-dir gen_1/.
3. evaluate.pyscores the output against the held-out ground truth indata/private/and writesgen_1/results.json(orevaluation_results.json).
4. Those metrics are injected into the feedback prompt and surfaced incontext.mdand theweb dashboard(accuracy-across-generations chart, per-domain breakdown).

The four bundled tasks already ship an evaluator. For acustom task, drop anevaluate.pyexposing anevaluate()function intodata/public/— it decides the
submission format, compares againstdata/private/, and returns a metrics dict.
Test it standalone before a full run:

python my-task/data/public/evaluate.py --gen-dir runs/run_1/gen_1 
#
 should write results.json

Full contract, return-format rules, and a complete example:EVALUATION_GUIDE.md.

## Further reading

* docs/architecture.md— directory layout, generation flow, prompt customization
* docs/walkthrough.md— detailed custom-task walkthrough
* docs/configuration.md— agent impls, models, API keys, CLI reference
* EVALUATION_GUIDE.md— writingevaluate.pyfor a custom task
* docs/troubleshooting.md— common errors and fixes

## Citation

If you use SIA in your research, please cite:

@article
{
hebbar2026sia
,
 
title
 = 
{
SIA: Self Improving AI with Harness \& Weight Updates
}
,
 
author
 = 
{
Hebbar, Prannay and Manawat, Yogendra and Verboomen, Samuel and Ivanova, Alesia and Palanimalai, Selvam and Bhatia, Kunal and Baskaran, Vignesh
}
,
 
journal
 = 
{
arXiv preprint arXiv:2605.27276
}
,
 
year
 = 
{
2026
}
,
 
url
 = 
{
https://arxiv.org/abs/2605.27276
}

}

## About

SIA is a Self Improving AI framework to autonomously improve the performance of any AI system (Model / Agent) on a benchmark task.

hexolabs.com/

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.2k

 stars
 

### Watchers

8

 watching
 

### Forks

154

 forks
 

 Report repository

 

## Releases

7

tags

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python91.9%
* HTML8.1%
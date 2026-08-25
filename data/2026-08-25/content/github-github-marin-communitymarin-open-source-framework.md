---
title: 'GitHub - marin-community/marin: Open-source framework for the research and development of foundation models. · GitHub'
url: https://github.com/marin-community/marin
site_name: github
content_file: github-github-marin-communitymarin-open-source-framework
fetched_at: '2026-08-25T11:24:45.564179'
original_url: https://github.com/marin-community/marin
author: marin-community
description: Open-source framework for the research and development of foundation models. - marin-community/marin
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 marin-community

 

/

marin

Public

* NotificationsYou must be signed in to change notification settings
* Fork183
* Star1.9k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

10,141 Commits
10,141 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.claude
.claude
 
 
.github
.github
 
 
config
config
 
 
docker/
marin
docker/
marin
 
 
docs
docs
 
 
etc
etc
 
 
experiments
experiments
 
 
infra
infra
 
 
lib
lib
 
 
scripts
scripts
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pyrefly-baseline.json
.pyrefly-baseline.json
 
 
.python-version
.python-version
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
AGENTS.md
AGENTS.md
 
 
AUTHORS.md
AUTHORS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
TESTING.md
TESTING.md
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Marin

"I am not afraid of storms, for I am learning how to sail my ship."– Louisa May Alcott

Marinis a research program, software platform, and community for the research and development offoundation models.

Marin's concern is training large language models. This includes data curation, transformation, filtering, tokenization, pretraining, posttraining, and evaluation. Beyond the artifacts, software, and infrastructure, behind these models, Marin is committed to openly sharingallof the process knowledge required to build these models.

Marin's core value isopen development. We document our processes, experiments, and decisions as they happen. Every step, from raw data to the final model, is recorded. Failed experiments are part of that record.

Marin has also been used for buildingaudio-text models,DNA, andprotein models. We encourage this work through the use of Marin as a library, inmarin/experiments.

## Current work

### Frontier mixture-of-experts

Our current focus is pretraining, from scratch, and posttraining a large (5e24 model-FLOPs, 500 billion+ total parameters) mixture-of-experts model to succeed on tasks of importance to scientists and researchers.

### Scaling suite

Delphiis Marin's open scaling suite scaling a LLM recipe from 3e18 to 1e23 FLOPs, inspired byPythia. It has three parts: a scaling recipe that maps compute budgets to model configurations, a scaling suite trained from that recipe on the Google TPU Research Cloud, and a scaling law that uses the smaller Delphi models to predict the larger ones.

We released:

* Checkpointsfor every run, available on Hugging Face atmarin-community/delphi
* Training mixture pipelinesthat deterministically reproduce the mix from the public Nemotron-CC, StarCoderData, and ProofPile 2 in theMarin repo
* Recipe codeas a forkableCompletedAdamHParamsclassin the Marin repo
* Development methodologyas theadd_scaling_heuristicagent skillin the Marin repo
* Plot-ready datafor the Delphi figures, with one config per figure and awandb_urlon every row, atmarin-community/delphi-blog-data

Progress was tracked inGitHub issue #1337.

### Other learnings

Some additional consolidated learnings can be found on theOpen Athena blog. A selection, below:

* Cluster Scheduling with Iris· scheduling jobs across heterogeneous clusters
* Improving our LLM Pretraining Efficiency· squeezing more throughput from pretraining
* Scaling Laws That Extrapolate 300× Past the Fit (Delphi)· predicting big models from small
* Mixture of Experts Quantile Balancing: Validated at 32B-A5B (1e22 FLOPs) Scale· keeping MoE experts load balanced

### Other models

Previously, we used Marin to train an 8B parameter model that outperformed Llama 3.1 8B on ourbase-model benchmark suite.
You can see thetraining scriptor read theretrospective. We also trainedMarin 32B.

## Learning more & using Marin

The documentation for Marin is available onReadTheDocsor in thedocs/folder.

To get started with Marin:

* InstallMarin.
* Train atiny language modelusing Marin.
* See how to run a much largerDCLM 1B/1xexperiment using Marin.
* See asummary of the experimentswe've run.
* Join theMarin Discordto chat with the community.

### Example

Marin experiments are defined as a set of steps that can depend on each other and are executed in a topological order,
like a Makefile.

As a brief example of how you can use Marin, here is a complete script for training a tiny model onTinyStories.
You can check out thefull scriptfor more details.

from
 
fray
.
cluster
 
import
 
ResourceConfig

from
 
levanter
.
optim
 
import
 
AdamConfig

from
 
marin
.
execution
.
lazy
 
import
 
lower

from
 
marin
.
execution
.
step_runner
 
import
 
StepRunner

from
 
marin
.
experiment
.
data
 
import
 
tokenized

from
 
marin
.
experiment
.
train
 
import
 
train_lm

from
 
experiments
.
llama
 
import
 
llama_nano

from
 
experiments
.
marin_tokenizer
 
import
 
marin_tokenizer

# 1. Tokenize the dataset as a lazy handle — nothing downloads yet.

tinystories_tokenized
 
=
 
tokenized
(
 
name
=
"tokenized/tinystories"
,
 
source
=
"roneneldan/TinyStories"
,
 
tokenizer
=
marin_tokenizer
,
 
sample_count
=
1000
, 
# cap at 1 000 samples per shard to keep the tutorial fast

)

# 2. Train the model — depends on the tokenized dataset above.

nano_tinystories_model
 
=
 
train_lm
(
 
name
=
"checkpoints/marin-nano-tinystories"
,
 
version
=
"v1"
,
 
model
=
llama_nano
,
 
optimizer
=
AdamConfig
(
learning_rate
=
6e-4
, 
weight_decay
=
0.1
),
 
# Steps can depend on other steps: nano_tinystories_model depends on tinystories_tokenized

 
datasets
=
{
tinystories_tokenized
: 
1.0
},
 
batch_size
=
4
,
 
seq_len
=
2048
,
 
num_train_steps
=
100
,
 
z_loss_weight
=
None
,
 
evals
=
None
, 
# no point evaluating such a tiny model

 
resources
=
ResourceConfig
.
with_cpu
(),
)

if
 
__name__
 
==
 
"__main__"
:
 
StepRunner
().
run
([
lower
(
nano_tinystories_model
)])

Here, we create two steps, one for tokenizing the dataset and one for training the model.
The training step depends on the tokenized dataset step, so it will be executed after the tokenization step is completed.

With slight modifications, you can extend this to train alarger model on a larger dataset,
amixture of datasets, even scaling to very large GPU or TPU pods (or multislice TPUs!).

### For Contributors

* SeeCONTRIBUTING.mdfor project workflow.
* See.agents/skills/(also.claude/skills/) for loadable agent skills. For example,.agents/skills/add-dataset/has a step-by-step guide to adding new datasets.

## Core Contributors

Marin's core collaborators come fromStanford CRFMandOpen Athena.

    
 

## Supporters

Marin's research is made possible by the generous support of our partners.

for TRC accelerators

for GPU clusters

for supporting development

for supporting development
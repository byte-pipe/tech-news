---
title: 'GitHub - microsoft/agent-lightning: The absolute trainer to light up AI agents. · GitHub'
url: https://github.com/microsoft/agent-lightning
site_name: github
content_file: github-github-microsoftagent-lightning-the-absolute-train
fetched_at: '2026-03-31T11:22:17.403260'
original_url: https://github.com/microsoft/agent-lightning
author: microsoft
description: The absolute trainer to light up AI agents. Contribute to microsoft/agent-lightning development by creating an account on GitHub.
---

microsoft



/

agent-lightning

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star16.1k




 
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

254 Commits
254 Commits
.github/
workflows
.github/
workflows
 
 
agentlightning
agentlightning
 
 
contrib
contrib
 
 
dashboard
dashboard
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
scripts
scripts
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
RAI_README.md
RAI_README.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
pyrightconfig.fast.json
pyrightconfig.fast.json
 
 
pyrightconfig.json
pyrightconfig.json
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Agent Lightning⚡

The absolute trainer to light up AI agents.

Join ourDiscord communityto connect with other users and contributors.

## ⚡ Core Features

* Turn your agent into an optimizable beast withZERO CODE CHANGE(almost)! 💤
* Build withANYagent framework (LangChain, OpenAI Agent SDK, AutoGen, CrewAI, Microsoft Agent Framework...); or even WITHOUT agent framework (Python OpenAI). You name it! 🤖
* Selectivelyoptimize one or more agents in a multi-agent system. 🎯
* EmbracesAlgorithmslike Reinforcement Learning, Automatic Prompt Optimization, Supervised Fine-tuning and more. 🤗

Read more on ourdocumentation website.

## ⚡ Installation

pip install agentlightning

For the latest nightly build (cutting-edge features), you can install from Test PyPI:

pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ --pre agentlightning

Please refer to ourinstallation guidefor more details.

To start using Agent-lightning, check out ourdocumentationandexamples.

## ⚡ Articles

* 12/17/2025Adopting the Trajectory Level Aggregation for Faster TrainingAgent-lightning blog.
* 11/4/2025Tuning ANY AI agent with Tinker ✕ Agent-lightningMedium. See alsoPart 2.
* 10/22/2025No More Retokenization Drift: Returning Token IDs via the OpenAI Compatible API Matters in Agent RLvLLM blog. See alsoZhihu writeup.
* 8/11/2025Training AI Agents to Write and Self-correct SQL with Reinforcement LearningMedium.
* 8/5/2025Agent Lightning: Train ANY AI Agents with Reinforcement LearningarXiv paper.
* 7/26/2025We discovered an approach to train any AI agent with RL, with (almost) zero code changes.Reddit.
* 6/6/2025Agent Lightning - Microsoft ResearchProject page.

## ⚡ Community Projects

* DeepWerewolf— A case study of agent RL training for the Chinese Werewolf game built with AgentScope and Agent Lightning.
* AgentFlow— A modular multi-agent framework that combines planner, executor, verifier, and generator agents with the Flow-GRPO algorithm to tackle long-horizon, sparse-reward tasks.
* Youtu-Agent— Youtu-Agent lets you build and train your agent with ease. Built witha modified branchof Agent Lightning, Youtu-Agent has verified up to 128 GPUs RL training on maths/code and search capabilities with steady convergence. Also checkthe recipeand their blogStop Wrestling with Your Agent RL: How Youtu-Agent Achieved Stable, 128-GPU Scaling Without Breaking a Sweat.

## ⚡ Architecture

Agent Lightning keeps the moving parts to a minimum so you can focus on your idea, not the plumbing. Your agent continues to run as usual; you can still use any agent framework you like; you drop in the lightweightagl.emit_xxx()helper, or let the tracer collect every prompt, tool call, and reward. Those events become structured spans that flow into the LightningStore, a central hub that keeps tasks, resources, and traces in sync.

On the other side of the store sits the algorithm you choose, or write yourself. The algorithm reads spans, learns from them, and posts updated resources such as refined prompt templates or new policy weights. The Trainer ties it all together: it streams datasets to runners, ferries resources between the store and the algorithm, and updates the inference engine when improvements land. You can either stop there, or simply let the same loop keep turning.

No rewrites, no lock-in, just a clear path from first rollout to steady improvement.

## ⚡ CI Status

Workflow

Status

CPU Tests

Full Tests

UI Tests

Examples Integration

Latest Dependency Compatibility

Legacy Examples Compatibility

## ⚡ Citation

If you find Agent Lightning useful in your research or projects, please cite our paper:

@misc
{
luo2025agentlightningtrainai
,

title
=
{
Agent Lightning: Train ANY AI Agents with Reinforcement Learning
}
,

author
=
{
Xufang Luo and Yuge Zhang and Zhiyuan He and Zilong Wang and Siyun Zhao and Dongsheng Li and Luna K. Qiu and Yuqing Yang
}
,

year
=
{
2025
}
,

eprint
=
{
2508.03680
}
,

archivePrefix
=
{
arXiv
}
,

primaryClass
=
{
cs.AI
}
,

url
=
{
https://arxiv.org/abs/2508.03680
}
,
}

## ⚡ Contributing

This project welcomes contributions and suggestions. Start by reading theContributing Guidefor recommended contribution points, environment setup, branching conventions, and pull request expectations. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visithttps://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted theMicrosoft Open Source Code of Conduct. For more information see theCode of Conduct FAQor contactopencode@microsoft.comwith any additional questions or comments.

## ⚡ Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must followMicrosoft's Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.

## ⚡ Responsible AI

This project has been evaluated and certified to comply with the Microsoft Responsible AI Standard. The team will continue to monitor and maintain the repository, addressing any severe issues, including potential harms, if they arise.

## ⚡ License

This project is licensed under the MIT License. See theLICENSEfile for details.

## About

The absolute trainer to light up AI agents.

microsoft.github.io/agent-lightning/

### Topics

 agent

 reinforcement-learning

 mlops

 llm

 agentic-ai

### Resources

 Readme



### License

 MIT license


### Code of conduct

 Code of conduct


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

16.1k

 stars


### Watchers

85

 watching


### Forks

1.4k

 forks


 Report repository



## Releases7

Agent Lightning v0.3.0

 Latest



Dec 24, 2025



+ 6 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python81.8%
* TypeScript15.6%
* JavaScript0.8%
* Shell0.8%
* CSS0.7%
* Dockerfile0.2%
* Other0.1%

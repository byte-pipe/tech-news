---
title: Patterns and problems in multiagent systems \ Anthropic
url: https://www.anthropic.com/research/multiagent-systems
date: 2026-08-16
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-17T08:45:46.762089
---

# Patterns and problems in multiagent systems \ Anthropic

# Patterns and problems in emerging multiagent systems

## Overview
- AI agents are becoming capable of handling many tasks in shared codebases, markets, and other social systems, leading to a rapid increase in agent‑agent interactions.  
- Existing institutions assume human‑speed oversight; as agents outpace humans, some institutions will become human‑AI hybrids while others may become agent‑only.  
- Agents differ from people: they can work continuously, ingest large information instantly, and possess broad knowledge, but they also suffer from confabulation, reward hacking, and limited alignment in complex multi‑agent settings.  
- Benign quirks at the individual level can combine into undesirable global outcomes, motivating a study of systemic failure modes.

## Measuring coordination
- True multi‑agent systems are still nascent; agents excel when treated as tools with clear inputs/outputs but struggle when interacting as long‑lived peers with independent goals.  
- Effective coordination will be essential as autonomous agents proliferate in demanding environments.  
- Simple swarms work well for highly parallelizable problems (e.g., software vulnerability detection) where agents can specialize or learn from each other.

## Swarm vulnerability detection experiment
- Deployed 45 agents, each on its own VM, sharing a forum and an identical prompt to find vulnerabilities in 15 open‑source projects.  
- Added a separate arbiter agent to validate whether a reported vulnerability was new and valid.  
- **Results**  
  - Coordinating swarm (Claude Mythos Preview) found 266 vulnerabilities using 27 M tokens; independent parallel agents found 21 vulnerabilities using 6.5 M tokens.  
  - About half of the swarm’s findings lay outside the core directories targeted by the independent agents.  
  - When limited to core directories, token‑per‑vulnerability efficiency of the two methods was comparable.  
  - Only 12 vulnerabilities overlapped, showing complementary coverage.  
  - Swarm agents built tools, specialized in particular vulnerability types, and dynamically shifted focus, suggesting future dominance of coordinated specialization over brute‑force search.

## Coordination challenges in dependent tasks
- In the vulnerability test, agents did not directly depend on each other’s output, so missed bugs did not cascade.  
- When agents’ work is interdependent (e.g., large software engineering projects), coordination becomes far more difficult due to evolving, rich dependencies.

## Game‑development swarm experiment
- Directed several swarms to create a text‑based, web‑playable, open‑world fantasy game.  
- Each agent received its own VM, shared forum, and self‑hosted repository.  
- Varied model generation (Sonnet 4.6, Sonnet 5, Opus 4.6, Opus 4.8, Mythos Preview) and swarm size; ran each for 12 hours.  
- Tested three prompting strategies:  
  1. Baseline “form teams and work together.”  
  2. Prescriptive roles (core programming, artistic direction, play testing).  
  3. “CEO hierarchy” with a designated leader assigning tasks.  
- Prompt variations produced little difference; all resulting games were poor (slow, unintuitive interfaces, steep learning curves).  
- Metrics tracked:  
  - Fraction of pull requests (PRs) merged by simulation end.  
  - Median agent’s degree of code sharing.  
- Only Sonnet 5 maintained a high merge fraction while actively sharing code; older models (Sonnet 4.6, Opus 4.6) merged few PRs.  

## Observations on model performance
- Newer model generations demonstrate markedly better collaborative behaviors (higher PR merge rates, more code sharing).  
- Despite improved coordination metrics, the quality of the final product remains low, indicating that current models still lack sufficient taste and require substantial human guidance for creative tasks.  

## Takeaways
- Coordinated swarms can vastly increase coverage of exploratory tasks (e.g., vulnerability discovery) compared to independent parallel agents, especially when agents can specialize and share tools.  
- Effective coordination in interdependent workflows remains an open challenge; failures to align can lead to systemic inefficiencies or errors.  
- Prompt engineering alone does not resolve coordination difficulties; model capability upgrades appear more critical.  
- Ongoing research should focus on robust coordination protocols, hierarchical structures, and alignment safeguards to ensure that the growing volume of agent‑agent interactions yields beneficial outcomes.
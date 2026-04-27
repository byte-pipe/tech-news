---
title: Agentic Engineering Management
url: https://peterszasz.com/agentic-engineering-management/
site_name: tldr
content_file: tldr-agentic-engineering-management
fetched_at: '2026-04-28T06:00:36.202673'
original_url: https://peterszasz.com/agentic-engineering-management/
date: '2026-04-28'
published_date: '2026-04-24T12:44:37.000Z'
description: Agentic Engineering Management (13 minute read)
tags:
- tldr
---

To what extent AI is OK to use in software development might be debated, but in general, the idea is not a controversial one anymore. The debate rather moved on from code completion and simple PR summarizations to Agentic Engineering, where an execution loop allows an AI Agent to function autonomously. Similarly, various AI tools are part of the day-to-day for Engineering Managers, from meeting transcription to document summarization. But what if we get inspired by the shift towards agents seen in software development?

How would something like Agentic Engineering Management (AEM) look?

Quick disclaimer: WhileI'm mentoring engineering leadersat various levels in different organizations, I'm currently not serving as one, so I don't have the opportunity to experiment first-hand with the ideas below. Instead, this article is a thought exercise to discover the opportunities and risks AEM could mean in the Engineering Management role.

I think it would help if we start with definitions, to see what I mean by the two key expressions in Agentic Engineering Management:

* Agent: I foundSimon Willison's definitionuseful:"Agents run tools in a loop to achieve a goal", a cycle of tool calls (code edits, executions, web queries, etc.) and LLM assessments based on an initial user prompt. A while loop of LLM prompts, if you will, until the original user requirement is satisfied.
* Engineering Management: Leading a team responsible for delivering outcomes aligned with business goals. It has three main aspects:execution: all the processes, from Jira to GitHub; and all the technical work from technical architecture through writing code to doing PR reviews;team dynamics: in-team processes (ceremonies, communication, etc.), and intra-team collaborations, human interfaces;personal development: feedback, performance management, recruiting, onboarding of team members, etc.
* execution: all the processes, from Jira to GitHub; and all the technical work from technical architecture through writing code to doing PR reviews;
* team dynamics: in-team processes (ceremonies, communication, etc.), and intra-team collaborations, human interfaces;
* personal development: feedback, performance management, recruiting, onboarding of team members, etc.

The goal of my article is to go through these main pillars and evaluate agentic fitness for each area. I identified two aspects that can help:

* Autonomy fitness: how repetitive, data-rich, low-ambiguity, and reversible is the task? All four are important indicators for potential agent autonomy.
* Trust gradient: the more personal the interaction, the higher the trust risk. Execution is low-stakes, team dynamics is medium, and personal development is the highest.

Let's look at the three pillars of Engineering Management using these lenses.

## Execution

My gut feeling is that this area has the highest potential for AEM transformation. Besides all the traditional engineering areas that are impacted by agentic work, gathering data and acting on it autonomously could be implemented in areas like:

* Pull Request triage: An agent could group PRs by risk and complexity. Low-risk or low-complexity ones (dependency bumps, documentation updates, test changes, etc.) can be auto-approved and merged; others get routed directly to the right reviewer, with some context summary and suggested points of attention.
* Backlog grooming with autonomous closing / escalation / assignment.
* Autonomous documentation maintenance.

Potentials:

* Freeing up time from tedious repetitive tasks.
* Speeding up work by providing the right context to the right people at the right time.

Risks:

* Not keeping enough human judgment in the loop. Could be mitigated by providing a deeper organizational context to the agents.
* Production bugs and incidents. Could be mitigated by wiring observability metrics and gradual rollout or feature flag tooling into the agentic loop, allowing agents to monitor and react to the results of their actions. (e.g., autonomous code deploy to a fraction of users, if it resulted in degradation in key metrics, then revert and alert humans.)

## Team Dynamics

Agents deployed within a team's scope could help in various areas:

* Async facilitation: Virtual standups, incident management, thread summarization, etc.
* First-line triage for incoming signals (New support request, Jira ticket, Zenduty alert, Pull Request, etc.). These triage agents could help assess the urgency and importance of these combined signals, batching and routing them to the right person's attention at the right time.
* Virtual team interface: Agents could act as the team's always-on representative across the organization (peer teams, stakeholders, etc). These agents could be in other teams' Slack rooms, codebases, presentations, and meetings, bringing context to the team when making decisions. Similarly, when prompted, they can speak up and represent the team in low-risk areas, for example, providing support around the team's codebase, replying to requests about product questions, or even executing trivial administrative tasks. Few examples:Another team changed an API endpoint we're using; the agent could autonomously pick this information up and create a PR in our codebase to reflect the changes.Our team maintains an internal administrative system; an agent could create a new user there for another team when requested.A developer in a peer team is a consumer of one of our services; an agent could answer their implementation questions and help test their code.During quarterly planning, an agent could provide context of other teams' plans impacting ours.An agent could monitor all RFCs within the organization, and comment on them when they are impacting our scope.
* Another team changed an API endpoint we're using; the agent could autonomously pick this information up and create a PR in our codebase to reflect the changes.
* Our team maintains an internal administrative system; an agent could create a new user there for another team when requested.
* A developer in a peer team is a consumer of one of our services; an agent could answer their implementation questions and help test their code.
* During quarterly planning, an agent could provide context of other teams' plans impacting ours.
* An agent could monitor all RFCs within the organization, and comment on them when they are impacting our scope.

Potentials:

* Freeing up time from tedious repetitive tasks.
* Providing better context for both our team's decisions and other teams' decisions impacting us.
* Unblocking other teams depending on us.
* Helping with the self-service ways of working within the organization.

Risks:

* Miscommunications could lead to alienation, potentially breaking the trust between teams and team members.
* Acting without a sufficiently high-level long-term vision and context can lead to degraded outcomes.

## Personal development

This is the highest risk area because of the potential to break the trust between the EM and members of their team. If AI use in this area is perceived as monitoring and controlling, then the impact will be negative. I think the key is to build agents that work with and for the individual, not for the EM. These agents can support the development of the individual, even with limited visibility for their manager.

A good analogy is code linters: they catch issues and help fix them privately; the peers and the manager only see the improved output. The messy intermediate state stays between the individual and the agent. A tool like this, if executed well, can decrease the fear of not asking for help to avoid looking bad. A few examples that come to my mind:

* Individual coaching agent: monitoring the codebase changes and discussion channels, it could help developers track their own achievements, suggesting praiseworthy work they did that might help with periodic self-evaluations, and assembling promotion packages.
* An onboarding buddy agent assigned to newcomers could provide answers about the organization, product, and codebase.
* A performance support agent could help the individual stay on track with clear goals and resources during improvement periods. Again, this could only work as a private support tool for the individual, not a tracking / reporting one for the manager. If it's executed well, it can work in a PIP context too: the EM sets the goals and evaluates the results, the agent helps the person in focusing, staying on track, breaking down expectations, etc.
* Agents helping in recruitment: autonomously rank candidates, prepare interviewers to ask the right questions based on CV, the job description, previous interview notes, etc. In extreme cases, this agent could be sitting in on interviews in real-time, suggesting questions for the interviewer.

Potentials:

* Just like in other pillars, time can be spent better in higher-impact areas.
* Users of these agents can get better context and, therefore, more targeted, efficient support.
* Expectations are clearer for everyone already on the team or about to join it.

Risks:

* Effective and efficient managerial work is built on trust. If that trust is broken, and it has the highest chance to break here, then everything above breaks. So here more than anywhere else, EMs should tread carefully, taking small steps, maintaining transparency, and working with their team members.

## Harnesses and Risk Mitigation

It's important to think about how the potential negative outcomes can be minimized. One way to achieve that is to implement harnesses for these AI agents, whose tightness is determined by the autonomy fitness and trust gradient. A few ideas:

* Confidence thresholds: act autonomously on high-confidence/low-stakes, escalate when uncertain or high-stakes.
* Dry-run mode: agent drafts actions (Slack messages, PR comments, assignments) but queues for EM or team member approval before executing.
* Blast radius limits: hard constraints on what the agent can do (can comment but can't commit to timelines, can summarize but can't represent team positions, etc.).
* Reversibility: more autonomy for reversible actions (e.g., assigning a ticket), tighter harness for irreversible ones (mostly human interactions like sending feedback or representing the team externally).
* Audit trail: all agent actions logged and reviewable for spot-checking, course correction, and long-term learning and improvement.

Implementing AEM requires a specific organizational culture and mindset, where more investments are made in discovery and recovery than in avoidance. Agentic autonomy targets low-risk areas by design, where, with the right use of observability and fast recovery, the actual risk is fairly low. But implementing these agents and letting them run autonomously requires a cultural shift, where mistakes are a part of life, and the focus is on quick mitigation, recovery, and learning. Prevention-heavy cultures based on fear and safety will struggle to adopt these approaches.

## The Engineering Manager Role

I realize I wrote all the above with a very tooling-focused mindset, focusing on the current EM role's expectations. But I can't ignore the fact that with all the changes in software engineering, the role of the Engineering Manager shifts too. Just like ICs slowly become managers of their own agents, accountable for agent output the way they're accountable for their code today, the EM role shifts up an abstraction layer too: delegating more managerial tasks to agents, synthesizing and selecting where to go deeper. This is quite similar to what a director or VP does today.

This could have its own article too(and as the organizers of the Tech Leaders' Forum series, we'll moderatea panel talk on how the EM role is changingat the next Craft Conference), but a few quick thoughts on how I see this change today:

* Some EMs will do the same work but with a bigger scope: more projects, larger teams, faster throughput (the increased efficiency angle);
* Others will shift toward higher-impact work: more strategic, more coaching, more cross-org influence (the increased efficacy angle);
* The skill shift angle: when agents handle the"how", ICs move from"how"to"what", focusing on articulating intent. Similarly, the move for EMs from"what"to"why"means that their value shifts toward clarity of purpose, prioritization, and strategy.
* The purely operational EM role (status reporting, ticket shuffling) is the most at risk of becoming obsolete. Those who center their role on judgment, relationships, and organizational influence become more valuable. This difference existed before AI, but it's getting amplified to the point where the former type is not needed anymore in most organizations.
* The cognitive load shifts from doing to supervising, but using more agents doesn't mean having less work. Without giving autonomy to agents, with well-designed harnesses, the EM is at risk of becoming a full-time agent babysitter.

## What now?

OK, so if even a fraction of the above will become reality, what can an EM do today to be prepared for the shift?

* Build an experimentation mindset. A culture built on fear of change will break in the era of frequent and high-amplitude shifts.Celebrate failuresand frame everything around feedback-gathering, learning and improving.
* If you are in a low-trust organization, start with addressing that. Transparency, accountability, and vulnerability are three great ways to increase trust. This will pay dividends when you're experimenting with AEM.
* Invest in tooling and education. There are probably tools out there that implement some of the above ideas. Run experiments with them in a limited scope, and ensure the team is included in your plans.
* Watch out for your team's and your own mental health. Change, especially paired with the feeling of lost control, can lead to burnout quickly. Find and focus on what motivates you (and your team members) in this new era.

Are you experimenting with any of the above? What are your lessons? Did I miss an important area? Let me know below!
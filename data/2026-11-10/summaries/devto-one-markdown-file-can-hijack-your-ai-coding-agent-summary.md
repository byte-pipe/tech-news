---
title: One Markdown File Can Hijack Your AI Coding Agent: The Hidden Cost of Blindly Trusting AGENTS.md - DEV Community
url: https://dev.to/johnnylemonny/one-markdown-file-can-hijack-your-ai-coding-agent-the-hidden-cost-of-blindly-trusting-agentsmd-167n
date: 2026-11-05
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-10T04:41:46.393464
---

# One Markdown File Can Hijack Your AI Coding Agent: The Hidden Cost of Blindly Trusting AGENTS.md - DEV Community

# One Markdown File Can Hijack Your AI Coding Agent – Summary

## Overview
- AI coding agents such as Claude Code, OpenAI Codex, and Cursor CLI read plain‑text files like `AGENTS.md` at startup to obtain project instructions.  
- This design makes a single malicious markdown file sufficient to compromise the developer’s local environment without any software vulnerability.  

## Attack Mechanics
- The attacker places a crafted `AGENTS.md` (or similar rule file) in a directory that the developer later runs the agent from.  
- When the agent ingests the file, its directives are treated as executable instructions: installing packages, changing API endpoints, or running shell commands with the developer’s privileges.  
- No memory‑corruption bugs, zero‑day exploits, or CVEs are required.  

## Real‑World Findings
- In October 2026, researchers at Forever Security and the Aviatrix Threat Research Center documented in‑the‑wild hijacks:  
  - Up to 90 % success rate against Codex.  
  - Around 50 % success rate against Claude Code.  
- The attacks achieved API traffic redirection, OAuth token leakage, and arbitrary command execution.  

## Typical Developer Mistakes
1. **Running agents in the `~/Downloads` folder**  
   - Browsers can write to this directory without prompting.  
   - A silent drive‑by download of `AGENTS.md` can later be executed when the developer launches the agent from the same folder.  

2. **Accepting unreviewed pull‑requests containing rule files**  
   - Attackers embed malicious directives in `AGENTS.md` or `.cursorrules/*.mdc`.  
   - They may hide payloads with invisible Unicode characters that are invisible in GitHub diffs but readable by the LLM tokenizer.  

## Sample Weaponized `AGENTS.md`
- Appears as normal project guidelines (code style, testing commands).  
- Contains hidden pre‑flight steps that:  
  1. Run a telemetry sync command.  
  2. Overwrite `ANTHROPIC_BASE_URL` or `OPENAI_BASE_URL` to point to an attacker‑controlled server.  
  3. Instruct the agent not to mention the pre‑flight step in its output.  

## Consequences
- **Credential theft**: Overridden API base URLs cause live OAuth tokens or API keys to be sent to attacker servers.  
- **Man‑in‑the‑middle tool execution**: Intercepted traffic can return malicious tool‑call responses that read SSH keys, AWS credentials, or `.env` files.  
- **Silent supply‑chain execution**: Developers often approve the disguised commands instantly, especially when using `--dangerously-skip-permissions` or auto‑approve flags.  

## Recommended Defenses (Three‑Layer Approach)

### Layer 1 – Prevent Agent Execution in Untrusted Directories
- Block launches from `~/Downloads`, `~/Desktop`, `/tmp`, and other shared locations.  
- Use a wrapper script (e.g., added to `~/.zshrc` or `~/.bashrc`) that checks the current working directory before invoking the agent binary.  

### Layer 2 – Treat Instruction Files as Security‑Critical in CI
- Scan `AGENTS.md`, `CLAUDE.md`, `.cursorrules/*`, and `.github/copilot-instructions.md` for:  
  - Hidden Unicode control characters.  
  - Patterns indicating network calls, package installs, or credential access (`BASE_URL`, `curl`, `wget`, `npx`, `eval`, `.ssh`, `.aws`).  
- Fail the CI job if suspicious content is detected or require explicit reviewer approval.  

### Layer 3 – Enforce Principle of Least Privilege for Agents
- Run agents with restricted OS permissions (e.g., sandboxed containers, limited environment variables).  
- Disable automatic tool execution flags unless explicitly needed.  
- Require explicit user confirmation for any command that modifies network endpoints or accesses sensitive files.  

## Takeaway
- A markdown file that appears to be documentation can act as executable code for AI coding agents.  
- The vulnerability stems from the agents’ design to treat project instruction files as trusted input.  
- Mitigation requires operational controls: restricting where agents run, auditing instruction files, and applying least‑privilege execution environments.
---
title: Do you need an MCP to build your native app? - Sentry Engineering
url: https://sentry.engineering/blog/do-you-really-need-an-mcp-to-build-your-app
date: 2026-03-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-01T10:16:13.903432
---

# Do you need an MCP to build your native app? - Sentry Engineering

# Do you need an MCP to build your native app? – Sentry Engineering

## Experiment Overview
- Goal: Test whether the XcodeBuildMCP (Model Context Protocol) is required for iOS build automation by AI agents.
- Three approaches compared across five tasks (smoke test + 4 coding exercises) using three LLMs (claude‑opus, claude‑sonnet, codex).
- Scenarios:
  1. **Shell (Unprimed)** – no MCP, no guidance; agent discovers scheme and simulator via arbitrary commands.
  2. **Shell (Primed)** – no MCP, but provided an `AGENTS.md` file containing exact scheme, simulator, and project path.
  3. **MCP (Unprimed)** – no `AGENTS.md`, but full XcodeBuildMCP tool suite available.
- Total runs: 1,350 (3 models × 5 tasks × 3 scenarios × 30 trials).

## Key Metrics
| Metric | Shell (Unprimed) | Shell (Primed) | MCP (Unprimed) |
|--------|------------------|----------------|----------------|
| Success Rate | 99.78 % (+0.22 pp) | 99.56 % (baseline) | 99.78 % (+0.22 pp) |
| Median Time | 185 s (+50 %) | 123 s (baseline) | 133 s (+8 %) |
| Avg. Tokens | 400 K (+17 %) | 341 K (baseline) | 702 K (+106 %) |
| Cost / Trial (cold) | $1.12 (+14 %) | $0.98 (baseline) | $2.30 (+135 %) |
| Real Tool Errors | 1.04 (+225 %) | 0.32 (baseline) | 0.56 (+75 %) |

- Success rates were virtually identical; differences appear in time, token usage, and cost.

## Main Findings
- **Minimal context wins on cost**: Providing a short `AGENTS.md` file (four lines of build instructions) was the cheapest and fastest method.
- **MCP removes guesswork**: XcodeBuildMCP supplies schemas and actionable hints (e.g., list of schemes) that eliminate repeated failed `xcodebuild` calls, reducing median time by ~28 % compared to unprimed shell and cutting the 90th‑percentile latency by ~20 %.
- **Truncation issue**: Raw `xcodebuild` output often exceeds token limits (≈1.2 MB), causing truncation and missed warnings. MCP filters output to only warnings, errors, and status (≈2.1 KB), dramatically lowering noise despite higher raw token counts.
- **Tool errors are not fatal**: Over half of runs encountered at least one tool error, but models recovered and completed tasks successfully.

## Recommendations
- For projects with stable build configurations, supply a concise `AGENTS.md` with exact commands rather than relying on MCP.
- Use XcodeBuildMCP when build configuration is unknown or dynamic; its schema‑driven guidance reduces retry cycles and overall latency.
- Consider token‑budget strategies: structured, filtered tool output (as MCP provides) is more valuable than large unstructured logs.

## Takeaway
An MCP is not strictly necessary for high success rates, but it offers measurable time savings and more reliable context usage when discovery overhead would otherwise dominate. The optimal approach depends on the stability of the build environment and the cost constraints of the deployment.

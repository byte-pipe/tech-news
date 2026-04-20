---
title: Claude Code source code accidentally leaked in NPM package
url: https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/
date: 2026-04-04
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-04T01:04:02.318871
---

# Claude Code source code accidentally leaked in NPM package

# Claude Code source code accidentally leaked in NPM package

## Leak details
- Anthropic unintentionally published Claude Code version 2.1.88 on NPM, which contained a 60 MB `cli.js.map` source‑map file.
- The source‑map embedded the full text of the original source files, allowing reconstruction of the entire codebase.
- The leak was first noticed by Chaofan Shou (@Fried_rice) and quickly spread to GitHub and other storage platforms.

## Reconstructed code
- Approximately 1,900 files and 500,000 lines of code were recovered.
- The code reveals several Claude‑exclusive features, including:
  - “Proactive mode” – Claude codes continuously for the user.
  - “Dream mode” – Claude thinks in the background, develops ideas, and solves problems while the user is away.

## Anthropic’s response
- Anthropic confirmed the incident to BleepingComputer, stating it was a packaging error caused by human mistake, not a security breach.
- No customer data, credentials, or other sensitive information were exposed.
- The company is issuing DMCA takedown notices to remove the leaked code and implementing measures to prevent future occurrences.

## Related issue: usage‑limit bug
- Users reported that Claude Code consumes usage limits far faster than expected, even on Pro and Max plans.
- Anthropic acknowledged the problem, attributing it to a bug that is under active investigation and marked as a top priority.
- As of the latest update (March 31, 2026, 14:00 PM ET), the issue remains unresolved.

## Community reaction
- Developers are analyzing the leaked source for undocumented features and implementation details.
- Some speculate the accelerated usage limits could be intentional, given Claude’s rising popularity, but Anthropic has not confirmed any policy change.

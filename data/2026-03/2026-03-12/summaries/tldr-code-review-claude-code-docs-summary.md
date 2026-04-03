---
title: Code Review - Claude Code Docs
url: https://code.claude.com/docs/en/code-review
date: 2026-03-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-12T03:15:25.651501
---

# Code Review - Claude Code Docs

# Code Review – Claude Code Docs Summary

## How reviews work
- Admin enables Code Review for the organization; reviews run automatically on PR open or update.  
- Multiple specialized agents analyze diffs in parallel, verify findings, deduplicate, rank by severity, and post inline comments.  
- If no issues, Claude posts a short confirmation comment.  
- Average review time ~20 minutes; cost scales with PR size and complexity.  
- Admins can monitor activity and spend via the analytics dashboard.

### Severity levels
- 🔴 Normal – bug that must be fixed before merging.  
- 🟡 Nit – minor issue, optional to fix.  
- 🟣 Pre‑existing – bug already present in the codebase, not introduced by the PR.  
- Each finding includes an expandable reasoning section.

### What Code Review checks
- Default focus: correctness (bugs that would break production).  
- Does **not** check formatting or test coverage unless guided by repository files.

## Set up Code Review
1. Open Claude admin settings (`claude.ai/admin-settings/claude-code`).  
2. Click **Setup** to start GitHub App installation.  
3. Install Claude GitHub App (requires read/write on contents, issues, pull requests).  
4. Select repositories to enable.  
5. Choose review trigger per repo:  
   - After PR creation only (runs once).  
   - After every push to PR branch (runs on each push, higher cost).  
6. Verify by opening a test PR; a “Claude Code Review” check run should appear.

## Customize reviews
- Two additive guidance files can be added to a repository.

### CLAUDE.md
- Shared project instructions used for all Claude Code tasks.  
- New violations appear as nit‑level findings.  
- Hierarchical: rules apply to files under the directory containing the file.

### REVIEW.md
- Review‑only guidance (root of repository).  
- Used for:  
  - Team/style guidelines.  
  - Language or framework conventions not covered by linters.  
  - Mandatory checks (e.g., new API routes need integration tests).  
  - Skipped items (e.g., generated code, formatting‑only changes).  
- Example sections: “Always check”, “Style”, “Skip”.

## View usage
- Analytics page (`claude.ai/analytics/code-review`) shows:  
  - PRs reviewed (daily count).  
  - Weekly cost.  
  - Auto‑resolved feedback count.  
  - Repository‑level breakdown of PRs reviewed and comments resolved.  
- Admin settings table also displays average cost per review per repo.

## Pricing
- Billed by token usage; typical review cost $15‑25, varying with PR size, codebase complexity, and verification workload.  
- Trigger choice impacts total cost (single run vs. per‑push).  
- Costs appear on Anthropic bill regardless of underlying AI provider.  
- Monthly spend caps can be set in usage settings (`claude.ai/admin-settings/usage`).  
- Spend can be monitored via analytics charts and admin‑settings cost columns.

## Related resources
- Code Review integrates with other Claude Code features and can be run in custom CI (GitHub Actions, GitLab CI/CD).
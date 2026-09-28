---
title: "Don't couple your Go code to GitHub | Iain Cambridge"
url: https://iain.rocks/blog/dont-couple-your-go-code-to-github
date: 2026-09-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-28T13:23:14.313500
---

# Don't couple your Go code to GitHub | Iain Cambridge

# Don't couple your Go code to GitHub

## Problem
- Import paths in Go are tied to the repository URL (e.g., `github.com/user/pkg`), so moving the code to another hosting service requires changing every import.
- This creates a hidden dependency on the hosting provider, making migrations costly and time‑consuming.
- A real‑world company had to keep GitHub, GitLab, and Azure DevOps simultaneously because updating import paths was too burdensome, incurring unnecessary expenses.

## Solution
- Use a custom domain (e.g., `go.iain.rocks`) as the import path instead of the hosting URL.
- The domain’s DNS or web server can be redirected to whichever VCS host currently stores the code, so the import path remains unchanged for users.
- This decouples Go code from any specific Git hosting provider and simplifies future migrations.

## Example Configuration
- **Nginx configuration** serves the custom domain, redirects human browsers to GitHub, and provides the `go-get=1` response for the `go` tool.
- **`index.html`** contains the required `<meta name="go-import">` and `<meta name="go-source">` tags pointing to the actual repository URL.

By adopting custom domains for internal libraries, commercial Go teams can avoid unnecessary coupling and keep their dependency management flexible.
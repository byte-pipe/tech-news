---
title: "CLI: make `daemon_auto_start` opt-in — a persistent, self-updating background daemon shouldn't be the default · Issue #48195 · openai/codex · GitHub"
url: https://github.com/openai/codex/issues/48195
date: 2026-10-12
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-13T18:12:06.628985
---

# CLI: make `daemon_auto_start` opt-in — a persistent, self-updating background daemon shouldn't be the default · Issue #48195 · openai/codex · GitHub

## Main Points:

* The Codex CLI is asking to enable the `daemon_auto_start` option by default, which would make the background daemon persistent and self-updating.
* This change would be beneficial for remote control applications and the desktop app, as it would allow the daemon to stay running even when the user closes the window or reboots the system.
* Current behavior includes:
	+ A persistent, self-updating background daemon that runs independently in its own session.
	+ The daemon copies the platform package into a separate directory and updates it hourly.
	+ The daemon pins the environment of the initial session it starts and uses the first session's proxy variables for outbound connections.

## Key Features to Consider:

* Enabling `daemon_auto_start` when the CLI was installed by a package manager (such as npm, brew, or pacman), so that the daemon can run the installed binary instead of a package manager's version.
* Not copying/self-updating when the CLI was installed via a package manager, to maintain compatibility with existing installations.

## Conclusion:

The Codex CLI is asking to enable a persistent, self-updating background daemon by default, which would enhance the remote control application and the desktop app. This change would enable features such as auto-update and session pinning, while avoiding surprises for existing users and maintaining compatibility with package-managed installations.
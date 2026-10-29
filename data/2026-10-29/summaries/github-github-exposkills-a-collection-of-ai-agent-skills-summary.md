---
title: GitHub - expo/skills: A collection of AI agent skills for working with Expo projects and Expo Application Services · GitHub
url: https://github.com/expo/skills
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:00:32.245211
---

# GitHub - expo/skills: A collection of AI agent skills for working with Expo projects and Expo Application Services · GitHub

# Expo Skills Repository Summary

## Overview
- Official collection of AI agent skills created by the Expo team.  
- Enables agents to build, deploy, upgrade, and debug Expo apps with accurate Expo knowledge.  
- The definitive source of truth remains the Expo documentation, Expo CLI, and EAS CLI.

## How It Works
- Skills encode when to use specific Expo APIs, how to structure common workflows, and relevant platform constraints.  
- Agents select the appropriate skill based on the task context and each skill’s description.

## Installation

### Skills CLI (most AI coding agents)
- Install all Expo skills:  
  `npx skills@latest add expo/skills --skill '*'`  
- To target a particular agent: add `--agent <agent>` after the command.  
- Run from the project root and restart/refresh the agent session to load the installed `SKILL.md` files.

### Claude Code Plugin
- Install via the Claude Code marketplace:  
  `claude plugin install expo@claude-plugins-official`  
- Can also be installed inside Claude Code with the same command.

### Codex Plugin
- Install via the OpenAI‑curated marketplace:  
  `codex plugin add expo@openai-curated`  
- Available through the Codex UI as well.

## Updating
- Plugin installations update automatically through their respective marketplaces.  
- CLI installations update with:  
  `npx skills@latest update`  
- To update a single skill, specify its name, e.g., `npx skills@latest update expo-router`.

## Try It
After installation, ask your agent Expo‑specific questions such as:
- Build a native‑feeling Expo Router screen with tabs, modals, and animations.  
- Create an EAS workflow that builds previews on pull requests.  
- Help me upgrade this app to the latest Expo SDK.  
- Check whether this EAS Update rollout is healthy.

## Skills Included

### Start Here
- **expo-overview** – General entry point for vague or unspecified Expo requests.

### Framework (Open Source, Free)
- **expo-project-structure** – Recommended folder layout for new Expo apps.  
- **expo-router** – File‑based navigation, links, native stacks, modals, sheets, tabs, headers.  
- **expo-animation** – Animations and gestures using Reanimated, Gesture Handler, Expo Router, expo‑haptics.  
- **expo-native-ui** – Native‑looking screen styling, semantic colors, controls, icons, media, visual effects.  
- **expo-design-system** – Token‑based theme, reusable component conventions, drift audits.  
- **expo-ui** – `@expo/ui` components with cross‑platform and platform‑specific implementations.  
- **expo-data-fetching** – API calls, React Query, SWR, caching, offline support, data loaders.  
- **expo-dom** – Expo DOM components for gradual web code integration.  
- **expo-web-to-native** – Migrating web/React apps (Next.js, Vite, CRA) to native iOS/Android with Expo.  
- **expo-module** – Native modules and views using Swift, Kotlin, TypeScript, config plugins, autolinking.  
- **expo-brownfield** – Adding Expo or React Native to existing native iOS/Android projects.  
- **expo-dev-client** – Development clients (local builds free; EAS Build/TestFlight paid).  
- **expo-examples** – Reference implementations from the `expo/examples` repository.  
- **expo-app-clip** – iOS App Clip targets, AASA files, associated domains, Smart App Banners.  
- **expo-upgrade** – SDK upgrades, dependency conflict resolution, deprecated packages, cache cleanup.

### Services & Paid Distribution (Require EAS)
- **eas-app-stores** – Build and submit iOS/Android apps, manage TestFlight, profiles, versioning, metadata.  
- **eas-hosting** – Deploy Expo websites and Router API routes to EAS Hosting (secrets, custom domains, Cloudflare Workers).  
- **eas-workflows** – Author EAS Workflow YAML files and CI/CD automation.  
- **eas-observe** – Set up and launch EAS Observe for route, event, and version metrics.  
- **eas-update** – Configure OTA updates, runtime compatibility, testing, debugging.  
- **eas-update-insights** – Monitor update health, crash rates, launch counts, payload size, rollout gates.  
- **eas-simulator** – Run apps on remote iOS simulators or Android emulators in the EAS cloud with live browser preview (iOS only).

### Experimental (Subject to Change)
- **expo-migrate-module** – Migrate Swift Expo modules from Modules API 1.0 DSL to the 2.0 macro API.  
- These skills are packaged in a separate `expo-experiments` plugin or can be installed individually via the CLI.

## Expo MCP Server
- Provides agents with live access to perform real Expo work: fetch latest docs, install compatible dependencies (`npx expo install`), trigger and monitor EAS builds, pull TestFlight crash data, capture simulator screenshots.  
- Bundled with the Claude Code and Codex plugins; other agents can set it up following the Expo MCP setup guide.

## FAQ

### Which AI coding agents are supported?
- Cursor, OpenCode, GitHub Copilot, Windsurf, Gemini, Cline, AMP, Factory Droid, Antigravity, Kiro CLI, and similar tools. Use the CLI command to install for these agents.

### Should I install the skills or the plugin?
- Use the plugin for Claude Code or Codex (updates handled by their marketplaces).  
- Use the Skills CLI for Cursor, OpenCode, and other AI coding agents.

### What is the source of truth?
- The official Expo documentation, Expo CLI, and EAS CLI remain the authoritative references.
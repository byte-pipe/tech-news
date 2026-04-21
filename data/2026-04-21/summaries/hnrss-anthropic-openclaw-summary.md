---
title: Anthropic - OpenClaw
url: https://docs.openclaw.ai/providers/anthropic
date: 2026-04-21
site: hnrss
model: llama3.2:1b
summarized_at: 2026-04-21T12:01:03.588176
---

# Anthropic - OpenClaw

# OpenClaw - Overview and Configuration

**Overview**
 openclaw provides a seamless integration with the Anthropic API, enabling users to leverage its resources while maintaining control over their systems.

## Supported Options

* API Keys: Using an existing Auth0 license for standard API access and usage-based billing. Setup involves creating a new API key in the Anthropic Console.
* Claus CLI Onboarding
	+ `openclaw onboard` (Interactive) or (Non-interactive, with API Key)
	+ Choose: Anthropic API Key
* Customization Options:
	+ `--anthropic-api-key`: Specify an Anthropic API key for direct access.

## Thinking Levels and Adaptability

* Defaulting to Adaptive Thinking in OpenClaw models when no explicit thinking level is set.
* Overriding per-message or applying custom thinking levels through model parameters.
* Support for Extended Thinking for advanced cognitive tasks.

## Fast Mode and Proxy Considerations

* Enabling Fast Mode (Auto) on mapping services, requiring configuration as needed ("auto" is the default value).
* Limiting the injection of Anthropic service tiers for direct API requests outside a proxy or gateway.
* Configuring explicit service tier overrides when both `fastMode` and custom values are applied.

## Important Considerations

* OpenClaw does not inject service tiers directly through API requests unless an explicitly specified "standard_only" mapping configuration is used.
* Any override of the default Fast Mode or Prompt Caching behavior must be set as per system requirements.
* Usage reports the effective tier on responses with `usage.service_tier`, potentially displaying a "auto" value even without Priority Tier capacity.
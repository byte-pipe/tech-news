---
title: GitHub - FxEmbed/FxEmbed: Fix X/Twitter and Bluesky embeds! Use multiple images, videos, polls, translations and more on Discord, Telegram and others...
url: https://github.com/FxEmbed/FxEmbed
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-09-24T15:53:52.564381
---

# GitHub - FxEmbed/FxEmbed: Fix X/Twitter and Bluesky embeds! Use multiple images, videos, polls, translations and more on Discord, Telegram and others...

### FxEmbed Overview

* A Cloudflare Worker allowing the embedding of videos, polls, quotes, translations, and more on various platforms including Discord, Telegram, and others.
* Utilizes the local Workers runtime through Wrangler, leveraging the `node:24-bookworm-slim` image for reliability.
* Custom domains, branding, and credentials can be enabled via `.env` files.

### Method to Use FxEmbed

* Clone the repository: `git clone https://github.com/cloudflare/iframe-api`
* Visit the repository's root directory in your favorite IDE.
* Locate the `src` directory, marked as the `main` branch.
* Build the application using Docker Compose: `docker-compose up -d --build`

### Customization Options

* Host header support is enabled by editing the local `.env` file.
* Environment variables can be supplied through a `.env` file or shell.
* Runtime secrets, such as CREDENTIAL_KEY and EXCEPTION_DISCORD_WEBHOOK, can be configured via a Compose `.envfile`.

### Security Considerations

* Runtime secrets must be generated securely to prevent unauthorized access.
* Custom domains and branding options require permission from Cloudflare.
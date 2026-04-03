---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
date: 2025-12-11
site: devto
model: llama3.2:1b
summarized_at: 2025-12-16T11:14:14.230469
screenshot: devto-give-your-ai-studio-deployed-app-a-custom-url-dev.png
---

# Give your AI Studio deployed app a custom URL - DEV Community

# Customizing Your Google Cloud Run App's URL with a New Domain

**Summary**

This article provides step-by-step instructions on how to customize your Google Cloud Run app's URL if you've invested in a custom domain. By following the steps outlined below, including adding a mapping in Cloud Run and configuring a new website root using Namecheap DNS.

## Step 1: Map Your Google Cloud Run App

To begin, head over to your Google Cloud Console and navigate to **Cloud Run domains**. Find your project in the dropdown list, select it, and click on **Add Mapping in the Domain Mappings section**. Here's how to do that:

- **Service**: Select your app
- **Verified domain**: Choose "Verify a new domain"
- **Base domain**: Type your root domain (e.g., `vibe-compose.com`), omitting the `www`. You'll need to confirm ownership before routing traffic to it.

## Step 2: Verify Your Domain

After adding the mapping, you now move on to verifying your domain. Head back to Google Cloud Console and verify with a TXT record:

- Copy that long string of text provided by Google.
- Go to Namecheap.
- Manage → Advanced DNS.
- Click Add New Record.
- Select TXT Record.
- Host: @
- Value: Paste the confirmation text entered earlier.

## Step 3: Resolve the Naked Domain

Now you can configure your site to load at `vibe-compose.com` with the naked website domain not including www:

- Go back over to Cloud Run Mappings and click **Add Mapping again**.
- This time, map `www.vibe-com` to a CNAME:
  - Host: www
  - Value: ghs.googlehosted.com

## Step 4: Include Subdomains in Namecheap DNS

Don't forget about your subdomains! To include them in the new domain:

- **Add** one more record for `web.vibe-com` with a CNAME:
  - Host: web
  - Value: h1h9bph8c3lxc2r6f.0a1145e23e8ee6de4b.b07feba3c6ad7a29

**Summary**

Here's what you need to do:

* Verify your custom domain
* Create a mapping in Cloud Run for the root domain
* Resolve its subdomains through Namecheap DNS.
* Add further mappings and records as needed.

That's it! Your Google Cloud Run app now runs on a custom, naked website domain.

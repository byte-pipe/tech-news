---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
date: 2025-12-11
site: devto
model: llama3.2:1b
summarized_at: 2025-12-12T11:11:30.086566
screenshot: devto-give-your-ai-studio-deployed-app-a-custom-url-dev.png
---

# Give your AI Studio deployed app a custom URL - DEV Community

**Customizing Your Google Cloud Run App's Domain with Namecheap**

To link your cloud-run app's custom domain to its registrar (Namecheap), you must perform several steps to ensure proper DNS configurations and traffic routing. This guide will walk you through the "DNS Dance" used by Google CloudRun domains.

### Step 1: Add the Mapping for Your App

First, navigate to the [Google Cloud Console](https://console.cloud.google.com) and find your project in the dropdown list in the top left (e.g., Generative Language Client). You'll see a button labeled "Add Mapping" within the Domain Mappings section. Select your app as the service, pick "Verified domain", choose "Verify a new domain...", select your root domain (e.g., vibe-compose.com), and base domain as `vibe-compose.com`. Do not enter `www` yet.

### Step 2: Verify Your Domain

Google CloudRun requires verification before traffic can be routed to it. To do this, click verify in the modal that will open after entering your website name. This will generate a string of text in Gmail titled "Verified Domain". Copy and save this text since you'll need it later.

Next, log into [Namecheap](https://www.namecheap.com/) as administrator credentials. Go to your Domain List > Manage > Advanced DNS. Click Add New Record. Select TXT Record with the specified `@` host, value from the Google verification string found in Step 2 (e.g., '@vibe-compose.com'), TTL set to Automatic, and enter a short duration.

### Step 3: Configure Cloud Run Domains for Root vs Naked

Once verified, you need to prepare your server domain ("naked" or "root"). CloudRun uses A Records (IPv4) with these, and AAAA Records (IPv6). You'll need the IP addresses of all A records in your Domain Advanced DNS. Namecheap's list should have four `A` records (`host@`, ending `.32.21,.34.21,.36.21,`.38.21`), as well as each corresponding IPv6 (which you don't actually update). Add these records to ensure proper traffic routing.

### Step 4: Don't Forget the www

Make sure "www.vibe-compose.com" also points correctly by adding another CNAME record in Cloud Run's Domain Mappings section (e.g., `host`) with a value of `ghan.googlehosted.com`. Ensure you're not accidentally pasting `ghs.googlehosted.com` into the `Host` field.

### Step 5: Apply DNS Changes

After preparing all necessary records, go back to Cloud Run to verify your mappings. If everything has updated correctly, the DNS Dance can be put in its place without causing issues (like www.vibe-compose.com crashing). Then, don't hesitate to proceed with deploying and testing your app on your custom domain.

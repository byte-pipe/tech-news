---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
date: 2025-12-11
site: devto
model: llama3.2:1b
summarized_at: 2025-12-17T11:11:59.208181
screenshot: devto-give-your-ai-studio-deployed-app-a-custom-url-dev.png
---

# Give your AI Studio deployed app a custom URL - DEV Community

# Customizing Your Google Cloud Run App's Domain with a Personal Vibe

In this article, we'll walk through the process of customizing your Google Cloud Run app's domain to use a personal website like "Burning Man Animal Cuddle" (https://burning-man-animal-cuddle-614365371127.us-west1.run.app). The app is deployed with an initial domain: https://vibe-compose.com.

## Step 1: Map Your Root Domain to Cloud Run

First, navigate to your Google Cloud Console and select "Cloud Run domains." Find your project in the dropdown list, then click on "Add Mapping" in theDomain Mappingssection. Select your app from the service dropdown menu and choose a verified domain (e.g., vibe-compose.com). Add the base domain by selecting it in the dropdown.

## Step 2: Verify Your Domain with Namecheap

You also need to verify that you own the domain. Sign into Namecheap, go to "Domain List" > "Manage" > "Advanced DNS," and create a new TXT record for your site name (e.g., "vibe-compose.com"). Copy and paste the long verification string given by Google in this field.

## Step 3: Map Your Naked Domain to Cloud Run

To load your personal website at vibe-compose.com, you need to map it as the root domain. This means adding all IP addresses ending in .32.21, .34.21, .36.21, and .38.21 to "Domain Mappings" in Cloud Run.

## Step 4: Don't Forget the www Subdomain

To avoid issues with subdomains, you need to add a CNAME record for www.vibe-compose.com.

## Step 5: Finalize Your DNS Setup

Finally, verify that your app can load at vibe-compose.com by clicking on "VERIFY" after verifying your domain with Google. Then, ensure all necessary records are set up in Namecheap to enable your Cloud Run application.

By following these steps, you should be able to successfully customize your Google Cloud Run app's domain for a personal website like "Burning Man Animal Cuddle."

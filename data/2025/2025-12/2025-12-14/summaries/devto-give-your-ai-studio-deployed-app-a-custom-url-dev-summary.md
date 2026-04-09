---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
date: 2025-12-11
site: devto
model: llama3.2:1b
summarized_at: 2025-12-14T11:14:19.432688
screenshot: devto-give-your-ai-studio-deployed-app-a-custom-url-dev.png
---

# Give your AI Studio deployed app a custom URL - DEV Community

**Configuring Google Cloud Run Domain to Point to a Custom Domain**

The goal here is to configure Google Cloud Run to point to a custom domain hosted on Namecheap instead of the default verified domain provided by Google. This configuration ensures that users can access your app through the custom website.

### Adding a Mapping in Cloud Run

To start, navigate to the Cloud Run domains section and find the project associated with your app. From there, follow these steps:

* Add a mapping button
* Select the service: pick "Pick my app"
* Choose verified domain
* Base domain: select your root domain (vibe-compose.com)
* Without www:
+ Type Google verification string on Namecheap

This creates a TXT record for DNS verification.

### The Verification Dance (Google)

Once verified, the next step is to perform a DNS update. Here are the steps:

* Log into Namecheap
* Go to your Domain List -> Manage -> Advanced DNS
* Click Add New Record (on-namecheap)
+ Select TXT Record
+ Host: @
+ Value: Copy the Google verification string from the Cloud Run dashboard
+ TTL Auto
* Save changes

### Mapping the Naked Domain (Root Domain)

Now, you need to add all necessary records to Namecheap for a root domain:

* 4 A Records:
 + Values end in .32.21,.34.21,.36.21, and .38.21
* 4 AAAA Records:
 + Host is @
+ Values are the long IPv6 addresses

### Adding a CNAME (Subdomain)

To point subdomains to Cloud Run as well:

* Go back to Cloud Run Domain Mappings
* Click Add Mapping
+ Type www.vibe-compose.com
+ Google will tell you to add a CNAME
+ Back in Namecheap, add one final record:
 + Value: ghs.googlehosted.com

### Important Considerations and Mitigations

- Make sure not to accidentally input the same value for both Host (www) and Values.
* Since the verification process takes 2 minutes, wait after completing these steps before proceeding.

By following these steps, you can successfully configure a Google Cloud Run app to point to a custom domain hosted on Namecheap instead of the default verified domain.

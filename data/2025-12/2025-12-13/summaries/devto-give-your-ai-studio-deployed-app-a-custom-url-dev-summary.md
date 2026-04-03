---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
date: 2025-12-11
site: devto
model: llama3.2:1b
summarized_at: 2025-12-13T11:13:10.028507
screenshot: devto-give-your-ai-studio-deployed-app-a-custom-url-dev.png
---

# Give your AI Studio deployed app a custom URL - DEV Community

# Custom Domain Setup for Google Cloud Run App

**Step 1: Verify Original Domain**

Connect to your Google Cloud Console and navigate to [Cloud Run domains](https://console.cloud.google.com/apis/). Find your project in the dropdown list and select "Add a new mapping".

Choose "Verify a new domain..." as the service, enter your root domain (e.g., "vibe-compose.com"), and ensure it's not set with www.

# Step 2: Obtain Verification Text

After verifying the domain, copy the long text returned by Google to get the verification code. This is necessary for mapping to the newly verified domain.

**Step 3: Configure Root Domain**

In Namecheap:

1. Log in, go to your website's advanced DNS settings.
2. Click "Add New Record" and select "TXT Record".
3. Host: @, Value: Paste the Google verification text.
4. TTL (Time To Live): set to Automatic.

**Step 4: Map "Burning Man Animal Cuddle"-like Domain**

Now add all required A Records (IPv4) and AAAA Records (IPv6):
- Four A Records: Host is@ value end in .32.21,.34.21,.36.21, and .38.21.
- Four AAAA Records: same logic.

**Step 5: Map Subdomain to Root Domain**

Add a final CNAME record for the subdomain:
- Type: CNAME
- Host: www.vibe-compose.com (replace with Google's hosted value)
- Value: ghs.googlehostsed.com

Remember: The last step must have been "Don't Forget thewww", or your app may crash due to subdomain mapping errors.

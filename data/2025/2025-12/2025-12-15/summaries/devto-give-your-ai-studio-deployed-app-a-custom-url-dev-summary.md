---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
date: 2025-12-11
site: devto
model: llama3.2:1b
summarized_at: 2025-12-15T11:12:41.561400
screenshot: devto-give-your-ai-studio-deployed-app-a-custom-url-dev.png
---

# Give your AI Studio deployed app a custom URL - DEV Community

### Setting up a Custom URL for Your Google Cloud Run App in DEV Community

#### Identifying Key Points

* Use an official Google domain (e.g., `vibe-compose.com`) instead of a subdomain to maintain user trust.
* Verify ownership of the domain before routing traffic through DNS changes.

#### Detailed Summarization

**Step 1: Map Your Cloud Run Domain to a Verification Domain**

* Navigate to your Google Cloud Console and explore the **Cloud Run domains** section in **Project Viewers**.
* Locate your app's verification domain and click on it to open its details page.
* Select "Add Mapping" and choose your verified domain as the **Service**.
* Set up the verified domain mapping to include a base domain `*.domain-name.com` which you will use for your primary identity (e.g., `vibe-compose.com`.

#### Interacting with Google's Verification Method

Google needs to verify ownership before routing traffic through DNS changes, so proceed as follows:

1.  Sign-in to your Google account and select the project containing your app.
2.  Click on "Add Mapping" in **Cloud Run Domain Mappings** section of the verification process.
3.  Set up a mapping to `*._domain_name.com` (replace `domain-name.com` with your verified domain).
4.  Verify the domain by obtaining a TXT record associated with it.

#### Configuring Namecheap

Namecheap is required for DNS changes that require a custom Root domain (`vibe-compose.com`). Proceed as follows:

1.  Log in to your Namecheap account.
2.  Go to **Domain List** > **Manage** > **Advanced DNS**.
3.  Create a new Record Set (e.g., `*.domain-name.com` with text content)
4.  In the "Value" field, paste Google's verification string obtained from Step 4 in the `Verify a new domain...` step of Cloud Run Domain Mappings configuration.

#### Setting up CNAME Records

To ensure seamless operations for users accessing subdomains (`vibe-compose.com`), also set up CNAME records following these steps:

1.  Log into your Namecheap account.
2.  Go back to **Domain List** > **Manage** > **Advanced DNS** and find the same domain `vibe-compose.com`.
3.  Add a new record by clicking "Add New Record".
4.  Set up the CNAME record with Google's hostname (e.g., `@` which is used for subdomains) as the value.
5.  Set the ttl to automatic.

### Conclusion

By following these steps, you'll be able to successfully integrate a custom URL for your Google Cloud Run app while maintaining user trust and preventing issues during DNS transitions.

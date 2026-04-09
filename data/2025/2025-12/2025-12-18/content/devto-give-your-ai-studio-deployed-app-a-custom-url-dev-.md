---
title: Give your AI Studio deployed app a custom URL - DEV Community
url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
site_name: devto
fetched_at: '2025-12-18T11:07:27.700133'
original_url: https://dev.to/googleai/give-your-ai-studio-deployed-app-a-custom-url-30f
author: Paige Bailey
date: '2025-12-11'
description: So, you’ve just built an incredible AI application using Build in Google’s AI Studio. You hit Deploy,... Tagged with webdev, programming, javascript, beginners.
tags: '#webdev, #programming, #javascript, #beginners'
---

So, you’ve just built an incredible AI application using Build inGoogle’s AI Studio. You hitDeploy, the code flies through the ether, and your app is live! But then you look at the URL. It’s something like:https://burning-man-animal-cuddle-614365371127.us-west1.run.app/.

While I personally love the vibe of"Burning Man Animal Cuddle", your users might find it a bit... suspicious. You bought a cool domain onNamecheap(like vibe-compose.com), and you want to use that instead.

If you’ve never connected a Google Cloud Run service to a third-party registrar like Namecheap, the "DNS Dance" can be confusing. Here is exactly how to do it without pulling your hair out.

## Step 1: Add the Mapping in Cloud Run

First, head over to your Google Cloud Console and navigate toCloud Run domains. Find your project in the dropdown list in the top left (ex:Generative Language Client). You’ll see a button toAdd Mappingin theDomain Mappingssection.

In the dropdown:

* Select service:Pick your app.
* Select a verified domain:Choose "Verify a new domain..."
* Base domain:Type your root domain (e.g., vibe-compose.com). Do not type www yet. We start with the root.

## Step 2: The Verification Dance

Google needs to know you actually own the domain before they route traffic to it. When you click verify, a modal will pop up giving you a TXT record.

Once you've entered in your website name and hitContinue, copy that long string of text. It's time to leave Google for a moment and head to Namecheap.

* Log intoNamecheap.
* Go to yourDomain List->Manage->Advanced DNS.
* ClickAdd New Record.
* SelectTXT Record.
* Host: @
* Value: Paste that Google verification string here.
* TTL: Automatic.
* Save changes.

☕Coffee Break:DNS changes usually take a while. Wait 2 minutes, then go back to the Google Cloud tab and press VERIFY.

## Step 3: Mapping the "Naked" Domain

Once verified, the hard part begins. You want your site to load atvibe-compose.com(no www). This is called the "Naked" or "Root" domain.

Cloud Run does not use CNAMEs for root domains. It uses A Records (IPv4) and AAAA Records (IPv6). Cloud Run will display a list of IP addresses. You need to add all of them to Namecheap.

In Namecheap Advanced DNS, your list should look like the image above:

* 4 A Records: Host is@, Values are the IPs ending in.32.21,.34.21,.36.21, and.38.21.
* 4 AAAA Records: Host is@, Values are the long IPv6 addresses.

## Step 4: Don't Forget thewww

If you stop now, vibe-compose.com will work, butwww.vibe-compose.comwill crash. We need to map the subdomain too.

* Go back toCloud Run Domain Mappings.
* Click Add Mapping again.
* Typewww.vibe-compose.com.
* Google will tell you to add a CNAME.
* Back in Namecheap, add one final record:
* Type:CNAMERecord
* Host:www
* Value:ghs.googlehosted.com.

⚠️ The "Gotcha": Many devs accidentally pasteghs.googlehosted.cominto the "Host" field. Don't do that! The Host iswww. If Namecheap adds a period at the end, that should be okay.

## Step 5: The spinning wheel of patience

Once your DNS records are in, head back to the Cloud Run dashboard. You will see your domains listed with a yellow spinner or a green checkmark.

## What is happening now?

DNS Propagation:Google is checking to see if Namecheap updated (can take 10 mins to 24 hours).

Certificate Provisioning:Once DNS is found, Google automatically creates a managed SSL certificate for you.

## Conclusion

Taking the extra 5 minutes to map a custom domain adds a massive layer of polish to your projects. Now, instead of sending people toburning-man-animal-cuddle, you can send them tovibe-compose.com.

(Though, honestly, I'm going to miss the animal cuddles).

Happy Coding! 🚀

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

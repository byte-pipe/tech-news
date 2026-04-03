---
title: How I Reverse Engineered a Billion-Dollar Legal AI Tool and Found 100k+ Confidential Files | Alex Schapiro
url: https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k
site_name: hackernews
fetched_at: '2025-12-04T11:08:11.079360'
original_url: https://alexschapiro.com/security/vulnerability/2025/12/02/filevine-api-100k
author: bearsyankees
date: '2025-12-04'
published_date: '2025-12-02T04:00:00-05:00'
description: 'Update: This post received a large amount of attention on Hacker News — see the discussion thread.'
---

Update: This post received a large amount of attention on Hacker News— see the discussion thread.

Timeline & Responsible Disclosure

Initial Contact:Upon discovering this vulnerability onOctober 27, 2025, I immediately reached out to Filevine’s security team via email.

November 4, 2025:Filevine’s security team thanked me for the writeup and confirmed they would review the vulnerability and fix it quickly.

November 20, 2025:I followed up to confirm the patch was in place from my end, and informed them of my intention to write a technical blog post.

November 21, 2025:Filevine confirmed the issue was resolved and thanked me for responsibly reporting it.

Publication:December 3, 2025.

The Filevine team was responsive, professional, and took the findings seriously throughout the disclosure process. They acknowledged the severity, worked to remediate the issues, allowed responsible disclosure, and maintained clear communication. This is another great example of how organizations should handle security disclosures.

AI legal-tech companies are exploding in value, and Filevine, now valued atover a billion dollars, is one of the fastest-growing platforms in the space. Law firms feed tools like this enormous amounts ofhighly confidential information.

Because I’d recently been working withYale Law School on a related project, I decided to take a closer look at how Filevine handles data security. What I discovered should concern every legal professional using AI systems today.

When I first navigated to the site to see how it worked, it seemed that I needed to be part of a law firm to actually play around with the tooling, or request an official demo. However, I know that companies often have a demo environment that is open, so I used a technique called subdomain enumeration (which I had first heard about inGal Nagli’s articlelast year) to see if there was a demo environment. I found something much more interesting instead.

I saw a subdomain calledmargolis.filevine.com. When I navigated to that site, I was greeted with a loading page that never resolved:

I wanted to see what was actually loading, so I opened Chrome’s developer tools, but sawno Fetch/XHR requests(the request you often expect to see if a page is loading data). Then, I decided to dig through some of the Javascript files to see if I could figure out what wassupposedto be happening. I saw a snippet in a JS file likePOST await fetch(${BOX_SERVICE}/recommend). This piqued my interest – recommend what? And what is the BOX_SERVICE? That variable was not defined in the JS file the fetch would be called from, but (after looking through minified code, which SUCKS to do) I found it in another one: “dxxxxxx9.execute-api.us-west-2.amazonaws.com/prod”. Now I had anew endpoint to test, I just had to figure out the correct payload structure to it. After looking at more minified js to determine the correct structure for this endpoint, I was able to construct a working payload to /prod/recommend:

{"projectName":"Very sensitive Project"}

(the name could be anything of course).No authorization tokens needed, and I was greeted with the response:

At first I didn’t entirely understand the impact of what I saw. No matter the name of the project I passed in, I was recommended the same boxFolders and couldn’t seem to access any files. Then, not realizing I stumbled upon somethingmassive, I turned my attention to theboxTokenin the response.

After reading some documentation on the Box Api, I realized this was amaximum access fully scoped admin tokento theentire Box filesystem(like an internal shared Google Drive) of this law firm. This includesall confidential files, logs, user information, etc.Once I was able to prove this had an impact (by searching for “confidential” and gettingnearly 100k resultsback)

Iimmediately stopped testingand responsibly disclosed this to Filevine. They responded quickly and professionally and remediated this issue.

If someone had malicious intent, they would have been able to extractevery single fileused by Margolis lawyers – countless data protected byHIPAAand other legal standards, internal memos/payrolls, literallymillions of the most sensitive documentsthis law firm has in their possession.Documents protected by court orders!This could have been a real nightmare for both the law firm and the clients whose data would have been exposed.

To companies who feel pressure to rush into the AI craze in their industry –be careful!Always ensure the companies you are giving your most sensitive information tosecure that data.

---
title: How we pwned X (Twitter), Vercel, Cursor, Discord, and hundreds of companies through a supply-chain attack · GitHub
url: https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28
site_name: hackernews_api
fetched_at: '2025-12-20T11:06:42.406605'
original_url: https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28
author: hackermondev
date: '2025-12-18'
description: How we pwned X (Twitter), Vercel, Cursor, Discord, and hundreds of companies through a supply-chain attack - writeup.md
tags:
- hackernews
- trending
---

Instantly share code, notes, and snippets.

# hackermondev/writeup.md

 Last active

December 20, 2025 09:15



Show Gist options



* Download ZIP





* Star104(104)You must be signed in to star a gist
* Fork9(9)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save hackermondev/5e2cdc32849405fff6b46957747a2d28 to your computer and use it in GitHub Desktop.



Embed

# Select an option



* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found





Learn more about clone URLs





 Clone this repository at &lt;script src=&quot;https://gist.github.com/hackermondev/5e2cdc32849405fff6b46957747a2d28.js&quot;&gt;&lt;/script&gt;





Save hackermondev/5e2cdc32849405fff6b46957747a2d28 to your computer and use it in GitHub Desktop.

Download ZIP

 How we pwned X (Twitter), Vercel, Cursor, Discord, and hundreds of companies through a supply-chain attack




Raw

 writeup.md


hi, i'm daniel. i'm a 16-year-old high school senior. in my free time, ihack billion dollar companiesand build cool stuff.

about a month ago, a couple of friends and I found serious critical vulnerabilities on Mintlify, an AI documentation platform used by some of the top companies in the world.

i found a critical cross-site scripting vulnerability that, if abused, would let an attacker to inject malicious scripts into the documentation of numerous companies and steal credentials from users with a single link open.

(go read my friends' writeups (after this one))how to hack discord, vercel, and more with one easy trick (eva)Redacted by Counsel: A supply chain postmortem (MDL)

here's my story...

# Discord

My story begins on Friday, November 7, 2025, when Discord announced a brand new update to their developer documentation platform. They were previously using a custom built documentation platform, but were switching to an AI-powered documentation platform.

Discord is one of my favorite places to hunt for vulnerabilities since I'm very familiar with their API and platform. I'm at the top of their bug bounty leaderboard having reported nearly 100 vulnerabilities over the last few years. After you've gone through every feature at least 10 times, it gets boring.

I found this new update exciting, and as soon as I saw the announcement, I started looking through how they implemented this new documentation platform.

# Mintlify

Mintlify is an AI-powered documentation platform. You write your documentation as markdown and Mintlify turns it into a beautiful documentation platform with all the modern features a documentation platform needs. (Despite the vulnerabilities we found, I would highly recommend them. They make it really easy to create beautiful docs that work.)

Mintlify-hosted documentation sites are on the *.mintlify.app domains, with support for custom domains. In Discord's case, they were just proxying certain routes to their Mintlify documentation atdiscord.mintlify.app.

Every Mintlify subdomain has a/_mintlify/*path that is used internally on the platform to power certain features. Regardless of whether it's hosted through themintlify.appdomain or a custom domain, the/_mintlifypath must be accessible to power the documentation.

(For example, the/api/userpath for authentication:https://docs.x.com/_mintlify/api/user,https://discord.com/_mintlify/api/user, etc)

# /_mintlify/markdown/

After Discord switched to Mintlify and when I started looking for bugs on the platform, from the get-go, my plan was to find a way to render another Mintlify documentation through Discord's domain.

At first, I tried path traversal attacks, but they didn't work. Then, I started looking through the/_mintlifyAPI endpoints.

Using Chrome DevTools to search the assets, I found the endpoint/_mintlify/_markdown/_sites/[subdomain]/[...route]. It accepted any Mintlify documentation ([subdomain]) and it returned a file from that specific documentation ([...route]). The endpoint didn't check to make sure the[subdomain]matched with the current host, which means you could fetch files from any Mintlify documentation on an host with the/_mintlify/route.

Unfortunately, this endpoint only returned raw markdown text. The markdown wasn't rendered as HTML, meaning it was impossible to run code. I spent the rest of the time trying different ways to bypass this, but nothing worked.

# /_mintlify/static/

Fast forward 2 days to Sunday, November 9, 2025, I went back to hunting.

I was confident there was another endpoint, like the markdown one, which could fetch and return cross-site data, but I couldn't find one. I tried searching web assets and some other techniques, but I couldn't find the endpoint I was looking for.

Finally, I decided to look through the Mintlify CLI. Mintlify lets you run your documentation site locally via their npm package (@mintlify/cli). I realized that this probably meant the code powering the documentation platform was somewhat public.

After digging through the package and downloading tarballs linked in the code, I found myself at exactly what I was looking for.

Jackpot!

This was a list of application endpoints (compiled by Nextjs), and in the middle, there's the endpoint/_mintlify/static/[subdomain]/[...route].

Like the markdown endpoint, this endpoint accepted any Mintlify documentation ([subdomain]). The only difference was this endpoint returned static files from the documentation repo.

First, I tried accessing HTML and JavaScript files but it didn't work; I realized there was some sort of whitelist of file extensions. Then, I tried an SVG file, and it worked.

If you didn't know, you can embed JavaScript into an SVG file. The script doesn't run unless the file is directly opened (you can't run scripts from (<img src="/image.svg">). This is very common knowledge for security researchers.

I created an SVG file with an embedded script, uploaded it to my Mintlify documentation, and opened the endpoint through Discord (https://discord.com/_mintlify/_static/hackerone-a00f3c6c/lmao.svg). It worked!

# Collaboration

XSS attacks are incredibly rare on Discord, so I shared it with a couple friends.

I sent a screenshot to xyzeva, only to find out she had also been looking into Mintlify after the Discord switch. She had previously discovered other vulnerabilities on the Mintlify platform, and had found more that she was preparing to disclose (go read her writeup!). I find it funny we had both separately been looking into Mintlify and found very different, but very critical bugs.

Another friend joined, and we created a group chat.

# Reporting

We reported the vulnerability to Discord and attempted to contact Mintlify through an employee.

Discord took this very seriously, and closed off its entire developer documentation for 2 hours while investigating the impact of this vulnerability. Then, they reverted to their old documentation platform and removed all the Mintlify routes.https://discordstatus.com/incidents/by04x5gnnng3

Mintlify contacted us directly very shortly after hearing about the vulnerability through Discord. We set up a Slack channel with Mintlify's engineering team and got to work. Personally, this cross-site scripting attack was the only thing I had the time to find; eva and MDL worked with Mintlify's engineering team to quickly remediate this and other vulnerabilities they found on the platform.

# Impact

In total, the cross-site scripting attack affected almost every Mintlify customer. To name a few: X (Twitter), Vercel, Cursor, Discord,and more.

These customers host their documentation on their primary domains and were vulnerable to account takeovers with a single malicious link.

# Conclusion

Fortunately, we responsibly found and disclosed this vulnerability but this is an example of how compromising a single supply chain can lead to a multitude of problems.

In total, we collectively recieved ~$11,000 in bounties. Discord paid $4,000 and Mintlify individually gave us bounties for the impact of the bugs we individually found.

Load earlier comments...



### NeilHanloncommentedDec 18, 2025

Discord owes you 10x what they paid. Goodness.

Great work dude.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ijsbolcommentedDec 18, 2025

i have been waiting for this writeup for like 2 weeks finally

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### IkariuPrimecommentedDec 18, 2025

$11K for bugs that could have cost billions is crazy

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### Aeyth8commentedDec 19, 2025

Billion dollar zero day turned into a measly eleven thousand dollars 🥰

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### opticaldrivecommentedDec 19, 2025

congratulations, nice to see more work from you :3

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### jschmidtnjcommentedDec 19, 2025

this is awesome, good write-up! agree that 11k seems too low...

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### yousafkcommentedDec 19, 2025•edited

somehow npm is involved :P great job on the find and write up!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ogpouryacommentedDec 19, 2025

You killed it 🔥

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### estcommentedDec 19, 2025•edited

if server only serves image if there's aSec-Fetch-Dest: imageheader, could tis prevent the .svg attack ?@hackermondev

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### idkhowisyourdaycommentedDec 19, 2025

very cool

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### azurenekowocommentedDec 19, 2025

mad cool, props off to yall for finding out this

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ArmyaAlicommentedDec 19, 2025

good stuff

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### vs4vijaycommentedDec 19, 2025

great work!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### Nebyat19commentedDec 19, 2025

wow this is great

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### bvsvntvcommentedDec 19, 2025

what a read. Great!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### trupuscommentedDec 19, 2025

damn, amazing!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### yan-alexcommentedDec 19, 2025•edited

Discord paid 4k? That's not the greatest "thank you" to someone that saved your business from a scandal.I guess they rather get ransomwared and have to pay millions instead huh...

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### marciobbjcommentedDec 19, 2025

That's a great discovery! You definitely deserve a higher income, by the way.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### bettinasosacommentedDec 19, 2025

Awesome work! You definitely deserve more from discord and mintlify, that's a critical bug.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### codeharmancommentedDec 19, 2025

Awesome work!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### albertocavalcantecommentedDec 19, 2025

Thanks for sharing. Well done!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ismai1337commentedDec 19, 2025

hell yeah

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### usercommentedDec 19, 2025

cool story bruh

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### GustavoStingelincommentedDec 19, 2025

congrats!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### tcelestinocommentedDec 19, 2025

🚀🚀

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### midazcommentedDec 19, 2025

You are doing god's work. You should have been paid way more than $5k. Thanks for your contributions to the ecosystem.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### TuanmcommentedDec 19, 2025

Good!!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### dirsiglercommentedDec 19, 2025

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### jaccquescommentedDec 19, 2025

interesting read!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ActiveTKcommentedDec 20, 2025

well done

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.





Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment

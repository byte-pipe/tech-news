---
title: The how and why of GitHub to Codeberg
url: https://www.arscyni.cc/file/codeberg.html
site_name: lobsters
fetched_at: '2025-08-06T23:07:26.197503'
original_url: https://www.arscyni.cc/file/codeberg.html
author: Angelino Desmet
date: '2025-08-06'
description: How to migrate (multiple) static websites from GitHub to Codeberg.
tags: privacy, web
---

# The how and why ofGitHubtoCodeberg

How to migrate (multiple) static websites fromGitHub PagestoCodeberg.

## GitHub pages toCodeberg+statichost.eu

The steps below will migrate a manually written static website fromGitHub PagestoCodeberg+statichost.eu, notCodeberg Pages. Any change to one's newCodebergrepository will be automatically pushed tostatichost.eu. The latter is used becauseCodeberg Pages is advised against by themselves if uptime is crucial. If reliable uptime isn't necessary one can follow thelegacy tutorial.

1. Create an account onCodeberg:https://codeberg.org. Then click the top right "+" menu → "+ New Repository". Choose whatever repository name and leave the rest as is. Click "Create Repository".
2. On one's PC, navigate to the website'sgitdirectory that's still linked toGitHuband make sure it is up-to-date:git pullshould output "Already up to date."
3. Deprecate theGitHubrepository and push/upload all content to theCodebergrepository made in step 1.git remote rename origin origin-old-githubgit remote add origin https://codeberg.org/USERNAME/REPOSITORY_NAME.gitgit branch -M maingit push --set-upstream origin --allgit push --set-upstream origin --tags“Credentials are incorrect or have expired”?If it throws “Password for 'https://username@codeberg.org':remote: Credentials are incorrect or have expired.”, it might be because 2FA is enabled and one still has to create an access token athttps://codeberg.org/user/settings/applications.Choose (1) whatever token name, (2) "☑ Public only" for "Repository and Organization Access", and (3)Read and writepermission for "repository" under "🢒 repository permissions". Save the code/token/password it gives in a password manager such asKeePassXCand use this code to authenticate instead of one'sCodebergaccount password.
4. Create an account onstatichost.euand click "Add site".
5. Addhttps://codeberg.org/USERNAME/REPOSITORY_NAME.gitas "Repository".
6. For manually written static HTML/CSS websites—notstatic site generators—leave the build settings as is and click "Continue"."Build settings"? 🤨Since GitHub does everything automatically, then one probably has no idea what these build settings mean if not having used a static site generator before.I reached out tostatichost.euand the founder was kind enough to respond:“For a simple HTML and CSS website built from scratch, you don't need to
	worry about complex build configurations. The settings as they are now
	are exactly correct.”
7. As "Managed domain" it will now suggest "username-repository_name.statichost.eu", this can again be named whatever as long as it's available. Add your custom domain name if you have one, e.g.,www.arscyni.ccand click "Publish".

✔ ⅓: The website will now be live atusername-repository_name.statichost.eu.

Whatoptionallyremains to be done is auto updates, and DNS settings so both "yourwebsite.org" and "www.yourwebsite.org" work.

### Automatically update thestatichostsite onCodebergrepository changes

Thestatichost.eufounder Eric Selin was kind enough to answer my question:

“Yes, statichost.eu can automatically detect changes and update your
 website when you push to your Codeberg repository. You don't need to
 manually press "Build now" each time. To set this up:

* Go to your repository on Codeberg
* Navigate to Settings -> Webhooks
* Add a new webhook with the URL: https://builder.statichost.eu/YOUR_SITE_NAME

Replace YOUR_SITE_NAME with the actual name of your site on statichost.eu. Seehttps://www.statichost.eu/docs/git-providers/#forgejo-eg-codebergfor more information.

This webhook will trigger a new build automatically whenever you push
	 changes to your repository.”

✔ ⅔.

### Custom domain DNS settings

Below, my adjusted settings without explanation because I still have no idea howDNSconfiguration works after all these years due to inconsistent behaviour between services, e.g., thecustom domains settings in the statichost.eu documentationdidn't resolve my root domainarscyni.ccwhile it did resolvewww.arscyni.cc:

The domain settings for arscyni.cc onhttps://builder.statichost.eu:

* Primary domain:www.arscyni.cc
* Redirect domains:arscyni.cc

The registrar DNS settings for arscyni.cc:

* TypeA Record, Hostarscyni.cc, Value95.217.26.94, TTLAutomatic
* TypeAAAA Record, Hostarscyni.cc, Value2a01:4f9:c01f:8002::, TTLAutomatic
* TypeALIAS Record, Host@, Valuears-cynic.statichost.eu., TTL5 min
* TypeCNAME Record, Hostwww, Valuears-cynic.statichost.eu., TTLAutomatic

✔ ³⁄₃: Great success. Enjoy the minimalist satisfaction. To hell with Microsoft.

## Wait, what, why to hell with Microsoft?

Microsoft ownsGitHub.Microsoft's ethically degenerate business practices such as lobbyingand preinstallations are the only reasons why their products aren't superseded yet by the absurdly superior Linux alternatives; Windoze is a horribleOS, nay, malware, now also spyware byWindows RecallandAIFoie Gras'ing everything, evenNotepad. Also,Microsoft's tax evasion. Microsoft is by no means alone in this. Nearly all big corporations such as Meta [Facebook,Instagram,WhatsApp], Alphabet [Google], Apple, have succumbed to the most insidious disease being cancerous greed, and y'all know how we treat cancer: nuke it with chemotherapy. I could keep going, but that would make for an inappropriate tutorial no different from a tasteless joke as the one depicted below which is not funny at all.

—Image:
IKEA's Oligarkchöp
.

Stocks must go up because we live on a planet with infinite resources. Eventually the wealth of the ultrarich will trickle down to end poverty thanks to the goodness of the hearts of these corporate heroes. Greed is leftist propaganda and history never happened.

—Angelino Desmet; 15 April 2023.

Latest edit: 2025, August 6.

* 2023-07-28: adds git commands that save git history.
* 2024-10-20: adds https redirect instructions.
* 2024-10-29: adds warning.
* 2025-08-06: rewrite to use statichost.eu

Ψ

## Legacy: How to migratemultiplestatic websites from GitHubpagesto Codeberg pages

Show legacy tutorial.

The official documentation to setup—not migrate to—Codeberg Pagescan be found onhttps://codeberg.page, but it is confusing and incomplete if one wantsmultiplepages with custom domain names.

Edit #1: for now I cannot recommend using Codeberg'spagesif one requires reliable uptimes.Codeberg Pages might even become deprecated soondue to unresolved server problems regarding the pages.

Edit #2: Codeberg agrees, as now shown on their pages documentation above:

 “Codeberg Pages is currently provided with a best effort approach. To be exact, the software behind this feature is currently in maintenance mode.
 Please do not rely on it for critical websites, as we can't guarantee high availability like some other providers do.”

### Getting the repository on Codeberg

The official documentation instructs to create a repository named "pages" for the static website, but what if one has multiple websites? It's also plain annoying to have such a name for a repository. Anyway, the following steps allows one to have multiple static pages on Codeberg without having to name them "pages", ugh.

1. Create an account on Codeberg:https://codeberg.org. Then via the top right button click "+ New Repository". Choose whatever repository name, and as "Default Branch" replace main withpages. Click "Create Repository".
2. Navigate one's computer to the directory of which the content needs to end up in the newly created Codeberg repository. For me that was "/home/…/quitfacebook.org/public/"

#### Option 1: keep git history

This will preserve the nice graph that shows all the contributions made, and all the file versioning history of course.


git remote rename origin old-origin-github


git remote add origin https://codeberg.org/CynicusRex/quitfacebook.git


git branch -M pages


git push --set-upstream origin --all


git push --set-upstream origin --tags



#### Option 2: remove git history

1. Assuming one still has the hidden .git folder, rename it to .git_BAK or whatever, or delete it.
2. Open the terminal in that directory and run:git initIt will probably show the following message: “hint: Using 'master' as the name for the initial branch. This default branch name […] The just-created branch can be renamed via this command: git branch -m <name>”
3. Run:git branch -m pagesYou see, the repository needn't be named pages, but the branch does. That's great because now one can have multiple pages with distinct names. The official documentation makes it seem as if one is limited to one page.
4. Run:git add .git commit -m "first commit"git remote add origin https://codeberg.org/CynicusRex/quitfacebook.gitgit push -u origin pages

### Domain configurations*

Assuming one has a custom domain name, do the following. If one doesn't, then the official documentation probably suffices.

1. Add the file ".domains" with the following content to one's local repository and push it to Codeberg, obviously adjusted with one's own domain name:quitfacebook.orgwww.quitfacebook.orgpages.quitfacebook.cynicusrex.codeberg.page
2. Open one's registrar website, and configure the "Advanced DNS" "host records" as follows:Type: A Record, Host: @, Value: 217.197.91.145, TTL: AutomaticType: AAAA Record, Host: @, Value: 2001:67c:1401:20f0::1, TTL: AutomaticType: CNAME Record, Host: www, Value: quitfacebook.cynicusrex.codeberg.page., TTL: AutomaticType: TXT Record, Host: @, Value: quitfacebook.cynicusrex.codeberg.page., TTL: Automatic

All is done. It might take a couple of hours until the domain configurations get updated. Also, don't forget to unpublish your page on GitHubunlessyou've changed your domain name as well—read on in the latter case.

– – – – –

* Credits toJan Wildeboer.

## Redirecting a GitHub https URL

Show redirection tutorial.

When changing domain names of a website formerly hosted on GitHub, then merely redirecting on one's registrar website willnotredirect httpsURLs becauseGitHub pages does not support a .htaccess file nor the SSL plugin. Instead leave unchanged the settings on one's registrar and GitHub, and add ameta refresh tagon every page one wants redirected*.

* To redirecthttps://www.cynicusrex.comtohttps://www.arscyni.cc, then add to a page:<meta http-equiv="refresh" content="0;URL=https://www.arscyni.cc">
* To redirect a specific page such ashttps://www.cynicusrex.com/file/takemymoney.htmltohttps://www.arscyni.cc/file/take_my_money.html, then add:<meta http-equiv="refresh" content="0;URL=https://www.arscyni.cc/file/take_my_money.html">

– – – – –

* Credits todiv72.

## Comments

Search forhttps://fosstodon.org/@stardust/110202336827539450(fosstodon invite) on one's preferredMastodonserver while logged in, comments appear below.

> load comments

Enable JavaScript to view the comments.

Additional comments:Lobsters.

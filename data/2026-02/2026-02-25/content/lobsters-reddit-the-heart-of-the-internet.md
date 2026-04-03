---
title: Reddit - The heart of the internet
url: https://reddit.com/r/selfhosted/comments/1rckopd/huntarr_your_passwords_and_your_entire_arr_stacks/
site_name: lobsters
content_file: lobsters-reddit-the-heart-of-the-internet
fetched_at: '2026-02-25T06:00:30.685951'
original_url: https://reddit.com/r/selfhosted/comments/1rckopd/huntarr_your_passwords_and_your_entire_arr_stacks/
date: '2026-02-25'
tags: security
---

Go to selfhosted


r/selfhosted

•

exe_CUTOR



# Huntarr - Your passwords and your entire arr stack's API keys are exposed to anyone on your network, or worse, the internet.

Today, after raising security concerns in a post onr/huntarrregarding the lack of development standards in what looks like a 100% vibe-coded project, I was banned. This made my spidey senses tingle, so I decided to do a security review of the codebase. What I found was... not good. TLDR: If you have Huntarr exposed on your stack, anyone can pull your API keys for Sonarr, Radarr, Prowlarr, and every other connected app without logging in, gaining full control over your media stack.

# The process

I did a security review of Huntarr.io (v9.4.2) and found critical auth bypass vulnerabilities. I'm posting this here because Huntarr sits on top of (and is now trying to replace them as well!) Sonarr, Radarr, Prowlarr, and other *arr apps that have years of security hardening behind them. If you install Huntarr, you're adding an app with zero authentication on its most sensitive endpoints, and that punches a hole through whatever network security you've set up for the rest of your stack.

The worst one:POST /api/settings/generalrequires no login, no session, no API key. Nothing. Anyone who can reach your Huntarr instance can rewrite your entire configuration and the response comes back withevery setting for every integrated applicationin cleartext. Not just Huntarr's own proxy credentials - the response includes API keys and instance URLs for Sonarr, Radarr, Prowlarr, Lidarr, Readarr, Whisparr, and every other connected app. One curl command and an attacker has direct API access to your entire media stack:

curl -X POST http://your-huntarr:9705/api/settings/general \
 -H "Content-Type: application/json" \
 -d '{"proxy_enabled": true}'

Full config dump with passwords and API keys for every connected application. If your instance is internet-facing - and it often is, Huntarr incorporates features like Requestarr designed for external access - anyone on the internet can pull your credentials without logging in.

Other findings (21 total across critical/high/medium):

* Unauthenticated 2FA enrollment on the owner account(Critical,proven in CI):POST /api/user/2fa/setupwith no session returned the actual TOTP secret and QR code for the owner account. An attacker generates a code, calls/api/user/2fa/verify, enrolls their own authenticator. Full account takeover, no password needed.
* Unauthenticated setup clear enables full account takeover(Critical,proven in CI):POST /api/setup/clearrequires no auth. Returns 200 "Setup progress cleared." An attacker re-arms the setup flow, creates a new owner account, replaces the legitimate owner entirely.
* Unauthenticated recovery key generation(Critical,proven in CI):POST /auth/recovery-key/generatewith{"setup_mode": true}reaches business logic with no auth check (returns 400, not 401/403). The endpoint is unauthenticated.
* Full cross-app credential exposure(Critical,proven in CI): Writing a single setting returns configuration for 10+ integrated apps. One call, your entire stack's API keys.
* Unauthenticated Plex account unlink- anyone can disconnect your Plex from Huntarr
* Auth bypass on Plex account linkingvia client-controlledsetup_modeflag - the server skips session checks if you send{"setup_mode": true}
* Zip Slip arbitrary file write(High):zipfile.extractall()on user-uploaded ZIPs without filename sanitization. The container runs as root.
* Path traversal in backup restore/delete(High):backup_idfrom user input goes straight into filesystem paths.shutil.rmtree()makes it a directory deletion primitive.
* local_access_bypasstrustsX-Forwarded-Forheaders, which are trivially spoofable - combine with the unauth settings write and you get full access to protected endpoints

How I found this:Basic code review and standard automated tools (bandit, pip-audit). The kind of stuff any maintainer should be running. The auth bypass isn't a subtle bug -auth.pyhas an explicit whitelist that skips auth for/api/settings/general. It's just not there.

About the maintainer and the codebase:

The maintainersaysthey have "a series of steering documents I generated that does cybersecurity checks and provides additional hardening" and"Note I also work in cybersecurity."Theysaythey've put in "120+ hours in the last 4 weeks" using "steering documents to advise along the way from cybersecurity, to hardening, and standards". If that's true, it's not showing in the code.

If you work in cybersecurity, you should know not to whitelist your most sensitive endpoint as unauthenticated. You should know that returning TOTP secrets to unauthenticated callers is account takeover. You should knowzipfile.extractall()on untrusted input is textbook Zip Slip. This is introductory stuff. The "cybersecurity steering documents" aren't catching what a basic security scan flags in seconds.

Look at thecommit history: dozens of commits with messages like "Update", "update", "Patch", "change", "Bug Patch" - hundreds of changed files in commits separated by a few minutes. No PR process, no code review, no second pair of eyes - just raw trunk-based development where 50 features get pushed in a day with zero review. Normal OSS projects are slower for a reason: multiple people look at changes before they go in. Huntarr has none of that.

Whencalled out on this, the maintainer said budget constraints: "With a limited budget, you can only go so far unless you want to spend $1000+. I allot $40 a month in the heaviest of tasks." That's just not true - you can use AI-assisted development 8 hours a day for $20/month. The real problem isn't the budget. It's that the maintainer doesn't understand the security architecture they're building and doesn't understand the tools they're using to build it. You can't guide an AI to implement auth if you don't recognize what's wrong when it doesn't.

They also censor security reports and ban people who raise concerns.A user posted security concerns onr/huntarrand it wasremoved by the moderator- the maintainer controls the subreddit. I was banned fromr/huntarrafter pointing out these issues inthis threadwhere the maintainer was claiming to work in cybersecurity (which they now deleted).

One more thing - the project's README has a "Support - Building My Daughter's Future" section soliciting donations. That's a red flag for me. You're asking people to fund your development while shipping code with 21 unpatched security vulnerabilities, no code review process, and banning people who point out the problems, while doing an appeal to emotion about your daughter. If you need money, that's fine - but you should be transparent about what you're spending it on and you should be shipping code that doesn't put your users at risk.

Proof repo with automated CI:https://github.com/rfsbraz/huntarr-security-review

Docker Compose setup that pulls the published Huntarr image and runs a Python script proving each vulnerability. GitHub Actions runs it on every push - check the workflow results yourself or run it locally withdocker compose up -d && python3 scripts/prove_vulns.py.

For what it's worth, and to prove I'm not an AI hater, theprove_vulnsscript itself was vibe coded - I identified the vulnerabilities through code review, wrote up the repro steps, and had AI generate the proof script.

Full security review (21 findings):https://github.com/rfsbraz/huntarr-security-review/blob/main/Huntarr.io_SECURITY_REVIEW.md

What happens next:The maintainer will most likely prompt these problems away - feed the findings to an AI and ship a patch. But fixing 21 specific findings doesn't fix the process that created them. No code review, no PR process, no automated testing, no one who understands security reviewing what ships. The next batch of features will have the next batch of vulnerabilities. This is only the start. If the community doesn't push for better coding standards, controlled development, and a sensible roadmap, people will keep running code that nobody has reviewed.

If you're running Huntarr, keep it off any network you don't fully trust until this is sorted. The *arr apps it wraps have their own API key auth - Huntarr bypasses that entirely.

Please let others know about this. If you have a Huntarr instance, share this with your community. If you know someone who runs one, share it with them. The more people know about the risks, the more pressure there will be on the maintainer to fix them and improve their development process.

Edit: Looks liker/huntarrwent private and the repo got deleted or privatedhttps://github.com/plexguide/Huntarr.io. I'm sorry for everyone that donated to this guy's "Daughter College Fund".

Edit 2: Thanks for all the love on the comments, I'll do my best to reach out to everyone I can. People asking me for help on security reviews, believe me when I say I did little more than the basics - the project wasterrible.

 Read more

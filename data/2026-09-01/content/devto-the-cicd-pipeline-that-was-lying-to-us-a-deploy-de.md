---
title: '# The CI/CD Pipeline That Was Lying to Us: A Deploy Debugging Story - DEV Community'
url: https://dev.to/highcenburg/-the-cicd-pipeline-that-was-lying-to-us-a-deploy-debugging-story-9fi
site_name: devto
content_file: devto-the-cicd-pipeline-that-was-lying-to-us-a-deploy-de
fetched_at: '2026-09-01T21:37:45.746232'
original_url: https://dev.to/highcenburg/-the-cicd-pipeline-that-was-lying-to-us-a-deploy-debugging-story-9fi
author: Vicente G. Reyes
date: '2026-09-01'
description: I had a GitHub Actions workflow called Deploy to DigitalOcean. It had been sitting in the repo for... Tagged with githubactions, docker, django, devops.
tags: '#githubactions, #docker, #django, #devops'
---

I had a GitHub Actions workflow calledDeploy to DigitalOcean. It had been sitting in the repo for weeks, fully wired up — SSH action, secrets references, the works. And yet every single time I shipped a backend change, I still had to SSH into the droplet and rungit pullby hand.

I hadn't stopped to askwhyuntil I actually went looking. It turned out the pipeline wasn't broken in any one obvious way — it was broken in six small, unrelated ways, stacked on top of each other, each one hiding the next. This is the story of digging through all of them, in the order I actually found them.

## Act 1: The Deploy Job That Never Ran

The setup looked correct on paper.deploy.ymlwas gated like this:

on
:

 
workflow_run
:

 
workflows
:
 
[
'
CI'
]

 
branches
:
 
[
'
main'
]

 
types
:
 
[
completed
]

jobs
:

 
deploy
:

 
if
:
 
${{ github.event.workflow_run.conclusion == 'success' }}

Enter fullscreen mode

Exit fullscreen mode

Reasonable: only deploy if CI passed. So the first thing worth checking wasn't the deploy job at all — it was whether CI hadeverpassed onmain.

gh run list 
--workflow
=
ci.yml 
--limit
 5

Enter fullscreen mode

Exit fullscreen mode

Every single row:failure. Every deploy run:skipped. The deploy pipeline wasn't broken — it was doing exactly what it was told, gating correctly on a CI workflow that had never once gone green onmain. I hadn't connected those dots because the failures and the missing deploys lived in two different tabs of the Actions UI.

## Act 2: Two Bugs Wearing One Trenchcoat

gh run view <run-id>showed two jobs failing for completely unrelated reasons.

Thelinterjobdied immediately:

The specified python version file at: .python-version doesn't exist.

Enter fullscreen mode

Exit fullscreen mode

.python-versionwas sitting right there in the repo root. Except it wasn't — it was in.gitignore, left over from apyenvboilerplate line nobody had questioned.actions/setup-python'spython-version-fileinput needs the file to actually exist in the checkout, and a gitignored file never reaches CI no matter how real it looks on disk locally.

Thefrontendjobdied differently:

Error: [vitest-pool]: Failed to start forks worker for test files ...
Caused by: TypeError: webidl.util.markAsUncloneable is not a function

Enter fullscreen mode

Exit fullscreen mode

That error has nothing to do with my test code.ci.ymlpinnednode-version: '20', butjsdom@30(a Vitest dependency) requires:

"engines"
:
 
{
 
"node"
:
 
"^22.22.2 || ^24.15.0 || >=26.0.0"
 
}

Enter fullscreen mode

Exit fullscreen mode

Node 20 doesn't havemarkAsUncloneable— jsdom needs it. Every frontend test run was crashing before a single test file even executed. The actual backend test suite (pytest) had been passing this entire time; it was just outvoted by two infrastructure bugs with nothing to do with the code being tested.

Fix: un-ignore.python-version, commit it. Bumpnode-versionto'22'. Two-line diff, two root causes eliminated.

## Act 3: The Debt That Was Always There

Pushed the fix, watched CI run again.pytestandfrontendwent green.linterfailedagain— different reason this time:

black....................................................................Failed
- hook id: black
reformatted job_board/jobs/services.py

isort....................................................................Failed
- hook id: isort
Fixing job_board/jobs/services.py

djLint formatting for Django.............................................Failed
- hook id: djlint-reformat-django
1 file was updated.

Enter fullscreen mode

Exit fullscreen mode

Formatting drift had been quietly accumulating in three files — a multi-line import that black wanted split, a.envsfile missing a trailing newline, anindex.html<meta>tag that djLint wanted wrapped. None of it mattered locally because nobody hadpre-commitwired into their git hooks. It only mattered in CI, which is exactly where it had been failing, unnoticed, this whole time.

The fix here was almost mechanical: CI's own hook outputisthe diff. Applied it verbatim rather than re-deriving it — no ambiguity about what "correctly formatted" means when the formatter already told you.

## Act 4: The Flaky Cache and the Duplicate Runs

Two more small papercuts surfaced once real CI runs were flowing:

A cache backend race.PR-triggered builds started intermittently failing with:

Error: cannot parse bake definitions: ERROR: failed to solve:
failed to load cache key: repository does not contain ref refs/pull/166/merge

Enter fullscreen mode

Exit fullscreen mode

This is a knowndocker/bake-action+ GitHub Actions cache quirk: a PR's merge ref gets recomputed (or invalidated) if the PR updates or merges while the cache backend is still resolving it. It never affected the push-triggered run onmain— the one that actually gates deploy — but it left a false red X on every promotion PR. Buildx's GHA cache backend has a purpose-built escape hatch for exactly this:

django.cache-from=type=gha,scope=django-cached-tests,ignore-error=true

Enter fullscreen mode

Exit fullscreen mode

ignore-error=truedegrades a cache-restore failure to a cache miss instead of failing the whole job.

Duplicate CI runs.With bothpull_request: branches: [main]andpush: branches: [main]as triggers, every promotion ran the exact same commit through CI twice — once when the PR opened, again the instant it merged. Since deploy only ever cares about the post-merge state ofmain, the fix was to drop thepull_requesttrigger entirely and letpushdo the only job that mattered.

While in there, I also pulled thefrontendlint/test job out of backend CI altogether — the frontend deploys through Vercel, which already runs its own build/lint pipeline as a separate PR check. There was no reason a frontend typo should ever gate a DigitalOcean backend deploy, sofrontend/**also got added topaths-ignore— a frontend-only commit no longer triggers a backend rebuild at all.

## Act 5: CI Was Finally Green. Deploy Still Failed.

For the first time,CIshowedsuccesson a push tomain. And for the first time,Deploy to DigitalOceanactuallyraninstead of showingskipped. It failed in 12 seconds:

ssh
.ParsePrivateKey: ssh: 
no
 key found

ssh
: handshake failed: ssh: unable to authenticate, attempted methods [none], 
no
 supported methods remain

Enter fullscreen mode

Exit fullscreen mode

gh secret list 
--repo
 <org>/<repo>

Enter fullscreen mode

Exit fullscreen mode

Zero rows.DO_HOST,DO_USERNAME,DO_SSH_KEY,DO_PORT— none of them existed. The workflow had been referencing four secrets that had simply never been created. CI passing had done its job; it just exposed the next layer down.

## Act 6: Two SSH Gotchas

Setting these up surfaced two mistakes worth writing down because they're both easy to make and easy to misdiagnose.

Gotcha 1 —ssh-copy-idfrom inside the box.Trying to install a public key onto the droplet whilealready SSH'd into that dropletdoesn't work:ssh-copy-idopens anewoutbound connection back to the same host to install the key, but that connection has no valid key to authenticate with yet. Classic chicken-and-egg. Once you're already sitting in a shell on the target machine, skipssh-copy-idand just append directly:

cat
 ~/.ssh/id_ed25519.pub 
>>
 ~/.ssh/authorized_keys

chmod 
700 ~/.ssh

chmod 
600 ~/.ssh/authorized_keys

Enter fullscreen mode

Exit fullscreen mode

Gotcha 2 — mangled secret content.Even after the public key was trusted server-side, the deploy still failed with the exact samessh: no key founderror. The private key had been set as a GitHub secret via a string interpolation (--body "...") rather than a direct file redirect, which had silently collapsed the multi-line PEM block. The fix is to never let anything touch the formatting:

gh secret 
set 
DO_SSH_KEY 
--repo
 <org>/<repo> < ~/.ssh/id_ed25519

Enter fullscreen mode

Exit fullscreen mode

Redirecting the raw file guarantees byte-for-byte fidelity, including the-----BEGIN/END-----lines and every internal newline that a shell string would otherwise eat.

## Act 7: Right Key, Wrong Directory

With auth finally working, the deploy script actually reached the droplet and ran — into a new error:

err: bash: line 1: cd: /home/***/apps/gigglegigs: No such file or directory
err: fatal: not a git repository (or any of the parent directories): .git
err: open /home/***/production.yml: no such file or directory

Enter fullscreen mode

Exit fullscreen mode

deploy.ymlassumed the checkout lived at~/apps/gigglegigs. It didn't — a quickls ~on the droplet showed the actual clone sitting at~/GiggleGigs. That path had apparently been copy-pasted from a different project's deploy config and never actually validated, because the workflow had never gotten far enough to hit it before. One-line fix, and the deploy script finally ran start to finish: build, collectstatic, migrate,up -d, all green.

## Act 8: The First Real Deploy Broke the Site

Two minutes after that first fully green deploy, the admin's user list started returning502 Bad Gateway. The instinct is to panic here — first automated deploy, and the site's down? But the logs told a much less dramatic story:

django-1 | PostgreSQL is available
django-1 | 186 static files copied to '/app/staticfiles', 538 post-processed.
django-1 | [2026-09-01 12:48:17 +0000] [1] [INFO] Starting gunicorn 21.2.0
django-1 | [2026-09-01 12:48:17 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000

Enter fullscreen mode

Exit fullscreen mode

Gunicorn didn't finish booting — Postgres wait,collectstatic, worker fork — until12:48:17. The 502 was timestamped12:48:16. One second earlier. Nothing crashed; I'd just refreshed the admin during the exact window wheredocker compose up -dhad already killed the olddjangocontainer and the new one wasn't listening yet.

That's not really a bug in the app — it's a gap in the deploy setup. Traefik here uses the staticfileprovider, routing unconditionally tohttp://django:5000with zero awareness of container readiness:

services
:

 
django
:

 
loadBalancer
:

 
servers
:

 
-
 
url
:
 
http://django:5000

Enter fullscreen mode

Exit fullscreen mode

Every deploy, without exception, would keep hitting this same window. The right fix is an active health check so Traefik stops sending traffic to a container until it's actually answering:

services
:

 
django
:

 
loadBalancer
:

 
servers
:

 
-
 
url
:
 
http://django:5000

 
healthCheck
:

 
path
:
 
/healthz/

 
hostname
:
 
api.example.com

 
interval
:
 
'
5s'

 
timeout
:
 
'
3s'

Enter fullscreen mode

Exit fullscreen mode

Two things worth calling out about that config. First,/healthz/didn't exist — it needed to be a genuinely trivial, unauthenticated view (no DB touch, no auth, just200 OK), because coupling infra health to a real business endpoint means a permissions change or a slow query silently takes your health check down with it. Second,hostnameisn't optional: without it, Traefik's health check request sendsHost: django(the internal service name), andALLOWED_HOSTS— quite correctly — rejects that as aDisallowedHost, returning400and making Traefik think the container is permanently unhealthy. Settinghostnameto the real public domain makes the health check's request indistinguishable from real traffic, from Django's point of view.

While already inproduction.yml, I addedrestart: unless-stoppedto every long-running service (everything except the one-off backup container). Without it, a droplet reboot — a DigitalOcean maintenance window, a crash, anything — leaves every container down until someone notices and SSHes in to bring them back up manually.unless-stoppedmeans Docker brings them back on its own the moment the daemon starts.

## What Actually Was Wrong, All Together

Laid out in one place, the full list is almost funny:

1. A gitignored file broke Python setup in CI
2. A pinned Node version was two majors behind what a dependency required
3. Formatting drift had been silently failing lint for who knows how long
4. A GHA cache backend race gave false negatives on PR checks
5. CI ran twice per promotion for no reason
6. Zero deploy secrets existed
7. A private key got mangled by shell interpolation
8. The deploy script's target directory was simply wrong
9. Traefik had no way to know when a container wasn't ready yet
10. Nothing would restart itself after a reboot

No single one of these was hard to fix once found. What made this a slog was thateach bug hid the next one— CI had to go green before deploy secrets could even matter; deploy secrets had to work before the wrong directory path could surface; the deploy had to actuallysucceedbefore the Traefik timing gap became visible at all. A pipeline with ten small breakages in series doesn't look like ten breakages. It looks like one big wall, and the only way through it is to fix the outermost failure, rerun, and see what the next layer reveals.

## Takeaway

If your "automated" deploy still requires someone to manually pull and rebuild, don't assume the deploy job itself is broken — check whether the thing gating it haseveractually succeeded. A pipeline that's silently and permanently gated behind a red CI run looks, from a distance, exactly like a pipeline that doesn't exist. The fix isn't usually one big rewrite. It's peeling one failing layer at a time until the thing underneath finally gets a chance to run — and then trusting the next error message, however unrelated it looks, to point at the next real problem.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
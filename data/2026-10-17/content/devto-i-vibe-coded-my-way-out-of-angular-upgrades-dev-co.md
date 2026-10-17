---
title: I Vibe-Coded My Way Out of Angular Upgrades - DEV Community
url: https://dev.to/gramli/i-vibe-coded-my-way-out-of-angular-upgrades-4fkh
site_name: devto
content_file: devto-i-vibe-coded-my-way-out-of-angular-upgrades-dev-co
fetched_at: '2026-10-17T14:04:08.878667'
original_url: https://dev.to/gramli/i-vibe-coded-my-way-out-of-angular-upgrades-4fkh
author: Daniel Balcarek
date: '2026-10-15'
description: Do you also hate upgrading Angular versions? Because I do. I maintain a few open-source projects, and... Tagged with ai, vibecoding, angular, showdev.
tags: '#showdev, #ai, #vibecoding, #angular'
---

CI pipeline failures reveal local vs remote quirks

Do you also hate upgrading Angular versions? Because I do. I maintain a few open-source projects, and upgrading Angular is probably my least favorite maintenance task. That's also why my frontend updates often get postponed for far too long.

But we have AI now, right? It should be able to handle this with some instructions. So I decided to create (or rather vibe-code) anAngular Update Skill for Codex.

## Creating the skill

Upgrading Angular isn't just about runningng update. There are several things I normally have to take care of, so I created a prompt describing what the skill should do:

* Follow the officialAngular Update Guide.
* Create a separate Git branch for the upgrade.
* Handle migrations and dependency updates.
* Validate that everything still builds and works.
* Follow the same good practices I would use when upgrading Angular manually.

(Updating NuGet packages in .NET feels so much simpler.)

Codex generated the first version of the skill, and surprisingly, it worked!

Well... locally.

### First problem: npm ci

After pushing my changes to GitHub, the CI pipeline failed with:

npm ci can only install packages when your package.json and package-lock.json are in sync.

Enter fullscreen mode

Exit fullscreen mode

Classic "works on my machine" problem. The skill had managed to update Angular, but it hadn't properly validated that a clean installation would work. So I added another validation step: runnpm cibefore considering the upgrade complete. This way, the agent can catch problems with the lock file before they reach CI.

### Second problem: npm publishing

Then I ran into another issue when trying to publish my Angular library to npm:

npm error code E404
npm error 404 Not Found - PUT https://registry.npmjs.org/gramli-angular-mydatepicker - Not found

Enter fullscreen mode

Exit fullscreen mode

At first, the error wasn't particularly helpful. After some investigation, I found that my publishing environment was using Node.js 22 with npm 10.

However, according to thenpm trusted publishing documentation, trusted publishing requires:

* Node.js 22.14.0 or higher
* npm 11.5.1 or higher

So I updated the skill again to prefer the latest Node.js LTS version compatible with the target Angular version, while also making sure the npm version meets any publishing requirements.

### Third problem: the skill was getting too big

After all these improvements, the skill was becoming quite large. That might not matter much with generous token limits, but I also wanted it to be usable by people working with more limited AI budgets. So I shortened the instructions, removed unnecessary repetition, and kept the important validation steps. The main skill went from 1,252 words to 701 words, with the complete bundle becoming approximately 40% shorter.

## Testing it on real projects

Of course, generating a skill is one thing. Actually using it is another. So far, I've used the current version on three of my open-source projects:

* Angular 21 → 22:angular-mydatepicker PR #12
* Angular 19 → 22:FileApi PR #13
* Angular 21 → 22:AuthApi PR #113

The Angular 19 → 22 upgrade was especially interesting because it required migrations across three major versions. In the AuthApi project, the upgrade also involved replacing PrimeNG with Optimus UI because of the PrimeNG licensing changes.

All three upgrades have now been merged.

## Three Projects Later

The current version works pretty well, at least on my smaller projects. It's not perfect, though. Some Angular projects are much more complicated than mine, so the skill would probably need to be adapted for them. But it already helped me upgrade three projects, and I learned a few things along the way.

The best part? I finally updated my Angular projects in just ONE WEEK instead of postponing them again. 😁

I wanted to share this with the community because it might help someone else. If you want to try the skill or improve it, you can find it here:

Angular Update Skill on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (29 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
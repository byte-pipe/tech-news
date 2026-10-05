---
title: Turn Your GitHub Contribution Graph Into an ASCII City - DEV Community
url: https://dev.to/sizzlebop/turn-your-github-contribution-graph-into-an-ascii-city-ic5
site_name: devto
content_file: devto-turn-your-github-contribution-graph-into-an-ascii
fetched_at: '2026-10-05T12:19:51.890712'
original_url: https://dev.to/sizzlebop/turn-your-github-contribution-graph-into-an-ascii-city-ic5
author: Jessica Doering
date: '2026-10-03'
description: I decided that a normal GitHub contribution graph is not enough. So I turned mine into a city. And... Tagged with github, opensource, go, showdev.
tags: '#showdev, #github, #opensource, #go'
---

Generates animated SVGs for profile READMEs

I decided that a normal GitHub contribution graph is not enough.

So I turned mine into a city.

And I wanted to share it so you can too.

I madeSkyline, a small Go CLI that takes your GitHub contribution history and turns it into an ASCII city.

Each week becomes a building.

Each day becomes a window.

If you contributed that day, the window lights up. Busier days get brighter colors, your biggest week gets a little antenna, and the whole thing ends up looking like a tiny city built from your coding activity.

It can render directly in your terminal, but my favorite part is that it can also generate an animated SVG for your GitHub profile README.

I mean my GitHub profile definitely needed infrastructure.

## How it works

The contribution graph maps surprisingly well to a skyline.

Each building represents one week of activity, and the height is based on the total contributions from that week.

The windows represent the seven days inside it.

A day with no activity stays dark:

·

Enter fullscreen mode

Exit fullscreen mode

A day with contributions lights up:

▪

Enter fullscreen mode

Exit fullscreen mode

The color intensity follows GitHub's contribution levels, so more active days get brighter windows.

There are also a few purely decorative bits because I couldn't resist.

Stars are scattered through the sky, some windows flicker in the SVG version, and the brightest stars twinkle.

The animations are deterministic, so regenerating the same contribution data doesn't completely rearrange your city every time.

## There are themes of course

I started with neon and then immediately did the completely predictable thing and added more.

There are currently 12:

* neon
* synthwave
* matrix
* amber
* ice
* sunset
* toxic
* vapor
* crimson
* mono
* prism
* rainbow

You can preview them right in the terminal:

skyline 
-themes

Enter fullscreen mode

Exit fullscreen mode

And choose one with:

skyline 
-theme
 synthwave your-username

Enter fullscreen mode

Exit fullscreen mode

Personally, I am incapable of making terminal software without eventually adding neon colors to it, so this was inevitable.

## Running it locally

You'll need Go 1.25 or newer.

Install Skyline with:

go 
install 
github.com/pinkpixel-dev/skyline@latest

Enter fullscreen mode

Exit fullscreen mode

Then run:

skyline your-username

Enter fullscreen mode

Exit fullscreen mode

Skyline needs access to the GitHub API, but it tries to make authentication fairly painless.

It checks:

GITHUB_TOKEN
GH_TOKEN
gh auth token

Enter fullscreen mode

Exit fullscreen mode

So if you're already authenticated with the GitHub CLI, there's a good chance you don't need to configure anything else.

The full city is 106 columns wide. If your terminal is a little less enthusiastic about this arrangement, you can render fewer weeks:

skyline 
-weeks
 30 your-username

Enter fullscreen mode

Exit fullscreen mode

You can also change the maximum building height:

skyline 
-height
 10 your-username

Enter fullscreen mode

Exit fullscreen mode

## Generating the SVG

To create the version you can use on a website or GitHub profile:

skyline 
-svg
 skyline.svg your-username

Enter fullscreen mode

Exit fullscreen mode

Or combine options:

skyline 
-theme
 prism 
-svg
 skyline.svg your-username

Enter fullscreen mode

Exit fullscreen mode

That generates the animated SVG version instead of printing the city to the terminal.

The animation also respectsprefers-reduced-motion, so it stays static for anyone who has reduced motion enabled.

## Putting it on your GitHub profile

This is probably my favorite use for it.

You can have GitHub Actions regenerate your city automatically every night so your skyline changes along with your contribution graph.

Your GitHub profile README lives in a repository with the same name as your username:

github.com/your-username/your-username

Enter fullscreen mode

Exit fullscreen mode

Inside that repository, create:

.github/workflows/skyline.yml

Enter fullscreen mode

Exit fullscreen mode

Then add:

name
:
 
skyline

on
:

 
schedule
:

 
-
 
cron
:
 
"
17
 
3
 
*
 
*
 
*"

 
workflow_dispatch
:

permissions
:

 
contents
:
 
write

jobs
:

 
skyline
:

 
runs-on
:
 
ubuntu-latest

 
steps
:

 
-
 
uses
:
 
actions/setup-go@v7

 
with
:

 
go-version
:
 
stable

 
-
 
name
:
 
Draw skyline

 
env
:

 
GITHUB_TOKEN
:
 
${{ secrets.SKYLINE_TOKEN || secrets.GITHUB_TOKEN }}

 
run
:
 
go run github.com/pinkpixel-dev/skyline@latest -theme neon -svg skyline.svg "${{ github.repository_owner }}"

 
-
 
name
:
 
Publish to output branch

 
env
:

 
TOKEN
:
 
${{ secrets.GITHUB_TOKEN }}

 
run
:
 
|

 
mkdir out && mv skyline.svg out/ && cd out

 
git init -q -b output

 
git add skyline.svg

 
git -c user.name="github-actions[bot]" \

 
-c user.email="41898282+github-actions[bot]@users.noreply.github.com" \

 
commit -qm "Update skyline"

 
git push -qf "https://x-access-token:${TOKEN}@github.com/${{ github.repository }}.git" output

Enter fullscreen mode

Exit fullscreen mode

You can swap:

-theme neon

Enter fullscreen mode

Exit fullscreen mode

for whichever theme you want.

Commit the workflow, open theActionstab on GitHub, and run theskylineworkflow manually once.

That creates theoutputbranch containingskyline.svg.

Then add this to your profile README:

![
My skyline
](
https://raw.githubusercontent.com/YOUR-USERNAME/YOUR-USERNAME/output/skyline.svg
)

Enter fullscreen mode

Exit fullscreen mode

ReplaceYOUR-USERNAMEwith your actual GitHub username.

After that, the workflow redraws it automatically every night.

The generated SVG lives on the separateoutputbranch, so you also don't end up with a year's worth of"update skyline"commits cluttering the main branch of your profile repo.

## What about private contributions?

The workflow uses GitHub's built-in Actions token by default.

Depending on what contribution data GitHub exposes through that token, you might notice that your skyline looks a little emptier than the contribution graph you see while logged in.

If that happens, you can create a classic personal access token with theread:userscope and add it to the profile repository as a secret named:

SKYLINE_TOKEN

Enter fullscreen mode

Exit fullscreen mode

The workflow will automatically use that instead when it's available.

## Unnecessary?

I suppose. But it's fun.

Why not take the data we already look at constantly and turn it into something a little more interesting? Contribution graphs are useful, but seeing an entire year transformed into this little glowing city makes it feel much more personal.

And because it's just an SVG, once the Action is configured there really isn't anything else to maintain. Your skyline just keeps changing as you work.

So yeah, you make one for your profile, I'd genuinely love to see it!

The project is open source here:

github.com/pinkpixel-dev/skyline

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
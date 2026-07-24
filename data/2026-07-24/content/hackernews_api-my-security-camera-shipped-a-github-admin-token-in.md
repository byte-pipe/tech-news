---
title: My security camera shipped a GitHub admin token in its login page
url: https://hhh.hn/hanwha-github-token/
site_name: hackernews_api
content_file: hackernews_api-my-security-camera-shipped-a-github-admin-token-in
fetched_at: '2026-07-24T19:32:36.561750'
original_url: https://hhh.hn/hanwha-github-token/
author: hhh
date: '2026-07-24'
description: i dissected some firmware for a Hanwha Wisenet XNP-9300RW and found that it had github admin tokens in it, also miltech is weird
tags:
- hackernews
- trending
---

i have been thinking a bit more about security cameras again, because ofAXIS starting to push more for every one of their cameras to be able to easily run linux applications on them, they're far more serious targets in an enterprise environment and need to be managed as such for vulnerabilities and credential management etc. someone brought up to me a company that sounded new to me, Hanwha (Vision.) I took a look at the site, and found that they had accessible firmware blobs for each model of camera, which is always a treat.

### poking and prodding

i took the image and threw it at binwalk hoping it was just a rootfs or something, but inside there was a separate tarball with some AI stuff for the camera and afwimage.tgzthat binwalk was flagging as encrypted.

I was googling around and saw thatMatt Brown has a writeup on these cameras that got me through. basically the passphrase isHTW+ the model number soHTWXNP-9300RWworked.

seems like they do some more stuff now, because inside ofthattarball wasanotherfwimage.tgzthat was encrypted but it wasn't the same scheme, so we can't just re-use the same setup from Matt Brown. I kinda figured I was gonna have to give up and that Hanwha was doing something more advanced, like burning a key into the hardware (which isnt foolproof obviously but you at least need to own the camera to start.) Anyways, there was afwupgraderbinary that was in that outer tarball, so I threw it into ghidra and started poking around.

well I would have been poking around if it was 2023 or something, but i pointed claude code at it and went to make a lovely dinner and spent time with my partner instead, and came back a bit later to a description and a nice rootfs.

Hanwha had built some obfuscation into thefwupgraderto hide how they decrypt the actual rootfs. the AES key is XOR'd against a small static key table in the binary and reassembled at runtime ( the IV is just plaintext in there) thefwupgraderjust shells out to theopensslCLI, and even the command fragments are XOR-obfuscated the same way.

reconstructed the command looks like this:

openssl enc -md sha256 -aes-256-cbc -d \
 -K <KEY> -iv <IV> -in <INPUT> -out <OUTPUT>

Since the key and iv are just hardcoded (the same across the model line), I will publish them here:

KEY = dfa049bb922e63e2decc764af5628068e5b7a2662e479a615b14643e567579b0
IV = 53f926801b81454a4f889c9a390db6e6

and with that we have a full rootfs to dig into normally.

### truffles

since we finally can just look at stuff I ran trufflehog immediately to see if there was anything obvious, and there was a github token duplicated in like 30 files... I checked what repos the token had access to, and it had admin privileges to hundreds of repositories in their github organization.

this isn't my first rodeo with an org shipping a Github token in their firmware though... but that's a story for a different blog post. Why would this org put this token in like 30 files though? it looks like they build the UI for these cameras with vite, and one of the variables is being set to the entirety ofprocess.envat build time, which means the entirety of the CI job's environment is being written to these files.

var W = {
 DATAPORT: "9090",
 GIT_LFS_SKIP_SMUDGE: "1",
 npm_command: "run-script",
 KUBERNETES_SERVICE_PORT_HTTPS: "443",
 GITHUB_NPM_TOKEN: "<snip>:ghp_…REDACTED…",
 npm_config_userconfig: "/home/docker/.npmrc",
 // etc

I don't have any of these cameras to test, butI thinkthis would mean that anyone accessing the admin ui of these cameras likely has had this github token sent to them over the wire and (hopefully) nobody evil noticed. Maybe it didn't get actually served and just lived on disk, though.

there were some other... interesting bits of data in the environment though: there were some env vars with IP addresses in them, but they are assigned to the US Department of Defense:

* SWARM_MASTER_NFS_ADDRESS: 55.101.212.23
* OTEL_ELASTIC_URL: http://55.101.212.21:5601/<snip>
* CIMIP: 55.101.211.213

huh... is this just a coincidence and one of those weird instances where people have taken IP space for internal services when they know they will never interact with it (insane practice btw...) or is Hanwha more directly tied with the US DoD?

let's look at the wikipedia page forHanwha Vision:

Hanwha Vision(Korean: 한화비전), founded asSamsung Techwin, is a video surveillance company. It is a subsidiary ofHanwha Group.

Former products

K9 Thunderself-propelled artillery,K10 ammunition resupply vehicles, sub-systems forK2 Black Panther,sentry gunrobotSGR-A1.

oh... okay.... I remember reading about theSGR-A1 when I was in high school, but I never thought I would be accidentally finding keys to the kingdom of the manufacturer on the ground later in my career... my life is kinda weird sometimes...

#### SPECULATION WARNING

even still, these aren't American devices, or anything like that. Why would Hanwha Vision need anything remotely related to the DoD? Is it possible that their CI is provided by some centralized team at their parent company Hanwha, where the needs of their sister companyHanwha Aerospacecause the shared platform to have these entries in the CI environment variables? Or maybe because of their other sister company,Hanwha Defense USA, where they make other large scary steel machines

### a little extra digging

I wanted to make sure this wasn't some kind of fluke, and that there weren't hundreds of other different github tokens in their firmware, so I scraped the Hanwha website to download every firmware for every camera i could find, and ended up with around ~500 firmwares (there were like 600 smth cameras but not all of them had firmware listed) and I was able to extract 62% of them with the same approach as above, and only three of them had github tokens, and they were all the same token.

not really sure why the others didn't work, but it's close enough for me to feel satisfied.

### disclosure

I wrote up a very small email with enough information to identify where the token was and sent it over to Hanwha, who have a nice open email for reporting security issues, and they responded within 12 hours notifying me that the token had been revoked. Sure they shouldn't have ever had a gh token in there but I have never had such a prompt response and resolution.

we really gotta stop making these mistakes so often, how am I supposed to be sleeping at night?

thanks computer, until next time
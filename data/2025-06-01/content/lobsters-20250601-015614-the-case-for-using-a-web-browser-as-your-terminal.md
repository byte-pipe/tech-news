---
title: The case for using a web browser as your terminal
url: |
  https://blog.pomdtr.me/posts/tweety-v1/
site_name: lobsters
fetched_at: |
  2025-06-01T01:56:14.979875
original_url: |
  https://blog.pomdtr.me/posts/tweety-v1/
date: 2025-06-01
description: I guess I write stuff.
tags: browsers, web
---



# The case for using a web browser as your terminal

by pomdtr

May 29th, 2025

4 min read

I don't actively use a terminal emulator app on my computer anymore, and usetweetyinstead from my web browser. I think you should consider doing the same.

## My browser is eating all my apps, and I like it

I don't really have a usecase for native apps anymore. All of the apps I use are web-based, so it make sense for me to use a web browser as my only opened app. Instead of having a bunch of window with their own set of tabs, I can manage everything from a single one.

However, as a developer, it is unthinkable to not have a terminal emulator app opened to run commands, manage and edit files, or interact with remote servers. Ideally, I would like those two remaining apps to be merged into a single one.

There have been some experiments on adding webviews to terminal emulators, such as theWave Terminalorawrit. While interesting, these projects are not a substitute to running a capable web browser.

I feel like going the other way around is much more interesting.ttydallows you to run a terminal emulator from a browser tab. It is mainly intended to share a terminal session over the web, but you can also run it completely locally.

$ ttyd --writable bash
Listening on port: 7681

It just works great! When paired with a capable web browser likeArcorZen, you can easily even split websites and terminal sessions in the same view.

Ttyd was missing some features that I wanted (ex: automatic light/dark mode,or a set of builtin themes), so I created my own project inspired by it, calledtweety. The rest of this article will focus on this specific project, but you can apply the same ideas to ttyd.

You can installtweetyon macOS and Linux usingHomebrew:

brew
install
 pomdtr/tap/tweety

## Going one step further: mapping URL to commands

tweetysupports passing args to a script using theargsquery parameter. For example, if you runtweety <entrypoint>thehttp://localhost:9999/?args=nvim+~/.bashrcurl will be mapped to the command<entrypoint> nvim ~/.bashrc.

The naive implementation of the entrypoint script would look like this:

#!/bin/sh

# ⚠️ Do not do this, this is dangerous!

exec

"
$@
"

But of course, you don't want to directly exec shell commands coming fromGETrequests, as someone could just easily redirect you to a malicious url likehttp://localhost:9999/?args=rm+-rf+%2Fand delete your entire filesystem.

So we'll the input use our entrypoint scripts to only allow a set of commands and arguments that we trust.

#!/usr/bin/env -S deno run --allow-run

import

{
 program
}

from

'npm:@commander-js/extra-typings'

import

{
 existsSync
}

from

"jsr:@std/fs"

// little helper to run commands

async

function

run
(
command
:

string
,

...
args
:

string
[
]
)

{


const
 cmd
=

new

Deno
.
Command
(
command
,

{
 args
}
)
;


const
 process
=
 cmd
.
spawn
(
)
;


await
 process
.
status
;

}

// handle http://localhost:9999/

program
.
action
(
async

(
)

=>

{


await

run
(
"bash"
)

}
)

// handle http://localhost:9999?args=htop

program
.
command
(
"htop"
)
.
action
(
async

(
)

=>

{


await

run
(
"htop"
)
;

}
)

// handle http://localhost:9999?args=ssh+<host>

program
.
command
(
"ssh"
)
.
argument
(
"<host>"
)
.
action
(
async

(
host
:

string
)

=>

{


await

run
(
"ssh"
,
 host
)
;

}
)

// handle http://localhost:9999?args=config

program
.
command
(
"config"
)
.
action
(
async

(
)

=>

{


const
 scriptPath
=

new

URL
(
import
.
meta
.
url
)
.
pathname
;


await

run
(
"nvim"
,
 scriptPath
)

}
)

// handle http://localhost:9999?args=nvim+<file>

program
.
command
(
"nvim"
)
.
argument
(
"<file>"
)
.
action
(
async

(
file
)

=>

{


// protect use again `nvim 'term://<malicious-command>'`


if

(
file
.
startsWith
(
"term://"
)
)

{


console
.
error
(
"Invalid file path: cannot use 'term://' prefix"
)
;

        Deno
.
exitCode
=

1
;


return
;


}


await

run
(
"nvim"
,
 file
)

}
)

if

(
import
.
meta
.
main
)

{


// parse arguments and run the appropriate command


await
 program
.
parseAsync
(
)
;

}

As a general rule, you should only allow commands that do not perform any destructive actions, such asrm,mv, orcpand instead use interactive commands likenvim,htoporsshthat requires user input to perform actions.

## Using a custom search engine to run commands

All modern web browsers supports defining custom search engines. You can use this feature to run commands directly from the address bar.

Just usehttp://localhost:9999/?args=%sas the URL, and%sas the placeholder for the command. You can then usetweetyas a search engine to run commands directly from the address bar.

## Saving commands as bookmarks

Since each command has a unique URL, you can save them as bookmarks in your web browser. This allows you to quickly access frequently used commands without having to type them every time.

In the arc browser, I make use of the Favorites feature to group commands into folders. The ability to rename them and assign icons makes it easy to identify them at a glance.

## Usinghttpsand local certificates

By pairing a reverse proxy likeCaddy, you can easily get ahttps://URL for your terminal emulator, protected behind local certificates.

tweety.localhost {
    tls internal
    reverse_proxy localhost:9999
}

Now you can acces your terminal emulator athttps://ttyd.localhost.

## Startingtweetyat login

Here is my plist file to starttweetyat login on macOS. You can save it as~/Library/LaunchAgents/com.github.pomdtr.tweety.plistand load it withlaunchctl load ~/Library/LaunchAgents/com.github.pomdtr.tweety.plist.

<!
DOCTYPE

plist

PUBLIC

"-//Apple//DTD PLIST 1.0//EN"

"http://www.apple.com/DTDs/PropertyList-1.0.dtd"
>

<
plist

version
=
"
1.0
"
>

<
dict
>


<
key
>
KeepAlive
</
key
>


<
true
/>


<
key
>
Label
</
key
>


<
string
>
com.github.pomdtr.tweety
</
string
>


<
key
>
LimitLoadToSessionType
</
key
>


<
array
>


<
string
>
Aqua
</
string
>


<
string
>
LoginWindow
</
string
>


</
array
>


<
key
>
ProgramArguments
</
key
>


<
array
>


<
string
>
/Users/pomdtr/go/bin/tweety
</
string
>


<
string
>
--theme=Tomorrow
</
string
>


<
string
>
--theme-dark=Tomorrow Night
</
string
>


<
string
>
/Users/pomdtr/.config/tweety/entrypoint.ts
</
string
>


</
array
>


<
key
>
RunAtLoad
</
key
>


<
true
/>


<
key
>
StandardErrorPath
</
key
>


<
string
>
/Users/pomdtr/Library/Logs/tweety.log
</
string
>


<
key
>
StandardOutPath
</
key
>


<
string
>
/Users/pomdtr/Library/Logs/tweety.log
</
string
>


<
key
>
WorkingDirectory
</
key
>


<
string
>
/Users/pomdtr
</
string
>


<
key
>
EnvironmentVariables
</
key
>


<
dict
>


<
key
>
PATH
</
key
>


<
string
>
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:/Users/pomdtr/go/bin/
</
string
>


</
dict
>

</
dict
>

</
plist
>

On Linux, you should be able to use a systemd service instead.

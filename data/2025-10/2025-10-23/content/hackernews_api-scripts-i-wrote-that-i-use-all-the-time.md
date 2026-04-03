---
title: Scripts I wrote that I use all the time
url: https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/
site_name: hackernews_api
fetched_at: '2025-10-23T11:13:13.215291'
original_url: https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/
author: speckx
date: '2025-10-22'
published_date: '2025-10-22T00:00:00+00:00'
description: I've written a number of little scripts over the years, many of which I use every day. Here's a little collection.
tags:
- hackernews
- trending
---

# Scripts I wrote that I use all the time

by
Evan Hahn
,
posted

Oct 22, 2025

In mydecade-plus of maintaining my dotfiles, I’ve written a lot of little shell scripts. Here’s a big list of my personal favorites.

## Clipboard

copyandpastaare simple wrappers around system clipboard managers, likepbcopyon macOS andxclipon Linux. I use theseall the time.

# High level examples

run_some_command | copy

pasta > file_from_my_clipboard.txt

# Copy a file's contents

copy < file.txt

# Open a file path from your clipboard

vim
"
$(
pasta
)
"

# Decode some base64 from the clipboard

pasta | base64 --decode

pastasprints the current state of your clipboard to stdout, and then whenever the clipboard changes, it prints the new version. I use this once a week or so.

# High level example

pastas > everything_i_copied.txt

# Download every link I copy to my clipboard

pastas | wget -i -

cpwdcopies the current directory to the clipboard. Basicallypwd | copy. I often use this when I’m in a directory and I want use that directory in another terminal tab; I copy it in one tab andcdto it in another. I use this once a day or so.

## File management

mkcd foomakes a directory andcds inside. It’s basicallymkdir foo && cd foo. I use thisall the time—almost every time I make a directory, I want to go in there.

tempechanges to a temporary directory. It’s basicallycd "$(mktemp -d)". I use thisall the timeto hop into a sandbox directory. It saves me from having to manually clean up my work. A couple of common examples:

# Download a file and extract it

tempe

wget
'https://example.com/big_file.tar.xz'

tar -xf big_file.tar.xz

# ...do something with the file...

# Write a quick throwaway script to try something out

tempe

vim foo.py

python3 foo.py

trash a.txt b.pngmovesa.txtandb.pngto the trash. Supports macOS and Linux. I use this every day. I definitely run it more thanrm, and it saves me from accidentally deleting files.

mkshmakes it quick to create shell scripts.mksh foo.shcreatesfoo.sh, makes it executable withchmod u+x, adds some nice Bash prefixes, and opens it with my editor (Vim in my case). I use this every few days. Many of the scripts in this post were made with this helper!

## Internet

serveitstarts a static file server onlocalhost:8000in the current directory. It’s basicallypython3 -m http.server 8000but handles cases where Python isn’t installed, falling back to other programs. I use this a few times a week. Probably less useful if you’re not a web developer.

getsongusesyt-dlpto download songs, often from YouTube or SoundCloud, in the highest available quality. For example,getsong https://www.youtube.com/watch?v=dQw4w9WgXcQdownloads that video as a song. I use this a few times a week…typically to grab video game soundtracks…

getpodsimilarly usesyt-dlpto download something for a podcast player. There are a lot of videos that I’d rather listen to like a podcast. I use this a few times a month.

getsubsdownloads the English subtitles for a video. (There’s some fanciness to look for “official” subtitles, falling back to auto-generated subtitles.) Sometimes I read the subtitles manually, sometimes I rungetsubs https://video.example/foo | ollama run llama3.2 "Summarize this", sometimes I just want it as a backup of a video I don’t want to save on my computer. I use this every few days.

wifi off,wifi on, andwifi toggleare useful for controlling my system’s wifi.wifi toggleis the one I use most often, when I’m having network trouble. I use this about once a month.

url "$my_url"parses a URL into its parts. I use this about once a month to pull data out of a URL, often because I don’t want to click a nasty tracking link.

url
'https://evil.example/track-user-link?url=https%3A%2F%2Furl-i-want-to-visit.example&track=06f8582a-91e6-4c9c-bf8e-516884584aba#cookie=123'

# original: https://evil.example/track-user-link?url=https%3A%2F%2Furl-i-want-to-visit.example&track=06f8582a-91e6-4c9c-bf8e-516884584aba#cookie=123

# protocol: https

# hostname: evil.example

# path: /track-user-link

# query: url=https%3A%2F%2Furl-i-want-to-visit.example&track=06f8582a-91e6-4c9c-bf8e-516884584aba

# - url https://url-i-want-to-visit.example

# - track 06f8582a-91e6-4c9c-bf8e-516884584aba

# hash: cookie=123

## Text processing

line 10prints line 10 from stdin. For example,cat some_big_file | line 10prints line 10 of a file. This feels like one of those things that should be built in, likeheadandtail. I use this about once a month.

scratchopens a temporary Vim buffer. It’s basically an alias for$EDITOR $(mktemp). I use this about once a day for quick text manipulation tasks, or to take a little throwaway note.

straightquoteconverts “smart quotes” to “straight quotes” (sometimes called “dumb quotes”). I don’t care much about these in general, but they sometimes weasel their way into code I’m working on. Itcanalso make the file size smaller, which is occasionally useful. I use this at least once a week.

markdownquoteadds>before every line. I use it in Vim a lot; I select a region and then run:'<,'>!markdownquoteto quote the selection. I use this about once a week.

length fooreturns3. (I should probably just usewc -c.)

jsonformattakes JSON at stdin and pretty-prints it to stdout. I use this a few times a year.

upperedandloweredconvert strings to upper and lowercase. For example,echo foo | upperedreturnsFOO. I use these about once a week.

nato barreturnsBravo Alfa Romeo. I use this most often when talking to customer service and need to read out a long alphanumeric string, which has only happened a couple of times in my whole life. But it’s sometimes useful!

u+ 2025returnsñ, LATIN SMALL LETTER N WITH TILDE. A quick way to do a lookup of a Unicode string. I don’t use this onethatoften…probably about once a month.

snippets foocats~/.config/evanhahn-snippets/foo. I usesnippet arrowfor→,snippet recruiterfor a quick “not interested” response to job recruiters,snippet loremto print a “Lorem ipsum” block, and a few others. I probably use one or two of these a week.

## REPL launchers

Inspired by Ruby’s built-inirbREPL, I’ve made:

* icljto start a Clojure REPL
* ijsto start a Deno REPL (or a Node REPL when Deno is missing)
* iphpto start a PHP REPL
* ipyto start a Python REPL
* isqlto start a SQLite shell (an alias forsqlite3 :memory:)

## Dates and times

hoyprints the current date in ISO format, like2020-04-20. I use thisall the timebecause I like to prefix files with the current date.

timer 10mstarts a timer for 10 minutes, then (1) plays an audible ring sound (2) sends an OS notification (seenotifybelow). I often usebb timer 5mto start a 5 minute timer in the background (seebbbelow). I use this almost every day as a useful way to keep on track of time.

rnprints the current time and date usingdateandcal. I probably use it once a week. It prints something like this:

 4:20PM on Wednesday, October 22, 2025

 September 2025
Su Mo Tu We Th Fr Sa
 1 2 3 4 5 6
 7 8 9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30

## Audio and video and pictures

ocr my_image.pngextracts text from an image and prints it to stdout. It only works on macOS, unfortunately, but I want to fix that. (I wrotea post about this script.)

boop(an alias, not a shell script) makes a happy sound if the previous command succeeded and a sad sound otherwise. I do things likerun_the_tests ; boopwhich will tell me, audibly, whether the tests succeed. It’s also helpful for long-running commands, because you get a little alert when they’re done. I use thisall the time.

sfx foobasically just plays~/.config/evanhahn-sfx/foo.ogg. Used inboopandtimerabove.

tunesusesmpvto play audio from a file. I use thisall the time, runningtunes --shuffle ~/music.

pixusesmpvto show a picture. I use this a few times a week to look at photos.

radiois a little wrapper around some of my favorite internet radio stations.radio lofiandradio salsaare two of my favorites. I use this a few times a month.

speakreads from stdin, removes all Markdown formatting, and pipes it to a text-to-speech system (sayon macOS andespeak-ngon Linux).I like using text-to-speech when I can’t proofread out loud.I use this a few times a month.

shrinkvidis anffmpegwrapper that compresses a video a bit. I use this about once a month.

removeexifremoves EXIF data from JPEGs. I don’t use this much, in part because it doesn’t remove EXIF data fromotherfile formats like PNGs…but I keep it around because I hope to expand this one day.

tuividis one I almost never use, but you can use it to watch videos in the terminal. It’s cursed and I love it, even if I never use it.

## Process management

eachis my answer toxargsandfind ... -exec, which I find hard to use. For example,ls | each 'du -h {}'runsdu -hon every file in a directory. I use this infrequently but I always mess upxargsso this is a nice alternative.

running foois likeps aux | grep foobut much easier (for me) to read—just the PID (highlighted in purple) and the command.

murder fooormurder 1234is a wrapper aroundkillthat sendskill -15 $PID, waits a little, then sendskill -2, waits and sendskill -1, waits before finally sendingkill -9. If I want a program to stop, I want to ask it nicely before getting more aggressive. I use this a few times a month.

waitfor $PIDwaits for a PID to exit before continuing. It also keeps the system from going to sleep. I use this about once a month to do things like:

# I want to start something only after another process finishes

waitfor
1234
 ; something_else

# I started a long-running process and want to know when it's done

waitfor
1234
 ; notify
'process 1234 is done'

bb my_commandis likemy_command &but itreally reallyruns it in the background. You’ll never hear from that program again. It’s useful when you want to start a daemon or long-running process you truly don’t care about. I usebb ollama serveandbb timer 5mmost often. I use this about once a day.

prettypathprints$PATHbut with newlines separating entries, which makes it much easier to read. I use this pretty rarely—mostly just when I’m debugging a$PATHissue, which is unusual—but I’m glad I have it when I do.

tryna my_commandrunsmy_commanduntil it succeeds.trynafail my_commandrunsmy_commanduntil it fails. I don’t use this much, but it’s useful for various things.tryna wget ...will keep trying to download something.trynafail npm testwill stop once my tests start failing.

## Quick references

emojiis my emoji lookup helper. For example,emoji coolprints the following:

😛
😒
😎
🪭
🆒

httpstatusprints all HTTP statuses.httpstatus 204prints204 No Content. As a web developer, I use this a few times a month, instead of looking it up online.

alphabetjust prints the English alphabet in upper and lowercase. I use this surprisingly often (probably about once a month). It literally just prints this:

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

## System management

theme 0changes my whole system to dark mode.theme 1changes it to light mode. It doesn’t just change the OS theme—it also changes my Vim, Tmux, and terminal themes. I use this at least once a day.

sleepybearputs my system to sleep, and works on macOS and Linux. I use this a few times a week.

ds-destroyrecursively deletes all.DS_Storefiles in a directory. I hate that macOS clutters directories with these files! I don’t use this often, but I’m glad I have it when I need it.

## Grab bag

catbin foois basicallycat "$(which foo)". Useful for seeing the source code of a file in your path (used it for writing up this post, for example!). I use this a few times a month.

notifysends an OS notification. It’s used in several of my other scripts (see above). I also do something like this about once a month:

run_some_long_running_process ; notify
'all done'

uuidprints a v4 UUID. I use this about once a month.

## What about your scripts?

These are just scriptsIuse a lot. I hope some of them are useful to you!

If you liked this post, you might like“Why ‘alias’ is my last resort for aliases”and“A decade of dotfiles”.

Oh, andcontact meif you have any scripts you think I’d like.

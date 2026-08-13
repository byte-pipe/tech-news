---
title: A shell exclamation mark is not for yelling. Be lazy. | Filip Roséen - refp.se
url: https://refp.se/articles/your-shell-and-the-lazy-exclamation-mark
site_name: tldr
content_file: tldr-a-shell-exclamation-mark-is-not-for-yelling-be-laz
fetched_at: '2026-08-13T11:41:50.220303'
original_url: https://refp.se/articles/your-shell-and-the-lazy-exclamation-mark
date: '2026-08-13'
published_date: '2026-08-05T22:12:46+02:00'
description: Event designators have been hiding in not-so-plain-sight since the late 1970s — so powerful that forgetting might be part of a massive conspiracy to wear out developer keyboards faster than otherwise.
tags:
- tldr
---

## A shell exclamation mark is not for yelling. Be lazy.

Event designators have been hiding in not-so-plain-sight since the late 1970s — so powerful that forgetting might be part of a massive conspiracy to wear out developer keyboards faster than otherwise.

Published
5 August 2026 at 20:12 UTC
Modified
8 August 2026 at 17:34 UTC
Author
Filip Roséen
Tags
* #shell
* #bash
* #zsh
* #posix
* #unix

## Table of Contents

* Don't yell at your colleagues; yell in your shell
* Command-line repetition we socially accept
* Don't Repeat Yourself.
* What isthis magican event designator?Event DesignatorWord DesignatorModifier
* Event Designator
* Word Designator
* Modifier
* POSIX and the power offc
* Yell responsiblyThe rule of threeThe powerful fourI don't trust my exclamation-mark-fu just yet, any advice?
* The rule of three
* The powerful four
* I don't trust my exclamation-mark-fu just yet, any advice?
* So, what now?
* Frequently Asked QuestionsWhen I usesudo !!, will it be stored unchanged in the shell history?!just gets in the way, how do I turn this off?Can history-ignored commands still be referenced?Why not usectrl-rinstead of memorizing a bunch of things?Why not usealt-.instead of!$?Are you not disregarding other useful features?
* When I usesudo !!, will it be stored unchanged in the shell history?
* !just gets in the way, how do I turn this off?
* Can history-ignored commands still be referenced?
* Why not usectrl-rinstead of memorizing a bunch of things?
* Why not usealt-.instead of!$?
* Are you not disregarding other useful features?
* Further Reading

# Don't yell at your colleagues; yell in your shell#

You and I are probably very different;mychoice of editor is likely to
make you cringe just thinking about it, andyourfavorite programming language
isstatistically— definitely — not mine.

There is however one thing (and maybe that's the only thing) we all have in
common; we are a bunch of lazy bastards.

Note: This article is primarily targetingbash,csh,tcsh, andzsh. If these shells are not your daily driver, seePOSIX and the power offc— worth a read no matter which POSIX-compatible shell you use.

### Command-line repetition we socially accept#

$ 
ssh some-user@10.240.33.109

$ 
echo
 
"done with some-user@10.240.33.109"
 >> ~/work/superfun-client/worklog

$ 
cd
 ~/work/superfun-client && 
cat
 TODO

$ 
ssh some-user@10.240.33.109 
# <- forgot something

I am sure we have all ended up in arrow-up-mashing hell when repeating commands
in our shell history, but what if we instead could save ourselves the trouble
and refer to previous commands and their arguments directly?

$ 
ssh some-user@10.240.33.109

$ 
echo
 
"done with !:1"
 >> ~/work/superfun-client/worklog

$ 
cd
 !$:h && 
cat
 TODO

$ 
!ssh

No yelling — just exclamation marks.

Note: The magic described in this article applies to interactive shells
unless configured otherwise, it isnotmeant to be used in your newamazing.shshell script.

## Don't Repeat Yourself.#

I bet you've heard it before, "do not repeat yourself", either from that
annoying colleague with all the obscure magic (who might smell a little funny) —
or perhaps you said it yourself during the last refactor session that somehow
lasted longer than the federation delay onmatrix.org.

$ 
apt install awesome-package 
# insufficient permissions

$ 
sudo
 !! 
# repeat with sudo

$ 
mkdir
 /var/mnt/cache 
# the usual create directory dance

$ 
cd
 !$ 
# cd to the directory, no finger strain needed

Most of us have heard DRY repeated since we were ki–, I mean junior. But is it
not funny that we've religiously been taught to apply DRY everywhere… except on
the command‑line?

$ 
touch
 ~/projects/work/awesome.sh

$ 
cd
 !$:h 
# cd to the directory of awesome.sh

$ 
ssh 10.240.33.109 -p2222 -i ~/.ssh/prod/ed25519

$ 
ssh 10.240.33.110 !:2* 
# same flags, another host

$ 
ffmpeg -i /recordings/a-sunny-day.mov !#:2:r.mkv

ffmpeg -i /recordings/a-sunny-day.mov /recordings/a-sunny-day.mkv

$ 
scp !$:r.* example.com:/media

scp /recordings/a-sunny-day.* example.com:/media

## What isthis magican event designator?#

Even though they might look mighty daunting at first glance,event
designatorsalways follow the same rather simple pattern:

![event][:word][:modifier]
 | | |
 | | '--> modifier [ :h :t :r :e ... ]
 | '-----------> which part [ :0 :$ :* :2-3 ... ]
 '------------------> which line [ !! !-2 !ssh !?needle? ... ]

Note: Want to know the bare necessities? Check outyell responsiblyfor the essential designators I consider
most useful.

Note: Already fluent? Skip toposix and the power offcfor one of
the most useful albeit niche commands I have ever had the pleasure of
running — who haven't wished they could edit their long commands in an editor
rather than in the shell?

### Event Designator#

The first part immediately following the exclamation mark denotes which lines we
are interested in — here are a few examples which will effectively rerun the
referred to command:

$ 
!! 
# the previous line

$ 
!-2 
# two lines back

$ 
!1337 
# the 1337th line, as displayed by `history`

$ 
!ssh 
# the most recent line starting with "ssh"

$ 
!?dandelion? 
# the most recent line containing "dandelion"

$ 
!# 
# the current line, written so far

$ 
^ssh^scp^ 
# replace first ssh with scp in previous command

Note: If the!is immediately followed by:, no explicit event is
specified and the expression will refer to the immediately previous line.

### Word Designator#

After theevent designator(if any) you may specify which part of the line
you are interested in. All examples below are written as if they follow the
command in the first code block.

$ 
/path/to/script.sh 
"hello world"
 --
enable
 1337

$ 
!:0 
# 1st word --> "/path/to/script.sh"

$ 
!:1 
# 2nd word --> "hello world"

$ 
!:$ 
# last word --> "1337"

$ 
!:1-2 
# 2nd to 3rd --> "hello world" "--enable"

$ 
!:* 
# all args --> "hello world" "--enable" "1337"

$ 
!:1- 
# all but last --> "hello world" "--enable"

$ 
!:2* 
# 3rd to last --> "--enable" "1337"

Note: There are several short-form expressions that work without even
specifying a colon, like!$being equivalent to!:$,!*being equivalent
to!:*, and so forth.

### Modifier#

Modifiers are perhaps where we enter"oh-daaaaaaaym"-territory — they allow
you to extract/modify only certain parts of what would otherwise be an entire
argument.

$ 
!:$:h 
# strip filename (`dirname`)

$ 
!:1:t 
# strip leading path (`basename`)

$ 
!:1:r 
# strip only the extension

$ 
!:1:e 
# leave only the extension

$ 
!:s/hello/bye/ 
# replace first 'hello' with 'bye'

$ 
!:gs/foo/bar/ 
# replace all 'foo' with 'bar'

$ 
!ssh:p 
# print what would run, without running it

## POSIX and the power offc#

Whether or not your shell speaks!,fcbelongs in your imaginary tool belt.
It can be used to repeat the previous command, but the true power lies in the
fact that you can edit your command-line not in your shell — but in your editor
of choice.

Every shell adventurer should runfcat least once a year, if only to marvel
at its usability:

$ 
fc
 
# edit the previous command

$ 
fc
 -2 
# edit the command 2 steps back

$ 
fc
 grep 
# edit last command starting with grep

$ 
fc
 -3 -1 
# the last three commands, all in one buffer

$ 
fc
 ssh -1 
# from the last 'ssh' line through the most recent one

$ 
fc
 -s ssh 
# repeat last command starting with 'ssh'

$ 
fc
 -s hello=world ssh 
# replace "hello" with "world" on the line starting with 'ssh'

fcwill invoke whatever program is specified in$FCEDITto do the editing,
if no such specification exists POSIX falls back toed— though many shells
will default to$EDITOR.

You may also specify which editor to invoke using-e:

$ 
scp api.tar.gz prod-01:/tmp

$ 
ssh prod-01 systemctl restart api

$ 
curl -sf https://prod-01/health

$ 
fc
 -e 
'sed -i s/prod-01/test-01/g'
 -3 -1

The above will rerun all three commands, replacingprod-01withtest-01in
each; a contrived example perhaps but man is it useful when you find yourself in
such trouble.

Note

* fclives in theUser Portability Utilitiesof POSIX.
* Truly minimal shells likedashand busyboxashship without it entirely.

## Yell responsibly#

Event designators, orfcin the case ofPOSIX, are not going to change your
life and turn you into anüber-10x-developer-always-wearing-a-hoodie; they might
however save you anywhere between four and forty-two keystrokes at a time, a few
hundred times a week, over the many years spanning your career.

See below for what I consider the essentials, memorize a few of these and you
are already miles ahead compared to your former self.

* ### The rule of three#!!which expands to the previous command!needlewhich expands to the most recent command starting with"needle"!?needle?matches the most recent command containing"needle"
* !!which expands to the previous command
* !needlewhich expands to the most recent command starting with"needle"
* !?needle?matches the most recent command containing"needle"
* ### The powerful four#!$the last argument of the previous command!:0when you need to rerun that annoyingly located script!$:hfor an easy extraction of the directory part!$:tfor when you want the filename and nothing else
* !$the last argument of the previous command
* !:0when you need to rerun that annoyingly located script
* !$:hfor an easy extraction of the directory part
* !$:tfor when you want the filename and nothing else

### I don't trust my exclamation-mark-fu just yet, any advice?#

There isshopt -s histverifyforbash, andsetopt HIST_VERIFYinzsh.

Rather than YOLO-running the command directly, either configuration will
expand commands in-place when you press enter — allowing you to edit (or
discard) the result if it is not what you aimed for.

You may also use the:p-modifier to print what would run without running it —
the expansion lands in your history so a plain!!(or arrow-up + enter) runs
it once you are ready.

## So, what now?#

I guess there is nothing left to do but practice.

Please refrain from yelling at your colleagues, spend the saved keystrokes on
watercooler chitchat, and forever remember that exclamation marks are not for
shouting — at least not in your shell.

## Frequently Asked Questions#

If you have a question or feedback of your own, please feel free to shoot me an
email atfilip.roseen@atch.se.

* ### When I usesudo !!, will it be stored unchanged in the shell history?#Event-designators themselves do not end up in history, it will be the expanded
contents:$echo"hello world"hello world$echo!$:s/world/idoubtit/echo "hello idoubtit"
hello idoubtit$history1 echo "hello world"
2 echo "hello idoubtit"
3 historyNote: The above is ironically enough quite annoying when writing a post
about event‑designators, as you would often want to reach for
previous pre-interpolation commands.
* ### !just gets in the way, how do I turn this off?#I bet many have been bitten by the "usability" of event designators without
realizing what they are for, such as in the example below:$echo"!dlrow olleh"bash: !dlrow: event not foundIf you would like to turn things off so that you can use!anywhere, you may
useset +Hinbashandsetopt nobanghistinzsh; for other shells I
recommend consulting your manual.You may also go full smelly-colleague-with-magic (please wear deodorant in
public), and instead use any character of your liking:$histchars='%^#'# event-trigger, substitution, comment$echo"hello world"hello world$echo%$:s/world/the internet/hello the internetNote: Remember to put your configuration in the relevant dot-rc file to
make the configuration persistent across sessions.
* ### Can history-ignored commands still be referenced?#Functionality such as leading space to ignore adding things to the history is
not default behavior, but event designators will still be able to capture
their contents.%setoptHIST_IGNORE_SPACE%echo"abc"abc%echo"321"321%echolast-argument-was !$echo last-argument-was "321"
last-argument-was 321%history1 setopt HIST_IGNORE_SPACE
2 echo "abc"
3 echo last-argument-was "321"Note: Notice howecho 321isnotpart ofhistory, but our
(expanded) usage of!$is.
* ### Why not usectrl-rinstead of memorizing a bunch of things?#ctrl-r, a.k.a. command-line history search, is extremely powerful, but it will
at best give you a template to modify;event designatorsallow you to
extract partial contents.Also, why search if you already know what you want to run?!sshvsctrl-r+ssh— the former is also kinda cooler™.
* ### Why not usealt-.instead of!$?#alt-.is great for what it is designed to do, iterating over the previous
"last arguments" of your shell history. It's great at doing that, but it is
also limited to doing just thatonething.
* ### Are you not disregarding other useful features?#I am not aiming for some sort of "either or" situation when I publish my
articles — whatever gets the work done is what you should use.And for what it's worth… never do what a stranger tells you online; personal
preference and workflows are worth more than any article (no matter the amount
of obscure sometimes forgotten magic).

## Further Reading#

Other articles in this series:

* A shell colon does nothing. Use it anyway (refp.se)

Documentation relevant to event designators:

* Event Designators (gnu.org)
* Word Designators (gnu.org)
* Designator Modifiers (gnu.org)

Enjoyed the contents? Please consider supporting me viaPayPalorBuy Me a Coffee.

I also buildpushups.sh— a service where you learn git by pushing to a server that reads your commits and pushes back. The repositories refuse to advance until you get it right, and all you need is git.
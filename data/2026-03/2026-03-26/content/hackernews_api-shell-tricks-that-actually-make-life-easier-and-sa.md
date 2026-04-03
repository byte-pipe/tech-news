---
title: Shell Tricks That Actually Make Life Easier (And Save Your Sanity) | Larvitz Blog
url: https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/
site_name: hackernews_api
content_file: hackernews_api-shell-tricks-that-actually-make-life-easier-and-sa
fetched_at: '2026-03-26T19:28:41.602954'
original_url: https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/
author: zdw
date: '2026-03-26'
published_date: '2026-03-26T00:00:00+01:00'
description: Watch someone backspace 40 characters instead of pressing CTRL+W, and you’ll understand why this list exists. A collection of shell tricks-grouped by what wo...
tags:
- hackernews
- trending
---

There is a distinct, visceral kind of pain in watching an otherwise brilliant engineer hold down the Backspace key for six continuous seconds to fix a typo at the beginning of a line.

We’ve all been there. We learnls,cd, andgrep, and then we sort of… stop. The terminal becomes a place we live in-but we rarely bother to arrange the furniture. We accept that certain tasks take forty keystrokes, completely unaware that the shell authors solved our exact frustration sometime in 1989.

Here are some tricks that aren’t exactly secret, but aren’t always taught either. To keep the peace in our extended Unix family, I’ve split these into two camps: the universal tricks that work on almost anyPOSIX-ish shell (likeshon FreeBSD orkshon OpenBSD), and the quality-of-life additions specific to interactive shells like Bash or Zsh.

## The “Works (Almost) Everywhere” Club

These tricks rely on standard terminal line disciplines, generic Bourne shell behaviors, orPOSIXfeatures. If youSSHinto an embedded router from 2009, a fresh OpenBSD box, or a minimal Alpine container, these will still have your back.

### The Backspace Replacements

Why shuffle character-by-character when you can teleport? These are standard Emacs-style line-editing bindings (via Readline or similar), enabled by default in most modern shells.

CTRL + W: You’re typing/var/log/nginx/but you actually meant/var/log/apache2/. You have two choices: hold down Backspace until your soul leaves your body, or hitCTRL + Wto instantly delete the word before the cursor. Once you get used to this, holding Backspace feels like digging a hole with a spoon.

CTRL + UandCTRL + K: You typed out a beautifully crafted, 80-characterrsynccommand, but suddenly realize you need to check if the destination directory actually exists first. You don’t want to delete it, but you don’t want to run it. HitCTRL + Uto cut everything from the cursor to the beginning of the line. Check your directory, and then hitCTRL + Yto paste (“yank”) your masterpiece right back into the prompt. (CTRL + Kdoes the same thing, but cuts from the cursor to theendof the line.)

CTRL + AandCTRL + E: Jump instantly to the beginning (A) or end (E) of the line. Stop reaching for the Home and End keys; they are miles away from the home row anyway.

ALT + BandALT + F: Move backward (B) or forward (F) one entire word at a time. It’s the arrow key’s much faster, much cooler sibling.(Mac users: you usually have to tweak your terminal settings to use Option as Meta for this to work).

### The “Oh No, Binary Output” Fix

reset(orstty sane): While strictly more of a terminal recovery tip than an interactive shell trick, it belongs here. We’ve all done it: you meant tocata text file, but you accidentallycata compiled binary or a compressed tarball. Suddenly, your terminal is spitting out ancient runes and Wingdings, and your prompt is completely illegible. Instead of closing the terminal window in shame, typereset(even if you can’t see the letters you’re typing) and hit enter. Your terminal will heal itself.

### The Emergency Exits

CTRL + C: Cancel the current command immediately. Your emergency exit when a command hangs, or you realize you’re tailing the wrong log file.

CTRL + D: Sends anEOF(End of File) signal. If you’re typing input to a command that expects it, this closes the stream. But if the command line is empty, it logs you out of the shell completely-be careful where you press it.

### The Screen Cleaner

CTRL + L: Your terminal is cluttered with stack traces, compiler spaghetti, and pure digital noise. Running theclearcommand works, but what if you’re already halfway through typing a new command?CTRL + Lwipes the slate clean, throwing your current prompt right up to the top without interrupting your train of thought.

### The Previous Directory Ping-Pong

cd -: The classic channel-flipper. You’re deep down in/usr/local/etc/postfixand you need to check something in/var/log. You typecd /var/log, look at the logs, and now you want to go back. Instead of typing that long path again, typecd -. It switches you to your previous directory. Run it again, and you’re back in logs. Perfect for toggling back and forth.

pushdandpopd: Ifcd -is a toggle switch,pushdis a stack. Need to juggle multiple directories?pushd /etcchanges to/etcbut saves your previous directory to a hidden stack. When you’re done, typepopdto pop it off the stack and return exactly where you left off.

### The Instant Truncate

> file.txt: This empties a file completely without deleting and recreating it. Why does this matter? It preserves file permissions, ownership, and doesn’t interrupt processes that already have the file open. It’s much cleaner thanecho "" > file.txt(which actually leaves a newline character) orrm file && touch file.

### The “Last Argument” Variable

$_: In most shells,$_expands to the last argument of the previous command-especially useful interactively or in simple scripts when you need to operate on the same long path twice:

mkdir
 
-p
 
/some/ridiculously/long/path/newdir
 
&&
 
cd
 
"
$_
"

No more re-typing paths or declaring temporary variables to enter a directory you created a second ago.

### Scripting Sanity Savers

If you are writing shell scripts, put these at the top immediately after your shebang. It will save you from deploying chaos to production.

* set -e: Exit on error. Very useful, but notoriously weird with edge cases (especially inside conditionals likeifstatements,whileloops, and pipelines). Don’t rely on it blindly as it can create false confidence.(Pro-tip: considerset -euo pipefailfor a more robust safety net, but learn its caveats first.)
* set -u: Treats referencing an unset variable as an error. This protects you from catastrophic disasters likerm -rf /usr/local/${MY_TYPO_VAR}/*accidentally expanding intorm -rf /usr/local/*.

## The Bash&Zsh Comfort Zone

If you’re on a Linux box or using a modern interactive shell, these are the tools that make theCLIfeel less like a rusty bicycle and more like something that actually responds when you steer.

### The History Hunter

CTRL + R: Reverse incremental search. Stop pressing the up arrow forty times to find that oneawkcommand you used last Tuesday. PressCTRL + R, start typing a keyword from the command, and it magically pulls it from your history. PressCTRL + Ragain to cycle backwards through matches.

### The “Oops, Sudo” Move

!!: This expands to the entirety of your previous command. 
Its most famous use case is the “Permission denied” walk of shame. You confidently typesystemctl restart nginx, hit enter, and the system laughs at your lack of privileges. Instead of retyping it, run:

sudo
 
!!

It’s your way of telling the shell, “Do what I said, but this time with authority.”

### The Ultimate Editor Escape Hatch

CTRL + X, thenCTRL + E: You start typing a quick one-liner. Then you add a pipe. Then anawkstatement. Soon, you’re editing a four-line monster inside your prompt and navigation is getting difficult. HitCTRL + Xfollowed byCTRL + E(in Bash; in Zsh, this needs configuring). This drops your current command into your default text editor (like Vim or Nano). You can edit it with all the power of a proper editor, save, and exit. The shell then executes the command instantly.

fc: The highly portable, traditional sibling toCTRL+X CTRL+E. Runningfcopens your previous command in your$EDITOR. It works across most shells and is a fantastic hidden gem for fixing complex, multi-line commands that went wrong.

### The Last Argument (Interactive Edition)

ESC + .(orALT + .): Inserts the last argument of the previous command right at your cursor. Press it repeatedly to cycle further back through your history, dropping the exact filename or parameter you need right into your current command.

!$: The non-interactive sibling ofESC + .. UnlikeESC + .(which inserts the text live at your cursor for you to review or edit),!$expands blindly at the exact moment you hit enter.(Pro-Tip: For scripting or standardsh, use the$_variable mentioned earlier instead!)

### The Renaming Trick&Brace Expansion

Brace expansion is pure magic for avoiding repetitive typing, especially when doing quick backups or renames.

The Backup Expansion:
Need to edit a critical config file and want to make a quick backup first?

cp
 
pf.conf
{
,.bak
}

The shell expands this seamlessly intocp pf.conf pf.conf.bak.

The Rename Trick:

mv
 
filename.
{
txt,md
}

This expands tomv filename.txt filename.md. Fast, elegant, and makes you look like a wizard.

Need multiple directories?mkdir -p project/{src,tests,docs}creates all three at once.

### Process Substitution

<(command): Treats the output of a command as if it were a file. 
Say you want to diff the sorted versions of two files. Traditionally, you’d sort them into temporary files, diff those, and clean up. Process substitution skips the middleman:

diff
 
<
(
sort
 
file1.txt
)
 
<
(
sort
 
file2.txt
)

### The Ultimate Glob

**(Globstar):findis a great command, but sometimes it feels like overkill. If you runshopt -s globstarin Bash (it’s enabled by default in Zsh),**matches files recursively in all subdirectories. 
Need to find all JavaScript files in your current directory and everything beneath it?

ls
 
**/*.js

Nofindcommand required.

### Backgrounding and Disowning

CTRL + Z, thenbg, thendisown:
You started a massive, hour-long database import task, but you forgot to run it intmuxorscreen. It’s tying up your terminal, and if yourSSHconnection drops, the process dies. Panic sets in.

1. HitCTRL + Zto suspend (pause) the process.
2. Typebgto let it resume running in the background. Your prompt is free!
3. Typedisownto detach it from your shell entirely. You can safely close your laptop, grab a coffee, and the process will survive.

### The Everything-Logger

command |& tee file.log: Standard pipes (|) only catch standard output (stdout). If a script throws an error (stderr), it skips the pipe and bleeds directly onto your screen, missing the log file.|&pipesbothstdout and stderr (it’s a helpful shorthand for2>&1 |).

Throw intee, and you get to watch the output on your screen while simultaneously saving it to a log file. It’s the equivalent of watching liveTVwhile recording it to yourDVR.

The shell is a toolbox, not an obstacle course. You don’t need to memorize all of these today. Pick just one trick, force it into your daily habits for a week, and then pick another. Stop letting the terminal push you around, and start rearranging the furniture. It’s your house now.
---
title: how i use my terminal
url: https://jyn.dev/how-i-use-my-terminal/
site_name: hackernews_api
fetched_at: '2025-06-25T01:05:26.853457'
original_url: https://jyn.dev/how-i-use-my-terminal/
author: jyn
date: '2025-06-24'
description: i have gone a little above and beyond trying to get all the features of VSCode
tags:
- hackernews
- trending
---

this is a whole blog post because it is "outside the overton window"; it usually takes at least a video before people even understand the thing i am trying to describe. so, here's the video:

the steps here that tend to surprise people are0:11,0:21, and0:41. when i say "surprise" i don't just mean that people are surprised that i've set this up, but they are surprised this is possible at all.

here's what happens in that video:

1. 0:00I start with Windows Terminal open on my laptop.
2. 0:02I hitctrl + shift + 5, which opens a new terminal tab whichssh's to my home desktop and immediately launches tmux.
3. 0:03tmux launches my default shell,zsh. zsh shows a prompt, while loading the full config asynchronously
4. 0:08i usezoxideto fuzzy find a recent directory
5. 0:09i start typing a ripgrep command. zsh autofills the command since i've typed it before and i accept it withctrl + f.
6. 0:11i hitctrl + kf, which tells tmux to search all output in the scrollback for filenames. the filenames are highlighted in blue.
7. 0:12i holdnto navigate through the files. there are a lot of them, so it takes me a bit to find the one i'm looking for.
8. 0:21i pressoto open the selected file in my default application (nvim). tmux launches it in a new pane. note that this is still runningon the remote server; it is opening a remote file in a remote tmux pane. i do not need to have this codebase cloned locally on my laptop.
9. 0:26i try to navigate to several references using rust-analyzer, which fails because RA doesn't understand the macros in this file. at0:32i finally find one which works and navigate to it.
10. 0:38i hitctrl + kh, which tells tmux to switch focus back to the left pane.
11. 0:39i hitnagain. the pane is still in "copy-mode", so all the files from before are still the focus of the search. they are highlighted again and tmux selects the next file in search order.
12. 0:41i hito, which opens a different file than before, but in thesameinstance ofnvim.
13. 0:43i hitb, which shows my open file buffers. in particular, this shows that the earlier file is still open. i switch back and forth between the two files a couple times before ending the stream.

## but why??

i got annoyed at VSCode a while back for being laggy, especially when the vim plugin was running, and at having lots of keybind conflicts between the editor, vim plugin, terminal, and window management. i tried zed but at the time it was quite immature (and still had the problem of lots of keybind conflicts).

i switched to using nvim in the terminal, but quickly got annoyed at how much time i spent copy-pasting filenames into the editor; in particular i would often copy-paste files with columns from ripgrep, get a syntax error, and then have to edit them before actually opening the file. this was quite annoying. what i wanted was an equivalent of ctrl-click in vscode, where i could take an arbitrary file path and have it open as smoothly as i could navigate to it. so, i started using tmux and built it myself.

people sometimes ask me why i use tmux. this is why! this is the whole reason! (well, this and session persistence.) terminals are stupidly powerful and most of them expose almost none of it to you as the user. i like tmux, despite its age, bugs, and antiquated syntax, because it's very extensible in this way.

## how it works

### search all scrollback for filenames

this is done purely with tmux config:

#
 i am so sorry

#
 see `search-regex.sh` for wtf this means

#
 TODO: include shell variable names

bind-key
 f
copy-mode
 \;
send-keys
 -X search-backward \


'
(^|/|
\<
|[[:space:]"])((
\.
|
\.
\.
)|[[:alnum:]~_"-]*)((/[][[:alnum:]_.#$%&+=@"-]+)+([/ "]|
\.
([][[:alnum:]_.#$%&+=@"-]+(:[0-9]+)?(:[0-9]+)?)|[][[:alnum:]_.#$%&+=@"-]+(:[0-9]+)(:[0-9]+)?)|(/[][[:alnum:]_.#$%&+=@"-]+){2,}([/ "]|
\.
([][[:alnum:]_.#$%&+=@"-]+(:[0-9]+)?(:[0-9]+)?)|[][[:alnum:]_.#$%&+=@"-]+(:[0-9]+)(:[0-9]+)?)?|(
\.
|
\.
\.
)/([][[:alnum:]_.#$%&+=@"-]+(:[0-9]+)?(:[0-9]+)?))
'

and this is the contents ofsearch-regex.sh:

start_delim
=
'
(^|/|\<|[[:space:]"])
'

relative_path
=
'
(\.|\.\.)
'

start_path
=
"
(
$
relative_path
|[[:alnum:]~_
\"
-]*)
"

component
=
'
[][[:alnum:]_.#$%&+=@"-]
'

intermediate_paths
=
"
(/
$
component
+)
"

line_no
=
'
(:[0-9]+)
'

file_end
=
"
(
$
component
+
$
line_no
?
$
line_no
?)
"

end
=
"
([/
\"
]|\.
$
file_end
|
$
component
+
$
line_no
$
line_no
?)
"

echo

"
$
start_delim
$
start_path
(
$
{
intermediate_paths
}
+
$
end
|
$
{
intermediate_paths
}
{2,}
$
end
?|
$
relative_path
/
$
file_end
)
"

#
 test cases omitted for brevity

i will not go through the whole regex, but uh. there you go. i spent more time on this than i probably should have.

### open selected file in a new pane running nvim

this is actually a trick; there are many steps here.

#### open selected file in default application

this part is not so bad. tmux again.

#
 `cd` is important in case this is a relative path. `echo | bash` is to perform tilde expansion.

bind-key
 -T
copy-mode
-vi o
send-keys
 -X copy-pipe \


'
cd #{pane_current_path}; xargs -I {} echo "echo {}" | bash | xargs open
'
 \; \

 if -F
"
#{alternate_on}
"
 {
send-keys
 -X cancel }

i also have a version that always opens an editor in the current pane, instead of launching in the default application. for example i usefxby default to view json files, butnvimto edit them.

#
 save the buffer, then open an editor in the current pane

bind-key
 -T
copy-mode
-vi O
send-keys
 -X copy-pipe-and-cancel \


'
tmux send-keys "C-q"; xargs -I {} tmux send-keys "${EDITOR:-vi} {}"; tmux send-keys "C-m"
'

#### open a new pane running nvim

here is the trick. i have createda shell script(actually a perl script) that is the default application for all text files.

setting up that many file associations by hand is a pain. i will write a separate blog post about the scripts that install my dotfiles onto a system. i don't use Nix partly because all my friends who use Nix haveeven weirderbugs than they already had, and partly because i don't like the philosophy of not being able to install things at runtime. i want to install things at runtime andtrackthat i did so. that's a separate post too.

the relevant part is this:

#
 don't use `` so that args can have embedded pipes

my

@
split

=

(
'
tmux
'
,

'
split-window
'
,

'
-h
'
,

'
-P
'
,

'
-F
'
,

'
"#{pane_id}"
'
,

$
editor
,

@
args
)
;

open
(
my

$
fd
,

'
-|
'
,

@
split
)

||

die

"
can't open pipeline:
$
!
"
;

this bouncesbackto tmux. in particular, this is being very dumb and assuming that tmux is running on the machine where the file is, which happens to be the case here. this is not too bad to ensure - i just use a separate terminalemulatortab for each instance of tmux i care about; for example i will often have open one Windows Terminal tab for WSL on my local laptop, one for my desktop, and one for a remote work machine via a VPN.

there's actually even more going on here—for example i am translating thefile:line:columnsyntax to something vim understands, and overridingxdg-openso that it doesn't error out on the:line—but for the most part it's straightforward and not that interesting.

### open a file in a running instance of nvim

this is a perl script that scripts tmux to send keys to a running instance of nvim (actually the same perl script as before, so that both of these can be bound to the same keybind regardless of whether nvim is already open or not):

my

$
current_window
=

trim

`
tmux display-message -p "#{window_id}"
`
;

my

$
pane

=

trim

`
tmux list-panes -a
\\

 -f '#{&&:#{==:#{window_id},
$
current_window
},#{==:#{pane_current_command},
$
editor
}}'
\\

 -F '#{pane_id}'
`
;

#
 ...

#
 exit copy mode so we don't send these commands directly to tmux

`
tmux send-keys -t
$
pane
 -X cancel 2>/dev/null
`
;

#
 Escape for some reason doesn't get sent as the escape key if it shows up next to any other keys???

`
tmux send-keys -t
$
pane
 Escape
`
;

my

$
args

=

join

'

'
,

@
args
;

my

$
cmd

=

$
editor

eq

'
nvim
'

?

'
drop
'

:

'
open
'
;

`
tmux send-keys -t
$
pane
 ":
$
cmd

$
args
" Enter
`
;

`
tmux select-pane -t
$
pane
 -Z
`
;

## consequences of this setup

* i don't need a fancy terminal locally; something with nice fonts is enough. all the fancy things are done through tmux, which is good because it means they work on Windows too without needing to install a separate terminal.
* the editor thing works even if the editor doesn't support remote scripting. nvimdoessupport RPC, but this setup also worked back when i usedhelixandkakoune.
* icouldhave written this such that the fancy terminal emulator scripts were in my editor, not in tmux (e.g.:terminalin nvim). but again this locks me into the editor; and the built-in terminals in editors are usually not very good.

## ok, but do you really want to use tmux

well. well. now that you mention it. the last thing keeping me on tmux was session persistence andAnsuz has just released a standalone tool that does persistence and nothing else. so. i plan to switch tokittyin the near future, which lets me keep all these scripts and does not require shoving a whole second terminal emulator inside my terminal emulator, which hopefully will reduce the number of weird mysterious bugs i encounter on a regular basis.

the reason i picked kitty overweztermis that ssh integration works by integrating with the shell, not by launching a server process, so it doesn't need to be installed on the remote. this mattered less for tmux because tmux is everywhere, but hardly anywhere has wezterm installed by default.

## ... was it worth it?

honestly, yeah. i spend quite a lot less time fighting my editor these days.

* it'smucheasier to debug when something goes wrong (vscode's debugging tools are mostly for plugin extension authors and running them is non-trivial). with vim plugins i can just addprintstatements to the lua source and see what's happening.
* all my keybinds make sense to me!
* my editor is less laggy.
* my terminal is much easier to script through tmux than through writing a VSCode plugin, which usually involves setting up a whole typescript toolchain and context-switching into a new project

that said, i cannot in good conscience recommend this to anyone else. all my scripts are fragile and will probably break if you look at them wrong, which is not ideal if you haven't written them yourself and don't know where to start debugging them.

## ok but this looks nice i want this

if you do want something similar without writing your own tools, i can recommend:

* fish+zoxide+fzf. that gets you steps 4, 5, and kinda sorta-ish 6.
* "builtin functionality in your editor" - fuzzy find, full text search, tabs and windows, and "open recent file" are all commonly supported.
* qf, which gets you the "select files in terminal output" part of 6, kinda. you have to remember to pipe your output to it though, so it doesn't work after the fact and it doesn't work if your tool is interactive. note that it hard-codes a vi-like CLI (vi +line file.ext), so you may need to fork it or still add a script that takes the place of $EDITOR. seejulia evans' most recent postfor more info.
* e, which gets you the "translatefile:lineinto something your editor recognizes" part of 8, kinda. i had never heard of this tool until i wrote my own with literally the exactly the same name that did literally exactly the same thing, forgot to put it in PATH, and got a suggestion fromcommand-not-foundasking if i wanted to install it, lol.
* vim --remote filenameorcode filenameoremacsclient filename, all of which get you 12, kinda. the problem with this is that they don't all supportfile:line, and it means you have to modify this whenever you switch editors. admittedly most people don't switch editors that often, lol.

## what have we learned?

* terminals are a lot more powerful than people think! by using terminals that let you script them, you can do quite a lot of things.
* you can kinda sorta replicate most of these features without scripting your terminal, as long as you don't mind tying yourself to an editor.
* doing this requires quite a lot of work, because no one who builds these tools thought of these features ahead of time.

hopefully this was interesting! i am always curious what tools people use and how - feel free toemail meabout your own setup :)

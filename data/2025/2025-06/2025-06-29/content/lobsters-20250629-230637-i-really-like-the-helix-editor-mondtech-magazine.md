---
title: I really like the Helix editor. | MOND←TECH MAGAZINE
url: https://herecomesthemoon.net/2025/06/i-like-helix/
site_name: lobsters
fetched_at: '2025-06-29T23:06:37.353618'
original_url: https://herecomesthemoon.net/2025/06/i-like-helix/
author: Mond
date: '2025-06-29'
published_date: '2025-06-28T00:00:00+00:00'
description: This is a website, which means it sometimes goes offline
tags: editors
---

A common depiction of the

Riemann Surface
 of the

Complex Logarithm
.


 Toggle original/dithered image

TheHelix editoris a modal1(read: Vim-like)Kakoune-inspired‘batteries included’
 terminal editor with sane defaults and a focus on multiple cursors and selection-based editing.

There are a lot of reasons to like the Helix editor.

One of my favorite ones is how good it is at handling vaguely structured data (e.g. structured logs, JSON
 output, etc.), outside of the realm of standard LSP-powered code editing. More about that later.

That’s also when I’ll tell you why, yes, that ‘search and replace in file’ popup most modern editors have
 is actually Bad™.

Here’s a demo of me using Helix to process a large JSON file. I’m extracting a list of all locations of
 resources deployed in 2025 with just a few keypresses. It’s not very hard. Pay special attention to theselection counterin the lower right corner.

Your browser does not support the video tag.

 This works by selecting the whole file, and then restricting our selection a few times. I will go
 into more detail later in the post.


One last thing before we get started: I’ll compare Helix to Vim in the following, but don’t make the
 mistake of assuming that I’d be happier with e.g. VSCode. Many of my reasons for disliking VSCode are
 pretty similar to my reasons for disliking Vim, and this includes theissues with highly context-specific and hard to learn keybinds.

## Getting the obvious one out of the way: It just works.

Everything just works out of the box. It’s a pretty massive difference from the world of Vim, where a
 significant investment to figure out how to customize your editor to your liking is required.

A barebones Neovim install neither has Treesitter set up nor manages to connect to my installed LSPs! Not
 without first dealing with someconfig fiddling and plugin setup,
 anyway.

(If you’re not familiar with LSPs, basically all semantics-aware features of (most) modern IDEs are
 handled by the Language Server Protocol (LSP). This includes ‘red squiggles’ beneath errors, renaming
 variables, jumping to definitions, autocompletion, and so on. What this basically means is that as long as
 your editor supports LSPs, it can doall of the same stuff VSCode does. This makes switching
 between modern editors pretty painless, as far as capabilities go. Most of them use the same LSPs!)

In Helix, if I press a button such asg(which still corresponds togoto, just
 like in Vim), it will automatically pop up a list of available options for me. If I pressspace(which corresponds to a bunch of ‘higher level’ operations or interactions with
 specific tools), the same happens. See for yourself:

 Everything within reach and easily accessible.

 Toggle original/dithered image

I cannot overstate how big of a deal this feature is. Discoverability is a big deal. If your users don’t
 know that a feature exists, they won’t use it. If they don’t even know how to easily figure outwhethera feature they’re looking for exists, it’s basically game over.

There’s a few more examples of easy usability.[and]work as in Vim-unimpaired, and allow you to jump to the previous/next function, test, diagnostic, paragraph, change, etc.

Likewise,mallows manipulation of ‘surrounding’ characters or syntactic structures. This
 includes jumping between pairs of brackets, selecting a string literal, test, or function, diff, etc.

This is nice! Treesitter is nice. I don’t know how easy it is to delete a function or testcase in your
 editor of choice, but there’s something nice about the fact that I can just typemafto
 select an entire function, and then delete it with a single button press. (And, most importantly, that the
 same principle extends to everything else.)

What else?

The fuzzy pickers are great. I can type<space>?and get a fuzzy picker that shows all
 available editor commands or<space>Sto get a fuzzy finder over all symbols (e.g.
 function names) across the entire repository, and then immediately jump to them.

All of the pickers work in the same unified way, even! It’s likeNvim’s Telescope, except
 there’s no need to scroll through a Github page through multiple dependency sections, an install section
 with four different options (depending on which plugin manager you’re using), and a long list of commands
 that you first need to map to your own personal keybinds.

You probably losesomecustomizability, but “I have a deep, intense need to customize the way my
 fuzzy finder editor plugin integrates into my bespoke coding workflow and external dependencies.” falls
 firmly into the category of “Sentences spoken by the utterly deranged” for me.

Anyway, just in case you’re getting worried we’re losing the fundamentals, all of the ‘standard’ Vim
 features are supported. The keybinds are somewhat different, but similar enough that picking it up and
 being productive didn’t take very long.

I was productive in ~2 hours, and have been using it as my daily driver for over a year by now.

I can record macros and replay them. I can type|to pipe each of my selections into a shell
 command and replace them with the output. I can yank to registers, paste, search for regex patterns, split
 and tile my screen, jump around in various ways, etc.

### Customizability

Don’t get me wrong, Vim’s customizability and plugin system are one of its biggest strengths.

This is why Vim is capable of handlingJupyter Notebooks, which isnotsomething you can say about Helix (for now).

That doesn’t change the equation, though: Requiring everyone to do their own bespoke setup and config
 fiddling isn’t great. That’s a lot of time people have to put into it just for some basic functionality,
 and in the endeveryonewill end up with something slightly different.


xkcd 1172.


 Toggle original/dithered image

Anyway. I acknowledge that “Helix is basically like Vim, except everything works out of the box, and you
 don’t have to deal with 30 year old historical baggage.” isn’t much of a selling point for people who’ve
 already spent hours setting up an entire dependency chain of Vim plugins on their computer.

That’s fine by me. As for myself, I’m tired of shaving that particular yak. I want something that “just
 works”andhas a composable modal interface.

I much prefer to shave other, slightly less hairy yaks. Preferably ones that are marginally closer to the
 projects I’m actually interested in working on, y’see.

Anyway.

Before we get into the whole selection-based editing part (aka ‘stuff that makes Helix unique and is
 cool’), here’s my entire Helix config:

theme =
"onedark"

[editor]

auto-save =
true

cursorline =
true

gutters = [
"diagnostics"
,
"line-numbers"
]

line-number =
"relative"

[editor.cursor-shape]

insert =
"bar"

normal =
"block"

select =
"underline"

[editor.file-picker]

hidden =
true

[editor.soft-wrap]

enable =
true

[keys.normal]

C-j =
"half_page_down"

C-k =
"half_page_up"

Please take note of how short it is. This is what I used when writing this very post.2

Meanwhile, in the world of Vim you findGithub repositoriesthat
 self-describe as ‘minimal neovim configuration’ and contain over a dozen files of Lua and a few hundred
 lines of code full of side effects.

Needless to say, I’m not much of a fan of fancy ‘Vim-with-batteries-included’ setups likeLunarVimeither.

LunarVim essentially stacks a ton of plugins on top of Neovim to make it look like VSCode. I’ve never been
 a fan, honestly. When I used Neovim, even a moderate amount of plugin resulted in some performance issues,
 whereas Helix just feels a lotsnappier, and less brittle.

If you’re into this, more power to you. It’s just not for me.

## Selection-based Editing

What Ireallylike about Helix is its ability to manipulate to easily manipulate multiple
 selections and cursors. It gives you a few basic, very powerful tools, which I reach forsurprisingly often, just because of how versatile they are.

You’ve already seen me use multi-cursor editing in the demo video at the start of the post. I’ll go into
 more detail in this section.

### Replacing Text

When writingcode, using the Language Server to ‘rename a variable’ is pretty easily the best
 workflow there is. It will query all of the usages, and just rename them. It will even return an error if
 you run into name collision issues.

When that doesn’t work for whatever reason, you’re usually forced to reach for second-class tools such as
 Vim’s terrible:%s/foo/bar/gworkflow or the standard GUI search-and-replacepopup window(which is also terrible).

If it’s not clear why the search-and-replace popup window is bad, it’s because it’s “glued onto” the main
 editor, and poorly interacts with the rest of the program.

1. It generally hashighly specific, hard to learn keybinds.that you need to learn if you’d like to leverage it to do utterly fundamental stuff.
2. It results in the existence of ’editor focus’. Your editor will either be focused on the popup window or
 on the main input window, both of which have their own keybinds and behavior. Even switching this focus
 probably requires its own keybind, separate from alt-tabbing.

It’s just so much more fiddly and complex than it has any right to be.Editing text should leverage the main editor window and input methods, not have its own bespoke
 interface. This is the GUI equivalent of a bespoke DSL that doesn’t compose with anything else.

In Helix, what you would instead do is the following:

1. Press%. This selects the entire file.
2. Presss. This opens a ‘select’ input field in the command bar.
3. Typefoo. This will narrow down your current selection to only select all matches offoo. In other words, you now have every match offooin your file selected.
4. Typec. This replaces each selection with a cursor, and puts you into insert mode.
5. Typebar. You’re editing all instances at the same time.

And you’re done. The reason why this is so powerful is that itcomposes. Instead of having to
 find a single regex which matcheseveryinstance of your string (or having to write a macro), you
 can narrow it down using repeated applications ofsor other selection-primitives.

Other selection-primitives include (for example)K(for keeping only those selections that
 include a given pattern) orAlt+Kfor removing those that contain a given pattern,xfor selecting an entire line,_for trimming whitespace and the whole
 selection ofmkeybinds for selecting quotes or braces.

This gets fancier with Treesitter features: Take some arbitrary Rust file. Press%, thens, then type^fn, and you selected thefnkeyword in every
 top-level function. Now pressAlt+o, to extend the selection to the surrounding syntactic
 element, i.e. the entire function.

This is stuff you can do. It’s easy. It might sound like a fancy gimmick—and that’s because it is—but that
 doesn’t keep it from being composable and easy.

### Handling semi-structured logs

Perhaps my first real ‘programming project’ was a Discord bot, written in Python and usingDiscordpy. It’s still running to this day,
 and had an uptime of a full year before I decided to update it not too long ago.

Iamproud of it, but it’s by no means an example of excellent engineering practices.

My Discord bot spits out logs that look something like this here:

.

.

.

01
/
06
/
2025
,
10
:
38
:
38

:
 ERROR
:

'NoneType'
 object has no attribute
'remove_roles'

Traceback
(
most recent call last
):

 File
"/bot/admintools.py"
, line
133
, in roles_loop

 await member.remove_roles
(
role, reason=
"Bot removed."
)


^^^^^^^^^^^^^^^^^^^

AttributeError
:

'NoneType'
 object has no attribute
'remove_roles'

05
/
06
/
2025
,
16
:
17
:
03

:
 ERROR
:
 on_command_error
:
 Command
"foo"
 is not found
:

!
foo bar

NoneType
:
 None

05
/
06
/
2025
,
18
:
54
:
49

:
 INFO
:
 discord.gateway
:
 Shard ID None has successfully RESUMED session
12345
.

05
/
06
/
2025
,
18
:
56
:
08

:
 INFO
:
 discord.gateway
:
 Shard ID None has successfully RESUMED session
12345
.

05
/
06
/
2025
,
19
:
17
:
55

:
 ERROR
:
 discord.client
:
 Ignoring exception in on_message

Traceback
(
most recent call last
):

 File
"/usr/local/lib/python3.13/site-packages/discord/client.py"
, line
481
, in _run_event

 await coro
(*
args,
**
kwargs
)

 File
"/bot/fixer.py"
, line
53
, in on_message

 await fixed.remove_reaction
(
DELETE, msg.guild.get_member
(
self.bot.user.id
))

 File
"/usr/local/lib/python3.13/site-packages/discord/message.py"
, line
1604
, in remove_reaction

 await self._state.http.remove_own_reaction
(
self.channel.id, self.id, emoji
)

 File
"/usr/local/lib/python3.13/site-packages/discord/http.py"
, line
758
, in request

 raise NotFound
(
response, data
)

discord.errors.NotFound
:

404
 Not Found
(
error code
:

10008
):
 Unknown Message

.

.

.

Wow, that sure looks like ass. I sure wish there were a way tostructurally editand inspect this
 file. Something that would make it easy to figure out what’s going on without having scroll through the
 thing carefully looking for whatever entry I might be looking for.

Enter Helix.

1. Select the whole file, then useAlt+sto split my selection into lines. I now have selected
 each line individually.
2. PressAlt+K, and then^\dto only keep those lines thatdo notstart
 with a number.
3. Pressdto delete all of them. Now all of the traceback lines are gone. (I might need them
 later, but for now I’m just considering them noise.)

Using a similar approach, I can delete all lines that only contain anINFOlog, and all logs
 that are too old, or those that don’t contain certain keywords that I am looking for, etc.

I arrive at a very slim, trimmed down log file that only contains the information I need. It takes me a
 few seconds, and is not hard to learn. I already told you all of the keybinds.

I’ve not seen a single tool that makes processing semi-structured datathiseasy. It’s laughably
 flexible.

### Curl, JSON, Config files…

Imagine you’re calling some sort of API and ask it to list all of yourWidgets. You might be
 usingcurl, and just want to quickly figure something out here.

Say, you’re interested in figuring out all the locations in which you’ve got widgets deployed.

For the sake of the argument and considering the absolute state of modern software development, let’s
 assume there’s no easier way of doing this. In fact, the web portal associated with the API is a dumpster
 fire and would require you to scroll through a few dozen pages of widgets and count manually.

The widget schema might be something like this here, and your curl call will spit out a whole list of
 objects in this format.

{


"name"
:
string
,


"displayName"
:
string
,


"description"
:
string
,


"location"
:
string
,


"createTime"
:
string
,


"updateTime"
:
string
,


"labels"
: {


string:

string,


...

 },


...

}

At this point youcouldreach forawkorjqand similar JSON
 manipulation tools, and use that to extract the information you need.People have been doing that for a long time, after all.

Oryou could pipe yourcurlcall directly into Helix.

At that point it’s simple, and doesn’t require learning a bespoke DSL.

That’show you end up at the demo from the intro. That’s a workflow of a few seconds which allows
 me to pick any arbitrary sub-value out of the list, restrict the selection in basic ways (e.g. by
 location, tag or creation time), and get exactly what I want out of it.

Does this sound complicated? It isn’t.

It’s all the same three or four keybinds + the basic Vim ones.

It’sdefinitelyfaster than figuring out how to usejqagain, or writing a Python
 script to process this data.3

### Handling Code

Handling unstructed data like that is pretty neat. Of course, you can do the same when handling code.

Nowadays most programming languages that people actually use have LSPs, meaning that fancy selection-based
 editing to e.g. rename functions is not all that useful.

I still get some mileage out of it. Here are some tricks I like to use now and then:

* Easily extract a list of all function signatures from a file.
* Sort a list of constants, or edit them all at once.
* Count the number of elements in a list by splitting the selection such that each element is selected
 individually. Helix shows the number of selections at the bottom of the screen.
* Replace all usages of some deprecated functionfoowithbetterFooat the same
 time.
* Add a debug-print statement that prints"{FUNCTION_NAME} entered!"for every single
 function in your file at the same time.
* Select and extract all// TODOcomments in your code. Maybe aggregate them in a new
 document.
* Trivially align/format all arms in a match statement or table using&. (Up to you when
 this is a good option over using a formatter.)

Even if none of this is particularly interesting, at its worst Helix is still “Vim, except no config or
 plugin shuffling required, and with better defaults, and where making large scale search-and-replace edits
 doesn’t require dealing with minor bespoke interfaces tacked onto the editor.”.

And that is, imo, a pretty good deal already.

## Caveats

There’s a few caveats.

Most of these are pretty harmless, and pretty deep in the “You’ll know if they apply to you.” territory.
 For example:

* Do you frequently use machines on which you do not have blanket install rights? Tough luck, as far as
 Linux servers go, Vim is basicallyeverywhere. Helix isn’t. If you can’tinstallHelix
 where you work, it’s probably not the editor you should invest time into!
* Are you married to your existing Vim keybinds? Does the thought of having to relearn a few old coding
 habits pain you? Helix gets rid of keybinds such asddorD.ddin favor ofxd, wherexselects the whole line, whileddeletes whatever you have selected right now. This follows the ‘selection first’
 principle. First you select something,thenyou apply some action. There’s a lot of more
 obscure ones that don’t work either.
* Are you working with highly specific languages or software? Preferably the type that requires a
 specialized editor, e.g. Jupyter notebooks or LaTeX. Youcanmake these work in Vim. The Vim
 plugin system is pretty extensive. With Helix you’ll be out of luck.
* Does the thought of interacting with the terminal scare you, or are you fully comfortable using VSCode
 or Eclipse or whatever else there is? Well, Helix might not be for you.Zedis apparently working in addingHelix-support, so that might be
 an option.

As a final point: If you have tried to ‘get into Vim’, but never managed to, thenHelix might be for you.

The same applies if you’re just curious about modal editors, and just never got around to using one. Helix
 is easy, and about as user friendly as it gets. Just install it and enter:tutorto get
 started.

## What’s missing?

 Cherish the editor.

 Toggle original/dithered image

I was considering to break this up into a separate article, but it doesn’t really make sense. Most of my
 thoughts here are just nitpicks.

But let’s quickly go over them, and talk about what’s missing, or what I didn’t manage to fit into the
 article so far.

### The Plugin System

If you’ve read the entire article up to this point it might surprise you to hear this, but the Helix
 developers areworking on a plugin systemfor Helix.

This has been in the workfor a whileand
 remains the most controversial topic in the community.

Wait, you don’t even know the funniest part yet!

The language of choice for writing plugins is planned to beScheme. Or rather,Steelan embeddable Scheme-dialect.
 ConsideringVim’s history with Emacs, andEmacs language of choice, there’s
 something poetic about this. I know some people would prefer Lua, Rust, or even Javascript, but frankly,
 I’m quite happy with Scheme.

It has some real THESIS / ANTITHESIS / SYNTHESIS energy, if you get what I am saying.

It might surprise you to hear that I’m looking forward to this. I don’t dislike plugin-systems per se, and
 am excited to see how this is going to play out. Considering Helix’s solid foundation, I’m not sure if
 I’ll use any of them, but we’ll see.

As far as I know making the plugin system happen required a rewrite of huge parts of the editor, and it’s
 all still awork in progress.We’re seeing the first prototype plugins now. I wish Matthew the best of luck, and I can’t wait to give it a go once it’s ready.

### Nitpicks + Wishes

Here we go:

* There are performance issues with handling really,reallylong lines upwards of 100_000
 characters in a single line. (Don’t ask me what sort of cursed stuff I was doing that I ran into this.)
* Entering view mode glues the main cursor to the viewport. This one is absolutely baffling to me. When I
 select say, 20 occurences of text throughout the entire file and start scrolling around, then the ‘main’
 selection will ‘move around’ to stay inside of the window. This predictably leads to it being in the
 completely wrong place and to dropping the original selection. This one doesn’t make sense to me
 whatsoever.
* AI-based Code Completion isn’t supported yet.There’s a fork that supports it, but
 I’ve got no reason to switch for some slightly fancier autocomplete features. I can’t blame the Helix
 people for putting this off. If I were in their position I’d either wait until there’s a standard
 protocol (like LSPs) or get the plugin system ready, such that people can build their own support for
 it.
* The interaction between the LSP and multi-cursors is not ideal. For example, if I have multiple cursors
 and ask for an LSP code transformation (such as inlining a function), it will only be applied at a
 single cursor. It makes sense why this is: There’s no guarantee we could get the same transformation at
 every single cursor, since there’s no guarantee that they’ll even all point at viable functions. That
 said, it’d be neat if there weresomeway to improve on this and say “Try to apply this at
 every cursor.” Trying to work around this using macros doesn’t quite seem to work either.

Finally, here’s a big one.

This one is less of a nitpick and more of a personal pipedream, though.

What I’dreallylike to see from Helix is the ability to have multi-cursors across multiple
 files.

Manipulation within a single file is all nice and good, but it doesn’t get you all that far. I’d get a
 real productivity boost out of the ability to selectallusages of a function across my entire
 workspace, and to edit all of my selections at the same time.

I’ve already made the case above: ‘Search and replace’ is one of the fundamental operations of editing. It
 shouldnotbe a tacked-on menu. It should compose with the main editor operations.

I don’t see how we could possibly get there, other than by allowing selections across multiple files, and
 having reasonable abstractions on top of them.

We already have multi-cursors, why not take it even further? Let me create and handle all cursors across
 some arbitrary number of buffers at the same time. Give me the ability to selectallcode, acrossallof my files, etc.

This is probably insane.

I’d still love to see it happen and, yes, believe that I’d get legitimate use out of this for reasonably
 large-scale migrations and code transformations.

Someday, maybe.

1. Quick explanation: In most editors you’re in ‘insert mode’ all the time. When you pressx, your cursor will insert the letterx. Modal editors also support
 different modes. For example, in Vim pressingxwill delete the character your cursor is
 currently pointing at, and in Helix pressingxwill select the entire line. This allows
 you to use a lot of fun keys to jump around, select, and edit text very easily.↩︎
2. For the record, I’m pretty impressed by the fact that I get nested syntax highlighting / treesitter
 actions for.tomlinside of this.mdfile. It just works.↩︎
3. Is this still true in the age of LLMs? Eh, maybe not. LLMs are pretty good at crafting fancy throwaway
 terminal commands.↩︎

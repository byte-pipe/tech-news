---
title: 'Vim 9.2 released : vim online'
url: https://www.vim.org/vim-9.2-released.php
site_name: hnrss
content_file: hnrss-vim-92-released-vim-online
fetched_at: '2026-02-14T19:11:09.588185'
original_url: https://www.vim.org/vim-9.2-released.php
date: '2026-02-14'
description: Vim 9.2 Released
tags:
- hackernews
- hnrss
---

# Vim 9.2 is available

The Vim project is happy to announce that Vim 9.2 has been released.

Vim 9.2 brings significant enhancements to the Vim9 scripting language, improved diff mode, comprehensive completion features, and platform-specific improvements including experimental Wayland support.

## New Features in Vim 9.2

* Comprehensive Completion:Added support forfuzzy matchingduring insert-mode completion and the ability to complete words directly fromregisters(CTRL-X CTRL-R). New'completeopt'flags likenosortandnearestoffer finer control over how matches are displayed and ordered.
* Modern Platform Support:Full support for theWaylandUI and clipboard has been added. On Linux and Unix-like systems, Vim now adheres to theXDG Base Directory Specification, using$HOME/.config/vimfor user configuration.
* UI Enhancements:A newvertical tabpanelprovides an alternative to the horizontal tabline. TheMS-WindowsGUI now supports native dark mode for the menu and title bars, along with improved fullscreen support and higher-quality toolbar icons.
* Interactive Learning:A new built-ininteractive tutor plugin(started via:Tutor) provides a modernized learning experience beyond the traditional vimtutor.

## Vim9 Script Evolution

Significant language enhancements including native support forEnums,Generic functions, and theTupledata type. Built-in functions are now integrated asobject methods, and classes now support protected_new()methods and:defcompilefor full method compilation.

## Vim9 Script Ecosystem & AI Integration

The maturity of Vim9 script's modern constructs is now being leveraged by advanced AI development tools. Contributor Yegappan Lakshmanan recently demonstrated the efficacy of these new features through two projects generated using GitHub Copilot:

* Battleship in Vim9:A complete implementation of the classic game, showcasing classes and type aliases. [GitHub]
* Number Puzzle:A logic game demonstrating the efficiency of modern Vim9 for interactive plugins. [GitHub]

## Diff Improvements

Vim 9.2 introduces significant enhancements to how changes are visualized and aligned in diff mode:

* Linematch Algorithm:Includes the "linematch" algorithm for the'diffopt'setting. This aligns changes between buffers on similar lines, greatly improving diff highlighting accuracy.
* Diff Anchors:The new'diffanchors'option allows you to specify anchor points (comma-separated addresses) to split and independently diff buffer sections, ensuring better alignment in complex files.
* Inline Highlighting:Improves highlighting for changes within a line. This is configurable via the"inline"sub-option for'diffopt'. Note that"inline:simple"has been added to the default'diffopt'value.

 Here are some examples for the improved inline highlighting:


inline:simple (old behavior)

inline:char

inline:word

## Changed Default Values

Several long-standing defaults have been updated to better suit modern hardware and workflows. These values have been removed fromdefaults.vimas they are now the internal defaults.

Option

Old Default

New Default (9.2)

'history'

50

200
 (More undo/command history saved)

'backspace'

"" (empty)

"indent,eol,start"
 (Normal backspace behavior)

'diffopt'

"internal,filler"

"internal,filler,closeoff,indent-heuristic,inline:char"

'fontsize'
 (GTK)

10pt

12pt
 (Optimized for High-DPI monitors)

'showcmd'

Off (Unix)

On
 (Always visible in non-compatible mode)

'ruler'

Off

On
 (Shows cursor position by default)

## Completion Feature Examples

These examples demonstrate how to use the powerful new completion and introspection tools available in Vim 9.2.

### 1. Auto-completion

Vim's standard completion frequently checks for user input while searching for new matches. It is responsive irrespective of file size. This makes it well-suited for smooth auto-completion.

Copy Code

vim9script
def InsComplete()
 if getcharstr(1) == '' && getline('.')->strpart(0, col('.') - 1) =~ '\k$'
 SkipTextChangedIEvent()
 feedkeys("\<c-n>", "n")
 endif
enddef

def SkipTextChangedIEvent(): string
 # Suppress next event caused by <c-e> (or <c-n> when no matches found)
 set eventignore+=TextChangedI
 timer_start(1, (_) => {
 set eventignore-=TextChangedI
 })
 return ''
enddef

set cot=menuone,popup,noselect inf

autocmd TextChangedI * InsComplete()

inoremap <silent> <c-e> <c-r>=<SID>SkipTextChangedIEvent()<cr><c-e>

### 2. Live grep, fuzzy find file, fuzzy find buffer

Copy Code

vim9script

var selected_match = null_string
var allfiles: list<string>

def GrepComplete(arglead: string, cmdline: string, cursorpos: number): list<any>
 return arglead->len() > 1 ? systemlist($'grep -REIHns "{arglead}"' ..
 ' --exclude-dir=.git --exclude=".*" --exclude="tags" --exclude="*.swp"') : []
enddef

def VisitFile()
 if (selected_match != null_string)
 var qfitem = getqflist({lines: [selected_match]}).items[0]
 if qfitem->has_key('bufnr') && qfitem.lnum > 0
 var pos = qfitem.vcol > 0 ? 'setcharpos' : 'setpos'
 exec $':b +call\ {pos}(".",\ [0,\ {qfitem.lnum},\ {qfitem.col},\ 0]) {qfitem.bufnr}'
 setbufvar(qfitem.bufnr, '&buflisted', 1)
 endif
 endif
enddef

def FuzzyFind(arglead: string, _: string, _: number): list<string>
 if allfiles == null_list
 allfiles = systemlist($'find {get(g:, "fzfind_root", ".")} \!
 \( -path "*/.git" -prune -o -name "*.swp" \) -type f -follow')
 endif
 return arglead == '' ? allfiles : allfiles->matchfuzzy(arglead)
enddef

def FuzzyBuffer(arglead: string, _: string, _: number): list<string>
 var bufs = execute('buffers', 'silent!')->split("\n")
 var altbuf = bufs->indexof((_, v) => v =~ '^\s*\d\+\s\+#')
 if altbuf != -1
 [bufs[0], bufs[altbuf]] = [bufs[altbuf], bufs[0]]
 endif
 return arglead == '' ? bufs : bufs->matchfuzzy(arglead)
enddef

def SelectItem()
 selected_match = ''
 if getcmdline() =~ '^\s*\%(Grep\|Find\|Buffer\)\s'
 var info = cmdcomplete_info()
 if info != {} && info.pum_visible && !info.matches->empty()
 selected_match = info.selected != -1 ? info.matches[info.selected] : info.matches[0]
 setcmdline(info.cmdline_orig) # Preserve search pattern in history
 endif
 endif
enddef

command! -nargs=+ -complete=customlist,GrepComplete Grep VisitFile()
command! -nargs=* -complete=customlist,FuzzyBuffer Buffer exe 'b ' .. selected_match->matchstr('\d\+')
command! -nargs=* -complete=customlist,FuzzyFind Find exe !empty(selected_match) ? $'e {selected_match}' : ''

nnoremap <leader>g :Grep<space>
nnoremap <leader>G :Grep <c-r>=expand("<cword>")<cr>

nnoremap <leader><space> :<c-r>=execute('let fzfind_root="."')\|''<cr>Find<space><c-@>
nnoremap <leader>fv :<c-r>=execute('let fzfind_root="$HOME/.vim"')\|''<cr>Find<space><c-@>
nnoremap <leader>fV :<c-r>=execute('let fzfind_root="$VIMRUNTIME"')\|''<cr>Find<space><c-@>
nnoremap <leader><bs> :Buffer <c-@>

autocmd CmdlineEnter : allfiles = null_list
autocmd CmdlineLeavePre : SelectItem()

### 3. Auto Completion

Copy Code

vim9script

def CmdComplete()
 var [cmdline, curpos] = [getcmdline(), getcmdpos()]
 if getchar(1, {number: true}) == 0 # Typehead is empty
 && !pumvisible() && curpos == cmdline->len() + 1
 && cmdline =~ '\%(\w\|[*/:.-]\)$' && cmdline !~ '^\d\+$'
 feedkeys("\<C-@>", "ti")
 SkipCmdlineChanged()
 timer_start(0, (_) => getcmdline()->substitute('\%x00', '', 'g')->setcmdline())
 endif
enddef

def SkipCmdlineChanged(key = ''): string
 set ei+=CmdlineChanged
 timer_start(0, (_) => execute('set ei-=CmdlineChanged'))
 return key != '' ? ((pumvisible() ? "\<c-e>" : '') .. key) : ''
enddef

set wim=noselect:lastused,full wop=pum wcm=<C-@> wmnu

autocmd CmdlineChanged : CmdComplete()
autocmd CmdlineEnter : set bo+=error
autocmd CmdlineLeave : set bo-=error

cnoremap <expr> <up> SkipCmdlineChanged("\<up>")
cnoremap <expr> <down> SkipCmdlineChanged("\<down>")

### Optional: Autocompletion (Popup Menu)

For automatic popup menu completion as you type in search or:commands, include this in your.vimrc:

Copy Code

vim9script
def CmdComplete()
 var [cmdline, curpos, cmdmode] = [getcmdline(), getcmdpos(), expand('<afile>') == ':']
 var trigger_char = '\%(\w\|[*/:.-]\)$'
 var not_trigger_char = '^\%(\d\|,\|+\|-\)\+$'
 if getchar(1, {number: true}) == 0
 && !wildmenumode() && curpos == cmdline->len() + 1
 && (!cmdmode || (cmdline =~ trigger_char && cmdline !~ not_trigger_char))
 SkipCmdlineChanged()
 feedkeys("\<C-@>", "t")
 timer_start(0, (_) => getcmdline()->substitute('\%x00', '', 'ge')->setcmdline())
 endif
enddef

def SkipCmdlineChanged(key = ''): string
 set ei+=CmdlineChanged
 timer_start(0, (_) => execute('set ei-=CmdlineChanged'))
 return key == '' ? '' : ((wildmenumode() ? "\<C-E>" : '') .. key)
enddef

set wim=noselect:lastused,full wop=pum wcm=<C-@> wmnu

autocmd CmdlineChanged :,/,? CmdComplete()

# Optional: Preserve history recall behavior
cnoremap <expr> <Up> SkipCmdlineChanged("\<Up>")
cnoremap <expr> <Down> SkipCmdlineChanged("\<Down>")

# Optional: Customize popup height
autocmd CmdlineEnter : set bo+=error | exec $'set ph={max([10, winheight(0) - 4])}'
autocmd CmdlineEnter /,? set bo+=error ph=8
autocmd CmdlineLeave :,/,? set bo-=error ph&

## Other Improvements and Changes

Many bugs have been fixed since the release of Vim 9.1, including security vulnerabilities, memory leaks and potential crashes.

* See the helpfile for other improvements::h new-other-9.2
* Changes to existing behaviour is documented at::h changed-9.2
* A few new functions, autocommands, ex commands and options have been added::h added-9.2
* The full list of patches is documented at::h patches-9.2

## Charity: Transition to Kuwasha

For over 30 years, Vim has been "Charityware," supporting children in Kibaale, Uganda. Following the passing of Bram Moolenaar, the ICCF Holland foundation was dissolved, and its mission has been carried forward by a new partner.

* ICCF Holland Dissolution:Because the charity could not be sustained in its original form without Bram, ICCF Holland was dissolved and its remaining funds were transferred to ensure continued support for the Kibaale project.
* Partnership with Kuwasha:To ensure that aid remained uninterrupted, all sponsorship activities were moved toKuwasha, a long-term partner based in Canada that now manages the projects in Uganda.
* Continuing the Legacy:Vim remains Charityware. We encourage users to continue supporting the needy children in Uganda through this new transition.

For information on how to support this cause, please visit theSponsor page.

## Appreciation

We would like to thank everybody who contributed to the project through patches, translations, and bug reports. We are very grateful for any support.

## Download

You can find the new release on theDownload page.

February 14th, 2026

 Questions about
Vim
 should go
 to the
maillist
.

Help Uganda
.


	 
	 



Vim at Github

---
title: A shell exclamation mark is not for yelling. Be lazy. | Filip Roséen - refp.se
url: https://refp.se/articles/your-shell-and-the-lazy-exclamation-mark
date: 2026-08-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:42:30.887553
---

# A shell exclamation mark is not for yelling. Be lazy. | Filip Roséen - refp.se

# A shell exclamation mark is not for yelling. Be lazy.

## Don't yell at your colleagues; yell in your shell
- The author points out that developers share a common laziness and can save keystrokes with shell shortcuts.  
- The article mainly targets **bash**, **csh**, **tcsh**, and **zsh**; POSIX‑compatible shells are also covered.

## Command‑line repetition we socially accept
- Typical workflow: press ↑ repeatedly to reuse previous commands.  
- Using event designators (`!`) lets you reference earlier commands and their arguments directly, e.g. `!$:h`, `!ssh`, without leaving the prompt.

## Don't Repeat Yourself.
- Demonstrates practical shortcuts:  
  - `!!` – repeat the previous command.  
  - `sudo !!` – run the previous command with sudo.  
  - `!$` – last argument of the previous command (e.g., `cd !$`).  
  - `!$:h` – directory part of the last argument.  
  - `!:2*` – reuse a range of arguments.  
  - `!:1-` – all arguments except the last.  
  - `!#:2*` – edit parts of the current line.  
- Shows how to reuse flags, rename files, and batch‑copy with concise syntax.

## What is this magical event designator?
- General form: `![event][:word][:modifier]`  
  - **Event** selects a line from history.  
  - **Word** selects one or more words from that line.  
  - **Modifier** transforms the selected text.

### Event Designator
- `!!` – previous line.  
- `!-2` – two lines back.  
- `!1337` – line number 1337 in history.  
- `!ssh` – most recent command starting with “ssh”.  
- `!?text?` – most recent command containing *text*.  
- `!#` – the current line as typed so far.  
- `^old^new^` – quick substitution in the previous command.

### Word Designator
- `!:0` – first word (the command).  
- `!:1` – second word.  
- `!:$` – last word.  
- `!:1-2` – words 2 through 3.  
- `!:*` – all arguments.  
- `!:1-` – all but the last word.  
- `!:2*` – third word through the end.  
- Short forms: `!$` ≡ `!:$`, `!*` ≡ `!:*`.

### Modifier
- `:h` – strip the directory (dirname).  
- `:t` – strip the leading path (basename).  
- `:r` – remove the file extension.  
- `:e` – keep only the extension.  
- `:s/old/new/` – replace first occurrence.  
- `:gs/old/new/` – replace all occurrences.  
- `:p` – print the expanded command without executing it.

## POSIX and the power of `fc`
- `fc` opens a previous command (or range of commands) in an external editor for modification.  
- Basic usages:  
  - `fc` – edit the previous command.  
  - `fc -2` – edit the command two steps back.  
  - `fc grep` – edit the last command starting with *grep*.  
  - `fc -3 -1` – edit the last three commands in one buffer.  
  - `fc -s ssh` – re‑execute the last *ssh* command.  
  - `fc -s old=new cmd` – replace *old* with *new* in the selected command.  
- The editor is taken from `$FCEDIT`, falling back to `$EDITOR` (or `ed` per POSIX).  
- `-e <editor>` overrides the default editor, enabling batch edits such as:  
  ```sh
  fc -e 'sed -i s/prod-01/test-01/g' -3 -1
  ```

## Yell responsibly
- **Rule of three**: start with a simple designator, preview with `:p`, then execute.  
- **The powerful four**: combine event, word, modifier, and `fc` for maximum reuse.  
- Advice for newcomers: test expansions in a harmless context, keep a mental list of the most useful designators, and avoid over‑reliance on complex patterns until comfortable.

## Frequently Asked Questions
- **Will `sudo !!` be stored unchanged in history?** Yes; the expanded command is saved as entered.  
- **How to disable `!` expansion?** `set +H` or `set +o histexpand`.  
- **Can history‑ignored commands be referenced?** Only if they are not filtered out by `HISTIGNORE`.  
- **Why not just use `Ctrl‑r`?** `Ctrl‑r` searches interactively; `!` provides instant, scriptable repeats.  
- **Why not use `Alt-.` instead of `!$`?** `Alt-.` fetches the last argument of the *previous* command, while `!$` can target any historic command.  
- **Am I ignoring other useful features?** No; the article complements existing shortcuts like `Ctrl‑r`, `Alt-.`, and history expansion.

## Further Reading
- POSIX specification for history expansion and `fc`.  
- Shell manual pages (`bash`, `zsh`, `csh`, `tcsh`).  
- Tutorials on advanced history manipulation and editor integration.
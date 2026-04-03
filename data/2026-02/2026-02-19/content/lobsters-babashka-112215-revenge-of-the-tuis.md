---
title: 'Babashka 1.12.215: Revenge of the TUIs'
url: https://blog.michielborkent.nl/babashka-1.12.215.html
site_name: lobsters
content_file: lobsters-babashka-112215-revenge-of-the-tuis
fetched_at: '2026-02-19T06:00:33.867672'
original_url: https://blog.michielborkent.nl/babashka-1.12.215.html
date: '2026-02-19'
description: Babashka 1.12.215 release with JLine3 TUI support, overhauled REPL, deftype map interfaces, riddley/cloverage compatibility, and more.
tags: clojure
---

Archive

Tags

Discuss

 Feed


 Twitter


About

# REPL adventures

A blog mostly about Clojure and ClojureScript.

# Babashka 1.12.215: Revenge of the TUIs

Babashkais a fast-starting native Clojure scripting runtime. It usesSCIto interpret Clojure and compiles to a native binary via GraalVM, giving you Clojure's power with near-instant startup. It's commonly used for shell scripting, build tooling, and small CLI applications. If you don't yet have bb installed, you can with brew:

brew install borkdude/brew/babashka

or bash:

bash <(curl -s https://raw.githubusercontent.com/babashka/babashka/master/install)

This release is, in my opinion, a game changer. With JLine3 bundled, you can now build full terminal user interfaces in babashka. Thebb replhas been completely overhauled with multi-line editing, completions, and eldoc.deftypenow supports map interfaces, making bb more compatible with existing libraries likecore.cache. SCI has had many small improvements, makingriddleycompatible too. Riddley is used in Cloverage, a code coverage library for Clojure, which now also works with babashka (Cloverage PR pending).

## Babashka conf 2026

But first, let me mention an exciting upcoming event!Babashka
confis happening again for the second time! The first time was 2023 in Berlin. This time it's in Amsterdam. The Call for Proposals is open until the end of February, so there is still time to submit your talk or workshop. We are also looking for one last gold sponsor (500 euros) to cover all costs.

## Highlights

### JLine3 and TUI support

Babashka now bundlesJLine3, a Java library for building interactive terminal applications. You get terminals, line readers with history and tab completion, styled output, keyboard bindings, and the ability toreifycustom completers, parsers, and widgets — all from bb scripts.

JLine3 works on all platforms, including Windows PowerShell and cmd.exe.

Here's a simple interactive prompt that reads lines from the user until EOF (Ctrl+D):

(import '[org.jline.terminal TerminalBuilder]
 '[org.jline.reader LineReaderBuilder])

(let [terminal (-> (TerminalBuilder/builder) (.build))
 reader (-> (LineReaderBuilder/builder)
 (.terminal terminal)
 (.build))]
 (try
 (loop []
 (when-let [line (.readLine reader "prompt> ")]
 (println "You typed:" line)
 (recur)))
 (catch org.jline.reader.EndOfFileException _
 (println "Goodbye!"))
 (finally
 (.close terminal))))

### babashka.terminal namespace

A newbabashka.terminalnamespace exposes atty?function to detect whether stdin, stdout, or stderr is connected to a terminal:

(require '[babashka.terminal :refer [tty?]])

(when (tty? :stdout)
 (println "Interactive terminal detected, enabling colors"))

This accepts:stdin,:stdout, or:stderras argument. It uses JLine3's terminal provider under the hood.

This is useful for scripts that want to behave differently when piped vs. run interactively, for example enabling colored output or progress bars only in a terminal.

### charm.clj compatibility

charm.cljis a new Clojure library for building terminal user interfaces using the Elm architecture (Model-Update-View). It provides components like spinners, text inputs, lists, paginators, and progress bars, with support for ANSI/256/true color styling and keyboard/mouse input handling.

charm.clj is now compatible with babashka (or rather, babashka is now compatible with charm.clj), enabled by the combination of JLine3 support and other interpreter improvements in this release. This means you can build rich TUI applications that start instantly as native binaries.

Here's a complete counter example you can save as a single file and run withbb:

#!/usr/bin/env bb

(babashka.deps/add-deps
 '{:deps {io.github.TimoKramer/charm.clj {:git/sha "cf7a6c2fcfcccc44fcf04996e264183aa49a70d6"}}})

(require '[charm.core :as charm])

(def title-style
 (charm/style :fg charm/magenta :bold true))

(def count-style
 (charm/style :fg charm/cyan
 :padding [0 1]
 :border charm/rounded-border))

(defn update-fn [state msg]
 (cond
 (or (charm/key-match? msg "q")
 (charm/key-match? msg "ctrl+c"))
 [state charm/quit-cmd]

 (or (charm/key-match? msg "k")
 (charm/key-match? msg :up))
 [(update state :count inc) nil]

 (or (charm/key-match? msg "j")
 (charm/key-match? msg :down))
 [(update state :count dec) nil]

 :else
 [state nil]))

(defn view [state]
 (str (charm/render title-style "Counter App") "\n\n"
 (charm/render count-style (str (:count state))) "\n\n"
 "j/k or arrows to change\n"
 "q to quit"))

(charm/run {:init {:count 0}
 :update update-fn
 :view view
 :alt-screen true})

More examples can be foundhere.

### Deftype with map interfaces

Until now,deftypein babashka couldn't implement JVM interfaces likeIPersistentMap,ILookup, orAssociative. This meant libraries that define custom map-like types, a very common Clojure pattern, couldn't work in babashka.

Starting with this release,deftypesupports map interfaces. Yourdeftypemust declareIPersistentMapto signal that you want a full map type. Other map-related interfaces likeILookup,Associative,Counted,Seqable, andIterableare accepted freely since the underlying class already implements them.

This unlocks several libraries that were previously incompatible:

* core.cache: all cache types (BasicCache, FIFOCache, LRUCache, TTLCache, LUCache) work unmodified
* linked: insertion-ordered maps and sets

### Riddley and Cloverage compatibility

Riddleyis a Clojure library for code walking that many other libraries depend on. Previously, SCI'sdeftypeandcasedid not macroexpand to the same special forms as JVM Clojure, which broke riddley's walker. Several changes now align SCI's behavior with Clojure:deftypemacroexpands todeftype*,casetocase*, andmacroexpand-1now accepts an optional env map as second argument (inspired by how the CLJS analyzer API works). Together these changes enable riddley and tools built on it, likecloverageandSpecter, to work with bb.

Riddley has moved toclj-commons, thanks toZach Tellmanfor transferring it. I'd like to thank Zach for all his contributions to the Clojure community over the years. Version 0.2.2 includes bb compatibility, which was one of the first PRs merged after the transfer. Cloverage compatibility has beensubmitted
upstream, all 75 cloverage tests pass on both JVM and babashka.

### Console REPL improvements

Thebb replexperience has been significantly improved with JLine3 integration. You no longer needrlwrapto get a comfortable console REPL:

* Multi-line editing: the REPL detects incomplete forms and continues reading on the next line with a#_=>continuation prompt
* Tab completion: Clojure-aware completions powered by SCI, including keywords (:foo,::foo,::alias/foo)
* Ghost text: as you type, the common completion prefix appears as faint inline text after the cursor. Press TAB to accept.
* Eldoc: automatic argument help — when your cursor is inside a function call like(map |), the arglists are displayed below the prompt
* Doc-at-point: press Ctrl+X Ctrl+D to show full documentation for the symbol at the cursor
* Persistent history: command history saved across sessions in~/.bb_repl_history
* Ctrl+C handling: first press on an empty prompt warns, second press exits

Many of these features were inspired byrebel-readline,Leiningen's REPL, andNode.js's REPL.

### SCI improvements

Under the hood,SCI(the interpreter powering babashka) received many improvements in this cycle:

* Functional interface adaptation for instance targets: you can now write(let [^Predicate p even?] (.test p 42))and SCI will adapt the Clojure function to the functional interface automatically.
* Type tag inference: SCI now infers type tags fromletbinding values to binding names, reducing the need for explicit type hints in interop-heavy code.
* Several bug fixes:readwithnil/falseas eof-value,letfnwith duplicate function names,ns-mapnot reflecting shadowed vars, NPE inresolve, and.methodon class objects routing incorrectly.

### Other improvements

* Support multiplecatchclauses in combination with^:sci/error
* Fixsatisfies?on protocols withproxy
* Supportreifywithjava.time.temporal.TemporalQuery
* Fixreifywith methods returningint/short/byte/floatprimitives
* nREPL server now uses non-daemon threads so the process stays alive without@(promise)
* Addclojure.test.junitas built-in source namespace
* Add cp437 (IBM437) charset support in native binary via selective GraalVM charset Feature, avoiding the ~5MB binary size increase fromAddAllCharsets. More charsets can be added on request.

For the full list of changes including new Java classes and library bumps, see thechangelog.

## Thanks

Thank you to all the contributors who helped make this release possible. Special thanks to everyone who reported issues, tested pre-release builds frombabashka-dev-builds, and provided feedback.

Thanks toClojurists Togetherand all babashkasponsorsandcontributorsfor their ongoing support. Your sponsorship makes it possible to keep developing babashka.

And thanks to all babashka users: you make this project what it is. Happy scripting!

Published: 2026-02-17

Tagged:clojurebabashka

Archive

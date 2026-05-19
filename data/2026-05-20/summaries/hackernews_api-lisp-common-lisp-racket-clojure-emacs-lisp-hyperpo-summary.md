---
title: Lisp: Common Lisp, Racket, Clojure, Emacs Lisp - Hyperpolyglot
url: https://hyperpolyglot.org/lisp
date: 2026-05-19
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-20T06:02:27.041567
---

# Lisp: Common Lisp, Racket, Clojure, Emacs Lisp - Hyperpolyglot

# Lisp: Common Lisp, Racket, Clojure, Emacs Lisp – Side‑by‑Side Reference

## Overview
- Comparative cheat‑sheet covering four Lisp dialects: **Common Lisp**, **Racket**, **Clojure**, **Emacs Lisp**.  
- Shows syntax, execution model, core data types, and standard library primitives side by side.

## Versions & Startup
- Common Lisp: SBCL 1.2 (`$ sbcl`).  
- Racket: 6.1 (`$ racket`).  
- Clojure: 1.6 (run via `java -cp clojure.jar clojure.main`).  
- Emacs Lisp: Emacs 24.5 (`M-x ielm`).

## Compilation & Execution
| Aspect | Common Lisp | Racket | Clojure | Emacs Lisp |
|--------|-------------|--------|---------|------------|
| Compile module | `raco make foo.rkt` | `sb-ext:save-lisp-and-die` | `java -jar clojure.jar` | `M-x byte-compile-file` |
| Stand‑alone exe | `sb-ext:save-lisp-and-die … :executable t` | `mzc —exe` | – | – |
| Interpreter | `sbcl` (script mode) | `racket -r foo.rkt` | `java -cp clojure.jar clojure.main foo.clj` | `emacs -batch -l foo.el` |
| Shebang | `#!/usr/bin/env sbcl` | `#!/usr/bin/env racket` | `#!/usr/bin/env java -jar clojure.jar` | `#!/usr/bin/env emacs` |
| REPL | `$ sbcl` | `$ racket` | `java -jar …` | `M-x ielm` |
| One‑liner | `$ racket -e '(+ 1 1)'` | `$ sbcl --script foo.lisp` | – | – |

## Tokenisation & Comments
- Word separator: whitespace in all dialects (Racket also allows commas).  
- End‑of‑line comment: `; …`.  
- Block comment: `#| … |#` (Common Lisp, Racket); not available in Clojure/Emacs Lisp.

## Identifiers & Variables
- **Case**: Common Lisp case‑insensitive; others case‑sensitive.  
- **Allowed characters**: vary; Common Lisp disallows `SP ( ) " , ' \` : ; # | \`; Racket adds `[` `]` `{}` `}`; Clojure permits `* + ! - _ ?` with `/ . :` reserved.  
- **Quoting**: `(quote x)` or `'x` in all except Emacs Lisp where `'x` is a symbol.  
- **Local bindings**: `let` (parallel) and `let*` (sequential) in CL/Racket; vector destructuring `let [x 3 y 4]` in Clojure; `let` with lexical‑let in Emacs Lisp.  
- **Globals**: `defparameter`/`defvar` (CL), `define` (Racket), `def` (Clojure), `defvar`/`setq` (Emacs).  
- **Unbinding**: `makunbound` (CL/Emacs), `ns-unmap` (Clojure), `namespace-undefine-variable!` (Racket).

## Null / Nil
- Common Lisp: `nil` (also `'()`).  
- Racket: `'()` (same as empty list).  
- Clojure: `nil`.  
- Emacs Lisp: `nil` (also `'()`).

## Booleans & Logic
| Dialect | True | False |
|---------|------|-------|
| Common Lisp | `t` | `nil` |
| Racket | `#t` | `#f` |
| Clojure | `true` | `false` |
| Emacs Lisp | `t` | `nil` |

Logical operators (`or`, `and`, `not`) exist in all; relational operators differ slightly (`=` vs `=`/`not=`).

## Numbers
- **Predicates**: `numberp`, `integerp` (CL); `number?`, `integer?` (Racket); `number?`, `integer?` (Clojure); CL‑like predicates in Emacs Lisp.  
- **Arithmetic**: `+ - * /` common; integer division: `truncate`/`rem` (CL), `quotient`/`remainder` (Racket), `quot`/`rem` (Clojure), `/` and `%` (Emacs).  
- **Division by zero**: error in all; CL signals `division-by-zero`, Clojure throws `ArithmeticException`.  
- **Power**: `expt` (CL/Racket), `Math/pow` (Clojure), `expt` (Emacs).  
- **Transcendentals**: `exp log sin cos tan …` (CL/Racket); `Math/…` (Clojure); same names in Emacs Lisp.  
- **Rationals**: literal `3/7` in CL/Racket; Clojure uses `(/ 3 7)`; Emacs Lisp lacks literal rationals.  
- **Complex numbers**: `#c(real imag)` in CL/Racket; `1+2i` style in CL; Clojure/Emacs lack built‑in complex literals.  
- **Overflow**: CL and Racket have arbitrary‑precision integers; Clojure throws on overflow; floating‑point overflow yields `Infinity`/`NaN`.

## Random Numbers
- CL: `(random n)` returns integer; `(random 1.0)` returns float.  
- Racket: same API.  
- Clojure: use Java `java.util.Random` or `rand`, `rand-int`.  
- Emacs Lisp: `random` for integers; no built‑in float/gaussian.

## Bitwise Operations
| CL | Racket | Clojure | Emacs |
|----|--------|---------|-------|
| `logand`, `logior`, `logxor`, `lognot`, `ash` | `bitwise-and`, `bitwise-ior`, `bitwise-xor`, `bitwise-not`, `arithmetic-shift` | `bit-and`, `bit-or`, `bit-xor`, `bit-not`, `bit-shift-left/right` | `logand`, `logior`, `logxor`, `lognot`, `lsh` |

## Literals
- Binary/Octal/Hex: `#b1010`, `#o12`, `#xA` (CL/Racket).  
- Radix formatting: `(format nil "~7r" 42)` in CL.

## Strings
- Predicate: `stringp` (CL), `string?` (Racket/Clojure), `stringp` (Emacs).  
- Literals use double quotes in all dialects.  
- Escape sequences (`\n`, `\t`, `\\`, `\"`, octal/hex Unicode) are supported similarly across the languages.  

---  

**Key takeaway:** While all four dialects share the fundamental Lisp syntax (parenthesized prefix notation), they differ in case sensitivity, identifier rules, module compilation, numeric tower, and standard library naming. This sheet provides a quick lookup for translating common constructs among them.
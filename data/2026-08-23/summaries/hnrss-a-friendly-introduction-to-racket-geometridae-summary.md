---
title: A Friendly Introduction to Racket – geometridae
url: https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/
date: 2026-08-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-23T06:01:01.460204
---

# A Friendly Introduction to Racket – geometridae

# A Friendly Introduction to Racket

## A bit of history
- Lisp was invented by John McCarthy at MIT in 1958; it is the second‑oldest high‑level language still in use.  
- Early innovations that originated in Lisp:
  - Garbage collection  
  - First‑class functions  
  - The REPL (read‑eval‑print loop)  
  - Conditionals as expressions  
  - Homoiconicity (code is data) – the most important idea for this tutorial.  
- Lisp powered AI research in the 70s‑80s; Lisp machines were built to run it directly.  
- After the AI winter Lisp survived as a cult language and later evolved.

### From Lisp to Scheme to Racket
| Year | Event |
|------|-------|
| 1958 | McCarthy invents Lisp |
| 1975 | Sussman & Steele create Scheme |
| 1984 | Common Lisp is standardized |
| 1995 | PLT Scheme (now Racket) is released |
| 2007 | Clojure appears (Lisp on the JVM) |
| 2010 | PLT Scheme is renamed Racket |
| Today | Racket is a language‑building platform (language‑oriented programming) |

## Who uses Lisp today?
- **Clojure** runs in production at banks, airlines, and startups (e.g., Nubank).  
- **Common Lisp** (SBCL) is used in expert systems, flight‑planning (Google Flights), and scientific computing.  
- **Emacs Lisp** powers millions of daily editor sessions.  
- **Guile/Guix** implements an entire Linux distribution in Scheme.  
- **Racket** has its own conference (RacketCon) and is used for language research, formal verification (Rosette), typography/publishing (Pollen), and education worldwide.  
- New Lisps continue to appear: Fennel (Lisp → Lua), Janet, Hy (Lisp on Python), etc.

## Installation (≈5 minutes)
1. Visit https://racket-lang.org.  
2. Download the installer for your OS.  
3. Open DrRacket, the bundled IDE.  
   - The top pane is for definitions, the bottom pane is the REPL.  
   - Begin a file with `#lang racket` to select the language.  
4. For terminal users: `racket` starts a REPL; `raco` is the package manager.

## First contact: everything is an expression
- Syntax rule: `(operator arg1 arg2 …)` – no operator precedence, no special forms.  
- Example REPL sessions show addition, multiplication, and string concatenation using this uniform pattern.

## Definitions and functions
- `(define name value)` creates a constant.  
- `(define (func arg …) body)` creates a function.  
- Comments start with `;`.  
- Anonymous functions use `lambda`:  
  ```racket
  (lambda (x) (* x x))
  ((lambda (x) (* x x)) 5) ; => 25
  ```

## Lists: the heart of Lisp
- Create a list: `(list 1 2 3)` → `'(1 2 3)`.  
- Quote `'` prevents evaluation, turning code into raw data.  
- Core list operations: `first`, `rest`, `cons`, `length`.  

### Higher‑order functions
- `map`, `filter`, and `foldl` let you process lists without explicit loops.  
  ```racket
  (map (lambda (x) (* x x)) '(1 2 3 4 5)) ; => '(1 4 9 16 25)
  (filter even? '(1 2 3 4 5 6))          ; => '(2 4 6)
  (foldl + 0 '(1 2 3 4 5))               ; => 15
  ```

## Recursion: thinking in spirals
- Example factorial definition using `if` and recursive call.  
- Graphics example: drawing a Sierpinski triangle with `2htdp/image` and `let`/`above`/`beside`.

## The grand finale: code that writes code
- Quoted forms turn code into data: `'(+ 1 2)` is the list `(+ 1 2)`.  
- `eval` executes a quoted list as code.  
- Real macros in Lisp operate on code as data, enabling language extension.  

### Example macro: a `while` loop
```racket
(define-syntax-rule (while condition body ...)
  (let loop ()
    (when condition
      body ...
      (loop))))

(define counter 0)
(while (< counter 5)
  (displayln counter)
  (set! counter (+ counter 1)))
```
- The macro creates a new looping construct, demonstrating Racket’s ability to let you build your own syntax.
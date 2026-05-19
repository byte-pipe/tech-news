---
title: 'Lisp: Common Lisp, Racket, Clojure, Emacs Lisp - Hyperpolyglot'
url: https://hyperpolyglot.org/lisp
site_name: hackernews_api
content_file: hackernews_api-lisp-common-lisp-racket-clojure-emacs-lisp-hyperpo
fetched_at: '2026-05-20T06:00:19.411893'
original_url: https://hyperpolyglot.org/lisp
author: veqq
date: '2026-05-19'
description: 'Hyperpolyglot Lisp: Common Lisp, Racket, Clojure, Emacs Lisp'
tags:
- hackernews
- trending
---

Lisp: Common Lisp, Racket, Clojure, Emacs Lisp
 

ca side-by-side reference sheet

grammar and execution|variables and expressions|arithmetic and logic|strings|regular expressions|dates and time|lists|fixed-length arrays|dictionaries|user-defined types|functions|execution control|exceptions|streams|emacs buffers|files|directories|processes and environment|libraries and namespaces|objects|lisp macros|reflection|java interop

common lisp

racket

clojure

emacs lisp

version used

 

SBCL 1.2

Racket 6.1

Clojure 1.6

Emacs 24.5

show version

 

$ sbcl 
--
version

$ racket 
--
version

displayed by repl on startup

$ emacs 
--
version

grammar and execution

common lisp

racket

clojure

emacs lisp

compiler

 

$ raco make 
module
.rkt

M-x byte-compile-file

standalone executable

(sb-ext:save-lisp-and-die

  
"
executable
"

  
:executable t

  
:toplevel '
function
)

$ mzc —exe 
executable
 
file

interpreter

  

$ sbcl 
--
script foo.lisp

$ racket -r foo.racket

specify full path to clojure jar:

java -cp clojure.jar clojure.main foo.clj

shebang

#!/usr/bin/env sbcl 
--
script

#!/usr/bin/env racket 
--
script

specify full path to clojure jar:

#!/usr/bin/env java -jar clojure.jar

#!/usr/bin/env emacs 
--
script

repl

 

$ sbcl

$ racket

$ java -jar /PATH/TO/clojure.jar

M-x ielm

command line program

$ racket -e '(+ 1 1)'

word separator

 

whitespace

whitespace

whitespace and commas

whitespace

end-of-line comment

(+ 1 1) 
; adding

(+ 1 1) 
; adding

(+ 1 1) 
; adding

(+ 1 1) 
; adding

multiple line comment

(+ 1 #| adding |# 1)

(+ 1 #| adding |# 1)

variables and expressions

common lisp

racket

clojure

emacs lisp

identifier

case insensitive, cannot start with digit

excluded characters:

SP ( ) " , ' 
`
 : ; # | \

reserved for user macros:

? ! [ ] { }

case sensitive, cannot start with digit

excluded characters:

SP ( ) [ ] { } " , ' 
`
 ; # | \

case sensitive, cannot start with digit

permitted characters:

A-Z a-z 0-9 * + ! - _ ?

these have special meaning or are reserved:

/ . :

case sensitive, cannot start with digit

excluded characters:

SP ( ) " , ' 
`
 ; # | \ _ [ ]

quoted identifier

and escaped identifier

(setq |white space symbol| 3)

(setq white\ space\ symbol 3)

(define |white space symbol| 3)

(define white\ space\ symbol 3)

none

none

none

(setq white\ space\ symbol 3)

local variable

; parallel assignment:

(let ((x 3) (y 4))

  
(+ x y))

; sequential assignment:

(let* ((x 3) (y (* x x)))

  
(+ x y))

; parallel assignment:

(let ((x 3) (y 4))

  
(+ x y))

; sequential assignment:

(let* ((x 3) (y (* x x)))

  
(+ x y))

(let [x 3 y 4]

  
(+ x y))

(let [[x y] [3 4]]

  
(+ x y))

(let [x 3 y (* x x)]

  
(+ x y))

; parallel assignment:

(lexical-let ((x 3) (y 4))

  
(+ x y))

(lexical-let* ((x 3) (y (* x x)))

  
(+ x y))

global variable

 

(defparameter *x* 3)

; doesn't change x if already set:

(defvar *x* 3)

(define x 3)

; y is not global:

(define (double z)

  
(define y 2)

  
(* y z))

(def x 3)

(set 'x 3)

(setq x 3)

remove variable

 

(makunbound 'x)

(namespace-undefine-variable! 'x)

(ns-unmap *ns* 'x)

(makunbound 'x)

null

 

nil '()

null '()

; same value as null in Java:

nil

nil '()

null test

 

(null x)

(null? x)

(nil? x)

(null x)

identifier as value

'x

(quote x)

'x

(quote x)

'x

(quote x)

'x

(quote x)

identifier test

 

(symbolp 'x)

(symbol? 'x)

(symbol? 'x)

(symbolp 'x)

identifier equality test

(eq 'x 'x)

(eq? 'x 'x)

(= 'x 'x)

(eq 'x 'x)

non-referential identifier

 

:foo

#:foo

:foo

:foo

identifier attributes

set, get, remove

(set 'x 13)

(setf (get 'x :desc) "unlucky")

(get 'x :desc)

(remprop 'x :desc)

none

; value must be instance of clojure.lang.IObj:

(def x (with-meta [13] {:desc "unlucky"}))

(get (meta x) :desc)

; none

(set 'x 13)

(setf (get 'x :desc) "unlucky")

(get 'x :desc)

(remprop 'x :desc)

arithmetic and logic

common lisp

racket

clojure

emacs lisp

true and false

t nil

#t #f

true false

true false

t nil

falsehoods

 

nil ()

#f false

false nil

nil ()

logical operators

 

(or (not t) (and t nil))

(or (not #t) (and #t #f))

(or (not true) (and true false))

(or (not t) (and t nil))

relational operators

 

=
 /= < > <= >=

=
 
none
 < > <= >=

=
 not= < > <= >=

=
 /= < > <= >=

min and max

(min 1 2 3)

(max 1 2 3)

(min 1 2 3)

(max 1 2 3)

(min 1 2 3)

(max 1 2 3)

(min 1 2 3)

(max 1 2 3)

numeric predicates

numberp integerp

rationalp floatp

realp complexp

number? integer?

rational? inexact?

real? complex?

number? integer?

rational? float?

none
 
none

numberp integerp

none
 floatp

none
 
none

arithmetic operators

 

+ - * / mod

+ - * / modulo

+ - * / mod

+ - * / %

integer division

and remainder

(truncate 7 3)

(rem 7 3)

(quotient 7 3)

(remainder 7 3)

(quot 7 3)

(rem 7 3)

(/ 7 3)

(% 7 3)

integer division by zero

division-by-zero 
error

division by zero 
error

arith-error

float division

rational:

(/ 7 3)

float:

(/ 7 (* 3 1.0))

rational:

(/ 7 3)

float:

(/ 7 (float 3))

rational:

(/ 7 3)

float:

(/ 7 (* 3 1.0))

integer quotient:

(/ 7 3)

float:

(/ 7 (* 3 1.0))

float division by zero

division-by-zero 
error

-1.0e+INF, -0.0e+NaN, 
or
 1.0e+INF

power

(expt 2 32)

(expt 2 32)

returns float:

(Math/pow 2 32)

(expt 2 32)

sqrt

 

(sqrt 2)

(sqrt 2)

(Math/sqrt 2)

(sqrt 2)

sqrt -1

 

#c(0.0 1.0)

0+1i

(Math/sqrt -1):
 NaN

-0.0e+NaN

transcendental functions

exp log sin cos tan asin acos atan atan

exp log sin cos tan asin acos atan atan

Math/exp Math/log Math/sin Math/cos Math/tan Math/asin Math/acos Math/atan Math/atan2

exp log sin cos tan asin acos atan atan

float truncation

return two values, first is integer:

truncate round ceiling floor

return floats:

truncate round ceiling floor

return integers:

int Math/round

return floats:

Math/ceil Math/floor

truncate round ceiling floor

fround fceiling ffloor

truncate 
returns integer

absolute value

and signum

abs signum

abs

racket:
 sgn

Math/abs Math/signum

abs signum

integer overflow

 

none; arbitrary-precision integers

none; arbitrary-precision integers

clojure.lang.Numbers.throwIntOverflow 
exception

float overflow

 

floating-point-overflow 
error

not literals:

-Infity NaN Infinity

rational construction

(/ 3 7)

; literal:

3/7

(/ 3 7)

; literal:

3/7

; also rational:

2.718

(exp 1)

(/ 3 7)

; literal:

3/7

rational decomposition

(numerator 3/7)

(denominator 3/7)

(numerator 3/7)

(denominator 3/7)

(numerator 3/7)

(denominator 3/7)

none
 
none

complex construction

#c(1 2)

1+2i

(+ 1 +2i)

none

none

complex decomposition

(realpart #c(1 2))

(imagpart #c(1 2))

(phase #c(1 2))

(abs #c(1 2))

(conjugate #c(1 2))

(real-part 1+2i)

(imag-part 1+2i)

(angle 1+2i)

(magnitude 1+2i)

(conjugate 1+2i)

none

none

none
 
none

random number

uniform integer, uniform float, normal float

(random 100)

(random 1.0)

none

(random 100)

(random)

none

(def rnd (java.util.Random.))

(.nextInt rnd 100)

(.nextFloat rnd)

(.nextGaussian rnd)

(random 100)

none

none

random seed

(setq *random-state*

  
(sb-ext:seed-random-state 17))

(random-seed 17)

bit operators

ash 
left shift when 2nd argument positive
 logand logior logxor lognot

arithmetic-shift 
left shift when 2nd argument positive
 bitwise-and bitwise-ior bitwise-xor bitwise-not

bit-shift-left bit-shift-right bit-and bit-or bit-xor bit-not

lsh 
left shift when 2nd argument positive
 logand logior logxor lognot

binary, octal, and hex literals

#b101010

#o52

#x2a

#b101010

#o52

#x2a

radix

 

(format nil "~7r" 42)

strings

common lisp

racket

clojure

emacs lisp

string test

 

(stringp "foo")

(string? "foo")

(string? "foo")

(stringp "foo")

string literal

 

"foo bar"

"foo bar"

"foo bar"

"foo bar"

newline in literal

 

yes

yes

yes

yes

literal escapes

\" \\

\t \n \r \" \\ \
ooo
 \u
hhhh

\b \t \n \f \r \" \\ \
ooo
 \u
hhhh

\b \t \n \f \r \" \\ \
ooo
 \u
hhhh
 \x
h
 - \x
hhhhhh
 \C-
x
 \M-
x

constructor

 

(string #\f #\o #\o)

(string ?f ?o ?o)

format string

(format nil "~a: ~a ~,2f" "Foo" 7 13.457)

(format "~a ~a ~a" "Foo" 7 13.457)

(String/format "%s: %d %.2f"

  
(to-array ["Foo" 7 13.457]))

(format "%s: %d %.2f" "Foo" 7 13.457)

format specifiers

~a
  
  
any type, human readable

~s
  
  
any time, read parseable

~%
  
  
newline

~~
  
  
tilde

~c
  
  
character

~,5f
  
5 digits right of decimal mark

~d
  
  
decimal

~x
  
  
hex

~o
  
  
octal

~b
  
  
binary

~a
  
  
any type, human readable

~s
  
  
any time, read parseable

~%
  
  
newline

~~
  
  
tilde

~c
  
  
character

~d
  
  
decimal

~x
  
  
hex

~o
  
  
octal

~b
  
  
binary

compare strings

(string= "foo" "bar")

(string< "foo" "bar")

(string=? "foo" "bar")

(string<? "foo" "bar")

(.equals "foo" "bar")

(.compareTo "foo" "bar")

(string= "foo" "bar")

(string< "foo" "bar")

concatenate

 

(concatenate 'string "foo " "bar " "bar")

(string-append "foo " "bar " "baz")

(str "foo " "bar " "baz")

(concat "foo " "bar " "baz")

replicate

make-string 3 :initial-element #\f)

(make-string 3 #\f)

(String. (into-array

  
(. Character TYPE)

  
(repeat 3 \f)))

(make-string 3 ?f)

translate case

(string-downcase "FOO")

(string-upcase "foo")

(string-downcase "FOO")

(string-upcase "foo")

(.toLowerCase "FOO")

(downcase "FOO")

(upcase "foo")

capitalize

; "Foo Bar":

(string-capitalize "foo bar")

; "Foo Bar":

(capitalize "foo")

trim

(string-trim

  
'(#\space #\tab #\newline)

  
" foo ")

(require srfi/13/string)

(string-trim-both " foo ")

(.trim " foo ")

none; see notes for an implementation

pad

on right, on left

(format nil "~10a" "foo")

(format nil "~10@a" "foo")

number to string

(concatenate 'string

  
"value: "

  
(princ-to-string 8))

(string-append

  
"value: "

  
(number->string 8))

(str "Value: " 8)

(concat

  
"value: "

  
(number-to-string 8))

string to number

(+ 7 (parse-integer "12"))

 

(+ 73.9 (read-from-string ".037"))

(+ 7 (string->number "12"))

 

(+ 73.9 (string->number ".037"))

(+ 7 (Integer/parseInt "12"))

 

(+ 73.9 (Float/parseFloat ".037"))

(+ 7 (string-to-number "12"))

 

(+ 73.9 (string-to-number ".037"))

split

(cl-ppcre:split

  
"[ \t\n]+"

  
"foo bar baz")

(regexp-split #rx"[ \n\t]+"

  
"foo bar baz")

(seq

  
(.split "foo bar baz"

  
  
"[ \t\n]+"))

(split-string "foo bar baz")

string join

(reduce

  
(lambda (m o)

  
  
(concatenate 'string m " " o))

  
'("foo" "bar" "baz"))

(string-join

  
'("foo" "bar" "baz")

  
" ")

(reduce #(str %1 " " %2)

  
'("foo" "bar" "baz"))

(reduce

  
(lambda (m o) (concat m " " o))

  
'("foo" "bar" "baz"))

length

 

(length "foo")

(string-length "foo")

(.length "foo")

(length "foo")

index of substring

(search "bar" "foo bar")

racket:

(require srfi/13/string)

(string-contains "foo bar" "bar")

(.indexOf "foo bar" "bar")

(search "bar" "foo bar")

extract substring

 

(subseq "foo bar" 4 7)

(substring "foo bar" 4 7)

(.substring "foo bar" 4 7)

(substring "foo bar" 4 7)

character literal

#\a #\space #\newline #\backspace #\tab #\linefeed #\page #\return #\rubout

#\a #\space #\newline #\backspace #\tab #\linefeed #\page #\return #\nul #\vtab #\alarm #\esc #\delete

not in racket:
 #\alarm #\esc #\delete

\a \newline \space \backspace \tab 
?
 \formfeed \return 
?

?a ?\b ?\t ?\n ?\f ?\r ?\" ?\\ ?\
ooo
 ?\u
hhhh
 ?\x
h
 - ?\x
hhhhhh
 ?\C-
x
 ?\M-
x

test characters

 

(characterp #\x)

(alpha-char-p #\x)

(alphanumericp #\x)

(digit-char-p #\7)

(lower-case-p #\x)

(upper-case-p #\X)

(char? #\x)

(char? \x)

(characterp ?x)

chr and ord

(code-char 97)

(char-code #\a)

(integer->char 97)

(char->integer #\a)

(char 97)

(int \a)

to array of characters

; list:

(string->list "foo")

character lookup

 

(char "foo" 0)

(string-ref "foo" 0)

(.charAt "foo" 0)

(aref "foo" 0)

regular expressions

common lisp

racket

clojure

emacs lisp

literal

use a string:

"\\b\\d{5}\\b"

posix extended:

#rx"^[0-9][0-9][0-9][0-9][0-9]$"

(regexp "^[0-9][0-9][0-9][0-9][0-9]$")

perl style:

#px"\\b\\d{5}\\b"

(pregexp "\\b\\d{5}\\b")

#"\b\d{5}\b"

character class abbrevations

. \d \D \s \S \w \W

regexp:

.

pregexp:

. \d \D \s \S \w \W

. \d \D \s \S \w \W

. \w \W \ca \cl \cg \Ca \Cl \Cg \s
x

\ca \cl 
and
 \cg 
match ASCII, Latin, and Greek characters.

Character classes of the form
 \sx 
depend on the current syntax table.

anchors

^ $ \b \B

regexp:

^ $

pregexp:

^ $ \b \B

^ $ \A \b \B \G \z \Z

^ $ \b \B

match test

(ql:quickload "cl-ppcre")

(if (cl-ppcre:all-matches "1999" s)

  
(format t "party!"))

(regexp-match #rx"bar" "foo bar")

(re-find #"bar" "foo bar")

(string-match "bar" "foo bar")

case insensitive match test

(regexp-match #px"(?i:lorem)" "Lorem")

(re-find #"(?i:lorem)" "Lorem")

substitution

(cl-ppcre:regex-replace "[^l]l"

  
"hello"

  
"EL")

 

(cl-ppcre:regex-replace-all "[^l]l"

  
"hello hello"

  
"EL")

(regexp-replace #rx"el"

  
"hello"

  
"EL")

 

(regexp-replace* #rx"el"

  
"hello hello"

  
"EL")

(.replaceFirst "hello" "[^l]l" "XX")

 

(.replaceAll "hello hello"

  
"[^l]l" "XX")

?

 

(replace-regexp-in-string "[^l]l"

  
"EL"

  
"hello hello")

group capture

(match (regexp-match

  
  
#px"(\\d{4})-(\\d{2})-(\\d{2})"

  
  
"2010-06-03")

  
[(list s yr mn dy) (list yr mn dy)])

(let [[_ yr mn dy]

  
  
(re-find #"(\d{4})-(\d{2})-(\d{2})"

  
  
  
"2010-06-03")]

  
yr)

scan

(re-seq #"\w+" "dolor sit amet")

backreference in match and substitution

(regexp-match #px"(\\w+) \\1" "do do")

(regexp-replace #px"(\\w+) (\\w+)"

  
"do re"

  
"\\2 \\1")

dates and time

common lisp

racket

clojure

emacs lisp

broken-down datetime type

No dedicated type; a list of 9 values is used:

  
second: 0-59

  
minute: 0-59

  
hour: 0-23

  
day of month: 1-31

  
month: 1-12

  
year: 4 digits

  
day of week: 0-6 for Mon-Sun

  
is daylight savings time: t or nil

  
timezone: negated UTC offset in hours

current datetime

(get-decoded-time)

(require racket/date)

(current-date)

(def dt (new java.util.Date))

(current-time)

current unix epoch

gray|; seconds since Jan 1, 1900:##

(get-universal-time)

(current-seconds)

(/ (System/currentTimeMillis) 1000.0)

(float-time)

unix epoch to broken-down datetime

(decode-universal-time

  
(get-unversal-time))

(seconds->date (current-seconds))

(def dt (new java.util.Date

  
  
(System/currentTimeMillis)))

(seconds-to-time (float-time))

broken-down datetime to unix epoch

(encode-universal-time 0 22 10 31 5 2015)

(require racket/date)

(date->seconds (current-date))

(/ (.getTime (new java.util.Date)) 1000.0)

(multiple-value-bind (b s)

  
(current-time)

  
(+ (* b (expt 2 16)) s))

format datetime

(def s "yyyy-MM-dd HH:mm:ss")

(def fmt (new java.text.SimpleDateFormat s))

(.format fmt (new java.util.Date))

(format-time-string

  
"%Y-%m-%d %H:%M:%S"

  
(current-time))

parse datetime

(require (prefix-in s19. srfi/19))

(define (date-str->unix-time s fmt)

  
  
(s19.time-second

  
  
  
(s19.date->time-utc

  
  
  
  
(s19.string->date s fmt))))

(date-str->unix-time

  
"2015-05-31 07:06:00"

  
"~Y-~m-~d ~H:~M:~S")

(def s "yyyy-MM-dd HH:mm:ss")

(def fmt (new java.text.SimpleDateFormat s))

(.parse fmt "2015-05-30 09:14:14")

date parts

(multiple-value-bind

  
(ss mi hr dy mo yr)

  
(get-decoded-time)

  
(list ss mi hr) 
; quiesce warning

  
(list dy mo yr))

(date-year (current-date))

(date-month (current-date))

(date-day (current-date))

(def cal (new java.util.GregorianCalendar))

(.setTime cal dt)

(.get cal java.util.Calendar/DAY_OF_MONTH)

(+ (.get cal java.util.Calendar/MONTH) 1)

(.get cal java.util.Calendar/YEAR)

(multiple-value-bind

  
(ss mi hr dy mo yr)

  
 (decode-time (current-time))

  
(list dy mo yr))

time parts

(multiple-value-bind

  
(ss mi hr)

  
(get-decoded-time)

  
(list ss mi hr))

(date-hour (current-date))

(date-minute (current-date))

(date-second (current-date))

(def cal (new java.util.GregorianCalendar))

(.setTime cal dt)

(.get cal java.util.Calendar/HOUR_OF_DAY)

(.get cal java.util.Calendar/MINUTE)

(.get cal java.util.Calendar/SECOND)

(multiple-value-bind

  
(ss mi hr dy mo yr)

  
 (decode-time (current-time))

  
(list ss mi hr))

build broken-down datetime

(encode-universal-time 0 22 10 31 5 2015)

(let

  
[yr 2015 mo 5 dy 31 hr 10 mi 22 ss 0]

  
(def cal

  
  
(new java.util.GregorianCalendar

  
  
  
yr (- mo 1) dy hr mi ss)))

(encode-time 0 50 8 31 5 2015)

lists

common lisp

racket

clojure

emacs lisp

literal

 

'(1 2 3)

(quote (1 2 3))

'(1 2 3)

'[1 2 3]

'{1 2 3}

(quote (1 2 3))

'(1 2 3)

(quote (1 2 3))

'(1 2 3)

(quote (1 2 3))

constructor

 

(list 1 2 3)

(list 1 2 3)

(list 1 2 3)

(list 1 2 3)

predicate

 

(listp '(1 2 3))

(list? '(1 2 3))

(list? '(1 2 3))

(listp '(1 2 3))

empty test

nil 
and
 '() 
are synonyms and evaluate as false in a boolean context. All other values are true.

(empty? '())

(empty? ())

nil 
and
 '() 
are synonyms and evaluate as false in a boolean context. All other values are true.

evaluating the empty list

nil

error

()

nil

cons

 

(cons 1 '(2 3))

(cons 1 '(2 3))

(cons 1 '(2 3))

(cons 1 '(2 3))

head

 

(car '(1 2 3))

(first '(1 2 3))

(car '(1 2 3))

(first '(1 2 3))

first

car

tail

 

(cdr '(1 2 3))

(rest '(1 2 3))

(cdr '(1 2 3))

(rest '(1 2 3))

(rest '(1 2 3))

(next '(1 2 3))

(cdr '(1 2 3))

(rest '(1 2 3))

head and tail of empty list

both evaluate to
 nil

error

()

both evaluate to
 nil

length

 

(length '(1 2 3))

(length '(1 2 3))

(count '(1 2 3))

(length '(1 2 3))

equality test

 

(equal '(1 2 3) '(1 2 3))

(equal? '(1 2 3) '(1 2 3))

(= '(1 2 3) '(1 2 3))

(equal '(1 2 3) '(1 2 3))

nth element

; indexed from zero:

(nth 2 '(1 2 3 4))

(list-ref '(1 2 3 4) 2)

(nth '(1 2 3 4) 2)

(nth 2 '(1 2 3 4))

out-of-bounds behavior

nil

error

raises
 IndexOutOfBoundsException

nil

element index

(position 7 '(5 6 7 8))

(require srfi/1)

(list-index (lambda (x) (= x 7)) '(5 6 7 8))

none

(position 7 '(5 6 7 8))

concatenate

 

(append '(1 2 3) '(4 5 6))

(append '(1 2 3) '(4 5 6))

(concat '(1 2 3) '(4 5 6))

(append '(1 2 3) '(4 5 6))

take

 

none

(take '(1 2 3 4) 2)

(take 2 '(1 2 3 4))

(subseq '(1 2 3 4) 0 2)

drop

 

(nthcdr 2 '(1 2 3 4))

(drop '(1 2 3 4) 2)

(drop 2 '(1 2 3 4))

(nthcdr 2 '(1 2 3 4))

last element

 

(car (last '(1 2 3)))

(last '(1 2 3))

(last '(1 2 3))

(car (last '(1 2 3)))

all but last element

(butlast '(1 2 3))

(define a '(1 2 3))

(take a (- (length a) 1))

(butlast '(1 2 3))

(butlast '(1 2 3))

reverse

 

(reverse '(1 2 3))

(reverse '(1 2 3))

(reverse '(1 2 3))

(reverse '(1 2 3))

sort

 

(sort '(3 2 4 1) '<)

(sort '(3 2 4 1) <)

(sort < '(3 2 4 1))

(sort '(3 2 4 1) '<)

dedupe

 

(remove-duplicates '(1 1 2 3))

(remove-duplicates '(1 1 2 3))

(remove-duplicates '(1 1 2 3))

membership

 

(member 7 '(1 2 3))

(member 7 '(1 2 3))

(member 7 '(1 2 3)

map

(mapcar

  
(lambda (x) (* x x))

  
'(1 2 3))

(map (lambda (x) (* x x)) '(1 2 3))

(map #(* % %) '(1 2 3))

(mapcar

  
(lambda (x) (* x x))

  
'(1 2 3))

filter

(remove-if-not

  
(lambda (x) (> x 2))

  
'(1 2 3))

; remove-if returns complement

(filter

  
(lambda (x) (> x 2))

  
'(1 2 3))

; filter-not returns complement

(filter #(> % 2) '(1 2 3))

; remove returns complement

(remove-if-not

  
(lambda (x) (> x 2))

  
'(1 2 3))

; remove-if returns complement

reduce

(reduce '-

  
'(1 2 3 4)

  
:initial-value 0)

(foldl (lambda (x y) (- y x)) 0 '(1 2 3 4))

(reduce - 0 '(1 2 3 4))

(reduce '-

  
'(1 2 3 4)

  
:initial-value 0)

right fold

(reduce '-

  
'(1 2 3 4)

  
:initial-value 0

  
:from-end t)

(foldr - 0 '(1 2 3 4))

none

(reduce '-

  
'(1 2 3 4)

  
:initial-value 0

  
:from-end t)

iterate

(dolist (x '(1 2 3))

  
(print x)

  
(print (- x)))

(for ((x '(1 2 3)))

  
(printf "~a~n" x)

  
(printf "~a~n" (- x)))

(doseq [x '(1 2 3)]

  
(println x)

  
(println (- x)))

(dolist (x '(1 2 3))

  
(print x)

  
(print (- x)))

universal predicate

(every

  
(lambda (i) (= 0 (rem i 2)))

  
'(1 2 3 4))

(for/and ((i '(1 2 3 4)))

  
(= 0 (remainder i 2)))

(every? #(= 0 (rem % 2)) '(1 2 3 4))

(every

  
(lambda (i) (= 0 (% i 2)))

  
'(1 2 3 4))

existential predicate

(some

  
(lambda (i) (= 0 (rem i 2)))

  
'(1 2 3 4))

(for/or ((i '(1 2 3 4)))

  
(= 0 (remainder i 2)))

(some #(= 0 (rem % 2)) '(1 2 3 4))

(some

  
(lambda (i) (= 0 (% i 2)))

  
'(1 2 3 4))

list comprehension

(for*/list

  
((file "ABCDEFGH") (rank (in-range 1 9)))

  
(format "~a~a" file rank))

(for

  
[file "ABCDEFGH" rank (range 1 9)]

  
(format "%c%d" file rank))

shuffle

 

(shuffle '(1 2 3 4))

(shuffle '(1 2 3 4))

set head

(defparameter *a* '(1 2 3))

(setf (car *a*) 3)

(require schema/mpair)

(define a (mlist 1 2 3))

(set-mcar! a 3)

none

(setq a '(1 2 3)

(setcar a 3)

set tail

(defparameter *a* '(1 2 3))

(setf (cdr *a*) '(4 5 6))

(require schema/mpair)

(define a (mlist 1 2 3))

(set-mcdr! a (mlist 4 5 6))

none

(setq a '(1 2 3)

(setcar a 3)

(setcdr a '(4 5 6))

manipulate back

(defparameter *a* '(1 2 3))

(push 4 *a*)

(pop *a*)

none

(setq a '(1 2 3))

(push 4 a)

(pop a)

flatten

(flatten '(1 2 (3 (4))))

(flatten '(1 2 (3 (4))))

associative array lookup

 

(assoc 3 '((1 2) (3 4)))

(assoc 3 '((1 2) (3 4)))

none, see note

(assoc 3 '((1 2) (3 4)))

flat associative array lookup

 

(getf '(1 2 3 4) 3)

none

none

(getf '(1 2 3 4) 3)

pair literal

 

'(1 . 2)

'(1 . 2)

none

'(1 . 2)

cons cell test

(cons '(1 . 2))

(not (atom '(1 . 2)))

(cons? '(1 . 2))

(pair? '(1 . 2))

none

(cons '(1 . 2))

(not (atom '(1 . 2)))

translate elements recursively

(sublis '((1 . 2) (3 . 4))

  
'(1 (3 3 (1))))

(sublis '((1 . 2) (3 . 4))

  
'(1 (3 3 (1))))

fixed-length arrays

common lisp

racket

clojure

emacs lisp

literal

 

#(1 2 3)

#(1 2 3)

[1 2 3]

[1 2 3]

constructor

 

(vector 1 2 3)

(vector 1 2 3)

(vector 1 2 3)

(vector 1 2 3)

size

 

(length #(1 2 3))

(vector-length #(1 2 3))

(count [1 2 3])

(length [1 2 3])

lookup

(elt #(1 2 3) 0) 
or

(aref #(1 2 3) 0)

(vector-ref #(1 2 3) 0)

(nth [1 2 3] 0)

(elt [1 2 3] 0)

update

(setq v [1 2 3])

(setf (aref v 2) 4)

(define v (vector 1 2 3))

(vector-set! v 2 4)

(replace {2 4} [1 2 3])

(setq v #(1 2 3))

(setf (aref v 2) 4)

out-of-bounds behavior

raises
 sb-kernel:index-too-large-error

error

array to list

 

(coerce #(1 2 3) 'list)

(vector->list #(1 2 3))

(seq [1 2 3])

(coerce [1 2 3] 'list)

list to array

 

(coerce '(1 2 3) 'vector)

(list->vector '(1 2 3))

(vec '(1 2 3))

(coerce '(1 2 3) 'vector)

reverse

(reverse #(1 2 3))

sort

(sort #(2 4 1 3) #'<)

map

(map 'vector (lambda (x) (* x x)) #(1 2 3))

filter

(remove-if-not (lambda (x) (> x 2)) #(1 2 3))

; also remove-if

reduce

dictionaries

common lisp

racket

clojure

emacs lisp

literal

 

none

; immutable:

#hash(("t" . 1) ("f" . 0))

; clojure.lang.PersistentArrayMap:

{"t" 1 "f" 0}

none

constructor

(defparameter *h* (make-hash-table :test 'equal))

; default equality test is 'eql

(define ih

  
(make-immutable-hash

  
  
'(("t" . 1) ("f" . 0))))

; mutable:

(define h (make-hash '(("t" . 1) ("f" . 0))))

; immutable:

(def ih (hash-map "t" 1 "f" 0))

(setq h (make-hash-table :test 'equal))

predicate

 

(hash-table-p *h*)

(hash? h)

; also true of assoc. lists and vectors:

(dict? h)

(map? ih)

(hash-table-p h)

size

 

(hash-table-count *h*)

(hash-count h)

; also works with assoc lists and vectors:

(dict-count ih)

(count ih)

(hash-table-count h)

lookup

 

(gethash "t" *h*)

(hash-ref h "t")

; return -1 if not found:

(hash-ref h "m" -1)

; also works with assoc. lists and vectors:

(dict-ref ih "t")

(dict-ref ih "m" -1)

(get ih "t")

(find ih "t")

; return -1 if not found:

(get ih "m" -1)

(gethash "t" h)

update

(setf (gethash "t" *h*) 1)

(hash-set! h "t" 2)

(define ih2 (hash-set ih "t" 2))

; also dict-set! and dict-set

(def ih2 (assoc ih "t" 2))

(puthash "t" 1 h)

missing key behavior

returns
 nil

error

returns
 nil

returns
 nil

is key present

 

(nth-value 1 (gethash "t" *h*))

(hash-has-key? h "t")

; also dict-has-key?

(contains? ih "t")

none

delete

(remhash "t" *h*)

(hash-remove! h "t")

 

(define ih2

  
(hash-remove ih "t"))

; also dict-remove! and dict-remove

(def ih2 (dissoc ih "t"))

(remhash "hello" h)

merge

; values in ih2 take precedence:

(define ih3 (merge ih ih2))

invert

(require 'clojure.set)

(define ih4 (clojure.set/map-invert ih))

iterate

(maphash

  
(lambda (k v)

  
  
(print k)

  
  
(print v))

  
*h*)

(hash-for-each h

  
(lambda (k v)

  
  
(printf "~a~n" k)

  
  
(printf "~a~n" v)))

; also dict-for-each

(doseq [p ih]

  
(println (first p))

  
(println (second p)))

(maphash

  
(lambda (k v)

  
  
(print k)

  
  
(print v))

  
h)

keys and values as lists

none

(hash-keys h)

(hash-values h)

; also dict-keys and dict-values

(def hkeys (map (fn [p] (first p)) ih))

(def hvals (map (fn [p] (second p)) ih))

none

user-defined types

common lisp

racket

clojure

emacs lisp

defstruct

(defstruct account id balance)

(define-struct account (id (balance #:mutable)))

(defstruct account :id :balance)

(defstruct account id balance)

struct

(setq a

  
(make-account

  
  
:id 3

  
  
:balance 17.12))

(define a (make-account 3 17.12))

(def a (struct account 3 17.12))

(setq a

  
(make-account :id 3 :balance 17.12))

struct getter

 

(account-id a)

(account-id a)

(:id a)

(account-id a)

struct setter

 

(setf (account-balance a) 0)

(set-account-balance! a 0)

none

(setf (account-balance a) 0)

struct predicate

 

(account-p a)

(account? a)

none

(account-p a)

functions

common lisp

racket

clojure

emacs lisp

define function

 

(defun add (x y) (+ x y))

(define (add x y) (+ x y))

(defn add [x y] (+ x y))

(defun add (x y) (+ x y))

can function and variable share name

yes

no

no

yes

optional argument

(defun add (a &optional b)

  
(if (null b) a (+ a b)))

(define (add a (b null))

  
(if (null? b) a (+ a b)))

(defn add ([a] a) ([a b] (+ a b)))

no syntax error if called with more than 2 args:

(defn add [a & [b]]

  
(if (nil? b) a (+ a b)))

(defun add (a &optional b)

  
(if (null b) a (+ a b)))

variable number of arguments

(defun add (a &rest b)

  
(if (null b)

  
  
a

  
  
(+ a (eval (cons '+ b)))))

(define (add a . b)

  
(if (null? b)

  
  
a

  
  
(+ a (apply + b))))

(defn add [a & b]

  
(if (nil? b) a (+ a (apply + b))))

(defun add (a &rest b)

  
(if (null b)

  
  
a

  
  
(+ a (eval (cons '+ b)))))

default value

(defun add (a &optional (b 0))

  
(+ a b))

racket:

(define (add a (b 0)) (+ a b))

(defn add

  
([a] (add a 0))

  
([a b] (+ a b)))

none

named parameter

(defun logarithm (&key number base)

  
(/ (log number) (log base)))

 

(logarithm :base 2 :number 8)

none

(defn logarithm [{x :number b :base}] (/ (Math/log x) (Math/log b)))

(logarithm {:base 2 :number 8})

(defun logarithm

  
(&key number &key base)

  
(if base

  
  
(/ (log number) (log base))

  
  
(log number)))

 

order significant, not key names:

(logarithm :foo 8 :bar 2)

return multiple values

(defun sqrts (x)

  
(values (sqrt x) (- (sqrt x))))

(define (sqrts x)

  
(values (sqrt x) (- (sqrt x))))

(defn sqrts [x] (list (Math/sqrt x) (- (Math/sqrt x))))

values 
creates a list:

(defun sqrts (x)

  
(values (sqrt x) (- (sqrt x))))

assign multiple values to local variables

(multiple-value-bind (r1 r2)

  
(sqrts 3)

  
r2)

(let-values

  
(((r1 r2) (sqrts 3)))

  
r2)

(let [[r1 r2] (sqrts 3)] r2)

(multiple-value-bind

  
(r1 r2)

  
(sqrts 3)

  
r2)

assign multiple values to global variables

(multiple-value-setq (r1 r2)

  
(sqrts 3))

(define-values (r1 r2) (sqrts 3))

none

(multiple-value-setq (r1 r2) (sqrts 3))

convert list to multiple values

(values-list '(1 2 3))

(apply values '(1 2 3))

multiple values are lists

multiple values are lists

assign multiple values to list

(multiple-value-list (sqrts 3))

(call-with-values

  
(lambda () (sqrts 3))

  
list)

multiple values are lists

multiple values are lists

tail call optimization

yes for sbcl

yes

yes with
 recur

no

lambda

(lambda (x) (* x x))

(lambda (x) (* x x))

#(* % %)

(fn [x] (* x x))

; shortcut notation with two args:

#(* %1 %2)

(lambda (x) (* x x))

apply

((lambda (x) (* x x)) 2)

 

(apply #'(lambda (x) (* x x)) '(2))

((lambda (x) (* x x)) 2)

 

(apply (lambda (x) (* x x)) '(2))

(#(* % %) 2)

 

((fn [x] (* x x)) 2)

 

(apply #(* % %) '(2))

((lambda (x) (* x x)) 2)

 

(apply

  
#'(lambda (x) (* x x))

  
'(2))

execution control

common lisp

racket

clojure

emacs lisp

progn

 

progn prog1 prog2

begin 
none
 
none

r6rs:

begin begin0 
none

do 
none
 
none

progn prog1 prog2

loop

(setq i 1)

(loop (print "hello")

  
(if (> i 10)

  
  
(return)

  
  
(setq i (+ i 1))))

none, use recursion

(loop [i 1]

  
(if (<= i 10)

  
  
  
(do (println "hello")

  
  
  
  
  
(recur (+ i 1)))))

(setq i 1)

(loop (print "hello")

  
  
  
(if (> i 10)

  
  
  
  
  
(return)

  
  
  
  
  
(setq i (+ i 1))))

do

(do ((i 1) (sum 0))

  
((> i 100) sum)

  
(setq sum (+ sum i))

  
(setq i (+ i 1)))

do* 
initializes serially

none

none

(do ((i 1) (sum 0))

  
  
((> i 100) sum)

  
  
(setq sum (+ sum i))

  
  
(setq i (+ i 1)))

do* 
initializes sequentially

dotimes

(dotimes (i 10 nil)

  
(format t "hello~%"))

none

(dotimes [_ 10]

  
(println "hello"))

(dotimes (i 10 nil)

  
(print "hello\n"))

if

 

(if (< x 0) (- x) x)

(if (< x 0) (- x) x)

(if (< x 0) (- x) x)

(if (< x 0) (- x) x)

when

(when (< x y)

  
(print "x is less ")

  
(print "than y"))

racket:

(when (< x y)

  
(display "x is less ")

  
(display "than y"))

(when (< x y)

  
(println "x is less ")

  
(println "than y"))

(when (< x y)

  
(print "x is less ")

  
(print "than y"))

cond

(cond ((> x 0) 1)

  
((= x 0) 0)

  
(t -1))

(cond ((> x 0) 1)

  
((= x 0) 0)

  
(else -1))

(cond (> x 0) 1

  
(= x 0) 0

  
true -1)

(cond ((> x 0) 1)

  
((= x 0) 0)

  
(t -1))

lazy evaluation

(define x (delay (/ 1 0)))

(promise? x)

(+ 1 (force x))

continuations

(define cc null)

(+ 1 (call/cc (lambda (x) (set! cc x) 0)))

(cc 5)

exceptions

common lisp

racket

clojure

emacs lisp

error

 

(error "failed")

(error "failed")

(throw (Exception. "failed"))

(error "failed")

handle error

(handler-case

  
(error "failed")

  
(simple-error (e)

  
  
(format t "error: ~a" e)))

(with-handlers

  
((exn:fail?

  
   
(lambda (e)

  
  
   
(printf "error: ~a"

  
  
  
   
(exn-message e)))))

  
(error "failed"))

(try (throw (Exception. "failure"))

  
(catch Exception e

  
  
(printf "error: %s"

  
  
  
(.getMessage e))))

(condition-case e

  
(error "failed")

  
(error (message "error: %s"

  
  
(error-message-string e))))

define exception

(define-condition odd-err (error)

  
((num :accessor odd-err-num

  
  
  
  
:initarg :num))

  
(:report

  
  
(lambda (e s)

  
  
  
(format s "odd number: ~a"

  
  
  
  
(odd-err-num e)))))

(define exn:odd-err? "odd number")

only symbols and keywords can be thrown and caught

throw exception

(error 'odd-err :num 7)

(raise exn:odd-err?)

(throw (Exception. "failed"))

(throw 'odd-err t)

catch exception

(handler-case (/ 1 0)

  
(division-by-zero ()

  
  
(progn

  
  
  
(format t "division by zero")

  
  
  
nil)))

(with-handlers ((exn:fail? (lambda (e) (begin (printf "division by zero~n") null)))) (/ 1 0))

(try (/ 1 0) (catch ArithmeticException _ (do (println "division by zero") nil)))

(catch 'failed (throw 'failed nil) t)

restart-case

(defun halve (l)

  
(mapcar (lambda (x)

  
  
(restart-case

  
  
  
(if (= (rem x 2) 0) (/ x 2)

  
  
  
  
(error 'odd-error :num x))

  
  
  
(round-down () (/ (- x 1) 2))

  
  
  
(round-up () (/ (+ x 1) 2)))) l))

none

none

invoke-restart

(handler-bind

  
((odd-err

  
  
  
(lambda (c)

  
  
  
  
(invoke-restart

  
  
  
  
  
'round-down))))

  
  
  
(halve '(1 2 4 9)))

none

none

finally clause

(unwind-protect

  
(error "failure")

  
(print "clean up"))

none

(try (throw (Exception. "failure"))

     
(finally (println "clean up")))

(unwind-protect

  
(error "failure")

  
(print "clean up"))

streams

common lisp

racket

clojure

emacs lisp

standard file handles

*standard-input*

*standard-output*

*error-output*

(current-input-port)

(current-output-port)

(current-error-port)

*in*

*out*

*err*

end-of-file behavior

read-line 
returns two values, the 2nd set to
 T 
at end-of-file.

EOF-OF-FILE 
is signaled when reading past end of file.

Returns the value
 eof.

Use
 eof-object? 
to test for it.

.readLine 
on a
 java.io.Reader 
object returns
 nil.

read line from stdin

(setq line (read-line))

(let ((s (read-line)))

  
#|use s
|#
)

(let [s (read-line)]

  
(comment use s)
)

chomp

 

read-line 
discards newline

read-line 
discards newline

write line to stdout

(defun println (s)

  
(format t "~a~%" s))

 

(println "hello")

(write-string s)

(newline)

(println "hello")

write formatted string to stdout

(format t "~s ~d: ~2$~%"

  
"foo"

  
7

  
13.7)

(printf "~a ~a: ~a~n"

  
"foo"

  
7

  
(/ (round (* 13.7 100)) 100))

(printf "%s %d %.2f\n" "foo" 7 13.7)

open file for reading

(setq in (open "/etc/hosts"))

(let

  
((f (open-input-file "/etc/hosts")))

  
#| use f 
|#
)

; f is java.io.Reader object:

(let [f (clojure.java.io/reader "/etc/hosts")]

  
(.readLine f))

open file for writing

(setq out (open "/tmp/test" :direction :output :if-exists :supersede))

(let

  
((f (open-output-file

  
  
  
  
"/tmp/foo"

  
  
  
  
#:exists 'truncate)))

  
#| use f 
|#
)

; f is java.io.Writer object:

(let [f (clojure.java.io/writer "/tmp/foo")]

  
(.write f "lorem ipsum\n")

  
(.close f))

open file for appending

(setq out (open "/tmp/test" :direction :output :if-exists :append))

(let

  
((f (open-output-file

  
  
  
  
"/tmp/foo"

  
  
  
  
#:exists 'append)))

  
#| use f 
|#
)

(let [f (clojure.java.io/writer "/tmp/foo"

  
  
  
:append true)]

  
(.write f "lorem ipsum\n")

  
(.close f))

close file

 

(close in)

(close-input-port f)

(close-output-port f)

(.close f)

close file implicitly

(with-open-file (out #P"/tmp/test" :direction :output) (write-line "lorem ipsum" out))

(call-with-input-file

  
"/etc/hosts"

  
(lambda (f) (
#| use f 
|#
))

; also call-with-output-file

(with-open [f

  
  
(clojure.java.io/reader "/etc/hosts")]

  
(comment use f)
)

read line

 

(setq line (read-line f))

(define line (read-line in))

(.readLine f)

iterate over file by line

(for ([line (in-lines

  
  
  
  
(open-input-file

  
  
  
  
  
"/etc/hosts"))])

  
(write-string line)

  
(newline))

(loop [line (.readLine f)]

  
(if (not= line nil)

  
  
(do (println line)

  
  
  
(recur (.readLine f)))))

read file into array of strings

; to list of strings:

(sequence->list (in-lines

  
  
(open-input-file "/etc/hosts")))

(vec (line-seq f))

read file into string

(define s (file->string "/etc/hosts"))

(let [s (slurp "/etc/hosts")]

  
(print s))

write string

 

(write-string s f)

(.write f s)

write line

(write-string s f)

(newline f)

(.write f (println-str s))

flush file handle

 

(flush-output f)

(f .flush)

file handle position

get, set

; Evaluates to non-negative integer:

(file-position f)

; Sets next read or write

; to beginning of file:

(file-position f 0)

; arg is characters from current position;

; moving backward not possible:

(.skip f 1000)

; arg is max characters to buffer:

(.mark f 1000000)

; move to position saved when .mark was called:

(.rest f)

in memory stream

(setq f (make-string-input-stream

  
  
"lorem ipsum"))

(read-line f)

(setq f2 (make-string-output-stream)

(write-string "lorem ipsum)

(get-output-stream-string out)

(define f (open-input-string "lorem ipsum"))

(read-line f)

(define f2 (open-output-string))

(write-string "lorem ipsum" f2)

(get-output-string f2)

; use *in* to read from string:

(with-in-str "lorem ispum"

  
(read-line))

; use *out* to write to string:

(with-out-str

  
(println "lorem ipsum"))

emacs buffers

emacs lisp

list buffers

;; list of buffer objects:

(buffer-list)

;; name of first buffer in list:

(buffer-name (car (buffer-list)))

;; name of current buffer:

(buffer-name (current-buffer))

current buffer

get and set

;; name of current buffer:

(buffer-name (current-buffer))

;; open in current pane:

(switch-to-buffer "foo.txt")

;; open in other pane:

(switch-to-buffer-other-window

  
"bar.txt")

clear buffer

;; current buffer:

(erase-buffer)

;; buffer named "foo.txt:

(with-current-buffer "foo.txt"

  
(erase-buffer))

point

get and set

;; 1-based index of char under cursor:

(point)

;; go to beginning of current buffer:

(goto-char 1)

;; go to end of current buffer:

(goto-char (buffer-size))

search and set point

;; Set point to character after string.

;; 1st arg is position in buffer beyond

;;
   
which search stops.

;; If 2nd arg is true, return nil

;;
   
on failure, otherwise raise error.

;; 3rd argument is the occurrence

;;
   
of the string, if negative

;;
   
search backwards from point.

(search-forward "lorem" nil t 1)

insert at string point

;; takes 1 or more args:

(insert "lorem" " ipsum")

current buffer as string

(buffer-string)

insert file contents at point

(insert-file "/etc/passwd")

mark

get and set

;; to beginning of current buffer:

(set-mark 1)

;; to point of current buffer:

(set-mark (point))

files

common lisp

racket

clojure

emacs lisp

file test, regular file test

(osicat:file-exists-p "/tmp/foo")

(osicat:regular-file-exists-p "/tmp/foo")

??

(file-exists? "/etc/hosts")

(.exists (io/file "/etc/hosts"))

(file-exists-p "/etc/hosts")

(file-regular-p "/etc/hosts")

file size

(file-size "/etc/hosts")

(.length (io/file "/etc/hosts"))

(eighth

  
(file-attributes "/etc/hosts"))

is file readable, writable, executable

(pair? (filter

  
  
(lambda (x) (eq? x 'read))

  
  
(file-or-directory-permissions

  
  
  
"/etc/hosts")))

(pair? (filter

  
  
(lambda (x) (eq? x 'write))

  
  
(file-or-directory-permissions

  
  
  
"/etc/hosts")))

(pair? (filter

  
  
(lambda (x) (eq? x 'execute))

  
  
(file-or-directory-permissions

  
  
  
"/etc/hosts")))

(.canRead (io/file "/etc/hosts"))

(.canWrite (io/file "/etc/hosts"))

(.canExecute (io/file "/etc/hosts"))

set file permissions

(file-or-directory-permissions

  
"/tmp/foo"

  
#o755)

(set-file-modes "/tmp/foo" #o755)

last modification time

(file-or-directory-modify-seconds "/tmp/foo")

; Unix epoch in milliseconds:

(.lastModified (java.io.File. "/tmp/foo"))

copy file, remove file, rename file

(cl-fad:copy-file #P"/tmp/foo"

  
#P"/tmp/bar")

(delete-file #P"/tmp/foo")

(rename-file #P"/tmp/bar"

  
#P"/tmp/foo")

(copy-file "/tmp/foo" "/tmp/bar")

(delete-file "/tmp/foo")

(rename-file-or-directory

  
"/tmp/bar"

  
"/tmp/foo")

(clojure.java.io/copy

  
(java.io.File. "/tmp/foo")

  
(java.io.File. "/tmp/bar"))

(clojure.java.io/delete-file "/tmp/foo")

(.renameTo (java.io.File. "/tmp/bar")

  
(java.io.File. "/tmp/foo"))

(copy-file "/tmp/foo" "/tmp/bar")

(delete-file "/tmp/foo")

(rename-file "/tmp/bar" "/tmp/foo")

create symlink, symlink test, get target

(osicat:make-link "/tmp/hosts" :target "/etc/hosts")

(make-file-or-directory-link

  
"/etc/hosts"

  
"/tmp/hosts")

(link-exists? "/tmp/hosts")

??

(make-symbolic-link "/etc/hosts" /tmp/hosts")

returns target if symlink or nil:

(file-symlink-p "/tmp/hosts")

temporary file

(define tmp (make-temporary-file))

(path->string tmp)

; java.io.File:

(java.io.File/createTempFile "foo" ".txt")

(make-temp-file "foo")

directories

common lisp

racket

clojure

emacs lisp

build pathname

(make-pathname

  
:directory '(:absolute "etc")

  
:name "hosts")

; returns path; convert to string

; with path->string:

(build-path "/etc" "hosts")

(require '[clojure.java.io :as io])

; returns java.io.File;

; convert to string with .getPath:

(io/file "/etc" "hosts")

dirname and basename

(pathname-directory #P"/etc/hosts")

(pathname-name #P"/etc/hosts")

(let-values (((dir file _)

  
  
  
  
(split-path "/etc/hosts")))

  
#| use dir or file 
|#
)

(require '[clojure.java.io :as io])

(.getParent (io/file "/etc/hosts"))

(.getName (io/file "/etc/hosts"))

(file-name-directory "/etc/hosts")

(file-name-nondirectory

  
"/etc/hosts")

absolute pathname

(simplify-path

  
(path->complete-path ".."))

(.getCanonicalPath (java.io.File. ".."))

(expand-file-name "..")

iterate over directory by file

(dolist (file (osicat:list-directory "/tmp")) (format t "~a~%" file))

(for ([path (directory-list "/etc")])

  
(write-string

  
  
(path->string path)))

; file-seq returns java.io.File objects for files

; in arg directory and any subdirs recursively.

(filter #(= (.getParent %) "/etc")

  
(file-seq (clojure.java.io/file "/etc")))

(dolist

  
(file (directory-files "/etc"))

  
(print file)))

make directory

(make-directory* "/tmp/foo/bar")

(require '[clojure.java.io :as io])

(.mkdir (io/file "/tmp/foo"))

creates parents if 2nd arg non-nil:

(make-directory "/tmp/foo/bar" t)

recursive copy

(copy-directory/files "/tmp/foo.d"

  
"/tmp/bar.d")

remove empty directory

(delete-directory "/tmp/foo.d")

(delete-directory "/tmp/foo.d")

(clojure.java.io/delete-file "/tmp/foo.d")

(delete-directory "/tmp/foo.d")

remove directory and contents

(osicat:delete-directory-and-files "/tmp/foo.d")

(delete-directory/files "/tmp/foo.d")

(delete-directory "/tmp/foo.d" t)

directory test

(osicat:directory-exists-p #P"/etc")

(directory-exists? "/etc")

(.isDirectory (io/file "/etc"))

(file-directory-p "/etc")

processes and environment

common lisp

racket

clojure

emacs lisp

command line arguments

*posix-argv*

current-command-line-arguments

*command-line-args*

in shebang mode only:

command-line-args 
or
 argv

program name

environment variables

(posix-getenv "HOME")

(getenv "HOME")

(System/getenv "HOME")

(getenv "HOME")

user id and name

exit

external command

(run-program "ls" '( "/etc"))

(require scheme/system)

(system "ls /etc")

(.exec (Runtime/getRuntime) "ls")

(shell-command "ls /etc")

command substitution

(shell-command-to-string "ls /etc")

libraries and namespaces

common lisp

racket

clojure

emacs lisp

complete example

$ cat b/a.clj

(ns b.a)

(def x 3)

$ java -cp clojure.jar:. clojure.main

=> (require 'b.a)

=> b.a/x

3

compile library

(compile-file "a.lisp")

$ raco make a.rkt

(compile 'a)

$ emacs -batch -Q -L . \

  
-f batch-byte-compile a.el

load library

 

(load "a.lisp")

(require a)

(require 'a)

(require "a")

load library in subdirectory

(load "b/a.lisp")

(require "b/a.rkt")

(require 'b.a)

hot patch

(load "a.lisp")

none

(require 'b.a :reload)

(load "a")

load error

raises
 sb-int:simple-file-error

raises
 exn:fail:syntax:missing-module. 
Because
 require 
must be top-level, the exception cannot be handled.

raises
 FileNotFoundException

raises
 file-err

library path

contains working directory at startup

(require setup/dirs)

(get-collects-search-dirs)

same as path used by java VM

; adds directory to library path:

(add-to-list 'load-path ("/home/ed/.emacs.d/lib"))

library path environment variable

none

CLASSPATH

EMACSLOADPATH

library path command line option

none

$ java -cp /foo/bar:/baz/quux

$ emacs -L /foo/bar

namespace declaration

(defpackage :foo)

(module mconst racket

  
(provide pi)

  
(define pi 3.14))

(ns mconst)

No namespaces; a common convention is to use a prefix on all identifiers in a library, separated from the rest of the identifier by a hyphen.

subnamespace declaration

none

; must be in b/a.clj:

(ns b.a)

namespace separator

:

:

. 
and
 /

import definitions

; set current *package* to foo and import symbol twiddle from bar:

(defpackage :foo

  
(:import-from :bar :twiddle))

import all definitions in namespace

; set current *package* to foo and import symbols from bar:

(defpackage :foo

  
(:use :bar))

namespace shadow avoidance

identifier shadow avoidance

package manager help

$ raco help

$ raco pkg 
--
help

$ raco pkg install 
--
help

list installed packages

$ raco pkg show 
--
all

M-x list packages

search packages

(ql:system-apropos "time")

http://pkgs.racket-lang.org

M-x list-packages

install package

; install quicklisp

(load "~/quicklisp/setup.lisp")

(ql:quickload "osicat")

$ raco pkg install 
--
deps search-auto srfi

Use
 M-x list-packages 
to bring up the package menu;
 i 
to select a package to install, and
 x 
to install it.

remove package

$ raco pkg remove srfi

In the package menu, use
 d 
to select a package to uninstall and
 x 
to uninstall it.

objects

common lisp

racket

clojure

emacs lisp

define class

(defclass rectangle ()

  
(

  
  
(height

  
  
  
:accessor rectangle-height

  
  
  
:initarg :height)

  
  
(width

  
  
  
:accessor rectangle-width

  
  
  
:initarg :width)))

(define rectangle%

  
(class object%

  
  
(init width)

  
  
(init height)

  
  
(super-new)

  
  
(define curr-height height)

  
  
(define curr-width width)

  
  
(define/public (get-height)

  
  
  
curr-height)

  
  
(define/public (get-width)

  
  
  
curr-width)

  
  
(define/public (set-height ht)

  
  
  
(set! curr-height ht))

  
  
(define/public (set-width wd)

  
  
  
(set! curr-width wd))))

use java:

public class Rectangle {

  
public float height;

  
public float width;

  
public Rectangle(float h, float w) {

  
  
this.height = h;

  
  
this.width = w;

  
}

  
public void setHeight(float h) {

  
  
this.height = h;

  
}

  
public void setWidth(float w) {

  
  
this.width = w;

}

make instance

(make-instance 'rectangle

  
:height 3

  
:width 7)

(define rect

  
(new rectangle

  
  
(height 7)

  
  
(width 3)))

(import 'Rectangle)

(def r (Rectangle. 7 3))

read attribute

 

(rectangle-height rect)

(send rect get-height)

(.height r)

write attribute

 

(setf (rectangle-height rect) 4)

(send rect set-height 4)

(.setHeight r 8)

define method

(defmethod area ((figure rectangle))

  
(* (rectangle-height figure)

  
  
(rectangle-width figure)))

(define/public (area)

  
(* curr-height curr-width))

(defmulti area class)

(defmethod area Rectangle [r] (* (.height r) (.width r)))

invoke method

 

(area rect)

(send rect area)

(area r)

universal superclass

standard-object t

object%

Object

multiple inheritance

yes

no

only one direct superclass; can implement multiple interfaces

lisp macros

common lisp

racket

clojure

emacs lisp

backquote and comma

(setq op '+)

(eval 
`
(,op 1 1))

(define op '+)

(eval 
`
(,op 1 1))

(eval (quasiquote ((unquote op) 1 1)))

(def op +)

(eval 
`
(,op 1 1))

(setq op '+)

(eval 
`
(,op 1 1))

defmacro

(defmacro rpn (arg1 arg2 op)

  
(list op arg1 arg2))

(define-syntax-rule (rpn arg1 arg2 op) (op arg1 arg2))

(defmacro rpn [arg1 arg2 op]

  
(list op arg1 arg2))

(defmacro rpn (arg1 arg2 op)

  
(list op arg1 arg2))

defmacro w/ backquote

(defmacro rpn (arg1 arg2 op)

  
`
(,op ,arg1 ,arg2))

(define-syntax-rule (rpn3 arg1 arg2 op)

  
(eval ‘(,op ,arg1 ,arg2)))

(defmacro rpn [arg1 arg2 op] 
`
(~op ~arg1 ~arg2))

(defmacro rpn (arg1 arg2 op)

  
`
(,op ,arg1 ,arg2))

macro predicate

(macro-function rpn)

none

none

none

macroexpand

(macroexpand ’(rpn 1 2 +))

(syntax-object->datum (expand-to-top-form '(rpn 1 2 +)))

(macroexpand '(rpn 1 2 +))

(macroexpand '(rpn 1 2 +))

splice quote

(defmacro add ( &rest args )

  
`
(+ ,@args))

(define-syntax-rule ( add first …) (+ first …))

(defmacro add [ & args ] 
`
(+ ~@args))

(defmacro add ( &rest args )

  
`
(+ ,@args))

recursive macro

(defmacro add (a &rest b)

  
`
(if (null ',b)

  
  
(+ ,a)

  
  
(+ ,a (add ,@b))))

(define-syntax add (syntax-rules ()

  
[(add x) x]

  
[(add x y) (+ x y)]

  
[(add x y …) (+ x (add y …))]))

(defmacro add ([a] 
`
(+ ~a)) ([a & b] 
`
(+ ~a (add ~@b))))

(defmacro add (a &rest b)

  
`
(if (null ',b)

  
  
(+ ,a)

  
  
(+ ,a (add ,@b))))

hygienic

 

no

yes

with
 # 
suffix

no

local values

(defmacro square-sum (x y)

  
(let ((sum (gensym)))

  
  
`
(let ((,sum (+ ,x ,y)))

  
  
  
(* ,sum ,sum))))

(define-syntax-rule (square-sum x y)

  
(let ((sum (+ x y)))

  
  
(* sum sum)))

(defmacro two-list [x] 
`
(let [arg# ~x] (list arg# arg#)))

(defmacro square-sum (x y)

  
(let ((sum (gensym)))

  
  
`
(let ((,sum (+ ,x ,y)))

  
  
  
(* ,sum ,sum))))

reflection

common lisp

racket

clojure

emacs lisp

inspect type

 

(type-of '(1 2 3))

(typep '(1 2 3) 'list)

(listp '(1 2 3))

(list? '(1 2 3))

(= (type 1) java.lang.Long)

(= (class 1) java.lang.Long)

(integer? 1)

(type-of [1 2 3] 'vector)

(typep [1 2 3] 'vector)

(vectorp [1 2 3])

instance-of

instance?

basic types

logical and numeric:

bignum bit complex double-float fixnum float integer long-float nil null number ratio rational real short-float signed-btye single-float t unsigned-byte

symbols and strings:

base-character character extended-character keyword simple-string standard-char string symbol

data structures:

array atom bit-vector cons hash-table list sequence simple-array simple-bit-vector simple-vector vector

other:

compiled-function function package pathname random-state stream

sequence data types

list vector

list vector hash-table string input-port range

all collections and strings

list vector

get docstring

 

(describe #'mapcar)

none

(doc map)

(describe-function 'mapcar)

define function with docstring

(defun add (x y)

  
"add x and y"

  
(+ x y))

none

(defn add "add x and y" [x y]

  
(+ x y))

(defun add (x y)

  
"add x and y"

  
(+ x y))

apropos and documentation search

none

none

(apropos #"^add$")

(find-doc #"add \S+ and \S+")

(apropos "^add$")

none

java interoperation

common lisp

racket

clojure

emacs lisp

new

(def rnd (new java.util.Random))

(def rnd (java.util.Random.))

method

(. rnd nextFloat)

(.nextFloat rnd)

(. rnd nextInt 10)

(.nextInt rnd 10)

class method

 

(Math/sqrt 2)

chain

 

import

(import '(java.util Random))

(def rnd (Random.))

to java array

(to-array '(1 2 3))

(into-array Integer '(1 2 3))

__________________________________________

__________________________________________

__________________________________________

__________________________________________

## version used

Versions used to verify examples in the reference sheet.

## show version

How to determine the version.

# Grammar and Execution

## compiler

racket

Compiling a.ss creates the byte-code compiled file a_ss.zo, which will be used bymzschemein preference to the source code if it encounters

(require a)

## standalone executable

racket

In order for code to be compiled as a standalone executable, it must be packaged as a module. This can be accomplished by putting the#lang schemeshorthand the top of the file. All functions that are defined in the module will be executed in order. Here is a simple example:

#lang scheme
(define hello
 (printf "Hello world!~n"))

emacs

Building Emacs

## interpreter

How to interpret the code in a file.

## shebang

How to have a script run by the interpreter automatically. Replace the given path with the path to the interpreter on your system.

emacs lisp

To run some lisp code from within emacs, useM-x loadorM-x load-file. The first command will use the list of strings inload-pathto search for the file. It is not necessary to specify the.elor.elcsuffix if the file has one.

The following snippet is an emacs lisp shebang script implementation ofcat:

#!/usr/bin/env emacs --script
(condition-case nil
 (let (line)
 (while (setq line (read-from-minibuffer ""))
 (princ line)
 (princ "\n")))
 (error nil))

An implementation ofecho:

#!/usr/bin/env emacs --script
(condition-case nil
 (progn
 (dotimes (i (length argv) nil)
 (princ (nth i argv))
 (princ " "))
 (princ "\n"))
 (error nil))

## repl

How to invoke the repl from the command line.

racket:

Racket also provides a GUI repl environment called DrRacket.

clojure:

The clojure repl saves the result of each evaluation in the variables *1, *2, … and the last exception in *e.

## command line program

How to pass in a program to be executed on the command line.

## word separator

What is used to separate the operator and data of a S-expression.

## identifier characters

In lisps other than clojure, any character can be used in a symbol. Some characters are special to the reader and must be escaped to include them in a symbol. The reader will interpret a sequence of characters starting with a digit as a number instead of a symbol, so escaping must be used to create such a symbol.

common lisp:

Common Lisp is case insensitive, and the reader converts all letters to upper case. A symbol consisting of just periods "." must be escaped. Symbols that start and end with an asterisk "*" may conflict with system defined special variables.

racket:

#is only disallowed by the reader at the beginning of symbols. A symbol consisting of a single period must be escaped.

## end-of-line comment

## multiple line comment

#| |# delimited comments in Common Lisp and Scheme can span multiple lines, and thus can be used to comment out code.

clojure:

Code with balanced parens can be commented out in the following manner:

(comment
(+ 1 1)
)

# Variables and Expressions

## identifier

Are identifiers case sensitive; which characters can be used in identifers.

In Lisp, identifiers are calledsymbols.

## quoted identifer

How to quote or escape characters in identifiers which are otherwise prohibited.

## local variable

How to declare a local variable.

## global variable

How to declare a global variable.

## remove variable

How to remove a variable.

## null

The null value.

common lisp

niland the empty list'()are identical.

racket

nulland the empty list'()are identical.

clojure

niland the empty list'()are distinct.

emacs lisp

niland the empty list'()are identical.

## null test

How to test whether a value is null.

## identifier as value

How to get the value of an identifier.

In Lisp, identifiers are first class values and can be stored in variables. When used as an argument, the Lisp interpreter will treat an identifier as the value of the variable associated with the identifier unless special syntax is used.

## identifier test

How to test whether a value is an identifier.

## non-referential identifier

A non-referential identifier is an identifier whose value is itself.

Non-referential identifiers are calledkeywordsin Lisp. They also appear in Prolog, where they are calledatoms, and Ruby, where they are calledsymbols.

A non-referential identifier can be convenient to use as a key in a dictionary, since it doesn't have to single quote escaped.

Strings are an alternative to non-referential identifiers; some languages have string interning which makes the use of strings just as efficient as non-referential identifiers.

## identifier attributes

In Common Lisp, there is a dictionary of attributes associated with each identifier called aproperty list.

Clojuremetadatais stored with a value which is an instance ofclojure.lang.IObj. Many types are subclasses ofclojure.lang.IObj, but integers, floats, and strings are not. Clojure metadata is immutable: all keys must be set at once and there is no way to remove keys.

## cell types

The different cell types. A lisp-1 only stores a single entity under a symbol in a given environment. A lisp-2 stores multiple entities, and which entity a symbol will resolve to depends on how the symbol is used. In particular, a value and a function can be stored under the same symbol without collision.

## nil, is () null?, is () symbol?

(eq nil ())

is true in common lisp and emacs lisp.

(eq? () null)

is true in Scheme.

## keyword

Keywords are pre-defined symbols that evaluate to their printed representation. The reader recognizes them by the initial colon, or in the case of Scheme, by the initial "#:". In Scheme it is an error to use a keyword as an expression.

## atom

atomis is a predicate which returns false for cons cells, and true for anything else. All lists except for the empty list are cons cells.

racket

Scheme lacksatom, butcons?is its logical negation.

clojure

Clojure lacks cons cells. Thusatomif implemented in the language would always return true. However,(not (list? x))is closer to the spirit and certainly more useful. Becausenilis not the empty list in clojure there is also ambiguity about what the value of(atom ())would be.

## quote

All lisps have a single quote macro abbreviation forquote. Here are identical ways to quote a symbol and a list:

(quote a)
'a

(quote (+ 3 7))
'(+ 3 7)

evalis a one-sided inverse ofquote. If X is arbitrary lisp code, then the following are identical

X
(eval (quote X))

## eq, equal, =

In his 1960 paper, McCarthy describedeqas undefined if either or both arguments are not atomic. Common Lisp and Scheme (eq?) return true if the arguments both evaluate to the same list in memory, otherwise false.equalandequal?(Scheme) return true if the arguments evaluate to lists with the same elements as determined by callingequalorequal?recursively.

In Common Lisp and Scheme, = can only be called on numeric arguments. The predicates for whether a symbol is numeric arenumberpandnumber?, respectively.

Clojure dispenses witheqandequaland defines=to be equivalent to the Common Lispequal.

## car

Becausecarandcdrare abbreviations for parts of the word of the IBM 704, there is a trend to replace them withfirstandrest. However,carandcdrare short, and convenient notation exists for abbreviating nested calls tocarandcdr.

In terms ofcar,cdr, and combinations thereof, here is what the dialects define:

common lisp

r5rs

racket

clojure

emacs lisp

car,first

car

car,first

first

car,first

cadr,second

cadr

cadr,second

second,fnext

cadr,second

caddr,third

caddr

caddr,third

caddr,third

cadddr,fourth

cadddr

cadddr,fourth

cadddr,fourth

fifth

fifth

fifth

sixth

sixth

sixth

seventh

seventh

seventh

eighth

eighth

eighth

ninth

ninth

ninth

tenth

tenth

tenth

cdr, rest

cdr

cdr, rest

rest,next

cdr, rest

cddr

cddr

cddr

cddr

cdddr

cdddr

cdddr

cdddr

cddddr

cddddr

cddddr

cddddr

caar

caar

caar

ffirst

caar

cdar

cdar

cdar

nfirst

cdar

## cdr

common lisp

cdrandrestreturnnilwhen called on an empty list.

racket

cdrandrestraise an error when called on an empty list.

clojure

restreturns an empty set () when called on an empty or singleton list, whereasnextreturnsnil. In clojure, the empty set evaluates as true in a boolean context andnilevaluates as false.

## cons

clojure

Clojure does not implement a list as a linked list of cons cells. The second argument toconsmust be a list.

## cond

## lambda

clojure:

(#(+ %1 %2) 1 2)

## label

## apply

# Arithmetic and Logic

integers

Common Lisp and Racket have arbitrary-precision integers and use them by default.

Racket provides thefixnumlibrary for access to hardware integers:

(require racket/fixnum)

(fx+ 3 7)

Operations on Racket fixnums cause an error when they overflow.

rationals and floats

Common Lisp and Racket have arbitrary-precision rationals. Racket uses them in a number of cases when Common Lisp uses hardware floats:

3.14
3e10
(exp 1)

Racket provides theflonumlibrary for access to hardware floats:

(require racket/flonum)

(fl* 3.1 -7.2)

complex numbers

Both the real and imaginary part of a Common Lisp complex number will have the same type, but the type can be integer, rational, or float.

## true and false

Literals for true and false.

## falsehoods

Values which evaluate to false in a boolean context.

racket

nulland the empty list {{'{} do not evaluate as false in a boolean context.

## logical operators

The logical operators.

## relational operators

Relational operators for performing comparisons.

## min and max

Functions for returning the least and greatest of the arguments.

## numeric predicates

A selection of numeric predicates.

realpandreal?are true of all numbers which have a zero imaginary component.floatpandinexact?are true if the number is being stored in a floating point representation.

racket:

The following all evaluate as #t:

(rational? 1.1)
(rational? (sqrt 2))
(rational? pi)

## closure of integers under division

The number system that containing the potential results of integer division. In mathematics, the closure of integers under division is the rationals, and this is true for common lisp, scheme, and clojure as well.

Emacs lisp performs integer division (i.e. computes the quotient), so the closure of the integers under division is the integers.

## arithmetic operators

In Lisp, + and * take zero or more arguments and - and / take one or more arguments. With zero arguments + and * return the additive and multiplicative identities 0 and 1. With one argument + and * return the argument and - and / return the additive and multiplicative inverses: i.e. the negation and the reciprocal. When evaluating 3 or more arguments - and / are computed from left to right: i.e. (- 3 4 5) is computed as (- (- 3 4) 5).

clojure:

Math.powreturns a double.

emacs:

Unary division (i.e. computing the reciprocal) generates a wrong number of arguments error.

## transcendental functions

## float truncation

For rounding, floor, and ceiling, the return value is integer if the argument is rational and floating point if the argument is floating point, unless otherwise noted.

racket:

inexact->exactcan be used to convert a float returned byround,ceiling, orfloorto an integer.

clojure:

Math/roundalways returns an integer and throws and error if called on a rational.Math/floorandMath/ceilcan be called on a rational, but always return a float.

emacs:

round,ceiling, andfloorreturn integers.fround,fceiling, andffloorreturn floats.

## quotient and remainder

## (sqrt -2)

The value of(sqrt -2). Common lisp and Scheme support complex numbers. Clojure and Emacs Lisp do not.

## decomposition of integer, rational, complex

For absolute value, the type of the return value is the same of the type of the argument.

racket:

Thescheme/mathlibrary must be loaded to usesgn.

clojure:

Math/signumonly operates on a float and returns a float

## random number

How to generate a random integer, and a random float in a uniform and a normal distribution.

## bit operators

racket:

The bitwise operators implemented by Gambit and Racket are specified in the withdrawn standardSRFI 33.

emacs:

Also hasash, which gives a different value when both arguments are negative.

# Strings

## character literals

The syntax for character literals. The first literal uses the letter "a" as an example of how to write a literal for all ASCII printing characters.

common lisp:

Characters are of type standard-char. The predicate ischaracterp.

racket:

The predicate ischar?.

clojure:

Characters are of type java.lang.Character.

emacs:

Characters are of type integer and can be manipulated by arithmetic operators.characterpandintegerpare synonyms.

## string literal

The syntax for a string literal.

## string escapes

A list of escape sequences that can be used in string literals.

emacs lisp:

The \x escape sequence is followed by one to six hex digits. Because a variable number of hex digits can be used, it may be necessary to indicate the end of the sequence with a backslash and a space, e.g. the following string literal is "λ123":

 "\x3bb\ 123"

## character access

How to get the character at a given position in a string.

## find substring

Find the location of a substring in a string.

## extract substring

## length

## constructors

## comparison

common lisp:

Here is the complete list of string comparison functions:

string=
string<
string>
string<=
string>=
string/=

There are also case insensitive versions of the above functions:

string-equal
string-lessp
string-greaterp
string-not-greaterp
string-not-lessp
string-not-equal

racket:

Case sensitive string comparison:

string<=?
string<?
string=?
string>=?
string>?

Case insensitive string comparison:

string-ci<=?
string-ci<?
string-ci=?
string-ci>=?
string-ci>?

emacs lisp:

Emacs has only these string comparison functions, all of which are case sensitive:

string=
string-equal
string<
string-lessp

string=andstring-equalare synonyms, as arestring<andstring-lessp.

## case

## trim

emacs:

An implementation oftrim:

(defun trim (s)
 (let ((s1 (replace-regexp-in-string "[ \t]*$" "" s)))
 (replace-regexp-in-string "^[ \t]*" "" s1)))

## convert from string, to string

How to convert strings to numbers, and numbers to strings.

common lisp:

read-from-stringinvokes the reader, so the return value is not guaranteed to be a floating point number.

Here is aparse-floatfunction which will convert all real numeric types to floats and raise a simple error if another condition is encountered.

(defun parse-float (s)
 (let ((readval (handler-case
 (read-from-string s)
 (sb-int:simple-reader-error nil)
 (end-of-file nil))))
 (cond ((realp readval ) (+ readval 0.0))
 (t (error (concatenate 'string "not a float: " s))))))

## concat

## split

## join

## format

# Regular Expressions

## regular expressions

common lisp

http://weitz.de/cl-ppcre/

emacs lisp

string-matchreturns the first index of the first matching substring, or nil.

The following code moves the point to next position following the point that matches the argument, and returns the index of the that position.

(re-search-forward "hello")

## regex substitution

## regex special characters

# Dates and Time

## current datetime

## current unix epoch

## unix epoch to broken-down datetime

## broken-down datetime to unix epoch

## format datetime

## parse datetime

## date parts

## time parts

## build broken-down datetime

# Lists

## list literal

## pair literal

## (car '())

## (cdr '())

## (eval '())

A practical advantage of having(eval '())be equal to '() is that the empty list doesn't have to be quoted.

## list functions

## nth

nthandlist-refcount from zero.nthreturnsnilif the index is too large.list-refthrows an error.

## index of list element

How to get the index of a list element. The first element of a list has an index of zero.

## last butlast

In clojure,lastandbutlastare analogs offirstandrestwhich operate at the end of a list. If X is a list, then the following code pairs are identities:

(last X)
(first (reverse X))

(butlast X)
(reverse (rest (reverse X)))

The analogy breaks down in Common Lisp becauselastreturns a list with a single element.

## set-car set-cdr

common lisp:

The following code pairs perform the same operation on the list:

(setf (car l) 3)
(rplaca l 3)

(setf (cdr l) '(4 5 6))
(rplacd l '(4 5 6))

However, they are not identical becauserplacaandrplacdreturn the modified list instead of their 2nd argument.

racket:

Racket provides a separate interpreterplt-r5rsfor an R5RS compliant version of Scheme. Also, the language can be set to R5RS within DrRacket.

emacs lisp:

Also hassetf.

## sort

## assoc

clojure

In Clojure,assocreturns a new association with the specified values replaced:

(def numbers {1 :one 2 :two 3 :three 4 :four})
(def jumble (assoc numbers 1 :uno 3 :drei 4 :quatre))

## getf

racket:

How to implementgetfin Scheme:

(define (getf lst key (default null))
 (cond ((null? lst) default)
 ((null? (cdr lst)) default)
 ((eq? (car lst) key) (cadr lst))
 (else (getf (cddr lst) key default))))

## map

common lisp

The lambda can accept multiple arguments:

(mapcar '+ '(1 2 3) '(4 5 6))

racket

(map + '(1 2 3) '(4 5 6))

clojure

(map + '(1 2 3) '(4 5 6))

emacs lisp

mapcardoes not accept multiple argument lambdas

## filter

common lisp

Also the negative version:

(remove-if (lambda (x) (> x 2)) '(1 2 3))

clojure

Also the negative version:

(remove #(> % 2) '(1 2 3))

emacs lisp

Also has negative version:

(remove-if (λ (x) (> x 2)) '(1 2 3))

## reduce (left fold)

## right fold

clojure:

How to definefoldr:

(defn foldr [f init list] (reduce #(f %2 %1) (reverse list)))

## sublis

How to apply the mapping defined by an associative list to a recursive list.

## dolist

## take

Here is how to definetakefor common lisp or emacs lisp:

(defun take (n l)
 (cond ((< n 0) (error "index negative"))
 ((= n 0) ())
 ((null l) (error "index too large"))
 (t (cons (car l) (take (- n 1) (cdr l))))))

## drop

## push and pop

racket:

Here is an implementation ofpushandpopin Racket using boxes:

(define (push x a-list)
 (set-box! a-list (cons x (unbox a-list))))

(define (pop a-list)
 (let ((result (first (unbox a-list))))
 (set-box! a-list (rest (unbox a-list)))
 result))

clojure:

Note the in clojure,poponly returns the first element; the original list is left unmodified.

# Fixed-Length Arrays

## vector literal

racket

#(1 2 3)creates an immutable vect.(vector 1 2 3)creates a mutable vector.

## vector access

## set vector element

racket

vector-set!throws an error if called on an immutable vector.

## vector to list

## list to vector

## abstract sequence

Lists and vectors support the same operations; the only difference is the speed at which the operations can be performed. It is a convenience for the developer if functions that perform the operations have the same name; i.e. if lists and vectors are members of an abstract sequence type. Clojure has gone furthest in this direction, making all the customary list functions work on vectors as well. In common lisp and emacs lisp, some of the list functions also work on vectors, and some don't. In Scheme none of the list functions work on vectors.

## sequence data types

The containers that respond to sequence functions.

## sequence predicate

## list functions usable on sequences

## make-array

In Lisp terminology, both arrays and vectors refer to collections which are of fixed size; vectors are arrays with rank 1. Only common lisp supports arrays with rank greater than 1.

## array access

## set array element

## array dimensions

array-rankreturns the number of indices required to specify an element in the array.array-dimensionsreturns the size of the array; the number of cells is the product of the elements of the list.

## range

## list comprehension

# Dictionaries

Lisp has a tradition of using lists of pairs for dictionaries. The data structures in this section are implemented using hash tables.

racket:

In addition to hash tables there are a set of functions which work with any dictionary type, which in Racket include hash tables, lists of cons cell pairs, and vectors. When a vector is treated as a dictionary, the value is an element and the key is the integer index of the element.

clojure:

There are three dictionary types which can be used with the functions described in this section:

constructor

type

(hash-map "t" 1 "f" 0)

clojure.lang.PersistentHashMap

(array-map "t" 1 "f" 0)

clojure.lang.PersistentArrayMap

(zipmap '("t" "f") '(1 0))

clojure.lang.PersistentArrayMap

(sorted-map "t" 1 "f" 0)

clojure.lang.PersistentTreeMap

(sorted-map-by #(< %1 %2) "t" 1 "f" 0)

clojure.lang.PersistentTreeMap

# literal

The syntax for a dictionary literal.

# constructor

The constructor for a dictionary.

racket:

The constructors useequal?to test for equality of the two keys.

There are also constructors which useeq?oreqv?to test keys:hasheq,hasheqv,make-immutable-hasheq,make-immutable-hasheqv.

# predicate

How to test whether a value is a dictionary.

# size

How to get the number of keys stored in the dictionary.

# lookup

How to look up the value associated with a key.

# update

How to insert a key-value pair or replace the value stored with an existing key.

# missing key behavior

What happens when a lookup is performed on a key not in the dictionary.

racket:

How to handle the error and return a null when the key is not found:

(with-handlers ((exn:fail? (lambda (e) null))) (get h "goodbye"))

# is key present

How to check whether a key exists in a dictionary.

# delete

How to remove a key and its associated value from a dictionary.

# merge

How to merge two dictionaries.

# invert

How to turn a dictionary into its inverse. If a key 'foo' is mapped to value 'bar' by a dictionary, then its inverse will map the key 'bar' to the value 'foo'.

If multiple keys are mapped to the same value in the original dictionary, some of the keys will be discarded in the inverse.

# iterate

How to iterate over the key-value pairs in a dictionary.

# keys and values as lists

How to get the keys or the values in a dictionary as lists.

# User-Defined Types

## defstruct

## struct

## struct getter

## struct setter

## struct predicate

# Functions

## let, let*

Traditionallyletperforms its assignments in parallel andlet*serially.

clojure

In Clojure,letandlet*are synonyms and both perform serial assignment.

emacs

Note thatletuses dynamic scope. Uselexical-letfor lexical scope:

ELISP> (let ((x 3)) (defun get-x () x))
get-x
ELISP> (get-x)
*** Eval error *** Symbol's value as variable is void: x
ELISP> (let ((x 4)) (get-x))
4
ELISP> (lexical-let ((x 3)) (defun get-x-2 () x))
get-x-2
ELISP> (get-x-2)
3
ELISP> (lexical-let ((x 4)) (get-x-2))
3

## define function

## optional argument

## variable number of arguments

## default value

## named parameter

common lisp:

In common lisp, named parameters are optional. Named values can be assigned default values:

 (defun logarithm (&key number (base 10)) (/ (log number) (log base)))

If a named parameter is not provided at invocation and has not been assigned a default value, then it is set tonil.

racket:

How to Implement Named Parameters in Scheme

emacs lisp:

In emacs lisp named parameters are mandatory. A runtime error results in they are not provided when the function is invoked.

## tail call optimization

common lisp:

The ANSI Common Lisp specification does not require an implementation to perform tail call optimization.

## get docstring

How to get the documentation string for a function.

common lisp:

describereturns the documentation string with additional information such as the function signature. To get just the documentation string use this:

(documentation #'mapcar 'function)

## define function with docstring

How to define a function that has a documentation string.

## apropos and documentation search

How to search definitions and documentation.

Apropos takes a pattern and returns all defined symbol names which match the pattern.

clojure:

aproposreturns matching symbol names as a list.

find-docsearches all documentation strings and writes any which match to standard out.

Bothaproposandfind-doccan take a string or a regular expression as an argument.

emacs lisp:

aproposdisplays the documentation for matching definitions in the*Apropos*buffer. The argument is a string but will be treated as a regular expression.

# Execution Control

## progn

prognand its equivalents in other dialects returns the value of the last expression. Common Lisp and Emacs Lisp also haveprog1andprog2for returning the value of the 1st or 2nd expression.

## loop

## do

## dotimes

## if

## when

# Exceptions

## error

## handle error

racket:

Callingerrorraises an exception of type exn:fail

emacs:

In the example:

(condition-case nil (error "failed") (error (message "caught error") nil))

the 2nd argument tocondition-caseis the code which might raise an error, and the 3rd argument is the error handler. The error handler starts with condition to be caught. The lastnilis the return value of the entirecondition-caseexpression.

An error cannot be handled by catch. An uncaught throw will generate an error, which can be handled by a condition-case error handler.

## define exception

How to define a custom exception with a payload.

common lisp:

The :report clause is not necessary. If defined it will be displayed if the exception is handled by the lisp debugger.

## throw exception

emacs:

The 1st argument of an emacsthrowexpression identifies the type of exception, and the 2nd argument will be the return value of thecatchexpression that catches the exception.

## catch exception

emacs

The followingcatchexpression will returnnil:

(catch 'failed (throw 'failed nil) t)

## restart case

## invoke restart

## finally clause

racket:

* Unwind-protect vs. ContinuationsKent Pitman
* Unwind-protect in Portable SchemeDorai Sitiram

clojure:

Here is an optional technique for making sure that a file handle is closed:

(with-open [#^PrintWriter w (writer f)] (.print w content))

## lazy evaluation

## continuations

# Streams

## standard file handles

## end-of-file behavior

## read line from stdin

## chomp

## write line to stdout

## write formatted string to stdout

racket

printfprints to stdout.formatreturns a string.

emacs lisp

Theformatstatement returns the generated string. When used for i/o, it prints in the emacs minibuffer.

## open file for reading

## open file for writing

## open file for appending

## close file

## close file implicitly

## read line

## iterate over file by line

## read file into array of strings

## read file into string

## write string

## write line

## flush filehandle

# Emacs Buffers

# Files

## file test, regular file test

## file size

## is file readable, writable, executable

## set file permissions

## copy file, remove file, rename file

## create symlink, symlink test, get target

## temporary file

## in memory file

# Directories

## build pathname

How to build a file pathname from components.

## dirname and basename

How to extract the directory portion of a pathname; how to extract the non-directory portion.

## absolute pathname

How to get the get the absolute pathname for a pathname. If the pathname is relative the current working directory will be appended.

## iterate over a directory by file

How to iterate over the files in a directory.

## make directory

How to create a directory, including any parents directories specified in the path.

## recursive copy

How to copy a directory and its contents.

## remove empty directory

How to remove an empty directory.

## remove directory and its contents

How to remove a directory and its contents.

## directory test

How to test whether a directory exists.

# Processes and Environment

## external command

## command line arguments

emacs

The global variablescommand-line-argsandargvare set when emacs is run in shebang mode: i.e. with the —script option.command-line-argscontains the pathname used to invoke emacs, as well as any options processed by emacs at startup, in addition to any additional arguments.argvonly contains the additional arguments.

## environment variables

# Libraries and Namespaces

## loading a file

How to load a file and evaluate the top level expressions.

common lisp

Does not display the result of any evaluations.

racket

Displays the result of the last evaluation.

## loading a library

# Objects

## define class

## make instance

## read attribute

## write attribute

## define method

## invoke method

## define subclass

## universal superclass

## multiple inheritance

# Lisp Macros

## backquote and comma

## defmacro

## defmacro-backquote

## macro predicate

## macroexpand

macroexpandrecursively expands a sexp until the head is no longer a macro. It does not expand arguments that are macros.

common lisp

Common lisp also hasmacroexpand-1, which will non-recursively expand a macro once. The head of the expansion may thus be a macro.

clojure

Clojure also hasmacroexpand-1. See above for an example of use.

emacs lisp

Emacs hasmacroexpand-all, which will recursively expand a sexp until head and arguments are free of macros.

## splice quote

## recursive macro

## hygienic

Does the language have macros whose expansions are guaranteed not to introduce name collisions.

## local values

# Reflection

## type-of

How to get the data type of the entity referred to by a symbol.

# Java Interoperation

## version used on jvm

## extra libraries used

racket:

The srfi-1 library brings in a common list functions which Kawa does not make available by default. SeeSRFI.

## new

## method

## class method

## chain

## import

## to java array

# Common Lisp

ANSI SpecificationSBCL User ManualQuicklisp

For a package manager we use Quicklisp. Here is how to install it and use it to load thecl-ppcrelibrary:

$ curl -O http://beta.quicklisp.org/quicklisp.lisp
$ sbcl
* (load "quicklisp.lisp")
* (quicklisp-quickstart:install)
* (ql:quickload "cl-ppcre")
* (cl-ppcre:all-matches "foo" "foo bar")

Quicklisp creates aquicklispdirectory in the user's home directory. Once quicklisp is downloaded and installed, it can be used like this:

$ sbcl
* (load "~/quicklisp/setup.lisp")
* (ql:quickload "cl-ppcre")
* (cl-ppcre:all-matches "foo" "foo bar")

One can ensure that Quicklisp is automatically loaded at startup by putting the load command into the.sbclrcfile:

$ cat ~/.sbclrc
(load "~/quicklisp/setup.lisp")

# Racket

Guide: RacketReference: RacketPLaneT: Racket Packages

Racket ships with a large number of libraries in thecollectsdirectory of the installation which can be loaded with therequirecommand, which takes a raw symbol which is the relative pathname from thecollectsdirectory to the file, not including the.rktsuffix. The Racket 5.1 distribution includes 50 SRFI libraries.

Racket also has a built in package management system. Browse thelist of available packages. To install a package, click through to the detail page for the package and get therequirestring to load it. If therequirestring is executed by Racket, the library will be downloaded somewhere in the user's home directory. When I ran this on my Mac

$ racket
> (require (planet "spgsql.rkt" ("schematics" "spgsql.plt" 2 3)))

the files for the PostgreSQL database bindings were installed in~/Library/Racket.

# Clojure

Clojure ReferenceClojure Cheat Sheet

## Calling Java

Here are the basics of calling Java code:

(def rnd (new java.util.Random)) ; create Java object
(. rnd nextFloat) ; invoke method on object
(. rnd nextInt 10) ; invoke method with argument
(. Math PI) ; static member
(import '(java.util Random)) ; import

Clojure automatically imports everything in java.lang.

There are shortcuts for the above syntax:

(Random.)
(new Random)

Math/PI
(. Math PI)

(.nextInt rnd)
(. rnd nextInt)

Because they are primitive types and not objects, Clojure provides functions specific to Java arrays:

(make-array CLASS LEN)
(make-array CLASS DIM & DIMS)
(aset ARY IDX VAL)
(aset ARY IDX_DIM1 IDX_DIM2 ... VAL)
(aget ARY IDX)
(aget ARY IDX_DIM1 IDX_DIM2 ...)
(alength JARY)
(to-array SEQ)
(into-array TYPE SEQ)
(amap ARY I COPY EXPR)
(areduce ARY IDX COPY INIT EXPR )

# Emacs Lisp

GNU Emacs ManualGNU Emacs Lisp Reference Manual

To get an introduction to Emacs Lisp Programming from within Emacs use

 C-h i m Emacs Lisp Intro

RunM-x lisp-interaction-modeto put Emacs in lisp interaction mode. In lisp interaction mode the commandC-x ewill evaluate the s-expression on the current line.M-x eval-bufferwill evaluate the entire buffer.

Use lisp interaction mode to define functions which can be called from Emacs. The following defines a function calleddired-emacs-lispfor browsing the Emacs Lisp directory:

(defun dired-emacs-lisp ()
 "Open the Emacs Lisp directory in dired."
 (interactive)
 (dired "/Applications/Emacs.app/Contents/Resources/lisp"))

The directory is hard-coded into the function and may be different on your system. Once defined the function can be invoked withM-x dired-emacs-lisp. Not all Lisp functions can be called in this manner. Those that can are calledcommands. The body of a command has an optional documentation string, followed by a call tointeractive, followed by the code which executes when the command is invoked. The documentation string can be accessed from Emacs by runningM-x describe-functionand entering the name of the function when prompted.

The call tointeractiveis what makes a Lisp function a command. It can takes optional arguments. UseM-x describe-functiononinteractiveto see a description of these arguments.

To bind the command to the keyC-c lrun the following in Lisp interaction mode:

(global-set-key "\C-cl" 'dired-emacs-lisp)

If it is desired to have the above command and key binding always available when Emacs starts up, put them in~/.emacs.d/init.el.
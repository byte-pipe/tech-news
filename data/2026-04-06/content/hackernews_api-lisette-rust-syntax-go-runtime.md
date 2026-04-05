---
title: Lisette — Rust syntax, Go runtime
url: https://lisette.run/
site_name: hackernews_api
content_file: hackernews_api-lisette-rust-syntax-go-runtime
fetched_at: '2026-04-06T01:01:24.853964'
original_url: https://lisette.run/
author: jspdown
date: '2026-04-05'
description: Little language inspired by Rust that compiles to Go.
tags:
- hackernews
- trending
---

# Lisettea little
 languageinspired byRustthat compiles toGo

Algebraic data types · Pattern matching·No nil·Hindley-Milner type system· Immutable by defaultInteroperability with Go's ecosystem

>
 cargo
 install lisette

import
 
"go:fmt"

import
 
"go:io"

import
 
"go:os"

fn
 
load_config
(
path
:
 
string
)
 
->
 
Result
<
Cfg
,
 
error
>
 
{

 
let
 
file
 
=
 
os
.
Open
(
path
)?

 
defer
 
file
.
Close
()

 
let
 
data
 
=
 
io
.
ReadAll
(
file
)?

 
parse_yaml
(
data
)

}

fn
 
main
()
 
{

 
match
 
load_config
(
"app.yaml"
)
 
{

 
Ok
(
config
)
 
=>
 
start
(
config
),

 
Err
(
e
)
 
=>
 
fmt
.
Println
(
"error:"
,
 
e
),

 
}

}

## Familiar

Syntactically similar to Rust

Enums & pattern matching

enum
 
Message
 
{

 
Ready
,

 
Write
(
string
),

 
Move
 
{
 
x
:
 
int
,
 
y
:
 
int
 
},

}

fn
 
handle
(
msg
:
 
Message
)
 
->
 
string
 
{

 
match
 
msg
 
{

 
Message
.
Ready
 
=>
 
"ready"
,

 
Message
.
Write
(
text
)
 
=>
 
f
"wrote: 
{
text
}
"
,

 
Message
.
Move
 
{
 
x
,
 
y
 
}
 
=>
 
f
"move to (
{
x
}
, 
{
y
}
)"
,

 
}

}

Structs & impl blocks

import
 
"go:math"

struct
 
Point
 
{

 
x
:
 
float64
,

 
y
:
 
float64
,

}

impl
 
Point
 
{

 
fn
 
distance
(
self
,
 
other
:
 
Point
)
 
->
 
float64
 
{

 
let
 
(
dx
,
 
dy
)
 
=
 
(
self
.
x
 
-
 
other
.
x
,
 
self
.
y
 
-
 
other
.
y
)

 
math
.
Sqrt
(
dx
*
dx
 
+
 
dy
*
dy
)

 
}

}

Expression oriented

fn
 
describe
(
score
:
 
int
)
 
->
 
string
 
{

 
let
 
grade
 
=
 
if
 
score
 
>=
 
90
 
{

 
"A"

 
}
 
else
 
if
 
score
 
>=
 
70
 
{

 
"B"

 
}
 
else
 
{

 
"C"

 
}

 
let
 
stars
 
=
 
{

 
let
 
count
 
=
 
score
 
/
 
20

 
strings
.
Repeat
(
"*"
,
 
count
)

 
}

 
f
"
{
grade
}
 
{
stars
}
"

}

Chaining and lambdas

fn
 
server_url
()
 
->
 
string
 
{

 
let
 
scheme
 
=
 
os
.
LookupEnv
(
"HTTPS"
)

 
.
filter
(|
s
|
 
s
 
==
 
"1"
)

 
.
map
(|
_
|
 
"https"
)

 
.
unwrap_or
(
"http"
)

 
let
 
host
 
=
 
os
.
LookupEnv
(
"HOST"
)

 
.
map
(|
s
|
 
strings
.
TrimSpace
(
s
))

 
.
filter
(|
s
|
 
s
.
length
()
 
>
 
0
)

 
.
unwrap_or
(
"localhost"
)

 
let
 
port
 
=
 
os
.
LookupEnv
(
"PORT"
)

 
.
unwrap_or
(
"8080"
)

 
scheme
 
+
 
"://"
 
+
 
host
 
+
 
":"
 
+
 
port

}

Interfaces & generics

interface
 
Metric
 
{

 
fn
 
label
(
self
)
 
->
 
string

 
fn
 
value
(
self
)
 
->
 
float64

}

fn
 
report
(
metrics
:
 
Slice
<
Metric
>)
 
{

 
for
 
m
 
in
 
metrics
 
{

 
fmt
.
Println
(
m
.
label
(),
 
m
.
value
())

 
}

}

fn
 
max
<
T
:
 
Metric
>(
metrics
:
 
Slice
<
T
>)
 
->
 
T
 
{

 
metrics
.
fold
(
metrics
[
0
],
 
|
a
,
 
b
|

 
if
 
a
.
value
()
 
>
 
b
.
value
()
 
{
 
a
 
}
 
else
 
{
 
b
 
}

 
)

}

if let & let else

type
 
Headers
 
=
 
Map
<
string
,
 
string
>

fn
 
handle_headers
(
h
:
 
Headers
)
 
->
 
Result
<
()
,
 
string
>
 
{

 
if
 
let
 
Some
(
token
)
 
=
 
h
.
get
(
"Authorization"
)
 
{

 
let
 
user
 
=
 
authenticate
(
token
)?

 
authorize
(
user
)?

 
}
 
else
 
{

 
return
 
Err
(
"missing credentials"
)

 
}

 
let
 
Some
(
id
)
 
=
 
h
.
get
(
"X-Request-ID"
)
 
else
 
{

 
return
 
Err
(
"missing request ID"
)

 
}

 
process
(
id
)

}

## Safe

Go runtime issues, caught at compile time

 
🔴 
match
 is not exhaustive

 ╭─[example.lis:4:3]
 
2
 │ enum Severity { Low, High, Critical }
 
3
 │ fn should_alert(s: Severity) -> bool {
 
4
 │ match s {
 · 
 ───┬───

 · 
╰── not all patterns covered

 
5
 │ Severity.Low => false,
 
6
 │ Severity.High => true,
 
7
 │ }
 ╰────
 
help: Handle the missing case 
Severity.Critical
,
 e.g. 
Severity.Critical => { ... }

 
🔴 
nil
 is not supported

 ╭─[users.lis:3:12]
 
1
 │ fn find(name: string) -> Option<User> {
 
2
 │ if name.is_empty() {
 
3
 │ return nil
 · 
─┬─

 · 
╰── does not exist

 
4
 │ }
 
5
 │ db.lookup(name)
 
6
 │ }
 ╰────
 
help: Absence is encoded with 
Option<T>
 in Lisette.
 Use 
None
 to represent absent values

 
🟡 
Result
 is silently discarded

 ╭─[files.lis:7:3]
 
5
 │ fn cleanup() -> Result<(), error> {
 
6
 │ os.RemoveAll("cache_dir")?
 
7
 │ os.Remove("temp.txt")
 · 
 ──────────┬──────────

 · 
╰── failure will go unnoticed

 
8
 │ }
 ╰────
 
help: Handle this 
Result
 with 
?
 or 
match
, or
 explicitly discard it with 
let _ = ...

 
🟡 Private type 
Config
 in public API

 ╭─[config.lis:6:24]
 
5
 │ struct Config { host: string, port: int }
 
6
 │ pub fn new_config() -> Config {
 · 
 ───┬──

 · 
╰── private

 
7
 │ Config { host: "localhost", port: 8080 }
 ╰────
 
help: 
Config
 is private but exposed by 
new_config
,
 which is public. Add 
pub
 to the private type
 or remove it from the public API

 
🔴 Immutable argument passed to 
mut
 parameter

 ╭─[sort.lis:5:13]
 
4
 │ let nums = [3, 1, 2]
 
5
 │ sort.Ints(nums)
 · 
 ──┬─

 · 
╰── expected mutable, found immutable

 
6
 │ }
 ╰────
 
help: Bindings in Lisette are immutable by default.
 Use 
let mut nums = ...
 to allow mutation

 
🔴 Struct 
Server
 is missing fields

 ╭─[server.lis:10:11]
 
9
 │ fn start(mux: http.Handler) {
 
10
 │ let s = Server { handler: mux }
 · 
───┬──

 · 
╰── missing fields: 
db
, 
logger

 
11
 │ http.ListenAndServe(":8080", s.handler)
 
12
 │ }
 ╰────
 
help: Initialize all fields in this struct literal

LSP support for:

 VSCode
 

 Neovim
 

 Zed
 

## Ergonomic

Designed for interoperability with Go

Pipeline operator

import
 
"go:strings"

fn
 
slugify
(
input
:
 
string
)
 
->
 
string
 
{

 
input

 
|>
 
strings
.
TrimSpace

 
|>
 
strings
.
ToLower

 
|>
 
strings
.
ReplaceAll
(
" "
,
 
"-"
)

}

slugify
(
" Hello World "
)
 
// => "hello-world"

Try blocks

fn
 
load_config
()
 
->
 
Config
 
{

 
let
 
result
 
=
 
try
 
{

 
let
 
data
 
=
 
os
.
ReadFile
(
"app.toml"
)?

 
parse_toml
(
data
)?

 
}

 
match
 
result
 
{

 
Ok
(
config
)
 
=>
 
config
,

 
Err
(
_
)
 
=>
 
Config
.
default
(),

 
}

}

Concurrency

fn
 
fetch_primary
()
 
->
 
string
 
{
 
...
 
}

fn
 
fetch_replica
()
 
->
 
string
 
{
 
...
 
}

let
 
ch1
 
=
 
Channel
.
new
<
string
>()

let
 
ch2
 
=
 
Channel
.
new
<
string
>()

task
 
{
 
ch1
.
send
(
fetch_primary
())
 
}
 
// goroutine

task
 
{
 
ch2
.
send
(
fetch_replica
())
 
}
 
// goroutine

let
 
quickest
 
=
 
select
 
{

 
match
 
ch1
.
receive
()
 
{

 
Some
(
v
)
 
=>
 
v
,

 
None
 
=>
 
"closed"
,

 
},

 
match
 
ch2
.
receive
()
 
{

 
Some
(
v
)
 
=>
 
v
,

 
None
 
=>
 
"closed"
,

 
},

}

Serialization attributes

#[json(camel_case)]

struct
 
UserProfile
 
{

 
user_name
:
 
string
,
 
// => `json:"userName"`

 
#[json("userID")]

 
account_id
:
 
int
,
 
// => `json:"userID"`

 
#[json(omitempty)]

 
bio
:
 
Option
<
string
>,
 
// => `json:"bio,omitempty"`

 
#[json(string)]

 
score
:
 
int64
,
 
// => `json:"score,string"`

 
#[tag("validate", "required")]

 
email
:
 
string
,
 
// => `validate:"required"`

 
#[json(skip)]

 
internal_id
:
 
int
,
 
// => `json:"-"`

}

Panic recovery

fn
 
safe_divide
(
a
:
 
int
,
 
b
:
 
int
)
 
->
 
Result
<
int
,
 
string
>
 
{

 
let
 
result
 
=
 
recover
 
{
 
a
 
/
 
b
 
}

 
// => Result<int, PanicValue>

 
result
.
map_err
(|
pv
|
 
pv
.
message
())

}

match
 
safe_divide
(
10
,
 0
)
 
{

 
Ok
(
v
)
 
=>
 
fmt
.
Println
(
v
),

 
Err
(
e
)
 
=>
 
fmt
.
Println
(
e
),

}

Deferral

fn
 
run
(
query
:
 
string
)
 
->
 
Result
<
()
,
 
error
>
 
{

 
let
 
db
 
=
 
connect
()?

 
defer
 
db
.
Close
()

 
let
 
tx
 
=
 
db
.
Begin
()?

 
defer
 
tx
.
Rollback
()

 
tx
.
Exec
(
query
)?

 
tx
.
Commit
()

}

## Transparent

Compiles to understandable Go

Lisette

fn
 
classify
(
opt
:
 
Option
<
int
>)
 
->
 
string
 
{

 
match
 
opt
 
{

 
Some
(
x
)
 
if
 
x
 
>
 
0
 
=>
 
"positive"
,

 
Some
(
x
)
 
if
 
x
 
<
 
0
 
=>
 
"negative"
,

 
Some
(
_
)
 
=>
 
"zero"
,

 
None
 
=>
 
"none"
,

 
}

}

Compiled Go

func
 
classify
(
opt
 
lisette.Option
[
int
])
 
string
 
{

 
if
 
opt
.
Tag
 
==
 
lisette
.
OptionSome
 
{

 
x
 
:=
 
opt
.
SomeVal

 
if
 
x
 
>
 
0
 
{

 
return
 
"positive"

 
}

 
if
 
x
 
<
 
0
 
{

 
return
 
"negative"

 
}

 
return
 
"zero"

 
}

 
return
 
"none"

}

Lisette

fn
 
combine
()
 
->
 
Result
<
int
,
 
string
>
 
{

 
let
 
x
 
=
 
first
()?

 
let
 
y
 
=
 
second
()?

 
Ok
(
x
 
+
 
y
)

}

Compiled Go

func
 
combine
()
 
lisette.Result
[
int
,
 
string
]
 
{

 
check_1
 
:=
 
first
()

 
if
 
check_1
.
Tag
 
!=
 
lisette
.
ResultOk
 
{

 
return
 
lisette
.
MakeResultErr
[
int
,
 
string
](

 
check_1
.
ErrVal
,

 
)

 
}

 
x
 
:=
 
check_1
.
OkVal

 
check_2
 
:=
 
second
()

 
if
 
check_2
.
Tag
 
!=
 
lisette
.
ResultOk
 
{

 
return
 
lisette
.
MakeResultErr
[
int
,
 
string
](

 
check_2
.
ErrVal
,

 
)

 
}

 
y
 
:=
 
check_2
.
OkVal

 
return
 
lisette
.
MakeResultOk
[
int
,
 
string
](
x
 
+
 
y
)

}

## Learn more

By visiting the repository:github.com/ivov/lisette
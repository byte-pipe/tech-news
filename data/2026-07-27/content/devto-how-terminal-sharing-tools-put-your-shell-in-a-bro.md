---
title: How terminal-sharing tools put your shell in a browser - DEV Community
url: https://dev.to/lovestaco/how-terminal-sharing-tools-put-your-shell-in-a-browser-328
site_name: devto
content_file: devto-how-terminal-sharing-tools-put-your-shell-in-a-bro
fetched_at: '2026-07-27T19:32:59.863375'
original_url: https://dev.to/lovestaco/how-terminal-sharing-tools-put-your-shell-in-a-browser-328
author: Athreya aka Maneshwar
date: '2026-07-26'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with webdev, programming, productivity, cli.
tags: '#webdev, #programming, #productivity, #cli'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star git-lrcto help devs discover the project. Do give it a try and share your feedback.

You have probably done this dance.

You are debugging something on a box, your teammate says "can you just show me", and you end up screen sharing a 4K monitor over a video call so they can squint at 11px monospace text that has been compressed into oatmeal.

There is a better way, and it has existed for years.

Tools likettyd,TermPair, andsshxput your actual terminal in someone else's browser. Real text. Real selection.

Real copy paste.

I got curious about how they pull this off, so I cloned all three and read them.

Turns out they are solving the same problem in three very different ways, and the differences are genuinely interesting.

Let's get shell shocked together.

## what even is a terminal

Before any of the web stuff makes sense, you need one concept: thepseudoterminal, or PTY.

When you runbashin your terminal app, bash is not talking to your keyboard.

It is talking to a file.

Specifically, a pair of linked file descriptors that the kernel sets up to impersonate an actual physical teletype from 1965.

One end is themaster, one end is theslave.

Your terminal emulator holds the master. Bash holds the slave, and bash has no idea it is being catfished.

Anything you write to the master shows up as keyboard input to bash. Anything bash prints comes back out of the master.

That is the entire trick.

Terminal sharing tools are just programs that hold the master end and forward those bytes somewhere more interesting than a window on your laptop.

Here is sshx doing exactly that, incrates/sshx/src/terminal/unix.rs:

use
 
nix
::
pty
::{
self
,
 
Winsize
};

use
 
nix
::
unistd
::{
execvp
,
 
fork
,
 
ForkResult
,
 
Pid
};

use
 
nix
::
libc
::{
login_tty
,
 
TIOCGWINSZ
,
 
TIOCSWINSZ
};

pub
 
struct
 
Terminal
 
{

 
child
:
 
Pid
,

 
master_read
:
 
File
,

 
master_write
:
 
File
,

}

Enter fullscreen mode

Exit fullscreen mode

Fork, calllogin_ttyin the child so the slave fd becomes its controlling terminal,execvpthe shell, and keep the master in the parent.

ttyd does the same thing in C.

TermPair does it in Rust.

Three codebases, one ancient POSIX handshake.

Everyone takes the same fork in the road.

Oh, andTIOCSWINSZis how the terminal size gets set.

When you resize your browser window, that ioctl is what eventually fires so thatvimredraws correctly instead of smearing itself across the screen.

Resize handling is not a nice-to-have here, it is load bearing.

## The simplest possible version: ttyd

ttyd is the "no, seriously, that's it" implementation.

One C process, built on libwebsockets and libuv.

Itisthe web server and itisthe terminal host.

There is no relay, no separate client, no key exchange.

The protocol is beautifully dumb. Fromsrc/server.h:

// client -> server

#define INPUT '0'
#define RESIZE_TERMINAL '1'
#define PAUSE '2'
#define RESUME '3'
#define JSON_DATA '{'

// server -> client

#define OUTPUT '0'
#define SET_WINDOW_TITLE '1'
#define SET_PREFERENCES '2'

Enter fullscreen mode

Exit fullscreen mode

Single byte opcode, then payload. That is the whole wire format.

'0'plus your keystrokes goes up,'0'plus terminal output comes down.

PAUSEandRESUMEexist because a fast-scrollingcatof a huge file can outrun the browser, so the client can apply backpressure instead of dying.

Here is the full round trip:

Two details worth stealing from ttyd:

The frontend ships inside the binary.

The Preact and xterm.js app inhtml/gets bundled, gzipped, and inlined intosrc/html.has a C byte array.

You get a single executable with no static file directory to misplace.

The tradeoff is that touching a.tsxfile means runningyarn run inlineand then rebuilding the C binary, which surprises people exactly once.

It is read only by default.You have to pass-Wto let viewers actually type.

ttyd 
-p
 7681 
-c
 user:pass 
-O
 
-W
 bash

Enter fullscreen mode

Exit fullscreen mode

That said, ttyd's threat model is "you trust the server, because the server is your machine."

The bytes are plaintext over the wire unless you turn on TLS.

Which brings us to the interesting question.

## What if you don't trust the server?

The moment you want to share a terminal with someone across the internet, you need a middleman with a public IP. And now that middleman can read everything you type.

TermPair and sshx both took that guy's advice.

They make the server ablind relay: it routes ciphertext between the terminal host and the browsers, and it structurally cannot decrypt any of it.

Green means "can read your terminal."

The whole game is shrinking the green.

## The key delivery trick

So the client encrypts and the browser decrypts. Both need the key.

The server must not have it. But the browser gets its entire existence from the server.

How do you hand a secret to a page that the server itself sent you?

The answer is a URL fragment.

https://sharemyclau.de/s/abc123#key-goes-right-here

Enter fullscreen mode

Exit fullscreen mode

Everything after#isnever sent in the HTTP request.

It is a client side construct.

Browsers use it for anchor scrolling and hash routing, and it stays in the address bar and in JavaScript'slocation.hashwhile the server sees only/s/abc123.

So you share one link, the recipient's browser reads the key out of its own address bar, and the relay in the middle sees an opaque session ID and a stream of noise.

Here is the flow end to end:

The security of this rests entirely on the link. Anyone who gets the full URL gets the session.

Don't paste it in a public Slack channel and then act surprised.

## Two flavors of crypto

TermPair and sshx both do AES, but they made different calls, and the differences are instructive.

### TermPair: AES-128-GCM with counter IVs

Fromcrates/termpair-common/src/encryption.rs:

pub
 
fn
 
iv_from_count
(
count
:
 
u64
)
 
->
 
[
u8
;
 
IV_LENGTH
]
 
{

 
let
 
mut
 
iv
 
=
 
[
0u8
;
 
IV_LENGTH
];

 
let
 
bytes
 
=
 
count
.to_le_bytes
();

 
iv
[
..
bytes
.len
()]
.copy_from_slice
(
&
bytes
);

 
iv

}

Enter fullscreen mode

Exit fullscreen mode

GCM gives you authentication for free, so a tampered message fails to decrypt rather than quietly turning into garbage that your terminal then interprets as escape sequences.

The IV is a plain message counter, which is fine and correctas long as you never reuse one with the same key.

Nonce reuse in GCM is not a "slightly weaker" situation, it is a "here is your key, thanks for playing" situation.

Which is whyconstants.rshas this:

pub
 
const
 
ROTATION_THRESHOLD
:
 
u64
 
=
 
1
 
<<
 
20
;

pub
 
const
 
MAX_MESSAGES_PER_KEY
:
 
u64
 
=
 
ROTATION_THRESHOLD
 
*
 
2
;

Enter fullscreen mode

Exit fullscreen mode

After about a million messages, the key rotates.

There is a wholeaes_key_rotationevent in the protocol for it.

Separate keys for terminal output and browser input, plus a bootstrap key for the handshake, so the counter spaces cannot collide.

It is careful work, and the kind of thing that is invisible when it is done right.

### sshx: Argon2 stretched key with AES-CTR

sshx made a different bet. Fromcrates/sshx/src/encrypt.rs, with a comment I really enjoyed:

const
 
SALT
:
 
&
str
 
=

 
"This is a non-random salt for sshx.io, since we want to stretch the security of 83-bit keys!"
;

let
 
hasher
 
=
 
Argon2
::
new
(

 
Algorithm
::
Argon2id
,

 
Version
::
V0x13
,

 
Params
::
new
(
19
 
*
 
1024
,
 
2
,
 
1
,
 
Some
(
16
))
.unwrap
(),

);

Enter fullscreen mode

Exit fullscreen mode

The key in your URL is only 83 bits of entropy, because sshx wants the shareable link to stay short enough to actually paste in chat.

83 bits is not a lot by modern standards, so it runs Argon2id over it with real memory cost parameters. Brute forcing now costs 19MB and real CPU time per guess instead of a nanosecond.

It is a deliberate trade of raw entropy for ergonomics, paid back with a KDF.

Then it uses CTR mode with a clever addressing scheme:

pub
 
fn
 
segment
(
&
self
,
 
stream_num
:
 
u64
,
 
offset
:
 
u64
,
 
data
:
 
&
[
u8
])
 
->
 
Vec
<
u8
>
 
{

 
assert_ne!
(
stream_num
,
 
0
,
 
"stream number must be nonzero"
);
 
// security check

 
let
 
mut
 
iv
 
=
 
[
0
;
 
16
];

 
iv
[
0
..
8
]
.copy_from_slice
(
&
stream_num
.to_be_bytes
());

 
let
 
mut
 
cipher
 
=
 
Aes128Ctr64BE
::
new
(
&
self
.aes_key
.into
(),
 
&
iv
.into
());

 
cipher
.seek
(
offset
);

 
cipher
.apply_keystream
(
&
mut
 
buf
);

 
buf

}

Enter fullscreen mode

Exit fullscreen mode

Because CTR mode is seekable, sshx can encrypt "the bytes at offset N of stream M" without touching anything before them.

That is not a crypto flex, it is an architecture decision: it means a browser that reconnects can say "I have everything up to byte 4096, send me the rest" and the server can serve that from its buffer.

Encryption and resumability designed together.

Theassert_ne!(stream_num, 0)guard is there because stream 0 is used for the encrypted zeros block that proves you have the right key.

Reusing it would mean reusing a keystream.

Nice to see the security check written down instead of assumed.

## The part that makes sshx feel fast

Here is my favorite detail in any of these codebases.

There is a fundamental problem with remote terminals: your keystroke has to go to the server, into the PTY, back out, and back to you before you see the character.

On a 200ms link, typing feels like moving through syrup.

sshx solves this the wayMoshdoes, withpredictive echo. Fromsrc/lib/typeahead.ts:

// A terminal "local echo" or typeahead addon for xterm.js.

//

// This is forked from VSCode's typeahead implementation at

// https://github.com/microsoft/vscode/blob/1.80.1/...

Enter fullscreen mode

Exit fullscreen mode

The client guesses. You pressk, it draws akimmediately (slightly dimmed) while the real round trip happens in the background.

When the server's actual output arrives, it reconciles.

If the guess was right, nothing visibly changes.

If it was wrong, because you were invimor hitting a password prompt, it rolls back.

The tricky part is knowing whennotto predict.

Predicting into a password prompt would echo your password onto the screen, which is a memorable way to lose a friend.

So the addon tracks terminal modes and bails out when it is not confident.

Getting a-head of the output, but politely.

## Sessions, state, and the boring stuff that matters

The last layer is lifecycle. Sessions are long lived, connections are not. Wifi drops. Laptops sleep.

sshx handles this with sequence numbers in the protocol (crates/sshx-core/proto/sshx.proto):

message
 
TerminalData
 
{

 
uint32
 
id
 
=
 
1
;

 
bytes
 
data
 
=
 
2
;

 
uint64
 
seq
 
=
 
3
;
 
// Sequence number of the first byte

}

message
 
SequenceNumbers
 
{

 
map
<
uint32
,
 
uint64
>
 
map
 
=
 
1
;
 
// Active shells and their sequence numbers

}

Enter fullscreen mode

Exit fullscreen mode

Every shell is a stream with a byte offset. On reconnect, the client sends where it left off and the server replays the difference.

Combined with seekable CTR encryption, resume is nearly free.

It also has to decide when to give up on a session:

/// Timeout for a disconnected session to be evicted and closed.

const
 
DISCONNECTED_SESSION_EXPIRY
:
 
Duration
 
=
 
Duration
::
from_secs
(
300
);

Enter fullscreen mode

Exit fullscreen mode

Five minutes without a backend client and the session is closed and dropped from theDashMap. Otherwise every crashed laptop leaks memory forever.

And because sshx runs a globally distributed mesh, session state also goes into Redis viacrates/sshx-server/src/state/mesh.rs, so you can connect to the nearest server rather than always crossing an ocean.

TermPair, meanwhile, caps things with hard limits (MAX_TERMINALS: 200,MAX_BROWSERS_PER_TERMINAL: 50,MAX_WS_MSGS_PER_SEC: 500) which is the sensible answer when you are running one modest box instead of a mesh.

## So which one should you use

Genuinely depends on what you are doing.

ttydif the network is already trusted. Homelab, LAN, behind a VPN, embedded devices, an OpenWrt router. It is one small C binary with no runtime dependencies and it will outlive us all.ttyd -W bashand you are done.

TermPairif you want end to end encryption with a simple mental model and the option to self host the relay. The three-key design with rotation is easy to reason about and the code is small enough to read in an afternoon.

sshxif you want the polished product experience. Multiple terminals on an infinite canvas, other people's cursors moving in real time, predictive echo, global mesh, automatic reconnect. Worth noting the README says self hosting is explicitly not supported, so this is "use sshx.io" rather than "run your own."

## The takeaway

Every one of these tools is, at its core,fork(), a PTY master fd, and a loop that shovels bytes into a WebSocket.

That part is 1970s technology wearing a 2020s hoodie.

Everything else, the encryption, the sequence numbers, the key rotation, the predictive echo, the session eviction, exists to answer one question:how much do you trust the machine in the middle?ttyd says "it's mine, so completely."

TermPair and sshx say "not at all, and here is the math."

Reading three implementations of the same idea side by side is the fastest architecture lesson I have had in a while.

If a concept keeps showing up in every version, it is essential.

If it only shows up in one, it is a product decision.

That distinction is hard to see from a single codebase and obvious from three.

Go clone them.

It is more fun than another framework tutorial, and you will never look atlocation.hashthe same way again.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs — without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Git Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|🇮🇳 हिन्दी|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

GenAI today is arace car without brakes. It accelerates fast -- you describe something, and large blocks of code appear instantly. But AI agentssilently break things: they remove logic, relax constraints, introduce expensive cloud calls, leak credentials, and change behavior -- without telling you. You often find out in production.

git-lrcis your braking system.It hooks intogit commitand runs an AI review on every diffbeforeit lands. 60-second setup. Completely free.

In short, git-lrc helpsPrevent Outages, Breaches, and Technical Debt Before They Happen

At a glance:10 risk categories·100+ failure patterns tracked· every commit…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
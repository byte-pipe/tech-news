---
title: Ruff v0.16.0
url: https://astral.sh/blog/ruff-v0.16.0
site_name: hackernews_api
content_file: hackernews_api-ruff-v0160
fetched_at: '2026-07-26T19:29:35.166502'
original_url: https://astral.sh/blog/ruff-v0.16.0
author: vismit2000
date: '2026-07-26'
description: The next stable version of Ruff is out now.
tags:
- hackernews
- trending
---

Back to blog

July 
 23, 
 2026

##### Brent Westbrook

@
ntBre

Ruff v0.16.0is available now! Install it fromPyPI, or with your package manager of choice:

uv 
tool
 
install
 
ruff@latest

As a reminder:Ruff is an extremely fast Python linter and formatter, written in Rust.Ruff can
be used to replace Black, Flake8 (plus dozens of plugins), isort, pydocstyle, pyupgrade, and more,
all while executing tens or hundreds of times faster than any individual tool.

## Migrating to v0.16#

Ruff v0.16 has a small number of breaking changes, allowing most users to update without significant
changes to code or configuration. The main exception is described below.

### Better default rule set#

Ruff now enables 413 rules by default, up from 59 in previous versions.

Since Ruff's default rule set was last modified inv0.1.0, the
number of rules in Ruff has grown from 708 to 968. Many of these rules catch severe issues,
includingsyntax errorsandimmediate runtime errorsbut were not previously
enabled by default. With the new rule set, Ruff will bring these issues and many others to your
attention without any Ruff configuration. Even if you're already usingselectorextend-select, we hope that this will
draw your attention to helpful rules that you previously hadn't discovered.

The full listing of enabled rules is too long to include here, but you can find it on our newDefault Rulespage in the documentation. A few of the
highlights include rules from the popular flake8-bugbear (B) and pyupgrade (UP) linters, as well
as rules from our ownRUFcategory.

If you want to revert to the old default set, you can easilyselectthe old rules with this
configuration:

[
lint
]

select
 
=
 [
"
E4
"
, 
"
E7
"
, 
"
E9
"
, 
"
F
"
]

We view this work as closely tied to our longstanding goal ofrule recategorization, so look forward to upcoming
developments in this area.

## New features in v0.16#

Ruff v0.16 also includes several newly stabilized features that are highlighted below.

### Markdown code block formatting#

Ruff can now format Python code blocks embedded in Markdown files.

In these files, Ruff v0.16 will formatfenced code blockswith apython,py,python3,py3,pyi, orpyconinfo string.pyiblocks are formatted like stub files,pyconblocks as REPL sessions, and the others use
normal Python file formatting. For example:

# README

Here's an example:

```py

import
 ruff

ruff_binary 
=
 (

 ruff.find_ruff_bin()

)

```

will be reformatted when runningruff format:

This can also be used to formatQuartonotebooks because Ruff still
recognizes the language when surrounded by curly braces (e.g.```{python}). Note that you may
need to configure yourextensionmapping if
your Quarto files use the.qmdextension.

If you need to suppress formatting, you have several options. If you want the suppression comments
to appear in the code block, you can use normalfmt: offandfmt: oncomments within the code
block itself, or you can use similar HTML comments to disable formatting for a whole region of the
document:

# README

<!-- fmt: off -->

```py

x 
=
 
"
this will be suppressed
"

```

<!-- fmt: on -->

To suppress Markdown formatting entirely, you can use the normalextend-excludesetting to exclude all
Markdown files with a glob like*.md.

See thefull documentationfor
more details.

### ruff: ignorecomments offer new suppression features#

Ruff now has its own suppression comment format that can be used on its own line.

In v0.15, the Ruff linter gained a range suppression mechanism through pairedruff: disableandruff: enablecomments, much like thefmt: offandfmt: onpair described above:

# ruff: disable[N803]

def
 
foo
(

 
legacyArg1
,

 
legacyArg2
,

 
legacyArg3
,

 
legacyArg4
,

): 
...

# ruff: enable[N803]

Ruff v0.16 builds on this to add two additionalruffsuppression comments.ruff: ignorecan be
used to suppress a diagnostic on the same line, likenoqa, or on the following logical line:

import
 math 
# ruff: ignore[F401]

# ruff: ignore[N803]

def
 
foo
(

 
legacyArg1
,

 
legacyArg2
,

 
legacyArg3
,

 
legacyArg4
,

): 
...

In this case, the logical line spans the whole function header (fromdefto the colon), so theruff: ignoresuppresses all of the sameN803diagnostics as thedisable/enablepair above.

ruff: file-ignorecomments can be used to suppress diagnostics for the entire file, just likeruff: noqacomments:

# ruff: file-ignore[F401] Allow unused imports in this file

import
 foo

import
 bar

import
 baz

As this example also shows, each of these comment kinds can have an associated "reason" explaining
why they were added, in this caseAllow unused imports in this file.

ruff: ignorecomments can be added automatically with the new--add-ignoreCLI flag, and inpreview, all of theseruffsuppression comments support rule names instead of codes:

❯ 
echo
 
'
import math
'
 
>
 
try.py

❯ 
uvx
 
ruff@latest
 
check
 
--preview
 
--add-ignore
 
try.py

Added 
1
 
ignore
 
comment.

❯ 
cat
 
try.py

import 
math
 
# ruff: ignore[unused-import]

You can find the full specification for all of these comments in thedocumentation.

### Fixes are now shown incheckandformat --checkoutput#

Ruff now shows the diff for linter and formatter fixes when rendering diagnostics.

Both thecheckandformatsubcommands have long supported the--diffflag for showing the
changes introduced by applying fixes withcheck --fixorformat, but this was separate from the
normal output and suppressed the accompanying explanatory diagnostics. In v0.16, available fixes are
now shown as part of the defaultfulloutput format, rendered below thehelpsubdiagnostic:

The same is true forformat --check. Given the following input:

# example.py

if
 
True
:

 
pass

elif
 
False
:

 
pass

The formatter produces:

format --checkalso now supports the full selection of output formats supported by the linter. You
can use this to obtain machine-readable JSON output or produce the formats expected by GitHub and
GitLab to render annotations in CI, as just a couple of examples. See the CLI help ordocumentationfor the full list of supported
formats.

One final note on output formats is that there is a small breaking change to the JSON output in
v0.16. Thefilename,location,end_location,fix.edits[].location, andfix.edits[].end_locationfields may now benullrather than defaulting to the empty string and
row 1, column 1, respectively. This should affect very few of Ruff's existing diagnostics but better
reflects the internal diagnostic representation and may become more common in future rules.

## Rule stabilizations#

The following rules have been stabilized and are no longer inpreview:

* airflow3-incompatible-function-signature(AIR303)
* missing-copyright-notice(CPY001)
* unnecessary-from-float(FURB164)
* sorted-min-max(FURB192)
* implicit-string-concatenation-in-collection-literal(ISC004)
* log-exception-outside-except-handler(LOG004)
* invalid-bool-return-type(PLE0304)
* too-many-positional-arguments(PLR0917)
* stop-iteration-return(PLR1708)
* none-not-at-end-of-union(RUF036)
* access-annotations-from-class-dict(RUF063)
* duplicate-entry-in-dunder-all(RUF068)

## Other behavior stabilizations#

This release also stabilizes some additional behavior, previously only available inpreview mode:

* blind-except(BLE001) is now suppressed when
the exception is logged vialoggingmethods other thancritical,errorandexception.
* future-required-type-annotation(FA102) now checks for additionalPEP 585-compatible APIs, such as those fromcollections.abc.
* f-string-in-get-text-func-call(INT001),format-in-get-text-func-call(INT002), andprintf-in-get-text-func-call(INT003) now check for additional common ways of using thegettextmodule, such as assigning
it tobuiltins._.
* suspicious-url-open-usage(S310) now resolves local string literal bindings to avoid more false positives.
* snmp-insecure-version(S508) andsnmp-weak-cryptography(S509) now
support the recommended API from newer versions of PySNMP.
* typing-text-str-alias(UP019) now
recognizestyping_extensions.Textin addition totyping.Text.

## Thank you!#

Thank you to everyone who provided feedback regarding the changes included in Ruff'spreview modeand to our contributors. It's an honor
building Ruff with you!

View the full changelog onGitHub.

Read more aboutAstral— the company behind Ruff.

Thanks to Zanie Blue, David Peter, Micha Reiser, and Alex Waygood who contributed to this blog
post.
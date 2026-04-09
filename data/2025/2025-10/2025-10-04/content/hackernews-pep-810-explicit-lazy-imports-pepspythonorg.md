---
title: PEP 810 – Explicit lazy imports | peps.python.org
url: https://pep-previews--4622.org.readthedocs.build/pep-0810/
site_name: hackernews
fetched_at: '2025-10-04T11:08:49.559964'
original_url: https://pep-previews--4622.org.readthedocs.build/pep-0810/
author: azhenley
date: '2025-10-04'
description: 'This PEP introduces syntax for lazy imports as an explicit language feature:'
---

# PEP 810 – Explicit lazy imports

Author
:

Pablo Galindo <pablogsal at python.org>,
Germán Méndez Bravo <german.mb at gmail.com>,
Thomas Wouters <thomas at python.org>,
Dino Viehland <dinoviehland at gmail.com>,
Brittany Reynoso <brittanyrey at gmail.com>,
Noah Kim <noahbkim at gmail.com>,
Tim Stumbaugh <me at tjstum.com>

Discussions-To
:

Discourse thread

Status
:

Draft

Type
:

Standards Track

Created
:

02-Oct-2025

Python-Version
:

3.15

Post-History
:

03-Oct-2025

Table of Contents
* Abstract
* Motivation
* RationaleOther design decisions
* Other design decisions
* SpecificationGrammarSyntax restrictionsSemanticsLazy import mechanismReification
* GrammarSyntax restrictions
* Syntax restrictions
* Semantics
* Lazy import mechanism
* Reification
* Reference ImplementationBytecode and adaptive specializationLazy imports filterGlobal lazy imports control
* Bytecode and adaptive specialization
* Lazy imports filter
* Global lazy imports control
* Backwards CompatibilityUnchanged semanticsObservable behavioral shifts (opt-in only)Thread-safety and reificationTyping and tools
* Unchanged semantics
* Observable behavioral shifts (opt-in only)
* Thread-safety and reification
* Typing and tools
* Security Implications
* How to Teach This
* FAQ
* Alternate Implementation IdeasLeveraging a subclass of dictAlternate keyword names
* Leveraging a subclass of dict
* Alternate keyword names
* Rejected IdeasModification of the dict objectPlacing thelazykeyword in the middle of from importsPlacing thelazykeyword at the end of import statementsReturning a proxy dict fromglobals()Reifying lazy imports whenglobals()is called
* Modification of the dict object
* Placing thelazykeyword in the middle of from imports
* Placing thelazykeyword at the end of import statements
* Returning a proxy dict fromglobals()
* Reifying lazy imports whenglobals()is called
* Acknowledgements
* Footnotes
* Copyright

## Abstract

This PEP introduces syntax for lazy imports as an explicit language feature:

lazy

import

json

lazy

from

json

import

dumps

Lazy imports defer the loading and execution of a module until the first time
the imported name is used, in contrast to ‘normal’ imports, which eagerly load
and execute a module at the point of the import statement.

By allowing developers to mark individual imports as lazy with explicit
syntax, Python programs can reduce startup time, memory usage, and unnecessary
work. This is particularly beneficial for command-line tools, test suites, and
applications with large dependency graphs.

This proposal preserves full backwards compatibility: normal import statements
remain unchanged, and lazy imports are enabled only where explicitly
requested.

## Motivation

The dominant convention in Python code is to place all imports at the module
level, typically at the beginning of the file. This avoids repetition, makes
import dependencies clear and minimizes runtime overhead by only evaluating an
import statement once per module.

A major drawback with this approach is that importing the first module for an
execution of Python (the “main” module) often triggers an immediate cascade of
imports, and optimistically loads many dependencies that may never be used.
The effect is especially costly for command-line tools with multiple
subcommands, where even running the command with--helpcan load dozens of
unnecessary modules and take several seconds. This basic example demonstrates
what must be loaded just to get helpful feedback to the user on how to run the
program at all. Inefficiently, the user incurs this overhead again when they
figure out the command they want and invoke the program “for real.”

A somewhat common way to delay imports is to move the imports into functions
(inline imports), but this practice requires more work to implement and
maintain, and can be subverted by a single inadvertent top-level import.
Additionally, it obfuscates the full set of dependencies for a module.
Analysis of the Python standard library shows that approximately 17% of all
imports outside tests (nearly 3500 total imports across 730 files) are already
placed inside functions or methods specifically to defer their execution. This
demonstrates that developers are already manually implementing lazy imports in
performance-sensitive code, but doing so requires scattering imports
throughout the codebase and makes the full dependency graph harder to
understand at a glance.

The standard library provides theLazyLoaderclass to
solve some of these inefficiency problems. It permits imports at the module
level to workmostlylike inline imports do. Many scientific Python
libraries have adopted a similar pattern, formalized inSPEC 1.
There’s also the third-partylazy_loaderpackage, yet another
implementation of lazy imports. Imports used solely for static type checking
are another source of potentially unneeded imports, and there are similarly
disparate approaches to minimizing the overhead. The various approaches used
here to defer or remove eager imports do not cover all potential use-cases for
a general lazy import mechanism. There is no clear standard, and there are
several drawbacks including runtime overhead in unexpected places, or worse
runtime introspection.

This proposal introduces syntax for lazy imports with a design that is local,
explicit, controlled, and granular. Each of these qualities is essential to
making the feature predictable and safe to use in practice.

The behavior islocal: laziness applies only to the specific import marked
with thelazykeyword, and it does not cascade recursively into other
imports. This ensures that developers can reason about the effect of laziness
by looking only at the line of code in front of them, without worrying about
whether imported modules will themselves behave differently. Alazyimportis an isolated decision each time it is used, not a global shift in semantics.

The semantics areexplicit. When a name is imported lazily, the binding is
created in the importing module immediately, but the target module is not
loaded until the first time the name is accessed. After this point, the
binding is indistinguishable from one created by a normal import. This clarity
reduces surprises and makes the feature accessible to developers who may not
be deeply familiar with Python’s import machinery.

Lazy imports arecontrolled, in the sense that deferred loading is only
triggered by the importing code itself. In the general case, a library will
only experience lazy imports if its own authors choose to mark them as such.
This avoids shifting responsibility onto downstream users and prevents
accidental surprises in library behavior. Since library authors typically
manage their own import subgraphs, they retain predictable control over when
and how laziness is applied.

The mechanism is alsogranular. It is introduced through explicit syntax
on individual imports, rather than a global flag or implicit setting. This
allows developers to adopt it incrementally, starting with the most
performance-sensitive areas of a codebase. As this feature is introduced to
the community, we want to make the experience of onboarding optional,
progressive, and adaptable to the needs of each project.

Lazy imports provide several concrete advantages:

* Command-line tools are often invoked directly by a user, so latency – in
particular startup latency – is quite noticeable. These programs are also
typically short-lived processes (contrasted with, e.g., a web server). With
lazy imports, only the code paths actually reached will import a module.
This can reduce startup time by 50-70% in practice, providing a significant
improvement to a common user experience and improving Python’s
competitiveness in domains where fast startup matters most.
* Type annotations frequently require imports that are never used at runtime.
The common workaround is to wrap them inifTYPE_CHECKING:blocks[1]. With lazy imports, annotation-only imports impose no runtime
penalty, eliminating the need for such guards and making annotated codebases
cleaner.
* Large applications often import thousands of modules, and each module
creates function and type objects, incurring memory costs. In long-lived
processes, this noticeably raises baseline memory usage. Lazy imports defer
these costs until a module is needed, keeping unused subsystems unloaded.
Memory savings of 30-40% have been observed in real workloads.

## Rationale

The design of this proposal is centered on clarity, predictability, and ease
of adoption. Each decision was made to ensure that lazy imports provide
tangible benefits without introducing unnecessary complexity into the language
or its runtime.

It is also worth noting that while this PEP outlines one specific approach, we
list alternate implementation strategies for some of the core aspects and
semantics of the proposal. If the community expresses a strong preference for
a different technical path that still preserves the same core semantics or
there is fundamental disagreement over the specific option, we have included
the brainstorming we have already completed in preparation for this proposal
as reference.

The choice to introduce a newlazykeyword reflects the need for explicit
syntax. Import behavior is too fundamental to be left implicit or hidden
behind global flags or environment variables. By marking laziness directly at
the import site, the intent is immediately visible to both readers and tools.
This avoids surprises, reduces the cognitive burden of reasoning about
imports, and keeps lazy import semantics in line with Python’s tradition of
explicitness.

Another important decision is to represent lazy imports with proxy objects in
the module’s namespace, rather than by modifying dictionary lookup. Earlier
approaches experimented with embedding laziness into dictionaries, but this
blurred abstractions and risked affecting unrelated parts of the runtime. The
dictionary is a fundamental data structure in Python – literally every object
is built on top of dicts – and adding hooks to dictionaries would prevent
critical optimizations and complicate the entire runtime. The proxy approach
is simpler: it behaves like a placeholder until first use, at which point it
resolves the import and rebinds the name. From then on, the binding is
indistinguishable from a normal import. This makes the mechanism easy to
explain and keeps the rest of the interpreter unchanged.

Compatibility for library authors was also a key concern. Many maintainers
need a migration path that allows them to support both new and old versions of
Python at once. For this reason, the proposal includes the__lazy_modules__global as a transitional mechanism. A module can
declare which imports should be treated as lazy (by listing the module names
as strings), and on Python 3.15 or later those imports will become lazy
automatically, as if they were imported with thelazykeyword. On earlier
versions the declaration is ignored, leaving imports eager. This gives authors
a practical bridge until they can rely on the keyword as the canonical syntax.

Finally, the feature is designed to be adopted incrementally. Nothing changes
unless a developer explicitly opts in, and adoption can begin with just a few
imports in performance-sensitive areas. This mirrors the experience of gradual
typing in Python: a mechanism that can be introduced progressively, without
forcing projects to commit globally from day one. Notably, the adoption can
also be done from the “outside in”, permitting CLI authors to introduce lazy
imports and speed up user-facing tools, without requiring changes to every
library the tool might use.

### Other design decisions

* The scope of laziness is deliberately local and non-recursive. A lazy import
only affects the specific statement where it appears; it does not cascade
into other modules or submodules. This choice is crucial for predictability.
When developers read code, they can reason about import behavior line by
line, without worrying about hidden laziness deeper in the dependency graph.
The result is a feature that is powerful but still easy to understand in
context.
* In addition, it is useful to provide a mechanism to activate or deactivate
lazy imports at a global level. While the primary design centers on explicit
syntax, there are scenarios – such as large applications, testing
environments, or frameworks – where enabling laziness consistently across
many modules provides the most benefit. A global switch makes it easy to
experiment with or enforce consistent behavior, while still working in
combination with the filtering API to respect exclusions or tool-specific
configuration. This ensures that global adoption can be practical without
reducing flexibility or control.

## Specification

### Grammar

A new soft keywordlazyis added. A soft keyword is a context-sensitive
keyword that only has special meaning in specific grammatical contexts;
elsewhere it can be used as a regular identifier (e.g., as a variable name).
Thelazykeyword only has special meaning when it appears before import
statements:

import_name:
 | 'lazy'? 'import' dotted_as_names

import_from:
 | 'lazy'? 'from' ('.' | '...')* dotted_name 'import' import_from_targets
 | 'lazy'? 'from' ('.' | '...')+ 'import' import_from_targets

#### Syntax restrictions

The soft keyword is only allowed at the global (module) level,notinside
functions, class bodies, withtry/withblocks, orimport*. Import
statements that use the soft keyword arepotentially lazy. Imports that
can’t be lazy are unaffected by the global lazy imports flag, and instead are
always eager.

Examples of syntax errors:

# SyntaxError: lazy import not allowed inside functions

def

foo
():


lazy

import

json

# SyntaxError: lazy import not allowed inside classes

class

Bar
:


lazy

import

json

# SyntaxError: lazy import not allowed inside try/except blocks

try
:


lazy

import

json

except

ImportError
:


pass

# SyntaxError: lazy import not allowed inside with blocks

with

suppress
(
ImportError
):


lazy

import

json

# SyntaxError: lazy from ... import * is not allowed

lazy

from

json

import

*

### Semantics

When thelazykeyword is used, the import becomespotentially lazy.
Unless lazy imports are disabled or suppressed (see below), the module is not
loaded immediately at the import statement; instead, a lazy proxy object is
created and bound to the name. The actual module is loaded on first use of
that name.

Example:

import

sys

lazy

import

json

print
(
'json'

in

sys
.
modules
)

# False - module not loaded yet

# First use triggers loading

result

=

json
.
dumps
({
"hello"
:

"world"
})

print
(
'json'

in

sys
.
modules
)

# True - now loaded

A module may contain a__lazy_modules__attribute, which is a
sequence of fully qualified module names (strings) to makepotentially lazy(as if thelazykeyword was used). This attribute is checked on eachimportstatement to determine whether the import should be madepotentially lazy. When a module is made lazy this way, from-imports using
that module are also lazy, but not necessarily imports of sub-modules.

The normal (non-lazy) import statement will check the global lazy imports
flag. If it is “enabled”, all imports arepotentially lazy(except for
imports that can’t be lazy, as mentioned above.)

Example:

__lazy_modules__

=

[
"json"
]

import

json

print
(
'json'

in

sys
.
modules
)

# False

result

=

json
.
dumps
({
"hello"
:

"world"
})

print
(
'json'

in

sys
.
modules
)

# True

If the global lazy imports flag is set to “disabled”, nopotentially lazyimport is ever imported lazily, and the behavior is equivalent to a regular
import statement: the import iseager(as if the lazy keyword was not used).

For apotentially lazyimport, the lazy imports filter (if set) is called
with the name of the module doing the import, the name of the module being
imported, and (if applicable) the fromlist. If the lazy import filter returnsTrue, thepotentially lazyimport becomes a lazy import. Otherwise, the
import isnotlazy, and the normal (eager) import continues.

### Lazy import mechanism

When an import is lazy,__lazy_import__is called instead of__import__.__lazy_import__has the same function signature as__import__. It adds the module name tosys.lazy_modules, a set of
fully-qualified module names which have been lazily imported at some point
(primarily for diagnostics and introspection), and returns a “lazy module
object.”

The implementation offrom...import(theIMPORT_FROMbytecode
implementation) checks if the module it’s fetching from is a lazy module
object, and if so, returns a lazy object for each name instead.

The end result of this process is that lazy imports (regardless of how they
are enabled) result in lazy objects being assigned to global variables.

Lazy module objects do not appear insys.modules, they’re just listed in
thesys.lazy_modulesset. Under normal operation lazy objects should only
end up stored in global variables, and the common ways to access those
variables (regular variable access, module attributes) will resolve lazy
imports (“reify”) and replace them when they’re accessed.

It is still possible to expose lazy objects through other means, like
debuggers. This is not considered a problem.

### Reification

When a lazy object is first used, it needs to be reified. This means resolving
the import at that point in the program and replacing the lazy object with the
concrete one. Reification imports the module in the same way as it would have
been if it had been imported eagerly, barring intervening changes to the
import system (e.g. tosys.path,sys.meta_path,sys.path_hooksor__import__).

Reification still calls__import__to resolve the import. When the module
is first reified, it’s removed fromsys.lazy_modules(even if there are
still other unreified lazy references to it). When a package is reified and
submodules in the package were also previously lazily imported, those
submodules arenotautomatically reified but theyareadded to the reified
package’s globals (unless the package already assigned something else to the
name of the submodule).

If reification fails (e.g., due to anImportError), the exception is
enhanced with chaining to show both where the lazy import was defined and
where it was first accessed (even though it propagates from the code that
triggered reification). This provides clear debugging information:

# app.py - has a typo in the import

lazy

from

json

import

dumsp

# Typo: should be 'dumps'

print
(
"App started successfully"
)

print
(
"Processing data..."
)

# Error occurs here on first use

result

=

dumsp
({
"key"
:

"value"
})

The traceback shows both locations:

App started successfully

Processing data...

Traceback (most recent call last):

 File
"app.py"
, line
2
, in
<module>


lazy

from

json

import

dumsp

ImportError
:
deferred import of 'json.dumsp' raised an exception during resolution

The above exception was the direct cause of the following exception:

Traceback (most recent call last):

 File
"app.py"
, line
8
, in
<module>


result

=

dumsp
({
"key"
:

"value"
})


^^^^^

ImportError
:
cannot import name 'dumsp' from 'json'. Did you mean: 'dump'?

This exception chaining clearly shows: (1) where the lazy import was defined,
(2) that it was deferred, and (3) where the actual access happened that
triggered the error.

Reification doesnotautomatically occur when a module that was previously
lazily imported is subsequently eagerly imported. Reification doesnotimmediately resolve all lazy objects (e.g.lazyfromstatements) that
referenced the module. Itonlyresolves the lazy object being accessed.

Accessing a lazy object (from a global variable or a module attribute) reifies
the object. Accessing a module’s__dict__reifiesalllazy objects in
that module. Operations that indirectly access__dict__(such asdir()) also trigger this behavior.

Example using__dict__from external code:

# my_module.py

import

sys

lazy

import

json

print
(
'json'

in

sys
.
modules
)

# False - still lazy

# main.py

import

sys

import

my_module

# Accessing __dict__ from external code DOES reify all lazy imports

d

=

my_module
.
__dict__

print
(
'json'

in

sys
.
modules
)

# True - reified by __dict__ access

print
(
type
(
d
[
'json'
]))

# <class 'module'>

However, callingglobals()doesnottrigger reification – it returns
the module’s dictionary, and accessing lazy objects through that dictionary
still returns lazy proxy objects that need to be manually reified upon use. A
lazy object can be resolved explicitly by calling thegetmethod. Other,
more indirect ways of accessing arbitrary globals (e.g. inspectingframe.f_globals) also donotreify all the objects.

Example usingglobals():

import

sys

lazy

import

json

# Calling globals() does NOT trigger reification

g

=

globals
()

print
(
'json'

in

sys
.
modules
)

# False - still lazy

print
(
type
(
g
[
'json'
]))

# <class 'lazy_import'>

# Explicitly reify using the get() method

resolved

=

g
[
'json'
]
.
get
()

print
(
type
(
resolved
))

# <class 'module'>

print
(
'json'

in

sys
.
modules
)

# True - now loaded

## Reference Implementation

A reference implementation is available at:https://github.com/LazyImportsCabal/cpython/tree/lazy

### Bytecode and adaptive specialization

Lazy imports are implemented through modifications to four bytecode
instructions:IMPORT_NAME,IMPORT_FROM,LOAD_GLOBAL, andLOAD_NAME.

Thelazysyntax sets a flag in theIMPORT_NAMEinstruction’s oparg
(oparg&0x01). The interpreter checks this flag and calls_PyEval_LazyImportName()instead of_PyEval_ImportName(), creating a
lazy import object rather than executing the import immediately. TheIMPORT_FROMinstruction checks whether its source is a lazy import
(PyLazyImport_CheckExact()) and creates a lazy object for the attribute
rather than accessing it immediately.

When a lazy object is accessed, it must be reified. TheLOAD_GLOBALinstruction (used in function scopes) andLOAD_NAMEinstruction (used at
module and class level) both check whether the object being loaded is a lazy
import. If so, they call_PyImport_LoadLazyImportTstate()to perform the
actual import and store the module insys.modules.

This check incurs a very small cost on each access. However, Python’s adaptive
interpreter can specializeLOAD_GLOBALafter observing that a lazy import
has been reified. After several executions,LOAD_GLOBALbecomesLOAD_GLOBAL_MODULE, which accesses the module dictionary directly without
checking for lazy imports.

Examples of the bytecode generated:

lazy

import

json

# IMPORT_NAME with flag set

Generates:

IMPORT_NAME 1 (json + lazy)

lazy

from

json

import

dumps

# IMPORT_NAME + IMPORT_FROM

Generates:

IMPORT_NAME 1 (json + lazy)
IMPORT_FROM 1 (dumps)

lazy

import

json

x

=

json

# Module-level access

Generates:

LOAD_NAME 0 (json)

lazy

import

json

def

use_json
():


return

json
.
dumps
({})

# Function scope

Before any calls:

LOAD_GLOBAL 0 (json)
LOAD_ATTR 2 (dumps)

After several calls,LOAD_GLOBALspecializes toLOAD_GLOBAL_MODULE:

LOAD_GLOBAL_MODULE 0 (json)
LOAD_ATTR_MODULE 2 (dumps)

### Lazy imports filter

This PEP adds two new functions to thesysmodule to manage the lazy
imports filter:

* sys.set_lazy_imports_filter(func)- Sets the filter function. Thefuncparameter must have the signature:func(importer:str,name:str,fromlist:tuple[str,...]|None)->bool
* sys.get_lazy_imports_filter()- Returns the currently installed filter
function, orNoneif no filter is set.

The filter function is called for every potentially lazy import, and must
returnTrueif the import should be lazy. This allows for fine-grained
control over which imports should be lazy, useful for excluding modules with
known side-effect dependencies or registration patterns.

The filter mechanism serves as a foundation that tools, debuggers, linters,
and other ecosystem utilities can leverage to provide better lazy import
experiences. For example, static analysis tools could detect modules with side
effects and automatically configure appropriate filters.In the future(out of scope for this PEP), this foundation may enable better ways to
declaratively specify which modules are safe for lazy importing, such as
package metadata, type stubs with lazy-safety annotations, or configuration
files. The current filter API is designed to be flexible enough to accommodate
such future enhancements without requiring changes to the core language
specification.

Example:

import

sys

def

exclude_side_effect_modules
(
importer
,

name
,

fromlist
):


"""

 Filter function to exclude modules with import-time side effects.

 Args:

 importer: Name of the module doing the import

 name: Name of the module being imported

 fromlist: Tuple of names being imported (for 'from' imports), or None

 Returns:

 True to allow lazy import, False to force eager import

 """


# Modules known to have important import-time side effects


side_effect_modules

=

{
'legacy_plugin_system'
,

'metrics_collector'
}


if

name

in

side_effect_modules
:


return

False

# Force eager import


return

True

# Allow lazy import

# Install the filter

sys
.
set_lazy_imports_filter
(
exclude_side_effect_modules
)

# These imports are checked by the filter

lazy

import

data_processor

# Filter returns True -> stays lazy

lazy

import

legacy_plugin_system

# Filter returns False -> imported eagerly

print
(
'data_processor'

in

sys
.
modules
)

# False - still lazy

print
(
'legacy_plugin_system'

in

sys
.
modules
)

# True - loaded eagerly

# First use of data_processor triggers loading

result

=

data_processor
.
transform
(
data
)

print
(
'data_processor'

in

sys
.
modules
)

# True - now loaded

### Global lazy imports control

The global lazy imports flag can be controlled through:

* The-Xlazy_imports=<mode>command-line option
* ThePYTHON_LAZY_IMPORTS=<mode>environment variable
* Thesys.set_lazy_imports(mode)function (primarily for testing)

Where<mode>can be:

* "default"(or unset): Only explicitly marked lazy imports are lazy
* "enabled": All module-level imports (except intryorwithblocks andimport*) becomepotentially lazy
* "disabled": No imports are lazy, even those explicitly marked withlazykeyword

When the global flag is set to"enabled", all imports at the global level
of all modules arepotentially lazyexceptfor those inside atryorwithblock or any wild card (from...import*) import.

If the global lazy imports flag is set to"disabled", nopotentially
lazyimport is ever imported lazily, the import filter is never called, and
the behavior is equivalent to a regularimportstatement: the import iseager(as if the lazy keyword was not used).

## Backwards Compatibility

Lazy imports areopt-in. Existing programs continue to run unchanged
unless a project explicitly enables laziness (vialazysyntax,__lazy_modules__, or an interpreter-wide switch).

### Unchanged semantics

* Regularimportandfrom...import...statements remain eager
unless explicitly madepotentially lazyby the local or global mechanisms
provided.
* Dynamic import APIs remain eager and unchanged:__import__()andimportlib.import_module().
* Import hooks and loaders continue to run under the standard import protocol
when a lazy object is reified.

### Observable behavioral shifts (opt-in only)

These changes are limited to bindings explicitly made lazy:

* Error timing.Exceptions that would have occurred during an eager import
(for exampleImportErrororAttributeErrorfor a missing member) now
occur at the firstuseof the lazy name.# With eager import - error at import statementimportbroken_module# ImportError raised here# With lazy import - error deferredlazyimportbroken_moduleprint("Import succeeded")broken_module.foo()# ImportError raised here on first use
* Side-effect timing.Import-time side effects in lazily imported modules
occur at first use of the binding, not at module import time.
* Import order.Because modules are imported on first use, the order in
which modules are imported may differ from how they appear in code.
* Presence in ``sys.modules``.A lazily imported module does not appear insys.modulesuntil first use. After reification, it must appear insys.modules. If some other code eagerly imports the same module before
first use, the lazy binding resolves to that existing (lazy) module object
when it is first used.
* Proxy visibility.Before first use, the bound name refers to a lazy
proxy. Indirect introspection that touches the value may observe a proxy
lazy object representation. After first use, the name is rebound to the real
object and becomes indistinguishable from an eager import.

### Thread-safety and reification

First use of a lazy binding follows the existing import-lock discipline.
Exactly one thread performs the import andatomically rebindsthe
importing module’s global to the resolved object. Concurrent readers
thereafter observe the real object.

Lazy imports are thread-safe and have no special considerations for
free-threading. A module that would normally be imported in the main thread
may be imported in a different thread if that thread triggers the first access
to the lazy import. This is not a problem: the import lock ensures thread
safety regardless of which thread performs the import.

Subinterpreters are supported. Each subinterpreter maintains its ownsys.lazy_modulesand import state, so lazy imports in one subinterpreter
do not affect others.

### Typing and tools

Type checkers and static analyzers may treatlazyimports as ordinary
imports for name resolution. At runtime, annotation-only imports can be markedlazyto avoid startup overhead. IDEs and debuggers should be prepared to
display lazy proxies before first use and the real objects thereafter.

## Security Implications

There are no known security vulnerabilities introduced by lazy imports.

## How to Teach This

The newlazykeyword will be documented as part of the language standard.

As this feature is opt-in, new Python users should be able to continue using
the language as they are used to. For experienced developers, we expect them
to leverage lazy imports for the variety of benefits listed above (decreased
latency, decreased memory usage, etc) on a case-by-case basis. Developers
interested in the performance of their Python binary will likely leverage
profiling to understand the import time overhead in their codebase and mark
the necessary imports aslazy. In addition, developers can mark imports
that will only be used for type annotations aslazy.

Below is guidance on how to best take advantage of lazy imports and how to
avoid incompatibilities:

* When adopting lazy imports, users should be aware that eliding an import
until it is used will result in side effects not being executed. In turn,
users should be wary of modules that rely on import time side effects.
Perhaps the most common reliance on import side effects is the registry
pattern, where population of some external registry happens implicitly
during the importing of modules, often via decorators but sometimes
implemented via metaclasses or__init_subclass__. Instead, registries of
objects should be constructed via explicit discovery processes (e.g. a
well-known function to call).# Problematic: Plugin registers itself on import# my_plugin.pyfromplugin_registryimportregister_plugin@register_plugin("MyPlugin")classMyPlugin:pass# In main code:lazyimportmy_plugin# Plugin NOT registered yet - module not loaded!# Better: Explicit discovery# plugin_registry.pydefdiscover_plugins():frommy_pluginimportMyPluginregister_plugin(MyPlugin)# In main code:plugin_registry.discover_plugins()# Explicit loading
* Always import needed submodules explicitly. It is not enough to rely on a
different import to ensure a module has its submodules as attributes.
Plainly, unless there is an explicitfrom.importbarinfoo/__init__.py, always useimportfoo.bar;foo.bar.Baz, notimportfoo;foo.bar.Baz. The latter only works (unreliably) because the
attributefoo.baris added as a side effect offoo.barbeing
imported somewhere else.
* Users who are moving imports into functions to improve startup time, should
instead consider keeping them where they are but adding thelazykeyword. This allows them to keep dependencies clear and avoid the overhead
of repeatedly re-resolving the import but will still speed up the program.# Before: Inline import (repeated overhead)defprocess_data(data):importjson# Re-resolved on every callreturnjson.dumps(data)# After: Lazy import at module levellazyimportjsondefprocess_data(data):returnjson.dumps(data)# Loaded once on first call
* Avoid using wild card (star) imports, as those are always eager.

## FAQ

Q: How does this differ from the rejected PEP 690?

A: PEP 810 takes an explicit, opt-in approach instead ofPEP 690’s implicit
global approach. The key differences are:

* Explicit syntax:lazyimportfooclearly marks which imports are
lazy.
* Local scope: Laziness only affects the specific import statement, not
cascading to dependencies.
* Simpler implementation: Uses proxy objects instead of modifying core
dictionary behavior.

Q: What happens when lazy imports encounter errors?

A: Import errors (ImportError,ModuleNotFoundError, syntax errors) are
deferred until first use of the lazy name. This is similar to moving an import
into a function. The error will occur with a clear traceback pointing to the
first access of the lazy object.

The implementation provides enhanced error reporting through exception
chaining. When a lazy import fails during reification, the original exception
is preserved and chained, showing both where the import was defined and where
it was first used:

Traceback (most recent call last):

 File
"test.py"
, line
1
, in
<module>


lazy

import

broken_module

ImportError
:
deferred import of 'broken_module' raised an exception during resolution

The above exception was the direct cause of the following exception:

Traceback (most recent call last):

 File
"test.py"
, line
3
, in
<module>


broken_module
.
foo
()


^^^^^^^^^^^^^

 File
"broken_module.py"
, line
2
, in
<module>


1
/
0

ZeroDivisionError
:
division by zero

Q: How do lazy imports affect modules with import-time side effects?

A: Side effects are deferred until first use. This is generally desirable for
performance, but may require code changes for modules that rely on import-time
registration patterns. We recommend:

* Use explicit initialization functions instead of import-time side effects
* Call initialization functions explicitly when needed
* Avoid relying on import order for side effects

Q: Can I use lazy imports withfrom...import...statements?

A: Yes, as long as you don’t usefrom...import*. Bothlazyimportfooandlazyfromfooimportbarare supported. Thebarname will be
bound to a lazy object that resolves tofoo.baron first use.

Q: DoeslazyfrommoduleimportClassload the entire module or just
the class?

A: It loads theentire module, not just the class. This is because
Python’s import system always executes the complete module file – there’s no
mechanism to execute only part of a.pyfile. When you first accessClass, Python:

1. Loads and executes the entiremodule.pyfile
2. Extracts theClassattribute from the resulting module object
3. BindsClassto the name in your namespace

This is identical to eagerfrommoduleimportClassbehavior. The only
difference with lazy imports is that steps 1-3 happen on first use instead of
at the import statement.

# heavy_module.py

print
(
"Loading heavy_module"
)

# This ALWAYS runs when module loads

class

MyClass
:


pass

class

UnusedClass
:


pass

# Also gets defined, even though we don't import it

# app.py

lazy

from

heavy_module

import

MyClass

print
(
"Import statement done"
)

# heavy_module not loaded yet

obj

=

MyClass
()

# NOW "Loading heavy_module" prints


# (and UnusedClass gets defined too)

Key point: Lazy imports deferwhena module loads, notwhatgets
loaded. You cannot selectively load only parts of a module – Python’s import
system doesn’t support partial module execution.

Q: What about type annotations andTYPE_CHECKINGimports?

A: Lazy imports eliminate the common need forTYPE_CHECKINGguards. You
can write:

lazy

from

collections.abc

import

Sequence
,

Mapping

# No runtime cost

def

process
(
items
:

Sequence
[
str
])

->

Mapping
[
str
,

int
]:


...

Instead of:

from

typing

import

TYPE_CHECKING

if

TYPE_CHECKING
:


from

collections.abc

import

Sequence
,

Mapping

def

process
(
items
:

Sequence
[
str
])

->

Mapping
[
str
,

int
]:


...

Q: What’s the performance overhead of lazy imports?

A: The overhead is minimal:

* Zero overhead after first use thanks to the adaptive interpreter optimizing
the slow path away.
* Small one-time cost to create the proxy object.
* Reification (first use) has the same cost as a regular import.
* No ongoing performance penalty unlikeimportlib.util.LazyLoader.

Benchmarking with thepyperformance suiteshows the implementation is
performance neutral when lazy imports are not used.

Q: Can I mix lazy and eager imports of the same module?

A: Yes. If modulefoois imported both lazily and eagerly in the same
program, the eager import takes precedence and both bindings resolve to the
same module object.

Q: How do I migrate existing code to use lazy imports?

A: Migration is incremental:

1. Identify slow-loading modules using profiling tools.
2. Addlazykeyword to imports that aren’t needed immediately.
3. Test that side-effect timing changes don’t break functionality.
4. Use__lazy_modules__for compatibility with older Python versions.

Q: What about star imports(frommoduleimport*)?

A: Wild card (star) imports cannot be lazy - they remain eager. This is
because the set of names being imported cannot be determined without loading
the module. Using thelazykeyword with star imports will be a syntax
error. If lazy imports are globally enabled, star imports will still be eager.

Q: How do lazy imports interact with import hooks and custom loaders?

A: Import hooks and loaders work normally. When a lazy object is first used,
the standard import protocol runs, including any custom hooks or loaders that
were in place at reification time.

Q: What happens in multi-threaded environments?

A: Lazy import reification is thread-safe. Only one thread will perform the
actual import, and the binding is atomically updated. Other threads will see
either the lazy proxy or the final resolved object.

Q: Can I force reification of a lazy import without using it?

A: Yes, accessing a module’s__dict__will reify all lazy objects in that
module. Individual lazy objects can be resolved by calling theirget()method.

Q: What’s the difference betweenglobals()andmod.__dict__for lazy imports?

A: Callingglobals()returns the module’s dictionary without reifying lazy
imports – you’ll see lazy proxy objects when accessing them through the
returned dictionary. However, accessingmod.__dict__from external code
reifies all lazy imports in that module first. This design ensures:

# In your module:

lazy

import

json

g

=

globals
()

print
(
type
(
g
[
'json'
]))

# <class 'lazy_import'> - your problem

# From external code:

import

sys

mod

=

sys
.
modules
[
'your_module'
]

d

=

mod
.
__dict__

print
(
type
(
d
[
'json'
]))

# <class 'module'> - reified for external access

This distinction means adding lazy imports and callingglobals()is your
responsibility to manage, while external code accessingmod.__dict__always sees fully loaded modules.

Q: Why not useimportlib.util.LazyLoaderinstead?

A:LazyLoaderhas significant limitations:

* Requires verbose setup code for each lazy import.
* Has ongoing performance overhead on every attribute access.
* Doesn’t work well withfrom...importstatements.
* Less clear and standard than dedicated syntax.

Q: Will this break tools likeisortorblack?

A: Tools will need updates to recognize thelazykeyword, but the changes
should be minimal since the import structure remains the same. The keyword
appears at the beginning, making it easy to parse.

Q: How do I know if a library is compatible with lazy imports?

A: Most libraries should work fine with lazy imports. Libraries that might
have issues:

* Those with essential import-time side effects (registration,
monkey-patching).
* Those that expect specific import ordering.
* Those that modify global state during import.

When in doubt, test lazy imports with your specific use cases.

Q: What happens if I globally enable lazy imports mode and a library doesn’t
work correctly?

A:Note: This is an advanced feature.You can use the lazy imports filter to
exclude specific modules that are known to have problematic side effects:

import

sys

def

my_filter
(
importer
,

name
,

fromlist
):


# Don't lazily import modules known to have side effects


if

name

in

{
'problematic_module'
,

'another_module'
}:


return

False

# Import eagerly


return

True

# Allow lazy import

sys
.
set_lazy_imports_filter
(
my_filter
)

The filter function receives the importer module name, the module being
imported, and the fromlist (if usingfrom...import). ReturningFalseforces an eager import.

Alternatively, set the global mode to"disabled"via-Xlazy_imports=disabledto turn off all lazy imports for debugging.

Q: Can I use lazy imports inside functions?

A: No, thelazykeyword is only allowed at module level. For
function-level lazy loading, use traditional inline imports or move the import
to module level withlazy.

Q: What about forwards compatibility with older Python versions?

A: Use the__lazy_modules__global for compatibility:

# Works on Python 3.15+ as lazy, eager on older versions

__lazy_modules__

=

[
'expensive_module'
,

'expensive_module_2'
]

import

expensive_module

from

expensive_module_2

import

MyClass

The__lazy_modules__attribute is a list of module name strings. When
an import statement is executed, Python checks if the module name being
imported appears in__lazy_modules__. If it does, the import is
treated as if it had thelazykeyword (becomingpotentially lazy). On
Python versions before 3.15 that don’t support lazy imports, the__lazy_modules__attribute is simply ignored and imports proceed
eagerly as normal.

This provides a migration path until you can rely on thelazykeyword. For
maximum predictability, it’s recommended to define__lazy_modules__once, before any imports. But as it is checked on each import, it can be
modified betweenimportstatements.

Q: How do explicit lazy imports interact with PEP-649/PEP-749

A: If an annotation is not stringified, it is an expression that is evaluated
at a later time. It will only be resolved if the annotation is accessed. In
the example below, thefake_typingmodule is only loaded when the user
inspects the__annotations__dictionary. Thefake_typingmodule would
also be loaded if the user usesannotationlib.get_annotations()orgetattrto access the annotations.

lazy

from

fake_typing

import

MyFakeType

def

foo
(
x
:

MyFakeType
):


pass

print
(
foo
.
__annotations__
)

# Triggers loading the fake_typing module

Q: How do lazy imports interact withdir(),getattr(),and
module introspection?

A: Accessing lazy imports through normal attribute access orgetattr()will trigger reification. Callingdir()on a module will reify all lazy
imports in that module to ensure the directory listing is complete. This is
similar to accessingmod.__dict__.

lazy

import

json

# Before any access

# json not in sys.modules

# Any of these trigger reification:

dumps_func

=

json
.
dumps

dumps_func

=

getattr
(
json
,

'dumps'
)

dir
(
json
)

# Now json is in sys.modules

Q: Do lazy imports work with circular imports?

A: Lazy imports don’t automatically solve circular import problems. If two
modules have a circular dependency, making the imports lazy might helponly
ifthe circular reference isn’t accessed during module initialization.
However, if either module accesses the other during import time, you’ll still
get an error.

Example that works(deferred access in functions):

# user_model.py

lazy

import

post_model

class

User
:


def

get_posts
(
self
):


# OK - post_model accessed inside function, not during import


return

post_model
.
Post
.
get_by_user
(
self
.
name
)

# post_model.py

lazy

import

user_model

class

Post
:


@staticmethod


def

get_by_user
(
username
):


return

f
"Posts by
{
username
}
"

This works because neither module accesses the other at module level – the
access happens later whenget_posts()is called.

Example that fails(access during import):

# module_a.py

lazy

import

module_b

result

=

module_b
.
get_value
()

# Error! Accessing during import

def

func
():


return

"A"

# module_b.py

lazy

import

module_a

result

=

module_a
.
func
()

# Circular dependency error here

def

get_value
():


return

"B"

This fails becausemodule_atries to accessmodule_bat import time,
which then tries to accessmodule_abefore it’s fully initialized.

The best practice is still to avoid circular imports in your code design.

Q: Will lazy imports affect the performance of my hot paths?

A: After first use, lazy imports havezero overheadthanks to the adaptive
interpreter. The interpreter specializes the bytecode (e.g.,LOAD_GLOBALbecomesLOAD_GLOBAL_MODULE) which eliminates the lazy check on subsequent
accesses. This means once a lazy import is reified, accessing it is just as
fast as a normal import.

lazy

import

json

def

use_json
():


return

json
.
dumps
({
"test"
:

1
})

# First call triggers reification

use_json
()

# After 2-3 calls, bytecode is specialized

use_json
()

use_json
()

You can observe the specialization usingdis.dis(use_json,adaptive=True):

=== Before specialization ===
LOAD_GLOBAL 0 (json)
LOAD_ATTR 2 (dumps)

=== After 3 calls (specialized) ===
LOAD_GLOBAL_MODULE 0 (json)
LOAD_ATTR_MODULE 2 (dumps)

The specializedLOAD_GLOBAL_MODULEandLOAD_ATTR_MODULEinstructions
are optimized fast paths with no overhead for checking lazy imports.

Q: What aboutsys.modules?When does a lazy import appear there?

A: A lazily imported module doesnotappear insys.modulesuntil it’s
reified (first used). Once reified, it appears insys.modulesjust like
any eager import.

import

sys

lazy

import

json

print
(
'json'

in

sys
.
modules
)

# False

result

=

json
.
dumps
({
"key"
:

"value"
})

# First use

print
(
'json'

in

sys
.
modules
)

# True

Q: Why you chose ``lazy`` as the keyword name?

A: Not “why”… memorize! :)

## Alternate Implementation Ideas

Here are some alternative design decisions that were considered during the
development of this PEP. While the current proposal represents what we believe
to be the best balance of simplicity, performance, and maintainability, these
alternatives offer different trade-offs that may be valuable for implementers
to consider or for future refinements.

### Leveraging a subclass of dict

Instead of updating the internal dict object to directly add the fields needed
to support lazy imports, we could create a subclass of the dict object to be
used specifically for Lazy Import enablement. This would still be a leaky
abstraction though - methods can be called directly such asdict.__getitem__and it would impact the performance of globals lookup in
the interpreter.

### Alternate keyword names

For this PEP, we decided to proposelazyfor the explicit keyword as it
felt the most familar to those already focused on optimizing import overhead.
We also considered a variety of other options to support explicit lazy
imports. The most compelling alternates weredeferanddelay.

## Rejected Ideas

### Modification of the dict object

The initial PEP for lazy imports (PEP 690) relied heavily on the modification
of the internal dict object to support lazy imports. We recognize that this
data structure is highly tuned, heavily used across the codebase, and very
performance sensitive. Because of the importance of this data structure and
the desire to keep the implementation of lazy imports encapsulated from users
who may have no interest in the feature, we’ve decided to invest in an
alternate approach.

The dictionary is the foundational data structure in Python. Every object’s
attributes are stored in a dict, and dicts are used throughout the runtime for
namespaces, keyword arguments, and more. Adding any kind of hook or special
behavior to dicts to support lazy imports would:

1. Prevent critical interpreter optimizations including future JIT
compilation.
2. Add complexity to a data structure that must remain simple and fast.
3. Affect every part of Python, not just import behavior.
4. Violate separation of concerns – the hash table shouldn’t know about the
import system.

Past decisions that violated this principle of keeping core abstractions clean
have caused significant pain in the CPython ecosystem, making optimization
difficult and introducing subtle bugs.

### Placing thelazykeyword in the middle of from imports

While we foundfromfoolazyimportbarto be a really intuitive placement
for the new explicit syntax, we quickly learned that placing thelazykeyword here is already syntactically allowed in Python. This is becausefrom.lazyimportbaris legal syntax (because whitespace does not
matter.)

### Placing thelazykeyword at the end of import statements

We discussed appending lazy to the end of import statements like suchimportfoolazyorfromfooimportbar,bazlazybut ultimately decided that
this approach provided less clarity. For example, if multiple modules are
imported in a single statement, it is unclear if the lazy binding applies to
all of the imported objects or just a subset of the items.

### Returning a proxy dict fromglobals()

An alternative to reifying onglobals()or exposing lazy objects would be
to return a proxy dictionary that automatically reifies lazy objects when
they’re accessed through the proxy. This would seemingly give the best of both
worlds:globals()returns immediately without reification cost, but
accessing items through the result would automatically resolve lazy imports.

However, this approach is fundamentally incompatible with howglobals()is
used in practice. Many standard library functions and built-ins expectglobals()to return a realdictobject, not a proxy:

* exec(code,globals())requires a real dict.
* eval(expr,globals())requires a real dict.
* Functions that checktype(globals())isdictwould break.
* Dictionary methods like.update()would need special handling.
* Performance would suffer from the indirection on every access.

The proxy would need to be so transparent that it would be indistinguishable
from a real dict in almost all cases, which is extremely difficult to achieve
correctly. Any deviation from true dict behavior would be a source of subtle
bugs.

### Reifying lazy imports whenglobals()is called

Callingglobals()returns the module’s namespace dictionary without
triggering reification of lazy imports. Accessing lazy objects through the
returned dictionary yields the lazy proxy objects themselves. This is an
intentional design decision for several reasons:

The key distinction: Adding a lazy import and callingglobals()is the
module author’s concern and under their control. However, accessingmod.__dict__from external code is a different scenario – it crosses
module boundaries and affects someone else’s code. Therefore,mod.__dict__access reifies all lazy imports to ensure external code sees fully realized
modules, whileglobals()preserves lazy objects for the module’s own
introspection needs.

Technical challenges: It is impossible to safely reify on-demand whenglobals()is called because we cannot return a proxy dictionary – this
would break common usages like passing the result toexec()or other
built-ins that expect a real dictionary. The only alternative would be to
eagerly reify all lazy imports wheneverglobals()is called, but this
behavior would be surprising and potentially expensive.

Performance concerns: It is impractical to cache whether a reification
scan has been performed with just the globals dictionary reference, whereas
module attribute access (the primary use case) can efficiently cache
reification state in the module object itself.

Use case rationale: The chosen design makes sense precisely because of
this distinction: adding a lazy import and callingglobals()is your
problem to manage, while having lazy imports visible inmod.__dict__becomes someone else’s problem. By reifying on__dict__access but not onglobals(), we ensure external code always sees fully loaded modules while
giving module authors control over their own introspection.

Note that three options were considered:

1. Callingglobals()ormod.__dict__traverses and resolves all lazy
objects before returning.
2. Callingglobals()ormod.__dict__returns the dictionary with lazy
objects present.
3. Callingglobals()returns the dictionary with lazy objects, butmod.__dict__reifies everything.

We chose the third option because it properly delineates responsibility: if
you add lazy imports to your module and callglobals(), you’re responsible
for handling the lazy objects. But external code accessing your module’s__dict__shouldn’t need to know about your lazy imports – it gets fully
resolved modules.

## Acknowledgements

We would like to thank Paul Ganssle, Yury Selivanov, Łukasz Langa, Lysandros
Nikolaou, Pradyun Gedam, Mark Shannon, Hana Joo and the Python Google team,
the Python team(s) @ Meta, the Python @ HRT team, the Bloomberg Python team,
the Scientific Python community, everyone who participated in the initial
discussion ofPEP 690, and many others who provided valuable feedback and
insights that helped shape this PEP.

## Footnotes

## Copyright

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.

Source:https://github.com/python/peps/blob/main/peps/pep-0810.rst

Last modified:2025-10-03 20:29:13 GMT

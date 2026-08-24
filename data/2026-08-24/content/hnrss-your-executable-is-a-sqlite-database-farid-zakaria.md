---
title: Your executable is a SQLite database | Farid Zakaria’s Blog
url: https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database
site_name: hnrss
content_file: hnrss-your-executable-is-a-sqlite-database-farid-zakaria
fetched_at: '2026-08-24T19:27:21.613303'
original_url: https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database
date: '2026-08-24'
published_date: '2026-08-23T07:30:00-07:00'
description: 'I have been probably obsessed with two things in the last few years: Nix as a tool to explore innovative ideas that require the capability to rebuild the world and replacing ELF with SQLite as an executable format. You might have noticed that these two ideas are well suited to each other.'
tags:
- hackernews
- hnrss
---

I have been probably obsessed with two things in the last few years: Nix as a tool to explore
innovative ideas that require the capability to rebuild the world and replacing ELF with SQLite as an executable format. You might have noticed that these two ideas are well suited to each other.

I explored the idea during my PhD thesis but found feedback from others unmotivating. 
Radical ideas are hard to sell, as you are working against the inertia of the established
solution.

One of the end results of that exploration wassqlelf,
a tool that lets you explore an ELF file declaratively using SQL.11I wrote a paper,arXiv:2405.03883,
that I failed to get published and a follow-up post onquerying with it.SELECT name FROM elf_symbolsinstead of fiddling withreadelfandgrep.
It was remarkably simple by leveragingvirtual tablesover the ELF: however I found it
to be a refreshing improvement to explore the ELF file format. I knew however that
there is still something much bigger to be done.

I never let the idea go and with the recent improvements with LLMs, I find it compelling to revisit these ideas to explore further. Specifically, can we replace ELF with SQLite as an executable format? 🤔

Not “a database that describes an executable”, but the actual file youchmod +xand run.

$
 
file hello

hello: SQLite 3.x database, application id 0x53454c46, user version 1

$
 
./hello

Hello, world!

$
 
sqlite3 hello 
'SELECT soname FROM ldd'

libc.so.6

I developed a pretty fleshed out prototype. It is calledSELF, theStructured Executable & Linkable Format, because I am unoriginal. It is onGitHubif you are interested. I’m surprised about all the interesting things that fall out of this idea.

# §ELF is a database that refuses to admit it

Working through my PhD, I realized something that bugged me. ELF isalreadya database. It just implements many database primitives by hand, along with a surprising number of
data structures for performance, like a bloom filter for symbol lookup.

ELF mechanism

The database primitive it reinvents

.strtab
 / 
.dynstr

string interning

.hash
 / 
.gnu.hash

an index (
CREATE INDEX
)

section header table

sqlite_schema
, a table of tables

st_name
 → offset into 
.strtab

a foreign key, done by hand

sh_offset
 / 
sh_size

the record layout of a b-tree page

.gnu.version_r

a column

objcopy --strip-debug

DELETE
 + 
VACUUM

ldconfig
 cache, 
debuginfod

out-of-band indexes over the above

If you ever have to analyze or parse ELF, the kernel,ld.so, binutils, LIEF, goblin,readelf, you are re-implementing the same parser over and over again. Every producer re-implements the same serializer.

The format itself is incredibly terse, designed for a world where disk space and network
bandwidth was at an extreme premium. Modifying the format is hard, you often have to zero out
sections and add new ones since it is packed so tightly. There is also no self-describing schema. ELF itself is a very generic format that supports sections of data that by convention
are interpreted in specific ways but the format does not enforce it.

SQLite is the counter-example. They are a self-describing
format that is extremely stable. It is designed to be extended to support new features without breaking existing consumers and supporting a wide range of queries performantly.

If we were to replace ELF with SQLite, what would fall out and can all of the necessary information be represented in a SQLite database? The answer is yes, and it is surprisingly simple.

# §What falls away

A SELF file needs two tables to run:self_metais the ELF header as key/value
pairs andsegmentsis the load image, one row per program header with the bytes
in aBLOB:

CREATE
 
TABLE
 
segments
 
(

 
-- original phdr index

 
id
 
INTEGER
 
PRIMARY
 
KEY
,

 
-- 'load' | 'tls' | 'stack' | 'relro'

 
type
 
TEXT
 
NOT
 
NULL
,

 
-- original file offset

 
offset
 
INTEGER
 
NOT
 
NULL
,

 
vaddr
 
INTEGER
 
NOT
 
NULL
,

 
filesz
 
INTEGER
 
NOT
 
NULL
,

 
memsz
 
INTEGER
 
NOT
 
NULL
,

 
r
 
INTEGER
,
 
w
 
INTEGER
,
 
x
 
INTEGER
,

 
align
 
INTEGER
 
NOT
 
NULL
 
DEFAULT
 
4096
,

 
-- the segment bytes; NULL for pure BSS

 
content
 
BLOB

);

A single table for the symbol table replaces many of the ELF sections and the.gnu.hashindex. It is a single table with a single index:

CREATE
 
TABLE
 
symbols
 
(

 
id
 
INTEGER
 
PRIMARY
 
KEY
,

 
name
 
TEXT
 
NOT
 
NULL
,

 
-- 'GLIBC_2.2.5'

 
version
 
TEXT
,

 
value
 
INTEGER
,

 
size
 
INTEGER
,

 
-- 'func' | 'object' | 'tls' | ...

 
type
 
TEXT
,

 
-- 'global' | 'weak' | 'local'

 
bind
 
TEXT
,

 
defined
 
INTEGER
 
NOT
 
NULL
,

 
exported
 
INTEGER
 
NOT
 
NULL

);

CREATE
 
INDEX
 
idx_symbols_name
 
ON
 
symbols
(
name
,
 
version
);

Our capability to include an index is equivalent to.gnu.hashand.hashin ELF, but it is a proper b-tree index maintained by SQLite instead of a hand-rolled bloom filter.22.gnu.hashis a bloom filter plus bucket chains, laid out sold.socan reject a miss without touching the chain during symbol discovery.

Surprisingly a lot more falls out as well:.dynstris gone, becausenameisTEXTand SQLite already interns strings, symbol versioning is a column, not the.gnu.version_r/.gnu.version_dcontraption and there is no need for astringstable.

Other tables exist as well for metadata which exist for tooling:sections,notes,dynamic_entries. Delete them and the program still
runs, which meansstrip(1)is a transaction:

# ldd(1)

$
 
sqlite3 hello 
'SELECT soname FROM ldd'
 

libc.so.6

# nm -D --undefined

$
 
sqlite3 hello 
'SELECT name,version FROM imports LIMIT 3'

__libc_start_main|GLIBC_2.34
_ITM_deregisterTMCloneTable|
puts|GLIBC_2.2.5

# readelf -l

$
 
sqlite3 hello 
\

 "SELECT type,vaddr,memsz,r,w,x FROM segments WHERE type='load'"
load|0|1744|1|0|0
load|4096|361|1|0|1
load|8192|312|1|0|0
load|15768|640|1|1|0

# strip(1)

$
 
sqlite3 hello 
'DELETE FROM sections; DELETE FROM notes; VACUUM;'

# 57344 -> 49152 bytes

# still runs, the optional tables were optional

$
 
./hello

Hello, world!

All the tools that operate on ELF files for reading, reduce to queries over the database.
Any tool that modifies an ELF file, likestrip, can operate on the database within a transaction rather than performing fragile offset surgery:stripis aDELETEandVACUUM.patchelfis anUPDATE.

Any information missing from the schema can be easily exposed via a view. For example,lddis a query over theneededtable, which is a join of thesymbolstable with thesegmentstable to find the sonames of the libraries needed by the program.

CREATE
 
VIEW
 
exports
 
AS
 
SELECT
 
name
,
 
version
,
 
type
,
 
size
 
FROM
 
symbols
 
WHERE
 
exported
 
=
 
1
;

CREATE
 
VIEW
 
imports
 
AS
 
SELECT
 
name
,
 
version
 
FROM
 
symbols
 
WHERE
 
defined
 
=
 
0
;

CREATE
 
VIEW
 
ldd
 
AS
 
SELECT
 
ord
,
 
soname
 
FROM
 
needed
 
ORDER
 
BY
 
ord
;

# §How does it work?

SQLite reserves a 4-byteapplication_idat byte
offset 68 of its header, for exactly this purpose. We stamp itSELF, so an
ordinary SQLite database never matches:

$
 
xxd 
-s
 64 
-l
 8 hello

00000040: 0000 0001 5345 4c46 ....SELF

We can now leveragebinfmt_misc, the subsystem that allows you to invoke any binary as if it were native. We need only to register
the magic to trigger on and an interpreter that will invoke our new file format.

On NixOS the registration is a few lines matching the SQLite magic at offset 0andSELFat 68:

boot
.
binfmt
.
registrations
.
self
 
=
 
{

 
recognitionType
 
=
 
"magic"
;

 
offset
 
=
 
0
;

 
# bytes 0-15, 68-71

 
magicOrExtension
 
=
 
"SQLite format 3
\\
x00"
 
+
 
...
 
+
 
"SELF"
;

 
# ignore the middle

 
mask
 
=
 
"
\\
xff..
\\
x00..
\\
xff"
;

 
interpreter
 
=
 
"
${
self-exec
}
/bin/self-exec"
;

};

For now, I have a small toolelf2selfthat converts an ELF file into a SELF file. It is a simplepostFixuphook you can opt into per package on NixOS. The tool reads the ELF, extracts the program headers and symbol table, and writes them into the SQLite database. We could look at extendinggccorldto emit SELF directly, but for now this is a simple way to explore the idea.

elf

hello

(ELF)

conv

elf2self

elf->conv

self

hello

(SQLite db)

conv->self

krn

execve()

binfmt_misc

self->krn

magic SELF@68

interp

self-exec

(interpreter)

krn->interp

run

running

process

interp->run

self-execis the interpreter. It is a small C program linked againstlibsqlite3.
Its implementation is remarkably similar to that ofld.sobut it fetches the program headers and symbol table from the database instead of reading them from the ELF file.
It maps the loadable segments into memory, relocates them, and jumps to the entry point.

Noteself-exechas to stay an ELF file. An interpreter that also matches the
registration recurses straight into-ELOOP.

# §Dynamic linking

Running a static program was quick and easy butboringand unimaginative. The interesting part is dynamic linking, which is where the database shines.

I explored two different ways to do dynamic linking. The first is to keepld.soand just replace the lookup with a SQL query viaglibcrtld-auditinterface, to quickly iterate on the design. The second is to replaceld.soentirely with a new dynamic linker that does the entire lookup and binding in SQL.

glibc’s rtld-audit interface lets an audit library intercept every shared object lookup (la_objsearch) before any filesystem search happens,dlopenincluded. The audit library can then answer the question “which library satisfies this symbol?” with a SQL query instead of walking theRUNPATHandLD_LIBRARY_PATH. Stockld.somaps and relocates it, so the full gamut of glibc features work: lazy PLT, IFUNCs, TLS and symbol versioning, while library storage are rows and library lookups are queries.

# no ELF library anywhere on disk

$
 
rm 
libgreet.so.1

$
 
./app

./app: error while loading shared libraries: 
 libgreet.so.1: cannot open ...

$
 
self scan 
--db
 system.db 
.

$
 
SELF_SYSTEM_DB
=
system.db 
LD_AUDIT
=
libself-audit.so ./app

Hello, world, from a SQLite library!

I was curious what a fully SQL dynamic linker would look like, so I prototyped one. It is calledself-ldand it is a small C program that implements the dynamic linker entirely in SQL. It is a proof-of-concept, but it works. It maps every object’s segments, publishes their exports, and for each relocation patches the GOT and jumps to the start.

SELECT
 
s
.
value
 
+
 
o
.
load_bias

FROM
 
relocations
 
r

JOIN
 
symbols
 
s
 
ON
 
r
.
symbol
 
=
 
s
.
id

JOIN
 
objects
 
o
 
ON
 
s
.
object
 
=
 
o
.
id

WHERE
 
r
.
id
 
=
 
?

ORDER
 
BY
 
o
.
load_order

LIMIT
 
1
;

# §Cost & Benchmark

The two things that often matter when replacing a well-established format are size and latency. How much bigger is a SELF file than an ELF file, and how much slower is it to run?

Size.A SELF file carries SQLite’s b-tree overhead and lands at roughly
double the ELF.

1980-01-01T00:00:00+00:00

image/svg+xml

Matplotlib v3.10.5, https://matplotlib.org/

Similar to ELF binaries, most of that is recoverable, because the overhead is mostly the optional tables for debugging and tooling. Stripping them and deleting them is a transaction. A strippedcoreutilsSELF is 1,794,048 B against the ELF’s 1,768,632 B, that iswithin 1%.

We will see though that there are interesting ways to amortise the overhead even more which I found very unique and interesting.

Latency.I benchmarked various binaries from a 15 KiBhelloto a 42 MiBgdblinking 47 libraries:

1980-01-01T00:00:00+00:00

image/svg+xml

Matplotlib v3.10.5, https://matplotlib.org/

There is a fixed ~5 ms to open SQLite and start the interpreter, plus a copy proportional
to the image. That copy is worse than it looks, because the b-tree pages are not mapped into memory. Two processes running the same SELF binary do not share text pages the way a normally-mmap‘d ELF does, because the bytes are copied out of the b-tree rather than mapped.33You might notice thatcurl(274 KiB, 27 libraries) starts slower than ELFgit(4.6 MiB, 5 libraries). That isld.sodoing work proportional to the
number of objects rather than the number of bytes, which I havecomplained about before.

# §The system is a closure

A SQLite database though need not merely be a single executable. It can be aclosure, a single file that contains a program and all of its transitive dependencies. Thelddoutput of a program is ambiguous: it only lists the sonames of the libraries it needs, not the specific files that satisfy those needs. Nix improves upon this by explicitly resolving every edge to a specific store path via the use ofRUNPATH.44I have written aboutRUNPATHon Nix before such asmaking it redundantorspeeding it up.

We can do the same in SELF by storing the resolved path of each edge in the database:

CREATE
 
TABLE
 
objects
 
(
id
 
INTEGER
 
PRIMARY
 
KEY
,
 
path
 
TEXT
 
UNIQUE
,

 
soname
 
TEXT
,
 
kind
 
TEXT
,
 
is_root
 
INTEGER
);

CREATE
 
TABLE
 
needs
 
(

 
object_id
 
INTEGER
 
REFERENCES
 
objects
(
id
),

 
ord
 
INTEGER
 
NOT
 
NULL
,

 
soname
 
TEXT
 
NOT
 
NULL
,

 
-- the FK that kills ambiguity

 
resolved_path
 
TEXT
 
REFERENCES
 
objects
(
path
)

);

self closurepacks a binary and its transitive dependencies intoone databasewith those edges filled in. Shared library resolution stops being a guess and
becomes a foreign key andlddbecomes aJOIN🤯:

$
 
self closure 
"
$(
readlink
 
-f
 
$(
command
 
-v
 
ls
))
"
 coreutils.db

ls + closure ->
 
coreutils.db

$
 
sqlite3 
-column
 coreutils.db 
\

 "SELECT n.soname, substr(n.resolved_path, 12, 20)
 FROM needs n JOIN objects o ON o.id = n.object_id
 WHERE o.is_root = 1"
libgmp.so.10 rfabfsmwq02sn94mb3qg
libacl.so.1 x0zgiss9hdzcsll3cswg
libattr.so.1 08nfpyc4qhzdkc37nznv
libc.so.6 8kvxvr3pmsypxiypq4g8

This single database is a closure of thelsexecutable and its five libraries:
six objects, segment bytes and all, in one 4.8 MiB file. There is no soname ambiguity inside a closure, because a closure by
construction contains exactly one provider per edge.

ls

ls

(is_root)

libc

libc.so.6

ls->libc

gmp

libgmp.so.10

ls->gmp

acl

libacl.so.1

ls->acl

attr

libattr.so.1

ls->attr

gmp->libc

acl->libc

acl->attr

attr->libc

# §How far does this go? One file, one userland

I hope you’ve been with me so far, because this is where it gets really interesting.
We can go even further and packmultiple closuresinto a single database.

I pointedself closureat every ELF binary on this system’sPATH: 723 executables,
which pull in 400 distinct shared libraries. 1,123 objects, 346,386 symbols,
3,808 dependency edges, all asone SQLite file.

Turns out when you do that, the database is much smaller than you would expect.

1980-01-01T00:00:00+00:00

image/svg+xml

Matplotlib v3.10.5, https://matplotlib.org/

611.9 MiB of database against 644.4 MiB of ELF files.The whole userland,
as one queryable file, issmallerthan the files it came from. The b-tree cost that doubled a singlehelloamortises to nearly nothing across 1,123 objects and is roughly 6% over
the actual program bytes.

The libraries and closure are shared across the executables very similar to how Nix might share them across multiple closures, if the store-path was the same. If every root shipped its own private closure (i.e. the AppImage model), the same 723 programs would come to
5.53 GiB but the deduplication of libraries and symbols falls out naturally from the database schema.

$
 
sqlite3 userland.db 
\

 'SELECT count(DISTINCT soname), count(*)
 FROM objects WHERE soname IS NOT NULL'
345|399

$
 
sqlite3 
-column
 userland.db 
\

 'SELECT soname, count(*) FROM objects
 WHERE soname IS NOT NULL

 GROUP BY soname HAVING count(*) >
 
1

 ORDER BY 2 DESC LIMIT 4'
libsystemd.so.0 3
libpthread.so.0 3
libgcc_s.so.1 3
libc.so.6 3

$
 
sqlite3 userland.db 
\

 "SELECT count(*)
 FROM needs
 WHERE resolved_path IS NULL AND soname NOT LIKE 'ld-%'"
4

Many common idioms we use in ELF immediately fall out of the database. For example,LD_PRELOADis a row in a table rather than an environment variable. Thepreloadtable is a list of objects to map last, so their exports win. This means that turningLD_PRELOADon and off is a transaction.

$
 
./app.self
;
 
echo
 
$?

13

$
 
sqlite3 system.db 
"BEGIN;

 CREATE TABLE preload(ord INTEGER PRIMARY KEY, path TEXT);

 INSERT INTO preload VALUES (0, 'libmul.so.1.self');

 COMMIT;
"

# same binary, no env var, no relink

$
 
./app.self
;
 
echo
 
$?

42

$
 
sqlite3 system.db 
'DELETE FROM preload;'

$
 
./app.self
;
 
echo
 
$?

13

We were able to accomplish an atomicLD_PRELOADacross a whole userland
in one file, “interpose a tracingmalloceverywhere, thenROLLBACK” is a
single transaction. 😈

# §Where it stands

The format is done and round-trips between ELF and SELF losslessly. The tooling is done and can query, modify, and pack closures. Lookup through SQL works on unmodified glibc programs perfectly and the native-SQL loader works enough to explore it as a possibility for ideas.

The whole thing is atfzakaria/selfdb.nix run .#self-vmboots a NixOS VM wherehellois a SQLite database. 🙌

Nix lets us explore radical ideas like this. We can rebuild the world down to the Linux kernel if needed. We need not be constrained by the existing decisions and constraints of the past. We can explore new ideas and see what falls out. I hope you find this idea as interesting as I do.
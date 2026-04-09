---
title: Notes by djb on using Fil-C
url: https://cr.yp.to/2025/fil-c.html
site_name: hackernews_api
fetched_at: '2025-11-03T11:10:51.727356'
original_url: https://cr.yp.to/2025/fil-c.html
author: transpute
date: '2025-11-02'
description: Notes by djb on using Fil-C
tags:
- hackernews
- trending
---

# Notes by djb on using Fil-C (2025)

I'm impressed with the level of compatibility
of the new memory-safe C/C++ compilerFil-C(filcc, fil++).
Many libraries and applications that I've tried
work under Fil-C without changes, and the exceptions haven't been hard to get working.

I've started accumulating miscellaneous notes on this page regarding usage of Fil-C.
My selfish objective here is to protect various machines that I manage
by switching them over to code compiled with Fil-C,
but maybe you'll find something useful here too.

Timings below are from a mini-PC namedphoenixexcept where otherwise mentioned.
This mini-PC has a 6-core (12-thread) AMD Ryzen 5 7640HS (Zen 4) CPU, 12GB RAM, and 36GB swap.
The OS is Debian 13.
(I normally run LTS software,
periodically upgrading from software that's 4–5 years old such as Debian 11 today
to software that's 2–3 years old such as Debian 12 today;
but some of the packages included in Fil-C expect newer utilities to be available.)

Related:

* I've posted ascriptto help auditors see how Fil-C differs from upstream sources (clang, glibc, ...).
* I've posted a self-containedfilian-install-compilerscript
(replacing the20251029 version)
to download+compile+install Fil-C on Debian 13 in what I think are Debian-appropriate locations,
along with glibc and binutils compiled with Fil-C.
A run took 86 minutes real time (for 477 minutes user time and 52 minutes system time).
* I've posted the start of afilian-install-packagesscript to download+compile+install Debian source packages, using Fil-C as the compiler
(afterfilian-install-compilerhas finished).
This script has various limitations that need fixing,
but it does work for a few packages already
(e.g.,./filian-install-packages bzip2),
after the installation ofdh-execetc. described below.
* I've posted agraphshowing nearly 9000 microbenchmarks of Fil-C vs. clang on cryptographic software (each run pinned to 1 core on the same Zen 4).
Typically code compiled with Fil-C takes between 1x and 4x as many cycles as the same code compiled with clang.

Another way to run Fil-C is viaFilnixfrom Mikael Brockman.
For example,
an unprivileged user under Debian 12 with about 10GB of free disk space
can download, compile, and install Fil-C,
and run a Fil-C-compiled Nethack, as follows:

unshare --user --pid echo YES # just to test
git clone https://github.com/nix-community/nix-user-chroot
cd nix-user-chroot
cargo build --release
mkdir -m 0755 ~/nix
~/nix-user-chroot/target/release/nix-user-chroot ~/nix \
 bash -c 'curl -L https://nixos.org/nix/install | sh'
env TERM=vt102 \
 ~/nix-user-chroot/target/release/nix-user-chroot ~/nix \
 ~/nix/store/*-nix-2*/bin/nix \
 --extra-experimental-features 'nix-command flakes' \
 run 'github:mbrock/filnix#nethack'

## Compiler and C library

Current recommendations for things to do at the beginning asroot:

mkdir -p /var/empty
apt install \
 autoconf-dickey build-essential bison clang cmake flex gawk \
 gettext ninja-build patchelf quilt ruby texinfo time

I created an unprivilegedfilcuser.
Everything else is as that user.

I downloaded the Fil-C source package:

git clone https://github.com/pizlonator/fil-c.git
cd fil-c

This isn't just the compiler;
there's also glibc and quite a few higher-level libraries and applications.
There are also binary Fil-C packages,
but I've worked primarily with the source package at this point.

I compiled Fil-C and glibc:

time ./build_all_fast_glibc.sh

There are also options to use musl instead of glibc,
but musl is incompatible with some of the packages shipped with Fil-C:attrneedsbasename,elfutilsneedsargp_parse,sed's test suite needs the glibc variant ofcalloc,
andvim's build needsiconvto be able to convert from CP932 to UTF-8.

I had originally configured the serverphoenixwith only 12GB swap.
I then had to restart./build_all_fast_glibc.sha few times
because the Fil-C compilation ran out of memory.
Switching to 36GB swap made everything work with no restarts;
monitoring showed that almost 19GB swap (plus 12GB RAM) was used at one point.
A larger server, 128 cores with 512GB RAM, took 8 minutes for Fil-C plus 6 minutes for musl,
with no restarts needed.

## More libraries and applications included with Fil-C

Fil-C includes a./build_all_slow.shthat builds many more libraries and applications
(sometimes with patches from the Fil-C author).
I wrote a replacement scripthttps://cr.yp.to/2025/build-parallel-20251023.pywith the following differences:

* Thebuild-parallelscript
 runs through everything, putting results intobuild/logs/*,
 whereasbuild_all_slowstops at the first error.
* Thebuild-parallelscript tries to use multiple cores,
 whilebuild_all_slowruns through targets serially,
 parallelizing only to the extent that each target's build mechanism is parallelized.
* Thebuild-parallelscript might produce wrong results if it's parallelizing things
 that shouldn't be parallelized.
 But this should be easy to fix via tweaking the dependencies listed in the script.

Onphoenix,
runningtime PATH="$HOME/bin:$HOME/fil-c/build/bin:$HOME/fil-c/pizfix/bin:$PATH" ./build-parallel.pywent through 61 targets in 101 minutes real time (467 minutes user time, 55 minutes system time),
successfully compiling 60 of them.

libcap.This is the one that didn't compile:/home/filc/fil-c/pizfix/bin/ld: /usr/libexec/gcc/x86_64-linux-gnu/14/liblto_plugin.so: error loading plugin: libc.so.6: cannot open shared object file: No such file or directory

util-linux.I skipped this one.
It does compile,
but the compiledtasksetutility needs to be patched to usesched_getaffinityandsched_setaffinityas library functions rather than viasyscall,
or Fil-C needs to be patched for those syscalls.
This is an issue forbuild-parallelsincebuild-parallelrelies ontaskset;
maybebuild-parallelshould instead use Python's affinity functions.

attr, bash, benchmarks, binutils, bison, brotli, bzip2, bzip3, check, cmake, coreutils, cpython, curl, dash, diffutils, elfutils, emacs, expat, ffi, gettext, git,
gmp, grep, icu, jpeg-6b, libarchive, libcap, libedit, libevent, libpipeline, libuev, libuv, lua, lz4, m4, make, mg, ncurses, nghttp2, openssh, openssl, pcre2, pcre,
perl, pkgconf, procps, quickjs, sed, shadow, simdutf, sqlite, tcl, tmux, toybox, vim, wg14_signals, xml_parser, xz, zlib, zsh, zstd.No problems encountered so far
(given whatever patches were already applied from the Fil-C author!).
The benchmarks package is supplied with Fil-C and does a few miscellaneous measurements.

## Further libraries and applications

I didexport PATH="$HOME/bin:$HOME/fil-c/build/bin:$HOME/fil-c/pizfix/bin:$PATH"before these.

boost 1.89.0:
Seems to mostly work.
Most of the package is header-only;
a few simple tests worked fine.

I also looked a bit at the compiled parts.
Running./bootstrap.sh --with-toolset=clang --prefix=$HOMEran intovfork,
which Fil-C doesn't support,
but editingtools/build/src/engine/execunix.cppto usedefined(__APPLE__) || defined(__FILC__)for the no-fork test got past this.

Running./b2 install --prefix=$HOME toolset=clang address-model=64 architecture=x86_64 binary-format=elfproduced an error message since I should have saidx86instead ofx86_64;
Fil-C said it caught a safety issue in theb2program after the error message:filc safety error: argument size mismatch (actual = 8, expected = 16).
I didn't compile with debugging so Fil-C didn't say where this is inb2.

cdb-20251021:
Seems to work.
One regression test, an artificial out-of-memory regression test,
currently produces a different error message with Fil-C:filc panic: src/libpas/pas_compact_heap_reservation.c:65: pas_aligned_allocation_result pas_compact_heap_reservation_try_allocate(size_t, size_t):
assertion page_result.result failed.

libcpucycles-20250925:
Seems to work.
I commented out the first three lines ofcpucycles/options.

libgc:
I replaced this with a small gcshim package
(https://cr.yp.to/2025/gcshim-20251022.tar.gz)
that simply callsmallocetc.
So far this seems to be an adequate replacement.
(Fil-C includes a garbage collector.)

libntruprime-20241021:
Seems to work after a few tweaks but I didn't collect full notes yet.chmod +t crypto_hashblocks/sha512/avx2disables assembly and makes things compile;
configured with--no-valgrindsince Fil-C doesn't support valgrind;
did a bit more tweaking to makecpuidwork.

lpeg-1.1.0:Compiles, maybe works (depends on lua, dependency of neovim):cd
PREFIX=$(dirname $(dirname $(which lua)))
wget https://www.inf.puc-rio.br/~roberto/lpeg/lpeg-1.1.0.tar.gz
tar -xf lpeg-1.1.0.tar.gz
cd lpeg-1.1.0
make CC=`which filcc` DLLFLAGS='-shared -fPIC' test
cp lpeg.so $PREFIX/lib

luv-1.51.0:Compiles, maybe works (depends on lua, dependency of neovim):cd
PREFIX=$(dirname $(dirname $(which lua)))
wget https://github.com/luvit/luv/releases/download/1.51.0-1/luv-1.51.0-1.tar.gz
tar -xf luv-1.51.0-1.tar.gz
cd luv-1.51.0-1
mkdir build
cd build
LUA_DIR=$HOME/fil-c/projects/lua-5.4.7
# lua install should probably do this:
cp $LUA_DIR/lua.h $PREFIX/include/
cp $LUA_DIR/lauxlib.h $PREFIX/include/
cp $LUA_DIR/luaconf.h $PREFIX/include/
cp $LUA_DIR/lualib.h $PREFIX/include/
# and then:
cmake -DCMAKE_C_COMPILER=`which filcc` -DCMAKE_INSTALL_PREFIX=$PREFIX -DWITH_LUA_ENGINE=Lua -DLUA_DIR=$HOME/fil-c/projects/lua-5.4.7/ ..
make test
make install

mutt-2-2-15-rel(depends on ncurses):wget https://github.com/muttmua/mutt/archive/refs/tags/mutt-2-2-15-rel.tar.gz
tar -xf mutt-2-2-15-rel.tar.gz
cd mutt-mutt-2-2-15-rel
CC=`which clang` ./prepare --prefix=$HOME/fil-c/pizfix --with-homespool
make -j12 installSeems to work, at least for reading email.

tig(depends on ncurses and maybe more):wget https://github.com/jonas/tig/releases/download/tig-2.6.0/tig-2.6.0.tar.gz
tar -xf tig-2.6.0.tar.gz
cd tig-2.6.0
CC=`which filcc` ./configure --prefix=$(dirname $(dirname $(which git)))
make -j12
make test
make -j12 installSeems to work, at least for viewing the Fil-C repo.

w3m(depends on gcshim and ncurses):
Seems to work.
I tried the Debian version:git clone https://salsa.debian.org/debian/w3m.git.
I usedCFLAGS=-Wno-incompatible-function-pointer-types(which is probably needed for clang anyway even without Fil-C).

## Debian using Fil-C (Filian?)

I've built and installed some replacement Debian packages using Fil-C as the compiler on a Debian 13 machine,
as explained below.
Hopefully this can rapidly scale to many packages,
taking advantage of the basic compile-install-test knowledge already built into Debian source packages,
although some packages will take more work because they need extra patches to work with Fil-C.

Structure.Debian already understands how to have packages for multiple architectures (ABIs; Debian "ports") installed at once.
For example,dpkg --add-architecture i386; apt update; apt install bash:i386installs a 32-bit version of bash,
replacing the usual 64-bit version;
you can doapt install bash:amd64to revert to the 64-bit version.
Meanwhile the 32-bit libraries and 64-bit libraries are installed in separate locations,
basically/lib/i386-linux-gnuor/usr/lib/i386-linux-gnuvs./lib/x86_64-linux-gnuor/usr/lib/x86_64-linux-gnu.
(On Debian 11 and newer, and on Ubuntu 22.04 and newer,/libis symlinked to/usr/lib.)

I'm following this model for plugging Fil-C into Debian:
the goal is forapt install bash:amd64fil0to install a Fil-C-compiled (amd64fil0) version of bash,
replacing the usual (amd64) version of bash,
while theamd64andamd64fil0libraries are installed in separate locations.

The include-file complication.Debianexpectslibrary packages compiled for multiple ABIs
to all provide the same include files:
for example,/usr/include/ncurses.his provided bylibncurses-dev:i386,libncurses-dev:amd64, etc.
This is safe because Debian forceslibncurses-dev:i386andlibncurses-dev:amd64and so on
to all have the same version.
An occasional package with ABI-dependent include files
can still use/usr/include/x86_64-linux-gnuetc.

Fil-C instead omits/usr/includein favor of a Fil-C-specific directory
(which will typically be different from/usr/include:
even if Fil-C is compiled with glibc,
probably the glibc version won't be the same as in/usr/include).
This difference is the top source of messiness below.
I'm planning to tweak the Fil-C driver to use/usr/includeon Debian.
[This is done in thefilian-install-compilerscript.]

Something else I'm planning to tweak is Fil-C's glibc compilation,
so that it uses the final system prefix.
[This is also done in thefilian-install-compilerscript.]
The approach described below instead requires/home/filian/fil-cto stay in place
for compiling and running programs.Building Debian packages.How does Debian package building work?
First, more packages to install as root:apt install dpkg-dev devscripts docbook2x \
 dh-exec dh-python python3-setuptools fakeroot \
 sbuild mmdebstrap uidmap piupartsDebian hasmultiple optionsfor building a package.
The option that has the best isolation,
and that Debian uses to continually build new packages for distribution,
is sbuild,
but for fast development I'll focus on directly using the lower-level
dpkg-buildpackage.Baseline 1: using sbuild without Fil-C.In case you do want to try sbuild,
here's the basic setup,
and then an example of building a small package (tinycdb):mkdir -p ~/shared/sbuild
time mmdebstrap --include=ca-certificates --skip=output/dev --variant=buildd unstable ~/shared/sbuild/unstable-amd64.tar.zst https://deb.debian.org/debian

mkdir -p ~/.config/sbuild
cat << "EOF" > ~/.config/sbuild/config.pl
$chroot_mode = 'unshare';
$external_commands = { "build-failed-commands" => [ [ '%SBUILD_SHELL' ] ] };
$build_arch_all = 1;
$build_source = 1;
$source_only_changes = 1;
$run_lintian = 1;
$lintian_opts = ['--display-info', '--verbose', '--fail-on', 'error,warning', '--info'];
$run_autopkgtest = 1;
$run_piuparts = 1;
$piuparts_opts = ['--no-eatmydata', '--distribution=%r', '--fake-essential-packages=systemd-sysv'];
EOF

mkdir -p ~/shared/packages
cd ~/shared/packages
apt source tinycdb
cd tinycdb-*/
time sbuildBaseline 2: using dpkg-buildpackage without Fil-C.Here's what it looks like compiling the same small package with dpkg-buildpackage:mkdir -p ~/shared/packages
cd ~/shared/packages
apt source tinycdb
cd tinycdb-*/
time dpkg-buildpackage -us -uc -bThe goal: Using dpkg-buildpackage with Fil-C.As root, teach dpkg basic features of the new architecture,
imitating the current lineamd64 x86_64 (amd64|x86_64) 64 littlein the same file:echo amd64fil0 x86_64+fil0 amd64fil0 64 little >> /usr/share/dpkg/cputable

Also, allowaptto install packages compiled for this architecture
(beware that this will also later makeapt updatelook for that architecture on servers,
and whimper a bit for not finding it,
but nothing breaks):

dpkg --add-architecture amd64fil0

Also, teachautoconfto accept amd64fil0
(the third of these lines is what's critical for Debian builds):

sed -i '/| x86_64 / a| x86_64+fil0 \\' /usr/share/autoconf/build-aux/config.sub
sed -i '/| x86_64 / a| x86_64+fil0 \\' /usr/share/libtool/build-aux/config.sub
sed -i '/| x86_64 / a| x86_64+fil0 \\' /usr/share/misc/config.sub

[Not necessary if you've usedfilian-install-compiler:]
As afilianuser,
compile Fil-C and its standard library:

cd
git clone https://github.com/pizlonator/fil-c.git
cd fil-c
time ./build_all_fast_glibc.sh

[Not necessary if you've usedfilian-install-compiler:]
As root,
copy Fil-C and its standard library into system locations:

mkdir -p /usr/libexec/fil/amd64/compiler
time cp -r /home/filian/fil-c/pizfix /usr/libexec/fil/amd64/
rm -rf /usr/lib/x86_64+fil0-linux-gnu
mv /usr/libexec/fil/amd64/pizfix/lib /usr/lib/x86_64+fil0-linux-gnu
ln -s /usr/lib/x86_64+fil0-linux-gnu /usr/libexec/fil/amd64/pizfix/lib
rm -rf /usr/include/x86_64+fil0-linux-gnu
mv /usr/libexec/fil/amd64/pizfix/include /usr/include/x86_64+fil0-linux-gnu
ln -s /usr/include/x86_64+fil0-linux-gnu /usr/libexec/fil/amd64/pizfix/include
time cp -r /home/filian/fil-c/build/bin /usr/libexec/fil/amd64/compiler/
time cp -r /home/filian/fil-c/build/include /usr/libexec/fil/amd64/compiler/
time cp -r /home/filian/fil-c/build/lib /usr/libexec/fil/amd64/compiler/
( echo '#!/bin/sh'
 echo 'exec /usr/libexec/fil/amd64/compiler/bin/filcc "$@"' ) > /usr/bin/x86_64+fil0-linux-gnu-gcc
chmod 755 /usr/bin/x86_64+fil0-linux-gnu-gcc
( echo '#!/bin/sh'
 echo 'exec /usr/libexec/fil/amd64/compiler/bin/fil++ "$@"' ) > /usr/bin/x86_64+fil0-linux-gnu-g++
chmod 755 /usr/bin/x86_64+fil0-linux-gnu-g++
ln -s /usr/libexec/fil/amd64/compiler/bin/llvm-objdump /usr/bin/x86_64+fil0-linux-gnu-objdump
ln -s x86_64+fil0-linux-gnu-gcc /usr/bin/filcc
ln -s x86_64+fil0-linux-gnu-g++ /usr/bin/fil++

Now, as userfilian(or whichever other user),
let's make a little helper script to adjust a Debian source package:

mkdir -p $HOME/bin
( echo '#!/bin/sh'
 echo 'sed -i '\''s/^ \([^"]*\)$/ pizlonated_\1/'\'' debian/*.symbols'
 echo 'find . -name '\''*.map'\'' | while read fn'
 echo 'do'
 echo ' awk '\''{'
 echo ' if ($1 == "local:") global = 0'
 echo ' if ($1 == "}") global = 0'
 echo ' if (global && NF > 0 && !index($0,"c++")) $1 = "pizlonated_"$1'
 echo ' if ($1 == "global:") global = 1'
 echo ' print'
 echo ' }'\'' < $fn > $fn.tmp'
 echo ' mv $fn.tmp $fn'
 echo 'done'
 echo 'find debian -name '\''*.install'\'' | while read fn'
 echo 'do'
 echo ' awk '\''{'
 echo ' if (NF == 2 && $2 == "usr/include") $2 = $2"/${DEB_HOST_MULTIARCH}"'
 echo ' if (NF == 1 && $1 == "usr/include") { $2 = $1"/${DEB_HOST_MULTIARCH}"; $1 = $1"/*" }'
 echo ' print'
 echo ' }'\'' < $fn > $fn.tmp'
 echo ' mv $fn.tmp $fn'
 echo 'done'
) > $HOME/bin/fillet
chmod 755 $HOME/bin/fillet

And now let's try building a small package:

mkdir -p ~/shared/packages
cd ~/shared/packages
apt source tinycdb
cd tinycdb-*/
$HOME/bin/fillet
time env DPKG_GENSYMBOLS_CHECK_LEVEL=0 \
 DEB_BUILD_OPTIONS='crossbuildcanrunhostbinaries nostrip' \
 dpkg-buildpackage -d -us -uc -b -a amd64fil0

Explanation of the differences from a normal build:

* DEB_BUILD_OPTIONS=nostripskips removing symbols from binaries,
in part because Debian'sdh_dwzutility doesn't currently work with Fil-C,
in part because we'll look at symbols later.
* DEB_BUILD_OPTIONS=crossbuildcanrunhostbinariessilences a warning
about cross-compilation not necessarily working with tests.
* -a amd64fil0specifies theamd64fil0ABI,
which triggers using thex86_64+fil0-linux-gnu-gcccompiler.
* -dstopsdpkg-buildpackagefrom checking for dependencies.
(This doesn't matter for this package.)
* [Superseded by thebinutilspatch in infilian-install-compilerstarting with version 20251030:]
The tweak to*.mapin the helper script
tries to stop Debian from hiding the shared-library symbols after Fil-C mangling.
* The tweak to*.symbolsin the helper script
tries to notify Debian regarding the expected shared-library symbols after Fil-C mangling.
[Not necessary givenDPKG_GENSYMBOLS_CHECK_LEVEL=0.]
* DPKG_GENSYMBOLS_CHECK_LEVEL=0should stop Debian from complaining that there are wrong symbols.
* [Not necessary if you've usedfilian-install-compiler:]
The tweak to*.installin the helper script
installs/usr/include/x86_64+fil0/cdb.h(where Fil-C will see it for programs using this library)
instead of/usr/include/cdb.h.

For me this worked and produced three../*.debpackages.
Installing them as root also worked:

apt install /home/filian/shared/packages/*.deb
# some sanity checks:
apt list | grep tinycdb
# prints "tinycdb/stable 0.81-2 amd64" (available package)
# and prints "tinycdb/now 0.81-2 amd64fil0 [installed,local]"
dpkg -L tinycdb:amd64fil0
# lists various files such as /usr/bin/cdb
nm /usr/bin/cdb
# shows various symbols including "pizlonated" (Fil-C) symbols
ldd /usr/bin/cdb
# shows dependence on libraries in /usr/libexec/fil
/usr/bin/cdb -h
# prints a help message: "cdb: Constant DataBase" etc.

Compiling a deliberately wrong test program
with the newly installed library also works,
and triggers Fil-C's run-time protection:

cd /root
( echo '#include <cdb.h>'
 echo 'int main() { cdb_init(0,0); return 0; }' ) > usecdb.c
filcc -o usecdb usecdb.c -lcdb
./usecdb < /bin/bash
# ... "filc panic: thwarted a futile attempt to violate memory safety."

## More Debian packages

libc-dev.Some packages depend on libc-dev,
so let's build a fake libc-dev package
(probably there's an easier way to do this):

FAKEPACKAGE=libc-dev
mkdir -p ~/shared/packages/$FAKEPACKAGE/debian
cd ~/shared/packages/$FAKEPACKAGE
( echo $FAKEPACKAGE' (0.0) unstable; urgency=medium'
 echo ''
 echo ' * Initial Release.'
 echo ''
 echo ' -- djb <djb@cr.yp.to> Sun, 26 Oct 2025 16:05:17 +0000'
) > debian/changelog
( echo 'Source: '$FAKEPACKAGE
 echo 'Build-Depends: debhelper-compat (= 13)'
 echo 'Maintainer: djb
'
 echo ''
 echo 'Package: '$FAKEPACKAGE
 echo 'Architecture: any'
 echo 'Multi-Arch: same'
 echo 'Description: fake '$FAKEPACKAGE
) > debian/control
( echo '#!/usr/bin/make -f'
 echo ''
 echo 'build-arch build-indep build \'
 echo 'install-arch install-indep install \'
 echo 'binary-arch binary-indep binary \'
 echo ':'
 echo 'Xdh $@' | tr X '\011'
 echo ''
 echo 'clean:'
 echo 'Xdh_clean' | tr X '\011'
) > debian/rules
time env DPKG_GENSYMBOLS_CHECK_LEVEL=0 \
 DEB_BUILD_OPTIONS='crossbuildcanrunhostbinaries nostrip' \
 dpkg-buildpackage -d -us -uc -b -a amd64fil0

ncurses.

mkdir -p ~/shared/packages
cd ~/shared/packages
apt source ncurses
cd ncurses-*/
$HOME/bin/fillet
time env DPKG_GENSYMBOLS_CHECK_LEVEL=0 \
 DEB_BUILD_OPTIONS='crossbuildcanrunhostbinaries nostrip' \
 dpkg-buildpackage -d -us -uc -b -a amd64fil0
rm ../ncurses-*deb # apt won't let us touch the binaries

As root, install the above libraries:

apt install /home/filian/shared/packages/lib*.deb

libmd.Seems to work.
At first this didn't install
since the compiled version (for amd64fil0) was 1.1.0-2
while the installed version (for amd64) was 1.1.0-2+b1.
Debian requires the same version number across architectures
(see above regarding include-file compatibility),
soaptsaid that 1.1.0-2+b1 breaks 1.1.0-2.
I resolved this by compiling and installing 1.1.0-2 for both amd64 and amd64fil0.
This is a downgrade since "+b" refers to
a "binNMU", a "binary-only non-maintainer upload",
a patch beyond the official source;
I don't know what the patch is.

readline.Needsln -s /usr/include/readline /usr/include/x86_64+fil0-linux-gnu/readlineafter installation.
Could have tweaks indebian/rules(which seems to predate*.install),
but this is in any case an example of the messiness that I'm planning to get rid of.

lua5.4.Seems to work.
Depends on readline.

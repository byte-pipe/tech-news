---
title: 'GitHub - php/php-src: The PHP Interpreter · GitHub'
url: https://github.com/php/php-src
site_name: github
content_file: github-github-phpphp-src-the-php-interpreter-github
fetched_at: '2026-10-22T16:04:27.640851'
original_url: https://github.com/php/php-src
author: php
description: The PHP Interpreter. Contribute to php/php-src development by creating an account on GitHub.
---

master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

149,513 Commits
149,513 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.circleci
.circleci
 
 
.github
.github
 
 
TSRM
TSRM
 
 
Zend
Zend
 
 
benchmark
benchmark
 
 
build
build
 
 
docs-old
docs-old
 
 
docs
docs
 
 
ext
ext
 
 
main
main
 
 
pear
pear
 
 
sapi
sapi
 
 
scripts
scripts
 
 
tests
tests
 
 
win32
win32
 
 
.editorconfig
.editorconfig
 
 
.gdbinit
.gdbinit
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CODING_STANDARDS.md
CODING_STANDARDS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
EXTENSIONS
EXTENSIONS
 
 
LICENSE
LICENSE
 
 
NEWS
NEWS
 
 
README.REDIST.BINS
README.REDIST.BINS
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
UPGRADING
UPGRADING
 
 
UPGRADING.INTERNALS
UPGRADING.INTERNALS
 
 
buildconf
buildconf
 
 
buildconf.bat
buildconf.bat
 
 
configure.ac
configure.ac
 
 
gcovr.cfg
gcovr.cfg
 
 
php.ini-development
php.ini-development
 
 
php.ini-production
php.ini-production
 
 
run-extra-tests.php
run-extra-tests.php
 
 
run-tests.php
run-tests.php
 
 
View all files

## Repository files navigation

# The PHP Interpreter

PHP is a popular general-purpose scripting language that is especially suited to
web development. Fast, flexible and pragmatic, PHP powers everything from your
blog to the most popular websites in the world.

PHP is distributed under theModified BSD License(SPDX-License-Identifier:BSD-3-Clause).

## Documentation

The PHP manual is available atphp.net/docs.

## Installation

### Prebuilt packages and binaries

Prebuilt packages and binaries can be used to get up and running fast with PHP.

For Windows, the PHP binaries can be obtained fromwindows.php.net. After extracting the archive the*.exefiles are ready to use.

For other systems, see theinstallation chapter.

### Building PHP source code

For Windows, seeBuild your own PHP on Windows.

For a minimal PHP build from Git, you will need autoconf, bison, and re2c. For
a default build, you will additionally need libxml2 and libsqlite3.

On Ubuntu, you can install these using:

sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev

On Fedora, you can install these using:

sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel

On MacOS, you can install these usingbrew:

brew install autoconf bison re2c libiconv libxml2 sqlite

or withMacPorts:

sudo port install autoconf bison re2c libiconv libxml2 sqlite3

Generate configure:

./buildconf

Configure your build.--enable-debugis recommended for development, see./configure --helpfor a full list of options.

#
 For development

./configure --enable-debug

#
 For production

./configure

Build PHP. To speed up the build, specify the maximum number of jobs using the-jargument:

make -j4

The number of jobs should usually match the number of available cores, which
can be determined usingnproc.

## Testing PHP source code

PHP ships with an extensive test suite, the commandmake testis used after
successful compilation of the sources to run this test suite.

Tests run in parallel by default, using up to 10 detected logical processors.
Set-jNinTEST_PHP_ARGSorTESTSto override the worker count:

make TEST_PHP_ARGS=-j4 
test

This runsmake testwith a maximum of 4 concurrent jobs. Alternatively,
use-j1to run tests sequentially.

Use theTEST_PHP_ARGSorTESTSvariable to test only specific directories:

make TESTS=tests/lang/ 
test

Theqa.php.netsite provides more detailed info about
testing and quality assurance.

## Installing PHP built from source

After a successful build (and test), PHP may be installed with:

make install

Depending on your permissions and prefix,make installmay need superuser
permissions.

## PHP extensions

Extensions provide additional functionality on top of PHP. PHP consists of many
essential bundled extensions. Additional extensions can be found on thePIE Extensionslist, and installed with🥧 PIE, the PHP Installer for Extensionsor the
deprecated PHP Extension Community Library -PECL.

## Contributing

The PHP source code is located in the Git repository atgithub.com/php/php-src. Contributions are most
welcome by forking the repository and sending a pull request.

Discussions are done on GitHub, but depending on the topic can also be relayed
to the official PHP developer mailing listinternals@lists.php.net.

New features require an RFC and must be accepted by the developers. SeeRequest for comments - RFCandVoting on PHP featuresfor more information
on the process.

Bug fixes don't require an RFC. If the bug has a GitHub issue, reference it in
the commit message usingGH-NNNNNN. Use#NNNNNNfor tickets in the oldbugs.php.netbug tracker.

Fix GH-7815: php_uname doesn't recognise latest Windows versions
Fix #55371: get_magic_quotes_gpc() throws deprecation warning

SeeGit workflowfor details on how pull
requests are merged.

### Guidelines for contributors

See further documents in the repository for more information on how to
contribute:

* Contributing to PHP
* PHP coding standards
* Internal documentation
* Mailing list rules
* PHP release process

## Credits

For the list of people who've put work into PHP, please see thePHP credits page.
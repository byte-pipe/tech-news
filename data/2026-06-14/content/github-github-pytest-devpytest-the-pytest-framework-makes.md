---
title: 'GitHub - pytest-dev/pytest: The pytest framework makes it easy to write small tests, yet scales to support complex functional testing · GitHub'
url: https://github.com/pytest-dev/pytest
site_name: github
content_file: github-github-pytest-devpytest-the-pytest-framework-makes
fetched_at: '2026-06-14T11:44:13.438237'
original_url: https://github.com/pytest-dev/pytest
author: pytest-dev
description: The pytest framework makes it easy to write small tests, yet scales to support complex functional testing - pytest-dev/pytest
---

pytest-dev

 

/

pytest

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3.2k
* Star13.9k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

17,439 Commits
17,439 Commits
.github
.github
 
 
bench
bench
 
 
changelog
changelog
 
 
doc/
en
doc/
en
 
 
extra
extra
 
 
scripts
scripts
 
 
src
src
 
 
testing
testing
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mailmap
.mailmap
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.readthedocs.yaml
.readthedocs.yaml
 
 
AUTHORS
AUTHORS
 
 
CHANGELOG.rst
CHANGELOG.rst
 
 
CITATION
CITATION
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.rst
CONTRIBUTING.rst
 
 
LICENSE
LICENSE
 
 
OPENCOLLECTIVE.rst
OPENCOLLECTIVE.rst
 
 
README.rst
README.rst
 
 
RELEASING.rst
RELEASING.rst
 
 
SECURITY.md
SECURITY.md
 
 
TIDELIFT.rst
TIDELIFT.rst
 
 
codecov.yml
codecov.yml
 
 
pyproject.toml
pyproject.toml
 
 
tox.ini
tox.ini
 
 
View all files

## Repository files navigation

Thepytestframework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

An example of a simple test:

# content of test_sample.py

def
 
inc
(
x
):
 
return
 
x
 
+
 
1

def
 
test_answer
():
 
assert
 
inc
(
3
) 
==
 
5

To execute it:

$ pytest
============================= test session starts =============================
collected 1 items

test_sample.py F

================================== FAILURES ===================================
_________________________________ test_answer _________________________________

 def test_answer():
> assert inc(3) == 5
E assert 4 == 5
E + where 4 = inc(3)

test_sample.py:5: AssertionError
========================== 1 failed in 0.04 seconds ===========================

Thanks topytest's detailed assertion introspection, you can simply use plainassertstatements. Seegetting-startedfor more examples.

## Features

* Detailed info on failingassert statements(no need to rememberself.assert*names)
* Auto-discoveryof test modules and functions
* Modular fixturesfor
managing small or parametrized long-lived test resources
* Can rununittest(or trial)
test suites out of the box
* Python 3.10+ or PyPy3
* Rich plugin architecture, with over 1300+external pluginsand thriving community

## Documentation

For full documentation, including installation, tutorials and PDF documents, please seehttps://docs.pytest.org/en/stable/.

## Bugs/Requests

Please use theGitHub issue trackerto submit bugs or request features.

## Changelog

Consult theChangelogpage for fixes and enhancements of each version.

## Support pytest

Open Collectiveis an online funding platform for open and transparent communities.
It provides tools to raise money and share your finances in full transparency.

It is the platform of choice for individuals and companies that want to make one-time or
monthly donations directly to the project.

See more details in thepytest collective.

## pytest for enterprise

Available as part of the Tidelift Subscription.

The maintainers of pytest and thousands of other packages are working with Tidelift to deliver commercial support and
maintenance for the open source dependencies you use to build your applications.
Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use.

Learn more.

### Security

If you have found an issue that you believe is a security vulnerability, please do not create an issue -- instead, report it via anew security advisory.

## License

Copyright Holger Krekel and others, 2004.

Distributed under the terms of theMITlicense, pytest is free and open source software.

## About

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing

pytest.org

### Topics

 python

 testing

 unit-testing

 test

 hacktoberfest

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

13.9k

 stars
 

### Watchers

197

 watching
 

### Forks

3.2k

 forks
 

 Report repository

 

## Releases83

9.1.0

 Latest

 

Jun 13, 2026

 

+ 82 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* tidelift.com/funding/github/pypi/pytest
* opencollective.com/pytest
* thanks.dev/u/gh/pytest-dev

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%
---
title: Sarah's website - Conventional Commits makes me sad
url: https://srazkvt.codeberg.page/posts/2025-07-06-conventional-commits-makes-me-sad.html
site_name: lobsters
fetched_at: '2025-07-07T23:06:46.083047'
original_url: https://srazkvt.codeberg.page/posts/2025-07-06-conventional-commits-makes-me-sad.html
date: '2025-07-07'
tags: practices, vcs
---

# Conventional Commits makes me sad

 Posted on July 6, 2025



I started this post by writing that this was going to be a
shorter than usual post, but it turned out to be my longest one
yet. In fact, larger than the two previous posts combined.
Funny.

## What I don’t like in the spec

1. Commits MUST be prefixed with a type, which consists of a noun, feat, fix, etc., followed by the OPTIONAL scope, OPTIONAL !, and REQUIRED terminal colon and space.

It’s worded a bit poorly, as a commit isn’t just its title, but
this isn’t the point I’m trying to make.

The type of a commit here is only really useful for automated
tools, usually the type can be inferred from the summary of the
commit. As such, I think the type would be better off as a
field in footer of commit, under a key such asCommit-TypeorType.

Also, the optional!here specifies there is a breaking
change.

1. A description MUST immediately follow the colon and space after the type/scope prefix. The description is a short summary of the code changes, e.g., fix: array parsing issue when multiple spaces were contained in string.

According to the git-commit manpage, it’s “a good idea to begin
the commit message with a single short (no more than 50
characters)”. This commit message lands at 71 characters.

Personally, I would have put something like “Fix array parsing
when input has multiple spaces”. Smaller, and also complies
with recommendations from the git documentation.

1. A footer’s token MUST use - in place of whitespace characters, e.g., Acked-by (this helps differentiate the footer section from a multi-paragraph body). An exception is made for BREAKING CHANGE, which MAY also be used as a token.

But why make an exception forBREAKING CHANGE? Why not have
it asBreaking-Change? It’s not like it adds or remove any
character, all that would change is it would stay consistent
with other keys.

1. If included in the type/scope prefix, breaking changes MUST be indicated by a ! immediately before the :. If ! is used, BREAKING CHANGE: MAY be omitted from the footer section, and the commit description SHALL be used to describe the breaking change.

Why would it be optional though ? This just makes it harder for
tools to find the actual reason of the breaking change, they’d
just know that there is one, and that the details are somewhere
in the description.

Also, breaking changes might not be found until after the
commit is pushed. In this case, it would be good to use agit
noteto add context to a
commit, without actually modifying it, so it doesn’t need to be
force pushed, and won’t confuse other developers.

## What I don’t like on the website (specifically the FAQ)

Ok so badly named section, but, I do like parts of the website
(and of the FAQ).

However, some trip me up in the wrong way.

What do I do if I accidentally use the wrong commit type?

When you used a type that’s of the spec but not the correct type, e.g. fix instead of feat

Prior to merging or releasing the mistake, we recommend using git rebase -i to edit the commit history. After release, the cleanup will be different according to what tools and processes you use.

That’s it;

Runninggit rebase -iwill leave you in a text editor, and
while there are instructions in the file that will be opened,
I generally prefer to have instructions listed. That, or
linking to another website that has them, such asthe git
docs.

Also, rebase isn’t necessary if the commit that needs its
message modified is the last one, then, as listed in the above
link, the command to run isgit comit --amend.

A common workflow for this is to have your git system automatically squash commits from a pull request and present a form for the lead maintainer to enter the proper git commit message for the merge.

I don’t think this is good advice. Squash merge will combine
every commit in the pull request into a single one. But doing
so leads to loss of information (as some commits would be
better off seperated, but aren’t anymore), and most
importantly, will need splitting afterwards in certain cases
(such as if a refactor happened alongside a feature addition,
then, as stated in an earlier statement answer of the FAQ, you
should “Go back and make multiple commits whenever possible.”).

## Final words

I’m not fundamentally against a standardisation of commit
messages, but Conventional Commits right now feels like it puts
human readable and machine readable at the same level, when it
should be human first, and machine compatible (which is also
why I dislike that you can decide to not put theBREAKING CHANGEfield if the commit has a breaking change,
and instead put the reason in the description, which makes the
information harder to reach for tools).
